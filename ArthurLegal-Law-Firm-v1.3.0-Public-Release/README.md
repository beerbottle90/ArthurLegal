# ArthurLegal — Claude Law Firm Assistant (TR)

**Sürüm:** v1.3.0 · **Tarih:** 2026-06-25 · **Lisans:** Apache 2.0
**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web)

> Türk hukukuna ve **danışman tarafı (hukuk bürosu)** pratiğine adapte edilmiş, **Claude tabanlı hibrit hukuk asistanı paketi**.
> Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiştir.
>
> *A Turkish-law adaptation of Anthropic's claude-for-legal — packaged as a Claude.ai Projects bundle (SYSTEM_PROMPT + 68+ knowledge files) for small-to-mid (0–30 staff) law firms.*

---

## Ne işe yarar?

0–30 çalışanlı, **dava + danışmanlık dengeli** Türk hukuk bürosunun gündelik üretim akışı için **atanan avukat incelemesi öncesi taslak çıktılar** üretir:

- Müvekkil intake + conflict check
- CMK görevli atama yönetimi (48 saat sınırı)
- Vergi davası süre kontrolü (30 gün kritik)
- NDA GREEN/YELLOW/RED triage
- Fesih değerlendirmesi ve iş davası arabuluculuk
- Marka clearance ve TÜRKPATENT itiraz
- KVKK DSAR yanıtı + DPIA
- Regülasyon takibi ve gap analizi
- GK/YK karar paketi, küçük M&A due diligence
- Enerji M&A, proje finansmanı, LNG offtake inceleme

Çıktılar daima **taslaktır** ve **atanan ortak / Yönetici Ortak onayı** gerektirir. Sıkı atıf disiplini zorunludur: `[Mevzuat MCP — tarih]`, `[Yargı MCP — kurum — tarih]`, `[model bilgisi — doğrulayın]`.

---

## v1.2.0 — Ne değişti?

| Alan | v1.0.1 | v1.2.0 |
|---|---|---|
| Plugin sayısı | 9 | **12** |
| Yeni pratik alanlar | — | privacy-legal, regulatory-legal, energy-finance |
| Skill formatı | Bireysel dosyalar | **Birleşik `__skills.md`** (daha kapsamlı) |
| Agents | Yok | **7 otomasyon agent'ı** |
| Yargı çevresi | TR | **17 yargı çevresi** (UK/US/AB/DE/FR/IT/JP/CH/RU/AZ/CN/SR/CZ) |
| Reference dosyası | 33 | **42+** |
| TR Legal MCP | Ayrı Mevzuat + Yargı MCP | **Birleşik yargi-mcp-pro** (OAuth) |
| Kurulum rehberi | KULLANIM-REHBERI.md | **KURULUM.md (TR) + INSTALLATION.md (EN)** |

---

## 15 pratik alan

> **v1.3.0 yeni:** `advocacy-legal` (dilekçe üretimi) · `expert-opinion` (bilirkişi/mütalaa) · `contract-drafting` (sözleşme redline) + rekabet/cmk/bilirkişilik/dilekçe-teknikleri referansları.

| Plugin | Kapsam |
|---|---|
| `commercial-legal` | NDA, MSA, SaaS, vendor; yaptırım taraması; governing law review |
| `corporate-legal` | M&A, board, due diligence, KAP |
| `employment-legal` | İş hukuku, internal investigation, TİS |
| `privacy-legal` | KVKK, DSAR, DPIA, DPA (**YENİ**) |
| `regulatory-legal` | Regülasyon takibi, EPDK/SPK/Rekabet (**YENİ**) |
| `ip-legal` | Marka/patent/tasarım, takedown, OSS |
| `litigation-legal` | HMK + UYAP + dava yönetimi |
| `tax-legal` | KVK + VUK + KDV/ÖTV + GİB + Danıştay vergi |
| `administrative-legal` | İdari yargı 3 dereceli + kurul kararları |
| `energy-finance` | Enerji M&A, proje finansmanı, JV, LNG offtake (**YENİ**) |
| `criminal-defense` | CMK zorunlu müdafi, özel müvekkil, mağdur müdahil |
| `firm-operations` | Müvekkil intake, conflict check, MASAK, KVKK |
| `advocacy-legal` **(YENİ)** | Dava dilekçesi üretimi (özel HMK / kamu İYUK+AYM / ceza CMK) + yazıhane asistanlığı |
| `expert-opinion` **(YENİ)** | Bilirkişi raporu + uzman mütalaası (HMK m.293); karşı rapora itiraz (m.281) |
| `contract-drafting` **(YENİ)** | Sözleşme üretimi & redline: incele→belgeye uygula, emsalden türet, versiyon karşılaştır, tadil |

---

## MCP entegrasyonları

| Sunucu | URL | Auth | Kapsam |
|---|---|---|---|
| **TR Legal MCP (yargi-mcp-pro)** | `yargi-mcp-pro-production.up.railway.app/mcp` | OAuth 2.0 | TR mevzuat + 15 kurum yargı/idari kararlar — 40+ araç |
| **OpenSanctions** | `api.opensanctions.org` | API key | Müvekkil sanctions/KYC taraması |
| **OpenCaseLaw.ch** | `mcp.opencaselaw.ch/sse` | Yok | İsviçre içtihadı — 33 araç |
| **Sbírka MCP** | — | OAuth | Çek mevzuatı + Anayasa Mah. |

---

## Kurulum — 7 adım

Türkçe rehber → [KURULUM.md](KURULUM.md)
English guide → [INSTALLATION.md](INSTALLATION.md)

**Özet:**
1. Claude.ai → Projects → New Project
2. `SYSTEM_PROMPT.md` → Custom Instructions
3. `knowledge/` klasörü → Upload Files
4. TR Legal MCP connector ekle
5. OpenSanctions API key (isteğe bağlı)
6. `/firm-operations:cold-start-interview` çalıştır
7. Pratik alan cold-start'larını çalıştır

---

## İlk kullanım örnekleri

```text
/firm-operations:new-client-intake
```
→ Intake + conflict + MASAK + KVKK + fee + vekalet zinciri tetiklenir.

```text
/firm-operations:conflict-check
[Müvekkil + karşı yan bilgisi]
```
→ Av. K. m. 38 + TBB MK m. 35-36: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ.

```text
/criminal-defense:cmk-gorev-atama
[Baro atama mesajı]
```
→ 48 saat akış, susma hakkı, CMK ödeme cetveli.

```text
/tax-legal:tax-litigation-prep
[İhbarname]
```
→ **30 g süre kritik kontrol**, uzlaşma vs. dava matrisi.

```text
/privacy-legal:dsar-response
[KVKK m. 11 başvurusu]
```
→ 30 gün yanıt süresi, cevap şablonu, VERBİS uyumu.

```text
/regulatory-legal:reg-feed-watcher
```
→ Haftalık regülasyon değişiklik özeti.

Tüm komutlar için: `/<plugin>:` yazın — asistan o plugin'in tüm skill listesini gösterir.

---

## Paket içeriği

```
ArthurLegal-Law-Firm-v1.3.0-Public-Release/
├── KURULUM.md              ← Türkçe kurulum rehberi
├── INSTALLATION.md         ← English installation guide
├── SYSTEM_PROMPT.md        ← Claude.ai Custom Instructions metni
├── README.md               ← Bu dosya
├── CHANGELOG.md            ← Sürüm notları
├── VERSION.md              ← Sürüm bilgisi
├── ATTRIBUTION.md          ← Atıf
├── LICENSE                 ← Apache 2.0
└── knowledge/
    ├── firm-profile.md     ← Büro profil şablonu ([DOLDUR] ile)
    ├── profiles/           ← 11 pratik alan profili
    ├── skills/             ← 12 birleşik skill dosyası
    ├── agents/             ← 7 otomasyon agent tanımı
    └── references/         ← 42+ TR mevzuat + uluslararası yargı rehberi
```

---

## Sınırlamalar

- **Hukuki tavsiye değildir.** Tüm çıktılar **Yönetici Ortak** incelemesi öncesi taslaktır.
- **Mesleki sorumluluk** avukatındır; baroya kayıtlı **imzalı** belge olmadan müvekkile/mahkemeye sunulamaz.
- **Mevzuat / içtihat değişebilir** — kritik karar öncesi UYAP / Lexpera / Resmi Gazete manuel doğrulama.
- **Conflict check otomatik** ama Av. K. m. 38 nüansları **insan yargısı** ister.
- **Aile/miras + özel denizcilik** kapsam dışı — başka uzmana yönlendirme önerilir.

---

## Kişisel veri uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket/müvekkil verisi içermez**. Tüm alanlar `[DOLDUR]` yer tutucuları ile işaretlenmiştir. Büro örneği (`ArthurLegal Hukuk Bürosu`) tamamen kurgusaldır.

⚠️ **Av. K. m. 36 hatırlatma:** Paketi kendi büronuza uyarladığınızda gerçek müvekkil bilgisini knowledge dosyalarına yazmayın. Matter klasörlerini **cross-matter izoleli** tutun.

---

## Atıf

- **Author** (içerik & kod üretimi): Claude (Anthropic) — Sonnet 4.6
- **Designer** (proje tasarımı & domain bilgisi): Ertuğ Demir
- **Knowledge base**: Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)

Detay → [ATTRIBUTION.md](ATTRIBUTION.md)

---

## Lisans

Apache License 2.0 — bkz. [LICENSE](LICENSE). Serbest kullanım, değiştirme ve dağıtım hakkı verir; orijinal atıf ve lisans bildirimi korunmalıdır.
