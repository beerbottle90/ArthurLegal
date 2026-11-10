# Avusturya Hukuku — Kullanım Rehberi (RIS OGD API yöntemi)

> ✅ **Bu yargı çevresi için artık custom MCP server VAR (v1.6.0):**
> **`at-ris MCP`** → `references/at-ris-mcp-rehberi.md`. **Önce onu kullan** —
> arama, atıf sözleşmesi ve statü disiplini orada hazırdır.
>
> Bu dosya **WebFetch yedeğidir**: connector bağlı değilse kullanılır.
> Yedek yol daha dar ve kırılgandır — buradan üretilen atıfa
> **`(MCP kullanılmadı)`** kaydını düş.

> **Erişim tipi:** WebFetch (GET) — auth yok, API anahtarı yok
> **Durum:** ✅ **Mevzuat VE içtihat tek API'de**, tam metin araması çalışıyor
> **Test:** 30.08.2026 — canlı doğrulandı
> **[Müvekkil] bağlamı:** AT, OMV/gaz depolama ve Baumgarten hub'ı üzerinden Orta Avrupa
> gaz ticaretinin merkezi; ayrıca Alman hukuk ailesine yakın olduğu için DE analizlerinde
> karşılaştırmalı destek verir.

---

## Kaynak haritası

| Kaynak | İçerik | Durum (30.08.2026) |
|---|---|---|
| **RIS OGD API v2.6** | Federal mevzuat + **OGH/VwGH/VfGH içtihadı** | ✅ 200 |
| ris.bka.gv.at | Web arayüzü (aynı külliyat) | manuel |
| EUR-Lex CELLAR | AB-türevli AT mevzuatı, DEU dilinde | ✅ |

> ⚠️ **Sürüm tuzağı:** `v2.5` yolu **404** veriyor. **`v2.6` kullan.**

---

## 1. Mevzuat — `Bundesrecht` uygulaması ✅

```
GET https://data.bka.gv.at/ris/api/v2.6/Bundesrecht
      ?Applikation=BrKons
      &Suchworte={ARAMA}
      &DokumenteProSeite=Ten
```
Doğrulandı: `?Applikation=BrKons&Suchworte=Aktiengesetz&DokumenteProSeite=Ten`
→ `Hits: 1423` ✅

`DokumenteProSeite`: `Ten` | `Twenty` | `Fifty` | `OneHundred`
Sayfalama: `&Seitennummer={n}`

**Yanıt yapısı (JSON):**
```
OgdSearchResult.OgdDocumentResults.Hits.#text            → toplam sonuç
OgdSearchResult...OgdDocumentReference[].Data.Metadaten
   .Technisch.ID                                          → ör. NOR11012319
   .Allgemein.DokumentUrl                                 → ELI URL'si
   .Bundesrecht.Kurztitel                                 → kanunun kısa adı
   .Allgemein.Geaendert                                   → son değişiklik tarihi
```

`DokumentUrl` doğrudan **ELI**'dir, ör.
`https://ogd.ris.bka.gv.at/eli/bgbl/1991/68/P0/NOR11012319` — atıfta bunu kullan.

---

## 2. İçtihat — `Judikatur` uygulaması ✅

```
GET https://data.bka.gv.at/ris/api/v2.6/Judikatur
      ?Applikation=Justiz
      &Suchworte={ARAMA}
      &DokumenteProSeite=Ten
```
Doğrulandı: `?Applikation=Justiz&Suchworte=Konkurrenzklausel` → `Hits: 148`,
ilk kayıt OGH `JJR_19920512_OGH0002_0040OB00030_9200000_001` ✅

**`Applikation` değerleri:**

| Değer | Mahkeme |
|---|---|
| `Justiz` | OGH (Yargıtay) + alt adli mahkemeler |
| `Vwgh` | Verwaltungsgerichtshof (İdare Yüksek Mah.) |
| `Vfgh` | Verfassungsgerichtshof (Anayasa Mah.) |
| `Bvwg` | Bundesverwaltungsgericht |

> 💡 **İsviçre ve Almanya ile birlikte kullan:** AT/DE/CH üçlüsü aynı hukuk ailesindendir.
> Bir Konkurrenzverbot/Konkurrenzklausel sorusunda üçünü paralel tarayıp
> karşılaştırmak, tek yargı çevresine bakmaktan çok daha güçlü bir analiz verir
> (`switzerland-caselaw-rehberi.md`, `de-eli-mcp-rehberi.md`).

---

## 3. [Müvekkil] için kritik AT mevzuatı

| Konu | Kanun | Bağlantı |
|---|---|---|
| Gaz piyasası | Gaswirtschaftsgesetz (GWG) | Baumgarten hub, depolama, şebeke |
| Elektrik | ElWOG / EIWOG | Şebeke erişimi, tedarik |
| Şirketler | AktG · GmbHG | AG/GmbH kurulumu, JV |
| Borçlar | ABGB | Tedarik sözleşmeleri |
| Rekabet | Kartellgesetz (KartG) | BWB birleşme bildirimi |
| İş hukuku | AngG · ArbVG | Yönetici sözleşmesi, Konkurrenzklausel |

---

## Atıf formatı

```
[AT Mevzuat — {Kurztitel} — {DokumentUrl ELI} — GG.AA.YYYY]
[AT İçtihat — {mahkeme} — {Technisch.ID} — GG.AA.YYYY]
```
⚠️ ELI ve belge ID'sini **API çıktısından birebir kopyala**.

---

*Test: 30.08.2026 — `v2.6/Bundesrecht?Suchworte=Aktiengesetz` → 1423 hit ✅ ·
`v2.6/Judikatur?Applikation=Justiz&Suchworte=Konkurrenzklausel` → 148 hit ✅.
`v2.5` yolunun 404 verdiği tespit edildi. Auth gerekmiyor. Sürüm: v1.6.0 (yeni).*
