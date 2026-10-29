# Finlandiya Hukuku — Kullanım Rehberi (Finlex açık veri API'si)

> ✅ **Bu yargı çevresi için artık custom MCP server VAR (v1.6.0):**
> **`fi-finlex MCP`** → `references/fi-finlex-mcp-rehberi.md`. **Önce onu kullan** —
> arama, atıf sözleşmesi ve statü disiplini orada hazırdır.
>
> Bu dosya **WebFetch yedeğidir**: connector bağlı değilse kullanılır.
> Yedek yol daha dar ve kırılgandır — buradan üretilen atıfa
> **`(MCP kullanılmadı)`** kaydını düş.

> **Erişim tipi:** WebFetch (GET) — auth yok, API anahtarı yok
> **Durum:** ✅ **Akoma Ntoso XML REST API** — mevzuat + içtihat + otorite düzenlemeleri
> **Test:** 30.08.2026 — canlı doğrulandı
> **[Müvekkil] bağlamı:** FI, Baltık enerji piyasası ve Fennovoima/nükleer–LNG
> tedarik zincirinde karşı taraf; ayrıca İskandinav sözleşme uygulamasının referansı.

---

## Kaynak haritası

| Kaynak | İçerik | Durum (30.08.2026) |
|---|---|---|
| **opendata.finlex.fi** | Akoma Ntoso REST API — kanun, içtihat, TES | ✅ 200 |
| Swagger | `https://opendata.finlex.fi/swagger-ui/index.html` | ✅ 200 |
| OpenAPI şeması | `https://opendata.finlex.fi/v3/api-docs` | ✅ (⚠️ **gzip** — `--compressed` gerekir) |
| finlex.fi / data.finlex.fi | Web arayüzü | ✅ 200 |
| EUR-Lex CELLAR | AB-türevli FI mevzuatı (FIN) | ✅ |

> ⚠️ `opendata.finlex.fi/` **kök adresi 403** verir — bu normaldir, alt yollar çalışır.

---

## 1. API yapısı

Taban: `https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi`

| Yol | İçerik |
|---|---|
| `/act/{actDocumentType}/list` | Kanun listesi (akn_uri + status) |
| `/act/{actDocumentType}/{yıl}` | O yılın kanunları, Akoma Ntoso XML |
| `/act/{actDocumentType}/{yıl}/{no}/{lang@sürüm}/main.akn` | Tek kanunun tam metni |
| `/judgment/{judgmentDocumentType}/{yıl}/{no}/...` | Mahkeme kararları |
| `/doc/authority-regulation/{otorite}/{yıl}/{no}/...` | Otorite düzenlemeleri |
| `.../main.pdf` | Aynı belgenin PDF'i |

`{actDocumentType}`: `statute` (yayımlandığı hâl) · **`statute-consolidated`** (konsolide)

**`{lang@sürüm}` formatı** — bu API'nin en kritik ayrıntısı:
```
fin@20221099    → Fince, o sürüm tarihi
swe@20221099    → İsveççe (FI'da ikinci resmî dil)
```

**Doğrulanmış çıktı (30.08.2026):**
```
GET /act/statute-consolidated/list?limit=2
→ [{"akn_uri":".../act/statute-consolidated/2019/469/swe@20221099","status":"MODIFIED"},
   {"akn_uri":".../act/statute-consolidated/2019/469/fin@20221099","status":"MODIFIED"}]

GET /act/statute/2023
→ <AknXmlList><Results><akomaNtoso ...><act contains="originalVersion" ...>   ✅
```

> 🔴 **Tuzak:** `{lang@sürüm}` olmadan `main.akn` çağırırsan
> `"No entry found in given path"` alırsın. **Önce `/list` ile doğru `akn_uri`'yi
> öğren, sonra onu çağır.** URI'yi elle kurma.

```
WebFetch:
  URL: https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/list?limit=20
  prompt: "Dönen akn_uri listesini ve her birinin status alanını çıkar"
```

---

## 2. Statü disiplini

`/list` çıktısındaki **`status`** alanı (`MODIFIED` vb.) belgenin güncelliğini gösterir.
Konsolide külliyat (`statute-consolidated`) yürürlükteki metni verir; `statute` ise
**yayımlandığı hâli**. Hangisini kullandığını atıfta belirt.

---

## 3. [Müvekkil] için kritik FI mevzuatı

| Konu | Kanun | Bağlantı |
|---|---|---|
| Şirketler | Osakeyhtiölaki (624/2006) | Oy kurulumu, yönetim sorumluluğu |
| Sözleşme | Laki varallisuusoikeudellisista oikeustoimista (228/1929) | Sözleşme geçerliliği |
| Elektrik piyasası | Sähkömarkkinalaki (588/2013) | Şebeke, tedarik |
| Doğal gaz | Maakaasumarkkinalaki | Balticconnector sonrası piyasa |
| Rekabet | Kilpailulaki (948/2011) | KKV birleşme bildirimi |
| İş hukuku | Työsopimuslaki (55/2001) | Rekabet yasağı (2022 reformu) |

---

## Atıf formatı

```
[FI Mevzuat — {kanun adı} ({no}/{yıl}) — {akn_uri} — {status} — GG.AA.YYYY]
```
⚠️ `akn_uri` ve `status`'ü **`/list` çıktısından birebir kopyala**.

---

*Test: 30.08.2026 — `/v3/api-docs` (gzip, 37 yol) ✅ · `/act/statute-consolidated/list`
✅ · `/act/statute/2023` Akoma Ntoso XML ✅ · `{lang@sürüm}` olmadan `main.akn`
"No entry found" ❌ (tuzak belgelendi) · kök adres 403 (normal). Sürüm: v1.6.0 (yeni).*
