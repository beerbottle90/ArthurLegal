"""Paket denetimi testleri (yayin/paket_denetimi.py): depo kökündeki paketlerde yeni kırık skill atfı,
sürüm ve sayım uyuşmazlığı, paketler arasında yeni ayrışma; ayrıca denetleyicinin kendisi, geçici klasördeki
küçük uydurma paketlerle. Ağa çıkmaz, birkaç saniyede biter.

    python -m unittest discover -s tests                            (ArthurLegal-setup içinden)
    python -m unittest ArthurLegal-setup/tests/test_paketler.py -v   (depo kökünden)

Bilinen eski sorunlar tests/paket_denetimi_taban.json'dadır; testler yalnız tabanda olmayan sorunda kırılır.
"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

BURASI = Path(__file__).resolve().parent
KOK = BURASI.parents[1]  # depo kökü
TABAN = BURASI / "paket_denetimi_taban.json"
sys.path.insert(0, str(BURASI.parent / "yayin"))
import paket_denetimi as pd  # noqa: E402

KITAPCIK = """# ornek-legal - Skill Referans Kitapçığı

> Toplam skill: 2

## İçindekiler

- /ornek-legal:inceleme (12 satir)
- /ornek-legal:ozet (8 satir)

---

## /ornek-legal:inceleme

İnceleme adımları; sonunda /ornek-legal:ozet çağrılır.

## /ornek-legal:ozet

Özet adımları.
"""
EK = "NOTLAR.md"  # paket kökünde: atıf taranır, knowledge sayımına girmez


def sahte_paket(kok: Path, ad: str = "Deneme", surum: str = "1.0.0", dosyalar: dict | None = None) -> Path:
    """Denetimden temiz geçen küçük bir paket; `dosyalar` ({göreli yol: metin}) ekler ya da değiştirir."""
    p = kok / f"ArthurLegal-{ad}-v{surum}-Public-Release"
    icerik = {
        "VERSION.md": f"{surum}\n",
        # "bölüm 5 eklenti" sayım değildir; CHANGELOG'daki kaldırılmış komut kırık atıf değildir
        "SYSTEM_PROMPT.md": (f"# Sistem Talimatları: ArthurLegal {ad} v{surum}\n\n"
                             f"> Sürüm {surum}. Talimat revizyonu: bölüm 5 eklenti tablosu.\n"
                             "> Paket: 1 plugin, 2 skill, 1 referans, 2 knowledge dosyası.\n\n---\n\n"
                             "Her işte önce /ornek-legal:inceleme.\n"),
        "README.md": f"# ArthurLegal {ad}\n\n**Sürüm:** v{surum}\n",
        "CHANGELOG.md": f"# Değişiklikler\n\n## [{surum}] — 2026-01-01\n\n- /ornek-legal:eski-komut kaldırıldı.\n",
        "knowledge/skills/ornek-legal__skills.md": KITAPCIK,
        "knowledge/references/rehber.md": "# Rehber\n\nAyrıntı: /ornek-legal:ozet.\n",
        **(dosyalar or {}),
    }
    for goreli, metin in icerik.items():
        yol = p / goreli
        yol.parent.mkdir(parents=True, exist_ok=True)
        yol.write_text(metin, encoding="utf-8", newline="\n")
    return p


def satirlar(bulgular) -> str:
    return "\n" + "\n".join(f"  {b}" for b in bulgular)


class PaketlerTesti(unittest.TestCase):
    """Depodaki paketler; tabandaki bilinen sorunlar testi kırmaz."""

    @classmethod
    def setUpClass(cls):
        cls.rapor = pd.denetle(KOK, TABAN)

    def test_paketler_ve_taban_bulundu(self):
        self.assertTrue(self.rapor.paketler, f"{KOK} altında ArthurLegal-*-v*-Public-Release klasörü yok")
        self.assertTrue(TABAN.is_file(), "taban dosyası yok: python ArthurLegal-setup/yayin/paket_denetimi.py --taban-yaz")

    def test_yeni_kirik_atif_yok(self):
        self.assertFalse(self.rapor.yeni_atif, "Pakette tanımlı olmayan skill'e yeni atıf (atfı düzeltin; bilinçliyse "
                                               "--taban-yaz):" + satirlar(self.rapor.yeni_atif))

    def test_surumler_tutarli(self):
        self.assertFalse(self.rapor.surum, "Sürüm, klasör adındakiyle aynı değil:" + satirlar(self.rapor.surum))

    def test_sayimlar_tutarli(self):
        self.assertFalse(self.rapor.sayim, "Yazılan sayı gerçek sayıyla aynı değil:" + satirlar(self.rapor.sayim))

    def test_yeni_ayrisma_yok(self):
        self.assertFalse(self.rapor.yeni_ayrisma, "Tabanda aynı olan kopyalar artık farklı (değişikliği öteki pakete de "
                                                  "uygulayın; bilinçliyse --taban-yaz):" + satirlar(self.rapor.yeni_ayrisma))


class DenetleyiciTesti(unittest.TestCase):
    """Denetleyicinin kendisi, geçici klasördeki uydurma paketlerle."""

    def setUp(self):
        gecici = tempfile.TemporaryDirectory()
        self.addCleanup(gecici.cleanup)
        self.kok = Path(gecici.name)
        self.taban = self.kok / "taban.json"

    def denetle(self) -> pd.Rapor:
        return pd.denetle(self.kok, self.taban)

    def test_temiz_paket_gecer(self):
        sahte_paket(self.kok)
        r = self.denetle()
        self.assertTrue(r.tamam, satirlar(r.yeni_atif + r.surum + r.sayim + r.yeni_ayrisma))
        self.assertEqual({"/ornek-legal:inceleme", "/ornek-legal:ozet"}, r.tanimli["Deneme"])
        self.assertGreaterEqual(len(r.surum_yerleri), 5)
        self.assertGreaterEqual(len(r.sayim_yerleri), 5)

    def test_kirik_atif_yakalanir(self):
        sahte_paket(self.kok, dosyalar={EK: "Bkz. /ornek-legal:yok-boyle ve /baska-legal:inceleme.\n"
                                            "Adresteki yol atıf değildir: https://example.com/ornek-legal:x\n"})
        r = self.denetle()
        self.assertEqual(["/baska-legal:inceleme", "/ornek-legal:yok-boyle"],
                         sorted(b.mesaj.split()[0] for b in r.yeni_atif))
        self.assertEqual({(EK, 1)}, {(b.dosya, b.satir) for b in r.yeni_atif})
        self.assertIn("ornek-legal eklentisinde yok-boyle skill'i yok", satirlar(r.yeni_atif))
        self.assertIn("baska-legal eklentisi bu pakette yok", satirlar(r.yeni_atif))

    def test_planli_atif_kirik_sayilmaz(self):
        sahte_paket(self.kok, dosyalar={EK: "- /ornek-legal:taslak (hazırlanıyor)\n"})
        r = self.denetle()
        self.assertEqual([], r.yeni_atif)
        self.assertEqual(["planli"], [a.tur for a in r.atiflar["Deneme"]])

    def test_eski_eklenti_adi_kirik_sayilir(self):
        sahte_paket(self.kok, dosyalar={EK: "Önce /dispute-litigation:case-intake.\n"})
        r = self.denetle()
        self.assertEqual(["eski_ad"], [a.tur for a in r.atiflar["Deneme"]])
        self.assertEqual(1, len(r.yeni_atif))
        self.assertIn("eski eklenti adı", r.yeni_atif[0].mesaj)

    def test_surum_uyusmazligi_yakalanir(self):
        sahte_paket(self.kok, surum="1.1.0", dosyalar={
            "README.md": "# X\n\n**Sürüm:** v1.0.9\n\nSürüm 0.9.0'dan beri bu özellik var.\n",  # düz yazı sayılmaz
            "CHANGELOG.md": "# Değişiklikler\n\n## [1.0.9] — 2026-01-01\n"})
        r = self.denetle()
        self.assertEqual(["CHANGELOG.md", "README.md"], sorted(b.dosya for b in r.surum))
        self.assertIn("klasör adındaki sürüm 1.1.0", r.surum[0].mesaj)
        self.assertIn(("SYSTEM_PROMPT.md", 1), {(b.dosya, b.satir) for b in r.surum_yerleri})

    def test_ayni_paketin_iki_klasoru_yakalanir(self):
        sahte_paket(self.kok, surum="1.0.0")
        sahte_paket(self.kok, surum="1.1.0")
        self.assertIn("2 klasörü var", satirlar(self.denetle().surum))

    def test_sayim_uyusmazligi_yakalanir(self):
        p = sahte_paket(self.kok, dosyalar={
            "knowledge/skills/ornek-legal__skills.md": KITAPCIK.replace("Toplam skill: 2", "Toplam skill: 3")})
        sp = p / "SYSTEM_PROMPT.md"
        sp.write_text(sp.read_text(encoding="utf-8").replace("1 referans", "2 referans"), encoding="utf-8")
        r = self.denetle()
        self.assertEqual(["SYSTEM_PROMPT.md", "knowledge/skills/ornek-legal__skills.md"], sorted(b.dosya for b in r.sayim))
        self.assertIn("'2 referans' yazıyor, pakette 1 referans var", satirlar(r.sayim))

    def test_tabandaki_atif_kirmaz_yenisi_kirar(self):
        p = sahte_paket(self.kok, dosyalar={EK: "/ornek-legal:yok-boyle\n"})
        ek = p / EK
        pd.taban_yaz(self.kok, self.taban)
        self.assertTrue(self.denetle().tamam)
        ek.write_text("Giriş.\n\nSatırı kaydı: /ornek-legal:yok-boyle\n", encoding="utf-8")
        self.assertTrue(self.denetle().tamam, "satır numarası kayınca bilinen atıf yeni sayılmamalı")
        ek.write_text("/ornek-legal:yok-boyle\n/ornek-legal:yok-boyle\n", encoding="utf-8")
        self.assertEqual([(EK, 2)], [(b.dosya, b.satir) for b in self.denetle().yeni_atif])
        ek.write_text("Düzeltildi.\n", encoding="utf-8")
        r = self.denetle()
        self.assertTrue(r.tamam)
        self.assertEqual(1, len(r.duzelen_atif))
        # --taban-yaz elle yazılmış notu korur
        ek.write_text("/ornek-legal:yok-boyle\n", encoding="utf-8")
        pd.taban_yaz(self.kok, self.taban)
        taban = json.loads(self.taban.read_text(encoding="utf-8"))
        taban["kirik_atiflar"]["Deneme"][0]["not"] = "bilinçli: skill sonraki sürümde"
        self.taban.write_text(json.dumps(taban, ensure_ascii=False), encoding="utf-8")
        pd.taban_yaz(self.kok, self.taban)
        self.assertIn("bilinçli: skill sonraki sürümde", self.taban.read_text(encoding="utf-8"))

    def test_yeni_ayrisma_yakalanir_duzelen_bilgi(self):
        sahte_paket(self.kok, ad="Bir")
        sahte_paket(self.kok, ad="Uc")
        rehber = sahte_paket(self.kok, ad="Iki") / "knowledge" / "references" / "rehber.md"
        ilk = rehber.read_text(encoding="utf-8")
        pd.taban_yaz(self.kok, self.taban)
        self.assertTrue(self.denetle().tamam)
        rehber.write_bytes(rehber.read_bytes().replace(b"\n", b"\r\n"))
        self.assertTrue(self.denetle().tamam, "yalnız satır sonu farkı ayrışma sayılmamalı")
        rehber.write_text("# Rehber\n\nYalnız bu pakette değişti.\n", encoding="utf-8")
        r = self.denetle()
        self.assertEqual(["knowledge/references/rehber.md"], [b.dosya for b in r.yeni_ayrisma])
        self.assertIn("tabanda aynıydı, şimdi: Bir = Uc | Iki", r.yeni_ayrisma[0].mesaj)
        pd.taban_yaz(self.kok, self.taban)  # bilinçli ayrışma kabul edildi
        self.assertTrue(self.denetle().tamam)
        rehber.write_text(ilk, encoding="utf-8")
        r = self.denetle()
        self.assertTrue(r.tamam)
        self.assertEqual(1, len(r.duzelen_ayrisma))

    def test_komut_satiri(self):
        sahte_paket(self.kok, dosyalar={EK: "/ornek-legal:yok-boyle\n"})
        arg = ["--kok", str(self.kok), "--taban", str(self.taban)]
        with contextlib.redirect_stdout(io.StringIO()) as cikti, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(1, pd.main(arg))
            self.assertEqual(0, pd.main(arg + ["--taban-yaz"]))
            self.assertEqual(0, pd.main(arg + ["--ayrinti"]))
            self.assertEqual(2, pd.main(["--kok", str(self.kok / "yok"), "--taban", str(self.taban)]))
            self.taban.write_text("{bozuk", encoding="utf-8")
            self.assertEqual(2, pd.main(arg))
        self.assertIn("Sonuç: TAMAM", cikti.getvalue())
        self.assertIn("/ornek-legal:yok-boyle", cikti.getvalue())


if __name__ == "__main__":
    unittest.main()
