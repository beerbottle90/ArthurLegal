"""ArthurLegal paketlerinin yayın denetimi (sürüm sınavı, Katman 1).

Ağa çıkmaz, API anahtarı istemez. Depo kökündeki ArthurLegal-*-v*-Public-Release klasörlerini okur;
arsiv/ altındaki eski sürümler denetim dışıdır. Dört denetim yapar:

1. Kırık skill atfı. Paketteki .md dosyalarında geçen her /eklenti:komut atfı o pakette tanımlı bir skill'e
   gitmeli. Tanımlı skill'ler knowledge/skills/<eklenti>__skills.md kitapçıklarının İçindekiler satırlarıdır.
   Eski eklenti adıyla yazılmış atıf da kırıktır. Satırında "hazırlanıyor" notu olan atıf planlı sayılır.
   CHANGELOG.md taranmaz: geçmişi anlatır, adı değişen ya da kaldırılan komutlar orada anılır.
2. Sürüm. Klasör adındaki sürüm VERSION.md'de, SYSTEM_PROMPT.md'nin ilk satırında ve başlığında, README'nin
   sürüm satırlarında, KURULUM.md ve INSTALLATION.md'nin başında, CHANGELOG.md'nin ilk girdisinde ve
   ATTRIBUTION.md başlığında aynı olmalı. Bir dosyada kalıp yoksa o dosya denetlenmez. Aynı paketin iki
   klasörü de sorundur (eskisi arsiv/'e taşınır).
3. Sayım. Her kitapçıkta "Toplam skill: N", İçindekiler ve gövdedeki "## /eklenti:komut" bölümleri aynı
   skill'leri saymalı. Sistem talimatı başlığındaki, VERSION.md tablosundaki, README, KURULUM ve INSTALLATION
   başındaki sayılar (plugin, skill, referans, agent, profil, knowledge dosyası) gerçek dosya sayılarıyla
   aynı olmalı.
4. Yeni ayrışma. En az iki pakette aynı yolda duran dosyalardan tabanda birbirinin aynısı olan iki kopya
   artık farklıysa hatadır; tabanda farklı olup artık aynı olanlar bilgi olarak raporlanır. Satır sonu
   (CRLF/LF) ve BOM farkı ayrışma sayılmaz. Paketten pakete farklı olması gereken belgeler (SYSTEM_PROMPT,
   README, VERSION, CHANGELOG, KURULUM, INSTALLATION, ATTRIBUTION) bu denetimin dışındadır.

Bilinen kırık atıflar ve paylaşılan dosyaların tabandaki durumu tests/paket_denetimi_taban.json'dadır:
1. ve 4. denetim yalnız tabanda olmayan YENİ sorunda kırılır. Sürüm ve sayımın tabanı yoktur.

    python ArthurLegal-setup/yayin/paket_denetimi.py              rapor; çıkış kodu 0 tamam, 1 sorun, 2 hata
    python ArthurLegal-setup/yayin/paket_denetimi.py --ayrinti    her bulgunun dosyası ve satırı
    python ArthurLegal-setup/yayin/paket_denetimi.py --taban-yaz  bugünkü kırık atıfları ve paylaşılan
                                                                  dosyaların durumunu tabana yazar
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

BURASI = Path(__file__).resolve().parents[1]  # ArthurLegal-setup
KOK = BURASI.parent  # depo kökü
TABAN = BURASI / "tests" / "paket_denetimi_taban.json"

KLASOR = re.compile(r"^ArthurLegal-(?P<ad>.+)-v(?P<surum>\d+\.\d+\.\d+)-Public-Release$")
GORUNEN_AD = {"Law-Firm": "Hukuk Bürosu", "CorporateAssistant": "Kurumsal", "Courthouse": "Courthouse",
              "Academician": "Akademisyen"}
# Eski eklenti adları ve bugünkü karşılıkları: bu adlarla yazılmış atıf kırıktır
ESKI_ADLAR = {
    "administrative-litigation": "administrative-legal",
    "commercial-advisory": "commercial-legal",
    "corporate-advisory": "corporate-legal",
    "dispute-litigation": "litigation-legal",
    "employment-advisory": "employment-legal",
    "ip-advisory": "ip-legal",
    "tax-litigation": "tax-legal",
}
# Paket kökünde, paketten pakete farklı olması gereken belgeler: ayrışma denetimine girmez
PAKETE_OZGU = {"SYSTEM_PROMPT.md", "README.md", "VERSION.md", "CHANGELOG.md", "KURULUM.md", "INSTALLATION.md",
               "ATTRIBUTION.md", "LICENSE-APACHE-2.0-THIRD-PARTY.txt"}

# Kitapçık
ICINDEKILER = re.compile(r"^##\s+[İI][çc]indekiler\s*$")
TOPLAM = re.compile(r"Toplam skill\s*:\s*(\d+)")
MADDE = re.compile(r"^\s*[-*]\s+`?(/[\w-]+:[\w-]+)")
BOLUM = re.compile(r"^##\s+`?(/[\w-]+:[\w-]+)")
BASLIK = re.compile(r"^#{1,6}\s")
# Atıf: önünde harf, rakam, / . - olmayan /eklenti:komut (adres içindeki yollar sayılmaz)
ATIF = re.compile(r"(?<![\w/.-])/([a-z][\w-]*):([a-z][\w-]*)")
PLANLI = re.compile(r"hazırlanıyor|hazirlaniyor", re.I)
# Sürüm
SURUM = r"v?(\d+\.\d+\.\d+)"
# "**Sürüm:** v1.1.2", "Sürüm: **Courthouse v1.2.0**"; iki nokta şart, düz yazıdaki "Sürüm 1.8.0'dan beri" sayılmaz
ETIKET = re.compile(r"^[>\s*_]*(?:sürüm|versiyon|version)[\s*_]*:[\s*_]*(?:[^\W\d_]+\s+)?" + SURUM, re.I)
# Sistem talimatı başlığında iki nokta olmadan da: "> Sürüm 1.11.0. Talimat revizyonu ..."
ETIKET_BASLIK = re.compile(r"^[>\s*_]*(?:sürüm|versiyon|version)\b[\s*_:]*(?:[^\W\d_]+\s+)?" + SURUM, re.I)
OZET_SATIRI = re.compile(r"^>\s*\*\*v(\d+\.\d+\.\d+)\s*[—–-]")
AGAC_SATIRI = re.compile(r"VERSION\.md\s*←\s*" + SURUM)
BU_SURUM = re.compile(r"(?:bu\s+(?:sürüm|versiyon)|this\s+is\s+version)\s*\**\s*" + SURUM, re.I)
CHANGELOG_GIRDISI = re.compile(r"^##\s*\[v?(\d+\.\d+\.\d+)\]")
BASLIK_SURUMU = re.compile(r"\bv(\d+\.\d+\.\d+)")
# Sayım: "12 plugin", "104 knowledge dosyası (12 birleşik skill, 84 referans, 7 agent)" ...
# ("bölüm 5 eklenti tablosu" gibi bölüm ve adım numaraları sayı değildir)
SAYIM = re.compile(
    r"(?<![\w.,])(?<!bölüm )(?<!section )(?<!adım )(?<!step )(\d+)[\s-]+(?:"
    r"(?P<kitapcik>birle[şs]ik\s+skill(?:\s+dosyas[ıi])?|plugins?|eklenti(?:li)?)"
    r"|(?P<skill>skills?)"
    r"|(?P<referans>referans|references?)"
    r"|(?P<agent>agents?|ajan|izleyici)"
    r"|(?P<profil>(?:mahkeme\s+(?:türü\s+)?)?profil(?:i|leri)?)"
    r"|(?P<knowledge>knowledge\s+(?:dosyas[ıi]|files?))"
    r")(?!\w)",
    re.I,
)
TABLO = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(\d+)\b")
TABLO_TURU = {"plugin": "kitapcik", "eklenti": "kitapcik", "skill": "skill", "referans": "referans",
              "reference": "referans", "references": "referans", "agent": "agent", "ajan": "agent",
              "izleyici": "agent", "profil": "profil", "knowledge": "knowledge"}
TUR_ADI = {"kitapcik": "plugin (kitapçık)", "skill": "skill", "referans": "referans", "agent": "agent",
           "profil": "profil", "knowledge": "knowledge dosyası"}


@dataclass
class Paket:
    yol: Path
    ad: str  # klasör adındaki sürümsüz ad: Law-Firm, CorporateAssistant ...
    surum: str

    @property
    def gorunen(self) -> str:
        return GORUNEN_AD.get(self.ad, self.ad)


@dataclass
class Kitapcik:
    eklenti: str
    dosya: str  # paket içindeki göreli yol
    toplam: tuple[int, int] | None = None  # (sayı, satır)
    icindekiler: list[tuple[str, int]] = field(default_factory=list)  # (/eklenti:komut, satır)
    govde: list[tuple[str, int]] = field(default_factory=list)


@dataclass
class Atif:
    dosya: str
    satir: int
    atif: str
    tur: str  # kirik, eski_ad, planli


@dataclass
class Bulgu:
    paket: str
    dosya: str
    satir: int
    mesaj: str

    def __str__(self) -> str:
        yer = f"{self.dosya}:{self.satir}" if self.satir else self.dosya
        return f"{self.paket}  {yer}  {self.mesaj}"


@dataclass
class Rapor:
    paketler: list[Paket]
    tanimli: dict[str, set[str]] = field(default_factory=dict)  # paket adı -> tanımlı skill'ler
    atiflar: dict[str, list[Atif]] = field(default_factory=dict)  # paket adı -> kırık ve planlı atıflar
    yeni_atif: list[Bulgu] = field(default_factory=list)
    duzelen_atif: list[str] = field(default_factory=list)
    surum: list[Bulgu] = field(default_factory=list)
    surum_yerleri: list[Bulgu] = field(default_factory=list)  # denetlenen her yer (--ayrinti)
    sayim: list[Bulgu] = field(default_factory=list)
    sayim_yerleri: list[Bulgu] = field(default_factory=list)
    paylasilan: dict[str, list[list[str]]] = field(default_factory=dict)
    yeni_ayrisma: list[Bulgu] = field(default_factory=list)
    duzelen_ayrisma: list[str] = field(default_factory=list)
    yeni_paylasilan: list[str] = field(default_factory=list)
    kaybolan: list[str] = field(default_factory=list)
    taban_yok: bool = False

    @property
    def tamam(self) -> bool:
        return not (self.yeni_atif or self.surum or self.sayim or self.yeni_ayrisma)


def oku(yol: Path) -> str:
    return yol.read_text(encoding="utf-8-sig", errors="replace")


def paketleri_bul(kok: Path = KOK) -> list[Paket]:
    """Depo kökündeki güncel paket klasörleri (arsiv/ hariç)."""
    paketler = []
    for yol in sorted(kok.glob("ArthurLegal-*-v*-Public-Release")):
        m = KLASOR.match(yol.name)
        if m and yol.is_dir():
            paketler.append(Paket(yol, m["ad"], m["surum"]))
    return paketler


def kitapcik_oku(paket: Paket, yol: Path) -> Kitapcik:
    k = Kitapcik(yol.name[: -len("__skills.md")], yol.relative_to(paket.yol).as_posix())
    icinde = False
    for no, satir in enumerate(oku(yol).splitlines(), 1):
        if ICINDEKILER.match(satir):
            icinde = True
            continue
        if icinde and (BASLIK.match(satir) or satir.strip() == "---"):
            icinde = False
        if icinde:
            if m := MADDE.match(satir):
                k.icindekiler.append((m[1], no))
        elif m := BOLUM.match(satir):
            k.govde.append((m[1], no))
        elif k.toplam is None and (m := TOPLAM.search(satir)):
            k.toplam = (int(m[1]), no)
    return k


def kitapciklar(paket: Paket) -> list[Kitapcik]:
    return [kitapcik_oku(paket, y) for y in sorted((paket.yol / "knowledge" / "skills").glob("*__skills.md"))]


# --- 1. Kırık skill atfı ----------------------------------------------------------------------------

def atiflari_tara(paket: Paket, tanimli: set[str], bilinen_eklentiler: set[str]) -> list[Atif]:
    """Pakette tanımlı olmayan skill'lere atıflar. Eklenti biçimindeki öneklere bakılır: dört paketten
    birinin eklentisi, "-legal" sonekli ya da eski eklenti adı."""
    eklentiler = {s.split(":")[0][1:] for s in tanimli}
    eskiler = set(ESKI_ADLAR) - eklentiler
    sonuc = []
    for yol in sorted(paket.yol.rglob("*.md")):
        goreli = yol.relative_to(paket.yol).as_posix()
        if goreli == "CHANGELOG.md":
            continue
        for no, satir in enumerate(oku(yol).splitlines(), 1):
            for ek, komut in ATIF.findall(satir):
                atif = f"/{ek}:{komut}"
                if atif in tanimli:
                    continue
                if not (ek in eklentiler or ek in bilinen_eklentiler or ek in eskiler or ek.endswith("-legal")):
                    continue
                tur = "planli" if PLANLI.search(satir) else "eski_ad" if ek in eskiler else "kirik"
                sonuc.append(Atif(goreli, no, atif, tur))
    return sonuc


def atif_notu(atif: str, tanimli: set[str]) -> str:
    """Atfın neden kırık olduğu, tek satır."""
    ek, komut = atif[1:].split(":", 1)
    eklentiler = {s.split(":")[0][1:] for s in tanimli}
    if ek in ESKI_ADLAR and ek not in eklentiler:
        yeni = ESKI_ADLAR[ek]
        if f"/{yeni}:{komut}" in tanimli:
            return f"eski eklenti adı; güncel karşılığı /{yeni}:{komut}"
        return f"eski eklenti adı ({ek} yerine {yeni}); {yeni} eklentisinde {komut} skill'i yok"
    if ek in eklentiler:
        return f"{ek} eklentisinde {komut} skill'i yok"
    return f"{ek} eklentisi bu pakette yok"


# --- 2. Sürüm ---------------------------------------------------------------------------------------

def satirlari(paket: Paket, ad: str) -> list[str] | None:
    yol = paket.yol / ad
    return oku(yol).splitlines() if yol.is_file() else None


def bas_bolum(satirlar: list[str], sinir: int = 25) -> list[tuple[int, str]]:
    """Dosyanın başı: ilk "---" çizgisine kadar, en çok `sinir` satır."""
    bas = []
    for no, satir in enumerate(satirlar[:sinir], 1):
        if satir.strip() == "---":
            break
        bas.append((no, satir))
    return bas


def surum_yerleri(paket: Paket) -> list[tuple[str, int, str, str]]:
    """Paketin kendi sürümünü yazdığı yerler: (dosya, satır, bulunan sürüm, yerin adı)."""
    yerler: list[tuple[str, int, str, str]] = []

    s = satirlari(paket, "VERSION.md")
    if s is not None:
        etiketli = [(no, m[1]) for no, x in enumerate(s, 1) if (m := ETIKET.match(x))]
        if not etiketli:  # yalnız sürüm numarası yazan VERSION.md
            etiketli = [(no, m[0]) for no, x in enumerate(s, 1) if (m := re.search(r"\d+\.\d+\.\d+", x))][:1]
        yerler += [("VERSION.md", no, v, "sürüm") for no, v in etiketli]

    s = satirlari(paket, "SYSTEM_PROMPT.md")
    if s:
        bas = [(no, x) for no, x in bas_bolum(s, 40) if x.strip()]
        if bas and (m := BASLIK_SURUMU.search(bas[0][1])):
            yerler.append(("SYSTEM_PROMPT.md", bas[0][0], m[1], "ilk satır"))
        yerler += [("SYSTEM_PROMPT.md", no, m[1], "başlıktaki sürüm") for no, x in bas[1:]
                   if (m := ETIKET_BASLIK.match(x))]

    kendi_klasoru = re.compile(rf"ArthurLegal-{re.escape(paket.ad)}-v(\d+\.\d+\.\d+)-Public-Release")
    s = satirlari(paket, "README.md")
    if s:
        for no, x in enumerate(s, 1):
            for kalip, yer in ((ETIKET, "sürüm satırı"), (OZET_SATIRI, "özet satırı")):
                if m := kalip.match(x):
                    yerler.append(("README.md", no, m[1], yer))
            for kalip, yer in ((AGAC_SATIRI, "dosya ağacı"), (kendi_klasoru, "klasör adı")):
                yerler += [("README.md", no, m[1], yer) for m in kalip.finditer(x)]

    for ad in ("KURULUM.md", "INSTALLATION.md"):
        s = satirlari(paket, ad)
        if not s:
            continue
        for no, x in bas_bolum(s, 15):
            if BASLIK.match(x) and "ArthurLegal" in x and (m := BASLIK_SURUMU.search(x)):
                yerler.append((ad, no, m[1], "başlık"))
            elif m := ETIKET.match(x):
                yerler.append((ad, no, m[1], "sürüm satırı"))
        for no, x in enumerate(s, 1):
            for kalip, yer in ((BU_SURUM, "güncel sürüm cümlesi"), (kendi_klasoru, "klasör adı")):
                yerler += [(ad, no, m[1], yer) for m in kalip.finditer(x)]

    s = satirlari(paket, "CHANGELOG.md")
    if s:
        ilk = next(((no, m[1]) for no, x in enumerate(s, 1) if (m := CHANGELOG_GIRDISI.match(x))), None)
        if ilk:
            yerler.append(("CHANGELOG.md", ilk[0], ilk[1], "ilk girdi"))

    s = satirlari(paket, "ATTRIBUTION.md")
    if s:
        yerler += [("ATTRIBUTION.md", no, m[1], "başlık") for no, x in enumerate(s[:10], 1)
                   if BASLIK.match(x) and "ArthurLegal" in x and (m := BASLIK_SURUMU.search(x))]
    return yerler


def surum_denetimi(paketler: list[Paket], rapor: Rapor) -> None:
    for ad, sayi in Counter(p.ad for p in paketler).items():
        if sayi > 1:
            klasorler = ", ".join(p.yol.name for p in paketler if p.ad == ad)
            rapor.surum.append(Bulgu(GORUNEN_AD.get(ad, ad), "", 0,
                                     f"aynı paketin {sayi} klasörü var ({klasorler}); eskisi arsiv/'e taşınmalı"))
    for p in paketler:
        for dosya, no, bulunan, yer in surum_yerleri(p):
            b = Bulgu(p.gorunen, dosya, no, f"{yer}: {bulunan}")
            rapor.surum_yerleri.append(b)
            if bulunan != p.surum:
                rapor.surum.append(Bulgu(p.gorunen, dosya, no,
                                         f"{yer} {bulunan} diyor, klasör adındaki sürüm {p.surum}"))


# --- 3. Sayım ---------------------------------------------------------------------------------------

def gercek_sayilar(paket: Paket, kitaplar: list[Kitapcik]) -> dict[str, int | None]:
    """Sayılabilen bileşenlerin gerçek sayısı; klasör yoksa None (o sayı denetlenmez)."""
    k = paket.yol / "knowledge"

    def dosya_sayisi(d: Path) -> int | None:
        return sum(1 for y in d.rglob("*") if y.is_file()) if d.is_dir() else None

    return {
        "kitapcik": len(kitaplar),
        "skill": sum(len(x.icindekiler) for x in kitaplar),
        "referans": dosya_sayisi(k / "references"),
        "agent": dosya_sayisi(k / "agents"),
        "profil": dosya_sayisi(k / "profiles"),
        "knowledge": dosya_sayisi(k),
    }


def sayim_ifadeleri(metin: str) -> list[tuple[str, int, str]]:
    """Metindeki "N plugin", "N skill" ... ifadeleri: (tür, sayı, ifade)."""
    return [(m.lastgroup, int(m[1]), m[0]) for m in SAYIM.finditer(metin)]


def kitapcik_denetimi(paket: Paket, kitaplar: list[Kitapcik], rapor: Rapor) -> None:
    for k in kitaplar:
        def bulgu(satir: int, mesaj: str) -> None:
            rapor.sayim.append(Bulgu(paket.gorunen, k.dosya, satir, mesaj))

        ic = [s for s, _ in k.icindekiler]
        govde = [s for s, _ in k.govde]
        rapor.sayim_yerleri.append(Bulgu(paket.gorunen, k.dosya, k.toplam[1] if k.toplam else 0,
                                         f"Toplam skill {k.toplam[0] if k.toplam else '-'}, İçindekiler "
                                         f"{len(ic)}, gövde {len(govde)}"))
        if k.toplam and k.toplam[0] != len(ic):
            bulgu(k.toplam[1], f"Toplam skill: {k.toplam[0]} diyor, İçindekiler'de {len(ic)} skill var")
        if len(govde) != len(ic):
            bulgu(0, f"İçindekiler'de {len(ic)} skill, gövdede {len(govde)} '## /{k.eklenti}:' bölümü var")
        for s, n in Counter(ic).items():
            if n > 1:
                bulgu(0, f"{s} İçindekiler'de {n} kez geçiyor")
        for s, no in k.icindekiler:
            if s not in govde:
                bulgu(no, f"{s} İçindekiler'de var, gövdede bölümü yok")
        for s, no in k.govde:
            if s not in ic:
                bulgu(no, f"{s} bölümü var, İçindekiler'de yok")
        for s, no in k.icindekiler + k.govde:
            if s.split(":")[0][1:] != k.eklenti:
                bulgu(no, f"{s} bu kitapçığın eklentisine ({k.eklenti}) ait değil")


def sayi_karsilastir(paket: Paket, gercek: dict[str, int | None], dosya: str, no: int,
                     tur: str, sayi: int, ifade: str, rapor: Rapor) -> None:
    beklenen = gercek.get(tur)
    if beklenen is None:
        return
    rapor.sayim_yerleri.append(Bulgu(paket.gorunen, dosya, no, f"'{ifade}' (gerçek: {beklenen})"))
    if sayi != beklenen:
        rapor.sayim.append(Bulgu(paket.gorunen, dosya, no,
                                 f"'{ifade}' yazıyor, pakette {beklenen} {TUR_ADI[tur]} var"))


def sayim_denetimi(paket: Paket, kitaplar: list[Kitapcik], rapor: Rapor) -> None:
    kitapcik_denetimi(paket, kitaplar, rapor)
    gercek = gercek_sayilar(paket, kitaplar)

    bolgeler: list[tuple[str, int, str]] = []  # (dosya, satır, metin)
    s = satirlari(paket, "SYSTEM_PROMPT.md")
    if s:  # başlık; sürüm ve revizyon geçmişini anlatan satırlar hariç
        bolgeler += [("SYSTEM_PROMPT.md", no, x) for no, x in bas_bolum(s, 40)
                     if not ETIKET_BASLIK.match(x) and "revizyon" not in x.lower()]
    s = satirlari(paket, "README.md")
    if s:
        bas = bas_bolum(s)
        bolgeler += [("README.md", no, x) for no, x in bas]
        bolgeler += [("README.md", no, x) for no, x in enumerate(s, 1) if no > len(bas) and OZET_SATIRI.match(x)]
    for ad in ("KURULUM.md", "INSTALLATION.md"):
        s = satirlari(paket, ad)
        if s:
            bolgeler += [(ad, no, x) for no, x in bas_bolum(s)]
    for dosya, no, metin in bolgeler:
        for tur, sayi, ifade in sayim_ifadeleri(metin):
            sayi_karsilastir(paket, gercek, dosya, no, tur, sayi, ifade, rapor)

    # VERSION.md sayım tablosu: "| Plugin | 8 |" ve eklenti başına "| `atif-kaynak` | 3 |"
    eklenti_skill = {k.eklenti: len(k.icindekiler) for k in kitaplar}
    for no, x in enumerate(satirlari(paket, "VERSION.md") or [], 1):
        if not (m := TABLO.match(x)):
            continue
        etiket, sayi = m[1].strip("`* ").lower(), int(m[2])
        if not etiket:
            continue
        if etiket in eklenti_skill:
            beklenen = eklenti_skill[etiket]
            rapor.sayim_yerleri.append(Bulgu(paket.gorunen, "VERSION.md", no, f"{etiket}: {sayi} (gerçek: {beklenen})"))
            if sayi != beklenen:
                rapor.sayim.append(Bulgu(paket.gorunen, "VERSION.md", no,
                                         f"{etiket} için {sayi} skill yazıyor, kitapçıkta {beklenen} var"))
        elif (tur := TABLO_TURU.get(etiket.split()[0])) is not None:
            sayi_karsilastir(paket, gercek, "VERSION.md", no, tur, sayi, f"{m[1].strip()} | {sayi}", rapor)


# --- 4. Yeni ayrışma ---------------------------------------------------------------------------------

def ozet(yol: Path) -> str:
    """İçeriğin özeti; satır sonu (CRLF/LF) ve BOM farkı yok sayılır."""
    ham = yol.read_bytes()
    if ham.startswith(b"\xef\xbb\xbf"):
        ham = ham[3:]
    return hashlib.sha256(ham.replace(b"\r\n", b"\n")).hexdigest()


def paylasilan_durum(paketler: list[Paket]) -> dict[str, list[list[str]]]:
    """En az iki pakette aynı yolda duran dosyalar: yol -> içeriği aynı olan paket grupları."""
    harita: dict[str, dict[str, str]] = defaultdict(dict)
    for p in paketler:
        for yol in p.yol.rglob("*"):
            goreli = yol.relative_to(p.yol).as_posix()
            if yol.is_file() and goreli not in PAKETE_OZGU:
                harita[goreli][p.ad] = ozet(yol)
    durum = {}
    for goreli, ozetler in sorted(harita.items()):
        if len(ozetler) >= 2:
            gruplar: dict[str, list[str]] = defaultdict(list)
            for ad, oz in sorted(ozetler.items()):
                gruplar[oz].append(ad)
            durum[goreli] = sorted(gruplar.values())
    return durum


def ayrisma_denetimi(durum: dict[str, list[list[str]]], taban: dict[str, list[list[str]]], rapor: Rapor) -> None:
    """Tabanda aynı gruptaki (içeriği aynı) kopyalar bölündüyse yeni ayrışma; ayrı gruplar birleştiyse bilgi."""
    def adlar(g: list[str]) -> str:
        return " = ".join(GORUNEN_AD.get(a, a) for a in g)

    for yol, gruplar in durum.items():
        if yol not in taban:
            rapor.yeni_paylasilan.append(yol)
            continue
        simdi = {a: i for i, g in enumerate(gruplar) for a in g}
        once = {a: i for i, g in enumerate(taban[yol]) for a in g}
        yeni_kopya = sorted(set(simdi) - set(once))
        if yeni_kopya:
            rapor.yeni_paylasilan.append(f"{yol} (yeni kopya: {', '.join(GORUNEN_AD.get(a, a) for a in yeni_kopya)})")
        for g in taban[yol]:
            parcalar: dict[int, list[str]] = defaultdict(list)
            for a in g:
                if a in simdi:
                    parcalar[simdi[a]].append(a)
            if len(parcalar) > 1:
                kalan = [a for p in parcalar.values() for a in p]
                rapor.yeni_ayrisma.append(Bulgu(adlar(kalan), yol, 0, "tabanda aynıydı, şimdi: "
                                                + " | ".join(adlar(p) for p in parcalar.values())))
        for g in gruplar:
            if len({once[a] for a in g if a in once}) > 1:
                rapor.duzelen_ayrisma.append(f"{yol}: {adlar([a for a in g if a in once])} artık aynı")
    rapor.kaybolan = sorted(set(taban) - set(durum))


# --- Taban -------------------------------------------------------------------------------------------

def taban_oku(yol: Path) -> dict | None:
    if not yol.is_file():
        return None
    try:
        return json.loads(yol.read_text(encoding="utf-8"))
    except ValueError as e:
        raise ValueError(f"taban dosyası okunamadı ({yol}): {e}") from e


def taban_durumu(taban: dict) -> dict[str, list[list[str]]]:
    return {yol: [g.split(" = ") for g in kayit["kopyalar"]]
            for yol, kayit in taban.get("paylasilan_dosyalar", {}).items()}


def atif_sayaci(atiflar: dict[str, list[Atif]]) -> Counter:
    return Counter((ad, a.dosya, a.atif) for ad, liste in atiflar.items() for a in liste if a.tur != "planli")


def taban_atif_sayaci(taban: dict) -> Counter:
    return Counter({(ad, k["dosya"], k["atif"]): k["adet"]
                    for ad, liste in taban.get("kirik_atiflar", {}).items() for k in liste})


# --- Denetim -----------------------------------------------------------------------------------------

def denetle(kok: Path = KOK, taban_yolu: Path = TABAN) -> Rapor:
    """Dört denetimi çalıştırır; tabandaki bilinen sorunlar hata sayılmaz."""
    paketler = paketleri_bul(kok)
    rapor = Rapor(paketler)
    taban = taban_oku(taban_yolu)
    rapor.taban_yok = taban is None
    taban = taban or {}

    kitaplar = {p.yol: kitapciklar(p) for p in paketler}
    bilinen_eklentiler = {k.eklenti for liste in kitaplar.values() for k in liste}
    for p in paketler:
        rapor.tanimli[p.ad] = {s for k in kitaplar[p.yol] for s, _ in k.icindekiler}
        rapor.atiflar[p.ad] = atiflari_tara(p, rapor.tanimli[p.ad], bilinen_eklentiler)
        sayim_denetimi(p, kitaplar[p.yol], rapor)
    surum_denetimi(paketler, rapor)

    # Taban (paket, dosya, atıf) başına adet tutar: satır numarası kaysa da bilinen atıf yeni sayılmaz
    simdi, once = atif_sayaci(rapor.atiflar), taban_atif_sayaci(taban)
    for (ad, dosya, atif), adet in simdi.items():
        fazla = adet - once.get((ad, dosya, atif), 0)
        if fazla <= 0:
            continue
        yerler = [a for a in rapor.atiflar[ad] if a.dosya == dosya and a.atif == atif and a.tur != "planli"]
        for a in yerler[-fazla:]:
            rapor.yeni_atif.append(Bulgu(GORUNEN_AD.get(ad, ad), dosya, a.satir,
                                         f"{atif} ({atif_notu(atif, rapor.tanimli[ad])})"))
    rapor.yeni_atif.sort(key=lambda b: (b.paket, b.dosya, b.satir))
    for (ad, dosya, atif), adet in sorted(once.items()):
        if simdi.get((ad, dosya, atif), 0) < adet:
            rapor.duzelen_atif.append(f"{GORUNEN_AD.get(ad, ad)}  {dosya}  {atif}")

    rapor.paylasilan = paylasilan_durum(paketler)
    ayrisma_denetimi(rapor.paylasilan, taban_durumu(taban), rapor)
    return rapor


def taban_olustur(rapor: Rapor, eski: dict | None) -> dict:
    """Raporun bugünkü kırık atıflarından ve paylaşılan dosyalarından taban; var olan notlar korunur."""
    eski = eski or {}
    eski_atif_notu = {(ad, k["dosya"], k["atif"]): k.get("not")
                      for ad, liste in eski.get("kirik_atiflar", {}).items() for k in liste}
    eski_dosya_notu = {yol: k.get("not") for yol, k in eski.get("paylasilan_dosyalar", {}).items()}
    sayac = atif_sayaci(rapor.atiflar)
    kirik: dict[str, list[dict]] = {p.ad: [] for p in rapor.paketler}
    for (ad, dosya, atif), adet in sorted(sayac.items()):
        not_ = eski_atif_notu.get((ad, dosya, atif)) or atif_notu(atif, rapor.tanimli[ad])
        kirik[ad].append({"dosya": dosya, "atif": atif, "adet": adet, "not": not_})
    dosyalar = {}
    for yol, gruplar in rapor.paylasilan.items():
        if len(gruplar) == 1:
            varsayilan = "kopyalar aynı; biri değişirse ötekiler de değişmeli"
        elif all(len(g) == 1 for g in gruplar):
            varsayilan = "kopyalar tabanda farklı (paket uyarlaması ya da eski kopya); denetim birbirine bağlamaz"
        else:
            varsayilan = "kopyalar tabanda kısmen farklı; aynı gruptakiler birlikte değişmeli"
        dosyalar[yol] = {"kopyalar": [" = ".join(g) for g in gruplar], "not": eski_dosya_notu.get(yol) or varsayilan}
    return {
        "not": ("Paket denetiminin tabanı: bilinen kırık skill atıfları ve paketler arasında paylaşılan dosyaların "
                "bugünkü durumu (içeriği aynı kopyalar aynı grupta). Test yalnız bunlara göre YENİ sorunda kırılır. "
                "Bir sorun düzeltilince ya da bilinçli bir ayrışma kabul edilince: "
                "python ArthurLegal-setup/yayin/paket_denetimi.py --taban-yaz (var olan notlar korunur)."),
        "kirik_atiflar": kirik,
        "paylasilan_dosyalar": dosyalar,
    }


def taban_metni(taban: dict) -> str:
    """Satır satır karşılaştırılabilir JSON: her kayıt tek satırda."""
    def j(x) -> str:
        return json.dumps(x, ensure_ascii=False)

    satirlar = ["{", f'  "not": {j(taban["not"])},', '  "kirik_atiflar": {']
    paketler = list(taban["kirik_atiflar"].items())
    for i, (ad, kayitlar) in enumerate(paketler):
        virgul = "," if i < len(paketler) - 1 else ""
        if not kayitlar:
            satirlar.append(f"    {j(ad)}: []{virgul}")
            continue
        satirlar.append(f"    {j(ad)}: [")
        satirlar += [f"      {j(k)}" + ("," if n < len(kayitlar) - 1 else "") for n, k in enumerate(kayitlar)]
        satirlar.append(f"    ]{virgul}")
    satirlar += ["  },", '  "paylasilan_dosyalar": {']
    dosyalar = list(taban["paylasilan_dosyalar"].items())
    satirlar += [f"    {j(yol)}: {j(k)}" + ("," if i < len(dosyalar) - 1 else "") for i, (yol, k) in enumerate(dosyalar)]
    satirlar += ["  }", "}"]
    return "\n".join(satirlar) + "\n"


def taban_yaz(kok: Path = KOK, taban_yolu: Path = TABAN) -> dict:
    rapor = denetle(kok, taban_yolu)
    taban = taban_olustur(rapor, taban_oku(taban_yolu))
    taban_yolu.write_text(taban_metni(taban), encoding="utf-8", newline="\n")
    return taban


# --- Komut satırı --------------------------------------------------------------------------------------

def yazdir(rapor: Rapor, ayrinti: bool = False) -> None:
    def durum(sorunlar: list) -> str:
        return "SORUN" if sorunlar else "TAMAM"

    def liste(bulgular, girinti: str = "     ") -> None:
        for b in bulgular:
            print(f"{girinti}{b}")

    kirik = {ad: sum(1 for a in atiflar if a.tur != "planli") for ad, atiflar in rapor.atiflar.items()}
    print(f"ArthurLegal paket denetimi: {len(rapor.paketler)} paket")
    for p in rapor.paketler:
        planli = len(rapor.atiflar.get(p.ad, [])) - kirik.get(p.ad, 0)
        print(f"  {p.gorunen:<14} v{p.surum:<9} {len(rapor.tanimli.get(p.ad, ())):>4} skill  "
              f"{kirik.get(p.ad, 0):>3} kırık atıf" + (f", {planli} planlı" if planli else ""))
    print()

    toplam = sum(kirik.values())
    dagilim = ", ".join(f"{GORUNEN_AD.get(ad, ad)} {n}" for ad, n in kirik.items() if n)
    print(f"1. Kırık skill atfı: {durum(rapor.yeni_atif)}. Paketlerde {toplam} kırık atıf var"
          + (f" ({dagilim})" if dagilim else "") + f"; {toplam - len(rapor.yeni_atif)} tanesi tabanda, "
          f"{len(rapor.yeni_atif)} tanesi yeni.")
    liste(rapor.yeni_atif)
    if ayrinti:
        for ad, atiflar in rapor.atiflar.items():
            for a in atiflar:
                print(f"       {GORUNEN_AD.get(ad, ad)}  {a.dosya}:{a.satir}  {a.atif}  [{a.tur}]")

    print(f"2. Sürüm: {durum(rapor.surum)}. {len(rapor.surum_yerleri)} sürüm yeri denetlendi.")
    liste(rapor.surum)
    if ayrinti:
        liste(rapor.surum_yerleri, "       ")

    print(f"3. Sayım: {durum(rapor.sayim)}. {len(rapor.sayim_yerleri)} sayı denetlendi.")
    liste(rapor.sayim)
    if ayrinti:
        liste(rapor.sayim_yerleri, "       ")

    ayrisan = sum(1 for g in rapor.paylasilan.values() if len(g) > 1)
    print(f"4. Yeni ayrışma: {durum(rapor.yeni_ayrisma)}. En az iki pakette {len(rapor.paylasilan)} ortak dosya var; "
          f"{ayrisan} tanesinin kopyaları farklı, {len(rapor.yeni_ayrisma)} yeni ayrışma.")
    liste(rapor.yeni_ayrisma)
    if ayrinti:
        for yol, gruplar in rapor.paylasilan.items():
            if len(gruplar) > 1:
                print(f"       {yol}  " + " | ".join(" = ".join(GORUNEN_AD.get(a, a) for a in g) for g in gruplar))

    bilgiler = (
        [f"tabanda olup düzelen kırık atıf: {x}" for x in rapor.duzelen_atif]
        + [f"tabanda olup düzelen ayrışma: {x}" for x in rapor.duzelen_ayrisma]
        + ([] if rapor.taban_yok else [f"tabanda olmayan ortak dosya: {x}" for x in rapor.yeni_paylasilan])
        + [f"artık ortak olmayan dosya: {x}" for x in rapor.kaybolan]
    )
    if rapor.taban_yok:
        print("\nTaban dosyası yok; bütün kırık atıflar yeni sayıldı. Bugünkü durumu taban yapmak için: --taban-yaz")
    if bilgiler:
        print("\nBilgi (hata değil; tabanı güncellemek için --taban-yaz):")
        for b in bilgiler:
            print(f"  {b}")
    print(f"\nSonuç: {'TAMAM' if rapor.tamam else 'SORUN VAR'}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="ArthurLegal paketlerinin yayın denetimi (ağa çıkmaz)")
    ap.add_argument("--ayrinti", action="store_true", help="her bulgunun dosyası ve satırı")
    ap.add_argument("--taban-yaz", action="store_true",
                    help="bugünkü kırık atıfları ve paylaşılan dosyaların durumunu tabana yaz")
    ap.add_argument("--kok", type=Path, default=KOK, help="paketlerin bulunduğu depo kökü")
    ap.add_argument("--taban", type=Path, default=TABAN, help="taban dosyası")
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not paketleri_bul(a.kok):
        print(f"HATA: {a.kok} altında ArthurLegal-*-v*-Public-Release klasörü yok", file=sys.stderr)
        return 2
    try:
        if a.taban_yaz:
            taban = taban_yaz(a.kok, a.taban)
            adet = sum(k["adet"] for liste_ in taban["kirik_atiflar"].values() for k in liste_)
            ayrisan = sum(1 for k in taban["paylasilan_dosyalar"].values() if len(k["kopyalar"]) > 1)
            print(f"Taban yazıldı: {a.taban}\n  {adet} kırık atıf, {len(taban['paylasilan_dosyalar'])} paylaşılan "
                  f"dosya ({ayrisan} tanesinde kopyalar farklı)\n")
        rapor = denetle(a.kok, a.taban)
    except ValueError as e:
        print(f"HATA: {e}", file=sys.stderr)
        return 2
    yazdir(rapor, a.ayrinti)
    return 0 if rapor.tamam else 1


if __name__ == "__main__":
    raise SystemExit(main())
