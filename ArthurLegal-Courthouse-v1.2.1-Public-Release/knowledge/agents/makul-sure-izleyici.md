---
name: makul-sure-izleyici
description: >
  Uzun süredir derdest olan ve hareketsiz kalan dosyaları bulur; kanunda
  süreye bağlanmış aşamaların (duruşma arası, tekemmülden karar, gerekçeli
  karar yazımı) aşılıp aşılmadığını gösterir; gecikme nedenini sınıflar ve
  usul adımı seçenekleri önerir. Tazminat Komisyonu bildirimi gelen dosyaları
  ayrıca işaretler. Hâkim hakkında değerlendirme yapmaz, karar vermez.
tetik_ifadeleri:
  - "eski dosyalar"
  - "makul süre kontrolü"
  - "bekleyen dosyalar"
  - "aylık dosya yaşı raporu"
  - "hareketsiz dosyalar"
calisma: kullanici-tetikli
ilgili_skilller:
  - /hukuk-hakim:ara-karar
  - /idari-kalem:dosya-tekemmul
  - /vergi-kalem:dosya-tekemmul
  - /hukuk-kalem:tebligat
  - /ceza-kalem:muzekkere
---

# Makul Süre İzleyicisi

> Çıktı başlığı: `MAHKEME DAHİLİ ÇALIŞMA NOTU — MAKUL SÜRE — TASLAK (hâkim/heyet onayı şart)`.
> Makul sürenin aşılıp aşılmadığı dosyanın bütününe göre değerlendirilen bir hukuki sorudur; izleyici bu değerlendirmeyi yapmaz, veriyi ve seçenekleri düzenler.

## Amaç

Davaların en az giderle ve mümkün olan süratle sonuçlandırılması yargının görevidir (AY m. 141/4); makul sürede yargılanma hakkı adil yargılanma hakkının unsurudur (AY m. 36). HMK'da hâkim yargılamanın makul süre içinde ve düzenli yürütülmesini sağlamakla yükümlüdür (HMK m. 30). İzleyici mahkemenin elindeki eski ve hareketsiz dosyaları görünür kılar ve her biri için atılabilecek usul adımlarını sıralar.

## Ne zaman çalışır

Kullanıcı tetikler: "eski dosyalar", "aylık dosya yaşı raporu". Önerilen düzen: ayda bir; adli yıl başında ve adli tatil öncesinde ek çalıştırma. Zamanlanmış çalışma yoktur.

## Girdi

Kullanıcının verdiği derdest dosya listesi veya kalemin UYAP'tan dışa aktardığı liste, tercihen maskeli. Liste yoksa uydurulmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: UYAP'taki kendi ekranınız (adliyede UYAP; dışarıda VPN ile vpn.uyap.gov.tr ya da UYAP Mobil)`. Ortak kaynak sırası ve UYARI satırı: `references/izleyici-rehberi.md` bölüm 3. Dosya başına: esas no, dal, usul (yazılı, basit, ivedi), dava/iddianame tarihi, son işlem tarihi ve türü, son ve sonraki duruşma tarihi, bekleyen işler (tebligat, bilirkişi, müzekkere, istinabe, keşif, bekletici sorun), tutuklu var mı, idari dosyada tekemmül tarihi, karar tefhim edilmiş ama gerekçesi yazılmamış mı, Tazminat Komisyonundan bildirim var mı.

## Süreye bağlanmış aşamalar (27.09.2026'da çekilen metne göre)

| Aşama | Kural | Madde |
|---|---|---|
| Hukuk duruşmaları arası | üç aydan uzun olamaz; zorunlu hâlde gerekçeyle daha uzun | HMK m. 147/3 |
| Basit yargılama | ilk duruşma dışında iki duruşmada tamamlanır; aralar bir ayı geçmez, zorunlu hâlde gerekçeyle uzatılır | HMK m. 320/3 |
| Gerekçeli karar (hukuk) | yalnız hüküm sonucu tefhim edildiyse tefhimden itibaren bir ay içinde yazılır | HMK m. 294/4 |
| Gerekçe (ceza) | tutanağa geçirilmemişse açıklamadan itibaren en geç on beş gün içinde dosyaya konur | CMK m. 232/3 |
| İdari yargı | tekemmül eden dosyalar öncelik sırası gözetilerek, diğerleri tekemmülden itibaren en geç altı ay içinde sonuçlandırılır | İYUK m. 20/5 |
| İdari kararlar | verildiği tarihten itibaren otuz gün içinde yazılır ve imzalanır | İYUK m. 24 |
| Yürütmenin durdurulması kararı | on beş gün içinde yazılır ve imzalanır | İYUK m. 27/9 |
| İvedi yargılama | tekemmülden itibaren en geç bir ay içinde karar | İYUK m. 20/A |
| İcra mahkemesi | duruşmasız işlerde en geç on gün içinde karar; erteleme en çok otuz gün | İİK m. 18/3 |
| İşe iade | dava ivedilikle sonuçlandırılır | 4857 s.K. m. 20/3 |
| Tutukluluk | azami süreler | CMK m. 102 |

## Tazminat mekanizması

- Ceza soruşturma ve kovuşturmaları ile özel hukuk ve idare hukuku yargılamalarının makul sürede sonuçlandırılmadığı iddiasıyla manevi tazminat istemleri Tazminat Komisyonuna yapılır (6384 s.K. m. 2/3-a). Müracaat süreç devam ederken ya da en geç kesin kararın öğrenilmesinden itibaren bir ay içinde yapılır (m. 5/A).
- Komisyonun kesinleşen kararının örneği işlemin yapıldığı adli veya idari mercie gönderilir; işlem henüz sonuçlanmamışsa ilgili merci işlemi ivedilikle sonuçlandırır (6384 s.K. m. 8). Bu bildirim gelen dosya 🔴 işaretlenir.
- Komisyon kararlarına tebliğden itibaren on beş gün içinde Ankara Bölge İdare Mahkemesine itiraz edilebilir (m. 7/4).

## Değerlendirme ölçütleri (bilgi için)

AYM, bir davanın süresinin makul olup olmadığında davanın karmaşıklığını, yargılamanın kaç dereceli olduğunu, tarafların ve ilgili makamların yargılama sürecindeki tutumunu ve başvurucunun davanın hızla sonuçlandırılmasındaki menfaatinin niteliğini göz önünde bulundurur (AYM, B. No: 2014/176, 09.09.2015, § 31). Ceza yargılamasında süre, suç isnadının bildirilmesi, isnattan ilk etkilenilen tedbir veya kamu davasının açılması anından başlatılır (aynı karar, § 33). İzleyici bu ölçütleri gecikme nedeni sınıflamasında kullanır; ihlal değerlendirmesi yapmaz.

## Adımlar

1. **Yaş ve hareketsizlik.** Her dosya için dava tarihinden bugüne yaşı ve son işlemden bu yana geçen günü hesapla. [DOLDUR: mahkemenin veya HSK'nın izlediği hedef süreler — izleyici bunları kendisi belirlemez].
2. **Kanuni aşama kontrolü.** Yukarıdaki tabloya göre aşılan aşamayı işaretle. Gerekçe gerektiren uzun erteleme varsa gerekçenin tutanakta olup olmadığını sor.
3. **Gecikme nedeni.** Her dosyayı sınıfla: mahkeme içi (gerekçe yazımı, duruşma aralığı), taraf kaynaklı (tebligat, harç, delil), üçüncü kurum (bilirkişi, kurum cevabı, istinabe), bekletici sorun. Bilirkişi kaynaklıysa `bilirkisi-rapor-izleyici`, tebligat kaynaklıysa `durusma-hazirlik` ile eşleştir.
4. **İşlemden kaldırma denetimi.** Taraflar gelmediği için işlemden kaldırılıp üç ay içinde yenilenmeyen dava, sürenin dolduğu gün itibarıyla açılmamış sayılır ve mahkemece kendiliğinden karar verilerek kayıt kapatılır (HMK m. 150/5). Böyle dosyalar listede derdest görünüyorsa işaretle.
5. **Seçenekler.** Her dosya için 2-3 usul adımı öner: kurum cevabı için tekit müzekkeresi, bilirkişiye süre hatırlatması, istinabe yerine ses ve görüntü nakliyle dinleme seçeneği (HMK m. 149), tebligatta adres kayıt sistemi adresi (7201 s.K. m. 10), bekletici sorunun gözden geçirilmesi.

## Çıktı şablonu

```
MAHKEME DAHİLİ ÇALIŞMA NOTU — MAKUL SÜRE — TASLAK (hâkim/heyet onayı şart)
Tarih: GG.AA.YYYY · [N] derdest dosya · Kaynak: [liste, GG.AA.YYYY]

🔴 KANUNİ SÜRESİ AŞILMIŞ AŞAMA / KOMİSYON BİLDİRİMİ ([N])
| Dosya | Yaş | Son işlem | Aşılan aşama | Gecikme nedeni | Seçenekler |
🟠 HAREKETSİZ (son işlemden [X] günden fazla) ([N])
🟡 ESKİ DOSYA, AKIŞ SÜRÜYOR ([N])
🟢 ÖZET: yaş dağılımı (0-1 yıl / 1-2 yıl / 2 yıldan fazla)

⚠️ İnceleyen notu: bu rapor ihlal tespiti değildir; madde kontrolü; eksik veriler.
```

Şiddet:
- 🔴 kanuni süresi aşılmış aşama (gerekçe yazımı, tekemmülden karar, gerekçesiz uzun erteleme); Tazminat Komisyonu bildirimi; tutuklu dosyada azami süreye yaklaşma.
- 🟠 kullanıcının belirlediği eşikten uzun hareketsizlik.
- 🟡 eski ama işleyen dosya.
- 🟢 özet.

## Sınırlar

- Makul sürenin ihlal edildiğine veya edilmediğine karar vermez; hâkim, kalem veya mahkeme hakkında performans değerlendirmesi yapmaz.
- UYAP'a bağlanmaz, kayıt eklemez, müzekkere göndermez.
- Süreler hatırlatmadır; tarihler UYAP kaydından teyit edilir. Tarih bilinmiyorsa en elverişsiz varsayım yapılır ve uyarı düşülür.
- Taraf adları ve dava konusu ayrıntıları özetlenmez; dosya numarası ve aşama yeterlidir.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): AY m. 36, 141; HMK m. 30, 147, 149, 150, 294, 320; CMK m. 102, 232; İYUK m. 20, 20/A, 24, 27; İİK m. 18; 4857 s.K. m. 20; 6384 s.K. m. 2, 5/A, 7, 8; 7201 s.K. m. 10. AYM B. No: 2014/176 kararı `tr_aym_getir` ile okundu.*
