# vergi-kalem — Skill Referans Kitapçığı

> Dal: Vergi yargısı (vergi mahkemesi) · Rol: **Kalem (yazı işleri)** · Usul: İYUK 2577 + VUK 213 + Tebligat K. 7201
> Toplam skill: 4
> Kullanım: `/vergi-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar belge iskeleti + kontrol listesidir; hâkim havalesi/onayı şarttır. Her çıktı **TASLAK**.

## İçindekiler

- /vergi-kalem:vergi-tebligat — VUK m. 93-109 tebliğ + İYUK kanun yolu süresi
- /vergi-kalem:vergi-sure-takip — dava açma / yürütme / tahsilat süre takibi
- /vergi-kalem:karar-uygulama-iade — kesinleşme + vergi dairesine gönderme + terkin/iade takibi
- /vergi-kalem:dosya-tekemmul — vergi davasında dilekçe ve savunma teatisi, işlem dosyası, ara karar takibi, tekemmül ve sunum (İYUK m. 16-20)

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

## /vergi-kalem:dosya-tekemmul

---
name: dosya-tekemmul
description: >
  Vergi davasında dilekçe ve savunmaların teatisi ile dosyanın karara hazır hâle
  gelmesini yönetir: vergi dairesinden istenecek işlem dosyası ve tebliğ belgeleri,
  savunma ve cevap süreleri, ara karar takibi, duruşma talebi, tek hâkim / heyet sunum
  notu. Kalem kontrol listesi ve takip tablosu.
user-invocable: true
---

# Vergi Davasında Dosyanın Tekemmülü — İYUK m. 16-20

## Konum hatırlatması

Tekemmül, tarafların dilekçe ve savunma haklarını kullanmasıyla oluşur; süreler dolmadan dosyanın karara çıkarılması çelişmeli yargılama sorununa yol açar. Davanın tek hâkimle mi heyetle mi görüleceği ve duruşma yapılıp yapılmayacağı hâkim/heyet kararıdır; kalem bilgi sunar. Asistan UYAP'ta işlem yapmaz.

## Amaç

Vergi davasında dilekçe ve savunmaların karşılıklı verilmesini ve dosyanın karara hazır hâle gelmesini takip etmek; vergi dairesinden istenecek belgeleri ve süreleri tek tabloda izlemek.

## Dayanak (bu sohbette çekilir)

- **İYUK m. 16** — dava dilekçesi ve ekleri davalıya, savunma davacıya tebliğ edilir; ikinci dilekçe ve ikinci savunma (m. 16/2); taraflar tebliğden itibaren otuz gün içinde cevap verebilir, süre haklı sebeple taraflardan birinin isteği üzerine mahkeme kararıyla otuz günü geçmemek ve bir defaya mahsus olmak üzere uzatılabilir, süre geçtikten sonraki uzatma talepleri kabul edilmez (m. 16/3); süreden sonra verilen savunma veya ikinci dilekçeye dayanarak hak iddia edilemez (m. 16/4); işlem dosyasının aslı veya onaylı örneği savunmayla birlikte gönderilir (m. 16/5).
- **İYUK m. 17** — vergi davalarında tarh edilen vergi ile zam ve cezaları toplamı metindeki tutarı aşan uyuşmazlıklarda taraflardan birinin isteği üzerine duruşma yapılır (tutar Ek m. 1 ile güncellenir); duruşma talebi dava dilekçesi, cevap ve savunmalarda yapılabilir; mahkeme kendiliğinden de duruşmaya karar verebilir; davetiyeler duruşmadan en az otuz gün önce gönderilir.
- **İYUK m. 19, 20** — duruşmalı işlerde karar; re'sen inceleme ve ara karar; tekemmül sırası ve altı ay (m. 20/5).
- **İYUK m. 27/4-5** — vergi uyuşmazlıklarında dava açılması dava konusu vergi ve cezaların tahsil işlemlerini durdurur (istisnalarıyla); yürütmenin durdurulması istemli davalarda m. 16 süreleri kısaltılabilir.
- **İYUK m. 3/2-e** — vergi davalarında dilekçede verginin veya vergi cezasının nevi ve yılı, tebliğ edilen ihbarnamenin tarihi ve numarası ile varsa mükellef hesap numarası gösterilir.
- **2576 s.K. m. 7/2** — metinde gösterilen toplam değeri aşmayan vergi uyuşmazlıkları vergi mahkemesi hâkimlerinden biri tarafından çözümlenir (tutar 7589 s.K. ile 16.07.2026'da değişti; güncel tutar çekilir).
- **VUK m. 31** (takdir kararının içeriği), **mükerrer m. 30** (idarece tarhta yoklama fişi ve ilan), **m. 378/2** (mükellefler beyan ettikleri matrahlara ve bunlar üzerinden tarh edilen vergilere karşı dava açamaz; vergi hatalarına ilişkin hükümler saklı), **Ek m. 6, Ek m. 11** (uzlaşılan hususlarda dava açılamaz).
- **6183 s.K. m. 55, 58** — ödeme emri ve ödeme emrine itiraz (on beş gün, sınırlı sebepler).

## Girdi

- Dava dilekçesinin kayıt tarihi, dava konusu (tarhiyat, ceza, ödeme emri) ve miktarı [DOLDUR]
- Dilekçenin vergi dairesine tebliğ tarihi; savunma ve cevap dilekçelerinin tarihleri [DOLDUR]
- Varsa ara kararlar ve cevap süreleri [DOLDUR]
- Duruşma talebi olup olmadığı [DOLDUR]
- Dosya bilgisi kullanıcıdan gelir; asistan UYAP'a bağlanmaz, kayıt eklemez.

## İşlem dosyası kontrol listesi (vergi dairesinden)

- [ ] Vergi veya ceza ihbarnamesi ve **tebliğ belgesi** (tebliğ şekli: posta, memur, elektronik ortam, ilan)
- [ ] Vergi inceleme raporu ve ekleri; tutanaklar
- [ ] Takdir komisyonu kararı (VUK m. 31 unsurları) ve tevdi belgesi
- [ ] İdarece tarhta yoklama fişi ve ilan tutanağı (mükerrer m. 30)
- [ ] Uzlaşma tutanakları (uzlaşılan hususta dava açılamaz — Ek m. 6, Ek m. 11)
- [ ] İhtirazi kayıtla verilen beyanname (beyana dayalı tarhiyatta)
- [ ] Ödeme emri davasında ödeme emri ve tebliğ belgesi (6183 s.K. m. 55, 58)

## Süreç ve süre takibi

1. İlk inceleme sonrası dava dilekçesinin tebliği → savunma süresi (30 gün; uzatma talebi süresi içinde mi — m. 16/3)
2. Savunmanın davacıya tebliği → cevap (30 gün) → ikinci savunma (30 gün) (m. 16/2-3)
3. Ara kararlar: tebliğ, süre, uzatma, cevap, karşı tarafa bildirim (m. 20)
4. Duruşma talebi varsa ve duruşma yapılmasına karar verilirse davetiye en az otuz gün önce (m. 17/5)
5. Tekemmül: süreler dolmuş, ara kararlar karşılanmış → tekemmül tarihi; heyet / tek hâkim sunum notu (2576 m. 7/2)
6. Çalışmaya ara verme: süre sonu ara vermeye rastlarsa ara vermenin sona erdiği günü izleyen tarihten itibaren yedi gün uzar (İYUK m. 8/3; m. 61)

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Tekemmül takip tablosu:** | İşlem | Tebliğ tarihi | Süre | Son gün (en erken) | Uzatma | Durum |
2. **İşlem dosyası eksik listesi** ve vergi dairesine yazı iskeleti: "[DOLDUR] Vergi Dairesi Müdürlüğüne — Mahkememizin [E.] sayılı dosyasında, dava konusu [ihbarname / ödeme emri]'ne ilişkin işlem dosyasının aslı veya onaylı örneği ile [tebliğ belgesi, inceleme raporu, takdir komisyonu kararı — DOLDUR]'nun [süre] içinde gönderilmesi rica olunur."
3. **Sunum notu:** tekemmül tarihi, duruşma talebi, tek hâkim / heyet bilgisi (tutar güncel metinden), tahsil durumu veya YD istemi.

**Risk skalası:**
- 🔴 Savunma veya cevap süresi dolmadan tekemmül; savunmanın davacıya tebliğ edilmemesi.
- 🟠 İşlem dosyasında tebliğ belgesi veya inceleme raporu eksik (süre ve esas denetimi yapılamaz).
- 🟡 Duruşma talebinin sunum notunda gösterilmemesi; tek hâkim / heyet bilgisinin güncel tutara göre kontrol edilmemesi.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: İYUK m. 3, 8, 16, 17, 19, 20, 27, 61, Ek m. 1; 2576 s.K. m. 7; VUK m. 31, mükerrer m. 30, m. 378, Ek m. 6, Ek m. 11; 6183 s.K. m. 55, 58 — bu sohbette çekildi mi, eşleşti mi.
- Süre hesabı hatırlatmadır; son günü kalem ve hâkim teyit eder.
- ⚠️ "Tekemmül ve sunum sırası hâkim/heyet onayına tabidir."

## Sıradaki adımlar

- `/vergi-kalem:vergi-sure-takip`
- `/vergi-hakim:vergi-karar`, `/vergi-hakim:vergi-ceza-degerlendirme`
- `/idari-hakim:ara-karar-bilgi-belge` — vergi dosyasında bilgi ve belge ara kararı (aynı İYUK m. 20)

---

> 🚧 v1.0.0 — `vergi-kalem` 3 kalem skill'i; v1.2.0'da dosyanın tekemmülü eklendi (toplam 4). Kalıp: `hukuk-hakim__skills.md`.
