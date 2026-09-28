#!/usr/bin/env python3
"""Yerel motoru eğitir ve TUTULAN altın kümede sınar.

Eğitim gövdesi üç kaynaktan birleşir:

  1. Küme etiketleri  — Opus'un küme temsilcisine verdiği etiket, kümenin tüm
                        üyelerine yayılır.
  2. Yapısal sıfırlar — başlığı konu taşımayan aileler (gerekçeleri
                        etiket_hazirla.YAPISAL_SIFIR'da satır satır yazılı).
  3. (hiçbiri)        — altın küme eğitime ASLA girmez.

Sınav, fixtures/fihrist_altin.json'daki elle ve gerekçeli etiketlenmiş 56
kalemdir. Bu kalemler gövdede vardır ama eğitimden çıkarılmıştır; model onları
ilk kez sınavda görür.

    python egit_yerel.py                 # eğit, sına, kaydet
    python egit_yerel.py --neden 17      # tek bir altın kalemin gerekçesi
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import etiket_hazirla as eh          # noqa: E402
import etiket_kumele as ek           # noqa: E402
import yerel                          # noqa: E402
from jev import noul                  # noqa: E402

DEPO = KOK / "fixtures" / "etiketler_kalem.json"
ALTIN = KOK / "fixtures" / "fihrist_altin.json"
MODEL = KOK / "model" / "rg_triyaj"
KONULAR = ("enerji", "rekabet", "vergi", "icra")


# --------------------------------------------------------------------------- #

def egitim_kumesi() -> Tuple[List[str], Dict[str, np.ndarray], Dict[str, int]]:
    """(metinler, konu -> etiket dizisi, sayaçlar).

    Etiket kaynağı başlık anahtarlıdır; gövde büyüdüğünde kayma olmaz.
    **Etiketlenmemiş kalem eğitime GİRMEZ** — sıfır sayılmaz. Bu ayrım kritik:
    "bu kaleme henüz bakmadım" ile "bu kalem konuyla ilgisiz" aynı şey değildir
    ve ikincisi gibi davranmak modele sistematik yalan söylemektir.
    """
    depo = json.loads(DEPO.read_text(encoding="utf-8"))
    etiketli = depo["etiket"]
    tutulan, sifirlar, etiketlenecek = eh.ayir()

    metinler: List[str] = []
    etiket: Dict[str, List[int]] = {k: [] for k in KONULAR}
    etiketsiz: List[str] = []

    for kal in etiketlenecek:
        deger = etiketli.get(eh.anahtar(kal["baslik"]))
        if deger is None:
            etiketsiz.append(kal["baslik"])
            continue
        metinler.append(kal["bolum"] + " " + kal["baslik"])
        for k in KONULAR:
            etiket[k].append(int(deger.get(k, 0)))
    elle = len(metinler)

    # Yapısal sıfırlar: gerekçesi etiket_hazirla.YAPISAL_SIFIR'da yazılı.
    for kal in sifirlar:
        metinler.append(kal["bolum"] + " " + kal["baslik"])
        for k in KONULAR:
            etiket[k].append(0)

    sayac = {"elle_etiketli": elle, "yapisal_sifir": len(sifirlar),
             "etiketsiz": len(etiketsiz), "toplam": len(metinler),
             "altin_tutulan": len(tutulan)}
    return metinler, {k: np.array(v, dtype=np.float64) for k, v in etiket.items()}, sayac


def altin_kume() -> List[Dict]:
    return json.loads(ALTIN.read_text(encoding="utf-8"))["kalemler"]


# --------------------------------------------------------------------------- #
# Sınav
# --------------------------------------------------------------------------- #

def sina(motor: yerel.YerelMotor, alt: float, ust: float) -> Dict[str, Dict]:
    """Pilot B'nin üç bantlı mantığıyla aynı ölçüm — karşılaştırılabilir olsun."""
    kalemler = altin_kume()
    sorular = {k: noul("") for k in KONULAR}   # yerel motorda soru metni kullanılmaz
    olcum = {k: {"dp": 0, "yp": 0, "dn": 0, "yn": 0, "kararsiz": 0, "kacan": []}
             for k in KONULAR}
    gecen_sn = 0.0
    for kal in kalemler:
        state = {"bolum": kal["bolum"], "baslik": kal["baslik"]}
        t0 = time.perf_counter()
        cevaplar = motor.sor(state, sorular)
        gecen_sn += time.perf_counter() - t0
        for k in KONULAR:
            p = float(cevaplar[k].deger)
            altin = bool(kal["altin"][k])
            if p < alt:
                if altin:
                    olcum[k]["yn"] += 1
                    olcum[k]["kacan"].append((kal["id"], round(p, 3), kal["baslik"][:70]))
                else:
                    olcum[k]["dn"] += 1
            else:
                if alt <= p < ust:
                    olcum[k]["kararsiz"] += 1
                if altin:
                    olcum[k]["dp"] += 1
                else:
                    olcum[k]["yp"] += 1
    for k in KONULAR:
        o = olcum[k]
        poz = o["dp"] + o["yn"]
        o["duyarlilik"] = (o["dp"] / poz) if poz else None
        gec = o["dp"] + o["yp"]
        o["isabet"] = (o["dp"] / gec) if gec else None
        o["altin_poz"] = poz
    olcum["_sure"] = {"kalem": len(kalemler), "toplam_sn": gecen_sn,
                      "kalem_basina_ms": 1000 * gecen_sn / len(kalemler)}
    return olcum


def yuzde(x) -> str:
    return "  ölçülemedi" if x is None else "%11.1f%%" % (100 * x)


# --------------------------------------------------------------------------- #

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--alt", type=float, default=0.30)
    ap.add_argument("--ust", type=float, default=0.70)
    ap.add_argument("--devir", type=int, default=400)
    ap.add_argument("--l2", type=float, default=1e-4)
    ap.add_argument("--neden", type=int, default=None, help="altın kalem id'si")
    a = ap.parse_args(argv)

    if a.neden is not None:
        motor = yerel.YerelMotor.yukle(MODEL)
        kal = next(k for k in altin_kume() if k["id"] == a.neden)
        print(kal["baslik"])
        print()
        for k in KONULAR:
            g = motor.neden({"bolum": kal["bolum"], "baslik": kal["baslik"]}, k)
            print("%-8s p=%.3f  (%s)  altın=%d"
                  % (k, g["karar"], g["dayanak"], kal["altin"][k]))
            for n in g.get("ngramlar", [])[:5]:
                print("           %-10r %+.4f" % (n["ngram"], n["katki"]))
            for r in g.get("kurallar", []):
                print("           KURAL: %s" % r["gerekce"])
        return 0

    print("=" * 78)
    print("YEREL MOTOR — eğitim")
    print("=" * 78)
    metinler, etiketler, sayac = egitim_kumesi()
    print("Elle etiketli: %d  +  yapısal sıfır: %d  =  eğitim gövdesi: %d"
          % (sayac["elle_etiketli"], sayac["yapisal_sifir"], sayac["toplam"]))
    print("Etiketsiz (eğitim DIŞI): %d" % sayac["etiketsiz"])
    print("Altın tutulan (sınav): %d kalem, eğitime girmedi." % sayac["altin_tutulan"])
    print()

    t0 = time.perf_counter()
    motor = yerel.egit(metinler, etiketler, l2=a.l2, devir=a.devir,
                       ad="YerelMotor (RG triyaj)")
    print("Eğitim süresi: %.1f sn" % (time.perf_counter() - t0))
    MODEL.parent.mkdir(exist_ok=True)
    motor.kaydet(MODEL)
    boyut = sum(f.stat().st_size for f in MODEL.parent.glob(MODEL.name + ".*"))
    print("Model: %s.{json,npz}  (%.1f MB)" % (MODEL, boyut / 1e6))
    print()

    print("=" * 78)
    print("SINAV — tutulan altın küme (56 kalem, eğitimde görülmedi)")
    print("=" * 78)
    print("Bantlar: ele < %.2f  ≤ kararsız <  %.2f ≤ geçir" % (a.alt, a.ust))
    print()
    olcum = sina(motor, a.alt, a.ust)
    print("%-9s %5s %7s %12s %12s %9s"
          % ("KONU", "altın", "yakala", "DUYARLILIK", "isabet", "kararsız"))
    print("-" * 78)
    for k in KONULAR:
        o = olcum[k]
        print("%-9s %5d %7d %s %s %9d"
              % (k, o["altin_poz"], o["dp"], yuzde(o["duyarlilik"]),
                 yuzde(o["isabet"]), o["kararsiz"]))
    print("-" * 78)

    kacanlar = [(k, o["kacan"]) for k, o in olcum.items()
                if isinstance(o, dict) and o.get("kacan")]
    if kacanlar:
        print()
        print("KAÇIRILANLAR:")
        for k, liste in kacanlar:
            for i, p, b in liste:
                print("  [%s] p=%.3f  #%d %s" % (k, p, i, b))
    else:
        print()
        print("KAÇIRILAN YOK.")

    s = olcum["_sure"]
    print()
    print("HIZ: %d kalem, toplam %.3f sn  ->  kalem başına %.2f ms"
          % (s["kalem"], s["toplam_sn"], s["kalem_basina_ms"]))
    print("     (dört soru tek geçişte; ağ turu yok, token yok, maliyet sıfır)")
    print()
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
