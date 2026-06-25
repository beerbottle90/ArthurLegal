# Claude.ai Projects – Kurulum Rehberi

## ArthurLegal Corporate Assistant v1.2.0

Türk hukuku odaklı 10-eklenti kurumsal hukuk asistanı. Claude.ai Projects üzerinde çalışır.

**İçerik:** 10 birleşik skill dosyası · 42 referans (17 yargı çevresi) · 7 ajan · company-profile şablonu

---

## Adım 1 — Yeni Proje Oluştur

1. https://claude.ai/projects → **+ New Project**
2. **İsim:** `TR Legal Assistant` (veya şirketinize özel bir isim)
3. **Açıklama (opsiyonel):** "Türk hukuku odaklı in-house hukuk asistanı — 10 pratik alan, 17 yargı çevresi"

---

## Adım 2 — System Prompt'u Yapıştır

1. **Project → Settings → Custom Instructions**
2. `SYSTEM_PROMPT.md` dosyasının tüm içeriğini kopyalayıp yapıştırın
3. Save.

> Not: Custom instructions limiti ~32K karakter. SYSTEM_PROMPT.md ~5K — rahat sığar.

---

## Adım 3 — Knowledge Dosyalarını Yükle

`knowledge/` klasörünün altında **~60 dosya** var (4 kategori):

```
knowledge/
  skills/      ← 10 dosya (birleşik skill kitapçıkları)
  references/  ← 42 dosya (TR mevzuat + 17 yargı çevresi rehberleri)
  agents/      ← 7 dosya (periyodik ajan tanımları)
  company-profile.md
```

> ⚠️ **Claude.ai Projects yükleme kısıtlaması:** Tüm dosyaları tek seferde sürüklemek
> çalışmıyor. **Klasör başına bir toplu sürükleme** yapın.

### Yükleme adımları

Project → **+ Add content** → **Files** ekranını açık tutun.

1. `knowledge/skills/` klasörünü aç → `Ctrl+A` (10 dosya) → sürükle → bekle
2. `knowledge/references/` klasörünü aç → `Ctrl+A` (42 dosya) → sürükle → bekle
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
| 🇦🇿 Azerbaycan | Yok | `azerbaycan-hukuk-rehberi.md` |
| 🇨🇳 Çin (HuggingFace/twang2218) | Yok | `cin-hukuku-rehberi.md` |
| 🇷🇸 Sırbistan (paragraf.rs) | Yok | `sirbistan-hukuku-rehberi.md` |
| 🇨🇿 Çek Cumhuriyeti | OAuth (Sbírka MCP) | `cek-hukuku-rehberi.md` |

**Çek Cumhuriyeti için Sbírka MCP connector:**
- URL: `sbirka-mcp.fastmcp.app/mcp`
- Adım 4'teki gibi ekle.

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

---

## Sınırlamalar (Claude Code'a Kıyasla)

| Özellik | Claude Code | Claude.ai Projects |
|---|---|---|
| `/<plugin>:<skill>` slash command | ✓ resmi | ⚠ simüle (system prompt anlar) |
| **TR Legal MCP** (mevzuat + yargı) | ✓ `.mcp.json` | ✓ custom connector |
| **OpenCaseLaw.ch MCP** | ✓ `.mcp.json` | ✓ custom connector |
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

*ArthurLegal Corporate Assistant v1.2.0 — https://github.com/beerbottle90/ArthurLegal*
