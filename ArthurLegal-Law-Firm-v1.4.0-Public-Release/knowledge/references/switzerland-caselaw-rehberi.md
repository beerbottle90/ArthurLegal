# İsviçre Hukuku & İçtihadı — Kullanım Rehberi (v1.7.0)

> **Erişim tipi:** OpenCaseLaw.ch MCP (33 araç, auth yok) + Fedlex WebFetch
> **Auth:** Yok — tüm kaynaklar tamamen açık
> **Kapsam:** 972.000+ İsviçre federal + kanton kararı; tüm federal mevzuat
> **[Müvekkil] bağlamı:** ICC/Swiss arbitration, İsviçre holdingler, Swiss OR sözleşmeleri

---

## 1. OpenCaseLaw.ch MCP — İsviçre İçtihadı

**MCP endpoint: `https://mcp.opencaselaw.ch/sse`**
**REST endpoint: `https://mcp.opencaselaw.ch/api/`**
**33 MCP aracı, CC0 lisans, günlük güncelleme, auth yok.**

Kapsam:
- Federal Yüksek Mahkeme (BGer/TF) — tüm daireler
- Federal İdare Mahkemesi (BVGer)
- Federal Ceza Mahkemesi (BStGer)
- Tüm 26 kanton mahkemeleri
- Fedlex mevzuat entegrasyonu

**MCP araçları (seçili):**
- `search_cases` — anahtar kelime/konu araması
- `get_case` — belirli karar tam metin
- `search_by_statute` — belirli kanun maddesine göre karar
- `get_related_cases` — atıf ağı
- `search_arbitration` — tahkim kararları

**WebFetch ile REST kullanımı:**
```
WebFetch("https://mcp.opencaselaw.ch/api/v1/search?q=ICC+arbitration+energy&lang=de",
         "Enerji sektörü ICC tahkim kararları")

WebFetch("https://mcp.opencaselaw.ch/api/v1/search?q=force+majeure+Liefervertrag&court=bger",
         "BGer force majeure LNG/enerji tedarik sözleşmesi kararları")
```

---

## 2. Fedlex — İsviçre Federal Mevzuatı

**Federal Şansölye resmi platformu. SPARQL + doğrudan URI. Auth yok.**

```
GET https://www.fedlex.admin.ch/eli/cc/{SR_numarası}/en
GET https://www.fedlex.admin.ch/eli/cc/{SR_numarası}/de
```

**[Müvekkil] için kritik İsviçre mevzuatı:**

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

**Örnek — IPRG m.176 (tahkim sözleşmesi geçerlilik):**
```
WebFetch("https://www.fedlex.admin.ch/eli/cc/1988/1776_1776_1776/en",
         "IPRG m.176 uluslararası tahkim sözleşmesinin geçerlilik şartları")
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

## [Müvekkil] için özel notlar

- **Swiss OR** — İsviçre'de kurulan holding yapıları için standart sözleşme hukuku
- **IPRG m.176-194** — ICC Tahkim Kuralları ile birlikte; Geneva seat ICC tahkiminde İsviçre tahkim hukuku uygulanır
- **Swiss GmbH/AG** — [Müvekkil]'ın Avrupa'daki olası holding yapısı için
- **nDSG (yeni DSG)** — Eylül 2023 yürürlüğe girdi; GDPR'a benzer ama ayrı rejim
- **FINMA** (finansal düzenleyici) kararları: `https://www.finma.ch/en/enforcement/`

*Son güncelleme: 29.05.2026 — v1.7.0. OpenCaseLaw.ch MCP + Fedlex WebFetch entegrasyonu.*
