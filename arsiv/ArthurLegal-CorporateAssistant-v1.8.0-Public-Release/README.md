# ArthurLegal — Claude Corporate Legal Assistant

**Version:** v1.8.0 · **Date:** 2026-09-13 · **License:** Proprietary — Non-Commercial (see [LICENSE](LICENSE))
**Target environment:** [Claude.ai Projects](https://claude.ai/projects) (web and Claude Desktop; Arthur Mask requires Claude Desktop for Windows)

> **Multi-jurisdiction legal assistant package for in-house corporate legal teams**, built on Claude and packaged as a Claude.ai Projects bundle — `SYSTEM_PROMPT.md` + 103 knowledge files + up to 5 MCP connectors + the optional local Arthur Mask privacy gate, covering **28 jurisdictions**.
>
> Derived from Anthropic's [claude-for-legal](https://github.com/anthropics/claude-for-legal) reference package.

> ### ⬇ Arthur Mask — mask documents on your own computer before Claude sees them
> **[Download the installer (Windows, about 1 GB)](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)**. The link downloads directly; no GitHub account needed.
> Double-click the downloaded `ArthurMask-Kurulum.exe`. Step-by-step guide: **[ARTHUR-MASK.md](ARTHUR-MASK.md)** (Türkçe)
> Requires Claude Desktop for Windows; it does not work in claude.ai on the web or in the mobile apps.
>
> **Türkçe:** [Kurulum dosyasını indirin](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe), inen dosyaya çift tıklayın; anlatım [ARTHUR-MASK.md](ARTHUR-MASK.md).

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

## Arthur Mask — local privacy gate (new in v1.8.0)

Company documents can now be masked **on the user's own Windows computer** before Claude
sees them. **Arthur Mask 1.0.0** is a local app, distributed as a single Windows installer:
**[download ArthurMask-Kurulum.exe](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)**
(about 1 GB, direct download, no GitHub account needed). Drop a Word, UYAP UDF, PDF or scanned
document into its local browser interface; names, companies, national ID and tax numbers,
IBANs, addresses, phone numbers, e-mail addresses, birth dates, file numbers, passports and
plates are replaced with labels such as `{{KİŞİ-01}}`. The real values stay in an encrypted
vault per matter. Claude receives only the masked text through Claude Desktop, and its
answer is decoded locally back to real names and opened in Word or UDF, with revisions
applied to the original as tracked changes.

- **Safeguards:** a review screen for uncertain detections; a red line that blocks sending
  defence strategy, settlement limits, special-category data or inside information until
  the user writes a justification; an exit gate that re-scans every response sent to
  Claude against the vault; a log of everything sent and a one-click leak check.
- **Fully offline.** Detection and OCR models ship inside the installer. The only other
  network call is a once-a-day update check that reads the latest version number.
- **Claude Desktop for Windows only.** Not supported in claude.ai on the web or in the
  mobile apps: remote connectors there are called from Anthropic's cloud, which cannot reach
  a program on your computer. Open the ArthurLegal Project from Claude Desktop.
- **Pseudonymisation, not anonymisation.** Detection is probabilistic, and data-protection,
  trade-secret and confidentiality obligations remain with the user and the company.

Setup: [KURULUM.md](KURULUM.md) Step 5 · user guide (Turkish): [ARTHUR-MASK.md](ARTHUR-MASK.md). The system prompt's section 9 tells the assistant how to use the
`arthur_mask_*` tools; `knowledge/references/arthur-mask-rehberi.md` answers setup and
troubleshooting questions.

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
| **OpenCaseLaw.ch** | MCP — `mcp.opencaselaw.ch/sse` | None | Switzerland — 972K+ federal and cantonal decisions + Fedlex legislation integration (CC0) — 33 tools |
| **CourtListener** | MCP — official server, Anthropic connector directory | OAuth 2.0 (dynamic client registration) | **United States case law** — federal and state opinions, PACER dockets, citation network, oral arguments, and **citation verification** (fabricated-citation defence). Operated by Free Law Project. See `courtlistener-rehberi.md` |
| **ArthurLegal MCP** | MCP — `arthurlegal-mcp.fly.dev/mcp` | None | **Türkiye + 14 jurisdictions behind one connector — 104 tools.** 🇹🇷 Türkiye (`tr_`, 23 tools): Yargıtay, Danıştay, regional and local courts, KYB, Constitutional Court, Uyuşmazlık Mahkemesi, 12 legislation types with article tree and gerekçe, Official Gazette, eight regulators (Rekabet, EPDK, SPK, BDDK, KVKK, BTK, GİB, Sigorta Tahkim) and a 19,404-document semantic archive · 🇦🇿 Azerbaijan, in-force status verified (`az_`) · 🇦🇹 Austria (`at_`) · 🇩🇪 Germany (`de_`) · 🇳🇱 Netherlands (`nl_`) · 🇵🇱 Poland (`pl_`) · 🇪🇸 Spain (`es_`) · 🇫🇮 Finland (`fi_`) · 🇮🇪 Ireland (`ie_`) · 🇬🇧 UK (`uk_`) · 🇪🇺 EU/CJEU (`eu_`) · 🇯🇵 Japan (`jp_`) · GLEIF (`gleif_`) · 10 scholarship indexes incl. 19 Turkish law journals (`scholar_`) · 5,125 signed petroleum & mining contracts (`contracts_`) |
| **TR Legal MCP** (optional) | MCP — `yargi-mcp-pro-production.up.railway.app/mcp` | OAuth (WorkOS) | Only for what the Turkish backend deliberately omits: ECHR, KİK, Sayıştay, Reklam Kurulu, KDK, TBB, HSK. Paid server by [saidsurucu](https://github.com/saidsurucu) |
| **OpenSanctions** | REST API — `api.opensanctions.org` | API key | Sanctions / PEP screening (paid membership) |
| **Fedlex** | MCP — Anthropic connector directory *(WebFetch fallback: `fedlex.admin.ch`)* | None | **Swiss federal legislation** — article text, full statute text, amendment history, title search |
| **KAP + e-ŞİRKET** | WebFetch — `kap.org.tr`, `e-sirket.mkk.com.tr` | None | Turkish public-company disclosures |

**Jurisdictions reached via WebFetch** (no additional connector required):
🇬🇧 UK · 🇺🇸 US *(federal legislation — GovInfo; case law is via the CourtListener MCP above)* · 🇪🇺 EU / CJEU / ECHR · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU *(sanctions / KYC only)* · 🇨🇳 CN · 🇷🇸 RS · 🇦🇿 AZ *(case law + English-language sources; legislation via ArthurLegal MCP (`az_`))*

**The 22 jurisdictions** = 12 national (🇹🇷 TR · 🇨🇭 CH · 🇺🇸 US · 🇦🇿 AZ · 🇬🇧 UK · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU · 🇨🇳 CN · 🇷🇸 RS) + 2 supranational legal orders (🇪🇺 EU/CJEU · ECHR).

**Coverage depth is not uniform**, and the package says so rather than papering
over it. Türkiye has the deepest coverage (inside ArthurLegal MCP under `tr_`: courts, legislation, Official Gazette, eight regulators and a semantic archive, plus the largest share of the reference layer); Switzerland, the United
States and Azerbaijan follow with primary-source MCP access; the WebFetch
jurisdictions provide legislation and, where available, case law. When scope
narrows, the assistant states it in the output.

The Turkish backend ([`ArthurLegalTR`](https://github.com/beerbottle90/arthurlegal-mcp/tree/master/arthur-tr-hukuk-mcp), MIT) reuses endpoint knowledge from [saidsurucu](https://github.com/saidsurucu)'s open-source yargi-mcp and mevzuat-mcp; sources whose official endpoints do not answer reliably (KİK, Sayıştay, TÜRKPATENT, İSTAÇ) are left out rather than shipped as stubs.
**ArthurLegal MCP is auth-free** — anyone with the URL can call every tool, so no
company secret, negotiating position or confidential draft goes into a query.
Every tool carries its jurisdiction as a prefix, because `get_act` means five
different things across the underlying servers. The `status` tool reports each
jurisdiction's index size and `index_coverage`: a statute outside that range is
not found, and the search returns its nearest neighbour rather than saying so.
Installing it is **optional** — without it the package still works, and the
assistant notes the narrowed scope in its output.

---

## Installation — 6 steps, ~25 minutes

Full guide → [KURULUM.md](KURULUM.md) (Turkish).

1. **Create a new Claude.ai Project** — [claude.ai/projects](https://claude.ai/projects) → "+ New Project".
2. **Paste `SYSTEM_PROMPT.md`** into the Custom Instructions field.
3. **Upload the 103 files** in `knowledge/` to Project Knowledge (bulk drag-and-drop per folder).
4. **Add the ArthurLegal MCP connector** — URL: `https://arthurlegal-mcp.fly.dev/mcp` (no auth; Türkiye under `tr_` plus 14 jurisdictions — KURULUM.md Step 4). Optional: OpenCaseLaw.ch · CourtListener · Fedlex (Step 4b) · TR Legal MCP for ECHR/KİK/Sayıştay (Step 4d).
5. **Install Arthur Mask** (recommended, optional; Windows + Claude Desktop) — download `ArthurMask-Kurulum.exe` from [this direct download link](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe), fully restart Claude Desktop, check `arthur-mask` under Settings → Developer (KURULUM.md Step 5).
6. **Fill the `[DOLDUR]` placeholders** in `knowledge/company-profile.md` for your own organization — or have the assistant do it with `/<plugin>:cold-start-interview`.

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
ArthurLegal-CorporateAssistant-v1.8.0-Public-Release/
├── KURULUM.md             ← Installation guide, Turkish (start here)
├── ARTHUR-MASK.md         ← Arthur Mask user guide (Turkish)
├── SYSTEM_PROMPT.md       ← Claude.ai Custom Instructions text
├── README.md              ← This file
├── CHANGELOG.md           ← Release notes
├── VERSION.md             ← 1.8.0
├── ATTRIBUTION.md         ← Attribution
├── LICENSE                ← Proprietary — Non-Commercial
└── knowledge/             ← 103 files to upload to Project Knowledge
    ├── company-profile.md       (organization profile template — ships with [DOLDUR] placeholders)
    ├── skills/                  (12 consolidated skill books, one file per plugin)
    ├── references/              (83 references: legislation, jurisdictions, MCP guides, Arthur Mask)
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
- **Arthur Mask pseudonymises; it does not anonymise.** Detection is probabilistic; dates and amounts are deliberately left unmasked; images, handwriting, signatures, stamps and QR codes in scans are not masked. It works only with Claude Desktop for Windows.
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
