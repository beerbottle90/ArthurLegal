---
name: fesih-degerlendirme
description: >
  İşveren tarafı fesih danışmanlığı: 4857 m. 17/18/25 değerlendirme, geçerli/haklı
  fesih ayrımı, tahmini tazminat yükü (kıdem + ihbar + işe iade riski + boşta
  geçen süre tazminatı), arabuluculuk + dava akışı, hukuki risk skalası,
  müvekkil-yönetici brief.
user-invocable: true
---

# Fesih Değerlendirme (İşveren tarafı)

## Müvekkil + işçi bilgisi

- Müvekkil işveren tipi: KOBİ / mid-cap / büyük
- İşçi: hizmet süresi (yıl + ay), ücret (brüt + net), pozisyon, sözleşme tipi (belirli/belirsiz)
- **İşyerinde 30+ işçi var mı?** (işe iade şartı — 4857 m. 18)
- İşçinin 6+ ay hizmeti var mı? (işe iade şartı)
- Fesih sebebi (işveren versiyonu)

## Fesih tipi matrisi

### 1. İşveren haklı fesih (m. 25)

| Sebep | Madde |
|---|---|
| Sağlık | m. 25/I |
| Ahlak ve iyi niyet kurallarına uymayan davranış | m. 25/II |
| **Zorlayıcı sebep** (1 hafta+) | m. 25/III |
| **Devamsızlık** (ardı sıra 2 iş günü / 1 ayda 3 / yıl 5 iş günü) | m. 25/II-g |

**Sonuç:**
- Kıdem tazminatı **YOK**
- İhbar tazminatı **YOK**
- Yıllık izin **VAR**
- 6 işgünü içinde fesih hakkı (m. 26)

⚠️ **İspat yükü işverende** — disiplin tutanağı + tanık + savunma alma şart.

### 2. İşveren geçerli fesih (m. 18) — işe iade kapsamında

| Sebep | Madde |
|---|---|
| İşçinin yetersizliği | m. 18 |
| İşin gereği değişen durum | m. 18 |
| İşletme zorunluluğu | m. 18 |

**Sonuç:**
- Kıdem tazminatı **VAR**
- İhbar tazminatı **VAR**
- İşçi **işe iade davası** açabilir (30+ işçi + 6 ay hizmet + belirsiz süreli + 30 g içinde arabuluculuk)

**İşe iade davası riski:**
- İşçi kazanırsa: işe iade veya **işe iade etmemenin tazminatı** (4-8 ay brüt ücret) + **boşta geçen süre tazminatı** (max 4 ay)
- Yüksek maliyet → işveren tek taraflı fesih düşünürken bunu hesaba kat

### 3. İşveren tek taraflı (ihbarlı) fesih (m. 17)

| Hizmet | İhbar süresi |
|---|---|
| < 6 ay | 2 hafta |
| 6 ay - 1.5 yıl | 4 hafta |
| 1.5 - 3 yıl | 6 hafta |
| 3 yıl + | 8 hafta |

**Sonuç:**
- Kıdem tazminatı **VAR**
- İhbar tazminatı (süre kullanılmazsa) **VAR**
- 30+ işçi varsa **işe iade davası açabilir**

## Tahmini tazminat yükü hesabı

```
Kıdem tazminatı = (Hizmet yılı) × 30 günlük brüt ücret
                 ↑ kıdem tazminatı tavanı kontrol (2026 değeri)

İhbar tazminatı = (İhbar süresi) × günlük brüt ücret

Yıllık izin = (Kullanılmayan izin günü) × günlük brüt ücret

İşe iade davası kaybedilirse:
  + İşe iade etmemenin tazminatı = (4-8 ay brüt ücret)
  + Boşta geçen süre tazminatı = (max 4 ay brüt ücret)
```

**Örnek hesap:**
- İşçi: 8 yıl hizmet, brüt 50.000 TL/ay
- Kıdem: 8 × (50.000 / 30) × 30 = 400.000 TL (tavan kontrol gerekli)
- İhbar: 8 hafta × 50.000 / 4 = 100.000 TL (eğer süre kullanılmamış)
- İşe iade riski (m. 17 ile fesih): 6 ay × 50.000 = 300.000 TL (eğer kaybedersek)
- **TOPLAM RİSK:** 800.000 TL

## Arabuluculuk + dava akışı (işçi açar)

```
[Fesih]
    ↓
[İşçi: 30 g içinde arabuluculuk başvuru — İş Mh. K. m. 3]
    ↓
[Arabuluculuk 3-6 hafta]
    ↓
[Anlaşma → ilam] veya [Anlaşmama → tutanak]
    ↓
[Tutanak + 2 hafta içinde dava — İş Mh.]
    ↓
[Dava 1-2 yıl — istinaf eklenirse +1 yıl]
```

## Hukuki risk skalası

| Senaryo | Risk |
|---|---|
| Haklı fesih (m. 25) + güçlü ispat (tanık + disiplin) | 🟢 Düşük |
| Haklı fesih + zayıf ispat | 🟠 Yüksek (m. 18'e dönüşür) |
| Geçerli fesih (m. 18) — orta seviye işçi | 🟡 Orta |
| Geçerli fesih (m. 18) — sendikalı / mobbing iddialı | 🟠 Yüksek |
| Tek taraflı fesih (m. 17) — 30+ işçi + 6+ ay | 🟠 Yüksek (işe iade davası kesin) |
| Tek taraflı fesih — küçük işyeri (< 30 işçi) | 🟡 Orta (sadece kıdem+ihbar) |

## Çıktı

```markdown
[ÜST BAŞLIK]

# Fesih Değerlendirme — [Müvekkil işveren] / [İşçi rumuz]

## ⚠️ İnceleyen notu
- Kaynaklar: Mevzuat MCP [✓ 4857 m. X] / Yargı MCP [✓ 9./22. HD]
- Risk skoru: 🔴/🟠/🟡/🟢
- Önerilen fesih tipi: m. 17 / m. 18 / m. 25

## İşçi bilgisi
- Hizmet: [N yıl, X ay]
- Brüt ücret: [TL/ay]
- Pozisyon: [...]
- İşyeri büyüklüğü: [< 30 / ≥ 30 işçi]
- Belirsiz/belirli süreli: [...]

## Fesih sebebi (müvekkilin beyanı)
[Özet]

## Fesih tipi önerisi
[m. 25 (haklı) / m. 18 (geçerli) / m. 17 (tek taraflı)] — gerekçe

## Tahmini tazminat yükü
| Kalem | Tutar |
|---|---|
| Kıdem tazminatı | [TL] (tavan: [TL]) |
| İhbar tazminatı | [TL] |
| Yıllık izin | [TL] |
| (İşe iade risk) İşe iade etmemenin tazminatı | [TL — 4-8 ay] |
| (İşe iade risk) Boşta geçen süre | [TL — max 4 ay] |
| **TOPLAM RİSK** | **[TL]** |

## Hukuki risk
[Detaylı değerlendirme] — Risk: 🔴/🟠/🟡/🟢

## Önerilen yol
1. [Belge hazırlama — savunma alma, disiplin tutanağı]
2. [Fesih bildirim yazısı — şekil + içerik]
3. [SGK + İŞKUR bildirim takvim]
4. [Müvekkili olası dava sürecine hazırla]

## Sonraki adımlar
- /employment-advisory:matter-workspace new
- (Tahmini yük > [TL] ise) → Yönetici Ortak'a brief
- (İşe iade riski yüksek ise) sulh teklif değerlendirme şimdiden
```

## Hatalar

- **Haklı fesihte 6 iş günü süresini kaçırma** (m. 26) → geçerli feshe dönüşür
- **30 işçi eşiğini yanlış sayma** → işe iade davası riski yanlış değerlendirilir
- **Kıdem tavanını hesaba katmama** → yanlış tutar
- **İşçinin savunmasını almama** (m. 25/II tetiklerken) → fesih usulü hatası
- **Mobbing iddiası gizliyse görmezden gelme** → ek manevi tazminat davası riski
