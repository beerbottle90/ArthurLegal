# Almanya Mevzuatı & İçtihadı — Kullanım Rehberi (v1.8.4)

> ✅ **Alman hukuku için özel MCP VAR (v1.5.0):** `de-eli-mcp-rehberi.md`.
> Mevzuat (NeuRIS), içtihat (yedi federal mahkeme tam + 16 eyalet) ve parlamento
> belgeleri tek uçtan, 14 araçla gelir. **Alman hukuku için birincil yol odur.**
> Aşağıdaki WebFetch rotaları MCP bağlı değilken geçerlidir — ve aşağıda kayıtlı
> ECONNREFUSED sorunu MCP'de görülmez, çünkü çağrıyı sunucu kendi tarafında yapar.


> **Erişim tipi:** WebFetch (GET) — MCP gerekmez
> **Auth:** Yok
> **Kapsam:** Tüm Alman federal mevzuatı + BGH/BVerfG kararları
> **[Müvekkil] bağlamı:** Alman karşı taraflar (M&A, enerji), [BORU HATTI PROJESİ] AB bağlantısı, Alman şirket hukuku
>
> ⚠️ **ERİŞİM NOTU (08.06.2026 test):** Resmi `gesetze-im-internet.de` ve NeuRIS
> (`api.rechtsinformationen.bund.de`) domain'leri **WebFetch ile ECONNREFUSED** döndürüyor
> (bu ortamın egress'i Alman hükümet domain'lerine ulaşamıyor). **İki çalışan birincil kaynak:**
> 1. **`bundestag/gesetze` raw GitHub** — tüm kanunlar Markdown, bloklu domain'i baypas eder (bölüm 1a) ✅
> 2. **`dejure.org`** — mevzuat + içtihat çapraz-referans (bölüm 1) ✅
> AB-türevli Alman hukuku için **EUR-Lex Almanca** (`/DE/TXT/`) da çalışıyor ✅.

---

## 1. dejure.org — Federal Mevzuat + İçtihat (BİRİNCİL ✅)

**Bağımsız Alman hukuk portalı. Auth yok. WebFetch ile tam metin döndürür (08.06.2026 test ✅:
BGB § 433 tam metin + 5.672 ilgili mahkeme kararı).**

```
GET https://dejure.org/gesetze/{KISALTMA}/{madde}.html
```

**[Müvekkil] için kritik Alman mevzuatı:**

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

## 1c. gesetze-im-internet.de — Resmi Kaynak (⚠️ WebFetch erişilemeyebilir)

**Resmi Alman Federal Adalet Bakanlığı platformu.** Tarayıcıda çalışır; bu ortamdan
WebFetch **ECONNREFUSED** (08.06.2026). Erişim sağlanabilen ortamlarda:

```
GET https://www.gesetze-im-internet.de/{kisaltma}/
örnek: https://www.gesetze-im-internet.de/bgb/__242.html
```
Kısaltmalar küçük harf: `bgb`, `hgb`, `aktg`, `gmbhg`, `enwg_2005`, `gwb`, `uwg_2004`,
`bdsg_2018`, `inso`, `zpo`. **Erişilemezse dejure.org birincil yedek.**

---

## 2. NeuRIS — Yeni Federal Hukuk Bilgi Sistemi (⚠️ WebFetch erişilemeyebilir)

**BGH, BVerfG ve 4 yüksek mahkeme + mevzuat. REST API.** Bu ortamdan **ECONNREFUSED**
(08.06.2026) — gesetze-im-internet.de ile aynı erişim engeli. Erişilebilen ortamlarda:

```
GET https://api.rechtsinformationen.bund.de/v1/search?q={query}&type=NORM
GET https://api.rechtsinformationen.bund.de/v1/search?q={query}&type=ENTSCHEIDUNG
```

Swagger: `https://docs.rechtsinformationen.bund.de/`
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
[DE Mevzuat — {Kanun adı} {§} — gesetze-im-internet.de — GG.AA.YYYY]   (erişilebildiyse)
[BGH — {Esas no/tarih} — GG.AA.YYYY]
[BVerfG — {BVerfGE cilt/sayfa} — GG.AA.YYYY]
```

---

## [Müvekkil] için özel notlar

- Alman enerji şirketleri ile yapılan M&A/JV sözleşmelerinde **Deutsches Recht** klozuna dikkat
- EnWG m.3 vd. — Alman enerji piyasası düzenlemesi [BORU HATTI PROJESİ] için ab-bağlantısı
- **BundesNetzAgentur (BNetzA)** kararları için: `https://www.bundesnetzagentur.de/EN/Areas/Energy/` (WebFetch)
- Alman şirket kurulumunda GmbHG/AktG + Handelsregister (HR): `https://www.unternehmensregister.de/`

*Son güncelleme: 08.06.2026 — v1.8.4. dejure.org birincil kaynak olarak eklendi (gesetze-im-internet.de + NeuRIS WebFetch ECONNREFUSED — erişim notu düşüldü). EUR-Lex DE fallback.*
