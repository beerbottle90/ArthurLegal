"""ArthurLegal simgesi: yumuşak köşeli lacivert kare, altın geometrik "A" (3.0.0; önceki pixel art'ın yerine).

    python varlik/simge.py            # simge-onizleme.png (512 px) yazar

Yalnız standart kütüphane: kurulum her derlemede görselleri yeniden üretir (yayin/derle.py) ve macOS paketi GitHub
Actions'ta aynı simgeden .icns çıkarır (yayin/derle_macos.py). Çizim vektördür; her boyut ayrı çizilir, büyütülmez.

Çizici tarama çizgisiyle çalışır: her piksel satırı ``ALT`` alt satıra bölünür, çokgen kenarlarının kesişimleri
sıfır olmayan sarım kuralıyla doldurulur, aralıkların uçları kesirli kapsamayla yumuşar. Şekiller birleşim olarak
çizilir (A'nın iki bacağı ve çizgisi üst üste biner, kapsama toplanmaz).

Şekil ve renkler masadaki armayla aynıdır (``arma_svg``): istemci/arayuz/ortak/tasarim/arma.svg'nin kaynağı
arthurlegal-app4all deposudur; bu modül aynı SVG'yi üretir, kopyası oraya elle konmaz.
"""
from __future__ import annotations

import math
import struct
import sys
import zlib
from pathlib import Path
from typing import List, Sequence, Tuple

Nokta = Tuple[float, float]
Renk = Tuple[int, int, int]

ALT = 4                                  # piksel başına alt satır (dikey yumuşatma)

# AL renkleri: canlı lacivert zemin (maviye kaymaz), parlak altın işaret (30.10.2026; önceki #223B63→#0B1524,
# #F6D98E→#D6A23A soluk kalıyordu).
ZEMIN_UST, ZEMIN_ALT = (0x18, 0x30, 0x64), (0x07, 0x12, 0x30)
ALTIN_UST, ALTIN_ALT = (0xFF, 0xE4, 0x8A), (0xF7, 0xBE, 0x2D)
KENAR_IZI = (0xFF, 0xFF, 0xFF)           # üst kenarda ince ışık


def _hex(r: Renk) -> str:
    return "#%02X%02X%02X" % r


# --------------------------------------------------------------------------- #
# Şekiller (birim kare, y aşağı)                                               #
# --------------------------------------------------------------------------- #

def squircle(pay: float = 0.0, n: float = 5.0, adim: int = 160) -> List[Nokta]:
    """Süperelips |x|^n + |y|^n = 1: macOS ve Windows 11 simgelerindeki sürekli eğrili kare."""
    yari = 0.5 - pay
    noktalar = []
    for i in range(adim):
        a = 2 * math.pi * i / adim
        c, s = math.cos(a), math.sin(a)
        x = math.copysign(abs(c) ** (2 / n), c)
        y = math.copysign(abs(s) ** (2 / n), s)
        noktalar.append((0.5 + yari * x, 0.5 + yari * y))
    return noktalar


def a_harfi(kalin: float = 0.125, ust: float = 0.235, alt: float = 0.775, sol: float = 0.225,
            cizgi: float = 0.575) -> List[List[Nokta]]:
    """Düz tepeli geometrik A: iki eğik bacak ve yatay çizgi (birleşim olarak çizilir)."""
    sag, orta = 1 - sol, 0.5
    sol_bacak = [(sol, alt), (sol + kalin, alt), (orta + kalin / 2, ust), (orta - kalin / 2, ust)]
    sag_bacak = [(sag - kalin, alt), (sag, alt), (orta + kalin / 2, ust), (orta - kalin / 2, ust)]
    yukseklik = kalin * 0.74
    cubuk = [(sol + 0.08, cizgi), (sag - 0.08, cizgi), (sag - 0.08, cizgi + yukseklik), (sol + 0.08, cizgi + yukseklik)]
    return [sol_bacak, sag_bacak, cubuk]


def _yonlu(cokgen: Sequence[Nokta]) -> List[Nokta]:
    """Saat yönünde (y aşağıyken pozitif alan): birleşimde bütün çokgenler aynı yönde olmalı."""
    alan = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(cokgen, list(cokgen[1:]) + [cokgen[0]]))
    return list(cokgen) if alan > 0 else list(reversed(cokgen))


# --------------------------------------------------------------------------- #
# Çizici                                                                       #
# --------------------------------------------------------------------------- #

def kapsama(cokgenler: Sequence[Sequence[Nokta]], en: int, boy: int) -> List[float]:
    """Çokgenlerin birleşiminin piksel başına kapsaması (0..1), sıfır olmayan sarım kuralı."""
    kenarlar = []
    for c in cokgenler:
        c = _yonlu(c)
        for (x1, y1), (x2, y2) in zip(c, c[1:] + c[:1]):
            if y1 != y2:
                kenarlar.append((x1 * en, y1 * boy, x2 * en, y2 * boy))
    sonuc = [0.0] * (en * boy)
    pay = 1.0 / ALT
    for py in range(boy):
        satir = sonuc[py * en:(py + 1) * en]
        for alt in range(ALT):
            y = py + (alt + 0.5) * pay
            kesisim = []
            for x1, y1, x2, y2 in kenarlar:
                if (y1 <= y < y2) or (y2 <= y < y1):
                    x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    kesisim.append((x, 1 if y2 > y1 else -1))
            if not kesisim:
                continue
            kesisim.sort()
            sarim = 0
            bas = 0.0
            for x, yon in kesisim:
                onceki = sarim
                sarim += yon
                if onceki == 0 and sarim != 0:
                    bas = x
                elif onceki != 0 and sarim == 0:
                    _aralik(satir, bas, x, pay, en)
        sonuc[py * en:(py + 1) * en] = satir
    return sonuc


def _aralik(satir: List[float], x0: float, x1: float, agirlik: float, en: int) -> None:
    x0, x1 = max(0.0, x0), min(float(en), x1)
    if x1 <= x0:
        return
    i0, i1 = int(x0), int(x1)
    if i0 == i1:
        satir[i0] += (x1 - x0) * agirlik
        return
    satir[i0] += (i0 + 1 - x0) * agirlik
    for i in range(i0 + 1, i1):
        satir[i] += agirlik
    if i1 < en:
        satir[i1] += (x1 - i1) * agirlik


def _karistir(a: Renk, b: Renk, t: float) -> Renk:
    t = min(1.0, max(0.0, t))
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))  # type: ignore[return-value]


class Tuval:
    """RGBA tuval (ön çarpımsız); katmanlar üst üste 'kaynak üstte' kuralıyla eklenir."""

    def __init__(self, en: int, boy: int) -> None:
        self.en, self.boy = en, boy
        self.p = [[0.0, 0.0, 0.0, 0.0] for _ in range(en * boy)]

    def boya(self, cokgenler: Sequence[Sequence[Nokta]], renk_ust: Renk, renk_alt: Renk,
             y_ust: float = 0.0, y_alt: float = 1.0, saydamlik: float = 1.0) -> None:
        """Çokgen birleşimini dikey degradeyle (y_ust → y_alt, birim kare) boyar."""
        k = kapsama(cokgenler, self.en, self.boy)
        for py in range(self.boy):
            t = ((py + 0.5) / self.boy - y_ust) / max(1e-9, y_alt - y_ust)
            r, g, b = _karistir(renk_ust, renk_alt, t)
            for px in range(self.en):
                a = min(1.0, k[py * self.en + px]) * saydamlik
                if a <= 0:
                    continue
                h = self.p[py * self.en + px]
                kalan = h[3] * (1 - a)
                yeni = a + kalan
                h[0] = (r * a + h[0] * kalan) / yeni
                h[1] = (g * a + h[1] * kalan) / yeni
                h[2] = (b * a + h[2] * kalan) / yeni
                h[3] = yeni

    def rgba(self) -> bytes:
        cikti = bytearray()
        for py in range(self.boy):
            cikti.append(0)                                   # PNG satır süzgeci: yok
            for px in range(self.en):
                r, g, b, a = self.p[py * self.en + px]
                cikti += bytes((int(round(r)), int(round(g)), int(round(b)), int(round(a * 255))))
        return bytes(cikti)

    def png(self) -> bytes:
        def parca(tur: bytes, veri: bytes) -> bytes:
            return struct.pack(">I", len(veri)) + tur + veri + struct.pack(">I", zlib.crc32(tur + veri) & 0xFFFFFFFF)
        return (b"\x89PNG\r\n\x1a\n" + parca(b"IHDR", struct.pack(">IIBBBBB", self.en, self.boy, 8, 6, 0, 0, 0))
                + parca(b"IDAT", zlib.compress(self.rgba(), 9)) + parca(b"IEND", b""))


# --------------------------------------------------------------------------- #
# Simge, sihirbaz görselleri, arma                                             #
# --------------------------------------------------------------------------- #

def simge_tuvali(boyut: int) -> Tuval:
    """Simge, ``boyut`` piksel. Küçük boyutlarda kenar payı yok ve harf kalın: 16 px'te de okunur."""
    kucuk = boyut <= 32
    pay = 0.0 if kucuk else 0.035
    t = Tuval(boyut, boyut)
    govde = squircle(pay)
    t.boya([govde], ZEMIN_UST, ZEMIN_ALT, pay, 1 - pay)
    if not kucuk:
        # Üst kenarda ince ışık: yalnız gövdenin üst bandı, çok hafif.
        t.boya([[(x, min(y, 0.5)) for x, y in govde]], KENAR_IZI, ZEMIN_UST, pay, 0.5, saydamlik=0.07)
    harf = a_harfi(kalin=0.17, ust=0.19, alt=0.82, sol=0.17) if kucuk else a_harfi()
    t.boya(harf, ALTIN_UST, ALTIN_ALT, 0.2, 0.8)
    return t


def simge_png(boyut: int) -> bytes:
    return simge_tuvali(boyut).png()


def ico_yaz(yol: Path, boyutlar: Sequence[int] = (16, 24, 32, 48, 64, 128, 256)) -> Path:
    """PNG gövdeli ICO (Windows Vista'dan beri her boyutta desteklenir)."""
    goruntuler = [simge_png(b) for b in boyutlar]
    bas = struct.pack("<HHH", 0, 1, len(boyutlar))
    sira = 6 + 16 * len(boyutlar)
    dizin = b""
    for b, veri in zip(boyutlar, goruntuler):
        dizin += struct.pack("<BBBBHHII", b % 256, b % 256, 0, 0, 1, 32, len(veri), sira)
        sira += len(veri)
    Path(yol).write_bytes(bas + dizin + b"".join(goruntuler))
    return Path(yol)


def sihirbaz_tuvali(en: int = 328, boy: int = 624) -> Tuval:
    """Kurulum sihirbazının sol görseli (Inno 164x312'nin iki katı): lacivert degrade, yumuşak iki daire, ortada
    simge. Yazı yok: ürün adı sihirbazın kendi metninde."""
    t = Tuval(en, boy)
    t.boya([[(0, 0), (1, 0), (1, 1), (0, 1)]], (0x12, 0x2B, 0x58), (0x06, 0x10, 0x2A))
    oran = boy / en

    def daire_birim(cx: float, cy: float, r: float) -> List[Nokta]:
        # r genişliğe göre; dikey ölçek tuvalin oranıyla düzeltilir (daire yuvarlak kalsın).
        return [(cx + r * math.cos(2 * math.pi * i / 96), cy + r / oran * math.sin(2 * math.pi * i / 96))
                for i in range(96)]

    t.boya([daire_birim(0.95, 0.80, 0.62)], (0x1F, 0x44, 0x7F), (0x0D, 0x22, 0x41), 0.5, 1.0, saydamlik=0.35)
    t.boya([daire_birim(0.05, 0.10, 0.45)], (0x21, 0x4A, 0x89), (0x12, 0x2B, 0x58), 0.0, 0.3, saydamlik=0.25)
    # Simge ortada, üstten üçte birde; ince altın çizgi altında.
    boyut = 0.56
    x0, y0 = (1 - boyut) / 2, 0.30 - boyut / 2 / oran
    govde = [(x0 + boyut * x, y0 + boyut / oran * y) for x, y in squircle(0.0)]
    t.boya([govde], ZEMIN_UST, ZEMIN_ALT, y0, y0 + boyut / oran)
    harf = [[(x0 + boyut * x, y0 + boyut / oran * y) for x, y in c] for c in a_harfi()]
    t.boya(harf, ALTIN_UST, ALTIN_ALT, y0 + 0.2 * boyut / oran, y0 + 0.8 * boyut / oran)
    cy = 0.30 + boyut / 2 / oran + 0.06
    t.boya([[(0.36, cy), (0.64, cy), (0.64, cy + 0.004), (0.36, cy + 0.004)]], ALTIN_UST, ALTIN_ALT,
           saydamlik=0.9)
    return t


def arma_svg() -> str:
    """Masadaki arma (istemci/arayuz/ortak/tasarim/arma.svg): simgeyle aynı şekil ve renkler, 100 birimlik kutu."""
    def yol(c: Sequence[Nokta]) -> str:
        return "M" + "L".join("%.2f %.2f" % (x * 100, y * 100) for x, y in _yonlu(c)) + "Z"
    govde = yol(squircle(0.0, adim=64))
    harf = "".join(yol(c) for c in a_harfi())
    return (
        '<svg class="arma" viewBox="0 0 100 100" role="img" aria-label="ArthurLegal arması">'
        '<defs><linearGradient id="alArmaZ" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{_hex(ZEMIN_UST)}"/><stop offset="1" stop-color="{_hex(ZEMIN_ALT)}"/>'
        '</linearGradient><linearGradient id="alArmaA" x1="0" y1="0.2" x2="0" y2="0.8">'
        f'<stop offset="0" stop-color="{_hex(ALTIN_UST)}"/><stop offset="1" stop-color="{_hex(ALTIN_ALT)}"/>'
        '</linearGradient></defs>'
        f'<path fill="url(#alArmaZ)" d="{govde}"/><path fill="url(#alArmaA)" d="{harf}"/></svg>'
    )


if __name__ == "__main__":
    hedef = Path(__file__).resolve().parent / "simge-onizleme.png"
    hedef.write_bytes(simge_png(int(sys.argv[1]) if len(sys.argv) > 1 else 512))
    print(hedef)
