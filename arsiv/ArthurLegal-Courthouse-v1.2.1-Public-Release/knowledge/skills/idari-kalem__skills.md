# idari-kalem — Skill Referans Kitapçığı

> Dal: İdari yargı (idare mahkemesi) · Rol: **Kalem (yazı işleri)** · Usul: İYUK 2577 + Tebligat K. 7201
> Toplam skill: 4
> Kullanım: `/idari-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar belge iskeleti + kontrol listesidir; hâkim havalesi/onayı şarttır. Her çıktı **TASLAK**.

## İçindekiler

- /idari-kalem:dosya-tekemmul — İYUK m. 16-20 dilekçe/savunma teatisi & dosyanın tekemmülü
- /idari-kalem:idari-tebligat — İYUK + 7201 tebligat ve süre takibi
- /idari-kalem:karar-uygulama-takip — İYUK m. 28 kesinleşme + idareye gönderme + 30 gün uygulama
- /idari-kalem:kanun-yolu-gonderme — İYUK m. 45, 46, 48 istinaf ve temyiz dilekçesinin alınması, harç ve eksiklik, tebliğ ve cevap, dosyanın gönderilmesi

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
2. **Savunma süresi:** **30 gün** (m. 16/3); haklı sebeplerin bulunması hâlinde taraflardan birinin isteği üzerine mahkeme kararıyla, otuz günü geçmemek ve bir defaya mahsus olmak üzere uzatılabilir; süre geçtikten sonra yapılan uzatma talebi kabul edilmez (m. 16/3). İşlem dosyasının aslı veya onaylı örneği savunmayla birlikte gönderilir (m. 16/5).
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
3. **Kanun yolu süreleri (İYUK):** istinaf **30 gün** (m. 45), temyiz **30 gün** (m. 46); ivedi yargılamada (m. 20/A; ÇED dahil) farklı: istinaf yok (m. 45/8), nihai karara tebliğden itibaren 15 gün içinde temyiz (m. 20/A/2-g). ⚠️ Süreyi mevzuat teyidiyle doğrula.
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

## /idari-kalem:kanun-yolu-gonderme

---
name: kanun-yolu-gonderme
description: >
  İdare mahkemesi kaleminin istinaf ve temyiz dilekçelerini alıp dosyayı bölge idare
  mahkemesine veya Danıştay'a göndermeden önceki işlemlerini sıralar: yolun ve sürenin
  tespiti (genel, ivedi yargılama, merkezî sınav, YD itirazı), dilekçe ve harç
  eksikliği, karşı tarafa tebliğ ve cevap, cevapla başvuru, YD istemli dilekçe, dizi
  listesi.
user-invocable: true
---

# Kanun Yolu Başvurusunun Alınması ve Dosyanın Gönderilmesi (İdari)

## Konum hatırlatması

Kesinlik, süre ve eksiklik nedeniyle verilecek ret veya "başvurulmamış sayılma" kararları kalemin değil yetkili merciin işidir; kalem hesaplar ve hâkime sunar. İstinaf temyizin şekil ve usullerine tabi olduğundan (İYUK m. 45/2) m. 48'deki işlemler istinafta kıyasen uygulanır; mahkemenizde hangi işlemin ilk derece mahkemesince, hangisinin bölge idare mahkemesince yapıldığı hâkimden teyit edilir. Asistan UYAP'ta işlem yapmaz. **Başvurunun reddi, süre ve kesinlik yönünden her karar için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

İstinaf ve temyiz dilekçelerinin alınmasından dosyanın bölge idare mahkemesine veya Danıştay'a gönderilmesine kadar kalem işlemlerini sıralamak; yol, süre, harç ve eksiklik konularını hâkime sunulacak biçimde ayırmak.

## Girdi

- Kararın türü (nihai karar veya yürütmenin durdurulması kararı), dava konusu ve miktarı [DOLDUR]
- Kararın taraflara tebliğ tarihleri [DOLDUR]
- İstinaf veya temyiz dilekçesinin veriliş tarihi ve yeri; yatırılan harç ve giderler [DOLDUR]
- Davanın ivedi yargılama veya merkezî sınav usulüne tabi olup olmadığı [DOLDUR]
- Dosya bilgisi kullanıcıdan gelir; asistan UYAP'a bağlanmaz, kayıt eklemez.

## Yol ve süre tespiti

| Dava / karar | Yol | Süre | Dayanak |
|---|---|---|---|
| Genel | İstinaf (bölge idare mahkemesi) | Kararın tebliğinden itibaren 30 gün | İYUK m. 45/1 |
| Bölge idare mahkemesi kararı (temyize açıksa) | Temyiz (Danıştay) | Tebliğden itibaren 30 gün | m. 46 |
| İvedi yargılama davası | İstinaf yok; temyiz | Tebliğden itibaren 15 gün | m. 45/8, 20/A/2-g |
| Merkezî ve ortak sınav davası | Temyiz | Tebliğden itibaren 5 gün | m. 20/B/1-f |
| Yürütmenin durdurulması kararı | İtiraz (bir defaya mahsus) | Tebliği izleyen günden itibaren 7 gün | m. 27/7 |

- Parasal kesinlik: m. 45/1'deki tutar Ek m. 1 ile her yıl güncellenir; davanın açıldığı tarihteki sınır esas alınır (Ek m. 1/2). Güncel tutar çekilmediyse UYARI satırı.
- Süre hesabı: süreler tebliği izleyen günden işler; son gün tatile rastlarsa izleyen çalışma gününün bitimine uzar; süre sonu çalışmaya ara verme zamanına rastlarsa ara vermenin sona erdiği günü izleyen tarihten itibaren yedi gün uzamış sayılır (m. 8).

## Kontrol listesi

- [ ] Dilekçe tarihi, kaydı ve verildiği yer (m. 48/3'te sayılan merciler)
- [ ] Dilekçe m. 3 esaslarına uygun mu; değilse on beş gün içinde tamamlatma bildirimi (m. 48/2 — istinafta kıyasen)
- [ ] Harç ve giderler; eksikse yedi günlük süre içinde tamamlanması, aksi hâlde başvurudan vazgeçilmiş sayılacağının yazılı bildirimi (m. 48/6); tamamlanmazsa verilecek karar için hâkime sunum
- [ ] Süre veya kesinlik yönünden tereddüt → hâkime sunum (m. 48/6; m. 45/2 ve 48/7'ye ilişkin Anayasa Mahkemesi iptal notu, metnin dipnotunda: 20.07.2022, E.2022/48, K.2022/93)
- [ ] Karşı tarafa tebliğ; tebliğ tarihini izleyen otuz gün içinde cevap (m. 48/3)
- [ ] Cevapla başvuru: cevap veren, kararı süresinde kanun yoluna götürmemiş olsa bile cevap dilekçesinde başvurabilir (m. 48/3) → bu başvurunun da karşı tarafa tebliği
- [ ] YD istemli dilekçe: karşı tarafa tebliğ edilmeden, YD istemi hakkında karar verilmek üzere gönderilir (m. 48/5 — istinafta kıyasen, hâkim teyidiyle)
- [ ] Dosyanın dizi listesine bağlı olarak gönderilmesi (m. 48/4); istinafta dilekçedeki hitap ve istekle bağlı kalınmaksızın bölge idare mahkemesine (m. 45/2)
- [ ] Çalışmaya ara verme (20 Temmuz – 31 Ağustos) ve nöbetçi mahkemenin gördüğü işler (m. 61-62)

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Kanun yolu formu:** | Başvuran | Yol | Karar tebliğ tarihi | Başvuru tarihi | Son gün (en erken) | Harç | Karşı tarafa tebliğ | Cevap süresi sonu | YD istemi |
2. **Eksiklik bildirimi iskeleti** (dilekçe veya harç): "[DOLDUR]'a — Mahkememizin [E./K.] sayılı kararına karşı verdiğiniz [istinaf/temyiz] dilekçesindeki [eksiklik: DOLDUR]'un bildirimin tebliğinden itibaren [15 / 7] gün içinde tamamlanması, aksi hâlde [DOLDUR — m. 48/2 veya 48/6'daki sonuç] hususu bildirilir." — [DOLDUR] alanları hâkim onayıyla doldurulur.
3. **Üst yazı iskeleti:** "[DOLDUR] BÖLGE İDARE MAHKEMESİ BAŞKANLIĞINA / DANIŞTAY BAŞKANLIĞINA — Mahkememizin [E./K.] sayılı kararına karşı yapılan [istinaf / temyiz] başvurusuna ilişkin dosya, cevap süreleri dolduğundan dizi listesine bağlı olarak gönderilmiştir. [YD istemi: var / yok]" — [DOLDUR].

**Risk skalası:**
- 🔴 İvedi yargılama davasında dosyanın istinafa gönderilmesi veya 15 günlük temyiz süresinin 30 gün sanılması; cevap süresi beklenmeden gönderme.
- 🟠 Harç eksikliği bildiriminin süresi veya sonucu belirtilmeden yapılması; YD istemli dilekçenin tebliğ sırasının gözetilmemesi.
- 🟡 Dizi listesi ve ek eksikleri.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: İYUK m. 3, 8, 20/A, 20/B, 27, 45, 46, 48, 61, 62, Ek m. 1 — bu sohbette çekildi mi, eşleşti mi.
- Süre hesabı hatırlatmadır; son günü kalem ve hâkim teyit eder.
- ⚠️ "Ret ve başvurulmamış sayılma kararları yetkili merciindir; hâkim onayı şart."

## Sıradaki adımlar

- `/idari-kalem:idari-tebligat` — kararın ve dilekçelerin tebliği
- `/istinaf-kalem:dosya-kabul-kontrol` (bölge idare mahkemesi kalemi)
- `/idari-kalem:karar-uygulama-takip` — kesinleşme sonrası

---

> 🚧 v1.0.0 — `idari-kalem` 3 kalem skill'i; v1.2.0'da kanun yolu gönderme eklendi (toplam 4). Kalıp: `hukuk-hakim__skills.md`.
