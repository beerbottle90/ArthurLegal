#!/usr/bin/env python3
"""Tek atışlık duman testi — sözleşme gerçekten tutuyor mu?

56 kalemlik bir koşu başlatmadan önce BİR çağrı yapar ve ucun döndürdüğü ham
gövdeyi olduğu gibi gösterir. Amacı ölçüm değil, doğrulama: alan adları,
yanıt şekli ve `usage` sayaçları belgelerde yazdığı gibi mi.

Gönderilen veri tek bir Resmî Gazete başlığıdır — kamuya açık.
Anahtar hiçbir yere basılmaz.

    python ilk_cagri.py
"""

from __future__ import annotations

import io
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))


def env_yukle(yol: Path) -> None:
    """.env'i sürece yükler. Değer asla yazdırılmaz."""
    if not yol.exists():
        raise SystemExit(".env yok. Önce anahtarı yerleştirin.")
    for satir in io.open(yol, encoding="utf-8"):
        satir = satir.strip()
        if satir and not satir.startswith("#") and "=" in satir:
            ad, _, deger = satir.partition("=")
            os.environ.setdefault(ad.strip(), deger.strip())


def main() -> int:
    env_yukle(KOK / ".env")
    import jev
    from pilot_b_fihrist import SORULAR

    anahtar = os.environ.get("JEV_API_KEY", "")
    if not anahtar:
        raise SystemExit("JEV_API_KEY boş.")
    print("Anahtar bulundu: %s***%s (%d hane)"
          % (anahtar[:4], anahtar[-3:], len(anahtar)))

    # Altın kümeden bilinen bir pozitif: EPDK kurul kararı, enerji=1.
    kalem = next(k for k in json.loads(
        (KOK / "fixtures" / "fihrist_altin.json").read_text(encoding="utf-8")
    )["kalemler"] if k["id"] == 26)
    state = {"kaynak": "Resmî Gazete fihristi", "tarih": kalem["tarih"],
             "sayi": kalem["rg"], "bolum": kalem["bolum"],
             "baslik": kalem["baslik"]}

    govde = {"model": os.environ.get("JEV_MODEL", "jev-latest"),
             "state": state, "questions": SORULAR}
    print()
    print("GÖNDERİLEN (anahtar hariç):")
    print(json.dumps(govde, ensure_ascii=False, indent=1)[:900] + " ...")
    print()

    istek = urllib.request.Request(
        jev.TYPESAFE_UC,
        data=json.dumps(govde, ensure_ascii=False).encode("utf-8"),
        method="POST",
        headers={"Authorization": "Bearer " + anahtar,
                 "Content-Type": "application/json; charset=utf-8"})
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(istek, timeout=30) as yanit:
            kod = yanit.status
            ham = yanit.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        kod = exc.code
        ham = exc.read().decode("utf-8", "replace")
    except urllib.error.URLError as exc:
        print("BAĞLANTI HATASI: %s" % exc.reason)
        return 2
    gecen_ms = 1000 * (time.perf_counter() - t0)

    print("HTTP %s  ·  %.0f ms" % (kod, gecen_ms))
    print()
    print("HAM YANIT:")
    try:
        print(json.dumps(json.loads(ham), ensure_ascii=False, indent=1)[:2500])
    except ValueError:
        print(ham[:2000])

    if kod != 200:
        print()
        print("Sözleşme tutmadı. Yukarıdaki gövde hangi alanı reddettiğini söylüyor.")
        return 1

    # Kendi çözücümüz ham yanıtı okuyabiliyor mu?
    print()
    try:
        cevaplar = jev.GercekJev._coz(json.loads(ham), SORULAR)
        print("ÇÖZÜCÜ TAMAM. Dört konu için olasılıklar:")
        for ad, c in cevaplar.items():
            altin = kalem["altin"][ad]
            print("  %-8s p=%.2f   (altın=%d)" % (ad, float(c.deger), altin))
        print()
        print("Beklenti: enerji yüksek (altın=1), diğer üçü düşük.")
    except jev.JevHatasi as exc:
        print("ÇÖZÜCÜ HATASI: %s" % exc)
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    raise SystemExit(main())
