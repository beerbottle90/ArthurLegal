"""Doğrulama kaydı (istemci/dogrulama_kaydi.py): masa geçmişindeki atıf teyitlerinden Markdown, CSV ve Word dökümü.
Ağa çıkmaz; geçmiş ve çıktı geçici klasörde.

    python -m unittest discover -s tests
"""
import csv
import io
import json
import os
import sys
import tempfile
import unittest
import zipfile
from datetime import datetime, timezone, timedelta
from pathlib import Path
from xml.etree import ElementTree

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "istemci"))
import dogrulama_kaydi as dk  # noqa: E402

TBK_URL = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6098&MevzuatTur=1&MevzuatTertip=5"
TBK_344 = "TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG 04.02.2011/27836) m. 344"
KVKK_9 = "KİŞİSEL VERİLERİN KORUNMASI KANUNU (Kanun No. 6698, RG 07.04.2016/29677) m. 9"
KVKK_URL = "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5"

KAYITLAR = [
    # Atıf teyidi: biri doğrulandı, biri bulunamadı; bağlantı madde kaydından gelir.
    {"id": "20261105-101500-aaaaaa", "zaman": "2026-11-05T10:15:00+03:00", "ekran": "mevzuat", "kategori": "atif",
     "tur": "atif", "baslik": "Atıf teyidi (2 atıf)", "adimlar": [["tamam", "2 atıf bulundu"]],
     "sorgu": {"atiflar": [{"kanun": "6098", "madde": "344"}, {"kanun": "6098", "madde": "9999"}]},
     "anlik": {"satirlar": [
         {"kanun": "6098", "madde": "344", "ok": True, "baslik": "Kira bedelinin belirlenmesi", "citation": TBK_344, "hata": ""},
         {"kanun": "6098", "madde": "9999", "ok": False, "baslik": "", "citation": "", "hata": "NOT_FOUND"}],
         "dogru": 1, "toplam": 2}},
    # Madde getirildi: TBK'nın resmî bağlantısı buradan.
    {"id": "20261105-100000-bbbbbb", "zaman": "2026-11-05T10:00:00+03:00", "ekran": "mevzuat", "kategori": "mevzuat",
     "tur": "madde", "baslik": "TBK m. 344", "adimlar": [], "sorgu": {"hedef": {"number": "6098"}, "maddeler": ["344"]},
     "anlik": {"veri": {"law": {"number": 6098, "source_url": TBK_URL},
                        "items": [{"requested": "344", "madde_no": "344", "ok": True, "heading": "Kira bedelinin belirlenmesi",
                                   "citation": TBK_344}]}}},
    # Claude cevabı: masa teyidi; KVKK bağlantısı cevabın kaynaklarından, AY m. 20'nin bağlantısı yok (uydurulmaz).
    {"id": "20261106-090000-cccccc", "zaman": "2026-11-06T09:00:00+03:00", "ekran": "sohbet", "kategori": "claude",
     "tur": "cevap", "baslik": "Yurt dışına aktarım şartları nedir?", "adimlar": [], "sorgu": {"metin": "x"},
     "anlik": {"cevap": "…", "kaynaklar": [{"baslik": "KVKK m. 9", "atif": KVKK_9, "url": KVKK_URL},
                                           {"baslik": "uydurma", "atif": "X", "url": "javascript:alert(1)"}],
               "teyit": {"satirlar": [
                   {"kanun": "6698", "madde": "9", "ok": True, "baslik": "Kişisel verilerin yurt dışına aktarılması",
                    "citation": KVKK_9, "hata": ""},
                   {"kanun": "2709", "madde": "20", "ok": True, "baslik": "Özel hayatın gizliliği",
                    "citation": "TÜRKİYE CUMHURİYETİ ANAYASASI (Kanun No. 2709) m. 20", "hata": ""}],
                   "dogru": 2, "toplam": 2}}},
    # Atıf taşımayan kayıt: dökümde yer almaz.
    {"id": "20261106-093000-dddddd", "zaman": "2026-11-06T09:30:00+03:00", "ekran": "ictihat", "kategori": "ictihat",
     "tur": "ictihat", "baslik": "İçtihat: kira", "adimlar": [], "sorgu": {"q": "kira"}, "anlik": None},
]


class DogrulamaKaydiTesti(unittest.TestCase):
    def setUp(self):
        self.gecici = tempfile.TemporaryDirectory()
        t = Path(self.gecici.name)
        self.gecmis, self.hedef = t / "masa-gecmisi", t / "cikti"
        self.gecmis.mkdir()
        for k in KAYITLAR:
            (self.gecmis / (k["id"] + ".json")).write_text(json.dumps(k, ensure_ascii=False), encoding="utf-8")
        (self.gecmis / "dizin.json").write_text("{}", encoding="utf-8")
        (self.gecmis / "20261106-100000-eeeeee.json").write_text("{bozuk", encoding="utf-8")
        self.simdi = datetime(2026, 11, 7, 12, 0, tzinfo=timezone(timedelta(hours=3)))

    def tearDown(self):
        self.gecici.cleanup()

    def aktar(self, **girdi):
        return dk.disa_aktar(str(self.gecmis), str(self.hedef), girdi, 90, simdi=self.simdi)

    def test_satirlar_ve_baglantilar(self):
        satirlar = dk.satirlari_kur(dk.kayitlari_oku(str(self.gecmis)))
        self.assertEqual([(s["kaynak"], s["madde"], s["sonuc"]) for s in satirlar], [
            ("Madde getirildi", "344", "Doğrulandı"),
            ("Atıf teyidi", "344", "Doğrulandı"),
            ("Atıf teyidi", "9999", "Bulunamadı"),
            ("Claude cevabı (masa teyidi)", "9", "Doğrulandı"),
            ("Claude cevabı (masa teyidi)", "20", "Doğrulandı"),
        ])
        b = {(s["kaynak"], s["madde"]): s["baglanti"] for s in satirlar}
        self.assertEqual(b[("Atıf teyidi", "344")], TBK_URL, "aynı kanunun madde kaydındaki resmî bağlantı")
        self.assertEqual(b[("Atıf teyidi", "9999")], "", "doğrulanamayan atfa bağlantı verilmez")
        self.assertEqual(b[("Claude cevabı (masa teyidi)", "9")], KVKK_URL, "cevabın kaynak listesinden")
        self.assertEqual(b[("Claude cevabı (masa teyidi)", "20")], "", "kayıtta bağlantı yoksa uydurulmaz")
        bulunamayan = next(s for s in satirlar if s["madde"] == "9999")
        self.assertIn("kayıttaki numara", bulunamayan["atif"], "doğrulanmayan numara atıf gibi yazılmaz")

    def test_markdown(self):
        r = self.aktar()
        self.assertEqual((r["satir"], r["dogrulanan"], r["dogrulanamayan"], r["kayit"], r["baglantisiz"]), (5, 4, 1, 3, 1))
        yol = Path(r["dosya"])
        self.assertEqual(yol.name, "dogrulama-kaydi-20261107-120000.md")
        metin = yol.read_text(encoding="utf-8")
        self.assertIn("# ArthurLegal doğrulama kaydı", metin)
        self.assertIn(TBK_344, metin)
        self.assertIn("05.11.2026 10:15", metin)
        self.assertIn("javascript", json.dumps(KAYITLAR))
        self.assertNotIn("javascript", metin, "yalnız https bağlantı yazılır")
        self.assertIn("Maddeye yüklenen içeriğin", metin, "kaydın sınırı yazılır")
        self.assertFalse(list(self.hedef.glob("*.yaziliyor")))

    def test_csv(self):
        r = self.aktar(bicim="csv", ara="6098")
        self.assertEqual(r["satir"], 3)
        ham = Path(r["dosya"]).read_bytes()
        self.assertTrue(ham.startswith(b"\xef\xbb\xbf"), "Excel Türkçeyi BOM ile tanır")
        satirlar = list(csv.reader(io.StringIO(ham.decode("utf-8-sig")), delimiter=";"))
        self.assertEqual(satirlar[0][:3], ["Tarih ve saat", "Atıf", "Sonuç"])
        self.assertEqual(len(satirlar), 4)
        self.assertEqual({x[7] for x in satirlar[1:]}, {"6098"})

    def test_docx_gecerli(self):
        r = self.aktar(bicim="docx", baslangic="2026-11-06", bitis="2026-11-06")
        self.assertEqual(r["satir"], 2)
        with zipfile.ZipFile(r["dosya"]) as z:
            self.assertEqual(set(z.namelist()), {"[Content_Types].xml", "_rels/.rels", "word/document.xml"})
            for ad in z.namelist():
                ElementTree.fromstring(z.read(ad))  # her parça geçerli XML
            belge = z.read("word/document.xml").decode("utf-8")
        self.assertIn(KVKK_9, belge)
        self.assertNotIn(TBK_344, belge, "tarih süzgeci")
        self.assertIn('w:orient="landscape"', belge)

    def test_bos_ve_hatalar(self):
        r = self.aktar(baslangic="2026-12-01")
        self.assertIsNone(r["dosya"])
        self.assertFalse(self.hedef.exists(), "satır yoksa klasör ve dosya açılmaz")
        for girdi in ({"bicim": "pdf"}, {"baslangic": "07.11.2026"}, {"baslangic": "2026-11-07", "bitis": "2026-11-01"}):
            with self.assertRaises(dk.KayitHatasi):
                self.aktar(**girdi)
        self.assertEqual(dk.kayitlari_oku(str(self.gecmis / "yok")), [])

    def test_arac_tanimi(self):
        t = dk.arac_tanimi()
        self.assertEqual(t["name"], "al_dogrulama_kaydi")
        self.assertEqual(t["inputSchema"]["properties"]["bicim"]["enum"], ["md", "csv", "docx"])
        self.assertFalse(t["annotations"]["readOnlyHint"], "dosya yazar")
        self.assertFalse(t["annotations"]["openWorldHint"], "ağa çıkmaz")


if __name__ == "__main__":
    unittest.main()
