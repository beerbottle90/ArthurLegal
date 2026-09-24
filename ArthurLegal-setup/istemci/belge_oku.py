"""Bilgisayardaki belgeyi Markdown olarak okur — `arthurlegal_belge_oku` aracının motoru.

Neden ayrı bir okuyucu: sözleşme müzakeresinde asıl içerik karşı tarafın redline'ıdır. Yaygın
dönüştürücüler (markitdown/mammoth, varsayılan pandoc) DOCX'i "tüm değişiklikleri kabul et" görünümüyle
okur: silinen metin ve yorumlar sessizce kaybolur. Bu modül izlenen değişiklikleri ve yorumları
CriticMarkup ile korur:

    {++eklenen++}  {--silinen--}  {==işaretli metin==}{>>Yazar tarih: yorum<<}

Ölçüm (arthurlegal-ai-roundtable altın seti, 2026-09-23): redline DOCX'te markitdown silinen metni ve
yorumu kaybetti; bu okuyucuyla model "önceki süre 30 gündü, karşı taraf faizi %12'ye indirmek istiyor"
diyebildi. Taranmış PDF'te markitdown "(cid:N)" çöpü üretti; burada metin uydurulmaz.

Yol seçimi:
  DOCX                      → bu modül (yalnız standart kütüphane; gömülü Python'da çalışır)
  PDF / diğerleri           → PATH'te markitdown varsa o; taranmış çıktı saptanırsa uydurmaz
  PDF, markitdown yoksa     → "PDF'i sohbete doğrudan ekleyin" (Claude Desktop PDF'i kendisi okur)
  HTML, markitdown yoksa    → standart kütüphaneyle düz metin

Güvenlik: yalnız kullanıcı klasörü (%USERPROFILE%) altındaki, belge uzantılı dosyalar okunur.
Günlüğe belge içeriği yazılmaz.
"""
from __future__ import annotations

import html.parser
import os
import re
import shutil
import subprocess
import tempfile
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

AZAMI = 60000
UZANTILAR = {".docx", ".pdf", ".htm", ".html", ".txt", ".md", ".xlsx", ".pptx", ".csv"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ISARET = {"ins": ("{++", "++}"), "del": ("{--", "--}")}


class BelgeHatasi(Exception):
    pass


# ---------------------------------------------------------------------------- yol ve güvenlik

def yol_coz(girdi: str) -> Path:
    girdi = (girdi or "").strip().strip('"')
    if not girdi:
        raise BelgeHatasi("yol verilmedi")
    if girdi.lower().startswith("file:"):
        girdi = urllib.request.url2pathname(urllib.parse.urlparse(girdi).path)
    yol = Path(os.path.expandvars(girdi)).expanduser().resolve()
    kok = Path(os.environ.get("USERPROFILE") or Path.home()).resolve()
    if kok not in yol.parents:
        raise BelgeHatasi(f"yalnız kullanıcı klasörü ({kok}) altındaki belgeler okunur")
    if yol.suffix.lower() not in UZANTILAR:
        raise BelgeHatasi(f"desteklenmeyen biçim: {yol.suffix or '(uzantısız)'} — {', '.join(sorted(UZANTILAR))}")
    if not yol.is_file():
        raise BelgeHatasi(f"dosya yok: {yol}")
    return yol


# ---------------------------------------------------------------------------- DOCX (redline korumalı)

def _yerel(etiket: str) -> str:
    return etiket.rsplit("}", 1)[-1]


def _xml(z: zipfile.ZipFile, ad: str) -> ET.Element | None:
    try:
        return ET.fromstring(z.read(ad))
    except KeyError:
        return None


class _Docx:
    def __init__(self, z: zipfile.ZipFile):
        self.baslik = {}
        stiller = _xml(z, "word/styles.xml")
        for s in (stiller.iter(W + "style") if stiller is not None else []):
            ad = s.find(W + "name")
            m = re.match(r"heading\s*(\d)", (ad.get(W + "val") if ad is not None else "") or "", re.I)
            if m:  # yerleşik stil adı Türkçe Word'de de "heading N"dir
                self.baslik[s.get(W + "styleId")] = int(m.group(1))
        self.yorum = {}
        yorumlar = _xml(z, "word/comments.xml")
        for y in (yorumlar.iter(W + "comment") if yorumlar is not None else []):
            metin = " ".join("".join(t.text or "" for t in p.iter(W + "t")) for p in y.iter(W + "p")).strip()
            tarih = (y.get(W + "date") or "")[:10]
            self.yorum[y.get(W + "id")] = f"{y.get(W + 'author') or '?'}{' ' + tarih if tarih else ''}: {metin}"
        self.yazilan = set()
        self.sayac = {"ekleme": 0, "silme": 0, "yorum": 0}
        self.yazarlar = set()

    def _yorum_isareti(self, yid):
        if not yid or yid in self.yazilan or yid not in self.yorum:
            return ""
        self.yazilan.add(yid)
        self.sayac["yorum"] += 1
        return "{>>" + self.yorum[yid] + "<<}"

    def _run(self, r):
        parca = []
        for c in r:
            ad = _yerel(c.tag)
            if ad in ("t", "delText"):
                parca.append(c.text or "")
            elif ad == "tab":
                parca.append("\t")
            elif ad in ("br", "cr"):
                parca.append("\n")
            elif ad == "noBreakHyphen":
                parca.append("-")
            elif ad == "commentReference":
                parca.append(self._yorum_isareti(c.get(W + "id")))
        return "".join(parca)

    def _gez(self, el, cikti):
        for c in el:
            ad = _yerel(c.tag)
            if ad == "r":
                cikti.append(self._run(c))
            elif ad in ("ins", "moveTo", "del", "moveFrom"):
                tur = "ins" if ad in ("ins", "moveTo") else "del"
                self.sayac["ekleme" if tur == "ins" else "silme"] += 1
                if c.get(W + "author"):
                    self.yazarlar.add(c.get(W + "author"))
                ic = []
                self._gez(c, ic)
                if "".join(ic):
                    cikti.append(ISARET[tur][0] + "".join(ic) + ISARET[tur][1])
            elif ad == "commentRangeStart":
                cikti.append("{==")
            elif ad == "commentRangeEnd":
                cikti.append("==}" + self._yorum_isareti(c.get(W + "id")))
            elif ad in ("hyperlink", "smartTag", "fldSimple", "sdt", "sdtContent", "customXml"):
                self._gez(c, cikti)

    def paragraf(self, p):
        cikti = []
        self._gez(p, cikti)
        metin = "".join(cikti).strip()
        if not metin:
            return ""
        ppr = p.find(W + "pPr")
        stil = ppr.find(W + "pStyle") if ppr is not None else None
        duzey = self.baslik.get(stil.get(W + "val")) if stil is not None else None
        if duzey:
            return "#" * min(duzey, 6) + " " + metin
        if ppr is not None and ppr.find(W + "numPr") is not None:
            return "- " + metin
        return metin

    def tablo(self, tbl):
        satirlar = []
        for tr in tbl.findall(W + "tr"):
            hucre = [" <br> ".join(filter(None, (self.paragraf(p) for p in tc.iter(W + "p")))).replace("|", "\\|")
                     for tc in tr.findall(W + "tc")]
            satirlar.append("| " + " | ".join(hucre) + " |")
        if not satirlar:
            return ""
        return "\n".join([satirlar[0], "|" + " --- |" * (satirlar[0].count(" | ") + 1)] + satirlar[1:])

    def govde(self, kok):
        bloklar = []
        body = kok.find(W + "body")
        for c in (body if body is not None else []):
            ad = _yerel(c.tag)
            if ad == "p":
                bloklar.append(self.paragraf(c))
            elif ad == "tbl":
                bloklar.append(self.tablo(c))
            elif ad == "sdt" and c.find(W + "sdtContent") is not None:
                bloklar += [self.paragraf(p) for p in c.find(W + "sdtContent").findall(W + "p")]
        return [b for b in bloklar if b]


def docx_md(yol: Path) -> str:
    try:
        with zipfile.ZipFile(yol) as z:
            kok = _xml(z, "word/document.xml")
            if kok is None:
                raise BelgeHatasi(f"DOCX değil ya da bozuk: {yol.name}")
            d = _Docx(z)
            bloklar = d.govde(kok)
    except (zipfile.BadZipFile, ET.ParseError) as e:
        raise BelgeHatasi(f"DOCX okunamadı ({yol.name}): {e}") from e
    s = d.sayac
    if not any(s.values()):
        return "\n\n".join(bloklar) + "\n"
    ozet = (f"> **İzlenen değişiklikler:** {s['ekleme']} ekleme, {s['silme']} silme, {s['yorum']} yorum"
            f"{' (yazarlar: ' + ', '.join(sorted(d.yazarlar)) + ')' if d.yazarlar else ''}. Gösterim CriticMarkup: "
            "{++eklenen++} {--silinen--} {==işaretli metin==}{>>yorum<<}. Silinen metin ÖNERİLEN metinde yoktur; "
            "müzakere geçmişi olarak okuyun.")
    return ozet + "\n\n" + "\n\n".join(bloklar) + "\n"


# ---------------------------------------------------------------------------- diğer biçimler

class _HtmlMetin(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.parca, self._atla = [], 0

    def handle_starttag(self, tag, attrs):
        self._atla += tag in ("script", "style")

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._atla:
            self._atla -= 1

    def handle_data(self, data):
        if not self._atla and data.strip():
            self.parca.append(data.strip())


def _html_metin(yol: Path) -> str:
    ham = yol.read_bytes()
    m = re.search(rb'charset=["\']?([\w-]+)', ham[:2048], re.I)
    kod = (m.group(1).decode("ascii") if m else "utf-8").lower().replace("windows-1254", "cp1254")
    a = _HtmlMetin()
    a.feed(ham.decode(kod, errors="replace"))
    return "\n".join(a.parca) + "\n"


def _markitdown(yol: Path) -> str | None:
    komut = shutil.which("markitdown")
    if not komut:
        return None
    with tempfile.TemporaryDirectory() as gecici:
        hedef = Path(gecici) / "cikti.md"
        r = subprocess.run([komut, str(yol), "-o", str(hedef)], capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=600, env={**os.environ, "PYTHONUTF8": "1"})
        if r.returncode != 0 or not hedef.exists():
            raise BelgeHatasi(f"markitdown başarısız ({yol.name})")
        return hedef.read_text(encoding="utf-8", errors="replace")


def _okunamaz(md: str) -> bool:
    glif = len(re.findall(r"\(cid:\d+\)", md))
    harf = sum(ch.isalpha() for ch in re.sub(r"\(cid:\d+\)", "", md))
    return glif > 20 or harf < 200


def oku(girdi: str, baslangic: int = 0) -> str:
    """Belgeyi Markdown olarak döndürür; AZAMI karakterden uzunsa `baslangic` ile parça parça."""
    yol = yol_coz(girdi)
    uzanti = yol.suffix.lower()
    if uzanti == ".docx":
        md = docx_md(yol)
    elif uzanti in (".txt", ".md", ".csv"):
        md = yol.read_text(encoding="utf-8", errors="replace")
    else:
        md = _markitdown(yol)
        if md is None:
            if uzanti == ".pdf":
                return ("Bu kurulumda PDF dönüştürücü yok. PDF'i sohbete doğrudan ekleyin: Claude PDF'i "
                        "(taranmış sayfalar dâhil) kendisi okur. Metin UYDURULMADI.")
            if uzanti in (".htm", ".html"):
                md = _html_metin(yol)
            else:
                raise BelgeHatasi(f"{uzanti} için markitdown gerekir (uv tool install 'markitdown[all]')")
        elif uzanti == ".pdf" and _okunamaz(md):
            return ("OKUNAMAZ PDF: metin katmanı yok ya da bozuk (taranmış görüntü). Metin UYDURULMADI. "
                    "PDF'i sohbete doğrudan ekleyin; Claude sayfa görüntüsünü okuyabilir.")
    baslangic = max(0, int(baslangic or 0))
    parca = md[baslangic:baslangic + AZAMI]
    if baslangic + AZAMI < len(md):
        parca += f"\n\n[… {len(md) - baslangic - AZAMI} karakter daha var: baslangic={baslangic + AZAMI} ile devam edin]"
    return parca
