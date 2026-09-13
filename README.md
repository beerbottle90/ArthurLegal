# ArthurLegal

> **Proprietary — Non-Commercial Use Only. All Rights Reserved. See [LICENSE](LICENSE).**

**Multi-jurisdiction legal AI assistant packages that run on [Claude.ai Projects](https://claude.ai/projects).**
Each package is a `SYSTEM_PROMPT.md` (Custom Instructions) plus a `knowledge/`
folder, and reaches **28 jurisdictions** through **one primary MCP connector** (Türkiye plus fourteen
jurisdictions, no auth), up to four optional ones, and a curated primary-source reference layer.

> ### ⬇ Arthur Mask — local privacy gate for Claude Desktop (Windows)
> **[Download ArthurMask-Kurulum.exe](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** (about 1 GB). The link downloads directly; no GitHub account needed.
> Double-click the downloaded file to install. Guide: `ARTHUR-MASK.md` in the Law Firm, Corporate or Courthouse package.
> **Türkçe:** [Kurulum dosyasını indirin](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe), inen dosyaya çift tıklayın; anlatım paketlerdeki `ARTHUR-MASK.md` dosyasında.

Built for legal teams that work across borders: a contract governed by English
law, arbitrated in Geneva, with an Azerbaijani counterparty and an EU data-transfer
question is one workflow, not four.

## Packages — current versions

| Profile | Current version | For | Scope |
|---|---|---|---|
| **Corporate Assistant** | **[v1.8.0](ArthurLegal-CorporateAssistant-v1.8.0-Public-Release/)** | In-house legal teams | 12 practice areas · 28 jurisdictions · one primary MCP connector (Türkiye + 14 jurisdictions) · 103 knowledge files · Arthur Mask local privacy gate |
| **Law Firm Assistant** | **[v1.8.0](ArthurLegal-Law-Firm-v1.8.0-Public-Release/)** | Law firms, 0–30 staff | 16 practice areas · 28 jurisdictions · one primary MCP connector (Türkiye + 14 jurisdictions) · 128 knowledge files · Arthur Mask local privacy gate |
| Academician | [v1.0.1](ArthurLegal-Academician-v1.0.1-Public-Release/) | Legal academics | Publication strategy, journal selection, associate-professorship track, ethics board |
| Courthouse | [v1.0.2](ArthurLegal-Courthouse-v1.0.2-Public-Release/) | Bench and prosecution | Judge and prosecutor workflows · Arthur Mask local privacy gate |

The two flagship packages (Corporate, Law Firm) are multi-jurisdictional. The
Academician and Courthouse packages are built around Turkish academic-promotion
and Turkish judicial procedure respectively, and are jurisdiction-specific by
design.

Earlier versions are retained as archives (`v1.0.0` … `v1.7.0`; Courthouse `v1.0.0` and `v1.0.1`).
To install, start from the `KURULUM.md` (Turkish) or `INSTALLATION.md` (English)
file in the package you want. The optional Arthur Mask privacy gate (Windows, Claude Desktop) installs from one file:
**[⬇ download ArthurMask-Kurulum.exe](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** (about 1 GB, direct download, no GitHub account needed).

## Jurisdictional coverage

Coverage is real but **not uniform in depth** — the packages state which tier a
source sits in, and the assistant flags reduced coverage in its output rather
than filling the gap with recalled text.

**14 jurisdictions** = 12 national (🇹🇷 TR · 🇨🇭 CH · 🇺🇸 US · 🇦🇿 AZ · 🇬🇧 UK ·
🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU · 🇨🇳 CN · 🇷🇸 RS) + 2 supranational
legal orders (🇪🇺 EU/CJEU · ECHR).

| Tier | Jurisdictions | How it is reached |
|---|---|---|
| **Primary-source MCP** — verbatim norm text and case law | 🇹🇷 Türkiye · 🇨🇭 Switzerland · 🇺🇸 United States *(case law)* · 🇦🇿 Azerbaijan · 🇦🇹 Austria · 🇩🇪 Germany · 🇳🇱 Netherlands · 🇵🇱 Poland · 🇪🇸 Spain · 🇫🇮 Finland · 🇮🇪 Ireland | **[ArthurLegal MCP](https://github.com/beerbottle90/arthurlegal-mcp)** — Türkiye (`tr_`: courts, legislation with gerekçe, Official Gazette, eight regulators, semantic archive) plus fourteen jurisdictions behind one connector, 104 tools, jurisdiction-prefixed, no auth · **OpenCaseLaw.ch** (972K+ decisions, 33 tools) · **CourtListener** (Free Law Project — US federal and state case law, PACER, citation verification) · **Fedlex** (Swiss federal legislation) · **TR Legal MCP** (optional; only ECHR, KİK, Sayıştay, Reklam Kurulu, KDK, TBB, HSK) |
| **Legislation via WebFetch** — no extra connector | 🇬🇧 UK · 🇺🇸 US *(federal legislation, GovInfo)* · 🇪🇺 EU / CJEU / ECHR · 🇩🇪 Germany · 🇫🇷 France · 🇮🇹 Italy · 🇯🇵 Japan · 🇷🇺 Russia · 🇨🇳 China · 🇷🇸 Serbia | Official gazette and legislation portals |
| **Cross-cutting corpora** — precedent, doctrine, screening | 107 countries (signed contracts) · 10 open-access scholarship indexes · global sanctions / PEP | **ArthurLegal MCP** (`contracts_`, `scholar_`) · **OpenSanctions** (REST API, API key) |

Türkiye currently has the deepest coverage: inside ArthurLegal MCP under the `tr_`
prefix — courts, legislation, Official Gazette, eight regulators and a 19,404-document
semantic archive — plus the largest share of the reference layer.
Switzerland (972K+ decisions and Fedlex legislation) and Azerbaijan (official
`api.e-qanun.az` with in-force status verification) follow. Seven more European
jurisdictions are also reached through ArthurLegal MCP, whose `status` tool reports
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

## v1.8.0 — Arthur Mask: documents are masked before anything leaves the computer (2026-09-13)

The packages gain a local privacy gate. **Arthur Mask 1.0.0** is a Windows app that runs
only on the user's computer: a lawyer drops a client document into its local browser
interface, personal data is replaced with labels such as `{{KİŞİ-01}}`, `{{ŞİRKET-02}}` or
`{{TCKN-01}}`, and the real values stay in an encrypted vault per matter. Claude receives
only the masked text, through Claude Desktop. Its answer is decoded locally back to real
names and opened in Word or as a UYAP UDF file.

| Stage | What happens |
|---|---|
| **Mask** | Word, UYAP UDF, PDF, scanned PDF or photo (local OCR), .txt and .md. Names, companies, TCKN/VKN, IBAN, addresses, phones, e-mails, birth dates, file numbers, passports and plates become labels; the same person keeps the same label across a matter's documents. Turkish, English and Azerbaijani; bilingual two-column Word contracts keep their table structure |
| **Review** | Uncertain detections wait for the lawyer's decision (mask or leave visible) |
| **Red line** | Content that must not reach AI even masked (defence strategy, settlement limits, special-category personal data, inside information) blocks sending until the lawyer writes a justification |
| **Exit gate** | Every response sent to Claude is re-scanned against all real values in the vault right before sending; any occurrence is replaced with its label |
| **Decode** | Claude's answer returns with real names; revisions are applied to the original document as Word tracked changes, layout preserved |
| **Audit** | A log of everything sent to Claude, in masked form, and a leak check that re-scans everything sent and received against the vault |

Everything runs offline: the detection and OCR models ship inside the installer. The only
other network call is an optional update check that reads the latest version number from
this repository's releases page.

**What it deliberately does not do.** Dates and amounts are not masked, and supreme and high
court citations are preserved. Images and embedded objects in Word files, and handwriting,
signatures, stamps and QR codes in scans, are not masked. Masking is pseudonymisation, not
anonymisation, and detection is probabilistic; the lawyer's obligations under data
protection law, professional secrecy, trade secret rules and NDAs are unchanged.

**Claude Desktop only, and why.** Remote connectors on claude.ai are called from
Anthropic's cloud, which cannot reach a program running on the user's computer. The gate
works only through Claude Desktop's local connector, so it is not available in claude.ai in
the browser or in the mobile apps. The ArthurLegal Project itself is shared between web and
desktop; open it from Claude Desktop.

**Download.** **[⬇ ArthurMask-Kurulum.exe](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)**, a direct download that needs no GitHub account
(always the latest version; about 1 GB; Windows 10/11 64-bit, Claude Desktop, about
4 GB free disk, 8 GB RAM recommended). It installs per user without administrator rights
and registers the `arthur-mask` connector in Claude Desktop. It is not code-signed, so
SmartScreen may warn ("More info" → "Run anyway"). Arthur Mask is covered by the same
proprietary non-commercial license and its source is not published; notices for the
open-source components it bundles ship inside the installation folder.

Package changes: Corporate and Law Firm **v1.8.0**, Courthouse **v1.0.2** — a compact
Arthur Mask section in each system prompt (fetch with `arthur_mask_belge_getir`, keep labels
verbatim, never put a label into a research query, revise the uploaded document with
tracked changes, one non-blocking reminder when identifiable data is pasted into a chat),
`knowledge/references/arthur-mask-rehberi.md`, an `ARTHUR-MASK.md` user guide (Law Firm
also `ARTHUR-MASK-EN.md`), a new installation step and third-party notices in
`ATTRIBUTION.md`. Academician is unchanged at v1.0.1.

## v1.7.0 — Türkiye behind the same connector (2026-09-06)

The Turkish sources moved from a third-party OAuth connector into ArthurLegal MCP
itself. Same endpoint, no auth, prefix `tr_`, 23 tools — **104 tools across 15
backends**, up from 81 across 14. The packages no longer need a separate
Turkish-law connector.

| `tr_` family | What it reaches |
|---|---|
| `tr_ictihat_*`, `tr_aym_*`, `tr_uyusmazlik_*` | Yargıtay, Danıştay, regional and local courts, KYB (Bedesten); Constitutional Court; Uyuşmazlık Mahkemesi |
| `tr_mevzuat_*` | 12 legislation types, article tree, single article, in-act search, **gerekçe** |
| `tr_resmi_gazete_*` | Daily Official Gazette index, document text, date-range title search |
| `tr_kurum_karari_*`, `tr_spk_bulten_icinde_ara` | Eight regulators behind one interface: Rekabet (10,368 decisions), EPDK (3,744 board decisions across five markets), SPK (weekly bulletins 2005–2026), BDDK (962), KVKK, BTK (1,904), GİB özelge, Sigorta Tahkim (66 journals) |
| `tr_semantik_ara`, `tr_belge_getir` | A 19,404-document local index — FTS5, trigram and Voyage `voyage-4-lite` vectors — so *"bir bankanın faaliyet izninin kaldırılması"* finds BDDK decisions that share none of its words |

Source: [`ArthurLegalTR`](https://github.com/beerbottle90/ArthurLegalTR) (MIT,
standard library only, no paid search keys). The endpoint knowledge comes from
[saidsurucu](https://github.com/saidsurucu)'s yargi-mcp and mevzuat-mcp; every
adapter was rewritten and verified live for both search and fetch.

**What was left out, and why.** KİK (the signed EKAP v2 API answers 500), Sayıştay
(its WAF answers 418 to every client), TÜRKPATENT (no decision database, reCAPTCHA
portal) and İSTAÇ (host unreachable) are not in the connector. A source that does
not answer is removed, not shipped as a stub; the packages route those questions to
the optional TR Legal MCP (yargi-mcp-pro) or say "not retrieved". The EPDK URL that
earlier packages cited as the board-decision page was in fact the regulations page;
the real decision tree is `son-kurul-kararlari/<market>`, and it is now crawled.

Package changes: Corporate and Law Firm **v1.7.0**, Courthouse and Academician
**v1.0.1** — `tr_` routing in the system prompts, the two Turkish MCP guides
rewritten, 60+ knowledge files' call examples converted (`phrase` → `query`,
`court_types` → `courts`, `birimAdi` → `chamber`, `mevzuat_no` → `number`), citation
tag `[ArthurLegal TR, …]`.

## v1.6.2 — four more jurisdictions (2026-09-04)

The connector address did not change. The same endpoint now carries **81 tools
across 14 backends**, up from 63 across 10.

| Prefix | Source |
|---|---|
| `uk_` | legislation.gov.uk — The National Archives, OGL v3.0 |
| `eu_` | CELLAR — EU legislation and CJEU case law |
| `jp_` | e-Gov 法令API v2 — Japanese statute law |
| `gleif_` | GLEIF — the global LEI register |

All four query upstream live and rerank in memory: no index to crawl, nothing to
go stale.

Each exists because the raw API misleads in a specific way, and each was found by
querying rather than by reading documentation. legislation.gov.uk accepts a
`year=` parameter and ignores it, so a filtered search returns an unfiltered list
that looks filtered. Japan's `remain_in_force` field means the opposite of what
it reads as — 残存効力, the residual effect of an *already repealed* law — so
trusting the name marks the entire live corpus as repealed. EUR-Lex's document
paths return a JavaScript shell. And in GLEIF an ACTIVE company can hold a LAPSED
LEI, which means stale data rather than dissolution.

**The most useful addition is an absence made visible.** The UK revised text is
current only to a stated date, and amendments enacted after it are not in what
you read. `uk_get_effects` with `unapplied_only` walks the whole feed to find
them: the Equality Act 2010 carries 24 such amendments that a single page reports
as none.

Neither the UK nor the Japanese server holds case law, and both say so.

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
