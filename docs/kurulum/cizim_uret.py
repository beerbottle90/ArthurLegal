"""README'nin indirme bölümündeki çizimleri (SVG) üretir: Türkçe ve İngilizce.

    python docs/kurulum/cizim_uret.py

Çizimler ekran görüntüsü değildir: Windows ve Edge pencerelerinin sade bir taslağıdır, tıklanacak
yer kırmızı çerçeve ve numarayla gösterilir. Üzerindeki yazılar Windows'un ve Edge'in o dildeki birebir
metinleridir; Microsoft bir metni değiştirirse yalnız aşağıdaki METIN sözlüğü düzeltilip bu betik
yeniden çalıştırılır. SVG dosyaları elle düzenlenmez.

Modül ekranı çizimlerinin (moduller.svg, modules-en.svg, moduller-courthouse.svg) yazıları ArthurLegal kurulum
betiğinden okunur (ArthurLegal-setup/kurulum/ArthurLegal.iss, Modul* iletileri).

Mac çizimleri (mac-*.svg): macOS'un ilk açılış uyarısı, Sistem Ayarları'ndaki Yine de Aç ve kurulum sihirbazının
Yükleme Türü ekranı. Üzerindeki macOS yazıları macOS'un kendi Türkçe ve İngilizce metinleridir (MAC_METIN; kaynağı
mac_metinleri.py); modül adları ve açıklamaları yine ArthurLegal.iss'ten, Mac'e özgü Arthur Mask koşuluyla
(ArthurLegal-setup/yayin/derle_macos.py, MASK_KOSULU).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

BURASI = Path(__file__).resolve().parent
DOSYA = "ArthurLegal-Kurulum.exe"

# Ekranda görünen metinler ve kaynakları (Ekim 2026):
# - SmartScreen: çevrimiçi pencerenin metni Microsoft'un sunucusundan gelir, Windows'ta yerel kaydı yoktur.
#   Türkçe başlık birbirinden bağımsız çok sayıda Türkçe ekran alıntısından ("Windows kişisel bilgisayarınızı
#   korudu"); Türkçe gövde metni kullanıcı alıntılarından (2021), en az kesin olan budur. "Ek bilgi",
#   "Yine de çalıştır", "Çalıştırma", "Uygulama:", "Yayımcı:" yerel smartscreen.exe.mui şablonuyla da uyumlu.
# - Edge: Edge 153'ün tr.pak ve en-US.pak dosyaları. Bu sürümde onay penceresinde "Daha fazla göster" yoktur;
#   "Yine de sakla" (Keep anyway), mavi "Sil" (Delete) düğmesinin yanındaki okla açılır. "Yayımcı: Bilinmiyor"
#   imzasız dosya için çıkarımdır.
METIN = {
    "tr": {
        "ss_baslik": "Windows kişisel bilgisayarınızı korudu",
        "ss_govde": [
            "Microsoft Defender SmartScreen tanınmayan bir uygulamanın",
            "başlamasını engelledi. Bu uygulamayı çalıştırmak",
            "bilgisayarınızın güvenliğini tehlikeye sokabilir.",
        ],
        "ss_ek_bilgi": "Ek bilgi",
        "ss_uygulama": "Uygulama:",
        "ss_yayimci": "Yayımcı:",
        "ss_bilinmeyen": "Bilinmeyen yayımcı",
        "ss_calistir": "Yine de çalıştır",
        "ss_calistirma": "Çalıştırma",
        "edge_panel": "İndirmeler",
        "edge_uyari": [
            f"{DOSYA} yaygın olarak indirilen",
            f"bir dosya değil. Açmadan önce {DOSYA}",
            "dosyasının güvenilir olduğundan emin olun.",
        ],
        # None: menüdeki ayırıcı çizgi
        "edge_menu": ["Sil", "Sakla", None, "Bu dosyayı güvenli olarak bildir", "Daha fazla bilgi edinin", None,
                      "İndirme bağlantısını kopyala"],
        "edge_sakla": "Sakla",
        "edge_d_baslik": [f"Açmadan önce {DOSYA} dosyasının", "güvenilir olduğundan emin olun"],
        "edge_d_govde": [
            "Dosya yaygın olarak indirilmediğinden Microsoft Defender SmartScreen",
            "bu dosyanın güvenli olup olmadığı doğrulayamadı. Açmadan önce",
            "indirdiğiniz dosyanın veya kaynağının güvenli olduğundan emin olun.",
        ],
        "edge_d_ad": f"Ad: {DOSYA}",
        "edge_d_yayimci": "Yayımcı: Bilinmiyor",
        "edge_d_bildir": "Bu uygulamayı güvenli olarak bildir",
        "edge_d_bilgi": "Daha fazla bilgi edinin",
        "edge_d_yine": "Yine de sakla",
        "edge_d_sil": "Sil",
        "edge_d_iptal": "İptal",
        # Çizimin kendi yazıları: alt yazı ve ekran okuyucu başlığı
        "dipnot_ss": "Çizim · Windows SmartScreen uyarısı (örnek görünüm)",
        "dipnot_edge1": "Çizim · Microsoft Edge indirme uyarısı (örnek görünüm)",
        "dipnot_edge2": "Çizim · Microsoft Edge onay penceresi (örnek görünüm)",
        "baslik_ss1": "Örnek: Windows kişisel bilgisayarınızı korudu penceresinde önce Ek bilgi yazısına tıklayın",
        "baslik_ss2": "Örnek: Ek bilgi'den sonra Yine de çalıştır düğmesine tıklayın",
        "baslik_edge1": "Örnek: Edge'de dosyanın satırındaki üç noktaya, sonra Sakla'ya tıklayın",
        "baslik_edge2": "Örnek: mavi Sil düğmesinin yanındaki oka, sonra Yine de sakla'ya tıklayın",
    },
    "en": {
        "ss_baslik": "Windows protected your PC",
        "ss_govde": [
            "Microsoft Defender SmartScreen prevented an unrecognized app",
            "from starting. Running this app might put your PC at risk.",
        ],
        "ss_ek_bilgi": "More info",
        "ss_uygulama": "App:",
        "ss_yayimci": "Publisher:",
        "ss_bilinmeyen": "Unknown publisher",
        "ss_calistir": "Run anyway",
        "ss_calistirma": "Don't run",
        "edge_panel": "Downloads",
        "edge_uyari": [
            f"{DOSYA} isn't commonly downloaded.",
            f"Make sure you trust {DOSYA}",
            "before you open it.",
        ],
        "edge_menu": ["Delete", "Keep", None, "Report this file as safe", "Learn more", None, "Copy download link"],
        "edge_sakla": "Keep",
        "edge_d_baslik": [f"Make sure you trust {DOSYA}", "before you open it"],
        "edge_d_govde": [
            "Microsoft Defender SmartScreen couldn't verify if this file is safe",
            "because it isn't commonly downloaded. Make sure you trust the file",
            "you're downloading or its source before you open it.",
        ],
        "edge_d_ad": f"Name: {DOSYA}",
        "edge_d_yayimci": "Publisher: Unknown",
        "edge_d_bildir": "Report this app as safe",
        "edge_d_bilgi": "Learn more",
        "edge_d_yine": "Keep anyway",
        "edge_d_sil": "Delete",
        "edge_d_iptal": "Cancel",
        "dipnot_ss": "Drawing · Windows SmartScreen warning (example)",
        "dipnot_edge1": "Drawing · Microsoft Edge download warning (example)",
        "dipnot_edge2": "Drawing · Microsoft Edge confirmation window (example)",
        "baslik_ss1": "Example: in the Windows protected your PC window, first click More info",
        "baslik_ss2": "Example: after More info, click the Run anyway button",
        "baslik_edge1": "Example: in Edge, click the three dots on the file's row, then Keep",
        "baslik_edge2": "Example: click the arrow next to the blue Delete button, then Keep anyway",
    },
}

# Dosya adları: Türkçe çizimler eski adlarını korur (README ve dış bağlantılar).
DOSYALAR = {
    "tr": {"edge1": "edge-1-sakla.svg", "edge2": "edge-2-yine-de-sakla.svg",
           "ss1": "smartscreen-1-ek-bilgi.svg", "ss2": "smartscreen-2-yine-de-calistir.svg"},
    "en": {"edge1": "edge-1-keep-en.svg", "edge2": "edge-2-keep-anyway-en.svg",
           "ss1": "smartscreen-1-more-info-en.svg", "ss2": "smartscreen-2-run-anyway-en.svg"},
}

YAZI = "'Segoe UI', 'Segoe UI Variable', 'Helvetica Neue', Arial, sans-serif"
KIRMIZI = "#e5243b"
LACIVERT = "#14233c"
ALTIN = "#b08d3c"
SS_MAVI = "#1f5fae"


def t(x, y, s, boyut=14, renk="#ffffff", agirlik=400, cizgi=False, hiza="start") -> str:
    alt = ' text-decoration="underline"' if cizgi else ""
    return (f'<text x="{x}" y="{y}" font-size="{boyut}" fill="{renk}" font-weight="{agirlik}" '
            f'text-anchor="{hiza}"{alt}>{escape(s)}</text>')


def satirlar(x, y, liste, boyut, renk, aralik, agirlik=400) -> str:
    return "".join(t(x, y + i * aralik, s, boyut, renk, agirlik) for i, s in enumerate(liste))


def isaret(x, y, g, h, no, rozet="sol") -> str:
    """Tıklanacak yerin kırmızı çerçevesi ve numara rozeti (solda, sağda ya da üstte)."""
    rx = {"sol": x - 14, "sag": x + g + 14, "ust": x + g / 2}[rozet]
    ry = y - 14 if rozet == "ust" else y + h / 2
    return (f'<rect x="{x}" y="{y}" width="{g}" height="{h}" rx="7" fill="none" stroke="{KIRMIZI}" stroke-width="3"/>'
            f'<circle cx="{rx}" cy="{ry}" r="13" fill="{KIRMIZI}"/>'
            + t(rx, ry + 5, str(no), 15, "#ffffff", 700, hiza="middle"))


def svg(gen, yuk, govde, baslik, yazi=YAZI) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{gen}" height="{yuk}" viewBox="0 0 {gen} {yuk}" '
            f'role="img" aria-label="{escape(baslik, {chr(34): "&quot;"})}">'
            f'<title>{escape(baslik)}</title><g font-family="{yazi}">{govde}</g></svg>\n')


def dipnot(gen, yuk, s) -> str:
    return t(gen / 2, yuk - 8, s, 12, "#8b949e", 400, hiza="middle")


def dugme(baslik: str, alt: str, aciklama: str) -> str:
    """İki dilli indirme düğmesi: README'nin en üstünde, her iki dildeki okura (Windows ve Mac için birer tane)."""
    gen, yuk = 760, 116
    ok = (f'<circle cx="66" cy="58" r="34" fill="{ALTIN}"/>'
          '<path d="M66 36 v32 M52 56 l14 14 l14 -14" stroke="#14233c" stroke-width="6" fill="none" '
          'stroke-linecap="round" stroke-linejoin="round"/><path d="M48 78 h36" stroke="#14233c" stroke-width="6" '
          'stroke-linecap="round"/>')
    govde = (f'<rect x="2" y="2" width="{gen - 4}" height="{yuk - 4}" rx="18" fill="{LACIVERT}" stroke="{ALTIN}" '
             f'stroke-width="3"/>{ok}'
             + t(120, 54, baslik, 28, "#ffffff", 700)
             + t(121, 84, alt, 16, "#e6d6a8", 400))
    return svg(gen, yuk, govde, aciklama)


def smartscreen(m: dict, adim: int) -> str:
    gen, yuk = 600, 352
    x0, y0, g, h = 10, 10, 580, 316
    govde = (f'<rect x="{x0 + 3}" y="{y0 + 4}" width="{g}" height="{h}" fill="#000000" opacity="0.18"/>'
             f'<rect x="{x0}" y="{y0}" width="{g}" height="{h}" fill="{SS_MAVI}" stroke="#16477f"/>'
             + t(x0 + g - 34, y0 + 26, "✕", 15, "#ffffff", 400)
             + t(x0 + 26, y0 + 66, m["ss_baslik"], 25, "#ffffff", 600)
             + satirlar(x0 + 26, y0 + 102, m["ss_govde"], 14.5, "#ffffff", 21))
    if adim == 1:
        lx, ly = x0 + 26, y0 + 180
        govde += t(lx, ly, m["ss_ek_bilgi"], 15, "#ffffff", 600, cizgi=True)
        govde += isaret(lx - 7, ly - 20, 88, 30, 1, rozet="sag")
        govde += (f'<rect x="{x0 + g - 150}" y="{y0 + h - 58}" width="126" height="36" fill="#174b8a" '
                  f'stroke="#ffffff" stroke-width="1.5"/>'
                  + t(x0 + g - 87, y0 + h - 34, m["ss_calistirma"], 15, "#ffffff", 600, hiza="middle"))
        baslik = m["baslik_ss1"]
    else:
        satir_y = y0 + 186
        govde += (t(x0 + 26, satir_y, m["ss_uygulama"], 14, "#ffffff")
                  + t(x0 + 116, satir_y, DOSYA, 14, "#ffffff", 600)
                  + t(x0 + 26, satir_y + 24, m["ss_yayimci"], 14, "#ffffff")
                  + t(x0 + 116, satir_y + 24, m["ss_bilinmeyen"], 14, "#ffffff"))
        bx = x0 + g - 300
        by = y0 + h - 58
        govde += (f'<rect x="{bx}" y="{by}" width="150" height="36" fill="#174b8a" stroke="#ffffff" stroke-width="1.5"/>'
                  + t(bx + 75, by + 24, m["ss_calistir"], 15, "#ffffff", 600, hiza="middle")
                  + f'<rect x="{bx + 162}" y="{by}" width="126" height="36" fill="#174b8a" stroke="#ffffff" '
                    f'stroke-width="1.5"/>'
                  + t(bx + 225, by + 24, m["ss_calistirma"], 15, "#ffffff", 600, hiza="middle")
                  + isaret(bx - 6, by - 6, 162, 48, 2))
        baslik = m["baslik_ss2"]
    govde += dipnot(gen, yuk, m["dipnot_ss"])
    return svg(gen, yuk, govde, baslik)


def edge_panel(m: dict) -> str:
    gen, yuk = 560, 356
    px, py, pg, ph = 10, 10, 480, 200
    govde = (f'<rect x="{px + 2}" y="{py + 4}" width="{pg}" height="{ph}" rx="10" fill="#000000" opacity="0.12"/>'
             f'<rect x="{px}" y="{py}" width="{pg}" height="{ph}" rx="10" fill="#ffffff" stroke="#d0d7de"/>'
             + t(px + 18, py + 32, m["edge_panel"], 16, "#1f2328", 600)
             + f'<line x1="{px}" y1="{py + 48}" x2="{px + pg}" y2="{py + 48}" stroke="#e6e6e6"/>'
             # uyarı simgesi
             + f'<path d="M{px + 32} {py + 70} l13 24 h-26 z" fill="#f2c94c" stroke="#9a6700" stroke-width="1.2"/>'
             + t(px + 32, py + 90, "!", 14, "#1f2328", 700, hiza="middle")
             + satirlar(px + 56, py + 76, m["edge_uyari"], 12.5, "#1f2328", 18))
    # satırdaki çöp kutusu (dosyayı siler) ve "..." (Diğer eylemler / More actions) düğmesi
    dx, dy = px + pg - 50, py + 64
    cx = dx - 34
    govde += (f'<path d="M{cx + 8} {dy + 9} h14 M{cx + 12} {dy + 9} v-2 h6 v2 M{cx + 10} {dy + 9} l1 13 h8 l1 -13" '
              f'stroke="#57606a" stroke-width="1.6" fill="none" stroke-linejoin="round"/>')
    govde += (f'<rect x="{dx}" y="{dy}" width="32" height="28" rx="6" fill="#f0f0f0"/>'
              + t(dx + 16, dy + 19, "⋯", 18, "#1f2328", 700, hiza="middle")
              + isaret(dx - 4, dy - 4, 40, 36, 1, rozet="sag"))
    # açılan menü
    mx, my, mg = px + 190, py + 130, 300
    oge = m["edge_menu"]
    mh = 12 + sum(30 if o else 12 for o in oge)
    govde += (f'<rect x="{mx + 2}" y="{my + 4}" width="{mg}" height="{mh}" rx="8" fill="#000000" opacity="0.12"/>'
              f'<rect x="{mx}" y="{my}" width="{mg}" height="{mh}" rx="8" fill="#ffffff" stroke="#d0d7de"/>')
    sy = my + 6
    for o in oge:
        if o is None:
            govde += f'<line x1="{mx + 10}" y1="{sy + 6}" x2="{mx + mg - 10}" y2="{sy + 6}" stroke="#e6e6e6"/>'
            sy += 12
            continue
        govde += t(mx + 18, sy + 20, o, 13.5, "#1f2328", 600 if o == m["edge_sakla"] else 400)
        if o == m["edge_sakla"]:
            govde += isaret(mx + 8, sy + 1, 120, 28, 2)
        sy += 30
    govde += dipnot(gen, yuk, m["dipnot_edge1"])
    return svg(gen, yuk, govde, m["baslik_edge1"])


def edge_dialog(m: dict) -> str:
    gen, yuk = 560, 372
    x0, y0, g, h = 10, 10, 540, 336
    govde = (f'<rect x="{x0 + 2}" y="{y0 + 4}" width="{g}" height="{h}" rx="10" fill="#000000" opacity="0.14"/>'
             f'<rect x="{x0}" y="{y0}" width="{g}" height="{h}" rx="10" fill="#ffffff" stroke="#d0d7de"/>'
             + satirlar(x0 + 22, y0 + 36, m["edge_d_baslik"], 17, "#1f2328", 23, 600)
             + satirlar(x0 + 22, y0 + 96, m["edge_d_govde"], 12.5, "#1f2328", 18)
             + t(x0 + 22, y0 + 164, m["edge_d_ad"], 12.5, "#1f2328")
             + t(x0 + 22, y0 + 184, m["edge_d_yayimci"], 12.5, "#1f2328")
             + t(x0 + 22, y0 + 212, m["edge_d_bildir"], 12.5, "#0f6cbd", cizgi=True)
             + t(x0 + 22, y0 + 234, m["edge_d_bilgi"], 12.5, "#0f6cbd", cizgi=True))
    # düğmeler: [İptal] [Sil | ˅]; okla açılan tek öğe: Yine de sakla
    by = y0 + h - 50
    sx = x0 + g - 132
    ix = sx - 96
    govde += (f'<rect x="{ix}" y="{by}" width="84" height="32" rx="6" fill="#ffffff" stroke="#8c959f"/>'
              + t(ix + 42, by + 21, m["edge_d_iptal"], 13.5, "#1f2328", 600, hiza="middle")
              + f'<rect x="{sx}" y="{by}" width="112" height="32" rx="6" fill="#0f6cbd"/>'
              + t(sx + 38, by + 21, m["edge_d_sil"], 13.5, "#ffffff", 600, hiza="middle")
              + f'<line x1="{sx + 76}" y1="{by + 6}" x2="{sx + 76}" y2="{by + 26}" stroke="#ffffff" opacity="0.6"/>'
              + f'<path d="M{sx + 88} {by + 13} l6 6 l6 -6" stroke="#ffffff" stroke-width="2" fill="none" '
                f'stroke-linecap="round" stroke-linejoin="round"/>'
              + isaret(sx + 77, by - 4, 37, 40, 3, rozet="sag"))
    my = by - 52
    govde += (f'<rect x="{sx - 40}" y="{my}" width="152" height="40" rx="8" fill="#ffffff" stroke="#d0d7de"/>'
              + t(sx - 24, my + 25, m["edge_d_yine"], 13.5, "#1f2328", 600)
              + isaret(sx - 34, my + 5, 140, 30, 4, rozet="sol"))
    govde += dipnot(gen, yuk, m["dipnot_edge2"])
    return svg(gen, yuk, govde, m["baslik_edge2"])


def kurulum_metinleri() -> dict:
    """Modül ekranının yazıları kurulum betiğinden okunur ([CustomMessages] Modul*): çizim kurulumla aynı kalır,
    metin bir yerde değişince yalnız bu betik yeniden çalıştırılır."""
    iss = (BURASI.parents[1] / "ArthurLegal-setup" / "kurulum" / "ArthurLegal.iss").read_text(encoding="utf-8-sig")
    metin = {"tr": {}, "en": {}}
    for satir in iss.splitlines():
        m = re.match(r"^(tr|en)\.(Modul\w+)=(.*)$", satir)
        if m:
            metin[m.group(1)][m.group(2)] = m.group(3)
    return metin


# Inno Setup 6'nın kendi metinleri (Default.isl, Languages\Turkish.isl) ve çizimin yazıları.
SIHIRBAZ = {
    "tr": {"pencere": "ArthurLegal - Kurulum yardımcısı", "onceki": "Önceki", "sonraki": "Sonraki", "iptal": "İptal",
           "dipnot": "Çizim · ArthurLegal kurulumunun modül ekranı (örnek görünüm)"},
    "en": {"pencere": "Setup - ArthurLegal", "onceki": "Back", "sonraki": "Next", "iptal": "Cancel",
           "dipnot": "Drawing · the module screen of ArthurLegal Setup (example)"},
}
MODUL_SIRASI = ("ModulHukuk", "ModulKurumsal", "ModulAdliye", "ModulAkademisyen", "ModulTapu", "ModulMask")


def moduller(dil: str, isaretli: tuple, numaralar: tuple, baslik: str) -> str:
    """Kurulumun modül ekranı: her modül kalın adlı bir onay kutusu ve altında gri kısa açıklama. ``isaretli``
    işaretli kutular; ``numaralar`` sırayla kırmızı çerçeve alan kutular, en sonda Sonraki düğmesi."""
    m, s = kurulum_metinleri()[dil], SIHIRBAZ[dil]
    gen, yuk = 600, 520
    x0, y0, g, h = 10, 10, 580, 484
    govde = (f'<rect x="{x0 + 2}" y="{y0 + 4}" width="{g}" height="{h}" fill="#000000" opacity="0.14"/>'
             f'<rect x="{x0}" y="{y0}" width="{g}" height="{h}" fill="#f0f0f0" stroke="#8c959f"/>'
             f'<rect x="{x0 + 1}" y="{y0 + 1}" width="{g - 2}" height="31" fill="#ffffff"/>'
             f'<rect x="{x0 + 10}" y="{y0 + 9}" width="16" height="16" fill="{LACIVERT}"/>'
             + t(x0 + 34, y0 + 22, s["pencere"], 12.5, "#1f2328")
             + t(x0 + g - 26, y0 + 22, "✕", 13, "#1f2328")
             + f'<rect x="{x0 + 1}" y="{y0 + 32}" width="{g - 2}" height="64" fill="#ffffff"/>'
             + t(x0 + 22, y0 + 54, m["ModulBaslik"], 13.5, "#1f2328", 700))
    aciklama = m["ModulAciklama"]
    if len(aciklama) > 84:  # sihirbazdaki gibi iki satır
        kes = aciklama.rfind(" ", 0, 84)
        govde += satirlar(x0 + 34, y0 + 74, [aciklama[:kes], aciklama[kes + 1:]], 12, "#1f2328", 16)
    else:
        govde += t(x0 + 34, y0 + 74, aciklama, 12, "#1f2328")
    govde += (f'<rect x="{x0 + g - 58}" y="{y0 + 38}" width="46" height="52" fill="{LACIVERT}"/>'
              + t(x0 + g - 35, y0 + 74, "A", 26, ALTIN, 700, hiza="middle")
              + f'<line x1="{x0 + 1}" y1="{y0 + 96}" x2="{x0 + g - 1}" y2="{y0 + 96}" stroke="#d0d7de"/>')
    y = y0 + 124
    cerceveler = {}
    for i, ileti in enumerate(MODUL_SIRASI):
        if i in (0, 4):
            if i == 4:
                y += 4
            govde += t(x0 + 22, y, m["ModulPaketler" if i == 0 else "ModulAraclar"], 12.5, "#1f2328")
            y += 14
        kx, ky = x0 + 24, y
        isaretli_mi = ileti in isaretli
        govde += (f'<rect x="{kx}" y="{ky}" width="13" height="13" fill="#ffffff" stroke="#333333"/>'
                  + (f'<path d="M{kx + 2.5} {ky + 6.5} l3 3 l5.5 -6" stroke="#1f2328" stroke-width="1.8" fill="none" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>' if isaretli_mi else "")
                  + t(kx + 20, ky + 11, m[ileti], 13, "#1f2328", 700)
                  + t(kx + 20, ky + 29, m[ileti + "Aciklama"], 12, "#6e7781"))
        cerceveler[ileti] = (kx - 5, ky - 5, 26 + len(m[ileti]) * 8, 23)
        y += 44
    by = y0 + h - 44
    govde += f'<line x1="{x0 + 1}" y1="{by - 12}" x2="{x0 + g - 1}" y2="{by - 12}" stroke="#d0d7de"/>'
    dugmeler = ((s["onceki"], x0 + g - 268), (s["sonraki"], x0 + g - 184), (s["iptal"], x0 + g - 96))
    for ad, bx in dugmeler:
        govde += (f'<rect x="{bx}" y="{by}" width="78" height="26" fill="#e1e1e1" '
                  f'stroke="{"#0f6cbd" if ad == s["sonraki"] else "#adadad"}"/>'
                  + t(bx + 39, by + 17, ad, 12.5, "#1f2328", hiza="middle"))
    for no, ileti in enumerate(numaralar, 1):
        if ileti == "sonraki":
            govde += isaret(x0 + g - 188, by - 4, 86, 34, no, rozet="ust")
        else:
            govde += isaret(*cerceveler[ileti], no, rozet="sag")
    govde += dipnot(gen, yuk, s["dipnot"])
    return svg(gen, yuk, govde, baslik)


# ---------------------------------------------------------------------------------------------------------------
# macOS çizimleri. Yazılar macOS 15.7'nin kendi yerelleştirmesinden (mac_metinleri.py, GitHub Actions'taki macOS
# bilgisayarında okundu, Ekim 2026): Installer (Giriş … Özet, Paket Adı/Eylem/Büyüklük, Yükle, Geri Dön),
# CoreServicesUIAgent (ilk açılış uyarısı: Açılmadı, Bitti, Yine de Aç) ve Sistem Ayarları (Gizlilik ve Güvenlik).
MAC_YAZI = "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', 'Segoe UI', Arial, sans-serif"
MAC_MAVI = "#007aff"
PAKET = "ArthurLegal-Kurulum.pkg"
MAC_METIN = {
    "tr": {
        "acilmadi": f"“{PAKET}” Açılmadı",
        "dogrulanamadi": f"Apple, “{PAKET}” öğesinin Mac’inize zarar verebilecek veya gizliliğinizi ihlal edebilecek "
                         "bir kötü amaçlı yazılım içermediğini doğrulayamadı.",
        "bitti": "Bitti", "cop": "Çöp Sepeti’ne Taşı",
        "gizlilik": "Gizlilik ve Güvenlik", "yine_de_ac": "Yine de Aç",
        "adimlar": ("Giriş", "Lisans", "Hedef Seç", "Yükleme Türü", "Yükleme", "Özet"),
        "sutunlar": ("Paket Adı", "Eylem", "Büyüklük"),
        "yukle": "Yükle", "atla": "Atla", "geri": "Geri Dön", "surdur": "Sürdür",
        "dipnot1": "Çizim · macOS ilk açılış uyarısı (örnek görünüm)",
        "dipnot2": "Çizim · Sistem Ayarları, Gizlilik ve Güvenlik (örnek görünüm)",
        "dipnot3": "Çizim · ArthurLegal macOS kurulumunun Yükleme Türü ekranı (örnek görünüm)",
        "baslik1": "Örnek: macOS'un Açılmadı penceresinde Bitti'ye tıklayın, mavi Çöp Sepeti'ne Taşı'ya değil",
        "baslik2": "Örnek: Sistem Ayarları'nda Gizlilik ve Güvenlik'i seçip Yine de Aç'a tıklayın",
    },
    "en": {
        "acilmadi": f"“{PAKET}” Not Opened",
        "dogrulanamadi": f"Apple could not verify “{PAKET}” is free of malware that may harm your Mac or compromise "
                         "your privacy.",
        "bitti": "Done", "cop": "Move to Trash",
        "gizlilik": "Privacy & Security", "yine_de_ac": "Open Anyway",
        "adimlar": ("Introduction", "License", "Destination Select", "Installation Type", "Installation", "Summary"),
        "sutunlar": ("Package Name", "Action", "Size"),
        "yukle": "Install", "atla": "Skip", "geri": "Go Back", "surdur": "Continue",
        "dipnot1": "Drawing · macOS first-launch warning (example)",
        "dipnot2": "Drawing · System Settings, Privacy & Security (example)",
        "dipnot3": "Drawing · the Installation Type screen of the ArthurLegal Mac installer (example)",
        "baslik1": "Example: in macOS's Not Opened window, click Done, not the blue Move to Trash",
        "baslik2": "Example: in System Settings choose Privacy & Security, then click Open Anyway",
    },
}
MAC_DOSYALAR = {"tr": ("mac-1-acilmadi.svg", "mac-2-yine-de-ac.svg"),
                "en": ("mac-1-not-opened-en.svg", "mac-2-open-anyway-en.svg")}


def sar(metin: str, en_fazla: int) -> list:
    """Sözcük sınırında satırlara böler (yaklaşık karakter sayısıyla)."""
    satir, sonuc = "", []
    for sozcuk in metin.split():
        if satir and len(satir) + 1 + len(sozcuk) > en_fazla:
            sonuc.append(satir)
            satir = sozcuk
        else:
            satir = f"{satir} {sozcuk}".strip()
    return sonuc + ([satir] if satir else [])


def mac_pencere(x, y, g, h, renk="#ececec", r=12) -> str:
    """Gölgeli, köşeleri yuvarlak macOS penceresi; sol üstte üç düğme."""
    return (f'<rect x="{x + 1}" y="{y + 5}" width="{g}" height="{h}" rx="{r}" fill="#000000" opacity="0.16"/>'
            f'<rect x="{x}" y="{y}" width="{g}" height="{h}" rx="{r}" fill="{renk}" stroke="#b9b9be"/>'
            + "".join(f'<circle cx="{x + 18 + i * 20}" cy="{y + 18}" r="6" fill="{c}"/>'
                      for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840"))))


def uyari_simgesi(cx, cy, boy=50) -> str:
    """macOS uyarı penceresinin sarı üçgeni ve ünlem işareti."""
    y = cy - boy / 2
    return (f'<path d="M{cx} {y} L{cx + boy * 0.56} {y + boy * 0.92} Q{cx + boy * 0.6} {y + boy} {cx + boy * 0.5} {y + boy} '
            f'H{cx - boy * 0.5} Q{cx - boy * 0.6} {y + boy} {cx - boy * 0.56} {y + boy * 0.92} Z" fill="#ffcc00" '
            f'stroke="#d9a400" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<rect x="{cx - 3}" y="{y + boy * 0.3}" width="6" height="{boy * 0.38}" rx="3" fill="#3a3a3c"/>'
            f'<circle cx="{cx}" cy="{y + boy * 0.82}" r="3.4" fill="#3a3a3c"/>')


def mac_acilmadi(m: dict) -> str:
    """İlk açılış uyarısı (macOS 15): Apple'ın onayından (noterleştirme) geçmemiş paket açılmaz. Bitti ile kapatılır;
    mavi olan ve Enter'ın seçtiği düğme Çöp Sepeti'ne Taşı'dır."""
    gen, yuk = 420, 360
    x0, y0, g, h = 55, 10, 310, 316
    govde = (f'<rect x="{x0 + 1}" y="{y0 + 5}" width="{g}" height="{h}" rx="14" fill="#000000" opacity="0.16"/>'
             f'<rect x="{x0}" y="{y0}" width="{g}" height="{h}" rx="14" fill="#ececee" stroke="#b9b9be"/>'
             f'<circle cx="{x0 + g - 26}" cy="{y0 + 26}" r="9" fill="#ffffff" stroke="#c7c7cc"/>'
             + t(x0 + g - 26, y0 + 30.5, "?", 12, "#3a3a3c", 600, hiza="middle")
             + uyari_simgesi(x0 + g / 2, y0 + 52))
    y = y0 + 110
    baslik = m["acilmadi"]
    kes = baslik.index("”") + 1                     # macOS dosya adından sonra satır kırar
    for satir in (baslik[:kes], baslik[kes:].strip()):
        govde += t(x0 + g / 2, y, satir, 13, "#1d1d1f", 700, hiza="middle")
        y += 17
    y += 6
    for satir in sar(m["dogrulanamadi"], 44):
        govde += t(x0 + g / 2, y, satir, 11, "#1d1d1f", 400, hiza="middle")
        y += 15
    by = y0 + h - 46
    bg = (g - 46) / 2
    bx, cx = x0 + 18, x0 + 28 + bg
    govde += (f'<rect x="{bx}" y="{by}" width="{bg}" height="28" rx="7" fill="#dcdce0"/>'
              + t(bx + bg / 2, by + 18.5, m["bitti"], 12, "#1d1d1f", 500, hiza="middle")
              + f'<rect x="{cx}" y="{by}" width="{bg}" height="28" rx="7" fill="{MAC_MAVI}"/>'
              + t(cx + bg / 2, by + 18.5, m["cop"], 12, "#ffffff", 500, hiza="middle")
              + isaret(bx - 5, by - 5, bg + 10, 38, 1, rozet="sol"))
    govde += dipnot(gen, yuk, m["dipnot1"])
    return svg(gen, yuk, govde, m["baslik1"], MAC_YAZI)


def mac_yine_de_ac(m: dict) -> str:
    """Sistem Ayarları → Gizlilik ve Güvenlik: engellenen paketin satırındaki Yine de Aç."""
    gen, yuk = 600, 372
    x0, y0, g, h = 24, 10, 566, 334   # solda numara rozetine yer
    sw = 176
    govde = mac_pencere(x0, y0, g, h, "#ffffff")
    govde += (f'<path d="M{x0 + 12} {y0} h{sw - 12} v{h} h{-sw + 12} q-12 0 -12 -12 v{-h + 24} q0 -12 12 -12 z" '
              f'fill="#ececee"/>'
              f'<rect x="{x0 + 10}" y="{y0 + 38}" width="{sw - 20}" height="22" rx="6" fill="#dcdce0"/>')
    # kenar çubuğu: ötekiler yer tutucu, seçili olan Gizlilik ve Güvenlik
    sy = y0 + 74
    for i in range(9):
        if i == 6:
            govde += (f'<rect x="{x0 + 8}" y="{sy - 3}" width="{sw - 16}" height="24" rx="6" fill="{MAC_MAVI}"/>'
                      f'<rect x="{x0 + 16}" y="{sy + 2}" width="14" height="14" rx="4" fill="#ffffff" opacity="0.9"/>'
                      + t(x0 + 38, sy + 14, m["gizlilik"], 12, "#ffffff", 600)
                      + isaret(x0 + 4, sy - 7, sw - 8, 32, 2, rozet="sol"))
        else:
            govde += (f'<rect x="{x0 + 16}" y="{sy + 2}" width="14" height="14" rx="4" fill="#c7c7cc"/>'
                      f'<rect x="{x0 + 38}" y="{sy + 5}" width="{60 + (i * 23) % 50}" height="8" rx="4" fill="#d1d1d6"/>')
        sy += 28
    # içerik
    cx = x0 + sw + 20
    cg = g - sw - 40
    govde += t(cx, y0 + 30, m["gizlilik"], 14, "#1d1d1f", 700)
    for i in range(3):  # üstteki bölümler: yer tutucu
        govde += (f'<rect x="{cx}" y="{y0 + 50 + i * 34}" width="{cg}" height="28" rx="7" fill="#f5f5f7" stroke="#e5e5ea"/>'
                  f'<rect x="{cx + 12}" y="{y0 + 60 + i * 34}" width="{90 + i * 30}" height="8" rx="4" fill="#d1d1d6"/>')
    # sayfanın altındaki bölüm: engellenen paketin satırı (yazısı yer tutucu; macOS sürümüne göre değişir)
    gy = y0 + 166
    govde += f'<rect x="{cx}" y="{gy - 9}" width="70" height="9" rx="4" fill="#c7c7cc"/>'
    kx, ky, kh = cx, gy + 10, 112
    govde += (f'<rect x="{kx}" y="{ky}" width="{cg}" height="{kh}" rx="8" fill="#f5f5f7" stroke="#e5e5ea"/>'
              + t(kx + 14, ky + 26, f"“{PAKET}”", 12, "#1d1d1f", 700)
              + f'<rect x="{kx + 14}" y="{ky + 36}" width="{cg - 60}" height="8" rx="4" fill="#d1d1d6"/>'
              + f'<rect x="{kx + 14}" y="{ky + 52}" width="{cg - 150}" height="8" rx="4" fill="#d1d1d6"/>')
    bx, by, bg = kx + cg - 112, ky + kh - 40, 98
    govde += (f'<rect x="{bx}" y="{by}" width="{bg}" height="26" rx="7" fill="#ffffff" stroke="#c7c7cc"/>'
              + t(bx + bg / 2, by + 17.5, m["yine_de_ac"], 12.5, "#1d1d1f", 500, hiza="middle")
              + isaret(bx - 5, by - 5, bg + 10, 36, 3, rozet="sol"))
    govde += dipnot(gen, yuk, m["dipnot2"])
    return svg(gen, yuk, govde, m["baslik2"], MAC_YAZI)


def mac_metinleri_kurulum(dil: str) -> dict:
    """Modül adları ve açıklamaları: Windows sihirbazınınkiler (ArthurLegal.iss) ve Mac'teki Arthur Mask koşulu."""
    m = dict(kurulum_metinleri()[dil])
    kaynak = (BURASI.parents[1] / "ArthurLegal-setup" / "yayin" / "derle_macos.py").read_text(encoding="utf-8")
    kosul = re.search(rf'"{dil}": "([^"]*)"', kaynak[kaynak.index("MASK_KOSULU"):]).group(1)
    m["ModulMaskAciklama"] = m["ModulMaskAciklama"] + kosul
    return m


def mac_moduller(dil: str, isaretli: tuple, numaralar: tuple, baslik: str) -> str:
    """macOS kurulumunun Yükleme Türü ekranı: modüller tabloda onay kutusuyla; seçilen modülün açıklaması altta.
    ``numaralar`` sırayla kırmızı çerçeve alan satırlar, en sonda Sürdür düğmesi (Yükle sonraki sayfadadır)."""
    mm, m = MAC_METIN[dil], mac_metinleri_kurulum(dil)
    gen, yuk = 640, 500
    x0, y0, g, h = 10, 10, 620, 462
    govde = mac_pencere(x0, y0, g, h, "#ececec")
    # sol: adımlar
    ay = y0 + 70
    for adim in mm["adimlar"]:
        su_an = adim == mm["adimlar"][3]
        gecti = mm["adimlar"].index(adim) < 3
        govde += (f'<circle cx="{x0 + 30}" cy="{ay - 4}" r="4.5" fill="{MAC_MAVI if su_an else ("#8e8e93" if gecti else "#d1d1d6")}"/>'
                  + t(x0 + 42, ay, adim, 12, "#1d1d1f" if su_an or gecti else "#8e8e93", 700 if su_an else 400))
        ay += 26
    # sağ: içerik
    cx, cy, cg = x0 + 170, y0 + 46, g - 186
    govde += f'<rect x="{cx}" y="{cy}" width="{cg}" height="{h - 110}" rx="8" fill="#ffffff" stroke="#d1d1d6"/>'
    govde += f'<rect x="{cx + 16}" y="{cy + 16}" width="190" height="10" rx="5" fill="#c7c7cc"/>'   # başlık
    tx, ty, tg = cx + 14, cy + 40, cg - 28
    sutun = (tx + 10, tx + tg - 150, tx + tg - 70)
    govde += (f'<rect x="{tx}" y="{ty}" width="{tg}" height="{22 + 6 * 24}" fill="#ffffff" stroke="#d1d1d6"/>'
              f'<rect x="{tx}" y="{ty}" width="{tg}" height="22" fill="#f5f5f7" stroke="#d1d1d6"/>'
              + "".join(t(sx, ty + 15, ad, 11, "#3a3a3c", 600) for sx, ad in zip(sutun, mm["sutunlar"])))
    satirlar_y = {}
    sy = ty + 22
    secili = numaralar[-2] if len(numaralar) > 1 else MODUL_SIRASI[0]
    for ileti in MODUL_SIRASI:
        isaretli_mi = ileti in isaretli
        if ileti == secili:
            govde += f'<rect x="{tx + 1}" y="{sy}" width="{tg - 2}" height="24" fill="#dce9fb"/>'
        kx, ky = sutun[0], sy + 6
        govde += (f'<rect x="{kx}" y="{ky}" width="12" height="12" rx="3" '
                  f'fill="{MAC_MAVI if isaretli_mi else "#ffffff"}" stroke="{MAC_MAVI if isaretli_mi else "#8e8e93"}"/>'
                  + (f'<path d="M{kx + 2.5} {ky + 6} l2.8 2.8 l4.5 -5.3" stroke="#ffffff" stroke-width="1.8" fill="none" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>' if isaretli_mi else "")
                  + t(kx + 20, sy + 16.5, m[ileti], 12, "#1d1d1f")
                  + t(sutun[1], sy + 16.5, mm["yukle"] if isaretli_mi else mm["atla"], 12, "#1d1d1f" if isaretli_mi else "#8e8e93")
                  + t(sutun[2], sy + 16.5, "1 KB", 12, "#1d1d1f" if isaretli_mi else "#8e8e93"))
        satirlar_y[ileti] = sy
        sy += 24
    # gereken ve kalan alan satırı (yer tutucu), sonra seçili modülün açıklaması
    govde += (f'<rect x="{tx + 10}" y="{sy + 12}" width="120" height="8" rx="4" fill="#d1d1d6"/>'
              f'<rect x="{tx + tg - 130}" y="{sy + 12}" width="120" height="8" rx="4" fill="#d1d1d6"/>')
    ay = sy + 30
    govde += f'<rect x="{tx}" y="{ay}" width="{tg}" height="70" rx="4" fill="#ffffff" stroke="#d1d1d6"/>'
    yy = ay + 20
    for satir in sar(m[secili + "Aciklama"], 64):
        govde += t(tx + 10, yy, satir, 11.5, "#1d1d1f")
        yy += 16
    # düğmeler
    by = y0 + h - 46
    yx = x0 + g - 112
    gx = yx - 112
    govde += (f'<rect x="{gx}" y="{by}" width="100" height="28" rx="7" fill="#ffffff" stroke="#c7c7cc"/>'
              + t(gx + 50, by + 18.5, mm["geri"], 12.5, "#1d1d1f", 500, hiza="middle")
              + f'<rect x="{yx}" y="{by}" width="100" height="28" rx="7" fill="{MAC_MAVI}"/>'
              + t(yx + 50, by + 18.5, mm["surdur"], 12.5, "#ffffff", 600, hiza="middle"))
    for no, ileti in enumerate(numaralar, 1):
        if ileti == "surdur":
            govde += isaret(yx - 5, by - 5, 110, 38, no, rozet="ust")
        else:
            govde += isaret(sutun[0] - 6, satirlar_y[ileti] + 1, 30 + len(m[ileti]) * 7.4, 22, no, rozet="sag")
    govde += dipnot(gen, yuk, mm["dipnot3"])
    return svg(gen, yuk, govde, baslik, MAC_YAZI)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ciktilar = {
        "indir-dugmesi.svg": dugme("Windows için indir · Download for Windows",
                                   "ArthurLegal kurulumu · installer (.exe) — hep en güncel · always the latest",
                                   "Windows için indir · Download for Windows: ArthurLegal-Kurulum.exe, her zaman en "
                                   "güncel sürüm · always the latest version"),
        "indir-dugmesi-mac.svg": dugme("Mac için indir · Download for Mac",
                                       "ArthurLegal kurulumu · installer (.pkg) — Apple Silicon · Intel · macOS 11+",
                                       "Mac için indir · Download for Mac: ArthurLegal-Kurulum.pkg, her zaman en güncel "
                                       "sürüm · always the latest version"),
    }
    for dil, m in METIN.items():
        d = DOSYALAR[dil]
        ciktilar.update({d["edge1"]: edge_panel(m), d["edge2"]: edge_dialog(m),
                         d["ss1"]: smartscreen(m, 1), d["ss2"]: smartscreen(m, 2)})
    # Modül ekranı: ana sayfa için genel örnek (avukat), Courthouse sayfası için hâkim ve kalem örneği.
    ciktilar.update({
        "moduller.svg": moduller("tr", ("ModulHukuk", "ModulTapu", "ModulMask"),
                                 ("ModulHukuk", "ModulTapu", "ModulMask", "sonraki"),
                                 "Örnek: modül ekranında paketinizi (burada Hukuk Bürosu), isterseniz Tapu ve Arthur Mask'i "
                                 "işaretleyip Sonraki'ye tıklayın"),
        "modules-en.svg": moduller("en", ("ModulHukuk", "ModulTapu", "ModulMask"),
                                   ("ModulHukuk", "ModulTapu", "ModulMask", "sonraki"),
                                   "Example: on the module screen tick your package (here Law Firm), optionally Tapu and "
                                   "Arthur Mask, then click Next"),
        "moduller-courthouse.svg": moduller("tr", ("ModulAdliye", "ModulTapu", "ModulMask"),
                                            ("ModulAdliye", "ModulTapu", "ModulMask", "sonraki"),
                                            "Örnek: modül ekranında Courthouse, ArthurLegal Tapu ve Arthur Mask'i "
                                            "işaretleyip Sonraki'ye tıklayın"),
    })
    for dil, (ad1, ad2) in MAC_DOSYALAR.items():
        ciktilar.update({ad1: mac_acilmadi(MAC_METIN[dil]), ad2: mac_yine_de_ac(MAC_METIN[dil])})
    ciktilar.update({
        "mac-3-moduller.svg": mac_moduller("tr", ("ModulHukuk", "ModulTapu", "ModulMask"),
                                           ("ModulHukuk", "ModulTapu", "ModulMask", "surdur"),
                                           "Örnek: Yükleme Türü ekranında paketinizi (burada Hukuk Bürosu), isterseniz Tapu "
                                           "ve Arthur Mask'i işaretleyip Sürdür'e tıklayın"),
        "mac-3-modules-en.svg": mac_moduller("en", ("ModulHukuk", "ModulTapu", "ModulMask"),
                                             ("ModulHukuk", "ModulTapu", "ModulMask", "surdur"),
                                             "Example: on the Installation Type screen tick your package (here Law Firm), "
                                             "optionally Tapu and Arthur Mask, then click Continue"),
        "mac-3-moduller-courthouse.svg": mac_moduller("tr", ("ModulAdliye", "ModulTapu", "ModulMask"),
                                                      ("ModulAdliye", "ModulTapu", "ModulMask", "surdur"),
                                                      "Örnek: Yükleme Türü ekranında Courthouse, ArthurLegal Tapu ve "
                                                      "Arthur Mask'i işaretleyip Sürdür'e tıklayın"),
    })
    for ad, icerik in ciktilar.items():
        (BURASI / ad).write_text(icerik, encoding="utf-8", newline="\n")
        print(f"  yazıldı: docs/kurulum/{ad}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
