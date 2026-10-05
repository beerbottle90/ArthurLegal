---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. Sözleşme tip envanteri (NDA,
  hizmet, satış, distribütörlük, lisans, JV vd.), aylık sözleşme hacmi, müvekkil
  pozisyon tipi (A/B/C tarafı dağılımı), uyuşmazlık çözüm klozu tercihi.
  Sonuç: tr-overlay/profiles/commercial-advisory.md güncellenir.
user-invocable: true
---

# Cold Start Interview — commercial-advisory

## Amaç

`tr-overlay/profiles/commercial-advisory.md` içindeki `[DOLDUR]` alanlarını doldur. ~10 dk.

## Adımlar

### 1. Sözleşme pratik modeli

- Aylık sözleşme hacmi (yazma + inceleme karışık)
- Aylık ihtarname hacmi
- Tipik sözleşme tipleri ağırlık sırasıyla

### 2. Müvekkil pozisyonu dağılımı

- A-tarafı (güçlü, standart şartları dayatabilir) — %?
- B-tarafı (denk müzakere) — %?
- C-tarafı (zayıf, karşı yanın şablonunu kabul) — %?

### 3. Şablon kütüphanesi

- Büro içi standart şablon kütüphanesi var mı? (varsa konum/yöntem)
- Anthropic/üçüncü taraf şablonlar kullanılıyor mu?
- Şablon güncelleme süreci? (kim, ne sıklıkta?)

### 4. Uyuşmazlık çözüm klozu tercihleri

- Yurtiçi müvekkil tipik → mahkeme klozu (hangi mahkeme?)
- Yurtdışı karşı yan tipik → tahkim (ISTAC / ICC / LCIA / başka?)
- Yatırımcı korumalı sözleşmeler → BIT/ICSID kapsamı?

### 5. Damga vergisi pratiği

- Müvekkilin damga vergisini ödediğini nasıl teyit ediyorsunuz?
- KEP teslim alışkanlığı (var/yok)?

### 6. Eskalasyon

- TBK 115 ihlal sinyali görülürse Yönetici Ortak
- "Yarın imzalanacak" baskısı durumunda 24 saat bekleme önerisi

## Çıktı

Profil güncellenir.

```
✓ Profil tamamlandı.

Sonraki adım: /commercial-advisory:draft-nda veya /commercial-advisory:review-contract
Re-run: /commercial-advisory:cold-start-interview --redo
```
