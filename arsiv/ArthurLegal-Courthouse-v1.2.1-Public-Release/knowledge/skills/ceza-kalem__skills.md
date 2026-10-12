# ceza-kalem — Skill Referans Kitapçığı

> Dal: Ceza mahkemesi · Rol: **Kalem (yazı işleri)** · Usul: CMK 5271 + Tebligat K. 7201
> Toplam skill: 5
> Kullanım: `/ceza-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar belge iskeleti + kontrol listesidir; hâkim havalesi/onayı şarttır. Her çıktı **TASLAK**.

## İçindekiler

- /ceza-kalem:muzekkere — müzekkere / yazışma türleri ve içerik kontrolü
- /ceza-kalem:ceza-tebligat — CMK + 7201 tebligat (sanık, müdafi, mağdur, tanık)
- /ceza-kalem:infaz-evraki — kesinleşme şerhi, müddetname, infaz savcılığına gönderme
- /ceza-kalem:durusma-tutanagi — CMK m. 219-222 duruşma tutanağı: başlık, içerik, son söz, hüküm ve tefhim, kapalı duruşma
- /ceza-kalem:kanun-yolu-gonderme — istinaf ve temyiz başvurusunun alınması, tebliğ ve cevap, dosyanın gönderilmesi (CMK m. 263, 273-277, 291, 293, 296, 297)

---

## /ceza-kalem:muzekkere

---
name: muzekkere
description: >
  Ceza dosyasında sık kullanılan müzekkere/yazışma türleri için içerik iskeleti:
  adli sicil, nüfus, SGK, banka/HTS, ekspertiz, talimat (istinabe) müzekkereleri.
user-invocable: true
---

# Müzekkere — Yazışma İskeleti

## Amaç

Hâkimin ara kararı doğrultusunda çıkacak müzekkerenin doğru muhataba, doğru içerikle hazırlanması.

## Tipik müzekkereler

1. **Adli sicil / arşiv kaydı** — Adli Sicil ve İstatistik GM.
2. **Nüfus & MERNİS adres** — NVİ.
3. **SGK / işyeri kaydı, HTS-baz kaydı, banka kayıtları** — koruma tedbiri/karar şartı varsa (CMK m. 135 vd. iletişim tespiti hâkim kararı gerektirir 🔴).
4. **Talimat (istinabe) müzekkeresi (CMK m. 180 — tanık/bilirkişi; m. 196/2 — sanık sorgusu, alt sınırı beş yıl ve daha fazla hapis gerektiren suçlar hariç)** — başka yer mahkemesinden tanık/sanık ifadesi.
5. **Bilirkişi / ATK** — rapor talebi, sorulacak sorular net.

## Kontrol

- Muhatap kurum + yasal dayanak + istenen bilgi net mi
- Koruma tedbiri gerektiren bilgi için **hâkim kararı** şart mı (HTS, iletişim, banka sırrı)
- UYAP üzerinden çıkış + takip → `uyap-rehberi.md`

## Çıktı

Müzekkere taslağı (`[DOLDUR]`) + dayanak/şart kontrolü. TASLAK + "hâkim havalesi şart".

---

## /ceza-kalem:ceza-tebligat

---
name: ceza-tebligat
description: >
  Ceza dosyasında tebligat usulü: sanık/müdafi/mağdur/tanık/katılan için 7201 ve CMK
  özel hükümleri (gıyapta hüküm, müdafiye tebliğ, kanun yolu süresi başlangıcı).
user-invocable: true
---

# Ceza Tebligat — CMK + 7201

## Amaç

Ceza dosyasında doğru muhataba doğru usulle tebligat; kanun yolu süresinin doğru başlaması.

## Notlar

1. **Muhatap:** sanık + **müdafi** (varsa). İstinaf ve temyiz süresini **hükmün gerekçesiyle birlikte tebliği** başlatır (CMK m. 273/1, 291/1); hüküm fıkrasında kanun yolu, süresi ve mercii açıkça gösterilir (m. 232/6).
2. **Mağdur/katılan** — katılma talebi/kararı ve tebligat hakları.
3. **Gıyabi işlemler & yokluk:** duruşmadan haberdar edilme; bazı kararların yüze karşı/yoklukta tefhimi.
4. **e-Tebligat:** müdafi (avukat) zorunlu e-tebligat muhatabı → `kep-etebligat-rehberi.md`.
5. **Süre başlangıcı:** istinaf ve temyiz süresi **iki hafta**dır ve hükmün gerekçesiyle birlikte tebliğinden işler (CMK m. 273/1, 291/1 — 7499 s.K.; tefhim süreyi başlatmaz). İtiraz da iki hafta, öğrenmeden (m. 268/1). ⚠️ Süreyi MCP/mevzuat teyidiyle doğrula.

## Çıktı

Tebligat planı + süre başlangıcı tablosu. TASLAK ibareli.

---

## /ceza-kalem:infaz-evraki

---
name: infaz-evraki
description: >
  Kesinleşen ceza kararı için kesinleşme şerhi, müddetname hazırlığı ve infaz
  Cumhuriyet savcılığına gönderme işlemleri kontrol listesi.
user-invocable: true
---

# İnfaz Evrakı — Kesinleşme & Gönderme

## Amaç

Karar kesinleştiğinde infaz sürecini başlatacak evrakı eksiksiz hazırla.

## Adımlar

1. **Kesinleşme kontrolü:** kanun yolu sürelerinin geçtiği / mercilerce onandığı; kesinleşme tarihi tespiti.
2. **Kesinleşme şerhi** — karara işlenir.
3. **Müddetname** (5275 İnfaz K.) — ceza süresi hesabı; mahsup (gözaltı/tutukluluk: TCK m. 63; adli kontrol süresi kural olarak mahsup edilmez — m. 109/3-e tedavi/muayene ve m. 109/3-j konutu terk etmeme hâlleri hariç, (j)'de her iki gün bir gün: CMK m. 109/6).
4. **İnfaz C. Başsavcılığına gönderme** — ilam + müddetname + kesinleşme şerhi.
5. **Harç/yargılama gideri** tahsili, varsa adli para cezası infazı.

## Çıktı

Kesinleşme & infaz gönderme kontrol listesi + müddetname unsur taslağı. ⚠️ Süre/mahsup hesabı için mevzuat (5275) teyidi şart. TASLAK ibareli.

---

## /ceza-kalem:durusma-tutanagi

---
name: durusma-tutanagi
description: >
  Ceza duruşma tutanağını CMK m. 219-222 çerçevesinde hazırlar ve denetler: başlık,
  hazır bulunanlar, sanık açıklamaları, tanık ve bilirkişi ifadeleri, okunan belgeler,
  istemler ve reddin gerekçesi, verilen kararlar, son söz, hüküm ve tefhim, kapalı
  duruşma ve ses-görüntü aktarımı. Zabıt kâtibinin kontrol listesi ve tutanak iskeleti.
user-invocable: true
---

# Duruşma Tutanağı (Ceza) — CMK m. 219-222

## Konum hatırlatması

Duruşmanın nasıl yapıldığı ve kanunda belirtilen usul ve esaslara uygun olarak yapılıp yapılmadığı ancak tutanakla ispat olunabilir; tutanağa karşı yalnız sahtecilik iddiası yöneltilebilir (CMK m. 222). Bu nedenle tutanak iddia ve savunmayı eşit özenle, değiştirmeden kaydeder; zabıt kâtibi yorum eklemez. Asistan UYAP'ta tutanak açmaz, ses ve görüntü kaydını göremez.

## Amaç

Zabıt kâtibinin ceza duruşma tutanağını kanunun aradığı başlık ve içerikle, iddia ve savunmayı eşit özenle kaydedecek biçimde tutmasına yardım etmek.

## Dayanak (bu sohbette çekilir)

- **CMK m. 219** — duruşma için tutanak tutulur; mahkeme başkanı veya hâkim ile zabıt kâtibince imzalanır; işlemler teknik araçlarla kayda alınmışsa kayıtlar vakit geçirilmeksizin yazılı tutanağa dönüştürülerek imzalanır; başkanın mazereti hâlinde en kıdemli üye imzalar.
- **CMK m. 220** — tutanak başlığı: duruşmanın yapıldığı mahkemenin adı, oturum tarihleri, hâkim, Cumhuriyet savcısı ve zabıt kâtibinin adı ve soyadı.
- **CMK m. 221** — tutanak içeriği: a) oturumlara katılan sanık, müdafi, katılan, vekil, kanuni temsilci, bilirkişi, tercüman ve teknik danışmanın adı; b) duruşmanın seyrini ve sonuçlarını yansıtan ve yargılama usulünün bütün temel kurallarına uyulduğunu gösteren unsurlar; c) sanık açıklamaları; d) tanık ifadeleri; e) bilirkişi ve teknik danışman açıklamaları; f) okunan veya okunmasından vazgeçilen belge ve yazılar; g) istemler ve reddi hâlinde gerekçesi; h) verilen kararlar; i) hüküm.
- **CMK m. 182, 185** — duruşma herkese açıktır; kapalı duruşmaya ilişkin gerekçeli karar ile hüküm açık duruşmada açıklanır; sanık on sekiz yaşını doldurmamışsa duruşma kapalı yapılır ve hüküm de kapalı duruşmada açıklanır.
- **CMK m. 183** — adliye binasında ve duruşma salonunda ses veya görüntü kaydı ya da nakli sağlayan aletler kullanılamaz (m. 180/5 ve 196/4 saklı).
- **CMK m. 180/5, 196/4** — tanık veya bilirkişinin ve sanığın aynı anda görüntülü ve sesli iletişim tekniğiyle dinlenmesi veya duruşmaya katılması.
- **CMK m. 58/3** — kimliği saklı tanığın hazır bulunma hakkı olanlar olmadan ses ve görüntülü aktarmayla dinlenmesi (örgüt faaliyeti çerçevesindeki suçlar, m. 58/5); **m. 236/3** — mağdur çocuğun veya suçun etkisiyle psikolojisi bozulmuş mağdurun tanık olarak dinlenmesinde uzman bulundurulması.
- **CMK m. 216** — delillerin tartışılmasında söz sırası; hükümden önce son söz hazır bulunan sanığa verilir (m. 216/3).
- **CMK m. 231/1-3** — tutanağa geçirilen hüküm fıkrası okunarak gerekçesi ana çizgileriyle anlatılır; hazır bulunan sanığa kanun yolları, mercii ve süresi bildirilir; beraat eden sanığa tazminat isteyebileceği hâl varsa bildirilir.
- **CMK m. 263** — tutuklu şüpheli veya sanık, zabıt kâtibine veya kurum müdürüne beyanla ya da dilekçeyle kanun yollarına başvurabilir; beyan deftere kaydedilir ve tutanak düzenlenir.

## Girdi

- Duruşma bilgileri: mahkeme, esas numarası, tarih ve saat, hâkim veya heyet, Cumhuriyet savcısı, zabıt kâtibi [DOLDUR]
- Hazır bulunanlar: sanık, müdafi, katılan ve vekili, tanık, bilirkişi, tercüman [DOLDUR]
- Sanık açıklamaları, tanık ve bilirkişi ifadeleri, okunan belgeler, istemler ve verilen kararlar [DOLDUR]
- Kapalı duruşma kararı veya ses ve görüntü aktarımı varsa bilgisi [DOLDUR]
- Dosya bilgisi kullanıcıdan gelir; asistan UYAP'a bağlanmaz, kayıt eklemez.

## Kontrol listesi

**Başlık ve hazırlık**
- [ ] m. 220 başlık unsurları; oturum tarihi ve saati
- [ ] Açık / kapalı (m. 182, 185); kapalıysa gerekçeli karar ve açıklanma biçimi
- [ ] Ses ve görüntü aktarımı kararı ve bağlantı (m. 180/5, 196/4)

**Seyir**
- [ ] Hazır bulunanlar ve bulunmayanlar (m. 221/1-a); zorunlu müdafi hazır mı
- [ ] Kimlik tespiti ve hakların hatırlatılması [DOLDUR — yapılan işlem]
- [ ] Sanık açıklamaları (m. 221/1-c) — birebir mi özet mi olduğu belirtilerek
- [ ] Tanık, bilirkişi ve teknik danışman ifadeleri (m. 221/1-d, e); mağdur çocuk dinlenmesinde uzman (m. 236/3)
- [ ] Okunan veya okunmasından vazgeçilen belgeler (m. 221/1-f)
- [ ] İstemler ve ret gerekçeleri (m. 221/1-g)
- [ ] Verilen kararlar (m. 221/1-h); tutukluluk incelemesi yapıldıysa sonucu
- [ ] Esas hakkında mütalaa; savunma; **son söz sanığa** (m. 216/3)
- [ ] Hüküm fıkrası okundu; gerekçesi ana çizgileriyle anlatıldı; hazır sanığa kanun yolu, mercii ve süresi bildirildi (m. 231/1-2); beraatte tazminat bildirimi (m. 231/3)
- [ ] Tutuklu sanığın kanun yoluna başvuru beyanı varsa ayrı tutanak ve defter kaydı (m. 263)

**Sonra**
- [ ] Teknik kayıt yazılı tutanağa dönüştürüldü (m. 219/1)
- [ ] Başkan veya hâkim ile zabıt kâtibi imzası (m. 219)

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

```
T.C. [DOLDUR] CEZA MAHKEMESİ                    DURUŞMA TUTANAĞI
Esas No: [DOLDUR]     Oturum: [DOLDUR]     Tarih ve saat: [DOLDUR]
Başkan/Hâkim: [DOLDUR]  Üyeler: [DOLDUR]  C. Savcısı: [DOLDUR]  Zabıt Kâtibi: [DOLDUR]
Duruşma: [açık / kapalı — gerekçe ve dayanak: DOLDUR]

Hazır bulunanlar: Sanık [DOLDUR] (tutuklu / tutuksuz), Müdafi [DOLDUR], Katılan [DOLDUR],
Vekil [DOLDUR], Tercüman / Bilirkişi [DOLDUR].  [Ses ve görüntü aktarımı: DOLDUR]

[Sanık açıklaması: DOLDUR]
[Tanık / bilirkişi ifadesi: DOLDUR — okundu]
[Okunan belgeler: 1) DOLDUR]
[İstemler: DOLDUR — karar ve gerekçe]
[Esas hakkında mütalaa: DOLDUR]   [Savunma: DOLDUR]
Sanığa son sözü soruldu: "[DOLDUR]"

HÜKÜM: [DOLDUR — hüküm fıkrası birebir]
Hüküm fıkrası okundu, gerekçesi ana çizgileriyle anlatıldı; hazır bulunan sanığa
kanun yolları, mercii ve süresi bildirildi.

Başkan/Hâkim [e-imza]              Zabıt Kâtibi [e-imza]
```

**Risk skalası:**
- 🔴 Son sözün sanığa verildiği tutanakta yok; on sekiz yaşından küçük sanıkta açık duruşma; imza eksik.
- 🟠 Teknik kayıt yazılı tutanağa dönüştürülmemiş; reddedilen istemin gerekçesi yazılmamış; tutanağa geçen hüküm fıkrası ile gerekçeli karar arasında fark.
- 🟡 Okunan belgeler veya hazır bulunanlar eksik.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: CMK m. 58, 180, 182, 183, 185, 196, 216, 219, 220, 221, 222, 231, 236, 263 — bu sohbette çekildi mi, eşleşti mi.
- Tutanak taslağında gereksiz kişisel veri tekrarlanmaz; dosya belgeleri Arthur Mask ile maskelenebilir.
- ⚠️ "Tutanak başkan veya hâkim ile zabıt kâtibi imzasıyla geçerlik kazanır."

## Sıradaki adımlar

- `/ceza-kalem:ceza-tebligat` — gerekçeli hükmün tebliği
- `/ceza-kalem:kanun-yolu-gonderme`
- `/ceza-hakim:gerekce-denetimi`

---

## /ceza-kalem:kanun-yolu-gonderme

---
name: kanun-yolu-gonderme
description: >
  Ceza dosyasında istinaf ve temyiz başvurularının alınmasından dosyanın bölge adliye
  mahkemesine veya Yargıtay'a gönderilmesine kadar kalem işlemlerini sıralar: dilekçe
  veya beyan tutanağı, tutuklunun başvurusu, süre ve başvuru hakkı yönünden hâkime
  sunum, karşı tarafa tebliğ ve cevap, dosyanın gönderilmesi.
user-invocable: true
---

# Kanun Yolu Başvurusunun Alınması ve Dosyanın Gönderilmesi (Ceza)

## Konum hatırlatması

Süre, istinaf veya temyiz edilemezlik ya da başvuru hakkının yokluğu nedeniyle ret kararı hükmü veren mahkemenindir (CMK m. 276, 296); kalem yalnız hesaplar ve sunar. İstinaf ve temyiz süreleri hükmün gerekçesiyle birlikte tebliğ edildiği tarihten işler (m. 273/1, 291/1; 7499 s.K.); tefhim süreyi başlatmaz. **Tutuklu dosyalar önceliklidir.** Asistan UYAP'ta işlem yapmaz. **Başvurunun reddi, süre ve kesinlik yönünden her karar için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

İstinaf ve temyiz başvurularının alınmasından dosyanın gönderilmesine kadar kalem işlemlerini sıraya koymak; süre ve başvuru hakkı gibi hâkime sunulacak hususları ayrı göstermek.

## Girdi

- Hükmün tarihi ve gerekçeli hükmün her ilgiliye tebliğ tarihi [DOLDUR]
- Başvuranın sıfatı: sanık, müdafi, katılan, Cumhuriyet savcısı, yasal temsilci veya eş [DOLDUR]
- Başvuru dilekçesi veya zabıt kâtibine yapılan beyanın tutanağı [DOLDUR]
- Sanığın tutuklu olup olmadığı; tutukluysa başvurunun yapıldığı yer ve kayıt bilgisi [DOLDUR]
- Dosya bilgisi kullanıcıdan gelir; asistan UYAP'a bağlanmaz, kayıt eklemez.

## Akış — istinaf

1. **Başvurunun alınması:** hükmü veren mahkemeye dilekçe veya zabıt kâtibine beyan; beyan tutanağa geçirilir ve tutanak hâkime onaylatılır (m. 273/1). Tutuklu: zabıt kâtibine veya kurum müdürüne beyan ya da dilekçe; deftere kayıt, tutanak ve örneğin verilmesi; bu işlemle süre kesilmiş sayılır (m. 263). Kanun yolunun veya merciin belirlenmesinde yanılma başvuranın haklarını ortadan kaldırmaz; başvuru derhâl görevli ve yetkili mercie gönderilir (m. 264).
2. **Başvuru hakkı:** Cumhuriyet savcısı, şüpheli, sanık, katılan ve katılma isteği karara bağlanmamış, reddedilmiş veya katılan sıfatını alabilecek surette suçtan zarar görenler (m. 260); yasal temsilci ve eş (m. 262).
3. **Süre:** iki hafta, hükmün gerekçesiyle birlikte tebliğinden (m. 273/1); ağır ceza mahkemesi Cumhuriyet savcısının yargı çevresindeki asliye mahkemesi hükümlerine başvurusunda kararın başsavcılığa geliş tarihinden (m. 273/3); yokluğunda verilen hükümde eski hâle getirme süresi içinde istinaf süresi de işler (m. 274). Süre hesabı: m. 39 (gün, hafta, ay; son gün tatile rastlarsa tatilin ertesi günü); adli tatil m. 331/4 (tatile rastlayan süreler işlemez, tatilin bittiği günden itibaren üç gün uzamış sayılır).
4. **Hâkime sunum:** süre geçmiş, istinaf edilemeyen hüküm (m. 272/3) veya başvuru hakkının yokluğu görünüyorsa → m. 276 ret kararı için; ret kararının tebliği ve tebliğden itibaren iki hafta içinde bölge adliye mahkemesinden karar istenebilmesi (m. 276/2).
5. **Tebliğ ve cevap:** reddedilmeyen dilekçe veya beyan tutanağının örneği karşı tarafa tebliğ edilir; iki hafta içinde yazılı cevap; karşı taraf sanıksa zabıt kâtibine beyanla da cevap verebilir (m. 277/1-2). Cumhuriyet savcısının istinaf istemi ilgililere tebliğ edilir; iki hafta içinde cevap (m. 273/5).
6. **Gönderme:** cevap verildikten veya süre bittikten sonra dosya bölge adliye mahkemesine gönderilir (m. 277/2). Süresi içinde yapılan başvuru hükmün kesinleşmesini engeller (m. 275/1).

## Akış — temyiz (bölge adliye mahkemesi kararına karşı)

1. Süre iki hafta, hükmün gerekçesiyle birlikte tebliğinden (m. 291/1); temyiz edilemeyen kararlar m. 286/2 (istisna suçlar m. 286/3).
2. Ret: süre geçmiş, temyiz edilemeyen hüküm veya hak yokluğunda temyiz istemi hükmü veren mahkemece reddedilir; tebliğden itibaren iki hafta içinde Yargıtay'dan karar istenebilir (m. 296).
3. Tebliğ ve cevap: iki hafta; dosya bölge adliye mahkemesince Yargıtay Cumhuriyet Başsavcılığına gönderilir (m. 297/1-2). Süresi içinde yapılan temyiz hükmün kesinleşmesini engeller (m. 293/1).

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Kanun yolu dosya formu:** | Başvuran ve sıfatı | Yol | Gerekçeli hüküm tebliğ tarihi | Başvuru tarihi ve şekli | Son gün (en erken) | Karşı tarafa tebliğ | Cevap süresi sonu | Tutuklu mu |
2. **Beyan tutanağı iskeleti:**

```
KANUN YOLU BEYAN TUTANAĞI
[DOLDUR] Mahkemesinin [DOLDUR] esas, [DOLDUR] karar sayılı hükmüne karşı
[DOLDUR — sıfatı] [istinaf / temyiz] yoluna başvurduğunu beyan etti.
Beyan okundu, imzası alındı. Tarih ve saat: [DOLDUR]
Beyan eden [imza]      Zabıt Kâtibi [imza]      Onaylayan Hâkim [imza]
```

3. **Üst yazı iskeleti** (bölge adliye mahkemesine; temyizde bölge adliye mahkemesince Yargıtay Cumhuriyet Başsavcılığına): dosya, başvurular, cevaplar, tutukluluk bilgisi, dizi listesi — [DOLDUR].

**Risk skalası:**
- 🔴 Sürenin tefhimden hesaplanması; cevap süresi beklenmeden gönderme; tutuklunun beyanının deftere kaydedilmemesi.
- 🟠 Ret kararı gerektirebilecek durumun hâkime sunulmaması; tutuklu dosyada gecikme.
- 🟡 Dizi listesi, emanet veya tebliğ mazbatası eksikleri.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: CMK m. 39, 260, 262, 263, 264, 272, 273, 274, 275, 276, 277, 286, 291, 293, 296, 297, 331 — bu sohbette çekildi mi, eşleşti mi. m. 295 mülgadır; atıf yapılmaz.
- Süre hesabı hatırlatmadır; son günü kalem ve hâkim teyit eder.
- ⚠️ "Ret kararları hükmü veren mahkemenindir; hâkim onayı şart."

## Sıradaki adımlar

- `/ceza-kalem:ceza-tebligat` — gerekçeli hükmün tebliği
- `/istinaf-kalem:dosya-kabul-kontrol` (bölge adliye mahkemesi kalemi)
- `/ceza-kalem:infaz-evraki` — kesinleşme sonrası

---

> 🚧 v1.0.0 — `ceza-kalem` 3 temel kalem skill'i; v1.2.0'da duruşma tutanağı ve kanun yolu gönderme eklendi (toplam 5). Kalıp: `hukuk-hakim__skills.md`.
