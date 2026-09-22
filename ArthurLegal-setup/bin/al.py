"""ArthurLegal başlatıcı.

Claude Desktop yapılandırması, kısayollar ve oturum açılışı hep bu dosyayı çağırır; etkin
sürüm klasörünü aktif.txt'den bulur. Güncellemeyle değişmez, o yüzden küçük tutulur.
Python 3.8+: kurulumun Python 3.12'siyle ve Arthur Mask'in 3.11'iyle (UYAP) çalışır.
Gömülü Python betiğin klasörünü sys.path'e eklemez; hedefin klasörünü burası ekler.
"""
import os
import re
import runpy
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEDEFLER = {
    "sunucu": ("istemci", "arthurlegal_sunucu.py"),
    "guncelle": ("istemci", "guncelle.py"),
    "kur": ("istemci", "kur.py"),
    "kisayol": ("istemci", "kisayol.py"),
    "tapu": ("tapu", "server.py"),
    "uyap": ("uyap", "server.py"),
}


def _gecerli(dizin):
    return os.path.isfile(os.path.join(dizin, "istemci", "arthurlegal_sunucu.py"))


def etkin_dizin():
    kok = os.path.join(KOK, "surumler")
    try:
        with open(os.path.join(KOK, "aktif.txt"), encoding="utf-8") as f:
            aktif = f.read().strip()
    except OSError:
        aktif = ""
    if aktif and _gecerli(os.path.join(kok, aktif)):
        return os.path.join(kok, aktif)
    adaylar = [a for a in (os.listdir(kok) if os.path.isdir(kok) else [])
               if re.fullmatch(r"\d+(\.\d+)*", a) and _gecerli(os.path.join(kok, a))]
    if not adaylar:
        sys.exit("ArthurLegal: kurulu sürüm bulunamadı; kurulum dosyasını yeniden çalıştırın.")
    return os.path.join(kok, max(adaylar, key=lambda s: tuple(int(x) for x in s.split("."))))


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in HEDEFLER:
        sys.exit("kullanım: al.py " + "|".join(HEDEFLER) + " [argümanlar]")
    hedef = sys.argv[1]
    if sys.stdout is None or sys.stderr is None:  # pythonw: konsol yok, çıktı günlüğe
        klasor = os.path.join(KOK, "veri", "gunluk")
        os.makedirs(klasor, exist_ok=True)
        dosya = open(os.path.join(klasor, hedef + "-cikti.log"), "a", encoding="utf-8", buffering=1)
        sys.stdout = sys.stdout or dosya
        sys.stderr = sys.stderr or dosya
    for akis in (sys.stdout, sys.stderr):  # Türkçe çıktı, konsol kod sayfası ne olursa olsun çökmemeli
        try:
            akis.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass
    alt, ad = HEDEFLER[hedef]
    dizin = os.path.join(etkin_dizin(), alt)
    sys.path.insert(0, dizin)
    sys.argv = [os.path.join(dizin, ad)] + sys.argv[2:]
    runpy.run_path(sys.argv[0], run_name="__main__")


if __name__ == "__main__":
    main()
