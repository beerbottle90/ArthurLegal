# ArthurLegal Law Firm Assistant — Installation Guide

**Version:** 1.8.1 | **Updated:** 2026-09-17

---

## Requirements

| Requirement | Details |
|---|---|
| Claude.ai account | Pro or Team plan (required for Projects feature) |
| ArthurLegal MCP | `https://arthurlegal-mcp.fly.dev/mcp` — one connector, Türkiye + 14 jurisdictions, 104 tools, no auth (Step 4) |
| TR Legal MCP | yargi-mcp-pro connector — only for ECHR, KİK, Sayıştay, Reklam Kurulu, KDK, TBB, HSK (optional — Step 4b) |
| Arthur Mask | Local privacy gate that masks documents on your computer; Windows 10/11 64-bit + Claude Desktop (recommended, optional — Step 5) |
| OpenSanctions API key | For sanctions screening (optional) |

---

## Step 1 — Create a Claude.ai Project

1. Go to [claude.ai](https://claude.ai) → **Projects** → **New Project**
2. Name the project (e.g. "Law Firm Assistant")

---

## Step 2 — Load the System Prompt

1. Project → **Customize** → **Custom Instructions**
2. Copy the **entire contents** of `SYSTEM_PROMPT.md` and paste it
3. Click **Save**

---

## Step 3 — Upload Knowledge Files

Project → **Add Content** → **Upload Files**

Upload files in the following order:

### First — Core firm profile (required)
```
knowledge/firm-profile.md
```

### Practice area profiles
```
knowledge/profiles/administrative-litigation.md
knowledge/profiles/commercial-advisory.md
knowledge/profiles/corporate-advisory.md
knowledge/profiles/criminal-defense.md
knowledge/profiles/dispute-litigation.md
knowledge/profiles/employment-advisory.md
knowledge/profiles/firm-operations.md
knowledge/profiles/ip-advisory.md
knowledge/profiles/tax-litigation.md
knowledge/profiles/legal-research.md          <- source layer (v1.4.0)
```

### Skill files (all plugins)
```
knowledge/skills/administrative-legal__skills.md
knowledge/skills/advocacy-legal__skills.md
knowledge/skills/contract-drafting__skills.md
knowledge/skills/expert-opinion__skills.md
knowledge/skills/legal-research__skills.md          <- source layer (v1.4.0)
knowledge/skills/commercial-legal__skills.md
knowledge/skills/corporate-legal__skills.md
knowledge/skills/criminal-defense__skills.md
knowledge/skills/employment-legal__skills.md
knowledge/skills/energy-finance__skills.md
knowledge/skills/firm-operations__skills.md
knowledge/skills/ip-legal__skills.md
knowledge/skills/litigation-legal__skills.md
knowledge/skills/privacy-legal__skills.md
knowledge/skills/regulatory-legal__skills.md
knowledge/skills/tax-legal__skills.md
```

### Agent definitions (optional — for scheduled/automated tasks)
```
knowledge/agents/commercial-legal__deal-debrief.md
knowledge/agents/commercial-legal__playbook-monitor.md
knowledge/agents/commercial-legal__renewal-watcher.md
knowledge/agents/corporate-legal__dataroom-watcher.md
knowledge/agents/employment-legal__leave-tracker.md
knowledge/agents/ip-legal__ip-renewal-watcher.md
knowledge/agents/regulatory-legal__reg-change-monitor.md
```

### Reference guides (select based on your practice needs)

**Core Turkish law references (recommended):**
```
knowledge/references/kanun-kisaltmalar.md
knowledge/references/hmk-rehberi.md
knowledge/references/iyuk-rehberi.md
knowledge/references/uyap-rehberi.md
knowledge/references/idari-yargi-yapisi-rehberi.md
knowledge/references/mevzuat-mcp-rehberi.md
knowledge/references/yargi-mcp-rehberi.md
knowledge/references/opensanctions-rehberi.md
knowledge/references/kvkk-m11-cevap-sablonu.md
knowledge/references/conflict-check-rehberi.md
knowledge/references/masak-kimlik-tespit-rehberi.md
knowledge/references/mesleki-sir-rehberi.md
knowledge/references/karsilastirmali-hukuk-rehberi.md
```

**Source-layer MCP guides (v1.4.0 — if you set up Step 4b):**
```
knowledge/references/eqanun-mcp-rehberi.md          <- AZ legislation (PRIMARY)
knowledge/references/lex-scholar-rehberi.md         <- legal scholarship + DergiPark (SECONDARY)
knowledge/references/resourcecontracts-rehberi.md   <- signed PSA/JOA precedent (BENCHMARK)
```

**Arthur Mask (v1.8.0 — recommended if you set up Step 5):**
```
knowledge/references/arthur-mask-rehberi.md        <- local masking, tool rules, troubleshooting
```

**Sector-specific references:**
```
knowledge/references/epdk-rehberi.md          ← Energy sector
knowledge/references/smk-rehberi.md           ← IP / industrial property
knowledge/references/turkpatent-rehberi.md    ← Trademark / patent
knowledge/references/istac-rehberi.md         ← Arbitration (ISTAC)
knowledge/references/transfer-pricing-rehberi.md ← Transfer pricing
knowledge/references/damga-vergisi-rehberi.md ← Stamp duty
knowledge/references/isg-dava-rehberi.md      ← Occupational safety litigation
knowledge/references/seveso-buyuk-kaza-rehberi.md ← Major industrial accidents
```

**International jurisdictions (select based on client portfolio):**
```
knowledge/references/uk-legislation-rehberi.md
knowledge/references/us-legislation-rehberi.md
knowledge/references/courtlistener-rehberi.md
knowledge/references/eu-legislation-rehberi.md
knowledge/references/germany-legislation-rehberi.md
knowledge/references/france-legislation-rehberi.md
knowledge/references/italy-legislation-rehberi.md
knowledge/references/japan-legislation-rehberi.md
knowledge/references/switzerland-caselaw-rehberi.md
knowledge/references/azerbaycan-hukuk-rehberi.md
knowledge/references/cin-hukuku-rehberi.md
knowledge/references/sirbistan-hukuku-rehberi.md
knowledge/references/russia-legislation-rehberi.md  ← KYC / sanctions only
knowledge/references/karsilastirmali-hukuk-rehberi.md
```

> **⚠️ Note:** Be mindful of Claude.ai Projects knowledge file limits. Start with core references and add more as needed.

---

## Step 4 — Connect ArthurLegal MCP (Türkiye + 14 jurisdictions, one endpoint)

Project → **Customize** → **Connectors** → **+ Add custom connector**

| | |
|---|---|
| **Name** | `arthurlegal` |
| **URL** | `https://arthurlegal-mcp.fly.dev/mcp` |
| **Auth** | **None** |

One endpoint, 15 backends, 104 tools. Türkiye is inside this connector under the `tr_`
prefix (23 tools) — no separate Turkish-law connector is needed.

| Prefix | Coverage |
|---|---|
| `tr_` | 🇹🇷 Türkiye — Yargıtay, Danıştay, regional and local courts, KYB (Bedesten) · Constitutional Court · Uyuşmazlık Mahkemesi · 12 legislation types with article tree and gerekçe · Official Gazette · 8 regulators (Rekabet, EPDK, SPK, BDDK, KVKK, BTK, GİB, Sigorta Tahkim) · a 19,404-document semantic archive |
| `es_` | 🇪🇸 Spain — BOE consolidated legislation (12,376 acts, indexed) |
| `pl_` | 🇵🇱 Poland — Dz.U. legislation (indexed) |
| `nl_` | 🇳🇱 Netherlands — case law + legislation (KOOP full text) |
| `fi_` | 🇫🇮 Finland — consolidated acts (indexed) |
| `ie_` | 🇮🇪 Ireland — Acts of the Oireachtas (indexed) |
| `at_` | 🇦🇹 Austria — RIS legislation + case law |
| `de_` | 🇩🇪 Germany — federal legislation + BVerfG/BGH/BAG/BFH/BVerwG |
| `az_` | 🇦🇿 Azerbaijan — e-qanun, **in-force status verified** |
| `scholar_` | 🌍 Legal scholarship — 10 indexes incl. 19 Turkish law journals (DergiPark) |
| `contracts_` | 🌍 5,125 signed PSA/JOA contracts |
| `uk_` | 🇬🇧 United Kingdom — legislation + **unapplied amendments** |
| `eu_` | 🇪🇺 EU — legislation + CJEU case law (CELLAR) |
| `jp_` | 🇯🇵 Japan — legislation with computed in-force status |
| `gleif_` | 🌍 Legal-entity identity + group structure (LEI) |

> ⚠️ **Prefixes are mandatory.** `get_act` means five different things across the
> underlying servers; call tools by their prefixed names: `tr_ictihat_ara`, `az_get_act`.

> ⚠️ **No authentication.** Anyone with the URL can call every tool. They search public
> sources only; never send a client name, matter number or confidential draft
> (Av. K. m. 36 — see `mesleki-sir-rehberi.md`).

**Verify coverage yourself.** The `status` tool reports each jurisdiction's index size,
`index_coverage` and whether semantic search is live; the Türkiye row shows how many
documents each regulator has indexed.

**Test:**
```
"TBK m. 6"                                   → tr_mevzuat_ara + tr_mevzuat_madde_getir
"Yargıtay 9. HD iş kazası"                   → tr_ictihat_ara(chamber="H9")
"EPDK lisanssız üretim kararları"            → tr_kurum_karari_ara(kurum="epdk")
"kişisel verilerin korunması" (Spain)        → es_search_legislation → LO 15/1999, LO 7/2021
```

**Source:** `github.com/beerbottle90/arthurlegal-mcp` (Turkish backend: `github.com/beerbottle90/arthurlegal-mcp/tree/master/arthur-tr-hukuk-mcp`) — hosted on Fly.io,
indexes baked into the image, semantic search via Voyage AI (`voyage-4-lite`).

> **Connect directly, without the package.** The same endpoint works on its own in any MCP client
> (Streamable HTTP, no auth):
> - **Claude (claude.ai / Claude Desktop):** Settings → Connectors → Add custom connector, URL `https://arthurlegal-mcp.fly.dev/mcp`
> - **Claude Code:** `claude mcp add --transport http arthurlegal https://arthurlegal-mcp.fly.dev/mcp`
> - **Clients with a JSON config such as Cursor or VS Code:** `{"mcpServers": {"arthurlegal": {"url": "https://arthurlegal-mcp.fly.dev/mcp"}}}`
> - **Clients that only launch local (stdio) servers:** use `npx -y mcp-remote https://arthurlegal-mcp.fly.dev/mcp` as the command
>
> Once connected, call the `status` tool. Details: [github.com/beerbottle90/arthurlegal-mcp](https://github.com/beerbottle90/arthurlegal-mcp#use-it-directly)

> **Without it** the package still works: these fifteen jurisdictions fall back to WebFetch
> (no Turkish case-law search; AZ in-force status **unverified**), scholarship and contract
> precedent drop out — and the assistant says so in its output.

---

## Step 4a — Jurisdiction connectors (optional)

Add these where your client portfolio touches the jurisdiction.

**From the Anthropic connector directory** (no custom connector needed —
**Customize → Connectors → Browse Connectors** → select → **Add**):

| Connector | Auth | Coverage |
|---|---|---|
| **CourtListener** | OAuth 2.0 (dynamic client registration — no pre-registration, no API key) | **US case law** — federal and state opinions, PACER dockets, citation network, oral arguments, and **citation verification** (Free Law Project) |
| **Fedlex** | None | **Swiss federal legislation** — article text, full statute text, amendment history |

**As custom connectors** (**+ Add custom connector** → *Name* + *URL*):

| Connector | URL | Auth | Coverage |
|---|---|---|---|
| `OpenCaseLaw.ch` | `https://mcp.opencaselaw.ch/sse` | None | Swiss case law — 972K+ federal and cantonal decisions (33 tools, CC0) |

> ⚠️ **Citation verification is mandatory.** Before citing any US decision, verify
> it in CourtListener — does the case exist, is the citation correct, has it been
> overruled? An unverified decision is tagged `[model knowledge — verify]` and
> never `[CourtListener]`. Every US citation that goes into a pleading passes this
> check. See `courtlistener-rehberi.md`.

> Without the Fedlex connector, Swiss legislation still works over WebFetch
> (`fedlex.admin.ch`) — see `switzerland-caselaw-rehberi.md`.

**Jurisdictions needing no connector** (automatic via WebFetch / direct API):
🇬🇧 UK · 🇺🇸 US legislation (GovInfo — free API key) · 🇪🇺 EU/CJEU/ECHR · 🇩🇪 DE ·
🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU *(sanctions / KYC only)* · 🇨🇳 CN · 🇷🇸 RS ·
🇦🇿 AZ *(case law / English sources — legislation via Step 4)*

---

## Step 4b — TR Legal MCP (optional: ECHR, KİK, Sayıştay, Reklam Kurulu, KDK, TBB, HSK)

The Turkish backend of ArthurLegal MCP deliberately does not carry these sources, because
their official endpoints do not answer reliably or they are out of scope: **KİK** (the signed
EKAP v2 API returns 500), **Sayıştay** (its WAF answers 418 to every query), **TÜRKPATENT**
(no decision database; the portal is reCAPTCHA-gated), **İSTAÇ** (site unreachable), **ECHR**,
**Reklam Kurulu**, **KDK**, **TBB**, **HSK**. If your matters need them, add saidsurucu's
paid **yargi-mcp-pro** server as a second connector:

1. Project → **Customize** → **Connectors** → **Add MCP Server**
2. **URL:** `https://yargi-mcp-pro-production.up.railway.app/mcp` — **Auth:** OAuth 2.0 (WorkOS)

The assistant uses it only for those sources (`aihm_ictihat_ara`,
`kurum_karari_ara(kurum="kik" | "sayistay" | "reklam" | "kdk" | "tbb" | "hsk")`); legislation,
case law and the other regulators go through the `tr_` tools first. Without it those sources
are fetched over WebFetch or reported as "not retrieved" — a source that does not work is
never presented as working.

---

## Step 5 — Arthur Mask (recommended, optional: mask documents on your own computer)

Arthur Mask masks client documents **on your own computer** before Claude sees them: names,
companies, national ID and tax numbers, IBANs, addresses, phone numbers, e-mail addresses and
file numbers become labels such as `{{KİŞİ-01}}` or `{{ŞİRKET-02}}`, and the real values stay in
an encrypted vault on your computer. Claude receives only the masked text; its answer is turned
back into real names locally and opened in Word or as a UDF file. The app works offline.

> ⚠️ **Claude Desktop for Windows only.** It does not work in claude.ai on the web or in the
> mobile apps: remote connectors on claude.ai are called from Anthropic's cloud, which cannot
> reach a program on your computer. Open your ArthurLegal Project from Claude Desktop; Projects
> are shared between web and desktop.

**Requirements:** Windows 10 or 11 (64-bit) · [Claude Desktop](https://claude.ai/download) ·
about 4 GB free disk · 8 GB RAM recommended.

1. **Download.** **[⬇ Click here to download the Arthur Mask installer](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** (Windows, about 1 GB).
   No GitHub account or GitHub knowledge is needed: the link downloads `ArthurMask-Kurulum.exe` straight into
   your **Downloads** folder. Depending on your connection this can take a few minutes. If the browser asks
   whether to keep the file, choose **Keep**. When the download finishes, double-click the file in Downloads.
2. **Run it.** The installer is not code-signed; if SmartScreen says **"Windows protected your
   PC"** (Turkish: "Windows bilgisayarınızı korudu"), choose **More info** → **Run anyway**.
   Antivirus software may scan the file for a while.
3. **Install.** No administrator rights (`%LOCALAPPDATA%\Programs\Arthur Mask`). The installer
   registers the `arthur-mask` connector in Claude Desktop's configuration and keeps a backup of
   the previous configuration file.
4. **Restart Claude Desktop:** quit **completely**, including the system tray icon, and reopen.
5. **Verify:** Claude Desktop → **Settings → Developer** lists `arthur-mask` as running; the
   tools menu in a chat shows the Arthur Mask tools.
6. **Store the recovery key:** Arthur Mask → **Kurtarma anahtarı** → print it or store it
   safely → **Sakladım**. Never type the key into Claude.

**Test:** drop a sample document into Arthur Mask, approve the review, and paste the command it
shows (`Arthur Mask'teki belge-1'i incele`) into the ArthurLegal Project chat in Claude Desktop.
Do not also attach the original document.

Everyday use, red line, leak check and troubleshooting: [ARTHUR-MASK-EN.md](ARTHUR-MASK-EN.md).

> **Without it** the package works as before. When identifiable personal data is pasted into a
> chat, the assistant adds one short, non-blocking reminder per conversation. Arthur Mask
> pseudonymises; it does not anonymise, and data protection and professional secrecy
> obligations remain with the lawyer.

---

## Step 6 — OpenSanctions API (optional)

For sanctions screening and KYC:
1. Get an API key at [opensanctions.org](https://www.opensanctions.org/)
2. Claude.ai → Project Settings → **Environment Variables**
3. Set `OPENSANCTIONS_API_KEY` = `[your API key]`

---

## Step 7 — Complete the Firm Profile

In your first conversation, run:

```
/firm-operations:cold-start-interview
```

This takes ~20-30 minutes and interactively fills in the `[DOLDUR]` fields in `knowledge/firm-profile.md`. **Run this before any other plugin** — all plugins read from this profile.

---

## Step 8 — Run Practice Area Cold-Starts

For each active practice area:

```
/commercial-legal:cold-start-interview
/corporate-legal:cold-start-interview
/litigation-legal:cold-start-interview
/employment-legal:cold-start-interview
/tax-legal:cold-start-interview
/administrative-legal:cold-start-interview
/ip-legal:cold-start-interview
/criminal-defense:cold-start-interview
/privacy-legal:cold-start-interview
/regulatory-legal:cold-start-interview
```

You can skip cold-starts for practice areas you don't use.

---

## Core Commands

| Command | Function |
|---|---|
| `/firm-operations:new-client-intake` | New client intake workflow |
| `/firm-operations:conflict-check` | Conflict of interest check |
| `/commercial-legal:nda-review` | NDA review |
| `/litigation-legal:case-intake` | Open a new litigation file |
| `/criminal-defense:cmk-gorev-atama` | CMK assignment management |
| `/<plugin>:cold-start-interview` | Configure a plugin profile |

To list all available commands for a plugin:
```
/<plugin>:
```
(Leave blank — the assistant will list all skills for that plugin)

---

## FAQ

**Q: Do I have to fill in all `[DOLDUR]` fields right now?**
A: No. When the assistant encounters `[DOLDUR]`, it will prompt you to run the cold-start interview. You can start working immediately and fill in details progressively.

**Q: Should I put real client names in firm-profile.md?**
A: NO. Use aggregate statistics and pseudonyms only. Real client data must never be written to knowledge files (attorney-client privilege + KVKK).

**Q: How do I give a client document to Claude safely?**
A: If you use Claude Desktop on Windows, drop the document into Arthur Mask first, approve the review, and paste only the command it shows into the chat; do not attach the original. Claude sees only the masked text. Masking is pseudonymisation, not anonymisation, and detection is probabilistic: check the masked copy before sending and use the "Claude'a giden" panel and the leak check. Responsibility under KVKK, professional secrecy (Av. K. m. 36), trade secret rules and NDAs stays with the lawyer. Arthur Mask does not work in claude.ai on the web or on mobile; there, remove identifiable client data yourself before sharing. Details: [ARTHUR-MASK-EN.md](ARTHUR-MASK-EN.md).

**Q: What if I hit the knowledge file limit?**
A: Keep core Turkish law references; temporarily add/remove international jurisdiction references as needed for specific matters.

**Q: The assistant says "This skill doesn't exist in this plugin." What do I do?**
A: Type `/<plugin>:` — the assistant will list all available skills for that plugin.

---

## Update Notes

This is version **1.8.1**. See `CHANGELOG.md` for what changed.

Upgrading from 1.8.0: only knowledge files changed (criminal-procedure deadlines under Law 7499). Replace these five files in Project knowledge: `knowledge/references/cmk-rehberi.md`, `knowledge/references/cmk-gorevli-rehberi.md`, `knowledge/references/dilekce-teknikleri-rehberi.md`, `knowledge/skills/advocacy-legal__skills.md`, `knowledge/skills/criminal-defense__skills.md`. `SYSTEM_PROMPT.md` changed only in its version label; pasting it again is optional. Connector URLs are unchanged.

Upgrading from v1.7.0: paste `SYSTEM_PROMPT.md` into Custom Instructions again (new section 9, Arthur Mask) and add `knowledge/references/arthur-mask-rehberi.md` to Project knowledge. To use Arthur Mask, follow Step 5 and open the Project from Claude Desktop. Connector addresses are unchanged.

Feedback and support: Open an issue on the project's GitHub page.
