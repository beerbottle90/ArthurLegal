---
name: employment-legal-termination-review
description: >
  Fesih incelemesi (Türk iş hukuku) — fesih türünü (geçerli sebep İş K. m. 18,
  haklı sebep m. 25, süreli fesih m. 17, ikale) belirler, yüksek risk
  bayraklarını tarar, süreleri (haklı fesihte 6 iş günü, işe iadede 1 ay
  arabuluculuk) kontrol eder; ihbar-kıdem-izin ücreti kalemlerini, ibraname
  (TBK m. 420) ve arabuluculuk anlaşması yolunu ve fesih günü kontrol listesini
  çıkarır. "Bu işçiyi çıkarabilir miyiz", "fesih incelemesi", "işten çıkarma",
  "işe iade riski" denince ya da bir fesih senaryosu anlatıldığında kullan.
argument-hint: "[feshi anlatın ya da belgeleri ekleyin]"
---

# /termination-review — Fesih İncelemesi

Çoğu fesih sorunsuzdur; birkaçı hazır bir işe iade ya da alacak davasıdır. Bu skill, karar kesinleşmeden önce ikinci türü yakalar. Kural ezberden söylenmez: atıf yapılan her madde `tr_mevzuat_madde_getir` ile çekilir; değişen tutarlar (kıdem tavanı, asgari ücret) her incelemede teyit edilir.

## ⏰ ÖN-KONTROL — Süre (her çalıştırmada)

| Durum | Süre | Dayanak |
|---|---|---|
| İşveren ahlak ve iyiniyet kurallarına aykırılık nedeniyle derhal fesih | Öğrenmeden itibaren **6 iş günü**; her hâlde fiilden itibaren **1 yıl** (işçi maddi çıkar sağladıysa 1 yıl uygulanmaz) | 4857 m. 26 |
| İşçi işe iade isteyecek | Fesih bildiriminin tebliğinden itibaren **1 ay** içinde arabulucuya başvuru; son tutanaktan itibaren **2 hafta** içinde dava | 4857 m. 20/1 |
| Toplu işçi çıkarma | Sendika temsilcileri, bölge müdürlüğü ve İŞKUR'a en az **30 gün** önce yazılı bildirim; fesihler bölge müdürlüğüne bildirimden 30 gün sonra hüküm doğurur | 4857 m. 29 |
| SGK işten ayrılış bildirimi | Sözleşmenin sona ermesinden itibaren en geç **10 gün** | 5510 m. 9 |
| İbraname | Sözleşmenin sona ermesinden **en az 1 ay sonra** | TBK m. 420/2 |

6 iş günü süresinde ≤ 2 gün kaldı → 🔴 ACİL. "Öğrenme"nin feshe yetkili kişi/organın öğrenmesi olarak arandığı yerleşik uygulamadır — içtihadı kontrol et. Süre kaçtıysa haklı fesih yerine geçerli sebep + bildirim süreli fesih yolunu değerlendir.

## Destination check

- **Müvekkile / İK'ya fesih notu** → profilin `## Outputs` bölümündeki işveren tarafı fesih notu başlığı ("AVUKATLIK K. m. 36 – DAHİLİ"; sır saklama: Av. K. m. 36)
- **Yöneticinin fesih görüşmesi konuşma metni** → hukuki değerlendirme ve risk notları çıkarılır
- **İşçiye tebliğ edilecek fesih bildirimi** → "TASLAK"; avukat onayından sonra
- **Arabulucuya / karşı tarafa gidecek metin** → iç hesap, risk puanı ve strateji çıkarılır

## ADIM 0 — Taraf ve çıkar çatışması

- [Müvekkil] işveren mi, işçi mi? Aynı işte menfaati zıt tarafa avukatlık etmiş avukat işi reddetmek zorundadır (Av. K. m. 38/1-b). Çatışma kontrolü yapılmadan devam etme (varsa `/arthurlegal:firm-operations-conflict-check`).
- İşveren tarafı → aşağıdaki akış. İşçi tarafı → en sondaki **İşçi tarafı varyantı**.

## Bağlamı yükle

`firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → fesih tetikleyicileri, yüksek risk bayrakları, ayrılış paketi pratiği, eskalasyon matrisi, `## Outputs` ve `## Who's using this`.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:employment-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Temel olgular

| Soru | Neden önemli |
|---|---|
| İşçi (ad ya da unvan takma adı), işin yapıldığı yer | Yurt dışındaysa uygulanacak hukuk (aşağıda) |
| İşyerindeki ve aynı işkolundaki işyerlerinde toplam işçi sayısı | 30 eşiği iş güvencesi için toplam sayıyla belirlenir (m. 18/1, m. 18/4) |
| Kıdem (işe giriş tarihi) | 6 ay eşiği; ihbar süresi; kıdem tazminatı |
| Sözleşme türü | Belirsiz / belirli süreli (m. 11); iş güvencesi belirsiz süreliye uygulanır |
| Pozisyon | İşletmenin bütününü sevk ve idare eden işveren vekili mi (m. 18 son fıkra) |
| Fesih nedeni | Yeterlilik / davranış / işletme gerekleri / haklı neden / anlaşma |
| Sendika üyeliği, temsilcilik, TİS | m. 18/3-a,b; TİS'teki disiplin usulü |
| Aynı dönemde başka çıkarma | Toplu çıkarma eşiği (m. 29/2) |
| Planlanan tarih | Süreler, izin ve rapor çakışması |

### 2. Fesih türünü belirle

- **Geçerli sebep (m. 18):** işçinin yeterliliği, davranışı ya da işletme/işyeri/iş gerekleri. Bildirim yazılı, sebep açık ve kesin (m. 19/1); davranış ya da verim nedeniyle fesihte önce savunma alınır (m. 19/2; m. 25/II hâlleri hariç). Savunma şartının iş güvencesi dışındaki işçiye de uygulanıp uygulanmadığı **tartışmalı — içtihadı kontrol et**; şüphede savunma al. İspat yükü işverendedir (m. 20/2). Bildirim süresine uyulur ya da ücreti peşin ödenir (m. 17).
- **Haklı sebep (m. 25):** I sağlık, II ahlak ve iyiniyet kurallarına aykırılık, III zorlayıcı sebep, IV gözaltı/tutukluluğun bildirim süresini aşması. II için m. 26 süresi işler.
- **İş güvencesi dışındaki işçinin süreli feshi (m. 17):** fesih hakkı kötüye kullanılırsa bildirim süresinin üç katı tutarında tazminat (m. 17/6).
- **Esaslı değişikliğin reddi üzerine fesih (m. 22/1):** geçerli nedenin yazılı açıklanması ve bildirim süresi şart.
- **İkale (bozma sözleşmesi):** kanunda düzenlenmemiş, karşılıklı anlaşmaya dayanan uygulama kavramı. İşveren önerdiyse işçiye "makul yarar" sağlanması ve irade sakatlığı denetimi yerleşik uygulamadır — **tartışmalı, içtihadı kontrol et** (sorgu aşağıda).
- **İş K. kapsamı dışındaki işçi** (m. 4 istisnaları, ör. ev hizmetleri): TBK hükümleri; ör. haklı sebep olmaksızın derhal fesihte TBK m. 438.

### 3. Yüksek risk bayrakları (en önemli adım)

Eklenti ayarındaki bayrakların hepsini işaretle. Varsayılan set:

| Bayrak | Neden riskli | Kontrol | Dayanak |
|---|---|---|---|
| Yakın tarihli şikâyet / resmî başvuru | Geçerli sebep sayılmaz; misilleme algısı | İşveren aleyhine idari/adli makama başvurdu ya da sürece katıldı mı? | m. 18/3-c |
| Sendika üyeliği / temsilcilik | Geçerli sebep sayılmaz; sendikal tazminat | Üyelik, faaliyet → 6356 s.K. ilgili maddesini çek | m. 18/3-a,b |
| Gebelik, doğum, aile yükümlülükleri, din, cinsiyet, engellilik vb. | Geçerli sebep sayılmaz; 4 aya kadar ücret tutarında ayrımcılık tazminatı + yoksun kalınan haklar; ispat yükü kayar | Yakın zamanda bildirilen gebelik, izin talebi, sağlık durumu | m. 5/6-7; m. 18/3-d; 6701 m. 3, 6 |
| Analık izni ya da raporlu bekleme süresinde devamsızlık | Geçerli sebep sayılmaz; hastalıkta bildirimsiz fesih hakkı ancak bildirim süresi + 6 hafta aşılınca doğar | Rapor tarihleri, kıdem → `/arthurlegal:employment-legal-leave-tracker` | m. 18/3-e,f; m. 25/I; m. 74 |
| Savunma alınmadı | Davranış/verim nedenli fesih yapılamaz | Yazılı davet, makul süre, tutanak | m. 19/2 |
| Sebep yazılı ve açık değil | Geçersizlik | Bildirim metni | m. 19/1 |
| Zayıf belge ("neden şimdi?") | İspat yükü işverende | Uyarılar, performans kayıtları; yakın tarihli olumlu değerlendirme, prim, terfi çelişkisi | m. 20/2 |
| Emsal sorunu | Eşit davranma ihlali | Aynı davranışı yapan başkası çıkarılmıyor mu? | m. 5 |
| İç prosedür sözü | Sözleşmesel usul ihlali | TİS, personel yönetmeliği, iş sözleşmesindeki disiplin aşamaları izlendi mi? | yerleşik uygulama — kontrol et |
| Ödenmemiş ücret / fazla çalışma | İşçinin haklı fesih hakkı ve alacak davası | Bordro, puantaj → `/arthurlegal:employment-legal-wage-hour-qa` | m. 24/II-e; m. 34 |
| Mobbing / taciz iddiası | TBK m. 417 sorumluluğu; basın riski | Açık şikâyet var mı → profil eskalasyonu | TBK m. 417 |
| İşletmesel karar | Feshin son çare olması, tutarlılık, keyfilik denetimi | İşletme kararı belgelendi mi, kadro gerçekten kaldırıldı mı? | yerleşik uygulama — içtihadı kontrol et |
| Toplu çıkarma eşiği | Usul ihlali; m. 18-21'i dolanmak yasak | 1 ay içindeki çıkarmaların toplamı | m. 29 |
| Alt işveren işçisi | Asıl işverenle birlikte sorumluluk, muvazaa | → `/arthurlegal:employment-legal-worker-classification` | m. 2 |

**Herhangi bir bayrak 🔴 → fesihten ÖNCE profilin eskalasyon matrisine göre onay.** Sonra değil.

### 4. İşe iade riskinin sonucu

İş güvencesi kapsamı: 30+ işçi, 6 ay kıdem, belirsiz süreli sözleşme, işveren vekili istisnası (m. 18). Geçersizlik kararında (m. 21): işveren işçiyi 1 ay içinde işe başlatır; başlatmazsa en az 4, en çok 8 aylık ücret tutarında tazminat; kesinleşmeye kadar en çok 4 aylık boşta geçen süre ücreti ve diğer haklar; işçi kesinleşen kararın tebliğinden itibaren 10 iş günü içinde başvurmazsa fesih geçerli sayılır (m. 21/6). Arabuluculukta işe başlatma anlaşması işe başlatma tarihini, boşta geçen süre alacağını ve işe başlatmama tazminatını parasal olarak içermek zorundadır (m. 21/7). Bu hükümler sözleşmeyle değiştirilemez.

### 5. Parasal kalemler (hesap iskeleti)

```
İhbar süresi (m. 17/2, asgari): <6 ay → 2 hf | 6 ay–1,5 yıl → 4 hf | 1,5–3 yıl → 6 hf | 3 yıl+ → 8 hf
İhbar tazminatı  = giydirilmiş günlük ücret × bildirim süresi (gün)          [m. 17/4, m. 17/7]
Kıdem tazminatı  = giydirilmiş son brüt ücret (tavanla sınırlı) × 30 gün × hizmet yılı (küsurat orantılı)  [1475 m. 14]
Kıdem tavanı     = güncel tutarı teyit et (dönemsel güncellenir)
Yıllık izin ücreti = kullanılmayan izin günü × sözleşmenin sona erdiği tarihteki ücret  [m. 59/1]
Kötüniyet (iş güvencesi dışı) = 3 × bildirim süresi ücreti                    [m. 17/6]
```

- Kıdem doğuran hâller 1475 m. 14'te sayılıdır: işveren feshi (ahlak ve iyiniyet hâlleri hariç), işçinin haklı feshi, muvazzaf askerlik, emeklilik/yaşlılık aylığı, yaş dışındaki şartların tamamlanması, kadının evlenmeden itibaren 1 yıl içinde ayrılması, ölüm. 1475'in yalnız m. 14'ü yürürlüktedir (4857 m. 120); m. 14'teki eski madde atıflarının 4857'deki karşılıklarla okunduğu yerleşik uygulamadır. Bir yılı doldurmayan çalışmada kıdem doğmadığı da yerleşik uygulamadır — teyit et.
- Sona ermede ücret ve para ile ölçülebilen tüm menfaatler tam ödenir (m. 32/6); kıdem gecikirse mevduata uygulanan en yüksek faiz (1475 m. 14).
- Bildirim süresi içinde günde en az 2 saat ücretli iş arama izni (m. 27); bildirim süresi yıllık izinle iç içe giremez (m. 59/2).
- İşsizlik ödeneği fesih nedenine bağlıdır (4447 m. 51; madde hâlâ 1475 numaralarına atıf yapar) → SGK çıkış kodu doğru seçilmeli. İkalenin işsizlik ödeneğine etkisi **tartışmalı** — SGK/İŞKUR uygulamasını ve içtihadı kontrol et.
- Her tutar satırına: `[doğrula — avukat/uzman kontrolünden geçmeden müvekkile verilmez]`.

### 6. Ayrılış paketi: ikale, ibraname, arabuluculuk anlaşması

ABD'deki "kıdem ödemesi + feragat (release)" kurgusunun Türk karşılıkları:

- **İbraname (TBK m. 420/2):** yazılı; sözleşmenin sona ermesinden en az 1 ay sonra; alacağın türü ve miktarı açık; ödeme hak tutarına göre noksansız ve banka aracılığıyla. Eksik unsur → kesin hükümsüz. Gerçek tutarı içermeyen belge yalnız ödenen miktar kadar makbuz hükmündedir (m. 420/3). **Fesih günü imzalatılan ibranameye güvenme.**
- **İkale + ek ödeme:** yazılı protokol; ödenecek kalemler tek tek; makul yarar ve irade sakatlığı riski (yukarıda).
- **Arabuluculuk anlaşması:** iş alacakları ve işe iade davalarında arabuluculuk dava şartıdır (7036 m. 3/1). Taraflar ve avukatları ile arabulucunun imzaladığı anlaşma belgesi ilam niteliğindedir (6325 m. 18/4); anlaşılan hususlar hakkında dava açılamaz (6325 m. 18/5). Anlaşılan kalemleri ve tutarları tek tek yaz; genel "tüm haklardan feragat" ifadesinin kapsamı **tartışmalı — içtihadı kontrol et**.
- **Gizlilik / karalamama klozu:** yalnız işçi aleyhine konan ceza koşulu geçersizdir (TBK m. 420/1) → karşılıklı kur.
- **Rekabet yasağı varsa:** işveren haklı sebep olmaksızın feshederse yasak sona erer (TBK m. 447/2).
- *Karşılaştırmalı not:* ABD'de 40 yaş üstü işçi için kanuni düşünme/cayma süreleri vardır; Türk hukukunda bunun karşılığı TBK m. 420'nin 1 aylık bekleme şartı ve arabuluculuk anlaşmasıdır.

### 7. Belge kontrolü

Uyarılar, savunma tutanakları, performans kayıtları tutarlı bir hikâye anlatıyor mu? Gerekçeyle çelişen yazılı bir şey (yakın tarihli olumlu değerlendirme, prim, terfi) var mı? "Bir yıldır düşük performans varsa ne değişti?" sorusunun cevabı yazılı olmalı.

### 8. Yurt dışında çalışan işçi

Uygulanacak hukuk: tarafların seçtiği hukuk, işçinin mutad işyeri hukukunun emredici asgari koruması saklı kalmak üzere (MÖHUK 5718 m. 27). Yabancı kural ezberden yazılmaz: AB `eu_search_eu_law(query="collective redundancies")`; İngiltere `uk_search_legislation`; Almanya `de_gesetz_ara`; Azerbaycan `az_search_acts(query="Əmək Məcəlləsi", types=[107])`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

### 9. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="4857", madde_no=["17","18","19","20","21","25","26"])
tr_mevzuat_madde_getir(number="1475", madde_no="14")
tr_mevzuat_madde_getir(number="6098", madde_no=["420","447"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="feshin son çare olması ilkesi işletmesel karar", date_from="2022-01-01")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="ikale makul yarar irade fesadı", date_from="2022-01-01")
tr_ictihat_semantik_ara(initial_keyword="savunma alınmadan fesih", query="iş güvencesi dışındaki işçide savunma zorunluluğu")
```

Daire dağılımı değişebilir; sonuç ince ise `chamber` boş bırakıp tekrar dene. Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Atıf etiketi: `[ArthurLegal TR — 4857 m. X — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`.

## Çıktı

Eklenti ayarında örnek fesih notu varsa onun biçimini izle; yoksa:

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Fesih İncelemesi — [Unvan/takma ad] — [Tarih]

## ⚠️ İnceleyen notu
- **Fesih türü:** [Geçerli m. 18 / Haklı m. 25 / Süreli m. 17 / İkale]
- **Süre:** [6 iş günü sonu GG.AA.YYYY / işe iade başvuru penceresi] 🔴/🟠/🟡
- **İş güvencesi:** [kapsamda / dışında — gerekçe]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) — [madde sayısı, içtihat sayısı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]
- **Eskalasyon:** [yok / [isim] — hangi bayrak]

## Sonuç
[Devam edilebilir / Önce X düzeltilmeli / Dur — tek cümle neden]

## Yüksek risk bayrakları
[Her bayrak: ✅ temiz ya da 🔴 BAYRAK + ayrıntı]

## İşe iade riski
[Kapsam + olası parasal sonuç aralığı]

## Parasal kalemler
[İhbar, kıdem (tavan teyidi), yıllık izin, diğer — formül + girdiler + doğrula etiketi]

## Ayrılış paketi
[İkale / ibraname zamanlaması / arabuluculuk anlaşması kalemleri]

## Belgeler
[Değerlendirme, eksikler]

## Karar
[Devam / Değişikliklerle devam / Bekle — eskalasyon]

### Fesih günü kontrol listesi
- [ ] Yazılı fesih bildirimi, sebep açık ve kesin (m. 19/1); tebliğ kanıtı
- [ ] Savunma tutanağı (davranış/verim nedenli fesihte, m. 19/2)
- [ ] Bildirim süresi ya da peşin ihbar ücreti (m. 17); iş arama izni planı (m. 27)
- [ ] Son ücret, yıllık izin ücreti, kıdem — banka yoluyla (m. 32, m. 59, 1475 m. 14)
- [ ] SGK işten ayrılış bildirimi 10 gün içinde, doğru çıkış kodu (5510 m. 9; 4447 m. 51)
- [ ] Çalışma belgesi (m. 28)
- [ ] Zimmet iadesi, sistem erişiminin kapatılması, kişisel verilerin saklama süresi
- [ ] İbraname gerekiyorsa en erken sona ermeden 1 ay sonra (TBK m. 420)
```

## Sonuç doğuran işlem kapısı (işçinin işine son verme)

"Devam edilebilir" ya da hazır kontrol listesi üretmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> İşten çıkarma işe iade, ayrımcılık, kötüniyet ve işçilik alacağı davalarına yol açabilir. Bu feshi bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: işçi, işyeri ve işçi sayısı, kıdem, fesih nedeni ve tarihi; çıkan her bayrak ve ayrıntısı; süre hesabı; parasal kalemler ve hangi kaynaktan çekildiği; ayrılış paketi önerisi; açık sorular; ters gidebilecek şey (bu olguların desteklediği dava teorisi); avukata sorulacaklar (fesih temiz mi, önce savunma/belge mi gerekir, arabuluculuk anlaşması nasıl kurulmalı). Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan "Devam edilebilir" yazma; avukat incelemesi için "TASLAK" işaretli çıktı serbest.

## İşçi tarafı varyantı

[Müvekkil] işçiyse: (1) tebliğ tarihini sabitle → işe iade için 1 aylık arabuluculuk penceresi (m. 20/1); alacaklar için zamanaşımı 5 yıl (m. 32/8; ek m. 3); arabuluculuk süresince zamanaşımı durur ve hak düşürücü süre işlemez (7036 m. 3/17). (2) Alacak kalemlerini `/arthurlegal:employment-legal-wage-hour-qa` ile hesapla; hesap doğru olmadan başvurma (profil uyarısı). (3) İmzalatılmış ibraname varsa TBK m. 420 şartlarıyla test et. (4) İlk arabuluculuk toplantısına mazeretsiz katılmamanın masraf ve vekâlet ücreti sonucu vardır (7036 m. 3/12).

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu incelemenin sonucuna göre uyarla (fesih bildirimi taslağı, eskalasyon, ek olgu, bekle-izle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Fesih kararını vermez; kararı denetler.
- Fesih görüşmesini yapmaz.
- Kural ya da tutarı ezberden vermez; her madde araçtan, her tutar güncel kaynaktan.
- Dava çıkmayacağını garanti etmez; bariz sorunları yakalayarak riski azaltır.

---

## Kaynak katmani — /legal-research (v1.4.0)

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur —
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
