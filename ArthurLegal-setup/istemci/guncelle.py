"""ArthurLegal sessiz güncelleyici.

Oturum açılışında (HKCU Run) ve yerel sunucu açıkken 6 saatte bir çalışır:
1. En son GitHub Release'teki arthurlegal-manifest.json ve .sig indirilir; imza güvenilen
   anahtarlardan biriyle (Ed25519: günlük yayın anahtarı ya da kasadaki yedek; liste çalışan
   paketten, ortak.guvenilen_anahtarlar) doğrulanmadan hiçbir şey kurulmaz.
2. Manifest'teki paket sürümü etkin sürümden yeniyse zip indirilir, sha256 doğrulanır, yeni
   bir surumler\\<sürüm> klasörüne açılır ve aktif.txt tek adımda değiştirilir. Çalışan
   sunucular eski klasörle devam eder; yeni sürüm Claude Desktop'ın bir sonraki açılışında
   devreye girer. Bir önceki sürüm geri dönüş için saklanır. Yerel derlemeyle kurulmuş, pakette
   olmayan UYAP köprüsü yeni sürüme kopyalanır.
3. ArthurMask kurulu sürümden yeniyse (≈1 GB) arka planda indirilir, Claude Desktop kapalıyken
   sessiz kurulur. Windows 11 Akıllı Uygulama Denetimi açıksa indirilmez: imzasız kurulum orada hiç çalışmaz.
   Kurulu değilse yalnız kurulumda seçildiyse (ortak.moduller) indirilir.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import zipfile
from pathlib import Path
from urllib.parse import urljoin

import ed25519
import ortak


class GuncellemeHatasi(Exception):
    pass


def _dogrula(ham: bytes, imza_metni: bytes, ayar: dict) -> dict:
    anahtarlar = ortak.guvenilen_anahtarlar(ayar)
    if not anahtarlar:
        raise GuncellemeHatasi("kurulumda yayın anahtarı yok")
    imza = bytes.fromhex(imza_metni.decode("ascii").strip())
    if not any(ed25519.verify(bytes.fromhex(a), ham, imza) for a in anahtarlar):
        raise GuncellemeHatasi("manifest imzası geçersiz; güncelleme reddedildi")
    return json.loads(ham.decode("utf-8"))


def _api_basliklari(ayar: dict, tur="application/vnd.github+json") -> dict:
    basliklar = {"Accept": tur, "X-GitHub-Api-Version": "2022-11-28"}
    if ayar.get("jeton"):
        basliklar["Authorization"] = "Bearer " + ayar["jeton"]
    return basliklar


def manifest_getir(ayar: dict):
    """(manifest, indirici) döndürür; yayın yoksa (None, None). indirici(dosya_adı, hedef) -> sha256.

    Dağıtım private depodan yapılır: varlıklar GitHub API'sinden, kurulumdaki salt okunur jetonla
    indirilir. manifest_url verilmişse (yerel sunucu, testler) düz HTTP yolu kullanılır.
    """
    depo = ayar.get("dagitim_deposu")
    if depo:
        if not ayar.get("jeton"):
            return None, None  # güncelleme kanalı yapılandırılmamış
        taban_api = ayar.get("api_tabani") or "https://api.github.com"
        yayinlar = json.loads(ortak.indir(f"{taban_api}/repos/{depo}/releases?per_page=10",
                                          zaman=30, basliklar=_api_basliklari(ayar)).decode("utf-8"))
        beta = ayar.get("kanal") == "beta"
        for yayin in yayinlar:
            if yayin.get("draft") or (yayin.get("prerelease") and not beta):
                continue
            varliklar = {a["name"]: a for a in yayin.get("assets", [])}
            if "arthurlegal-manifest.json" not in varliklar or "arthurlegal-manifest.sig" not in varliklar:
                continue

            def indirici(dosya, hedef=None, varliklar=varliklar):
                if dosya not in varliklar:
                    raise GuncellemeHatasi(f"yayında yok: {dosya}")
                return ortak.indir(varliklar[dosya]["url"], hedef, zaman=180,
                                   basliklar=_api_basliklari(ayar, "application/octet-stream"))

            manifest = _dogrula(indirici("arthurlegal-manifest.json"), indirici("arthurlegal-manifest.sig"), ayar)
            return manifest, indirici
        return None, None

    url = ayar.get("manifest_url")
    if not url:
        return None, None
    try:
        ham = ortak.indir(url, zaman=30)
    except urllib.error.HTTPError as e:
        if e.code != 404 or not ayar.get("yedek_depo"):
            raise
        # En son yayın manifest taşımıyorsa (ör. yalnız sürüm notu) taşıyan en yeni yayın aranır.
        taban_api = ayar.get("api_tabani") or "https://api.github.com"
        yayinlar = json.loads(ortak.indir(f"{taban_api}/repos/{ayar['yedek_depo']}/releases?per_page=10", zaman=30,
                                          basliklar=_api_basliklari(ayar)).decode("utf-8"))
        beta = ayar.get("kanal") == "beta"
        url = next((a["browser_download_url"] for y in yayinlar
                    if not y.get("draft") and (beta or not y.get("prerelease"))
                    for a in y.get("assets", []) if a.get("name") == "arthurlegal-manifest.json"), None)
        if not url:
            return None, None
        ham = ortak.indir(url, zaman=30)
    manifest = _dogrula(ham, ortak.indir(url[: -len(".json")] + ".sig", zaman=30), ayar)
    taban = manifest.get("taban") or url.rsplit("/", 1)[0] + "/"

    def indirici(dosya, hedef=None):
        return ortak.indir(urljoin(taban, dosya), hedef, zaman=180)

    return manifest, indirici


def _guvenli_ac(zip_yolu: Path, hedef: Path) -> None:
    with zipfile.ZipFile(zip_yolu) as z:
        for ad in z.namelist():
            yol = (hedef / ad).resolve()
            if not str(yol).startswith(str(hedef.resolve())) or ad.startswith(("/", "\\")):
                raise GuncellemeHatasi(f"zip içinde geçersiz yol: {ad}")
        z.extractall(hedef)


# Yerel derlemeyle kurulup genel pakette bulunmayan bileşenler (UYAP köprüsü) güncellemede yeni sürüme kopyalanır:
# GitHub'daki paket UYAP içermez; köprüsü olmayan sürümde Claude Desktop kaydı UYAP bağlantısını siler
# (claude_ayari.kaydet). Paket kendi köprüsünü getiriyorsa (büro derlemesi) eskisi taşınmaz.
YEREL_BILESENLER = ("uyap",)


def yerel_bilesenleri_tasi(eski: Path, yeni: Path) -> list:
    tasinan = []
    for ad in YEREL_BILESENLER:
        if (eski / ad / "server.py").exists() and not (yeni / ad).exists():
            shutil.copytree(eski / ad, yeni / ad, ignore=shutil.ignore_patterns("__pycache__"))
            tasinan.append(ad)
    return tasinan


def paket_guncelle(manifest: dict, indirici) -> bool:
    yeni, etkin = manifest["surum"], ortak.aktif() or (ortak.surumler() or ["0"])[-1]
    if ortak.surum_demeti(yeni) <= ortak.surum_demeti(etkin):
        return False
    p = manifest["paket"]
    indirilen = ortak.VERI / "indirilen" / p["dosya"]
    sha = indirici(p["dosya"], indirilen)
    if sha != p["sha256"]:
        indirilen.unlink(missing_ok=True)
        raise GuncellemeHatasi(f"paket sha256 uyuşmadı ({p['dosya']})")
    surumler = ortak.KOK / "surumler"
    gecici = surumler / f"{yeni}.yeni"
    shutil.rmtree(gecici, ignore_errors=True)
    _guvenli_ac(indirilen, gecici)
    if (gecici / "surum.txt").read_text(encoding="utf-8").strip() != yeni or not (gecici / "istemci" / "arthurlegal_sunucu.py").exists():
        shutil.rmtree(gecici, ignore_errors=True)
        raise GuncellemeHatasi("paket içeriği beklenen sürümle uyuşmuyor")
    tasinan = yerel_bilesenleri_tasi(surumler / etkin, gecici)
    shutil.rmtree(surumler / yeni, ignore_errors=True)
    os.replace(gecici, surumler / yeni)
    ortak.aktif_yaz(yeni)
    indirilen.unlink(missing_ok=True)
    for eski in ortak.surumler()[:-2]:  # etkin + bir önceki kalır
        shutil.rmtree(surumler / eski, ignore_errors=True)
    ortak.gunluk("guncelle", f"paket {etkin} -> {yeni}" + (f"; yerel bileşen taşındı: {', '.join(tasinan)}" if tasinan else ""))
    return True


def mask_mac_engeli() -> str:
    """ArthurMask'in Mac sürümü Apple Silicon ve macOS 14 (Sonoma) ister. Uymuyorsa nedeni, uyuyorsa boş."""
    arm = subprocess.run(["sysctl", "-n", "hw.optional.arm64"], capture_output=True, text=True).stdout.strip() == "1"
    if not arm:
        return "ArthurMask Mac'te yalnız Apple Silicon'da çalışır"
    import platform
    try:
        ana = int((platform.mac_ver()[0] or "0").split(".")[0])
    except ValueError:
        ana = 0
    return "" if ana >= 14 else "ArthurMask Mac'te macOS 14 (Sonoma) ya da sonrasını ister"


def mac_mask_kur(manifest: dict) -> str:
    """macOS: ArthurMask'i ilk kez kurar (kurulumda seçildiyse; Apple Silicon ve macOS 14'te). Disk görüntüsü
    indirilir, sha256'sı imzalı manifestteki değerle (mask_macos) doğrulanır, uygulama Uygulamalar klasörüne kopyalanır
    (yazılamıyorsa ~/Applications) ve ArthurMask'in kendi aracıyla Claude Desktop'a kaydedilir. Kurulu ArthurMask
    güncellemesini kendisi yapar; buraya karışılmaz. Bu yolla indirilen dosya karantina işareti taşımaz."""
    kurulu = ortak.mask_surumu()
    if kurulu:
        return f"mask: kurulu ({kurulu}); ArthurMask Mac'te güncellemesini kendisi yapar"
    if "mask" not in ortak.moduller():
        return "mask: kurulumda seçilmedi"
    engel = mask_mac_engeli()
    if engel:
        return f"mask: {engel}"
    m = manifest.get("mask_macos")
    if not m:
        return "mask: manifest'te macOS sürümü yok"
    dmg = ortak.VERI / "indirilen" / f"ArthurMask-Kurulum-{m['surum']}.dmg"
    if not (dmg.exists() and ortak.sha256_dosya(dmg) == m["sha256"]):
        if ortak.indir(m["url"], dmg, zaman=120) != m["sha256"]:
            dmg.unlink(missing_ok=True)
            raise GuncellemeHatasi("ArthurMask (macOS) sha256 uyuşmadı")
    import tempfile
    nokta = Path(tempfile.mkdtemp(prefix="arthurmask-"))
    subprocess.run(["hdiutil", "attach", "-nobrowse", "-readonly", "-noautoopen", "-mountpoint", str(nokta), str(dmg)],
                   check=True, capture_output=True, timeout=600)
    try:
        kok = Path("/Applications") if os.access("/Applications", os.W_OK) else Path.home() / "Applications"
        kok.mkdir(parents=True, exist_ok=True)
        # Mask 1.1.3 ve sonrası paketi "ArthurMask.app" adıyla taşır; 1.1.2 ve öncesi ayrı yazılmış eski adla.
        kaynak = next((nokta / ad for ad in ortak.MASK_UYGULAMA_ADLARI if (nokta / ad).is_dir()),
                      nokta / ortak.MASK_UYGULAMA_ADLARI[0])
        hedef = kok / kaynak.name
        subprocess.run(["ditto", str(kaynak), str(hedef)], check=True, capture_output=True, timeout=1800)
    finally:
        subprocess.run(["hdiutil", "detach", str(nokta), "-force"], capture_output=True, timeout=300)
        shutil.rmtree(nokta, ignore_errors=True)
    subprocess.run(["xattr", "-dr", "com.apple.quarantine", str(hedef)], capture_output=True, timeout=300)
    py = hedef / "Contents" / "Resources" / "runtime" / "bin" / "python3"
    # ArthurMask'in kendi kurulumunun yaptığı gibi (modülü derlenmiş olduğundan -m ile değil, -c ile çağrılır).
    kayit = subprocess.run([str(py), "-I", "-B", "-c", "import sys; from arthur_mask.claude_ayari import main; "
                            "sys.exit(main(['kaydet']))"], capture_output=True, text=True, timeout=300)
    if kayit.returncode and kayit.stderr.strip():  # 1: zaten kayıtlı (değişen dosya yok)
        ortak.gunluk("guncelle", f"ArthurMask Claude kaydı {kayit.returncode}: {kayit.stderr.strip()[-300:]}")
    dmg.unlink(missing_ok=True)
    ortak.gunluk("guncelle", f"ArthurMask (macOS) {m['surum']} kuruldu: {hedef}")
    import mac
    # ChatGPT seçildiyse arthur-mask girdisini ChatGPT ayarına kur --kaydet yazar (codex_ayari; güncelleme sonunda).
    uyg = {"claude": ("Claude Desktop'tan", "Claude Desktop", "Claude Desktop-dan"),
           "chatgpt": ("ChatGPT'den", "ChatGPT", "ChatGPT-dən"),
           "ikisi": ("Claude Desktop'tan ve ChatGPT'den", "Claude Desktop and ChatGPT", "Claude Desktop-dan və ChatGPT-dən")
           }[ortak.asistan_anahtari()]
    mac.bildirim("ArthurMask", ortak.metin(
        f"ArthurMask kuruldu. {uyg[0]} Cmd+Q ile çıkıp yeniden açın; araçları o zaman görünür.",
        f"ArthurMask is installed. Quit {uyg[1]} with Cmd+Q and open it again to see its tools.",
        f"ArthurMask quraşdırıldı. {uyg[2]} Cmd+Q ilə çıxıb yenidən açın; alətləri onda görünəcək."))
    return f"mask: {m['surum']} kuruldu"


def mask_guncelle(manifest: dict) -> str:
    if ortak.MAC:
        return mac_mask_kur(manifest)
    m = manifest.get("mask")
    if not m:
        return "mask: manifest'te yok"
    kurulu = ortak.mask_surumu()
    if kurulu and ortak.surum_demeti(kurulu) >= ortak.surum_demeti(m["surum"]):
        return f"mask: güncel ({kurulu})"
    if not kurulu and "mask" not in ortak.moduller():
        # Kurulumda seçilmedi: kurulu değilse indirilmez. Kendi kurulumuyla eklenmiş bir ArthurMask ise güncellenir.
        return "mask: kurulumda seçilmedi"
    if ortak.akilli_denetim_acik() and not m.get("imzali"):
        # Denetim imzasız kurulumu engeller: ~1 GB boşuna iner ve her denetimde engellenen kurulum yeni bir Windows
        # uyarısı gösterirdi (zip yoluyla kurulan bilgisayarlar). Denetim kapatılırsa ya da ArthurMask kurulumu
        # imzalanırsa (manifest: mask.imzali) bir sonraki denetimde iner. Önceki denemeden kalan dosya silinir.
        for eski in (ortak.VERI / "indirilen").glob("ArthurMask-Kurulum-*.exe*"):
            eski.unlink(missing_ok=True)
        return "mask: Akıllı Uygulama Denetimi açık, ArthurMask bu bilgisayarda kurulamaz"
    exe = ortak.VERI / "indirilen" / f"ArthurMask-Kurulum-{m['surum']}.exe"
    if not (exe.exists() and ortak.sha256_dosya(exe) == m["sha256"]):
        if ortak.indir(m["url"], exe, zaman=120) != m["sha256"]:
            exe.unlink(missing_ok=True)
            raise GuncellemeHatasi("ArthurMask sha256 uyuşmadı")
    if ortak.asistan_calisiyor():  # açık uygulama ArthurMask köprüsünü kullanıyor olabilir (Claude ya da ChatGPT)
        return "mask: indirildi, " + {"claude": "Claude Desktop", "chatgpt": "ChatGPT",
                                       "ikisi": "Claude Desktop ve ChatGPT"}[ortak.asistan_anahtari()] + " kapanınca kurulacak"
    sonuc = subprocess.run([str(exe), "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART", "/SP-"],
                           creationflags=ortak.PENCERESIZ, timeout=3600)
    if sonuc.returncode != 0:
        raise GuncellemeHatasi(f"ArthurMask kurulumu {sonuc.returncode} ile bitti")
    exe.unlink(missing_ok=True)
    ortak.gunluk("guncelle", f"ArthurMask {kurulu or 'yok'} -> {m['surum']}")
    return f"mask: {m['surum']} kuruldu"


def _claude_kaydet(guncellendi: bool = False) -> None:
    """Etkin (belki yeni) sürümün kodu ile Claude Desktop kaydını (ChatGPT seçildiyse ChatGPT ayarını ve becerilerini
    de; kur.asistan_kayitlari) tazeler. Paket güncellendiyse kısayollar ve
    programlar listesi yeni sürümün koduyla, onun numarasıyla yeniden yazılır; güncellenmediyse yalnız başka
    numara taşıyan (yarım kalmış bir güncellemeden kalan) kısayollar çalışan sürüme eşitlenir. Numara hep
    çalışan kodun surum.txt'sinden gelir: güncelleme olmadıysa ad değişmez."""
    py = ortak.python_yolu()
    if py.exists():
        subprocess.run([str(py), "-B", str(ortak.AL), "kur", "--kaydet", "--kisayol" if guncellendi else "--kisayol-esitle"],
                       creationflags=ortak.PENCERESIZ, timeout=180)


# --- Arayüzlerin "Güncellemeleri denetle" düğmesi (3.3.1) -------------------------------------------------------
# Dört arayüz (masa, ArthurMask, UYAP Dashboard, ArthurTapu) GitHub'a kendileri bağlanmaz: bu komutu alt süreç olarak
# çağırır (al.py guncelle --denetle --json). Hiçbir şey indirilmez ya da kurulmaz; yalnız imzalı manifest okunur ve
# kurulu sürümlerle karşılaştırılır. Sonuç bir saat saklanır: bürodaki bilgisayarlar aynı IP'yi paylaşsa da GitHub'a
# her düğme basışında gidilmez (--zorla hariç).
DENETIM_DOSYASI = "guncelleme-denetimi.json"
DENETIM_ONBELLEK_SN = 3600
MODUL_ADLARI = ("al", "masa", "tapu", "uyap", "mask")
GUVENLI_ONEK = "https://github.com/beerbottle90/"
KURULUM_SAYFASI = GUVENLI_ONEK + "ArthurLegal#indir"
KURULUM_SAYFASI_MAC = GUVENLI_ONEK + "ArthurLegal#mac"
MASK_SAYFASI = GUVENLI_ONEK + "ArthurLegal/releases/tag/arthur-mask"
YENILIK_SINIRI = 5


def _masa_surumu() -> str | None:
    """Kurulu masanın sürümü: paketin icerik.json'u (3.3.1+), yoksa masa kodundaki SURUM sabiti."""
    s = ortak.json_oku(ortak.SURUM_DIZINI / "icerik.json").get("bilesenler", {}).get("masa")
    if s:
        return str(s)
    try:
        import re
        kod = (ortak.SURUM_DIZINI / "istemci" / "arayuz" / "al_arayuz.py").read_text(encoding="utf-8")
        m = re.search(r'^SURUM\s*=\s*"([^"]+)"', kod, re.M)
        return m.group(1) if m else None
    except OSError:
        return None


def kurulu_surumler() -> dict:
    bilesen = ortak.json_oku(ortak.SURUM_DIZINI / "icerik.json").get("bilesenler", {})
    kurulu = {"al": ortak.surum(), "masa": _masa_surumu(), "tapu": bilesen.get("tapu"), "uyap": bilesen.get("uyap")}
    try:
        kurulu["mask"] = ortak.mask_surumu()
    except OSError:
        kurulu["mask"] = None
    return {k: str(v) for k, v in kurulu.items() if v and v not in ("?", "0.0.0")}


def yenilikleri_temizle(veri) -> dict:
    """{"tr": [...], "az": [...], "en": [...]}: yalnız tanınan diller, en çok beş kısa madde."""
    if not isinstance(veri, dict):
        return {}
    temiz = {}
    for d in ortak.DILLER:
        liste = veri.get(d)
        if isinstance(liste, list):
            maddeler = [" ".join(str(m).split())[:200] for m in liste if isinstance(m, str) and m.strip()]
            if maddeler:
                temiz[d] = maddeler[:YENILIK_SINIRI]
    return temiz


def _son_surumler(manifest: dict) -> dict:
    bilesen = (manifest.get("icerik") or {}).get("bilesenler") or {}
    mask = manifest.get("mask_macos" if ortak.MAC else "mask") or {}
    son = {"al": manifest.get("surum"), "masa": bilesen.get("masa"), "tapu": bilesen.get("tapu"),
           "uyap": bilesen.get("uyap"), "mask": mask.get("surum")}
    return {k: str(v) for k, v in son.items() if v}


def _baglantilar() -> dict:
    baglanti = {"al": KURULUM_SAYFASI_MAC if ortak.MAC else KURULUM_SAYFASI, "mask": MASK_SAYFASI}
    return {k: v for k, v in baglanti.items() if v.startswith(GUVENLI_ONEK)}


def _guncelleme_durumu() -> dict:
    kilit = ortak.VERI / "guncelle.kilit"
    try:
        calisiyor = kilit.exists() and time.time() - kilit.stat().st_mtime < 7200
    except OSError:
        calisiyor = False
    d = ortak.durum()
    sonuc = {"calisiyor": calisiyor, "son_sonuc": str(d.get("son_sonuc") or "")}
    son = d.get("son_guncelleme")
    if isinstance(son, dict):
        sonuc["son_guncelleme"] = son
    # Yeni paket indi ama çalışan sunucu hâlâ eskisiyse: Claude Desktop yeniden açılınca devreye girer.
    calisan = d.get("calisan_surum")
    etkin = ortak.aktif()
    sonuc["yeniden_baslat"] = bool(calisan and etkin and ortak.surum_demeti(etkin) > ortak.surum_demeti(calisan))
    return sonuc


def denetle(zorla: bool = False, ayar: dict | None = None) -> dict:
    """Arayüzlerin düğmesi için sürüm karşılaştırması (bkz. sözleşme: SOZLESME ust serit). Hata da sözlük döner."""
    yol = ortak.VERI / DENETIM_DOSYASI
    kayit = ortak.json_oku(yol)
    kayit = kayit if isinstance(kayit, dict) else {}
    onbellek = (not zorla and isinstance(kayit.get("denetim"), (int, float)) and not kayit.get("hata")
                and 0 <= time.time() - kayit["denetim"] < DENETIM_ONBELLEK_SN and isinstance(kayit.get("son"), dict))
    hata = ""
    if not onbellek:
        try:
            manifest, _ = manifest_getir(ayar or ortak.ayar())
            if manifest is None:
                hata = "yayında manifest yok"
            else:
                kayit = {"denetim": time.time(), "son": _son_surumler(manifest),
                         "yenilikler": yenilikleri_temizle(manifest.get("yenilikler"))}
        except GuncellemeHatasi as e:
            hata = str(e)
        except (OSError, ValueError, KeyError) as e:
            hata = "internet yok ya da GitHub yanıt vermedi" if isinstance(e, OSError) else f"manifest okunamadı ({e})"
        if hata:
            ortak.gunluk("guncelle", f"denetim hatası: {hata}")
            kayit = {**{k: kayit[k] for k in ("son", "yenilikler") if k in kayit}, "denetim": time.time(), "hata": hata}
        try:
            ortak.json_yaz(yol, kayit)
        except OSError:
            pass
    kurulu = kurulu_surumler()
    son = kayit.get("son") if isinstance(kayit.get("son"), dict) else {}
    yeni = [m for m in MODUL_ADLARI
            if m in kurulu and son.get(m) and ortak.surum_demeti(son[m]) > ortak.surum_demeti(kurulu[m])]
    sonuc = {"durum": "hata" if hata else ("yeni" if yeni else "guncel"), "denetim": int(kayit.get("denetim") or 0),
             "onbellek": onbellek, "kurulu": kurulu, "son": son, "yeni": yeni,
             "yenilikler": kayit.get("yenilikler") or {}, "baglanti": _baglantilar(),
             "guncelleme": _guncelleme_durumu()}
    if hata:
        sonuc["hata"] = hata
    return sonuc


def kurulu_yenilikler() -> dict:
    """Kurulu paketin "Yenilikler"i (yenilikler.json; derle.py etkin sürümün maddelerini koyar)."""
    veri = ortak.json_oku(ortak.SURUM_DIZINI / "yenilikler.json")
    return {"surum": ortak.surum(), "yenilikler": yenilikleri_temizle(veri)}


def _ev_gizle(metin: str) -> str:
    ev = str(Path.home())
    return metin.replace(ev, "~").replace(ev.replace("\\", "/"), "~")


def son_hatalar(sinir: int = 5) -> list:
    """Günlükten destek için son hata satırları: yalnız güncelleyici ve sunucu, kısaltılmış, ev klasörü gizli."""
    satirlar = []
    for ad in ("guncelle", "sunucu"):
        try:
            metin = (ortak.VERI / "gunluk" / f"{ad}.log").read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for s in metin.splitlines():
            if "hata" in s.lower() or "error" in s.lower():
                satirlar.append(f"{s[:19]} {ad}: {_ev_gizle(s[20:])[:200]}")
    return sorted(satirlar)[-sinir:]


def tani() -> dict:
    """"Sistem bilgisini kopyala" için: sürümler, işletim sistemi, dil, modüller, son denetim. Belge, müvekkil ya da
    UYAP dosya bilgisi girmez."""
    import platform
    d = ortak.durum()
    if ortak.MAC:
        isletim = f"macOS {platform.mac_ver()[0]}"
    elif sys.platform == "win32":
        isletim = f"Windows {platform.release()} {platform.version()}"
    else:
        isletim = f"{platform.system()} {platform.release()}"
    son_denetim = d.get("son_denetim")
    return {"urun": ortak.urun_adi(), "surumler": kurulu_surumler(), "isletim_sistemi": isletim,
            "mimari": platform.machine(), "python": platform.python_version(), "dil": ortak.arayuz_dili(),
            "moduller": ortak.moduller(),
            "son_denetim": time.strftime("%Y-%m-%d %H:%M", time.localtime(son_denetim))
            if isinstance(son_denetim, (int, float)) else "",
            "son_sonuc": _ev_gizle(str(d.get("son_sonuc") or ""))[:300], "son_hatalar": son_hatalar()}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal güncelleyici")
    ap.add_argument("--sessiz", action="store_true", help="arka plan çalıştırması")
    ap.add_argument("--mask-yok", action="store_true", help="ArthurMask'e dokunma")
    ap.add_argument("--bildir", action="store_true", help="sonucu bildirimle göster (macOS: Güncellemeleri Denetle)")
    ap.add_argument("--denetle", action="store_true", help="yalnız denetle (indirmez, kurmaz); arayüz düğmesi için")
    ap.add_argument("--zorla", action="store_true", help="--denetle: bir saatlik saklanan sonucu kullanma")
    ap.add_argument("--tani", action="store_true", help="destek için sistem bilgisi")
    ap.add_argument("--yenilikler", action="store_true", help="kurulu sürümün Yenilikler'i")
    ap.add_argument("--json", action="store_true", help="--denetle/--tani/--yenilikler: tek satır JSON")
    args = ap.parse_args(argv)
    if args.denetle or args.tani or args.yenilikler:
        veri = denetle(args.zorla) if args.denetle else (tani() if args.tani else kurulu_yenilikler())
        print(json.dumps(veri, ensure_ascii=False) if args.json else json.dumps(veri, ensure_ascii=False, indent=1))
        return 0

    kilit = ortak.VERI / "guncelle.kilit"
    kilit.parent.mkdir(parents=True, exist_ok=True)
    try:
        if kilit.exists() and time.time() - kilit.stat().st_mtime > 7200:
            kilit.unlink()
        fd = os.open(kilit, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError:
        return 0  # başka bir güncelleyici çalışıyor
    try:
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        ortak.durum_guncelle(son_denetim=time.time())
        sonuclar = []
        guncellendi = False
        try:
            manifest, indirici = manifest_getir(ortak.ayar())
            if manifest is None:
                sonuclar.append("yayında manifest yok")
            else:
                onceki = ortak.aktif() or (ortak.surumler() or ["?"])[-1]
                guncellendi = paket_guncelle(manifest, indirici)
                if guncellendi:
                    # Yalnız paket doğrulanıp etkin sürüm değiştikten sonra: panel bunu "son güncelleme" diye gösterir.
                    ortak.durum_guncelle(son_guncelleme={"zaman": time.time(), "onceki": onceki,
                                                         "yeni": manifest["surum"]})
                sonuclar.append(f"paket {manifest['surum']} kuruldu" if guncellendi
                                else f"paket güncel ({ortak.aktif()})")
                if not args.mask_yok:
                    sonuclar.append(mask_guncelle(manifest))
        except (GuncellemeHatasi, OSError, ValueError, KeyError, subprocess.SubprocessError) as e:
            sonuclar.append(f"hata: {e}")
            ortak.gunluk("guncelle", f"hata: {e!r}")
        # macOS'ta ArthurMask'i bu kurulum kurar: masaüstü takma adı için kısayollar yeniden yazılır.
        mask_kuruldu = ortak.MAC and any(s.startswith("mask: ") and s.endswith(" kuruldu") for s in sonuclar)
        _claude_kaydet(guncellendi or mask_kuruldu)
        ortak.durum_guncelle(son_sonuc="; ".join(sonuclar))
        if not args.sessiz:
            print("\n".join(sonuclar))
        if args.bildir and ortak.MAC:
            import mac
            mac.bildirim(ortak.urun_adi(), "; ".join(sonuclar))
        return 1 if any(s.startswith("hata") for s in sonuclar) else 0
    finally:
        kilit.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
