#!/usr/bin/env python3
"""Seçim partisindeki küme etiketlerini başlık anahtarlı depoya yazar.

Sözleşme: bir parti yazıldığında, o partideki HER küme için dört konunun da
kararı verilmiş sayılır ve kümenin bütün üyelerine yayılır. Konu listesinde
adı geçmeyen küme o konu için sıfırdır.

Depo başlık anahtarlıdır (bkz. etiket_tasima.py): gövde büyüyüp kümeler
yeniden numaralandığında eski etiketler yanlış kaleme bağlanmaz.

    python etiket_yaz_kume.py --parti 0 --enerji 12,88 --vergi 4 --rekabet "" --icra ""
    python etiket_yaz_kume.py --durum
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import etiket_hazirla as eh   # noqa: E402
import etiket_kumele as ek    # noqa: E402
import etiket_sec as es       # noqa: E402

DEPO = KOK / "fixtures" / "etiketler_kalem.json"
KONULAR = ("enerji", "rekabet", "vergi", "icra")


def coz(deger: Optional[str]) -> List[int]:
    if not deger or not deger.strip():
        return []
    return sorted({int(p) for p in deger.replace(" ", "").split(",") if p})


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parti", type=int, default=None)
    ap.add_argument("--boy", type=int, default=es.PARTI_BOY)
    ap.add_argument("--durum", action="store_true")
    for k in KONULAR:
        ap.add_argument("--" + k, type=str, default="")
    a = ap.parse_args(argv)

    depo = json.loads(DEPO.read_text(encoding="utf-8"))
    kalemler, kumeler = ek.hazirla()

    if a.durum or a.parti is None:
        etiketli = depo["etiket"]
        poz = {k: sum(v.get(k, 0) for v in etiketli.values()) for k in KONULAR}
        print("Etiketli kalem: %d / %d" % (len(etiketli), len(kalemler)))
        print("Pozitifler    : %s"
              % ", ".join("%s=%d" % (k, v) for k, v in poz.items()))
        if es.SECIM.exists():
            s = json.loads(es.SECIM.read_text(encoding="utf-8"))
            kalan = [ki for ki, _ in s["sira"]
                     if eh.anahtar(kalemler[kumeler[ki][0]]["baslik"]) not in etiketli]
            print("Seçimde kalan küme: %d (%d parti)"
                  % (len(kalan), (len(kalan) + a.boy - 1) // a.boy))
        return 0

    s = json.loads(es.SECIM.read_text(encoding="utf-8"))
    sira = s["sira"]
    bas = a.parti * a.boy
    dilim = [ki for ki, _ in sira[bas:bas + a.boy]]
    if not dilim:
        print("Parti boş.", file=sys.stderr)
        return 1
    gecerli = set(dilim)

    verilen = {}
    for k in KONULAR:
        idler = coz(getattr(a, k))
        disari = [i for i in idler if i not in gecerli]
        if disari:
            print("HATA: %s için parti dışı küme no: %s" % (k, disari), file=sys.stderr)
            return 2
        verilen[k] = set(idler)

    yeni = degisen = 0
    for ki in dilim:
        deger = {k: (1 if ki in verilen[k] else 0) for k in KONULAR}
        for i in kumeler[ki]:
            anahtar = eh.anahtar(kalemler[i]["baslik"])
            onceki = depo["etiket"].get(anahtar)
            if onceki is None:
                yeni += 1
            elif onceki != deger:
                degisen += 1
            depo["etiket"][anahtar] = deger

    DEPO.write_text(json.dumps(depo, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Parti %d: %d küme -> %d yeni kalem, %d değişen. Toplam etiketli: %d"
          % (a.parti, len(dilim), yeni, degisen, len(depo["etiket"])))
    print("  " + ", ".join("%s=%d" % (k, len(v)) for k, v in verilen.items()))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
