"""Claude Desktop yapılandırmasına ArthurLegal sunucularını ekler ve kaldırır.

Arthur Mask'in claude_ayari.py'si örnek alındı: klasik (%APPDATA%\\Claude) ve Microsoft
Store/MSIX (Packages\\Claude_*\\LocalCache\\Roaming\\Claude) yapılandırmalarının hepsine
yazar, Claude'un kendi alanlarına (preferences vb.) dokunmaz, değiştirmeden önce yedek alır.
`arthur-mask` girdisini Arthur Mask'in kendi kurulumu yönetir; burada ona dokunulmaz.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

import ortak

ADLAR = ("arthurlegal-yerel", "arthur-tapu", "arthur-uyap")
YEDEK_ONEKI = "claude_desktop_config.arthurlegal-yedek-"


def yapilandirma_yollari() -> list:
    yollar = []
    if os.environ.get("APPDATA"):
        yollar.append(Path(os.environ["APPDATA"]) / "Claude" / "claude_desktop_config.json")
    if os.environ.get("LOCALAPPDATA"):
        for paket in sorted((Path(os.environ["LOCALAPPDATA"]) / "Packages").glob("Claude_*")):
            yollar.append(paket / "LocalCache" / "Roaming" / "Claude" / "claude_desktop_config.json")
    return yollar


def istenen_girdiler() -> dict:
    py = str(ortak.RUNTIME / "python.exe")
    al = str(ortak.AL)
    env = {"PYTHONIOENCODING": "utf-8", "PYTHONDONTWRITEBYTECODE": "1"}
    girdiler = {
        "arthurlegal-yerel": {"command": py, "args": ["-B", al, "sunucu"], "env": dict(env)},
        "arthur-tapu": {"command": py, "args": ["-B", al, "tapu", "--ui-ile"], "env": dict(env)},
    }
    mask = ortak.mask_python()
    # UYAP yalnız bu kurulumda varsa ve Arthur Mask kuruluysa kaydedilir: maskelemeyi atlayamaz,
    # arthur_mask olmadan veri döndürmez, o yüzden Mask'in Python'unda çalışır.
    if mask and (ortak.SURUM_DIZINI / "uyap" / "server.py").exists():
        girdiler["arthur-uyap"] = {"command": str(mask), "args": ["-B", al, "uyap"],
                                   "env": {**env, "HF_HUB_OFFLINE": "1", "PYTHONNOUSERSITE": "1"}}
    return girdiler


def _oku(yol: Path) -> dict:
    if not yol.exists():
        return {}
    metin = yol.read_text(encoding="utf-8-sig")
    return json.loads(metin) if metin.strip() else {}


def _yaz(yol: Path, veri: dict) -> None:
    if yol.exists():
        shutil.copy2(yol, yol.with_name(YEDEK_ONEKI + datetime.now().strftime("%Y%m%d-%H%M%S") + ".json"))
        for eski in sorted(yol.parent.glob(YEDEK_ONEKI + "*.json"))[:-5]:  # son 5 yedek kalır
            eski.unlink(missing_ok=True)
    ortak.json_yaz(yol, veri)


def _uygula(degistir) -> list:
    tum = yapilandirma_yollari()
    hedefler = [y for y in tum if y.parent.exists()] or tum[:1]
    degisen = []
    for yol in hedefler:
        try:
            veri = _oku(yol)
        except (json.JSONDecodeError, OSError) as e:
            ortak.gunluk("kurulum", f"{yol} okunamadı, dokunulmadı: {e}")
            continue
        sunucular = veri.setdefault("mcpServers", {})
        if degistir(sunucular):
            _yaz(yol, veri)
            degisen.append(yol)
    return degisen


def kaydet() -> list:
    """Eksik ya da farklı girdileri yazar; Mask kaldırılmışsa UYAP girdisini siler. Değişen dosyaları döndürür."""
    istenen = istenen_girdiler()

    def degistir(sunucular):
        degisti = False
        for ad in ADLAR:
            if ad in istenen and sunucular.get(ad) != istenen[ad]:
                sunucular[ad] = istenen[ad]
                degisti = True
            elif ad not in istenen and ad in sunucular:
                del sunucular[ad]
                degisti = True
        return degisti

    return _uygula(degistir)


def sil() -> list:
    def degistir(sunucular):
        var = [ad for ad in ADLAR if ad in sunucular]
        for ad in var:
            del sunucular[ad]
        return bool(var)

    return _uygula(degistir)


def kayitli() -> dict:
    return {str(y): sorted(_oku(y).get("mcpServers", {})) for y in yapilandirma_yollari() if y.exists()}


if __name__ == "__main__":
    komut = sys.argv[1] if len(sys.argv) > 1 else "durum"
    sonuc = kaydet() if komut == "kaydet" else sil() if komut == "sil" else kayitli()
    print(json.dumps(sonuc if isinstance(sonuc, dict) else [str(y) for y in sonuc], ensure_ascii=False, indent=2))
