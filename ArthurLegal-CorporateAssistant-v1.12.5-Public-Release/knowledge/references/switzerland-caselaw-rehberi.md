# İsviçre Hukuku & İçtihadı — Kullanım Rehberi (v1.7.0)

> **Erişim tipi:** OpenCaseLaw.ch MCP (42 araç, auth yok) + Fedlex WebFetch
> **Auth:** Yok — tüm kaynaklar tamamen açık
> **Kapsam:** 1.050.000+ İsviçre federal + kanton kararı; tüm federal mevzuat
> **[ŞİRKET ADI] bağlamı:** ICC/Swiss arbitration, İsviçre holdingler, Swiss OR sözleşmeleri

---

## 1. OpenCaseLaw.ch MCP — İsviçre İçtihadı

**MCP endpoint: `https://mcp.opencaselaw.ch/sse`** ✅ (30.08.2026 test)
**42 MCP aracı, CC0 lisans, günlük güncelleme, auth yok.**

> ⚠️ **REST/WebFetch yedeği YOK.** v1.5.0'a kadar burada
> `https://mcp.opencaselaw.ch/api/` diye bir REST endpoint'i yazıyordu — **böyle bir
> şey yok**: `/api`, `/api/v1/search`, `/api/v1/decisions`, `/openapi.json`, `/docs`
> yollarının **hepsi 404** (30.08.2026 doğrulandı). Yalnızca `/sse` yaşıyor.
> **Connector eklenmemişse İsviçre içtihadına erişim yoktur** — bu durumda tahmin
> yürütme, aşağıdaki adımları izle.

Kapsam:
- Federal Yüksek Mahkeme (BGer/TF) — tüm daireler
- Federal İdare Mahkemesi (BVGer)
- Federal Ceza Mahkemesi (BStGer)
- Tüm 26 kanton mahkemeleri
- Fedlex mevzuat entegrasyonu

**MCP araçları (seçili):**
- `search_decisions` — anahtar kelime/konu araması (dosya numarasıyla da)
- `get_decision` — belirli kararın tam metni
- `find_leading_cases` — konuya ya da kanun maddesine (`law_code` + `article`) göre en çok atıf alan kararlar
- `find_citations` — atıf ağı (kararın andıkları ve kararı ananlar)
- `find_appeal_chain` — kanun yolu zinciri (alt ve üst derece kararları)
- Tahkim için ayrı araç yoktur; tahkim kararları `search_decisions` ile aranır

**Connector yoksa ne yapılır:**

1. **Söyle:** "İsviçre içtihat araması için OpenCaseLaw.ch connector'ı gerekiyor:
   Settings → Connectors → Add custom connector → `https://mcp.opencaselaw.ch/sse`,
   auth: None."
2. **İsviçre *mevzuatı*** için fedlex-connector MCP (bölüm 2a) gerekir; Fedlex `eli/cc` sayfaları
   WebFetch'te içerik vermez (bölüm 2 erişim notu).
3. **AB-türevli İsviçre uygulaması** için EUR-Lex karşılaştırması yapılabilir
   (`eurlex-cellar-rehberi.md`).
4. ⚠️ **BGE/BGer atıfını asla elle kurma.** R1 kuralı: atıf dizesi yalnızca `cite` aracının
   döndürdüğü `citation_string` (`citation_string_de` / `_fr` / `_it`) alanından birebir kopyalanır. Connector yokken
   "muhtemelen BGE 4A_..." tarzı tahmin **yasaktır**.

---

## 2. Fedlex — İsviçre Federal Mevzuatı

**Federal Şansölye resmi platformu. SPARQL + doğrudan URI. Auth yok.**

> ⚠️ **ERİŞİM NOTU (08.06.2026 test):** Fedlex `eli/cc/...` sayfaları **SPA (JavaScript)** —
> doğrudan WebFetch "yalnızca JS-özellikli tarayıcıda erişilebilir" uyarısı döndürüyor,
> içerik gelmiyor. **Mevzuat için iki çözüm:**
> 1. **fedlex-connector MCP** (aşağıda 2a) — Fedlex'i SPARQL üzerinden sarmalayan hosted
>    connector, DE/FR/IT mevzuat tam metni ✅
> 2. **OpenCaseLaw.ch MCP** — içtihat + bağlı mevzuat (zaten çalışıyor ✅)
> Fedlex doğrudan `eli/cc` URI yalnızca JS-özellikli erişimde yedek.

### 2a. fedlex-connector MCP — İsviçre Mevzuatı (hosted, kurulum kolay)

İsviçre federal mevzuatını (Classified Compilation — SR/RS) Fedlex SPARQL üzerinden
sunan hosted MCP. **Kurulum yok — sadece connector ekle.** DE/FR/IT madde/kanun arama.
Endpoint canlı (08.06.2026 ✅).

- **Claude Code:** `claude mcp add --transport http Fedlex-Connector https://mcp.fedlex-connector.ch`
- **Claude.ai Projects:** Customize → Connectors → + Add → URL: `https://mcp.fedlex-connector.ch`
  (auth yok)
- **Atıf:** `[CH Mevzuat — Fedlex (fedlex-connector MCP) — SR:{no} Art.{no} — GG.AA.YYYY]`

> **Alternatif (Claude Code, self-host):** `Ansvar-Systems/switzerland-law-mcp` — 4.873
> İsviçre federal kanunu, SPARQL census tabanlı, DE/FR/IT. Python self-host.
>
> **Kapsama mantığı:** OpenCaseLaw.ch = **içtihat** (1.050.000+ karar) · fedlex-connector =
> **mevzuat** (SR/RS). İkisi birlikte İsviçre hukukunu tam kapsar.

```
GET https://www.fedlex.admin.ch/eli/cc/{SR_numarası}/en
GET https://www.fedlex.admin.ch/eli/cc/{SR_numarası}/de
```

**[ŞİRKET ADI] için kritik İsviçre mevzuatı:**

| Mevzuat | SR No | Konu |
|---|---|---|
| OR (Obligationenrecht — Borçlar) | `220` | Sözleşme hukuku (Swiss OR) |
| ZGB (Zivilgesetzbuch — Medeni) | `210` | Genel medeni hukuk |
| SchKG (İcra ve İflas) | `281.1` | Alacak takibi |
| IPRG (Uluslararası Özel Hukuk) | `291` | **m.176-194: İsviçre tahkim hukuku (ICC/CAS)** |
| KG (Kartellgesetz — Rekabet) | `251` | Rekabet hukuku |
| GwG (Kara para aklama) | `955.0` | AML uyumu |
| Energiegesetz | `730.0` | Enerji kanunu |
| Elektrizitätsgesetz | `734.0` | Elektrik piyasası |
| DSG (Veri koruma) | `235.1` | İsviçre veri koruma kanunu (nDSG) |

**Örnek — IPRG m.176 (tahkim sözleşmesi geçerlilik):** madde metni fedlex-connector MCP (bölüm 2a) ile
alınır. Aşağıdaki adres yalnız JS destekli tarayıcıda açılır; WebFetch içerik vermez:
```
https://www.fedlex.admin.ch/eli/cc/1988/1776_1776_1776/en
```

---

## 3. Fedlex SPARQL — Gelişmiş Mevzuat Araması

```
POST https://fedlex.data.admin.ch/sparql
Content-Type: application/sparql-query
Accept: application/sparql-results+json
```

Veya GET ile URL-encoded sorgu:
```
WebFetch("https://fedlex.data.admin.ch/sparql?query=SELECT+?uri+?title+WHERE+{+?uri+rdfs:label+?title+.+FILTER(LANG(?title)='en')+FILTER(CONTAINS(STR(?title),'energy'))}&format=json",
         "Enerji alanındaki İsviçre kanunlarını listele")
```

---

## 4. BGer (Federal Yüksek Mahkeme) Doğrudan Erişim

Karar arama:
```
WebFetch("https://www.bger.ch/ext/eurospider/live/de/php/aza/http/index.php?lang=de&type=show_document&highlight_docid={DOC_ID}",
         "Karar özeti")
```

BGer kararı referansı formatı: `BGE {cilt} {daire} {sayfa}` (ör. BGE 148 III 105)

---

## Atıf formatı

```
[CH Mevzuat — {Kanun adı/SR} Art.{no} — Fedlex — GG.AA.YYYY]
[BGer — BGE {cilt} {daire} {sayfa} / {YILI}_{ESAS_NO} — GG.AA.YYYY]
[OpenCaseLaw.ch — {mahkeme} — {karar no} — GG.AA.YYYY]
```

---

## [ŞİRKET ADI] için özel notlar

- **Swiss OR** — İsviçre'de kurulan holding yapıları için standart sözleşme hukuku
- **IPRG m.176-194** — ICC Tahkim Kuralları ile birlikte; Geneva seat ICC tahkiminde İsviçre tahkim hukuku uygulanır
- **Swiss GmbH/AG** — [ŞİRKET ADI]'ın Avrupa'daki olası holding yapısı için
- **nDSG (yeni DSG)** — Eylül 2023 yürürlüğe girdi; GDPR'a benzer ama ayrı rejim
- **FINMA** (finansal düzenleyici) kararları: `https://www.finma.ch/en/enforcement/`

*Son güncelleme: 29.05.2026 — v1.7.0. OpenCaseLaw.ch MCP + Fedlex WebFetch entegrasyonu.*
