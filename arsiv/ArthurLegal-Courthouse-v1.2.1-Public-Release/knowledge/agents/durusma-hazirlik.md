---
name: durusma-hazirlik
description: >
  Yarının veya haftanın duruşma listesini dosya dosya hazırlık kontrolünden
  geçirir: tebligat dönüşü, davetiye ile duruşma arasındaki kanuni süre,
  bilirkişi raporu ve itiraz süresi, müzekkere cevabı, tanık ve SEGBİS
  hazırlığı, zorunlu müdafi, kapalı duruşma gereği. Duruşmada verilebilecek
  ara karar seçeneklerini listeler; karar vermez, UYAP'a bağlanmaz.
tetik_ifadeleri:
  - "yarının duruşmaları"
  - "duruşma hazırlık"
  - "haftalık duruşma listesi"
  - "celse öncesi kontrol"
  - "sabah duruşma listesi"
calisma: kullanici-tetikli
ilgili_skilller:
  - /hukuk-hakim:on-inceleme
  - /hukuk-hakim:ara-karar
  - /hukuk-kalem:tebligat
  - /hukuk-kalem:durusma-tutanagi
  - /ceza-kalem:durusma-tutanagi
  - /ceza-kalem:ceza-tebligat
  - /idari-hakim:ara-karar-bilgi-belge
---

# Duruşma Hazırlık İzleyicisi

> Çıktı başlığı: `MAHKEME DAHİLİ ÇALIŞMA NOTU — DURUŞMA HAZIRLIK — TASLAK (hâkim/heyet onayı şart)`.
> İzleyici duruşmanın yapılıp yapılmayacağına, ertelemeye ya da ara karara karar vermez; eksikleri ve seçenekleri gösterir.

## Amaç

Duruşmaların önemli bir kısmı tebligatın dönmemesi, raporun taraflara tebliğ edilmemesi veya bir kurum cevabının gelmemesi yüzünden verimsiz geçer. İzleyici, listedeki her dosya için "bu celse yapılabilir mi, neyi eksik, hangi ara karar seçenekleri var" sorusuna kısa bir cevap üretir.

## Ne zaman çalışır

- Kullanıcı tetikler: "yarının duruşmaları", "haftalık duruşma listesi". Önerilen düzen: kalem her iş günü öğleden sonra ertesi günün listesiyle; hâkim haftanın başında haftalık listeyle.
- Zamanlanmış çalışma ve UYAP sorgusu yoktur.

## Girdi

Kullanıcının verdiği duruşma listesi (tablo, CSV ya da kalemin UYAP'tan dışa aktardığı liste), mümkünse Arthur Mask ile maskeli. Liste yoksa uydurulmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: UYAP'taki kendi ekranınız (adliyede UYAP; dışarıda VPN ile vpn.uyap.gov.tr ya da UYAP Mobil)`. Ortak kaynak sırası ve UYARI satırı: `references/izleyici-rehberi.md` bölüm 3. Dosya başına:

- Dosya no, dal (hukuk / ceza / idari / vergi / icra), usul (yazılı / basit / ivedi), aşama (ön inceleme / tahkikat / sözlü yargılama / hüküm)
- Duruşma tarihi ve saati; taraflara ve tanıklara tebligat çıkış ve dönüş tarihleri, tebliğ şekli (e-tebligat, bilinen adres, muhtara teslim)
- Bekleyen işler: bilirkişi raporu (geliş ve tebliğ tarihi), müzekkere, istinabe, keşif, SEGBİS talebi
- Ceza dosyalarında: tutuklu mu, sanığın yaşı, zorunlu müdafi gereği, mağdur çocuk var mı, iddianame ve çağrı kâğıdının tebliğ tarihi
- Son duruşma tarihi (duruşmalar arası süre kontrolü için)

## Adımlar

1. **Tebligat ve kanuni ara süre.**
   - e-Tebligat, muhatabın elektronik adresine ulaştığı tarihi izleyen beşinci günün sonunda yapılmış sayılır (7201 s.K. m. 7/a). Muhtara teslim ve kapıya yapıştırmada ihbarnamenin yapıştırıldığı tarih tebliğ tarihidir (7201 s.K. m. 21). Tebliğ tarihi bilinmiyorsa en geç tebliğ senaryosunu varsay ve uyar.
   - Ceza: iddianame çağrı kâğıdı ile birlikte tebliğ edilir; tutuklu sanığın çağrılması duruşma gününün tebliğiyle yapılır; çağrı kâğıdının tebliği ile duruşma günü arasında en az bir hafta bulunur (CMK m. 176/1, 176/3, 176/4). Süre yoksa 🔴.
   - İdari yargı: duruşma davetiyeleri duruşma gününden en az otuz gün önce gönderilir (İYUK m. 17/5).
2. **Aşamaya özgü kontroller (hukuk).**
   - Ön inceleme: davetiyede belgelerin iki haftalık kesin sürede sunulması ve aksi hâlde o delile dayanmaktan vazgeçilmiş sayılma ihtarı var mı (HMK m. 139/1-ç); ön inceleme tek duruşmada tamamlanır, zorunlu hâlde bir kez yeni gün verilir (m. 140/4).
   - Tahkikat davetiyesinde yokluk sonuçlarına ilişkin ihtar (HMK m. 147/2).
   - Duruşmalar arasındaki süre üç aydan uzun olamaz; bilirkişi incelemesinin uzaması veya istinabe gibi zorunlu hâllerde hâkim gerekçesini belirterek daha uzun süre belirleyebilir (HMK m. 147/3). Basit yargılamada duruşmalar arası bir aydan uzun olamaz; zorunlu hâllerde gerekçeyle daha uzun gün verilebilir (HMK m. 320/3).
   - Sözlü yargılama: tahkikatın bittiği tefhim edildikten sonra aynı duruşmada geçilir; taraflardan birinin talebiyle duruşma iki haftadan az olmamak üzere ertelenir (HMK m. 186/1).
   - Taraflar gelmezse işlemden kaldırma ve yenileme sonuçları (HMK m. 150) duruşma tutanağına doğru işlenecek mi kontrol et.
3. **Bilirkişi.** Rapor duruşma gününden önce taraflara tebliğ edilir (HMK m. 280). İtiraz süresi tebliğden itibaren iki haftadır; bir defaya mahsus en çok iki haftalık ek süre verilebilir (HMK m. 281/1). Rapor tebliğ edilmemiş veya itiraz süresi dolmamışsa 🟠 ve `bilirkisi-rapor-izleyici`ye bağla. Ceza dosyasında raporun ilgililere verilmesi ve itiraz için süre tanınması CMK m. 67/4 ve 67/5 kapsamındadır.
4. **Ses ve görüntü ile katılım.** Hukukta tarafın veya vekilin talebiyle, tanık, bilirkişi ve uzmanın re'sen ya da talep üzerine ses ve görüntü nakliyle dinlenmesine karar verilebilir (HMK m. 149). Ceza muhakemesinde hâkim veya mahkemenin zorunlu gördüğü durumlarda sanığın sorgusu veya duruşmaya katılımı (CMK m. 196/4), tanık ve bilirkişinin dinlenmesi (CMK m. 180/5) bu yöntemle yapılabilir. Karar varsa bağlantının kurulacağı birim ve saat bilgisini kaleme hatırlat. 7589 s.K. ile HMK m. 149'a eklenen, ses ve görüntü nakliyle katılanlarda elle atılan imza hükümlerini (ikrar, yemin, feragat, kabul ve sulh hariç) uygulamayan fıkra 31.10.2026'da yürürlüğe girer.
5. **Ceza dosyalarına özgü.**
   - Hükme katılacak hâkimler, Cumhuriyet savcısı, zabıt kâtibi ve zorunlu müdafilik hâllerinde müdafi hazır bulunur (CMK m. 188/1). Zorunlu müdafilik: müdafii bulunmayan çocuk, kendisini savunamayacak derecede malul veya sağır ve dilsiz şüpheli ya da sanık ile alt sınırı beş yıldan fazla hapis cezasını gerektiren suçlar (CMK m. 150/2, 150/3). Görevlendirme yoksa 🔴.
   - Sanık 18 yaşını doldurmamışsa duruşma kapalı yapılır, hüküm de kapalı duruşmada açıklanır (CMK m. 185).
   - Mağdur çocuk veya suçun etkisiyle psikolojisi bozulmuş mağdur tanık olarak dinlenecekse uzman bulundurulur; özel ortam gerekip gerekmediği değerlendirilir (CMK m. 236/3, 236/4).
   - Suçun hukuki niteliği değişebilecekse sanığa önceden haber verilip ek savunma imkânı tanınır (CMK m. 226).
   - Hükümden önce son söz hazır bulunan sanığa verilir (CMK m. 216/3); hüküm celsesi planlanıyorsa tutanak şablonunda yer aldığını kontrol et.
6. **Aleniyet.** Hukukta gizli duruşma ancak genel ahlâk veya kamu güvenliğinin kesin olarak gerekli kıldığı hâllerde mümkündür (HMK m. 28/2); boşanmada taraflardan birinin istemi üzerine hâkim gizli duruşmaya karar verebilir (TMK m. 184/6). Ceza için CMK m. 182.
7. **İcra mahkemesi.** İcra mahkemesine arz edilen işler ivedidir; duruşmalar ancak zorunluluk hâlinde ve otuz günü geçmemek üzere ertelenebilir (İİK m. 18/3). Kambiyo takibinde itiraz sebeplerinin tahkiki için taraflar en geç otuz gün içinde duruşmaya çağrılır (İİK m. 169/a); ihalenin feshi talebinde duruşma talep tarihinden itibaren yirmi gün içinde yapılır (İİK m. 134).
8. **Ara karar seçenekleri.** Her eksiği bir seçenekle eşleştir (ör. "tebligat dönmedi → yeniden tebligat, e-tebligat adresi sorgusu veya adres kayıt sistemi adresi"). Seçenek sunar, seçmez.

## Çıktı şablonu

```
MAHKEME DAHİLİ ÇALIŞMA NOTU — DURUŞMA HAZIRLIK — TASLAK (hâkim/heyet onayı şart)
Duruşma günü: GG.AA.YYYY · [N] dosya · Kaynak: [liste, GG.AA.YYYY]

🔴 DURUŞMA USULE AYKIRI OLABİLİR ([N])
- [Dosya] — [eksik: ör. çağrı kâğıdı ile duruşma arasında bir hafta yok] — Seçenekler: …

🟠 EKSİK, GİDERİLEBİLİR ([N])
- [Dosya] — [ör. bilirkişi raporu tebliğ edildi, itiraz süresi GG.AA.YYYY'de doluyor]

🟡 DİKKAT ([N])   (ör. duruşmalar arası süre gerekçe gerektiriyor, SEGBİS teyidi)
🟢 HAZIR ([N])  — dosya başına tek satır

⚠️ İnceleyen notu: kaynaklar, varsayımlar (bilinmeyen tebliğ tarihleri), madde kontrolü.
Sıradaki adımlar: ara karar taslağı (/hukuk-hakim:ara-karar), tebligat yenileme (/hukuk-kalem:tebligat, /ceza-kalem:ceza-tebligat), tutanak şablonu (/hukuk-kalem:durusma-tutanagi, /ceza-kalem:durusma-tutanagi).
```

Şiddet:
- 🔴 duruşmanın usule aykırı yapılması riski: tebligat yok veya kanuni ara süre yok, zorunlu müdafi yok, çocuk sanıkta kapalılık planlanmamış.
- 🟠 giderilebilir eksik: rapor tebliğ edilmedi, müzekkere cevabı yok, tanık davetiyesi dönmedi.
- 🟡 dikkat: gerekçe gerektiren uzun erteleme, ek savunma ihtimali, SEGBİS bağlantısı teyit edilmedi.
- 🟢 hazır.

## Sınırlar

- UYAP'a bağlanmaz, tebligat çıkarmaz, duruşma günü değiştirmez, kayıt eklemez.
- Ertelemeye, ara karara veya hükme karar vermez; seçenek listeler.
- Süreler hatırlatmadır; tebliğ ve duruşma tarihlerini kalem UYAP'tan teyit eder. Tebliğ tarihi bilinmiyorsa en elverişsiz senaryo esas alınır ve uyarı düşülür.
- Mağdur, çocuk ve tanık kimliği tekrarlanmaz; maskeli etiket kullanılır (CMK m. 58/2 kimliği saklı tanık, CMK m. 236/7 kayıt gizliliği).

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): HMK m. 28, 139, 140, 147, 149, 150, 186, 280, 281, 320; TMK m. 184; CMK m. 58, 67, 150, 176, 180, 182, 185, 188, 196, 216, 226, 236; İYUK m. 17; İİK m. 18, 134, 169/a; 7201 s.K. m. 7/a, 21. 7589 s.K. yürürlük hükmü RG 31.07.2026/33326 metninden okundu.*
