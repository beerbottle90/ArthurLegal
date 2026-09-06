# EUR-Lex Cellar — Kullanım Rehberi (SPARQL + REST / WebFetch yöntemi)

> **MCP durumu:** Birincil yol ArthurLegal MCP `eu_` araçlarıdır (aşağıdaki "ArthurLegal MCP"
> bölümü); CELLAR'ı sunucu tarafında sorgular. Aşağıdaki SPARQL ve WebFetch prosedürü yedek
> rotadır ve kimlik şemasını belgeler.
>
> **Durum:** ✅ Açık erişim — **API anahtarı gerekmez**, kayıt gerekmez. Birincil yargı
> çevresi Türkiye'dir; bu kaynak yalnızca AB hukuku (AB tüzük/direktifleri, CJEU içtihadı,
> hazırlık belgeleri) temas eden işlerde kullanılır (bkz. `karsilastirmali-hukuk-rehberi.md`).
> Genel EUR-Lex WebFetch prosedürü için `eu-legislation-rehberi.md` yedek yoldur.

---

## Cellar nedir?

**Cellar** — AB Yayın Ofisi'nin (Publications Office of the European Union) ortak
belge deposu. EUR-Lex'in arkasındaki yapılandırılmış veri katmanıdır: 2,7 milyondan
fazla "work" (eser) RDF olarak modellenmiş ve kalıcı tanımlayıcılarla erişilebilir.

**Kapsam:**
- Kurucu antlaşmalar (TEU, TFEU)
- Tüzükler (regulations) ve direktifler — hem OJ hâli hem konsolide metinler
- CJEU kararları (CELEX sektör 6)
- Hazırlık belgeleri (COM önerileri, görüşler — yasama tarihi)
- Tüm içerik 24 resmî dilde, çok formatlı (HTML, XML/Formex, PDF, RDF)

**ArthurLegal için neden gerekli?** Mevcut `eu-legislation-rehberi.md` EUR-Lex'in
HTML arayüzünü WebFetch ile kazır; bu çalışır ama tanımlayıcı disiplini elle kurulur.
Cellar ise her belgeye **kararlı CELEX/ELI URI'si** ve makine-okunur metadata verir:
"kaynaksız hukuk yok" ilkesinin istediği kaynak + tarih bilgisi, kazıma yerine
yapılandırılmış alandan gelir. GDPR, AI Act, NIS2, AB yaptırım tüzükleri gibi sık
başvurulan metinlerde sürüm ve kimlik belirsizliği ortadan kalkar.

---

## Endpoint / URI şeması

### 1. Public SPARQL endpoint (doğrulandı: 13.08.2026)

```
https://publications.europa.eu/webapi/rdf/sparql
```

- OpenLink Virtuoso (v8) sorgu editörü; auth yok, kayıt yok.
- GET parametreleri: `query={URL-encoded SPARQL}`, `format=` ile çıktı formatı
  (`application/sparql-results+json`, XML, CSV, Turtle, HTML).
- Ontoloji: **CDM** (`http://publications.europa.eu/ontology/cdm#`).
- Operatör iletişimi: `OP-CELLAR@ec.europa.eu`.

### 2. CELEX tabanlı Cellar resource URI (doğrulandı: 13.08.2026)

```
http://publications.europa.eu/resource/celex/{CELEX_NO}
```

Bu URI `303 See Other` ile ilgili work'ün kalıcı Cellar UUID kaydına yönlenir
(ör. GDPR → `.../resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1/...`).

⚠️ **Düzeltme (30.08.2026):** "varsayılan yönlendirmeyi izlemek yeterlidir" **yanlıştı**.
Format/dil seçimi `Accept` + `Accept-Language` başlıklarıyla yapılır ve **WebFetch başlık
gönderemez**; başlıksız yönlendirme RDF metadata'sına gider, **belge metnine değil**.

**Tam metne inmenin doğru yolu — üç adım (canlı doğrulandı):**

```
1) WebFetch: https://publications.europa.eu/resource/celex/{CELEX}
   → WebFetch cross-host redirect'i izlemez, sana 303 hedefini verir:
     http://publications.europa.eu/resource/cellar/{UUID}/rdf/object/full
   → buradan {UUID}'yi al

2) SPARQL ile o dilin manifestation URI'sini çöz:
   ?expr cdm:expression_uses_language lang:ENG   (RON, DEU, FRA, ITA, ELL, POL ...)
   ?manif cdm:manifestation_manifests_expression ?expr

3) WebFetch: {manifestation_uri}/DOC_1     ← gerçek tam metin
```

Doğrulanmış: GDPR EN → `.../3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0006.03/DOC_1` ✅;
Dir. 2019/944 RO → `.../8594f013-8e7c-11e9-9369-01aa75ed71a1.0020.03/DOC_1` ✅.

⚠️ Uzun tüzüklerde WebFetch metni Recital'lerde kesebilir — bkz.
`eu-legislation-rehberi.md` bölüm 1 "Uzun metin uyarısı".

### 3. ELI URI (doğrulandı: 13.08.2026)

```
http://data.europa.eu/eli/{tür}/{yıl}/{numara}/oj
```

`307` ile EUR-Lex'teki ELI sayfasına yönlenir (24 dil, HTML/PDF/düz metin).
Örnek: `http://data.europa.eu/eli/reg/2016/679/oj` → GDPR.

### CELEX sektör kodları (sık kullanılanlar)

| Sektör | Anlam | Örnek |
|---|---|---|
| `1` | Antlaşmalar | `12012E/TXT` (TFEU) |
| `3` | Mevzuat (tüzük `R`, direktif `L`) | `32016R0679` (GDPR), `32022L2555` (NIS2) |
| `6` | CJEU içtihadı (`CJ` = karar) | `62019CJ0715` |
| `0` | Konsolide metinler (`02016R0679-...`) | tarihli konsolidasyon |

---

## Uygulamalı örnekler

### Örnek 1 — SPARQL ile CELEX'ten work + tarih çekme (canlı doğrulandı)

```
WebFetch:
  URL: https://publications.europa.eu/webapi/rdf/sparql?query=PREFIX%20cdm%3A%20%3Chttp%3A%2F%2Fpublications.europa.eu%2Fontology%2Fcdm%23%3E%20SELECT%20%3Fwork%20%3Fdate%20WHERE%20%7B%20%3Fwork%20cdm%3Aresource_legal_id_celex%20%2232016R0679%22%5E%5E%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23string%3E%20.%20%3Fwork%20cdm%3Awork_date_document%20%3Fdate%20%7D&format=application%2Fsparql-results%2Bjson
  prompt: "SPARQL JSON sonucundaki work URI ve belge tarihini çıkar"
```

Sorgunun açık hâli:

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?work ?date WHERE {
  ?work cdm:resource_legal_id_celex "32016R0679"^^<http://www.w3.org/2001/XMLSchema#string> .
  ?work cdm:work_date_document ?date
}
```

Doğrulanmış çıktı: work = `http://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1`,
date = `2016-04-27`. Work URI, atıfta kullanılacak kalıcı kimliktir.

### Örnek 2 — ELI URI (⚠️ ATIF için geçerli, METİN çekmek için DEĞİL)

```
# ❌ Metin çekmez — OJ tarih indeksi döner (30.08.2026 doğrulandı):
https://eur-lex.europa.eu/eli/reg/2016/679/oj
https://eur-lex.europa.eu/eli/dir/2019/944/oj/ron
```

`http://data.europa.eu/eli/reg/2016/679/oj` **kalıcı tanımlayıcıdır ve atıfta
kullanılır** — ama WebFetch ile metin vermez. Metin için Örnek 3'teki zinciri kullan.

> **Ayrım net olsun:** ELI = *atıf kimliği* ✅ · CELLAR manifestation `/DOC_1` = *metin* ✅

### Örnek 3 — CELEX'ten TAM METNE: üç adım (canlı doğrulandı ✅)

```
# ADIM 1 — UUID'yi al
WebFetch:
  URL: https://publications.europa.eu/resource/celex/32016R0679
  → 303: http://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1/rdf/object/full

# ADIM 2 — İngilizce manifestation'ı çöz (SPARQL)
PREFIX cdm:  <http://publications.europa.eu/ontology/cdm#>
PREFIX lang: <http://publications.europa.eu/resource/authority/language/>
SELECT ?manif WHERE {
  ?work cdm:resource_legal_id_celex "32016R0679"^^<http://www.w3.org/2001/XMLSchema#string> .
  ?expr cdm:expression_belongs_to_work ?work ;
        cdm:expression_uses_language lang:ENG .
  ?manif cdm:manifestation_manifests_expression ?expr .
} LIMIT 5
  → http://publications.europa.eu/resource/cellar/3e485e15-...-01aa75ed71a1.0006.03

# ADIM 3 — metni çek
WebFetch:
  URL: http://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0006.03/DOC_1
  prompt: "..."
```

**Dil değiştirmek:** ADIM 2'de `lang:ENG` yerine `lang:RON` / `lang:DEU` / `lang:FRA` /
`lang:ITA` / `lang:ELL` / `lang:POL` yaz. Bu, Romanya ve Yunanistan gibi ulusal portalı
erişilemeyen yargı çevrelerinde **AB-türevli mevzuatı ana dilinde** almanın çalışan yoludur
(bkz. `romanya-hukuku-rehberi.md` bölüm 1b).

---

## ArthurLegal MCP — `eu_` araçları

| Alan | Değer |
|------|-------|
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on dört yargı çevresi tek uçta) |
| **Araç öneki** | `eu_` |
| **Auth** | **Yok** |

| Araç | Ne yapar |
|---|---|
| `eu_search_eu_law` | Başlıkta arama — mevzuat **ve** CJEU içtihadı; CELEX döndürür |
| `eu_get_metadata` | Tek CELEX için başlık, tarih, ELI, yürürlük bayrağı |
| `eu_get_document_text` | Otantik tam metin, karakterle sayfalanır (GDPR ≈ 350.000) |
| `eu_sparql` | CELLAR grafiğine doğrudan SELECT — diğer araçların kapsamadığı sorular |

> ⚠️ **`eur-lex.europa.eu` belge yollarını kullanma.** JS kabuğu döndürürler:
> her istek için Resmî Gazete tarih dizini gelir, sorunsuz parse olur ve
> istediğin belge **değildir**. Bu araçlar CELLAR üzerinden gider.

> ⚠️ **CELEX uydurma.** Sektör + yıl + tür + sıra kodlar (32016R0679 = GDPR).
> Yanlış CELEX hataya değil, **başka bir mevzuata** çözülür.

> ⚠️ **Konsolide ≠ orijinal.** `0` ile başlayıp tarih eki taşıyan CELEX
> (02010D0146-20161217) konsolide metindir: bilgi amaçlı hazırlanır, **hukuki
> bağlayıcılığı yoktur**. Bağlayıcı olan Resmî Gazete hâlidir. `consolidated:
> true` bunu işaretler; hangisini kullandığını söyle.

> ⚠️ **Dil bir görüntüleme seçeneği değildir.** Her dil ayrı bir expression'dır;
> ya vardır ya yoktur. Yoksa araç bunu söyler, sessizce başka dile düşmez.

> **CELEX öneki:** `3` mevzuat · `6` içtihat · `0` + tarih eki konsolide metin.

---

## Yasama tarihi tamamlayıcısı: European Parliament Open Data

Bir tüzüğün müzakere geçmişi (komisyon raporları, oylamalar, pozisyonlar) için
**European Parliament Open Data** portalı (`data.europarl.europa.eu`) mevcuttur.
Ancak dürüst kayıt şudur: portalın yeniden kullanım rejimi Cellar'ınki gibi
standart CC lisansı değil, **EP'nin kendi Legal Notice'ı**dır — atıf zorunludur,
CC BY 4.0 eşdeğerliği **teyit edilememiştir**; portal sayfası bu oturumda
JS-render nedeniyle canlı doğrulanamadı (entegrasyon öncesi doğrulanmalı).
Yasama tarihi çıktıları bu nedenle ayrı etiketlenir ve lisans netleşene kadar
yalnızca bağlam (context) olarak kullanılır, yeniden yayımlanmaz.

---

## Atıf disiplini

Cellar/EUR-Lex'ten oturumda fiilen çekilen her belge:

```
[EUR-Lex Cellar — CELEX:{no} — çekim: GG.AA.YYYY]
[EUR-Lex Cellar — ELI: {eli-uri} — çekim: GG.AA.YYYY]
[EUR-Lex Cellar — CJEU CELEX:6{YIL}CJ{no} — çekim: GG.AA.YYYY]
```

Örnek: `[EUR-Lex Cellar — CELEX:32016R0679 — çekim: 13.08.2026]`

Kurallar:
- Çekilmemiş bir AB metni "biliniyor" diye bu etiketle sunulamaz →
  `[model bilgisi — doğrulayın]`.
- Konsolide metinden alıntı yapılıyorsa CELEX'in `0` sektörlü tarihli hâli
  yazılır ve konsolidasyonun referans amaçlı olduğu belirtilir (aşağıya bakın).
- Doktrin ve ikincil kaynak bağlamdır, otorite değildir; eval verisi hiçbir
  zaman atıf kaynağı değildir.

---

## Lisans ve sınırlar

**Lisans (EUR-Lex legal notice, doğrulandı: 13.08.2026):**
- Yeniden kullanım rejimi **Komisyon Kararı 2011/833/EU**'ya dayanır; aksi
  belirtilmedikçe belgeler ticari/ticari olmayan amaçla yeniden kullanılabilir.
- **Editoryal içerik, özetler ve konsolide metinler: CC BY 4.0** — kaynak
  gösterilir, yapılan değişiklik belirtilir.
- **Metadata: CC0 1.0** (kamu malı).
- Üçüncü kişi hakları (kişi görselleri, marka/patent/logo) kapsam dışıdır.

**Otantiklik sınırı (kritik):** Yalnızca **Resmî Gazete'de (Official Journal)**
yayımlanan metinler otantiktir (e-OJ 2013'ten beri hukuken geçerli nüsha).
**Konsolide metinler referans amaçlıdır** — bağlayıcı analizde OJ metni esas
alınır ve çıktıda bu ayrım açıkça söylenir. İçtihatta resmî kaynak European
Court Reports'ta yayımlanan sürümdür.

**Teknik sınırlar:**
- SPARQL endpoint'inde execution timeout vardır; geniş sorguları CELEX/ELI ile daraltın.
- WebFetch `Accept` başlığı ayarlayamaz → format seçimi URL parametresiyle
  (`format=`) veya EUR-Lex HTML sayfası üzerinden yapılır.
- CDM ontolojisi geniştir; buradaki alan adları dışındakiler kullanılmadan önce
  canlı doğrulanır (alan adı uydurulmaz).
- Endpoint arızasında yedek yol: `eu-legislation-rehberi.md` (EUR-Lex HTML WebFetch).

---

## Karar kaydı (mini-ADR)

**Bağlam.** AB/CJEU kaynağı bugüne dek WebFetch katmanındaydı
(`eu-legislation-rehberi.md`): EUR-Lex HTML kazıması çalışıyor, ancak kalıcı
tanımlayıcı ve çekim metadatası elle kuruluyordu; sürüm (OJ mü konsolide mi)
ayrımı kazınan sayfanın görünümüne bağlıydı.

**Karar.** Cellar, SPARQL + kararlı CELEX/ELI URI katmanı olarak kabul edildi.
Varsayılan erişim WebFetch/GET; MCP yalnızca cyanheads/eur-lex-mcp-server'ın
pin'lenmiş, kod incelemesinden geçmiş bir release'inin self-hosted loopback
kurulumuyla ve çıktılarının CELEX/ECLI + çekim tarihi taşıdığı doğrulanarak
kullanılır. Yazarın hosted örneği hiçbir koşulda kullanılmaz.

**Sonuçlar.** Kaynak + tarih artık yapılandırılmış alandan gelir ("kaynaksız
hukuk yok" için bedava kazanım); konsolide/OJ ayrımı CELEX sektörüyle makine
düzeyinde görünür. Serbest metin araması ve hızlı madde okuması eski yolda
(`eu-legislation-rehberi.md`) kalır. Entegrasyon anında yeniden doğrulanacaklar:
SPARQL endpoint'in erişilebilirliği, MCP sürümü (pre-1.0 kırılma riski) ve EP
Open Data lisans rejimi.

---

## İlgili rehberler

- `eu-legislation-rehberi.md` — EUR-Lex/CJEU/ECHR WebFetch yolu (yedek ve serbest arama)
- `karsilastirmali-hukuk-rehberi.md` — yabancı hukuk ne zaman devreye girer, atıf çerçevesi

---

*Son güncelleme: 13.08.2026 — Cellar SPARQL + CELEX/ELI URI katmanı; açık erişim, anahtar gerektirmez.*

---

## MCP connector olarak eklemek

**Bugünkü durum:** Bu kaynağın hazır bir MCP sunucusu **yoktur**; yukarıdaki
prosedür `WebFetch` ile çalışır ve bağlayıcı kurulumu gerektirmez. claude.ai'daki
"custom connector" **MCP tabanlıdır** — dolayısıyla bu kaynağı connector olarak
eklemek, önce REST ucunu bir MCP sunucusuyla sarmayı gerektirir.

Aşağıdaki bilgi o sarmalamayı yapabilmeniz içindir. **Hazır bir endpoint
verilmemiştir; olmayan bir adres yazmak yerine sarmalanacak sözleşme verilmiştir.**

### Sarmalanacak sözleşme

| Alan | Değer |
|---|---|
| **Base URL** | ``https://publications.europa.eu/webapi/rdf/sparql`` |
| **Auth** | **Yok** — kayıt gerekmez |
| **Hız sınırı** | Ağır SPARQL sorgularında zaman aşımı olur; `LIMIT` kullan |
| **Yanıt** | SPARQL results JSON (`format=application/sparql-results+json`) |
| **Lisans** | İçerik **CC BY 4.0**, metadata **CC0** (Komisyon Kararı 2011/833/EU) |

**Açılacak araç yüzeyi:**

| Araç | Uç | Ne döndürür |
|---|---|---|
| `cellar_sparql` | `/sparql?query=&format=` | Ham SPARQL sonucu |
| `cellar_find_celex` | (sarmalayıcı sorgusu) | Başlık/tarih/tipten CELEX numarası |
| `cellar_get_metadata` | (sarmalayıcı sorgusu) | Bir CELEX'in konsolidasyon ve yürürlük metadatası |

> Cellar **kimlik ve metadata** katmanıdır. Operatif metin EUR-Lex'te okunur;
> sarmalayıcı bunu araç açıklamasında açıkça söylemelidir, yoksa model metni
> buradan bekler.

### Kanıtlanmış sarma kalıbı

Bu ekosistemde üç MCP sunucusu (`eqanun-api`, `lex-scholar-api`,
`resourcecontracts-api`) tam olarak bu işi yapıyor: public bir REST API'yi
bağımlılıksız (yalnız Python stdlib) bir MCP sunucusuyla sarıyorlar. Kalıp:

- **Transport:** Streamable HTTP, `/mcp` yolunda (`x-ms-agentic-protocol:
  mcp-streamable-1.0` muadili; claude.ai için düz Streamable HTTP yeterli)
- **Auth:** yok (upstream public olduğu için)
- **Port:** her sunucu kendi portunda; bu kaynak için önerilen **`8050`**
  (mevcutlar: resourcecontracts `8000` · lex-scholar `8010` · e-qanun `8020` ·
  de-eli `8790`). Aynı porta ikinci sunucu başlatmak açıkça hata verir.
- **Araç adları:** yukarıdaki yüzeyi birebir yansıt; **jenerik ad kullanma**.
  Başka bir sunucuda aynı adda bir araç varsa istemci şemaları karıştırır ve
  çağrılar düşer — bu ekosistemde bir kez yaşandı (`search_articles` çakışması).

Referans uygulamalar: `github.com/beerbottle90/eqanun-api` ·
`github.com/beerbottle90/lex-scholar-api` ·
`github.com/beerbottle90/resourcecontracts-api` ·
`github.com/beerbottle90/de-eli-mcp`

### claude.ai'a bağlama (sunucu ayağa kalktıktan sonra)

1. Settings → Connectors → **Add custom connector**
2. MCP endpoint URL'sini gir (`https://arthurlegal-mcp.fly.dev/mcp`)
3. Auth: **None**
4. Araçlar bağlantı sonrası otomatik keşfedilir. Tool isim prefiksi verdiğin
   connector adına göre üretilir — **prefiksi sabit varsayma**, base isimleri kullan.

> ⚠️ Geçici tünel (`*.trycloudflare.com`) kullanıyorsan adres **her yeniden
> başlatmada değişir** ve connector sessizce kırılır: tanım doğru görünür,
> çağrılar düşer. Kalıcı kullanım için adlandırılmış tünel veya hosted deploy.

**Sarmadan da çalışır.** Connector zorunlu değildir; yukarıdaki `WebFetch`
prosedürü bu kaynağın tam işlevini verir. Sarmalama, yapılandırılmış araç
çağrısı ve tekrarlanabilir parametre disiplini istendiğinde değer katar.
