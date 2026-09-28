#!/usr/bin/env python3
"""Pilot B — Resmî Gazete fihristini Jev ile ön eleme.

Fikir: günlük fihrist 5-80 kalem gelir, bunların çoğu sizi ilgilendirmez.
Her kalemi Opus'a okutmak pahalı ve yavaş. Jev'e kalem başına tek çağrıda
dört evet/hayır sorusu sorulur; eleyemediklerini Opus okur.

Bu bir *ön eleme*dir, hukukî bir karar değildir. Bu yüzden ölçtüğümüz asıl
sayı isabet değil **duyarlılıktır (recall)**: ilgili bir kalemi elemek pahalı
bir hatadır, ilgisiz bir kalemi Opus'a göndermek sadece birkaç kuruştur.
Asimetri tasarımın merkezindedir — üç bantlı eşik bundandır.

Veri: yalnız fixtures/fihrist_altin.json. Tamamı kamuya açık Resmî Gazete
başlıklarıdır. Bu betik müvekkil verisine erişmez ve erişemez.

Kullanım:
    python pilot_b_fihrist.py                 # ortamdaki anahtara göre
    python pilot_b_fihrist.py --sahte         # anahtar varsa bile çevrimdışı
    python pilot_b_fihrist.py --esik 0.6
    python pilot_b_fihrist.py --tarama        # eşik süpürmesi
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

from jev import Cevap, JevHatasi, istemci_kur, noul  # noqa: E402

FIXTURE = KOK / "fixtures" / "fihrist_altin.json"

# Üç bant. Ortadaki bant "karar verme, Opus'a sor" demektir; bir ön elemede
# kararsızlık bir hata değil, doğru cevaptır.
#
# BU EŞİKLER ARTIK ÖLÇÜLMÜŞTÜR (kalibrasyon.py, 938 küme temsilcisi,
# olcum/jev_kalibrasyon_ham.jsonl). Daha önce tahmindi.
#
# Ölçülen eşik süpürmesi (duyarlılık / elenen oranı):
#
#     eşik    enerji  rekabet   vergi    icra   elenen
#     0.05      100%     100%     98%     97%     48%
#     0.10      100%     100%     95%     90%     67%
#     0.15      100%     100%     91%     87%     74%
#     0.20       99%     100%     86%     84%     77%   <- eski varsayım
#     0.50       95%      50%     67%     48%     83%
#
# JEV TEK BAŞINA kullanılacaksa alt bant 0.05 olmalı: 0.20'de vergi ve icra
# pozitiflerinin altıda biri eleniyor.
#
# AMA BİRLEŞİK MOTORDA DURUM TERSİNE DÖNÜYOR — ve bu kalibrasyonun en değerli
# bulgusu. Altın kümede birleşik motor her eşikte AYNI duyarlılığı veriyor
# (87.5 / 100 / 100 / 100, tek kaçak #51), ama triyaj çökiyor:
#
#     alt    duyarlılık          triyaj   enerji isabeti
#     0.05   aynı                  %29         %33
#     0.10   aynı                  %57         %70
#     0.15   aynı                  %61         %78
#     0.20   aynı                  %62         %88   <- seçilen
#
# Sebebi: kural katmanı gerçek pozitifleri zaten 1.0'a sabitliyor. Jev'in
# bandını düşürmek duyarlılığa hiçbir şey EKLEMİYOR, yalnız yanlış pozitif
# ekliyor. Yani doğru eşik, elinizde kural tabanı olup olmamasına göre değişir:
# tabanı olan yüksek eşik kullanabilir, olmayan düşüğe inmek zorundadır.
#
# Üst bant 0.60'ta bırakıldı: güvenilirlik tablosunda 0.6 üstü bantlarda
# gerçek pozitif oranı dört konuda da 1.000'e çok yakın.
#
# Ayrıca ölçüldü: Jev'in noul cevapları DÖRT KONUDA DA GÜVENSİZ kalibre —
# yeniden uydurulan sıcaklık T = 0.50 / 0.46 / 0.63 / 0.65, hepsi 1'in altında.
# Bu, bağımsız depoların İngilizce verilerde bulduğu yönü (boolean T≈0.66)
# Türkçe hukuk metninde bağımsız olarak doğruluyor. ECE gürültü tabanının
# 2.7-4.2 katı, yani sapma örnekleme gürültüsü değil, gerçek.
VARSAYILAN_ALT = 0.20   # ÖLÇÜLDÜ: birleşik motorda en iyi takas
#                       (Jev TEK BAŞINA kullanılacaksa: --alt 0.05)
VARSAYILAN_UST = 0.60   # ÖLÇÜLDÜ: 0.6 üstünde gerçek pozitif oranı ~1.00


# Sorular ATOMİK tutuldu: her biri tek bir hukuk alanını sorar. İlk sürümde
# tek soruda sekiz kavram sayılıyordu ("elektrik, doğal gaz, petrol, akaryakıt,
# kömür, yenilenebilir, iletim/dağıtım veya EPDK") — TypeSafe belgelerinin
# açıkça kaçınılmasını söylediği kalıp: "birden çok yargıyı tek soruya
# saklamayın", yoksa birinde yüksek diğerinde düşük olan girdi ölçeğe
# yerleştirilemez.
#
# Her soruya ``criteria`` eklendi. Jev'in state dışında dünya bilgisi yoktur;
# "enerji mevzuatı"nın Türk hukukunda neyi kapsadığını bilmesini ummak yerine
# yazmak gerekir. Belgeler instructions ile criteria'nın ÇELİŞMEMESİNİ de
# vurguluyor — ikisi de aynı yönde yazıldı, yüksek olasılık her zaman "evet".
SORULAR = {
    "enerji": noul(
        "Bu Resmî Gazete kalemi enerji piyasası hukukunu ilgilendiriyor.",
        {"true": "Elektrik, doğal gaz, petrol, akaryakıt, LPG, kömür, "
                 "yenilenebilir enerji, nükleer enerji, enerji iletim veya "
                 "dağıtım altyapısı, enerji verimliliği ya da EPDK düzenlemesi.",
         "false": "Konusu enerji olmayan her kalem. Madencilik tek başına, "
                  "su/sulama projeleri, elektronik para, demiryolu "
                  "elektrifikasyonu ve enerji kurumlarının kendi personel "
                  "işleri buraya girer."}),
    "rekabet": noul(
        "Bu Resmî Gazete kalemi rekabet hukukunu ilgilendiriyor.",
        {"true": "4054 sayılı Kanun, Rekabet Kurumu veya Kurulu, birleşme ve "
                 "devralma izni, hâkim durumun kötüye kullanılması, rekabeti "
                 "kısıtlayan anlaşmalar, özelleştirme devir izni.",
         "false": "Konusu rekabet hukuku olmayan her kalem. 'İthalatta haksız "
                  "rekabetin önlenmesi' bir ANTİDAMPİNG düzenlemesidir ve "
                  "rekabet hukuku DEĞİLDİR; 'haksız ticari uygulamalar' "
                  "tüketici hukukudur."}),
    "vergi": noul(
        "Bu Resmî Gazete kalemi vergi hukukunu ilgilendiriyor.",
        {"true": "Vergi Usul Kanunu, gelir/kurumlar/katma değer/özel tüketim/"
                 "emlak/damga vergisi, harçlar, amme alacaklarının tahsili, "
                 "vergi istisnası veya Gelir İdaresi Başkanlığı düzenlemesi.",
         "false": "Konusu iç vergi mevzuatı olmayan her kalem. Gümrük vergisi, "
                  "tarife kontenjanı ve ithalat rejimi DIŞ TİCARET aracıdır; "
                  "SGK primi vergi değildir."}),
    "icra": noul(
        "Bu Resmî Gazete kalemi icra-iflas hukukunu veya yargılama usulünü "
        "ilgilendiriyor.",
        {"true": "İcra ve İflâs Kanunu, Hukuk Muhakemeleri Kanunu, cebrî icra, "
                 "haciz, konkordato, malvarlığının dondurulması, yargı "
                 "teşkilatı ve yargı çevresi, yargılama gider tarifeleri.",
         "false": "Konusu icra-iflas veya yargılama usulü olmayan her kalem. "
                  "Adalet kurumlarının personel işlemleri buraya girer."}),
}

# SahteJev'e verilen ipuçları. Bunlar Jev'in bilgisi DEĞİL — çevrimdışı boru
# hattını çalıştırmak için kaba bir vekil. Kasıtlı olarak kusurludur: tuzak
# kalemlere ("elektronik para", "doğal afet") düşer ki rapor gerçekçi görünsün.
SAHTE_IPUCLARI = {
    "enerji": {"enerji": 2.2, "epdk": 2.5, "elektrik": 1.8, "dogal gaz": 2.0,
               "petrol": 2.0, "akaryakit": 2.0, "komur": 1.5, "yakit": 1.4,
               "teias": 1.6, "tedas": 1.6, "ges": 1.0, "kv ": 1.0,
               "aydinlatma": 1.2, "elektronik": 0.9, "dogal": 0.6},
    "rekabet": {"rekabet": 2.6, "birlesme": 1.6, "devralma": 1.6,
                "ozellestirme": 1.3, "fiyatlandirma": 0.8, "hakim durum": 2.0},
    "vergi": {"vergi": 2.6, "otv": 2.0, "kdv": 2.0, "tevkifat": 1.8,
              "harc": 1.2, "istisna": 0.9, "emlak vergisi": 2.2, "teblig": 0.45,
              "maliye": 0.8, "gelir idaresi": 2.2},
    "icra": {"icra": 2.4, "iflas": 2.2, "haciz": 2.2, "malvarlig": 1.6,
             "dondurulmasi": 1.4, "mahkemesi": 1.3, "yargi cevresi": 1.8,
             "usul": 0.7, "ilan": 0.5, "yargitay": 0.9},
}


# --------------------------------------------------------------------------- #

@dataclass
class KalemSonucu:
    kalem: Dict[str, Any]
    cevaplar: Dict[str, Cevap]

    def p(self, konu: str) -> float:
        return float(self.cevaplar[konu].deger)


@dataclass
class KonuOlcumu:
    """Tek konu için karıştırma matrisi ve türevleri."""
    konu: str
    dogru_pozitif: int = 0
    yanlis_pozitif: int = 0
    dogru_negatif: int = 0
    yanlis_negatif: int = 0
    kararsiz: int = 0
    kaciranlar: List[int] = None  # yanlış negatif kalem id'leri

    def __post_init__(self) -> None:
        if self.kaciranlar is None:
            self.kaciranlar = []

    @property
    def altin_pozitif(self) -> int:
        return self.dogru_pozitif + self.yanlis_negatif

    @property
    def duyarlilik(self) -> Optional[float]:
        """Recall — ilgili kalemlerin kaçta kaçı yakalandı. Asıl sayı budur."""
        if self.altin_pozitif == 0:
            return None
        return self.dogru_pozitif / self.altin_pozitif

    @property
    def isabet(self) -> Optional[float]:
        """Precision — geçirilenlerin kaçta kaçı gerçekten ilgiliydi."""
        gecen = self.dogru_pozitif + self.yanlis_pozitif
        return self.dogru_pozitif / gecen if gecen else None


def olc(sonuclar: List[KalemSonucu], konu: str, alt: float, ust: float) -> KonuOlcumu:
    """Üç bantlı değerlendirme.

    Orta bant (alt <= p < ust) "kararsız"dır: kalem Opus'a gider. Bu yüzden
    kararsız bir POZİTİF kaçırılmış sayılmaz — yakalanmıştır, sadece pahalıya.
    Kararsız bir NEGATİF ise boşa giden bir Opus çağrısıdır.
    """
    o = KonuOlcumu(konu)
    for s in sonuclar:
        altin = bool(s.kalem["altin"][konu])
        p = s.p(konu)
        if p >= ust:
            karar = "gecir"
        elif p < alt:
            karar = "ele"
        else:
            karar = "kararsiz"
            o.kararsiz += 1

        if karar == "ele":
            if altin:
                o.yanlis_negatif += 1
                o.kaciranlar.append(s.kalem["id"])
            else:
                o.dogru_negatif += 1
        else:  # gecir veya kararsiz -> ikisi de Opus'a gider
            if altin:
                o.dogru_pozitif += 1
            else:
                o.yanlis_pozitif += 1
    return o


def kalemi_calistir(istemci: Any, kalem: Dict[str, Any]) -> KalemSonucu:
    """Bir kalem, TEK çağrı, DÖRT soru.

    Jev'in soru haritası alması buranın can alıcı noktası: dört ayrı konu için
    dört ayrı istek atmak yerine tek istekte hepsi sorulur. Girdi tokeni bir kez
    ödenir, gecikme bir kez yaşanır.
    """
    state = {
        "kaynak": "Resmî Gazete fihristi",
        "tarih": kalem["tarih"],
        "sayi": kalem["rg"],
        "bolum": kalem["bolum"],
        "baslik": kalem["baslik"],
    }
    return KalemSonucu(kalem, istemci.sor(state, SORULAR))


# --------------------------------------------------------------------------- #
# Rapor
# --------------------------------------------------------------------------- #

def yuzde(x: Optional[float]) -> str:
    return "  ölçülemedi" if x is None else "%11.1f%%" % (100 * x)


def rapor_yaz(sonuclar: List[KalemSonucu], istemci: Any, alt: float, ust: float,
              konular: Dict[str, str]) -> Dict[str, KonuOlcumu]:
    print()
    print("=" * 78)
    print("PILOT B — Resmî Gazete ön eleme")
    print("=" * 78)
    print("İstemci  : %s" % istemci.ad)
    if getattr(istemci, "sahte", False):
        print("           ⚠ SAHTE İSTEMCİ — aşağıdaki sayılar Jev'in başarımı")
        print("             DEĞİLDİR. SahteJev'in anahtar kelimeleri bu fixture'a")
        print("             bakılarak yazıldı; iyi skor alması kaçınılmazdır ve")
        print("             hiçbir şey kanıtlamaz. Yalnız boru hattının uçtan uca")
        print("             çalıştığını gösterir. Gerçek sayı için anahtar gerekir.")
    print("Kalem    : %d (kaynak: %s)" % (len(sonuclar), FIXTURE.name))
    print("Bantlar  : ele < %.2f   ≤ kararsız <   %.2f ≤ geçir" % (alt, ust))
    print()

    olcumler: Dict[str, KonuOlcumu] = {}
    print("%-9s %5s %7s %12s %12s %9s" %
          ("KONU", "altın", "yakala", "DUYARLILIK", "isabet", "kararsız"))
    print("-" * 78)
    for konu in konular:
        o = olc(sonuclar, konu, alt, ust)
        olcumler[konu] = o
        print("%-9s %5d %7d %s %s %9d" %
              (konu, o.altin_pozitif, o.dogru_pozitif,
               yuzde(o.duyarlilik), yuzde(o.isabet), o.kararsiz))
    print("-" * 78)

    # Kaçırılanlar — bir hukuk aracında tek tek görülmesi gereken şey budur.
    kaciranlar = {k: o.kaciranlar for k, o in olcumler.items() if o.kaciranlar}
    if kaciranlar:
        print()
        print("KAÇIRILANLAR (elenmiş ama altın etiketi pozitif) — filtreyi bunlar yargılar:")
        idx = {k["id"]: k for k in (s.kalem for s in sonuclar)}
        for konu, idler in kaciranlar.items():
            for i in idler:
                k = idx[i]
                p = next(s.p(konu) for s in sonuclar if s.kalem["id"] == i)
                print("  [%s] p=%.3f  #%d %s — %.90s" % (konu, p, i, k["tarih"], k["baslik"]))
    else:
        print()
        print("KAÇIRILAN YOK — hiçbir ilgili kalem elenmedi.")

    # Triyaj kazancı: kaç kalem hiç Opus görmeden düştü.
    dusen = sum(1 for s in sonuclar
                if all(s.p(k) < alt for k in konular))
    print()
    print("TRİYAJ: %d/%d kalem (%%%.0f) hiç Opus görmeden elendi."
          % (dusen, len(sonuclar), 100 * dusen / len(sonuclar)))
    print("        Kalan %d kalem okunmak üzere Opus'a gider."
          % (len(sonuclar) - dusen))
    print()
    print("MALİYET: %s" % istemci.olcer.ozet())
    if not getattr(istemci, "sahte", False):
        gunluk = istemci.olcer.usd / len(sonuclar) * 40  # ~40 kalem/gün
        print("         Kaba yıllık: 40 kalem/gün × 250 iş günü ≈ $%.2f" % (gunluk * 250))
    print()
    return olcumler


def esik_taramasi(sonuclar: List[KalemSonucu], konular: Dict[str, str]) -> None:
    """Eşik nerede kırılıyor — duyarlılık/triyaj takasını gösterir."""
    print("=" * 78)
    print("EŞİK SÜPÜRMESİ — tek eşikli (bantsız) basit kesim")
    print("=" * 78)
    print("%6s %s %8s" % ("eşik", "".join("%12s" % k for k in konular), "elenen"))
    print("-" * 78)
    for esik in (0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90):
        satir = ""
        for konu in konular:
            o = olc(sonuclar, konu, esik, esik)
            satir += "%12s" % ("  —" if o.duyarlilik is None
                               else "%.0f%%" % (100 * o.duyarlilik))
        dusen = sum(1 for s in sonuclar if all(s.p(k) < esik for k in konular))
        print("%6.2f %s %7d%%" % (esik, satir, 100 * dusen / len(sonuclar)))
    print("-" * 78)
    print("Okuma: sol sütunlar duyarlılık (yüksek iyi), sağ sütun elenen oranı")
    print("       (yüksek ucuz). İkisi ters çalışır; iş kararı bu takastır.")
    print()


# --------------------------------------------------------------------------- #

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Jev ile Resmî Gazete ön eleme pilotu")
    ap.add_argument("--sahte", action="store_true", help="anahtar olsa bile çevrimdışı çalış")
    ap.add_argument("--yerel", action="store_true",
                    help="Jev yerine cihazdaki YerelMotor'u kullan (aynı arayüz)")
    ap.add_argument("--birlesik", action="store_true",
                    help="yerel + Jev, ikisinin azamisi (ölçülmüş en iyi duyarlılık)")
    ap.add_argument("--alt", type=float, default=VARSAYILAN_ALT)
    ap.add_argument("--ust", type=float, default=VARSAYILAN_UST)
    ap.add_argument("--esik", type=float, default=None,
                    help="tek eşik kullan (alt=üst); bantları kapatır")
    ap.add_argument("--tarama", action="store_true", help="eşik süpürmesi de yaz")
    ap.add_argument("--json", type=Path, default=None, help="ham sonuçları bu dosyaya yaz")
    a = ap.parse_args(argv)

    alt, ust = (a.esik, a.esik) if a.esik is not None else (a.alt, a.ust)
    if alt > ust:
        ap.error("--alt, --ust'ten büyük olamaz")

    veri = json.loads(FIXTURE.read_text(encoding="utf-8"))
    kalemler = veri["kalemler"]
    konular = veri["konular"]

    if a.birlesik:
        import yerel as _yerel
        from birlesik import BirlesikMotor
        model_yolu = KOK / "model" / "rg_triyaj"
        if not model_yolu.with_suffix(".json").exists():
            ap.error("Yerel model yok. Önce: python egit_yerel.py")
        jev_istemci = istemci_kur(SAHTE_IPUCLARI)
        if getattr(jev_istemci, "sahte", False):
            print("UYARI: Jev anahtarı yok, birleşik motor yalnız yerelle çalışacak.",
                  file=sys.stderr)
            jev_istemci = None
        istemci = BirlesikMotor(_yerel.YerelMotor.yukle(model_yolu), jev_istemci)
    elif a.yerel:
        # Aynı ``sor(state, sorular)`` sözleşmesi; tek fark, hiçbir şeyin
        # cihazdan çıkmaması. Raporun geri kalanı değişmeden çalışır.
        import yerel as _yerel
        model_yolu = KOK / "model" / "rg_triyaj"
        if not model_yolu.with_suffix(".json").exists():
            ap.error("Yerel model yok. Önce: python egit_yerel.py")
        istemci = _yerel.YerelMotor.yukle(model_yolu)
    else:
        istemci = istemci_kur(SAHTE_IPUCLARI, zorla_sahte=a.sahte)

    sonuclar: List[KalemSonucu] = []
    for kalem in kalemler:
        try:
            sonuclar.append(kalemi_calistir(istemci, kalem))
        except JevHatasi as exc:
            print("HATA (#%d): %s" % (kalem["id"], exc), file=sys.stderr)
            return 2

    olcumler = rapor_yaz(sonuclar, istemci, alt, ust, konular)
    if a.tarama:
        esik_taramasi(sonuclar, konular)

    if a.json:
        a.json.write_text(json.dumps({
            "istemci": istemci.ad,
            "sahte": bool(getattr(istemci, "sahte", False)),
            "alt": alt, "ust": ust,
            "olcum": {k: {"duyarlilik": o.duyarlilik, "isabet": o.isabet,
                          "altin_pozitif": o.altin_pozitif,
                          "kaciranlar": o.kaciranlar}
                      for k, o in olcumler.items()},
            "kalemler": [{"id": s.kalem["id"],
                          "baslik": s.kalem["baslik"][:80],
                          "altin": s.kalem["altin"],
                          "p": {k: s.p(k) for k in konular}}
                         for s in sonuclar],
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Ham sonuç yazıldı: %s" % a.json)

    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Windows konsolu cp1254'e düşmesin
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
