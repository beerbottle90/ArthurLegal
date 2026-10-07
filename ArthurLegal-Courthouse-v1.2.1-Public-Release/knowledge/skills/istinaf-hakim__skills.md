# istinaf-hakim — Skill Referans Kitapçığı

> Dal: İstinaf — bölge adliye mahkemesi hukuk ve ceza daireleri, bölge idare mahkemesi idari ve vergi dava daireleri · Rol: **Hâkim / heyet** · Usul: HMK 6100 m. 341-360, CMK 5271 m. 272-285, İYUK 2577 m. 45
> Toplam skill: 4
> Kullanım: `/istinaf-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Çıktılar ön inceleme ve esas inceleme iskeleti ile karar türü seçenek analizidir; karar türünü ve sonucu **heyet** belirler. İnceleme kapsamı her usul kanununda ayrıdır ve metinden çekilerek uygulanır. Asistan UYAP'a bağlanmaz; dosya bilgisi kullanıcıdan gelir. Her çıktı **TASLAK — hâkim/heyet onayı şart**.

## İçindekiler

- /istinaf-hakim:hukuk-on-inceleme — HMK m. 352 ön inceleme: daire, kesinlik, süre, başvuru şartları, sebep gösterme; dosyanın incelemeye hazırlığı
- /istinaf-hakim:hukuk-esas-karar — HMK m. 353-360 esas inceleme ve karar türleri (kaldırma, esastan ret, düzelterek ve yeniden esas hakkında karar, duruşmalı inceleme)
- /istinaf-hakim:ceza-istinaf-inceleme — CMK m. 272-284 ön inceleme, esas inceleme ve karar türleri
- /istinaf-hakim:idari-istinaf — İYUK m. 45 bölge idare mahkemesi incelemesi ve karar türleri

---

## /istinaf-hakim:hukuk-on-inceleme

---
name: hukuk-on-inceleme
description: >
  Bölge adliye mahkemesi hukuk dairesine gelen istinaf dosyasının HMK m. 352 ön
  incelemesini yapılandırır: dairenin görevi ve iş bölümü, kararın kesin olup olmadığı,
  başvurunun süresi, başvuru şartları, başvuru sebeplerinin hiç gösterilmemesi; ayrıca
  dosyanın incelemeye hazır olup olmadığı (tebligat, cevap süresi, harç). Kararı VERMEZ;
  heyetin önüne seçenekli ön inceleme raporu koyar.
user-invocable: true
---

# İstinaf Ön İncelemesi (Hukuk) — HMK m. 352

## Konum hatırlatması

Ön inceleme dosya üzerinde yapılır; heyetçe veya görevlendirilen bir üye tarafından yürütülür, karar heyetçe verilir (HMK m. 352/2). Bu skill heyetin önüne tespit ve seçenek koyar; hangi kararın verileceği heyet takdiridir. Asıl başvuru ve katılma yoluyla başvuru aynı ölçütle incelenir. Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir. **Başvurunun reddi veya dosyanın geri çevrilmesi gibi her ön inceleme kararı için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

İstinaf dosyasının ön inceleme aşamasında heyetin önüne görev, kesinlik, süre, başvuru şartları ve dosyanın incelemeye hazır olup olmadığı yönünden tespitleri ve seçenekleri gösteren bir rapor koymak.

## Girdi

Kullanıcıdan (eksikse iste, varsayma):
- İlk derece kararı: mahkeme, E./K., karar tarihi, dava türü ve değeri, davanın açıldığı tarih
- Kararın her tarafa tebliğ tarihi ve tebliğ şekli (e-tebligat ise elektronik adrese ulaştığı tarih)
- İstinaf dilekçesi veya dilekçeleri: kayıt tarihi, verildiği mahkeme, başvuru sebepleri
- Karşı tarafa tebliğ tarihi, cevap dilekçesi ve varsa katılma yoluyla istinaf
- Harç ve gider makbuzları; ilk derece mahkemesince verilmiş ret veya "başvuru yapılmamış sayılma" kararı varsa onun tebliği
- Dairenin iş bölümü (UYAP'ta dosyadan / başkanlar kurulu kararı)

## Kontrol listesi (HMK m. 352/1 sırasıyla)

1. **Daire ve bölge (a).** İnceleme başka bir dairece veya başka bir bölge adliye mahkemesince mi yapılmalı? Daireler arası iş bölümü uyuşmazlığı başkanlar kurulunca karara bağlanır (5235 s.K. m. 35/1-1). 🟠 yanlış dairede inceleme.
2. **Kararın kesinliği (b).**
   - İstinafa tabi karar mı: nihai karar ya da ihtiyati tedbir ve ihtiyati hacizle ilgili m. 341/1-b'de sayılan kararlar.
   - Parasal kesinlik sınırı: HMK m. 341/2'deki tutar Ek m. 1 uyarınca her yıl yeniden değerleme oranında artırılır ve davanın açıldığı tarihteki sınır esas alınır (Ek m. 1/2). Manevi tazminat davalarında miktara bakılmaksızın istinaf yolu açıktır (m. 341/2). Alacağın bir kısmı dava edilmişse sınır alacağın tamamına göre (m. 341/3); tamamı dava edilmişse asıl talebin kabul edilmeyen bölümü esas alınır (m. 341/4).
   - Güncel sınır tutarı hafızadan yazılmaz; çekilir ya da `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.
3. **Süre (c).** İki hafta; ilamın usulen taraflardan her birine tebliğiyle ayrı ayrı işler (m. 345). Kontrol: tebliğ usule uygun mu (Tebligat K. m. 21, 35; e-tebligatta elektronik adrese ulaşmayı izleyen beşinci günün sonu — Tebligat K. m. 7/a); başvuru tarihi, m. 343/3'ün yollamasıyla dilekçenin kaydedildiği tarihtir (m. 118/1); süre sonu resmî tatile veya adli tatile rastlıyor mu (m. 93, 104). Bilinmeyen tebliğ tarihinde en erken ihtimal esas alınır ve 🟠 ile işaretlenir.
4. **Başvuru şartları (ç).** Harç ve giderler yatırılmış mı (m. 344 — eksiklik ilk derece mahkemesince bir haftalık kesin süreyle tamamlatılır; tamamlanmazsa başvuru yapılmamış sayılır); dilekçenin asgari unsurları (m. 342/3: başvuranın kimliği, imzası ve kararı yeteri kadar belli edecek kayıtlar varsa diğer eksikler ret sebebi değildir); başvuranın sıfatı; feragat (m. 349).
5. **Sebep ve gerekçe (d).** Başvuru sebepleri veya gerekçesi **hiç** gösterilmemiş mi? Kısmen gösterilmişse ret sebebi değildir; inceleme gösterilen sebeplerle sınırlı yapılır, kamu düzenine aykırılık resen gözetilir (m. 355).
6. **Dosyanın incelemeye hazırlığı.** İstinaf dilekçesi karşı tarafa tebliğ edilmiş ve iki haftalık cevap süresi dolmuş mu (m. 347); katılma yoluyla başvuruya karşı asıl başvuranın iki haftalık cevap süresi (m. 348/1). Süre dolmadan gelen dosya için geri çevirme → `/istinaf-kalem:geri-cevirme`. Anayasa Mahkemesi, cevap süresi dolmadan dosyanın gönderilip dairece kesin karar verilmesini silahların eşitliği ve çelişmeli yargılama ilkelerinin ihlali saymıştır `[ArthurLegal TR — AYM — B. No: 2017/18458 — 10.02.2021]` (27.09.2026'da çekildi; çıktıya girecekse `tr_aym_getir` ile yeniden çekilir).
7. **İlk derece mahkemesince verilmiş ret kararı.** Süre veya kesinlik nedeniyle ilk derece mahkemesi dilekçeyi reddetmişse (m. 346/1), bu karara karşı tebliğden itibaren iki hafta içinde istinaf yoluna başvurulabilir; daire ret kararını yerinde görmezse ilk istinaf dilekçesine göre gerekli incelemeyi yapar (m. 346/2).
8. **Kaldırma sebeplerine ilk bakış.** Esasa geçmeden görülen m. 353/1-a hâlleri (yasak hâkim, haklı ret talebine rağmen davaya bakan hâkim, görev ve yetki, diğer dava şartları, usule aykırı açılmamış sayılma, birleştirme veya ayırma, önemli delillerin toplanmaması veya değerlendirilmemesi, talebin önemli bir kısmı hakkında karar verilmemesi) not edilir → `/istinaf-hakim:hukuk-esas-karar`.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Ön inceleme tablosu**

| Denetim | Dayanak | Dosyadaki durum | Değerlendirme | Risk |
|---|---|---|---|---|
| Daire / bölge | HMK m. 352/1-a | [DOLDUR] | uygun / başka daire | 🟢/🟠 |
| Kesinlik | m. 341, 352/1-b, Ek m. 1 | [DOLDUR — değer, dava tarihi] | istinafa tabi / kesin | |
| Süre (her başvuran için ayrı) | m. 345, 352/1-c | tebliğ: [DOLDUR] · başvuru: [DOLDUR] | süresinde / süre geçmiş / tebliğ belirsiz | |
| Başvuru şartları | m. 342, 344, 349, 352/1-ç | [DOLDUR] | | |
| Sebep / gerekçe | m. 352/1-d, 355 | [DOLDUR] | gösterilmiş / kısmen / hiç | |
| Cevap süreleri | m. 347, 348 | [DOLDUR] | dolmuş / dolmamış → geri çevirme | |

2. **Ön inceleme sonucu seçenekleri** (heyet takdiri): (i) dosyanın görevli daireye veya bölge adliye mahkemesine gönderilmesi; (ii) kesin karar nedeniyle başvurunun reddi; (iii) süre nedeniyle başvurunun reddi; (iv) başvuru şartı eksikliği — tamamlatılabilir mi, tamamlatılamaz mı; (v) başvuru sebeplerinin hiç gösterilmemesi nedeniyle ret; (vi) eksiklik yoksa dosyanın incelemeye alınması (m. 352/3).
3. **Geri çevirme listesi** (varsa): eksiklik, kime, dayanak.
4. **Kanun yolu notu:** verilecek kararın temyiz edilebilirliği HMK m. 362'den (güncel metin ve dipnotlarıyla) çekilerek yazılır.

**Risk skalası:**
- 🔴 Cevap süresi dolmadan incelemeye geçilmesi; tebliği usulsüz tarafa karşı süre aşımı kabulü; kesin olmayan kararın kesin sayılması.
- 🟠 Tebliğ tarihi belirsiz; iş bölümü tereddütlü; harç eksikliğinin ilk derece mahkemesince m. 344'e göre tamamlatılmamış olması.
- 🟡 Dilekçenin m. 342/2 unsurlarında giderilebilir eksik.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 93, 104, 118, 341, 342, 343, 344, 345, 346, 347, 348, 349, 352, 353, 355, 362, Ek m. 1; Tebligat K. m. 7/a, 21, 35; 5235 s.K. m. 35 — bu sohbette `tr_mevzuat_madde_getir` ile çekildi mi, eşleşti mi.
- Süre hesabı hatırlatmadır; son günü heyet ve kalem teyit eder. Bilinmeyen olguda en erken gün esas alınmıştır.
- Parasal sınırın güncel tutarı çekilemediyse: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.
- ⚠️ "Ön inceleme kararı heyetçe verilir (HMK m. 352/2); sonuç heyet takdirindedir."

## Sıradaki adımlar

- `/istinaf-hakim:hukuk-esas-karar` — incelemeye alınan dosyada karar türü
- `/istinaf-kalem:geri-cevirme` — eksiklik yazısı
- `/yargi-arastirma:emsal-tarama` — kesinlik veya süre meselesinde dairenin ve Yargıtay'ın çizgisi

---

## /istinaf-hakim:hukuk-esas-karar

---
name: hukuk-esas-karar
description: >
  İncelemeye alınan hukuk istinaf dosyasında HMK m. 353-360 çerçevesinde karar türü
  seçenek analizi yapar: duruşmasız kaldırma ve gönderme, esastan ret, düzelterek
  yeniden esas hakkında karar, eksikleri tamamlayarak karar, duruşmalı inceleme.
  Gerekçe (m. 359) ve hüküm iskeletini kurar; sonucu DAYATMAZ.
user-invocable: true
---

# İstinaf Esas İncelemesi ve Karar Türleri (Hukuk) — HMK m. 353-360

## Konum hatırlatması

İnceleme istinaf dilekçesinde belirtilen sebeplerle sınırlıdır; bölge adliye mahkemesi kamu düzenine aykırılık gördüğü takdirde bunu resen gözetir (HMK m. 355). Asistan hangi karar türünün verileceğini seçmez; her seçeneğin şartını, dosyadaki karşılığını ve sonucunu yan yana koyar. Karar ve takdir heyettedir. Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir. **Karar türünün seçimi için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

İncelemeye alınan hukuk istinaf dosyasında verilebilecek karar türlerinin şartlarını dosyadaki karşılıklarıyla yan yana koymak; heyetin seçeceği karar için gerekçe ve hüküm iskeletini hazırlamak.

## Girdi

- Ön inceleme sonucu (`/istinaf-hakim:hukuk-on-inceleme`)
- İlk derece kararının gerekçesi ve hüküm fıkrası
- İstinaf sebepleri (her başvuran için ayrı liste), cevaplar, katılma yoluyla başvuru
- Dosyadaki deliller; ilk derece mahkemesinde usulüne uygun gösterildiği hâlde incelenmeden reddedilen veya mücbir sebeple gösterilemeyen deliller (m. 357/3)

## Karar ağacı

1. **Kaldırma ve gönderme — duruşmasız, kesin (m. 353/1-a).** Şu hâllerden biri var mı: davaya bakması yasak hâkimin karar vermesi; haklı ret talebine rağmen reddedilen hâkimin davaya bakması; görev veya yetki hatası; diğer dava şartlarına aykırılık; usule aykırı olarak davanın veya karşı davanın açılmamış sayılması, birleştirme veya ayırma; uyuşmazlığın çözümünde etkili olabilecek ölçüde önemli delillerin toplanmaması veya değerlendirilmemesi ya da talebin önemli bir kısmı hakkında karar verilmemesi. Varsa dosya kararı veren mahkemeye, yargı çevresinde uygun görülecek başka bir yer mahkemesine veya görevli ve yetkili mahkemeye gönderilir. Bu kararlar hakkında temyiz yoluna başvurulamaz (m. 362/1-g).
2. **Esastan ret — duruşmasız (m. 353/1-b-1).** Karar usul ve esas yönünden hukuka uygun. Esastan ret kararında istinaf sebepleri özetlenip ret sebepleri açıklanarak kararın hukuka uygunluk gerekçesi gösterilmekle yetinilebilir (m. 359/3).
3. **Düzelterek yeniden esas hakkında karar — duruşmasız (m. 353/1-b-2).** Yargılamada eksiklik yok; kanunun olaya uygulanmasında hata var ve yeniden yargılamaya ihtiyaç yok ya da gerekçede hata var.
4. **Eksikleri duruşmasız tamamlama (m. 353/1-b-3).** Eksiklik duruşma yapılmadan tamamlanabilecek nitelikte; tamamlandıktan sonra esastan ret veya yeniden esas hakkında karar.
5. **Duruşmalı inceleme (m. 356).** Yukarıdakiler dışında inceleme duruşmalı yapılır; duruşma günü taraflara tebliğ edilir. Davetiyede, hazır bulunmazlarsa tahkikatın yokluklarında yapılarak karar verileceği ve başvurana, dairece belirlenen giderin iki haftadan az olmamak üzere verilecek kesin süre içinde avans olarak yatırılması gerektiği açıkça belirtilir (m. 358/1). Gider süresinde yatırılmazsa dosyanın mevcut durumuna göre karar verilir; öngörülen tahkikat yapılmadan karar verilemeyen hâllerde başvuru reddedilir (m. 358/3). Duruşma sonunda başvuru esastan reddedilir veya ilk derece hükmü kaldırılarak yeniden hüküm kurulur (m. 356/2).

## Yapılamayacak işlemler (m. 357)

İstinafta karşı dava açılamaz, davaya müdahale talebinde bulunulamaz, ıslah yapılamaz; m. 166/1 saklı kalmak üzere davaların birleştirilmesi istenemez; resen gözetilecekler dışında ilk derecede ileri sürülmeyen iddia ve savunmalar dinlenemez, yeni delile dayanılamaz; bölge adliye mahkemeleri için yetki sözleşmesi yapılamaz. İlk derecede usulüne uygun gösterildiği hâlde incelenmeden reddedilen veya mücbir sebeple gösterilemeyen deliller incelenebilir (m. 357/3). Her istinaf sebebi bu süzgeçten geçirilir.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **İstinaf sebepleri matrisi** (her başvuran için ayrı)

| # | Sebep | Başvuran | m. 357 süzgeci | İlk derece gerekçesindeki karşılığı | Dosyadaki delil | Kabul yönünde / ret yönünde değerlendirme |
|---|---|---|---|---|---|---|

2. **Kamu düzeni resen denetimi** (m. 355): görev, dava şartları, yasak hâkim vb.
3. **Karar türü seçenek tablosu:** her seçenek için şart, dosyadaki karşılık, sonuç ve kanun yolu (m. 362'den çekilerek).
4. **Gerekçe iskeleti (m. 359/1):** a) daire, başkan, üyeler ve zabıt kâtibi [DOLDUR]; b) taraflar ve ilk derecede müdahil olarak katılanlar [DOLDUR]; c) iddia ve savunma özeti; ç) ilk derece kararının özeti; d) istinaf sebepleri; e) uyuşmazlık konusu olan ve olmayan hususlar, delillerin tartışılması, ret ve üstün tutma sebepleri, sabit vakıalar, çıkarılan sonuç ve hukuki sebep; f) hüküm sonucu, varsa kanun yolu ve süresi; g-ğ) tarih ve imzalar, gerekçeli kararın yazıldığı tarih.
5. **Hüküm iskeleti (m. 359/2):** her talep hakkında sıra numaralı, gerekçe tekrar edilmeden, şüphe ve tereddüt uyandırmayacak açıklıkta; sonuç **boş** veya seçenekli.
6. **Tebliğ notu (m. 359/4):** temyizi kabil olmayan kararlar ilk derece mahkemesince, temyizi kabil olanlar bölge adliye mahkemesince resen tebliğe çıkarılır.

**Risk skalası:**
- 🔴 m. 353/1-a hâli varken esasa girilmesi; istinaf sebepleri dışında ve kamu düzeniyle ilgisiz bir gerekçeyle karar; m. 357'ye aykırı yeni delile dayanma.
- 🟠 Esaslı bir istinaf sebebinin karşılanmaması; duruşmalı işte gider avansı ihtarının eksik yapılması.
- 🟡 Hüküm fıkrasında sıra numarası veya açıklık eksiği; kanun yolu bilgisinin güncel metinden teyit edilmemesi.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 166, 353, 355, 356, 357, 358, 359, 360, 362 (dipnotlardaki Anayasa Mahkemesi iptal kararları ve 7589 s.K. ile eklenen m. 362/3 dâhil), Ek m. 1 — bu sohbette çekildi mi, eşleşti mi. Bu bölümde hüküm bulunmayan hâllerde ilk derece yargılama usulü uygulanır (m. 360).
- Temyiz sınırı ve temyiz edilebilirlik: metindeki tutar Ek m. 1 ile güncellenir; güncel tutar çekilemediyse UYARI satırı.
- Emsal: yalnız `/yargi-arastirma:ictihat-dogrulama`dan geçen künyeler.
- Süre hesapları hatırlatmadır; son günü hâkim/kalem teyit eder. Tebliğ tarihi gibi bilinmeyen bir olguda en erken olası gün esas alınır ve bu açıkça uyarı olarak yazılır.
- ⚠️ "Karar türü ve sonuç heyet takdirindedir."

## Sıradaki adımlar

- `/yargi-arastirma:karsi-gorus-taramasi` — sebeplerle ilgili aykırı içtihat
- `/yargi-arastirma:aym-aihm-standart-kontrolu` — gerekçeli karar ve çelişmeli yargılama kontrolü
- `/istinaf-kalem:karar-sonrasi-islemler` — tebliğ ve dosyanın iadesi

---

## /istinaf-hakim:ceza-istinaf-inceleme

---
name: ceza-istinaf-inceleme
description: >
  Bölge adliye mahkemesi ceza dairesinde istinaf incelemesini CMK m. 272-284
  çerçevesinde yapılandırır: istinafa tabi hüküm, süre ve başvuru hakkı, dosya üzerinde
  ön inceleme (m. 279), esas inceleme ve karar türleri (m. 280), duruşma, aleyhe
  değiştirme yasağı, diğer sanıklara uygulanma. Mahkûmiyet, beraat veya cezayı DAYATMAZ.
user-invocable: true
---

# Ceza İstinaf İncelemesi — CMK m. 272-284

## Konum hatırlatması

Masumiyet karinesi (AY m. 38) istinafta da geçerlidir. Sanık, katılan ve katılma isteği karara bağlanmamış, reddedilmiş veya katılan sıfatını alabilecek surette suçtan zarar görmüş olanların dilekçe veya beyanında nedenlerin gösterilmemesi incelemeye engel olmaz (CMK m. 273/4); Cumhuriyet savcısı ise başvuru nedenlerini gerekçeleriyle açıkça gösterir (m. 273/5). Karar türü, suç vasfı ve ceza heyet takdiridir; **tutukluluğa ilişkin her karar için hâkim/heyet takdiri ve onayı şarttır.** Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir.

## Amaç

Ceza istinaf dosyasında ön inceleme ve esas inceleme adımlarını sıraya koymak; karar türlerinin şartlarını ve aleyhe değiştirme yasağı gibi sınırları heyetin önüne getirmek.

## Girdi

- İlk derece hükmü (gerekçeli), hüküm türü, verilen ceza veya tedbir, sanık sayısı, tutukluluk durumu
- Gerekçeli hükmün her ilgiliye tebliğ tarihi; istinaf dilekçesi veya zabıt kâtibine beyan tutanağı; tutuklu için CMK m. 263 işlemi
- Başvuranların sıfatı (sanık, müdafi, katılan, Cumhuriyet savcısı, yasal temsilci, eş)
- İlk derece mahkemesince verilmiş ret kararı (m. 276) varsa tebliği ve buna karşı başvuru

## Ön inceleme — dosya üzerinde (m. 279)

1. **Yetki.** Bölge adliye mahkemesi yetkili değilse dosya yetkili bölge adliye mahkemesine gönderilir (m. 279/1-a).
2. **Süre.** İki hafta, hükmün gerekçesiyle birlikte tebliğ edildiği tarihten (m. 273/1); ağır ceza mahkemesi Cumhuriyet savcısının yargı çevresindeki asliye mahkemesi hükümlerine karşı başvurusunda kararın başsavcılığa geliş tarihinden (m. 273/3). Tutuklu şüpheli veya sanığın zabıt kâtibine ya da kurum müdürüne beyanında, m. 263/2 işlemi yapıldığında süre kesilmiş sayılır (m. 263/4). Yokluğunda verilen hükümde eski hâle getirme süresi içinde istinaf süresi de işler (m. 274).
3. **İstinafa tabi hüküm.** İlk derece hükümlerine karşı istinaf yolu açıktır; on beş yıl ve daha fazla hapis cezasına ilişkin hükümler resen incelenir (m. 272/1). İstinaf edilemeyenler (m. 272/3): hapisten çevrilenler hariç sonuç olarak belirlenen on beş bin Türk lirası dâhil adli para cezasına mahkûmiyet; üst sınırı beş yüz günü geçmeyen adli para cezasını gerektiren suçlardan beraat; kanunlarda kesin olduğu yazılı hükümler. Hükümden önce verilip hükme esas teşkil eden veya başka kanun yolu öngörülmemiş kararlar hükümle birlikte incelenir (m. 272/2).
4. **Başvuru hakkı.** CMK m. 260, 262.
5. **Sonuç:** yetkisizlik → gönderme; süre, incelenemez karar veya başvuru hakkının yokluğu → istinaf başvurusunun reddi. Bu kararlar itiraza tabidir (m. 279/1).
6. **Tebligat eksikliği.** Daire, varsa tebligat eksikliklerinin giderilmesini sağlar (m. 278).

## Esas inceleme ve karar türleri (m. 280)

| Seçenek | Şart (metin) | Dayanak |
|---|---|---|
| Esastan ret | Usul veya esasa ilişkin hukuka aykırılık yok, delillerde veya işlemlerde eksiklik yok, ispat değerlendirmesi yerinde | m. 280/1-a |
| Düzelterek esastan ret | m. 303/1'in (a), (c), (d), (e), (f), (g), (h) bentlerindeki ihlaller | m. 280/1-a |
| Düzelterek esastan ret | Cumhuriyet savcısının başvuru nedenine uygun olarak kanunda yazılı cezanın en alt derecesinin uygulanmasının uygun görülmesi | m. 280/1-b |
| Düzelterek esastan ret | Başka araştırma gerekmeden cezayı kaldıran veya indiren şahsi sebepler ya da şahsi cezasızlık sebepleri | m. 280/1-c |
| Düzelterek esastan ret | Daha fazla araştırma gerekmeden davanın reddi veya güvenlik tedbirine ilişkin hatalı kararın düzeltilmesi | m. 280/1-d |
| Bozma ve gönderme | m. 289'daki hukuka kesin aykırılık hâlleri | m. 280/1-e |
| Bozma ve gönderme | Soruşturma veya kovuşturma şartının gerçekleşmemesi; önödeme veya uzlaştırma usulünün uygulanmaması; ilk derecede görülen bir davayla birlikte yürütme zorunluluğu | m. 280/1-f |
| Yeniden görülme | Diğer hâllerde gerekli tedbirler alınarak davanın yeniden görülmesi ve duruşma hazırlığı | m. 280/1-g |

- **Duruşma:** hazırlık (m. 281); duruşmaya özgü istisnalar (m. 282: görevlendirilen üyenin inceleme raporunun ve ilk derece gerekçeli hükmünün anlatılması, ilk derecede dinlenen tanık ifadeleri, keşif tutanakları ve bilirkişi raporunun anlatılması, gerekli görülen tanık ve bilirkişilerin çağrılması; sanık, müdafi, katılan ve vekilinin davetiyeye rağmen gelmemesi hâlinde yokluklarında bitirme — ancak verilecek ceza ilk derece cezasından ağırsa sanığın her hâlde dinlenmesi). Duruşma sonunda istinaf başvurusu esastan reddedilir veya ilk derece hükmü kaldırılarak yeniden hüküm kurulur (m. 280/2).
- **Aleyhe değiştirme yasağı:** istinaf yoluna yalnız sanık lehine başvurulmuşsa yeniden verilen hüküm önceki cezadan daha ağır olamaz (m. 283).
- **Diğer sanıklara uygulanma:** sanık lehine kararlar, uygulanma olanağı varsa istinaf isteminde bulunmamış diğer sanıklara da uygulanır (m. 280/3).
- **Direnme yasağı:** bölge adliye mahkemesi karar ve hükümlerine direnilemez; itiraz ve temyize ilişkin hükümler saklıdır (m. 284).
- **Hukuka kesin aykırılık kontrolü (m. 289):** mahkemenin teşekkülü, yasaklı veya reddedilmiş hâkim, görev veya yetki, kanunen hazır bulunması gerekenlerin yokluğu, açıklık kuralı, m. 230'a göre gerekçesiz hüküm, savunma hakkının sınırlandırılması, hukuka aykırı delile dayanma — her biri ayrı işaretlenir.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Ön inceleme tablosu** (m. 279 kalemleri, her başvuran için ayrı; süre: tebliğ tarihi → son gün, "en erken gün" işaretli).
2. **m. 289 kontrol listesi** (✓ / ✗ / bilgi yok).
3. **Başvuru nedenleri matrisi:** neden — başvuran — ilk derece gerekçesindeki karşılığı — delil — değerlendirme (sanık lehine ve aleyhine iki yön).
4. **Karar türü seçenekleri** (yukarıdaki tablo üzerinden; sonuç boş); m. 283 ve m. 280/3 notu.
5. **Tutukluluk notu:** dosya bölge adliye mahkemesindeyken salıverilme istemi hakkında karar dosya üzerinde yapılacak incelemeyle verilir, re'sen de verilebilir (m. 104/3) → `/ceza-hakim:tutukluluk-incelemesi`. Adli tatilde bölge adliye mahkemesi yalnız tutuklu hükümlere ilişkin veya Meşhud Suçların Muhakeme Usulü Kanunu gereğince görülen işlerin incelemesini yapar (m. 331/3).
6. **Kanun yolu:** kararın temyiz edilebilirliği m. 286'dan çekilerek; süre iki hafta, hükmün gerekçesiyle birlikte tebliğinden (m. 291/1); hüküm fıkrasında merci ve süre tereddüde yer vermeyecek açıklıkta (m. 232/6).

**Risk skalası:**
- 🔴 m. 289 hâlinin gözden kaçması; yalnız sanık lehine başvuruda daha ağır ceza (m. 283); ilk derece cezasından ağır ceza verilecekken sanığın dinlenmemesi (m. 282/1-f).
- 🟠 Süre hesabının tefhimden yapılması (7499 s.K. sonrası tebliğ esastır); m. 280/3 değerlendirmesinin yapılmaması.
- 🟡 Tebligat eksikliğinin dairece giderilmemesi (m. 278).
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: AY m. 38; CMK m. 104, 230, 232, 260, 262, 263, 272, 273, 274, 276, 278, 279, 280, 281, 282, 283, 284, 286, 289, 291, 303, 331 — bu sohbette çekildi mi, eşleşti mi. m. 295 mülgadır; atıf yapılmaz.
- Suç tipi ve ceza hükümleri (TCK) çıktıya girecekse ayrıca çekilir.
- ⚠️ "Mahkûmiyet, beraat, ceza ve tutukluluk kararları heyet takdirindedir; hâkim/heyet onayı şart."

## Sıradaki adımlar

- `/ceza-hakim:gerekce-denetimi` — ilk derece gerekçesinin m. 230 denetimi
- `/yargi-arastirma:emsal-tarama` — ilgili Yargıtay ceza dairesi ve CGK çizgisi
- `/istinaf-kalem:karar-sonrasi-islemler`

---

## /istinaf-hakim:idari-istinaf

---
name: idari-istinaf
description: >
  Bölge idare mahkemesi idari ve vergi dava dairelerinde İYUK m. 45 incelemesini
  yapılandırır: istinafa tabi karar ve parasal kesinlik, süre, dilekçe ve harç
  (temyizin şekil ve usulleri, m. 48 kıyasen), ret türleri (m. 45/3), kaldırma ve
  yeniden esas hakkında karar (m. 45/4), kaldırıp geri gönderme hâlleri (m. 45/5),
  temyiz edilebilirlik (m. 46). Sonucu DAYATMAZ.
user-invocable: true
---

# İdari İstinaf — İYUK m. 45 (Bölge İdare Mahkemesi)

## Konum hatırlatması

İdari yargı yetkisi hukuka uygunluk denetimiyle sınırlıdır; yerindelik denetimi yapılamaz, idari eylem ve işlem niteliğinde karar verilemez (İYUK m. 2/2). Bölge idare mahkemesi istinaf incelemesini kendiliğinden yapar ve gereken bilgi ve belgeyi ara kararıyla ister (m. 20/1); istinafta bu ara kararlarını daire başkanı veya dosyanın havale edildiği üye de verebilir (m. 20/6). Karar türü ve sonuç heyet takdiridir. 7589 s.K. ile İYUK m. 45 ve 46'da 16.07.2026 tarihli değişiklikler vardır; metin her dosyada güncel hâliyle çekilir. Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir. **Karar türünün seçimi için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

Bölge idare mahkemesi dairesinde istinaf incelemesini kesinlik, süre, dilekçe ve harç kontrolüyle başlatmak; verilebilecek karar türlerini şartları ve sonuçlarıyla yan yana göstermek.

## Girdi

- İlk derece kararı: mahkeme (idare / vergi), tek hâkim mi heyet mi, dava türü (iptal / tam yargı / vergi), uyuşmazlık miktarı, davanın açıldığı tarih
- Kararın tebliğ tarihleri; istinaf dilekçesinin tarihi ve verildiği yer; harç
- Cevap dilekçesi ve cevapla birlikte yapılan başvuru; yürütmenin durdurulması istemi
- Dava özel usule tabi mi (İYUK m. 20/A ivedi yargılama, m. 20/B merkezî ve ortak sınavlar)

## Ön kontrol

1. **İstinaf yolu açık mı.**
   - İvedi yargılama usulüne tabi davalarda istinaf yoluna başvurulamaz (m. 45/8); nihai kararlara karşı tebliğden itibaren on beş gün içinde temyiz (m. 20/A/2-g). Merkezî ve ortak sınav davalarında temyiz süresi beş gündür (m. 20/B/1-f).
   - Parasal kesinlik: konusu m. 45/1'deki tutarı geçmeyen vergi davaları, tam yargı davaları ve iptal davaları hakkında verilen kararlar kesindir; tutar Ek m. 1 uyarınca her yıl güncellenir ve davanın açıldığı tarihteki sınır esas alınır (Ek m. 1/2). Güncel tutar çekilir ya da UYARI satırı yazılır.
2. **Süre.** Kararın tebliğinden itibaren otuz gün (m. 45/1). Süreler tebliği izleyen günden işler; son gün tatile rastlarsa izleyen çalışma günü sonuna uzar; süre sonu çalışmaya ara verme zamanına rastlarsa ara vermenin sona erdiği günü izleyen tarihten itibaren yedi gün uzamış sayılır (m. 8).
3. **Şekil ve usul.** İstinaf temyizin şekil ve usullerine tabidir; dosyalar dilekçedeki hitap ve istekle bağlı kalınmaksızın bölge idare mahkemesine gönderilir (m. 45/2). m. 48'in kıyasen uygulanması: dilekçenin m. 3 esaslarına uygunluğu ve on beş günlük tamamlama (m. 48/2), harç ve giderler için yedi günlük süre (m. 48/6), dosya geldiğinde bu hâllerde verilecek kararlar (m. 48/7). m. 45/2'nin birinci cümlesi ve m. 48/7'deki "ve 6 ncı" ibaresi hakkında, istinafın kanuni süre geçtikten sonra yapılması hâli yönünden Anayasa Mahkemesi iptal kararı bulunduğu metnin dipnotunda yazılıdır (20.07.2022, E.2022/48, K.2022/93); süre aşımında hangi merciin karar vereceği bu notla birlikte güncel metinden belirlenir.
4. **Cevapla başvuru.** Cevap veren, kararı süresinde kanun yoluna götürmemiş olsa bile cevap dilekçesinde başvuruda bulunabilir (m. 48/3, m. 45/2 yoluyla).
5. **Yürütmenin durdurulması.** İlk derece YD kararlarına itiraz ayrı yoldur: idare ve vergi mahkemeleri ile tek hâkim kararlarına karşı bölge idare mahkemesine, tebliği izleyen günden itibaren yedi gün içinde, bir defaya mahsus; itiraz mercii dosyanın gelişinden itibaren yedi gün içinde karar verir; itiraz üzerine verilen kararlar kesindir (m. 27/7).

## Karar türleri

| Seçenek | Şart (metin) | Dayanak |
|---|---|---|
| İstinaf başvurusunun reddi | Karar hukuka uygun | m. 45/3-a |
| Gerekçe değiştirilerek ret | Sonuç hukuka uygun, gösterilen gerekçe yanlış veya eksik | m. 45/3-b |
| Düzeltilerek ret | Karardaki maddi yanlışlıkların düzeltilmesi mümkün | m. 45/3-c |
| Kabul, kaldırma ve yeniden esas hakkında karar | İlk derece kararı hukuka uygun değil; gerektiğinde kararı veren veya başka yer idare ya da vergi mahkemesi istinabe olunur | m. 45/4 |
| Kabul, kaldırma ve kararı veren mahkemeye gönderme (kesin) | Yalnız sayılı hâller: ilk inceleme üzerine verilen kararlar ile usule ilişkin diğer nihai kararlara karşı başvurunun haklı bulunması; görevsiz veya yetkisiz mahkeme ya da reddedilmiş veya yasaklanmış hâkim; dilekçenin reddi gerekirken dava hakkında karar verilmesi; eksik veya yanlış hasımla tekemmül; talep hakkında karar verilmemesi veya eksik hükümle karar; gerektiği hâlde keşif veya bilirkişi incelemesi yaptırılmaması; gerektiği hâlde duruşma yapılmaması. Son iki hâlde daire eksikliği kendisi gidererek karar verebilir. Bu hâller dışında kaldırıp geri gönderme yapılamaz. | m. 45/5 |

- İstinafa konu kararı veren veya karara katılan hâkim aynı davanın istinaf incelemesinde bulunamaz (m. 45/7).
- **Temyiz:** m. 46/1'de sayılan davalar ve m. 46/2 (7589 s.K.) uyarınca, birinci fıkra kapsamında olmayan davalarda kaldırma üzerine yeniden verilen kararlar — istisnalarıyla. Temyize açık olmayan kararlar kesindir; dosyayla birlikte kararı veren ilk derece mahkemesine gönderilir ve bu mahkemece yedi gün içinde tebliğe çıkarılır (m. 45/6). m. 45/6'nın birinci cümlesi hakkında, istinaf başvurusunun kısmen veya tümden kabulü hâli yönünden Anayasa Mahkemesi iptal kararı dipnotta yazılıdır (27.03.2025, E.2024/189, K.2025/83).
- **Kesin kararlar arasında aykırılık:** bölge idare mahkemesi daireleri veya farklı bölge idare mahkemeleri arasında aykırılık hâlinde başkanlar kurulu yolu (2576 s.K. m. 3/C).

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Ön kontrol tablosu:** istinaf yolu / kesinlik / süre / dilekçe / harç / cevap / YD.
2. **Hukuka uygunluk denetimi:** iptal davasında işlemin yetki, şekil, sebep, konu ve maksat unsurları (m. 2/1-a); vergi davasında tarhiyat ve ceza unsurları; her unsur için ilk derece değerlendirmesi ↔ istinaf sebebi ↔ dosya.
3. **Karar türü seçenekleri** (tablo üzerinden; m. 45/5 hâllerinin sınırlı sayısı vurgulanır).
4. **Gerekçe ve hüküm iskeleti** (sonuç boş; iptal ve ret yönleri ayrı).
5. **Kanun yolu notu:** m. 46'dan çekilerek temyiz edilebilirlik ve süre (tebliğden itibaren otuz gün).

**Risk skalası:**
- 🔴 m. 45/5 dışındaki bir gerekçeyle kaldırıp geri gönderme; ivedi yargılama davasında istinaf incelemesine girilmesi; yerindelik denetimi niteliğinde gerekçe.
- 🟠 Parasal sınırın dava tarihine göre değil karar tarihine göre uygulanması; süre hesabında m. 8 uzamasının atlanması.
- 🟡 Temyiz edilebilirlik notunun 7589 s.K. değişikliğine göre güncellenmemesi.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: İYUK m. 2, 3, 8, 20, 20/A, 20/B, 27, 45, 46, 48, Ek m. 1; 2576 s.K. m. 3/A, 3/C — bu sohbette çekildi mi, eşleşti mi. m. 47 mülgadır; atıf yapılmaz.
- Danıştay içtihadı: `tr_ictihat_ara` (`DANISTAYKARAR`, `IDDK`, `VDDK` ve ilgili daire); bölge idare mahkemesi kararları için bu araçta ayrı mahkeme türü yoktur → `UYARI: veri çekilemedi, teyidiniz gerekli: https://emsal.uyap.gov.tr/`.
- Süre hesapları hatırlatmadır; son günü hâkim/kalem teyit eder. Tebliğ tarihi gibi bilinmeyen bir olguda en erken olası gün esas alınır ve bu açıkça uyarı olarak yazılır.
- ⚠️ "Karar türü ve sonuç heyet takdirindedir; yerindelik denetimi yapılmaz."

## Sıradaki adımlar

- `/idari-hakim:ara-karar-bilgi-belge` — istinafta eksik bilgi ve belge
- `/vergi-hakim:vergi-ceza-degerlendirme` — vergi dava dairesinde ceza denetimi
- `/istinaf-kalem:karar-sonrasi-islemler`

---

> v1.2.0 — `istinaf-hakim` 4 skill. Kalıp: `hukuk-hakim__skills.md`. Detay: `hmk-rehberi.md`, `cmk-rehberi.md`, `iyuk-rehberi.md`.
