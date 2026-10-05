"""README'nin indirme bölümündeki çizimleri (SVG) üretir.

    python docs/kurulum/cizim_uret.py

Çizimler ekran görüntüsü değildir: Windows ve Edge pencerelerinin sade bir taslağıdır, tıklanacak
yer kırmızı çerçeve ve numarayla gösterilir. Üzerindeki yazılar Türkçe Windows'un ve Edge'in birebir
metinleridir; Microsoft bir metni değiştirirse yalnız aşağıdaki METIN sözlüğü düzeltilip bu betik
yeniden çalıştırılır. SVG dosyaları elle düzenlenmez.
"""
from __future__ import annotations

import sys
from pathlib import Path
from xml.sax.saxutils import escape

BURASI = Path(__file__).resolve().parent
DOSYA = "ArthurLegal-Kurulum.exe"

# Ekranda birebir görünen metinler. Kaynaklar README'nin indirme bölümünde ve commit mesajında.
METIN = {
    "ss_baslik": "Windows bilgisayarınızı korudu",
    "ss_govde": [
        "Microsoft Defender SmartScreen tanınmayan bir uygulamanın",
        "başlatılmasını engelledi. Bu uygulamanın çalıştırılması",
        "bilgisayarınızı riske atabilir.",
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
    "edge_menu": ["Sil", "Sakla", "Bu dosyayı güvenli olarak bildir", "Daha fazla bilgi edinin", "Bağlantıyı kopyala"],
    "edge_sakla": "Sakla",
    "edge_d_baslik": [f"Açmadan önce {DOSYA} dosyasının", "güvenilir olduğundan emin olun"],
    "edge_d_govde": [
        "Dosya yaygın olarak indirilmediğinden Microsoft Defender SmartScreen",
        "bu dosyanın güvenli olup olmadığı doğrulayamadı. Açmadan önce",
        "indirdiğiniz dosyanın veya kaynağının güvenli olduğundan emin olun.",
    ],
    "edge_d_ad": f"Ad: {DOSYA}",
    "edge_d_bildir": "Bu uygulamayı güvenli olarak bildir",
    "edge_d_bilgi": "Microsoft Defender SmartScreen hakkında daha fazla bilgi edinin",
    "edge_d_daha": "Daha fazla göster",
    "edge_d_yine": "Yine de sakla",
    "edge_d_sil": "Sil",
    "edge_d_iptal": "İptal",
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
    """Tıklanacak yerin kırmızı çerçevesi ve numara rozeti."""
    rx = x - 14 if rozet == "sol" else x + g + 14
    return (f'<rect x="{x}" y="{y}" width="{g}" height="{h}" rx="7" fill="none" stroke="{KIRMIZI}" stroke-width="3"/>'
            f'<circle cx="{rx}" cy="{y + h / 2}" r="13" fill="{KIRMIZI}"/>'
            + t(rx, y + h / 2 + 5, str(no), 15, "#ffffff", 700, hiza="middle"))


def svg(gen, yuk, govde, baslik) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{gen}" height="{yuk}" viewBox="0 0 {gen} {yuk}" '
            f'role="img" aria-label="{escape(baslik, {chr(34): "&quot;"})}">'
            f'<title>{escape(baslik)}</title><g font-family="{YAZI}">{govde}</g></svg>\n')


def dipnot(gen, yuk, s) -> str:
    return t(gen / 2, yuk - 8, s, 12, "#8b949e", 400, hiza="middle")


def dugme() -> str:
    gen, yuk = 640, 116
    ok = (f'<circle cx="66" cy="58" r="34" fill="{ALTIN}"/>'
          '<path d="M66 36 v32 M52 56 l14 14 l14 -14" stroke="#14233c" stroke-width="6" fill="none" '
          'stroke-linecap="round" stroke-linejoin="round"/><path d="M48 78 h36" stroke="#14233c" stroke-width="6" '
          'stroke-linecap="round"/>')
    govde = (f'<rect x="2" y="2" width="{gen - 4}" height="{yuk - 4}" rx="18" fill="{LACIVERT}" stroke="{ALTIN}" '
             f'stroke-width="3"/>{ok}'
             + t(120, 54, "ArthurLegal'i indir", 32, "#ffffff", 700)
             + t(121, 84, "Windows kurulum dosyası · her zaman en güncel sürüm", 17, "#e6d6a8", 400))
    return svg(gen, yuk, govde, "ArthurLegal'i indir: Windows kurulum dosyası, her zaman en güncel sürüm")


def smartscreen(adim: int) -> str:
    gen, yuk = 560, 352
    x0, y0, g, h = 10, 10, 540, 316
    govde = (f'<rect x="{x0 + 3}" y="{y0 + 4}" width="{g}" height="{h}" fill="#000000" opacity="0.18"/>'
             f'<rect x="{x0}" y="{y0}" width="{g}" height="{h}" fill="{SS_MAVI}" stroke="#16477f"/>'
             + t(x0 + 506, y0 + 26, "✕", 15, "#ffffff", 400)
             + t(x0 + 26, y0 + 66, METIN["ss_baslik"], 27, "#ffffff", 600)
             + satirlar(x0 + 26, y0 + 102, METIN["ss_govde"], 14.5, "#ffffff", 21))
    if adim == 1:
        lx, ly = x0 + 26, y0 + 180
        govde += t(lx, ly, METIN["ss_ek_bilgi"], 15, "#ffffff", 600, cizgi=True)
        govde += isaret(lx - 7, ly - 20, 82, 30, 1, rozet="sag")
        govde += (f'<rect x="{x0 + g - 150}" y="{y0 + h - 58}" width="126" height="36" fill="#174b8a" '
                  f'stroke="#ffffff" stroke-width="1.5"/>'
                  + t(x0 + g - 87, y0 + h - 34, METIN["ss_calistirma"], 15, "#ffffff", 600, hiza="middle"))
        baslik = "Örnek: SmartScreen penceresinde önce Ek bilgi yazısına tıklayın"
    else:
        satir_y = y0 + 186
        govde += (t(x0 + 26, satir_y, METIN["ss_uygulama"], 14, "#ffffff")
                  + t(x0 + 116, satir_y, DOSYA, 14, "#ffffff", 600)
                  + t(x0 + 26, satir_y + 24, METIN["ss_yayimci"], 14, "#ffffff")
                  + t(x0 + 116, satir_y + 24, METIN["ss_bilinmeyen"], 14, "#ffffff"))
        bx = x0 + g - 300
        by = y0 + h - 58
        govde += (f'<rect x="{bx}" y="{by}" width="150" height="36" fill="#174b8a" stroke="#ffffff" stroke-width="1.5"/>'
                  + t(bx + 75, by + 24, METIN["ss_calistir"], 15, "#ffffff", 600, hiza="middle")
                  + f'<rect x="{bx + 162}" y="{by}" width="126" height="36" fill="#174b8a" stroke="#ffffff" '
                    f'stroke-width="1.5"/>'
                  + t(bx + 225, by + 24, METIN["ss_calistirma"], 15, "#ffffff", 600, hiza="middle")
                  + isaret(bx - 6, by - 6, 162, 48, 2))
        baslik = "Örnek: Ek bilgi'den sonra Yine de çalıştır düğmesine tıklayın"
    govde += dipnot(gen, yuk, "Çizim · Windows SmartScreen uyarısı (örnek görünüm)")
    return svg(gen, yuk, govde, baslik)


def edge_panel() -> str:
    gen, yuk = 560, 350
    px, py, pg, ph = 10, 10, 480, 200
    govde = (f'<rect x="{px + 2}" y="{py + 4}" width="{pg}" height="{ph}" rx="10" fill="#000000" opacity="0.12"/>'
             f'<rect x="{px}" y="{py}" width="{pg}" height="{ph}" rx="10" fill="#ffffff" stroke="#d0d7de"/>'
             + t(px + 18, py + 32, METIN["edge_panel"], 16, "#1f2328", 600)
             + f'<line x1="{px}" y1="{py + 48}" x2="{px + pg}" y2="{py + 48}" stroke="#e6e6e6"/>'
             # uyarı simgesi
             + f'<path d="M{px + 32} {py + 70} l13 24 h-26 z" fill="#f2c94c" stroke="#9a6700" stroke-width="1.2"/>'
             + t(px + 32, py + 90, "!", 14, "#1f2328", 700, hiza="middle")
             + satirlar(px + 56, py + 76, METIN["edge_uyari"], 12.5, "#1f2328", 18))
    # "..." düğmesi
    dx, dy = px + pg - 50, py + 64
    govde += (f'<rect x="{dx}" y="{dy}" width="32" height="28" rx="6" fill="#f0f0f0"/>'
              + t(dx + 16, dy + 19, "⋯", 18, "#1f2328", 700, hiza="middle")
              + isaret(dx - 4, dy - 4, 40, 36, 1, rozet="sag"))
    # açılan menü
    mx, my, mg = px + 190, py + 130, 300
    mh = 16 + 30 * len(METIN["edge_menu"])
    govde += (f'<rect x="{mx + 2}" y="{my + 4}" width="{mg}" height="{mh}" rx="8" fill="#000000" opacity="0.12"/>'
              f'<rect x="{mx}" y="{my}" width="{mg}" height="{mh}" rx="8" fill="#ffffff" stroke="#d0d7de"/>')
    for i, s in enumerate(METIN["edge_menu"]):
        sy = my + 30 + i * 30
        govde += t(mx + 18, sy, s, 13.5, "#1f2328", 600 if s == METIN["edge_sakla"] else 400)
        if s == METIN["edge_sakla"]:
            govde += isaret(mx + 8, sy - 20, 120, 28, 2)
    govde += dipnot(gen, yuk, "Çizim · Microsoft Edge indirme uyarısı (örnek görünüm)")
    return svg(gen, yuk, govde, "Örnek: Edge'de indirilen dosyanın yanındaki üç noktaya, sonra Sakla'ya tıklayın")


def edge_dialog() -> str:
    gen, yuk = 560, 372
    x0, y0, g, h = 10, 10, 540, 336
    govde = (f'<rect x="{x0 + 2}" y="{y0 + 4}" width="{g}" height="{h}" rx="10" fill="#000000" opacity="0.14"/>'
             f'<rect x="{x0}" y="{y0}" width="{g}" height="{h}" rx="10" fill="#ffffff" stroke="#d0d7de"/>'
             + satirlar(x0 + 22, y0 + 36, METIN["edge_d_baslik"], 17, "#1f2328", 23, 600)
             + satirlar(x0 + 22, y0 + 96, METIN["edge_d_govde"], 12.5, "#1f2328", 18)
             + t(x0 + 22, y0 + 164, METIN["edge_d_ad"], 12.5, "#1f2328")
             + t(x0 + 22, y0 + 190, METIN["edge_d_bildir"], 12.5, "#0f6cbd", cizgi=True)
             + t(x0 + 22, y0 + 212, METIN["edge_d_bilgi"], 12.5, "#0f6cbd", cizgi=True))
    dy = y0 + 244
    govde += (t(x0 + 22, dy, METIN["edge_d_daha"], 13.5, "#1f2328", 600)
              + f'<path d="M{x0 + 158} {dy - 8} l5 5 l5 -5" stroke="#1f2328" stroke-width="1.8" fill="none" '
                f'stroke-linecap="round" stroke-linejoin="round"/>'
              + isaret(x0 + 14, dy - 20, 168, 30, 3, rozet="sag"))
    yy = dy + 38
    govde += (f'<rect x="{x0 + 22}" y="{yy - 22}" width="120" height="32" rx="6" fill="#ffffff" stroke="#8c959f"/>'
              + t(x0 + 82, yy - 1, METIN["edge_d_yine"], 13.5, "#1f2328", 600, hiza="middle")
              + isaret(x0 + 16, yy - 28, 132, 44, 4, rozet="sag"))
    bx = x0 + g - 196
    by = y0 + h - 50
    govde += (f'<rect x="{bx}" y="{by}" width="84" height="32" rx="6" fill="#0f6cbd"/>'
              + t(bx + 42, by + 21, METIN["edge_d_sil"], 13.5, "#ffffff", 600, hiza="middle")
              + f'<rect x="{bx + 96}" y="{by}" width="84" height="32" rx="6" fill="#ffffff" stroke="#8c959f"/>'
              + t(bx + 138, by + 21, METIN["edge_d_iptal"], 13.5, "#1f2328", 600, hiza="middle"))
    govde += dipnot(gen, yuk, "Çizim · Microsoft Edge onay penceresi (örnek görünüm)")
    return svg(gen, yuk, govde, "Örnek: Daha fazla göster'e, sonra Yine de sakla'ya tıklayın")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ciktilar = {
        "indir-dugmesi.svg": dugme(),
        "edge-1-sakla.svg": edge_panel(),
        "edge-2-yine-de-sakla.svg": edge_dialog(),
        "smartscreen-1-ek-bilgi.svg": smartscreen(1),
        "smartscreen-2-yine-de-calistir.svg": smartscreen(2),
    }
    for ad, icerik in ciktilar.items():
        (BURASI / ad).write_text(icerik, encoding="utf-8", newline="\n")
        print(f"  yazıldı: docs/kurulum/{ad}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
