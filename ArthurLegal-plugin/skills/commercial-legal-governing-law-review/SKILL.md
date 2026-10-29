---
name: commercial-legal-governing-law-review
description: >
  Cross-border mega-skill: Sözleşmeden yargı çevrelerini otomatik tespit eder,
  karşı taraf ülke bazlı risk profili çeker (resmî yaptırım listeleri + ülke rehberi),
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
TR bağlantısı  : [[Müvekkil] taraf — Türk hukuku iş hukuku + vergi uygulanır]
```

**Uyarı — çoklu yargı çevresi tetikleyici:**
Governing law ≠ arbitration seat ≠ counterparty ülkesi ise 🟠 flag koy. Her katman ayrı risk ve Adım 4'te ayrı analiz gerektirir.

---

## Adım 2 — büro-default karşılaştırması

CLAUDE.md `Governing law and venue` ile karşılaştır. Severity:

| Durum | Severity |
|---|---|
| Tercih listesinde (İngiliz/Türk + ICC/LCIA/ISTAC) | 🟢 |
| Tercih dışı ama kabul edilebilir (Fransız, İsviçre OR + ICC) | 🟡 |
| Asimetrik venue — tek tarafa mahkeme seçim hakkı | 🟠 |
| Karanlık yargı çevresi (belirsiz devlet hukuku, kısıtlı mahkeme erişimi) | 🔴 |
| Rusya, İran, OFAC yaptırım altındaki ülke mahkemesi | 🔴 — dur, [Uyum Direktörü]'e sor |

---

## Adım 3 — Karşı taraf ülke risk profili

Karşı tarafın ülkesine göre iki paralel kontrol:

### 3a. Yaptırım taraması
Karşı taraf tüzel kişiyi resmî yaptırım listelerinde tara (`yaptirim-tarama-rehberi.md`).
Eşleşme varsa → Adım 3b'ye geçme, dur ve [Uyum Direktörü]'e eskalasyon öner.

### 3b. Ülke bazlı mevzuat kontrol
Karşı tarafın hukuku governing law değilse bile taraf yükümlülükleri yerel mevzuata tabi olabilir. İlgili rehberi oku ve gerekirse WebFetch ile bağımlı kanunu çek:

| Karşı taraf ülkesi | Rehber | Kritik kontrol |
|---|---|---|
| 🇬🇧 İngiltere | `uk-legislation-rehberi.md` | Arbitration Act 1996, UCTA 1977 s.3 |
| 🇺🇸 ABD | `us-legislation-rehberi.md (bu eklentide yok: kullanıcı API anahtarı ister)` + `courtlistener-rehberi.md` | CISG opt-out, UCC Art.2, FAA §2 |
| 🇩🇪 Almanya | `germany-legislation-rehberi.md` | BGB §307 standart şart denetimi, HGB |
| 🇫🇷 Fransa | `france-legislation-rehberi.md` | Code civil m.1171 (haksız şart), m.1442 |
| 🇨🇭 İsviçre | `switzerland-caselaw-rehberi.md` | IPRG m.178 tahkim sözleşmesi, OR m.19 |
| 🇮🇹 İtalya | `italy-legislation-rehberi.md` | Codice Civile, D.Lgs. 231/2001 |
| 🇯🇵 Japonya | `japan-legislation-rehberi.md` | Companies Act, FEFTA (yabancı taraf ise) |
| 🇳🇱 Hollanda | **`nl-rechtspraak-mcp-rehberi.md`** | BW Boek 6 (borçlar), Boek 2 (şirketler) — holding yapılarının varsayılan yargı çevresi |
| 🇵🇱 Polonya | **`pl-sejm-mcp-rehberi.md`** | Kodeks cywilny, KSH; **akt statüsü** (`obowiązujący`) atıfın parçası |
| 🇦🇹 Avusturya | **`at-ris-mcp-rehberi.md`** | ABGB, AktG/GmbHG; Konkurrenzklausel için OGH içtihadı |
| 🇮🇪 İrlanda | **`ie-statutebook-mcp-rehberi.md`** | Companies Act 2014; AB içi common law forumu |
| 🇫🇮 Finlandiya | **`fi-finlex-mcp-rehberi.md`** | Osakeyhtiölaki; iki resmî dil eşit yetkili |
| 🇪🇸 İspanya | **`es-boe-mcp-rehberi.md`** | Código Civil, LSC; LNG terminal erişimi (Ley 34/1998) |
| 🇪🇺 AB şirketi | `eu-legislation-rehberi.md` | GDPR, AI Act, NIS2 uyum yükümlülüğü |
| 🇦🇿 Azerbaycan | ArthurLegal MCP (`az_`) + model | Azerbaycan hukuku — özel dikkat |

Çekilen kanunlara `[DE Mevzuat — ...]` / `[UK Legislation — ...]` vb. atıf koy.
Çekemediğin hukuku `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>` etiketle.

---

## Adım 4 — İcra-edilebilirlik: governing law connector teyidi

**Governing law**'u fiilen çek:
- İngiliz hukuku → `uk-legislation-rehberi.md` → `legislation.gov.uk` WebFetch
- ABD hukuku → `us-legislation-rehberi.md (bu eklentide yok: kullanıcı API anahtarı ister)` + `courtlistener-rehberi.md` → citation verification zorunlu
- Alman hukuku → **de-eli MCP** (`de-eli-mcp-rehberi.md`) ⚠️ `gesetze-im-internet.de` bu ortamdan **erişilemez**; MCP kendi egress'inden çeker
- Hollanda hukuku → **nl-rechtspraak MCP** (`nl-rechtspraak-mcp-rehberi.md`) ⚠️ içtihat resmî API'den kelimeyle **aranamaz**
- Polonya hukuku → **pl-sejm MCP** (`pl-sejm-mcp-rehberi.md`) — statü + değişiklik grafiği
- Avusturya hukuku → **at-ris MCP** (`at-ris-mcp-rehberi.md`) ⚠️ Rechtssatz karar değildir
- İrlanda hukuku → **ie-statutebook MCP** (`ie-statutebook-mcp-rehberi.md`) ⚠️ varsayılan metin *as enacted*
- Finlandiya hukuku → **fi-finlex MCP** (`fi-finlex-mcp-rehberi.md`) ⚠️ `statute` ≠ `statute-consolidated`
- İspanya hukuku → **es-boe MCP** (`es-boe-mcp-rehberi.md`) ⚠️ konsolide ≠ yayımlandığı hâl
- Fransız hukuku → `france-legislation-rehberi.md` → Légifrance
- İsviçre hukuku → `switzerland-caselaw-rehberi.md` → OpenCaseLaw.ch MCP + Fedlex
- AB hukuku → `eu-legislation-rehberi.md` → EUR-Lex CELEX
- Türk hukuku → ArthurLegal MCP (`tr_`) (MÖHUK m.24 — hukuk seçimi)

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
NY Konvansiyonu Madde V ret gerekçeleri (m.62 kapıları):
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

Katman 4 — Türkiye ([Müvekkil] taraf):
  → İcra ayağı: MÖHUK 5718 / NY Konvansiyonu [Adım 5]
  → Bağlantı noktaları: iş hukuku, vergi, EPDK lisans
```

Çakışma riski: iki governing law aynı anda uygulanabilirse ya da çelişen zorunlu kurallar (mandatory rules) varsa 🔴 flag + `[review]`.

---

## Adım 7 — Severity özeti ve memo

| Kriter | Severity |
|---|---|
| Yaptırım listesi eşleşmesi | 🔴 dur |
| Rusya/İran/OFAC mahkemesi | 🔴 |
| Çakışan mandatory rules | 🔴 |
| MÖHUK tenfiz engeli yüksek | 🔴 |
| Asimetrik venue / tek taraflı seçim | 🟠 |
| Çoklu yargı çevresi — her biri kontrol edildi | 🟡 |
| büro-default dışı ama kabul edilebilir | 🟡 |
| Tercih listesinde | 🟢 |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# Cross-Border Yargı & İcra Analizi — [Sözleşme adı]

## ⚠️ Reviewer note
- **Kaynaklar:** [ArthurLegal MCP (`tr_`) / UK / DE / FR / CH / EU / CourtListener — hangileri çekildi]
- **Governing law:** [...] | **Seat:** [...] | **Karşı taraf ülkesi:** [...]
- **Çoklu katman:** [evet/hayır — kaç katman]
- **Türkiye icra:** [MÜMKÜN / SORUNLU / BELİRSİZ]
- **[review] sayısı:** N

## Bottom line (2 cümle)

## Yargı çevresi haritası

## Karşı taraf risk profili (resmî yaptırım listeleri + ülke rehberi)

## İcra-edilebilirlik bulguları (connector atıflı)

## MÖHUK / NY Konvansiyonu icra analizi

## Çoklu katman özeti (varsa)

## Önerilen kloz / redline
```

CLAUDE.md `## Outputs` decision tree ile kapat. Yüksek riskli değişiklik counterparty'ye gitmeden önce avukat/GC onayı şart.

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
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/arthurlegal:legal-research-az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/arthurlegal:legal-research-sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
