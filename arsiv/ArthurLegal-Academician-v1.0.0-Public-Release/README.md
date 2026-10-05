# ArthurLegal — Claude Academician Assistant (TR / EN)

**Sürüm:** v1.0.0 · **Tarih:** 2026-07-09 · **Lisans:** Proprietary — Non-Commercial (bkz. [LICENSE](LICENSE))
**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web)

> **v1.0.0 — 8 plugin · 28 skill · 23 referans · 4 agent.** Tam iki dilli (TR + EN),
> Türkiye ve uluslararası akademik rejimleri eşit ağırlıkta kapsar.

> Hukuk **akademisyeni** (araştırma görevlisi → profesör) için araştırma, yazım, atıf
> doğrulama, yayın etiği, tez danışmanlığı ve fon başvurusu asistanı.

---

## Diğer ArthurLegal paketlerinden farkı

| | Corporate / Law-Firm | Courthouse | **Academician** |
|---|---|---|---|
| Kullanıcı | In-house / hukuk bürosu | Hâkim + kalem | **Hukuk akademisyeni** |
| Perspektif | Taraf vekili | Yargısal / tarafsız | **Bilimsel / yazar-merkezli** |
| Amaç | Müvekkil lehine taslak | Gerekçe + usul | **Taslak + atıf doğrulama + etik uyum** |
| Asistanın konumu | Düzenlemenin **öznesine** yardım eder | Aynı | **Asistanın kendisi düzenlemenin nesnesidir** |
| Üst başlık | GİZLİDİR – HUKUK MÜŞAVİRLİĞİ | MAHKEME DAHİLİ ÇALIŞMA NOTU | **AKADEMİK ÇALIŞMA NOTU — TASLAK** |

**Temel fark:** Akademik yayın ve proje süreçlerinde üretken yapay zekâ kullanımı hem
Türkiye'de hem uluslararası düzlemde **doğrudan düzenlenmiştir**. Bu paket, o düzenlemeye
uyumu ürünün merkezine koyar.

---

## 🚪 ÜYZ Kapısı — dört kural

1. **ÜYZ yazar olamaz.** Sorumluluk her zaman insandadır.
   *(COPE 13.02.2023 · ICMJE · WAME · YÖK ÜYZ Etik Rehberi 2024 · TÜBİTAK ÜYZ Rehberi)*
2. **Kullanım beyan edilir.** Her esaslı çıktının sonunda kopyala-yapıştır hazır bir
   **ÜYZ beyan metni** üretilir (araç + sürüm + tarih + kapsam).
3. **Gizli müsvedde yutulmaz.** Değerlendirme altındaki yayımlanmamış müsvedde, proje
   önerisi veya tez metni asistana **girilmez** — gizlilik ihlalidir.
   *(TÜBİTAK ÜYZ Rehberi § 2.2.1 · NIH NOT-OD-23-149 · NSF · Elsevier · Springer Nature · Wiley · ICMJE)*
   → `hakemlik-editorluk` plugin'i **metin okumaz, süreç yürütür.**
4. **Sıfır-halüsinasyon atıf.** Çekilmemiş hiçbir kaynak dipnota giremez. Uydurma dipnot,
   yayın etiği yönergeleri kapsamında **intihal/sahtecilik riskidir**.

---

## Mimari — 8 plugin

| Plugin | Kapsam |
|---|---|
| `arastirma-tasarim` | Araştırma sorusu, literatür haritası, yöntem seçimi, **etik kurul triyajı** |
| `makale-yazim` | Makale iskeleti, dergi seçimi, hakem yanıt mektubu, özet & anahtar kelime |
| `atif-kaynak` | **Atıf doğrulama**, kaynakça üretimi, atıf stili dönüştürme |
| `yayin-etigi` | **ÜYZ beyanı**, etik ihlal triyajı, benzerlik raporu yorumu, yazarlık & CRediT |
| `akademik-yukselme` | Doçentlik puan analizi, dosya eksik analizi, atama kriter kontrolü |
| `proje-fon` | TÜBİTAK başvurusu, AB/Horizon başvurusu, iş paketi kurgusu |
| `tez-danismanlik` | Tez yapısı, savunma hazırlığı, öğrenci geri bildirimi |
| `hakemlik-editorluk` | **Müsvedde almaz.** Hakem rubriği, editör karar mektubu, COPE vaka akışı |

Kullanım: `/<plugin>:<skill>` — örn. `/yayin-etigi:uyz-beyani`

---

## Veri kaynakları

**Bağlı MCP sunucuları**

| Sunucu | Kapsam |
|---|---|
| TR Legal MCP (Mevzuat + Yargı) | TR mevzuat + Yargıtay / Danıştay / AYM / Emsal |
| CourtListener | ABD içtihadı + RECAP (resmî MCP) |
| Fedlex | İsviçre federal mevzuatı |
| OpenCaseLaw.ch | İsviçre içtihadı + doktrin ↔ karar köprüsü |

**Ücretsiz REST (anahtar gerekmez):** Crossref/DOI · OpenAlex · Semantic Scholar · DOAJ ·
ORCID · EUR-Lex · HUDOC

**API'si olmayan (manuel doğrulama zorunlu):** Lexpera · Kazancı · Jurix · Legalbank ·
HeinOnline · Westlaw · LexisNexis · Beck-online

> ⚠️ **Bu paket hiçbir API anahtarı gömmez.**

---

## Kurulum

Türkçe → [KURULUM.md](KURULUM.md) · English → [INSTALLATION.md](INSTALLATION.md)

Özet: Claude.ai Project oluştur → `SYSTEM_PROMPT.md`'yi Custom Instructions'a yapıştır →
`knowledge/` dosyalarını yükle → `akademisyen-profili.md`'yi doldur.

---

## Uyarılar

- Çıktılar **taslaktır**; bilimsel eser, hakem raporu veya akademik değerlendirme yerine geçmez.
- **Benzerlik oranı ≠ intihal.** Evrensel bir yüzde eşiği **yoktur**; eşiği kurumunuz belirler.
- **Doçentlik ölçütleri dönemden döneme değişir.** Hiçbir puan hesabı, başvuru dönemine ait
  ÜAK PDF'i teyit edilmeden kesin sunulmaz.
- **Bibliyometrinin sınırı:** Hukuk kitap ve ulusal-dil dergisi ağırlıklı bir disiplindir;
  WoS'ta büyük ölçüde AHCI'da yer alır ve AHCI'ya Impact Factor / quartile atanmaz.
  JIF ve h-index hukukta yanıltıcıdır (DORA · CoARA · Leiden Manifesto).
- Bu paket **gerçek kişi veya kurum verisi içermez**; profil alanları `[DOLDUR]` gelir.

---
---

# ArthurLegal — Claude Academician Assistant (English)

**Version:** v1.0.0 · **Date:** 2026-07-09 · **License:** Proprietary — Non-Commercial (see [LICENSE](LICENSE))
**Target environment:** [Claude.ai Projects](https://claude.ai/projects) (web)

> **v1.0.0 — 8 plugins · 28 skills · 23 references · 4 agents.** Fully bilingual (TR + EN),
> covering Turkish and international academic regimes at equal depth.

> A research, writing, citation-verification, publication-ethics, thesis-supervision and
> grant-application assistant for **legal academics** (research assistant → professor).

---

## How it differs from the other ArthurLegal packages

| | Corporate / Law-Firm | Courthouse | **Academician** |
|---|---|---|---|
| User | In-house / law firm | Judge + court clerk | **Legal academic** |
| Stance | Party advocate | Judicial / neutral | **Scholarly / author-centred** |
| Purpose | Draft favouring the client | Reasoning + procedure | **Draft + citation verification + ethics compliance** |
| Position of the assistant | Serves the **subject** of regulation | Same | **The assistant is itself the object of regulation** |

**The core difference:** the use of generative AI in scholarly publishing and research
funding is **directly regulated**, both in Türkiye and internationally. This package puts
compliance with that regime at the centre of the product.

---

## 🚪 The GenAI Gate — four rules

1. **GenAI cannot be an author.** Responsibility always rests with a human.
   *(COPE, 13 Feb 2023 · ICMJE · WAME · YÖK GenAI Ethics Guide 2024 · TÜBİTAK GenAI Guide)*
2. **Use must be disclosed.** Every substantive output ends with a ready-to-paste
   **AI use statement** (tool + version + date + scope).
3. **Confidential manuscripts are never ingested.** An unpublished manuscript, proposal or
   thesis under evaluation must **not** be entered into the assistant — doing so breaches
   confidentiality.
   *(TÜBİTAK GenAI Guide § 2.2.1 · NIH NOT-OD-23-149 · NSF · Elsevier · Springer Nature · Wiley · ICMJE)*
   → the `hakemlik-editorluk` plugin **does not read text; it runs process.**
4. **Zero-hallucination citation.** No source enters a footnote unless it was actually
   retrieved. A fabricated citation is a **plagiarism/falsification risk** under publication
   ethics codes.

---

## Architecture — 8 plugins

| Plugin | Scope |
|---|---|
| `arastirma-tasarim` | Research question, literature map, method selection, **ethics-committee triage** |
| `makale-yazim` | Article skeleton, journal selection, response-to-reviewers, abstract & keywords |
| `atif-kaynak` | **Citation verification**, bibliography generation, citation-style conversion |
| `yayin-etigi` | **AI use statement**, misconduct triage, similarity-report interpretation, authorship & CRediT |
| `akademik-yukselme` | Associate-professorship scoring, dossier gap analysis, appointment criteria |
| `proje-fon` | TÜBİTAK applications, EU/Horizon applications, work-package design |
| `tez-danismanlik` | Thesis structure, defence preparation, student feedback |
| `hakemlik-editorluk` | **Ingests no manuscript.** Reviewer rubric, editorial decision letter, COPE flowcharts |

Usage: `/<plugin>:<skill>` — e.g. `/yayin-etigi:uyz-beyani`

---

## Data sources

**Connected MCP servers:** TR Legal MCP (Turkish legislation + case law) · CourtListener
(US case law, official MCP) · Fedlex (Swiss federal law) · OpenCaseLaw.ch (Swiss case law +
scholarship bridge)

**Free REST, no key required:** Crossref/DOI · OpenAlex · Semantic Scholar · DOAJ · ORCID ·
EUR-Lex · HUDOC

**No API — manual verification required:** Lexpera · Kazancı · Jurix · Legalbank ·
HeinOnline · Westlaw · LexisNexis · Beck-online

> ⚠️ **This package embeds no API keys.**

---

## Installation

English → [INSTALLATION.md](INSTALLATION.md) · Türkçe → [KURULUM.md](KURULUM.md)

---

## Cautions

- Outputs are **drafts**; they do not substitute for scholarly work, a referee report or
  academic evaluation.
- **Similarity score ≠ plagiarism.** There is **no universally accepted threshold**; your
  institution sets it.
- **Associate-professorship criteria change between application periods.** No score is
  presented as definitive without confirming the ÜAK PDF for your period.
- **Limits of bibliometrics:** law is a book- and national-language-heavy discipline, largely
  indexed in AHCI, to which no Impact Factor or quartile is assigned. JIF and h-index are
  misleading in law (DORA · CoARA · Leiden Manifesto).
- This package contains **no real personal or institutional data**; profile fields ship as
  `[DOLDUR]` placeholders.
