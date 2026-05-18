---
name: idari-dava-prep
description: >
  Yeni idari dava ön-değerlendirme: İYUK m. 7 süre kritik kontrolü (60 g idare /
  30 g vergi / 30 g ÇED ivedi), görevli mahkeme tespiti (İdare Mh / Danıştay K.
  m. 24 istisnaları), husumet (davalı idare), m. 27 yürütmenin durdurulması
  değerlendirmesi, m. 11 üst makama başvuru opsiyonu, dava dilekçesi iskeleti.
user-invocable: true
---

# İdari Dava Ön-Değerlendirme

## Adımlar

### 1. İdari işlem özeti

- Hangi idare/kurum işlem yaptı?
- İşlem tipi: yıkım kararı / lisans iptal / idari para cezası / ÇED red / kurul kararı / disiplin
- Tebligat tarihi
- Müvekkilin pozisyonu (idari işlem muhatabı / üçüncü kişi etkilenmiş)

### 2. **Süre kritik kontrolü (İYUK m. 7)**

| Senaryo | Süre |
|---|---|
| **İdari işlem genel** | **60 g** |
| **Vergi mahkemesi** | **30 g** |
| **ÇED ivedi (m. 20/A)** | **30 g** (+ Danıştay temyiz 15 g) |
| Üst makama başvuru sonrası (m. 11) | 60 g + 60 g gizli ret |

⚠️ **Tebligat tarihi nedir?** Süre başlangıç noktası kontrolü. **Kalan gün < 7 ise 🔴 acil.**

### 3. Görevli mahkeme

**Genel:** İdare Mahkemesi (ilk derece)

**Danıştay K. m. 24 istisnaları (Danıştay ilk derece):**
- CB Kararnameleri
- Bakanlıkların düzenleyici işlemleri
- Sektör kurulu (EPDK / BDDK / SPK / Rekabet) **düzenleyici** işlemleri
- Yüksek yargı disiplin

**Vergi mahkemesi:** Vergi tarhiyatı, gümrük, harç → `tax-litigation` plugin'ine yönlendir

### 4. Husumet

- Davalı idare: hangi tüzel kişi? (Bakanlık + Genel Müdürlük + Kurum)
- Birden fazla idare yönlendi mi? (örn. ÇED'de Çevre Bakanlığı + ilgili Valilik)
- Müşterek idari işlem → birden fazla davalı

### 5. Hukuka aykırılık değerlendirmesi

- **Yetki** (idare bu işlemi yapma yetkisinde mi?)
- **Şekil** (gerekli prosedür izlendi mi? — örn. ÇED için duyuru + halk katılımı)
- **Sebep** (idare hangi olguya dayandı?)
- **Konu** (işlemin içeriği mevzuata uygun mu?)
- **Maksat** (kamu yararı amacı var mı, takdir yetkisinin yerinde kullanımı?)

### 6. **Yürütmenin durdurulması (m. 27) değerlendirmesi**

**İki şart birlikte:**
1. **Telafisi güç veya imkânsız zararlar** doğacak
2. İdari işlem **açıkça hukuka aykırı** olmalı

**Çoğu davada REDDEDİLİR.** Müvekkili gerçekçi beklenti ile bilgilendir.

YD talep edilecek mi?
- ✓ Evet → dilekçenin başında ayrı paragraf
- ✗ Hayır → süreçte sonradan da talep edilebilir (HMK ile uyum)

### 7. m. 11 — Üst makama başvuru opsiyonu

Dava açmadan önce **üst makama itiraz** (60 g) → cevap (60 g, sessizlik gizli ret).

- Avantaj: Bedelsiz, hızlı
- Dezavantaj: Süreyi durdurmaz **eğer ret çıkarsa** kalan süreyle dava açarsın
- Pratik: Genelde ÇED ve büyük lisans iptallerinde dava paralel + itiraz paralel

### 8. Yargı MCP emsal

```
mcp__claude_ai_Yargi_MCP__search_danistay_decisions(
  arananKelime="<konu>", daire="<ilgili — örn. 13. enerji, 10. çevre>"
)
```

### 9. Dava dilekçesi iskeleti

Çıktı: hak iddiası + delil + hukuka aykırılık + (varsa) YD talep gerekçesi + sonuç talebi.

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# İdari Dava Ön-Değerlendirme — [matter-slug]

## ⚠️ İnceleyen notu
- Kaynaklar: Yargı MCP [✓N] / Mevzuat MCP [✓]
- **Süre durumu: [N gün kaldı]** — KRİTİK / Normal
- Şiddet: 🔴/🟠/🟡/🟢

## İdari işlem
[İdare] — [tarih] — [işlem tipi]

## Süre kontrolü
- İYUK m. [7 / 20/A] — [60 g / 30 g]
- Tebligat tarihi: GG.AA.YYYY
- Süre bitiş: GG.AA.YYYY
- Kalan: N gün

## Görevli mahkeme
[İdare Mh / Danıştay (K. m. 24 istisnası)]

## Husumet (davalı)
[İdare tüzel kişi(leri)]

## Hukuka aykırılık değerlendirmesi
- Yetki: [değerlendirme]
- Şekil: [değerlendirme]
- Sebep: [değerlendirme]
- Konu: [değerlendirme]
- Maksat: [değerlendirme]

## YD talep
✓/✗ — gerekçe (telafisi güç + açıkça hukuka aykırı)

## m. 11 üst makama başvuru
✓/✗ — paralel mi?

## Emsal (Yargı MCP)
| Karar | Eğilim |

## Önerilen yol
1. Dava açma — son gün GG.AA.YYYY
2. (Varsa) YD talep + ayrı gerekçe
3. (Opsiyonel) m. 11 paralel itiraz

## Sonraki adımlar
- /administrative-litigation:yurutmenin-durdurulmasi (YD detay)
- /administrative-litigation:matter-workspace new
```

## Hatalar

- **30 g vs. 60 g karışırlığı** → Her zaman İYUK m. 7'yi çek + işlem tipini kontrol
- **ÇED davasında m. 20/A ivedi rejim atlanması** → 30 g + Danıştay temyiz 15 g unutulur
- **Üst makama başvurunun süreyi durdurduğu yanılgısı** → m. 11/2 "ret kararı tebliğinden itibaren süre yeniden başlar" — paralel taktik gerekli
