---
name: energy-finance-jv-agreement-review
description: >
  Enerji sektörü ortak girişim (JV) ve hissedar sözleşmelerini inceler.
  Yönetim yapısı, kilitlenme mekanizmaları, çıkış hakları, rekabet yasağı,
  EPDK lisans uyumu ve çok taraflı/uluslararası JV özel dikkat noktaları.
argument-hint: "[JVA / SHA / konsorsiyum sözleşmesi dosyası]"
---

# /jv-agreement-review — JV & Hissedar Sözleşmesi İncelemesi

## Adım 1 — Yapı haritası

| Unsur | Değer |
|---|---|
| JV türü | SPV kurulumu / Var olan şirkete katılım / Konsorsiyum |
| Taraflar + hisse oranları | [Müvekkil]: % / Karşı taraf: % |
| Governing law | [belirle] |
| Tahkim | |
| JV amacı ve süresi | |
| Karşı taraf ülkesi | [belirle — yabancı ortak varsa hukuk sistemi notu] |

## Adım 2 — Yönetim yapısı & kilit karar mekanizmaları

- **Board kompozisyonu:** [Müvekkil] atama hakkı, veto hakları
- **Süper çoğunluk kararlar:** neler var, eşik nedir?
- **Deadlock mekanizması:** Russian roulette / Texas shoot-out / mediasyon / fesih
- **CEO/CFO atama:** [Müvekkil] belirliyor mu, müşterek mi?
- **Operasyonel kararlar:** günlük işletme, capex eşiği, borçlanma onay

## Adım 3 — Çıkış hakları ve transfer kısıtlamaları

- **Tag-along / drag-along:** şartlar, fiyat hesabı
- **Ön alım hakkı (right of first refusal):** süre, şekil
- **Kilit-up (lock-up):** süre, istisnalar
- **Change of control:** JVA fesih tetikler mi?
- **Put/call opsiyonları:** tetikleyiciler (performance, EPDK lisans kaybı, deadlock)
- **Çıkış valuation:** EBITDA multiple / DCF / third party appraisal

## Adım 4 — Rekabet yasağı & münhasırlık

- Rekabet yasağı süresi, coğrafi kapsamı — 4054 sayılı RKHK m.4 sınırı aşıyor mu?
- AB Rekabet Tüzüğü (ECMR) — AB cirosu varsa Komisyon bildirimi tetiklenir mi?
- Müvekkilin mevcut enerji portföyü ile örtüşme riski?
- Münhasır teknoloji / know-how lisansı var mı?

## Adım 5 — EPDK & düzenleyici uyum

- JV yapısının EPDK lisans şartlarını etkileyip etkilemediği
- Çoklu lisans sahibi JV'lerde konsolidasyon ve pazar payı bildirimi
- Müvekkil halka açıksa: önemli işlem bildirimi eşiği (SPK/KAP)

## Adım 6 — İlişkili taraf & uluslararası ortak özel dikkat

Karşı taraf ilişkili kuruluş veya yabancı ortak ise:
- Transfer fiyatlandırması (TP) riski — KVK m.13
- Yaptırım riski (OFAC/AB) — özellikle CIS, İran, Rusya bağlantılı taraf varsa
- Yabancı ortağın kurumsal yönetim gereksinimleri
- Döviz kontrol kuralları (ilgili ülke mevzuatı)

## Findings özeti

| # | Kloz | Severity | Not |
|---|---|---|---|
| | | 🔴/🟠/🟡/🟢 | |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# JV & Hissedar Sözleşmesi İncelemesi — [JV adı / tarih]

## ⚠️ Reviewer note

## Bottom line

## Yapı haritası

## Yönetim & karar mekanizmaları

## Çıkış hakları

## Rekabet & düzenleyici

## İlişkili taraf notları (varsa)

## Findings

## Önerilen kloz değişiklikleri
```

---

## Kaynak katmani — /legal-research (v1.4.0)

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur —
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| **bu plugin icin birincil kullanim** — PSA/JOA, cost recovery, profit split, stabilizasyon, DMO, decommissioning, yerel icerik benchmark'i | `/arthurlegal:legal-research-sozlesme-emsali` |
| AZ upstream/yer alti serveti rejimi, JV ve enerji mevzuati — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| Energy Charter Treaty, yatirim tahkimi, stabilizasyon klozu ogretisi — **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
