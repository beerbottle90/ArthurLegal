# Installation — ArthurLegal Academician Assistant v1.0.0

> English installation guide. Türkçe → [KURULUM.md](KURULUM.md)
>
> Target environment: [Claude.ai Projects](https://claude.ai/projects) (web).
> Time required: ~15 minutes.

---

## Step 1 — Create a Claude.ai Project

1. [claude.ai](https://claude.ai) → sidebar → **Projects** → **Create Project**
2. Name: `ArthurLegal Academician` (or your preference)
3. Description: `Research & writing assistant for legal academics`

## Step 2 — Paste the system instructions

1. In the project, open **Set custom instructions** (or ⚙️ → Instructions)
2. Copy and paste the **entire** [`SYSTEM_PROMPT.md`](SYSTEM_PROMPT.md) file
3. Save

> The file is written in Turkish, but the assistant answers in whichever language you
> write in — and honours the `Çıktı dili` (output language) field in your profile.

## Step 3 — Upload the knowledge files

In the project, **Add content / Upload** everything under `knowledge/`:

```
knowledge/
├─ akademisyen-profili.md      ← fill this in first (Step 4)
├─ skills/      (8 files)
├─ references/  (23 files)
└─ agents/      (4 files)
```

Drag the folder in if bulk upload is available. Upload order does not matter.

## Step 4 — Fill in your profile

Complete [`knowledge/akademisyen-profili.md`](knowledge/akademisyen-profili.md) **before**
uploading it. The package ships every field as a `[DOLDUR]` (fill-in) placeholder and
contains **no real personal or institutional data**.

The four fields that matter most:

| Field | Why it matters |
|---|---|
| **Doctorate date** | The "post-doctorate" threshold in associate-professorship scoring depends on it |
| **Citation style** | Classic Turkish full-footnote / OSCOLA / Bluebook — determines output form |
| **Role flags** (reviewer / editor / panellist / examiner) | Triggers the confidentiality rule |
| **ÜAK period PDF confirmed?** | Without `Yes`, no definitive promotion score is produced |

## Step 5 — Add MCP connectors (optional, recommended)

Add via Claude.ai → **Settings → Connectors**:

| Server | Purpose | Required |
|---|---|---|
| **TR Legal MCP** (Mevzuat + Yargı) | Turkish legislation, Court of Cassation / Council of State / Constitutional Court | Yes, for Turkish law work |
| **CourtListener** | US case law (comparative work) | No |
| **Fedlex** | Swiss federal legislation | No |
| **OpenCaseLaw.ch** | Swiss case law + scholarship bridge | No |

Without connectors the assistant still runs, but it **will not cite**. Every proposition is
tagged `[model bilgisi — DOĞRULAYIN]` (*model knowledge — verify*) and you are asked to
verify manually. This is the zero-hallucination rule working as intended, not a bug.

> **No API key needed.** Crossref, OpenAlex, Semantic Scholar, DOAJ, ORCID, EUR-Lex and
> HUDOC are reached over WebFetch without keys. This package embeds no API keys.

## Step 6 — Try it

In the project, type:

```
/yayin-etigi:uyz-beyani
```

The assistant should ask for the tool version, date and scope of use, then produce an AI
use statement formatted for your target venue (TÜBİTAK / TR Dizin / international journal /
thesis).

Then try:

```
/arastirma-tasarim:etik-kurul-triyaji
```

It should determine, by questioning, whether your study requires ethics-committee approval.

---

## Frequently encountered

**The assistant refuses to cite and says "DOĞRULAYIN".**
Expected. If no connector is present, or the source could not be retrieved, the assistant
does **not** invent one. Add the connector, or verify the source yourself.

**I pasted a manuscript I'm peer-reviewing and it refused.**
Correct behaviour. Entering a manuscript under evaluation into a generative AI tool
breaches confidentiality (TÜBİTAK GenAI Guide § 2.2.1; NIH NOT-OD-23-149; NSF; Elsevier;
Springer Nature; Wiley; ICMJE). Use `/hakemlik-editorluk:hakem-rubrigi`, which builds a
report skeleton **without** the manuscript.

**It won't compute my associate-professorship score.**
Your profile must have `Başvuru dönemi ÜAK PDF'i teyit edildi mi?` set to `Evet`. Criteria
change between application periods; the assistant will not give a definitive figure from a
stale table.

**My similarity score is 18% — is that fine?**
The assistant will not give you a threshold, and should not. There is **no universally
accepted percentage**; your institution or journal sets it. `/yayin-etigi:benzerlik-yorumu`
reads the report **qualitatively**: which matches are legitimate quotation, which are not.

**Wrong output language.**
Set the `Çıktı dili` field in `akademisyen-profili.md`.

---

## Updating

On a new release, replace `SYSTEM_PROMPT.md` and the `knowledge/` files, but **keep** your
own `akademisyen-profili.md` — it holds your data.
Release notes → [CHANGELOG.md](CHANGELOG.md)
