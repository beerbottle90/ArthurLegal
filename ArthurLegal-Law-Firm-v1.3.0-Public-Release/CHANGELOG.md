# Değişiklik Günlüğü

[Keep a Changelog](https://keepachangelog.com/tr-TR/1.1.0/) formatına uygundur.
Semver: [Semantic Versioning 2.0](https://semver.org/lang/tr/).

---

## [1.3.0] — 2026-06-25 — *Dilekçe Üretimi + Bilirkişi/Mütalaa + Sözleşme Redline + Rekabet*

### Eklendi

**3 yeni pratik alan (plugin):**
- `advocacy-legal` — dava dilekçesi üretimi + yazıhane asistanlığı: özel hukuk (HMK), kamu/idari (İYUK + AYM bireysel başvuru), ceza (CMK) dilekçeleri + süre/duruşma takvimi, dosya özeti, evrak/harç.
- `expert-opinion` — bilirkişi raporu + uzman mütalaası (HMK m.293 uzman görüşü): teknik rapor taslağı / karşı rapora itiraz (HMK m.281) + taraf lehine bilimsel/hukuki mütalaa.
- `contract-drafting` — sözleşme belgesi üretimi & redline: incele→belgeye uygula, emsalden türet, versiyon karşılaştır, tadil/süre uzatımı.

**5 yeni referans dosyası:**
- `rekabet-hukuku-rehberi.md` (4054 + birleşme eşikleri 2022 + Tebliğ 2010/4 + muafiyet + soruşturma/ceza + uzlaşma)
- `cmk-rehberi.md` (5271 CMK genel — süre/görev/dilekçe tipleri; mevcut `cmk-gorevli-rehberi`yi tamamlar)
- `bilirkisilik-rehberi.md` (6754 + HMK m.266-287/m.293 + CMK m.62-73)
- `dilekce-teknikleri-rehberi.md` (HMK m.119 / İYUK m.3 / CMK zorunlu unsurlar + iskelet + harç)
- `redline-konvansiyonlari-rehberi.md` (redline & comment standardı)

> Tüm içerik generic hukuk bürosu şablonu; kişisel veri / kurum-spesifik bilgi içermez.

---

## [1.2.0] — 2026-06-04 — *Multi-Jurisdiction Merge + 3 Yeni Pratik Alan*

v1.0.1 (Law Firm Public) + TR Legal Suite v1.8.3 (dist) birleştirmesi.
Tüm kişisel veri ve kurum-spesifik içerik temizlenmiş, generic hukuk bürosu şablonuna dönüştürülmüştür.

### Eklendi

**3 yeni pratik alan:**
- `privacy-legal` — KVKK, GDPR, DSAR (veri sahibi başvurusu), DPIA, DPA müzakeresi; cold-start + 7 skill
- `regulatory-legal` — Regülasyon takibi, gap analizi, EPDK/SPK/Rekabet; cold-start + 7 skill + `reg-change-monitor` agent
- `energy-finance` — Enerji M&A, proje finansmanı, JV, LNG offtake; cold-start + 4 skill

**7 otomasyon agent'ı** (`knowledge/agents/`):
- `commercial-legal__deal-debrief.md` — Deal sonrası özet
- `commercial-legal__playbook-monitor.md` — Playbook değişiklik takibi
- `commercial-legal__renewal-watcher.md` — Sözleşme yenileme alarmı (haftalık)
- `corporate-legal__dataroom-watcher.md` — VDR yeni belge bildirimi
- `employment-legal__leave-tracker.md` — İzin ve devamsızlık takibi
- `ip-legal__ip-renewal-watcher.md` — Marka/patent yenileme alarmı
- `regulatory-legal__reg-change-monitor.md` — Düzenleyici değişiklik izleme

**18 yeni yargı çevresi referansı** (`knowledge/references/`):
- `azerbaycan-hukuk-rehberi.md` — e-qanun.az + minenergy.gov.az + CODICES
- `cek-hukuku-rehberi.md` — Sbírka MCP (1848'den günümüze)
- `cin-hukuku-rehberi.md` — HuggingFace/twang2218 (22.552 kanun)
- `courtlistener-rehberi.md` — ABD federal içtihat REST API
- `eu-legislation-rehberi.md` — EUR-Lex CELEX + CJEU + ECHR/HUDOC
- `france-legislation-rehberi.md` — Légifrance WebFetch
- `germany-legislation-rehberi.md` — gesetze-im-internet.de / NeuRIS
- `italy-legislation-rehberi.md` — Normattiva WebFetch
- `japan-legislation-rehberi.md` — e-Gov API + JLT
- `karsilastirmali-hukuk-rehberi.md` — Karşılaştırmalı hukuk araştırma rehberi
- `reg-feed-haftalik-sablon.md` — Düzenleyici değişiklik haftalık şablon
- `russia-legislation-rehberi.md` — pravo.gov.ru / ЕГРЮЛ (yalnız KYC/yaptırım)
- `seveso-buyuk-kaza-rehberi.md` — Büyük endüstriyel kaza mevzuatı
- `sirbistan-hukuku-rehberi.md` — paragraf.rs WebFetch
- `switzerland-caselaw-rehberi.md` — OpenCaseLaw.ch MCP (33 araç)
- `uk-legislation-rehberi.md` — legislation.gov.uk data.xml
- `us-legislation-rehberi.md` — GovInfo REST
- `yargi-mcp-rehberi.md` — TR Legal MCP birleşik (yargi-mcp-pro)

**Skill kapsamı artırıldı** — Mevcut 9 pratik alan için v1.8.3 birleşik skill dosyaları:
- `administrative-legal__skills.md` (11 skill — idari dava, ÇED, EPDK proaktif görüş, vd.)
- `commercial-legal__skills.md` (13 skill — governing-law-review, amendment-history, vd.)
- `corporate-legal__skills.md` (11 skill — closing-checklist, dataroom-review, vd.)
- `employment-legal__skills.md` (16 skill — internal-investigation, leave-tracker, vd.)
- `ip-legal__skills.md` (12 skill — cease-desist, takedown, OSS audit, vd.)
- `litigation-legal__skills.md` (15 skill — outside-counsel-brief, case-intake, vd.)
- `tax-legal__skills.md` (7 skill — kdv-otv-iade-review, transfer-pricing-review, vd.)

**Kurulum dosyaları:**
- `KURULUM.md` — Türkçe, 7 adım, referans seçim rehberi dahil
- `INSTALLATION.md` — İngilizce, aynı içerik

### Değişti

- **Skill formatı:** Bireysel dosyalar (`__cold-start-interview.md`, `__draft-nda.md` vb.) → **Birleşik `__skills.md`** (tüm skill'ler tek dosyada, `## /<plugin>:<skill>` başlıklarıyla)
- **Plugin adlandırması:** `administrative-litigation` → `administrative-legal`, `commercial-advisory` → `commercial-legal`, `corporate-advisory` → `corporate-legal`, `dispute-litigation` → `litigation-legal`, `employment-advisory` → `employment-legal`, `ip-advisory` → `ip-legal`, `tax-litigation` → `tax-legal` (v1.8.3 standart adlandırması)
- **TR Legal MCP:** Ayrı Mevzuat MCP + Yargı MCP → **Tek birleşik `yargi-mcp-pro`** (OAuth 2.0, WorkOS)
- **SYSTEM_PROMPT.md:** 17 yargı çevresi atıf formatları, 12 plugin haritası, generic büro kadro entegrasyonu
- **firm-profile.md:** Kurum-spesifik içerik tamamen kaldırıldı → tam `[DOLDUR]` placeholder şablonu
- **`knowledge/references/`:** 33 → 42+ dosya (eskiler güncellendi, yeniler eklendi)
- **README.md:** v1.2.0 içerik tablosu, yeni komut örnekleri, güncel paket yapısı
- **KULLANIM-REHBERI.md:** `KURULUM.md` ve `INSTALLATION.md` olarak ikiye ayrıldı; ana klasör altına taşındı

### Kaldırıldı

- `KULLANIM-REHBERI.md` → yerini `KURULUM.md` + `INSTALLATION.md` aldı
- `knowledge/references/socar-*.md` (3 dosya) — kurum-spesifik içerik, public release için uygun değil
- v1.0.1 bireysel skill dosyaları (criminals+firm-operations hariç yeni birleşik format ile değiştirildi)

### Güvenlik / Gizlilik

- Tüm gerçek kişi isimleri, unvanlar, şirket adları, vergi numaraları temizlendi
- `firm-profile.md` sıfırdan yazıldı — herhangi bir tüzel kişi veya gerçek kişi verisi içermez
- Tüm referans dosyaları SOCAR / kurum-spesifik bölümlerden arındırıldı
- `energy-finance__skills.md` içinde kurum adları `[Müvekkil]` ile değiştirildi

---

## [1.0.1] — 2026-05-23 — *Yargı MCP Düzeltmesi + MCP Connector Kurulum Adımı*

### Eklendi
- **KULLANIM-REHBERI.md:** MCP bağlantı kurulumu eklendi (Mevzuat MCP + Yargı MCP + OpenSanctions)

### Düzeltildi
- **Yargı MCP connector adı hatası:** `mcp__claude_ai_Yargi_MCP__*` → `mcp__claude_ai_Yarg_MCP__*`
- **14 hatalı araç adı** gerçek 26 araç isimleriyle değiştirildi
- Atıf formatı güncellendi: `[Yargı MCP ...]` → `[Yarg MCP ...]`

---

## [1.0.0] — 2026-05-17 — *Initial Public Release*

İlk halka açık sürüm. Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiş, dava + danışmanlık dengeli, 0–30 çalışanlı Türk hukuk büroları için danışman tarafı adapte edilmiş hibrit hukuk asistanı paketi.

### Eklendi
- 9 plugin (dispute-litigation, administrative-litigation, tax-litigation, criminal-defense, commercial-advisory, corporate-advisory, employment-advisory, ip-advisory, firm-operations)
- 19 bireysel skill dosyası
- 33 TR mevzuat ve meslek pratiği referansı
- Mevzuat MCP + Yargı MCP entegrasyonu

---

[1.2.0]: ./VERSION.md
[1.0.1]: https://github.com/beerbottle90/ArthurLegal/tree/main/ArthurLegal-Law-Firm-v1.0.1-Public-Release
[1.0.0]: https://github.com/beerbottle90/ArthurLegal/tree/main/ArthurLegal-Law-Firm-v1.0.0-Public-Release
