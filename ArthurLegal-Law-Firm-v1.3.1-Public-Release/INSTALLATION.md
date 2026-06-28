# ArthurLegal Law Firm Assistant — Installation Guide

**Version:** 1.2.0 | **Updated:** 2026-06-04

---

## Requirements

| Requirement | Details |
|---|---|
| Claude.ai account | Pro or Team plan (required for Projects feature) |
| TR Legal MCP | yargi-mcp-pro connector (optional but recommended) |
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
```

### New practice areas (v1.2.0)
```
knowledge/profiles/privacy-legal.md       ← GDPR / KVKK / data protection
knowledge/profiles/regulatory-legal.md    ← Regulatory / agency law
```

### Skill files (all plugins)
```
knowledge/skills/administrative-legal__skills.md
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
knowledge/references/cek-hukuku-rehberi.md
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
