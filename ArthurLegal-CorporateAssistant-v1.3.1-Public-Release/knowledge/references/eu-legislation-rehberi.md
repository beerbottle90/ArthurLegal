# AB Mevzuatı & CJEU/ECHR İçtihatı — Kullanım Rehberi (v1.7.0)

> **Erişim tipi:** WebFetch (GET) — MCP gerekmez
> **Auth:** Yok (EUR-Lex doğrudan erişim)
> **Kapsam:** Tüm AB tüzükleri, direktifler, CJEU kararları, ECHR içtihadı
> **[ŞİRKET ADI] bağlamı:** [BORU HATTI PROJESİ] AB bağlantısı, GDPR, AB yaptırım rejimleri, enerji direktifleri

---

## 1. EUR-Lex — CELEX numarasıyla doğrudan erişim

En hızlı yol: CELEX numarasını biliyorsan doğrudan çek.

```
GET https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{CELEX_NO}
```

**[ŞİRKET ADI] için kritik AB mevzuatı:**

| Mevzuat | CELEX | Konu |
|---|---|---|
| GDPR | `32016R0679` | Kişisel veri (10.000+ çalışan, AB iletişimi) |
| AI Act | `32024R1689` | Yapay zeka sistemleri (2025 yürürlük) |
| NIS2 Direktifi | `32022L2555` | Siber güvenlik (enerji altyapısı — kritik) |
| DORA | `32022R2554` | Dijital operasyonel dayanıklılık (finans/enerji) |
| AB Taksonomi (enerji) | `32021R2139` | Sürdürülebilir enerji sınıflandırması |
| EU ETS | `32003L0087` | Emisyon ticaret sistemi ([RAFİNERİ]) |
| 3. Enerji Paketi — Gaz | `32009L0073` | [BORU HATTI PROJESİ]'a uygulanabilir AB gaz direktifi |
| 3. Enerji Paketi — Elektrik | `32009L0072` | [ELEKTRİK SANTRALİ] için AB elektrik direktifi |
| Gaz Güvenliği Yönetmeliği | `32017R1938` | Tedarik güvenliği ([BORU HATTI PROJESİ] güzergâhı) |
| Russia Sanctions (son) | `32022R0428` | AB Rusya yaptırımları (temel tüzük) |
| TFEU (Rekabet m.101/102) | `12012E/TXT` | AB rekabet hukuku |

**Örnek:**
```
WebFetch("https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679",
         "GDPR m.83 idari para cezası tavanını ver")
```

---

## 2. EUR-Lex Arama (konu bazlı)

CELEX bilinmiyorsa metin araması:
```
GET https://eur-lex.europa.eu/search.html?type=ALL&text={encoded_query}&lang=en
```

Örnek: `https://eur-lex.europa.eu/search.html?type=ALL&text=LNG+terminal+licensing&lang=en`

---

## 3. CJEU Kararları (EUR-Lex üzerinden)

CJEU kararları EUR-Lex'te CELEX formatıyla indekslenmiştir:
- Format: `6{YIL}CJ{DAVA_NO}` (ör. `62019CJ0715`)
- Direkt URL: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:6{YIL}CJ{DAVA_NO}`

Belirli kararı bulmak için InfoCuria arama:
```
WebFetch("https://curia.europa.eu/juris/liste.jsf?language=en&td=ALL&text={query}",
         "Enerji piyasası rekabet kararlarını listele")
```

---

## 4. ECHR — HUDOC (Avrupa İnsan Hakları Mahkemesi)

**İstanbul Sözleşmesi, mülkiyet hakkı (P1-1), adil yargılanma (m.6) [ŞİRKET ADI] için ilgili.**

```
GET https://hudoc.echr.coe.int/app/query/results?query=contentsitename:ECHR+AND+doctypebranch:JUDGMENTS+AND+article:P1-1&select=itemid,docname,judgementdate&sort=judgementdate+Descending
```

Belirli karar: Bir davayı bulduktan sonra tam metin:
```
WebFetch("https://hudoc.echr.coe.int/eng#{itemid}", "Kararın özeti ve gerekçesi")
```

---

## 5. AB Yaptırım Listesi (konsolide)

OpenSanctions zaten aktif; ek olarak AB resmi yaptırım listesi:
```
WebFetch("https://www.sanctionsmap.eu/api/v1/sanction?include_draft=0&lang=en",
         "Rusya ve İran yaptırım listesi özeti")
```

---

## Atıf formatı

```
[EU Legislation — CELEX:{no} — GG.AA.YYYY]
[CJEU — {Dava adı, C-no/YIL} — GG.AA.YYYY]
[ECHR — {Dava adı} — GG.AA.YYYY]
```

---

## Sınırlamalar

- EUR-Lex HTML çıktısı uzun olabilir; belirli madde numarası istenerek daralt
- CJEU kararları Fransızca/İngilizce; makine çevirisi için Claude'dan yardım al
- ECHR HUDOC resmi API değil, endpoint değişebilir

*Son güncelleme: 29.05.2026 — v1.7.0. EUR-Lex + CJEU + ECHR WebFetch entegrasyonu.*
