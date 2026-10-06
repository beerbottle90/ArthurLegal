# Mahkeme Türü Profili — Asliye Ceza ve Ağır Ceza Mahkemeleri

> `mahkeme-profili.md` ile birlikte okunur. Madde numaraları 27.09.2026'da ArthurLegal MCP ile çekilen metne dayanır; hüküm veya tutanak gövdesine girmeden önce yeniden çekilir. Soruşturma evresinin hâkim kararları için `sulh-ceza-hakimligi.md`.

## Kim kullanır

- **Asliye ceza:** tek hâkimli (5235 s.K. m. 9/2). **Ağır ceza:** bir başkan ve yeteri kadar üye; bir başkan ve iki üyeyle toplanır (5235 s.K. m. 9/3).
- Plugin: `ceza-hakim`, `ceza-kalem`; araştırma için `yargi-arastirma`.

## Görev ve yetki

- **Ağır ceza:** kanunların ayrıca görevli kıldığı hâller saklı kalmak üzere TCK'daki yağma, irtikâp ve resmî belgede sahteciliğin maddede gösterilen fıkraları ile hileli iflas suçları, İkinci Kitap Dördüncü Kısım 4-7. bölüm suçları (sayılan istisnalar hariç), 3713 s.K. kapsamındaki suçlar ile ağırlaştırılmış müebbet, müebbet ve on yıldan fazla hapis cezasını gerektiren suçlar; hangi TCK maddelerinin sayıldığı 5235 s.K. m. 12 metninden okunur. 7571 s.K. ile nitelikli dolandırıcılık (TCK m. 158) bu listeden çıkarılmıştır (metin dipnotu); görev, ceza üst sınırına göre yeniden belirlenir.
- **Asliye ceza:** sulh ceza hâkimliği ve ağır ceza mahkemelerinin görevleri dışında kalan dava ve işler (5235 s.K. m. 11).
- **Görev kanunla belirlenir** (CMK m. 3/1); iddianamenin kabulünden sonra işin mahkemenin görevini aştığı veya dışında kaldığı anlaşılırsa görevli mahkemeye gönderilir, adli yargı içindeki görevsizlik kararlarına itiraz edilebilir (CMK m. 5).
- **Yetki:** suçun işlendiği yer; teşebbüste son icra hareketi, kesintisiz suçta kesintinin, zincirleme suçta son suçun işlendiği yer; bilişim sistemleri, banka ve kredi kurumları veya kartların araç olarak kullanıldığı suçlarda mağdurun yerleşim yeri mahkemesi de yetkilidir (CMK m. 12).

## Usul akışı

1. **İddianamenin değerlendirilmesi:** mahkeme iddianame ve soruşturma evrakının verildiği tarihten itibaren on beş gün içinde; CMK m. 170'e aykırılık, sübuta doğrudan etkili delilin toplanmaması, önödeme, uzlaştırma veya seri muhakemenin uygulanmaması, izin veya talep yokluğu ve 7593 s.K. ile eklenen, on beş yaşını doldurmamış çocuk hakkında sosyal inceleme yaptırılmaması hâllerinde iadeye karar verir; hukuki nitelendirme sebebiyle iade edilemez; süre sonunda iade edilmeyen iddianame kabul edilmiş sayılır (CMK m. 174). `/ceza-hakim:iddianame-degerlendirme`.
2. **Kovuşturma ve duruşma hazırlığı:** iddianamenin kabulüyle kamu davası açılır; duruşma günü belirlenir (CMK m. 175). İddianame çağrı kâğıdıyla tebliğ edilir; çağrı kâğıdının tebliği ile duruşma arasında en az bir hafta bulunur (m. 176).
3. **Basit yargılama:** asliye cezada, iddianamenin kabulünden sonra adli para cezası ve/veya üst sınırı iki yıl veya daha az hapis gerektiren suçlarda; duruşma günü belirlendikten sonra uygulanmaz; beyan ve savunma için iki hafta; mahkûmiyette sonuç ceza dörtte bir indirilir; yaş küçüklüğü, akıl hastalığı ve izne veya talebe bağlı suçlarda uygulanmaz (CMK m. 251). Hükme itiraz edilebilir, süresinde itiraz edilmeyen hüküm kesinleşir; itiraz üzerine genel hükümlere göre duruşma açılır (CMK m. 252).
4. **Uzlaştırma:** kovuşturma evresinde suçun uzlaşma kapsamında olduğu anlaşılırsa dosya uzlaştırma bürosuna gönderilir; edim def'aten yerine getirilirse düşme, ileri tarihe bırakılırsa durma kararı (CMK m. 254). Kapsam için CMK m. 253/1 ve 253/3. `/ceza-hakim:uzlastirma-denetimi`.
5. **Duruşma:** hükme katılacak hâkimler, savcı, zabıt kâtibi ve zorunlu müdafilikte müdafi hazır bulunur (CMK m. 188/1); sanık hazır bulunmadan kural olarak duruşma yapılmaz (m. 193); ses ve görüntü ile sorgu (m. 196/4); delillerin tartışılması, son söz sanığa (m. 216/3); suç niteliği değişirse ek savunma (m. 226).
6. **Hüküm:** hüküm çeşitleri (CMK m. 223); hüküm iddianamedeki fiil ve fail hakkında verilir, nitelendirmede mahkeme bağlı değildir (m. 225); gerekçenin içeriği (m. 230); gerekçe tutanağa geçmemişse açıklamadan itibaren en geç on beş gün içinde dosyaya konur (m. 232/3). `/ceza-hakim:hukum-taslagi`, `/ceza-hakim:gerekce-denetimi`.

## Hükmün açıklanmasının geri bırakılması (7589 s.K.)

- 7589 s.K. (RG 31.07.2026) CMK m. 231/5-14'ü yeniden düzenledi: hükmolunan ceza iki yıl veya daha az hapis ya da adli para cezasıysa HAGB'ye karar verilebilir; koşullar arasında zararın aynen iade, eski hâle getirme veya tazmin suretiyle tamamen giderilmesi sayılır; denetim süresi beş yıldır; HAGB kararına karşı istinaf yoluna başvurulabilir (CMK m. 231/5, 231/6, 231/8, 231/12).
- Aynı fıkralar hakkında AYM'nin 10.07.2025 tarihli, E. 2024/98, K. 2025/149 sayılı iptal kararı metin dipnotuna göre 30.09.2026'da yürürlüğe girer. İki olayın derdest dosyalara etkisini hâkim değerlendirir; `ictihat-ve-aym-izleyici` ve `/ceza-hakim:hagb-degerlendirme` ile birlikte ele alın.
- Çocuklar hakkında HAGB'de denetim süresi üç yıldır; 7593 s.K. ile yönlendirme tedbirleri de uygulanabilir (5395 s.K. m. 23).

## Kritik süreler

| İşlem | Süre | Madde |
|---|---|---|
| İddianamenin iadesi | evrakın verilmesinden 15 gün | CMK m. 174/1 |
| Çağrı kâğıdı ile duruşma arası | en az 1 hafta | CMK m. 176/4 |
| Gerekçenin dosyaya konması | açıklamadan en geç 15 gün | CMK m. 232/3 |
| Basit yargılamada beyan ve savunma | 2 hafta | CMK m. 251/2 |
| Tutukluluk incelemesi | her oturumda veya 30 günlük süre içinde | CMK m. 108/3 |
| İstinaf | gerekçeli hükmün tebliğinden 2 hafta | CMK m. 273/1 |
| Temyiz | gerekçeli hükmün tebliğinden 2 hafta | CMK m. 291/1 |
| İtiraz | öğrenmeden 2 hafta | CMK m. 268/1 |
| Eski hâle getirme | engelin kalkmasından 2 hafta | CMK m. 41/1 |

Adli tatilde soruşturma ve tutuklu işlerin nasıl yürütüleceğini HSK belirler; tatile rastlayan süreler işlemez ve tatilin bittiği günden itibaren üç gün uzatılmış sayılır (CMK m. 331/2, 331/4).

## Sık usul riskleri (genel)

- 🔴 Hükmün CMK m. 230 gereği gerekçeyi içermemesi; hukuka aykırı yöntemlerle elde edilen delile dayanılması (CMK m. 289/1-g, 289/1-i).
- 🔴 Suç niteliğinin değişmesine rağmen ek savunma hakkı tanınmaması (CMK m. 226/1).
- 🔴 Zorunlu müdafi bulunmadan duruşma (CMK m. 150/2, 150/3, 188/1).
- 🔴 Son sözün sanığa verilmemesi (CMK m. 216/3).
- 🟠 18 yaşından küçük sanık için duruşmanın kapalı yapılmaması (CMK m. 185).
- 🟠 Uzlaştırma veya seri muhakeme kapsamındaki işte iddianamenin denetlenmemesi (CMK m. 174/1-c).
- 🟡 Tutukluluk incelemesinin oturumlar arasında 30 günü aşması (CMK m. 108/3; `tutukluluk-inceleme-izleyici`).

## Kalem iş akışı

- Tebligat ve çağrı (CMK m. 176), tutuklu sanığın kanun yolu beyanı (m. 263), müzekkere ve istinabe (m. 180), ses ve görüntü bağlantısı.
- Kanun yolu gönderme ve infaz evrakı: `/ceza-kalem:kanun-yolu-gonderme`, `/ceza-kalem:infaz-evraki`, `/ceza-kalem:muzekkere`, `/ceza-kalem:ceza-tebligat`, `/ceza-kalem:durusma-tutanagi`.

## Hangi skill ve izleyici ne zaman

| Durum | Skill / izleyici |
|---|---|
| İddianame geldi | `/ceza-hakim:iddianame-degerlendirme` |
| Tutuklu dosya | `/ceza-hakim:tutukluluk-incelemesi`, `tutukluluk-inceleme-izleyici` |
| Uzlaştırma raporu | `/ceza-hakim:uzlastirma-denetimi` |
| Hüküm | `/ceza-hakim:hukum-taslagi`, `/ceza-hakim:gerekce-denetimi`, `/ceza-hakim:hagb-degerlendirme` |
| Takip | `durusma-hazirlik`, `kanun-yolu-kesinlesme-izleyici`, `mevzuat-degisiklik-izleyici` |

## Veri hassasiyeti

- Mağdur çocuk veya suçun etkisiyle psikolojisi bozulmuş mağdur bir defa dinlenebilir; dinlemede uzman bulunur; cinsel suç mağduru çocukların beyan ve görüntü kayıtları gizli tutulur (CMK m. 236/2, 236/3, 236/5, 236/7).
- Örgüt faaliyeti çerçevesindeki suçlarda tanığın kimliği saklı tutulabilir (CMK m. 58/2, 58/5).
- Çocuğun kimliğinin belirlenememesine yönelik önlemler (5395 s.K. m. 4/1-l); ceza mahkûmiyeti ve güvenlik tedbiri verileri özel nitelikli kişisel veridir (KVKK m. 6/1).
- Soruşturma evresi işlemleri gizlidir (CMK m. 157); kovuşturmada duruşma açıktır, kapalılık genel ahlâk veya kamu güvenliği gereğiyle (CMK m. 182).

## Mahkemeye özgü alanlar

- Asliye ceza mı, ağır ceza mı; HSK ihtisas veya iş bölümü kararı: [DOLDUR]
- Çocuk mahkemesi sıfatı veya çocuk dosyası yoğunluğu: [DOLDUR]
- Tutuklu dosya sayısı ve ceza infaz kurumu ile SEGBİS düzeni: [DOLDUR]
- Bağlı BAM ceza daireleri: [DOLDUR]

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): 5235 s.K. m. 9, 11, 12; TCK m. 158; CMK m. 3, 5, 12, 41, 58, 108, 150, 157, 170, 174, 175, 176, 180, 182, 185, 188, 193, 196, 216, 223, 225, 226, 230, 231, 232, 236, 251, 252, 253, 254, 263, 268, 273, 289, 291, 331; 5395 s.K. m. 4, 23; KVKK m. 6.*
