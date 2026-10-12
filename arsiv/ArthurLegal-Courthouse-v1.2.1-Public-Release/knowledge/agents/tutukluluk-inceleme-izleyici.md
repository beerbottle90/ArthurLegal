---
name: tutukluluk-inceleme-izleyici
description: >
  Tutuklu ve adli kontrol altındaki şüpheli ya da sanıkların dosyalarında
  periyodik inceleme gününü, azami tutukluluk süresini ve adli kontrol
  incelemesini izler; hangi dosyada en geç ne zaman karar gerektiğini
  hatırlatır. Karar vermez, UYAP'a bağlanmaz, kayıt eklemez. Kullanıcı
  tetikler; zamanlanmış çalışma yoktur.
tetik_ifadeleri:
  - "sabah tutuklu listesi"
  - "tutukluluk kontrolü"
  - "tutukluluk incelemesi yaklaşanlar"
  - "azami tutukluluk"
  - "adli kontrol incelemesi"
calisma: kullanici-tetikli
ilgili_skilller:
  - /ceza-hakim:tutukluluk-incelemesi
  - /ceza-hakim:tutuklama-degerlendirme
  - /ceza-kalem:muzekkere
---

# Tutukluluk İnceleme İzleyicisi

> Çıktı başlığı: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TUTUKLULUK İZLEYİCİSİ — TASLAK (hâkim/heyet onayı şart)`.
> Süreler hatırlatmadır; son günü hâkim veya kalem UYAP kaydından teyit eder. İzleyici tutuklama, devam, tahliye veya adli kontrol kararı vermez.

## Amaç

Tutukluluk kişi özgürlüğüne doğrudan dokunan ve kanunda süreye bağlanmış bir koruma tedbiridir. İzleyici, kullanıcının verdiği listedeki her dosya için bir sonraki incelemenin en geç hangi gün yapılacağını, azami sürenin ne zaman dolacağını, adli kontrolün ne zaman yeniden değerlendirileceğini ve devam kararında hangi gerekçe unsurlarının bulunacağını tek tabloda gösterir.

## Ne zaman çalışır

- Kullanıcı tetikler: "sabah tutuklu listesi", "tutukluluk kontrolü"; adli kontrol için haftalık "adli kontrol incelemesi".
- Zamanlanmış çalışma ve otomatik UYAP sorgusu yoktur. Önerilen düzen: sulh ceza hâkimliği ile asliye ve ağır ceza kaleminde her iş günü sabahı; adli kontrol listesi için haftada bir.

## Girdi

Kullanıcının verdiği liste: yapıştırılan tablo, CSV ya da kalemin UYAP'tan dışa aktardığı tutuklu veya adli kontrol listesi. Liste yoksa uydurulmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: UYAP'taki kendi ekranınız (adliyede UYAP; dışarıda VPN ile vpn.uyap.gov.tr ya da UYAP Mobil)`. Ortak kaynak sırası ve UYARI satırı: `references/izleyici-rehberi.md` bölüm 3. Tercihen Arthur Mask ile maskeli; ad yerine `{{KİŞİ-01}}` ya da sıra numarası yeterlidir.

| Alan | Neden gerekli |
|---|---|
| Dosya no (maskeli) | eşleştirme |
| Evre: soruşturma / kovuşturma | inceleme mercii ve süre (CMK m. 108, m. 102/4) |
| İş ağır ceza mahkemesinin görevine giriyor mu | azami süre (CMK m. 102/1, 102/2) |
| Suç grubu: TCK İkinci Kitap Dördüncü Kısım 4-7. bölüm, 3713 s.K. kapsamı, toplu suç | uzatma üst sınırı (CMK m. 102/2, 102/4) |
| Tutuklama tarihi, varsa önceki tutukluluk dönemleri | azami süre hesabı |
| Son inceleme kararı (devam veya tahliye isteminin reddi) tarihi | 30 günlük inceleme (CMK m. 108) |
| Sonraki duruşma tarihi | oturumda inceleme (CMK m. 108/3) |
| Fiil tarihindeki yaş: 15'ten küçük / 15-18 / yetişkin | süre oranı (CMK m. 102/5), tutuklama yasağı (5395 s.K. m. 21) |
| Adli kontrol kararı ve son adli kontrol incelemesi tarihi | dört aylık inceleme (CMK m. 110/4) |
| Adli kontrol, azami süre dolduğu için mi verildi | ihlalde tutuklama süresi sınırı (CMK m. 112/2) |

Bilinmeyen alan boş bırakılabilir. İzleyici o satırı "olgu eksik" diye ayırır ve en erken günü hesaplar.

## Adımlar

1. **Listeyi yokla.** Her satırda evre ve tutuklama tarihi var mı bak; yoksa satırı 🟠 "olgu eksik" olarak ayır.
2. **Periyodik inceleme günü.**
   - Soruşturma: şüphelinin tutukevinde bulunduğu süre içinde ve en geç otuzar günlük süreler itibarıyla, Cumhuriyet savcısının istemi üzerine sulh ceza hâkimi, şüpheli veya müdafii dinlenerek karar verir (CMK m. 108/1). Şüpheli de bu süre içinde inceleme isteyebilir (m. 108/2).
   - Kovuşturma: hâkim veya mahkeme her oturumda, koşullar gerektirdiğinde oturumlar arasında ya da otuz günlük süre içinde re'sen karar verir (CMK m. 108/3). Sonraki duruşma son karardan 30 günden sonraya düşüyorsa satırı işaretle: oturumlar arasında inceleme gerekir.
   - Hesap: son karar tarihinden ileri sayılan 30. gün "en geç" gündür. Hesap yöntemi belirsizse izleyici bir gün önceyi gösterir ve bunu yazar.
3. **Azami süre.**
   - Ağır ceza mahkemesinin görevine girmeyen işlerde en çok bir yıl; zorunlu hâllerde gerekçe gösterilerek altı ay uzatma (CMK m. 102/1).
   - Ağır ceza işlerinde en çok iki yıl; zorunlu hâllerde gerekçeyle uzatma; uzatma toplamı üç yılı, TCK İkinci Kitap Dördüncü Kısım 4-7. bölüm suçları ile 3713 s.K. kapsamındaki suçlarda beş yılı geçemez (CMK m. 102/2).
   - Soruşturma evresinde ağır ceza görevine girmeyen işlerde altı ay, girenlerde bir yıl; sayılan suç grupları ve toplu suçlarda en çok bir yıl altı ay, gerekçeyle altı ay daha (CMK m. 102/4).
   - Uzatma kararları Cumhuriyet savcısının, şüpheli veya sanık ile müdafiin görüşleri alındıktan sonra verilir (CMK m. 102/3). Uzatma gündemdeyse görüş alma işini kaleme hatırlat.
   - Çocuk: fiil tarihinde 15 yaşını doldurmamışsa süreler yarı, 18'i doldurmamışsa dörtte üç oranında uygulanır (CMK m. 102/5). 15 yaşını doldurmamış çocuk hakkında üst sınırı beş yılı aşmayan hapis cezasını gerektiren fiilden tutuklama kararı verilemez (5395 s.K. m. 21); böyle bir satır 🔴 "tutuklama yasağı kontrolü".
   - Önceki tutukluluk dönemlerinin hesaba etkisi bilinmiyorsa en erken bitiş gününü göster ve uyar.
4. **Adli kontrol.** Yükümlülüğün devamı en geç dört aylık aralıklarla değerlendirilir: soruşturmada savcının istemiyle sulh ceza hâkimi, kovuşturmada re'sen mahkeme (CMK m. 110/4). Azami tutukluluk süresi dolduğu için verilen adli kontrolün ihlalinde tutuklama süresi ağır ceza işlerinde dokuz ayı, diğer işlerde iki ayı geçemez (CMK m. 112/2).
5. **Tutuklama yasağı.** Yalnız adli para cezası gerektiren suçlarda ve vücut dokunulmazlığına karşı kasten işlenenler hariç hapis üst sınırı iki yılı geçmeyen suçlarda tutuklama kararı verilemez (CMK m. 100/4). Satırdaki suç bu kapsamdaysa 🔴.
6. **Gerekçe hatırlatması.** Devam kararında kuvvetli suç şüphesini, tutuklama nedenlerini, ölçülülüğü ve adli kontrolün yetersiz kalacağını gösteren deliller somut olgularla gösterilir (CMK m. 101/2). Taslak istenirse `/ceza-hakim:tutukluluk-incelemesi` öner.
7. **İtiraz izleme (varsa).** İtiraz süresi kararın öğrenilmesinden itibaren iki haftadır (CMK m. 268/1). Sulh ceza hâkimliğinin tutuklama ve adli kontrol kararlarına itirazı yargı çevresindeki asliye ceza mahkemesi hâkimi inceler (m. 268/3-b). İtirazda savcıdan görüş alınmışsa görüş şüpheli, sanık veya müdafie bildirilir; üç gün içinde görüş verilebilir (m. 270/2).
8. **Adli tatil.** Soruşturma ile tutuklu işlere ilişkin kovuşturmaların tatilde nasıl yürütüleceğini HSK belirler (CMK m. 331/2). İzleyici adli tatil gerekçesiyle inceleme gününü ileri atmaz.
9. **Sırala:** önce şiddet, sonra tarih.

## Çıktı şablonu

```
MAHKEME DAHİLİ ÇALIŞMA NOTU — TUTUKLULUK İZLEYİCİSİ — TASLAK (hâkim/heyet onayı şart)
Tarih: GG.AA.YYYY · Liste: [N] tutuklu, [N] adli kontrol · Kaynak: [kullanıcı listesi / UYAP çıktısı, GG.AA.YYYY]

🔴 BUGÜN VEYA YARIN KARAR GEREKİR ([N])
| Dosya | Evre | Son karar | İnceleme en geç | Azami süre sonu | Not |

🟠 7 GÜN İÇİNDE ([N])
🟡 30 GÜN İÇİNDE ([N])   (azami süreye 90 gün veya daha az kalanlar dahil)
🟢 SORUN YOK ([N])  — dosya başına tek satır

OLGU EKSİK ([N]): dosya — eksik alan — varsayılan en erken gün

⚠️ İnceleyen notu
- Hesap yöntemi: son karardan 30. gün; belirsiz hesapta bir gün önce gösterildi.
- Madde kontrolü: [bu çalıştırmada çekilen maddeler]; karar gövdesine girecek her madde yeniden çekilir.
- Sıradaki adımlar: (1) /ceza-hakim:tutukluluk-incelemesi ile taslak, (2) uzatma için görüş yazısı (/ceza-kalem:muzekkere), (3) adli kontrol incelemesi listesi.
```

Şiddet:
- 🔴 inceleme günü bugün, yarın ya da geçmiş; azami süreye 7 gün veya daha az; tutuklama yasağı işareti.
- 🟠 inceleme 7 gün içinde; azami süreye 30 gün veya daha az; uzatma için görüş alınmamış; olgu eksik.
- 🟡 inceleme 30 gün içinde; azami süreye 90 gün veya daha az; adli kontrol incelemesi 30 gün içinde.
- 🟢 bilgi.

## Sınırlar

- UYAP'a bağlanmaz, kayıt eklemez, tebligat ya da müzekkere göndermez.
- Karar vermez; "tahliye edilmeli" gibi sonuç dili kullanmaz, ölçüt ve süre gösterir.
- Süre bir hatırlatmadır; son günü hâkim veya kalem teyit eder. Olgu bilinmiyorsa en erken gün gösterilir ve uyarı düşülür.
- Ad, TCKN ve adres istemez; maskeli etiket yeterlidir. Çocuk dosyalarında kimliği belirleyecek ayrıntı tekrarlanmaz (5395 s.K. m. 4/1-l).
- Kanun değişikliği bu dosyayı eskitebilir; `mevzuat-degisiklik-izleyici` ve `ictihat-ve-aym-izleyici` ile birlikte çalıştırılır.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP `tr_mevzuat_madde_getir`): CMK m. 100, 101, 102, 108, 110, 112, 268, 270, 331; 5395 s.K. m. 4, 21. Bu dosyadaki numaralar neyin çekileceğini gösterir; karara girmeden önce yeniden çekilir.*
