#!/usr/bin/env python3
"""Etiketleri küme indeksinden BAŞLIK anahtarına taşır — tek seferlik göç.

Sorun: ``etiketler.json`` etiketleri küme numarasına göre tutuyordu. Gövdeye
yeni gün eklendiğinde kümeleme baştan yapılır, numaralar kayar ve elle verilmiş
bütün etiketler sessizce yanlış kalemlere bağlanır. Sessiz olması en kötü yanı:
hiçbir şey hata vermez, sadece model çöp öğrenir.

Çözüm: etiketi kalemin KENDİ başlığına bağlamak. Başlık, Resmî Gazete'nin
verdiği kimliktir; gövde büyüdükçe değişmez.

    python etiket_tasima.py --uygula
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

ESKI = KOK / "fixtures" / "etiketler.json"
YENI = KOK / "fixtures" / "etiketler_kalem.json"
KONULAR = ("enerji", "rekabet", "vergi", "icra")


def tasi() -> Dict[str, Dict]:
    kalemler, kumeler = ek.hazirla()
    depo = json.loads(ESKI.read_text(encoding="utf-8"))
    boy = depo["boy"]
    kayit: Dict[str, Dict[str, int]] = {}
    for ki, uyeler in enumerate(kumeler):
        parti = depo["partiler"].get(str(ki // boy))
        if parti is None:
            continue
        deger = {k: (1 if ki in parti.get(k, []) else 0) for k in KONULAR}
        for i in uyeler:
            kayit[eh.anahtar(kalemler[i]["baslik"])] = dict(deger)
    return {
        "aciklama": "Opus damıtma etiketleri, kalem başlığına bağlı. Küme "
                    "numarasına bağlı DEĞİL: gövde büyüdükçe kayma olmaz.",
        "konular": list(KONULAR),
        "kaynak": "etiketler.json (küme tabanlı) -> göç, 2026-09-20",
        "etiket": kayit,
    }


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--uygula", action="store_true")
    a = ap.parse_args(argv)

    yeni = tasi()
    n = len(yeni["etiket"])
    poz = {k: sum(v[k] for v in yeni["etiket"].values()) for k in KONULAR}
    print("Taşınan kalem: %d" % n)
    print("Pozitifler   : %s" % ", ".join("%s=%d" % (k, v) for k, v in poz.items()))
    if not a.uygula:
        print("(--uygula verilmedi, yazılmadı)")
        return 0
    YENI.write_text(json.dumps(yeni, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Yazıldı: %s" % YENI)
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
