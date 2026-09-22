"""Kurulum sonrası adım ve kaldırma. Inno Setup, KUR.cmd ve güncelleyici çağırır.

    al.py kur --kurulum      etkin sürümü seç, Claude Desktop yoksa winget ile kur, sunucuları kaydet
    al.py kur --zip-kurulum  zip'ten kurulum: içeriği %LOCALAPPDATA%\\Programs\\ArthurLegal'e taşı,
                             kısayolları ve oturum açılışı güncellemesini de kendisi yazar
    al.py kur --kaydet       yalnız Claude Desktop kaydını tazele (güncelleyici kullanır)
    al.py kur --kaldir       Claude Desktop girdilerini, kısayolları ve Run anahtarını sil

Zip yolu, Windows 11 Akıllı Uygulama Denetimi açık bilgisayarlar içindir: imzasız kurulum motoru
(.exe içindeki .tmp) orada engellenir, PSF imzalı python.exe engellenmez. O makinelerde Arthur Mask
de kurulamaz; ArthurLegal paketleri ve Tapu çalışır, UYAP çalışmaz (Arthur Mask'e bağlı).
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

import claude_ayari
import ortak


def claude_kurulu() -> bool:
    yerel = Path(os.environ.get("LOCALAPPDATA", ""))
    return (yerel / "AnthropicClaude").exists() or any((yerel / "Packages").glob("Claude_*")) \
        or any(y.parent.exists() for y in claude_ayari.yapilandirma_yollari())


def claude_kur() -> bool:
    """Claude Desktop'u kullanıcı kapsamında winget ile kurmayı dener (yönetici gerekmez)."""
    try:
        sonuc = subprocess.run(["winget", "install", "-e", "--id", "Anthropic.Claude", "--scope", "user", "--silent",
                                "--accept-package-agreements", "--accept-source-agreements", "--disable-interactivity"],
                               capture_output=True, creationflags=ortak.PENCERESIZ, timeout=900)
    except (OSError, subprocess.SubprocessError) as e:
        ortak.gunluk("kurulum", f"winget çalıştırılamadı: {e!r}")
        return False
    ortak.gunluk("kurulum", f"winget Anthropic.Claude çıkış kodu {sonuc.returncode}")
    return sonuc.returncode == 0 or claude_kurulu()


VARSAYILAN_KOK = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "ArthurLegal"
RUN_ANAHTARI = r"Software\Microsoft\Windows\CurrentVersion\Run"
RUN_ADI = "ArthurLegalGuncelleme"


def _menu() -> Path:
    return Path(os.environ["APPDATA"]) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "ArthurLegal"


def _masaustu() -> Path:
    return Path(os.environ["USERPROFILE"]) / "Desktop"


def kisayollar_yaz() -> None:
    """Kısayollar .cmd ve .url olarak yazılır: COM (WScript.Shell) Akıllı Uygulama Denetimi altında
    kısıtlı dil kipinde kullanılamıyor. İçerik saf ASCII'dir (yol %LOCALAPPDATA% ile çözülür);
    Türkçe karakterli bir kullanıcı adı .cmd kod sayfasını bozmasın diye."""
    kok = "%LOCALAPPDATA%\\Programs\\ArthurLegal"
    komutlar = {
        "ArthurLegal - Tapu": f'"{kok}\\runtime\\pythonw.exe" -B "{kok}\\bin\\al.py" kisayol tapu',
        "ArthurLegal - UYAP Tarayıcısı": f'"{kok}\\runtime\\python.exe" -B "{kok}\\bin\\al.py" kisayol uyap-tarayici',
        "ArthurLegal - Güncellemeleri Denetle": f'"{kok}\\runtime\\python.exe" -B "{kok}\\bin\\al.py" guncelle',
    }
    menu = _menu()
    menu.mkdir(parents=True, exist_ok=True)
    for ad, komut in komutlar.items():
        (menu / f"{ad}.cmd").write_text(f'@echo off\r\nstart "" {komut}\r\n', encoding="ascii")
    adres = quote(str(ortak.KOK / "rehber" / "baslangic.html").replace(chr(92), "/"), safe=":/")
    rehber = f"[InternetShortcut]\r\nURL=file:///{adres}\r\n"
    for klasor in (menu, _masaustu()):
        (klasor / "ArthurLegal - Başlangıç Rehberi.url").write_text(rehber, encoding="ascii")
    (_masaustu() / "ArthurLegal - Tapu.cmd").write_text(
        f'@echo off\r\nstart "" {komutlar["ArthurLegal - Tapu"]}\r\n', encoding="ascii")
    (ortak.KOK / "KALDIR.cmd").write_text(
        "@echo off\r\nchcp 65001 >nul\r\n"
        f'"{kok}\\runtime\\python.exe" -B "{kok}\\bin\\al.py" kur --kaldir\r\n'
        f'start "" cmd /c "timeout /t 3 >nul & rmdir /s /q "{kok}""\r\n', encoding="ascii")


def kisayollar_sil() -> None:
    for klasor, desenler in ((_menu(), ("*.cmd", "*.url")), (_masaustu(), ("ArthurLegal - *.cmd", "ArthurLegal - *.url"))):
        for desen in desenler:
            for y in klasor.glob(desen):
                y.unlink(missing_ok=True)
    if _menu().is_dir() and not any(_menu().iterdir()):
        _menu().rmdir()


def run_anahtari(yaz: bool) -> None:
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_ANAHTARI, 0, winreg.KEY_SET_VALUE) as k:
            if yaz:
                winreg.SetValueEx(k, RUN_ADI, 0, winreg.REG_SZ,
                                  f'"{ortak.RUNTIME / "pythonw.exe"}" -B "{ortak.AL}" guncelle --sessiz')
            else:
                winreg.DeleteValue(k, RUN_ADI)
    except (ImportError, OSError):
        pass


def zip_kurulum() -> int:
    """Zip'ten çalıştırılınca içeriği kurulum klasörüne taşır ve kurulumu oradan sürdürür."""
    kaynak = ortak.KOK
    if kaynak.resolve() == VARSAYILAN_KOK.resolve():
        return main(["--kurulum", "--kisayol"])
    print(f"ArthurLegal {ortak.surum()} kuruluyor: {VARSAYILAN_KOK}")
    for y in sorted(kaynak.rglob("*")):
        goreli = y.relative_to(kaynak)
        if goreli.parts and goreli.parts[0] == "veri":
            continue
        hedef = VARSAYILAN_KOK / goreli
        if y.is_dir():
            hedef.mkdir(parents=True, exist_ok=True)
        else:
            hedef.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(y, hedef)
    sonuc = subprocess.run([str(VARSAYILAN_KOK / "runtime" / "python.exe"), "-B",
                            str(VARSAYILAN_KOK / "bin" / "al.py"), "kur", "--kurulum", "--kisayol"])
    return sonuc.returncode


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal kurulum adımı")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--kurulum", action="store_true")
    g.add_argument("--zip-kurulum", action="store_true")
    g.add_argument("--kaydet", action="store_true")
    g.add_argument("--kaldir", action="store_true")
    ap.add_argument("--kisayol", action="store_true", help="kısayolları ve oturum açılışı güncellemesini de yaz")
    args = ap.parse_args(argv)

    if args.zip_kurulum:
        return zip_kurulum()
    if args.kaldir:
        silinen = claude_ayari.sil()
        kisayollar_sil()
        run_anahtari(False)
        ortak.gunluk("kurulum", f"kaldırma: {len(silinen)} yapılandırmadan silindi")
        return 0
    if args.kurulum:
        mevcut = ortak.surumler()
        if mevcut:  # eski bir kurulum dosyası yeniden çalıştırılsa da daha yeni sürüme geri dönülmez
            ortak.aktif_yaz(mevcut[-1])
        if not claude_kurulu():
            ortak.durum_guncelle(claude_winget=claude_kur())
        ortak.durum_guncelle(kurulum_zamani=time.time(), kurulum_surumu=ortak.surum())
    if args.kisayol:
        kisayollar_yaz()
        run_anahtari(True)
    degisen = claude_ayari.kaydet()
    ortak.gunluk("kurulum", f"Claude Desktop kaydı: {len(degisen)} dosya güncellendi; Mask {'var' if ortak.mask_python() else 'yok'}")
    if args.kurulum and args.kisayol:  # zip yolu: kullanıcı konsolda okuyor
        print(f"Kuruldu. Claude Desktop'a {len(claude_ayari.istenen_girdiler())} sunucu eklendi.")
        if not ortak.mask_python():
            print("Arthur Mask kurulu değil: müvekkil belgelerini maskeleyen kapı ve UYAP bağlantısı bu bilgisayarda çalışmaz.")
        print("Son adım rehberde: masaüstünde 'ArthurLegal - Başlangıç Rehberi'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
