# istinaf-kalem — Skill Referans Kitapçığı

> Dal: İstinaf mahkemesi kalemi — bölge adliye mahkemesi hukuk ve ceza daireleri, bölge idare mahkemesi daireleri · Rol: **Kalem (daire yazı işleri)** · Usul: HMK 6100, CMK 5271, İYUK 2577 + Tebligat K. 7201
> Toplam skill: 3
> Kullanım: `/istinaf-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar kontrol listesi ve yazı iskeletidir; daire başkanı veya görevlendirilen üye havalesi ve heyet onayı şarttır. Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir. Süre hesapları hatırlatmadır; son günü kalem ve heyet teyit eder, bilinmeyen olguda en erken gün esas alınır. Her çıktı **TASLAK**.

## İçindekiler

- /istinaf-kalem:dosya-kabul-kontrol — istinaf dosyası daireye geldiğinde eksik kontrolü (hukuk, ceza, idari/vergi)
- /istinaf-kalem:geri-cevirme — eksikliklerin giderilmesi için ilk derece mahkemesine yazı (geri çevirme)
- /istinaf-kalem:karar-sonrasi-islemler — daire kararı sonrası tebliğ, kanun yolu başvurusu, dosyanın iadesi

---

## /istinaf-kalem:dosya-kabul-kontrol

---
name: dosya-kabul-kontrol
description: >
  İlk derece mahkemesinden gelen istinaf dosyasını tevzi ve ön incelemeden önce kalem
  gözüyle kontrol eder: karar ve tebliğler, istinaf ve cevap dilekçeleri, cevap
  süreleri, harç, ekler ve emanet, tutukluluk ve öncelik. Eksik listesi ile "tevzi /
  geri çevirme / heyete sunum" önerisi üretir.
user-invocable: true
---

# İstinaf Dosyası Kabul Kontrolü

## Konum hatırlatması

Kalem kontrolü hukuki değerlendirme değildir: süre aşımı, kesinlik veya başvuru hakkı gibi sonuç doğuran tespitler heyete sunulur, kalem karar vermez. Asistan UYAP'a bağlanmaz, kayıt eklemez ve dizi listesini göremez; kullanıcı UYAP'taki dosyadan bilgiyi aktarır. **Süre aşımı, kesinlik ve başvuru hakkına ilişkin her sonuç için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

İlk derece mahkemesinden gelen istinaf dosyasının tevzi ve ön incelemeye hazır olup olmadığını kalem gözüyle kontrol etmek; eksikleri listeleyip tevzi, geri çevirme veya heyete sunum önerisi üretmek.

## Girdi

- Dal (hukuk / ceza / idari-vergi) ve dosyanın geliş tarihi
- Dizi listesi özeti (UYAP'ta dosyadan)
- Karar, tebliğ mazbataları veya e-tebligat kayıtları (tarih ve muhatap)
- İstinaf dilekçeleri veya beyan tutanakları, cevaplar, harç makbuzları
- Tutukluluk bilgisi (ceza), YD istemi (idari)

## Kontrol listesi

**Ortak**

- [ ] Gerekçeli karar dosyada, imzalı, sayfaları tam; hüküm fıkrasında kanun yolu, mercii ve süre yazılı (HMK m. 297/1-ç; CMK m. 232/6; AY m. 40)
- [ ] Karar her taraf ve ilgiliye tebliğ edilmiş; her tebliğ için tarih ve muhatap (vekil varsa vekile — Tebligat K. m. 11); e-tebligatta elektronik adrese ulaşma tarihi (tebliğ, izleyen beşinci günün sonunda yapılmış sayılır — Tebligat K. m. 7/a)
- [ ] Tebliğ şerhleri usule uygun (Tebligat K. m. 21, 35); usulsüz tebliğde muhatabın beyan ettiği öğrenme tarihi (Tebligat K. m. 32)
- [ ] Her istinaf dilekçesi veya beyanı: tarih, verildiği yer, kayıt ve alındı (HMK m. 343; CMK m. 273/1 — beyan tutanağı hâkime onaylatılmış mı)
- [ ] Karşı tarafa tebliğ ve **cevap süresinin dolduğu** görülüyor (HMK m. 347/2: iki hafta; CMK m. 277/1: iki hafta; İYUK m. 48/3 ve m. 45/2: otuz gün). Süre dolmadan gelen dosya 🔴
- [ ] Cevapla yapılan başvuru (HMK m. 348; İYUK m. 48/3) ve buna karşı cevap süresi (HMK m. 348/1: iki hafta)
- [ ] İlk derece mahkemesince verilmiş ret veya "başvuru yapılmamış sayılma" kararı varsa tebliği ve buna karşı başvuru (HMK m. 344, 346; CMK m. 276; İYUK m. 48/6)
- [ ] Ekler, delil klasörleri, bilirkişi raporları, keşif tutanakları, birleşen dosyalar

**Hukuk ek**

- [ ] Harç ve giderler (HMK m. 344); eksikse ilk derece mahkemesinin bir haftalık kesin süre işlemi yapılmış mı
- [ ] Feragat beyanı var mı: dosya gönderilmeden önce ise ilk derece mahkemesi, gönderildikten sonra ise daire başvuruyu feragat nedeniyle reddeder (HMK m. 349/2) → heyete

**Ceza ek**

- [ ] Tutuklu sanık var mı → dosya öncelikli; tutuklama tarihi ve azami süre bilgisi heyete (CMK m. 102); dosya dairedeyken salıverilme istemi dosya üzerinden incelenir (m. 104/3)
- [ ] On beş yıl ve daha fazla hapis cezası → başvuru olmasa da resen inceleme (CMK m. 272/1)
- [ ] Tutuklunun zabıt kâtibine veya kurum müdürüne beyanı: defter kaydı ve tutanak (CMK m. 263)
- [ ] Teknik araçlarla kayda alınan duruşmalarda kaydın yazılı tutanağa dönüştürülüp imzalanmış olması (CMK m. 219/1)
- [ ] Emanet ve adli emanete alınan eşya listesi
- [ ] Tebligat eksikliği → daire tarafından giderilebilir (CMK m. 278); geri çevirme yerine dairece tamamlama heyete sunulur

**İdari / vergi ek**

- [ ] İvedi yargılama davası mı (İYUK m. 20/A) → istinaf yolu yok (m. 45/8); yanlış merciye gelen dosya heyete
- [ ] YD istemi var mı; ilk derece YD kararına itiraz ayrı mı yürüyor (m. 27/7)
- [ ] Dava tarihi ve uyuşmazlık miktarı (kesinlik değerlendirmesi heyete — m. 45/1, Ek m. 1)

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

```
İSTİNAF DOSYASI KABUL KONTROL FORMU
Daire: [DOLDUR]                       Geliş tarihi: [DOLDUR]
İlk derece: [DOLDUR mahkeme] E. [DOLDUR] K. [DOLDUR]   Karar tarihi: [DOLDUR]
Dal: [hukuk / ceza / idari / vergi]   Tutuklu: [evet/hayır]   YD istemi: [evet/hayır]

Taraf / ilgili | Karar tebliğ tarihi | Başvuru tarihi | Cevap için tebliğ | Cevap süresi sonu (en erken) | Durum
[DOLDUR]       | [DOLDUR]            | [DOLDUR]       | [DOLDUR]          | [DOLDUR]                      | [✓/✗]

Eksikler: 1) [DOLDUR] (dayanak: [çekilen madde])  2) [DOLDUR]
Öneri: [tevzi / geri çevirme / heyete sunum (süre, kesinlik, başvuru hakkı tespiti)]
Hazırlayan: [rol]            Havale: [daire başkanı / görevlendirilen üye]
```

**Risk skalası:**
- 🔴 Cevap süresi dolmadan gelen dosya; bir tarafa tebliğ yok veya usulsüz; tutuklu dosyada gecikme.
- 🟠 Harç eksikliği işleminin ilk derece mahkemesince tamamlanmamış olması; ret kararının tebliğ edilmemesi.
- 🟡 Ek, emanet veya tutanak eksikleri.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: AY m. 40; HMK m. 297, 343, 344, 346, 347, 348, 349; CMK m. 102, 104, 219, 232, 263, 272, 273, 276, 277, 278; İYUK m. 20/A, 27, 45, 48, Ek m. 1; Tebligat K. m. 7/a, 11, 21, 32, 35 — bu sohbette çekildi mi, eşleşti mi.
- Süre hesabı hatırlatmadır: HMK m. 92-93 ve adli tatil m. 104; CMK m. 39 ve m. 331/4; İYUK m. 8. Son günü kalem ve heyet teyit eder.
- ⚠️ "Süre aşımı, kesinlik ve başvuru hakkı tespitleri heyete sunulur; kalem karar vermez."

## Sıradaki adımlar

- `/istinaf-kalem:geri-cevirme`
- `/istinaf-hakim:hukuk-on-inceleme`, `/istinaf-hakim:ceza-istinaf-inceleme`, `/istinaf-hakim:idari-istinaf`
- `/ceza-hakim:tutukluluk-incelemesi` (tutuklu dosya)

---

## /istinaf-kalem:geri-cevirme

---
name: geri-cevirme
description: >
  Daireye gelen istinaf dosyasındaki eksikliklerin giderilmesi için ilk derece
  mahkemesine yazılacak geri çevirme (eksiklik) yazısının iskeletini üretir: eksikliğin
  tam tanımı, muhatap, dayanak, beklenen işlem ve sürelerin beklenmesi. Geri çevirme
  kararı heyetindir; kalem yazıyı hazırlar.
user-invocable: true
---

# Geri Çevirme (Eksiklik) Yazısı

## Konum hatırlatması

Geri çevirme dosyanın incelemesini geciktirir; tutuklu işlerde ve kısa süreli işlerde öncelik ve alternatif (dairece giderme) heyete sunulur. Yazı taraflardan birini kayıran veya esasa ilişkin görüş bildiren ifade içermez; yalnız usul eksikliğini tanımlar. Asistan UYAP'ta yazı oluşturmaz. **Geri çevirme kararı için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

Heyetin geri çevirme kararı üzerine ilk derece mahkemesine yazılacak yazının iskeletini, eksikliği açıkça tanımlayan ve beklenen işlemi gösteren biçimde hazırlamak.

## Dayanak (bu sohbette çekilir)

- **Hukuk:** ön incelemede eksiklik tespit edilirse öncelikle gerekli karar verilir (HMK m. 352/1); dosya dilekçeler verildikten veya bunun için belli süreler geçtikten sonra gönderilir (m. 347/3); harç ve gider eksikliği kararı veren mahkemece bir haftalık kesin süreyle tamamlatılır (m. 344).
- **Ceza:** daire, varsa tebligat eksikliklerinin giderilmesini sağlar (CMK m. 278); tebligat eksikliği dairece de giderilebilir.
- **İdari/vergi:** istinaf temyizin şekil ve usullerine tabidir (İYUK m. 45/2); dilekçe eksikliği için on beş gün (m. 48/2), harç ve gider için yedi gün (m. 48/6).
- "Geri çevirme" uygulamada kullanılan terimdir; yazının biçim ve usulüne ilişkin yönetmelik hükümleri bu sohbette çekilemedi: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## Girdi

- Heyetin geri çevirme kararı ve eksiklik tespiti [DOLDUR]
- İlk derece mahkemesi, esas ve karar numarası [DOLDUR]
- Eksikliğin türü: tebligat, cevap süresi, harç, tutanak veya karar örneği, ek belge [DOLDUR]
- Dosyanın tutuklu veya öncelikli iş olup olmadığı [DOLDUR]
- Dosya bilgisi kullanıcıdan gelir; asistan UYAP'a bağlanmaz, kayıt eklemez.

## Tipik eksiklik kataloğu

| Kod | Eksiklik | Beklenen işlem | Dayanak |
|---|---|---|---|
| T1 | Gerekçeli karar bir tarafa tebliğ edilmemiş veya mazbata okunaksız | Usulüne uygun tebliğ ve mazbatanın eklenmesi | HMK m. 345; CMK m. 273/1; İYUK m. 45/1; Tebligat K. m. 21 |
| T2 | e-Tebligat kaydında elektronik adrese ulaşma tarihi yok | Kaydın eklenmesi | Tebligat K. m. 7/a |
| T3 | İstinaf dilekçesi karşı tarafa tebliğ edilmemiş | Tebliğ ve cevap süresinin beklenmesi | HMK m. 347; CMK m. 277; İYUK m. 48/3 |
| T4 | Cevapla yapılan başvuruya karşı cevap süresi beklenmemiş | Tebliğ ve sürenin beklenmesi | HMK m. 348/1; İYUK m. 48/3 |
| H1 | İstinaf harç ve giderleri eksik | Kesin süreli bildirim ve sonucuna göre karar | HMK m. 344; İYUK m. 48/6 |
| R1 | İlk derece ret kararı (süre / kesinlik) tebliğ edilmemiş | Tebliğ ve başvuru süresinin beklenmesi | HMK m. 346; CMK m. 276; İYUK m. 48/6 |
| D1 | Gerekçeli karar imzasız veya eksik sayfalı | Tamamlanması | HMK m. 297/1-d; CMK m. 232/4 |
| D2 | Teknik araçlarla kaydedilen duruşma yazılı tutanağa dönüştürülmemiş | Dönüştürülüp imzalanması | CMK m. 219/1 |
| D3 | Ekler, delil klasörü, emanet listesi, birleşen dosya eksik | Gönderilmesi | [DOLDUR — dizi listesi] |

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

```
T.C.
[DOLDUR] BÖLGE [ADLİYE / İDARE] MAHKEMESİ
[DOLDUR]. [HUKUK / CEZA / İDARİ DAVA / VERGİ DAVA] DAİRESİ

Daire esas no: [DOLDUR]                                    Tarih: [DOLDUR]
Konu: İstinaf dosyasındaki eksikliklerin giderilmesi

[DOLDUR] MAHKEMESİNE

İlgi: Mahkemenizin [DOLDUR] esas, [DOLDUR] karar sayılı dosyası.

Mahkemenizce verilen karara karşı yapılan istinaf başvurusu üzerine Dairemize
gönderilen dosyanın incelenmesinde aşağıdaki eksikliklerin bulunduğu anlaşılmıştır:

1. [DOLDUR — eksiklik: hangi belge, hangi taraf veya ilgili, hangi usul] (dayanak: [çekilen madde])
2. [DOLDUR]

Belirtilen eksikliklerin giderilmesinden [ve ilgili cevap / başvuru sürelerinin
dolmasından] sonra dosyanın dizi listesine bağlı olarak Dairemize yeniden gönderilmesi
rica olunur.

[Onay: Daire Başkanı / görevlendirilen üye — DOLDUR]
[Yazı işleri müdürü — DOLDUR]
```

- **Tutuklu dosya notu:** geri çevirme yerine dairece giderme (CMK m. 278) ve öncelik heyete sunulur.
- **Takip satırı:** geri çevirme tarihi, beklenen dönüş, dönüşte yeniden kabul kontrolü (`/istinaf-kalem:dosya-kabul-kontrol`).

**Risk skalası:**
- 🔴 Tebliğ veya cevap süresi eksikliği giderilmeden incelemeye geçilmesi; tutuklu dosyada gereksiz geri çevirme.
- 🟠 Eksikliğin belirsiz tanımlanması (ilk derece mahkemesi neyi tamamlayacağını anlayamaz) → ikinci geri çevirme.
- 🟡 Dayanak gösterilmemesi.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 297, 344, 345, 346, 347, 348, 352; CMK m. 219, 232, 273, 276, 277, 278; İYUK m. 45, 48; Tebligat K. m. 7/a, 21 — bu sohbette çekildi mi, eşleşti mi.
- Geri çevirmeye ilişkin yönetmelik hükmü: UYARI satırı (yukarıda).
- Süre hesapları hatırlatmadır; son günü hâkim/kalem teyit eder. Tebliğ tarihi gibi bilinmeyen bir olguda en erken olası gün esas alınır ve bu açıkça uyarı olarak yazılır.
- ⚠️ "Geri çevirme kararı heyetindir; yazı onay olmadan gönderilmez."

## Sıradaki adımlar

- `/istinaf-kalem:dosya-kabul-kontrol` — dönüşte yeniden kontrol
- `/istinaf-hakim:hukuk-on-inceleme` (hukuk) — eksiklik giderilince ön inceleme

---

## /istinaf-kalem:karar-sonrasi-islemler

---
name: karar-sonrasi-islemler
description: >
  Daire kararından sonra kalem işlemlerini sıralar: kararın kimin tarafından tebliğe
  çıkarılacağı, temyiz dilekçesinin alınması ve karşı tarafa tebliği, temyize gönderme,
  temyize açık olmayan kararlarda dosyanın ilk derece mahkemesine iadesi ve kesinleşme
  kaydının yeri. Hukuk, ceza ve idari/vergi için ayrı akış.
user-invocable: true
---

# Karar Sonrası İşlemler — Tebliğ, Kanun Yolu, Dosyanın İadesi

## Konum hatırlatması

Temyiz edilebilirlik, süre aşımı ve ret kararları yetkili merciin işidir; kalem akışı hazırlar ve sunar. Asistan UYAP'ta tebligat çıkarmaz, kayıt kapatmaz. **Temyiz edilebilirlik, süre ve ret konularında hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

Daire kararından sonraki tebliğ, kanun yolu başvurusu ve dosyanın iadesi işlemlerini hukuk, ceza ve idari/vergi dosyaları için ayrı akışlarla sıralamak.

## Girdi

- Daire kararı: tarih, türü (esastan ret, kaldırma, bozma, düzelterek ret, yeniden hüküm), temyiz edilebilirlik notu
- Taraflar ve vekiller, tebligat yöntemi (e-tebligat zorunlu muhatap mı — Tebligat K. m. 7/a)
- Varsa temyiz dilekçeleri ve tarihleri

## Akış

**Hukuk (bölge adliye mahkemesi hukuk dairesi)**

1. **Tebliğ:** temyizi kabil olmayan kararlar ilk derece mahkemesince, temyizi kabil olanlar bölge adliye mahkemesince resen tebliğe çıkarılır (HMK m. 359/4).
2. **Temyiz süresi:** tebliğ tarihinden itibaren iki hafta (m. 361/1). Temyiz edilemeyen kararlar m. 362'dedir (m. 353/1-a kapsamındaki kaldırma kararları dâhil — m. 362/1-g); parasal sınır Ek m. 1 ile güncellenir.
3. **Temyiz dilekçesi:** kararı veren bölge adliye mahkemesi dairesine veya m. 365/1'de sayılan yerlere verilebilir; başka yere verilmişse temyiz defterine kaydedilir ve kararı temyiz edilen mahkemeye derhâl bildirilir (m. 365). İstinafa ilişkin m. 343-349 ve 352 temyizde kıyasen uygulanır (m. 366): karşı tarafa tebliğ, cevap, harç, ret kararları.
4. **İade ve kesinleşme:** kanun yollarından geçerek kesinleşen kararların kesinleşme kaydı ve yerine getirme bildirimleri ilk derece mahkemesince yapılır (m. 302/5).

**Ceza (bölge adliye mahkemesi ceza dairesi)**

1. **Açıklama ve tebliğ:** ilgili tarafın yüzüne karşı verilen karar kendisine açıklanır; koruma tedbirlerine ilişkin olanlar hariç, aleyhine kanun yoluna başvurulabilecek kararlar hazır bulunamayan ilgilisine tebliğ olunur (CMK m. 35).
2. **Temyiz edilebilirlik:** m. 286 (temyiz edilemeyen bölge adliye mahkemesi kararları m. 286/2; istisna suçlar m. 286/3). Temyiz süresi iki hafta, hükmün gerekçesiyle birlikte tebliğ edildiği tarihten (m. 291/1).
3. **Temyiz istemi:** dilekçe veya zabıt kâtibine beyan; tutuklu için m. 263. Süre geçmiş, temyiz edilemeyen hüküm veya hak yokluğunda temyiz istemi hükmü veren bölge adliye mahkemesince reddedilir; ret kararına karşı tebliğden itibaren iki hafta içinde Yargıtay'dan karar istenebilir (m. 296).
4. **Tebliğ ve cevap:** reddedilmeyen temyiz dilekçesinin örneği karşı tarafa tebliğ edilir, iki hafta içinde yazılı cevap verilebilir; sonra dosya bölge adliye mahkemesince Yargıtay Cumhuriyet Başsavcılığına gönderilir (m. 297/1-2).
5. **Kesinleşen karar:** dosya ilk derece mahkemesine; infaz işlemleri → `/ceza-kalem:infaz-evraki`.

**İdari / vergi (bölge idare mahkemesi dairesi)**

1. **Temyize açık olmayan kararlar:** kesindir; dosyayla birlikte kararı veren ilk derece mahkemesine gönderilir ve bu mahkemece yedi gün içinde tebliğe çıkarılır (İYUK m. 45/6).
2. **Temyize açık kararlar:** m. 46; süre kararın tebliğinden itibaren otuz gün. Temyiz dilekçesi m. 48'e göre kararı veren bölge idare mahkemesine veya m. 48/3'te sayılan mercilere verilir ve karşı tarafa tebliğ edilir; otuz gün içinde cevap; cevap veren kararı süresinde temyiz etmemiş olsa bile cevap dilekçesinde temyiz isteminde bulunabilir; dosya dizi listesine bağlı olarak Danıştay'a gönderilir (m. 48/4); YD istemli temyiz dilekçeleri karşı tarafa tebliğ edilmeden gönderilir (m. 48/5); harç ve gider için yedi günlük süre (m. 48/6).
3. **Danıştay kararından sonra:** karar dosyayla kararı veren mercie gönderilir; onamaya ilişkin kararlar dosyayla birlikte ilk derece mahkemesine, örneği bölge idare mahkemesine gönderilir ve dosyanın gelişinden itibaren yedi gün içinde tebliğe çıkarılır (m. 50/1).
4. **Uygulama:** idare kararın gereğini gecikmeksizin ve kararın idareye tebliğinden itibaren en geç otuz gün içinde yerine getirir (m. 28/1) → `/idari-kalem:karar-uygulama-takip`, `/vergi-kalem:karar-uygulama-iade`.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **İşlem akış tablosu:** adım — sorumlu birim (daire / ilk derece mahkemesi) — dayanak — tarih [DOLDUR] — durum.
2. **Tebliğ planı:** muhatap, yöntem (e-tebligat / posta), belge (gerekçeli karar), süre başlangıcı.
3. **Süre takip tablosu:** her muhatap için tebliğ tarihi → son gün (en erken ihtimal) → "teyit edildi" sütunu.
4. **Dosya iade üst yazısı iskeleti:**

```
[DOLDUR] MAHKEMESİNE
Dairemizin [DOLDUR] esas, [DOLDUR] karar sayılı ve [DOLDUR] tarihli kararı ile
Mahkemenizin [DOLDUR] esas, [DOLDUR] karar sayılı dosyası dizi listesine bağlı olarak
iade edilmiştir. [Temyize açık olmayan kararın tebliği / kesinleşme kaydı ve
bildirimleri Mahkemenizce yapılacaktır — dayanak: DOLDUR]
[Onay — DOLDUR]
```

**Risk skalası:**
- 🔴 Temyizi kabil kararın ilk derece mahkemesince tebliğe çıkarılması veya tersi (süre başlangıcı tartışmalı hâle gelir); ceza temyizinde sürenin tefhimden hesaplanması.
- 🟠 Temyiz dilekçesine cevap süresi beklenmeden gönderme; YD istemli dilekçenin tebliğ sırasının gözetilmemesi.
- 🟡 Dizi listesi veya örnek eksikleri.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 302, 343-349, 352, 353, 359, 361, 362, 365, 366, Ek m. 1; CMK m. 35, 263, 286, 291, 296, 297; İYUK m. 28, 45, 46, 48, 50; Tebligat K. m. 7/a — bu sohbette çekildi mi, eşleşti mi.
- Süre hesapları hatırlatmadır (HMK m. 92-93, 104; CMK m. 39, 331/4; İYUK m. 8); son günü kalem ve heyet teyit eder.
- ⚠️ "Temyiz edilebilirlik ve ret kararları yetkili merciindir."

## Sıradaki adımlar

- `/hukuk-kalem:kesinlesme-serhi` (ilk derece mahkemesinde kesinleşme)
- `/ceza-kalem:kanun-yolu-gonderme`, `/idari-kalem:kanun-yolu-gonderme`

---

> v1.2.0 — `istinaf-kalem` 3 kalem skill'i. Kalıp: `hukuk-hakim__skills.md`. Detay: `tebligat-7201-rehberi.md`, `uyap-rehberi.md`.
