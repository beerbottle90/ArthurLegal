"""ArthurLegal macOS kurulum paketini (ArthurLegal-Kurulum.pkg) derler. Yalnız macOS'ta çalışır (pkgbuild,
productbuild, iconutil, uv); GitHub Actions'taki macOS bilgisayarında: .github/workflows/macos-kurulum.yml.

    python yayin/derle_macos.py                  yayin/cikti/ArthurLegal-Kurulum.pkg ve derleme-macos.json
    python yayin/derle_macos.py --calisma-agaci  commitlenmemiş değişiklikler de girer

Paketler, istemci, Tapu, başlangıç rehberi, lisans ve ayar Windows derlemesiyle aynı kaynaktan ve aynı işlevlerle
hazırlanır (derle.py); güncelleme kanalı da aynıdır (releases/latest, aynı imzalı paket). Farklar:

- Python: python-build-standalone 3.12 (uv ile), Apple Silicon ve Intel için ikisi birden. Kurulumda bilgisayarın
  işlemcisine uyan kalır, öteki silinir.
- Sihirbaz: macOS Installer. Karşılama, lisans, modül seçimi (Özelleştir; her modülün başlığı ve seçilince altta
  açıklaması), kurulum, bitiş. Yalnız kullanıcının ev klasörüne kurulur, yönetici şifresi istemez:
  ~/Library/Application Support/ArthurLegal.
- Modüller: her modül küçük bir bileşen paketidir; seçilen bileşen kurulum klasörüne bir işaret dosyası bırakır
  (secim/<kod>). En son kurulan bileşenin betiği (kurulum/macos/postinstall) işaretleri kur.py'ye --moduller olarak
  geçirir. Önceki seçim onceki/ klasöründe durur; kurulum yeniden açılınca o kutular işaretli gelir.
- Modül başlıkları ve açıklamaları Windows sihirbazınınkiyle aynıdır: kurulum/ArthurLegal.iss'teki Modul*
  iletilerinden okunur.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "yayin"))
import derle  # noqa: E402
from derle import CIKTI, ortak  # noqa: E402

KIMLIK = "com.arthurlegal"
KURULUM_YERI = "/Library/Application Support/ArthurLegal"  # ev klasörüne kurulumda ~/Library/... olur
MODUL_ILETISI = {"hukuk-burosu": "ModulHukuk", "kurumsal": "ModulKurumsal", "adliye": "ModulAdliye",
                 "akademisyen": "ModulAkademisyen", "tapu": "ModulTapu", "mask": "ModulMask"}
# Python'un kurulumda gerekmeyen parçaları (yalnız standart kütüphane kullanılır; test, tkinter ve araçlar yok).
# lib/libpython3.12.dylib kalır: bin/python3.12 ona bağlıdır.
ATILACAK = ("lib/python3.12/test", "lib/python3.12/idlelib", "lib/python3.12/tkinter", "lib/python3.12/turtledemo",
            "lib/python3.12/ensurepip", "lib/python3.12/lib2to3", "lib/python3.12/pydoc_data", "lib/python3.12/config-*",
            "lib/python3.12/lib-dynload/_tkinter*", "lib/tcl*", "lib/tk*", "lib/itcl*", "lib/thread*", "lib/pkgconfig",
            "include", "share")


def calistir(komut, **k):
    print("  $ " + " ".join(str(x) for x in komut))
    return subprocess.run([str(x) for x in komut], check=True, **k)


# Arthur Mask'in Mac sürümünün koşulu: seçenek öteki Mac'lerde soluk gelir, nedeni açıklamasında yazar.
MASK_KOSULU = {"tr": " Mac'te Apple Silicon (M1 ve sonrası) ve macOS 14 gerekir.",
               "en": " On a Mac it needs Apple Silicon (M1 or later) and macOS 14."}


def iletiler() -> dict:
    """Modül ekranının metinleri, Windows sihirbazıyla aynı kaynaktan (ArthurLegal.iss [CustomMessages])."""
    iss = (BURASI / "kurulum" / "ArthurLegal.iss").read_text(encoding="utf-8-sig")
    sonuc = {"tr": {}, "en": {}}
    for satir in iss.splitlines():
        m = re.match(r"^(tr|en)\.(Modul\w+)=(.*)$", satir)
        if m:
            sonuc[m.group(1)][m.group(2)] = m.group(3).replace("%n", "\n")
    for dil, ek in MASK_KOSULU.items():
        sonuc[dil]["ModulMaskAciklama"] = sonuc[dil].get("ModulMaskAciklama", "") + ek
    return sonuc


def python_hazirla(k: dict, hedef: Path) -> dict:
    """İki işlemci için Python (uv'nin python-build-standalone derlemeleri; uv indirdiğinin sha256'sını kendi
    listesiyle doğrular): runtime-arm64 ve runtime-x86_64. Öteki işlemcinin Python'u çalıştırılmadan, uv'nin kurulum
    klasöründen alınır (Intel Python'u Apple Silicon derleyicide ancak Rosetta'yla açılır)."""
    surum = k["python_macos"]["surum"]
    dizin = Path(subprocess.run(["uv", "python", "dir"], check=True, capture_output=True, text=True).stdout.strip())
    surumler = {}
    for mimari, ad in (("aarch64", "arm64"), ("x86_64", "x86_64")):
        istek = f"cpython-{surum}-macos-{mimari}-none"
        calistir(["uv", "python", "install", istek])
        kok = dizin / istek
        if not (kok / "bin" / "python3").exists():
            bulunan = ", ".join(p.name for p in dizin.iterdir()) if dizin.is_dir() else "klasör yok"
            sys.exit(f"Python bulunamadı: {kok} ({bulunan})")
        yer = hedef / f"runtime-{ad}"
        shutil.rmtree(yer, ignore_errors=True)
        shutil.copytree(kok, yer, symlinks=True)
        for desen in ATILACAK:
            for parca in yer.glob(desen):
                if parca.is_dir() and not parca.is_symlink():
                    shutil.rmtree(parca)
                else:
                    parca.unlink()
        for p in list(yer.rglob("__pycache__")):
            shutil.rmtree(p, ignore_errors=True)
        (yer / "lib" / "python3.12" / "EXTERNALLY-MANAGED").unlink(missing_ok=True)
        surumler[ad] = subprocess.run([str(yer / "bin" / "python3"), "-c", "import sys; print(sys.version.split()[0])"],
                                      capture_output=True, text=True).stdout.strip() or "?"
        print(f"  Python {ad}: {surumler[ad]} ({sum(1 for _ in yer.rglob('*'))} dosya)")
    return surumler


def simge_hazirla(hedef: Path) -> None:
    """Windows simgesinin (varlik/gorseller.py, 16x16 pixel art) macOS biçimi (.icns): her boyut pikselin tam katıyla
    büyütülür, keskin kalır. Yalnız standart kütüphane ve macOS'un iconutil'i."""
    sys.path.insert(0, str(BURASI / "varlik"))
    import gorseller
    tuval = gorseller.simge_tuvali()
    takim = hedef.parent / "arthurlegal.iconset"
    shutil.rmtree(takim, ignore_errors=True)
    takim.mkdir(parents=True)
    for boyut in (16, 32, 128, 256, 512):
        for kat, ek in ((1, ""), (2, "@2x")):
            tuval.png_yaz(takim / f"icon_{boyut}x{boyut}{ek}.png", boyut * kat // tuval.en)
    calistir(["iconutil", "-c", "icns", takim, "-o", hedef])
    shutil.rmtree(takim, ignore_errors=True)


def strings_yaz(yol: Path, cift: dict) -> None:
    """Localizable.strings (UTF-16, Installer'ın beklediği biçim)."""
    kac = lambda s: s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")  # noqa: E731
    metin = "".join(f'"{kac(a)}" = "{kac(d)}";\n' for a, d in cift.items())
    yol.write_bytes(metin.encode("utf-16"))


SAYFA = """<!doctype html><html lang="{dil}"><head><meta charset="utf-8"><style>
body{{font:13px -apple-system,"Helvetica Neue",sans-serif;color:#1b2433;margin:0 4px}}h2{{font-size:15px;margin:4px 0 10px}}
li{{margin:4px 0}}.not{{color:#5b6576;font-size:12px}}</style></head><body>{govde}</body></html>"""

METIN = {
    "tr": {
        "baslik": "ArthurLegal",
        "karsilama": """<h2>ArthurLegal kurulumu</h2>
<p>Bu kurulum, seçtiğiniz hukuk asistanı paketlerini ve araçları Claude Desktop'a bağlar.</p>
<ul><li>Bir sonraki ekranlardan birinde <b>kurmak istediğiniz modülleri işaretleyin</b>. Bir modülü seçince ne işe
yaradığı altta yazar. İlk kurulumda hiçbir kutu işaretli gelmez; <b>en az bir paket</b> gerekir: Hukuk Bürosu,
Kurumsal Asistan, Courthouse ya da Akademisyen.</li>
<li>Kurulum yalnız sizin kullanıcı hesabınıza yapılır, yönetici şifresi istemez.</li>
<li>Arthur Mask'i seçtiyseniz kurulumdan sonra arka planda iner (yaklaşık 1,2 GB) ve hazır olunca bildirim gelir.
Arthur Mask Mac'te Apple Silicon (M1 ve sonrası) ve macOS 14 (Sonoma) ya da sonrasını ister.</li>
<li>Güncellemeler bundan sonra arka planda, imzaları doğrulanarak kendiliğinden kurulur.</li></ul>""",
        "bitis": """<h2>ArthurLegal kuruldu</h2>
<p>Seçtiğiniz modüllerin simgeleri Uygulamalar klasöründe ve masaüstünde. Başlangıç rehberi tarayıcıda açılır.</p>
<ul><li>Claude Desktop açıksa <b>Cmd+Q</b> ile tamamen çıkıp yeniden açın; sonra yeni bir sohbet açıp sorunuzu
yazın. Claude bir aracı ilk kez kullanırken izin sorarsa <b>Always allow</b>'u seçin.</li>
<li>Claude Desktop kurulu değilse <b>claude.ai/download</b> adresinden kurun.</li>
<li>Modül eklemek ya da çıkarmak için bu kurulumu yeniden çalıştırın; son seçiminiz işaretli gelir.</li></ul>
<p class="not">Kaldırmak için: Uygulamalar &gt; ArthurLegal &gt; ArthurLegal'i Kaldır.</p>""",
        "paket_yok": "En az bir paket seçin: Hukuk Bürosu, Kurumsal Asistan, Courthouse ya da Akademisyen. "
                     "Kurulum tamamlanmadı; kurulum dosyasını yeniden açıp bir paket işaretleyin.",
    },
    "en": {
        "baslik": "ArthurLegal",
        "karsilama": """<h2>ArthurLegal setup</h2>
<p>This setup connects the legal assistant packages and tools you choose to Claude Desktop.</p>
<ul><li>On one of the next screens, <b>tick the modules you want to install</b>. Select a module to see what it does
below the list. Nothing is ticked on a first installation; <b>at least one package</b> is needed: Law Firm, Corporate
Assistant, Courthouse or Academician.</li>
<li>Setup installs for your user account only and does not ask for an administrator password.</li>
<li>If you choose Arthur Mask, it downloads in the background after setup (about 1.2 GB) and a notification tells you
when it is ready. On a Mac, Arthur Mask needs Apple Silicon (M1 or later) and macOS 14 (Sonoma) or later.</li>
<li>From now on, updates install themselves in the background after their signatures are verified.</li></ul>""",
        "bitis": """<h2>ArthurLegal is installed</h2>
<p>The icons of the modules you chose are in the Applications folder and on the desktop. The start guide opens in
your browser.</p>
<ul><li>If Claude Desktop is open, quit it completely with <b>Cmd+Q</b> and open it again; then open a new chat and
type your question. When Claude asks for permission the first time it uses a tool, choose <b>Always allow</b>.</li>
<li>If Claude Desktop is not installed, get it from <b>claude.ai/download</b>.</li>
<li>To add or remove modules, run this setup again; your last choice comes pre-ticked.</li></ul>
<p class="not">To uninstall: Applications &gt; ArthurLegal &gt; Uninstall ArthurLegal.</p>""",
        "paket_yok": "Choose at least one package: Law Firm, Corporate Assistant, Courthouse or Academician. Setup did "
                     "not finish; open the installer again and tick a package.",
    },
}


def dagitim_yaz(yol: Path, surum: str, moduller: list) -> None:
    """Distribution.xml: modül seçimi (Özelleştir her zaman açılır), yalnız ev klasörüne kurulum, Arthur Mask'in koşulu
    (Apple Silicon, macOS 14) ve önceki seçim için Installer JavaScript'i. Bileşenler seçim sırasıyla kurulur: önce çekirdek, sonra işaretler, en son
    postinstall'u çalışan 'son' bileşeni."""
    satirlar = "\n".join(f'    <line choice="{m}"/>' for m in moduller)
    secimler = []
    for m in moduller:
        ek = ' start_enabled="mask_uygun()"' if m == "mask" else ""
        secili = f"onceki('{m}') &amp;&amp; mask_uygun()" if m == "mask" else f"onceki('{m}')"
        secimler.append(f'  <choice id="{m}" title="{MODUL_ILETISI[m]}" description="{MODUL_ILETISI[m]}Aciklama" '
                        f'start_selected="{secili}"{ek}>\n    <pkg-ref id="{KIMLIK}.modul.{m}"/>\n  </choice>')
    paketler = "\n".join(f'  <pkg-ref id="{KIMLIK}.{ad}" version="{surum}" auth="none">{ad}.pkg</pkg-ref>'
                         for ad in ["cekirdek", "son"] + [f"modul.{m}" for m in moduller])
    yol.write_text(f"""<?xml version="1.0" encoding="utf-8"?>
<installer-gui-script minSpecVersion="2">
  <title>KurulumBasligi</title>
  <welcome file="Welcome.html" mime-type="text/html"/>
  <license file="License.txt" mime-type="text/plain"/>
  <conclusion file="Conclusion.html" mime-type="text/html"/>
  <options customize="always" require-scripts="false" hostArchitectures="arm64,x86_64"/>
  <domains enable_anywhere="false" enable_currentUserHome="true" enable_localSystem="false"/>
  <volume-check>
    <allowed-os-versions><os-version min="11.0"/></allowed-os-versions>
  </volume-check>
  <script><![CDATA[
function onceki(kod) {{
  try {{ return system.files.fileExistsAtPath(system.env.HOME + '/Library/Application Support/ArthurLegal/onceki/' + kod); }}
  catch (e) {{ return false; }}
}}
function mask_uygun() {{
  var arm = true, surum = true;
  try {{ arm = system.sysctl('hw.optional.arm64') == 1; }} catch (e) {{}}
  try {{ surum = system.compareVersions(system.version.ProductVersion, '14.0') >= 0; }} catch (e) {{}}
  return arm && surum;
}}
  ]]></script>
  <choices-outline>
    <line choice="cekirdek"/>
{satirlar}
    <line choice="son"/>
  </choices-outline>
  <choice id="cekirdek" visible="false" selected="true" enabled="false">
    <pkg-ref id="{KIMLIK}.cekirdek"/>
  </choice>
{chr(10).join(secimler)}
  <choice id="son" visible="false" selected="true" enabled="false">
    <pkg-ref id="{KIMLIK}.son"/>
  </choice>
{paketler}
</installer-gui-script>
""", encoding="utf-8")


def betik_yaz(klasor: Path, ad: str, metin: str) -> None:
    klasor.mkdir(parents=True, exist_ok=True)
    (klasor / ad).write_text(metin, encoding="utf-8", newline="\n")
    (klasor / ad).chmod(0o755)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal macOS kurulum paketi")
    ap.add_argument("--calisma-agaci", action="store_true", help="commitlenmemiş değişiklikleri de al")
    args = ap.parse_args(argv)
    if sys.platform != "darwin":
        sys.exit("macOS kurulum paketi yalnız macOS'ta derlenir (GitHub Actions: macos-kurulum.yml).")
    for arac in ("pkgbuild", "productbuild", "iconutil", "uv"):
        if not shutil.which(arac):
            sys.exit(f"{arac} bulunamadı")
    derle.CALISMA_AGACI = args.calisma_agaci
    k = derle.kaynaklar()
    surum = k["surum"]
    hazirlik = CIKTI / "hazirlik-macos"
    shutil.rmtree(hazirlik, ignore_errors=True)
    kok = hazirlik / "kok"
    kok.mkdir(parents=True)
    print(f"ArthurLegal macOS kurulumu {surum} derleniyor → ArthurLegal-Kurulum.pkg")

    # 1) Windows derlemesiyle ortak olanlar: sürüm klasörü (istemci, paketler, Tapu), başlatıcı, rehber, lisans, ayar.
    icerik = derle.paket_hazirla(k, kok / "surumler" / surum)
    derle.kopyala(BURASI / "bin", kok / "bin", lambda g: g.endswith(".py"))
    derle.varlik_uret()
    simge_hazirla(kok / "bin" / "arthurlegal.icns")
    derle.rehber_yaz(kok, "", icerik)
    for ad, hedef in (("rehber-banner.png", "banner.png"), ("rehber-banner-en.png", "banner-en.png")):
        shutil.copy2(BURASI / "varlik" / ad, kok / "rehber" / hedef)
    derle.lisans_yaz(k, kok)
    ortak.json_yaz(kok / "ayar.json", {
        "manifest_url": f"https://github.com/{k['yayin_deposu']}/releases/latest/download/arthurlegal-manifest.json",
        "yedek_depo": k["yayin_deposu"], "kanal": k.get("kanal", "kararli"),
        "uzak_mcp": k["uzak_mcp"], "yayin_anahtari": k["yayin_anahtari"]})
    python_surumleri = python_hazirla(k, kok)

    # 2) Bileşen paketleri: çekirdek (bütün dosyalar), her modül için işaret, en son kur.py'yi çağıran 'son'.
    paket_dizini = hazirlik / "paketler"
    paket_dizini.mkdir()
    betik_yaz(hazirlik / "betik-cekirdek", "preinstall",
              '#!/bin/bash\n# Yarım kalmış bir önceki kurulumdan kalan seçim işaretleri silinir ($2: kurulum klasörü).\n'
              'for d in "$2" "$HOME/Library/Application Support/ArthurLegal"; do\n'
              '  [ -n "$d" ] && [ -d "$d/secim" ] && rm -rf "$d/secim"\n'
              'done\nexit 0\n')
    calistir(["pkgbuild", "--root", kok, "--identifier", f"{KIMLIK}.cekirdek", "--version", surum,
              "--install-location", KURULUM_YERI, "--scripts", hazirlik / "betik-cekirdek",
              paket_dizini / "cekirdek.pkg"])
    moduller = [m for m in ortak.MODULLER if m in ("tapu", "mask") or m in icerik["paketler"]]
    if not icerik["bilesenler"].get("tapu"):
        moduller.remove("tapu")
    for m in moduller:
        isaret = hazirlik / f"isaret-{m}" / "secim"
        isaret.mkdir(parents=True)
        (isaret / m).write_text("", encoding="utf-8")
        calistir(["pkgbuild", "--root", isaret.parent, "--identifier", f"{KIMLIK}.modul.{m}", "--version", surum,
                  "--install-location", KURULUM_YERI, paket_dizini / f"modul.{m}.pkg"])
    son = (BURASI / "kurulum" / "macos" / "postinstall").read_text(encoding="utf-8").replace("\r\n", "\n")
    son = son.replace("{{PAKET_YOK_TR}}", METIN["tr"]["paket_yok"]).replace("{{PAKET_YOK_EN}}", METIN["en"]["paket_yok"])
    betik_yaz(hazirlik / "betik-son", "postinstall", son)
    calistir(["pkgbuild", "--nopayload", "--identifier", f"{KIMLIK}.son", "--version", surum,
              "--scripts", hazirlik / "betik-son", paket_dizini / "son.pkg"])

    # 3) Sihirbaz: karşılama, lisans, modül seçimi, bitiş; Türkçe ve İngilizce.
    kaynak = hazirlik / "kaynak"
    ileti = iletiler()
    for dil, lisans in (("tr", "LISANS.txt"), ("en", "LICENSE.txt")):
        d = kaynak / f"{'tr' if dil == 'tr' else 'en'}.lproj"
        d.mkdir(parents=True)
        (d / "License.txt").write_bytes((kok / lisans).read_bytes().removeprefix(b"\xef\xbb\xbf"))
        (d / "Welcome.html").write_text(SAYFA.format(dil=dil, govde=METIN[dil]["karsilama"]), encoding="utf-8")
        (d / "Conclusion.html").write_text(SAYFA.format(dil=dil, govde=METIN[dil]["bitis"]), encoding="utf-8")
        strings_yaz(d / "Localizable.strings", {"KurulumBasligi": f"{METIN[dil]['baslik']} {surum}",
                                                **{a: html.unescape(v) for a, v in ileti[dil].items()}})
    dagitim_yaz(hazirlik / "Distribution.xml", surum, moduller)
    pkg = CIKTI / "ArthurLegal-Kurulum.pkg"
    pkg.unlink(missing_ok=True)
    calistir(["productbuild", "--distribution", hazirlik / "Distribution.xml", "--resources", kaynak,
              "--package-path", paket_dizini, pkg])
    ozet = hashlib.sha256(pkg.read_bytes()).hexdigest()
    ortak.json_yaz(CIKTI / "derleme-macos.json", {
        "surum": surum, "icerik": {"paketler": icerik["paketler"], "bilesenler": icerik["bilesenler"]},
        "kaynak": icerik["kaynak"], "python": python_surumleri, "moduller": moduller,
        "kurulum": {pkg.name: ozet}})
    print(f"  kurulum: {pkg} ({pkg.stat().st_size // (1024 * 1024)} MB, sha256 {ozet[:16]}…)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
