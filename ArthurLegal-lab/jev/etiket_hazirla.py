#!/usr/bin/env python3
"""Etiketleme hazırlığı — gövdeyi tekilleştirir, ayırır, parti parti yazdırır.

Üç grup:

  ALTIN TUTULAN  fixtures/fihrist_altin.json'daki 56 kalem. Eğitime GİRMEZ;
                 modelin daha önce elle, gerekçeli etiketlenmiş bir kümede
                 sınanması için ayrılır. Kendi sınavını kendi hazırlayan bir
                 model hiçbir şey kanıtlamaz.

  YAPISAL SIFIR  Başlığı konu taşımayan aileler (AYM karar numaraları, TCMB
                 günlük kur ilanları, atama/vekâlet kararları). Bunlar için
                 "hiçbir konuyu ilgilendirmiyor" etiketi bir yargı değil, bir
                 olgu tespitidir: başlıkta karar verilecek bilgi yoktur. Kural
                 açıkça yazılıdır, denetlenebilir.

  ETİKETLENECEK  Geri kalan. Parti parti basılır, Opus etiketler.

    python etiket_hazirla.py --ozet
    python etiket_hazirla.py --parti 3
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

KOK = Path(__file__).resolve().parent
GOVDE = KOK / "fixtures" / "rg_govde.json"
ALTIN = KOK / "fixtures" / "fihrist_altin.json"
KONULAR = ("enerji", "rekabet", "vergi", "icra")
PARTI_BOY = 160

# Başlığı konu taşımayan ya da dört konunun hiçbirine değmediği başlıktan kesin
# görülen aileler. İki ayrı gerekçe türü vardır ve karıştırılmamalıdır:
#
#   (a) "başlık konu taşımıyor"  — karar verilecek bilgi yok (AYM başvuru no)
#   (b) "konu belli, dördü de değil" — başlık konuyu söylüyor, konumuz değil
#
# İkisi de sıfır üretir ama (b) bir yargıdır, (a) bir olgu tespitidir. Gerekçe
# metinleri bu ayrımı korur ki sonradan denetlenebilsin.
YAPISAL_SIFIR: Tuple[Tuple[str, str], ...] = (
    (r"^Anayasa Mahkemesinin .*?E: ?\d+/\d+ \(Siyasi Parti Mali Denetimi\)",
     "(b) AYM siyasi parti mali denetimi — konu belli, dört konumuzun hiçbiri değil"),
    (r"^Anayasa Mahkemesinin .*?Başvuru Numaralı Karar",
     "(a) AYM bireysel başvuru — başlıkta yalnız başvuru numarası var, konu görünmez"),
    (r"^Anayasa Mahkemesinin .*?E: ?\d+/\d+, ?K: ?\d+/\d+ Sayılı Kararı",
     "(a) AYM iptal/itiraz kararı — başlıkta yalnız esas/karar numarası var"),
    (r"^T\.C\. Merkez Bankasınca Belirlenen",
     "(b) günlük kur/DİBS ilanı — her gün tekrar eden sabit kalem"),
    (r"Atamalar Hakkında Karar",
     "(b) atama kararı — kişi tayini, mevzuat değil"),
    (r"Vekâlet Etmesine Dair Karar",
     "(b) vekâlet kararı — konu taşımaz"),
    (r"Üyeliğine (Seçilme|Seçilmesine)",
     "(b) üyelik seçim kararı — kişi tayini"),
    (r"^Yargıtay \d+\. (Hukuk|Ceza) Dairesine Ait Karar",
     "(a) başlıkta yalnız daire numarası var; karar konusu görünmez"),
    # Üniversite yönetmelikleri: yalnız eğitim-öğretim/sınav/merkez kuruluş
    # kalıpları. "Döner Sermaye", "Taşınmaz" gibi başlıklar BU LİSTEYE GİRMEZ,
    # elle etiketlenir — daraltmayı bilerek dar tuttum.
    (r"Üniversitesi.*(Eğitim-Öğretim ve Sınav|Ön Lisans ve Lisans|Lisansüstü Eğitim|"
     r"Uygulama ve Araştırma Merkezi|Eğitim ve Öğretim) Yönetmeli",
     "(b) üniversite eğitim/merkez yönetmeliği — akademik düzen, dört konumuz değil"),
)


def yapisal_sifir(baslik: str) -> Optional[str]:
    for desen, gerekce in YAPISAL_SIFIR:
        if re.search(desen, baslik):
            return gerekce
    return None


# Resmî Gazete tipografik kesme/tırnak kullanır (’ “ ”), elle yazılan fixture
# düz olanları (' "). Eşleştirme bunları ayırt etmemeli, yoksa sınav kümesinin
# bir kısmı sessizce eğitime sızar — ölçümü çürüten türden bir hata.
_TIRNAK = str.maketrans({"’": "'", "‘": "'", "ʼ": "'",
                         "“": '"', "”": '"', "«": '"', "»": '"'})


def anahtar(baslik: str) -> str:
    """Başlık eşleştirme anahtarı: tırnaklar düzleştirilmiş, boşluklar tekilleşmiş."""
    return " ".join(baslik.translate(_TIRNAK).split())


def gövde_yukle() -> List[Dict[str, str]]:
    g = json.loads(GOVDE.read_text(encoding="utf-8"))["gunler"]
    gorulen: Dict[str, Dict[str, str]] = {}
    for tarih, v in sorted(g.items()):
        for k in v["kalemler"]:
            gorulen.setdefault(anahtar(k["baslik"]), {"baslik": k["baslik"],
                                                      "bolum": k["bolum"],
                                                      "ilk_tarih": tarih})
    return list(gorulen.values())


def altin_basliklar() -> set:
    veri = json.loads(ALTIN.read_text(encoding="utf-8"))
    return {anahtar(k["baslik"]) for k in veri["kalemler"]}


def ayir() -> Tuple[List[Dict[str, str]], List[Dict[str, str]], List[Dict[str, str]]]:
    tumu = gövde_yukle()
    altin = altin_basliklar()
    tutulan, sifir, etiketlenecek = [], [], []
    for k in tumu:
        if anahtar(k["baslik"]) in altin:
            tutulan.append(k)
        elif (gerekce := yapisal_sifir(k["baslik"])):
            k = dict(k, gerekce=gerekce)
            sifir.append(k)
        else:
            etiketlenecek.append(k)
    etiketlenecek.sort(key=lambda k: (k["bolum"], k["baslik"]))
    return tutulan, sifir, etiketlenecek


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ozet", action="store_true")
    ap.add_argument("--parti", type=int, default=None, help="0'dan başlayan parti no")
    ap.add_argument("--boy", type=int, default=PARTI_BOY)
    a = ap.parse_args(argv)

    tutulan, sifir, etiketlenecek = ayir()

    if a.ozet or a.parti is None:
        n_parti = (len(etiketlenecek) + a.boy - 1) // a.boy
        print("ALTIN TUTULAN : %4d  (eğitime girmez, sınav kümesi)" % len(tutulan))
        print("YAPISAL SIFIR : %4d  (başlık konu taşımıyor)" % len(sifir))
        print("ETİKETLENECEK : %4d  -> %d parti × %d" % (len(etiketlenecek), n_parti, a.boy))
        print()
        print("Yapısal sıfır dağılımı:")
        from collections import Counter
        for g, c in Counter(k["gerekce"] for k in sifir).most_common():
            print("  %4d  %s" % (c, g))
        return 0

    bas = a.parti * a.boy
    dilim = etiketlenecek[bas:bas + a.boy]
    if not dilim:
        print("Parti boş.")
        return 1
    print("### PARTI %d  (kalem %d-%d / %d)" % (a.parti, bas, bas + len(dilim) - 1,
                                                len(etiketlenecek)))
    for i, k in enumerate(dilim, start=bas):
        print("%d|%s|%s" % (i, k["bolum"], k["baslik"]))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
