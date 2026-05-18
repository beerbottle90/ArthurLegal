---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. Vergi davası hacmi, ağırlıklı
  vergi tipi (KV/KDV/ÖTV/transfer pricing/damga), dış YMM/SMMM koordinasyonu,
  uzlaşma vs. dava alışkanlığı, Danıştay vergi daireleri deneyimi.
  Sonuç: tr-overlay/profiles/tax-litigation.md güncellenir.
user-invocable: true
---

# Cold Start Interview — tax-litigation

## Amaç

`tr-overlay/profiles/tax-litigation.md` içindeki `[DOLDUR]` alanlarını doldur. ~10 dk.

## Adımlar

### 1. Vergi davası pratik modeli

- Aktif vergi davası hacmi
- Vergi tipi ağırlığı: KV / KDV / ÖTV / transfer pricing / damga / GVK / diğer
- Birincil venue: hangi vergi mahkemesi(leri)
- Danıştay vergi daireleri (3/4/7/9) deneyimi

### 2. Dış YMM / SMMM koordinasyonu

- Çalıştığınız dış YMM/SMMM firma adı, iletişim
- Her vergi matter'ında **YMM raporu** zorunlu mu?
- Müvekkilin kendi mali müşaviri var mı? (genelde KOBİ'de evet)

### 3. Uzlaşma vs. dava alışkanlığı

- "Hep önce uzlaşma" mı, "doğrudan dava" mı?
- Uzlaşma indirim oranı tipik (% kaç bekliyorsunuz?)
- Müvekkilin "uzlaşalım" baskısına nasıl yaklaşıyorsunuz?

### 4. Eskalasyon

- Tarhiyat > [TL] — Yönetici Ortak
- Transfer pricing → dış uzman + Ortaklar Kurulu
- VUK m. 359 (sahte fatura) → criminal-defense koordinasyon

### 5. (Opsiyonel) Seed dosyalar

| Dava | Mükellef | Vergi tipi | Tutar | Sonuç |
|---|---|---|---|---|

## Çıktı

Profil güncellenir.

```
✓ Profil tamamlandı.

Sonraki adım: /tax-litigation:vergi-davasi-prep
Re-run: /tax-litigation:cold-start-interview --redo
```
