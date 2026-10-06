"""İstemci testleri: Ed25519, Claude yapılandırması, yerel MCP sunucusu (sahte uzak sunucuyla)
ve güncelleyici (sahte GitHub yayınıyla). Ağa çıkmaz; her şey 127.0.0.1'de ve geçici klasörde.

    python -m unittest discover -s tests
"""
import contextlib
import http.server
import io
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
KASA_TOHUM = bytes(range(32, 64))
YABANCI_TOHUM = bytes(range(64, 96))
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8", "ARTHURLEGAL_GUNCELLEME": "0"}
ENV.pop("ARTHURLEGAL_KOK", None)
MACOS = sys.platform == "darwin"
# Windows kısayolları (.lnk), Başlat menüsü ve %APPDATA% yapılandırmaları; macOS karşılıkları MacKurulumTesti'nde.
SADECE_WINDOWS = unittest.skipIf(MACOS, "Windows'a özgü (macOS: MacKurulumTesti)")

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


def sahte_kok(kok: Path, surum="0.0.1", uzak="http://127.0.0.1:9/mcp", manifest="http://127.0.0.1:9/m.json",
              anahtarlar=None):
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
    (s / "tapu").mkdir()  # genel derlemede Tapu bileşeni var (seçilirse kaydedilir)
    (s / "tapu" / "server.py").write_text("", encoding="utf-8")
    icerik = {"paketler": {"hukuk-burosu": "1.9.1"}}
    if anahtarlar is not None:
        icerik["anahtarlar"] = anahtarlar
    (s / "icerik.json").write_text(json.dumps(icerik), encoding="utf-8")
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
                               for n in ("status", "tr_ictihat_ara", "tkgm_tapu_kaydi_oku")]
                     + [{"name": "ornek_yazan", "description": "yazar", "inputSchema": {"type": "object"},
                         "annotations": {"readOnlyHint": False}}]}
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
        self.assertIn("<i data-os=\"windows\">Örnek Büro Asistanı - Tapu</i>", sayfa)
        self.assertIn("<i data-os=\"mac\">Örnek Büro Asistanı Tapu</i>", sayfa, "macOS uygulamasının adı")
        self.assertIn("<i>Örnek Büro Asistanı - Kaldır</i>", sayfa, "macOS'taki kaldırma uygulamasının adı (kur._kaldir_adi)")
        self.assertNotIn("{{", sayfa)
        self.assertIn('<a href="baslangic-en.html">English</a>', sayfa)
        self.assertIn("<b>Always allow</b>", sayfa, "Claude Desktop'un arayüzü Türkçe değil")
        en = (self.kok / "rehber" / "baslangic-en.html").read_text(encoding="utf-8")
        self.assertIn("<title>Örnek Büro Asistanı Start</title>", en)
        self.assertIn("<i data-os=\"windows\">Örnek Büro Asistanı - Tapu</i>", en)
        self.assertIn("<i>Örnek Büro Asistanı - Uninstall</i>", en)
        self.assertIn('<a href="baslangic.html">Türkçe</a>', en)
        self.assertIn("You are the ArthurLegal Law Firm assistant.", en, "İngilizce ön yükleme talimatı")
        self.assertNotIn("{{", en)
        self.derle.rehber_yaz(self.kok, "", icerik)
        sayfa = (self.kok / "rehber" / "baslangic.html").read_text(encoding="utf-8")
        self.assertIn("<title>ArthurLegal Başlangıç</title>", sayfa)
        self.assertIn("<i>ArthurLegal&#x27;i Kaldır</i>", sayfa)

    def test_zip_talimati_iki_dilde(self):
        """Akıllı Uygulama Denetimi internetten gelen .cmd'yi engeller: işaret ayıklamadan önce kaldırılır."""
        self.assertIn("Engellemeyi Kaldır", self.derle.ZIP_BENIOKU)
        self.assertIn("Tümünü Ayıkla...", self.derle.ZIP_BENIOKU)
        self.assertIn("Unblock", self.derle.ZIP_README)
        self.assertIn("Extract All...", self.derle.ZIP_README)
        self.assertLess(self.derle.ZIP_BENIOKU.index("Engellemeyi Kaldır"), self.derle.ZIP_BENIOKU.index("Tümünü Ayıkla"))


class KurulumBetigiTesti(unittest.TestCase):
    """Üzerine kurulum: kısayollar kurulan sürümün koduyla yazılır, Başlat menüsü klasörü ürün adından gelir."""

    def test_uzerine_kurulum_yeni_kodla_ve_yeni_klasorle(self):
        iss = (BURASI / "kurulum" / "ArthurLegal.iss").read_text(encoding="utf-8-sig")
        self.assertIn("UsePreviousGroup=no", iss, "Inno önceki kurulumun menü klasörünü yeniden kullanırdı")
        sil, kur = iss.find(r"DeleteFile(ExpandConstant('{app}\aktif.txt'))"), iss.find("kur --kurulum --kisayol")
        self.assertTrue(0 < sil < kur, "al.py aktif.txt'deki eski sürümü seçerdi; önce silinmeli")
        # Kaldırma kısayolunun adı iki dilde de kur._kaldir_adi ile aynı olmalı.
        self.assertIn('#define KaldirAdiTr "ArthurLegal\'i Kaldır"', iss)
        self.assertIn('#define KaldirAdiTr UrunAd + " - Kaldır"', iss)
        self.assertIn('#define KaldirAdiEn "Uninstall ArthurLegal"', iss)
        self.assertIn('#define KaldirAdiEn UrunAd + " - Uninstall"', iss)
        self.assertIn('Name: "{group}\\{cm:KaldirAdi}"', iss)

    def test_iki_dil_ve_dil_kur_py_ye_gecer(self):
        """Kurulum İngilizce ve Türkçe; dil sorulur, lisans sayfası dile göre, seçilen dil kur.py'ye --dil ile geçer."""
        iss = (BURASI / "kurulum" / "ArthurLegal.iss").read_text(encoding="utf-8-sig")
        self.assertIn('Name: "en"; MessagesFile: "compiler:Default.isl"; LicenseFile: "{#Kaynak}\\LICENSE.txt"', iss)
        self.assertIn('Name: "tr"; MessagesFile: "compiler:Languages\\Turkish.isl"; LicenseFile: "{#Kaynak}\\LISANS.txt"', iss)
        self.assertIn("ShowLanguageDialog=yes", iss)
        self.assertIn("kur --kurulum --kisayol --dil ' +\n       ActiveLanguage", iss)
        self.assertIn("en.RehberDosyasi=baslangic-en.html", iss)
        self.assertIn("tr.RehberDosyasi=baslangic.html", iss)
        self.assertNotIn("Her zaman izin ver'i seçin", iss, "Claude Desktop'un düğmesi İngilizce: Always allow")
        import re
        # Her özel ileti iki dilde de tanımlı olmalı; CustomMessage('X') tanımsız ileti çalışırken hata verir.
        tanimli = {dil: set(re.findall(rf"^{dil}\.(\w+)=", iss, re.M)) for dil in ("en", "tr")}
        self.assertEqual(tanimli["en"], tanimli["tr"])
        kullanilan = set(re.findall(r"CustomMessage\('(\w+)'\)", iss)) | set(re.findall(r"\{cm:(\w+)\}", iss))
        self.assertTrue(kullanilan, "özel iletiler kullanılıyor")
        self.assertLessEqual(kullanilan, tanimli["en"])

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


@SADECE_WINDOWS
class ClaudeAyariTesti(unittest.TestCase):
    def calistir(self, komut, kok, appdata, yerel):
        kod = f"import sys; sys.path.insert(0, r'{kok}/surumler/0.0.1/istemci'); import claude_ayari, json; print(json.dumps([str(y) for y in claude_ayari.{komut}()]))"
        env = {**ENV, "APPDATA": str(appdata), "LOCALAPPDATA": str(yerel), "HOME": str(kok.parent / "ev")}
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


@SADECE_WINDOWS
class KisayolTesti(unittest.TestCase):
    """UYAP için tek simge (UYAP Dashboard) yalnız köprü ve Arthur Mask birlikteyse; Mask'in Python'unda açılır."""

    LISTE = "import kur; print(json.dumps([[y.name, str(h), a] for y, h, a, _ in kur._kisayol_listesi()]))"
    AC = ("import kisayol, ortak; k = []; ortak.arka_planda = lambda a, o=None: k.append([[str(x) for x in a], "
          "{d: o.get(d) for d in ('HF_HUB_OFFLINE', 'PYTHONNOUSERSITE')}]); print(json.dumps([kisayol.uyap_ekran(), k]))")

    def calistir(self, t, kod):
        tam = f"import sys, json; sys.path.insert(0, r'{t / 'kok'}/surumler/0.0.1/istemci'); {kod}"
        env = {**ENV, "APPDATA": str(t / "Roaming"), "LOCALAPPDATA": str(t / "Local"), "USERPROFILE": str(t / "ev"),
               "HOME": str(t / "ev"), "ARTHURLEGAL_PROJE_KOKU": str(t / "projeler")}
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

    def test_kisayollar_kurulumun_dilinde(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            sahte_kok(t / "kok")
            adlar = [s[0] for s in self.calistir(t, self.LISTE)]
            self.assertIn("ArthurLegal - Başlangıç Rehberi 0.0.1.lnk", adlar, "dil yazılmamışsa (eski kurulum) Türkçe")
            (t / "kok" / "rehber").mkdir()
            (t / "kok" / "rehber" / "baslangic-en.html").write_text("", encoding="utf-8")
            self.calistir(t, "import kur; print(kur.main(['--kaydet', '--dil', 'en']))")
            liste = self.calistir(t, self.LISTE)
            adlar = [s[0] for s in liste]
            for ad in ("ArthurLegal 0.0.1.lnk", "ArthurLegal - Tapu 0.0.1.lnk", "ArthurLegal - Start Guide 0.0.1.lnk",
                       "ArthurLegal - Project Folders 0.0.1.lnk", "ArthurLegal - Check for Updates 0.0.1.lnk"):
                self.assertIn(ad, adlar)
            self.assertFalse([a for a in adlar if "Rehberi" in a or "Denetle" in a])
            rehber = next(s for s in liste if s[0] == "ArthurLegal - Start Guide 0.0.1.lnk")
            self.assertEqual(Path(rehber[1]).name, "baslangic-en.html")
            self.assertEqual(self.calistir(t, "import kur; print(json.dumps([kur._kaldir_adi('ArthurLegal'), "
                                              "kur._kaldir_adi('Örnek'), kur._kaldir_adi('ArthurLegal', 'tr')]))"),
                             ["Uninstall ArthurLegal", "Örnek - Uninstall", "ArthurLegal'i Kaldır"])
            # Dil değişince öteki dildeki kısayollar ve kaldırma kısayolu temizlenir.
            menu = t / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "ArthurLegal"
            menu.mkdir(parents=True)
            for ad in ("ArthurLegal - Başlangıç Rehberi 0.0.1.lnk", "ArthurLegal - Güncellemeleri Denetle 0.0.1.lnk",
                       "ArthurLegal'i Kaldır.lnk", "Uninstall ArthurLegal.lnk"):
                (menu / ad).write_bytes(b"")
            self.calistir(t, "import kur; kur.eski_kisayollari_temizle(kur._menu(), {y for y, *_ in "
                             "kur._kisayol_listesi()} | {kur._menu() / (kur._kaldir_adi(kur.ortak.urun_adi()) + "
                             "'.lnk')}); print(1)")
            self.assertEqual([p.name for p in menu.iterdir()], ["Uninstall ArthurLegal.lnk"])
            # İngilizce sayfa yoksa (eski kurulumun rehber klasörü) Türkçesi açılır.
            (t / "kok" / "rehber" / "baslangic-en.html").unlink()
            self.assertEqual(self.calistir(t, "import ortak; print(json.dumps(ortak.rehber_dosyasi().name))"),
                             "baslangic.html")

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
        araclar = {t["name"]: t for t in self.iste("tools/list")["result"]["tools"]}
        adlar = list(araclar)
        self.assertIn("arthurlegal_bilgi_getir", adlar)
        self.assertIn("tr_ictihat_ara", adlar)
        self.assertNotIn("tkgm_tapu_kaydi_oku", adlar, "tapu kaydı aracı buluta aktarılmamalı")
        # Araştırma araçları salt okunur: Claude Desktop kalıcı "Always allow" sunabilsin.
        self.assertEqual(araclar["tr_ictihat_ara"]["annotations"], {"readOnlyHint": True, "openWorldHint": True})
        self.assertEqual(araclar["ornek_yazan"]["annotations"], {"readOnlyHint": False}, "uzak işaret korunur")

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


class SaltOkunurTesti(unittest.TestCase):
    def test_isaretsiz_arac_salt_okunur_olur_acik_isarete_dokunulmaz(self):
        import arthurlegal_sunucu as s
        girdi = [{"name": "a"}, {"name": "b", "annotations": {"title": "B"}},
                 {"name": "c", "annotations": {"readOnlyHint": False}}, {"name": "d", "annotations": {"destructiveHint": True}}]
        cikti = {t["name"]: t["annotations"] for t in s.salt_okunur_isaretle(girdi)}
        self.assertEqual(cikti["a"], {"readOnlyHint": True, "openWorldHint": True})
        self.assertEqual(cikti["b"], {"title": "B", "readOnlyHint": True, "openWorldHint": True})
        self.assertEqual(cikti["c"], {"readOnlyHint": False})
        self.assertEqual(cikti["d"], {"destructiveHint": True})
        self.assertNotIn("annotations", girdi[0], "girdi değiştirilmez")
        self.assertEqual(s.salt_okunur_isaretle(None), [])


@SADECE_WINDOWS
class AkilliDenetimTesti(unittest.TestCase):
    """Akıllı Uygulama Denetimi açıkken imzasız Arthur Mask kurulumu çalışmaz: güncelleyici onu indirmez."""

    def test_denetim_acikken_mask_indirilmez(self):
        import guncelle
        import ortak
        eski = (ortak.akilli_denetim_acik, ortak.mask_surumu, ortak.indir, ortak.VERI)
        with tempfile.TemporaryDirectory() as t:
            try:
                ortak.VERI = Path(t)
                (Path(t) / "indirilen").mkdir()
                kalan = Path(t) / "indirilen" / "ArthurMask-Kurulum-1.0.0.exe"
                kalan.write_bytes(b"onceki deneme")
                ortak.mask_surumu = lambda: None

                def indir(*a, **k):
                    raise AssertionError("indirilmemeliydi")
                ortak.indir = indir
                ortak.akilli_denetim_acik = lambda: True
                manifest = {"mask": {"surum": "1.0.0", "url": "https://ornek.invalid/m.exe", "sha256": "0" * 64}}
                self.assertIn("Akıllı Uygulama Denetimi açık", guncelle.mask_guncelle(manifest))
                self.assertFalse(kalan.exists(), "önceki denemeden kalan 1 GB'lık dosya silinir")
                # Arthur Mask kurulumu imzalıysa (manifest bunu söylerse) denetim engel değildir: indirmeye çalışır.
                manifest["mask"]["imzali"] = True
                with self.assertRaises(AssertionError):
                    guncelle.mask_guncelle(manifest)
                ortak.akilli_denetim_acik = lambda: False
                manifest["mask"].pop("imzali")
                with self.assertRaises(AssertionError):
                    guncelle.mask_guncelle(manifest)
            finally:
                ortak.akilli_denetim_acik, ortak.mask_surumu, ortak.indir, ortak.VERI = eski


class YayimlamaTesti(unittest.TestCase):
    """yayinla.py: yeni yayın önce taslak açılır, bütün dosyalar yüklenince tek adımda yayımlanır (indirme düğmesi
    ve güncelleyici arada "Not Found" görmez); var olan yayında dosya geçici adla yüklenip adı düzeltilir; public
    depoya yalnız bu derlemenin genel kurulumu gider."""

    KURULUMLAR = ("ArthurLegal-Kurulum.exe", "ArthurLegal-Kurulum.zip")

    def setUp(self):
        sys.path.insert(0, str(BURASI / "yayin"))
        import ortak
        import yayinla
        self.y = yayinla
        self.cikti = Path(tempfile.mkdtemp())
        self.eski = (yayinla.CIKTI, yayinla.api, yayinla.github_jetonu)
        yayinla.CIKTI = self.cikti
        yayinla.github_jetonu = lambda: "jeton"
        for ad in ("arthurlegal-paket-9.9.9.zip", "arthurlegal-manifest.json", "arthurlegal-manifest.sig") + self.KURULUMLAR:
            (self.cikti / ad).write_bytes(ad.encode())
        self.d = {"surum": "9.9.9", "icerik": {"paketler": {}, "bilesenler": {"tapu": "0.5.2"}},
                  "paket": {"dosya": "arthurlegal-paket-9.9.9.zip"},
                  "kurulum": {a: ortak.sha256_dosya(self.cikti / a) for a in self.KURULUMLAR}}

    def tearDown(self):
        self.y.CIKTI, self.y.api, self.y.github_jetonu = self.eski
        shutil.rmtree(self.cikti, ignore_errors=True)

    def sahte_github(self, var_olan=None):
        """İstekleri sırayla kaydeden sahte GitHub API'si. var_olan: yayımlanmış yayının dosya adları."""
        import urllib.error
        kayit, yayin = [], {}
        sayac = iter(range(1, 1000))

        def varlik(ad):
            return {"name": ad, "url": f"A/{next(sayac)}"}
        if var_olan is not None:
            yayin.update(url="R/1", upload_url="U{?name,label}", html_url="h", draft=False,
                         assets=[varlik(a) for a in var_olan])

        def api(yontem, url, jeton, veri=None, tur="application/json"):
            yol = url.replace("https://api.github.com/repos/o/r/releases", "R")
            kayit.append((yontem, yol, veri if isinstance(veri, dict) else None))
            if yontem == "GET" and yol.startswith("R/tags/"):
                if not yayin:
                    raise urllib.error.HTTPError(url, 404, "yok", {}, None)
                return dict(yayin)
            if yontem == "GET" and yol.startswith("R?"):
                return []
            if yontem == "POST" and yol == "R":
                yayin.update(url="R/1", upload_url="U{?name,label}", html_url="h", assets=[], **veri)
                return dict(yayin)
            if yontem == "POST" and yol.startswith("U?name="):
                yeni = varlik(urllib.parse.unquote(yol.split("=", 1)[1]))
                yayin["assets"].append(yeni)
                return yeni
            if yontem == "DELETE":
                yayin["assets"] = [a for a in yayin["assets"] if a["url"] != yol]
                return None
            if yontem == "PATCH" and yol.startswith("A/"):
                next(a for a in yayin["assets"] if a["url"] == yol)["name"] = veri["name"]
                return None
            if yontem == "PATCH" and yol == "R/1":
                yayin.update(veri)
                return dict(yayin)
            raise AssertionError(f"beklenmeyen istek: {yontem} {yol}")
        import urllib.parse
        self.y.api = api
        return kayit, yayin

    def test_yeni_yayin_once_taslak_sonra_tek_adimda_latest(self):
        kayit, yayin = self.sahte_github()
        with contextlib.redirect_stdout(io.StringIO()):
            self.y.yayimla("o/r", "v9.9.9", self.d, False, public=True)
        olustur = next(v for y, u, v in kayit if y == "POST" and u == "R")
        self.assertTrue(olustur["draft"])
        self.assertNotIn("make_latest", olustur, "taslak Latest olamaz; işaret yayımlarken verilir")
        yuklenen = [u.split("=", 1)[1] for y, u, v in kayit if y == "POST" and u.startswith("U?")]
        self.assertEqual(yuklenen, ["arthurlegal-paket-9.9.9.zip", *self.KURULUMLAR, "arthurlegal-manifest.sig",
                                    "arthurlegal-manifest.json"], "manifest en son")
        son = kayit[-1]
        self.assertEqual(son, ("PATCH", "R/1", {"draft": False, "prerelease": False, "make_latest": "true"}))
        self.assertFalse(yayin["draft"])

    def test_on_surum_latest_olmaz(self):
        kayit, _ = self.sahte_github()
        with contextlib.redirect_stdout(io.StringIO()):
            self.y.yayimla("o/r", "v9.9.9", self.d, True, public=True)
        self.assertEqual(kayit[-1][2], {"draft": False, "prerelease": True, "make_latest": "false"})

    def test_var_olan_yayinda_dosya_gecici_adla_degisir(self):
        adlar = ["arthurlegal-paket-9.9.9.zip", *self.KURULUMLAR, "arthurlegal-manifest.sig", "arthurlegal-manifest.json"]
        kayit, yayin = self.sahte_github(var_olan=adlar)
        with contextlib.redirect_stdout(io.StringIO()):
            self.y.yayimla("o/r", "v9.9.9", self.d, False, public=True)
        exe = [(y, u.split("=", 1)[-1] if y == "POST" else u, v) for y, u, v in kayit
               if (y == "POST" and "Kurulum.exe" in u) or (y == "DELETE" and u == "A/2")
               or (y == "PATCH" and v == {"name": "ArthurLegal-Kurulum.exe"})]
        self.assertEqual([x[0] for x in exe], ["POST", "DELETE", "PATCH"], "yeni dosya yüklenmeden eski silinmez")
        self.assertEqual(exe[0][1], "yukleniyor-ArthurLegal-Kurulum.exe")
        self.assertEqual(sorted(a["name"] for a in yayin["assets"]), sorted(adlar))
        self.assertFalse([y for y, u, v in kayit if y == "PATCH" and u == "R/1"], "yayımlanmış yayına dokunulmaz")

    def test_public_depoya_yalniz_bu_derlemenin_genel_kurulumu(self):
        (self.cikti / "ArthurLegal-Kurulum-ornek.exe").write_bytes(b"buro")
        self.assertEqual(self.y.yuklenecek_kurulumlar(self.cikti, self.d, True), list(self.KURULUMLAR))
        self.assertIn("ArthurLegal-Kurulum-ornek.exe", self.y.yuklenecek_kurulumlar(self.cikti, self.d, False))
        (self.cikti / "ArthurLegal-Kurulum.exe").write_bytes(b"UYAP'li deneme derlemesi")
        with self.assertRaises(SystemExit):
            self.y.yuklenecek_kurulumlar(self.cikti, self.d, True)
        (self.cikti / "ArthurLegal-Kurulum.exe").write_bytes(b"ArthurLegal-Kurulum.exe")
        with self.assertRaises(SystemExit):
            self.y.yuklenecek_kurulumlar(self.cikti, {**self.d, "icerik": {"bilesenler": {"uyap": "1.18.3"}}}, True)
        with self.assertRaises(SystemExit):
            self.y.yuklenecek_kurulumlar(self.cikti, {**self.d, "kurulum": {}}, True)

    def test_mac_paketi_yalniz_ayni_derlemeden(self):
        """macOS paketi GitHub Actions'ta derlenir; yayına ancak aynı sürümün ve aynı kaynakların (ArthurLegal ve Tapu
        commit'leri) derlemesiyse ve özeti tutuyorsa girer. Sürüm notu iki kurulumu da söyler."""
        import ortak
        kaynak = {"ArthurLegal": {"commit": "abc1234"}, "tapu": {"commit": "def5678"}}
        self.d["kaynak"] = kaynak
        pkg = self.cikti / "ArthurLegal-Kurulum.pkg"
        pkg.write_bytes(b"pkg")
        mac = {"surum": "9.9.9", "kaynak": kaynak, "kurulum": {pkg.name: ortak.sha256_dosya(pkg)}}
        (self.cikti / "derleme-macos.json").write_text(json.dumps(mac), encoding="utf-8")
        self.assertEqual(self.y.yuklenecek_kurulumlar(self.cikti, self.d, True), [*self.KURULUMLAR, pkg.name])
        uzun = {**mac, "kaynak": {**kaynak, "ArthurLegal": {"commit": "abc1234f"}}}
        (self.cikti / "derleme-macos.json").write_text(json.dumps(uzun), encoding="utf-8")
        self.assertIn(pkg.name, self.y.yuklenecek_kurulumlar(self.cikti, self.d, True), "kısa özetin uzunluğu değişebilir")
        for bozuk in ({"surum": "9.9.8"}, {"kaynak": {**kaynak, "tapu": {"commit": "0000000"}}},
                      {"kurulum": {pkg.name: "0" * 64}}):
            (self.cikti / "derleme-macos.json").write_text(json.dumps({**mac, **bozuk}), encoding="utf-8")
            with self.subTest(bozuk=bozuk), self.assertRaises(SystemExit):
                self.y.yuklenecek_kurulumlar(self.cikti, self.d, True)
        (self.cikti / "derleme-macos.json").unlink()
        with self.assertRaises(SystemExit):
            self.y.yuklenecek_kurulumlar(self.cikti, self.d, True)
        (self.cikti / "derleme-macos.json").write_text(json.dumps(mac), encoding="utf-8")
        kayit, _ = self.sahte_github()
        with contextlib.redirect_stdout(io.StringIO()):
            self.y.yayimla("o/r", "v9.9.9", self.d, False, public=True)
        govde = next(v for y, u, v in kayit if y == "POST" and u == "R")["body"]
        self.assertIn("Windows ArthurLegal-Kurulum.exe · macOS ArthurLegal-Kurulum.pkg", govde)
        yuklenen = [u.split("=", 1)[1] for y, u, v in kayit if y == "POST" and u.startswith("U?")]
        self.assertLess(yuklenen.index(pkg.name), yuklenen.index("arthurlegal-manifest.json"), "manifest en son")


class GuncelleyiciTesti(unittest.TestCase):
    def hazirla(self, t: Path, kurcala=None, tohum=TEST_TOHUM, anahtarlar=None):
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
        (yayin / "arthurlegal-manifest.sig").write_text(ed25519.sign(tohum, ham).hex(), encoding="ascii")
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
        sahte_kok(t / "kok", manifest=url + "/arthurlegal-manifest.json", anahtarlar=anahtarlar)
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

    def test_kasa_anahtariyla_imzali_paket_kurulur(self):
        """Günlük anahtar kaybolursa yayın kasadaki yedekle imzalanır; güvenilen liste çalışan paketten gelir."""
        liste = [ed25519.public_key(TEST_TOHUM).hex(), ed25519.public_key(KASA_TOHUM).hex()]
        with tempfile.TemporaryDirectory() as t:
            r, aktif = self.hazirla(Path(t), tohum=KASA_TOHUM, anahtarlar=liste)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertEqual(aktif, "0.0.2")

    def test_listede_olmayan_anahtar_reddedilir(self):
        liste = [ed25519.public_key(TEST_TOHUM).hex(), ed25519.public_key(KASA_TOHUM).hex()]
        with tempfile.TemporaryDirectory() as t:
            r, aktif = self.hazirla(Path(t), tohum=YABANCI_TOHUM, anahtarlar=liste)
            self.assertIn("imza", r.stdout)
            self.assertEqual(aktif, "")

    def test_paketteki_liste_eski_anahtarin_yerine_gecer(self):
        """Anahtar değişikliği güncellemeyle yayılır: listede olmayan eski anahtar (ayar.json'daki) artık geçmez."""
        with tempfile.TemporaryDirectory() as t:
            r, aktif = self.hazirla(Path(t), tohum=TEST_TOHUM, anahtarlar=[ed25519.public_key(KASA_TOHUM).hex()])
            self.assertIn("imza", r.stdout)
            self.assertEqual(aktif, "")

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


class YayinAnahtariTesti(unittest.TestCase):
    """yayinla.py: kasa anahtarının üretimi ve onunla imza. Ağa çıkmaz (--kuru); gerçek anahtarlara dokunmaz."""

    def setUp(self):
        sys.path.insert(0, str(BURASI / "yayin"))
        import yayinla
        self.y = yayinla
        self.t = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.t, True)
        eski = {a: getattr(yayinla, a) for a in ("BURASI", "CIKTI", "ANAHTAR", "KASA")}
        self.addCleanup(lambda: [setattr(yayinla, a, d) for a, d in eski.items()])
        yayinla.BURASI, yayinla.CIKTI = self.t, self.t / "cikti"
        yayinla.ANAHTAR = self.t / "imza" / "yayin_anahtari.hex"
        yayinla.KASA = self.t / "imza" / "kasa_anahtari.hex"
        (self.t / "kaynaklar.json").write_text(json.dumps({"surum": "9.9.9", "yayin_deposu": "x/y",
                                                           "yayin_anahtari": "", "dallar": {}}), encoding="utf-8")

    def derleme_yaz(self, anahtarlar):
        (self.t / "cikti").mkdir(exist_ok=True)
        (self.t / "cikti" / "derleme.json").write_text(json.dumps({
            "surum": "9.9.9", "icerik": {}, "mask": {}, "paket": {"dosya": "p.zip", "sha256": "0" * 64},
            "anahtarlar": anahtarlar}), encoding="utf-8")

    def test_kasa_anahtari_uretilir_ve_kasayla_imzalanir(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.y.anahtar_uret()
            self.y.anahtar_uret(kasa=True)
        k = json.loads((self.t / "kaynaklar.json").read_text(encoding="utf-8"))
        self.assertEqual(list(k).index("kasa_anahtari"), list(k).index("yayin_anahtari") + 1)
        with self.assertRaises(SystemExit):  # var olan kasa anahtarı sessizce yenilenmez
            self.y.anahtar_uret(kasa=True)
        self.derleme_yaz([k["yayin_anahtari"], k["kasa_anahtari"]])
        with contextlib.redirect_stdout(io.StringIO()):
            self.y.main(["v9.9.9", "--kuru", "--kasa"])
        ham = (self.t / "cikti" / "arthurlegal-manifest.json").read_bytes()
        imza = bytes.fromhex((self.t / "cikti" / "arthurlegal-manifest.sig").read_text(encoding="ascii"))
        self.assertTrue(ed25519.verify(bytes.fromhex(k["kasa_anahtari"]), ham, imza))
        self.assertFalse(ed25519.verify(bytes.fromhex(k["yayin_anahtari"]), ham, imza))

    def test_paketin_tanimadigi_anahtarla_imzalanmaz(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.y.anahtar_uret()
        self.derleme_yaz(["0" * 64])
        with self.assertRaises(SystemExit):
            self.y.main(["v9.9.9", "--kuru"])


def dort_paket(kok: Path, surum="0.0.1"):
    """sahte_kok'a Kurumsal, Courthouse ve Akademisyen paketlerini ekler (genel derlemede dördü de var)."""
    s = kok / "surumler" / surum
    for profil, dosya in (("kurumsal", "company-profile.md"), ("adliye", "mahkeme-profili.md"),
                          ("akademisyen", "akademisyen-profili.md")):
        p = s / "paketler" / profil
        (p / "knowledge").mkdir(parents=True)
        (p / "SYSTEM_PROMPT.md").write_text(f"# SİSTEM\n{profil} talimatı.", encoding="utf-8")
        (p / "knowledge" / dosya).write_text(f"# {profil} profili — [DOLDUR]", encoding="utf-8")
    (s / "paketler" / "adliye" / "knowledge" / "profiles").mkdir()
    (s / "paketler" / "adliye" / "knowledge" / "profiles" / "asliye-hukuk.md").write_text("# Asliye Hukuk", encoding="utf-8")
    (s / "icerik.json").write_text(json.dumps({"paketler": {"hukuk-burosu": "1.10.1", "kurumsal": "1.10.1",
                                                            "adliye": "1.2.0", "akademisyen": "1.1.1"},
                                               "bilesenler": {"tapu": "0.5.2"}}), encoding="utf-8")


def secim_yaz(kok: Path, *moduller):
    (kok / "moduller.json").write_text(json.dumps({"moduller": list(moduller)}), encoding="utf-8")


class ModulTesti(unittest.TestCase):
    """2.5.0: tek kurulum dosyası, modül ekranı. Seçim kurulum klasöründeki moduller.json'dadır; kısayollar, Claude
    kaydı, paketler, proje klasörleri ve Arthur Mask indirmesi ona uyar. Seçim dosyası olmayan (2.5.0 öncesi) kurulum
    eski modülleriyle sürer."""

    def calistir(self, t, kod, kontrol=True):
        tam = f"import sys, json; sys.path.insert(0, r'{t / 'kok'}/surumler/0.0.1/istemci'); {kod}"
        env = {**ENV, "APPDATA": str(t / "Roaming"), "LOCALAPPDATA": str(t / "Local"), "USERPROFILE": str(t / "ev"),
               "HOME": str(t / "ev"), "ARTHURLEGAL_PROJE_KOKU": str(t / "projeler")}
        r = subprocess.run([sys.executable, "-c", tam], env=env, capture_output=True, text=True, encoding="utf-8",
                           check=kontrol)
        return json.loads(r.stdout.strip().splitlines()[-1]) if kontrol else r

    def kok(self, t, *moduller):
        sahte_kok(t / "kok")
        dort_paket(t / "kok")
        if moduller:
            secim_yaz(t / "kok", *moduller)

    def test_secim_dogrulanir_ve_siralanir(self):
        import ortak
        self.assertEqual(ortak.secim_coz(" Mask, tapu;ADLIYE "), ["adliye", "tapu", "mask"])
        for kotu in ("tapu,mask", "", "adliye,uyap", "courthouse"):
            with self.subTest(kotu=kotu), self.assertRaises(ValueError):
                ortak.secim_coz(kotu)
        self.assertEqual(ortak.MODULLER, ("hukuk-burosu", "kurumsal", "adliye", "akademisyen", "tapu", "mask"))

    def test_secim_dosyasi_yoksa_eski_modullerle_surer(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t)
            kod = "import ortak; print(json.dumps(ortak.moduller()))"
            self.assertEqual(self.calistir(t, kod), ["hukuk-burosu", "kurumsal", "tapu", "mask"])
            (t / "kok" / "moduller.json").write_text("bozuk", encoding="utf-8")
            self.assertEqual(self.calistir(t, kod), ["hukuk-burosu", "kurumsal", "tapu", "mask"])
            self.assertEqual(self.calistir(t, "import kur; print(kur.main(['--kaydet', '--moduller', 'mask,adliye']))"), 0)
            self.assertEqual(json.loads((t / "kok" / "moduller.json").read_text(encoding="utf-8")),
                             {"moduller": ["adliye", "mask"]})
            r = self.calistir(t, "import kur; print(kur.main(['--kaydet', '--moduller', 'tapu']))")
            self.assertEqual(r, 2, "paket seçilmemiş: kurulum durur")
            self.assertEqual(self.calistir(t, kod), ["adliye", "mask"], "geçersiz seçim öncekini bozmaz")

    @SADECE_WINDOWS
    def test_courthouse_tapu_mask_simgeleri(self):
        """Kullanıcının istediği: masaüstünde Courthouse, Tapu ve (Arthur Mask'in kendi kurulumundan) Mask simgesi."""
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "adliye", "tapu", "mask")
            liste = self.calistir(t, KisayolTesti.LISTE)
            adlar = sorted({s[0] for s in liste})
            self.assertIn("ArthurLegal - Courthouse 0.0.1.lnk", adlar)
            self.assertIn("ArthurLegal - Tapu 0.0.1.lnk", adlar)
            self.assertNotIn("ArthurLegal 0.0.1.lnk", adlar, "Hukuk Bürosu ve Kurumsal seçilmedi: ana simge yok")
            self.assertFalse([a for a in adlar if "Akademisyen" in a])
            courthouse = [s for s in liste if s[0] == "ArthurLegal - Courthouse 0.0.1.lnk"]
            self.assertEqual(len(courthouse), 2, "masaüstü ve Başlat menüsü")
            self.assertTrue(all(s[2].endswith("kisayol baslat adliye") for s in courthouse))
            masa = self.calistir(t, "import kur; print(json.dumps(sorted(y.name for y, *_ in kur._kisayol_listesi() "
                                    "if y.parent == kur._masaustu())))")
            self.assertEqual(masa, ["ArthurLegal - Courthouse 0.0.1.lnk", "ArthurLegal - Tapu 0.0.1.lnk"],
                             "Arthur Mask simgesini Arthur Mask'in kendi kurulumu koyar")

    @SADECE_WINDOWS
    def test_paket_simgeleri_ve_secimden_cikan_temizlenir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "hukuk-burosu", "adliye", "akademisyen")
            adlar = {s[0] for s in self.calistir(t, KisayolTesti.LISTE)}
            for ad in ("ArthurLegal 0.0.1.lnk", "ArthurLegal - Courthouse 0.0.1.lnk", "ArthurLegal - Akademisyen 0.0.1.lnk"):
                self.assertIn(ad, adlar)
            self.assertFalse([a for a in adlar if "Tapu" in a], "Tapu seçilmedi")
            self.calistir(t, "import kur; print(kur.main(['--kaydet', '--dil', 'en']))")
            adlar = {s[0] for s in self.calistir(t, KisayolTesti.LISTE)}
            self.assertIn("ArthurLegal - Academician 0.0.1.lnk", adlar)
            self.assertIn("ArthurLegal - Courthouse 0.0.1.lnk", adlar, "Courthouse özel ad, çevrilmez")
            # Courthouse seçimden çıkınca simgesi gider; kullanıcının başka kısayolu kalır.
            masa = t / "ev" / "Desktop"
            masa.mkdir(parents=True)
            for ad in ("ArthurLegal - Courthouse 0.0.1.lnk", "ArthurLegal - Academician 0.0.1.lnk", "Başka Program.lnk"):
                (masa / ad).write_bytes(b"")
            secim_yaz(t / "kok", "hukuk-burosu", "akademisyen")
            self.calistir(t, "import kur; kur.eski_kisayollari_temizle(kur._menu(), {y for y, *_ in "
                             "kur._kisayol_listesi()}); print(1)")
            self.assertEqual(sorted(p.name for p in masa.iterdir()),
                             ["ArthurLegal - Academician 0.0.1.lnk", "Başka Program.lnk"])

    @SADECE_WINDOWS
    def test_tapu_yalniz_secilirse_kaydedilir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "adliye", "tapu")
            yapi = t / "Roaming" / "Claude" / "claude_desktop_config.json"
            yapi.parent.mkdir(parents=True)
            yapi.write_text(json.dumps({"mcpServers": {"arthur-mask": {"command": "m"}}}), encoding="utf-8")
            kod = "import claude_ayari; claude_ayari.kaydet(); print(1)"
            self.calistir(t, kod)
            self.assertEqual(set(json.loads(yapi.read_text(encoding="utf-8"))["mcpServers"]),
                             {"arthur-mask", "arthurlegal-yerel", "arthur-tapu"})
            secim_yaz(t / "kok", "adliye")
            self.calistir(t, kod)
            self.assertEqual(set(json.loads(yapi.read_text(encoding="utf-8"))["mcpServers"]),
                             {"arthur-mask", "arthurlegal-yerel"}, "seçimden çıkan Tapu'nun kaydı silinir")
            self.assertEqual(self.calistir(t, "import kisayol; print(json.dumps(kisayol.tapu()))"), 1)

    def test_sunucu_yalniz_secilen_paketleri_sunar(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "adliye", "mask")
            kod = ("import arthurlegal_sunucu as s, ortak; b = s.Bilgi(ortak.SURUM_DIZINI, ortak.FIRMA); "
                   "p = b.profil(None); a = s.yerel_araclar(b.profiller(), b.varsayilan()); "
                   "print(json.dumps([b.profiller(), p, b.talimat(p), a[0]['inputSchema']['properties']['profil']['enum'], "
                   "a[0]['description']]))")
            profiller, varsayilan, talimat, secenek, aciklama = self.calistir(t, kod)
            self.assertEqual((profiller, varsayilan, secenek), (["adliye"], "adliye", ["adliye"]),
                             "yalnız Courthouse seçilmiş: varsayılan Courthouse")
            self.assertTrue(talimat.startswith("# ArthurLegal — oturum talimatı: Courthouse (Adliye)"))
            self.assertIn("knowledge/mahkeme-profili.md", talimat)
            self.assertIn("knowledge/profiles/", talimat)
            self.assertIn("UYARI: veri çekilemedi, teyidiniz gerekli: https://parselsorgu.tkgm.gov.tr/", talimat,
                          "Tapu seçilmedi: parsel bilgisi uydurulmaz")
            self.assertNotIn("`arthur-tapu` yerel araçlarını kullan", talimat)
            self.assertIn("dosya belgesi (UYAP UDF dâhil)", talimat)
            self.assertNotIn("müvekkil belgesi", aciklama)
            self.assertIn("gerekçeli karar", aciklama)
            r = self.calistir(t, "import arthurlegal_sunucu as s, ortak; b = s.Bilgi(ortak.SURUM_DIZINI, ortak.FIRMA); "
                                 "b.profil('hukuk-burosu')", kontrol=False)
            self.assertIn("Bu kurulumda olmayan profil", r.stderr)
            # Birden çok paket: varsayılan Hukuk Bürosu; talimat öteki paketleri ve ne zaman seçileceklerini söyler.
            secim_yaz(t / "kok", "hukuk-burosu", "adliye", "akademisyen", "tapu")
            profiller, varsayilan, talimat, secenek, aciklama = self.calistir(t, kod)
            self.assertEqual(varsayilan, "hukuk-burosu")
            self.assertEqual(secenek, ["hukuk-burosu", "adliye", "akademisyen"])
            self.assertIn("`adliye` = hâkim ve kalem", talimat)
            self.assertIn("`arthur-tapu` yerel araçlarını kullan", talimat)
            self.assertIn('profil="akademisyen"', aciklama)
            akademisyen = self.calistir(t, "import arthurlegal_sunucu as s, ortak; b = s.Bilgi(ortak.SURUM_DIZINI, "
                                           "ortak.FIRMA); print(json.dumps(b.talimat('akademisyen')))")
            self.assertIn("knowledge/akademisyen-profili.md", akademisyen)
            self.assertIn("maskeli olsa bile sohbete alınmaz", akademisyen)

    def test_secimden_cikan_paketin_proje_klasoru_bosaltilir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "hukuk-burosu", "adliye")
            self.assertEqual(self.calistir(t, "import proje; print(len(proje.esitle()))"), 2)
            courthouse = t / "projeler" / "Courthouse"
            self.assertIn('profil="adliye"', (courthouse / "CLAUDE.md").read_text(encoding="utf-8"))
            self.assertTrue((courthouse / "knowledge" / "profiles" / "asliye-hukuk.md").exists())
            self.assertFalse((t / "projeler" / "Akademisyen").exists(), "seçilmeyen paketin klasörü açılmaz")
            (courthouse / "calismalar" / "taslak.md").write_text("hâkimin taslağı", encoding="utf-8")
            secim_yaz(t / "kok", "hukuk-burosu")
            self.calistir(t, "import proje; proje.esitle(); print(1)")
            self.assertFalse((courthouse / "SYSTEM_PROMPT.md").exists())
            self.assertFalse((courthouse / "knowledge").exists())
            self.assertTrue((courthouse / "calismalar" / "taslak.md").exists(), "kullanıcının dosyası kalır")
            self.assertEqual(list(self.calistir(t, "import proje; print(json.dumps(proje.durum()))")), ["hukuk-burosu"])

    @SADECE_WINDOWS
    def test_mask_secilmediyse_indirilmez(self):
        import guncelle
        import ortak
        eski = (ortak.moduller, ortak.mask_surumu, ortak.indir, ortak.akilli_denetim_acik, ortak.VERI)
        try:
            def indir(*a, **k):
                raise AssertionError("indirilmemeliydi")
            ortak.VERI = Path(tempfile.mkdtemp())
            ortak.indir, ortak.akilli_denetim_acik = indir, lambda: False
            ortak.moduller, ortak.mask_surumu = (lambda: ["adliye"]), (lambda: None)
            manifest = {"mask": {"surum": "1.0.0", "url": "https://ornek.invalid/m.exe", "sha256": "0" * 64}}
            self.assertEqual(guncelle.mask_guncelle(manifest), "mask: kurulumda seçilmedi")
            ortak.mask_surumu = lambda: "0.9.0"  # kendi kurulumuyla gelmiş eski Arthur Mask güncellenir
            with self.assertRaises(AssertionError):
                guncelle.mask_guncelle(manifest)
        finally:
            shutil.rmtree(ortak.VERI, ignore_errors=True)
            ortak.moduller, ortak.mask_surumu, ortak.indir, ortak.akilli_denetim_acik, ortak.VERI = eski

    def test_zip_kurulumu_modulleri_sorar(self):
        import kur
        cevaplar = iter(["", "6", "5", "3,5"])
        with contextlib.redirect_stdout(io.StringIO()) as cikti:
            self.assertEqual(kur.zip_secimi("tr", None, lambda _: next(cevaplar)), ["adliye", "tapu"])
        self.assertIn("Arthur Mask bu yolla kurulamaz", cikti.getvalue())
        self.assertEqual(cikti.getvalue().count("en az biri olmalı"), 3, "boş, liste dışı ve paketsiz cevap reddedilir")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(kur.zip_secimi("en", ["adliye", "mask"], lambda _: ""), ["adliye"], "Enter: önceki seçim")

            def kapali(_):
                raise EOFError
            self.assertEqual(kur.zip_secimi("tr", None, kapali), ["hukuk-burosu", "kurumsal", "tapu"])
        self.assertEqual(list(kur.MODUL_METNI["tr"]), list(kur.ortak.MODULLER))

    def test_baslangic_sayfasi_dort_paket_karti(self):
        sys.path.insert(0, str(BURASI / "yayin"))
        import derle
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            icerik = {"surum": "0.0.1", "paketler": {"hukuk-burosu": "1", "kurumsal": "1", "adliye": "1", "akademisyen": "1"}}
            derle.rehber_yaz(t, "", icerik)
            for sayfa, metin in (("baslangic.html", "Sen ArthurLegal Courthouse (Adliye) asistanısın"),
                                 ("baslangic-en.html", "You are the ArthurLegal Courthouse assistant")):
                html = (t / "rehber" / sayfa).read_text(encoding="utf-8")
                self.assertNotIn("{{", html)
                self.assertIn(metin, html)
                for profil in ("hukuk-burosu", "kurumsal", "adliye", "akademisyen"):
                    self.assertEqual(html.count(f'<div class="kart" data-modul="{profil}">'), 2,
                                     "paket kartı ve talimat kartı; sayfa seçilmeyeni gizler")
                self.assertIn('data-modul="tapu"', html)
                self.assertIn("d.moduller", html)
            self.assertIn("3,5", derle.ZIP_BENIOKU)

    def test_kurulum_betigi_modul_ekrani(self):
        import re
        iss = (BURASI / "kurulum" / "ArthurLegal.iss").read_text(encoding="utf-8-sig")
        self.assertIn("CreateCustomPage(wpLicense", iss, "modül ekranı lisanstan sonra")
        self.assertIn("{param:MODULLER|}", iss)
        self.assertIn("SetPreviousData(PreviousDataKey, 'Moduller', Secim)", iss)
        self.assertIn("ActiveLanguage + ' --moduller ' + Secim", iss)
        self.assertIn("ESKI_SECIM = 'hukuk-burosu,kurumsal,tapu,mask'", iss)
        tanimli = {dil: set(re.findall(rf"^{dil}\.(\w+)=", iss, re.M)) for dil in ("en", "tr")}
        kodlar = re.findall(r"\d: Result := '(\w+)';|else\s+Result := '(Modul\w+)';", iss)
        iletiler = {a or b for a, b in kodlar if (a or b).startswith("Modul")}
        self.assertEqual(len(iletiler), 6)
        for ileti in iletiler:  # CustomMessage(ModulIletisi(I)) ve ... + 'Aciklama' çalışırken çözülür
            for dil in ("en", "tr"):
                self.assertIn(ileti, tanimli[dil])
                self.assertIn(ileti + "Aciklama", tanimli[dil])
        import ortak
        sira = re.findall(r"\d: Result := '([a-z-]+)';", iss) + ["mask"]
        self.assertEqual(tuple(sira), ortak.MODULLER, "Pascal ve Python aynı sırada")


class MacKurulumTesti(unittest.TestCase):
    """macOS kurulumu (.pkg, yayin/derle_macos.py): paketler, istemci ve güncelleme kanalı Windows'takiyle aynı; değişen
    yalnız işletim sistemine bağlanan yerler (Python yolu, Claude ayar dosyası, uygulamalar ve masaüstü takma adları,
    LaunchAgent, Arthur Mask). İşletim sisteminden bağımsız kısımlar her bilgisayarda ortak.MAC = True ile sınanır;
    sembolik bağ ve sh isteyenler yalnız macOS'ta (GitHub Actions: .github/workflows/macos-kurulum.yml)."""

    # (yol, hedef, argüman): ev klasörünün altındakiler ev klasörüne göre, öteki yollar POSIX biçiminde.
    LISTE = ("import kur; ev = Path.home(); g = lambda p: Path(p).relative_to(ev).as_posix() "
             "if Path(p).is_relative_to(ev) else Path(p).as_posix(); "
             "print(json.dumps([[g(y), g(h), a] for y, h, a, _ in kur._kisayol_listesi()]))")

    def calistir(self, t, kod):
        tam = (f"import sys, json; from pathlib import Path; sys.path.insert(0, r'{t / 'kok'}/surumler/0.0.1/istemci'); "
               f"import ortak; ortak.MAC = True; {kod}")
        env = {**ENV, "HOME": str(t / "ev"), "USERPROFILE": str(t / "ev"), "ARTHURLEGAL_PROJE_KOKU": str(t / "projeler")}
        r = subprocess.run([sys.executable, "-c", tam], env=env, capture_output=True, text=True, encoding="utf-8")
        if r.returncode:
            self.fail(r.stdout + r.stderr)
        return json.loads(r.stdout.strip().splitlines()[-1])

    def kok(self, t, *moduller):
        sahte_kok(t / "kok")
        dort_paket(t / "kok")
        (t / "ev").mkdir()
        if moduller:
            secim_yaz(t / "kok", *moduller)

    def test_simgeler_uygulamalar_ve_masaustu_takma_adlari(self):
        """İstenen: masaüstünde Courthouse, Tapu ve Mask simgeleri. macOS'ta paket ve Tapu simgeleri ~/Applications'ta
        uygulamadır (Launchpad, Spotlight), masaüstünde takma adları durur; adlar sürüm taşımaz."""
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "adliye", "tapu", "mask")
            py = ((t / "kok").resolve() / "runtime" / "bin" / "python3").as_posix()
            liste = {y: (h, a) for y, h, a in self.calistir(t, self.LISTE)}
            liste.pop("Desktop/Arthur Mask.app", None)  # bu Mac'te /Applications'ta kurulu bir Arthur Mask varsa
            self.assertEqual(sorted(y for y in liste if not y.startswith("Applications/ArthurLegal/")),
                             ["Applications/ArthurLegal Courthouse.app", "Applications/ArthurLegal Tapu.app",
                              "Desktop/ArthurLegal Courthouse.app", "Desktop/ArthurLegal Tapu.app"],
                             "Hukuk Bürosu ve Kurumsal seçilmedi: ana simge yok")
            hedef, arg = liste["Applications/ArthurLegal Courthouse.app"]
            self.assertEqual(hedef, py)
            self.assertTrue(arg.startswith("-B ") and arg.endswith("kisayol baslat adliye"), arg)
            self.assertTrue(liste["Applications/ArthurLegal Tapu.app"][1].endswith("kisayol tapu"))
            self.assertEqual(liste["Desktop/ArthurLegal Courthouse.app"], ("Applications/ArthurLegal Courthouse.app", ""))
            yardimci = {y.rsplit("/", 1)[1]: h for y, (h, a) in liste.items() if y.startswith("Applications/ArthurLegal/")}
            self.assertEqual(sorted(yardimci), ["ArthurLegal'i Kaldır.app", "Başlangıç Rehberi.app",
                                                "Güncellemeleri Denetle.app", "Proje Klasörleri.app"])
            self.assertEqual((yardimci["Başlangıç Rehberi.app"], yardimci["ArthurLegal'i Kaldır.app"],
                              yardimci["Güncellemeleri Denetle.app"]), ("/usr/bin/open", "/bin/sh", py))
            # Arthur Mask kuruluysa ve seçildiyse masaüstünde onun da takma adı olur.
            if not Path("/Applications/Arthur Mask.app").exists():
                self.assertNotIn("Desktop/Arthur Mask.app", [y for y, *_ in self.calistir(t, self.LISTE)],
                                 "Arthur Mask kurulu değil")
            mask = t / "ev" / "Applications" / "Arthur Mask.app" / "Contents" / "Resources" / "runtime" / "bin"
            mask.mkdir(parents=True)
            (mask / "python3").write_bytes(b"")
            liste = {y: (h, a) for y, h, a in self.calistir(t, self.LISTE)}
            self.assertTrue(liste["Desktop/Arthur Mask.app"][0].endswith("Applications/Arthur Mask.app"))
            secim_yaz(t / "kok", "adliye", "tapu")
            self.assertNotIn("Desktop/Arthur Mask.app", [y for y, *_ in self.calistir(t, self.LISTE)], "Mask seçilmedi")
            # Ana simge (Hukuk Bürosu), İngilizce adlar; seçilmeyen Tapu ve Courthouse yok.
            secim_yaz(t / "kok", "hukuk-burosu", "akademisyen")
            self.calistir(t, "ortak.durum_guncelle(dil='en'); print(1)")
            adlar = [y for y, *_ in self.calistir(t, self.LISTE)]
            for ad in ("Applications/ArthurLegal.app", "Desktop/ArthurLegal.app", "Applications/ArthurLegal Academician.app",
                       "Applications/ArthurLegal/Start Guide.app", "Applications/ArthurLegal/Uninstall ArthurLegal.app"):
                self.assertIn(ad, adlar)
            self.assertFalse([a for a in adlar if "Tapu" in a or "Courthouse" in a])
            durum = self.calistir(t, "import kisayol; y = kisayol.durum_yaz('kurulu'); "
                                     "print(y.read_text(encoding='utf-8').split('=', 1)[1].strip().rstrip(';'))")
            self.assertEqual(durum["isletim"], "mac", "başlangıç sayfası Mac'e özgü cümleleri gösterir")

    def test_uygulama_yazilir_kullanicinin_uygulamasina_dokunulmaz(self):
        import plistlib
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "adliye")
            kod = ("import mac, plistlib; app = mac.uygulamalar() / 'ArthurLegal Courthouse.app'; "
                   "mac.uygulama_yaz(app, Path('/k/runtime/bin/python3'), '-B /k/bin/al.py kisayol baslat adliye', "
                   "'Courthouse', '0.0.1', None); "
                   "b = plistlib.loads((app / 'Contents' / 'Info.plist').read_bytes()); "
                   "betik = (app / 'Contents' / 'MacOS' / 'arthurlegal').read_text(encoding='utf-8'); "
                   "print(json.dumps([b, betik, mac.bizim_mi(app), mac.surumu(app), "
                   "mac.eski_surumlu_kisayol_var([(app, 0, 0, 0)], '0.0.1'), "
                   "mac.eski_surumlu_kisayol_var([(app, 0, 0, 0)], '0.0.2')]))")
            bilgi, betik, bizim, surum, ayni, eski = self.calistir(t, kod)
            self.assertTrue(bilgi["CFBundleIdentifier"].startswith("com.arthurlegal.kisayol."))
            self.assertEqual((bilgi["CFBundleExecutable"], bilgi["CFBundleShortVersionString"], bilgi["LSUIElement"]),
                             ("arthurlegal", "0.0.1", True), "Dock'ta simge açmaz; sürüm uygulamanın bilgisinde")
            self.assertTrue(betik.startswith("#!/bin/sh\n"))
            self.assertIn(" -B /k/bin/al.py kisayol baslat adliye >/dev/null 2>&1\n", betik)
            self.assertEqual((bizim, surum, ayni, eski), (True, "0.0.1", False, True))
            uyg = t / "ev" / "Applications"
            if os.name == "posix":
                self.assertTrue(os.access(uyg / "ArthurLegal Courthouse.app" / "Contents" / "MacOS" / "arthurlegal", os.X_OK))
            # Kullanıcının aynı adlı uygulaması: üzerine yazılmaz, yanına kopya kalmaz.
            kendi = uyg / "ArthurLegal Tapu.app" / "Contents"
            kendi.mkdir(parents=True)
            (kendi / "Info.plist").write_bytes(plistlib.dumps({"CFBundleIdentifier": "com.ornek.tapu"}))
            self.calistir(t, "import mac; mac.uygulama_yaz(mac.uygulamalar() / 'ArthurLegal Tapu.app', Path('/k/py'), 'x', "
                             "'Tapu', '0.0.1', None); print(1)")
            self.assertEqual(plistlib.loads((kendi / "Info.plist").read_bytes())["CFBundleIdentifier"], "com.ornek.tapu")
            self.assertEqual(sorted(p.name for p in uyg.iterdir()), ["ArthurLegal Courthouse.app", "ArthurLegal Tapu.app"])

    @unittest.skipUnless(MACOS, "sembolik bağ ve sh: macOS")
    def test_kisayollar_yazilir_secimden_cikan_silinir(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "adliye", "tapu")
            ev, kok = t / "ev", t / "kok"
            masa, uyg = ev / "Desktop", ev / "Applications"
            masa.mkdir()
            (masa / "Başka Program.app").mkdir()                              # kullanıcının gerçek klasörü
            os.symlink("/System/Applications/Notes.app", masa / "Notlar.app")  # kullanıcının takma adı
            self.calistir(t, "import kur; kur.kisayollar_yaz(); print(1)")
            self.assertTrue((uyg / "ArthurLegal Courthouse.app" / "Contents" / "MacOS" / "arthurlegal").exists())
            self.assertEqual(os.readlink(masa / "ArthurLegal Courthouse.app"), str(uyg / "ArthurLegal Courthouse.app"))
            self.assertTrue((uyg / "ArthurLegal" / "ArthurLegal'i Kaldır.app").is_dir())
            kaldir = kok / "KALDIR.command"
            self.assertTrue(os.access(kaldir, os.X_OK))
            self.assertEqual(subprocess.run(["sh", "-n", str(kaldir)]).returncode, 0)
            self.assertEqual(subprocess.run(["bash", "-n", str(BURASI / "kurulum" / "macos" / "postinstall")]).returncode, 0)
            # Courthouse seçimden çıkar, Hukuk Bürosu girer: eski uygulama ve takma adı gider, kullanıcınınkiler kalır.
            secim_yaz(kok, "hukuk-burosu", "tapu")
            self.calistir(t, "import kur; kur.kisayollar_yaz(); print(1)")
            self.assertFalse((uyg / "ArthurLegal Courthouse.app").exists())
            self.assertEqual(sorted(p.name for p in masa.iterdir()),
                             ["ArthurLegal Tapu.app", "ArthurLegal.app", "Başka Program.app", "Notlar.app"])
            self.calistir(t, "import kur; kur.kisayollar_sil(); print(1)")
            self.assertEqual(sorted(p.name for p in masa.iterdir()), ["Başka Program.app", "Notlar.app"])
            self.assertEqual(sorted(p.name for p in uyg.iterdir()), [])

    def test_oturum_acilisi_ajani(self):
        """Windows'taki Run anahtarının karşılığı: LaunchAgent oturum açılışında ve altı saatte bir sessiz günceller."""
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "adliye")
            kod = ("import mac, os, plistlib; os.getuid = getattr(os, 'getuid', lambda: 501); c = []; "
                   "mac.subprocess.run = lambda a, **k: c.append(a) or type('R', (), {'returncode': 0, 'stderr': ''})(); "
                   "mac.ajan(True, Path('/k/runtime/bin/python3'), Path('/k/bin/al.py')); "
                   "p = plistlib.loads(mac.ajan_yolu().read_bytes()); "
                   "mac.ajan(False, Path('/k/runtime/bin/python3'), Path('/k/bin/al.py')); "
                   "print(json.dumps([p, c, mac.ajan_yolu().exists(), os.getuid()]))")
            plist, komutlar, kaldi, uid = self.calistir(t, kod)
            self.assertEqual(plist["Label"], "com.arthurlegal.guncelleme")
            self.assertEqual((plist["ProgramArguments"][1], plist["ProgramArguments"][-2:]), ("-B", ["guncelle", "--sessiz"]))
            self.assertEqual((plist["RunAtLoad"], plist["StartInterval"]), (True, 6 * 3600))
            self.assertEqual([k[:2] for k in komutlar], [["launchctl", "bootout"], ["launchctl", "bootstrap"],
                                                         ["launchctl", "bootout"]])
            self.assertEqual(komutlar[1][2], f"gui/{uid}")
            self.assertFalse(kaldi, "kaldırmada ajan dosyası silinir")

    def test_claude_ayari_mac_yolunda(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            self.kok(t, "adliye", "tapu")
            kod = "import claude_ayari; print(json.dumps([str(y) for y in claude_ayari.kaydet()]))"
            yapi = t / "ev" / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
            self.assertEqual([Path(y).resolve() for y in self.calistir(t, kod)], [yapi.resolve()],
                             "Claude Desktop henüz açılmamış olsa da yazılır")
            sunucular = json.loads(yapi.read_text(encoding="utf-8"))["mcpServers"]
            self.assertEqual(set(sunucular), {"arthurlegal-yerel", "arthur-tapu"})
            self.assertEqual(Path(sunucular["arthurlegal-yerel"]["command"]).resolve(),
                             (t / "kok" / "runtime" / "bin" / "python3").resolve())
            self.assertEqual(sunucular["arthurlegal-yerel"]["args"][-1], "sunucu")
            secim_yaz(t / "kok", "adliye")
            self.calistir(t, kod)
            self.assertEqual(set(json.loads(yapi.read_text(encoding="utf-8"))["mcpServers"]), {"arthurlegal-yerel"},
                             "seçimden çıkan Tapu'nun kaydı silinir")

    def test_arthur_mask_mac_kosullari(self):
        """Mac'te Arthur Mask'i güncelleyici ilk kez kurar: yalnız seçildiyse, Apple Silicon ve macOS 14'te, manifestte
        macOS disk görüntüsü varsa ve sha256'sı tutuyorsa. Kurulu Arthur Mask'in güncellemesine karışılmaz."""
        import platform
        import guncelle
        import ortak
        eski = (ortak.MAC, ortak.moduller, ortak.mask_surumu, ortak.indir, ortak.VERI, guncelle.subprocess.run)
        eski_mac_ver = platform.mac_ver
        t = Path(tempfile.mkdtemp())
        islemci, macos = ["1"], ["15.0"]
        try:
            platform.mac_ver = lambda *a: (macos[0], ("", "", ""), "arm64")
            def indir(url, hedef=None, **k):
                Path(hedef).parent.mkdir(parents=True, exist_ok=True)
                Path(hedef).write_bytes(b"bozuk")
                return "1" * 64
            ortak.MAC, ortak.VERI, ortak.indir = True, t, indir
            guncelle.subprocess.run = lambda a, **k: subprocess.CompletedProcess(a, 0, stdout=islemci[0] + "\n", stderr="")
            manifest = {"mask_macos": {"surum": "1.0.0", "url": "https://ornek.invalid/m.dmg", "sha256": "0" * 64}}
            ortak.mask_surumu, ortak.moduller = (lambda: "1.0.0"), (lambda: ["adliye", "mask"])
            self.assertTrue(guncelle.mask_guncelle(manifest).startswith("mask: kurulu (1.0.0)"))
            ortak.mask_surumu, ortak.moduller = (lambda: None), (lambda: ["adliye"])
            self.assertEqual(guncelle.mask_guncelle(manifest), "mask: kurulumda seçilmedi")
            ortak.moduller = lambda: ["adliye", "mask"]
            islemci[0] = "0"
            self.assertIn("yalnız Apple Silicon", guncelle.mask_guncelle(manifest))
            islemci[0], macos[0] = "1", "13.6"
            self.assertIn("macOS 14 (Sonoma)", guncelle.mask_guncelle(manifest))
            macos[0] = "14.0"
            self.assertEqual(guncelle.mask_guncelle({}), "mask: manifest'te macOS sürümü yok")
            with self.assertRaises(guncelle.GuncellemeHatasi):
                guncelle.mask_guncelle(manifest)
            self.assertEqual(list((t / "indirilen").iterdir()), [], "özeti tutmayan disk görüntüsü silinir")
        finally:
            ortak.MAC, ortak.moduller, ortak.mask_surumu, ortak.indir, ortak.VERI, guncelle.subprocess.run = eski
            platform.mac_ver = eski_mac_ver
            shutil.rmtree(t, ignore_errors=True)

    def test_kurulum_paketi_sihirbazi(self):
        """Distribution.xml: modül ekranı (Özelleştir) Windows sihirbazıyla aynı metinlerle; yalnız ev klasörüne kurulum;
        kur.py'yi çağıran 'son' bileşeni en son; Arthur Mask yalnız Apple Silicon ve macOS 14'te seçilebilir."""
        import xml.etree.ElementTree as ET
        sys.path.insert(0, str(BURASI / "yayin"))
        import derle_macos
        import ortak
        ileti = derle_macos.iletiler()
        self.assertEqual(set(ileti["tr"]), set(ileti["en"]))
        with tempfile.TemporaryDirectory() as t:
            yol = Path(t) / "Distribution.xml"
            moduller = list(ortak.MODULLER)
            derle_macos.dagitim_yaz(yol, "9.9.9", moduller)
            kok = ET.parse(yol).getroot()
            self.assertEqual(kok.find("options").get("customize"), "always")
            alan = kok.find("domains")
            self.assertEqual((alan.get("enable_currentUserHome"), alan.get("enable_localSystem"),
                              alan.get("enable_anywhere")), ("true", "false", "false"), "yönetici şifresi istemez")
            self.assertEqual([s.get("choice") for s in kok.find("choices-outline")], ["cekirdek", *moduller, "son"])
            secim = {c.get("id"): c for c in kok.findall("choice")}
            for m in moduller:
                for dil in ("tr", "en"):
                    self.assertIn(secim[m].get("title"), ileti[dil])
                    self.assertIn(secim[m].get("description"), ileti[dil])
                self.assertIn(f"onceki('{m}')", secim[m].get("start_selected"), "önceki seçim işaretli gelir")
            self.assertEqual(secim["mask"].get("start_enabled"), "mask_uygun()")
            self.assertEqual(secim["mask"].get("start_selected"), "onceki('mask') && mask_uygun()")
            self.assertIn("compareVersions(system.version.ProductVersion, '14.0')", kok.find("script").text)
            self.assertIn("Apple Silicon", ileti["tr"]["ModulMaskAciklama"], "Mac'teki koşul modül açıklamasında")
            self.assertTrue(all(p.get("auth") == "none" for p in kok.findall("pkg-ref") if p.text))
            strings = Path(t) / "Localizable.strings"
            derle_macos.strings_yaz(strings, {"A": 'tırnak " ve\nsatır'})
            self.assertIn(strings.read_bytes()[:2], (b"\xff\xfe", b"\xfe\xff"), "UTF-16")
            self.assertEqual(strings.read_bytes().decode("utf-16"), '"A" = "tırnak \\" ve\\nsatır";\n')
        son = (BURASI / "kurulum" / "macos" / "postinstall").read_text(encoding="utf-8")
        self.assertIn('kur --kurulum --kisayol --dil "$DIL" --moduller "$SECIM"', son)
        self.assertIn("{{PAKET_YOK_TR}}", son)
        self.assertIn("{{PAKET_YOK_EN}}", son)

    def test_kaldirma_betigi(self):
        from pathlib import PurePosixPath
        import mac
        metin = mac.kaldirma_betigi(PurePosixPath("/Users/a b/Library/Application Support/ArthurLegal"), 'Örnek "Büro"', "tr")
        self.assertIn("KOK='/Users/a b/Library/Application Support/ArthurLegal'", metin)
        self.assertIn('kur --kaldir\nrm -rf "$KOK"\n', metin)
        self.assertIn('Örnek \\"Büro\\"', metin, "AppleScript dizgesinde tırnak kaçışlı")
        self.assertIn("Kaldır", metin)
        self.assertIn("Uninstall", mac.kaldirma_betigi(PurePosixPath("/k"), "ArthurLegal", "en"))
        if MACOS:
            self.assertEqual(subprocess.run(["sh", "-n"], input=metin, text=True).returncode, 0)


if __name__ == "__main__":
    unittest.main()
