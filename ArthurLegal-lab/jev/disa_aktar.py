#!/usr/bin/env python3
"""Eğitilmiş yerel motoru STANDART KÜTÜPHANEYLE okunabilir biçime aktarır.

Neden gerekli: ArthurLegalTR sunucusu bilinçli olarak yalnız standart
kütüphaneyle çalışır (tek isteğe bağlı bağımlılık pypdf). `retrieval.py`
yoğun vektörleri bile `struct` + `math` ile taşıyor. Triyaj motorunu oraya
gömmek için numpy'yi sunucuya sokmak, bir ön eleme özelliği uğruna dağıtım
sözleşmesini bozmak olurdu.

Çözüm ayrım: **eğitim numpy ile burada kalır, ÇIKARIM saf Python'a gider.**
Çıkarım yolu zaten taşınabilir — karakter n-gramı, seyrek iç çarpım, Platt
sigmoidi ve regex kural katmanı. Hiçbiri matris cebri değildir.

Üretilen iki dosya kendi kendine yeter; `yerel.py`'ye bağlanmazlar:

    rg_triyaj_saf.json   sözlük (n-gram listesi), konu skalerleri (b, platt_a,
                         platt_c), KURAL desenleri + gerekçeleri, iç idare
                         istisnası, eşik ve ölçüm künyesi
    rg_triyaj_saf.bin    struct ile paketli float32: once idf[V], sonra her
                         konu icin w[V] — JSON'daki konu sırasıyla

float32 seçimi bilinçli: ağırlıklar 1e-2 mertebesinde ayrışıyor, float32'nin
7 anlamlı basamağı fazlasıyla yetiyor ve dosya yarıya iniyor. Eşdeğerlik
`test_triyaj_esdeger` ile kilitli.

    python disa_aktar.py            # yalnız model/ altına yaz
    python disa_aktar.py --mcp      # ArthurLegalTR/model/ altına da kopyala

``--mcp`` hedefi bilinçli olarak ``ArthurLegalTR/model/``tir, ``data/`` DEĞİL:
``build_bundle.py`` ``data``yı SKIP_DIRS ile toptan atlar (orada onlarca
megabaytlık, önyüklemede taranan indeksler durur). Model oraya konsaydı
dağıtıma hiç girmez, uçtaki her ``konu`` çağrısı "model bulunamadı" derdi ve
sunucu bu arada sağlıklı görünmeye devam ederdi.
"""

from __future__ import annotations

import argparse
import json
import shutil
import struct
import sys
from pathlib import Path

import numpy as np

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import yerel                        # noqa: E402

KAYNAK = KOK / "model" / "rg_triyaj"
HEDEF = KOK / "model" / "rg_triyaj_saf"

# esik_yerel.py ile ölçüldü (kat dışı, 3581 kalem, Jev'siz). Ayrıntı README'de.
ESIK = 0.20
OLCUM = {
    "yontem": "kat disi (5 kat), egitim govdesi 3581 kalem, altin kume disarida",
    "betik": "esik_yerel.py",
    "tarih": "2026-09-20",
    "duyarlilik_esik_0.20": {"enerji": 0.97, "rekabet": 1.00,
                             "vergi": 0.93, "icra": 0.92},
    "elenen_oran_esik_0.20": 0.90,
    "not": ("Yerel motor TEK BASINA olculdu; Jev yok. Duyarlilik tavani %100 "
            "DEGILDIR — esik 0.02'ye indirilse bile icra'da %92'de kaliyor. "
            "Yani bu bir on elemedir, tam kapsam garantisi vermez."),
}


MCP_HEDEF = KOK.parent / "ArthurLegalTR" / "model"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mcp", action="store_true",
                    help="ArthurLegalTR/model/ altına da kopyala")
    a = ap.parse_args(argv)
    motor = yerel.YerelMotor.yukle(KAYNAK)
    sozluk = motor._sozluk
    konular = list(motor._k.keys())
    V = sozluk.boyut

    # Sözlüğü indeks sırasına diz — .bin'deki sıra budur.
    siralı = [None] * V
    for gram, i in sozluk.esleme.items():
        siralı[i] = gram
    if any(g is None for g in siralı):
        raise SystemExit("Sözlük indeksleri delikli; dışa aktarım güvenli değil.")

    ust = {
        "ad": motor.ad,
        "surum": 1,
        "ngram": [yerel.N_MIN, yerel.N_MAX],
        "boyut": V,
        "konular": konular,
        "skaler": {k: {"b": float(v["b"]), "platt_a": float(v["platt_a"]),
                       "platt_c": float(v["platt_c"])}
                   for k, v in motor._k.items()},
        "esik": ESIK,
        "olcum": OLCUM,
        "ic_idare": yerel.IC_IDARE.pattern,
        "kurallar": [{"konu": k.konu, "desen": k.desen, "gerekce": k.gerekce,
                      "kurum_adi": k.kurum_adi} for k in yerel.KURALLAR],
        "sozluk": siralı,
        "kaynak": ("arthurlegal-1.9.1-jev-edition/disa_aktar.py — egitim "
                   "egit_yerel.py ile, govde Resmi Gazete fihristi"),
    }
    HEDEF.with_suffix(".json").write_text(
        json.dumps(ust, ensure_ascii=False), encoding="utf-8")

    # .bin: idf[V] + her konu icin w[V], float32, little-endian.
    with HEDEF.with_suffix(".bin").open("wb") as f:
        f.write(struct.pack("<%df" % V, *sozluk.idf.astype(np.float32).tolist()))
        for k in konular:
            f.write(struct.pack("<%df" % V,
                                *motor._k[k]["w"].astype(np.float32).tolist()))

    j = HEDEF.with_suffix(".json").stat().st_size
    b = HEDEF.with_suffix(".bin").stat().st_size
    print("Yazıldı: %s.json (%.0f KB) + %s.bin (%.0f KB)"
          % (HEDEF.name, j / 1024, HEDEF.name, b / 1024))
    print("Sözlük %d n-gram · konular: %s · eşik %.2f"
          % (V, ", ".join(konular), ESIK))
    print("Kural %d · iç idare istisnası var" % len(ust["kurallar"]))

    if a.mcp:
        if not MCP_HEDEF.parent.exists():
            print("ArthurLegalTR bulunamadı: %s" % MCP_HEDEF.parent)
            return 1
        MCP_HEDEF.mkdir(parents=True, exist_ok=True)
        for uzanti in (".json", ".bin"):
            shutil.copy2(HEDEF.with_suffix(uzanti),
                         MCP_HEDEF / (HEDEF.name + uzanti))
        print("MCP'ye kopyalandı: %s" % MCP_HEDEF)
        print("Eşdeğerliği doğrulayın: python -m pytest tests/test_disa_aktar.py -q")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
