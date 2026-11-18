# Excel çıktısı (`.xlsx`) — çalışma kitabı yapısı

> Tabular review ve benzeri toplu inceleme çıktılarının Excel biçimi.
> Google Sheets eşleniği: `gsheets-output.md` — **yapı birebir aynıdır**, yalnız
> yorum/not mekanizması ve yazma yolu farklıdır.

---

## Sayfalar

| Sayfa | İçerik |
|---|---|
| `Review` | Ana ızgara — satır başına bir belge, sütun başına bir veri noktası |
| `_sources` | Her hücrenin alıntısı ve konumu (gizli sütunların okunabilir kopyası) |
| `_schema` | Sütun tanımları — dosya kendi kendini belgeler |

## `Review` sayfası — sütun düzeni

```
A: Belge adı        B: Kaynak yol/ID     C: İnceleme tarihi
D: [Veri 1]         E: [Veri 1 _src]     F: [Veri 1 Verified]
G: [Veri 2]         H: [Veri 2 _src]     I: [Veri 2 Verified]
...
```

**Her veri sütununun üç bileşeni vardır:**

1. **Değer sütunu** — görünür. Çıkarılan cevap.
2. **`_src` sütunu** — **gizli**. Birebir alıntı + konum (`s.12 §4.2`). Gizli,
   çünkü ızgarayı okunmaz hâle getirir; silinmez, çünkü kanıt zinciridir.
3. **`Verified` sütunu** — görünür, **varsayılan boş**. İnceleyen kişi işaretler.

> ⚠️ `Verified` sütununu **asla önceden doldurma.** Bu sütunun tek anlamı
> "bir insan buna baktı"tır. Model tarafından doldurulursa denetlenebilirlik
> ortadan kalkar ve tablo olduğundan daha güvenilir görünür.

## Hücre yorumları

Görünür değer hücresine, `_src` içeriğini taşıyan bir **yorum** (comment) ekle —
fareyle üzerine gelince alıntı görünür. `openpyxl` ile:
`cell.comment = Comment(alinti_ve_konum, "ArthurLegal")`.

## Renk kodu — durum

| Renk | Anlam |
|---|---|
| Beyaz | Cevaplandı, alıntı var |
| Sarı | Belirsiz / inceleme gerekiyor (`needs_review`) |
| Gri | Belgede yok (`not_present`) |

> 🔴 **Boş hücre ile gri hücre aynı şey değildir.** Gri = "arandı, belgede yok".
> Boş = "bakılmadı". Ayrımı koru; kaybolursa tablo yanlış okunur.

## Üst bilgi ve dağıtım notu

İlk satıra plugin yapılandırmasındaki `## Outputs` iş-ürünü başlığını koy.
Yanına dağıtım notunu ekle (ör. *"Avukat incelemesi öncesi taslak — dış
dağıtıma kapalı"*).

## Yazma yolu

1. **Claude in Excel** (Office agent) — varsa tercih edilir.
2. **`openpyxl`** — yedek. Gizli sütun: `ws.column_dimensions['E'].hidden = True`.

## CSV eşleniği

Excel istenmiyorsa **iki CSV** üret: `review.csv` (değerler) ve
`review_sources.csv` (alıntılar + konumlar). Ana dosya temiz kalır, kanıt zinciri
eksilmez.

---

*Sürüm: v1.6.0 (yeni — daha önce atıf vardı, dosya yoktu).*
