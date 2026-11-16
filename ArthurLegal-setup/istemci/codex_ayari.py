"""ChatGPT masaüstü uygulamasına (Codex) ArthurLegal sunucularını ve becerilerini ekler ve kaldırır (16.11.2026, K2/K21).

claude_ayari.py'nin karşılığıdır. ChatGPT masaüstü MCP sunucularını ~/.codex/config.toml'daki [mcp_servers.<ad>]
tablolarından okur (learn.chatgpt.com/docs/extend/mcp: command, args, env, cwd; startup_timeout_sec varsayılanı 10,
tool_timeout_sec 60), kullanıcı becerilerini ~/.codex/skills/<ad> altından (uygulamanın skill-installer becerisi:
$CODEX_HOME/skills). Windows'ta ve macOS'ta aynı yer; CODEX_HOME verilmişse orası.

Standart kütüphanede TOML yazıcısı yok (tomllib yalnız okur): dosya satır satır tablolara ayrılır, yalnız AL'nin
tabloları değiştirilir, öteki her satır (kullanıcının ayarları, yorumlar, başka sunucular) bayt bayt korunur.
Değiştirmeden önce yedek alınır (son 5). Kullanıcının uygulamadan kapattığı AL sunucusu (enabled = false) yeniden
yazılırken kapalı kalır.

ArthurMask'in kendi kurulumu yalnız Claude Desktop'a yazar; ChatGPT'deki `arthur-mask` girdisini bu modül yazar
(Mask'in kendi girdisiyle aynı komut). Beceriler: kurulum paketindeki chatgpt/skills (ArthurLegal-openai-plugin'den,
1 kural + 11 alan becerisi) ~/.codex/skills altına kopyalanır; yalnız ArthurLegal'in kurduğu klasörler (işaret
dosyasında listelenir) güncellenir ya da silinir.
"""
from __future__ import annotations

import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import claude_ayari
import ortak

ADLAR = ("arthurlegal-yerel", "arthur-tapu", "arthur-uyap", "arthur-mask")
YEDEK_ONEKI = "config.toml.arthurlegal-yedek-"
BECERI_ISARETI = ".arthurlegal-beceriler.json"
BECERI_ADI = re.compile(r"^arthurlegal(?:-[a-z0-9]+)*$")
MASK_KOPRU = "import sys; from arthur_mask.kopru import main; sys.exit(main())"
# Uzun işler (semantik arama, Resmî Gazete eki, Word revizyonu) ChatGPT'nin 60 sn'lik varsayılanını aşabilir.
SURE = {"arthurlegal-yerel": 120, "arthur-tapu": 120, "arthur-uyap": 120, "arthur-mask": 300}
ACILIS_SURESI = 30


def codex_evi() -> Path:
    return Path(os.environ.get("CODEX_HOME") or (Path.home() / ".codex"))


def yapilandirma_yolu() -> Path:
    return codex_evi() / "config.toml"


def beceri_hedefi() -> Path:
    return codex_evi() / "skills"


def beceri_kaynagi() -> Path:
    """Kurulum paketinde chatgpt/skills (derle.py koyar); kaynak ağacından çalışırken depodaki üretilmiş eklenti."""
    paket = ortak.SURUM_DIZINI / "chatgpt" / "skills"
    depo = ortak.SURUM_DIZINI.parent / "ArthurLegal-openai-plugin" / "skills"
    return paket if paket.is_dir() or not depo.is_dir() else depo


# --------------------------------------------------------------------------- girdiler

def istenen_girdiler() -> Dict[str, Dict]:
    """Claude'a yazılanların aynısı; yerel sunucu ChatGPT kipinde (AL_EV=chatgpt), Mask kuruluysa onun köprüsü."""
    girdiler = {}
    for ad, g in claude_ayari.istenen_girdiler().items():
        g = json.loads(json.dumps(g))
        if ad == "arthurlegal-yerel":
            g["env"]["AL_EV"] = "chatgpt"
        girdiler[ad] = g
    mask = ortak.mask_python()
    if mask:
        bayraklar = ["-I", "-B"] if ortak.MAC else []
        girdiler["arthur-mask"] = {"command": str(mask), "args": [*bayraklar, "-c", MASK_KOPRU],
                                   "env": {"PYTHONIOENCODING": "utf-8", "HF_HUB_OFFLINE": "1", "PYTHONNOUSERSITE": "1"}}
    for ad, g in girdiler.items():
        g["startup_timeout_sec"] = ACILIS_SURESI
        g["tool_timeout_sec"] = SURE.get(ad, 120)
    return girdiler


# --------------------------------------------------------------------------- TOML

_BASLIK = re.compile(r"^\s*\[(?!\[)\s*([^\]]+?)\s*\]\s*(?:#.*)?$")


def dizgi(s: str) -> str:
    """TOML dizgisi: tek tırnaklı (literal) yazım Windows yolunu kaçışsız taşır; içinde ' ya da satır sonu varsa
    çift tırnaklı (temel) yazım."""
    if "'" not in s and "\n" not in s and "\r" not in s:
        return "'%s'" % s
    return json.dumps(s, ensure_ascii=False)


def _anahtar_yolu(baslik: str) -> List[str]:
    parcalar, simdiki, tirnak = [], "", None
    for c in baslik:
        if tirnak:
            if c == tirnak:
                tirnak = None
            else:
                simdiki += c
        elif c in "\"'":
            tirnak = c
        elif c == ".":
            parcalar.append(simdiki.strip())
            simdiki = ""
        else:
            simdiki += c
    parcalar.append(simdiki.strip())
    return parcalar


def bloklar(metin: str) -> List[Tuple[Optional[List[str]], str]]:
    """(tablo anahtar yolu ya da None (en baştaki tablosuz kısım), bloğun ham metni) listesi."""
    out: List[Tuple[Optional[List[str]], str]] = []
    yol: Optional[List[str]] = None
    tampon: List[str] = []
    for satir in metin.splitlines(keepends=True):
        m = _BASLIK.match(satir.rstrip("\r\n"))
        if m:
            out.append((yol, "".join(tampon)))
            yol, tampon = _anahtar_yolu(m.group(1)), [satir]
        else:
            tampon.append(satir)
    out.append((yol, "".join(tampon)))
    return out


def _tablo(ad: str, g: Dict, enabled: Optional[str], ss: str) -> str:
    s = ["[mcp_servers.%s]" % ad, "command = %s" % dizgi(g["command"]),
         "args = [%s]" % ", ".join(dizgi(a) for a in g.get("args") or [])]
    if g.get("cwd"):
        s.append("cwd = %s" % dizgi(g["cwd"]))
    for k in ("startup_timeout_sec", "tool_timeout_sec"):
        if g.get(k):
            s.append("%s = %d" % (k, int(g[k])))
    if enabled is not None:
        s.append("enabled = %s" % enabled)
    if g.get("env"):
        s += ["", "[mcp_servers.%s.env]" % ad] + ["%s = %s" % (k, dizgi(str(v))) for k, v in sorted(g["env"].items())]
    return ss.join(s) + ss


def uygula(metin: str, girdiler: Dict[str, Dict], kaldirilacak=()) -> str:
    """girdiler yazılır, kaldirilacak silinir; öteki tablolar ve yorumlar aynen kalır."""
    ss = "\r\n" if "\r\n" in metin else "\n"
    adlar = set(girdiler) | set(kaldirilacak)
    kalan, acik, bulundu = [], {}, False
    for yol, ham in bloklar(metin):
        ad = yol[1] if yol and len(yol) >= 2 and yol[0] == "mcp_servers" and yol[1] in adlar else None
        if ad is None:
            kalan.append(ham)
            continue
        bulundu = True
        m = re.search(r"(?m)^\s*enabled\s*=\s*(true|false)\s*$", ham)
        if m and len(yol) == 2:
            acik[ad] = m.group(1)
    if not girdiler and not bulundu:   # silinecek bir şey yok: kullanıcının dosyasına dokunulmaz
        return metin
    govde = "".join(kalan).rstrip("\r\n")
    ekler = [_tablo(ad, girdiler[ad], acik.get(ad), ss) for ad in sorted(girdiler)]
    if not ekler:
        return govde + ss if govde else ""
    return (govde + ss + ss if govde else "") + ss.join(ekler)


def _oku() -> str:
    yol = yapilandirma_yolu()
    return yol.read_text(encoding="utf-8-sig") if yol.exists() else ""


def _yaz(metin: str) -> Path:
    yol = yapilandirma_yolu()
    yol.parent.mkdir(parents=True, exist_ok=True)
    if yol.exists():
        shutil.copy2(yol, yol.with_name(YEDEK_ONEKI + datetime.now().strftime("%Y%m%d-%H%M%S")))
        for eski in sorted(yol.parent.glob(YEDEK_ONEKI + "*"))[:-5]:   # son 5 yedek kalır
            eski.unlink(missing_ok=True)
    gecici = yol.with_name(yol.name + ".al-yaziliyor")
    gecici.write_bytes(metin.encode("utf-8"))
    os.replace(gecici, yol)
    return yol


def _gecerli(metin: str) -> bool:
    try:
        import tomllib
    except ImportError:   # Python < 3.11: denetim yapılamaz, yazılan metin yine aynı biçimde
        return True
    try:
        tomllib.loads(metin)
        return True
    except tomllib.TOMLDecodeError:
        return False


def _degistir(girdiler: Dict[str, Dict], kaldirilacak) -> List[Path]:
    try:
        eski = _oku()
    except OSError as e:
        ortak.gunluk("kurulum", f"ChatGPT ayarı okunamadı, dokunulmadı: {e}")
        return []
    if eski and not _gecerli(eski):
        ortak.gunluk("kurulum", "ChatGPT ayarı (config.toml) bozuk, dokunulmadı")
        return []
    yeni = uygula(eski, girdiler, kaldirilacak)
    if yeni == eski or not _gecerli(yeni):
        return []
    return [_yaz(yeni)]


def kaydet() -> List[Path]:
    """AL sunucularını yazar; bu kurulumda olmayan AL sunucularını siler. Değişen dosyaları döndürür."""
    girdiler = istenen_girdiler()
    return _degistir(girdiler, [ad for ad in ADLAR if ad not in girdiler])


def sil() -> List[Path]:
    eski = _oku() if yapilandirma_yolu().exists() else ""
    return _degistir({}, ADLAR) if eski else []


def kayitli() -> List[str]:
    try:
        import tomllib
        return sorted((tomllib.loads(_oku()).get("mcp_servers") or {}))
    except Exception:   # noqa: BLE001 — durum gösterimi için; okunamazsa boş
        return []


# --------------------------------------------------------------------------- beceriler

def _kurulu_beceriler() -> List[str]:
    try:
        veri = json.loads((beceri_hedefi() / BECERI_ISARETI).read_text(encoding="utf-8"))
        return [a for a in veri.get("beceriler", []) if BECERI_ADI.match(a)]
    except (OSError, ValueError):
        return []


def beceriler_kur() -> List[str]:
    """Paketteki becerileri ~/.codex/skills altına kurar (her klasör yeni kopyayla değişir); önceki kurulumdan kalıp
    pakette olmayan ArthurLegal becerisini kaldırır. Başkasının becerisine dokunmaz."""
    kaynak = beceri_kaynagi()
    if not kaynak.is_dir():
        return []
    hedef = beceri_hedefi()
    hedef.mkdir(parents=True, exist_ok=True)
    kurulan = []
    for d in sorted(kaynak.iterdir()):
        if not (d.is_dir() and BECERI_ADI.match(d.name) and (d / "SKILL.md").exists()):
            continue
        yeni, gecici = hedef / d.name, hedef / (d.name + ".al-yeni")
        shutil.rmtree(gecici, ignore_errors=True)
        shutil.copytree(d, gecici)
        if yeni.exists():
            shutil.rmtree(yeni)
        os.replace(gecici, yeni)
        kurulan.append(d.name)
    for eski in _kurulu_beceriler():
        if eski not in kurulan:
            shutil.rmtree(hedef / eski, ignore_errors=True)
    (hedef / BECERI_ISARETI).write_text(json.dumps({"beceriler": kurulan, "surum": ortak.surum()}, ensure_ascii=False),
                                        encoding="utf-8")
    return kurulan


def beceriler_sil() -> List[str]:
    silinen = []
    for ad in _kurulu_beceriler():
        if (beceri_hedefi() / ad).exists():
            shutil.rmtree(beceri_hedefi() / ad, ignore_errors=True)
            silinen.append(ad)
    (beceri_hedefi() / BECERI_ISARETI).unlink(missing_ok=True)
    return silinen


def beceriler_kayitli() -> List[str]:
    return [a for a in _kurulu_beceriler() if (beceri_hedefi() / a / "SKILL.md").exists()]
