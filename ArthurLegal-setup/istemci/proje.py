"""Claude Desktop "Use a folder" yolu için hazır proje klasörleri.

Kurulum %USERPROFILE%\\ArthurLegal\\ altında her paket için bir klasör açar (Hukuk Bürosu, Kurumsal).
Kullanıcı Claude'da proje oluştururken "Use a folder" ile bu klasörü seçer; talimat ve bilgi dosyaları
klasörden gelir. Yerel araçlar (arthurlegal-yerel) çalışıyorsa CLAUDE.md önce onları kullandırır.

Yönetilen içerik: CLAUDE.md, SYSTEM_PROMPT.md, knowledge/, buro/. Güncelleyici bunları etkin sürümden
yeniler; kullanıcının klasöre koyduğu başka dosyalara dokunmaz. Kaldırmada yalnız yönetilen içerik
silinir, klasör boş kalırsa o da silinir.
"""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

import ortak

KLASOR_ADLARI = {"hukuk-burosu": "Hukuk Bürosu", "kurumsal": "Kurumsal"}
YONETILEN = ("CLAUDE.md", "SYSTEM_PROMPT.md", "knowledge", "buro", ".arthurlegal.json")


def kok() -> Path:
    return Path(os.environ.get("ARTHURLEGAL_PROJE_KOKU") or Path(os.environ.get("USERPROFILE", Path.home())) / "ArthurLegal")


def klasorler() -> dict:
    return {profil: kok() / ad for profil, ad in KLASOR_ADLARI.items()}


def _claude_md(profil: str, surum: str, firma: str) -> str:
    ad = ortak.PROFILLER[profil]
    buro = ("\nBüro kuralları `buro/` klasöründedir; paketle çelişirse büro kuralı geçerlidir.\n" if firma else "")
    return (
        f"# ArthurLegal — {ad}\n\n"
        f"Bu klasör ArthurLegal {ad} asistanının proje klasörüdür (paket {surum}"
        + (f", büro: {firma}" if firma else "") + ").\n\n"
        "1. `arthurlegal_talimat` aracı görünüyorsa, cevap vermeden önce onu "
        f"profil=\"{profil}\" ile çağır ve dönen metni bu projenin sistem talimatı olarak uygula.\n"
        "2. Araç görünmüyorsa bu klasördeki `SYSTEM_PROMPT.md` dosyasını oku ve sistem talimatı olarak uygula.\n"
        "3. Talimatta adı geçen `knowledge/...` dosyaları bu klasörün `knowledge/` alt klasöründedir; "
        "gerektiğinde oradan oku, okumadığın dosyanın içeriğini varsayma.\n"
        "4. `CLAUDE.md`, `SYSTEM_PROMPT.md`, `knowledge/` ve `buro/` ArthurLegal güncelleyicisi tarafından "
        "yönetilir ve her sürümde yenilenir; bunları değiştirme. Taslak ve çalışma dosyalarını `calismalar/` "
        "alt klasörüne yaz.\n" + buro
    )


def esitle(zorla: bool = False) -> list:
    """Etkin sürümün paketlerini proje klasörlerine yazar. Sürüm değişmediyse dokunmaz."""
    surum_dizini = ortak.SURUM_DIZINI
    icerik = ortak.json_oku(surum_dizini / "icerik.json")
    firma = ortak.json_oku(ortak.FIRMA / "firma.json").get("ad", "")
    yazilan = []
    for profil, hedef in klasorler().items():
        paket = surum_dizini / "paketler" / profil
        if not (paket / "SYSTEM_PROMPT.md").exists():
            continue
        paket_surumu = icerik.get("paketler", {}).get(profil, "?")
        isaret = {"kurulum": ortak.surum(), "paket": paket_surumu, "firma": firma}
        if not zorla and ortak.json_oku(hedef / ".arthurlegal.json") == isaret:
            continue
        hedef.mkdir(parents=True, exist_ok=True)
        for ad in YONETILEN:
            _sil(hedef / ad)
        shutil.copy2(paket / "SYSTEM_PROMPT.md", hedef / "SYSTEM_PROMPT.md")
        shutil.copytree(paket / "knowledge", hedef / "knowledge")
        if (ortak.FIRMA / "knowledge").is_dir():  # büro katmanı paketteki şablonların yerine geçer
            shutil.copytree(ortak.FIRMA / "knowledge", hedef / "knowledge", dirs_exist_ok=True)
        if (ortak.FIRMA / "buro").is_dir():
            shutil.copytree(ortak.FIRMA / "buro", hedef / "buro")
        (hedef / "calismalar").mkdir(exist_ok=True)
        (hedef / "CLAUDE.md").write_text(_claude_md(profil, paket_surumu, firma), encoding="utf-8")
        ortak.json_yaz(hedef / ".arthurlegal.json", isaret)
        yazilan.append(hedef)
    if yazilan:
        ortak.gunluk("kurulum", f"proje klasörleri güncellendi: {', '.join(p.name for p in yazilan)}")
    return yazilan


def kaldir() -> None:
    for hedef in klasorler().values():
        if not hedef.is_dir():
            continue
        for ad in YONETILEN:
            _sil(hedef / ad)
        calisma = hedef / "calismalar"
        if calisma.is_dir() and not any(calisma.iterdir()):
            calisma.rmdir()
        if not any(hedef.iterdir()):
            hedef.rmdir()
    if kok().is_dir() and not any(kok().iterdir()):
        kok().rmdir()


def _sil(yol: Path) -> None:
    if yol.is_dir():
        shutil.rmtree(yol, ignore_errors=True)
    elif yol.exists():
        yol.unlink()


def durum() -> dict:
    return {profil: str(hedef) for profil, hedef in klasorler().items() if (hedef / "SYSTEM_PROMPT.md").exists()}


if __name__ == "__main__":
    print(json.dumps([str(p) for p in esitle(zorla=True)], ensure_ascii=False))
