---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. Büro pratik modeli, aktif dava
  hacmi, birincil yakıcı sorun, dış vekil ağı (varsa), eskalasyon eşikleri,
  vekalet ücreti modeli, AAÜT katsayı tercihi soru-cevap ile doldurulur.
  Sonuç: tr-overlay/profiles/dispute-litigation.md güncellenir.
user-invocable: true
---

# Cold Start Interview — dispute-litigation

## Amaç

`tr-overlay/profiles/dispute-litigation.md` içindeki `[DOLDUR]` alanlarını **kullanıcı sohbeti** ile doldurmak. ~10-15 dakika.

## Ön gereksinim

- `firm-profile.md` doldurulmuş olmalı (`/firm-operations:cold-start-interview` önce çalıştırılmış).
- Yoksa: "Önce büro profilini doldur" diyerek `/firm-operations:cold-start-interview` öner.

## Adımlar

### 1. Büro pratik modeli

- Aktif dava hacmi (yaklaşık adet)
- Davaların ağırlık dağılımı: ticari / iş / icra / kira / aile / diğer
- Birincil müvekkil tipi (KOBİ / bireysel / kurumsal)
- Birincil venue (İstanbul Çağlayan / Anadolu / Bakırköy / başka şehir)

### 2. "Yakıcı sorun" tespiti

> "Bu pratik alanında sizi en çok yoran tek bir şey nedir?"

Cevabı profile yaz — bu pluginin tüm skill'leri bu alanda **ekstra dikkat** gösterecek.

### 3. Vekalet ücreti modeli

- Peşin avans + başarı bonusu modeli mi?
- Saatlik ücret mi?
- Karma mı?
- AAÜT × ne katsayı?
- Başarı bonusu oranı (%X, max %25)?
- Karşı yan vekalet ücreti müvekkille mi paylaşılır, vekilde mi kalır?

### 4. Eskalasyon eşikleri

- Sulh teklif kabul/red karar yetkisi (kim, hangi tutardan sonra Yönetici Ortak'a danışılır)
- İstinaf/temyiz kararı yetkisi
- Tutar dışı otomatik eskalasyon tetikleyicileri (PEP, basın, halka açık karşı yan vd.)

### 5. Birincil entegrasyonlar

- UYAP Avukat Portalı kullanıyor musunuz? (her ortak/avukat ayrı oturum mu?)
- KEP adresi (büro + her ortak?)
- iManage / SharePoint / Drive matter yönetimi?
- Dedicated dava yönetim yazılımı? (Clio, TimeSolv, Excel, dahili)

### 6. (Opsiyonel) Seed davalar

> "Önemli emsal davalardan birkaç tanesini özetler misiniz? Bu davalar bu plugin'in playbook'unu öğrenmesine yardım eder."

Müvekkil rumuz + dava tipi + sonuç + öğrenilen ders.

## Çıktı

`tr-overlay/profiles/dispute-litigation.md` güncellenir; `[DOLDUR]` alanları doldurulur.

```
✓ Profil tamamlandı.

Sonraki adım:
- İlk davanız için /dispute-litigation:case-intake çalıştırın.
- Veya mevcut bir matter'da çalışıyorsanız /dispute-litigation:matter-workspace switch.

Re-run: /dispute-litigation:cold-start-interview --redo
```

## Hatalar / kenar durumlar

- **Kullanıcı "bilmiyorum" der bir alana** → atla, `[DOLDUR]` bırak. Sonra dolduracak.
- **Kullanıcı tüm soruları cevaplamak istemez** → "Minimal profile yeterli. 5 dakikalık quick start mı, full 15 dk mı?"
- **Kullanıcı `firm-profile.md` doldurmadan başlatırsa** → Önce büro profili öneri.
