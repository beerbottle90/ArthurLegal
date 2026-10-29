# Karar Anonimleştirme Rehberi

> Kullanan: `karar-yayim:anonimlestirme`, `karar-yayim:karar-kunye-ozeti`, `karar-yayim:sade-dil-ozeti`; ayrıca bir belgenin mahkeme dışına çıkan her sürümü. Dosya belgelerinin asistana verilmeden önce bilgisayarda maskelenmesi (takma adlandırma) ayrı bir iştir: `arthur-mask-rehberi.md`.
> Madde içerikleri 27.09.2026'da ArthurLegal MCP ile çekilen metne dayanır. Dosyadaki asıl karar ve UYAP kaydı değiştirilmez; anonimleştirme yalnız mahkeme dışına çıkan sürüm içindir. Hangi sürümün hangi kanalda paylaşılacağına mahkeme ve kurum karar verir: `[DOLDUR — kurum yayın ve paylaşım politikası]`.

## 1. Hukuki çerçeve

| Konu | Kural | Madde |
|---|---|---|
| Anayasal hak | herkes kişisel verilerinin korunmasını isteme hakkına sahiptir; veriler kanunda öngörülen hâllerde veya açık rızayla işlenebilir | AY m. 20/3 |
| Aleniyet | duruşmalar ve kararların bildirilmesi alenidir; kapalılık istisnadır | AY m. 141/1; HMK m. 28/1; CMK m. 182 |
| Anonim hâle getirme tanımı | kişisel verilerin, başka verilerle eşleştirilerek dahi hiçbir surette kimliği belirli veya belirlenebilir bir gerçek kişiyle ilişkilendirilemeyecek hâle getirilmesi | KVKK m. 3/1-b |
| Yargı istisnası | soruşturma, kovuşturma, yargılama veya infaz işlemlerine ilişkin olarak yargı makamlarınca işleme KVKK kapsamı dışındadır | KVKK m. 28/1-d |
| Araştırma ve istatistik | resmî istatistik ile anonim hâle getirilmek suretiyle araştırma, planlama ve istatistik amaçlı işleme KVKK kapsamı dışındadır | KVKK m. 28/1-b |
| Genel ilkeler | amaçla bağlantılı, sınırlı ve ölçülü işleme | KVKK m. 4/2 |
| Özel nitelikli veri | ırk, etnik köken, siyasi düşünce, felsefi inanç, din, mezhep, kılık kıyafet, dernek, vakıf, sendika üyeliği, sağlık, cinsel hayat, ceza mahkûmiyeti ve güvenlik tedbirleri, biyometrik ve genetik veriler | KVKK m. 6/1 |
| Çocuk | çocuklar hakkında yürütülen işlemlerde, yargılamada ve kararların yerine getirilmesinde kimliğin başkalarınca belirlenememesine yönelik önlemler | 5395 s.K. m. 4/1-l |
| Çocuk sanık | 18 yaşını doldurmamış sanıkta duruşma kapalı, hüküm de kapalı duruşmada açıklanır | CMK m. 185 |
| Mağdur kayıtları | m. 236/5-6 kapsamında (TCK m. 103/2 ve 102/2'deki suçlar; madde başlıkları "çocukların cinsel istismarı" ve "cinsel saldırı") alınan beyan ve görüntü kayıtları dosyada saklanır, kimseye verilmez, gizliliği için tedbir alınır | CMK m. 236/5-7 |
| Tanık | kimliğin ortaya çıkması ağır tehlike oluşturacaksa kimlik saklı tutulur (örgüt suçlarıyla sınırlı) | CMK m. 58/2, 58/5 |
| Soruşturma | soruşturma evresindeki usul işlemleri gizlidir | CMK m. 157 |
| Genetik veri | inceleme sonuçları kişisel veridir, başka amaçla kullanılamaz | CMK m. 80/1 |
| Şiddet mağduru | gerekirse korunan kişi ve aile bireylerinin kimlik ve adres bilgileri tüm resmî kayıtlarda gizli tutulur | 6284 s.K. m. 8/6 |
| Gizli duruşma (hukuk) | genel ahlak veya kamu güvenliğinin kesin gerekli kıldığı hâllerde; hazır bulunanlar uyarılır | HMK m. 28/2, 28/4 |
| Boşanma | taraflardan birinin istemiyle duruşma gizli yapılabilir | TMK m. 184/6 |

**Aleniyet ve anonimleştirme birlikte.** Kararların aleniyeti, kararın yayım sürümünde kişilerin kimliğinin gereksiz yere açıklanmasını gerektirmez. Yargı istisnası (KVKK m. 28/1-d) yargılama işlemlerine ilişkindir; kararın yayım, eğitim veya araştırma amacıyla dışarı verilmesinin bu istisnaya girip girmediği kurum politikasıyla belirlenir. Asistan temkinli davranır: dışarı çıkan her sürüm anonimleştirilmiş veya en azından maskelenmiş olur.

**AB çerçevesi (bilgi).** AB Yapay Zekâ Tüzüğü'nün 61. gerekçesi, yargı kararlarının, belgelerinin veya verilerinin anonimleştirilmesi veya takma adlandırılması gibi, bireysel davalarda yargı yetkisinin fiilen kullanılmasını etkilemeyen salt yardımcı idari faaliyetlere yönelik sistemlerin yüksek riskli sayılmayacağını belirtir (Regulation (EU) 2024/1689, recital 61). Tüzük Türkiye'de doğrudan uygulanmaz; ayrıntı `yargida-yapay-zeka-rehberi.md`.

## 2. Ne maskelenir

| Katman | Örnek | İşlem |
|---|---|---|
| 1. Doğrudan tanımlayıcı | ad soyad, T.C. kimlik no, pasaport no, telefon, e-posta, açık adres, IBAN, araç plakası, tapu ada/parsel, sicil ve sigorta numarası | rol etiketi: `[DAVACI]`, `[DAVALI]`, `[SANIK-1]`, `[MAĞDUR]`, `[TANIK-2]`; numaralar `[TCKN]`, `[IBAN]`, `[PLAKA]` |
| 2. Dolaylı tanımlayıcı | küçük bir yerde nadir meslek, olayın tam tarihi ve yeri, akrabalık bağı, okul veya işyeri adı, başka dosya numaraları | genelleştir: "bir ilçede", "20XX yılında", "bir özel okulda"; başka dosya numaralarını çıkar |
| 3. Özel nitelikli veri (KVKK m. 6/1) | sağlık durumu, cinsel hayat, sabıka, din, etnik köken, sendika üyeliği | gerekçe için zorunlu değilse çıkar; zorunluysa genel ifade ("sağlık raporu bulunan") |
| 4. Çocuk (5395 s.K. m. 4/1-l) | çocuğun adı, okulu, sınıfı, fotoğrafı; çocuğu tanımlatan ebeveyn bilgisi | hepsini çıkar; ebeveyn de çocuğu tanımlatıyorsa ebeveyni de maskele |
| 5. Korunan kişi | mağdur (CMK m. 236), kimliği saklı tanık (CMK m. 58/2), 6284 kapsamında korunan kişi (m. 8/6) | kimlik ve adres izine yer verme; olay anlatımını da tanımlatmayacak düzeyde genelleştir |
| 6. Yargı ve meslek mensupları | hâkim, savcı, zabıt kâtibi, avukat, bilirkişi, arabulucu adları | `[DOLDUR — kurum politikası]`; karar metninde bulunmaları kanun gereğidir (HMK m. 297/1-a; CMK m. 232/2-b), yayım sürümü ayrı değerlendirilir |
| 7. Tüzel kişi | şirket unvanı | KVKK tanımı gerçek kişiye ilişkindir (m. 3/1-d); ancak unvan gerçek kişiyi belirlenebilir kılıyorsa (ör. kişinin adını taşıyan işletme) maskele; ticari sır ayrıca değerlendirilir |
| 8. Belge izleri | dosya adı, belge özellikleri, UYAP barkodu, karekod, imza ve mühür görüntüsü, fotoğraf, kroki | çıkar veya kara kutuyla kapat; metin katmanında da sil |

**Korunması gerekenler:** kararın künyesi (mahkeme, esas ve karar numarası, tarih) emsal değeri için kurum politikası uygun görürse bırakılır; hüküm sonucu, uygulanan maddeler, hukuki gerekçe ve hesaplamalar bozulmaz.

## 3. Yöntem

- **Tutarlılık:** aynı kişiye metnin tamamında aynı etiket verilir. Baş harfler küçük yerleşimlerde kişiyi tanımlatabilir; rol etiketi tercih edilir.
- **Maskeleme ile anonimleştirme farkı:** eşleştirme tablosu (etiket - gerçek kimlik) tutuluyorsa veri KVKK m. 3/1-b anlamında anonim değildir; bu sürüm "maskeli" diye etiketlenir. Eşleştirme tablosu mahkeme dışına çıkmaz ve asistan tarafından kalıcı olarak saklanmaz.
- **Yeniden tanımlama sınaması:** "Olayı bilen bir komşu veya iş arkadaşı bu metinden kişiyi tanır mı?" sorusu her bulgu için sorulur; evetse genelleştirme artırılır.
- **Metin dışı katmanlar:** PDF'te görünmeyen metin katmanı, açıklamalar ve belge özellikleri temizlenmeden dosya paylaşılmaz.

## 4. İş akışı (`/karar-yayim:anonimlestirme`)

1. Kullanıcı amacı ve kanalı belirtir: kurum içi eğitim, yayım, emsal paylaşımı, araştırma, dış bir araca yükleme.
2. Asistan metni tarar ve bulgu listesi çıkarır: katman, konum (paragraf), önerilen etiket veya genelleştirme.
3. Maskeli veya anonim sürüm ile değişiklik özeti üretilir; eşleştirme tablosu yalnız kullanıcıya ve yalnız bu oturumda gösterilir.
4. Kalan risk notu: dolaylı tanımlayıcılar ve özel nitelikli veri kalıntıları.
5. İnsan onayı: yazı işleri müdürü veya hâkim kontrol eder; onay satırı doldurulmadan sürüm "yayıma hazır" sayılmaz.

```
ANONİMLEŞTİRME ÇIKTISI — TASLAK (insan onayı şart)
Amaç / kanal: [..]            Sürüm türü: [maskeli / anonim]
Bulgular: [N] doğrudan · [N] dolaylı · [N] özel nitelikli · çocuk: [var/yok]
Kalan risk: [..]
Korunanlar: künye [bırakıldı / çıkarıldı — kurum politikası], hüküm sonucu ve gerekçe bozulmadı
Onay: [ad soyad değil, unvan] — [tarih]
```

## 5. Sınırlar

- Asistan UYAP'a veya kaynak belgeye yazmaz; yalnız ayrı bir sürüm üretir.
- Otomatik tarama her tanımlayıcıyı bulamayabilir; insan kontrolü atlanmaz.
- Maskelenmemiş belge kurum kuralları izin vermedikçe dış bir sisteme yüklenmez (`yargida-yapay-zeka-rehberi.md`).

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): AY m. 20, 141; KVKK m. 3, 4, 6, 28; 5395 s.K. m. 4; CMK m. 58, 80, 157, 182, 185, 232, 236; HMK m. 28, 297; TMK m. 184; 6284 s.K. m. 8; TCK m. 102, 103 (CMK m. 236/5-6'nın yollama yaptığı suçların başlıkları). AB: Regulation (EU) 2024/1689 recital 61, `eu_get_document_text` ile okundu.*
