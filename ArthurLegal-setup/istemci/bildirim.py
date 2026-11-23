"""Masaya cevap gelince bilgisayar bildirimi (23.11.2026).

Kullanıcı isteği: "her cevap geldiğinde kullanıcı notification ile bilgilendirilmeli". Claude cevabın tamamını
al_masaya_yaz aracının girdisine yazar; uzun cevapta bu bir iki dakika sürer, kullanıcı o arada başka işe geçer.
Teslim bu bilgisayardaki kurulumdan geçtiği için bildirim de buradan gider: Windows'ta işlem merkezi bildirimi,
macOS'ta Bildirim Merkezi.

Bildirimde sorunun ve cevabın metni yoktur: müvekkil bilgisi kilit ekranına ve Windows'un bildirim geçmişine
yazılmaz; yalnız cevabın masaya geldiği söylenir. Kapatmak için ayar.json'da "bildirim": false.

Windows'ta bildirimin uygulama adı (ArthurLegal) ve simgesi bu kullanıcının kayıt defterinde bir uygulama kimliğiyle
tanıtılır (HKCU\\Software\\Classes\\AppUserModelId\\ArthurLegal.Masa); kaldırma (kur --kaldir) siler. Bildirimi
Windows PowerShell gösterir (pencere açmadan); tıklanınca Claude (ya da ChatGPT) öne gelir.
"""
from __future__ import annotations

import base64
import os
import subprocess
import sys
import threading
import time
from xml.sax.saxutils import escape

import ortak

UYGULAMA_KIMLIGI = "ArthurLegal.Masa"
KAYIT_YOLU = "Software\\Classes\\AppUserModelId\\" + UYGULAMA_KIMLIGI
ARALIK = 10.0   # saniye: aynı cevap iki kez teslim edilirse tek bildirim

METINLER = {
    "tr": {"claude": "Cevabınız masada. Claude'daki ArthurLegal Masası'nda okuyabilirsiniz.",
           "chatgpt": "Cevabınız masada. ChatGPT'deki ArthurLegal Masası'nda okuyabilirsiniz."},
    "az": {"claude": "Cavabınız masadadır. Claude-dakı ArthurLegal Masasında oxuya bilərsiniz.",
           "chatgpt": "Cavabınız masadadır. ChatGPT-dəki ArthurLegal Masasında oxuya bilərsiniz."},
    "en": {"claude": "Your answer is on the desk. Read it in the ArthurLegal Desk in Claude.",
           "chatgpt": "Your answer is on the desk. Read it in the ArthurLegal Desk in ChatGPT."},
}
TIKLAMA = {"claude": "claude://", "chatgpt": ""}

_son = 0.0
_kilit = threading.Lock()


def acik() -> bool:
    if os.environ.get("AL_BILDIRIM") == "0":
        return False
    try:
        return ortak.ayar().get("bildirim", True) is not False
    except (OSError, ValueError):
        return True


def metin(dil: str | None, ev: str | None) -> tuple[str, str]:
    d = METINLER.get(dil or "tr") or METINLER["tr"]
    return "ArthurLegal", d["chatgpt" if ev == "chatgpt" else "claude"]


def _simge() -> str:
    yol = ortak.KOK / "bin" / "arthurlegal.ico"
    return str(yol) if yol.exists() else ""


def windows_kimligi() -> bool:
    """Bildirimin ArthurLegal adıyla görünmesi için uygulama kimliği (bu kullanıcıda, bir kez)."""
    try:
        import winreg
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, KAYIT_YOLU) as k:
            winreg.SetValueEx(k, "DisplayName", 0, winreg.REG_SZ, "ArthurLegal")
            simge = _simge()
            if simge:
                winreg.SetValueEx(k, "IconUri", 0, winreg.REG_SZ, simge)
        return True
    except OSError as e:
        ortak.gunluk("bildirim", f"uygulama kimliği yazılamadı: {e!r}")
        return False


def windows_kimligini_sil() -> None:
    try:
        import winreg
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, KAYIT_YOLU)
    except OSError:
        pass


def windows_betigi(baslik: str, govde: str, tikla: str) -> str:
    """Windows PowerShell 5.1 ile işlem merkezi bildirimi (WinRT); metinler XML olarak kaçırılır."""
    acilis = f' activationType="protocol" launch="{escape(tikla)}"' if tikla else ""
    xml = (f'<toast{acilis}><visual><binding template="ToastGeneric"><text>{escape(baslik)}</text>'
           f'<text>{escape(govde)}</text></binding></visual></toast>')
    return ("$ErrorActionPreference = 'Stop'\n"
            "[void][Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]\n"
            "[void][Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime]\n"
            "$x = New-Object Windows.Data.Xml.Dom.XmlDocument\n"
            f"$x.LoadXml('{xml.replace(chr(39), chr(39) * 2)}')\n"
            "$t = New-Object Windows.UI.Notifications.ToastNotification $x\n"
            f"[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('{UYGULAMA_KIMLIGI}').Show($t)\n")


def _windows(baslik: str, govde: str, tikla: str) -> None:
    windows_kimligi()
    kod = base64.b64encode(windows_betigi(baslik, govde, tikla).encode("utf-16-le")).decode("ascii")
    sonuc = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                            "-EncodedCommand", kod], capture_output=True, timeout=60,
                           creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    if sonuc.returncode:
        ortak.gunluk("bildirim", f"Windows bildirimi gösterilemedi ({sonuc.returncode}): "
                                 f"{sonuc.stderr.decode('utf-8', 'replace').strip()[-300:]}")


def _goster(dil: str | None, ev: str | None) -> None:
    baslik, govde = metin(dil, ev)
    try:
        if sys.platform == "win32":
            _windows(baslik, govde, TIKLAMA.get("chatgpt" if ev == "chatgpt" else "claude", ""))
        elif sys.platform == "darwin":
            import mac
            mac.bildirim(baslik, govde)
    except (OSError, subprocess.SubprocessError) as e:   # bildirim çıkmazsa cevap yine masada
        ortak.gunluk("bildirim", f"bildirim gösterilemedi: {e!r}")


def cevap_geldi(dil: str | None = None, ev: str | None = None) -> bool:
    """Cevap masaya teslim edildi: arka planda bir bildirim. Kapalıysa ya da az önce gösterildiyse False."""
    global _son
    if not acik():
        return False
    with _kilit:
        if time.monotonic() - _son < ARALIK and _son:
            return False
        _son = time.monotonic()
    threading.Thread(target=_goster, args=(dil, ev), daemon=True).start()
    return True


if __name__ == "__main__":   # elle deneme: python bildirim.py [tr|az|en] [claude|chatgpt]
    _goster(sys.argv[1] if len(sys.argv) > 1 else "tr", sys.argv[2] if len(sys.argv) > 2 else "claude")
