"""ArthurLegal Masası ve sohbet içi kartların (MCP Apps ön yüzü) durağan denetimi. Ağ istemez, yalnız standart
kütüphane kullanır; haftalık denetim rutini her hafta koşturur, elle de çalıştırılabilir:

    python3 tests/on_yuz_denetimi.py                                  depodaki kopyayı denetler
    python3 tests/on_yuz_denetimi.py --esle ../arthurlegal-mcp/arayuz  öbür kopyayla bayt bayt karşılaştırır
    python3 tests/on_yuz_denetimi.py --json sonuc.json                 sonucu JSON olarak da yazar

Denetlenenler: kopyaların eşitliği, görünümlerin birleşmesi (yer tutucu kalmaması), dışarıdan yüklenen her adresin
CSP izninde olması, araç verisini HTML olarak yazan kod, sürüm eşitliği, ekran listesi, masanın çağırdığı araçlar
(canlı araç listesiyle karşılaştırmak için dökülür), açık ve koyu temada yazı/zemin karşıtlığı (WCAG AA 4,5:1),
dar ekran, hareket azaltma, odak halkası, en küçük yazı ve dokunma hedefi, etiketsiz alanlar, temaya bağlı olmayan
sabit renkler.

Sonuç: her denetim "geçti", "uyarı" ya da "kaldı". En az bir "kaldı" varsa çıkış kodu 1'dir.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
VARSAYILAN_KOK = BURASI / "istemci" / "arayuz"
KAYNAKLAR_JSON = BURASI / "kaynaklar.json"
SUNUCU = BURASI / "istemci" / "arthurlegal_sunucu.py"

sonuclar: list = []


def kaydet(kimlik: str, ad: str, durum: str, ayrinti: str = "", **ek) -> None:
    sonuclar.append({"kimlik": kimlik, "ad": ad, "durum": durum, "ayrinti": ayrinti, **ek})
    print(f"  {durum:<6} {ad}" + (f": {ayrinti}" if ayrinti else ""), flush=True)


def al_arayuz_yukle(kok: Path):
    os.environ["AL_ARAYUZ_ORTAK"] = str(kok / "ortak")
    spec = importlib.util.spec_from_file_location("al_arayuz_denetim", kok / "al_arayuz.py")
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def dosyalar(kok: Path) -> dict:
    """Karşılaştırılan dosyalar: al_arayuz.py ve ortak/ altındaki her şey (KAYNAK.txt satır sonu yüzünden hariç)."""
    out = {"al_arayuz.py": kok / "al_arayuz.py"}
    for p in sorted((kok / "ortak").rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
            out[p.relative_to(kok).as_posix()] = p
    return out


# ---------------------------------------------------------------- renk ve karşıtlık
def renk(deger: str):
    """#rgb, #rrggbb ya da rgb(r g b / a) -> (r, g, b, a). Çözülemezse None."""
    d = deger.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", d)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 1.0)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+)\s*(?:[/,]\s*([\d.]+%?))?\s*\)", d)
    if m:
        a = m.group(4)
        alfa = 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)), alfa)
    return None


def ustune(on, arka):
    a = on[3]
    return tuple(round(on[i] * a + arka[i] * (1 - a)) for i in range(3)) + (1.0,)


def parlaklik(c) -> float:
    def kanal(v):
        v = v / 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * kanal(c[0]) + 0.7152 * kanal(c[1]) + 0.0722 * kanal(c[2])


def karsitlik(a, b) -> float:
    la, lb = sorted((parlaklik(a), parlaklik(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def tema_degiskenleri(css: str) -> dict:
    """{"acik": {...}, "koyu": {...}}: :root ve :root[data-tema="koyu"] bloklarındaki --değişkenler."""
    def blok(secici):
        m = re.search(re.escape(secici) + r"\s*\{(.*?)\n\}", css, re.S)
        return dict(re.findall(r"--([\w-]+)\s*:\s*([^;]+);", m.group(1))) if m else {}
    acik = blok(":root")
    koyu = {**acik, **blok(':root[data-tema="koyu"]')}
    return {"acik": acik, "koyu": koyu}


# Yazı rengi -> üstünde durduğu zeminler. Alfa'lı zemin önce --yuzey'in üstüne konur.
KARSITLIK_CIFTLERI = [
    ("metin", ["zemin", "yuzey", "grup"]),
    ("ikincil", ["zemin", "yuzey", "grup"]),
    ("soluk", ["zemin", "yuzey", "grup"]),          # 11-12 px yazılar: bölüm adı, sürüm, saat, yer tutucu
    ("altin-metin", ["zemin", "yuzey", "secili"]),
    ("nane-metin", ["nane-zemin"]),
    ("amber-metin", ["amber-zemin"]),
    ("kirmizi-metin", ["kirmizi-zemin"]),
    ("mavi-metin", ["mavi-zemin"]),
    ("birincil-yazi", ["birincil"]),
]


def karsitlik_denetimi(css: str) -> None:
    temalar = tema_degiskenleri(css)
    for tema, d in temalar.items():
        dusuk = []
        olculen = 0
        for yazi, zeminler in KARSITLIK_CIFTLERI:
            ya = renk(d.get(yazi, ""))
            for z in zeminler:
                za = renk(d.get(z, ""))
                taban = renk(d.get("yuzey", "#ffffff"))
                if not ya or not za or not taban:
                    continue
                if za[3] < 1:
                    za = ustune(za, taban)
                oran = karsitlik(ya, za)
                olculen += 1
                if oran < 4.5:
                    dusuk.append(f"--{yazi} / --{z} {oran:.2f}:1")
        durum = "geçti" if not dusuk else ("kaldı" if any(float(x.split()[-1][:-2]) < 3 for x in dusuk) else "uyarı")
        kaydet(f"karsitlik-{tema}", f"Karşıtlık ({'açık' if tema == 'acik' else 'koyu'} tema)", durum,
               f"{olculen} çift ölçüldü" + (f"; 4,5:1 altı: {', '.join(dusuk)}" if dusuk else ""), dusuk=dusuk)


# ---------------------------------------------------------------- ana denetim
def denetle(kok: Path, esler: list, depo_kontrolu: bool) -> None:
    print(f"Ön yüz denetimi: {kok}", flush=True)
    mod = al_arayuz_yukle(kok)
    kaynaklar = mod.kaynaklar()
    css = (kok / "ortak" / "tasarim" / "al.css").read_text(encoding="utf-8")
    js = (kok / "ortak" / "tasarim" / "al.js").read_text(encoding="utf-8")
    masa_sablon = (kok / "ortak" / "gorunumler" / "masa.html").read_text(encoding="utf-8")
    sablonlar = {p.name: p.read_text(encoding="utf-8") for p in (kok / "ortak" / "gorunumler").glob("*.html")}

    # 1. Kopyalar
    asil = dosyalar(kok)
    for es in esler:
        es = Path(es)
        if not (es / "al_arayuz.py").is_file():
            kaydet("kopya", f"Kopya eşitliği ({es})", "kaldı", "klasörde al_arayuz.py yok")
            continue
        obur = dosyalar(es)
        farkli = [ad for ad in asil if ad in obur and asil[ad].read_bytes() != obur[ad].read_bytes()]
        eksik = sorted(set(asil) ^ set(obur))
        kaynak = ""
        k = es / "KAYNAK.txt"
        if k.is_file():
            m = re.search(r"kaynak commit:\s*([0-9a-f]{7,40})", k.read_text(encoding="utf-8"))
            kaynak = m.group(1) if m else ""
        kaydet("kopya", f"Kopya eşitliği ({es.as_posix()})", "geçti" if not farkli and not eksik else "kaldı",
               f"{len(asil)} dosya" + (f"; farklı: {', '.join(farkli)}" if farkli else "")
               + (f"; yalnız birinde: {', '.join(eksik)}" if eksik else "") + (f"; KAYNAK {kaynak}" if kaynak else ""),
               farkli=farkli, eksik=eksik, kaynak_commit=kaynak)
    k = kok / "KAYNAK.txt"
    if k.is_file():
        m = re.search(r"kaynak commit:\s*([0-9a-f]{7,40})", k.read_text(encoding="utf-8"))
        kaydet("kaynak-commit", "Kopyanın kaynak commit'i", "geçti", m.group(1) if m else "okunamadı",
               kaynak_commit=m.group(1) if m else "")

    # 2. Birleşme
    kalan = [r["uri"] for r in kaynaklar if re.search(r"/\*AL:[A-Z]+\*/|<!--AL:[A-Z]+-->", r["text"])]
    boyut = {r["uri"].rsplit("/", 1)[-1]: round(len(r["text"].encode("utf-8")) / 1024, 1) for r in kaynaklar}
    kaydet("birlesme", "Görünümlerin birleşmesi", "kaldı" if kalan else "geçti",
           ("yer tutucu kaldı: " + ", ".join(kalan)) if kalan else
           ", ".join(f"{ad} {kb} KB" for ad, kb in boyut.items()), boyut_kb=boyut)
    eksik_bas = []
    for r in kaynaklar:
        t = r["text"]
        for ad, desen in (("lang", r'<html lang="tr"'), ("viewport", r'name="viewport"'),
                          ("color-scheme", r'name="color-scheme"'), ("title", r"<title>[^<]+</title>")):
            if not re.search(desen, t):
                eksik_bas.append(f"{r['uri'].rsplit('/', 1)[-1]}: {ad}")
    kaydet("bas", "Belge başı (dil, viewport, renk düzeni, başlık)", "uyarı" if eksik_bas else "geçti",
           ", ".join(eksik_bas))

    # 3. Dışarıdan yüklenenler ve CSP
    izin = set(mod.META.get("ui", {}).get("csp", {}).get("resourceDomains", []))
    baglanti = set(mod.META.get("ui", {}).get("csp", {}).get("connectDomains", []))
    yuklenen, izinsiz, surumsuz = set(), [], []
    for r in kaynaklar:
        t = r["text"]
        for adres in re.findall(r"""(?:import\s[^;]*?from\s*|import\(\s*|src\s*=\s*|<link[^>]+href\s*=\s*|url\(\s*|@import\s+)["']?(https?://[^"')\s]+)""", t):
            koken = re.match(r"https?://[^/]+", adres).group(0)
            yuklenen.add(adres)
            if koken not in izin:
                izinsiz.append(f"{r['uri'].rsplit('/', 1)[-1]}: {adres}")
            if "unpkg.com" in adres or "cdn.jsdelivr.net" in adres:
                if not re.search(r"@\d+\.\d+\.\d+/", adres):
                    surumsuz.append(adres)
        if re.search(r"\bfetch\(|XMLHttpRequest|new WebSocket\(", t) and not baglanti:
            izinsiz.append(f"{r['uri'].rsplit('/', 1)[-1]}: ağ çağrısı var, connectDomains boş")
    kaydet("csp", "Dış yüklemeler CSP izninde", "kaldı" if izinsiz else "geçti",
           "; ".join(izinsiz) if izinsiz else f"izin: {', '.join(sorted(izin)) or 'yok'}; yüklenen: {', '.join(sorted(yuklenen)) or 'yok'}",
           yuklenen=sorted(yuklenen))
    ext = sorted({m for r in kaynaklar for m in re.findall(r"@modelcontextprotocol/ext-apps@([\w.\-]+)/", r["text"])})
    kaydet("ext-apps", "MCP Apps istemcisinin sabit sürümü", "kaldı" if surumsuz or len(ext) > 1 else "geçti",
           (f"sürümsüz adres: {', '.join(surumsuz)}" if surumsuz else "") + (f"sürüm: {', '.join(ext)}" if ext else "yok"),
           ext_apps=ext)

    # 4. Araç verisini HTML olarak yazan kod
    tehlike = []
    for ad, t in [("al.js", js), *sablonlar.items(),
                  ("kartlar.js", (kok / "ortak" / "tasarim" / "kartlar.js").read_text(encoding="utf-8")),
                  ("atif.js", (kok / "ortak" / "tasarim" / "atif.js").read_text(encoding="utf-8"))]:
        for n, satir in enumerate(t.splitlines(), 1):
            kod = re.sub(r"//.*$", "", satir)
            if re.search(r"\.innerHTML\s*[+]?=|\.outerHTML\s*=|insertAdjacentHTML|document\.write|\beval\(|new Function\(|setAttribute\(\s*[\"']on", kod):
                tehlike.append(f"{ad}:{n}")
    kaydet("html-yazimi", "Araç verisi HTML olarak yazılmıyor", "kaldı" if tehlike else "geçti", ", ".join(tehlike))

    # 5. Sürüm
    js_surum = (re.search(r'const SURUM = "([\d.]+)"', js) or [None, "?"])[1]
    surumler = {"al_arayuz.SURUM": mod.SURUM, "al.js SURUM": js_surum}
    if depo_kontrolu and KAYNAKLAR_JSON.is_file():
        surumler["kaynaklar.json"] = json.loads(KAYNAKLAR_JSON.read_text(encoding="utf-8")).get("surum", "?")
    kaydet("surum", "Sürüm eşitliği", "geçti" if len(set(surumler.values())) == 1 else "kaldı",
           ", ".join(f"{k} {v}" for k, v in surumler.items()), surumler=surumler)

    # 6. Ekranlar
    masa_ekran = re.findall(r'\{\s*id:\s*"(\w+)",\s*ad:', masa_sablon)
    kaydet("ekranlar", "Ekran listesi (al_arayuz ↔ masa.html)",
           "geçti" if tuple(masa_ekran) == tuple(mod.EKRANLAR) else "kaldı",
           f"{len(masa_ekran)} ekran: {', '.join(masa_ekran)}"
           + ("" if tuple(masa_ekran) == tuple(mod.EKRANLAR) else f"; al_arayuz: {', '.join(mod.EKRANLAR)}"))

    # 7. Masanın çağırdığı araçlar (canlı tools/list ile karşılaştırılmak üzere dökülür)
    kodlar = [*sablonlar.values(), *((kok / "ortak" / "tasarim" / ad).read_text(encoding="utf-8")
                                     for ad in ("kartlar.js", "atif.js"))]
    cagrilan = sorted({a for t in kodlar for a in re.findall(r'cagir\(\s*[\w.]+,\s*"(\w+)"', t)}
                      | {a for t in kodlar for a in re.findall(r'callServerTool\(\{\s*name:\s*"(\w+)"', t)})
    yerel = [a for a in cagrilan if a.startswith("al_")]
    ayrinti = f"{', '.join(cagrilan)}"
    durum = "geçti"
    if depo_kontrolu and SUNUCU.is_file():
        sunucu = SUNUCU.read_text(encoding="utf-8")
        m = re.search(r"MASA_UZAK\s*=\s*\(([^)]*)\)", sunucu)
        masa_uzak = re.findall(r'"(\w+)"', m.group(1)) if m else []
        eksik = [a for a in cagrilan if a not in masa_uzak and a not in yerel]
        tanimsiz = [a for a in yerel if f'"{a}"' not in sunucu]
        if eksik or tanimsiz:
            durum = "kaldı"
            ayrinti += (f"; yerel sunucunun MASA_UZAK listesinde yok: {', '.join(eksik)}" if eksik else "") + \
                       (f"; yerel sunucuda tanımsız: {', '.join(tanimsiz)}" if tanimsiz else "")
    kaydet("araclar", "Masanın çağırdığı araçlar", durum, ayrinti, araclar=cagrilan)

    # 8. Karşıtlık
    karsitlik_denetimi(css)

    # 9. Erişilebilirlik ve dar ekran (durağan)
    hepsi = css + "\n" + "\n".join(sablonlar.values())
    eksikler = []
    if "@keyframes" in hepsi and "prefers-reduced-motion" not in hepsi:
        eksikler.append("hareket azaltma (prefers-reduced-motion) yok")
    if ":focus-visible" not in hepsi:
        eksikler.append("odak halkası (:focus-visible) yok")
    if 'aria-live' not in masa_sablon:
        eksikler.append("masada aria-live duyuru alanı yok")
    if not re.search(r"@media\s*\(max-width:\s*\d+px\)", masa_sablon):
        eksikler.append("masada dar ekran kuralı yok")
    kaydet("erisilebilirlik", "Hareket azaltma, odak, duyuru, dar ekran", "uyarı" if eksikler else "geçti", "; ".join(eksikler))

    yazilar = sorted({float(x) for x in re.findall(r"font-size:\s*([\d.]+)px", hepsi)})
    hedefler = sorted({float(x) for x in re.findall(r"min-height:\s*([\d.]+)px", hepsi)})
    kucuk_yazi = [x for x in yazilar if x < 11]
    kucuk_hedef = [x for x in hedefler if x < 24]
    kaydet("olcu", "En küçük yazı ve dokunma hedefi", "uyarı" if kucuk_yazi or kucuk_hedef else "geçti",
           f"en küçük yazı {yazilar[0] if yazilar else '?'} px, en küçük düğme yüksekliği {hedefler[0] if hedefler else '?'} px"
           + (f"; 11 px altı: {kucuk_yazi}" if kucuk_yazi else "") + (f"; 24 px altı hedef: {kucuk_hedef}" if kucuk_hedef else ""),
           yazi_px=yazilar[:3], hedef_px=hedefler[:3])

    etiketsiz = []
    for ad, t in sablonlar.items():
        satirlar = t.splitlines()
        for n, satir in enumerate(satirlar, 1):
            if re.search(r'ogesi\("label"', satir) and not any("htmlFor" in s for s in satirlar[n - 1:n + 2]):
                etiketsiz.append(f"{ad}:{n}")
    kaydet("etiket", "Etiketler bir alana bağlı", "uyarı" if etiketsiz else "geçti",
           ("bağlanmamış <label>: " + ", ".join(etiketsiz)) if etiketsiz else "")

    sabit = []
    for ad, t in sablonlar.items():
        stil = "\n".join(re.findall(r"<style>(.*?)</style>", t, re.S))
        for n, satir in enumerate(stil.splitlines(), 1):
            if "var(--" not in satir:
                sabit += [f"{ad}: {c}" for c in re.findall(r"#[0-9a-fA-F]{3,6}\b", satir)]
    kaydet("sabit-renk", "Temaya bağlı olmayan sabit renk", "uyarı" if sabit else "geçti", ", ".join(sabit))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--kok", default=str(VARSAYILAN_KOK), help="al_arayuz.py ve ortak/ klasörünü içeren yer")
    ap.add_argument("--esle", action="append", default=[], help="bayt bayt karşılaştırılacak öbür kopya (yinelenebilir)")
    ap.add_argument("--json", help="sonucu bu dosyaya da yaz")
    a = ap.parse_args()
    kok = Path(a.kok).resolve()
    denetle(kok, a.esle, depo_kontrolu=kok == VARSAYILAN_KOK.resolve())
    kalan = sum(1 for s in sonuclar if s["durum"] == "kaldı")
    uyari = sum(1 for s in sonuclar if s["durum"] == "uyarı")
    print(f"\n{len(sonuclar)} denetim: {len(sonuclar) - kalan - uyari} geçti, {uyari} uyarı, {kalan} kaldı")
    if a.json:
        Path(a.json).write_text(json.dumps({"kok": str(kok), "sonuclar": sonuclar}, ensure_ascii=False, indent=2),
                                encoding="utf-8")
    return 1 if kalan else 0


if __name__ == "__main__":
    sys.exit(main())
