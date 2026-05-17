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

**Bulgular:**
- Aktif matter (devam ediyor)
- Tasfiye matter (kapanmış)
- Reddedilen matter (kabul edilmemiş — REJECTED.md kaydı)

### 2. Karşı yan taraması

- Karşı yanın geçmiş matter'ları (eski müvekkilimiz mi?)
- Karşı yanın grup ilişkileri (MERSİS sicili)
- Karşı yanın yan-kurumsal yapı

### 3. Atanan avukat taraması

- Atanan avukatın eski büro/iş geçmişi (önceden gördüğü matter'lar)
- Hakim/savcı/müfettiş geçmişi (Av. K. m. 38/b)
- Aile/yakın ilişki — büro içi (örn. eşi karşı yanın avukatı mı?)

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

## 🟠 İncele durumunda çözüm yolu

1. **Eski müvekkilden yazılı rıza** iste (mümkünse — bazen yeni müvekkili açıklamak zor)
2. **Ethical wall** kur (büyük büroda; küçük büroda zor)
3. **Ortaklar Kurulu** kararı
4. **Reddet** (genelde en güvenli)

## Çıktı

```markdown
[ÜST BAŞLIK — CONFLICT CHECK SONUCU — DAHİLİ]

# Conflict Check — [Müvekkil rumuz] vs. [Karşı yan rumuz]
Tarih: GG.AA.YYYY
Atanan ortak: [Yönetici Ortak veya öneri]

## ⚠️ İnceleyen notu
- Veritabanı tarama tarihi: GG.AA.YYYY HH:MM
- Tarama derinliği: son 10+ yıl
- Bulgu sayısı: [N matter karşılaştırıldı]
- **SONUÇ: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ**

## Müvekkil tarama
- Aktif matter: [N]
- Tasfiye matter: [N]
- Reddedilen matter: [N]
- **Eşleşme sayısı: [N]**

### Eşleşmeler (varsa)
| Matter ID | Tarih | Konu | İlişki | Risk |
|---|---|---|---|---|
| [...] | [...] | [...] | Eski müvekkil / yan-grup / vd. | 🟠/⛔ |

## Karşı yan tarama
- Eşleşme sayısı: [N]

### Eşleşmeler (varsa)
[Tablo]

## Atanan avukat tarama
- Eski büro geçmişi: [Varsa kayıt]
- Kamu görevi: [Yok/Varsa detay]
- Aile/yakın ilişki: [Yok/Varsa]

## Çatışma değerlendirmesi
[Detaylı analiz — Av. K. m. 38 hangi bent, TBB MK m. 35/36 nasıl uygulanır]

## SONUÇ
⛔ RET / 🟠 İNCELE / ✓ TEMİZ

### Karar gerekçesi
[Açıklama]

### (🟠 ise) Çözüm yolu
1. Eski müvekkilden yazılı rıza
2. Ethical wall
3. Ortaklar Kurulu kararı
4. Reddet

### (⛔ ise) Reddetme kayıt
- Pre-matter/.../REJECTED.md oluşturuldu
- Müvekkile uygun (kibar) red mektubu önerildi

## Sonraki adımlar
[✓ TEMİZ ise] → /firm-operations:masak-kontrol
[🟠 ise] → Ortaklar Kurulu toplantısı + eski müvekkil yazılı rıza
[⛔ ise] → Müvekkile red mektubu + REJECTED.md kaydı + (önerirsek) başka avukat
```

## Hatalar

- **Sadece müvekkil ad ile tarama** (TC/Vergi no atlanır) → grup eşleşmesi kaçar
- **10 yıl geriye gitmeme** — Av. K. m. 36 süresiz, kayıtların tümü taranmalı
- **MERSİS yan-grup taramayı atlamak** — grup içi çatışma sezilmez
- **Yazılı rıza olmadan ethical wall** — TBB MK m. 36 ihlali (rıza olmadan eski müvekkil bilgisi kullanılamaz)
- **Yeni avukat geldiğinde retrospektif taramayı atlamak** — eski büro matter'ları yeni büroda devam edebilir
- **🟠 sonucu sessizce 🟢'a düşürmek** — Av. K. m. 38 ihlal riski + disiplin tetikleyici
