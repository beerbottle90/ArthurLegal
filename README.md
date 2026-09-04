# ArthurLegal

> **Proprietary — Non-Commercial Use Only. All Rights Reserved. See [LICENSE](LICENSE).**

**Multi-jurisdiction legal AI assistant packages that run on [Claude.ai Projects](https://claude.ai/projects).**
Each package is a `SYSTEM_PROMPT.md` (Custom Instructions) plus a `knowledge/`
folder, and reaches **28 jurisdictions** through **up to 5 MCP connectors** and a
curated primary-source reference layer.

Built for legal teams that work across borders: a contract governed by English
law, arbitrated in Geneva, with an Azerbaijani counterparty and an EU data-transfer
question is one workflow, not four.

## Packages — current versions

| Profile | Current version | For | Scope |
|---|---|---|---|
| **Corporate Assistant** | **[v1.6.1](ArthurLegal-CorporateAssistant-v1.6.1-Public-Release/)** | In-house legal teams | 12 practice areas · 28 jurisdictions · up to 5 MCP connectors · 102 knowledge files |
| **Law Firm Assistant** | **[v1.6.1](ArthurLegal-Law-Firm-v1.6.1-Public-Release/)** | Law firms, 0–30 staff | 16 practice areas · 28 jurisdictions · up to 5 MCP connectors · 127 knowledge files |
| Academician | [v1.0.0](ArthurLegal-Academician-v1.0.0-Public-Release/) | Legal academics | Publication strategy, journal selection, associate-professorship track, ethics board |
| Courthouse | [v1.0.0](ArthurLegal-Courthouse-v1.0.0-Public-Release/) | Bench and prosecution | Judge and prosecutor workflows |

The two flagship packages (Corporate, Law Firm) are multi-jurisdictional. The
Academician and Courthouse packages are built around Turkish academic-promotion
and Turkish judicial procedure respectively, and are jurisdiction-specific by
design.

Earlier versions are retained as archives (`v1.0.0`, `v1.0.1`, `v1.2.0`, `v1.3.1`).
To install, start from the `KURULUM.md` (Turkish) or `INSTALLATION.md` (English)
file in the package you want.

## Jurisdictional coverage

Coverage is real but **not uniform in depth** — the packages state which tier a
source sits in, and the assistant flags reduced coverage in its output rather
than filling the gap with recalled text.

**14 jurisdictions** = 12 national (🇹🇷 TR · 🇨🇭 CH · 🇺🇸 US · 🇦🇿 AZ · 🇬🇧 UK ·
🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU · 🇨🇳 CN · 🇷🇸 RS) + 2 supranational
legal orders (🇪🇺 EU/CJEU · ECHR).

| Tier | Jurisdictions | How it is reached |
|---|---|---|
| **Primary-source MCP** — verbatim norm text and case law | 🇹🇷 Türkiye · 🇨🇭 Switzerland · 🇺🇸 United States *(case law)* · 🇦🇿 Azerbaijan · 🇦🇹 Austria · 🇩🇪 Germany · 🇳🇱 Netherlands · 🇵🇱 Poland · 🇪🇸 Spain · 🇫🇮 Finland · 🇮🇪 Ireland | **TR Legal MCP** (15 institutions, 40+ tools) · **OpenCaseLaw.ch** (972K+ decisions, 33 tools) · **CourtListener** (Free Law Project — US federal and state case law, PACER, citation verification) · **Fedlex** (Swiss federal legislation) · **[ArthurLegal MCP](https://github.com/beerbottle90/arthurlegal-mcp)** — ten jurisdictions behind one connector, 63 tools, jurisdiction-prefixed |
| **Legislation via WebFetch** — no extra connector | 🇬🇧 UK · 🇺🇸 US *(federal legislation, GovInfo)* · 🇪🇺 EU / CJEU / ECHR · 🇩🇪 Germany · 🇫🇷 France · 🇮🇹 Italy · 🇯🇵 Japan · 🇷🇺 Russia · 🇨🇳 China · 🇷🇸 Serbia | Official gazette and legislation portals |
| **Cross-cutting corpora** — precedent, doctrine, screening | 107 countries (signed contracts) · 10 open-access scholarship indexes · global sanctions / PEP | **ArthurLegal MCP** (`contracts_`, `scholar_`) · **OpenSanctions** (REST API, API key) |

Türkiye currently has the deepest coverage: a dedicated MCP server spanning 15
institutions with 40+ tools, plus the largest share of the reference layer.
Switzerland (972K+ decisions and Fedlex legislation) and Azerbaijan (official
`api.e-qanun.az` with in-force status verification) follow. Seven more European
jurisdictions are reached through ArthurLegal MCP, whose `status` tool reports
each one's index coverage — a statute outside that range is not found, and the
search returns its nearest neighbour rather than saying so.

## v1.6.0 — Source audit: 7 broken sources fixed, 7 new jurisdictions (2026-08-30)

Every MCP and every WebFetch/REST source in the package was hit with a **real
query** — the returned data was inspected, not just the status code.

**Fixed (each verified live):**

- **EUR-Lex full text.** `eur-lex.europa.eu/legal-content/...`, `search.html` and
  `eli/...` return a JS shell, not the document — a working **CELLAR three-step
  chain** replaces them (proved on GDPR/EN and Directive 2019/944/RO).
- **German NeuRIS host.** `api.rechtsinformationen.bund.de` never existed
  (NXDOMAIN); corrected to `testphase.rechtsinformationen.bund.de`.
- **Romania.** `legislatie.just.ro` drops the connection; primary source moved to
  EUR-Lex CELLAR Romanian full text, with working fallbacks documented.
- **OpenCaseLaw.ch REST fallback.** Every `/api/*` path 404s — the fictitious
  fallback was removed.
- **EU sanctions endpoint.** `sanctionsmap.eu/api/v1/sanction` 404s; replaced with
  the EU FSF consolidated list (CSV/XML) and the working UN consolidated XML.
- **ILO NATLEX (AZ)** 403 → routed to the e-qanun MCP.
- **CourtListener `citation-lookup/`** needs a token header WebFetch cannot send →
  routed to the `analyze_citations` / `extract_citations` MCP tools.

**Added — six MCP servers**, one per jurisdiction whose official source cannot be
searched properly. All dependency-free (standard library only) and auth-free, with
hybrid retrieval — BM25 plus trigram fuzzy matching, and a dense-vector channel that
turns on when an embeddings endpoint is configured:
[nl-rechtspraak-mcp](https://github.com/beerbottle90/nl-rechtspraak-mcp) ·
[pl-sejm-mcp](https://github.com/beerbottle90/pl-sejm-mcp) ·
[at-ris-mcp](https://github.com/beerbottle90/at-ris-mcp) ·
[ie-statutebook-mcp](https://github.com/beerbottle90/ie-statutebook-mcp) ·
[fi-finlex-mcp](https://github.com/beerbottle90/fi-finlex-mcp) ·
[es-boe-mcp](https://github.com/beerbottle90/es-boe-mcp)

**Added — 6 jurisdictions, each with a live-tested API:** 🇳🇱 Netherlands (KOOP SRU
full text + 3,751,381 ECLI decisions) · 🇵🇱 Poland (Sejm ELI API with in-force
status) · 🇦🇹 Austria (RIS OGD v2.6 — legislation *and* case law) · 🇮🇪 Ireland
(section-level ELI) · 🇫🇮 Finland (Finlex Akoma Ntoso REST) · 🇪🇸 Spain (BOE).

Luxembourg was assessed and **dropped**: every Legilux URL returns the same
2,116-byte empty Angular shell, and no other route exists. HTTP 200 is not the
same as a working source.

Plus `references/MCP-ROADMAP.md` — an evidence-based ranking of which jurisdictions
justify building an MCP server, and which already have a good enough public API.

## v1.6.1 — ten MCP connectors become one (2026-09-04)

The packages' content did not change; the way you reach it did. Ten separately
connected MCP servers now sit behind one permanent endpoint —
[`arthurlegal-mcp`](https://github.com/beerbottle90/arthurlegal-mcp), 63 tools,
no auth. You add one connector instead of ten, and you never update a tunnel
address again.

Every tool now carries its jurisdiction as a prefix (`az_` `at_` `de_` `nl_`
`pl_` `es_` `fi_` `ie_` `scholar_` `contracts_`). This is not cosmetic: across
the underlying servers `get_act` means five different things and
`search_legislation` three, so without prefixes a Spanish question could be
answered with Finnish law. The nine per-server `server_status` tools collapse
into one `status`, which reports each jurisdiction's index size, date coverage
and whether semantic search is live.

**Know this limit.** When a statute falls outside a jurisdiction's index
coverage, the search does not say "out of scope" — it returns the nearest
neighbour. Asked in Turkish for Finnish employment-contract termination, it
returned travel-document and fishing regulations, because the Employment
Contracts Act is outside the index's 2024-2025 slice. Read `index_coverage`
from `status`. Where coverage is complete the cross-language retrieval works as
intended: Turkish *"kişisel verilerin korunması"* returns Spain's LO 15/1999,
LO 7/2021 and the AEPD Instruction.

## v1.5.0 — German law, the OSS source wave, eight more jurisdictions (2026-08-29)

A fourth self-hosted MCP server and the full 2026-08 open-source research wave.

| Addition | What it brings |
|---|---|
| **de-eli MCP** — **PRIMARY**, 14 tools | German legislation (NeuRIS, BMJV), case law (rechtsprechung-im-internet.de — **complete** for BVerfG, BGH, BAG, BFH, BVerwG, BSG, BPatG; Open Legal Data for the sixteen state courts and full-text search), and Bundestag Drucksachen including legislative explanatory materials. Every response carries `eli_uri`/`ECLI`, `human_readable_citation` and `source_url` — **citation strings are never constructed**. |
| **OSS source wave** — 10 references | US citation verification (fabricated-citation defence) · PII redaction · GLEIF · SEC EDGAR · UK legislation MCP · EUR-Lex Cellar · Japan e-Gov API · France DILA · ECHR HUDOC · machine-readable source catalogue. 89 candidates screened to 48 independent vetting decisions against five invariants. |
| **Eight new jurisdictions** (14 → 22) | UAE · Czechia · Georgia · Israel · Central Asia (KZ, UZ) · Romania · Ukraine · Greece |
| **Eight new `legal-research` skills** (4 → 12) | `alman-hukuku` · `abd-atif-dogrulama` · `karsi-taraf-kimlik` · `uk-mevzuat` · `ab-mevzuat` · `jp-mevzuat` · `fr-mevzuat` · `echr-ictihat` |

Also fixed in this release: broken cross-references between guides, and residual
client identifiers that had survived into the public packages.

## v1.4.0 — research source layer (2026-07-26)

The Corporate and Law Firm packages gained a `legal-research` plugin and three
**self-hosted, no-auth** MCP servers:

| MCP | Role | Coverage |
|---|---|---|
| **e-qanun** | **PRIMARY** | Azerbaijani legislation — official `api.e-qanun.az`; **in-force status verified** (`Qüvvədədir` / `Ləğv olunmuş`) |
| **LexScholar** | **SECONDARY** | 10 federated open-access indexes; includes 19 verified Turkish law journals via DergiPark's official OAI-PMH endpoint |
| **ResourceContracts** | **PRECEDENT** | 5,125 signed petroleum and mining contracts across 107 countries, with expert clause annotations (CC BY-SA 4.0, NRGI/CCSI) |

All three are **optional** — the packages work without them, and the assistant
states the narrowed scope in its output. Details: the `CHANGELOG.md` of the
relevant package.

---

Copyright (c) 2026 ArthurLegal. All rights reserved.

This repository is **source-available but not open source**. **Commercial use is
prohibited.** Within that limit, you are permitted to use, run, and modify the
Software for non-commercial purposes.

The following are expressly **not** commercial use:

- use by an **in-house counsel**, or any member of an in-house legal department,
  in the ordinary course of their duties;
- use by an **employee of a law firm** — partner, associate, trainee, paralegal
  — in the ordinary course of their duties, including work performed for the
  firm's clients;
- **personal use** by a natural person;
- **modifications** a person makes, or commissions a third party to make, for
  their own permitted use (and does not distribute).

Revenue earned from the *legal services* in which the Software is used does not
make that use commercial. What is prohibited is commercializing **the Software
itself** — selling, sublicensing, redistributing, or offering it as a product or
hosted service. Redistribution of any kind requires prior written permission.

This repository includes third-party components licensed under the Apache
License 2.0 (the Anthropic [`claude-for-legal`](https://github.com/anthropics/claude-for-legal)
knowledge base). Those components remain governed by their own license; their
license texts and attribution notices are retained in the release packages and
must not be removed.

See the [LICENSE](LICENSE) file for the full and binding terms.

---

## Türkçe — lisans

> **Tescilli (Proprietary) — Yalnızca ticari olmayan kullanım. Tüm hakları saklıdır. Bkz. [LICENSE](LICENSE).**

*Aşağıdaki metin kolaylık sağlamak için sunulmuştur; bağlayıcı olan [LICENSE](LICENSE)
dosyasındaki İngilizce koşullardır.*

Telif Hakkı (c) 2026 ArthurLegal. Tüm hakları saklıdır.

Bu depo **kaynağı görünür ancak açık kaynak değildir.** **Ticari kullanım
yasaktır.** Bu sınır içinde yazılımı ticari olmayan amaçlarla kullanabilir,
çalıştırabilir ve değiştirebilirsiniz.

Aşağıdakiler ticari kullanım **sayılmaz**:

- **Şirket içi (in-house) hukuk müşavirinin** veya hukuk departmanı çalışanının
  olağan görevleri kapsamındaki kullanımı;
- Bir **hukuk bürosu çalışanının** — ortak, avukat, stajyer, paralegal —
  olağan görevleri kapsamındaki kullanımı; büronun müvekkilleri için yapılan
  çalışmalar dahil;
- Gerçek kişinin **kişisel kullanımı**;
- Kişinin kendi izinli kullanımı için bizzat yaptığı veya bir üçüncü kişiye
  **yaptırdığı geliştirmeler** (başkasına dağıtılmamak kaydıyla).

Yazılımın kullanıldığı *hukuki hizmetlerden* gelir elde edilmesi, o kullanımı
ticari hâle getirmez. Yasak olan, **yazılımın kendisinin** ticarileştirilmesidir
— satmak, alt lisanslamak, yeniden dağıtmak veya bir ürün ya da barındırılan
hizmet olarak sunmak. Her türlü yeniden dağıtım önceden yazılı izne tabidir.

Bu depo, Apache 2.0 lisanslı üçüncü taraf bileşenler (Anthropic
[`claude-for-legal`](https://github.com/anthropics/claude-for-legal) bilgi
tabanı) içerir. Bu bileşenler kendi lisanslarına tabidir; lisans metinleri ve
atıf bildirimleri paketlerde korunmuştur ve kaldırılamaz.

Tam ve bağlayıcı koşullar için [LICENSE](LICENSE) dosyasına bakınız.
