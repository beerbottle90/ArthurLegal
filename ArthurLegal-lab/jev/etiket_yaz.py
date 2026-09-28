#!/usr/bin/env python3
"""Etiket deposu — parti parti gelen Opus etiketlerini birleştirir.

Sözleşme: bir parti "tamamlandı" işaretlendiğinde, o partideki her kalem için
dört konunun da kararı verilmiş sayılır. Konu listesinde adı geçmeyen kalem
o konu için SIFIRDIR. Bu yüzden eksik bir parti hiç yoktur — ya tamamı vardır
ya hiçbiri. Yarım etiketlenmiş parti sessizce sıfır üretip modeli zehirler.

    python etiket_yaz.py --parti 0 --enerji 4,17 --vergi 9 --icra "" --rekabet ""
    python etiket_yaz.py --durum
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set

KOK = Path(__file__).resolve().parent
DEPO = KOK / "fixtures" / "etiketler.json"
KONULAR = ("enerji", "rekabet", "vergi", "icra")


def yukle() -> Dict:
    if DEPO.exists():
        return json.loads(DEPO.read_text(encoding="utf-8"))
    return {"aciklama": "Opus damıtma etiketleri. Parti tamamlandıysa listede "
                        "olmayan kalem o konu için 0'dır.",
            "partiler": {}, "boy": 160}


def kaydet(d: Dict) -> None:
    DEPO.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def coz(deger: Optional[str]) -> List[int]:
    if not deger or not deger.strip():
        return []
    return sorted({int(p) for p in deger.replace(" ", "").split(",") if p})


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parti", type=int, default=None)
    ap.add_argument("--boy", type=int, default=160)
    ap.add_argument("--durum", action="store_true")
    for k in KONULAR:
        ap.add_argument("--" + k, type=str, default="")
    a = ap.parse_args(argv)

    depo = yukle()

    if a.durum or a.parti is None:
        import etiket_hazirla as eh
        _, _, etiketlenecek = eh.ayir()
        n_parti = (len(etiketlenecek) + depo["boy"] - 1) // depo["boy"]
        bitmis = sorted(int(p) for p in depo["partiler"])
        print("Parti: %d/%d tamam" % (len(bitmis), n_parti))
        eksik = [i for i in range(n_parti) if i not in bitmis]
        if eksik:
            print("Eksik: %s" % ", ".join(str(i) for i in eksik))
        toplam = {k: 0 for k in KONULAR}
        for p in depo["partiler"].values():
            for k in KONULAR:
                toplam[k] += len(p.get(k, []))
        print("Pozitif sayıları: %s" % ", ".join("%s=%d" % (k, v) for k, v in toplam.items()))
        return 0

    bas = a.parti * a.boy
    son = bas + a.boy - 1
    parti = {}
    for k in KONULAR:
        idler = coz(getattr(a, k))
        disari = [i for i in idler if not bas <= i <= son]
        if disari:
            print("HATA: %s için parti dışı id: %s (aralık %d-%d)"
                  % (k, disari, bas, son), file=sys.stderr)
            return 2
        parti[k] = idler
    depo["partiler"][str(a.parti)] = parti
    depo["boy"] = a.boy
    kaydet(depo)
    print("Parti %d yazıldı: %s" % (a.parti,
          ", ".join("%s=%d" % (k, len(v)) for k, v in parti.items())))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
