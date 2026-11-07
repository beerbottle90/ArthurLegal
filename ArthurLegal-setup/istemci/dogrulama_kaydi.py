"""Doğrulama kaydı (`al_dogrulama_kaydi`): ArthurLegal Masası'nda hangi madde atfının ne zaman, hangi sonuçla ve hangi
resmî bağlantıyla teyit edildiğini bu bilgisayardaki masa geçmişinden okur; Markdown, CSV ya da Word (.docx) dosyası
olarak yazar. Avukat dökümü dosyasına koyar ya da büronun yapay zekâ politikasındaki kullanım kaydına ekler.

Kaynak, masa geçmişidir (al_arayuz.Gecmis: veri/masa-gecmisi, kayıt başına bir JSON). Üç kayıt türü atıf taşır:
- "atif": Mevzuat ekranındaki atıf teyidi. anlik.satirlar = [{kanun, madde, ok, baslik, citation, hata}].
- "cevap": masaya teslim edilen cevap. Masa cevaptaki atıfları kendisi teyit eder (anlik.teyit.satirlar, aynı biçim);
  Claude'un dayandığı kaynaklar anlik.kaynaklar = [{baslik, atif, url}].
- "madde": Mevzuat ekranında getirilen madde. anlik.veri = tr_mevzuat_madde_getir yanıtı (law.source_url, items).

Bağlantı uydurulmaz. Bir satırın bağlantısı sırasıyla: aynı kanunun madde kaydındaki law.source_url, cevabın kaynak
listesinde aynı atfı taşıyan https bağlantısı. İkisi de yoksa alan boş kalır; belgenin notu resmî giriş sayfasını
gösterir. Uzak masa (claude.ai, telefon) geçmişi o cihazın tarayıcısında tutar, bu bilgisayardan okunmaz.

Yalnız okur: masa geçmişine dokunmaz. Kayıt yoksa dosya yazmaz. Yalnız standart kütüphane.
"""
from __future__ import annotations

import csv
import io
import json
import os
import re
import zipfile
from datetime import date, datetime
from typing import Any, Dict, List, Optional, Tuple
from xml.sax.saxutils import escape

VARSAYILAN_AD = "ArthurLegal-Dogrulama-Kaydi"
BICIMLER = ("md", "csv", "docx")
RESMI_GIRIS = "https://www.mevzuat.gov.tr/"
_KIMLIK = re.compile(r"^\d{8}-\d{6}-[0-9a-f]{6}$")
_KATLA = str.maketrans("İIıŞşĞğÜüÖöÇçÂâÎîÛû", "iiissgguuooccaaiiuu")
_XML_DISI = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
KAYNAK_ADI = {"atif": "Atıf teyidi", "cevap": "Claude cevabı (masa teyidi)", "madde": "Madde getirildi"}

# Sütunlar: (anahtar, başlık). CSV hepsini, Markdown ve Word ilk altısını yazar.
SUTUNLAR = (
    ("tarih_saat", "Tarih ve saat"),
    ("atif", "Atıf"),
    ("sonuc", "Sonuç"),
    ("madde_basligi", "Madde başlığı"),
    ("baglanti", "Resmî bağlantı"),
    ("is", "İş"),
    ("zaman", "Zaman (ISO)"),
    ("kanun", "Kanun no"),
    ("madde", "Madde"),
    ("kaynak", "Kaynak"),
    ("konu", "Konu"),
    ("kayit_id", "Kayıt"),
)
BELGE_SUTUNLARI = SUTUNLAR[:6]


class KayitHatasi(ValueError):
    """Geçersiz istek; çağıran isError olarak döndürür."""


def arac_tanimi() -> Dict[str, Any]:
    return {
        "name": "al_dogrulama_kaydi",
        "title": "ArthurLegal doğrulama kaydı",
        "description": (
            "ArthurLegal Masası'nda yapılan madde atfı teyitlerinin kaydını (hangi atıf, ne zaman, sonuç, resmî metin "
            "bağlantısı) bu bilgisayardaki masa geçmişinden okur ve Markdown (md), CSV ya da Word (docx) dosyası olarak "
            "yazar; dosyanın yolunu döndürür. Kullanıcı doğrulama kaydı, atıf teyit dökümü ya da yapay zekâ "
            "politikasındaki kullanım kaydı için döküm isterse çağırın. Yalnız bu bilgisayardaki masanın geçmişini "
            "okur (90 gün); web ya da telefondaki masanın geçmişi o cihazdadır. Bağlantısı kayıtta olmayan satırda "
            "bağlantı boş kalır, uydurulmaz."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "bicim": {"type": "string", "enum": list(BICIMLER), "default": "md",
                          "description": "md (Markdown), csv (Excel için noktalı virgüllü) ya da docx (Word)."},
                "baslangic": {"type": "string", "description": "İlk gün, YYYY-AA-GG (dahil). Boşsa geçmişin başı."},
                "bitis": {"type": "string", "description": "Son gün, YYYY-AA-GG (dahil). Boşsa bugün."},
                "ara": {"type": "string", "description": "Yalnız atfında, kanun no'sunda, başlığında ya da konusunda "
                                                         "bu ifade geçen satırlar (ör. 6098, TBK, kira)."},
            },
        },
        "annotations": {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": False,
                        "openWorldHint": False},
    }


# ---------------------------------------------------------------------------- okuma

def kayitlari_oku(klasor: str) -> List[Dict[str, Any]]:
    """Masa geçmişindeki kayıtlar, eskiden yeniye. Okunamayan dosya atlanır; klasör yoksa boş liste."""
    try:
        adlar = sorted(a for a in os.listdir(klasor) if a.endswith(".json") and _KIMLIK.match(a[:-5]))
    except OSError:
        return []
    kayitlar = []
    for ad in adlar:
        try:
            with open(os.path.join(klasor, ad), encoding="utf-8") as fh:
                k = json.load(fh)
        except (OSError, ValueError):
            continue
        if isinstance(k, dict) and _KIMLIK.match(str(k.get("id", ""))):
            kayitlar.append(k)
    return kayitlar


def _sozluk(x: Any) -> Dict[str, Any]:
    return x if isinstance(x, dict) else {}


def _liste(x: Any) -> List[Any]:
    return x if isinstance(x, list) else []


def _https(u: Any) -> str:
    u = str(u or "").strip()
    return u if u.startswith("https://") and not re.search(r"\s", u) else ""


def _katla(s: Any) -> str:
    return str(s or "").translate(_KATLA).lower()


def _kisalt(s: Any, n: int) -> str:
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def _sonuc(ok: Any, hata: Any) -> str:
    if ok:
        return "Doğrulandı"
    return "Bulunamadı" if str(hata or "") == "NOT_FOUND" else "Doğrulanamadı"


def _tarih_saat(zaman: str) -> Tuple[Optional[date], str]:
    try:
        z = datetime.fromisoformat(str(zaman))
    except ValueError:
        return None, str(zaman or "")
    return z.date(), z.strftime("%d.%m.%Y %H:%M")


def baglanti_haritasi(kayitlar: List[Dict[str, Any]]) -> Tuple[Dict[str, str], Dict[str, str]]:
    """(kanun no -> resmî metin bağlantısı, atıf -> bağlantı): yalnız kayıtta duran https bağlantıları."""
    kanun, atif = {}, {}
    for k in kayitlar:
        a = _sozluk(k.get("anlik"))
        if k.get("tur") == "madde":
            law = _sozluk(_sozluk(a.get("veri")).get("law"))
            no, url = str(law.get("number") or "").strip(), _https(law.get("source_url"))
            if no and url:
                kanun.setdefault(no, url)
        elif k.get("tur") == "cevap":
            for y in _liste(a.get("kaynaklar")):
                y = _sozluk(y)
                metin, url = str(y.get("atif") or "").strip(), _https(y.get("url"))
                if metin and url:
                    atif.setdefault(metin, url)
    return kanun, atif


def satirlari_kur(kayitlar: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Atıf taşıyan kayıtların satırları, eskiden yeniye."""
    kanun_bag, atif_bag = baglanti_haritasi(kayitlar)
    satirlar = []
    for k in sorted(kayitlar, key=lambda x: str(x.get("id"))):
        tur = k.get("tur")
        if tur not in KAYNAK_ADI:
            continue
        gun, tarih_saat = _tarih_saat(k.get("zaman"))
        konu = _kisalt(k.get("baslik"), 160)
        ortak = {"zaman": str(k.get("zaman") or ""), "gun": gun, "tarih_saat": tarih_saat,
                 "kaynak": KAYNAK_ADI[tur], "konu": konu, "kayit_id": str(k.get("id")),
                 "is": KAYNAK_ADI[tur] + (": " + konu if tur == "cevap" and konu else "")}
        a = _sozluk(k.get("anlik"))
        if tur in ("atif", "cevap"):
            kaynak = a.get("satirlar") if tur == "atif" else _sozluk(a.get("teyit")).get("satirlar")
            for s in _liste(kaynak):
                s = _sozluk(s)
                no, madde = str(s.get("kanun") or "").strip(), str(s.get("madde") or "").strip()
                if not no or not madde:
                    continue
                citation = str(s.get("citation") or "").strip() if s.get("ok") else ""
                satirlar.append({**ortak, "kanun": no, "madde": madde,
                                 "atif": citation or "%s sayılı Kanun m. %s (kayıttaki numara)" % (no, madde),
                                 "madde_basligi": _kisalt(s.get("baslik"), 200), "sonuc": _sonuc(s.get("ok"), s.get("hata")),
                                 "baglanti": (atif_bag.get(citation) or kanun_bag.get(no, "")) if citation else ""})
        else:  # madde
            veri = _sozluk(a.get("veri"))
            law = _sozluk(veri.get("law"))
            no, url = str(law.get("number") or "").strip(), _https(law.get("source_url"))
            for it in _liste(veri.get("items")):
                it = _sozluk(it)
                madde = str(it.get("madde_no") or it.get("requested") or "").strip()
                if not madde:
                    continue
                ok = bool(it.get("ok"))
                citation = str(it.get("citation") or "").strip() if ok else ""
                satirlar.append({**ortak, "kanun": no, "madde": madde,
                                 "atif": citation or "%s sayılı Kanun m. %s (kayıttaki numara)" % (no or "?", madde),
                                 "madde_basligi": _kisalt(it.get("heading"), 200) if ok else "",
                                 "sonuc": _sonuc(ok, it.get("error_code")), "baglanti": url if ok else ""})
    return satirlar


def _gun(metin: Any, alan: str) -> Optional[date]:
    metin = str(metin or "").strip()
    if not metin:
        return None
    try:
        return date.fromisoformat(metin)
    except ValueError:
        raise KayitHatasi("%s YYYY-AA-GG biçiminde olmalı (ör. 2026-11-07)." % alan) from None


def suz(satirlar: List[Dict[str, Any]], baslangic: Optional[date], bitis: Optional[date],
        ara: Optional[str]) -> List[Dict[str, Any]]:
    q = _katla(ara).strip()
    sonuc = []
    for s in satirlar:
        if baslangic and (s["gun"] is None or s["gun"] < baslangic):
            continue
        if bitis and (s["gun"] is None or s["gun"] > bitis):
            continue
        if q and not any(q in _katla(s.get(a)) for a in ("atif", "kanun", "madde", "madde_basligi", "konu")):
            continue
        sonuc.append(s)
    return sonuc


# ---------------------------------------------------------------------------- yazma

def notlar(saklama_gun: int) -> List[str]:
    """Belgenin sınır notları: kaydın neyi gösterip neyi göstermediği."""
    return [
        "Doğrulandı: madde numarası resmî metinde bulundu ve başlığı getirildi. Maddeye yüklenen içeriğin (hakkın "
        "sahibi, şart, süre, sonuç) metinle örtüştüğü ayrıca okunarak kontrol edilir; bu kayıt onu göstermez.",
        "Bulunamadı ya da Doğrulanamadı: o atıf bu haliyle kullanılmaz; resmî metinden teyit edilir.",
        "Kapsam: yalnız bu bilgisayardaki ArthurLegal Masası'nda yapılan teyitler. Web ya da telefondaki masanın "
        "geçmişi o cihazda kalır. Masa geçmişi %d gün tutulur; dökümü bu süre dolmadan almak kaydı kesintisiz tutar."
        % saklama_gun,
        "İçtihat künyeleri bu kayıtta yoktur: masa kanun maddesi atıflarını teyit eder.",
        "Resmî bağlantı: kayıtta resmî metin bağlantısı yoksa alan boştur; maddeyi %s üzerinden açın." % RESMI_GIRIS,
        "İş sütunu masadaki sorunun ya da işin başlığıdır; dökümü dosyaya ya da müvekkile vermeden önce müvekkil "
        "bilgisi içerip içermediğine bakın.",
    ]


def _ozet_satirlari(ozet: Dict[str, Any]) -> List[str]:
    k = ozet["kapsam"]
    aralik = "%s – %s" % (k.get("baslangic") or "geçmişin başı", k.get("bitis") or "bugün")
    satirlar = ["Oluşturma: %s" % ozet["olusturma"], "Aralık: %s" % aralik]
    if k.get("ara"):
        satirlar.append("Süzgeç: %s" % k["ara"])
    satirlar.append("%d atıf · %d doğrulandı · %d doğrulanamadı ya da bulunamadı · %d kayıt"
                    % (ozet["satir"], ozet["dogrulanan"], ozet["satir"] - ozet["dogrulanan"], ozet["kayit"]))
    return satirlar


def _hucre_md(s: Any) -> str:
    return re.sub(r"\s+", " ", str(s or "")).replace("|", "\\|").strip() or "—"


def markdown(satirlar: List[Dict[str, Any]], ozet: Dict[str, Any], saklama_gun: int) -> str:
    out = ["# ArthurLegal doğrulama kaydı", ""]
    out += ["- " + x for x in _ozet_satirlari(ozet)]
    out += ["", "| " + " | ".join(b for _, b in BELGE_SUTUNLARI) + " |",
            "|" + "---|" * len(BELGE_SUTUNLARI)]
    for s in satirlar:
        out.append("| " + " | ".join(_hucre_md(s.get(a)) for a, _ in BELGE_SUTUNLARI) + " |")
    out += ["", "## Notlar", ""] + ["- " + n for n in notlar(saklama_gun)]
    return "\n".join(out) + "\n"


def csv_metni(satirlar: List[Dict[str, Any]]) -> str:
    """Noktalı virgüllü CSV: Türkçe Excel ayırıcı olarak bunu bekler. BOM'u yazan ekler."""
    tampon = io.StringIO()
    w = csv.writer(tampon, delimiter=";", lineterminator="\r\n")
    w.writerow([b for _, b in SUTUNLAR])
    for s in satirlar:
        w.writerow([str(s.get(a) or "") for a, _ in SUTUNLAR])
    return tampon.getvalue()


def _x(s: Any) -> str:
    return escape(_XML_DISI.sub("", str(s or "")))


def _paragraf(metin: str, kalin: bool = False, boyut: Optional[int] = None) -> str:
    rpr = ("<w:b/>" if kalin else "") + ('<w:sz w:val="%d"/>' % boyut if boyut else "")
    return ('<w:p><w:r>%s<w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % ("<w:rPr>%s</w:rPr>" % rpr if rpr else "", _x(metin)))


def docx_bayt(satirlar: List[Dict[str, Any]], ozet: Dict[str, Any], saklama_gun: int) -> bytes:
    """En küçük geçerli Word belgesi: başlık, özet, tablo ve notlar; A4 yatay. Stil dosyası yok, Word varsayılanı."""
    genislik = (1700, 3600, 1300, 2600, 3000, 2370)   # dxa; toplam yatay A4 metin alanı (~14570)
    kenar = "".join('<w:%s w:val="single" w:sz="4" w:space="0" w:color="999999"/>' % y
                    for y in ("top", "left", "bottom", "right", "insideH", "insideV"))

    def hucre(metin: Any, w: int, kalin: bool = False) -> str:
        return ('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/></w:tcPr>%s</w:tc>'
                % (w, _paragraf(str(metin or "") or "—", kalin=kalin, boyut=18)))

    tablo = ['<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/><w:tblBorders>%s</w:tblBorders></w:tblPr><w:tblGrid>'
             % kenar + "".join('<w:gridCol w:w="%d"/>' % w for w in genislik) + "</w:tblGrid>"]
    tablo.append('<w:tr><w:trPr><w:tblHeader/></w:trPr>' +
                 "".join(hucre(b, w, True) for (_, b), w in zip(BELGE_SUTUNLARI, genislik)) + "</w:tr>")
    for s in satirlar:
        tablo.append("<w:tr>" + "".join(hucre(s.get(a), w) for (a, _), w in zip(BELGE_SUTUNLARI, genislik)) + "</w:tr>")
    tablo.append("</w:tbl>")
    govde = ([_paragraf("ArthurLegal doğrulama kaydı", kalin=True, boyut=32)]
             + [_paragraf(x) for x in _ozet_satirlari(ozet)] + ["".join(tablo)]
             + [_paragraf("Notlar", kalin=True, boyut=24)] + [_paragraf("• " + n) for n in notlar(saklama_gun)])
    belge = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
             + "".join(govde) +
             '<w:sectPr><w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/>'
             '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/>'
             "</w:sectPr></w:body></w:document>")
    turler = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
              '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
              '<Default Extension="xml" ContentType="application/xml"/>'
              '<Override PartName="/word/document.xml" '
              'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>')
    iliski = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
              '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/'
              'officeDocument" Target="word/document.xml"/></Relationships>')
    tampon = io.BytesIO()
    with zipfile.ZipFile(tampon, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", turler)
        z.writestr("_rels/.rels", iliski)
        z.writestr("word/document.xml", belge)
    return tampon.getvalue()


def disa_aktar(gecmis_klasoru: str, hedef_klasor: str, girdi: Dict[str, Any], saklama_gun: int = 90,
               simdi: Optional[datetime] = None) -> Dict[str, Any]:
    """İsteği doğrular, satırları kurar ve dosyayı yazar. Satır yoksa dosya yazmaz."""
    girdi = girdi if isinstance(girdi, dict) else {}
    bicim = str(girdi.get("bicim") or "md").lower().lstrip(".")
    if bicim not in BICIMLER:
        raise KayitHatasi("bicim md, csv ya da docx olmalı.")
    baslangic, bitis = _gun(girdi.get("baslangic"), "baslangic"), _gun(girdi.get("bitis"), "bitis")
    if baslangic and bitis and baslangic > bitis:
        raise KayitHatasi("baslangic bitis'ten sonra olamaz.")
    ara = _kisalt(girdi.get("ara"), 100)
    kayitlar = kayitlari_oku(gecmis_klasoru)
    satirlar = suz(satirlari_kur(kayitlar), baslangic, bitis, ara)
    kapsam = {"baslangic": baslangic.isoformat() if baslangic else None,
              "bitis": bitis.isoformat() if bitis else None, "ara": ara or None}
    if not satirlar:
        return {"dosya": None, "bicim": bicim, "satir": 0, "kapsam": kapsam, "saklama_gun": saklama_gun,
                "mesaj": "Bu aralıkta masa geçmişinde teyit edilmiş atıf yok; dosya yazılmadı. Kayıt yalnız bu "
                         "bilgisayardaki ArthurLegal Masası'nda yapılan atıf teyitlerinden ve masaya gelen cevaplardan "
                         "oluşur (son %d gün)." % saklama_gun}
    simdi = simdi or datetime.now().astimezone()
    dogrulanan = sum(1 for s in satirlar if s["sonuc"] == "Doğrulandı")
    ozet = {"olusturma": simdi.strftime("%d.%m.%Y %H:%M"), "kapsam": kapsam, "satir": len(satirlar),
            "dogrulanan": dogrulanan, "kayit": len({s["kayit_id"] for s in satirlar})}
    os.makedirs(hedef_klasor, exist_ok=True)
    ad = "dogrulama-kaydi-%s.%s" % (simdi.strftime("%Y%m%d-%H%M%S"), bicim)
    yol = os.path.join(hedef_klasor, ad)
    gecici = yol + ".yaziliyor"
    if bicim == "docx":
        with open(gecici, "wb") as fh:
            fh.write(docx_bayt(satirlar, ozet, saklama_gun))
    else:
        metin = markdown(satirlar, ozet, saklama_gun) if bicim == "md" else csv_metni(satirlar)
        with open(gecici, "w", encoding="utf-8-sig" if bicim == "csv" else "utf-8", newline="") as fh:
            fh.write(metin)
    os.replace(gecici, yol)
    return {"dosya": yol, "bicim": bicim, "satir": len(satirlar), "dogrulanan": dogrulanan,
            "dogrulanamayan": len(satirlar) - dogrulanan, "kayit": ozet["kayit"],
            "baglantisiz": sum(1 for s in satirlar if s["sonuc"] == "Doğrulandı" and not s["baglanti"]),
            "kapsam": kapsam, "saklama_gun": saklama_gun,
            "mesaj": "Doğrulama kaydı yazıldı. Dosyanın yolunu kullanıcıya verin; içeriği sohbete aktarmayın."}
