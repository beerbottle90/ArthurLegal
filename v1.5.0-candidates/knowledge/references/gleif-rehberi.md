# GLEIF LEI Verisi — Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK** — GLEIF (Global Legal Entity Identifier Foundation) verisi
> açık REST API üzerinden `WebFetch` ile kullanılır. Bu rehber, karşı-taraf kimlik
> çözümleme (counterparty identity resolution) prosedürünü tanımlar.
>
> **Durum:** ✅ Açık erişim — API anahtarı gerekmez, kayıt gerekmez.
>
> **Yargı çevresi notu:** ArthurLegal'in birincil yargı çevresi **Türkiye**'dir. GLEIF
> küresel bir kimlik katmanıdır; dosya yabancı bir karşı tarafa, çapraz sınır işleme
> veya KYC/yaptırım taramasına dokunduğunda devreye girer. Çok-yargı-çevresi analiz
> sırası için `karsilastirmali-hukuk-rehberi.md`.

---

## GLEIF nedir?

**GLEIF** = Global Legal Entity Identifier Foundation. Finansal İstikrar Kurulu (FSB)
öncülüğünde kurulmuş, Basel merkezli, kâr amacı gütmeyen vakıf. Küresel **LEI**
(Legal Entity Identifier, ISO 17442, 20 karakter) sisteminin işleticisidir.

**Kapsam:**
- **Level 1 — "kim kimdir":** tüzel kişi referans verisi — tescilli unvan, yargı
  çevresi, adresler, yerel sicil numarası (TR'de MERSİS/ticaret sicili), statü
- **Level 2 — "kim kime aittir":** doğrudan ve nihai ana ortaklık ilişkileri
  (**yalnızca muhasebe konsolidasyonu bazlı** — aşağıdaki sınırlara bak)
- 3,4 milyon+ LEI kaydı; günde 3 kez güncellenen Golden Copy dosyaları
- Küresel kapsama: TR, AZ, RU, CN, JP, RS dahil tüm yargı çevrelerinden tüzel kişiler

**ArthurLegal için neden gerekli?** Karşı-taraf incelemesinin ilk adımı, taranan
varlığın **hangi tüzel kişi olduğunu** deterministik biçimde sabitlemektir. Serbest
metin unvanla yaptırım taraması yanlış pozitif/negatif üretir; LEI ise tek ve
küresel benzersiz kimliktir. Akış: **önce GLEIF ile kimlik çözümle (LEI + tescilli
unvan + yargı çevresi + sicil no), sonra bu doğrulanmış kimlikle OpenSanctions
taraması yap** (`opensanctions-rehberi.md`). Aynı veri KYC dosyası ve governing-law
analizinde (karşı tarafın gerçek kuruluş yeri) doğrudan kullanılır.

---

## Endpoint / URI şeması

### Base URL
```
https://api.gleif.org/api/v1
```
Auth başlığı yok; `Accept: application/vnd.api+json` (JSON:API formatı) yeterli.

### 1. LEI kayıt arama — filtreli liste
```
GET https://api.gleif.org/api/v1/lei-records?filter[entity.legalName]={unvan}&page[size]=5
GET https://api.gleif.org/api/v1/lei-records?filter[entity.jurisdiction]=TR&page[size]=1
```
Cevap JSON:API: `meta` (sayfalama, `total`), `data[]` → `id` (LEI), `attributes`
(entity + registration blokları), `relationships`.

### 2. Fulltext autocomplete — unvan tamamlama
```
GET https://api.gleif.org/api/v1/autocompletions?field=fulltext&q={parça}
```
Her öneri, ilgili LEI kaydına `relationships.lei-records` ile bağlanır.

### 3. Tekil kayıt + Level 2 ilişkiler
```
GET https://api.gleif.org/api/v1/lei-records/{LEI}
GET https://api.gleif.org/api/v1/lei-records/{LEI}/ultimate-parent
GET https://api.gleif.org/api/v1/lei-records/{LEI}/direct-parent
GET https://api.gleif.org/api/v1/lei-records/{LEI}/direct-child-relationships
```

### 4. Toplu veri — Golden Copy dosyaları
```
https://www.gleif.org/en/lei-data/gleif-golden-copy
```
Günde 3 set (02:00, 10:00, 18:00 UTC), format: **XML, CSV, JSON**. Delta dosyaları
8 saat / 24 saat / 7 gün / 31 gün önceye göre değişiklikleri verir — tam popülasyonu
indirmeden yeni/güncellenmiş LEI'leri yakalamak için.

### Önemli alanlar (Level 1)

| Alan | İçerik |
|---|---|
| `id` | LEI (20 karakter, ISO 17442) |
| `attributes.entity.legalName` | Tescilli unvan + dil kodu |
| `attributes.entity.jurisdiction` | Kuruluş yargı çevresi (örn. `TR`, `AZ`, `AE-DU`) |
| `attributes.entity.legalAddress` | Tescilli adres (şehir, ülke) |
| `attributes.registration.status` | `ISSUED` / `LAPSED` / `RETIRED` vb. |
| `attributes.registration.nextRenewalDate` | Yenileme tarihi — `LAPSED` kayıtta veri bayat olabilir |

---

## Örnek 1 — TR karşı tarafın kimlik çözümü + grup yapısı

Senaryo: sözleşme karşı tarafı "SOCAR Turkey Enerji" — kimlik sabitle, nihai ana
ortağı bul, sonra yaptırım taramasına geç.

```
ADIM 1 — Unvandan LEI bul:
  WebFetch: https://api.gleif.org/api/v1/autocompletions?field=fulltext&q=SOCAR%20Turkey
  → "SOCAR TURKEY ENERJİ ANONİM ŞİRKETİ" — LEI: 789000J4L7UFTRMDR776

ADIM 2 — Kaydı doğrula:
  WebFetch: https://api.gleif.org/api/v1/lei-records/789000J4L7UFTRMDR776
  → jurisdiction: TR, legalAddress: İstanbul, registration.status: ISSUED

ADIM 3 — Nihai ana ortak (Level 2):
  WebFetch: https://api.gleif.org/api/v1/lei-records/789000J4L7UFTRMDR776/ultimate-parent
  → "Azərbaycan Dövlət Neft Şirkəti" (State Oil Company of Azerbaijan Republic)
    LEI: 2549002HARR1VE257O76, jurisdiction: AZ

ADIM 4 — Doğrulanmış kimlikle yaptırım taraması:
  opensanctions-rehberi.md prosedürü — Matching API'ye unvan + ülke + sicil no
  ile git; hem TR iştiraki hem AZ nihai ana ortağı ayrı ayrı tara.

ADIM 5 — Atıf:
  [GLEIF — LEI 789000J4L7UFTRMDR776 — çekim: 13.08.2026]
```

## Örnek 2 — Unvan filtresiyle grup şirketlerini haritalama

```
ADIM 1 — Unvan filtresi:
  WebFetch: https://api.gleif.org/api/v1/lei-records?filter[entity.legalName]=SOCAR&page[size]=5
  → SOCAR - S.P.A. (IT), SOCAR OVERSEAS DMCC (AE), SOCAR LOGISTICS DMCC (AE),
    SOCAR Capital MMC (AZ), SOCAR OVERSEAS LTD. (AE-DU)

ADIM 2 — Her adayın jurisdiction + registration.status alanını kontrol et;
  sözleşmedeki taraf hangisi? (Aynı marka altında farklı yargı çevrelerinde
  ayrı tüzel kişiler — yanlış tüzel kişiyle sözleşme riski.)

ADIM 3 — Seçilen tüzel kişinin direct-parent / ultimate-parent zincirini çek,
  KYC dosyasına grup şemasını yaz; her kayda LEI + çekim tarihi ile atıf ekle.
```

---

## Atıf disiplini

Her GLEIF verisi kullanımında kaynak + çekim tarihi zorunlu ("kaynaksız hukuk yok"):

```
[GLEIF — LEI 789000J4L7UFTRMDR776 — çekim: 13.08.2026]
[GLEIF — ultimate-parent: 2549002HARR1VE257O76 — çekim: 13.08.2026]
```

- Çekilmemiş bir kayıt asla "GLEIF'te doğrulandı" diye sunulmaz; LEI kayıtları
  değişir (`LAPSED` düşebilir), tarihsiz atıf geçersizdir.
- GLEIF verisi **kimlik** kaynağıdır, hukuki yetki/temsil kaynağı değildir —
  imza yetkisi için ilgili ticaret sicili (TR'de Türkiye Ticaret Sicili Gazetesi)
  ayrıca kontrol edilir.

---

## Lisans ve sınırlar

**Lisans:** GLEIF tüm LEI verisini **CC0 1.0 Universal** ile yayımlar. Kaynaktaki
ifade: *"The data available through the Access Service are provided under the CC0
licence, see CC0 1.0 Universal (CC0 1.0)."* (gleif.org — LEI Data Terms of Use,
çekim: 13.08.2026). Veri "as is / as available" sağlanır; GLEIF garanti vermez.
Ticari kullanım, kopyalama ve yeniden dağıtım serbesttir.

**Governance sınırları — yumuşatmadan:**

- **Level 2 muhasebe konsolidasyonunda durur.** "Ultimate parent" = konsolide
  finansal tablo hazırlayan ana ortaklık. **Gerçek kişi nihai yararlanıcı (UBO /
  beneficial owner) verisi DEĞİLDİR.** MASAK/AML anlamında gerçek faydalanıcı
  tespiti için GLEIF tek başına yeterli olmaz. Tamamlayıcı: Open Ownership (BODS
  formatı) gerçek kişi BO verisi sunar, ancak **TR, AZ, RU ve CN kapsaması yoktur**
  — bu yargı çevrelerinde gerçek faydalanıcı ancak yerel sicil/beyan üzerinden
  çözülür.
- **LEI kapsaması evrensel değildir.** Kapsam, LEI zorunluluğu olan düzenlenmiş
  işlemlere (türev, sermaye piyasası raporlaması) yönelik şirketlere eğiktir.
  Örnek: TR yargı çevresinde yalnızca ~10.884 LEI kaydı var (çekim: 13.08.2026).
  **LEI'nin yokluğu, tüzel kişinin yokluğu demek değildir** — "GLEIF'te bulunamadı"
  asla "şirket mevcut değil" diye raporlanmaz.
- Ana ortaklık ilişkilerinde raporlama istisnaları vardır (entity "reporting
  exception" bildirebilir); ilişki kaydının yokluğu bağımsızlık kanıtı değildir
  (entegrasyon öncesi ilgili kayıtta doğrulanmalı).
- `LAPSED` statülü kayıtlarda referans veri bayat olabilir — statüyü her zaman
  raporla.

---

## İlgili rehberler

- `opensanctions-rehberi.md` — kimlik çözümünden sonraki yaptırım/PEP taraması;
  GLEIF → OpenSanctions sırası bu rehberin ana akışıdır
- `socar-yaptirim-tarama-rehberi.md` — tam yaptırım tarama prosedürü; Adım 1'de
  karşı-taraf kimliği GLEIF ile sabitlenir
- `karsilastirmali-hukuk-rehberi.md` — karşı tarafın yargı çevresi belirlendikten
  sonra ülke hukuku katmanı

---

*Son güncelleme: 13.08.2026 — api.gleif.org v1 endpoint'leri, Golden Copy yayın saatleri ve CC0 lisans metni canlı doğrulandı.*