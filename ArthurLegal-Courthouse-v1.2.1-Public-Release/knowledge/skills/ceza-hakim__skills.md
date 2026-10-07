# ceza-hakim — Skill Referans Kitapçığı

> Dal: Ceza mahkemesi · Rol: **Hâkim** · Usul: CMK 5271 (+ TCK 5237)
> Toplam skill: 7
> Kullanım: `/ceza-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Masumiyet karinesi esastır. Çıktılar değerlendirme iskeletidir; **takdir ve hüküm hâkim/heyettedir**. Her çıktı **TASLAK**.

## İçindekiler

- /ceza-hakim:hukum-taslagi — CMK m. 223/230/232 hüküm gerekçesi iskeleti
- /ceza-hakim:iddianame-degerlendirme — CMK m. 170/174 iddianame iade kontrolü
- /ceza-hakim:tutuklama-degerlendirme — CMK m. 100-101 tutuklama/adli kontrol ölçütleri
- /ceza-hakim:hagb-degerlendirme — CMK m. 231 hükmün açıklanmasının geri bırakılması
- /ceza-hakim:uzlastirma-denetimi — CMK m. 253-255 uzlaştırma kapsam & rapor denetimi
- /ceza-hakim:tutukluluk-incelemesi — CMK m. 100-109 periyodik ve istem üzerine tutukluluk incelemesi (m. 108), azami süreler (m. 102)
- /ceza-hakim:gerekce-denetimi — CMK m. 34, 230, 232 hüküm gerekçesinin denetimi ve m. 289 hukuka kesin aykırılık kontrolü

---

## /ceza-hakim:hukum-taslagi

---
name: hukum-taslagi
description: >
  CMK m. 223 hüküm türleri ve m. 230/232 gerekçe unsurlarına göre ceza hükmü iskeleti:
  sabit görülen/görülmeyen fiiller, delil değerlendirmesi, vasıflandırma, lehe-aleyhe
  unsurlar, ceza bireyselleştirme ölçütleri. Sonucu ve cezayı DAYATMAZ.
user-invocable: true
---

# Ceza Hükmü — CMK m. 230/232 İskeleti

## Konum hatırlatması

**Masumiyet karinesi (AY m. 38/4, AİHS m. 6/2).** Şüpheden sanık yararlanır. Bu skill mahkûmiyet/beraat **sonucunu vermez**; gerekçenin iskeletini kurar, takdir hâkim/heyettedir.

## Çıktı yapısı — m. 230 unsurları

1. **İddia & savunma** — iddia makamının anlatımı + sanık savunması ayrı.
2. **Sabit görülen fiil** — hangi vakıa hangi delille sabit; çelişkilerin giderilmesi.
3. **Delil değerlendirmesi** — her delilin tartışılması (m. 217 — hukuka uygun + duruşmaya getirilmiş delil); hukuka aykırı delil (m. 206/2-a, 217/2) dışlanır.
4. **Vasıflandırma** — fiilin hukuki niteliği (TCK ilgili madde, MCP'den verbatim). **İki yönlü:** suçun oluştuğu ve oluşmadığı yorumları ayrı kurulur.
5. **Lehe kanun & bireyselleştirme** — TCK m. 7 lehe hüküm, m. 61 temel ceza, artırım/indirim, m. 62 takdiri indirim, erteleme/HAGB (CMK m. 231), seçenek yaptırımlar.
6. **Hüküm (iskelet, m. 223):** mahkûmiyet / beraat / ceza verilmesine yer olmadığı / düşme / güvenlik tedbiri — **seçenekli sunulur**, sonuç boş.

## Adımlar

1. Görev/yetki + soruşturma usulü kontrolü (yetkisiz/hukuka aykırı delil var mı).
2. Vakıa–delil eşleştirmesi; çelişki haritası.
3. TCK normunu MCP'den çek, atıf et.
4. Lehe-aleyhe unsurları dengeli sun; ceza miktarını **dayatma**, ölçüt ver.

## İnceleyen notu

- Kullanılan TCK/CMK maddeleri + emsal (atıflı)
- Hukuka aykırı delil riski işaretleri
- ⚠️ "Mahkûmiyet/beraat ve ceza takdiri hâkime/heyete aittir."

---

## /ceza-hakim:iddianame-degerlendirme

---
name: iddianame-degerlendirme
description: >
  CMK m. 170 iddianamenin unsurları ve m. 174 iade sebepleri çerçevesinde iddianamenin
  kabul/iade kontrolü. 15 günlük iade süresini ve eksiklik türlerini yapılandırır.
user-invocable: true
---

# İddianame Değerlendirme — CMK m. 170 / 174

## Amaç

İddianamenin kabule değer olup olmadığını **15 gün** içinde (m. 174/1) yapılandırılmış biçimde kontrol et.

## Kontrol listesi

1. **m. 170 zorunlu unsurlar:** şüpheli kimliği, müdafi, mağdur, suç tarihi/yeri, suçu oluşturan olaylar, deliller, sevk maddeleri, yüklenen suç.
2. **İade sebepleri (m. 174/1):**
   - 🔴 m. 170'e aykırı düzenleme (eksik unsur)
   - 🔴 Suçun sübûtuna doğrudan etki edecek mevcut bir delil toplanmadan düzenlenmiş (m. 174/1-b; genel 'eksik soruşturma' iade sebebi değildir)
   - 🔴 Önödeme, uzlaştırma veya seri muhakemeye tâbi olduğu soruşturma dosyasından açıkça anlaşılan işte bu usuller uygulanmaksızın düzenlenmiş (m. 174/1-c; basit yargılama iade sebebi değildir)
   - 🔴 Soruşturma veya kovuşturma yapılması izne/talebe bağlı suçta izin alınmaksızın/talep olmaksızın düzenlenmiş (m. 174/1-d)
   - 🔴 Onbeş yaşını doldurmamış çocuk hakkında sosyal inceleme yaptırılmaksızın düzenlenmiş (m. 174/1-e, 7593 s.K.)
3. **İade edilemez (m. 174/2):** suçun hukuki nitelendirmesi sebebiyle iade yapılamaz (vasıflandırma mahkemeye ait).
4. **Süre:** 15 gün içinde iade edilmezse iddianame **kabul edilmiş sayılır** (m. 174/3).

## Çıktı

Kabul / iade önerisi (gerekçeli, seçenekli) + eksiklik listesi (🔴🟠). Karar hâkimindir. TASLAK ibareli.

---

## /ceza-hakim:tutuklama-degerlendirme

---
name: tutuklama-degerlendirme
description: >
  CMK m. 100-101 tutuklama şartları ve m. 109 adli kontrol çerçevesinde koruma tedbiri
  değerlendirme ölçütleri. Ölçülülük ve gerekçe zorunluluğunu vurgular; tedbiri DAYATMAZ.
user-invocable: true
---

# Tutuklama / Adli Kontrol — CMK m. 100-101 / 109

## Konum hatırlatması

Tutuklama **istisnai** ve **ölçülü** olmak zorundadır (AY m. 19, AİHS m. 5). Adli kontrol önceliklidir (m. 101/1). Bu skill ölçüt sunar; tedbir kararı hâkimindir.

## Ölçütler

1. **Kuvvetli suç şüphesi** + somut delil (m. 100/1).
2. **Tutuklama nedeni (m. 100/2):**
   - Kaçma şüphesi / saklanma
   - Delilleri karartma / tanık-mağdur üzerinde baskı
   - Katalog suçlar (m. 100/3) — varsayılan neden (yine de somutlaştır)
3. **Ölçülülük (m. 100/1 son):** işin önemi + beklenen ceza/tedbir ile orantı; adli kontrol yeterli mi (m. 109).
4. **Gerekçe zorunluluğu (m. 101/2):** somut olgularla; matbu gerekçe 🔴 bozma/ihlal sebebi (AYM bireysel başvuru içtihadı — ArthurLegal MCP (`tr_`)'den teyit).
5. **Süre & ölçülü süre** — soruşturma/kovuşturma azami süreleri.

## Çıktı

Adli kontrol ↔ tutuklama seçenek analizi + somut gerekçe iskeleti (matbu DEĞİL). Karar hâkimindir. TASLAK ibareli.

---

## /ceza-hakim:hagb-degerlendirme

---
name: hagb-degerlendirme
description: >
  CMK m. 231 hükmün açıklanmasının geri bırakılması: objektif ve sübjektif
  şartlar (7589 s.K. metni), zararın giderilmesi (m. 231/6-c, taksitle m. 231/9), 5 yıllık denetim süresi.
  HAGB'yi DAYATMAZ; şart kontrolü + ölçüt sunar.
user-invocable: true
---

# HAGB — CMK m. 231/5-14

## Konum hatırlatması

HAGB, kurulan hükmün açıklanmasının geri bırakılmasıdır; uygulanıp uygulanmaması ölçütlere bağlıdır, takdir hâkim/heyettedir. (7589 s.K. ile yeniden düzenlenen m. 231/6'da sanığın kabulü koşulu yer almaz.)

## Şartlar (m. 231/5-6)

1. **Ceza sınırı:** hükmolunan hapis **2 yıl veya daha az** ya da adli para cezası.
2. **Sabıka:** sanık daha önce kasıtlı suçtan mahkûm olmamış.
3. **Kanaat:** sanığın yeniden suç işlemeyeceği yönünde kanaat (kişilik + duruşmadaki tutum).
4. **Zarar:** mağdurun/kamunun zararının **aynen iade / öncesi hale getirme / tazmin** yoluyla giderilmesi.
5. **Taksitle zarar giderimi (m. 231/9):** (c) koşulu derhal yerine getirilemiyorsa, zararın denetim süresince aylık taksitlerle tamamen giderilmesi koşuluyla da HAGB verilebilir. (Eski m. 231/6 son cümlesindeki 'sanığın kabulü' koşulu, 7589 s.K. ile yeniden düzenlenen metinde yer almaz — 31/7/2026.)

## Sonuç & denetim

- **Denetim süresi 5 yıl** (m. 231/8); denetimli serbestlik tedbiri eklenebilir.
- Süre içinde kasıtlı suç işlenmez + yükümlülüklere uyulursa → **dava düşer** (m. 231/10).
- İhlal → **hüküm açıklanır** (m. 231/11).
- Kanun yolu: **istinaf** (m. 231/12 — 7499 s.K. ile itirazdan istinafa çevrildi; m. 272/3 saklı); BAM kararlarına m. 286 uygulanır. Denetim süresinde açıklanan/yeniden kurulan hükme **itiraz** (m. 231/11).

## Çıktı

Şart-şart kontrol tablosu (🔴 eksik) + zarar giderim durumu + kanaat ölçütleri. Karar hâkim/heyettedir. TASLAK ibareli. Detay: `cmk-rehberi.md`.

---

## /ceza-hakim:uzlastirma-denetimi

---
name: uzlastirma-denetimi
description: >
  CMK m. 253-255 uzlaştırma: kapsamdaki suçlar, uzlaştırmanın zorunluluğu,
  uzlaştırmacı raporunun mahkemece denetimi ve sonuçları. Mahkeme uzlaştırmayı
  bizzat yürütmez; kapsamı ve raporu denetler.
user-invocable: true
---

# Uzlaştırma Denetimi — CMK m. 253-255

## Konum

Uzlaştırma, uzlaştırmacı eliyle yürür; mahkeme **kapsamı** ve **raporu** denetler. Kapsamdaki suçta uzlaştırma yoluna gidilmemesi 🔴 bozma/iade sebebidir.

## Kontrol

1. **Kapsam (m. 253/1):** şikâyete bağlı suçlar + kanunda sayılan belirli suçlar. **İstisnalar (m. 253/3):** cinsel dokunulmazlığa karşı suçlar vb. uzlaştırma kapsamı dışı.
2. **Zorunluluk:** kapsamdaysa uzlaştırma zorunlu ön/ara aşamadır; atlanmışsa giderilir.
3. **Rapor denetimi:** uzlaştırmacı raporu usulüne uygun mu; tarafların özgür iradesi, edimin belirliliği.
4. **Sonuç (soruşturmada m. 253/19, kovuşturmada m. 254/2):** edim def'aten ifa → kovuşturmaya yer olmadığı (soruşturma) / davanın düşmesi (kovuşturma); ileri tarihli/taksitli/süreklilik arz eden edim → kamu davasının açılmasının ertelenmesi (soruşturma) / **durma kararı** (kovuşturma, 7531 s.K.); edim yerine getirilmezse kamu davası açılır / yargılamaya kaldığı yerden devam olunur.

## Çıktı

Kapsam kontrolü (uzlaştırmaya tabi mi) + rapor usul denetimi + sonuç önerisi (düşme/devam). Karar hâkimindir. TASLAK ibareli.

---

## /ceza-hakim:tutukluluk-incelemesi

---
name: tutukluluk-incelemesi
description: >
  Tutuklu şüpheli veya sanık için periyodik ve istem üzerine tutukluluk incelemesini
  CMK m. 100-109 çerçevesinde yapılandırır: süre takvimi (otuzar günlük inceleme,
  oturumlar, azami süreler), kuvvetli şüphe ve tutuklama nedeninin güncelliği,
  ölçülülük, adli kontrolün neden yetersiz kaldığı, somut gerekçe. Devam veya tahliye
  kararını VERMEZ.
user-invocable: true
---

# Tutukluluk İncelemesi — CMK m. 100-109

## Konum hatırlatması

Kişi hürriyeti kuraldır; tutuklanan kişilerin makul süre içinde yargılanmayı ve soruşturma veya kovuşturma sırasında serbest bırakılmayı isteme hakları vardır (AY m. 19). Tutukluluğun devamına veya tahliye isteminin reddine ilişkin karar da tutuklama kararı gibi somut olgularla gerekçelendirilir (CMK m. 101/2). Masumiyet karinesi (AY m. 38) gerekçenin dilinde de gözetilir. **Tutukluluğun devamı, adli kontrol veya tahliye kararı için hâkim/heyet takdiri ve onayı şarttır.** Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir.

## Amaç

Tutukluluk incelemesinde hâkimin veya heyetin önüne süre takvimini, tutuklama şartlarının güncel durumunu ve adli kontrolün yeterli olup olmadığını somut olgularla gösteren bir çalışma notu koymak.

## Dayanak (bu sohbette çekilir)

- **CMK m. 100** — kuvvetli suç şüphesinin varlığını gösteren somut deliller ve bir tutuklama nedeni; işin önemi, verilmesi beklenen ceza veya güvenlik tedbiri ile ölçülü olmama hâlinde tutuklama kararı verilemez; tutuklama nedenleri (m. 100/2), katalog suçlar (m. 100/3), tutuklama yasağı (m. 100/4).
- **CMK m. 101/2** — tutuklamaya, devamına veya tahliye isteminin reddine ilişkin kararlarda kuvvetli suç şüphesi, tutuklama nedenlerinin varlığı, ölçülülük ve adli kontrolün yetersiz kalacağı somut olgularla gerekçelendirilerek açıkça gösterilir; kararın içeriği sözlü bildirilir ve örneği verilir.
- **CMK m. 102** — azami süreler (ağır ceza mahkemesinin görevine girmeyen ve giren işler; soruşturma evresi sınırları — m. 102/4; suç tarihinde on beş ve on sekiz yaşını doldurmamış çocuklar için oranlar — m. 102/5); uzatma kararları Cumhuriyet savcısının, şüpheli veya sanık ile müdafiin görüşleri alındıktan sonra verilir (m. 102/3).
- **CMK m. 104-105** — salıverilme istemi her aşamada yapılabilir; istem üzerine görüş alınarak üç gün içinde karar (örgüt faaliyeti çerçevesinde işlenen suçlarda yedi gün); duruşma dışında bu karar verilirken görüş alınmaz; kararlara itiraz edilebilir; dosya bölge adliye mahkemesinde veya Yargıtay'da ise karar dosya üzerinden verilir, re'sen de verilebilir (m. 104/3).
- **CMK m. 108** — soruşturma evresinde en geç otuzar günlük süreler itibarıyla, Cumhuriyet savcısının istemi üzerine sulh ceza hâkimince, şüpheli veya müdafii dinlenerek; kovuşturma evresinde hâkim veya mahkemece her oturumda veya koşullar gerektirdiğinde oturumlar arasında ya da otuz günlük süre içinde re'sen karar.
- **CMK m. 109** — adli kontrol yükümlülükleri (m. 109/3 a-l); ağır hastalık, engellilik, gebelik ve doğum sonrası hâlleri (m. 109/4); kanuni tutukluluk süreleri dolduğu için salıverilenler hakkında adli kontrol (m. 109/7).
- **CMK m. 267-268** — itiraz, kararı öğrenmeden itibaren iki hafta; sulh ceza hâkimliğinin tutuklama ve adli kontrol kararlarına itirazı yargı çevresindeki asliye ceza mahkemesi hâkimi inceler (m. 268/3-b).

## Girdi

- Evre (soruşturma / kovuşturma), görevli mahkeme (ağır ceza / asliye ceza), suç ve katalog durumu
- Yakalama, gözaltı ve tutuklama tarihleri; son inceleme tarihi; uzatma kararları
- Şüpheli veya sanığın suç tarihindeki yaşı; karar için gerekli olduğu ölçüde sağlık ve aile durumu
- Delil durumu: toplanan ve toplanacak deliller; tanık ve mağdur dinlenmesi tamamlandı mı
- Cumhuriyet savcısının görüşü, müdafi beyanları

## Adımlar

1. **Süre takvimi:** tutuklama tarihi → son inceleme → bir sonraki inceleme (soruşturmada otuz günü aşmayacak; kovuşturmada oturum veya ara) → azami süre (m. 102; çocuksa m. 102/5 oranı) → uzatma gerekiyor mu, görüşler alındı mı. Bilinmeyen tarihte en erken inceleme günü esas alınır ve 🔴/🟠 işaretlenir.
2. **Kuvvetli şüphe güncel mi:** tutuklamadan bu yana yeni delil, çelişen beyan, bilirkişi raporu.
3. **Tutuklama nedeni hâlâ somut mu:** kaçma, saklanma veya kaçacağı şüphesini uyandıran somut olgular; delil karartma veya tanık, mağdur üzerinde baskı şüphesi — deliller toplanmışsa bu nedenin güncel ağırlığı.
4. **Ölçülülük:** tutuklulukta geçen süre ile işin önemi ve beklenen ceza veya güvenlik tedbiri (m. 100/1).
5. **Adli kontrol seçenekleri:** m. 109/3'teki yükümlülüklerden hangileri tutuklama nedenini karşılar; hangileri neden yetersiz (m. 101/2-d). m. 109/4 hâlleri.
6. **Gerekçe:** her ölçüt için somut olgu; kanun metnini tekrar eden matbu ifade kullanılmaz.
7. **Usul:** görüş alma (m. 102/3, 105), sözlü bildirim ve örnek (m. 101/2), itiraz yolu ve mercii (m. 268).

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Süre takvimi tablosu:** | Olay | Tarih | Dayanak | Sonraki son gün | Not |
2. **Ölçüt × olgu tablosu (iki sütun):** | Ölçüt | Devam yönünde somut olgular | Tahliye / adli kontrol yönünde somut olgular |
3. **Adli kontrol seçenekleri:** her yükümlülük için hangi riski karşıladığı.
4. **Karar iskeleti (seçenekli, sonuç boş):** (a) tutukluluğun devamı; (b) adli kontrol şartıyla tahliye; (c) tahliye — her seçenek için m. 101/2 unsurlarını karşılayan gerekçe paragrafı ve itiraz bilgisi (süre, merci).

**Risk skalası:**
- 🔴 Otuz günlük inceleme süresi geçmiş veya azami süre dolmuş; uzatma kararı görüş alınmadan verilmiş; matbu gerekçe.
- 🟠 Adli kontrolün neden yetersiz kaldığı gösterilmemiş; deliller toplandığı hâlde "delil karartma" nedeni gerekçesiz tekrarlanıyor.
- 🟡 Çocuklara ilişkin oran veya m. 109/4 hâli değerlendirilmemiş.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: AY m. 19, 38; CMK m. 100, 101, 102, 104, 105, 108, 109, 267, 268 — bu sohbette çekildi mi, eşleşti mi.
- AYM bireysel başvuru içtihadı (tutuklulukta makul süre, gerekçe) gerekiyorsa `tr_aym_ara(query=…, kind="bireysel")` ile çekilip okunur; aksi hâlde anılmaz.
- Süre hesabı hatırlatmadır; son günü hâkim ve kalem teyit eder.
- ⚠️ "Tutukluluğun devamı, adli kontrol veya tahliye kararı hâkim/heyet takdiridir; hâkim/heyet onayı şart."

## Sıradaki adımlar

- `/ceza-hakim:tutuklama-degerlendirme` — ilk tutuklama değerlendirmesi
- `/yargi-arastirma:aym-aihm-standart-kontrolu` — kişi özgürlüğü ve gerekçe standardı
- `/ceza-kalem:durusma-tutanagi` — tutukluluk incelemesinin tutanağa geçirilmesi

---

## /ceza-hakim:gerekce-denetimi

---
name: gerekce-denetimi
description: >
  Ceza hükmünün gerekçesini imzadan önce CMK m. 34, 230 ve 232'ye göre denetler: iddia
  ve savunmanın karşılanması, delillerin tartışılması ve hükme esas alınan / reddedilen
  deliller, hukuka aykırı delillerin ayrıca gösterilmesi, sabit fiil ve nitelendirme,
  cezanın TCK'daki sıra ve esaslara göre belirlenmesi, hüküm fıkrasının unsurları.
  Hukuka kesin aykırılık (m. 289) risklerini işaretler; sonucu DEĞİŞTİRMEZ.
user-invocable: true
---

# Gerekçe Denetimi (Ceza) — CMK m. 34, 230, 232

## Konum hatırlatması

Bu skill hükmü yeniden yazmaz, sonucu sorgulamaz; gerekçenin kanunun aradığı unsurları taşıyıp taşımadığını gösterir. Hükmün m. 230 gereğince gerekçeyi içermemesi hukuka kesin aykırılık hâlidir (CMK m. 289/1-g). Mahkûmiyet, beraat ve ceza takdiri hâkim/heyettedir. Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir.

## Amaç

Ceza hükmünün gerekçesinin kanunun aradığı unsurları taşıyıp taşımadığını imzadan önce kontrol etmek; eksik veya bozma riski taşıyan noktaları önem derecesiyle işaretlemek.

## Dayanak (bu sohbette çekilir)

- **CMK m. 34** — hâkim ve mahkemelerin her türlü kararı karşı oy dâhil gerekçeli yazılır, gerekçede m. 230 göz önünde bulundurulur; kararlarda başvurulabilecek kanun yolu, süresi, mercii ve şekli belirtilir.
- **CMK m. 230/1** — mahkûmiyet gerekçesinde: a) iddia ve savunmada ileri sürülen görüşler; b) delillerin tartışılması ve değerlendirilmesi, hükme esas alınan ve reddedilen delillerin belirtilmesi, hukuka aykırı yöntemlerle elde edilen delillerin ayrıca ve açıkça gösterilmesi; c) ulaşılan kanaat, sabit görülen fiil ve nitelendirilmesi, TCK m. 61 ve 62'de belirlenen sıra ve esaslara göre cezanın belirlenmesi, TCK m. 53 ve devamına göre güvenlik tedbirinin belirlenmesi; d) erteleme, çevirme ve ek güvenlik tedbirleri ile bunlara ilişkin istemlerin kabul veya reddine ait dayanaklar. **m. 230/2:** beraatte m. 223/2'nin hangi bendine dayanıldığı; **m. 230/3:** ceza verilmesine yer olmadığı kararında m. 223/3-4'teki hâl; **m. 230/4:** diğer karar veya hükümlerde nedenler.
- **CMK m. 232** — hükmün başında yazılacaklar (m. 232/2); gerekçe ve karşı oy gerekçesi tutanağa tümüyle geçirilmemişse açıklamadan itibaren en geç on beş gün içinde dosyaya konulur (m. 232/3); hüküm fıkrasında m. 223'e göre verilen karar, uygulanan kanun maddeleri, ceza miktarı, kanun yollarına başvurma ve tazminat isteme olanağı, süre ve mercii tereddüde yer vermeyecek şekilde gösterilir (m. 232/6).
- **CMK m. 217** — hâkim kararını ancak duruşmaya getirilmiş ve huzurunda tartışılmış delillere dayandırabilir; yüklenen suç hukuka uygun elde edilmiş delille ispat edilir.
- **CMK m. 206/2** — kanuna aykırı elde edilen, karara etkisi olmayan veya davayı uzatma amaçlı delil istemi reddolunur.
- **CMK m. 216/3** — hükümden önce son söz hazır bulunan sanığa verilir.
- **CMK m. 289/1** — g) hükmün m. 230 gereğince gerekçeyi içermemesi; h) hüküm için önemli hususlarda savunma hakkının mahkeme kararıyla sınırlandırılması; i) hükmün hukuka aykırı yöntemlerle elde edilen delile dayanması.
- **TCK m. 61** — cezanın belirlenmesi: temel cezada göz önünde bulundurulacak hususlar (m. 61/1) ve indirim ile artırımların uygulanma sırası (m. 61/5); **m. 62** — takdiri indirim nedenleri kararda gerekçeleriyle gösterilir (m. 62/2); **m. 53** — belli hakları kullanmaktan yoksun bırakılma.
- **AY m. 38** — kanuna aykırı olarak elde edilmiş bulgular delil olarak kabul edilemez; **AY m. 141** — bütün mahkemelerin her türlü kararları gerekçeli olarak yazılır.

## Girdi

- Taslak gerekçe ve hüküm fıkrası
- İddianame özeti, esas hakkında mütalaa, savunma ve müdafi beyanlarının ana başlıkları (özellikle sonuca etkili itirazlar)
- Delil listesi: hangi delil duruşmada tartışıldı, hangisi reddedildi

## Denetim adımları

1. **İddia ve savunma (m. 230/1-a):** sonucu değiştirebilecek her savunma iddiası listelenir; gerekçede karşılığı var mı.
2. **Delil tartışması (m. 230/1-b, 217):** her delil için "duruşmaya getirildi / tartışıldı / esas alındı veya reddedildi, neden". Hukuka aykırı delil ayrı başlıkta ve açıkça.
3. **Sabit fiil ve nitelendirme (m. 230/1-c):** fiil hangi delillerle sabit; nitelendirme iki yönlü tartışılmış mı.
4. **Ceza tayini:** temel ceza ölçütleri (TCK m. 61/1) ve uygulama sırası (TCK m. 61/5) gerekçeden izlenebiliyor mu; takdiri indirim nedenleri gerekçeleriyle gösterilmiş mi (TCK m. 62/2).
5. **Seçenek kararlar (m. 230/1-d):** erteleme, çevirme ve ek güvenlik tedbirleri ile bunlara ilişkin istemlerin kabul veya reddinin dayanağı; hükmün açıklanmasının geri bırakılması değerlendirmesi ayrıca m. 231/6 şartları üzerinden gerekçelendirilir (`/ceza-hakim:hagb-degerlendirme`).
6. **Beraat / ceza verilmesine yer olmadığı (m. 230/2-3):** m. 223'ün hangi bendi.
7. **Hüküm fıkrası (m. 232/6):** karar türü, uygulanan maddeler, ceza miktarı, kanun yolu ve tazminat isteme olanağı, süre ve merci; tefhim edilen hüküm fıkrasıyla gerekçeli karar arasında fark olmaması.
8. **Usul güvenceleri:** son sözün sanığa verildiği tutanakta (m. 216/3); gerekçenin on beş günlük süre içinde dosyaya konulması (m. 232/3).

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Gerekçe denetim tablosu:** | Unsur | Dayanak | Taslakta var mı (paragraf) | Eksik / sorun | Risk |
2. **Delil–vakıa matrisi:** | Vakıa | Delil | Duruşmada tartışıldı mı | Esas alındı / reddedildi | Gerekçedeki yeri |
3. **Karşılanmamış esaslı savunma iddiaları listesi** (her biri için kabul yönünde ve ret yönünde karşılama seçenekleri).
4. **Hüküm fıkrası kontrol listesi** (m. 232/6).

**Risk skalası:**
- 🔴 m. 230 unsurlarından biri yok (m. 289/1-g); hukuka aykırı delile dayanılmış veya bu delil ayrıca gösterilmemiş (m. 289/1-i, 230/1-b); son söz verilmemiş.
- 🟠 Esaslı savunma iddiası karşılanmamış; takdiri indirim nedenleri gerekçesiz; hüküm fıkrasında kanun yolu, süre veya merci belirsiz.
- 🟡 Ceza tayininde uygulama sırası gerekçeden izlenemiyor; tefhim edilen hüküm ile gerekçeli karar arasında biçimsel fark.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: AY m. 38, 141; CMK m. 34, 206, 216, 217, 223, 230, 231, 232, 289; TCK m. 53, 61, 62 — bu sohbette çekildi mi, eşleşti mi. (27.09.2026 ölçümü: TCK m. 61 `number` ve `madde_no` ile istendiğinde NOT_FOUND döndü; `tr_mevzuat_icindekiler(number="5237", madde_from=59, madde_to=64)` ile alınan `madde_id` üzerinden çekildi.)
- Suç tipine ait TCK maddeleri ayrıca çekilir.
- ⚠️ "Mahkûmiyet, beraat ve ceza takdiri hâkim/heyettedir."

## Sıradaki adımlar

- `/ceza-hakim:hukum-taslagi` — eksik unsurların gerekçeye eklenmesi
- `/yargi-arastirma:aym-aihm-standart-kontrolu` — gerekçeli karar hakkı
- `/ceza-kalem:durusma-tutanagi` — son söz ve tefhim satırlarının kontrolü

---

> 🚧 v1.0.0 — `ceza-hakim` 5 skill; v1.2.0'da tutukluluk incelemesi ve gerekçe denetimi eklendi (toplam 7). Kalıp: `hukuk-hakim__skills.md`. Detay: `cmk-rehberi.md`, `sulh-ceza-hakimligi-rehberi.md`.
