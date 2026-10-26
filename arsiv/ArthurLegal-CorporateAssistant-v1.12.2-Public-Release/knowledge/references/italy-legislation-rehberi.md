# İtalya Mevzuatı & İçtihadı — Kullanım Rehberi (v1.7.0)

> **Erişim tipi:** WebFetch (GET) — Normattiva doğrudan, auth yok
> **Auth:** Yok (Normattiva OpenData + Corte Costituzionale tamamen açık)
> **Kapsam:** İtalyan mevzuatı + Anayasa Mahkemesi; Corte di Cassazione ücretli
> **[ŞİRKET ADI] bağlamı:** İtalyan enerji şirketleri (ENI, Enel), Avrupa M&A karşı tarafı

---

## 1. Normattiva OpenData — İtalyan Mevzuatı

**Resmi İtalyan konsolide mevzuat platformu. Auth yok.**

URN-NİR formatı ile doğrudan erişim:
```
GET https://www.normattiva.it/uri-res/N2Ls?urn:nir:{tip}:{tarih};{numara}
```

**[ŞİRKET ADI] için kritik İtalyan mevzuatı:**

| Mevzuat | URN |
|---|---|
| Codice Civile (1942) | `urn:nir:stato:regio.decreto:1942-03-16;262` |
| Codice del Commercio (TUF yerine) | — |
| TUF — Finans Kanunu | `urn:nir:stato:decreto.legislativo:1998-02-24;58` |
| Codice del Consumo | `urn:nir:stato:decreto.legislativo:2005-09-06;206` |
| D.Lgs. 231/2001 (Şirket sorumluluğu) | `urn:nir:stato:decreto.legislativo:2001-06-08;231` |
| Decreto Legislativo GDPR uyumu | `urn:nir:stato:decreto.legislativo:2018-08-10;101` |
| Codice del Lavoro (İş kanunu toplamı) | Ayrı arama gerekli |

**Normattiva REST API arama:**
```
GET https://dati.normattiva.it/ricercaAtto?testoSearch={sorgu}&tipoAtto=DECRETO_LEGISLATIVO&annoVigore={YIL}
```

**Madde bazlı erişim:**
```
WebFetch("https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262~art1299",
         "Codice Civile m.1299 rücu hakkı")
```

---

## 2. Corte Costituzionale — SPARQL (Auth Yok, CC BY-SA)

**20.000+ karar, 1956'dan bugüne. SPARQL endpoint.**

```
POST https://dati.cortecostituzionale.it/sparql
Content-Type: application/sparql-query
Accept: application/sparql-results+json

SELECT ?decision ?date ?text WHERE {
  ?decision a :Sentenza .
  ?decision :hasTopic "energia" .
  ?decision :date ?date .
} ORDER BY DESC(?date) LIMIT 10
```

HTML araması (daha pratik):
```
WebFetch("https://www.cortecostituzionale.it/actionPronuncia.do?select_pronunce=sentenze_2024&tema={sorgu}",
         "Enerji vergisi anayasallık kararları")
```

---

## 3. Corte di Cassazione (Yargıtay) — Sınırlı Erişim

⚠️ **Italgiure** (tam metin veritabanı) **ücretli abonelik** gerektirir.

Ücretsiz seçenekler:
- **DeJure (Giuffré)** — kısmi ücretsiz erişim: `https://www.iusexplorer.it/`
- **Massimario** (özet kararlar): `https://www.cortedicassazione.it/corte-di-cassazione/massimario-e-ruolo/`
- **Giustizia Amministrativa** (TAR/Consiglio di Stato) — tamamen ücretsiz:
  ```
  WebFetch("https://www.giustizia-amministrativa.it/rito_sentenze_adunanza_plenaria.html",
           "Son Adunanza Plenaria kararları")
  ```

---

## 4. MISE / MASE — Enerji Bakanlığı Kararları

İtalyan enerji düzenleyici kararları:
```
WebFetch("https://www.mase.gov.it/energia/mercato-del-gas-naturale",
         "İtalya doğal gaz piyasası düzenlemeleri")
```

**ARERA** (enerji düzenleyicisi — İtalya EPDK'sı):
```
WebFetch("https://www.arera.it/it/inglese/arera_en.htm",
         "ARERA son tarife ve lisans kararları")
```

---

## Atıf formatı

```
[IT Mevzuat — {Kanun adı} Art.{no} — Normattiva — GG.AA.YYYY]
[Corte Cost. — Sentenza n.{no}/{YIL} — GG.AA.YYYY]
[Cass. — Sez.{daire} — n.{no}/{YIL} — GG.AA.YYYY]
```

---

## [ŞİRKET ADI] için özel notlar

- **ENI/Enel** ile M&A veya JV — **D.Lgs. 231/2001** şirket cezai sorumluluğu önemli
- **TUF (58/1998)** — Borsa Milano'da kote İtalyan şirketleri için içeriden öğrenenlerin ticareti kuralları
- İtalya **GDPR uygulama otoritesi Garante** en aktif AB DPA'larından biri
- **Avrupa Enerji Şartı (ECT)** davalarında İtalyan tahkim precedenti: CourtListener + ICSID

*Son güncelleme: 29.05.2026 — v1.7.0. Normattiva + Corte Costituzionale entegrasyonu.*
