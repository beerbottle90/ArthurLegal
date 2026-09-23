# Polonya Hukuku — Kullanım Rehberi (Sejm ELI API yöntemi)

> ✅ **Bu yargı çevresi için artık custom MCP server VAR (v1.6.0):**
> **`pl-sejm MCP`** → `references/pl-sejm-mcp-rehberi.md`. **Önce onu kullan** —
> arama, atıf sözleşmesi ve statü disiplini orada hazırdır.
>
> Bu dosya **WebFetch yedeğidir**: connector bağlı değilse kullanılır.
> Yedek yol daha dar ve kırılgandır — buradan üretilen atıfa
> **`(MCP kullanılmadı)`** kaydını düş.

> **Erişim tipi:** WebFetch (GET) — auth yok, API anahtarı yok
> **Durum:** ✅ **Tam ELI uyumlu REST API** — arama + metadata + tam metin (HTML/PDF)
> **Test:** 30.08.2026 — canlı doğrulandı
> **[Müvekkil] bağlamı:** PL, Orta Avrupa gaz/elektrik koridorunun düğüm noktası;
> Baltık–Adriyatik enerji altyapısı, AB enerji direktiflerinin sıkı transpozisyonu,
> emtia ticareti karşı tarafları.

---

## Kaynak haritası

| Kaynak | İçerik | Durum (30.08.2026) |
|---|---|---|
| **api.sejm.gov.pl/eli** | Dziennik Ustaw (DU) + Monitor Polski (MP) — **tam metin + statü** | ✅ 200 |
| isap.sejm.gov.pl | Web arayüzü (aynı külliyat) | manuel |
| EUR-Lex CELLAR | AB-türevli PL mevzuatı, POL dilinde | ✅ (`eurlex-cellar-rehberi.md`) |

---

## 1. Sejm ELI API — BİRİNCİL ✅

**ELI (European Legislation Identifier) uyumlu, auth yok, JSON.**

### Başlıkla arama

```
GET https://api.sejm.gov.pl/eli/acts/search?title={ARAMA}&limit=20
```
Doğrulandı: `?title=energetyczne&limit=2` → `{"count":2,"items":[...]}` ✅

Ek filtreler: `publisher=DU|MP`, `year=`, `type=`, `inForce=`, `offset=`.

### Yıla göre listeleme

```
GET https://api.sejm.gov.pl/eli/acts/{publisher}/{yıl}
örnek: https://api.sejm.gov.pl/eli/acts/DU/2024   → {"count":1984,...}  ✅
```

### Tek aktın metadata'sı

```
GET https://api.sejm.gov.pl/eli/acts/{publisher}/{yıl}/{pozisyon}
örnek: .../eli/acts/DU/2024/1984   ✅
```

Dönen alanlar — **atıf için doğrudan kullanılabilir**:

| Alan | Anlam |
|---|---|
| `displayAddress` | Resmî atıf dizesi, ör. `Dz.U. 2024 poz. 1984` |
| `title` | Aktın tam başlığı |
| **`status`** | ⚠️ **`obowiązujący` = yürürlükte** · `uchylony` = ilga · `wygaśnięcie` |
| `promulgation` / `announcementDate` | İlan / yayım tarihi |
| `textHTML` / `textPDF` | Tam metin formatı mevcut mu (bool) |
| `changeDate` | Son değişiklik zamanı |

### Tam metin

```
GET https://api.sejm.gov.pl/eli/acts/{publisher}/{yıl}/{poz}/text.html   ✅ 200
GET https://api.sejm.gov.pl/eli/acts/{publisher}/{yıl}/{poz}/text.pdf    ✅ 200
```
⚠️ Bazı aktlarda `textHTML:false` olur (yalnız PDF) — metadata'daki bayrağı **önce
kontrol et**, yoksa boş içerik alırsın.

```
WebFetch:
  URL: https://api.sejm.gov.pl/eli/acts/DU/2024/1984/text.html
  prompt: "{madde} maddesinin metnini çıkar; aktın statüsünü ve yayım tarihini belirt"
```

---

## 2. Statü disiplini (PL'de kritik)

Polonya mevzuatı sık değişir ve API **statüyü açıkça verir**. Bu, e-qanun (AZ)
kalıbının aynısıdır: **statü atıfın parçasıdır.**

```
✅ [PL Mevzuat — Dz.U. 2024 poz. 1984 — obowiązujący — 30.08.2026]
❌ [PL Mevzuat — Dz.U. 2024 poz. 1984]        ← statü yok, eksik atıf
```

`status` alanı `obowiązujący` değilse **metni yürürlükteki hukuk gibi sunma**;
ilga/değişiklik tarihini belirt.

---

## 3. [Müvekkil] için kritik PL mevzuatı

| Konu | Kanun | Bağlantı |
|---|---|---|
| Enerji | Prawo energetyczne | Lisans, şebeke erişimi, tarife |
| Şirketler | Kodeks spółek handlowych (KSH) | sp. z o.o. / S.A. kurulumu, JV |
| Borçlar/sözleşme | Kodeks cywilny | Tedarik sözleşmeleri, force majeure |
| Rekabet | Ustawa o ochronie konkurencji (UOKiK) | Birleşme bildirimi |
| Yenilenebilir | Ustawa o OZE | Destek mekanizmaları, açık artırma |
| Kamu ihalesi | Prawo zamówień publicznych | Devlet kurumlarıyla sözleşme |

---

## Atıf formatı

```
[PL Mevzuat — {displayAddress} — {status} — {title} — GG.AA.YYYY]
```
⚠️ `displayAddress` ve `status` alanlarını **API çıktısından birebir kopyala** —
`Dz.U.` numarasını elle kurma.

---

*Test: 30.08.2026 — `/eli/acts/search?title=energetyczne` ✅ · `/eli/acts/DU/2024`
→ 1984 kayıt ✅ · `/eli/acts/DU/2024/1984` metadata ✅ · `text.html` + `text.pdf`
200 ✅. Auth gerekmiyor. Sürüm: v1.6.0 (yeni).*
