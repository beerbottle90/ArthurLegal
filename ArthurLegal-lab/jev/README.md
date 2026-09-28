# ArthurLegal — JEV Edition (test)

İki soruyu deneyerek cevaplamak için kurulmuş bir çalışma alanı:

1. **TypeSafe'in [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) modeli
   ArthurLegal'a ne katar?** (Pilot B ve C)
2. **Jev'in yaptığını, veriyi cihazdan hiç çıkarmadan biz yapabilir miyiz?** (`yerel.py`)

İkinci sorunun cevabı: **evet.** Ölçülmüş hâli aşağıda.

---

## Neden mümkün — "Jev etkisi"nin ayrıştırılması

Jev bir dil modeli değildir. Metin üretmez; girdiyi alıp **tek geçişte tipli bir
karar** döndürür (`noul` = olasılıklı evet/hayır, `choice`, `score`). Değerli
özelliklerinin çoğu zekâdan değil mimari kısıttan gelir ve o kısıtlar bedavadır:

| Jev'in özelliği | Nereden geliyor | Yereldeki karşılığı |
|---|---|---|
| Tipli çıktı, şema garantisi | Metin üretmemesi | Sınıflandırıcı zaten etiket döndürür — bedava |
| Hız (iddia: 70–500 ms) | Otoregresif olmaması | **Ölçülen: 2.4 ms** — ağ turu da yok |
| Kalibre olasılık | RLCD eğitimi | Platt kalibrasyonu — ~20 satır |
| Ucuzluk ($0.042/Mtok) | Çıktının sıfır fiyatlı olması | **$0.00** — marjinal maliyet yok |
| Frontier zekâ | Devasa ön eğitim | ← tek gerçek fark |

Kalan tek fark **damıtmayla** kapatılır: Resmî Gazete başlıkları kamuya açıktır,
Opus onları çevrimdışı etiketler, yerel model o etiketlerden öğrenir. Gizlilik
sorunu hiçbir adımda doğmaz, çünkü öğretmene giden veri zaten herkese açıktır.

---

## Üç ayağa göre tasarım

**1. Doğru resmî kaynak.** Eğitim gövdesi resmigazete.gov.tr'nin kendi
fihristidir, ArthurLegalTR'nin kendi ayrıştırıcısıyla okunur (`hasat.py`
doğrudan `ArthurLegalTR/sources/resmi_gazete.py` çağırır). Arada kimse yoktur.

**2. Az hatalı sözel yorum.** Bu motor yorum **yapmaz**. Yorumu Opus yapar.
Buranın tek işi Opus'a neyin gideceğine karar vermektir. Bu yüzden ölçtüğümüz
sayı isabet değil **duyarlılıktır**: ilgili bir kalemi elemek pahalı bir
hatadır, ilgisiz bir kalemi Opus'a göndermek birkaç kuruştur.

**3. İnsan denetimi.** Her karar açıklanabilir:

```bash
python egit_yerel.py --neden 17     # bir kalemin kararını sürükleyen n-gramlar
```

### Omurga: kural katmanı yalnızca EKLER, asla ELEMEZ

```
p_son = max(p_kural, p_model)
```

Bir kural eşleşirse olasılık 1.0'a sabitlenir ve model bunu **veto edemez**.
Sonuç: sistemin duyarlılığı, modelin ne yaptığından bağımsız olarak kuralların
duyarlılığından asla düşük olamaz. Kanıtlanabilir bir taban. Kurallar
(`yerel.KURALLAR`) satır satır okunabilir ve her birinin gerekçesi yazılıdır.
`tests/test_yerel.py::test_kural_modeli_ezer` bu garantiyi kilitler.

---

## Ölçülen sonuçlar

Sınav kümesi: `fixtures/fihrist_altin.json` — 56 kalem, elle ve **gerekçeli**
etiketlenmiş, 17'si kasıtlı tuzak. Eğitime hiç girmedi.

| Tur | Eğitim gövdesi | enerji | rekabet | vergi | icra |
|---|---|---|---|---|---|
| 1 — 220 gün | 1703 kalem | 62.5% | 100% | 85.7% | 100% |
| 2 — 776 gün | **3581 kalem** | 62.5% | 100% | **100%** | 100% |

İsabet (precision) her iki turda ve dört konuda da **%100**.
**Hız: kalem başına 2.47 ms.** **Maliyet: $0.00.**
**Triyaj: 56 kalemin 42'si (%75) hiç Opus görmeden elendi.**

Gövdeyi 1755'ten 6146 başlığa çıkarmak ölçülebilir bir kazanç verdi: sınıf
başına pozitif sayısı ikiye katlandı (enerji 120→179, rekabet 30→37,
vergi 36→86, icra 31→52) ve **vergi duyarlılığı %85.7'den %100'e çıktı.**

### Kaçırılan üç kalem — hepsi kasıtlı tuzak

```
[enerji] p=0.005  #17 Hava Kalitesinin Korunması Amacıyla Katı Yakıtların Kontrolü Yönetmeliği
[enerji] p=0.080  #18 Isınmadan Kaynaklanan Hava Kirliliğinin Kontrolü Yönetmeliği
[enerji] p=0.001  #51 Belediyeler ... Vergi Gelirleri Payından ... Aydınlatma Gideri Kesintileri
```

İkinci turda #18'in olasılığı 0.007'den 0.080'e çıktı — on kat, ama eşiğin hâlâ
altında. Üçü de gövdede benzeri bulunmayan vakalar: "katı yakıt" kalıbı 776
günde bir kez geçiyor. Bunları kapatmak için kural eklemek **mümkün ama
yapılmadı**: sınav kümesine bakarak kural yazmak o sınavı anlamsızlaştırır —
TypeSafe'in kendi benchmark'larında eleştirdiğimiz kusurun aynısı olur.

### Dürüst olumsuz bulgu: öğrenilmiş katman kurallara az şey ekliyor

İlk turda ayrıştırma (`sadece kural` / `sadece model` / `birlikte`) şunu
gösterdi: model, kuralların üstüne **tam bir kalem** ekledi — *"Özelleştirme
İdaresi Başkanlığı ile İlgili Kararlar" → rekabet* (p=0.999). Hiçbir dar
kuralın ifade edemeyeceği anlamsal bir çağrışım ve modelin öğrenebildiğinin
kanıtı; ama sınıf başına 30–36 pozitifle fazlası beklenemezdi. İkinci turda
pozitifler ikiye katlandı ve vergi sınıfı tamamlandı. Bağlayıcı kısıt
**veridir**, mimari değil.

### Kural katmanının bir istisnası var

Kurum adına bakan kurallar (`EPDK`, `Rekabet Kurumu`, `Gelir İdaresi
Başkanlığı`, `TEİAŞ/EÜAŞ/BOTAŞ`), o kurumun **kendi iç idari** düzenlemelerinde
susar: "Gelir İdaresi Başkanlığı Personeli Görevde Yükselme Yönetmeliği" bir
vergi düzenlemesi değildir. İstisna kuralın ateşlenip ateşlenmeyeceğine karar
verir, modelin cevabını bastırmaz — "kural yalnız ekler" ilkesi korunur.
`test_ic_idare_*` ve `test_etiketler_kurallarla_celismez` bunu kilitler.

---

## Araştırma sonrası düzeltmeler (2026-09-20)

Kod ilk yazıldığında Jev'in API'si **belgelere bakılmadan tahmin edilmişti**.
GitHub, HuggingFace ekosistemi, HN launch tartışması (256 yorum), LiteLLM geçiş
belgeleri ve bağımsız kalibrasyon ölçümleri taranınca yedi hata çıktı. Üçü,
anahtar geldiği gün kodu çalışmaz hâle getirecek cinstendi.

### Kodu bozan üç hata

**1. Soru şeması yanlıştı.** Uydurulan `question`/`options` alanları gerçekte
`instructions`/`criteria`. Üstelik `choice`'ta `criteria` bir LİSTE değil,
{seçenek: açıklaması} HARİTASI. Uç 400 dönerdi.

**2. OpenRouter uç yolu uydurmaydı.** `openrouter.ai/typesafe/jev-1.13` **404
veriyor**; bağımsız incelemeler "no OpenRouter listing" diyor. Kaldırıldı.
Doğrulanmış yollar: doğrudan `api.typesafe.ai`, LiteLLM geçişi, Cloudflare
Workers AI. Artık `JEV_UC` ortam değişkeniyle seçiliyor, varsayılan tahmin yok.

**3. Bağlam sınırı bilinmiyordu.** State + sorular toplamı **32k token**
(belgeler; bir kaynak 64k toplam / 32k tek soru diyor — ihtiyatlı olan alındı).
Hız sınırı 250k token/sn ve 1200 istek/dk. İstek artık gönderilmeden önce
ölçülüyor; 56 kalemlik bir koşunun ortasında patlamaktansa baştan durur.

`tests/test_pilot.py` bu üçünü kilitleyen sözleşme testleri içeriyor — biri
doğrudan "uydurma OpenRouter yolu geri gelmesin" diye duruyor.

### Tasarımı bozan iki hata

**4. Sorular çok boyutluydu.** İlk enerji sorusu tek cümlede sekiz kavram
sayıyordu. TypeSafe belgeleri bunu açıkça yasaklıyor: *"birden çok yargıyı tek
soruya saklamayın"* — birinde yüksek, diğerinde düşük olan girdi ölçeğe
yerleştirilemez. Sorular atomik hâle getirildi.

**5. `criteria` hiç kullanılmamıştı.** Jev'in **state dışında dünya bilgisi
yoktur**; "enerji mevzuatı"nın Türk hukukunda neyi kapsadığını bilmesini ummak
yerine yazmak gerekir. Dört soruya da true/false açıklamaları eklendi — ve tam
da bizim tuzaklarımız oraya yazıldı ("İthalatta haksız rekabetin önlenmesi bir
ANTİDAMPİNG düzenlemesidir, rekabet hukuku DEĞİLDİR").

### Ölçümü bozan iki hata

**6. Eşikler yanlış yöndeydi.** Bağımsız kalibrasyon çalışmaları
([huncho](https://github.com/edgardcham/huncho),
[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration),
[jev-exploration](https://github.com/SamuelSacco/jev-exploration/issues/10))
900 girdide tip başına sapmanın **yönünü** ölçtü: choice ve score **aşırı
güvenli** (T 3.3–3.4), boolean/noul ise **güvensiz** (T 0.66). Biz yalnız noul
kullanıyoruz; bildirilen olasılıklar olmaları gerekenden 0.5'e daha yakın
demek. Yüksek bir alt eşik gerçek pozitifleri eler. Bantlar 0.30/0.70'ten
**0.20/0.60**'a çekildi. Doğrusu anahtar gelince kendi altın kümemizde
güvenilirlik diyagramı çıkarmaktır; bu değerler o ölçüme kadar geçerli bir
varsayımdır.

**7. "Çıktı tokeni yok" yanlıştı.** Yanıttaki `usage` alanı `output_tokens`
sayıyor (örnekte 48). Çıktı **sıfır fiyatlı**, yok değil. Maliyet hesabı
değişmiyor ama cümle yanlıştı.

### Düzeltilmeyen ama bilinmesi gereken dört şey

| Bulgu | Bizim için anlamı |
|---|---|
| Jev 50+ dilde ön eğitimli; **Türkçe adı geçmiyor** (İspanyolca, Almanca, Fransızca, Japonca, Mandarin sayılıyor) | Türk hukuku başlıklarında başarımı **bilinmiyor**. Anahtar gelince ölçülecek ilk şey bu olmalı. |
| Ölçülen bir toplulukta **Jev yeniden sıralama, vektör erişimini geçemedi** (33 bin kayıt) | "İçtihat arama sonuçlarını Jev ile sırala" fikri zayıf. Jev keşif sıralamasında değil, **doğrulamada** iyi. |
| Bağımsız doğrulama yok: mimari makalesi yok, kamuya açık liderlik tablosu yok | Satıcı rakamlarına dayanan hiçbir cümle kurulmamalı. |
| Projeler gecikme oynaklığı için devre kesici/son tarih mantığı kuruyor | 70–500 ms sabit değil. Üretimde zaman aşımı şart. |

### Değişmeyen şey

Bu düzeltmelerin hiçbiri **yerel motoru** etkilemedi: `yerel.py` Jev'in
API'sini kullanmıyor, yalnız aynı çağrı arayüzünü taşıyor. Ölçülen 2.47 ms,
$0.00 ve tutulan altın kümedeki duyarlılıklar aynen geçerli. Bu, arayüzü
sözleşmeye bağlamanın ve bağımlılığı tek dosyada toplamanın karşılığı.

---

## İkinci tur: GitHub, HuggingFace ve bağımsız ölçümler (2026-09-20)

Birinci tur ağırlıkla belge ve haber kaynağıydı. İkinci tur doğrudan kodun
içine girdi: `gh` ile GitHub issue gövdeleri, bağımsız ölçüm depolarının
README'leri, HuggingFace reprodüksiyon izleyicisi. **Altı yeni bulgu**, biri
birinci turdaki kendi düzeltmemi düzeltiyor.

### 0. Düzeltmenin düzeltmesi — Jev OpenRouter'da VAR

Birinci turda "OpenRouter uç yolu uydurmaydı, kaldırıldı" demiştim. Yarısı
doğruydu: yol (`/api/v1/systemone`) gerçekten uydurmaydı. Ama "Jev
OpenRouter'da yok" sonucu **yanlıştı**. Jev OpenRouter'da ayrı bir
**Decisions API**'sindedir:

```
POST https://openrouter.ai/api/alpha/decisions
{ model: "typesafe/jev-1.13", state, questions } -> { answers, usage }
```

Sohbet tamamlama SDK'ları çalışmaz ve model `GET /api/v1/models` listesinde
**görünmez** — "no OpenRouter listing" iddiası buradan doğmuş. Destek geri
eklendi, doğru uçla. Vercel Gateway'de ayrı bir tuzak var: `typesafe-ai/jev`
çalışıyor, `typesafe-ai/jev-latest` "Model not found" dönüyor.

### 1. Toplu istek kaliteyi bozuyor — neredeyse ters yöne gidiyorduk

[MinusPod](https://github.com/ttlequals0/MinusPod) kimliği doğrulanmış bir
koşuda "tek istekte yüzlerce soru, paylaşılan state" kalıbını kullanmış ve iyi
sonuç almış. Tam bunu benimsemek üzereydim: bir günün fihristini state yapıp
80 kalem x 4 soruyu tek çağrıda sormak. Çok daha ucuz olurdu.

Ama [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) bunu
ölçmüş: aynı satırlar 40'lık toplu isteklerle gönderildiğinde **sıralama
kapısını geçemiyor** (ters çevirme 0.171 / eşik 0.15); tek tek gönderildiğinde
geçiyor. Yani toplu istek, sonucu istek şeklinin kendisi üzerinden değiştiriyor.

Pilot bilerek **kalem başına bir çağrı** yapıyor ve
`test_bir_kalem_bir_cagri_sozlesmesi` bunu kilitliyor.

### 2. En önemli bulgu: dağılım DIŞINDA kendinden emin şekilde yanlış

[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration),
4.621 çağrıyla şunu ölçmüş:

| Küme | Doğruluk | ECE | Yeniden uydurulan T |
|---|---|---|---|
| OpenBookQA (muhtemelen eğitimde) | %94.2 | 0.024 | 0.96 |
| CommonsenseQA (muhtemelen eğitimde) | %88.1 | 0.032 | 1.35 |
| Sentetik destek talepleri (**görmemiş**) | — | kendinden emin şekilde yanlış | — |

Yani **iyi kalibrasyon rakamları alan içi**. Modelin görmediği, etiketi metinde
olmayan bir kuralda (politika) bilmediği yeri bilmiyor. Türkçe Resmî Gazete
başlıkları Jev için tam olarak bu durumdadır.

Aynı deponun tavsiyesi bizim çerçevemizi değiştirdi: *"çıktıyı monoton bir
SKOR gibi ele alın, olasılık gibi değil, ve yerelde kalibre edin."*

### 3. Soru metnini değiştirmek cevabı bantlardan fazla oynatıyor

Zor bir erişim ölçütünde (Amazon ESCI, 306 insan derecelendirmeli çift) düz bir
başka söyleyiş cevabı **ortalama 0.164** oynatıyor. Bizim bantlar arası mesafe
0.40. Yani Türkçe soru metnimizin yeniden yazılması, ölçtüğümüz farkın yarısı
kadar kayma yaratabilir. Aynı ölçümde altı kapıdan dördü kalıyor
(`jev_bool` ECE 0.242, ters çevirme 0.255).

### 4. Olasılıklar 0.01'e yuvarlı ve sık sık tam 0 / tam 1

`rounding: {probabilityDecimals: 2}`. Ölçülmüş: 360 satır yalnız **45 ayrı
değer** üretmiş, **53 satır 0.99'da eşitlenmiş**. Tam 0 dönen bir cevap
sıcaklık ölçeklemesiyle **onarılamaz**. Eşikler bu çözünürlükten ince olamaz;
`test_olasilik_cozunurlugu_belgelenmis` bunu kilitliyor.

### 5. `confidence` alanına eşik kurmayın

Ayrı dönen `confidence` istatistiği, ölçülen hiçbir kümede azami olasılıktan
iyi çıkmamış, bazılarında çok daha kötü (sentetik kümede ECE 0.18). Kodumuz
zaten kullanmıyordu; artık test de var.

### 6. Bağımsız ölçümler birbirini tutmuyor — ve bu bilgi

| Ölçüm | Sonuç |
|---|---|
| [MinusPod](https://github.com/ttlequals0/MinusPod) reklam tespiti, 14 bölüm | Jev F1 0.929 / **isabet 0.979** / duyarlılık 0.893; Haiku 4.5 F1 0.920 / 0.900 / **0.946**. Maliyetin %1'inden azı, p50 ~0.1 sn. |
| [jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench), 2.000 e-posta | Jev **%62.6**, ECE 0.154; Claude Haiku 4.5 ECE 0.097. Jev belirgin şekilde geride. |
| [jev-spam-eval](https://github.com/bitnovus/jev-spam-eval), ~9.9 bin e-posta | %98.6 doğruluk, bağlam zenginleştirmeyle. |
| [gbrain](https://github.com/garrytan/gbrain) yeniden sıralama | Gecikmede Voyage 7438 ms / Jev 1582 ms. |

Aynı model bir işte Haiku'yu geçiyor, başka bir işte %62'ye düşüyor. **Tek bir
"Jev iyidir/kötüdür" cümlesi kurulamaz** — işe özgü ölçmek şart.

Bizim için en can alıcı satır MinusPod'unki: Jev **isabete meyilli**
(P 0.979 / R 0.893). Bizim ihtiyacımız tam tersi: duyarlılık. Jev'in doğal
eğilimi bizim istediğimiz yönde değil.

### Türkçe için tek olumlu iz

Aynı OOD çalışmasında "müşteri kızgın mı" sorusunda %91.7 başarım, **içinde
Korece metin bulunan talepler dâhil**. İngilizce dışı metinde tamamen
çuvallamadığına dair dolaylı bir kanıt — ama Türkçe hâlâ ölçülmemiş.

---

## GERÇEK ÖLÇÜM — anahtar geldi, Jev koşturuldu (2026-09-20)

Tutulan 56 kalemlik altın küme, gerçek `api.typesafe.ai` ucuna karşı.
Ham kayıt: [`olcum/jev_altin_2026-09-20.json`](olcum/jev_altin_2026-09-20.json).
Model `jev-1.13.0` olarak çözüldü.

### Önce: sözleşme tuttu ve **Türkçe çalışıyor**

İlk çağrı HTTP 200. Bilinen bir pozitifte (EPDK kurul kararı):

```
enerji 0.97   rekabet 0.06   vergi 0.04   icra 0.02      (altın: 1/0/0/0)
```

Bu, projenin en büyük açık sorusunu kapatıyor: Jev'in adı geçen 50+ dil
listesinde Türkçe yoktu. **Türk hukuku başlıklarını anlıyor.**

### Üç motorun yan yana ölçümü

| Konu | JEV | YEREL | **BİRLEŞİK** |
|---|---|---|---|
| | duyarlılık / isabet | duyarlılık / isabet | duyarlılık / isabet |
| enerji | 88% / 88% | 62% / 100% | **88% / 88%** |
| rekabet | 100% / 100% | 100% / 100% | **100% / 100%** |
| vergi | 100% / 100% | 100% / 100% | **100% / 100%** |
| icra | **50% / 20%** | 100% / 100% | **100% / 33%** |
| **kaçan** | 2 | 3 | **1** |
| triyaj | %64 | %73 | %62 |

### Asıl bulgu: ikisi farklı yerlerde hata yapıyor

```
JEV yakaladı, YEREL kaçırdı
  [enerji] jev=0.49 yerel=0.00  Katı Yakıtların Kontrolü Yönetmeliği
  [enerji] jev=0.28 yerel=0.08  Isınmadan Kaynaklanan Hava Kirliliği Yönetmeliği

YEREL yakaladı, JEV kaçırdı
  [icra]   jev=0.18 yerel=1.00  BM Güvenlik Konseyi ... Malvarlığının Dondurulması
```

Sebepler simetrik:

* **Jev'in dünya bilgisi var.** "Katı yakıt"ın kömür demek olduğunu biliyor.
  Yerel modelin 776 günlük gövdesinde bu kalıptan **bir tane** var — öğrenemez.
  Bunlar tam da sekiz ay boyunca "kapatılamayan tuzaklar" diye yazdığımız
  kalemlerdi.
* **Yerelin alan kuralları var.** "Malvarlığının dondurulması"nın cebrî icra
  olduğunu bir kural söylüyor ve o kural veto edilemiyor. Jev bunu Türk hukuku
  bağlamında görmediği için 0.18 diyor.

Birleşik motor (`birlesik.py`, yine `max` ile) kaçanı **3'ten 1'e** indiriyor.
Bedeli triyajın %73'ten %62'ye düşmesi — Opus'a 15 yerine 21 kalem gidiyor.
Bir kaçağı altı fazladan okumayla değiştirmek bu işte doğru takastır.

```bash
python pilot_b_fihrist.py --birlesik    # ölçülmüş en iyi duyarlılık
```

### Satıcı iddialarıyla ölçülen arasındaki fark

| İddia | Ölçülen |
|---|---|
| 70–500 ms | **medyan 774 ms** (ilk çağrı 893 ms) — 1.5–11 kat yavaş |
| Ucuz | **$0.002475 / 56 kalem** → 40 kalem/gün × 250 gün ≈ **$0.44/yıl**. İddia doğru. |
| Kalibre olasılık | 0.01'e yuvarlı, belgelendiği gibi |

Gecikme farkının bir kısmı bizden: kalem başına 1.033 girdi tokeni gönderiyoruz
ve bunun çoğu **her istekte tekrarlanan `criteria` metni**. Başlığın kendisi
~40 token. Kısaltmak hem hızlandırır hem ucuzlatır — ama bağımsız ölçümler
soru metnini değiştirmenin cevabı 0.164 oynattığını söylüyor, yani kısaltma
ölçümü tazelemeden yapılmamalı.

### Jev'in zayıf noktası bizde de çıktı

`icra` konusunda isabet **%20** — geçirdiği 5 kalemin 4'ü yanlış pozitif. Bu,
bağımsız ölçümlerdeki "dağılım dışında kendinden emin şekilde yanlış"
bulgusuyla birebir örtüşüyor: Türk icra-iflas hukuku Jev için görülmemiş bir
alan. Kural katmanı olmasaydı bu konu kullanılamazdı.

---

## KALİBRASYON — eşikler artık tahmin değil, ölçüm (2026-09-20)

56 kalem eşik seçmeye yetmez. Etiketli **938 küme temsilcisinde** Jev
koşturuldu: 0 hata, 96 saniye (8 eşzamanlı), **~$0.04**. Ham kayıt:
[`olcum/jev_kalibrasyon_ham.jsonl`](olcum/jev_kalibrasyon_ham.jsonl).

> **Ölçümün sınırı:** bu kümenin etiketleri altın değil, Opus damıtmasıdır.
> Ölçülen şey "Jev doğru mu" değil, **"Jev Opus ile ne kadar örtüşüyor"dur.**
> Eşik seçmek için gereken şey mutlak doğruluk değil, olasılık dağılımının
> ŞEKLİ olduğu için yine de işe yarar. Gerçek altın küme (56 kalem) bu koşuya
> girmedi; temiz kaldı.

### Bağımsız bulguyu Türkçe hukuk metninde doğruladık

| Konu | pozitif | ECE | gürültü tabanı | oran | **T** | yön |
|---|---|---|---|---|---|---|
| enerji | 101/938 | 0.048 | 0.021 | 2.3× | **0.50** | güvensiz |
| rekabet | 10/938 | 0.040 | 0.009 | 4.2× | **0.46** | güvensiz |
| vergi | 43/938 | 0.035 | 0.013 | 2.7× | **0.63** | güvensiz |
| icra | 31/938 | 0.030 | 0.011 | 2.8× | **0.65** | güvensiz |

**Dört konuda da T < 1.** Bu, bağımsız depoların İngilizce verilerde boolean
için bulduğu yönü (T ≈ 0.66) Türkçe hukuk metninde bağımsız olarak üretiyor.
ECE gürültü tabanının 2.7–4.2 katı — yani sapma örnekleme gürültüsü değil,
gerçek. Jev'in `noul` olasılıkları olmaları gerekenden **0.5'e daha yakın**.

### Eşik süpürmesi — Jev tek başına

```
eşik    enerji  rekabet   vergi    icra   elenen
0.05      100%     100%     98%     97%     48%
0.10      100%     100%     95%     90%     67%
0.20       99%     100%     86%     84%     77%   <- eski varsayım
0.50       95%      50%     67%     48%     83%
```

Eski 0.20 varsayımı vergi ve icra pozitiflerinin **altıda birini** eliyordu.
Jev tek başına kullanılacaksa doğru bant **0.05**.

### Ama birleşik motorda durum tersine dönüyor — bu bulgunun en değerlisi

Altın kümede birleşik motor **her eşikte aynı duyarlılığı** veriyor
(87.5 / 100 / 100 / 100, tek kaçak #51), ama triyaj çöküyor:

| alt bant | duyarlılık | triyaj | enerji isabeti |
|---|---|---|---|
| 0.05 | aynı | %29 | %33 |
| 0.10 | aynı | %57 | %70 |
| 0.15 | aynı | %61 | %78 |
| **0.20** | aynı | **%62** | **%88** |

Sebebi: **kural katmanı gerçek pozitifleri zaten 1.0'a sabitliyor.** Jev'in
bandını düşürmek duyarlılığa hiçbir şey eklemiyor, yalnız yanlış pozitif
ekliyor.

Yani doğru eşik, elinizde **kural tabanı olup olmamasına** göre değişir:
tabanı olan yüksek eşik kullanabilir, olmayan düşüğe inmek zorundadır. Aylar
önce "kural yalnız ekler, asla elemez" diye koyduğumuz ilke burada ikinci kez
karşılığını verdi — önce Jev'in %20'lik icra isabetini kurtararak, şimdi de
eşiği yükseltmemize izin vererek.

### Gecikme, geniş ölçekte

938 çağrı: **medyan 823 ms, p90 929 ms, azami 1758 ms.** İddia 70–500 ms.
Eşzamanlılık 8 ile etkin hız kalem başına ~100 ms; tek tek gönderirken ~820 ms.

## MEVZUATA AKTARIM — ayrıca ölçüldü, kopyalanmadı (2026-09-20)

Model Resmî Gazete fihristinde eğitildi. `tr_mevzuat_ara` aynı mevzuatı başka biçimde döndürür
(BÜYÜK HARF, bölüm adı yok, başlık içinde satır sonları), bu yüzden RG'deki duyarlılık oraya
taşınmadı; `olc_mevzuat.py` 187 Bedesten başlığında ayrıca ölçtü.

| dilim | ne ölçer | sonuç (eşik 0,20) |
|---|---|---|
| eğitimde görülmüş 127 başlık | yalnız Bedesten biçimine aktarım | 26/26 pozitif, 3 yanlış pozitif |
| görülmemiş 60 başlık | genelleme | vergi 4/4 · icra 2/2 · **enerji 0/3** · 2 yanlış pozitif |
| aynı, torba kanun geçişi kapalı | başlığın tek başına yettiği yer | vergi 3/4 · icra 1/2 |

**İki dilim ayrı raporlanır, çünkü aynı şeyi ölçmezler.** 187 başlığın 127'si modelin eğitim
örneği çıktı: RG fihristi ile Bedesten aynı başlıkları taşıyor. Tek sayı olarak "29/32" demek
mümkündü ve yanıltıcı olurdu. `tests/test_mevzuat.py` sayıları değil bu dürüstlüğü kilitler:
görülmemiş dilime eğitim kalemi sızamaz, RG altın kümesiyle çakışan beş kalem aynı etiketi
taşır, adı okunamayan torba kanun asla elenmez ve uçta duyurulan sayılar bu ölçümün çıktısıyla
aynıdır (`test_mcp_kunyesi_olcumle_ayni_sayilari_tasir`).

**Torba kanunlar.** "Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanun" hiçbir başlık tabanlı
yöntemin göremeyeceği bir şeydir: 7531 sayılı Kanun İİK ve HMK'yı değiştirir. Etiketler metin
okunarak verildi; uçtaki `tr_mevzuat_ara(konu=…)` değiştirilen kanun adlarını okur. Adları
okunamayan torba kanun elenmez. "Kural yalnız ekler" ilkesinin mevzuattaki karşılığı budur.

**Enerji 0/3.** İkisi RG altın kümesinin bilinen tuzağı (katı yakıt, aydınlatma gideri), biri
yeni (Rüzgâr Gücü İzleme ve Tahmin Merkezine Bağlantı Yönetmeliği). Kural eklenerek
kapatılmadı. Bu sayı uçta şemada, her yanıtta, `status` çıktısında ve ana paketlerin sistem
talimatında yazıyor: zayıf konu gizlenmez.

```bash
python olc_mevzuat.py                   # rapor
python olc_mevzuat.py --torbasiz        # yalnız başlık
python canli_dogrula.py                 # dağıtım sonrası: canlı uç bu ölçülen şeyi mi koşturuyor?
```

## Kurulum ve çalıştırma

Bağımlılık: Python 3.11 + **numpy**. Başka hiçbir şey. Ayrı süreç, sunucu veya
pencere yoktur — `yerel.py` bir modüldür, `import yerel` ile ArthurLegalTR veya
uyap-mcp içine gömülür.

```bash
python egit_yerel.py                    # eğit + tutulan altın kümede sına
python pilot_b_fihrist.py --yerel       # yerel motorla triyaj raporu
python pilot_b_fihrist.py --sahte       # Jev (çevrimdışı taklit) ile aynı rapor
python pilot_b_fihrist.py --birlesik    # yerel + Jev (en iyi duyarlılık)
python kalibrasyon.py                   # ölçülmüş kalibrasyon raporu
python -m pytest tests/ -q              # 120 test
```

Jev'i gerçekten denemek için `.env.ornek` → `.env`, tek satır anahtar.
Anahtar yoksa pilotlar `SahteJev`'e düşer ve hata vermez.

---

## Dosyalar

```
kalibrasyon.py           Jev'i geniş dilimde koştur + güvenilirlik/ECE/eşik raporu
birlesik.py              BİRLEŞİK MOTOR — yerel + Jev, ikisinin azamisi
yerel.py                 YEREL MOTOR — kural katmanı + char n-gram lojistik regresyon
jev.py                   Jev istemcisi (gerçek uç + çevrimdışı sahte), aynı arayüz
egit_yerel.py            eğitim + tutulan altın kümede sınav + --neden açıklaması
pilot_b_fihrist.py       Resmî Gazete ön eleme raporu (--yerel | --sahte)
pilot_c_maske.py         maskeleme denetçisi (gerileme testi, üretim bileşeni DEĞİL)

hasat.py                 Resmî Gazete fihrist hasadı (ArthurLegalTR'nin kendi kodunu çağırır)
etiket_hazirla.py        tekilleştirme, altın kümeyi ayırma, yapısal sıfırlar
etiket_kumele.py         şablon kümeleme (aynı kalıbı bir kez etiketlemek için)
etiket_sec.py            kararsız/çelişkili kalemleri seçer + rastgele kalibrasyon dilimi
etiket_yaz_kume.py       etiketleri başlık anahtarlı depoya yazar
etiket_tasima.py         küme-indeksli -> başlık-anahtarlı göç (tek seferlik)

fixtures/rg_govde.json         776 gün ham fihrist
fixtures/fihrist_altin.json    56 kalemlik sınav kümesi, gerekçeli
fixtures/etiketler_kalem.json  damıtma etiketleri (başlık anahtarlı)
fixtures/maske_sentetik.json   14 uydurma metin (Pilot C)
model/rg_triyaj.{json,npz}     eğitilmiş model (~0.5 MB)
tests/                         120 test
```

---

## Güvenlik duruşu

Bu depoda **hiçbir müvekkil verisi yoktur ve olamaz.**

| | Veri | Neden güvenli |
|---|---|---|
| Gövde | Resmî Gazete fihristi | Kamuya açık, herkesin okuyabildiği metin |
| Pilot C | Uydurma dava metinleri | Kişiler, şirketler, numaralar tamamen kurgu |
| Yerel motor | — | Hiçbir şey cihazdan çıkmaz |

`tests/test_yerel.py::test_yerel_ag_kullanmaz` bunu kod düzeyinde kilitler:
`yerel.py` hiçbir ağ modülünü içe aktaramaz. Biri ileride "küçük bir telemetri"
eklemek isterse test düşer.

Pilot C'nin fixture'ı her çalıştırmada yeniden doğrulanır: her kalem
`"sentetik": true` taşımak zorundadır, sağlaması **tutan** bir TC kimlik
numarası veya sıfırlardan oluşmayan bir IBAN görülürse çalışma durur.

---

## Pilot C — bulduğu şey bir sayı değil, bir çelişki

> **Jev canlı bir maske guardrail'i olamaz.** Kontrol, maskeden geçmiş metni
> dışarı göndermeyi gerektirir. Maske çalıştıysa kontrole gerek yoktur; maske
> kaçırdıysa **tam da kaçırdığı veriyi** göndermiş olursunuz. Kontrol yalnızca
> işe yaramadığı durumda zararsızdır.

Bu yüzden Pilot C bir üretim bileşeni değil, `maske.py` değiştiğinde uydurma
veriyle koşulacak bir **gerileme testi**dir.

Aynı muhakeme yerel motor için geçerli değildir: orada metin zaten hiçbir yere
gitmez. PII tespiti de ML-önce olmamalıdır — TCKN/IBAN/telefon regex + sağlama
ile deterministik çözülür, ad tespiti Arthur Mask kasasının işidir.

---

## Bulgular

**1. Rekabet filtresi Resmî Gazete'de çalışmaz.** 50 gün tarandı
(1 Ağu – 19 Eyl 2026): "Rekabet Kurulu" için **0 sonuç**. Rekabet Kurumu
kararları RG'de değil rekabet.gov.tr'de yayımlanır. Doğru uç
`tr_kurum_karari_ara` (kurum=`rekabet`).

**2. "İthalatta Haksız Rekabetin Önlenmesi" rekabet hukuku değildir.** Gövdede
en büyük küme bu (96 kalem) ve antidamping mevzuatıdır. Kelime eşleşmesine
dayanan her rekabet filtresi buraya düşer. `test_kural_eslesmeleri_negatif`
bunu kilitler.

**3. Az veride Platt kalibrasyonu sıralamayı ters çevirebiliyor.** Negatif eğim
öğrenildiğinde model bütün cevapları sessizce tersine çeviriyordu. `_platt`
artık negatif eğimi reddedip kimliğe düşüyor
(`test_platt_negatif_egimi_reddeder`).

---

## Sıradaki adım

Gövde 6146 başlığa çıkarıldı. Etiketleme `etiket_sec.py` ile **belirsizlik
örneklemesi** yaparak sürüyor: modelin kararsız kaldığı ve kuralla çeliştiği
kalemler öncelikli, artı kalibrasyonu bozmamak için düz rastgele bir dilim.
Hedef, sınıf başına pozitif sayısını 30'lardan birkaç yüze çıkarıp öğrenilmiş
katmanın kuralların üstüne gerçekten bir şey ekleyip eklemediğini ölçmek.
Sınav kümesi bu süre boyunca **dokunulmadan** kalır.
