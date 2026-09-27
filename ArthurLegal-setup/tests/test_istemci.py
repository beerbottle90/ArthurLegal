"""İstemci testleri: Ed25519, Claude yapılandırması, yerel MCP sunucusu (sahte uzak sunucuyla)
ve güncelleyici (sahte GitHub yayınıyla). Ağa çıkmaz; her şey 127.0.0.1'de ve geçici klasörde.

    python -m unittest discover -s tests
"""
import http.server
import json
import os
import queue
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
import zipfile
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BURASI / "istemci"))
import ed25519  # noqa: E402

TEST_TOHUM = bytes(range(32))
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8", "ARTHURLEGAL_GUNCELLEME": "0"}
ENV.pop("ARTHURLEGAL_KOK", None)

BECERILER = """# commercial-legal - Skill Referans Kitapcigi
## Icindekiler
- /commercial-legal:nda-review
## /commercial-legal:nda-review
# /nda-review
## Instructions
NDA incelemesi adımları. Gizlilik süresi.
## /commercial-legal:renewal
# /renewal
Yenileme adımları.
"""


def sahte_kok(kok: Path, surum="0.0.1", uzak="http://127.0.0.1:9/mcp", manifest="http://127.0.0.1:9/m.json"):
    (kok / "bin").mkdir(parents=True)
    shutil.copy2(BURASI / "bin" / "al.py", kok / "bin" / "al.py")
    s = kok / "surumler" / surum
    paket_yaz(s, surum)
    p = s / "paketler" / "hukuk-burosu"
    (p / "knowledge" / "skills").mkdir(parents=True)
    (p / "knowledge" / "references").mkdir(parents=True)
    (p / "SYSTEM_PROMPT.md").write_text("# SİSTEM\nArthurLegal Hukuk Bürosu talimatı.", encoding="utf-8")
    (p / "VERSION.md").write_text("1.9.0", encoding="utf-8")
    (p / "knowledge" / "firm-profile.md").write_text("# Büro Profili — [BÜRO_ADI]\n[DOLDUR]", encoding="utf-8")
    (p / "knowledge" / "skills" / "commercial-legal__skills.md").write_text(BECERILER, encoding="utf-8")
    (p / "knowledge" / "references" / "hmk-rehberi.md").write_text("# HMK\nIslah HMK m. 176.\nİstinaf süresi iki hafta.", encoding="utf-8")
    (s / "icerik.json").write_text(json.dumps({"paketler": {"hukuk-burosu": "1.9.1"}}), encoding="utf-8")
    f = kok / "firma"
    (f / "knowledge").mkdir(parents=True)
    (f / "buro").mkdir()
    (f / "firma.json").write_text(json.dumps({"kod": "t", "ad": "Test & Ortakları"}), encoding="utf-8")
    (f / "knowledge" / "firm-profile.md").write_text("# Büro Profili — Test & Ortakları", encoding="utf-8")
    (f / "buro" / "ek-3-kirmizi-hatlar.md").write_text("# Kırmızı hatlar", encoding="utf-8")
    (kok / "ayar.json").write_text(json.dumps({"uzak_mcp": uzak, "manifest_url": manifest, "api_url": "",
                                               "yayin_anahtari": ed25519.public_key(TEST_TOHUM).hex()}), encoding="utf-8")


def paket_yaz(s: Path, surum: str):
    (s / "istemci").mkdir(parents=True)
    for y in (BURASI / "istemci").glob("*.py"):
        shutil.copy2(y, s / "istemci" / y.name)
    (s / "surum.txt").write_text(surum, encoding="utf-8")


def sunucu_baslat(isleyici):
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), isleyici)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}"


class SahteUzak(http.server.BaseHTTPRequestHandler):
    """ArthurLegal MCP taklidi: oturum başlığı verir, tools/call'a SSE ile cevap verir."""
    def log_message(self, *a):
        pass

    def do_POST(self):
        m = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if "id" not in m:
            self.send_response(202)
            self.end_headers()
            return
        if m["method"] == "initialize":
            sonuc = {"protocolVersion": "2025-06-18", "capabilities": {"tools": {}}, "serverInfo": {"name": "sahte"}}
        elif m["method"] == "tools/list":
            sonuc = {"tools": [{"name": n, "description": n, "inputSchema": {"type": "object"}}
                               for n in ("status", "tr_ictihat_ara", "tkgm_tapu_kaydi_oku")]}
        else:
            if self.headers.get("Mcp-Session-Id") != "oturum-1":
                self.send_response(404)
                self.end_headers()
                return
            metin = json.dumps(m["params"], ensure_ascii=False)
            govde = f"event: message\ndata: {json.dumps({'jsonrpc': '2.0', 'id': m['id'], 'result': {'content': [{'type': 'text', 'text': metin}]}})}\n\n"
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()
            self.wfile.write(govde.encode("utf-8"))
            return
        ham = json.dumps({"jsonrpc": "2.0", "id": m["id"], "result": sonuc}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Mcp-Session-Id", "oturum-1")
        self.send_header("Content-Length", str(len(ham)))
        self.end_headers()
        self.wfile.write(ham)


class Ed25519Testi(unittest.TestCase):
    def test_rfc8032_vektoru(self):
        sk = bytes.fromhex("9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60")
        self.assertEqual(ed25519.public_key(sk).hex(), "d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a")
        imza = ed25519.sign(sk, b"")
        self.assertTrue(imza.hex().startswith("e5564300c360ac72"))
        self.assertTrue(ed25519.verify(ed25519.public_key(sk), b"", imza))
        self.assertFalse(ed25519.verify(ed25519.public_key(sk), b"x", imza))
        self.assertFalse(ed25519.verify(ed25519.public_key(sk), b"", imza[:-1] + bytes([imza[-1] ^ 1])))


class BuroSimgesiTesti(unittest.TestCase):
    """derle.py: büronun simgesi ArthurLegal simgesinin yerini alır; bozuk dosya almaz."""

    def setUp(self):
        sys.path.insert(0, str(BURASI / "yayin"))
        import derle
        self.derle = derle
        self.kok = Path(tempfile.mkdtemp())
        (self.kok / "bin").mkdir()
        (self.kok / "bin" / "arthurlegal.ico").write_bytes(b"\x00\x00\x01\x00arthurlegal")
        (self.kok / "firma" / "marka").mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(self.kok, ignore_errors=True)

    def test_buro_simgesi_yerine_gecer(self):
        (self.kok / "firma" / "marka" / "simge.ico").write_bytes(b"\x00\x00\x01\x00buro")
        ad = self.derle.buro_simgesi(self.kok / "firma", self.kok / "bin")
        self.assertRegex(ad, r"^buro-[0-9a-f]{8}\.ico$", "ad içeriğin özetini taşır: Windows simge önbelleği")
        self.assertEqual((self.kok / "bin" / "arthurlegal.ico").read_bytes(), b"\x00\x00\x01\x00buro")
        self.assertEqual((self.kok / "bin" / ad).read_bytes(), b"\x00\x00\x01\x00buro")
        (self.kok / "firma" / "marka" / "simge.ico").write_bytes(b"\x00\x00\x01\x00yeni")
        self.assertNotEqual(self.derle.buro_simgesi(self.kok / "firma", self.kok / "bin"), ad, "yeni simge yeni ad")

    def test_simge_yoksa_ya_da_ico_degilse_dokunulmaz(self):
        self.assertFalse(self.derle.buro_simgesi(self.kok / "firma", self.kok / "bin"))
        (self.kok / "firma" / "marka" / "simge.ico").write_bytes(b"\x89PNG")
        self.assertFalse(self.derle.buro_simgesi(self.kok / "firma", self.kok / "bin"))
        self.assertEqual((self.kok / "bin" / "arthurlegal.ico").read_bytes(), b"\x00\x00\x01\x00arthurlegal")
        self.assertEqual(sorted(p.name for p in (self.kok / "bin").iterdir()), ["arthurlegal.ico"])

    def test_baslangic_sayfasi_urun_adiyla(self):
        icerik = {"surum": "0.0.1", "paketler": {}}
        self.derle.rehber_yaz(self.kok, "Örnek Büro", icerik, "Örnek Büro Asistanı")
        sayfa = (self.kok / "rehber" / "baslangic.html").read_text(encoding="utf-8")
        self.assertIn("<title>Örnek Büro Asistanı Başlangıç</title>", sayfa)
        self.assertIn("<i>Örnek Büro Asistanı - Tapu</i>", sayfa)
        self.assertNotIn("{{", sayfa)
        self.derle.rehber_yaz(self.kok, "", icerik)
        self.assertIn("<title>ArthurLegal Başlangıç</title>",
                      (self.kok / "rehber" / "baslangic.html").read_text(encoding="utf-8"))


class KurulumBetigiTesti(unittest.TestCase):
    """Üzerine kurulum: kısayollar kurulan sürümün koduyla yazılır, Başlat menüsü klasörü ürün adından gelir."""

    def test_uzerine_kurulum_yeni_kodla_ve_yeni_klasorle(self):
        iss = (BURASI / "kurulum" / "ArthurLegal.iss").read_text(encoding="utf-8-sig")
        self.assertIn("UsePreviousGroup=no", iss, "Inno önceki kurulumun menü klasörünü yeniden kullanırdı")
        sil, kur = iss.find(r"DeleteFile(ExpandConstant('{app}\aktif.txt'))"), iss.find("kur --kurulum --kisayol")
        self.assertTrue(0 < sil < kur, "al.py aktif.txt'deki eski sürümü seçerdi; önce silinmeli")
        # Kaldırma kısayolunun adı kur._kaldir_adi ile aynı olmalı.
        self.assertIn('#define KaldirAdi "ArthurLegal\'i Kaldır"', iss)
        self.assertIn('#define KaldirAdi UrunAd + " - Kaldır"', iss)

    def test_aktif_yoksa_en_yeni_surum(self):
        """Kurulumun dayandığı kural: aktif.txt silinince al.py en yeni sürüm klasörünü seçer."""
        with tempfile.TemporaryDirectory() as t:
            kok = Path(t) / "kok"
            sahte_kok(kok, surum="0.0.1")
            paket_yaz(kok / "surumler" / "0.0.2", "0.0.2")
            (kok / "aktif.txt").write_text("0.0.1", encoding="utf-8")
            kod = f"import runpy; print(runpy.run_path(r'{kok / 'bin' / 'al.py'}')['etkin_dizin']())"
            secilen = lambda: Path(subprocess.run([sys.executable, "-c", kod], env=ENV, capture_output=True,  # noqa: E731
                                                  text=True, check=True).stdout.strip()).name
            self.assertEqual(secilen(), "0.0.1")
            (kok / "aktif.txt").unlink()
            self.assertEqual(secilen(), "0.0.2")


class ClaudeAyariTesti(unittest.TestCase):
    def calistir(self, komut, kok, appdata, yerel):
        kod = f"import sys; sys.path.insert(0, r'{kok}/surumler/0.0.1/istemci'); import claude_ayari, json; print(json.dumps([str(y) for y in claude_ayari.{komut}()]))"
        env = {**ENV, "APPDATA": str(appdata), "LOCALAPPDATA": str(yerel)}
        return json.loads(subprocess.run([sys.executable, "-c", kod], env=env, capture_output=True, text=True, encoding="utf-8", check=True).stdout)

    def test_birlestirir_yedekler_kaldirir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            appdata, yerel = t / "Roaming", t / "Local"
            msix = yerel / "Packages" / "Claude_abc" / "LocalCache" / "Roaming" / "Claude"
            msix.mkdir(parents=True)
            yapi = msix / "claude_desktop_config.json"
            yapi.write_text(json.dumps({"preferences": {"x": 1}, "mcpServers": {"arthur-mask": {"command": "m"}}}), encoding="utf-8")
            self.assertEqual(len(self.calistir("kaydet", t / "kok", appdata, yerel)), 1)
            veri = json.loads(yapi.read_text(encoding="utf-8"))
            self.assertEqual(veri["preferences"], {"x": 1})
            self.assertEqual(set(veri["mcpServers"]), {"arthur-mask", "arthurlegal-yerel", "arthur-tapu"})
            self.assertFalse((appdata / "Claude").exists(), "klasik yol yokken MSIX varsa klasik oluşturulmamalı")
            self.assertEqual(len(list(msix.glob("claude_desktop_config.arthurlegal-yedek-*.json"))), 1)
            self.assertEqual(self.calistir("kaydet", t / "kok", appdata, yerel), [], "ikinci kayıt değişiklik yapmamalı")
            mask = yerel / "Programs" / "Arthur Mask" / "runtime"
            mask.mkdir(parents=True)
            (mask / "python.exe").write_bytes(b"")
            self.calistir("kaydet", t / "kok", appdata, yerel)
            self.assertNotIn("arthur-uyap", json.loads(yapi.read_text(encoding="utf-8"))["mcpServers"],
                             "UYAP bu kurulumda yokken kaydedilmemeli")
            (t / "kok" / "surumler" / "0.0.1" / "uyap").mkdir()
            (t / "kok" / "surumler" / "0.0.1" / "uyap" / "server.py").write_text("", encoding="utf-8")
            self.calistir("kaydet", t / "kok", appdata, yerel)
            uyap = json.loads(yapi.read_text(encoding="utf-8"))["mcpServers"]["arthur-uyap"]
            self.assertEqual(uyap["command"], str(mask / "python.exe"))
            self.assertEqual(uyap["args"][-1], "uyap")
            self.calistir("sil", t / "kok", appdata, yerel)
            veri = json.loads(yapi.read_text(encoding="utf-8"))
            self.assertEqual(set(veri["mcpServers"]), {"arthur-mask"})
            self.assertEqual(veri["preferences"], {"x": 1})


class KisayolTesti(unittest.TestCase):
    """UYAP için tek simge (UYAP Dashboard) yalnız köprü ve Arthur Mask birlikteyse; Mask'in Python'unda açılır."""

    LISTE = "import kur; print(json.dumps([[y.name, str(h), a] for y, h, a, _ in kur._kisayol_listesi()]))"
    AC = ("import kisayol, ortak; k = []; ortak.arka_planda = lambda a, o=None: k.append([[str(x) for x in a], "
          "{d: o.get(d) for d in ('HF_HUB_OFFLINE', 'PYTHONNOUSERSITE')}]); print(json.dumps([kisayol.uyap_ekran(), k]))")

    def calistir(self, t, kod):
        tam = f"import sys, json; sys.path.insert(0, r'{t / 'kok'}/surumler/0.0.1/istemci'); {kod}"
        env = {**ENV, "APPDATA": str(t / "Roaming"), "LOCALAPPDATA": str(t / "Local"), "USERPROFILE": str(t / "ev"),
               "ARTHURLEGAL_PROJE_KOKU": str(t / "projeler")}
        cikti = subprocess.run([sys.executable, "-c", tam], env=env, capture_output=True, text=True,
                               encoding="utf-8", check=True).stdout
        return json.loads(cikti.strip().splitlines()[-1])       # işleyicinin uyarı satırından sonra

    def test_ekran_kisayolu_ve_acilisi(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            uyap = t / "kok" / "surumler" / "0.0.1" / "uyap"
            uyap.mkdir()
            (uyap / "ekran.py").write_text("", encoding="utf-8")
            adlar = [s[0] for s in self.calistir(t, self.LISTE)]
            self.assertFalse([a for a in adlar if "UYAP" in a], "Arthur Mask yokken UYAP simgesi yok")
            self.assertEqual(self.calistir(t, self.AC), [1, []])
            mask = t / "Local" / "Programs" / "Arthur Mask" / "runtime"
            mask.mkdir(parents=True)
            for ad in ("python.exe", "pythonw.exe"):
                (mask / ad).write_bytes(b"")
            liste = self.calistir(t, self.LISTE)
            ekran = [s for s in liste if s[0] == "ArthurLegal - UYAP Dashboard 0.0.1.lnk"]
            self.assertEqual(len(ekran), 2, "masaüstü ve Başlat menüsü")
            self.assertEqual([s[0] for s in liste if "UYAP" in s[0]], ["ArthurLegal - UYAP Dashboard 0.0.1.lnk"] * 2,
                             "UYAP için tek simge; ayrı giriş kısayolu yok")
            self.assertTrue(all(s[1].endswith("pythonw.exe") and s[2].endswith("kisayol uyap-ekran") for s in ekran))
            sonuc, baslatilan = self.calistir(t, self.AC)
            self.assertEqual(sonuc, 0)
            self.assertEqual(baslatilan[0][0][0], str(mask / "pythonw.exe"))
            self.assertEqual(Path(baslatilan[0][0][-1]), uyap / "ekran.py")
            self.assertEqual(baslatilan[0][1], {"HF_HUB_OFFLINE": "1", "PYTHONNOUSERSITE": "1"})

    def test_urun_adi_kisayollarda_ve_eski_adlar_temizlenir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            self.assertIn("ArthurLegal 0.0.1.lnk", [s[0] for s in self.calistir(t, self.LISTE)], "ürün adı yoksa ArthurLegal")
            (t / "kok" / "firma" / "marka").mkdir(parents=True)
            (t / "kok" / "firma" / "marka" / "tema.json").write_text(json.dumps({"urun": "Örnek Büro Asistanı"}),
                                                                     encoding="utf-8")
            adlar = [s[0] for s in self.calistir(t, self.LISTE)]
            self.assertIn("Örnek Büro Asistanı 0.0.1.lnk", adlar)                 # sürüm adın sonunda
            self.assertIn("Örnek Büro Asistanı - Tapu 0.0.1.lnk", adlar)
            self.assertFalse([a for a in adlar if a.startswith("ArthurLegal")])
            self.assertEqual(self.calistir(t, "import kur; print(json.dumps([kur._menu().name, "
                                              "kur._kaldir_adi(kur.ortak.urun_adi())]))"),
                             ["Örnek Büro Asistanı", "Örnek Büro Asistanı - Kaldır"])
            # Ürün adı değişince önceki adla (ArthurLegal) kalan kısayollar ve boş kalan Başlat klasörü gider.
            masa = t / "ev" / "Desktop"
            programlar = t / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs"
            eski_menu, yeni_menu = programlar / "ArthurLegal", programlar / "Örnek Büro Asistanı"
            for klasor in (masa, eski_menu, yeni_menu):
                klasor.mkdir(parents=True, exist_ok=True)
            for yol in (masa / "ArthurLegal.lnk", masa / "ArthurLegal - Tapu.lnk", eski_menu / "ArthurLegal.lnk",
                        eski_menu / "ArthurLegal'i Kaldır.lnk", masa / "Örnek Büro Asistanı.lnk",
                        masa / "Örnek Büro Asistanı 0.0.0.lnk", masa / "Örnek Büro Asistanı 0.0.1.lnk",
                        yeni_menu / "Örnek Büro Asistanı - Kaldır.lnk", masa / "Başka Program.lnk"):
                yol.write_bytes(b"")
            self.calistir(t, "import kur; kur.eski_kisayollari_temizle(kur._menu(), {y for y, *_ in "
                             "kur._kisayol_listesi()} | {kur._menu() / (kur._kaldir_adi(kur.ortak.urun_adi()) + "
                             "'.lnk')}); print(1)")
            self.assertEqual(sorted(p.name for p in masa.iterdir()), ["Başka Program.lnk", "Örnek Büro Asistanı 0.0.1.lnk"])
            self.assertFalse(eski_menu.exists(), "boş kalan eski Başlat menüsü klasörü silinir")
            self.assertEqual([p.name for p in yeni_menu.iterdir()], ["Örnek Büro Asistanı - Kaldır.lnk"])
            self.calistir(t, "import kur; kur.kisayollar_sil(); print(1)")
            self.assertEqual([p.name for p in masa.iterdir()], ["Başka Program.lnk"])
            self.assertFalse(yeni_menu.exists())

    def test_uyap_simgesi_kisa_adla_eskiler_temizlenir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            (t / "kok" / "surumler" / "0.0.1" / "uyap").mkdir()
            (t / "kok" / "surumler" / "0.0.1" / "uyap" / "ekran.py").write_text("", encoding="utf-8")
            mask = t / "Local" / "Programs" / "Arthur Mask" / "runtime"
            mask.mkdir(parents=True)
            for ad in ("python.exe", "pythonw.exe"):
                (mask / ad).write_bytes(b"")
            (t / "kok" / "firma" / "marka").mkdir(parents=True)
            (t / "kok" / "firma" / "marka" / "tema.json").write_text(
                json.dumps({"urun": "Örnek Büro Asistanı", "kisa_ad": "Örnek"}), encoding="utf-8")
            adlar = [s[0] for s in self.calistir(t, self.LISTE)]
            self.assertEqual([a for a in adlar if "UYAP" in a], ["Örnek - UYAP Dashboard 0.0.1.lnk"] * 2)
            self.assertIn("Örnek Büro Asistanı - Tapu 0.0.1.lnk", adlar)      # öteki simgeler tam adla
            # Önceki sürümlerin UYAP kısayolları gider; kullanıcının kısa adla başlayan başka kısayolu kalır.
            masa = t / "ev" / "Desktop"
            menu = t / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Örnek Büro Asistanı"
            for klasor in (masa, menu):
                klasor.mkdir(parents=True, exist_ok=True)
            for yol in (masa / "Örnek Büro Asistanı - UYAP Ekranı.lnk", menu / "Örnek Büro Asistanı - UYAP Tarayıcısı.lnk",
                        masa / "Örnek - UYAP Dashboard.lnk", masa / "Örnek - UYAP Dashboard 0.0.1.lnk",
                        masa / "Örnek.lnk", masa / "Örnek - Notlar.lnk"):
                yol.write_bytes(b"")
            self.calistir(t, "import kur; kur.eski_kisayollari_temizle(kur._menu(), {y for y, *_ in "
                             "kur._kisayol_listesi()}); print(1)")
            self.assertEqual(sorted(p.name for p in masa.iterdir()),
                             ["Örnek - Notlar.lnk", "Örnek - UYAP Dashboard 0.0.1.lnk", "Örnek.lnk"])
            self.assertEqual(list(menu.iterdir()), [])
            self.calistir(t, "import kur; kur.kisayollar_sil(); print(1)")
            self.assertEqual(sorted(p.name for p in masa.iterdir()), ["Örnek - Notlar.lnk", "Örnek.lnk"])

    def test_guvenli_olmayan_kisa_ad_kullanilmaz(self):
        import ortak
        with tempfile.TemporaryDirectory() as t:
            marka = Path(t) / "marka"
            marka.mkdir()
            (marka / "tema.json").write_text(json.dumps({"urun": "Örnek Büro"}), encoding="utf-8")
            self.assertEqual(ortak.kisa_ad(Path(t)), "ArthurLegal")          # alan yoksa ArthurLegal
            for ad in ("Kötü/Ad", "CON", "a" * 61, "{app}"):
                with self.subTest(ad=ad):
                    (marka / "tema.json").write_text(json.dumps({"kisa_ad": ad}), encoding="utf-8")
                    self.assertEqual(ortak.kisa_ad(Path(t)), "ArthurLegal")
            (marka / "tema.json").write_text(json.dumps({"kisa_ad": " Örnek  Hukuk "}), encoding="utf-8")
            self.assertEqual(ortak.kisa_ad(Path(t)), "Örnek Hukuk")

    def test_eski_numarali_kisayol_taninir(self):
        """Güncelleme yarıda kaldıysa: kısayol çalışan sürümden başka bir numara taşıyor; güncelleyici eşitler."""
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            masa = t / "ev" / "Desktop"
            masa.mkdir(parents=True)
            kod = "import kur; print(json.dumps(kur.eski_surumlu_kisayol_var()))"
            self.assertFalse(self.calistir(t, kod), "hiç kısayol yoksa eşitlenecek bir şey yok")
            (masa / "ArthurLegal 0.0.1.lnk").write_bytes(b"")
            (masa / "Başka Program 0.0.0.lnk").write_bytes(b"")
            self.assertFalse(self.calistir(t, kod), "çalışan sürümle aynı numara; başka programa bakılmaz")
            (masa / "ArthurLegal - Tapu 0.0.0.lnk").write_bytes(b"")
            self.assertTrue(self.calistir(t, kod))
            (masa / "ArthurLegal - Tapu 0.0.0.lnk").unlink()
            (masa / "ArthurLegal - Tapu.lnk").write_bytes(b"")                     # 2.4.0'dan önceki sürümsüz ad
            self.assertTrue(self.calistir(t, kod))

    def test_programlar_listesi_anahtari_kurulum_betigiyle_ayni(self):
        import re
        iss = (BURASI / "kurulum" / "ArthurLegal.iss").read_text(encoding="utf-8-sig")
        appid = re.search(r"^AppId=\{(\{[0-9A-F-]+\})", iss, re.M).group(1)
        kod = "import kur; print(json.dumps(kur.KALDIRMA_ANAHTARI))"
        with tempfile.TemporaryDirectory() as t:
            sahte_kok(Path(t) / "kok")
            self.assertTrue(self.calistir(Path(t), kod).endswith("\\" + appid + "_is1"))
        self.assertIn("UninstallDisplayName={#UrunAd} {#Surum}", iss)

    def test_guncelleyici_yalniz_dogrulanmis_guncellemede_yeniden_yazar(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            (t / "kok" / "runtime").mkdir()
            (t / "kok" / "runtime" / "python.exe").write_bytes(b"")
            kod = ("import guncelle; c = []; guncelle.subprocess.run = lambda a, **k: c.append(a[-1]); "
                   "guncelle._claude_kaydet(True); guncelle._claude_kaydet(False); print(json.dumps(c))")
            self.assertEqual(self.calistir(t, kod), ["--kisayol", "--kisayol-esitle"])

    def test_guvenli_olmayan_urun_adi_kullanilmaz(self):
        import ortak
        with tempfile.TemporaryDirectory() as t:
            marka = Path(t) / "marka"
            marka.mkdir()
            for ad in ("Kötü/Ad", "Ad: İki", "CON", "nul", "a" * 61, "Ad.", "", "{app}", "Yüzde %n", None):
                with self.subTest(ad=ad):
                    (marka / "tema.json").write_text(json.dumps({"urun": ad}), encoding="utf-8")
                    self.assertEqual(ortak.urun_adi(Path(t)), "ArthurLegal")
            (marka / "tema.json").write_text(json.dumps({"urun": "  Örnek   Büro (Hukuk) · Asistanı  "}),
                                             encoding="utf-8")
            self.assertEqual(ortak.urun_adi(Path(t)), "Örnek Büro (Hukuk) · Asistanı")

    def test_simge_ayardaki_ozetli_dosya(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            kod = "import kur; print(json.dumps(kur._simge().name))"
            self.assertEqual(self.calistir(t, kod), "arthurlegal.ico")
            ayar = json.loads((t / "kok" / "ayar.json").read_text(encoding="utf-8"))
            for deger in ("buro-1234abcd.ico", "..\\disari.ico"):          # dosya yok; klasör dışı
                (t / "kok" / "ayar.json").write_text(json.dumps({**ayar, "simge": deger}), encoding="utf-8")
                self.assertEqual(self.calistir(t, kod), "arthurlegal.ico")
            (t / "kok" / "bin" / "buro-1234abcd.ico").write_bytes(b"\x00\x00\x01\x00")
            (t / "kok" / "ayar.json").write_text(json.dumps({**ayar, "simge": "buro-1234abcd.ico"}), encoding="utf-8")
            self.assertEqual(self.calistir(t, kod), "buro-1234abcd.ico")


class ProjeKlasoruTesti(unittest.TestCase):
    """'Use a folder' klasörleri: yönetilen içerik yenilenir, kullanıcı dosyaları korunur."""

    def calistir(self, kok, proje_koku, kod):
        tam = f"import sys, json; sys.path.insert(0, r'{kok}/surumler/0.0.1/istemci'); import proje; {kod}"
        env = {**ENV, "ARTHURLEGAL_PROJE_KOKU": str(proje_koku)}
        return subprocess.run([sys.executable, "-c", tam], env=env, capture_output=True, text=True,
                              encoding="utf-8", check=True).stdout.strip()

    def test_esitle_korur_ve_kaldirir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            pk = t / "projeler"
            self.assertEqual(self.calistir(t / "kok", pk, "print(len(proje.esitle()))"), "1")
            hedef = pk / "Hukuk Bürosu"
            self.assertIn("arthurlegal_talimat", (hedef / "CLAUDE.md").read_text(encoding="utf-8"))
            self.assertIn("Test & Ortakları", (hedef / "knowledge" / "firm-profile.md").read_text(encoding="utf-8"),
                          "büro katmanı paketteki şablonu ezmeli")
            self.assertTrue((hedef / "buro" / "ek-3-kirmizi-hatlar.md").exists())
            (hedef / "calismalar" / "taslak.txt").write_text("avukatın taslağı", encoding="utf-8")
            (hedef / "notlar.txt").write_text("kişisel not", encoding="utf-8")
            self.assertEqual(self.calistir(t / "kok", pk, "print(len(proje.esitle()))"), "0", "sürüm aynıysa dokunmamalı")
            self.calistir(t / "kok", pk, "proje.esitle(zorla=True)")
            self.assertEqual((hedef / "calismalar" / "taslak.txt").read_text(encoding="utf-8"), "avukatın taslağı")
            self.calistir(t / "kok", pk, "proje.kaldir()")
            self.assertFalse((hedef / "SYSTEM_PROMPT.md").exists())
            self.assertFalse((hedef / "knowledge").exists())
            self.assertTrue((hedef / "notlar.txt").exists(), "kullanıcı dosyası silinmemeli")
            self.assertTrue((hedef / "calismalar" / "taslak.txt").exists())


class SunucuTesti(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gecici = tempfile.TemporaryDirectory()
        cls.uzak, url = sunucu_baslat(SahteUzak)
        kok = Path(cls.gecici.name) / "kok"
        sahte_kok(kok, uzak=url + "/mcp")
        cls.surec = subprocess.Popen([sys.executable, "-B", str(kok / "bin" / "al.py"), "sunucu"], stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=ENV, text=True, encoding="utf-8")
        cls.kuyruk = queue.Queue()
        threading.Thread(target=lambda: [cls.kuyruk.put(json.loads(s)) for s in cls.surec.stdout], daemon=True).start()
        cls.no = 0

    @classmethod
    def tearDownClass(cls):
        cls.surec.stdin.close()
        cls.surec.wait(10)
        cls.surec.stderr.close()
        cls.surec.stdout.close()
        cls.uzak.shutdown()
        cls.uzak.server_close()
        cls.gecici.cleanup()

    def iste(self, metod, params=None):
        SunucuTesti.no += 1
        no = SunucuTesti.no
        self.surec.stdin.write(json.dumps({"jsonrpc": "2.0", "id": no, "method": metod, "params": params or {}}) + "\n")
        self.surec.stdin.flush()
        while True:
            m = self.kuyruk.get(timeout=20)
            if m.get("id") == no:
                return m

    def arac(self, ad, **arg):
        return self.iste("tools/call", {"name": ad, "arguments": arg})["result"]

    def test_1_el_sikisma_ve_arac_listesi(self):
        r = self.iste("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "t"}})["result"]
        self.assertEqual(r["protocolVersion"], "2025-06-18")
        self.assertIn("arthurlegal_talimat", r["instructions"])
        self.surec.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")
        self.surec.stdin.flush()
        adlar = [t["name"] for t in self.iste("tools/list")["result"]["tools"]]
        self.assertIn("arthurlegal_bilgi_getir", adlar)
        self.assertIn("tr_ictihat_ara", adlar)
        self.assertNotIn("tkgm_tapu_kaydi_oku", adlar, "tapu kaydı aracı buluta aktarılmamalı")

    def test_2_talimat_buro_katmani(self):
        metin = self.arac("arthurlegal_talimat", profil="hukuk-burosu")["content"][0]["text"]
        self.assertIn("ArthurLegal Hukuk Bürosu talimatı", metin)
        self.assertIn("Paket 1.9.1", metin)
        self.assertIn("Test & Ortakları", metin)
        self.assertIn("buro/ek-3-kirmizi-hatlar.md", metin)
        varsayilan = self.arac("arthurlegal_talimat")["content"][0]["text"]  # profil verilmeden: kurulum varsayılanı
        self.assertIn("Hukuk Bürosu", varsayilan.splitlines()[0])
        profil = self.arac("arthurlegal_bilgi_getir", yol="firm-profile.md")["content"][0]["text"]
        self.assertIn("Test & Ortakları", profil, "büro katmanı paketteki şablonu ezmeli")

    def test_3_arama_turkce_duyarsiz(self):
        metin = self.arac("arthurlegal_bilgi_ara", sorgu="ıslah", profil="hukuk-burosu")["content"][0]["text"]
        self.assertIn("knowledge/references/hmk-rehberi.md", metin)
        self.assertIn("HMK m. 176", metin)

    def test_4_beceri_bolumu(self):
        metin = self.arac("arthurlegal_bilgi_getir", yol="knowledge/skills/commercial-legal__skills.md",
                          bolum="/commercial-legal:nda-review")["content"][0]["text"]
        self.assertIn("NDA incelemesi", metin)
        self.assertIn("## Instructions", metin, "bölüm iç başlıkta kesilmemeli")
        self.assertNotIn("Yenileme", metin, "sonraki beceri bölüme girmemeli")

    def test_5_uzak_arac_sse_ve_oturum(self):
        r = self.arac("tr_ictihat_ara", sorgu="iş kazası")
        self.assertIn("iş kazası", r["content"][0]["text"])
        r = self.arac("tkgm_tapu_kaydi_oku", metin="x")
        self.assertTrue(r["isError"])

    def test_6_hatalar(self):
        r = self.arac("arthurlegal_bilgi_getir", yol="../../ayar.json")
        self.assertTrue(r["isError"])
        self.assertEqual(self.iste("yok/boyle")["error"]["code"], -32601)
        self.assertIn("uzak_arac_sayisi", self.arac("arthurlegal_durum")["content"][0]["text"])


class GuncelleyiciTesti(unittest.TestCase):
    def hazirla(self, t: Path, kurcala=None):
        yayin = t / "yayin"
        yayin.mkdir()
        paket_yaz(t / "yeni", "0.0.2")
        with zipfile.ZipFile(yayin / "arthurlegal-paket-0.0.2.zip", "w") as z:
            for y in (t / "yeni").rglob("*"):
                z.write(y, y.relative_to(t / "yeni").as_posix())
        import hashlib
        ozet = hashlib.sha256((yayin / "arthurlegal-paket-0.0.2.zip").read_bytes()).hexdigest()
        manifest = {"surum": "0.0.2", "paket": {"dosya": "arthurlegal-paket-0.0.2.zip", "sha256": ozet}}
        if kurcala == "sha":
            manifest["paket"]["sha256"] = "0" * 64
        ham = json.dumps(manifest).encode()
        (yayin / "arthurlegal-manifest.sig").write_text(ed25519.sign(TEST_TOHUM, ham).hex(), encoding="ascii")
        if kurcala == "imza":
            ham = ham.replace(b"0.0.2", b"0.0.3", 1)
        (yayin / "arthurlegal-manifest.json").write_bytes(ham)

        class Statik(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *a, **k):
                super().__init__(*a, directory=str(yayin), **k)

            def log_message(self, *a):
                pass

        httpd, url = sunucu_baslat(Statik)
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)
        sahte_kok(t / "kok", manifest=url + "/arthurlegal-manifest.json")
        r = subprocess.run([sys.executable, "-B", str(t / "kok" / "bin" / "al.py"), "guncelle", "--mask-yok"],
                           env=ENV, capture_output=True, text=True, encoding="utf-8", timeout=120)
        aktif = (t / "kok" / "aktif.txt").read_text(encoding="utf-8") if (t / "kok" / "aktif.txt").exists() else ""
        return r, aktif

    def test_imzali_paket_kurulur(self):
        with tempfile.TemporaryDirectory() as t:
            r, aktif = self.hazirla(Path(t))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertEqual(aktif, "0.0.2")
            self.assertTrue((Path(t) / "kok" / "surumler" / "0.0.2" / "istemci" / "arthurlegal_sunucu.py").exists())
            self.assertTrue((Path(t) / "kok" / "surumler" / "0.0.1").exists(), "önceki sürüm geri dönüş için kalmalı")
            durum = json.loads((Path(t) / "kok" / "veri" / "durum.json").read_text(encoding="utf-8"))
            self.assertEqual((durum["son_guncelleme"]["onceki"], durum["son_guncelleme"]["yeni"]), ("0.0.1", "0.0.2"))

    def test_kurcalanmis_manifest_reddedilir(self):
        with tempfile.TemporaryDirectory() as t:
            r, aktif = self.hazirla(Path(t), kurcala="imza")
            self.assertIn("imza", r.stdout)
            self.assertEqual(aktif, "")
            self.assertFalse((Path(t) / "kok" / "surumler" / "0.0.3").exists())
            durum = json.loads((Path(t) / "kok" / "veri" / "durum.json").read_text(encoding="utf-8"))
            self.assertNotIn("son_guncelleme", durum, "güncelleme olmadıysa olmuş gibi gösterilmez")

    def test_private_depo_jetonla_iner(self):
        """Dağıtım private depodan: varlıklar GitHub API'sinden, kurulumdaki jetonla indirilir."""
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            yayin = t / "yayin"
            yayin.mkdir()
            paket_yaz(t / "yeni", "0.0.2")
            zip_yolu = yayin / "arthurlegal-paket-0.0.2.zip"
            with zipfile.ZipFile(zip_yolu, "w") as z:
                for y in (t / "yeni").rglob("*"):
                    z.write(y, y.relative_to(t / "yeni").as_posix())
            import hashlib
            manifest = json.dumps({"surum": "0.0.2", "paket": {"dosya": zip_yolu.name,
                                                               "sha256": hashlib.sha256(zip_yolu.read_bytes()).hexdigest()}}).encode()
            (yayin / "arthurlegal-manifest.json").write_bytes(manifest)
            (yayin / "arthurlegal-manifest.sig").write_text(ed25519.sign(TEST_TOHUM, manifest).hex(), encoding="ascii")
            gorulen = []

            class SahteApi(http.server.BaseHTTPRequestHandler):
                def log_message(self, *a):
                    pass

                def do_GET(self):
                    gorulen.append((self.path, self.headers.get("Authorization"), self.headers.get("Accept")))
                    if self.headers.get("Authorization") != "Bearer jeton-123":
                        self.send_response(404)
                        self.end_headers()
                        return
                    if self.path.startswith("/repos/"):
                        taban = f"http://127.0.0.1:{self.server.server_address[1]}/varlik/"
                        govde = json.dumps([
                            {"draft": True, "prerelease": False, "assets": []},
                            {"draft": False, "prerelease": True, "assets": [  # ön sürüm atlanmalı
                                {"name": "arthurlegal-manifest.json", "url": taban + "yok"}]},
                            {"draft": False, "prerelease": False, "assets": [
                                {"name": a, "url": taban + a} for a in
                                ("arthurlegal-manifest.json", "arthurlegal-manifest.sig", zip_yolu.name)]},
                        ]).encode()
                    else:
                        govde = (yayin / self.path.rsplit("/", 1)[1]).read_bytes()
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(govde)))
                    self.end_headers()
                    self.wfile.write(govde)

            httpd, url = sunucu_baslat(SahteApi)
            self.addCleanup(httpd.server_close)
            self.addCleanup(httpd.shutdown)
            sahte_kok(t / "kok")
            ayar = json.loads((t / "kok" / "ayar.json").read_text(encoding="utf-8"))
            ayar.update(dagitim_deposu="x/y", jeton="jeton-123", manifest_url="", api_tabani=url)
            (t / "kok" / "ayar.json").write_text(json.dumps(ayar), encoding="utf-8")
            r = subprocess.run([sys.executable, "-B", str(t / "kok" / "bin" / "al.py"), "guncelle", "--mask-yok"],
                               env=ENV, capture_output=True, text=True, encoding="utf-8", timeout=120)
            self.assertIn("0.0.2 kuruldu", r.stdout, r.stdout + r.stderr)
            self.assertEqual((t / "kok" / "aktif.txt").read_text(encoding="utf-8"), "0.0.2")
            self.assertTrue(any(a[2] == "application/octet-stream" for a in gorulen), "varlıklar octet-stream ile inmeli")

    def test_sha_uyusmazligi_reddedilir(self):
        with tempfile.TemporaryDirectory() as t:
            r, aktif = self.hazirla(Path(t), kurcala="sha")
            self.assertIn("sha256", r.stdout)
            self.assertEqual(aktif, "")
            self.assertFalse((Path(t) / "kok" / "surumler" / "0.0.2").exists())


if __name__ == "__main__":
    unittest.main()
