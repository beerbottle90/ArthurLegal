"""Başlat menüsü ve masaüstü kısayollarının işleri.

    al.py kisayol baslat          ana simge: Claude Desktop'ı açar ve başlat panelini gösterir
    al.py kisayol tapu            Tapu arayüzü açıksa tarayıcıda gösterir, değilse başlatır
    al.py kisayol uyap-tarayici   UYAP için ayrı profilli tarayıcı (Brave varsa Brave, yoksa Edge)
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
import webbrowser
from pathlib import Path

import claude_ayari
import ortak
import proje

TAPU_ADRES = ("127.0.0.1", 8765)


def claude_ac() -> str:
    """Claude Desktop'ı başlatır. Zaten açıksa öne getirmeye çalışmaz, sadece durumu döndürür."""
    if ortak.claude_calisiyor():
        return "zaten açık"
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


def durum_yaz(claude_durumu: str | None = None) -> Path:
    """Başlat panelinin okuduğu durum dosyası (rehber/durum.js)."""
    if claude_durumu is None:
        import kur
        claude_durumu = "açık" if ortak.claude_calisiyor() else ("kurulu" if kur.claude_kurulu() else "bulunamadı")
    bilgi = ortak.json_oku(ortak.SURUM_DIZINI / "icerik.json")
    d = ortak.durum()
    kayitli = claude_ayari.kayitli()
    sunucular = sorted({s for adlar in kayitli.values() for s in adlar if s.startswith("arthur")})
    veri = {
        "surum": ortak.surum(),
        "paketler": bilgi.get("paketler", {}),
        "bilesenler": bilgi.get("bilesenler", {}),
        "mask": ortak.mask_surumu() or "",
        "sunucular": sunucular,
        "claude": claude_durumu,
        "son_denetim": time.strftime("%d.%m.%Y %H:%M", time.localtime(d["son_denetim"])) if d.get("son_denetim") else "",
        "son_sonuc": d.get("son_sonuc", ""),
        "proje_klasorleri": proje.durum(),
    }
    yol = ortak.KOK / "rehber" / "durum.js"
    yol.parent.mkdir(parents=True, exist_ok=True)
    yol.write_text("window.ARTHURLEGAL_DURUM = " + json.dumps(veri, ensure_ascii=False) + ";\n", encoding="utf-8")
    return yol


def baslat() -> int:
    durum_yaz(claude_ac())
    webbrowser.open((ortak.KOK / "rehber" / "baslangic.html").as_uri())
    return 0


def tapu() -> int:
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
        print("Bu kurulumda UYAP köprüsü yok.")
        return 1
    return subprocess.call(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(betik),
                            "-Tarayici", "brave" if brave else "edge"])


def knowledge() -> int:
    """Proje klasörlerini açar: Claude'da 'Use a folder' ile seçilir ya da dosyalar projeye sürüklenir."""
    proje.esitle()
    os.startfile(proje.kok())  # noqa: S606
    return 0


if __name__ == "__main__":
    islem = {"baslat": baslat, "tapu": tapu, "uyap-tarayici": uyap_tarayici, "knowledge": knowledge}.get(
        sys.argv[1] if len(sys.argv) > 1 else "")
    if not islem:
        sys.exit("kullanım: al.py kisayol baslat|tapu|uyap-tarayici|knowledge")
    sys.exit(islem())
