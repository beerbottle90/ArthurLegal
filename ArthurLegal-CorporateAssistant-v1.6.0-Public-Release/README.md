# ArthurLegal — Claude Corporate Legal Assistant

**Version:** v1.6.0 · **Date:** 2026-08-30 · **License:** Proprietary — Non-Commercial (see [LICENSE](LICENSE))
**Target environment:** [Claude.ai Projects](https://claude.ai/projects) (web)

> **Multi-jurisdiction legal assistant package for in-house corporate legal teams**, built on Claude and packaged as a Claude.ai Projects bundle — `SYSTEM_PROMPT.md` + 66 knowledge files + up to 7 MCP connectors, covering **29 jurisdictions**.
>
> Derived from Anthropic's [claude-for-legal](https://github.com/anthropics/claude-for-legal) reference package.

---

## What it does

Produces **pre-review draft output** for the day-to-day production workflow of an
in-house legal team: NDA triage, M&A diligence, data-subject access request
responses, occupational health and safety incident runbooks, administrative
litigation pre-assessment, trademark clearance, weekly regulatory digests,
transfer pricing control notes, tax litigation workflows, and cross-border
governing-law analysis.

Output is **always a draft** and requires attorney review. The package enforces
this through strict citation discipline — every legal proposition carries its
source and retrieval date (`[Legislation MCP — date]`, `[Case Law MCP —
institution — date]`, `[model knowledge — verify]`), and unretrieved text is
never presented as retrieved.

---

## 12 practice areas

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
| `commercial-legal` | Contracts and obligations, commercial code, stamp duty, registered e-delivery, ISTAC arbitration; NDA GREEN/YELLOW/RED triage; **cross-border governing-law analysis** |
| `corporate-legal` | Corporate reorganizations, merger control, capital markets, data controller registry; M&A diligence; tabular review |
| `employment-legal` | Employment, social security, collective bargaining, occupational health & safety; internal investigations, termination, international expansion |
| `privacy-legal` | Dual-regime data protection (Turkish KVKK 6698 + GDPR), cross-border transfer regime, 30-day DSAR clock |
| `regulatory-legal` | Official gazette monitoring + energy / banking / capital markets / audit regulators; weekly digest |
| `ip-legal` | Industrial property, patent office practice, internet and copyright law; trademark clearance, UDRP |
| `litigation-legal` | Civil procedure + national e-justice portal + OHS incident runbook (0–1 / 0–24 / 0–72 hours); pre-litigation checks; outside-counsel coordination |
| `tax-legal` | Tax procedure, corporate tax and transfer pricing, VAT, excise, revenue-authority rulings; finance–legal coordination |
| `administrative-legal` | Administrative procedure and time limits (60-day general / 30-day tax / expedited environmental review); three-tier administrative judiciary; proactive regulator dialogue |
| `energy-finance` | Energy M&A · project finance · JV · LNG offtake; CAATSA / sanctions; cross-border (JP / EU / AZ / CN) |
| `contract-drafting` | Contract document generation & redlining: review→apply to document, derive from precedent, version comparison (track-changes diff), amendment / extension |
| `legal-research` **(NEW)** | Source layer — Azerbaijani legislation (e-qanun MCP, status-verified) · academic doctrine (LexScholar, incl. DergiPark) · signed PSA/JOA precedent (ResourceContracts) |

For detailed content → [CHANGELOG.md](CHANGELOG.md).

---

## MCP integrations & 22 jurisdictions

| Source | Access | Auth | Coverage |
|---|---|---|---|
| **TR Legal MCP** (unified) | MCP — `yargi-mcp-pro-production.up.railway.app/mcp` | OAuth (WorkOS) | Turkish legislation (verbatim norm text) + judicial and administrative decisions from 15 institutions — 40+ tools, single connector |
| **OpenCaseLaw.ch** | MCP — `mcp.opencaselaw.ch/sse` | None | Switzerland — 972K+ federal and cantonal decisions + Fedlex legislation integration (CC0) — 33 tools |
| **CourtListener** | MCP — official server, Anthropic connector directory | OAuth 2.0 (dynamic client registration) | **United States case law** — federal and state opinions, PACER dockets, citation network, oral arguments, and **citation verification** (fabricated-citation defence). Operated by Free Law Project. See `courtlistener-rehberi.md` |
| **e-qanun** 🆕 | MCP — self-host `/mcp` | None | Azerbaijani legislation — official `api.e-qanun.az`, **in-force status verified** (PRIMARY) |
| **LexScholar** 🆕 | MCP — self-host `/mcp` | None | 10 federated open-access indexes — DOAJ · SciELO · HAL · Dialnet · OpenAIRE · Law Review Commons · OpenAlex · Crossref · Unpaywall · **DergiPark (19 Turkish law journals)** (SECONDARY) |
| **ResourceContracts** 🆕 | MCP — self-host `/mcp` | None | 5,125 signed petroleum & mining contracts, 107 countries + expert clause annotations (PRECEDENT) |
| **OpenSanctions** | REST API — `api.opensanctions.org` | API key | Sanctions / PEP screening (paid membership) |
| **Fedlex** | MCP — Anthropic connector directory *(WebFetch fallback: `fedlex.admin.ch`)* | None | **Swiss federal legislation** — article text, full statute text, amendment history, title search |
| **KAP + e-ŞİRKET** | WebFetch — `kap.org.tr`, `e-sirket.mkk.com.tr` | None | Turkish public-company disclosures |

**Jurisdictions reached via WebFetch** (no additional connector required):
🇬🇧 UK · 🇺🇸 US *(federal legislation — GovInfo; case law is via the CourtListener MCP above)* · 🇪🇺 EU / CJEU / ECHR · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU *(sanctions / KYC only)* · 🇨🇳 CN · 🇷🇸 RS · 🇦🇿 AZ *(case law + English-language sources; legislation via the e-qanun MCP)*

**The 22 jurisdictions** = 12 national (🇹🇷 TR · 🇨🇭 CH · 🇺🇸 US · 🇦🇿 AZ · 🇬🇧 UK · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU · 🇨🇳 CN · 🇷🇸 RS) + 2 supranational legal orders (🇪🇺 EU/CJEU · ECHR).

**Coverage depth is not uniform**, and the package says so rather than papering
over it. Türkiye has the deepest coverage (dedicated MCP, 15 institutions, 40+
tools, and the largest share of the reference layer); Switzerland, the United
States and Azerbaijan follow with primary-source MCP access; the WebFetch
jurisdictions provide legislation and, where available, case law. When scope
narrows, the assistant states it in the output.

TR Legal MCP is a public MCP server published by [saidsurucu](https://github.com/saidsurucu).
The three new MCP servers are **self-hosted and auth-free**; installing them is
**optional** — without them the package still works, and the assistant notes the
narrowed scope in its output.

---

## Installation — 5 steps, ~15 minutes

Full guide → [KURULUM.md](KURULUM.md) (Turkish).

1. **Create a new Claude.ai Project** — [claude.ai/projects](https://claude.ai/projects) → "+ New Project".
2. **Paste `SYSTEM_PROMPT.md`** into the Custom Instructions field.
3. **Upload the ~66 files** in `knowledge/` to Project Knowledge (bulk drag-and-drop per folder).
4. **Add the TR Legal MCP connector** — URL: `https://yargi-mcp-pro-production.up.railway.app/mcp` (WorkOS OAuth). Optional jurisdiction connectors: OpenCaseLaw.ch · CourtListener · Fedlex (KURULUM.md Step 4b) · e-qanun · LexScholar · ResourceContracts (no auth — Step 4d).
5. **Fill the `[DOLDUR]` placeholders** in `knowledge/company-profile.md` for your own organization — or have the assistant do it with `/<plugin>:cold-start-interview`.

---

## First-use examples

```text
/commercial-legal:nda-review
[paste the NDA text]
```
→ Limitation-of-liability check, stamp duty, sanctions screening, GREEN/YELLOW/RED triage.

```text
/commercial-legal:governing-law-review
[upload the contract — select a foreign governing law]
```
→ Conflict-of-laws and New York Convention enforcement analysis across 22 jurisdictions.

```text
/privacy-legal:dsar-response
[paste the data-subject request]
```
→ 30-day calendar, statutory exemption check, draft response.

```text
/litigation-legal:isg-incident-response
[describe the incident]
```
→ Phased 0–1 / 0–24 / 0–72 hour runbook; parallel criminal, civil-damages and administrative risk.

```text
/energy-finance:project-finance-review
[upload the financing documents]
```
→ Project finance structure analysis; take-or-pay, CAATSA / sanctions, energy licence transfer.

```text
/legal-research:az-mevzuat
What is the notice period under the Azerbaijani Labour Code?
```
→ `search_acts` → **status verification via `get_act`** (`Qüvvədədir` / `Ləğv olunmuş`) → article text, with the in-force status inside the citation.

```text
/legal-research:sozlesme-emsali
Our cost recovery cap is 50%. What does the market look like?
```
→ Signed PSA precedents + expert clause annotations → market / aggressive / conservative assessment.

```text
/legal-research:karsilastirmali-doktrin
How is force majeure treated in TR, FR and BR?
```
→ Each jurisdiction is searched in its own terminology (`mücbir sebep` / `force majeure` / `caso fortuito`); DergiPark + HAL + SciELO.

To see all commands, type just `/<plugin>:` in a new conversation — Claude will
list that plugin's skills.

---

## Package contents

```
ArthurLegal-CorporateAssistant-v1.5.0-Public-Release/
├── KURULUM.md             ← Installation guide, Turkish (start here)
├── SYSTEM_PROMPT.md       ← Claude.ai Custom Instructions text
├── README.md              ← This file
├── CHANGELOG.md           ← Release notes
├── VERSION.md             ← 1.5.0
├── ATTRIBUTION.md         ← Attribution
├── LICENSE                ← Proprietary — Non-Commercial
└── knowledge/             ← 66 files to upload to Project Knowledge
    ├── company-profile.md       (organization profile template — ships with [DOLDUR] placeholders)
    ├── skills/                  (12 consolidated skill books, one file per plugin)
    ├── references/              (65 references: legislation + 22 jurisdictions + 4 MCP guides)
    └── agents/                  (7 scheduled agent definitions)
```

> **Note on language:** the knowledge layer and `SYSTEM_PROMPT.md` are written in
> Turkish, and the assistant's default working language is Turkish. The
> jurisdictional reach is multi-jurisdictional; the interface language is not yet.

---

## Limitations

- **This is not legal advice.** All output is a draft for attorney review.
- **Legislation and case law change** — verify manually against the official sources before any critical decision.
- **Tool calls are cancelled at 100 seconds** and a cancelled call returns nothing. Queries are kept narrow; if scope narrowed, the assistant says so.
- **Doctrine and contract precedent are secondary / comparative** — they cannot carry a legal conclusion on their own. Peer-review status is three-valued (`true` / `false` / `null`); US law reviews are student-edited.
- **The three new MCP servers are public search tools** — confidential drafts, negotiation positions and personal data are never sent to them.
- Hooks, CLM integration and matter persistence do not exist in Claude.ai Projects (they are available with Claude Code).

---

## Personal data notice

The public release of this package contains **no real personal or company data**.
`knowledge/company-profile.md` is a template consisting entirely of `[DOLDUR]`
placeholders. Data you enter when adapting the package to your own organization
is **under your control** — review it before committing to a public repository.

---

## Attribution

- **Author** (code & content generation): Claude (Anthropic)
- **Knowledge base**: Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)

For details → [ATTRIBUTION.md](ATTRIBUTION.md).

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
