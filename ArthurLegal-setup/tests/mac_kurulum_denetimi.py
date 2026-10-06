"""macOS kurulumunun denetimi: ArthurLegal-Kurulum.pkg kurulduktan sonra bilgisayara bakar, eksik bir şey varsa
hata verir. GitHub Actions'ta (.github/workflows/macos-kurulum.yml) çalışır; Mac'te elle de çalıştırılabilir:

    python3 tests/mac_kurulum_denetimi.py adliye,tapu,mask            kurulumu denetler
    python3 tests/mac_kurulum_denetimi.py adliye,tapu,mask --mask     Arthur Mask'i kurar ve denetler (~1,2 GB indirir)
    python3 tests/mac_kurulum_denetimi.py adliye,tapu,mask --kaldir   kaldırır ve geride bir şey kalmadığını denetler

Denetlenenler: kurulum günlüğü, işlemciye uyan Python ve HTTPS, modül seçimi, Claude Desktop kaydı, uygulamalar ve
masaüstü takma adları, kaldırma betiği, oturum açılışı güncellemesi (LaunchAgent), başlangıç sayfası, Courthouse
simgesinin açtığı panel, yerel ArthurLegal sunucusu ve Tapu sunucusu (MCP el sıkışması ve araç listesi).
"""
from __future__ import annotations

import json
import os
import plistlib
import queue
import subprocess
import sys
import threading
import time
from pathlib import Path

EV = Path.home()
KOK = EV / "Library" / "Application Support" / "ArthurLegal"
PY = KOK / "runtime" / "bin" / "python3"
AL = KOK / "bin" / "al.py"
UYG = EV / "Applications"
MASA = EV / "Desktop"
CLAUDE = EV / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
AJAN = EV / "Library" / "LaunchAgents" / "com.arthurlegal.guncelleme.plist"
BURASI = Path(__file__).resolve().parents[1]
PAKETLER = ("hukuk-burosu", "kurumsal", "adliye", "akademisyen")

hatalar: list = []
uyarilar: list = []


def denetle(kosul, ileti: str, yalniz_uyari: bool = False) -> bool:
    print(("  tamam  " if kosul else ("  UYARI  " if yalniz_uyari else "  HATA   ")) + ileti, flush=True)
    if not kosul:
        (uyarilar if yalniz_uyari else hatalar).append(ileti)
    return bool(kosul)


def calistir(komut, zaman=120, **k) -> subprocess.CompletedProcess:
    return subprocess.run([str(x) for x in komut], capture_output=True, text=True, timeout=zaman, **k)


def kurulu_python(kod: str, zaman=120) -> str:
    """Kurulumun kendi Python'unda, kurulu istemciyle çalıştırır (kur, ortak, guncelle ...)."""
    istemci = KOK / "surumler" / (KOK / "aktif.txt").read_text(encoding="utf-8").strip() / "istemci"
    r = calistir([PY, "-B", "-c", f"import sys, json; sys.path.insert(0, {str(istemci)!r}); {kod}"], zaman=zaman)
    if r.returncode:
        raise RuntimeError(r.stdout + r.stderr)
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""


class Sunucu:
    """Claude Desktop'un yaptığı gibi: yapılandırmadaki komutu başlatır, stdio üzerinden JSON-RPC konuşur."""

    def __init__(self, girdi: dict):
        self.p = subprocess.Popen([girdi["command"], *girdi["args"]], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, env={**os.environ, **girdi.get("env", {})}, text=True,
                                  encoding="utf-8")
        self.kuyruk: queue.Queue = queue.Queue()
        self.no = 0
        threading.Thread(target=self._oku, daemon=True).start()

    def _oku(self):
        for satir in self.p.stdout:
            try:
                self.kuyruk.put(json.loads(satir))
            except ValueError:
                pass

    def _gonder(self, ileti: dict):
        self.p.stdin.write(json.dumps(ileti) + "\n")
        self.p.stdin.flush()

    def iste(self, metod: str, params: dict | None = None, zaman: float = 60) -> dict:
        self.no += 1
        self._gonder({"jsonrpc": "2.0", "id": self.no, "method": metod, "params": params or {}})
        bitis = time.time() + zaman
        while time.time() < bitis:
            try:
                m = self.kuyruk.get(timeout=max(0.1, bitis - time.time()))
            except queue.Empty:
                break
            if m.get("id") == self.no:
                return m
        raise TimeoutError(f"{metod}: {zaman} sn içinde cevap gelmedi")

    def el_sikis(self) -> dict:
        r = self.iste("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                     "clientInfo": {"name": "mac-kurulum-denetimi", "version": "1"}})["result"]
        self._gonder({"jsonrpc": "2.0", "method": "notifications/initialized"})
        return r

    def kapat(self) -> str:
        try:
            self.p.stdin.close()
            self.p.wait(15)
        except (OSError, subprocess.TimeoutExpired):
            self.p.kill()
        return self.p.stderr.read()[-2000:] if self.p.stderr else ""


def kurulum(secim: list, surum: str) -> None:
    print("\n1. Kurulum günlüğü ve Python")
    gunluk = KOK / "veri" / "gunluk" / "kurulum-pkg.log"
    metin = gunluk.read_text(encoding="utf-8") if gunluk.exists() else ""
    print("\n".join("    | " + s for s in metin.strip().splitlines()[-15:]))
    denetle("kur çıkış kodu 0" in metin, "kurulumun son adımı (postinstall) kur.py'yi başarıyla çalıştırdı")
    arm = calistir(["sysctl", "-n", "hw.optional.arm64"]).stdout.strip() == "1"
    denetle(PY.exists(), f"Python: {PY}")
    r = calistir([PY, "-c", "import json, platform, ssl, sys; "
                            "print(json.dumps([platform.machine(), sys.version.split()[0], ssl.OPENSSL_VERSION]))"])
    makine, surum_py, openssl = json.loads(r.stdout) if r.returncode == 0 else ("?", "?", r.stderr[-300:])
    denetle(makine == ("arm64" if arm else "x86_64"), f"işlemciye uyan Python: {makine} {surum_py} ({openssl})")
    denetle(not (KOK / "runtime-arm64").exists() and not (KOK / "runtime-x86_64").exists(), "öteki işlemcinin Python'u silindi")
    r = calistir([PY, "-c", "import urllib.request; print(urllib.request.urlopen('https://api.github.com', timeout=30).status)"])
    denetle(r.stdout.strip() == "200", "HTTPS (sertifika doğrulaması; güncelleyici ve uzak sunucu için)" +
            ("" if r.returncode == 0 else f": {r.stderr.strip()[-300:]}"))

    print("\n2. Modül seçimi ve sürüm")
    moduller = json.loads((KOK / "moduller.json").read_text(encoding="utf-8")).get("moduller")
    denetle(moduller == secim, f"moduller.json: {moduller}")
    onceki = sorted(p.name for p in (KOK / "onceki").iterdir()) if (KOK / "onceki").is_dir() else []
    denetle(onceki == sorted(secim), f"önceki seçim (kurulum yeniden açılınca işaretli gelir): {onceki}")
    denetle(not (KOK / "secim").exists(), "kurulumun seçim işaretleri temizlendi")
    aktif = (KOK / "aktif.txt").read_text(encoding="utf-8").strip() if (KOK / "aktif.txt").exists() else ""
    denetle(aktif == surum, f"etkin sürüm: {aktif}")

    print("\n3. Claude Desktop kaydı")
    sunucular = json.loads(CLAUDE.read_text(encoding="utf-8")).get("mcpServers", {}) if CLAUDE.exists() else {}
    yerel = sunucular.get("arthurlegal-yerel", {})
    denetle(yerel.get("command") == str(PY) and yerel.get("args") == ["-B", str(AL), "sunucu"],
            f"arthurlegal-yerel: {yerel.get('command')} {' '.join(yerel.get('args', []))}")
    denetle(("arthur-tapu" in sunucular) == ("tapu" in secim), f"arthur-tapu {'var' if 'arthur-tapu' in sunucular else 'yok'}")

    print("\n4. Uygulamalar ve masaüstü")
    liste = json.loads(kurulu_python("import kur; print(json.dumps([[str(y), str(h), a] for y, h, a, _ in "
                                     "kur._kisayol_listesi()]))"))
    for y, h, a in liste:
        y = Path(y)
        if y.parent == MASA:
            denetle(y.is_symlink() and os.readlink(y) == h, f"masaüstünde takma ad: {y.name} → {h}")
            continue
        try:
            bilgi = plistlib.loads((y / "Contents" / "Info.plist").read_bytes())
        except OSError:
            bilgi = {}
        denetle(str(bilgi.get("CFBundleIdentifier", "")).startswith("com.arthurlegal.kisayol.")
                and bilgi.get("CFBundleShortVersionString") == surum, f"uygulama: {y.relative_to(EV)} ({surum})")
        denetle(os.access(y / "Contents" / "MacOS" / "arthurlegal", os.X_OK)
                and (y / "Contents" / "Resources" / "arthurlegal.icns").exists(), "  çalıştırılabilir ve simgeli")
    adlar = {Path(y).name for y, _, _ in liste}
    if "adliye" in secim:
        denetle((MASA / "ArthurLegal Courthouse.app").is_symlink(), "masaüstünde Courthouse simgesi")
    if "tapu" in secim:
        denetle((MASA / "ArthurLegal Tapu.app").is_symlink(), "masaüstünde Tapu simgesi")
    if not {"hukuk-burosu", "kurumsal"} & set(secim):
        denetle("ArthurLegal.app" not in adlar and not (UYG / "ArthurLegal.app").exists(),
                "Hukuk Bürosu ve Kurumsal seçilmedi: ana simge yok")
    kaldir = KOK / "KALDIR.command"
    denetle(os.access(kaldir, os.X_OK) and calistir(["sh", "-n", kaldir]).returncode == 0, "kaldırma betiği")

    print("\n5. Oturum açılışında güncelleme")
    denetle(AJAN.exists(), f"LaunchAgent: {AJAN.name}")
    r = calistir(["launchctl", "print", f"gui/{os.getuid()}/com.arthurlegal.guncelleme"])
    denetle(r.returncode == 0, "launchctl'de yüklü" + ("" if r.returncode == 0 else f": {r.stderr.strip()[-200:]}"))
    durum_yolu = KOK / "veri" / "durum.json"
    durum: dict = {}
    for _ in range(60):  # RunAtLoad: ilk denetim kurulumla başladı; bitmesini bekle (kilit dosyası)
        durum = json.loads(durum_yolu.read_text(encoding="utf-8") or "{}") if durum_yolu.exists() else {}
        if not (KOK / "veri" / "guncelle.kilit").exists() and "son_sonuc" in durum:
            break
        time.sleep(2)
    denetle("son_sonuc" in durum and not str(durum.get("son_sonuc")).startswith("hata"),
            f"ilk güncelleme denetimi: {durum.get('son_sonuc')}", yalniz_uyari=True)

    print("\n6. Başlangıç sayfası ve Courthouse simgesi")
    denetle((KOK / "rehber" / "baslangic.html").exists() and (KOK / "rehber" / "baslangic-en.html").exists(),
            "başlangıç rehberi (Türkçe ve İngilizce)")
    if "adliye" in secim:
        betik = UYG / "ArthurLegal Courthouse.app" / "Contents" / "MacOS" / "arthurlegal"
        r = calistir([betik], env={**os.environ, "BROWSER": "/usr/bin/true"})  # tarayıcı açılmasın
        js = (KOK / "rehber" / "durum.js").read_text(encoding="utf-8")
        veri = json.loads(js.split("=", 1)[1].strip().rstrip(";"))
        denetle(r.returncode == 0 and veri.get("odak") == "adliye" and veri.get("isletim") == "mac"
                and veri.get("moduller") == secim, f"Courthouse simgesi paneli açtı: odak={veri.get('odak')}, "
                f"işletim={veri.get('isletim')}, Claude={veri.get('claude')}")

    print("\n7. Yerel ArthurLegal sunucusu (Claude Desktop'un başlattığı gibi)")
    s = Sunucu(yerel)
    try:
        r = s.el_sikis()
        denetle("arthurlegal_talimat" in r.get("instructions", ""), f"el sıkışma: {r.get('serverInfo')}")
        araclar = {t["name"]: t for t in s.iste("tools/list", zaman=90)["result"]["tools"]}
        talimat = araclar.get("arthurlegal_talimat", {})
        secenek = talimat.get("inputSchema", {}).get("properties", {}).get("profil", {}).get("enum")
        denetle(secenek == [m for m in secim if m in PAKETLER], f"yalnız seçilen paketler: {secenek}")
        uzak = [a for a in araclar if a.startswith("tr_")]
        denetle(uzak, f"uzak araçlar (arthurlegal-mcp): {len(araclar)} araç, {len(uzak)} tr_", yalniz_uyari=True)
        metin = s.iste("tools/call", {"name": "arthurlegal_talimat", "arguments": {}})["result"]["content"][0]["text"]
        denetle(metin.splitlines()[0].startswith("# ArthurLegal"), f"talimat: {metin.splitlines()[0]}")
        if uzak:
            r = s.iste("tools/call", {"name": "status", "arguments": {}}, zaman=90).get("result", {})
            denetle(not r.get("isError"), "uzak araç çağrısı (status)", yalniz_uyari=True)
    except (TimeoutError, KeyError, IndexError, ValueError) as e:
        denetle(False, f"yerel sunucu: {e!r}")
    finally:
        hata = s.kapat()
        if hatalar and hata:
            print("    stderr: " + hata.replace("\n", "\n    "))

    if "tapu" in secim:
        print("\n8. Tapu sunucusu")
        s = Sunucu(sunucular["arthur-tapu"])
        try:
            r = s.el_sikis()
            araclar = [t["name"] for t in s.iste("tools/list")["result"]["tools"]]
            denetle(any(a.startswith("tkgm_") for a in araclar),
                    f"Tapu: {r.get('serverInfo', {}).get('name')}, {len(araclar)} araç ({', '.join(araclar[:4])} ...)")
        except (TimeoutError, KeyError, ValueError) as e:
            denetle(False, f"Tapu sunucusu: {e!r}")
        finally:
            hata = s.kapat()
            if hatalar and hata:
                print("    stderr: " + hata.replace("\n", "\n    "))


def mask(surum: str) -> None:
    """Güncelleyicinin Mac'teki Arthur Mask kurulumu (guncelle.mac_mask_kur): disk görüntüsü iner, sha256'sı
    doğrulanır, uygulama Uygulamalar'a kopyalanır, Arthur Mask kendini Claude Desktop'a kaydeder; kısayollar yeniden
    yazılınca masaüstünde onun da takma adı olur."""
    print("\n9. Arthur Mask (macOS)")
    k = json.loads((BURASI / "kaynaklar.json").read_text(encoding="utf-8"))
    t0 = time.time()
    sonuc = kurulu_python(f"import guncelle; print(guncelle.mac_mask_kur({{'mask_macos': {k['mask_macos']!r}}}))",
                          zaman=3600)
    denetle(sonuc.endswith(" kuruldu") or sonuc.startswith("mask: kurulu"),
            f"{sonuc} ({int(time.time() - t0)} sn)")
    app = next((p for p in (Path("/Applications/Arthur Mask.app"), UYG / "Arthur Mask.app") if p.exists()), None)
    denetle(app and (app / "Contents" / "Resources" / "runtime" / "bin" / "python3").exists(), f"uygulama: {app}")
    sunucular = json.loads(CLAUDE.read_text(encoding="utf-8")).get("mcpServers", {})
    denetle("arthur-mask" in sunucular, "Arthur Mask kendini Claude Desktop'a kaydetti: "
            + json.dumps(sunucular.get("arthur-mask", {}), ensure_ascii=False)[:200])
    r = calistir([PY, "-B", AL, "kur", "--kaydet", "--kisayol"])
    denetle(r.returncode == 0 and (MASA / "Arthur Mask.app").is_symlink(),
            f"masaüstünde Arthur Mask simgesi → {os.readlink(MASA / 'Arthur Mask.app') if (MASA / 'Arthur Mask.app').is_symlink() else '-'}")
    if "arthur-mask" in sunucular:
        s = Sunucu(sunucular["arthur-mask"])
        try:
            r = s.el_sikis()
            araclar = [t["name"] for t in s.iste("tools/list", zaman=300)["result"]["tools"]]
            denetle(araclar, f"Arthur Mask sunucusu: {r.get('serverInfo', {}).get('name')}, {len(araclar)} araç")
        except (TimeoutError, KeyError, ValueError) as e:
            denetle(False, f"Arthur Mask sunucusu: {e!r}")
        finally:
            hata = s.kapat()
            if hatalar and hata:
                print("    stderr: " + hata.replace("\n", "\n    "))


def kaldir() -> None:
    """KALDIR.command'ın işi (onay penceresi olmadan): kayıt, uygulamalar, takma adlar ve LaunchAgent gider."""
    print("\n10. Kaldırma")
    r = calistir([PY, "-B", AL, "kur", "--kaldir"])
    denetle(r.returncode == 0, "kur --kaldir" + ("" if r.returncode == 0 else f": {r.stderr[-300:]}"))
    kalan = [p.name for p in UYG.glob("ArthurLegal*")] + [
        p.name for p in MASA.glob("*.app") if p.is_symlink() and ("ArthurLegal" in os.readlink(p) or p.name == "Arthur Mask.app")]
    denetle(not kalan, f"uygulamalar ve masaüstü takma adları silindi{': ' + ', '.join(kalan) if kalan else ''}")
    denetle(not AJAN.exists() and calistir(["launchctl", "print", f"gui/{os.getuid()}/com.arthurlegal.guncelleme"]).returncode,
            "LaunchAgent kaldırıldı")
    sunucular = json.loads(CLAUDE.read_text(encoding="utf-8")).get("mcpServers", {})
    denetle(not {"arthurlegal-yerel", "arthur-tapu"} & set(sunucular), f"Claude Desktop kaydı silindi: {sorted(sunucular)}")


def main(argv: list) -> int:
    secim = (argv[0] if argv and not argv[0].startswith("--") else "adliye,tapu,mask").split(",")
    surum = json.loads((BURASI / "kaynaklar.json").read_text(encoding="utf-8"))["surum"]
    print(f"ArthurLegal {surum} macOS kurulumu denetleniyor: {KOK} (modüller: {', '.join(secim)})")
    try:
        if "--mask" in argv:
            mask(surum)
        elif "--kaldir" in argv:
            kaldir()
        else:
            kurulum(secim, surum)
    except Exception as e:  # noqa: BLE001 — denetim yarıda kalsa da özet yazılsın
        denetle(False, f"denetim yarıda kaldı: {e!r}")
    print(f"\n{len(hatalar)} hata, {len(uyarilar)} uyarı")
    for h in hatalar:
        print(f"::error::{h}")
    for u in uyarilar:
        print(f"::warning::{u}")
    return 1 if hatalar else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
