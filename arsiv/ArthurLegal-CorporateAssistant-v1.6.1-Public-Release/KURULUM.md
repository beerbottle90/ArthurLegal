# Claude.ai Projects – Kurulum Rehberi

## ArthurLegal Corporate Assistant v1.4.0

Çok yargı çevreli (multi-jurisdiction) 12-eklenti kurumsal hukuk asistanı.
Claude.ai Projects üzerinde çalışır.

**İçerik:** 12 birleşik skill dosyası · 65 referans (22 yargı çevresi) · 7 ajan · company-profile şablonu
**MCP connector:** 5'e kadar — TR Legal · OpenCaseLaw.ch · **CourtListener** · **Fedlex** · **ArthurLegal** (tek uçta on yargı çevresi)
(TR Legal dışındakiler isteğe bağlıdır · ayrıca OpenSanctions REST API)

> **22 yargı çevresi** = 12 ulusal (TR · CH · US · AZ · UK · DE · FR · IT ·
> JP · RU · CN · RS) + 2 supranasyonel hukuk düzeni (AB/CJEU · ECHR).

---

## Adım 1 — Yeni Proje Oluştur

1. https://claude.ai/projects → **+ New Project**
2. **İsim:** `TR Legal Assistant` (veya şirketinize özel bir isim)
3. **Açıklama (opsiyonel):** "Multi-jurisdiction in-house hukuk asistanı — 12 pratik alan, 22 yargı çevresi, 7 MCP connector'a kadar"

---

## Adım 2 — System Prompt'u Yapıştır

1. **Project → Settings → Custom Instructions**
2. `SYSTEM_PROMPT.md` dosyasının tüm içeriğini kopyalayıp yapıştırın
3. Save.

> Not: Custom instructions limiti ~32K karakter. v1.4.0 SYSTEM_PROMPT.md **~27K** —
> sığar ama marj daralmıştır. Kendi eklemelerinizi yaparken karakter sayısını kontrol edin.

---

## Adım 3 — Knowledge Dosyalarını Yükle

`knowledge/` klasörünün altında **~67 dosya** var (4 kategori):

```
knowledge/
  skills/      ← 12 dosya (birleşik skill kitapçıkları — legal-research dâhil)
  references/  ← 65 dosya (TR mevzuat + 22 yargı çevresi + 3 yeni MCP rehberi)
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

## Adım 4b — Ek MCP connector'ları (isteğe bağlı)

Üç ayrı connector: İsviçre içtihadı + İsviçre mevzuatı + ABD içtihadı.

### 4b-1 · OpenCaseLaw.ch — İsviçre İçtihadı

Swiss OR sözleşmeleri, ICC/Swiss tahkim kararları için.

1. **Customize → Connectors → + Add custom connector**
2. **Name:** `OpenCaseLaw.ch`
3. **URL:** `https://mcp.opencaselaw.ch/sse`
4. Auth bölümünü **boş bırak** (auth yok)

**Kapsam:** 972K+ BGer/BVGer/26 kanton kararı, Fedlex mevzuat entegrasyonu (CC0).

### 4b-2 · CourtListener — ABD İçtihadı

**Resmi MCP sunucusu vardır ve Anthropic connector dizininde listelidir** —
custom connector eklemek gerekmez:

1. **Customize → Connectors → Browse Connectors**
2. Listeden **CourtListener**'ı seç → **Add**
3. CourtListener hesabına yetki ver — **OAuth 2.0** (Dynamic Client Registration;
   ön-kayıt ve API anahtarı gerekmez)

**Kapsam:** ABD federal/eyalet mahkeme kararları, PACER dosyaları, atıf ağı,
sözlü duruşma kayıtları ve **citation verification**. Free Law Project işletir.

> ⚠️ **Citation verification zorunludur.** Bir ABD kararına atıf yapılacaksa önce
> CourtListener'da doğrulanır (karar var mı, citation doğru mu, overrule edilmiş
> mi). Doğrulanmayan karar `[model bilgisi — doğrulayın]` ile işaretlenir, asla
> `[CourtListener]` etiketi almaz. Ayrıntı: `courtlistener-rehberi.md`.

### 4b-3 · Fedlex — İsviçre Mevzuatı

Verbatim madde metni ve değişiklik geçmişi için; Anthropic connector dizininde:

1. **Customize → Connectors → Browse Connectors**
2. Listeden **Fedlex**'i seç → **Add**

**Kapsam:** İsviçre federal mevzuatı — madde metni, kanun tam metni, değişiklik
listesi, başlığa göre arama. Tahkim ve Swiss OR işlerinde madde metninin
verbatim gerekmesi hâlinde OpenCaseLaw.ch entegrasyonuna göre daha doğrudandır.

> Connector kurulmazsa Fedlex WebFetch ile de çalışır (`fedlex.admin.ch`) —
> bkz. `switzerland-caselaw-rehberi.md`.

---

## Adım 4c — Connector gerektirmeyen yargı çevreleri

Aşağıdakiler WebFetch veya doğrudan API ile otomatik çalışır:

| Yargı | Auth | Rehber |
|---|---|---|
| 🇬🇧 UK | Yok | `uk-legislation-rehberi.md` |
| 🇺🇸 US Mevzuat (GovInfo) | Ücretsiz API key | `us-legislation-rehberi.md` |
| 🇪🇺 AB/EU + CJEU + ECHR | Yok | `eu-legislation-rehberi.md` |
| 🇩🇪 Almanya | Yok | `germany-legislation-rehberi.md` |
| 🇫🇷 Fransa | Yok | `france-legislation-rehberi.md` |
| 🇮🇹 İtalya | Yok | `italy-legislation-rehberi.md` |
| 🇯🇵 Japonya | Yok | `japan-legislation-rehberi.md` |
| 🇷🇺 Rusya ⚠️ (yalnız yaptırım/KYC) | Yok | `russia-legislation-rehberi.md` |
| 🇦🇿 Azerbaycan (içtihat/EN — mevzuat için Adım 4d) | Yok | `azerbaycan-hukuk-rehberi.md` |
| 🇨🇳 Çin (HuggingFace/twang2218) | Yok | `cin-hukuku-rehberi.md` |
| 🇷🇸 Sırbistan (paragraf.rs) | Yok | `sirbistan-hukuku-rehberi.md` |

> 🇺🇸 **ABD içtihadı bu tabloda değildir** — CourtListener MCP connector'ı ile
> gelir (Adım 4b-2). 🇨🇭 **İsviçre** de öyle: içtihat 4b-1, mevzuat 4b-3.

---

## Adım 4d — ArthurLegal MCP (tek connector, on yargı çevresi)

**Customize → Connectors → + Add custom connector**

| | |
|---|---|
| **Ad** | `arthurlegal` |
| **URL** | `https://arthurlegal-mcp.fly.dev/mcp` |
| **Auth** | **None** — kimlik doğrulama yok |

Bu tek uç, daha önce ayrı ayrı bağlanan **on sunucuyu** taşır (63 araç):

| Önek | Kapsam |
|---|---|
| `es_` | 🇪🇸 İspanya — BOE konsolide mevzuat (12.376 akt, indeksli) |
| `pl_` | 🇵🇱 Polonya — Dz.U. mevzuat (indeksli) |
| `nl_` | 🇳🇱 Hollanda — içtihat + mevzuat (KOOP tam metin araması) |
| `fi_` | 🇫🇮 Finlandiya — konsolide kanunlar (indeksli) |
| `ie_` | 🇮🇪 İrlanda — Acts of the Oireachtas (indeksli) |
| `at_` | 🇦🇹 Avusturya — RIS mevzuat + içtihat |
| `de_` | 🇩🇪 Almanya — federal mevzuat + BVerfG/BGH/BAG/BFH/BVerwG |
| `az_` | 🇦🇿 Azerbaycan — e-qanun, **yürürlük statüsü doğrulamalı** |
| `scholar_` | 🌍 Hukuk doktrini — 10 indeks, DergiPark dahil 19 Türk hukuk dergisi |
| `contracts_` | 🌍 5.125 imzalı PSA/JOA sözleşmesi |

> ⚠️ **Önek zorunlu.** Alttaki sunucularda `get_act` **beş ayrı şey** demek. Önek,
> İspanyol hukuku sorusunun Fin mevzuatıyla cevaplanmasını engelleyen tek şeydir.
> Araçları önekli adlarıyla çağır: `az_get_act`, `es_search_legislation`.

> ⚠️ **Kimlik doğrulama yok.** Adresi bilen herkes tüm araçları çağırabilir.
> Kamuya açık kaynaklarda arama yaparlar; şirket sırrı, müzakere pozisyonu veya
> gizli taslak **gönderilmez**.

**Kapsamı kendin doğrula.** `status` aracı her yargı çevresi için indeks
büyüklüğünü, `index_coverage` aralığını ve semantiğin açık olup olmadığını verir.
Bu önemli: bir kanun indekste yoksa arama **en yakın komşuyu** döndürür, "kapsam
dışı" demez.

**Test:**
```
"kişisel verilerin korunması" (İspanya)     → es_search_legislation, LO 15/1999 ve LO 7/2021 dönmeli
"Azerbaycan Əmək Məcəlləsi yürürlükte mi?"  → az_get_act, statusName dönmeli
"mücbir sebep uyarlama Türk doktrini"       → scholar_search_legal_scholarship, DergiPark kayıtları
"Azerbaycan PSA stabilizasyon klozu"        → contracts_search_contracts
```

**Kaynak:** `github.com/beerbottle90/arthurlegal-mcp` — Fly.io'da barındırılıyor,
indeksler image'a gömülü, semantik arama Voyage AI (`voyage-4-lite`) ile.

> **Kurulmazsa ne olur?** Paket çalışmaya devam eder: bu on yargı çevresi WebFetch
> yoluna düşer (AZ'de **statü doğrulanmaz**), doktrin ve sözleşme emsali kapsam
> dışı kalır — asistan bunu çıktısında belirtir.

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
| **ArthurLegal MCP** (on yargı çevresi, 63 araç) | ✓ `.mcp.json` | ✓ tek custom connector (auth yok) |
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
