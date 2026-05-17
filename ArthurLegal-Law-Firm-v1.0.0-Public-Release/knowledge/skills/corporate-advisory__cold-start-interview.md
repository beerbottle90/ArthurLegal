---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. Kurumsal müvekkil portföyü
  (KOBİ + aile şirketi + mid-cap), GK/YK yıllık takvim, küçük M&A deneyimi,
  aile çatışması matter alışkanlığı, TTSG/MERSİS işlem ritmi.
  Sonuç: tr-overlay/profiles/corporate-advisory.md güncellenir.
user-invocable: true
---

# Cold Start Interview — corporate-advisory

## Amaç

`tr-overlay/profiles/corporate-advisory.md` içindeki `[DOLDUR]` alanlarını doldur. ~10 dk.

## Adımlar

### 1. Kurumsal müvekkil portföyü

- Aktif kurumsal müvekkil sayısı
- Tip dağılımı: aile şirketi (1./2./3. nesil) / KOBİ / mid-cap / halka açık (varsa)
- Sürekli danışmanlık (retainer) müvekkil sayısı
- M&A müvekkili (alıcı / satıcı dağılımı)

### 2. GK/YK yıllık takvim

- Olağan GK Mart sonu (TTK m. 409) — kaç müvekkil için?
- YK kararları aylık tipik sayı
- TTSG tescil deneyimi (her büro hızlı veya yavaş — büronuz?)

### 3. Küçük M&A deneyimi

- Son 2 yılda kaç M&A matter'ı?
- Tipik bedel aralığı
- R&W insurance kullandınız mı (genelde TR'de yaygın değil)?
- Earn-out klozu deneyimi?
- Yabancı yatırımcı (4875 sayılı K.) süreç tecrübesi?

### 4. Aile çatışması matter'ı

- "Kardeş A vs. kardeş B" tipi matter'ı kabul ediyor musunuz?
- Conflict check ne kadar derin? (büro tarihinde ailenin diğer üyesi müvekkil olmuş olabilir)
- Etik duvarı (büyük büroda) deneyimi?

### 5. Eskalasyon

- M&A SPA imza → Yönetici Ortak + müvekkil yazılı
- Aile çatışması matter → Ortaklar Kurulu

## Çıktı

Profil güncellenir.

```
✓ Profil tamamlandı.

Sonraki adım: /corporate-advisory:gk-yk-karar-paketi veya /corporate-advisory:diligence-issue-extraction
Re-run: /corporate-advisory:cold-start-interview --redo
```
