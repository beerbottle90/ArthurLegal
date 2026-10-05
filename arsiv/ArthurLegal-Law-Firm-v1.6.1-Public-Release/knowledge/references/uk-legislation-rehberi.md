# UK Legislation (legislation.gov.uk) — Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK** — legislation.gov.uk yalnızca REST API + content
> negotiation sunar. Bu rehber, Claude'un `WebFetch` aracını UK mevzuatıyla
> birlikte kullanma prosedürünü tanımlar. OpenSanctions rehberiyle aynı kalıp.
>
> **Durum:** ✅ Açık erişim — **API anahtarı gerekmez**, kayıt gerekmez. Birincil
> yargı çevresi Türkiye'dir; bu kaynak yalnızca İngiliz hukuku temas eden işlerde
> kullanılır (bkz. `karsilastirmali-hukuk-rehberi.md`).

---

## legislation.gov.uk nedir?

**legislation.gov.uk** — Birleşik Krallık'ın resmi mevzuat veri tabanı (The
National Archives tarafından işletilir). İngiltere & Galler, İskoçya ve Kuzey
İrlanda yürürlükteki ve tarihsel mevzuatını içerir.

**Kapsam:**
- Kanunlar (Acts) ve ikincil mevzuat (Statutory Instruments)
- Hem **as-enacted** (kabul edildiği hâl) hem **revised/consolidated** (yürürlükteki güncel hâl)
- "Point in time" — belirli bir tarihteki metin sürümü

**Bu rehber neden gerekli?** Uluslararası enerji sözleşmeleri (ham petrol
alım-satım, charter party, EPC, finansman) sıklıkla **İngiliz hukukunu**
(English law) uygulanacak hukuk seçer; tahkim genelde Londra (LCIA) veya ICC
olur. Sözleşmenin governing-law klozu İngiliz hukukuysa ilgili statü metnine
buradan erişilir. Detay: `karsilastirmali-hukuk-rehberi.md`.

---

## URI şeması

Her mevzuatın kalıcı (permalink) URI'si vardır:

```
https://www.legislation.gov.uk/{tür}/{yıl}/{numara}
https://www.legislation.gov.uk/{tür}/{yıl}/{numara}/section/{madde}
```

**Mevzuat tür kodları:**

| Kod | Anlam |
|---|---|
| `ukpga` | UK Public General Act (genel kanun) |
| `uksi` | UK Statutory Instrument (ikincil mevzuat / yönetmelik) |
| `ukla` | UK Local Act |
| `asp` | Act of the Scottish Parliament |
| `asc` / `anaw` | Act/Measure of Senedd Cymru (Galler) |
| `nia` | Act of the Northern Ireland Assembly |
| `eur` | Retained / assimilated EU legislation (Brexit sonrası UK'e dâhil) |

**Örnekler:**
- `https://www.legislation.gov.uk/ukpga/2010/15` — Equality Act 2010
- `https://www.legislation.gov.uk/ukpga/1977/50` — Unfair Contract Terms Act 1977 (UCTA)
- `https://www.legislation.gov.uk/ukpga/2015/15` — Consumer Rights Act 2015
- `https://www.legislation.gov.uk/ukpga/1996/23` — Arbitration Act 1996 (Londra tahkimi)
- `https://www.legislation.gov.uk/ukpga/2018/12` — Data Protection Act 2018 (UK GDPR ile birlikte)

---

## Content negotiation — veri formatları

Herhangi bir mevzuat/madde URI'sinin sonuna ekleyerek makine-okunur veri çekilir:

| Ek | Format | Kullanım |
|---|---|---|
| `/data.xml` | XML (Legislation Schema — CLML) | Tam metin + metadata |
| `/data.akn` | Akoma Ntoso XML | Standart yapısal hukuk metni |
| `/data.htm` | Ready-transformed HTML | Web gömme / okunabilir snippet |
| `/data.feed` | Atom | Mevzuat **listesi** (arama/feed sonuçları) |
| `/data.rdf` | RDF/XML (bağlı veri) | Sürüm zinciri, yürürlük durumu, coğrafi kapsam, tadil etkileri |

**Pratik:** WebFetch ile **`/data.xml`** en güvenilirdir; sade HTML sayfası da
(`/section/{no}`) okunur ama `/data.xml` metadata + yürürlük durumu da verir.

```
WebFetch:
  URL: https://www.legislation.gov.uk/ukpga/1977/50/section/2/data.xml
  prompt: "UCTA 1977 madde 2 (negligence liability) tam metnini ve yürürlük durumunu çıkar"
```

---

## RDF / bağlı veri API'si (`/data.rdf`)

> Kaynak: `https://www.legislation.gov.uk/developer/formats/rdf`

legislation.gov.uk **RDF/XML** olarak da yayımlar — özel bir ontoloji
gerektirmeden standart semantik-web sözlükleriyle (RDF Schema, OWL, Dublin Core
Terms, FOAF, XHTML Vocabulary, **FRBR/Metalex**). RDF, düz metinden çok
**sürüm/yürürlük/tadil metadatası** için değerlidir.

**FRBR kaynak hiyerarşisi** — RDF dört kaynak türünü birbirine bağlar:
- **Work** (`frbr:Work`) — soyut mevzuat öğesi, kalıcı URI:
  `http://www.legislation.gov.uk/id/ukpga/1985/67`
- **Expression** (`frbr:Expression`) — belirli sürüm (güncel / tarihli /
  prospektif/ileri-tarihli varyant)
- **Manifestation** (`frbr:Manifestation`) — biçime özgü gövde (XML, RDF/XML,
  HTML) — `dct:hasFormat` ile bağlı
- **Alias** — alternatif URI'ler (`owl:sameAs` ile kanonik kimliğe eşlenir)

**Neden işe yarar (governing-law incelemesinde kritik):**
- **Sürüm zinciri** — `dct:replaces` / `dct:isReplacedBy` tarihli sürümleri
  kronolojik bağlar; `dct:isVersionOf` belirli sürümü güncel metne bağlar.
  Bir İngiliz statüsünün **belirli bir tarihte** hangi metinde olduğunu kesin
  saptamak için.
- **Tadil etkileri** — henüz uygulanmamış değişiklikler
  `metalex:LegislativeModification` ile modellenir → "changes not yet applied"
  uyarısının makine-okunur karşılığı.
- **Coğrafi kapsam (extent)** — `dct:spatial` ile İngiltere/İskoçya/Galler/
  K.İrlanda uygulanabilirliği; `dct:hasPart` ülke-spesifik varyantlara gider.

**Çekme:** URI'ye `/data.rdf` eklenir; tarihli sürüm için tarih de eklenir:
```
https://www.legislation.gov.uk/ukpga/1985/67/data.rdf
https://www.legislation.gov.uk/ukpga/1985/67/<tarih>/data.rdf
```

**Lisans:** Tüm içerik **Open Government Licence v3.0** altındadır
(aksi belirtilmedikçe). Yeniden kullanım serbesttir; atıf disiplini korunur.

**Pratik öneri:** Statü **metni** için `/data.xml` (RDF'ten daha okunur);
statünün **hangi sürümde / yürürlükte mi / nereye uygulanır** sorusu için
`/data.rdf`. İkisi birlikte: önce `/data.rdf` ile doğru sürüm tarihini bul,
sonra o tarihli `/data.xml` ile metni çek.

---

## Arama ve feed endpoint'leri

Mevzuat listesi (tür/yıl/başlık/tam metin filtreli) Atom feed olarak alınır:

```
https://www.legislation.gov.uk/{tür}/{yıl}/data.feed
https://www.legislation.gov.uk/{tür}?title={başlık}
https://www.legislation.gov.uk/all?text={anahtar+kelime}
```

**Örnek:**
- `https://www.legislation.gov.uk/ukpga/2015/data.feed` — 2015'in tüm genel kanunları
- `https://www.legislation.gov.uk/uksi?title=energy` — başlığında "energy" geçen SI'lar

WebFetch'e bu URL'leri verip "listele + her birinin URI'sini ver" denir, sonra
ilgili maddeye `/data.xml` ile inilir.

---

## "Point in time" — sürüm uyarısı (KRİTİK)

legislation.gov.uk iki tür metin tutar:
- **as-enacted** — kanunun ilk kabul edildiği hâl (değiştirilmemiş)
- **revised** — sonraki tadillerle güncellenmiş yürürlükteki hâl

⚠️ **Revised metin her zaman tam güncel olmayabilir** — site bazı tadilleri henüz
işlememiş olabilir ("changes not yet applied" uyarısı). Belirli bir tarihteki
metin için URI'ye tarih eklenir:

```
https://www.legislation.gov.uk/ukpga/2010/15/2024-01-01
```

Çıktıda hangi sürümü çektiğini belirt; "changes to legislation" uyarısı varsa
bunu `[review]` ile flag et.

---

## Atıf disiplini

UK mevzuatı oturumda fiilen WebFetch ile çekildiyse:

```
[UK Legislation — <tür yıl c./no> s.<madde> — GG.AA.YYYY]
```

Örnek: `[UK Legislation — UCTA 1977 s.2 — 22.05.2026]`,
`[UK Legislation — Consumer Rights Act 2015 s.62 — 22.05.2026]`.

Çekmediğin bir İngiliz statüsünü "biliyorum" diye `[UK Legislation]`
etiketleyemezsin → `[model bilgisi — doğrulayın]` kullan. legislation.gov.uk
**içtihat içermez** (case law); İngiliz mahkeme kararları ayrı kaynaktır
(BAILII / Westlaw UK — bu pakette bağlı değil).

---

## Sınırlamalar

- **Yalnızca mevzuat** — İngiliz içtihatı (common law precedent) burada yok. Bir
  governing-law analizinde case law gerekirse kullanıcıya BAILII / Westlaw UK /
  dış İngiliz solicitor önerisi flag et.
- **Revised metin gecikmesi** — yukarıdaki "point in time" uyarısı.
- **Brexit sonrası `eur` kategorisi** — "retained/assimilated EU law" statüsü
  Retained EU Law (Revocation and Reform) Act 2023 ile değişti; bu kategoride
  yürürlük durumunu ayrıca doğrula.
- **JS yok ama büyük belgeler** — çok uzun kanunlarda tek madde (`/section/{no}`)
  çekmek tam metin çekmekten güvenilir.

---

## Yedek kaynaklar (WebFetch erişilemezse)

| Kaynak | URL | Not |
|---|---|---|
| legislation.gov.uk (HTML) | https://www.legislation.gov.uk | `/data.xml` yerine sade sayfa |
| The National Archives | https://www.nationalarchives.gov.uk | Kurum |
| BAILII | https://www.bailii.org | İçtihat (mevzuat değil) |

---

## Versiyon disiplini

- Bu rehber **v1.6.0** (*Cross-Border Connectors*) ile eklendi.
- legislation.gov.uk API'si stabil; content negotiation şeması yıllardır
  değişmedi. Yine de format ekleri (`/data.akn` vd.) için
  `https://www.legislation.gov.uk/developer/formats` teyit edilir.

---

*Son güncelleme: 22.05.2026 — v1.6.0. legislation.gov.uk WebFetch entegrasyon prosedürü; açık erişim, anahtar gerektirmez.*
