# Almanya Mevzuatı & İçtihadı — Kullanım Rehberi (v1.7.0)

> **Erişim tipi:** WebFetch (GET) — MCP gerekmez
> **Auth:** Yok (gesetze-im-internet.de tamamen açık)
> **Kapsam:** Tüm Alman federal mevzuatı + BGH/BVerfG kararları
> **[Müvekkil] bağlamı:** Alman karşı taraflar (M&A, enerji), TANAP AB bağlantısı, Alman şirket hukuku

---

## 1. gesetze-im-internet.de — Federal Mevzuat

**Resmi Alman Federal Adalet Bakanlığı platformu. Auth yok.**

```
GET https://www.gesetze-im-internet.de/{KISALTMA}/
```

**[Müvekkil] için kritik Alman mevzuatı:**

| Mevzuat | Kısaltma | URL |
|---|---|---|
| BGB (Türk TBK eşdeğeri) | `bgb` | `https://www.gesetze-im-internet.de/bgb/` |
| HGB (Türk TTK eşdeğeri) | `hgb` | `https://www.gesetze-im-internet.de/hgb/` |
| AktG (Anonim şirket) | `aktg` | `https://www.gesetze-im-internet.de/aktg/` |
| GmbHG (Ltd şirket) | `gmbhg` | `https://www.gesetze-im-internet.de/gmbhg/` |
| EnWG (Enerji sektörü) | `enwg_2005` | `https://www.gesetze-im-internet.de/enwg_2005/` |
| GWB (Rekabet hukuku) | `gwb` | `https://www.gesetze-im-internet.de/gwb/` |
| UWG (Haksız rekabet) | `uwg_2004` | `https://www.gesetze-im-internet.de/uwg_2004/` |
| BDSG (Alman veri koruma) | `bdsg_2018` | `https://www.gesetze-im-internet.de/bdsg_2018/` |
| InsO (İflas) | `inso` | `https://www.gesetze-im-internet.de/inso/` |
| ZPO (Medeni yargılama) | `zpo` | `https://www.gesetze-im-internet.de/zpo/` |

**Belirli paragraf çekimi** (§ madde numarasıyla):
```
WebFetch("https://www.gesetze-im-internet.de/bgb/__242.html",
         "BGB §242 Treu und Glauben maddesinin içeriği")
```

---

## 2. NeuRIS — Yeni Federal Hukuk Bilgi Sistemi (Beta, 2025+)

**BGH, BVerfG ve 4 yüksek mahkeme + mevzuat. REST API, auth yok.**

```
GET https://api.rechtsinformationen.bund.de/v1/search?q={query}&type=NORM
GET https://api.rechtsinformationen.bund.de/v1/search?q={query}&type=ENTSCHEIDUNG
```

Swagger: `https://docs.rechtsinformationen.bund.de/`

**Mahkeme kararı örneği:**
```
WebFetch("https://api.rechtsinformationen.bund.de/v1/search?q=Energierecht+Konzessionsvertrag&type=ENTSCHEIDUNG",
         "Enerji konsesyon sözleşmesi alanında BGH kararlarını listele")
```

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
[DE Mevzuat — {Kanun adı} {§ veya Art.} — gesetze-im-internet.de — GG.AA.YYYY]
[BGH — {Esas no/tarih} — GG.AA.YYYY]
[BVerfG — {BVerfGE cilt/sayfa} — GG.AA.YYYY]
```

---

## [Müvekkil] için özel notlar

- Alman enerji şirketleri ile yapılan M&A/JV sözleşmelerinde **Deutsches Recht** klozuna dikkat
- EnWG m.3 vd. — Alman enerji piyasası düzenlemesi TANAP için ab-bağlantısı
- **BundesNetzAgentur (BNetzA)** kararları için: `https://www.bundesnetzagentur.de/EN/Areas/Energy/` (WebFetch)
- Alman şirket kurulumunda GmbHG/AktG + Handelsregister (HR): `https://www.unternehmensregister.de/`

*Son güncelleme: 29.05.2026 — v1.7.0. gesetze-im-internet.de + NeuRIS beta entegrasyonu.*
