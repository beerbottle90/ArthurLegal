# ArthurLegal — Claude Law Firm Assistant

**Version:** v1.9.1 · **Date:** 2026-09-22 · **License:** Proprietary — Non-Commercial (see [LICENSE](LICENSE))
**Target environment:** [Claude.ai Projects](https://claude.ai/projects) (web and Claude Desktop; Arthur Mask requires Claude Desktop for Windows)

> **Multi-jurisdiction legal assistant package for small-to-mid law firms (0–30 staff)**, built on Claude and packaged as a Claude.ai Projects bundle — `SYSTEM_PROMPT.md` + 128 knowledge files + up to 5 MCP connectors + the optional local Arthur Mask privacy gate, covering **28 jurisdictions**.
>
> Derived from Anthropic's [claude-for-legal](https://github.com/anthropics/claude-for-legal) reference package.

> ### ⬇ Arthur Mask — mask documents on your own computer before Claude sees them
> **[Download the installer (Windows, about 1 GB)](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)**. The link downloads directly; no GitHub account needed.
> Double-click the downloaded `ArthurMask-Kurulum.exe`. Step-by-step guide: **[ARTHUR-MASK.md](ARTHUR-MASK.md)** (Türkçe) · English: [ARTHUR-MASK-EN.md](ARTHUR-MASK-EN.md)
> Requires Claude Desktop for Windows; it does not work in claude.ai on the web or in the mobile apps.
>
> **Türkçe:** [Kurulum dosyasını indirin](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe), inen dosyaya çift tıklayın; anlatım [ARTHUR-MASK.md](ARTHUR-MASK.md).

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

Version history and the full v1.0.1 → v1.9.1 progression: [CHANGELOG.md](CHANGELOG.md).

---

## Arthur Mask — local privacy gate (new in v1.8.0)

Client documents can now be masked **on the lawyer's own Windows computer** before Claude
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
  the lawyer writes a justification; an exit gate that re-scans every response sent to
  Claude against the vault; a log of everything sent and a one-click leak check.
- **Fully offline.** Detection and OCR models ship inside the installer. The only other
  network call is a once-a-day update check that reads the latest version number.
- **Claude Desktop for Windows only.** Not supported in claude.ai on the web or in the
  mobile apps: remote connectors there are called from Anthropic's cloud, which cannot reach
  a program on your computer. Open the ArthurLegal Project from Claude Desktop.
- **Pseudonymisation, not anonymisation.** Detection is probabilistic, and professional
  secrecy and data-protection obligations remain with the lawyer.

Setup: [INSTALLATION.md](INSTALLATION.md) Step 5 · user guide: [ARTHUR-MASK-EN.md](ARTHUR-MASK-EN.md)
([Türkçe](ARTHUR-MASK.md)). The system prompt's section 9 tells the assistant how to use the
`arthur_mask_*` tools; `knowledge/references/arthur-mask-rehberi.md` answers setup and
troubleshooting questions.

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
| **OpenCaseLaw.ch** | MCP — `mcp.opencaselaw.ch/sse` | None | Swiss case law — 972K+ federal and cantonal decisions + Fedlex legislation integration (CC0) — 33 tools |
| **CourtListener** | MCP — official server, Anthropic connector directory | OAuth 2.0 (dynamic client registration) | **United States case law** — federal and state opinions, PACER dockets, citation network, oral arguments, and **citation verification** (fabricated-citation defence). Operated by Free Law Project. See `courtlistener-rehberi.md` |
| **ArthurLegal MCP** | MCP — `arthurlegal-mcp.fly.dev/mcp` | None | **Türkiye + 14 jurisdictions behind one connector — 104 tools.** 🇹🇷 Türkiye (`tr_`, 23 tools): Yargıtay, Danıştay, regional and local courts, KYB, Constitutional Court, Uyuşmazlık Mahkemesi, 12 legislation types with article tree and gerekçe, Official Gazette, eight regulators (Rekabet, EPDK, SPK, BDDK, KVKK, BTK, GİB, Sigorta Tahkim) and a 19,498-document semantic archive · 🇦🇿 Azerbaijan, in-force status verified (`az_`) · 🇦🇹 Austria (`at_`) · 🇩🇪 Germany (`de_`) · 🇳🇱 Netherlands (`nl_`) · 🇵🇱 Poland (`pl_`) · 🇪🇸 Spain (`es_`) · 🇫🇮 Finland (`fi_`) · 🇮🇪 Ireland (`ie_`) · 🇬🇧 UK (`uk_`) · 🇪🇺 EU/CJEU (`eu_`) · 🇯🇵 Japan (`jp_`) · GLEIF (`gleif_`) · 10 scholarship indexes incl. 19 Turkish law journals (`scholar_`) · 5,125 signed petroleum & mining contracts (`contracts_`) |
| **TR Legal MCP** (optional) | MCP — `yargi-mcp-pro-production.up.railway.app/mcp` | OAuth (WorkOS) | Only for what the Turkish backend deliberately omits: ECHR, KİK, Sayıştay, Reklam Kurulu, KDK, TBB, HSK. Paid server by [saidsurucu](https://github.com/saidsurucu) |
| **OpenSanctions** | REST API — `api.opensanctions.org` | API key | Client sanctions / PEP / KYC screening |
| **Fedlex** | MCP — Anthropic connector directory *(WebFetch fallback: `fedlex.admin.ch`)* | None | **Swiss federal legislation** — article text, full statute text, amendment history, title search |

**Jurisdictions reached via WebFetch** (no additional connector required):
🇬🇧 UK · 🇺🇸 US *(federal legislation — GovInfo; case law is via the CourtListener MCP above)* · 🇪🇺 EU / CJEU / ECHR · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU *(sanctions / KYC only)* · 🇨🇳 CN · 🇷🇸 RS · 🇦🇿 AZ *(case law + English-language sources; legislation via ArthurLegal MCP (`az_`))*

**The 22 jurisdictions** = 20 national (🇹🇷 TR · 🇨🇭 CH · 🇺🇸 US · 🇦🇿 AZ · 🇬🇧 UK · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU · 🇨🇳 CN · 🇷🇸 RS · 🇦🇪 AE · 🇨🇿 CZ · 🇬🇪 GE · 🇮🇱 IL · 🇰🇿 KZ · 🇺🇿 UZ · 🇷🇴 RO · 🇺🇦 UA · 🇬🇷 GR) + 2 supranational legal orders (🇪🇺 EU/CJEU · ECHR).

**Coverage depth is not uniform**, and the package says so rather than papering
over it. Türkiye has the deepest coverage (inside ArthurLegal MCP under `tr_`: courts, legislation, Official Gazette, eight regulators and a semantic archive, plus the largest share of the reference layer); Switzerland, the
United States and Azerbaijan follow with primary-source MCP access; the WebFetch
jurisdictions provide legislation and, where available, case law. When scope
narrows, the assistant states it in the output.

> **ArthurLegal MCP is auth-free** — anyone with the URL can call every tool, so
> no client name, matter number or confidential draft goes into a query. Every
> tool carries its jurisdiction as a prefix, because `get_act` means five
> different things across the underlying servers. The `status` tool reports each
> jurisdiction's index size and `index_coverage`: a statute outside that range is
> not found, and the search returns its nearest neighbour rather than saying so.
> Installing it is **optional** — without it the package still works and the
> assistant notes the narrowed scope. Setup: [INSTALLATION.md](INSTALLATION.md)
> Step 4 (jurisdiction connectors: Step 4a).
>
> ⚠️ **Professional secrecy:** all three are **public** search tools — never send a
> client name, a matter summary or a confidential draft; queries must be framed as
> abstract legal concepts.

---

## Installation — 8 steps

English guide → [INSTALLATION.md](INSTALLATION.md)
Turkish guide → [KURULUM.md](KURULUM.md)

**Summary:**
1. Claude.ai → Projects → New Project
2. `SYSTEM_PROMPT.md` → Custom Instructions
3. `knowledge/` folder → Upload Files
4. Add the ArthurLegal MCP connector (Türkiye under `tr_` plus 14 jurisdictions, no auth — Step 4); then, per client portfolio, CourtListener · Fedlex · OpenCaseLaw.ch (Step 4a) and, only if ECHR/KİK/Sayıştay work is needed, TR Legal MCP (Step 4b)
5. Arthur Mask on Windows with Claude Desktop (recommended, optional — Step 5)
6. OpenSanctions API key (optional)
7. Run `/firm-operations:cold-start-interview`
8. Run the practice-area cold-starts

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
ArthurLegal-Law-Firm-v1.9.1-Public-Release/
├── INSTALLATION.md         ← English installation guide
├── KURULUM.md              ← Turkish installation guide
├── ARTHUR-MASK.md          ← Arthur Mask user guide (Turkish)
├── ARTHUR-MASK-EN.md       ← Arthur Mask user guide (English)
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
    └── references/         ← 94 references: legislation + international jurisdictions + MCP guides + Arthur Mask
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
- **Arthur Mask pseudonymises; it does not anonymise.** Detection is probabilistic; dates and amounts are deliberately left unmasked; images, handwriting, signatures, stamps and QR codes in scans are not masked. It works only with Claude Desktop for Windows.
- **Family / inheritance and specialist maritime law are out of scope** — referral to another specialist is recommended.

---

## Personal data notice

The public release of this package contains **no real personal, company or client
data**. All such fields are marked with `[DOLDUR]` placeholders. The example firm
(`ArthurLegal Hukuk Bürosu`) is entirely fictional.

⚠️ **Professional secrecy reminder:** when adapting the package to your own firm,
do not write real client information into the knowledge files. Keep matter folders
**isolated across matters**. To give Claude a client document, mask it first with Arthur Mask
(Claude Desktop, Windows) — see [ARTHUR-MASK-EN.md](ARTHUR-MASK-EN.md).

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
