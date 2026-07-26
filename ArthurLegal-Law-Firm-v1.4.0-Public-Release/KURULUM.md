# ArthurLegal Hukuk Bürosu Asistanı — Kurulum Rehberi

**Versiyon:** 1.4.0 | **Güncelleme:** 2026-07-26

---

## Gereksinimler

| Gereksinim | Açıklama |
|---|---|
| Claude.ai hesabı | Pro veya Team plan (Projects özelliği için) |
| TR Legal MCP | yargi-mcp-pro connector (isteğe bağlı ama önerilir) |
| e-qanun / LexScholar / ResourceContracts MCP | self-hosted, auth yok (isteğe bağlı — Adım 4b) |
| OpenSanctions API key | Yaptırım taraması için (isteğe bağlı) |

---

## Adım 1 — Claude.ai Project oluşturun

1. [claude.ai](https://claude.ai) → **Projects** → **New Project**
2. Projeye bir isim verin (örn. "Büro Asistanı")

---

## Adım 2 — System Prompt yükleyin

1. Project → **Customize** → **Custom Instructions**
2. `SYSTEM_PROMPT.md` dosyasının içeriğini **tamamını** kopyalayıp yapıştırın
3. **Save** edin

---

## Adım 3 — Knowledge dosyalarını yükleyin

Project → **Add Content** → **Upload Files**

Aşağıdaki dosyaları **bu sırayla** yükleyin:

### Önce — Ana profil (zorunlu)
```
knowledge/firm-profile.md
```

### Sonra — Pratik alan profilleri
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
knowledge/profiles/legal-research.md          ← kaynak katmanı (v1.4.0)
```

### Yeni pratik alanlar (v1.2.0)
```
knowledge/profiles/privacy-legal.md       ← KVKK / veri koruma
knowledge/profiles/regulatory-legal.md    ← Regülasyon / düzenleyici
```

### Skill dosyaları (tüm plugin'ler)
```
knowledge/skills/administrative-legal__skills.md
knowledge/skills/advocacy-legal__skills.md
knowledge/skills/contract-drafting__skills.md
knowledge/skills/expert-opinion__skills.md
knowledge/skills/legal-research__skills.md          ← kaynak katmanı (v1.4.0)
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

### Agent tanımları (isteğe bağlı — otomatik görevler için)
```
knowledge/agents/commercial-legal__deal-debrief.md
knowledge/agents/commercial-legal__playbook-monitor.md
knowledge/agents/commercial-legal__renewal-watcher.md
knowledge/agents/corporate-legal__dataroom-watcher.md
knowledge/agents/employment-legal__leave-tracker.md
knowledge/agents/ip-legal__ip-renewal-watcher.md
knowledge/agents/regulatory-legal__reg-change-monitor.md
```

### Reference rehberleri (ihtiyaca göre seçin)

**Türk hukuku temel referanslar (önerilir):**
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
knowledge/references/mesleki-sir-rehberi.md
knowledge/references/karsilastirmali-hukuk-rehberi.md
```

**Kaynak katmanı MCP rehberleri (v1.4.0 — Adım 4b'yi kurduysanız):**
```
knowledge/references/eqanun-mcp-rehberi.md          ← AZ mevzuatı (BİRİNCİL)
knowledge/references/lex-scholar-rehberi.md         ← akademik doktrin + DergiPark (İKİNCİL)
knowledge/references/resourcecontracts-rehberi.md   ← imzalı PSA/JOA emsali (EMSAL)
```

**Sektöre göre ek referanslar:**
```
knowledge/references/epdk-rehberi.md          ← Enerji sektörü
knowledge/references/smk-rehberi.md           ← Fikri sınai haklar
knowledge/references/turkpatent-rehberi.md    ← Marka/patent
knowledge/references/istac-rehberi.md         ← Tahkim
knowledge/references/transfer-pricing-rehberi.md ← Transfer fiyatlandırması
knowledge/references/damga-vergisi-rehberi.md ← Vergi
knowledge/references/isg-dava-rehberi.md      ← İş güvenliği davaları
knowledge/references/seveso-buyuk-kaza-rehberi.md ← Büyük endüstriyel kaza
```

**Uluslararası yargı çevreleri (müvekkil portföyüne göre):**
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
knowledge/references/russia-legislation-rehberi.md  ← Yalnız KYC/yaptırım
knowledge/references/karsilastirmali-hukuk-rehberi.md
```

> **⚠️ Not:** Claude.ai Projects knowledge dosyası limitlerine dikkat edin. Önce temel referansları yükleyin, ihtiyaç halinde ek referanslar ekleyin.

---

## Adım 4 — TR Legal MCP bağlantısı (önerilir)

1. Project → **Customize** → **Connectors** → **Add MCP Server**
2. Bağlantı bilgileri:
   - **URL:** `https://yargi-mcp-pro-production.up.railway.app/mcp`
   - **Auth:** OAuth 2.0 (WorkOS) — bağlantı kurulurken yetkilendirme ekranı açılır
3. Bağlantı başarılı olduğunda 40+ TR mevzuat + yargı aracı aktif olur

---

## Adım 4b — Üç yeni MCP (v1.4.0) — kaynak katmanı (isteğe bağlı)

Üçü de **self-hosted, auth'suz** Streamable HTTP MCP sunucusudur. Sunucuları
kendiniz çalıştırırsınız; sonra her biri için:

Project → **Customize** → **Connectors** → **Add custom connector** →
*Name* + *URL* → Auth bölümünü **boş bırakın** (No authentication).

| # | Name | URL | Rol | Rehber |
|---|---|---|---|---|
| 1 | `e-qanun` | `https://<HOST>/mcp` | **AZ mevzuatı — BİRİNCİL**, yürürlük statüsü doğrulamalı (6 araç) | `eqanun-mcp-rehberi.md` |
| 2 | `LexScholar` | `https://<HOST>/mcp` | 10 indeks hukuk doktrini (**DergiPark 19 TR hukuk dergisi dâhil**) — İKİNCİL (6 araç) | `lex-scholar-rehberi.md` |
| 3 | `ResourceContracts` | `https://<HOST>/mcp` | 5.125 imzalı PSA/JOA — EMSAL (9 araç) | `resourcecontracts-rehberi.md` |

**Sunucu kaynakları:** `github.com/beerbottle90/eqanun-api` ·
`github.com/beerbottle90/lex-scholar-api` ·
`github.com/beerbottle90/resourcecontracts-api`
(umbrella: `github.com/beerbottle90/socar-api-s`)

**Yerel portlar (varsayılan):** e-qanun `8020` · LexScholar `8010` ·
ResourceContracts `8000`.

> ⚠️ **Host geçici tünelse** (`*.trycloudflare.com`) adres her yeniden
> başlatmada değişir → connector URL'sini güncellemeniz gerekir. Kalıcı kullanım
> için adlandırılmış tünel veya sabit deploy kullanın.

> ⚠️ **Araç adı çakışması:** aynı projede iki connector aynı araç adını
> taşımamalı — istemci şemaları karıştırıp `_2` sonekli araçlar üretir ve
> çağrılar 400 ile düşer.

> ⚠️ **Av. K. m. 36:** üçü de **public** arama aracıdır. Müvekkil adı, dosya
> numarası, dosya özeti veya gizli taslak **gönderilmez**; sorgu soyut hukuki
> kavram olur. Bkz. `mesleki-sir-rehberi.md`.

**Test:**
```
"Azerbaycan Əmək Məcəlləsi yürürlükte mi?"     → get_act, statusName dönmeli
"mücbir sebep uyarlama Türk doktrini"           → DergiPark kayıtları dönmeli
"Azerbaycan PSA'larında stabilizasyon klozu"    → search_contracts dönmeli
```

> **Kurulmazsa ne olur?** Paket çalışmaya devam eder: AZ mevzuatı
> `azerbaycan-hukuk-rehberi.md` WebFetch yoluna düşer (**statü doğrulanmaz**),
> doktrin ve sözleşme emsali kapsam dışı kalır — asistan bunu çıktısında belirtir.

---

## Adım 5 — OpenSanctions API (isteğe bağlı)

Yaptırım taraması ve KYC için:
1. [opensanctions.org](https://www.opensanctions.org/) → API key edinin
2. Claude.ai → Project Settings → **Environment Variables**
3. `OPENSANCTIONS_API_KEY` = `[API key]`

---

## Adım 6 — Büro profilini doldurun

İlk konuşmada şu komutu çalıştırın:

```
/firm-operations:cold-start-interview
```

Bu komut ~20-30 dakika sürer ve `knowledge/firm-profile.md` içindeki `[DOLDUR]` alanlarını interaktif olarak doldurur. **Tüm diğer plugin'ler bu profilden beslendiği için önce bunu çalıştırın.**

---

## Adım 7 — Pratik alan cold-start'larını çalıştırın

Her aktif pratik alan için:

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

Kullanmayacağınız pratik alanların cold-start'larını atlamanız sorun değil.

---

## Temel komutlar

| Komut | İşlev |
|---|---|
| `/firm-operations:new-client-intake` | Yeni müvekkil ön sohbet sonrası intake |
| `/firm-operations:conflict-check` | Çıkar çatışması taraması |
| `/commercial-legal:nda-review` | NDA inceleme |
| `/litigation-legal:case-intake` | Dava dosyası açma |
| `/criminal-defense:cmk-gorev-atama` | CMK atama yönetimi |
| `/<plugin>:cold-start-interview` | Plugin profilini doldurma |

Tüm mevcut komutları görmek için:
```
/<plugin>:
```
(Boş bırakın — asistan o plugin'in tüm skill'lerini listeler)

---

## Sık sorulan sorular

**S: `[DOLDUR]` alanlarını şimdi doldurmak zorunda mıyım?**
A: Hayır. Asistan `[DOLDUR]` gördüğünde sizi cold-start'a yönlendirir. Acil durumda doğrudan çalışmaya başlayabilirsiniz.

**S: Gerçek müvekkil isimlerini firm-profile.md'ye yazmam gerekiyor mu?**
A: HAYIR. Sadece agregat istatistik ve rumuz kullanın. Gerçek müvekkil bilgileri asla knowledge dosyasına yazılmamalıdır (KVKK + mesleki sır).

**S: Knowledge limiti aşılırsa ne yapmalıyım?**
A: Önce temel TR mevzuat referanslarını koruyun; uluslararası yargı referanslarını yalnızca ilgili matter'lar için geçici olarak ekleyip çıkarın.

**S: Asistan "Bu skill bu plugin'de yok" derse ne yapmalıyım?**
A: `/<plugin>:` yazın — asistan o plugin'in tüm mevcut skill'lerini listeler.

---

## Güncelleme notları

Bu versiyon **v1.2.0**'dır. Değişiklikler için `CHANGELOG.md` dosyasına bakın.

Destek ve geri bildirim: Projenin GitHub sayfasına issue açın.
