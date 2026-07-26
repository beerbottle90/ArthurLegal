# Claude.ai Projects – Kurulum Rehberi

## ArthurLegal Corporate Assistant v1.4.0

Türk hukuku odaklı 12-eklenti kurumsal hukuk asistanı. Claude.ai Projects üzerinde çalışır.

**İçerik:** 12 birleşik skill dosyası · 47 referans (17 yargı çevresi) · 7 ajan · company-profile şablonu
**MCP sunucusu:** 5 — TR Legal · OpenCaseLaw.ch · **e-qanun** 🆕 · **LexScholar** 🆕 · **ResourceContracts** 🆕

---

## Adım 1 — Yeni Proje Oluştur

1. https://claude.ai/projects → **+ New Project**
2. **İsim:** `TR Legal Assistant` (veya şirketinize özel bir isim)
3. **Açıklama (opsiyonel):** "Türk hukuku odaklı in-house hukuk asistanı — 12 pratik alan, 17 yargı çevresi, 5 MCP"

---

## Adım 2 — System Prompt'u Yapıştır

1. **Project → Settings → Custom Instructions**
2. `SYSTEM_PROMPT.md` dosyasının tüm içeriğini kopyalayıp yapıştırın
3. Save.

> Not: Custom instructions limiti ~32.000 karakter. v1.4.0 SYSTEM_PROMPT.md
> **29.246 karakter** (limitin ~%91'i) — sığar, ancak **marj dardır**. Kendi
> kurumunuza özel kural eklerseniz önce karakter sayısını ölçün; taşarsa
> `Sınır-ötesi connector'lar` tablosunu çıkarın (aynı atıf biçimleri
> `Atıf disiplini` maddesinde zaten var).

---

## Adım 3 — Knowledge Dosyalarını Yükle

`knowledge/` klasörünün altında **~67 dosya** var (4 kategori):

```
knowledge/
  skills/      ← 12 dosya (birleşik skill kitapçıkları — legal-research dâhil)
  references/  ← 47 dosya (TR mevzuat + 17 yargı çevresi + 3 yeni MCP rehberi)
  agents/      ← 7 dosya (periyodik ajan tanımları)
  company-profile.md
```

> ⚠️ **Claude.ai Projects yükleme kısıtlaması:** Tüm dosyaları tek seferde sürüklemek
> çalışmıyor. **Klasör başına bir toplu sürükleme** yapın.

### Yükleme adımları

Project → **+ Add content** → **Files** ekranını açık tutun.

1. `knowledge/skills/` klasörünü aç → `Ctrl+A` (12 dosya) → sürükle → bekle
2. `knowledge/references/` klasörünü aç → `Ctrl+A` (47 dosya) → sürükle → bekle
3. `knowledge/agents/` klasörünü aç → `Ctrl+A` (7 dosya) → sürükle → bekle
4. `knowledge/company-profile.md`'yi ayrıca sürükle

> **İpucu:** Her yüklemeden sonra dosyaların listede göründüğünü teyit et.
> Boyut limiti aşılırsa yalnızca kullandığın pratik alanın skill dosyasını yükle.

---

## Adım 4 — TR Legal MCP Connector Ekle (mevzuat + yargı)

Tek birleşik MCP sunucusu — **yargi-mcp-pro** — hem mevzuat hem yargı araçlarını sağlar.

1. **Customize → Connectors → + Add custom connector**
2. **Name:** `TR Legal MCP`
3. **URL:** `https://yargi-mcp-pro-production.up.railway.app/mcp`
4. **Add** → WorkOS izin sayfasında giriş yap / hesap oluştur

**Test:**
```
"TBK m. 6'yı getir"               → mevzuat aracı dönmeli
"Yargıtay 9. HD iş kazası kararı"  → yargı aracı dönmeli
```

---

## Adım 4b — OpenCaseLaw.ch MCP — İsviçre İçtihadı (isteğe bağlı)

Swiss OR sözleşmeleri, ICC/Swiss tahkim kararları için.

1. **Customize → Connectors → + Add custom connector**
2. **Name:** `OpenCaseLaw.ch`
3. **URL:** `https://mcp.opencaselaw.ch/sse`
4. Auth bölümünü **boş bırak** (auth yok)

**Kapsam:** 972K+ BGer/BVGer/26 kanton kararı, Fedlex mevzuatı (CC0).

---

## Adım 4c — 17 Yargı Çevresi (connector gerektirmez)

Aşağıdaki yargı çevreleri WebFetch veya doğrudan API ile otomatik çalışır:

| Yargı | Auth | Rehber |
|---|---|---|
| 🇬🇧 UK | Yok | `uk-legislation-rehberi.md` |
| 🇺🇸 US Mevzuat | Ücretsiz API key | `us-legislation-rehberi.md` |
| 🇺🇸 US İçtihat (CourtListener) | Yok | `courtlistener-rehberi.md` |
| 🇪🇺 AB/EU + CJEU + ECHR | Yok | `eu-legislation-rehberi.md` |
| 🇩🇪 Almanya | Yok | `germany-legislation-rehberi.md` |
| 🇫🇷 Fransa | Yok | `france-legislation-rehberi.md` |
| 🇮🇹 İtalya | Yok | `italy-legislation-rehberi.md` |
| 🇯🇵 Japonya | Yok | `japan-legislation-rehberi.md` |
| 🇨🇭 İsviçre Mevzuat (Fedlex) | Yok | `switzerland-caselaw-rehberi.md` |
| 🇷🇺 Rusya ⚠️ (yalnız yaptırım/KYC) | Yok | `russia-legislation-rehberi.md` |
| 🇦🇿 Azerbaycan (içtihat/EN — mevzuat için Adım 4d) | Yok | `azerbaycan-hukuk-rehberi.md` |
| 🇨🇳 Çin (HuggingFace/twang2218) | Yok | `cin-hukuku-rehberi.md` |
| 🇷🇸 Sırbistan (paragraf.rs) | Yok | `sirbistan-hukuku-rehberi.md` |
| 🇨🇿 Çek Cumhuriyeti | OAuth (Sbírka MCP) | `cek-hukuku-rehberi.md` |

**Çek Cumhuriyeti için Sbírka MCP connector:**
- URL: `sbirka-mcp.fastmcp.app/mcp`
- Adım 4'teki gibi ekle.

---

## Adım 4d — Üç yeni MCP (v1.4.0) — kaynak katmanı

Üçü de **self-hosted, auth'suz** Streamable HTTP MCP sunucusudur. Sunucuları
kendiniz çalıştırırsınız; sonra her biri için:

**Customize → Connectors → + Add custom connector** → *Name* + *URL* → Auth
bölümünü **boş bırak** (No authentication).

| # | Name | URL | Rol | Rehber |
|---|---|---|---|---|
| 1 | `e-qanun` | `https://<HOST>/mcp` | **AZ mevzuatı — BİRİNCİL**, yürürlük statüsü doğrulamalı | `eqanun-mcp-rehberi.md` |
| 2 | `LexScholar` | `https://<HOST>/mcp` | 10 indeks hukuk doktrini (**DergiPark 19 TR hukuk dergisi dâhil**) — İKİNCİL | `lex-scholar-rehberi.md` |
| 3 | `ResourceContracts` | `https://<HOST>/mcp` | 5.125 imzalı PSA/JOA — EMSAL/BENCHMARK | `resourcecontracts-rehberi.md` |

**Sunucu kaynakları (MIT/self-host):**
`github.com/beerbottle90/eqanun-api` · `github.com/beerbottle90/lex-scholar-api`
· `github.com/beerbottle90/resourcecontracts-api`
(umbrella: `github.com/beerbottle90/socar-api-s`)

**Yerel portlar (varsayılan):** e-qanun `8020` · LexScholar `8010` ·
ResourceContracts `8000`. Her sunucu kendi portunda çalışır; aynı porta ikinci
sunucu başlatmak açıkça hata verir.

> ⚠️ **Host geçici tünelse** (`*.trycloudflare.com`) adres **her yeniden
> başlatmada değişir** → connector URL'sini güncellemeniz gerekir. Kalıcı
> kullanım için adlandırılmış Cloudflare tüneli veya sabit bir deploy kullanın.

> ⚠️ **Araç adı çakışması:** aynı projede iki connector aynı araç adını
> taşımamalı — istemci şemaları karıştırıp `_2` sonekli araçlar üretir ve
> çağrılar 400 ile düşer. Yeni connector eklerken araç adlarını mevcutlarla
> karşılaştırın.

**Test:**
```
"Azerbaycan Əmək Məcəlləsi yürürlükte mi?"        → get_act, statusName dönmeli
"mücbir sebep uyarlama Türk doktrini"              → DergiPark kayıtları dönmeli
"Azerbaycan'daki PSA'larda stabilizasyon klozu"    → search_contracts dönmeli
```

> **Bu üçü isteğe bağlıdır.** Kurulmazsa paket çalışmaya devam eder; AZ mevzuatı
> `azerbaycan-hukuk-rehberi.md` WebFetch yoluna düşer (statü doğrulanmaz),
> doktrin ve sözleşme emsali ise kapsam dışı kalır — asistan bunu çıktıda
> belirtir.

---

## Adım 5 — company-profile.md'yi Doldur

`knowledge/company-profile.md` dosyasındaki `[DOLDUR]` alanlarını şirketinize özgü bilgilerle tamamlayın:

1. Dosyayı bir metin editöründe açın
2. `[DOLDUR]` etiketli tüm alanları gerçek bilgilerle değiştirin
3. Eski dosyayı projeden silin → güncellenmiş dosyayı yeniden yükleyin

**Alternatif:** Proje chat'inde `/<plugin>:cold-start-interview` yazarak asistanın soruları size yönlendirmesini ve yanıtları company-profile formatına dönüştürmesini sağlayabilirsiniz.

> ⚠️ Gerçek şirket verilerini bu klasörün GitHub kopyasına eklemeyin — sadece yerel kullanım için doldurun.

---

## Adım 6 — İlk Komutu Dene

```
/commercial-legal:nda-review

[NDA metnini yapıştır veya yükle]
```

veya doğrudan:
```
SaaS sözleşmesi inceleyeceğim, vendor olarak biz, customer Avrupa'dan.
Limitation of liability ve KVKK maddelerine odaklan.
```

---

## Kullanılabilir Plugin'ler ve Skill'ler

Her plugin için `knowledge/skills/<plugin>__skills.md` dosyasını açıp `## Icindekiler` bölümüne bakın.

| Plugin | Örnek skill'ler |
|---|---|
| `commercial-legal` | `nda-review`, `governing-law-review`, `saas-msa-review`, `vendor-agreement-review` |
| `corporate-legal` | `closing-checklist`, `board-minutes`, `diligence-issue-extraction`, `tabular-review` |
| `employment-legal` | `internal-investigation`, `termination-review`, `international-expansion`, `leave-tracker` |
| `privacy-legal` | `dsar-response`, `pia-generation`, `dpa-review`, `reg-gap-analysis` |
| `regulatory-legal` | `reg-feed-watcher`, `gap-surfacer`, `policy-diff`, `comments` |
| `ip-legal` | `cease-desist`, `clearance`, `fto-triage`, `portfolio` |
| `litigation-legal` | `isg-incident-response`, `outside-counsel-brief`, `case-intake`, `settlement-eval` |
| `tax-legal` | `tax-litigation-prep`, `kdv-otv-iade-review`, `transfer-pricing-review`, `gib-ozelge-request` |
| `administrative-legal` | `ced-itiraz`, `epdk-proaktif-gorus`, `idari-dava-prep` |
| `energy-finance` | `project-finance-review`, `ma-diligence-energy`, `jv-agreement-review`, `lng-offtake-review` |
| `contract-drafting` | `redline-contract`, `belge-turet`, `versiyon-karsilastir`, `tadil-protokol` |
| `legal-research` **(YENİ)** | `kaynak-secimi`, `az-mevzuat`, `karsilastirmali-doktrin`, `sozlesme-emsali` |

---

## Sınırlamalar (Claude Code'a Kıyasla)

| Özellik | Claude Code | Claude.ai Projects |
|---|---|---|
| `/<plugin>:<skill>` slash command | ✓ resmi | ⚠ simüle (system prompt anlar) |
| **TR Legal MCP** (mevzuat + yargı) | ✓ `.mcp.json` | ✓ custom connector |
| **OpenCaseLaw.ch MCP** | ✓ `.mcp.json` | ✓ custom connector |
| **e-qanun / LexScholar / ResourceContracts MCP** | ✓ `.mcp.json` | ✓ custom connector (auth yok) |
| Araç çağrısı zaman aşımı | uzun | **100 saniye — sabit** |
| Tüm WebFetch kaynakları | ✓ | ✓ |
| Hook'lar (pre/post tool) | ✓ | ✗ |
| Local dosya okuma | ✓ | Drive connector + upload |
| Memory persist (matter workspaces) | ✓ | Sınırlı — knowledge statik |

---

## Güncelleme

Yeni bir sürüm geldiğinde:

1. Değişen dosyaları yerel olarak güncelleyin
2. Claude.ai projesinde ilgili dosyaları silin → güncellenmiş halleri yeniden yükleyin
3. `SYSTEM_PROMPT.md` değiştiyse Custom Instructions'ı güncelleyin

---

*ArthurLegal Corporate Assistant v1.4.0 — https://github.com/beerbottle90/ArthurLegal*
