---
name: marka-clearance
description: >
  Yeni marka kullanım/tescil öncesi clearance: TÜRKPATENT sınıf bazlı arama
  (Nice), fonetik + görsel + ticaret unvanı + EU + Madrid + alan adı + sosyal
  medya + telif kontrolü. 6769 SMK m. 5 (mutlak red) + m. 6 (nispi red)
  değerlendirme. Risk skalası 🔴/🟠/🟡/🟢. Tanınmış marka çakışması.
user-invocable: true
---

# Marka Clearance — Ön Araştırma

## Bilgi al

- Marka adı / işareti (figüratif varsa açıklama)
- Müvekkil tüzel kişi (üreten / hizmet veren)
- Hedef sınıf(lar) (Nice — kabaca: kategori-mal-hizmet)
- Hedef coğrafya (TR / EU / Madrid uluslararası / belirli ülke)
- Kullanım niyeti (tescil + kullanım / sadece kullanım / yenileme)
- Tanınmış marka iddiası var mı?

## Adımlar

### 1. **TÜRKPATENT marka arama** (manuel veya WebFetch)

URL pattern: `https://www.turkpatent.gov.tr/arama` → marka adı + sınıf

**Arama tipleri:**
- **Tam isim eşleşme**
- **Fonetik benzer** — Türkçe karakter varyasyon (Ş/S, İ/I, Ç/C, Ö/O, Ü/U, Ğ/G)
- **Görsel benzer** — figüratif markalar (logo)
- **Kelime + sınıf** — aynı sınıfta benzer kelime
- **Tanınmış marka listesi** — TÜRKPATENT yayınladığı tanınmış markalar

### 2. **Ticaret unvanı arama** (MERSİS + TTSG)

URL: `https://www.mersis.gov.tr/`

- Müvekkilin markası bir başka şirketin ticaret unvanına çakışıyor mu?
- **6769 SMK m. 6/6** — ticaret unvanı önceki hak sahibinden korunur

### 3. **EUIPO arama** (varsa AB pazarı hedefli)

URL: `https://www.tmdn.org/tmview/`

- EUTM (European Union Trade Mark) çakışması
- Madrid sistem üzerinden AB tesciller

### 4. **Madrid Protokolü sistem arama**

URL: `https://www3.wipo.int/branddb/en/`

- Uluslararası tescil + Madrid IR no
- Türkiye'ye uzantı kontrolü

### 5. **Alan adı (domain) kontrolü**

- WHOIS sorgu (.com / .com.tr / .net / .org)
- Sosyal medya handle (Instagram / Twitter / LinkedIn / TikTok)
- TR-NIC (`.tr` uzantısı için)

### 6. **Telif hak çakışması**

- Popüler eser / karakter / figür adı kullanılmış mı?
- 5846 FSEK m. 2 eser kapsamı

### 7. **6769 SMK değerlendirmesi**

**M. 5 — Mutlak red sebepleri (TÜRKPATENT resen reddedebilir):**
- Ayırt edicilik yokluğu (jenerik isim, tanımlayıcı)
- Kamu düzeni / genel ahlaka aykırı
- Yanıltıcı (mal/hizmet hakkında)
- Resmi armayı içeren (devlet armaları)
- Tanınmış marka aynısı (m. 5/1-ç)

**M. 6 — Nispi red sebepleri (itiraz üzerine):**
- Önceki marka tescili (aynı / benzer + aynı / benzer sınıf)
- Önceki tescilsiz kullanım (ticari etki kazanmış)
- Ticaret unvanı önceki hak
- Telif önceki hak
- **Tanınmış marka** (Paris Sözleşmesi m. 6bis + 6769 m. 6/4)

### 8. Risk skalası

| Sonuç | Skala |
|---|---|
| Hiçbir çakışma yok, ayırt edici | 🟢 TEMİZ |
| Uzak benzerlik (farklı sınıf veya hafif fonetik) | 🟡 DİKKAT |
| Yakın benzerlik (aynı sınıf + benzer ad) — itiraz riski | 🟠 ŞÜPHELİ |
| Aynısı / tanınmış marka çakışması | 🔴 ÇAKIŞMA — yasak |

## Çıktı

```markdown
[ÜST BAŞLIK]

# Marka Clearance Raporu — "[marka adı]"
Müvekkil: [rumuz]
Sınıf(lar): [Nice X, Y]
Hedef coğrafya: [TR / EU / Madrid (ülkeler) / ABD / ortadoğu vb.]

## ⚠️ İnceleyen notu
- Aranan kaynaklar: TÜRKPATENT [✓] / MERSİS [✓] / EUIPO [✓/✗] / Madrid [✓/✗] / WHOIS [✓]
- Bulgu sayısı: [N benzer marka / M ticaret unvanı / K domain]
- Genel risk: 🟢 TEMİZ / 🟡 DİKKAT / 🟠 ŞÜPHELİ / 🔴 ÇAKIŞMA

## Bulgular

### TÜRKPATENT
| Marka | Sahibi | Sınıf | Risk |
|---|---|---|---|
| [...] | [...] | [...] | 🟡 |

### EUIPO (varsa)
| EUTM | Sahibi | Sınıf | Risk |
|---|---|---|---|

### Madrid (varsa)
| IR no | Sahibi | TR uzantı? | Risk |
|---|---|---|---|

### Ticaret unvanı
[MERSİS bulgular]

### Tanınmış marka
[TÜRKPATENT tanınmış listesinde tarama sonucu]

### Alan adı + sosyal medya
| Platform | Durum |
|---|---|
| .com | Müsait/dolu |
| .com.tr | ... |
| Instagram @[handle] | ... |

## SMK m. 5 değerlendirmesi (mutlak red)
| Sebep | Durum |
|---|---|
| Ayırt edicilik | ✓/✗ |
| Tanımlayıcılık | ✓/✗ |
| Kamu düzeni | ✓/✗ |

## SMK m. 6 değerlendirmesi (nispi red)
| Sebep | Risk |
|---|---|
| Önceki marka | [varsa: marka adı + risk] |
| Önceki ticaret unvanı | [...] |
| Telif | [...] |
| Tanınmış marka | [...] |

## Risk değerlendirmesi
**Genel:** 🟢/🟡/🟠/🔴 — [gerekçe]

## Önerim
- 🟢 TEMİZ → Tescil başvurusu önerilir → /ip-advisory:marka-tescil
- 🟡 DİKKAT → Müzakere veya alternatif isim
- 🟠 ŞÜPHELİ → Müvekkille konuş, yazılı feragat al
- 🔴 ÇAKIŞMA → Alternatif isim önerisi (3-5 alternatif)

## Sonraki adımlar
- /ip-advisory:marka-tescil (✓ TEMİZ ise)
- Alternatif isim listesi (🟠/🔴 ise)
- Müvekkile detaylı brief
```

## Hatalar

- **Sadece tam isim eşleşmesi** — fonetik + görsel benzerliği atlama
- **Nice sınıflandırması yıllık güncellenir** — eski sınıf numarasıyla arama
- **Ticaret unvanı + telif kontrolünü atlama** — sadece marka veri tabanı
- **Tanınmış marka listesi taranmama** — TÜRKPATENT tanınmış markalar Paris Sözleşmesi m. 6bis + 6769 m. 6/4 koruması
- **Müvekkilin "ben kullanırım" baskısı altında 🟠/🔴 sonucu yumuşatma** → yazılı feragat olmadan devam etme
