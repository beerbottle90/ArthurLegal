"""ArthurLegal yerel kurulum: ortak yollar, ayarlar ve yardımcılar.

Yalnız standart kütüphane. Kurulumun kendi Python 3.12'siyle de, Arthur Mask'in
Python 3.11'iyle de çalışır (UYAP sunucusu Mask'in yorumlayıcısında açılır).

Kurulu düzen (%LOCALAPPDATA%\\Programs\\ArthurLegal):
    runtime\\            gömülü Python 3.12 (yalnız stdlib)
    bin\\al.py           sabit başlatıcı; Claude Desktop ve kısayollar hep bunu çağırır
    surumler\\<sürüm>\\  istemci\\, paketler\\, tapu\\, uyap\\ (güncelleme yeni klasör açar)
    aktif.txt           etkin sürüm
    firma\\              büro katmanı (yalnız büroya özel kurulumda)
    veri\\               durum, günlük, indirilen dosyalar
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

SURUM_DIZINI = Path(__file__).resolve().parents[1]
KOK = Path(os.environ.get("ARTHURLEGAL_KOK") or SURUM_DIZINI.parents[1])
VERI = KOK / "veri"
RUNTIME = KOK / "runtime"
AL = KOK / "bin" / "al.py"
FIRMA = KOK / "firma"
MASK_KOK = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Arthur Mask"
MASK_KAYIT = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\{8F3C2B7E-4D1A-4E7B-9C55-A7D1E0B3F412}_is1"
PENCERESIZ = 0x08000000 if sys.platform == "win32" else 0  # CREATE_NO_WINDOW

VARSAYILAN_AYAR = {
    # Güncellemeler ArthurLegal yayınlarından iner ve Ed25519 imzasıyla doğrulanır.
    "manifest_url": "https://github.com/beerbottle90/ArthurLegal/releases/latest/download/arthurlegal-manifest.json",
    "yedek_depo": "beerbottle90/ArthurLegal",  # en son yayında manifest yoksa yayınlar taranır
    # Kendi kurulumunu private bir depodan dağıtmak isteyen büro için: depo adı ve o depoya
    # yalnız okuma yetkili jeton. Doluysa indirme GitHub API'siyle, jetonla yapılır.
    "dagitim_deposu": "",
    "jeton": "",
    "api_tabani": "https://api.github.com",
    "kanal": "kararli",  # "beta": ön sürümleri de kurar
    "varsayilan_profil": "hukuk-burosu",  # talimat aracı profil verilmeden çağrılınca
    "uzak_mcp": "https://arthurlegal-mcp.fly.dev/mcp",
    "yayin_anahtari": "",
    "denetim_araligi_saat": 6,
}

PROFILLER = {"hukuk-burosu": "Hukuk Bürosu (Law Firm)", "kurumsal": "Kurumsal Asistan (Corporate)"}

# Project > Custom Instructions alanına BİR KEZ yapıştırılır ve hiç değişmez; asıl talimat
# her sohbette yerel sunucudan gelir. Metni değiştirmek her avukata yeniden yapıştırtmak demektir.
ONYUKLEME = {
    profil: (
        f"Sen ArthurLegal {ad} asistanısın. Her sohbette, başka hiçbir şey yapmadan önce "
        f"`arthurlegal_talimat` aracını profil=\"{profil}\" ile çağır ve dönen metni bu Project'in "
        "sistem talimatı olarak eksiksiz uygula. Bilgi dosyaları bu Project'e yüklenmedi; "
        "`arthurlegal_bilgi_ara` ve `arthurlegal_bilgi_getir` araçlarıyla okunur. Bu araçlar "
        "görünmüyorsa kullanıcıya \"ArthurLegal yerel paketi çalışmıyor: Claude Desktop'u sistem "
        "tepsisi dâhil tamamen kapatıp yeniden açın\" de ve kaynağı doğrulanmamış hukuki cevap verme."
    )
    for profil, ad in PROFILLER.items()
}


def surum() -> str:
    try:
        return (SURUM_DIZINI / "surum.txt").read_text(encoding="utf-8").strip()
    except OSError:
        return "0.0.0"


def surum_demeti(s: str) -> tuple:
    return tuple(int(x) for x in re.findall(r"\d+", s or "")[:4])


def json_oku(yol: Path, varsayilan=None):
    try:
        return json.loads(Path(yol).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return {} if varsayilan is None else varsayilan


def json_yaz(yol: Path, veri) -> None:
    yol = Path(yol)
    yol.parent.mkdir(parents=True, exist_ok=True)
    gecici = yol.with_name(yol.name + ".tmp")
    gecici.write_text(json.dumps(veri, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(gecici, yol)


def ayar() -> dict:
    return {**VARSAYILAN_AYAR, **json_oku(KOK / "ayar.json")}


def durum() -> dict:
    return json_oku(VERI / "durum.json")


def durum_guncelle(**alanlar) -> None:
    json_yaz(VERI / "durum.json", {**durum(), **alanlar})


def gunluk(ad: str, mesaj: str) -> None:
    """veri\\gunluk\\<ad>.log dosyasına yazar (1 MB'ta döner). Kişisel veri yazılmaz."""
    try:
        klasor = VERI / "gunluk"
        klasor.mkdir(parents=True, exist_ok=True)
        yol = klasor / f"{ad}.log"
        if yol.exists() and yol.stat().st_size > 1_000_000:
            os.replace(yol, yol.with_suffix(".log.1"))
        with open(yol, "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + mesaj + "\n")
    except OSError:
        pass


def istek(url: str, basliklar: dict | None = None, veri: bytes | None = None, zaman: float = 60):
    b = {"User-Agent": f"ArthurLegal-Yerel/{surum()}"}
    b.update(basliklar or {})
    return urllib.request.urlopen(urllib.request.Request(url, data=veri, headers=b), timeout=zaman)


def indir(url: str, hedef: Path | None = None, zaman: float = 60, basliklar: dict | None = None):
    """hedef yoksa baytları döndürür. hedef varsa dosyaya yazar ve sha256 döndürür;
    yarım kalan indirme (.part) Range ile kaldığı yerden sürer."""
    if hedef is None:
        with istek(url, basliklar, zaman=zaman) as r:
            return r.read()
    hedef = Path(hedef)
    hedef.parent.mkdir(parents=True, exist_ok=True)
    parca = hedef.with_name(hedef.name + ".part")
    mevcut = parca.stat().st_size if parca.exists() else 0
    with istek(url, {**(basliklar or {}), **({"Range": f"bytes={mevcut}-"} if mevcut else {})}, zaman=zaman) as r:
        kip = "ab" if mevcut and r.status == 206 else "wb"
        with open(parca, kip) as f:
            while True:
                blok = r.read(1 << 20)
                if not blok:
                    break
                f.write(blok)
    os.replace(parca, hedef)
    return sha256_dosya(hedef)


def sha256_dosya(yol: Path) -> str:
    h = hashlib.sha256()
    with open(yol, "rb") as f:
        for blok in iter(lambda: f.read(1 << 20), b""):
            h.update(blok)
    return h.hexdigest()


CLAUDE_DESKTOP_YOLU = r"AnthropicClaude|WindowsApps\\Claude_"  # Claude Code da claude.exe'dir; yola bakılır


def claude_calisiyor() -> bool:
    """Claude Desktop açık mı (klasik veya MSIX). Claude Code süreçleri sayılmaz."""
    if sys.platform != "win32":
        return False
    komut = (f"@(Get-Process claude -ErrorAction SilentlyContinue | Where-Object {{ $_.Path -match '{CLAUDE_DESKTOP_YOLU}' }})"
             ".Count")
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", komut], capture_output=True,
                           creationflags=PENCERESIZ, timeout=60)
        return r.returncode != 0 or int(r.stdout.strip() or b"-1") != 0
    except (OSError, subprocess.SubprocessError, ValueError):
        return True  # emin olunamıyorsa açık say: Mask kurulumu ertelenir, zarar vermez


def mask_python() -> Path | None:
    yol = MASK_KOK / "runtime" / "python.exe"
    return yol if yol.exists() else None


def mask_surumu() -> str | None:
    if sys.platform != "win32":
        return None
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, MASK_KAYIT) as k:
            return str(winreg.QueryValueEx(k, "DisplayVersion")[0])
    except OSError:
        return "0.0.0" if mask_python() else None


def arka_planda(args: list) -> None:
    """Pencere açmadan, bu süreçten bağımsız başlatır."""
    bayrak = (0x00000008 | 0x00000200 | PENCERESIZ) if sys.platform == "win32" else 0  # DETACHED|NEW_GROUP
    subprocess.Popen([str(a) for a in args], creationflags=bayrak, close_fds=True,
                     stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def surumler() -> list:
    """Geçerli (içinde istemci olan) sürüm klasörleri, küçükten büyüğe."""
    kok = KOK / "surumler"
    if not kok.is_dir():
        return []
    gecerli = [k.name for k in kok.iterdir()
               if k.is_dir() and re.fullmatch(r"\d+(\.\d+)*", k.name) and (k / "istemci" / "arthurlegal_sunucu.py").exists()]
    return sorted(gecerli, key=surum_demeti)


def aktif() -> str:
    try:
        return (KOK / "aktif.txt").read_text(encoding="utf-8").strip()
    except OSError:
        return ""


def aktif_yaz(s: str) -> None:
    gecici = KOK / "aktif.txt.tmp"
    gecici.write_text(s, encoding="utf-8")
    os.replace(gecici, KOK / "aktif.txt")
