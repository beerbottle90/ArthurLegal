# Google Sheets çıktısı — çalışma kitabı yapısı

> Excel eşleniği `excel-output.md`. **Yapı birebir aynıdır**: `Review`,
> `_sources`, `_schema` sayfaları; değer + gizli `_src` + `Verified` üçlüsü;
> beyaz/sarı/gri durum renkleri. Burada yalnız **Sheets'e özgü farklar** var.

---

## Excel'den farklar

| Konu | Excel | Sheets |
|---|---|---|
| Alıntı gösterimi | Hücre **yorumu** (comment) | Hücre **notu** (note) |
| Sütun gizleme | `column_dimensions[...].hidden` | `hideColumn` isteği (batchUpdate) |
| Renk | Hücre dolgusu | `repeatCell` → `userEnteredFormat.backgroundColor` |
| Yazma yolu | Claude in Excel → `openpyxl` | Sheets MCP → Sheets API (ADC) → CSV içe aktarma |

## Yazma yolu — sırayla dene

1. **Sheets MCP connector** — varsa en temizi.
2. **Sheets API + ADC** (Application Default Credentials).
3. **CSV içe aktarma** — yedek: `review.csv` + `review_sources.csv` üret,
   kullanıcı elle içe aktarsın. ⚠️ Bu yolda **notlar ve renkler kaybolur**;
   kullanıcıya bunu söyle, sessizce düşürme.

## Not (note) ekleme

```
batchUpdate → repeatCell → cell.note = "{birebir alıntı} — {konum}"
```
Not, **değer** sütununa eklenir; `_src` sütunu yine de gizli olarak durur, çünkü
notlar dışa aktarmada kaybolur.

## Paylaşım uyarısı

> 🔴 Sheets varsayılan olarak **paylaşılabilir bir bağlantı** üretir. İş ürünü
> avukat incelemesi öncesi taslaktır ve müvekkil gizli bilgisi taşır.
> **Paylaşım ayarını açıkça kısıtla** ve dosyayı oluşturduktan sonra kime açık
> olduğunu kullanıcıya bildir. Bu, Excel'de olmayan ek bir risktir.

---

*Sürüm: v1.6.0 (yeni — daha önce atıf vardı, dosya yoktu).*
