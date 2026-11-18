"""Derlenen sürümü imzalar ve public ArthurLegal deposunun GitHub Release'ine koyar.

    python yayin/yayinla.py --anahtar-uret        ilk kez: yayın anahtarı (gizli kısım depoya GİRMEZ)
    python yayin/yayinla.py --kasa-anahtari-uret  bir kez: kasada duracak yedek anahtar
    python yayin/yayinla.py v2.0.0 --kuru         yalnız imzalı manifest üret, yükleme yapma
    python yayin/yayinla.py v2.0.0 --on-surum     pre-release: avukatların güncelleyicisi görmez
    python yayin/yayinla.py v2.0.0                latest olarak yayımla: kurulu bilgisayarlar 6 saat içinde alır
    python yayin/yayinla.py v2.0.0 --kasa         günlük anahtar kayıpsa kasadaki yedekle imzala
    python yayin/yayinla.py v2.0.0 --sinavsiz     sürüm sınavını bilerek atla
    python yayin/yayinla.py v2.0.0 --deneme win,mac,chatgpt   yayın sonrası denemede geçen ortamları nota yaz
    python yayin/yayinla.py v2.0.0 --deneme-kaldi mac         kalan ortamı nota yaz (✗)
    python yayin/yayinla.py v2.0.0 --deneme-listesi           yayın sonrası deneme listesini yeniden yazdır

Yayın sonrası deneme (kalite süreci 4, kurulum sağlığı): yayın notu "Yayın sonrası deneme: Win … Mac … ChatGPT …"
satırıyla açılır ve yayından sonra deneme listesi yazdırılır. Üç ortamda (Windows Claude Desktop, macOS Claude
Desktop, ChatGPT masaüstü) aynı üç deneme yapılır; sonuç --deneme ile aynı satıra işlenir: "Win ✓ Mac ✓ ChatGPT ✓".

Sürüm sınavı (Katman 2): %USERPROFILE%/.arthurlegal/sinav.json varsa yayından önce bir kalite sınavı çalışır ve
kalite önceki sürüme göre düştüyse yayın durur (bkz. surum_sinavi). Ayar yoksa sınavsız devam edilir.
Sınavdan önce Claude eklentisinin (ArthurLegal-plugin/) depodaki paketten üretildiği denetlenir (eklenti_denetimi).

Önce: python yayin/derle.py  (standart kurulum ve paket zip'i). Etiket zaten varsa (ör. sürüm notu
elle açıldıysa) dosyalar o yayına eklenir. Büroya özel kurulumlar ve büro katmanı YÜKLENMEZ.

İndirme düğmesi (README) ve kurulu bilgisayarların güncelleyicisi releases/latest/download/... adresine bakar.
Bu yüzden yeni yayın önce TASLAK açılır, bütün dosyalar yüklenir, sonra tek adımda yayımlanıp Latest olur:
arada düğme "Not Found" vermez. Var olan bir yayının dosyası değişirken yeni dosya önce geçici adla yüklenir,
eskisi silinir ve yenisinin adı düzeltilir. Public depoya yalnız bu derlemenin (derleme.json'daki özetler) genel
kurulumu gider; UYAP'lı ya da başka bir derlemeden kalan kurulum dosyası yüklenmez.

Kurulumlar iki anahtara güvenir; liste paketin icerik.json'unda, güncellemeyle gelir:
- günlük yayın anahtarı: %USERPROFILE%\\.arthurlegal\\imza\\yayin_anahtari.hex — yedekleyin;
- kasa anahtarı: kâğıtta ya da USB bellekte, kasada durur; bilgisayarda kalmaz.
Günlük anahtar kaybolursa: kasadaki anahtarı imza klasörüne kasa_anahtari.hex adıyla yazın,
--anahtar-uret ile yeni günlük anahtar üretin, derleyin ve --kasa ile imzalayın. Kurulumlar yeni
listeyi bu güncellemeyle alır; kimsenin yeniden kurması gerekmez. İkisi birden kaybolursa kurulu
bilgisayarlar yeni güncelleme alamaz, herkese yeni kurulum dosyası gerekir.
"""
from __future__ import annotations

import argparse
import json
import os
import re
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
KASA = ANAHTAR.with_name("kasa_anahtari.hex")
SINAV_AYARI = Path.home() / ".arthurlegal" / "sinav.json"


def kaynaklar() -> dict:
    return json.loads((BURASI / "kaynaklar.json").read_text(encoding="utf-8"))


def anahtar_uret(kasa: bool = False) -> int:
    """Günlük yayın anahtarını ya da kasada duracak yedek anahtarı üretir; açık kısmı kaynaklar.json'a yazar."""
    dosya, alan = (KASA, "kasa_anahtari") if kasa else (ANAHTAR, "yayin_anahtari")
    if dosya.exists():
        sys.exit(f"Anahtar zaten var: {dosya}")
    k = kaynaklar()
    if kasa and k.get(alan):
        sys.exit("kaynaklar.json'da kasa anahtarı zaten var. Yenilemek bilinçli bir iştir: önce oradaki "
                 "kasa_anahtari satırını silin.")
    tohum = os.urandom(32)
    dosya.parent.mkdir(parents=True, exist_ok=True)
    dosya.write_text(tohum.hex(), encoding="ascii")
    k[alan] = ed25519.public_key(tohum).hex()
    sira = list(k)  # kasa anahtarı yayın anahtarının hemen altında dursun
    if kasa and "yayin_anahtari" in sira:
        sira.remove(alan)
        sira.insert(sira.index("yayin_anahtari") + 1, alan)
    k = {a: k[a] for a in sira}
    (BURASI / "kaynaklar.json").write_text(json.dumps(k, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if kasa:
        print(f"Kasa anahtarı: {dosya}\n  Kâğıda basın ya da USB belleğe alın, kasaya koyun, sonra bu dosyayı "
              f"bilgisayardan SİLİN.\nAçık anahtar kaynaklar.json'a yazıldı: {k[alan]}")
    else:
        print(f"Gizli anahtar: {dosya}  (YEDEKLEYİN, depoya koymayın)\nAçık anahtar kaynaklar.json'a yazıldı: {k[alan]}")
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


GECICI_ONEK = "yukleniyor-"  # var olan yayında dosya değişirken yeni dosyanın geçici adı


def _commitler(derleme: dict) -> dict:
    return {ad: (v or {}).get("commit") or "" for ad, v in (derleme.get("kaynak") or {}).items()}


# UYAP köprüsünün public kuruluma girebildiği tek dal.
UYAP_DALI = "origin/main"
# Yalnız Windows kurulumuna giren bileşenler: macOS paketi bunlarsız derlenir, karşılaştırmada sayılmaz.
YALNIZ_WINDOWS = ("uyap",)


def ayni_kaynaklar(a: dict, b: dict) -> bool:
    """İki derleme aynı depolardan, aynı commit'lerden mi? Kısa özetin uzunluğu deponun büyüklüğüne göre değişir
    (GitHub Actions'taki sığ klonda daha kısa olabilir): biri ötekinin başıysa aynı commit sayılır. Yalnız Windows'a
    giren bileşenler (UYAP) karşılaştırılmaz."""
    ca, cb = ({ad: c for ad, c in _commitler(d).items() if ad not in YALNIZ_WINDOWS} for d in (a, b))
    return bool(ca) and ca.keys() == cb.keys() and all(
        len(min(ca[ad], cb[ad], key=len)) >= 7 and (ca[ad].startswith(cb[ad]) or cb[ad].startswith(ca[ad])) for ad in ca)


def yuklenecek_kurulumlar(cikti: Path, derleme: dict, public: bool) -> list:
    """Yüklenecek kurulum dosyaları (.exe/.zip; varsa macOS'un .pkg'si). Public depoya yalnız genel
    ArthurLegal-Kurulum.exe/.zip/.pkg ve yalnız bu derlemenin dosyaları gider: özeti derleme.json'dakiyle uyuşmayan
    dosya (eski ya da bir deneme derlemesinden kalan) reddedilir. UYAP köprüsü (3.0.0'dan beri genel kurulumda) yalnız
    arthur-uyap'ın sabit dalından derlendiyse yüklenir: çalışılan bir daldan ya da yerel deneme derlemesinden gelen
    köprü public'e çıkmaz."""
    kurulumlar = sorted(y.name for y in cikti.glob("ArthurLegal-Kurulum*") if y.suffix in (".exe", ".zip"))
    if not public:
        return kurulumlar
    icerik = derleme.get("icerik") or {}
    if icerik.get("bilesenler", {}).get("uyap"):
        # derleme.json kaynakları üst düzeyde tutar (derle.py); içerikteki kopya eski biçim için.
        kaynak = (derleme.get("kaynak") or icerik.get("kaynak") or {}).get("uyap") or {}
        if kaynak.get("ref") != UYAP_DALI:
            sys.exit(f"Bu derlemenin UYAP köprüsü {UYAP_DALI} dalından değil ({kaynak.get('ref') or 'bilinmiyor'}); public depoya "
                     "yüklenmez. kaynaklar.json 'dallar' → uyap: origin/main ile yeniden derleyin.")
    ozetler = derleme.get("kurulum") or {}
    secilen = []
    for ad in ("ArthurLegal-Kurulum.exe", "ArthurLegal-Kurulum.zip"):
        if ad not in kurulumlar:
            continue
        if ozetler.get(ad) != ortak.sha256_dosya(cikti / ad):
            sys.exit(f"{ad} bu derlemeden değil (derleme.json'daki özetle uyuşmuyor; eski ya da başka bir derlemeden "
                     "kalmış olabilir). python yayin/derle.py ile yeniden derleyin.")
        secilen.append(ad)
    # macOS kurulum paketi (derle_macos.py, GitHub Actions'ta): aynı sürümün ve aynı kaynakların (ArthurLegal ve Tapu
    # commit'leri) derlemesi olmalı; iki kurulum aynı paketleri taşır.
    pkg = cikti / "ArthurLegal-Kurulum.pkg"
    if pkg.exists():
        mac = ortak.json_oku(cikti / "derleme-macos.json")
        if mac.get("surum") != derleme.get("surum") or not ayni_kaynaklar(mac, derleme):
            sys.exit("ArthurLegal-Kurulum.pkg bu derlemenin sürümünden ya da kaynaklarından değil (derleme-macos.json: "
                     f"{mac.get('surum')} {_commitler(mac)}; derleme.json: {derleme.get('surum')} {_commitler(derleme)}). "
                     "macOS paketini aynı commit'ten yeniden derleyin.")
        if (mac.get("kurulum") or {}).get(pkg.name) != ortak.sha256_dosya(pkg):
            sys.exit("ArthurLegal-Kurulum.pkg özeti derleme-macos.json'dakiyle uyuşmuyor.")
        secilen.append(pkg.name)
    return secilen


def taslak_bul(taban: str, jeton: str, etiket: str):
    """Yarım kalmış bir yayımlamadan kalan taslak (etiket aramasında taslaklar görünmez)."""
    for yayin in api("GET", f"{taban}?per_page=30", jeton) or []:
        if yayin.get("draft") and yayin.get("tag_name") == etiket:
            return yayin
    return None


def yayin_ac(taban: str, jeton: str, etiket: str, govde: str, on_surum: bool) -> tuple:
    """(yayın, yeni_mi). Var olan yayın aynen döner; yoksa taslak açılır (ya da yarım kalan taslak kullanılır)."""
    try:
        return api("GET", f"{taban}/tags/{etiket}", jeton), False
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
    taslak = taslak_bul(taban, jeton, etiket)
    if taslak:
        return taslak, True
    return api("POST", taban, jeton, {"tag_name": etiket, "name": f"ArthurLegal {etiket}", "draft": True,
                                      "prerelease": on_surum, "body": govde}), True


def dosyalari_yukle(yayin: dict, jeton: str, dosyalar: list, yeni: bool) -> None:
    """Taslağa doğrudan yükler. Yayımlanmış yayında önce geçici adla yükler, eskiyi siler, adı düzeltir: dosya
    adresi yalnız iki istek arasında boş kalır (eskiden yükleme boyunca, 12 MB'lık exe için dakikalarca)."""
    yukleme = yayin["upload_url"].split("{", 1)[0]
    varliklar = {v["name"]: v for v in yayin.get("assets", [])}
    for ad in dosyalar:
        if yeni:
            if ad in varliklar:  # yarım kalan taslaktan
                api("DELETE", varliklar[ad]["url"], jeton)
            api("POST", f"{yukleme}?name={urllib.parse.quote(ad)}", jeton, (CIKTI / ad).read_bytes(),
                "application/octet-stream")
        else:
            gecici = GECICI_ONEK + ad
            if gecici in varliklar:
                api("DELETE", varliklar[gecici]["url"], jeton)
            yuklenen = api("POST", f"{yukleme}?name={urllib.parse.quote(gecici)}", jeton, (CIKTI / ad).read_bytes(),
                           "application/octet-stream")
            if ad in varliklar:
                api("DELETE", varliklar[ad]["url"], jeton)
            api("PATCH", yuklenen["url"], jeton, {"name": ad})
        print(f"  yüklendi: {ad}")


def eklenti_denetimi() -> None:
    """Yayından önce: Claude eklentisi (ArthurLegal-plugin/) depodaki Law Firm paketinden üretilmiş mi. Paket değişip
    eklenti üretilmediyse dizindeki eklenti eski pakette kalır; sınavdan önce durur, sınav boşuna harcanmaz."""
    import eklenti_uret
    try:
        sorunlar = eklenti_uret.denetle()
    except eklenti_uret.EklentiHata as e:
        sys.exit(f"Claude eklentisi denetlenemedi: {e}")
    if sorunlar:
        sys.exit("Claude eklentisi pakete göre eski; yayın durdu:\n  " + "\n  ".join(sorunlar[:5])
                 + ("\n  ..." if len(sorunlar) > 5 else "")
                 + "\nÖnce: python yayin/eklenti_uret.py (sürümü kendisi artırır), commit ve push.")


def surum_sinavi(etiket: str, kabul: str | None, ayar_yolu: Path = SINAV_AYARI) -> str | None:
    """Yayından önce kalite sınavı (sürüm sınavı, Katman 2). Özet satırını döndürür; ayar yoksa None.

    Ayar bu bilgisayara özeldir ve depoya girmez: %USERPROFILE%/.arthurlegal/sinav.json →
    {"komut": ["python", ".../surum_sinavi.py", "--aday", "{kok}", "--etiket", "{etiket}"]}.
    {kok} bu deponun kökü, {etiket} yayın etiketidir. Komut 0 dönerse sınav geçer; 1 dönerse kalite düşmüştür ve
    yayın durur (bilerek geçmek için --sinav-kabul NEDEN); başka bir çıkış hatadır (sınavsız yayın: --sinavsiz).
    Komutun "SINAV:" ile başlayan son satırı yayın notuna eklenir. Ayar yoksa sınavsız devam edilir: kendi
    derleyenlerin akışı değişmez."""
    if not ayar_yolu.exists():
        print(f"Sürüm sınavı tanımlı değil ({ayar_yolu} yok); sınavsız devam ediliyor.")
        return None
    ayar = json.loads(ayar_yolu.read_text(encoding="utf-8"))
    komut = [str(p).replace("{kok}", str(BURASI.parent)).replace("{etiket}", etiket) for p in ayar["komut"]]
    print("Sürüm sınavı çalışıyor (gerçek Claude oturumları; birkaç dakika sürer):\n  " + " ".join(komut))
    ozet = ""
    with subprocess.Popen(komut, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                          errors="replace") as p:
        for satir in p.stdout:
            print(satir, end="")
            if satir.startswith("SINAV:"):
                ozet = satir[len("SINAV:"):].strip()
    if p.returncode == 0:
        return ozet or "geçti"
    if p.returncode == 1:
        if kabul:
            print(f"Kalite düşüşü bilerek kabul edildi: {kabul}")
            return f"{ozet} · düşüş kabul edildi: {kabul}"
        sys.exit("Sürüm sınavında kalite düştü; yayın durdu. Nedenini inceleyin ya da bilerek geçmek için: "
                 "--sinav-kabul \"<neden>\"")
    sys.exit(f"Sürüm sınavı çalışmadı (çıkış {p.returncode}); yayın durdu. Sınavsız yayın için: --sinavsiz")


# Yayın sonrası deneme (kalite süreci 4, kurulum sağlığı). Otomatik testler kodun doğru olduğunu söyler, kullanıcının
# bilgisayarında paketin yüklendiğini söylemez: 18.11.2026 olayında bir kurulumda paket hiç yüklenmemişti ve kimse fark
# etmemişti. Her yayından sonra üç ortamda gerçek kurulumla aynı üç deneme yapılır; sonuç yayın notunun tek satırıdır.
DENEME_ORTAMLARI = {"win": ("Win", "Windows · Claude Desktop"),
                    "mac": ("Mac", "macOS · Claude Desktop"),
                    "chatgpt": ("ChatGPT", "ChatGPT masaüstü")}
DENEME_ISARETI = {"gecti": "✓", "kaldi": "✗", "bekliyor": "…"}
DENEME_BASI = "Yayın sonrası deneme:"
DENEME_ICTIHAT = "Dosya alacağına konulan haciz takası engeller mi? Yargıtay kararlarıyla cevaplayın."
DENEME_ADIMLARI = (
    "Uygulamayı tamamen kapatıp açın (Windows'ta sistem tepsisi dâhil, macOS'ta Cmd+Q; güncelleme yeniden açılışta "
    "devreye girer). Yeni sohbette arthurlegal_durum'u isteyin: yerel_kurulum {surum}, paket_durumu \"tamam\", "
    "araştırma sunucusu bağlı.",
    "İçtihat sorusu: \"{ictihat}\" → tr_ictihat_ara çağrılır, künyeli Yargıtay kararları gelir; cevabın başında "
    "paket onarım cümlesi yoktur.",
    "\"ArthurLegal Masası'nı aç\" → masa açılır, kırmızı paket uyarısı yoktur, şeritteki sürüm v{surum} (AL ile aynı).",
)


def deneme_sonuclari(govde: str) -> dict:
    """Yayın notundaki deneme satırı → {ortam: "gecti" | "kaldi" | "bekliyor"}; satır yoksa hepsi bekliyor."""
    sonuc = {o: "bekliyor" for o in DENEME_ORTAMLARI}
    satir = next((s for s in (govde or "").splitlines() if s.startswith(DENEME_BASI)), "")
    durum = {v: k for k, v in DENEME_ISARETI.items()}
    for o, (kisa, _) in DENEME_ORTAMLARI.items():
        m = re.search(r"(?:^|\s)" + re.escape(kisa) + r" (\S)", satir[len(DENEME_BASI):])
        if m and m.group(1) in durum:
            sonuc[o] = durum[m.group(1)]
    return sonuc


def deneme_satiri(sonuc: dict) -> str:
    """"Yayın sonrası deneme: Win ✓ Mac ✓ ChatGPT ✓" (bekleyen …, kalan ✗)."""
    return DENEME_BASI + " " + " ".join(f"{kisa} {DENEME_ISARETI[sonuc.get(o, 'bekliyor')]}"
                                        for o, (kisa, _) in DENEME_ORTAMLARI.items())


def deneme_notu(govde: str, sonuc: dict) -> str:
    """Yayın notunda deneme satırını yazar: varsa yerinde değiştirir, yoksa sona ekler; notun geri kalanı aynen kalır."""
    govde = govde or ""
    satirlar = govde.splitlines()
    for i, s in enumerate(satirlar):
        if s.startswith(DENEME_BASI):
            satirlar[i] = deneme_satiri(sonuc)
            return "\n".join(satirlar)
    return (govde.rstrip() + "\n\n" if govde.strip() else "") + deneme_satiri(sonuc)


def deneme_listesi(etiket: str, surum: str) -> str:
    """Yayından sonra yazdırılan liste: üç ortam, her birinde aynı üç deneme ve sonucun nota nasıl yazılacağı."""
    satirlar = [f"YAYIN SONRASI DENEME · {etiket} · her ortamda gerçek kurulumla:"]
    satirlar += [f"  [ ] {ad}" for _, ad in DENEME_ORTAMLARI.values()]
    satirlar.append("  Her birinde:")
    satirlar += [f"    {i}. " + a.format(surum=surum, ictihat=DENEME_ICTIHAT) for i, a in enumerate(DENEME_ADIMLARI, 1)]
    satirlar.append(f"  Geçenleri yayın notuna yazın:  python yayin/yayinla.py {etiket} --deneme win,mac,chatgpt")
    satirlar.append(f"  Kalan ortam:                   python yayin/yayinla.py {etiket} --deneme-kaldi mac")
    satirlar.append("  Hepsi geçince notta: " + deneme_satiri({o: "gecti" for o in DENEME_ORTAMLARI}))
    return "\n".join(satirlar)


def deneme_ortamlari(metin: str | None) -> list:
    """"win,mac" → ["win", "mac"]; bilinmeyen ad hatadır."""
    ortamlar = [o.strip().lower() for o in (metin or "").split(",") if o.strip()]
    bilinmeyen = [o for o in ortamlar if o not in DENEME_ORTAMLARI]
    if bilinmeyen:
        sys.exit(f"Bilinmeyen deneme ortamı: {', '.join(bilinmeyen)} (geçerli: {', '.join(DENEME_ORTAMLARI)})")
    return ortamlar


def deneme_isle(depo: str, etiket: str, gecen: list, kalan: list) -> dict:
    """Yayın sonrası deneme sonucunu yayının notuna işler; önceki sonuçlar korunur (ortamlar ayrı günlerde
    denenebilir). Notun yalnız deneme satırı değişir."""
    if set(gecen) & set(kalan):
        sys.exit("Aynı ortam hem geçti hem kaldı olamaz.")
    jeton = github_jetonu()
    yayin = api("GET", f"https://api.github.com/repos/{depo}/releases/tags/{etiket}", jeton)
    eski = yayin.get("body") or ""
    sonuc = deneme_sonuclari(eski)
    sonuc.update({o: "gecti" for o in gecen})
    sonuc.update({o: "kaldi" for o in kalan})
    govde = deneme_notu(eski, sonuc)
    if govde != eski:
        api("PATCH", yayin["url"], jeton, {"body": govde})
    return sonuc


def yayimla(depo: str, etiket: str, d: dict, on_surum: bool, public: bool, sinav: str | None = None) -> dict:
    """Dosyaları yükler ve yayını yayımlar; yayının son hâlini döndürür."""
    # Sıra: paket ve kurulum dosyaları önce, imzalı manifest en son. Var olan bir yayında dosyalar tek tek değişirken
    # güncelleyici hiçbir an henüz yüklenmemiş bir paketi gösteren manifest görmez.
    dosyalar = [d["paket"]["dosya"]] + yuklenecek_kurulumlar(CIKTI, d, public) + \
        ["arthurlegal-manifest.sig", "arthurlegal-manifest.json"]
    jeton = github_jetonu()
    taban = f"https://api.github.com/repos/{depo}/releases"
    # Sürüm notu derlemedeki her paketi sayar (2.5.0'dan beri dördü de kurulumun modülüdür).
    adlar = {"hukuk-burosu": "Hukuk Bürosu", "kurumsal": "Kurumsal", "adliye": "Courthouse", "akademisyen": "Akademisyen"}
    paketler = " · ".join(f"{adlar.get(p, p)} {s}" for p, s in d["icerik"]["paketler"].items())
    kurulum = ("Windows ArthurLegal-Kurulum.exe · macOS ArthurLegal-Kurulum.pkg" if "ArthurLegal-Kurulum.pkg" in dosyalar
               else "ArthurLegal-Kurulum.exe")
    govde = f"Yerel kurulum {d['surum']} · {paketler}\n\nKurulum: {kurulum}"
    if sinav:
        govde += f"\n\nSürüm sınavı: {sinav}"
    govde += "\n\n" + deneme_satiri({})   # denemeler yayından sonra yapılır: --deneme işler
    yayin, yeni = yayin_ac(taban, jeton, etiket, govde, on_surum)
    dosyalari_yukle(yayin, jeton, dosyalar, yeni)
    if yeni:  # bütün dosyalar yerinde: tek adımda yayımla (ön sürüm Latest olmaz)
        yayin = api("PATCH", yayin["url"], jeton, {"draft": False, "prerelease": on_surum,
                                                   "make_latest": "false" if on_surum else "true"})
    return yayin


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal yayını")
    ap.add_argument("etiket", nargs="?")
    ap.add_argument("--anahtar-uret", action="store_true")
    ap.add_argument("--kasa-anahtari-uret", action="store_true", help="kasada duracak yedek anahtarı üret (bir kez)")
    ap.add_argument("--link", metavar="DOSYA", help="private yayındaki dosya için geçici indirme adresi üret")
    ap.add_argument("--kararli-yap", action="store_true", help="var olan ön sürümü kararlıya çevir (sessiz güncelleme açılır)")
    ap.add_argument("--kuru", action="store_true")
    ap.add_argument("--on-surum", action="store_true")
    ap.add_argument("--kasa", action="store_true", help="günlük anahtar kayıpsa kasadaki yedek anahtarla imzala")
    ap.add_argument("--sinavsiz", action="store_true", help="sürüm sınavını atla (bilinçli; yayın notunda görünmez)")
    ap.add_argument("--sinav-kabul", metavar="NEDEN", help="sınavdaki kalite düşüşünü bilerek kabul et ve yayımla")
    ap.add_argument("--deneme", metavar="ORTAMLAR", help="yayın sonrası denemede geçen ortamlar (win,mac,chatgpt): yayın notuna ✓")
    ap.add_argument("--deneme-kaldi", metavar="ORTAMLAR", help="yayın sonrası denemede kalan ortamlar: yayın notuna ✗")
    ap.add_argument("--deneme-listesi", action="store_true", help="yayın sonrası deneme listesini yazdır (yayımlamaz)")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):   # cp1254 konsolu ✓ ve ✗ basamaz: "?" olur, yayın yarıda kalmaz
        sys.stdout.reconfigure(errors="replace")
    if args.anahtar_uret or args.kasa_anahtari_uret:
        return anahtar_uret(kasa=args.kasa_anahtari_uret)
    if args.deneme or args.deneme_kaldi or args.deneme_listesi:
        if not args.etiket:
            ap.error("etiket gerekli: python yayin/yayinla.py v2.0.0 --deneme win,mac,chatgpt")
        if args.deneme_listesi:
            print(deneme_listesi(args.etiket, args.etiket.lstrip("v")))
            return 0
        k = kaynaklar()
        sonuc = deneme_isle(k.get("dagitim_deposu") or k["yayin_deposu"], args.etiket,
                            deneme_ortamlari(args.deneme), deneme_ortamlari(args.deneme_kaldi))
        print(f"{args.etiket} yayın notu: {deneme_satiri(sonuc)}")
        if "kaldi" in sonuc.values():
            print("Kalan ortam var: kullanıcılar etkileniyor olabilir. Nedeni bulun; düzeltme sürümü çıkana kadar "
                  "yayını ön sürüme çevirmeyi düşünün (kurulu bilgisayarlar Latest'e bakar).")
        return 0
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
    eklenti_denetimi()
    sinav = None if (args.kuru or args.sinavsiz) else surum_sinavi(args.etiket, args.sinav_kabul)
    manifest = {
        "urun": "arthurlegal-yerel", "surum": d["surum"], "etiket": args.etiket,
        "taban": f"https://github.com/{depo}/releases/download/{args.etiket}/",
        "tarih": time.strftime("%Y-%m-%d"), "paket": d["paket"], "mask": d["mask"], "icerik": d["icerik"],
        # Yenilikler (3.3.1): arayüzlerin "yeni sürüm var" paneli bu maddeleri gösterir (en çok beş, üç dil).
        **({"yenilikler": d["yenilikler"]} if d.get("yenilikler") else {}),
        # macOS: güncelleyici ArthurMask'i ilk kurulumda bu disk görüntüsünden kurar (guncelle.mac_mask_kur).
        **({"mask_macos": d["mask_macos"]} if d.get("mask_macos") else {}),
    }
    ham = json.dumps(manifest, ensure_ascii=False, indent=1).encode("utf-8")
    dosya, alan = (KASA, "kasa_anahtari") if args.kasa else (ANAHTAR, "yayin_anahtari")
    if not dosya.exists():
        sys.exit(f"İmza anahtarı yok: {dosya}" + ("" if args.kasa else "\n  Kayıpsa kasadaki yedekle imzalayın: --kasa"))
    gizli = bytes.fromhex(dosya.read_text(encoding="ascii").strip())
    acik = ed25519.public_key(gizli).hex()
    if acik != k.get(alan):
        sys.exit(f"Gizli anahtar kaynaklar.json'daki {alan} ile eşleşmiyor.")
    if d.get("anahtarlar") and acik not in d["anahtarlar"]:
        sys.exit("Bu derlemenin paketi imzalayan anahtarı tanımıyor (derleme eski kaynaklar.json'la yapılmış "
                 "olabilir); yeniden derleyin.")
    imza = ed25519.sign(gizli, ham)
    assert ed25519.verify(bytes.fromhex(acik), ham, imza)
    (CIKTI / "arthurlegal-manifest.json").write_bytes(ham)
    (CIKTI / "arthurlegal-manifest.sig").write_text(imza.hex(), encoding="ascii")
    print(f"İmzalı manifest: sürüm {d['surum']}, etiket {args.etiket}")
    if args.kuru:
        return 0

    yayin = yayimla(depo, args.etiket, d, args.on_surum, public=depo == k.get("yayin_deposu"), sinav=sinav)
    print(f"Yayın: {yayin['html_url']}")
    print("\n" + deneme_listesi(args.etiket, d["surum"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
