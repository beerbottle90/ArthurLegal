> **Durum:** Konvansiyon rehberi (erişim gerektirmez). `contract-drafting` eklentisinin (redline-contract, belge-turet, versiyon-karsilastir, tadil-protokol, playbook-inceleme) ev redline, yorum ve sözleşme yazım standardı. Bölüm 5 ve bölüm 7 ile 11 arası, ticari sözleşme ve satınalma şartnamelerinden oluşan bir örnek setten çıkarılmıştır; kalıp değil örnektir. Sistem talimatlarının 1. ve 3. bölümleriyle uyumludur; çelişki hâlinde sistem talimatı üstündür. [Şirket/Büro adı]

# Sözleşme Yazımı, Redline ve Yorum Konvansiyonları: Pratik Rehber

## 1. Ortam ve çıktı biçimi

1. Dosya üretimi açık olan her ortamda (Claude.ai'da dosya oluşturma, Claude Code) redline gerçek izlenen değişiklik içeren `.docx` olarak verilir: `w:ins` ve `w:del` öğeleri, `w:author="ArthurLegal"`, tarih o günün tarihi; yorumlar `w:comment` ile `w:author="ArthurLegal"`, `w:initials="AL"`. python-docx ile `core_properties.author` ve `core_properties.last_modified_by` de `ArthurLegal` olur.
2. Dosya üretimi kapalıysa redline metin olarak verilir: silinen kısım `[silinen: ...]`, eklenen kısım `[eklenen: ...]`. Üstü çizili, kalın ve renk kullanılmaz. Kullanıcıya "Word'de Değişiklikleri İzle açıkken uygulayın" notu düşülür.
3. Dosya adı alt çizgili ve Türkçe karaktersizdir: `hizmet_sozlesmesi_redline_05092026.docx`.
4. Kullanıcının yüklediği belgede var olan biçim korunur; değiştirilen bölümler belgenin kendi biçimini izler.

## 2. Yorum yapısı (her zaman fallback ile)

Yorum tek paragraf düz metindir; emoji, tire, başlık ve kalın kullanılmaz. Sıra sabittir: önem derecesi kelimeyle, sorun, tercih edilen pozisyon, kabul edilmezse asgari pozisyon.

```
Yüksek: Sorumluluk tavanı sözleşme bedelinin yüzde 50'sine çekilmiş; müvekkil için risk. Tercih: tavan sözleşme bedeline eşit olsun, kasıt ve ağır kusur hariç tutulsun. Kabul edilmezse asgari: yüzde 75 ve can ve mal güvenliği istisnası.
```

## 3. Önem derecesi (dört kademe, kelimeyle)

Bloklayıcı: imzalanmaz. Yüksek: müzakere şart. Orta: düzeltme gerekli, işlemi bozmaz. Düşük: bilgi notu. Üst incelemenin Bloklayıcı dediği bulgu alt incelemede sessizce düşürülmez. Renkli daire veya simge kullanılmaz; knowledge dosyalarındaki renk kodları bu kelimelere çevrilir.

## 4. Sessiz düzeltme ve yorum ayrımı

Sessiz düzeltilir: yazım, atıf ve numara, tutarlılık, tanım hizalama. Yorum zorunludur: hukuki veya ticari pozisyon değişikliği, risk dağılımı, tutar, süre ve eşik, sorumluluk, fesih, uygulanacak hukuk ve yetki.

## 5. Standart kloz seti (her ticari sözleşmede kontrol)

Uzun form sözleşmede aşağıdakilerin her biri ayrı maddedir; şartname, sipariş genel koşulları ve kısa formda kısaltılmış hâlleri bulunur. Parantezdeki kanun maddeleri yalnız hangi maddenin çekileceğini gösterir; belgeye yazılmadan önce sistem talimatı bölüm 4 madde 9'daki doğrulama kapısından geçer. "Örnek" diye verilen süre ve oranlar başlangıç noktasıdır, işin riskine göre değişir.

1. Mücbir sebep ve aşırı ifa güçlüğü (TBK m. 136 ve 138). Tanım üç unsurla kurulur: sözleşme kurulurken öngörülemeyen, tarafların kontrolü dışında gelişen ve makul özene rağmen önlenemeyen olay. Örnek olaylar sayılır (doğal afet, salgın ve buna bağlı resmî kısıtlamalar, savaş, terör, genel grev, makul önleme rağmen gerçekleşen siber saldırı, ifayı doğrudan engelleyen kamu tasarrufu). Mücbir sebep sayılmayanlar açıkça yazılır: tarafın mali durumunun bozulması, piyasa değişikliği, tarafın kendi işyerine özgü grev, alt yüklenicinin temerrüdü. Etkilenen taraf kısa bir süre içinde (örnek: 3 gün) olayı, başlangıcını, etkilenen yükümlülükleri, tahmini süreyi ve aldığı önlemleri yazılı bildirir; süresinde bildirmeyen mücbir sebebe dayanamaz. Yalnız etkilenen yükümlülükler askıya alınır, muaccel ödeme borcu sürer. Uzun süren mücbir sebepte iki tarafa fesih hakkı tanınır (örnek: kesintisiz 30 gün ya da toplam 60 gün) ve fesihte ifa edilmiş edimlerin bedeli dışında tazminat istenmez. Enerji işlerinde şebeke kesintisi, mevzuat değişikliği ve kuraklık (HES) ayrıca değerlendirilir.
2. Sorumluluk ve ceza koşulu (TBK m. 115, 179 ile 182; TTK m. 22). Ceza koşulunun bağlandığı ihlal (gecikme, hiç ya da gereği gibi ifa etmeme), oranı, toplam tavanı, tavana ulaşınca fesih hakkı ve cezayı aşan zararın istenebileceği yazılır. Gecikme cezası asıl borçla birlikte istenebilir; ancak alacaklı ifayı çekincesiz kabul ederse bu hakkı kaybeder (TBK m. 179/2). Bu yüzden kabul ve tutanak hükümlerinde ceza hakkının saklı olduğu yazılır. Hâkim aşırı gördüğü cezayı kendiliğinden indirir (TBK m. 182/3); tacir sıfatını taşıyan borçlu ise aşırılık iddiasıyla indirim isteyemez (TTK m. 22), bu da tacirler arası sözleşmede oranın baştan doğru konmasını önemli kılar. Sorumluluk sınırı konursa kasıt ve ağır kusur dışarıda tutulur; ağır kusurdan sorumsuzluk anlaşması kesin olarak hükümsüzdür (TBK m. 115/1).
3. Ödeme süresi (TTK m. 1530/5). Ödeme süresi faturanın ya da mal veya hizmetin alındığı ya da kabul usulünün tamamlandığı tarihten itibaren en fazla 60 gündür. Daha uzun süre ancak açıkça kararlaştırılır ve alacaklı aleyhine ağır haksızlık yaratmamalıdır; alacaklı KOBİ ya da tarımsal veya hayvansal üretici ise ya da borçlu büyük ölçekli işletme ise 60 gün aşılamaz.
4. Vergi, resim ve harçlar (`damga-vergisi-rehberi.md`). Damga vergisinin kime ait olduğu ve nasıl yansıtılacağı, KDV dışındaki vergilerin bedele dâhil olduğu, yabancı tarafa ödemede stopaj ve gross-up yazılır; oranlar belgeye yazılmadan önce güncel mevzuattan doğrulanır.
5. Kişisel verilerin korunması (KVKK m. 9 ve 12/5). Tarafların sıfatı (veri sorumlusu, veri işleyen) yazılır. Veri işleyen verileri yalnız sözleşmenin ifası için ve talimata göre işler, teknik ve idari tedbirleri alır, erişimi bilmesi gerekenlerle sınırlar, ilgili kişi başvuruları ve Kurul süreçleri için destek verir, sözleşme sona erince verileri iade eder ya da yok eder. Alt veri işleyen ve yurt dışına aktarım yazılı izne bağlanır; yeterlilik kararı yoksa aktarım standart sözleşme gibi uygun bir güvenceyle yapılır ve standart sözleşme imzadan itibaren beş iş günü içinde Kuruma bildirilir (KVKK m. 9/5). Veri ihlalini öğrenen veri işleyen, veri sorumlusunun en kısa sürede bildirim yükümlülüğünü (KVKK m. 12/5) yerine getirebilmesi için kısa bir süre içinde (örnek: 24 saat) bildirir. Denetim hakkı, idari para cezaları dâhil tazmin ve kapsamlı veri işlemede ayrı veri işleme protokolü eklenir; çelişkide veriyi daha iyi koruyan hüküm uygulanır.
6. Etik ve yolsuzlukla mücadele. Karşı tarafın etik kurallara uyması; rüşvet, irtikâp, nüfuz ticareti, suç gelirlerinin aklanması, terörizmin finansmanı, ihaleye fesat karıştırma ve kolaylaştırma ödemesi yasağı; Türk mevzuatı (TCK, Kabahatler Kanunu, 5549 ve 6415 sayılı Kanunlar) ve uygulanabildiği ölçüde FCPA ile UK Bribery Act; yükümlülüğün çalışanlara ve alt yüklenicilere yayılması; kayıt tutma ve denetim; aykırılığın bildirilmesi; aykırılığın esaslı ihlal sayılması ve derhal tazminatsız fesih.
7. Yaptırım ve ihracat kontrolü (`yaptirim-tarama-rehberi.md`). Yaptırım mevzuatı geniş tanımlanır: Türkiye (6415 ve 7262 sayılı Kanunlar uyarınca alınan kararlar dâhil), BM Güvenlik Konseyi, AB, Birleşik Krallık (OFSI) ve ABD (OFAC ve Ticaret Bakanlığı); proje finansmanında uluslararası finans kuruluşlarının yasaklı listeleri. Karşı taraf; kendisinin, yöneticilerinin ve kendisini kontrol edenlerin listede olmadığını, listedeki kişilerce tek başına ya da birlikte yüzde 50 ya da daha fazla oranda sahip olunmadığını veya kontrol edilmediğini ve kapsamlı yaptırım uygulanan bir ülkede kurulu olmadığını beyan eder. Mal, yazılım ve teknolojinin menşei ile ihracat kontrol sınıflandırması talep üzerine bildirilir, gereken lisanslar karşı taraf masrafıyla alınır. Durum değişikliği derhal bildirilir. Aykırılıkta ödemeler ve edimler askıya alınabilir ya da sözleşme derhal feshedilir; hiçbir hüküm tarafı yaptırıma aykırı davranmaya zorlayacak biçimde yorumlanamaz.
8. Bilgi ve siber güvenlik. ISO/IEC 27001 ya da eşdeğer bir çerçeveyle uyumlu tedbirler; asgari olarak erişim yönetimi, çok faktörlü kimlik doğrulama, şifreleme, zararlı yazılıma karşı koruma, güncellemelerin zamanında uygulanması, kayıt tutma, yedekleme ve iş sürekliliği. 7545 sayılı Siber Güvenlik Kanunu ve sektörel düzenlemelerden doğan yükümlülükler. Güvenlik olayının kısa bir süre içinde (örnek: 24 saat) bildirilmesi, olayın giderilmesinde iş birliği ve onaysız kamuya açıklama yapılmaması. Denetim ya da bağımsız denetim raporu ve sertifika talebi; alt yükleniciye aynı yükümlülük; sona ermede verinin iadesi ya da yok edilmesi.
9. Yapay zekâ kullanımı. Yapay zekâ aracı geniş tanımlanır (üretken uygulamalar dâhil). Karşı taraf gizli bilgiyi ve kişisel veriyi bir araca ancak yazılı onayla ve verinin model eğitiminde kullanılmayacağı, üçüncü kişilerle paylaşılmayacağı kurumsal kullanım koşullarıyla girebilir. Yapay zekâ yardımıyla hazırlanan çıktının doğruluğundan, mevzuata ve fikri mülkiyete uygunluğundan ve yetkin bir insan tarafından denetlenmesinden kendisi hazırlamış gibi sorumludur; talep üzerine hangi çıktıda hangi aracın kullanıldığını bildirir. Kişiler üzerinde hukuki sonuç doğuran kararlar yalnız otomatik işlemeyle alınmaz. Aykırılık gizlilik ve kişisel veri hükümlerinin ihlali sayılır.
10. Sürdürülebilirlik, insan hakları ve sorumlu tedarik. Çocuk işçi, zorla çalıştırma ve insan ticareti yasağı; ayrımcılık ve tacizin önlenmesi; İş Kanunu ve İş Sağlığı ve Güvenliği Kanunu başta olmak üzere çalışma mevzuatına uyum; çevre mevzuatına uyum ve talep üzerine enerji tüketimi, emisyon ve sosyal performans verisinin paylaşılması; yükümlülüklerin tedarik zincirine yayılması ve denetim. Esaslı aykırılıkta giderme süresi verilir, giderilmezse fesih; çocuk işçi, zorla çalıştırma ve insan ticaretinde süre verilmez.
11. Gizlilik. Gizli bilgi geniş tanımlanır (sözleşmenin kendisi, ticari sırlar, fiyatlar, teknik bilgi, kişisel veri). Kullanım yalnız ifa amacıyla; açıklama yalnız bilmesi gerekenlere ve en az aynı yükümlülükle; dört istisna (kamuya mal olmuş, önceden meşru olarak sahip olunan, bağımsız geliştirilen, kanunen açıklanması zorunlu; sonuncusunda önceden bildirim ve yalnız zorunlu kısmın açıklanması); sona ermede iade ya da yok etme; ad, marka ve sözleşmenin referans olarak kullanılması yasağı; yükümlülüğün sona ermeden sonra sürmesi; önceki gizlilik sözleşmesiyle ilişkide daha koruyucu hükmün uygulanması.
12. Fikri ve sınai mülkiyet. Sözleşme kapsamında üretilen çıktıların hakları (devir ya da lisans; kapsamı, süresi, yeri), tarafların önceden var olan haklarının saklı tutulması, üçüncü kişi hak ihlali iddiasında tazmin ve savunma.
13. Uygulanacak hukuk ve uyuşmazlık çözümü (TTK m. 5/A; HMK m. 17). Türk hukuku; önce yetkililer arasında görüşme; konusu bir miktar para olan alacak, tazminat, itirazın iptali, menfi tespit ve istirdat davaları gibi ticari davalarda dava şartı olarak arabuluculuk; münhasır yetkili mahkeme (tacirler arasında yetki sözleşmesi) ya da tahkim (örnek: İstanbul Tahkim Merkezi kuralları; hakem sayısı, yer ve dil yazılır). Tahkim şartı ile münhasır yetkili mahkeme hükmü birlikte bırakılmaz. Yabancı taraf, ICC ya da LCIA tercihi için `governing-law-review`.
14. Delil sözleşmesi (HMK m. 193). Ticari defterlerin, yetkililer arasındaki kurumsal e-posta ve KEP yazışmalarının, dekont, fatura, tutanak ve sistem kayıtlarının delil olacağı kararlaştırılır. Hüküm tarafların öteki ispat imkânlarını kaldırmaz; bir tarafın ispat hakkını imkânsız kılan ya da fevkalade güçleştiren delil sözleşmesi geçersizdir (HMK m. 193/2).
15. Bildirim (TTK m. 18/3). Sözleşmedeki adresler tebligat adresi sayılır; olağan yazışma e-posta ile yapılabilir. Temerrüde düşürme, fesih ve dönme ihbarları ise tacirler arasında noter, taahhütlü mektup, telgraf ya da güvenli elektronik imzalı KEP ile yapılır. Adres ve iletişim kişisi değişikliği kısa sürede (örnek: 7 gün) bildirilir. Her taraf için adres, ticaret sicil numarası, vergi dairesi ve numarası, KEP adresi, e-posta, telefon ve iletişim kişisi yazılır. Faks bildirim yolu olarak yazılmaz.
16. Elektronik imza (5070 sayılı Kanun m. 5). Sözleşme güvenli elektronik imzayla imzalanabilir; bu imza elle atılan imzayla aynı sonucu doğurur. Resmî şekle veya özel merasime tabi işlemler ile banka teminat mektupları ve Türkiye'de yerleşik sigorta şirketlerinin kefalet senetleri dışındaki teminat sözleşmeleri güvenli elektronik imzayla kurulamaz.
17. Genel işlem koşulları (TBK m. 20, 21 ve 24). Önceden tek taraflı hazırlanıp çok sayıda sözleşmede kullanılan standart metin genel işlem koşulu sayılabilir. Karşı taraf aleyhine olan koşullar ancak açıkça bilgi verilip içeriği öğrenme imkânı sağlanır ve karşı taraf kabul ederse bağlar, aksi hâlde yazılmamış sayılır. Her hükmün tartışılarak kabul edildiğine ilişkin kayıt tek başına bu sonucu değiştirmez (TBK m. 20/3); bu yüzden bilgilendirme ve kabul beyanına ek olarak müzakere yazışmaları saklanır. Düzenleyene karşı taraf aleyhine tek taraflı değiştirme yetkisi veren kayıt yazılmamış sayılır (TBK m. 24).
18. Diğer hükümler. Sözleşmenin bütünlüğü ve bölünebilirlik; ekler ve öncelik sırası (sözleşme metni ile ek çeliştiğinde, ekteki hükmün geçerli olacağı açıkça kararlaştırılmadıkça sözleşme metni uygulanır); devir ve temlik yasağı; değişikliklerin yazılı yapılması; takas ve mahsup; tarafların birbirini temsil yetkisinin bulunmaması; süre ve yenileme; rekabet yasağı (`rekabet-hukuku-rehberi.md`).
19. Sektöre özgü klozlar. Enerji işlerinde EPDK lisans ve pay devri ön onayı (kontrol değişikliği) ve akreditif; proje finansmanında kredi verenin onayı; saha işlerinde iş sağlığı, güvenliği ve çevre şartnamesi ile olay başına uygunsuzluk cezası.

## 6. Üst başlık ve onay

Her çıktının ilk satırı:

```
TASLAK. DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ([Baş Hukuk Müşaviri]) ONAYI ALINMADAN İMZALANMAZ.
```

Her çıktı taslaktır; imza öncesi onay zinciri: [Baş Hukuk Müşaviri], yüksek tutar veya stratejik işlemde [Genel Müdür], SHA reserved matter'da [Yönetim Kurulu] ve kredi veren veya ortak kuruluş onayı.

## 7. Sözleşme kurarken örneklerden yararlanma

1. Bölüm 5 ve bölüm 8 ile 11 arası, bir örnek sözleşme ve şartname setinden çıkarılmış yapı, karar ve yazım notlarıdır. Kalıp değildir: metin kelimesi kelimesine aktarılmaz; işin taraflarına, sektörüne, tutarına ve pazarlık gücüne göre yeniden kurulur. Örnek değerler (oran, süre, tavan) yalnız başlangıç noktasıdır.
2. Öncelik sırası: kullanıcının yüklediği şablon veya emsal belge, sonra büronun playbook'u ve profil dosyaları (`firm-profile.md` ya da `company-profile.md`, ilgili pratik profili), sonra bu rehber. Çelişkide üstteki uygulanır ve fark İnceleme notunda söylenir.
3. Örnekler mal ve hizmet alan tarafın lehine kuruludur. Satıcıyı ya da hizmet vereni temsil ederken denge tersine kurulur: ceza koşulu ve fesih hakları karşılıklı yapılır, sorumluluğa tavan konur, tek taraflı askıya alma, değiştirme ve sebepsiz fesih yetkileri daraltılır ya da bir bedele bağlanır.
4. Bilinmeyen değer `[DOLDUR: ...]` biçiminde bırakılır; kullanıcının belgesi `[●]` kullanıyorsa o korunur. Seçenekli ifade köşeli ayraç içinde eğik çizgiyle yazılır: `[ilk 3 faturadan eşit oranda / ilk faturadan tamamı]`.
5. İşe uymayan fıkra çıkarılır (avans yoksa avans maddesi ve tanımı; teminat yoksa teminatı irat kaydetmeye ilişkin bütün ifadeler), ardından bütün iç atıflar yeniden kontrol edilir. Numaranın korunması gerekiyorsa fıkranın yerine `[KULLANILMADI]` yazılır.
6. Kullanıcıya bırakılan taslak notu belge gövdesine değil Word yorumuna yazılır (yazar ArthurLegal, AL); bölüm 2'deki sırayı izler, yalnız bilgi veren not "Düşük:" ile başlar.

## 8. Belge türleri ve iskeletler

1. Uzun form sözleşme (iki tarafın imzaladığı, tanımlı terimli). Olağan madde sırası: taraflar; konu ve nitelik; tanımlar; süre; bedel ve ödeme şartları; fiyat farkı talep yasağı; karşı tarafın hak ve yükümlülükleri; alıcının hak ve yükümlülükleri; teminat; garanti ve ayıp; sigorta; değişiklikler, ilave işler ve süre uzatımı; askıya alma; mücbir sebep; fesih; taahhüt, zarar tazmini ve ceza koşulu; kişisel verilerin korunması; etik; yaptırım; bilgi ve siber güvenlik; yapay zekâ; sürdürülebilirlik; gizlilik; fikri mülkiyet; bütünlük ve bölünebilirlik; vergi, resim ve harçlar; uygulanacak hukuk ve uyuşmazlık; temsil yetkisinin bulunmaması; takas ve mahsup; delil sözleşmesi; bildirimler; diğer hükümler (ekler ve öncelik, elektronik imza, bilgilendirme ve kabul); imza ve yürürlük.
2. Satınalma şartnamesi ve sipariş genel koşulları (sipariş emriyle kurulan kısa form). Sıra: giriş ve konu; bütünlük ve bölünebilirlik; fiyat ve ödeme; teslimat ya da hizmetlerin tamamlanması; muayene ve testler; garanti; askıya alma ve uzatma; fesih; tazmin ve sorumluluk; mülkiyet ve riskin geçişi; sigorta; bölüm 5'teki genel hükümlerin kısa hâlleri; fikri mülkiyet; diğer hükümler; vergi; uygulanacak hukuk. Hizmet içeren şartnameye bağımsız işveren ve iş sağlığı ve güvenliği maddeleri eklenir. Şartname ile sipariş emri arasındaki öncelik yazılır.
3. Türe özgü maddeler:
   a. Mal alımı ve çerçeve sözleşme: çerçeve ile sipariş emri ilişkisi (siparişin verilmesi ve teyidi, çerçeve hükümlerinin her siparişe uygulanması), teslim yeri ve Incoterms 2020 kuralı, muayene ve kabul, ayıp ihbarı, mülkiyet ve hasarın geçişi, sipariş bazında fesih.
   b. Hizmet, danışmanlık ve eğitim: hizmet planı ve performans denetimi; personel (asıl işveren ile alt işveren ilişkisi kurulmadığı, işe giriş ve SGK belgeleri, işçilik alacaklarından sorumluluk); hizmet tamamlama tutanağı; ilave işler. Danışmanlıkta çıktıların mülkiyeti ve çıkar çatışması; eğitimde katılımcı verileri için ayrı veri aktarım protokolü.
   c. Eser ve inşaat: işe başlama ve tamamlama süreleri, iş programı, malzeme ve ekipman, geçici ve kesin kabul, mülkiyet ve hasarın geçişi, işin askıya alınması, iş sağlığı ve güvenliği ile çevre, saha teslimi ve temizliği, tüm riskler sigortası.
   d. Karayolu taşıma: sözleşme belgeleri ve öncelik, taşıma talebi ve araç tahsisi, yükleme ve teslim süreleri, taşıyıcının personel ve araç yükümlülükleri, kayıt ve raporlar, sağlık, emniyet ve çevre, teminat mektubu, ceza koşulu tablosu, taşıyıcının bağımsızlığı. Taşıyıcının sorumluluğu ve sınırları yazılmadan önce TTK'nın taşıma hükümleri çekilir.
   e. Sponsorluk: sponsorluk bedeli ve aşamalı ödeme, karşı edimler (görünürlük, logo ve marka kullanımının sınırları), etkinliğin iptali ya da ertelenmesinde bedelin akıbeti, itibar zedeleyici davranışta fesih.
   f. İş birliği ve mutabakat zaptı: amaç ve görevler; bağlayıcı hükümlerin (gizlilik, fikri mülkiyet, uygulanacak hukuk, masraflar) bağlayıcı olmayan ticari niyet beyanlarından açıkça ayrılması; temsilcilik ilişkisinin bulunmaması; devir yasağı.
   g. Aracılar arası iş birliği: portföy ve müşteri paylaşımı, bedel ve komisyonun bölüşülmesi, müşteriyle doğrudan temas yasağı, temsil yetkisinin bulunmaması.
   h. Veri aktarım protokolü (sözleşme eki): tarafların sıfatları, aktarılan veri kategorileri, aktarım, saklama ve imha, ilgili kişi başvuruları, veri güvenliği, denetim, sorumluluk.
   i. İngilizce genel koşullar (yabancı tedarikçi): aynı iskelet ve Türk hukuku; Incoterms 2020; dövizli alacakta gecikme faizi için para birimine göre güncel gösterge oran (ör. USD için Term SOFR, EUR için €STR) artı marj. LIBOR yazılmaz.

## 9. Ticari maddelerde karar listesi

Aşağıdaki her kalem için taslakta bir karar ya da `[DOLDUR: ...]` bulunur. Parantezdeki değerler örnek setteki tipik değerlerdir; işin riskine göre değişir.

1. Süre: başlangıç (imza ya da belirli tarih), bitiş, kendiliğinden yenileme ve yenilememe bildirimi.
2. Bedel: birim fiyat ya da götürü; azami sözleşme bedeli (tutar artı KDV); konaklama ve ulaşım gibi masrafların bedele dâhil olup olmadığı ve ön onaya bağlanması; dövizle belirlenen bedelin hangi kurla (TCMB döviz satış kuru gibi) ve hangi tarihte Türk lirasına çevrileceği; fiyat farkı talep yasağı.
3. Ödeme: hakediş ya da fatura dönemi, ödeme süresi (bölüm 5 madde 3'teki 60 gün sınırı), ödemeye eklenecek belgeler (hizmet işlerinde SGK ve ücret belgeleri), eksik belgenin sonucu, gecikmede faiz.
4. Avans: tutar (sözleşme bedelinin yüzde 20'sini aşmaması önerilir), mahsup yöntemi, avans tutarında avans teminat mektubu.
5. Kesin teminat: oran (en az yüzde 10, işin riskine göre artar); güvence altına aldığı borçlar (işçilik alacakları ve SGK borçları dâhil); süre uzatımında mektubun da uzatılması; iade koşulları (garanti süresinin bitmesi, tamamlama tutanağı, ilişiksiz belgesi); yurt dışı bankanın mektubunda Türkiye'de kurulu bir bankanın kontrgarantisi; masrafın kime ait olduğu. Teminat alınmayacaksa irat kaydına ilişkin bütün ifadeler çıkarılır.
6. Gecikme cezası: günlük oran ve toplam tavan (sipariş genel koşullarında günlük yüzde 0,5 ve toplam yüzde 10; hizmet genel koşullarında günlük binde 2 ve toplam yüzde 20), tavana ulaşınca fesih hakkı, kabul ve tutanaklarda ceza hakkının saklı tutulması (bölüm 5 madde 2).
7. Garanti ve ayıp: garanti süresi ve başlangıcı (teslim ya da kabul), ayıp bildiriminden sonra giderme süresi (10 gün), giderilmezse ayıbın karşı taraf masrafıyla üçüncü kişiye giderttirilmesi ve masrafın teminattan alınması.
8. Sigorta: türleri (işveren mali sorumluluk, üçüncü kişi mali sorumluluk, nakliyat, tüm riskler) ve asgari limitler, ortak sigortalı ve rücu, poliçenin işe başlamadan sunulması. Yalnız alıcının ofisinde ya da uzaktan verilen hizmette işveren mali sorumluluk sigortası aranmayabilir.
9. Değişiklik ve ilave iş: yazılı talimat şartı, bedele ve süreye etkisinin önceden yazılı kararlaştırılması, talimatsız işin ödenmemesi.
10. Askıya alma: alıcının yazılı bildirimle askıya alma hakkı (10 gün önceden), karşı tarafın makul ek maliyeti isteyebileceği hâller, uzun askıda fesih.
11. Fesih: haklı nedenler (ihlal ve giderme süresi; iflas, konkordato ve aciz; kontrol değişikliği; yaptırım, etik ve veri ihlali), alıcının sebepsiz fesih hakkı (15 gün önceden bildirim) ve karşılığında ödenecekler, ikame alımda fiyat farkının istenmesi, fesihten sonra süren hükümler.
12. Alt yüklenici: yazılı ön onay ve alt yüklenicinin fiillerinden kendi fiili gibi sorumluluk.
13. Kapanış: madde sayısı, nüsha sayısı ya da güvenli elektronik imza, imza tarihi ve yürürlük.

## 10. Sık yapılan hatalar

1. Standart metinde tek taraflı değiştirme yetkisi ("alıcı bu koşulları tek taraflı değiştirebilir"): yazılmamış sayılır (TBK m. 24). Değişiklik yazılı ve karşılıklı kurulur; yetki korunacaksa risk İnceleme notunda yazılır.
2. 60 günü aşan ödeme süresi, özellikle alacaklı KOBİ ya da borçlu büyük ölçekli işletme olduğunda (TTK m. 1530/5).
3. Eskimiş atıf ve araçlar: mülga 818 sayılı Borçlar Kanunu ve 6762 sayılı Türk Ticaret Kanunu, LIBOR, Incoterms 2010, faksla bildirim.
4. Eski tarihli sabit tutarlar (ceza, sigorta limiti, masraf tavanı) güncellenmeden taşınmaz; `[DOLDUR: ...]` bırakılır.
5. Birden çok grup şirketinin aynı belgede birlikte alıcı yapılması: kimin borçlu ve alacaklı olduğu, faturanın kime kesileceği belirsizleşir. Tek alıcı kurulur; bağlı ortaklıkların korunması gizlilik ve tazmin hükümlerinde ayrıca yazılır.
6. Tahkim şartı ile münhasır yetkili mahkeme hükmünün birlikte bırakılması.
7. Tanımlanıp metinde hiç kullanılmayan ya da kullanılıp tanımlanmayan terim (silinen teminat maddesinden kalan "Kesin Teminat Mektubu" tanımı gibi).
8. Madde eklenip çıkarıldıktan sonra kayan iç atıflar; teslimden önce bütün atıflar taranır.
9. Mücbir sebep tanımına mali güçlük, piyasa değişikliği ya da tedarikçinin temerrüdünün alınması.
10. Ceza koşulunun asıl sözleşme geçersiz olsa bile istenebilecek bağımsız bir taahhüt olarak yazılması: asıl borç geçersizse cezanın ifası istenemez (TBK m. 182/2).
11. Kefalet ya da garanti gibi teminat sözleşmelerinin güvenli elektronik imzayla kurulması (5070 sayılı Kanun m. 5'teki istisnalar dışında).
12. Sözleşme metninde tire kullanılması: ek numarası "Ek 1", iki kavram arasındaki ilişki "asıl işveren ile alt işveren ilişkisi", aralık "yüzde 10 ile 100 arası" biçiminde yazılır (sistem talimatı bölüm 1 madde 2).

## 11. Yazım ve Word düzeni

1. Tanımlı terim ilk geçtiği yerde tanımlanır ve büyük harfle başlar ("Sözleşme", "Şirket", "Gizli Bilgi"). Çekim eki kesme işaretiyle ve ünlü uyumuna göre eklenir: Şirket'e, Satıcı'nın, Sipariş Emri'nde; iyelik ekiyle biten terimde kaynaştırma harfi korunur: İş Ortağı'na.
2. Taraflar işin türüne göre adlandırılır (Satıcı, Hizmet Veren, Yüklenici, Taşıyıcı, Danışman) ve bütün belgede aynı adla anılır; şartnamede büyük harfli ad (ALICI, FİRMA) seçildiyse belge boyunca öyle kalır.
3. Numara düzeni: madde 1., fıkra 1.1., alt fıkra 1.1.1., bent (a), alt bent (i). İç atıf numarayla yapılır ("9.2.1 maddesi"); Word'de otomatik numara ve çapraz başvuru kullanılır.
4. Süre ve oranlar rakam ve yazıyla yazılır: 30 (otuz) gün, yüzde 10 (on). Tutarlar 1.250.000 TL + KDV biçimindedir. "Gün" ile "İş Günü" ayrımı tanımlarda yapılır.
5. Word düzeni: Times New Roman 11 punto, A4, kenar boşlukları 2,5 cm, gövde iki yana yaslı. Madde başlıkları büyük harfle ve kalın yazılır (sistem talimatı bölüm 1 madde 3'teki sözleşme madde başlığı istisnası); kalın bunun dışında yalnız tanımlı terimin tanımlandığı yerde kullanılır, italik ve altı çizili kullanılmaz. Sağ üstte belge adı, altta ortada "Sayfa X / Y" bulunur. Renk, logo ve çerçeve kullanılmaz.
6. Çift dilli belgede iki sütunlu, çerçevesiz tablo kullanılır: sol sütun Türkçe, sağ sütun İngilizce, her satırda aynı fıkra; numaralar iki sütunda birebir aynıdır. İki metin çeliştiğinde hangisinin üstün olduğu yazılır.
7. Kapanış cümlesi madde ve nüsha sayısını söyler: "İşbu Sözleşme [DOLDUR: ...] maddeden ibaret olup [DOLDUR: ...] tarihinde 2 (iki) nüsha olarak imzalanmıştır." Güvenli elektronik imza kullanılıyorsa nüsha yerine bu yazılır. İmza bloğunda taraf unvanı, yetkilinin adı ve unvanı bulunur.
8. Ekler sözleşmenin sonunda numaralı listeyle sayılır (Ek 1 Teknik Şartname gibi); kullanılmayan ek "[KULLANILMADI]" olarak bırakılır ki ek numaraları ve atıflar bozulmasın.
9. Dosya adı ve yazar bölüm 1'e göredir: `hizmet_sozlesmesi_taslak_22112026.docx`, yazar ArthurLegal.

## Bağlantılı referanslar

`kanun-kisaltmalar.md`, `rekabet-hukuku-rehberi.md`, `yaptirim-tarama-rehberi.md`, `kvkk-m11-cevap-sablonu.md`, `damga-vergisi-rehberi.md`, `mevzuat-mcp-rehberi.md` (bölüm 9, madde doğrulama)

*Son güncelleme: 22.11.2026. Bölüm 5 bütün ticari sözleşmelere genişletildi; sözleşme yazım rehberi (bölüm 7 ile 11) eklendi. Kanun maddeleri 22.11.2026'da mevzuat.gov.tr metninden doğrulandı: TBK m. 20, 21, 24, 115, 136, 138, 179, 182; TTK m. 5/A, 18/3, 22, 1530/5; HMK m. 17, 193; KVKK m. 9/5, 12/5; 5070 sayılı Kanun m. 5.*
