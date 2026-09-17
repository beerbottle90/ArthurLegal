# Arthur Mask — Kullanım Rehberi

**Arthur Mask 1.0.0** · ArthurLegal Law Firm Assistant v1.8.0 ile birlikte · 13.09.2026
English → [ARTHUR-MASK-EN.md](ARTHUR-MASK-EN.md)

Arthur Mask, müvekkil belgelerini Claude'a vermeden önce **kendi bilgisayarınızda**
maskeleyen bir Windows programıdır. Adlar, şirketler, TCKN, VKN, IBAN, adres,
telefon, e-posta, doğum tarihi, dosya numarası, pasaport ve plaka gibi bilgiler
`{{KİŞİ-01}}`, `{{ŞİRKET-02}}`, `{{TCKN-01}}` gibi etiketlerle değiştirilir. Gerçek
değerler bilgisayarınızda, her dosya için ayrı şifreli bir kasada kalır. Claude
yalnız maskeli metni görür; cevabı yine bilgisayarınızda gerçek adlarla Word veya
UDF olarak açılır.

> **Önemli.** Arthur Mask yalnız **Claude Desktop (Windows)** ile çalışır. claude.ai
> web sürümünde ve mobil uygulamalarda çalışmaz. ArthurLegal Project'inizi Claude
> Desktop'tan açmanız yeterlidir; Project'ler web ile masaüstü arasında ortaktır.

> **[⬇ Kurulum dosyasını indirin (Windows, yaklaşık 1 GB)](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** · tıklayınca iner, GitHub hesabı gerekmez

---

## Ne zaman kullanmalı

- **Kullanın:** müvekkil, karşı taraf, tanık veya çalışan adı; TCKN, adres, telefon, IBAN, dosya numarası geçen dilekçe, sözleşme, bilirkişi raporu, yazışma ve tutanaklar.
- **Gerekmez:** kişi veya şirket adı geçmeyen hukuki araştırma soruları ("TBK m.344 kira artışı sınırı nedir?"), mevzuat ve içtihat taramaları, boş şablonlar.
- **Kararsız kaldığınızda:** belgede bir kişiyi veya şirketi tanıtan tek bir bilgi bile varsa Arthur Mask'ten geçirin.
  Belgeyi ya da içeriğini Claude sohbetine doğrudan yapıştırmayın veya eklemeyin; o yol Arthur Mask'ten geçmez.

ArthurLegal Project'inizi henüz kurmadıysanız önce [KURULUM.md](KURULUM.md) dosyasındaki adımları tamamlayın.

---

## 1. Neye ihtiyacınız var

| | |
|---|---|
| Bilgisayar | Windows 10 veya 11, 64 bit |
| Claude | Claude Desktop, Windows sürümü: [claude.ai/download](https://claude.ai/download) |
| Disk | Yaklaşık 4 GB boş alan |
| Bellek | 8 GB RAM önerilir |
| İnternet | Maskeleme için gerekmez; program tamamen çevrimdışı çalışır |

Belge verileriniz bilgisayarınızdan çıkmaz. Dışarı çıkan tek şey, Claude Desktop'un
aldığı maskeli metindir. Bu metin Claude'a, yani Anthropic'e gider; Claude hesabınızın
veri kullanımı ve saklama ayarları bu metin için de geçerlidir. Program ayrıca günde bir kez
ArthurLegal sürüm sayfasından yalnız en son sürüm numarasını okur (belge verisi göndermez).

---

## 2. Kurulum (yaklaşık 10 dakika)

1. **İndirin.** **[⬇ Arthur Mask kurulum dosyasını indirmek için buraya tıklayın](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** (Windows, yaklaşık 1 GB).
   GitHub hesabı ya da GitHub bilgisi gerekmez: bağlantıya tıklayınca `ArthurMask-Kurulum.exe` dosyası
   doğrudan bilgisayarınızın **İndirilenler** klasörüne iner. İnternet hızınıza göre birkaç dakika sürebilir.
   Tarayıcı "Sakla / Keep" diye sorarsa **Sakla**'yı seçin. İndirme bitince İndirilenler klasöründe dosyaya çift tıklayın.
2. **Çalıştırın.** Kurulum dosyası kod imzalı olmadığından Windows
   **"Windows bilgisayarınızı korudu"** diyebilir: **Ek bilgi** → **Yine de çalıştır**.
   Antivirüs programınız dosyayı bir süre tarayabilir; bekleyin.
3. **Kurun.** Yönetici yetkisi gerekmez. Program `%LOCALAPPDATA%\Programs\Arthur Mask`
   klasörüne kurulur, Başlat menüsüne ve masaüstüne **Arthur Mask** kısayolu ekler ve
   Claude Desktop'a `arthur-mask` bağlantısını kendiliğinden kaydeder (önceki ayarların
   yedeği tutulur).
4. **Claude Desktop'u yeniden başlatın.** Claude Desktop'tan **tamamen** çıkın (sağ alttaki
   sistem tepsisi simgesinden de **Çıkış**), sonra yeniden açın.
5. **Kontrol edin.** Claude Desktop → **Ayarlar → Geliştirici** bölümünde `arthur-mask`
   çalışıyor görünmeli. Bir sohbette araçlar menüsünde Arthur Mask araçları görünmeli.

---

## 3. İlk iş: kurtarma anahtarı

Arthur Mask'i açın → üst menüde **Kurtarma anahtarı**.

Kasalarınız Windows kullanıcı hesabınızla korunur. Bilgisayarınız değişirse veya
Windows yeniden kurulursa kasaları **yalnız bu anahtar** açar. Anahtar bir kez
gösterilir: yazdırın veya güvenli bir yerde saklayın, sonra **Sakladım** deyin.
Anahtarı **asla Claude'a yazmayın**.

---

## 4. Günlük kullanım, 6 adımda

**1. Açın.** Masaüstündeki **Arthur Mask** kısayolu tarayıcınızda
`http://127.0.0.1:47831` adresini açar. Sağ üstte **Claude Desktop'a bağlı** ve
**Tam koruma** yazmalıdır.

**2. Belgeyi bırakın.** Word (.docx), UYAP (.udf), PDF, taranmış PDF veya fotoğraf,
.txt ya da .md dosyasını pencereye sürükleyin. İlk belge, belgenin adıyla yeni bir
**dosya** açar. Başka bir müvekkil veya iş için **+ Yeni dosya** kullanın. Aynı
dosyadaki belgelerde aynı kişi hep aynı etiketi alır.

**3. İnceleyin.** Durum **Onayınızı bekliyor** veya **Kırmızı hat** ise **İncele**'yi açın:

- Programın emin olmadığı her bilgi için **Maskele** veya **Açık bırak** seçin.
- Maskeli kopyaya göz atın.
- **Kırmızı hat** uyarısı varsa (savunma stratejisi, uzlaşma sınırı, sağlık veya
  inanç gibi özel nitelikli veri, içeriden öğrenilen bilgi), bu içeriğin neden
  gönderilebileceğini bir cümleyle yazın. Gerekçe yazılmadan gönderim açılmaz.
- **Onayla — Claude'a hazırla**.

**4. Claude'a verin.** Arthur Mask size bir komut gösterir, örneğin:

```
Arthur Mask'teki belge-1'i incele
```

Kopyalayıp **Claude Desktop'taki ArthurLegal Project sohbetine** yapıştırın ve ne
istediğinizi ekleyin ("kira bedeli maddesini değerlendir", "cevap dilekçesi taslağı
hazırla" gibi). **Orijinal belgeyi ayrıca sohbete eklemeyin.**

**5. Cevabı alın.** Claude'un cevabı Arthur Mask'te **Cevaplar** altında gerçek
adlarla görünür:

- **Word'de aç** veya **UYAP editöründe aç**
- Revizyonlarda **Word'de aç (izli değişiklikler)**: değişiklikler orijinal belgenize
  Word izli değişikliği olarak işlenir, sayfa düzeni korunur.
- **Gerçek adlarla / Claude'daki hâli** sekmeleriyle iki hâli karşılaştırabilirsiniz.

**6. Denetleyin.** **Claude'a giden** paneli Claude'un tam olarak ne aldığını gösterir.
**Sızıntı denetimi yap** düğmesi gönderilen ve alınan her şeyi kasaya karşı yeniden
tarar: **✓ Temiz** ya da bulgu listesi.

---

## 5. Sizi koruyan dört kilit

1. **İnceleme ekranı.** Emin olunamayan tespitler sizin onayınıza sunulur.
2. **Kırmızı hat.** Maskeli olsa bile yapay zekâya gitmemesi gereken içerik,
   gerekçe yazmadan gönderilemez.
3. **Çıkış kapısı.** Claude'a giden her yanıt, gönderilmeden hemen önce kasadaki bütün
   gerçek değerlere karşı yeniden taranır; geçen bir değer etiketiyle değiştirilir. Kapı, bu dosyanın
   herhangi bir belgesinde **en az bir kez tespit edilmiş** değerleri tanır; hiç tespit edilmemiş bir
   bilgiyi yakalayamaz. Onun güvencesi inceleme ekranı ve sizin okumanızdır.
4. **Kayıt ve denetim.** Claude'a giden her şey maskeli hâliyle kaydedilir ve
   istediğiniz an sızıntı denetimi yapabilirsiniz.

---

## 6. Verileriniz nerede

`Belgeler\Arthur Mask\<dosya adı>` klasöründe. Maskeli kopyalar 30 gün sonra
kendiliğinden silinir; gerçek adlarla açılmış cevaplar ve kasa kalır. Büronuzun
saklama ve imha kuralları bu klasöre de uygulanır.

---

## 7. Güncelleme ve kaldırma

**Güncelleme.** Yeni sürüm yayımlandığında Arthur Mask ekranında bildirim çıkar.
[Aynı indirme bağlantısından](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe) yeni dosyayı indirip eskisinin üzerine kurun;
dosyalarınız, kasalarınız ve kurtarma anahtarınız korunur.

**Dosyayı doğrulamak isterseniz.** [Arthur Mask sürüm sayfasında](https://github.com/beerbottle90/ArthurLegal/releases/tag/arthur-mask) kurulum dosyasının
SHA-256 özeti yayımlanır. PowerShell'de `Get-FileHash .\ArthurMask-Kurulum.exe` komutunun
çıktısı bu özetle aynı olmalıdır.

**Kaldırma.** Windows **Ayarlar → Uygulamalar → Arthur Mask → Kaldır**. Program ve
Claude Desktop bağlantısı kaldırılır. `Belgeler\Arthur Mask` klasörü ve kurtarma
anahtarı dosyası silinmez; isterseniz elle silin.

---

## 8. Sorun giderme

| Ne görüyorsunuz | Ne yapmalısınız |
|---|---|
| **Bağlantı yok — Claude Desktop'u açın** | Claude Desktop açık değil ya da kurulumdan sonra yeniden başlatılmadı. Tamamen çıkıp yeniden açın. |
| Claude'da Arthur Mask araçları yok | Claude Desktop'tan sistem tepsisi dâhil tamamen çıkıp yeniden açın; **Ayarlar → Geliştirici**'de `arthur-mask` kaydına bakın. |
| **Koruma hazırlanıyor…** | Açılışta 15 ile 30 saniye normaldir. |
| **Temel koruma** | Yapay zekâ tespiti veya OCR yüklenemedi; kurallar yine çalışır. Programı yeniden kurun. |
| Claude "belge hazır değil" diyor | Arthur Mask'te incelemeyi bitirip **Onayla** deyin. |
| Cevabın altında bilinmeyen etiket uyarısı | Claude bir etiketi değiştirmiş; o cümleyi kontrol edin. |
| **Sızıntı denetimi** bulgu gösteriyor | "Çıkış kapısından önce" satırları, değerin depodaki maskeli metinde durduğunu gösterir; Claude'a giderken etiketlenir. "Claude'un yazdığı metin" satırı, Claude'un o değeri bir yerden açık gördüğünü gösterir: sohbete yazılan ya da eklenen bir şey olabilir. İlgili sohbeti gözden geçirin, belgeyi yeni bir dosyada yeniden maskeleyin. |
| claude.ai web veya telefonda çalışmıyor | Desteklenmez; Claude Desktop'u kullanın. |

---

## 9. Sık sorulan sorular

**Maskeli belge artık anonim mi?**
Hayır. Yapılan işlem hukuken **takma adlandırmadır**, anonim hâle getirme değildir.
Gerçek değerler kasanızda durur ve etiketler onlara geri çevrilebilir. Metnin geri
kalanı da bağlamıyla birlikte kişiyi belirlenebilir kılabilir.

**Arthur Mask her kişisel veriyi yakalar mı?**
Garanti edilemez; tespit olasılığa dayalıdır. Bu yüzden inceleme ekranı, çıkış kapısı
ve sızıntı denetimi vardır. Göndermeden önce maskeli kopyaya bakın.

**Hangi bilgiler bilerek maskelenmez?**
Tarihler ve tutarlar (süre ve hesap için gerekir). Yargıtay, Danıştay gibi yüksek
mahkeme karar künyeleri de korunur. Bir tutarın kendisi gizliyse (ör. uzlaşma sınırı)
kırmızı hattı kullanın veya o kısmı çıkarın.

**Neler maskelenemez?**
Word içindeki resimler ve gömülü nesneler; taranmış belgelerdeki el yazısı, imza, kaşe
ve QR kod.

**Arthur Mask kullanınca sorumluluğum kalkar mı?**
Hayır. KVKK yükümlülükleriniz, Avukatlık Kanunu'ndaki sır saklama yükümlülüğünüz,
ticari sır ve gizlilik sözleşmelerinden doğan yükümlülükler aynen devam eder. Arthur
Mask bu yükümlülükleri yerine getirmenize yardım eden bir araçtır; maskeli metnin
Claude'a gönderilmesinin değerlendirmesi size aittir.

**İngilizce veya Azerbaycanca belge olur mu?**
Olur. İki sütunlu iki dilli Word sözleşmeleri tablo yapısını korur; Claude revizyonu
iki dil sütununa birlikte işler.

**Neden claude.ai web sürümünde çalışmıyor?**
claude.ai'deki bağlantılar Anthropic'in bulutundan çağrılır ve bulut, bilgisayarınızda
çalışan bir programa ulaşamaz. Kapı yalnız Claude Desktop'un yerel bağlantısı üzerinden
çalışır.

**Kaynak kodu nerede?**
Arthur Mask yalnız kurulum dosyası olarak dağıtılır. İçerdiği üçüncü taraf açık kaynak
bileşenlerin bildirimleri kurulum klasöründedir; bkz. [ATTRIBUTION.md](ATTRIBUTION.md).
