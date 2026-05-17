---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. İşveren/işçi tarafı dengesi,
  aylık matter hacmi, mobbing iddia deneyimi, iş davası arabuluculuk pratiği,
  toplu sözleşme / sendika koordinasyonu (varsa).
  Sonuç: tr-overlay/profiles/employment-advisory.md güncellenir.
user-invocable: true
---

# Cold Start Interview — employment-advisory

## Amaç

`tr-overlay/profiles/employment-advisory.md` içindeki `[DOLDUR]` alanlarını doldur. ~10 dk.

## Adımlar

### 1. İşveren/işçi taraf dengesi

- Aylık iş hukuku matter hacmi
- İşveren tarafı %?
- İşçi tarafı %?
- Conflict check ekstra sıkı uygulama beyanı

### 2. İşveren müvekkil profili

- Tipik işveren tipi: KOBİ / mid-cap / büyük endüstri
- Sürekli danışmanlık (retainer) işveren müvekkili var mı?
- TİS / sendika ilişkisi olan işveren?

### 3. İşçi müvekkil profili

- Tipik işçi tipi: orta-üst kademe (kıdem yüksek) / mavi yaka / yönetici
- Toplu işçi davası deneyimi (örn. tek bir işverenin toplu fesih)
- Pro bono / yoksul işçi davası alıp almama

### 4. Mobbing + iş kazası deneyimi

- Mobbing iddialı matter sayısı (yıllık)
- İş kazası tazminat davası deneyimi
- Paralel ceza davası (TCK 89) — kim takip ediyor (kendinin / dış)?

### 5. Arabuluculuk pratiği

- Hangi arabuluculuk merkezi/arabulucu ile çalışılıyor?
- Hesaplama paketinin standart şablonu var mı?
- Sulh teklif değerlendirme matrisi standart mı?

### 6. Eskalasyon

- Mobbing iddia + basın riski → Yönetici Ortak
- Toplu işten çıkarma danışmanlığı → Yönetici Ortak

## Çıktı

Profil güncellenir.

```
✓ Profil tamamlandı.

Sonraki adım: /employment-advisory:fesih-degerlendirme veya /employment-advisory:isci-alacak-hesabi
Re-run: /employment-advisory:cold-start-interview --redo
```
