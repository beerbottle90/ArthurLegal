---
name: energy-finance-project-finance-review
description: >
  Enerji altyapısı proje finansmanı belgelerini inceler: facility agreement, security
  package, conditions precedent checklist, lender's due diligence.
  EPDK lisans teyidi ve SPK bildirim kontrolü dahil.
argument-hint: "[facility agreement | info memo | CP checklist | term sheet]"
---

# /project-finance-review — Proje Finansmanı Belge İncelemesi

Birincil yargı çevresi Türkiye'dir. Finansman belgelerinde İngiliz hukuku + Londra
tahkimi yaygın; governing law analizi için `/arthurlegal:commercial-legal-governing-law-review` çalıştır.

## Adım 0 — Belge tespiti

| Belge | Mevcut mu? |
|---|---|
| Facility Agreement (ana kredi) | [evet/hayır] |
| Security Package (teminat belgeleri) | [evet/hayır] |
| CP Checklist (conditions precedent) | [evet/hayır] |
| Term Sheet | [evet/hayır] |
| Technical Due Diligence raporu | [evet/hayır] |
| EPDK lisans belgesi | [evet/hayır] |
| Insurance programme | [evet/hayır] |

## Adım 1 — Yapı analizi

- **Borçlu yapısı:** SPV mi, doğrudan müvekkil mi, JV şirketi mi?
- **Borç/öz kaynak oranı:** D/E ratio — müvekkil / büroin risk eşiği
- **Borç türü:** Proje finansmanı (non-recourse) / kurumsal kredi (recourse) / karma
- **Kredi verenler:** Ticari banka konsorsiyumu / DFI (EBRD, IFC, AIIB) / tahvil / karma
- **Para birimi:** USD / EUR / TL / karma — döviz riski hedge

## Adım 2 — Conditions Precedent tarama

Kritik CP'ler:
- EPDK lisans alındı mı ve finansman için ön koşul mu?
- Halka açık müvekkil varsa KAP bildirimi tamamlandı mı?
- Çevre/ÇED izni finalize edildi mi?
- Temel sözleşmeler (EPC, O&M, offtake) imzalandı mı?
- Yatırımcı onayları (board resolution, shareholders') alındı mı?
- Sigortalar yerleştirildi mi?

Her eksik CP: `[review]` + finansal kapanış engelleyici mi tespit et.

## Adım 3 — Temel finansman şartları incelemesi

Facility Agreement'dan çıkar:
- **Faiz:** SOFR/EURIBOR + margin, PIK var mı
- **Taahhüt ücreti + düzenleme ücreti**
- **Geri ödeme profili:** sculpting mi, bullet mu, balloon mı
- **DSCR covenant:** minimum, test periyodu
- **Kısıtlayıcı taahhütler:** capex limit, dividend lock-up, change of control
- **Cross-default / cross-acceleration** — diğer müvekkil borç belgelerini etkiler mi?
- **Temerrüt olayları:** material adverse change (MAC) tanımı dar mı?

## Adım 4 — Teminat (security package) analizi

- İpotek: taşınmaz, makine-teçhizat
- Temlik: proje gelirleri, sigorta poliçeleri, sözleşmeler
- Rehin: SPV hisseleri, banka hesapları
- Kefalet: müvekkil / ana ortak garantisi — recourse seviyesi nedir?
- Türk hukukunda tescil: Tapu Sicili / Ticaret Sicili kayıtlı mı?

## Adım 5 — EPDK & SPK bildirim kontrolü

- **EPDK:** Lisans devri veya değişikliği gerektiriyor mu? Üretim/iletim/dağıtım lisans türü — kapasite ve sahiplik eşikleri. Rehber: `${CLAUDE_PLUGIN_ROOT}/references/epdk-rehberi.md`.
- **SPK/KAP:** Müvekkil veya iştiraki halka açıksa — önemli ilişkili taraf işlemi, maddi gelişme bildirimi. Rehber: `${CLAUDE_PLUGIN_ROOT}/references/kap-esirket-webfetch-rehberi.md`.
- **Yabancı yatırımcı:** FEFTA (Japonya), FIRPA (ABD) — DFI kredi verenlerin uyum yükümlülüğü.

## Adım 6 — Risk matrisi

🔴 Bloklayıcı: CP eksik + kapanış tarihi kısa / recourse covenant ihlali / EPDK lisans bekliyor
🟠 Yüksek: MAC tanımı geniş / dividend lock-up çok uzun / cross-default riski
🟡 Orta: Margin yüksek ama piyasa normunda / minor CP
🟢 Düşük: İdari, standart

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# Proje Finansmanı İncelemesi — [Proje adı / tarih]

## ⚠️ Reviewer note
- Belgeler: [okunanlar, atlanlar]
- CP durumu: N/M tamamlandı
- Flagged: N [review]

## Bottom line (2 cümle)

## Yapı özeti

## CP tarama tablosu

## Temel finansman şartları

## Teminat analizi

## EPDK/SPK bildirim durumu

## Risk matrisi

## Önerilen adımlar
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
