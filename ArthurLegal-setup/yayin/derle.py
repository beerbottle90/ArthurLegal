"""ArthurLegal kurulum dosyasını derler.

    python yayin/derle.py                    ArthurLegal-Kurulum.exe ve ArthurLegal-Kurulum.zip
    python yayin/derle.py --firma <kod>      büroya özel kurulum (firma/<kod>/ katmanı gömülü)
    python yayin/derle.py --exe-yok          yalnız hazırlık klasörü ve güncelleme paketi (Inno Setup gerekmez)

Kaynaklar kaynaklar.json'daki yerel klonlardan, her deponun commitlenmiş HEAD'inden alınır:
paketler bu deponun kendisinden, Tapu public arthurlegal-mcp klonundan. En yeni Law Firm ve
Corporate klasörü kendiliğinden seçilir. Çıktı yayin/cikti/ altına yazılır; yayinla.py
derleme.json'u okuyup imzalı manifest üretir.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
CIKTI = BURASI / "yayin" / "cikti"
ONBELLEK = BURASI / "yayin" / ".onbellek"
sys.path.insert(0, str(BURASI / "istemci"))
import ortak  # noqa: E402

BOM = b"\xef\xbb\xbf"


def kaynaklar() -> dict:
    return json.loads((BURASI / "kaynaklar.json").read_text(encoding="utf-8"))


def kaynaklar_yaz(k: dict) -> None:
    (BURASI / "kaynaklar.json").write_text(json.dumps(k, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


CALISMA_AGACI = False  # --calisma-agaci: commitlenmemiş değişiklikler de derlemeye girer


def depo_klonu(k: dict, ad: str) -> Path:
    yol = (BURASI / k["depolar"][ad]).resolve()
    if not yol.is_dir():
        sys.exit(f"{ad} deposu bulunamadı: {yol}\n  git clone https://github.com/beerbottle90/{ad}.git  (kaynaklar.json 'depolar')")
    return yol


def depo(k: dict, ad: str) -> Path:
    """Varsayılan olarak deponun commitlenmiş HEAD'i (git archive) kullanılır: aynı depoda çalışan başka
    bir oturumun yarım işi kuruluma girmez. Anlık görüntü commit'e göre önbellekte tutulur.
    kaynaklar.json 'alt_yol' verirse o alt klasör döner (ör. arthurlegal-mcp içindeki tkgm-mcp)."""
    alt = k.get("alt_yol", {}).get(ad, "")
    klon = depo_klonu(k, ad)
    if CALISMA_AGACI:
        return klon / alt if alt else klon
    ref = k.get("dallar", {}).get(ad, "HEAD")  # public sürüm sabit bir dala bakar, çalışılan dala değil
    commit = git(klon, "rev-parse", "--short", ref)
    hedef = ONBELLEK / f"agac-{ad}-{commit}"
    if not hedef.is_dir():
        ONBELLEK.mkdir(parents=True, exist_ok=True)
        arsiv = ONBELLEK / f"agac-{ad}-{commit}.zip"
        subprocess.run(["git", "-C", str(klon), "archive", "--format=zip", "-o", str(arsiv), ref], check=True)
        with zipfile.ZipFile(arsiv) as z:
            z.extractall(hedef)
        arsiv.unlink()
    return hedef / alt if alt else hedef


def git(yol: Path, *args) -> str:
    r = subprocess.run(["git", "-C", str(yol), *args], capture_output=True, text=True, encoding="utf-8")
    return r.stdout.strip()


def depo_bilgisi(yol: Path, ref: str = "HEAD") -> dict:
    degisen = [s for s in git(yol, "status", "--porcelain").splitlines() if s.strip()]
    return {"commit": git(yol, "rev-parse", "--short", ref), "ref": ref,
            "dal": git(yol, "branch", "--show-current"), "commitlenmemis_dosya": len(degisen)}


def sha256(yol: Path) -> str:
    return ortak.sha256_dosya(yol)


def en_yeni_paket(kok: Path, desen: str) -> Path:
    adaylar = [Path(p) for p in glob.glob(str(kok / desen)) if re.search(r"v\d+\.\d+\.\d+", p)]
    if not adaylar:
        sys.exit(f"Paket klasörü yok: {kok / desen}")
    return max(adaylar, key=lambda p: tuple(int(x) for x in re.search(r"v(\d+)\.(\d+)\.(\d+)", p.name).groups()))


def kopyala(kaynak: Path, hedef: Path, dahil=lambda g: True) -> int:
    sayi = 0
    for y in sorted(kaynak.rglob("*")):
        g = y.relative_to(kaynak).as_posix()
        if not y.is_file() or any(p.startswith(".") or p == "__pycache__" for p in g.split("/")) or not dahil(g):
            continue
        (hedef / g).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(y, hedef / g)
        sayi += 1
    return sayi


def modul_surumu(dosya: Path) -> str:
    m = re.search(r'^__version__\s*=\s*"([^"]+)"', dosya.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else "?"


def python_hazirla(k: dict, hedef: Path) -> None:
    p = k["python"]
    arsiv = ONBELLEK / Path(p["url"]).name
    if not arsiv.exists():
        print(f"  Python {p['surum']} gömülü dağıtımı indiriliyor...")
        ortak.indir(p["url"], arsiv, zaman=300)
    ozet = sha256(arsiv)
    if p.get("sha256") and p["sha256"] != ozet:
        sys.exit(f"Python arşivinin sha256'sı sabitlenenle uyuşmuyor: {ozet}")
    if not p.get("sha256"):
        p["sha256"] = ozet
        kaynaklar_yaz(k)
        print(f"  Python arşivi sha256 sabitlendi: {ozet}")
    with zipfile.ZipFile(arsiv) as z:
        z.extractall(hedef)
    # Varsayılan ._pth (pythonXY.zip + .) yeterli: bin\al.py hedefin klasörünü sys.path'e kendisi ekler.


def mask_bilgisi(k: dict) -> dict:
    """Mask sürümü ve sha256'sı yayındaki güncel dosyadan okunur (etiket sabit, dosya yenilenebiliyor)."""
    m = dict(k["mask"])
    try:
        with ortak.istek("https://api.github.com/repos/beerbottle90/ArthurLegal/releases/tags/arthur-mask",
                         {"Accept": "application/vnd.github+json"}, zaman=30) as r:
            yayin = json.loads(r.read().decode("utf-8"))
        varlik = next(a for a in yayin["assets"] if a["name"] == Path(m["url"]).name)
        m.update(sha256=varlik["digest"].split(":", 1)[1], boyut=varlik["size"])
        s = re.search(r"(\d+\.\d+\.\d+)", yayin.get("name", ""))
        if s:
            m["surum"] = s.group(1)
    except Exception as e:  # noqa: BLE001 — çevrimdışı derlemede sabitlenen değer kullanılır
        print(f"  Uyarı: Arthur Mask yayın bilgisi okunamadı, kaynaklar.json kullanılıyor ({e})")
    return m


def paket_hazirla(k: dict, hedef: Path) -> dict:
    icerik = {"surum": k["surum"], "paketler": {}, "bilesenler": {}, "kaynak": {}}
    kopyala(BURASI / "istemci", hedef / "istemci", lambda g: g.endswith(".py"))
    al = depo(k, "ArthurLegal")
    for profil, desen in k["paketler"].items():
        klasor = en_yeni_paket(al, desen)
        sayi = kopyala(klasor, hedef / "paketler" / profil)
        icerik["paketler"][profil] = re.search(r"v(\d+\.\d+\.\d+)", klasor.name).group(1)
        print(f"  {profil}: {klasor.name} ({sayi} dosya)")
    kullanilan = ["ArthurLegal"]
    if k["bilesenler"].get("tapu"):
        tapu = depo(k, "tapu")
        kopyala(tapu, hedef / "tapu", lambda g: not g.startswith(("tests/", "docs/")) and not g.endswith(".cmd"))
        icerik["bilesenler"]["tapu"] = modul_surumu(tapu / "server.py")
        kullanilan.append("tapu")
    if k["bilesenler"].get("uyap"):  # arthur-uyap deposu private: public kuruluma girmez
        uyap = depo(k, "uyap")
        kopyala(uyap, hedef / "uyap", lambda g: not g.startswith("tests/"))
        icerik["bilesenler"]["uyap"] = modul_surumu(uyap / "server.py")
        kullanilan.append("uyap")
    for ad in kullanilan:
        icerik["kaynak"][ad] = bilgi = depo_bilgisi(depo_klonu(k, ad), k.get("dallar", {}).get(ad, "HEAD"))
        if bilgi["commitlenmemis_dosya"]:
            print(f"  Not: {ad} deposunda {bilgi['commitlenmemis_dosya']} commitlenmemiş dosya var; "
                  + ("derlemeye GİRDİ (--calisma-agaci)." if CALISMA_AGACI else f"derlemeye girmedi (HEAD {bilgi['commit']})."))
    (hedef / "surum.txt").write_text(k["surum"], encoding="utf-8")
    ortak.json_yaz(hedef / "icerik.json", icerik)
    return icerik


def buro_simgesi(firma_dizini: Path, bin_dizini: Path) -> bool:
    """Büronun simgesi (``firma/<kod>/marka/simge.ico``) varsa ArthurLegal simgesinin yerini alır:
    kurulum dosyası, kısayollar ve kaldırma girdisi ``bin/arthurlegal.ico``'yu kullanır. Güncelleme
    paketi ``bin/``'e dokunmadığı için simge güncellemelerde korunur. Geçerli bir ICO değilse
    (başlık 00 00 01 00) ya da 1 MB'tan büyükse ArthurLegal simgesi kalır."""
    simge = firma_dizini / "marka" / "simge.ico"
    if not simge.is_file() or simge.stat().st_size > 1024 * 1024:
        return False
    with open(simge, "rb") as f:
        if f.read(4) != b"\x00\x00\x01\x00":
            return False
    shutil.copy2(simge, bin_dizini / "arthurlegal.ico")
    return True


def firma_hazirla(kod: str, hedef: Path) -> dict:
    kaynak = BURASI / "firma" / kod
    bilgi = ortak.json_oku(kaynak / "firma.json")
    if not bilgi:
        sys.exit(f"Büro bulunamadı: {kaynak / 'firma.json'}")
    kopyala(kaynak, hedef, lambda g: g != "firma.json")
    for desen in bilgi.get("buro_kaynaklari", []):
        for y in sorted(glob.glob(str((kaynak / desen).resolve()))):
            (hedef / "buro").mkdir(parents=True, exist_ok=True)
            shutil.copy2(y, hedef / "buro" / Path(y).name)
    ortak.json_yaz(hedef / "firma.json", {"kod": bilgi["kod"], "ad": bilgi["ad"]})
    print(f"  büro katmanı: {bilgi['ad']} ({sum(1 for _ in hedef.rglob('*.md'))} dosya)")
    return bilgi


def _lisans_metni(k: dict, ad: str, yollar, adres: str = "") -> str:
    """Lisansı yerel klondan okur; klon yoksa GitHub'dan çeker (public depo)."""
    for yol in yollar:
        if yol and Path(yol).exists():
            return Path(yol).read_text(encoding="utf-8")
    if adres:
        try:
            return ortak.indir(adres, zaman=30).decode("utf-8")
        except Exception as e:  # noqa: BLE001
            print(f"  Uyarı: {ad} lisansı alınamadı ({e})")
    return "(Lisans metni bileşenin kendi deposundadır.)"


def lisans_yaz(k: dict, hedef: Path) -> None:
    """Lisans sayfası UTF-8 BOM ile yazılır; Inno Setup BOM'suz .txt'yi ANSI sanar ve Türkçe bozulur."""
    al = depo(k, "ArthurLegal")
    tapu_klonu = depo_klonu(k, "tapu") if (BURASI / k["depolar"]["tapu"]).is_dir() else None
    bolumler = [
        ("1. ArthurLegal Lisansı", _lisans_metni(k, "ArthurLegal", [al / "LICENSE"])),
        ("2. Arthur Mask Lisansı", _lisans_metni(
            k, "Arthur Mask", [(BURASI / k["depolar"].get("arthur-mask", "")) / "LICENSE"],
            "https://raw.githubusercontent.com/beerbottle90/arthur-mask/main/LICENSE")),
        ("3. ArthurLegal Tapu (tkgm-mcp) — MIT Lisansı", _lisans_metni(
            k, "Tapu", [depo(k, "tapu") / "LICENSE", tapu_klonu and tapu_klonu / "LICENSE"],
            "https://raw.githubusercontent.com/beerbottle90/arthurlegal-mcp/master/LICENSE")),
        ("4. Üçüncü taraf bildirimleri (Apache 2.0)", _lisans_metni(
            k, "Apache", [en_yeni_paket(al, k["paketler"]["hukuk-burosu"]) / "LICENSE-APACHE-2.0-THIRD-PARTY.txt"])),
    ]
    metin = (BURASI / "kurulum" / "lisans_onsoz.txt").read_text(encoding="utf-8")
    for baslik, govde in bolumler:
        metin += f"\n\n{'═' * 70}\n{baslik}\n{'═' * 70}\n\n{govde.strip()}\n"
    (hedef / "LISANS.txt").write_bytes(BOM + metin.replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8"))


def rehber_yaz(hedef: Path, firma_ad: str, icerik: dict) -> None:
    sablon = (BURASI / "kurulum" / "rehber.html").read_text(encoding="utf-8")
    degerler = {
        "{{FIRMA_SATIRI}}": html.escape(firma_ad) + " · " if firma_ad else "",
        "{{SURUM}}": icerik["surum"],
        "{{PAKET_HUKUK}}": icerik["paketler"].get("hukuk-burosu", "-"),
        "{{PAKET_KURUMSAL}}": icerik["paketler"].get("kurumsal", "-"),
        "{{ONYUKLEME_HUKUK}}": html.escape(ortak.ONYUKLEME["hukuk-burosu"]),
        "{{ONYUKLEME_KURUMSAL}}": html.escape(ortak.ONYUKLEME["kurumsal"]),
    }
    for anahtar, deger in degerler.items():
        sablon = sablon.replace(anahtar, deger)
    (hedef / "rehber").mkdir(parents=True, exist_ok=True)
    (hedef / "rehber" / "baslangic.html").write_text(sablon, encoding="utf-8")


def zip_yap(kaynak: Path, hedef: Path) -> None:
    """Aynı içerik aynı sha256'yı verir (sabit tarih, sıralı giriş)."""
    with zipfile.ZipFile(hedef, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for y in sorted(p for p in kaynak.rglob("*") if p.is_file()):
            bilgi = zipfile.ZipInfo(y.relative_to(kaynak).as_posix(), (2026, 1, 1, 0, 0, 0))
            bilgi.compress_type = zipfile.ZIP_DEFLATED
            bilgi.external_attr = 0o644 << 16
            z.writestr(bilgi, y.read_bytes())


def varlik_uret() -> None:
    """Pixel art simge ve görseller (varlik/gorseller.py)."""
    sonuc = subprocess.run([sys.executable, str(BURASI / "varlik" / "gorseller.py")], capture_output=True, text=True,
                           encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    if sonuc.returncode:
        sys.exit(f"Görseller üretilemedi:\n{sonuc.stdout}{sonuc.stderr}")


def iscc_bul() -> Path:
    adaylar = [Path(os.environ.get(v, "")) / "Inno Setup 6" / "ISCC.exe" for v in ("ProgramFiles(x86)", "ProgramFiles")]
    adaylar.insert(0, Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Inno Setup 6" / "ISCC.exe")
    bulunan = next((a for a in adaylar if a.exists()), None) or (shutil.which("ISCC") and Path(shutil.which("ISCC")))
    if not bulunan:
        sys.exit("Inno Setup 6 bulunamadı: winget install -e --id JRSoftware.InnoSetup --scope user")
    return bulunan


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal kurulum dosyasını derler")
    ap.add_argument("--firma", help="büro kodu (firma/<kod>/firma.json)")
    ap.add_argument("--exe-yok", action="store_true")
    ap.add_argument("--calisma-agaci", action="store_true", help="commitlenmemiş değişiklikleri de al")
    args = ap.parse_args(argv)
    global CALISMA_AGACI
    CALISMA_AGACI = args.calisma_agaci
    k = kaynaklar()
    if len(bytes.fromhex(k.get("yayin_anahtari") or "")) != 32:
        sys.exit("Yayın anahtarı yok: önce  python yayin/yayinla.py --anahtar-uret")
    iss = BURASI / "kurulum" / "ArthurLegal.iss"
    if not iss.read_bytes().startswith(BOM):
        sys.exit(f"{iss.name} UTF-8 BOM olmadan kaydedilmiş; Türkçe karakterler bozulur. BOM ile yeniden kaydedin.")

    surum = k["surum"]
    ad = "ArthurLegal-Kurulum" + (f"-{ortak.json_oku(BURASI / 'firma' / args.firma / 'firma.json').get('kurulum_adi', args.firma)}" if args.firma else "")
    hazirlik = CIKTI / f"hazirlik-{args.firma or 'genel'}"
    shutil.rmtree(hazirlik, ignore_errors=True)
    hazirlik.mkdir(parents=True)
    print(f"ArthurLegal yerel kurulum {surum} derleniyor → {ad}.exe")

    python_hazirla(k, hazirlik / "runtime")
    kopyala(BURASI / "bin", hazirlik / "bin", lambda g: g.endswith(".py"))
    varlik_uret()
    for ad_varlik in ("arthurlegal.ico", "rehber-banner.png"):
        shutil.copy2(BURASI / "varlik" / ad_varlik, hazirlik / "bin" / ad_varlik)
    icerik = paket_hazirla(k, hazirlik / "surumler" / surum)
    firma = firma_hazirla(args.firma, hazirlik / "firma") if args.firma else {}
    if args.firma and buro_simgesi(BURASI / "firma" / args.firma, hazirlik / "bin"):
        print(f"  büro simgesi: firma/{args.firma}/marka/simge.ico")
    rehber_yaz(hazirlik, firma.get("ad", ""), icerik)
    shutil.copy2(BURASI / "varlik" / "rehber-banner.png", hazirlik / "rehber" / "banner.png")
    lisans_yaz(k, hazirlik)
    ayar = {"manifest_url": f"https://github.com/{k['yayin_deposu']}/releases/latest/download/arthurlegal-manifest.json",
            "yedek_depo": k["yayin_deposu"], "kanal": k.get("kanal", "kararli"),
            "uzak_mcp": k["uzak_mcp"], "yayin_anahtari": k["yayin_anahtari"]}
    if k.get("dagitim_deposu"):  # private dağıtım: indirme GitHub API'siyle, gömülü salt okunur jetonla
        ayar.update(dagitim_deposu=k["dagitim_deposu"], jeton=k.get("istemci_jetonu", ""), manifest_url="")
        if not k.get("istemci_jetonu"):
            print("  Uyarı: private dağıtım seçili ama istemci jetonu yok; kurulumlar güncelleme alamaz.")
    ortak.json_yaz(hazirlik / "ayar.json", ayar)

    # Yedek kurulum yolu: Akıllı Uygulama Denetimi açık bilgisayarlarda imzasız kurulum motoru
    # engellenir, PSF imzalı python.exe engellenmez. Aynı içerik, motor yerine Python.
    (hazirlik / "KUR.cmd").write_text(
        '@echo off\r\nchcp 65001 >nul\r\nset PYTHONIOENCODING=utf-8\r\ntitle ArthurLegal kurulumu\r\n'
        'echo ArthurLegal kuruluyor, lutfen bekleyin...\r\necho.\r\n'
        '"%~dp0runtime\\python.exe" -B "%~dp0bin\\al.py" kur --zip-kurulum\r\necho.\r\npause\r\n', encoding="ascii")
    (hazirlik / "BENIOKU.txt").write_text(
        "ArthurLegal kurulumu (zip)\r\n\r\n"
        "Bu zip, kurulum dosyası (.exe) Windows tarafından engellendiğinde kullanılır:\r\n"
        "\"Bir Uygulama Denetimi ilkesi bu dosyayı engelledi\" / \"Hata 4551\".\r\n\r\n"
        "1. Zip'i sağ tıklayıp \"Tümünü ayıkla\" ile bir klasöre çıkarın (zip içinden çalıştırmayın).\r\n"
        "2. KUR.cmd dosyasına çift tıklayın. Yönetici yetkisi gerekmez.\r\n"
        "3. Kurulum bitince açılan rehberdeki talimatı Claude'da bir Projeye yapıştırın.\r\n\r\n"
        "Bu yolla Arthur Mask kurulmaz: müvekkil belgesi maskeleme ve UYAP bağlantısı çalışmaz.\r\n"
        "ArthurLegal paketleri, araştırma araçları ve Tapu çalışır.\r\n\r\n"
        "Kaldırmak için: %LOCALAPPDATA%\\Programs\\ArthurLegal\\KALDIR.cmd\r\n", encoding="utf-8-sig")
    kurulum_zip = CIKTI / f"{ad}.zip"
    zip_yap(hazirlik, kurulum_zip)
    print(f"  yedek kurulum: {kurulum_zip.name} ({kurulum_zip.stat().st_size // (1024 * 1024)} MB)")

    zip_adi = f"arthurlegal-paket-{surum}.zip"
    zip_yap(hazirlik / "surumler" / surum, CIKTI / zip_adi)
    mask = mask_bilgisi(k)
    ortak.json_yaz(CIKTI / "derleme.json", {
        "surum": surum, "icerik": {"paketler": icerik["paketler"], "bilesenler": icerik["bilesenler"]},
        "kaynak": icerik["kaynak"], "mask": mask,
        "paket": {"dosya": zip_adi, "sha256": sha256(CIKTI / zip_adi), "boyut": (CIKTI / zip_adi).stat().st_size}})
    print(f"  paket: {zip_adi} ({(CIKTI / zip_adi).stat().st_size // 1024} KB)")

    if not args.exe_yok:
        # Kod imzalama (isteğe bağlı): signtool komutu, imzalanacak dosya yerine $f, tırnak yerine $q.
        # Ör. Azure Trusted Signing: signtool sign /fd SHA256 /tr http://timestamp.acs.microsoft.com /td SHA256
        #     /dlib <Azure.CodeSigning.Dlib.dll> /dmdf <metadata.json> $f
        imza = os.environ.get("ARTHURLEGAL_IMZA_KOMUTU") or k.get("imzalama", {}).get("komut")
        imza_args = [f"/Simzaci={imza}", "/DImzali=1"] if imza else []
        if not imza:
            print("  Uyarı: kod imzası yok. Windows 11 Akıllı Uygulama Denetimi açık bilgisayarlarda kurulum çalışmaz;"
                  " SmartScreen 'Yine de çalıştır' ister (README: Kod imzalama).")
        r = subprocess.run([str(iscc_bul()), f"/DKaynak={hazirlik}", f"/DSurum={surum}", f"/DFirmaAd={firma.get('ad', '')}",
                            f"/DCiktiDizini={CIKTI}", f"/DCiktiAdi={ad}", f"/DMaskUrl={mask['url']}",
                            f"/DMaskSha={mask['sha256']}", f"/DVarlik={BURASI / 'varlik'}", *imza_args, "/Qp", str(iss)])
        if r.returncode:
            sys.exit(f"ISCC hata verdi ({r.returncode})")
        exe = CIKTI / f"{ad}.exe"
        print(f"  kurulum: {exe} ({exe.stat().st_size // (1024 * 1024)} MB, sha256 {sha256(exe)[:16]}…)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
