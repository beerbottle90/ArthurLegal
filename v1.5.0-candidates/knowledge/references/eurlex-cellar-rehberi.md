# EUR-Lex Cellar — Kullanım Rehberi (SPARQL + REST / WebFetch yöntemi)

> **MCP/connector durumu:** Varsayılan erişim doğrudan `WebFetch`/HTTP GET iledir — MCP gerekmez.
> Opsiyonel self-hosted MCP seçeneği için aşağıdaki "MCP seçeneği" bölümüne bakın; yalnızca
> orada sayılan koşullar altında kullanılır.
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
Format seçimi normalde `Accept` başlığıyla yapılır (content negotiation); WebFetch
başlık ayarlayamadığından varsayılan yönlendirmeyi izlemek yeterlidir.

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

### Örnek 2 — ELI URI üzerinden tam metne inme (canlı doğrulandı)

```
WebFetch:
  URL: https://eur-lex.europa.eu/eli/reg/2016/679/oj
  prompt: "GDPR m.83 idari para cezası tavanlarını madde metniyle ver"
```

`http://data.europa.eu/eli/reg/2016/679/oj` bu sayfaya yönlenir; her iki URI de
atıfta geçerlidir, ELI olan kalıcı tanımlayıcıdır.

### Örnek 3 — CELEX resource URI ile metadata

```
WebFetch:
  URL: http://publications.europa.eu/resource/celex/32016R0679
  prompt: "Yönlendirilen Cellar kaydındaki work kimliğini ve mevcut formatları listele"
```

---

## MCP seçeneği (opsiyonel, koşullu)

**cyanheads/eur-lex-mcp-server** (GitHub; doğrulandı: 13.08.2026): TypeScript,
**Apache-2.0**, sürüm **v0.9.8 — pre-1.0**. Yedi araç sunar: Cellar araması, çok
dilli/çok formatlı belge çekme, CELEX çözümleme, CJEU içtihadı, ilişki grafı,
EuroVoc tarama, ham SPARQL. Auth gerektirmez; STDIO ve HTTP transport destekler.

Kullanım koşulları (yumuşatılamaz):
- **Yalnızca self-hosted loopback** (localhost) — yazarın barındırdığı örnek
  **hiçbir koşulda** kullanılmaz.
- Sürüm **pin'lenir** ve kod incelemesinden geçmiş bir release'ten kurulur
  (pre-1.0: API yüzeyi kırılabilir).
- Araç çıktılarının **CELEX/ECLI kimliği + çekim tarihi** taşıdığı entegrasyonda
  doğrulanır; taşımıyorsa çıktı atıf kaynağı olarak kullanılamaz.

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