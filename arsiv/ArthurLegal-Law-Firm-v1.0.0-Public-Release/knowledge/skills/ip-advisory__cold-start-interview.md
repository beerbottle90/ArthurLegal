---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. IP portföy büyüklüğü, marka
  vekili lisansı (büro içi veya dış), Madrid Protokolü deneyimi, UDRP sıklığı,
  açık kaynak / yazılım müvekkili deneyimi.
  Sonuç: tr-overlay/profiles/ip-advisory.md güncellenir.
user-invocable: true
---

# Cold Start Interview — ip-advisory

## Amaç

`tr-overlay/profiles/ip-advisory.md` içindeki `[DOLDUR]` alanlarını doldur. ~10 dk.

## Adımlar

### 1. IP portföy

- Müvekkilleriniz adına aktif marka tescili (yaklaşık adet)
- Patent başvuru hacmi (yıllık)
- Tasarım tescil hacmi
- Telif hak yönetimi (kreatif/yazılım müvekkil)

### 2. Marka vekili lisansı

- Büro içi marka vekili lisanslı avukat var mı (varsa kim)?
- Yoksa dış marka vekili firma adı + iletişim?

### 3. Madrid Protokolü deneyimi

- Aylık/yıllık tipik Madrid başvuru sayısı
- Hangi ülkeler ağırlıkta? (EU / ABD / ortadoğu / başka?)
- WIPO'nun yıllık tarifesi takibi yöntemi?

### 4. UDRP + 5651 takedown deneyimi

- UDRP başvuru sıklığı
- 5651 sayılı K. içerik kaldırma (hosting ihtarname) sıklığı
- WIPO Arbitration vs. ulusal mahkeme tercihleri

### 5. Yazılım / açık kaynak müvekkil

- Yazılım stüdyosu müvekkil var mı?
- Açık kaynak lisans uyumu (GPL/MIT/Apache) ile çalıştınız mı?
- SaaS müvekkili tipik sözleşme yapısı?

### 6. Yenileme takvimi

- Marka yenileme reminder sistemi (10 yılda bir) — manuel mi, otomasyon mu?
- Yıllık yenileme hacmi

## Çıktı

Profil güncellenir.

```
✓ Profil tamamlandı.

Sonraki adım: /ip-advisory:marka-clearance veya /ip-advisory:marka-tescil
Re-run: /ip-advisory:cold-start-interview --redo
```
