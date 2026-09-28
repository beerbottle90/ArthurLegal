#!/usr/bin/env python3
"""Yerel motorun TEK BAŞINA doğru eşiğini ölçer — kat dışı (out-of-fold).

Neden ayrı bir betik: `kalibrasyon.py` Jev'i 938 küme temsilcisinde ölçüyor ve
oradan 0.20 eşiği çıktı. Ama o sayı BİRLEŞİK motorun (yerel + Jev) sayısıdır.
Laboratuvarın kalıcı kararlarından biri bunu açıkça söylüyor: "doğru eşik modelin değil, SİSTEMİN
özelliğidir; eşiği değiştirmeden önce hangi motorun konuştuğuna bakın."

MCP'ye gömülen motorda Jev YOK — ağ yok, anahtar yok, veri cihazdan çıkmıyor.
Yani gömülü yapılandırma üçüncü bir sistemdir ve kendi eşiğini hak eder.

ÖLÇÜMÜN DÜRÜSTLÜĞÜ. 938 küme temsilcisi yerel modelin EĞİTİM kümesindedir
(yalnız 56 kalemlik altın küme tutulmuştur). Onlarda ölçülen olasılıklar
iyimserdir. Bu yüzden burada eğitim gövdesinin KAT DIŞI tahminleri kullanılır:
her kalem, onu görmemiş bir modelle puanlanır. `yerel.egit` zaten aynı beşli
katlamayı Platt kalibrasyonu için kuruyor; burada aynı tohum ve aynı bölme
yeniden üretilir.

Altın kümeye BAKILMAZ (laboratuvarın kalıcı kuralı). Eşik burada seçilir, altın kümede
yalnız doğrulanır.

Küçük çekince: Platt (a, c) aynı kat dışı skorlara uyduruluyor; iki parametre
için bu ihmal edilebilir bir iyimserlik, ama sıfır değil.

    python esik_yerel.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

import numpy as np

KOK = Path(__file__).resolve().parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import yerel                        # noqa: E402
from egit_yerel import egitim_kumesi, KONULAR   # noqa: E402


def kat_disi(metinler: List[str], etiketler: Dict[str, np.ndarray],
             *, katlar: int = 5, l2: float = 1e-4, devir: int = 400
             ) -> Dict[str, np.ndarray]:
    """Konu -> kalem başına kat dışı OLASILIK (kural katmanı dahil edilmeden)."""
    sozluk = yerel.Sozluk.kur(metinler)
    satir, sutun, deger = sozluk.yigin(metinler)
    n = len(metinler)

    # yerel.egit ile AYNI tohum ve AYNI bölme — karşılaştırılabilir olsun.
    rng = np.random.default_rng(20260920)
    kat_no = rng.permutation(n) % katlar

    cikti: Dict[str, np.ndarray] = {}
    for konu, y in etiketler.items():
        y = y.astype(np.float64)
        oof = np.zeros(n, dtype=np.float64)
        for k in range(katlar):
            egitim = kat_no != k
            maske = egitim[satir]
            harita = -np.ones(n, dtype=np.int64)
            egitim_idx = np.flatnonzero(egitim)
            harita[egitim_idx] = np.arange(len(egitim_idx))
            w, b = yerel._egit_lojistik(harita[satir[maske]], sutun[maske],
                                        deger[maske], y[egitim_idx],
                                        sozluk.boyut, l2=l2, devir=devir)
            oof += np.where(egitim, 0.0,
                            yerel._skor(satir, sutun, deger, w, b, n))
        a, c = yerel._platt(oof, y)
        cikti[konu] = yerel._sigmoid(a * oof + c)
    return cikti


def main() -> int:
    metinler, etiketler, sayac = egitim_kumesi()
    print("=" * 78)
    print("YEREL MOTOR — TEK BAŞINA EŞİK ÖLÇÜMÜ (kat dışı)")
    print("=" * 78)
    print("Gövde: %d kalem (elle %d + yapısal sıfır %d) · altın tutulan %d"
          % (sayac["toplam"], sayac["elle_etiketli"], sayac["yapisal_sifir"],
             sayac["altin_tutulan"]))
    print("Bu koşuda Jev YOK. Ölçülen şey MCP'ye gömülecek yapılandırmadır.")
    print()

    olasilik = kat_disi(metinler, etiketler)

    # Kural katmanı dağıtımdaki gibi uygulanır: p = max(kural, model).
    kural_var = {k: np.array([bool(yerel.kural_eslesmeleri(m, k)) for m in metinler])
                 for k in KONULAR}
    p = {k: np.where(kural_var[k], 1.0, olasilik[k]) for k in KONULAR}

    for k in KONULAR:
        print("%-8s pozitif %4d/%d · kuralla yakalanan %d"
              % (k, int(etiketler[k].sum()), len(metinler), int(kural_var[k].sum())))
    print()
    print("EŞİK SÜPÜRMESİ — duyarlılık (kaçırmamak) ve elenen oranı (kazanç)")
    print("%6s %s %10s" % ("eşik", "".join("%12s" % k for k in KONULAR), "elenen"))
    for esik in (0.02, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50):
        satir = ""
        for k in KONULAR:
            y = etiketler[k]
            d = float(((p[k] >= esik) & (y > 0)).sum() / y.sum()) if y.sum() else 0.0
            satir += "%11.0f%%" % (100 * d)
        elenen = float(np.mean([all(p[k][i] < esik for k in KONULAR)
                                for i in range(len(metinler))]))
        print("%6.2f %s %9.0f%%" % (esik, satir, 100 * elenen))
    print()
    print("Okuma: ön elemede kaçırmak pahalı, fazladan okumak ucuz.")
    print("       Duyarlılığı %100'e yakın tutan EN YÜKSEK eşik seçilir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
