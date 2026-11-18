"""Geçiş provası: yeni sürüme geçişi, kullanıcıların bilgisayarında kurulu ESKİ güncelleyiciyle yayından önce dener.

    python yayin/gecis_provasi.py                      yayin/cikti'deki adayı yayındaki son iki sürüme karşı dener
    python yayin/gecis_provasi.py --eski E.zip [--onceki O.zip]   ağsız: eski sürümler yerel paket zip'lerinden
    python yayin/gecis_provasi.py --sakla              geçici kurulumları silme (inceleme için)

Neden: sürüm geçişini yeni sürüm değil, kullanıcının bilgisayarında kurulu eski güncelleyici yapar; yeni sürümün kendi
kuralları ancak ondan sonraki geçişte devreye girer. 18.11.2026 olayında eski güncelleyici, uygulama iki güncelleme
boyunca hiç kapanmadığı için çalışan sunucunun sürüm klasörünü sildi; asistan "Bu kurulumda paket yok" dedi ve iki hafta
paketin kuralları olmadan çalıştı. Yeni sürümü tek başına denemek bunu göstermez: "eski güncelleyici + yeni sürüm"
birlikte denenmelidir. yayinla.py bu provayı yayından önce çalıştırır; düşerse yayın durur (bilerek geçmek: --provasiz).

Ne yapar (her senaryo ayrı geçici kurulumda; gerçek kuruluma, Claude Desktop ya da ChatGPT ayarına, kısayollara,
kayıt defterine ve proje klasörlerine dokunmaz):
1. Yayındaki son sürüm ("eski") ve bir önceki yayın ("önceki") indirilir; manifest imzaları yayın anahtarlarıyla,
   paketler sha256 ile doğrulanır (önbellek: yayin/.onbellek/prova).
2. Geçici kök: surumler/<önceki>, surumler/<eski>, kurulumun gömülü Python'u (runtime), ayar.json (yerel manifest
   adresi), moduller.json (dört paket). Adayın manifesti bir kerelik deneme anahtarıyla imzalanır ve yerel bir HTTP
   sunucusundan verilir; eski sürümlerin icerik.json'una yalnız bu anahtar yazılır.
3. bin/al.py yerine sarmalayıcı (SARMALAYICI): "kur" çağrısında yalnız kur.calisan_sunucuyu_onar çalışır (açık
   sunucunun paketini geri koyan adım); uygulamanın açık olup olmadığı senaryodan gelir; ArthurMask'e dokunulmaz.
4. Senaryolar:
   - açık: uygulama iki güncelleme boyunca kapanmadı. Sunucu <önceki>den çalışıyor, etkin sürüm <eski>; eski
     güncelleyici adayı kurar. Çalışan sunucu paketini bulmayı sürdürmeli (18.11 olayı).
   - kapalı: uygulama kapalı; eski güncelleyici adayı kurar ve eski klasörleri siler.
   İkisinde de: etkin sürüm aday olur, bir önceki sürüm geri dönüş için kalır; uygulama yeniden açılınca sunucu adaydan
   başlar, paket_durumu "tamam", talimat tam (çekirdek kurallar değil), masanın sürümü adayla aynı.
"""
from __future__ import annotations

import argparse
import hashlib
import http.server
import json
import os
import queue
import shutil
import subprocess
import sys
import tempfile
import threading
import zipfile
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]
CIKTI = BURASI / "yayin" / "cikti"
ONBELLEK = BURASI / "yayin" / ".onbellek"
sys.path.insert(0, str(BURASI / "istemci"))
import ed25519  # noqa: E402
import ortak  # noqa: E402

CEKIRDEK_BASI = "# ArthurLegal — çekirdek kurallar"   # arthurlegal_sunucu.cekirdek_talimat: paket yüklenemedi
YEREL_UZAK = "http://127.0.0.1:9/mcp"                  # araştırma sunucusuna çıkılmaz (bağlantı hemen reddedilir)
SUNUCU_ZAMAN = 30


class ProvaHatasi(Exception):
    """Prova düştü ya da kurulamadı; ileti kullanıcıya gösterilir."""


# Geçici kökün bin/al.py'si. Gerçek başlatıcı (al_gercek.py) etkin sürümü seçer; sarmalayıcı provada gerçek bilgisayara
# dokunan adımları çalıştırmaz. Python 3.8+ (gömülü Python'un ._pth'si betiğin klasörünü sys.path'e eklemez).
SARMALAYICI = r'''"""Geçiş provası sarmalayıcısı (yayin/gecis_provasi.py yazar; elle düzenlemeyin).

Gerçek bin/al.py (al_gercek.py) gibi etkin sürümü çalıştırır, ama provada gerçek bilgisayara dokunan adımları atlar:
- kur: yalnız kur.calisan_sunucuyu_onar (varsa). Claude Desktop/ChatGPT kaydı, kısayollar, kayıt defteri, proje
  klasörleri yazılmaz.
- guncelle ve sunucu: olduğu gibi; uygulamanın açık olup olmadığı (ortak.asistan_calisiyor) AL_PROVA_ACIK'tan gelir.
- öteki hedefler çalıştırılmaz.
Her çağrı veri/prova-cagrilar.jsonl'e yazılır.
"""
import importlib.util
import json
import os
import runpy
import sys
import time

_spec = importlib.util.spec_from_file_location(
    "al_gercek", os.path.join(os.path.dirname(os.path.abspath(__file__)), "al_gercek.py"))
gercek = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gercek)


def kaydet(**alan):
    klasor = os.path.join(gercek.KOK, "veri")
    os.makedirs(klasor, exist_ok=True)
    alan["zaman"] = time.time()
    with open(os.path.join(klasor, "prova-cagrilar.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(alan, ensure_ascii=False) + "\n")


def main():
    hedef = sys.argv[1] if len(sys.argv) > 1 else ""
    argumanlar = sys.argv[2:]
    dizin = gercek.etkin_dizin()
    kaydet(hedef=hedef, argumanlar=argumanlar, surum=os.path.basename(dizin))
    if hedef not in ("guncelle", "sunucu", "kur"):
        return 0
    for akis in (sys.stdout, sys.stderr):
        try:
            akis.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass
    istemci = os.path.join(dizin, "istemci")
    sys.path.insert(0, istemci)
    import ortak
    acik = os.environ.get("AL_PROVA_ACIK") == "1"
    ortak.asistan_calisiyor = lambda: acik
    if hedef == "kur":
        import kur
        onar = getattr(kur, "calisan_sunucuyu_onar", None)
        kaydet(hedef="kur-onar", var=onar is not None, sonuc=onar() if onar else None)
        return 0
    yol = os.path.join(istemci, "guncelle.py" if hedef == "guncelle" else "arthurlegal_sunucu.py")
    sys.argv = [yol] + argumanlar
    runpy.run_path(yol, run_name="__main__")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


# ------------------------------------------------------------------------------------------------ eski sürümler

def zip_surumu(yol: Path) -> str:
    """Paket zip'inin sürümü (kökteki surum.txt)."""
    try:
        with zipfile.ZipFile(yol) as z:
            return z.read("surum.txt").decode("utf-8").strip()
    except (OSError, KeyError, zipfile.BadZipFile) as e:
        raise ProvaHatasi(f"paket zip'i okunamadı ({yol}): {e}") from None


def yayin_anahtarlari(k: dict) -> list:
    return [a for a in (k.get("yayin_anahtari"), k.get("kasa_anahtari")) if isinstance(a, str) and len(a) == 64]


def yayindaki_surumler(depo: str, anahtarlar: list, jeton: str = "", adet: int = 2) -> list:
    """Yayındaki en yeni `adet` kararlı sürüm, yeniden eskiye: [{"surum", "etiket", "zip"}]. Manifest imzası yayın
    anahtarlarından biriyle, paket sha256'sı manifestle doğrulanır; paketler yayin/.onbellek/prova'da saklanır."""
    basliklar = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if jeton:
        basliklar["Authorization"] = "Bearer " + jeton
    varlik_basligi = {**basliklar, "Accept": "application/octet-stream"}
    yayinlar = json.loads(ortak.indir(f"https://api.github.com/repos/{depo}/releases?per_page=30", zaman=30,
                                      basliklar=basliklar).decode("utf-8"))
    sonuc = []
    for y in yayinlar:
        varliklar = {a["name"]: a for a in y.get("assets", [])}
        if y.get("draft") or y.get("prerelease") or not {"arthurlegal-manifest.json", "arthurlegal-manifest.sig"} <= set(varliklar):
            continue
        ham = ortak.indir(varliklar["arthurlegal-manifest.json"]["url"], zaman=60, basliklar=varlik_basligi)
        imza = bytes.fromhex(ortak.indir(varliklar["arthurlegal-manifest.sig"]["url"], zaman=60,
                                         basliklar=varlik_basligi).decode("ascii").strip())
        if not any(ed25519.verify(bytes.fromhex(a), ham, imza) for a in anahtarlar):
            raise ProvaHatasi(f"{y.get('tag_name')} manifest imzası yayın anahtarlarıyla doğrulanmadı")
        m = json.loads(ham.decode("utf-8"))
        dosya, ozet = m["paket"]["dosya"], m["paket"]["sha256"]
        hedef = ONBELLEK / "prova" / dosya
        if not hedef.exists() or ortak.sha256_dosya(hedef) != ozet:
            if dosya not in varliklar:
                raise ProvaHatasi(f"{y.get('tag_name')} yayınında paket yok: {dosya}")
            print(f"  {y.get('tag_name')} paketi indiriliyor ({varliklar[dosya].get('size', 0) // (1 << 20)} MB)...")
            if ortak.indir(varliklar[dosya]["url"], hedef, zaman=300, basliklar=varlik_basligi) != ozet:
                hedef.unlink(missing_ok=True)
                raise ProvaHatasi(f"{dosya} sha256'sı manifestle uyuşmadı")
        sonuc.append({"surum": m["surum"], "etiket": y.get("tag_name"), "zip": hedef})
        if len(sonuc) == adet:
            break
    if not sonuc:
        raise ProvaHatasi(f"{depo} deposunda manifestli kararlı yayın bulunamadı")
    return sonuc


# ------------------------------------------------------------------------------------------------ geçici kurulum

def runtime_kur(hedef: Path, tur, python: dict | None = None) -> Path:
    """Geçici kökün Python'u; ortak.python_yolu'nun bulacağı yerde. Güncelleyici `kur --kaydet` adımını yalnız bu
    dosya varsa çağırır: koruma o adımdadır, Python'suz prova onu hiç denemezdi.
    tur "gomulu": kurulumun kendi gömülü Python'u (Windows; kaynaklar.json python, sha256 doğrulanır, önbellekte).
    tur "sistem": bu Python (testler): Windows'ta sanal ortam, macOS'ta bağlantı.
    tur bir klasörse: daha önce bu işlevle kurulmuş runtime kopyalanır (testler her senaryoda yeniden kurmasın)."""
    if isinstance(tur, Path):
        shutil.copytree(tur, hedef, symlinks=True)
        return hedef / "bin" / "python3" if ortak.MAC else hedef / "python.exe"
    if ortak.MAC:  # macOS kurulumunun Python'u ayrıca derlenir; provada bu Python yeterli
        (hedef / "bin").mkdir(parents=True, exist_ok=True)
        os.symlink(sys.executable, hedef / "bin" / "python3")
        return hedef / "bin" / "python3"
    if tur == "gomulu":
        if not python or not python.get("url"):
            raise ProvaHatasi("kaynaklar.json'da gömülü Python adresi yok")
        arsiv = ONBELLEK / Path(python["url"]).name
        if not arsiv.exists():
            print(f"  Python {python.get('surum', '')} gömülü dağıtımı indiriliyor...")
            ortak.indir(python["url"], arsiv, zaman=300)
        if python.get("sha256") and ortak.sha256_dosya(arsiv) != python["sha256"]:
            raise ProvaHatasi(f"gömülü Python arşivinin sha256'sı uyuşmadı: {arsiv}")
        with zipfile.ZipFile(arsiv) as z:
            z.extractall(hedef)
    else:
        subprocess.run([sys.executable, "-m", "venv", "--without-pip", str(hedef)], check=True, capture_output=True)
        for ad in ("python.exe", "pythonw.exe"):
            shutil.copy2(hedef / "Scripts" / ad, hedef / ad)
    return hedef / "python.exe"


def surum_ac(zip_yolu: Path, kok: Path, anahtar: str) -> str:
    """Paket zip'ini surumler/<sürüm>'e açar; icerik.json'un güvenilen anahtarları yalnız deneme anahtarı olur."""
    surum = zip_surumu(zip_yolu)
    hedef = kok / "surumler" / surum
    with zipfile.ZipFile(zip_yolu) as z:
        z.extractall(hedef)
    icerik = ortak.json_oku(hedef / "icerik.json", {})
    icerik["anahtarlar"] = [anahtar]
    ortak.json_yaz(hedef / "icerik.json", icerik)
    return surum


def kok_kur(kok: Path, zipler: list, aktif: str, anahtar: str, manifest_url: str, paketler: list,
            runtime: str, python: dict | None) -> Path:
    (kok / "bin").mkdir(parents=True)
    shutil.copy2(BURASI / "bin" / "al.py", kok / "bin" / "al_gercek.py")
    (kok / "bin" / "al.py").write_text(SARMALAYICI, encoding="utf-8")
    for z in zipler:
        surum_ac(z, kok, anahtar)
    ortak.json_yaz(kok / "ayar.json", {"manifest_url": manifest_url, "yedek_depo": "", "uzak_mcp": YEREL_UZAK,
                                      "yayin_anahtari": anahtar})
    ortak.json_yaz(kok / "moduller.json", {"moduller": paketler})
    ortak.json_yaz(kok / "veri" / "durum.json", {"asistan": "claude", "arayuz": "yeni", "dil": "tr"})
    (kok / "aktif.txt").write_text(aktif, encoding="utf-8")
    return runtime_kur(kok / "runtime", runtime, python)


def ortam(acik: bool) -> dict:
    e = {**os.environ, "PYTHONIOENCODING": "utf-8", "ARTHURLEGAL_GUNCELLEME": "0", "AL_PROVA_ACIK": "1" if acik else "0"}
    for ad in ("ARTHURLEGAL_KOK", "AL_EV", "PYTHONHOME", "PYTHONPATH"):
        e.pop(ad, None)
    return e


class Sunucu:
    """Geçici kökte arthurlegal-yerel (bin/al.py sunucu): Claude Desktop'ın başlattığı gibi, stdio üzerinden."""

    def __init__(self, py: Path, kok: Path, acik: bool):
        self.p = subprocess.Popen([str(py), "-B", str(kok / "bin" / "al.py"), "sunucu"], stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=ortam(acik), text=True,
                                  encoding="utf-8", errors="replace")
        self.kuyruk, self.no, self.hata = queue.Queue(), 0, []
        threading.Thread(target=self._oku, daemon=True).start()
        threading.Thread(target=lambda: [self.hata.append(s) for s in self.p.stderr], daemon=True).start()

    def _oku(self):
        for satir in self.p.stdout:
            try:
                self.kuyruk.put(json.loads(satir))
            except ValueError:
                pass

    def istek(self, metod: str, params: dict) -> dict:
        self.no += 1
        try:
            self.p.stdin.write(json.dumps({"jsonrpc": "2.0", "id": self.no, "method": metod, "params": params}) + "\n")
            self.p.stdin.flush()
            while True:
                m = self.kuyruk.get(timeout=SUNUCU_ZAMAN)
                if m.get("id") == self.no:
                    return m
        except (OSError, queue.Empty):
            raise ProvaHatasi("yerel sunucu cevap vermedi: " + "".join(self.hata[-5:]).strip()[:400]) from None

    def arac(self, ad: str, **arg) -> tuple:
        """(metin, yapı, hata): araç hatası ya da JSON-RPC hatası `hata`dadır."""
        m = self.istek("tools/call", {"name": ad, "arguments": arg})
        if "error" in m:
            return "", None, str(m["error"].get("message") or m["error"])
        r = m.get("result") or {}
        metin = "".join(b.get("text", "") for b in r.get("content") or [] if isinstance(b, dict))
        return metin, r.get("structuredContent"), (metin[:200] or "hata") if r.get("isError") else None

    def kapat(self):
        try:
            self.p.stdin.close()
        except OSError:
            pass
        try:
            self.p.wait(10)
        except subprocess.TimeoutExpired:
            self.p.kill()
            self.p.wait(10)
        for akis in (self.p.stdout, self.p.stderr):
            try:
                akis.close()
            except OSError:
                pass


def talimat_sorunu(s: Sunucu) -> str | None:
    """Talimat tam geliyorsa None; paket yüklenemiyorsa nedeni."""
    metin, _, hata = s.arac("arthurlegal_talimat")
    if hata:
        return f"talimat hata verdi: {hata}"
    if metin.startswith(CEKIRDEK_BASI):
        return "paket yüklenemedi, talimat yalnız çekirdek kurallar"
    return None


def yeniden_acilis(py: Path, kok: Path, aday: str) -> list:
    """Uygulama yeniden açıldı: sunucu adaydan başlamalı, paketi ve masası adayla aynı sürümde olmalı."""
    s, sorunlar = Sunucu(py, kok, acik=True), []
    try:
        metin, _, hata = s.arac("arthurlegal_durum")
        durum = json.loads(metin) if not hata and metin.startswith("{") else {}
        if durum.get("yerel_kurulum") != aday:
            sorunlar.append(f"yeniden açılışta sunucu {durum.get('yerel_kurulum') or hata or '?'} sürümünden başladı, "
                            f"{aday} değil")
        if "paket_durumu" in durum and durum["paket_durumu"] != "tamam":
            sorunlar.append(f"yeniden açılışta paket_durumu: {json.dumps(durum['paket_durumu'], ensure_ascii=False)[:300]}")
        neden = talimat_sorunu(s)
        if neden:
            sorunlar.append("yeniden açılışta " + neden)
        _, masa, hata = s.arac("al_masasi")
        if not hata and isinstance(masa, dict) and masa.get("surum") != aday:
            sorunlar.append(f"masanın sürümü {masa.get('surum')}, AL {aday}")
    finally:
        s.kapat()
    return sorunlar


def guncelleyici(py: Path, kok: Path, acik: bool) -> subprocess.CompletedProcess:
    """Etkin (eski) sürümün güncelleyicisi, oturum açılışındaki gibi; ArthurMask'e dokunmaz."""
    return subprocess.run([str(py), "-B", str(kok / "bin" / "al.py"), "guncelle", "--mask-yok"], env=ortam(acik),
                          capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)


def kur_cagrilari(kok: Path) -> list:
    yol = kok / "veri" / "prova-cagrilar.jsonl"
    if not yol.exists():
        return []
    return [json.loads(s) for s in yol.read_text(encoding="utf-8").splitlines() if s.strip()]


def senaryo(ad: str, kok: Path, acik: bool, eski: dict, onceki: dict, aday: str, paketler: list, anahtar: str,
            manifest_url: str, runtime: str, python: dict | None) -> tuple:
    """(sorunlar, notlar). açık: sunucu önceki sürümden çalışırken eski güncelleyici adayı kurar. kapalı: sunucu yok."""
    zipler = [onceki["zip"]] + ([eski["zip"]] if eski["surum"] != onceki["surum"] else [])
    py = kok_kur(kok, zipler, onceki["surum"] if acik else eski["surum"], anahtar, manifest_url, paketler, runtime, python)
    sorunlar, notlar, calisan = [], [], None
    try:
        if acik:
            calisan = Sunucu(py, kok, acik=True)   # uygulama önceki sürümle açıldı ...
            neden = talimat_sorunu(calisan)
            if neden:
                raise ProvaHatasi(f"hazırlık: önceki sürümün ({onceki['surum']}) sunucusu daha güncellemeden önce: {neden}")
            (kok / "aktif.txt").write_text(eski["surum"], encoding="utf-8")   # ... eski sürüm kuruldu, kapanmadı
        r = guncelleyici(py, kok, acik)   # çıktı metnine bakılmaz: eski sürümler başka biçimde yazmış olabilir
        if r.returncode != 0:
            sorunlar.append(f"eski güncelleyici ({eski['surum']}) hatayla bitti (çıkış {r.returncode}): "
                            + (r.stdout + r.stderr).strip()[-400:])
        son = ortak.json_oku(kok / "veri" / "durum.json").get("son_guncelleme", {})
        etkin = (kok / "aktif.txt").read_text(encoding="utf-8").strip()
        if etkin != aday:
            sorunlar.append(f"etkin sürüm {etkin}, {aday} olmalıydı")
        yeni = kok / "surumler" / aday
        if not (yeni / "istemci" / "arthurlegal_sunucu.py").exists():
            sorunlar.append(f"surumler/{aday} istemci kodu taşımıyor")
        eksik = [p for p in paketler if not (yeni / "paketler" / p / "SYSTEM_PROMPT.md").exists()]
        if eksik:
            sorunlar.append(f"surumler/{aday} içinde seçili paket yok: {', '.join(eksik)}")
        if not (kok / "surumler" / eski["surum"] / "istemci" / "arthurlegal_sunucu.py").exists():
            sorunlar.append(f"geri dönüş sürümü ({eski['surum']}) silindi")
        if calisan is not None:
            neden = talimat_sorunu(calisan)
            if neden:
                sorunlar.append(f"uygulama açıkken çalışan sunucu ({onceki['surum']}) geçişten sonra: {neden} "
                                "(18.11.2026 olayı: kullanıcı uygulamayı kapatana kadar asistan paketsiz çalışır)")
            calisan.kapat()
            calisan = None
        for c in kur_cagrilari(kok):
            if c.get("hedef") == "kur-onar" and c.get("sonuc"):
                notlar.append(f"çalışan sunucunun ({c['sonuc']}) paketleri geri kondu")
        if isinstance(son, dict) and son.get("yeni") == aday:
            notlar.append(f"güncelleyici {son.get('onceki')} → {aday} kaydetti")
        sorunlar += yeniden_acilis(py, kok, aday)
    finally:
        if calisan is not None:
            calisan.kapat()
    return [f"{ad}: {s}" for s in sorunlar], notlar


# ------------------------------------------------------------------------------------------------ prova

def prova(aday_zip: Path, manifest: dict, eski: dict, onceki: dict | None = None, runtime: str = "gomulu",
          python: dict | None = None, sakla: bool = False) -> dict:
    """Adayı eski güncelleyiciyle iki senaryoda dener. manifest: yayımlanacak manifest (imzasız; taban yerel sunucuya
    çevrilir ve deneme anahtarıyla imzalanır). eski, onceki: {"surum", "zip"}; onceki yoksa eski. Düşerse ProvaHatasi.
    Dönüş: {"durum": "gecti" | "atlandi", "aday", "eski", "onceki", "ozet", "notlar"}."""
    aday = str(manifest["surum"])
    onceki = onceki or eski
    if ortak.surum_demeti(aday) <= ortak.surum_demeti(eski["surum"]):
        return {"durum": "atlandi", "aday": aday, "eski": eski["surum"], "onceki": onceki["surum"],
                "ozet": f"aday {aday} yayındaki {eski['surum']}'den yeni değil; güncelleyici kurmaz, prova atlandı",
                "notlar": []}
    if ortak.sha256_dosya(aday_zip) != manifest["paket"]["sha256"]:
        raise ProvaHatasi(f"aday paketin sha256'sı derlemeyle uyuşmuyor: {aday_zip}")
    with zipfile.ZipFile(aday_zip) as z:
        adaydaki = {n.split("/")[1] for n in z.namelist() if n.startswith("paketler/") and n.endswith("/SYSTEM_PROMPT.md")}
    paketler = [p for p in ortak.PAKETLER if p in adaydaki]
    for e in {eski["surum"]: eski, onceki["surum"]: onceki}.values():
        with zipfile.ZipFile(e["zip"]) as z:
            ad = set(z.namelist())
        paketler = [p for p in paketler if f"paketler/{p}/SYSTEM_PROMPT.md" in ad]
    if not paketler:
        raise ProvaHatasi("aday ile eski sürümlerin ortak paketi yok")

    gizli = os.urandom(32)
    anahtar = ed25519.public_key(gizli).hex()
    taban = Path(tempfile.mkdtemp(prefix="al-gecis-provasi-"))
    yayin = taban / "yayin"
    yayin.mkdir()
    shutil.copy2(aday_zip, yayin / manifest["paket"]["dosya"])

    class Statik(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(yayin), **k)

        def log_message(self, *a):
            pass

    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Statik)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{httpd.server_address[1]}"
    m = dict(manifest, taban=url + "/")
    ham = json.dumps(m, ensure_ascii=False, indent=1).encode("utf-8")
    (yayin / "arthurlegal-manifest.json").write_bytes(ham)
    (yayin / "arthurlegal-manifest.sig").write_text(ed25519.sign(gizli, ham).hex(), encoding="ascii")

    sorunlar, notlar, basarili = [], [], False
    try:
        for ad, acik in (("uygulama açık", True), ("uygulama kapalı", False)):
            try:
                s, n = senaryo(ad, taban / ("acik" if acik else "kapali"), acik, eski, onceki, aday, paketler,
                               anahtar, url + "/arthurlegal-manifest.json", runtime, python)
            except (ProvaHatasi, OSError, subprocess.SubprocessError) as e:
                s, n = [f"{ad}: {e}"], []
            sorunlar += s
            notlar += [f"{ad}: {x}" for x in n]
        basarili = not sorunlar
    finally:
        httpd.shutdown()
        httpd.server_close()
        if basarili and not sakla:
            shutil.rmtree(taban, ignore_errors=True)
    calisan = f" (çalışan sunucu {onceki['surum']})" if onceki["surum"] != eski["surum"] else ""
    if sorunlar:
        raise ProvaHatasi(f"Geçiş provası düştü: {eski['surum']}{calisan} → {aday}\n  " + "\n  ".join(sorunlar)
                          + f"\n  Geçici kurulum incelemek için duruyor: {taban}")
    return {"durum": "gecti", "aday": aday, "eski": eski["surum"], "onceki": onceki["surum"], "notlar": notlar,
            "ozet": f"eski güncelleyici {eski['surum']}{calisan} → {aday}: uygulama açık ✓ · kapalı ✓",
            **({"klasor": str(taban)} if sakla else {})}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal geçiş provası (yayından önce)")
    ap.add_argument("--eski", type=Path, help="yayındaki son sürümün paket zip'i (verilirse GitHub'a çıkılmaz)")
    ap.add_argument("--onceki", type=Path, help="bir önceki yayının paket zip'i (yoksa --eski)")
    ap.add_argument("--runtime", choices=("gomulu", "sistem"), default="gomulu",
                    help="geçici kurulumun Python'u: kurulumun gömülü Python'u (varsayılan) ya da bu Python")
    ap.add_argument("--sakla", action="store_true", help="geçici kurulumları silme")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    sys.path.insert(0, str(BURASI / "yayin"))
    import yayinla
    k, d = yayinla.kaynaklar(), ortak.json_oku(CIKTI / "derleme.json")
    if not d:
        sys.exit("Önce derleyin: python yayin/derle.py")
    depo = k.get("dagitim_deposu") or k["yayin_deposu"]
    try:
        if args.eski:
            eski = {"surum": zip_surumu(args.eski), "zip": args.eski}
            onceki = {"surum": zip_surumu(args.onceki), "zip": args.onceki} if args.onceki else None
        else:
            jeton = yayinla.github_jetonu() if k.get("dagitim_deposu") else ""
            surumler = yayindaki_surumler(depo, yayin_anahtarlari(k), jeton)
            eski, onceki = surumler[0], (surumler[1] if len(surumler) > 1 else None)
        sonuc = prova(CIKTI / d["paket"]["dosya"], yayinla.manifest_olustur(d, "v" + d["surum"], depo), eski, onceki,
                      args.runtime, k.get("python"), args.sakla)
    except ProvaHatasi as e:
        print(e)
        return 1
    print("Geçiş provası: " + sonuc["ozet"])
    for n in sonuc["notlar"]:
        print("  " + n)
    if sonuc.get("klasor"):
        print("  Geçici kurulum: " + sonuc["klasor"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
