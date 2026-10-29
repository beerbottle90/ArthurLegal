#!/usr/bin/env python3
"""Claude eklentisi: Law Firm paketinden Anthropic dizinine gönderilen `ArthurLegal-plugin/` klasörünü üretir.

Kaynak, depodaki güncel `ArthurLegal-Law-Firm-v*-Public-Release` paketidir. SYSTEM_PROMPT ana beceri olur
(`/arthurlegal:arthurlegal`), birleşik skill dosyalarındaki her `## /<alan>:<skill>` bölümü kendi becerisine ayrılır
(`/arthurlegal:<alan>-<skill>`), rehberler, profiller ve büro profili `references/` altına girer. Eklenti klasörü
elle düzenlenmez: paket değişince bu betik çalıştırılır ve çıktı commitlenir; elle yapılan değişiklik testte yakalanır.

    python yayin/eklenti_uret.py             klasörü paketten yeniden üret
    python yayin/eklenti_uret.py --denetle   yalnız denetle: klasör paketten farklıysa 1 ile çık

Eklenti, Claude dizinindeki ArthurLegal MCP profiline (`/directory/mcp`) bağlanır. Tapu (`arthur-tapu`), UYAP
(`arthur-uyap`) ve Arthur Mask masaüstü kurulumun yerel modülleridir: eklenti onları taşımaz, ana beceri kuruluysa
onlara yönlendirir (yerel kurulumun `arthurlegal_talimat` kurallarıyla aynı). Yalnız standart kütüphane.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple

KOK = Path(__file__).resolve().parents[2]
CIKTI = "ArthurLegal-plugin"
AD = "arthurlegal"
MCP_URL = "https://arthurlegal-mcp.fly.dev/directory/mcp"
DEPO = "https://github.com/beerbottle90/ArthurLegal"
GIZLILIK = "https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md"
DESTEK_EPOSTA = "ertug@datsproject.io"

PAKET = re.compile(r"^ArthurLegal-Law-Firm-v(\d+\.\d+\.\d+)-Public-Release$")
BOLUM = re.compile(r"(?m)^## /([a-z0-9-]+):([a-z0-9-]+)\n")
KOMUT = re.compile(r"/([a-z]+(?:-[a-z]+)*):([a-z0-9]+(?:-[a-z0-9]+)*)")
ONBILGI = re.compile(r"\A\s*---\n(.*?)\n---\n", re.S)
REHBER = re.compile(r"(?<![\w/$}])(?:knowledge/)?references/([\w.-]+\.md)")
IKILI = {".png"}

# Kullanıcının makinesindeki bir API anahtarını okuyup dış bir hizmete gönderen rehber eklentiye girmez (dizin bunu
# "credential leaving the machine" diye bekletir); Projects paketinde kalabilirler. Rehbere yapılan atıf, varsa aynı
# işi anahtarsız yapan rehbere döner, yoksa rehberin eklentide olmadığı yazılır. Anahtarı anan satırlar da düşer.
ANAHTARLI_REHBER = {
    "us-legislation-rehberi.md": None,
}
KIMLIK = re.compile(r"\b[A-Z][A-Z0-9]*_(?:API_KEY|TOKEN|SECRET)\b")
SERBEST_KIMLIK = {"EMBEDDINGS_API_KEY", "OPENALEX_API_KEY"}   # sunucu tarafı ya da isteğe bağlı; kullanıcıdan istenmez


class EklentiHata(Exception):
    pass


def paket_dizini(kok: Path = KOK) -> Tuple[Path, str]:
    bulunan = [(p, m.group(1)) for p in kok.iterdir() if p.is_dir() for m in [PAKET.match(p.name)] if m]
    if len(bulunan) != 1:
        raise EklentiHata("depoda tek bir güncel Law Firm paketi bekleniyordu, bulunan: %d" % len(bulunan))
    return bulunan[0]


def _oku(yol: Path) -> str:
    return yol.read_text(encoding="utf-8").lstrip("﻿").replace("\r\n", "\n")


def becerilere_ayir(knowledge: Path) -> Tuple[List[Tuple[str, str, str]], Dict[str, str]]:
    """(alan, skill, bölüm metni) listesi ve alan başına ortak not (skill dosyasının içindekilerden sonraki kısmı)."""
    beceriler, notlar = [], {}
    for dosya in sorted((knowledge / "skills").glob("*__skills.md")):
        alan = dosya.name.split("__")[0]
        parcalar = BOLUM.split(_oku(dosya))
        on = parcalar[0].split("\n---\n", 1)
        notlar[alan] = on[1].strip().strip("-").strip() if len(on) == 2 else ""
        for i in range(1, len(parcalar), 3):
            if parcalar[i] != alan:
                raise EklentiHata("%s içinde başka alanın bölümü: /%s:%s" % (dosya.name, parcalar[i], parcalar[i + 1]))
            govde = re.sub(r"\n-{3,}\s*\Z", "", parcalar[i + 2].rstrip())
            beceriler.append((alan, parcalar[i + 1], govde.strip() + "\n"))
    return beceriler, notlar


def anahtarsiz(metin: str) -> str:
    """Anahtarlı rehberlere atfı yönlendirir, kullanıcı anahtarını anan satırları atar."""
    for rehber, yerine in ANAHTARLI_REHBER.items():
        kalip = re.compile(r"(?:\$\{CLAUDE_PLUGIN_ROOT\}/|knowledge/)?(?:references/)?" + re.escape(rehber))
        metin = kalip.sub(yerine or (rehber + " (bu eklentide yok: kullanıcı API anahtarı ister)"), metin)
    return "\n".join(s for s in metin.split("\n")
                     if not (set(KIMLIK.findall(s)) - SERBEST_KIMLIK))


def _komutlar(metin: str, adlar: set) -> str:
    def degistir(m: re.Match) -> str:
        yeni = "%s-%s" % (m.group(1), m.group(2))
        return "/%s:%s" % (AD, yeni) if yeni in adlar else m.group(0)
    return KOMUT.sub(degistir, metin)


def beceri_metni(metin: str, adlar: set, rehberler: set) -> str:
    """Beceri gövdesi: komutlar eklenti adına, knowledge yolları eklenti köküne (Claude Code gövdede çözer)."""
    metin = _komutlar(anahtarsiz(metin), adlar)
    metin = metin.replace("knowledge/firm-profile.md", "${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md")
    metin = metin.replace("knowledge/profiles/", "${CLAUDE_PLUGIN_ROOT}/references/profiles/")
    return REHBER.sub(lambda m: "${CLAUDE_PLUGIN_ROOT}/references/" + m.group(1) if m.group(1) in rehberler
                      else m.group(0), metin)


def rehber_metni(metin: str, adlar: set) -> str:
    """Rehberler düz dosyadır, gövdede değişken çözülmez: yollar eklenti köküne göre kalır."""
    metin = _komutlar(anahtarsiz(metin), adlar)
    return (metin.replace("knowledge/references/", "references/").replace("knowledge/profiles/", "references/profiles/")
            .replace("knowledge/firm-profile.md", "references/firm-profile.md"))


ANA_ACIKLAMA = (
    "ArthurLegal'in çalışma kuralları: Türk hukuku odaklı hukuk bürosu asistanının yazım biçimi, e-postaya hazır "
    "çıktı iskeleti, kanun maddesi ve karar künyesi doğrulama kapıları, canlı veri çekilemediğinde UYARI satırı, "
    "16 pratik alanın beceri haritası ve Tapu, UYAP, Arthur Mask yönlendirmesi. Türk hukukuyla ilgili her soruda ve "
    "/arthurlegal: becerilerinden biri çalışmadan önce yüklenir. Working rules of the ArthurLegal legal assistant "
    "(Turkish law first); load before any legal task or any other /arthurlegal: skill."
)


def ana_beceri(sistem: str, surum: str, adlar: set, rehberler: set) -> str:
    govde = sistem.split("\n---\n", 1)[1] if "\n---\n" in sistem else sistem
    on = f"""---
name: {AD}
description: >-
  {ANA_ACIKLAMA}
---

# ArthurLegal: çalışma kuralları (Claude eklentisi, Law Firm paketi {surum})

Aşağıdaki metin ArthurLegal Law Firm paketinin sistem talimatıdır; bu eklentide her hukuki işte eksiksiz uygulanır.
Talimat claude.ai Project için yazıldığından bu eklentideki farklar şunlardır:

1. Metinde "knowledge" diye geçen dosyalar bu eklentidedir: birleşik skill dosyalarının her bölümü ayrı bir
   beceridir ve `/{AD}:<alan>-<skill>` adıyla çağrılır (ör. `/{AD}:commercial-legal-nda-review`); rehberler
   `${{CLAUDE_PLUGIN_ROOT}}/references/`, pratik profilleri `${{CLAUDE_PLUGIN_ROOT}}/references/profiles/`, büro profili
   `${{CLAUDE_PLUGIN_ROOT}}/references/firm-profile.md` dosyasındadır. Okumadığın dosyanın içeriğini varsayma.
2. Metinde geçen `~/.claude/plugins/config/...` yolları bu eklentide yoktur; büro bilgisi büro profilindedir. Profil
   doldurulmamışsa varsayım yapma, eksik bilgiyi kullanıcıya sor.
3. Araştırma araçları (`tr_`, `az_`, `eu_`, `uk_` ... önekli) ve `status` eklentinin ArthurLegal MCP bağlantısından
   gelir ({MCP_URL}). ArthurLegal masaüstü kurulumu varsa aynı araçlar yerel `arthurlegal-yerel` sunucusundan da
   gelir; o durumda yerel sunucudakini kullan.
4. Tapu, parsel ve harç işlerinde ArthurLegal kurulumunun yerel `arthur-tapu` araçlarını kullan (`parsel_sorgula`,
   `konumdan_parsel`, `yer_bul`); sohbetteki ilk canlı çağrının onay kartını olduğu gibi göster. `tkgm_` önekli uzak
   araçlar bu eklentide yoktur ve kullanılmaz. `arthur-tapu` kurulu değilse taşınmaz ya da parsel bilgisini uydurma;
   `UYARI: veri çekilemedi, teyidiniz gerekli: https://parselsorgu.tkgm.gov.tr/` yaz.
5. UYAP işleri yalnız ArthurLegal kurulumunun yerel `arthur-uyap` köprüsüyle yapılır (salt okunur, esas numaraları
   etiketli); kuruluysa onun kendi talimatı geçerlidir: son gün hesaplanmaz ve sana gün gelmez. Kurulu değilse UYAP
   verisi uydurulmaz; `UYARI: veri çekilemedi, teyidiniz gerekli: https://avukat.uyap.gov.tr/` yazılır.
6. Arthur Mask için aşağıdaki kurallar geçerlidir; müvekkil belgesi sohbete doğrudan yapıştırılmışsa kullanıcıyı
   Arthur Mask'e yönlendir.

---

"""
    return on + beceri_metni(govde.strip(), adlar, rehberler) + "\n"


def beceri_dosyasi(alan: str, skill: str, govde: str, alan_notu: str, adlar: set, rehberler: set) -> str:
    m = ONBILGI.match(govde)
    if not m:
        raise EklentiHata("/%s:%s bölümünde ön bilgi (---) yok" % (alan, skill))
    onbilgi = re.sub(r"(?m)^name:.*$", "name: %s-%s" % (alan, skill), m.group(1), count=1)
    metin = "---\n%s\n---\n\n%s" % (onbilgi, govde[m.end():].strip())
    if alan_notu:
        metin += "\n\n---\n\n" + alan_notu
    return beceri_metni(metin, adlar, rehberler).rstrip() + "\n"


def readme(surum: str, beceri_sayisi: int, rehber_sayisi: int, alanlar: List[str]) -> str:
    alan_listesi = ", ".join("`%s`" % a for a in alanlar)
    return f"""# ArthurLegal for Claude

ArthurLegal is a Turkish-law-first legal assistant for law firms. This plugin brings its working rules and
{beceri_sayisi} practice skills to Claude: contracts and NDAs, corporate and M&A, employment, KVKK and privacy,
regulatory, intellectual property, litigation and petitions, tax, administrative law, criminal defense, energy and
finance, expert opinions, contract drafting and law firm operations. Statutes and decisions are quoted from the official
text through ArthurLegal MCP, which covers fifteen jurisdictions from Türkiye and the EU to the UK, Germany and Japan.

Plugin version {surum} is the ArthurLegal Law Firm package {surum}. Source: [{DEPO}]({DEPO}).

## What it contains

- **`/{AD}:{AD}`**: the working rules: output format, citation and statute-verification gates, and the `UYARI` line
  that replaces any fact a live source could not return. Claude loads it before any legal task.
- **{beceri_sayisi} practice skills**, called as `/{AD}:<area>-<skill>`, for example
  `/{AD}:commercial-legal-nda-review` or `/{AD}:tax-legal-gib-ozelge-request`. Areas: {alan_listesi}.
- **`references/`**: {rehber_sayisi} guides, practice profiles and a firm profile template that the skills read.
- **One connector: ArthurLegal MCP** (`{MCP_URL}`), read-only legal research with no account.

## What it runs and sends

The plugin contains no scripts, hooks or programs; it is Markdown, one image and one connector declaration. Its only
network connection is ArthurLegal MCP: when Claude calls one of its tools, the tool name and its arguments (search words,
statute and article numbers, decision identifiers) go to that server, which queries the official sources and returns
the result. Interactive views (article card, decision list, the ArthurLegal desk) load the MCP Apps client library from
unpkg.com. What the server stores and for how long is in its [privacy policy]({GIZLILIK}). Do not put client names or
other confidential facts into requests; mask documents on your own computer first with Arthur Mask.

Some skills also ask Claude to use tools the user already has, through Claude and with the user's own permissions; the
plugin installs none of them and sends nothing to them by itself:

- **Claude's web search and web fetch**, for official public sources such as EUR-Lex, legislation.gov.uk, HUDOC, KAP
  and GovInfo (search words and document identifiers).
- **Connectors the user has added**, when they are connected: CourtListener and TR Legal MCP for case law; document
  stores such as Google Drive, Box or iManage; Slack for posting a report the user asked for; DocuSign for sending a
  document for signature after the user approves it.
- **The local ArthurLegal modules** described below (`arthur-tapu`, `arthur-uyap`, Arthur Mask), which run on the
  user's computer.

## Desktop modules (not part of this plugin)

ArthurTapu (land registry), UYAP Dashboard (a read-only bridge to the lawyer's own UYAP account), Arthur Mask and
ArthurLegal Hafıza run on the lawyer's computer and come with the ArthurLegal installer ([download]({DEPO}#download)).
When they are installed, the `{AD}` skill sends land-registry work to `arthur-tapu` and UYAP work to `arthur-uyap`;
when they are not, it says the data could not be retrieved instead of guessing.

## A lawyer stays in charge

Every output is a draft for review by a qualified lawyer and is marked as such. ArthurLegal does not give legal advice,
does not file anything and does not write to UYAP.

## License and support

[LICENSE](LICENSE) (ArthurLegal Proprietary Non-Commercial License). Parts derived from Anthropic's claude-for-legal
are under Apache 2.0: [LICENSE-APACHE-2.0-THIRD-PARTY.txt](LICENSE-APACHE-2.0-THIRD-PARTY.txt),
[ATTRIBUTION.md](ATTRIBUTION.md). Support: [GitHub issues]({DEPO}/issues) or {DESTEK_EPOSTA}.

## Türkçe

ArthurLegal, Türk hukuku odaklı hukuk bürosu asistanıdır. Bu eklenti çalışma kurallarını ve {beceri_sayisi} beceriyi
Claude'a ekler; mevzuat ve kararlar ArthurLegal MCP üzerinden resmî metinden alıntılanır. Tapu, UYAP Dashboard, Arthur
Mask ve ArthurLegal Hafıza bilgisayarınızdaki ArthurLegal kurulumuyla gelir ([indir]({DEPO}#indir)); kuruluysa eklenti
onlara yönlendirir. Çıktılar avukat incelemesi öncesi taslaktır.
"""


def _simge_png() -> bytes:
    yol = KOK / "ArthurLegal-setup" / "varlik" / "simge.py"
    spec = importlib.util.spec_from_file_location("al_simge", yol)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul.simge_png(512)


def uret(kok: Path = KOK) -> Dict[str, bytes]:
    """Eklenti klasörünün tamamı: göreli yol -> içerik."""
    paket, surum = paket_dizini(kok)
    knowledge = paket / "knowledge"
    beceriler, notlar = becerilere_ayir(knowledge)
    adlar = {"%s-%s" % (a, s) for a, s, _ in beceriler}
    if len(adlar) != len(beceriler):
        raise EklentiHata("aynı adlı iki beceri var")
    rehberler = {p.name for p in (knowledge / "references").glob("*.md")} - set(ANAHTARLI_REHBER)

    dosyalar: Dict[str, str] = {}
    dosyalar["skills/%s/SKILL.md" % AD] = ana_beceri(_oku(paket / "SYSTEM_PROMPT.md"), surum, adlar, rehberler)
    for alan, skill, govde in beceriler:
        dosyalar["skills/%s-%s/SKILL.md" % (alan, skill)] = beceri_dosyasi(
            alan, skill, govde, notlar.get(alan, ""), adlar, rehberler)
    for p in sorted((knowledge / "references").glob("*.md")):
        if p.name in rehberler:
            dosyalar["references/" + p.name] = rehber_metni(_oku(p), adlar)
    for p in sorted((knowledge / "profiles").glob("*.md")):
        dosyalar["references/profiles/" + p.name] = rehber_metni(_oku(p), adlar)
    dosyalar["references/firm-profile.md"] = rehber_metni(_oku(knowledge / "firm-profile.md"), adlar)

    manifest = {
        "name": AD,
        "displayName": "ArthurLegal",
        "version": surum,
        "description": ("Turkish-law-first legal assistant for law firms: %d practice skills with citations checked "
                        "against the official text through ArthurLegal MCP (15 jurisdictions)." % len(beceriler)),
        "author": {"name": "ArthurLegal", "url": DEPO},
        "homepage": DEPO + "/tree/main/" + CIKTI,
        "repository": DEPO,
        "keywords": ["legal", "law-firm", "turkish-law", "citations", "kvkk", "contracts"],
        "icon": "./logo.png",
        "documentationUrl": DEPO + "/tree/main/" + CIKTI + "#readme",
        "supportUrl": DEPO + "/issues",
        "privacyPolicyUrl": GIZLILIK,
    }
    dosyalar[".claude-plugin/plugin.json"] = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    dosyalar[".mcp.json"] = json.dumps({"mcpServers": {AD: {"type": "http", "url": MCP_URL}}}, indent=2) + "\n"
    dosyalar["README.md"] = readme(surum, len(beceriler), len(rehberler) + 11, sorted(notlar))
    dosyalar["LICENSE"] = _oku(kok / "LICENSE")
    dosyalar["LICENSE-APACHE-2.0-THIRD-PARTY.txt"] = _oku(paket / "LICENSE-APACHE-2.0-THIRD-PARTY.txt")
    dosyalar["ATTRIBUTION.md"] = _oku(paket / "ATTRIBUTION.md")

    cikti = {yol: metin.encode("utf-8") for yol, metin in dosyalar.items()}
    cikti["logo.png"] = _simge_png()
    return cikti


def _normal(yol: str, veri: bytes) -> bytes:
    return veri if Path(yol).suffix in IKILI else veri.replace(b"\r\n", b"\n")


def denetle(kok: Path = KOK) -> List[str]:
    hedef = kok / CIKTI
    beklenen = uret(kok)
    sorunlar = []
    mevcut = {p.relative_to(hedef).as_posix() for p in hedef.rglob("*") if p.is_file()} if hedef.exists() else set()
    for yol in sorted(set(beklenen) - mevcut):
        sorunlar.append("eksik: %s/%s" % (CIKTI, yol))
    for yol in sorted(mevcut - set(beklenen)):
        sorunlar.append("fazla: %s/%s" % (CIKTI, yol))
    for yol in sorted(set(beklenen) & mevcut):
        if _normal(yol, (hedef / yol).read_bytes()) != _normal(yol, beklenen[yol]):
            sorunlar.append("paketten farklı: %s/%s" % (CIKTI, yol))
    return sorunlar


def yaz(kok: Path = KOK) -> int:
    hedef = kok / CIKTI
    dosyalar = uret(kok)
    if hedef.exists():
        shutil.rmtree(hedef)
    for yol, veri in dosyalar.items():
        dosya = hedef / yol
        dosya.parent.mkdir(parents=True, exist_ok=True)
        dosya.write_bytes(veri)
    return len(dosyalar)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--denetle", action="store_true", help="yalnız denetle, yazma")
    a = ap.parse_args(argv)
    try:
        if a.denetle:
            sorunlar = denetle()
            for s in sorunlar:
                print(s)
            print("eklenti: " + ("paketle aynı" if not sorunlar else "%d sorun" % len(sorunlar)))
            return 1 if sorunlar else 0
        print("yazılan dosya: %d (%s/)" % (yaz(), CIKTI))
        return 0
    except EklentiHata as e:
        print("hata: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
