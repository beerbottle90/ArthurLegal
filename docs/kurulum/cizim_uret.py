"""README'nin indirme bölümündeki çizimleri (SVG) üretir: Türkçe ve İngilizce.

    python docs/kurulum/cizim_uret.py

Çizimler ekran görüntüsü değildir: Windows ve Edge pencerelerinin sade bir taslağıdır, tıklanacak
yer kırmızı çerçeve ve numarayla gösterilir. Üzerindeki yazılar Windows'un ve Edge'in o dildeki birebir
metinleridir; Microsoft bir metni değiştirirse yalnız aşağıdaki METIN sözlüğü düzeltilip bu betik
yeniden çalıştırılır. SVG dosyaları elle düzenlenmez.

Modül ekranı çizimlerinin (moduller.svg, modules-en.svg, moduller-courthouse.svg) yazıları ArthurLegal kurulum
betiğinden okunur (ArthurLegal-setup/kurulum/ArthurLegal.iss, Modul* iletileri).
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


def svg(gen, yuk, govde, baslik) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{gen}" height="{yuk}" viewBox="0 0 {gen} {yuk}" '
            f'role="img" aria-label="{escape(baslik, {chr(34): "&quot;"})}">'
            f'<title>{escape(baslik)}</title><g font-family="{YAZI}">{govde}</g></svg>\n')


def dipnot(gen, yuk, s) -> str:
    return t(gen / 2, yuk - 8, s, 12, "#8b949e", 400, hiza="middle")


def dugme() -> str:
    """İki dilli indirme düğmesi: README'nin en üstünde, her iki dildeki okura."""
    gen, yuk = 700, 116
    ok = (f'<circle cx="66" cy="58" r="34" fill="{ALTIN}"/>'
          '<path d="M66 36 v32 M52 56 l14 14 l14 -14" stroke="#14233c" stroke-width="6" fill="none" '
          'stroke-linecap="round" stroke-linejoin="round"/><path d="M48 78 h36" stroke="#14233c" stroke-width="6" '
          'stroke-linecap="round"/>')
    govde = (f'<rect x="2" y="2" width="{gen - 4}" height="{yuk - 4}" rx="18" fill="{LACIVERT}" stroke="{ALTIN}" '
             f'stroke-width="3"/>{ok}'
             + t(120, 54, "ArthurLegal'i indir · Download", 30, "#ffffff", 700)
             + t(121, 84, "Windows kurulumu · installer — hep en güncel · always the latest", 16, "#e6d6a8", 400))
    return svg(gen, yuk, govde, "ArthurLegal'i indir · Download ArthurLegal: Windows kurulum dosyası, her zaman en "
                                "güncel sürüm · Windows installer, always the latest version")


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


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ciktilar = {"indir-dugmesi.svg": dugme()}
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
    for ad, icerik in ciktilar.items():
        (BURASI / ad).write_text(icerik, encoding="utf-8", newline="\n")
        print(f"  yazıldı: docs/kurulum/{ad}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
