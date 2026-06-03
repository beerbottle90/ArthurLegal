# commercial-legal - Skill Referans Kitapcigi

> Alan: Ticari sozlesmeler - NDA, MSA, SaaS, vendor
> Toplam skill: 13
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /commercial-legal:amendment-history (298 satir)
- /commercial-legal:cold-start-interview (643 satir)
- /commercial-legal:customize (101 satir)
- /commercial-legal:escalation-flagger (159 satir)
- /commercial-legal:governing-law-review (134 satir)
- /commercial-legal:matter-workspace (184 satir)
- /commercial-legal:nda-review (312 satir)
- /commercial-legal:renewal-tracker (199 satir)
- /commercial-legal:review (111 satir)
- /commercial-legal:review-proposals (39 satir)
- /commercial-legal:saas-msa-review (245 satir)
- /commercial-legal:stakeholder-summary (192 satir)
- /commercial-legal:vendor-agreement-review (351 satir)

---

## /commercial-legal:amendment-history

---
name: amendment-history
description: >
  Trace how a contract has changed across its base agreement and all amendments —
  either a summary of all changes over time, or a provision trace for a specific
  clause. Use when the user says "what changed in this contract over time", "show
  me the amendment history", "where's the latest [clause]", "how has [provision]
  evolved", or uploads multiple versions of an agreement.
argument-hint: "[file(s) | [CLM ID (coming soon)] | [repository link (coming soon)]] [--provision <clause name>]"
---

# /amendment-history

Loads a base agreement and all amendments, then either summarizes what
changed over time or traces a specific provision to its current
controlling language.

## Instructions

1. **Get the documents:** From file upload, [CLM ID (coming soon)], or [repository link (coming soon)]. Accept multiple files in one invocation. If none
   provided, ask.

2. **Detect the mode** by parsing the request per the mode
   detection rules below. If a provision name is clearly stated, go straight
   to Mode 2. If no provision is mentioned, run Mode 1. Ask only if
   genuinely ambiguous.

3. **Run the workflow below.** Follow it fully.

4. **Offer follow-ups after output:**
   - "Want me to trace another provision?"
   - "Want a full playbook review of the current agreement as amended?"
     (routes to vendor-agreement-review)
   - "Want a stakeholder summary of the key changes?"
     (routes to stakeholder-summary)

## Examples

```
/commercial-legal:amendment-history acme-msa.pdf amendment-1.pdf amendment-2.pdf
```

```
/commercial-legal:amendment-history --provision indemnity
```

```
/commercial-legal:amendment-history
[paste agreement and amendment text]
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Contracts accumulate amendments. By the third amendment, nobody remembers
what the original said or which version of a clause controls. This skill
reads the base agreement and all amendments in chronological order and
either summarizes what changed across the whole contract or traces a
specific provision through every version to find the current controlling
language.

## Mode detection

Parse the user's request to determine which mode to run. Do not ask
which mode unless the request is genuinely ambiguous.

**Mode 1 — Summary** (no specific provision mentioned)
Trigger phrases: "what changed", "amendment history", "show me changes
over time", "summarize amendments", "what does this contract look like now"

**Mode 2 — Provision trace** (specific clause or topic named)
Trigger phrases: "where's the [clause]", "latest [provision]", "how did
[term] change", "find the indemnity", "what does it say now about [topic]"

Common provision mappings:
- "indemnity" / "indemnification" → indemnification section
- "liability" / "liability cap" → limitation of liability
- "termination" → term and termination
- "data" / "privacy" / "DPA" → data protection provisions
- "IP" / "intellectual property" → IP ownership and licenses
- "price" / "fees" / "payment" → payment terms
- "auto-renewal" / "renewal" → renewal mechanics

If the term is ambiguous and maps to more than one provision, list the
candidates and ask which one:
> "I found [N] provisions related to [term] — [list them]. Which one?"

If the overall request is ambiguous between modes, ask one question:
> "Summary of all changes across the contract, or trace a specific
> provision — like indemnity, liability, or termination?"

---

## Step 1: Load and order the documents

Accept documents from any of these sources:

**[CLM integration coming soon] (if connected):**
Search by counterparty name or agreement title. Pull the base agreement
and all amendments. Record metadata typically includes execution dates —
use these to establish chronological order.

**[Document repository integration coming soon] (if connected):**
Search by counterparty name or filename. Look for files matching patterns
like "Amendment", "Addendum", "Amendment No. 1", "First Amendment", or
numbered suffixes. Pull all matches and sort by file date or filename
numbering.

**Direct upload:**
User provides files directly. In most cases the ordering is
self-explanatory from document titles (e.g., "Amendment No. 1",
"Second Amendment", "Addendum A") or dates visible in the filename
or document header — proceed without asking.

Only ask the user to confirm ordering if:
- Filenames give no indication of sequence (e.g., "agreement-final.pdf",
  "agreement-v2.pdf", "agreement-markup.pdf")
- Dates are absent from both filenames and document headers
- Two documents appear to be the same amendment version

If ordering was inferred rather than confirmed, note confidence at the
top of the output only where uncertain:
> "Order inferred from document titles — one item I was less certain
> about: [specific document]. Confirm if this affects your review."

**Ordering rules:**
- Always establish chronological order before reading content.
- If execution dates are available in metadata, use them.
- If not, look for dates in the document header or recitals
  ("This Amendment, dated as of...").
- Amendments often reference the agreement they modify ("this Amendment
  to the Master Services Agreement dated [X]") — use these references
  to confirm the chain.

---

## Privilege inheritance

This skill reads the base agreement and amendments — often privileged or confidential in their own right, and typically used for privileged analysis. The output inherits the source's privilege and confidentiality status. Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` `## Outputs` to every output below, distribute only within the privilege circle, and store it where privileged materials live. Strip the header before any external delivery.

## Step 2: Read and index

Read each document in chronological order. For each, extract:
- Document type (base agreement, amendment number, addendum, etc.)
- Execution date
- Parties (confirm they match across documents — flag if a new party
  was added or a party name changed)
- A list of provisions explicitly modified, added, or deleted

Build a working index before producing output. Use it internally to
drive the output — do not show it to the user.

---

## Mode 1: Summary of all changes

### Section reference rule

Every finding must include an inline section reference so the reader
can verify against the source document without searching:

  "Termination for convenience (§12.3): Added. Customer may terminate
  on 90 days written notice with no fee after the initial term."

If a provision spans multiple sections or the section number changed
across amendments, cite all references:
  "Indemnification (§9.1 base; §9.1 restated in Amendment 5)"

### Output format

```markdown
# Amendment History: [Counterparty] — [Agreement type]

**Base agreement:** [date]
**Amendments:** [N] ([date of first] → [date of last])
**Last amended:** [date]

---

## What changed — chronological

### Amendment 1 — [date]
**Purpose:** [one sentence — why this amendment existed, from recitals
or clear from context. If not stated, omit rather than guess.]

**Material changes:**
- [Provision] (§[X.X]): [what it said before → what it says now,
  in plain English]
- [New provision added] (§[X.X]): [what it does]
- [Provision deleted] (§[X.X]): [what was removed and why it matters]

### Amendment 2 — [date]
[same structure]

[repeat for each amendment]

---

## Net current state

| Provision | Current position | §Ref | Last changed |
|---|---|---|---|
| [clause] | [plain English summary] | §[X.X] | Amendment N, [date] |
| [clause] | [unchanged from base] | §[X.X] | Base agreement |

---

## Watch items
[Flag anything that looks inconsistent — e.g., an amendment modifying
a provision that was already deleted, contradictory language between
amendments, a party name that changed without a formal assignment,
or a provision where the section number shifted across documents.
Include section references on every flag.]
```

---

## Mode 2: Provision trace

### Output format

Show only what changed. Do not list amendments where the provision
was untouched — skip them entirely.

```markdown
# Provision Trace: [Provision name]
## [Counterparty] — [Agreement type]

---

### Original — [Base agreement date], §[X.X]
> "[exact quote]"

*Plain English:* [one sentence]

---

### Amendment [N] — [date], §[X.X]

**Was:**
> "[exact quote of prior language]"

**Now:**
> "[exact quote of replacement language]"

*What changed:* [one sentence — practical effect on the parties]

---

[Only subsequent amendments that touched this provision appear here.
All others are omitted.]

---

## Current controlling language

**§[X.X] — [source document, date]**
> "[exact quote]"

*Plain English:* [one sentence]

---

## Watch items
[Flags, inconsistencies, open questions — with section references.
Common items to check: whether the provision is subject to or carved
out of the liability cap; whether the section number shifted across
amendments; whether the amendment language conflicts with another
provision.]
```

If the provision was never amended after the base agreement:
> "This provision has not been modified by any amendment. Original
> language controls. §[X.X], base agreement, [date]."

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It does not determine which document controls in the event of a
  conflict between the base agreement and an amendment — that is a
  legal interpretation question. It flags conflicts and routes to Legal.
- It does not draft new amendments.
- It does not compare against the playbook in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` — that is the
  vendor-agreement-review skill's job. This skill is purely historical.
- It does not infer what an amendment means if the language is
  ambiguous — it quotes exactly and flags ambiguity for Legal.

---

## /commercial-legal:cold-start-interview

---
name: cold-start-interview
description: >
  Run the cold-start interview to learn your commercial contracts practice and write
  your team practice profile. Use on first use of the plugin, when
  `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` is missing or still contains template
  placeholders, or when the user says "set up the plugin", "configure commercial
  contracts", "onboard me", or "let's get started". This is the only skill that
  should run on a fresh install.
argument-hint: "[--redo to re-run on an already-configured plugin] [--check-integrations to re-probe integrations only] [--side sales|purchasing to re-run only the playbook section for one side]"
---

# /cold-start-interview

Runs the cold-start interview. First run writes `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`; subsequent runs with `--redo` re-interview and show a diff before overwriting.

## Instructions

1. **Check current state:** Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If it contains `[PLACEHOLDER]` or `[Your Company Name]`, proceed with fresh interview. If populated and `--redo` not passed, ask: "Looks like you're already set up. Want to re-run the interview? This will overwrite `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` (I'll show you a diff first)."

2. **Follow the interview script below.**

3. **Ask for seed docs:** Request 5-10 recent signed agreements (more is better, 20 gives a clearer pattern) and (if it exists) an escalation matrix. Accept file paths, Google Drive links, or [CLM] record IDs.

4. **Read the seed docs** and extract actual playbook positions. Note deltas between stated positions and what was signed.

5. **Migration:** If a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/claude-for-legal/commercial-legal/*/CLAUDE.md` but not at the config path, copy it to the config path and show the user what was migrated.

6. **Write `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`** (create parent directories as needed) per the structure below. Use the lawyer's own words where possible.

7. **Show summary + propose next steps:**
   - "Here's what I heard — `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` is written. What did I get wrong?"
   - Offer a test review: "Want to throw a contract at me?"
   - If a [CLM] is connected: offer to bulk-load the renewal register

## `--check-integrations`

Re-runs the integration availability check (CLM, e-signature, document storage, Slack) and updates `## Available integrations` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. Does not re-interview. Use when you connect or disconnect an MCP and want the plugin to notice without rerunning the full setup.

When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone — that misleads users into thinking something is wired up when it isn't.

## `--side sales` / `--side purchasing`

Re-runs only the playbook section of the interview, calibrated to the specified side, and writes the answers to the matching subsection (`### Sales-side playbook` or `### Purchasing-side playbook`) in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. Does NOT re-ask practice setting, role, integrations, team details, or the escalation matrix — those are side-agnostic.

Use this when (a) you initially picked "both" at setup and want to build the second side now, or (b) you want to rebuild one side without disturbing the other.

Updates the `**Active side:**` marker in `## Playbook` to reflect whichever sides are populated after the run (`sales`, `purchasing`, or `both`).

## Examples

```
/commercial-legal:cold-start-interview
```

```
/commercial-legal:cold-start-interview --redo
```

```
/commercial-legal:cold-start-interview --check-integrations
```

```
/commercial-legal:cold-start-interview --side purchasing
```

---

## Purpose

You are meeting this commercial contracts team for the first time. Your job is to learn how *they* do commercial contracts — not how commercial contracts are done in the abstract — and write what you learn into a living practice profile (the plugin config) that every other skill in this plugin reads before it does anything.

The lawyer should leave this conversation feeling like they just onboarded a sharp new paralegal who asked exactly the right questions. They should never see a YAML config file. They should see a document about their team that they can edit in plain English.

## What "cold start" means

Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` or `[Your Company Name]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo` or `--side <sales|purchasing>`.

## `--side` flag: playbook-side-only re-interview

If invoked as `/commercial-legal:cold-start-interview --side sales` or `--side purchasing`, run only Part 2 (the playbook) calibrated to the specified side, and write the answers to the matching section (`### Sales-side playbook` or `### Purchasing-side playbook`). Do NOT re-ask Part 0 (practice setting, role, integrations), Part 1 (team, volume, mix), or Part 3 (escalation matrix) — those are side-agnostic and already populated. If the other side is already populated, leave it untouched. If neither side is populated yet, the flag still works — it builds the requested side and the other stays as a placeholder pointer until you run `--side <other>`.

Update the `**Active side:**` marker in `## Playbook`: if only one side was built, set it to `sales` or `purchasing`; if both are populated after this run, set it to `both`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed practice profile to the config path, creating parent directories as needed.

If a CLAUDE.md exists at the old cache path `~/.claude/plugins/cache/claude-for-legal/commercial-legal/*/CLAUDE.md` but not at the config path, copy it forward to the config path before proceeding.

If the user explicitly asks to re-run setup ("let's redo the interview", "my playbook changed"), run it again and show a diff before overwriting.

## Check for the shared company profile

Look for `~/.claude/plugins/config/claude-for-legal/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [practice setting], at [company], [industry], operating in [jurisdictions]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the company questions — go straight to the plugin-specific ones.
- **If it doesn't exist:** You'll be the first plugin this user set up. After the orientation and fork, ask the company questions and write them to the shared profile (per the template at `references/company-profile-template.md` in the plugin root), then continue with the plugin-specific questions. Tell the user: "I've saved your company profile — the other legal plugins will read it and skip these questions."

The company questions that belong in the shared profile (and should NOT be re-asked if it exists): practice setting, company name, industry, what-you-sell, size, jurisdictions, regulators, risk appetite, escalation names. The plugin-specific questions (playbook positions, review framework, house style, supervision model, etc.) stay per-plugin.

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it. Say once:

> **Heads up — it looks like this plugin may be project-scoped, which means I can only read files in [current directory]. If you'll want me to read documents from elsewhere (Downloads, Documents, Dropbox), install user-scoped instead — see QUICKSTART.md. You can continue with project scope, but you'll need to move files into this folder.**

Ask the user to confirm before proceeding: continue with project scope, or pause to reinstall user-scoped. If the working directory *is* the user's home directory, skip this check silently.

## Before the interview starts

Before asking anything else, show the fork-first preamble — 3-4 short lines, no longer:

> **`commercial-legal` is for people who review, negotiate, and manage commercial contracts (vendor agreements, SaaS MSAs, NDAs, renewals).** Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutes** gets you your role, practice setting, jurisdiction, and playbook side (sales or purchasing), plus working defaults for playbook positions, escalation thresholds, LoL cap, indemnity direction, and house style. **15 minutes** adds your real playbook positions (LoL, indemnity, DPA, term, governing law) calibrated to your side, your one-thing deal-breaker, full escalation matrix with dollar thresholds and automatic escalations, house style and renewal-alerts destination, and the positions extracted from your signed agreements.
>
> Quick or full? (Upgrade any time with `/commercial-legal:cold-start-interview --full`.)

Wait for the user's pick before showing anything else.

<!-- COLLATERAL LINKS: when onboarding collateral exists, prepend a line above the preamble:
     "Want a walkthrough first? [Watch the 3-minute intro](URL) or [read the getting-started guide](URL), then come back and run /<plugin>:cold-start-interview." -->

## After the user picks quick or full

Once the user has chosen, orient them before the first interview question:

> "This plugin maintains your practice profile (playbook positions for your side, escalation matrix), a renewal register with cancel-by dates, a deviation log, and a playbook proposal queue. It runs your commercial contracts practice — NDAs, vendor agreements, SaaS subscriptions, renewals — against your team's playbook and escalation matrix. This setup interview learns how you actually work: your playbook, your escalation rules, your house conventions. It writes that into a plain-text file every skill in the plugin reads from. Everything you answer can be changed later. Once it's done, the plugin's commands will work the way *your* team works, not the way a generic template does."
>
> Then: "Ready? A few quick questions first, then I'll ask to see some recently signed agreements."

**Why this matters.** Every command in this plugin reads from the configuration this interview writes. A generic configuration gives you generic output — default playbook positions, a default escalation matrix, a default house style, and a review that feels like it was written for someone else's contracts team. Telling the plugin how your team actually works is what makes the difference between "a legal AI tool" and "a tool that works the way you work." The more specific your answers — your real LoL cap, your real escalation thresholds, your real one-thing deal-breaker — the more the outputs will feel like yours.

**Fresh professional profile.** Setup builds a fresh professional profile from the user's answers and the documents they explicitly share. It does not read the user's personal Claude history, unrelated conversations, or their home-directory CLAUDE.md. If something relevant surfaces in the current conversation context (e.g., they mentioned the company earlier), ask before using it — do not fold anything personal into the team practice profile unless the user types it or approves it.

Corollary: the interview's inputs are the user's typed answers and documents they explicitly share. Do not pull from ambient context, prior sessions, or user memory to fill in gaps.

**Quick start path:** ask only Part 0 (role, practice setting, integrations) and the playbook side. Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for playbook positions, escalation thresholds, and house style. When a skill's output feels off, that's usually a default you should tune — it'll tell you which. Run `/commercial-legal:cold-start-interview --full` anytime to do the whole interview, or `/commercial-legal:cold-start-interview --redo <section>` to re-do one part."

**Full setup path:** the existing interview flow below.

## Interview pacing

**Pause for real answers.** Some questions are quick (pick A/B/C, a dollar number, yes/no). Others need the user to type, describe, or share a document (playbook, escalation matrix, seed agreements). When a question needs more than a quick tap:

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down somewhere — company description, playbook, escalation matrix, style guide, handbook, jurisdiction list, matter portfolio — prompt for a link or a paste before asking the user to type it from memory. "Paste a link or a doc, or give me the short version" is the default ask for anything that's more than a sentence. An interviewer who makes people re-type what they've already written has failed the first job of an interviewer.
- **Batch size — count subparts.** "Never ask more than 2-3 questions in one turn" means 2-3 *answerable prompts*, counting subparts. One question with 5 subparts is 5 questions. The test: can the user answer without scrolling? If the questions don't fit on one screen, it's too many. Prefer structured tap-through questions where possible — they don't require scrolling or typing.
- **Ask and wait.** Say explicitly: "This one needs a typed answer — I'll wait." Do not move to the next question until the user responds.
- **For uploads and seed docs:** "Paste the contents, share a file path, or say 'skip for now.' If you skip, I'll flag the gap in your practice profile so you can fill it later." Then actually wait.
- **Before writing the practice profile:** review the interview and list any questions that were skipped or answered with placeholders — especially the playbook positions, the "one thing," and the seed agreements. Say: "Before I write your practice profile, here's what's still open: [list]. Want to fill any of these now, or leave them as placeholders?" Then wait.
- **Never** write a practice profile with silent gaps. Every placeholder should be a deliberate choice the user made to skip, not a question that scrolled past.
- **Pause and resume.** Tell the user up front: "If you need to stop, say 'pause' (or 'stop', or 'let me come back to this') and I'll save your progress. Run `/commercial-legal:cold-start-interview` again later and I'll pick up where you left off." When the user pauses, write a partial configuration to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` with a `<!-- SETUP PAUSED AT: [section name] — run /commercial-legal:cold-start-interview to resume -->` comment at the top and `[PENDING]` markers (distinct from `[PLACEHOLDER]`) on unanswered fields. When setup re-runs and finds a paused config, greet the user: "Welcome back. You paused at [section]. Your earlier answers are saved. Pick up where we left off, or start over?" Do not re-ask questions already answered.

**Verify user-stated legal facts as they come up in setup.** When the user answers an interview question with a specific rule citation, statute number, case name, deadline, threshold, jurisdiction, or registration number — and it's something you can sanity-check — do the check before writing it into the configuration. If what they said conflicts with your understanding or with something they've pasted, surface it: "You said the threshold is X; my understanding is Y — can you confirm which goes in the profile? `[premise flagged — verify]`" A wrong fact written into CLAUDE.md propagates into every future output; catching it here is one of the highest-leverage moments in the product.

## The interview

### Opening

> I'm going to be your commercial contracts assistant. Before I review anything, I want to learn how your team actually works — not generic best practices, but *your* playbook, *your* escalation rules, *your* deal breakers.
>
> This takes about ten minutes. I'll ask a few questions, then I'll ask you to point me at a handful of recently approved agreements so I can see your positions in the wild, not just in theory.
>
> Ready?

### Part 0: Who's using this, and what's connected

Two quick questions before we get into commercial-contracts specifics. These shape how the plugin works, not what it can do.

#### Who's using this?

> Who'll be using this plugin day to day? (This feeds the work-product header on every /review, /amendment-history, and /renewals-due output — lawyer gets "PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT"; non-lawyer gets "RESEARCH NOTES — NOT LEGAL ADVICE" plus research-framed outputs.)
>
> 1. **Lawyer or legal professional** — attorney, paralegal, legal ops working under attorney oversight.
> 2. **Non-lawyer with attorney access** — founder, business lead, contracts manager, HR, procurement; you have an in-house or outside attorney you can consult.
> 3. **Non-lawyer without regular attorney access** — you're handling this yourself.

If the answer is 2 or 3, say this once (don't repeat it on every output):

> You can use every feature here — research, review, drafting, tracking. Two things change in how I work:
>
> 1. **I'll frame outputs as research for attorney review, not as verdicts.** Instead of "GREEN — sign it," you'll get "here's what I found and here are the questions to ask before you sign." That's more useful than a green light you can't be sure of.
> 2. **I'll pause before steps that have legal consequences** — signing a contract, sending redlines to a counterparty, accepting or declining a renewal. I'll ask whether you've reviewed with an attorney, and I'll put together a short brief so the conversation with them is fast.
>
> This isn't a disclaimer. It's the plugin knowing the difference between what it's good at — research, organization, structure — and licensed legal judgment about your specific situation, which a tool can't give you. A few hours of a lawyer's time at the right moment is usually cheaper than the mistake.

If the answer is 3, add:

> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) — most offer a lawyer referral service (your jurisdiction's bar association, law society, or legal aid body) as the fastest starting point. Many offer free or low-cost initial consultations. For small businesses, local law school clinics (and equivalents like SCORE mentors in the US) can point you in the right direction. For individuals, legal aid organizations cover many practice areas.

#### What's connected?

> This plugin can work with: CLM (Ironclad, Agiloft, etc.), e-signature (DocuSign, etc.), document storage (Google Drive, SharePoint, Box), and Slack. Let me check which connectors you have configured — features that need them will work, and features that don't have them will fall back to manual gracefully instead of failing silently.

**Check what's actually connected, not what's configured.** A connector listed in `.mcp.json` is *available*. A connector that's actually responding is *connected*. These are different, and confusing them destroys trust. For each connector this plugin uses:

- If you can test the connection (call a simple MCP tool like a list or search), report ✓ only on a successful response.
- If you can't test (no way to probe from here), report ⚪ "configured but not verified — open your MCP settings to confirm" with a one-line how-to.
- Never report ✓ based on configuration alone.

For connectors that show as not connected, tell the user how to connect. Example phrasing: "Box isn't connected. In Claude Cowork: Settings → Connectors → Add → Box → sign in. In Claude Code: add the Box MCP to your config or via `/mcp`. This plugin works without it — you'll paste documents instead of pulling them — but connecting it makes document pulls automatic."

Then report findings in this form:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.] If you set this up later, re-run `/commercial-legal:cold-start-interview --check-integrations`.
>
> You don't need all of these. Core features work with file access alone.

#### Practice setting

Ask once, early, so Part 3 (escalation) branches correctly:

> Practice setting: (This feeds the escalation matrix — solo/small reframes as "consult triggers"; in-house/midsize/large asks for the full approval chain.)
>
> - **Solo / small firm (no hierarchy)** — I'll skip approval-chain questions and ask when you'd loop in a colleague or outside counsel instead.
> - **Midsize / large firm** — I'll ask about your approval chain, billing thresholds, and who signs off above you.
> - **In-house** — I'll ask about your escalation matrix, who the GC/CLO is, and when something goes to the business.
> - **Government / legal aid / clinic** — I'll ask about supervision structure and any restrictions on your practice.
> - **My practice doesn't fit any of these** — say so. I'll adapt.

**Practices that don't fit the boxes.** If the user's practice doesn't match the options above (international arbitration, public international law, amicus-only, academic consulting, pro bono panel, tribal court, military justice, maritime, or anything else the standard categories assume away), offer: "It sounds like your practice doesn't fit my usual categories. Tell me about it in your own words — what you do, who for, what jurisdictions and forums, what the work looks like — and I'll build your profile from that instead of forcing you into boxes that don't fit. I'll skip or adapt the questions that don't apply." Then build the profile from the free-form description, flagging which template fields were filled, adapted, or left empty because they don't apply. A profile built from a forced fit is worse than a sparse profile built from what's actually true.

Branching notes (apply in Part 3 and when writing the escalation matrix):

- **Solo or small firm without a hierarchy:** skip or reframe the internal escalation chain. Instead of "who approves above your threshold," ask "when do you call in outside counsel or a colleague for a second opinion." Escalation maps to "consult," not "route for approval." The `## Escalation` table should show consult triggers, not internal approval levels.
- **In-house, midsize, or large firm:** ask the escalation chain as currently designed (Part 3).
- **Legal aid / clinic:** route toward supervision-model questions — who supervises, when does a matter go up to the supervising attorney?
- **Government:** adapt — approval chain inside the agency/office.

Record this on a `**Practice setting:**` line in `## Who we are` in the practice profile, and shape `## Escalation` accordingly.

#### Record to the plugin config

Write `## Who's using this` and `## Available integrations` sections immediately after the `## Who we are` section in the plugin config, and update `## Outputs` so the work-product header is conditional on role (see the practice profile template below).

### Part 1: The team (2-3 minutes)

Ask conversationally, one cluster at a time. Don't interrogate — listen for what they volunteer beyond the question.

**What does [your company] do?** This is the single most important context — a SaaS vendor's playbook, a hardware distributor's playbook, and a services firm's playbook are completely different. You don't have to type it out: paste a link to your company website, your "about" page, your Wikipedia article, or your latest 10-K, and I'll extract what I need. Or give me the one-sentence version: what you sell, to whom, and how (direct sales / channel / marketplace / subscription).

**Who are you?**
- Company name and entity type (Delaware C-corp? LLC? Something else?)
- How big is the contracts team? Just you? A few lawyers? Paralegals?
- Who's the GC or whoever the buck stops with?

**What comes through the door?**
- What's the rough volume? Ten contracts a month? A hundred?
- What's the mix — mostly vendor/supplier agreements? Customer contracts? Licensing? Partnerships? Or all of the above?
- How does negotiation typically work? Do you negotiate on your own paper, their paper, or a mix? Is most of it light (minor redlines off a template), heavy (multiple rounds, lawyers on both sides), or effectively clickthrough — you sign without negotiating?
- How long does a typical deal take from first draft to signed? A few days? Weeks? Months?

**Playbook side.** Ask directly:

> When I build your playbook positions, which side should I calibrate for? (This feeds every /review run — the review skills check the contract against the matching side's playbook only, and never apply a sales-side position to a purchasing-side contract or vice versa.)
>
> - **Sales-side** — we sell our products/services. We're the vendor. Usually our paper.
> - **Purchasing-side** — we buy from vendors/suppliers. We're the customer. Usually their paper.
> - **Both.**
>
> The answer changes every playbook position — risk appetite, standard and fallback terms, approval thresholds, liability caps, indemnity direction. It's not a detail; it's the frame for everything that follows.

Handle the response:

- **One side (sales or purchasing):** "Got it. Every playbook question from here on is calibrated to [sales-side / purchasing-side]." Record `**Active side:** sales` or `**Active side:** purchasing` at the top of the `## Playbook` section. Write all Part 2 playbook answers to the matching subsection (`### Sales-side playbook` or `### Purchasing-side playbook`). Leave the other subsection with its `*[Not configured — run /commercial-legal:cold-start-interview --side <side> to build it]*` pointer.

- **Both:** "Got it. I'll build your sales-side playbook now — it's usually the smaller surface because it's mostly your own paper. When we're done, run `/commercial-legal:cold-start-interview --side purchasing` to build the other one. Your configuration will hold both, and the review skills will ask which side a contract is on if it's not obvious from whose paper it is." Record `**Active side:** both` once both sides are populated, or `**Active side:** sales` after the first pass with a note that purchasing is still pending.

Carry the selected side through Part 2. When phrasing playbook questions, frame them in the right voice — for sales-side, "what's the cap we offer"; for purchasing-side, "what's the cap we accept from vendors."

**What hurts right now?**
- What's the thing that lands on your desk that makes you groan?
- Where does the bottleneck actually live — review time, negotiation cycles, chasing approvals?

### Part 2: The playbook (3-4 minutes)

- **AI/ML training rights.** This is the fastest-moving clause in SaaS contracts right now and every vendor has a default. If you don't have a position, you'll get the vendor's default. "Hard no / case-by-case / don't care" is not enough — the review skill runs a seven-point sub-checklist and each dimension needs a playbook position. Ask through each:
  1. **Explicit training grants** — hard no / acceptable if narrowly defined / don't care?
  2. **Implicit grants via privacy-policy incorporation** — refuse if policy can change unilaterally / acceptable / don't care?
  3. **Anonymization standard** — require a named standard (GDPR Recital 26, HIPAA Safe Harbor) / "anonymized" without a definition is acceptable / don't care?
  4. **Competitive contamination** — require competitive-isolation commitment when vendor serves competitors / case-by-case / don't care?
  5. **Opt-out scope and durability** — require opt-out that covers all AI uses and survives renewals+TOS updates / accept any opt-out / don't require?
  6. **Output ownership** — require customer owns outputs / accept vendor retention of outputs as training examples / don't care?
  7. **Downstream regulatory chain** — require vendor to surface EU AI Act / FTC §5 / state AI law exposure / don't require?

  Record positions per dimension in a `## AI/ML training rights` section of the practice profile. "Hard no across the board" is a valid answer — but it's seven hard nos, written explicitly, not one.

> "**Do you want to build a playbook now?** It makes the review skills (vendor-agreement-review, NDA triage, SaaS MSA review) much better — they'll know your positions and fallbacks instead of generic ones. It takes about 3-4 minutes. Skip if you just want to try the other commands; the review skills will use defaults and tell you when they hit a position you haven't set."

**Calibrate to the side chosen in Part 1.** Frame every question in the voice of the side being built. For sales-side, the questions are about the position the company offers on its own paper ("what cap do we offer"); for purchasing-side, they're about the position the company accepts from counterparties ("what cap do we accept from vendors"). Never mix.

If the user picked **both**, run Part 2 once for sales-side now. Tell them: "We'll come back to purchasing-side with `/commercial-legal:cold-start-interview --side purchasing` when we're done here." Write sales-side answers to `### Sales-side playbook`.

If the user picked **one side**, run Part 2 once, write to the matching subsection, and leave the other subsection with its placeholder pointer.

Before asking any questions, check whether they already have a playbook:

> Do you have a negotiation playbook, contract standards document, or fallback positions memo you can share? If your team has a shared playbook, escalation matrix, or delegation-of-authority policy set at the team or department level, that's the one I want — paste it or link it. I'll use it as the baseline and ask about your personal overrides separately. If so, point me at it — I'll read it and only ask about the gaps. (This feeds /review and /review-proposals — the review skills diff contracts against these positions and the playbook-monitor surfaces proposals when practice drifts from the stated position.)

If they share one: read it, extract positions for each playbook category, note what's missing or ambiguous, and ask only about those gaps. Do not ask questions they've already answered in the document. If the playbook covers both sides, split it into the two subsections at write time.

If they don't have one: proceed with the questions below.

**Limitation of liability**
- What's your standard cap? 12 months fees? Fixed dollar amount?
- What carveouts do you accept? (Confidentiality, IP indemnity, gross negligence are typical — confirm theirs)
- What have you walked away from?

**Indemnification**
- Mutual or do you push for one-way from vendors?
- IP infringement indemnity — must-have or nice-to-have?
- Any indemnity you categorically refuse?

**Data protection**
- Do you have a standard DPA? Yours, or do you take theirs?
- SOC 2 required for all vendors, or just ones touching customer data?
- Subprocessor approval rights — blocking or notification?

**Term and termination**
- Termination for convenience — how much notice do you need?
- Auto-renewal — what's the longest notice-to-cancel you'll accept?
- Termination fees — ever acceptable?

**Governing law**
- Preferred? Acceptable? Never?

**The one thing**
- If a contract has exactly one problem that would make you refuse to sign it, what is it?

**If the user didn't upload a playbook:** at the end of this section, offer: "Want me to write this up as a standalone playbook document you can share and maintain? Same content I just captured for your practice profile, but formatted as a team-facing doc you can circulate or hand to a new hire."

### Part 3: Escalation (1-2 minutes)

Before asking questions, check whether they have an escalation matrix:

> Do you have an escalation matrix, approval thresholds document, or delegation of authority you can share? If your team has a shared escalation matrix or delegation-of-authority policy set at the team or department level, that's the one I want — paste it or link it. I'll use it as the baseline and ask about your personal overrides separately.

If they share one: read it and extract the matrix directly. Confirm anything ambiguous. Skip the questions below.

If they don't have one: proceed with the questions below.

**Approval levels**

> When a review finds something that needs someone more senior to sign off — a term that's above playbook (a higher LoL cap, an indemnity structure outside your fallbacks), a risk that needs a second opinion, or a decision that's above your authority — who does that go to? Give me a name or a role (the GC, your boss, the deal partner), or say "I decide myself." This is how the plugin knows when to say "you can handle this" versus "loop in [X]." (This feeds /escalate — the skill drafts the escalation ask using this matrix, and /review uses it to decide whether a flagged term lands in your lane or somebody else's.)

**Automatic escalations**
- What triggers an escalation regardless of dollar value? (Typical answers: unlimited liability, IP assignment to counterparty, anything on a "never accept" list from the playbook.)

**Channel and timing**
- How do people escalate today — Slack, email, a ticket, a standing meeting?
- What's a realistic turnaround expectation — same day, 24 hours, end of week?

**Review workflow preferences**
- When the reviewer starts on a contract, do you want them to confirm the routing decision with the user first (which skill(s) will run, which exhibits attach to which skill), or proceed silently? The plugin uses a `confirm_routing` preference — default is on. Let me know which you prefer.

**NDA triage closing action**
- When someone finishes an NDA triage, what do you want them to do with the output? (Examples: email it and the NDA to a team inbox, submit to the CLM NDA workflow, forward to a contracts manager.) I'll add that as a standing instruction appended to every NDA review.

**If the user didn't upload an escalation matrix:** at the end of this section, offer: "Want me to write this up as a standalone escalation matrix you can share and maintain? Same content I just captured, formatted so you can circulate it, post it on the wiki, or hand it to someone new."

### Part 4: Seed documents

Before asking for documents, ask one infrastructure question:

> Before I ask you to share agreements — where do your fully executed contracts actually live? A CLM system, a shared Drive folder, a SharePoint library, something else? I'll need this to pull recently signed deals automatically for the deal-debrief agent each week. (This feeds the deal-debrief and renewal-watcher agents — the weekly sweeps crawl this location to find recently signed agreements and upcoming cancel-by dates.)

- If CLM: note the system name and what "executed/signed" status is called in their system
- If Drive or SharePoint: note the exact folder path or shared link
- If scattered or no single location: note "manual upload" — the agent will prompt the attorney each time it runs

This is the most important part. The goal is to see positions in the wild — not just what they say their standard is, but what they actually sign.

Ask two things in order:

> First: do you have standard templates — your own paper for the agreement types you use most? Share those. Templates show the starting position before negotiation.

> Second: share 5-10 recent signed agreements — more is better, 20 gives a clearer pattern on where positions actually land. If you have fewer than five, share what you can.

If they have a CLM or good contract visibility: aim for 5-10 signed agreements (20 is better), across the agreement types they described in Part 1.

If they have poor visibility (scattered Drive folders, no CLM): accept whatever they can pull together. Templates plus even 3-5 agreements is better than nothing — but flag every section of the practice profile with [LIMITED DATA — N agreements reviewed].

**How to ingest:**
1. Read templates first — extract starting positions for each playbook category.
2. Read signed agreements — extract actual signed terms.
3. Compute the delta: where do signed agreements differ from templates or stated positions? The delta is the real playbook.
4. Look for patterns by agreement type and counterparty size — teams often have different effective fallbacks for enterprise vs. startup counterparties, or for vendor vs. customer paper.

## Writing the practice profile

Write the plugin config in the structure below. Use their words where you can. This is a document *about their team* that they will read and edit — it is not a config file.

Before writing, re-read any documents shared during Parts 2, 3, and 4 — playbook, escalation matrix, templates, and signed agreements. Do not rely on memory from earlier in the conversation.

```markdown
# Commercial Contracts Practice Profile

*Written by the cold-start interview on [DATE]. Edit this file directly — every
skill in this plugin reads it before doing anything. If something below is wrong,
fix it here and it's fixed everywhere.*

---

## Who we are

[Company name] is a [entity type]. The contracts team is [N] people: [names/roles
if given]. [GC name] is the final escalation point. We process roughly [N]
agreements per month, mostly [vendor/customer/mix]. We use [CLM/other] for
contract lifecycle management.

**The thing that hurts:** [what they said hurts — write it in their words]

---

## Who's using this

**Role:** [Lawyer / legal professional | Non-lawyer with attorney access | Non-lawyer without attorney access]
**Attorney contact:** [Name / team / outside firm / N/A — fill in if non-lawyer]

---

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| CLM (Ironclad, Agiloft, etc.) | [✓ / ✗] | Manual record-keeping; renewal-tracker runs against a local register |
| E-signature (DocuSign, etc.) | [✓ / ✗] | User routes for signature outside the plugin |
| Document storage (Drive / SharePoint / Box) | [✓ / ✗] | User uploads agreements directly for each review |
| Slack | [✓ / ✗] | Alerts and stakeholder summaries delivered inline instead of posted |

*Re-check: `/commercial-legal:cold-start-interview --check-integrations`*

---

## Playbook

**Active side:** [sales / purchasing / both]

*Sales-side = the company sells its products or services. We're the vendor. Usually our paper. Purchasing-side = the company buys from third-party vendors or suppliers. We're the customer. Usually their paper. The answer changes every playbook position.*

> Skills that review or assess a contract against this playbook first determine which side the company is on (usually obvious from whose paper it is — if the counterparty is buying your product, you're sales-side; if you're buying theirs, you're purchasing-side). If it's not obvious, ask. Read the matching playbook section. Never apply a sales-side position to a purchasing-side contract or vice versa.

### Sales-side playbook

*Applies when the company is the vendor. Usually our paper.*

*[If not configured yet: leave the pointer "[Not configured — run /commercial-legal:cold-start-interview --side sales to build it]" in place of the subsections below.]*

#### Limitation of liability

**Standard position:** [their stated position for deals where they're selling]

**Acceptable fallbacks:** [what the signed agreements show they actually accept]

**Never accept:** [their hard nos]

**Carveouts we accept:** [list]

> *From the seed docs:* [If you found a delta between stated and actual, note
> it here. E.g., "Stated standard is a 12-month cap. 3 of 5 reviewed agreements
> closed at 24 months. Treating 24 months as an acceptable fallback."]

#### Indemnification

[same structure]

#### Data protection

[same structure]

#### Term and termination

[same structure]

#### Governing law and venue

**Preferred:** [list]
**Acceptable:** [list]
**Escalate:** [list]
**Never:** [list]

#### The one thing

[The deal-breaker they named for sales-side deals. This is the first thing every sales-side review checks.]

---

### Purchasing-side playbook

*Applies when the company is the customer. Usually their paper.*

*[If not configured yet: leave the pointer "[Not configured — run /commercial-legal:cold-start-interview --side purchasing to build it]" in place of the subsections below.]*

[Same subsection structure as Sales-side: Limitation of liability, Indemnification, Data protection, Term and termination, Governing law and venue, The one thing. Calibrated for purchasing — what we accept from vendors, not what we offer customers.]

---

## Escalation

| Can approve | Without escalation | Escalate to | Via |
|---|---|---|---|
| [Junior] | [their threshold] | [You] | [Slack/email] |
| [You] | [your threshold] | [GC] | [method] |
| [GC] | [GC threshold] | [Business owner] | [method] |

**Dollar thresholds:** [if they mentioned any]

**Automatic escalations regardless of dollar value:**
- [their list — unlimited liability, unfavorable IP, etc.]

---

## House style

**Tone in redlines:** [terse? collaborative? depends on counterparty?]

**Stakeholder summaries:** [who reads them? how long should they be?]

**Where work product goes:** [[CLM]? Google Drive folder? Slack thread?]

**Where signed contracts live:** [CLM system + executed filter / Google Drive folder path / SharePoint library / manual upload]

---

## Outputs

**Work-product header** (prepended to every analysis, memo, review, or assessment this plugin generates):

- If Role is Lawyer / legal professional: `PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT — PREPARED AT THE DIRECTION OF COUNSEL`
- If Role is Non-lawyer: `RESEARCH NOTES — NOT LEGAL ADVICE — REVIEW WITH A LICENSED ATTORNEY, SOLICITOR, BARRISTER, OR OTHER AUTHORISED LEGAL PROFESSIONAL IN YOUR JURISDICTION BEFORE ACTING`

Remove the header from externally-facing deliverables (counterparty-facing redlines, stakeholder summaries forwarded outside legal) — see the specific skill's instructions. Confirm the correct marking for your jurisdiction and matter.

---

## Seed documents reviewed

| Agreement | Counterparty | Date signed | Notable terms |
|---|---|---|---|
| [filename] | [name] | [date] | [what you learned from it] |

---

## Review preferences

confirm_routing: true   # Set to false to skip routing confirmation and proceed automatically

---

## NDA triage preferences

closing_action: "[what the user said to append to every NDA triage output — e.g., 'Forward this output and the NDA to your contracts manager.']"

---

## Playbook monitor settings

pattern_threshold: 5
lookback_months: 12

*Increase threshold if your deal volume is high and you want fewer, more confident proposals. Decrease if you want earlier signals.*

---

*To re-run the interview: `/commercial-legal:cold-start-interview --redo`*
```

## After writing the practice profile

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list (not a generic template — these are the concrete things this plugin does best):

> **Here's what I'm good at in commercial contracts:**
>
> - **Review a vendor MSA against your playbook** — e.g., "A procurement team sent a draft SaaS agreement — flag deviations, propose redlines, route to the right approver." Try: `/commercial-legal:review`
> - **Triage an inbound NDA to GREEN / YELLOW / RED** — e.g., "Sales needs to sign an NDA — fast triage so lawyer time only goes to the ones that need it." Try: `/commercial-legal:review`
> - **Track renewal deadlines** — e.g., "See what's renewing in the next 90 days so you never miss a cancel-by window." Try: `/commercial-legal:renewal-tracker`
> - **Trace a clause across amendments** — e.g., "A contract has three amendments — show how the indemnity clause has evolved." Try: `/commercial-legal:amendment-history`
> - **Escalate a deviation** — e.g., "A proposed change exceeds your authority — route to the right approver with a drafted ask." Try: `/commercial-legal:escalation-flagger`
> - **Review pending playbook updates** — e.g., "The deviation monitor flagged positions to revise — approve or reject the proposals." Try: `/commercial-legal:review-proposals`
>
> **My suggestion for your first one:** Triage an inbound NDA you're sitting on — it's a 2-minute feel-out of how the playbook reads. Or tell me what's on your plate and I'll pick.

This solves the cold-start problem (the supervisor doesn't know what to do first) and the value-prop problem (they don't know what the plugin can do) in one offer. Make the list specific. Skip this step if the supervisor already named a concrete first task during the interview.


1. **Show it to them.** Not the whole thing — a summary. "Here's what I heard. Take a look at the plugin config and tell me what I got wrong."

2. **Research connector prompt.** Say:

   > "Before your first contract review: connect a research tool. Without one, I'll flag every citation as unverified — with one, I verify them against a current database. In Cowork: Settings → Connectors. In Claude Code: authorize when a skill prompts you."

3. **Propose starter skills.** Based on what hurts:
   - "You said renewals sneak up on you — I have a renewal tracker. Want me to scan [CLM] for everything expiring in the next 90 days?"
   - "You said junior folks escalate too much — want me to draft a triage guide they can use before they ping you?"

4. **Offer a test run.** "Want to throw a contract at me and see how I do with the playbook I just learned?"

5. **Close with a note on changeability.** End with something like:

   > "Done. Your practice profile is at `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` — it's a plain text file you can read and edit directly. Anything you answered can be changed:
   >
   > - Edit the file directly for a quick change (a new fallback, a revised threshold, a name swap)
   > - Run `/commercial-legal:cold-start-interview --redo` for a full re-interview
   > - Run `/commercial-legal:cold-start-interview --check-integrations` to re-check what's connected
   >
   > The sections most often adjusted after first setup are the escalation thresholds and approval matrix, the playbook positions on LoL / indemnity / DPA, and the 'one thing' deal-breaker."

## Your practice profile learns

After writing the practice profile, close with this note:

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - The `playbook-monitor` agent watches for patterns. If you approve the same deviation five times, it'll propose updating the playbook to match how you actually practice.
> - You can always say "update my playbook to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.
> - Run `/commercial-legal:cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.
>
> Ten minutes of setup gets you a working profile. A month of use gets you one that reads like you wrote it yourself.

## Tone

Warm, curious, a little bit delighted to be here. You're the new hire who did their homework. You're not a form. Don't say "please provide" — say "what's the deal with". Don't say "configure your settings" — say "tell me how your team works".

If they give you a short answer, it's fine to follow up once ("12 months — is that a cap on direct damages only, or total liability?") but don't drill. You can always ask later when it comes up in a real review.

## Failure modes to avoid

- **Don't write YAML.** The practice profile is prose with occasional tables. They edit it in a text editor, not a schema validator.
- **Don't skip the seed docs.** The interview tells you what they think their playbook is. The docs tell you what it actually is. Both matter.
- **Don't write a generic playbook.** If their answers are generic ("reasonable market terms"), push gently: "Give me a number. When a vendor says 24-month cap, do you counter or sign?"
- **Don't promise things the other skills can't deliver.** Check what skills exist in this plugin before offering them.
- **Don't run this interview on every session.** Check the plugin config first. If it's populated, you're done.

---

## /commercial-legal:customize

---
name: customize
description: >
  Guided customization of your commercial contracts practice profile — change
  one thing without re-running the whole cold-start interview. Adjust risk
  posture, escalation contacts, playbook positions, NDA triage preferences,
  house style, review preferences, or matter workspace paths. Use when the
  user says "change my [thing]", "update my profile", "edit my playbook",
  "tune my config", or "customize".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/commercial-legal:customize`. They want to change something
in their practice profile — a risk posture, an escalation contact, a playbook
position, a jurisdiction, an output format — without re-running the whole
cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`
   (and `~/.claude/plugins/config/claude-for-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/commercial-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting, sales-side vs. purchasing-side orientation *(shared across all
     12 plugins — changes flow through `company-profile.md`)*
   - **Risk posture** — conservative / middle / aggressive, what each means
     for fallback positions and escalation triggers
   - **People** — escalation chain, approvers by dollar threshold and by
     clause type
   - **Playbook positions** — the substantive contract positions: liability
     caps, indemnity scope, IP ownership, data protection, termination,
     auto-renewal, price escalation, and the fallbacks for each
   - **NDA triage preferences** — what green / yellow / red looks like for
     inbound NDAs
   - **Review preferences** — redline style, explanation depth, whether to
     produce a stakeholder summary by default
   - **House style** — document format, signature block, renewal-alert
     channel, deviation-log format
   - **Workflow** — matter workspace paths, intake path, renewal watcher
     cadence
   - **Integrations** — Ironclad / DocuSign / Slack / document storage
     status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Liability cap fallback 12 months → 6 months:* "`/review` will now flag
     anything above 6 months as a deviation; existing deal-debrief entries
     stay as logged."
   - *New escalation approver:* "Any redline exceeding your own authority
     will now route to this approver — `/escalate` will include them by
     default for the matching risk band."
   - *Risk posture middle → aggressive:* "I'll accept more vendor-friendly
     positions without flagging them and shift the `[review]` bar higher."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/commercial-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" something, set it
  to `[Not configured]` and explain what that means for the plugin's behavior.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., risk posture aggressive + "every redline needs GC
  approval"; or "sales-side" + a purchasing-side playbook position), flag the
  tension and ask which one they want.
- **Flag guardrail degradation.** If the user asks to turn off a guardrail
  (drop the `[review]` flag, skip the privilege header, remove `[verify]`
  tags), explain what the guardrail protects against and confirm they
  understand the trade-off. The `[review]` flag, source attribution tags, and
  `[verify]` tags on cited statutes are load-bearing and should not be
  removed.
- **One change at a time.** Don't re-ask the whole interview.

---

## /commercial-legal:escalation-flagger

---
name: escalation-flagger
description: >
  Route a contract issue to the right approver per the escalation matrix in
  `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, and draft the ask. Use when the user
  says "who needs to approve this", "escalate this", "does this need GC sign-off",
  "route this for approval", or when another skill finds an issue that exceeds the
  reviewer's authority.
argument-hint: "[describe the issue, or reference a review memo]"
---

# /escalation-flagger

Names the approver for a contract issue per the `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` escalation matrix and drafts the message so you're not writing "hey got a sec" at 5pm.

## Instructions

1. **Load `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`** → Escalation section. If missing, say so — the practice profile needs editing.

2. **Characterize the issue:** dollar threshold / term deviation / automatic trigger / business decision.

3. **Match to matrix, name the approver.** Be specific — a person or role, not "legal leadership."

4. **Draft the ask** per the template below: what the contract says, what playbook says, options with recommendation, decision-by date.

5. **Do not send.** Draft it, show it, let the lawyer send.

## Examples

```
/commercial-legal:escalation-flagger
The Acme MSA has uncapped liability — who approves and what do I say?
```

```
/commercial-legal:escalation-flagger
Reference: acme-review-memo.md
Issue: §8.2 indemnity carveouts
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Every contracts team has an escalation matrix, written or not. This skill reads the written one (in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`), matches a contract issue against it, names the approver, and drafts the ask so the lawyer isn't writing "hey do you have a sec" messages at 5pm.

## Load the matrix

**Which side?** Before matching to the matrix, determine which side the company is on for the contract whose issue is being escalated. Usually obvious: if the counterparty is a vendor/supplier providing goods or services, you're purchasing-side. If the counterparty is a customer buying your product/service, you're sales-side. If it's not obvious, ask. Read the matching playbook section (`### Sales-side playbook` or `### Purchasing-side playbook`) to evaluate whether the term is inside fallbacks or triggers an automatic escalation — a term that's fine on one side can be a hard-no on the other. Note which side in the drafted ask so the approver knows which playbook was applied.

Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## Escalation`. If it's missing or vague, say so — the cold-start interview should have captured this, and if it didn't, the practice profile needs editing.

Expected structure:

| Can approve | Threshold | Escalates to | Via |
|---|---|---|---|
| Paralegal | Standard terms, <$50K | Counsel | Slack |
| Counsel | Non-standard but within fallbacks, <$500K | GC | Slack or email |
| GC | Everything else | CFO/Board | Meeting |

Plus **automatic escalation triggers** — things that escalate regardless of dollar value. Typically: unlimited liability, IP assignment, anything on the "never accept" lists.

## Workflow

### Step 1: Characterize the issue

What's being escalated?

- **Dollar threshold:** Contract value exceeds someone's approval authority
- **Term deviation:** A term is outside the playbook fallbacks — someone more senior needs to decide whether to accept
- **Automatic trigger:** One of the always-escalate items is present
- **Business decision:** Not a legal call — needs the business owner, not legal leadership

Don't escalate things that are actually fine. If the term is within the fallbacks in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, it doesn't need to go up.

### Step 2: Match to the matrix

```
Is the issue an automatic trigger?
  → YES: escalate to [person named for that trigger]
  → NO: continue

Is the contract value above the reviewer's threshold?
  → YES: escalate to whoever has authority at that dollar level
  → NO: continue

Is the term deviation outside all documented fallbacks?
  → YES: escalate to whoever can approve non-standard terms
  → NO: reviewer can approve — no escalation needed
```

### Step 3: Name the approver

Be specific. Not "escalate to legal leadership" — name the person or role from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the matrix doesn't name anyone for this situation, say so: "The escalation matrix doesn't cover [situation]. Suggest asking [GC name] who owns this."

### Step 4: Draft the ask

The approver should be able to decide from the message alone — no "let me pull up the contract."

```markdown
**Escalating to:** [name]
**Via:** [Slack #channel / email / meeting — per `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`]
**Urgency:** [deadline if there is one]

---

Hey [name] —

Need your call on the [Counterparty] [agreement type]. [One sentence on deal context.]

**The issue:** [Plain English, one paragraph. What they want, why it's outside
our standard, what the risk actually is.]

**What the contract says:**
> "[exact quote]"

**What our playbook says:** [quote from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`]

**Options:**
1. **Accept** — [one line on why this might be okay]
2. **Push back with:** "[proposed counter-language]" — [one line on likely counterparty reaction]
3. **Walk** — [one line on whether that's realistic given the business context]

**My recommendation:** [which option and why, briefly]

**Need a decision by:** [date, if there is a deadline]

[Link to full review memo]
```

### Step 5: Record the escalation

If this team uses a ticket system or [CLM] approval workflows, log it. If not, note in the review memo that the escalation was sent, to whom, and when. The next person who reads the memo should see the status.

## Calibration: when in doubt, escalate with a note

The cost of an unnecessary escalation is ~30 seconds of the approver's time — they read, say "fine, proceed," and the record shows they saw it. The cost of a missed escalation is signing an unapproved term, which is a one-way door. The costs are not symmetric. **When in doubt, escalate.**

The calibration for what warrants escalation lives in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, not in this skill. Check the playbook's stated position, its fallbacks, and its "automatic escalation regardless of dollar value" list:

- **Clearly inside the fallback range:** no escalation needed.
- **Clearly outside the range, or on the automatic-escalation list:** escalate.
- **Uncertain — the term is ambiguous, novel, or arguably inside the range but the argument is a stretch:** escalate anyway, and note the uncertainty explicitly. The draft flags the specific question the approver needs to decide and why the skill couldn't confidently place it inside the fallback. The approver narrows; the skill does not.

Do not suppress an escalation because over-escalation might train approvers to skim. That's an approver-experience problem the attorney solves by adjusting thresholds in the playbook, not a problem the skill solves by making its own subjective call on a term it's uncertain about.

If a term comes up that the playbook doesn't address, don't guess the threshold — ask the reviewing attorney whether this class of issue should escalate, and offer to record the answer in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` so future reviews are consistent.

## What this skill does not do

- It does not approve anything. It routes.
- It does not decide between the options. The draft includes a recommendation but the approver decides.
- It does not send the escalation message — it drafts it. The lawyer sends it after reading.

---

## /commercial-legal:governing-law-review

---
name: governing-law-review
description: >
  Cross-border mega-skill: Sözleşmeden yargı çevrelerini otomatik tespit eder,
  karşı taraf ülke bazlı risk profili çeker (OpenSanctions + ülke rehberi),
  MÖHUK 5718 / NY Konvansiyonu icra analizini yapar, çoklu yargı çevresi
  katmanlarını (governing law ≠ arbitration seat ≠ counterparty ülkesi) ayrı
  ayrı ele alır. Tüm yabancı hukuk sorularında kullan.
argument-hint: "[sözleşme dosyası | governing-law + jurisdiction + tahkim klozunu yapıştır]"
---

# /governing-law-review — Cross-Border Yargı Çevresi & İcra Analizi (v1.8.0)

Birincil yargı çevresi Türkiye'dir. Bu skill yabancı hukuk seçimini analiz eder, Türk hukukunu ikame etmez.
Rehberler: `karsilastirmali-hukuk-rehberi.md` (bağlayıcı) + ilgili yargı çevresi `*-rehberi.md`.

## Precondition

`commercial-legal/CLAUDE.md` → `Governing law and venue` bölümünü oku.
Placeholder ise "provisional" modda devam et: varsayılan tercih → İngiliz hukuku + ICC/LCIA **veya** Türk hukuku + ISTAC.

---

## Adım 0 — Sözleşme tarama: tüm yargı unsurlarını çıkar

Sözleşmeden şunları birebir alıntıla:

| Unsur | Metin |
|---|---|
| Uygulanacak hukuk (governing law) | "[...]" |
| Yetkili mahkeme (jurisdiction/venue) | "[...]" |
| Tahkim klozu — kurum / seat / kural / dil / hakem | "[...]" |
| Karşı taraf tüzel kişinin ülkesi | [tespit et] |
| Asimetri: tek tarafa opsiyon var mı? | [evet/hayır] |
| Birden fazla governing law klozu var mı? | [evet/hayır] |

---

## Adım 1 — Yargı çevresi haritası

Tüm unsurları haritalandır. Farklı katmanlar varsa her biri ayrı analiz gerektirir:

```
Governing law  : [örn. İngiliz hukuku]
Venue/tahkim   : [örn. ICC Paris, seat Cenevre/İsviçre]
Karşı taraf    : [örn. Alman şirket — BGB/HGB]
TR bağlantısı  : [[ŞİRKET ADI] taraf — Türk hukuku iş hukuku + vergi uygulanır]
```

**Uyarı — çoklu yargı çevresi tetikleyici:**
Governing law ≠ arbitration seat ≠ counterparty ülkesi ise 🟠 flag koy. Her katman ayrı risk ve Adım 4'te ayrı analiz gerektirir.

---

## Adım 2 — şirket-default karşılaştırması

CLAUDE.md `Governing law and venue` ile karşılaştır. Severity:

| Durum | Severity |
|---|---|
| Tercih listesinde (İngiliz/Türk + ICC/LCIA/ISTAC) | 🟢 |
| Tercih dışı ama kabul edilebilir (Fransız, İsviçre OR + ICC) | 🟡 |
| Asimetrik venue — tek tarafa mahkeme seçim hakkı | 🟠 |
| Karanlık yargı çevresi (belirsiz devlet hukuku, kısıtlı mahkeme erişimi) | 🔴 |
| Rusya, İran, OFAC yaptırım altındaki ülke mahkemesi | 🔴 — dur, [UYUM DİREKTÖRÜ]'e sor |

---

## Adım 3 — Karşı taraf ülke risk profili

Karşı tarafın ülkesine göre iki paralel kontrol:

### 3a. OpenSanctions taraması
Karşı taraf tüzel kişiyi OpenSanctions'da tara (`opensanctions-rehberi.md`).
Eşleşme varsa → Adım 3b'ye geçme, dur ve [UYUM DİREKTÖRÜ]'e eskalasyon öner.

### 3b. Ülke bazlı mevzuat kontrol
Karşı tarafın hukuku governing law değilse bile taraf yükümlülükleri yerel mevzuata tabi olabilir. İlgili rehberi oku ve gerekirse WebFetch ile bağımlı kanunu çek:

| Karşı taraf ülkesi | Rehber | Kritik kontrol |
|---|---|---|
| 🇬🇧 İngiltere | `uk-legislation-rehberi.md` | Arbitration Act 1996, UCTA 1977 s.3 |
| 🇺🇸 ABD | `us-legislation-rehberi.md` + `courtlistener-rehberi.md` | CISG opt-out, UCC Art.2, FAA §2 |
| 🇩🇪 Almanya | `germany-legislation-rehberi.md` | BGB §307 standart şart denetimi, HGB |
| 🇫🇷 Fransa | `france-legislation-rehberi.md` | Code civil m.1171 (haksız şart), m.1442 |
| 🇨🇭 İsviçre | `switzerland-caselaw-rehberi.md` | IPRG m.178 tahkim sözleşmesi, OR m.19 |
| 🇮🇹 İtalya | `italy-legislation-rehberi.md` | Codice Civile, D.Lgs. 231/2001 |
| 🇯🇵 Japonya | `japan-legislation-rehberi.md` | Companies Act, FEFTA (yabancı taraf ise) |
| 🇪🇺 AB şirketi | `eu-legislation-rehberi.md` | GDPR, AI Act, NIS2 uyum yükümlülüğü |
| 🇦🇿 Azerbaycan ([ANA ORTAK]) | TR Legal MCP + model | Azerbaycan hukuku — özel dikkat |

Çekilen kanunlara `[DE Mevzuat — ...]` / `[UK Legislation — ...]` vb. atıf koy.
Çekemediğin hukuku `[model bilgisi — doğrulayın]` etiketle.

---

## Adım 4 — İcra-edilebilirlik: governing law connector teyidi

**Governing law**'u fiilen çek:
- İngiliz hukuku → `uk-legislation-rehberi.md` → `legislation.gov.uk` WebFetch
- ABD hukuku → `us-legislation-rehberi.md` + `courtlistener-rehberi.md` → citation verification zorunlu
- Alman hukuku → `germany-legislation-rehberi.md` → gesetze-im-internet.de/NeuRIS
- Fransız hukuku → `france-legislation-rehberi.md` → Légifrance
- İsviçre hukuku → `switzerland-caselaw-rehberi.md` → OpenCaseLaw.ch MCP + Fedlex
- AB hukuku → `eu-legislation-rehberi.md` → EUR-Lex CELEX
- Türk hukuku → TR Legal MCP (TBK m.24 governing law seçimi, MÖHUK m.24)

**Tahkim seat** ayrıca kontrol et: seat ülkesinin tahkim mevzuatı arbitral prosedürü yönetir.
- İsviçre seat → IPRG m.176-194 (OpenCaseLaw.ch)
- Fransa seat → Code de procédure civile m.1504 vd.
- İngiltere seat → Arbitration Act 1996

---

## Adım 5 — MÖHUK 5718 + NY Konvansiyonu icra analizi (KRİTİK)

Hüküm/karar Türkiye'de icra edilecekse her iki yol için:

### 5a. Yabancı mahkeme kararı — MÖHUK m.50-59
Tenfiz şartları (m.54):
1. **Mütekabiliyet** — karşı taraf devleti TR kararlarını tanıyor mu? `[verify]`
2. **Kamu düzeni** — karar TR kamu düzenine aykırı mı? (nişan bozma, faiz vs.)
3. **Savunma hakkı** — yargılamada usul ihlali var mı?
4. **Münhasır yetki** — TR mahkemelerinin münhasır yetkisi söz konusu mu? (taşınmaz, miras)
5. **Kesinleşme** — karar kesinleşmiş mi?

### 5b. Yabancı hakem kararı — NY Konvansiyonu + MÖHUK m.60-62
NY Konvansiyonu Madde V ret gerekçeleri (m.61 kapıları):
- Tahkim sözleşmesinin geçersizliği
- Usul ihlali / haber verilmeme
- Hakem yetkisi aşımı
- Hakem heyeti / prosedür anlaşmayla uyumsuzluk
- Kamu düzeni (m.V/2b)

**Sonuç formatı:**
```
Türkiye'de icra: [MÜMKÜN / SORUNLU / BELİRSİZ]
Engel riski: [🔴 Yüksek / 🟠 Orta / 🟡 Düşük / 🟢 Yok]
[review] gerektiren: [spesifik şart veya boşluk]
```

---

## Adım 6 — Çoklu yargı çevresi katman analizi

Governing law ≠ seat ≠ counterparty ülkesi ise her katman için:

```
Katman 1 — Governing law [örn. İngiliz hukuku]:
  → Maddi hukuk: sözleşme yorumu, sorumluluk, fesih [Adım 4]
  → Connector: UK Legislation WebFetch

Katman 2 — Arbitration seat [örn. Cenevre/İsviçre]:
  → Usul hukuku: tahkim yürütmesi, delil, hakem reddi
  → Connector: OpenCaseLaw.ch MCP + Fedlex IPRG m.176-194

Katman 3 — Karşı taraf ülkesi [örn. Almanya]:
  → Taraf yükümlülükleri: iş hukuku, veri, rekabet uyumu
  → Connector: gesetze-im-internet.de / NeuRIS

Katman 4 — Türkiye ([ŞİRKET ADI] taraf):
  → İcra ayağı: MÖHUK 5718 / NY Konvansiyonu [Adım 5]
  → Bağlantı noktaları: iş hukuku, vergi, EPDK lisans
```

Çakışma riski: iki governing law aynı anda uygulanabilirse ya da çelişen zorunlu kurallar (mandatory rules) varsa 🔴 flag + `[review]`.

---

## Adım 7 — Severity özeti ve memo

| Kriter | Severity |
|---|---|
| OpenSanctions eşleşmesi | 🔴 dur |
| Rusya/İran/OFAC mahkemesi | 🔴 |
| Çakışan mandatory rules | 🔴 |
| MÖHUK tenfiz engeli yüksek | 🔴 |
| Asimetrik venue / tek taraflı seçim | 🟠 |
| Çoklu yargı çevresi — her biri kontrol edildi | 🟡 |
| şirket-default dışı ama kabul edilebilir | 🟡 |
| Tercih listesinde | 🟢 |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# Cross-Border Yargı & İcra Analizi — [Sözleşme adı]

## ⚠️ Reviewer note
- **Kaynaklar:** [TR Legal MCP / UK / DE / FR / CH / EU / CourtListener — hangileri çekildi]
- **Governing law:** [...] | **Seat:** [...] | **Karşı taraf ülkesi:** [...]
- **Çoklu katman:** [evet/hayır — kaç katman]
- **Türkiye icra:** [MÜMKÜN / SORUNLU / BELİRSİZ]
- **[review] sayısı:** N

## Bottom line (2 cümle)

## Yargı çevresi haritası

## Karşı taraf risk profili (OpenSanctions + ülke rehberi)

## İcra-edilebilirlik bulguları (connector atıflı)

## MÖHUK / NY Konvansiyonu icra analizi

## Çoklu katman özeti (varsa)

## Önerilen kloz / redline
```

CLAUDE.md `## Outputs` decision tree ile kapat. Yüksek riskli değişiklik counterparty'ye gitmeden önce avukat/GC onayı şart.

---

## /commercial-legal:matter-workspace

---
name: matter-workspace
description: >
  Manage matter workspaces — new, list, switch, close, or detach (practice-level).
  Use when a multi-client practitioner needs to create a matter, switch the active
  matter, list matters, archive a matter, or detach to practice-level context, or
  when another skill needs to know which matter it's working in.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Practitioners work across multiple clients and matters. A matter workspace keeps one client or engagement's context separate from every other. This command manages those workspaces.

## Subcommands

- `/commercial-legal:matter-workspace new <slug>` — create a new matter workspace, run a short intake, write `matter.md`
- `/commercial-legal:matter-workspace list` — list matters with status and active flag
- `/commercial-legal:matter-workspace switch <slug>` — set the active matter
- `/commercial-legal:matter-workspace close <slug>` — archive a matter (move to `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/_archived/`, never delete)
- `/commercial-legal:matter-workspace none` — detach from any active matter, work at practice-level only

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` — confirm the `## Matter workspaces` section is populated. If `Enabled` is `✗`, tell the user: "Matter workspaces are off — you're configured as an in-house practice with one client, so the plugin works from practice-level context automatically. If you actually work across multiple clients, re-run `/commercial-legal:cold-start-interview --redo` and select a private-practice setting. Otherwise, you don't need `/matter-workspace` at all." Don't error — the disabled state is the expected one for in-house users.
2. Use the subcommand logic below.
3. Dispatch on the first token of `$ARGUMENTS`:
   - `new` → run the intake interview, write `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<slug>/matter.md`, seed `history.md` and `notes.md`.
   - `list` → enumerate `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/*/matter.md`, print a table, mark the active matter.
   - `switch` → update the `Active matter:` line in the practice-level CLAUDE.md.
   - `close` → move `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<slug>/` to `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/_archived/<slug>/`, log the close date in `history.md`.
   - `none` → set `Active matter:` to `none — practice-level context only`.
4. Show the user what changed and confirm before writing.

## Notes

- The skill never reads across matters unless `Cross-matter context` is `on` in the practice-level CLAUDE.md.
- Archiving is not deletion — closed matters remain readable for retention/conflicts purposes.
- Slugs are lowercase with hyphens. If a slug is reused across archived and active, the archived one is preserved under `_archived/<slug>/`.

---

Multi-client practitioners (private practice — solo, small firm, large firm) work across many matters. Context from one must not leak into another. This skill is the thin file-management layer that makes that true.

**Default state is off.** In-house users never see this — they run at practice-level only. Matter workspaces turn on at cold-start for private-practice users, or by editing `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, this skill does not run; the workflow above explains the disabled state and suggests `/commercial-legal:cold-start-interview --redo` for users who actually need matter isolation.

## Storage layout

All matter data lives under:

```
~/.claude/plugins/config/claude-for-legal/commercial-legal/
├── CLAUDE.md                       # practice-level practice profile
└── matters/
    ├── <slug>/
    │   ├── matter.md               # client, counterparty, matter type, key facts, overrides
    │   ├── history.md              # dated log of events, decisions, drafts, reviews
    │   ├── notes.md                # free-form working notes
    │   └── outputs/                # skill outputs for this matter (optional subfolder)
    └── _archived/
        └── <slug>/                 # closed matters — readable but not active
```

Slugs are lowercase with hyphens. Examples: `acme-msa-2026`, `zenith-renewal`, `vendor-xyz-nda`.

## Active matter is in the practice CLAUDE.md

The `Active matter:` line under `## Matter workspaces` in the practice-level CLAUDE.md is the single source of truth. Switching a matter edits that line. No separate state file.

## Subcommand logic

### `new <slug>`

1. Confirm slug is not already present in `matters/<slug>/` or `matters/_archived/<slug>/`. If reused, ask the user to pick a different slug.
2. Run the intake interview:
   - **Client** (the party we represent, or the internal business unit if in-house)
   - **Counterparty** (the other side — may be multiple)
   - **Matter type** (read the plugin's practice profile for typical categories; for commercial-legal: vendor MSA | customer agreement | NDA | SaaS subscription | amendment | renewal | other)
   - **Confidentiality level** (standard | heightened | clean-team — heightened prompts extra care in cross-matter settings)
   - **Key facts** (2–5 sentences: what this matter is about, who the stakeholders are, what's at stake)
   - **Matter-specific overrides to the practice playbook** (e.g., "client requires 24-month LoL cap not 12", "counterparty is a strategic partner — relationship-preserving tone")
   - **Related matters** (slugs of any connected matters)
3. Write `matters/<slug>/matter.md` using the template below.
4. Seed `matters/<slug>/history.md` with a single "Opened" entry.
5. Create an empty `matters/<slug>/notes.md`.
6. Do **not** auto-switch to the new matter. Ask: "Want to switch to `<slug>` now? (`/commercial-legal:matter-workspace switch <slug>`)"

### `list`

Enumerate `matters/*/matter.md`. Read each file's front-matter or first few lines to extract status. Print a table:

| Slug | Client | Matter type | Status | Opened | Active |
|---|---|---|---|---|---|

Mark the currently-active matter with `*`. Include `_archived/*` under a separate "Archived" heading if any exist.

### `switch <slug>`

1. Confirm `matters/<slug>/matter.md` exists. If not, offer `/commercial-legal:matter-workspace new <slug>`.
2. Edit the `Active matter:` line in the practice-level CLAUDE.md to `Active matter: <slug>`.
3. Show the user the matter.md summary so they can confirm they're on the right matter.

### `close <slug>`

1. Confirm `matters/<slug>/` exists.
2. Append a "Closed" entry to `matters/<slug>/history.md` with today's date.
3. Move `matters/<slug>/` → `matters/_archived/<slug>/`.
4. If the closed matter was the active matter, set `Active matter:` to `none — practice-level context only`.

### `none`

Set `Active matter:` in the practice-level CLAUDE.md to `none — practice-level context only`. Confirm with the user.

## `matter.md` template

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this` in the practice-level CLAUDE.md]

# Matter: [Client] — [short description]

**Slug:** [slug]
**Opened:** [YYYY-MM-DD]
**Status:** active
**Confidentiality:** [standard / heightened / clean-team]

---

## Parties

**Client:** [name]
**Counterparty:** [name(s)]

## Matter type

[vendor MSA | customer agreement | NDA | SaaS subscription | amendment | renewal | other — with one-line rationale]

## Key facts

[2–5 sentences. What this matter is about. Who the stakeholders are. What's at stake. What makes it different from the default playbook.]

## Matter-specific overrides

*Any deviation from the practice-level playbook that applies to this matter and only this matter.*

- [e.g., "LoL cap: client requires 24 months, not house standard 12."]
- [e.g., "Tone: relationship-preserving — counterparty is a strategic partner."]
- [e.g., "Governing law: must be English law, not Delaware."]

## Related matters

- [slug — one line why related]

## Notes on confidentiality

[If heightened or clean-team, describe why. Who may see matter files. Whether cross-matter context is permissible even if globally on.]
```

## `history.md` seed

```markdown
# History: [Client] — [short description]

Append-only event log. Most recent at top.

---

## [YYYY-MM-DD] — Matter opened

Intake completed. Slug: `[slug]`. Status: active.
[Any initial context worth preserving beyond matter.md — e.g., "Opened in response to inbound MSA draft from [counterparty]."]
```

## Cross-matter context

The practice-level CLAUDE.md has a `Cross-matter context:` flag. When it's `off` (the default), a skill working in matter A **never reads** files in `matters/B/` for any other `B`. Period. This is the confidentiality guarantee the setting exists to provide.

When it's `on`, a skill may read files across matter folders only when the user explicitly asks it to (e.g., "compare our position on liability caps across the last five vendor matters"). Even when `on`, the default is to load only the active matter unless the user asks for a cross-matter view.

## What this skill does not do

- **Run a conflicts check.** Conflicts are the practitioner's/firm's job; the intake captures what the user declares.
- **Enforce retention.** Closing archives a matter; it does not delete. Retention policy is out of scope.
- **Auto-route outputs.** The substantive skill decides where to write; this skill tells it *which folder* is active, not what to put in it.
- **Decide whether cross-matter is appropriate.** It reads the flag and obeys.

---

## /commercial-legal:nda-review

---
name: nda-review
description: >
  Reference: fast triage of inbound NDAs into GREEN / YELLOW / RED so the team only
  spends lawyer time on the ones that need it. Built for sales and BD to self-serve
  before pinging legal. Loaded by /commercial-legal:review when an NDA is detected.
user-invocable: false
---

# NDA Review

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for work product) waive the protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitized version for the broader channel, or (c) both — don't silently apply a privileged header and then help paste it somewhere the header won't protect it. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

Most inbound NDAs are fine. A few have landmines. This skill sorts them in under a minute so legal only reads the ones that matter.

**The goal:** a GREEN NDA should need nothing more than a signature. A YELLOW needs a lawyer's eyes on one or two specific things. A RED stops before anyone wastes time.

## Load the playbook first

**Which side?** Before applying the playbook, determine which side the company is on for this NDA. Usually obvious from the context: if the counterparty is a vendor or partner evaluating your product, you're sales-side; if you're evaluating theirs, you're purchasing-side. Mutual NDAs still have a side — whose paper is it, and which direction is the evaluation running. If it's not obvious, ask. Read the matching playbook section (`### Sales-side playbook` or `### Purchasing-side playbook`) from the config. Note which side in the output so the reviewer knows which playbook was applied. If the matching side is `[Not configured]`, stop and tell the user to run `/commercial-legal:cold-start-interview --side <side>` before this triage can proceed.

**Before triaging anything, read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## Playbook` → the matching side → `NDA triage positions`.** That section is the source of truth for what makes an NDA GREEN, YELLOW, or RED for *this* team on *this* side. This skill does not ship with default positions on NDA terms — the law, the market, and each team's risk tolerance vary too much for hardcoded defaults to be safe.

If `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` doesn't have an `NDA triage positions` section yet, or it's silent on a term that comes up in the NDA you're reviewing, ask the user:

> Your playbook doesn't cover [term — e.g., "residuals clauses," "survival period," "one-way NDAs where you're the receiver"]. What's your default position — when should this be GREEN, when YELLOW, when RED? I'll add it to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` so the next review is consistent.

Then record the answer in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` and proceed with the triage using the new position.

## Scope check

**Before reviewing NDA-specific provisions, check whether the document is doing more than its name suggests.** Mutual commercial NDAs can hide: standstills, licensing grants, exclusivity, non-solicits, non-competes, IP assignments, right of first refusal, most-favored-nation clauses, and arbitration/jurisdiction clauses that govern far more than confidentiality disputes.

If the NDA contains obligations beyond confidentiality: **auto-YELLOW regardless of the NDA-term analysis.** Flag the non-NDA provisions:

> This document is labeled an NDA but contains [standstill / license grant / non-solicit / exclusivity / IP assignment / ROFR / MFN / broad arbitration]. It's more than an NDA. Route for attorney review.

Do not silently push a document labeled "NDA" through NDA triage when the substantive obligations are a services agreement, a term sheet, or a covenant package in NDA clothing.

## The triage

Classify the NDA into one of three buckets by applying the positions from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. The bucket definitions below are stable; the *criteria* that fill each bucket come from the playbook.

### GREEN — route to signature

The NDA satisfies every position in the team's playbook, and no term triggers a RED flag per the playbook. Examples of checks the playbook typically covers: mutuality, term length, survival period, carveouts, governing law, restrictive covenants, fee-shifting. Confirm each one against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` before calling GREEN.

**GREEN requires attorney-reviewed playbook positions.** GREEN is the only path to signature without lawyer review. It cannot be issued against default or absent positions. Before issuing GREEN, check: does the practice profile have an attorney-reviewed `## NDA triage positions` section? If not:

> I can't issue GREEN without attorney-reviewed NDA positions in your practice profile. Run `/commercial-legal:cold-start-interview --full` with your commercial counsel to set them, or route this NDA for attorney review. Issuing GREEN against defaults means a non-lawyer set the positions the next non-lawyer relies on.

Do not route to signature on defaults. YELLOW is the right call when positions are missing — it surfaces the NDA to a human who can decide.

**Output:**

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

## NDA Triage: [Counterparty]

GREEN — route to signature

### Executive Summary

No red flags identified under the playbook. Route for signature per standard process.

| Check | Status | Playbook reference |
|---|---|---|
| [Each playbook check] | [pass/fail] | [`~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` section] |

**Next step:** [Submit to [CLM] standard NDA workflow | Send to [approver from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`] for signature]
```

**Before proceeding past GREEN to signature:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the Role is Non-lawyer:

> This step has legal consequences (countersigning an NDA binds the company). Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, NDA direction (mutual / one-way), the playbook checks run, anything the playbook didn't cover, what could go wrong if signed as-is, and the three things to ask the attorney.]
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service.

Do not proceed past this gate without an explicit yes.

### YELLOW — needs a lawyer's eyes on specific items

One or more terms deviate from the playbook but aren't categorical deal-breakers, OR a term appears that the playbook doesn't address. Surface each item individually so the approver can make the call.

**Output:**

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

## NDA Triage: [Counterparty]

YELLOW — flag for [approver name from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`]

### Executive Summary

- [One-line actionable edit, e.g. "Strike non-solicit clause (Section 6)"]
- [One-line actionable edit]

### Flagged items

**1. [Issue]** — Section [X]
   What: [one line]
   Why flagged: [one line — which playbook position this hits, or "playbook is silent on this"]
   **Legal risk:** [🔴/🟠/🟡/🟢] | **Business friction:** [🔴 Blocks deals / 🟠 Slows deals / 🟡 Confuses customers / 🟢 Invisible]
   Likely resolution: [accept / push back on X / depends on deal context]

[repeat for each flag]

### Everything else

| Check | Status | Playbook reference |
|---|---|---|
| [playbook checks that passed] | pass | [`~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` section] |

**Next step:** Ask [approver] about the flagged items, then route to signature if they're okay with it.
```

### RED — stop, talk to legal first

The NDA hits a position on the playbook's "never accept" list, or the structure of the agreement is incompatible with the team's standard posture (e.g., a one-way NDA where the team's playbook requires mutual; a perpetual term where the playbook caps at a finite period; governing law on the "never" list).

**Output:**

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

## NDA Triage: [Counterparty]

RED — do not submit, talk to legal first

### Executive Summary

- [One-line actionable edit, e.g. "Section 4 — route to Legal for review"]
- [One-line actionable edit]

### Critical issues

**1. [Issue]** — Section [X]
   > "[exact quote]"
   Why this is a problem: [specific risk; cite the playbook position it violates]
   **Legal risk:** [🔴/🟠/🟡/🟢] | **Business friction:** [🔴 Blocks deals / 🟠 Slows deals / 🟡 Confuses customers / 🟢 Invisible]
   Recommended response: [use our paper instead | push back with specific language | walk]

**Next step:** Send this triage to [GC or named escalation person from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`]. Do not send to [CLM or approvals workflow]. Do not tell the counterparty we'll sign.
```

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artifact, not a rewrite. Wholesale clause replacement signals "we threw out your drafting" — it's aggressive, it forces the counterparty to re-read the whole clause, and it discards the parts of their drafting that were fine. Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept.

Default to the smallest edit that achieves the playbook position:
- Replace a **word** before a phrase. ("twelve (12)" → "twenty-four (24)")
- Replace a **phrase** before a sentence. ("paid by the Buyer" → "paid and payable by the Buyer")
- Restructure a **subclause** before replacing the sentence. (Add "(a)" and "(b)" to split a compound condition.)
- Replace a **sentence** before replacing the clause.
- Only replace a **whole clause** when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and when you do, say so in the transmittal: "We've replaced §8.2 rather than marking it up because the changes were extensive. Happy to walk you through the delta."

When in doubt, smaller. A client who receives a surgical redline trusts that you read carefully. A client who receives a wholesale replacement wonders whether you read at all.

## Jurisdiction assumption

This triage applies the governing-law and restrictive-covenant positions recorded in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. Legal rules (enforceability of non-competes, non-solicits, fee-shifting, choice of law) vary materially by jurisdiction. If the NDA involves a jurisdiction outside the team's configured posture, flag it in the output and note that the triage may not transfer as written.

## Output rules

**Complexity filter:** If addressing an issue would require drafting new
language, restructuring a clause, or inserting substantive new
provisions — do not attempt it. Instead write:
"Section [X] — route to Legal for review."
Only include simple, mechanical actions in the Executive Summary
(strike, delete, replace a word or phrase).

**Clean NDA rule:** If the NDA passes all checks with no flags, the Executive Summary
should say only: "No red flags identified. Route for signature per
standard process."

Do not produce a lengthy report for a clean NDA.

## Detailed check reference

For each check below, the bucket (GREEN/YELLOW/RED) is determined by `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. This skill lists the *categories* to check; it does not hardcode thresholds.

### Mutuality

Is the NDA mutual or one-way? Apply the team's position from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the playbook doesn't address one-way NDAs for this context, run the one-way questionnaire below and surface the result for a human.

**One-way NDA questionnaire**

When the NDA is unilateral (one party discloses, the other only receives), do not immediately flag RED or exit. Ask:

> A one-way NDA is appropriate in some situations. Before flagging this,
> let me ask a few quick questions:
>
> 1. In this relationship, are you the only party disclosing confidential
>    information? (i.e., the other side shares nothing back)
> 2. Is this for a limited, specific disclosure — for example, sharing
>    your technology with a vendor who will work on it, but not sharing
>    theirs with you?
> 3. Is this related to M&A, employment, or investment? (If yes, stop —
>    this skill is for commercial MNDAs only. Route to Legal.)

Use the answers plus the `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` position to decide GREEN/YELLOW/RED. If `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` doesn't take a position on this fact pattern, flag YELLOW and surface the questionnaire answers for the approver.

### Definition of Confidential Information

Check scope (marked-only vs. everything-disclosed), marking requirements, and oral-disclosure confirmation windows. Apply the team's position from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the playbook is silent on any of these, ask.

### Carveouts

The five carveouts typically present in an NDA:

1. Information that is or becomes public (other than through breach)
2. Information the receiving party already had
3. Information independently developed without reference to the CI
4. Information received from a third party without restriction
5. Information required to be disclosed by law or court order (with notice to discloser where legally permitted)

Which carveouts the team requires, and how strictly, is a playbook question. Check `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` for the team's position on required carveouts, acceptable variations in wording, and what happens when one is missing.

### Residuals

A residuals clause lets the receiving party use information retained in unaided memory. Whether this is acceptable — and under what conditions (e.g., narrow "unaided memory" wording vs. broader scope covering notes or copies) — is a playbook question. Apply `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the playbook doesn't address residuals, ask.

### Term and survival

Check the initial term length, the post-term survival period for confidentiality obligations, and whether trade secrets are carved out with longer protection. Apply the team's position from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the playbook doesn't cover one of these, ask.

### Restrictive covenants

Check for non-solicits (employee, customer), non-competes, exclusivity, and any restriction on who else the receiving party can engage with. Apply `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the playbook is silent, ask — restrictive covenants are jurisdiction-sensitive and the team's posture matters.

### Attorneys' fees

Check for fee-shifting provisions and whether they are mutual, one-sided, or prevailing-party. Apply `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.

### Backup and archival carveout

Check whether the destruction/return clause includes an exception for standard backup and archival retention systems. Apply the team's position from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` — some teams require this carveout and will push to add it; others accept an NDA without it. If the playbook doesn't address this, ask.

### Governing law

Per `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` `## Playbook` → `Governing law and venue`.

## Counterparty context

**BigCo NDAs:** Fortune 500 counterparties generally won't negotiate NDAs. Calibrate: is the RED flag truly a deal-breaker, or is it "different from our form"? If the business relationship matters, the call is whether to accept their paper — escalate that decision, don't make it.

**Startup NDAs:** Will usually take our paper. If their NDA has issues, the fastest path is often "let's use ours" rather than redlining theirs.

## Integration: CLM

If connected:
- GREEN → offer to create the CLM record in the standard NDA workflow
- YELLOW → offer to create it with a note attached listing the flagged items
- RED → do not create a record; the lawyer decides what happens next

## What this skill does NOT do

- It does not negotiate. It sorts.
- It does not draft an NDA. If the answer is "use our paper," the user pulls our form from [CLM or document system].
- It does not make the call on YELLOW items. It surfaces them for a human.
- It does not state a position on any NDA term. Positions live in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.

## Closing action

Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## NDA triage preferences` → `closing_action`.

If configured, append the closing action verbatim at the end of every
output. Example configurations:

```
closing_action: "Send the full text of this analysis along with a copy
of the NDA to Legal at legal@[yourcompany].com for final confirmation before
signing."

closing_action: "Submit to [CLM] using the standard NDA workflow.
Legal will confirm before routing for signature."

closing_action: "Forward this output and the NDA to your contracts
manager."
```

If `closing_action` is not configured in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, append:
"Route final NDA through your standard approval process."

The cold-start interview asks: "When someone finishes an NDA
triage, what do you want them to do with the output? I'll add that as
a standing instruction at the end of every review."

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

---

## /commercial-legal:renewal-tracker

---
name: renewal-tracker
description: >
  Show contracts with cancel-by deadlines coming up and warn before notice windows
  close, working from a maintained renewal register. Use when the user asks "what's
  renewing soon", "what renewals are due", "did we miss a cancellation window", "add
  this to the renewal tracker", or on a scheduled basis. Receives handoffs from
  saas-msa-review.
argument-hint: "[--days N to change window | --missed for lapsed windows]"
---

# /renewal-tracker

Surfaces what's renewing and when you have to cancel by.

## Instructions

1. **Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-register.yaml`** (the config directory — survives plugin updates).

2. **Default mode:** Mode 2 — what's coming up in the next 90 days, grouped by urgency using half-open intervals so each deadline lands in exactly one band: 🔴 0–13 days, 🟠 14–44 days, 🟡 45–89 days. Days 14, 45, and 90 are boundaries — each belongs to exactly one band, not two.

3. **`--days N`:** Change the window.

4. **`--missed`:** Mode 4 — cancel-by deadlines that passed without recorded cancellation.

5. **If register is empty and the [CLM] is connected:** Offer Mode 3 — scan the [CLM] for active agreements with renewal dates and bulk-load.

6. **Output includes recommended actions:** who to ping (the business owner from each register entry), which ones have uncapped pricing (get leverage before window closes).

## Examples

```
/commercial-legal:renewal-tracker
```

```
/commercial-legal:renewal-tracker --days 180
```

```
/commercial-legal:renewal-tracker --missed
```

---

## Purpose

Nobody reads a contract twice. The renewal date is extracted once, at review time, and then it lives somewhere — ideally somewhere that shouts at you 45 days before the cancel-by deadline, not 45 days after.

This skill maintains the renewal register and surfaces what's coming.

## The register

Lives at `~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-register.yaml` (the config directory — survives plugin updates). Each entry:

```yaml
- counterparty: "Acme SaaS Inc."
  agreement: "Acme Platform Subscription Agreement"
  signed_date: 2025-06-15
  initial_term_end: 2026-06-15
  current_term_end: 2026-06-15     # rolls forward after each auto-renewal; compute cancel_by_* from this
  renewal_mechanism: "auto-renew annual"
  notice_period_days: 60
  notice_method: "email"           # email / portal / certified mail / registered post / courier / per contract §X
  transit_buffer_days: 0           # 0 for electronic, 5 for domestic certified mail, 10 for international registered post — or per contract if specified
  cancel_by_calendar: 2026-04-16    # current_term_end minus notice_period_days
  cancel_by_effective: 2026-04-16   # rolled back to last business day if needed
  send_by_effective: 2026-04-16    # cancel_by_effective minus transit_buffer_days — the date you must SEND the notice
  cancel_by_roll_note: ""           # e.g., "rolled back from Sunday 2026-11-01; verify against contract's business-day definition"
  cancel_by_provenance: "[model calculation — verify against the notice clause]"
  price_on_renewal: "then-current list (uncapped)"
  annual_value: 48000
  business_owner: "jane@company.com"
  clm_id:        "IC-12345"        # if connected
  docusign_envelope: "abc-123"   # if connected
  status: "active"               # active | cancelled | renewed | lapsed
  notes: "Pricing uncapped — revisit before renewal. Alt vendors: X, Y."
```

**Notice transit time — alert off `send_by_effective`, not `cancel_by_effective`.** A 60-day window with a certified-mail requirement is really ~55 days. The tracker that alerts on the received-by date is the tracker that misses the deadline. Compute `send_by_effective = cancel_by_effective - transit_buffer_days` and fire alerts (the 🔴 / 🟠 / 🟡 urgency bands in Mode 2) off `send_by_effective`. Mode 2's urgency column shows `send_by_effective`; a detail column surfaces `cancel_by_effective`, `notice_method`, and `transit_buffer_days` so the reader can see the delta and challenge the buffer.

**Rolling renewals — the register that doesn't roll forward is the register that's right once.** Store `initial_term_end` for the record, but compute `cancel_by_*` from `current_term_end`. When a renewal fires (the cancel window passes and no notice was given), prompt:

> This contract auto-renewed on [date]. Update the register: new `current_term_end` is [date + renewal period], new `cancel_by_effective` is [computed], new `send_by_effective` is [computed]. Confirm?

After year one, `initial_term_end` is wrong and only `current_term_end` produces a correct cancel-by date.

## Business-day check on every cancel-by date

**The register's cancel-by date must be the last BUSINESS DAY on which notice
is effective, not the calendar date.** A calendar date that falls on a
weekend is the single most common way a renewal deadline gets missed. The
register catches it.

When you compute (or ingest) a cancel-by date:

1. **Compute the calendar date.** `cancel_by_calendar = initial_term_end − notice_period_days` (or whatever the clause specifies). This is the raw arithmetic.
2. **Business-day roll-back keyed to governing law.** The contract's governing law determines which holidays count. US: federal holidays + the state's holidays if governing law is a state. England & Wales: bank holidays. Germany: Feiertage (vary by Bundesland — ask which). Canada: federal + provincial. Singapore: public holidays. If Saturday, roll back to Friday. If Sunday, roll back to Friday. If a holiday in the governing-law jurisdiction, roll back to the prior business day. Roll BACK, never forward — forward means notice arrives after the window closes. For non-US governing law, if you can't determine the holiday calendar, flag it: "Governing law is [X] — business-day roll-back uses US federal holidays as a placeholder. Verify against the [jurisdiction] holiday calendar before relying on the effective date."
3. **Check the contract's own day-counting rule.** Look for "business day," "received by," "deemed received," "5:00 p.m. [local time]," or a notice-method clause. If the contract defines "business day" or specifies receipt mechanics (certified mail, email with read receipt), that definition controls. Flag any mismatch between the default roll-back and the contract's own rule.
4. **Record BOTH dates in the register.** `cancel_by_calendar` is the raw arithmetic; `cancel_by_effective` is the last business day on which notice is effective; `cancel_by_roll_note` records why they differ (e.g., "rolled back from Sunday 2026-11-01; verify against contract's business-day definition"). Every computed `cancel_by_effective` carries a `cancel_by_provenance` tag of `[model calculation — verify against the notice clause]` so the verify flag travels with the date, not with the surrounding prose.
5. **Fire alerts off the EFFECTIVE date, not the calendar date.** Urgency bands (🔴 / 🟠 / 🟡 in Mode 2) use `cancel_by_effective`. Mode 2 output shows `cancel_by_effective` in the urgency column and surfaces `cancel_by_calendar` and `cancel_by_roll_note` in a detail column where the roll-back happened, so the reader can see it and challenge it.

A Mode 2 report that prints `cancel_by: 2026-11-01` (a Sunday) with no weekday and no warning is a silently wrong effective deadline. The register is the place to catch it — once, at ingest — not later, when the window has already moved.

## Modes

### Mode 1: Ingest a renewal (handoff from review)

When saas-msa-review or vendor-agreement-review finds a renewal clause, it hands off a record. Append it to the register. If the counterparty already has an entry, ask whether this is a replacement (renewed agreement) or an additional agreement.

### Mode 2: What's coming up

**Default lookback window:** next 90 days.

**Urgency bands are half-open intervals — a deadline lives in exactly one band.** Use days-until-cancel-by (`cancel_by_effective - today`). Day 14, 45, and 90 each belong to exactly one band, not two; an off-by-one here puts the most-urgent items into the less-urgent bucket.

- 🔴 **0–13 days** (cancel-by in less than 14 days — including today)
- 🟠 **14–44 days**
- 🟡 **45–89 days**
- (everything 90+ days is outside the default lookback window; include only if the user passed `--horizon` beyond 90)

```markdown
## Renewals — next 90 days

### 🔴 Cancel-by deadline in 0–13 days

| Counterparty | Cancel by | Renewal date | Annual $ | Owner | Notes |
|---|---|---|---|---|---|
| [name] | **[date]** | [date] | $[n] | [email] | [notes] |

### 🟠 Cancel-by deadline in 14–44 days

[same table]

### 🟡 Cancel-by deadline in 45–89 days

[same table]

---

**Recommended actions:**
- [ ] [Counterparty] — ping [business owner]: do we want to keep this?
- [ ] [Counterparty] — pricing is uncapped; get a quote from an alternative before we lose leverage
```

If the register has more than ~10 renewals in the window, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer for this output — counts by urgency tier (🔴 / 🟠 / 🟡), a cancel-by timeline, and a sortable register with counterparty, renewal date, annual $, and owner.

### Mode 3: Scan the [CLM] / e-signature tool to populate the register

If MCPs are connected and the register is empty or stale:

1. Query the [CLM] for all agreements with status "Active" and a renewal date field
2. Query DocuSign for completed envelopes in the last 24 months with "subscription" / "renewal" / "auto-renew" in metadata
3. For each hit, extract renewal mechanics and add to register
4. Flag any where the renewal date can't be determined from metadata — those need a human to read the contract

This is a one-time bulk load. After that, ingest happens at review time.

### Mode 4: Missed windows (the bad news report)

```markdown
## Missed cancellation windows

The following agreements had cancel-by deadlines that have passed and no
cancellation was recorded:

| Counterparty | Cancel-by was | Renewal date | Status |
|---|---|---|---|
| [name] | [date] | [date] | Will auto-renew on [date] |

**Options:**
- Negotiate late cancellation (rarely works but worth asking)
- Accept the renewal, mark next year's cancel-by now
- Check the agreement for any other termination rights (for convenience, for cause)
```

## Gate: accepting or declining a renewal

Tracking a renewal date is research. *Acting* on it — sending a notice of non-renewal, letting an auto-renewal fire, or countersigning a renewal form — is a consequential legal step.

**Before proceeding to accept or decline a renewal (including sending a non-renewal notice or letting an auto-renewal run past the cancel-by date):** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the Role is Non-lawyer:

> This step has legal consequences (you're either committing to another term or terminating the relationship). Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, current term end and cancel-by date, renewal price mechanism, what happens if we do nothing, alternative vendors if we want to shop, and the three things to ask the attorney before the window closes.]
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service.

Do not proceed past this gate without an explicit yes.

## Integration: renewal-watcher agent

The renewal-watcher agent in this plugin runs this skill on a schedule (weekly by default) and posts the "coming up" report to the channel named in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## House style` → where work product goes. Mode 2 is the agent's primary output.

## What this skill does not do

- It does not cancel contracts. It tells you when to decide.
- It does not decide whether to renew. It surfaces the deadline and the business owner.
- It does not read contracts to find renewal dates — that happens at review time. If a contract is in the register without a renewal date, it was added manually and someone needs to fill in the gap.

---

## /commercial-legal:review

---
name: review
description: >
  Review a vendor agreement, NDA, or SaaS subscription against your playbook.
  Identifies the agreement structure from titles, routes to the right review skill
  (vendor-agreement-review, nda-review, saas-msa-review), and integrates the output
  into a single memo. Use when the user says "review this contract", "check this
  MSA", "is this NDA okay", "look at this SaaS agreement", or attaches an inbound
  agreement for review.
argument-hint: '[file path | Drive link | [CLM ID] | paste text]'
---

# /review

Reviews an inbound agreement against the playbook in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. Identifies the agreement structure from titles, selects the appropriate skill(s), and — if confirm_routing is enabled — checks with the user before proceeding.

## Instructions

1. **Load `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.** If placeholders present, stop and prompt: "Run `/commercial-legal:cold-start-interview` first — I need to learn your playbook before I can review against it."

   Also read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## Review preferences` → `confirm_routing`. If the field is missing, treat it as `true`.

2. **Get the agreement:** From file path, Drive link, [CLM ID], or pasted text. If none provided, ask.

3. **Read the document structure — titles first.**

   Before reading the body, extract:
   - The main agreement title (e.g., "Master Services Agreement", "Non-Disclosure Agreement")
   - All exhibit, schedule, addendum, and attachment titles (e.g., "Exhibit A — Data Processing Addendum", "Schedule 1 — Subscription Order Form", "Annex B — Service Level Agreement")

   This is the routing signal. Do not rely on body keywords alone — a 40-page MSA with "confidential" throughout is not an NDA.

4. **Select the skill(s) based on document structure.**

   Map each identified document or section to a skill:

   | Document / section title contains | Skill |
   |---|---|
   | Non-Disclosure, NDA, Confidentiality Agreement (as the *main* agreement) | **nda-review** |
   | Master Services Agreement, Professional Services, Statement of Work, Consulting Agreement | **vendor-agreement-review** |
   | Subscription, SaaS, Cloud Services, Order Form with auto-renewal, Software License with recurring fees | **saas-msa-review** (overlay on vendor-agreement-review) |
   | Data Processing Addendum, DPA, Data Processing Agreement (as exhibit or standalone) | note for **vendor-agreement-review** → data protection section |
   | Service Level Agreement, SLA (as exhibit) | note for **saas-msa-review** → SLA section |

   Multiple skills may apply. Common combinations:
   - MSA + DPA exhibit → vendor-agreement-review, with DPA noted
   - SaaS subscription + Order Form + SLA exhibit → saas-msa-review (covers all three)
   - MSA + Order Form with auto-renewal → vendor-agreement-review + saas-msa-review overlay

   When the structure is genuinely ambiguous after reading titles (e.g., a document titled "Agreement" with no exhibits listed), read the first two pages of the body to resolve it — then stop and route.

5. **Confirm routing if enabled.**

   If `confirm_routing` is `true` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` (or field is absent):

   ```
   I'm going to review this as: [agreement type(s)].

   Documents identified:
   - [Main agreement title] → [skill]
   - [Exhibit A title] → [how it will be handled]
   - [Exhibit B title] → [how it will be handled]

   Sound right? (yes / no — or tell me what I got wrong)
   ```

   Wait for confirmation before proceeding. If the user corrects the routing, apply their instruction and proceed.

   If `confirm_routing` is `false`: proceed silently. Log the routing decision at the top of the review memo so the user can see what was applied.

6. **Run the skill(s).** Follow each skill's workflow fully. If multiple skills apply, run them in sequence and integrate the output into a single memo — don't produce separate memos.

7. **Check for escalations:** If any issue exceeds the reviewer's authority per the `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` matrix, invoke **escalation-flagger** to route and draft the ask.

8. **Offer follow-ups:**
   - Stakeholder summary for the business owner
   - Redline .docx with tracked changes
   - [CLM] record creation (if connected)
   - Add to renewal register (if auto-renewal found)
   - **Governing-law / jurisdiction deep-dive** — if the agreement's governing law is non-Turkish (English law, US/NY law) or the venue/arbitration clause is asymmetric, offer `/commercial-legal:governing-law-review` for a focused cross-border enforceability check using the UK/US legislation and CourtListener connectors (`references/karsilastirmali-hukuk-rehberi.md`).

## Configuring confirm_routing

Add to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## Review preferences`:

```markdown
## Review preferences

confirm_routing: true   # Set to false to skip routing confirmation and proceed automatically
```

The cold-start interview should ask about this preference. Default is `true` — confirmation on. As trust builds, the user can set it to `false`.

## Examples

```
/commercial-legal:review vendor-msa.pdf
```

```
/commercial-legal:review https://drive.google.com/file/d/ABC123
```

```
/commercial-legal:review
[paste agreement text]
```

## Output

Full review memo per the skill's format. Routing decision logged at the top. Deviation-by-deviation, specific redline language, named approver. Saved where `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → House style says work product goes.

---

## /commercial-legal:review-proposals

---
name: review-proposals
description: >
  Review and approve (or reject) pending playbook update proposals from the
  playbook-monitor agent and apply approved changes to the practice profile. Use
  when the playbook-monitor agent has surfaced proposals, when the user says
  "review playbook proposals", "what playbook updates are pending", or wants to
  step through deviation-driven playbook changes.
argument-hint: "[no arguments needed — works from the pending proposals file]"
---

# /review-proposals

Steps through pending playbook update proposals from the monitor agent and applies approved changes to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.

## Instructions

1. **Load the playbook-monitor agent** and run Step 5 (review and approval flow).

2. **If no proposals file exists** or it is empty: respond *"No pending proposals. Playbook is up to date."* Do not proceed further.

3. **Present proposals one at a time.** For each, show the full proposal block and offer four options: Accept, Reject, Edit, Defer.

4. **For Accept or Edit:** show the exact diff to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` before writing. Only apply after the attorney explicitly confirms.

5. **For Reject or Defer:** log the decision. Do not modify `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.

6. **After all proposals are resolved:** show a summary of what changed, then archive the proposals file.

## Examples

```
/commercial-legal:review-proposals
```

```
/commercial-legal:review-proposals
(runs automatically after playbook-monitor notifies you)
```

---

## /commercial-legal:saas-msa-review

---
name: saas-msa-review
description: >
  Reference: review of SaaS subscription agreements with attention to the terms
  that matter most in subscription deals — auto-renewal mechanics, price escalation,
  data portability, uptime SLAs, and subprocessor rights. Loaded by
  /commercial-legal:review when a SaaS or subscription agreement is detected.
user-invocable: false
---

# SaaS / Subscription Agreement Review

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

SaaS agreements have a distinct risk profile from one-time vendor contracts. The dollars compound over renewals, the data accumulates, and the switching cost grows every month. This skill reviews with that in mind.

It runs the standard playbook check from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` and adds a SaaS-specific overlay on the terms that bite hardest in subscription deals.

## Jurisdiction assumption

SaaS terms (auto-renewal notice requirements, price-escalation caps, data-portability mandates, subprocessor rules) are jurisdiction-sensitive — California, New York, and EU rules diverge materially, and some states have auto-renewal statutes that override private contract terms. This review applies the team's positions from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, which assume the governing law recorded there. If the agreement picks a different governing law, or the deal spans jurisdictions with statutory overrides (e.g., EU-based users, California consumers), flag it — the analysis may not transfer as written.

> **No silent supplement.** If a research query to the configured legal research tool (Westlaw, or firm platform) returns few or no results for a statutory override that might bear on the deal (auto-renewal statute, data-portability mandate, consumer-protection rule), report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [jurisdiction / rule]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Where the review cites a statute, regulation, or case (e.g., a state auto-renewal law overriding contract terms), tag the citation: `[Westlaw]`, `[statute / regulator site]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations from the counterparty draft or house files. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

## Load the playbook

**Which side?** Before applying the playbook, determine which side the company is on for this SaaS agreement. Usually obvious: if the counterparty is a SaaS vendor selling you their platform, you're purchasing-side. If you are the SaaS vendor and the counterparty is your customer, you're sales-side. If it's not obvious (a reseller arrangement, a white-label deal), ask: "Which side is [company] on for this agreement — vendor or customer?" Read the matching playbook section (`### Sales-side playbook` or `### Purchasing-side playbook`) from the config. Note which side in the output so the reviewer knows which playbook was applied. If the matching side is `[Not configured]`, stop and tell the user to run `/commercial-legal:cold-start-interview --side <side>` before this review can proceed.

Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` first. The general playbook for the matching side (liability, indemnity, termination, governing law) applies fully — run all the standard checks from the vendor-agreement-review skill.

Then look for a `## Playbook` → matching side → `SaaS positions` section. That's where the team records its positions on auto-renewal notice windows, acceptable price escalators, data export rights, SLA thresholds, subprocessor approval rights, and deprecation notice. This skill does not ship with defaults for these — the right numbers vary by deal size, vendor leverage, and the team's risk tolerance.

If `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` doesn't address a SaaS-specific term that comes up in this review, ask:

> Your playbook doesn't cover [term — e.g., "maximum acceptable auto-renewal notice window" or "whether vendor retention of anonymized derivatives is acceptable"]. What's your team's position? I'll add it to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.

Record the answer and proceed.

## SaaS-specific overlay

For each category below, list what you found in the contract and compare to the team's position in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. Do not apply hardcoded thresholds from this skill.

### 1. Auto-renewal mechanics

The single most common way a SaaS deal goes wrong: nobody notices the renewal notice window and we're locked in for another year at a higher price.

Check each element and compare against the team's `SaaS positions` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`:

- **Renewal term length** (e.g., same as initial, longer, multi-year auto-convert)
- **Notice-to-cancel window** (number of days before renewal)
- **Notice method** (email, written notice to legal, portal-only, certified mail)
- **Price on renewal** (same, CPI-capped, then-current list, uncapped discretionary)

**Extract and record** the exact renewal date and the notice window regardless of whether any item is flagged. This feeds the renewal-tracker skill.

### 2. Price escalation

Check each element against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`:

- **Annual escalator** (fixed %, CPI, uncapped, etc.)
- **Usage overage pricing** (published rate card, premium rate, unspecified)
- **Scope of "fees"** (subscription only vs. "additional services" broadly defined)

### 3. Data portability and exit

When (not if) we leave this vendor, can we get our data out? Check each element against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`:

- **Export format** (open/standard, proprietary-but-documented, "commercially reasonable")
- **Export availability** (self-serve anytime, on request during term, only at termination)
- **Post-termination access** (days available to export after termination)
- **Export cost** (free, T&M, per-GB or per-record)
- **Deletion certification** (certified on request, none, vendor retains derivatives)

Vendor retention of "anonymized" or "aggregated" derivatives is a material position — confirm the team's stance in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` and flag either way.

### 4. Uptime and SLA

Only matters if the business actually depends on this service being up. If it's a nice-to-have tool, skip this section — don't spend negotiating capital on SLAs for a survey tool.

Check each element against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`:

- **Uptime commitment** (percentage, or "commercially reasonable efforts")
- **Measurement period** (monthly, quarterly, annual)
- **Remedy** (service credits — how calculated, whether capped, whether sole remedy)
- **Scheduled maintenance exclusions** (defined window, advance notice, unlimited)
- **Credit-as-sole-remedy** interaction with the liability cap

### 5. Subprocessors

This is a data protection issue but it's SaaS-specific because the subprocessor list *changes* over the life of the subscription.

Check each element against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`:

- **Current list** (published, on request, unavailable)
- **Change notification** (advance notice period, or none)
- **Objection rights** (blocking, notice-and-terminate, notice-only, none)

### 6. Service changes and deprecation

SaaS vendors change their product. Usually fine. Sometimes they deprecate the thing you bought.

Check each element against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`:

- **Material adverse changes** (right to terminate on material degradation, notice-only, unrestricted)
- **Deprecation notice period** for features the team relies on
- **Feature parity on replacement** (same price tier, higher tier)



## AI and machine learning rights

**AI/ML data rights decision procedure.** Don't just check whether an AI training clause exists. The #1 emerging negotiation point in SaaS contracts is structurally more than a one-line existence check. Work through:

1. **Explicit grant.** Does the contract explicitly grant the vendor rights to use Customer Data / Customer Content / Usage Data for AI training, model improvement, or ML development? Purchasing-side: this is usually a NO — customer data training the vendor's models means the customer is subsidizing the vendor's product and possibly leaking competitive information. Sales-side: this is revenue if you get it, reputation risk if you abuse it.
2. **Implicit grant via policy.** Does the contract incorporate the vendor's privacy policy or terms of service by reference? Can the vendor add training rights via a unilateral policy update? Check: "The parties agree to the Provider's Privacy Policy as updated from time to time" is a training-rights grant waiting to happen. Also watch for "service improvement" or "analytics" catch-alls and "usage data" definitions that carve logs/telemetry out of the Customer Data definition so data-use restrictions don't apply.
3. **Anonymization standard.** If the vendor claims it only trains on "anonymized" or "aggregated" data, what's the standard? "Anonymized" without a definition is weak. Does it meet GDPR Recital 26 / HIPAA Safe Harbor / a named standard? Is it reversible?
4. **Competitive contamination.** Does the vendor serve your competitors? If so, training on your data could leak competitive intelligence into outputs your competitors see. Is there a competitive isolation commitment?
5. **Opt-out scope and durability.** If there's an opt-out, does it cover all AI uses or only some? Does it survive renewals and TOS updates? Is it per-user or per-org? Many vendors default to training and offer an opt-out buried in an admin console — check whether the contract makes the default explicit.
6. **Output ownership.** If the SaaS product is itself AI-generated (drafting, summarization, analysis), who owns the outputs? Can the vendor use your outputs as training examples? Check third-party AI subprocessors too — the vendor may send customer data to a third-party LLM (OpenAI, Anthropic, Google) and the subprocessor list / data flow is where that shows up.
7. **Downstream regulatory chain.** Does the vendor's use of your data for AI create regulatory exposure for YOU? EU AI Act deployer obligations, FTC §5 undisclosed data-sharing exposure (see *FTC v. Humor Rainbow/OkCupid*), state AI laws.

Match each to a playbook position. The practice profile's `## AI/ML training rights` section should have positions for each. If the agreement is silent on all seven, that's still a finding: "The agreement is silent on AI/ML training rights — request an explicit prohibition or a defined carve-out tied to each of the seven dimensions above."

## Liability cap decision procedure

**The cap amount is the least important part of the cap.** Limitation-of-liability is not a single "check against playbook" item. Work through:

1. **Direct vs. indirect/consequential damages.** Does the cap apply to ALL liability, or only direct damages? A 12-month cap on direct damages with uncapped consequential damages is a completely different position than a 12-month aggregate cap. State both treatments explicitly.

2. **The cap base — quote it verbatim.** "12-month cap" could mean: (a) fees paid in the 12 months preceding the claim, (b) fees payable in the current 12-month period, (c) fees over the last 12 months of usage, (d) fees under the current order form, (e) total fees ever paid. These can differ by an order of magnitude. Quote the exact language. If ambiguous, flag it: "Cap base is ambiguous — `[the quoted language]` — could mean [X] or [Y]. Confirm before signing."

3. **Cap-carveout interaction.** A $100K cap with uncapped indemnity for data breach, IP, and confidentiality is functionally uncapped for the claims that actually arise in SaaS disputes. Enumerate what sits ABOVE the cap (the carveouts), what sits BELOW (what's actually capped), and assess whether the capped surface is meaningful: "The cap covers [general contract breach]. Data breach, IP indemnity, and confidentiality are carved out and uncapped. For this vendor's risk profile, the capped surface is [meaningful / nominal]."

4. **Your playbook position per dimension.** The practice profile should have positions for: direct cap (multiple of fees), indirect damages (excluded / capped / uncapped), carveout list (what's acceptable above the cap), and cap base (which definition you'll accept). If the playbook has one "standard position" field, note: "Your playbook has a single cap position — consider splitting into direct/indirect/carveouts/base for more precise review."

## Jurisdiction delta check

**The playbook applies one governing-law preference globally. Enforceability varies materially.** Check the SaaS contract's actual governing law against the top divergences before accepting playbook positions at face value:

- **Non-solicits/non-competes:** Unenforceable in CA (Bus. & Prof. Code §16600). Restricted in many EU jurisdictions. Enforceable with limitations elsewhere. `[jurisdiction — verify]`
- **Auto-renewal:** CA GBL §17600-17606, NY GBL §527-a, IL 815 ILCS 601 have specific consumer/B2B notice requirements. Other states vary. `[jurisdiction — verify]`
- **Liability exclusions:** EU and UK unfair contract terms rules (UCTA 1977, Consumer Rights Act 2015) constrain consumer exclusions. Some US states limit exclusion of gross negligence or willful misconduct. `[jurisdiction — verify]`
- **Indemnification:** Some states void indemnification for the indemnitee's own negligence. `[jurisdiction — verify]`
- **Confidentiality term:** Some jurisdictions limit "perpetual" confidentiality to a reasonable period. `[jurisdiction — verify]`

When the playbook position conflicts with the contract's governing-law enforceability, flag: "Your playbook prefers [X], but this contract is governed by [Y] law where [X] is [unenforceable / restricted / subject to statutory override]. `[jurisdiction — verify]`"

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artifact, not a rewrite. Wholesale clause replacement signals "we threw out your drafting" — it's aggressive, it forces the counterparty to re-read the whole clause, and it discards the parts of their drafting that were fine. Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept.

Default to the smallest edit that achieves the playbook position:
- Replace a **word** before a phrase. ("twelve (12)" → "twenty-four (24)")
- Replace a **phrase** before a sentence. ("paid by the Buyer" → "paid and payable by the Buyer")
- Restructure a **subclause** before replacing the sentence. (Add "(a)" and "(b)" to split a compound condition.)
- Replace a **sentence** before replacing the clause.
- Only replace a **whole clause** when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and when you do, say so in the transmittal: "We've replaced §8.2 rather than marking it up because the changes were extensive. Happy to walk you through the delta."

When in doubt, smaller. A client who receives a surgical redline trusts that you read carefully. A client who receives a wholesale replacement wonders whether you read at all.

## Output

Use the vendor-agreement-review memo structure, with a SaaS-specific section added after the standard playbook checks. The vendor-agreement-review memo already carries the privilege header.

**Dual severity.** Every SaaS-specific finding carries both axes (see CLAUDE.md `## Dual severity`):
- **Legal risk:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low
- **Business friction:** 🔴 Blocks deals | 🟠 Slows deals | 🟡 Confuses customers | 🟢 Invisible

Data-exit, auto-renewal, and price-escalation findings are the ones most likely to be 🟢 legal / 🔴 business — the clause is enforceable, but it's the reason a customer can't leave or a renewal surprises finance. Surface those at the business-friction severity, not the legal one.

```markdown
### Bottom line

[Can you sign / Need to fight for X first / Walk — one-sentence why]

### AI and machine learning rights

[The #1 emerging SaaS negotiation point. Flag: explicit ML training clauses, "service improvement" catch-alls, usage data definitions, output ownership, third-party AI subprocessors, opt-out vs opt-in. If the agreement is silent: "Silent on AI/ML training rights — request explicit prohibition or defined carve-out."]

## SaaS-specific findings

### Auto-renewal
**Renewal date:** [date]
**Notice window:** Cancel by [date] ([N] days before renewal)
**Renewal price mechanism:** [as written]
**Playbook fit:** [within position / deviation / not addressed]
**Flag for renewal-tracker:** [yes — and the record the tracker needs]

### Price escalation
[findings against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` positions]

### Data exit
[findings — this is the one the business owner should read]

### SLA
[findings, or "Skipped — service is not business-critical per [stakeholder]"]

### Subprocessors
[findings against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` positions]

### Service changes
[findings against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` positions]
```

## Handoffs

**To renewal-tracker:** When you find the renewal date and notice window, hand them off. The renewal-tracker register expects the following fields (see `skills/renewal-tracker/references/renewal-register.yaml` for the full schema):

```yaml
counterparty:         [name]
agreement:            [title]
signed_date:          [ISO date]
initial_term_end:     [ISO date]
renewal_mechanism:    [e.g., "auto-renew annual"]
notice_period_days:   [integer]
cancel_by_effective:            [ISO date — initial_term_end minus notice_period_days]
price_on_renewal:     [mechanism as written]
annual_value:         [integer, if stated]
business_owner:       [email, if known]
clm_id:               [id if available]
status:               active
```

If any field is not determinable from the contract or context, leave it out and note which fields were missing so the human can fill them in. `clm_id`, `annual_value`, and `business_owner` are especially likely to need human input.

**To escalation-flagger:** If any of the SaaS-specific checks hits the team's "never accept" or escalation-trigger list in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, the escalation-flagger skill routes it.

## A note on what to fight over

SaaS vendors, especially large ones, negotiate their paper about as willingly as airlines negotiate ticket terms. Pick battles *per the team's playbook* — the `SaaS positions` section in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` should distinguish between terms the team will always push on, terms it fights over only for material deals, and terms it lets slide. If the playbook doesn't draw those lines, ask.

Calibrate based on contract value and switching cost. A $5K/year tool with easy alternatives gets a lighter touch than a $500K/year platform we'll build on top of.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

---

## /commercial-legal:stakeholder-summary

---
name: stakeholder-summary
description: >
  Translates a contract review into a summary the business stakeholder will
  actually read. Not a legal memo — a two-minute answer to "can I sign this
  and what do I need to know." Use when user says "summarize for the business",
  "write this up for [stakeholder]", "explain this to procurement", "non-legal
  summary", or when a review is done and needs to go to someone outside legal.
---

# Stakeholder Summary

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for work product) waive the protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitized version for the broader channel, or (c) both — don't silently apply a privileged header and then help paste it somewhere the header won't protect it. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

The business owner who asked for this contract doesn't want a legal memo. They want to know: can I sign it, what's the catch, and what do I need to do. This skill takes a completed review and turns it into that.

## Which side?

The underlying review memo was run against either the sales-side or the purchasing-side playbook. Carry that framing through. A purchasing-side summary tells the business owner "here's what we're getting and what we agreed to give up"; a sales-side summary tells them "here's what we're selling and what we're on the hook for." Check which side the review was run on (it should be noted at the top of the review memo) and match the voice. If it's not obvious from the memo, ask the lawyer before summarizing.

## Audience calibration

Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## House style` → who reads stakeholder summaries, how long should they be. If not specified, default to: procurement or a department head, two paragraphs max, no legal terms of art.

Different audiences need different summaries:

| Audience | Cares about | Doesn't care about |
|---|---|---|
| **Procurement** | Price, renewal mechanics, approval routing | Liability cap structure |
| **Department head (budget owner)** | Can their team use it, what happens if it breaks, cost | Indemnity scope |
| **Finance** | Total cost of ownership, renewal price risk, off-balance-sheet commitments | Governing law |
| **Security / IT** | Data handling, subprocessors, SOC 2, where data lives | Everything else |
| **Executive sponsor** | Is this going to embarrass us, is legal a blocker | Details |

Ask who this is for if it's not obvious from context.

## The summary

### Length cap — enforced

The summary is:
- **One paragraph** for the verdict and what this is (business terms, plain English)
- **One paragraph** for the catch — the thing the stakeholder would be surprised by later if nobody told them now
- **A 2-3 item checklist** for what the stakeholder actually needs to do (at most three items; if you want a fourth, the first three aren't tight enough)
- **A one-line close** with approval timing

**Under 200 words total.** If you're writing more, you're including detail the stakeholder doesn't need — they have the memo for that. This is the quick read before the stakeholder hits reply.

If the close needs a third paragraph, fold it into the checklist instead. Don't let the close grow into a fourth block.

### Scope of quote — discipline

When quoting a contract clause (in the summary, in the "catch" paragraph, or in the checklist), quote the **full conditional sentence**, not a truncated version. A clause that reads "Except as expressly provided in the Order Form, renewal of promotional or one-time priced subscriptions resets to list price" means something different from "renewal resets to list price" — the truncation drops the condition and misrepresents what the term does.

If a full conditional quote doesn't fit the summary's length cap, paraphrase rather than truncate. "For promotional pricing, renewal resets to list" is a fair paraphrase; "renewal resets to list" is not — it promotes the exception to the rule.

### Format

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]
<!-- Remove the header above if forwarding outside the legal-privileged circle (e.g., to a business stakeholder, counterparty, or vendor). Confirm the correct marking for your jurisdiction and matter before forwarding. -->

**[Counterparty] [Agreement type]** — [READY TO SIGN | NEEDS CHANGES | BLOCKED]

[One paragraph: what this agreement does, in business terms. Not "Master Services
Agreement for the provision of cloud-based analytics" — "this is the contract
for the dashboard tool the marketing team wants."]

[One paragraph: what the stakeholder needs to know. The catch, if there is one.
The thing that will surprise them later if nobody tells them now. E.g., "Heads
up: this auto-renews every year and we have to cancel 60 days out. I've added
it to the tracker but you should know." Or: "Clean agreement, no surprises,
cleared to sign."]

<!-- Do not claim "I've added it to the tracker" unless `renewal-tracker` has
actually been run for this contract — see Verify tracker entries before
asserting them below. -->

**Verify tracker entries before asserting them.** Before the summary says "I've added it to the tracker" (or any equivalent — "it's in the tracker," "tracked," "set a reminder"), verify that `renewal-tracker` has been run for this contract. Check the outputs folder or the matter folder for a `renewal-tracker` output that names this counterparty / agreement. If there isn't one:

- Either run `renewal-tracker` for this contract first, then write the summary.
- Or write the summary without asserting the tracker entry, and include an action item: "Add to renewal tracker — not yet done."

Claiming a tracker entry exists when it does not is worse than omitting the reassurance. The stakeholder then trusts the reminder that will never fire. If the truthful statement is "tracked," the skill runs the tracker. If it's "you should add this to your calendar — I haven't logged it," say that.

**What you need to do:**
- [ ] [Action item, if any — "confirm the team is okay with data living in EU"
  or "nothing — I'll route for signature"]

**Approval:** [who's approving and expected timing]
```

### What to translate

| Legal finding | Business translation |
|---|---|
| "Liability capped at 12 months fees" | "If they break something, the most we can recover is a year's worth of what we paid them." |
| "No termination for convenience" | "Once we sign, we're locked in for the full term — we can't just cancel if we stop using it." |
| "Auto-renewal with 60-day notice" | "This renews automatically every year. To cancel, we have to tell them two months before the renewal date." |
| "No IP indemnity" | "If someone sues us claiming this tool infringes their patent, the vendor isn't on the hook to defend us." |
| "Subprocessor list not disclosed" | "We don't know what other companies will have access to our data through them." |
| "Data deletion within 30 days of termination" | "When we cancel, they delete our data within a month. Export anything you need before then." |
| "SLA credits capped at 10% of monthly fee" | "If the service goes down, we get a small credit back. It won't cover the cost of the downtime to the business." |

### What NOT to include

- Section numbers
- Defined terms in quotes
- The word "indemnification" (say "they cover us if" / "we cover them if")
- The word "notwithstanding"
- Risk matrices with colored dots (unless this stakeholder has specifically asked for them before)
- Caveats about how this isn't legal advice — the stakeholder knows who sent it

## When the review found problems

If the review has 🔴 or 🟠 issues, the summary still needs to be two paragraphs — but the second paragraph is "here's what we're pushing back on and why."

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]
<!-- Remove the header above if forwarding outside the legal-privileged circle. -->

**[Counterparty] [Agreement type]** — NEEDS CHANGES

[What it is, one paragraph.]

We're going back to them on [N] things before this is ready. The main one:
[the critical issue in plain English — "they want the right to use our data
to improve their product, which means our competitors' instance gets smarter
from our data"]. We've asked them to strike it. [Realistic assessment: "They'll
probably agree" / "This might be a sticking point — will keep you posted."]

**What you need to do:**
- [ ] Nothing yet — I'll let you know when it's back from them.
  OR
- [ ] [Business decision they need to make: "If they won't budge on X, are you
  okay with Y, or do we walk?"]
```

## Handoffs

**From vendor-agreement-review / saas-msa-review:** Those skills produce the full memo. This skill reads the memo and compresses it. Don't re-review the contract — read the review.

**To the stakeholder:** Via whatever channel `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` says. If Slack, keep it under 150 words. If email, the format above is fine as-is.

## Escalation-fan-out reconciliation

The upstream review is a one-to-many producer: it can name five escalation targets (Deputy GC, CISO, Privacy Officer, CFO, business owner) across different findings. `escalation-flagger` routes one finding at a time. Without a reconciliation step, the Deputy GC sees the memo and the other four approvers never do.

Before producing the summary, read the upstream review memo and tally escalations:

1. **Count the escalation targets the review named.** Look for the routing / escalation block at the end of the review, or for per-finding "escalate to [X]" tags. De-dupe by approver name — a reviewer named for two findings counts once.
2. **Count the escalations actually routed.** Read the review folder (or matter folder) for `escalation-*.md` drafts produced by `escalation-flagger` since the review was written. Each draft names one approver.
3. **Reconcile.** If N approvers were named and M drafts exist, (N − M) escalations have not been routed.

Include a short reconciliation block in the summary — above the checklist, below the catch paragraph:

```markdown
**Escalation status:** [M] of [N] escalation targets routed. The following have not been routed and require action:
- [Approver name] — [one line on the finding that named them]
- [Approver name] — [one line]
```

If all N have been routed:
```markdown
**Escalation status:** [N] of [N] escalation targets routed.
```

If the upstream review surfaced no escalations, omit the block.

**Do not omit a named approver from the reconciliation because the stakeholder wouldn't recognize the name.** Business stakeholders often do not know who the Privacy Officer or CISO is. The reconciliation is internal-facing — it tells the lawyer sending the summary whether all the routing is done, not the stakeholder. If the stakeholder-facing summary needs to stay narrow, the reconciliation can live in a "routing status" footer or attached note — but it has to exist. A summary that implies routing is complete when it is not is worse than no summary.

**Word-count carve-out.** The escalation reconciliation block is exempt from the 200-word cap. Length-cap discipline on the summary body stays; the reconciliation is housekeeping, not narrative.

**When no escalation-flagger drafts exist.** If the upstream review named approvers and no drafts are in the folder, treat the count as M = 0. The reconciliation block lists all N as unrouted. That is the finding.

## A note on tone

Stakeholders remember two things about legal: did it block me, and did it make sense. This skill is how legal makes sense. Write like you're explaining it to a smart colleague over coffee, not like you're writing a memo to file.

If the honest summary is "this is fine, sign it," say that. Don't pad a clean review into three paragraphs to look thorough.

---

## /commercial-legal:vendor-agreement-review

---
name: vendor-agreement-review
description: >
  Reference: review of an inbound vendor agreement against the team playbook in
  `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. Flags deviations, assesses risk, generates
  specific redline language, and routes to the right approver. Loaded by
  /commercial-legal:review when a vendor MSA, services agreement, or similar is detected.
user-invocable: false
---

# Vendor Agreement Review

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for work product) waive the protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitized version for the broader channel, or (c) both — don't silently apply a privileged header and then help paste it somewhere the header won't protect it. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

Read a vendor agreement against the playbook this team actually uses (in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`), find every term that deviates, and tell the lawyer what to do about each one — with specific redline language, not vague "consider revising."

The output is a review memo the lawyer can act on in one pass. Every issue has a severity, a business-impact explanation, a proposed fix, and an escalation call if one is needed.

## Precondition: load the playbook

**Before reading the contract, read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.** If it's missing or still has placeholders, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor playbook positions, escalation, and house style to your practice.
>
> **Two choices:**
> - Run `/commercial-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll review tailored to YOUR playbook.
> - Say **"provisional"** and I'll review against generic defaults — US jurisdiction, middle risk appetite, lawyer role, no playbook (flag all common vendor-contract risks from first principles) — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," run the review normally using these generic defaults: middle risk appetite, lawyer role, US jurisdiction, no playbook (flag the common vendor-side risks from first principles — unlimited liability, no data-breach carveout, uncapped indemnity, auto-renewal without notice, etc. — rather than matching to configured positions). Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against default assumptions. Run `/commercial-legal:cold-start-interview` to get output calibrated to YOUR practice — your playbook, your jurisdiction, your risk appetite. 2 minutes."

**Which side?** Before applying the playbook, determine which side the company is on for this contract. Usually obvious: if the counterparty is a vendor/supplier providing goods or services, you're purchasing-side. If the counterparty is a customer buying your product/service, you're sales-side. If it's not obvious (a reseller agreement, a partnership, a revenue share), ask: "Which side is [company] on for this agreement — vendor or customer?" Read the matching playbook section (`### Sales-side playbook` or `### Purchasing-side playbook`) from the config. Note which side in the output so the reviewer knows which playbook was applied. If the matching side is `[Not configured]`, stop and tell the user to run `/commercial-legal:cold-start-interview --side <side>` before this review can proceed.

This skill is typically used for purchasing-side contracts (vendors supplying you), but the side check still applies — a "vendor agreement" could be your own template sent to a vendor as part of a reseller arrangement (sales-side).

The playbook in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` is the source of truth. It tells you:
- What this team's standard positions are (not market standard — *their* standard)
- What fallbacks they've accepted before
- What they never accept
- Who approves what
- The one deal-breaker to check first

If the contract has the deal-breaker, flag it at the top of the memo and stop the detailed review. There's no point spending 30 minutes on liability caps if the agreement gives the vendor rights to use customer data for training.

## Workflow

### Step 1: Orient

Read the whole agreement once, fast. Answer:

| Question | Answer |
|---|---|
| What kind of agreement is this? | MSA / SaaS subscription / Professional services / License / Other |
| Who are we? | Customer / Vendor (this plugin assumes customer — flag if not) |
| Counterparty | Name, and are they a BigCo (won't negotiate) or a startup (will)? |
| Dollar value | Annual / total contract value if stated |
| Term | Length, renewal mechanics |
| Is there a DPA? | Attached / referenced by URL / missing |
| Is there an order form? | Separate doc or integrated |

**Dollar-value handling.** If the main agreement does not state a dollar value (the MSA sets terms but the Order Form carries price, which is typical), **stop and ask** before running escalation math or applying dollar thresholds:

> The MSA itself doesn't state an annual contract value. The Order Form carries the price. Your escalation threshold is $[X from the matrix]. Before I route this, I need the ACV. Options:
> 1. Paste the Order Form value (preferred — I'll use it for routing and the memo).
> 2. Tell me if this is above or below $[threshold] and I'll route accordingly; the memo will flag that the routing assumed [above/below threshold] without an ACV in hand.
> 3. Route conservatively to the higher approver regardless — safer for a review you haven't priced.

Do NOT silently assume a value and then use the assumed value to drive routing. The assumption propagates into the approval call, which is a place the review shouldn't be guessing.

**DPA-by-reference handling.** If the main agreement incorporates a DPA "available at [URL]" or "as set forth at [URL]" or similar by reference, the DPA is part of the contract but is not in front of you. Note it explicitly in the Orient table and in the review memo:

> This agreement incorporates a DPA by URL reference at `[URL]`. The DPA carries the real data terms — subprocessor rights, breach-notification timing, data-return mechanics, standard contractual clauses, audit rights. Without reading it, the data-protection analysis below is partial. Offer to route the DPA to `/privacy-legal:dpa-review` (if installed) for a separate review, or fetch and read it inline before completing Step 3's data-protection analysis.

If the user is installed with `privacy-legal`, explicitly offer:

> Want me to hand the DPA URL to `/privacy-legal:dpa-review` once you're ready? That skill is built for the DPA work and will catch subprocessor / SCC / breach-notification issues that this skill only flags at the gate.

Do not silently proceed as if the DPA were absent when it is incorporated by reference. A missing DPA and an unread DPA are different gaps — label them differently.

### Step 2: Deal-breaker check

Check the "one thing" from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` first. If present:

```markdown
## ⛔ DEAL-BREAKER PRESENT

**Section [X.X]** contains [the deal-breaker]. Per the team playbook, this is a
hard no. Recommend:

- [ ] Push back — propose [specific alternative language]
- [ ] Walk — if counterparty won't move, we don't sign

Detailed review below is provided for completeness but is moot unless this is
resolved.
```

### Step 3: Term-by-term comparison

For each playbook category in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, find the corresponding contract section and compare.

**For each deviation, produce:**

```markdown
### [Section X.X]: [Issue name]

**Playbook says:** [our standard position, quoted from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`]

**Contract says:**
> "[exact quote from the contract]"

**Gap:** [Missing term | Weaker than standard | Weaker than fallback | Non-standard structure | Unacceptable]

**Legal risk:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low
**Business friction:** 🔴 Blocks deals | 🟠 Slows deals | 🟡 Confuses customers | 🟢 Invisible

**Why it matters:** [one or two sentences in plain English — what goes wrong
for the business if this term stays as-is]

**Proposed redline:**
> "[the specific replacement language — ready to paste into a markup]"

**If they won't move:** [the fallback from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, or "escalate to [person]"
if no fallback exists]
```

**Severity calibration:**

| Level | Means |
|---|---|
| 🔴 Critical | Don't sign without fixing. A term on the team's "never accept" list in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`, or a deal-breaker. |
| 🟠 High | Strongly push; escalate if they won't move. A term outside the playbook's stated fallback range. |
| 🟡 Medium | Push in first round; accept if it's the last open item. A term inside the fallback range but short of the standard position. |
| 🟢 Low | Note it, don't spend capital. A term the playbook explicitly tolerates, or a purely stylistic deviation. |

Severity is always applied *against `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`*. If a term doesn't map cleanly to a playbook position, ask the user which bucket it belongs in and offer to record the answer in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.

#### Liability cap decision procedure

**The cap amount is the least important part of the cap.** When reviewing the limitation-of-liability clause, do not produce a single "check liability cap against playbook" line item. Work through the four dimensions below and state each one explicitly in the finding:

1. **Direct vs. indirect/consequential damages.** Does the cap apply to ALL liability, or only direct damages? A 12-month cap on direct damages with uncapped consequential damages is a completely different position than a 12-month aggregate cap. State both treatments explicitly.

2. **The cap base — quote it verbatim.** "12-month cap" could mean: (a) fees paid in the 12 months preceding the claim, (b) fees payable in the current 12-month period, (c) fees over the last 12 months of usage, (d) fees under the current order form, (e) total fees ever paid. These can differ by an order of magnitude. Quote the exact language. If ambiguous, flag it: "Cap base is ambiguous — `[the quoted language]` — could mean [X] or [Y]. Confirm before signing."

3. **Cap-carveout interaction.** A $100K cap with uncapped indemnity for data breach, IP, and confidentiality is functionally uncapped for the claims that actually arise in SaaS disputes. Enumerate what sits ABOVE the cap (the carveouts), what sits BELOW (what's actually capped), and assess whether the capped surface is meaningful: "The cap covers [general contract breach]. Data breach, IP indemnity, and confidentiality are carved out and uncapped. For this vendor's risk profile, the capped surface is [meaningful / nominal]."

4. **Your playbook position per dimension.** The practice profile should have positions for: direct cap (multiple of fees), indirect damages (excluded / capped / uncapped), carveout list (what's acceptable above the cap), and cap base (which definition you'll accept). If the playbook has one "standard position" field, note: "Your playbook has a single cap position — consider splitting into direct/indirect/carveouts/base for more precise review."

#### Jurisdiction delta check

**The playbook applies one governing-law preference globally. Enforceability varies materially.** Check the contract's actual governing law against the top divergences before accepting playbook positions at face value:

- **Non-solicits/non-competes:** Unenforceable in CA (Bus. & Prof. Code §16600). Restricted in many EU jurisdictions. Enforceable with limitations elsewhere. `[jurisdiction — verify]`
- **Auto-renewal:** CA GBL §17600-17606, NY GBL §527-a, IL 815 ILCS 601 have specific consumer/B2B notice requirements. Other states vary. `[jurisdiction — verify]`
- **Liability exclusions:** EU and UK unfair contract terms rules (UCTA 1977, Consumer Rights Act 2015) constrain consumer exclusions. Some US states limit exclusion of gross negligence or willful misconduct. `[jurisdiction — verify]`
- **Indemnification:** Some states void indemnification for the indemnitee's own negligence. `[jurisdiction — verify]`
- **Confidentiality term:** Some jurisdictions limit "perpetual" confidentiality to a reasonable period. `[jurisdiction — verify]`

When the playbook position conflicts with the contract's governing-law enforceability, flag: "Your playbook prefers [X], but this contract is governed by [Y] law where [X] is [unenforceable / restricted / subject to statutory override]. `[jurisdiction — verify]`"

**Cross-border connector teyidi (v1.6.0).** Bir `[jurisdiction — verify]` etiketini boş bırakma — uygulanacak hukuk İngiliz veya ABD hukukuysa ilgili statüyü fiilen çek:
- **İngiliz hukuku** → `legislation.gov.uk` WebFetch (örn. UCTA 1977, Consumer Rights Act 2015, Arbitration Act 1996). Rehber: `references/uk-legislation-rehberi.md`. Atıf: `[UK Legislation — <tür yıl> s.<madde> — GG.AA.YYYY]`.
- **ABD federal hukuku** → GovInfo WebFetch / WebFetch. Rehber: `references/us-legislation-rehberi.md`. Atıf: `[US Legislation — GovInfo — <atıf> — GG.AA.YYYY]`.
- **ABD içtihatı** (örn. CA §16600 enforceability) → CourtListener REST + citation verification. Rehber: `references/courtlistener-rehberi.md`. Atıf: `[CourtListener — <mahkeme> — <citation> — GG.AA.YYYY]`.
- **ABD eyalet statüsü** (CA/NY/IL) connector kapsamında değil → web search + `[verify]`.

Türkiye'de icra ayağı varsa (yabancı mahkeme kararı tanıma-tenfiz veya yabancı hakem kararı), bunu da flag et — bkz. `references/karsilastirmali-hukuk-rehberi.md`. Çekemediğin yabancı hukuku `[model bilgisi — doğrulayın]` olarak bırak; connector etiketini yalnız fiilen çektiğinde kullan.

### Step 4: Favorable terms and gaps

Two short lists:

**Better than our standard:** Terms where the vendor gave us more than we'd ask for. Note these — they're trade bait if you need to give something up elsewhere.

**Missing entirely:** Standard provisions that just aren't there. Most common: assignment restrictions, audit rights (if we want them), force majeure, insurance requirements.

### Step 5: Escalation routing

Check the escalation matrix in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` against:
- Contract dollar value
- Presence of any 🔴 critical issues
- Any automatic-escalation triggers (unlimited liability, IP assignment, etc.)

State clearly who needs to approve this:

```markdown
## Approval routing

Based on [dollar value / issue severity], this agreement requires:

- [ ] **[Name/role]** approval — [reason]
- [ ] **Business owner sign-off** on [specific commercial term they should weigh in on]

**Recommended next step:** [Send redlines to counterparty | Escalate to GC before
responding | Get business input on commercial term X before legal responds]
```

**Before proceeding to send redlines to the counterparty:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the Role is Non-lawyer:

> Sending redlines is a legal act — the counterparty will treat every edit as our negotiating position. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, agreement type, the specific redlines proposed, the playbook positions behind each, the fallbacks, and what to ask the attorney before the package leaves.]
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service.

Do not proceed past this gate without an explicit yes.

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artifact, not a rewrite. Wholesale clause replacement signals "we threw out your drafting" — it's aggressive, it forces the counterparty to re-read the whole clause, and it discards the parts of their drafting that were fine. Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept.

Default to the smallest edit that achieves the playbook position:
- Replace a **word** before a phrase. ("twelve (12)" → "twenty-four (24)")
- Replace a **phrase** before a sentence. ("paid by the Buyer" → "paid and payable by the Buyer")
- Restructure a **subclause** before replacing the sentence. (Add "(a)" and "(b)" to split a compound condition.)
- Replace a **sentence** before replacing the clause.
- Only replace a **whole clause** when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and when you do, say so in the transmittal: "We've replaced §8.2 rather than marking it up because the changes were extensive. Happy to walk you through the delta."

When in doubt, smaller. A client who receives a surgical redline trusts that you read carefully. A client who receives a wholesale replacement wonders whether you read at all.

### Step 6: Assemble the memo

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

This memo and the underlying agreement may be privileged, confidential, or both. The output inherits that status from the source. Distribute only within the privilege circle; mark and store it where privileged materials live; strip the work-product header before any external delivery (e.g., counterparty redlines, stakeholder summaries).

The playbook positions applied below reflect the jurisdiction recorded in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `Governing law and venue`. Legal rules and enforceability vary materially by jurisdiction. If this deal implicates a different governing law or a choice-of-law question, flag it in the memo — the analysis may not transfer as written.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a rule the memo needs (enforceability of a limitation clause, indemnity scope, governing-law choice), report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule / jurisdiction]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Where the memo cites a statute, regulation, or case, tag the citation: `[Westlaw]`, `[statute / regulator site]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations from the counterparty draft or house files. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Vendor Agreement Review: [Counterparty] [Agreement Type]

**Reviewed:** [date]
**Contract value:** $[amount] / [term]
**Our role:** Customer

---

## Bottom line

[Two sentences. Can we sign this? What has to change first?]

**Issues (legal risk):** [N]🔴 [N]🟠 [N]🟡 [N]🟢
**Issues (business friction):** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Approval needed from:** [name]

---

## Deal-breaker check

[✅ Clear | ⛔ Present — see above]

---

## Issues by severity

[All the deviation blocks from Step 3, grouped Critical → Low]

---

## Favorable terms

[list]

## Missing provisions

[list]

---

## Approval routing

[from Step 5]

---

## Redline package

[If requested: consolidated markup-ready language for all proposed changes]
```

## Integration: [CLM]

If a [CLM] MCP is connected, after the review:

- Check if this counterparty already has agreements with us (may inform negotiating posture — "we already gave them 24-month cap on the last deal")
- Pull the workflow template that matches this agreement type
- Offer to create the [CLM] record with the review memo attached and approvers pre-routed

## Integration: DocuSign

If DocuSign MCP is connected and the agreement is ready to sign (all greens or all issues accepted), offer to:
- Generate the envelope
- Route to signers in the right order per the escalation matrix

Do **not** send anything for signature without explicit instruction. "Ready to sign" is the lawyer's call, not yours.

**Before generating a signature envelope or routing for countersignature:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the Role is Non-lawyer:

> This step has legal consequences (signing binds the company to the whole agreement). Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, contract value, the issues found and how they resolved, any risk the lawyer accepted, and what to ask the attorney before envelope goes out.]
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service.

Do not proceed past this gate without an explicit yes.

## Output formats

**Full memo (default):** As above. Goes in the [CLM] record or the Drive folder from `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` house-style section.

**Slack-sized summary:** Two lines and a link. For when someone asks "is this okay?" in a channel.

```
[Counterparty] [type] — NEEDS WORK. 1🔴 (uncapped liability §8.2), 2🟠. Full review: [link]. Needs [GC] approval.
```

**Redline doc:** If the user asks for it, output a .docx with tracked changes. Use the docx skill. Comments on each change cite the playbook position.

## Quality checks before delivering

- [ ] `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` was loaded and quoted — not generic market positions
- [ ] Deal-breaker checked first
- [ ] Every issue has specific replacement language
- [ ] Risk levels are calibrated (not everything is Critical)
- [ ] Approver is named, not "escalate to legal"
- [ ] Counterparty context considered (BigCo vs. startup — affects what's worth fighting over)

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

---

