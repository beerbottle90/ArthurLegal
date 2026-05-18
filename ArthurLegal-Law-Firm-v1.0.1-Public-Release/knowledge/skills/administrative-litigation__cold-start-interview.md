---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. İdari yargıda aktif dava hacmi,
  sektör kurumu (EPDK/BDDK/SPK/KVKK Kurulu/Rekabet) deneyimi, birincil venue
  (İdare Mh + BİM + Danıştay), yürütmenin durdurulması talep alışkanlığı.
  Sonuç: tr-overlay/profiles/administrative-litigation.md güncellenir.
user-invocable: true
---

# Cold Start Interview — administrative-litigation

## Amaç

`tr-overlay/profiles/administrative-litigation.md` içindeki `[DOLDUR]` alanlarını doldur. ~10 dk.

## Adımlar

### 1. İdari dava pratik modeli

- Aktif idari dava hacmi
- Tipik müvekkil: KOBİ / enerji şirketi / ihale yüklenicisi / ÇED itirazcısı / KVKK ihlali
- Birincil venue:
  - İdare Mh.: hangi şehir(ler)
  - BİM: İstanbul / Ankara / başka
  - Danıştay: Ankara — hangi daire(ler) ile en çok iş

### 2. Sektör kurumu deneyimi

- EPDK kararlarına dava (enerji)?
- BDDK kararlarına dava (bankacılık)?
- SPK kararlarına dava (sermaye piyasası)?
- KVKK Kurulu kararlarına dava (kişisel veri)?
- Rekabet Kurulu kararlarına dava?
- KİK kararlarına dava (ihale)?

### 3. Yürütmenin durdurulması alışkanlığı

- Tipik matter'larda YD talep ediyor musunuz (her seferinde / seçici)?
- Müvekkili gerçekçi beklenti ile hazırlıyor musunuz (çoğu reddedilir)?

### 4. Ankara koordinasyonu

- Büronuzda Ankara ofisi / Ankara irtibat ortağı var mı?
- Danıştay duruşmalarında bizzat mı, dış muhabir avukat mı?

### 5. Eskalasyon eşikleri

- İdari para cezası iptal davası — onay yetkisi
- Lisans iptal riski → otomatik Yönetici Ortak
- Üst yargı yolu (BİM istinaf, Danıştay temyiz)

## Çıktı

Profil güncellenir.

```
✓ Profil tamamlandı.

Sonraki adım: /administrative-litigation:idari-dava-prep
Re-run: /administrative-litigation:cold-start-interview --redo
```
