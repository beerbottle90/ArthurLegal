# vergi-kalem — Skill Referans Kitapçığı

> Dal: Vergi yargısı (vergi mahkemesi) · Rol: **Kalem (yazı işleri)** · Usul: İYUK 2577 + VUK 213 + Tebligat K. 7201
> Toplam skill: 3
> Kullanım: `/vergi-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar belge iskeleti + kontrol listesidir; hâkim havalesi/onayı şarttır. Her çıktı **TASLAK**.

## İçindekiler

- /vergi-kalem:vergi-tebligat — VUK m. 93-109 tebliğ + İYUK kanun yolu süresi
- /vergi-kalem:vergi-sure-takip — dava açma / yürütme / tahsilat süre takibi
- /vergi-kalem:karar-uygulama-iade — kesinleşme + vergi dairesine gönderme + terkin/iade takibi

---

## /vergi-kalem:vergi-tebligat

---
name: vergi-tebligat
description: >
  Vergi yargısında ve idari aşamada tebliğ: VUK m. 93-109 özel tebliğ hükümleri ile
  İYUK/7201 mahkeme tebligatının ayrımı ve süre başlangıcı.
user-invocable: true
---

# Vergi Tebligat — VUK m. 93-109 + İYUK

## Amaç

İdari aşama (VUK) ile yargısal aşama (İYUK/7201) tebliğ rejimlerini ayır; süre başlangıcını doğru tespit et.

## Notlar

1. **İdari aşama (VUK m. 93 vd.):** ihbarname/ödeme emri tebliği — posta, memur, ilan (m. 103-106), e-tebligat (VUK m. 107/A). Bu tebliğ **dava açma süresini** (30 gün) başlatır.
2. **Yargısal aşama:** mahkeme tebligatı İYUK + 7201; avukat/kurum e-tebligat.
3. **İlanen tebliğ (m. 103-106):** şartları dar; usulsüz ilan 🔴 süre işlememesi.
4. **Kanun yolu süresi:** istinaf/temyiz 30 gün (İYUK m. 45-46). ⚠️ Süreleri mevzuat teyidiyle doğrula.

## Çıktı

Tebliğ türü ayrımı (idari/yargısal) + süre başlangıcı tablosu. TASLAK ibareli. Detay: `vuk-rehberi.md`, `kep-etebligat-rehberi.md`.

---

## /vergi-kalem:vergi-sure-takip

---
name: vergi-sure-takip
description: >
  Vergi dosyasında kritik süreleri tek tabloda takip eder: 30 gün dava açma, yürütmenin
  durması/teminat, tahsilat (6183), istinaf/temyiz süreleri.
user-invocable: true
---

# Vergi Süre Takibi

## Amaç

Vergi dosyasının tüm süre kalemlerini görünür kıl; hak kaybı/zamanaşımı riskini önle.

## Süre haritası

1. **Dava açma:** ihbarname/ödeme emri tebliğinden **30 gün** (İYUK m. 7).
2. **Yürütme:** vergi/ceza ihbarnamesine karşı dava açılması tahsilatı **kendiliğinden durdurur** (İYUK m. 27/4); ödeme emrine (6183) karşı dava yürütmeyi durdurmaz — teminat/YD ayrımı.
3. **Tahsilat (6183 AATUHK):** ödeme emri, haciz, tecil-taksit süreçleri (idari, mahkeme dışı ama dosyayla ilişkili).
4. **Kanun yolu:** istinaf 30 gün (m. 45), temyiz 30 gün (m. 46).
5. **Zamanaşımı:** tarh (VUK m. 114 — 5 yıl), tahsil (6183 m. 102 — 5 yıl).

## Çıktı

Süre takip tablosu (kalem × tarih × kalan gün, `[DOLDUR]`) + risk işaretleri (🔴 yaklaşan/aşılmış). TASLAK ibareli.

---

## /vergi-kalem:karar-uygulama-iade

---
name: karar-uygulama-iade
description: >
  Vergi mahkemesi kararının kesinleşmesi sonrası vergi dairesine gönderme,
  terkin/düzeltme ve iade işlemlerinin takibi (kalem işlemi).
user-invocable: true
---

# Vergi Kararının Uygulanması & İade

## Amaç

Vergi yargısı kararının (iptal/kısmen iptal) kesinleşmesi sonrası uygulanması ve mükellef lehine terkin/iade takibi.

## Adımlar

1. **Kesinleşme** + şerh; karar vergi dairesine tebliğ (İYUK m. 28).
2. **Uygulama (m. 28/1):** idare 30 gün içinde kararın gereğini yerine getirir (terkin/düzeltme).
3. **İade:** iptal edilen vergi/cezanın iadesi; iade faizi (varsa) — oran/usul mevzuat teyidi.
4. **Kısmen iptal:** terkin edilen ve onanan kısımların ayrı işlenmesi.
5. **Takip:** 30 gün uygulama + iade süreçleri izlenir.

## Çıktı

Kesinleşme + gönderme + terkin/iade takip tablosu. TASLAK + "hâkim havalesi şart". Detay: `vergi-yargisi-rehberi.md`, `vuk-rehberi.md`.

---

> 🚧 v1.0.0 — `vergi-kalem` 3 kalem skill'i. Kalıp: `hukuk-hakim__skills.md`.
