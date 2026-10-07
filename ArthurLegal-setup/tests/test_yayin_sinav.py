"""Sürüm sınavı kapısı (yayinla.surum_sinavi): ayar yoksa geçer, sınav geçerse özet döner, düşüşte ve hatada durur.

Ağa çıkmaz; sınav yerine geçici klasörde istenen çıkış koduyla biten küçük bir betik çalışır.
"""
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "yayin"))
import yayinla  # noqa: E402

BETIK = """import sys
print("ilerleme satırı")
print("SINAV: hukuk-burosu mevzuat 18/20, atifyaz 16/20")
sys.exit(int(sys.argv[1]))
"""


class SurumSinavi(unittest.TestCase):
    def setUp(self):
        self._gecici = tempfile.TemporaryDirectory()
        self.dizin = Path(self._gecici.name)
        (self.dizin / "sinav.py").write_text(BETIK, encoding="utf-8")

    def tearDown(self):
        self._gecici.cleanup()

    def _ayar(self, cikis: int) -> Path:
        yol = self.dizin / "sinav.json"
        yol.write_text(json.dumps({"komut": [sys.executable, str(self.dizin / "sinav.py"), str(cikis)]}), encoding="utf-8")
        return yol

    def _kos(self, cikis: int, kabul=None):
        with redirect_stdout(StringIO()):
            return yayinla.surum_sinavi("v9.9.9", kabul, ayar_yolu=self._ayar(cikis))

    def test_ayar_yoksa_sinavsiz_devam(self):
        with redirect_stdout(StringIO()):
            self.assertIsNone(yayinla.surum_sinavi("v9.9.9", None, ayar_yolu=self.dizin / "yok.json"))

    def test_gecen_sinav_ozeti_dondurur(self):
        self.assertEqual(self._kos(0), "hukuk-burosu mevzuat 18/20, atifyaz 16/20")

    def test_kalite_dususunde_yayin_durur(self):
        with self.assertRaises(SystemExit):
            self._kos(1)

    def test_bilerek_kabul_edilen_dusus_nota_yazilir(self):
        ozet = self._kos(1, kabul="soru kümesi değişti")
        self.assertIn("düşüş kabul edildi: soru kümesi değişti", ozet)

    def test_calismayan_sinav_yayini_durdurur(self):
        with self.assertRaises(SystemExit):
            self._kos(2)

    def test_yer_tutucular_doldurulur(self):
        yol = self.dizin / "sinav.json"
        yol.write_text(json.dumps({"komut": [sys.executable, "-c",
                                             "import sys; print('SINAV: ' + sys.argv[1] + ' ' + sys.argv[2])",
                                             "{etiket}", "{kok}"]}), encoding="utf-8")
        with redirect_stdout(StringIO()):
            ozet = yayinla.surum_sinavi("v9.9.9", None, ayar_yolu=yol)
        self.assertEqual(ozet, f"v9.9.9 {BURASI.parent}")


if __name__ == "__main__":
    unittest.main()
