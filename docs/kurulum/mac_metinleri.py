"""macOS'un kendi arayüz metinlerini Türkçe ve İngilizce olarak listeler: README'deki Mac çizimlerinin
(cizim_uret.py) yazıları buradan alınır, tahminle yazılmaz. Yalnız macOS'ta çalışır; GitHub Actions'ta
macos-kurulum.yml her derlemede çalıştırır, çıktı iş günlüğündedir.

    python3 docs/kurulum/mac_metinleri.py

Bakılan yerler: Installer (kurulum sihirbazı), CoreServicesUIAgent (açılışı engellenen dosya uyarısı) ve Sistem
Ayarları'nın Gizlilik ve Güvenlik bölümü. macOS 13'ten beri metinler .loctable dosyalarında (bütün diller tek
dosyada), daha eskilerde <dil>.lproj/*.strings dosyalarındadır; ikisi de okunur.
"""
from __future__ import annotations

import json
import plistlib
import platform
import subprocess
from pathlib import Path

KOKLER = [
    "/System/Library/CoreServices/Installer.app",
    "/System/Library/CoreServices/CoreServicesUIAgent.app",
    "/System/Library/ExtensionKit/Extensions/SecurityPrivacyExtension.appex",
    "/System/Applications/System Settings.app",
    "/System/Library/PrivateFrameworks/SystemPolicy.framework",
]
# Tek sözcüklükler birebir, uzunlar parça olarak aranır.
BIREBIR = {"Continue", "Go Back", "Install", "Agree", "Disagree", "Customize", "Standard Install", "Close", "Done",
           "Introduction", "License", "Summary", "Installation", "Installation Type", "Destination Select",
           "Package Name", "Action", "Size", "Skip", "Open Anyway", "Move to Trash", "Privacy & Security",
           "System Settings", "Open", "Cancel"}
PARCA = ["Not Opened", "blocked to protect", "could not verify", "free of malware", "Custom Install on",
         "Standard Install on", "unidentified developer", "must agree to the terms", "Click Agree to continue",
         "was blocked from use", "Open Anyway"]
EN = ("en", "English", "Base", "en_US", "en_GB")
TR = ("tr", "Turkish", "tr_TR")


def oku(yol: Path):
    try:
        with open(yol, "rb") as f:
            return plistlib.load(f)
    except Exception:  # noqa: BLE001 — metin biçimli .strings: plutil çevirir
        r = subprocess.run(["plutil", "-convert", "json", "-o", "-", str(yol)], capture_output=True, text=True)
        try:
            return json.loads(r.stdout) if r.returncode == 0 else {}
        except ValueError:
            return {}


def ciftler():
    """(dosya, anahtar, ingilizce, türkçe) dörtlüleri."""
    for kok in map(Path, KOKLER):
        if not kok.exists():
            continue
        for tablo in kok.rglob("*.loctable"):
            veri = oku(tablo)
            en = next((veri[d] for d in EN if isinstance(veri.get(d), dict)), {})
            tr = next((veri[d] for d in TR if isinstance(veri.get(d), dict)), {})
            for anahtar, deger in en.items():
                if isinstance(deger, str):
                    yield tablo, anahtar, deger, tr.get(anahtar)
        for en_dizin in [p for d in EN for p in kok.rglob(f"{d}.lproj")]:
            tr_dizin = next((en_dizin.parent / f"{d}.lproj" for d in TR if (en_dizin.parent / f"{d}.lproj").is_dir()), None)
            for dosya in en_dizin.glob("*.strings"):
                en = oku(dosya)
                tr = oku(tr_dizin / dosya.name) if tr_dizin and (tr_dizin / dosya.name).exists() else {}
                for anahtar, deger in (en.items() if isinstance(en, dict) else []):
                    if isinstance(deger, str):
                        yield dosya, anahtar, deger, (tr.get(anahtar) if isinstance(tr, dict) else None)


def main() -> int:
    print(f"macOS {platform.mac_ver()[0]}")
    bulunan: dict = {}
    for dosya, anahtar, en, tr in ciftler():
        temiz = en.strip().rstrip("…").rstrip(".").strip()
        hedef = temiz if temiz in BIREBIR else next((p for p in PARCA if p in en), None)
        if not hedef or not tr:
            continue
        kayit = bulunan.setdefault(hedef, [])
        if (en, tr) not in [(k["en"], k["tr"]) for k in kayit] and len(kayit) < 6:
            kayit.append({"en": en, "tr": tr, "dosya": str(dosya).replace("/System/Library/", ""), "anahtar": anahtar})
    for hedef in sorted(bulunan):
        print(f"\n## {hedef}")
        for k in bulunan[hedef]:
            print(f"  {k['en']!r} → {k['tr']!r}   [{k['dosya']} :: {k['anahtar']}]")
    eksik = sorted((BIREBIR | set(PARCA)) - set(bulunan))
    print(f"\nbulunamayan: {', '.join(eksik) or '-'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
