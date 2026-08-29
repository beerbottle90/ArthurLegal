# Almanya Mevzuatı & İçtihadı — Kullanım Rehberi (v1.8.4)

> ✅ **Alman hukuku için özel MCP VAR (v1.5.0):** `de-eli-mcp-rehberi.md`.
> Mevzuat (NeuRIS), içtihat (yedi federal mahkeme tam + 16 eyalet) ve parlamento
> belgeleri tek uçtan, 14 araçla gelir. **Alman hukuku için birincil yol odur.**
> Aşağıdaki WebFetch rotaları MCP bağlı değilken geçerlidir — ve aşağıda kayıtlı
> ECONNREFUSED sorunu MCP'de görülmez, çünkü çağrıyı sunucu kendi tarafında yapar.


> **Erişim tipi:** WebFetch (GET) — MCP gerekmez
> **Auth:** Yok
> **Kapsam:** Tüm Alman federal mevzuatı + BGH/BVerfG kararları
> **[ŞİRKET ADI] bağlamı:** Alman karşı taraflar (M&A, enerji), [BORU HATTI PROJESİ] AB bağlantısı, Alman şirket hukuku
>
> ⚠️ **ERİŞİM NOTU (30.08.2026 yeniden test):** Burada **iki ayrı sorun** var, karıştırma:
>
> 1. **`api.rechtsinformationen.bund.de` diye bir host hiç var olmadı** — NXDOMAIN
>    (dns.google: "Non-existent domain"). Bu bir egress engeli değil, **yanlış hostname'di**.
>    Doğru NeuRIS host'u: **`testphase.rechtsinformationen.bund.de`** ✅ (bölüm 2).
> 2. **`gesetze-im-internet.de` ve `rechtsprechung-im-internet.de` gerçekten erişilemez**
>    (bağlantı kurulamıyor, 30.08.2026 doğrulandı) — bu ortamın egress'i bu iki domain'e
>    ulaşamıyor. ⚠️ **Ama de-eli MCP'nin `de_rii_*` araçları çalışır:** MCP sunucusu bu
>    siteleri kendi egress'inden çeker, senin WebFetch engelin onu bağlamaz.
>
> **Çalışan birincil kaynaklar (30.08.2026 test):**
> 1. **de-eli MCP** — mevzuat + içtihat, tercih edilen yol (`de-eli-mcp-rehberi.md`) ✅
> 2. **`testphase.rechtsinformationen.bund.de`** — NeuRIS REST, auth yok (bölüm 2) ✅
> 3. **`dejure.org`** — mevzuat + içtihat çapraz-referans (bölüm 1) ✅
> 4. **`bundestag/gesetze` raw GitHub** — tüm kanunlar Markdown (bölüm 1a) ✅
> AB-türevli Alman hukuku için **EUR-Lex Almanca** (`/DE/TXT/`) da çalışıyor ✅.

---

## 1. dejure.org — Federal Mevzuat + İçtihat (BİRİNCİL ✅)

**Bağımsız Alman hukuk portalı. Auth yok. WebFetch ile tam metin döndürür (08.06.2026 test ✅:
BGB § 433 tam metin + 5.672 ilgili mahkeme kararı).**

```
GET https://dejure.org/gesetze/{KISALTMA}/{madde}.html
```

**[ŞİRKET ADI] için kritik Alman mevzuatı:**

| Mevzuat | Kısaltma | Örnek madde URL |
|---|---|---|
| BGB (Türk TBK eşdeğeri) | `BGB` | `https://dejure.org/gesetze/BGB/433.html` (satış sözl.) |
| HGB (Türk TTK eşdeğeri) | `HGB` | `https://dejure.org/gesetze/HGB/1.html` |
| AktG (Anonim şirket) | `AktG` | `https://dejure.org/gesetze/AktG/1.html` |
| GmbHG (Ltd şirket) | `GmbHG` | `https://dejure.org/gesetze/GmbHG/1.html` |
| EnWG (Enerji sektörü) | `EnWG` | `https://dejure.org/gesetze/EnWG/1.html` |
| GWB (Rekabet hukuku) | `GWB` | `https://dejure.org/gesetze/GWB/1.html` |
| UWG (Haksız rekabet) | `UWG` | `https://dejure.org/gesetze/UWG/1.html` |
| BDSG (Alman veri koruma) | `BDSG` | `https://dejure.org/gesetze/BDSG/1.html` |
| InsO (İflas) | `InsO` | `https://dejure.org/gesetze/InsO/1.html` |
| ZPO (Medeni yargılama) | `ZPO` | `https://dejure.org/gesetze/ZPO/1.html` |

**Belirli paragraf çekimi:**
```
WebFetch("https://dejure.org/gesetze/BGB/242.html",
         "BGB §242 Treu und Glauben maddesinin içeriği + ilgili kararlar")
```

dejure.org her madde sayfasında ilgili BGH/BVerfG kararlarına çapraz-referans verir —
mevzuat + içtihat tek çağrıda.

---

## 1a. bundestag/gesetze — Tüm Alman Kanunları Markdown (raw GitHub ✅)

**En sağlam yöntem.** Tüm Alman federal kanunları Markdown olarak GitHub'da; resmi
gesetze-im-internet.de XML'lerinden üretilmiş. **`raw.githubusercontent.com` erişilebilir
olduğundan bloklu resmi domain'i tamamen baypas eder** (08.06.2026 test ✅: BGB tam metin).

```
GET https://raw.githubusercontent.com/bundestag/gesetze/master/{harf}/{kisaltma}/index.md
```

- `{harf}` = kısaltmanın ilk harfi (küçük), `{kisaltma}` = kanun kısaltması (küçük)
- Örnek: BGB → `.../master/b/bgb/index.md` · HGB → `.../master/h/hgb/index.md`

| Mevzuat | raw URL |
|---|---|
| BGB | `https://raw.githubusercontent.com/bundestag/gesetze/master/b/bgb/index.md` |
| HGB | `https://raw.githubusercontent.com/bundestag/gesetze/master/h/hgb/index.md` |
| AktG | `https://raw.githubusercontent.com/bundestag/gesetze/master/a/aktg/index.md` |
| GmbHG | `https://raw.githubusercontent.com/bundestag/gesetze/master/g/gmbhg/index.md` |
| EnWG | `https://raw.githubusercontent.com/bundestag/gesetze/master/e/enwg_2005/index.md` |
| GWB | `https://raw.githubusercontent.com/bundestag/gesetze/master/g/gwb/index.md` |

> Büyük kanunlar tek dosyada — WebFetch otomatik özetler; belirli § için prompt'ta madde
> numarasını belirt. Kısaltma bilinmiyorsa dejure.org (bölüm 1) veya repo arama kullan.

**Opsiyonel MCP'ler** (Claude Code, kurulum isteğe bağlı): `Ansvar-Systems/German-law-mcp`
(gesetze-im-internet sarmalayıcı, 21★) · `wolfgangihloff/rechtsinformationen-bund-de-mcp`
(NeuRIS resmi portal sarmalayıcı). Bunlar da resmi domain'e bağlanır — erişim engeli
varsa bundestag/gesetze raw birincil kalır.

---

## 1b. AB-türevli Alman hukuku — EUR-Lex Almanca (✅)

GDPR (DSGVO), AB direktiflerinin Alman uyumu vb. için EUR-Lex Almanca versiyonu çalışıyor:
```
GET https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679
```
(Detay: `eu-legislation-rehberi.md` — CELEX pattern aynı, dil kodu `DE`.)

---

## 1c. gesetze-im-internet.de — Resmi Kaynak (❌ bu ortamdan ERİŞİLEMEZ)

**Resmi Alman Federal Adalet Bakanlığı platformu.** Tarayıcıda çalışır; bu ortamdan
WebFetch **bağlantı kuramıyor** (30.08.2026 yeniden doğrulandı — kalıcı görünüyor).
**Bu bölümdeki URL'leri çağırma; atıf dizesinde de kaynak olarak gösterme.**
Erişim sağlanabilen ortamlarda desen şudur:

```
GET https://www.gesetze-im-internet.de/{kisaltma}/
örnek: https://www.gesetze-im-internet.de/bgb/__242.html
```
Kısaltmalar küçük harf: `bgb`, `hgb`, `aktg`, `gmbhg`, `enwg_2005`, `gwb`, `uwg_2004`,
`bdsg_2018`, `inso`, `zpo`.

> **Bunun yerine ne kullan:** madde metni için **dejure.org** (bölüm 1) veya
> **de-eli MCP `de_get_text`**; her ikisi de 30.08.2026'da test edildi ✅.

---

## 2. NeuRIS — Yeni Federal Hukuk Bilgi Sistemi (✅ ÇALIŞIYOR — host düzeltildi)

**BGH, BVerfG ve 4 yüksek mahkeme + federal mevzuat. REST API, auth yok.**

⚠️ **v1.5.0'a kadar burada yazan `api.rechtsinformationen.bund.de` host'u hiç var olmadı**
(NXDOMAIN). Doğru host **`testphase.rechtsinformationen.bund.de`** — de-eli MCP'nin
kendi `source_url` alanı da bu host'u döndürür.

```
GET https://testphase.rechtsinformationen.bund.de/v1/legislation?searchTerm={q}&size=20
GET https://testphase.rechtsinformationen.bund.de/v1/case-law?searchTerm={q}&size=20
```
30.08.2026 test ✅ — `/v1/legislation?searchTerm=Aktiengesetz&size=1` → 200 + ELI'li kayıt;
`/v1/case-law?searchTerm=Kuendigung&size=1` → 200.

Swagger: `https://docs.rechtsinformationen.bund.de/` ✅

> **Önce MCP dene.** `de-eli-mcp-rehberi.md` aynı API'yi sarmalar; `eli_uri` +
> `human_readable_citation` + `source_url` atıf üçlüsünü hazır döndürür ve `de_rii_*`
> araçlarıyla altı federal mahkemenin **tam** külliyatına ulaşır. Bu WebFetch yolu
> yalnızca MCP connector'ı yokken kullanılır.

⚠️ **NeuRIS BETA'dır** — mevzuat kümesi eksik (~2.400 akt), içtihat kümesi dar bir dilim.
Kapsamlı araştırmada de-eli MCP'nin `de_rii_*` araçlarıyla çapraz kontrol et.

**Erişilemezse:** içtihat için dejure.org madde sayfalarındaki karar referansları veya
Open Legal Data (bkz. bölüm 5).

---

## 3. BGH (Federal Yargıtay) Doğrudan Erişim

```
GET https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/list.py?Gericht=bgh&Art=en&Datum={YYYY}&Seite={page}
```

Belirli karar metni:
```
WebFetch("https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&nr={karar_no}",
         "Kararın özeti")
```

---

## 4. BVerfG (Anayasa Mahkemesi)

```
WebFetch("https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/{YIL}/{YIL}{NO}.html",
         "Kararın özeti")
```

---

## 5. Open Legal Data — Toplu Karar Erişimi

Topluluk destekli REST API, 100.000+ karar:
```
GET https://de.openlegaldata.io/api/cases/?search={query}&court=bgh
```

Auth yok. Format: JSON.

---

## Atıf formatı

```
[DE Mevzuat — {Kanun adı} {§ veya Art.} — dejure.org — GG.AA.YYYY]
[DE Mevzuat — {Kanun adı} {§} — NeuRIS testphase — GG.AA.YYYY]        (WebFetch REST)
[BGH — {Esas no/tarih} — GG.AA.YYYY]
[BVerfG — {BVerfGE cilt/sayfa} — GG.AA.YYYY]
```

---

## [ŞİRKET ADI] için özel notlar

- Alman enerji şirketleri ile yapılan M&A/JV sözleşmelerinde **Deutsches Recht** klozuna dikkat
- EnWG m.3 vd. — Alman enerji piyasası düzenlemesi [BORU HATTI PROJESİ] için ab-bağlantısı
- **BundesNetzAgentur (BNetzA)** kararları için: `https://www.bundesnetzagentur.de/EN/Areas/Energy/` (WebFetch)
- Alman şirket kurulumunda GmbHG/AktG + Handelsregister (HR): `https://www.unternehmensregister.de/`

*Son güncelleme: 30.08.2026 — v1.8.5. NeuRIS host düzeltmesi: `api.rechtsinformationen.bund.de` NXDOMAIN olduğu tespit edildi, doğru host `testphase.rechtsinformationen.bund.de` ile değiştirildi ve canlı doğrulandı. gesetze-im-internet.de / rechtsprechung-im-internet.de erişilemezliği yeniden doğrulandı; de-eli MCP'nin `de_rii_*` araçlarının bu engelden etkilenmediği not edildi. dejure.org birincil. EUR-Lex DE fallback.*
