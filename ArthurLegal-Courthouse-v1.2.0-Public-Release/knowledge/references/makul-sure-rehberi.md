# Makul Süre Rehberi

> Kullanan: `makul-sure-izleyici`, `durusma-hazirlik`, `yargi-arastirma:aym-aihm-standart-kontrolu`, bütün hâkim plugin'lerinin ara karar skill'leri.
> Madde içerikleri 27.09.2026'da ArthurLegal MCP ile çekilen metne, AYM kararı `tr_aym_getir` ile okunan metne dayanır. Asistan "ihlal" tespiti yapmaz; yalnız risk işareti ve kanuni süre karşılaştırması üretir. Mahkemenin kendi hedef süreleri `[DOLDUR]` alanıdır; asistan istatistik veya ortalama süre uydurmaz.

## 1. Dayanak

- Herkes adil yargılanma hakkına sahiptir (AY m. 36/1). Davaların en az giderle ve mümkün olan süratle sonuçlandırılması yargının görevidir (AY m. 141/4).
- AYM, makul sürede yargılanma hakkını AY m. 36'daki adil yargılanma hakkının kapsamında görür ve AY m. 141'i de bu değerlendirmede gözetir (AYM, B. No: 2014/176, 09.09.2015, § 30).
- Hâkim, yargılamanın makul süre içinde ve düzenli biçimde yürütülmesini ve gereksiz gider yapılmamasını sağlamakla yükümlüdür (HMK m. 30).

## 2. AYM'nin ölçütleri (B. No: 2014/176, 09.09.2015)

- **§ 31:** davanın karmaşıklığı, yargılamanın kaç dereceli olduğu, tarafların ve ilgili makamların tutumu, başvurucunun davanın hızla sonuçlandırılmasındaki menfaatinin niteliği.
- **§ 33 (ceza):** süre, suç isnadının yetkili makamlarca bildirilmesi, isnattan ilk etkilenilen arama veya gözaltı gibi tedbirler ya da kamu davasının açılmasıyla başlar; isnadın nihai olarak karara bağlandığı tarihte biter.
- **§ 34:** gecikme, gerekli özenin gösterilmemesinden olduğu kadar yapısal sorunlardan ve organizasyon eksikliğinden de doğabilir. Kalemdeki rutin işlerde aksamalar, hükmün yazılmasında, dosyanın bir mahkemeden diğerine gönderilmesinde yaşanan gecikmeler, hâkim ve personel yetersizliği ile iş yükü nedeniyle sürenin aşılmasında da yetkili makamların sorumluluğu gündeme gelir.
- **§ 35:** sanık sayısı ile suçun vasıf ve mahiyeti de dikkate alınır.
- **§ 36:** AYM, derece mahkemelerinin mevzuattaki sürelere uyup uymadığını denetlemez; yargılama süresinin bütününü ele alır.

**Mahkeme için anlamı:** kalemde bekleyen tebligat, gecikmiş dosya gönderme ve gerekçeli karar yazımı da süre hesabına girer. `makul-sure-izleyici` bu nedenle yalnız duruşma aralarını değil, kalem adımlarını da izler.

## 3. Kanundaki hız kuralları

| Konu | Kural | Madde |
|---|---|---|
| Hukukta duruşma arası (7589 s.K.) | üç aydan uzun olamaz; bilirkişi incelemesinin uzaması veya istinabe gibi zorunlu hâllerde gerekçe gösterilerek daha uzun | HMK m. 147/3 |
| Basit yargılama | ilk duruşma hariç tahkikat iki duruşmada; duruşmalar arası en çok bir ay; zorunlu hâllerde gerekçeyle daha uzun ve ikiden fazla duruşma | HMK m. 320/3 |
| Ön inceleme | tek duruşmada; zorunlu hâlde bir defaya mahsus yeni gün | HMK m. 140/4 |
| Gerekçeli karar (hukuk) | yalnız hüküm sonucu tefhim edilmişse tefhimden itibaren bir ay | HMK m. 294/4 |
| Gerekçe (ceza) | gerekçe tutanağa geçirilmemişse hükmün açıklanmasından itibaren en geç on beş gün içinde dosyaya konur | CMK m. 232/3 |
| İdari yargıda sıra | öncelikli ve ivedi işler dışındaki dosyalar tekemmül sırasına göre ve tekemmülden itibaren en geç altı ay içinde sonuçlandırılır | İYUK m. 20/5 |
| İdari yargıda karar yazımı | kararlar verildiği tarihten itibaren otuz gün içinde yazılır ve imzalanır; yürütmenin durdurulması kararları on beş gün içinde | İYUK m. 24, 27/9 |
| İvedi yargılama | tekemmülden itibaren en geç bir ay | İYUK m. 20/A/2-f |
| İcra mahkemesi | duruşmasız işlerde en geç on gün; duruşma ancak zorunlulukla ve otuz günü geçmemek üzere ertelenebilir | İİK m. 18/3 |
| İşe iade | dava ivedilikle sonuçlandırılır | 4857 s.K. m. 20/3 |
| Tutukluluk | kanuni azami süreler | CMK m. 102 |
| Yargıtay (hukuk) | duruşma günü karar verilemeyen işler en geç bir ay içinde | HMK m. 369/6 |

## 4. Tazminat Komisyonu (6384 s.K.)

- Ceza soruşturma ve kovuşturmaları ile özel hukuk ve idare hukuku yargılamalarının makul sürede sonuçlandırılmadığı iddiasıyla manevi tazminat istemleri Komisyona yapılır (6384 s.K. m. 2/3-a); idari nitelikteki soruşturmalardan doğan başvurular kapsam dışıdır (m. 2/4).
- Müracaat süreç devam ederken ya da en geç kesin kararın öğrenilmesinden itibaren bir ay içinde yapılır; haklı mazeret hâlinde mazeretin kalkmasından itibaren on beş gün (m. 5/A/1).
- Komisyon kararlarına tebliğden itibaren on beş gün içinde Ankara Bölge İdare Mahkemesine itiraz edilebilir; itiraz üç ay içinde karara bağlanır, kararı kesindir (m. 7/4).
- Komisyonun kesinleşen kararının örneği işlemin yapıldığı adli veya idari mercie gönderilir; işlem henüz sonuçlanmamışsa ilgili merci ivedilikle sonuçlandırır (m. 8). Bu yazının geldiği dosya `makul-sure-izleyici` listesinde 🔴 işaretlenir.
- AYM'de derdest olmuş belirli bireysel başvurular için geçiş hükümleri geçici m. 2 ve geçici m. 3'tedir.

## 5. Bilgi: disiplin hükmü

Kanun ve diğer mevzuat ile karar ve talimatlarda açıkça belirtilen konularda işi uzatacak davranışlar ile yazı ve tekitlerin zamanında cevaplandırılmaması, Hâkimler ve Savcılar Kanunu'nda uyarma cezasını gerektiren hâller arasında sayılır (2802 s.K. m. 63/2-d). 7589 s.K. ile, mesleğin gerektirdiği hukuki bilgiyle çözümlenebilecek konularda bilirkişiye başvurmak da bu hâllere eklenmiştir (m. 63/2-f); ayrıntı `bilirkisi-rapor-izleyici`.

## 6. Kontrol listesi (izleyici ve kalem için)

- [ ] Son duruşmadan bu yana geçen süre ve bir sonraki gün: HMK m. 147/3 veya 320/3 sınırı aşılıyor mu; aşılıyorsa ara kararda gerekçe var mı?
- [ ] Bilirkişi dosyası: rapor süresi ve ek süre (HMK m. 274; `bilirkisi-rapor-izleyici`).
- [ ] Bekleyen tebligat: e-Tebligat zorunlu muhatap mı (7201 s.K. m. 7/a)?
- [ ] Gerekçeli karar yazım süresi: HMK m. 294/4, CMK m. 232/3, İYUK m. 24 ve 27/9.
- [ ] Kanun yolu için dosya gönderimi: cevap süresi dolduktan sonra bekleyen dosya (HMK m. 347/3; CMK m. 277/2; İYUK m. 48/4).
- [ ] İşlemden kaldırılan dosyada üç aylık yenileme süresi doldu mu; açılmamış sayılma kararı resen verilir (HMK m. 150/5).
- [ ] İdari yargıda tekemmülden altı ay (İYUK m. 20/5).
- [ ] Tutukluluk süresi (CMK m. 102; `tutukluluk-inceleme-izleyici`).
- [ ] 6384 s.K. m. 8 bildirimi gelen dosya.

## 7. Çıktı dili

- "Makul süre aşıldı" değil, "makul süre riski: [neden]" yazılır. Hukuki değerlendirme hâkimindir.
- Süreler dosyadaki tarihlerden hesaplanır; tarih eksikse "tarih bilinmiyor, en erken olası tarih esas alındı" uyarısı eklenir.
- Mahkeme hedefleri: `[DOLDUR — örn. tensipten ön incelemeye hedef gün sayısı]`.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): AY m. 36, 141; HMK m. 30, 140, 147, 150, 274, 294, 320, 347, 369; CMK m. 102, 232, 277; İYUK m. 20, 20/A, 24, 27, 48; İİK m. 18; 4857 s.K. m. 20; 6384 s.K. m. 2, 5/A, 7, 8, geçici m. 2, geçici m. 3; 2802 s.K. m. 63; 7201 s.K. m. 7/a. AYM B. No: 2014/176 kararı `tr_aym_getir` ile okundu (§§ 30-36).*
