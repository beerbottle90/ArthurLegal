# ArthurLegal Law Firm Assistant — Installation Guide

**Version:** 1.7.0 | **Updated:** 2026-09-06

---

## Requirements

| Requirement | Details |
|---|---|
| Claude.ai account | Pro or Team plan (required for Projects feature) |
| ArthurLegal MCP | `https://arthurlegal-mcp.fly.dev/mcp` — one connector, Türkiye + 14 jurisdictions, 104 tools, no auth (Step 4) |
| TR Legal MCP | yargi-mcp-pro connector — only for ECHR, KİK, Sayıştay, Reklam Kurulu, KDK, TBB, HSK (optional — Step 4b) |
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

**Source:** `github.com/beerbottle90/arthurlegal-mcp` (Turkish backend: `github.com/beerbottle90/arthurlegal-mcp/tree/main/ArthurLegalTR`) — hosted on Fly.io,
indexes baked into the image, semantic search via Voyage AI (`voyage-4-lite`).

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

## Step 5 — OpenSanctions API (optional)

For sanctions screening and KYC:
1. Get an API key at [opensanctions.org](https://www.opensanctions.org/)
2. Claude.ai → Project Settings → **Environment Variables**
3. Set `OPENSANCTIONS_API_KEY` = `[your API key]`

---

## Step 6 — Complete the Firm Profile

In your first conversation, run:

```
/firm-operations:cold-start-interview
```

This takes ~20-30 minutes and interactively fills in the `[DOLDUR]` fields in `knowledge/firm-profile.md`. **Run this before any other plugin** — all plugins read from this profile.

---

## Step 7 — Run Practice Area Cold-Starts

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

**Q: What if I hit the knowledge file limit?**
A: Keep core Turkish law references; temporarily add/remove international jurisdiction references as needed for specific matters.

**Q: The assistant says "This skill doesn't exist in this plugin." What do I do?**
A: Type `/<plugin>:` — the assistant will list all available skills for that plugin.

---

## Update Notes

This is version **1.6.2**. See `CHANGELOG.md` for what changed.

Feedback and support: Open an issue on the project's GitHub page.
