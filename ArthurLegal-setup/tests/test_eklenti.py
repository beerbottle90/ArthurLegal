"""Claude eklentisi: ArthurLegal-plugin/ paketten üretilmiş mi ve Anthropic dizininin otomatik kurallarına uyuyor mu.

Ağa çıkmaz; gerçek depoyu yalnız okur. Kurallar dizinin plugin pre-submission checklist'inden: README en az 40 kelime,
lisans, dosya başına 256 KiB, en çok 512 dosya, yalnız metin ve PNG, https uzak bağlantı, geçerli beceri ön bilgisi.
"""
import json
import re
import sys
import unittest
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "yayin"))
import eklenti_uret  # noqa: E402

AD_KALIBI = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")


class EklentiKlasoru(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dosyalar = eklenti_uret.uret()

    def test_klasor_paketle_ayni(self):
        sorunlar = eklenti_uret.denetle()
        self.assertEqual(sorunlar, [], "\n".join(sorunlar) + "\nEklentiyi elle değil paketten üretin: "
                         "`python ArthurLegal-setup/yayin/eklenti_uret.py`.")

    def test_dizin_dosya_kurallari(self):
        self.assertLessEqual(len(self.dosyalar), 512)
        for yol, veri in self.dosyalar.items():
            if not yol.endswith(".png"):
                self.assertLess(len(veri), 256 * 1024, yol)
            self.assertTrue(yol.endswith((".md", ".json", ".png", ".txt")) or yol == "LICENSE", yol)
        self.assertEqual(len({y.lower() for y in self.dosyalar}), len(self.dosyalar))
        readme = self.dosyalar["README.md"].decode("utf-8")
        self.assertGreaterEqual(len(re.sub(r"```.*?```", "", readme, flags=re.S).split()), 40)
        self.assertIn("LICENSE", self.dosyalar)

    def test_manifest_ve_baglanti(self):
        manifest = json.loads(self.dosyalar[".claude-plugin/plugin.json"])
        self.assertRegex(manifest["name"], AD_KALIBI)
        for alan in ("description", "author", "version"):
            self.assertTrue(manifest.get(alan), alan)
        self.assertIn(manifest["icon"].lstrip("./"), self.dosyalar)
        sunucular = json.loads(self.dosyalar[".mcp.json"])["mcpServers"]
        self.assertEqual(list(sunucular), [eklenti_uret.AD])
        self.assertEqual(sunucular[eklenti_uret.AD]["type"], "http")
        self.assertTrue(sunucular[eklenti_uret.AD]["url"].startswith("https://"))

    def test_beceriler(self):
        beceriler = {y.split("/")[1]: v.decode("utf-8") for y, v in self.dosyalar.items()
                     if y.startswith("skills/") and y.endswith("/SKILL.md")}
        self.assertIn(eklenti_uret.AD, beceriler)
        for ad, metin in beceriler.items():
            self.assertRegex(ad, AD_KALIBI)
            m = re.match(r"---\n(.*?)\n---\n", metin, re.S)
            self.assertTrue(m, ad)
            self.assertRegex(m.group(1), r"(?m)^name: %s$" % re.escape(ad))
            self.assertRegex(m.group(1), r"(?m)^description:", ad)
            for hedef in re.findall(r"/%s:([a-z0-9-]+)" % eklenti_uret.AD, metin):
                self.assertIn(hedef, beceriler, "%s içinde kırık atıf: /%s:%s" % (ad, eklenti_uret.AD, hedef))
            for rehber in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/(references/[\w./-]+\.md)", metin):
                self.assertIn(rehber, self.dosyalar, "%s içinde olmayan rehber: %s" % (ad, rehber))

    def test_kullanici_anahtari_istenmez(self):
        # Dizin, kullanıcının makinesindeki anahtarı okuyup dışarı gönderen talimatı bekletir (MCP_FORWARDS_CREDENTIAL_ENV).
        for yol, veri in self.dosyalar.items():
            if yol.endswith(".png"):
                continue
            metin = veri.decode("utf-8")
            kalan = set(eklenti_uret.KIMLIK.findall(metin)) - eklenti_uret.SERBEST_KIMLIK
            self.assertEqual(kalan, set(), yol)
            self.assertNotRegex(metin, r"\b[0-9a-f]{32}\b", yol)
        for rehber in eklenti_uret.ANAHTARLI_REHBER:
            self.assertNotIn("references/" + rehber, self.dosyalar)

    def test_yerel_moduller_eklentiye_girmez(self):
        # Tapu, UYAP ve Mask kullanıcının bilgisayarında çalışır; eklenti yalnız onlara yönlendirir.
        ana = self.dosyalar["skills/%s/SKILL.md" % eklenti_uret.AD].decode("utf-8")
        for arac in ("arthur-tapu", "arthur-uyap", "Arthur Mask"):
            self.assertIn(arac, ana)
        self.assertFalse([y for y in self.dosyalar if y.startswith(("bin/", "hooks/", "agents/", "scripts/"))])


if __name__ == "__main__":
    unittest.main()
