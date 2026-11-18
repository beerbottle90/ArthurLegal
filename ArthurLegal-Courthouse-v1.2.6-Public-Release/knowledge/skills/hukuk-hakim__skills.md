# hukuk-hakim — Skill Referans Kitapçığı

> Dal: Hukuk mahkemesi · Rol: **Hâkim** · Usul: HMK 6100
> Toplam skill: 7
> Kullanım: `/hukuk-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Çıktılar gerekçe ve usulü yapılandırır; karar hâkimindir. Her çıktı **TASLAK — hâkim/heyet onayı şart**.

## İçindekiler

- /hukuk-hakim:gerekceli-karar — HMK m. 297 yapısında gerekçeli karar iskeleti
- /hukuk-hakim:on-inceleme — HMK m. 137-142 ön inceleme tutanağı & kontrol
- /hukuk-hakim:delil-degerlendirme — HMK m. 187 vd. ispat yükü & delil takdiri metodu
- /hukuk-hakim:ihtiyati-tedbir — HMK m. 389-399 geçici hukuki koruma değerlendirmesi
- /hukuk-hakim:ara-karar — duruşma ara kararı; HMK m. 94 kesin süre ve ihtarat, kanuni sonuçlu süreler
- /hukuk-hakim:bilirkisi-raporu-denetimi — HMK m. 266-282 ve 293 bilirkişi raporu denetimi, itiraz, ek rapor, yeni bilirkişi
- /hukuk-hakim:dava-sarti-kontrolu — HMK m. 114-115 dava şartları ve dava şartı arabuluculuk alanları

---

## /hukuk-hakim:gerekceli-karar

---
name: gerekceli-karar
description: >
  Bir hukuk uyuşmazlığında HMK m. 297'ye uygun gerekçeli karar iskeleti üretir:
  taraf iddiaları, uyuşmazlık konusu, delil değerlendirmesi, uygulanacak norm ve
  hukuki gerekçe ayrı ayrı yapılandırılır. Sonucu DAYATMAZ; gerekçenin iskeletini kurar.
user-invocable: true
---

# Gerekçeli Karar — HMK m. 297 İskeleti

## Konum hatırlatması

Sen tarafsızsın. Bu skill **kararı yazmaz**, kararın **gerekçe iskeletini** kurar. Sonuç (kabul/ret/kısmen kabul) **hâkim/heyet takdiridir**. İki tarafı dengeli sun.

## Girdi

Kullanıcı şunları sağlamalı (eksikse iste, varsayma):
- Dava türü (eda / tespit / inşai) ve talep
- Tarafların temel iddiaları (davacı + davalı)
- Toplanan deliller (belge, tanık, bilirkişi, keşif)
- Varsa bilirkişi raporu sonucu ve itirazlar

## Çıktı yapısı — HMK m. 297 unsurları

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Başlık & taraflar** — mahkeme, esas no, taraflar ve vekilleri (kalıp; `[DOLDUR]`).
2. **Dava ve talep** — davacının talebi, hukuki sebep (1-2 cümle özet).
3. **Savunma** — davalının savunması ve karşı talepleri.
4. **Uyuşmazlık konusu** — tarafların üzerinde anlaştığı ve çekiştiği noktalar ayrı ayrı.
5. **Deliller ve değerlendirilmesi** — her delil için: ne ispatlıyor, çekişme var mı (HMK m. 187), ispat yükü kimde (HMK m. 190). Bilirkişi raporu varsa: rapor sonucu + itirazların karşılanması.
6. **Gerekçe** — uygulanacak norm (MCP'den `[ArthurLegal TR — GG.AA.YYYY]`) + varsa emsal içtihat (`[ArthurLegal TR — kurum — Esas/Karar — GG.AA.YYYY]`) + somut olaya uygulama. **İki yönlü:** kabul gerekçesi ile ret gerekçesi ayrı ayrı kurulur; hangisinin daha güçlü olduğunu hâkim takdir eder.
7. **Hüküm (iskelet)** — HMK m. 297/1-ç (hüküm sonucu, yargılama giderleri, avansın iadesi, kanun yolu ve süresi) ve m. 297/2 (her talep hakkında sıra numaralı, açık hüküm) unsurları: talep kalemleri tek tek, vekâlet ücreti, yargılama gideri, kanun yolu/süre. **Sonuç boş bırakılır veya seçenekli sunulur.**

## Adımlar

1. **Usulü önce kontrol et.** Görev/yetki, dava şartları (HMK m. 114-115), husumet, derdestlik/kesin hüküm. Engel varsa 🔴/🟠 flag'le ve esasa geçme.
2. **Uyuşmazlığı daralt.** Çekişmesiz vakıaları ayır (ispat gerektirmez, HMK m. 187/2).
3. **İspat yükünü dağıt.** Her çekişmeli vakıa için kim ispatla yükümlü (m. 190) ve ispat edildi mi.
4. **Normu MCP'den çek.** İlgili TBK/TMK/TTK/HMK maddelerini verbatim al, atıf et. Çekmeden madde numarası yazma.
5. **Emsal varsa** ArthurLegal MCP (`tr_`)'den çek; yoksa "emsal teyidi gerekir" notu düş.
6. **İki yönlü gerekçe** kur, sonucu dayatma.

## İnceleyen notu (çıktının sonunda)

- Kullanılan normlar ve içtihat (atıflı)
- Teyit gereken noktalar (`UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>`)
- ⚠️ "Sonuç ve takdir hâkime/heyete aittir."

## Sıradaki adımlar (öner)

- `/hukuk-hakim:delil-degerlendirme` — ispat yükü derinleştirme
- Emsal içtihat taraması (ArthurLegal MCP (`tr_`))
- Bilirkişi raporuna itirazların ayrı değerlendirmesi (`bilirkisilik-rehberi.md`)

---

## /hukuk-hakim:on-inceleme

---
name: on-inceleme
description: >
  HMK m. 137-142 ön inceleme aşaması için kontrol listesi ve tutanak iskeleti:
  dava şartları, ilk itirazlar, sulh/arabuluculuk teşviki, uyuşmazlık noktalarının
  tespiti, tahkikata hazırlık.
user-invocable: true
---

# Ön İnceleme — HMK m. 137-142

## Amaç

Ön inceleme duruşması öncesi/sırasında hâkimin kontrol etmesi gerekenleri **eksiksiz** yapılandır. Bu aşama atlanırsa tahkikat sakatlanır.

## Kontrol listesi

1. **Dava şartları (m. 114) — re'sen:** görev, yetki (kesin mi), hukuki yarar, taraf/dava ehliyeti, derdestlik, kesin hüküm. 🔴 eksikse dava usulden ret.
2. **İlk itirazlar (m. 116-117):** yetki (kesin değilse) ve tahkim itirazı — **cevap dilekçesinde** ileri sürülmüş mü (m. 117/1); süresinde değilse dinlenmez. (İş bölümü itirazı m. 116/1-c'den 7251 s. K. ile kaldırılmıştır; artık ilk itiraz değildir.)
3. **TTK m. 5/A dava şartı arabuluculuk:** ticari davalardan konusu bir miktar para olan alacak, tazminat, itirazın iptali, menfi tespit veya istirdat davasıysa (TTK m. 5/A/1 — 7445 s. K. ile genişletilmiş hâli) dava açılmadan önce arabulucuya başvurulmuş mu. 🔴 değilse dava şartı yokluğundan ret.
4. **Sulh ve arabuluculuk teşviki (m. 140/2):** tarafları teşvik et, tutanağa geçir.
5. **Uyuşmazlık noktalarının tespiti (m. 140/1):** çekişmeli/çekişmesiz vakıalar ayrılır — tahkikatın sınırını çizer.
6. **Delil gösterme & sunma süresi (m. 140/5, 145):** taraflara kesin süre; sonradan delil sınırlı.

## Çıktı

Ön inceleme tutanağı iskeleti (`[DOLDUR]` alanlı) + 🔴🟠🟡 işaretli eksiklik listesi. Üst başlık TASLAK ibareli.

---

## /hukuk-hakim:delil-degerlendirme

---
name: delil-degerlendirme
description: >
  HMK m. 187 vd. çerçevesinde ispat yükü dağılımı ve delil takdiri metodu:
  hangi vakıa ispat gerektirir, yük kimde, deliller nasıl tartılır, bilirkişi
  raporu nasıl değerlendirilir. Takdiri DAYATMAZ; ölçüt sunar.
user-invocable: true
---

# Delil Değerlendirme — İspat Yükü & Takdir Metodu

## Amaç

Delil takdirini **yöntemli** hale getir. Sonucu söyleme; hâkimin vicdani kanaatine (HMK m. 198 serbest delil takdiri, senette m. 200 sınır) **ölçüt** sun.

## Yöntem

1. **Vakıaları ayır:** çekişmeli mi, çekişmesiz mi (m. 187/2 — çekişmesiz ispat gerektirmez).
2. **İspat yükü (m. 190):** kural — iddia eden ispatla yükümlü. Karine/aksi ispat hâlleri ayrıca işaretle.
3. **Delil türü sınırları:**
   - Senetle ispat zorunluluğu (m. 200/1) ve istisnaları (hatırlatma üzerine karşı tarafın açık muvafakati m. 200/2; delil başlangıcı m. 202; diğer istisnalar m. 203).
   - Tanıkla ispat sınırı (senede karşı tanık yasağı, m. 201).
   - Kesin deliller (senet, yemin, kesin hüküm) ↔ takdiri deliller (tanık, bilirkişi, keşif, özel uzman görüşü m. 293).
4. **Bilirkişi raporu (m. 266 vd.):** rapor hâkimi bağlamaz; teknik/özel bilgi alanı mı, denetime elverişli mi, itirazlar karşılandı mı. Çelişki varsa ek rapor/yeni bilirkişi. Detay: `bilirkisilik-rehberi.md`.
5. **Belgenin ibrazı (m. 219-220):** karşı tarafın elindeki belge — ibraz etmezse aleyhe takdir karinesi.

## Çıktı

Vakıa × delil × ispat-yükü tablosu + her çekişmeli vakıa için "ispat edildi / edilmedi / eksik" ölçütlü değerlendirme. **Sonuç hâkim takdirine bırakılır.**

---

## /hukuk-hakim:ihtiyati-tedbir

---
name: ihtiyati-tedbir
description: >
  HMK m. 389-399 geçici hukuki koruma: ihtiyati tedbir talebinin şartları
  (yaklaşık ispat + tedbir sebebi), teminat, tedbir türü ve ölçülülük
  değerlendirmesi. Tedbiri DAYATMAZ; ölçüt sunar.
user-invocable: true
---

# İhtiyati Tedbir — HMK m. 389-399

## Konum hatırlatması

Geçici koruma istisnaidir ve **gerekçeli** olmalıdır. Uyuşmazlık konusu hakkında esası çözer nitelikte tedbir kural olarak verilemez. Karar hâkimindir.

## Şartlar

1. **Tedbir sebebi (m. 389):** mevcut durumda meydana gelebilecek değişiklik nedeniyle hakkın elde edilmesinin önemli ölçüde zorlaşması / imkânsızlaşması veya gecikmede sakınca / ciddi zarar.
2. **Yaklaşık ispat (m. 390/3):** talep eden, davanın esası yönünden haklılığını **yaklaşık** ispatla yükümlü (kesin ispat aranmaz).
3. **Teminat (m. 392):** kural olarak teminat karşılığı (m. 392/1); istisnaları: talep resmî belgeye veya başkaca kesin delile dayanıyorsa ya da durum ve koşullar gerektiriyorsa gerekçesi açıkça belirtilerek teminat alınmayabilir; adli yardımdan yararlanan teminat göstermez. Kamu kurumlarına özel kanunlarla tanınan teminat muafiyetleri (ör. 6362 s. SPKn m. 92/3) saklıdır.

## Adımlar

1. Talebin türü ve dayanağı (m. 389) — neye yönelik tedbir.
2. Yaklaşık ispat değerlendirmesi (m. 390/3).
3. **Ölçülülük:** talep edilen tedbir korunacak hakla orantılı mı; esası çözer nitelikte mi (aşırı tedbir riski).
4. Teminat (m. 392) + tedbir kararının içeriği (m. 391).
5. **Karşı tarafın dinlenmesi:** kural; gecikmesinde sakınca varsa dinlenmeden (sonra itiraz — m. 394).
6. **Tamamlayıcı işlemler:** uygulama + esas dava süreleri (m. 393, 397).

## Çıktı

Şart-şart değerlendirme + teminat + tedbir türü önerisi (seçenekli) + somut gerekçe iskeleti. İtiraz yolu (m. 394) ve haksız tedbir tazminatı (m. 399) notu. Karar hâkimindir. TASLAK ibareli.

---

## /hukuk-hakim:ara-karar

---
name: ara-karar
description: >
  Duruşma ara kararlarını HMK çerçevesinde yapılandırır: her ara karar kaleminde
  muhatap, yapılacak işlem, süre ve kesin olup olmadığı, sürenin başlangıcı, kanuni
  sonuç ve ihtarın tutanağa geçirilmesi. Hak kaybı doğuran kesin süre ve ihtaratı
  özellikle denetler. Kararı VERMEZ; ara karar iskeleti kurar.
user-invocable: true
---

# Duruşma Ara Kararı — Kesin Süre ve İhtarat

## Konum hatırlatması

Ara kararlar iki tarafa eşit mesafede kurulur; aynı türde işlem için taraflara aynı açıklıkta süre ve ihtar verilir. Kesin sürenin sonucu hak kaybıdır; **hak kaybı doğuran her ara karar için hâkim/heyet takdiri ve onayı şarttır.** Asistan UYAP'ta ara karar oluşturmaz.

## Amaç

Duruşmada verilecek ara kararları, her muhatabın ne yapacağını, hangi sürede ve hangi sonuçla yapacağını açıkça gösteren kalemler hâlinde kurmak; hak kaybına yol açabilecek kesin süre ve ihtarları hâkimin önüne ayrıca koymak.

## Dayanak (bu sohbette çekilir)

- **HMK m. 94** — kanunun belirlediği süreler kesindir; hâkim tayin ettiği sürenin kesin olduğuna karar verebilir; bu takdirde kesin süreye konu işlemi hiçbir duraksamaya yer vermeyecek şekilde açıklar ve süreye uyulmamasının hukuki sonuçlarını açıkça tutanağa geçirerek ihtar eder; kesin olduğu belirtilmeyen süreyi geçiren taraf yeniden süre isteyebilir, ikinci süre kesindir; kesin süre içinde yapılmayan işlemi yapma hakkı ortadan kalkar.
- **HMK m. 90** — hâkim kendi tespit ettiği süreleri haklı sebeplerle artırabilir veya eksiltebilir; kanundaki süreleri, kanunda belirtilen istisnalar dışında değiştiremez. **m. 95** — elde olmayan sebeplerle kesin süreyi kaçıran için eski hâle getirme.
- **HMK m. 31, 32** — hâkimin davayı aydınlatma ödevi; yargılamanın sevk ve idaresi.
- **Kanuni sonuçlu tipik süreler:** gider avansının yetersizliği — iki haftalık kesin süre (m. 120/2); delil avansı — kesin süre, yatırılmazsa delil ikamesinden vazgeçilmiş sayılma (m. 324); ön inceleme davetiyesindeki belge ihtarı ve delile dayanmaktan vazgeçmiş sayılma (m. 139/1-ç, 140/5); giderilebilir dava şartı noksanlığı için kesin süre (m. 115/2); belgenin ibrazı için kesin süre ve ibraz edilmemesinin sonucu (m. 220); tanık adresi için kesin süre, gösterilmezse tanığın dinlenmesinden vazgeçilmiş sayılma (m. 240/3); sonradan delil gösterme (m. 145).
- **Tutanak:** ara kararları mutlak olarak tutanağa yazılır (m. 154/3-ğ).
- **Duruşma aralığı:** duruşmalar arasındaki süre üç aydan uzun olamaz; bilirkişi incelemesinin uzaması veya istinabe gibi zorunlu hâllerde hâkim gerekçesini belirterek daha uzun süre belirleyebilir (m. 147/3).
- **Duruşmaya gelmeme:** usulüne uygun davete rağmen gelmemenin sonuçları ve işlemden kaldırma (m. 150).
- **Kanun yolu:** HMK m. 341/1 istinafa tabi kararları sayar (nihai kararlar; ihtiyati tedbir ve ihtiyati hacizle ilgili belirli kararlar); ara kararlar için bu maddede ayrıca istinaf yolu öngörülmemiştir.

## Girdi

- Duruşmanın aşaması (ön inceleme / tahkikat / sözlü yargılama), hazır olanlar
- Her ara karar kalemi için amaç (delil toplama, bilirkişi, keşif, avans, müzekkere, tanık, belge ibrazı)
- Tarafların talepleri ve itirazları; reddedilecek talepler

## Kontrol listesi (her kalem için)

1. **Muhatap:** davacı / davalı / vekil / kurum — açık.
2. **İşlem:** ne yapılacak, hangi belge, hangi tutar, hangi adres — "hiçbir duraksamaya yer vermeyecek" açıklıkta (m. 94/2).
3. **Süre:** kaç gün veya hafta; **kesin mi?** Kanuni kesin süre mi, hâkimin belirlediği kesin süre mi.
4. **Başlangıç:** hazır olan taraf için tefhim; hazır olmayan tarafa kesin süre ve sonuç ihtarı ancak ara kararın tebliğiyle ulaşır → tebliğ satırı eklenir, süre tebliğ tarihinden izlenir.
5. **Sonuç:** yalnız kanunda öngörülen sonuç yazılır (m. 94/3, 120/2, 139/1-ç, 140/5, 220/3, 240/3, 324/2). Kanunda karşılığı olmayan yaptırım yazılmaz.
6. **İhtar:** sonuç tutanağa açıkça geçirilir (m. 94/2; 154/3-ğ).
7. **Talep reddi:** reddedilen delil ve taleplerde kısa gerekçe (çelişmeli yargılama).
8. **Sonraki duruşma:** tarih ve m. 147/3 kontrolü.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

```
ARA KARAR (TASLAK)
1- [Muhatap]'a, [işlem]'i yapması için tefhimden / tebliğden itibaren [süre] KESİN SÜRE
   verilmesine; bu süre içinde [işlem] yapılmadığı takdirde [kanuni sonuç — HMK m. …]
   hususunun İHTARINA (ihtar tutanağa geçirildi, HMK m. 94/2),
2- [Kurum]'a müzekkere yazılarak [bilgi/belge]'nin [süre] içinde gönderilmesinin
   istenmesine,
3- [Taraf]'ın [talep]'inin, [kısa gerekçe] nedeniyle reddine,
4- Duruşmanın [tarih] günü saat [saat]'e bırakılmasına (duruşma aralığı: HMK m. 147/3).
```

**Kalem × kontrol tablosu:** | Kalem | Muhatap | Süre / kesin mi | Başlangıç (tefhim / tebliğ) | Kanuni sonuç | Dayanak | Risk |

**Risk skalası:**
- 🔴 Kesin süre ihtarında işlem veya sonuç belirsiz ya da tutanağa geçmemiş (hak kaybı uygulanamaz, kanun yolunda bozma riski); kanunda olmayan yaptırım.
- 🟠 Hazır olmayan tarafa kesin süreli ara kararın tebliğ edilmemesi; iki tarafa eşit olmayan süre.
- 🟡 Duruşma aralığı üç ayı aşıyor ve gerekçe yazılmamış.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 31, 32, 90, 94, 95, 115, 120, 139, 140, 145, 147, 150, 154, 220, 240, 324, 341 — bu sohbette çekildi mi, eşleşti mi.
- Süre hesapları hatırlatmadır; son günü hâkim/kalem teyit eder. Tebliğ tarihi gibi bilinmeyen bir olguda en erken olası gün esas alınır ve bu açıkça uyarı olarak yazılır.
- ⚠️ "Hak kaybı doğuran kesin süre ve ihtaratta hâkim/heyet takdiri ve onayı şarttır."

## Sıradaki adımlar

- `/hukuk-kalem:durusma-tutanagi` — ara kararın tutanağa geçirilmesi
- `/hukuk-kalem:tebligat` — hazır olmayan tarafa ara kararın tebliği
- `/hukuk-hakim:bilirkisi-raporu-denetimi` — bilirkişi görevlendirme veya ek rapor kalemi varsa

---

## /hukuk-hakim:bilirkisi-raporu-denetimi

---
name: bilirkisi-raporu-denetimi
description: >
  Hukuk yargılamasında bilirkişi raporunu hükme esas alınmadan önce denetler:
  görevlendirme kararının kapsamı, raporun şekli, görev sınırı ve hukuki nitelendirme
  yasağı, denetime elverişlilik, taraflara tebliğ ve itiraz süresi, itirazların
  türüne göre ek rapor / sözlü açıklama / yeni bilirkişi seçenekleri, uzman görüşüyle
  çelişki. Rapora uyulup uyulmayacağını hâkime bırakır.
user-invocable: true
---

# Bilirkişi Raporu Denetimi — HMK m. 266-282, 293; 6754 s.K. m. 3

## Konum hatırlatması

Hâkim bilirkişinin oy ve görüşünü diğer delillerle birlikte serbestçe değerlendirir (HMK m. 282). Bu skill raporu "doğru / yanlış" diye nitelemez; hükme esas alınmaya elverişli olup olmadığını ölçütlerle gösterir ve itirazları iki yönlü sınıflandırır. Karar hâkimindir. Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir.

## Amaç

Bilirkişi raporunun hükme esas alınmaya elverişli olup olmadığını görevlendirme kararı ve rapor şartlarıyla karşılaştırarak göstermek; tarafların itirazlarını sınıflandırıp ek rapor, sözlü açıklama veya yeni bilirkişi seçeneklerini gerekçeleriyle sunmak.

## Dayanak (bu sohbette çekilir)

- **HMK m. 266** — çözümü hukuk dışında özel veya teknik bilgi gerektiren hâllerde bilirkişiye başvurulur; genel bilgi veya tecrübeyle ya da hâkimlik mesleğinin gerektirdiği hukuki bilgiyle çözülebilecek konularda başvurulamaz; hukuk öğrenimi görmüş kişiler, hukuk dışında ayrı bir uzmanlığı belgelendirmedikçe bilirkişi olarak görevlendirilemez.
- **HMK m. 268** — bilirkişi, bilirkişilik bölge kurulunun listesinden seçilir; liste dışı görevlendirme istisnaları.
- **HMK m. 272** — hâkimlere ilişkin yasaklılık ve ret kuralları bilirkişiye de uygulanır; ret talebi, ret sebebinin öğrenilmesinden itibaren en geç bir hafta içinde.
- **HMK m. 273** — görevlendirme kararında inceleme konusunun bütün sınırlarıyla belirlenmesi, cevaplanacak sorular ve raporun verilme süresi.
- **HMK m. 274** — rapor süresi üç ayı geçemez, gerekçeyle en çok üç ay uzatılabilir; basit yargılamada iki ay.
- **HMK m. 279** — raporun zorunlu unsurları (m. 279/2); bilirkişi uzmanlığı, özel veya teknik bilgiyi gerektiren hususlar dışında açıklama yapamaz, hâkim tarafından yapılması gereken hukuki nitelendirme ve değerlendirmelerde bulunamaz (m. 279/4).
- **HMK m. 280** — rapor, verildiği tarih yazılarak mahkemeye verilir ve duruşma gününden önce taraflara tebliğ edilir.
- **HMK m. 281** — taraflar tebliğden itibaren iki hafta içinde eksikliğin tamamlatılmasını, belirsizliğin açıklanmasını veya yeni bilirkişi atanmasını isteyebilir; zorunlu hâlde süre içinde başvurana, bir defaya mahsus ve iki haftayı geçmemek üzere ek süre; mahkeme yeni sorularla ek rapor veya duruşmada sözlü açıklama isteyebilir, gerekirse yeni bilirkişiyle tekrar inceleme yaptırabilir.
- **HMK m. 293** — taraflar uzmanından bilimsel mütalaa alabilir; uzman dinlenebilir; çağrıldığı duruşmaya geçerli özürsüz gelmeyen uzmanın raporu değerlendirmeye alınmaz.
- **6754 s.K. m. 3** — bilirkişi bağımsız, tarafsız ve objektif; hukuki nitelendirme yasağı; aynı konuda bir kez rapor alınması esas, eksiklik veya belirsizlik için ek rapor; UYAP ve entegre sistemlerle ulaşılabilen bilgiler için bilirkişiye başvurulamaz.

## Girdi

- Görevlendirme kararı (sorular, süre), bilirkişinin uzmanlık alanı
- Rapor metni ve veriliş tarihi; taraflara tebliğ tarihleri
- Taraf itirazları (tarih, içerik), varsa uzman görüşleri

## Denetim adımları

1. **Başvuru yerinde mi:** konu özel veya teknik bilgi mi; hukuki bilgiyle çözülebilecek bir soru mu sorulmuş (m. 266; 6754 m. 3/3, 3/8).
2. **Görevlendirme kararı:** inceleme konusu, sorular ve süre açık mı (m. 273; 6754 m. 3/6).
3. **Bilirkişi:** listeden mi, uzmanlık uyumu, yasaklılık ve ret (m. 268, 272).
4. **Şekil:** m. 279/2 unsurları (taraflar, görevlendirildiği hususlar, incelenen maddi vakıalar, gerekçe ve sonuç, görüş ayrılığı ve sebebi, tarih, imza).
5. **Görev sınırı ve hukuki nitelendirme:** rapor sorulmayan konuya veya hukuki değerlendirmeye girmiş mi (m. 279/4; 6754 m. 3/2). Girdiyse o kısım ayrılır ve hükme esas alınmaz.
6. **Denetime elverişlilik:** veri, kaynak, yöntem ve hesap izlenebilir mi; varsayımlar açık mı; ara sonuçlar tutarlı mı.
7. **Tebliğ ve itiraz süresi:** rapor her tarafa tebliğ edildi mi; iki haftalık süre ve varsa ek süre (m. 280, 281/1).
8. **İtiraz sınıflandırması (m. 281):**
   - Eksiklik → ek rapor (yeni sorular) — m. 281/2
   - Belirsizlik → açıklama veya duruşmada sözlü dinleme — m. 281/2
   - Esaslı teknik çelişki (uzman görüşüyle, başka raporla, dosya verisiyle) → yeni bilirkişiyle tekrar inceleme — m. 281/3
   - Hukuki itiraz → bilirkişiye sorulmaz; mahkemece gerekçede karşılanır
9. **Uzman görüşü:** uzman dinlendi mi; çağrıya geçerli özürsüz uymadıysa mütalaa değerlendirme dışıdır (m. 293/3).
10. **Gerekçeye aktarım:** rapora neden itibar edildiği veya edilmediği somut olarak gösterilir (m. 282); matbu "rapora itibar edilmiştir" ifadesi yetmez → `/yargi-arastirma:aym-aihm-standart-kontrolu` (gerekçeli karar).

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Rapor denetim tablosu:** | Ölçüt | Dayanak | Rapordaki durum | Değerlendirme | Risk |
2. **İtiraz matrisi:** | # | İtiraz | Taraf | Tür (eksiklik / belirsizlik / teknik çelişki / hukuki) | Önerilen işlem | Kabul yönünde / ret yönünde gerekçe |
3. **Ek rapor soru iskeleti** (tarafsız, teknik): "1- [DOLDUR] hesabında hangi veri esas alınmıştır; [karşı taraf verisi] esas alındığında sonuç nasıl değişir? 2- [DOLDUR]"
4. **Gerekçe paragrafı iskeleti** (iki yönlü; sonuç boş).

**Risk skalası:**
- 🔴 Raporun hukuki nitelendirme içeren kısmının hükme esas alınması; rapor tebliğ edilmeden veya itiraz süresi dolmadan karar.
- 🟠 Esaslı teknik itirazın karşılanmaması; hukuk öğrenimi görmüş kişinin ayrı uzmanlığı belgelenmeden görevlendirilmesi.
- 🟡 Süre aşımı (m. 274); şekil eksiği.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 266, 268, 272, 273, 274, 279, 280, 281, 282, 293; 6754 s.K. m. 3 — bu sohbette çekildi mi, eşleşti mi.
- Emsal gerekiyorsa: `tr_ictihat_ara(query="+\"bilirkişi raporu\" +\"hukuki nitelendirme\"", courts=["YARGITAYKARARI"], chamber="HGK", date_from=…, date_to=…)` → yalnız okunan kararlar.
- Detay: `bilirkisilik-rehberi.md`.
- Süre hesapları hatırlatmadır; son günü hâkim/kalem teyit eder. Tebliğ tarihi gibi bilinmeyen bir olguda en erken olası gün esas alınır ve bu açıkça uyarı olarak yazılır.
- ⚠️ "Rapora itibar edilip edilmeyeceği hâkim takdirindedir (HMK m. 282)."

## Sıradaki adımlar

- `/hukuk-hakim:ara-karar` — ek rapor, sözlü açıklama veya yeni bilirkişi ara kararı
- `/hukuk-hakim:delil-degerlendirme`
- `/hukuk-hakim:gerekceli-karar`

---

## /hukuk-hakim:dava-sarti-kontrolu

---
name: dava-sarti-kontrolu
description: >
  HMK m. 114-115 dava şartlarını ve özel kanunlardaki dava şartı arabuluculuk
  alanlarını (TTK m. 5/A, 7036 s.K. m. 3, 6325 s.K. m. 18/B, 6502 s.K. m. 73/A) tek
  tabloda denetler; eksikliğin giderilebilir olup olmadığını, verilecek kesin süreyi
  ve usulden ret seçeneğini yapılandırır. Kararı hâkime bırakır.
user-invocable: true
---

# Dava Şartı Kontrolü — HMK m. 114-115 ve Dava Şartı Arabuluculuk

## Konum hatırlatması

Mahkeme dava şartlarının mevcut olup olmadığını davanın her aşamasında kendiliğinden araştırır (HMK m. 115/1). Dava şartları ilk itirazlardan ayrıdır: ilk itirazlar (kesin yetki kuralının bulunmadığı hâllerde yetki itirazı, tahkim itirazı) cevap dilekçesinde ileri sürülmezse dinlenmez ve dava şartlarından sonra incelenir (m. 116-117). Usulden ret hak arama hürriyetine dokunan bir sonuçtur; **karar hâkimindir.** Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir. **Kesin süre ve usulden ret kararı için hâkim/heyet takdiri ve onayı şarttır.**

## Amaç

Dava şartlarının ve özel kanunlardaki dava şartı arabuluculuk koşulunun dosyada karşılanıp karşılanmadığını tek tabloda göstermek; eksiklik giderilebilirse verilecek kesin süreyi ve ihtarı, giderilemezse usulden ret seçeneğini hâkimin önüne koymak.

## Dayanak (bu sohbette çekilir)

- **HMK m. 114/1:** a) Türk mahkemelerinin yargı hakkı; b) yargı yolunun caiz olması; c) görev; ç) kesin yetki; d) taraf ve dava ehliyeti, kanuni temsilcinin gerekli niteliği; e) dava takip yetkisi; f) vekilin davaya vekâlet ehliyeti ve usulüne uygun vekâletname; g) davacının yatırması gereken gider avansı; ğ) teminat kararının gereğinin yerine getirilmesi; h) hukuki yarar; ı) derdestlik; i) kesin hüküm. **m. 114/2:** diğer kanunlardaki dava şartları saklıdır.
- **HMK m. 115:** noksanlık → usulden ret; giderilmesi mümkünse kesin süre, süre içinde giderilmezse usulden ret; esasa girilmeden fark edilmemiş ve hüküm anında giderilmiş noksanlık nedeniyle usulden ret yapılamaz. **m. 138:** dava şartları ve ilk itirazlar hakkında öncelikle dosya üzerinden karar verilir.
- **Dava şartı arabuluculuk:**
  - **TTK m. 5/A** — ticari davalardan konusu bir miktar para olan alacak, tazminat, itirazın iptali, menfi tespit ve istirdat davaları.
  - **7036 s.K. m. 3** — kanuna, bireysel veya toplu iş sözleşmesine dayanan işçi veya işveren alacağı ve tazminatı ile işe iade; bu alacak ve tazminatla ilgili itirazın iptali, menfi tespit ve istirdat davaları. İş kazası veya meslek hastalığından kaynaklanan maddi ve manevi tazminat ile bunlarla ilgili tespit, itiraz ve rücu davaları hariç (m. 3/3).
  - **6325 s.K. m. 18/B** — kiralanan taşınmazların ilamsız icra yoluyla tahliyesine ilişkin hükümler hariç kira ilişkisinden kaynaklanan uyuşmazlıklar; taşınır ve taşınmazların paylaştırılması ve ortaklığın giderilmesi; 634 s. Kat Mülkiyeti K.'dan kaynaklanan uyuşmazlıklar; komşu hakkından kaynaklanan uyuşmazlıklar.
  - **6502 s.K. m. 73/A** — tüketici mahkemelerinde görülen uyuşmazlıklar; istisnalar: tüketici hakem heyetinin görevine giren uyuşmazlıklar, hakem heyeti kararlarına itirazlar, m. 73/6 ve m. 74'teki davalar, tüketici işlemi niteliğinde olup taşınmazın aynından doğan uyuşmazlıklar.
  - **Usul — 6325 s.K. m. 18/A (7036 m. 3/2 aynı yönde):** davacı son tutanağın aslını veya arabulucu onaylı örneğini dava dilekçesine ekler; eklenmemişse bir haftalık kesin süre ve usulden ret ihtarlı davetiye gönderilir; ihtarın gereği yerine getirilmezse dava dilekçesi karşı tarafa tebliğe çıkarılmaksızın usulden ret; arabulucuya başvurulmadan dava açıldığı anlaşılırsa herhangi bir işlem yapılmaksızın dava şartı yokluğundan usulden ret (m. 18/A/2). Özel kanunda tahkim veya başka bir alternatif uyuşmazlık çözüm yoluna başvurma zorunluluğu ya da tahkim sözleşmesi varsa dava şartı arabuluculuk hükümleri uygulanmaz (m. 18/A/18). Arabuluculuk bürosuna başvurudan son tutanağa kadar zamanaşımı durur, hak düşürücü süre işlemez (m. 18/A/15).

## Girdi

- Dava dilekçesi özeti: taraflar, dava türü ve her talep kalemi, değer, dava tarihi
- Vekâletname, harç ve avans makbuzları, arabuluculuk son tutanağı (tarih, taraflar, konu, sonuç)
- Cevap dilekçesindeki ilk itirazlar; derdest veya kesin hükümle sonuçlanmış başka dava bilgisi

## Adımlar

1. **Genel dava şartları** m. 114/1 sırasıyla; her biri için "var / yok / bilgi yok".
2. **Talep kalemlerini ayır:** birden çok talep varsa dava şartı arabuluculuk her kalem için ayrı değerlendirilir (örn. iş davasında alacak kalemleri ile iş kazası tazminatı).
3. **Arabuluculuk matrisi:** kalem → kanun → kapsam / istisna → son tutanak var mı → tutanak ile dava arasında taraf ve konu uyumu → tutanak tarihi dava tarihinden önce mi.
4. **Giderilebilirlik:** noksanlık giderilebilir mi (m. 115/2) → kesin süre ve ihtar; giderilemez mi → usulden ret seçeneği. Arabulucuya hiç başvurulmamışsa m. 18/A/2 son cümlesi; son tutanak eklenmemişse bir haftalık kesin süre.
5. **İlk itirazlarla karıştırmama:** tahkim itirazı ilk itirazdır (m. 116/1-b); tahkim sözleşmesi varsa dava şartı arabuluculuk uygulanmaz (6325 m. 18/A/18) — iki kontrol ayrı yazılır.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Dava şartı tablosu:** | Şart | Dayanak | Dosyadaki durum | Giderilebilir mi | Önerilen işlem (seçenekli) | Risk |
2. **Arabuluculuk matrisi:** | Talep kalemi | Kanun ve kapsam | İstisna | Son tutanak (tarih / taraf / konu) | Uyum | İşlem |
3. **Kesin süre ve ihtar kalıbı:** "Davacıya, arabuluculuk faaliyeti sonunda düzenlenen son tutanağın aslını veya arabulucu tarafından onaylanmış bir örneğini tebliğden itibaren bir haftalık KESİN SÜRE içinde mahkemeye sunması, aksi takdirde davanın usulden reddedileceği hususunun İHTARINA (6325 s.K. m. 18/A/2)."
4. **Usulden ret iskeleti** (seçenekli; hangi şart, hangi gerekçe); esasa girilecekse "dava şartları yönünden eksiklik görülmediği" notu.

**Risk skalası:**
- 🔴 Dava şartı arabuluculuk kapsamındaki talepte arabulucuya hiç başvurulmamış; görev veya kesin yetki yok; kesin hüküm veya derdestlik.
- 🟠 Son tutanak eklenmemiş (kesin süre ve ihtar gerekir); tutanak ile dava arasında taraf veya konu uyumsuzluğu; vekâletname eksiği.
- 🟡 Gider avansı eksiği (m. 120/2 kesin süresi); kalemlerin bir kısmının kapsam dışı olduğunun yazılmaması.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: HMK m. 114, 115, 116, 117, 120, 138; TTK m. 5/A; 7036 s.K. m. 3; 6325 s.K. m. 18/A, 18/B; 6502 s.K. m. 73/A — bu sohbette çekildi mi, eşleşti mi.
- Tüketici hakem heyeti parasal sınırı (6502 m. 68) her yıl yeniden değerleme oranında artırılır; güncel tutar çekilmediyse UYARI satırı.
- Süre hesapları hatırlatmadır; son günü hâkim/kalem teyit eder. Tebliğ tarihi gibi bilinmeyen bir olguda en erken olası gün esas alınır ve bu açıkça uyarı olarak yazılır.
- ⚠️ "Usulden ret veya kesin süre kararı hâkim takdirindedir."

## Sıradaki adımlar

- `/hukuk-hakim:on-inceleme` — ön inceleme tutanağı
- `/hukuk-hakim:ara-karar` — kesin süre ve ihtar
- `/yargi-arastirma:emsal-tarama` — kapsam tereddüdünde Yargıtay çizgisi

---

> 🚧 **v1.0.0.** `hukuk-hakim` için 4 skill (gerekçe yazımı, ön inceleme, delil değerlendirme, ihtiyati tedbir) ve diğer plugin'lerin yapı kalıbıdır. **v1.2.0:** ara karar, bilirkişi raporu denetimi ve dava şartı kontrolü eklendi (toplam 7). Genişletme sırası → [CHANGELOG.md](../../CHANGELOG.md).
