# ArthurLegal Law Firm Assistant — Installation Guide

**Version:** 1.4.0 | **Updated:** 2026-07-26

---

## Requirements

| Requirement | Details |
|---|---|
| Claude.ai account | Pro or Team plan (required for Projects feature) |
| TR Legal MCP | yargi-mcp-pro connector (optional but recommended) |
| e-qanun / LexScholar / ResourceContracts MCP | self-hosted, no auth (optional — Step 4b) |
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

### New practice areas (v1.2.0)
```
knowledge/profiles/privacy-legal.md       ← GDPR / KVKK / data protection
knowledge/profiles/regulatory-legal.md    ← Regulatory / agency law
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

## Step 4 — Connect TR Legal MCP (recommended)

1. Project → **Customize** → **Connectors** → **Add MCP Server**
2. Connection details:
   - **URL:** `https://yargi-mcp-pro-production.up.railway.app/mcp`
   - **Auth:** OAuth 2.0 (WorkOS) — authorization screen will appear on first connection
3. Once connected, 40+ Turkish legislation and case law tools become available

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
🇦🇿 AZ *(case law / English sources — legislation via Step 4b)*

---

## Step 4b — Three new MCP servers (v1.4.0) — the source layer (optional)

All three are **self-hosted, auth-free** Streamable HTTP MCP servers. You run the
servers yourself, then for each one:

Project → **Customize** → **Connectors** → **Add custom connector** →
*Name* + *URL* → leave the Auth section **empty** (No authentication).

| # | Name | URL | Role | Guide |
|---|---|---|---|---|
| 1 | `e-qanun` | `https://<HOST>/mcp` | **Azerbaijani legislation — PRIMARY**, in-force status verified (6 tools) | `eqanun-mcp-rehberi.md` |
| 2 | `LexScholar` | `https://<HOST>/mcp` | Legal doctrine across 10 indexes (**incl. DergiPark, 19 Turkish law journals**) — SECONDARY (6 tools) | `lex-scholar-rehberi.md` |
| 3 | `ResourceContracts` | `https://<HOST>/mcp` | 5,125 signed PSA/JOA contracts — PRECEDENT (9 tools) | `resourcecontracts-rehberi.md` |

**Sunucu kaynakları:** `github.com/beerbottle90/eqanun-api` ·
`github.com/beerbottle90/lex-scholar-api` ·
`github.com/beerbottle90/resourcecontracts-api`
(umbrella: `github.com/beerbottle90/socar-api-s`)

**Yerel portlar (varsayılan):** e-qanun `8020` · LexScholar `8010` ·
ResourceContracts `8000`.

> ⚠️ **Host geçici tünelse** (`*.trycloudflare.com`) adres her yeniden
> başlatmada değişir → connector URL'sini güncellemeniz gerekir. Kalıcı kullanım
> için adlandırılmış tünel veya sabit deploy kullanın.

> ⚠️ **Araç adı çakışması:** aynı projede iki connector aynı araç adını
> taşımamalı — istemci şemaları karıştırıp `_2` sonekli araçlar üretir ve
> çağrılar 400 ile düşer.

> ⚠️ **Av. K. m. 36:** üçü de **public** arama aracıdır. Müvekkil adı, dosya
> numarası, dosya özeti veya gizli taslak **gönderilmez**; sorgu soyut hukuki
> kavram olur. Bkz. `mesleki-sir-rehberi.md`.

**Test:**
```
"Azerbaycan Əmək Məcəlləsi yürürlükte mi?"     → get_act, statusName dönmeli
"mücbir sebep uyarlama Türk doktrini"           → DergiPark kayıtları dönmeli
"Azerbaycan PSA'larında stabilizasyon klozu"    → search_contracts dönmeli
```

> **Kurulmazsa ne olur?** Paket çalışmaya devam eder: AZ mevzuatı
> `azerbaycan-hukuk-rehberi.md` WebFetch yoluna düşer (**statü doğrulanmaz**),
> doktrin ve sözleşme emsali kapsam dışı kalır — asistan bunu çıktısında belirtir.

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

This is version **1.2.0**. See `CHANGELOG.md` for what changed.

Feedback and support: Open an issue on the project's GitHub page.
