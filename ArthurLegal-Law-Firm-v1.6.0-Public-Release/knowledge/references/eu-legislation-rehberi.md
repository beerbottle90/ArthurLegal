# AB Mevzuatı & CJEU/ECHR İçtihatı — Kullanım Rehberi (v1.7.0)

> **Erişim tipi:** WebFetch (GET) — MCP gerekmez
> **Auth:** Yok (EUR-Lex doğrudan erişim)
> **Kapsam:** Tüm AB tüzükleri, direktifler, CJEU kararları, ECHR içtihadı
> **[Müvekkil] bağlamı:** [BORU HATTI PROJESİ] AB bağlantısı, GDPR, AB yaptırım rejimleri, enerji direktifleri

---

## 1. EUR-Lex — CELEX numarasıyla doğrudan erişim

> 🔴 **KRİTİK DÜZELTME (30.08.2026):** `eur-lex.europa.eu` sayfaları **WebFetch ile
> kullanılamaz.** `legal-content/{DIL}/TXT/?uri=CELEX:...`, `.../TXT/HTML/?uri=...`,
> `search.html?...` ve `eli/...` yollarının **hepsi** JS kabuğu döndürüyor: gelen içerik
> istenen mevzuat değil, **Resmî Gazete tarih indeksi** oluyor. Test edilen örnekler —
> GDPR (`32016R0679`), Direktif 2019/944, `search.html?text=LNG+terminal+licensing`,
> `eli/dir/2019/944/oj/ron` — hiçbiri belge metni vermedi.
>
> **Bu bölümdeki `eur-lex.europa.eu` URL'lerini çağırma.** Aşağıdaki CELLAR zincirini
> kullan; canlı doğrulandı ve gerçek metni döndürüyor.

### ✅ Çalışan yol — CELLAR üç adımı (30.08.2026 doğrulandı)

```
# ADIM 1 — CELEX'ten Cellar UUID'si (WebFetch 303 döner, redirect URL'sinden UUID'yi al)
WebFetch: https://publications.europa.eu/resource/celex/{CELEX_NO}
       → 303 → http://publications.europa.eu/resource/cellar/{UUID}/rdf/object/full

# ADIM 2 — istenen DİLİN manifestation URI'sini SPARQL ile çöz
#          lang: ENG · DEU · FRA · ITA · RON · ELL · POL · NLD ...
PREFIX cdm:  <http://publications.europa.eu/ontology/cdm#>
PREFIX lang: <http://publications.europa.eu/resource/authority/language/>
SELECT ?manif WHERE {
  ?work cdm:resource_legal_id_celex "{CELEX_NO}"^^<http://www.w3.org/2001/XMLSchema#string> .
  ?expr cdm:expression_belongs_to_work ?work ;
        cdm:expression_uses_language lang:{DIL} .
  ?manif cdm:manifestation_manifests_expression ?expr .
} LIMIT 5

# ADIM 3 — tam metni çek
WebFetch: {manifestation_uri}/DOC_1
```

**Doğrulanmış örnekler:**

| Belge | Manifestation | Sonuç |
|---|---|---|
| GDPR (EN) | `.../cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0006.03/DOC_1` | ✅ gerçek metin |
| Dir. 2019/944 (RO) | `.../cellar/8594f013-8e7c-11e9-9369-01aa75ed71a1.0020.03/DOC_1` | ✅ "DIRECTIVA (UE) 2019/944..." |

⚠️ **Uzun metin uyarısı:** WebFetch'in kendi boyut sınırı, GDPR gibi uzun tüzüklerde
metni **başlangıç bölümünde (Recital'lerde) kesiyor** — belirli bir maddeye inmek
istiyorsan DOC_1 tek başına yetmeyebilir. O durumda:
- **konsolide** CELEX'i dene (`0` sektörü, ör. `02016R0679-20160504`) — parçalı gelir;
- ya da maddeyi kullanıcıdan iste / ikincil kaynaktan (doktrin) teyitle;
- **asla madde metnini hafızadan yazma.**

*(Aşağıdaki tablo CELEX numaraları için geçerlidir — URL deseni değil, numara referansı.)*

**[Müvekkil] için kritik AB mevzuatı:**

| Mevzuat | CELEX | Konu |
|---|---|---|
| GDPR | `32016R0679` | Kişisel veri (10.000+ çalışan, AB iletişimi) |
| AI Act | `32024R1689` | Yapay zeka sistemleri (2025 yürürlük) |
| NIS2 Direktifi | `32022L2555` | Siber güvenlik (enerji altyapısı — kritik) |
| DORA | `32022R2554` | Dijital operasyonel dayanıklılık (finans/enerji) |
| AB Taksonomi (enerji) | `32021R2139` | Sürdürülebilir enerji sınıflandırması |
| EU ETS | `32003L0087` | Emisyon ticaret sistemi ([RAFİNERİ]) |
| 3. Enerji Paketi — Gaz | `32009L0073` | [BORU HATTI PROJESİ]'a uygulanabilir AB gaz direktifi |
| 3. Enerji Paketi — Elektrik | `32009L0072` | [ELEKTRİK ÜRETİM İŞTİRAKİ] için AB elektrik direktifi |
| Gaz Güvenliği Yönetmeliği | `32017R1938` | Tedarik güvenliği ([BORU HATTI PROJESİ] güzergâhı) |
| Russia Sanctions (son) | `32022R0428` | AB Rusya yaptırımları (temel tüzük) |
| TFEU (Rekabet m.101/102) | `12012E/TXT` | AB rekabet hukuku |

**Örnek (düzeltilmiş — CELLAR zinciri):**
```
1) WebFetch: https://publications.europa.eu/resource/celex/32016R0679
   → UUID: 3e485e15-11bd-11e6-ba9a-01aa75ed71a1
2) SPARQL (lang:ENG) → .../cellar/3e485e15-...-01aa75ed71a1.0006.03
3) WebFetch: http://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0006.03/DOC_1
```
❌ **Şunu kullanma:** `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679`
— OJ indeksi döner, GDPR metni gelmez (30.08.2026 doğrulandı).

---

## 2. EUR-Lex Arama (konu bazlı)

❌ **`eur-lex.europa.eu/search.html` WebFetch ile çalışmaz** — OJ tarih indeksi döner
(30.08.2026 doğrulandı, `text=LNG+terminal+licensing` ile test edildi).

**✅ Çalışan alternatifler:**

```
# (a) CELLAR SPARQL ile başlık/konu araması — birincil
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?work ?celex ?title WHERE {
  ?work cdm:resource_legal_id_celex ?celex ;
        cdm:work_date_document ?date .
  ?expr cdm:expression_belongs_to_work ?work ;
        cdm:expression_title ?title .
  FILTER(CONTAINS(LCASE(STR(?title)), "lng"))
} LIMIT 20
```

```
# (b) CELEX'i başka yoldan öğren, sonra bölüm 1'deki zinciri kullan:
#     - LexScholar MCP (doktrin, AB mevzuatına atıf verir)
#     - Bu rehberin CELEX tablosu (aşağıda)
#     - Kullanıcıdan CELEX/başlık iste
```

> **Kural:** CELEX numarası doğrulanmadan AB mevzuatına atıf verme. "Muhtemelen
> 32024R1689'dur" tarzı tahmin yasaktır — SPARQL ile doğrula ya da sor.

---

## 3. CJEU Kararları (EUR-Lex üzerinden)

CJEU kararları EUR-Lex'te CELEX formatıyla indekslenmiştir:
- Format: `6{YIL}CJ{DAVA_NO}` (ör. `62019CJ0715`)
- ❌ `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:6{YIL}CJ{DAVA_NO}`
  **çalışmaz** (OJ indeksi döner)
- ✅ Bölüm 1'deki **CELLAR üç adımını** aynen uygula — CJEU kararları da `cdm:` ontolojisinde
  work olarak modellenmiştir, aynı zincir geçerlidir.

Belirli kararı bulmak için InfoCuria arama:
```
WebFetch("https://curia.europa.eu/juris/liste.jsf?language=en&td=ALL&text={query}",
         "Enerji piyasası rekabet kararlarını listele")
```

---

## 4. ECHR — HUDOC (Avrupa İnsan Hakları Mahkemesi)

**İstanbul Sözleşmesi, mülkiyet hakkı (P1-1), adil yargılanma (m.6) [Müvekkil] için ilgili.**

```
GET https://hudoc.echr.coe.int/app/query/results?query=contentsitename:ECHR+AND+doctypebranch:JUDGMENTS+AND+article:P1-1&select=itemid,docname,judgementdate&sort=judgementdate+Descending
```

Belirli karar: Bir davayı bulduktan sonra tam metin:
```
WebFetch("https://hudoc.echr.coe.int/eng#{itemid}", "Kararın özeti ve gerekçesi")
```

---

## 5. AB Yaptırım Listesi (konsolide)

OpenSanctions zaten aktif (isim taraması için **birincil** araç odur).

⚠️ **`sanctionsmap.eu/api/v1/sanction` diye bir endpoint YOK — 404** (30.08.2026).
Ayrıca sanctionsmap bir **isim arama API'si değildir**; ülke/rejim haritası ve filtre
meta verisi döndürür.

**Çalışan AB kaynakları (30.08.2026 test ✅):**

```
# 1) AB konsolide mali yaptırım listesi (FSF) — İSİM TARAMASI İÇİN DOĞRU KAYNAK
#    Kamuya açık token, ek auth yok. CSV veya XML.
https://webgate.ec.europa.eu/fsd/fsf/public/files/csvFullSanctionsList_1_1/content?token=dG9rZW4tMjAxNw
https://webgate.ec.europa.eu/fsd/fsf/public/files/xmlFullSanctionsList_1_1/content?token=dG9rZW4tMjAxNw

# 2) Rejim/ülke haritası ve yürürlükteki tedbir tipleri (isim araması DEĞİL)
https://www.sanctionsmap.eu/api/v1/data?include_draft=0&lang=en
https://www.sanctionsmap.eu/api/v1/regime?lang=en
```

> **Sıralama:** isim/varlık taraması → **OpenSanctions** (`opensanctions-rehberi.md`);
> "hangi AB tüzüğü hangi ülkeye hangi tedbiri koyuyor" → sanctionsmap `/data`;
> resmî liste kaydının birebir doğrulanması → FSF CSV/XML.

---

## Atıf formatı

```
[EU Legislation — CELEX:{no} — GG.AA.YYYY]
[CJEU — {Dava adı, C-no/YIL} — GG.AA.YYYY]
[ECHR — {Dava adı} — GG.AA.YYYY]
```

---

## Sınırlamalar

- EUR-Lex HTML çıktısı uzun olabilir; belirli madde numarası istenerek daralt
- CJEU kararları Fransızca/İngilizce; makine çevirisi için Claude'dan yardım al
- ECHR HUDOC resmi API değil, endpoint değişebilir

*Son güncelleme: 29.05.2026 — v1.7.0. EUR-Lex + CJEU + ECHR WebFetch entegrasyonu.*
