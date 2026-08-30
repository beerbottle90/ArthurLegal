# İrlanda Hukuku — Kullanım Rehberi (Irish Statute Book ELI yöntemi)

> ✅ **Bu yargı çevresi için artık custom MCP server VAR (v1.6.0):**
> **`ie-statutebook MCP`** → `references/ie-statutebook-mcp-rehberi.md`. **Önce onu kullan** —
> arama, atıf sözleşmesi ve statü disiplini orada hazırdır.
>
> Bu dosya **WebFetch yedeğidir**: connector bağlı değilse kullanılır.
> Yedek yol daha dar ve kırılgandır — buradan üretilen atıfa
> **`(MCP kullanılmadı)`** kaydını düş.

> **Erişim tipi:** WebFetch (GET) — auth yok
> **Durum:** ✅ ELI URL'leri **madde düzeyinde** çalışıyor · ⚠️ arama API'si yok
> **Test:** 30.08.2026
> **[Müvekkil] bağlamı:** IE, common law + AB üyesi kombinasyonuyla İngiliz hukukuna
> alternatif AB-içi forum; uçak/ekipman kiralama ve holding yapıları. Brexit sonrası
> "AB içinde common law" arayan sözleşmelerde hukuk seçimi olarak karşına çıkar.

---

## Kaynak haritası

| Kaynak | İçerik | Durum (30.08.2026) |
|---|---|---|
| **irishstatutebook.ie ELI** | Kanunlar + SI'lar, **madde düzeyinde** | ✅ 200 |
| irishstatutebook.ie/eli/acts.html | Kanun dizini (yıl bazlı) | ✅ 200 |
| `/search`, `/searchresults.html` | ❌ 404 — arama yolu yok | ❌ |
| courts.ie | İçtihat | manuel |
| EUR-Lex CELLAR | AB-türevli IE mevzuatı (ENG) | ✅ |

---

## 1. ELI URL deseni — BİRİNCİL ✅

```
# Kanunun tamamı (yayımlandığı hâli)
https://www.irishstatutebook.ie/eli/{yıl}/act/{no}/enacted/en/html

# TEK MADDE — token tasarrufu için tercih et
https://www.irishstatutebook.ie/eli/{yıl}/act/{no}/section/{madde}/enacted/en/html
```

**Doğrulanmış (30.08.2026):**
- `/eli/2014/act/38/enacted/en/html` → **Companies Act 2014** ✅ 200
- `/eli/2014/act/38/section/1/enacted/en/html` → madde 1 ✅ 200

> 💡 **Madde düzeyinde çekmek IE'nin en kullanışlı özelliğidir.** Companies Act 2014
> 1.400+ maddedir; tamamını çekme — `section/{n}` ile ilgili maddeye in.

⚠️ **`enacted` = yayımlandığı hâl.** Irish Statute Book'un "Revised Acts" (konsolide)
külliyatı ayrıdır ve tüm kanunları kapsamaz. Değişiklik yapılmış bir maddeye
bakıyorsan `revisedacts` sürümünü ara; bulamazsan atıfa
`(enacted sürümü — sonraki değişiklikler kontrol edilmedi)` kaydını düş.

---

## 2. Arama

Arama endpoint'i **yok** (`/search` ve `/searchresults.html` → 404). Sıralama:

1. `https://www.irishstatutebook.ie/eli/acts.html` ✅ — yıl bazlı dizin; kanun
   numarasını buradan bul, sonra ELI deseniyle in.
2. **EUR-Lex CELLAR** (`lang:ENG`) — AB-türevli IE mevzuatı için.
3. **LexScholar MCP** — IE/common law doktrini.
4. **CourtListener'a güvenme** — o ABD içtihadıdır, İrlanda değil. IE içtihadı için
   `courts.ie` (manuel) veya BAILII.

---

## 3. [Müvekkil] için kritik IE mevzuatı

| Konu | Metin | Bağlantı |
|---|---|---|
| Şirketler | Companies Act 2014 (No. 38) | DAC/LTD kurulumu, yönetici görevleri |
| Sözleşme | common law + Sale of Goods Acts | Hukuk seçimi olarak IE |
| Enerji düzenleme | Electricity Regulation Act 1999 | CRU yetkileri |
| Rekabet | Competition Act 2002 | CCPC birleşme bildirimi |
| Vergi | Taxes Consolidation Act 1997 | Holding rejimi, stopaj |

---

## Atıf formatı

```
[IE Mevzuat — {Act adı} {yıl} (No. {no}) s.{madde} — enacted — GG.AA.YYYY]
```

---

*Test: 30.08.2026 — `/eli/2014/act/38/enacted/en/html` ✅ · `section/1/...` ✅ ·
`/eli/acts.html` ✅ · `/search` ve `/searchresults.html` 404 ❌. Sürüm: v1.6.0 (yeni).*
