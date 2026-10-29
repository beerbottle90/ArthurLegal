"""Claude dizini denetimi (dizin_denetimi.py) ve eklenti sürüm kuralının ağsız kısmı.

Kayıt (dizin_kaydi.json) bağlayıcı ilanının söylediğini tutar; eklentinin bağlantısı ve yargı çevresi sayısı onunla
aynı olmalı. Canlı uçla karşılaştırma haftalık GitHub işindedir (dizin-denetimi.yml); burada aynı karşılaştırma uydurma
araç listesiyle sınanır.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "tests"))
sys.path.insert(0, str(BURASI / "yayin"))
import dizin_denetimi  # noqa: E402
import eklenti_uret  # noqa: E402


def _arac(ad, baslik="Başlık", salt_okunur=True):
    return {"name": ad, "title": baslik, "annotations": {"readOnlyHint": salt_okunur} if salt_okunur is not None else {}}


class Kayit(unittest.TestCase):
    def setUp(self):
        self.kayit = json.loads(dizin_denetimi.KAYIT.read_text(encoding="utf-8"))
        self.b = self.kayit["baglayici"]

    def test_kayit_kendi_icinde_tutarli(self):
        self.assertEqual(self.b["arac_sayisi"], len(self.b["araclar"]))
        self.assertEqual(self.b["araclar"], sorted(set(self.b["araclar"])))
        self.assertEqual(self.b["yargi_cevresi"], len(dizin_denetimi.yargi_cevreleri(self.b["araclar"])))

    def test_eklenti_ilanla_ayni_seyi_soyler(self):
        self.assertEqual(eklenti_uret.MCP_URL, self.b["url"])
        self.assertEqual(eklenti_uret.YARGI_CEVRESI, self.b["yargi_cevresi"])

    def test_ayni_liste_gecer(self):
        sonuc = dizin_denetimi.karsilastir(self.kayit, [_arac(a) for a in self.b["araclar"]])
        self.assertEqual([s[0] for s in sonuc], ["geçti"] * 3, sonuc)

    def test_eklenen_arac_ve_kural_ihlali_kalir(self):
        araclar = [_arac(a) for a in self.b["araclar"][1:]] + [_arac("xx_yeni_arac", baslik="", salt_okunur=None)]
        sonuc = {s[1]: s for s in dizin_denetimi.karsilastir(self.kayit, araclar)}
        self.assertEqual(sonuc["araç listesi"][0], "kaldı")
        self.assertIn("xx_yeni_arac", sonuc["araç listesi"][2])
        self.assertIn(self.b["araclar"][0], sonuc["araç listesi"][2])
        self.assertEqual(sonuc["dizin kuralları"][0], "kaldı")
        self.assertIn("başlık yok", sonuc["dizin kuralları"][2])
        self.assertEqual(sonuc["yargı çevresi"][0], "kaldı")   # xx yeni bir önek


class EklentiSurumu(unittest.TestCase):
    def test_yeni_surum(self):
        self.assertEqual(eklenti_uret.yeni_surum("1.12.5", "1.12.5"), "1.12.6")
        self.assertEqual(eklenti_uret.yeni_surum("1.12.6", "1.12.6"), "1.12.7")
        self.assertEqual(eklenti_uret.yeni_surum("1.12.9", "1.13.0"), "1.13.0")   # paketin gerisinde kalmaz
        self.assertEqual(eklenti_uret.yeni_surum("1.12.9", "1.12.10"), "1.12.10")
        with self.assertRaises(eklenti_uret.EklentiHata):
            eklenti_uret.yeni_surum("1.12", "1.12.5")

    def test_degisen_eklentide_surum_artmali(self):
        with tempfile.TemporaryDirectory() as d:
            kok = Path(d)
            manifest = kok / eklenti_uret.CIKTI / ".claude-plugin" / "plugin.json"
            beceri = kok / eklenti_uret.CIKTI / "README.md"
            manifest.parent.mkdir(parents=True)

            def yaz(surum, metin):
                manifest.write_text(json.dumps({"name": "x", "version": surum}), encoding="utf-8")
                beceri.write_text(metin, encoding="utf-8")

            def git(*args):
                subprocess.run(["git", "-C", d, "-c", "user.name=t", "-c", "user.email=t@t", "-c",
                                "core.autocrlf=false", *args], check=True, capture_output=True)

            git("init", "-q")
            yaz("1.0.0", "ilk")
            git("add", "-A")
            git("commit", "-q", "-m", "ilk")
            self.assertEqual(eklenti_uret.surum_denetle("HEAD", kok), [])          # değişiklik yok
            yaz("1.0.0", "ikinci")
            self.assertEqual(len(eklenti_uret.surum_denetle("HEAD", kok)), 1)      # değişti, sürüm aynı
            yaz("1.0.1", "ikinci")
            self.assertEqual(eklenti_uret.surum_denetle("HEAD", kok), [])          # değişti, sürüm arttı
            (kok / eklenti_uret.CIKTI / "yeni.md").write_text("x", encoding="utf-8")
            yaz("1.0.0", "ilk")
            self.assertEqual(len(eklenti_uret.surum_denetle("HEAD", kok)), 1)      # yeni dosya da değişikliktir
            with self.assertRaises(eklenti_uret.EklentiHata):
                eklenti_uret.surum_denetle("yok-boyle-bir-ref", kok)


if __name__ == "__main__":
    unittest.main()
