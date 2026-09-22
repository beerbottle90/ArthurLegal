"""Derlenen sürümü imzalar ve public ArthurLegal deposunun GitHub Release'ine koyar.

    python yayin/yayinla.py --anahtar-uret        ilk kez: yayın anahtarı (gizli kısım depoya GİRMEZ)
    python yayin/yayinla.py v2.0.0 --kuru         yalnız imzalı manifest üret, yükleme yapma
    python yayin/yayinla.py v2.0.0 --on-surum     pre-release: avukatların güncelleyicisi görmez
    python yayin/yayinla.py v2.0.0                latest olarak yayımla: kurulu bilgisayarlar 6 saat içinde alır

Önce: python yayin/derle.py  (standart kurulum ve paket zip'i). Etiket zaten varsa (ör. sürüm notu
elle açıldıysa) dosyalar o yayına eklenir. Büroya özel kurulumlar ve büro katmanı YÜKLENMEZ.
Gizli anahtar: %USERPROFILE%\\.arthurlegal\\imza\\yayin_anahtari.hex — yedekleyin; kaybolursa kurulu
bilgisayarlar yeni güncelleme alamaz, herkese yeni kurulum dosyası gerekir.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
CIKTI = BURASI / "yayin" / "cikti"
sys.path.insert(0, str(BURASI / "istemci"))
import ed25519  # noqa: E402
import ortak  # noqa: E402

ANAHTAR = Path.home() / ".arthurlegal" / "imza" / "yayin_anahtari.hex"


def kaynaklar() -> dict:
    return json.loads((BURASI / "kaynaklar.json").read_text(encoding="utf-8"))


def anahtar_uret() -> int:
    if ANAHTAR.exists():
        sys.exit(f"Anahtar zaten var: {ANAHTAR}")
    tohum = os.urandom(32)
    ANAHTAR.parent.mkdir(parents=True, exist_ok=True)
    ANAHTAR.write_text(tohum.hex(), encoding="ascii")
    k = kaynaklar()
    k["yayin_anahtari"] = ed25519.public_key(tohum).hex()
    (BURASI / "kaynaklar.json").write_text(json.dumps(k, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Gizli anahtar: {ANAHTAR}  (YEDEKLEYİN, depoya koymayın)\nAçık anahtar kaynaklar.json'a yazıldı: {k['yayin_anahtari']}")
    return 0


def github_jetonu() -> str:
    r = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                       capture_output=True, text=True, timeout=60)
    jeton = next((s.split("=", 1)[1] for s in r.stdout.splitlines() if s.startswith("password=")), "")
    if not jeton:
        sys.exit("GitHub kimliği alınamadı (git credential). Bir kez 'git push' ile oturum açın.")
    return jeton


def api(yontem: str, url: str, jeton: str, veri=None, tur="application/json"):
    govde = veri if isinstance(veri, (bytes, type(None))) else json.dumps(veri).encode("utf-8")
    basliklar = {"Authorization": f"Bearer {jeton}", "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28", "Content-Type": tur}
    istek = urllib.request.Request(url, data=govde, method=yontem, headers=basliklar)
    with urllib.request.urlopen(istek, timeout=600) as r:
        ham = r.read()
    return json.loads(ham) if ham else None


class _Yonlendirmesiz(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def indirme_linki(etiket: str, dosya: str) -> int:
    """Private yayındaki bir dosya için imzalı, kısa ömürlü (birkaç dakika) indirme adresi verir.
    Adresi alan kişinin GitHub hesabı olması gerekmez; süresi dolunca adres çalışmaz."""
    k = kaynaklar()
    depo = k.get("dagitim_deposu") or k["yayin_deposu"]
    jeton = github_jetonu()
    yayin = api("GET", f"https://api.github.com/repos/{depo}/releases/tags/{etiket}", jeton)
    varlik = next((a for a in yayin.get("assets", []) if a["name"] == dosya), None)
    if not varlik:
        sys.exit(f"{etiket} yayınında yok: {dosya}\nVar olanlar: " + ", ".join(a["name"] for a in yayin.get("assets", [])))
    istek = urllib.request.Request(varlik["url"], headers={
        "Authorization": f"Bearer {jeton}", "Accept": "application/octet-stream", "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.build_opener(_Yonlendirmesiz).open(istek, timeout=60) as y:
            sys.exit(f"Beklenen yönlendirme gelmedi (HTTP {y.status}).")
    except urllib.error.HTTPError as e:
        adres = e.headers.get("Location")
    if not adres:
        sys.exit("İndirme adresi alınamadı.")
    print(f"{dosya} ({varlik['size'] // (1024 * 1024)} MB) — adres birkaç dakika geçerlidir:\n\n{adres}\n")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal yayını")
    ap.add_argument("etiket", nargs="?")
    ap.add_argument("--anahtar-uret", action="store_true")
    ap.add_argument("--link", metavar="DOSYA", help="private yayındaki dosya için geçici indirme adresi üret")
    ap.add_argument("--kararli-yap", action="store_true", help="var olan ön sürümü kararlıya çevir (sessiz güncelleme açılır)")
    ap.add_argument("--kuru", action="store_true")
    ap.add_argument("--on-surum", action="store_true")
    args = ap.parse_args(argv)
    if args.anahtar_uret:
        return anahtar_uret()
    if args.link:
        if not args.etiket:
            ap.error("etiket gerekli: python yayin/yayinla.py v2.0.0 --link ArthurLegal-Kurulum.exe")
        return indirme_linki(args.etiket, args.link)
    if args.kararli_yap:
        if not args.etiket:
            ap.error("etiket gerekli (ör. v2.0.0)")
        k = kaynaklar()
        depo = k.get("dagitim_deposu") or k["yayin_deposu"]
        jeton = github_jetonu()
        yayin = api("GET", f"https://api.github.com/repos/{depo}/releases/tags/{args.etiket}", jeton)
        api("PATCH", yayin["url"], jeton, {"prerelease": False, "make_latest": "true"})
        print(f"{args.etiket} kararlı sürüm oldu; kurulu bilgisayarlar 6 saat içinde günceller.")
        return 0
    if not args.etiket:
        ap.error("etiket gerekli (ör. v2.0.0)")

    k, d = kaynaklar(), ortak.json_oku(CIKTI / "derleme.json")
    if not d:
        sys.exit("Önce derleyin: python yayin/derle.py")
    depo = k.get("dagitim_deposu") or k["yayin_deposu"]
    manifest = {
        "urun": "arthurlegal-yerel", "surum": d["surum"], "etiket": args.etiket,
        "taban": f"https://github.com/{depo}/releases/download/{args.etiket}/",
        "tarih": time.strftime("%Y-%m-%d"), "paket": d["paket"], "mask": d["mask"], "icerik": d["icerik"],
    }
    ham = json.dumps(manifest, ensure_ascii=False, indent=1).encode("utf-8")
    gizli = bytes.fromhex(ANAHTAR.read_text(encoding="ascii").strip())
    if ed25519.public_key(gizli).hex() != k["yayin_anahtari"]:
        sys.exit("Gizli anahtar kaynaklar.json'daki açık anahtarla eşleşmiyor.")
    imza = ed25519.sign(gizli, ham)
    assert ed25519.verify(bytes.fromhex(k["yayin_anahtari"]), ham, imza)
    (CIKTI / "arthurlegal-manifest.json").write_bytes(ham)
    (CIKTI / "arthurlegal-manifest.sig").write_text(imza.hex(), encoding="ascii")
    print(f"İmzalı manifest: sürüm {d['surum']}, etiket {args.etiket}")
    if args.kuru:
        return 0

    dosyalar = ["arthurlegal-manifest.json", "arthurlegal-manifest.sig", d["paket"]["dosya"]]
    # Depo private olduğu için büroya özel kurulumlar da buraya konur; .zip yolu Akıllı Uygulama
    # Denetimi açık bilgisayarlar içindir. Public bir depoya yayımlanıyorsa büro dosyaları dışarıda kalır.
    kurulumlar = sorted(y.name for y in CIKTI.glob("ArthurLegal-Kurulum*") if y.suffix in (".exe", ".zip"))
    if depo == k.get("yayin_deposu"):
        kurulumlar = [a for a in kurulumlar if a in ("ArthurLegal-Kurulum.exe", "ArthurLegal-Kurulum.zip")]
    dosyalar += kurulumlar
    jeton = github_jetonu()
    taban = f"https://api.github.com/repos/{depo}/releases"
    try:
        yayin = api("GET", f"{taban}/tags/{args.etiket}", jeton)
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
        yayin = api("POST", taban, jeton, {
            "tag_name": args.etiket, "name": f"ArthurLegal {args.etiket}", "prerelease": args.on_surum,
            "make_latest": "false" if args.on_surum else "true",
            "body": f"Yerel kurulum {d['surum']} · Hukuk Bürosu {d['icerik']['paketler'].get('hukuk-burosu')} · "
                    f"Kurumsal {d['icerik']['paketler'].get('kurumsal')}\n\nKurulum: ArthurLegal-Kurulum.exe"})
    for varlik in yayin.get("assets", []):
        if varlik["name"] in dosyalar:
            api("DELETE", varlik["url"], jeton)
    yukleme = yayin["upload_url"].split("{", 1)[0]
    for ad in dosyalar:
        api("POST", f"{yukleme}?name={urllib.parse.quote(ad)}", jeton, (CIKTI / ad).read_bytes(), "application/octet-stream")
        print(f"  yüklendi: {ad}")
    print(f"Yayın: {yayin['html_url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
