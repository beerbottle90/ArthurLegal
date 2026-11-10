# Mahkeme Türü Profili — İdare ve Vergi Mahkemeleri

> `mahkeme-profili.md` ile birlikte okunur; ayrıntı için `iyuk-rehberi.md`, `vergi-yargisi-rehberi.md`, `yurutmenin-durdurulmasi-rehberi.md`. Madde numaraları 27.09.2026'da ArthurLegal MCP ile çekilen metne dayanır; karar gövdesine girmeden önce yeniden çekilir.

## Kim kullanır

- **Hâkim ve heyet:** 2576 s.K. m. 7'de sayılan davalar mahkeme hâkimlerinden biri tarafından çözülür; heyet yapısı ve dağılım için mahkemeye özgü alanlara bakın. 7589 s.K. ile tek hâkim sınırı, düzenleyici işlemlere karşı açılanlar hariç, konusu dört yüz seksen altı bin Türk lirasını aşmayan iptal ve tam yargı davaları ile vergi uyuşmazlıklarında aynı tutar olarak belirlendi; yürürlükten sonra açılan davalara uygulanır (2576 s.K. m. 7/1, 7/2; 7589 s.K. geçici m. 1/2). Tutarın güncelliği her dosyada çekilir.
- Plugin: `idari-hakim`, `idari-kalem`, `vergi-hakim`, `vergi-kalem`.

## Görev

- **İdare mahkemesi:** vergi mahkemelerinin görevine giren ve ilk derecede Danıştayda çözümlenecek olanlar dışındaki iptal ve tam yargı davaları, tahkim öngörülmeyen idari sözleşme uyuşmazlıkları ve diğer kanunlarla verilen işler (2576 s.K. m. 5).
- **Vergi mahkemesi:** genel bütçeye, il özel idarelerine, belediye ve köylere ait vergi, resim, harç ve benzeri mali yükümler ile zam ve cezaları ve tarifelere ilişkin davalar; bu konularda 6183 s.K.'nın uygulanmasına ilişkin davalar (2576 s.K. m. 6).
- **Danıştay ilk derece:** Cumhurbaşkanı kararları, CB kararnameleri dışındaki Cumhurbaşkanınca çıkarılan düzenleyici işlemler, bakanlıklar ve kamu kuruluşlarının ülke çapında uygulanacak düzenleyici işlemleri, birden çok mahkemenin yetki alanına giren işler ve sayılan diğer işler (2575 s.K. m. 24).
- **Dava türleri ve sınır:** iptal, tam yargı ve idari sözleşme davaları; idari yargı yetkisi hukuka uygunluk denetimiyle sınırlıdır, yerindelik denetimi yapılamaz (İYUK m. 2).
- **Yetki:** kural olarak işlemi veya sözleşmeyi yapan idari merciin bulunduğu yerdeki idare mahkemesi; yetki kamu düzenindendir (İYUK m. 32).

## Usul akışı

1. **Dilekçe ve ilk inceleme:** dilekçe İYUK m. 3'e uygun olmalı. İlk inceleme görev ve yetki, idari merci tecavüzü, ehliyet, kesin ve yürütülmesi gereken işlem, süre aşımı, husumet ile m. 3 ve m. 5'e (aynı dilekçeyle dava açılabilecek hâller) uygunluk yönlerinden sırasıyla, dilekçenin alındığı tarihten itibaren en geç on beş gün içinde yapılır (İYUK m. 14); sonuçları m. 15'te (ret, gönderme, gerçek hasma tebliğ, otuz günde yenilenmek üzere dilekçe reddi).
2. **Tebligat ve savunma:** tebliğden itibaren otuz gün içinde cevap; haklı sebeple bir defaya mahsus otuz güne kadar uzatma (İYUK m. 16/3). Tam yargı davasında miktar nihai karara kadar bir defaya mahsus artırılabilir (m. 16/4).
3. **Re'sen araştırma:** mahkemeler her türlü incelemeyi kendiliğinden yapar, bilgi ve belge ister; ara karar gereği yerine getirilmezse bunun etkisi önceden takdir edilip ara kararda belirtilir; dosyalar tekemmül sırasına göre ve tekemmülden itibaren en geç altı ay içinde sonuçlandırılır (İYUK m. 20). `/idari-hakim:ara-karar-bilgi-belge`, `/idari-kalem:dosya-tekemmul`.
4. **Duruşma:** iptal davaları ile kanundaki tutarı aşan tam yargı ve vergi davalarında taraf isteğiyle; davetiyeler en az otuz gün önce (İYUK m. 17/1, 17/5); tutar dava tarihindeki güncel sınıra göre (İYUK ek m. 1).
5. **Yürütmenin durdurulması:** telafisi güç veya imkânsız zarar ve açık hukuka aykırılık birlikte; kural olarak savunma alındıktan veya süresi geçtikten sonra, gerekçeli; kararda hukuka aykırılık ve zararın ne olduğu belirtilir; itiraz tebliği izleyen günden yedi gün, merci yedi gün içinde karar verir; YD kararları on beş gün içinde yazılır; aynı sebeple ikinci kez YD istenemez (İYUK m. 27/2, 27/7, 27/9, 27/10). `/idari-hakim:yurutmenin-durdurulmasi`.
6. **Karar:** kararda bulunacak hususlar; karar verildiği tarihten itibaren otuz gün içinde yazılır ve imzalanır (İYUK m. 24). İdare, esasa ve YD'ye ilişkin kararların gereğini en geç otuz gün içinde yerine getirir (m. 28/1).

## Vergi davalarına özgü

- Dava açılması, tarh edilen vergi ve cezaların dava konusu bölümünün tahsilini durdurur; ihtirazi kayıtla verilen beyannameler üzerine yapılan işlemler ve tahsilat işlemleri için açılan davalar tahsili durdurmaz, bunlar için YD istenebilir (İYUK m. 27/4).
- Mükellefler ve kendilerine vergi cezası kesilenler tarh edilen vergilere ve cezalara karşı dava açabilir; beyan edilen matrahlara ve bunlar üzerinden tarh edilen vergilere karşı dava açılamaz, vergi hatalarına ilişkin hükümler saklıdır (VUK m. 377, 378).
- Ödeme emrine itiraz tebliğden itibaren on beş gündür (6183 s.K. m. 58/1). Metin itiraz merciini "vergi itiraz komisyonu" olarak anar; 6183 s.K.'nın uygulanmasına ilişkin davalar vergi mahkemesinin görevindedir (2576 s.K. m. 6/b). Merciin uygulamadaki karşılığı için güncel içtihadı çekin.
- Vergi uyuşmazlıklarında İYUK'ta hüküm olmayan hâllerde VUK uygulanır (İYUK m. 31/2).

## İvedi yargılama

İhale işlemleri (ihaleden yasaklama hariç), acele kamulaştırma, Özelleştirme Yüksek Kurulu kararları, 2634 s.K. uyarınca satış, tahsis ve kiralama işlemleri, idari yaptırımlar hariç ÇED kararları ve 6306 s.K. uyarınca Cumhurbaşkanı kararları: dava süresi otuz gün, üst makama başvuru uygulanmaz, ilk inceleme yedi gün, savunma on beş gün (+ en çok on beş gün), YD kararlarına itiraz yok, tekemmülden itibaren en geç bir ayda karar, temyiz tebliğden on beş gün (İYUK m. 20/A); istinaf yolu yoktur (m. 45/8).

## Kritik süreler

| İşlem | Süre | Madde |
|---|---|---|
| Dava açma | Danıştay ve idare mahkemesinde 60 gün, vergi mahkemesinde 30 gün | İYUK m. 7/1 |
| İdarenin sükûtu | 30 gün cevap verilmezse ret; bekleme en çok 4 ay | İYUK m. 10/2 |
| Üst makama başvuru | dava süresini durdurur; 30 günde cevap verilmezse ret | İYUK m. 11 |
| Eylemden doğan tam yargı | öğrenmeden 1 yıl, her hâlde eylemden 5 yıl içinde idareye başvuru | İYUK m. 13/1 |
| Adli yargıdan görevsizlik sonrası | kesinleşmeden 30 gün | İYUK m. 9/1 |
| Savunma ve cevap | 30 gün (+ en çok 30 gün) | İYUK m. 16/3 |
| YD itirazı | 7 gün | İYUK m. 27/7 |
| Ödeme emrine itiraz | 15 gün | 6183 s.K. m. 58/1 |
| İstinaf | tebliğden 30 gün | İYUK m. 45/1 |
| Temyiz | tebliğden 30 gün | İYUK m. 46 |

Süreler tebliğ, yayın veya ilan tarihini izleyen günden işler; son gün tatile rastlarsa izleyen çalışma günü biter; çalışmaya ara verme (20 Temmuz - 31 Ağustos) zamanına rastlayan süre, ara vermenin sona erdiği günü izleyen tarihten itibaren yedi gün uzar (İYUK m. 8, 61/1).

## 2026 değişiklikleri (7589 s.K., RG 31.07.2026)

- BİM'in istinafı reddetme hâlleri ve kaldırarak dosyayı geri gönderebileceği hâller sınırlandı; bu hâller dışında kaldırıp geri gönderme yapılamaz (İYUK m. 45/3, 45/5).
- Temyize açık davalar listesinden bir bent çıkarıldı; m. 46/1 kapsamı dışındaki davalarda BİM'in kaldırma üzerine yeniden verdiği kararlar otuz gün içinde temyiz edilebilir, sayılan istisnalar hariç (İYUK m. 46/2); yürürlükten sonra BİM'lerce verilen kararlara uygulanır (7589 s.K. geçici m. 1/3).
- Tek hâkim sınırı (2576 s.K. m. 7).

## Sık usul riskleri (genel)

- 🔴 Süre aşımının ilk incelemede ve her aşamada kontrol edilmemesi (İYUK m. 14/3-e, 14/6).
- 🔴 YD kararında hukuka aykırılık ve zararın gerekçelendirilmemesi (İYUK m. 27/2).
- 🟠 Husumetin yanlış idareye yöneltildiği dosyada gerçek hasma tebliğ yerine ret (İYUK m. 15/1-c).
- 🟠 Ara karara uyulmamasının etkisinin ara kararda belirtilmemesi (İYUK m. 20/2).
- 🟡 Tekemmülden itibaren altı aylık sürenin aşılması (İYUK m. 20/5; `makul-sure-izleyici`).

## Kalem iş akışı

- İlk inceleme raporu ve tebligat; idarelere e-tebligat (7201 s.K. m. 7/a); işlem dosyası istenmesi (İYUK m. 16/5).
- Karar tebliği, istinaf ve temyiz gönderimi, BİM kararlarının yedi gün içinde tebliğe çıkarılması (İYUK m. 45/6).
- Skill'ler: `/idari-kalem:dosya-tekemmul`, `/idari-kalem:idari-tebligat`, `/idari-kalem:karar-uygulama-takip`, `/idari-kalem:kanun-yolu-gonderme`, `/vergi-kalem:vergi-tebligat`, `/vergi-kalem:vergi-sure-takip`, `/vergi-kalem:karar-uygulama-iade`, `/vergi-kalem:dosya-tekemmul`.

## Hangi skill ve izleyici ne zaman

| Durum | Skill / izleyici |
|---|---|
| Dava açıldı | `/idari-hakim:ehliyet-husumet`, ivedi işte `/idari-hakim:ivedi-yargilama` |
| YD istemi | `/idari-hakim:yurutmenin-durdurulmasi` |
| Vergi davası | `/vergi-hakim:tarhiyat-degerlendirme`, `/vergi-hakim:vergi-ceza-degerlendirme`, `/vergi-hakim:odeme-emri-itiraz` |
| Karar | `/idari-hakim:idari-karar`, `/vergi-hakim:vergi-karar` |
| Takip | `kanun-yolu-kesinlesme-izleyici`, `makul-sure-izleyici`, `mevzuat-degisiklik-izleyici` |

## Veri hassasiyeti

- Kamu görevlisi disiplin ve sağlık raporu dosyalarında özel nitelikli veri (KVKK m. 6/1); vergi mahremiyeti gereken bilgiler maskeli kullanılır.
- Devletin güvenliği veya yüksek menfaatleri gerekçesiyle verilmeyen bilgi ve belgelere dayanılarak ileri sürülen savunmaya göre karar verilemez (İYUK m. 20/3).

## Mahkemeye özgü alanlar

- İdare mi vergi mi; daire numarası ve heyet yapısı: [DOLDUR]
- Bağlı bölge idare mahkemesi ve daireleri: [DOLDUR]
- Tek hâkim dosya oranı ve güncel parasal sınır: [DOLDUR]
- Yoğun dosya türleri (imar, kamu görevlisi, vergi cezası): [DOLDUR]

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): 2576 s.K. m. 5, 6, 7; 2575 s.K. m. 24; İYUK m. 2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 20, 20/A, 24, 27, 28, 31, 32, 45, 46, 61, ek m. 1; VUK m. 377, 378; 6183 s.K. m. 58; KVKK m. 6; 7201 s.K. m. 7/a.*
