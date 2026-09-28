#!/usr/bin/env python3
"""Pilot C — Jev'i maskeleme katmanının bağımsız ikinci gözü olarak sınamak.

════════════════════════════════════════════════════════════════════════════
ÖNCE ŞUNU OKUYUN — bu pilotun bulduğu asıl şey bir sayı değil, bir çelişki:

  Jev CANLI bir maske guardrail'i OLAMAZ.

  Çünkü kontrol, maskeden geçmiş metni TypeSafe'e göndermeyi gerektirir.
  Maske çalıştıysa gönderilen metinde kişisel veri yoktur — kontrole gerek
  yoktur. Maske kaçırdıysa, tam da kaçırdığı veriyi dışarı göndermiş olursunuz.
  Yani kontrol, yalnızca işe yaramadığı durumda zararsızdır.

  Bu yüzden Pilot C bir üretim bileşeni değil, bir GERİLEME TESTİdir:
  uydurma veriyle, maskeleme katmanı değiştiğinde onu çapraz sınamak için
  çalıştırılır. Üretimde bunun yeri yoktur.
════════════════════════════════════════════════════════════════════════════

Veri: yalnız fixtures/maske_sentetik.json. Her kalem 'sentetik': true taşımak
zorundadır; taşımayan kalem varsa betik çalışmayı reddeder. Betik dosya yolu
argümanı almaz — başka bir veri kümesine yöneltilemez.

Kullanım:
    python pilot_c_maske.py            # ortamdaki anahtara göre
    python pilot_c_maske.py --sahte    # anahtar varsa bile çevrimdışı
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

from jev import Cevap, JevHatasi, istemci_kur, noul  # noqa: E402

FIXTURE = KOK / "fixtures" / "maske_sentetik.json"
ESIK = 0.50

# Sorular atomik: her biri tek bir veri türünü sorar. criteria eklendi çünkü
# Jev'in state dışında dünya bilgisi yoktur — "mahkeme adı kişisel veri
# değildir" gibi ayrımları yazmadan bilmesi beklenemez.
SORULAR = {
    "kisi": noul(
        "Bu metinde maskelenmemiş, açık yazılmış bir gerçek kişi adı var.",
        {"true": "Bir insanın adı veya soyadı düz metin olarak geçiyor.",
         "false": "{{KİŞİ-01}} gibi etiketler maskelenmiş sayılır. Mahkeme, "
                  "daire, kanun ve kamu kurumu adları kişi adı değildir."}),
    "unvan": noul(
        "Bu metinde maskelenmemiş bir özel şirket ticaret unvanı var.",
        {"true": "A.Ş., Ltd. Şti. gibi bir özel hukuk tüzel kişisinin unvanı "
                 "düz metin olarak geçiyor.",
         "false": "{{ŞİRKET-01}} gibi etiketler maskelenmiş sayılır. Kamu "
                  "kurumları ticaret unvanı değildir."}),
    "numara": noul(
        "Bu metinde maskelenmemiş bir kimlik veya hesap numarası var.",
        {"true": "TC kimlik numarası, vergi numarası, IBAN, banka hesap "
                 "numarası veya telefon numarası.",
         "false": "Mahkeme esas/karar numaraları (2026/1834 E.), kanun "
                  "numaraları, madde numaraları ve para tutarları."}),
    "adres": noul(
        "Bu metinde maskelenmemiş bir açık adres var.",
        {"true": "Mahalle, sokak ve kapı numarası düzeyinde, bir kişiyi "
                 "bulmaya yetecek açıklıkta adres.",
         "false": "Yalnız il veya ilçe adı geçmesi açık adres sayılmaz."}),
}

# SahteJev ipuçları — kasıtlı olarak kaba. Gerçek Jev'in yapacağı ayrımları
# (mahkeme adı vs. kişi adı) yapamaz; rapor bunu göstermelidir.
SAHTE_IPUCLARI = {
    "kisi": {"ayse yilmaz": 3.0, "zeynep arslan": 3.0, "mehmet kaya": 3.0,
             "hakan ozturk": 3.0, "arslan": 1.4, "isimli": 0.8, "tanik": 0.5},
    "unvan": {"a.s.": 2.4, "ltd. sti.": 2.4, "demir lojistik": 2.0,
              "karatas nakliyat": 2.0, "kurumu": 0.5},
    "numara": {"11111111111": 3.0, "tr00": 2.6, "0555": 2.6, "kimlik no": 2.0,
               "iban": 1.6, "telefon": 1.2, "numarali": 0.6},
    "adres": {"mahallesi": 2.2, "sokak": 2.2, "no: 14": 1.6, "adresine": 1.4,
              "besiktas": 0.8},
}


# --------------------------------------------------------------------------- #
# Güvenlik kilidi
# --------------------------------------------------------------------------- #

class SentetikOlmayanVeri(RuntimeError):
    """Uydurma olduğu işaretlenmemiş veri görüldü — çalışma reddedildi."""


# Uydurma kümede geçmesine izin verilen kimlikler. Bunların dışında bir ad
# görünürse birinin fixture'a gerçek veri eklediğinden şüphelenilir.
IZINLI_ADLAR = {
    "Ayşe Yılmaz", "Zeynep Arslan", "Mehmet Kaya", "Hakan Öztürk",
    "Demir Lojistik A.Ş.", "Karataş Nakliyat Ltd. Şti.",
}

# Gerçek veri kokusu: geçerli görünen TCKN (11 hane, hepsi aynı değil),
# sağlaması tutan IBAN uzunluğu, 0'la başlamayan gerçekçi cep numarası.
_TCKN = re.compile(r"\b[1-9]\d{10}\b")
_IBAN = re.compile(r"\bTR\d{24}\b")


def gecersiz_tckn(numara: str) -> bool:
    """Uydurma numara mı: tek rakam tekrarı veya sağlama tutmuyorsa evet."""
    if len(set(numara)) == 1:
        return True
    hane = [int(c) for c in numara]
    tek = sum(hane[0:9:2])
    cift = sum(hane[1:8:2])
    onuncu = (tek * 7 - cift) % 10
    onbirinci = sum(hane[:10]) % 10
    return not (hane[9] == onuncu and hane[10] == onbirinci)


def veriyi_dogrula(kalemler: List[Dict[str, Any]]) -> None:
    """Fixture'ın uydurma kaldığını her çalıştırmada yeniden kanıtlar.

    Bu bir süs değil: bu betik dış bir ucа metin gönderir. Tek savunma,
    gönderilen metnin gerçek olamayacağını her seferinde doğrulamaktır.
    """
    for k in kalemler:
        if k.get("sentetik") is not True:
            raise SentetikOlmayanVeri(
                "#%s 'sentetik': true taşımıyor. Bu betik yalnız uydurma veriyle "
                "çalışır." % k.get("id"))
        metin = k["metin"]
        for numara in _TCKN.findall(metin):
            if not gecersiz_tckn(numara):
                raise SentetikOlmayanVeri(
                    "#%s içinde sağlaması TUTAN bir TC kimlik numarası var (%s). "
                    "Gerçek veri şüphesi — çalışma durduruldu." % (k["id"], numara))
        if _IBAN.search(metin.replace(" ", "")):
            ham = _IBAN.search(metin.replace(" ", "")).group(0)
            if set(ham[2:]) != {"0"}:
                raise SentetikOlmayanVeri(
                    "#%s içinde sıfırlardan oluşmayan bir IBAN var. Gerçek veri "
                    "şüphesi — çalışma durduruldu." % k["id"])


# --------------------------------------------------------------------------- #
# Ölçüm
# --------------------------------------------------------------------------- #

@dataclass
class Sonuc:
    kalem: Dict[str, Any]
    cevaplar: Dict[str, Cevap]

    def p(self, alan: str) -> float:
        return float(self.cevaplar[alan].deger)

    @property
    def altin_sizinti(self) -> bool:
        return any(self.kalem["sizinti"].values())

    def tespit(self, esik: float) -> bool:
        return any(self.p(a) >= esik for a in SORULAR)


@dataclass
class Ozet:
    yakalanan: int = 0        # sızıntı vardı, yakalandı
    kacan: int = 0            # sızıntı vardı, yakalanamadı  <-- ÖLDÜREN HATA
    yanlis_alarm: int = 0     # sızıntı yoktu, alarm verdi
    temiz: int = 0            # sızıntı yoktu, sessiz kaldı
    kacanlar: List[int] = field(default_factory=list)
    alarmlar: List[int] = field(default_factory=list)

    @property
    def duyarlilik(self) -> Optional[float]:
        toplam = self.yakalanan + self.kacan
        return self.yakalanan / toplam if toplam else None

    @property
    def yanlis_alarm_orani(self) -> Optional[float]:
        toplam = self.yanlis_alarm + self.temiz
        return self.yanlis_alarm / toplam if toplam else None


def ozetle(sonuclar: List[Sonuc], esik: float) -> Ozet:
    o = Ozet()
    for s in sonuclar:
        tespit = s.tespit(esik)
        if s.altin_sizinti and tespit:
            o.yakalanan += 1
        elif s.altin_sizinti:
            o.kacan += 1
            o.kacanlar.append(s.kalem["id"])
        elif tespit:
            o.yanlis_alarm += 1
            o.alarmlar.append(s.kalem["id"])
        else:
            o.temiz += 1
    return o


# --------------------------------------------------------------------------- #

def yuzde(x: Optional[float]) -> str:
    return "ölçülemedi" if x is None else "%.1f%%" % (100 * x)


def rapor_yaz(sonuclar: List[Sonuc], istemci: Any, esik: float) -> Ozet:
    print()
    print("=" * 78)
    print("PILOT C — maskeleme denetçisi (GERİLEME TESTİ, üretim bileşeni DEĞİL)")
    print("=" * 78)
    print("İstemci : %s" % istemci.ad)
    if getattr(istemci, "sahte", False):
        print("          ⚠ SAHTE İSTEMCİ — sayılar Jev'in başarımı DEĞİLDİR.")
        print("            SahteJev'in ipuçları bu fixture'a bakılarak yazıldı;")
        print("            yüksek skor alması kaçınılmazdır ve hiçbir şey kanıtlamaz.")
        print("            (TypeSafe'in kendi benchmark'ındaki kusurun aynısı —")
        print("             testi yazan ile sınanan aynı elden çıkarsa sonuç bilgi")
        print("             taşımaz.) Gerçek sayı için anahtar gerekir.")
    print("Veri    : %d uydurma kalem (%s)" % (len(sonuclar), FIXTURE.name))
    print("Eşik    : %.2f (herhangi bir alan bu değeri aşarsa alarm)" % esik)
    print()

    print("%-4s %-22s %6s %6s %6s %6s  %s" %
          ("#", "durum", "kişi", "unvan", "numara", "adres", "sonuç"))
    print("-" * 78)
    for s in sonuclar:
        tespit = s.tespit(esik)
        if s.altin_sizinti:
            isaret = "✓ yakalandı" if tespit else "✗ KAÇTI"
        else:
            isaret = "! yanlış alarm" if tespit else "✓ temiz"
        print("%-4d %-22s %6.2f %6.2f %6.2f %6.2f  %s" %
              (s.kalem["id"], s.kalem["durum"][:22],
               s.p("kisi"), s.p("unvan"), s.p("numara"), s.p("adres"), isaret))
    print("-" * 78)

    o = ozetle(sonuclar, esik)
    print()
    print("SIZINTI YAKALAMA (asıl sayı): %s  — %d/%d"
          % (yuzde(o.duyarlilik), o.yakalanan, o.yakalanan + o.kacan))
    print("YANLIŞ ALARM ORANI          : %s  — %d/%d"
          % (yuzde(o.yanlis_alarm_orani), o.yanlis_alarm,
             o.yanlis_alarm + o.temiz))
    if o.kacanlar:
        print()
        print("KAÇANLAR — bir denetçide bu satırın boş olması gerekir:")
        idx = {s.kalem["id"]: s.kalem for s in sonuclar}
        for i in o.kacanlar:
            print("  #%d %s — %s" % (i, idx[i]["durum"], idx[i]["aciklama"]))
    if o.alarmlar:
        print()
        print("YANLIŞ ALARMLAR — her biri gereksiz bir insan incelemesi demektir:")
        idx = {s.kalem["id"]: s.kalem for s in sonuclar}
        for i in o.alarmlar:
            print("  #%d %s — %s" % (i, idx[i]["durum"], idx[i]["aciklama"]))

    print()
    print("MALİYET: %s" % istemci.olcer.ozet())
    print()
    print("─" * 78)
    print("HATIRLATMA: bu denetçi üretime konulamaz. Maskeden geçmiş metni dışarı")
    print("göndermek, maske kaçırdığında tam da kaçırdığı veriyi göndermek demektir.")
    print("Yeri: maske.py değiştiğinde çalıştırılan bir gerileme testidir.")
    print("─" * 78)
    print()
    return o


# --------------------------------------------------------------------------- #

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="Jev'i maskeleme denetçisi olarak sınayan gerileme testi")
    ap.add_argument("--sahte", action="store_true", help="anahtar olsa bile çevrimdışı")
    ap.add_argument("--esik", type=float, default=ESIK)
    a = ap.parse_args(argv)

    veri = json.loads(FIXTURE.read_text(encoding="utf-8"))
    kalemler = veri["kalemler"]
    try:
        veriyi_dogrula(kalemler)
    except SentetikOlmayanVeri as exc:
        print("GÜVENLİK KİLİDİ: %s" % exc, file=sys.stderr)
        return 3

    istemci = istemci_kur(SAHTE_IPUCLARI, zorla_sahte=a.sahte)

    sonuclar: List[Sonuc] = []
    for kalem in kalemler:
        state = {"kaynak": "maskelenmiş yanıt (uydurma test verisi)",
                 "metin": kalem["metin"]}
        try:
            sonuclar.append(Sonuc(kalem, istemci.sor(state, SORULAR)))
        except JevHatasi as exc:
            print("HATA (#%d): %s" % (kalem["id"], exc), file=sys.stderr)
            return 2

    o = rapor_yaz(sonuclar, istemci, a.esik)
    # Bir denetçi sızıntı kaçırıyorsa test başarısızdır.
    return 0 if not o.kacanlar else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
