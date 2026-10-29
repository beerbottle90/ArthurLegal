# karar-yayim — Skill Referans Kitapçığı

> Alan: Karar metninin paylaşım ve yayım öncesi hazırlığı (dal fark etmez) · Rol: **Hâkim + kalem** · Dayanak: AY m. 20 ve 141, KVKK 6698 ve dosyaya özgü gizlilik hükümleri
> Toplam skill: 3
> Kullanım: `/karar-yayim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: Bu skill'ler hükmü değiştirmez; kararın dışa açılacak kopyasını, sade özetini ve emsal kaydını hazırlar. Asıl karar UYAP'taki hâliyle kalır; asistan UYAP'a bağlanmaz, kayıt eklemez. Yayım ve paylaşım kararı ile yöntemi mahkemenin ve yetkili birimin kurallarına tabidir. Her çıktı **TASLAK — hâkim/heyet onayı şart**.

## İçindekiler

- /karar-yayim:anonimlestirme — yayım veya paylaşım öncesi kişisel veri karartma kontrol listesi (özel nitelikli veri, çocuk, mağdur, tanık)
- /karar-yayim:sade-dil-ozeti — taraflar ve vatandaş için anlaşılır özet; "bu özet karar değildir" ibaresiyle
- /karar-yayim:karar-kunye-ozeti — emsal kaydı için künye kartı: uygulanan normlar, ilke cümlesi, anahtar kavramlar

---

## /karar-yayim:anonimlestirme

---
name: anonimlestirme
description: >
  Karar metni yayım, emsal arşivi, eğitim veya akademik paylaşım ya da taraf dışı bir
  kuruma gönderim için dışa açılmadan önce kişisel veri karartma kontrolünü yapar:
  doğrudan ve dolaylı tanımlayıcılar, özel nitelikli veriler, çocuk, mağdur, kimliği
  saklı tanık, gizlilik kararı olan kişiler. Karartma önerisi üretir; hukuki anlamı
  bozan karartmayı işaretler.
user-invocable: true
---

# Anonimleştirme — Yayım Öncesi Karartma Kontrolü

## Konum hatırlatması

Anonim hâle getirme, kişisel verilerin başka verilerle eşleştirilerek dahi hiçbir surette kimliği belirli veya belirlenebilir bir gerçek kişiyle ilişkilendirilemeyecek hâle getirilmesidir (KVKK m. 3/1-b). Etiketle değiştirme (takma adlandırma, Arthur Mask dâhil) tek başına bu sonucu garanti etmez; dolaylı tanımlayıcılar ayrıca denetlenir. Yayım kararı, kapsamı ve kurum kuralları kullanıcıya ve yetkili birime aittir. Asistan çıktısında gerçek kişisel veri yeniden yazılmaz. Asistan UYAP'a bağlanmaz, kayıt eklemez; karar metni kullanıcıdan gelir.

## Amaç

Karar metni dışa açılmadan önce kişisel verileri ve kişiyi dolaylı olarak tanıtabilecek ayrıntıları tespit etmek; karartma önerisini hukuki anlamı bozmayacak biçimde hazırlamak.

## Dayanak (bu sohbette çekilir)

- **AY m. 20** — herkes kendisiyle ilgili kişisel verilerin korunmasını isteme hakkına sahiptir.
- **AY m. 141** — duruşmaların açıklığı ve istisnası; küçüklerin yargılanması hakkında kanunla özel hükümler konulur.
- **KVKK m. 3/1-b** (anonim hâle getirme), **m. 4/2** (işlendikleri amaçla bağlantılı, sınırlı ve ölçülü olma), **m. 6/1** (özel nitelikli kişisel veriler: ırk, etnik köken, siyasi düşünce, felsefi inanç, din, mezhep veya diğer inançlar, kılık ve kıyafet, dernek, vakıf ya da sendika üyeliği, sağlık, cinsel hayat, ceza mahkûmiyeti ve güvenlik tedbirleri, biyometrik ve genetik veriler), **m. 28/1-d** (kişisel verilerin soruşturma, kovuşturma, yargılama veya infaz işlemlerine ilişkin olarak yargı makamları veya infaz mercileri tarafından işlenmesi Kanun kapsamı dışındadır). Kararın yayım veya paylaşım amacıyla dışa açılmasının bu istisnaya girip girmediği ayrı değerlendirme konusudur; tereddütte ölçülülük ve karartma esas alınır.
- **CMK m. 185** — sanık on sekiz yaşını doldurmamışsa duruşma kapalı yapılır, hüküm de kapalı duruşmada açıklanır.
- **CMK m. 236/7** — özel ortamda alınan mağdur çocuk ve mağdur beyan ve görüntü kayıtları dava dosyasında saklanır, kimseye verilmez, gizliliği için tedbir alınır.
- **CMK m. 58/2** — kimliğinin ortaya çıkması ağır tehlike oluşturacak tanığın kimliği saklı tutulur; bu hüküm örgüt faaliyeti çerçevesinde işlenen suçlarda uygulanır (m. 58/5).
- **6284 s.K. m. 8/6** — gerekli hâllerde korunan kişi ve diğer aile bireylerinin kimlik bilgileri, kimliğini ortaya çıkarabilecek bilgileri ve adresleri tüm resmî kayıtlarda gizli tutulur.
- **HMK m. 28/4** — gizli yargılamada hazır bulunanlara, edindikleri bilgileri açıklamamaları ihtar edilir.
- **5187 s. Basın K. m. 21** — süreli yayınlarda on sekiz yaşından küçük suç faili veya mağdurlarının ve maddede sayılan diğer kişilerin kimliklerini açıklayacak ya da tanınmalarına yol açacak yayın cezai yaptırıma bağlanmıştır (paylaşılan kopyanın basına ulaşabileceği göz önünde tutulur).
- Yargı kararlarının yayımına ilişkin kurum kuralları (HSK, Adalet Bakanlığı, emsal karar sistemi) bu sohbette çekilmediyse: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## Girdi

- Karar metni (tercihen Arthur Mask ile maskelenmiş; `{{KİŞİ-01}}` gibi etiketler harfi harfine korunur, gerçek değer tahmin edilmez)
- Amaç: emsal arşivi / eğitim veya akademik paylaşım / basın bilgilendirmesi / taraf dışı kuruma gönderim
- Özel durum bayrakları: çocuk (sanık, mağdur, tanık), cinsel suç, 6284 gizlilik kararı, kapalı duruşma, kimliği saklı tanık, sağlık veya ceza mahkûmiyeti bilgisi, gizlilik kararı kapsamındaki belgeler

## Kontrol listesi

**A. Doğrudan tanımlayıcılar** — ad-soyad (taraf, sanık, mağdur, tanık, katılan, üçüncü kişi), T.C. kimlik no, vergi no, pasaport no, adres, telefon, e-posta, IBAN ve hesap no, plaka, tapu ada/parsel ve bağımsız bölüm, başka dosyaların numaraları, işyeri ve okul adı, imza ve paraf.

**B. Dolaylı tanımlayıcılar** — küçük yerleşim yeri + meslek + yaş; akrabalık bağı; benzersiz olay ayrıntısı; tarih + yer + unvan birleşimi; kamuoyunda bilinen olay adı. Test: dosyayı bilmeyen biri metin ve genel bilgiyle kişiyi tanıyabilir mi?

**C. Özel nitelikli veriler (KVKK m. 6/1)** — gerekçe için zorunlu olmayan ayrıntı çıkarılır veya genelleştirilir ("sağlık raporu mevcuttur", "adli sicil kaydı bulunmaktadır").

**D. Çocuk** — ad, okul, veli, adres, fiziksel tarif; CMK m. 185 kapsamındaki yargılamalarda duruşma içeriğinin ayrıntısı; mağdur çocuk beyan içeriği (CMK m. 236/7 kayıtları) yalnız hükme etkisi kadar ve ayrıntısız.

**E. Mağdur ve korunan kişi** — cinsel suç mağdurunun kimliği ve tanınmasına yol açacak ayrıntılar; 6284 m. 8/6 gizlilik kararı varsa kimlik ve adres hiçbir biçimde yer almaz.

**F. Tanık** — kimliği saklı tanığın (CMK m. 58/2) kimliğini ortaya çıkarabilecek her ayrıntı; diğer tanıklarda ad yerine rol etiketi.

**G. Belge içi ve üst veri** — dosya adı, belge özellikleri, başlık ve altbilgi, QR kod, barkod, ekler.

**H. Meslek mensupları** — hâkim, savcı, zabıt kâtibi, avukat, bilirkişi adları: kurum kuralına göre (kural çekilemediyse varsayılan: karart ve UYARI satırı).

## Yöntem

1. **Rol etiketi, tutarlı:** Davacı, Davalı, Sanık-1, Mağdur, Tanık-2, Bilirkişi. Aynı kişi her yerde aynı etiketle.
2. **Hukuki anlamı koru:** süre, zamanaşımı veya yaş hesabına etkili tarihler korunur ya da gün/ay düzeyinde genelleştirilir ve bu işaretlenir; tutarlar kişiyi tanıtmıyorsa korunur. Karartma sonucu gerekçe anlaşılmaz hâle geliyorsa 🟠 ile bildirilir.
3. **Karar künyesi:** mahkeme, E./K. ve tarihin korunup korunmayacağı amaca ve kurum kuralına bağlıdır; kural teyit edilmeden varsayım yapılmaz.
4. **İkinci geçiş:** karartılmış metin baştan sona yeniden okunur; dolaylı tanımlayıcı testi uygulanır.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Karartma tablosu**

| # | Kategori (A-H) | Metindeki yer (paragraf) | Önerilen işlem (çıkar / etiketle / genelleştir / koru) | Dayanak | Risk |
|---|---|---|---|---|---|

2. **Etiket sözlüğü:** yalnız etiketler ve rolleri; gerçek değerlerle eşleme kullanıcıda kalır, çıktıya yazılmaz.
3. **Karartılmış metin taslağı** (istenirse) — gerçek veri yerine etiket.
4. **Kalan risk notu:** dolaylı tanınma ihtimali, amaç için gereksiz kalan bilgi.

**Risk skalası:**
- 🔴 Çocuk, cinsel suç mağduru, 6284 gizlilik kararı kapsamındaki kişi veya kimliği saklı tanığın kimliği ya da adresi metinde; özel nitelikli verinin gereksiz ayrıntıyla yer alması.
- 🟠 Dolaylı tanımlayıcı birleşimi kişiyi tanıtıyor; karartma gerekçeyi anlaşılmaz kılıyor.
- 🟡 Etiket tutarsızlığı; üst veri temizlenmemiş.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: AY m. 20, 141; KVKK m. 3, 4, 6, 28; CMK m. 58, 185, 236; 6284 s.K. m. 8; HMK m. 28; 5187 s.K. m. 21 — bu sohbette çekildi mi, eşleşti mi.
- Kurum kuralları çekilemediyse UYARI satırı.
- Maskeleme hatırlatması: dosya belgeleri paylaşılmadan önce Arthur Mask ile bilgisayarda maskelenebilir (yalnız Claude Desktop, Windows); takma adlandırma anonim hâle getirme değildir.
- ⚠️ "Yayım ve paylaşım kararı ile karartmanın son hâli hâkim/heyet onayına tabidir."

## Sıradaki adımlar

- `/karar-yayim:sade-dil-ozeti` — karartılmış metinden özet
- `/karar-yayim:karar-kunye-ozeti` — emsal kaydı
- Paylaşım amacına göre yetkili birime sunum

---

## /karar-yayim:sade-dil-ozeti

---
name: sade-dil-ozeti
description: >
  Kararın taraflar ve vatandaş için anlaşılır bir özetini hazırlar: dava neyle
  ilgiliydi, mahkeme ne karar verdi, neden, bundan sonra ne olacak. Hüküm fıkrasına
  birebir sadıktır; yorum ve tavsiye eklemez, hukuki sonucu değiştirmez; üstte ve
  altta "bu özet karar değildir" ibaresi bulunur.
user-invocable: true
---

# Sade Dil Özeti — "Bu Özet Karar Değildir"

## Konum hatırlatması

Özet kararın yerine geçmez ve kararı yorumlamaz. Kazanan-kaybeden dili kullanılmaz; iki tarafın iddiası eşit uzunluk ve tonda aktarılır. Kanun yolu bilgisi yalnız hüküm fıkrasından alınır. Özet de karartma kurallarına tabidir (`/karar-yayim:anonimlestirme`). Asistan UYAP'a bağlanmaz, kayıt eklemez; karar metni kullanıcıdan gelir.

## Amaç

Kararı taraflar ve vatandaş için anlaşılır bir dille özetlemek: dava neyle ilgiliydi, mahkeme ne karar verdi, neden ve bundan sonra ne olacak.

## Girdi

- Karar metni (gerekçeli), tercihen karartılmış
- Hedef okuyucu: taraf / genel kamu / basın bilgilendirmesi
- Kesinleşme durumu (kesinleşti / kanun yolunda / bilinmiyor)

## Kurallar

1. **Hüküm fıkrasına sadakat.** Hüküm kalemleri sırasıyla ve anlamı değiştirilmeden aktarılır; tutar, süre ve oranlar hükümdeki gibi yazılır, yuvarlanmaz. Hüküm sonucu sıra numaralı ve açık yazıldığından (HMK m. 297/2, 359/2; CMK m. 232/6) her özet cümlesi bir hüküm kalemine bağlanır.
2. **Yorum yok.** Kararın söylemediği sonuç, tahmin, tavsiye ("temyiz etmelisiniz") yazılmaz. Kalıp: "Mahkeme … karar verdi."
3. **Kanun yolu.** Hükümdeki kanun yolu, mercii, süre ve sürenin başlangıcı aynen sade dile çevrilir; hükümde yoksa özete eklenmez, eksiklik İnceleyen notuna yazılır.
4. **Terimler.** İlk geçtiği yerde tek cümlelik açıklama: istinaf (ilk derece kararının bölge adliye veya bölge idare mahkemesince incelenmesi için başvuru yolu), temyiz, tebliğ, kesinleşme, yargılama gideri, vekâlet ücreti.
5. **Kısa ve düz.** Cümle başına bir bilgi; eskimiş hukuk kalıpları yerine günlük dil ("müddeabbih" değil "dava konusu").
6. **Zorunlu ibare**, üstte ve altta: "Bu özet karar değildir ve hukuki sonuç doğurmaz. Bağlayıcı olan, mahkemenin [tarih] tarihli ve [E./K.] sayılı kararının metnidir; özet ile karar arasında fark varsa karar metni esastır."

## Çıktı yapısı

Üst başlık (iç taslak): `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

```
KARAR ÖZETİ (SADE DİL) — BU ÖZET KARAR DEĞİLDİR
[Zorunlu ibare]

1. Dava neyle ilgiliydi?                [2-3 cümle, tarafsız]
2. Taraflar ne istedi, ne savundu?      [her taraf için eşit uzunlukta 1-2 cümle]
3. Mahkeme ne karar verdi?              [hüküm kalemleri sırayla, sade dil]
4. Mahkeme neden böyle karar verdi?     [gerekçenin ana hatları, 3-5 cümle]
5. Bundan sonra ne olur?                [kanun yolu, mercii, süre — hükümdeki gibi; kesinleşme durumu]
6. Terimler                             [kısa sözlük]
[Zorunlu ibare]
```

**Sadakat tablosu** (iç kontrol, yayımlanmaz):

| Hüküm kalemi (karar metni) | Özet cümlesi | Anlam aynı mı | Sayı / tutar / süre aynı mı |
|---|---|---|---|

**Risk skalası:**
- 🔴 Özet hüküm fıkrasıyla çelişiyor; tutar, süre veya kanun yolu farklı; zorunlu ibare yok.
- 🟠 Kanun yolu bilgisi eksik ya da hüküm dışı bir kaynaktan alınmış; bir tarafın iddiası diğerinden belirgin biçimde uzun veya yüklü.
- 🟡 Yorum içeren ifade; açıklanmamış terim.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 297, 359; CMK m. 232 — bu sohbette çekildi mi, eşleşti mi (yalnız hüküm fıkrası yapısını göstermek için).
- Özet karartılmış metinden mi üretildi; gerçek kişisel veri kaldı mı.
- ⚠️ "Özet, hâkim/heyet onayı olmadan paylaşılmaz; bağlayıcı olan karar metnidir."

## Sıradaki adımlar

- `/karar-yayim:anonimlestirme` (önce yapılmadıysa)
- `/karar-yayim:karar-kunye-ozeti`

---

## /karar-yayim:karar-kunye-ozeti

---
name: karar-kunye-ozeti
description: >
  Mahkemenin kendi kararı ya da çekilen bir üst mahkeme kararı için emsal kaydına
  uygun künye kartı hazırlar: künye, uygulanan normlar (çekilen metin ve sürüm),
  mesele, ilke cümlesi (metinden birebir), anahtar kavramlar, sonuç, kanun yolu
  durumu. Kişisel veri içermez; ilke cümlesi uydurulmaz.
user-invocable: true
---

# Karar Künye Özeti — Emsal Kaydı

## Konum hatırlatması

Künye kartı bir arama ve hatırlama aracıdır; kararın yerine geçmez. İlke cümlesi yalnız karar metninden alınır; özetleyenin cümlesi ayrı işaretlenir. Taraf adı, kişisel veri ve olayın tanıtıcı ayrıntısı yazılmaz. Asistan UYAP'a bağlanmaz; karar metni kullanıcıdan veya araçla çekilen kaynaktan gelir.

## Amaç

Karar için emsal kaydına uygun, kişisel veri içermeyen bir künye kartı hazırlamak: künye, uygulanan normlar, mesele, karar metninden birebir alınan ilke cümlesi, anahtar kavramlar ve sonuç.

## Girdi

- Karar metni (kendi mahkemesinin kararı: kullanıcıdan; üst mahkeme kararı: `tr_ictihat_getir` / `tr_aym_getir` ile çekilmiş)
- Kayıt amacı: mahkeme içi emsal defteri / daire içtihat takibi / eğitim

## Adımlar

1. **Künye.** Mahkeme ve daire, E., K., karar tarihi; araçtan çekildiyse `citation` alanı birebir. Kesinleşme: araçta `kesinlesme` alanı varsa o; yoksa kullanıcıdan veya "bilinmiyor".
2. **Normlar.** Kararda uygulanan her madde `tr_mevzuat_madde_getir` ile çekilir; kararın tarihindeki metin ile güncel metin arasında değişiklik notu varsa yazılır (norm sürümü).
3. **Mesele.** Soru biçiminde, soyut: "… hâlinde … gerekir mi?"
4. **İlke.** Gerekçeden taşıyıcı cümle tırnak içinde, birebir. Yanında tek cümlelik soyutlama, "özetleyenin notu — karar değildir" etiketiyle.
5. **Anahtar kavramlar.** 3-8 terim; arama sorgusu olarak kullanılabilecek biçimde (`+"istinaf dilekçesine cevap"` gibi).
6. **Olay tipi.** Genelleştirilmiş, tanıtıcı olmayan (örn. "kira alacağı, kısmi ödeme savunması").
7. **Sonuç ve kanun yolu.** Hüküm türü; kanun yolu durumu ve bağlantılı kararlar (yalnız doğrulanan künyeler).
8. **Ayırt edici olgular.** Kararın başka olaya aktarılmasını sınırlayan olgular.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

```
KÜNYE KARTI — EMSAL KAYDI
Mahkeme / daire      : [DOLDUR]
E. / K. / tarih      : [DOLDUR]
Kesinleşme           : [kesinleşti / kesinleşmedi / bilinmiyor — kaynak]
Dava / suç / işlem   : [DOLDUR]
Uygulanan normlar    : [ArthurLegal TR — kanun m. X — çekim tarihi] (sürüm notu)
Mesele               : [soru biçiminde]
İlke (karardan)      : "[birebir cümle]"
Özetleyenin notu     : [tek cümle — karar değildir]
Anahtar kavramlar    : [3-8 terim]
Olay tipi            : [genelleştirilmiş]
Sonuç                : [hüküm türü]
Bağlantılı kararlar  : [yalnız doğrulanan künyeler]
Ayırt edici olgular  : [DOLDUR]
Kaydı hazırlayan     : [rol] · Tarih: [DOLDUR]
```

**Risk skalası:**
- 🔴 İlke cümlesi karar metninde yok ya da çarpıtılmış; doğrulanmamış bağlantılı künye.
- 🟠 Madde numarası çekilmeden yazılmış; norm sürüm notu eksik.
- 🟡 Kesinleşme bilinmiyor; anahtar kavramlar arama için kullanışsız.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: kartta geçen her madde bu sohbette çekildi mi, eşleşti mi.
- Üst mahkeme kararı çekilemediyse kart oluşturulmaz; ilgili resmî karar arama sayfasıyla UYARI satırı yazılır (Yargıtay https://karararama.yargitay.gov.tr/, Danıştay https://karararama.danistay.gov.tr/, bölge adliye, bölge idare ve yerel mahkeme https://emsal.uyap.gov.tr/, AYM https://kararlarbilgibankasi.anayasa.gov.tr/).
- ⚠️ "Emsal kaydının kullanımı hâkim/heyet takdirindedir."

## Sıradaki adımlar

- `/yargi-arastirma:emsal-tarama` — aynı meselede diğer kararlar
- `/yargi-arastirma:karsi-gorus-taramasi`

---

> v1.2.0 — `karar-yayim` 3 skill. Kalıp: `hukuk-hakim__skills.md`.
