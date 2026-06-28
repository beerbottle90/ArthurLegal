# ArthurLegal — Claude Courthouse Assistant (TR)

**Sürüm:** v1.0.0 · **Tarih:** 2026-06-28 · **Lisans:** Apache 2.0
**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web)

> **v1.0.0 — 8/8 plugin kurulu** (her biri 2-5 skill, toplam 28 skill + 23 referans). Referansların tamamı yargısal/tarafsız çerçevede (müşteri-spesifik içerik temizlendi).

> Türk **yargı mensubu** (mahkeme hâkimleri + mahkeme kalem memurlukları) için **yargısal / tarafsız** decision-support asistanı. ArthurLegal Law-Firm / Corporate iskeletinden türetilmiştir; ancak konum **savunucu değil, yargısaldır**.

---

## Diğer ArthurLegal paketlerinden farkı

| | Corporate / Law-Firm | **Courthouse** |
|---|---|---|
| Kullanıcı | In-house ekip / hukuk bürosu | **Mahkeme hâkimi + kalem memurluğu** |
| Perspektif | Taraf vekili (savunucu) | **Yargısal / tarafsız** |
| Amaç | Müvekkil lehine taslak | **Gerekçe + usulü yapılandırma** |
| Atıf | Katı | **Sıfır-halüsinasyon (karara girecek)** |
| Üst başlık | GİZLİDİR – HUKUK MÜŞAVİRLİĞİ | **MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK** |

**Temel ilke:** Asistan asla karar vermez. İki tarafı dengeli analiz eder, gerekçe iskeleti ve usul kontrolü üretir; nihai değerlendirme **hâkim / heyet** tarafından yapılır.

---

## Mimari — 4 dal × 2 rol = 8 plugin

| Dal | Usul | Hâkim plugin | Kalem plugin |
|---|---|---|---|
| **Hukuk** | HMK 6100 | `hukuk-hakim` ✅ | `hukuk-kalem` ✅ |
| **Ceza** | CMK 5271 | `ceza-hakim` ✅ | `ceza-kalem` ✅ |
| **İdari** | İYUK 2577 | `idari-hakim` ✅ | `idari-kalem` ✅ |
| **Vergi** | VUK 213 + İYUK | `vergi-hakim` ✅ | `vergi-kalem` ✅ |

- **Hâkim plugin'leri:** gerekçeli karar/hüküm taslağı, delil değerlendirme metodu, içtihat-emsal tarama, usul kontrol.
- **Kalem plugin'leri:** tensip zaptı, müzekkere, tebligat (7201), duruşma tutanağı, harç/gider, UYAP iş akışı, süre/zamanaşımı takibi.
- **DRY:** Çapraz içerik (tarafsızlık/atıf disiplini, tebligat, harç) paylaşılan referans katmanında tutulur, her plugin oradan çağırır.

---

## MCP entegrasyonları

| Sunucu | Kapsam |
|---|---|
| **TR Legal MCP** (Mevzuat + Yargı) | TR mevzuat norm metni + Yargıtay/Danıştay/AYM + Bedesten/Emsal/UYAP içtihat |
| **CourtListener / OpenCaseLaw.ch** (ops.) | Karşılaştırmalı hukuk gerektiğinde ABD / İsviçre içtihadı |

Detay → `knowledge/references/yargi-mcp-rehberi.md`, `mevzuat-mcp-rehberi.md`.

---

## Kurulum

Tam rehber → [KURULUM.md](KURULUM.md). Özet: Claude.ai Project oluştur → `SYSTEM_PROMPT.md`'yi Custom Instructions'a yapıştır → `knowledge/` dosyalarını yükle.

---

## Paket içeriği

```
ArthurLegal-Courthouse-v1.0.0-Public-Release/
├── KURULUM.md             ← Kurulum rehberi (buradan başlayın)
├── SYSTEM_PROMPT.md       ← Claude.ai Custom Instructions metni
├── README.md              ← Bu dosya
├── CHANGELOG.md           ← Sürüm notları
├── VERSION.md             ← 1.0.0
├── ATTRIBUTION.md         ← Atıf bilgisi
├── LICENSE                ← Apache 2.0
└── knowledge/             ← Project Knowledge'a yüklenecek dosyalar
    ├── mahkeme-profili.md      (mahkeme profil şablonu — [DOLDUR])
    ├── skills/                 (8 plugin skill kitapçığı — 8/8, 28 skill)
    └── references/             (23 referans: 15 paylaşılan + 7 mahkeme-tarafı + 1 connector-sağlık)
```

---

## Sınırlamalar

- **Yargısal karar değildir.** Tüm çıktılar hâkim/heyet incelemesi öncesi **taslaktır**.
- **Mevzuat / içtihat değişebilir** — kritik karar öncesi UYAP / Resmi Gazete manuel doğrulama.
- v1.0.0: 8 plugin de kuruludur (her biri 2-5 skill, toplam 28); referansların tamamı yargısal çerçevede. Skill derinliği sonraki patch'lerde artırılacaktır.

---

## Lisans

Apache License 2.0 — bkz. [LICENSE](LICENSE). Atıf için → [ATTRIBUTION.md](ATTRIBUTION.md).
