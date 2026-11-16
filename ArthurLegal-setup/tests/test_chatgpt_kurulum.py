"""ChatGPT masaüstü kurulumu (16.11.2026, Aşama 2): ~/.codex/config.toml yazıcısı, beceri kurulumu, asistan seçimi
(K21), seçimden çıkanın silinmesi (K30), masa bağlantısı ve başlangıç simgesi (K28, K29).

Ağa çıkmaz; ChatGPT'ye dokunmaz. Her şey geçici klasörde (CODEX_HOME, APPDATA, LOCALAPPDATA sahte).

    python -m unittest discover -s tests
"""
import json
import subprocess
import sys
import tempfile
import tomllib
import unittest
import urllib.parse
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "istemci"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import codex_ayari  # noqa: E402
from test_istemci import ENV, SADECE_WINDOWS, sahte_kok  # noqa: E402

KULLANICI = """# kullanıcının kendi ayarları
model = "gpt-5.6-terra"
model_reasoning_effort = "medium"

[projects.'C:\\Users\\x\\proje']
trust_level = "trusted"

[mcp_servers.baskasi]
command = "npx"
args = ["-y", "baska-sunucu"]

[mcp_servers.baskasi.env]
ANAHTAR = "deger"
"""

GIRDI = {"command": r"C:\Users\Ertuğ\AppData\Local\Programs\ArthurLegal\runtime\python.exe",
         "args": ["-B", r"C:\Users\Ertuğ\AppData\Local\Programs\ArthurLegal\bin\al.py", "sunucu"],
         "env": {"PYTHONIOENCODING": "utf-8", "AL_EV": "chatgpt"}, "startup_timeout_sec": 30, "tool_timeout_sec": 120}


class TomlYaziciTesti(unittest.TestCase):
    """Standart kütüphanede TOML yazıcısı yok: yalnız AL'nin tabloları değişir, gerisi bayt bayt kalır."""

    def test_ekler_korur_ve_tekrarda_degismez(self):
        yeni = codex_ayari.uygula(KULLANICI, {"arthurlegal-yerel": GIRDI})
        self.assertTrue(yeni.startswith(KULLANICI.rstrip("\n")), "kullanıcının satırları ve yorumları aynen kalır")
        veri = tomllib.loads(yeni)
        self.assertEqual(veri["model"], "gpt-5.6-terra")
        self.assertEqual(veri["mcp_servers"]["baskasi"]["env"], {"ANAHTAR": "deger"})
        al = veri["mcp_servers"]["arthurlegal-yerel"]
        self.assertEqual((al["command"], al["args"], al["env"]["AL_EV"]), (GIRDI["command"], GIRDI["args"], "chatgpt"))
        self.assertEqual((al["startup_timeout_sec"], al["tool_timeout_sec"]), (30, 120))
        self.assertEqual(codex_ayari.uygula(yeni, {"arthurlegal-yerel": GIRDI}), yeni, "ikinci yazım değişiklik yapmaz")

    def test_kapatilan_sunucu_kapali_kalir_ve_silinir(self):
        kapali = codex_ayari.uygula(KULLANICI, {"arthurlegal-yerel": GIRDI}).replace(
            "tool_timeout_sec = 120\n", "tool_timeout_sec = 120\nenabled = false\n", 1)
        yeniden = codex_ayari.uygula(kapali, {"arthurlegal-yerel": {**GIRDI, "tool_timeout_sec": 90}})
        self.assertIs(tomllib.loads(yeniden)["mcp_servers"]["arthurlegal-yerel"]["enabled"], False,
                      "kullanıcının ChatGPT'de kapattığı sunucu güncellemeyle açılmaz")
        silinmis = codex_ayari.uygula(yeniden, {}, codex_ayari.ADLAR)
        self.assertNotIn("arthurlegal-yerel", tomllib.loads(silinmis)["mcp_servers"])
        self.assertEqual(silinmis, KULLANICI, "kaldırınca dosya eski hâline döner")

    def test_silinecek_yoksa_dosyaya_dokunulmaz(self):
        tuhaf = KULLANICI + "\n\n\n"   # sondaki boş satırlar bile korunur
        self.assertEqual(codex_ayari.uygula(tuhaf, {}, codex_ayari.ADLAR), tuhaf)
        self.assertEqual(codex_ayari.uygula("", {}, codex_ayari.ADLAR), "")

    def test_tirnakli_baslik_satir_sonu_ve_kesme_isareti(self):
        """Başka bir araç başlığı tırnaklı yazmış olabilir; Windows dosyası CRLF olabilir; yolda kesme işareti olabilir."""
        eski = KULLANICI.replace("\n", "\r\n") + "\r\n[mcp_servers.\"arthurlegal-yerel\"]\r\ncommand = \"eski\"\r\n" \
            "\r\n[mcp_servers.\"arthurlegal-yerel\".env]\r\nX = \"1\"\r\n"
        girdi = {**GIRDI, "command": r"C:\Users\O'Brien\py.exe"}
        yeni = codex_ayari.uygula(eski, {"arthurlegal-yerel": girdi})
        self.assertNotIn("eski", yeni)
        self.assertNotIn("\n", yeni.replace("\r\n", ""), "satır sonları dosyanınkiyle aynı (CRLF)")
        al = tomllib.loads(yeni)["mcp_servers"]["arthurlegal-yerel"]
        self.assertEqual(al["command"], r"C:\Users\O'Brien\py.exe")
        self.assertNotIn("X", al["env"])

    def test_dizi_tablosu_ve_ic_ice_anahtar_bozulmaz(self):
        metin = KULLANICI + "\n[[hooks]]\nad = \"a\"\n\n[mcp_servers]\nvarsayilan = 1\n"
        yeni = codex_ayari.uygula(metin, {"arthur-tapu": GIRDI})
        veri = tomllib.loads(yeni)
        self.assertEqual(veri["hooks"], [{"ad": "a"}])
        self.assertEqual(veri["mcp_servers"]["varsayilan"], 1)
        self.assertIn("arthur-tapu", veri["mcp_servers"])


class _Ortam:
    def calistir(self, t, kod):
        tam = f"import sys, json; sys.path.insert(0, r'{t / 'kok'}/surumler/0.0.1/istemci'); {kod}"
        env = {**ENV, "APPDATA": str(t / "Roaming"), "LOCALAPPDATA": str(t / "Local"), "USERPROFILE": str(t / "ev"),
               "HOME": str(t / "ev"), "CODEX_HOME": str(t / "codex"), "ARTHURLEGAL_PROJE_KOKU": str(t / "projeler")}
        r = subprocess.run([sys.executable, "-c", tam], env=env, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout.strip().splitlines()[-1])

    @staticmethod
    def beceri(kok: Path, ad: str, metin="---\nname: x\ndescription: >-\n  y\n---\n"):
        (kok / ad / "references").mkdir(parents=True, exist_ok=True)
        (kok / ad / "SKILL.md").write_text(metin, encoding="utf-8")
        (kok / ad / "references" / "a.md").write_text("a", encoding="utf-8")


@SADECE_WINDOWS
class CodexAyariTesti(_Ortam, unittest.TestCase):
    def test_kaydeder_yedekler_kaldirir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            yapi = t / "codex" / "config.toml"
            yapi.parent.mkdir()
            yapi.write_text(KULLANICI, encoding="utf-8")
            kaydet = "import codex_ayari; print(json.dumps([str(y) for y in codex_ayari.kaydet()]))"
            self.assertEqual(len(self.calistir(t, kaydet)), 1)
            veri = tomllib.loads(yapi.read_text(encoding="utf-8"))
            self.assertEqual(set(veri["mcp_servers"]), {"baskasi", "arthurlegal-yerel", "arthur-tapu"})
            yerel = veri["mcp_servers"]["arthurlegal-yerel"]
            self.assertEqual(yerel["env"]["AL_EV"], "chatgpt", "yerel sunucu ChatGPT kipinde açılır")
            self.assertEqual(yerel["args"][-1], "sunucu")
            self.assertGreater(yerel["tool_timeout_sec"], 60, "uzun işler ChatGPT'nin 60 sn varsayılanını aşabilir")
            self.assertNotIn("AL_EV", veri["mcp_servers"]["arthur-tapu"]["env"])
            self.assertEqual(len(list(yapi.parent.glob("config.toml.arthurlegal-yedek-*"))), 1)
            self.assertEqual(self.calistir(t, kaydet), [], "ikinci kayıt değişiklik yapmaz")
            # ArthurMask kuruluysa köprüsü ChatGPT'ye de yazılır (Mask'in kendi kurulumu yalnız Claude'a yazar).
            mask = t / "Local" / "Programs" / "Arthur Mask" / "runtime"
            mask.mkdir(parents=True)
            (mask / "python.exe").write_bytes(b"")
            self.calistir(t, kaydet)
            m = tomllib.loads(yapi.read_text(encoding="utf-8"))["mcp_servers"]["arthur-mask"]
            self.assertEqual(m["command"], str(mask / "python.exe"))
            self.assertEqual(m["args"], ["-c", codex_ayari.MASK_KOPRU])
            self.assertEqual(m["env"]["HF_HUB_OFFLINE"], "1")
            self.assertEqual(self.calistir(t, "import codex_ayari; print(json.dumps(codex_ayari.kayitli()))"),
                             ["arthur-mask", "arthur-tapu", "arthurlegal-yerel", "baskasi"])
            self.calistir(t, "import codex_ayari; print(json.dumps([str(y) for y in codex_ayari.sil()]))")
            self.assertEqual(yapi.read_text(encoding="utf-8"), KULLANICI, "kaldırınca kullanıcının dosyası aynen kalır")

    def test_bozuk_dosyaya_dokunulmaz(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            yapi = t / "codex" / "config.toml"
            yapi.parent.mkdir()
            yapi.write_text("model = \n[[[", encoding="utf-8")
            self.assertEqual(self.calistir(t, "import codex_ayari; print(json.dumps([str(y) for y in codex_ayari.kaydet()]))"), [])
            self.assertEqual(yapi.read_text(encoding="utf-8"), "model = \n[[[")

    def test_beceriler_kurulur_tazelenir_ve_yalniz_bizimkiler_silinir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            kaynak = t / "kok" / "surumler" / "0.0.1" / "chatgpt" / "skills"
            for ad in ("arthurlegal", "arthurlegal-vergi"):
                self.beceri(kaynak, ad)
            self.beceri(t / "codex" / "skills", "benim-becerim")
            kur = "import codex_ayari; print(json.dumps(codex_ayari.beceriler_kur()))"
            self.assertEqual(self.calistir(t, kur), ["arthurlegal", "arthurlegal-vergi"])
            hedef = t / "codex" / "skills"
            self.assertTrue((hedef / "arthurlegal-vergi" / "references" / "a.md").exists())
            (kaynak / "arthurlegal" / "SKILL.md").write_text("yeni", encoding="utf-8")
            import shutil
            shutil.rmtree(kaynak / "arthurlegal-vergi")
            self.assertEqual(self.calistir(t, kur), ["arthurlegal"])
            self.assertEqual((hedef / "arthurlegal" / "SKILL.md").read_text(encoding="utf-8"), "yeni")
            self.assertFalse((hedef / "arthurlegal-vergi").exists(), "paketten çıkan beceri kaldırılır")
            self.assertEqual(self.calistir(t, "import codex_ayari; print(json.dumps(codex_ayari.beceriler_sil()))"),
                             ["arthurlegal"])
            self.assertEqual(sorted(p.name for p in hedef.iterdir()), ["benim-becerim"],
                             "kullanıcının kendi becerisine dokunulmaz")


@SADECE_WINDOWS
class AsistanSecimiTesti(_Ortam, unittest.TestCase):
    """K21 seçim ekranı, K30 seçimden çıkan uygulamadan ArthurLegal'in silinmesi (yalnız seçim açıkça yapıldıysa)."""

    def hazirla(self, t):
        sahte_kok(t / "kok")
        msix = t / "Local" / "Packages" / "Claude_abc" / "LocalCache" / "Roaming" / "Claude"
        msix.mkdir(parents=True)
        (msix / "claude_desktop_config.json").write_text(json.dumps({"mcpServers": {}}), encoding="utf-8")
        (t / "codex").mkdir()
        (t / "codex" / "config.toml").write_text(KULLANICI, encoding="utf-8")
        self.beceri(t / "kok" / "surumler" / "0.0.1" / "chatgpt" / "skills", "arthurlegal")
        return msix / "claude_desktop_config.json", t / "codex" / "config.toml"

    DURUM = ("import kur, ortak, claude_ayari, codex_ayari; kur.main(['--kaydet'] + {arg}); "
             "print(json.dumps([ortak.asistanlar(), sorted(s for a in claude_ayari.kayitli().values() for s in a), "
             "codex_ayari.kayitli(), codex_ayari.beceriler_kayitli()]))")

    def test_secim_kaydedilir_ve_cikan_silinir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            claude, codex = self.hazirla(t)
            secim, cl, cg, bec = self.calistir(t, self.DURUM.format(arg="[]"))
            self.assertEqual(secim, ["claude"], "seçim yoksa önceki kurulumlar gibi yalnız Claude")
            self.assertIn("arthurlegal-yerel", cl)
            self.assertEqual((cg, bec), (["baskasi"], []), "seçilmeyen ChatGPT'ye bir şey yazılmaz")
            secim, cl, cg, bec = self.calistir(t, self.DURUM.format(arg="['--asistan', 'ikisi']"))
            self.assertEqual(secim, ["claude", "chatgpt"])
            self.assertIn("arthurlegal-yerel", cl)
            self.assertIn("arthurlegal-yerel", cg)
            self.assertEqual(bec, ["arthurlegal"])
            secim, cl, cg, bec = self.calistir(t, self.DURUM.format(arg="['--asistan', 'chatgpt']"))
            self.assertEqual(secim, ["chatgpt"])
            self.assertFalse([s for s in cl if s.startswith("arthurlegal")], "seçimden çıkan Claude'dan silinir (K30)")
            self.assertIn("arthurlegal-yerel", cg)
            self.assertEqual(self.calistir(t, self.DURUM.format(arg="[]"))[0], ["chatgpt"],
                             "güncelleyicinin --kaydet'i seçimi korur")
            secim, cl, cg, bec = self.calistir(t, self.DURUM.format(arg="['--asistan', 'claude']"))
            self.assertEqual((cg, bec), (["baskasi"], []), "ChatGPT'den sunucular ve beceriler silinir")
            self.assertEqual(codex.read_text(encoding="utf-8"), KULLANICI)

    def test_secim_yapilmamissa_elle_yazilan_chatgpt_ayari_korunur(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            _, codex = self.hazirla(t)
            elle = KULLANICI + "\n[mcp_servers.arthurlegal-yerel]\ncommand = \"elle\"\nargs = []\n"
            codex.write_text(elle, encoding="utf-8")
            self.calistir(t, self.DURUM.format(arg="[]"))
            self.assertEqual(codex.read_text(encoding="utf-8"), elle)

    def test_kaldirma_iki_uygulamadan_da_siler(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            claude, codex = self.hazirla(t)
            self.calistir(t, self.DURUM.format(arg="['--asistan', 'ikisi']"))
            kod = ("import kur, claude_ayari, codex_ayari; kur.kisayollar_sil = lambda: None; kur.run_anahtari = "
                   "lambda y: None; kur.main(['--kaldir']); print(json.dumps([sorted(s for a in claude_ayari.kayitli()"
                   ".values() for s in a), codex_ayari.kayitli(), codex_ayari.beceriler_kayitli()]))")
            cl, cg, bec = self.calistir(t, kod)
            self.assertEqual((cl, cg, bec), ([], ["baskasi"], []))
            self.assertEqual(codex.read_text(encoding="utf-8"), KULLANICI)


@SADECE_WINDOWS
class ChatGPTSimgesiTesti(_Ortam, unittest.TestCase):
    """Ana simge: ChatGPT seçildiyse masa ChatGPT'de (codex://new?prompt=…, K24), kurulu değilse resmî indirme sayfası
    (K28), ikisi seçildiyse yalnız başlangıç paneli ve orada iki düğme (K29)."""

    BASLAT = ("import kisayol, ortak, webbrowser; acilan = []; webbrowser.open = lambda u: acilan.append("
              "'indirme' if u == ortak.CHATGPT_INDIRME else 'rehber'); kisayol._ac = lambda a: acilan.append("
              "a.split(':', 1)[0]) or 0; kisayol.claude_ac = lambda: 'açık'; ortak.chatgpt_calisiyor = lambda: False; "
              "ortak.durum_guncelle(asistan='{secim}'); kisayol.baslat(); "
              "d = json.loads((ortak.KOK / 'rehber' / 'durum.js').read_text(encoding='utf-8').split('=', 1)[1].rstrip().rstrip(';')); "
              "print(json.dumps([acilan, d['asistanlar'], d['chatgpt'], bool(d['masa_claude']), bool(d['masa_chatgpt'])]))")

    def test_masa_baglantisi(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            adres = self.calistir(t, "import kisayol; print(json.dumps(kisayol.chatgpt_masa_adresi()))")
            self.assertTrue(adres.startswith("codex://new?prompt=ArthurLegal%20Masas%C4%B1%27n%C4%B1%20a%C3%A7"))
            mesaj = urllib.parse.unquote(adres.split("?prompt=", 1)[1])
            oneri = json.loads((BURASI / "istemci" / "arayuz" / "ortak" / "tasarim" / "model-onerisi.json")
                               .read_text(encoding="utf-8"))
            self.assertIn(oneri["cumle_chatgpt"], mesaj, "K14 cümlesi aynen")
            self.assertNotIn("Opus", mesaj)
            self.assertLess(len(adres), 2000)

    def test_secime_gore_acilis(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            acilan, secim, durum, mc, mg = self.calistir(t, self.BASLAT.format(secim="chatgpt"))
            self.assertEqual((acilan, secim, durum, mc, mg), (["indirme", "rehber"], ["chatgpt"], "bulunamadı", False, True),
                             "ChatGPT kurulu değilse resmî indirme sayfası ve panel")
            (t / "Local" / "Packages" / "OpenAI.Codex_2p2nqsd0c76g0").mkdir(parents=True)
            acilan, _, durum, _, _ = self.calistir(t, self.BASLAT.format(secim="chatgpt"))
            self.assertEqual((acilan, durum), (["codex", "rehber"], "kurulu"))
            acilan, secim, _, mc, mg = self.calistir(t, self.BASLAT.format(secim="ikisi"))
            self.assertEqual((acilan, secim, mc, mg), (["rehber"], ["claude", "chatgpt"], True, True),
                             "ikisi seçildiyse yalnız panel; masa düğmeleri orada")
            acilan, secim, durum, mc, mg = self.calistir(t, self.BASLAT.format(secim="claude"))
            self.assertEqual((acilan, durum, mc, mg), (["claude", "rehber"], "", True, False))

    def test_kisayol_aciklamasi_ve_proje_klasoru(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            kod = ("import kur, ortak; ortak.durum_guncelle(asistan='{secim}'); print(json.dumps("
                   "[[y.name, a] for y, h, _, a in kur._kisayol_listesi()]))")
            claude = dict(self.calistir(t, kod.format(secim="claude")))
            self.assertEqual(claude["ArthurLegal 0.0.1.lnk"], "Claude Desktop'ı ve başlangıç panelini açar (0.0.1)")
            self.assertTrue(any("Proje" in a for a in claude))
            chatgpt = dict(self.calistir(t, kod.format(secim="chatgpt")))
            self.assertEqual(chatgpt["ArthurLegal 0.0.1.lnk"], "ChatGPT'yi ve başlangıç panelini açar (0.0.1)")
            self.assertFalse(any("Proje" in a for a in chatgpt), "'Use a folder' Claude'undur")
            ikisi = dict(self.calistir(t, kod.format(secim="ikisi")))
            self.assertIn("Claude Desktop'ta ya da ChatGPT'de", ikisi["ArthurLegal 0.0.1.lnk"])


class KurulumMetniTesti(unittest.TestCase):
    def test_uc_dilde_her_secim(self):
        import kur
        for sozluk in (kur.ACILIS_METNI, kur.UYAP_SIZ, kur.UYGULAMA_ADI):
            self.assertEqual(set(sozluk), {"tr", "en", "az"})
            for dil, metinler in sozluk.items():
                self.assertEqual(set(metinler), {"claude", "chatgpt", "ikisi"}, dil)
        for dil, m in kur.KISAYOL_METNI.items():
            self.assertNotIn("Claude", m["ana"] + m["adliye_aciklama"] + m["akademisyen_aciklama"] + m["uyap"], dil)


if __name__ == "__main__":
    unittest.main()
