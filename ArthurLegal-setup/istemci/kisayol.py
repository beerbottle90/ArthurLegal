"""Başlat menüsü ve masaüstü kısayollarının işleri.

    al.py kisayol tapu            Tapu arayüzü açıksa tarayıcıda gösterir, değilse başlatır
    al.py kisayol uyap-tarayici   UYAP için ayrı profilli tarayıcı (Brave varsa Brave, yoksa Edge)
"""
from __future__ import annotations

import os
import runpy
import socket
import subprocess
import sys
import webbrowser
from pathlib import Path

import ortak

TAPU_ADRES = ("127.0.0.1", 8765)


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
    return subprocess.call(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(betik),
                            "-Tarayici", "brave" if brave else "edge"])


if __name__ == "__main__":
    islem = {"tapu": tapu, "uyap-tarayici": uyap_tarayici}.get(sys.argv[1] if len(sys.argv) > 1 else "")
    if not islem:
        sys.exit("kullanım: al.py kisayol tapu|uyap-tarayici")
    sys.exit(islem())
