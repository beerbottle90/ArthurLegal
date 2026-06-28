# Değişiklik Günlüğü

[Keep a Changelog](https://keepachangelog.com/tr-TR/1.1.0/) formatına uygundur.
Semver: [Semantic Versioning 2.0](https://semver.org/lang/tr/).

---

## [1.3.1] — 2026-06-28 — *Connector Fallback'leri + OpenSanctions Key Default*

> Yalnızca **dış kaynak erişim/connector** güncellemesi — plugin/skill içeriği değişmedi.

### Eklendi / Düzeltildi

- **Connector sağlık taraması (2026-06-28):** API/WebFetch jurisdiction connector'ları canlı test edildi; `karsilastirmali-hukuk-rehberi`'ye **Connector Sağlık & Fallback tablosu** (16 connector) eklendi.
- **🇩🇪 DE:** `gesetze-im-internet.de` erişilemiyor (ECONNREFUSED) → birincil alternatif **NeuRIS API** (`testphase.rechtsinformationen.bund.de`).
- **🇷🇺 RU:** `pravo.gov.ru` geo-block → çalışan alternatif **consultant.ru**.
- **🇺🇸 US (no-key):** GovInfo alternatifi **Cornell LII** (`law.cornell.edu/uscode`).
- **🇦🇿 AZ:** e-qanun.az anti-bot → **cis-legislation.com**. **🇨🇳 CN:** HuggingFace gated → **flk.npc.gov.cn / gov.cn**.
- **🌍 OpenSanctions:** API key (`a1c019…`) **default gömülü** işlendi; `{API_KEY_FROM_ENV}` placeholder ve çelişkili "env'de tut / paylaşılan dosyaya yazma" notları kaldırıldı.

---

## [1.3.0] — 2026-06-25 — *Sözleşme Üretimi & Redline + Rekabet Hukuku*

### Eklendi

**1 yeni pratik alan (plugin):**
- `contract-drafting` — sözleşme belgesi üretimi & redline: yüklenen sözleşmeyi son hâline getirme (incele→belgeye redline + comment uygula), örnek/emsalden yeni belge türetme, iki versiyon karşılaştırma (track-changes diff), ek protokol/tadil/süre uzatımı. Claude.ai Projects kalibreli (markdown redline + temiz revize + değişiklik listesi).

**2 yeni referans dosyası:**
- `rekabet-hukuku-rehberi.md` — 4054 sayılı Kanun çatısı: m.4/6/7 yasaklar, muafiyet (m.5 + grup muafiyeti), **birleşme-devralma kontrolü** (2022 ciro eşikleri + Tebliğ 2010/4), soruşturma usulü + idari para cezası, pişmanlık/uzlaşma, de minimis.
- `redline-konvansiyonlari-rehberi.md` — sözleşme redline & comment ev standardı (severity, fallback pozisyon, standart kloz seti).

> Tüm içerik generic kurumsal şablon olarak hazırlanmıştır; kişisel veri / kurum-spesifik bilgi içermez.

---

## [1.2.0] — 2026-06-04 — *Çok Yargı Çevresi Genişlemesi + 4 Yeni Plugin*

### Eklendi

**4 yeni pratik alan (plugin):**
- `tax-legal` — KVK + VUK + KDV/ÖTV + GİB + Danıştay vergi davası; Mali İşler-Hukuk koordinasyon modeli
- `administrative-legal` — 3 dereceli idari yargı + EPDK proaktif dialog + ÇED itiraz
- `litigation-legal` — HMK + UYAP + İSG 24-72 saat runbook + dış vekil koordinasyon
- `energy-finance` — Enerji M&A · proje finansmanı · JV · LNG offtake (cross-border)

**1 yeni commercial skill:**
- `governing-law-review` — Sınır ötesi sözleşmelerde yargı çevresi analizi (17 yargı çevresi)

**31 yeni referans dosyası (17 yargı çevresi):**
- 🇬🇧 UK: `uk-legislation-rehberi.md`
- 🇺🇸 US: `us-legislation-rehberi.md`, `courtlistener-rehberi.md`
- 🇪🇺 AB/ECHR: `eu-legislation-rehberi.md`
- 🇩🇪 DE: `germany-legislation-rehberi.md`
- 🇫🇷 FR: `france-legislation-rehberi.md`
- 🇮🇹 IT: `italy-legislation-rehberi.md`
- 🇯🇵 JP: `japan-legislation-rehberi.md`
- 🇨🇭 CH: `switzerland-caselaw-rehberi.md`
- 🇷🇺 RU: `russia-legislation-rehberi.md`
- 🇦🇿 AZ: `azerbaycan-hukuk-rehberi.md`
- 🇨🇳 CN: `cin-hukuku-rehberi.md`
- 🇷🇸 SR: `sirbistan-hukuku-rehberi.md`
- 🇨🇿 CZ: `cek-hukuku-rehberi.md`
- TR: `epdk-rehberi.md`, `ced-rehberi.md`, `hmk-rehberi.md`, `iyuk-rehberi.md`, `idari-yargi-yapisi-rehberi.md`, `isg-dava-rehberi.md`, `istac-rehberi.md`, `seveso-buyuk-kaza-rehberi.md`, `vuk-rehberi.md`, `transfer-pricing-rehberi.md`, `gib-ozelge-rehberi.md`, `otv-rehberi.md`, `smk-rehberi.md`, `turkpatent-rehberi.md`, `udrp-domain-rehberi.md`, `uyap-rehberi.md`, `karsilastirmali-hukuk-rehberi.md`

**Mimari değişiklik — birleşik skill format:**
- Her plugin için ayrı ayrı skill dosyaları → tek `<plugin>__skills.md` dosyasında birleştirildi
- `profiles/` klasörü kaldırıldı; profile bilgileri birleşik skill dosyalarına entegre edildi

**TR Legal MCP birleşik connector (v1.5.0+):**
- Mevzuat MCP + Yargı MCP tek connector altında — `yargi-mcp-pro`
- Endpoint: `https://yargi-mcp-pro-production.up.railway.app/mcp`

**OpenCaseLaw.ch MCP (v1.7.0+):**
- İsviçre 972K+ karar, Fedlex mevzuatı, 33 MCP aracı (auth yok, CC0)

**KURULUM.md** klasörün kök dizinine taşındı — kurulum kolaylığı

### Değiştirildi

- `SYSTEM_PROMPT.md` v1.2.0 olarak yeniden yazıldı: generik, şirket-agnostik, 10 plugin haritası
- `company-profile.md` tam `[DOLDUR]` şablona dönüştürüldü — public repoda gerçek şirket verisi saklanmıyor
- Skill dosyaları eskiye dönük birleştirildi — `knowledge/skills/` içinde 10 dosya

---

## [1.0.1] — 2026-05-18 — *Yarg MCP Düzeltmesi*

### Düzeltildi

- **Yargı MCP connector adı hatası giderildi:** `mcp__claude_ai_Yargi_MCP__*` → `mcp__claude_ai_Yarg_MCP__*` (gerçek Claude.ai connector adı)
- **14 hatalı araç adı kaldırıldı**, gerçek 26 araç isimleriyle değiştirildi:
  - Arama: `search`, `search_bedesten_unified`, `search_emsal_detailed_decisions`, `search_anayasa_unified`, `search_kvkk_decisions`, `search_rekabet_kurumu_decisions`, `search_sayistay_unified`, `search_bddk_decisions`, `search_gib_ozelge`, `search_sigorta_tahkim_decisions`, `search_kik_v2_decisions`, `search_uyusmazlik_decisions`, `search_within_sigorta_tahkim_issue`
  - Tam metin: `get_emsal_document_markdown`, `get_anayasa_document_unified`, `get_bedesten_document_markdown`, `get_kvkk_document_markdown`, `get_rekabet_kurumu_document`, `get_sayistay_document_unified`, `get_bddk_document_markdown`, `get_gib_ozelge_document_markdown`, `get_kik_v2_document_markdown`, `get_sigorta_tahkim_document_markdown`, `get_uyusmazlik_document_markdown_from_url`
  - Yardımcı: `fetch`, `check_government_servers_health`
- **Önemli davranış notu eklendi:** Yargıtay ve Danıştay kararları için ayrı araç yoktur; `search_bedesten_unified` veya `search_emsal_detailed_decisions` üzerinden sorgulanır
- **Atıf formatı güncellendi:** `[Yargı MCP ...]` → `[Yarg MCP ...]`
- Tam metin alma araçları ilk kez belgelendi (v1.0.0'da yoktu)

---

## [1.0.0] — 2026-05-17 — *Initial Public Release*

İlk halka açık sürüm. Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiş, Türk hukukuna ve kurumsal in-house pratiğine adapte edilmiş hibrit hukuk asistanı paketi.

### Eklendi

**9 plugin:**

- `commercial-legal` — TBK + TTK + damga vergisi + KEP + ISTAC; NDA GREEN/YELLOW/RED triage playbook
- `corporate-legal` — TTK 134-209, Rekabet Kurulu 2010/4, SPK, VERBİS; M&A diligence
- `employment-legal` — 4857, 5510, 6356, 6331; iç soruşturma, fesih, kıdem tazminatı tavanı
- `privacy-legal` — 6698 KVKK + GDPR ikili rejim, m. 9 yurt dışı 2024 rejimi, DSAR 30 gün
- `regulatory-legal` — Resmi Gazete + EPDK/BDDK/SPK/KGK + CBK haftalık digest
- `ip-legal` — 6769 SMK, TÜRKPATENT, 5651 + 5846 FSEK; marka clearance, UDRP, IP brief
- `litigation-legal` — HMK + UYAP + İSG runbook (0-1/0-24/0-72 saat fazlı); dış-vekil koordinasyon; TTK m. 5/A ön-kontrol
- `tax-legal` — VUK 213, KVK 5520 (TP), KDVK 3065, ÖTV 4760, GİB özelge; Mali İşler-Hukuk koordinasyon modeli; Danıştay vergi davası (İYUK 30 g)
- `administrative-legal` — İYUK 2577 (idare 60 g / vergi 30 g + m. 20/A ÇED ivedi rejim); 3 dereceli idari yargı (İdare Mah. → BİM → Danıştay); EPDK proaktif dialog; ÇED ret/itiraz

**MCP entegrasyonları (her plugin .mcp.json'da):**

- ✅ Mevzuat MCP (https://mevzuat.surucu.dev/mcp) — 26 araç, TR mevzuat norm metinleri
- ✅ Yargı MCP (https://yargimcp.surucu.dev/mcp) — 24 araç, 15 kurum (Yargıtay, Danıştay, AYM norm/bireysel, Bedesten, Uyuşmazlık, Emsal/UYAP, KİK, Rekabet, Sayıştay, KVKK Kurulu, BDDK, GİB özelge, Sigorta Tahkim)
- ⚙️ OpenSanctions API (REST/WebFetch pattern) — kullanıcı API key girişiyle aktif
- ✅ KAP + e-ŞİRKET (WebFetch) — public BIST açıklamaları
- (Kütüphane) Anthropic standart MCP'leri — Ironclad, DocuSign, iManage, Slack, GDrive, Box

**TR Overlay:**

- `tr-overlay/company-profile.md` — Şirket profil şablonu (rol-bazlı yer-tutucularla, kurumsal holding örneği üzerinden)
- 9 plugin için TR-adapte CLAUDE.md profilleri (`tr-overlay/profiles/`)
- 20+ TR referans dosyası (`tr-overlay/references/`):
  - `kanun-kisaltmalar.md` — TR mevzuat + enerji + sermaye piyasası + yaptırım kısaltma sözlüğü
  - `mevzuat-mcp-rehberi.md` — Mevzuat MCP kullanım kılavuzu
  - `yargi-mcp-rehberi.md` — Yargı MCP 24 araç + kurumsal kullanım pattern'ları
  - `damga-vergisi-rehberi.md` — DVK hesabı + tipik kurumsal senaryolar
  - `kvkk-m11-cevap-sablonu.md` — DSAR cevap şablonu (KVKK m. 28 istisna kontrolü dahil)
  - `reg-feed-haftalik-sablon.md` — Regülasyon haftalık digest şablonu
  - `yaptirim-tarama-rehberi.md` — 6 yaptırım rejimi + adım adım akış
  - `opensanctions-rehberi.md` — REST API WebFetch pattern + match skoru kalibrasyon
  - `halka-acik-istirak-kap-rehberi.md` — BIST'e kayıtlı şirket içsel bilgi + KAP açıklama + ilişkili taraf
  - `elektrik-uretim-istiraki-rehberi.md` — EPDK 6 adımlı süreç (lisans devri/değişiklik)
  - `kap-esirket-webfetch-rehberi.md` — KAP WebFetch URL pattern'ları
  - `hmk-rehberi.md` — HMK temel maddeler + dava akışı
  - `uyap-rehberi.md` — UYAP modülleri + dış vekil-in-house iş akışı
  - `isg-dava-rehberi.md` — İSG üçlü-paralel risk (ceza + tazminat + idari)
  - `istac-rehberi.md` — ISTAC + ICC tahkim
  - `seveso-buyuk-kaza-rehberi.md` — Büyük Endüstriyel Kazalar Yönetmeliği (2872 sayılı Çevre K. m. 10/A + RG 02.08.2019/30850); Üst Seviye Kuruluş yükümlülükleri
  - `vuk-rehberi.md` — Vergi Usul Kanunu temel maddeler + süreler
  - `transfer-pricing-rehberi.md` — KVK m. 13 + OECD TPG + BEPS
  - `gib-ozelge-rehberi.md` — Özelge talep süreci + risk yönetimi
  - `otv-rehberi.md` — ÖTV ihracat istisnası + Danıştay 3. Daire
  - `iyuk-rehberi.md` — İYUK m. 7 (idare 60 g / vergi 30 g) + m. 20/A (ÇED ivedi) + m. 27 (yürütmenin durdurulması) + m. 45/46 (istinaf/temyiz)
  - `ced-rehberi.md` — ÇED özel rejim tablosu + m. 20/A
  - `epdk-rehberi.md` — EPDK lisans + proaktif dialog modeli + Kurul karar itirazı
  - `idari-yargi-yapisi-rehberi.md` — 3 dereceli yapı + Danıştay K. m. 24/30 istisnaları
  - `smk-rehberi.md` — 6769 SMK marka/patent/tasarım pratiği, m. 5 mutlak red + m. 6 nispi red
  - `turkpatent-rehberi.md` — TÜRKPATENT online araçlar (marka arama, EPATS, Madrid), YİDK itiraz prosedürü
  - `udrp-domain-rehberi.md` — Sahte domain takedown (3 paralel rejim: SMK + 5651 + TCK 158), UDRP başvuru

**Dağıtım paketleri:**

- `dist/claude-code/` — Claude Code (CLI / VSCode) kurulum rehberi
- `dist/claude-projects/` — Claude.ai Projects için SYSTEM_PROMPT.md + knowledge dosyaları (açık halde)

**Manifest:**

- `.claude-plugin/marketplace.json` — 9 plugin'i expose eden marketplace manifest

**Sürüm disiplini:**

- `VERSION.md` + `CHANGELOG.md` — Semver 2.0

### Tasarım notları

- **TR overlay orijinal Anthropic skill'lerini DEĞİŞTİRMEZ;** üstüne ek context koyar. Upstream güncellemesi cherry-pick ile alınabilir.
- **3 dereceli idari yargı doğru kurgulandı:** Önceki Danıştay-only kurgu hatası çözüldü; İdare Mah. → BİM → Danıştay; Danıştay K. m. 24/30 dar istisnalar ayrı.
- **İYUK süre ayrımı:** İdare mahkemeleri 60 g, vergi mahkemeleri 30 g (2021/7331 sayılı K. değişikliği); ÇED davaları için m. 20/A ivedi rejim (30 g + doğrudan Danıştay temyiz 15 g).
- **TTK m. 5/A zorunlu arabuluculuk:** Ticari uyuşmazlık + alacak/tazminat davalarında dava şartı; `litigation-legal` skill'leri ön-kontrol yapar.
- **İSG runbook 0-1/0-24/0-72 saat fazları:** Üçlü-paralel risk (ceza + tazminat + idari); BIST açıklama (varsa) kontrol matrisi entegre.
- **Mali İşler-Hukuk koordinasyon modeli:** `tax-legal` plugin'i Mali İşler'in ana operasyonel yetki sahibi olduğunu, hukukun Maliye eylemi/dava aşamasında devreye girdiğini varsayar.
- **Privilege:** US "attorney work product" doktrini Türkiye'de yok — overlay Avukatlık K. m. 36 + ticari sır rejimine geçiş yapar.

### Bilinen sınırlar

- `tr-overlay/company-profile.md` ve plugin profillerindeki `[DOLDUR]` ve `[…]` yer-tutucular kurulum sonrası kullanıcı tarafından doldurulmalıdır.
- OpenSanctions API key kullanıcı tarafından temin edilmeli (paid membership); manuel yedek prosedür devrede.
- En güncel Yargıtay/Danıştay kararları için UYAP/Lexpera manuel doğrulama hâlâ tavsiye edilir.
- Tasarı/kanun teklifi aşamasındaki düzenlemeler kapsam dışıdır.

### Atıf

- **Author:** Claude (Anthropic, Opus 4.7 — `claude-opus-4-7`)
- **Designer:** [VERSİYON YÖNETİCİSİ]
- **Knowledge base:** Anthropic [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)

---

[1.0.1]: ./VERSION.md
[1.0.0]: https://github.com/beerbottle90/ArthurLegal/tree/main/ArthurLegal-CorporateAssistant-v1.0.0-Public-Release