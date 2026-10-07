# criminal-defense - Skill Referans Kitapçığı

> Alan: Ceza müdafaa — CMK zorunlu müdafi, özel müvekkil, mağdur müdahil
> Toplam skill: 2
> Kullanım: /{plugin}:{skill-adı} komutunu yaz, aşağıdaki ilgili bölümü uygula.

## İçindekiler

- /criminal-defense:cold-start-interview
- /criminal-defense:cmk-gorev-atama

---

## /criminal-defense:cold-start-interview

---
name: cold-start-interview
description: >
  Plugin'i ilk kullanım için profilini doldurma. Ceza müdafaa pratik modeli
  (CMK görevli + özel müvekkil dengesi), uzmanlık alanları (genel / ekonomik /
  beyaz yaka / basın), CMK gönüllü avukat listesi, müdahil vekilliği deneyimi.
  Sonuç: knowledge/firm-profile.md güncellenir.
user-invocable: true
---

# Cold Start Interview — criminal-defense

## Amaç

`knowledge/firm-profile.md` içindeki `[DOLDUR]` alanlarını doldur. ~10 dk.

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

- Tutukluluk duruşmasına genelde kim katılır (Yönetici Ortak / bağlı avukat)?
- İki haftalık itiraz süresi (CMK m. 268) takvim takibi yöntemi?
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

Sonraki adım: /criminal-defense:cmk-gorev-atama
Re-run: /criminal-defense:cold-start-interview --redo
```

---

## /criminal-defense:cmk-gorev-atama

---
name: cmk-gorev-atama
description: >
  Baro CMK servisinden gelen zorunlu müdafii atama yönetimi. Gözaltı süresi (24 saat; toplu suçta en çok 4 gün)
  takibi (CMK m. 91), karakol/savcılık ifade öncesi hazırlık checklist, susma
  hakkı hatırlatma (CMK m. 147), tutukluluk değerlendirme + itiraz prosedürü
  (m. 268/1 — iki hafta, öğrenmeden), CMK ödeme cetveli oluşturma.
user-invocable: true
---

# CMK Görev Atama Yönetimi

## Tetikleyici

Baro CMK servisinden telefon/SMS atama mesajı geldiğinde.

⚠️ **2 saat içinde teyit + 6 saat içinde yere ulaşma** — bu süreler kritik.

## Adımlar

### 1. Atama bilgisi al

- Atama no
- Müvekkil: TC kimlik son 4 rakam (takma ad)
- Suçlama (TCK m. X)
- Yer: karakol / cezaevi / mahkeme
- Zaman: ifade saati / duruşma saati
- Atama tipi: m. 150 zorunlu / m. 156 isteğe bağlı / talimat müdafiliği

### 2. **Gözaltı süresi hesabı (CMK m. 91 — kural 24 saat; toplu suçta en çok 4 gün)**

| T | Olay | Süre |
|---|---|---|
| T+0 | Yakalama | — |
| T+24 | Gözaltı süresi dolar (m. 91/1; zorunlu yol süresi hariç, o da en çok 12 saat) | Toplu suçlarda C. savcısı her defasında 1 günü geçmemek üzere 3 gün uzatabilir (m. 91/3) → en çok 4 gün |
| Süre sonu | Bırakılmayan şüpheli sulh ceza hâkimi önüne çıkarılıp sorguya çekilir (m. 91/7; suçüstü kolluk gözaltısında en geç 48 saat / toplu suçta 4 gün, m. 91/4) | Tutuklama veya salıverme |

⚠️ **Gözaltı süresi (kural 24 saat; toplu suçta en çok 4 gün) dolunca şüpheli ya serbest bırakılır ya da sulh ceza hâkimi önüne çıkarılır (m. 91/7); gözaltına/uzatma emrine karşı sulh ceza hâkimine başvuru: m. 91/5.**

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
- [ ] **Baro görevlendirme yazısı** (CMK m. 156; müdafi ile görüşme vekâletname aranmaksızın yapılır — CMK m. 154/1)

### 5. İfade tutanağı kontrol

- Müvekkilin söylediği noktasal mı?
- Yönlendirici soru var mı?
- "Susma hakkımı kullanıyorum" ifadesi kayıt mı?
- Müvekkil + müdafi imzası tamam mı?

⚠️ **Müdafi hazır bulunmaksızın kollukça alınan ifade**, hâkim veya mahkeme huzurunda şüpheli/sanık tarafından doğrulanmadıkça **hükme esas alınamaz** (CMK m. 148/4).

### 6. Sulh ceza hakimliği duruşması (tutuklama)

Hakim **CMK m. 100** şartlarını değerlendirir:
1. Kuvvetli suç şüphesi
2. Kaçma şüphesi / delil karartma / tanık-mağdur üzerinde baskı (m. 100/2) veya katalog suç (m. 100/3)
3. Adli kontrol yetersizliği

**Müdafi savunma noktaları:**
- Delilin yetersizliği (kuvvetli şüphe yok)
- Yerleşik adres + aile + iş (kaçma şüphesi yok)
- Adli kontrol yeterli (ev hapsi, imza, yurtdışı yasağı)

### 7. Tutuklama itirazı (CMK m. 268)

- **İki hafta içinde** itiraz şart (m. 268/1 — öğrenmeden; 7499 s.K. öncesi 7 gündü)
- İtiraz kararı veren sulh ceza hâkimliğine verilir; tutuklama ve adli kontrol kararında inceleme mercii asliye ceza mahkemesi hâkimi (m. 268/3-b)
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
TC son 4: [....] — takma ad: [....]
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
- (Tutuklama olursa) /criminal-defense:matter-workspace new + CMK ödeme planla
```

## Hatalar

- **Susma hakkı hatırlatmama** → ifade kanıt değer kaybı + müvekkil zarar
- **48 saat sınırı kaçırma** → resen salıverme + müdafii hatası iddia
- **Tutukluluk itirazını iki haftalık süreden sonra yapma** → süre kaybı
- **Baro görevlendirme yazısını (CMK m. 156) dosyaya koymama** → görev dayanağı belgelenmez (görüşme için vekâletname aranmaz, CMK m. 154/1)
- **CMK ödeme cetvelini geç verme** → ödeme gecikir + yıllık beyana etki
