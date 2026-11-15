"""Arayüzlerin "Güncellemeleri denetle" düğmesi (3.3.1): al.py guncelle --denetle/--tani/--yenilikler --json.

Denetim hiçbir şey indirmez ya da kurmaz; imzalı manifesti okur, kurulu sürümlerle karşılaştırır, sonucu bir saat
saklar. Sistem bilgisi belge ya da kişisel klasör yolu taşımaz.
"""
import http.server
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_istemci import BURASI, ENV, TEST_TOHUM, ed25519, sahte_kok, sunucu_baslat  # noqa: E402

YENILIKLER = {"tr": ["Güncellemeleri denetle düğmesi", "Üç dil", "Yazı boyutu", "Sistem bilgisi", "Durum",
                     "altıncı madde gösterilmez"],
              "az": ["Yeniləmələri yoxla"], "en": ["Check for updates"], "de": ["tanınmayan dil"]}


class DenetimTesti(unittest.TestCase):
    def kur(self, t: Path, kurcala=False):
        yayin = t / "yayin"
        yayin.mkdir()
        manifest = {"surum": "0.0.2", "paket": {"dosya": "p.zip", "sha256": "0" * 64},
                    "icerik": {"bilesenler": {"masa": "99.0.0", "tapu": "9.9.9"}},
                    "mask": {"surum": "99.0.0", "url": "https://example.invalid/m.exe"},
                    "yenilikler": YENILIKLER}
        ham = json.dumps(manifest, ensure_ascii=False).encode("utf-8")
        (yayin / "arthurlegal-manifest.sig").write_text(ed25519.sign(TEST_TOHUM, ham).hex(), encoding="ascii")
        (yayin / "arthurlegal-manifest.json").write_bytes(ham.replace(b"0.0.2", b"0.0.9", 1) if kurcala else ham)

        class Statik(http.server.SimpleHTTPRequestHandler):
            sayac = 0

            def __init__(self, *a, **k):
                super().__init__(*a, directory=str(yayin), **k)

            def do_GET(self):
                type(self).sayac += 1
                super().do_GET()

            def log_message(self, *a):
                pass

        httpd, url = sunucu_baslat(Statik)
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)
        sahte_kok(t / "kok", manifest=url + "/arthurlegal-manifest.json")
        return Statik

    def al(self, t: Path, *args):
        r = subprocess.run([sys.executable, "-B", str(t / "kok" / "bin" / "al.py"), "guncelle", *args, "--json"],
                           env=ENV, capture_output=True, text=True, encoding="utf-8", timeout=120)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return json.loads(r.stdout)

    def test_yeni_surum_bulunur_hicbir_sey_kurulmaz(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kur(t)
            d = self.al(t, "--denetle")
            self.assertEqual(d["durum"], "yeni")
            self.assertEqual(d["kurulu"]["al"], "0.0.1")
            self.assertEqual(d["son"]["al"], "0.0.2")
            self.assertIn("al", d["yeni"])
            self.assertIn("masa", d["yeni"], "masanın sürümü kodundaki SURUM'dan okunur")
            self.assertNotIn("tapu", d["yeni"], "kurulu sürümü bilinmeyen modül yeni sayılmaz")
            self.assertEqual(len(d["yenilikler"]["tr"]), 5, "en çok beş madde")
            self.assertNotIn("de", d["yenilikler"])
            self.assertTrue(all(v.startswith("https://github.com/beerbottle90/") for v in d["baglanti"].values()))
            self.assertFalse(d["guncelleme"]["calisiyor"])
            self.assertFalse((t / "kok" / "surumler" / "0.0.2").exists(), "denetim kurmaz")
            self.assertFalse((t / "kok" / "aktif.txt").exists())

    def test_sonuc_bir_saat_saklanir_zorla_yeniden_sorar(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sunucu = self.kur(t)
            self.assertFalse(self.al(t, "--denetle")["onbellek"])
            istek = sunucu.sayac
            self.assertTrue(self.al(t, "--denetle")["onbellek"])
            self.assertEqual(sunucu.sayac, istek, "saklanan sonuç varken GitHub'a gidilmez")
            self.assertFalse(self.al(t, "--denetle", "--zorla")["onbellek"])
            self.assertGreater(sunucu.sayac, istek)

    def test_kurcalanmis_manifest_hata_olur(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kur(t, kurcala=True)
            d = self.al(t, "--denetle")
            self.assertEqual(d["durum"], "hata")
            self.assertIn("imza", d["hata"])
            self.assertEqual(d["yeni"], [])

    def test_ulasilamayan_sunucu_hata_olur(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")  # manifest adresi kapalı bir port
            d = self.al(t, "--denetle")
            self.assertEqual(d["durum"], "hata")
            self.assertIn("internet", d["hata"])
            self.assertFalse(self.al(t, "--denetle")["onbellek"], "hata saklanmaz: sonraki basış yeniden dener")

    def test_tani_kisisel_yol_tasimaz(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            gunluk = t / "kok" / "veri" / "gunluk"
            gunluk.mkdir(parents=True)
            (gunluk / "guncelle.log").write_text(
                f"2026-11-15 13:01:00 hata: {Path.home() / 'Belgeler' / 'x.txt'} okunamadı\n"
                "2026-11-15 13:02:00 paket güncel\n", encoding="utf-8")
            d = self.al(t, "--tani")
            for alan in ("urun", "surumler", "isletim_sistemi", "python", "dil", "moduller", "son_hatalar"):
                self.assertIn(alan, d)
            self.assertEqual(len(d["son_hatalar"]), 1)
            self.assertNotIn(str(Path.home()), json.dumps(d, ensure_ascii=False))

    def test_kurulu_yenilikler(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            (t / "kok" / "surumler" / "0.0.1" / "yenilikler.json").write_text(
                json.dumps(YENILIKLER, ensure_ascii=False), encoding="utf-8")
            d = self.al(t, "--yenilikler")
            self.assertEqual(d["surum"], "0.0.1")
            self.assertEqual(d["yenilikler"]["en"], ["Check for updates"])


class TercihTesti(unittest.TestCase):
    def calistir(self, kok: Path, kod: str):
        r = subprocess.run([sys.executable, "-B", "-c", "import json, ortak\n" + kod],
                           cwd=str(kok / "surumler" / "0.0.1" / "istemci"),
                           env={**ENV, "ARTHURLEGAL_KOK": str(kok)}, capture_output=True, text=True,
                           encoding="utf-8", timeout=60)
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)

    def test_tercih_yalniz_kendi_anahtarini_yazar(self):
        with tempfile.TemporaryDirectory() as t:
            kok = Path(t) / "kok"
            sahte_kok(kok)
            self.calistir(kok, "ortak.tercih_yaz(dil='az', gorulen_yenilikler={'mask': '1.4.0'}); print(1)")
            d = self.calistir(kok, "ortak.tercih_yaz(yazi='buyuk', gorulen_yenilikler={'masa': '3.3.1'}); "
                                   "print(json.dumps(ortak.tercihler()))")
            self.assertEqual(d, {"dil": "az", "yazi": "buyuk",
                                 "gorulen_yenilikler": {"mask": "1.4.0", "masa": "3.3.1"}})
            self.assertEqual(self.calistir(kok, "print(json.dumps(ortak.arayuz_dili()))"), "az")

    def test_gecersiz_tercih_reddedilir(self):
        with tempfile.TemporaryDirectory() as t:
            kok = Path(t) / "kok"
            sahte_kok(kok)
            d = self.calistir(kok, "\ntry:\n    ortak.tercih_yaz(yazi='dev')\n    print(0)\nexcept ValueError:\n    print(1)")
            self.assertEqual(d, 1)

    def test_dil_sirasi(self):
        with tempfile.TemporaryDirectory() as t:
            kok = Path(t) / "kok"
            sahte_kok(kok)
            self.assertEqual(self.calistir(kok, "ortak.durum_guncelle(dil='en'); print(json.dumps(ortak.arayuz_dili()))"), "en")
            self.assertEqual(self.calistir(kok, "ortak.durum_guncelle(masa_dili='az'); print(json.dumps(ortak.arayuz_dili()))"), "az")


class MasaAraciTesti(unittest.TestCase):
    def test_arac_listede_ve_yetenekte(self):
        kod = (BURASI / "istemci" / "arthurlegal_sunucu.py").read_text(encoding="utf-8")
        self.assertIn('"name": "al_guncelleme"', kod)
        self.assertIn('yetenekler.append("al_guncelleme")', kod)


if __name__ == "__main__":
    unittest.main()
