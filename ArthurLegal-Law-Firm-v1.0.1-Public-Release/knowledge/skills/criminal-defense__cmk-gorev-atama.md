---
name: cmk-gorev-atama
description: >
  Baro CMK servisinden gelen zorunlu müdafii atama yönetimi. 48 saat sınırı
  takibi (CMK m. 91), karakol/savcılık ifade öncesi hazırlık checklist, susma
  hakkı hatırlatma (CMK m. 147), tutukluluk değerlendirme + itiraz prosedürü
  (m. 268 7 g), CMK ödeme cetveli oluşturma.
user-invocable: true
---

# CMK Görev Atama Yönetimi

## Tetikleyici

Baro CMK servisinden telefon/SMS atama mesajı geldiğinde.

⚠️ **2 saat içinde teyit + 6 saat içinde yere ulaşma** — bu süreler kritik.

## Adımlar

### 1. Atama bilgisi al

- Atama no
- Müvekkil: TC kimlik son 4 rakam (rumuz)
- Suçlama (TCK m. X)
- Yer: karakol / cezaevi / mahkeme
- Zaman: ifade saati / duruşma saati
- Atama tipi: m. 150 zorunlu / m. 156 isteğe bağlı / talimat müdafiliği

### 2. **48 saat sınırı hesabı (CMK m. 91)**

| T | Olay | Süre |
|---|---|---|
| T+0 | Yakalama | — |
| T+24 | Savcılığa sevk şart | (toplu yakalamada T+48) |
| T+48 | Sulh ceza hakimine sevk + karar | Tutuklama veya salıverme |

⚠️ **48. saatten sonra hakim karar vermezse → resen salıverme.**

### 3. Müdafi atama reddi gerekçeleri

- **Conflict** (karşı tarafın vekiliyiz)
- **Sağlık** (acil tıbbi durum)
- **Aynı anda başka acil iş** (mevcut duruşma)
- **Coğrafi imkansızlık** (uzak şehir)

Red yazılı + gerekçeli. Sürekli red → CMK gönüllü listesinden çıkarılma.

### 4. Karakol/cezaevi görüşmesi — kontrol listesi

- [ ] Müvekkil kimlik (TC + isim)
- [ ] **Susma hakkı (CMK m. 147/1-e) hatırlat** — yazılı not müvekkile imzalat
- [ ] Yakalama tarihi/saati öğren
- [ ] Suçlama özetini savcının dosyasından al
- [ ] Müvekkilin **kendi anlatımı** (mahremiyet — CMK m. 154)
- [ ] Avukatın kanaati: "ifade ver / verme / kısmi cevap"
- [ ] Tutuklama olasılığı ön değerlendirme
- [ ] Müvekkilin ailesini bilgilendirme isteği var mı?
- [ ] **Av. K. m. 35 müdafi vekaleti** (yazılı talep — noter şart değil)

### 5. İfade tutanağı kontrol

- Müvekkilin söylediği noktasal mı?
- Yönlendirici soru var mı?
- "Susma hakkımı kullanıyorum" ifadesi kayıt mı?
- Müvekkil + müdafi imzası tamam mı?

⚠️ **Müdafi olmadan alınan ifade kanıt olarak kullanılamaz** (CMK m. 147/1-h).

### 6. Sulh ceza hakimliği duruşması (tutuklama)

Hakim **CMK m. 100** şartlarını değerlendirir:
1. Kuvvetli suç şüphesi
2. Kaçma şüphesi / delil karartma / suça yeniden başlama
3. Adli kontrol yetersizliği

**Müdafi savunma noktaları:**
- Delilin yetersizliği (kuvvetli şüphe yok)
- Yerleşik adres + aile + iş (kaçma şüphesi yok)
- Adli kontrol yeterli (ev hapsi, imza, yurtdışı yasağı)

### 7. Tutuklama itirazı (CMK m. 268)

- **7 gün içinde** itiraz şart
- Üst sulh ceza hakimliği veya asliye ceza
- Müvekkil imzası şart değil — müdafi yazar

### 8. CMK ödeme cetveli (görev bitiminde)

```
CMK ÖDEME CETVELİ — [Baro] — [Tarih]
Avukat: [Av. ad-soyad — sicil no]
Atama no: [...]
Müvekkil: [TC kimlik]
Esas no: [...]
Aşama: [Soruşturma / Sorgu / Kovuşturma / Tutukluluk inceleme]
Tarih detay:
- Karakol görüşmesi: [tarih + süre]
- Savcılık ifadesi: [tarih + süre]
- Sulh ceza duruşması: [tarih]
Ücret (TBB CMK Tarifesi [yıl]):
- Soruşturma: [TL]
- Toplam: [TL]
```

Teslim: Baronun CMK servisine. Ödeme 30-60 g.

## Çıktı

```markdown
[ÜST BAŞLIK — CMK MÜDAFİ]

# CMK Görev Atama — [Atama no]

## ⚠️ İnceleyen notu
- Atama tipi: m. 150 zorunlu / m. 156 isteğe bağlı
- Suçlama: TCK m. [X]
- 48 saat sınırı: T+[N] — kalan [...]
- Müvekkil durumu: gözaltında / serbest

## Müvekkil bilgi
TC son 4: [....] — rumuz: [....]
Yer: [karakol / cezaevi]
İfade saati: GG.AA.YYYY HH:MM

## Ön değerlendirme
- Suçlama özet: [...]
- Delil durumu: [...] [savcının dosyası okundu mu?]
- Tutuklama olasılığı: [yüksek / orta / düşük]

## Strateji
- İfade: [ver / verme / kısmi] — gerekçe
- Tutuklama itirazı stratejisi (varsa)
- Aileye bilgi: [evet/hayır]

## Sonraki adımlar
- [Karakol görüşmesine N dakika içinde git]
- /criminal-defense:ifade-hazirlik (detay hazırlık)
- (Tutuklama olursa) /criminal-defense:matter-workspace new + CMK ödeme planla
```

## Hatalar

- **Susma hakkı hatırlatmama** → ifade kanıt değer kaybı + müvekkil zarar
- **48 saat sınırı kaçırma** → resen salıverme + müdafii hatası iddia
- **Tutukluluk itirazını 7 gün geçirme** → süre kayıp
- **Vekalet (Av. K. m. 35) yazılı talep almama** → işlem geçersiz
- **CMK ödeme cetvelini geç verme** → ödeme gecikir + yıllık beyana etki
