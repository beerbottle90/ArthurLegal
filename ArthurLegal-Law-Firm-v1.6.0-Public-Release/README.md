# ArthurLegal — Claude Law Firm Assistant

**Version:** v1.6.0 · **Date:** 2026-08-30 · **License:** Proprietary — Non-Commercial (see [LICENSE](LICENSE))
**Target environment:** [Claude.ai Projects](https://claude.ai/projects) (web)

> **Multi-jurisdiction legal assistant package for small-to-mid law firms (0–30 staff)**, built on Claude and packaged as a Claude.ai Projects bundle — `SYSTEM_PROMPT.md` + 91 knowledge files + up to 7 MCP connectors, covering **29 jurisdictions**.
>
> Derived from Anthropic's [claude-for-legal](https://github.com/anthropics/claude-for-legal) reference package.

---

## What it does

Produces **pre-review draft output** for the day-to-day production workflow of a
law firm with 0–30 staff and a balanced litigation / advisory practice:

- Client intake + conflict check
- Duty-counsel assignment management (48-hour limit)
- Tax litigation deadline control (30-day critical window)
- NDA GREEN/YELLOW/RED triage
- Termination assessment and employment mediation
- Trademark clearance and patent office oppositions
- Data-subject access request responses + DPIA
- Regulatory monitoring and gap analysis
- Shareholder/board resolution packages, small-cap M&A due diligence
- Energy M&A, project finance, LNG offtake review

Output is **always a draft** and requires **assigned partner / managing partner
approval**. Strict citation discipline is mandatory — every legal proposition
carries its source and retrieval date (`[Legislation MCP — date]`, `[Case Law MCP
— institution — date]`, `[model knowledge — verify]`), and unretrieved text is
never presented as retrieved.

Version history and the full v1.0.1 → v1.5.0 progression: [CHANGELOG.md](CHANGELOG.md).

---

## 16 practice areas

> **New in v1.5.0:** **de-eli MCP** — German legislation, case law and
> parliamentary materials through one endpoint (14 tools: NeuRIS federal statutes,
> the complete decisions of seven federal supreme courts, sixteen state courts via
> Open Legal Data, and Bundestag Drucksachen). Plus the **2026-08 OSS source wave**
> (10 references: US citation verification, PII redaction, GLEIF, SEC EDGAR, UK
> legislation MCP, EUR-Lex Cellar, Japan e-Gov API, France DILA, ECHR HUDOC),
> **eight new jurisdictions** (UAE · Czechia · Georgia · Israel · Central Asia ·
> Romania · Ukraine · Greece — 14 → 22), and **eight new `legal-research` skills**
> (4 → 12).

| Plugin | Scope |
|---|---|
| `commercial-legal` | NDA, MSA, SaaS, vendor agreements; sanctions screening; governing law review |
| `corporate-legal` | M&A, board, due diligence, public-company disclosure |
| `employment-legal` | Employment law, internal investigations, collective bargaining |
| `privacy-legal` | Data protection, DSAR, DPIA, DPA |
| `regulatory-legal` | Regulatory monitoring — energy, capital markets, competition |
| `ip-legal` | Trademark / patent / design, takedown, open-source review |
| `litigation-legal` | Civil procedure + national e-justice portal + case management |
| `tax-legal` | Corporate tax, tax procedure, VAT / excise, revenue rulings, tax chamber case law |
| `administrative-legal` | Three-tier administrative judiciary + regulatory board decisions |
| `energy-finance` | Energy M&A, project finance, JV, LNG offtake |
| `criminal-defense` | Mandatory duty counsel, privately retained defence, victim intervention |
| `firm-operations` | Client intake, conflict check, AML, data protection |
| `advocacy-legal` **(NEW)** | Pleading generation (private-law / public-law / criminal tracks) + clerical assistance |
| `expert-opinion` **(NEW)** | Expert reports + specialist legal opinions; objections to opposing reports |
| `contract-drafting` | Contract generation & redlining: review→apply to document, derive from precedent, version comparison, amendment |
| `legal-research` **(NEW)** | Source layer — Azerbaijani legislation (e-qanun MCP, status-verified) · academic doctrine (LexScholar; **DergiPark, 19 Turkish law journals**) · signed PSA/JOA precedent (ResourceContracts) |

---

## MCP integrations & 22 jurisdictions

| Source | Access | Auth | Coverage |
|---|---|---|---|
| **TR Legal MCP (yargi-mcp-pro)** | MCP — `yargi-mcp-pro-production.up.railway.app/mcp` | OAuth 2.0 | Turkish legislation + judicial and administrative decisions from 15 institutions — 40+ tools |
| **OpenCaseLaw.ch** | MCP — `mcp.opencaselaw.ch/sse` | None | Swiss case law — 972K+ federal and cantonal decisions + Fedlex legislation integration (CC0) — 33 tools |
| **CourtListener** | MCP — official server, Anthropic connector directory | OAuth 2.0 (dynamic client registration) | **United States case law** — federal and state opinions, PACER dockets, citation network, oral arguments, and **citation verification** (fabricated-citation defence). Operated by Free Law Project. See `courtlistener-rehberi.md` |
| **e-qanun** 🆕 | MCP — self-host `/mcp` | None | Azerbaijani legislation — official `api.e-qanun.az`, **in-force status verified** (PRIMARY) — 6 tools |
| **LexScholar** 🆕 | MCP — self-host `/mcp` | None | 10 federated open-access indexes — DOAJ · SciELO · HAL · Dialnet · OpenAIRE · Law Review Commons · OpenAlex · Crossref · Unpaywall · **DergiPark (19 Turkish law journals)** (SECONDARY) — 6 tools |
| **ResourceContracts** 🆕 | MCP — self-host `/mcp` | None | 5,125 signed petroleum & mining contracts, 107 countries + expert clause annotations (PRECEDENT) — 9 tools |
| **OpenSanctions** | REST API — `api.opensanctions.org` | API key | Client sanctions / PEP / KYC screening |
| **Fedlex** | MCP — Anthropic connector directory *(WebFetch fallback: `fedlex.admin.ch`)* | None | **Swiss federal legislation** — article text, full statute text, amendment history, title search |

**Jurisdictions reached via WebFetch** (no additional connector required):
🇬🇧 UK · 🇺🇸 US *(federal legislation — GovInfo; case law is via the CourtListener MCP above)* · 🇪🇺 EU / CJEU / ECHR · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU *(sanctions / KYC only)* · 🇨🇳 CN · 🇷🇸 RS · 🇦🇿 AZ *(case law + English-language sources; legislation via the e-qanun MCP)*

**The 22 jurisdictions** = 20 national (🇹🇷 TR · 🇨🇭 CH · 🇺🇸 US · 🇦🇿 AZ · 🇬🇧 UK · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU · 🇨🇳 CN · 🇷🇸 RS · 🇦🇪 AE · 🇨🇿 CZ · 🇬🇪 GE · 🇮🇱 IL · 🇰🇿 KZ · 🇺🇿 UZ · 🇷🇴 RO · 🇺🇦 UA · 🇬🇷 GR) + 2 supranational legal orders (🇪🇺 EU/CJEU · ECHR).

**Coverage depth is not uniform**, and the package says so rather than papering
over it. Türkiye has the deepest coverage (dedicated MCP, 15 institutions, 40+
tools, and the largest share of the 76-file reference layer); Switzerland, the
United States and Azerbaijan follow with primary-source MCP access; the WebFetch
jurisdictions provide legislation and, where available, case law. When scope
narrows, the assistant states it in the output.

> 🆕 = v1.4.0 / v1.5.0. The four self-hosted servers are **auth-free**; installing
> them is **optional** — without them the package still works, and the assistant
> notes the narrowed scope in its output. Setup: [INSTALLATION.md](INSTALLATION.md)
> Step 4b (jurisdiction connectors: Step 4a).
>
> ⚠️ **Professional secrecy:** all three are **public** search tools — never send a
> client name, a matter summary or a confidential draft; queries must be framed as
> abstract legal concepts.

---

## Installation — 7 steps

English guide → [INSTALLATION.md](INSTALLATION.md)
Turkish guide → [KURULUM.md](KURULUM.md)

**Summary:**
1. Claude.ai → Projects → New Project
2. `SYSTEM_PROMPT.md` → Custom Instructions
3. `knowledge/` folder → Upload Files
4. Add the TR Legal MCP connector — then, per client portfolio, the jurisdiction connectors (CourtListener · Fedlex · OpenCaseLaw.ch, Step 4a) and the source layer (e-qanun · LexScholar · ResourceContracts, Step 4b)
5. OpenSanctions API key (optional)
6. Run `/firm-operations:cold-start-interview`
7. Run the practice-area cold-starts

---

## First-use examples

```text
/firm-operations:new-client-intake
```
→ Triggers intake + conflict + AML + data protection + fee + power-of-attorney chain.

```text
/firm-operations:conflict-check
[client + opposing party details]
```
→ Bar act and professional-conduct rules applied: ⛔ DECLINE / 🟠 REVIEW / ✓ CLEAR.

```text
/criminal-defense:cmk-gorev-atama
[bar association assignment message]
```
→ 48-hour workflow, right to silence, duty-counsel fee schedule.

```text
/tax-legal:tax-litigation-prep
[tax assessment notice]
```
→ **30-day deadline critical check**, settlement vs. litigation matrix.

```text
/privacy-legal:dsar-response
[data-subject request]
```
→ 30-day response clock, response template, registry compliance.

```text
/regulatory-legal:reg-feed-watcher
```
→ Weekly regulatory change digest.

To see all commands, type just `/<plugin>:` — the assistant will list that
plugin's full skill set.

---

## Package contents

```
ArthurLegal-Law-Firm-v1.5.0-Public-Release/
├── INSTALLATION.md         ← English installation guide
├── KURULUM.md              ← Turkish installation guide
├── SYSTEM_PROMPT.md        ← Claude.ai Custom Instructions text
├── README.md               ← This file
├── CHANGELOG.md            ← Release notes
├── VERSION.md              ← Version
├── ATTRIBUTION.md          ← Attribution
├── LICENSE                 ← Proprietary — Non-Commercial
└── knowledge/
    ├── firm-profile.md     ← Firm profile template (ships with [DOLDUR] placeholders)
    ├── profiles/           ← 10 practice-area profiles (incl. legal-research)
    ├── skills/             ← 16 consolidated skill files
    ├── agents/             ← 7 automation agent definitions
    └── references/         ← 76 references: legislation + international jurisdictions + MCP guides
```

> **Note on language:** the knowledge layer and `SYSTEM_PROMPT.md` are written in
> Turkish, and the assistant's default working language is Turkish. The
> jurisdictional reach is multi-jurisdictional; the interface language is not yet.

---

## Limitations

- **This is not legal advice.** All output is a draft for **managing partner** review.
- **Professional responsibility rests with the attorney**; nothing may be filed with a court or sent to a client without a signed document from a bar-registered attorney.
- **Legislation and case law change** — verify manually against the official sources before any critical decision.
- **Conflict check is automated** but the nuances of the bar act's conflict rules require **human judgment**.
- **Tool calls are cancelled at 100 seconds** and a cancelled call returns nothing. If scope narrowed, the assistant says so; partial research is never presented as complete.
- **Doctrine and contract precedent are secondary / comparative** — they cannot carry a pleading on their own. Peer-review status is three-valued (`true` / `false` / `null`); US law reviews are student-edited.
- **In-force status of Azerbaijani legislation** is verified only via `get_act`; a repealed act (`Ləğv olunmuş`) can never be relied on.
- **Family / inheritance and specialist maritime law are out of scope** — referral to another specialist is recommended.

---

## Personal data notice

The public release of this package contains **no real personal, company or client
data**. All such fields are marked with `[DOLDUR]` placeholders. The example firm
(`ArthurLegal Hukuk Bürosu`) is entirely fictional.

⚠️ **Professional secrecy reminder:** when adapting the package to your own firm,
do not write real client information into the knowledge files. Keep matter folders
**isolated across matters**.

---

## Attribution

- **Author** (content & code generation): Claude (Anthropic) — Sonnet 4.6
- **Designer** (project design & domain expertise): Ertuğ Demir
- **Knowledge base**: Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)

For details → [ATTRIBUTION.md](ATTRIBUTION.md)

---

## License

This package **as a whole** is governed by the ArthurLegal Proprietary
Non-Commercial License — see [LICENSE](LICENSE). **Commercial use is prohibited.**
Use by in-house counsel, by law firm employees, and personal use by a natural
person — together with modifications made by or commissioned for such permitted
use — are not commercial use. All rights reserved.

The third-party knowledge base from which this package is derived (Anthropic
`claude-for-legal`) is licensed under the **Apache License 2.0**. Its license and
attribution notice are retained in
[LICENSE-APACHE-2.0-THIRD-PARTY.txt](LICENSE-APACHE-2.0-THIRD-PARTY.txt) and must
not be removed. In case of conflict, Apache 2.0 governs those components.
