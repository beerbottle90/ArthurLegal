# ArthurLegal — Claude Corporate Legal Assistant (TR)

**Sürüm:** v1.4.0 · **Tarih:** 26.07.2026 · **Lisans:** Proprietary — Non-Commercial (bkz. [LICENSE](LICENSE))
**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web)

> Türk hukukuna ve kurumsal in-house pratiğine adapte edilmiş, **Claude tabanlı hibrit hukuk asistanı paketi**. Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiştir.
>
> *A Turkish-law adaptation of Anthropic's [claude-for-legal](https://github.com/anthropics/claude-for-legal) — packaged as a Claude.ai Projects bundle (SYSTEM_PROMPT + 67 knowledge files, 5 MCP servers) for in-house corporate legal teams.*

---

## Ne işe yarar?

Türkiye'de bir in-house hukuk ekibinin gündelik üretim akışı için **avukat incelemesi öncesi taslak çıktılar** üretir: NDA triage, M&A diligence, KVKK DSAR cevabı, İSG runbook, idari dava ön-değerlendirme, marka clearance, haftalık regülasyon digest, transfer pricing kontrol notu, vergi davası akışı, sınır-ötesi yargı çevresi analizi vb.

Çıktılar daima **taslaktır** ve avukat onayı gerektirir; paket bunu sıkı atıf disiplini ile zorlar (`[Mevzuat MCP - tarih]`, `[Yargı MCP - kurum - tarih]`, `[model bilgisi - doğrulayın]`).

---

## 12 pratik alan

> **v1.4.0 yeni:** `legal-research` (kaynak katmanı) + üç MCP rehberi — `eqanun-mcp-rehberi.md`, `lex-scholar-rehberi.md`, `resourcecontracts-rehberi.md`.
> **v1.3.0:** `contract-drafting` (sözleşme üretimi & redline) + `rekabet-hukuku-rehberi.md` + `redline-konvansiyonlari-rehberi.md`.

| Plugin | Kapsam |
|---|---|
| `commercial-legal` | TBK + TTK + damga vergisi + KEP + ISTAC; NDA GREEN/YELLOW/RED triage; **sınır-ötesi yargı çevresi analizi** |
| `corporate-legal` | TTK 134-209, Rekabet Kurulu 2010/4, SPK, VERBİS; M&A diligence; tabular review |
| `employment-legal` | 4857, 5510, 6356, 6331; iç soruşturma, fesih, uluslararası genişleme |
| `privacy-legal` | 6698 KVKK + GDPR ikili rejim, m. 9 yurt dışı 2024 rejimi, DSAR 30 gün |
| `regulatory-legal` | Resmi Gazete + EPDK/BDDK/SPK/KGK + CBK haftalık digest |
| `ip-legal` | 6769 SMK, TÜRKPATENT, 5651 + 5846 FSEK; marka clearance, UDRP |
| `litigation-legal` | HMK + UYAP + İSG runbook (0-1/0-24/0-72 saat); TTK m. 5/A ön-kontrol; dış vekil koordinasyon |
| `tax-legal` | VUK 213, KVK 5520 (TP), KDVK 3065, ÖTV 4760, GİB özelge; Mali İşler-Hukuk koordinasyon |
| `administrative-legal` | İYUK 2577 (idare 60 g / vergi 30 g + m. 20/A ÇED ivedi); 3 dereceli idari yargı; EPDK proaktif dialog |
| `energy-finance` | Enerji M&A · proje finansmanı · JV · LNG offtake; CAATSA/sanctions; cross-border (JP/EU/AZ/CN) |
| `contract-drafting` | Sözleşme belgesi üretimi & redline: incele→belgeye uygula, emsalden türet, versiyon karşılaştır (track-changes diff), tadil/süre uzatımı |
| `legal-research` **(YENİ)** | Kaynak katmanı — AZ mevzuatı (e-qanun MCP, statü doğrulamalı) · akademik doktrin (LexScholar, DergiPark dâhil) · imzalı PSA/JOA emsali (ResourceContracts) |

Detaylı içerik için → [CHANGELOG.md](CHANGELOG.md).

---

## MCP entegrasyonları & 17 Yargı Çevresi

| Sunucu | URL | Auth | Kapsam |
|---|---|---|---|
| **TR Legal MCP** (birleşik) | `yargi-mcp-pro-production.up.railway.app/mcp` | OAuth (WorkOS) | TR mevzuat norm metinleri + yargı/idari kararlar (15 kurum) — tek connector |
| **OpenCaseLaw.ch MCP** | `mcp.opencaselaw.ch/sse` | Yok | İsviçre 972K+ karar + Fedlex mevzuatı (CC0) |
| **e-qanun MCP** 🆕 | self-host `/mcp` | Yok | AZ mevzuatı — resmî `api.e-qanun.az`, **yürürlük statüsü doğrulamalı** (BİRİNCİL) |
| **LexScholar MCP** 🆕 | self-host `/mcp` | Yok | 10 açık erişim indeksi federe — DOAJ · SciELO · HAL · Dialnet · OpenAIRE · Law Review Commons · OpenAlex · Crossref · Unpaywall · **DergiPark (19 TR hukuk dergisi)** (İKİNCİL) |
| **ResourceContracts MCP** 🆕 | self-host `/mcp` | Yok | 5.125 imzalı petrol & madencilik sözleşmesi, 107 ülke + uzman kloz anotasyonları (EMSAL) |
| **OpenSanctions** | `api.opensanctions.org` | API key | Yaptırım/PEP taraması (paid membership) |
| **KAP + e-ŞİRKET** | `kap.org.tr`, `e-sirket.mkk.com.tr` | Yok | BIST açıklamaları (WebFetch) |

**WebFetch ile çalışan yargı çevreleri** (ek connector gerekmez): 🇬🇧 UK · 🇺🇸 US (mevzuat + CourtListener içtihat) · 🇪🇺 AB/CJEU/ECHR · 🇩🇪 DE · 🇫🇷 FR · 🇮🇹 IT · 🇯🇵 JP · 🇷🇺 RU · 🇨🇳 CN · 🇷🇸 SR · 🇨🇿 CZ (Sbírka MCP) · 🇦🇿 AZ *(içtihat + EN kaynaklar; mevzuat artık e-qanun MCP'de)*

TR Legal MCP, [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan public MCP sunucusudur. Üç yeni MCP **self-hosted ve auth'suz**; kurulumu **isteğe bağlıdır** — kurulmazsa paket çalışmaya devam eder, asistan kapsam daralmasını çıktısında belirtir.

---

## Kurulum — 5 adım, ~15 dakika

Tam rehber için → [KURULUM.md](KURULUM.md).

1. **Yeni Claude.ai Project oluşturun** — [claude.ai/projects](https://claude.ai/projects) → "+ New Project".
2. **`SYSTEM_PROMPT.md`** içeriğini Custom Instructions alanına yapıştırın.
3. **`knowledge/`** klasöründeki ~67 dosyayı Project Knowledge'a yükleyin (klasör başına toplu sürükle-bırak).
4. **TR Legal MCP connector ekleyin** — URL: `https://yargi-mcp-pro-production.up.railway.app/mcp` (WorkOS OAuth). İsteğe bağlı: e-qanun · LexScholar · ResourceContracts (auth yok — KURULUM.md Adım 4d).
5. **`knowledge/company-profile.md`** dosyasındaki `[DOLDUR]` yer-tutucularını kendi kurumunuza göre doldurun — ya da `/<plugin>:cold-start-interview` ile asistana yaptırın.

---

## İlk kullanım örnekleri

```text
/commercial-legal:nda-review
[NDA metnini yapıştır]
```
→ TBK 115 sorumsuzluk, damga vergisi, yaptırım taraması, GREEN/YELLOW/RED triage.

```text
/commercial-legal:governing-law-review
[Sözleşmeyi yükle - yabancı governing law seç]
```
→ 17 yargı çevresinde MÖHUK 5718 + NY Konvansiyonu analizi.

```text
/privacy-legal:dsar-response
[DSAR başvurusunu yapıştır]
```
→ 30 gün takvimi, KVKK m. 28 istisna kontrolü, Türkçe cevap taslağı.

```text
/litigation-legal:isg-incident-response
[Olay özetini yaz]
```
→ 0-1 / 0-24 / 0-72 saat fazlı runbook; ceza + tazminat + idari üçlü-paralel risk.

```text
/energy-finance:project-finance-review
[Finansman belgelerini yükle]
```
→ Proje finansmanı yapı analizi; take-or-pay, CAATSA/sanctions, EPDK lisans devri.

```text
/legal-research:az-mevzuat
Azerbaycan Əmək Məcəlləsi'nde ihbar süresi ne?
```
→ `search_acts` → **`get_act` ile statü doğrulaması** (`Qüvvədədir`/`Ləğv olunmuş`) → madde metni; statü atıfın içinde.

```text
/legal-research:sozlesme-emsali
Cost recovery tavanımız %50. Piyasa ne?
```
→ İmzalı PSA emsalleri + uzman kloz anotasyonları → piyasa/agresif/muhafazakâr değerlendirmesi.

```text
/legal-research:karsilastirmali-doktrin
Mücbir sebep TR, FR ve BR'de nasıl ele alınıyor?
```
→ Her yargı çevresi kendi dilindeki terimle aranır (`mücbir sebep` / `force majeure` / `caso fortuito`); DergiPark + HAL + SciELO.

Tüm komutlar için yeni konuşmada sadece `/<plugin>:` yazın — Claude o plugin'in skill listesini gösterir.

---

## Paket içeriği

```
ArthurLegal-CorporateAssistant-v1.4.0-Public-Release/
├── KURULUM.md             ← Kurulum rehberi (buradan başlayın)
├── SYSTEM_PROMPT.md       ← Claude.ai Custom Instructions metni
├── README.md              ← Bu dosya
├── CHANGELOG.md           ← Sürüm notları
├── VERSION.md             ← 1.4.0
├── ATTRIBUTION.md         ← Atıf bilgisi
├── LICENSE                ← Proprietary — Non-Commercial
└── knowledge/             ← Project Knowledge'a yüklenecek 67 dosya
    ├── company-profile.md       (kurum profil şablonu — [DOLDUR] ile gelir)
    ├── skills/                  (12 birleşik skill kitapçığı, birer dosya per plugin)
    ├── references/              (47 referans: TR mevzuat + 17 yargı çevresi + 3 MCP rehberi)
    └── agents/                  (7 periyodik ajan tanımı)
```

---

## Sınırlamalar

- **Hukuki tavsiye değildir.** Tüm çıktılar avukat incelemesi öncesi taslaktır.
- **Mevzuat / içtihat değişebilir** — kritik karar öncesi UYAP / Lexpera / Resmi Gazete manuel doğrulama.
- **Araç çağrıları 100 saniyede iptal edilir** ve iptal edilen çağrı hiçbir şey döndürmez. Sorgular dar tutulur; kapsam daraldıysa asistan bunu söyler.
- **Doktrin ve sözleşme emsali ikincil/karşılaştırmalıdır** — bir hukuki sonucun dayanağı olamaz. Hakemlilik üç durumludur (`true`/`false`/`null`); ABD law review'ları öğrenci editörlüdür.
- **Üç yeni MCP public arama aracıdır** — gizli taslak, müzakere pozisyonu veya kişisel veri gönderilmez.
- Hook'lar, CLM entegrasyonu ve matter persistence Claude.ai Projects'te yoktur (Claude Code ile mevcuttur).

---

## Kişisel veri uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket verisi içermez**. `knowledge/company-profile.md` tamamen `[DOLDUR]` yer-tutucularından oluşan bir şablondur. Paketi kendi kurumunuza uyarladığınızda doldurduğunuz veriler **sizin kontrolünüzdedir** — public repoya commit etmeden önce gözden geçirin.

---

## Atıf

- **Author** (kod & içerik üretimi): Claude (Anthropic)
- **Knowledge base**: Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)

Detay için → [ATTRIBUTION.md](ATTRIBUTION.md).

---

## Lisans

Bu paket **bir bütün olarak** ArthurLegal Proprietary Non-Commercial License
kapsamındadır — bkz. [LICENSE](LICENSE). **Ticari kullanım yasaktır.** In-house
counsel'ın, hukuk bürosu çalışanının ve gerçek kişinin kişisel kullanımı ile bu
kullanımlar için bizzat yapılan veya üçüncü kişiye yaptırılan geliştirmeler ticari
kullanım sayılmaz. Tüm hakları saklıdır.

Paketin türetildiği üçüncü taraf bilgi tabanı (Anthropic `claude-for-legal`)
**Apache License 2.0** altındadır. İlgili lisans ve atıf bildirimi
[LICENSE-APACHE-2.0-THIRD-PARTY.txt](LICENSE-APACHE-2.0-THIRD-PARTY.txt) dosyasında
korunmuştur ve kaldırılamaz. Çelişki hâlinde, o bileşenler bakımından Apache 2.0
geçerlidir.
