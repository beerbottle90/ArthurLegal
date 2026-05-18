# ArthurLegal — Claude Law Firm Assistant (TR)

**Sürüm:** v1.0.0 — Initial Public Release · **Tarih:** 17.05.2026 · **Lisans:** Apache 2.0
**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web)

> Türk hukukuna ve **danışman tarafı (hukuk bürosu)** pratiğine adapte edilmiş, **Claude tabanlı hibrit hukuk asistanı paketi**. Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiştir.
>
> *A Turkish-law adaptation of Anthropic's [claude-for-legal](https://github.com/anthropics/claude-for-legal) — packaged as a Claude.ai Projects bundle (SYSTEM_PROMPT + ~60 knowledge files) for small-to-mid (0–30 staff) law firms practicing balanced litigation + advisory work.*

> Kardeş paket: [ArthurLegal Claude Corporate Assistant](../ArthurLegal-v1.0.0-Public-Release/) — in-house (danışan) tarafı. Aynı metodoloji, farklı hedef kullanıcı.

---

## Ne işe yarar?

0–30 çalışanlı, **dava + danışmanlık dengeli** Türk hukuk bürosunun gündelik üretim akışı için **atanan avukat incelemesi öncesi taslak çıktılar** üretir: müvekkil intake + conflict check, CMK görevli atama yönetimi, vergi davası süre kontrolü, NDA GREEN/YELLOW/RED triage, fesih değerlendirmesi, marka clearance, GK/YK karar paketi, ücret sözleşmesi, AAÜT hesabı vb.

Çıktılar daima **taslaktır** ve **atanan ortak / Yönetici Ortak onayı** gerektirir. Paket bunu sıkı atıf disiplini ile zorlar (`[Mevzuat MCP — tarih]`, `[Yargı MCP — kurum — tarih]`, `[model bilgisi — doğrulayın]`).

**Çıkış başlığı:** `AVUKATLIK K. m. 36 – VEKİL-MÜVEKKİL YAZIŞMASI – DAHİLİ VE GİZLİDİR – [Matter ID]`

---

## "Danışan → Danışman" farkı (Corporate paketten)

| Konu | Corporate (in-house) | Law Firm (büro) |
|---|---|---|
| Profil dosyası | `company-profile.md` | **`firm-profile.md`** + müvekkil portföyü agregat |
| Müvekkil yönetimi | Tek "kendi şirketim" | **Çok-müvekkilli matter workspace + zorunlu conflict check** |
| Dış vekil | Panel yönetilir | **Kendisi dış vekil** (panel yerine muhabir avukat ağı) |
| Mesleki sır | KVKK + ticari sır + Av. K. m. 36 sınırlı | **Av. K. m. 36 tam koruma + TBB Meslek Kuralları + CMK m. 130** |
| Ücret | İç bütçe satırı | **AAÜT + Av. K. m. 164 + KDV/Stopaj/Damga** ana iş kalemi |
| Eskalasyon | CLCO → CEO → YK | **Atanan Ortak → Yönetici Ortak → Ortaklar Kurulu** |
| Çıktı üst başlığı | `HUKUK MÜŞAVİRLİĞİ DAHİLİ` | `AVUKATLIK K. m. 36 – VEKİL-MÜVEKKİL YAZIŞMASI – Matter ID` |

---

## 9 pratik alan

| Plugin | Kapsam |
|---|---|
| **`dispute-litigation`** | HMK 6100 + UYAP + AAÜT; TTK m. 5/A zorunlu arabuluculuk ön-kontrol; ticari + adli yargı; ISTAC/ICC tahkim klozu |
| **`administrative-litigation`** | İYUK 2577 + 3 dereceli idari yargı (İdare Mh → BİM → Danıştay); ÇED m. 20/A ivedi; EPDK/BDDK/SPK/KVKK/Rekabet/KİK kararlarına dava |
| **`tax-litigation`** | VUK 213 + İYUK m. 7 (**30 g vergi davası kritik**); uzlaşma vs. dava matrisi; Danıştay 3/4/7/9. Daire; KDV iade, mukteza |
| **`criminal-defense`** | CMK 5271 + TCK 5237 + Av. K. m. 35; **CMK görevli atama** (48 saat), müdafiilik, müdahil vekilliği, uzlaştırma, AYM bireysel |
| **`commercial-advisory`** | TBK + TTK sözleşme **yazma + inceleme**; NDA, hizmet, distribütörlük, lisans, JV; damga + KEP + ISTAC; ihtarname |
| **`corporate-advisory`** | KOBİ + aile şirketi (TTK GK/YK, pay devri, esas sözleşme, sermaye, küçük M&A, kurumsallaşma) |
| **`employment-advisory`** | 4857 + 5510 + 6356 + 6331; **işveren + işçi** dual taraf vekillik; fesih + işe iade + alacak hesabı + mobbing; iş davası arabuluculuk dava şartı |
| **`ip-advisory`** | 6769 SMK + TÜRKPATENT + Madrid; marka clearance + tescil + YİDK itiraz + ihtarname + UDRP; 5651 + 5846 FSEK |
| **`firm-operations`** | **Büro işletim ekseni**: müvekkil intake + conflict check + MASAK + sanctions + KVKK + fee agreement + vekalet + baro koordinasyonu + aylık matter bazlı fatura |

Detaylı içerik için → [CHANGELOG.md](CHANGELOG.md).

---

## MCP entegrasyonları

| Sunucu | URL | Auth | Kapsam |
|---|---|---|---|
| **Mevzuat MCP** | `mevzuat.surucu.dev/mcp` | Yok | TR mevzuat norm metinleri — 26 araç |
| **Yargı MCP** | `yargimcp.surucu.dev/mcp` | Yok | TR yargı/idari kararlar — 24 araç, 15 kurum |
| **OpenSanctions** | `api.opensanctions.org` | API key | Müvekkil due diligence (paid membership) |
| **UYAP + KEP** | `uyap.gov.tr`, KEP sağlayıcı | Kullanıcı oturumu | E-tebligat, dosya takip, KEP yazışma |

Mevzuat MCP ve Yargı MCP, [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan public MCP sunucularıdır.

---

## Kurulum — 4 adım, ~10 dakika

Tam rehber için → [KULLANIM-REHBERI.md](KULLANIM-REHBERI.md).

1. **Yeni Claude.ai Project oluşturun** — [claude.ai/projects](https://claude.ai/projects) → "+ New Project".
2. **`SYSTEM_PROMPT.md`** içeriğini Custom Instructions alanına yapıştırın.
3. **`knowledge/`** klasöründeki ~60 dosyayı Project Knowledge'a sürükle-bırak ile yükleyin.
4. **`knowledge/firm-profile.md`** ve `profiles/*.md` dosyalarındaki `[DOLDUR]` yer-tutucularını kendi büronuza göre özelleştirin (opsiyonel — atlanabilir).

---

## İlk kullanım örnekleri

```text
/firm-operations:new-client-intake
[Müvekkil ön sohbet özetini yaz]
```
→ Bilgi toplama + matter tipi tespit + 7-adımlı zorunlu zincir (conflict / MASAK / sanctions / KVKK / fee / vekalet / matter-open) tetiklenir.

```text
/firm-operations:conflict-check
[Müvekkil + karşı yan bilgisi]
```
→ Av. K. m. 38 + TBB MK m. 35-36 üç eksen tarama: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ.

```text
/dispute-litigation:case-intake
[Dava materyali]
```
→ HMK yargı yeri, husumet, zamanaşımı, TTK m. 5/A arabuluculuk kontrol, Yargı MCP emsal.

```text
/criminal-defense:cmk-gorev-atama
[Baro atama mesajı]
```
→ 48 saat akış, susma hakkı hatırlatma, ifade hazırlık, tutukluluk değerlendirme, CMK ödeme cetveli.

```text
/tax-litigation:vergi-davasi-prep
[İhbarname]
```
→ **30 g süre kritik kontrol**, uzlaşma vs. dava matrisi, Danıştay vergi dairesi tespiti.

```text
/commercial-advisory:draft-nda
[Karşı yan NDA taslağı]
```
→ TBK 115 sorumsuzluk şartı kontrolü, damga vergisi, KEP teslim, GREEN/YELLOW/RED triage.

Tüm komutlar için yeni konuşmada sadece `/<plugin>:` yazın — Claude o plugin'in skill listesini gösterir.

---

## Paket içeriği

```
ArthurLegal-Law-Firm-v1.0.0-Public-Release/
├── README.md                  ← Bu dosya
├── KULLANIM-REHBERI.md        ← Detaylı kurulum & kullanım
├── SYSTEM_PROMPT.md           ← Claude.ai Custom Instructions metni
├── knowledge/                 ← Project Knowledge'a yüklenecek dosyalar (~60)
│   ├── firm-profile.md        (büro profil şablonu)
│   ├── profiles/              (9 plugin profili)
│   ├── references/            (33 TR mevzuat + meslek pratiği referansı)
│   └── skills/                (19 adım-adım iş yöntemi — flat naming)
├── ATTRIBUTION.md             ← Author / Designer / Knowledge atfı
├── LICENSE                    ← Apache 2.0
└── CHANGELOG.md               ← Sürüm notları
```

**Toplam knowledge dosyası: 62** | **Paket boyutu: ~350 KB**.

---

## Hukuk bürosuna özel referanslar (yeni — Corporate paketten)

`knowledge/references/` altında 9 hukuk bürosu spesifik referans:

| Dosya | İçerik |
|---|---|
| `aaut-rehberi.md` | Avukatlık Asgari Ücret Tarifesi — uygulama + başarı bonusu %25 sınırı |
| `vekalet-uyap-rehberi.md` | Vekalet türleri + HMK m. 74 özel yetki + UYAP'a sunum + azil/istifa |
| `mesleki-sir-rehberi.md` | Av. K. m. 36 + TBB MK m. 36-37 + CMK m. 130 + KVKK uyumu |
| `conflict-check-rehberi.md` | Av. K. m. 38 + TBB MK m. 35-36 + ethical wall + yazılı rıza |
| `cmk-gorevli-rehberi.md` | CMK görevli atama + 48 saat + ödeme cetveli + TBB CMK tarifesi |
| `baro-islemleri-rehberi.md` | Levha kayıt + yıllık aidat + sicil + disiplin işlemler |
| `ucret-sozlesmesi-rehberi.md` | Ücret sözleşmesi şart + KDV + stopaj + damga + tahsil yolları |
| `kep-etebligat-rehberi.md` | KEP + e-Tebligat 5. gün kuralı + KEP ihtarname pratiği |
| `masak-kimlik-tespit-rehberi.md` | Tebliğ 5 yükümlülükleri + UBO + tipping-off yasağı |

+ 24 ortak referans (Corporate paket ile aynı): HMK, UYAP, İYUK, Mevzuat/Yargı MCP, kanun kısaltmalar, SMK, TÜRKPATENT, ISTAC, damga vergisi, OpenSanctions, ÇED, EPDK, transfer pricing, vd.

---

## Sınırlamalar

- **Hukuki tavsiye değildir.** Tüm çıktılar **atanan ortak / Yönetici Ortak** incelemesi öncesi taslaktır.
- **Mesleki sorumluluk** yine avukatındır; baroya kayıtlı **imzalı** belge olmadan müvekkile/mahkemeye sunulamaz.
- **Mevzuat / içtihat değişebilir** — kritik karar öncesi UYAP / Lexpera / Resmi Gazete manuel doğrulama.
- **Conflict check otomatik** ama Av. K. m. 38'in nüansları **insan yargısı** ister; otomatik tarama eşik filter görevi görür.
- **CMK görevli atama** baro CMK servisi üzerinden gelir — paket sadece sonrasını yönetir.
- **Aile/miras + denizcilik + enerji ihtisas** kapsam dışı — başka uzmana yönlendirme önerisi otomatik flag.

---

## Kişisel veri uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket/müvekkil verisi içermez**. Tüm gerçek-kişi isimleri rol-bazlı yer-tutucularla (`[Yönetici Ortak]`, `[Kıdemli Ortak A]`, `[Müvekkil rumuz]`, `[KOBİ Üretici]` vb.) değiştirilmiştir. Büro örneği (`ArthurLegal Hukuk Bürosu`) tamamen kurgusaldır.

⚠️ **Av. K. m. 36 hatırlatma:** Paketi kendi büronuza uyarladığınızda müvekkil bilgisini şablonlara yazmadan önce iki kez düşünün; matter klasörlerini **cross-matter izoleli** tutun (Müvekkil A'nın bilgisi Müvekkil B'nin dosyasına asla sızmamalı). Paylaşmadan önce gözden geçirin.

---

## Atıf

- **Author** (kod & içerik üretimi): Claude (Anthropic) — Opus 4.7 (`claude-opus-4-7`)
- **Designer** (proje tasarımı & domain bilgisi): Ertuğ Demir
- **Knowledge base**: Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)
- **Kardeş paket**: ArthurLegal Claude Corporate Assistant v1.0.0 (in-house, danışan tarafı)

Detay için → [ATTRIBUTION.md](ATTRIBUTION.md).

---

## Lisans

Apache License 2.0 — bkz. [LICENSE](LICENSE). Serbest kullanım, değiştirme ve dağıtım hakkı verir; orijinal atıf ve lisans bildirimi korunmalıdır.
