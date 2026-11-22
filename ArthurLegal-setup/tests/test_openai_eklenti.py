"""ChatGPT (OpenAI) eklentisi: ArthurLegal-openai-plugin/ paketten üretilmiş mi, OpenAI'ın biçimine ve 16.11.2026
kararlarına (K6 alan becerileri, K11 /openai/mcp, K24 masayı açma cümlesi, K26 Hafıza) uyuyor mu.

Ağa çıkmaz; gerçek depoyu yalnız okur. Biçim: developers.openai.com/plugins/build/plugins (kökte plugin.json ve
mcp.json, skills/<ad>/SKILL.md) ve build/skills (ad ve açıklama zorunlu, ayrıntı references/ altında).
"""
import json
import re
import sys
import unittest
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "yayin"))
import openai_eklenti_uret as oe  # noqa: E402

AD_KALIBI = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")
ONBILGI = re.compile(r"\A---\nname: ([^\n]+)\ndescription: >-\n  ([^\n]+)\n---\n")


class OpenAIEklentisi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dosyalar = oe.uret()
        cls.metin = {y: v.decode("utf-8") for y, v in cls.dosyalar.items() if not y.endswith(".png")}
        cls.veri = oe.akislar()

    def test_klasor_paketle_ayni(self):
        sorunlar = oe.denetle()
        self.assertEqual(sorunlar, [], "\n".join(sorunlar) + "\nEklentiyi elle değil paketten üretin: "
                         "`python ArthurLegal-setup/yayin/openai_eklenti_uret.py`.")

    def test_bir_kural_ve_on_bir_alan_becerisi(self):
        beceriler = sorted(y.split("/")[1] for y in self.metin if re.fullmatch(r"skills/[^/]+/SKILL\.md", y))
        self.assertEqual(len(beceriler), 12)
        self.assertIn("arthurlegal", beceriler)
        self.assertEqual(set(beceriler) - {"arthurlegal"}, set(oe.KATEGORI_ADI.values()))

    def test_beceri_on_bilgisi_ve_liste_butcesi(self):
        """Ad ve açıklama zorunlu; ChatGPT'nin beceri listesi bütçesi 8.000 karakter (K6)."""
        toplam = 0
        for yol, metin in self.metin.items():
            if not re.fullmatch(r"skills/[^/]+/SKILL\.md", yol):
                continue
            m = ONBILGI.match(metin)
            self.assertIsNotNone(m, yol)
            self.assertEqual(m.group(1), yol.split("/")[1], yol)
            self.assertRegex(m.group(1), AD_KALIBI)
            toplam += len(m.group(2))
        self.assertLess(toplam, 8000)

    def test_her_beceri_bir_alanda_eksiksiz(self):
        """156 beceri: kural becerisi + 122 iş akışı ve 33 yardımcı, hepsi bir alanın references/ klasöründe."""
        dosyalar = [y for y in self.metin if re.fullmatch(r"skills/(?!arthurlegal/)[^/]+/references/[^/]+\.md", y)]
        self.assertEqual(len(dosyalar), 155)
        for a in self.veri["akislar"]:
            yol = "skills/%s/references/%s.md" % (oe.KATEGORI_ADI[a["k"]], a["id"])
            self.assertIn(yol, self.metin, a["id"])
            self.assertIn("`references/%s.md`" % a["id"], self.metin["skills/%s/SKILL.md" % oe.KATEGORI_ADI[a["k"]]])

    def test_claude_izi_yok(self):
        """OpenAI kuralı: becerilerdeki Claude'a özgü göndermeler sağlayıcıdan bağımsız dile çevrilir."""
        for yol, metin in self.metin.items():
            if yol in oe.IZ_SERBEST:
                continue
            self.assertIsNone(oe.IZ.search(metin), yol)

    def test_masa_cumlesi_ve_hafiza_kurali(self):
        kural = self.metin["skills/arthurlegal/SKILL.md"]
        aciklama = ONBILGI.match(kural).group(2)
        self.assertIn("ArthurLegal Masası'nı aç", aciklama)                     # K24
        self.assertIn("al_masasi", aciklama)
        self.assertIn("hafiza_yaz", kural)                                      # K26
        self.assertIn("ChatGPT modelleriyle henüz ölçüm yapmadık", kural)         # K14
        self.assertIn(oe.MCP_URL, kural)
        self.assertTrue(any("Hafıza › Pratik/" in m for m in self.metin.values()))

    def test_manifest_ve_mcp_resmi_bicimde(self):
        m = json.loads(self.metin["plugin.json"])
        self.assertEqual(m["$schema"], oe.SEMA_EKLENTI)
        self.assertEqual(m["name"], "arthurlegal")
        self.assertRegex(m["version"], r"^\d+\.\d+\.\d+$")
        self.assertTrue(m["description"])
        arayuz = m["extensions"]["com.openai"]["interface"]
        self.assertEqual(arayuz["displayName"], "ArthurLegal")
        self.assertNotIn("GPT", json.dumps(arayuz))                            # OpenAI marka kuralı (K16)
        for alan in ("composerIcon", "logo"):
            self.assertTrue(arayuz[alan].startswith("./assets/"))
            self.assertIn(arayuz[alan][2:], self.dosyalar)
        mcp = json.loads(self.metin["mcp.json"])
        self.assertEqual(mcp["$schema"], oe.SEMA_MCP)
        sunucu = mcp["mcpServers"]["arthurlegal"]
        self.assertEqual((sunucu["type"], sunucu["url"]), ("streamable-http", "https://arthurlegal-mcp.fly.dev/openai/mcp"))
        self.assertEqual(sunucu["extensions"]["com.openai"]["auth"], {"type": "none"})
        self.assertNotIn(".claude-plugin/plugin.json", self.dosyalar)

    def test_kural_becerisinin_dosya_yollari_cozulur(self):
        """Yollar becerinin klasörüne göredir: metindeki ../<beceri>/references/... yolları pakette bulunur (eklentide de,
        ~/.codex/skills altına tek tek kurulumda da beceriler kardeş klasördür)."""
        sayi = 0
        for yol, metin in self.metin.items():
            for beceri, dosya in re.findall(r"\.\./([a-z0-9-]+)/references/([\w./-]+\.md)", metin):
                self.assertIn("skills/%s/references/%s" % (beceri, dosya), self.dosyalar, "%s -> %s" % (yol, dosya))
                sayi += 1
            self.assertNotIn("skills/arthurlegal/references/", metin, yol)
        self.assertGreater(sayi, 100)

    def test_alan_becerileri_onekli(self):
        """~/.codex/skills ortak klasördür: alan becerilerinin adı arthurlegal- ile başlar."""
        for ad in oe.KATEGORI_ADI.values():
            self.assertTrue(ad.startswith("arthurlegal-"), ad)

    def test_claude_eklentisi_degismez(self):
        """K6: Claude eklentisi 156 beceriyle kalır; ChatGPT üreticisi onun klasörüne yazmaz."""
        self.assertFalse(any(y.startswith("ArthurLegal-plugin/") for y in self.dosyalar))
        self.assertEqual(oe.CIKTI, "ArthurLegal-openai-plugin")


if __name__ == "__main__":
    unittest.main()
