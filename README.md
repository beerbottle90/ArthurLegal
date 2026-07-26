# ArthurLegal

> **Proprietary — Non-Commercial Use Only. All Rights Reserved. See [LICENSE](LICENSE).**

Türk hukukuna adapte edilmiş, **Claude.ai Projects** üzerinde çalışan hukuk
asistanı paketleri. Her paket bir `SYSTEM_PROMPT.md` (Custom Instructions) ve
bir `knowledge/` klasöründen oluşur.

## Paketler — güncel sürümler

| Profil | Güncel sürüm | Kime | Kapsam |
|---|---|---|---|
| **Corporate Assistant** | **[v1.4.0](ArthurLegal-CorporateAssistant-v1.4.0-Public-Release/)** | Şirket içi (in-house) hukuk ekibi | 12 pratik alan · 17 yargı çevresi · 5 MCP · 67 knowledge dosyası |
| **Law Firm Assistant** | **[v1.4.0](ArthurLegal-Law-Firm-v1.4.0-Public-Release/)** | 0–30 kişilik hukuk bürosu | 16 pratik alan · 17 yargı çevresi · 5 MCP · 92 knowledge dosyası |
| Academician | [v1.0.0](ArthurLegal-Academician-v1.0.0-Public-Release/) | Hukuk akademisyeni | Yayın, dergi seçimi, doçentlik, etik kurul |
| Courthouse | [v1.0.0](ArthurLegal-Courthouse-v1.0.0-Public-Release/) | Adliye tarafı | Hâkim/savcı iş akışları |

Önceki sürümler arşiv olarak korunur (`v1.0.0`, `v1.0.1`, `v1.2.0`, `v1.3.1`).
Kurulum için ilgili paketin `KURULUM.md` dosyasından başlayın.

### v1.4.0 — kaynak katmanı (26.07.2026)

Corporate ve Law Firm paketlerine `legal-research` eklentisi ve üç **self-hosted,
auth'suz** MCP sunucusu eklendi:

| MCP | Rol | Kapsam |
|---|---|---|
| **e-qanun** | **BİRİNCİL** | Azerbaycan mevzuatı — resmî `api.e-qanun.az`; **yürürlük statüsü doğrulamalı** (`Qüvvədədir` / `Ləğv olunmuş`) |
| **LexScholar** | **İKİNCİL** | 10 açık erişim indeksi federe; **DergiPark'ın 19 doğrulanmış Türk hukuk dergisi** resmî OAI-PMH ucundan |
| **ResourceContracts** | **EMSAL** | 5.125 imzalı petrol & madencilik sözleşmesi, 107 ülke + uzman kloz anotasyonları (CC BY-SA 4.0, NRGI/CCSI) |

Üçü de **isteğe bağlıdır** — kurulmazsa paketler çalışmaya devam eder ve asistan
kapsam daralmasını çıktısında belirtir. Ayrıntı: ilgili paketin `CHANGELOG.md`
dosyası.

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

## Türkçe

> **Tescilli (Proprietary) — Yalnızca ticari olmayan kullanım. Tüm hakları saklıdır. Bkz. [LICENSE](LICENSE).**

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
