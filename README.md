# ArthurLegal

> **Proprietary — Non-Commercial Use Only. All Rights Reserved. See [LICENSE](LICENSE).**

**Multi-jurisdiction legal AI assistant packages that run on [Claude.ai Projects](https://claude.ai/projects).**
Each package is a `SYSTEM_PROMPT.md` (Custom Instructions) plus a `knowledge/`
folder, and reaches **14 jurisdictions** through **up to 7 MCP connectors** and a
curated primary-source reference layer.

Built for legal teams that work across borders: a contract governed by English
law, arbitrated in Geneva, with an Azerbaijani counterparty and an EU data-transfer
question is one workflow, not four.

## Packages — current versions

| Profile | Current version | For | Scope |
|---|---|---|---|
| **Corporate Assistant** | **[v1.4.0](ArthurLegal-CorporateAssistant-v1.4.0-Public-Release/)** | In-house legal teams | 12 practice areas · 14 jurisdictions · up to 7 MCP connectors · 66 knowledge files |
| **Law Firm Assistant** | **[v1.4.0](ArthurLegal-Law-Firm-v1.4.0-Public-Release/)** | Law firms, 0–30 staff | 16 practice areas · 14 jurisdictions · up to 7 MCP connectors · 91 knowledge files |
| Academician | [v1.0.0](ArthurLegal-Academician-v1.0.0-Public-Release/) | Legal academics | Publication strategy, journal selection, associate-professorship track, ethics board |
| Courthouse | [v1.0.0](ArthurLegal-Courthouse-v1.0.0-Public-Release/) | Bench and prosecution | Judge and prosecutor workflows |

The two flagship packages (Corporate, Law Firm) are multi-jurisdictional. The
Academician and Courthouse packages are built around Turkish academic-promotion
and Turkish judicial procedure respectively, and are jurisdiction-specific by
design.

Earlier versions are retained as archives (`v1.0.0`, `v1.0.1`, `v1.2.0`, `v1.3.1`).
To install, start from the `KURULUM.md` (Turkish) or `INSTALLATION.md` (English)
file in the package you want.

## Jurisdictional coverage

Coverage is real but **not uniform in depth** — the packages state which tier a
source sits in, and the assistant flags reduced coverage in its output rather
than filling the gap with recalled text.

**14 jurisdictions** = 12 national (🇹🇷 TR · 🇨🇭 CH · 🇺🇸 US · 🇦🇿 AZ · 🇬🇧 UK ·
🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU · 🇨🇳 CN · 🇷🇸 RS) + 2 supranational
legal orders (🇪🇺 EU/CJEU · ECHR).

| Tier | Jurisdictions | How it is reached |
|---|---|---|
| **Primary-source MCP** — verbatim norm text and case law | 🇹🇷 Türkiye · 🇨🇭 Switzerland · 🇺🇸 United States *(case law)* · 🇦🇿 Azerbaijan | **TR Legal MCP** (15 institutions, 40+ tools) · **OpenCaseLaw.ch** (972K+ decisions, 33 tools) · **CourtListener** (Free Law Project — US federal and state case law, PACER, citation verification) · **Fedlex** (Swiss federal legislation) · **e-qanun** (in-force status verified) |
| **Legislation via WebFetch** — no extra connector | 🇬🇧 UK · 🇺🇸 US *(federal legislation, GovInfo)* · 🇪🇺 EU / CJEU / ECHR · 🇩🇪 Germany · 🇫🇷 France · 🇮🇹 Italy · 🇯🇵 Japan · 🇷🇺 Russia · 🇨🇳 China · 🇷🇸 Serbia | Official gazette and legislation portals |
| **Cross-cutting corpora** — precedent, doctrine, screening | 107 countries (signed contracts) · 10 open-access scholarship indexes · global sanctions / PEP | **ResourceContracts** · **LexScholar** · **OpenSanctions** (REST API, API key) |

Türkiye currently has the deepest coverage: a dedicated MCP server spanning 15
institutions with 40+ tools, plus the largest share of the reference layer.
Switzerland (972K+ decisions and Fedlex legislation) and Azerbaijan (official
`api.e-qanun.az` with in-force status verification) follow.

## v1.4.0 — research source layer (2026-07-26)

The Corporate and Law Firm packages gained a `legal-research` plugin and three
**self-hosted, no-auth** MCP servers:

| MCP | Role | Coverage |
|---|---|---|
| **e-qanun** | **PRIMARY** | Azerbaijani legislation — official `api.e-qanun.az`; **in-force status verified** (`Qüvvədədir` / `Ləğv olunmuş`) |
| **LexScholar** | **SECONDARY** | 10 federated open-access indexes; includes 19 verified Turkish law journals via DergiPark's official OAI-PMH endpoint |
| **ResourceContracts** | **PRECEDENT** | 5,125 signed petroleum and mining contracts across 107 countries, with expert clause annotations (CC BY-SA 4.0, NRGI/CCSI) |

All three are **optional** — the packages work without them, and the assistant
states the narrowed scope in its output. Details: the `CHANGELOG.md` of the
relevant package.

---

Copyright (c) 2026 ArthurLegal. All rights reserved.

This repository is **source-available but not open source**. **Commercial use is
prohibited.** Within that limit, you are permitted to use, run, and modify the
Software for non-commercial purposes.

The following are expressly **not** commercial use:

- use by an **in-house counsel**, or any member of an in-house legal department,
  in the ordinary course of their duties;
- use by an **employee of a law firm** — partner, associate, trainee, paralegal
  — in the ordinary course of their duties, including work performed for the
  firm's clients;
- **personal use** by a natural person;
- **modifications** a person makes, or commissions a third party to make, for
  their own permitted use (and does not distribute).

Revenue earned from the *legal services* in which the Software is used does not
make that use commercial. What is prohibited is commercializing **the Software
itself** — selling, sublicensing, redistributing, or offering it as a product or
hosted service. Redistribution of any kind requires prior written permission.

This repository includes third-party components licensed under the Apache
License 2.0 (the Anthropic [`claude-for-legal`](https://github.com/anthropics/claude-for-legal)
knowledge base). Those components remain governed by their own license; their
license texts and attribution notices are retained in the release packages and
must not be removed.

See the [LICENSE](LICENSE) file for the full and binding terms.

---

## Türkçe — lisans

> **Tescilli (Proprietary) — Yalnızca ticari olmayan kullanım. Tüm hakları saklıdır. Bkz. [LICENSE](LICENSE).**

*Aşağıdaki metin kolaylık sağlamak için sunulmuştur; bağlayıcı olan [LICENSE](LICENSE)
dosyasındaki İngilizce koşullardır.*

Telif Hakkı (c) 2026 ArthurLegal. Tüm hakları saklıdır.

Bu depo **kaynağı görünür ancak açık kaynak değildir.** **Ticari kullanım
yasaktır.** Bu sınır içinde yazılımı ticari olmayan amaçlarla kullanabilir,
çalıştırabilir ve değiştirebilirsiniz.

Aşağıdakiler ticari kullanım **sayılmaz**:

- **Şirket içi (in-house) hukuk müşavirinin** veya hukuk departmanı çalışanının
  olağan görevleri kapsamındaki kullanımı;
- Bir **hukuk bürosu çalışanının** — ortak, avukat, stajyer, paralegal —
  olağan görevleri kapsamındaki kullanımı; büronun müvekkilleri için yapılan
  çalışmalar dahil;
- Gerçek kişinin **kişisel kullanımı**;
- Kişinin kendi izinli kullanımı için bizzat yaptığı veya bir üçüncü kişiye
  **yaptırdığı geliştirmeler** (başkasına dağıtılmamak kaydıyla).

Yazılımın kullanıldığı *hukuki hizmetlerden* gelir elde edilmesi, o kullanımı
ticari hâle getirmez. Yasak olan, **yazılımın kendisinin** ticarileştirilmesidir
— satmak, alt lisanslamak, yeniden dağıtmak veya bir ürün ya da barındırılan
hizmet olarak sunmak. Her türlü yeniden dağıtım önceden yazılı izne tabidir.

Bu depo, Apache 2.0 lisanslı üçüncü taraf bileşenler (Anthropic
[`claude-for-legal`](https://github.com/anthropics/claude-for-legal) bilgi
tabanı) içerir. Bu bileşenler kendi lisanslarına tabidir; lisans metinleri ve
atıf bildirimleri paketlerde korunmuştur ve kaldırılamaz.

Tam ve bağlayıcı koşullar için [LICENSE](LICENSE) dosyasına bakınız.
