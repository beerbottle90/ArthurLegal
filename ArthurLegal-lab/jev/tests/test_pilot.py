"""Pilot testleri — sözleşme, eşik mantığı ve güvenlik kilidi.

Testlerin çoğu "Jev doğru cevap veriyor mu"yu sınamaz; onu ancak gerçek
anahtarla ölçebilirsiniz. Burada sınanan şey daha önemlisidir: **yanlış bir
cevap geldiğinde kodun ne yaptığı.** Uç seçenek dışı değer dönerse, olasılık
aralık dışı gelirse, fixture'a gerçek veri sızarsa — kod sessizce devam
etmemeli, durmalıdır.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest

KOK = Path(__file__).resolve().parent.parent
if str(KOK) not in sys.path:
    sys.path.insert(0, str(KOK))

import jev  # noqa: E402
import pilot_b_fihrist as pb  # noqa: E402
import pilot_c_maske as pc  # noqa: E402


# --------------------------------------------------------------------------- #
# jev.py — soru kurucuları ve cevap sözleşmesi
# --------------------------------------------------------------------------- #

def test_choice_secenek_sinirlari():
    with pytest.raises(ValueError):
        jev.choice("tek seçenek olur mu", {"a": "A"})
    with pytest.raises(ValueError):
        jev.choice("çok seçenek", {"s%d" % i: "x" for i in range(256)})
    assert set(jev.choice("iki", {"a": "A", "b": "B"})["criteria"]) == {"a", "b"}


def test_noul_cevabi_bool_degil_olasiliktir():
    c = jev.Cevap("x", "noul", 0.62)
    assert c.evet_mi(0.5) is True
    assert c.evet_mi(0.7) is False
    assert c.olasilik == pytest.approx(0.62)


def test_evet_mi_yalniz_noul_icin():
    with pytest.raises(TypeError):
        jev.Cevap("x", "choice", "a").evet_mi()


def test_coz_secenek_disi_degeri_reddeder():
    """Uç 'sıfır halüsinasyon' diyor; biz yine de doğruluyoruz."""
    sorular = {"k": jev.choice("hangi", {"a": "A", "b": "B"})}
    with pytest.raises(jev.JevHatasi, match="seçenek dışı"):
        jev.GercekJev._coz({"answers": {"k": {"choice": "z"}}}, sorular)


def test_coz_aralik_disi_olasiligi_reddeder():
    sorular = {"k": jev.noul("öyle mi")}
    with pytest.raises(jev.JevHatasi, match="aralık dışı"):
        jev.GercekJev._coz({"answers": {"k": {"noul": 1.7}}}, sorular)


def test_coz_eksik_cevabi_reddeder():
    sorular = {"a": jev.noul("x"), "b": jev.noul("y")}
    with pytest.raises(jev.JevHatasi, match="cevaplamadı"):
        jev.GercekJev._coz({"answers": {"a": {"noul": 0.5}}}, sorular)


def test_coz_duz_govdeyi_de_kabul_eder():
    """Uç 'answers' sarmalı olmadan dönerse de çözülebilmeli."""
    sorular = {"a": jev.noul("x")}
    cikti = jev.GercekJev._coz({"a": {"noul": 0.3}}, sorular)
    assert cikti["a"].deger == pytest.approx(0.3)
    assert cikti["a"].sahte is False


def test_sahte_cevaplar_her_zaman_isaretli():
    istemci = jev.SahteJev({"a": {"kömür": 2.0}})
    cevaplar = istemci.sor({"baslik": "Katı Yakıt Kömür Tebliği"}, {"a": jev.noul("enerji mi")})
    assert cevaplar["a"].sahte is True
    assert cevaplar["a"].deger > 0.5


def test_olcer_maliyeti():
    o = jev.Olcer()
    o.ekle(1_000_000, 0.1)
    assert o.usd == pytest.approx(0.042)
    o.ekle(1_000_000, 0.3)
    assert o.cagri == 2
    assert o.medyan_ms == pytest.approx(300.0)


def test_katla_turkce():
    assert jev.katla("İSTANBUL Şişli") == "istanbul sisli"
    assert jev.katla("ÇAĞRI") == jev.katla("çağrı")


def test_istemci_kur_anahtarsiz_sahteye_duser(monkeypatch):
    # .env'i devre disi birak: bu test secim mantigini olcuyor, dosya
    # yuklemesini degil. Gercek bir .env varsa anahtar geri gelir ve test
    # yanlis sebeple duser.
    monkeypatch.setattr(jev, "env_yukle", lambda *a, **k: None)
    monkeypatch.delenv("JEV_API_KEY", raising=False)
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    assert isinstance(jev.istemci_kur(), jev.SahteJev)


def test_istemci_kur_anahtarla_gercege_gecer(monkeypatch):
    monkeypatch.setenv("JEV_API_KEY", "sk-test")
    istemci = jev.istemci_kur()
    assert isinstance(istemci, jev.GercekJev)
    assert istemci.sahte is False


def test_istemci_kur_zorla_sahte_anahtari_yok_sayar(monkeypatch):
    monkeypatch.setenv("JEV_API_KEY", "sk-test")
    assert isinstance(jev.istemci_kur(zorla_sahte=True), jev.SahteJev)


# --------------------------------------------------------------------------- #
# Pilot B — üç bantlı eşik
# --------------------------------------------------------------------------- #

def _sonuc(id_: int, altin: int, p: float) -> pb.KalemSonucu:
    return pb.KalemSonucu(
        {"id": id_, "tarih": "2026-01-01", "rg": "0", "bolum": "X",
         "baslik": "test", "altin": {"enerji": altin}},
        {"enerji": jev.Cevap("enerji", "noul", p, sahte=True)})


def test_kararsiz_pozitif_kacirilmis_sayilmaz():
    """Orta bant Opus'a gider; oraya düşen bir pozitif YAKALANMIŞTIR."""
    o = pb.olc([_sonuc(1, 1, 0.50)], "enerji", 0.30, 0.70)
    assert o.dogru_pozitif == 1
    assert o.yanlis_negatif == 0
    assert o.kararsiz == 1


def test_esigin_altindaki_pozitif_kacirilir():
    o = pb.olc([_sonuc(1, 1, 0.10)], "enerji", 0.30, 0.70)
    assert o.yanlis_negatif == 1
    assert o.kaciranlar == [1]
    assert o.duyarlilik == 0.0


def test_altin_pozitif_yoksa_duyarlilik_olculemez():
    """Sıfıra bölmek yerine None döner — rapor 'ölçülemedi' yazar."""
    o = pb.olc([_sonuc(1, 0, 0.9)], "enerji", 0.30, 0.70)
    assert o.duyarlilik is None
    assert o.isabet == 0.0


def test_tek_esik_bantlari_kapatir():
    """--esik 0.5 verildiğinde kararsız bant kalmaz."""
    o = pb.olc([_sonuc(1, 1, 0.50), _sonuc(2, 0, 0.49)], "enerji", 0.5, 0.5)
    assert o.kararsiz == 0
    assert o.dogru_pozitif == 1 and o.dogru_negatif == 1


def test_fixture_altin_etiketleri_tutarli():
    veri = json.loads(pb.FIXTURE.read_text(encoding="utf-8"))
    konular = set(veri["konular"])
    idler = set()
    for k in veri["kalemler"]:
        assert set(k["altin"]) == konular, "#%d eksik konu etiketi" % k["id"]
        assert k["id"] not in idler, "yinelenen id: %d" % k["id"]
        idler.add(k["id"])
        for konu in k.get("sinirda", []):
            assert konu in konular


def test_her_konunun_sorusu_var():
    veri = json.loads(pb.FIXTURE.read_text(encoding="utf-8"))
    assert set(veri["konular"]) == set(pb.SORULAR)


def test_tek_cagride_dort_soru():
    """Maliyetin can alıcı noktası: kalem başına bir çağrı, dört soru."""
    istemci = jev.SahteJev(pb.SAHTE_IPUCLARI)
    veri = json.loads(pb.FIXTURE.read_text(encoding="utf-8"))
    pb.kalemi_calistir(istemci, veri["kalemler"][0])
    assert istemci.olcer.cagri == 1


# --------------------------------------------------------------------------- #
# Pilot C — güvenlik kilidi
# --------------------------------------------------------------------------- #

def test_sentetik_isareti_olmayan_kalem_reddedilir():
    with pytest.raises(pc.SentetikOlmayanVeri, match="sentetik"):
        pc.veriyi_dogrula([{"id": 1, "metin": "zararsız", "sizinti": {}}])


def test_gecerli_tckn_calismayi_durdurur():
    """Sağlaması tutan bir numara gerçek veri şüphesidir — betik durmalı."""
    gecerli = "10000000146"
    assert not pc.gecersiz_tckn(gecerli), "test verisi hatalı: numara geçersizmiş"
    with pytest.raises(pc.SentetikOlmayanVeri, match="TUTAN"):
        pc.veriyi_dogrula([{"id": 1, "sentetik": True,
                            "metin": "T.C. Kimlik No: " + gecerli, "sizinti": {}}])


def test_tekrar_eden_rakam_gecersiz_sayilir():
    assert pc.gecersiz_tckn("11111111111")
    assert pc.gecersiz_tckn("12345678901")


def test_sifirdan_farkli_iban_reddedilir():
    with pytest.raises(pc.SentetikOlmayanVeri, match="IBAN"):
        pc.veriyi_dogrula([{"id": 1, "sentetik": True,
                            "metin": "IBAN: TR330006100519786457841326",
                            "sizinti": {}}])


def test_gercek_fixture_kilitten_gecer():
    veri = json.loads(pc.FIXTURE.read_text(encoding="utf-8"))
    pc.veriyi_dogrula(veri["kalemler"])  # istisna atmamalı


# Fixture'da geçen BÜTÜN büyük harfli ikililer. Liste kasıtlı olarak tam ve
# elle yazılmıştır: fixture'a yeni bir ad eklenirse test düşer ve birinin
# gözden geçirmesini zorlar. Amaç ad tespiti değil, sessiz değişikliği
# imkânsızlaştırmaktır — bu dosya dış bir uca gidiyor.
FIXTURE_IKILILERI = {
    "Alacaklı Demir", "Ayşe Yılmaz", "Gelir İdaresi", "Hakan Öztürk",
    "Hukuk Dairesinin", "Hukuk Muhakemeleri", "Karataş Nakliyat", "Kimlik No",
    "Mehmet Kaya", "Sosyal Güvenlik", "Yıldız Mahallesi", "Çınar Sokak",
    "İcra Hukuk", "İstanbul Anadolu",
}


def test_fixture_yeni_ad_eklenemez():
    """Fixture'a gerçek bir ad eklenirse bu test düşer — sessiz sızıntı tripwire'ı."""
    import re
    veri = json.loads(pc.FIXTURE.read_text(encoding="utf-8"))
    tum_metin = " ".join(k["metin"] for k in veri["kalemler"])
    adaylar = set(re.findall(r"\b[A-ZÇĞİÖŞÜ][a-zçğıöşü]+ [A-ZÇĞİÖŞÜ][a-zçğıöşü]+\b",
                             tum_metin))
    yeni = adaylar - FIXTURE_IKILILERI
    assert not yeni, (
        "fixture'a yeni büyük harfli ikili girmiş: %s\n"
        "Gerçek veri değilse FIXTURE_IKILILERI listesine elle ekleyin." % sorted(yeni))


def test_uydurma_kisiler_beyannamede_ve_kodda_ayni():
    """Fixture'ın ilan ettiği uydurma kimlikler ile koddaki izin listesi ayrışmasın."""
    veri = json.loads(pc.FIXTURE.read_text(encoding="utf-8"))
    ilan = set(veri["uydurma_kimlikler"]["kisiler"]) | set(
        veri["uydurma_kimlikler"]["sirketler"])
    assert ilan == pc.IZINLI_ADLAR, (
        "fixture beyanı ile pilot_c_maske.IZINLI_ADLAR ayrışmış:\n"
        "  yalnız fixture'da: %s\n  yalnız kodda: %s"
        % (sorted(ilan - pc.IZINLI_ADLAR), sorted(pc.IZINLI_ADLAR - ilan)))


def test_sizinti_kacirmak_ozette_gorunur():
    sonuc = pc.Sonuc(
        {"id": 1, "durum": "t", "aciklama": "", "metin": "",
         "sizinti": {"kisi": 1, "unvan": 0, "numara": 0, "adres": 0}},
        {a: jev.Cevap(a, "noul", 0.01, sahte=True) for a in pc.SORULAR})
    o = pc.ozetle([sonuc], 0.5)
    assert o.kacan == 1 and o.kacanlar == [1]
    assert o.duyarlilik == 0.0


def test_temiz_metinde_alarm_yanlis_alarmdir():
    sonuc = pc.Sonuc(
        {"id": 2, "durum": "t", "aciklama": "", "metin": "",
         "sizinti": {"kisi": 0, "unvan": 0, "numara": 0, "adres": 0}},
        {a: jev.Cevap(a, "noul", 0.99, sahte=True) for a in pc.SORULAR})
    o = pc.ozetle([sonuc], 0.5)
    assert o.yanlis_alarm == 1 and o.alarmlar == [2]
    assert o.duyarlilik is None


# --------------------------------------------------------------------------- #
# Uçtan uca
# --------------------------------------------------------------------------- #

def test_pilot_b_cevrimdisi_sifirla_biter(capsys):
    assert pb.main(["--sahte"]) == 0
    cikti = capsys.readouterr().out
    assert "SAHTE İSTEMCİ" in cikti
    assert "TRİYAJ" in cikti


def test_pilot_c_cevrimdisi_calisir(capsys):
    kod = pc.main(["--sahte"])
    cikti = capsys.readouterr().out
    assert "SIZINTI YAKALAMA" in cikti
    assert "üretime konulamaz" in cikti
    assert kod in (0, 1)


# --------------------------------------------------------------------------- #
# Tel üstü sözleşme — TypeSafe'in belgelenmiş şemasına birebir uyum
# --------------------------------------------------------------------------- #
#
# Bu blok, ilk sürümde YAPILAN bir hatayı kilitler: sorular belgelere
# bakılmadan yazılmıştı ve alan adları uydurulmuştu (`question`/`options`
# yerine gerçekte `instructions`/`criteria`). Anahtar geldiği gün uç 400
# dönerdi ve hata, pilotun kendi kodunda değil, aylar önce yazılmış bir
# varsayımda olurdu. Testler artık şemayı belgelenmiş hâline sabitliyor.
#
# Referans: docs.typesafe.ai/primitives ve LiteLLM TypeSafe geçiş belgeleri.

BELGELENMIS_ALANLAR = {"type", "instructions"}


def test_noul_belgelenmis_alanlari_kullanir():
    q = jev.noul("Bu bir iade talebi.")
    assert set(q) == BELGELENMIS_ALANLAR
    assert q["type"] == "noul"
    assert "question" not in q, "eski uydurma alan adı geri gelmiş"


def test_noul_criteria_istege_bagli_ve_harita():
    q = jev.noul("X doğru.", {"true": "öyleyse", "false": "değilse"})
    assert q["criteria"] == {"true": "öyleyse", "false": "değilse"}


def test_choice_criteria_haritadir_liste_degil():
    """Seçenekler açıklamalı harita olmalı: Jev'in state dışında dünya bilgisi yok."""
    q = jev.choice("Hangi ekip?", {"billing": "Ödeme, fatura, iade",
                                   "technical": "Hata, kesinti"})
    assert isinstance(q["criteria"], dict)
    assert q["criteria"]["billing"].startswith("Ödeme")
    assert "options" not in q


def test_score_criteria_sirali_listedir():
    q = jev.score("Ne kadar kızgın?", ["sakin", "rahatsız", "çok kızgın"])
    assert q["criteria"] == ["sakin", "rahatsız", "çok kızgın"]
    assert "levels" not in q
    with pytest.raises(ValueError):
        jev.score("tek seviye", ["sakin"])


def test_istek_govdesi_belgelenmis_sekilde():
    """{model, state, questions} — LiteLLM belgelerindeki gövdenin aynısı."""
    q = {"department": jev.choice("Hangi ekip?", {"billing": "b", "technical": "t"})}
    govde = {"model": "jev-latest", "state": "Ödemem 3 gündür başarısız.",
             "questions": q}
    assert set(govde) == {"model", "state", "questions"}
    assert set(govde["questions"]["department"]) == {"type", "instructions", "criteria"}


def test_yanit_belgelenmis_sekilde_cozulur():
    """LiteLLM belgelerindeki örnek yanıt birebir çözülebilmeli."""
    ham = {
        "model": "jev-1.13.0",
        "answers": {"department": {"type": "choice", "choice": "technical",
                                   "probabilities": {"billing": 0.08,
                                                     "technical": 0.85,
                                                     "sales": 0.07},
                                   "confidence": 0.82}},
        "usage": {"input_tokens": 312, "output_tokens": 48},
    }
    sorular = {"department": jev.choice("Hangi ekip?",
                                        {"billing": "b", "technical": "t", "sales": "s"})}
    cikti = jev.GercekJev._coz(ham, sorular)
    assert cikti["department"].deger == "technical"


def test_baglam_siniri_once_yakalanir(monkeypatch):
    """32k token sınırı uçta değil, bizde patlamalı — koşunun ortasında değil."""
    monkeypatch.setenv("JEV_API_KEY", "sk-test")
    istemci = jev.istemci_kur()
    kocaman = "a" * (4 * jev.AZAMI_ISTEK_TOKEN + 10_000)
    with pytest.raises(jev.JevHatasi, match="uç sınırı"):
        istemci.sor(kocaman, {"k": jev.noul("X")})


def test_openrouter_decisions_ucu_kullanilir():
    """OpenRouter'da Jev ayrı bir Decisions API'sindedir, sohbet ucunda değil.

    İlk sürümde /api/v1/systemone uydurulmuştu; sonra "Jev OpenRouter'da yok"
    denip tamamen kaldırıldı. İKİSİ DE YANLIŞTI. Doğrusu /api/alpha/decisions;
    model GET /api/v1/models listesinde görünmediği için "listelenmemiş"
    sanılıyor ve sohbet tamamlama SDK'ları onunla çalışmıyor.
    """
    assert jev.OPENROUTER_UC == "https://openrouter.ai/api/alpha/decisions"
    kaynak = (Path(__file__).resolve().parent.parent / "jev.py").read_text(
        encoding="utf-8")
    # Yorum satırları hariç: uydurma yolun neden kaldırıldığı yorumda yazılı,
    # ama kodda bulunmamalı.
    kod = " ".join(x for x in kaynak.splitlines()
                   if not x.lstrip().startswith("#"))
    assert "/api/v1/systemone" not in kod, "uydurma sohbet uç yolu geri gelmiş"
    assert "chat/completions" not in kod, "Jev sohbet ucunda çalışmaz"


def test_openrouter_anahtari_decisions_ucuna_gider(monkeypatch):
    monkeypatch.setattr(jev, "env_yukle", lambda *a, **k: None)
    monkeypatch.delenv("JEV_API_KEY", raising=False)
    monkeypatch.delenv("JEV_UC", raising=False)
    monkeypatch.delenv("JEV_MODEL", raising=False)
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")
    istemci = jev.istemci_kur()
    assert istemci._uc == jev.OPENROUTER_UC
    assert istemci._model == jev.OPENROUTER_MODEL
def test_istemci_kur_uc_ortamdan_gecersiz_kilinabilir(monkeypatch):
    """LiteLLM proxy veya Cloudflare geçişi için JEV_UC yeterli olmalı."""
    monkeypatch.setenv("JEV_API_KEY", "sk-test")
    monkeypatch.setenv("JEV_UC", "https://proxy.example/typesafe/v1/systemone")
    istemci = jev.istemci_kur()
    assert istemci._uc == "https://proxy.example/typesafe/v1/systemone"


def test_pilot_sorulari_atomik_ve_criteria_tasiyor():
    """Her soru tek yargı sormalı ve evet/hayır açıkça yazılmalı.

    TypeSafe belgeleri birden çok yargıyı tek soruya saklamayı açıkça
    yasaklıyor; ilk sürümde enerji sorusu sekiz kavram sayıyordu.
    """
    for ad, soru in pb.SORULAR.items():
        assert soru["type"] == "noul"
        assert "criteria" in soru, "%s sorusunda criteria yok" % ad
        assert set(soru["criteria"]) == {"true", "false"}
        # Kaba bir atomiklik ölçüsü: yönerge tek cümle ve kısa olmalı.
        yonerge = soru["instructions"]
        assert yonerge.count(".") <= 1, "%s yönergesi çok cümleli" % ad
        assert len(yonerge) < 160, "%s yönergesi çok uzun (%d)" % (ad, len(yonerge))


def test_olasilik_cozunurlugu_belgelenmis():
    """Jev olasılıkları 0.01'e yuvarlar; eşikler bundan ince olamaz.

    Bağımsız ölçüm: 360 satır yalnız 45 ayrı değer üretti, 53 satır 0.99'da
    eşitlendi. Sıralama ve eşik mantığı bu çözünürlüğü bilmeli.
    """
    assert jev.OLASILIK_COZUNURLUK == 0.01
    adim = pb.VARSAYILAN_UST - pb.VARSAYILAN_ALT
    assert adim >= 10 * jev.OLASILIK_COZUNURLUK, \
        "bantlar arası mesafe uç çözünürlüğüne göre anlamsız derecede dar"


def test_tam_sifir_ve_tam_bir_kabul_edilir():
    """Uç sık sık tam 0 / tam 1 döndürüyor; çözücü bunu reddetmemeli."""
    sorular = {"a": jev.noul("x"), "b": jev.noul("y")}
    cikti = jev.GercekJev._coz({"answers": {"a": {"noul": 0.0},
                                            "b": {"noul": 1.0}}}, sorular)
    assert cikti["a"].deger == 0.0 and cikti["b"].deger == 1.0


def test_confidence_alani_kullanilmiyor():
    """Bağımsız ölçüm: `confidence` üstünde eşik kurmayın — hiçbir kümede
    azami olasılıktan iyi değildi, bazılarında çok daha kötüydü."""
    sorular = {"k": jev.choice("hangi", {"a": "A", "b": "B"})}
    cikti = jev.GercekJev._coz(
        {"answers": {"k": {"choice": "a", "confidence": 0.99,
                           "probabilities": {"a": 0.51, "b": 0.49}}}}, sorular)
    assert cikti["k"].deger == "a"          # karar seçimden okunur
    assert cikti["k"].olasilik == 1.0       # choice için confidence taşınmaz


def test_bir_kalem_bir_cagri_sozlesmesi():
    """Kalemler TEK bir isteğe toplanmamalı.

    Ölçülmüş bulgu: aynı satırlar 40'lık toplu isteklerle gönderildiğinde
    sıralama kapısını GEÇEMİYOR (ters çevirme 0.171 / eşik 0.15), tek tek
    gönderildiğinde geçiyor. Toplu istek ucuz ama kaliteyi bozuyor; bu pilot
    bilinçli olarak kalem başına bir çağrı yapar.
    """
    istemci = jev.SahteJev(pb.SAHTE_IPUCLARI)
    veri = json.loads(pb.FIXTURE.read_text(encoding="utf-8"))
    for kalem in veri["kalemler"][:5]:
        pb.kalemi_calistir(istemci, kalem)
    assert istemci.olcer.cagri == 5, "kalemler tek çağrıda toplanmış"


def test_yeniden_deneme_kodlari_belgeye_uyar():
    """Belgelenmiş kodlar: 401, 422, 429, 529.

    529 (Overloaded) TypeSafe'e özgüdür ve standart "geçici hata" listelerinde
    bulunmaz; unutulursa aşırı yük anında pilot tek hatayla düşer. 401 ve 422
    ise yeniden denemeyle düzelmez — denemek yalnız gecikme üretir.
    """
    assert 529 in jev.YENIDEN_DENENIR, "529 Overloaded yeniden denenmiyor"
    assert 429 in jev.YENIDEN_DENENIR
    assert 401 not in jev.YENIDEN_DENENIR, "geçersiz anahtar denemekle düzelmez"
    assert 422 not in jev.YENIDEN_DENENIR, "doğrulama hatası denemekle düzelmez"


def test_yetkili_sozlesmeye_uyum():
    """docs.typesafe.ai/api.md'deki sözleşmenin birebir karşılığı.

    Birinci turda şema tahmin edilmişti ve tahminim, meğer ARTIK GEÇERSİZ olan
    preview API'sinin şekliydi (`document`/`prompts`/`options`/`levels`).
    Geçiş kılavuzu bunu açıkça gösteriyor. Bu test v1 sözleşmesini sabitler.
    """
    n = jev.noul("X doğru.", {"true": "öyle", "false": "değil"})
    assert n == {"type": "noul", "instructions": "X doğru.",
                 "criteria": {"true": "öyle", "false": "değil"}}
    c = jev.choice("Hangi?", {"a": "A açıklaması", "b": "B açıklaması"})
    assert c["type"] == "choice" and isinstance(c["criteria"], dict)
    sc = jev.score("Ne kadar?", ["az", "orta", "çok"])
    assert sc["type"] == "score" and sc["criteria"] == ["az", "orta", "çok"]
    # Preview dönemi alan adlarının hiçbiri kalmamalı.
    for soru in (n, c, sc):
        assert not ({"document", "prompts", "options", "levels", "question"}
                    & set(soru))


def test_score_yanitindaki_legend_cozumu_bozmaz():
    """v1'de score cevabı `legend` taşıyor; çözücü fazladan alana takılmamalı."""
    sorular = {"s": jev.score("Ne kadar?", ["az", "orta", "çok"])}
    cikti = jev.GercekJev._coz(
        {"answers": {"s": {"type": "score", "score": 1.035,
                           "legend": {"0": "az", "1": "orta", "2": "çok"},
                           "probabilities": {"0": 0.2, "1": 0.7, "2": 0.1},
                           "confidence": 0.7}}}, sorular)
    assert cikti["s"].deger == pytest.approx(1.035)


def test_env_yukle_mevcut_degiskeni_ezmez(tmp_path, monkeypatch):
    """.env, ortamda zaten tanimli bir degiskenin uzerine YAZMAMALI.

    Aksi halde `JEV_UC=... python ...` gibi tek seferlik bir gecersiz kilma
    sessizce yok sayilirdi.
    """
    dosya = tmp_path / ".env"
    dosya.write_text("JEV_MODEL=dosyadan\nJEV_UC=https://dosya.example\n",
                     encoding="utf-8")
    monkeypatch.setenv("JEV_MODEL", "ortamdan")
    monkeypatch.delenv("JEV_UC", raising=False)
    jev.env_yukle(dosya)
    assert os.environ["JEV_MODEL"] == "ortamdan"      # ezilmedi
    assert os.environ["JEV_UC"] == "https://dosya.example"   # bostu, dolduruldu


def test_env_yukle_olmayan_dosyada_sessiz(tmp_path):
    jev.env_yukle(tmp_path / "yok.env")   # istisna atmamali


# --------------------------------------------------------------------------- #
# Birleşik motor — ölçümün ürünü
# --------------------------------------------------------------------------- #

class _SabitMotor:
    """Her konuya sabit olasılık dönen sahte motor."""
    def __init__(self, deger, patlat=False):
        self._d = deger
        self._patlat = patlat
        self.olcer = jev.Olcer()

    def sor(self, state, sorular):
        if self._patlat:
            raise jev.JevHatasi("uç düştü")
        return {a: jev.Cevap(a, "noul", self._d) for a in sorular}

    def neden(self, state, konu, kac=8):
        return {"karar": self._d, "dayanak": "model"}


def test_birlesik_azamiyi_alir():
    from birlesik import BirlesikMotor
    m = BirlesikMotor(_SabitMotor(0.10), _SabitMotor(0.90))
    c = m.sor({"baslik": "x"}, {"enerji": jev.noul("y")})
    assert c["enerji"].deger == pytest.approx(0.90)


def test_birlesik_yerel_yuksekse_yereli_alir():
    from birlesik import BirlesikMotor
    m = BirlesikMotor(_SabitMotor(0.95), _SabitMotor(0.10))
    c = m.sor({"baslik": "x"}, {"icra": jev.noul("y")})
    assert c["icra"].deger == pytest.approx(0.95)


def test_birlesik_jev_dusunce_ayakta_kalir():
    """Dış uç çökünce ön eleme durmamalı; yerel motor her zaman ayaktadır."""
    from birlesik import BirlesikMotor
    m = BirlesikMotor(_SabitMotor(0.42), _SabitMotor(0.99, patlat=True))
    c = m.sor({"baslik": "x"}, {"vergi": jev.noul("y")})
    assert c["vergi"].deger == pytest.approx(0.42)
    assert m.jev_hatasi == 1


def test_birlesik_jevsiz_kurulabilir():
    from birlesik import BirlesikMotor
    m = BirlesikMotor(_SabitMotor(0.33), None)
    assert "yalnız yerel" in m.ad
    c = m.sor({"baslik": "x"}, {"enerji": jev.noul("y")})
    assert c["enerji"].deger == pytest.approx(0.33)


def test_olcum_kaydi_gercek_ucten():
    """Ölçüm kaydı saklanmalı ve sahte istemciyle üretilmemiş olmalı."""
    yol = KOK / "olcum" / "jev_altin_2026-09-20.json"
    d = json.loads(yol.read_text(encoding="utf-8"))
    assert d["sahte"] is False, "ölçüm sahte istemciyle üretilmiş"
    assert d["model_cozulen"] == "jev-1.13.0"
    assert len(d["kalemler"]) == 56
    # Yalnız kamuya açık başlık saklanmış olmalı; state alanı kaydedilmemiş.
    assert all(set(k) <= {"id", "baslik", "altin", "p"} for k in d["kalemler"])
