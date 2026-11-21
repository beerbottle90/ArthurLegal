#!/usr/bin/env python3
"""ChatGPT (OpenAI) eklentisi: Law Firm paketinden `ArthurLegal-openai-plugin/` klasörünü üretir.

Claude eklentisiyle (eklenti_uret.py, `ArthurLegal-plugin/`, 146 beceri) aynı kaynaktan üretilir, onu değiştirmez
(16.11.2026, K3/K6). ChatGPT'nin beceri listesi bütçesi dardır (bağlamın %2'si ya da 8.000 karakter), bu yüzden paket:

  - 1 kural becerisi (`skills/arthurlegal/`): SYSTEM_PROMPT, sağlayıcıdan bağımsız dille; rehberler, pratik profilleri
    ve büro profili onun `references/` klasöründe. Masayı açma cümlesi açıklamadadır (K24).
  - 11 alan becerisi (masadaki İş akışları kategorileri, `tasarim/is-akislari.json`): 112 iş akışı ve 34 yardımcı
    beceri, kendi alanının `references/` klasöründe tam metin.

Bağlantı OpenAI profilidir (`/openai/mcp`, K11/K12). Claude'a özgü yollar ve adlar çevrilir (OpenAI kuralı: "Replace
Claude-specific references ... with provider-neutral language"); pratik profili ve dosya çalışma alanları masaüstünde
ArthurLegal Hafıza'ya yazılır, Hafıza yoksa sohbette sorulur (K26). Çıktıda Claude izi kalırsa üretim durur.

    python yayin/openai_eklenti_uret.py                        klasörü yeniden üret (gerekirse sürümü artırır)
    python yayin/openai_eklenti_uret.py --denetle              yalnız denetle: klasör paketten farklıysa 1 ile çık
    python yayin/openai_eklenti_uret.py --denetle --taban REF  ayrıca: eklenti REF'tekinden farklıysa sürümü artmış mı

Biçim resmî belgeden (developers.openai.com/plugins/build/plugins, 16.11.2026): kökte Agent Plugins `plugin.json`
(OpenAI ayarları `extensions.com.openai`), kökte `mcp.json` (`streamable-http`, `auth.type: none`), `skills/<ad>/SKILL.md`
ve becerinin yanında `references/`. Yalnız standart kütüphane.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

_YER = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("eklenti_uret", _YER / "eklenti_uret.py")
EK = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(EK)

KOK = EK.KOK
CIKTI = "ArthurLegal-openai-plugin"
AD = "arthurlegal"
MCP_URL = "https://arthurlegal-mcp.fly.dev/openai/mcp"
AKISLAR = KOK / "ArthurLegal-setup" / "istemci" / "arayuz" / "ortak" / "tasarim" / "is-akislari.json"
# Dosya yolları becerinin kendi klasörüne göredir (eklenti içinde de, ~/.codex/skills altına tek tek kurulumda da
# beceriler kardeş klasördür): kural becerisinin başvuru klasörü her beceriden ../arthurlegal/references/.
KURAL_DOSYASI = "skills/%s/references/" % AD
KURAL_YOLU = "../%s/references/" % AD
SEMA_EKLENTI = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
SEMA_MCP = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
LACIVERT = "#12285a"

# Yardımcı becerilerin (kurulum, ayar, dosya çalışma alanı) alanı, uygulama alanından. İş akışlarının alanı dosyadadır.
ALAN_KATEGORISI = {
    "advocacy-legal": "dava", "litigation-legal": "dava", "expert-opinion": "dava", "criminal-defense": "dava",
    "administrative-legal": "idare", "regulatory-legal": "idare",
    "commercial-legal": "sozlesme", "contract-drafting": "sozlesme",
    "corporate-legal": "sirket", "employment-legal": "is", "ip-legal": "fsmh", "privacy-legal": "kvkk",
    "tax-legal": "vergi", "energy-finance": "enerji", "firm-operations": "buro", "legal-research": "arastirma",
}
KATEGORI_ADI = {   # beceri adı, arthurlegal- önekli: ~/.codex/skills ortak klasördür, "vergi" gibi ad çakışmasın
    "dava": "arthurlegal-dava-ve-dilekce", "idare": "arthurlegal-idare-ve-duzenleyici-kurumlar", "sozlesme": "arthurlegal-sozlesme",
    "sirket": "arthurlegal-sirketler-ve-birlesme", "is": "arthurlegal-is-hukuku", "fsmh": "arthurlegal-fikri-mulkiyet", "kvkk": "arthurlegal-kisisel-veriler",
    "vergi": "arthurlegal-vergi", "enerji": "arthurlegal-enerji-ve-proje-finansmani", "buro": "arthurlegal-buro-isleri", "arastirma": "arthurlegal-arastirma-ve-atif",
}

# SYSTEM_PROMPT tam uç (/mcp) için yazılmıştır; OpenAI profilinde olmayan araçlar burada söylenir. Her kalıp metinde
# birebir bir kez bulunmalı: talimat değişip kalıp tutmazsa üretim durur.
KONUMSUZ = ("`tkgm_konumdan_parsel`, `tkgm_yer_bul`, `tkgm_koordinat_donustur`, `tkgm_koridor_kesisim`, "
            "`tkgm_parsel_oku`")
OPENAI_UYARLAMALARI: List[Tuple[str, str]] = [
    ("`https://arthurlegal-mcp.fly.dev/mcp`, auth yok, 132 araç, 17 önek.",
     "`%s` (bu paketin bağlantısı, OpenAI profili), auth yok; tam uçtaki %s ve `tr_resmi_gazete_ek_sayfa` bu "
     "profilde yoktur, `tkgm_parsel_sorgula`, `tkgm_parsel_raporu` ve `tkgm_baglanti` konum ya da serbest metin "
     "almaz (parsel il/ilçe/mahalle/ada/parsel ile bulunur)." % (MCP_URL, KONUMSUZ)),
    ("`tr_` 24 (bölüm 7)", "`tr_` 23 (bölüm 7; `tr_resmi_gazete_ek_sayfa` bu profilde yok)"),
    ("`tr_resmi_gazete_ek_sayfa` (`url`, `sayfa`: ek PDF'inin tek sayfası, tarife ve cetveller için; taranmış sayfa "
     "görüntü döner)",
     "`tr_resmi_gazete_ek_sayfa` (`url`, `sayfa`: ek PDF'inin tek sayfası, tarife ve cetveller için; taranmış sayfa "
     "görüntü döner; yalnız masaüstü kurulumunun yerel sunucusunda, bu bağlantıda yoktur: ekin bağlantısını ver, "
     "içeriğini yazma)"),
    ("16. `tkgm_`: ",
     "16. `tkgm_` (bu bağlantıda konum, adres ya da geometri alan araçlar yoktur: %s; parseli il/ilçe/mahalle/ada/"
     "parsel ile sorgula): " % KONUMSUZ),
]

# Claude'a özgü yollar ve adlar, sırayla (uzun kalıp önce). Pratik profili ve çalışma alanları Hafıza notudur (K26).
NOTR: List[Tuple[str, str]] = [
    (r"~/\.claude/plugins/cache/claude-for-legal/[a-z0-9-]+/\*/CLAUDE\.md", KURAL_YOLU + "profiles/"),
    (r"~/\.claude/plugins/config/claude-for-legal/firm-profile\.md", KURAL_YOLU + "firm-profile.md"),
    (r"~/\.claude/plugins/config/claude-for-legal/([a-z0-9-]+)/", r"Hafıza › Pratik/\1/"),
    (r"~/\.claude/plugins/config/claude-for-legal/?", "Hafıza › Pratik/"),
    (r"~/\.claude/[^\s)`\"'\]]*", "Hafıza › Pratik/"),
    (r"\.claude/plugins/config/claude-for-legal/([a-z0-9-]+)/", r"Hafıza › Pratik/\1/"),
    (r"CLAUDE\.md", "PROFIL.md"),
    (r"\$\{CLAUDE_PLUGIN_ROOT\}/", ""),
    (r"claude-for-legal", "kaynak eklenti"),
    (r"WebFetch", "web erişimi"),
    (r"Claude Desktop'taki", "masaüstü uygulamasındaki"), (r"Claude Desktop'tan", "masaüstü uygulamasından"),
    (r"Claude Desktop'ta", "masaüstü uygulamasında"), (r"Claude Desktop'un", "masaüstü uygulamasının"),
    (r"Claude Desktop'u", "masaüstü uygulamasını"), (r"Claude Desktop'a", "masaüstü uygulamasına"),
    (r"Claude Desktop", "masaüstü uygulaması"),
    (r"Claude Code'da", "masaüstü uygulamasında"), (r"Claude Code'un", "masaüstü uygulamasının"),
    (r"Claude Code", "masaüstü uygulaması"), (r"Cowork", "masaüstü uygulaması"),
    (r"claude\.ai/download", "masaüstü uygulamasının indirme sayfası"),
    (r"claude\.ai/[^\s)`\"'\]]*", "sohbet uygulaması"),
    (r"claude\.ai'deki", "sohbet uygulamasındaki"), (r"claude\.ai'den", "sohbet uygulamasından"),
    (r"claude\.ai'de", "sohbet uygulamasında"), (r"claude\.ai'nin", "sohbet uygulamasının"),
    (r"claude\.ai'ye", "sohbet uygulamasına"), (r"claude\.ai", "sohbet uygulaması"),
    (r"Anthropic'in", "yapay zekâ sağlayıcısının"), (r"Anthropic'ten", "yapay zekâ sağlayıcısından"),
    (r"Anthropic'e", "yapay zekâ sağlayıcısına"), (r"Anthropic's", "the AI provider's"),
    (r"Anthropic", "yapay zekâ sağlayıcısı"),
    (r"Claude'undur", "modelindir"), (r"Claude'daki", "modeldeki"), (r"Claude'dan", "modelden"),
    (r"Claude'da", "modelde"), (r"Claude'un", "modelin"), (r"Claude'la", "modelle"), (r"Claude'u", "modeli"),
    (r"Claude'a", "modele"), (r"Claude's", "the model's"), (r"Claude(?!\w)", "model"), (r"claude(?!\w)", "model"),
]
_NOTR = [(re.compile(d), y) for d, y in NOTR]
# Çıktıda kalmaması gereken izler (lisans ve atıf dosyaları hariç: üçüncü taraf lisansı aynen kalır).
IZ = re.compile(r"[Cc]laude|CLAUDE|WebFetch|Cowork|Anthropic")
IZ_SERBEST = {"LICENSE", "LICENSE-APACHE-2.0-THIRD-PARTY.txt", "ATTRIBUTION.md"}


class EklentiHata(EK.EklentiHata):
    pass


def notrle(metin: str) -> str:
    for desen, yeni in _NOTR:
        metin = desen.sub(yeni, metin)
    return metin


def openai_uyarla(metin: str) -> str:
    for eski, yeni in OPENAI_UYARLAMALARI:
        if metin.count(eski) != 1:
            raise EklentiHata("OpenAI uyarlaması tutmadı (%d eşleşme): %s" % (metin.count(eski), eski[:70]))
        metin = metin.replace(eski, yeni)
    return metin


def akislar() -> dict:
    return json.loads(AKISLAR.read_text(encoding="utf-8"))


def _becerinin_alani(ad: str, akis_alani: Dict[str, str]) -> str:
    if ad in akis_alani:
        return akis_alani[ad]
    alan = next((a for a in sorted(ALAN_KATEGORISI, key=len, reverse=True) if ad.startswith(a + "-")), None)
    if alan is None:
        raise EklentiHata("becerinin alanı bulunamadı: %s" % ad)
    return ALAN_KATEGORISI[alan]


def _komutlar(metin: str, adlar: set, beceri_alani: Dict[str, str]) -> str:
    """`/<alan>:<skill>` komutları ChatGPT'de yoktur: alan becerisinin başvuru dosyasına çevrilir."""
    def degistir(m: re.Match) -> str:
        ad = "%s-%s" % (m.group(1), m.group(2))
        if ad not in adlar:
            return m.group(0)
        alan = KATEGORI_ADI[beceri_alani[ad]]
        return "`%s` iş akışı (`%s` becerisi, `../%s/references/%s.md`)" % (ad, alan, alan, ad)
    return EK.KOMUT.sub(degistir, metin)


def _yollar(metin: str, rehberler: set) -> str:
    """Rehber, profil ve büro profili kural becerisinin references/ klasöründedir (becerinin klasörüne göre yol)."""
    metin = metin.replace("knowledge/firm-profile.md", KURAL_YOLU + "firm-profile.md")
    metin = metin.replace("knowledge/profiles/", KURAL_YOLU + "profiles/").replace("](../profiles/", "](profiles/")
    return EK.REHBER.sub(lambda m: KURAL_YOLU + m.group(1) if m.group(1) in rehberler else m.group(0), metin)


def metin_uyarla(metin: str, adlar: set, rehberler: set, beceri_alani: Dict[str, str]) -> str:
    return notrle(_yollar(_komutlar(EK.anahtarsiz(metin), adlar, beceri_alani), rehberler))


KURAL_ACIKLAMASI = (
    "ArthurLegal'in çalışma kuralları: Türk hukuku odaklı hukuk asistanının yazım biçimi, kanun maddesi ve karar "
    "künyesi doğrulama kapıları, canlı veri çekilemediğinde UYARI satırı, 11 iş alanının haritası ve ArthurLegal "
    "Masası. Kullanıcı \"ArthurLegal Masası'nı aç\" ya da \"masayı aç\" derse masayı al_masasi ile açar (bu bilgisayarda "
    "kuruluysa arthurlegal-yerel MCP sunucusundaki). Türk hukukuyla "
    "ilgili her soruda ve ArthurLegal alan becerilerinden biri çalışmadan önce yüklenir. Working rules of the "
    "ArthurLegal legal assistant (Turkish law first); load before any legal task."
)


def kural_becerisi(sistem: str, surum: str, adlar: set, rehberler: set, beceri_alani: Dict[str, str],
                   kategoriler: List[dict]) -> str:
    govde = sistem.split("\n---\n", 1)[1] if "\n---\n" in sistem else sistem
    alanlar = "\n".join("   - `%s`: %s (%s)" % (KATEGORI_ADI[k["id"]], k["tr"], k["en"]) for k in kategoriler)
    on = f"""---
name: {AD}
description: >-
  {KURAL_ACIKLAMASI}
---

# ArthurLegal: çalışma kuralları (Law Firm paketi {surum})

Aşağıdaki metin ArthurLegal Law Firm paketinin sistem talimatıdır; her hukuki işte eksiksiz uygulanır. Kullanıcının
açık talimatı bu kurallardan önce gelir; bir kural kullanıcının istediğiyle çelişirse kullanıcıya sor. Bu paketteki
farklar şunlardır:

1. **ArthurLegal Masası.** Kullanıcı "ArthurLegal Masası'nı aç", "masayı aç" ya da bir modülün adını (Mevzuat, İçtihat,
   ArthurTapu, Beyin, ArthurMask, UYAP Dashboard, Donna) söylerse masayı `al_masasi` aracıyla aç. Bu bilgisayarda
   ArthurLegal kuruluysa araç `arthurlegal-yerel` MCP sunucusundadır (araçları kod çalıştırarak çağırıyorsan adı
   `mcp__arthurlegal_yerel__al_masasi`): önce onu çağır; kurulum yoksa ArthurLegal bağlantısının `al_masasi`'sini.
   Aracı araç listende aramadan kullanıcıya bağlantıları ya da MCP'leri kontrol etmesini söyleme; kabuk komutu ya da
   tarayıcı kullanma. Masa açıldıktan sonra her soruda: önce `al_masada_basla`, sonra araştırma, en son cevabın
   tamamıyla `al_masaya_yaz`; sohbete yalnız "Cevap masada." yaz.
2. **İş alanları.** Metinde "knowledge" diye geçen birleşik skill dosyalarının her bölümü bu pakette bir iş akışıdır ve
   kendi alan becerisinin `references/<iş-akışı>.md` dosyasındadır:
{alanlar}
   Rehberler `{KURAL_YOLU}`, pratik profilleri `{KURAL_YOLU}profiles/`, büro profili
   `{KURAL_YOLU}firm-profile.md` dosyasındadır. Bu paketteki bütün dosya yolları becerinin kendi klasörüne göredir
   (`../arthurlegal/references/` her beceriden kural becerisinin başvuru klasörüdür). Okumadığın dosyanın içeriğini
   varsayma.
3. **Hafıza (pratik profili ve dosya çalışma alanları).** Metinde `Hafıza › <yol>` diye geçen dosya ArthurLegal Hafıza
   kasasındaki nottur (`Hafıza › Pratik/<alan>/PROFIL.md` pratik profili, `matters/` altı dosya çalışma alanları):
   okumak için `hafiza_getir(yol="Pratik/...")`, aramak ve listelemek için `hafiza_ara`, yazmak için kullanıcının
   onayıyla `hafiza_yaz`. Hafıza yalnız maskeli metin kabul eder: müvekkil adı yerine dosya kodu ya da ArthurMask
   etiketi yaz. Hafıza araçları yoksa (web, telefon ya da kurulumda Hafıza seçilmemiş) bilgiyi kullanıcıya sor, hiçbir
   yere yazma ve kaydedilmemiş bir şeyi kaydedilmiş sayma.
4. **Araçlar.** Bu bilgisayarda ArthurLegal kuruluysa (`arthurlegal-yerel` MCP sunucusu) araştırma araçları (`tr_`,
   `az_`, `eu_`, `uk_` ... önekli), `status`, `hesap_` hesap kartları, tapu araçları ve ArthurLegal Masası oradadır;
   önce onu kullan. Kurulum yoksa (web, telefon) aynı araçlar bu paketin ArthurLegal bağlantısından gelir ({MCP_URL});
   bu bağlantıda konum, adres ya da geometri alan tapu araçları ve `tr_resmi_gazete_ek_sayfa` yoktur.
5. **UYAP, ArthurMask, yerel tapu.** Yalnız ArthurLegal masaüstü kurulumunda çalışır. Kurulu değilse UYAP verisi
   uydurulmaz (`UYARI: veri çekilemedi, teyidiniz gerekli: https://avukat.uyap.gov.tr/`), müvekkil belgesi sohbete
   doğrudan yapıştırılmışsa kullanıcı ArthurMask'e yönlendirilir.
6. **Model.** ChatGPT modelleriyle henüz ölçüm yapmadık; en yetenekli güncel modeli seçmenizi tavsiye ederiz,
   bağlayıcı değildir. Aşağıdaki metinde geçen model ve effort tavsiyesi başka bir ortamın ölçümüdür; bu pakette
   kullanıcıya söyleme.

---

"""
    return on + metin_uyarla(openai_uyarla(govde.strip()), adlar, rehberler, beceri_alani) + "\n"


def is_akisi_dosyasi(ad: str, govde: str, alan_notu: str, adlar: set, rehberler: set,
                     beceri_alani: Dict[str, str]) -> Tuple[str, str]:
    """İş akışının başvuru dosyası ve kısa açıklaması: ön bilgi başlığa döner (yalnız SKILL.md beceridir)."""
    m = EK.ONBILGI.match(govde)
    if not m:
        raise EklentiHata("%s bölümünde ön bilgi (---) yok" % ad)
    aciklama = ""
    d = re.search(r"(?ms)^description:\s*(?:>-?\s*\n)?(.*?)(?=^\w[\w-]*:|\Z)", m.group(1))
    if d:
        aciklama = " ".join(s.strip() for s in d.group(1).strip().splitlines()).strip().strip('"')
    metin = "# %s\n\n%s\n\n%s" % (ad, aciklama, govde[m.end():].strip())
    if alan_notu:
        metin += "\n\n---\n\n" + alan_notu
    return metin_uyarla(metin, adlar, rehberler, beceri_alani).rstrip() + "\n", notrle(aciklama)


def _kisa(metin: str, n: int) -> str:
    metin = re.sub(r"\s+", " ", metin).strip()
    return metin if len(metin) <= n else metin[: n - 1].rsplit(" ", 1)[0] + "…"


def alan_becerisi(kategori: dict, isler: List[Tuple[str, str, str]], yardimcilar: List[Tuple[str, str]]) -> str:
    """isler: (ad, başlık, ne işe yarar); yardimcilar: (ad, açıklama)."""
    ad = KATEGORI_ADI[kategori["id"]]
    basliklar = ", ".join(b for _, b, _ in isler)
    aciklama = _kisa("ArthurLegal %s (%s): %s. Bu alanda bir iş istendiğinde kullanılır; adımlar references/ "
                     "dosyalarındadır." % (kategori["tr"], kategori["en"], basliklar), 600)
    satirlar = "\n".join("| %s | %s | `references/%s.md` |" % (b, n.replace("|", "/"), a) for a, b, n in isler)
    yardim = "\n".join("- `references/%s.md`: %s" % (a, _kisa(n, 180).replace("\n", " ")) for a, n in yardimcilar)
    return f"""---
name: {ad}
description: >-
  {aciklama}
---

# {kategori["tr"]} ({kategori["en"]})

ArthurLegal'in bu alandaki iş akışları. Önce `{AD}` kural becerisini uygula (atıf doğrulama, UYARI satırı, masa).
İstenen işe uyan iş akışını aşağıdan seç, dosyasını oku ve adımlarını izle; okumadığın dosyanın içeriğini varsayma.
Kullanıcının açık talimatı iş akışından önce gelir.

| İş akışı | Ne işe yarar | Dosya |
|---|---|---|
{satirlar}
""" + ("""
## Kurulum ve çalışma alanı

Bu alanın pratik profili, ayarı ve dosya çalışma alanı işleri (kural becerisinin 3. maddesi: Hafıza):

%s
""" % yardim if yardim else "")


def uret(kok: Path = KOK, surum: Optional[str] = None) -> Dict[str, bytes]:
    paket, paket_surumu = EK.paket_dizini(kok)
    surum = surum or mevcut_surum(kok) or paket_surumu
    knowledge = paket / "knowledge"
    beceriler, notlar = EK.becerilere_ayir(knowledge)
    adlar = {"%s-%s" % (a, s) for a, s, _ in beceriler}
    rehberler = {p.name for p in (knowledge / "references").glob("*.md")} - set(EK.ANAHTARLI_REHBER)
    veri = akislar()
    kategoriler = veri["kategoriler"]
    akis = {a["id"]: a for a in veri["akislar"]}
    eksik = sorted(set(akis) - adlar)
    if eksik:
        raise EklentiHata("İş akışları dosyasında pakette olmayan beceri: %s" % ", ".join(eksik[:5]))
    beceri_alani = {ad: _becerinin_alani(ad, {k: v["k"] for k, v in akis.items()}) for ad in adlar}

    dosyalar: Dict[str, str] = {}
    dosyalar["skills/%s/SKILL.md" % AD] = kural_becerisi(EK._oku(paket / "SYSTEM_PROMPT.md"), paket_surumu, adlar,
                                                         rehberler, beceri_alani, kategoriler)
    for p in sorted((knowledge / "references").glob("*.md")):
        if p.name in rehberler:
            dosyalar[KURAL_DOSYASI + p.name] = metin_uyarla(EK._oku(p), adlar, rehberler, beceri_alani)
    for p in sorted((knowledge / "profiles").glob("*.md")):
        dosyalar[KURAL_DOSYASI + "profiles/" + p.name] = metin_uyarla(EK._oku(p), adlar, rehberler, beceri_alani)
    dosyalar[KURAL_DOSYASI + "firm-profile.md"] = metin_uyarla(EK._oku(knowledge / "firm-profile.md"), adlar, rehberler,
                                                            beceri_alani)
    isler: Dict[str, List[Tuple[str, str, str]]] = {k["id"]: [] for k in kategoriler}
    yardimcilar: Dict[str, List[Tuple[str, str]]] = {k["id"]: [] for k in kategoriler}
    for alan, skill, govde in beceriler:
        ad = "%s-%s" % (alan, skill)
        kat = beceri_alani[ad]
        metin, aciklama = is_akisi_dosyasi(ad, govde, notlar.get(alan, ""), adlar, rehberler, beceri_alani)
        dosyalar["skills/%s/references/%s.md" % (KATEGORI_ADI[kat], ad)] = metin
        if ad in akis:
            baslik, ne = akis[ad]["tr"]
            isler[kat].append((ad, baslik, ne))
        else:
            yardimcilar[kat].append((ad, aciklama))
    sira = {a["id"]: i for i, a in enumerate(veri["akislar"])}
    for k in kategoriler:
        dosyalar["skills/%s/SKILL.md" % KATEGORI_ADI[k["id"]]] = alan_becerisi(
            k, sorted(isler[k["id"]], key=lambda x: sira[x[0]]), sorted(yardimcilar[k["id"]]))

    manifest = {
        "$schema": SEMA_EKLENTI,
        "name": AD,
        "version": surum,
        "description": ("Turkish-law-first legal assistant for lawyers in Türkiye: %d workflows in 11 practice areas, "
                        "with citations checked against the official text through ArthurLegal MCP (%d jurisdictions)."
                        % (len(akis), EK.YARGI_CEVRESI)),
        "author": {"name": "ArthurLegal", "url": EK.DEPO},
        "homepage": EK.DEPO + "/tree/main/" + CIKTI,
        "repository": EK.DEPO,
        "license": "SEE LICENSE IN LICENSE",
        "keywords": ["legal", "law-firm", "turkish-law", "citations", "kvkk", "contracts"],
        "extensions": {"com.openai": {"interface": {
            "displayName": "ArthurLegal",
            "shortDescription": "Turkish legal research with citations checked against the official text",
            "longDescription": ("Legislation, case law and regulator decisions from official sources in twelve "
                                "jurisdictions, Turkish first; %d law-firm workflows in 11 practice areas; the "
                                "ArthurLegal desk shows the question, every research step and the answer with its "
                                "citations checked. Free and open source for lawyers in Türkiye." % len(akis)),
            "developerName": "ArthurLegal",
            "websiteURL": EK.DEPO,
            "privacyPolicyURL": EK.GIZLILIK,
            "defaultPrompt": ["ArthurLegal Masası'nı aç", "TBK m. 49'un başlığı ve ilk cümlesi nedir?"],
            "brandColor": LACIVERT,
            "composerIcon": "./assets/icon.png",
            "logo": "./assets/logo.png",
        }}},
    }
    dosyalar["plugin.json"] = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    dosyalar["mcp.json"] = json.dumps({"$schema": SEMA_MCP, "mcpServers": {AD: {
        "type": "streamable-http", "url": MCP_URL,
        "extensions": {"com.openai": {"auth": {"type": "none"}}}}}}, indent=2) + "\n"
    dosyalar["README.md"] = readme(surum, paket_surumu, len(akis), len(beceriler) - len(akis), kategoriler)
    dosyalar["LICENSE"] = EK._oku(kok / "LICENSE")
    dosyalar["LICENSE-APACHE-2.0-THIRD-PARTY.txt"] = EK._oku(paket / "LICENSE-APACHE-2.0-THIRD-PARTY.txt")
    dosyalar["ATTRIBUTION.md"] = EK._oku(paket / "ATTRIBUTION.md")

    izler = ["%s: …%s…" % (yol, metin[max(0, m.start() - 40): m.end() + 40].replace("\n", " "))
             for yol, metin in dosyalar.items() if yol not in IZ_SERBEST for m in IZ.finditer(metin)]
    if izler:
        raise EklentiHata("Claude izi kaldı (%d):\n  %s" % (len(izler), "\n  ".join(izler[:40])))
    cikti = {yol: metin.encode("utf-8") for yol, metin in dosyalar.items()}
    png = EK._simge_png()
    cikti["assets/logo.png"] = png
    cikti["assets/icon.png"] = png
    return cikti


def readme(surum: str, paket_surumu: str, is_sayisi: int, yardimci: int, kategoriler: List[dict]) -> str:
    alanlar = "\n".join("- `%s`: %s" % (KATEGORI_ADI[k["id"]], k["en"]) for k in kategoriler)
    return f"""# ArthurLegal plugin (ChatGPT)

ArthurLegal is a Turkish-law-first legal assistant for lawyers in Türkiye. This plugin brings its working rules,
{is_sayisi} law-firm workflows and {yardimci} setup helpers to ChatGPT as 12 skills (one rule skill and 11 practice
areas), connected to ArthurLegal MCP at `{MCP_URL}`.

**Status:** the ArthurLegal installer (v3.4.0 and later) installs these 12 skills in the ChatGPT desktop app, together
with the local ArthurLegal servers, when ChatGPT is chosen during setup. The plugin is not yet published in the ChatGPT
plugin directory, and ChatGPT on the web and on a phone is in preparation. It is generated from the same package as
ArthurLegal's other plugin, so the two stay in step.

Version {surum}, generated from the ArthurLegal Law Firm package {paket_surumu} by
`ArthurLegal-setup/yayin/openai_eklenti_uret.py`. Do not edit this folder by hand.

ChatGPT and OpenAI are trademarks of OpenAI.

## Skills

- `arthurlegal`: working rules, citation checks, the warning line for unreachable sources, the ArthurLegal desk.
{alanlar}

Each practice-area skill lists its workflows; the full steps are in that skill's `references/` folder.

## Notes

- Free and open source for lawyers in Türkiye; non-commercial use. See `LICENSE`.
- Land-registry tools that take coordinates, an address or a geometry file are not on this connection; parcels are
  found by province, district, neighbourhood, block and parcel.
- UYAP, ArthurMask and ArthurLegal Memory run only with the ArthurLegal desktop install.
- Outputs are drafts for review by a lawyer.
"""


def mevcut_surum(kok: Path = KOK) -> Optional[str]:
    yol = kok / CIKTI / "plugin.json"
    return json.loads(yol.read_text(encoding="utf-8"))["version"] if yol.exists() else None


def _farklar(hedef: Path, beklenen: Dict[str, bytes]) -> List[str]:
    sorunlar = []
    mevcut = {p.relative_to(hedef).as_posix() for p in hedef.rglob("*") if p.is_file()} if hedef.exists() else set()
    for yol in sorted(set(beklenen) - mevcut):
        sorunlar.append("eksik: %s/%s" % (CIKTI, yol))
    for yol in sorted(mevcut - set(beklenen)):
        sorunlar.append("fazla: %s/%s" % (CIKTI, yol))
    for yol in sorted(set(beklenen) & mevcut):
        if EK._normal(yol, (hedef / yol).read_bytes()) != EK._normal(yol, beklenen[yol]):
            sorunlar.append("paketten farklı: %s/%s" % (CIKTI, yol))
    return sorunlar


def denetle(kok: Path = KOK) -> List[str]:
    return _farklar(kok / CIKTI, uret(kok))


def surum_denetle(taban: str, kok: Path = KOK) -> List[str]:
    def git(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", "-C", str(kok), *args], capture_output=True)

    if git("rev-parse", "--verify", "--quiet", taban + "^{commit}").returncode:
        raise EklentiHata("taban commit okunamadı: %s" % taban)
    eski = git("show", "%s:%s/plugin.json" % (taban, CIKTI))
    if eski.returncode:
        return []
    fark = git("diff", "--quiet", taban, "--", CIKTI).returncode
    if fark not in (0, 1):
        raise EklentiHata("git diff çalışmadı: %s" % taban)
    if fark == 0 and not git("ls-files", "--others", "--exclude-standard", "--", CIKTI).stdout.strip():
        return []
    e, y = json.loads(eski.stdout)["version"], mevcut_surum(kok)
    if y is None or EK._sayi(y) <= EK._sayi(e):
        return ["ChatGPT eklentisi %s'e göre değişti ama sürümü artmadı (%s → %s); "
                "`python ArthurLegal-setup/yayin/openai_eklenti_uret.py` sürümü kendisi artırır" % (taban[:12], e, y)]
    return []


def yaz(kok: Path = KOK) -> Tuple[int, str]:
    hedef = kok / CIKTI
    dosyalar = uret(kok)
    eski = mevcut_surum(kok)
    if eski and _farklar(hedef, dosyalar):
        dosyalar = uret(kok, EK.yeni_surum(eski, EK.paket_dizini(kok)[1]))
    if hedef.exists():
        shutil.rmtree(hedef)
    for yol, veri in dosyalar.items():
        dosya = hedef / yol
        dosya.parent.mkdir(parents=True, exist_ok=True)
        dosya.write_bytes(veri)
    return len(dosyalar), json.loads(dosyalar["plugin.json"])["version"]


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--denetle", action="store_true", help="yalnız denetle, yazma")
    ap.add_argument("--taban", metavar="REF", help="--denetle ile: eklenti bu commit'tekinden farklıysa sürümü artmış mı")
    a = ap.parse_args(argv)
    try:
        if a.denetle:
            sorunlar = denetle() + (surum_denetle(a.taban) if a.taban else [])
            for s in sorunlar:
                print(s)
            print("ChatGPT eklentisi: " + ("paketle aynı, sürüm %s" % mevcut_surum() if not sorunlar
                                          else "%d sorun" % len(sorunlar)))
            return 1 if sorunlar else 0
        sayi, surum = yaz()
        print("yazılan dosya: %d (%s/), sürüm %s" % (sayi, CIKTI, surum))
        return 0
    except EK.EklentiHata as e:
        print("hata: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
