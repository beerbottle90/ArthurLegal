#!/usr/bin/env python3
"""RG triyaj modeli Bedesten MEVZUAT başlıklarına aktarılıyor mu? — ölçüm.

    python olc_mevzuat.py            # rapor
    python olc_mevzuat.py --esik 0.1

Neden ayrı bir ölçüm: model Resmî Gazete fihristinde eğitildi ("BÖLÜM başlık",
karışık harf). ``tr_mevzuat_ara`` aynı mevzuatı başka biçimde döndürür: BÜYÜK
HARF, bölüm adı yok, başlık içinde satır sonları. RG'de ölçülen duyarlılık
oraya KOPYALANAMAZ (kalıcı karar: eşik ve başarım sistemin özelliğidir).

İki dilim ayrı raporlanır, çünkü aynı şeyi ölçmezler:

* **görülmüş** (127) — başlık RG modelinin eğitim örneği. Genelleme ölçmez;
  yalnız BİÇİM aktarımını ölçer: aynı kalem Bedesten kılığında aynı kararı
  alıyor mu?
* **görülmemiş** (60) — eğitimde yok, elle etiketli (5'i RG altın kümesinden).
  Genelleme buradan okunur. Pozitif sayısı azdır; yüzde değil sayı okuyun.

Torba kanunlar: "Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanun" başlığı
hiçbir başlık tabanlı yöntemin göremeyeceği bir şeydir. Ölçüm, değiştirilen
kanun ADLARI üzerinden ikinci bir geçişi de raporlar (``--torba`` varsayılan
açık); adlar fixture'da durur, ölçüm ağa çıkmaz.

Çıkarım ``ArthurLegalTR/triyaj.py`` ile yapılır — yani ölçülen şey, uçta
koşan kodun kendisidir (numpy'lı eğitim motoru değil).
"""
from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path
from typing import Dict, List

KOK = Path(__file__).resolve().parent
ALTIN = KOK / "fixtures" / "mevzuat_altin.json"
TR = KOK.parent / "ArthurLegalTR"

# Bedesten türü -> RG fihristindeki bölüm adı. Model girdiyi "BÖLÜM başlık"
# olarak gördü; tür adını aynı sözcüklerle vermek biçim farkını küçültür.
# ArthurLegalTR/sources/bedesten_mevzuat.py aynı eşlemeyi kullanır.
TUR_BOLUM = {
    "KANUN": "KANUNLAR",
    "KHK": "KANUN HÜKMÜNDE KARARNAMELER",
    "CB_KARARNAME": "CUMHURBAŞKANLIĞI KARARNAMELERİ",
    "CB_KARAR": "CUMHURBAŞKANI KARARLARI",
    "CB_YONETMELIK": "YÖNETMELİKLER",
    "CB_GENELGE": "GENELGELER",
    "YONETMELIK": "YÖNETMELİKLER",
    "KKY": "YÖNETMELİKLER",
    "UY": "YÖNETMELİKLER",
    "TEBLIGLER": "TEBLİĞLER",
    "TUZUK": "TÜZÜKLER",
    "MULGA": "",
}


def motor():
    sys.path.insert(0, str(TR))
    import triyaj  # noqa: E402
    return triyaj.motor()


def skorla(m, kalem: Dict, konu: str, torba: bool) -> Dict:
    metin = (TUR_BOLUM.get(kalem["tur"], "") + " " + kalem["baslik"]).strip()
    p = m.p(konu, metin)
    kaynak = "baslik"
    if torba and kalem.get("torba"):
        adlar = kalem.get("degistirilen_kanunlar") or []
        if not adlar:
            return {"p": p, "kaynak": "belirsiz"}          # asla elenmez
        p2 = max(m.p(konu, "KANUNLAR " + ad) for ad in adlar)
        if p2 > p:
            p, kaynak = p2, "degistirilen_kanunlar"
    return {"p": p, "kaynak": kaynak}


def olc(esik: float, torba: bool) -> Dict:
    veri = json.load(io.open(ALTIN, encoding="utf-8"))
    m = motor()
    rapor: Dict = {"esik": esik, "torba": torba, "dilimler": {}}
    for ad, sec in (("gorulmus", True), ("gorulmemis", False)):
        kalemler = [k for k in veri["kalemler"] if bool(k["egitimde_goruldu"]) is sec]
        d: Dict = {"n": len(kalemler), "konular": {}}
        for konu in veri["konular"]:
            dp = yp = yn = belirsiz = 0
            kacan: List[str] = []
            yanlis: List[str] = []
            for k in kalemler:
                s = skorla(m, k, konu, torba)
                gecti = s["kaynak"] == "belirsiz" or s["p"] >= esik
                belirsiz += s["kaynak"] == "belirsiz"
                altin = bool(k["altin"][konu])
                if altin and gecti:
                    dp += 1
                elif altin:
                    yn += 1
                    kacan.append("#%d p=%.3f %s" % (k["id"], s["p"], k["baslik"][:80]))
                elif gecti and s["kaynak"] != "belirsiz":
                    yp += 1
                    yanlis.append("#%d p=%.3f %s" % (k["id"], s["p"], k["baslik"][:80]))
            d["konular"][konu] = {"pozitif": dp + yn, "yakalanan": dp, "kacan": kacan,
                                  "yanlis_pozitif": yanlis, "belirsiz_tutulan": belirsiz}
        rapor["dilimler"][ad] = d
    return rapor


def yaz(r: Dict) -> None:
    print("eşik %.2f · torba geçişi %s" % (r["esik"], "AÇIK" if r["torba"] else "kapalı"))
    for ad, d in r["dilimler"].items():
        print("\n== %s (%d kalem) ==" % (ad, d["n"]))
        print("%-8s %8s %9s %8s" % ("konu", "pozitif", "yakalanan", "yanlış+"))
        for konu, o in d["konular"].items():
            print("%-8s %8d %9d %8d" % (konu, o["pozitif"], o["yakalanan"], len(o["yanlis_pozitif"])))
        for konu, o in d["konular"].items():
            for s in o["kacan"]:
                print("   KAÇAN  [%s] %s" % (konu, s))
            for s in o["yanlis_pozitif"]:
                print("   YANLIŞ [%s] %s" % (konu, s))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--esik", type=float, default=0.20)
    ap.add_argument("--torbasiz", action="store_true", help="değiştirilen kanun adları geçişini kapat")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    r = olc(a.esik, not a.torbasiz)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        yaz(r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
