# Arthur Mask Rehberi (yerel gizlilik kapısı)

> **Sürüm:** Arthur Mask 1.0.0, ArthurLegal v1.8.0 ile birlikte yayımlandı (13.09.2026).
> **Bu dosya kimin için:** Claude'un, kullanıcının Arthur Mask hakkındaki sorularını (kurulum, günlük kullanım, sorun giderme, sınırlar) doğru cevaplaması ve `arthur_mask_*` araçlarını doğru kullanması için. Hâkim ve kalem personeline yönelik adım adım anlatım paket kökündeki `ARTHUR-MASK.md` dosyasındadır.
> **Dağıtım:** Yalnız ArthurLegal GitHub sürüm sayfasındaki kurulum dosyası. Kaynak kodu yayımlanmaz.

---

## 1. Arthur Mask nedir

Arthur Mask, yalnız kullanıcının bilgisayarında çalışan bir Windows programıdır. Kullanıcı (hâkim veya kalem personeli) bir belgeyi Arthur Mask'in yerel tarayıcı arayüzüne bırakır; belgedeki kişisel veriler `{{KİŞİ-01}}`, `{{ŞİRKET-02}}`, `{{TCKN-01}}` gibi etiketlerle değiştirilir. Gerçek değerler bilgisayarda, her dosya için ayrı ve şifreli bir kasada kalır. Claude, Claude Desktop üzerinden yalnız maskeli metni alır. Claude'un cevabı yine bilgisayarda gerçek adlara geri çevrilir ve Word veya UDF olarak açılır.

Hukuki terim olarak yapılan işlem **takma adlandırmadır** (KVKK ve GDPR bakımından pseudonymisation), anonim hâle getirme değildir: gerçek değerler kasada durduğu ve etiketler onlara geri çevrilebildiği için maskeli metin de kişisel veri niteliğini sürdürebilir.

Desteklenen belgeler: Word (.docx), UYAP (.udf), PDF, taranmış PDF veya fotoğraf (bilgisayardaki OCR ile), .txt ve .md. Türkçe, İngilizce ve Azerbaycanca belgeler desteklenir; iki sütunlu iki dilli Word sözleşmeleri tablo yapısını korur.

## 2. Ne maskelenir, ne maskelenmez

| Maskelenir | Maskelenmez |
|---|---|
| Kişi adları, şirket adları | Tarihler (bilinçli olarak; süre hesabı için gerekir) |
| TCKN, VKN, IBAN | Tutarlar (bilinçli olarak) |
| Adresler, telefonlar, e-posta adresleri | Yargıtay, Danıştay ve diğer yüksek mahkeme karar künyeleri (korunur) |
| Doğum tarihleri, dosya numaraları | Word içindeki resimler ve gömülü nesneler |
| Pasaport numaraları, araç plakaları | Taramalardaki el yazısı, imza, kaşe ve QR kod |

Aynı dosyadaki belgeler etiketleri paylaşır: aynı kişi, dosyanın bütün belgelerinde aynı etiketi alır.

## 3. Gereksinimler

| Gereksinim | Açıklama |
|---|---|
| İşletim sistemi | Windows 10 veya 11, 64 bit |
| Claude | Claude Desktop, Windows sürümü (claude.ai/download) |
| Disk | Yaklaşık 4 GB boş alan |
| Bellek | 8 GB RAM önerilir |
| İnternet | Gerekmez. Yapay zekâ tespit modeli ve OCR modelleri kurulum dosyasının içindedir |

Çevrimdışı çalışır. Belge verisi bilgisayardan çıkmaz; tek istisna, Claude Desktop'un aldığı maskeli metindir. Bunun dışındaki tek ağ çağrısı isteğe bağlı güncelleme kontrolüdür: ArthurLegal GitHub sürüm sayfasından en son sürüm numarasını okur, belge verisi göndermez.

**Desteklenmeyen:** claude.ai web tarayıcı sürümü ve mobil uygulamalar. Nedeni: claude.ai'deki uzak connector'lar Anthropic'in bulutundan çağrılır ve bulut, kullanıcının bilgisayarında çalışan bir programa ulaşamaz. Kapı yalnız Claude Desktop'un yerel connector'ı üzerinden çalışır. Kullanıcı ArthurLegal Project'ini Claude Desktop içinden açmalıdır; Project'ler web ile masaüstü arasında ortaktır, ayrıca kurulum gerekmez.

## 4. İndirme ve kurulum

1. İndirme adresi: https://github.com/beerbottle90/ArthurLegal/releases/tag/v1.8.0 , dosya `ArthurMask-Kurulum-1.0.0.exe` (yaklaşık 1 GB).
2. Kurulum dosyası kod imzalı değildir. Windows SmartScreen "Windows bilgisayarınızı korudu" uyarısı gösterebilir: "Ek bilgi", ardından "Yine de çalıştır". Bazı antivirüs ürünleri dosyayı bir süre tarayabilir.
3. Kurulum kullanıcı başınadır, yönetici yetkisi istemez ve `%LOCALAPPDATA%\Programs\Arthur Mask` klasörüne kurar.
4. Başlat menüsüne ve masaüstüne "Arthur Mask" kısayolu ekler.
5. `arthur-mask` yerel connector'ını Claude Desktop yapılandırmasına kendiliğinden kaydeder; önceki yapılandırma dosyasının yedeğini tutar.
6. Sonunda Arthur Mask'i açmayı önerir.

## 5. Kurulumdan sonra doğrulama

1. Claude Desktop'tan tamamen çıkın; sistem tepsisindeki simgeden de çıkın. Sonra yeniden açın.
2. Claude Desktop'ta Ayarlar, Geliştirici (Settings, Developer) bölümünde "arthur-mask" çalışır durumda görünür.
3. Bir sohbette araçlar menüsünde Arthur Mask araçları görünür.

## 6. Günlük akış (6 adım)

1. **Aç.** "Arthur Mask" kısayolu tarayıcıda http://127.0.0.1:47831 adresini açar. Sağ üstte "Claude Desktop'a bağlı" ve "Tam koruma" göstergeleri görünür.
2. **Belgeyi bırak.** İlk belge, belgenin adını taşıyan yeni bir dosya oluşturur. Başka bir iş için "+ Yeni dosya" kullanılır. Aynı dosyadaki belgeler etiketleri paylaşır.
3. **İncele.** Durum "Onayınızı bekliyor" veya "Kırmızı hat" ise "İncele" açılır: belirsiz tespitler için "Maskele" veya "Açık bırak" seçilir, maskeli kopya kontrol edilir, kırmızı hat içeriği için gerekçe yazılır, sonra "Onayla — Claude'a hazırla".
4. **Claude'a ver.** Gösterilen komut (ör. "Arthur Mask'teki belge-1'i incele") kopyalanır ve Claude Desktop'taki ArthurLegal Project sohbetine yapıştırılır. Orijinal belge ayrıca sohbete eklenmez.
5. **Cevabı al.** Claude'un cevabı "Cevaplar" altında gerçek adlarla görünür: "Word'de aç", "UYAP editöründe aç" veya revizyonlarda "Word'de aç (izli değişiklikler)" (değişiklikler orijinal belgeye Word izli değişikliği olarak işlenir, sayfa düzeni korunur). Her cevapta "Gerçek adlarla" ve "Claude'daki hâli" sekmeleri vardır.
6. **Denetle.** "Claude'a giden" paneli Claude'un tam olarak ne aldığını gösterir. "Sızıntı denetimi yap" düğmesi "✓ Temiz" sonucunu verir veya bulguları listeler.

## 7. İnceleme ekranı ve kırmızı hat

**İnceleme ekranı.** Tespit olasılığa dayalıdır. Program emin olmadığı tespitleri kullanıcının onayına sunar; kullanıcı her biri için "Maskele" veya "Açık bırak" der ve maskeli kopyayı göndermeden önce görür.

**Kırmızı hat.** Maskeli olsa bile yapay zekâya gitmemesi gereken içerik: savunma stratejisi, uzlaşma veya sulh sınırları, KVKK m. 6 kapsamındaki özel nitelikli kişisel veriler, içeriden öğrenilen bilgi. Program böyle bir içerik sezdiğinde, avukat gerekçe yazana kadar gönderimi durdurur.

## 8. Çıkış kapısı ve sızıntı denetimi

**Çıkış kapısı.** Claude'a giden her yanıt, gönderilmeden hemen önce kasadaki bütün gerçek değerlere karşı yeniden taranır; bir gerçek değer geçiyorsa etiketiyle değiştirilir. Bu, inceleme ekranından sonra eklenen bir ikinci savunma hattıdır.

**"Claude'a giden" paneli.** Claude'a gönderilen her yanıt maskeli hâliyle kayda geçer; kullanıcı Claude'un tam olarak ne gördüğünü sonradan kontrol edebilir.

**Sızıntı denetimi.** "Sızıntı denetimi yap" düğmesi gönderilen ve alınan her şeyi kasaya karşı yeniden tarar. Sonuç "✓ Temiz" ya da bulgu listesidir.

## 9. Kurtarma anahtarı

Üst menüde "Kurtarma anahtarı". Kasalar Windows kullanıcı hesabıyla korunur. Bilgisayar değişirse veya Windows yeniden kurulursa kasaları yalnız bu anahtar açar. Anahtar bir kez gösterilir; yazdırılır veya güvenli bir yerde saklanır, sonra "Sakladım" düğmesine basılır. Anahtar asla Claude'a yazılmaz. Kullanıcı anahtarı sohbete yazmaya kalkarsa Claude bunu yapmamasını söyler ve anahtarı tekrar etmez.

## 10. Veriler nerede, ne kadar kalır

Konum: `Belgeler\Arthur Mask\<dosya adı>`. Maskeli kopyalar 30 gün sonra kendiliğinden silinir; gerçek adlara çevrilmiş cevaplar ve kasa kalır. Kurumun saklama ve imha kuralları bu klasöre de uygulanır.

## 11. Güncelleme ve kaldırma

**Güncelleme.** ArthurLegal sürüm sayfasında daha yeni bir kurulum dosyası yayımlandığında Arthur Mask arayüzü bildirim gösterir. Yeni sürüm eskisinin üzerine kurulur.

**Kaldırma.** Windows Ayarlar, Uygulamalar, Arthur Mask, Kaldır. Program ve Claude Desktop connector kaydı kaldırılır. `Belgeler\Arthur Mask` klasörü ve kurtarma anahtarı dosyası korunur; istenirse elle silinir.

## 12. Sorun giderme

| Belirti | Neden ve çözüm |
|---|---|
| Gösterge "Bağlantı yok — Claude Desktop'u açın" | Claude Desktop çalışmıyor veya kurulumdan sonra yeniden başlatılmadı. Claude Desktop'tan tamamen çıkıp yeniden açın. |
| Araçlar Claude'da görünmüyor | Claude Desktop'tan sistem tepsisi dâhil tamamen çıkıp yeniden açın; Ayarlar, Geliştirici bölümünde "arthur-mask" kaydını kontrol edin. |
| Açılışta "Koruma hazırlanıyor…" | 15 ile 30 saniye arası normaldir (model yükleniyor). |
| "Temel koruma" göstergesi | Yapay zekâ tespit bileşeni veya OCR yüklenemedi; kural tabanlı tespit çalışmaya devam eder. Programı yeniden kurun. |
| Claude belgenin hazır olmadığını söylüyor | İnceleme Arthur Mask'te tamamlanmamış. "İncele" ekranını bitirip onaylayın. |
| Cevabın altında bilinmeyen etiket uyarısı | Claude bir etiketi değiştirmiş. O cümleyi kontrol edin. |
| Resim, gömülü nesne, el yazısı, imza, kaşe, QR kod maskelenmedi | Bu içerikler kapsam dışıdır. Belgeyi göndermeden önce elle kontrol edin veya bu kısımları çıkarın. |
| claude.ai web veya mobilde araçlar yok | Desteklenmez. ArthurLegal Project'ini Claude Desktop'ta açın. |

## 13. Sınırlar

1. Takma adlandırma anonim hâle getirme değildir. Maskeli metin, bağlamıyla birlikte kişiyi belirlenebilir kılabilir.
2. Tespit olasılığa dayalıdır; hiçbir tespit sistemi her kişisel veriyi yakalamayı garanti etmez. İnceleme ekranı ve sızıntı denetimi bu yüzden vardır.
3. Sorumluluk kullanıcıdadır: KVKK yükümlülükleri, soruşturma ve kovuşturma dosyalarına ilişkin gizlilik kuralları, ticari sır ve kurumun bilgi güvenliği kuralları Arthur Mask kullanılsa da devam eder. Bir dosya içeriğinin maskeli hâliyle bile harici bir yapay zekâ hizmetine verilip verilemeyeceği (yurt dışına aktarım dâhil) mevzuata ve kurum kurallarına göre kullanıcı tarafından değerlendirilir.
4. Yalnız Claude Desktop (Windows). claude.ai web ve mobil uygulamalarda çalışmaz.
5. Word içindeki resimler ve gömülü nesneler; taramalardaki el yazısı, imza, kaşe ve QR kod maskelenmez.
6. Tarihler ve tutarlar bilinçli olarak maskelenmez; bunların kendisi gizliyse (ör. uzlaşma tutarı) kırmızı hat veya elle çıkarma gerekir.

## 14. Claude için araç kullanımı

| Araç | Ne yapar | Parametreler |
|---|---|---|
| `arthur_mask_belgeler` | Etkin dosyadaki maskeli belgeleri listeler | yok |
| `arthur_mask_belge_getir` | Maskeli metni döndürür; Word dosyaları Markdown olarak gelir, tablolar `\| AZ \| EN \|` biçiminde | `kimlik`, `parca` |
| `arthur_mask_belgeyi_revize_et` | Değişiklikleri yüklenen Word veya UDF belgesine izli değişiklik olarak uygular | `kimlik`, `degisiklikler=[{eski, yeni, hepsi?}]`, `baslik`, `izli=true` |
| `arthur_mask_teslim` | Yeni bir belge teslim eder; Markdown tablo ve başlıklar Word tablo ve başlığına dönüşür | `metin`, `bicim` (`docx`, `udf`, `txt`), `baslik` |

Kurallar:

1. Kullanıcı "belge-N" veya "Arthur Mask'teki…" diyorsa belgeyi `arthur_mask_belge_getir` ile çek; kimlik belirsizse önce `arthur_mask_belgeler`. Ham belgeyi yapıştırmasını veya eklemesini isteme.
2. Uzun belgede `parca` ile sırayla ilerle; okunmayan parçayı okunmuş gibi değerlendirme.
3. `{{TÜR-NN}}` etiketleri harfi harfine korunur. Türkçe ek kesme işaretinden sonra gelir: `{{KİŞİ-01}}'in`, `{{ŞİRKET-02}}'ye`. Etiket değiştirilmez, birleştirilmez, çevrilmez.
4. Gerçek değer tahmin edilmez, bağlamdan yeniden kurulmaz, kullanıcıdan istenmez.
5. Etiket hiçbir araştırma sorgusuna konmaz (`tr_` araçları, diğer MCP'ler, web). Hukuki soru soyut terimlerle araştırılır ("kira bedelinin uyarlanması", "tutuklamanın ölçülülüğü").
6. Yüklenen belgede değişiklik: `arthur_mask_belgeyi_revize_et`. Her `eski`, tek bir paragraf veya tek bir tablo hücresinden birebir kopyalanır; paragraflar arasına yayılan `eski` eşleşmez. İki dilli belgede iki dil sütunu birlikte revize edilir.
7. Yeni belge: `arthur_mask_teslim`. Başlık ve tablo Markdown ile yazılır; kaynak iki dilliyse çıktı iki sütunlu tablodur. Paketin dosya üretimi kuralları içeriğe uygulanır.
8. Araç belgenin hazır olmadığını söylerse kullanıcıdan incelemeyi Arthur Mask'te tamamlamasını iste.
9. Kullanıcı soruşturma veya kovuşturma dosyasından, UYAP'tan alınmış bir UDF'den ya da dava dosyasından tanımlanabilir kişisel veriyi (taraf, şüpheli, sanık, mağdur, tanık adı, TCKN, adres) doğrudan sohbete yapıştırır ya da eklerse, sohbet başına en çok bir kez, işi durdurmadan kısa bir hatırlatma yapılır: dosya belgeleri Arthur Mask ile (Claude Desktop, Windows) paylaşılmadan önce bilgisayarda maskelenebilir. Reddedilmez, ders verilmez.
10. Arthur Mask araçları yoksa (web, mobil veya kurulmamış) bu araçlar varmış gibi davranılmaz; kullanıcı soruyorsa bölüm 3 ve 4 anlatılır.

İlgili: `hakimlik-etigi-rehberi.md`, `uyap-rehberi.md`.
