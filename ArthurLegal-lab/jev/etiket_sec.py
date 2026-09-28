#!/usr/bin/env python3
"""Etiketlenecek kümeleri seçer — hepsini değil, öğreten olanları.

Gövde 5000 başlığa çıktığında hepsini elle etiketlemek hem pahalı hem
gereksizdir: modelin zaten %99 güvenle doğru bildiği bir kalemi etiketlemek
ona hiçbir şey öğretmez. Öğreten kalemler şunlardır:

  KARARSIZ     modelin olasılığı karar sınırına yakın (0.15-0.70). Bilginin
               yoğun olduğu yer burasıdır.
  ÇELİŞKİ      kural "evet" diyor ama model "hayır" diyor (ya da tersi).
               Böyle bir kalem ya kuralın ya modelin yanlış olduğunu söyler.
  RASTGELE     yukarıdakilerden bağımsız, düz rastgele bir dilim.

Rastgele dilim isteğe bağlı bir süs DEĞİLDİR. Yalnızca sınıra yakın kalemleri
etiketlerseniz eğitim kümeniz sınırın etrafında yoğunlaşır; model iyi ayırır
ama olasılıkları artık gerçek sıklığı yansıtmaz — yani KALİBRASYON bozulur.
Bir hukuk aracında 0.70 eşiğinin bir anlamı olacaksa, dağılımı temsil eden bir
dilim şarttır. Oranı ``--rastgele`` ile ayarlanır, varsayılanı üçte birdir.

    python etiket_sec.py --ozet
    python etiket_sec.py --parti 0
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import etiket_hazirla as eh   # noqa: E402
import etiket_kumele as ek    # noqa: E402
import yerel                  # noqa: E402

DEPO = KOK / "fixtures" / "etiketler_kalem.json"
SECIM = KOK / "fixtures" / "secim.json"
MODEL = KOK / "model" / "rg_triyaj"
KONULAR = ("enerji", "rekabet", "vergi", "icra")
PARTI_BOY = 120
KARARSIZ_ALT, KARARSIZ_UST = 0.15, 0.70


def etiketli_anahtarlar() -> set:
    if not DEPO.exists():
        return set()
    return set(json.loads(DEPO.read_text(encoding="utf-8"))["etiket"])


def bilgi_degeri(motor: yerel.YerelMotor, metin: str) -> Tuple[float, str]:
    """(öncelik, sebep). Yüksek öncelik = daha çok öğretir."""
    en_iyi, sebep = 0.0, "kesin"
    for k in KONULAR:
        kural = bool(yerel.kural_eslesmeleri(metin, k))
        pm = motor._model_p(k, metin)
        if kural and pm < 0.30:
            # Kural zorla geçirecek ama model katılmıyor: ya kural geniş, ya
            # model eksik. İkisi de bilmeye değer.
            return 1.0, "çelişki:" + k
        if KARARSIZ_ALT <= pm < KARARSIZ_UST:
            # Sınıra uzaklık ne kadar azsa o kadar öğretici.
            deger = 0.9 - abs(pm - 0.42) / 2
            if deger > en_iyi:
                en_iyi, sebep = deger, "kararsız:%s(%.2f)" % (k, pm)
    return en_iyi, sebep


def secim_kur(rastgele_oran: float, tohum: int = 20260920) -> Dict:
    kalemler, kumeler = ek.hazirla()
    etiketli = etiketli_anahtarlar()
    motor = yerel.YerelMotor.yukle(MODEL)

    aday: List[Tuple[float, int, str]] = []
    zaten = 0
    for ki, uyeler in enumerate(kumeler):
        temsilci = kalemler[uyeler[0]]
        if eh.anahtar(temsilci["baslik"]) in etiketli:
            zaten += 1
            continue
        metin = temsilci["bolum"] + " " + temsilci["baslik"]
        oncelik, sebep = bilgi_degeri(motor, metin)
        # Büyük küme daha çok kalemi etkiler; eşitlikte öne alınır.
        oncelik += min(len(uyeler), 20) / 400.0
        aday.append((oncelik, ki, sebep))

    aday.sort(key=lambda t: -t[0])
    bilgili = [t for t in aday if t[0] >= 0.30]
    kalan = [t for t in aday if t[0] < 0.30]

    rng = np.random.default_rng(tohum)
    n_rast = int(len(bilgili) * rastgele_oran / (1 - rastgele_oran)) if rastgele_oran < 1 else len(kalan)
    n_rast = min(n_rast, len(kalan))
    secilen_rast = [kalan[i] for i in rng.choice(len(kalan), size=n_rast, replace=False)] if n_rast else []
    for t in secilen_rast:
        aday[aday.index(t)] = (t[0], t[1], "rastgele")

    sira = [(ki, sebep) for _, ki, sebep in bilgili] + \
           [(t[1], "rastgele") for t in secilen_rast]
    return {"zaten_etiketli_kume": zaten, "aday_kume": len(aday),
            "bilgili": len(bilgili), "rastgele": len(secilen_rast),
            "sira": sira}


def yukle_veya_kur(rastgele_oran: float) -> Dict:
    kalemler, kumeler = ek.hazirla()
    if SECIM.exists():
        s = json.loads(SECIM.read_text(encoding="utf-8"))
        if s.get("kume_sayisi") == len(kumeler):
            return s
    s = secim_kur(rastgele_oran)
    s["kume_sayisi"] = len(kumeler)
    SECIM.write_text(json.dumps(s, ensure_ascii=False), encoding="utf-8")
    return s


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ozet", action="store_true")
    ap.add_argument("--parti", type=int, default=None)
    ap.add_argument("--boy", type=int, default=PARTI_BOY)
    ap.add_argument("--rastgele", type=float, default=0.33,
                    help="seçimin kaçta kaçı düz rastgele olsun (kalibrasyon için)")
    ap.add_argument("--yenile", action="store_true", help="seçimi baştan kur")
    a = ap.parse_args(argv)

    if a.yenile and SECIM.exists():
        SECIM.unlink()
    kalemler, kumeler = ek.hazirla()
    s = yukle_veya_kur(a.rastgele)
    sira = s["sira"]

    if a.ozet or a.parti is None:
        from collections import Counter
        tur = Counter(x[1].split(":")[0] for x in sira)
        print("Toplam küme          : %d" % len(kumeler))
        print("Zaten etiketli       : %d" % s["zaten_etiketli_kume"])
        print("Etiketlenmeyi bekleyen: %d" % s["aday_kume"])
        print()
        print("SEÇİLEN              : %d  -> %d parti × %d"
              % (len(sira), (len(sira) + a.boy - 1) // a.boy, a.boy))
        for t, c in tur.most_common():
            print("  %-10s %5d" % (t, c))
        print()
        print("Seçilmeyen %d küme, modelin yüksek güvenle karar verdiği kalemler."
              % (s["aday_kume"] - len(sira)))
        print("Bunlar eğitime GİRMEZ (etiketsiz sayılır), sıfır varsayılmaz.")
        return 0

    bas = a.parti * a.boy
    dilim = sira[bas:bas + a.boy]
    if not dilim:
        print("Parti boş.")
        return 1
    print("### SECIM PARTI %d  (%d-%d / %d)"
          % (a.parti, bas, bas + len(dilim) - 1, len(sira)))
    for ki, sebep in dilim:
        uyeler = kumeler[ki]
        t = kalemler[uyeler[0]]
        cok = "%d×" % len(uyeler) if len(uyeler) > 1 else "  "
        print("%d|%s|%s|%s|%s" % (ki, cok, sebep, t["bolum"], ek.kirp(t["baslik"])))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
