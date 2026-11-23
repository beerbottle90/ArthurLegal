"""ArthurLegal Hafıza (hafiza.py) testleri: Beyin uyumlu kasa düzeni, kişisel veri kapısı, yol sınırı, yazma kipleri,
devir kartı ve arşiv. Ağa çıkmaz; kasa geçici klasördedir.

    python -m unittest discover -s tests
"""
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "istemci"))
import hafiza  # noqa: E402
import ortak  # noqa: E402

SUREKLILIK = "🔮 850-Companion"


class HafizaTesti(unittest.TestCase):
    def setUp(self):
        self.kasa = Path(tempfile.mkdtemp()) / "kasa"
        self.eski = (hafiza.kasa, ortak.dil, ortak.gunluk)
        hafiza.kasa = lambda: self.kasa
        ortak.dil = lambda: "tr"
        ortak.gunluk = lambda *a: None

    def tearDown(self):
        hafiza.kasa, ortak.dil, ortak.gunluk = self.eski
        shutil.rmtree(self.kasa.parent, ignore_errors=True)

    def oku(self, goreli):
        return (self.kasa / goreli).read_text(encoding="utf-8")

    def test_kasa_beyin_duzeninde_acilir_ve_var_olan_not_ezilmez(self):
        hafiza.hazirla()
        for ad in ("Core.md", "Kurallar.md", "Last-Session.md", "Threads.md", "Journal.md"):
            self.assertTrue((self.kasa / SUREKLILIK / ad).is_file(), ad)
        self.assertTrue((self.kasa / "Projeler").is_dir())
        self.assertTrue((self.kasa / "knowledge" / "index.md").is_file())
        self.assertIn("## Active Threads", self.oku(f"{SUREKLILIK}/Threads.md"), "Beyin'in bölüm adları")
        (self.kasa / SUREKLILIK / "Core.md").write_text("# Benim notum", encoding="utf-8")
        hafiza.hazirla()
        self.assertEqual(self.oku(f"{SUREKLILIK}/Core.md"), "# Benim notum", "kullanıcının notu korunur")

    def test_var_olan_beyin_kasasinin_suereklilik_klasoru_bulunur(self):
        (self.kasa / "Benim Companion").mkdir(parents=True)
        (self.kasa / "Benim Companion" / "Soul.md").write_text("# Ruh", encoding="utf-8")
        self.assertEqual(hafiza.sureklilik().name, "Benim Companion")
        hafiza.hazirla()
        self.assertFalse((self.kasa / "Benim Companion" / "Core.md").exists(), "Soul.md varken rakip Core açılmaz")
        self.assertFalse((self.kasa / SUREKLILIK).exists())
        (self.kasa / "Ikinci Companion").mkdir()
        with self.assertRaises(hafiza.HafizaHatasi):
            hafiza.sureklilik()

    def test_kisisel_veri_kapisi(self):
        for metin, tur in (("Müvekkil TCKN 10000000146", "T.C. kimlik numarası"),
                           ("IBAN: TR33 0006 1005 1978 6457 8413 26", "IBAN"),
                           ("Tel 0532 123 45 67", "telefon"), ("+90 (212) 555 12 34'ü arayın", "telefon"),
                           ("avukat@ornek.com.tr adresine", "e-posta")):
            with self.subTest(metin=metin):
                self.assertIn(tur, hafiza.kisisel_veri(metin))
        for temiz in ("{{KİŞİ-01}} ile {{KİŞİ-02}} arasındaki 2026/1234 E., 2026/567 K. sayılı karar",
                      "6698 sayılı KVKK m. 6; 27.10.2026 tarihli dilekçe; 1.250.000 TL alacak",
                      "Kimlik no 12345678901 (sağlama tutmuyor)"):
            with self.subTest(temiz=temiz):
                self.assertEqual(hafiza.kisisel_veri(temiz), [])
        with self.assertRaisesRegex(hafiza.HafizaHatasi, "ArthurMask"):
            hafiza.yaz("Kurallar.md", "- Karşı tarafın telefonu 0532 123 45 67")
        with self.assertRaises(hafiza.HafizaHatasi):
            hafiza.oturum_karti("dosya", "IBAN TR330006100519786457841326 ödendi")

    def test_yol_kasanin_icinde_kalir(self):
        for kotu in ("../disari.md", "Projeler/../../x.md", ".obsidian/a.md", "not.txt", "", f"{SUREKLILIK}/../../y.md"):
            with self.subTest(kotu=kotu), self.assertRaises(hafiza.HafizaHatasi):
                hafiza.yaz(kotu, "metin")
        with self.assertRaises(hafiza.HafizaHatasi):
            hafiza.baslangic(dosya="../kasa-disi")
        self.assertFalse((self.kasa.parent / "disari.md").exists())

    def test_yazma_kipleri(self):
        self.assertIn(SUREKLILIK, hafiza.yaz("Kurallar.md", "- 27.10: Dilekçede başlık büyük harf."))
        self.assertIn("- 27.10: Dilekçede başlık büyük harf.\n", self.oku(f"{SUREKLILIK}/Kurallar.md"),
                      "kısa ad süreklilik klasörüne gider, sona eklenir")
        hafiza.yaz("Projeler/2026-014/Kurallar.md", "- Bu dosyada süre hesabı hep iş günüyle.", kip="yeni")
        with self.assertRaises(hafiza.HafizaHatasi):
            hafiza.yaz("Projeler/2026-014/Kurallar.md", "ikinci", kip="yeni")
        hafiza.yaz("Projeler/2026-014/Kurallar.md", "takvim günüyle", kip="degistir", eski="iş günüyle")
        self.assertIn("hep takvim günüyle", self.oku("Projeler/2026-014/Kurallar.md"))
        hafiza.yaz("Projeler/2026-014/Not.md", "a\na\n")
        with self.assertRaisesRegex(hafiza.HafizaHatasi, "2 kez"):
            hafiza.yaz("Projeler/2026-014/Not.md", "b", kip="degistir", eski="a")
        with self.assertRaises(hafiza.HafizaHatasi):
            hafiza.yaz("Projeler/2026-014/Not.md", "b", kip="sil")
        satir_sonu = self.kasa / "Projeler" / "crlf.md"
        satir_sonu.write_bytes(b"bir\r\niki\r\n")
        hafiza.yaz("Projeler/crlf.md", "uc\ndort")
        self.assertEqual(satir_sonu.read_bytes(), b"bir\r\niki\r\nuc\r\ndort\r\n", "notun satır sonu korunur")

    def test_devir_karti_yalniz_kendini_yeniden_yazar(self):
        cevap = hafiza.oturum_karti("kira sözleşmesi", "Yapılan: inceleme.\n**Karar:** tahliye ihtarı.")
        kart = re.search(r"kart=([0-9a-f]{8})", cevap).group(1)
        metin = self.oku(f"{SUREKLILIK}/Last-Session.md")
        self.assertNotIn("Henüz kart yok", metin, "başlangıç açıklaması ilk kartla kalkar")
        self.assertRegex(metin, r"(?m)^## \d{4}-\d{2}-\d{2} \d{2}:\d{2} · kira sözleşmesi · " + kart + "$")
        hafiza.oturum_karti("başka oturum", "Başka iş.")
        hafiza.oturum_karti("kira sözleşmesi", "Yapılan: inceleme bitti.", kart=kart)
        metin = self.oku(f"{SUREKLILIK}/Last-Session.md")
        self.assertIn("Başka iş.", metin, "öteki oturumun kartı kalır")
        self.assertIn("inceleme bitti", metin)
        self.assertNotIn("tahliye ihtarı", metin)
        self.assertLess(metin.index("başka oturum"), metin.index("inceleme bitti"), "yeni kart en üstte")
        with self.assertRaises(hafiza.HafizaHatasi):
            hafiza.oturum_karti("x", "y", kart="00000000")

    def test_eski_kartlar_arsive_tasinir_silinmez(self):
        for i in range(12):
            hafiza.oturum_karti(f"iş {i}", f"Kart {i}: " + "ayrıntı " * 40)
        metin = self.oku(f"{SUREKLILIK}/Last-Session.md")
        self.assertLessEqual(len(metin), hafiza.KART_SINIRI + 10)
        self.assertIn("Kart 11:", metin)
        arsiv = list((self.kasa / SUREKLILIK / "Arşiv").glob("Last-Session-*.md"))
        self.assertEqual(len(arsiv), 1)
        eski = arsiv[0].read_text(encoding="utf-8")
        self.assertTrue(eski.startswith("---\nvisibility: private\n---\n"), "Beyin arşivi otomatik bağlama yüklemez")
        for i in range(12):
            self.assertTrue(f"Kart {i}:" in metin or f"Kart {i}:" in eski, f"kart {i} kaybolmadı")

    def test_baslangic_ve_arama(self):
        hafiza.yaz("Threads.md", "### Kapanmış iş\nbitti", kip="ekle")
        hafiza.yaz("Threads.md", "### Kira davası\nTanık listesi bekleniyor.", kip="degistir", eski="Henüz açık konu yok.")
        hafiza.yaz("Projeler/2026-014/Kurallar.md", "- Bilirkişi raporuna itiraz süresi takvimde.")
        metin = hafiza.baslangic(dosya="2026-014")
        self.assertIn(f"## {SUREKLILIK}/Core.md", metin)
        self.assertIn("Tanık listesi bekleniyor", metin)
        self.assertNotIn("Kapanmış iş", metin, "kapanan konular yüklenmez")
        self.assertIn("Bilirkişi raporuna itiraz", metin)
        sonuc = hafiza.ara("BILIRKISI itiraz")
        self.assertIn("Projeler/2026-014/Kurallar.md", sonuc)
        self.assertIn("Eşleşme yok", hafiza.ara("bilirkişi", dosya="2025-001"))
        self.assertIn("Tanık listesi", hafiza.getir("Threads.md"))
        with self.assertRaises(hafiza.HafizaHatasi):
            hafiza.getir("Projeler/yok.md")

    def test_arac_tanimlari(self):
        araclar = {a["name"]: a for a in hafiza.araclar()}
        self.assertEqual(set(araclar), {"hafiza_baslangic", "hafiza_ara", "hafiza_getir", "hafiza_yaz", "hafiza_oturum_karti"})
        for ad in ("hafiza_baslangic", "hafiza_ara", "hafiza_getir"):
            self.assertTrue(araclar[ad]["annotations"]["readOnlyHint"], ad)
        for ad in ("hafiza_yaz", "hafiza_oturum_karti"):
            self.assertFalse(araclar[ad]["annotations"]["readOnlyHint"], "yazan araç izin ister: " + ad)
        self.assertIn("{{KİŞİ-01}}", araclar["hafiza_yaz"]["description"])
        self.assertIn("maskeli", hafiza.talimat_maddesi())
        self.assertIn(str(self.kasa), hafiza.talimat_maddesi())

    def buyuk_kasa(self, satir_sonu="\n"):
        """Var olan bir Beyin kasası gibi: Kurallar bütçeden büyük, en yeni kural sonda; kartlar ve konular dolu."""
        s = self.kasa / SUREKLILIK
        s.mkdir(parents=True)
        yaz = lambda ad, satirlar: (s / ad).write_bytes(satir_sonu.join(satirlar).encode("utf-8"))  # noqa: E731
        yaz("Core.md", ["# Düşünme ortağı", "", "Avukat; jargonsuz anlat."])
        yaz("Kurallar.md", ["# Kullanıcının düzeltmeleri", ""]
            + [f"- {i % 28 + 1:02d}.11: kural {i:03d}, tarih sırasıyla eklenmiş bir düzeltme satırı" for i in range(400)])
        yaz("Last-Session.md", ["# Son oturum", ""] + [f"## 2026-11-{23 - i:02d} 10:00 · iş {i} · {i:08x}\nKart {i}: yapılan, "
                                                       "karar, açık kalan ve sonraki adım." * 3 for i in range(10)])
        yaz("Threads.md", ["# Threads", "", "## Active Threads", ""]
            + [f"- konu {i:02d}: açık iş, sıradaki adım ve bağlantılı not" * 2 for i in range(40)]
            + ["", "## Closed Threads", "- kapanmış eski iş"])

    def test_buyuk_kasada_en_yeni_kurallar_ve_ilk_kartlar_yuklenir(self):
        """23.11.2026: Beyin kasasında Kurallar tek başına bütçeyi aşıyordu; en yeni kurallar kesiliyor, Last-Session ve
        Threads boş geliyordu. Bütçe paylaşılır, Kurallar sondan okunur."""
        for satir_sonu in ("\n", "\r\n"):
            with self.subTest(satir_sonu=repr(satir_sonu)):
                shutil.rmtree(self.kasa, ignore_errors=True)
                self.buyuk_kasa(satir_sonu)
                metin = hafiza.baslangic()
                self.assertLessEqual(len(metin), hafiza.BUTCE + 1500, "bütçe aşılmaz (başlık ve işaretler hariç)")
                self.assertIn("Avukat; jargonsuz anlat.", metin, "Core tam gelir")
                kurallar = metin.split(f"## {SUREKLILIK}/Kurallar.md", 1)[1].split(f"## {SUREKLILIK}/Last-Session.md")[0]
                self.assertIn("# Kullanıcının düzeltmeleri", kurallar, "başlık kalır")
                self.assertIn("kural 399", kurallar, "en yeni kural yüklenir")
                self.assertNotIn("kural 000", kurallar, "en eskisi kalkar")
                self.assertIn('en eski satırlar gösterilmedi', kurallar)
                self.assertIn(f'hafiza_getir yol="{SUREKLILIK}/Kurallar.md"', kurallar)
                for satir in kurallar.splitlines():
                    if satir.startswith("- "):
                        self.assertRegex(satir, r"^- \d\d\.11: kural \d{3}, tarih sırasıyla eklenmiş bir düzeltme satırı$",
                                         "satır yarıdan kesilmez")
                self.assertGreater(kurallar.count("\n- "), 40, "Kurallar en büyük payı alır")
                self.assertIn("Kart 0:", metin, "en yeni kart (üstte) yüklenir")
                self.assertIn("konu 00:", metin, "ilk açık konu yüklenir")
                self.assertNotIn("kapanmış eski iş", metin)
                self.assertNotIn("\r", metin)
                self.assertNotIn(chr(0x2014), metin.split("\n", 1)[0], "başlıkta uzun tire yok")

    def test_butce_ayardan_okunur_ve_sinirlanir(self):
        self.buyuk_kasa()
        eski = ortak.ayar
        try:
            for deger, beklenen in ((None, hafiza.BUTCE), ("abc", hafiza.BUTCE), (10, hafiza.BUTCE_EN_AZ),
                                    (40000, 40000), (10 ** 9, hafiza.AZAMI)):
                ortak.ayar = lambda d=deger: {"hafiza_butce": d}
                self.assertEqual(hafiza.butce(), beklenen, deger)
            ortak.ayar = lambda: {"hafiza_butce": 40000}
            metin = hafiza.baslangic()
            self.assertNotIn("kısaltıldı", metin, "büyük bütçede her şey tam gelir")
            self.assertIn("kural 000", metin)
            self.assertIn("Kart 9:", metin)
        finally:
            ortak.ayar = eski

    def test_paylastirma(self):
        pay = hafiza._paylastir([100, 20000, 3000, 8000], [1, 2, 1, 1], 9000)
        self.assertEqual(pay[0], 100, "küçük parça tamamını alır")
        self.assertLessEqual(sum(pay), 9000)
        self.assertEqual(pay[1], 2 * pay[2], "Kurallar iki pay alır")
        self.assertEqual(hafiza._paylastir([100, 200, 0], [1, 2, 1], 9000), [100, 200, 0], "sığan her şey tam gelir")
        self.assertEqual(hafiza._paylastir([5000, 100], [1, 1], 3000), [2900, 100], "artan pay büyüğe kalır")


if __name__ == "__main__":
    unittest.main()
