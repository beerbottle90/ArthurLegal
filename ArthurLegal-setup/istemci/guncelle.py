"""ArthurLegal sessiz güncelleyici.

Oturum açılışında (HKCU Run) ve yerel sunucu açıkken 6 saatte bir çalışır:
1. En son GitHub Release'teki arthurlegal-manifest.json ve .sig indirilir; imza güvenilen
   anahtarlardan biriyle (Ed25519: günlük yayın anahtarı ya da kasadaki yedek; liste çalışan
   paketten, ortak.guvenilen_anahtarlar) doğrulanmadan hiçbir şey kurulmaz.
2. Manifest'teki paket sürümü etkin sürümden yeniyse zip indirilir, sha256 doğrulanır, yeni
   bir surumler\\<sürüm> klasörüne açılır ve aktif.txt tek adımda değiştirilir. Çalışan
   sunucular eski klasörle devam eder; yeni sürüm Claude Desktop'ın bir sonraki açılışında
   devreye girer. Bir önceki sürüm geri dönüş için saklanır.
3. Arthur Mask kurulu sürümden yeniyse (≈1 GB) arka planda indirilir, Claude Desktop kapalıyken
   sessiz kurulur. Windows 11 Akıllı Uygulama Denetimi açıksa indirilmez: imzasız kurulum orada hiç çalışmaz.
   Kurulu değilse yalnız kurulumda seçildiyse (ortak.moduller) indirilir.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import zipfile
from pathlib import Path
from urllib.parse import urljoin

import ed25519
import ortak


class GuncellemeHatasi(Exception):
    pass


def _dogrula(ham: bytes, imza_metni: bytes, ayar: dict) -> dict:
    anahtarlar = ortak.guvenilen_anahtarlar(ayar)
    if not anahtarlar:
        raise GuncellemeHatasi("kurulumda yayın anahtarı yok")
    imza = bytes.fromhex(imza_metni.decode("ascii").strip())
    if not any(ed25519.verify(bytes.fromhex(a), ham, imza) for a in anahtarlar):
        raise GuncellemeHatasi("manifest imzası geçersiz; güncelleme reddedildi")
    return json.loads(ham.decode("utf-8"))


def _api_basliklari(ayar: dict, tur="application/vnd.github+json") -> dict:
    basliklar = {"Accept": tur, "X-GitHub-Api-Version": "2022-11-28"}
    if ayar.get("jeton"):
        basliklar["Authorization"] = "Bearer " + ayar["jeton"]
    return basliklar


def manifest_getir(ayar: dict):
    """(manifest, indirici) döndürür; yayın yoksa (None, None). indirici(dosya_adı, hedef) -> sha256.

    Dağıtım private depodan yapılır: varlıklar GitHub API'sinden, kurulumdaki salt okunur jetonla
    indirilir. manifest_url verilmişse (yerel sunucu, testler) düz HTTP yolu kullanılır.
    """
    depo = ayar.get("dagitim_deposu")
    if depo:
        if not ayar.get("jeton"):
            return None, None  # güncelleme kanalı yapılandırılmamış
        taban_api = ayar.get("api_tabani") or "https://api.github.com"
        yayinlar = json.loads(ortak.indir(f"{taban_api}/repos/{depo}/releases?per_page=10",
                                          zaman=30, basliklar=_api_basliklari(ayar)).decode("utf-8"))
        beta = ayar.get("kanal") == "beta"
        for yayin in yayinlar:
            if yayin.get("draft") or (yayin.get("prerelease") and not beta):
                continue
            varliklar = {a["name"]: a for a in yayin.get("assets", [])}
            if "arthurlegal-manifest.json" not in varliklar or "arthurlegal-manifest.sig" not in varliklar:
                continue

            def indirici(dosya, hedef=None, varliklar=varliklar):
                if dosya not in varliklar:
                    raise GuncellemeHatasi(f"yayında yok: {dosya}")
                return ortak.indir(varliklar[dosya]["url"], hedef, zaman=180,
                                   basliklar=_api_basliklari(ayar, "application/octet-stream"))

            manifest = _dogrula(indirici("arthurlegal-manifest.json"), indirici("arthurlegal-manifest.sig"), ayar)
            return manifest, indirici
        return None, None

    url = ayar.get("manifest_url")
    if not url:
        return None, None
    try:
        ham = ortak.indir(url, zaman=30)
    except urllib.error.HTTPError as e:
        if e.code != 404 or not ayar.get("yedek_depo"):
            raise
        # En son yayın manifest taşımıyorsa (ör. yalnız sürüm notu) taşıyan en yeni yayın aranır.
        taban_api = ayar.get("api_tabani") or "https://api.github.com"
        yayinlar = json.loads(ortak.indir(f"{taban_api}/repos/{ayar['yedek_depo']}/releases?per_page=10", zaman=30,
                                          basliklar=_api_basliklari(ayar)).decode("utf-8"))
        beta = ayar.get("kanal") == "beta"
        url = next((a["browser_download_url"] for y in yayinlar
                    if not y.get("draft") and (beta or not y.get("prerelease"))
                    for a in y.get("assets", []) if a.get("name") == "arthurlegal-manifest.json"), None)
        if not url:
            return None, None
        ham = ortak.indir(url, zaman=30)
    manifest = _dogrula(ham, ortak.indir(url[: -len(".json")] + ".sig", zaman=30), ayar)
    taban = manifest.get("taban") or url.rsplit("/", 1)[0] + "/"

    def indirici(dosya, hedef=None):
        return ortak.indir(urljoin(taban, dosya), hedef, zaman=180)

    return manifest, indirici


def _guvenli_ac(zip_yolu: Path, hedef: Path) -> None:
    with zipfile.ZipFile(zip_yolu) as z:
        for ad in z.namelist():
            yol = (hedef / ad).resolve()
            if not str(yol).startswith(str(hedef.resolve())) or ad.startswith(("/", "\\")):
                raise GuncellemeHatasi(f"zip içinde geçersiz yol: {ad}")
        z.extractall(hedef)


def paket_guncelle(manifest: dict, indirici) -> bool:
    yeni, etkin = manifest["surum"], ortak.aktif() or (ortak.surumler() or ["0"])[-1]
    if ortak.surum_demeti(yeni) <= ortak.surum_demeti(etkin):
        return False
    p = manifest["paket"]
    indirilen = ortak.VERI / "indirilen" / p["dosya"]
    sha = indirici(p["dosya"], indirilen)
    if sha != p["sha256"]:
        indirilen.unlink(missing_ok=True)
        raise GuncellemeHatasi(f"paket sha256 uyuşmadı ({p['dosya']})")
    surumler = ortak.KOK / "surumler"
    gecici = surumler / f"{yeni}.yeni"
    shutil.rmtree(gecici, ignore_errors=True)
    _guvenli_ac(indirilen, gecici)
    if (gecici / "surum.txt").read_text(encoding="utf-8").strip() != yeni or not (gecici / "istemci" / "arthurlegal_sunucu.py").exists():
        shutil.rmtree(gecici, ignore_errors=True)
        raise GuncellemeHatasi("paket içeriği beklenen sürümle uyuşmuyor")
    shutil.rmtree(surumler / yeni, ignore_errors=True)
    os.replace(gecici, surumler / yeni)
    ortak.aktif_yaz(yeni)
    indirilen.unlink(missing_ok=True)
    for eski in ortak.surumler()[:-2]:  # etkin + bir önceki kalır
        shutil.rmtree(surumler / eski, ignore_errors=True)
    ortak.gunluk("guncelle", f"paket {etkin} -> {yeni}")
    return True


def mask_mac_engeli() -> str:
    """Arthur Mask'in Mac sürümü Apple Silicon ve macOS 14 (Sonoma) ister. Uymuyorsa nedeni, uyuyorsa boş."""
    arm = subprocess.run(["sysctl", "-n", "hw.optional.arm64"], capture_output=True, text=True).stdout.strip() == "1"
    if not arm:
        return "Arthur Mask Mac'te yalnız Apple Silicon'da çalışır"
    import platform
    try:
        ana = int((platform.mac_ver()[0] or "0").split(".")[0])
    except ValueError:
        ana = 0
    return "" if ana >= 14 else "Arthur Mask Mac'te macOS 14 (Sonoma) ya da sonrasını ister"


def mac_mask_kur(manifest: dict) -> str:
    """macOS: Arthur Mask'i ilk kez kurar (kurulumda seçildiyse; Apple Silicon ve macOS 14'te). Disk görüntüsü
    indirilir, sha256'sı imzalı manifestteki değerle (mask_macos) doğrulanır, uygulama Uygulamalar klasörüne kopyalanır
    (yazılamıyorsa ~/Applications) ve Arthur Mask'in kendi aracıyla Claude Desktop'a kaydedilir. Kurulu Arthur Mask
    güncellemesini kendisi yapar; buraya karışılmaz. Bu yolla indirilen dosya karantina işareti taşımaz."""
    kurulu = ortak.mask_surumu()
    if kurulu:
        return f"mask: kurulu ({kurulu}); Arthur Mask Mac'te güncellemesini kendisi yapar"
    if "mask" not in ortak.moduller():
        return "mask: kurulumda seçilmedi"
    engel = mask_mac_engeli()
    if engel:
        return f"mask: {engel}"
    m = manifest.get("mask_macos")
    if not m:
        return "mask: manifest'te macOS sürümü yok"
    dmg = ortak.VERI / "indirilen" / f"ArthurMask-Kurulum-{m['surum']}.dmg"
    if not (dmg.exists() and ortak.sha256_dosya(dmg) == m["sha256"]):
        if ortak.indir(m["url"], dmg, zaman=120) != m["sha256"]:
            dmg.unlink(missing_ok=True)
            raise GuncellemeHatasi("Arthur Mask (macOS) sha256 uyuşmadı")
    import tempfile
    nokta = Path(tempfile.mkdtemp(prefix="arthurmask-"))
    subprocess.run(["hdiutil", "attach", "-nobrowse", "-readonly", "-noautoopen", "-mountpoint", str(nokta), str(dmg)],
                   check=True, capture_output=True, timeout=600)
    try:
        kok = Path("/Applications") if os.access("/Applications", os.W_OK) else Path.home() / "Applications"
        kok.mkdir(parents=True, exist_ok=True)
        hedef = kok / "Arthur Mask.app"
        subprocess.run(["ditto", str(nokta / "Arthur Mask.app"), str(hedef)], check=True, capture_output=True, timeout=1800)
    finally:
        subprocess.run(["hdiutil", "detach", str(nokta), "-force"], capture_output=True, timeout=300)
        shutil.rmtree(nokta, ignore_errors=True)
    subprocess.run(["xattr", "-dr", "com.apple.quarantine", str(hedef)], capture_output=True, timeout=300)
    py = hedef / "Contents" / "Resources" / "runtime" / "bin" / "python3"
    # Arthur Mask'in kendi kurulumunun yaptığı gibi (modülü derlenmiş olduğundan -m ile değil, -c ile çağrılır).
    kayit = subprocess.run([str(py), "-I", "-B", "-c", "import sys; from arthur_mask.claude_ayari import main; "
                            "sys.exit(main(['kaydet']))"], capture_output=True, text=True, timeout=300)
    if kayit.returncode and kayit.stderr.strip():  # 1: zaten kayıtlı (değişen dosya yok)
        ortak.gunluk("guncelle", f"Arthur Mask Claude kaydı {kayit.returncode}: {kayit.stderr.strip()[-300:]}")
    dmg.unlink(missing_ok=True)
    ortak.gunluk("guncelle", f"Arthur Mask (macOS) {m['surum']} kuruldu: {hedef}")
    import mac
    mac.bildirim("Arthur Mask", ortak.metin(
        "Arthur Mask kuruldu. Claude Desktop'tan Cmd+Q ile çıkıp yeniden açın; araçları o zaman görünür.",
        "Arthur Mask is installed. Quit Claude Desktop with Cmd+Q and open it again to see its tools."))
    return f"mask: {m['surum']} kuruldu"


def mask_guncelle(manifest: dict) -> str:
    if ortak.MAC:
        return mac_mask_kur(manifest)
    m = manifest.get("mask")
    if not m:
        return "mask: manifest'te yok"
    kurulu = ortak.mask_surumu()
    if kurulu and ortak.surum_demeti(kurulu) >= ortak.surum_demeti(m["surum"]):
        return f"mask: güncel ({kurulu})"
    if not kurulu and "mask" not in ortak.moduller():
        # Kurulumda seçilmedi: kurulu değilse indirilmez. Kendi kurulumuyla eklenmiş bir Arthur Mask ise güncellenir.
        return "mask: kurulumda seçilmedi"
    if ortak.akilli_denetim_acik() and not m.get("imzali"):
        # Denetim imzasız kurulumu engeller: ~1 GB boşuna iner ve her denetimde engellenen kurulum yeni bir Windows
        # uyarısı gösterirdi (zip yoluyla kurulan bilgisayarlar). Denetim kapatılırsa ya da Arthur Mask kurulumu
        # imzalanırsa (manifest: mask.imzali) bir sonraki denetimde iner. Önceki denemeden kalan dosya silinir.
        for eski in (ortak.VERI / "indirilen").glob("ArthurMask-Kurulum-*.exe*"):
            eski.unlink(missing_ok=True)
        return "mask: Akıllı Uygulama Denetimi açık, Arthur Mask bu bilgisayarda kurulamaz"
    exe = ortak.VERI / "indirilen" / f"ArthurMask-Kurulum-{m['surum']}.exe"
    if not (exe.exists() and ortak.sha256_dosya(exe) == m["sha256"]):
        if ortak.indir(m["url"], exe, zaman=120) != m["sha256"]:
            exe.unlink(missing_ok=True)
            raise GuncellemeHatasi("Arthur Mask sha256 uyuşmadı")
    if ortak.claude_calisiyor():
        return "mask: indirildi, Claude Desktop kapanınca kurulacak"
    sonuc = subprocess.run([str(exe), "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART", "/SP-"],
                           creationflags=ortak.PENCERESIZ, timeout=3600)
    if sonuc.returncode != 0:
        raise GuncellemeHatasi(f"Arthur Mask kurulumu {sonuc.returncode} ile bitti")
    exe.unlink(missing_ok=True)
    ortak.gunluk("guncelle", f"Arthur Mask {kurulu or 'yok'} -> {m['surum']}")
    return f"mask: {m['surum']} kuruldu"


def _claude_kaydet(guncellendi: bool = False) -> None:
    """Etkin (belki yeni) sürümün kodu ile Claude Desktop kaydını tazeler. Paket güncellendiyse kısayollar ve
    programlar listesi yeni sürümün koduyla, onun numarasıyla yeniden yazılır; güncellenmediyse yalnız başka
    numara taşıyan (yarım kalmış bir güncellemeden kalan) kısayollar çalışan sürüme eşitlenir. Numara hep
    çalışan kodun surum.txt'sinden gelir: güncelleme olmadıysa ad değişmez."""
    py = ortak.python_yolu()
    if py.exists():
        subprocess.run([str(py), "-B", str(ortak.AL), "kur", "--kaydet", "--kisayol" if guncellendi else "--kisayol-esitle"],
                       creationflags=ortak.PENCERESIZ, timeout=180)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal güncelleyici")
    ap.add_argument("--sessiz", action="store_true", help="arka plan çalıştırması")
    ap.add_argument("--mask-yok", action="store_true", help="Arthur Mask'e dokunma")
    ap.add_argument("--bildir", action="store_true", help="sonucu bildirimle göster (macOS: Güncellemeleri Denetle)")
    args = ap.parse_args(argv)

    kilit = ortak.VERI / "guncelle.kilit"
    kilit.parent.mkdir(parents=True, exist_ok=True)
    try:
        if kilit.exists() and time.time() - kilit.stat().st_mtime > 7200:
            kilit.unlink()
        fd = os.open(kilit, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError:
        return 0  # başka bir güncelleyici çalışıyor
    try:
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        ortak.durum_guncelle(son_denetim=time.time())
        sonuclar = []
        guncellendi = False
        try:
            manifest, indirici = manifest_getir(ortak.ayar())
            if manifest is None:
                sonuclar.append("yayında manifest yok")
            else:
                onceki = ortak.aktif() or (ortak.surumler() or ["?"])[-1]
                guncellendi = paket_guncelle(manifest, indirici)
                if guncellendi:
                    # Yalnız paket doğrulanıp etkin sürüm değiştikten sonra: panel bunu "son güncelleme" diye gösterir.
                    ortak.durum_guncelle(son_guncelleme={"zaman": time.time(), "onceki": onceki,
                                                         "yeni": manifest["surum"]})
                sonuclar.append(f"paket {manifest['surum']} kuruldu" if guncellendi
                                else f"paket güncel ({ortak.aktif()})")
                if not args.mask_yok:
                    sonuclar.append(mask_guncelle(manifest))
        except (GuncellemeHatasi, OSError, ValueError, KeyError, subprocess.SubprocessError) as e:
            sonuclar.append(f"hata: {e}")
            ortak.gunluk("guncelle", f"hata: {e!r}")
        # macOS'ta Arthur Mask'i bu kurulum kurar: masaüstü takma adı için kısayollar yeniden yazılır.
        mask_kuruldu = ortak.MAC and any(s.startswith("mask: ") and s.endswith(" kuruldu") for s in sonuclar)
        _claude_kaydet(guncellendi or mask_kuruldu)
        ortak.durum_guncelle(son_sonuc="; ".join(sonuclar))
        if not args.sessiz:
            print("\n".join(sonuclar))
        if args.bildir and ortak.MAC:
            import mac
            mac.bildirim(ortak.urun_adi(), "; ".join(sonuclar))
        return 1 if any(s.startswith("hata") for s in sonuclar) else 0
    finally:
        kilit.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
