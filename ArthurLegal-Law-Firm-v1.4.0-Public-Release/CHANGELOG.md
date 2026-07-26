# Değişiklik Günlüğü

[Keep a Changelog](https://keepachangelog.com/tr-TR/1.1.0/) formatına uygundur.
Semver: [Semantic Versioning 2.0](https://semver.org/lang/tr/).

---

## [1.4.0] — 2026-07-26 — *LC Digital Twin MCP Senkronu: e-qanun · LexScholar (DergiPark) · ResourceContracts*

> **Kaynak katmanı sürümü.** Üç yeni MCP sunucusu, bir yeni plugin, bir yeni
> pratik profil ve bağlayıcı bir araç-kullanım disiplini eklendi. Mevcut
> 15 plugin'in skill içeriği değişmedi; her birine yalnızca kaynak yönlendirme
> bloğu eklendi.

### Eklendi

**1 yeni pratik alan (plugin) — `legal-research` (kaynak katmanı):**

- `/legal-research:kaynak-secimi` — kaynak yönlendirme matrisi, kaynak
  hiyerarşisi, 100 saniye kuralı, **meslek sırrı sınırı (Av. K. m. 36)**,
  "araç ne tutmuyor" kontrolü.
- `/legal-research:az-mevzuat` — e-qanun MCP; akt arama + **yürürlük statüsü
  doğrulaması** + madde metni.
- `/legal-research:karsilastirmali-doktrin` — LexScholar MCP; Türk + yabancı +
  karşılaştırmalı akademik doktrin.
- `/legal-research:sozlesme-emsali` — ResourceContracts MCP; imzalı PSA/JOA
  emsali ve kloz benchmark.

> `legal-research` bağımsız bir pratik alan değil, **kaynak katmanıdır** —
> dilekçenin, mütalaanın ve görüşün altındaki kaynağı besler.

**1 yeni pratik profil:**

- `profiles/legal-research.md` — kaynak hiyerarşisi tablosu, DergiPark dergi
  eşlemesi, meslek sırrı sınırı, 100 saniyenin dosya planlamasına etkisi,
  **araştırma notu asgari içeriği** (7 madde) ve "bu büroda kabul edilmeyen
  yaygın hatalar" listesi.

**3 yeni MCP sunucusu (self-hosted, auth'suz):**

| MCP | Rol | Kapsam |
|---|---|---|
| **e-qanun** | **BİRİNCİL** — AZ mevzuatı | Adalet Bakanlığı'nın resmî `api.e-qanun.az` veritabanı; 6 araç; **yürürlük statüsü** (`Qüvvədədir` / `Ləğv olunmuş`) doğrulamalı |
| **LexScholar** | **İKİNCİL** — hukuk doktrini | 10 açık erişim indeksi federe: DOAJ · SciELO · HAL · Dialnet · OpenAIRE · Law Review Commons · OpenAlex · Crossref · Unpaywall · **DergiPark**; 6 araç |
| **ResourceContracts** | **EMSAL** — imzalı sözleşme | 5.125 sözleşme, 107 ülke, 141 emtia + uzman kloz anotasyonları (NRGI/CCSI/Dünya Bankası); 9 araç |

**3 yeni referans dosyası:**

- `eqanun-mcp-rehberi.md` · `lex-scholar-rehberi.md` · `resourcecontracts-rehberi.md`

**Türk doktrini artık araçla aranabiliyor.** DergiPark'ın **resmî OAI-PMH** ucu
LexScholar'ın onuncu kaynak adaptörü olarak eklendi — anahtar yok, CAPTCHA yok,
0,2-0,5 s. **19 hukuk dergisi tek tek doğrulandı:** 15 hukuk fakültesi dergisi
(Ankara, Ankara Hacı Bayram Veli, Ankara Sosyal Bilimler, Anadolu, Dicle,
Dokuz Eylül, İnönü, İstanbul, Kocaeli, Marmara, Necmettin Erbakan, Sakarya,
Selçuk, Yeditepe, Karatekin) + Ceza Hukuku ve Kriminoloji, İdare Hukuku ve
İlimleri, Adalet Dergisi, İslam Hukuku Araştırmaları. Router konuya göre doğru
dergiyi seçer.

### Değiştirildi

- **`SYSTEM_PROMPT.md`** — 16 plugin haritası; üç yeni atıf biçimi (AZ mevzuatı
  **statü atıfın içinde**, LexScholar `citation` birebir, ResourceContracts
  `source_url` + CC BY-SA); yeni **"Üç yeni MCP"** bölümü (kaynak hiyerarşisi,
  100 saniye kuralı, araçların ne tutmadığı, **Av. K. m. 36 sınırı**, araç adı
  çakışması); sınır-ötesi tabloya iki satır; footer sürüm ve lisans düzeltildi.
- **`azerbaycan-hukuk-rehberi.md`** — kapsamı daraltıldı: mevzuat okuma yolu
  `eqanun-mcp-rehberi.md`'ye taşındı; bu rehber içtihat (constcourt.gov.az,
  CODICES) + İngilizce kaynaklar (minenergy.gov.az, NATLEX) + WebFetch yedekleri
  için kaldı. WebFetch yolunda **statünün doğrulanmadığı** açıkça işaretlendi.
- **`karsilastirmali-hukuk-rehberi.md`** — MCP sunucu haritası (5 sunucu);
  AZ satırı WebFetch'ten MCP'ye taşındı; **100 saniye kuralı** ve "özel araç >
  genel web arama" ölçümü; kaynak hiyerarşisi; üç yeni atıf etiketi.
- **On iki plugin skill kitapçığı** (`commercial-legal`, `corporate-legal`,
  `energy-finance`, `regulatory-legal`, `litigation-legal`, `tax-legal`,
  `contract-drafting`, `administrative-legal`, `employment-legal`,
  **`advocacy-legal`**, **`expert-opinion`**, **`firm-operations`**) —
  İçindekiler altına **"Kaynak katmanı — /legal-research"** yönlendirme bloğu
  eklendi. Skill gövdeleri değişmedi.
- **`KURULUM.md` / `INSTALLATION.md`** — v1.4.0 sayıları ve üç MCP connector
  kurulum adımı.
- **`ATTRIBUTION.md`** — sürüm başlığı v1.0.0 → v1.4.0 (paketle uyumsuzdu);
  üç yeni MCP, upstream veri kaynakları ve lisansları eklendi.
- **`README.md`** — 16 pratik alan, MCP tablosu, paket ağacı (92 knowledge dosyası,
  58 referans), sınırlamalar;
  `LICENSE ← Apache 2.0` satırı `Proprietary — Non-Commercial` olarak düzeltildi.

### Talimat hizalaması — LC Digital Twin canonical prompt'u

`copilot-socar-lc-digital-twin` deposundaki `global-instructions.md`'de bulunup
bu pakette eksik veya zayıf olan kurallar `SYSTEM_PROMPT.md`'ye taşındı:

- **Üç değer kuralı keskinleştirildi** — belirsiz "tamamla / sustur / flag et"
  üçlüsü yerine **Atıfla / Sor / Çekimser kal**. Eksik olguyu doldurmak değil
  **sormak**, doğrulanamayan olguda sonuç üretmemek **çekimser kalmak** artık
  ayrı ayrı adlandırıldı.
- **Uydurma yasağı sayıldı** — kanun, madde numarası, karar numarası, tarih,
  URL, yaptırım eşleşmesi, kaynak adı, iç politika. Önceden yalnız "çekmediğin
  kaynağa atıf yapma" vardı; neyin uydurulamayacağı açıkça listelenmemişti.
- **Statik bilgi güncellik kanıtı değildir** (yeni) — knowledge dosyaları ve
  model bilgisi iç bağlamdır; dış hukukun, içtihadın, resmî kurum olgularının
  veya yaptırım listelerinin **güncel olduğunu kanıtlamaz**. Bu tür sorularda
  canlı araç ve resmî kaynak statik bilgiye tercih edilir.
- **Yaptırım stop-rule'ü genişletildi** — tetikleyici varlıklar sayıldı:
  **taraf, gerçek faydalanıcı (UBO), gemi, ürün, ülke, banka, işlem güzergâhı
  veya bağlantılı kuruluş**. Önceki hâli yalnız "yaptırım listesi eşleşmesi"
  diyordu.
- **"İmzaya hazır" kapısı** (yeni) — bu ifade, ilgili P0 kontrolleri
  karşılanmadan ve 🔴/🟠 bulgu kalmadan kullanılamaz; kullanıldığında bile
  nihai onayın **Yönetici Ortak / dosya sorumlusu avukata** ait olduğu belirtilir.
- **Yaptırım skalası dört değerli** — `prohibited` / `restricted` / `unclear` /
  `clear`, mevcut 🔴🟠🟡🟢 renk koduna eşlendi. **Belirsiz, temiz diye
  raporlanamaz.**
- **Kişisel veri maskeleme** (yeni madde) — TCKN, pasaport, telefon, IBAN,
  adres, kişisel e-posta; hukuka uygun bir inceleme amacı yoksa maskelenir.
  Yüklenen belge içeriği, istenen analizin gerektirdiğinin ötesinde açığa
  çıkarılmaz. Pakette bu kural hiç yoktu.
- **Dil kuralı** — çıktı dili Türkçedir, ancak soru başka bir dilde yazılmışsa
  o dilde cevap verilir.

### Bağlayıcı yeni kurallar

- **Yürürlük statüsü doğrulaması zorunludur.** `search_acts` bir Azerbaycan
  aktının yürürlükte olup olmadığını **söyleyemez**; yalnız `get_act` söyler.
  `Ləğv olunmuş` bir akt **dayanak yapılamaz** ve statü **atıfın içinde** taşınır.
  Müvekkile giden bir görüşte yürürlükten kalkmış bir aktın güncelmiş gibi
  görünmesi meslekî sorumluluk doğurur.
- **Kaynak hiyerarşisi:** BİRİNCİL (mevzuat/içtihat) → EMSAL (imzalı sözleşme)
  → DOKTRİN (akademik). Çelişki hâlinde birincil üstündür; çelişki **raporlanır**.
  **Dilekçede doktrin tek başına gerekçe olmaz** — birincil kaynakla birlikte
  kullanılır ve yazarına atfedilir.
- **Hakemlilik üç durumludur** (`true` / `false` / `null`). Preprint'ler ve
  **ABD öğrenci editörlü law review'ları** hakemli değildir.
- **100 saniye kuralı.** Her araç çağrısı 100 saniyede iptal edilir ve **hiçbir
  şey döndürmez**. Kısmi araştırmayı tam gibi sunmak meslekî sorumluluk doğurur —
  kapsam daralması dosya notuna yazılır.
- **Özel araç > genel web arama.** Ölçüm (25.07.2026): üç yargı çevresini
  kapsayan bir karşılaştırmalı soru özel araçtan **1 saniyenin altında** isabetli
  sonuç verdi; **aynı soru** genel web-arama sohbetinde **iki kez 100 saniyede
  iptal edildi**.
- **Meslek sırrı sınırı (Av. K. m. 36).** Üç MCP de **public** arama aracıdır;
  müvekkil adı, dosya numarası, dosya özeti, gizli taslak, müzakere pozisyonu
  veya kişisel veri gönderilmez. Sorgu soyut hukuki kavram olur. Bir arama,
  vekâlet ilişkisini ele verebilecek kadar belirginse yapılmaz.
- **Kapsam dürüstlüğü.** e-qanun içtihat tutmaz; LexScholar kanun/karar resmî
  metnini tutmaz; ResourceContracts mevzuat tutmaz. Çekilmemiş bir kaynağa
  bakılmış gibi **ima edilmez**.

### Notlar

- Üç MCP **isteğe bağlıdır**. Kurulmazsa paket çalışmaya devam eder: AZ mevzuatı
  WebFetch yoluna düşer (statü doğrulanmaz), doktrin ve sözleşme emsali kapsam
  dışı kalır — asistan bunu çıktısında belirtir.
- Üçüncü taraf DergiPark scraper'ına (`literatur-mcp`) **bağımlılık kaldırıldı**;
  resmî OAI-PMH ucu kullanılıyor.
- **Araç adı çakışması dersi:** aynı ortamda iki connector aynı araç adını
  taşımamalı — `search_articles` çakışması istemcinin şemaları karıştırıp
  `search_articles_2` üretmesine ve çağrıların 400 ile düşmesine yol açmıştı.
- Bu sürüm `copilot-socar-lc-digital-twin` deposundaki MCP entegrasyon
  çalışmasından senkronlandı; içerik büro tarafına ve generic placeholder
  şablonuna uyarlandı, gerçek müvekkil/kurum verisi içermez.

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
- `knowledge/references/sirket-*.md` (3 dosya) — kurum-spesifik içerik, public release için uygun değil
- v1.0.1 bireysel skill dosyaları (criminals+firm-operations hariç yeni birleşik format ile değiştirildi)

### Güvenlik / Gizlilik

- Tüm gerçek kişi isimleri, unvanlar, şirket adları, vergi numaraları temizlendi
- `firm-profile.md` sıfırdan yazıldı — herhangi bir tüzel kişi veya gerçek kişi verisi içermez
- Tüm referans dosyaları kurum-spesifik bölümlerden arındırıldı
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
