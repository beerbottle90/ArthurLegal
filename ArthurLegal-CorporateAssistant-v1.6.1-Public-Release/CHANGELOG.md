# Değişiklik Günlüğü

[Keep a Changelog](https://keepachangelog.com/tr-TR/1.1.0/) formatına uygundur.
Semver: [Semantic Versioning 2.0](https://semver.org/lang/tr/).

---

## [1.6.1] — 2026-09-04 — *On MCP Connector Tek Uçta*

> **Dağıtım sürümü.** Paketin içeriği değişmedi; ona erişim yolu değişti. Daha
> önce ayrı ayrı bağlanan on MCP sunucusu tek bir kalıcı adresin arkasında
> toplandı — kullanıcı bir connector girer ve arkasına yaslanır.

### Değişti

- **Tek connector.** `https://arthurlegal-mcp.fly.dev/mcp` — auth yok, 63 araç.
  Yerini aldığı on connector: e-qanun · LexScholar · ResourceContracts · de-eli ·
  nl-rechtspraak · pl-sejm · at-ris · ie-statutebook · fi-finlex · es-boe.
  Adres kalıcıdır; geçici tünel adresleri (`*.trycloudflare.com`) her yeniden
  başlatmada değişiyor ve connector'ı **sessizce** kırıyordu — tanım doğru
  görünüyor, çağrılar düşüyordu.

- **Araç adları artık yargı çevresi önekli** — `az_` `at_` `de_` `nl_` `pl_`
  `es_` `fi_` `ie_` `scholar_` `contracts_`. Bu şart: alttaki sunucularda
  `get_act` **beş ayrı şey**, `search_legislation` üç ayrı şey demek. Öneksiz
  birleştirilseydi İspanyol hukuku sorusu Fin mevzuatıyla cevaplanabilirdi.
  Tüm referanslar, system prompt ve kurulum rehberleri önekli adlara geçirildi.

- **Dokuz ayrı `server_status` yerine tek `status`.** Her yargı çevresinin
  indeks büyüklüğünü, `index_coverage` aralığını ve semantiğin açık olup
  olmadığını bir seferde verir. Yüklenemeyen bir yargı çevresi **duyurulur**;
  sessizce boş sonuç dönmez — "sonuç yok" ile "aranmadı" farklı cevaplardır.

- **Araç sayıları düzeltildi.** System prompt bağımsız sunucuların sayılarını
  yazıyordu; toplayıcıda her sunucunun `server_status`'ı tek `status`a indiği
  için hepsi bir eksik: NL 6→5 · PL 6→5 · AT 4→3 · IE 5→4 · FI 5→4 · ES 6→5 ·
  DE 14→15.

### Bilinmesi gereken sınırlar

- **Kapsam dışında sessiz kalmaz, en yakınını döndürür.** Aradığın kanun
  indekste yoksa arama "kapsam dışı" demez — en yakın komşuyu döndürür.
  Ölçüldü: Finlandiya'ya *"iş sözleşmesi feshi"* sorulduğunda seyahat belgesi
  ve balıkçılık yönetmeliği döndü, çünkü İş Sözleşmeleri Kanunu indeksin
  2024-2025 diliminde yok. `status` aracının `index_coverage` alanını oku.

- **İndeks derinliği yargı çevresine göre değişir.** İspanya konsolide
  külliyatın tamamını taşır (12.376 akt) ve diller arası semantik arama orada
  ölçülerek doğrulandı: Türkçe *"kişisel verilerin korunması"* → LO 15/1999,
  LO 7/2021 ve AEPD Talimatı. Hollanda içtihat indeksi iki haftalık bir dilimdir
  ve karar metni içermez, yalnızca künye — Rechtspraak karar başına ayrı istek
  ister. Hollanda **mevzuatı** bundan etkilenmez (`nl_search_legislation` tüm
  KOOP deposunda tam metin arar) ve `nl_get_decision` kararın tam metnini
  anında getirir.

- **Kimlik doğrulama yok.** Adresi bilen herkes tüm araçları çağırabilir.
  Araçlar kamuya açık kaynaklarda arama yapar; müvekkil adı, dosya numarası
  veya gizli taslak sorguya konmaz.

### Düzeltildi

- `es-boe/crawl.py` belgesi `materias` konu etiketlerini indekslediğini
  yazıyordu; kod onları indekslemiyor (BOE onları yalnızca akt-detay ucunda
  veriyor). Konu sinyali başlıktan gelir.

---

## [1.6.0] — 2026-08-30 — *Kaynak Denetimi: 7 Kırık Düzeltme + 7 Yeni Yargı Çevresi*

> **Doğrulama sürümü.** Paketteki her MCP ve her WebFetch/REST kaynağına **gerçek
> sorgu** atıldı; status kodu değil, dönen veri incelendi. Yedi kırık kaynak
> düzeltildi, yedi yeni yargı çevresi eklendi — hepsi canlı endpoint testiyle.
>
> Paket: 16 plugin · **28 yargı çevresi** · 8 MCP · 93 knowledge dosyası
> (16 birleşik skill + 73 referans + 10 profil + 7 agent + firm-profile)

### Düzeltildi — canlı testle tespit edilen kırık kaynaklar

- **🔴 EUR-Lex tam metin zinciri (en yüksek etkili).** `eur-lex.europa.eu/legal-content/...`,
  `search.html` ve `eli/...` yollarının **hiçbiri WebFetch ile belge döndürmüyor** —
  JS kabuğu geliyor, içerik Resmî Gazete tarih indeksi oluyor. GDPR, Direktif 2019/944
  ve serbest metin araması ayrı ayrı doğrulandı. Çalışan **CELLAR üç adımı** belgelendi
  (`resource/celex/{CELEX}` → 303'ten UUID → SPARQL ile dil manifestation'ı →
  `{manif}/DOC_1`) ve GDPR (EN) + Dir. 2019/944 (RO) üzerinde kanıtlandı.
  `eu-legislation-rehberi.md` + `eurlex-cellar-rehberi.md`.
- **🔴 Alman NeuRIS host'u.** `api.rechtsinformationen.bund.de` **hiç var olmadı**
  (NXDOMAIN). Doğru host `testphase.rechtsinformationen.bund.de` ile değiştirildi ve
  mevzuat + içtihat uçları canlı doğrulandı. `gesetze-im-internet.de` /
  `rechtsprechung-im-internet.de` erişilemezliği yeniden doğrulandı; **de-eli MCP'nin
  `de_rii_*` araçlarının bu engelden etkilenmediği** not edildi.
- **🔴 Romanya erişimi.** `legislatie.just.ro` bağlantıyı düşürüyor (TLS kuruluyor,
  sunucu `close_notify` göndermeden kapatıyor); `cdep.ro`, `scj.ro`, `idrept.ro` de
  erişilemez, `ccr.ro` 503. Birincil kaynak **EUR-Lex CELLAR Romence tam metne**
  taşındı; `portal.just.ro`, `just.ro/legislatie`, `anre.ro` çalışan yollar olarak
  eklendi; `lege5.ro` ücretsiz katmanı **"konsolide değil"** uyarısıyla belgelendi.
- **🔴 OpenCaseLaw.ch REST yedeği.** `mcp.opencaselaw.ch/api/*` yollarının **hepsi 404** —
  böyle bir REST endpoint'i yok. Yanıltıcı "yedek" kaldırıldı; connector yokken
  izlenecek adımlar ve **atıf uydurma yasağı** yazıldı.
- **🔴 AB yaptırım endpoint'i.** `sanctionsmap.eu/api/v1/sanction` **404**; ayrıca
  sanctionsmap bir isim-arama API'si değil. İsim taraması OpenSanctions'a, resmî kayıt
  doğrulaması **AB FSF konsolide listesine** (CSV/XML, canlı doğrulandı) yönlendirildi.
  BM listesi için de çalışan tek yol (`consolidated.xml`) düzeltildi.
- **🟠 ILO NATLEX (AZ).** Eski ve yeni host'ların ikisi de **403**. e-qanun MCP'ye
  yönlendirildi (zaten daha güncel ve **statü doğrulamalı**).
- **🟠 CourtListener `citation-lookup/`.** Token başlığı istiyor (**401**), WebFetch
  başlık gönderemez. Atıf doğrulaması `analyze_citations` / `extract_citations` MCP
  araçlarına taşındı; camelCase↔snake_case alan adı tuzağı belgelendi.

### Eklendi — 6 yeni yargı çevresi (hepsi canlı API testiyle)

- **🇳🇱 Hollanda** — KOOP SRU **tam metin** mevzuat araması (1961/20991 ayrışması
  doğrulandı) + Rechtspraak Open Data **3.751.381 ECLI**. ⚠️ İçtihatta **serbest metin
  araması yok** ve tanınmayan parametreler **sessizce yok sayılıyor** — bu tuzak
  baseline karşılaştırmasıyla belgelendi.
- **🇵🇱 Polonya** — Sejm **ELI API'si**: başlıkla arama, `text.html`/`text.pdf` tam
  metin ve **`status` alanı** (`obowiązujący`). Statü, AZ kalıbındaki gibi atıfın parçası.
- **🇦🇹 Avusturya** — RIS OGD **v2.6** (⚠️ v2.5 artık 404): mevzuat **ve** OGH/VwGH/VfGH
  içtihadı tek API'de, tam metin aramasıyla.
- **🇮🇪 İrlanda** — Irish Statute Book ELI, **madde düzeyinde** erişim.
- **🇫🇮 Finlandiya** — Finlex açık veri **Akoma Ntoso REST API'si**; `{lang@sürüm}`
  tuzağı belgelendi.
- **🇪🇸 İspanya** — `xml.php` belge XML'i + günlük `sumario`. ⚠️ Konsolide mevzuat
  API'si `Accept` başlığı istediği için WebFetch'e kapalı — MCP adayı olarak işaretlendi.

- **`references/MCP-ROADMAP.md`** — hangi yargı çevresi için MCP yazılmalı, hangisi
  için gerekmiyor: canlı test kanıtına dayalı sıralama, semantik arama tasarımı ve
  mevcut 8 MCP'nin sağlık tablosu.

### Bilinen sorun

- **🇱🇺 Lüksemburg pakete alınmadı.** İlk taramada Legilux ELI URL'leri
  HTTP 200 döndürdüğü için çalışıyor sanıldı; içerik doğrulandığında her
  URL'in aynı **2.116 baytlık boş Angular kabuğunu** döndürdüğü görüldü.
  `api/v1` 401, `/sparql` SPA, `sitemap.xml` ve `/oai` 404, içerik
  müzakeresi yine kabuk — **agent'a açık hiçbir yol yok.** Rehber ve
  yargı çevresi kaydı kaldırıldı; gerekçe `MCP-ROADMAP.md`'de duruyor.
  *Ders: HTTP 200 "çalışıyor" demek değildir.*

- **OpenSanctions API anahtarı public repo'da gömülü** (`opensanctions-rehberi.md`).
  Anahtarın **hâlâ geçerli olduğu** doğrulandı. Rotasyon + connector header'ına taşıma
  önerilir; bu sürümde **bilinçli olarak değiştirilmedi** (paket sahibinin kararı).
- **sbirka-mcp (CZ)** endpoint'i canlı ama **401** — connector yetkilendirilmeden
  `cek-hukuku-rehberi.md` çalışmaz.
- **İsrail ve BAE** rehberleri, resmî portalların agent'a kapalı olduğunu (403)
  dürüstçe belgeliyor; bu iki yargı çevresinde otomatik araştırma kapasitesi yoktur.

---

## [1.5.0] — 2026-08-29 — *OSS Kaynak Dalgası + Alman Hukuku MCP + 8 Yeni Yargı Çevresi*

> **Kaynak katmanı sürümü.** Bir yeni MCP sunucusu (de-eli — Alman mevzuatı,
> içtihadı ve yasama belgeleri, 14 araç), 13.08.2026 OSS kaynak dalgasının
> tamamı, sekiz yeni yargı çevresi rehberi ve sekiz yeni `legal-research`
> skill'i. Mevcut plugin'lerin skill içeriği değişmedi.
>
> Paket: 12 plugin · 22 yargı çevresi · 8 MCP · 85 knowledge dosyası (12 birleşik skill + 65 referans + 7 agent + company-profile)

### Eklendi

- **de-eli MCP — Alman hukuku (BİRİNCİL, 14 araç).** Dört üst kaynak tek uçta:
  NeuRIS federal mevzuat (BMJV), rechtsprechung-im-internet.de (BVerfG, BGH,
  BAG, BFH, BVerwG, BSG, BPatG için **tam** külliyat), Open Legal Data (16 eyalet
  dahil, tek tam metin araması) ve Bundestag DIP (Drucksachen, gerekçeler,
  tutanaklar). Rehber: `references/de-eli-mcp-rehberi.md`. Skill:
  `/legal-research:alman-hukuku`. Atıf sözleşmesi: her yanıt `eli_uri` / `ECLI`,
  `human_readable_citation` ve `source_url` taşır — **atıf dizesi asla kurulmaz**.
- **OSS kaynak dalgası (13.08.2026) — 10 referans.** `abd-atif-dogrulama` ·
  `pii-redaksiyon` · `gleif` · `edgar` · `uk-legislation-mcp` · `eurlex-cellar` ·
  `japan-egov-api` · `france-dila` · `echr-hudoc` + makine-okur `oss-source-catalog.json`.
  89 aday → 48 bağımsız vet kararı; beş değişmez (resmî provenans, açık lisans,
  kimlik bilgisisiz erişim, aktif bakım, kaynak + çekim tarihi atıf disiplini).
- **Sekiz yeni yargı çevresi (14 → 22).** BAE · Çekya · Gürcistan · İsrail ·
  Orta Asya (KZ + UZ) · Romanya · Ukrayna · Yunanistan.
- **Sekiz yeni `legal-research` skill'i (4 → 12).** `alman-hukuku` ·
  `abd-atif-dogrulama` · `karsi-taraf-kimlik` · `uk-mevzuat` · `ab-mevzuat` ·
  `jp-mevzuat` · `fr-mevzuat` · `echr-ictihat`.
- **İsviçre emtia ticareti uyum çerçevesi** (`isvicre-emtia-ticareti-rehberi.md`):
  AML/GwG · SECO yaptırım · OR 964 kurumsal due diligence · FinSA/FinIA. İsviçre
  merkezli bir emtia ticaret kolu olan gruplar için; OpenCaseLaw.ch MCP + SECO +
  OpenSanctions üzerinden çalışır.
- **Dört REST kaynağına "MCP connector olarak eklemek" bölümü** (`gleif` ·
  `edgar` · `eurlex-cellar` · `japan-egov-api`): sarmalanacak sözleşme (base URL,
  araç yüzeyi, auth, hız sınırı, lisans), bu ekosistemde kanıtlanmış sarma kalıbı,
  port konvansiyonu ve claude.ai bağlama adımları. **Hazır endpoint verilmedi** —
  bu dördünün MCP sunucusu yok; olmayan bir adres yazmak yerine sarmalamayı
  mümkün kılan sözleşme verildi. WebFetch rotası bağlayıcısız çalışmaya devam eder.

### Değişti

- `germany-legislation-rehberi.md` artık MCP'yi birincil yol olarak gösteriyor.
  Rehberde kayıtlı **ECONNREFUSED** ölçümü MCP rotasında görülmez; çağrıyı
  sunucu kendi tarafında yapar, istemcinin çıkış ağı devreye girmez.
- Kaynak yönlendirme matrisine on satır eklendi; Almanya WebFetch satırından
  çıkarılıp MCP satırına taşındı.
- `cin-hukuku` · `switzerland-caselaw` · `seveso-buyuk-kaza` · `courtlistener`
  (+ Corporate'ta `mevzuat-mcp`) rehberleri güncel içerikle tazelendi.

### Düzeltildi

- **Kırık çapraz atıflar.** `opensanctions-rehberi.md` var olmayan bir dosyaya
  işaret ediyordu; Law Firm'de `turkpatent-rehberi.md` ve üç rehber yanlış profil
  dosyasını çağırıyordu. Paket genelinde kırık iç atıf kalmadı.
- **Artık müşteri tanımlayıcıları.** Law Firm'de iki referans dosyası
  (`kap-esirket-webfetch`, `reg-feed-haftalik-sablon`) URL'lerde bir BIST kodu
  taşımaya devam ediyordu; `[BIST KOD]` yer tutucusuna çevrildi. GLEIF rehberinin
  çalışılmış örneği de müşteriyi ele veriyordu — yerine canlı GLEIF üzerinde
  28.08.2026'da doğrulanmış nötr bir örnek kondu (Siemens AG Österreich → Siemens
  AG); örnek, rehberin "aynı marka, farklı tüzel kişi" dersini birebir gösteriyor.

---

## [1.4.0] — 2026-07-26 — *LC Digital Twin MCP Senkronu: e-qanun · LexScholar (DergiPark) · ResourceContracts*

> **Kaynak katmanı sürümü.** Üç yeni MCP sunucusu, bir yeni plugin ve bağlayıcı
> bir araç-kullanım disiplini eklendi. Mevcut 11 plugin'in skill içeriği
> değişmedi; her birine yalnızca kaynak yönlendirme bloğu eklendi.

### Eklendi

**1 yeni pratik alan (plugin) — `legal-research` (kaynak katmanı):**

- `/legal-research:kaynak-secimi` — kaynak yönlendirme matrisi, kaynak
  hiyerarşisi, 100 saniye kuralı, gizlilik sınırı, "araç ne tutmuyor" kontrolü.
- `/legal-research:az-mevzuat` — e-qanun MCP; akt arama + **yürürlük statüsü
  doğrulaması** + madde metni.
- `/legal-research:karsilastirmali-doktrin` — LexScholar MCP; Türk + yabancı +
  karşılaştırmalı akademik doktrin.
- `/legal-research:sozlesme-emsali` — ResourceContracts MCP; imzalı PSA/JOA
  emsali ve kloz benchmark.

> `legal-research` bağımsız bir pratik alan değil, **kaynak katmanıdır** —
> diğer plugin'lerin dayanağını besler, tek başına iş ürünü üretmez.

**3 yeni MCP sunucusu (self-hosted, auth'suz):**

| MCP | Rol | Kapsam |
|---|---|---|
| **e-qanun** | **BİRİNCİL** — AZ mevzuatı | Adalet Bakanlığı'nın resmî `api.e-qanun.az` veritabanı; 6 araç; **yürürlük statüsü** (`Qüvvədədir` / `Ləğv olunmuş`) doğrulamalı |
| **LexScholar** | **İKİNCİL** — hukuk doktrini | 10 açık erişim indeksi federe: DOAJ · SciELO · HAL · Dialnet · OpenAIRE · Law Review Commons · OpenAlex · Crossref · Unpaywall · **DergiPark**; 6 araç |
| **ResourceContracts** | **EMSAL** — imzalı sözleşme | 5.125 sözleşme, 107 ülke, 141 emtia + uzman kloz anotasyonları (NRGI/CCSI/Dünya Bankası); 9 araç |

**3 yeni referans dosyası:**

- `eqanun-mcp-rehberi.md` — araçlar, zorunlu statü doğrulama sırası, Azerbaycanca
  arama terimleri, atıf biçimi, kapsam dürüstlüğü (mevzuat var, içtihat yok).
- `lex-scholar-rehberi.md` — on indeksin kapsam tablosu, **DergiPark'ın 19
  doğrulanmış Türk hukuk dergisi**, router mantığı, sorgu-dili tuzağı,
  üç durumlu hakemlilik, lisans yükümlülükleri.
- `resourcecontracts-rehberi.md` — dokuz araç, `page` parametresi tuzağı,
  örnek Azerbaycan emsal indeksi (16 birincil belge), CC BY-SA 4.0 atıf zorunluluğu.

**Türk doktrini artık araçla aranabiliyor.** DergiPark'ın **resmî OAI-PMH** ucu
(`dergipark.org.tr/api/public/oai/`) LexScholar'ın onuncu kaynak adaptörü olarak
eklendi — anahtar yok, CAPTCHA yok, 0,2-0,5 s. **19 hukuk dergisi tek tek
doğrulandı:** 15 hukuk fakültesi dergisi (Ankara, Ankara Hacı Bayram Veli,
Ankara Sosyal Bilimler, Anadolu, Dicle, Dokuz Eylül, İnönü, İstanbul, Kocaeli,
Marmara, Necmettin Erbakan, Sakarya, Selçuk, Yeditepe, Karatekin) + Ceza Hukuku
ve Kriminoloji, İdare Hukuku ve İlimleri, Adalet Dergisi, İslam Hukuku
Araştırmaları.

### Değiştirildi

- **`SYSTEM_PROMPT.md`** — 12 plugin haritası; üç yeni atıf biçimi (AZ mevzuatı
  **statü atıfın içinde**, LexScholar `citation` birebir, ResourceContracts
  `source_url` + CC BY-SA); yeni **"Üç yeni MCP"** bölümü (kaynak hiyerarşisi,
  100 saniye kuralı, araçların ne tutmadığı, gizlilik sınırı, araç adı çakışması);
  sınır-ötesi tabloya iki satır; footer lisansı `MIT` → `Proprietary —
  Non-Commercial` olarak düzeltildi.
- **`azerbaycan-hukuk-rehberi.md`** — kapsamı daraltıldı: mevzuat okuma yolu
  `eqanun-mcp-rehberi.md`'ye taşındı; bu rehber içtihat (constcourt.gov.az,
  CODICES) + İngilizce kaynaklar (minenergy.gov.az, NATLEX) + WebFetch yedekleri
  için kaldı. WebFetch yolunda **statünün doğrulanmadığı** açıkça işaretlendi.
- **`karsilastirmali-hukuk-rehberi.md`** — MCP sunucu haritası (5 sunucu)
  eklendi; AZ satırı WebFetch'ten MCP'ye taşındı; **100 saniye kuralı** ve
  "özel araç > genel web arama" ölçümü eklendi; kaynak hiyerarşisi ve üç yeni
  atıf etiketi eklendi.
- **Dokuz plugin skill kitapçığı** (`commercial-legal`, `corporate-legal`,
  `energy-finance`, `regulatory-legal`, `litigation-legal`, `tax-legal`,
  `contract-drafting`, `administrative-legal`, `employment-legal`) — İçindekiler
  altına **"Kaynak katmanı — /legal-research"** yönlendirme bloğu eklendi.
  Skill gövdeleri değişmedi.
- **`KURULUM.md`** — v1.4.0 sayıları; yeni **Adım 4d** (üç MCP connector kurulumu,
  yerel portlar, geçici tünel uyarısı, araç adı çakışması uyarısı, test
  sorguları); Claude Code karşılaştırma tablosuna 100 saniye satırı.
- **`ATTRIBUTION.md`** — sürüm başlığı v1.2.0 → v1.4.0 (paketle uyumsuzdu);
  üç yeni MCP ve upstream veri kaynakları ile lisansları eklendi.

### Bağlayıcı yeni kurallar

- **Yürürlük statüsü doğrulaması zorunludur.** `search_acts` bir Azerbaycan
  aktının yürürlükte olup olmadığını **söyleyemez**; yalnız `get_act` söyler.
  `Ləğv olunmuş` bir akt **dayanak yapılamaz** ve statü **atıfın içinde** taşınır.
- **Kaynak hiyerarşisi:** BİRİNCİL (mevzuat/içtihat) → EMSAL (imzalı sözleşme)
  → DOKTRİN (akademik). Çelişki hâlinde birincil üstündür; çelişki **raporlanır**,
  ikincil kaynak lehine sessizce çözülmez.
- **Hakemlilik üç durumludur** (`true` / `false` / `null`). Preprint'ler ve
  **ABD öğrenci editörlü law review'ları** hakemli değildir; `false` veya `null`
  bir kayıt "hakemli araştırma" diye sunulamaz.
- **100 saniye kuralı.** Her araç çağrısı 100 saniyede iptal edilir ve **hiçbir
  şey döndürmez**. Sorgular dar tutulur; iptal edilen çağrı aynen tekrarlanmaz,
  bölünür ve **kapsam daralması kullanıcıya bildirilir**.
- **Özel araç > genel web arama.** Ölçüm (25.07.2026): üç yargı çevresini
  kapsayan bir karşılaştırmalı soru özel araçtan **1 saniyenin altında** isabetli
  sonuç verdi; **aynı soru** genel web-arama sohbetinde **iki kez 100 saniyede
  iptal edildi**.
- **Gizlilik sınırı.** Üç MCP de **public** arama aracıdır; gizli taslak, kloz
  metni, müzakere pozisyonu veya kişisel veri gönderilmez. Sorgu soyut hukuki
  kavram olur, belge alıntısı olmaz.
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
- Bu sürüm, Copilot Studio tarafındaki MCP entegrasyon
  çalışmasından senkronlandı; içerik generic şablon olarak uyarlandı,
  kurum-spesifik veri içermez.

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