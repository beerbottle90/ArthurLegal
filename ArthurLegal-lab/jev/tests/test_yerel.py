"""Yerel motor testleri — sözleşme, kural üstünlüğü ve ağ sessizliği.

En önemli iki test burada:

  * ``test_kural_modeli_ezer`` — tasarımın omurgası. Kural eşleşince model ne
    derse desin sonuç 1.0'dır. Bu, sistemin duyarlılığına kanıtlanabilir bir
    taban koyar; bozulursa "kural katmanı garanti verir" cümlesi yalan olur.

  * ``test_yerel_ag_kullanmaz`` — bu modülün varlık sebebi verinin cihazdan
    çıkmaması. Birinin ileride "küçük bir telemetri" eklemesini kod düzeyinde
    engeller.
"""

from __future__ import annotations

import ast
import json
import sys
import unicodedata
from pathlib import Path

import numpy as np
import pytest

KOK = Path(__file__).resolve().parent.parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import jev  # noqa: E402
import yerel  # noqa: E402


# --------------------------------------------------------------------------- #
# Kural katmanı
# --------------------------------------------------------------------------- #

def test_kurallar_derlenir_ve_temiz():
    """Desenler geçerli regex olmalı ve kontrol karakteri taşımamalı.

    Kontrol karakteri sınaması boşuna değil: kural listesi betikle düzenlendiğinde
    ``\\b`` kaçışı sessizce backspace karakterine dönüşebiliyor ve desen hiçbir
    şeyle eşleşmiyor — hata vermeden.
    """
    import re
    for k in yerel.KURALLAR:
        re.compile(k.desen)
        assert not any(unicodedata.category(c) == "Cc" for c in k.desen), \
            "kontrol karakteri: %r" % k.desen
        assert k.gerekce.strip(), "gerekçesiz kural: %r" % k.desen
        assert k.konu in ("enerji", "rekabet", "vergi", "icra")


def test_kurallar_katlanmis_metne_gore_yazilmis():
    """Desenlerde büyük harf veya Türkçe aksan olmamalı — katla() sonrası eşleşirler."""
    for k in yerel.KURALLAR:
        govde = "".join(c for c in k.desen if c.isalpha())
        assert govde == govde.lower(), "büyük harf içeren desen: %r" % k.desen
        assert not (set("çğıöşüâîû") & set(k.desen)), "aksanlı desen: %r" % k.desen


@pytest.mark.parametrize("metin,konu", [
    ("Enerji Piyasası Düzenleme Kurulunun 14864 Sayılı Kararı", "enerji"),
    ("Şarj Hizmeti Yönetmeliğinde Değişiklik", "enerji"),
    ("Rekabet Kurumu Teşkilat Yönetmeliği", "rekabet"),
    ("Vergi Usul Kanunu Genel Tebliği", "vergi"),
    ("Konkordato Gider Avansı Tarifesi", "icra"),
])
def test_kural_eslesmeleri_pozitif(metin, konu):
    assert yerel.kural_eslesmeleri(metin, konu)


@pytest.mark.parametrize("metin,konu", [
    # Antidamping rekabet hukuku DEĞİLDİR. Gövdede 25 kez geçer; kural buna
    # düşerse rekabet filtresi kullanılamaz hâle gelir.
    ("İthalatta Haksız Rekabetin Önlenmesine İlişkin Tebliğ", "rekabet"),
    # Maden mevzuatı her madeni kapsar; enerji kuralı olmamalı.
    ("Maden Sahaları İhale Yönetmeliği", "enerji"),
    # "Elektronik Para" içinde 'elektr' geçer ama enerji değildir.
    ("Ödeme ve Elektronik Para Kuruluşlarının Bilgi Sistemleri Tebliği", "enerji"),
    # Ticari reklam/haksız ticari uygulama tüketici hukukudur.
    ("Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği", "rekabet"),
])
def test_kural_eslesmeleri_negatif(metin, konu):
    assert not yerel.kural_eslesmeleri(metin, konu), \
        "yanlış pozitif kural: %r / %s" % (metin, konu)


# --------------------------------------------------------------------------- #
# Omurga: kural yalnız ekler
# --------------------------------------------------------------------------- #

def _bos_motor() -> yerel.YerelMotor:
    """Ağırlıkları sıfır, dolayısıyla her zaman 'hayır' diyen bir model."""
    sozluk = yerel.Sozluk({"aaa": 0}, np.array([1.0]))
    kat = {k: {"w": np.zeros(1), "b": -8.0, "platt_a": 1.0, "platt_c": 0.0}
           for k in ("enerji", "rekabet", "vergi", "icra")}
    return yerel.YerelMotor(sozluk, kat, ad="test")


def test_kural_modeli_ezer():
    """Model 'hayır' dese bile kural eşleşirse sonuç 1.0."""
    motor = _bos_motor()
    metin = "Enerji Piyasası Düzenleme Kurulunun Kararı"
    assert motor._model_p("enerji", metin) < 0.01      # model gerçekten hayır diyor
    assert motor.p("enerji", metin) == 1.0             # ama kural ezer


def test_kural_yoksa_model_konusur():
    motor = _bos_motor()
    metin = "Sığır Tüberkülozu ile Mücadele Yönetmeliği"
    assert not yerel.kural_eslesmeleri(metin, "enerji")
    assert motor.p("enerji", metin) == pytest.approx(motor._model_p("enerji", metin))


def test_kural_hicbir_zaman_elemez():
    """Kural katmanının max() dışında bir etkisi olmamalı.

    Model yüksek olasılık verdiğinde kural sessizse sonuç düşmemeli.
    """
    sozluk = yerel.Sozluk({"aaa": 0}, np.array([1.0]))
    kat = {"enerji": {"w": np.zeros(1), "b": 8.0, "platt_a": 1.0, "platt_c": 0.0}}
    motor = yerel.YerelMotor(sozluk, kat, ad="test")
    metin = "Sığır Tüberkülozu ile Mücadele Yönetmeliği"
    assert motor.p("enerji", metin) > 0.99


# --------------------------------------------------------------------------- #
# Özellik çıkarımı
# --------------------------------------------------------------------------- #

def test_ngram_kelime_sinirini_yakalar():
    """Metin boşlukla sarılır; kelime başı bir sinyaldir."""
    g = yerel.ngramlar("vergi", 3, 3)
    assert " ve" in g and "gi " in g


def test_ngram_turkce_katlar():
    assert yerel.ngramlar("ŞARJ") == yerel.ngramlar("şarj")


def test_vektor_l2_normlu():
    sozluk = yerel.Sozluk.kur(["vergi usul kanunu", "elektrik piyasası kanunu",
                               "vergi usul tebliği"], asgari_df=1)
    _, v = sozluk.vektor("vergi usul kanunu")
    assert np.linalg.norm(v) == pytest.approx(1.0)


def test_sozlukte_olmayan_metin_cokmez():
    sozluk = yerel.Sozluk.kur(["vergi usul kanunu"], asgari_df=1)
    idx, val = sozluk.vektor("zzzzzz qqqqqq")
    assert len(idx) == len(val)


def test_sigmoid_tasmaz():
    z = np.array([-1e6, -50.0, 0.0, 50.0, 1e6])
    p = yerel._sigmoid(z)
    assert np.all(np.isfinite(p)) and np.all((p >= 0) & (p <= 1))
    assert p[2] == pytest.approx(0.5)


# --------------------------------------------------------------------------- #
# Eğitim ve kalıcılık
# --------------------------------------------------------------------------- #

@pytest.fixture(scope="module")
def kucuk_motor():
    poz = ["elektrik piyasası lisans yönetmeliği",
           "doğal gaz dağıtım tesisi kurulması",
           "elektrik üretim tesisi kamulaştırma",
           "enerji iletim hattı projesi"]
    neg = ["gıda kodeksi içme sütleri tebliği",
           "üniversite lisansüstü eğitim yönetmeliği",
           "sığır tanımlama ve tescil yönetmeliği",
           "avcılık düzenlenmesi hakkında tebliğ"]
    metinler = poz + neg
    y = {"enerji": np.array([1, 1, 1, 1, 0, 0, 0, 0], dtype=float)}
    return yerel.egit(metinler, y, katlar=2, devir=200, sessiz=True)


def test_egitim_ogrenir(kucuk_motor):
    """Model doğru tarafa eğilmeli — ve kalibrasyon sıralamayı ters çevirmemeli."""
    p_poz = kucuk_motor._model_p("enerji", "elektrik dağıtım lisansı")
    p_neg = kucuk_motor._model_p("enerji", "gıda kodeksi peynir tebliği")
    assert p_poz > p_neg


def test_platt_negatif_egimi_reddeder():
    """Ters korelasyonlu skorlarda kalibrasyon kimliğe düşmeli, ters çevirmemeli.

    Az veride Platt uydurması negatif eğim öğrenebiliyor; bu, modelin bütün
    cevaplarını sessizce tersine çevirir. Koruma olmazsa hata vermeden yanlış
    çalışan bir sınıflandırıcı elde edilir.
    """
    skor = np.array([3.0, 2.0, 1.0, -1.0, -2.0, -3.0])
    y = np.array([0.0, 0.0, 0.0, 1.0, 1.0, 1.0])     # kasıtlı ters ilişki
    a, c = yerel._platt(skor, y)
    assert a > 0.0, "negatif Platt eğimi geçti: a=%r" % a
    assert (a, c) == (1.0, 0.0)


def test_kaydet_yukle_ayni_sonucu_verir(kucuk_motor, tmp_path):
    yol = tmp_path / "m"
    kucuk_motor.kaydet(yol)
    geri = yerel.YerelMotor.yukle(yol)
    for metin in ["elektrik dağıtım lisansı", "gıda kodeksi tebliği", "zzz"]:
        assert geri.p("enerji", metin) == pytest.approx(
            kucuk_motor.p("enerji", metin), abs=1e-9)


def test_tek_sinifli_etiket_cokmez():
    """Bir konuda hiç pozitif yoksa eğitim patlamamalı, sadece hep hayır demeli."""
    m = yerel.egit(["aaa bbb", "ccc ddd"],
                   {"rekabet": np.array([0.0, 0.0])}, katlar=2, devir=50, sessiz=True)
    assert m._model_p("rekabet", "aaa bbb") < 0.5


# --------------------------------------------------------------------------- #
# Sözleşme: jev.py ile yer değiştirebilirlik
# --------------------------------------------------------------------------- #

def test_sor_jev_ile_ayni_sozlesme(kucuk_motor):
    sorular = {"enerji": jev.noul("enerji mi")}
    cevaplar = kucuk_motor.sor({"baslik": "elektrik dağıtım lisansı"}, sorular)
    c = cevaplar["enerji"]
    assert isinstance(c, jev.Cevap)
    assert c.tip == "noul" and 0.0 <= c.deger <= 1.0
    assert c.sahte is False          # yerel motor sahte değildir


def test_desteklenmeyen_soru_tipi_reddedilir(kucuk_motor):
    with pytest.raises(NotImplementedError):
        kucuk_motor.sor({"baslik": "x"}, {"a": jev.choice("hangi", {"a": "A", "b": "B"})})


def test_maliyet_sifir(kucuk_motor):
    kucuk_motor.olcer.girdi_token = 0
    kucuk_motor.sor({"baslik": "elektrik"}, {"enerji": jev.noul("")})
    assert kucuk_motor.olcer.usd == 0.0


def test_neden_kural_dayanagini_soyler(kucuk_motor):
    g = kucuk_motor.neden({"baslik": "Enerji Piyasası Düzenleme Kurulu Kararı"}, "enerji")
    assert g["dayanak"] == "kural" and g["karar"] == 1.0
    assert g["kurallar"]


def test_neden_model_dayanaginda_ngram_verir(kucuk_motor):
    # Kural eşleşmeyen bir metin seçilmeli, yoksa dayanak "kural" döner.
    g = kucuk_motor.neden({"baslik": "gaz tesisi kurulması hakkında"}, "enerji")
    assert g["dayanak"] == "model"
    assert g["ngramlar"] and "ngram" in g["ngramlar"][0]


# --------------------------------------------------------------------------- #
# Ağ sessizliği
# --------------------------------------------------------------------------- #

AG_MODULLERI = {"urllib", "urllib3", "requests", "http", "socket", "httpx",
                "ftplib", "smtplib", "telnetlib", "asyncio"}


def test_yerel_ag_kullanmaz():
    """yerel.py hiçbir ağ modülünü içe aktarmamalı.

    Bu modülün tek gerekçesi verinin cihazdan çıkmaması. İleride biri
    'küçük bir telemetri' eklemek isterse bu test düşer.
    """
    agac = ast.parse((KOK / "yerel.py").read_text(encoding="utf-8"))
    icerik = set()
    for dugum in ast.walk(agac):
        if isinstance(dugum, ast.Import):
            icerik.update(a.name.split(".")[0] for a in dugum.names)
        elif isinstance(dugum, ast.ImportFrom) and dugum.module:
            icerik.add(dugum.module.split(".")[0])
    sizinti = icerik & AG_MODULLERI
    assert not sizinti, "yerel.py ağ modülü içe aktarıyor: %s" % sorted(sizinti)


def test_yerel_jevden_yalniz_veri_tipi_alir():
    """jev.py'den ağ istemcisi değil, yalnız Cevap/Olcer/katla alınmalı."""
    agac = ast.parse((KOK / "yerel.py").read_text(encoding="utf-8"))
    for dugum in ast.walk(agac):
        if isinstance(dugum, ast.ImportFrom) and dugum.module == "jev":
            adlar = {a.name for a in dugum.names}
            assert adlar <= {"Cevap", "Olcer", "katla"}, \
                "yerel.py jev'den fazlasını alıyor: %s" % sorted(adlar)


# --------------------------------------------------------------------------- #
# Kurum adı istisnası
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("metin,konu", [
    ("Gelir İdaresi Başkanlığı Personeli Görevde Yükselme Yönetmeliği", "vergi"),
    ("Gelir İdaresi Başkanlığı Personeli Yer Değiştirme Yönetmeliği", "vergi"),
    ("Rekabet Kurumu Meslek Personeli Yönetmeliğinde Değişiklik", "rekabet"),
    ("Elektrik Üretim A.Ş. Genel Müdürlüğü Malzeme-Taşıt Değerlendirme ve "
     "Satış Yönetmeliği", "enerji"),
    ("Enerji ve Tabii Kaynaklar Uzmanlığı Yönetmeliği", "enerji"),
])
def test_ic_idare_kurum_kuralini_susturur(metin, konu):
    """Kurumun kendi personel/hurda işi, o kurumun konusu sayılmaz."""
    assert not yerel.kural_eslesmeleri(metin, konu)


@pytest.mark.parametrize("metin,konu", [
    ("Gelir İdaresi Başkanlığı Genel Tebliği (Seri No: 1)", "vergi"),
    ("Enerji Piyasası Düzenleme Kurulunun 14864 Sayılı Kararı", "enerji"),
    ("Rekabet Kurulundan İzin Alınması Gereken Birleşme ve Devralmalar Tebliği", "rekabet"),
])
def test_ic_idare_esasa_iliskin_kurali_susturmaz(metin, konu):
    """İstisna dar olmalı: kurumun ESAS işlemleri etkilenmemeli."""
    assert yerel.kural_eslesmeleri(metin, konu)


def test_ic_idare_yalniz_kurum_adi_kurallarini_etkiler():
    """Konuya bakan kurallar iç idare başlığında bile ateşlemeli.

    "Vergi Usul Kanunu" bir vergi düzenlemesidir; başlıkta 'personeli' geçmesi
    bunu değiştirmez.
    """
    metin = "Vergi Usul Kanunu Uygulamasında Personeli İlgilendiren Genel Tebliğ"
    assert yerel.kural_eslesmeleri(metin, "vergi")


def test_etiketler_kurallarla_celismez():
    """Kural 'evet' derken etiketin 'hayır' demesi düzeltilemeyen hatadır.

    Kural katmanı veto edilemediği için böyle bir kalem sistemde kalıcı yanlış
    pozitif olur VE model ona karşı eğitilir. İkisi birden kötüdür.
    """
    import etiket_hazirla as eh
    depo = json.loads((KOK / "fixtures" / "etiketler_kalem.json")
                      .read_text(encoding="utf-8"))
    _, _, etiketlenecek = eh.ayir()
    idx = {eh.anahtar(k["baslik"]): k for k in etiketlenecek}
    celiski = []
    for anahtar, deger in depo["etiket"].items():
        kal = idx.get(anahtar)
        if kal is None:
            continue
        metin = kal["bolum"] + " " + kal["baslik"]
        for konu in ("enerji", "rekabet", "vergi", "icra"):
            if yerel.kural_eslesmeleri(metin, konu) and not deger.get(konu):
                celiski.append((konu, kal["baslik"][:70]))
    assert not celiski, "kural/etiket çelişkisi: %s" % celiski[:5]
