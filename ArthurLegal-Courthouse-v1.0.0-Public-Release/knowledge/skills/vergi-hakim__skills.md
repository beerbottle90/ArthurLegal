# vergi-hakim — Skill Referans Kitapçığı

> Dal: Vergi yargısı (vergi mahkemesi) · Rol: **Hâkim** · Usul: İYUK 2577 + VUK 213
> Toplam skill: 3
> Kullanım: `/vergi-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Vergi yargısı idari yargının parçasıdır; re'sen araştırma + İYUK usulü + VUK esas hükümleri birlikte uygulanır. Çıktılar değerlendirme iskeletidir; **takdir hâkim/heyettedir**. Her çıktı **TASLAK**.

## İçindekiler

- /vergi-hakim:vergi-karar — tarhiyat / vergi cezası davası karar iskeleti
- /vergi-hakim:tarhiyat-degerlendirme — VUK tarh türleri + ispat + matrah değerlendirme
- /vergi-hakim:odeme-emri-itiraz — 6183 m. 58 ödeme emrine itiraz (7 gün, sınırlı sebep)

---

## /vergi-hakim:vergi-karar

---
name: vergi-karar
description: >
  Tarhiyatın/vergi cezasının iptali davasında karar iskeleti: tarhiyatın hukuki dayanağı,
  usul (tebliğ, tahakkuk, zamanaşımı), matrah/ceza denetimi, re'sen araştırma. Sonucu DAYATMAZ.
user-invocable: true
---

# Vergi Kararı — Tarhiyat/Ceza İptali İskeleti

## Konum hatırlatması

Vergi yargısı idari yargı usulüyle (İYUK) yürür; esasta VUK + ilgili vergi kanunu uygulanır. Re'sen araştırma geçerli. Sonuç hâkim/heyet takdiridir.

## Çıktı yapısı

1. **Dava konusu işlem** — tarhiyat türü (ikmalen/re'sen/idarece, VUK m. 29-30) + kesilen ceza (vergi ziyaı m. 344, usulsüzlük m. 351-352).
2. **İlk inceleme** — süre (**30 gün**, İYUK m. 7), ehliyet, husumet (doğru vergi dairesi).
3. **Usul denetimi:** tebliğ (VUK m. 93-109), tahakkuk, **tarh zamanaşımı** (VUK m. 114 — 5 yıl), takdir komisyonu süreci.
4. **Esas denetimi:** matrahın hukuki/maddi dayanağı; ispat (VUK m. 3/B — ekonomik yaklaşım, vergiyi doğuran olayın gerçek mahiyeti); re'sen takdir sebepleri var mı.
5. **Ceza denetimi:** kusur/ziyaa illiyeti; pişmanlık (m. 371), izaha davet (m. 370), uzlaşma etkisi.
6. **Hüküm (iskelet):** iptal / ret / kısmen iptal (matrah/ceza ayrı) — **seçenekli**, sonuç boş.

## Adımlar

1. VUK + ilgili vergi kanunu maddelerini MCP'den çek, atıf et.
2. Danıştay (vergi dava daireleri / VDDK) emsali Yargı MCP'den; yoksa "emsal teyidi gerekir".
3. Usul ve esas itirazlarını ayrı değerlendir; iptal/ret gerekçesini ayrı kur.

## İnceleyen notu

- Kullanılan VUK/vergi kanunu maddeleri + Danıştay emsali (atıflı)
- Zamanaşımı / tebliğ usulü kontrol sonucu
- ⚠️ "Sonuç ve takdir hâkime/heyete aittir."

---

## /vergi-hakim:tarhiyat-degerlendirme

---
name: tarhiyat-degerlendirme
description: >
  VUK tarh türleri (beyana dayanan / ikmalen / re'sen / idarece) ve ispat yükü çerçevesinde
  matrahın ve cezanın hukuka uygunluğunu değerlendirme metodu. Takdiri DAYATMAZ.
user-invocable: true
---

# Tarhiyat Değerlendirme — VUK

## Amaç

Tarhiyatın türüne göre denetim ölçütlerini yapılandır.

## Yöntem

1. **Tarh türü tespiti:**
   - Beyana dayanan (kural) — ihtirazi kayıt varsa dava hakkı.
   - **İkmalen (m. 29)** — defter/belge/kanuni ölçüye dayanan ek matrah.
   - **Re'sen (m. 30)** — matrah tespiti mümkün değilse; re'sen sebepleri sınırlı sayıda mı.
   - **İdarece (m. 30 son)** — verilmeyen beyanname vb.
2. **İspat yükü (VUK m. 3/B):** iktisadi/ticari icaplara uymayan veya olağandışı durumu **iddia eden** ispatla yükümlü; vergiyi doğuran olayın gerçek mahiyeti esas.
3. **Takdir komisyonu / matrah** — dayanağı denetime elverişli mi.
4. **Ceza illiyeti:** vergi ziyaı doğdu mu, kusur derecesi; tekerrür (m. 339).
5. **Süre & zamanaşımı:** tarh zamanaşımı (m. 114), ceza kesme zamanaşımı (m. 374).

## Çıktı

Tarh türü × dayanak × ispat-yükü tablosu + matrah/ceza için "hukuka uygun / aykırı / eksik" ölçütlü değerlendirme. Sonuç hâkim takdirine bırakılır. Detay: `vuk-rehberi.md`, `vergi-yargisi-rehberi.md`, `gib-ozelge-rehberi.md`.

---

## /vergi-hakim:odeme-emri-itiraz

---
name: odeme-emri-itiraz
description: >
  6183 sayılı AATUHK m. 58 ödeme emrine itiraz davası: 7 günlük özel süre,
  sınırlı itiraz sebepleri (böyle bir borç yok / kısmen ödedim / zamanaşımı),
  yürütmeyi durdurmama kuralı. Tarhiyat davasından ayrımı.
user-invocable: true
---

# Ödeme Emrine İtiraz — 6183 m. 58

## Konum

Ödeme emri **tahsil** aşaması işlemidir (tarhiyat değil). İtiraz sebepleri **sınırlıdır**; tarhiyatın esasına bu davada girilmez (o, tarhiyat davasının konusudur).

## Özellikler

1. **Süre: 7 gün** (m. 58/1 — tebliğden). Genel 30 günlük vergi davası süresinden **farklı** 🔴.
2. **Sınırlı sebepler (m. 58/1):** "**böyle bir borcun olmadığı**", "**kısmen ödendiği**" veya "**zamanaşımına uğradığı**". Bunlar dışında esasa girilemez.
3. **Yürütme:** ödeme emrine dava açılması tahsilatı **kendiliğinden durdurmaz** (tarhiyat ihbarnamesinden farkı) → teminat / YD ayrı (İYUK m. 27).
4. **Haksız itiraz (m. 58):** tamamen/kısmen reddedilen itirazda zam riski (oran için mevzuat teyidi).

## Hâkim için kontrol

- İtiraz 7 gün içinde mi?
- İleri sürülen sebep m. 58 kapsamında mı (yoksa tarhiyat davası gerekir)?
- Borcun aslı kesinleşmiş mi; tahsil zamanaşımı (6183 m. 102 — 5 yıl) işledi mi?

## Çıktı

Süre + sebep kapsamı + zamanaşımı kontrolü + sonuç önerisi (iptal/ret). Karar hâkimindir. TASLAK ibareli. Detay: `vergi-yargisi-rehberi.md`.

---

> 🚧 v1.0.0 — `vergi-hakim` 3 skill. Kalıp: `hukuk-hakim__skills.md`.
