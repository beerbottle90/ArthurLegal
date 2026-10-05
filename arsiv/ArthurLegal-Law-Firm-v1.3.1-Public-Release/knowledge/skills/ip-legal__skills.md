# ip-legal - Skill Referans Kitapcigi

> Alan: Fikri sinai haklar - marka, patent, OSS, takedown
> Toplam skill: 12
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /ip-legal:cease-desist (501 satir)
- /ip-legal:clearance (505 satir)
- /ip-legal:cold-start-interview (479 satir)
- /ip-legal:customize (103 satir)
- /ip-legal:fto-triage (537 satir)
- /ip-legal:infringement-triage (628 satir)
- /ip-legal:invention-intake (472 satir)
- /ip-legal:ip-clause-review (286 satir)
- /ip-legal:matter-workspace (184 satir)
- /ip-legal:oss-review (283 satir)
- /ip-legal:portfolio (539 satir)
- /ip-legal:takedown (447 satir)

---

## /ip-legal:cease-desist

---
name: cease-desist
description: >
  Draft a cease-and-desist letter (send mode) or triage one you received
  (receive mode). Use when asserting your rights against an infringer with a
  demand letter calibrated to your enforcement posture, or when an incoming
  C&D needs triage into a structured options memo with a recommendation.
argument-hint: "<--send | --receive> [context, counterparty, or path to incoming letter]"
---

# /cease-desist

Two modes. Pick one:

- `/ip-legal:cease-desist --send` — draft a cease-and-desist letter calibrated to your enforcement posture. Loud gate runs before delivery.
- `/ip-legal:cease-desist --receive` — triage a C&D someone sent you. Produces an options memo with a recommendation.

## Instructions

1. **Read the practice profile.** Load `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it contains `[PLACEHOLDER]` markers or does not exist, stop and say: "This plugin needs setup before it can give you useful output. Run `/ip-legal:cold-start-interview` — the C&D skill depends on your enforcement posture, approval matrix, and practice-area mix, none of which are configured yet."

2. **Check matter workspaces.** Per `## Matter workspaces`: if `Enabled` is `✗`, skip — skills use practice-level context. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`."

3. **Dispatch on `$ARGUMENTS`:**
   - If `--send` is present: run send mode (below). Walk through identify-the-right, identify-the-conduct, identify-the-relationship, identify-the-demand, calibrate-to-posture, draft, and the pre-delivery gate.
   - If `--receive` is present: run receive mode (below). Ask for the incoming letter (path or pasted text), then assess, identify exposure, present options, and write the triage memo.
   - If neither flag is present: ask once — "Are we sending a cease-and-desist (you're asserting) or triaging one we received (you're defending)?" — and then dispatch.

4. **Respect the gate.** In send mode, the loud gate runs before any final draft is written to disk. Do not skip it.

5. **Respect the approval matrix.** Pull the approver for the C&D row from `## Enforcement posture → Approval matrix`. Pull automatic escalations. Surface both in the gate; do not smother them.

6. **Hand off where appropriate.** In receive mode, if the recommendation is to respond firmly, offer to chain into `/ip-legal:cease-desist --send` pre-populated with the response context. If the recommendation is to pre-empt with a DJ action or TTAB cancellation, escalate to outside counsel per the practice profile's IP litigation row — do not draft.

## Examples

```
/ip-legal:cease-desist --send
/ip-legal:cease-desist --receive ~/Downloads/incoming-cd-acme.pdf
/ip-legal:cease-desist
```

## Notes

- The outgoing C&D does not carry the work-product header. The internal draft, the pre-send brief, and the triage memo do.
- Trademark rights are territorial; the draft assumes the jurisdictions declared in your practice profile's `Registered in:` footprint. If the conduct or counterparty is somewhere else, flag before drafting.
- Every `[CITE:___]` is unverified until a citator run. Source attribution tags stay on the draft.
- Non-lawyer users get a one-page brief for the attorney conversation before the gate clears.

---

## Purpose

A cease-and-desist letter asserts a legal right and demands that someone stop doing something. It is one of the most consequential letters an IP practice sends or receives. Sending one is a first step toward litigation — recipients can file a declaratory judgment action in a forum of their choosing, and overbroad or bad-faith assertions can be used against the sender. Receiving one starts a clock and forces a decision. This skill handles both sides with the guardrails the decision deserves.

Two modes:

- `--send` — you are asserting. Draft a C&D calibrated to the posture, gate before delivery.
- `--receive` — you are defending. Triage the incoming letter, produce an options memo, route to matter creation if warranted.

If the user does not pass a flag, ask once: "Are we sending a cease-and-desist (you're asserting) or triaging one we received (you're defending)?"

> **External deliverable (send mode):** the drafted C&D is sent to counterparty. Do NOT include the `PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT` header on the outgoing letter. Internal drafts, pre-send briefs, and triage memos keep the header per plugin config `## Outputs`.

## Jurisdiction assumption

Trademark rights are territorial — a US registration does not travel. Copyright is Berne-multilateral but enforcement is jurisdiction-specific, and statutory remedies (including US §504 statutory damages) turn on local law. This skill assumes the jurisdiction declared in the matter or the practice profile's `Registered in:` footprint. If the infringing conduct, counterparty, or forum is somewhere else, flag it — the draft may not apply as written.

## Load context

- `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → `## Enforcement posture` (posture, C&D triggers, soft-letter criteria, approval matrix, automatic escalations), `## IP practice profile` (practice area mix, registered jurisdictions, outside counsel roster), `## Outputs` (work-product header, role), `## Who's using this` (role — lawyer vs. non-lawyer)
- Any C&D template or enforcement playbook referenced in the practice profile's seed documents — read it, match the structure
- **Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip matter machinery — skills use practice-level context. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific overrides (e.g., posture override, approver override). Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

## Send mode — drafting the C&D

### Step 1: Identify the right

Ask, in one batch:

> Which IP right are we asserting?
>
> - **Trademark** — is it registered? Where (USPTO, EUIPO, UKIPO, national)? Reg number and class(es)? Or common-law-only (first-use date, geographic scope)?
> - **Copyright** — is it registered? Title, registration number, date? Or unregistered (note: US suits require registration for filed claims; statutory damages and fees require pre-infringement registration)?
> - **Both** — identify each.

Record each right. Registered rights get cited by number. Common-law rights get the first-use evidence paragraph. Unregistered copyrights get a flag: "We may not be able to file suit on an unregistered US copyright without registering first — `[SME VERIFY]` before the letter threatens litigation."

### Step 2: Identify the conduct

> Describe the infringing conduct in specifics, not adjectives:
>
> - **Who** is doing it — entity name, individual, platform handle?
> - **What** — the accused mark, the accused copy, the accused product? Attach or describe samples.
> - **Where** — website URL, marketplace listing, physical retail, social media?
> - **Since when** — date first observed, date of the earliest use you can document?
> - **Evidence** — screenshots, receipts, watch-service hit, customer confusion reports?

Facts go in specific. "You sold product X on [URL] bearing the mark [Y] on [date]" beats "You have been infringing our rights." Adjectives tell on a thin record.

### Step 3: Identify the relationship

> What's the relationship between us and the recipient?
>
> - **Competitor** (direct or adjacent) — standard posture applies
> - **Reseller / channel partner** — tone adjusts; consider the soft-letter path
> - **Former licensee / ex-employee / former partner** — contract provisions likely apply; cite them
> - **Stranger / random infringer** — standard
> - **Current customer / partner** — automatic escalation per practice profile; flag before drafting

This changes tone, approver, and whether to draft at all without escalation.

### Step 4: Identify the demand

> What does the client actually want?
>
> - **Stop** — cease the infringing use
> - **Account** — report sales, profits, volumes (for damages baseline)
> - **Destroy** — destroy or recall infringing inventory
> - **Damages** — monetary settlement
> - **Transfer / assign** — transfer the domain, hand over the account, assign the accused mark or copyright
> - **Public correction** — takedown of offending content, public statement
> - **Confirm in writing** — compliance undertaking by a date

Pick the actual remedies. The demand must be proportionate to the harm — an overbroad demand is evidence of bad faith if the matter is ever litigated.

**Channel-takedown parallel path (marketplace infringement).** If the accused conduct is on a marketplace (Amazon, Etsy, eBay, Alibaba, TikTok Shop, AliExpress, Walmart Marketplace, Shopify-hosted storefronts), flag the platform's brand-protection / IP-infringement reporting path as a faster, cheaper parallel track that does not require a C&D or litigation:

- **Amazon Brand Registry** (trademark and copyright takedown, counterfeit removal)
- **Etsy IP Infringement reporting** (trademark / copyright / patent forms)
- **eBay VeRO** (Verified Rights Owner program)
- **Alibaba IPP** (IP Protection Platform)
- **TikTok Shop IP Protection**
- **Shopify DMCA / trademark reporting**

A marketplace takedown often resolves in days; a C&D gives the infringer time to sell through inventory while negotiating. The two paths are not mutually exclusive — recommend filing both when the conduct is marketplace-based, with the C&D covering off-platform conduct (DTC site, wholesale, social, physical retail) that the platform report cannot reach. Note in the pre-send brief whether the parallel-path has been filed, is queued, or is declined (and why).

### Step 5: Calibrate to posture

Read `## Enforcement posture` → `Default posture:` and apply:

- **Aggressive** — firm letter, short deadline (often 7–14 days), explicit consequence language (litigation, statutory damages, fees, injunctive relief), no settlement softening
- **Measured** — firm but professional, standard deadline (14–30 days), consequences noted without theatrics, openness to discussion if they respond
- **Conservative** — soft letter framing, longer deadline or no hard deadline, "we'd like to discuss" opening, consequence language muted or absent

Also read `When we send a C&D`, `When we send a soft letter first`, and `When we just file`. If the facts suggest this should be a soft letter or a direct filing per the practice profile, flag it before drafting: "Per your enforcement posture, this pattern matches [soft letter / filing]. Do you still want a C&D, or would you prefer [alternative]?"

Matter-level overrides in `matter.md` beat the practice default.

### Step 5.5: Counterparty diligence — REQUIRED PRECONDITION

**Before drafting, run counterparty diligence and present the results to the user.** This is not conditional on "if the counterparty looks big." Every C&D assertion carries DJ / fee-shifting / bad-faith exposure calibrated to *who* the recipient is. The skill does not draft a C&D until the user has seen the diligence and confirmed they still want to pick this fight.

Collect and present — in one block, for user sign-off — the following:

- **Legal entity** — exact corporate name, state/country of formation, registered agent, any `d/b/a` aliases. USPTO / EUIPO ownership records; state Secretary of State business search; public company filings if any. Flag `[SME VERIFY]` if the source is unconfirmed.
- **Size and resources** — approximate headcount, revenue band if publicly known, funding if a startup, parent company if a subsidiary. Public sources (LinkedIn headcount, press, Crunchbase, SEC filings). Flag honestly if size can't be determined.
- **IP portfolio** — do they hold registered marks, patents, or copyrights in adjacent classes? A counterparty with its own IP portfolio is more likely to (a) understand the posture, (b) counter-assert, and (c) file DJ. USPTO TESS / TSDR quick search on the accused entity and affiliates.
- **Litigation history** — PACER / Court Listener quick pass for prior IP litigation as plaintiff or defendant. A repeat litigant or DJ-happy counterparty changes the calculus. Flag any prior C&D campaigns in the industry.
- **Counsel** — do they have known outside IP counsel? Firm, lead partner if identifiable from prior filings. "No counsel on file" is itself a data point.
- **DJ-plaintiff risk posture** — given size, IP portfolio, litigation history, counsel, and forum: is this a counterparty likely to welcome a C&D as an invitation to file DJ in a forum of their choosing? Flag high / medium / low with a one-sentence reason.
- **Relationship risk** — are we a customer of theirs, do we share investors, are they a potential acquirer or partner? "Not a customer" confirmation pulled from the practice profile; anything else flagged.

Present this as a short memo in-chat BEFORE the draft:

```
## Counterparty diligence — [Entity Name]

- **Entity:** [name, state of formation, parent if any]
- **Size:** [headcount band, revenue band, funding stage] — [source, `[SME VERIFY]` where applicable]
- **IP portfolio:** [registered marks / patents / copyrights in adjacent classes — or "none found"]
- **Litigation history:** [prior IP cases as plaintiff or defendant — or "none found in quick pass"]
- **Counsel:** [known outside IP counsel — or "none identified"]
- **DJ-plaintiff risk:** [high / medium / low — reasoning]
- **Relationship risk:** [any customer / investor / partner / acquirer overlap — or "none identified"]

**Automatic escalations this triggers** (per practice profile `## Enforcement posture` → Automatic escalations):
- [list each trigger that this diligence surfaces]

**Confirm before I draft:**
- Do you want to proceed with a C&D against this counterparty, given the diligence above?
- Any of the automatic escalations applicable? If yes, the approver named in the profile signs off before drafting, not after.
```

**Do not proceed to Step 6 (Draft) until the user has engaged with the diligence block.** A blank "ok" is worse than no confirmation — push back: "Before I draft — anything in the diligence that changes the calculus? Size, prior litigation, their counsel, relationship?"

If diligence surfaces anything in the practice profile's automatic-escalation list (customer, bigger counterparty, patent matter, press-attracting, etc.), route to the named approver per the profile — do not draft on the reviewer's behalf until the approver has signed off on going forward.

If critical diligence items cannot be answered (e.g., entity cannot be confirmed, size is unknown and the counterparty is not on any public register), say so and flag: "I can't confirm [entity / size / counsel] from available sources. Do you have this, or should we pause until a paralegal or OC runs the confirmation?"

### Step 6: Draft

Draft structure:

1. **Sender / letterhead and date**
2. **Recipient block**
3. **Re: line** — concise, does not reveal privileged strategy. `Re: Unauthorized use of [MARK] (US Reg. No. [•])`
4. **Opening** — identify the sender, the right, the registration (if any), and the fact of the letter
5. **The right** — trademark: reg number, class, first-use date, registration status; copyright: registration number, title, year, work description; common-law: first-use date, geographic scope, evidence of acquired distinctiveness
6. **The infringing conduct** — specific: who, what, where, when, evidence
7. **The legal basis** — `[CITE: Lanham Act §32 / §43(a) / 17 U.S.C. §501 / state UCL / contract §]` as applicable
8. **The demand** — numbered, specific, proportionate
9. **The deadline** — calendar date, method of confirmation
10. **Consequences of non-compliance** — calibrated to posture
11. **Preservation demand** — documents, communications, metadata related to the accused conduct
12. **Reservation of rights** — "without waiver of any claims or remedies, whether at law or in equity"
13. **Signature block** — approver per practice profile

**Drafting rules:**

- **Specificity over adjectives.** Dates, URLs, reg numbers, samples. Adjectives are a draftsperson's tell that the facts are thin.
- **No overbroad assertions.** If the mark is registered in one class and the accused use is in a different class, say so — don't pretend the registration covers both. Overbroad C&Ds are evidence of bad faith and can support §43(a)(1)(B) or Rule 11 exposure.
- **Citations as placeholders unless verified.** `[CITE: Lanham Act §32, 15 U.S.C. §1114]` stays as a placeholder unless the user provided the cite or a research tool returned it. Tag every citation with source — `[Westlaw]`, `[user provided]`, `[model knowledge — verify]`, `[web search — verify]`. Never strip the tags.
- **Consequence language matches posture.** Aggressive → specific relief threatened (injunction, statutory damages under 15 U.S.C. §1117 / 17 U.S.C. §504, attorneys' fees). Measured → "we reserve all rights." Conservative → "we'd like to discuss before considering further steps."
- **Jurisdiction-specific hooks** — if US, watch for Anti-Cybersquatting (15 U.S.C. §1125(d)) for domain matters, §43(a) for unregistered marks, §504(c) for pre-registration timing. Non-US: flag the forum and note the draft may need foreign associate review.

### Step 7: The loud gate before delivery

Before presenting the draft in-chat or writing the .docx, display this gate verbatim. **The user must engage with it** — a blank acknowledgment is worse than no gate.

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS DRAFT GOES ANYWHERE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  This is a draft for attorney review — not a letter to      │
│  send. Sending a cease-and-desist letter is an assertion    │
│  of legal rights with real consequences:                    │
│                                                             │
│  • It can trigger a declaratory judgment action in a        │
│    jurisdiction of the recipient's choosing. A well-funded  │
│    recipient can use a C&D as an invitation to pick a       │
│    hostile forum.                                           │
│                                                             │
│  • Overbroad or bad-faith assertions can be used against    │
│    the sender — §43(a)(1)(B) claims, Rule 11 sanctions,     │
│    attorneys' fees under the Lanham Act / Copyright Act.    │
│                                                             │
│  • It starts a dispute that may not settle cheaply.         │
│                                                             │
│  Confirm before the letter leaves:                          │
│                                                             │
│    1. The rights asserted are valid — registered (pulled    │
│       from the register, not assumed) or solidly common     │
│       law with evidence of acquired distinctiveness.        │
│    2. The claim is colorable — a reasonable practitioner    │
│       would make it on these facts.                         │
│    3. The demand is proportionate — we are asking for       │
│       relief the conduct warrants, not everything.          │
│    4. Whoever has authority to start a fight has approved.  │
│    5. Counterparty diligence (Step 5.5) was presented       │
│       and confirmed — entity, size, IP portfolio, prior     │
│       litigation, counsel, DJ-plaintiff risk, and           │
│       relationship risk. Not conditional. Required.         │
│                                                             │
│  Approver per your practice profile: [approver name/role    │
│  from Enforcement posture → Approval matrix → C&D row]      │
│                                                             │
│  Automatic escalations that apply here: [list any from the  │
│  practice profile that this matter triggers — customer,     │
│  bigger counterparty, patent, press-attracting, etc. —      │
│  surfaced in Step 5.5 diligence]                            │
│                                                             │
│  Parallel-path status (marketplace conduct): [filed /       │
│  queued / declined — from Step 4. "Not applicable" if       │
│  conduct is not on a marketplace.]                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer (per `## Who's using this`), add:

> Sending a C&D has legal consequences that go beyond the recipient's response — it is an affirmative assertion of rights that can be held against you. Have you reviewed this with an attorney? If not, here's a brief to bring to them: [generate a 1-page summary: parties, rights asserted, infringing conduct, demand, posture, risks flagged above, what could go wrong, specific questions for the attorney].
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent). The ABA IP section and state IP associations (US), CIPA/ITMA (UK), and equivalent bodies elsewhere maintain referral rosters for trademark and copyright practitioners.

Do not write the .docx or mark the draft as ready without explicit engagement with the gate.

### Step 8: Output

**Primary:** `<matter-folder>/cease-desist/<slug>/draft-v<N>.docx` (or `cease-desist/<slug>/draft-v<N>.docx` at practice level). Use the `docx` skill. Letter-formatted per the draft structure above. Strip the work-product header from the outgoing letter.

**In-chat:** show the draft as plain text for review before writing the .docx. Iterate before committing to disk.

**Reviewer-facing closing note** (appended to the in-chat preview only, stripped from the .docx):

> This is a draft cease-and-desist letter for attorney review, not a letter ready to send. Sending it is an assertion of legal rights with the consequences described in the pre-delivery gate. A licensed attorney reviews, edits, and takes professional responsibility before sending. Do not send this draft unreviewed.

**Citation verification.** Every `[CITE:___]` and every cite carried from a template or provided authority is unverified until run through a citator. Before sending, verify each cite is good law on a legal research platform. Fabricated or misquoted cites in sent assertion letters are professional responsibility exposure. Preserve the source-attribution tags — `[Westlaw]`, `[CourtListener]`, `[Descrybe]`, `[user provided]`, `[model knowledge — verify]`, `[web search — verify]` — tags flagged `verify` get checked first.

**No silent supplement.** If a configured research tool returns few or no results for an authority the draft needs, report what was found and stop. Do NOT backfill from web search or model knowledge without asking. Present options — broaden the query, try a different tool, accept web search with tags, leave the placeholder — and let the user decide.

**Post-send checklist.** After the draft is approved, write `<matter-folder>/cease-desist/<slug>/checklist.md` with: final read by approver, all `[VERIFY]` resolved, all `[CITE]` filled and verified, privilege markings stripped from the outgoing letter, approver signed, delivery method executed, proof of delivery retained, compliance deadline calendared, escalation plan if no response, matter created in `matters/` if not already.

## Receive mode — triaging the incoming C&D

### Step 1: Read the letter

Extract:

- **Sender** — entity, signer, outside counsel if any
- **Recipient** — which of our entities/people
- **Delivery method and date**
- **Asserted right** — trademark (reg number? jurisdiction?), copyright (registered? title?), both, something else
- **Alleged conduct** — their version of what we're doing
- **Legal basis** — statutes, contract provisions, theories cited
- **Demand** — what they want; is the deadline stated?
- **Threats** — what they say they'll do
- **Tone** — firm / soft / scorched-earth; counsel signature usually signals seriousness

### Step 2: Assess the assertion

Not a legal opinion — a structured read:

- **Rights validity.** Are the asserted registrations real and active? (Check USPTO TSDR, EUIPO eSearch, Copyright Office records — flag any that look dormant or not in force.) For common-law claims, what evidence do they actually cite?
- **Plausibility of confusion / similarity / infringement.** On the facts as alleged, is this a colorable claim or is it stretching? For trademark: likelihood of confusion turns on multi-factor tests (Polaroid / AMF / Sleekcraft depending on circuit — `[SME VERIFY]` the forum's test). For copyright: access + substantial similarity. Flag where the claim looks weakest.
- **Overbreadth.** Are they demanding more than the conduct warrants? (They want the mark transferred when registration would at most cover re-labeling? They want all sales when only one channel touched the right?) Overbroad demands weaken leverage and strengthen a §43(a)(1)(B) / unclean-hands counter.
- **Timing.** Laches, statute of limitations, registration timing (for US copyright statutory damages) — flag any date issues on the face of the letter.
- **Forum.** Where would they sue? Is the forum contractually fixed (most unlikely in a stranger IP dispute)? Is there a DJ opportunity for us?

### Step 3: Assess our exposure

- **Are we actually infringing?** Honest look. What does the record show?
- **Could we stop easily?** Cost of compliance vs. cost of fight.
- **Is the sender a troll or a real claimant?** Repeat-plaintiff? Known-willing-to-fight? Recent C&D campaign on comparable use? Check public dockets if time permits.
- **What's at stake beyond this dispute?** Brand equity, customer relationships, precedent for similar inbound C&Ds.

### Step 4: Options

Present 4-5 options with tradeoffs:

**A — Comply quickly**
- When: the claim is colorable, compliance is cheap, and the fight isn't worth it
- Tradeoff: establishes a concession they may point to later; may embolden future assertions
- Next step: confirm compliance in writing (narrow), do not concede broader theory

**B — Negotiate**
- When: there's a middle-ground business deal (license, coexistence, rebranding timeline) that resolves it
- Tradeoff: commits time; requires care on settlement-communication posture (FRE 408 or state equivalent; protection attaches from substance and context, not labeling alone)
- Next step: holding letter + opening negotiation track

**C — Respond firmly (reject)**
- When: their claim is weak, overbroad, or factually wrong; we want to close this down without litigating
- Tradeoff: locks in a position; if the claim is in fact colorable, our response becomes an exhibit
- Next step: draft a response letter — consider running it through `/ip-legal:cease-desist --send` reframed as a response

**D — Ignore (and preserve)**
- When: the claim is frivolous, the sender has no apparent capacity to sue, the deadline has no legal consequence
- Tradeoff: silence can be used as non-denial in some contexts; legal hold required regardless; risk that filing follows
- Next step: issue legal hold via matter-level process; log the demand; move on

**E — Pre-empt with a DJ action or cancellation**
- When: we face real business uncertainty, the claim is weak, and we benefit from our own forum
- Tradeoff: we go on offense; budget and leadership sign-off required; now there's a lawsuit
- Next step: escalate to outside counsel per practice profile, do not draft

**F — File to cancel their mark (TTAB) or invalidate their copyright registration**
- When: their rights themselves are vulnerable and we want to take the instrument off the board
- Tradeoff: slow, expensive, public; separate from the dispute itself
- Next step: escalate to outside counsel

Recommend one with two sentences of rationale. Be specific about why.

### Step 5: Deadline triage

- Their stated deadline — note it, but it doesn't legally bind us (unless a specific statute gives it teeth).
- Our internal decision deadline — typically stated deadline minus enough time to draft, review, and approve a response. Flag it on the calendar.
- Legal deadlines — statute of limitations on any underlying claim, contractual cure periods, forum-specific timelines.

Ignoring a stated deadline entirely is a choice, not a default. Note that filing usually follows silence, not the deadline date.

### Step 6: Write the triage memo

Output: `<matter-folder>/cease-desist/inbound/<slug>/triage.md` (or at practice level if matter workspaces are off).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

[PRIVILEGE INHERITANCE BLOCK — pick by role and matter type; see guidance below the template]

# C&D Received — Triage

> **READ FOR TRIAGE, NOT OPINION.** This is an intake scan and options analysis — not a legal merit opinion. The assessment below is a structured read to support counsel's decision on routing and response. Every cited statute, rule, or case is flagged for SME verification; every merit call is the counsel's, not this skill's.

**Slug:** [slug]
**Received:** [YYYY-MM-DD]
**Received by:** [entity / person]
**Incoming file:** [path]

## The assertion

**Sender:** [entity, signer, counsel]
**Asserted right:** [trademark / copyright / both — with specifics, reg numbers, jurisdictions]
**Alleged conduct:** [their version, one paragraph]
**Demand:** [list — specific asks]
**Their stated deadline:** [date]
**Tone:** [firm / soft / scorched-earth]

## Rights validity

[Registrations as asserted — `[SME VERIFY]` against the register; common-law claims evaluated against the evidence cited]

## Legal basis cited

[Each citation inline-tagged with `[SME VERIFY: applicability / currency / jurisdiction]` and source `[Westlaw / user provided / model knowledge — verify / web search — verify]`. Do not rely on any citation here without independent check.]

## Plausibility assessment

- **Confusion / similarity / infringement on the facts:** [read]
- **Overbreadth:** [read]
- **Timing issues (laches, SoL, registration timing):** [read]
- **Forum:** [their likely forum; DJ opportunity]

## Our exposure

- **Actually infringing?** [honest look]
- **Cost of compliance vs. cost of fight:** [read]
- **Sender credibility:** [troll / real claimant / repeat plaintiff — with any public-docket evidence]
- **Collateral stakes:** [brand, customers, precedent]

**Triage rating:** [substantial / debatable / weak / frivolous] — *structured read for routing, not a merit opinion; `[SME VERIFY]`*

## Options

### A. Comply quickly
[Rationale, tradeoffs, next step]

### B. Negotiate
[Rationale, tradeoffs, next step]

### C. Respond firmly
[Rationale, tradeoffs, next step]

### D. Ignore + preserve
[Rationale, tradeoffs, next step]

### E. Pre-empt (DJ)
[Rationale, tradeoffs, next step]

### F. File to cancel / invalidate
[Rationale, tradeoffs, next step]

**Recommendation:** [A/B/C/D/E/F] — [two sentences why] — `[SME VERIFY: counsel to confirm before executing]`

## Deadlines

- **Their stated deadline:** [date]
- **Our internal decision deadline:** [date]
- **Legal deadlines on any underlying claim:** [SoL, cure, procedural — with dates]

## Immediate actions

- [ ] Legal hold issued — [yes/no]
- [ ] Matter created in log — [yes/no/TBD]
- [ ] Counsel assigned — [who]
- [ ] Insurance tendered — [yes/no/N-A]
- [ ] Internal escalation — [who/when]
```

**Privilege inheritance block — pick by role and matter type.** Read `## Who's using this` (Role) in the plugin config and the matter type (trademark / copyright / patent / OSS / other). This triage records a first-pass merit read on an adverse assertion; whether it's actually privileged depends on who prepared it and what it's about. Getting this wrong in either direction is harmful — a false "privileged" marking creates a discoverable admission that reads as a concession; under-marking a genuinely privileged memo can waive the protection. Insert exactly one of the following:

- **Role = Lawyer / legal professional:**
  > **Privilege inheritance.** This triage records our first-pass merit read and response posture on an adverse assertion. It is attorney-client and/or work-product material. Do not forward, attach to an insurance tender without scrubbing, or share with counterparty. Store with privileged matter material and mark per house privilege conventions.

- **Role = Registered patent agent, matter is a patent matter before the USPTO:**
  > **Privilege (patent agent-client).** This triage is privileged under the federal patent agent-client privilege recognized in *In re Queen's University at Kingston*, 820 F.3d 1287 (Fed. Cir. 2016), because it relates to a matter reasonably necessary and incident to the prosecution of patents before the USPTO. That privilege is narrow: it does not extend to matters outside USPTO practice. Do not forward, attach to an insurance tender without scrubbing, or share with counterparty. Bring to supervising counsel for matter-specific privilege decisions.

- **Role = Registered patent agent, matter is NOT a patent matter** (trademark, copyright, OSS, trade secret, contract, or anything else outside USPTO practice):
  > **CONFIDENTIAL — NOT PRIVILEGED.** This triage is not privileged because a registered patent agent's privilege is limited to patent prosecution before the USPTO (*In re Queen's University at Kingston*, 820 F.3d 1287 (Fed. Cir. 2016)). A trademark, copyright, OSS, or other non-patent matter falls outside that privilege. Treat this document as confidential, store it with care, bring it to counsel, and let counsel mark it. Do not forward it as a privileged document.

- **Role = Non-lawyer and not a registered patent agent:**
  > **CONFIDENTIAL — NOT PRIVILEGED.** This document is not privileged unless and until reviewed by a licensed attorney. Treat it as confidential; do not forward to anyone outside the legal review chain; bring it to counsel and let counsel mark it. Forwarding this document as "privileged" before an attorney reviews it does not make it so and can harm you if the matter becomes contested.

Close the in-chat presentation with this guardrail verbatim:

> This is a triage memo, not advice. The strength assessment above is a first read based on the letter alone — it does not account for facts you haven't told me, registrations I can't verify, or jurisdictional issues. An attorney evaluates before you respond, decide to ignore, or commit to a path.

If the user is a non-lawyer, add the "find-an-attorney" routing paragraph from send mode.

### Step 7: Hand off

Based on the recommendation and user confirmation:

- Respond firmly → hand off to `/ip-legal:cease-desist --send` with context pre-populated as a response letter (this triggers the send-mode gate anew).
- Negotiate → start a holding letter / negotiation track in the matter.
- Pre-empt or file to cancel → escalate to outside counsel per the practice profile's IP litigation row; do not draft.
- Matter creation → if there isn't one and the matter is material, offer `/ip-legal:matter-workspace new <slug>` pre-populated.
- Comply / ignore → log the decision in the matter history; issue or confirm the legal hold; close the triage record.

## Decision posture

Per `## Decision posture on subjective legal calls` in the practice profile: when uncertain whether there is infringement, whether a mark is confusingly similar, whether a work is substantially similar, whether a claim is colorable, or whether sending is safe — do not silently decide it's fine. Flag for attorney review, surface the factors cutting both ways, note the uncertainty. Sending a C&D on an assumption is a one-way door; surfacing doubt is a two-way door.

## What this skill does not do

- **Send the letter.** Drafting only. The user sends, after approval.
- **Research citations.** Placeholders stay as placeholders unless the user provides authorities or a connected research tool returns them. Inventing cites is professional responsibility exposure.
- **Bypass the gate.** The send-mode gate runs every time. Even with an `--skip-gate` flag (none is provided), the skill would log the skip in the draft file.
- **Decide merit definitively on the receive side.** The rating is a structured read for routing; a formal merit opinion lives with counsel.
- **Validate the sender's cited law.** Flags for the user; does not autonomously call a claim valid or invalid.
- **Make the matter-creation call.** Surfaces the recommendation; user decides.

---

## /ip-legal:clearance

---
name: clearance
description: >
  Trademark clearance first pass — knockout + similar-marks check producing a
  flag list, not a clearance opinion. Use when a new mark is proposed, when
  asked whether a mark is available or to run a knockout search, or when
  assessing likelihood-of-confusion factors before a full professional search.
  This skill never concludes a mark is clear.
argument-hint: "[describe the proposed mark, goods/services, and jurisdictions — or just the mark and I'll ask]"
---

# /clearance

**This is a triage, not a clearance opinion.** A trademark clearance opinion
requires a full professional search and registered trademark counsel's
judgment. A "no obvious conflicts" result means the triage
didn't find anything — it does not mean the mark is clear. Clients have been
sued over marks that passed a knockout search.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal:cold-start-interview`.
2. Follow the workflow below.
3. Run intake (mark, goods/services, classes, jurisdictions, visual/stylization).
4. Knockout check for intrinsic bars — generic, descriptive, deceptive,
   geographic, surname, false connection, prohibited matter, functional.
5. Similar-marks search against what's connected (Solve Intelligence, CourtListener, Descrybe, or whatever MCP is available). If nothing is
   connected, say so in the output and proceed with the factor analysis only.
6. Walk the applicable circuit's likelihood-of-confusion factors — du Pont /
   Polaroid / Sleekcraft / other. Flag each; never conclude.
7. Write the triage memo to the matter folder (if a matter is active) or the
   practice outputs folder. Apply the work-product header per role.
8. End with recommended next steps and the non-lawyer gate if the role is
   non-lawyer.

This skill never concludes a mark is clear. If uncertain, flag — the attorney
decides.

## Examples

```
/ip-legal:clearance "APEXLEAF for an outdoor apparel line, planned launch US + EU"
```

```
/ip-legal:clearance
```

(And the skill will ask for the mark, goods, classes, and jurisdictions.)

---

## THIS IS A FIRST PASS, NOT A CLEARANCE OPINION

**Say this at the top of every output. Do not drop it. Do not soften it.**

> **This is a first pass, not a clearance opinion.** A trademark clearance opinion
> requires a full professional search (TESS, state registries, common law sources,
> international registries, domain and social, trade dress and design marks where
> relevant) and attorney judgment on likelihood of confusion, which depends on
> factors a structured triage cannot fully assess. A "no obvious conflicts" result
> from this skill means the triage didn't find anything — it does not mean the
> mark is clear. Clients have been sued over marks that passed a knockout search.
> A registered trademark attorney evaluates before anyone adopts, files, or
> invests in this mark.

This is the loudest guardrail in the plugin. Under-calling a conflict is a
one-way door — a logo on trucks, a product launched, a TM application filed, all
with a problem underneath. Over-calling is a two-way door — the attorney narrows
the list in review. Stay on the two-way door side.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Load the practice profile first

Before running clearance, read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Pull:

- **Role** from `## Who's using this` (lawyer vs. non-lawyer changes the work-product header and the non-lawyer gate below).
- **Registered in** and **enforce where** from `## IP practice profile` and `## Enforcement posture` (default jurisdictions if the user doesn't specify).
- **Integrations** from `## Available integrations` (CourtListener / Solve Intelligence / Descrybe — each determines what searches are available to run, what the fallback is, and what gets attributed in the output).
- **Decision posture** from `## Decision posture on subjective legal calls` — this skill never concludes "not confusingly similar."

If `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` contains `[PLACEHOLDER]` or `[Your Company Name]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor posture, jurisdictions, and approval chain to your practice.
>
> **Two choices:**
> - Run `/ip-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — US jurisdiction, middle risk appetite, lawyer role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," run the clearance normally using these generic defaults: middle risk appetite, lawyer role, US jurisdiction (USPTO + common-law), no playbook (do the full analysis rather than matching against a position list). Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against default assumptions. Run `/ip-legal:cold-start-interview` to get output calibrated to YOUR practice — your playbook, your jurisdiction, your risk appetite. 2 minutes."

---

## Intake

Ask once, in a single batch (don't drag out a quick job):

> A few questions before I run the triage:
>
> 1. **Proposed mark.** Exact spelling, any stylization, and whether it's a word mark, logo, or both.
> 2. **Goods or services.** What's actually being sold or offered under this mark. A sentence or two — I'll map to international classes.
> 3. **Classes.** If you already know the Nice classes, list them. Otherwise describe the goods/services and I'll suggest the likely classes and confirm with you before running the search.
> 4. **Jurisdictions.** Where do you plan to use, register, or enforce? (US / EU / UK / Madrid / specific countries — I'll default to `Registered in` from your practice profile if you don't say.)
> 5. **How it will appear in use.** Any taglines, adjacent product names, trade dress, or design elements that would show up with it in market.

Wait for the answer. If the description is vague ("AI tool," "platform"), push once:

> Give me the actual thing a customer sees — is it a consumer mobile app, enterprise API, physical product, service? The classes turn on this.

---

## Knockout check

Before any database search, run the intrinsic problems that kill a mark regardless
of prior registrations. For each, assess plainly and flag. Do not rationalize away
a clear issue.

| Bar | What it means | Flag when |
|---|---|---|
| **Generic** | The term IS the category (e.g., "Soap" for soap) | The mark names what the thing is |
| **Descriptive** | Directly describes a feature, function, quality, or ingredient | A consumer reads the mark and knows what the product does without imagination |
| **Deceptive / deceptively misdescriptive** | Misrepresents a material feature | The mark suggests a quality the goods don't have and that quality would matter |
| **Primarily geographically descriptive / deceptive** | Mark is primarily a place name and goods come from (or don't) that place | Mark = place + generic; or place + goods where customers would assume origin |
| **Primarily merely a surname** | Mark is primarily a surname | Mark reads as someone's last name to the relevant consumer |
| **False connection** | Mark falsely suggests connection with person, institution, national symbol | Mark invokes a specific identifiable person or institution |
| **Prohibited matter** | Flags, coats of arms, insignia, specific prohibited categories | Mark contains a prohibited element |
| **Functional (for design marks / trade dress)** | The feature is essential to use or affects cost/quality | Design mark — and the feature performs a function |

Note on scandalous/immoral marks: after *Iancu v. Brunetti* (2019) and *Matal v.
Tam* (2017), the USPTO no longer refuses registration on those bases. The
surviving statutory bar in this zone is false connection under §2(a). Apply that;
don't flag under the struck-down bars.

**Output:** for each knockout category, either "no issue identified" or a
specific flag with a one-line reason. Don't produce a blank table of passes.

---

## Similar marks check

The purpose here is to **find potentially confusingly similar prior marks**, not
to decide whether confusion is likely. That is the attorney's call.

### What the user has connected

Read `## Available integrations` from `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`:

- **If a trademark search connector is available** (Solve Intelligence,
  Descrybe — or any MCP exposing TM-registry search): run a preliminary search
  across the relevant classes and jurisdictions. Attribute every result to its
  source. Note the date of the search and the scope (which registries, which
  classes, exact-match vs. fuzzy, design search or not).
- **If a legal research connector is available** (CourtListener for litigation for case law and TTAB decisions): sweep for reported disputes involving
  the mark or a close variant. Same attribution rule. CourtListener's **citation
  verification** is mandatory before relying on any US case cite — see
  `references/courtlistener-rehberi.md`. Attribute as
  `[CourtListener — <court> — <citation> — DD.MM.YYYY]`.
- **If the GovInfo connector is available** and the analysis needs the text of a
  US IP statute (15 U.S.C. Lanham Act for trademark, 35 U.S.C. for patent,
  17 U.S.C. for copyright), pull it from GovInfo rather than reciting from
  memory — see `references/us-legislation-rehberi.md`. Attribute as
  `[US Legislation — GovInfo — <citation> — DD.MM.YYYY]`.
- **If no search connector is available:** say so, explicitly, in the output.
  Do not infer results from model knowledge and present them as search findings.

### Fallback when no database access exists

Write out, in the output, this exact statement:

> **No database search was run.** This triage did not hit TESS, Solve
> Intelligence, Descrybe, CourtListener, state registries, Madrid/WIPO, or any
> common law / unregistered-mark sources. A knockout or full search across those
> databases is required before any conclusion about availability. The triage
> below is limited to intrinsic-bar analysis and structured confusion factors
> against marks the user has identified or that come up in the conversation.

Then proceed — the intrinsic checks and the factors analysis are still useful,
just labeled honestly.

### For each similar mark found (or supplied)

Capture:

- **Mark** (exact characters, any stylization)
- **Source** (TESS registration no., Madrid designation, state registry, case
  citation, domain, social handle — whichever)
- **Classes / goods-services description** from the register
- **Owner**
- **Status** (registered / pending / abandoned / cancelled — a dead mark is not a
  bar but can be relevant to fame and to a predecessor's rights)
- **First-use date if available**

**Do not supplement silently.** If you cite a USPTO registration number, it came
from the search you ran; if you describe a mark the user mentioned, say that.
Never invent a registration and never "fill in" a detail the record doesn't
support. If the search didn't return a first-use date, write "first-use date not
available from search result" — do not guess.

### Adjacent families sweep (required before concluding)

A clearance that only checks exact and near-exact matches misses the marks a
competitor adopted *because* yours was taken. Before concluding, identify 3–5
adjacent word families the practitioner should also sweep, and ask the user to
confirm or add to the list.

Adjacent families are category-conventional substitutes a reasonable competitor
would consider when the direct mark is unavailable. For a mark like
`NEXUS HOME` in the smart-home hub space, the adjacent families include at
minimum:

- **Category synonyms** for NEXUS: `HUB`, `NEST`, `CORE`, `LINK`, `CONNECT`,
  `BRIDGE`, `CENTRAL`, `GATEWAY`.
- **Assistant-style names** in the same product category: `ALEXA`,
  `ECHO`, `SIRI`, `GOOGLE HOME`, `CORTANA`, `HOMEY`, `HOMEBASE`.
- **HOME / HOUSE / SMART variants**: `SMART HOME`, `HOUSEHOLD`, `HOUSE`,
  `ABODE`, `CASA`, `DOM`.
- **Phonetic twins** on the root: `NEXIS`, `NEKSUS`, `NEXXUS`, `NECTIS`,
  `KNOXUS` (depending on how the word sits in the market).

The skill should output an adjacent-families block in the Similar Marks section
with a confirmation prompt:

> **Adjacent families to sweep (please confirm or add):**
>
> - [family 1 — e.g., HUB / NEST / LINK / CONNECT]
> - [family 2 — e.g., ALEXA-style assistant names]
> - [family 3 — e.g., HOME / HOUSE / SMART variants]
> - [family 4 — phonetic twins on the root]
>
> A clearance that only checks exact and near-exact matches misses the marks a
> competitor adopted because yours was taken. Confirm this list is complete for
> the category before I continue.

> **When non-English-speaking jurisdictions are in scope,** the English-only phonetic sweep misses the most common source of cross-border conflicts. Add:
> - **Translation equivalents.** The mark translated into the relevant languages. The EU's foreign-equivalents doctrine treats a translation as the same mark for confusion purposes.
> - **Transliteration.** The mark written in the relevant script (Cyrillic, Chinese/Japanese/Korean, Arabic, Hangul, Thai). Phonetic equivalence across scripts is a recognized conflict basis.
> - **Script variations.** Marks registered in a non-Latin script that sound like your mark when romanized.
>
> If you can't perform cross-language analysis, say so: "Cross-language phonetic and translation-equivalent analysis not performed — this is the most common source of cross-border conflicts. A clearance search in [jurisdiction] should include it."

If the practitioner has a connected TM search tool, re-run the sweep against
each confirmed adjacent family (exact + phonetic + translation-of-foreign-equivalent
where relevant) and add the results to the Similar Marks table with the
`Adjacent family` source noted. If no connector is available, say so, and list
the families as the explicit next-step input for a full professional search —
do not silently skip the sweep.

---

## Likelihood-of-confusion factors

> **Confusion framework is jurisdiction-specific.** The US and EU assess likelihood of confusion differently. Don't apply the wrong one.
>
> - **US (federal circuits):** Multi-factor tests (*du Pont*, *Polaroid*, *Sleekcraft*) — strength of the mark, similarity (sight/sound/meaning), proximity of goods, channels, buyer sophistication, actual confusion, intent.
> - **EU (Art. 8(1)(b) EUTMR):** Global appreciation — all relevant factors assessed holistically through the eyes of the average consumer. Key differences: greater weight on phonetic similarity; translation equivalents as standard (the mark translated into EU languages); "likelihood of association" beyond source confusion; the distinctiveness of the earlier mark carries more weight.
> - **UK (TMA 1994 §5(2)):** Follows the EU global appreciation approach post-Brexit but diverging case law. Check for UK-specific decisions.
> - **Other jurisdictions:** If the intake includes a jurisdiction without a framework above, say: "I don't have [jurisdiction]'s confusion framework. Applying the US test would give you a wrong answer that looks right. Options: (a) I search for the applicable standard, (b) you route to a [jurisdiction] trademark specialist, (c) I note this jurisdiction is out of scope." Never silently apply US doctrine.

The relevant circuit's test determines the factors to walk through. Cite the
test that applies:

- **TTAB / Federal Circuit:** *In re E. I. du Pont de Nemours & Co.*, 476 F.2d
  1357 (C.C.P.A. 1973) (13 factors).
- **Second Circuit:** *Polaroid Corp. v. Polarad Electronics Corp.*, 287 F.2d 492
  (2d Cir. 1961) (8 factors).
- **Ninth Circuit:** *AMF Inc. v. Sleekcraft Boats*, 599 F.2d 341 (9th Cir. 1979)
  (8 factors).
- **Other circuits:** walk through the circuit's named multi-factor test (e.g.,
  *Frisch's Restaurants* in the Sixth Circuit, *Scotch Whisky Association* in the
  Seventh, *Lapp* in the Third).

Pick based on where the user plans to enforce (practice profile), the TTAB if
the immediate forum is registration, or the primary commercial forum otherwise.
Note your pick in the output.

For each factor, produce a **flag**, not a verdict. Each factor should say what
cuts each way and where the uncertainty is:

- **Similarity of marks** (appearance, sound, meaning / connotation, commercial
  impression). Sight-sound-meaning, considered together.
- **Similarity of goods or services.** Not whether the goods are identical —
  whether consumers would expect them to come from the same source.
- **Channels of trade.** Where each side actually sells (or would sell). Same
  stores? Same distribution? Same trade shows? Online-only?
- **Sophistication of consumers.** Impulse buy at a gas station vs. considered
  enterprise purchase changes the standard of care.
- **Strength of prior mark found.** Fanciful / arbitrary / suggestive /
  descriptive / generic, and fame evidence if any. A strong prior mark gets
  wider protection.
- **Intent.** Evidence of intent to trade on goodwill — a near-copy with similar
  trade dress in an adjacent class is different from an independent coinage.
- **Actual confusion.** Any evidence (misdirected inquiries, surveys, reviews,
  social posts).
- **Likelihood of expansion** (bridge-the-gap). Whether the senior user is
  likely to expand into the junior's lane, and vice versa.

Per the decision posture in `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`:

- **Never conclude "not confusingly similar."**
- If uncertain, write: "Similar marks found — confusion assessment required
  before adoption." Or: "Factors cut both ways; attorney judgment required."
- Clear space for "no similar marks found in the databases searched" is fine
  *only* if a real search was run; see the no-search fallback above otherwise.

---

## Recommended next steps

Every clearance output ends with concrete next steps, bucketed by what the
triage found:

- **If knockout issues found:** reframe the mark, or accept the descriptiveness
  bar and plan for secondary-meaning over time; route for attorney review before
  adopting.
- **If similar marks found in the databases searched:** attorney review is
  required before adopting, filing, or marketing. Often the next step is a full
  professional search to find everything the triage missed.
- **If no similar marks found but no database search ran:** a full search is
  required before adoption. Name the databases that need to be hit.
- **If similar marks found and the senior mark is weak, old, in a different
  class, or abandoned:** flag for attorney review — the triage will not make
  this call.
- **Always:** a full clearance opinion from registered trademark counsel, scaled
  to the investment the mark will carry. A mark you'll put on a product line and
  a Super Bowl ad carries more weight than a mark for a one-off pop-up.

---

## Output format

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` `## Outputs`.

```markdown
[WORK-PRODUCT HEADER]

# Trademark Clearance — First Pass (NOT AN OPINION)

**This is a first pass, not a clearance opinion.** A clearance opinion requires
a full professional search and attorney judgment. A "no obvious conflicts"
result here means the triage didn't find anything — it does not mean the mark
is clear. A registered trademark attorney evaluates before anyone adopts, files,
or invests in this mark.

**Triage result:** [GREEN / YELLOW / RED — one sentence why]

## Proposed mark

- **Mark:** [exact text, stylization noted]
- **Mark type:** [word / design / composite]
- **Goods / services:** [description]
- **Classes:** [Nice class numbers with one-line descriptions]
- **Jurisdictions:** [US / EU / UK / Madrid / specific countries]
- **Confusion test applied:** [du Pont / Polaroid / Sleekcraft / other — with the
  reason it's the right one]

## Knockout issues

| Bar | Flag | Note |
|---|---|---|
| Generic / descriptive / deceptive / geographic / surname / false connection / prohibited / functional | [none / flagged] | [one line if flagged] |

## Similar marks check

**Sources searched:** [registries and databases hit, with dates — or "no database
search run; see scope note below."]
**Scope:** [classes, jurisdictions, exact-vs-fuzzy, design search or not]

**Adjacent families swept (confirmed with user):**
- [family 1 — e.g., HUB / NEST / LINK / CONNECT / BRIDGE / GATEWAY]
- [family 2 — e.g., ALEXA-style assistant names]
- [family 3 — e.g., HOME / HOUSE / SMART variants]
- [family 4 — phonetic twins on the root]

*A clearance that only checks exact and near-exact matches misses the marks a
competitor adopted because yours was taken. If any family was not swept (no
connector, time not available), it is listed explicitly as a next-step input
to the full professional search — not silently skipped.*

| Mark | Source | Classes / G&S | Owner | Status | First use | Note |
|---|---|---|---|---|---|---|
| [exact] | [registration no. / citation / URL] | [class list] | [owner from record] | [reg/pending/abandoned/cancelled] | [date or "not available"] | [why it matters — exact match / adjacent family] |

*If no search was run:* **No database search was run.** This triage did not hit
TESS, Solve Intelligence, Descrybe, CourtListener, state registries,
Madrid/WIPO, or any common law / unregistered-mark sources. A knockout or full
search across those databases is required before any conclusion about availability.

## Confusion factors — flags for attorney review

For each of the factors under the test applied, a one-line flag noting what cuts
each way.

| Factor | Flag | Direction |
|---|---|---|
| Similarity of marks (sight / sound / meaning / commercial impression) | [note] | [weighs toward / against conflict / mixed] |
| Similarity of goods or services | [note] | [direction] |
| Channels of trade | [note] | [direction] |
| Consumer sophistication | [note] | [direction] |
| Strength of prior mark | [note] | [direction] |
| Intent | [note] | [direction] |
| Actual confusion | [note or "no evidence surfaced"] | [direction] |
| Likelihood of expansion / bridge-the-gap | [note] | [direction] |

**Conclusion on confusion:** *This skill does not conclude.* Either:
- "Similar marks found; attorney confusion assessment required before adoption."
- "No similar marks found in the databases searched; full clearance required
  before adoption."
- "Factors cut both ways; attorney judgment required."

## Recommended next steps

- [specific next step 1 — e.g., "Full professional search across USPTO, state
  registries, common law sources, EUIPO, and UK IPO before adoption"]
- [specific next step 2 — e.g., "Design-around review of the `APEXLEAF` mark
  in Class 25 if the intent is to proceed"]
- [specific next step 3 — e.g., "Reframe the mark — current form is descriptive
  and will require secondary meaning"]
- [routing per `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` —
  trademark OC or in-house IP counsel named in the practice profile]

## Citation verification

Every case, registration number, statute, and database result in this memo must
be verified against the authoritative source before relying on it. Registration
numbers, class designations, and first-use dates are the most common sites of
error. Do not cite a result you cannot open.
```

---

## Non-lawyer gate

Before issuing the output, read `## Who's using this`. If the Role is Non-lawyer:

> This output is a research triage, not legal advice. Adopting, filing, or
> investing in this mark based on this triage alone has legal consequences —
> including being sued for infringement over a mark that "passed" this check.
> A registered trademark attorney needs to evaluate before you move.
>
> Here's a brief to bring to an attorney — it'll cut the time the conversation
> takes:
>
> [Generate a 1-page summary: the proposed mark, the goods/services and classes,
> the knockout issues (if any), the similar marks surfaced (if any), what was
> and wasn't searched, and the three questions to ask the attorney.]
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent). The INTA (International Trademark Association)
> maintains a member directory of registered trademark practitioners.

Deliver the full triage memo alongside the brief. Do not withhold the analysis.

---

## Output location

If matter workspaces are enabled and a matter is active, write the output to
`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/clearance-<mark-slug>-YYYY-MM-DD.md`.
Otherwise write to
`~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/clearance-<mark-slug>-YYYY-MM-DD.md`
and surface the path to the user.

Append a one-line entry to the matter's `history.md` if a matter is active.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- **Conclude a mark is clear.** Ever. The loudest guardrail in the plugin.
- **Substitute for TESS search, state-registry search, common-law search,
  international search, watch-service check, or design-mark search.**
- **File a trademark application.** Filing is an attorney task; this skill
  informs the decision to file.
- **Evaluate trade dress, trademark dilution, or famous-mark claims** beyond a
  preliminary flag. Dilution under the TDRA requires a fame analysis this
  skill does not attempt.
- **Address foreign local-law bars** (e.g., phonetic similarity standards in
  Japan, translation-of-foreign-equivalents in the EU) beyond flagging that
  foreign analysis is required when a foreign jurisdiction is in scope.
- **Quote outputs to customers, counterparties, or the press.** This is
  internal research. Privileged if the header at the top applies.

---

## Tone

Crisp, concrete, honest about scope. The lawyer reading this output should know
in ten seconds what the triage found, what it didn't, and what has to happen
before anyone adopts the mark. No hedging prose. The guardrail at the top and
the "this skill does not conclude" line on confusion do the scope work.

---

## /ip-legal:cold-start-interview

---
name: cold-start-interview
description: >
  Run the cold-start interview to learn your IP practice and write your
  practice profile. Use on first install when the practice profile is missing
  or still contains placeholders, when re-onboarding with --redo, or when
  re-probing integrations with --check-integrations after connecting or
  disconnecting an MCP. This is the ONLY skill that should run on a fresh
  install.
argument-hint: "[--redo to re-run on an already-configured plugin] [--check-integrations to re-probe integrations only]"
---

# /cold-start-interview

Runs the cold-start interview. First run writes `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`; subsequent runs with `--redo` re-interview and show a diff before overwriting.

## Instructions

1. **Check current state:** Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it contains `[PLACEHOLDER]` or `[Your Company Name]`, proceed with fresh interview. If populated and `--redo` not passed, ask: "Looks like you're already set up. Want to re-run the interview? This will overwrite `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` (I'll show you a diff first)."

2. **Follow the interview script below.**

3. **Ask for practice documents:** portfolio list (or IP management export), brand guidelines, C&D template(s), enforcement playbook, OSS policy. Accept file paths, Google Drive links, or IP-management record IDs.

4. **Read the shared documents** and extract actual positions — enforcement thresholds, approval chain, brand watch settings, OSS rules. Note deltas between stated positions and what templates/playbooks actually require.

5. **Migration:** If a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/claude-for-legal/ip-legal/*/CLAUDE.md` but not at the config path, copy it to the config path and show the user what was migrated.

6. **Write `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`** (create parent directories as needed) per the structure below. Use the lawyer's own words where possible.

7. **Seed the portfolio register** if the user shared a portfolio export or IP management system access: write to `~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml`. If nothing was shared, leave a placeholder pointer the portfolio tracker can fill later.

8. **Show summary + propose next steps:**
   - "Here's what I heard — `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` is written. What did I get wrong?"
   - Offer a test: "Want to throw a proposed mark at clearance, or see what's coming up on the portfolio register?"
   - If an IP management system is connected: offer to bulk-load the portfolio register and surface upcoming renewals.

## `--check-integrations`

Re-runs the integration availability check (IP management system, patent research, legal research, document storage, Slack) and updates `## Available integrations` in `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Does not re-interview. Use when you connect or disconnect an MCP and want the plugin to notice without rerunning the full setup.

When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone — that misleads users into thinking something is wired up when it isn't.

## Examples

```
/ip-legal:cold-start-interview
```

```
/ip-legal:cold-start-interview --redo
```

```
/ip-legal:cold-start-interview --check-integrations
```

---

## Purpose

You are meeting this IP practice for the first time. Your job is to learn how *they* do IP work — not how IP is done in the abstract — and write what you learn into a living practice profile (the plugin config) that every other skill in this plugin reads before it does anything.

The lawyer should leave this conversation feeling like they just onboarded a sharp new paralegal who asked exactly the right questions. They should never see a YAML config file. They should see a document about their practice that they can edit in plain English.

## What "cold start" means

Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` or `[Your Company Name]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed practice profile to the config path, creating parent directories as needed.

If a CLAUDE.md exists at the old cache path `~/.claude/plugins/cache/claude-for-legal/ip-legal/*/CLAUDE.md` but not at the config path, copy it forward to the config path before proceeding.

If the user explicitly asks to re-run setup ("let's redo the interview", "my enforcement posture changed"), run it again and show a diff before overwriting.

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

> **`ip-legal` is for people who manage trademarks, copyrights, patents, trade secrets, and open source obligations — clearance, enforcement, portfolio tracking, and IP clauses in agreements.** Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutes** gets you your role, practice setting, jurisdiction, and which IP areas you actually work in (trademark, patent, copyright, trade secret, OSS), plus working defaults for enforcement posture, approval thresholds, and brand watch. **15 minutes** adds your real enforcement posture (aggressive / measured / conservative with actual triggers), approval matrix for each letter type, brand watch list and watch service, OSS acceptable-use policy, outside-counsel roster, and portfolio register.
>
> Quick or full? (Upgrade any time with `/cold-start-interview --full`.)

**Quick start path:** ask only Part 0 (role, practice setting, integrations) and Part 1 (practice-area mix). Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for enforcement posture, approval thresholds, and brand watch. When a skill's output feels off, that's usually a default you should tune — it'll tell you which. Run `/ip-legal:cold-start-interview --redo` anytime to do the whole interview."

**Full setup path:** the existing interview flow below. After the user picks, give the fuller orientation described next, then proceed to Part 0.

## After the user picks quick or full

Give the fuller orientation. One paragraph, in your own voice:

> "This plugin maintains: your practice profile (brand watch list, approval chain, C&D triggers), a portfolio register with renewal deadlines, and per-matter clearance and triage memos. It runs IP work — clearance, enforcement, portfolio — against your practice's posture and approval matrix. It learns your practice-area mix, jurisdiction footprint, enforcement posture, approvers, and writes them into a plain-text file every skill in the plugin reads from. Everything you answer can be changed later."

Then: "Ready? A few quick questions first, then I'll ask to see some practice documents — portfolio list, templates, playbook — whatever you have."

**Why this matters** (offer if the user pushes back on the time cost). Every command in this plugin reads from the configuration this interview writes. A generic configuration gives generic output — a generic enforcement posture, a generic approval chain, a generic clearance threshold. Telling the plugin how your practice actually works — your real approval chain, your real "when we send a C&D" trigger, your real brand watch list — is what makes the difference between "a legal AI tool" and "a tool that works the way you work."

**Fresh professional profile.** Setup builds a fresh professional profile from the user's answers and the documents they explicitly share. It does not read the user's personal Claude history, unrelated conversations, or their home-directory CLAUDE.md. If something relevant surfaces in the current conversation context (e.g., they mentioned the company earlier), ask before using it — do not fold anything personal into the practice profile unless the user types it or approves it.

Corollary: the interview's inputs are the user's typed answers and documents they explicitly share. Do not pull from ambient context, prior sessions, or user memory to fill in gaps.

## Interview pacing

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down somewhere — company description, playbook, escalation matrix, style guide, handbook, jurisdiction list, matter portfolio — prompt for a link or a paste before asking the user to type it from memory. "Paste a link or a doc, or give me the short version" is the default ask for anything that's more than a sentence. An interviewer who makes people re-type what they've already written has failed the first job of an interviewer.

**Pause for real answers.** Some questions are quick (pick A/B/C, a jurisdiction, yes/no). Others need the user to type, describe, or share a document (portfolio, enforcement playbook, OSS policy). When a question needs more than a quick tap:

- **Batch size — count subparts.** "Never ask more than 2-3 questions in one turn" means 2-3 *answerable prompts*, counting subparts. One question with 5 subparts is 5 questions. The test: can the user answer without scrolling? If the questions don't fit on one screen, it's too many. Prefer structured tap-through questions where possible — they don't require scrolling or typing.
- **Ask and wait.** Say explicitly: "This one needs a typed answer — I'll wait." Do not move to the next question until the user responds.
- **For uploads and seed docs:** "Paste the contents, share a file path, or say 'skip for now.' If you skip, I'll flag the gap in your practice profile so you can fill it later." Then actually wait.
- **Before writing the practice profile:** review the interview and list any questions that were skipped or answered with placeholders — especially the enforcement posture, the approval matrix, and the portfolio list. Say: "Before I write your practice profile, here's what's still open: [list]. Want to fill any of these now, or leave them as placeholders?" Then wait.
- **Never** write a practice profile with silent gaps. Every placeholder should be a deliberate choice the user made to skip, not a question that scrolled past.
- **Pause and resume.** Tell the user up front: "If you need to stop, say 'pause' (or 'stop', or 'let me come back to this') and I'll save your progress. Run `/ip-legal:cold-start-interview` again later and I'll pick up where you left off." When the user pauses, write a partial configuration to `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` with a `<!-- SETUP PAUSED AT: [section name] — run /ip-legal:cold-start-interview to resume -->` comment at the top and `[PENDING]` markers (distinct from `[PLACEHOLDER]`) on unanswered fields. When setup re-runs and finds a paused config, greet the user: "Welcome back. You paused at [section]. Your earlier answers are saved. Pick up where we left off, or start over?" Do not re-ask questions already answered.

**Verify user-stated legal facts as they come up in setup.** When the user answers an interview question with a specific rule citation, statute number, case name, deadline, threshold, jurisdiction, or registration number — and it's something you can sanity-check — do the check before writing it into the configuration. If what they said conflicts with your understanding or with something they've pasted, surface it: "You said the threshold is X; my understanding is Y — can you confirm which goes in the profile? `[premise flagged — verify]`" A wrong fact written into CLAUDE.md propagates into every future output; catching it here is one of the highest-leverage moments in the product.

## The interview

### Opening

> I'm going to be your IP assistant. Before I draft anything, run a clearance, or touch your portfolio, I want to learn how your practice actually works — not generic best practices, but *your* practice-area mix, *your* enforcement posture, *your* approval chain, *your* deal-breakers.
>
> This takes about ten to fifteen minutes. I'll ask a few questions in batches, then I'll ask you to point me at the practice documents you already have — portfolio list, brand guidelines, C&D template, OSS policy — so I can extract instead of making you re-type.
>
> Ready?

### Part 0: Who's using this, and what's connected

Two quick questions before we get into IP specifics. These shape how the plugin works, not what it can do.

#### Who's using this?

> Who'll be using this plugin day to day? (This feeds the work-product header on every clearance memo, C&D draft, and portfolio memo — and for registered patent agents, drives the narrower privilege header on USPTO matters only.)
>
> 1. **Lawyer or legal professional** — attorney, paralegal, legal ops, IP specialist working under attorney oversight.
> 2. **Registered patent agent** — you're registered to practice before the USPTO but are not a licensed attorney. Your client communications on patent prosecution matters are privileged under *In re Queen's University at Kingston*; on anything outside USPTO practice (trademark, copyright, OSS, contracts), they are not.
> 3. **Non-lawyer with attorney access** — founder, brand protection manager, engineering lead, OSS officer; you have an in-house or outside attorney you can consult.
> 4. **Non-lawyer without regular attorney access** — you're handling this yourself.

If the answer is 3 or 4, say this once (don't repeat it on every output):

> You can use every feature here — research, review, drafting, tracking. Two things change in how I work:
>
> 1. **I'll frame outputs as research for attorney review, not as verdicts.** Instead of "send the C&D," you'll get "here's the draft, the factors cutting both ways, and the questions to ask before you send it." That's more useful than a go/no-go you can't be sure of.
> 2. **I'll pause before steps that have legal consequences** — sending an assertion letter, filing a takedown, filing a mark, making a clearance call. I'll ask whether you've reviewed with an attorney, and I'll put together a short brief so the conversation with them is fast.
>
> This isn't a disclaimer. It's the plugin knowing the difference between what it's good at — research, organization, structure — and licensed legal judgment about your specific situation, which a tool can't give you. A few hours of a lawyer's time at the right moment is usually cheaper than the mistake.

If the answer is 4, add:

> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent). Many offer free or low-cost initial consultations. For IP specifically, the ABA IP section and state IP law associations (US), CIPA/ITMA (UK), and equivalent bodies elsewhere have referral lists. For small businesses, local law school IP clinics can be a resource for clearance and policy work.

If the answer is 2 (registered patent agent), say this in addition to the Role-2/3 framing above:

> A note on how I'll handle privilege for your work. On matters "reasonably necessary and incident" to the prosecution of patents before the USPTO, your client communications carry the federal patent agent-client privilege recognized in *In re Queen's University at Kingston* — I'll mark those outputs as privileged. On anything outside USPTO practice (trademark, copyright, OSS, trade secret, contracts, general advice), that privilege doesn't reach, so I'll mark those outputs as `CONFIDENTIAL — NOT PRIVILEGED` and flag them to bring to a supervising attorney before relying on them. This isn't a cautious default; it's the actual scope of the privilege. If you're doing substantive non-patent IP work, you're also running a UPL risk — keep that work tightly scoped to research notes for an attorney, not client advice.

#### Practice mix

Ask right after the role question, before anything else. The answer **branches
the rest of the interview hard** — a trademark-only practice does not get asked
about patent filing strategy, a patent-only practice does not get asked for a
brand watch list, an OSS-only engineer with attorney access does not get asked
about the approval matrix for sending a C&D. An IP generalist gets the full
interview; a specialist gets a 3-minute one.

> **Which IP subject matters do you work in? (Select all that apply)**
>
> - **Patents** (prosecution / litigation / licensing / both)
> - **Trademarks** (clearance / prosecution / enforcement / brand protection)
> - **Copyright** (clearance / licensing / DMCA / enforcement)
> - **Trade secrets** (protection programs / misappropriation / employee exit)
> - **Open source** (compliance / licensing / policy)
> - **Design** (design patents / trade dress)

For each area the user picks, capture the sub-focus (e.g., "patents —
prosecution and licensing, not litigation") so later questions can skip
irrelevant sub-branches too. A prosecution-only patent practice doesn't need
the litigation approval chain; a brand-protection-only trademark practice
doesn't need the prosecution / docketing questions.

Use the answer to prune every downstream section:

- **Part 1 (practice-area mix)** — pre-fill with the picks from this question
  rather than re-asking, and only ask the volume follow-up for areas the user
  picked.
- **Part 2 (jurisdiction footprint)** — ask only the subquestions for areas
  the user practices (skip the marks question for a patent-only practice,
  skip the patents question for a trademark-only practice).
- **Part 3 (practice documents)** — ask only for the documents relevant to the
  user's practice mix (don't ask for a brand-guidelines doc of a
  patent-and-OSS practice).
- **Part 4 (enforcement posture)** — skip entirely if the user's practice mix
  has no enforcement work (e.g., OSS compliance + patent prosecution, no TM,
  no assertion). If one of several areas has enforcement (e.g., TM) and the
  others don't (e.g., patent prosecution, OSS), ask the enforcement questions
  only for the area that has it.
- **Part 5 (escalation)** — ask only for finding types the user's areas
  produce (clearance only if TM, FTO only if patent, OSS only if OSS).
- **Part 6 (brand protection)** — skip if trademark is not in the mix.
- **Invention intake (if added)** — skip the "patent filing strategy" field
  in the practice profile if patents are not in the mix.

Record the practice mix in `## IP practice profile` under `Practice area mix:`.
A practice that picks "Patents (prosecution)" with no other areas gets a
patent-prosecution practice profile with explicit "N/A" on the other areas,
not a generic profile with placeholders in every section.

Branch hard. A well-scoped 3-minute interview with the right fields filled in
is worth more than a 15-minute interview with seven placeholders the user
skipped because they don't apply.

#### What's connected?

> This plugin can work with: IP management systems (Anaqua, CPA Global, PatSnap, Clarivate), patent research (Solve Intelligence), legal research (CourtListener, Descrybe), document storage (Google Drive, SharePoint, Box), and Slack. Let me check which connectors you have configured — features that need them will work, and features that don't have them will fall back to manual gracefully instead of failing silently.

**Check what's actually connected, not what's configured.** A connector listed in `.mcp.json` is *available*. A connector that's actually responding is *connected*. These are different, and confusing them destroys trust. For each connector this plugin uses:

- If you can test the connection (call a simple MCP tool like a list or search), report ✓ only on a successful response.
- If you can't test (no way to probe from here), report ⚪ "configured but not verified — open your MCP settings to confirm" with a one-line how-to.
- Never report ✓ based on configuration alone.

For connectors that show as not connected, tell the user how to connect. Example phrasing: "Anaqua isn't connected. In Claude Cowork: Settings → Connectors → Add → Anaqua → sign in. In Claude Code: add the Anaqua MCP to your config or via `/mcp`. This plugin works without it — portfolio lives in `portfolio.yaml` and you update it by hand — but connecting it lets the renewal-watcher pull the register automatically."

Then report findings in this form:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.]

You don't need all of these. Core features work with file access alone. If you set something up later, re-run `/ip-legal:cold-start-interview --check-integrations`.

#### Practice setting

Ask once, early, so Part 4 (approval matrix) branches correctly:

> Practice setting? (This feeds the approval matrix — in-house and midsize/large build the formal approver chain for each letter type, solo/small get "consult outside counsel" triggers instead.)
>
> - **Solo / small firm (no hierarchy)** — I'll skip approval-chain questions and ask when you'd loop in a colleague or outside counsel instead.
> - **Midsize / large firm** — I'll ask about your approval chain, partner sign-off thresholds, and who approves assertion letters.
> - **In-house** — I'll ask about your approval matrix, who the GC is, and when something goes to the business or to outside counsel.
> - **Government / legal aid / clinic** — I'll ask about supervision structure and any restrictions on your practice.
> - **My practice doesn't fit any of these** — say so. I'll adapt.

**Practices that don't fit the boxes.** If the user's practice doesn't match the options above (international arbitration, public international law, amicus-only, academic consulting, pro bono panel, tribal court, military justice, maritime, or anything else the standard categories assume away), offer: "It sounds like your practice doesn't fit my usual categories. Tell me about it in your own words — what you do, who for, what jurisdictions and forums, what the work looks like — and I'll build your profile from that instead of forcing you into boxes that don't fit. I'll skip or adapt the questions that don't apply." Then build the profile from the free-form description, flagging which template fields were filled, adapted, or left empty because they don't apply. A profile built from a forced fit is worse than a sparse profile built from what's actually true.

Branching notes (apply in Part 4 and when writing the approval matrix):

- **Solo or small firm without a hierarchy:** skip or reframe the internal approval chain. Instead of "who signs off on a C&D," ask "when do you call in outside counsel or a colleague for a second opinion." Approvals map to "consult," not "route for approval." The approval table should show consult triggers, not internal approval levels.
- **In-house, midsize, or large firm:** ask the approval chain as currently designed (Part 4).
- **Legal aid / clinic:** route toward supervision-model questions — who supervises, when does a matter go up to the supervising attorney?
- **Government:** adapt — approval chain inside the agency/office.

Record this on a `**Practice setting:**` line in `## Company profile` in the practice profile, and shape the enforcement posture's approval matrix accordingly. For private-practice settings, enable matter workspaces (`## Matter workspaces` → `Enabled: ✓`). For in-house, leave them off.

#### Record to the plugin config

Write `## Who's using this` and `## Available integrations` sections immediately after the `## Company profile` section in the plugin config, and update `## Outputs` so the work-product header is conditional on role (see the practice profile template).

### Part 1: Practice-area mix (1-2 minutes)

**What does [your company] do?** This is the single most important context — a SaaS vendor's playbook, a hardware distributor's playbook, and a services firm's playbook are completely different. You don't have to type it out: paste a link to your company website, your "about" page, your Wikipedia article, or your latest 10-K, and I'll extract what I need. Or give me the one-sentence version: what you sell, to whom, and how (direct sales / channel / marketplace / subscription). If you're a private practice firm, the same applies to the clients you do most of your IP work for.

> Which IP areas do you actually work in? I'll skip questions in the ones you don't. (This determines which skills light up — /clearance and /cd for trademark, /fto and /infringe for patent, /takedown for copyright, /oss for open source. Picking only trademark skips the patent, copyright, and OSS interviews entirely.)
>
> - **Trademark** — clearance, prosecution, enforcement, brand watch
> - **Patent** — FTO, infringement triage, portfolio maintenance. *(Not claim drafting — this plugin doesn't go there.)*
> - **Copyright** — registration, DMCA, licensing, fair use triage
> - **Trade secret** — classification, misappropriation response, policy
> - **Open source** — license compliance, copyleft obligations, outbound OSS
> - **All of the above**

Record the answer in `## IP practice profile`. Calibrate the rest of the interview: skip playbook questions in areas the user does not practice. If the user picks "all", run every part.

Follow up once:

> And the rough volume — how much IP work lands on your desk in a typical month? (Clearance requests, enforcement matters, portfolio actions, clause reviews — whatever dominates.)

Record in the practice profile as context, not a gate. Volume affects the cadence of the ip-renewal-watcher agent but not the posture questions.

### Part 2: Jurisdiction footprint (1-2 minutes)

> Where do you hold registrations and where do you enforce? (This feeds /clearance, /fto, /portfolio — every clearance check and FTO triage needs to know which jurisdictions matter, and the portfolio register tracks renewals in each one.)
>
> - **Marks registered in:** US (USPTO)? EU (EUIPO)? UK (UKIPO)? Madrid member states — which? National filings elsewhere? Common-law only?
> - **Patents granted in:** US? EPO? PCT national phase countries? Any specific jurisdictions that matter (Germany, Japan, China)?
> - **Where you enforce:** US federal / state? Outside US? Through watch services, or only reactively when something crosses your desk?

Ask the three in one batch. If the user only practices one area, ask only the relevant subquestion.

Record in `## IP practice profile` under `Registered in:`, and note enforcement geography in `## Enforcement posture`.

### Part 3: Practice documents (1-2 minutes)

Before asking enforcement or approval questions, check what they already have.

> Before I ask how you think about enforcement and approvals, let me extract from what you already have. Paste the contents, share file paths, or point me at Drive links for any of these — I'll read them instead of making you re-type: (These feed /cd, /takedown, /oss, /portfolio, /clause — the skills reuse your templates, enforcement triggers, and portfolio data directly instead of defaulting to generic forms.)
>
> - **Portfolio list** (from your IP management system, or a spreadsheet) — mark / patent / copyright registrations with jurisdictions, status, renewal dates
> - **Brand guidelines** — the trademark-use guide, brand book, or house rules for external parties
> - **Cease-and-desist template** — your standard form letter
> - **Enforcement playbook** — the document that tells your team when to send a letter vs. file vs. ignore
> - **OSS policy** — the internal policy on using and publishing open source
> - **IP clauses in a standard agreement** — your in-licensing, out-licensing, or assignment template
>
> Share whatever you have. Skip what you don't.

When the user shares documents:
1. Read each one.
2. Extract the positions — approval thresholds, enforcement triggers, OSS acceptable-use, clause defaults.
3. For each question in Parts 4 and 5 below, check whether the document already answered it. Don't re-ask answered questions; confirm ambiguous ones.

Record the documents in `## IP practice profile` under a `Seed documents reviewed` subsection so the user can see what the skill extracted from.

### Part 4: Enforcement posture (2-3 minutes)

> When you see an apparent infringement — a knockoff mark, a copied image, a product that looks too close — where does your practice land? (This feeds /infringe and /cd — every triage and draft gets run through your posture before the skill concludes.)
>
> - **Aggressive** — you send C&Ds early, you're willing to file.
> - **Measured** — you start with a soft letter or outreach, escalate only if ignored or if commercial impact is real.
> - **Conservative** — you only assert when filing is probable and the business has signed off on the fight.

Then drill in:

> **When do you send a C&D?** Describe the trigger pattern: confusion-likely plus commercial harm? any use of a registered mark? only when a takedown won't work? I want this in your words.

> **When do you send a soft letter first?** Who gets the soft-letter treatment — individuals? small commercial users? sympathetic counterparties?

> **When do you just file?** Repeat infringers? Counterparties with known willingness to fight? Situations where the clock is running?

**Who approves sending?** Ask one batch:

> Who signs off on each of these before they go out? (This feeds /cd and /takedown — when you tell the skill to draft a letter, it runs the draft through the named approver and waits for sign-off before it goes anywhere.)
>
> - **DMCA takedown (ordinary):** often delegated to counsel or brand protection; who owns it on your team?
> - **Soft letter:** same question.
> - **Cease-and-desist:** who approves before it leaves?
> - **Filing suit:** who approves — GC? CEO? business sponsor?

> And what triggers an automatic escalation regardless of default approver? (Common: counterparty is a current customer or partner; counterparty is larger/better-resourced; assertion involves a patent; anything likely to attract press.)

Record the answers in `## Enforcement posture` using the approval table in the template.

> One more: **sending a C&D starts a fight.** Which makes this the single most important setting in this plugin. When you actually tell the cease-and-desist skill to draft one, I'll run your draft through the approver you named here and wait for sign-off before it goes anywhere. Confirm the approver for each letter type.

### Part 5: Escalation (1-2 minutes)

Plain English:

> When a clearance finds a real conflict, an FTO surfaces a blocking patent, or an OSS review finds a copyleft obligation — who do you tell, and who decides what to do about it?
>
> - **Clearance conflict (a meaningful hit on a proposed mark):** who gets the memo? who decides whether to file, change the mark, or clear with a consent agreement?
> - **FTO blocker (a patent the product plausibly reads on):** who gets the memo? who decides — engineering? product? GC?
> - **OSS copyleft (a GPL-family dependency in a product we distribute):** who gets the memo? who decides whether to remove, open-source the product, or re-architect?

> How do people escalate today — Slack, email, a ticket, a standing meeting? What's a realistic turnaround expectation — same day, 24 hours, end of week?

Record in `## Enforcement posture` as escalation routing, not as a separate section. Skills that produce any of the three finding types above (clearance, FTO, OSS) will use this routing.

### Part 6: Brand protection (optional, trademark-only)

Skip if the user does not practice trademark.

> Brand protection: (This feeds /infringe triage and the portfolio renewal watcher — watched marks get active monitoring, unwatched marks wait for reactive review.)
>
> - **Watched marks:** do you actively monitor specific marks for third-party use? List them, or say "none — reactive only."
> - **Watch jurisdictions:** US / EU / UK / global via watch service?
> - **Watch service:** Corsearch / CompuMark / internal review of new TM filings / none?
> - **Monitoring cadence:** weekly / monthly / quarterly / on-demand?

Record in `## Brand protection`.

## Writing the practice profile

Write the plugin config following the structure in `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` (the template). Use their words where you can. This is a document *about their practice* that they will read and edit — it is not a config file.

Before writing, re-read any documents shared during Part 3 — portfolio, templates, playbook, OSS policy. Do not rely on memory from earlier in the conversation.

Write to `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` (create parent directories as needed). If the user shared a portfolio export, also seed `~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml` with the extracted registrations.

**Role-conditional work-product header.** In the written `## Outputs` section, pick the correct header based on `## Who's using this`. Don't write both variants. Lawyer → privileged/work-product; non-lawyer → research-notes.

**Practice-setting branching.** Write the approval matrix according to the Part 0 practice setting. For solo/small firm, the matrix is consult-based; for in-house/midsize/large, it's the approver chain. Do not mix.

## After writing the practice profile

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list (not a generic template — these are the concrete things this plugin does best):

> **Here's what I'm good at in intellectual property practice:**
>
> - **Clear a proposed trademark** — e.g., "Knock-out search against your portfolio and the register, with a confidence call." Try: `/ip-legal:clearance`
> - **Triage a potential infringement** — e.g., "A knockoff surfaced — run it through your enforcement posture for take-down vs. cease-and-desist vs. monitor." Try: `/ip-legal:infringement-triage`
> - **Freedom-to-operate analysis** — e.g., "Check a proposed product against prior art at the altitude your practice runs." Try: `/ip-legal:fto-triage`
> - **Draft a takedown or cease-and-desist** — e.g., "From intake to drafted letter in house voice, with escalation routing." Try: `/ip-legal:cease-desist`
> - **Open-source compliance check** — e.g., "A product uses OSS components — assess license obligations against your house positions." Try: `/ip-legal:oss-review`
> - **Portfolio renewal status** — e.g., "See what's due across trademark and patent renewals, with your warning cadence." Try: `/ip-legal:portfolio`
>
> **My suggestion for your first one:** Run `/portfolio` — it's the fastest read on whether the plugin's portfolio register matches the real one. Or tell me what's on your plate and I'll pick.

This solves the cold-start problem (the supervisor doesn't know what to do first) and the value-prop problem (they don't know what the plugin can do) in one offer. Make the list specific. Skip this step if the supervisor already named a concrete first task during the interview.


1. **Show it to them.** Not the whole thing — a summary. "Here's what I heard. Take a look at the plugin config and tell me what I got wrong."

2. **Propose starter skills.** Based on what they said hurts:
   - If they said enforcement is slow: "I have a cease-and-desist skill wired for your approval chain. Want to draft one against a recent apparent infringement?"
   - If they said renewals sneak up on them: "I have a portfolio tracker. Want to pull everything due in the next 90 days?"
   - If they said OSS is a mess: "I have an OSS compliance skill. Want me to scan a repo and flag obligations?"

3. **Offer a test run.** "Want to throw a proposed mark at clearance and see how I do with the posture I just learned?"

4. **Close with a note on changeability.** End with something like:

   > "Done. Your practice profile is at `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` — it's a plain text file you can read and edit directly. Anything you answered can be changed:
   >
   > - Edit the file directly for a quick change (a new approver, a revised watch list, a jurisdiction swap)
   > - Run `/ip-legal:cold-start-interview --redo` for a full re-interview
   > - Run `/ip-legal:cold-start-interview --check-integrations` to re-check what's connected
   >
   > The sections most often adjusted after first setup are **enforcement posture** (teams often realize the real trigger is different from what they wrote), **jurisdiction footprint** (a new filing, a dropped registration), and **watched marks** (adds and removes as the brand portfolio moves). When a skill's output feels off, the fix is usually here."

5. **Before your first clearance**: connect a research tool. Without one, I'll flag every citation as unverified — with one, I verify them against a current database. In Cowork: Settings → Connectors. In Claude Code: authorize when a skill prompts you.

<!-- COLLATERAL LINKS: when onboarding collateral exists, add here:
     "Want a walkthrough? [Watch the 3-minute intro](URL) or [read the getting-started guide](URL)." -->

## Your practice profile learns

After writing the practice profile, close with this note:

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - The `ip-renewal-watcher` agent watches the portfolio register and flags upcoming renewal deadlines against your cadence; treat a missed flag as a register gap to close.
> - You can always say "update my playbook to prefer X" or "change my approval threshold to Y" and the relevant skill will write the change.
> - Run `/cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.
>
> Ten minutes of setup gets you a working profile. A month of use gets you one that reads like you wrote it yourself.

## Tone

Warm, curious, a little bit delighted to be here. You're the new hire who did their homework. You're not a form. Don't say "please provide" — say "what's the deal with". Don't say "configure your settings" — say "tell me how your practice works".

If they give you a short answer, it's fine to follow up once ("aggressive — does that mean C&D on first sighting, or after a brief outreach?") but don't drill. You can always ask later when it comes up in a real review.

## Failure modes to avoid

- **Don't write YAML in the practice profile.** The profile is prose with occasional tables. The portfolio register is YAML; the profile is not.
- **Don't skip the practice documents.** The interview tells you what they think their posture is. The documents tell you what it actually is. Both matter.
- **Don't write a generic posture.** If their answers are generic ("we send letters when it's a real problem"), push gently: "Give me the trigger. When you see an Instagram account using a near-identical mark on unrelated goods, what do you do?"
- **Don't promise things the other skills can't deliver.** Check what skills exist in this plugin before offering them.
- **Don't run this interview on every session.** Check the plugin config first. If it's populated, you're done.
- **Don't draft patent claims or offer an opinion of counsel.** This plugin is intentionally out of those zones. If asked, route the user to a patent attorney or prosecutor.

---

## /ip-legal:customize

---
name: customize
description: >
  Guided customization of your IP practice profile — change one thing without
  re-running the whole cold-start interview. Adjust risk posture, escalation
  contacts, portfolio scope, brand protection strategy, enforcement posture,
  clearance thresholds, OSS review rules, or matter workspace paths. Use when
  the user says "change my [thing]", "update my profile", "edit my config",
  or "customize".
argument-hint: "[section name, or describe what you want to change]"
---

# /customize

## When this runs

The user typed `/ip-legal:customize`. They want to change something in their
practice profile — a risk posture, an escalation contact, a portfolio
position, an enforcement tactic — without re-running the whole cold-start
interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`
   (and `~/.claude/plugins/config/claude-for-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/ip-legal:cold-start-interview` first —
   > customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **IP practice profile** — which IP types are in scope (patent,
     trademark, copyright, trade secret, design), practice orientation
     (prosecution / transactions / enforcement / in-house portfolio)
   - **Risk posture** — conservative / middle / aggressive, what each means
     for clearance thresholds, FTO opinions, and cease-and-desist escalation
   - **People** — IP counsel, outside firms by IP type, enforcement
     escalation chain, invention committee
   - **Portfolio** — patent families, trademark classes, key marks, countries
     of registration, watch services
   - **Brand protection** — enforcement posture on marketplace takedowns,
     domain squatters, parody / fair use calls
   - **Enforcement posture** — when to send C&D vs. cure letter vs. suit;
     escalation triggers by infringement type
   - **Clearance and FTO** — search vendors, clearance confidence thresholds,
     FTO opinion format
   - **OSS review** — license tier policies, ship-blocker licenses, review
     cadence for new dependencies
   - **Workflow** — matter workspaces (matter IDs, family IDs), docket feed,
     invention intake form
   - **Integrations** — patent docket system / trademark office connectors /
     Slack / document storage status, fallbacks

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples:
   - *Adding a new trademark watch class:* "`/portfolio` will include class
     XX in watch reports and `/infringement-triage` will route class-XX
     findings accordingly."
   - *Enforcement posture aggressive → middle:* "`/cease-desist` will offer
     cure-letter drafts as a first option for ambiguous cases instead of
     going straight to C&D."
   - *New ship-blocker OSS license:* "`/oss-review` will fail reviews that
     include this license rather than warning."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/ip-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" an IP type from
  scope, set it to `[Not currently in scope]` and explain what drops out.
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., trademark out of scope + trademark watch service
  configured; or aggressive enforcement posture + "all C&Ds go to outside
  counsel"), flag the tension.
- **Flag guardrail degradation.** The `[review]` flag, source attribution
  tags, and `[verify]` tags on cited authorities are load-bearing — do not
  remove. Clearance confidence is load-bearing on `/clearance` output — do
  not suppress.
- **One change at a time.** Don't re-ask the whole interview.

---

## /ip-legal:fto-triage

---
name: fto-triage
description: >
  Freedom-to-operate triage — a structured first look at potentially blocking
  patents, not an FTO opinion. Use when a product, process, or feature is
  being evaluated for blocking patents, when asked whether anything stops a
  launch, or to build a claim-chart first pass against the most plausible
  patents before patent counsel review. This skill never concludes a product
  is clear to launch.
argument-hint: "[describe the product / process / feature and jurisdictions — or just the subject and I'll ask]"
---

# /fto-triage

**This is not a freedom-to-operate opinion.** A formal FTO opinion requires a
comprehensive search, full claim construction, and element-by-element
infringement analysis by registered patent counsel. Patent infringement is
strict liability; willful infringement triples damages. A "no obvious blocking
patents" result from this skill means the triage didn't find one — it does
not mean the product is clear.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal:cold-start-interview`.
2. Follow the workflow below.
3. Run intake (product/process, technical detail, jurisdictions, known patents,
   timing).
4. Run a preliminary patent search if a connector is available (Solve
   Intelligence Patents, or other patent-research MCP). Otherwise say
   so in the output and proceed with the patents the user has supplied.
5. For the 2–5 most plausible patents, build a claim-chart first pass against
   each independent claim — element by element. Literal read first; flag
   doctrine-of-equivalents separately; flag indirect / divided infringement.
6. List open questions a real FTO study would resolve (enforceability,
   prosecution history, IPR outcomes, license availability, enforcement
   history of the assignee).
7. Write the triage memo to the matter folder or practice outputs folder. Apply
   the work-product header per role.
8. End with recommended next steps, a willfulness note (knowledge of specific
   patents factors into willfulness if the company proceeds without further
   counsel review), and the non-lawyer gate if the role is non-lawyer.

This skill never concludes that a product is clear to launch. If uncertain,
flag — patent counsel decides.

## Examples

```
/ip-legal:fto-triage "an on-device speech recognition model for consumer wearables, US launch first"
```

```
/ip-legal:fto-triage
```

---

## THIS IS NOT A FREEDOM-TO-OPERATE OPINION

**The loudest guardrail in the plugin. Say this at the top of every output. Do
not drop it. Do not soften it. Do not let the reader skim past it.**

> **This is not a freedom-to-operate opinion.** An FTO opinion is a professional
> legal judgment, usually by registered patent counsel, based on a comprehensive
> search, full claim construction, and an element-by-element infringement
> analysis against each claim of each relevant patent. This triage is a
> structured first look at what might be out there. A "no obvious blocking
> patents" result means the triage didn't find one — it does not mean the
> product is clear. Patent infringement is strict liability; willful
> infringement (which can follow from knowing about a patent and proceeding
> anyway) triples damages under 35 U.S.C. § 284. The decision to launch, make,
> use, sell, or import is a business decision informed by a formal FTO study
> and counsel's judgment — not by this triage. A registered patent attorney or
> agent evaluates before anyone relies on this for a product decision.

Under-flagging a blocking patent is a one-way door — a product launched, a
deposition a year later, treble damages on the table. Over-flagging is a
two-way door — the attorney narrows the list in a read-through. Stay on the
two-way door side. Always.

### A note on willfulness

Reading this triage is reading something about patents. Reading something about
patents can, in some circumstances, factor into a willfulness analysis down the
road. This is one reason the output is marked as privileged when a lawyer is
using it, and why the non-lawyer output is framed as research to take to
counsel. Do not discuss specific patents surfaced by this triage outside
privileged channels.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

Patent FTO matters are particularly common candidates for **clean-team** or
**heightened** confidentiality at matter-open. Respect the matter's confidentiality
marking from `matter.md`.

---

## Load the practice profile first

Before running triage, read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Pull:

- **Role** from `## Who's using this` (lawyer vs. non-lawyer changes the
  work-product header and the non-lawyer gate below).
- **Registered in** and **enforce where** from `## IP practice profile` and
  `## Enforcement posture` (useful for defensive-portfolio cross-check and for
  jurisdiction defaults).
- **Patent OC** from `## IP practice profile` → `Outside counsel roster` for
  the routing step.
- **Integrations** from `## Available integrations` — specifically Solve
  Intelligence, or any patent-research MCP. Determines what searches
  are available.
- **Decision posture** from `## Decision posture on subjective legal calls` —
  this skill never concludes "does not infringe."

If `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` contains `[PLACEHOLDER]` or `[Your Company Name]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor posture, jurisdictions, and approval chain to your practice.
>
> **Two choices:**
> - Run `/ip-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — US jurisdiction, middle risk appetite, lawyer role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," run the FTO triage normally using these generic defaults: middle risk appetite, lawyer role, US jurisdiction, no playbook (do the full analysis rather than matching against a position list). Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against default assumptions. Run `/ip-legal:cold-start-interview` to get output calibrated to YOUR practice — your playbook, your jurisdiction, your risk appetite. 2 minutes."

---

## Intake

Ask in a single batch:

> I'll run an FTO triage. A few questions first:
>
> 1. **Product, process, or feature.** What's being made, used, offered for
>    sale, sold, or imported? Describe it plainly — the technical essence, not
>    the marketing pitch.
> 2. **Technical detail.** Any architectural diagrams, claim-relevant specs, a
>    public product page, or a spec document you can share? (The more detail,
>    the more real the triage.)
> 3. **Jurisdictions.** Where will it be made, used, sold, offered for sale,
>    imported? (Each is a separate infringing act under 35 U.S.C. § 271. I'll
>    default to the US if you don't specify.)
> 4. **Known patents.** Are there patents already on your radar — a competitor's
>    portfolio, a known SEP pool, an NPE letter, something an engineer
>    mentioned?
> 5. **Timing.** How close is this to launch? If it's months out, the triage
>    is early and design-around is on the table. If it's already shipping,
>    we're in cover-our-downside mode.

Wait for the answer. If the description is vague ("an AI agent," "a database"),
push once:

> Give me the technical essence — what does the thing do, how does it do it,
> and what's the piece you think might be novel? Patent claims live at that
> level.

---

## Scope — utility patents only

**This skill analyzes utility patents.** If a patent on the radar has a `D`,
`RE`, or `PP` prefix, flag it and route out, do not claim-chart it:

- **`D` (design patent).** Different test entirely — ordinary observer under
  *Egyptian Goddess, Inc. v. Swisa, Inc.*, 543 F.3d 665 (Fed. Cir. 2008) (en
  banc), overall ornamental appearance, no claim chart. Route to the
  `infringement-triage` design patent branch and to design patent counsel.
  **Design patents are not analyzed in this FTO triage** — a design-patent
  overlap must be flagged as a separate workstream.
- **`RE` (reissue).** Treat as a utility patent with added §252 intervening-
  rights and recapture-rule flags.
- **`PP` (plant patent).** Route to plant-patent counsel; out of scope.

Also cross-flag **trade dress**: if the product's appearance is the risk,
the same facts may be a §43(a) product-configuration claim that requires
secondary meaning (*Wal-Mart Stores, Inc. v. Samara Bros., Inc.*, 529 U.S.
205 (2000)) and non-functionality (*TrafFix Devices, Inc. v. Marketing
Displays, Inc.*, 532 U.S. 23 (2001)). Flag as a parallel track.

---

## Search

### What the user has connected

Read `## Available integrations`:

- **Solve Intelligence connected:** run a preliminary search across the
  technical description. Note the date of the search, the query used, the
  jurisdictions covered, and any date window (current in-force patents; recent
  published applications).
- **Patent-research MCP (Google Patents Public Datasets, PatSnap
  export): available:** use it.
- **None of the above:** explicitly say so. Do not infer patents from model
  knowledge and present them as search results.

### Fallback when no patent database is connected

Write this exact statement in the output:

> **No patent database search was run.** This triage did not hit Solve
> Intelligence Patents, USPTO Patents Full-Text, EPO Espacenet,
> Google Patents, PatSnap, or any other patent corpus. A structured search
> across the jurisdictions in scope is required before relying on this triage
> for any launch decision. The analysis below is limited to patents and
> applications the user has named or that come up in the conversation.

Then proceed. The claim-chart-first-pass work below is still valuable — just
label the scope honestly.

### Supplementary signals (not a substitute)

If available and the user allows, sweep for non-patent signals that flag a
patent concern:

- **Competitor patent filings** around the product area.
- **Known NPE targeting** of the technology class (e.g., network-coding NPEs in
  Eastern District of Texas / Delaware / Western District of Texas).
- **Standards-essential declarations** (IEEE, ETSI, 3GPP) if the product touches
  a relevant standard.
- **Reported litigation** in the technology space (CourtListener / RECAP, Unified
  Patents, Lex Machina).

Each signal is a reason to look harder, not a patent hit. Mark them as signals
in the output, not as identified patents.

---

## For each relevant patent found or supplied

Capture:

- **Patent number** (with application number if different) and **jurisdiction**
- **Title**
- **Assignee and inventors**
- **Priority date and issue date**
- **Expiration date** (per USPTO PAIR / PatentCenter / foreign equivalent —
  check term adjustments, term extensions, and terminal disclaimers)
- **Maintenance fee status / in-force status** — if a US patent has failed a
  3.5/7.5/11.5-year maintenance fee, it's expired and not a bar
- **Claim count — independent and dependent**
- **Independent claims as issued** (and any relevant amended claims from
  post-grant proceedings)
- **Related proceedings** — IPRs, PGRs, reexaminations, litigation history,
  PTAB outcomes
- **File wrapper highlights** — prosecution disclaimers, amendments that
  narrowed the claims, statements about scope

**Do not supplement silently.** If a search surfaces a patent, attribute the
result. If the user mentioned a patent, say that. Never invent a patent
number, never "fill in" a claim element the file doesn't support, never
imagine an expiration date. If maintenance fee status isn't available, write
"maintenance fee status not verified from search result — confirm in PAIR
before relying on in-force status."

---

## Claim-chart first pass

This is the core of the triage. Pick the patents with the most plausible read
on the product — usually the 2–5 with the closest technical mapping — and walk
each independent claim element-by-element.

**For each selected patent, write out one claim chart per independent claim:**

| Claim element | Does the product practice this? | Basis |
|---|---|---|
| "A [preamble phrase]" | [yes / no / possibly / depends on construction] | [one sentence — what in the product maps; what doesn't; what's ambiguous] |
| "comprising [element 1]" | [yes / no / possibly] | [mapping or gap] |
| "wherein [element 2]" | [yes / no / possibly] | [mapping or gap] |
| [continue for every element] | | |

**Rules for the chart:**

- **Every element matters.** A claim is infringed only if the accused product
  practices every element of at least one claim (all-elements rule). Missing one
  element literally means no literal infringement on that claim. Do not skip.
- **Doctrine of equivalents is a separate pass.** First chart literal
  infringement. Then, for any "no" elements, note whether a DOE read is
  plausible (insubstantial differences / function-way-result). Flag DOE
  analysis as requiring attorney judgment — prosecution history estoppel and
  claim vitiation are common bars and the triage does not adjudicate them.
- **Claim construction is the attorney's job.** Where a term could be
  construed narrowly or broadly and the answer changes the infringement read,
  flag the term and note both constructions. Do not pick one silently.
- **Indirect infringement (induced, contributory) and divided infringement**
  are flags only. Do not attempt a full analysis; note that these may apply and
  require patent counsel.

> **Patent systems differ by jurisdiction.** The US claim chart (all-elements rule, doctrine of equivalents, prosecution history estoppel, §284/§289 damages) does not transfer to other systems:
> - **Germany:** Utility models (Gebrauchsmuster), the Schneidmesser/Kunststoffrohrteil questions for DOE, bifurcated validity/infringement proceedings.
> - **China:** Utility models (shiyong xinxing), CNIPA examination, different claim construction.
> - **Japan:** Utility models, JPO examination, a narrower DOE.
> - **Europe (unified patent court):** UPC procedure as of 2023.
>
> When non-US jurisdictions are in scope: "This analysis uses the US claim-charting framework. A product manufactured in China and sold in the EU needs CNIPA and EP analysis, not a US claim chart. I can flag the issues a US analysis surfaces, but the infringement and validity calls require [jurisdiction]-specific review."

**Decision posture:** per the practice profile, this skill never concludes "no
infringement." Either:

- "Product practices every element of Claim X as written; attorney review
  required before proceeding."
- "One or more elements are not clearly present; attorney review required to
  assess literal infringement and doctrine of equivalents."
- "Claim construction is dispositive on element [Y]; attorney construction
  required before proceeding."

---

## Open questions

Every patent surfaced in the triage should produce a list of open questions
that a real FTO study would answer. Examples:

- Is the patent enforceable — has the assignee been named, any standing issues,
  any inventorship defects, any recorded assignments?
- What did the applicant say about term [X] in prosecution, and does that
  limit the claim?
- Has this claim been the subject of an IPR or reexamination — what did the
  PTAB say about scope or validity?
- Is there a license already available (standards pool, patent marking, open
  patent non-assertion commitment)?
- What's the real-world enforcement history of this assignee?

List them plainly.

---

## Recommended next steps

Bucket by what the triage found:

- **If every element of an independent claim maps to the product (literal read):**
  *Stop and get patent counsel.* Options typically include formal FTO opinion,
  design-around, license, challenge validity (IPR/PGR), or (rarely) proceed at
  risk. The choice is a business decision informed by counsel.
- **If elements cut both ways or claim construction is dispositive:**
  Full FTO study by registered patent counsel. Do not launch on this triage.
- **If the patent appears expired, abandoned, or unenforceable:** Attorney
  confirms the in-force status — the triage does not.
- **If no patents were identified in the search but no database access
  existed:** Formal search is the next step, not a launch decision.
- **Always:** flag a willfulness risk. If the triage surfaces a specific
  patent, the company now has knowledge of it. Proceeding without further
  analysis can support a willfulness finding. Counsel should document the
  path forward.

---

## Output format

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` `## Outputs`. Mark the document as privileged if the role is lawyer; see the non-lawyer gate below if not.

```markdown
[WORK-PRODUCT HEADER]

# FTO Triage — First Pass (NOT AN OPINION)

**This is not a freedom-to-operate opinion.** A formal FTO opinion requires a
comprehensive search, full claim construction, and element-by-element
infringement analysis by registered patent counsel. Patent infringement is
strict liability; willful infringement triples damages. A "no obvious blocking
patents" result means the triage didn't find one — it does not mean the product
is clear. A registered patent attorney or agent evaluates before anyone relies
on this for a product decision.

**Triage result:** [GREEN / YELLOW / RED — one sentence why]

## Subject

- **Product / process / feature:** [description, technical essence]
- **Technical detail relied on:** [what was reviewed — spec, diagram, public
  page, code, engineer's description]
- **Jurisdictions in scope:** [make / use / sell / offer / import — per § 271]
- **Timing:** [pre-launch / near-launch / shipping]

## Search scope

- **Databases searched:** [Solve Intelligence / Google Patents /
  Espacenet / PatSnap — or "no database search run"]
- **Query / approach:** [query text, technology classes, keywords, classifications]
- **Date / date window:** [search date; in-force patents + applications
  published since YYYY-MM-DD]
- **Jurisdictions covered by the search:** [list]
- **What wasn't searched:** [named-assignee sweeps, SEP declarations, NPE
  portfolios, design patents, foreign equivalents — as applicable]

*If no database search was run:* **No patent database search was run.** This
triage did not hit Solve Intelligence Patents, USPTO Patents Full-Text,
EPO Espacenet, Google Patents, PatSnap, or any other patent corpus. A
structured search across the jurisdictions in scope is required before
relying on this triage for any launch decision.

## Patents identified

| Patent | Jurisdiction | Assignee | Priority / Issue | Expiration | In-force? | Source |
|---|---|---|---|---|---|---|
| [number] | [US/EP/...] | [assignee] | [dates] | [date] | [yes/no/unverified] | [search result link or "user-supplied"] |

## Claim charts — first pass

### [Patent number] — independent Claim [N]

> "[Exact text of Claim N]"

| Element | Practiced by the product? | Basis |
|---|---|---|
| [element 1] | [yes/no/possibly] | [mapping or gap] |
| [element 2] | [yes/no/possibly] | [mapping or gap] |

**Literal read:** [every element maps / one or more elements do not clearly
map / claim construction is dispositive on element [Y]]

**Doctrine of equivalents (flag only):** [DOE read plausible on element [Y] —
attorney construction required / not plausible on the surfaced elements /
prosecution history suggests estoppel]

**Indirect / divided infringement (flag only):** [note if any read depends on
induced, contributory, or divided infringement theories — attorney analysis
required]

*(Repeat for each independent claim of each selected patent.)*

## Open questions

- [question 1]
- [question 2]

## Signals (not confirmed patents)

- [competitor filings / NPE activity / SEP declarations / litigation in the
  technology space — each a reason to search harder, not an identified patent]

## Recommended next steps

- [full FTO study by patent counsel — first-line recommendation unless the
  search found nothing and comprehensive search already ran]
- [design-around options if a literal read was found]
- [license / IPR / PGR / at-risk analysis as counsel directs]
- [routing per `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` —
  patent OC named in the practice profile]

## Willfulness note

This triage surfaces specific patents. Proceeding with the product without
further counsel review after this knowledge can support a willfulness finding
and enhanced damages under § 284. The path forward should be documented by
patent counsel; the business decision to launch, design around, or license is
informed by a formal FTO opinion and counsel's judgment, not by this triage.

## Citation verification

Every patent number, claim quote, date, and prosecution fact in this memo must
be verified against the authoritative source (USPTO PatentCenter / PAIR, EPO
register, national equivalent) before relying on it. Claim quotes are the
most common error site — a single word changes the analysis. Do not cite a
result you cannot open.
```

---

## Non-lawyer gate

Before issuing the output, read `## Who's using this`. If the Role is Non-lawyer:

> This output is a research triage, not legal advice. Launching, continuing to
> sell, or investing in this product based on this triage alone has legal
> consequences — including strict liability for patent infringement, with
> enhanced damages for willfulness. Patent counsel needs to evaluate before
> you move.
>
> Here's a brief to bring to an attorney — it'll cut the time the conversation
> takes:
>
> [Generate a 1-page summary: the product description, the jurisdictions in
> scope, the search run (and what wasn't searched), the patents surfaced and
> the claim-chart-first-pass reads, the open questions, and the three
> questions to ask the attorney.]
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: for US patent work, a registered patent attorney or patent agent is required (not every lawyer is registered — the USPTO
> Office of Enrollment and Discipline maintains a directory). For other jurisdictions, use the relevant patent office register (EPO, UK IPO, etc.). Your professional regulator's referral service is a starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent); specifically ask for registered
> patent counsel.

Deliver the full triage memo alongside the brief. Do not withhold the analysis.
Flag that the triage itself is a privileged research document and should not
be forwarded to non-attorney third parties.

---

## Output location

If matter workspaces are enabled and a matter is active, write the output to
`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`.
Otherwise write to
`~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`
and surface the path.

Append a one-line entry to the matter's `history.md` if a matter is active.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- **Issue an FTO opinion.** Ever. The loudest guardrail in the plugin.
- **Construe claims.** Where construction is dispositive, it flags the term and
  both plausible constructions. It does not pick one.
- **Adjudicate validity.** It may note known PTAB proceedings; it does not
  opine on novelty, obviousness, § 112, § 101, or enablement.
- **Draft patent claims.** This plugin does not go there; route to prosecution
  counsel.
- **Assess damages exposure.** Damages modeling is an expert's job.
- **Handle trade-secret or trademark analysis** — use `/ip-legal:infringement-triage`
  with the right mode.
- **Quote outputs to counterparties or non-privileged audiences.** This is a
  privileged research document.

---

## Tone

Technically precise. Element-by-element. Every flag is specific to a claim
element or a known patent. No hedging prose in the body — the guardrails at
the top and bottom do the scope work, and the analysis does the analysis. The
reader should leave knowing what the triage looked at, what it didn't, and
what the next step is.

---

## /ip-legal:infringement-triage

---
name: infringement-triage
description: >
  Infringement triage across trademark, copyright, patent, and trade secret —
  a flag list with the factors cutting each way, not a finding. Use when
  assessing whether someone is infringing your IP or whether you might be
  infringing theirs, when a knockoff or copycat surfaces, or when deciding
  whether a matter is worth pursuing and how.
argument-hint: "[describe the facts and which right — or just the facts and I'll ask which right]"
---

# /infringement-triage

**This is a triage, not a finding of infringement or non-infringement.**
Infringement analysis is fact-intensive and legally complex. Acting on a
triage — sending a cease-and-desist, refusing to stop, filing suit, or
deciding not to — without attorney review is how companies end up on the
wrong side of fee awards, Rule 11 sanctions, declaratory-judgment actions,
and (for patents) treble damages.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal:cold-start-interview`.
2. Follow the workflow below.
3. Ask which right is at issue — trademark / copyright / patent / trade secret
   / mixed. If mixed, run each separately; do not blend.
4. Run common intake (party posture — senior or accused, jurisdiction, timing,
   exhibits).
5. Walk the mode-specific factors:
   - **Trademark** — circuit's confusion test + dilution (if famous) +
     false advertising (if a comparative claim).
   - **Copyright** — ownership + registration + access + substantial
     similarity + fair use + DMCA safe harbor (if applicable).
   - **Patent** — claim-chart first pass (route to `fto-triage` output
     structure); literal + DOE; indirect + divided; invalidity defenses to
     consider.
   - **Trade secret** — secrecy + reasonable measures + misappropriation;
     preemption + reverse-engineering flags.
6. Produce a flag list with direction — what cuts toward the senior party,
   what cuts toward the accused, what's mixed. Never conclude.
7. Write the triage memo to the matter folder or practice outputs folder. Apply
   the work-product header per role.
8. End with recommended next steps, the non-lawyer gate if the role is
   non-lawyer, and — if the practice posture supports assertion — an offer to
   draft the C&D via `/ip-legal:cease-desist` or the takedown via
   `/ip-legal:takedown`. Do not draft automatically.

This skill never concludes. If uncertain, flag — the attorney decides.

## Examples

```
/ip-legal:infringement-triage "competitor launched a tool called APEXSEED in class 9 — we have APEXLEAF registered in class 9; likely confusion?"
```

```
/ip-legal:infringement-triage "former engineer took notes on our model architecture to a competitor — possible trade secret?"
```

```
/ip-legal:infringement-triage
```

(And the skill will ask which right and for the facts.)

---

## THIS IS A TRIAGE, NOT A FINDING

**The loudest guardrail in the plugin. Say this at the top of every output. Do
not drop it. Do not soften it.**

> **This is a triage, not a finding of infringement or non-infringement.**
> Infringement analysis is fact-intensive and legally complex. The triage
> identifies the factors and flags the ones that matter most; it does not
> conclude. A conclusion that something does or does not infringe is a legal
> opinion that requires an attorney's judgment on the facts, the claim or
> right scope, the relevant jurisdiction's law, and the likely defenses.
> Acting on a triage — sending a cease-and-desist, refusing to stop, filing
> suit, or deciding not to — without attorney review is how companies end up
> on the wrong side of fee awards, Rule 11 sanctions, declaratory-judgment
> actions, and (for patents) treble damages.

Under-calling a conflict is a one-way door — a C&D not sent and a mark goes
generic in the market; a claim not chased and the statute of limitations runs;
a copied copyrighted work kept on the site. Over-calling is a two-way door —
the attorney narrows. Stay on the two-way door side.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

Infringement triages often lead into cease-and-desist drafting or takedown
routing. Open a matter if one isn't active and the practice is private — the
triage, the C&D, and any downstream response belong in one workspace.

---

## Load the practice profile first

Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Pull:

- **Role** from `## Who's using this`.
- **Enforcement posture** from `## Enforcement posture` — the triage output
  should end with a routing suggestion consistent with the stated posture
  (aggressive / measured / conservative) and the named approver for the
  relevant letter type.
- **Registered in / enforce where** from `## IP practice profile` — determines
  which circuit / jurisdiction test to apply by default.
- **Integrations** from `## Available integrations` — CourtListener,
  Solve Intelligence each affects whether the triage can cite to case law,
  prior rulings, or prior art.
- **Decision posture** from `## Decision posture on subjective legal calls` —
  this skill never concludes on a subjective threshold.

If the config has `[PLACEHOLDER]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor posture, jurisdictions, and approval chain to your practice.
>
> **Two choices:**
> - Run `/ip-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll run this tailored to YOUR practice.
> - Say **"provisional"** and I'll run this against generic defaults — US jurisdiction, middle risk appetite, lawyer role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," run the infringement triage normally using these generic defaults: middle risk appetite, lawyer role, US jurisdiction, no playbook (do the full analysis rather than matching against a position list). Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against default assumptions. Run `/ip-legal:cold-start-interview` to get output calibrated to YOUR practice — your playbook, your jurisdiction, your risk appetite. 2 minutes."

---

## Mode selection

Ask at the top, before anything else:

> Which right are we triaging?
>
> 1. **Trademark** — confusion, dilution, or false advertising
> 2. **Copyright** — substantial similarity, fair use, DMCA safe harbor
> 3. **Patent** — claim-chart first pass, literal read + doctrine of equivalents
> 4. **Trade secret** — secrecy, reasonable measures, misappropriation
> 5. **Mixed / not sure** — describe the facts and I'll pick

If the user picks "not sure," help them sort. The same facts can implicate
multiple rights (e.g., a competitor's product uses our logo — trademark; and
the product is a near-copy of ours — possible patent, copyright on packaging,
possible trade dress; and a former employee launched it — trade secret).

**If more than one right is in play, run the triage for each, separately.**
Don't mash them together. Each right has different factors, different
jurisdictional rules, and different remedies.

---

## Intake (common to all modes)

> Before I walk factors:
>
> 1. **Posture.** Are you the potentially senior party (they're taking
>    yours) or the potentially accused party (we're the ones being looked at)?
>    The factors are symmetric but the output differs — a "mine's being
>    copied" triage routes toward an assertion letter; a "we might be
>    exposed" triage routes toward a risk memo.
> 2. **Jurisdiction.** Which country / circuit / court? US federal default if
>    not specified. Flag if foreign law may apply.
> 3. **Timing.** Is a statute of limitations or laches clock running?
> 4. **What exhibits / evidence / source documents do you have?** A screenshot,
>    a URL, a packaging photo, a code excerpt, an ex-employee contract.

Wait for the answer before walking factors.

---

## Trademark mode

### Confusion

Use the applicable circuit's multi-factor test. Cite the test (du Pont /
Polaroid / Sleekcraft / other — see the `clearance` skill for the case
citations and pick logic). Walk each factor and flag what cuts each way.

- **Similarity of marks** — sight / sound / meaning / commercial impression.
- **Similarity of goods or services** — expected-source test, not identity.
- **Channels of trade.**
- **Consumer sophistication.**
- **Strength of the senior mark** — fanciful / arbitrary / suggestive /
  descriptive with secondary meaning / generic.
- **Intent** — evidence of copying, knock-off trade dress, near-miss mark.
- **Actual confusion** — any evidence (surveys, misdirected inquiries, social).
- **Likelihood of expansion / bridge-the-gap** — whether the zones overlap
  commercially.

### Dilution

Apply the federal TDRA (15 U.S.C. § 1125(c)) and any applicable state statute.

- **Fame threshold.** The senior mark must be famous to the general consuming
  public — a niche-famous mark is not enough. *Starbucks Corp. v. Wolfe's
  Borough Coffee, Inc.*, 588 F.3d 97 (2d Cir. 2009) is representative.
- **Blurring vs. tarnishment.** Blurring = distinctiveness harm; tarnishment
  = reputation harm.
- **Defenses** — comparative advertising, news reporting, fair use,
  non-commercial use.

If the senior mark is not plainly famous nationally, flag dilution as a
stretch.

### False advertising / comparative claims

If the triage is prompted by a competitor's comparative ad or a claim about
product attributes:

- Apply Lanham Act § 43(a) / 15 U.S.C. § 1125(a) for the materiality,
  falsity-or-misleading, deception, commercial-speech, and injury elements.
- Flag whether the statement is literally false, implicitly false, or
  puffery. Puffery is not actionable.
- Substantiation evidence the claimant has or needs.

### Output

Factors table; what cuts each way; a "not a finding" conclusion line. End with
a routing suggestion against the enforcement posture in the practice profile.

---

## Copyright mode

### Ownership

Is the claimant the owner (or exclusive licensee with standing)? Work-for-hire
issues; joint authorship; assignments; and termination rights all flag.

### Registration

17 U.S.C. § 411 requires registration (or preregistration) as a precondition
to filing an infringement action in US federal court. *Fourth Estate Public
Benefit Corp. v. Wall-Street.com, LLC*, 586 U.S. 296 (2019) — registration
means actually issued, not just applied for. Flag registration status; if
not registered, flag the practical bar on filing.

### Access + substantial similarity

Two paths to proving copying:

- **Access + probative similarity** — defendant had access and the works share
  features probative of copying.
- **Striking similarity** — even absent proof of access, the similarity is so
  striking that independent creation is unlikely.

For substantial similarity, apply the circuit's test (Second Circuit's
ordinary-observer; Ninth Circuit's extrinsic / intrinsic under *Krofft* and
*Swirsky*; Fourth / Seventh / Eleventh circuits' variations). Flag which
test applies.

### Fair use

17 U.S.C. § 107 four factors, analyzed as a whole:

1. Purpose and character of the use (transformativeness; commercial vs.
   non-commercial).
2. Nature of the copyrighted work (factual / functional vs. creative).
3. Amount and substantiality of the portion used.
4. Effect on the market for the original.

Recent touchstones: *Google LLC v. Oracle America, Inc.*, 593 U.S. 1 (2021);
*Andy Warhol Found. for the Visual Arts, Inc. v. Goldsmith*, 598 U.S. 508
(2023). Flag the transformativeness analysis carefully — *Warhol* narrowed
the scope of transformative use and is still being applied by lower courts.

### DMCA safe harbor

17 U.S.C. § 512. If the accused is a service provider hosting user content,
flag whether § 512(c) applies: designated agent, notice-and-takedown
procedure, no actual or red-flag knowledge, no financial benefit
attributable to infringement the provider could control, expeditious
takedown on valid notice. Repeat-infringer policy required. Safe harbor does
not cover direct infringement by the service provider itself.

### Output

Factors flagged; fair-use balance with "the triage does not conclude";
ownership / registration / safe-harbor threshold notes. Routing per posture.

---

## Patent mode

**Route to `/ip-legal:fto-triage` for the detailed framework.** This mode is the
mirror image of the FTO skill — same claim charts, same doctrine-of-equivalents
flag, same all-elements rule — applied to an accused product instead of one's
own.

### Design patent (D-number) — branch before the workflow

**Check the asserted patent's registration number FIRST.** If it has a `D`,
`RE`, or `PP` prefix (e.g., `D712,345`), it's not a utility patent and the
workflow below does NOT apply. Branch per prefix:

- **`D` prefix — design patent (35 U.S.C. §171).** Different test, different
  claim structure, different damages. Do NOT build a claim chart, do NOT run
  doctrine of equivalents, do NOT do element-by-element mapping. Design
  patents have a single claim defined by the drawings; charting a figure as
  if it were a utility claim element list is wrong doctrine.
- **`RE` prefix — reissue patent.** Treat as the utility patent it reissued,
  but flag reissue-specific defenses (intervening rights under §252,
  recapture rule, original-patent requirement).
- **`PP` prefix — plant patent.** Separate regime (35 U.S.C. §161). Asexually
  reproduced plant varieties. Route to plant-patent counsel; this skill does
  not analyze plant patents.

**Design patent infringement test — ordinary observer.** *Egyptian Goddess,
Inc. v. Swisa, Inc.*, 543 F.3d 665 (Fed. Cir. 2008) (en banc). The question
is whether an ordinary observer, **familiar with the prior art designs**,
would be deceived into thinking the accused design is the same as the
patented design. Compare **overall ornamental appearance**, not individual
elements. The accused product must appropriate the **novelty** that
distinguishes the patented design from the prior art (the "point of novelty"
survives as a guidepost inside the ordinary-observer test, not as a separate
test).

**Functional-vs-ornamental filter.** Design patents protect ornamental
features only; functional features are not protected. If the accused
similarity is in features dictated by function, flag that the overlap may
fall outside the patented scope.

**§289 total-profit damages flag.** Design patent damages under 35 U.S.C.
§289 are the infringer's **total profits on the "article of manufacture,"**
which can be the whole product or a component. *Samsung Electronics Co. v.
Apple Inc.*, 580 U.S. 53 (2016). This is a separate analysis from utility
patent reasonable-royalty / lost-profits and is specialist work — do not
compute.

**Trade dress cross-flag.** The same ornamental-shape facts are usually also
a **trade dress** question under Lanham Act §43(a) (15 U.S.C. §1125(a)).
Product configuration trade dress requires **secondary meaning** (*Wal-Mart
Stores, Inc. v. Samara Bros., Inc.*, 529 U.S. 205 (2000)) and must be
**non-functional** (*TrafFix Devices, Inc. v. Marketing Displays, Inc.*,
532 U.S. 23 (2001)). Flag trade dress as a parallel track; the tests are
different but the evidence overlaps.

### Design patent triage — output

Because you cannot see the patent drawings or the accused product directly,
the design patent triage is mostly a request for the materials and a frame
for the analysis:

- **Ask for the drawings.** "I can't run the ordinary-observer test without
  seeing the patent figures and the accused product. Paste or attach: (a)
  the patent drawings (all figures, including any broken-line disclaimers),
  (b) photos of the accused product from comparable angles, (c) any prior
  art designs you're aware of."
- **Prior-art landscape.** Ordinary observer is a *comparison* test — the
  observer is "familiar with the prior art," so the scope of the patented
  design narrows as the prior-art field crowds. Flag what prior art is
  known and what's missing.
- **Functional-vs-ornamental analysis.** Walk the features and flag which
  look functional (and therefore unprotected) vs. ornamental.
- **Broken lines.** Design patents use solid lines for claimed features and
  broken lines for unclaimed environmental context. Flag whether the
  alleged copying is in claimed (solid-line) or unclaimed (broken-line)
  territory.
- **§289 damages flag** as above.
- **Trade dress cross-flag** as above.

**Route to a design patent specialist for anything beyond first-pass triage.**
Design patent litigation is a subspecialty (Perkins Coie, Sterne Kessler,
Desmarais, Kirkland's design team, Gibson Dunn's design group are
representative; use your practice profile's IP litigation OC as the starting
point). This skill flags issues; it does not assess infringement.

### Utility patent workflow

The rest of this mode assumes the asserted patent is a **utility patent**
(no `D`/`RE`/`PP` prefix). If the D-number branch above applies, stop here.

> **Patent systems differ by jurisdiction.** The US claim chart (all-elements rule, doctrine of equivalents, prosecution history estoppel, §284/§289 damages) does not transfer to other systems:
> - **Germany:** Utility models (Gebrauchsmuster), the Schneidmesser/Kunststoffrohrteil questions for DOE, bifurcated validity/infringement proceedings.
> - **China:** Utility models (shiyong xinxing), CNIPA examination, different claim construction.
> - **Japan:** Utility models, JPO examination, a narrower DOE.
> - **Europe (unified patent court):** UPC procedure as of 2023.
>
> When non-US jurisdictions are in scope: "This analysis uses the US claim-charting framework. A product manufactured in China and sold in the EU needs CNIPA and EP analysis, not a US claim chart. I can flag the issues a US analysis surfaces, but the infringement and validity calls require [jurisdiction]-specific review."

### Workflow

- Accused product / process / method — described in technical detail.
- Identified patent(s) at issue.
- Claim chart for each independent claim: element-by-element mapping to the
  accused product.
- Literal infringement first. DOE as a flag.
- Indirect (induced, contributory) and divided infringement as flags.
- **Invalidity defenses to consider** — anticipation (§ 102), obviousness
  (§ 103), § 112 written-description / enablement / definiteness, § 101
  subject-matter eligibility (*Alice* / *Mayo*). Known IPR or PGR outcomes,
  known prior art, known prosecution history. Flag each; do not opine.
- **Unenforceability defenses** — inequitable conduct flag, prosecution
  laches flag, assignor / licensee estoppel flag. Each is attorney-only.
- **Damages posture** — lost profits vs. reasonable royalty (Georgia-Pacific
  factors), marking, pre-suit notice, willfulness (reading this triage may
  factor into willfulness — see the FTO skill's willfulness note).

### Output

Claim charts. Element flags. Defense flags. Routing to patent counsel. See
the `fto-triage` skill for the full output structure — the infringement-triage
patent mode uses the same format with "accused product" substituted for
"own product."

### Handoff to the full claim chart

For a detailed element-by-element claim chart suitable for infringement or
invalidity contentions, run `/litigation-legal:claim-chart`. This triage's
claim chart is a first pass to identify the strongest and weakest mappings;
the litigation claim chart builds the full chart with pin cites, claim
construction flags, dependent claims, and the verification workflow that
contentions require.

---

## Trade secret mode

### Was it a secret?

Apply the Defend Trade Secrets Act (18 U.S.C. § 1836 et seq.) for federal
purposes and the applicable state UTSA (or, in New York / Massachusetts /
other non-UTSA jurisdictions, the state's common-law test). Flag:

- **Not generally known** — to the public or to others in the industry who can
  obtain economic value from disclosure.
- **Economic value from secrecy** — independent economic value actual or
  potential, derived from not being generally known.
- **Combinations and compilations** — a combination of public elements can
  be a trade secret (*Altavion v. Konica Minolta*, and the Restatement view).

### Reasonable measures

- NDAs with employees, contractors, counterparties. Scope, signed, enforced?
- Access controls — technical (role-based), physical (doors, badges),
  organizational (need-to-know).
- Marking — confidentiality legends on documents, code, data.
- Exit interviews / return of materials on termination.
- Trade-secret policy / training.

Flag what's in place and what's missing. *Reasonable* is fact-specific; the
triage does not decide whether the measures were reasonable — it lists them.

### Misappropriation

Acquisition by improper means, or disclosure / use in breach of duty.
Improper means includes theft, bribery, misrepresentation, breach or
inducement of breach of a duty to maintain secrecy, or espionage (electronic
or otherwise). 18 U.S.C. § 1839(6).

- **Former employee fact pattern:** new employer, overlapping work,
  departure timing, documents taken (and returned?), access logs, recruiting
  channels, assignment and invention-assignment agreements.
- **Inadvertent disclosure:** Was disclosure made by a person with a duty? Did
  the recipient know or have reason to know of the breach?
- **Reverse engineering** — a defense if the means were lawful. Flag whether
  reverse engineering is plausible on the facts.

### Preemption

Where state tort claims (unfair competition, conversion, breach of confidence)
might be preempted by the UTSA, flag preemption. Some jurisdictions preserve
contract claims; others preempt most tort claims addressing the same facts.

### Output

Three flag groups — secrecy, measures, misappropriation — each with what cuts
each way. Routing per posture.

---

## Output format (all modes)

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` `## Outputs`.

```markdown
[WORK-PRODUCT HEADER]

# Infringement Triage — [Trademark | Copyright | Patent | Trade Secret] (NOT A FINDING)

**This is a triage, not a finding of infringement or non-infringement.** The
triage identifies factors and flags what matters most; it does not conclude.
A conclusion requires an attorney's judgment on the facts, the right scope,
jurisdiction, and defenses. Acting on a triage without attorney review is
how companies end up on the wrong side of fee awards, Rule 11 sanctions,
declaratory-judgment actions, and enhanced damages.

**Triage result:** [GREEN / YELLOW / RED — one sentence why]

## Posture and scope

- **Party posture:** [senior / accused]
- **Right at issue:** [trademark / copyright / patent / trade secret]
- **Jurisdiction:** [US federal — specific circuit / state / foreign]
- **Legal framework applied:** [cite the governing test and statute]
- **Statute of limitations / laches posture:** [clock status]
- **Exhibits / evidence reviewed:** [list]

## Factor analysis

[Mode-specific factor table — confusion factors / fair-use factors / claim chart
/ trade-secret elements. Each factor has a flag and a direction. This is
a flag list, not a verdict.]

## Defenses and thresholds

[Mode-specific: dilution fame threshold / registration prerequisite /
§ 512 safe harbor / invalidity / inequitable conduct / preemption /
reverse-engineering / consent / license / laches / statute of limitations.
Flag each.]

## What cuts which way — summary

| Factor | Flag | Direction (senior / accused / mixed) |
|---|---|---|
| [factor 1] | [note] | [direction] |

**Conclusion:** *This skill does not conclude.* Attorney judgment required
before acting. The factors cutting [direction] are [brief summary]; the
factors cutting [direction] are [brief summary].

## Recommended next steps

- [formal opinion from counsel / route to IP OC named in the practice profile]
- [evidence preservation and hold — if a litigation clock is running]
- [fact development needed before a decision — e.g., access logs, prosecution
  history, market studies, survey evidence]
- [routing per `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`
  `## Enforcement posture`, if the posture is to assert]

## Citation verification

Every case, statute, registration number, claim quote, and exhibit cited here
must be verified against the authoritative source before relying on it.
Jurisdictional tests vary by circuit and change over time — confirm the
current controlling authority.
```

---

## Non-lawyer gate

Before issuing the output, read `## Who's using this`. If the Role is Non-lawyer:

> This output is a research triage, not legal advice. Sending a C&D, deciding
> not to stop, filing suit, or relying on "it's fair use" based on this triage
> alone has legal consequences — including Rule 11 sanctions for a baseless
> assertion, declaratory-judgment exposure for a threatening letter, treble
> damages on the patent side, and fee awards in unfair-competition cases.
> An attorney needs to evaluate before you move.
>
> Here's a brief to bring to an attorney:
>
> [Generate a 1-page summary: the right at issue, the posture, the facts and
> evidence, the factors surfaced, the defenses flagged, and the three
> questions to ask the attorney.]
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is
> the starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent). For patents in the US, the attorney must be registered before the
> USPTO; for other jurisdictions, use the relevant patent office register. For trademarks, INTA maintains a directory of practitioners worldwide.

Deliver the triage alongside the brief.

---

## Output location

If matter workspaces are enabled and a matter is active, write to
`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/infringe-<mode>-<subject-slug>-YYYY-MM-DD.md`.
Otherwise write to
`~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/infringe-<mode>-<subject-slug>-YYYY-MM-DD.md`
and surface the path.

Append a one-line entry to the matter's `history.md` if a matter is active.

---

## Handoff to enforcement skills

If the triage output points toward an assertion and the practice profile's
posture supports it, offer:

> Want me to draft a cease-and-desist on this? Run `/ip-legal:cease-desist`.
> I'll use the flag list from this triage as the factual basis and apply the
> approval chain from your practice profile — the letter won't go anywhere
> without the approver signing off.

Or, if the mode is copyright and the accused is hosted content:

> Want me to prepare a DMCA takedown? Run `/ip-legal:takedown`.

Do not draft the letter automatically from the triage. The decision to assert
is the approver's, not the triage's.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- **Conclude infringement or non-infringement.** Ever. The loudest guardrail.
- **Substitute for survey evidence, damages experts, or claim construction.**
- **Evaluate jurisdiction-specific defenses outside the triage's jurisdiction
  scope.** If the facts cross borders, flag that foreign-law analysis is
  required.
- **Decide fair use as a matter of law.** Fair use is fact-intensive and
  reserved for the attorney and, ultimately, the court.
- **Draft the C&D, takedown, or complaint.** Those are separate skills
  (`/ip-legal:cease-desist`, `/ip-legal:takedown`) gated by the approval
  chain in the practice profile.
- **Quote outputs to counterparties.** Privileged if the header applies.

---

## Tone

Factor-by-factor, flag-by-flag. No hedging prose. The guardrail at the top
does the scope work; the analysis does the analysis. A lawyer should leave
the output knowing exactly which factors are flagged, which defenses apply,
and what they need to do next to either assert or stand down.

---

## /ip-legal:invention-intake

---
name: invention-intake
description: >
  Invention disclosure first-pass screen — novelty, obviousness, §101
  eligibility, bar dates, detectability, and strategic value. Use when an
  invention disclosure comes in and needs triage on whether to pursue a
  prior-art search and patent counsel review, investigate further, or decline.
argument-hint: "[paste or describe the invention disclosure — or just the title and I'll ask]"
---

# /invention-intake

**This is a first-pass screen by a non-specialist, not a patentability
opinion.** The screen never concludes that an invention is patentable — it
concludes that it passes the initial screen and warrants a prior-art search
and registered-practitioner review, that it needs more information, or that
it hits a disqualifier. A prior-art search is a separate step; this skill
does not do one.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it
   contains `[PLACEHOLDER]`, stop and direct to `/ip-legal:cold-start-interview`. If the
   practice profile shows trademark- or copyright-only (no patent practice),
   say so and route the user elsewhere — this is the wrong tool.
2. Follow the workflow below.
3. Run intake. If the user pasted or uploaded a disclosure, read it. If not,
   ask the seven intake questions (what / problem / differences / inventors /
   public disclosure / status / technology area) in one batch and wait.
4. Run the six screens: novelty signals, obviousness flags, § 101 eligibility,
   public disclosure / bar dates, detectability, strategic value. Each screen
   gets a ✓ / 🟡 / 🔴 verdict with one-line reasoning.
5. Write the invention screen memo to the matter folder (if a matter is
   active) or the practice outputs folder. Apply the work-product header per
   role.
6. Bottom-line verdict: **PURSUE** (schedule prior-art search and attorney
   review) / **INVESTIGATE** (needs more info on a specific open item) /
   **DECLINE** (state the concrete reason). Never say "patentable."
7. Close with the decision tree (prior-art search / inventor follow-up /
   specialist review / decline + thank-you / trade-secret route) and the
   non-lawyer gate if the role is non-lawyer.
8. If the screen hit a within-one-year US disclosure or any public disclosure
   with foreign rights in scope, flag at the top: **time-sensitive**.

This skill never concludes that an invention is patentable. If uncertain,
flag — a registered patent attorney or agent decides.

## Examples

```
/ip-legal:invention-intake "a new cache-eviction algorithm that uses a learned model rather than LRU; conceived Q1 this year, not yet disclosed, engineering prototype in internal staging"
```

```
/ip-legal:invention-intake
```

(And the skill will ask for the invention, the problem it solves, how it
differs, inventors, public disclosure status, usage status, and technology
area.)

---

## THIS IS A FIRST-PASS SCREEN, NOT A PATENTABILITY OPINION

**Say this at the top of every output. Do not drop it, do not soften it.**

> **This is a first-pass screen by a non-specialist, not a patentability
> opinion.** A patentability opinion requires a prior-art search, full claim
> construction, and the judgment of a registered patent attorney or agent. This
> screen does not do a prior-art search, does not assess what is in the art, and
> does not construct claims. It screens for the obvious disqualifiers (the
> invention is already on the market, it was publicly disclosed two years ago,
> it is plainly an abstract idea) and the obvious go-aheads (new mechanism,
> technical advance, recent conception, in-use secretly). Everything in between
> needs a prior-art search and a registered practitioner's review. This screen
> never concludes that something is "patentable" — it concludes that it "passes
> the initial screen, warrants investigation" or that it does not.

Under-flagging an invention that should have been filed is a one-way door — the
one-year US bar runs, foreign rights are lost at first public disclosure, the
competitor files first. Over-flagging just means a prior-art search that comes
back empty. Stay on the two-way door side.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level
CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest
of this paragraph — skills use practice-level context and the matter machinery
is invisible. If enabled and there is no active matter, ask: "Which matter is
this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Load
the active matter's `matter.md` for matter-specific context and overrides.
Write outputs to the matter folder at
`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`.
Never read another matter's files unless `Cross-matter context` is `on`.

Invention disclosures are particularly common candidates for **clean-team** or
**heightened** confidentiality at matter-open. Respect the matter's
confidentiality marking from `matter.md`. Invention content is inherently
sensitive — do not summarize, quote, or reference it outside privileged
channels.

---

## Load the practice profile first

**Before reading the disclosure, read
`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`.** If it is
missing or still contains placeholders, stop and run `/ip-legal:cold-start-interview`. The
practice profile tells you:

- The company's **patent filing strategy** — offensive (building an assertion
  portfolio), defensive (filing to protect freedom to operate), hybrid, or
  licensing-revenue. This determines the strategic-value bar.
- The **technology areas of interest** — where the company files and where it
  does not. An invention that falls outside the areas of interest is often a
  decline even if the technical screen is clean.
- The **filing budget posture** — aggressive (file everything that passes the
  screen), selective (file the best few), or minimal (only what the business
  needs to protect). This shapes the output's recommendation.
- The **approval chain** — who signs off on a filing decision, and who the
  invention gets routed to if it passes the screen.

If the practice profile shows trademark-only or copyright-only (no patent
practice), this skill is the wrong tool — say so and route the user elsewhere.

---

## Workflow

### Step 1: Intake the disclosure

If the user pastes or uploads a disclosure, read it. If not, ask — in one
batch, not one at a time:

> To screen this, I need:
>
> 1. **What is the invention?** In plain language — what does it do, what makes
>    it work, what is the key idea.
> 2. **What problem does it solve?** What was broken or missing before.
> 3. **How does it differ from what existed before?** What did people do
>    previously? What does this do differently?
> 4. **Who invented it, and when?** Names and rough conception date.
> 5. **Has it been publicly disclosed?** Published, sold, offered for sale,
>    demonstrated at a conference, shown to a customer under an NDA, posted to
>    a public repo, written up in a paper, included in a product release note.
>    If yes, when and where.
> 6. **Is it in use or planned?** Shipping now? In a limited pilot? On the
>    roadmap? Still on paper?
> 7. **What technology area?** (Software, hardware, mechanical, biotech,
>    method-of-doing-business, AI/ML, etc.)

Wait for answers. Do not proceed on a half-disclosure — a screen of "a new
machine learning thing that helps users" is worse than no screen.

If the disclosure is a formal invention disclosure form (IDF) from an IPMS or
a template, extract these fields from the form and only ask for what's missing.

### Step 2: Screen against the checklist

Walk the five screens in order. Each produces a per-screen verdict:
`✓ clear`, `🟡 flagged — needs further look`, or `🔴 red flag`. Explain the
reasoning briefly; do not pad.

#### Screen 1: Novelty signals

Does the disclosure describe something new? This is not a full novelty
analysis — that requires a prior-art search. This screens the disclosure's own
description for self-evident novelty problems.

**Red flags (🔴):**
- "We just applied [known technique] to [new domain]" — e.g., "we took
  gradient boosting and applied it to predicting customer churn"
- "It's like [existing product] but for [X]" — Uber-for-dog-walking framing
- "Competitors do something similar" — if the disclosure itself says this,
  novelty is in question
- The disclosure describes a feature of an existing public product with minor
  tuning

**Green flags (✓):**
- A new **mechanism** — a new way of doing the thing, not a new application
- A new **combination** that produces an unexpected result (not just
  additive — "faster," "smaller," "cheaper" are sometimes unexpected, sometimes
  obvious)
- Solving a problem the field **had not solved** — the disclosure explains why
  the prior approaches failed and how this one doesn't

**Flagged (🟡):** anything ambiguous. Prior-art search settles it.

#### Screen 2: Obviousness flags

Would a person of ordinary skill in the art (POSA) have arrived at this
combination based on what's known? This is a screen, not a § 103 analysis —
flag for further investigation, never conclude obviousness or non-obviousness.

**Red flags (🔴) for further investigation:**
- Combining **known elements in a predictable way** — putting a known sensor
  on a known machine to measure a known thing
- **Routine optimization** — "we tuned the existing parameter from X to Y and
  got better results"
- **Design choice without functional advantage** — aesthetic, ergonomic, or
  stylistic changes that don't change how the thing works
- **Obvious to try** — one of a small number of identified solutions with a
  reasonable expectation of success

**Green flags (✓):**
- Teaching away — prior art expected the opposite result or said this approach
  wouldn't work
- Unexpected result — the combination produces something the POSA would not
  have predicted
- Long-felt need — the problem was known, and attempts to solve it had failed

#### Screen 3: Subject-matter eligibility (§ 101)

Is this an abstract idea, law of nature, or natural phenomenon? This is the
hardest screen, the most litigated, and the one most likely to require a
specialist read. Flag anything borderline for specialist review.

**Red flags (🔴) for § 101:**
- Pure **business method** without technical implementation — "a method of
  pricing widgets more efficiently"
- **Mathematical algorithm** on its own — even as dressed up in pseudocode
- **Organizing human activity** — scheduling, pairing, matching, reviewing —
  without a technical improvement
- Claim that reads as "**do [known thing] on a computer**" with no
  improvement to the computer itself
- AI/ML invention where the claim is the **function** (recommend, classify,
  predict) without the specific technical means that improves how the computer
  performs the function

**Green flags (✓) for software/AI inventions:**
- Technical improvement to the **computer itself** — new architecture, new
  training technique, new hardware/software interface, new security mechanism
- Specific technical means, not just results
- Improvement to a **technical field** (image processing, compression,
  cryptography, robotics) with the technical means described

**Anything borderline gets a 🟡 with "§ 101 — route to specialist for
Alice/Mayo analysis."** A non-specialist should not call a close § 101
question.

For **biotech / diagnostic** inventions, also flag for § 101 if the claim
recites:
- A natural correlation ("if level of X is above Y, patient has Z")
- A naturally occurring substance (isolated gene, natural product) without
  significant human modification

> **§101 is a US standard. Other patent offices are different.** The EPO's "technical effect" test (Art. 52 EPC) is materially more permissive for software and AI inventions than US §101 post-*Alice*. JPO and CNIPA also apply different standards. An invention that screens 🔴 under *Alice* may be perfectly eligible at EPO/JPO/CNIPA.
>
> When the practice profile includes non-US jurisdictions: "This §101 screen is US-only. If you file internationally, the eligibility posture may be different — particularly for software, AI/ML, and business methods, which EPO is more permissive on. Don't decline based on US §101 alone if you have EP/JP/CN filing plans."

#### Screen 4: Public disclosure / bar dates

Has the invention been disclosed, sold, offered for sale, or publicly used?
This is the most time-sensitive screen — the answer can kill patentability
absolutely, or start a clock that cannot be stopped.

Categorize the disclosure status:

**🔴 Likely barred:**
- Publicly disclosed, sold, or offered for sale **more than 12 months ago**
  in the US — 35 U.S.C. § 102(b) one-year grace period has run
- **Any** public disclosure, anywhere, before filing — absolute novelty bar in
  the EU, China, Japan, and most countries outside the US. If the business
  cares about foreign rights, this is potentially fatal even if US is still
  open.

**🟡 Clock is running:**
- Publicly disclosed within the last 12 months — US one-year clock is running,
  foreign rights may already be lost. Urgent. Confirm the disclosure date and
  route to filing immediately.

**✓ Clear:**
- No public disclosure. Confidential customer demonstrations under NDA, internal
  use, beta releases to named parties under NDA, draft papers not yet submitted
  — usually not "public" for § 102 purposes, but depends on the facts. When the
  disclosure was to a customer or external party, even under NDA, flag the
  specifics for the prosecution team to assess.

**Ask specifically about:**
- Papers submitted to journals or conferences (submission ≠ publication; but
  check the journal's policy and whether preprints were posted)
- Talks given at conferences, meetups, internal company events open to
  non-employees
- Posts to public repos, blogs, social media, or forums
- Product releases, even in limited beta
- Sales activity including quotes, RFP responses, and offers for sale
- Disclosures to investors or board members who are not under NDA

The **on-sale bar** catches offers for sale of a product embodying the
invention, not just completed sales. An RFP response describing the invention
can trigger it.

#### Screen 5: Detectability

If a competitor were to infringe this invention, could you tell? An invention
that's practiced in secret — server-side processing, back-office operations,
internal manufacturing techniques — may be better protected as a **trade
secret** than as a patent. Publishing a patent on an undetectable invention is
giving it to competitors in exchange for an asset you can never enforce.

**🔴 Low detectability flags:**
- Server-side algorithm with no observable output pattern
- Internal manufacturing process (e.g., a novel etch step in a semiconductor
  process)
- Data-pipeline or analytics methodology that happens inside a competitor's
  infrastructure
- Training data composition or training technique for an ML model — visible
  only through fine-grained probing, if at all

For these, flag for the **patent-vs-trade-secret decision**. The question is
not "is this patentable" but "should we patent it if we could." Route to
whoever in the practice profile owns trade-secret classification decisions.

**✓ High detectability:**
- Consumer product — visible in the product
- Published API, SDK, protocol — visible in network traffic or integration
  docs
- Physical mechanism in a distributed product — reverse-engineerable
- Compiled code with distinctive signatures in a distributed binary

#### Screen 6: Strategic value

Does this align with the company's patent strategy from the practice profile?
This is where the screen becomes company-specific rather than doctrinal.

Check against the profile:

- **Offensive strategy (build to assert):** is this asset assert-worthy? A
  narrow, easily designed-around patent has lower offensive value than a broad
  mechanism claim. Is the competitive landscape one where you would want to
  sue?
- **Defensive strategy (build to protect FTO):** does this cover a technology
  area where competitors are filing? A defensive filing in an area nobody
  files in is a wasted spend.
- **Licensing / revenue strategy:** is this licensable? Who would pay for it,
  and under what circumstances?

Also check:

- Is this **core** technology (part of the product's differentiation) or
  **peripheral** (incidental to a side feature)? Core is worth more.
- What is the **competitive landscape**? Patent-heavy (semiconductors,
  pharmaceuticals) — file early or lose the race. Patent-light (many
  open-source-heavy software segments) — sometimes skip entirely and spend
  the money elsewhere.
- Is the technology area on the company's list of **tech areas of interest**
  from the practice profile? If not, it is often a decline regardless of
  doctrine.

### Step 3: Assemble the invention screen memo

Format:

> **Invention screen memo — [invention title]**
>
> **Bottom line: [PURSUE / INVESTIGATE / DECLINE]**
>
> *[One sentence — the reason in plain language.]*
>
> ---
>
> ### Screen results
>
> | Screen | Verdict | Notes |
> |---|---|---|
> | Novelty signals | [✓ / 🟡 / 🔴] | [one-line reasoning] |
> | Obviousness flags | [✓ / 🟡 / 🔴] | [one-line reasoning] |
> | § 101 eligibility | [✓ / 🟡 / 🔴] | [one-line reasoning] |
> | Public disclosure / bar dates | [✓ / 🟡 / 🔴] | [one-line reasoning + dates] |
> | Detectability | [✓ / 🟡 / 🔴] | [one-line reasoning] |
> | Strategic value | [✓ / 🟡 / 🔴] | [one-line reasoning, referenced to profile] |
>
> ---
>
> ### Open questions
>
> *Things that would change the answer. The inventor, the prosecution team, or
> a specialist would need to address these before this screen converts to a
> filing decision.*
>
> - [question]
> - [question]
>
> ### Next steps (decision tree)
>
> Pick one and I'll help you build it out:
>
> 1. **Commission the prior-art search** — I'll draft the search request for
>    [outside counsel / search vendor] with the claim concepts, inventors,
>    technology classification, and any known references.
> 2. **Go back to the inventor for more facts** — I'll draft the follow-up
>    questions on [specific open items above].
> 3. **Route to outside counsel for § 101 / patent-vs-trade-secret judgment** —
>    I'll draft a transmittal summarizing what the screen found and what
>    specialist judgment is needed.
> 4. **Decline and send the standard thank-you** — I'll draft the inventor
>    thank-you and archive the disclosure with the declination reason.
> 5. **Flag for trade secret instead** — I'll draft a note to whoever owns
>    trade-secret classification explaining why a trade-secret approach is a
>    better fit.

Apply the work-product header per role. Apply the reviewer note. Keep the
deliverable clean of internal narration ("I'm using the invention-intake
skill..." etc.).

### Step 4: Recommend the bottom-line verdict

The bottom line is one of three:

- **PURSUE** — enough screens are clear (or clearly fixable) to warrant a
  prior-art search and attorney review. This is NOT "patentable" — it is
  "passes the initial screen, investigation warranted."
- **INVESTIGATE** — one or more screens flagged something that needs more
  information, specialist review, or a clarifying question back to the
  inventor before a pursue/decline decision can be made. Name the specific
  open item.
- **DECLINE** — a screen hit a fatal flag (barred by disclosure over 12
  months old with no foreign rights concern, plainly obvious, plainly abstract
  under Alice, outside the company's technology areas of interest, fundamentally
  undetectable with no trade-secret path). State the reason clearly.

A DECLINE should always be backed by a concrete reason the inventor can
understand. "Not patentable" is not an acceptable decline reason; "barred by
your paper at NeurIPS 2023 — the US one-year bar ran in December 2024" is.

## Guardrails

**Never say "patentable."** The closest you can come is "passes the initial
screen, warrants further investigation." Patentability is a conclusion a
registered practitioner reaches after a prior-art search and claim
construction.

**Never do a prior-art search in this skill.** A WebSearch for "does this
already exist" is not a prior-art search — it's a credibility check the
user can also run. If you want to sanity-check novelty, say so explicitly
("quick web check — the technique was discussed in [X] — this is not a prior-
art search, it's context for the screen") and flag it as `[web — verify]`.

**Defer on § 101 calls.** For anything borderline under Alice/Mayo, flag for
specialist review. § 101 is where practitioners routinely disagree and where
a non-specialist's confident call ages badly.

**Flag detectability before strategic value.** An undetectable invention that
would be "high strategic value" as a patent is usually higher strategic value
as a trade secret. Do not recommend PURSUE on an undetectable invention
without addressing the trade-secret alternative.

**Urgent cases get urgent flagging.** If the screen hits a within-one-year
public disclosure in the US, or any public disclosure with foreign rights in
scope, say so at the top of the memo. Bottom line, then: "**Time-sensitive —
US bar runs [date], foreign rights already at risk.**" This is the kind of
finding a lawyer needs to see in the first three seconds.

**Respect the routing.** Per the practice profile, this screen is a triage
step. The person who decides what to file is the attorney or agent responsible
for patent prosecution. The screen feeds that person; it does not replace them.

## Non-lawyer gate

If the role is **non-lawyer** (with or without attorney access), close the
memo with:

> **This is a screening tool for your disclosure, not a patentability opinion.
> The decision about whether to file — and how — belongs to a registered
> patent attorney or agent. If this screen says PURSUE or INVESTIGATE, your
> next step is not to file or draft claims; it is to share this memo (and the
> underlying disclosure) with patent counsel. If there is no counsel engaged
> yet, [contact from profile / "your professional regulator's IP referral service — state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent"] is the
> starting point.**

---

## /ip-legal:ip-clause-review

---
name: ip-clause-review
description: >
  Review the IP clauses in an agreement — assignment, ownership, license
  grants, warranties, indemnities. Use when reviewing IP terms in employment,
  consulting, SOW, vendor, or licensing agreements, when asked to check the
  assignment language or license scope, or when an agreement with IP
  provisions is pasted or attached.
argument-hint: "[file path | Drive link | paste text]"
---

# /ip-clause-review

Reviews the IP clauses in an agreement against the practice profile in `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Flags assignment gaps, ownership ambiguity, license-scope issues, and IP warranty/indemnity problems. Produces a memo with per-clause findings, prioritized by risk, with suggested redline language where appropriate.

## Instructions

1. **Load `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`.** If placeholders present, stop and prompt: "Run `/ip-legal:cold-start-interview` first — I need to learn your practice profile before I can review IP clauses against it."

2. **Get the agreement:** From file path, Drive link, or pasted text. If none provided, ask.

3. **Follow the workflow below.** In particular:
   - Establish the agreement type and which side the company is on for IP (granting / receiving / both). The side question is per-document, not a one-time setup answer.
   - Run the assignment gap check first if the agreement is an employment, consulting, SOW, or work-for-hire document.
   - Produce per-clause findings prioritized by risk.
   - Check cross-clause consistency, not just clause-by-clause.
   - Note jurisdiction implications (moral rights, work-for-hire, implied license, patent indemnity).

4. **Output the memo** per the template below — work-product header first, bottom line, assignment gap check, clauses by severity, consistency flags, jurisdiction note, approval routing.

5. **Respect the decision posture.** When a clause could be read to allocate IP either way, flag for attorney review and surface the factors cutting both ways. Never silently decide a subjective allocation question.

## Examples

```
/ip-legal:ip-clause-review ~/Documents/vendor-sow.pdf
/ip-legal:ip-clause-review https://docs.google.com/document/d/...
/ip-legal:ip-clause-review
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Read the IP clauses in an agreement and tell the lawyer what each one does, how it deviates from market or from the team's standard position, what the risk is, and — where appropriate — the specific redline to propose. The goal is a memo the lawyer can act on in one pass.

**The highest-stakes clauses in most agreements are IP ownership and assignment.** They are hard to fix later. A failure to get a clean assignment on an employment or consulting agreement surfaces in M&A diligence, in financing, and in litigation, sometimes years after the agreement was signed. If assignment language is weak or missing in a document that should have it, flag it loudly at the top of the memo — not buried as one line item among many.

## Precondition: load the practice profile

**Before reading the agreement, read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`.** If it is missing or still contains placeholders, stop and run `/ip-legal:cold-start-interview`. The practice profile tells you:

- The jurisdiction footprint — which affects whether moral rights waivers are enforceable, whether work-for-hire applies, whether implied assignment fills a gap, how broad license grants can be
- Who approves deviations and at what severity
- The work-product header to prepend to outputs

## Workflow

### Step 1: Orient

Read the whole agreement once, fast. Answer:

| Question | Answer |
|---|---|
| What kind of agreement is this? | Employment / consulting or SOW / vendor MSA / in-license / out-license / collaboration or JDA / settlement / acquisition or asset purchase / other |
| Which side are we on for IP? | Granting rights or receiving them / assigning IP or acquiring it / licensor or licensee |
| Who is the counterparty? | Name, and sophistication — individual, startup, BigCo |
| Is there consideration flowing for the IP specifically? | Salary, fee, royalty, upfront payment, equity, none |
| Governing law and venue | What does it say — and does our practice profile flag that jurisdiction as escalate/never? |

The side question is per-document, not a one-time setup answer. An in-house counsel reviewing an employment agreement is on the "receiving" side; reviewing an out-license the same day, on the "granting" side. The posture inverts.

If the side is ambiguous (a collaboration agreement where both parties contribute and both receive rights, a reseller agreement with flow-through IP), ask:

> Which side is [company] on for this agreement's IP? Granting rights, receiving rights, or both? If both, I'll review each direction separately.

### Step 2: Assignment gap check (highest priority)

If the agreement is an employment agreement, consulting agreement, SOW, work-for-hire contract, or anything else where the company should be receiving an assignment of the counterparty's IP in work product — check the assignment language first.

Look for:

- **Present-tense assignment** ("hereby assigns" or "hereby irrevocably assigns and agrees to assign"). A bare "agrees to assign" is a promise to assign, not an assignment, and can require a second document to perfect.
- **Scope** — does it cover all IP created in the course of engagement, or only IP related to the company's business, or only IP created using company resources? Narrow scope is a gap if work product is expected to range broadly.
- **Moral rights waiver** (for jurisdictions that recognize moral rights — EU member states, Canada, many others — the US recognizes a narrow version for visual art). If the agreement is governed by or has counterparties in a moral-rights jurisdiction, a waiver or non-assertion covenant matters.
- **Further assurances** clause — counterparty agrees to sign whatever else is needed to perfect the assignment later.
- **Pre-existing IP carveout** — what does the counterparty exclude from the assignment, and is that list specific or open-ended?

If any of the above is missing or weak, flag at the top of the memo with a 🔴 or 🟠 severity and a specific redline.

```markdown
## ⚠️ ASSIGNMENT GAP

**Section [X]** assigns IP in the work product, but: [specific issue — e.g.,
"'agrees to assign' rather than 'hereby assigns,'" or "no moral rights waiver
and governing law is France," or "no carveout list is provided and the
counterparty has pre-existing platform IP"].

**Risk:** This is the kind of gap that surfaces in M&A diligence years later.
The counterparty (or a successor) may have residual rights in work product we
thought we owned.

**Proposed redline:**
> "[specific replacement language]"

**Escalation:** Per `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`, assignment-scope gaps escalate to [approver].
```

> **Can the assignment convey AI-generated content?** *Thaler v. Perlmutter* and the Copyright Office's 2023 AI registration guidance suggest that AI-generated works without any human authorship may not be copyrightable, though the boundaries remain unclear and this area is evolving. If the contractor uses AI for substantial portions of the deliverables, the copyright status of those portions is uncertain — and an assignment clause can only convey rights that exist.
>
> Check: does the agreement have an AI-use disclosure obligation? A representation about the role of AI in the deliverables? A mechanism to identify which portions are AI-assisted vs. human-authored?
>
> If absent and AI-assisted creation is foreseeable (consulting, development, content creation, design): 🟠 High. "The assignment clause is well-drafted but there's no AI-use disclosure. The copyright status of AI-generated content is unsettled, and without a disclosure obligation you won't know which portions are affected. Add an AI-use representation and a disclosure obligation." `[review — copyright status of AI-generated works is an evolving area; verify against current Copyright Office guidance and case law]`

> **AI-assisted inventorship.** A patent filed with incorrect inventorship is unenforceable. If a consultant uses AI tools that contribute to an inventive concept, the inventorship question is unsettled and the patent is at risk. For any agreement with patent assignment provisions covering potentially patentable work product:
>
> Check: does the agreement have an AI-use representation? A process for determining inventorship where AI contributed? A disclosure obligation about AI use in the inventive process?
>
> If absent: flag. "Patent assignment without an AI-use representation. If AI tools contributed to the inventive concept, inventorship determination is complicated and an incorrectly-attributed patent is unenforceable. Add an AI-use representation and inventorship protocol."

### Step 3: Clause-by-clause review

For every IP-relevant clause, produce a block. The clauses to look for:

- **Assignment / work-for-hire** — who owns what's created under the agreement
- **Ownership of deliverables** — distinct from assignment; often states the output of the engagement
- **Improvements and derivatives** — who owns improvements to pre-existing IP, who owns derivative works
- **Background IP vs. foreground IP** — does the agreement define pre-existing IP and newly-created IP separately, and license the background IP to the extent needed?
- **License grants** — scope, exclusivity, territory, field of use, sublicensability, term, termination triggers, royalty or fee structure
- **IP warranties** — non-infringement of third-party rights, authority to grant, original work
- **IP indemnities** — scope, cap, procedure, exclusions (user modifications, combinations, unauthorized use)
- **Moral rights waiver** — jurisdiction-dependent
- **Open source representations** — representations about what OSS is and is not embedded in deliverables
- **Trademark use** — any grant or restriction on use of the other party's marks; brand guidelines; quality control for licensor
- **Confidentiality / trade secrets** — treatment of trade secret material, reasonable measures, return or destruction, post-term obligations

For each clause present, produce:

```markdown
### [Section X.X]: [Clause name]

**What it says:** [plain-English summary, one or two sentences]

**What's market (for this agreement type, this side, this jurisdiction):**
[brief reference point]

**Risk:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

**Why it matters:** [one or two sentences — what goes wrong for the business
if this stays as-is]

**Proposed redline (if needed):**
> "[specific replacement language]"

**Decision call:** [If uncertain whether the clause achieves the intended IP
allocation, flag for attorney review and state the factors cutting both
ways. Do not silently decide a subjective allocation question.]
```

**Severity calibration:**

| Level | Means |
|---|---|
| 🔴 Critical | Don't sign without fixing. Assignment gap in a document that should have one. Unlimited license where a narrow one was intended. Exclusive grant where non-exclusive was intended. |
| 🟠 High | Strongly push; escalate if they won't move. Ambiguous scope, missing moral rights waiver in a moral rights jurisdiction, missing further assurances, narrow indemnity. |
| 🟡 Medium | Push in first round; accept if it's the last open item. Cosmetic but imprecise language, survival periods shorter than standard. |
| 🟢 Low | Note it, don't spend capital. A stylistic deviation that doesn't change the allocation. |

### Step 4: Cross-clause consistency

IP clauses fail as a system. Check:

- **Does the license grant match the scope of what's being licensed?** (A license to "use" the deliverable is narrower than a license to "use, modify, and create derivative works.")
- **Do the warranties cover everything the grant covers?** (A warranty of non-infringement limited to patents, in a license that also covers copyrights and trade secrets, leaves gaps.)
- **Does the indemnity cover what the warranty promises?** (A warranty without indemnity is a promise without a remedy.)
- **Does termination pull the license back?** (Or does a paid-up license survive termination? Either is defensible — the question is whether it matches intent.)
- **Is the IP allocation between this agreement and any related SOW, order form, or related side letter consistent?** Flag conflicts.

### Step 5: Jurisdiction note

IP rules are jurisdiction-specific in ways that change the outcome. Flag if the agreement implicates any of these:

- **Moral rights** — EU member states, Canada, much of the civil-law world recognize moral rights (paternity, integrity) that may not be fully assignable or waivable. US recognition is narrow (VARA, for visual art).
- **Work-for-hire** — US doctrine is statutory (17 U.S.C. § 101) and only applies to enumerated categories for independent contractors. UK implies assignment in the employment context but not always for contractors. Civil-law jurisdictions handle this differently again.
- **Implied license** — common-law jurisdictions may read in an implied license where the written grant is silent. Civil-law jurisdictions tend not to.
- **Patent indemnity exclusions** — combinations, modifications, and user supply of accused features are standard US exclusions; the interaction with EU patent and UPC is still developing.

State what jurisdiction the agreement is governed by, and whether the practice profile flags that jurisdiction as standard, escalate, or never.

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

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`).

This memo and the underlying agreement may be privileged, confidential, or both. The output inherits that status from the source. Distribute only within the privilege circle; mark and store it where privileged materials live; strip the work-product header before any external delivery.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a rule the memo needs (enforceability of a moral rights waiver in a given jurisdiction, scope of an implied license, standard for an IP warranty survival period), report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule / jurisdiction]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Where the memo cites a statute, regulation, case, or treatise, tag the citation: `[Westlaw]`, `[statute / regulator site]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations from the counterparty draft or house files. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# IP Clause Review: [Counterparty] [Agreement Type]

**Reviewed:** [date]
**Our side for IP:** [Granting / Receiving / Both]
**Governing law:** [jurisdiction]

---

## Bottom line

[Two sentences. Can the IP allocation stand? What has to change first?]

**Issues:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Approval needed from:** [name, per practice profile]

---

## Assignment gap check

[✅ Clear | ⚠️ Gap present — see above]

---

## Clauses by severity

[All clause blocks from Step 3, grouped Critical → Low]

---

## Cross-clause consistency

[Flags from Step 4]

---

## Jurisdiction note

[Flags from Step 5]

---

## Approval routing

[From practice profile — who approves, what triggers automatic escalation]
```

## Decision posture

When a clause could be read to allocate IP either way, or when it is unclear whether the drafter's chosen words achieve the stated intent, **flag it for attorney review and surface the factors cutting both ways**. Do not silently decide a subjective allocation question. An unresolved IP allocation that gets signed is a one-way door — the error surfaces in diligence, financing, or litigation. Flagging an ambiguous clause that turns out to be fine is a two-way door.

## Quality checks before delivering

- [ ] Practice profile was loaded and the jurisdiction note reflects what's there
- [ ] Assignment gap checked first (for employment/consulting/SOW/WFH)
- [ ] Every 🔴 and 🟠 issue has specific replacement language
- [ ] Cross-clause consistency checked, not just clause-by-clause
- [ ] Source tags applied to citations; no stripped `verify` tags
- [ ] Approver named per practice profile, not "escalate to legal"
- [ ] Output marked with the work-product header

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

---

## /ip-legal:matter-workspace

---
name: matter-workspace
description: >
  Manage matter workspaces — create, list, switch, close, or detach the
  active matter. Use in multi-client private practice to keep one client's
  context separate from another, or when a substantive skill needs to know
  which matter it's working in.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Practitioners work across multiple clients and matters. A matter workspace keeps one client or engagement's context separate from every other. This skill manages those workspaces.

## Subcommands

- `/ip-legal:matter-workspace new <slug>` — create a new matter workspace, run a short intake, write `matter.md`
- `/ip-legal:matter-workspace list` — list matters with status and active flag
- `/ip-legal:matter-workspace switch <slug>` — set the active matter
- `/ip-legal:matter-workspace close <slug>` — archive a matter (move to `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/_archived/`, never delete)
- `/ip-legal:matter-workspace none` — detach from any active matter, work at practice-level only

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` — confirm the `## Matter workspaces` section is populated. If `Enabled` is `✗`, tell the user: "Matter workspaces are off — you're configured as an in-house practice with one client, so the plugin works from practice-level context automatically. If you actually work across multiple clients, re-run `/ip-legal:cold-start-interview --redo` and select a private-practice setting. Otherwise, you don't need `/ip-legal:matter-workspace` at all." Don't error — the disabled state is the expected one for in-house users.
2. Follow the subcommand logic below.
3. Dispatch on the first token of `$ARGUMENTS`:
   - `new` → run the intake interview, write `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<slug>/matter.md`, seed `history.md` and `notes.md`.
   - `list` → enumerate `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/*/matter.md`, print a table, mark the active matter.
   - `switch` → update the `Active matter:` line in the practice-level CLAUDE.md.
   - `close` → move `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<slug>/` to `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/_archived/<slug>/`, log the close date in `history.md`.
   - `none` → set `Active matter:` to `none — practice-level context only`.
4. Show the user what changed and confirm before writing.

## Notes

- The skill never reads across matters unless `Cross-matter context` is `on` in the practice-level CLAUDE.md.
- Archiving is not deletion — closed matters remain readable for retention/conflicts purposes.
- Slugs are lowercase with hyphens. If a slug is reused across archived and active, the archived one is preserved under `_archived/<slug>/`.

---

Multi-client practitioners (private practice — solo, small firm, large firm) work across many matters. Context from one must not leak into another. This skill is the thin file-management layer that makes that true.

**Default state is off.** In-house users never see this — they run at practice-level only. Matter workspaces turn on at cold-start for private-practice users, or by editing `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗`, this skill does not run; instead it explains the disabled state and suggests `/ip-legal:cold-start-interview --redo` for users who actually need matter isolation.

## Storage layout

All matter data lives under:

```
~/.claude/plugins/config/claude-for-legal/ip-legal/
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

Slugs are lowercase with hyphens. Examples: `acme-trademark-2026`, `zenith-dmca`, `novacorp-fto`.

## Active matter is in the practice CLAUDE.md

The `Active matter:` line under `## Matter workspaces` in the practice-level CLAUDE.md is the single source of truth. Switching a matter edits that line. No separate state file.

## Subcommand logic

### `new <slug>`

1. Confirm slug is not already present in `matters/<slug>/` or `matters/_archived/<slug>/`. If reused, ask the user to pick a different slug.
2. Run the intake interview:
   - **Client** (the party we represent, or the internal business unit if in-house)
   - **Counterparty** (the other side — may be multiple; may be "unknown third-party infringer" for watch-triggered matters)
   - **Matter type** (read the plugin's practice profile for typical categories; for ip-legal: trademark clearance | trademark enforcement | DMCA | patent FTO | patent infringement | IP clause review | OSS compliance | portfolio maintenance | other)
   - **Confidentiality level** (standard | heightened | clean-team — heightened prompts extra care in cross-matter settings; clean-team common in patent FTO work)
   - **Key facts** (2–5 sentences: what this matter is about, who the stakeholders are, what's at stake)
   - **Matter-specific overrides to the practice posture** (e.g., "client wants aggressive posture for this mark only", "counterparty is a strategic partner — measured tone only", "inventor unavailable — don't surface for interview")
   - **Related matters** (slugs of any connected matters)
3. Write `matters/<slug>/matter.md` using the template below.
4. Seed `matters/<slug>/history.md` with a single "Opened" entry.
5. Create an empty `matters/<slug>/notes.md`.
6. Do **not** auto-switch to the new matter. Ask: "Want to switch to `<slug>` now? (`/ip-legal:matter-workspace switch <slug>`)"

### `list`

Enumerate `matters/*/matter.md`. Read each file's front-matter or first few lines to extract status. Print a table:

| Slug | Client | Matter type | Status | Opened | Active |
|---|---|---|---|---|---|

Mark the currently-active matter with `*`. Include `_archived/*` under a separate "Archived" heading if any exist.

### `switch <slug>`

1. Confirm `matters/<slug>/matter.md` exists. If not, offer `/ip-legal:matter-workspace new <slug>`.
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

[trademark clearance | trademark enforcement | DMCA | patent FTO | patent infringement | IP clause review | OSS compliance | portfolio maintenance | other — with one-line rationale]

## Key facts

[2–5 sentences. What this matter is about. Who the stakeholders are. What's at stake. What makes it different from the default posture.]

## Matter-specific overrides

*Any deviation from the practice-level posture that applies to this matter and only this matter.*

- [e.g., "Enforcement posture: measured here even though house default is aggressive — counterparty is a key channel partner."]
- [e.g., "Approval for assertion: extra sign-off from marketing required before any letter goes out."]
- [e.g., "Clean-team: matter files not readable even with cross-matter context on."]

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
[Any initial context worth preserving beyond matter.md — e.g., "Opened in response to watch-service hit on `APEXLEAF` in class 25."]
```

## Cross-matter context

The practice-level CLAUDE.md has a `Cross-matter context:` flag. When it's `off` (the default), a skill working in matter A **never reads** files in `matters/B/` for any other `B`. Period. This is the confidentiality guarantee the setting exists to provide.

When it's `on`, a skill may read files across matter folders only when the user explicitly asks it to (e.g., "show me every enforcement letter we've sent on this mark across matters"). Even when `on`, the default is to load only the active matter unless the user asks for a cross-matter view.

## What this skill does not do

- **Run a conflicts check.** Conflicts are the practitioner's/firm's job; the intake captures what the user declares.
- **Enforce retention.** Closing archives a matter; it does not delete. Retention policy is out of scope.
- **Auto-route outputs.** The substantive skill decides where to write; this skill tells it *which folder* is active, not what to put in it.
- **Decide whether cross-matter is appropriate.** It reads the flag and obeys.

---

## /ip-legal:oss-review

---
name: oss-review
description: >
  Open source license compliance check for a dependency list, a single
  library, or outbound code. Use when reviewing a manifest, SBOM, or repo for
  copyleft obligations and license compatibility, when asked whether a library
  can ship, or when preparing code to be open-sourced.
argument-hint: "[file path to manifest / SBOM | package name | repo path | paste text]"
---

# /oss-review

Runs an open source license compliance check against the practice profile in `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Classifies dependencies by license family, maps obligations to the deployment model, flags license-unknown and non-OSI-posing-as-OSS packages, and recommends actions — comply, replace, remove, seek legal review, seek commercial license.

## Instructions

1. **Load `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`.** If placeholders present, stop and prompt: "Run `/ip-legal:cold-start-interview` first — I need to learn your practice profile (and OSS policy, if any) before I can review." If the practice profile points at an uploaded OSS policy, read that too — it is the source of truth for accepted / review / banned licenses on this team.

2. **Establish the scope:** a dependency list (package.json, requirements.txt, go.mod, Gemfile, Cargo.toml, pom.xml, SBOM), a single library, or outbound code the team is preparing to open-source. If the user passed a path, infer from the file; otherwise ask.

3. **Establish the deployment model** before classifying obligations — SaaS, distributed binary, internal only, or embedded. The same dependency list triggers different obligations depending on this.

4. **Follow the workflow below.** In particular:
   - Read the actual license text, not just metadata — LICENSE files can be wrong, package metadata can be stale.
   - Classify each package into permissive / weak copyleft / strong copyleft / public domain / non-OSI / unknown.
   - Flag license-unknown as "needs review," not permissive by default.
   - Flag non-OSI source-available licenses (SSPL, BUSL, Commons Clause, Elastic License, fair-source) — these are not open source.
   - For outbound code, check that the chosen outbound license is compatible with every embedded dependency.

5. **Output the memo** per the template below — work-product header first, bottom line, top-of-memo flags, per-package blocks grouped by severity, jurisdiction note, outbound check (if applicable), approval routing.

6. **Respect the decision posture.** When a copyleft-trigger analysis turns on a contested question (AGPL's "interacts over a network," GPL-3.0's "conveying," LGPL linking scope), flag for attorney review and surface the factors cutting both ways. Anything flagged as strong copyleft or license-unknown goes to an attorney before the dependency ships or the code is released.

## Examples

```
/ip-legal:oss-review ~/code/my-project/package.json
/ip-legal:oss-review ~/code/my-project/requirements.txt
/ip-legal:oss-review redis
/ip-legal:oss-review ~/code/my-project  # repo root — scan all manifests
```

---

## Works better connected

OSS clearance requests usually come in via a ticketing system. Connected to
Jira, Linear, or Asana, this skill can: monitor incoming OSS requests, respond
with guidance directly in the ticket (flagging incomplete info, asking for the
repo link, returning the license-family classification), and track clearance
status across requests.

Without a connector, paste the ticket or describe the request and I'll handle
it one at a time. See `CONNECTORS.md` at the repo root for how to add a
ticketing connector.

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Tell the user what licenses are in their dependency tree, what obligations those licenses trigger given how the code will be deployed, and what to do about each one. The output is a memo the lawyer (or the engineer with attorney access) can act on — comply, replace, remove, seek legal review, seek commercial license.

**This is a first-pass classification.** Copyleft analysis depends on the deployment model, the degree of linking, the jurisdiction, and sometimes on legal questions that have not been tested in court (notably AGPL's "interacts over a network," GPL-3.0's patent clause). For anything that classifies as strong copyleft or license-unknown, an attorney evaluates before the dependency ships or the code is released. The skill reports what it found; the lawyer decides what to do.

## Precondition: load the practice profile

**Before scanning dependencies, read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`.** If it is missing or still contains placeholders, stop and run `/ip-legal:cold-start-interview`. The practice profile tells you:

- Who owns OSS review on this team (often engineering with legal sign-off)
- Escalation routing for copyleft obligations
- The work-product header to prepend

If the practice profile has an OSS policy uploaded, read that too — it is the source of truth for which licenses the team accepts, which trigger review, and which are banned.

## Workflow

### Step 1: What's the scope?

Ask (or infer from what the user provided):

> What are we reviewing?
>
> 1. **A dependency list** — `package.json`, `requirements.txt`, `go.mod`, `Gemfile`, `Cargo.toml`, `pom.xml`, an SBOM (SPDX / CycloneDX), a lockfile
> 2. **A single library** — one specific package you're considering adding
> 3. **Our own code** — we're planning to open-source this and need to check what's embedded

The analysis path differs:

- Dependency list → classify every entry, roll up obligations
- Single library → classify one package and walk its transitive dependencies if available
- Outbound code → check what's embedded (direct and transitive), check whether chosen outbound license is compatible with all embedded licenses, check that LICENSE / NOTICE files are correct

### Step 2: What's the deployment model?

This is the single most important input after the license list — the same library carries different obligations depending on how the software is delivered. Ask:

> How will this be deployed?
>
> 1. **SaaS / hosted service** — users access over a network; nothing ships to the user
> 2. **Distributed binary** — we ship compiled code to users (desktop app, mobile app, on-prem server, CLI tool)
> 3. **Internal only** — used only inside the company, not distributed outside
> 4. **Embedded / firmware** — shipped in hardware or as closed-system firmware

| Deployment | Licenses that materially matter |
|---|---|
| SaaS | AGPL (network-trigger), permissive attribution in any UI, SSPL/BUSL/Elastic if repurposing as competing service |
| Distributed binary | GPL, LGPL, MPL, EPL (all trigger on distribution), permissive attribution |
| Internal only | Most copyleft does not trigger — no distribution. Permissive attribution still good hygiene. AGPL still triggers if users outside the company interact over the network. |
| Embedded / firmware | GPL is especially hard to comply with here (source disclosure + reproducible build + installation information in some cases). Plan for this before shipping, not after. |

Flag the deployment model in the output memo — the same dependency list reviewed against "SaaS" vs. "distributed binary" yields different obligations.

### Step 3: Classify each dependency

For every package, determine the license. Read the actual license text, not just the metadata — LICENSE files can be wrong (the file says MIT but the headers say GPL; the README claims Apache but there's no license file), and package manager metadata can be stale.

Classify into:

| Bucket | Examples | Key obligations |
|---|---|---|
| **Permissive** | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Zlib, Unlicense | Attribution, preserve license text, Apache-2.0 adds patent grant + NOTICE requirement |
| **Weak copyleft** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-1.0, EPL-2.0, CDDL | File-level or library-level source disclosure; linking rules vary |
| **Strong copyleft** | GPL-2.0, GPL-3.0, AGPL-3.0, OSL, EUPL (depending on version) | Broad source disclosure; AGPL extends to network use |
| **Public domain / dedication** | CC0, Unlicense, WTFPL | Typically no obligations, but some are contested in jurisdictions that don't recognize dedication to public domain |
| **Non-OSI source-available** | SSPL, BUSL, Commons Clause, Elastic License, Confluent Community, fair-source family | Not open source — restrict commercial use, competing-service use, or both. Read the specific license. |
| **Other / custom / unknown** | vendor-specific, proprietary, missing license file, license conflict between file and headers | Stop — do not treat as permissive by default |

Flag:

- **Dual-licensed packages** — which license are we using? The choice may change obligations.
- **Deprecated packages** — the package is no longer maintained; is there a supported replacement?
- **Packages with a copyleft dependency in their own tree** — the top-level license is permissive but a transitive dependency is copyleft.
- **Packages that changed license recently** — Redis, MongoDB, Elastic, HashiCorp — make sure the version pinned is under the license you think it is.

### Step 4: Map obligations to the deployment model

For each classified dependency, state what the deployment model triggers:

```markdown
### [package@version] — [License]

**Classification:** [Permissive / Weak copyleft / Strong copyleft / Public domain / Non-OSI / Unknown]

**Obligations for our deployment ([SaaS / binary / internal / embedded]):**

- [ ] [Specific obligation — e.g., "Include attribution in a NOTICES file shipped with the app"]
- [ ] [e.g., "If we modify and distribute, publish source of our modifications"]
- [ ] [e.g., "AGPL network trigger — if users access our modified version over a network, source must be offered to them"]

**Risk:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

**Recommendation:** [Comply with obligations | Replace with [alternative] | Remove | Attorney review before shipping | Seek commercial license from [vendor]]
```

> **How is the copyleft dependency consumed?** The linking relationship determines whether copyleft actually triggers. Ask or determine:
> - **Static linking / compilation together:** The works are combined into one binary. Strong signal that copyleft triggers (LGPL "work based on the Library," GPL derivative work).
> - **Dynamic linking / shared library:** The works remain separable at runtime. LGPL explicitly permits this ("work that uses the Library"). GPL's position is contested (FSF says derivative, others disagree).
> - **Header inclusion / inline functions:** Can create a derivative work depending on how much is included.
> - **Subprocess / IPC:** Separate processes communicating over well-defined interfaces. Generally not derivative.
> - **Network API call:** For most licenses, no. For **AGPL**, the network-interaction clause means serving the software over a network IS distribution. In a microservices architecture, an AGPL component behind an API still triggers.
> - **File-scope copyleft (MPL):** Only the modified files carry copyleft, not the whole work. Check whether any copyleft files were modified.
>
> **The severity rating depends on this.** "LGPL — weak copyleft, linking rules vary" without the linking analysis is the answer that gets an engineer sued. Static-linked LGPL in a proprietary product is 🔴 Critical. Dynamic-linked LGPL is 🟢 Low. Same license, opposite rating.

**Severity calibration:**

| Level | Means |
|---|---|
| 🔴 Critical | Strong copyleft in a deployment that triggers it (e.g., GPL in a distributed binary, AGPL in a SaaS). Non-OSI license that the business model actually conflicts with (e.g., SSPL while we're building a managed service). License cannot be determined and the package is load-bearing. |
| 🟠 High | Weak copyleft with obligations the team hasn't set up for (file-level disclosure, NOTICE requirements). Dual-licensed where the chosen license is ambiguous. License file says one thing, headers say another. |
| 🟡 Medium | Permissive with attribution requirements that haven't been wired into the build (missing NOTICES file, missing LICENSE in distribution). Transitive copyleft in a position that may or may not trigger, depending on how the library is consumed. |
| 🟢 Low | Permissive with obligations already satisfied. Copyleft in a deployment model that doesn't trigger it (e.g., GPL library used internally only, with no redistribution). |

### Step 5: Flag failure modes

Call out any of the following in a top-of-memo section:

- **License unknown** — classify as "needs review," not permissive. An unclassified dependency should stop a ship decision, not slip through.
- **License file conflicts with file headers** — read both and report the conflict.
- **Incompatible combinations** — GPL-2.0 only + Apache-2.0 historically a known incompatibility; check MPL / EPL / GPL combinations carefully.
- **Non-OSI licenses posing as open source** — SSPL, BUSL, Commons Clause, Elastic License, Confluent Community. Read the license; don't rely on GitHub's "open source" badge.
- **License changes** — if a prior version was permissive and the current version is source-available, the pin matters.

### Step 6: Outbound check (if reviewing our own code before open-sourcing)

If the user is preparing to open-source code:

- Confirm the chosen outbound license is compatible with every embedded dependency's license (e.g., you cannot release under MIT if you've embedded GPL code — the combined work must be GPL)
- Confirm LICENSE file is present and correct
- Confirm NOTICE file is present and lists required attributions (Apache-2.0 and others)
- Confirm third-party license texts are bundled where required
- Confirm no proprietary or confidential code, no customer data, no embedded credentials in the repo history
- Confirm trademark and brand policy for any project name (separate from the copyright license)

### Step 7: Assemble the memo

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → `## Outputs` (differs by user role — see `## Who's using this`).

This memo and any dependency list reviewed may be privileged, confidential, or both. The output inherits that status from the source. Distribute only within the privilege circle; strip the work-product header before any external delivery (including before attaching the memo to an engineering ticket outside the privilege circle).

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a rule the memo needs (enforceability of AGPL's network trigger in a given jurisdiction, scope of GPL-3.0's patent grant, latest license text for a recently-relicensed package), report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule / license / jurisdiction]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Where the memo cites a license text, a court decision interpreting a license, or guidance from a steward (FSF, OSI, SPDX, SFLC), tag the citation: `[OSI]`, `[SPDX]`, `[FSF]`, `[SFC/SFLC]`, `[Westlaw]`, or the MCP tool name for citations retrieved from a connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for license text read directly from the repo. Citations tagged `verify` carry higher fabrication risk. Never strip or collapse the tags.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# OSS Review: [Project / Dependency List / Package]

**Reviewed:** [date]
**Scope:** [Dependency list / Single library / Outbound code]
**Deployment model:** [SaaS / Binary / Internal / Embedded]

---

## Bottom line

[Two sentences. Can this ship? What has to happen first?]

**Packages reviewed:** [N]
**By classification:** [N permissive, N weak copyleft, N strong copyleft, N public domain, N non-OSI, N unknown]
**Issues:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Approval needed from:** [name, per practice profile]

---

## Top-of-memo flags

[License-unknown list, license-conflict list, non-OSI-posing-as-OSS list, incompatible combinations]

---

## By package

[Blocks from Step 4, grouped by severity]

---

## Jurisdiction note

OSS license enforceability varies — AGPL's network trigger has not been broadly tested in court; GPL-3.0's patent clause reads differently under US vs. EU patent law; dedications to public domain are not universally recognized. State the governing-law choice for any downstream distribution (e.g., vendor agreements incorporating the code) and flag jurisdictions the practice profile marks as escalate.

---

## Outbound check (if applicable)

[From Step 6]

---

## Approval routing

[From practice profile — who approves, what triggers automatic escalation]
```

## Decision posture

When a license cannot be confidently classified, flag it as **"needs review"** — do not call it permissive. Under-classifying license risk is a one-way door: a ship decision made on a permissive-by-default assumption becomes a source-disclosure obligation or an injunction months later. Over-flagging is a two-way door — the attorney narrows the list in review.

Likewise, when the copyleft-trigger analysis turns on a contested question (AGPL's "interacts over a network," GPL-3.0's "conveying," the scope of LGPL linking), flag for attorney review and surface the factors cutting both ways.

## Quality checks before delivering

- [ ] Practice profile and any OSS policy were loaded
- [ ] Deployment model was established before classifying obligations
- [ ] Every dependency has a classification, including transitives where available
- [ ] License-unknown packages are flagged, not defaulted to permissive
- [ ] License text was read (not just metadata) for any copyleft or non-OSI finding
- [ ] Source tags applied to citations; no stripped `verify` tags
- [ ] Approver named per practice profile
- [ ] Output marked with the work-product header

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

If the scan surfaced more than ~10 packages, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer to what's useful here — counts by license family (permissive / weak copyleft / strong copyleft / AGPL / proprietary / unknown), risk distribution, and a table of findings with severity and package version.

---

## /ip-legal:portfolio

---
name: portfolio
description: >
  Track the IP portfolio — registrations, renewals, maintenance fees, and use
  declarations. Use when checking what's renewing, adding or updating an
  asset, recording a maintenance filing, or auditing the register for gaps,
  lapses, and use-in-commerce questions. Receives handoffs from prosecution
  and clearance work.
argument-hint: "[--report [--days N] | --add | --update | --audit]"
---

# /portfolio

Surfaces what's renewing, adds assets, records filings, and audits the register.

## Instructions

1. **Follow the workflow below** and read
   `~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml`.

2. **Default (no args):** equivalent to `--report` — show deadlines in the
   next 90 days grouped by urgency (🔴 lapsed/grace, ⏰ due within window,
   🟡 upcoming, 🌐 agent-managed, ❓ unknown).

3. **`--report [--days N]`:** Mode 2. Change the window with `--days`
   (30 / 60 / 90 / 180 typical). Always prepend the work-product header
   per CLAUDE.md → Outputs. Always close with the verification caveat.

4. **`--add`:** Mode 3. Walk through a new asset interactively — type,
   jurisdiction, number, dates, owner, business owner. Capture a custom
   rule if the jurisdiction isn't built in.

5. **`--update`:** Mode 4. Record that a maintenance filing or fee payment
   was made, sync with the IP management system, or change an asset's
   status. Enforce the consequential-action gate before setting any
   deadline to `filed`.

6. **`--audit`:** Mode 5. Broader health check — deadline hygiene,
   registration gaps, use-in-commerce questions on §8-approaching marks,
   owner inconsistencies, expiration horizon, unwatched marks.

7. **If the register is empty and an IP management system is connected:**
   Offer Mode 1 — pull the portfolio from the system of record and
   initialise the register.

8. **Guardrail reminder:** Computed deadlines are reference only. Every
   output closes with a line directing verification against the USPTO
   TSDR, WIPO, or relevant registry before filing or paying. A
   docketed-but-wrong deadline creates false confidence; do not let the
   user treat this as the system of record unless the IP management
   system is sync-integrated.

## Examples

```
/ip-legal:portfolio
```

```
/ip-legal:portfolio --report --days 180
```

```
/ip-legal:portfolio --add
```

```
/ip-legal:portfolio --update
```

```
/ip-legal:portfolio --audit
```

---

## Works better connected

This skill tracks deadlines from what you tell it. It works much better
connected to:

- **An IP management system (IPMS) via MCP** — Anaqua, Clarivate IPfolio,
  AppColl, Patrix, Alt Legal, FoundationIP. A connected IPMS gives you the
  full docket, maintenance fee schedules, and incoming correspondence in one
  place, instead of the register being whatever the lawyer remembers to
  paste. Ask your IPMS vendor if they have an MCP connector, or see
  `CONNECTORS.md` at the repo root for how to get one added.
- **USPTO directly via customer number** — pulls status, deadlines, and
  correspondence for your whole portfolio rather than one application at a
  time. Not currently available as an MCP; on the wish list in
  `CONNECTORS.md`.

Without either, paste your docket or upload a spreadsheet and I'll track from
there.

## Purpose

A trademark registration that isn't renewed on time can be cancelled. A patent
without its maintenance fee paid lapses. A domain that expires can be sniped
within the hour. All of this is avoidable, and all of it depends on one thing:
the right deadline is on someone's calendar, tied to the right registration
number, in the right jurisdiction.

This skill maintains that calendar.

## Important: deadline reference caveat

> The deadline rules this skill applies reflect publicly available requirements
> as of the skill's build date. IP office requirements, grace periods, fee
> structures, and maintenance schedules change. **Always confirm computed
> deadlines against the USPTO TSDR / Patent Center, WIPO Madrid Monitor /
> Patentscope, EUIPO eSearch, UKIPO online records, or the relevant national
> registry before acting.** If you use Anaqua, CPA Global, Clarivate, Alt Legal,
> or another IP management system, their docket is authoritative for your
> assets — use this tracker to organize and surface their data, not to replace
> it.
>
> A docketed-but-wrong deadline is worse than an undocketed one: it creates
> false confidence. "No deadline soon" outputs especially deserve a second
> look before you rely on them.

## Jurisdiction and type assumptions

Maintenance mechanics vary by jurisdiction and asset type:

- **US trademarks:** §8 Declaration of Use between 5th and 6th anniversary of
  registration (or §71 for Madrid designations), then combined §8/§9 renewal
  at 10 years and every 10 years thereafter. §15 Incontestability available
  after 5 years of continuous use. 6-month grace period with surcharge for §8
  and §9; no grace for the underlying use itself.
- **Madrid International trademarks:** 10-year registration term renewable at
  WIPO; individual designated countries may have local use or declaration
  requirements (e.g., US §71).
- **EUIPO trademarks:** 10-year renewal; 6-month grace with surcharge.
- **US utility patents:** Maintenance fees due at 3.5, 7.5, and 11.5 years
  from grant. 6-month grace window with surcharge; after that, potential
  revival by petition if lapse was unintentional.
- **US design patents:** No maintenance fees — 15-year term from grant for
  applications filed on or after May 13, 2015 (14 years if earlier). No action
  required mid-term.
- **EPO / national patents:** Annuities typically due annually from filing or
  from national phase entry. National rules vary — confirm per jurisdiction.
- **US copyright:** No maintenance for works created 1978 or later.
  Pre-1978 works may have had renewal obligations; flag for attorney review
  if the asset pre-dates 1964 (rarely in scope for modern portfolios).
- **Domains:** Annual or multi-year renewal per registrar; typical 30-day
  grace then redemption period (~30 days at high fee) then drop.

If the portfolio includes assets in jurisdictions not listed above, capture
the maintenance mechanic in the register's `custom_rules` block and the
report will surface them as `agent_managed` — confirm status with the
foreign associate rather than computing a date this skill doesn't understand.

---

## The register

Lives at `~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml`.
Structure:

```yaml
# IP Portfolio Register
# Generated: [date]
# Last updated: [date]
# Disclaimer: computed deadlines are reference only — confirm with USPTO/WIPO/
# relevant registry or the IP management system of record before acting.

metadata:
  company: "[Company Name]"
  generated: "[date]"
  last_updated: "[date]"
  last_audit: "[date or null]"
  source_system: "[Anaqua / CPA Global / manual / none]"

custom_rules:   # non-built-in jurisdictions captured manually
  []

assets:
  - id: "TM-US-001"
    type: "trademark"                          # trademark / patent / copyright / design / domain
    jurisdiction: "US"
    mark_or_title: "[Mark or title]"
    owner: "[Record owner — registered entity name]"
    status: "registered"                       # pending / registered / lapsed / abandoned / cancelled
    application_number: "[number or null]"
    registration_number: "[number or null]"
    classes: ["9", "42"]                       # Nice classes for TM; CPC/IPC for patents; null otherwise
    filing_date: "[YYYY-MM-DD or null]"
    registration_date: "[YYYY-MM-DD or null]"
    priority_date: "[YYYY-MM-DD or null]"
    grant_date: "[YYYY-MM-DD or null]"         # patents
    next_deadlines:                            # computed; refreshed on --report and --audit
      - type: "§8 Declaration of Use"
        due_date: "[YYYY-MM-DD]"
        grace_end: "[YYYY-MM-DD or null]"
        basis: "5th-6th anniversary of registration"
        action: "File §8 Declaration of Use (or excusable nonuse)"
        status: "upcoming"                     # upcoming / due_soon / overdue / grace / filed
    use_in_commerce: true                      # TM only — drives §8 analysis
    agent_managed: false                       # true for foreign associate / outside counsel managed
    local_agent: null
    docket_id: "[IP-mgmt-system ID or null]"
    outside_counsel: "[firm or null]"
    business_owner: "[email or team]"
    notes: ""

  - id: "PAT-US-001"
    type: "patent"
    jurisdiction: "US"
    mark_or_title: "[Invention title]"
    owner: "[Owner]"
    status: "granted"
    application_number: "[number]"
    registration_number: "[patent number]"
    filing_date: "[YYYY-MM-DD]"
    grant_date: "[YYYY-MM-DD]"
    priority_date: "[YYYY-MM-DD or null]"
    expiration_date: "[YYYY-MM-DD]"            # 20 years from earliest non-provisional filing
    next_deadlines:
      - type: "3.5-year maintenance fee"
        due_date: "[YYYY-MM-DD]"
        grace_end: "[YYYY-MM-DD]"
        basis: "3.5 years from grant"
        action: "Pay maintenance fee (small/micro entity if applicable)"
        status: "upcoming"
    claims_count: 20
    entity_size: "large"                       # large / small / micro (drives USPTO fees)
    docket_id: null
    outside_counsel: null
    business_owner: null
    notes: ""
```

Status values for `next_deadlines`:
- `upcoming` — more than 90 days out
- `due_soon` — due within 90 days, not yet filed
- `overdue` — past the primary due date, within grace window (if any)
- `grace` — in the grace period (explicit flag — carries surcharge)
- `lapsed` — past grace with no action; asset effectively lost unless revivable
- `filed` — action completed this cycle

---

## Mode 1: Initialise

Run when no register exists, or with `--rebuild`.

### Step 1: Determine the source

Read `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`:
- **IP management system connected** (Anaqua, CPA Global, etc.): pull the portfolio via its integration. The IP system is the authoritative source; this register mirrors it and adds no deadlines the system doesn't already have.
- **No IP management system, but spreadsheet / export available:** ask the user to share the export. Import what's present; flag any asset missing a registration or grant date as `unknown` for deadline computation.
- **Nothing at hand:** walk through assets interactively — type, jurisdiction, number, key dates, owner.

### Step 2: For each asset, compute deadlines

Apply the rules at the top of this file. Populate `next_deadlines` with the
two or three closest upcoming items — further-out deadlines (10-year renewals
decades away) are computed on demand during reports rather than stored
speculatively.

**For assets the skill cannot confidently schedule:**
- Unknown jurisdiction rules → add a stub under `custom_rules` and flag the
  asset `agent_managed: true` with a TODO to confirm with the foreign associate.
- Missing dates needed for computation (no grant date for a patent, no
  registration date for a TM) → set `next_deadlines` empty with a note in
  `notes`, and list the asset as `unknown` in the initialisation summary.

### Step 3: Write the register

Generate `portfolio.yaml` at the config path. Show a summary:

```
Portfolio register initialised.

Assets: [N]
  Trademarks: [N]   ([N registered] / [N pending])
  Patents:    [N]   ([N granted] / [N pending])
  Copyrights: [N]
  Designs:    [N]
  Domains:    [N]

Deadlines computed: [N]
Agent-managed / jurisdiction TBC: [N] — confirm with foreign associates
Unknown (missing key dates): [N] — fill in before relying on reports

Run /ip-legal:portfolio --report to see what's due.
```

---

## Mode 2: Report

```
/ip-legal:portfolio --report [--days 30|60|90|180]
```

Default window: 90 days. Refresh computed deadlines for every asset before
producing the report — don't rely on stored dates alone.

Output (prepend work-product header per `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → Outputs):

```
IP PORTFOLIO DEADLINE REPORT — [date]
[Company Name] — window: next [N] days

🔴 LAPSED / IN GRACE ([N])
  [Asset ID] / [Jurisdiction] / [Type] / [Mark or title]
    [Action] — original due [date], grace ends [date]
    Status: [grace / lapsed]

⏰ DUE WITHIN [N] DAYS ([N])
  [Asset ID] / [Jurisdiction] / [Type] / [Mark or title]
    [Action] — due [date]
    Basis: [e.g., "5th-6th anniversary of registration"]
    [Agent: firm / docket: id — if present]

🟡 UPCOMING (next window beyond 30 days, within [N] days)
  [list]

🌐 AGENT-MANAGED ([N])
  [Asset ID] / [Jurisdiction] — managed by [local agent]; confirm directly
  [Asset ID] / [Jurisdiction] — no local agent recorded; add with --update

❓ UNKNOWN ([N])
  [Asset ID] — missing [field]; cannot compute deadline
  Confirm with [IP management system / USPTO TSDR / relevant registry] before relying on this report.

SUMMARY
  Total assets tracked: [N]
  Deadlines in window: [N]
  Last audit: [date]
```

Close the report with the caveat line: *"Computed from portfolio register. Verify each deadline against the USPTO/WIPO/registry of record before filing or paying."*

If the report lists more than ~10 assets, or any time the user asks: offer the dashboard (see CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Shape the offer for this output — counts by registration status (live / in grace / lapsed / pending), a deadline timeline, and a sortable portfolio table with jurisdiction, type, and next-action date.

---

## Mode 3: Add

```
/ip-legal:portfolio --add
```

Interactive add of a single asset. Ask for:
1. Type (trademark / patent / copyright / design / domain)
2. Jurisdiction
3. Mark or title / invention name
4. Owner (record owner — matters for §8 filings and assignments)
5. Key dates (per type: filing, registration, grant, priority, expiration)
6. Number(s)
7. Classes / claims count
8. Source — is this being tracked in the IP management system under a docket ID?
9. Outside counsel / foreign associate, if any
10. Business owner (who does this matter to — product line, brand manager)

After capture:
- Compute next deadlines per the rules at the top of this file.
- If jurisdiction rules aren't built in, walk through the `custom_rules` capture flow (see below).
- Append to `assets:` in `portfolio.yaml`.

### Custom rules capture

When a jurisdiction isn't in the built-in list:

> I don't have maintenance rules for [Jurisdiction] / [Asset type] built in.
> Let me capture them so we can track this going forward.
>
> 1. What maintenance events apply? (Renewal every N years? Annuities annually?
>    Declarations of use? Something else?)
> 2. What triggers the due date — filing date, registration date, grant date,
>    national phase entry, anniversary of something else?
> 3. Is there a grace period? At what cost?
> 4. Is there a foreign associate or local agent managing this?

Store under `custom_rules:` and apply to future assets in that jurisdiction.

---

## Mode 4: Update

```
/ip-legal:portfolio --update
```

### Consequential-action gate

**Before recording that a maintenance filing or fee payment was made:** Read
`## Who's using this` in `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Recording a §8 declaration, a §9 renewal, a patent maintenance fee payment,
> or an international annuity as "filed" has consequences. If the record is
> wrong — missed due date, wrong entity size, wrong specimen of use — the
> deadline doesn't move, and the asset can still lapse. Have you confirmed
> this with the attorney or foreign associate who actually made the filing
> (or with the USPTO TSDR / WIPO Madrid Monitor / relevant registry)? If yes,
> proceed. If no:
>
> - Do not record as filed yet.
> - Here is what to bring to the attorney: asset ID, jurisdiction, deadline
>   type, what the IP management system shows, what you believe was filed and
>   when, and the source of that belief.
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service
> is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

Do not set a deadline's `status` to `filed` past this gate without an
explicit yes. Status refresh, report generation, and upcoming-deadline
surfacing do not require the gate.

### Sub-modes

**Manual update:** "We filed the §8 for TM-US-001 on March 4, specimen
attached." Update the matching deadline: `status: filed`, `filed_date`,
and compute the next deadline in its lifecycle (for §8 that's the §9
renewal 10 years out).

**From IP management system sync:** If Anaqua / CPA Global / similar is
connected, pull the latest docket and reconcile. Flag mismatches between
the register and the system of record — the system of record wins; update
the register to match and surface anything the register had that the
system doesn't.

**Status change:** "Mark TM-US-004 as abandoned." Update `status`, clear
`next_deadlines`, note the date abandoned.

---

## Mode 5: Audit

```
/ip-legal:portfolio --audit
```

Broader health check beyond this month's deadlines:

**Deadline hygiene**
- Any deadlines in `grace` status right now? (In progress but surcharge-costing.)
- Any `lapsed` assets that aren't marked `abandoned` or `cancelled`? Either
  revive or update status.
- Any assets with no `next_deadlines` computed? Either missing data or a
  jurisdiction the skill doesn't know.

**Registration gaps**
- Trademark applications filed more than 18 months ago still `pending`?
  Flag for status check at the office — may need response to an action.
- Patents filed more than 4 years ago still `pending`? Flag for prosecution
  check.

**Use-in-commerce (TM only)**
- §8 approaching on a mark flagged `use_in_commerce: false` or uncertain?
  The §8 requires use; mark needs a use audit before filing or an excusable
  nonuse declaration.

**Ownership hygiene**
- Any assets where the `owner` is not a currently active entity per the
  entity register (if available)? Flag — may need recordal of assignment.
- Owner name inconsistencies across assets (same entity, different name
  strings)? Surface for cleanup.

**Expiration horizon**
- Any patents expiring in the next 24 months? Even without a maintenance
  deadline, the business may want to know — product planning, continuation
  strategy, licensing window.

**Unwatched assets**
- Any registered marks not on the watch list in CLAUDE.md → Brand protection?
  Flag as a gap for the attorney to decide whether to add.

Output format:

```
IP PORTFOLIO AUDIT — [date]

DEADLINE HYGIENE
  In grace: [N] — acting now avoids lapse
  Lapsed (not marked abandoned): [N] — confirm status
  Missing next-deadline computation: [N] — fill data or mark agent-managed

REGISTRATION GAPS
  TM applications pending >18 months: [list]
  Patent applications pending >4 years: [list]

USE IN COMMERCE (TM)
  §8 approaching on uncertain-use marks: [list]

OWNERSHIP
  Assets with unrecognised owner strings: [N]
  Owner name inconsistencies: [list]

EXPIRATION HORIZON (24 months)
  Patents expiring: [list]

BRAND WATCH
  Registered marks not on watch list: [list]

RECOMMENDED ACTIONS
  1. [highest priority]
  2. [etc.]
```

---

## Integration: ip-renewal-watcher agent

The `ip-renewal-watcher` agent in this plugin runs this skill on a schedule
(weekly by default) and posts the Mode 2 report to the channel named in
CLAUDE.md → Renewal alerts. If 🔴 items appear (grace / lapsed), the agent
posts them immediately regardless of schedule.

## Handoffs

- Receives: new asset records from prosecution skills (when an application
  is filed or a mark clears), from clearance skills (when a mark is adopted
  and a filing is queued), and from assignment recordals.
- Sends: "file §8 now" triggers to the attorney — this skill doesn't file
  anything; it tells the attorney the deadline and what to bring.

## What this skill does not do

- It does not file anything. Every action it surfaces is for the attorney
  or foreign associate to execute.
- It does not verify deadlines against the USPTO TSDR, WIPO, or any other
  registry. It computes them from the dates you give it. The register is
  a working copy; the registry is the source of truth.
- It does not decide whether to renew. Renewal is a business call — is the
  mark still in use, is the patent still valuable, does the domain still
  matter. This skill surfaces the deadline and the cost; the business and
  the attorney decide.
- It does not replace an IP management system for multi-hundred-asset
  portfolios. Anaqua, CPA Global, Clarivate, Alt Legal, and similar systems
  have direct registry feeds, deadline automation, and annuity payment
  services. This skill is best suited for smaller portfolios, or as a
  lightweight layer that surfaces what the system of record shows.
- It does not read office records to verify status. A §8 shown as "filed"
  here means someone told it so — not that the USPTO accepted it. Confirm
  acceptance through TSDR or the IP management system.

---

## /ip-legal:takedown

---
name: takedown
description: >
  Draft a DMCA takedown notice, triage one you received, or draft a §512(g)
  counter-notice. Use when asserting copyright through a §512(c)(3) takedown
  with the fair-use and perjury gates, when an incoming takedown needs triage
  into comply / counter / engage / ignore options, or when drafting a
  §512(g)(3) counter-notice with the consent-to-federal-jurisdiction gate.
argument-hint: "<--send | --respond | --counter> [context or path to incoming notice]"
---

# /takedown

Three modes. Pick one:

- `/ip-legal:takedown --send` — draft a §512(c)(3) takedown notice. Fair-use gate (*Lenz*) + loud perjury / §512(f) gate before delivery.
- `/ip-legal:takedown --respond` — triage a takedown someone sent you. Options: comply / counter / engage / ignore.
- `/ip-legal:takedown --counter` — draft a §512(g)(3) counter-notice. Loud gate for the federal-jurisdiction admission and the perjury statement.

## Instructions

1. **Read the practice profile.** Load `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. If it contains `[PLACEHOLDER]` markers or does not exist, stop and say: "This plugin needs setup before it can give you useful output. Run `/ip-legal:cold-start-interview` — the takedown skill depends on your approval matrix and practice profile."

2. **Check matter workspaces.** Per `## Matter workspaces`: if `Enabled` is `✗`, skip. If enabled and there is no active matter, ask: "Which matter is this for? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`."

3. **Dispatch on `$ARGUMENTS`:**
   - `--send` → run send mode (below). Walk identify-the-work, identify-the-infringing-material, fair-use gate (*Lenz*), good-faith belief, accuracy/authority, draft the §512(c)(3) notice, run the loud gate, write output.
   - `--respond` → run respond mode (below). Read the incoming notice, assess (license, fair use, defects, host §512(g) compliance, sender credibility), present the four options, recommend, write the triage memo.
   - `--counter` → run counter mode (below). Confirm the predicate (taken down in response to a §512 notice, good-faith belief of mistake/misidentification, ready for federal-jurisdiction admission, attorney in the loop), draft the §512(g)(3) counter-notice, run the loud gate, write output.
   - No flag → ask once: "Are we sending a DMCA takedown, triaging one we received, or drafting a counter-notice?"

4. **Respect the gates.** In `--send` and `--counter`, the loud gate runs before any final output is written. The fair-use gate in `--send` is separate and runs earlier; "debatable" or "likely" fair use stops the draft and routes to attorney review.

5. **Jurisdiction note.** DMCA §512 is US federal law. If the service provider, content, or infringer sits outside US jurisdiction, flag before drafting — you may need an EU DSA notice, UK OSA notice, or local-regime instrument instead of (or in addition to) a DMCA notice.

6. **Hand off where appropriate.** `--respond` with a counter-notice recommendation chains into `/ip-legal:takedown --counter` — but only after the triage memo has been reviewed and the decision to counter has been made deliberately.

## Examples

```
/ip-legal:takedown --send
/ip-legal:takedown --respond ~/Downloads/youtube-takedown-notice.pdf
/ip-legal:takedown --counter
/ip-legal:takedown
```

## Notes

- The outgoing notice and counter-notice do not carry the work-product header. Internal drafts, fair-use analyses, and triage memos do.
- §512(c)(3) and §512(g)(3) are element-by-element statutes — every required element must be present or the notice is defective.
- Counter-notices consent to federal court jurisdiction in the claimant's district (or a designated district for non-US subscribers). This is not a formality.
- Non-lawyer users get a one-page brief for the attorney conversation before the gate clears — particularly important for counter-notices, which are the step before litigation.

---

## Purpose

The DMCA §512 notice-and-takedown system is fast, cheap, and consequential in equal measure. A takedown is a sworn statement under penalty of perjury that gets content pulled with no judicial review. A counter-notice is another sworn statement that consents to federal jurisdiction and puts the content back. Both decisions can become litigation. This skill handles all three moves with the guardrails each warrants.

Three modes:

- `--send` — draft a §512(c)(3) takedown notice
- `--respond` — triage a takedown someone sent you; produce options
- `--counter` — draft a §512(g)(3) counter-notice

If the user does not pass a flag, ask once: "Are we sending a DMCA takedown, triaging one we received, or drafting a counter-notice?"

> **External deliverables (send and counter modes):** the outgoing notice/counter-notice goes to the service provider's designated agent. Do NOT include the `PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT` header on the outgoing document. The notice itself is not privileged — it's a statement made in a statutory process. Internal drafts, pre-send briefs, fair-use analyses, and triage memos keep the header per plugin config `## Outputs`.

## Jurisdiction assumption

DMCA §512 is **US federal law**. It runs against service providers subject to US jurisdiction. Other jurisdictions have their own notice-and-action regimes — EU Digital Services Act Art. 16, UK Online Safety Act, India IT Rules 2021, etc. — that differ materially in required elements, counter-notice mechanics, and liability for misuse. If the service provider, content, or infringer sits outside US jurisdiction, flag it — a US DMCA notice may be the wrong instrument, or may need to be paired with a local regime's notice. Copyright subsistence itself is Berne-multilateral, but enforcement mechanics are jurisdiction-specific.

## Load context

- `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` → `## IP practice profile` (copyright registrations if any), `## Enforcement posture` → `Approval matrix → DMCA takedown (ordinary)` row, `## Outputs` (work-product header, role), `## Who's using this` (role — lawyer vs. non-lawyer)
- **Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (in-house default), skip matter machinery. If enabled and no active matter, ask: "Which matter? Run `/ip-legal:matter-workspace switch <slug>` or say `practice-level`." Write outputs to the active matter's folder at `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/takedown/<slug>/` (or `takedown/<slug>/` at practice level). Never read another matter's files unless `Cross-matter context` is `on`.

## Send mode — drafting a §512(c)(3) takedown notice

### Step 1: Identify the copyrighted work

> What is the copyrighted work?
>
> - **Title / description** — what is the work (software, image, text, video, audio)?
> - **Registration status** — US Copyright Office registration number and date (if any). Registration is NOT required to send a takedown, but it is required to file suit on a US work and its pre-infringement timing controls statutory damages and fees.
> - **Ownership** — do we own it outright, or hold an exclusive license with takedown authority? (Non-exclusive licensees typically cannot send takedowns on the licensor's work.)
> - **Prior licensing** — have we ever licensed this use, or a broader use that might cover it?

Ownership and authority are the first things §512(f) cases look at. Get them clearly on the record before drafting.

### Step 2: Identify the infringing material and its location

> Where is the infringing material?
>
> - **Platform / service provider** — YouTube, Twitter/X, GitHub, Reddit, Amazon, a web host, etc.
> - **URL(s)** — specific permalinks to the infringing material. One notice can cover multiple URLs if they're all from the same service.
> - **Description** — what is the infringing material and how does it infringe (verbatim copy, substantially similar, derivative)?
> - **Screenshots / evidence** — preserved with timestamp and URL visible

§512(c)(3) requires "information reasonably sufficient to permit the service provider to locate the material." URLs alone are usually enough; be precise.

### Step 3: Fair-use gate

Under *Lenz v. Universal Music Corp.*, 801 F.3d 1126 (9th Cir. 2015), a copyright holder must consider fair use before sending a takedown. This is not a judgment about fair use — it is a consideration step that the sender must take and can prove they took.

Ask:

> Before we draft the notice, walk through fair use. Under *Lenz*, you have to consider it before sending — even if the conclusion is "not fair use." The four factors:
>
> 1. **Purpose and character** — commercial? transformative? criticism, comment, news reporting, teaching, scholarship, research?
> 2. **Nature of the copyrighted work** — factual or creative? published or not?
> 3. **Amount and substantiality** — how much of the work is used? is it the heart of the work?
> 4. **Effect on the market** — does the use substitute for the original or harm a derivative market?
>
> Your read on each? And your conclusion — fair use unlikely, debatable, likely?

Record the answer in the notice file. If "debatable" or "likely," do not draft. Stop and route to attorney review: "Fair use is debatable/likely on these facts. Sending a takedown on a use that is protected by fair use is the exact §512(f) exposure the statute creates. Route this to counsel before any notice goes out."

### Step 4: Good-faith belief

§512(c)(3)(A)(v) requires "a statement that the complaining party has a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law."

The sender forms this belief on the record. Have they:

- Confirmed the work is theirs (or they have takedown authority via exclusive license)?
- Confirmed the use is not licensed (no prior deal, no implied license, no Creative Commons grant that would cover it)?
- Considered fair use (Step 3)?
- Reviewed the accused content directly (not just a report about it)?

If yes on all four, the good-faith belief is colorable. If no on any, pause.

### Step 5: Accuracy and agent authority

§512(c)(3)(A)(vi) requires "a statement that the information in the notification is accurate, and under penalty of perjury, that the complaining party is authorized to act on behalf of the owner of an exclusive right that is allegedly infringed."

This is the perjury statement. It applies to the accuracy of the identification and the authority — not to the fair-use determination itself, though §512(f) liability reaches both.

Confirm signer: who is sending this on behalf of whom, and do they have authority to do so?

### Step 6: Draft the notice

§512(c)(3)(A) elements — every one must be present:

1. **Signature** (physical or electronic) of the rights holder or authorized agent
2. **Identification of the copyrighted work** — "Copyrighted work: [title, description, registration no. if any]"
3. **Identification of the infringing material** with location information — "Infringing material: [URL(s), description, how it infringes]"
4. **Contact information** — address, phone, email of the complaining party or agent
5. **Good-faith belief statement** — verbatim, adapted: "I have a good faith belief that use of the copyrighted material described above is not authorized by the copyright owner, its agent, or the law."
6. **Accuracy and authority statement under penalty of perjury** — verbatim, adapted: "I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner, or am authorized to act on behalf of the owner, of an exclusive right that is allegedly infringed."

Structure:

- Sender address block / date
- Recipient: designated DMCA agent at [service provider] (find via Copyright Office's DMCA Designated Agent Directory — `https://www.copyright.gov/dmca-directory/`)
- Re: Notice of Copyright Infringement pursuant to 17 U.S.C. §512(c)
- The six elements above, numbered or clearly set apart
- Signature line

Most service providers publish a preferred form or a web intake (YouTube Content ID / Copyright webform, Twitter / X copyright report, GitHub DMCA repo, etc.). The skill produces the notice content; the user submits through the provider's path. Note in the output which intake path is expected for the named service provider.

### Step 7: The loud gate before delivery

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS TAKEDOWN GOES ANYWHERE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A DMCA takedown is a statement under penalty of perjury.   │
│  Signing and sending it is not a routine administrative     │
│  step — it is a sworn declaration with specific legal       │
│  consequences.                                              │
│                                                             │
│  • 17 U.S.C. §512(f) creates LIABILITY for knowing          │
│    material misrepresentations. People have been sued,      │
│    and have lost, for bad-faith takedowns — *Lenz v.        │
│    Universal*, 801 F.3d 1126 (9th Cir. 2015); *Online       │
│    Policy Group v. Diebold*, 337 F. Supp. 2d 1195 (N.D.     │
│    Cal. 2004); *Stephens v. Clash*, 796 F.3d 281 (3d        │
│    Cir. 2015).                                              │
│                                                             │
│  • The accuracy and authority statement is sworn under      │
│    penalty of perjury. That is a real statement, not a      │
│    formality.                                               │
│                                                             │
│  • Sending a takedown on material that is in fact           │
│    licensed, owned by someone else, or fair use is the      │
│    fact pattern §512(f) was written for.                    │
│                                                             │
│  Confirm before the notice leaves:                          │
│                                                             │
│    1. You own the copyright, or you hold an exclusive       │
│       license with takedown authority.                      │
│    2. The accused use is not authorized — you have          │
│       checked licenses, grants, and any prior consents.     │
│    3. You considered fair use per *Lenz* (see Step 3 of     │
│       this draft); your conclusion is on the record.        │
│    4. Whoever has authority to sign approves sending.       │
│                                                             │
│  Approver per your practice profile: [approver from         │
│  Enforcement posture → Approval matrix → DMCA takedown      │
│  (ordinary) row]                                            │
│                                                             │
│  Automatic escalations that apply here: [list any from      │
│  the practice profile that this matter triggers]            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer (per `## Who's using this`), add:

> A DMCA takedown is sworn under penalty of perjury and creates §512(f) exposure for bad-faith or overbroad use. Have you reviewed this with an attorney? If not, here's a brief to bring to them: [generate a short summary: work, ownership, accused use, licensing check, fair-use analysis, signer, service provider]. A few thousand dollars of attorney time now is materially cheaper than a §512(f) suit.
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent); ABA IP section referral roster (US); law school IP clinics for individual creators and small businesses.

Do not write the final output without explicit engagement with the gate.

### Step 8: Output

**Primary:** `<matter-folder>/takedown/<slug>/notice-v<N>.md` (or .docx if the service provider accepts it — most accept pasted text or web-form submission). The notice content, ready to paste into the service provider's DMCA intake form or send to its designated agent.

**In-chat:** show the notice as plain text for review before writing. Iterate before committing to disk.

**Reviewer-facing closing note** (in the in-chat preview only):

> This is a draft DMCA notice for attorney review, not a notice ready to send. Sending it is a sworn statement with §512(f) exposure. A licensed attorney reviews, edits, and takes professional responsibility before submission. Do not send this unreviewed.

**Citation verification.** Any case or statutory citation included (for example, in internal memoranda around the notice) must be verified on a legal research tool. Source-tag each — `[Westlaw]`, `[CourtListener]`, `[user provided]`, `[model knowledge — verify]`, `[web search — verify]`. Citations tagged `verify` get checked first. No silent supplement from web or model knowledge if a configured research tool comes up thin — present options to the user.

**Post-send record.** After submission, write `<matter-folder>/takedown/<slug>/submission.md`: service provider, designated agent used (address or web form URL), date submitted, confirmation ID if returned, URLs targeted, counter-notice watch date (generally 10–14 business days), legal hold refreshed.

## Respond mode — triaging a takedown you received

Your content was taken down. A service provider has notified you of a §512(c)(3) notice. You have options.

### Step 1: Read the notice you received

Extract:

- **Sender** — entity, signer, address, email
- **Service provider** — who notified you (the platform)
- **Claimed work** — what they say is theirs
- **Your content alleged to infringe** — URL(s) or identifiers as they named them
- **Date of takedown / notice**
- **Whether the notice appears to meet §512(c)(3) on its face** — flag missing elements; a defective notice is not a proper notice

### Step 2: Assess

- **Do we have a license?** Negotiated, implied, Creative Commons, prior settlement, assignment — anything that authorizes the use.
- **Is it fair use?** Walk the *Lenz* four factors. Be honest; this is for us, not the response.
- **Is the notice defective?** Missing any of the §512(c)(3)(A) elements, lacking the perjury statement, signed by someone without apparent authority? Defective notices are not properly compliant; the host may still act on them but the sender's §512(f) exposure rises and our leverage rises.
- **Did the host comply properly with §512(g)?** Were we given notice and an opportunity to counter? If the host acted without giving us the chance, that is a separate issue with the host (not the sender).
- **Is the sender a troll?** Repeat pattern of overbroad takedowns on this platform?

### Step 3: Options

Present 4 options with tradeoffs:

**A — Comply (let the takedown stand)**
- When: they're right, or the fight isn't worth it
- Tradeoff: content stays down; may affect SEO, accounts with strikes policies, livelihood for creators
- Next step: log the event, confirm no counter-notice deadline issues, move on

**B — Send a counter-notice** (§512(g)(3))
- When: we have a good-faith belief the material was misidentified or removed by mistake — often applies where the use is licensed, fair use, or the sender doesn't own the work
- Tradeoff: sworn under penalty of perjury, consents to federal court jurisdiction in the sender's district (or our own if outside the US and we designate), puts the decision in the sender's hands for 10–14 business days — if they sue, content stays down; if they don't, content is restored
- Next step: `/ip-legal:takedown --counter`

**C — Engage the sender directly**
- When: there's room for a business resolution (license, credit, takedown of a narrower portion)
- Tradeoff: the content stays down during the conversation; settlement-communication hygiene matters (FRE 408 or equivalent; protection from substance and context, not labeling)
- Next step: outreach letter to the sender; do not send the counter-notice while discussions are live

**D — Ignore and let it stand; raise it elsewhere**
- When: the harm is small, we don't want the federal-jurisdiction admission, and we'd rather deal with the sender separately
- Tradeoff: content stays down; if the takedown itself was bad-faith, we may have §512(f) to assert on our own schedule — but that's its own fight

Recommend one with two sentences of rationale.

### Step 4: Write triage memo

Output: `<matter-folder>/takedown/inbound/<slug>/triage.md`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

> **Privilege inheritance.** This triage records our first-pass assessment of an adverse takedown. It is attorney-client and/or work-product material. Do not forward outside the privilege circle or attach to counter-notice submissions without scrubbing.

# DMCA Takedown Received — Triage

> **READ FOR TRIAGE, NOT OPINION.** Structured intake scan, not a legal merit opinion. Every authority flagged for SME verification; every merit call is counsel's.

**Slug:** [slug]
**Received:** [YYYY-MM-DD]
**Service provider:** [platform]
**Incoming file:** [path]

## The notice

**Sender:** [entity, signer, counsel if any]
**Claimed work:** [title, description, reg no. if provided]
**Our content targeted:** [URLs / identifiers]
**Date of takedown:** [YYYY-MM-DD]
**Notice meets §512(c)(3) on its face:** [yes / no — list any missing elements]

## Assessment

**License / authorization check:** [read]
**Fair use walkthrough (Lenz factors):** [read — each factor + conclusion; `[SME VERIFY]`]
**Notice defects:** [list or none]
**Host compliance with §512(g):** [were we given notice and opportunity]
**Sender credibility:** [troll / real claimant / repeat takedown pattern]

## Options

### A. Comply
### B. Counter-notice (§512(g)(3))
### C. Engage sender
### D. Ignore

**Recommendation:** [A/B/C/D] — [two sentences why] — `[SME VERIFY: counsel to confirm before executing]`

## Deadlines

- **Counter-notice watch window:** 10–14 business days after counter-notice is submitted — content stays down if sender files suit in that window
- **Sender's suit filing timing:** typically on our counter-notice clock, if we counter
- **Any contractual deadlines with the host:** [check]

## Immediate actions

- [ ] Legal hold issued on the accused work and our related content — [yes/no]
- [ ] Business impact assessed (revenue, account strikes, SEO) — [yes/no]
- [ ] Matter created in log — [yes/no/TBD]
- [ ] Counsel assigned — [who]
```

Close the in-chat presentation with:

> This is a triage memo, not advice. The assessments above are a first read from the four corners of the notice. An attorney evaluates before you counter-notice (which consents to federal jurisdiction) or decide not to respond.

## Counter mode — drafting a §512(g)(3) counter-notice

Counter-notices put content back up unless the original sender sues within 10–14 business days. They are the step before litigation.

### Step 1: Confirm the predicate

- The content was taken down in response to a §512 notice (not a terms-of-service action by the host).
- You have a good-faith belief the material was removed by mistake or misidentification — the statutory test.
- You are prepared to consent to federal court jurisdiction in the original sender's district (or designate if you are outside the US).
- The decision has been made deliberately — not in reaction, not without attorney input.

### Step 2: Draft per §512(g)(3)

§512(g)(3) elements — every one must be present:

1. **Signature** (physical or electronic) of the subscriber
2. **Identification of the material removed** and its location before removal (the URL where the content was)
3. **Statement under penalty of perjury that the subscriber has a good faith belief the material was removed or disabled as a result of mistake or misidentification** — verbatim, adapted
4. **Subscriber's name, address, telephone number** — and, critically, **consent to the jurisdiction of the federal district court** for the district where the subscriber's address is located (or, if outside the US, any district in which the service provider may be found), and acceptance of service of process from the person who provided notification or that person's agent

Structure:

- Subscriber address block / date
- Recipient: designated DMCA agent at the service provider (same agent that received the original takedown)
- Re: Counter-Notification pursuant to 17 U.S.C. §512(g)
- The four elements above, numbered or clearly set apart
- Signature line

### Step 3: The loud gate before delivery

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE THIS COUNTER-NOTICE GOES ANYWHERE                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A DMCA counter-notice is a statement under penalty of      │
│  perjury AND consents to federal court jurisdiction. It     │
│  is the step before litigation.                             │
│                                                             │
│  • If the original claimant files suit within 10–14         │
│    business days after your counter-notice, the content     │
│    stays down pending the suit. 17 U.S.C. §512(g)(2)(C).    │
│                                                             │
│  • If they do not sue within the window, the host must      │
│    restore the content within 14 business days of your      │
│    counter-notice.                                          │
│                                                             │
│  • You are consenting to be sued in federal court in the    │
│    claimant's judicial district (or, if you are outside     │
│    the US, designating a district). This is a jurisdiction  │
│    admission you make by signing.                           │
│                                                             │
│  • The perjury statement is real. §512(f) liability runs    │
│    in both directions — senders and counter-senders.        │
│                                                             │
│  Confirm before the counter-notice leaves:                  │
│                                                             │
│    1. The material was removed in response to a §512        │
│       notice (not a TOS action).                            │
│    2. You have a good-faith belief the removal was a        │
│       mistake or misidentification — because the use is     │
│       licensed, fair use, not actually infringing, or the   │
│       sender doesn't own the work.                          │
│    3. You are prepared to be sued in federal court in the   │
│       claimant's district. Budget, counsel, and risk        │
│       tolerance are all set.                                │
│    4. An attorney has reviewed this before it is sent.      │
│                                                             │
│  Approver per your practice profile: [approver from         │
│  Enforcement posture → Approval matrix — counter-notices    │
│  generally route above the DMCA takedown (ordinary)         │
│  approver because of the federal-jurisdiction admission]    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

If the user is a non-lawyer:

> A counter-notice consents to federal court jurisdiction and is sworn under penalty of perjury. Have you reviewed with a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction? This is not the Claude-review layer; this is the step where you need licensed professional judgment. Brief for the conversation: [generate a 1-page summary]. Referral resources: your professional regulator's referral service (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent); law school IP clinics; ABA IP section (US).

Do not write the final output without explicit engagement.

### Step 4: Output

**Primary:** `<matter-folder>/takedown/<slug>/counter-notice-v<N>.md` — the counter-notice content, ready to submit via the service provider's counter-notice intake.

**In-chat:** present as plain text for review before committing.

**Reviewer-facing closing note** (in-chat only):

> This is a draft counter-notice for attorney review, not a counter ready to send. Sending it is a sworn statement and consents to federal court jurisdiction in the claimant's district. A licensed attorney reviews before submission. Do not send this unreviewed.

**Post-submission record.** After submission, write `<matter-folder>/takedown/<slug>/counter-submission.md`: service provider, date submitted, confirmation ID, 10–14 business-day watch window end date calendared, watch for suit filing in the claimant's district, plan if content is restored, plan if suit is filed.

## Decision posture

Per `## Decision posture on subjective legal calls` in the practice profile: when uncertain whether the use is fair, whether the rights holder is us, whether the work is actually ours, whether fair use defeats the claim on the receiving side — do not silently decide. Fair use is the paradigmatic uncertain call. Flag for attorney review; surface the factors. Sending a takedown or a counter-notice on an assumption is a one-way door.

## What this skill does not do

- **Submit the notice.** Drafting only. The user submits through the service provider's designated channel.
- **Pick a service provider's intake form for the user.** Notes which path is expected; does not auto-submit.
- **Decide fair use.** Walks the four factors; flags. An attorney decides whether to proceed.
- **Validate the sender's claim on the receive side.** Structured read; every authority flagged for SME verification.
- **Bypass the gate.** The gate runs every time in `--send` and `--counter` modes.
- **Invent citations.** Any cites included are source-tagged and flagged for verification; no silent supplement.
- **Handle non-US regimes.** DMCA is US-specific. For EU DSA, UK OSA, India IT Rules, and other regimes — flag and route.

---

