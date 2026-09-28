"""Dışa aktarılan saf-Python modelin numpy modeliyle eşdeğerliği.

Bu dosyanın varlık sebebi tek bir tehlike: ``ArthurLegalTR`` sunucusu standart
kütüphaneyle çalışır, dolayısıyla oraya giden çıkarım kodu ``yerel.py``'nin
numpy sürümünden AYRI bir uygulamadır. İki uygulama sessizce ayrışırsa hiçbir
şey patlamaz — MCP sadece yanlış kalemleri eler ve kimse fark etmez.

En sinsi ayrışma biçimi katlama (``katla``) farkıdır: bir karakter eşleşmezse
n-gramlar tutmaz, model kendi sözlüğünü tanımaz ve HER ŞEYE sıfıra yakın
olasılık verir. Yani süzgeç "hiçbir şey bulamadı" der, hata vermez.

Testler ``ArthurLegalTR`` yoksa atlanır: JEV deposu tek başına da klonlanabilir.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

KOK = Path(__file__).resolve().parent.parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

MCP = KOK.parent / "ArthurLegalTR"
SAF = MCP / "model" / "rg_triyaj_saf"

import yerel                                    # noqa: E402
from jev import katla as katla_egitim           # noqa: E402

pytestmark = pytest.mark.skipif(
    not (SAF.with_suffix(".json").exists() and (MCP / "triyaj.py").exists()),
    reason="ArthurLegalTR yanında değil; dışa aktarım testi atlanıyor.")


def _saf():
    if str(MCP) not in sys.path:
        sys.path.insert(0, str(MCP))
    import triyaj
    return triyaj


def _ornekler():
    """Gövdeden değil, elle seçilmiş kalemler — test veriye bağlanmasın."""
    return [
        "YÖNETMELİKLER Elektrik Piyasası Lisans Yönetmeliğinde Değişiklik Yapılmasına Dair Yönetmelik",
        "TEBLİĞLER Vergi Usul Kanunu Genel Tebliği (Sıra No: 560)",
        "TEBLİĞLER Konkordato Gider Avansı Tarifesi",
        "YÖNETMELİKLER Türkiye Okçuluk Federasyonu Ana Statüsü",
        "KARAR İdare Mahkemelerinin Kurulmasına ve Yargı Çevresinin Belirlenmesine İlişkin Karar",
        "YÖNETMELİKLER Gelir İdaresi Başkanlığı Personeli Görevde Yükselme Yönetmeliği",
        "YÖNETMELİKLER Katı Yakıtların Kontrolü Yönetmeliği",
        "TEBLİĞLER Rüzgâr Kaynağına Dayalı Elektrik Üretimi Başvurularının Teknik Değerlendirmesi",
        "İLÂNLAR Çeşitli İlânlar",
    ]


def test_katlama_birebir_ayni():
    """Katlama ayrışırsa model sözlüğünü tanımaz ve sessizce sıfır döner."""
    triyaj = _saf()
    for s in _ornekler() + ["İSTANBUL IĞDIR", "Kürşat ŞİŞLİ", "Çağrı Öztürk â î û"]:
        assert triyaj.katla(s) == katla_egitim(s), s


def test_olasiliklar_esdeger():
    triyaj = _saf()
    nm = yerel.YerelMotor.yukle(KOK / "model" / "rg_triyaj")
    sp = triyaj.Triyaj.yukle(SAF)
    assert set(sp.konular) == set(nm._k)
    for metin in _ornekler():
        for konu in sp.konular:
            a, b = nm.p(konu, metin), sp.p(konu, metin)
            # float32'ye yuvarlama dışında fark olmamalı.
            assert abs(a - b) < 1e-5, (konu, metin, a, b)
            # Asıl önemlisi: eşik kararı hiç ayrışmamalı.
            assert (a >= sp.esik) == (b >= sp.esik), (konu, metin, a, b)


def test_kural_katmani_ve_istisna_tasindi():
    triyaj = _saf()
    sp = triyaj.Triyaj.yukle(SAF)
    assert len(sp._ust["kurallar"]) == len(yerel.KURALLAR)
    assert sp.p("vergi", "TEBLİĞLER Vergi Usul Kanunu Genel Tebliği") == 1.0
    # kurum_adi istisnası: kurumun kendi personel işi vergi düzenlemesi değil.
    ic = "YÖNETMELİKLER Gelir İdaresi Başkanlığı Personeli Görevde Yükselme Yönetmeliği"
    assert sp.kural_eslesmeleri(ic, "vergi") == []
    assert sp.p("vergi", ic) < sp.esik


def test_esik_olculen_degerle_gonderiliyor():
    """0.20 tahmin değil; esik_yerel.py'nin kat dışı ölçümünden geliyor.

    Künyedeki duyarlılık %100'ün ALTINDA olmalı — bu bir ön elemedir ve
    çıktısı 'tam liste' diye sunulursa kullanıcı yanıltılmış olur.
    """
    triyaj = _saf()
    sp = triyaj.Triyaj.yukle(SAF)
    assert sp.esik == 0.20
    duyarlilik = sp._ust["olcum"]["duyarlilik_esik_0.20"]
    assert set(duyarlilik) == set(sp.konular)
    assert min(duyarlilik.values()) < 1.0


def test_saf_surum_numpy_ithal_etmiyor():
    """MCP tarafı standart kütüphaneyle çalışmak zorunda; bu sözleşmedir."""
    kaynak = (MCP / "triyaj.py").read_text(encoding="utf-8")
    assert "import numpy" not in kaynak
    assert "import scipy" not in kaynak
