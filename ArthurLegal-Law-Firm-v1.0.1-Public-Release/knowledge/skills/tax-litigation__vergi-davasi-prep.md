---
name: vergi-davasi-prep
description: >
  Yeni vergi davası ön-değerlendirme: İYUK m. 7 — 30 günlük süre KRİTİK kontrolü,
  uzlaşma vs. dava matrisi, Danıştay vergi daireleri (3/4/7/9) tespiti, YMM raporu
  ihtiyacı, hukuki dayanak, vergi mahkemesi dilekçe iskeleti.
user-invocable: true
---

# Vergi Davası Ön-Değerlendirme

## Adımlar

### 1. Tarhiyat özet bilgi

- Vergi türü: KV / KDV / ÖTV / GVK / KDV iade / damga / MTV
- Tarhiyat tutarı (vergi + cezalar — ayrı kalem)
- Vergi dönemi (hangi yıl/dönem?)
- İncelemeli (vergi inceleme raporu) mı, kendiliğinden mi?
- İhbarname / vergi/ceza ihbarnamesi tebligat tarihi

### 2. **Süre KRİTİK kontrolü (İYUK m. 7)**

⚠️ **30 GÜN — vergi mahkemesi dava süresi.** Tebligat tarihinden itibaren.

| Süre | Tarih |
|---|---|
| İhbarname tebliğ | GG.AA.YYYY |
| Süre bitiş | GG.AA.YYYY (+30 g) |
| Kalan gün | [N] |

**Kalan < 10 gün → 🔴 acil**

### 3. Uzlaşma vs. dava matrisi

| Faktör | Uzlaşma yönünde | Dava yönünde |
|---|---|---|
| Tarhiyat hukuki dayanağı zayıf | — | ✓ |
| Tarhiyat şüpheli ama müvekkil kabul ediyor | ✓ | — |
| Tutar küçük (< AAÜT × 2) | ✓ | — |
| Emsal değeri var (müvekkil aynı pozisyon devam edecek) | — | ✓ |
| Süre çok dar | — (önce dava, paralel uzlaşma değil — riskli) | ✓ |
| Yargısal başarı şansı yüksek | — | ✓ (>%50) |

⚠️ **VUK m. ek 11/2:** Uzlaşma vaki olmazsa dava açma süresi **yeniden başlamaz** — orijinal 30 g devam eder. **Uzlaşmaya gitmek süreyi durdurmaz.**

### 4. Danıştay vergi daireleri ayrımı

| Daire | Konu |
|---|---|
| 3. Daire | KV, ÖTV, damga, MTV, özel usulsüzlük |
| 4. Daire | KV, kurumlar vergisi istisnaları, transfer pricing |
| 7. Daire | KDV, damga, BSMV, gümrük |
| 9. Daire | KDV iade, KDV mahsup, KDV indirim |

Yargı MCP arama:
```
mcp__claude_ai_Yargi_MCP__search_danistay_decisions(
  arananKelime="<konu>", daire="vergi dava dairesi 9", baslangicTarihi="2023-01-01"
)
```

### 5. YMM/SMMM koordinasyonu

- Müvekkilin YMM raporu var mı?
- Yoksa: YMM raporu hazırlatmak gerekli mi? (genelde ek tarhiyatta evet)
- YMM raporu masrafı (~20.000-100.000 TL — matter ücretinden ayrı)

### 6. Hukuki dayanak değerlendirmesi

- **Vergi hatası** (matrah / hesap / vergi türü) — VUK m. 116-126 düzeltme yolu açık mı?
- **Hukuki yorum farkı** (idare yanlış yorumladı) — dava
- **Usul hatası** (inceleme süresi aşıldı, ifade hakkı verilmedi) — dava
- **Sahte/yanıltıcı belge iddiası** (VUK m. 359) — ⚠️ **CEZA DAVASI**, `criminal-defense` koordinasyon

### 7. VUK m. 359 — özel uyarı

Sahte/yanıltıcı belge iddiası varsa:
- 3 yıldan 8 yıla hapis cezası riski
- Tarhiyat vergi davası, savcılık ceza davası — **paralel**
- `criminal-defense` plugin koordinasyon zorunlu

### 8. Yürütmenin durdurulması (m. 27)

Vergi davasında YD:
- Telafisi güç + açıkça hukuka aykırı
- Genelde **teminat şartı** istenir (% — tarhiyatın belirli oranı)
- Müvekkilin nakit/teminat kapasitesi sorulmalı

### 9. Dilekçe iskeleti

1. Taraf bilgileri (mükellef + idare — vergi dairesi)
2. Tarhiyat özet
3. Hukuki dayanak (mükellef lehine)
4. Yargı MCP emsalleri
5. Bilirkişi/YMM raporu eki
6. Sonuç talep (iptal / kısmen iptal / yeniden tarhiyat)
7. YD talep (varsa)

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Vergi Davası Ön-Değerlendirme — [matter-slug] — Mükellef: [rumuz]

## ⚠️ İnceleyen notu
- Kaynaklar: Yargı MCP [✓ Danıştay X. Daire] / Mevzuat MCP [✓ VUK m. X]
- **Süre: [N gün kaldı]** — KRİTİK/Normal
- Şiddet: 🔴/🟠/🟡/🟢

## Tarhiyat
| Kalem | Tutar |
|---|---|
| Vergi | [TL] |
| Vergi ziyaı cezası | [TL] |
| Özel usulsüzlük | [TL] |
| **Toplam** | **[TL]** |

## Süre
- Tebligat: GG.AA.YYYY
- Bitiş: GG.AA.YYYY (+30 g İYUK m. 7)
- Kalan: N gün

## Uzlaşma vs. dava analizi
[Matris tamamlandı] → Önerim: [Uzlaşma / Dava / Karma]

## Danıştay daire
[3 / 4 / 7 / 9] — gerekçe

## YMM raporu
✓/✗ — varsa: [tarih, YMM adı]
Yoksa: tahmini maliyet [TL], önerilen YMM [...]

## Hukuki dayanak
[VUK / KVK / KDVK madde + içtihat]

## VUK m. 359 sinyali
✓/✗ — varsa → criminal-defense'e yönlendir

## YD talep
✓/✗ — teminat ihtiyacı [TL]

## Önerilen yol
1. [Uzlaşma — son gün GG.AA.YYYY VUK m. ek 11]
2. [Dava — son gün GG.AA.YYYY İYUK m. 7]
3. [Paralel uzlaşma + dava — riskli]

## Sonraki adımlar
- /tax-litigation:uzlasma-vs-dava (matris detay)
- /tax-litigation:matter-workspace new
- (varsa sahte belge) /criminal-defense:cmk-gorev-atama yönlendir
```

## Hatalar

- **30 g süreyi 60 g sanma (idari ile karıştırma)**
- **Uzlaşmanın süreyi durdurduğunu sanma** (VUK m. ek 11/2 — durmaz)
- **Danıştay vergi dairesini yanlış belirleme** → emsal eşleşmesi yanlış
- **VUK m. 359 sahte fatura sinyalini atlama** → ceza davası kaybı
