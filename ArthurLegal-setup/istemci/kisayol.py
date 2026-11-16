"""Başlat menüsü ve masaüstü kısayollarının işleri.

    al.py kisayol baslat          ana simge: Claude Desktop'ı ArthurLegal Masası mesajı yazılmış olarak açar
                                  ve her tıklamada başlat panelini tarayıcıda açar; klasik arayüzde Claude
                                  Desktop'ı ve başlat panelini açar
    al.py kisayol baslat adliye   Courthouse simgesi (akademisyen: Akademisyen simgesi): aynı iş; panel o paketin
                                  kartını öne çıkarır
    al.py kisayol masa            yalnız masa bağlantısı (claude://claude.ai/new?q=…)
    al.py kisayol chatgpt-masa    ChatGPT masaüstünde masa bağlantısı (codex://new?prompt=…); kurulu değilse indirme sayfası
                                  (kurulumda ChatGPT seçildiyse ana simge de bunu açar; ikisi seçildiyse panel iki düğmeyle)
    al.py kisayol mask            ArthurMask uygulamasını açar (masadaki düğme)
    al.py kisayol tapu            Tapu arayüzü açıksa tarayıcıda gösterir, değilse başlatır
    al.py kisayol uyap-tarayici   UYAP için ayrı profilli tarayıcı (Brave varsa Brave, yoksa Edge). Kısayolu
                                  yok: UYAP Dashboard girişi kendisi açar; elle çalıştırmak için durur
    al.py kisayol uyap-ekran      UYAP Dashboard: giriş, sabah taraması, son gün, uyuşmazlık, takvim; Claude'suz
    al.py kisayol knowledge       paket bilgi dosyalarını Gezgin'de açar (klasik Project yükleme yolu)
"""
from __future__ import annotations

import json
import os
import runpy
import socket
import subprocess
import sys
import time
import urllib.parse
import webbrowser
from pathlib import Path

import claude_ayari
import ortak
import proje

# Claude Desktop'ın resmî bağlantısı yeni sohbeti mesajı yazılmış olarak açar; kullanıcı Enter'a basar
# (bağlantı mesajı kendiliğinden göndermez). Claude mesajı yerel sunucudaki al_masasi aracına götürür.
MASA_ISTEMI = "ArthurLegal Masası'nı aç"
# Bağlantı modeli ya da effort'u seçemez (claude://claude.ai/new yalnız metin taşır). Mesajın ikinci satırı kullanıcıya,
# Enter'a basmadan önce, tam model menüsünün yanında hatırlatır; Claude son seçimi hatırladığı için bir kez seçmek yeter.
MODEL_ONERISI = Path(__file__).resolve().parent / "arayuz" / "ortak" / "tasarim" / "model-onerisi.json"

TAPU_ADRES = ("127.0.0.1", 8765)


def claude_ac() -> str:
    """Claude Desktop'ı başlatır. Zaten açıksa öne getirmeye çalışmaz, sadece durumu döndürür."""
    if ortak.claude_calisiyor():
        return "zaten açık"
    if ortak.MAC:
        r = subprocess.run(["open", "-a", "Claude"], capture_output=True, timeout=60)
        return "başlatıldı" if r.returncode == 0 else "bulunamadı"
    try:
        os.startfile("claude://")  # noqa: S606 — Claude Desktop'ın kendi protokolü
        return "başlatıldı"
    except OSError:
        pass
    klasik = Path(os.environ.get("LOCALAPPDATA", "")) / "AnthropicClaude" / "claude.exe"
    if klasik.exists():
        ortak.arka_planda([klasik])
        return "başlatıldı"
    try:  # Microsoft Store (MSIX) kurulumu
        kimlik = subprocess.run(["powershell", "-NoProfile", "-Command",
                                 "(Get-StartApps | Where-Object { $_.Name -like 'Claude*' } | Select-Object -First 1).AppID"],
                                capture_output=True, text=True, creationflags=ortak.PENCERESIZ, timeout=60).stdout.strip()
        if kimlik:
            subprocess.Popen(["explorer.exe", f"shell:AppsFolder\\{kimlik}"], creationflags=ortak.PENCERESIZ)
            return "başlatıldı"
    except (OSError, subprocess.SubprocessError):
        pass
    return "bulunamadı"


def chatgpt_ac() -> str:
    """ChatGPT masaüstünü başlatır (16.11.2026). Zaten açıksa yalnız durumu döndürür; kurulu değilse "bulunamadı"."""
    if not ortak.chatgpt_kurulu():
        return "bulunamadı"
    if ortak.chatgpt_calisiyor():
        return "zaten açık"
    if ortak.MAC:
        for ad in ("ChatGPT", "Codex"):
            if subprocess.run(["open", "-a", ad], capture_output=True, timeout=60).returncode == 0:
                return "başlatıldı"
        return "bulunamadı"
    try:
        kimlik = subprocess.run(["powershell", "-NoProfile", "-Command",
                                 "(Get-StartApps | Where-Object { $_.AppID -like 'OpenAI.Codex_*' } | Select-Object -First 1).AppID"],
                                capture_output=True, text=True, creationflags=ortak.PENCERESIZ, timeout=60).stdout.strip()
        subprocess.Popen(["explorer.exe", f"shell:AppsFolder\\{kimlik or ortak.CHATGPT_UYGULAMA_KIMLIGI}"],
                         creationflags=ortak.PENCERESIZ)
        return "başlatıldı"
    except (OSError, subprocess.SubprocessError):
        return "bulunamadı"


def chatgpt_durumu() -> str:
    return "açık" if ortak.chatgpt_calisiyor() else ("kurulu" if ortak.chatgpt_kurulu() else "bulunamadı")


def durum_yaz(claude_durumu: str | None = None, odak: str = "", chatgpt: str | None = None) -> Path:
    """Başlat panelinin okuduğu durum dosyası (rehber/durum.js). Panel seçilmeyen modüllerin bölümlerini gizler;
    ``odak`` (Courthouse ya da Akademisyen simgesi) o paketin kartını öne çıkarır. Seçilen asistanlar
    (ortak.asistanlar) panelde hangi uygulamanın adımlarının ve masa düğmelerinin görüneceğini belirler."""
    import codex_ayari
    asistanlar = ortak.asistanlar()
    if claude_durumu is None and "claude" in asistanlar:
        import kur
        claude_durumu = "açık" if ortak.claude_calisiyor() else ("kurulu" if kur.claude_kurulu() else "bulunamadı")
    if chatgpt is None and "chatgpt" in asistanlar:
        chatgpt = chatgpt_durumu()
    bilgi = ortak.json_oku(ortak.SURUM_DIZINI / "icerik.json")
    d = ortak.durum()
    klasik = ortak.arayuz() == "klasik"
    kayitli = claude_ayari.kayitli()
    # Yalnız ArthurLegal'in sunucuları (adı "arthur" ile başlayan başka bir araç, ör. arthurball, sayılmaz).
    sunucular = sorted({s for adlar in kayitli.values() for s in adlar if s in codex_ayari.ADLAR})
    sg = d.get("son_guncelleme") if isinstance(d.get("son_guncelleme"), dict) else {}
    veri = {
        "surum": ortak.surum(),
        "urun": ortak.urun_adi(),
        # Yalnız doğrulanmış güncelleme (guncelle.py); kurulumdan beri güncelleme yoksa boş.
        "son_guncelleme": (time.strftime("%d.%m.%Y %H:%M", time.localtime(sg["zaman"])) + " · "
                           + str(sg.get("onceki", "?")) + " → " + str(sg.get("yeni", "?"))) if sg.get("zaman") else "",
        # Claude Desktop'taki yerel sunucunun açılışta yazdığı sürüm: güncelleme kurulu ama Claude yeniden
        # açılmadıysa burada eski numara görünür.
        "calisan_surum": d.get("calisan_surum", ""),
        "paketler": {p: s for p, s in bilgi.get("paketler", {}).items() if p in ortak.moduller()},
        "bilesenler": bilgi.get("bilesenler", {}),
        "moduller": ortak.moduller(),
        "arayuz": ortak.arayuz(),  # klasikte panel masa paragrafını gizler
        "uyap": ortak.uyap_acik(),  # UYAP Dashboard maddesi yalnız kurulduğu bilgisayarda
        "odak": odak if odak in ortak.PAKETLER else "",
        "isletim": "mac" if ortak.MAC else "windows",  # sayfa Mac'e özgü cümleleri buna göre gösterir
        "mask": ortak.mask_surumu() or "",
        "sunucular": sunucular,
        "claude": claude_durumu or "",
        # ChatGPT masaüstü (K21, K29): seçilen uygulamalar, ChatGPT'nin durumu, oradaki AL sunucuları ve becerileri,
        # masa düğmelerinin bağlantıları (ikisi seçildiyse panel iki düğme gösterir).
        "asistanlar": asistanlar,
        "chatgpt": chatgpt or "",
        "chatgpt_sunucular": [s for s in codex_ayari.kayitli() if s in codex_ayari.ADLAR] if chatgpt else [],
        "chatgpt_beceriler": len(codex_ayari.beceriler_kayitli()) if chatgpt else 0,
        "chatgpt_indirme": ortak.CHATGPT_INDIRME,
        # Klasik arayüzde düğme yalnız uygulamayı açar (masa mesajı yazılmaz).
        "masa_claude": ("claude://" if klasik else masa_adresi()) if "claude" in asistanlar else "",
        "masa_chatgpt": ("codex://" if klasik else chatgpt_masa_adresi()) if "chatgpt" in asistanlar else "",
        "son_denetim": time.strftime("%d.%m.%Y %H:%M", time.localtime(d["son_denetim"])) if d.get("son_denetim") else "",
        "son_sonuc": d.get("son_sonuc", ""),
        "proje_klasorleri": proje.durum(),
    }
    yol = ortak.KOK / "rehber" / "durum.js"
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text("window.ARTHURLEGAL_DURUM = " + json.dumps(veri, ensure_ascii=False) + ";\n", encoding="utf-8")
    return yol


def model_notu() -> str:
    """Önerilen model ve effort, masanın okuduğu dosyadan (arayuz/ortak/tasarim/model-onerisi.json). Dosya yoksa
    ya da okunamıyorsa (eski arayüz kopyası) not eklenmez: mesaj eskisi gibi tek satırdır."""
    try:
        o = json.loads(MODEL_ONERISI.read_text(encoding="utf-8"))
        cumle, cumle_en = str(o["cumle"]), str(o["cumle_en"])
        cumle_az = str(o.get("cumle_az") or "")  # eski arayüz kopyasında yoksa Azerbaycanca kurulumda Türkçesi yazılır
    except (OSError, ValueError, KeyError, TypeError):
        return ""
    # Öneri tavsiyedir, bağlayıcı değildir: cümle dosyadaki hâliyle (kullanıcının kesinleştirdiği metin) yazılır.
    return ortak.metin(
        f"({cumle} Bu kutudaki model menüsünden bir kez seçmeniz yeter; Claude hatırlar.)",
        f"({cumle_en} Choose once in the model menu of this box; Claude remembers.)",
        f"({cumle_az} Bu qutudakı model menyusundan bir dəfə seçməyiniz kifayətdir; Claude yadda saxlayır.)"
        if cumle_az else None)


def masa_adresi() -> str:
    hatirlatma = model_notu()
    return "claude://claude.ai/new?q=" + urllib.parse.quote(MASA_ISTEMI + ("\n\n" + hatirlatma if hatirlatma else ""),
                                                            safe="")


def chatgpt_model_notu() -> str:
    """ChatGPT için model cümlesi (K14): ChatGPT modelleriyle ölçüm yapılmadı, en yetenekli güncel model tavsiye
    edilir. Dosyada yoksa not eklenmez."""
    try:
        o = json.loads(MODEL_ONERISI.read_text(encoding="utf-8"))
        cumle, cumle_en = str(o["cumle_chatgpt"]), str(o["cumle_chatgpt_en"])
        cumle_az = str(o.get("cumle_chatgpt_az") or "")
    except (OSError, ValueError, KeyError, TypeError):
        return ""
    return "(" + ortak.metin(cumle, cumle_en, cumle_az or None) + ")"


def chatgpt_masa_adresi() -> str:
    """ChatGPT masaüstünün resmî bağlantısı (codex://new?prompt=…) yeni sohbeti mesajı yazılmış olarak açar; kullanıcı
    Enter'a basar. ChatGPT mesajı ArthurLegal kural becerisi ve yerel sunucudaki al_masasi aracına götürür (K24)."""
    hatirlatma = chatgpt_model_notu()
    return "codex://new?prompt=" + urllib.parse.quote(MASA_ISTEMI + ("\n\n" + hatirlatma if hatirlatma else ""), safe="")


def _ac(adres: str) -> int:
    try:
        if ortak.MAC:
            return 0 if subprocess.run(["open", adres], capture_output=True, timeout=60).returncode == 0 else 1
        os.startfile(adres)  # noqa: S606 — uygulamanın kendi protokolü (claude://, codex://)
        return 0
    except (OSError, subprocess.SubprocessError):
        return 1


def masa() -> int:
    """Claude Desktop'ı ArthurLegal Masası mesajıyla açar. Açılamazsa 1 (Claude Desktop yok ya da eski)."""
    return _ac(masa_adresi())


def chatgpt_masa() -> int:
    """ChatGPT masaüstünü ArthurLegal Masası mesajıyla açar. Kurulu değilse resmî indirme sayfası açılır (K28)."""
    if not ortak.chatgpt_kurulu():
        webbrowser.open(ortak.CHATGPT_INDIRME)
        return 1
    return _ac(chatgpt_masa_adresi())


def baslat(profil: str = "") -> int:
    """Setup → Çalıştır → AL Masası. Başlat paneli (başlangıç sayfası) simgeye her tıklamada tarayıcıda açılır;
    yeni arayüzde önce masa bağlantısı açılır. Kurulumda "Claude Desktop klasik" seçildiyse 2.6'daki gibi yalnız
    uygulamayı ve başlat panelini açar. Kurulumda seçilen uygulamada açılır (ortak.asistanlar): Claude ya da ChatGPT;
    ikisi seçildiyse yalnız panel açılır, masa orada iki düğmeyle seçilen uygulamada açılır (K29, 16.11.2026).
    ChatGPT seçilip kurulu değilse resmî indirme sayfası da açılır (K28)."""
    secim = ortak.asistan_anahtari()
    klasik = ortak.arayuz() == "klasik"
    if secim == "claude":
        durum_yaz(claude_ac(), profil)
        if not klasik:
            masa()
    elif secim == "chatgpt":
        if not ortak.chatgpt_kurulu():
            durum_yaz(odak=profil, chatgpt="bulunamadı")
            webbrowser.open(ortak.CHATGPT_INDIRME)
        elif klasik:
            durum_yaz(odak=profil, chatgpt=chatgpt_ac())
        else:
            durum_yaz(odak=profil, chatgpt=chatgpt_durumu())
            chatgpt_masa()
    else:
        durum_yaz(odak=profil)
    webbrowser.open(ortak.rehber_dosyasi().as_uri())
    return 0


def mask() -> int:
    """ArthurMask uygulamasını açar (masadaki "ArthurMask'i aç" düğmesi)."""
    if ortak.MAC:
        app = ortak.mask_uygulamasi()
        if app:
            return 0 if subprocess.run(["open", str(app)], capture_output=True, timeout=60).returncode == 0 else 1
    else:
        programlar = Path(os.environ.get("APPDATA", "")) / "Microsoft" / "Windows" / "Start Menu" / "Programs"
        for ad in ("ArthurMask.lnk", "Arthur Mask.lnk"):  # Mask 1.1.2 ve öncesi kısayolu ayrı yazılmış adla kurar
            lnk = programlar / ad
            if lnk.exists():
                os.startfile(str(lnk))  # noqa: S606 — ArthurMask kurulumunun kendi kısayolu
                return 0
    print(ortak.metin("ArthurMask bu bilgisayarda kurulu değil.", "ArthurMask is not installed on this computer.",
                      "ArthurMask bu kompüterdə quraşdırılmayıb."))
    return 1


def tapu() -> int:
    if not ortak.bilesen_var("tapu"):
        print(ortak.metin("Bu kurulumda ArthurLegal Tapu seçilmedi.", "ArthurLegal Tapu was not selected in this installation.",
                          "Bu quraşdırmada ArthurLegal Tapu seçilməyib."))
        return 1
    try:
        socket.create_connection(TAPU_ADRES, 1).close()
        webbrowser.open(f"http://{TAPU_ADRES[0]}:{TAPU_ADRES[1]}/")
        return 0
    except OSError:
        pass
    dizin = ortak.SURUM_DIZINI / "tapu"
    sys.path.insert(0, str(dizin))
    sys.argv = [str(dizin / "server.py"), "--ui"]
    runpy.run_path(sys.argv[0], run_name="__main__")
    return 0


def uyap_tarayici() -> int:
    kokler = [os.environ.get(k, "") for k in ("LOCALAPPDATA", "ProgramFiles", "ProgramFiles(x86)")]
    brave = any((Path(k) / "BraveSoftware" / "Brave-Browser" / "Application" / "brave.exe").exists() for k in kokler if k)
    betik = ortak.SURUM_DIZINI / "uyap" / "araclar" / "tarayici_uyap.ps1"
    if not betik.exists():
        print(ortak.metin("Bu kurulumda UYAP köprüsü yok.", "This installation has no UYAP bridge.",
                          "Bu quraşdırmada UYAP körpüsü yoxdur."))
        return 1
    return subprocess.call(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(betik),
                            "-Tarayici", "brave" if brave else "edge"])


def uyap_ekran() -> int:
    """UYAP Dashboard ArthurMask'in Python'unda açılır: maskeleme orada. Ortam, Claude Desktop'taki UYAP
    kaydıyla aynıdır (claude_ayari): model indirilmez, kullanıcı paketleri karışmaz."""
    mask, ekran = ortak.mask_python(), ortak.SURUM_DIZINI / "uyap" / "ekran.py"
    if not mask or not ekran.exists():
        print(ortak.metin("Bu kurulumda UYAP Dashboard yok: UYAP köprüsü ve ArthurMask gerekir.",
                          "This installation has no UYAP Dashboard: it needs the UYAP bridge and ArthurMask.",
                          "Bu quraşdırmada UYAP Dashboard yoxdur: UYAP körpüsü və ArthurMask lazımdır."))
        return 1
    pencereli = mask.with_name("pythonw.exe")
    ortam = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONDONTWRITEBYTECODE": "1",
             "HF_HUB_OFFLINE": "1", "PYTHONNOUSERSITE": "1"}
    ortak.arka_planda([pencereli if pencereli.exists() else mask, "-B", ekran], ortam)
    return 0


def knowledge() -> int:
    """Proje klasörlerini açar: Claude'da 'Use a folder' ile seçilir ya da dosyalar projeye sürüklenir."""
    proje.esitle()
    if ortak.MAC:
        subprocess.run(["open", str(proje.kok())], timeout=60)
    else:
        os.startfile(proje.kok())  # noqa: S606
    return 0


if __name__ == "__main__":
    islem = {"baslat": baslat, "masa": masa, "chatgpt-masa": chatgpt_masa, "tapu": tapu, "mask": mask,
             "uyap-tarayici": uyap_tarayici, "uyap-ekran": uyap_ekran,
             "knowledge": knowledge}.get(sys.argv[1] if len(sys.argv) > 1 else "")
    if not islem:
        sys.exit("kullanım: al.py kisayol baslat [adliye|akademisyen]|masa|chatgpt-masa|tapu|mask|uyap-tarayici|"
                 "uyap-ekran|knowledge")
    sys.exit(islem(*sys.argv[2:3]) if islem is baslat else islem())
