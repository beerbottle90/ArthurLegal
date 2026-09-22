"""ArthurLegal pixel art: küçük bir ızgaraya çizer, büyütür, PNG ve ICO yazar.

Yalnız standart kütüphane (zlib, struct). Marka renkleri: lacivert #0D1826, altın #E0B24C /
#F4D58D, krem; açık kaynak temalı vurgular için yeşil, kırmızı, mor, mavi, turuncu.
Kullanım: varlik/gorseller.py bu modülle kurulum simgesini, sihirbaz görsellerini ve afişleri üretir.
"""
from __future__ import annotations

import struct
import zlib

PALET = {
    ".": None,                       # saydam
    "K": (8, 14, 24), "N": (13, 24, 38), "n": (22, 36, 54), "m": (34, 54, 79), "l": (44, 66, 96),
    "d": (147, 163, 184), "s": (169, 182, 204), "t": (107, 122, 153),
    "W": (237, 239, 243), "c": (245, 239, 224), "C": (217, 207, 184),
    "G": (224, 178, 76), "H": (244, 213, 141), "g": (166, 124, 46), "Y": (255, 224, 102),
    "E": (116, 196, 160), "V": (63, 174, 106), "v": (43, 122, 75),
    "R": (226, 118, 108), "r": (200, 69, 59),
    "O": (242, 155, 75), "P": (123, 92, 196), "p": (74, 58, 120),
    "M": (180, 90, 154), "S": (94, 200, 229), "B": (59, 125, 216), "b": (139, 90, 60),
}

GOKKUSAGI = ["r", "O", "Y", "V", "S", "B", "P", "M"]  # açık kaynak şeridi

FONT = {
    "A": [".XXX.", "X...X", "X...X", "XXXXX", "X...X", "X...X", "X...X"],
    "B": ["XXXX.", "X...X", "X...X", "XXXX.", "X...X", "X...X", "XXXX."],
    "C": [".XXX.", "X...X", "X....", "X....", "X....", "X...X", ".XXX."],
    "D": ["XXXX.", "X...X", "X...X", "X...X", "X...X", "X...X", "XXXX."],
    "E": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "XXXXX"],
    "F": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "X...."],
    "G": [".XXX.", "X...X", "X....", "X.XXX", "X...X", "X...X", ".XXXX"],
    "H": ["X...X", "X...X", "X...X", "XXXXX", "X...X", "X...X", "X...X"],
    "I": [".XXX.", "..X..", "..X..", "..X..", "..X..", "..X..", ".XXX."],
    "J": ["..XXX", "...X.", "...X.", "...X.", "X..X.", "X..X.", ".XX.."],
    "K": ["X...X", "X..X.", "X.X..", "XX...", "X.X..", "X..X.", "X...X"],
    "L": ["X....", "X....", "X....", "X....", "X....", "X....", "XXXXX"],
    "M": ["X...X", "XX.XX", "X.X.X", "X.X.X", "X...X", "X...X", "X...X"],
    "N": ["X...X", "XX..X", "X.X.X", "X.X.X", "X..XX", "X...X", "X...X"],
    "O": [".XXX.", "X...X", "X...X", "X...X", "X...X", "X...X", ".XXX."],
    "P": ["XXXX.", "X...X", "X...X", "XXXX.", "X....", "X....", "X...."],
    "Q": [".XXX.", "X...X", "X...X", "X...X", "X.X.X", "X..X.", ".XX.X"],
    "R": ["XXXX.", "X...X", "X...X", "XXXX.", "X.X..", "X..X.", "X...X"],
    "S": [".XXXX", "X....", "X....", ".XXX.", "....X", "....X", "XXXX."],
    "T": ["XXXXX", "..X..", "..X..", "..X..", "..X..", "..X..", "..X.."],
    "U": ["X...X", "X...X", "X...X", "X...X", "X...X", "X...X", ".XXX."],
    "V": ["X...X", "X...X", "X...X", "X...X", "X...X", ".X.X.", "..X.."],
    "W": ["X...X", "X...X", "X...X", "X.X.X", "X.X.X", "XX.XX", "X...X"],
    "X": ["X...X", "X...X", ".X.X.", "..X..", ".X.X.", "X...X", "X...X"],
    "Y": ["X...X", "X...X", ".X.X.", "..X..", "..X..", "..X..", "..X.."],
    "Z": ["XXXXX", "....X", "...X.", "..X..", ".X...", "X....", "XXXXX"],
    "0": [".XXX.", "X...X", "X..XX", "X.X.X", "XX..X", "X...X", ".XXX."],
    "1": ["..X..", ".XX..", "..X..", "..X..", "..X..", "..X..", ".XXX."],
    "2": [".XXX.", "X...X", "....X", "...X.", "..X..", ".X...", "XXXXX"],
    "3": ["XXXXX", "...X.", "..X..", "...X.", "....X", "X...X", ".XXX."],
    "4": ["...X.", "..XX.", ".X.X.", "X..X.", "XXXXX", "...X.", "...X."],
    "5": ["XXXXX", "X....", "XXXX.", "....X", "....X", "X...X", ".XXX."],
    "6": ["..XX.", ".X...", "X....", "XXXX.", "X...X", "X...X", ".XXX."],
    "7": ["XXXXX", "....X", "...X.", "..X..", ".X...", ".X...", ".X..."],
    "8": [".XXX.", "X...X", "X...X", ".XXX.", "X...X", "X...X", ".XXX."],
    "9": [".XXX.", "X...X", "X...X", ".XXXX", "....X", "...X.", ".XX.."],
    ".": [".....", ".....", ".....", ".....", ".....", ".XX..", ".XX.."],
    "-": [".....", ".....", ".....", "XXXXX", ".....", ".....", "....."],
    "+": [".....", "..X..", "..X..", "XXXXX", "..X..", "..X..", "....."],
    "/": ["....X", "....X", "...X.", "..X..", ".X...", "X....", "X...."],
    ":": [".....", ".XX..", ".XX..", ".....", ".XX..", ".XX..", "....."],
    "!": ["..X..", "..X..", "..X..", "..X..", "..X..", ".....", "..X.."],
}


class Tuval:
    """Izgara tuval. Renkler PALET anahtarı ya da (r, g, b) demeti; None saydam."""

    def __init__(self, en: int, boy: int, zemin=None):
        self.en, self.boy = en, boy
        self.p = [[self._renk(zemin) for _ in range(en)] for _ in range(boy)]

    @staticmethod
    def _renk(c):
        return PALET[c] if isinstance(c, str) else c

    def px(self, x, y, c):
        if 0 <= x < self.en and 0 <= y < self.boy:
            renk = self._renk(c)
            if renk is not None or c == ".":
                self.p[y][x] = renk

    def rect(self, x0, y0, x1, y1, c):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.px(x, y, c)

    def sprite(self, x0, y0, satirlar):
        for j, satir in enumerate(satirlar):
            for i, ch in enumerate(satir):
                if ch != ".":
                    self.px(x0 + i, y0 + j, ch)

    def yazi(self, x0, y0, metin, c, olcek=1, aralik=1):
        x = x0
        for ch in metin.upper():
            if ch == " ":
                x += (3 + aralik) * olcek
                continue
            for j, satir in enumerate(FONT[ch]):
                for i, v in enumerate(satir):
                    if v == "X":
                        self.rect(x + i * olcek, y0 + j * olcek, x + (i + 1) * olcek - 1, y0 + (j + 1) * olcek - 1, c)
            x += (5 + aralik) * olcek
        return x

    @staticmethod
    def yazi_eni(metin, olcek=1, aralik=1):
        en = 0
        for ch in metin.upper():
            en += (3 + aralik if ch == " " else 5 + aralik) * olcek
        return en - aralik * olcek

    def buyut(self, olcek):
        """(genişlik, yükseklik, RGBA baytları) — satır satır, üstten alta."""
        satirlar = []
        for y in range(self.boy):
            satir = bytearray()
            for x in range(self.en):
                renk = self.p[y][x]
                satir += (bytes(renk) + b"\xff") * olcek if renk else b"\x00\x00\x00\x00" * olcek
            satirlar.append(bytes(satir) * olcek)
        return self.en * olcek, self.boy * olcek, b"".join(satirlar)

    def png_yaz(self, yol, olcek=1):
        en, boy, veri = self.buyut(olcek)
        ham = b"".join(b"\x00" + veri[i * en * 4:(i + 1) * en * 4] for i in range(boy))

        def parca(etiket, govde):
            return struct.pack(">I", len(govde)) + etiket + govde + struct.pack(">I", zlib.crc32(etiket + govde) & 0xffffffff)

        with open(yol, "wb") as f:
            f.write(b"\x89PNG\r\n\x1a\n"
                    + parca(b"IHDR", struct.pack(">IIBBBBB", en, boy, 8, 6, 0, 0, 0))
                    + parca(b"IDAT", zlib.compress(ham, 9)) + parca(b"IEND", b""))
        return yol

    def ico_yaz(self, yol, boyutlar=(16, 32, 48, 64, 128, 256)):
        """Klasik BMP girdili .ico (32 bit BGRA + AND maskesi): her boyutta Windows okur."""
        girdiler, govdeler = [], []
        for boyut in boyutlar:
            olcek = max(1, boyut // self.en)
            en, boy, veri = self.buyut(olcek)
            if en != boyut:  # tam katı değilse en yakın kat kullanılır
                boyut = en
            satir_bayt = boyut * 4
            xor = bytearray()
            for y in range(boy - 1, -1, -1):  # BMP alttan üste
                for x in range(boyut):
                    r, g, b, a = veri[(y * en + x) * 4:(y * en + x) * 4 + 4]
                    xor += bytes((b, g, r, a))
            maske_satir = ((boyut + 31) // 32) * 4
            ve_maske = bytearray()
            for y in range(boy - 1, -1, -1):
                bitler = bytearray(maske_satir)
                for x in range(boyut):
                    if veri[(y * en + x) * 4 + 3] == 0:
                        bitler[x // 8] |= 0x80 >> (x % 8)
                ve_maske += bitler
            basi = struct.pack("<IiiHHIIiiII", 40, boyut, boy * 2, 1, 32, 0, len(xor) + len(ve_maske), 0, 0, 0, 0)
            govdeler.append(basi + bytes(xor) + bytes(ve_maske))
            girdiler.append((boyut, boy))
        ofset = 6 + 16 * len(govdeler)
        bas = struct.pack("<HHH", 0, 1, len(govdeler))
        dizin = b""
        for (boyut, boy), govde in zip(girdiler, govdeler):
            dizin += struct.pack("<BBBBHHII", boyut % 256, boy % 256, 0, 0, 1, 32, len(govde), ofset)
            ofset += len(govde)
        with open(yol, "wb") as f:
            f.write(bas + dizin + b"".join(govdeler))
        return yol
