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
import proje


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


def _programlar() -> Path:
    return Path(os.environ["APPDATA"]) / "Microsoft" / "Windows" / "Start Menu" / "Programs"


def _menu() -> Path:
    """Başlat menüsü klasörü: ürün adı (ortak.urun_adi). Kurulum betiğindeki {group} ile aynı olmalı."""
    return _programlar() / ortak.urun_adi()


def _masaustu() -> Path:
    return Path(os.environ["USERPROFILE"]) / "Desktop"


def _kaldir_adi(ad: str) -> str:
    """Kaldırma kısayolunun adı; kurulum betiğindeki KaldirAdi ile aynı olmalı (kurulum/ArthurLegal.iss)."""
    return "ArthurLegal'i Kaldır" if ad == ortak.URUN_VARSAYILAN else ad + " - Kaldır"


def _simge() -> Path:
    """Kısayol simgesi. Büroya özel kurulumda simgenin adı içeriğinin özetini taşır (ayar.json → simge):
    Windows simgeleri dosya yoluna göre önbelleğe alır; aynı yol başka bir simgeyle kalsaydı eski resim
    görünmeye devam ederdi."""
    ad = str(ortak.ayar().get("simge") or "")
    yol = ortak.KOK / "bin" / ad
    if ad and Path(ad).name == ad and yol.is_file():
        return yol
    return ortak.KOK / "bin" / "arthurlegal.ico"


def _kisayol_klasorleri(menu: Path) -> list:
    """Kısayolların durduğu yerler; ürün adı değiştiyse eski adlı Başlat menüsü klasörü de."""
    eski = _programlar() / ortak.URUN_VARSAYILAN
    return [menu, _masaustu()] + ([eski] if eski != menu else [])


def _desenler(ad: str, kisa: str = "") -> list:
    """Bu kurulumun kısayollarını tanıyan adlar: ürün adıyla ve (önceki kurulumdan kalan) ArthurLegal adıyla,
    sürümlü ("<ad> 2.4.0") ya da sürümsüz (2.4.0'dan önceki kurulumlar). Kısa ad yalnız UYAP simgesinde
    kullanılır; onunla yalnız "<kısa ad> - UYAP…" tanınır, başka kısayol değil."""
    adlar = sorted({ortak.URUN_VARSAYILAN, ad})
    kisa_desen = [f"{kisa} - UYAP*.lnk"] if kisa and kisa not in adlar else []
    return [d.format(a) for a in adlar
            for d in ("{}.lnk", "{} [0-9]*.lnk", "{}.cmd", "{} [0-9]*.cmd", "{} - *.lnk", "{} - *.cmd",
                      "{} - *.url", "{}*.url")] \
        + kisa_desen + ["ArthurLegal'i Kaldır.lnk"]


ESKI_KISAYOLLAR = ("ArthurLegal - Tapu.cmd", "ArthurLegal - UYAP Tarayıcısı.cmd",
                   "ArthurLegal - Güncellemeleri Denetle.cmd", "ArthurLegal - Başlangıç Rehberi.url")


def _kisayol_listesi() -> list:
    """(yol, hedef, argüman, açıklama) dörtlüleri. Adlar ürün adını taşır (ortak.urun_adi): genel kurulumda
    ArthurLegal, büroya özel kurulumda büronun ürün adı. Ana simge Claude'u açar, paneli gösterir.

    Her ad sonda çalışan kodun sürümünü taşır (ortak.surum: bu dosyanın sürüm klasöründeki surum.txt):
    "<ad> 2.4.0", "<ad> - Tapu 2.4.0". Güncelleyici adları ancak yeni sürüm doğrulanıp etkin olunca, o
    sürümün koduyla yeniden yazar; güncelleme olmadıysa ad eski numarada kalır."""
    py, pyw, al = ortak.RUNTIME / "python.exe", ortak.RUNTIME / "pythonw.exe", ortak.AL
    ad, kisa, menu, masa, s = ortak.urun_adi(), ortak.kisa_ad(), _menu(), _masaustu(), ortak.surum()
    ana = (pyw, f'-B "{al}" kisayol baslat', f"Claude Desktop'ı ve başlangıç panelini açar ({s})")
    tapu = (pyw, f'-B "{al}" kisayol tapu', f"ArthurLegal Tapu arayüzü ({s})")
    liste = [
        (masa / f"{ad} {s}.lnk", *ana),
        (masa / f"{ad} - Tapu {s}.lnk", *tapu),
        (menu / f"{ad} {s}.lnk", *ana),
        (menu / f"{ad} - Tapu {s}.lnk", *tapu),
        (menu / f"{ad} - Başlangıç Rehberi {s}.lnk", ortak.KOK / "rehber" / "baslangic.html", "", "Kurulum sonrası adımlar"),
        (menu / f"{ad} - Proje Klasörleri {s}.lnk", proje.kok(), "", "Claude'da 'Use a folder' ile seçilecek hazır proje klasörleri"),
        (menu / f"{ad} - Güncellemeleri Denetle {s}.lnk", py, f'-B "{al}" guncelle', "Güncellemeleri şimdi denetle"),
    ]
    # UYAP için tek simge: UYAP Dashboard. UYAP'a giriş tarayıcısını Dashboard kendisi açar. Maskeleme
    # olmadan açılmaz: köprü ve Arthur Mask birlikte varsa eklenir. Ad kısa addan ("<kısa ad> - UYAP Dashboard").
    if ortak.mask_python() and (ortak.SURUM_DIZINI / "uyap" / "ekran.py").exists():
        dashboard = (pyw, f'-B "{al}" kisayol uyap-ekran',
                     f"UYAP Dashboard: UYAP'a giriş, sabah taraması, son gün, uyuşmazlık ve takvim; Claude'suz ({s})")
        liste += [(masa / f"{kisa} - UYAP Dashboard {s}.lnk", *dashboard),
                  (menu / f"{kisa} - UYAP Dashboard {s}.lnk", *dashboard)]
    return liste


def eski_surumlu_kisayol_var() -> bool:
    """Bu kurulumun kısayollarından biri çalışan sürümden başka bir numara (ya da hiç numara) taşıyor mu?
    Güncelleme yarıda kaldıysa ya da ad yazılamadıysa güncelleyici bir sonraki denetimde düzeltir."""
    s, menu = ortak.surum(), _menu()
    kaldir = _kaldir_adi(ortak.urun_adi()) + ".lnk"
    for klasor in _kisayol_klasorleri(menu):
        for desen in _desenler(ortak.urun_adi(), ortak.kisa_ad()):
            for y in klasor.glob(desen):
                if y.suffix.lower() == ".lnk" and y.name != kaldir and not y.stem.endswith(" " + s):
                    return True
    return False


# Kurulum betiğindeki AppId (kurulum/ArthurLegal.iss) ile aynı olmalı; test karşılaştırır.
KALDIRMA_ANAHTARI = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\{5B7A1E2C-9D4F-4C8B-A6E3-2F1D0C9B8A71}_is1"


def programlar_listesi_yaz() -> bool:
    """Windows programlar listesindeki ad ve sürüm, çalışan kodun sürümüyle: kurulum betiği bunları yalnız
    kurulumda yazar, sessiz güncellemeden sonra eski numara kalırdı. Girdi yoksa (zip kurulumu) bir şey yapmaz."""
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, KALDIRMA_ANAHTARI, 0, winreg.KEY_SET_VALUE) as k:
            winreg.SetValueEx(k, "DisplayName", 0, winreg.REG_SZ, f"{ortak.urun_adi()} {ortak.surum()}")
            winreg.SetValueEx(k, "DisplayVersion", 0, winreg.REG_SZ, ortak.surum())
        return True
    except (ImportError, OSError):
        return False


# WScript.Shell .lnk dosya adını ANSI kod sayfasına çevirir: Türkçe olmayan Windows'ta "ş", "ı", "ğ"
# bozulur ("Başlangıç" -> "Baslangiç") ve kullanıcı adında bu harfler varsa hedef yol da bozulabilir.
# IShellLinkW + IPersistFile Unicode'dur; Add-Type ile derlenir (Akıllı Uygulama Denetimi açıkken denendi).
_KISAYOL_CS = r"""
using System;
using System.Runtime.InteropServices;
using System.Runtime.InteropServices.ComTypes;
using System.Text;
[ComImport, Guid("00021401-0000-0000-C000-000000000046")] class ArthurShellLink {}
[ComImport, InterfaceType(ComInterfaceType.InterfaceIsIUnknown), Guid("000214F9-0000-0000-C000-000000000046")]
interface IArthurShellLinkW {
  void GetPath([Out, MarshalAs(UnmanagedType.LPWStr)] StringBuilder f, int c, IntPtr d, uint fl);
  void GetIDList(out IntPtr p); void SetIDList(IntPtr p);
  void GetDescription([Out, MarshalAs(UnmanagedType.LPWStr)] StringBuilder n, int c);
  void SetDescription([MarshalAs(UnmanagedType.LPWStr)] string n);
  void GetWorkingDirectory([Out, MarshalAs(UnmanagedType.LPWStr)] StringBuilder d, int c);
  void SetWorkingDirectory([MarshalAs(UnmanagedType.LPWStr)] string d);
  void GetArguments([Out, MarshalAs(UnmanagedType.LPWStr)] StringBuilder a, int c);
  void SetArguments([MarshalAs(UnmanagedType.LPWStr)] string a);
  void GetHotkey(out short h); void SetHotkey(short h);
  void GetShowCmd(out int s); void SetShowCmd(int s);
  void GetIconLocation([Out, MarshalAs(UnmanagedType.LPWStr)] StringBuilder p, int c, out int i);
  void SetIconLocation([MarshalAs(UnmanagedType.LPWStr)] string p, int i);
  void SetRelativePath([MarshalAs(UnmanagedType.LPWStr)] string p, uint r);
  void Resolve(IntPtr h, uint f);
  void SetPath([MarshalAs(UnmanagedType.LPWStr)] string f);
}
public static class ArthurKisayol {
  public static void Yaz(string yol, string hedef, string arg, string calisma, string aciklama, string ikon) {
    var l = (IArthurShellLinkW)new ArthurShellLink();
    l.SetPath(hedef); if (arg.Length > 0) l.SetArguments(arg); l.SetWorkingDirectory(calisma);
    l.SetDescription(aciklama); if (ikon.Length > 0) l.SetIconLocation(ikon, 0);
    ((IPersistFile)l).Save(yol, true);
  }
}
"""


def kisayollar_yaz() -> None:
    """Simgeli .lnk kısayolları (IShellLinkW, Unicode). Add-Type engellenirse .cmd yedeğine düşer."""
    menu = _menu()
    menu.mkdir(parents=True, exist_ok=True)
    ikon = _simge()
    tirnak = lambda s: str(s).replace("'", "''")  # noqa: E731
    satirlar = ["$ErrorActionPreference = 'Stop'", "Add-Type -TypeDefinition @'", _KISAYOL_CS.strip(), "'@"]
    for yol, hedef, arg, aciklama in _kisayol_listesi():
        satirlar.append(f"[ArthurKisayol]::Yaz('{tirnak(yol)}', '{tirnak(hedef)}', '{tirnak(arg)}', "
                        f"'{tirnak(ortak.KOK)}', '{tirnak(aciklama)}', '{tirnak(ikon) if ikon.exists() else ''}')")
    betik = ortak.VERI / "kisayollar.ps1"
    betik.parent.mkdir(parents=True, exist_ok=True)
    betik.write_text("\n".join(satirlar) + "\n", encoding="utf-8-sig")
    try:
        sonuc = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(betik)],
                               capture_output=True, creationflags=ortak.PENCERESIZ, timeout=180)
        tamam = sonuc.returncode == 0 and all(y.exists() for y, *_ in _kisayol_listesi())
        if not tamam:
            ortak.gunluk("kurulum", "kısayol betiği: " + sonuc.stderr.decode("utf-8", "replace")[-400:])
    except (OSError, subprocess.SubprocessError) as e:
        ortak.gunluk("kurulum", f"kısayol betiği çalışmadı: {e!r}")
        tamam = False
    finally:
        betik.unlink(missing_ok=True)
    if not tamam:
        ortak.gunluk("kurulum", "kısayollar .cmd yedeğiyle yazıldı (COM kullanılamadı)")
        _kisayol_cmd_yedegi()
    kalacak = {y for y, *_ in _kisayol_listesi()} | {menu / (_kaldir_adi(ortak.urun_adi()) + ".lnk")}
    eski_kisayollari_temizle(menu, kalacak)
    kok = "%LOCALAPPDATA%\\Programs\\ArthurLegal"
    (ortak.KOK / "KALDIR.cmd").write_text(
        "@echo off\r\nchcp 65001 >nul\r\n"
        f'"{kok}\\runtime\\python.exe" -B "{kok}\\bin\\al.py" kur --kaldir\r\n'
        f'start "" cmd /c "timeout /t 3 >nul & rmdir /s /q "{kok}""\r\n', encoding="ascii")


def eski_kisayollari_temizle(menu: Path, kalacak: set) -> None:
    """Önceki sürümlerden (UYAP, .cmd, .url) ve ürün adı değiştiyse önceki adla (ArthurLegal) kalan
    kısayolları siler; boş kalan eski Başlat menüsü klasörü de gider."""
    for klasor in _kisayol_klasorleri(menu):
        for desen in _desenler(ortak.urun_adi(), ortak.kisa_ad()):
            for y in klasor.glob(desen):
                if y not in kalacak:
                    y.unlink(missing_ok=True)
    eski = _programlar() / ortak.URUN_VARSAYILAN
    if eski != menu and eski.is_dir() and not any(eski.iterdir()):
        eski.rmdir()


def _kisayol_cmd_yedegi() -> None:
    """COM yoksa: .cmd ve .url kısayolları. İçerik saf ASCII (yol %LOCALAPPDATA% ile çözülür)."""
    kok = "%LOCALAPPDATA%\\Programs\\ArthurLegal"
    urun, s = ortak.urun_adi(), ortak.surum()
    for ad, komut in ((f"{urun} {s}", f'"{kok}\\runtime\\pythonw.exe" -B "{kok}\\bin\\al.py" kisayol baslat'),
                      (f"{urun} - Tapu {s}", f'"{kok}\\runtime\\pythonw.exe" -B "{kok}\\bin\\al.py" kisayol tapu')):
        icerik = f'@echo off\r\nstart "" {komut}\r\n'
        (_menu() / f"{ad}.cmd").write_text(icerik, encoding="ascii")
        (_masaustu() / f"{ad}.cmd").write_text(icerik, encoding="ascii")
    adres = quote(str(ortak.KOK / "rehber" / "baslangic.html").replace(chr(92), "/"), safe=":/")
    (_menu() / f"{urun} - Başlangıç Rehberi {s}.url").write_text(
        f"[InternetShortcut]\r\nURL=file:///{adres}\r\n", encoding="ascii")


def kisayollar_sil() -> None:
    menu = _menu()
    for klasor in _kisayol_klasorleri(menu):
        for desen in _desenler(ortak.urun_adi(), ortak.kisa_ad()):
            for y in klasor.glob(desen):
                y.unlink(missing_ok=True)
    for klasor in {menu, _programlar() / ortak.URUN_VARSAYILAN}:
        if klasor.is_dir() and not any(klasor.iterdir()):
            klasor.rmdir()


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
    # al.py aktif.txt'deki sürümü seçer; üzerine kurulumda o hâlâ önceki sürümdür ve kısayollar önceki sürümün
    # koduyla yazılırdı. aktif.txt yoksa en yeni sürüm seçilir; kur.py onu yeniden yazar (kurulum betiği de aynı).
    (VARSAYILAN_KOK / "aktif.txt").unlink(missing_ok=True)
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
    ap.add_argument("--kisayol-esitle", action="store_true",
                    help="kısayollar çalışan sürümden başka bir numara taşıyorsa yeniden yaz (güncelleyici)")
    args = ap.parse_args(argv)

    if args.zip_kurulum:
        return zip_kurulum()
    if args.kaldir:
        silinen = claude_ayari.sil()
        kisayollar_sil()
        run_anahtari(False)
        proje.kaldir()
        ortak.gunluk("kurulum", f"kaldırma: {len(silinen)} yapılandırmadan silindi")
        return 0
    if args.kurulum:
        mevcut = ortak.surumler()
        if mevcut:  # eski bir kurulum dosyası yeniden çalıştırılsa da daha yeni sürüme geri dönülmez
            ortak.aktif_yaz(mevcut[-1])
        if not claude_kurulu():
            ortak.durum_guncelle(claude_winget=claude_kur())
        ortak.durum_guncelle(kurulum_zamani=time.time(), kurulum_surumu=ortak.surum())
    if args.kisayol or (args.kisayol_esitle and eski_surumlu_kisayol_var()):
        kisayollar_yaz()
        run_anahtari(True)
        programlar_listesi_yaz()
        import kisayol  # başlangıç panelinin durum kartı ilk açılışta dolu gelsin
        kisayol.durum_yaz()
    degisen = claude_ayari.kaydet()
    try:  # "Use a folder" proje klasörleri; güncelleyici her sürümde buradan tazeler
        proje.esitle()
    except OSError as e:
        ortak.gunluk("kurulum", f"proje klasörleri yazılamadı: {e!r}")
    ortak.gunluk("kurulum", f"Claude Desktop kaydı: {len(degisen)} dosya güncellendi; Mask {'var' if ortak.mask_python() else 'yok'}")
    if args.kurulum and args.kisayol:  # zip yolu: kullanıcı konsolda okuyor
        print(f"Kuruldu. Claude Desktop'a {len(claude_ayari.istenen_girdiler())} sunucu eklendi.")
        if not ortak.mask_python():
            print("Arthur Mask kurulu değil: müvekkil belgelerini maskeleyen kapı bu bilgisayarda çalışmaz.")
        print(f"Masaüstündeki '{ortak.urun_adi()} {ortak.surum()}' simgesine çift tıklayın: Claude Desktop'u açar ve son adımı gösterir.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
