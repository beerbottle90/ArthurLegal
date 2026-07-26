# Açık Erişimli Hukuk Literatürü — LexScholar MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.4.0).** Hakemli / açık erişimli **hukuk
> literatürü** (öğreti–doktrin) artık **tek uçtan on indeks** üzerinden
> aranabiliyor.
>
> **İKİNCİL / KARŞILAŞTIRMALI kaynaktır.** Mevzuat (`mevzuat-mcp-rehberi.md`,
> `eqanun-mcp-rehberi.md`) ve içtihat (`yargi-mcp-rehberi.md`) yerine **geçmez**.
>
> **DergiPark bu MCP'nin İÇİNDEDİR.** Türk hukuk dergilerine DergiPark'ın
> **resmî OAI-PMH** ucundan erişiliyor — anahtar yok, CAPTCHA yok, 0,2–0,5 s.
> Türk doktrini için ayrı bir araca gerek yoktur.

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint — uzak** | `https://<DEPLOY-FQDN>/mcp` ⟵ deploy sonrası doldur |
| **MCP endpoint — yerel** | `http://127.0.0.1:8010/mcp` |
| **Transport** | Streamable HTTP (`/mcp`, SSE-or-JSON) |
| **Auth** | **Yok** (tüm upstream'ler public) |
| **Opsiyonel** | `OPENALEX_API_KEY` (ücretsiz) → OpenAlex bütçesini ~100× artırır |
| **Sunucu kaynağı** | `github.com/beerbottle90/lex-scholar-api` |
| **Mimari** | Bağımlılıksız (yalnız Python stdlib); on public API'yi federe eder |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL → auth "None". Araç isim prefiksi connector adına göre üretilir — prefiksi
sabit varsayma, base isimleri kullan.

---

## 1. On indeks — ne, nerede, ne kadar

| İndeks | Hukuk filtresi | Hakemli | Tam metin | Hacim |
|---|---|---|---|---|
| **DOAJ** (omurga) | `bibjson.subject.term:law` | ✅ **garantili** | abstract + link | 268.222 makale / 1.265 dergi |
| **Law Review Commons** | 67 konu seti | ❌ öğrenci editörlü | PDF link | 351.887 (petrol-gaz 845, enerji 1.305, tahkim 2.082) |
| **SciELO** | `v440` ⊃ DIREITO/DERECHO | ✅ küratörlü | ✅ **gerçek gövde metni** | 26.003 (Şili 7.421, Meksika 4.250, Brezilya 4.228) |
| **HAL** (FR) | `domainAllCode_s:shs.droit` | ✅ bayraklı | ✅ PDF + TEI | 236.486 / 26.422 açık |
| **Dialnet** (ES) | `set=18` Ciencias jurídicas | karışık | ❌ yalnız keşif | 95.402 |
| **DergiPark** (TR) | 19 doğrulanmış hukuk dergisi seti | çoğu hakemli | abstract + link | 19 Türk hukuk dergisi |
| **OpenAIRE** (AB) | `fos=0505 law` | ✅ bayraklı | link | 582.820 |
| **Crossref / Unpaywall** | — | — | OA çözücü | DOI evreni |
| **OpenAlex** ⚠ ölçülü | `subfields/3308` | çıkarımsal | link | 2.244.618 / 362.231 açık |

**Ülke kapsamı (DOAJ hakemli hukuk dergisi):** ID 191 · BR 90 · PL 66 · ES 58 ·
IR 42 · IT 37 · GB 37 · RU 31 · UA 24 · **TR 20** · EG 20 · MX 15 · US 10 ·
RO 10 · NL 10 · DE 8 · FR 7 · CH 7 · IQ 6 · ZA 5 · KZ 2.

> **AZ, IN, JP, AE = 0.** Bu yargı çevrelerine yalnız OpenAlex üzerinden
> ulaşılır (AZ'de 193 açık erişim hukuk çalışması var). **Literatürün yokluğu,
> hukukun yokluğu değildir** — raporla.

---

## 1b. DergiPark kapsamı (19 dergi — hepsi tek tek doğrulandı)

**Hukuk fakültesi dergileri (15):** Ankara · Ankara Hacı Bayram Veli · Ankara
Sosyal Bilimler · Anadolu · Dicle · Dokuz Eylül · İnönü · İstanbul (Mecmua) ·
Kocaeli · Marmara · Necmettin Erbakan · Sakarya · Selçuk · Yeditepe · Karatekin

**Konu dergileri (4):** Ceza Hukuku ve Kriminoloji · İdare Hukuku ve İlimleri ·
Adalet Dergisi · İslam Hukuku Araştırmaları

Router konuya göre doğru dergiyi seçer: *ceza/kriminoloji* → Ceza Hukuku
Dergisi · *idari/imar/ihale* → İdare Hukuku · *deniz/sigorta/petrol/maden* →
İstanbul Mecmuası · *ticaret/şirket/tahkim/enerji* → Marmara ·
*anayasa/vergi/milletlerarası* → Ankara.

> **Neden liste küratörlü?** DergiPark'ın `ListSets` ucu 100 sette duruyor ve
> `resumptionToken` vermiyor — binlerce dergilik katalog OAI üzerinden
> sayılamıyor. Kapsam üç bağımsız yoldan derlendi (DergiPark'ın açtığı setler,
> DOAJ'ın Türk hukuk dergileri, OpenAlex kaynak kayıtları) ve **her dergi kodu
> tek tek denendi**. Sitenin kendi arama ucuna dokunulmadı: `robots.txt`
> `/search` yolunu tüm ajanlara kapatıyor.
>
> **Kod eklerken:** makul görünen slug yetmez — `ybhd` hukuk kodu gibi duruyor
> ama *Yoğun Bakım Hemşireliği Dergisi*, `ashd` de tıp. İkisi de doğrulamada
> yakalanıp elendi.

**Neden scraping değil OAI-PMH?** Üçüncü taraf bir DergiPark scraper'ı
(`literatur-mcp`) daha önce kullanılıyordu; el sıkışması 0,2 s'de dönerken
`search_articles` yanıtsız kalıyor ve her çağrıda platformun 100 s araç limitini
dolduruyordu — arkasında ücretli CAPTCHA çözme + site kazıma zinciri vardı.
Resmî OAI-PMH ucu (`dergipark.org.tr/api/public/oai/`) anahtarsız,
CAPTCHA'sız ve 0,2–0,5 s yanıt veriyor. **Ayrı DergiPark aracı kurma — bu MCP
zaten kapsıyor.**

---

## 2. Araçlar (6 adet)

| Araç | Ne yapar | Önemli parametreler |
|------|----------|---------------------|
| `search_legal_scholarship` | Federe arama; router 2–3 indeks seçer | `query`, `jurisdiction`, `language`, `peer_reviewed_only`, `source`, `year_from/to`, `limit` |
| `compare_jurisdictions` | Aynı soruyu N ülkede çalıştırır, **ülke bazlı gruplar** | `query`, `jurisdictions:[...]`, `limit_per` |
| `get_scholarship_article` | Tek makale künyesi | `source`, `id` |
| `get_scholarship_fulltext` | Gövde metni (karakterle sayfalanır) | `source`, `id`, `offset`, `max_chars` |
| `resolve_doi` | DOI → künye + açık kopya | `doi` |
| `list_sources` | İndeks yetenek kartları + canlı OpenAlex bütçesi | — |

**Şeffaflık:** her yanıt `sources_queried`, `sources_skipped` (+ sebep),
`routing_reasons` ve `errors` döndürür. Sessiz kırpma yok — `sources_skipped`
doluysa **kapsam notunda söyle**.

> ⚠️ **Araç adı çakışması dersi:** bu araçlar başlangıçta `search_articles`
> adını kullanıyordu; başka bir literatür sunucusunda aynı isim vardı, istemci
> şemaları karıştırıp `search_articles_2` üretti ve çağrılar 400 ile düştü.
> Adlar `search_legal_scholarship` / `get_scholarship_article` /
> `get_scholarship_fulltext` olarak ayrıştırıldı. **Aynı ortamda iki connector
> aynı araç adını taşımamalı.**

---

## 3. Router nasıl karar veriyor

| Sinyal | Yönlendirme |
|---|---|
| Sorguda **DOI** | Crossref + Unpaywall (keşif atlanır) |
| `jurisdiction=` | ülkenin kendi indeksi (BR→SciELO, FR→HAL, ES→Dialnet, AZ→OpenAlex) |
| Sorgu dili | es/pt→SciELO+Dialnet · fr→HAL · de→OpenAIRE · **tr→DergiPark+DOAJ** · ru→DOAJ+OpenAlex |
| Enerji/tahkim sözcükleri | + Law Review Commons (ABD dışı bir ülkeye kilitliyse **eklenmez**) |
| `peer_reviewed_only=true` | preprint ve öğrenci-editörlü kaynaklar elenir |
| OpenAlex bütçesi düşük | 429 yemeden önce atlanır, sebebi raporlanır |
| Her zaman | DOAJ omurga (o ülkede hiç dergisi yoksa hariç) |

`source="doaj,hal"` veya `source="all"` ile override edilir.

---

## 3b. ⚠️ SORGU DİLİ — en sık yapılan hata

İndeksler makalenin **kendi dilindeki** kelimeleri eşler, çeviri yapmaz.
Canlı doğrulama:

| Sorgu | Brezilya (BR) sonucu |
|---|---|
| `force majeure` (EN) | **0** |
| `força maior` (PT) | 2 |
| `caso fortuito` (PT) | 2 — *"Risco da empresa e caso fortuito externo"* |

**Kural:** İngilizce olmayan bir yargı çevresinde arama yaparken kavramı o
ülkenin **hukukî terimiyle** yaz — birebir çeviri değil:

| Yargı çevresi | Terim |
|---|---|
| BR / PT | `caso fortuito`, `força maior` |
| ES / LatAm | `fuerza mayor`, `caso fortuito` |
| FR | `force majeure`, `imprévision` |
| DE | `höhere Gewalt`, `Wegfall der Geschäftsgrundlage` |
| TR | `mücbir sebep`, `aşırı ifa güçlüğü`, `uyarlama` |

Boş dönen bir grup **"bu dilde bulunamadı"** demektir, **"literatür yok"**
demek değildir. Hangi terimi aradığını belirt ve başka terimle tekrar dene.
Adil karşılaştırma için `compare_jurisdictions`'ı tek İngilizce sorguyla değil,
**dil grubu başına bir kez** çalıştır.

---

## 4. Tipik kullanım

```
search_legal_scholarship("energy charter treaty", peer_reviewed_only=true)
search_legal_scholarship("stabilization clause")
search_legal_scholarship("mücbir sebep uyarlama", language="tr")   # → DergiPark
compare_jurisdictions("force majeure", ["FR","BR","ID","TR"])
search_legal_scholarship("arbitraje de inversiones", jurisdiction="ES")
search_legal_scholarship("oil law", jurisdiction="AZ")   # DOAJ'da yok → OpenAlex
get_scholarship_fulltext("scielo", "<PID>", collection="scl")
resolve_doi("10.1093/jiel/jgaa002")
```

---

## 5. ATIF DİSİPLİNİ (zorunlu)

Her kayıt hazır bir **`citation`** alanı taşır → **BİREBİR kullan**:

```
[LexScholar - {indeks} - {yazar, başlık, dergi, yıl}] doi:{...}
```

- **`peer_reviewed` ÜÇ DURUMLU:**
  - `true` — indeks garanti ediyor (DOAJ yalnız hakemli OA dergileri listeler;
    HAL ve OpenAIRE açık bayrak taşır),
  - `false` — bilinen şekilde hakemli **değil**: preprint ve **ABD öğrenci
    editörlü law review**'ları,
  - `null` — bilinmiyor.
  `false` veya `null` olanı **asla** "hakemli araştırma" diye sunma.
- Araç döndürmediyse kaynak **UYDURMA** → `[model bilgisi - doğrulayın]`.
- Yazarın görüşünü **yazara atfet** ("[Yazar]'a göre…"), "hukuk şöyle der"
  diye sunma.
- Öğreti **argümandır, otorite değildir.** Mevzuatla çelişirse birincil kaynak
  üstündür; çelişkiyi **raporla**, makale lehine çözme.
- Güncellik: eski bir makale bir değişikliği öncelemiş olabilir — kanunun
  yürürlükteki metnini birincil araçla teyit et.
- Çıktılar **hukuki tavsiye değildir**.

---

## 6. Lisans / uyum

- **DOAJ `robots.txt`: `ai-train=no`.** API/OAI ayrı belgelenmiş makine
  arayüzleridir ve metadata CC0 → **getir-ve-atıf-ver uyumlu; model eğitimi
  HAYIR**.
- **Dialnet `dc:rights`:** çoğaltma için **açık yazılı izin** şart → yalnız
  keşif/atıf, yeniden yayım yok. Sunucu bunu zaten "discovery only" kurar.
- **Law Review Commons:** `robots.txt` genel ajanlara `/do/` yolunu kapatır;
  içerik öğrenci editörlüdür (hakemli değil).
- **DergiPark:** resmî OAI-PMH ucu kullanılır; sitenin `/search` yolu
  `robots.txt` ile kapalıdır ve **kazınmaz**.
- Kısa alıntı + atıf; **toplu çoğaltma yok**.
- Kuruma ait gizli taslakları bu araca **yapıştırma** — public literatür
  aramasıdır.

---

## 7. Diğer rehberlerle ilişki

| İhtiyaç | Kaynak |
|---|---|
| **Türk** doktrini / akademik makale | **bu MCP** (DergiPark 19 dergi + DOAJ TR 20) |
| **Türkiye dışı + karşılaştırmalı** doktrin | **bu MCP** + `/legal-research:karsilastirmali-doktrin` |
| TR mevzuat / içtihat | `mevzuat-mcp-rehberi.md`, `yargi-mcp-rehberi.md` (BİRİNCİL) |
| AZ mevzuatı | `eqanun-mcp-rehberi.md` (BİRİNCİL) |
| İmzalı sözleşme emsali (PSA/JOA) | `resourcecontracts-rehberi.md` |
| İsviçre içtihadı/doktrini | `switzerland-caselaw-rehberi.md` (OpenCaseLaw.ch) — **zaten var, tekrar kurma** |
| ABD içtihadı | `courtlistener-rehberi.md` |

---

## 8. Sınırlamalar

- **İkincil/karşılaştırmalı** kaynak — hukuki sonucun nihai dayanağı olamaz.
- Bazı yargı çevrelerinde açık erişimli hukuk dergisi **hiç yok** (AZ, IN, JP,
  AE) → yalnız OpenAlex üzerinden dolaylı erişim.
- **Adanmış açık erişim enerji hukuku dergisi yok** — enerji hukuku genel
  dergilere dağılmıştır; konu bazlı arama, dergi bazlı filtrelemeyi yener.
- OAI tabanlı indekslerde (SciELO, Dialnet, Law Review Commons, DergiPark)
  sunucu tarafı serbest metin arama yok → tarama sınırlıdır; yanıt ne kadar
  tarandığını (`scanned`) söyler.
- OpenAlex **ölçülü**: anahtarsız ~100 arama/gün. Key yoksa router onu korur.
- SciELO koleksiyon bazlı: `scielo.br` tam metin verir, `scielo.cl`
  Cloudflare'lıdır.
- Her araç çağrısı **100 saniyede iptal edilir**. Geniş bir
  `compare_jurisdictions` çağrısı bu limite girebilir → ülke sayısını azalt,
  `limit`i düşür, `jurisdiction` set et. İptal olursa aynı sorguyu tekrarlama;
  böl ve **kapsamın daraldığını söyle**.

---

## Versiyon disiplini

- Bu rehber **v1.4.0** (*LC Digital Twin MCP Senkronu*) ile eklendi.
- DergiPark, 25.07.2026'da üçüncü taraf scraper yerine resmî OAI-PMH ucuyla bu
  sunucunun içine alındı; ayrı bir DergiPark connector'ı **gerekmez**.

---

*Son güncelleme: 26.07.2026 — v1.4.0. LexScholar MCP — self-hosted,
bağımlılıksız, auth'suz. Companion skill: `skills/legal-research__skills.md` →
`/legal-research:karsilastirmali-doktrin`.*
