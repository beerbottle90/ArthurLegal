# MCP Yol Haritası — kanıta dayalı üretim sırası

> **Statü:** planlama belgesi. Buradaki sıralama **tahmin değil**, 30.08.2026'da
> yapılan canlı endpoint testlerinin sonucudur. Her satırın gerekçesi, o yargı
> çevresinin rehberinde doğrulanmış test çıktısına dayanır.
> **Sürüm:** v1.6.0 ile eklendi.

---

## Neden MCP? — üç somut kısıt

WebFetch'in bu pakette karşılaştığı, **rehber yazarak çözülemeyen** üç kısıt var.
MCP sunucusu üçünü de çözer, çünkü sunucu **kendi egress'inden ve kendi HTTP
istemcisiyle** çalışır:

| Kısıt | Somut örnek (doğrulandı) | MCP çözer mi? |
|---|---|---|
| **1. Özel HTTP başlığı gönderilemez** | ES konsolide mevzuat API'si `Accept: application/xml` şart koşuyor; başlıksız **400**. CourtListener `citation-lookup/` `Authorization: Token` istiyor; **401**. | ✅ evet |
| **2. Egress engeli** | `legislatie.just.ro` (RO) bağlantıyı düşürüyor; `gesetze-im-internet.de` (DE) erişilemiyor. Ama de-eli MCP'nin `de_rii_*` araçları aynı siteyi **sorunsuz** çekiyor — kanıt burada. | ✅ evet |
| **3. Kaynakta arama yok** | NL Rechtspraak açık API'sinde **serbest metin araması yok** ve tanınmayan parametreleri sessizce yok sayıyor (3.751.381 karar, hepsi filtresiz dönüyor). IE ve LU'da arama endpoint'i hiç yok. | ✅ evet — kendi indeksiyle |

**Semantik arama** üçüncü kısıtın üstüne gelen katmandır: kaynak yalnız anahtar
kelime veriyorsa bile, MCP kendi embedding indeksini kurup *"tedarik sözleşmesinde
mücbir sebep nedeniyle fesih"* gibi bir soruyu kavramsal olarak eşleştirebilir.

---

## Sıra — etki / emek oranına göre

### 🥇 1. `nl-rechtspraak-mcp` — en yüksek getirili

| | |
|---|---|
| **Neden** | 3.751.381 karar **var** ama **aranamıyor**. Kaynak açık, ücretsiz, ECLI'li — eksik olan tek şey arama katmanı. Boşluk tam olarak MCP'nin doldurduğu boşluk. |
| **Kaynak** | `data.rechtspraak.nl/uitspraken/zoeken` (yapılandırılmış) + `/content?id={ECLI}` (tam metin) + `/Waardelijst/*` (sözlükler) — hepsi ✅ 200 |
| **MCP'nin katacağı** | (a) tam metin + **semantik** arama · (b) `rechtsgebied`/`instantie` ile birleşik filtre · (c) ECLI atıf sözleşmesi (`citation` alanı hazır dönsün) |
| **İş kalemi** | Toplu indirme (`zoeken` sayfalama) → yerel indeks → BM25 + embedding hibrit → `search_decisions` / `get_decision` araçları |
| **Risk** | 3,7 M belge indekslemek ciddi disk/işlem ister; **tarih penceresiyle başla** (ör. son 15 yıl) |
| **Referans** | `hollanda-hukuku-rehberi.md` |

### 🥈 2. `ro-legislatie-mcp` — tıkalı yargı çevresini açar

| | |
|---|---|
| **Neden** | Romanya'nın **tek** ücretsiz konsolide kaynağı bu ortamdan erişilemiyor. Şu an RO için elimizde yalnız EUR-Lex (AB-türevli) var; saf ulusal mevzuat kapsanmıyor. |
| **Kanıt** | `legislatie.just.ro` — TLS kuruluyor, istek gidiyor, sunucu `close_notify` göndermeden kapatıyor. İkinci bağımsız egress'ten "HTTP/2 framing layer" hatası. **cdep.ro / scj.ro / idrept.ro** da erişilemez, **ccr.ro** 503. |
| **⚠️ ÖN KOŞUL** | **Önce erişimi doğrula.** Sunucu adayı (Hetzner/Railway/RO VPS) üzerinden `curl https://legislatie.just.ro/Public/DetaliiDocument/109884` çalışıyor mu? **Çalışmıyorsa bu maddeyi başlatma** — MCP her egress engelini çözmez, yalnız *bizim* egress'imize özgü olanı çözer. |
| **Referans** | `romanya-hukuku-rehberi.md` bölüm 1b |

### 🥉 3. `es-boe-mcp` — küçük emek, temiz kazanç

| | |
|---|---|
| **Neden** | Sorun tek bir HTTP başlığı. `Accept: application/xml` gönderebilen herhangi bir istemci ES **konsolide** mevzuatının tamamına erişiyor. |
| **Kanıt** | `Accept: application/xml` → `BOE-A-2010-10544` (Ley de Sociedades de Capital) **200** ✅ · başlıksız / `application/json` → **400** ❌ |
| **İş kalemi** | İnce bir sarmalayıcı: `get_consolidated_act(boe_id)`, `get_document(boe_id)`, `get_daily_summary(date)`. İndeks bile gerekmez. |
| **Emek** | **En düşük** — bir günlük iş |
| **Referans** | `ispanya-hukuku-rehberi.md` bölüm 2 |

### 4. `eli-search-mcp` — LU + IE ortak arama katmanı

| | |
|---|---|
| **Neden** | İkisinde de **belge URL'leri mükemmel** (ELI, madde düzeyinde) ama **arama yok**. Aynı problem, aynı çözüm → **tek sunucu, iki yargı çevresi**. |
| **Kanıt** | LU `.../consolide/20230101` ✅ · IE `/eli/2014/act/38/section/1/enacted/en/html` ✅ · IE `/search` **404**, LU `api/v1` **401** |
| **İş kalemi** | Dizinleri tara (LU `/search`, IE `/eli/acts.html`) → başlık + metin indeksi → semantik arama → mevcut ELI URL'sine yönlendir |
| **Not** | AT/PL/FI'yi de aynı sunucuya eklemek mümkün ama **gerek yok** — onların kendi API'leri zaten arama yapıyor |

### 5. AT · PL · FI — **şimdilik MCP YAZMA**

Üçünün de resmî API'si arama dahil her şeyi yapıyor:

| Ülke | Doğrulanmış yetenek |
|---|---|
| **AT** | RIS OGD v2.6 — mevzuat `Suchworte=Aktiengesetz` → 1.423 hit · içtihat `Konkurrenzklausel` → 148 hit ✅ |
| **PL** | Sejm ELI — `search?title=` ✅ · statü alanı (`obowiązujący`) ✅ · `text.html`/`text.pdf` ✅ |
| **FI** | Finlex Akoma Ntoso REST — `/list`, `/{yıl}`, `main.akn` ✅ |

> **Karar:** Rehber yazmak yeterli. MCP yalnızca **semantik arama** istendiğinde
> ve yukarıdaki 1–4 bittikten sonra gündeme gelir. Erken optimizasyon yapma.

---

## Semantik arama — ortak tasarım notu

1–4 arasındaki her sunucu aynı iskeleti paylaşmalı ki bakım tek noktada kalsın:

```
search(query, filters, mode="hybrid")
  ├─ BM25 / FTS5            → tam terim eşleşmesi (madde no, taraf adı, docket)
  ├─ embedding (kosinüs)    → kavramsal eşleşme (dil-içi)
  └─ RRF ile birleştir      → tek sıralı liste
```

**Dil uyarısı — bu paket için kritik:** kullanıcı Türkçe sorar, kaynak Felemenkçe /
Lehçe / Fince'dir. İki seçenek:
- **(a)** çok dilli embedding modeli (tercih) — Türkçe sorgu, Felemenkçe belgeyi bulur;
- **(b)** sorguyu hedef dile çevirip öyle ara — daha ucuz, terim kaybı riski var.

**Atıf sözleşmesi — pazarlık dışı.** Her sunucu, mevcut MCP'lerin (de-eli,
OpenCaseLaw.ch, e-qanun) kuralını izlemeli: yanıt **hazır bir `citation` alanı**
taşısın, model atıf dizesini **asla kendisi kurmasın**. Ayrıca `source_url` ve —
varsa — **statü/konsolidasyon tarihi** dönsün. Bu, paketteki "kaynaksız hukuk yok"
ilkesinin teknik karşılığıdır.

---

## Mevcut MCP'lerin sağlık durumu (30.08.2026 canlı test)

| MCP | Test | Sonuç |
|---|---|---|
| YargiMCP (TR) | `mevzuat_no=6698` · `+"rekabet yasağı" +"cezai şart"` | ✅ KVKK + 801 karar |
| e-qanun (AZ) | `search_acts("Mülki Məcəllə")` | ✅ 623 akt |
| OpenCaseLaw.ch | `Konkurrenzverbot…` court=bger | ✅ 57+ karar, pinpoint E. |
| Fedlex (CH) | `search_by_title("Obligationenrecht")` | ✅ RS 220 |
| de-eli (DE) | `de_search("Lieferkettensorgfaltspflichtengesetz")` | ✅ LkSG + ELI |
| CourtListener (US) | NY Convention araması | ✅ 242 opinion |
| LexScholar | TR rekabet yasağı | ✅ dergipark+doaj+openalex |
| ResourceContracts | `country=az`, Hydrocarbons | ✅ 16 PSA |

⚠️ **sbirka-mcp (CZ)** — endpoint canlı ama **401**; connector yetkilendirilmeden
Çekya rehberi çalışmaz.

---

*Oluşturuldu: 30.08.2026 — v1.6.0. Sıralama, v1.6.0 denetimindeki canlı endpoint
testlerine dayanır; yeni test yapıldıkça güncellenmelidir.*
