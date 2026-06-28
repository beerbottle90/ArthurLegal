# idari-kalem — Skill Referans Kitapçığı

> Dal: İdari yargı (idare mahkemesi) · Rol: **Kalem (yazı işleri)** · Usul: İYUK 2577 + Tebligat K. 7201
> Toplam skill: 3
> Kullanım: `/idari-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar belge iskeleti + kontrol listesidir; hâkim havalesi/onayı şarttır. Her çıktı **TASLAK**.

## İçindekiler

- /idari-kalem:dosya-tekemmul — İYUK m. 16-20 dilekçe/savunma teatisi & dosyanın tekemmülü
- /idari-kalem:idari-tebligat — İYUK + 7201 tebligat ve süre takibi
- /idari-kalem:karar-uygulama-takip — İYUK m. 28 kesinleşme + idareye gönderme + 30 gün uygulama

---

## /idari-kalem:dosya-tekemmul

---
name: dosya-tekemmul
description: >
  İYUK m. 16-20 dilekçe ve savunmaların teatisi sürecini yönetir: tebliğ, savunma
  süreleri (30 gün + ek süre), ara karar, dosyanın tekemmülü ve heyete sunum kontrolü.
user-invocable: true
---

# Dosyanın Tekemmülü — İYUK m. 16-20

## Amaç

Dilekçeler aşamasının (m. 16) usulüne uygun yürümesi; dosyanın karara hazır hâle gelmesi.

## Süreç & süreler

1. **Dava dilekçesi tebliği** → davalı idareye.
2. **Savunma süresi:** **30 gün** (m. 16/1); haklı sebeple bir defaya mahsus ek süre (m. 16/5 — uzatılabilir, MCP teyidi).
3. **Cevaba cevap / ikinci savunma** — m. 16/2-3 sınırları.
4. **Ara karar (m. 20):** re'sen araştırma kapsamında eksik bilgi/belge istemi; idareye süre.
5. **Tekemmül:** süreler dolup dosya tamamlanınca heyete/hâkime sunum.
6. **Dosya üzerinden inceleme** kural; duruşma talebe bağlı (m. 17).

## Çıktı

Tekemmül kontrol listesi + süre takip tablosu (`[DOLDUR]` tarihli) + bekleyen ara karar listesi. TASLAK + "hâkim havalesi şart".

---

## /idari-kalem:idari-tebligat

---
name: idari-tebligat
description: >
  İdari yargıda tebligat usulü ve süre başlangıcı: idareye/taraflara tebliğ, e-tebligat,
  kanun yolu (istinaf/temyiz) süre başlangıcının doğru hesaplanması.
user-invocable: true
---

# İdari Tebligat & Süre

## Amaç

Doğru tebligat + kanun yolu sürelerinin doğru başlaması (yanlış tebligat = süre işlememesi 🔴).

## Notlar

1. **Muhatap:** taraflar + vekilleri; idare için ilgili makam.
2. **e-Tebligat:** avukat + kamu kurumları zorunlu → `kep-etebligat-rehberi.md`.
3. **Kanun yolu süreleri (İYUK):** istinaf **30 gün** (m. 45), temyiz **30 gün** (m. 46); ÇED ivedi rejimde farklı (m. 20/A — doğrudan Danıştay, 15 gün). ⚠️ Süreyi mevzuat teyidiyle doğrula.
4. **Tebliğ tarihi** = süre başlangıcı; karar düzeltme kaldırıldı (istinaf sistemi).

## Çıktı

Tebligat planı + kanun yolu süre tablosu. TASLAK ibareli. Detay: `iyuk-rehberi.md`.

---

## /idari-kalem:karar-uygulama-takip

---
name: karar-uygulama-takip
description: >
  İYUK m. 28 kararların uygulanması: kesinleşme, idareye tebliğ, 30 gün içinde
  uygulama yükümlülüğü ve takibi; uygulanmama hâlinde başvuru/tazminat notu.
user-invocable: true
---

# Kararın Uygulanması — İYUK m. 28

## Amaç

İdari yargı kararının kesinleşmesi sonrası idareye gönderme + uygulama süresinin takibi (kalem işlemi).

## Adımlar

1. **Kesinleşme:** kanun yolu süreleri/sonuçları → kesinleşme şerhi.
2. **İdareye tebliğ:** karar, gereği için ilgili idareye tebliğ.
3. **Uygulama süresi (m. 28/1):** idare, kararın gereğini **gecikmeksizin ve en geç 30 gün** içinde yerine getirmek zorundadır.
4. **Takip:** sürenin işleyişi izlenir; uygulanmama hâlinde ilgilinin başvuru/tazminat hakkı (m. 28/3-4) + sorumluluk notu.

## Çıktı

Kesinleşme + gönderme + 30 gün uygulama takip tablosu (`[DOLDUR]`). TASLAK + "hâkim havalesi şart". Detay: `iyuk-rehberi.md`.

---

> 🚧 v1.0.0 — `idari-kalem` 3 kalem skill'i. Kalıp: `hukuk-hakim__skills.md`.
