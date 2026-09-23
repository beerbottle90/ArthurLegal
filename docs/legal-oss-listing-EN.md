# legal-oss.com listing — ArthurLegal (revised, English, v1.4.0; MIT note added 2026-08-13)

Paste-ready copy for https://legal-oss.com/projects/beerbottle90/ArthurLegal
Corrects four errors in the current listing (see "Corrections" at the bottom).

---

## Project name

ArthurLegal

## Tagline (one line)

Multi-jurisdiction legal AI assistant packages for Claude.ai Projects — 28 jurisdictions, up to 5 MCP connectors, primary-source citation discipline, and a local document-masking gate.

## Short description (≈50 words)

ArthurLegal packages a legal AI assistant as a Claude.ai Project: a system prompt plus a curated knowledge base that reaches 28 jurisdictions through up to 5 MCP connectors. Four profiles target in-house teams, law firms, legal academics and the bench. Every legal proposition carries its source and retrieval date.

## Long description

ArthurLegal is a set of multi-jurisdiction legal assistant packages that run on
Claude.ai Projects. Each package is a `SYSTEM_PROMPT.md` (Custom Instructions)
plus a `knowledge/` folder of consolidated skill books, practice-area profiles,
scheduled agent definitions, and a primary-source reference layer.

It is built for legal work that crosses borders: a contract governed by English
law, arbitrated in Geneva, with an Azerbaijani counterparty and an EU
data-transfer question is one workflow, not four.

**Four profiles**

| Profile | Version | For | Scope |
|---|---|---|---|
| Corporate Assistant | v1.8.0 | In-house legal teams | 12 practice areas · 28 jurisdictions · up to 5 MCP connectors · 103 knowledge files · Arthur Mask |
| Law Firm Assistant | v1.8.1 | Law firms, 0–30 staff | 16 practice areas · 28 jurisdictions · up to 5 MCP connectors · 128 knowledge files · Arthur Mask |
| Academician | v1.0.1 | Legal academics | Publication strategy, journal selection, promotion track, ethics board |
| Courthouse | v1.0.3 | Bench and prosecution | Judge and prosecutor workflows · Arthur Mask |

The two flagship packages are multi-jurisdictional. Academician and Courthouse are
built around Turkish academic-promotion and Turkish judicial procedure
respectively, and are jurisdiction-specific by design.

**Jurisdictional coverage — three tiers, stated honestly**

Coverage is real but not uniform in depth, and the packages say which tier a
source sits in rather than papering over the difference.

- **Primary-source MCP** (verbatim norm text and case law): Türkiye · Switzerland ·
  United States (case law) · Azerbaijan — via **ArthurLegal MCP** (Türkiye under the
  `tr_` prefix: courts, legislation with gerekçe, Official Gazette, eight regulators and a
  19,498-document semantic archive; source [`arthur-tr-hukuk-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/arthur-tr-hukuk-mcp)), **OpenCaseLaw.ch** (972K+ Swiss federal and cantonal
  decisions, 33 tools), **CourtListener** (Free Law Project — US federal and state
  opinions, PACER dockets, citation network, and citation verification as a defence
  against fabricated citations), **Fedlex** (Swiss federal legislation — article
  text and amendment history), and the same **ArthurLegal MCP** — fourteen more jurisdictions and the
  Turkish land registry (live parcels from TKGM Parsel Sorgu) behind the one connector (121 tools in total): Azerbaijan (official `api.e-qanun.az` with in-force
  status verification), Austria, Germany, the Netherlands, Poland, Spain, Finland
  and Ireland, plus scholarship and contract corpora. Every tool carries its
  jurisdiction as a prefix, because `get_act` means five different things across
  the underlying servers.
- **Legislation via WebFetch** (no extra connector): UK · US (federal legislation,
  GovInfo) · EU / CJEU / ECHR · Germany · France · Italy · Japan · Russia · China ·
  Serbia.
- **Cross-cutting corpora** (inside ArthurLegal MCP): 5,125 signed petroleum and
  mining contracts across 107 countries with expert clause annotations (CC BY-SA
  4.0, NRGI/CCSI) · 10 federated open-access scholarship indexes, including 19
  Turkish law journals via DergiPark's official OAI-PMH endpoint ·
  **OpenSanctions** (REST API — sanctions / PEP screening).

Türkiye currently has the deepest coverage — its own backend inside ArthurLegal MCP
and the largest share of the reference layer. Sources whose official endpoints do not
answer reliably (KİK, Sayıştay, TÜRKPATENT, İSTAÇ) are left out rather than stubbed. Switzerland, the United
States and Azerbaijan follow with primary-source MCP access.

**Design principle: no unsourced law**

Every legal proposition in the output carries its source and retrieval date
(`[Legislation MCP — date]`, `[Case Law MCP — institution — date]`, `[model
knowledge — verify]`). Unretrieved text is never presented as retrieved. Tool
calls are cancelled at 100 seconds and a cancelled call returns nothing — when
scope narrows, the assistant states it instead of filling the gap from memory.
All output is a draft for attorney review.

**v1.8.1 (2026-09-17)** corrects criminal-procedure deadlines to the text in force after Law 7499 (objection, objection to non-prosecution, appeal and appeal on points of law: two weeks; appeals run from service of the reasoned judgment) and, in Courthouse v1.0.3, the 15-day objection to a tax payment order.

**v1.8.0 (2026-09-13)** adds **Arthur Mask**, a local privacy gate for Windows. Documents
(Word, UYAP UDF, PDF, scans via local OCR) are masked on the user's own computer: personal
data becomes labels such as `{{KİŞİ-01}}`, the real values stay in an encrypted vault per
matter, Claude receives only the masked text through Claude Desktop, and the answer is
decoded locally back to real names. A review screen, a red line for content that must not
reach AI even masked, an exit gate that re-scans every outgoing response against the vault,
and a leak check back it up. It runs fully offline. It works only with Claude Desktop, not
claude.ai in the browser or the mobile apps, because remote connectors are called from
Anthropic's cloud and cannot reach a program on the user's computer. Masking is
pseudonymisation, not anonymisation, and detection is probabilistic. The installer
(`ArthurMask-Kurulum.exe`) is a direct download from the
[Arthur Mask release](https://github.com/beerbottle90/ArthurLegal/releases/tag/arthur-mask); Arthur Mask
is covered by the proprietary package license (not an open-source license); its source can be read at
[beerbottle90/arthur-mask](https://github.com/beerbottle90/arthur-mask).

**v1.6.1 (2026-09-04)** collapsed ten separate MCP connectors into one hosted
endpoint, [`arthurlegal-mcp`](https://github.com/beerbottle90/arthurlegal-mcp).
It is optional; without it the packages still work and the assistant notes the
narrowed scope. Search reports what it actually did: which retrieval channels
ran, how many documents are indexed, how many are vectorised, and the index's
date coverage — because a statute outside that coverage is not found, and the
search returns its nearest neighbour rather than announcing the gap.

The server's 16 backends are open source. Fifteen are published under the MIT
license as folders of the [`arthurlegal-mcp`](https://github.com/beerbottle90/arthurlegal-mcp) repository,
each with its own `LICENSE` file ([`arthur-tr-hukuk-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/arthur-tr-hukuk-mcp),
[`eqanun-api`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/eqanun-api),
[`lex-scholar-api`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/lex-scholar-api),
[`resourcecontracts-api`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/resourcecontracts-api),
[`at-ris-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/at-ris-mcp),
[`nl-rechtspraak-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/nl-rechtspraak-mcp),
[`pl-sejm-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/pl-sejm-mcp),
[`es-boe-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/es-boe-mcp),
[`fi-finlex-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/fi-finlex-mcp),
[`ie-statutebook-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/ie-statutebook-mcp),
[`uk-legislation-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/uk-legislation-mcp),
[`eu-cellar-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/eu-cellar-mcp),
[`jp-egov-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/jp-egov-mcp),
[`gleif-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/gleif-mcp),
[`tkgm-mcp`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/tkgm-mcp));
the German backend is [`de-eli-mcp`](https://github.com/matematicsolutions/de-eli-mcp)
under the Apache-2.0 license.
The proprietary package license below covers the ArthurLegal packages themselves,
not these components.

## License

**Proprietary — Non-Commercial Use Only. All Rights Reserved.**

Source-available but not open source. Commercial use is prohibited; within that
limit, use, running and modification for non-commercial purposes are permitted.

Expressly **not** commercial use: use by in-house counsel or any member of an
in-house legal department in the ordinary course of their duties; use by a law
firm employee — partner, associate, trainee, paralegal — in the ordinary course
of their duties, including work for the firm's clients; personal use by a natural
person; and modifications made by or commissioned for such permitted use, where
not distributed.

Revenue earned from the *legal services* in which the software is used does not
make that use commercial. What is prohibited is commercializing **the software
itself** — selling, sublicensing, redistributing, or offering it as a product or
hosted service. Redistribution of any kind requires prior written permission.

## Third-party components

Includes third-party components licensed under the **Apache License 2.0** — the
Anthropic [`claude-for-legal`](https://github.com/anthropics/claude-for-legal)
knowledge base. The three companion self-hosted MCP servers (`eqanun-api`,
`lex-scholar-api`, `resourcecontracts-api`) are separate **MIT-licensed**
open-source projects (LICENSE files added 2026-08-13). Those components remain
governed by their own license; license
texts and attribution notices are retained in the release packages and must not
be removed. In case of conflict, Apache 2.0 governs those components.

The Arthur Mask installer bundles third-party open-source components (among them
Microsoft Presidio, spaCy, GLiNER with the `urchade/gliner_multi_pii-v1` model, PyTorch,
Hugging Face Transformers, RapidOCR with PaddleOCR PP-OCRv6 models and ONNX Runtime, under
MIT, Apache-2.0, BSD-3-Clause and PSF licenses). Their full notices ship inside the
installation folder, and each package's `ATTRIBUTION.md` lists them.

## Suggested tags / categories

multi-jurisdiction · legal-research · contract-review · contract-drafting ·
litigation-support · privacy-data-protection · regulatory-compliance ·
ip-management · tax · energy-project-finance · mcp · claude · legal-ai ·
in-house-legal · law-firm-tools

## Installation

Per-package: `KURULUM.md` (Turkish), plus `INSTALLATION.md` (English) in Law Firm and Academician.
Roughly 15 minutes — create a Claude.ai Project, paste the system prompt, upload
the knowledge folder, add the MCP connectors, fill in the profile template.

## Note on interface language

The knowledge layer and system prompts are written in Turkish and the assistant's
default working language is Turkish. Jurisdictional reach is multi-jurisdictional;
the interface language is not yet. (Worth stating in the listing so international
visitors are not surprised.)

---

## Corrections to the current listing

1. **"integration with three Model Context Protocol servers" → up to 7.**
   The full set, identical in both flagship packages: TR Legal MCP · OpenCaseLaw.ch ·
   CourtListener · Fedlex · e-qanun · LexScholar · ResourceContracts. Plus
   OpenSanctions as a REST API, and GovInfo / EUR-Lex / the other national portals
   via WebFetch. The "three" appears to have been read off the phrase "three *new*
   MCP guides" — those three (e-qanun, LexScholar, ResourceContracts) were the ones
   *added* in v1.4.0, not the total.

2. **"67-92 documents per package" applies to two of four packages, not all.**
   Actual counts: Corporate v1.4.0 → 66 · Law Firm v1.4.0 → 91 · Academician
   v1.0.0 → 36 · Courthouse v1.0.0 → 33. Likewise "latest release is v1.4.0" is
   true for Corporate and Law Firm only; Academician and Courthouse are at v1.0.0.

3. **Positioning.** The current listing describes the project as "a legal software
   project for Turkish legal practice." As of v1.4.0 the two flagship packages are
   multi-jurisdictional (14 jurisdictions, 4 of them with primary-source MCP
   access). Türkiye is the deepest-covered jurisdiction, not the project's scope.

4. **"17 jurisdictions" → 14.** The old figure was inflated and appeared in the
   READMEs, both `SYSTEM_PROMPT.md` files and `KURULUM.md`. The authoritative
   enumeration in `SYSTEM_PROMPT.md` listed 14 entries, one of which bundled EU +
   CJEU + ECHR — so the real figure was 15, and dropping Czechia (below) brings it to
   **14**: **12 national jurisdictions** (TR · CH · US · AZ · UK · DE · FR · IT · JP ·
   RU · CN · RS) **+ 2 supranational legal orders** (EU/CJEU · ECHR). Corrected
   throughout the packages; only the historical `CHANGELOG.md` entries still carry
   "17", as a record of what earlier versions claimed.

5. **Czechia dropped; Sbírka removed.** The Sbírka MCP connector was the only route
   to Czech legislation and does not work in practice, so Czech coverage has been
   withdrawn rather than advertised as working: the connector, the `cek-hukuku-rehberi.md`
   reference guide, the citation format and the routing rule are all gone from both
   packages. Knowledge-file counts drop accordingly (Corporate 67 → 66, Law Firm
   92 → 91; references 47 → 46 and 58 → 57).

---

## Resolved in this pass (were open items)

- **CourtListener misclassified.** `KURULUM.md` Step 4c listed it under "no
  connector required / WebFetch" and the README repeated that, while
  `knowledge/references/courtlistener-rehberi.md` said the opposite and was correct:
  an **official MCP server with OAuth 2.0 dynamic client registration, listed in the
  Anthropic connector directory**. Both packages now carry a proper connector step
  (Corporate: Step 4b-2 · Law Firm: Step 4a) plus the mandatory
  citation-verification warning.
- **Fedlex promoted to a connector.** Previously WebFetch-only. Both install guides
  now add it from the Anthropic connector directory, with the WebFetch route kept as
  a documented fallback.
- **Law Firm install guides had no connector steps** for OpenCaseLaw.ch,
  CourtListener or Fedlex even though the README listed them. Added as Step 4a in
  both `KURULUM.md` and `INSTALLATION.md`.
- **`INSTALLATION.md` Step 4b body was untranslated Turkish** in the English guide.
  Translated.
