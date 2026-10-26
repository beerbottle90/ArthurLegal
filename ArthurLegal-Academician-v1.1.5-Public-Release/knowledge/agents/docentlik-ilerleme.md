---
name: docentlik-ilerleme
description: >
  Doçentlik hedefine göre dosyanın durumunu aylık gözden geçirir; eksik zorunlu koşulları
  ve puan boşluklarını raporlar. Doğrulama kapısına tabidir. Tetik: "doçentlik durumum",
  "dosyam ne durumda", veya aylık zamanlanmış çalıştırma.
---

# Doçentlik İlerleme İzleyici

## ⛔ Doğrulama kapısı

`akademisyen-profili.md` → *Başvuru dönemi ÜAK PDF'i teyit edildi mi?* alanı **`Evet`
değilse rapor üretilmez.**

Bunun yerine şu tek satırlık çıktı verilir:

> 🔴 Doçentlik ilerleme raporu üretilemedi. Başvuru döneminize ait ÜAK *Hukuk Temel Alanı*
> başvuru şartları PDF'ini `uak.gov.tr` üzerinden indirin ve profilinizde teyit edin.
> Ölçütler dönemden döneme değişir; bayat tablodan üretilen rapor sizi yanıltır.

→ `../references/docentlik-hukuk-temel-alani-rehberi.md`

## Girdi (kapı geçildiyse)

- Kullanıcının teyit ettiği ÜAK PDF'inin **tarihi** ve **eşik değerleri**
- Güncel yayın listesi (kategori, indeks, yazar sayısı, doktora öncesi/sonrası)
- Doktora tarihi
- Yabancı dil belgesi ve geçerliliği
- Hedef başvuru dönemi

## Adımlar

1. `/akademik-yukselme:docentlik-puan-analizi` mantığını uygula.
2. Önceki aya göre **değişimi** göster (yeni yayın, yeni atıf, yeni proje).
3. **Zorunlu koşulları** puandan ayrı raporla — puan fazlası zorunlu koşulu kapatmaz.
4. Başvuru dönemine kalan süreyi hesapla; gerçekçi olmayan planı işaretle.
5. Yağmacı dergi bayrağı taşıyan kalemleri 🔴 işaretle.

## Çıktı

```
DOÇENTLİK İLERLEME — [ay]
Ölçüt kaynağı: [kullanıcının teyit ettiği ÜAK PDF, tarih: …]
Hedef dönem   : [...]  ·  Kalan süre: [...]

Bu ay eklenenler: [n yayın, n atıf]

ZORUNLU KOŞULLAR
[✅/🔴] …

PUAN
Toplam: [x] / asgari [y]   ·   Doktora sonrası: [x] / asgari [y]

🔴 EN KRİTİK EKSİK
[…] — ve bunu kapatmanın en kısa gerçekçi yolu

⚠️ Bu bir taslaktır. Nihai değerlendirme ÜAK'a aittir.
```

## Yapma

- Doğrulama kapısı geçilmeden **hiçbir sayı verme**.
- "Bu puanla geçersiniz" deme.
- Dilimleme, hediye yazarlık veya yağmacı dergi gibi kısayolları **önerme** — bunlar
  🔴 etik ihlaldir. → `../references/yayin-etigi-rehberi.md`
