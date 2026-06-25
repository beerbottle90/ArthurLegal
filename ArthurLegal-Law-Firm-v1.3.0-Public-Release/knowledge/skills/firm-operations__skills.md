# firm-operations - Skill Referans Kitapçığı

> Alan: Büro operasyonları — müvekkil intake, çıkar çatışması, MASAK, KVKK, ücret, vekalet
> Toplam skill: 3
> Kullanım: /{plugin}:{skill-adı} komutunu yaz, aşağıdaki ilgili bölümü uygula.

## İçindekiler

- /firm-operations:cold-start-interview
- /firm-operations:conflict-check
- /firm-operations:new-client-intake

---

## /firm-operations:cold-start-interview

---
name: cold-start-interview
description: >
  Büro profilini ilk doldurma — TÜM diğer plugin'lerin okuyacağı ana profil.
  Büro kadrosu, ortaklar, organizasyon yapısı, baro kayıt durumu, müvekkil
  portföyü agregat (sektör + tip + coğrafya), pratik alanları, müvekkil intake
  politikası, vekalet ücreti modeli, mesleki sır pratikleri, operasyonel platformlar.
  Sonuç: knowledge/firm-profile.md doldurulur.
user-invocable: true
---

# Cold Start Interview — firm-operations (ANA PROFİL)

## Amaç

`knowledge/firm-profile.md` içindeki `[DOLDUR]` alanlarını doldur. ~20-30 dk (büronun tüm bilgisini topluyor).

⚠️ **Bu, paketteki TÜM diğer plugin'lerin okuyacağı ana profildir. Önce bu plugin'i çalıştırın, sonra diğer plugin'lerin cold-start'larını.**

## Adımlar

### 1. Büro temel bilgileri

- Büro adı, hukuki yapı (Avukatlık Ortaklığı / Hibrit / Bireysel)
- TBB Avukatlık Ortaklıkları Sicil no (varsa)
- Kuruluş yılı
- Vergi no, MERSİS (varsa Av. Ortaklığı tüzel kişiliği)

### 2. Ofis ve coğrafya

- Merkez ofis: il / ilçe / adres
- İrtibat ofisleri (varsa)
- Çalışma dilleri (Türkçe ana, İngilizce, başka?)

### 3. Kadro

- Yönetici Ortak (rumuz + baro/sicil + uzmanlık)
- Kıdemli Ortaklar (sayı + uzmanlık dağılımı)
- Bağlı avukat sayısı
- Stajyer sayısı
- Hukuk asistan + sekretarya sayısı
- **Toplam kadro** (0-30 bandı kontrol)

### 4. Baro kayıt

- İstanbul Barosu kaç ortak/avukat (asıl)
- Ankara Barosu kaç ortak/avukat (asıl/bağlı)
- Diğer barolar

### 5. Müvekkil portföyü (agregat — gerçek isim YOK)

- Aktif müvekkil sayısı
- Sürekli danışmanlık (retainer) sayısı
- Müvekkil tip dağılımı (bireysel / KOBİ / mid-cap / yabancı)
- Sektör dağılımı (inşaat / perakende / üretim / hizmet / teknoloji / bireysel)
- Coğrafi dağılım (İstanbul / Anadolu yakası / Ankara / başka / yurtdışı)

### 6. Pratik alanları

- Hangi plugin'ler aktif kullanılacak? (criminal-defense, firm-operations dahil)
- Aylık matter hacmi tahmini her plugin için

### 7. Müvekkil intake politikası

- Yeni müvekkil kabul akışında zorunlu adımlar
- Conflict check derinliği
- MASAK kimlik tespit alışkanlığı
- KVKK aydınlatma metni standardı var mı?
- Otomatik 🟠 incelemeli kabul tetikleyicileri

### 8. Vekalet ücreti modeli (büro seviye)

- Standart model: saatlik / götürü / hibrit / başarı bonusu?
- Saatlik oran (Yönetici/Kıdemli Ortak, Bağlı Avukat, Stajyer)
- Başarı bonusu sınırı (max %25 — Av. K. m. 164)
- Karşı yan vekalet ücreti politikası (vekile mi, paylaşılır mı)

### 9. Operasyonel platformlar

- Matter / belge yönetimi (iManage / SharePoint / Drive / dahili)
- Zaman takibi (Clio / TimeSolv / Excel)
- Fatura / muhasebe (dahili / dış muhasebeci)
- E-imza / KEP (büro + her ortak)
- CRM (varsa)
- Sanctions tarama (OpenSanctions API — API key alınmış mı?)

### 10. "Yakıcı" stres alanları

> "Bu büroda günlük operasyonu en çok zorlayan 1-3 şey nedir?"

## Çıktı

`knowledge/firm-profile.md` doldurulur.

```
✓ Büro profili tamamlandı.

Sonraki adımlar:
1. Diğer plugin'lerin cold-start-interview'larını çalıştırın:
   /litigation-legal:cold-start-interview
   /commercial-legal:cold-start-interview
   (her aktif plugin için)
2. İlk müvekkil için: /firm-operations:new-client-intake

Re-run: /firm-operations:cold-start-interview --redo
```

## Hatalar / kenar durumlar

- **Kullanıcı 30+ çalışan diyorsa** → "Bu paket 0-30 kadro için optimize edilmiş. 30+ için bazı pratikler (matter izolasyonu, ethical wall, large M&A) farklı yönetilir. Yine de devam edelim mi?"
- **Tüm soruları cevaplamak istemez** → Quick start (5 dk) vs. Full (20-30 dk) seçeneği sun
- **Müvekkil isim/şirket isteyebilir** → "ASLA gerçek müvekkil ismi yazmayın. Rumuz/agregat kullanın."

---

## /firm-operations:conflict-check

---
name: conflict-check
description: >
  Av. K. m. 38 + TBB Meslek Kuralları m. 35-36 çatışma taraması. Müvekkil + karşı
  yan + atanan avukat üç eksen tarama; eşzamanlı / eski müvekkil / grup içi /
  vekil değişimi / kamu görevi geçmişi senaryoları. Sonuç: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ.
user-invocable: true
---

# Conflict Check — Çıkar Çatışması Taraması

## Tetikleyici

- Yeni müvekkil intake (her yeni matter için zorunlu)
- Mevcut matter'da karşı yan kimliği netleştiğinde
- Mevcut müvekkilin başka bir işi
- Yeni ortak/avukat alındığında (retrospektif)
- Müvekkil yapısı değişti (M&A, pay devri)

## Tarama girdisi

### Müvekkil bilgisi
- Tip: Bireysel / Tüzel kişi
- TC kimlik / Vergi no / MERSİS no
- Ad-soyad / Ünvan
- (Tüzel) yan-grup şirketler — UBO + holding zinciri

### Karşı yan bilgisi
- Tip: Bireysel / Tüzel kişi
- TC kimlik / Vergi no / MERSİS no
- Ad-soyad / Ünvan
- (Tüzel) yan-grup şirketler

### Atanan avukat
- Sicil + baro
- Eski büro/iş geçmişi
- Kamu görevi (hakim/savcı/müfettiş) geçmişi
- Aile/yakın ilişki (büro içi)

## Tarama akışı

### 1. Müvekkilin geçmiş matter'ları taraması

Veritabanı sorgu:
- **Tam eşleşme** (TC/Vergi no)
- **Fonetik benzer ad** (Soundex TR varyasyon — Ş/S, İ/I, Ç/C, Ö/O, Ü/U, Ğ/G)
- **Tarih kapsamı:** son 10+ yıl (Av. K. m. 36 süresiz, ama 10 yıl pratik baseline)

### 2. Karşı yan taraması

- Karşı yanın geçmiş matter'ları (eski müvekkilimiz mi?)
- Karşı yanın grup ilişkileri (MERSİS sicili)

### 3. Atanan avukat taraması

- Atanan avukatın eski büro/iş geçmişi
- Hakim/savcı/müfettiş geçmişi (Av. K. m. 38/b)
- Aile/yakın ilişki — büro içi

### 4. Çatışma sınıflandırma

| Tip | Kural | Karar |
|---|---|---|
| Doğrudan eşzamanlı (m. 38/c) | Aynı işte iki taraf | ⛔ MUTLAK YASAK |
| Eski müvekkille çatışma (m. 35-36) | Bilgi alakası varsa | 🟠 İNCELE (yazılı rıza) |
| Grup içi (m. 38/a) | Aynı holding | 🟠 İNCELE (bilgi izolasyonu mümkün?) |
| Vekil değişimi (yeni gelen avukat) | Eski büro geçmişi | 🟠 İNCELE (ethical wall) |
| Kamu görevliyken iş (m. 38/b) | Hakim/savcı geçmişi | ⛔ MUTLAK YASAK |
| Avukatın kendi menfaati | Self-dealing | ⛔ MUTLAK YASAK |
| Hiçbir çakışma yok | — | ✓ TEMİZ |

## Çıktı

```markdown
[ÜST BAŞLIK — CONFLICT CHECK SONUCU — DAHİLİ]

# Conflict Check — [Müvekkil rumuz] vs. [Karşı yan rumuz]
Tarih: GG.AA.YYYY
Atanan ortak: [Yönetici Ortak veya öneri]

## ⚠️ İnceleyen notu
- SONUÇ: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ

## SONUÇ
[Gerekçeli değerlendirme]

## Sonraki adımlar
[✓ TEMİZ ise] → /firm-operations:new-client-intake devam
[🟠 ise] → Ortaklar Kurulu + yazılı rıza
[⛔ ise] → Müvekkile red + REJECTED.md kaydı
```

---

## /firm-operations:new-client-intake

---
name: new-client-intake
description: >
  Yeni müvekkil ön sohbet sonrası intake akışı: müvekkil bilgisi alma, talep
  özeti, matter tipi belirleme + plugin yönlendirmesi, aciliyet kontrolü, sonraki
  zorunlu adımlar (conflict-check, MASAK, sanctions, KVKK, fee, vekalet) tetikleme.
user-invocable: true
---

# New Client Intake — Yeni Müvekkil Ön Sohbet

## Tetikleyici

İlk temas (telefon / web / referans) sonrası, atanan ortak müvekkille ön sohbeti yaptıktan sonra.

## Adımlar

### 1. Müvekkil bilgisi

**Gerçek kişi:**
- Rumuz (kayıt için — gerçek isim KVKK uyarınca minimum)
- TC kimlik no (kimlik tespit için sonradan MASAK)
- Telefon + e-posta (mümkünse KEP)
- Meslek + işveren

**Tüzel kişi:**
- Ünvan (kısaltılmış rumuz)
- Vergi no + MERSİS no
- Faaliyet alanı (NACE)
- Yetkili temsilci
- KEP adresi

### 2. Talep özeti

- 1-2 cümle özet
- Karşı taraf var mı?
- Tahmini değer
- Tarih + süreler (aciliyet kontrolü)

### 3. Matter tipi → plugin yönlendirmesi

| Talep | Plugin |
|---|---|
| Müvekkil davacı/davalı (ticari/medeni) | `litigation-legal` |
| Müvekkil idari kararı iptal | `administrative-legal` |
| Müvekkil vergi tarhiyatı iptal | `tax-legal` |
| Müvekkil ceza şüphelisi/sanığı | `criminal-defense` |
| Müvekkil sözleşme yazımı/inceleme | `commercial-legal` |
| Müvekkilin GK/YK/M&A işlemi | `corporate-legal` |
| Müvekkil işveren/işçi iş hukuku | `employment-legal` |
| Müvekkilin marka/patent/tasarım | `ip-legal` |
| Veri koruma / KVKK | `privacy-legal` |
| Düzenleyici kurum / lisans | `regulatory-legal` |
| Enerji M&A / proje finansmanı | `energy-finance` |
| Aile/miras/boşanma | **KAPSAM DIŞI** — başka büroya yönlendir |

### 4. Aciliyet kontrolü

| Süre durumu | Etiket |
|---|---|
| Dava süresi < 7 gün | 🔴 ACİL |
| Dava süresi < 30 gün | 🟠 Yüksek |
| Sözleşme imza < 3 gün | 🟠 Yüksek |
| Tutuklu müvekkil (ceza) | 🔴 ACİL — 48 saat sınırı |
| Süre kritik değil | 🟢 Standart akış |

### 5. Sonraki zorunlu adımlar listesi

```
ZORUNLU SONRAKI ADIMLAR:
[ ] /firm-operations:conflict-check  ← İLK + KRİTİK
[ ] MASAK kimlik tespit
[ ] Sanctions tarama (tüzel/yabancı için)
[ ] KVKK aydınlatma metni
[ ] Ücret sözleşmesi
[ ] Vekalet
[ ] Matter klasörü açma
```

## Çıktı

```markdown
[ÜST BAŞLIK — INTAKE NOTU — DAHİLİ]

# Müvekkil Intake — [Rumuz] — [Tarih]

## ⚠️ İnceleyen notu
- Aciliyet: 🔴/🟠/🟢
- Önerilen plugin: [...]
- Sonraki zorunlu adımlar: 7 adım

## Müvekkil
- Tip: Bireysel / Tüzel kişi
- Rumuz: [...]

## Talep özeti
[1-2 cümle]

## Matter tipi
[Plugin]: [...] — gerekçe

## Aciliyet
🔴/🟠/🟢 — [neden]

## Sonraki ZORUNLU adımlar
1. /firm-operations:conflict-check (İLK)
2. MASAK kimlik tespit
3. Sanctions tarama
4. KVKK aydınlatma
5. Ücret sözleşmesi
6. Vekalet
7. Matter klasörü açma
```

## Hatalar

- **Müvekkilin gerçek ismini intake notuna yazma** — rumuz kullan
- **Conflict check tetiklenmeden iş başlatma** — Av. K. m. 38 ihlal riski
- **KAPSAM DIŞI matter'ı kabul etme** — yetersiz hizmet riski
