"""ArthurLegal kurulum görsellerini üretir (pixel art, stdlib).

    python varlik/gorseller.py

Üretilenler (hepsi bu klasöre):
    arthurlegal.ico        kurulum ve kısayol simgesi (16/32/48/64/128/256)
    banner.png             README afişi
    rehber-banner.png      başlangıç rehberi başlığı
    sihirbaz.png           Inno Setup sihirbaz görseli (164x312)
    sihirbaz-kucuk.png     Inno Setup küçük görsel (55x55)

Tema: açık kaynak, özgürlük, hukuk yapay zekâsı. Lacivert zemin, altın "A", gökkuşağı şeridi.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pixelart import GOKKUSAGI, Tuval  # noqa: E402

BURASI = Path(__file__).resolve().parent

TERAZI = [
    "......G......",
    "......G......",
    "GGGGGGGGGGGGG",
    "G.....G.....G",
    "G.....G.....G",
    "HHH...G...HHH",
    ".H....G....H.",
    "......G......",
    "......G......",
    "......G......",
    "...GGGGGGG...",
    "..GGGGGGGGG..",
]

KILIT = [  # açık asma kilit: özgürlük
    "..VVVV...",
    ".V....V..",
    ".V....V..",
    ".V.......",
    "VVVVVVVV.",
    "VVVVVVVV.",
    "VVV..VVV.",
    "VVV..VVV.",
    "VVVVVVVV.",
    "VVVVVVVV.",
]

TOKMAK = [
    "...bbbb....",
    "..bbbbbb...",
    "...bbbb....",
    "....bb.....",
    ".....bb....",
    "......bb...",
    ".......bb..",
    "........b..",
]

KOD = [  # </> açık kaynak işareti
    "..S...S..",
    ".S.....S.",
    "S...Y...S",
    "S..Y....S",
    "S.Y.....S",
    ".S.....S.",
    "..S...S..",
]


def gokkusagi(t: Tuval, y0: int, y1: int, x0: int = 0, x1: int | None = None, genislik: int = 0) -> None:
    x1 = t.en - 1 if x1 is None else x1
    genislik = genislik or max(1, (x1 - x0 + 1) // len(GOKKUSAGI))
    for i, x in enumerate(range(x0, x1 + 1, genislik)):
        t.rect(x, y0, min(x + genislik - 1, x1), y1, GOKKUSAGI[i % len(GOKKUSAGI)])


def zemin(t: Tuval, bantlar=(("N", 0.0), ("n", 0.45), ("m", 0.78))) -> None:
    for renk, oran in bantlar:
        t.rect(0, int(t.boy * oran), t.en - 1, t.boy - 1, renk)


def a_isareti(t: Tuval, x: int, y: int, olcek: int) -> None:
    """Marka işareti: altın A, tepesinde açık altın vurgu."""
    t.yazi(x, y, "A", "G", olcek)
    t.rect(x + olcek, y, x + 4 * olcek - 1, y + max(1, olcek // 3) - 1, "H")


def simge() -> Path:
    t = Tuval(16, 16, "N")
    t.rect(0, 0, 15, 0, "n")
    a_isareti(t, 3, 0, 2)
    gokkusagi(t, 14, 15, 0, 15, 2)
    return Path(t.ico_yaz(BURASI / "arthurlegal.ico"))


def afis() -> Path:
    t = Tuval(200, 64, "N")
    zemin(t, (("N", 0.0), ("n", 0.62), ("m", 0.88)))
    a_isareti(t, 8, 8, 6)
    t.yazi(48, 10, "ARTHUR", "G", 3)
    t.yazi(48, 32, "LEGAL", "c", 3)
    t.yazi(10, 54, "ACIK KAYNAK HUKUK YAPAY ZEKASI", "E", 1)
    t.sprite(162, 6, TERAZI)
    t.sprite(181, 8, KILIT)
    t.sprite(163, 24, TOKMAK)
    t.sprite(180, 28, KOD)
    gokkusagi(t, 62, 63)
    return Path(t.png_yaz(BURASI / "banner.png", 5))


def rehber_afisi() -> Path:
    t = Tuval(200, 30, "N")
    zemin(t, (("N", 0.0), ("n", 0.7)))
    a_isareti(t, 6, 3, 3)
    t.yazi(32, 5, "ARTHURLEGAL", "G", 2)
    t.yazi(32, 21, "ACIK KAYNAK HUKUK YZ", "E", 1)
    t.sprite(166, 6, TERAZI)
    t.sprite(185, 8, KILIT)
    gokkusagi(t, 28, 29)
    return Path(t.png_yaz(BURASI / "rehber-banner.png", 4))


def sihirbaz() -> Path:
    t = Tuval(41, 78, "N")
    zemin(t, (("N", 0.0), ("n", 0.5), ("m", 0.82)))
    a_isareti(t, 9, 6, 4)
    t.yazi(3, 38, "ARTHUR", "G", 1)
    t.yazi(3, 46, "LEGAL", "c", 1)
    t.sprite(23, 54, TERAZI)
    t.sprite(4, 56, KILIT)
    t.sprite(16, 67, KOD)
    t.sprite(28, 66, TOKMAK)
    gokkusagi(t, 74, 77, 0, 40, 5)
    return Path(t.png_yaz(BURASI / "sihirbaz.png", 4))


def sihirbaz_kucuk() -> Path:
    t = Tuval(11, 11, "N")
    a_isareti(t, 3, 1, 1)
    gokkusagi(t, 9, 10, 0, 10, 2)
    return Path(t.png_yaz(BURASI / "sihirbaz-kucuk.png", 5))


def main() -> int:
    for uret in (simge, afis, rehber_afisi, sihirbaz, sihirbaz_kucuk):
        yol = uret()
        print(f"  {yol.name} ({yol.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
