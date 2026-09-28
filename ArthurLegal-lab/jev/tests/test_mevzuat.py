"""Mevzuat sınav kümesi ve aktarım ölçümü — sözleşme testleri.

Bu testler modelin NE KADAR iyi olduğunu kilitlemez (o bir ölçümdür, değişebilir);
ölçümün DÜRÜST kalmasını kilitler: iki dilim ayrı tutulur, görülmemiş kalemler
eğitime sızmaz, torba kanun asla sessizce elenmez.
"""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

import pytest

KOK = Path(__file__).resolve().parent.parent
TR = KOK.parent / "ArthurLegalTR"
ALTIN = KOK / "fixtures" / "mevzuat_altin.json"

pytestmark = pytest.mark.skipif(not (TR / "triyaj.py").exists(),
                                reason="ArthurLegalTR yan depoda yok; çıkarım modülü oradadır")

sys.path.insert(0, str(KOK))
import olc_mevzuat  # noqa: E402


def _veri():
    return json.load(io.open(ALTIN, encoding="utf-8"))


def _norm(metin: str) -> str:
    sys.path.insert(0, str(TR))
    import triyaj
    return re.sub(r"\s+", " ", triyaj.katla(metin)).strip()


def test_kume_butun_ve_etiketler_ikili():
    v = _veri()
    assert v["konular"] == ["enerji", "rekabet", "vergi", "icra"]
    assert len(v["kalemler"]) == 187
    assert [k["id"] for k in v["kalemler"]] == list(range(1, 188))
    for k in v["kalemler"]:
        assert set(k["altin"]) == set(v["konular"])
        assert all(x in (0, 1) for x in k["altin"].values()), k["id"]
        assert k["tur"] in olc_mevzuat.TUR_BOLUM
        assert "\n" not in k["baslik"], "başlıktaki satır sonları kurulumda düzlenmeli"


def test_gorulmemis_dilim_gercekten_egitimde_yok():
    """Genelleme bu dilimden okunur. Bir başlık eğitim etiketlerinde varsa orada duramaz."""
    egitim = json.load(io.open(KOK / "fixtures" / "etiketler_kalem.json", encoding="utf-8"))["etiket"]
    egitim_anahtar = {_norm(b) for b in egitim}
    v = _veri()
    gorulmemis = [k for k in v["kalemler"] if not k["egitimde_goruldu"]]
    assert len(gorulmemis) == 60
    sizan = [k["id"] for k in gorulmemis if _norm(k["baslik"]) in egitim_anahtar]
    assert not sizan, "eğitimde görülen kalem 'görülmemiş' dilimde: %s" % sizan
    yanlis = [k["id"] for k in v["kalemler"] if k["egitimde_goruldu"] and _norm(k["baslik"]) not in egitim_anahtar]
    assert not yanlis


def test_rg_altin_kumesiyle_cakisan_kalemler_ayni_etiketi_tasir():
    """İki sınav kümesi aynı kalem için farklı şey söylerse ikisi de güvenilmez olur."""
    rg = {_norm(k["baslik"]): k["altin"] for k in
          json.load(io.open(KOK / "fixtures" / "fihrist_altin.json", encoding="utf-8"))["kalemler"]}
    cakisan = [k for k in _veri()["kalemler"] if _norm(k["baslik"]) in rg]
    assert len(cakisan) == 5
    for k in cakisan:
        assert k["altin"] == rg[_norm(k["baslik"])], k["id"]
        assert not k["egitimde_goruldu"], "RG altın kalemi eğitime girmiş olamaz"


def test_elle_etiketli_pozitifler_gerekceli():
    """Elle verilen her pozitif ve her sınır kararı gerekçesini taşımalı."""
    for k in _veri()["kalemler"]:
        if k["etiket_kaynagi"].startswith("elle") and (any(k["altin"].values()) or k.get("sinirda")):
            assert k.get("gerekce"), "#%d gerekçesiz" % k["id"]


def test_torba_kanun_adlari_cevrimdisi_duruyor():
    """Ölçüm ağa çıkmaz: değiştirilen kanun adları fixture'dadır."""
    torba = {k["id"]: k for k in _veri()["kalemler"] if k.get("torba")}
    assert set(torba) == {2, 3, 5}
    assert "İcra ve İflas Kanunu" in torba[5]["degistirilen_kanunlar"]
    assert "Damga Vergisi Kanunu" in torba[2]["degistirilen_kanunlar"], \
        "'ile \\nilgili olup' satır sonu her ikinci kanunu kaçırtmıştı"
    assert torba[3]["degistirilen_kanunlar"] == []        # 'İlgili Kanunlara işlenmiştir'
    assert not any(ad.strip().lower() in ("kanun", "kanun hükmünde kararname")
                   for k in torba.values() for ad in k["degistirilen_kanunlar"])


def test_adlari_okunamayan_torba_kanun_asla_elenmez():
    m = olc_mevzuat.motor()
    k3 = next(k for k in _veri()["kalemler"] if k["id"] == 3)
    for konu in ("enerji", "rekabet", "vergi", "icra"):
        assert olc_mevzuat.skorla(m, k3, konu, torba=True)["kaynak"] == "belirsiz"
    r = olc_mevzuat.olc(0.20, torba=True)
    assert all(o["belirsiz_tutulan"] == 1 for o in r["dilimler"]["gorulmemis"]["konular"].values())


def test_olcum_iki_dilimi_ayri_raporlar_ve_torba_gecisi_yalniz_ekler():
    acik = olc_mevzuat.olc(0.20, torba=True)
    kapali = olc_mevzuat.olc(0.20, torba=False)
    assert acik["dilimler"]["gorulmus"]["n"] == 127 and acik["dilimler"]["gorulmemis"]["n"] == 60
    for dilim in ("gorulmus", "gorulmemis"):
        for konu, o in acik["dilimler"][dilim]["konular"].items():
            k = kapali["dilimler"][dilim]["konular"][konu]
            assert o["pozitif"] == k["pozitif"]
            assert o["yakalanan"] >= k["yakalanan"], "torba geçişi bir pozitifi düşürdü (%s/%s)" % (dilim, konu)


def test_mcp_kunyesi_olcumle_ayni_sayilari_tasir():
    """Uçta duyurulan sayılar bu ölçümün çıktısıdır; biri değişip diğeri kalırsa yalan olur."""
    sys.path.insert(0, str(TR))
    import triyaj
    if not hasattr(triyaj, "MEVZUAT_OLCUM"):
        pytest.skip("ArthurLegalTR bu sürümde mevzuat ölçümünü taşımıyor")
    r = olc_mevzuat.olc(0.20, torba=True)
    g = r["dilimler"]["gorulmemis"]["konular"]
    duyurulan = triyaj.MEVZUAT_OLCUM["gorulmemis"]
    for konu in ("enerji", "rekabet", "vergi", "icra"):
        assert duyurulan[konu] == {"pozitif": g[konu]["pozitif"], "yakalanan": g[konu]["yakalanan"]}, konu
    assert duyurulan["yanlis_pozitif"] == sum(len(o["yanlis_pozitif"]) for o in g.values())
    gm = r["dilimler"]["gorulmus"]["konular"]
    b = triyaj.MEVZUAT_OLCUM["bicim_aktarimi"]
    assert b["pozitif"] == sum(o["pozitif"] for o in gm.values())
    assert b["yakalanan"] == sum(o["yakalanan"] for o in gm.values())
    assert b["yanlis_pozitif"] == sum(len(o["yanlis_pozitif"]) for o in gm.values())
    t = olc_mevzuat.olc(0.20, torba=False)["dilimler"]["gorulmemis"]["konular"]
    assert duyurulan["torba_gecisi_olmadan"] == {"vergi": t["vergi"]["yakalanan"], "icra": t["icra"]["yakalanan"]}
