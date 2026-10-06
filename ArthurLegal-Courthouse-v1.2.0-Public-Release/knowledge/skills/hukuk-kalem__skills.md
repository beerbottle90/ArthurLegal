# hukuk-kalem — Skill Referans Kitapçığı

> Dal: Hukuk mahkemesi · Rol: **Kalem (yazı işleri)** · Usul: HMK 6100 + Tebligat K. 7201 + Harçlar K. 492
> Toplam skill: 6
> Kullanım: `/hukuk-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar belge iskeleti ve kontrol listesidir; hâkim havalesi/onayı şarttır. Her çıktı **TASLAK**.

## İçindekiler

- /hukuk-kalem:tensip-zapti — dava açılışında (HMK m. 137 ön incelemesinden önce) tensip tutanağı & tahkikat planı
- /hukuk-kalem:tebligat — 7201 Tebligat K. usulü, tebliğ şerhi, e-tebligat
- /hukuk-kalem:harc-hesabi — Harçlar K. 492 nispi/maktu harç + gider avansı (HMK m. 120)
- /hukuk-kalem:durusma-tutanagi — HMK m. 154-158 duruşma tutanağı: mutlak yazılacaklar, okunup imzalatılacak beyanlar, ara karar ve ihtar
- /hukuk-kalem:istinaf-gonderme-kontrol — dosyayı bölge adliye mahkemesine göndermeden önce kontrol listesi (HMK m. 343-349)
- /hukuk-kalem:kesinlesme-serhi — kesinleşme tarihinin her taraf için hesabı ve şerh iskeleti (HMK m. 302)

---

## /hukuk-kalem:tensip-zapti

---
name: tensip-zapti
description: >
  Dava açıldıktan sonra düzenlenen tensip zaptı (tahkikat planı) iskeletini üretir:
  dava şartı ön-kontrol, taraflara verilecek süreler, harç/avans kontrolü,
  tebligat çıkışları, ilk duruşma. Hâkim havalesine sunulur.
user-invocable: true
---

# Tensip Zaptı — Tahkikat Planı İskeleti

## Amaç

Dava dosyası açıldığında kalemin hazırladığı ilk işlem zincirini eksiksiz yapılandır. Tensip zaptı hâkim tarafından imzalanır; kalem **taslağını** hazırlar.

## Kontrol & adımlar

1. **Dava dilekçesi kontrolü (HMK m. 119):** zorunlu unsurlar tam mı (taraflar, talep, vakıa, deliller, hukuki sebep, imza). Eksiklik (b), (c), (ç), (ğ) veya (h) bentlerinde ise (taraf ad/soyad/adres, davacı T.C. kimlik no, kanuni temsilci/vekil bilgisi, talep sonucu, imza) 1 haftalık kesin süre; tamamlanmazsa dava açılmamış sayılır (m. 119/2). (a), (d), (e), (f), (g) bentleri — mahkeme adı, dava konusu/değer, vakıalar, deliller, hukuki sebepler — bu kesin sürenin kapsamı dışındadır.
2. **Harç & gider avansı (m. 120):** başvuru + peşin harç yatırılmış mı; gider avansı tarifesi. Eksikse muhtıra. → `harc-gider-rehberi.md`.
3. **Tensip maddeleri (kalıp):**
   - Dilekçenin davalıya tebliği, **2 hafta** cevap süresi (m. 127)
   - Delil avansı ve delillerin sunulması (m. 121, 129)
   - Ön inceleme duruşma günü tayini
   - Varsa tedbir taleplerinin ayrı değerlendirilmesi
4. **Tebligat çıkışları:** kime, hangi adrese, hangi usulle (aşağıdaki `tebligat` skill'i).
5. **UYAP işlemleri:** dosya açılış, taraf/vekil kaydı, tevzi. → `uyap-rehberi.md`.

## Çıktı

`[DOLDUR]` alanlı tensip zaptı taslağı + eksik/muhtıra listesi (🔴🟠🟡). Üst başlık TASLAK + "hâkim havalesi şart".

---

## /hukuk-kalem:tebligat

---
name: tebligat
description: >
  7201 sayılı Tebligat Kanunu çerçevesinde tebligat usulünü belirler: muhatap,
  adres, tebliğ türü (normal / 21 / 35 / e-tebligat), şerh ve süre başlangıcı.
user-invocable: true
---

# Tebligat — 7201 Usulü

## Amaç

Bir evrakın hangi usulle, kime ve nasıl tebliğ edileceğini doğru belirle. Yanlış tebligat = sürelerin işlememesi + bozma riski 🔴.

## Karar ağacı

1. **Muhatap kim?** Gerçek kişi / tüzel kişi / vekil. Vekil varsa **vekile** tebliğ (HMK m. 73-81, Teb. K. m. 11).
2. **Adres var mı, doğru mu?** MERNİS adresi esas. Tüzel kişide ticaret sicil adresi.
3. **Tebliğ türü:**
   - **Normal tebliğ** (Teb. K. m. 10) — muhatap adreste.
   - **m. 21/1** — adreste bulunamazsa muhtara/komşu + 2 no'lu haber kâğıdı.
   - **m. 21/2** — gösterilen adres muhatabın adres kayıt sistemindeki adresiyse, muhatap orada hiç oturmamış veya sürekli ayrılmış olsa dahi muhtar/zabıtaya teslim + ihbarname kapıya; yapıştırma tarihi tebliğ tarihidir (bilinen en son adres elverişsizse veya orada tebligat yapılamazsa adres kayıt sistemindeki yerleşim yeri adresine çıkarma: m. 10/2).
   - **m. 35** — daha önce tebligat yapılmış adres değişmişse.
   - **e-Tebligat** (m. 7/a) — zorunlu muhataplar (avukat, tüzel kişi, kamu) için. → `kep-etebligat-rehberi.md`.
4. **Şerh & süre:** tebliğ tarihi sürelerin başlangıcı (istinaf ve temyiz süresi de ilamın tebliğinden işler — HMK m. 345/1, 361/1; hükümde kanun yolu ve süresinin gösterilmesi HMK m. 297/1-ç). Şerhin usulüne uygunluğunu kontrol et.

## Çıktı

Tebligat türü önerisi + tebliğ mazbatası kontrol listesi + süre başlangıcı hesabı. TASLAK ibareli.

---

## /hukuk-kalem:harc-hesabi

---
name: harc-hesabi
description: >
  Harçlar Kanunu 492 ve HMK m. 120 çerçevesinde dava harcı (başvuru, peşin nispi/maktu,
  karar-ilam) ve gider avansı hesabı için kontrol listesi. Adli yardım hâllerini de gözetir.
user-invocable: true
---

# Harç & Gider Avansı

## Amaç

Dava türüne göre alınacak harç ve avansı doğru belirle. Eksik harç = davanın açılmamış sayılması riski: yargı harçları ödenmedikçe müteakip işlemler yapılmaz (Harçlar K. m. 32); değer sonradan fazla tespit edilirse noksan harç tamamlanmadıkça davaya devam olunmaz ve dosyanın yeniden işleme konulması noksan harcın ödenmesine bağlıdır (Harçlar K. m. 30); işlemden kaldırılıp üç ay içinde yenilenmeyen dava açılmamış sayılır (HMK m. 150/4-5).

## Adımlar

1. **Dava türü → harç türü:**
   - **Konusu para ile ölçülebilen** → nispi harç (dava değeri üzerinden, Harçlar K. 492 (1) tarife).
   - **Konusu para ile ölçülemeyen** (tespit, bazı aile davaları) → maktu harç.
2. **Harç kalemleri:** başvurma harcı + peşin harç (nispi davada 1/4) + karar-ilam harcı (sonda).
3. **Gider avansı (HMK m. 120):** tarifeye göre; tebligat, bilirkişi, tanık, keşif giderleri. Delil avansı ayrı (m. 324).
4. **Adli yardım (HMK m. 334-340):** talep varsa harç/avanstan geçici muafiyet değerlendirmesi — hâkim kararına sunulur.
5. **Eksiklik → muhtıra:** kesin süre + sonuç (açılmamış sayılma / delilden vazgeçme).

## Çıktı

Harç/avans kalem tablosu (`[DOLDUR]` tutarlı) + eksiklik muhtırası taslağı. Güncel tarife için → `damga-vergisi-rehberi.md` ve yıllık Harçlar tarifesi (Resmi Gazete teyidi).

---

## /hukuk-kalem:durusma-tutanagi

---
name: durusma-tutanagi
description: >
  Hukuk duruşma tutanağını HMK m. 154-158 çerçevesinde hazırlar ve denetler: mutlak
  yazılacak hususlar, okunup imzalatılacak beyanlar, ara kararlar ve ihtarlar,
  belgeler, ses ve görüntü naklinin tutanağa geçirilmesi, imza, örnek verme. Zabıt
  kâtibinin kontrol listesi ve tutanak iskeleti.
user-invocable: true
---

# Duruşma Tutanağı (Hukuk) — HMK m. 154-158

## Konum hatırlatması

Ön inceleme, tahkikat ve yargılama işlemleri ancak tutanakla ispat olunabilir (HMK m. 156). Tutanak tarafların beyanlarını değiştirmeden ve eşit özenle kaydeder; zabıt kâtibi yorum eklemez. Tutanak hâkim ve zabıt kâtibi tarafından derhâl imzalanır (m. 155/1). Asistan UYAP'ta tutanak açmaz; taslak kalemin kullanımı içindir.

## Amaç

Zabıt kâtibinin duruşma tutanağını eksiksiz ve tarafsız tutmasına yardım etmek: tutanağa mutlaka yazılacakları, okunup imzalatılacak beyanları, ara kararları ve ihtarları kontrol listesiyle denetlemek.

## Dayanak (bu sohbette çekilir)

- **HMK m. 154** — hâkim işlemleri ve sözlü açıklamaları gerekirse özet olarak zabıt kâtibine kaydettirir; taraflar hâkimin izniyle doğrudan yazdırabilir. Mutlak olarak yazılacaklar (m. 154/3): a) mahkemenin adı, duruşmanın açıldığı yer, gün ve saat; b) hâkim, zabıt kâtibi, hazır bulunan taraflar, vekilleri, kanuni temsilcileri, fer'î müdahil ve tercümanın adları; c) yargılamanın aleni mi gizli mi yapıldığı; ç) beyanda bulunana okunup imzası alınmak kaydıyla ikrar, yeminin edası, davanın geri alınmasına muvafakat, davadan feragat ve davayı kabul beyanları ile sulh müzakereleri ve sonucu; d) beyanda bulunana okunmak kaydıyla taraf, tanık, bilirkişi veya uzman beyanı; e) duruşma dışında yapılan işlemlerin özeti; f) sunulan belgeler; g) soruşturmaya ilişkin istekler ve diğer kanunların tutanağa yazılmasını emrettiği konular; ğ) ara kararları ve hükmün sonucu; h) karar veya hükmün açıklanma biçimi. Tutanakta sözü edilen veya dosyaya konduğu belirtilen belgeler tutanağın eki sayılır (m. 154/4); teknik araçlarla kayıt tutanakla tespit edilir (m. 154/5).
- **HMK m. 155** — derhâl imza; imza atamayanın parmak izi (hangi parmak olduğu), parmağı olmayanlarda mühür veya özel işaret.
- **HMK m. 157** — mahkemede veya mahkeme dışında hâkim huzurundaki bütün işlemlerde zabıt kâtibinin bulunması zorunludur; zorunlu hâlde yemin ettirilerek başka kişi görevlendirilebilir.
- **HMK m. 158** — talep hâlinde örnek verilir, mühürlenir ve yazı işleri müdürünce onaylanır; gizlilik kararı kapsamındaki eklerin örneği ancak hâkimin izniyle verilir.
- **HMK m. 28/4** — gizli yargılamada hazır bulunanlara açıklamama ihtarı yapılır ve tutanağa geçirilir.
- **HMK m. 94/2** — kesin süre ve süreye uyulmamasının sonuçları açıkça tutanağa geçirilerek ihtar edilir.
- **HMK m. 140/3** — ön inceleme duruşması sonunda sulh veya arabuluculuk sonucu ve anlaşılamayan hususlar tutanakla tespit edilir; tutanağın altı hazır taraflarca imzalanır.
- **HMK m. 149** — ses ve görüntü nakledilmesi yoluyla katılım ve dinleme kararı.
- **HMK m. 294/3** — hükmün tefhimi, hüküm sonucunun duruşma tutanağına geçirilerek okunmasıyla olur.
- **HMK m. 147/3** — duruşmalar arasındaki süre üç aydan uzun olamaz; zorunlu hâllerde hâkim gerekçesini belirterek daha uzun süre belirleyebilir.
- **HMK m. 150** — usulüne uygun davet edilen tarafların gelmemesinin sonuçları.

## Girdi

- Duruşma bilgileri: mahkeme, esas numarası, tarih ve saat, hâkim veya heyet, zabıt kâtibi [DOLDUR]
- Hazır bulunanlar ve yoklama sonucu: taraflar, vekiller, tanık, bilirkişi [DOLDUR]
- Alınan beyanlar, sunulan belgeler ve hâkimin dikte ettirdiği ara kararlar [DOLDUR]
- Ses ve görüntü nakli yoluyla katılım varsa bilgisi [DOLDUR]
- Dosya bilgisi kullanıcıdan gelir; asistan UYAP'a bağlanmaz, kayıt eklemez.

## Kontrol listesi

**Duruşmadan önce**
- [ ] Esas no, taraflar ve vekiller, davetiyelerin tebliğ durumu
- [ ] Önceki ara kararın gereği yapıldı mı (müzekkere cevapları, avans, belge)
- [ ] Ses ve görüntü nakli kararı varsa bağlantı bilgisi (m. 149)

**Duruşma sırasında**
- [ ] m. 154/3-a, b, c başlık satırları
- [ ] Hazır olanlar ve olmayanlar; gelmeyen için tebligat durumu (m. 150)
- [ ] İkrar, feragat, kabul, sulh ve yemin beyanları **okunup imzalatıldı** (m. 154/3-ç)
- [ ] Taraf, tanık, bilirkişi, uzman beyanları **okundu** (m. 154/3-d)
- [ ] Sunulan belgeler tek tek (m. 154/3-f)
- [ ] Talepler ve itirazlar (m. 154/3-g)
- [ ] Ara kararlar numaralı; kesin süre ve sonuç ihtarı açık (m. 94/2; 154/3-ğ)
- [ ] Gizli yargılamada m. 28/4 ihtarı
- [ ] Ön incelemede anlaşılan ve anlaşılamayan hususlar ile sulh veya arabuluculuk sonucu, hazır tarafların imzası (m. 140/3)
- [ ] Hüküm verildiyse hüküm sonucunun tutanağa geçirilerek okunması (m. 294/3) ve açıklama biçimi (m. 154/3-h)
- [ ] Sonraki duruşma günü (m. 147/3)

**Duruşmadan sonra**
- [ ] Hâkim ve zabıt kâtibi imzası derhâl (m. 155/1)
- [ ] Ekler dosyada (m. 154/4); teknik kayıt tespit tutanağı (m. 154/5)
- [ ] Örnek talepleri; gizlilik kararı kapsamındaki ekler için hâkim izni (m. 158/2)

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

```
T.C. [DOLDUR] MAHKEMESİ                   DURUŞMA TUTANAĞI
Esas No: [DOLDUR]   Celse: [DOLDUR]   Tarih ve saat: [DOLDUR]   Yer: [DOLDUR]
Hâkim: [DOLDUR]     Zabıt Kâtibi: [DOLDUR]
Yargılama: [aleni / gizli — gizlilik kararı: DOLDUR]

Belirli gün ve saatte celse açıldı. Davacı [DOLDUR] ile vekili [DOLDUR] [geldi / gelmedi],
davalı [DOLDUR] ile vekili [DOLDUR] [geldi / gelmedi]. [Ses ve görüntü nakli: DOLDUR]
Açık yargılamaya başlandı.

[Beyanlar — her beyan ayrı paragraf; "okundu" / "okundu, imzası alındı" notu]
[Sunulan belgeler: 1) DOLDUR  2) DOLDUR]
[Talepler / itirazlar: DOLDUR]

GEREĞİ DÜŞÜNÜLDÜ: (ara karar)
1- [DOLDUR — muhatap, işlem, süre, kesin mi, sonuç ihtarı]
2- Duruşmanın [tarih] günü saat [saat]'e bırakılmasına,
dair [taraflar huzurunda / yokluğunda] karar verildi, açıkça okundu, usulen anlatıldı.

Hâkim [e-imza]                         Zabıt Kâtibi [e-imza]
```

**Risk skalası:**
- 🔴 İkrar, feragat, kabul veya sulh beyanının okunup imzalatılmadan kaydı; hâkim veya zabıt kâtibi imzasının eksikliği.
- 🟠 Kesin süre ihtarının tutanakta açık olmaması; gizli yargılama ihtarının yazılmaması.
- 🟡 Belge listesi veya hazır bulunanlar eksik; duruşma aralığı gerekçesiz üç ayı aşıyor.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 28, 94, 140, 147, 149, 150, 154, 155, 156, 157, 158, 294 — bu sohbette çekildi mi, eşleşti mi.
- UYAP'ta tutanak şablonu ve e-imza işlemi kullanıcı tarafından yapılır.
- ⚠️ "Tutanak hâkim ve zabıt kâtibi imzasıyla geçerlik kazanır; taslak onaysız kullanılmaz."

## Sıradaki adımlar

- `/hukuk-hakim:ara-karar` — ara karar kalemlerinin denetimi
- `/hukuk-kalem:tebligat` — hazır olmayan tarafa ara kararın tebliği

---

## /hukuk-kalem:istinaf-gonderme-kontrol

---
name: istinaf-gonderme-kontrol
description: >
  İlk derece hukuk mahkemesi kaleminin, istinaf başvurusu yapılan dosyayı bölge adliye
  mahkemesine göndermeden önce yapacağı kontrol: başvurunun kaydı, harç ve giderler,
  süre ve kesinlik yönünden hâkime sunulacak hususlar, karşı tarafa tebliğ ve cevap
  süresi, katılma yoluyla başvuru, feragat, dizi listesi.
user-invocable: true
---

# İstinafa Göndermeden Önce Kontrol (Hukuk Kalemi)

## Konum hatırlatması

Süre aşımı veya kesin karar nedeniyle istinaf dilekçesinin reddi ilk derece mahkemesinin kararıdır (HMK m. 346); kalem bu hususları hâkime sunar, kendisi karar vermez. Cevap süresi dolmadan gönderme, bölge adliye mahkemesinde silahların eşitliği sorununa yol açabilir (aşağıdaki not). Asistan UYAP'ta işlem yapmaz. **Başvurunun reddi, süre ve kesinlik yönünden her karar için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

İstinaf başvurusu yapılan dosyanın bölge adliye mahkemesine eksiksiz ve zamanında gönderilmesi için kalemin yapacağı kontrolleri sıralamak; süre, kesinlik ve harç gibi sonuç doğuran hususları hâkime sunulacak biçimde ayırmak.

## Girdi

- Karar tarihi ve gerekçeli kararın her tarafa tebliğ tarihi [DOLDUR]
- İstinaf dilekçesinin veriliş tarihi, verildiği yer ve kayıt bilgisi [DOLDUR]
- Yatırılan harç ve giderler [DOLDUR]
- Karşı tarafa tebliğ tarihi; cevap ve katılma yoluyla başvuru dilekçeleri [DOLDUR]
- Dava değeri ve kararın türü (kesinlik kontrolü için) [DOLDUR]
- Dosya bilgisi kullanıcıdan gelir; asistan UYAP'a bağlanmaz, kayıt eklemez.

## Kontrol listesi

- [ ] **Kayıt ve alındı:** dilekçe bölge adliye mahkemesi başvuru defterine kaydedildi, ücretsiz alındı verildi; başka yer mahkemesine verilmişse örnekleriyle gönderildi ve durum bildirildi (m. 343/1-2)
- [ ] **Başvuru tarihi:** m. 343/3'ün yollamasıyla dilekçenin kaydedildiği tarih (m. 118/1)
- [ ] **Harç ve giderler:** istinaf için gerekli harçlar ve tebliğ giderleri dâhil tüm giderler; eksikse bir haftalık kesin süre ve "başvurudan vazgeçmiş sayılma" sonucunu içeren yazılı bildirim; süre içinde tamamlanmazsa "başvuru yapılmamış sayılma" kararı için hâkime sunum (m. 344)
- [ ] **Süre:** her başvuran için ilamın tebliğ tarihi → iki haftalık süre (m. 345) → son gün (resmî tatil m. 93, adli tatil m. 104); süre geçmiş görünüyorsa hâkime sunum (m. 346/1)
- [ ] **Kesinlik:** dava değeri ve dava tarihi; kesinlik tereddüdü varsa hâkime sunum (m. 341/2, Ek m. 1; manevi tazminat davalarında miktara bakılmaz)
- [ ] **Ret kararı varsa:** ret kararı ilgiliye tebliğ edildi mi; ret kararına karşı iki hafta içinde başvuru ve giderler (m. 346)
- [ ] **Karşı tarafa tebliğ:** istinaf dilekçesi karşı tarafa tebliğ edildi; iki haftalık cevap süresi doldu mu veya cevap verildi mi (m. 347/1-2)
- [ ] **Katılma yoluyla istinaf:** cevap dilekçesinde başvuru varsa asıl başvurana tebliğ ve iki haftalık cevap süresi (m. 348/1)
- [ ] **Feragat:** dosya gönderilmeden önce feragat edildiyse dosya gönderilmez, başvurunun reddi kararı için hâkime sunum (m. 349/2)
- [ ] **Dizi listesi:** dilekçeler verildikten veya süreler geçtikten sonra dosya dizi listesine bağlı olarak gönderilir (m. 347/3); gerekçeli karar, tebliğ mazbataları, ekler, bilirkişi raporları, tedbir dosyası
- [ ] **Adli tatil:** istinaf ve cevap dilekçelerinin alınması, her türlü tebligat ve dosyanın bölge adliye mahkemesine gönderilmesi adli tatilde de yapılır (m. 103/3)

> Not: Anayasa Mahkemesi, istinaf dilekçesine cevap süresi dolmadan dosyanın gönderilmesini ve dairenin bu süre dolmadan kesin karar vermesini silahların eşitliği ve çelişmeli yargılama ilkelerinin ihlali saymıştır `[ArthurLegal TR — AYM — B. No: 2017/18458 — 10.02.2021]` (27.09.2026'da çekildi; çıktıya girecekse yeniden çekilir).

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Gönderme kontrol formu** (yukarıdaki liste ✓/✗) ve süre tablosu: | Başvuran | İlam tebliğ tarihi | Başvuru (kayıt) tarihi | Son gün (en erken) | Karşı tarafa tebliğ | Cevap süresi sonu |
2. **Hâkime sunulacaklar listesi** (süre, kesinlik, harç, feragat).
3. **Üst yazı iskeleti:**

```
[DOLDUR] BÖLGE ADLİYE MAHKEMESİ İLGİLİ HUKUK DAİRESİ BAŞKANLIĞINA
Mahkememizin [DOLDUR] esas, [DOLDUR] karar sayılı dosyasında verilen karara karşı
[DOLDUR] tarafından istinaf yoluna başvurulmuş olup cevap [ve katılma yoluyla başvuruya
cevap] süreleri dolmuştur. Dosya dizi listesine bağlı olarak gönderilmiştir.
Ek: Dizi listesi ([DOLDUR] sayfa)
[Yazı işleri müdürü — DOLDUR]          [Hâkim onayı — DOLDUR]
```

**Risk skalası:**
- 🔴 Cevap veya katılma yoluyla başvuruya cevap süresi dolmadan gönderme; bir tarafa ilam tebliği yokken süre hesabı.
- 🟠 Harç eksikliği için m. 344 işleminin yapılmaması; süre veya kesinlik tereddüdünün hâkime sunulmaması.
- 🟡 Dizi listesi veya ek eksikleri.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 93, 103, 104, 118, 341, 343, 344, 345, 346, 347, 348, 349, Ek m. 1 — bu sohbette çekildi mi, eşleşti mi.
- Dosya, istinaf dilekçesinde gösterilen daireyle bağlı kalınmaksızın ilgili bölge adliye mahkemesine gönderilir (m. 343/4).
- Süre hesabı hatırlatmadır; son günü kalem ve hâkim teyit eder.
- ⚠️ "Ret, yapılmamış sayılma ve feragat nedeniyle ret kararları hâkime aittir."

## Sıradaki adımlar

- `/hukuk-kalem:tebligat` — ilam ve istinaf dilekçesi tebliğleri
- `/hukuk-kalem:kesinlesme-serhi` — başvurmayan taraflar yönünden

---

## /hukuk-kalem:kesinlesme-serhi

---
name: kesinlesme-serhi
description: >
  Hukuk mahkemesi kararının kesinleşme tarihini her taraf için ayrı hesaplayıp
  kesinleşme şerhi iskeletini hazırlar: tebliğin usule uygunluğu, istinaf ve temyiz
  süreleri, feragat, kanun yolu sonuçları, kısmi kesinleşme, kesinleşmeden yerine
  getirilemeyen kararlar ve yerine getirme bildirimleri.
user-invocable: true
---

# Kesinleşme Şerhi (Hukuk)

## Konum hatırlatması

Hükmün kesinleştiği, ilamın altına veya arkasına yazılıp tarih ve mahkeme mührü konmak ve başkan veya hâkim tarafından imzalanmak suretiyle belirtilir (HMK m. 302/4). Kalem hesaplar ve taslağı hazırlar; şerhi hâkim imzalar. Yanlış şerh icra ve tescil gibi geri dönüşü güç sonuçlar doğurur. Asistan UYAP'ta şerh işlemez. **Kesinleşme şerhi için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

Kararın kesinleşme tarihini her taraf için ayrı hesaplamak ve hâkimin imzasına sunulacak kesinleşme şerhi taslağını hazırlamak; hesabı etkileyen tebliğ ve kanun yolu bilgilerindeki eksikleri önceden göstermek.

## Dayanak (bu sohbette çekilir)

- **HMK m. 302/4-5** — şerhin biçimi; kanun yollarından geçmek suretiyle kesinleşen kararların kesinleşme kaydı ve yerine getirilmeleri için gerekli bildirimler ilk derece mahkemesince yapılır.
- **HMK m. 345** — istinaf süresi iki hafta; ilamın usulen taraflardan her birine tebliğiyle işler.
- **HMK m. 361/1** — temyiz süresi tebliğ tarihinden itibaren iki hafta.
- **HMK m. 359/4** — bölge adliye mahkemesi kararlarından temyizi kabil olmayanlar ilk derece mahkemesince, temyizi kabil olanlar bölge adliye mahkemesince resen tebliğe çıkarılır.
- **HMK m. 348, 349** — katılma yoluyla başvuru; kanun yolundan feragat (ilamın tebliğinden önce feragat edilemez).
- **HMK m. 341/2, 362, Ek m. 1** — kesin kararlar ve parasal sınırlar.
- **HMK m. 350/2, 367/2** — kişiler hukuku, aile hukuku ve taşınmaz mal ile ilgili ayni haklara ilişkin kararlar kesinleşmedikçe yerine getirilemez.
- **HMK m. 92-93, 104** — sürenin bitimi; son günün resmî tatile rastlaması; süre sonu adli tatile rastlarsa adli tatilin bittiği günden itibaren bir hafta uzamış sayılır.
- **Tebligat K. m. 7/a** (elektronik tebligat, elektronik adrese ulaşmayı izleyen beşinci günün sonunda yapılmış sayılır), **m. 11** (vekile tebligat), **m. 21, 35** (tebliğ şekilleri), **m. 32** (usulsüz tebliğde muhatabın öğrendiğini beyan ettiği tarih).

## Girdi

- Karar tarihi ve türü (ilk derece / bölge adliye mahkemesi / Yargıtay sonrası)
- Her taraf ve vekil için tebliğ tarihi, tebliğ şekli ve mazbata bilgisi
- Kanun yolu başvuruları, feragatler, bölge adliye mahkemesi ve Yargıtay kararları ile bunların tebliğ tarihleri
- Karar birden çok hüküm kalemi içeriyorsa hangi kaleme başvurulduğu

## Adımlar

1. **Tebliğ denetimi:** her taraf için tebliğ usule uygun mu; vekil varsa vekile yapılmış mı (Tebligat K. m. 11); e-tebligatta beşinci gün kuralı.
2. **Süre hesabı:** tebliğ tarihi → iki hafta (istinaf m. 345 / temyiz m. 361/1) → son gün (m. 92-93; adli tatil m. 104). Bilinmeyen olguda en erken tarih alınır ve 🟠 işaretlenir.
3. **Başvuru var mı:** her taraf için ayrı; katılma yoluyla başvuru (m. 348) dâhil.
4. **Kanun yolu sonucu:** bölge adliye mahkemesi veya Yargıtay kararı ve tebliği; kararın temyize açık olup olmadığı (m. 362) ve tebliği kimin yapacağı (m. 359/4).
5. **Feragat:** tarihi ve ilamın tebliğinden sonra mı (m. 349/1).
6. **Kısmi kesinleşme:** kanun yoluna konu edilmeyen hüküm kalemleri ayrı değerlendirilir; hangi kalemin kesinleştiği açıkça yazılır.
7. **Kesinleşme tarihi:** tarafların son günlerinden en geç olanı ya da kanun yolu kararının kesinleştiği tarih — hâkime sunulur.
8. **Yerine getirme bildirimleri:** tapu, nüfus, sicil vb. (m. 302/5) — [DOLDUR].

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Kesinleşme hesap tablosu:** | Taraf / vekil | Tebliğ tarihi ve şekli | Usule uygun mu | Kanun yolu ve süresi | Son gün (en erken) | Başvuru / feragat | Kanun yolu sonucu | Kesinleşme |
2. **Şerh iskeleti:**

```
KESİNLEŞME ŞERHİ
İşbu karar [tamamı / … numaralı hüküm kalemleri yönünden] [DOLDUR] tarihinde kesinleşmiştir.
[Kanun yolu: başvurulmadan / … Dairesinin … E., … K. sayılı kararı ile]
Tarih: [DOLDUR]                    Mühür
Hâkim / Başkan: [DOLDUR — imza]
```

3. **Bildirim listesi** (kurum, belge, dayanak).

**Risk skalası:**
- 🔴 Bir tarafa tebliğ yokken veya usulsüzken şerh; süre dolmadan şerh; kişiler hukuku, aile hukuku veya taşınmaz ayni hak kararında kesinleşme hatası.
- 🟠 Kanun yolu sonucu veya tebliği dosyada yok; e-tebligatta beşinci gün kuralının atlanması.
- 🟡 Kısmi kesinleşmenin şerhte belirtilmemesi.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 92, 93, 104, 302, 341, 345, 348, 349, 350, 359, 361, 362, 367, Ek m. 1; Tebligat K. m. 7/a, 11, 21, 32, 35 — bu sohbette çekildi mi, eşleşti mi.
- Süre hesabı hatırlatmadır; kesinleşme tarihini hâkim teyit eder.
- ⚠️ "Kesinleşme şerhi hâkim veya başkan imzasıyla verilir."

## Sıradaki adımlar

- `/hukuk-kalem:tebligat` — usulsüz tebliğin yenilenmesi
- `/istinaf-kalem:karar-sonrasi-islemler` — kanun yolundan dönen dosya

---

> 🚧 v1.0.0 — `hukuk-kalem` 3 temel kalem skill'i; v1.2.0'da duruşma tutanağı, istinafa gönderme kontrolü ve kesinleşme şerhi eklendi (toplam 6). Kalıp: `hukuk-hakim__skills.md`.
