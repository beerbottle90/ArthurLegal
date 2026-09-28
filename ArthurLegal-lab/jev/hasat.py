#!/usr/bin/env python3
"""Resmî Gazete fihrist hasadı — yerel modelin eğitim gövdesi.

ArthurLegalTR'nin kendi ``sources/resmi_gazete.py`` modülünü içeriden çağırır:
MCP turu yok, token maliyeti yok, aynı ayrıştırıcı. Kaynak tek ve resmîdir —
üç ayağınızın birincisi budur.

Günde bir istek atar, aralarında bekler ve her günü diske yazar; yeniden
çalıştırıldığında yalnız eksik günleri çeker. Site nazikçe taranır.

    python hasat.py --gun 180              # bugünden geriye 180 takvim günü
    python hasat.py --gun 400 --devam      # gövdeyi büyüt (5000 hedefi)

Çıktı: fixtures/rg_govde.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

KOK = Path(__file__).resolve().parent
TR = KOK.parent / "ArthurLegalTR"
if not TR.is_dir():
    raise SystemExit("ArthurLegalTR bulunamadı: %s" % TR)
for yol in (str(TR), str(KOK)):
    if yol not in sys.path:
        sys.path.insert(0, yol)

from sources import resmi_gazete  # noqa: E402

GOVDE = KOK / "fixtures" / "rg_govde.json"
BEKLEME_SN = 0.35   # siteye nezaket


def gun_cek(d: date) -> Optional[Dict[str, Any]]:
    """Bir günün fihristi. Yayım yoksa (tatil) None."""
    sonuc = resmi_gazete.fihrist({"date": d.isoformat()})
    if sonuc.get("error") or not sonuc.get("items"):
        return None
    return sonuc


def normalize(baslik: str) -> str:
    """Fihrist başlıkları HTML'den satır sonlarıyla gelir; tek satıra indir."""
    return " ".join(baslik.split())


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Resmî Gazete fihrist hasadı")
    ap.add_argument("--gun", type=int, default=180, help="geriye kaç takvim günü")
    ap.add_argument("--bitis", type=str, default=None, help="YYYY-MM-DD (varsayılan dün)")
    ap.add_argument("--devam", action="store_true",
                    help="mevcut gövdeye ekle (varsayılan: zaten ekler, bu bayrak açıklayıcıdır)")
    a = ap.parse_args(argv)

    bitis = (datetime.strptime(a.bitis, "%Y-%m-%d").date() if a.bitis
             else date.today() - timedelta(days=1))

    govde: Dict[str, Any] = {"gunler": {}, "guncelleme": ""}
    if GOVDE.exists():
        govde = json.loads(GOVDE.read_text(encoding="utf-8"))
    gunler: Dict[str, Any] = govde["gunler"]

    istenen = [(bitis - timedelta(days=i)).isoformat() for i in range(a.gun)]
    eksik = [g for g in istenen if g not in gunler]
    print("Gövdede %d gün var. İstenen %d günün %d tanesi eksik."
          % (len(gunler), len(istenen), len(eksik)))
    if not eksik:
        print("Çekilecek yeni gün yok.")
    hata = 0
    for i, gs in enumerate(eksik, 1):
        d = datetime.strptime(gs, "%Y-%m-%d").date()
        try:
            sonuc = gun_cek(d)
        except Exception as exc:                      # ağ hatası bir günü atlatır
            hata += 1
            print("  %s HATA: %s" % (gs, str(exc)[:70]))
            if hata > 25:
                print("Çok fazla hata — durduruldu. Gövde korundu.")
                break
            time.sleep(1.5)
            continue
        if sonuc is None:
            gunler[gs] = {"yayim": False, "kalemler": []}
        else:
            gunler[gs] = {
                "yayim": True,
                "rg": sonuc.get("number", ""),
                "kalemler": [{"bolum": normalize(k["section"]),
                              "baslik": normalize(k["title"])}
                             for k in sonuc["items"]],
            }
        if i % 20 == 0 or i == len(eksik):
            print("  %d/%d  (%s)" % (i, len(eksik), gs))
            govde["guncelleme"] = datetime.now().isoformat(timespec="seconds")
            GOVDE.write_text(json.dumps(govde, ensure_ascii=False), encoding="utf-8")
        time.sleep(BEKLEME_SN)

    govde["guncelleme"] = datetime.now().isoformat(timespec="seconds")
    GOVDE.write_text(json.dumps(govde, ensure_ascii=False), encoding="utf-8")

    yayimli = [g for g, v in gunler.items() if v["yayim"]]
    toplam = sum(len(v["kalemler"]) for v in gunler.values())
    tekil = len({k["baslik"] for v in gunler.values() for k in v["kalemler"]})
    print()
    print("GÖVDE: %d gün (%d yayımlı) · %d kalem · %d tekil başlık"
          % (len(gunler), len(yayimli), toplam, tekil))
    if yayimli:
        print("Aralık: %s .. %s" % (min(yayimli), max(yayimli)))
    print("Yazıldı: %s" % GOVDE)
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
