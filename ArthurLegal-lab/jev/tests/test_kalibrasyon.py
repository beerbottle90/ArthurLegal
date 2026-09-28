"""Kalibrasyon matematiğinin testleri.

Bu fonksiyonlar eşik seçimini belirleyecek; yanlışlarsa yanlış eşik seçilir ve
bunu hiçbir şey fark ettirmez. O yüzden işareti ve büyüklüğü ayrı ayrı sınanır:

  * ECE tek başına yanıltıcıdır — sapmanın YÖNÜNÜ taşımaz. Sıcaklık taşır.
  * ECE'nin kendisi sonlu örneklemde sıfır olmaz; gürültü tabanı olmadan
    "0.03 ECE" cümlesi bir şey ifade etmez.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

KOK = Path(__file__).resolve().parent.parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import kalibrasyon as kb  # noqa: E402


@pytest.fixture(scope="module")
def rng():
    return np.random.default_rng(1234)


def test_mukemmel_kalibrasyonda_ece_kucuk(rng):
    p = rng.uniform(0.02, 0.98, 4000)
    y = (rng.random(4000) < p).astype(float)
    assert kb.ece(p, y) < 0.03


def test_asiri_guvenlide_ece_buyur(rng):
    """Gerçek 0.5 iken 0.95 demek: büyük sapma."""
    p = np.full(2000, 0.95)
    y = (rng.random(2000) < 0.5).astype(float)
    assert kb.ece(p, y) > 0.30


def test_sicaklik_asiri_guveni_1in_ustunde_isaretler(rng):
    """T > 1 = aşırı güvenli. Uç olasılıkları yumuşatmak gerekiyor."""
    gercek = rng.uniform(0.1, 0.9, 3000)
    y = (rng.random(3000) < gercek).astype(float)
    z = np.log(gercek / (1 - gercek))
    keskin = 1 / (1 + np.exp(-z * 2.5))        # olduğundan emin
    assert kb.sicaklik_uydur(keskin, y) > 1.3


def test_sicaklik_guvensizligi_1in_altinda_isaretler(rng):
    """T < 1 = güvensiz. Bağımsız ölçümler noul'u burada buldu (T 0.66)."""
    gercek = rng.uniform(0.05, 0.95, 3000)
    y = (rng.random(3000) < gercek).astype(float)
    z = np.log(gercek / (1 - gercek))
    yumusak = 1 / (1 + np.exp(-z * 0.4))       # olduğundan çekingen
    assert kb.sicaklik_uydur(yumusak, y) < 0.8


def test_kalibre_veride_sicaklik_1e_yakin(rng):
    p = rng.uniform(0.05, 0.95, 5000)
    y = (rng.random(5000) < p).astype(float)
    assert 0.85 < kb.sicaklik_uydur(p, y) < 1.20


def test_tam_sifir_ve_bir_sicakligi_patlatmaz():
    """Jev sıkça tam 0/1 döndürüyor; logit sonsuza gitmemeli."""
    p = np.array([0.0, 0.0, 1.0, 1.0, 0.5, 0.5])
    y = np.array([0.0, 0.0, 1.0, 1.0, 1.0, 0.0])
    t = kb.sicaklik_uydur(p, y)
    assert np.isfinite(t) and t > 0


def test_gurultu_tabani_pozitif_ve_n_ile_kuculur(rng):
    """Küçük örneklemde mükemmel model bile sıfır ECE vermez."""
    kucuk = kb.gurultu_tabani(rng.uniform(0.1, 0.9, 80), tekrar=60)
    buyuk = kb.gurultu_tabani(rng.uniform(0.1, 0.9, 2000), tekrar=60)
    assert kucuk > buyuk > 0


def test_guvenilirlik_bos_kovalari_atlar():
    p = np.array([0.05, 0.06, 0.95, 0.96])
    y = np.array([0.0, 0.0, 1.0, 1.0])
    satir = kb.guvenilirlik(p, y, kova=10)
    assert len(satir) == 2                      # yalnız dolu iki kova
    assert all(n > 0 for _, _, n, _, _ in satir)
    assert sum(n for _, _, n, _, _ in satir) == 4


def test_guvenilirlik_gercek_orani_dogru_hesaplar():
    p = np.array([0.15, 0.16, 0.17, 0.18])
    y = np.array([1.0, 0.0, 0.0, 0.0])
    (_, _, n, ort_p, gercek), = kb.guvenilirlik(p, y, kova=10)
    assert n == 4
    assert gercek == pytest.approx(0.25)
    assert ort_p == pytest.approx(0.165)


def test_kirp_logiti_sonlu_tutar():
    p = kb._kirp(np.array([0.0, 1.0]))
    z = np.log(p / (1 - p))
    assert np.all(np.isfinite(z))


def test_adaylar_altin_kumeyi_disarida_birakir():
    """Sınav kümesi kalibrasyon koşusuna GİRMEMELİ — temiz kalmalı."""
    import json
    import etiket_hazirla as eh
    altin = {eh.anahtar(k["baslik"]) for k in json.loads(
        (KOK / "fixtures" / "fihrist_altin.json").read_text(encoding="utf-8")
    )["kalemler"]}
    for k in kb.adaylar():
        assert eh.anahtar(k["baslik"]) not in altin, \
            "altın kalem kalibrasyona sızmış: %.60s" % k["baslik"]
