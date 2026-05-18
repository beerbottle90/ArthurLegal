---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. Ceza müdafaa pratik modeli
  (CMK görevli + özel müvekkil dengesi), uzmanlık alanları (genel / ekonomik /
  beyaz yaka / basın), CMK gönüllü avukat listesi, müdahil vekilliği deneyimi.
  Sonuç: tr-overlay/profiles/criminal-defense.md güncellenir.
user-invocable: true
---

# Cold Start Interview — criminal-defense

## Amaç

`tr-overlay/profiles/criminal-defense.md` içindeki `[DOLDUR]` alanlarını doldur. ~10 dk.

## Adımlar

### 1. Ceza müdafaa pratik modeli

- Aktif ceza dosya hacmi
- Dağılım: özel müvekkil (genelde ücret peşin) / CMK görevli (Adalet Bakanlığı tarifesi) / müdahil
- Uzmanlık alanları: genel / ekonomik suç / beyaz yaka / basın / iş kazası ceza / bilişim

### 2. CMK görevli atama

- Hangi avukat(lar) baro CMK gönüllüsü listesinde?
- Aylık tipik CMK atama sayısı
- 48 saat sınırı içinde ulaşım — coğrafi kapsam (şehir içi / komşu il?)
- CMK ödeme cetveli teslim disiplini (aylık / kümülatif?)

### 3. Tutukluluk pratik modeli

- Tutukluluk duruşmasına genelde kim katılır (Kıdemli Ortak / bağlı avukat)?
- 7 günlük itiraz süresi takvim takibi yöntemi?
- Tutukluluk üst sınırı dolduğunda salıverme talebi standart mı?

### 4. Müdahil vekilliği

- Mağdur müvekkil temsilini yapıyor musunuz (genelde paralel hukuk davası)?
- Uzlaştırma teklif değerlendirme akışı?

### 5. Eskalasyon

- PEP / basın riski olan dosya → Yönetici Ortak
- AYM bireysel başvuru → Ortaklar Kurulu

## Çıktı

Profil güncellenir.

```
✓ Profil tamamlandı.

Sonraki adım: /criminal-defense:cmk-gorev-atama veya /criminal-defense:ifade-hazirlik
Re-run: /criminal-defense:cold-start-interview --redo
```
