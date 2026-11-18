---
name: kanun-yolu-kesinlesme-izleyici
description: >
  Karar verilmiş dosyalarda tebliğ tarihlerinden kanun yolu sürelerini izler;
  süresi dolan dosyalarda kesinleşme kaydını, kanun yoluna başvurulanlarda
  cevap süresini ve dosyanın üst mahkemeye gönderilmesini hatırlatır. HMK,
  CMK, İYUK ve İİK sürelerini ayrı hesaplar. Karar vermez, kesinleşme şerhi
  düşmez, UYAP'a bağlanmaz.
tetik_ifadeleri:
  - "kesinleşme kontrolü"
  - "kanun yolu süreleri"
  - "istinaf süresi dolanlar"
  - "haftalık kesinleşme listesi"
  - "gönderilecek dosyalar"
calisma: kullanici-tetikli
ilgili_skilller:
  - /hukuk-kalem:kesinlesme-serhi
  - /hukuk-kalem:istinaf-gonderme-kontrol
  - /ceza-kalem:kanun-yolu-gonderme
  - /ceza-kalem:infaz-evraki
  - /idari-kalem:kanun-yolu-gonderme
  - /idari-kalem:karar-uygulama-takip
  - /vergi-kalem:karar-uygulama-iade
  - /istinaf-kalem:dosya-kabul-kontrol
---

# Kanun Yolu ve Kesinleşme İzleyicisi

> Çıktı başlığı: `MAHKEME DAHİLİ ÇALIŞMA NOTU — KANUN YOLU / KESİNLEŞME — TASLAK (hâkim/heyet onayı şart)`.
> Süre hatırlatmadır. Kesinleşme kaydını hâkim imzalar; kalem UYAP'tan tebliğ ve başvuru kayıtlarını teyit eder.

## Amaç

Kesinleşmesi geciken karar infaza, icraya ve sicile geç yansır; erken kesinleşme şerhi ise hak kaybına yol açar. İzleyici her karar için taraf bazında süre sonunu hesaplar, "kesinleşti", "kanun yoluna başvuruldu", "tebliğ eksik" diye ayırır.

## Ne zaman çalışır

Kullanıcı tetikler: "kesinleşme kontrolü", "haftalık kesinleşme listesi". Önerilen düzen: kalemde haftada bir; tefhim yoğunluğu olan günlerin ertesinde ek çalıştırma. Zamanlanmış çalışma yoktur.

## Girdi

Kullanıcının verdiği liste (tablo, CSV veya kalemin UYAP'tan dışa aktardığı karar ve tebligat listesi), tercihen maskeli. Liste yoksa uydurulmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: UYAP'taki kendi ekranınız (adliyede UYAP; dışarıda VPN ile vpn.uyap.gov.tr ya da UYAP Mobil)`. Ortak kaynak sırası ve UYARI satırı: `references/izleyici-rehberi.md` bölüm 3. Karar başına: dal, karar türü (nihai karar, ihtiyati tedbir, çekişmesiz yargı, hüküm, HAGB, basit yargılama hükmü, idari karar, YD kararı), karar ve tefhim tarihi, dava değeri veya ceza miktarı, her taraf için tebliğ tarihi ve şekli, kanun yolu başvuru tarihi ve harç durumu, cevap dilekçesi tarihi.

## Hesap kuralları (27.09.2026'da çekilen metne göre)

| Dal | Başvuru | Süre ve başlangıç | Madde |
|---|---|---|---|
| Hukuk | istinaf | iki hafta; ilamın usulen taraflardan her birine tebliğiyle başlar | HMK m. 345 |
| Hukuk | temyiz | iki hafta; tebliğden | HMK m. 361 |
| Hukuk | istinaf veya temyize cevap | iki hafta; katılma yoluyla başvuru cevap dilekçesiyle | HMK m. 347, 348, 366 |
| Hukuk | süre geçmiş veya kesin karara başvuru | ilk derece reddeder; ret kararına iki hafta içinde istinaf | HMK m. 346 |
| Hukuk | eksik harç ve gider | bir haftalık kesin süre; tamamlanmazsa başvuru yapılmamış sayılır | HMK m. 344 |
| Hukuk | çekişmesiz yargı | kararın öğrenilmesinden iki hafta içinde istinaf | HMK m. 387 |
| İş | kanun yolu | süre ilamın taraflara tebliğinden işler; bazı kararlar temyiz edilemez | 7036 s.K. m. 7/4, m. 8 |
| İcra | istinaf / temyiz | tebliğden iki hafta | İİK m. 363, 364 |
| Ceza | istinaf | hükmün gerekçesiyle birlikte tebliğinden iki hafta; ağır cezadaki savcı için kararın o yer başsavcılığına gelişinden iki hafta | CMK m. 273/1, 273/3 |
| Ceza | temyiz | hükmün gerekçesiyle birlikte tebliğinden iki hafta | CMK m. 291/1 |
| Ceza | itiraz | kararın öğrenilmesinden iki hafta | CMK m. 268/1 |
| Ceza | istinafın reddine karşı | ret kararının tebliğinden iki hafta | CMK m. 276/2 |
| Ceza | HAGB kararı | istinaf yolu (7589 s.K. ile) | CMK m. 231/12 |
| İdari / vergi | istinaf | tebliğden otuz gün; parasal kesinlik sınırı var | İYUK m. 45/1 |
| İdari / vergi | temyiz | tebliğden otuz gün | İYUK m. 46/1, 46/2 |
| İdari / vergi | temyize cevap | tebliği izleyen otuz gün | İYUK m. 48/3 |
| İdari / vergi | ivedi yargılama | istinaf yok; temyiz tebliğden on beş gün | İYUK m. 45/8, 20/A |
| İdari / vergi | YD kararına itiraz | tebliği izleyen günden yedi gün | İYUK m. 27/7 |

Ortak kurallar:
- **Tebliğ tarihi:** e-tebligat, elektronik adrese ulaştığı tarihi izleyen beşinci günün sonunda yapılmış sayılır (7201 s.K. m. 7/a). Muhtara teslimde ihbarnamenin kapıya yapıştırıldığı tarih (m. 21), adres değişikliği bildirilmemişse eski adrese asılma tarihi (m. 35) tebliğ tarihidir. Usulsüz tebliğde muhatabın öğrendiğini beyan ettiği tarih esas alınır (m. 32).
- **Hesap:** HMK m. 92 ve 93, CMK m. 39, İYUK m. 8, İİK m. 19. Son gün resmî tatile rastlarsa süre ilk iş günü biter.
- **Adli tatil:** hukukta tatile rastlayan sürenin bitimi tatilin bittiği günden itibaren bir hafta uzar (HMK m. 104); ceza işlerinde tatile rastlayan süreler işlemez ve tatilin bittiği günden itibaren üç gün uzatılmış sayılır (CMK m. 331/4); idari yargıda yedi gün uzar (İYUK m. 8/3). Adli tatilde görülen işler için HMK m. 103 listesine bak.
- **Tutuklu:** tutuklu, zabıt kâtibine veya kurum müdürüne beyanla başvurabilir; bu işlemle süre kesilmiş sayılır (CMK m. 263).
- **Parasal sınırlar:** HMK m. 341/2 ve m. 362/1-a, İİK m. 363 ve 364, İYUK m. 45/1 ve 46/1-b'deki tutarlar her yıl yeniden değerleme oranında artırılır ve davanın açıldığı (icra şikâyetinde başvurunun yapıldığı) tarihteki sınır esas alınır (HMK ek m. 1; İİK ek m. 1; İYUK ek m. 1). Metindeki tutarı değil güncel tutarı kullan; güncel tutar çekilemezse UYARI satırı yaz.

## Adımlar

1. **Taraf bazında süre sonu.** Her taraf için tebliğ tarihinden süre sonunu hesapla; en geç tebliğ edilen tarafın süresi bitmeden kesinleşme yoktur. Tebliğ tarihi bilinmeyen taraf varsa dosyayı "tebliğ eksik" listesine al; kesinleşme hesabı yapma.
2. **Kanun yolu açık mı?** HMK m. 341/1 (istinafa açık kararlar), m. 362 (temyiz edilemeyen kararlar; 7589 s.K. ile eklenen m. 362/3), CMK m. 272/3 (istinaf edilemeyen hükümler), m. 286/2 (temyiz edilemeyen kararlar), İYUK m. 45/1 ikinci cümle ve m. 46/2 istisnaları, 7036 s.K. m. 8. Kesin kararda kesinleşme karar tarihine veya tefhim ve tebliğe bağlanabilir; hâkime soru olarak yaz.
3. **Başvuru varsa.** Harç ve giderler tam mı (HMK m. 344; İYUK m. 48/6), karşı tarafa tebliğ ve cevap süresi (HMK m. 347; CMK m. 277; İYUK m. 48/3), dosyanın gönderilmesi (HMK m. 347/3; CMK m. 277/2; İYUK m. 48/4). Yürütmenin durdurulması istemli temyiz dilekçesi tebliğ beklemeden gönderilir (İYUK m. 48/5).
4. **Süre dolmuş ve başvuru yoksa.** Hukukta hükmün kesinleştiği ilamın altına veya arkasına yazılır, tarih ve mühürle başkan veya hâkim imzalar; kanun yollarından geçerek kesinleşen kararların kesinleşme kaydı ve gerekli bildirimler de ilk derece mahkemesince yapılır (HMK m. 302/4, 302/5). Kişiler hukuku, aile hukuku ve taşınmaz ayni haklarına ilişkin kararlar kesinleşmedikçe yerine getirilemez (HMK m. 367/2); bu dosyaları ayrıca işaretle. Ceza ve idari dosyalar için ilgili skill'e yönlendir.
5. **Üst mahkemeden dönen dosyalar.** BİM'in temyize açık olmayan kararları ilk derece mahkemesine gönderilir ve yedi gün içinde tebliğe çıkarılır (İYUK m. 45/6); Danıştay onama kararları dosyanın gelişinden itibaren yedi gün içinde tebliğe çıkarılır (İYUK m. 50/1). Bozma üzerine yeniden inceleme ve uyma/direnme için `/istinaf-hakim:*` ve HMK m. 373, CMK m. 307, İYUK m. 50 akışına bak.
6. **İdari kararların uygulanması.** İdare esasa ve yürütmenin durdurulmasına ilişkin kararların icabına göre en geç otuz gün içinde işlem tesis eder (İYUK m. 28/1). Takip kalemin işidir: `/idari-kalem:karar-uygulama-takip`.

## Çıktı şablonu

```
MAHKEME DAHİLİ ÇALIŞMA NOTU — KANUN YOLU / KESİNLEŞME — TASLAK (hâkim/heyet onayı şart)
Tarih: GG.AA.YYYY · [N] karar · Kaynak: [liste, GG.AA.YYYY]

🔴 İŞLEM GEREKİR ([N])
| Dosya | Karar | Son tebliğ | Süre sonu | Durum | Öneri |
(süresi dolmuş ve başvurusuz: kesinleşme kaydı taslağı / süresi bugün doluyor / harç için kesin süre bitti)

🟠 7 GÜN İÇİNDE SÜRESİ DOLACAK ([N])
🟡 BAŞVURU VAR: CEVAP SÜRESİ VEYA GÖNDERME BEKLİYOR ([N])
🟢 İZLEMEDE ([N])
TEBLİĞ EKSİK ([N]): dosya — tebliğ edilmeyen taraf — kesinleşme hesaplanmadı

⚠️ İnceleyen notu: adli tatil etkisi, parasal sınır (güncel tutar çekildi mi), madde kontrolü.
```

Şiddet:
- 🔴 süre bugün veya yarın doluyor; süre dolmuş ve başvuru yok (kesinleşme işlemi bekliyor); eksik harç için verilen kesin süre bitti.
- 🟠 süre 7 gün içinde doluyor.
- 🟡 kanun yoluna başvurulmuş; cevap süresi veya gönderme bekliyor.
- 🟢 izlemede.

## Sınırlar

- UYAP'a bağlanmaz; kesinleşme şerhi, ilam veya gönderme yazısını sisteme işlemez, yalnız taslak ve hatırlatma üretir.
- Kanun yolunun açık olup olmadığına karar vermez; metne göre işaretler, hâkime sorar.
- Tebliğ tarihi bilinmiyorsa kesinleşme hesabı yapmaz. Kanun yolu süresi için en erken bitiş gününü gösterir ve uyarır.
- Parasal sınırlarda güncel tutar çekilemezse metindeki tutarla hesap yapmaz; UYARI satırı yazar.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): HMK m. 92, 93, 103, 104, 302, 341, 344, 345, 346, 347, 348, 361, 362, 366, 367, 373, 387, ek m. 1; CMK m. 39, 231, 263, 268, 272, 273, 276, 277, 286, 291, 307, 331; İYUK m. 8, 20/A, 27, 28, 45, 46, 48, 50, ek m. 1; İİK m. 19, 363, 364, ek m. 1; 7036 s.K. m. 7, 8; 7201 s.K. m. 7/a, 21, 32, 35.*
