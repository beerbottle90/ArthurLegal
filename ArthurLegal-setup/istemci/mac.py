"""macOS'ta kısayollar, kaldırma ve oturum açılışı: Windows'taki .lnk kısayollarının, Başlat menüsünün, programlar
listesinin ve Run anahtarının karşılığı. kur.py çağırır; liste (hangi simge, hangi ad) kur._kisayol_listesi'ndedir.

- Paket ve Tapu simgeleri ~/Applications'ta küçük uygulamalardır (Launchpad'de ve Spotlight'ta görünür) ve masaüstünde
  birer takma adları (sembolik bağ) durur. Arthur Mask kuruluysa onun da masaüstü takma adı yazılır; Windows'ta bunu
  Arthur Mask'in kendi kurulumu yapar.
- Yardımcılar (başlangıç rehberi, proje klasörleri, güncelleme denetimi, kaldırma) ~/Applications/<ürün> klasöründedir.
- Adlar sürüm numarası taşımaz (Mac alışkanlığı; Dock'a eklenen simge güncellemede kopmasın). Sürüm uygulamanın
  bilgisindedir (Finder: Bilgi Al) ve her güncellemede yeniden yazılır; eski_surumlu_kisayol_var ona bakar.
- Silme yalnız bu kurulumun yazdığı uygulamalara (paket kimliği com.arthurlegal.kisayol.*) ve masaüstündeki sembolik
  bağlara dokunur; kullanıcının başka dosyasına dokunulmaz.
- Güncelleyici oturum açılışında ve altı saatte bir LaunchAgent'la çalışır (~/Library/LaunchAgents).
"""
from __future__ import annotations

import hashlib
import os
import plistlib
import shlex
import shutil
import subprocess
from pathlib import Path

import ortak

AJAN_ETIKETI = "com.arthurlegal.guncelleme"
KIMLIK_ONEKI = "com.arthurlegal.kisayol."
CALISTIRILABILIR = "arthurlegal"
LSREGISTER = Path("/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister")


def uygulamalar() -> Path:
    return Path.home() / "Applications"


def masaustu() -> Path:
    return Path.home() / "Desktop"


def ajan_yolu() -> Path:
    return Path.home() / "Library" / "LaunchAgents" / f"{AJAN_ETIKETI}.plist"


def bizim_mi(app: Path) -> bool:
    """Bu kurulumun yazdığı bir uygulama mı (paket kimliğine bakılır)."""
    try:
        with open(app / "Contents" / "Info.plist", "rb") as f:
            return str(plistlib.load(f).get("CFBundleIdentifier", "")).startswith(KIMLIK_ONEKI)
    except (OSError, ValueError):
        return False


def surumu(app: Path) -> str:
    try:
        with open(app / "Contents" / "Info.plist", "rb") as f:
            return str(plistlib.load(f).get("CFBundleShortVersionString", ""))
    except (OSError, ValueError):
        return ""


def uygulama_yaz(app: Path, hedef: Path, arg: str, aciklama: str, surum: str, simge: Path | None) -> None:
    """Küçük bir .app: Contents/MacOS/arthurlegal kabuk betiği hedefi argümanla çalıştırır. Kurulumun yazdığı dosya
    karantina işareti taşımaz, Gatekeeper sormaz."""
    gecici = app.with_name(app.name + ".yeni")
    shutil.rmtree(gecici, ignore_errors=True)
    (gecici / "Contents" / "MacOS").mkdir(parents=True)
    (gecici / "Contents" / "Resources").mkdir()
    ad = app.stem
    bilgi = {
        "CFBundleName": ad, "CFBundleDisplayName": ad,
        "CFBundleIdentifier": KIMLIK_ONEKI + hashlib.sha1(ad.encode("utf-8")).hexdigest()[:10],
        "CFBundleExecutable": CALISTIRILABILIR, "CFBundlePackageType": "APPL",
        "CFBundleShortVersionString": surum, "CFBundleVersion": surum, "CFBundleInfoDictionaryVersion": "6.0",
        "CFBundleGetInfoString": aciklama, "LSUIElement": True, "LSMinimumSystemVersion": "11.0",
    }
    if simge and simge.exists():
        shutil.copy2(simge, gecici / "Contents" / "Resources" / "arthurlegal.icns")
        bilgi["CFBundleIconFile"] = "arthurlegal"
    with open(gecici / "Contents" / "Info.plist", "wb") as f:
        plistlib.dump(bilgi, f)
    betik = gecici / "Contents" / "MacOS" / CALISTIRILABILIR
    betik.write_text(f"#!/bin/sh\n# {aciklama}\nexec {shlex.quote(str(hedef))} {arg} >/dev/null 2>&1\n", encoding="utf-8")
    betik.chmod(0o755)
    if app.exists() or app.is_symlink():
        if app.is_symlink() or not bizim_mi(app):  # kullanıcının aynı adlı uygulaması: dokunulmaz, yanına yazılmaz
            shutil.rmtree(gecici, ignore_errors=True)
            ortak.gunluk("kurulum", f"{app} bu kurulumun değil, üzerine yazılmadı")
            return
        shutil.rmtree(app, ignore_errors=True)
    os.replace(gecici, app)
    if LSREGISTER.exists():  # Launchpad ve Spotlight yeni uygulamayı hemen görsün
        subprocess.run([str(LSREGISTER), "-f", str(app)], capture_output=True, timeout=60)


def takma_ad_yaz(yol: Path, hedef: Path) -> None:
    """Masaüstündeki takma ad: sembolik bağ. Yerinde gerçek bir dosya ya da klasör varsa dokunulmaz."""
    if yol.is_symlink():
        if os.readlink(yol) == str(hedef):
            return
        yol.unlink()
    elif yol.exists():
        ortak.gunluk("kurulum", f"{yol} masaüstünde gerçek bir dosya, takma ad yazılmadı")
        return
    yol.parent.mkdir(parents=True, exist_ok=True)
    os.symlink(hedef, yol)


def kaldirma_betigi(kok: Path, urun: str, dil: str) -> str:
    """KALDIR.command: onay sorar; Claude Desktop kaydını, kısayolları, oturum açılışını ve kurulum klasörünü siler.
    Proje klasörlerinde kullanıcının kendi dosyaları kalır (kur --kaldir)."""
    if dil == "en":
        soru = f"Remove {urun} from this Mac? Your own files in the project folders are kept."
        evet, hayir, bitti = "Uninstall", "Cancel", f"{urun} was removed."
    else:
        soru = f"{urun} bu Mac'ten kaldırılsın mı? Proje klasörlerinizdeki kendi dosyalarınız silinmez."
        evet, hayir, bitti = "Kaldır", "Vazgeç", f"{urun} kaldırıldı."
    soru_as = 'button returned of (display dialog {} buttons {{{}, {}}} default button {} with icon caution)'.format(
        _as(soru), _as(hayir), _as(evet), _as(hayir))
    bitti_as = "display notification {} with title {}".format(_as(bitti), _as(urun))
    return (
        "#!/bin/sh\n"
        f"# {urun}: kaldırma. Kısayolu Uygulamalar klasöründeki {urun} klasöründedir.\n"
        f"CEVAP=$(/usr/bin/osascript -e {shlex.quote(soru_as)} 2>/dev/null)\n"
        f"[ \"$CEVAP\" = {shlex.quote(evet)} ] || exit 0\n"
        f"KOK={shlex.quote(str(kok))}\n"
        "\"$KOK/runtime/bin/python3\" -B \"$KOK/bin/al.py\" kur --kaldir\n"
        "rm -rf \"$KOK\"\n"
        f"/usr/bin/osascript -e {shlex.quote(bitti_as)} 2>/dev/null\n"
        "exit 0\n"
    )


def _as(metin: str) -> str:
    """AppleScript dizgesi: tırnak içinde, ters eğik çizgi ve tırnak kaçışlı."""
    return '"' + metin.replace("\\", "\\\\").replace('"', '\\"') + '"'


def kisayollar_yaz(liste: list, menu: Path, simge: Path | None, surum: str) -> None:
    """kur._kisayol_listesi'nin (yol, hedef, argüman, açıklama) satırlarını yazar: .app ile biten yol uygulamadır;
    masaüstündeki satır, hedefi bir uygulama olan takma addır."""
    menu.mkdir(parents=True, exist_ok=True)
    uygulamalar().mkdir(parents=True, exist_ok=True)
    for yol, hedef, arg, aciklama in liste:
        if yol.parent == masaustu():
            takma_ad_yaz(yol, Path(hedef))
        else:
            uygulama_yaz(yol, Path(hedef), arg, aciklama, surum, simge)


def eski_kisayollari_temizle(liste: list, menu: Path, urun: str) -> None:
    """Listede olmayan, bu kurulumun yazdığı uygulamaları ve masaüstündeki takma adları siler (seçimden çıkan modül,
    önceki ad). Arthur Mask'in kendi uygulamasına dokunulmaz, yalnız masaüstündeki takma adı."""
    kalacak = {yol for yol, *_ in liste}
    adaylar = [p for p in uygulamalar().glob(f"{urun}*.app")] + ([p for p in menu.glob("*.app")] if menu.is_dir() else [])
    for app in adaylar:
        if app not in kalacak and not app.is_symlink() and bizim_mi(app):
            shutil.rmtree(app, ignore_errors=True)
    for bag in masaustu().glob("*.app") if masaustu().is_dir() else []:
        if bag in kalacak or not bag.is_symlink():
            continue
        hedef = os.readlink(bag)
        if hedef.endswith("/Arthur Mask.app") or (Path(hedef).parent == uygulamalar() and Path(hedef).name.startswith(urun)):
            bag.unlink()
    if menu.is_dir() and not any(menu.iterdir()):
        menu.rmdir()


def eski_surumlu_kisayol_var(liste: list, surum: str) -> bool:
    """Bu kurulumun uygulamalarından biri çalışan sürümden başka bir sürüm taşıyor mu ya da eksik mi?"""
    for yol, *_ in liste:
        if yol.parent != masaustu() and (not yol.exists() or surumu(yol) != surum):
            return True
    return False


def kisayollar_sil(urun: str, menu: Path) -> None:
    eski_kisayollari_temizle([], menu, urun)
    if menu.is_dir():
        for app in menu.glob("*.app"):
            if bizim_mi(app):
                shutil.rmtree(app, ignore_errors=True)
        if not any(menu.iterdir()):
            menu.rmdir()


def ajan(yaz: bool, python: Path, al: Path) -> None:
    """Oturum açılışında ve altı saatte bir sessiz güncelleme (Windows'taki Run anahtarının karşılığı)."""
    yol = ajan_yolu()
    hedef = f"gui/{os.getuid()}"
    subprocess.run(["launchctl", "bootout", f"{hedef}/{AJAN_ETIKETI}"], capture_output=True, timeout=60)
    if not yaz:
        yol.unlink(missing_ok=True)
        return
    yol.parent.mkdir(parents=True, exist_ok=True)
    with open(yol, "wb") as f:
        plistlib.dump({"Label": AJAN_ETIKETI, "ProgramArguments": [str(python), "-B", str(al), "guncelle", "--sessiz"],
                       "RunAtLoad": True, "StartInterval": 6 * 3600, "ProcessType": "Background",
                       "StandardOutPath": "/dev/null", "StandardErrorPath": "/dev/null"}, f)
    sonuc = subprocess.run(["launchctl", "bootstrap", hedef, str(yol)], capture_output=True, text=True, timeout=60)
    if sonuc.returncode:
        ortak.gunluk("kurulum", f"launchctl bootstrap {sonuc.returncode}: {sonuc.stderr.strip()[-200:]}")


def bildirim(baslik: str, metin: str) -> None:
    subprocess.run(["osascript", "-e", f"display notification {_as(metin)} with title {_as(baslik)}"],
                   capture_output=True, timeout=30)
