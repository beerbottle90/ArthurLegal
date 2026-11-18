# vergi-hakim — Skill Referans Kitapçığı

> Dal: Vergi yargısı (vergi mahkemesi) · Rol: **Hâkim** · Usul: İYUK 2577 + VUK 213
> Toplam skill: 4
> Kullanım: `/vergi-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Vergi yargısı idari yargının parçasıdır; re'sen araştırma + İYUK usulü + VUK esas hükümleri birlikte uygulanır. Çıktılar değerlendirme iskeletidir; **takdir hâkim/heyettedir**. Her çıktı **TASLAK**.

## İçindekiler

- /vergi-hakim:vergi-karar — tarhiyat / vergi cezası davası karar iskeleti
- /vergi-hakim:tarhiyat-degerlendirme — VUK tarh türleri + ispat + matrah değerlendirme
- /vergi-hakim:odeme-emri-itiraz — 6183 m. 58 ödeme emrine itiraz (15 gün, sınırlı sebep)
- /vergi-hakim:vergi-ceza-degerlendirme — vergi ziyaı, usulsüzlük ve özel usulsüzlük cezası denetimi (VUK m. 341, 344, 351-353: kat, tekerrür, içtima, zamanaşımı, ceza kesilmeyecek hâller)

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

1. **Dava konusu işlem** — tarhiyat türü (ikmalen/re'sen/idarece — VUK m. 29, 30, mükerrer m. 30) + kesilen ceza (vergi ziyaı m. 344, usulsüzlük m. 351-352).
2. **İlk inceleme** — süre (**30 gün**, İYUK m. 7), ehliyet, husumet (doğru vergi dairesi).
3. **Usul denetimi:** tebliğ (VUK m. 93-109), tahakkuk, **tarh zamanaşımı** (VUK m. 114 — 5 yıl), takdir komisyonu süreci.
4. **Esas denetimi:** matrahın hukuki/maddi dayanağı; ispat (VUK m. 3/B — ekonomik yaklaşım, vergiyi doğuran olayın gerçek mahiyeti); re'sen takdir sebepleri var mı.
5. **Ceza denetimi:** kusur/ziyaa illiyeti; pişmanlık (m. 371), izaha davet (m. 370), uzlaşma etkisi.
6. **Hüküm (iskelet):** iptal / ret / kısmen iptal (matrah/ceza ayrı) — **seçenekli**, sonuç boş.

## Adımlar

1. VUK + ilgili vergi kanunu maddelerini MCP'den çek, atıf et.
2. Danıştay (vergi dava daireleri / VDDK) emsali ArthurLegal MCP (`tr_`)'den; yoksa "emsal teyidi gerekir".
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
   - **İdarece (mükerrer m. 30)** — m. 29 ve 30 dışında kalan hâllerde, mükellefin vergi kanunlarıyla belirli zamanda müracaat etmemesi veya kendisine yüklenen mecburiyeti yerine getirmemesi nedeniyle zamanında tarh edilemeyen verginin kanunen belli matrah üzerinden, yoklama fişine dayanılarak tarhı. (Kanuni süresi geçtiği hâlde verilmeyen beyanname re'sen tarh sebebidir — m. 30/2-1.)
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
  6183 sayılı AATUHK m. 58 ödeme emrine itiraz davası: 15 günlük özel süre,
  sınırlı itiraz sebepleri (böyle bir borç yok / kısmen ödedim / zamanaşımı),
  yürütmeyi durdurmama kuralı. Tarhiyat davasından ayrımı.
user-invocable: true
---

# Ödeme Emrine İtiraz — 6183 m. 58

## Konum

Ödeme emri **tahsil** aşaması işlemidir (tarhiyat değil). İtiraz sebepleri **sınırlıdır**; tarhiyatın esasına bu davada girilmez (o, tarhiyat davasının konusudur).

## Özellikler

1. **Süre: 15 gün** (m. 58/1 — tebliğden; 7061 s.K. ile 1.1.2018'den beri, önce 7 gündü). Genel 30 günlük vergi davası süresinden **farklı** 🔴.
2. **Sınırlı sebepler (m. 58/1):** "**böyle bir borcun olmadığı**", "**kısmen ödendiği**" veya "**zamanaşımına uğradığı**". Bunlar dışında esasa girilemez.
3. **Yürütme:** ödeme emrine dava açılması tahsilatı **kendiliğinden durdurmaz** (tarhiyat ihbarnamesinden farkı) → teminat / YD ayrı (İYUK m. 27).
4. **Haksız itiraz zammı yok:** m. 58'de haksız çıkan itiraza zam öngören fıkra AYM'nin 21.04.2022 tarihli, E.2021/119, K.2022/48 sayılı kararıyla iptal edildi; yürürlükteki metinde yer almaz.

## Hâkim için kontrol

- İtiraz 15 gün içinde mi?
- İleri sürülen sebep m. 58 kapsamında mı (yoksa tarhiyat davası gerekir)?
- Borcun aslı kesinleşmiş mi; tahsil zamanaşımı (6183 m. 102 — 5 yıl) işledi mi?

## Çıktı

Süre + sebep kapsamı + zamanaşımı kontrolü + sonuç önerisi (iptal/ret). Karar hâkimindir. TASLAK ibareli. Detay: `vergi-yargisi-rehberi.md`.

---

## /vergi-hakim:vergi-ceza-degerlendirme

---
name: vergi-ceza-degerlendirme
description: >
  Vergi ziyaı, usulsüzlük ve özel usulsüzlük cezalarının hukuka uygunluğunu VUK
  çerçevesinde denetler: cezanın türü ve dayanağı, vergi ziyaının doğup doğmadığı, kat
  ve oranlar, tekerrür, cezaların birleşmesi, ceza kesilmeyecek hâller (yanılma,
  mücbir sebep, pişmanlık), izaha davet, ceza kesmede zamanaşımı, uzlaşma ve indirim
  etkisi. Ceza yönünden iptal veya ret sonucunu DAYATMAZ.
user-invocable: true
---

# Vergi Cezası Değerlendirmesi — VUK

## Konum hatırlatması

Vergi mahkemesi idari yaptırımın hukuka uygunluğunu denetler; kaçakçılık suçlarına ilişkin hapis cezası ceza yargılamasının konusudur. Vergi aslına bağlı cezada tarhiyat hakkındaki değerlendirme cezayı doğrudan etkiler; ceza ayrıca ve kendi unsurlarıyla denetlenir. Sonuç hâkim/heyet takdiridir. Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir.

## Amaç

Dava konusu vergi cezasının türünü, dayanağını ve hesaplanmasını VUK hükümleriyle karşılaştırarak denetlemek; cezayı etkileyen hâlleri (tekerrür, ceza kesilmeyecek hâller, zamanaşımı, uzlaşma ve indirim) iki yönlü göstermek.

## Dayanak (bu sohbette çekilir)

- **VUK m. 341** — vergi ziyaı: mükellefin veya sorumlunun vergilendirmeyle ilgili ödevlerini zamanında yerine getirmemesi veya eksik yerine getirmesi yüzünden verginin zamanında tahakkuk ettirilmemesi veya eksik tahakkuk ettirilmesi; gerçeğe aykırı beyanlarla verginin noksan tahakkuku veya haksız iadesi de vergi ziyaı hükmündedir.
- **VUK m. 344** — ziyaa uğratılan verginin bir katı; m. 359'daki fiillerle ziyaa sebebiyet verilmişse üç kat, bu fiillere iştirak edenlere bir kat; vergi incelemesine başlanmasından veya takdir komisyonuna sevkten önce, kanuni süresinden sonra verilen beyannamelerde yüzde elli; mükellefiyet tesis ettirilmeksizin faaliyette bulunularak vergi ziyaına sebebiyet verilmesinde yüzde elli artırım.
- **VUK m. 351, 352, 353, mükerrer m. 355** — usulsüzlüğün tarifi; usulsüzlük dereceleri ve 1 sayılı cetvel (usulsüzlük re'sen takdiri gerektiriyorsa cezalar iki kat); özel usulsüzlükler. Tutarlar her yıl güncellenir; güncel tutar çekilir.
- **VUK m. 336** — cezayı gerektiren tek bir fiille vergi ziyaı ve usulsüzlük birlikte işlenmişse miktar itibarıyla en ağırı kesilir; usulsüzlük cezası kesilen fiille vergi ziyaına da sebebiyet verildiği sonradan anlaşılırsa mukayese ve noksanın ikmali.
- **VUK m. 339** — tekerrür: ceza kesinleştikten sonra, vergi ziyaında beşinci, usulsüzlükte ikinci yılın isabet ettiği takvim yılı sonuna kadar yeniden ceza kesilirse vergi ziyaı cezası yüzde elli, usulsüzlük cezası yüzde yirmi beş artırılır; artırım tutarı kesinleşen cezayı aşamaz; sürelerde kesinleşme tarihi esas alınır.
- **VUK m. 359** — kaçakçılık suçları ve cezaları (ceza yargılaması).
- **VUK m. 369** — yetkili makamların mükellefe yazıyla yanlış izahat vermiş olması veya bir hükmün uygulanma tarzına ilişkin içtihadın değişmiş olması hâlinde vergi cezası kesilmez ve gecikme faizi hesaplanmaz.
- **VUK m. 373, 13** — mücbir sebeplerden birinin vukuu malumsa veya tevsik ve ispat olunursa vergi cezası kesilmez; mücbir sebepler (ağır kaza, ağır hastalık, tutukluluk; afetler; iradesi dışında gaybubet; defter ve belgelerin iradesi dışında elden çıkması).
- **VUK m. 370** — izaha davet: şartları içinde izah ve ödeme yapılırsa vergi ziyaı cezası yüzde yirmi oranında kesilir; m. 359 kapsamındaki ön tespitlerde sınırlı uygulama.
- **VUK m. 371** — pişmanlık ve ıslah: kendiliğinden haber verme ve süreli şartlar yerine getirilirse vergi ziyaı cezası kesilmez.
- **VUK m. 374** — ceza kesmede zamanaşımı: vergi ziyaı cezasında cezanın bağlı olduğu vergi alacağının doğduğu yılı izleyen yılın başından, m. 353 ve mükerrer m. 355 usulsüzlük cezalarında usulsüzlüğün yapıldığı yılı izleyen yılın başından itibaren beş yıl; diğer usulsüzlüklerde iki yıl; m. 336 birleşmesinde vergi ziyaı süresi; ceza ihbarnamesinin tebliği zamanaşımını keser.
- **VUK m. 376** — indirim: ihbarnamenin tebliğinden itibaren otuz gün içinde başvurulup vadesinde veya teminatla ödeneceği bildirilirse cezanın yarısı indirilir; ödenmez veya dava konusu yapılırsa indirimden yararlanılmaz.
- **VUK Ek m. 1, Ek m. 6, Ek m. 11** — uzlaşma (cezalar yönünden; talep ihbarnamenin tebliğinden itibaren otuz gün içinde); uzlaşılan ve tutanakla tespit olunan hususlar hakkında dava açılamaz (Ek m. 6); tarhiyat öncesi uzlaşmaya varılan hususta dava açılamaz (Ek m. 11).
- **VUK m. 377, 378** — mükellefler ve kendilerine vergi cezası kesilenler vergi mahkemesinde dava açabilir; mükellefler beyan ettikleri matrahlara ve bunlar üzerinden tarh edilen vergilere karşı dava açamaz (vergi hatalarına ilişkin hükümler saklı).
- **İYUK m. 7, 27/4** — vergi mahkemesinde dava açma süresi otuz gün; vergi uyuşmazlıklarında dava açılması dava konusu vergi ve cezaların tahsil işlemlerini durdurur (istisnalarıyla).

## Girdi

- Ceza ihbarnamesi: türü, dönemi, tutarı, kat veya oran, tekerrür uygulanıp uygulanmadığı, tebliğ tarihi
- Bağlı tarhiyat (varsa) ve onun dava durumu; vergi inceleme raporu
- İleri sürülen savunmalar: yanılma, mücbir sebep, pişmanlık, izaha davet, zamanaşımı, içtima
- Uzlaşma ve indirim başvuruları

## Adımlar

1. **Ceza türü ve dayanak:** vergi ziyaı / usulsüzlük (derece) / özel usulsüzlük; ihbarnamedeki madde doğru mu.
2. **Unsur:** vergi ziyaı doğmuş mu (m. 341); bağlı tarhiyat iptal edilirse cezanın akıbeti ayrı hüküm kalemi olarak kurulur.
3. **Kat ve oran:** m. 344'ün hangi fıkrası; üç kat için m. 359 kapsamındaki fiilin tespit edilmiş olması; süresi geçmiş beyanname hâli; mükellefiyet tesis ettirmeme artırımı.
4. **Tekerrür:** önceki cezanın kesinleşme tarihi, süre penceresi, oran ve üst sınır (m. 339).
5. **Birleşme:** tek fiil — m. 336.
6. **Ceza kesilmeyecek hâller:** m. 369 (yazılı yanlış izahat, içtihat değişikliği), m. 373 ve 13 (mücbir sebep), m. 371 şartları; izaha davet (m. 370) uygulanabilir miydi.
7. **Zamanaşımı:** m. 374 süresi ve ceza ihbarnamesinin tebliğ tarihi.
8. **Uzlaşma ve indirim:** uzlaşılan hususta dava açılamaz (Ek m. 6, Ek m. 11); indirimden yararlanıp dava açılmış mı (m. 376).
9. **Hesap kontrolü:** matrah farkı → vergi → ceza; rakamlar kullanıcıdan gelir, asistan tutar üretmez.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Ceza denetim tablosu:** | Unsur | Dayanak | İhbarnamedeki | Dosyadaki | Değerlendirme (hukuka uygun / aykırı / eksik) | Risk |
2. **Hesap kontrol satırları:** [DOLDUR] alanlı; kat, oran, tekerrür artırımı, üst sınır.
3. **İki yönlü gerekçe iskeleti:** ceza yönünden iptal ve ret gerekçeleri ayrı; kısmen iptal (kat veya tekerrür düzeltmesi) seçeneği.
4. **Hüküm iskeleti:** vergi aslı ve ceza ayrı kalemler; sonuç boş.

**Risk skalası:**
- 🔴 Ceza kesme zamanaşımı dolmuş; tek fiilde birleşme (m. 336) uygulanmamış; üç kat ceza m. 359 kapsamındaki fiil tespit edilmeden uygulanmış.
- 🟠 Tekerrür penceresi, oranı veya üst sınırı yanlış; m. 369 veya mücbir sebep iddiası karşılanmamış.
- 🟡 Özel usulsüzlük tutarının ilgili yıl tutarıyla karşılaştırılmaması; hesap hatası.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: VUK m. 13, 336, 339, 341, 344, 351, 352, 353, mükerrer m. 355, 359, 369, 370, 371, 373, 374, 376, 377, 378, Ek m. 1, Ek m. 6, Ek m. 11; İYUK m. 7, 27 — bu sohbette çekildi mi, eşleşti mi. VUK m. 338 mülgadır; atıf yapılmaz.
- Yıllık güncellenen tutarlar (özel usulsüzlük, uzlaşma sınırı) çekilmediyse UYARI satırı.
- Danıştay vergi dava daireleri ve Vergi Dava Daireleri Kurulu içtihadı: `tr_ictihat_ara(courts=["DANISTAYKARAR"], chamber="VDDK", …)` → yalnız okunan kararlar.
- Süre ve zamanaşımı hesapları hatırlatmadır; son günü hâkim/kalem teyit eder. Tebliğ tarihi gibi bilinmeyen bir olguda en erken olası gün esas alınır ve bu açıkça uyarı olarak yazılır.
- ⚠️ "Sonuç ve takdir hâkime/heyete aittir."

## Sıradaki adımlar

- `/vergi-hakim:tarhiyat-degerlendirme` — bağlı tarhiyat
- `/vergi-hakim:vergi-karar` — karar iskeleti
- `/yargi-arastirma:emsal-tarama` — ceza meselesinde Danıştay çizgisi

---

> 🚧 v1.0.0 — `vergi-hakim` 3 skill; v1.2.0'da vergi cezası değerlendirmesi eklendi (toplam 4). Kalıp: `hukuk-hakim__skills.md`.
