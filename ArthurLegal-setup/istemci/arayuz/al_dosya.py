"""Masada dosya (3.5.0, 23.11.2026): Claude'un ürettiği dosya masada açılır ve indirilir.

Kullanıcı: "Claude herhangi bir dosya üretir ve indirmem için bana getirirse bu dosyalar AL masasında gözükmüyor, chat'e
geçmek gerekiyor." Claude'un kendi kod ortamında ürettiği dosya (Word, Excel) yalnız sohbetin indirme kartında durur; masa
o ortama erişemez. Çözüm: masa açıkken Claude dosyanın içeriğini al_masaya_yaz'ın ``dosyalar`` alanına yazar, dosyayı bu
modül kurar. Bilgisayardaki kurulum dosyayı Belgeler\\ArthurLegal klasörüne kaydeder (masada Aç, Klasörde göster, İndir);
uzak uç hiçbir şey saklamaz, masa indirirken içeriği yeniden kurdurur (``al_dosya`` islem=uret).

Biçimler: docx (Word), xlsx (Excel), csv, md, txt, html. Word ve HTML Markdown'dan kurulur (başlık, paragraf, madde
işaretli ve numaralı liste, tablo, alıntı, kod, yatay çizgi; **kalın**, *italik*, `kod`, [bağlantı](https://...)).
Excel ve CSV Markdown tablolarından (her tablo ayrı sayfa) ya da ayırıcılı satırlardan kurulur. PDF yoktur: Word
belgesi Word'de PDF olarak kaydedilir.

Yalnız standart kütüphane: uzak uç ve yerel kurulum aynı dosyayı kullanır (sunucu/esitle.py kopyalar).
"""
from __future__ import annotations

import base64
import csv
import io
import os
import re
import unicodedata
import zipfile
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple
from xml.sax.saxutils import escape

BICIMLER = {
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "csv": "text/csv",
    "md": "text/markdown",
    "txt": "text/plain",
    "html": "text/html",
}
BICIM_ADI = {"docx": "Word", "xlsx": "Excel", "csv": "CSV", "md": "Markdown", "txt": "Metin", "html": "HTML"}
# Claude'un yazabileceği öteki adlar.
BICIM_ESI = {"doc": "docx", "word": "docx", "xls": "xlsx", "excel": "xlsx", "markdown": "md", "metin": "txt",
             "text": "txt", "htm": "html"}
DOSYA_AZAMI = 5
ICERIK_SINIRI = 400_000      # karakter, dosya başına
BOYUT_SINIRI = 8_000_000     # bayt, kurulan dosya
AD_SINIRI = 80               # karakter, uzantısız
VARSAYILAN_AD = "ArthurLegal belge"
_YASAK = re.compile(r'[<>:"/\\|?*\x00-\x1f\x7f]')
_AYRILMIS = {"CON", "PRN", "AUX", "NUL"} | {"COM%d" % i for i in range(1, 10)} | {"LPT%d" % i for i in range(1, 10)}
_XML_DISI = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


class DosyaHatasi(ValueError):
    """Geçersiz dosya isteği; çağıran isError olarak döndürür (teslimde TeslimHatasi'na çevrilir)."""


# --------------------------------------------------------------------------- ad ve biçim
def bicim_bul(ad: Any, bicim: Any = None) -> str:
    """Açık biçim, yoksa adın uzantısı. Bilinmeyen biçim hatadır (PDF dahil: Word üretilir)."""
    b = str(bicim or "").strip().lower().lstrip(".")
    if not b:
        m = re.search(r"\.([A-Za-z0-9]{1,8})\s*$", str(ad or ""))
        b = m.group(1).lower() if m else "md"
    b = BICIM_ESI.get(b, b)
    if b not in BICIMLER:
        if b == "pdf":
            raise DosyaHatasi("PDF doğrudan üretilmiyor: dosyayı docx (Word) olarak yazın; Word'de PDF olarak kaydedilir.")
        raise DosyaHatasi("bicim şunlardan biri olmalı: %s." % ", ".join(BICIMLER))
    return b


def ad_temizle(ad: Any, bicim: str) -> str:
    """Dosya adı: klasör kısmı, yasak işaretler ve Windows'un ayrılmış adları atılır; uzantı biçimden gelir."""
    s = re.split(r"[\\/]", str(ad or ""))[-1]
    s = unicodedata.normalize("NFC", _YASAK.sub(" ", s))
    s = re.sub(r"\s+", " ", s).strip()
    kok, uzanti = os.path.splitext(s)
    if uzanti.lower().lstrip(".") in set(BICIMLER) | set(BICIM_ESI) | {"pdf"}:
        s = kok
    s = s.strip(" .")[:AD_SINIRI].strip(" .") or VARSAYILAN_AD
    if s.split(".")[0].upper() in _AYRILMIS:
        s = "_" + s
    return "%s.%s" % (s, bicim)


_ASCII = str.maketrans("İIıŞşĞğÜüÖöÇçÂâÎîÛûƏə", "IIiSsGgUuOoCcAaIiUuEe")


def ascii_ad(ad: str) -> str:
    """İndirme adresinde kullanılan ad (ev sahibi adı adresten okur): Türkçe harf sadeleşir, boşluk tire olur."""
    s = unicodedata.normalize("NFKD", ad.translate(_ASCII)).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", s).strip("-.")
    return s or "ArthurLegal-belge"


def dosyalari_duzenle(liste: Any) -> List[Dict[str, Any]]:
    """al_masaya_yaz'ın ``dosyalar`` alanı: [{ad, bicim, icerik}]. İçeriği olmayan öğe sohbetteki bir dosyanın adıdır
    (Claude onu kendi ortamında üretmiş, içeriğini yazamıyor): masa dosyanın sohbette olduğunu söyler."""
    if liste is None:
        return []
    if not isinstance(liste, list):
        raise DosyaHatasi("dosyalar bir liste olmalı: [{ad, bicim, icerik}].")
    if len(liste) > DOSYA_AZAMI:
        raise DosyaHatasi("Bir cevapta en çok %d dosya teslim edilir." % DOSYA_AZAMI)
    out: List[Dict[str, Any]] = []
    for i, o in enumerate(liste, 1):
        if not isinstance(o, dict):
            raise DosyaHatasi("dosyalar[%d] bir nesne olmalı: {ad, bicim, icerik}." % i)
        bicim = bicim_bul(o.get("ad"), o.get("bicim"))
        icerik = o.get("icerik")
        if icerik is not None and not isinstance(icerik, str):
            raise DosyaHatasi("dosyalar[%d].icerik metin olmalı." % i)
        if isinstance(icerik, str) and len(icerik) > ICERIK_SINIRI:
            raise DosyaHatasi("dosyalar[%d].icerik çok uzun (en çok %d karakter)." % (i, ICERIK_SINIRI))
        d: Dict[str, Any] = {"ad": ad_temizle(o.get("ad"), bicim), "bicim": bicim}
        if isinstance(icerik, str) and icerik.strip():
            d["icerik"] = icerik
        else:
            d["sohbette"] = True
        out.append(d)
    return out


def ozet(d: Dict[str, Any], veri: Optional[bytes] = None) -> Dict[str, Any]:
    """Masanın ve geçmişin tuttuğu bilgi: içerik yok."""
    o = {"ad": d["ad"], "bicim": d["bicim"]}
    if veri is not None:
        o["boyut"] = len(veri)
    if d.get("sohbette"):
        o["sohbette"] = True
    return o


# --------------------------------------------------------------------------- Markdown blokları
_BASLIK = re.compile(r"^ {0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
_CIZGI = re.compile(r"^ {0,3}([-*_])(\s*\1){2,}\s*$")
_LISTE = re.compile(r"^(\s*)([-*+•]|\d{1,3}[.)])\s+(.*)$")
_TABLO_AYIRAC = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
_ALINTI = re.compile(r"^ {0,3}>\s?(.*)$")
_KOD = re.compile(r"^ {0,3}(```|~~~)")


def _tablo_satiri(s: str) -> List[str]:
    s = s.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    hucreler, parca, kacis = [], "", False
    for ch in s:
        if kacis:
            parca += ch
            kacis = False
        elif ch == "\\":
            kacis = True
        elif ch == "|":
            hucreler.append(parca.strip())
            parca = ""
        else:
            parca += ch
    hucreler.append(parca.strip())
    return hucreler


def bloklar(md: str) -> List[Tuple]:
    """Markdown → bloklar: ("baslik", düzey, metin) ("paragraf", [satırlar]) ("liste", [(düzey, sirali, numara, metin)])
    ("tablo", [[hücre]]) ("alinti", [satırlar]) ("kod", metin) ("cizgi",)."""
    satirlar = str(md or "").replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out: List[Tuple] = []
    i, n = 0, len(satirlar)
    paragraf: List[str] = []

    def paragrafi_bitir() -> None:
        if paragraf:
            out.append(("paragraf", list(paragraf)))
            paragraf.clear()

    while i < n:
        s = satirlar[i]
        if not s.strip():
            paragrafi_bitir()
            i += 1
            continue
        m = _KOD.match(s)
        if m:
            paragrafi_bitir()
            cit, kod = m.group(1), []
            i += 1
            while i < n and not satirlar[i].strip().startswith(cit):
                kod.append(satirlar[i])
                i += 1
            out.append(("kod", "\n".join(kod)))
            i += 1
            continue
        m = _BASLIK.match(s)
        if m:
            paragrafi_bitir()
            out.append(("baslik", len(m.group(1)), m.group(2)))
            i += 1
            continue
        if _CIZGI.match(s):
            paragrafi_bitir()
            out.append(("cizgi",))
            i += 1
            continue
        if "|" in s and i + 1 < n and _TABLO_AYIRAC.match(satirlar[i + 1]) and "-" in satirlar[i + 1]:
            paragrafi_bitir()
            satir_listesi = [_tablo_satiri(s)]
            i += 2
            while i < n and satirlar[i].strip() and "|" in satirlar[i]:
                satir_listesi.append(_tablo_satiri(satirlar[i]))
                i += 1
            genislik = max(len(r) for r in satir_listesi)
            out.append(("tablo", [r + [""] * (genislik - len(r)) for r in satir_listesi]))
            continue
        if _ALINTI.match(s):
            paragrafi_bitir()
            alinti = []
            while i < n and _ALINTI.match(satirlar[i]):
                alinti.append(_ALINTI.match(satirlar[i]).group(1))
                i += 1
            out.append(("alinti", alinti))
            continue
        m = _LISTE.match(s)
        if m and not _CIZGI.match(s):
            paragrafi_bitir()
            ogeler: List[List[Any]] = []
            taban = len(m.group(1).expandtabs(4))
            while i < n:
                s = satirlar[i]
                m = _LISTE.match(s)
                if m and not _CIZGI.match(s):
                    girinti = len(m.group(1).expandtabs(4))
                    isaret = m.group(2)
                    sirali = isaret[0].isdigit()
                    ogeler.append([min(2, max(0, (girinti - taban) // 2)), sirali,
                                   int(isaret[:-1]) if sirali else 0, m.group(3)])
                    i += 1
                elif s.strip() and s[:1] in (" ", "\t") and ogeler:
                    ogeler[-1][3] += "\n" + s.strip()   # öğenin devamı
                    i += 1
                else:
                    break
            out.append(("liste", [tuple(o) for o in ogeler]))
            continue
        paragraf.append(s.strip())
        i += 1
    paragrafi_bitir()
    return out


# Satır içi: **kalın** __kalın__ *italik* _italik_ `kod` [metin](https://...). İç içe kalın/italik çözülür.
_SATIR_ICI = re.compile(
    r"(?P<kod>`[^`\n]+`)"
    r"|(?P<bag>\[(?P<bm>[^\]\n]+)\]\((?P<bu>https?://[^)\s]+)\))"
    r"|(?P<kalin>(\*\*|__)(?P<km>.+?)(?:\*\*|__))"
    r"|(?P<italik>(?<![\w*])\*(?!\s)(?P<im>[^*\n]+?)(?<!\s)\*(?![\w*])|(?<![\w_])_(?!\s)(?P<im2>[^_\n]+?)(?<!\s)_(?![\w_]))"
    r"|(?P<kacis>\\[\\`*_\[\]()#+\-.!|>])")


def satir_ici(metin: str, kalin: bool = False, italik: bool = False) -> List[Dict[str, Any]]:
    """Metin parçaları: [{metin, kalin, italik, kod, url}]."""
    out: List[Dict[str, Any]] = []
    yer = 0

    def duz(s: str) -> None:
        if s:
            out.append({"metin": s, "kalin": kalin, "italik": italik})

    for m in _SATIR_ICI.finditer(metin):
        duz(metin[yer:m.start()])
        if m.group("kod"):
            out.append({"metin": m.group("kod")[1:-1], "kalin": kalin, "italik": italik, "kod": True})
        elif m.group("bag"):
            for p in satir_ici(m.group("bm"), kalin, italik):
                p["url"] = m.group("bu")
                out.append(p)
        elif m.group("kalin"):
            out.extend(satir_ici(m.group("km"), True, italik))
        elif m.group("italik"):
            out.extend(satir_ici(m.group("im") or m.group("im2") or "", kalin, True))
        elif m.group("kacis"):
            duz(m.group("kacis")[1:])
        yer = m.end()
    duz(metin[yer:])
    return out


def duz_metin(metin: str) -> str:
    """Satır içi işaretleri atılmış metin (Excel hücresi, CSV)."""
    return "".join(p["metin"] for p in satir_ici(str(metin or ""))).replace("<br>", " ").strip()


# --------------------------------------------------------------------------- Word
_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
_YAZI = "Times New Roman"   # büro belgesi: Times New Roman 11 pt, siyah


def _x(s: Any) -> str:
    return escape(_XML_DISI.sub("", str(s or "")))


class _Word:
    def __init__(self) -> None:
        self.baglantilar: List[str] = []
        self.numaralar: List[Tuple[int, int]] = []   # (soyut numara, başlangıç); numId = sıra + 1

    def _bag(self, url: str) -> str:
        if url not in self.baglantilar:
            self.baglantilar.append(url)
        return "rIdL%d" % (self.baglantilar.index(url) + 1)

    def kosular(self, metin: str, kalin: bool = False) -> str:
        parcalar = []
        for satir_no, satir in enumerate(metin.split("\n")):
            if satir_no:
                parcalar.append("<w:r><w:br/></w:r>")
            for p in satir_ici(satir, kalin=kalin):
                # Word öğe sırasına bakar (rStyle, rFonts, b, i, sz); sıra bozulursa belge "okunamayan içerik" verir.
                rpr = ('<w:rStyle w:val="Hyperlink"/>' if p.get("url") else "") + (
                    '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/>' if p.get("kod") else "") + (
                    "<w:b/>" if p.get("kalin") else "") + ("<w:i/>" if p.get("italik") else "") + (
                    '<w:sz w:val="20"/>' if p.get("kod") else "")
                kosu = '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (
                    "<w:rPr>%s</w:rPr>" % rpr if rpr else "", _x(p["metin"]))
                if p.get("url"):
                    kosu = '<w:hyperlink r:id="%s" w:history="1">%s</w:hyperlink>' % (self._bag(p["url"]), kosu)
                parcalar.append(kosu)
        return "".join(parcalar)

    def paragraf(self, metin: str, stil: Optional[str] = None, ek_ppr: str = "", kalin: bool = False) -> str:
        ppr = ('<w:pStyle w:val="%s"/>' % stil if stil else "") + ek_ppr
        return "<w:p>%s%s</w:p>" % ("<w:pPr>%s</w:pPr>" % ppr if ppr else "", self.kosular(metin, kalin))

    def liste(self, ogeler: List[Tuple]) -> str:
        sirali_ilk = next((o for o in ogeler if o[1]), None)
        sirali_no = madde_no = 0
        if sirali_ilk:
            self.numaralar.append((1, max(1, sirali_ilk[2])))
            sirali_no = len(self.numaralar)
        if any(not o[1] for o in ogeler):
            self.numaralar.append((0, 1))
            madde_no = len(self.numaralar)
        out = []
        for duzey, sirali, _, metin in ogeler:
            ppr = '<w:numPr><w:ilvl w:val="%d"/><w:numId w:val="%d"/></w:numPr>' % (
                duzey, sirali_no if sirali else madde_no)
            out.append(self.paragraf(metin, "ListParagraph", ppr))
        return "".join(out)

    def tablo(self, satirlar: List[List[str]]) -> str:
        sutun = max(len(r) for r in satirlar)
        genislik = 9638 // max(1, sutun)   # A4 dikey metin alanı (2 cm kenar boşluğu)
        kenar = "".join('<w:%s w:val="single" w:sz="4" w:space="0" w:color="808080"/>' % y
                        for y in ("top", "left", "bottom", "right", "insideH", "insideV"))
        out = ['<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/><w:tblBorders>%s</w:tblBorders>'
               '<w:tblCellMar><w:left w:w="85" w:type="dxa"/><w:right w:w="85" w:type="dxa"/></w:tblCellMar>'
               "</w:tblPr><w:tblGrid>" % kenar + '<w:gridCol w:w="%d"/>' % genislik * sutun + "</w:tblGrid>"]
        for no, r in enumerate(satirlar):
            bas = no == 0
            out.append("<w:tr>%s" % ("<w:trPr><w:tblHeader/></w:trPr>" if bas else ""))
            for h in r:
                golge = '<w:shd w:val="clear" w:color="auto" w:fill="E7E9EE"/>' if bas else ""
                out.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>%s</w:tcPr>%s</w:tc>' % (
                    genislik, golge, self.paragraf(h.replace("<br>", "\n").replace("<br/>", "\n"), "Tablo", kalin=bas)))
            out.append("</w:tr>")
        out.append("</w:tbl>")
        return "".join(out) + self.paragraf("", "Tablo")   # Word iki tabloyu bitiştirmesin

    def govde(self, md: str) -> str:
        out = []
        for b in bloklar(md):
            tur = b[0]
            if tur == "baslik":
                out.append(self.paragraf(b[2], "Title" if b[1] == 1 else "Heading%d" % min(4, b[1] - 1)))
            elif tur == "paragraf":
                out.append(self.paragraf("\n".join(b[1])))
            elif tur == "liste":
                out.append(self.liste(b[1]))
            elif tur == "tablo":
                out.append(self.tablo(b[1]))
            elif tur == "alinti":
                out.append(self.paragraf("\n".join(b[1]), "Quote"))
            elif tur == "kod":
                for satir in b[1].split("\n") or [""]:
                    out.append('<w:p><w:pPr><w:pStyle w:val="Kod"/></w:pPr><w:r><w:t xml:space="preserve">%s</w:t>'
                               "</w:r></w:p>" % _x(satir))
            elif tur == "cizgi":
                out.append('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="808080"/>'
                           "</w:pBdr></w:pPr></w:p>")
        return "".join(out) or "<w:p/>"


def _stiller() -> str:
    def baslik(stil: str, ad: str, boyut: int, once: int, sonra: int) -> str:
        return ('<w:style w:type="paragraph" w:styleId="%s"><w:name w:val="%s"/><w:basedOn w:val="Normal"/>'
                '<w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="%d" w:after="%d"/>'
                '</w:pPr><w:rPr><w:b/><w:sz w:val="%d"/><w:szCs w:val="%d"/></w:rPr></w:style>'
                % (stil, ad, once, sonra, boyut, boyut))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:styles xmlns:w="%s"><w:docDefaults><w:rPrDefault><w:rPr>'
            '<w:rFonts w:ascii="{y}" w:hAnsi="{y}" w:cs="{y}" w:eastAsia="{y}"/><w:color w:val="000000"/>'
            '<w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="tr-TR"/></w:rPr></w:rPrDefault>'
            '<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault>'
            "</w:docDefaults>"
            '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>'
            % _W).replace("{y}", _YAZI) + (
            baslik("Title", "Title", 28, 0, 240) + baslik("Heading1", "heading 1", 26, 240, 120)
            + baslik("Heading2", "heading 2", 24, 200, 100) + baslik("Heading3", "heading 3", 22, 160, 80)
            + baslik("Heading4", "heading 4", 22, 120, 60)
            + '<w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/>'
              '<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:after="60"/></w:pPr></w:style>'
            + '<w:style w:type="paragraph" w:styleId="Quote"><w:name w:val="Quote"/><w:basedOn w:val="Normal"/>'
              '<w:qFormat/><w:pPr><w:pBdr><w:left w:val="single" w:sz="12" w:space="8" w:color="A0A4AE"/></w:pBdr>'
              '<w:ind w:left="567"/></w:pPr><w:rPr><w:i/></w:rPr></w:style>'
            + '<w:style w:type="paragraph" w:styleId="Kod"><w:name w:val="Kod"/><w:basedOn w:val="Normal"/>'
              '<w:pPr><w:shd w:val="clear" w:color="auto" w:fill="F2F3F5"/>'
              '<w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
              '<w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/><w:sz w:val="19"/></w:rPr></w:style>'
            + '<w:style w:type="paragraph" w:styleId="Tablo"><w:name w:val="Tablo"/><w:basedOn w:val="Normal"/>'
              '<w:pPr><w:spacing w:before="40" w:after="40" w:line="240" w:lineRule="auto"/></w:pPr>'
              '<w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr></w:style>'
            + '<w:style w:type="character" w:styleId="Hyperlink"><w:name w:val="Hyperlink"/>'
              '<w:rPr><w:color w:val="12285A"/><w:u w:val="single"/></w:rPr></w:style>'
            + "</w:styles>")


def _numaralar(w: _Word) -> str:
    def duzey(ilvl: int, bicim: str, metin: str) -> str:
        return ('<w:lvl w:ilvl="%d"><w:start w:val="1"/><w:numFmt w:val="%s"/><w:lvlText w:val="%s"/>'
                '<w:lvlJc w:val="left"/><w:pPr><w:ind w:left="%d" w:hanging="360"/></w:pPr></w:lvl>'
                % (ilvl, bicim, metin, 720 + 360 * ilvl))
    madde = "".join(duzey(i, "bullet", s) for i, s in enumerate(("•", "◦", "▪")))
    sira = "".join(duzey(i, f, t) for i, (f, t) in enumerate((("decimal", "%1."), ("lowerLetter", "%2)"),
                                                                 ("lowerRoman", "%3."))))
    nums = "".join('<w:num w:numId="%d"><w:abstractNumId w:val="%d"/>%s</w:num>' % (
        i + 1, soyut, '<w:lvlOverride w:ilvl="0"><w:startOverride w:val="%d"/></w:lvlOverride>' % bas if soyut else "")
        for i, (soyut, bas) in enumerate(w.numaralar))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:numbering xmlns:w="%s">'
            '<w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="hybridMultilevel"/>%s</w:abstractNum>'
            '<w:abstractNum w:abstractNumId="1"><w:multiLevelType w:val="hybridMultilevel"/>%s</w:abstractNum>%s'
            "</w:numbering>" % (_W, madde, sira, nums))


def _ozellikler(baslik: str) -> str:
    zaman = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            "<dc:title>%s</dc:title><dc:creator>ArthurLegal</dc:creator>"
            '<dcterms:created xsi:type="dcterms:W3CDTF">%s</dcterms:created>'
            '<dcterms:modified xsi:type="dcterms:W3CDTF">%s</dcterms:modified></cp:coreProperties>'
            % (_x(baslik), zaman, zaman))


def _zip(parcalar: List[Tuple[str, str]]) -> bytes:
    tampon = io.BytesIO()
    with zipfile.ZipFile(tampon, "w", zipfile.ZIP_DEFLATED) as z:
        for ad, metin in parcalar:
            z.writestr(ad, metin.encode("utf-8"))
    return tampon.getvalue()


def docx(md: str, baslik: str = "") -> bytes:
    """Markdown → Word (.docx). A4 dikey, 2 cm kenar boşluğu, Times New Roman 11 pt, siyah."""
    w = _Word()
    govde = w.govde(md)
    belge = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<w:document xmlns:w="%s" xmlns:r="%s"><w:body>%s'
             '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
             '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/>'
             "</w:sectPr></w:body></w:document>" % (_W, _R, govde))
    iliskiler = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                 '<Relationship Id="rIdS" Type="%s/styles" Target="styles.xml"/>'
                 '<Relationship Id="rIdN" Type="%s/numbering" Target="numbering.xml"/>' % (_R, _R)
                 + "".join('<Relationship Id="rIdL%d" Type="%s/hyperlink" Target="%s" TargetMode="External"/>'
                           % (i + 1, _R, _x(u)) for i, u in enumerate(w.baglantilar))
                 + "</Relationships>")
    turler = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
              '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
              '<Default Extension="xml" ContentType="application/xml"/>'
              '<Override PartName="/word/document.xml" '
              'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
              '<Override PartName="/word/styles.xml" '
              'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
              '<Override PartName="/word/numbering.xml" '
              'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
              '<Override PartName="/docProps/core.xml" '
              'ContentType="application/vnd.openxmlformats-package.core-properties+xml"/></Types>')
    kok = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
           '<Relationship Id="rId1" Type="%s/officeDocument" Target="word/document.xml"/>'
           '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/'
           'core-properties" Target="docProps/core.xml"/></Relationships>' % _R)
    return _zip([("[Content_Types].xml", turler), ("_rels/.rels", kok), ("word/document.xml", belge),
                 ("word/_rels/document.xml.rels", iliskiler), ("word/styles.xml", _stiller()),
                 ("word/numbering.xml", _numaralar(w)), ("docProps/core.xml", _ozellikler(baslik))])


# --------------------------------------------------------------------------- tablolar (Excel, CSV)
def tablolar(icerik: str) -> List[Tuple[str, List[List[str]]]]:
    """İçerikteki tablolar, adlarıyla (tablodan önceki başlık). Markdown tablosu yoksa ayırıcılı satırlar (; sekme ,)
    tek tablo olur; ayırıcı da yoksa her satır tek hücre."""
    out: List[Tuple[str, List[List[str]]]] = []
    son_baslik = ""
    for b in bloklar(icerik):
        if b[0] == "baslik":
            son_baslik = duz_metin(b[2])
        elif b[0] == "tablo":
            out.append((son_baslik, [[duz_metin(h) for h in r] for r in b[1]]))
            son_baslik = ""
    if out:
        return out
    satirlar = [s for s in str(icerik or "").replace("\r\n", "\n").split("\n") if s.strip()]
    for ayirac in (";", "\t", ","):
        if satirlar and all(ayirac in s for s in satirlar):
            return [("", [list(r) for r in csv.reader(satirlar, delimiter=ayirac)])]
    return [("", [[duz_metin(s)] for s in satirlar])]


_TAM = re.compile(r"^-?(0|[1-9]\d{0,14})$")
_TR_ONDALIK = re.compile(r"^-?\d{1,3}(\.\d{3})*(,\d+)?$|^-?\d+,\d+$")
_EN_ONDALIK = re.compile(r"^-?\d+\.\d{1,2}$|^-?\d+\.\d{4,}$")


def sayi(s: str) -> Optional[str]:
    """Excel'de sayı olarak yazılacak değer (nokta ondalıklı metin) ya da None. Türkçe yazım (1.234,56) tanınır;
    "1.500" binlik sayılır. Para birimi, yüzde ya da başka işaret taşıyan değer metin kalır."""
    s = s.strip()
    if _TAM.match(s):
        return s
    if _TR_ONDALIK.match(s) and ("," in s or "." in s):
        return s.replace(".", "").replace(",", ".")
    if _EN_ONDALIK.match(s):
        return s
    return None


def _sutun_adi(i: int) -> str:
    ad = ""
    i += 1
    while i:
        i, k = divmod(i - 1, 26)
        ad = chr(65 + k) + ad
    return ad


def _sayfa_adi(ad: str, no: int, kullanilan: set) -> str:
    ad = re.sub(r"[\[\]:*?/\\]", " ", ad).strip()[:28].strip() or "Tablo %d" % no
    aday, k = ad, 2
    while aday.lower() in kullanilan:
        aday = "%s (%d)" % (ad[:24], k)
        k += 1
    kullanilan.add(aday.lower())
    return aday


def xlsx(icerik: str, baslik: str = "") -> bytes:
    """Tablolar → Excel (.xlsx): her tablo bir sayfa, ilk satır kalın ve sabit, sütun genişliği içeriğe göre."""
    sayfalar, kullanilan = [], set()
    for no, (ad, satirlar) in enumerate(tablolar(icerik), 1):
        sayfalar.append((_sayfa_adi(ad, no, kullanilan), satirlar))
    xml_sayfalar = []
    for _, satirlar in sayfalar:
        sutun = max((len(r) for r in satirlar), default=1)
        genislik = [min(60, max(8, max((len(r[c]) if c < len(r) else 0) for r in satirlar) + 2))
                    for c in range(sutun)] if satirlar else [10]
        rows = []
        for r_no, r in enumerate(satirlar, 1):
            hucreler = []
            for c, deger in enumerate(r):
                ref = "%s%d" % (_sutun_adi(c), r_no)
                stil = ' s="1"' if r_no == 1 else ""
                v = None if r_no == 1 else sayi(deger)
                if v is not None:
                    hucreler.append('<c r="%s"%s><v>%s</v></c>' % (ref, stil, v))
                elif deger:
                    hucreler.append('<c r="%s"%s t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>'
                                    % (ref, stil, _x(deger)))
            rows.append('<row r="%d">%s</row>' % (r_no, "".join(hucreler)))
        dondur = ('<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" '
                  'state="frozen"/></sheetView></sheetViews>' if len(satirlar) > 1 else "")
        xml_sayfalar.append(
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">%s<cols>%s</cols>'
            "<sheetData>%s</sheetData></worksheet>" % (
                dondur, "".join('<col min="%d" max="%d" width="%d" customWidth="1"/>' % (i + 1, i + 1, g)
                                for i, g in enumerate(genislik)), "".join(rows)))
    kitap = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="%s"><sheets>%s'
             "</sheets></workbook>" % (_R, "".join('<sheet name="%s" sheetId="%d" r:id="rId%d"/>' % (_x(ad), i, i)
                                                   for i, (ad, _) in enumerate(sayfalar, 1))))
    kitap_iliski = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">%s'
                    '<Relationship Id="rIdS" Type="%s/styles" Target="styles.xml"/></Relationships>' % (
                        "".join('<Relationship Id="rId%d" Type="%s/worksheet" Target="worksheets/sheet%d.xml"/>'
                                % (i, _R, i) for i in range(1, len(sayfalar) + 1)), _R))
    stiller = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
               '<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font>'
               '<font><b/><sz val="11"/><name val="Calibri"/></font></fonts>'
               '<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/>'
               '</fill><fill><patternFill patternType="solid"><fgColor rgb="FFE7E9EE"/><bgColor indexed="64"/>'
               "</patternFill></fill></fills>"
               '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
               '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
               '<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
               '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/></cellXfs>'
               '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>')
    turler = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
              '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
              '<Default Extension="xml" ContentType="application/xml"/>'
              '<Override PartName="/xl/workbook.xml" '
              'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
              '<Override PartName="/xl/styles.xml" '
              'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
              + "".join('<Override PartName="/xl/worksheets/sheet%d.xml" '
                        'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' % i
                        for i in range(1, len(sayfalar) + 1))
              + '<Override PartName="/docProps/core.xml" '
                'ContentType="application/vnd.openxmlformats-package.core-properties+xml"/></Types>')
    kok = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
           '<Relationship Id="rId1" Type="%s/officeDocument" Target="xl/workbook.xml"/>'
           '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/'
           'core-properties" Target="docProps/core.xml"/></Relationships>' % _R)
    return _zip([("[Content_Types].xml", turler), ("_rels/.rels", kok), ("xl/workbook.xml", kitap),
                 ("xl/_rels/workbook.xml.rels", kitap_iliski), ("xl/styles.xml", stiller)]
                + [("xl/worksheets/sheet%d.xml" % i, x) for i, x in enumerate(xml_sayfalar, 1)]
                + [("docProps/core.xml", _ozellikler(baslik))])


def csv_bayt(icerik: str) -> bytes:
    """Noktalı virgüllü CSV (Türkçe Excel bunu bekler), UTF-8 BOM'lu. Markdown tablosu yoksa içerik olduğu gibi."""
    tablo_listesi = [t for _, t in tablolar(icerik)] if "|" in str(icerik or "") else []
    if not any(len(r) > 1 for t in tablo_listesi for r in t):
        metin = str(icerik or "").replace("\r\n", "\n").replace("\n", "\r\n")
        return ("﻿" + metin).encode("utf-8")
    tampon = io.StringIO()
    w = csv.writer(tampon, delimiter=";", lineterminator="\r\n")
    for no, t in enumerate(tablo_listesi):
        if no:
            w.writerow([])
        w.writerows(t)
    return ("﻿" + tampon.getvalue()).encode("utf-8")


# --------------------------------------------------------------------------- HTML
def _html_satir(metin: str) -> str:
    out = []
    for satir_no, satir in enumerate(metin.split("\n")):
        if satir_no:
            out.append("<br>")
        for p in satir_ici(satir):
            h = escape(p["metin"])
            if p.get("kod"):
                h = "<code>%s</code>" % h
            if p.get("italik"):
                h = "<em>%s</em>" % h
            if p.get("kalin"):
                h = "<strong>%s</strong>" % h
            if p.get("url"):
                h = '<a href="%s">%s</a>' % (escape(p["url"], {'"': "&quot;"}), h)
            out.append(h)
    return "".join(out)


def html(md: str, baslik: str = "") -> bytes:
    """Markdown → tek dosyalık HTML (yazdırılabilir; tarayıcıda PDF olarak da kaydedilir). Betik yok."""
    govde = []
    for b in bloklar(md):
        tur = b[0]
        if tur == "baslik":
            govde.append("<h%d>%s</h%d>" % (b[1], _html_satir(b[2]), b[1]))
        elif tur == "paragraf":
            govde.append("<p>%s</p>" % _html_satir("\n".join(b[1])))
        elif tur == "liste":
            yigin: List[str] = []
            for duzey, sirali, numara, metin in b[1]:
                etiket = "ol" if sirali else "ul"
                while len(yigin) > duzey + 1:
                    govde.append("</%s>" % yigin.pop())
                while len(yigin) < duzey + 1:
                    baslangic = ' start="%d"' % numara if sirali and numara > 1 and not yigin else ""
                    govde.append("<%s%s>" % (etiket, baslangic))
                    yigin.append(etiket)
                govde.append("<li>%s</li>" % _html_satir(metin))
            while yigin:
                govde.append("</%s>" % yigin.pop())
        elif tur == "tablo":
            satirlar = b[1]
            govde.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (
                "".join("<th>%s</th>" % _html_satir(h) for h in satirlar[0]),
                "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _html_satir(h) for h in r) for r in satirlar[1:])))
        elif tur == "alinti":
            govde.append("<blockquote>%s</blockquote>" % _html_satir("\n".join(b[1])))
        elif tur == "kod":
            govde.append("<pre><code>%s</code></pre>" % escape(b[1]))
        elif tur == "cizgi":
            govde.append("<hr>")
    sayfa = ('<!doctype html>\n<html lang="tr"><head><meta charset="utf-8">'
             '<meta name="viewport" content="width=device-width, initial-scale=1"><title>%s</title><style>'
             "body{font:11pt/1.5 'Times New Roman',Times,serif;color:#000;background:#fff;max-width:46rem;"
             "margin:2rem auto;padding:0 1rem}h1{font-size:14pt}h2{font-size:13pt}h3,h4,h5,h6{font-size:12pt}"
             "table{border-collapse:collapse;width:100%%;margin:.5rem 0}th,td{border:1px solid #808080;"
             "padding:.25rem .4rem;text-align:left;vertical-align:top}th{background:#e7e9ee}"
             "blockquote{margin:.5rem 0;padding-left:.8rem;border-left:3px solid #a0a4ae;font-style:italic}"
             "pre{background:#f2f3f5;padding:.5rem;overflow:auto}a{color:#12285a}"
             "@media print{body{margin:0;max-width:none}}</style></head><body>\n%s\n</body></html>\n"
             % (escape(baslik or "ArthurLegal"), "\n".join(govde)))
    return sayfa.encode("utf-8")


# --------------------------------------------------------------------------- kur ve kaydet
def uret(bicim: str, icerik: str, baslik: str = "") -> bytes:
    """Dosyanın baytları. Sınırı aşan dosya hatadır."""
    bicim = bicim_bul(None, bicim)
    icerik = str(icerik or "")
    if len(icerik) > ICERIK_SINIRI:
        raise DosyaHatasi("İçerik çok uzun (en çok %d karakter)." % ICERIK_SINIRI)
    if bicim == "docx":
        veri = docx(icerik, baslik)
    elif bicim == "xlsx":
        veri = xlsx(icerik, baslik)
    elif bicim == "csv":
        veri = csv_bayt(icerik)
    elif bicim == "html":
        veri = html(icerik, baslik)
    else:   # md, txt: olduğu gibi, UTF-8
        veri = icerik.encode("utf-8")
    if len(veri) > BOYUT_SINIRI:
        raise DosyaHatasi("Dosya çok büyük (%d bayt; en çok %d)." % (len(veri), BOYUT_SINIRI))
    return veri


def indirme(ad: str, bicim: str, veri: bytes) -> Dict[str, Any]:
    """Masanın indirme isteği için: base64 veri, MIME ve adreste kullanılacak ASCII ad."""
    return {"ad": ad, "indirme_adi": ascii_ad(ad), "bicim": bicim, "mime": BICIMLER[bicim], "boyut": len(veri),
            "veri": base64.b64encode(veri).decode("ascii")}


def bos_ad(klasor: str, ad: str) -> str:
    """Klasörde olmayan ad: "Dilekçe.docx" varsa "Dilekçe (2).docx". Var olan dosyanın üzerine yazılmaz."""
    kok, uzanti = os.path.splitext(ad)
    aday, k = ad, 2
    while os.path.exists(os.path.join(klasor, aday)):
        aday = "%s (%d)%s" % (kok, k, uzanti)
        k += 1
    return aday


def kaydet(dosyalar: List[Dict[str, Any]], klasor: str) -> List[Dict[str, Any]]:
    """Teslimdeki dosyaları klasöre yazar; masanın ve geçmişin tuttuğu bilgiyi döndürür ({ad, bicim, boyut, kayit, yol}).
    Sohbetteki dosya (içeriksiz) yazılmaz, yalnız adı döner. Yazma geçici dosya + değiştirme ile yapılır."""
    out: List[Dict[str, Any]] = []
    for d in dosyalar:
        if d.get("sohbette") or not d.get("icerik"):
            out.append(ozet(d))
            continue
        veri = uret(d["bicim"], d["icerik"], os.path.splitext(d["ad"])[0])
        os.makedirs(klasor, exist_ok=True)
        ad = bos_ad(klasor, d["ad"])
        yol = os.path.join(klasor, ad)
        gecici = yol + ".yaziliyor"
        with open(gecici, "wb") as fh:
            fh.write(veri)
        os.replace(gecici, yol)
        o = ozet(d, veri)
        o.update(ad=ad, kayit=ad, yol=yol)
        out.append(o)
    return out


def klasordeki(klasor: str, ad: Any) -> str:
    """Masanın açmak ya da indirmek istediği dosyanın yolu: yalnız bu klasörün içinde, bilinen uzantıyla ve var olan
    bir dosya. Klasör işareti, üst klasör ya da başka uzantı hatadır (masa başka dosya açtıramaz)."""
    ad = str(ad or "")
    if not ad or ad != os.path.basename(ad) or "/" in ad or "\\" in ad or ad in (".", "..") or ad.startswith("."):
        raise DosyaHatasi("Geçersiz dosya adı.")
    if os.path.splitext(ad)[1].lower().lstrip(".") not in BICIMLER:
        raise DosyaHatasi("Bu dosya türü masadan açılmaz.")
    yol = os.path.join(klasor, ad)
    if not os.path.isfile(yol) or os.path.islink(yol):
        raise DosyaHatasi("Dosya bulunamadı: taşınmış ya da silinmiş olabilir.")
    return yol
