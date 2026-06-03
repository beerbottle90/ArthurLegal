# employment-legal - Skill Referans Kitapcigi

> Alan: Is hukuku - ise iade, sorusturma, politika
> Toplam skill: 20
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /employment-legal:cold-start-interview (324 satir)
- /employment-legal:customize (104 satir)
- /employment-legal:expansion-kickoff (41 satir)
- /employment-legal:expansion-update (74 satir)
- /employment-legal:handbook-updates (107 satir)
- /employment-legal:hiring-review (213 satir)
- /employment-legal:internal-investigation (765 satir)
- /employment-legal:international-expansion (361 satir)
- /employment-legal:investigation-add (39 satir)
- /employment-legal:investigation-memo (36 satir)
- /employment-legal:investigation-open (36 satir)
- /employment-legal:investigation-query (44 satir)
- /employment-legal:investigation-summary (40 satir)
- /employment-legal:leave-tracker (36 satir)
- /employment-legal:log-leave (59 satir)
- /employment-legal:matter-workspace (187 satir)
- /employment-legal:policy-drafting (131 satir)
- /employment-legal:termination-review (283 satir)
- /employment-legal:wage-hour-qa (214 satir)
- /employment-legal:worker-classification (399 satir)

---

## /employment-legal:cold-start-interview

---
name: cold-start-interview
description: >
  Cold-start setup — learns your jurisdictional footprint and escalation rules
  from your handbook and termination memos. Asks which states and countries
  have employees, reads seed documents, and builds a jurisdiction-aware
  escalation table. Use on fresh install, when CLAUDE.md still has
  [PLACEHOLDER] markers, or when re-running with --redo or --check-integrations.
argument-hint: "[--redo | --check-integrations]"
---

# /cold-start-interview

1. Check `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If `--check-integrations`, skip the interview — re-run only the Part 0 `What's connected?` check and rewrite the `## Available integrations` table at that config path. When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone — that misleads users into thinking something is wired up when it isn't.
2. Run the interview below (Part 0 first — role + integrations — then footprint): states/countries, hiring/term review triggers, severance practice.
3. Seed docs: handbook + 3 termination memos.
4. Build jurisdiction-specific escalation table.
5. If a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/claude-for-legal/employment-legal/*/CLAUDE.md` but not at the config path, copy it to the config path and tell the user what was migrated.
6. Write `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`, creating parent directories as needed.

---

# Cold-Start Interview: Employment Counsel

## Purpose

Employment law is jurisdictional down to the bone. The right answer in Texas is the wrong answer in California. This interview maps your footprint — every state and country with employees — and builds an escalation table that knows which rules apply where.

## Cold-start check

Read `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed practice profile to the config path, creating parent directories as needed. If a CLAUDE.md exists at the old cache path `~/.claude/plugins/cache/claude-for-legal/employment-legal/*/CLAUDE.md` but not here, copy it forward.

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

Open with the fork-first preamble. Keep it to 3-4 short lines. Ask quick-or-full before anything else.

> **`employment-legal` is for people who handle hiring, terminations, investigations, leave, policies, worker classification, and international expansion.** Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutes** gets you your role, practice setting, and jurisdictional footprint (states + countries with employees), plus working defaults for termination risk flags, severance posture, and handbook policies. **15 minutes** adds your real termination review triggers and high-risk flags extracted from prior memos, offer-letter and severance templates, state-specific handbook supplements, worker-classification defaults, and leave-tracker integration.
>
> Quick or full? (Upgrade any time with `/cold-start-interview --full`.)

**Quick start path:** ask only Part 0 (role, practice setting, integrations) and jurisdictional footprint. Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for termination risk thresholds, severance posture, and handbook policies. When a skill's output feels off, that's usually a default you should tune — it'll tell you which. Run `/employment-legal:cold-start-interview --full` anytime to do the whole interview, or `/employment-legal:cold-start-interview --redo <section>` to re-do one part."

**Full setup path:** the existing interview flow below. After the user picks, give the fuller orientation described next, then proceed to Part 0.

## After the user picks quick or full

Give the fuller orientation. One paragraph, in your own voice:

> "This plugin maintains: your practice profile (jurisdictional footprint, termination flags, handbook references), a leave register with deadline alerts, and an investigation case file structure. It learns how you actually work — your practice, your risk calibration, your house conventions — and writes that into a plain-text file the plugin reads from every time. Everything you answer can be changed later."

Then the fresh-profile note:

> "Setup builds a fresh professional profile from your answers. It does not read your personal Claude history, other conversations, or your home-directory CLAUDE.md. If I notice relevant information in our conversation context — e.g., you mentioned your firm earlier — I'll ask before using it. Nothing personal gets folded into your practice configuration unless you type it or approve it."

Then: "Ready? A few quick questions first, then we'll go deeper."

**Why this matters** (offer if the user pushes back on the time cost). Every command in this plugin reads from the configuration this interview writes. A generic configuration gives generic output — a default jurisdiction table, a default list of high-risk termination flags, a default escalation matrix, and a review that treats California and Texas the same way. Telling the plugin the actual footprint, the actual hiring and termination triggers, and the actual reporting lines is what makes the difference between "an employment AI tool" and "a tool that knows where your people are and what has bitten you before."

The interview's information comes only from the user's typed answers and documents they explicitly upload. Do not read `~/CLAUDE.md`, personal notes, or any ambient context to fill in practice details. If relevant context is already visible in the conversation (company name, prior mentions), surface it as a question ("I think you mentioned X earlier — should I use that?") before using it.

## Interview pacing

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down somewhere — company description, playbook, escalation matrix, style guide, handbook, jurisdiction list, matter portfolio — prompt for a link or a paste before asking the user to type it from memory. "Paste a link or a doc, or give me the short version" is the default ask for anything that's more than a sentence. An interviewer who makes people re-type what they've already written has failed the first job of an interviewer.
- **Batch size — count subparts.** "Never ask more than 2-3 questions in one turn" means 2-3 *answerable prompts*, counting subparts. One question with 5 subparts is 5 questions. The test: can the user answer without scrolling? If the questions don't fit on one screen, it's too many. Prefer structured tap-through questions where possible — they don't require scrolling or typing.

**Pause for real answers.** Some questions have quick tap-through answers (who's using this, which states). Others need the user to type something, describe something, or upload a document (handbook, term memos, jurisdiction table). When a question needs more than a quick tap:

- **Ask the question and wait.** Say explicitly: "This one needs a typed answer — I'll wait." Do not move to the next question until the user responds.
- **For uploads:** "Paste the contents, share a file path, or say 'skip for now.' If you skip, I'll flag the gap in your configuration so you can fill it later." Then actually wait.
- **Before writing the configuration:** review the interview. List any questions that were skipped or answered with placeholders. Say: "Before I write your configuration, here's what's still open: [list]. Want to fill any of these now, or leave them as placeholders?" Then wait for the answer.
- **Never** write a configuration with silent gaps. Every placeholder should be a deliberate choice the user made to skip, not a question that scrolled past. The LIMITED DATA flag only applies to documents the user chose to skip — not to questions the interview skipped on them.
- **Pause and resume.** Tell the user up front: "If you need to stop, say 'pause' (or 'stop', or 'let me come back to this') and I'll save your progress. Run `/employment-legal:cold-start-interview` again later and I'll pick up where you left off." When the user pauses, write a partial configuration to `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` with a `<!-- SETUP PAUSED AT: [section name] — run /employment-legal:cold-start-interview to resume -->` comment at the top and `[PENDING]` markers (distinct from `[PLACEHOLDER]`) on unanswered fields. When setup re-runs and finds a paused config, greet the user: "Welcome back. You paused at [section]. Your earlier answers are saved. Pick up where we left off, or start over?" Do not re-ask questions already answered.

**Verify user-stated legal facts as they come up in setup.** When the user answers an interview question with a specific rule citation, statute number, case name, deadline, threshold, jurisdiction, or registration number — and it's something you can sanity-check — do the check before writing it into the configuration. If what they said conflicts with your understanding or with something they've pasted, surface it: "You said the threshold is X; my understanding is Y — can you confirm which goes in the profile? `[premise flagged — verify]`" A wrong fact written into CLAUDE.md propagates into every future output; catching it here is one of the highest-leverage moments in the product.

## The interview

### Opening

> Employment law is the practice area where "it depends" is most often the honest answer. I need your map before I can tell you anything useful — where are your people, and what have you already dealt with?

### Part 0: Who's using this, and what's connected

Three quick questions before we get into employment specifics. These shape how the plugin works, not what it can do.

#### Who's using this?

> Who'll be using this plugin day to day? (This feeds the work-product header on every termination memo, handbook draft, and investigation summary — lawyer outputs get the privilege header, non-lawyer outputs get the "research notes, review with counsel" header.)
>
> 1. **Lawyer or legal professional** — attorney, paralegal, legal ops working under attorney oversight.
> 2. **Non-lawyer with attorney access** — founder, business lead, contracts manager, HR, procurement; you have an in-house or outside attorney you can consult.
> 3. **Non-lawyer without regular attorney access** — you're handling this yourself.

If the answer is 2 or 3, say this once (don't repeat it on every output):

> You can use every feature here — research, review, drafting, tracking. Two things change in how I work:
>
> 1. **I'll frame outputs as research for attorney review, not as verdicts.** Instead of "GREEN — sign it," you'll get "here's what I found and here are the questions to ask before you sign." That's more useful than a green light you can't be sure of.
> 2. **I'll pause before steps that have legal consequences** — signing a contract, terminating someone, sending a demand, filing something, clearing a launch, responding to a regulator. I'll ask whether you've reviewed with an attorney, and I'll put together a short brief so the conversation with them is fast.
>
> This isn't a disclaimer. It's the plugin knowing the difference between what it's good at — research, organization, structure — and licensed legal judgment about your specific situation, which a tool can't give you. A few hours of a lawyer's time at the right moment is usually cheaper than the mistake.

If the answer is 3, add:

> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) — most offer a lawyer referral service as the fastest starting point. Many offer free or low-cost initial consultations. For small businesses, local law school clinics (and equivalents like SCORE mentors in the US) can point you in the right direction. For individuals, legal aid organizations cover many practice areas.

#### Practice setting

> Which of these best describes where you're practicing? (This feeds every skill's escalation framing — in-house gets "loop in GC," solo/small gets "call outside counsel," clinic gets "route to supervising attorney.")
>
> - **Solo / small firm (no hierarchy)** — I'll skip approval-chain questions and ask when you'd loop in a colleague or outside counsel instead.
> - **Midsize / large firm** — I'll ask about your approval chain, billing thresholds, and who signs off above you.
> - **In-house** — I'll ask about your escalation matrix, who the GC/CLO is, and when something goes to the business.
> - **Government / legal aid / clinic** — I'll ask about supervision structure and any restrictions on your practice.
> - **My practice doesn't fit any of these** — say so. I'll adapt.

**Practices that don't fit the boxes.** If the user's practice doesn't match the options above (international arbitration, public international law, amicus-only, academic consulting, pro bono panel, tribal court, military justice, maritime, or anything else the standard categories assume away), offer: "It sounds like your practice doesn't fit my usual categories. Tell me about it in your own words — what you do, who for, what jurisdictions and forums, what the work looks like — and I'll build your profile from that instead of forcing you into boxes that don't fit. I'll skip or adapt the questions that don't apply." Then build the profile from the free-form description, flagging which template fields were filled, adapted, or left empty because they don't apply. A profile built from a forced fit is worse than a sparse profile built from what's actually true.

This one changes how the rest of the interview runs:

- **Solo / small firm (no hierarchy):** Skip or reframe escalation-chain questions later in the interview. Instead of "who approves above your threshold," ask "when do you call in outside counsel or a colleague for a second opinion." Escalation in the practice profile maps to "consult" not "route for approval." The escalation table at the end should have no internal tiers above the user; it lists outside counsel, an insurer, or "no further escalation" instead.
- **Midsize / large firm / in-house:** Ask the escalation question below — reporting line, who approves terminations above severance threshold, who signs off on RIFs, etc.
- **Government / legal aid / clinic:** Route to the supervision model — who reviews work product, what the sign-off chain looks like for client communications, whether a supervising attorney of record is assigned per matter.

**Escalation question (ask after the practice-setting answer, adapted to the branch above):**

> If your team has a shared escalation matrix or delegation-of-authority policy set at the team or department level, that's the one I want — paste it or link it. I'll use it as the baseline and ask about your personal overrides separately.

> "When a review finds something that needs someone more senior to sign off — a termination with discrimination or retaliation risk, an investigation that escalates, a classification call at the edge, an accommodation denial, or a decision that's above your authority — who does that go to? Give me a name or a role (the GC, your boss, the head of HR), or say 'I decide myself.' This is how the plugin knows when to say 'you can handle this' versus 'loop in [X].' (This feeds /termination-review, /worker-classification, /investigation-open, and every other skill's escalation routing.)"

Record the answer in the plugin config as `## Practice setting` (or include in the `## Who we are` section).

#### What's connected?

> This plugin can work with: HRIS (Workday, BambooHR, Rippling, ADP), document storage (Google Drive, SharePoint, Box), and Slack. Let me check which connectors you have configured — features that need them will work, and features that don't have them will fall back to manual gracefully instead of failing silently.

**Check what's actually connected, not what's configured.** A connector listed in `.mcp.json` is *available*. A connector that's actually responding is *connected*. These are different, and confusing them destroys trust. For each connector this plugin uses:

- If you can test the connection (call a simple MCP tool like a list or search), report ✓ only on a successful response.
- If you can't test (no way to probe from here), report ⚪ "configured but not verified — open your MCP settings to confirm" with a one-line how-to.
- Never report ✓ based on configuration alone.

For connectors that show as not connected, tell the user how to connect. Example phrasing: "Box isn't connected. In Claude Cowork: Settings → Connectors → Add → Box → sign in. In Claude Code: add the Box MCP to your config or via `/mcp`. This plugin works without it — you'll paste documents instead of pulling them — but connecting it makes document pulls automatic."

Then report findings in this form:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.] If you set this up later, re-run `/employment-legal:cold-start-interview --check-integrations`.
>
> You don't need all of these. Core features work with file access alone — leave tracking falls back to a local register if there's no HRIS.

#### Write to the config CLAUDE.md

Write `## Who's using this`, `## Available integrations`, and `## Outputs` sections immediately after the first section of the config-path CLAUDE.md (the plugin config) per the template in `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`. These drive work-product header choice and feature-fallback behavior across every skill in this plugin.

### Part 1: The footprint (2-3 min)

> **What does [your company] do?** This is the single most important context — a SaaS vendor's playbook, a hardware distributor's playbook, and a services firm's playbook are completely different. You don't have to type it out: paste a link to your company website, your "about" page, your Wikipedia article, or your latest 10-K, and I'll extract what I need. Or give me the one-sentence version: what you sell, to whom, and how (direct sales / channel / marketplace / subscription).

> Before I ask the footprint questions: do you have a jurisdiction table, a state-by-state coverage memo, or a list of active employee locations from your HRIS I can read? Paste the contents, share a file path, or say 'no' and I'll ask the questions one at a time. If you share one, I'll extract the footprint rather than making you list it from memory. (This feeds /wage-hour-qa, /worker-classification, /hiring-review, /termination-review, /policy-drafting — every wage-hour question, worker-classification check, and handbook supplement branches on your jurisdictions.)

If not:

- Every US state with at least one employee. All of them.
- Every country outside the US.
- Remote-first or office-based? (Remote-first means the footprint keeps expanding without anyone telling you.)
- Which state has the most employees? That's your default jurisdiction when the question doesn't specify.

**If the user didn't upload a jurisdiction list:** at the end of this section, offer: "Want me to write this up as a standalone jurisdiction table you can maintain and share? Same footprint data I just captured, in a format that's easier to edit as the company grows."

### Part 2: The review triggers (2-3 min)

> "**Do you want to build your positions now?** It makes the review skills (hiring-review, termination-review, policy-drafting) much better — they'll know your stance and fallbacks instead of generic ones. It takes about 3-4 minutes. Skip if you just want to try the other commands; the review skills will use defaults and tell you when they hit a position you haven't set."

> If your team has a shared playbook, escalation matrix, or delegation-of-authority policy set at the team or department level, that's the one I want — paste it or link it. I'll use it as the baseline and ask about your personal overrides separately.

> Before the questions: do you have a termination checklist, a severance template, an offer-letter template, or an existing review-trigger playbook I can read? Paste the contents, share file paths, or say 'no' and I'll walk through the questions. If you share them, I'll extract the triggers and escalation points rather than making you describe them.

If not:

**Hiring:** When does legal see an offer?
- Every offer? Only exec? Only with restrictive covenants? Never?
- What's in the standard offer letter? Restrictive covenants vary by state — non-competes are unenforceable in California, fine in Florida.

**Termination:** When does legal see a termination?
- Every term? Performance only? RIFs only?
- What's the standard severance — formula, discretionary, none?
- Release required? Always, or only above X severance?

**The high-risk flags:** What makes a termination scary? (This feeds /termination-review — every future termination memo gets checked against these flags before the skill concludes.)
- Recent complaint (harassment, discrimination, whistleblower)
- Recently returned from protected leave
- Protected class + thin documentation
- Anything else that's bitten you before?

**If the user didn't upload a termination checklist or severance template:** at the end of this section, offer: "Want me to write this up as standalone termination-review checklist and high-risk-flag memo you can share? Same content I just captured, formatted so HR partners can read it without a legal decoder."

### Part 3: Seed documents (3-4 min)

**Where does leave data live?**

Before asking for documents, ask one infrastructure question:

> Do you have an HRIS — Workday, BambooHR, Rippling, ADP, or something else — that tracks employee leave? And does legal have read access to it? (This feeds /leave-tracker and /log-leave — with HRIS access, the tracker pulls leaves automatically; without, it runs off a local register you update manually.)

- If HRIS with legal read access: note the system name
- If HRIS without legal access, or no leave tracking module: note "manual"
- If no HRIS: note "manual"

**Seed documents**

> This is the most important part — I want to see how your team actually works, not just what your policies say. I need two things:
>
> 1. **Your handbook.** Current version. I'll read it to know what you've promised employees and where the gaps are. (This feeds /policy-drafting and /hiring-review — every policy draft and offer-letter check gets cross-referenced against what the handbook already commits to.)
>
> 2. **Recent employment documents — the more the better.** Ten is a good floor; twenty gives a much clearer picture. Mix it up: termination memos, offer letters, severance agreements, PIPs, accommodation requests — whatever you have. If you have fewer than ten, share what you can, but flag it. (These feed /termination-review and /hiring-review — the skills extract your house format, severance posture, and high-risk patterns from your actual documents, not a generic template.)

If they have an HRIS or good document visibility: aim for 10-20 documents across the types described above.

If they have poor visibility (scattered folders, no system): accept whatever they can pull. Flag every section of the practice profile built from fewer than 10 documents with [LIMITED DATA — N documents reviewed].

**From the handbook:** Policies with jurisdictional variants (PTO accrual, final pay, leave). State supplements if any. The gaps — things the handbook doesn't cover that it should.

**From the seed documents:** What got checked on terminations. What high-risk flags look like in practice. Offer letter format and standard restrictive covenant language. Severance agreement format for the termination-review skill to match. Any patterns in what the team actually approves vs. what the policies say.

## Build the jurisdiction table

This is the core output. For each state/country in the footprint:

| Jurisdiction | Special rules | Auto-escalate |
|---|---|---|
| California | No non-competes. Final pay due last day (or 72hrs if employee quits w/o notice). Meal/rest break penalties. PAGA exposure. | Any termination. Any restrictive covenant. |
| New York | Pay transparency in postings. NYC has separate rules. Final pay next regular payday. | Exec hires (pay transparency). |
| [etc.] | | |

Don't invent rules for jurisdictions they didn't name. If they have one employee in Montana and no memo ever mentioned Montana, note `[Montana: 1 employee, no history — research on first issue]`.

## Writing the practice profile

Per the template structure at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`. Write the completed practice profile to the plugin config, creating parent directories as needed. Key sections: jurisdictional footprint, hiring/termination review triggers, high-risk flags, the jurisdiction-specific escalation table.

## After writing

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list (not a generic template — these are the concrete things this plugin does best):

> **Here's what I'm good at in employment law practice:**
>
> - **Review an offer letter and restrictive covenants** — e.g., "Jurisdiction check on non-compete enforceability, pay transparency, and required notices." Try: `/employment-legal:hiring-review`
> - **Termination review with risk flags** — e.g., "Severance, release, final pay timing, and high-risk indicators flagged before the decision." Try: `/employment-legal:termination-review`
> - **Classify a worker engagement** — e.g., "Employee / IC / temp / vendor — with misclassification gap analysis." Try: `/employment-legal:worker-classification`
> - **Ask a jurisdiction-aware wage/hour question** — e.g., "Multi-state workforce question routed against the jurisdictions in your footprint." Try: `/employment-legal:wage-hour-qa`
> - **Kick off international expansion** — e.g., "New country on the roadmap — plan the employment-law workstream." Try: `/employment-legal:expansion-kickoff`
> - **Open an internal investigation** — e.g., "Create the privileged workspace, start the log, route interviews." Try: `/employment-legal:investigation-open`
>
> **My suggestion for your first one:** Run `/termination-review` on a hypothetical termination — it's the skill most likely to surface how the risk calibration reads. Or tell me what's on your plate and I'll pick.

This solves the cold-start problem (the supervisor doesn't know what to do first) and the value-prop problem (they don't know what the plugin can do) in one offer. Make the list specific. Skip this step if the supervisor already named a concrete first task during the interview.


- "Here's your jurisdiction table. The California row is the one to double-check."
- "What's the next termination? Let me take a look."
- Flag handbook gaps: "Your handbook doesn't have a remote work policy and you're remote-first. Want one?"
- Check HRIS field: "You said your HRIS is [system] — want me to run the leave tracker now to see if anything is open?"
- If manual leave tracking: "You don't have an HRIS leave module — I'll track leaves in a register file. Use /employment-legal:log-leave to add any leaves that are currently open."

**Before your first review**: connect a research tool. Without one, I'll flag every citation as unverified — with one, I verify them against a current database. In Cowork: Settings → Connectors. In Claude Code: authorize when a skill prompts you.

<!-- COLLATERAL LINKS: when onboarding collateral exists, add here:
     "Want a walkthrough? [Watch the 3-minute intro](URL) or [read the getting-started guide](URL)." -->


### Close with the "you can change anything later" note

After writing the configuration, say:

> "Done. Your configuration is at `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` — a plain text file you can read and edit directly. Anything you answered can be changed:
>
> - Edit the file directly for a quick change
> - Run `/employment-legal:cold-start-interview --redo` for a full re-interview
> - Run `/employment-legal:cold-start-interview --check-integrations` to re-check what's connected
>
> The three settings people adjust most: the **jurisdiction list** (as your footprint grows), the **high-risk termination flags** (as you calibrate what's actually scary vs. what's noise), and the **escalation matrix** (as reporting lines shift)."

## Your practice profile learns

After writing the configuration, close with this note:

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - You can always say "update my playbook to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.
> - Run `/employment-legal:cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.
>
> Ten minutes of setup gets you a working profile. A month of use gets you one that reads like you wrote it yourself.

---

## /employment-legal:customize

---
name: customize
description: >
  Guided customization of your employment practice profile — change one thing
  without re-running the whole cold-start interview. Adjust jurisdictional
  footprint, risk posture, escalation contacts, hiring review rules,
  termination review rules, handbook positions, investigation preferences,
  or matter workspace paths. Use when the user says "change my [thing]",
  "add a jurisdiction", "update my profile", "edit my config", or "customize".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/employment-legal:customize`. They want to change something
in their practice profile — a jurisdiction, a risk posture, an escalation
contact, a handbook position — without re-running the whole cold-start
interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`
   (and `~/.claude/plugins/config/claude-for-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/employment-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, practice setting, jurisdictions
     *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Jurisdictional footprint** — states (and countries) where employees
     work, single-state vs. multi-state, and any upcoming expansion. This
     drives state-specific supplement logic.
   - **Risk posture** — conservative / middle / aggressive, what each means
     for flagging termination risk, restrictive covenant enforceability, and
     leave accommodation
   - **People** — HR partners, people team lead, outside counsel, escalation
     chain, investigation sponsor
   - **Hiring review** — offer letter template, restrictive covenants
     posture, background check vendor, standard at-will language
   - **Termination review** — severance framework, release language, final
     pay timing rules per state, high-risk flags
   - **Handbook** — handbook file path, state supplements approach, review
     cadence
   - **Investigation preferences** — privileged labeling, interview protocol,
     audience-specific summary templates
   - **Workflow** — matter workspaces, leave tracker cadence, expansion
     project paths
   - **Integrations** — HRIS / Slack / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding Washington to the jurisdictional footprint:* "`/wage-hour-qa`
     and `/termination-review` will start applying WA rules. `/handbook-
     updates` will prompt for a WA supplement. `/hiring-review` will now
     flag non-compete attempts in WA (unenforceable)."
   - *Severance framework 2 weeks/year → 4 weeks/year:* "`/termination-
     review` will use the new baseline in severance calculations."
   - *Risk posture middle → conservative:* "I'll flag more terminations for
     escalation, recommend more protective release language, and be stricter
     on restrictive covenants."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/employment-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" a jurisdiction,
  offer to mark it `[Not currently staffed — retain rules for re-entry]` and
  explain that going to `[Not configured]` will drop state-specific
  flagging.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., CA in the footprint + aggressive non-compete posture;
  or risk posture aggressive + "every termination goes to outside counsel"),
  flag the tension.
- **Flag guardrail degradation.** The pre-flight citation check, source
  attribution tags, and `[verify]` tags on cited statutes are load-bearing —
  do not remove. The `[review]` flag is load-bearing — explain the trade-off
  before adjusting.
- **One change at a time.** Don't re-ask the whole interview.

---

## /employment-legal:expansion-kickoff

---
name: expansion-kickoff
description: >
  Kick off international expansion planning for a new country — gathers intake,
  runs EOR vs. entity framing, drafts cross-functional questions, surfaces
  country-specific flags, and creates a persistent tracker. Use when someone
  says "we're hiring in [country]", "expansion to [country]", or "first hire
  in [country]".
argument-hint: "[country name]"
---

# /expansion-kickoff

Starts an international expansion project for a new country — gathers intake,
runs EOR vs. entity framing, drafts cross-functional questions, surfaces
country-specific flags, and creates a persistent tracker.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, escalation table.
2. Load the `international-expansion` reference skill and run the full workflow.
3. If a tracker file already exists for this country (`~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-[slug].yaml`),
   flag it: "An expansion tracker for [country] already exists. Use
   `/employment-legal:expansion-update [country]` to update it, or confirm
   you want to start over."
4. Create `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-[slug].yaml` on completion.

## Examples

```
/employment-legal:expansion-kickoff Germany
```

```
/employment-legal:expansion-kickoff
(skill will ask which country)
```

> Detailed EOR vs. entity framework, cross-functional questions, briefing
> templates, and tracker schema live in the `international-expansion`
> reference skill — load it before doing substantive work.

---

## /employment-legal:expansion-update

---
name: expansion-update
description: >
  Update the status of an in-progress international expansion project —
  recalculates what is now unblocked, flags anything overdue, and surfaces
  the next priorities. Use when work has happened since the last session and
  the expansion tracker needs to reflect the current state.
argument-hint: "[country name]"
---

# /expansion-update

Returns to an open expansion tracker and updates item status based on what
has happened since the last session. Recalculates what is now unblocked,
flags anything overdue, and surfaces the next priorities.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`.

2. Identify the tracker file: `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-[slug].yaml`. If it doesn't
   exist, respond: "No expansion tracker found for [country]. Run
   `/employment-legal:expansion-kickoff [country]` to start one."

3. Read the tracker. Show the current state:

```
[Country] Expansion — last updated [date]
Open: [N] | In progress: [N] | Done: [N] | Blocked: [N]

Next priorities (open items with earliest due dates or highest-dependency):
  [item] — owner: [owner]
  [item] — owner: [owner]
  [item] — owner: [owner]
```

4. Ask for updates in a single prompt — do not ask about each item one by one:

   > Which items have moved since we last looked? Tell me what's changed
   > (e.g., "EOR decision made — going with Deel", "outside counsel engaged —
   > call scheduled for Thursday", "PE analysis still open, waiting on tax").
   > You can also add new items or change due dates.

5. Apply updates to the tracker file. For any item newly marked `done`,
   check whether it unblocks other items and flag those as now actionable.

6. If any item has a due date that has passed and is still `open` or
   `in-progress`, flag it:

```
⚠️ Overdue: [item] — was due [date], owner: [owner]
```

7. Write the updated tracker. Confirm:

```
Tracker updated — [N] items closed, [N] still open.
Next priority: [top open item].
```

## Examples

```
/employment-legal:expansion-update Germany
```

```
/employment-legal:expansion-update
(will ask which country if multiple trackers exist)
```

> Detailed tracker schema, item-status rules, and dependency logic live in the
> `international-expansion` reference skill — load it before doing substantive
> work.

---

## /employment-legal:handbook-updates

---
name: handbook-updates
description: >
  Diff a proposed handbook change against the current version, flag ripple
  effects and state supplement impacts. Use when user says "update the
  handbook", "add this to the handbook", "handbook change", or has a policy
  ready for insertion.
---

# Handbook Updates

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Handbook changes have ripple effects. Change the PTO policy and you've affected the final pay calculation, the leave policy cross-reference, and three state supplements. This skill finds the ripples before they become inconsistencies.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → handbook location, state supplements list, update cadence.

## Workflow

### Step 1: Get the change

- What section is changing?
- What's the new language?
- Why? (Legal requirement, policy decision, cleanup)

### Step 2: Diff against current

Read the current handbook section. Show the diff:

```diff
- [old language]
+ [new language]
```

### Step 3: Find cross-references

Search the handbook for references to the changed section:

- Other policies that cite this one ("see the PTO policy for accrual rates")
- Defined terms that this section uses or defines
- State supplements that modify this section

Each cross-reference: does it still make sense after the change? Flag any that break.

### Step 4: State supplement impact

For each state supplement in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`:

- Does this supplement modify the section being changed?
- Does the change make the supplement obsolete, wrong, or incomplete?
- Does the change create a need for a *new* supplement in a state that didn't need one before?

### Step 5: Promise check

Is the change reducing something the old version promised?

If yes: that's a risk. Some states treat handbook policies as contractual. Reducing a benefit may need more than just updating the document — advance notice, consideration, or in some cases it can't be done retroactively.

Flag this. Don't block it — but flag it.

## Output

```markdown
## Handbook Update: [Section name]

### Change

[diff]

### Cross-reference impact

| Section | References changed section | Still accurate? | Fix needed |
|---|---|---|---|
| [name] | [how] | ✅/⚠️ | [what] |

### State supplement impact

| State | Current supplement | After change | Action |
|---|---|---|---|
| [state] | [what it says] | [still valid / obsolete / needs update] | [none / update / new supplement needed] |

### Promise check

[If reducing a benefit: flag + jurisdictional risk note]

### Ready to publish

- [ ] Cross-references updated
- [ ] State supplements updated
- [ ] [If benefit reduction: notice/consideration addressed]
- [ ] Version number and date updated
- [ ] Acknowledgment process (if required)
```

## What this skill does not do

- Approve handbook changes. HR/legal leadership does.
- Communicate changes to employees.
- Track acknowledgments.

---

## /employment-legal:hiring-review

---
name: hiring-review
description: >
  Review an offer letter and any restrictive covenants — jurisdiction check
  included. Substantive rules (covenant enforceability, pay-transparency,
  salary-history limits, exemption criteria) are researched per hire, not
  stored. Use when the user says "review this offer", "can we use a
  non-compete here", "check this offer letter", "hiring in [state]", or
  attaches an offer.
argument-hint: "[offer letter file, or describe the hire]"
---

# /hiring-review

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, hiring review triggers, restrictive covenant policy.
2. Use the workflow below.
3. Check: jurisdiction, classification, restrictive covenants, background check compliance.
4. Flag anything that hits the jurisdiction-specific escalation table.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Offer letters are mostly boilerplate until they're not. The jurisdiction check
and the restrictive-covenant check are where this skill earns its keep. The
skill does not state the law — every jurisdiction-specific rule is researched
and cited at the time of review.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, hiring review triggers, restrictive
covenant policy, offer letter template location.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`).

## Workflow

### Step 1: Jurisdiction

Where will this person work? Not where HQ is — where *they* are.

If remote: their home state/country governs. If hybrid: usually their home
state, but check the offer letter's choice-of-law clause (may or may not hold
up).

Check the jurisdiction table in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` for this state/country. If it's
not in the table — new jurisdiction — flag that: "First hire in [state]. The
jurisdiction table doesn't cover this. Research needed before offer goes out."

### Step 2: Classification

Exempt or non-exempt? The offer should say, and the role should support it.

| Test | Check |
|---|---|
| Salary basis | Paid a fixed salary regardless of hours? |
| Salary level | Above the applicable federal and state thresholds? |
| Duties test | Does the role actually involve the exempt duties? |

> **Research before calling exemption.** Identify the currently operative
> salary thresholds (federal and state — several states index annually and
> several have tiered thresholds by employer size) and the applicable duties
> test(s) for the role. Cite primary sources. Verify currency.

If the offer says exempt but the role description does not support the
exempt duties — flag it. Misclassification is expensive.

### Step 3: Restrictive covenants

If the offer includes a non-compete, customer non-solicit, employee
non-solicit, or confidentiality/IP assignment:

> **Research enforceability before advising.** For the employee's jurisdiction,
> identify the currently operative rules on each restrictive covenant in the
> offer. Non-compete enforceability in particular has shifted in multiple
> states in recent years through legislation, agency action, and litigation —
> do not rely on prior memory of which states permit non-competes. Note:
> - The specific type of covenant (non-compete, customer non-solicit, employee
>   non-solicit, confidentiality/trade-secret, IP assignment) — each has its
>   own rules.
> - Any salary or income threshold that conditions enforceability.
> - Any notice, consideration, or garden-leave requirements.
> - Any industry-specific carve-outs (e.g., healthcare, broadcasting).
> - Duration and geographic-scope reasonableness tests.
> - Choice-of-law and choice-of-forum enforceability for out-of-state covenants.
> Cite primary sources. Verify currency.

Per `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` restrictive covenant policy: does this hire even get one?
Some companies use them selectively. Apply the house policy first, then
research overlays from the jurisdiction.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for the jurisdiction's exemption thresholds, restrictive-covenant rules, pay-transparency law, or any other item you're researching, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [jurisdiction / topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Tag every citation in the review with where it came from: `[Westlaw]`, `[CourtListener]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the user supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

### Step 4: Jurisdiction-specific requirements

Check the `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` table for this jurisdiction. Common categories to
research for each hire:

- **Pay transparency** — does the jurisdiction require a salary range in the
  posting? If so, is this offer within the posted range? Research the current
  rule (including any recent amendments or new enforcement guidance).
- **Ban-the-box** — does the jurisdiction or locality restrict the timing or
  scope of criminal-history inquiries?
- **Salary-history limits** — is the jurisdiction one that restricts asking
  about or relying on prior salary? Research current rules and recent
  amendments.
- **Required offer-letter or onboarding notices** — some jurisdictions require
  specific notices at offer or hire (wage-notice statutes, sick-leave notices,
  etc.). Research what is currently required and whether a template exists.

Cite primary sources. Verify currency.

### Step 5: Offer letter content

Read the letter. Check:

**Employment-at-will is US-only.** "At-will" means either party can terminate without cause or notice (subject to statutory exceptions). This concept does not exist outside the US:

- **US (most states):** At-will is the default. Offer letters often include "at-will" language to defeat implied-contract arguments. Check that it's present if US.
- **Montana:** Not at-will — Wrongful Discharge from Employment Act requires cause after probation.
- **UK:** No at-will. Employees have statutory protections from day 1 (unfair dismissal after 2 years of service, automatic unfair dismissal for protected reasons from day 1). The offer letter must contain the written statement of particulars (ERA 1996 s.1): pay, hours, notice period, holidays, pension, disciplinary/grievance procedures.
- **EU:** No at-will. Termination requires cause, notice, and often works council consultation or collective redundancy procedures. The offer letter requirements vary by member state but notice periods and written particulars are standard.
- **Australia:** No at-will. Fair Work Act minimum notice periods, unfair dismissal protections, NES.
- **Canada:** No at-will. Common law reasonable notice (can be months), ESA minimums, wrongful dismissal exposure.
- **Singapore, other APAC:** No at-will. Employment Act and contract-based protections.

**Check for at-will language ONLY if the jurisdiction is US.** For non-US jurisdictions, check instead for: notice period (and whether it meets statutory minimum), the written-statement particulars the jurisdiction requires, probation period terms, and any jurisdiction-specific mandatory clauses.

**Never recommend adding at-will language to a non-US offer letter.** It's legally meaningless, it can conflict with mandatory statutory terms, and it signals to the employee's lawyer that the employer didn't understand the jurisdiction.

- At-will language present and not undermined elsewhere (US only — see above)
- Contingencies clear (background check, reference, I-9 if US / right-to-work verification for the applicable jurisdiction)
- Start date, title, salary, reporting structure stated
- Equity terms (if any) consistent with the plan
- Integration clause so the letter is the whole deal
- For non-US: notice period meets statutory minimum, jurisdiction's required written-statement particulars included, probation period compliant with local rules

## Output

> **Jurisdiction assumption.** This review applies the rules of the employee's work jurisdiction identified in Step 1. Enforceability of restrictive covenants, exemption thresholds, pay-transparency obligations, salary-history limits, and required notices vary materially by state and locality, and several have shifted recently. If the candidate's work location changes, or the role spans jurisdictions, this review may not apply as written.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Hiring Review: [Candidate] — [Role] — [Jurisdiction]

**Overall:** [Clear to send | Changes needed | Escalate]

### Jurisdiction: [State/Country]
[Jurisdiction table entry. Any auto-escalate triggers that fire.]

### Classification
[Exempt/non-exempt call, grounded in researched thresholds and duties test.
Any flags.]

### Restrictive covenants
[If any. Enforceability call per researched jurisdiction rules, with pinpoint
cites and currency note. Suggested changes.]

### Jurisdiction-specific requirements
[Pay transparency, notices, salary-history rules, etc. — each researched and
cited, or flagged as needing research.]

### Offer letter
[Any issues with the letter itself]

### Action items
- [ ] [specific change needed before sending]
```

## Consequential-action gate (make an offer)

**Before producing a "Clear to send" recommendation or a final offer letter for signature:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Making an offer has legal consequences — the letter is a contract, and restrictive covenants, classification, and jurisdiction-specific terms are difficult to reset once sent. Have you reviewed this offer with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - Candidate, role, jurisdiction (where they'll actually work)
> - Classification call (exempt/non-exempt) and why
> - Restrictive covenants in the offer and the enforceability analysis
> - Jurisdiction-specific requirements that apply (pay transparency, wage notices, salary-history rules)
> - Open questions and what's unresolved
> - What could go wrong (misclassification liability, unenforceable non-compete, missing required notice, conflicting at-will language)
> - What to ask the attorney (is this the right form for this jurisdiction; can we use our standard non-compete here; what notices need to go with the letter)
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service.

Do not produce a "Clear to send" output past this gate without an explicit yes. A marked-DRAFT flagged for attorney review is fine.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- Draft the offer letter — reviews it.
- Make the hire decision — checks the paperwork.
- State restrictive-covenant or exemption rules from memory — every
  jurisdiction-specific call is based on researched, cited sources verified
  for currency.
- Research a new jurisdiction in depth on its own — flags that research is
  needed, and uses `wage-hour-qa` or outside counsel to fill in.

---

## /employment-legal:internal-investigation

---
name: internal-investigation
description: >
  Reference: shared framework for managing internal investigations from intake
  through final memo — privileged investigation log, document processing with
  needle-finding, source coverage tracking, Q&A against the log, memo drafting,
  and audience summaries. Loaded by /investigation-open, /investigation-add,
  /investigation-query, /investigation-memo, and /investigation-summary; not
  invoked directly.
user-invocable: false
---

# Internal Investigation Skill

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Output header

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`). Every file, log, memo, and summary produced by this skill opens with that header.

> **Distribution discipline.** Every file this skill creates — log entries, memo drafts, audience summaries, document notes — inherits the privilege and confidentiality status of the underlying investigation. Distribution beyond the privilege circle (forwarding to non-attorneys outside the investigation team, cc'ing HR without scoping, handing to the business side) can waive privilege over the entire investigation. Store these files where privileged materials live, label per the work-product header, and make every distribution decision deliberately.

## ⚠️ Privilege notice — read before proceeding

**Marking does not create privilege.** The header above reflects the intended
protection and is important to include — but it does not itself establish
privilege. Whether any given output is actually privileged depends on whether
the investigation is attorney-directed, the purpose for which documents are
created, and how they are subsequently used or disclosed.

**Before opening a matter, confirm:** Is this investigation attorney-directed?
If it is not — if HR is running it with legal in an advisory role, or if it was
not initiated at the direction of counsel for the purpose of obtaining legal advice —
the privilege analysis changes materially and this skill's default labeling may
be misleading. Flag that question to the attorney before creating any log or file.

If there is any doubt about privilege applicability, the attorney should resolve it
before investigation files are created. Improperly labeled materials can create
problems in discovery if privilege is later challenged.

---

## Purpose

Internal investigations fail in two ways: coverage gaps (sources that were
never gathered) and synthesis gaps (evidence that was gathered but never
connected). This skill handles both — it tracks what has and hasn't been
gathered, processes document dumps to surface what matters without burying
the attorney, and maintains a structured log that can be turned into a
privileged memo at any point.

## Privilege note

All files created by this skill carry the privilege marking above.
See the notice at the top of this skill for the full caveat on what that
marking does and does not do.

## Load context

Read `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → escalation table, any investigation protocols noted.

---

## Mode 1: Open a new matter

Triggered by `/employment-legal:investigation-open` or "open an investigation"
or "start an investigation into".

### Step 1 — Intake

Ask the following in a single block:

> To open the investigation log I need a few things:
>
> **The matter**
> - What is the allegation or concern in plain terms?
> - Who is the complainant (or what triggered this — complaint, tip, audit,
>   manager observation)?
> - Who is the respondent or subject?
> - What is the approximate timeframe the alleged conduct occurred?
> - Is this attorney-directed? (If yes: work product protection applies.
>   If no: flag privilege risk before proceeding.)
>
> **Investigation type** (helps me suggest the right sources checklist)
> - HR: harassment / discrimination / retaliation
> - Financial misconduct: expense fraud / procurement irregularities / embezzlement
> - Executive misconduct: COI / undisclosed relationships / governance failures
> - Whistleblower: retaliation for protected activity
> - Other: describe briefly
>
> **Representation and employer status** (surfaces parallel legal frameworks
> that change interview procedure)
> - Is the respondent, the complainant, or any anticipated witness represented
>   by a union or covered by a collective bargaining agreement? (If yes, flag
>   for Weingarten research — representational rights at investigatory
>   interviews may apply and change the interview protocol.)
> - Is the company a public employer (government entity, public university,
>   state or municipal agency) or otherwise acting under color of state law?
>   (If yes, flag for Garrity research — compelled statements in public-sector
>   investigations have special use-immunity consequences and change how
>   interviews must be conducted and documented.)

If either flag fires, research the applicable rules (NLRA / state
public-sector labor statutes for Weingarten; 5th Amendment and the Garrity
line of cases, plus any state analogs) before conducting interviews. Cite
primary sources. Verify currency. Do not interview until the protocol is
adjusted.

### Step 2 — Create the matter directory and files

Create the following files:

`~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/log.yaml`:

```yaml
# [WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]
matter: "[matter name]"
matter_slug: "[slug]"
opened: "[ISO date]"
attorney_directed: [true/false]
allegation: "[plain-language summary]"
complainant: "[name/role or anonymous]"
respondent: "[name/role]"
conduct_timeframe: "[approximate dates]"
investigation_type: "[HR/financial/executive/whistleblower/other]"
status: open
last_updated: "[ISO date]"

issues:
  - "[Issue 1 — derived from allegation, e.g. 'alleged hostile work environment']"
  - "[Issue 2 if applicable]"

entries: []

evidentiary_gaps: []
```

`~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/sources-checklist.yaml`:

Generated from the investigation type. See sources checklist templates below.

`~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[matter-slug]/documents-reviewed.yaml`:

```yaml
# [WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]
matter: "[matter name]"
total_reviewed: 0
total_surfaced: 0
last_updated: "[ISO date]"
documents: []
```

### Step 3 — Sources checklist

Generate the appropriate checklist based on investigation type. Present it
to the attorney and ask: "Does this fit your matter? Let me know if any items
are not applicable (I'll mark them N/A) or if there are additional sources
specific to this situation."

**HR investigation sources (harassment/discrimination/retaliation):**
```yaml
sources:
  - id: 1
    source: "Complainant interview"
    status: open
    notes: ""
  - id: 2
    source: "Respondent interview"
    status: open
    notes: ""
  - id: 3
    source: "Witness interviews — identify from complainant and respondent accounts"
    status: open
    notes: ""
  - id: 4
    source: "Email/messaging review — parties, relevant date range"
    status: open
    notes: ""
  - id: 5
    source: "HR records — respondent's performance history, prior complaints,
             prior discipline"
    status: open
    notes: ""
  - id: 6
    source: "Prior complaints — any prior complaints against respondent in
             HR system"
    status: open
    notes: ""
  - id: 7
    source: "Comparator data — how were similar situations handled"
    status: open
    notes: ""
  - id: 8
    source: "Relevant policies — harassment, code of conduct, reporting
             procedures (version in effect at time of alleged conduct)"
    status: open
    notes: ""
  - id: 9
    source: "Org chart and reporting relationships at time of alleged conduct"
    status: open
    notes: ""
  - id: 10
    source: "Calendar records — any meetings or events mentioned in accounts"
    status: open
    notes: ""
  - id: 11
    source: "Upjohn warning documentation — confirm interviews were preceded
             by Upjohn warnings and documented"
    status: open
    notes: ""
```

**Financial misconduct sources:**
```yaml
sources:
  - id: 1
    source: "Expense reports — subject, relevant period"
    status: open
    notes: ""
  - id: 2
    source: "Approval records — who approved the expenses or transactions"
    status: open
    notes: ""
  - id: 3
    source: "Vendor/contractor records — contracts, invoices, payment records"
    status: open
    notes: ""
  - id: 4
    source: "Financial system records — AP, GL entries for relevant accounts"
    status: open
    notes: ""
  - id: 5
    source: "Email/messaging review — subject, approvers, counterparties"
    status: open
    notes: ""
  - id: 6
    source: "Subject interview"
    status: open
    notes: ""
  - id: 7
    source: "Approver interviews"
    status: open
    notes: ""
  - id: 8
    source: "Counterparty/vendor interviews (if accessible)"
    status: open
    notes: ""
  - id: 9
    source: "Audit logs — system access logs for relevant accounts/systems"
    status: open
    notes: ""
  - id: 10
    source: "Prior audits or reviews covering the relevant period"
    status: open
    notes: ""
  - id: 11
    source: "Upjohn warning documentation"
    status: open
    notes: ""
```

**Executive misconduct sources:**
```yaml
sources:
  - id: 1
    source: "Subject interview"
    status: open
    notes: ""
  - id: 2
    source: "Board/compensation committee records — relevant resolutions,
             minutes, approvals"
    status: open
    notes: ""
  - id: 3
    source: "Employment agreement and any amendments"
    status: open
    notes: ""
  - id: 4
    source: "Equity records — grants, exercises, vesting"
    status: open
    notes: ""
  - id: 5
    source: "Expense reports and approval records"
    status: open
    notes: ""
  - id: 6
    source: "Email/messaging review — subject, relevant counterparties"
    status: open
    notes: ""
  - id: 7
    source: "Conflict of interest disclosures (or absence thereof)"
    status: open
    notes: ""
  - id: 8
    source: "Outside business activity records"
    status: open
    notes: ""
  - id: 9
    source: "Witness interviews — direct reports, peers, board members"
    status: open
    notes: ""
  - id: 10
    source: "Prior complaints or concerns raised about subject"
    status: open
    notes: ""
  - id: 11
    source: "Upjohn warning documentation"
    status: open
    notes: ""
```

**Whistleblower sources:**
```yaml
sources:
  - id: 1
    source: "Complainant interview"
    status: open
    notes: ""
  - id: 2
    source: "Original complaint or tip — written form if exists"
    status: open
    notes: ""
  - id: 3
    source: "Records related to the underlying allegation (the thing
             complainant blew the whistle on)"
    status: open
    notes: ""
  - id: 4
    source: "Records related to any adverse action taken against complainant
             after the protected activity"
    status: open
    notes: ""
  - id: 5
    source: "Decision-maker interviews — who made the adverse action decision"
    status: open
    notes: ""
  - id: 6
    source: "Comparator data — treatment of similarly situated employees
             who did not engage in protected activity"
    status: open
    notes: ""
  - id: 7
    source: "Email/messaging review — decision-makers, relevant timeframe"
    status: open
    notes: ""
  - id: 8
    source: "Timing analysis — proximity of protected activity to adverse
             action"
    status: open
    notes: ""
  - id: 9
    source: "Respondent/decision-maker interviews"
    status: open
    notes: ""
  - id: 10
    source: "Upjohn warning documentation"
    status: open
    notes: ""
```

After presenting the checklist, write it to
`~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[slug]/sources-checklist.yaml`.

---

## Mode 2: Add data

Triggered by `/employment-legal:investigation-add` or "add to the [matter]
investigation" or when the attorney pastes documents or interview notes.

### Step 1 — Identify the matter

If multiple investigation folders exist in `~/.claude/plugins/config/claude-for-legal/employment-legal/`, ask which matter this
data belongs to. If only one, proceed.

### Step 2 — Identify the data type

Ask (if not clear from context):
- Interview notes (whose interview?)
- Document batch (emails, records, files)
- Attorney notes or observations
- Upjohn warning confirmation

### Step 3 — Document pull criteria

For any document batch, apply the following pull criteria. A document is
surfaced if it meets ANY of the following. The criteria are intentionally
set to pull slightly aggressively — it is better to surface a false positive
than to miss a significant item.

**Pull criteria:**
1. Contains the name of any party to the investigation (complainant,
   respondent, witnesses named in prior log entries)
2. Was authored or received by a party during the key conduct timeframe
3. Contains keywords related to the allegation type (identified at intake
   and from prior log entries — update the keyword list as new terms emerge
   from accounts)
4. Contains explicit or implicit admissions ("I shouldn't have," "I know
   how this looks," "don't put this in writing," "delete this")
5. Contains language contradicting any account already in the log — flag
   the specific contradiction and the log entry it conflicts with
6. Contains language that would be sensitive in litigation: discriminatory
   terms, threats, discussions of protected characteristics or activities,
   financial irregularities matching the allegation pattern
7. Is a document type that has been mentioned in prior accounts but has
   not yet appeared in the document set (e.g., a meeting was mentioned in
   an interview but no calendar invite has been reviewed) → log as
   evidentiary gap, not a surfaced document

**Disposition for every document reviewed:**
- `surfaced`: meets one or more pull criteria — added to log as a log entry
- `reviewed-nothing-significant`: reviewed, does not meet pull criteria —
  logged in documents-reviewed.yaml with one-line description only

**After processing a document batch, report:**

```
Document review complete.
Reviewed: [N] documents
Surfaced: [N] as potentially significant
Logged as reviewed / nothing significant: [N]
New evidentiary gaps identified: [N]

Surfaced items:
[list with one-line description and which pull criterion triggered]
```

This report is the answer to "what about missed needles." The pull criteria
are documented, the surface ratio is visible, and the attorney can review
the full document log at any time. In Q&A mode, "I have not seen any document
on [topic] in the [N] documents reviewed" is a meaningful statement only
because every document reviewed is logged.

### Step 4 — Write log entries

For each surfaced item, append to `log.yaml`:

```yaml
- entry_id: [auto-increment]
  entry_type: [interview / document / attorney-note / gap]
  date_of_event: "[date the event occurred — not when logged]"
  date_logged: "[ISO datetime]"
  source: "[witness name/role, or document filename/description]"
  source_type: [complainant / respondent / witness / document / attorney-note]
  issues: ["[which investigation issue(s) this entry relates to]"]
  significance: [high / medium / background]
  summary: "[what this entry adds to the record — 2-5 sentences]"
  quote: "[verbatim quote if significant — otherwise empty]"
  contradicts_entry: [entry_id or null]
  corroborates_entry: [entry_id or null]
  credibility_note: ""
  pull_criterion: "[which criterion triggered — for documents]"
  privilege: attorney-work-product
```

For evidentiary gaps:

```yaml
- gap_id: [auto-increment]
  description: "[what document/source should exist but hasn't been found]"
  identified_from: "[which log entry or account raised this]"
  source_to_obtain: "[where to get it]"
  priority: [high / medium / low]
  status: open
```

### Step 5 — Update sources checklist

If the data added corresponds to a checklist item, ask the attorney if it
should be marked complete or in-progress. Do not auto-mark complete —
the attorney decides when a source is adequately covered.

---

## Mode 3: Query the log

Triggered by `/employment-legal:investigation-query` or any question
phrased against the investigation (e.g., "what did [witness] say about",
"what documents corroborate", "what do we still need", "what's the
strongest evidence on each side").

Read the full log before answering. Answer types:

**Factual query** ("what did X say about Y"):
Answer from the log entries, citing entry IDs. If the log contains nothing
on the topic: "I have not seen any information on [topic] in this
investigation log ([N] entries reviewed). This may be worth flagging as
a gap."

**Conflict query** ("where do accounts conflict"):
Surface all contradicts_entry links. For each conflict: state what the
conflict is, which entries are in tension, and what (if any) documentary
evidence bears on the conflict.

**Coverage query** ("what do we still need" / "what are our gaps"):
Read sources-checklist.yaml and evidentiary_gaps in log.yaml. Report:
- Checklist items still open
- Evidentiary gaps logged
- Any accounts that reference sources not yet gathered

**Strength query** ("what's the strongest evidence on each issue"):
For each issue in the log, identify: the highest-significance log entries,
any documentary corroboration, and any unresolved conflicts. Present
issue by issue.

**Upjohn query** ("have we documented Upjohn warnings"):
Check checklist item and any log entries tagged as Upjohn documentation.
Flag if not yet completed.

---

## Mode 4: Draft or update the memo

Triggered by `/employment-legal:investigation-memo` or "draft the memo"
or "update the memo".

### If no memo exists — first draft

Read the full log. Do not draft until the following are complete (warn if
not):
- At least one entry for each open issue
- Complainant and respondent entries present
- Sources checklist reviewed (flag any high-priority open items)

Draft the memo in the following structure, following standard internal
investigation memorandum practice:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

---

**MEMORANDUM**

To: [Attorney to fill in]
From: [Attorney to fill in]
Date: [Date]
Re: Internal Investigation — [Matter name]
Status: PRELIMINARY DRAFT

---

## Executive Summary

[2-3 paragraphs: allegation in plain terms, investigation scope and
methodology summary, key findings in bullet form (Sustained / Not
Sustained / Inconclusive), recommended actions. Written last but
appears first.]

---

## Background and Scope

**Triggering event:** [What initiated the investigation]

**Allegations investigated:**
[Each issue from the log as a numbered allegation]

**Out of scope:** [Anything explicitly not investigated and why]

**Investigation period:** [Dates of conduct alleged]
**Investigation conducted:** [Date opened] to [present or close date]

---

## Methodology

**Interviews conducted:**
| Witness | Role | Date | Notes |
|---|---|---|---|
[Populated from log entries with source_type = interview]

**Documents reviewed:**
[Summary of document categories reviewed, volume, date range.
Full document log is maintained separately.]

**Other sources:**
[Any other sources from checklist — policies, HR records, etc.]

**Limitations:** [Any sources requested but not obtained, any constraints]

---

## Factual Findings

*[Organized by issue — one section per allegation. Not by witness,
not purely chronological.]*

### Issue 1: [Allegation]

[Narrative of what the evidence shows on this issue. Cite log entry IDs
inline in brackets. Where accounts conflict, present the conflict directly
— do not smooth it over. Documentary evidence presented with quotes where
significant.]

### Issue 2: [Allegation]

[Same structure]

[Continue for each issue]

---

## Credibility Assessment

*[Standalone section. Address only witnesses whose credibility is
determinative — i.e., where the finding on an issue depends on which
account is credited.]*

### [Witness name/role]

**Internal consistency:** [Consistent / Inconsistent — note specifics]
**Corroboration:** [What documentary or other evidence corroborates
or undermines the account]
**Motive:** [Any reason to credit or discount the account]
**Demeanor:** [Attorney's observations if interviews were in person —
leave blank if not applicable or not observed]
**Assessment:** [Credit / Do not credit / Partially credit — with basis]

---

## Relevant Policies

[Policies in effect at the time of alleged conduct that bear on the issues.
Cite the version. Do not cite policies that were adopted after the conduct.]

---

## Conclusions

| Issue | Finding | Basis |
|---|---|---|
| [Issue 1] | Sustained / Not Sustained / Inconclusive | [One sentence] |
| [Issue 2] | ... | ... |

*Findings are based on a preponderance of the evidence standard.*

---

## Recommendations

[Organized by action type:]

**Disciplinary action:** [If any — state the basis, not just the outcome]
**Policy or process changes:** [If any gap in policies contributed]
**Training:** [If indicated]
**Further investigation:** [Any threads not fully resolved]
**Monitoring:** [Any follow-up needed]

---

## Appendix A: Chronology of Events

[Auto-generated from log entries sorted by date_of_event, not date_logged.
Format: Date | Summary | Source (Entry ID)]

## Appendix B: Documents Reviewed

[Summary table from documents-reviewed.yaml]
```

Write the draft to `~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-[slug]/memo.md`.

### If memo already exists — update

Read the memo and the log. Identify log entries added since the memo was
last drafted (compare date_logged against memo's last-updated date).

Report what has changed:

```
Since the last memo draft ([date]), the following has been added to the log:

[N] new entries
New issues: [any]
New conflicts: [any]
Resolved gaps: [any]

Sections that need updating:
  Factual findings: [which issues are affected]
  Credibility: [any new credibility-relevant entries]
  Conclusions: [any findings that should be revisited]
  Appendix A: [N] new chronology entries
```

Ask: "Want me to update the full memo, or just the affected sections?"

Apply updates. Preserve prior drafting. Mark changed sections with
`[UPDATED: date]` until the attorney reviews.

---

## Mode 5: Draft audience summary

Triggered by `/employment-legal:investigation-summary` or "draft a
summary for [audience]".

Ask: who is the audience and what decision or action does this summary
support?

**HR summary** (for HR decision on disciplinary action):
- What happened (factual summary, no legal analysis)
- Finding on each allegation (Sustained/Not Sustained/Inconclusive)
- Recommended action
- What is NOT in this summary: privilege analysis, credibility methodology,
  legal exposure assessment, attorney mental impressions
- Header: "Confidential — HR Use Only — Do Not Distribute"
- Do not include entry IDs or document citations — those stay in the memo

**Leadership/Board summary** (for governance decision):
- The allegation and scope in one paragraph
- Key findings
- Business impact / exposure (high level — no specific legal analysis)
- What the company is doing about it
- Header: "[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]"

**Outside counsel briefing** (handing off for litigation or deeper review):
- Full context including legal exposure analysis
- Open evidentiary threads
- Credibility issues that remain contested
- Documents that would be most significant in litigation
- Header: "[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]"

---

## Consequential-action gate (respond to a demand or complaint)

**Before producing a summary, memo, or content intended for an external response (EEOC/DFEH/state agency charge response, plaintiff's-counsel demand letter response, regulator response, or any formal complaint reply):** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Responding to a demand, charge, or complaint has legal consequences — positions taken here are admissions in later proceedings, waivers of defenses can be inadvertent, and privilege over the underlying investigation can be lost. Have you reviewed this response with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - The allegation, the forum, and the deadline
> - What the investigation surfaced (findings by allegation; documents reviewed; witnesses interviewed; Upjohn warnings given or not)
> - Any unresolved evidentiary threads or credibility contests
> - What the proposed response says and what it implicitly concedes
> - Open questions and what's unresolved
> - What could go wrong (privilege waiver, inconsistent factual statements, missed affirmative defense)
> - What to ask the attorney (is this the right theory; are we preserving defenses; should an outside firm take this over; what needs redaction or a privilege log)
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service. Agency and demand-letter responses are a place where untrained replies regularly create more exposure than the underlying allegation did.

Do not produce an external-response draft past this gate without an explicit yes. Internal memos, HR summaries, and leadership briefings used only within the organization do not trip this gate (but the privilege-formation caveat at the top of this skill still applies).

---

## What this skill does NOT do

- Make disciplinary decisions — it supports the attorney's findings,
  not HR's action
- Guarantee privilege — privilege depends on how the investigation is
  structured, not on how the memo is labeled
- Process documents it cannot read — if files are in formats that cannot
  be parsed, flag them for manual review
- Conduct interviews — it logs interview notes, it does not interview witnesses
- Replace Upjohn warnings — it tracks whether they were given, it does not
  give them

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

---

## /employment-legal:international-expansion

---
name: international-expansion
description: >
  Reference: implementation-planning framework for international hiring — EOR
  vs. entity decision framing, cross-functional triggers for tax/finance/HR,
  structured outside-counsel briefing requests, and a persistent gap tracker.
  Loaded by /expansion-kickoff and /expansion-update; not invoked directly.
user-invocable: false
---

# International Expansion Skill

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

International hiring gets handled sloppily at scaleups because nobody owns
the full picture. Legal knows the employment-law questions but not the PE
risk questions. Finance knows the cost model but not the employee-representation
triggers. HR knows the comp benchmarks but not the Day 1 compliance requirements.

This skill doesn't replace any of those functions. It maps the terrain, drafts
the right questions for each stakeholder, produces a briefing request that
walks outside counsel through the country-specific issues, and creates a
tracker that keeps the project moving across sessions.

This skill assumes expansion is decided. It is not a "should we expand?"
framework.

This skill does not contain country-specific employment law. The substantive
rules change frequently and vary by role, headcount, and industry — the skill
routes every country through an outside-counsel briefing rather than relying
on a stored reference table.

## Load context

Read `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, escalation table, any existing
expansion notes.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`).

## Workflow

### Step 1 — Information gathering

Ask all of the following in a single block:

> Before I build the expansion plan I need to understand the shape of this
> expansion. Please answer what you can — gaps in the answers are themselves
> useful data:
>
> **The expansion**
> - Which country?
> - What roles are you hiring? (Job function matters — a sales rep closing
>   deals creates different legal exposure than an engineer writing code)
> - How many hires are planned in the next 12 months?
> - When do you need the first person to start?
>
> **Current state**
> - Do you already have a legal entity in this country?
> - Have you used an EOR provider before? Are you already considering one?
> - Has tax or finance been looped in yet?
> - Do you have outside employment counsel in this country?
>
> **Strategic context**
> - Is this a long-term strategic commitment (building a real team) or
>   testing the market (one or two hires, see how it goes)?
> - Who is the executive sponsor making the structure decision?

Wait for responses before proceeding.

### Step 2 — EOR vs. entity framing

Do not make this decision. Frame it with enough precision that the CFO and
tax counsel can make it.

Work through the following factors against the intake answers and produce a
structured framing document:

**The core trade-off:**

| Factor | Points toward EOR | Points toward Entity |
|---|---|---|
| Headcount in 12 months | Fewer hires | More hires |
| Timeline to first hire | Short runway | Longer runway available |
| Strategic commitment | Testing the market | Long-term presence |
| Cost sensitivity | EOR markup acceptable | Scale makes entity more efficient |
| Control needs | Low — EOR employer handles local HR | High — want direct employer relationship |
| IP sensitivity | Lower | Higher — entity ownership cleaner |

Specific headcount break-even points, EOR markup ranges, setup costs, and
timelines vary by country and provider — do not hardcode them. Route those
questions to tax/finance and the EOR provider.

**PE risk flag (route to tax counsel):**
If roles include sales, business development, account management, or anyone
with authority to negotiate or sign contracts on behalf of the company —
flag this explicitly:

> PE Risk: [Role type] may create a taxable permanent establishment in
> [country] even before a legal entity exists. This is a tax question, not
> an employment question. Tax counsel must assess before the first hire.

**Produce the question for the CFO/tax:**

> Questions for your CFO and tax counsel:
> - At [N] hires over 12 months, at what headcount does entity setup become
>   more cost-effective than EOR (accounting for EOR markup, setup costs,
>   and ongoing compliance burden)?
> - [If PE-risk roles:] Do these role types create a taxable permanent
>   establishment in [country]? If yes, does that change the entity timeline?
> - If we start with EOR and convert to entity later, what are the transition
>   risks for the employees already on the EOR?
> - Who is our preferred EOR provider for this country, and have we vetted
>   their local compliance track record?

### Step 3 — Cross-functional triggers

For each function that needs to be looped in, state: what they need to do,
and the specific questions legal should ask them. Do not just say "loop in
finance." Draft the ask.

**Tax counsel** (always required before first hire)

What they need to do: PE risk analysis, determine whether entity is required
for tax purposes, advise on equity tax treatment in this jurisdiction.

Questions legal should ask:
- Does hiring a [role type] in [country] create a permanent establishment or
  taxable nexus before we have an entity?
- What is our exposure window if we start hiring before the PE question is
  resolved?
- How are our equity awards (RSUs/options) taxed in [country]? Do we need
  local tax counsel to advise employees at grant and vesting?
- If we set up an entity, what intercompany services agreement is needed
  between the subsidiary and the US parent?

**Finance / Payroll** (required before first paycheck)

What they need to do: identify local payroll provider (or confirm EOR handles
it), budget mandatory employer contributions, set up local banking if entity.

Questions legal should ask:
- Have we identified a local payroll provider? (If EOR: confirm EOR handles
  payroll including local social contributions)
- What are the mandatory employer contributions in [country] — pension,
  social insurance, healthcare — and are these budgeted in the comp model?
- How will equity grants be administered for employees in [country]? Has
  anyone modeled the employer-side tax withholding obligations at vesting?

**HR / Total Rewards** (required before offer is made)

What they need to do: benefits benchmarking, comp benchmarking against local
market, confirm mandatory vs. supplemental benefits.

Questions legal should ask:
- What benefits are legally mandatory in [country] vs. market-standard? (Do
  not want to accidentally promise more than required or less than market)
- Is our standard equity package competitive in this market, or does local
  practice differ significantly?
- Who will be this person's day-to-day manager — local or remote from HQ?
  (Affects employee-representation analysis and employment agreement terms
  in some jurisdictions)

**Outside counsel** (required — do not skip)

What they need to do: research and advise on the local employment framework
for this role and headcount, review/draft local employment agreement, flag
any structural issues with the proposed arrangement.

The outside-counsel briefing request in Step 4 is the agenda for this
engagement. Send it at the start — do not ask piecemeal.

### Step 4 — Country-specific briefing request

Instead of a stored country reference table, this skill produces a structured
outside-counsel briefing request. Substantive local law (entity requirements,
statutory benefits and contributions, termination protections, notice periods,
employee-representation / works-council / collective-bargaining obligations,
mandatory leave, restrictive covenants, data protection, work authorization)
varies by country *and* by role and headcount *and* by industry, and changes
frequently. Treat every country as a country that requires verification — do
not rely on the skill's own knowledge.

Draft the briefing request below, tailored to the intake answers:

**Outside counsel briefing request — [Country]**

> We are planning to hire [N] employees in [Country] starting [date], in the
> following roles: [roles]. Target headcount over 12 months: [N]. Preferred
> structure (subject to your advice and tax counsel): [EOR / entity /
> undecided]. We need a briefing covering each of the following. Please
> answer as questions with cites to primary law, not as a reference table —
> we want to be able to track changes over time.
>
> 1. **Entity and engagement structure** — what are our options (direct
>    hire via entity, EOR, contractor) and what are the practical and legal
>    trade-offs for this headcount and these roles?
>
> 2. **Employment contract requirements** — what form is required or standard?
>    What must be included? What cannot be included or is unenforceable?
>    What language or translation requirements apply?
>
> 3. **Termination** — what are the notice requirements and severance
>    obligations? How difficult is termination in practice (protected-cause
>    standards, social-selection rules in RIFs, reasonable-notice common-law
>    exposure)? What documentation standard should we establish from day one?
>
> 4. **Mandatory benefits and employer contributions** — what must we provide
>    by law (pension, social insurance, healthcare, paid leave, bonuses)?
>    What are the current employer contribution rates we should budget?
>    Please cite the controlling statute and verify currency.
>
> 5. **Restrictive covenants** — are non-competes enforceable? Under what
>    conditions and with what compensation requirements? What confidentiality
>    and IP assignment language holds up?
>
> 6. **Employee representation** — are there works council, employee
>    representation, union, or collective bargaining requirements? At what
>    headcount do they trigger? What consultation or co-determination rights
>    apply? Are we covered by any sectoral collective agreement even if we
>    are not unionized?
>
> 7. **Data protection** — what obligations apply to employee data? Is there
>    a data transfer mechanism needed for employee data flowing to the US?
>
> 8. **Work authorization** — what permits or visas are required for foreign
>    nationals? What are the processing timelines?
>
> 9. **Industry-specific rules** — are there sector rules, awards, or
>    collective agreements that apply to our industry regardless of whether
>    we are unionized?
>
> 10. **Contractor/independent-contractor risk** — what is the country's test
>     for classification, and what are the deemed-employment or reclassification
>     risks for any contractor arrangements we may consider?
>
> 11. **Equity / incentive compensation** — any local tax, securities, or
>     employment-law rules that govern how we grant RSUs, options, or other
>     equity here?
>
> 12. **Day 1 compliance** — what must be in place before the first employee
>     starts? Registration requirements, notices, filings, posters?
>
> 13. **Top 2-3 things that surprise US companies hiring here for the first
>     time** — what do you wish clients had asked you earlier? What has
>     *changed recently* that a US team might not have caught?

Add this briefing request to the expansion tracker as a single open item:
owner = Outside Counsel, status = open, with the full briefing agenda in
the questions field. If the jurisdiction is one the team has asked about
before, still send the briefing — this is a currency check, not a first
contact.

### Step 5 — Create the expansion tracker

Write a new file to `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-[country-slug].yaml` with all open items
identified in Steps 2-4. This file persists across sessions.

Format:

```yaml
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]
country: [Country name]
country_slug: [lowercase-hyphenated]
kickoff_date: [ISO date]
first_hire_target: [ISO date or "TBD"]
headcount_12mo: [N]
roles: [list]
strategic_commitment: [testing / long-term]
eor_or_entity: [EOR / entity / undecided]
outside_counsel_engaged: [true / false]
pe_risk_flagged: [true / false]
last_updated: [ISO date]

open_items:
  - id: 1
    category: [structure / tax / finance / hr / outside-counsel / compliance]
    item: "[what needs to happen]"
    owner: "[function or person]"
    status: [open / in-progress / done / blocked]
    due: [ISO date or null]
    questions:
      - "[specific question drafted in Steps 2-4]"
    notes: ""

  - id: 2
    [etc.]
```

Generate one open item per action identified across Steps 2-4. Do not collapse
multiple actions into one item — each item should be completable and
attributable to a single owner.

### Step 6 — Output

> **Jurisdiction assumption.** This plan frames the expansion to the single country identified in intake. Local employment law, tax rules, employee-representation obligations, and data-protection requirements vary materially by country, region, industry, and headcount, and change frequently. Every substantive local-law answer comes from the outside-counsel briefing request, not from this skill. If the plan is adapted for another country later, re-run the briefing.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## International Expansion: [Country] — [Date]

**First hire target:** [date]
**Headcount (12 months):** [N]
**Roles:** [list]
**Tracker:** ~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-[slug].yaml

---

### EOR vs. Entity

[Framing from Step 2 — table, PE risk flag if applicable, questions for CFO/tax]

---

### Who needs to be looped in — and what to ask them

**Tax counsel** — [N] questions
[Questions from Step 3]

**Finance / Payroll** — [N] questions
[Questions from Step 3]

**HR / Total Rewards** — [N] questions
[Questions from Step 3]

**Outside counsel** — see briefing request below
[Full briefing request from Step 4]

---

### Open items ([N] total)

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | [item] | [owner] | Open |
[etc.]

---

Run `/employment-legal:expansion-update [country]` to update status
as items close.
```

## What this skill does NOT do

- Advise on specific local employment law — that is outside counsel's job.
- Make the EOR vs. entity decision — frames it for the right decision-makers.
- Draft the local employment agreement — flags that outside counsel must do
  this.
- State country-specific rules from its own knowledge — every country is
  routed through an outside-counsel briefing.
- Substitute for outside counsel engagement — every new country requires
  local counsel, no exceptions.

---

## /employment-legal:investigation-add

---
name: investigation-add
description: >
  Add data to an open investigation — documents, interview notes, or
  observations. Processes batches against the documented pull criteria,
  surfaces significant items, and logs everything reviewed for coverage
  verification. Use when new evidence, interview notes, or document
  productions come in for an open investigation.
argument-hint: "[matter name or slug, then paste or attach data]"
---

# /investigation-add

Adds data to an open investigation log. Processes document batches using
documented pull criteria, surfaces significant items, logs everything
reviewed for coverage verification.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`.
2. Load the `internal-investigation` reference skill and run Mode 2 (Add data).
3. After processing, show the surface ratio and list of surfaced items.
4. Prompt to update the sources checklist if the data covers a checklist item.

## Examples

```
/employment-legal:investigation-add [matter name]
[paste interview notes]
```

```
/employment-legal:investigation-add [matter name]
[attach email export]
```

> Detailed needle-finding process, log entry format, surface-ratio rules, and
> sources-checklist tracking live in the `internal-investigation` reference
> skill — load it before doing substantive work.

---

## /employment-legal:investigation-memo

---
name: investigation-memo
description: >
  Draft or update the privileged investigation memo from the investigation log.
  Use when an investigation is far enough along to write the first memo cut, or
  when new data has been added and the existing draft needs updating.
argument-hint: "[matter name]"
---

# /investigation-memo

Drafts the first cut of the privileged investigation memo from the log,
or updates an existing draft when new data has been added.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 4 (Draft or update memo).
2. If drafting for the first time, warn if high-priority sources are still
   open on the checklist.
3. If updating, show what changed before rewriting.
4. All output is marked PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT.

## Examples

```
/employment-legal:investigation-memo [matter name]
```

```
/employment-legal:investigation-memo [matter name]
(updates existing memo if one exists)
```

> Detailed memo structure, credibility-assessment framework, and update rules
> live in the `internal-investigation` reference skill — load it before doing
> substantive work.

---

## /employment-legal:investigation-open

---
name: investigation-open
description: >
  Open a new internal investigation matter — runs intake, generates the sources
  checklist, and creates the persistent investigation log. Use when a complaint
  or allegation comes in and the attorney needs to stand up a privileged
  investigation workspace.
argument-hint: "[brief description of the allegation]"
---

# /investigation-open

Opens a new investigation matter — runs intake, generates the sources
checklist, and creates the persistent investigation log.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`.
2. Load the `internal-investigation` reference skill and run Mode 1 (Open).
3. If a matter with the same slug already exists, warn before overwriting.

## Examples

```
/employment-legal:investigation-open
Harassment complaint filed against a manager in the Austin office.
```

```
/employment-legal:investigation-open
(skill will ask for details)
```

> Detailed intake, privilege-formation requirements, sources checklist, and log
> templates live in the `internal-investigation` reference skill — load it
> before doing substantive work.

---

## /employment-legal:investigation-query

---
name: investigation-query
description: >
  Ask questions against an open investigation log — what witnesses said, where
  accounts conflict, what gaps exist, what the strongest evidence is on each
  issue. Use when the attorney needs to query the investigation record without
  re-reading every entry.
argument-hint: "[matter name] [question]"
---

# /investigation-query

Answers questions against the investigation log — what witnesses said,
where accounts conflict, what gaps exist, what the strongest evidence is
on each issue.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 3 (Query).
2. Always cite log entry IDs in the answer.
3. If the log contains nothing relevant to the question, say so explicitly —
   "I have not seen any information on [topic] in this investigation log
   ([N] entries reviewed)" — and offer to flag it as a gap.

## Examples

```
/employment-legal:investigation-query [matter name]
What did the respondent say about the December team dinner?
```

```
/employment-legal:investigation-query [matter name]
Where do the complainant's and respondent's accounts conflict?
```

```
/employment-legal:investigation-query [matter name]
What do we still need?
```

> Detailed log-query process, citation rules, and gap-flagging templates live
> in the `internal-investigation` reference skill — load it before doing
> substantive work.

---

## /employment-legal:investigation-summary

---
name: investigation-summary
description: >
  Draft an audience-specific summary from the privileged investigation memo —
  HR, leadership, or outside counsel versions. Use when an investigation memo
  needs to be communicated to an audience that should not see the full
  privileged work product.
argument-hint: "[matter name] [audience: hr / leadership / outside-counsel]"
---

# /investigation-summary

Drafts a stripped-down, audience-appropriate summary from the privileged
investigation memo. HR summaries contain no privilege analysis. Leadership
summaries are high-level. Outside counsel briefings include full context.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 5 (Audience summary).
2. If no memo exists yet, offer to draft the memo first.
3. HR summaries must not include attorney mental impressions, credibility
   methodology, or legal exposure analysis.

## Examples

```
/employment-legal:investigation-summary [matter name] hr
```

```
/employment-legal:investigation-summary [matter name] leadership
```

```
/employment-legal:investigation-summary [matter name] outside-counsel
```

> Detailed audience-stripping rules and summary templates live in the
> `internal-investigation` reference skill — load it before doing substantive
> work.

---

## /employment-legal:leave-tracker

---
name: leave-tracker
description: >
  Check open leaves for deadline alerts and required decisions. Surfaces only
  the leaves that require an action and explains why — not a status board.
  Use weekly, or whenever the attorney needs to know which leaves have
  upcoming designation, certification, or exhaustion deadlines.
argument-hint: "[no arguments — works from HRIS or leave-register.yaml]"
---

# /leave-tracker

Checks all open leaves with hard legal deadlines and surfaces only the ones
requiring a decision or action. Not a status board — tells you what you need
to do and why.

## Instructions

1. Load the `leave-tracker` agent and run the full workflow.

2. If no HRIS is connected and no `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` exists, prompt
   the attorney to upload a leave spreadsheet or use
   `/employment-legal:log-leave` to add entries.

3. Alerts only for leaves requiring action. Clean leaves summarized one line each.

## Examples

```
/employment-legal:leave-tracker
```

Run this weekly — set a Monday-morning reminder to invoke
`/employment-legal:leave-tracker`. Automated scheduling requires a separate
integration (calendar reminder, cron job, etc.); Claude Code agents do not
self-schedule.

---

## /employment-legal:log-leave

---
name: log-leave
description: >
  Add a new leave to the leave register with the minimum information needed to
  start tracking deadlines. Use when an employee goes on leave and you want the
  tracker to watch designation, certification, and exhaustion clocks from day
  one.
argument-hint: "[describe the leave — employee/role, type, jurisdiction, start date]"
---

# /log-leave

Adds a new leave entry to `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` with the minimum
information needed to start tracking deadlines. Use when an employee goes on
leave and you want the tracker to watch the clocks from day one.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdiction table and Systems section.

2. Ask all of the following in a single prompt — do not drip them one at a time:

   > A few quick questions to set up leave tracking:
   >
   > - Employee name or role (anonymized is fine)
   > - Where do they work? (State — this determines which rules apply)
   > - Leave type: FMLA / state leave (which state) / USERRA / ADA accommodation
   > - Leave start date
   > - Is this intermittent leave?
   > - Expected return date (if known — leave blank if not)
   > - Has the designation notice been sent? If yes, when?
   > - Has medical certification been requested? If yes, when?

3. Using the jurisdiction table in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`, look up the applicable leave
   entitlement (hours/weeks) for this leave type in this jurisdiction.

4. Compute the first upcoming deadline based on the information provided:
   - Designation not yet sent → deadline is 5 business days from leave start
   - Med cert requested but not received → deadline is 15 days from request date
   - Both sent and received → next deadline is at 75% exhaustion

5. Write a new entry to `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` using the leave register
   format from the leave-tracker agent. If the file doesn't exist, create it.

6. Confirm with a single line:
   > "Logged. [Employee/Role] — [Leave type] — [Jurisdiction] — started [date].
   > First deadline: [what it is and when]. Leave tracker will alert automatically."

## Examples

```
/employment-legal:log-leave
```

```
/employment-legal:log-leave
Sarah (Sr. Engineer, works in California) just started FMLA today for a
serious health condition. Intermittent. No designation sent yet.
```

---

## /employment-legal:matter-workspace

---
name: matter-workspace
description: >
  Manage matter workspaces — new, list, switch, close, or detach (practice-
  level). Creates, lists, switches, closes, and detaches the active matter so
  context from one client engagement never leaks into another. Use when a
  multi-client practitioner says "new matter", "switch matter", "list my
  matters", "close this matter", or needs to manage which matter is active.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Practitioners work across multiple clients and matters. A matter workspace keeps one client or engagement's context separate from every other. This skill manages those workspaces.

## Subcommands

- `/employment-legal:matter-workspace new <slug>` — create a new matter workspace, run a short intake, write `matter.md`
- `/employment-legal:matter-workspace list` — list matters with status and active flag
- `/employment-legal:matter-workspace switch <slug>` — set the active matter
- `/employment-legal:matter-workspace close <slug>` — archive a matter (move to `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/_archived/`, never delete)
- `/employment-legal:matter-workspace none` — detach from any active matter, work at practice-level only

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` — confirm the `## Matter workspaces` section is populated. If `Enabled` is `✗`, tell the user: "Matter workspaces are off — you're configured as an in-house practice with one client, so the plugin works from practice-level context automatically. If you actually work across multiple clients, re-run `/employment-legal:cold-start-interview --redo` and select a private-practice setting. Otherwise, you don't need `/matter-workspace` at all." Don't error — the disabled state is the expected one for in-house users.
2. Use the subcommand logic below.
3. Dispatch on the first token of `$ARGUMENTS`:
   - `new` → run the intake interview, write `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<slug>/matter.md`, seed `history.md` and `notes.md`.
   - `list` → enumerate `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/*/matter.md`, print a table, mark the active matter.
   - `switch` → update the `Active matter:` line in the practice-level CLAUDE.md.
   - `close` → move `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<slug>/` to `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/_archived/<slug>/`, log the close date in `history.md`.
   - `none` → set `Active matter:` to `none — practice-level context only`.
4. Show the user what changed and confirm before writing.

## Notes

- The skill never reads across matters unless `Cross-matter context` is `on` in the practice-level CLAUDE.md.
- Archiving is not deletion — closed matters remain readable for retention/conflicts purposes.
- Slugs are lowercase with hyphens. If a slug is reused across archived and active, the archived one is preserved under `_archived/<slug>/`.

---

## Reference

Multi-client practitioners (private practice — solo, small firm, large firm) work across many matters. Context from one must not leak into another. This skill is the thin file-management layer that makes that true.

**Default state is off.** In-house users never see this — they run at practice-level only. Matter workspaces turn on at cold-start for private-practice users, or by editing `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, this skill does not run; instead it explains the disabled state and suggests `/employment-legal:cold-start-interview --redo` for users who actually need matter isolation.

## Storage layout

All matter data lives under:

```
~/.claude/plugins/config/claude-for-legal/employment-legal/
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
   - **Matter type** (read the plugin's practice profile for typical categories; for employment-legal: hire | termination | investigation | leave | accommodation | classification | country expansion | policy project | other)
   - **Confidentiality level** (standard | heightened | clean-team — heightened prompts extra care in cross-matter settings)
   - **Key facts** (2–5 sentences: what this matter is about, who the stakeholders are, what's at stake)
   - **Matter-specific overrides to the practice playbook** (e.g., "client requires 24-month LoL cap not 12", "counterparty is a strategic partner — relationship-preserving tone")
   - **Related matters** (slugs of any connected matters)
3. Write `matters/<slug>/matter.md` using the template below.
4. Seed `matters/<slug>/history.md` with a single "Opened" entry.
5. Create an empty `matters/<slug>/notes.md`.
6. Do **not** auto-switch to the new matter. Ask: "Want to switch to `<slug>` now? (`/employment-legal:matter-workspace switch <slug>`)"

### `list`

Enumerate `matters/*/matter.md`. Read each file's front-matter or first few lines to extract status. Print a table:

| Slug | Client | Matter type | Status | Opened | Active |
|---|---|---|---|---|---|

Mark the currently-active matter with `*`. Include `_archived/*` under a separate "Archived" heading if any exist.

### `switch <slug>`

1. Confirm `matters/<slug>/matter.md` exists. If not, offer `/employment-legal:matter-workspace new <slug>`.
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

## /employment-legal:policy-drafting

---
name: policy-drafting
description: >
  Draft an employment policy with state supplements where law differs across
  the jurisdictional footprint. Use when the user says "draft a [topic]
  policy", "we need a policy on", "update our [topic] policy", or names a
  policy gap.
argument-hint: "[policy topic — e.g., 'remote work', 'parental leave', 'PTO']"
---

# /policy-drafting

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, handbook location.
2. Use the workflow below.
3. Draft core policy. Check each jurisdiction in footprint for required variants.
4. Output: core policy + state supplements. Flag where law is currently shifting.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A policy that's right for California may be wrong (or unnecessary) in Texas. This skill drafts a core policy and generates state supplements where the footprint requires different rules.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, handbook location and format.

## Workflow

### Step 1: Scope the policy

- What's the policy for? (Remote work, parental leave, social media, etc.)
- Why now? (Legal requirement, incident, growth, gap noticed)
- Who does it apply to? (All employees, certain roles, certain locations)

### Step 2: Jurisdictional scan

For each state/country in the footprint, check: does this jurisdiction have a specific rule on this topic?

**Common topics with jurisdictional variance:**

| Topic | Variance |
|---|---|
| Paid leave | State mandates (CA, NY, CO, WA, etc.) with different accrual rates, uses, carryover |
| Parental leave | State programs layer on top of FMLA (CA PFL, NY PFL, etc.) |
| Meal and rest breaks | CA is the outlier (penalty pay); most states minimal |
| Expense reimbursement | CA requires; most states don't |
| Pay transparency | Growing list of states requiring ranges in postings |
| Non-competes | See hiring-review skill — unenforceable in some states |
| Final pay | Timing varies widely |

If the topic has no jurisdictional variance (dress code, say), skip this step.

### Step 3: Draft the core policy

One policy. Applies everywhere. Clear and readable — employees should understand it without a lawyer.

Structure:
- Purpose (one sentence — why this policy exists)
- Scope (who it applies to)
- The rule (what's required/permitted/prohibited)
- Process (how to request, who approves, what happens if)
- Questions (who to ask)

Avoid: "heretofore," "notwithstanding," nested exceptions. This is a handbook policy, not a contract.

### Step 4: State supplements

For each jurisdiction where the rule differs, a supplement:

```markdown
### [State] Supplement

Employees working in [State] are subject to the following in addition to / instead of the core policy:

- [Specific difference]
- [Cite the state law if helpful]
```

Keep supplements tight. Only what's different — don't repeat the core.

### Step 5: Cross-check

- Does this policy conflict with anything already in the handbook?
- Does it promise more than the company intends to deliver? (A policy is a promise — courts hold employers to handbook promises.)
- Does it inadvertently create a contract? (Some states treat handbook policies as contractual — include the standard "this is not a contract" language if the handbook doesn't already.)

## Output

```markdown
# [Policy Name]

## Core Policy

[Full text]

## State Supplements

### [State 1]
[Supplement]

### [State 2]
[Supplement]

---

## Drafting Notes (internal — remove before handbook insertion)

- **Jurisdictional scan:** [which states checked, which have variance]
- **Conflicts with existing handbook:** [none | list]
- **Law currently shifting:** [any state where this is in flux]
- **Review cadence:** [when to revisit — annual, or when X happens]
```

> **Draft, not a policy in effect.** This is a drafting aid for attorney review, not a policy you can publish. Publishing a handbook policy has legal consequences — in several states it can bind the company as a contractual promise, and wage/leave/accommodation policies are routinely read against the employer. A licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction reviews, edits as needed, and takes professional responsibility before the policy is rolled out. Do not publish or distribute this draft unreviewed.

## Handoff

To handbook-updates skill: when this policy is approved, it diffs against the current handbook and flags what changes.

## What this skill does not do

- Approve the policy. It drafts; a human approves.
- Roll out the policy. Communication to employees is an HR workflow.
- Cover every jurisdiction on earth — only the ones in the footprint. If the footprint expands, re-run.

---

## /employment-legal:termination-review

---
name: termination-review
description: >
  Termination review — high-risk flag detection, severance + release, and
  final pay timing by jurisdiction. Jurisdiction-specific rules and release
  consideration periods are researched per review, not stored. Use when the
  user says "reviewing a termination", "can we fire this person", "term
  review", or describes a termination scenario.
argument-hint: "[describe the termination, or attach documentation]"
---

# /termination-review

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → termination review triggers, high-risk flags, severance practice, jurisdiction rules.
2. Use the workflow below.
3. Walk the checklist. Check every high-risk flag.
4. Final pay timing per employee's jurisdiction. Severance + release if applicable.
5. If any high-risk flag fires: escalate per table, don't proceed without sign-off.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Most terminations are fine. A few are lawsuits waiting to happen. This skill
runs the checklist that catches the second kind before the decision is final.
The skill does not state the law — every jurisdiction-specific rule and
release-period requirement is researched and cited at the time of review.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → termination review triggers, high-risk flags, standard severance,
jurisdiction table.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`). Match the memo format from seed term memos referenced in that config where one exists. The work-product header is always first.

## Workflow

### Step 1: The basic facts

- Employee name (or role if staying abstract)
- Jurisdiction (where they work)
- Reason for termination (performance, misconduct, RIF, position elimination)
- How long employed
- Age (relevant to release requirements for older-worker protections)
- Whether any other employees are being terminated as part of the same
  decisional unit or program (relevant to group-termination release rules)
- When is the planned term date

### Step 2: High-risk flag scan

This is the most important step. Check every flag from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. Default
set:

| Flag | Why it's high-risk | Check |
|---|---|---|
| **Recent complaint** | Retaliation claim | Has this employee filed any complaint (HR, ethics hotline, regulatory) recently? |
| **Protected leave** | Leave-law interference/retaliation | Currently on or recently returned from protected leave (FMLA/state equivalents, disability, parental, military)? |
| **Protected class + timing** | Discrimination claim | Protected class AND recently disclosed/visible (pregnancy announcement, religious accommodation request, disability disclosure)? |
| **Whistleblower** | Federal and state whistleblower statutes | Has this employee raised concerns about illegality, safety, fraud? |
| **Thin documentation** | "Why now?" problem | For performance terms: is there a PIP, written warnings, documented feedback? Or did this come out of nowhere? |
| **Comparator problem** | Disparate treatment | Is someone else doing the same thing and not being terminated? |
| **Contract/handbook promise** | Breach | Does the offer letter, handbook, or any writing promise a process that isn't being followed? |
| **Exempt misclassification** | FLSA + state wage claim with liquidated damages | See the classification check below. Fires on state + classification + title. |

**Exempt/non-exempt classification flag.** Fire this flag when ALL of the
following are true:

1. The employee works in a state with a high exempt salary threshold — **CA,
   NY, WA, CO, AK** (and any other state listed in
   `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` →
   `## Wage & hour` → Known classification risk areas as a high-threshold
   state) — **AND**
2. The employee is classified **exempt** (salaried, no overtime) — **AND**
3. The employee's title contains **"supervisor," "lead," "coordinator,"
   "analyst," "administrator,"** or **"specialist"** (case-insensitive, and
   any equivalent-scope title the practice profile flags as risky).

When all three fire, emit:

> 🔴 **Potential exempt misclassification** — [title] earning $[X] in
> [state]. The exempt salary threshold in [state] is approximately $[Y]
> `[model knowledge — verify]`. Before termination, route to
> `/employment-legal:wage-hour-qa` for a classification check — a misclassified
> employee who's terminated has a ready-made FLSA and state-wage claim with
> liquidated damages, attorneys' fees, and (in CA) PAGA exposure, which
> the separation agreement may not be able to release cleanly. A terminated
> plaintiff with unpaid-OT exposure is the most litigated wage-and-hour
> fact pattern in these states.

Do not suppress this flag because the title "looks managerial" — the whole
premise of the misclassification claim is that titles lie. Route to
`/employment-legal:wage-hour-qa` for the actual duties-and-salary test.

**If a back-pay number is being computed as part of this review (severance
modeling, settlement posture, exposure estimate), do NOT compute it in this
skill.** Route to `wage-hour-qa` → Step 2a and use its regular-rate
scaffold: §207(e) inclusions (non-discretionary bonuses, commissions,
shift diffs) in the regular rate, 0.5× premium when straight time was
already paid for OT hours (else 1.5×), liquidated damages under §216(b),
and 2-year / 3-year willful SOL under §255(a). Every back-pay number
carries `[verify — consult wage-and-hour counsel before asserting or
paying]`. A clean-looking wrong number here is the specific failure mode
this scaffold prevents.

**Any flag fires → escalate per `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` before the term proceeds.** Not
after. Before.

### Step 3: Jurisdiction-specific requirements

> **Research the applicable rules for the employee's jurisdiction before
> finalizing the plan.** Specifically:
>
> - Final-pay timing — this varies widely by state and often depends on
>   whether the employee was terminated or resigned. Research the currently
>   operative rule, including any waiting-time or late-pay penalties.
> - Accrued-PTO payout — research whether the jurisdiction requires payout,
>   and any interaction with accrual-cap or use-it-or-lose-it policies.
> - Required notices — research any jurisdiction-specific notices required at
>   termination (e.g., state unemployment, continuation-coverage notices
>   beyond federal COBRA, benefits continuation).
> - Mass-layoff / plant-closing notices — research federal WARN Act and any
>   state "mini-WARN" or local ordinance that may apply if this is part of a
>   larger reduction. Coverage thresholds and notice periods differ.
>
> Cite primary sources. Verify currency.
>
> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for the jurisdiction's final-pay, PTO, notice, or WARN rule, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [jurisdiction / rule]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) stop here and flag for attorney verification. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Tag every citation in the plan — final-pay rule, PTO rule, notices, WARN / mini-WARN, OWBPA consideration periods, state release restrictions — with where it came from: `[Westlaw]`, `[CourtListener]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the user supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

### Step 4: Severance and release

Per `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → standard severance:

- Is severance being offered? Per formula or discretionary?
- Release required? (Usually yes if paying severance — that's the
  consideration.)

> **Research the applicable release-consideration rules.** If the employee is
> 40 or over, federal law (OWBPA) imposes specific requirements that affect
> the consideration period, revocation period, required advisements, and —
> for group terminations — required decisional-unit disclosures. The specific
> consideration period differs between an individual termination, a group
> RIF, and a group exit incentive; the rule also depends on the employee's
> age and the number of employees affected. Do not state the day count from
> memory — research the currently operative rule for the specific situation
> and cite primary sources. Also research any state-law analogs or parallel
> release requirements. Verify currency.

Separately, consider whether any of the following apply to the release:
- State-specific waiver restrictions (some states limit what can be released
  or require specific language).
- Federal or state restrictions on non-disclosure or non-disparagement
  clauses that relate to sexual harassment, discrimination, or other
  protected categories.
- Separation-agreement rules on NLRA-protected activity.

### Step 5: Documentation check

For performance terminations especially:

- Is there a paper trail? Written warnings, PIP, feedback docs?
- Does the paper trail tell a consistent story?
- Is there anything in writing that contradicts the reason (recent positive
  review, bonus, promotion)?

The "why now" question: if this person has been underperforming for a year,
what changed? The answer should be documented.

## Output

> **Research-connector pre-flight.** Before emitting the memo, check whether a legal research connector is reachable for this session — Westlaw, CourtListener, or any firm-configured research MCP. Collect this into the reviewer note per CLAUDE.md `## Outputs`: if no connector returns results in Step 3 (or none is configured at run time), record it in the **Sources:** line of the reviewer note — e.g., `not connected — cites from training knowledge; the highest-fabrication topics in termination-law memos are final-pay timing, OWBPA group/individual distinctions, state-specific NDA / non-disparagement rules (e.g., CA SB 331), and NLRB positions (e.g., McLaren Macomb) — spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner above the memo.

> **Jurisdiction assumption.** This review assumes the employee's jurisdiction as stated in Step 1 and any defaults from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → Jurisdictional footprint. Employment rules, final-pay timing, release requirements, and notice obligations vary materially by jurisdiction. If the employee works in a different state or country, or if choice-of-law is contested, this analysis may not apply as written.

Match the memo format from seed term memos referenced in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If none:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Termination Review: [Role/Name] — [Date]

**Jurisdiction:** [State]
**Reason:** [Performance / Misconduct / RIF / Elimination]
**Planned date:** [Date]

---

### Bottom line

[Can you proceed / Need to fix X first / Stop — one-sentence why]

---

### High-risk flags

[Every flag from Step 2. ✅ Clear or 🔴 FLAG with detail.]

**Escalation:** [None needed | Escalate to [name] before proceeding — [which flag]]

---

### Jurisdiction requirements ([State])

- Final pay: [researched rule and cite; state whether PTO is included per the
  researched rule and any team policy]
- Required notices: [list, each researched and cited]
- Mass-layoff notice (if applicable): [researched rule and cite]

---

### Severance and release

- Severance: [amount per formula / none]
- Release: [required / not — if required, research and apply the
  consideration-period, revocation-period, advisement, and (for groups)
  decisional-unit-disclosure requirements that govern this specific
  situation; cite primary sources and verify currency]
- [Any state-law release rules or non-disclosure/non-disparagement
  restrictions that apply]

---

### Documentation

[Assessment of paper trail. Gaps flagged.]

---

### Go / No-go

[Clear to proceed | Proceed with changes below | Hold — escalation pending]

### Checklist for term day

- [ ] Final paycheck ready, correct amount, delivered per researched rule
- [ ] Continuation-coverage notices (COBRA / state analogs) prepared
- [ ] [State] unemployment notice prepared
- [ ] Severance agreement (if applicable) with the consideration period
      required for this specific situation
- [ ] Return of property / access cutoff coordinated
- [ ] [etc.]
```

## Consequential-action gate (terminate an employee)

**Before producing a "Go" recommendation or a term-day checklist marked ready:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Terminating an employee has legal consequences — wrongful-termination, discrimination, retaliation, and wage-law claims all trace back to how this decision is structured. Have you reviewed this termination with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - Employee, jurisdiction, reason, planned date
> - Every high-risk flag the review surfaced (recent complaint, protected leave, protected class + timing, whistleblower, thin documentation, comparator, contract/handbook promise) — with detail
> - Jurisdiction-specific findings (final pay, PTO, required notices, mass-layoff rules) and where they were cited from
> - Severance/release analysis, including any OWBPA/older-worker-protection angles
> - Open questions and what's unresolved
> - What could go wrong (the claim theory this fact pattern supports)
> - What to ask the attorney (is this a clean term; do we need more documentation first; does the release need specific language; do we need to stagger decisional units)
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service. Employment is one of the practice areas where a short consult before the termination meeting consistently outvalues a post-termination claim defense.

Do not produce a "Clear to proceed" output past this gate without an explicit yes. A marked-DRAFT flagged for attorney review is fine.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- Make the termination decision. It checks the decision.
- Have the conversation. The manager does that.
- State release or jurisdiction rules from memory — every rule is researched
  and cited at the time of review.
- Guarantee no lawsuit. It reduces the risk by catching the obvious problems.

---

## /employment-legal:wage-hour-qa

---
name: wage-hour-qa
description: >
  Jurisdiction-aware wage/hour and employment Q&A — classification, overtime,
  meal/rest breaks, leave, final pay — answered for the specific state/country
  with the controlling rule researched and cited rather than stated from
  memory. Use when the user asks any employment law question, or says "what's
  the rule in [state]", "is this exempt", "do we have to pay overtime for",
  or "can we classify this as".
argument-hint: "[question]"
---

# /wage-hour-qa

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint.
2. Use the workflow below.
3. Identify jurisdiction the question is about. If not specified, ask.
4. Answer per that jurisdiction's rule. Cite. Flag if it's a close call or law is shifting.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

"It depends" is true but unhelpful. This skill produces a jurisdiction-specific
answer grounded in researched, cited primary sources — and flags when the
question is close enough to need human judgment. It does not state rules from
memory: wage-and-hour thresholds, exemption criteria, and final-pay timing
change frequently and vary meaningfully by state.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint. If the question doesn't specify a
jurisdiction, ask — or answer for the state with the most employees and note
that.

## The answer

### Step 1: Jurisdiction

Which state/country is this about? If not stated:
- If it's about a specific employee: where do they work?
- If it's a policy question: identify the jurisdictions in the footprint that
  are most likely to be the most restrictive on the question at hand, then
  research those.

### Step 2: Research the rule, then state it

> **Research before answering.** For the jurisdiction and question, identify
> the currently operative rule. Cite the controlling primary source (statute,
> regulation, wage order, or case) with a pinpoint cite. Note the effective
> date and whether the rule has been recently amended, indexed, or is in
> litigation. If you are uncertain or cannot verify the current state of the
> law, say so and flag for attorney verification — do not state a rule you
> haven't confirmed.

State the rule in one paragraph, tied to the cite. Use your tools (web search,
legal research integrations, team reference materials) to verify currency —
especially for:

> **No silent supplement.** If a research query to the configured legal research tool (Westlaw, CourtListener, or firm platform) returns few or no results for the jurisdiction-and-question, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [jurisdiction / question]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag the question as unverified and stop here. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Tag every citation in the answer with where it came from: `[Westlaw]`, `[CourtListener]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the user supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.


- Salary thresholds for any exemption (federal and state — several states
  index annually and several have tiered thresholds by employer size).
- Final-pay timing on termination vs. resignation (many states differ).
- PTO payout requirements (jurisdiction-specific; some require, some leave
  it to policy, some depend on accrual-plan design).
- Meal and rest break rules and any penalty-pay consequence.
- Daily or weekly overtime rules (some states have daily overtime and
  double-time rules that federal law does not).
- Classification tests — see the worker-classification skill; the applicable
  test depends on jurisdiction and purpose.

Common question types you may be asked — for each, the answer is
jurisdiction-specific and time-sensitive. Do not state the rule here; route
to research:

- "Is this role exempt?" — Research the applicable federal and state salary
  thresholds (verify current amounts and any employer-size tiers) and the
  applicable duties test(s).
- "Do we have to pay overtime for X?" — Research federal FLSA overtime plus
  any state-specific overtime rules (daily OT, double-time, alternative
  workweeks).
- "Do we have to provide meal/rest breaks?" — Research the applicable
  state rule and any penalty-pay consequence for missed breaks.
- "When is final pay due?" — Research the applicable state rule, including
  whether timing differs for termination vs. resignation and whether
  waiting-time or late-pay penalties apply.
- "Do we have to pay out accrued PTO?" — Research the applicable state rule
  and any carve-out for accrual-cap or use-it-or-lose-it policies.
- "Can we classify this person as a contractor?" — Route to
  `/employment-legal:worker-classification` if the facts are not already clear.

### Step 2a: FLSA regular-rate and back-pay calculations

When the question is a back-pay computation, unpaid-OT computation, or any
question that turns on the FLSA "regular rate," use this scaffold. Do not
answer from bare hourly wage × OT hours; that's the two most common errors
this skill exists to catch.

**The regular rate is NOT just the hourly wage.** Under 29 U.S.C. §207(e),
the regular rate is **all remuneration** for employment EXCEPT the eight
statutory exclusions in §207(e)(1)–(8) (e.g., discretionary bonuses, gifts,
premium pay, expense reimbursements, profit-sharing plans meeting the DOL
regs, stock options meeting §207(e)(8), retirement/insurance contributions).
Anything NOT within those eight exclusions is IN.

1. **Non-discretionary bonuses are IN the regular rate.** Productivity
   bonuses, attendance bonuses, commissions, shift differentials, contest
   awards, and most "bonuses" a reasonable employee would expect as a matter
   of course are non-discretionary under §207(e)(3) and 29 C.F.R. §778.211.
   Divide the bonus by the total hours worked in the bonus period to get
   the per-hour increase to the regular rate. True discretionary bonuses
   (§207(e)(3)) require both the fact of payment AND the amount to be
   within the employer's sole discretion, determined at or near the end of
   the period — narrow category.
2. **The unpaid OT premium is 0.5×, not 1.5× — when straight time was
   already paid for all hours.** If the employee was paid straight time for
   every hour (including the OT hours) but no premium, they are owed the
   **half-time premium** on OT hours, not time-and-a-half: `unpaid OT =
   0.5 × regular rate × OT hours`. 29 C.F.R. §778.110(b). If the employee
   was NOT paid for the OT hours at all, the owed amount is 1.5× the
   regular rate on those hours. **State which pay posture you're assuming
   before you compute** — it determines 0.5× vs. 1.5× and is the most
   common error in this computation.
3. **Show your math.** Print the formula and the inputs explicitly:
   ```
   Regular rate    = (straight-time wages + non-discretionary bonuses + other non-excluded comp) ÷ total hours worked
   OT premium owed = 0.5 × regular rate × OT hours    [if straight time already paid for OT hours]
                   = 1.5 × regular rate × OT hours    [if OT hours were unpaid]
   ```
   A number without the formula is not usable by a wage-and-hour lawyer.
4. **Liquidated damages double the back-pay.** 29 U.S.C. §216(b). Liquidated
   damages equal the unpaid back-pay amount unless the employer proves, to
   the court's satisfaction, that the violation was in good faith and based
   on reasonable grounds to believe it was not a violation. 29 U.S.C.
   §260. Default assumption is liquidated damages apply; the employer bears
   the burden to avoid them.
5. **Statute of limitations is 2 years; 3 for willful.** 29 U.S.C. §255(a).
   State the lookback explicitly and compute both bookends unless the
   willfulness posture is already established by the user.
6. **State overlay.** Many states have longer lookback, higher overtime
   multipliers (daily OT, double-time), and different regular-rate rules.
   Check state wage-and-hour law against the jurisdiction gate from Step 1
   and flag where state law compounds (higher cap) or replaces (different
   rate) federal. California, New York, Massachusetts, and Washington are
   the most frequent overlay hits.
7. **Attach the verify tag to the number.** Any back-pay amount produced by
   this skill carries `[verify — consult wage-and-hour counsel before
   asserting or paying]` on the line the number appears. The computation is
   specialist work; the skill is scaffolding, not opinion.

If the question is a back-pay calculation and any of these inputs are
missing (bonus breakdown, whether straight time was paid for OT hours,
willfulness posture, state jurisdiction), **ask before computing**. A
confident wrong number is the worst output this skill can produce.

### Step 3: The flag

Is this a close call? Be honest.

- If the answer is clear on the researched rule: say so. "Exempt — meets
  each element of the applicable duties test and the current salary
  threshold."
- If it's close: say so. "The duties test is borderline — this role could
  go either way. Recommend classifying as non-exempt to be safe, or getting
  a formal opinion."
- If the law is in flux: say so. "This rule has been amended recently — the
  current version takes effect [date]. Confirm effective date before relying
  on this answer."
- If you could not verify currency: say so. Do not guess.

## Output format

Conversational. This is a Q&A, not a memo.

> **Research-connector pre-flight.** Before emitting the answer, check whether a legal research connector is reachable for this session — Westlaw, CourtListener, or any firm-configured research MCP. Collect this into the reviewer note per CLAUDE.md `## Outputs`: if no connector returns results in Step 2 (or none is configured at run time), record it in the **Sources:** line of the reviewer note — e.g., `not connected — cites from training knowledge; pinpoint cites (volume/page/subsection) carry the highest fabrication risk, spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner above the output.

> **Jurisdiction assumption.** Answers apply only to the jurisdiction identified. Wage-hour rules, exemption thresholds, and final-pay timing vary materially by state and country, and many rules index or change year over year. If the employee works in another jurisdiction, or the question is answered for the default-footprint state, this answer may not apply as written.

```
**[Jurisdiction]:** [The researched rule, one paragraph, with pinpoint cite
and currency note.]

[If close call or shifting law: the flag.]

[If the answer differs in other footprint jurisdictions: one line noting that,
and whether the differences are material.]
```

> **Verify citations.** Any case, statute, regulation, or wage-order cite above was generated with AI assistance. Before relying on a cite, check it against Westlaw, CourtListener, the relevant state agency's site, or your firm's research tool for accuracy, currency, and subsequent history. Fabricated or misquoted citations in filings or formal advice have resulted in sanctions.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- State the rule from memory — every answer is grounded in a researched,
  cited primary source verified for currency.
- Make classification decisions for borderline cases. It states the rule and
  flags the close call. Human decides.
- Give a 50-state survey unless asked. Answers for the relevant
  jurisdiction(s).
- Track when the answer changes. If thresholds index or law shifts, the
  answer goes stale. Re-ask for current.

---

## /employment-legal:worker-classification

---
name: worker-classification
description: >
  Classify a proposed worker engagement — employee, IC, temp, or vendor — by
  running the applicable jurisdiction tests and flagging misclassification gaps
  between the intended arrangement and what the facts actually support.
  Prospective use only. Use when someone says "we want to bring on a
  contractor", "is this a vendor or a temp", "how should we classify this
  person", or describes a proposed working arrangement.
argument-hint: "[describe the proposed arrangement, or just start and I'll ask]"
---

# /worker-classification

Runs the applicable classification tests for the jurisdiction and flags where
the proposed arrangement doesn't match the structure you're trying to use.
Prospective only — for existing relationships, consult counsel.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, escalation table.
2. Run the full workflow below.
3. If the attorney provides details upfront, extract what's available and ask
   only about the gaps. Do not re-ask information already provided.

## Examples

```
/employment-legal:worker-classification
We want to bring on a data scientist for 6 months, working out of our
SF office, using our tools, embedded in our analytics team.
```

```
/employment-legal:worker-classification
Is our recruiter contractor arrangement okay? She works exclusively for
us, sets her own hours, uses her own laptop, project fee per placement.
```

```
/employment-legal:worker-classification
(skill will ask for details)
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

The most expensive classification decision is the one nobody made consciously.
Someone describes what they want ("a contractor"), the engagement starts, and
two years later the facts look like employment. This skill walks the applicable
tests on the proposed arrangement before it starts — and tells you when what
you're describing doesn't match the structure you're trying to use.

This skill teaches the reasoning pattern. It does not state the law. Every
test formulation, statutory citation, threshold, and carve-out must come from
current research for the applicable jurisdiction.

## Prospective-only hard gate — run BEFORE intake

**This skill analyzes a PROPOSED engagement before the work starts.** Before any substantive intake (Step 1), ask:

> Has this work already started? Is the worker currently engaged, or have they been performing work under this arrangement for any period of time (days, weeks, months, or years)?

If the answer is yes — the engagement already exists, in any form, for any duration — **STOP**. Do not proceed to Step 1 intake. Classifying an existing arrangement is not a planning exercise; it's a liability assessment with remediation implications: back pay (OT, meal/rest premiums), unpaid employer-side payroll tax, benefits eligibility that was denied, unemployment and workers' comp back-exposure, state penalties (in CA, PAGA), IRS § 530 relief analysis, and — in strict-test jurisdictions with ongoing work — the prospective exposure of letting it run another day. That analysis is privileged, led by counsel, and coupled with a remediation plan.

Output exactly this block and wait for a response:

> **Out of scope — existing arrangement.**
>
> This skill is designed to analyze a worker engagement *before it starts*, so the classification choice informs how to structure the contract and operations. You've described an arrangement that already exists. Analyzing an existing engagement retroactively is a different exercise: reclassification risk assessment coupled with remediation planning — back-pay exposure, payroll-tax back-exposure, penalty exposure, benefits exposure, IRS § 530 relief analysis, and prospective restructuring. That work should be privileged, led by an attorney, and likely coupled with outside-counsel review given the dollar and enforcement exposure.
>
> Recommended next step: escalate per your config's escalation table (for retroactive classification, this typically routes to GC + outside employment counsel). I've flagged this for escalation routing.
>
> **If you want to proceed with the prospective-style analysis anyway for planning purposes, say "proceed anyway" — but understand:**
>
> - The output is NOT a remediation plan and should not be treated as one.
> - The output does NOT scope back-pay, penalty, or payroll-tax exposure for the period already worked.
> - The output does NOT substitute for the reclassification-risk assessment that this fact pattern actually calls for.
> - The output will carry a prominent banner reflecting this scope mismatch, and the consequential-action gate will require an attorney yes before the analysis is treated as reliable.
>
> Only say "proceed anyway" if you're using this skill for forward-looking planning (e.g., "if we were structuring this fresh today, how should we think about it?") and you have a separate plan for the remediation question.

**Only proceed past this gate with an explicit `"proceed anyway"` (or equivalent user instruction). A hesitant "I guess" does not count — re-prompt. If the user proceeds anyway, prepend this banner to every output of this skill for this session:**

```
⚠️ SCOPE MISMATCH — OUT-OF-SCOPE USE
This skill analyzes prospective worker engagements. The arrangement here
already exists. This output is the prospective-style analysis the user
requested for planning purposes only — it is NOT a remediation plan, does
NOT scope existing back-pay / penalty / payroll-tax exposure, and does
NOT substitute for the reclassification-risk assessment this fact pattern
requires. The remediation question has been flagged for escalation to
counsel per your config's escalation table.
```

If the answer to "has this work already started?" is no (the engagement is genuinely prospective, not yet begun), proceed to load context.

---

## Load context

Read `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, any classification history or
prior settlements noted, escalation table, and any house classification
policy the team has recorded.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`).

## Workflow

### Step 1 — Information gathering

Ask all of the following in a single block. Do not drip questions one at a
time. Briefly explain why you're asking — attorneys answer better when they
understand what the question is testing.

> To run the right classification tests I need to understand the proposed
> arrangement in detail. Please answer as many of these as you can — the more
> complete the picture, the more accurate the analysis:
>
> **The work**
> - What will this person actually do day-to-day?
> - Is this work part of your company's core business, or peripheral to it?
>   (e.g., a software engineer at a software company = core; an IT
>   contractor at a law firm = more peripheral)
> - Is this a defined project with a clear end, or ongoing indefinite work?
> - How specialized is the skill? Does this person have expertise your team
>   doesn't?
>
> **Control**
> - Who sets their hours and schedule — them or you?
> - Where will they work — your office, their location, or either?
> - Will you direct how they do the work (methods, process, sequence), or
>   just what the end result should be?
> - Will they supervise any of your employees?
>
> **Economics**
> - How will they be paid — hourly, daily, or fixed project fee?
> - Will you provide equipment, tools, or software, or do they use their own?
> - Do they work for other companies, or will this be exclusive?
> - Will they bear any financial risk — can they profit beyond the fee, or
>   lose money on the engagement?
> - Do they have their own business entity (LLC, S-corp, sole proprietor)?
>
> **The arrangement**
> - How do you want to structure this — direct contractor, staffing agency
>   temp, or vendor/SOW (company-to-company)?
> - If staffing agency: who pays the worker — the agency or you? Who controls
>   day-to-day work?
> - Will there be a written contract? Do you have a template in mind?
> - Roughly how long is the engagement — weeks, months, over a year?
> - Will they work alongside your employees doing similar work?
>
> **Purpose(s) of the classification**
> - What legal purposes does the classification need to serve — federal
>   payroll tax, FLSA wage/hour, state wage/hour, unemployment insurance,
>   workers' compensation, benefits eligibility? Different purposes are often
>   governed by different tests, and the answers can diverge.
>
> **Jurisdiction**
> - Where will this person physically perform the work?

Wait for responses before proceeding. If the attorney can't answer certain
questions, note the gaps — they affect the analysis.

### Step 2 — Identify the applicable tests

> **Research the applicable tests before proceeding.** For the jurisdiction(s)
> and purpose(s) identified in intake, research the currently operative
> classification test(s). Jurisdictions commonly use one or more of: an ABC
> test, an economic-realities test, a common-law right-to-control test, a
> hybrid, or a purpose-specific statutory test. The test that governs for
> federal payroll tax may not be the same test that governs for state
> wage/hour, unemployment, or workers' compensation — run each purpose on its
> own track. Cite the controlling statute, regulation, or case. Note the
> effective date of each rule and whether it has been recently amended.
> Identify any carve-outs or exceptions that may apply (e.g., B2B,
> professional services, construction, referral-agency, business-to-business
> contracting relationship). Verify currency. If you are uncertain about the
> current state of the law in any jurisdiction, flag it for attorney
> verification — do not state a test you haven't confirmed.

If `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` records the company's house classification policy, apply it
first and flag any tension with the researched test.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a jurisdiction-and-purpose combination, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [jurisdiction / purpose / test]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Tag every citation — each classification test, statute, regulation, or case — with where it came from: `[Westlaw]`, `[CourtListener]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the attorney supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

### Step 3 — Apply the researched tests to the facts

For each test identified in Step 2, apply it to the intake facts. Score each
factor or prong explicitly — do not summarize. The attorney needs to see which
factors are clean and which are problems.

Use a structure like the one below, but populate the *factors* from the
researched test, not from this file:

```
Test: [name of test, per research]
Purpose: [what this test governs — federal tax / state wage-hour / UI / etc.]
Source: [pinpoint cite to statute/regulation/case]
Currency: [verified as of date]

| Factor / prong | Intake facts | Signal / pass-fail |
|---|---|---|
| [Factor 1 from researched test] | [from intake] | [direction or pass/fail] |
| [Factor 2] | [from intake] | [direction or pass/fail] |
| ...                            |                |                   |

Structure of the test:
[How the test weighs factors — e.g., a multi-factor balancing test, or a
conjunctive test where each prong must be satisfied, or a hybrid. State this
from research, not from memory.]

Result under this test:
[Employee-leaning / IC-leaning / Fails prong X / Uncertain — contested prong]
```

Repeat for each applicable test.

**Notes on contested prongs.** Some prongs of some tests are heavily contested
in case law and fact-sensitive. Identify contested prongs explicitly — do not
paper over them. The fact that a test is stated does not mean its application
to these facts is settled; flag prongs that require attorney judgment or that
have generated recent litigation in the jurisdiction.

### Step 4 — Classify and flag gaps

**The classification call**

Based on the test results, state the most accurate classification for this
proposed arrangement:

- **Employee (W-2):** Facts support employment under one or more applicable
  tests for the relevant purpose(s).
- **Independent Contractor (1099):** Facts support IC status under all
  applicable tests for the relevant purpose(s).
- **Temp via staffing agency:** Worker will be on the agency's payroll;
  company is a client — co-employment risk exists if company exercises
  day-to-day control. Research the applicable joint-employer standard if
  relevant.
- **Vendor/SOW:** Company-to-company engagement; worker is employed by the
  vendor entity — cleanest structure if facts support it.
- **Unclear / close call:** Facts cut both ways under one or more tests —
  state which test is the problem and why.

If tests give different answers for different purposes (e.g., defensible as
IC for federal tax but fails a state wage/hour test), say so explicitly and
name the controlling purpose and jurisdiction.

**The gap analysis**

This is the most important output. Compare the intended structure against what
the facts actually support:

```
Intended structure: [what they said they want]
What the facts suggest: [what the researched tests say this actually is]

Gaps — where the arrangement doesn't match the intended structure:
🔴 [Factor]: [What they described] conflicts with [intended classification]
   because [specific researched test language + cite]. This is a significant
   misclassification risk if the engagement proceeds as described.
🟡 [Factor]: [What they described] is a weaker point under [test]. Not
   disqualifying alone, but combined with other factors increases risk.
✅ [Factor]: Supports [intended classification]. No issue.
```

**Escalation trigger**

Escalate per `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` if any of the following, or any team-specific
triggers recorded in that config:
- The jurisdiction uses a strict test and the proposed work is core to the
  company's business — do not proceed without counsel review.
- Prior misclassification settlement or audit noted in the config — heightened
  scrutiny applies.
- Worker will supervise employees or have significant budget authority.
- Engagement expected to exceed 12 months with no clear project endpoint.
- Any contested prong where the outcome changes the classification.

### Step 5 — Output

> **Research-connector pre-flight.** Before emitting the analysis, check whether a legal research connector is reachable for this session — Westlaw, CourtListener, or any firm-configured research MCP. Collect this into the reviewer note per CLAUDE.md `## Outputs`: if no connector returns results in Step 2 (or none is configured at run time), record it in the **Sources:** line of the reviewer note — e.g., `not connected — cites from training knowledge; the highest-fabrication pinpoints in classification analyses are ABC-test codifications, state carve-out subsections (e.g., CA Lab. Code §§ 2775/2776/2783), element counts in B2B exemptions, and purpose-specific test selection — spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner above the output.

> **Jurisdiction assumption.** This analysis applies the tests operative in the jurisdiction(s) identified in intake. Classification rules vary materially by state and country, and the test that governs for one purpose (e.g., federal payroll tax) often differs from the test that governs another (e.g., state wage/hour). If the work will be performed in a jurisdiction not analyzed here, or if a new purpose is added later, this analysis may not apply as written.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Worker Classification Analysis
**Proposed arrangement:** [what they described]
**Jurisdiction:** [state/country]
**Purpose(s):** [federal tax / state wage-hour / UI / WC / benefits]
**Tests applied:** [list, each with pinpoint cite and currency date]

---

### Bottom line

[Can you proceed / Need to fix X first / Stop — one-sentence why]

---

### Classification

**Closest classification:** [Employee / IC / Temp via agency / Vendor-SOW / Unclear]

[One paragraph summary of why — test results in plain language, tied to the
cited sources.]

---

### Test results

#### [Test name — per research]
Purpose: [...] | Source: [...] | Currency: [...]
[Scored table from Step 3]
**Result:** [Employee-leaning / IC-leaning / Fails prong X / Mixed]

#### [Additional researched tests — repeat the block]

---

### Gap analysis

[Flags as structured in Step 4 — 🔴 significant risks, 🟡 weaker points,
✅ clean factors]

---

### Escalation

[None needed | Escalate to [name] before proceeding — [reason]]

---

### Next steps

[If IC viable: "Proceed — ensure the written agreement reflects the terms that
support IC status under the researched test."]
[If gaps exist: "Address the following before using IC structure: [list]"]
[If agency/vendor is cleaner: "Consider restructuring as [agency/SOW] — here's
why it's cleaner for this fact pattern."]
[If escalation needed: "Do not proceed until counsel reviews the [specific
issue]."]
[If employee confirmed: "Classification confirmed as W-2 employee — run
`/employment-legal:hiring-review` to review the offer letter, restrictive
covenants, and jurisdiction-specific requirements."]
[If IC confirmed: "Classification confirmed as independent contractor — no
offer letter review needed. Ensure the written agreement reflects IC-supporting
terms before the engagement starts."]
[If agency/vendor: "Engagement should be structured through [agency/vendor
entity] — coordinate with them on worker agreement. No `/hiring-review` needed."]
```

## Consequential-action gate (classify a worker)

**Before producing a "Proceed as IC / employee / agency / vendor" final recommendation:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Classifying a worker has legal consequences — misclassification exposes the company to back wages, taxes, benefits, penalties, and private-action risk, and in several states is strict-liability. Have you reviewed this classification call with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - The arrangement (work, control, economics, structure) as described
> - Jurisdiction and which tests were applied
> - Test-by-test results with cites and currency
> - Gap analysis (🔴 / 🟡 / ✅) with the weak prongs called out
> - Open questions and what's unresolved
> - What could go wrong (the misclassification theory this arrangement most likely fails on; prior-audit/settlement overlay if any)
> - What to ask the attorney (is IC viable here; would restructuring through an agency or vendor remove the risk; what contract terms do we need to support the classification)
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent) for a referral service.

Do not produce a final "IC viable" / "use this classification" output past this gate without an explicit yes. A marked-DRAFT analysis for attorney review is fine.

---

## What this skill does NOT do

- Analyze an existing relationship retroactively — this is prospective only.
- Draft the contractor agreement or SOW.
- Advise on remediation if misclassification has already occurred.
- State the law for any jurisdiction on its own — every test, factor, and
  carve-out must come from verified current research.
- Substitute for outside counsel on close calls — strict-test jurisdictions,
  contested prongs, and prior-audit situations should always get a human
  review before the engagement starts.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

---

