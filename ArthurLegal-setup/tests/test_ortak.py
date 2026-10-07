"""Ortak rehberler: paketlerdeki kopyalar tek kaynakla (ArthurLegal-setup/ortak-rehberler/) aynı mı; türetme kuralları doğru mu.

Ağa çıkmaz. Gerçek depoyu yalnız okur; türetme sınamaları geçici bir klasördeki uydurma paketlerle yapılır.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "yayin"))
import ortak_uret  # noqa: E402


class OrtakRehberler(unittest.TestCase):
    def test_kopyalar_kaynakla_ayni(self):
        sorunlar = ortak_uret.denetle()
        self.assertEqual(sorunlar, [], "\n".join(sorunlar) + "\nOrtak rehberi paketin içinde değil kaynağında "
                         "(ArthurLegal-setup/ortak-rehberler/references/) düzeltip `python ArthurLegal-setup/yayin/ortak_uret.py` "
                         "çalıştırın.")

    def test_tablodaki_her_degisken_kullaniliyor(self):
        tablo = ortak_uret.tablo_oku(ortak_uret.KOK)
        kullanilan = set()
        for yol in (ortak_uret.ortak_dizini(ortak_uret.KOK) / "references").glob("*.md"):
            kullanilan |= set(ortak_uret.DEGISKEN.findall(yol.read_text(encoding="utf-8")))
        self.assertEqual(sorted(set(tablo["degiskenler"]) - kullanilan), [])


class Turetme(unittest.TestCase):
    def setUp(self):
        self._gecici = tempfile.TemporaryDirectory()
        self.kok = Path(self._gecici.name)
        tablo = {
            "paketler": {"buro": "ArthurLegal-Buro-v*-Public-Release", "sirket": "ArthurLegal-Sirket-v*-Public-Release"},
            "degiskenler": {"KURUM": {"buro": "[Müvekkil]", "sirket": "[ŞİRKET ADI]"}},
            "rehberler": {},
        }
        ortak = self.kok / "ArthurLegal-setup" / "ortak-rehberler"
        (ortak / "references").mkdir(parents=True)
        (ortak / "paketler.json").write_text(json.dumps(tablo, ensure_ascii=False), encoding="utf-8")
        self.buro = self.kok / "ArthurLegal-Buro-v1.0.0-Public-Release" / "knowledge" / "references"
        self.sirket = self.kok / "ArthurLegal-Sirket-v2.0.0-Public-Release" / "knowledge" / "references"
        self.buro.mkdir(parents=True)
        self.sirket.mkdir(parents=True)

    def tearDown(self):
        self._gecici.cleanup()

    def _yaz(self, ad, buro, sirket, bom_crlf=False):
        (self.buro / ad).write_text(buro, encoding="utf-8", newline="\n")
        ham = ("﻿" + sirket.replace("\n", "\r\n")) if bom_crlf else sirket
        (self.sirket / ad).write_bytes(ham.encode("utf-8"))

    def test_yer_tutucu_farki_degiskene_doner(self):
        self._yaz("a.md", "# A\n\n[Müvekkil]'ın sözleşmesi.\n", "# A\n\n[ŞİRKET ADI]'ın sözleşmesi.\n")
        kabul, red = ortak_uret.benimse(["a.md"], self.kok)
        self.assertEqual((kabul, red), (["a.md"], {}))
        kaynak = (self.kok / "ArthurLegal-setup" / "ortak-rehberler" / "references" / "a.md").read_text(encoding="utf-8")
        self.assertIn("{{AL_KURUM}}'ın sözleşmesi.", kaynak)
        self.assertEqual(ortak_uret.denetle(self.kok), [])

    def test_icerik_farki_reddedilir(self):
        self._yaz("b.md", "Muhafaza süresi 5 yıl.\n", "Muhafaza süresi 8 yıl.\n")
        kabul, red = ortak_uret.benimse(["b.md"], self.kok)
        self.assertEqual(kabul, [])
        self.assertIn("içerik farkı", red["b.md"])

    def test_pakette_elle_duzeltme_yakalanir(self):
        self._yaz("c.md", "Aynı metin.\n", "Aynı metin.\n")
        ortak_uret.benimse(["c.md"], self.kok)
        (self.sirket / "c.md").write_text("Aynı metin, elle düzeltildi.\n", encoding="utf-8")
        self.assertEqual(ortak_uret.denetle(self.kok), ["c.md: sirket paketindeki kopya kaynaktan farklı"])

    def test_kaynak_degisince_kopyalar_uretilir_bom_ve_satir_sonu_korunur(self):
        self._yaz("d.md", "[Müvekkil] için not.\n", "[ŞİRKET ADI] için not.\n", bom_crlf=True)
        ortak_uret.benimse(["d.md"], self.kok)
        kaynak = self.kok / "ArthurLegal-setup" / "ortak-rehberler" / "references" / "d.md"
        kaynak.write_text("{{AL_KURUM}} için güncel not.\n", encoding="utf-8", newline="\n")
        self.assertEqual(ortak_uret.yaz_paketlere(self.kok), 2)
        self.assertEqual((self.buro / "d.md").read_text(encoding="utf-8"), "[Müvekkil] için güncel not.\n")
        self.assertEqual((self.sirket / "d.md").read_bytes().decode("utf-8"), "﻿[ŞİRKET ADI] için güncel not.\r\n")
        self.assertEqual(ortak_uret.denetle(self.kok), [])


if __name__ == "__main__":
    unittest.main()
