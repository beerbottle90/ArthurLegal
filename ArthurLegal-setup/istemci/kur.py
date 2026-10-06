"""Kurulum sonrası adım ve kaldırma. Inno Setup, KUR.cmd ve güncelleyici çağırır.

    al.py kur --kurulum      etkin sürümü seç, Claude Desktop yoksa winget ile kur, sunucuları kaydet
                             (--moduller adliye,tapu,mask: kurulumda seçilen modüller; moduller.json'a yazılır)
    al.py kur --zip-kurulum  zip'ten kurulum: modülleri konsolda sorar, içeriği %LOCALAPPDATA%\\Programs\\ArthurLegal'e
                             taşır, kısayolları ve oturum açılışı güncellemesini de kendisi yazar
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


def _kaldir_adi(ad: str, dil: str | None = None) -> str:
    """Kaldırma kısayolunun adı, kurulumun dilinde; kurulum betiğindeki KaldirAdiTr/KaldirAdiEn ile aynı olmalı
    (kurulum/ArthurLegal.iss)."""
    if (dil or ortak.dil()) == "en":
        return "Uninstall ArthurLegal" if ad == ortak.URUN_VARSAYILAN else ad + " - Uninstall"
    return "ArthurLegal'i Kaldır" if ad == ortak.URUN_VARSAYILAN else ad + " - Kaldır"


# Kısayol adları ve açıklamaları, kurulumun dilinde (ortak.dil). "Tapu", "Courthouse" ve "UYAP Dashboard" özel ad,
# çevrilmez. Paket simgeleri (ana, Courthouse, Akademisyen) aynı işi yapar: Claude Desktop'ı ve başlangıç panelini açar.
KISAYOL_METNI = {
    "tr": {"ana": "Claude Desktop'ı ve başlangıç panelini açar ({s})", "tapu": "ArthurLegal Tapu arayüzü ({s})",
           "adliye": "Courthouse", "adliye_aciklama": "Courthouse (hâkim ve kalem): Claude Desktop'ı ve başlangıç panelini açar ({s})",
           "akademisyen": "Akademisyen",
           "akademisyen_aciklama": "Akademisyen: Claude Desktop'ı ve başlangıç panelini açar ({s})",
           "rehber": "Başlangıç Rehberi", "rehber_aciklama": "Kurulum sonrası adımlar",
           "proje": "Proje Klasörleri", "proje_aciklama": "Claude'da 'Use a folder' ile seçilecek hazır proje klasörleri",
           "guncelle": "Güncellemeleri Denetle", "guncelle_aciklama": "Güncellemeleri şimdi denetle",
           "uyap": "UYAP Dashboard: UYAP'a giriş, sabah taraması, son gün, uyuşmazlık ve takvim; Claude'suz ({s})"},
    "en": {"ana": "Opens Claude Desktop and the start panel ({s})",
           "tapu": "ArthurLegal Tapu: Turkish land-registry parcel tool ({s})",
           "adliye": "Courthouse", "adliye_aciklama": "Courthouse (judges and court clerks): opens Claude Desktop and the start panel ({s})",
           "akademisyen": "Academician",
           "akademisyen_aciklama": "Academician: opens Claude Desktop and the start panel ({s})",
           "rehber": "Start Guide", "rehber_aciklama": "Steps after setup",
           "proje": "Project Folders", "proje_aciklama": "Ready-made project folders to choose with 'Use a folder' in Claude",
           "guncelle": "Check for Updates", "guncelle_aciklama": "Check for updates now",
           "uyap": "UYAP Dashboard: UYAP sign-in, morning scan, deadlines, mismatches and calendar; works without Claude ({s})"},
}


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
        + kisa_desen + ["ArthurLegal'i Kaldır.lnk", "Uninstall ArthurLegal.lnk"]


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
    m = KISAYOL_METNI[ortak.dil()]
    secili = ortak.moduller()
    # Kurulumda seçilen modüllere göre (ortak.moduller): Hukuk Bürosu ya da Kurumsal seçildiyse ana simge "<ad> <s>";
    # Courthouse ve Akademisyen kendi simgesini ("<ad> - Courthouse <s>"), Tapu kendi simgesini alır. Seçimden
    # çıkarılan modülün simgesi eski_kisayollari_temizle'de gider ("<ad> - *" deseni).
    simgeler = []
    if {"hukuk-burosu", "kurumsal"} & set(secili):
        simgeler.append((f"{ad} {s}.lnk", (pyw, f'-B "{al}" kisayol baslat', m["ana"].format(s=s))))
    for profil in ("adliye", "akademisyen"):
        if profil in secili:
            simgeler.append((f"{ad} - {m[profil]} {s}.lnk",
                             (pyw, f'-B "{al}" kisayol baslat {profil}', m[profil + "_aciklama"].format(s=s))))
    if ortak.bilesen_var("tapu"):
        simgeler.append((f"{ad} - Tapu {s}.lnk", (pyw, f'-B "{al}" kisayol tapu', m["tapu"].format(s=s))))
    liste = [(klasor / dosya, *hedef) for klasor in (masa, menu) for dosya, hedef in simgeler] + [
        (menu / f"{ad} - {m['rehber']} {s}.lnk", ortak.rehber_dosyasi(), "", m["rehber_aciklama"]),
        (menu / f"{ad} - {m['proje']} {s}.lnk", proje.kok(), "", m["proje_aciklama"]),
        (menu / f"{ad} - {m['guncelle']} {s}.lnk", py, f'-B "{al}" guncelle', m["guncelle_aciklama"]),
    ]
    # UYAP için tek simge: UYAP Dashboard. UYAP'a giriş tarayıcısını Dashboard kendisi açar. Maskeleme
    # olmadan açılmaz: köprü ve Arthur Mask birlikte varsa eklenir. Ad kısa addan ("<kısa ad> - UYAP Dashboard").
    if ortak.mask_python() and (ortak.SURUM_DIZINI / "uyap" / "ekran.py").exists():
        dashboard = (pyw, f'-B "{al}" kisayol uyap-ekran', m["uyap"].format(s=s))
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
    for yol, hedef, arg, _ in _kisayol_listesi():  # paket ve Tapu simgeleri, seçilen modüllere göre
        if Path(hedef).name != "pythonw.exe":
            continue
        komut = f'"{kok}\\runtime\\pythonw.exe" ' + arg.replace(f'"{ortak.AL}"', f'"{kok}\\bin\\al.py"')
        yol.parent.mkdir(parents=True, exist_ok=True)
        yol.with_suffix(".cmd").write_text(f'@echo off\r\nstart "" {komut}\r\n', encoding="ascii")
    adres = quote(str(ortak.rehber_dosyasi()).replace(chr(92), "/"), safe=":/")
    (_menu() / f"{urun} - {KISAYOL_METNI[ortak.dil()]['rehber']} {s}.url").write_text(
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


# Modül adları ve kısa açıklamaları; zip kurulumunun konsol sorusunda. Kurulum sihirbazındaki metinler
# kurulum/ArthurLegal.iss'tedir ([CustomMessages] Modul*), iki yer aynı tutulur.
MODUL_METNI = {
    "tr": {"hukuk-burosu": ("Hukuk Bürosu", "avukatlar için dilekçe, sözleşme, içtihat ve mevzuat araştırması"),
           "kurumsal": ("Kurumsal Asistan", "şirket hukuk birimleri için sözleşme, uyum ve KVKK işleri"),
           "adliye": ("Courthouse", "hâkim ve kalem için tarafsız taslak: gerekçe, tensip, müzekkere, tebligat"),
           "akademisyen": ("Akademisyen", "hukuk akademisyenleri için literatür, atıf, dergi seçimi, yayın etiği"),
           "tapu": ("ArthurLegal Tapu", "ada/parsel ya da yer adıyla TKGM'den canlı parsel, kroki ve harç"),
           "mask": ("Arthur Mask", "belgeleri Claude'a vermeden önce bu bilgisayarda maskeler")},
    "en": {"hukuk-burosu": ("Law Firm", "for lawyers: petitions, contracts, case-law and legislation research"),
           "kurumsal": ("Corporate Assistant", "for in-house legal teams: contracts, compliance, data protection"),
           "adliye": ("Courthouse", "for judges and court clerks: neutral drafts of reasoning, orders, writs, service"),
           "akademisyen": ("Academician", "for legal academics: literature, citations, journal choice, ethics"),
           "tapu": ("ArthurLegal Tapu", "live Turkish land-registry parcels (TKGM) with sketch and fees"),
           "mask": ("Arthur Mask", "masks documents on this computer before Claude sees them")},
}


def zip_secimi(dil: str, onceki: list | None = None, girdi=input) -> list:
    """Zip kurulumunda modül seçimi, konsolda numarayla. Arthur Mask bu yolla kurulamaz (Akıllı Uygulama Denetimi imzasız
    kurulumu engeller), sorulmaz. Enter: önceki seçim. Konsol yoksa (girdi okunamıyorsa) önceki seçim, o da yoksa 2.5.0
    öncesinin modülleri; kurulum yarıda kalmaz."""
    secenekler = [m for m in ortak.MODULLER if m != "mask"]
    onceki = [m for m in (onceki or []) if m in secenekler]
    metin = MODUL_METNI[dil]
    en = dil == "en"
    print("Which modules should be installed? At least one of the first four is needed." if en
          else "Hangi modüller kurulsun? İlk dördünden en az biri gerekir.")
    for no, m in enumerate(secenekler, 1):
        print(f"  {no}  {metin[m][0]} - {metin[m][1]}")
    print("Arthur Mask cannot be installed this way." if en else "Arthur Mask bu yolla kurulamaz.")
    soru = ("Type the numbers separated by commas (e.g. 3,5)" if en else "Numaraları virgülle yazın (ör. 3,5)")
    if onceki:
        soru += " [Enter: " + ", ".join(metin[m][0] for m in onceki) + "]"
    soru += ": "
    for _ in range(20):
        try:
            cevap = girdi(soru).strip()
        except (EOFError, OSError):
            return onceki or [m for m in ortak.ESKI_SECIM if m != "mask"]
        if not cevap and onceki:
            return onceki
        try:
            nolar = [int(x) for x in cevap.replace(" ", "").split(",") if x]
            if not nolar or any(not 1 <= n <= len(secenekler) for n in nolar):
                raise ValueError(cevap)
            return ortak.secim_coz(",".join(secenekler[n - 1] for n in nolar))
        except ValueError:
            print("Please type the numbers from the list, including at least one of 1-4." if en
                  else "Listedeki numaraları yazın; 1-4 arasından en az biri olmalı.")
    return onceki or [m for m in ortak.ESKI_SECIM if m != "mask"]


def zip_kurulum() -> int:
    """Zip'ten çalıştırılınca içeriği kurulum klasörüne taşır ve kurulumu oradan sürdürür. Dil sorulmaz: önceki
    kurulumun dili, yoksa Windows'un arayüz dili (ortak.sistem_dili). Modüller konsolda sorulur (zip_secimi)."""
    kaynak = ortak.KOK
    dil = ortak.json_oku(VARSAYILAN_KOK / "veri" / "durum.json").get("dil")
    dil = dil if dil in ortak.DILLER else ortak.sistem_dili()
    onceki = ortak.json_oku(VARSAYILAN_KOK / "moduller.json").get("moduller")
    secim = ",".join(zip_secimi(dil, onceki if isinstance(onceki, list) else None))
    if kaynak.resolve() == VARSAYILAN_KOK.resolve():
        return main(["--kurulum", "--kisayol", "--dil", dil, "--moduller", secim])
    print((f"ArthurLegal {ortak.surum()} is being installed: {VARSAYILAN_KOK}" if dil == "en"
           else f"ArthurLegal {ortak.surum()} kuruluyor: {VARSAYILAN_KOK}"))
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
                            str(VARSAYILAN_KOK / "bin" / "al.py"), "kur", "--kurulum", "--kisayol", "--dil", dil,
                            "--moduller", secim])
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
    ap.add_argument("--dil", choices=ortak.DILLER, help="kurulumun dili (kurulum sihirbazında seçilen)")
    ap.add_argument("--moduller", help="kurulumda seçilen modüller, virgülle: " + ",".join(ortak.MODULLER))
    args = ap.parse_args(argv)
    if args.dil and not args.zip_kurulum:
        ortak.durum_guncelle(dil=args.dil)
    if args.moduller and not args.zip_kurulum:
        try:
            ortak.moduller_yaz(args.moduller)
        except ValueError as e:
            ortak.gunluk("kurulum", f"geçersiz modül seçimi: {e}")
            print(f"Geçersiz modül seçimi / invalid module selection: {e}")
            return 2

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
    ortak.gunluk("kurulum", f"Claude Desktop kaydı: {len(degisen)} dosya güncellendi; modüller "
                            f"{','.join(ortak.moduller())}; Mask {'var' if ortak.mask_python() else 'yok'}")
    if args.kurulum and args.kisayol:  # zip yolu: kullanıcı konsolda okuyor
        paket = next((y.stem for y, _, a, _ in _kisayol_listesi() if y.parent == _masaustu() and "kisayol baslat" in a),
                     f"{ortak.urun_adi()} {ortak.surum()}")
        sayi, simge = len(claude_ayari.istenen_girdiler()), paket
        print(ortak.metin(f"Kuruldu. Claude Desktop'a {sayi} sunucu eklendi.",
                          f"Installed. {sayi} servers were added to Claude Desktop."))
        if not ortak.mask_python():
            print(ortak.metin("Arthur Mask kurulu değil: müvekkil belgelerini maskeleyen kapı bu bilgisayarda çalışmaz.",
                              "Arthur Mask is not installed: the gate that masks client documents does not work on "
                              "this computer."))
        print(ortak.metin(f"Masaüstündeki '{simge}' simgesine çift tıklayın: Claude Desktop'u açar ve son adımı gösterir.",
                          f"Double-click the '{simge}' icon on the desktop: it opens Claude Desktop and shows the last step."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
