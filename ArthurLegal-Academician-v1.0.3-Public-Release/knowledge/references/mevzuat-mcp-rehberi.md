# ArthurLegal MCP (`tr_`): Mevzuat ve Resmî Gazete Rehberi

> Bu rehber mevzuat ve Resmî Gazete araçlarını anlatır. Yargı, AYM, Uyuşmazlık ve kurum kararları `yargi-mcp-rehberi.md` içindedir; ikisi aynı connector'dır (endpoint `arthurlegal-mcp.fly.dev/mcp`, auth yok, önek `tr_`).
> Araç adları ve parametreler 20.09.2026'da Türkiye backend'inin (ArthurLegalTR) 0.4.0 sürümünden ve canlı Bedesten çağrılarından doğrulanmıştır. `status` çıktısında `backend_status.tr.version` 0.4.0'dan küçükse bölüm 4'teki `konu` süzgeci, sorgusuz listeleme ve tarih aralığı düzeltmesi o uçta yoktur; o durumda `query` ile çalış ve tarih aralığının iki ucunu da ver. `search_mevzuat`, `mevzuat_ara`, `mevzuat_getir(id_type=...)`, `search_kanun`, `search_teblig` gibi öneksiz veya eski adlar bu connector'da yoktur.

## 1. Araçlar

| Araç | Ne yapar | Kritik parametreler |
|---|---|---|
| `tr_mevzuat_ara` | Bedesten (mevzuat.adalet.gov.tr) üzerinde 12 tür mevzuatta arama; sorgu kelimesi olmadan tür ve tarih aralığıyla listeleme | `query` (varsayılan başlıkta; `search_in="fulltext"` ile metinde), `number` (mevzuat numarası, en kesin yol), `types` (tür listesi), `exact_phrase`, `rg_date_from`, `rg_date_to`, `rg_number`, `page`, `page_size` (en çok 20), `konu`, `esik`, `max_pages` (bölüm 4) |
| `tr_mevzuat_getir` | Tam metin, sayfalı | `mevzuat_id` (aramadan), `page`, `page_chars` |
| `tr_mevzuat_icindekiler` | Madde ağacı: bölüm ve madde başlıkları, `madde_id`'ler | `mevzuat_id` |
| `tr_mevzuat_madde_getir` | Tek madde metni (başlık dâhil) | `madde_id` (`tr_mevzuat_icindekiler` sonucundan); yeni sürümde şemada görünüyorsa `number` ve `madde_no` ile tek çağrı, `madde_no` liste olabilir (bölüm 5 ve 9) |
| `tr_mevzuat_icinde_ara` | Bir mevzuatın maddelerinde anahtar kelime arama; isabete göre sıralı madde listesi | `mevzuat_id`, `query` (düz kelimeler), `limit` |
| `tr_mevzuat_gerekce` | Kanun gerekçesi: genel gerekçe, komisyon raporları, madde gerekçeleri | `gerekce_id` (aramada `gerekce_id` alanı dolu olan kanunlar), `page` |
| `tr_resmi_gazete_fihrist` | Bir günün Resmî Gazete fihristi: bölüm, başlık, link | `date` (ISO; verilmezse bugün), `mukerrer`, `query` (başlık filtresi), `konu`, `esik` |
| `tr_resmi_gazete_getir` | Fihristteki bir belgenin tam metni | `url` (fihrist sonucundaki `url`), `page` |
| `tr_resmi_gazete_tara` | Tarih aralığında (en çok 60 gün) fihrist başlıklarında arama; gün başına bir istek | `query` veya `konu` (biri yeter, ikisi VE ile birleşir), `esik`, `date_from`, `date_to` |

Mevzuat türleri (`types`): `KANUN`, `KHK`, `TUZUK`, `CB_KARARNAME`, `CB_KARAR`, `CB_YONETMELIK`, `CB_GENELGE`, `YONETMELIK` (Bakanlar Kurulu yönetmelikleri), `KKY` (kurum ve kuruluş yönetmelikleri), `UY` (üniversite yönetmelikleri), `TEBLIGLER`, `MULGA`. `types` verilmezse tüm türlerde aranır. Sektörel ikincil düzenleme (EPDK, SPK, BDDK yönetmelik ve tebliğleri) `types=["KKY", "TEBLIGLER"]` ile ve kurum adıyla bulunur.

## 2. Kimlik disiplini

1. `number` resmî kanun numarasıdır (6698 KVKK, 6102 TTK, 6098 TBK, 213 VUK, 5237 TCK, 5271 CMK, 6100 HMK, 2577 İYUK, 4857 İş K., 3065 KDVK, 6446 EPK, 5015 PPK, 4646 DGPK). Emin değilsen numarayı uydurma; önce `query` ile ara, numarayı yanıttan al.
2. `mevzuat_id` Bedesten'in sayısal kimliğidir (`103045` gibi) ve yalnız `tr_mevzuat_ara` yanıtından gelir; kendin kurma.
3. `madde_id` yalnız `tr_mevzuat_icindekiler` yanıtından gelir. Madde numarası ve RG künyesi kayıttan okunur; ezberden yazılmaz. Kural sözleşme, protokol, dilekçe ve karar gövdesine yazılan madde numaraları için de geçerlidir ve yalnız numarayı değil, maddeye yüklenen içeriği de kapsar: başlık ve metin okunup karşılaştırılır. Knowledge dosyalarındaki madde haritaları ezber sayılır, çekimin yerine geçmez (bölüm 9).
4. Her arama sonucu hazır bir `citation` alanı taşır (`<Ad> (Kanun No. 6446, RG 30.03.2013/28603)`); birebir kullanılır.

## 3. Arama davranışı

1. Varsayılan arama BAŞLIKTADIR. Hüküm metni için `search_in="fulltext"` ver; Bedesten Solr diyalekti geçerlidir (`"tam öbek"`, `+zorunlu`, `-hariç`, `AND`, `OR`, `NOT`). 2 ile 5 terim yaz.
2. Sorgu kelimesi zorunlu değildir: `types` ve/veya `rg_date_from`, `rg_date_to`, `rg_number` verilirse Bedesten o türdeki mevzuatı RG tarihine göre yeniden eskiye listeler. "Son iki yılda çıkan kanunlar" böyle sorulur.
3. Sayfa başına en çok 20 kayıt gelir; Bedesten 20'den büyüğünü HTTP 400 ile reddeder. Daha fazlası için `page` ile ilerle.
4. Tarih aralığı: Bedesten tek taraflı aralığı (yalnız başlangıç veya yalnız bitiş) sessizce yok sayar; 0.4.0'dan önce `rg_date_from="2024-09-01"` tek başına 6 yerine 917 kanunun hepsini döndürüyordu. Sunucu artık eksik ucu kendisi doldurur. Yine de sonuçtaki `rg_date` alanlarının istenen aralıkta olduğuna bak; aralık dışı kayıt görürsen iki ucu da açıkça ver ve bunu çıktıda belirt.
5. Sıralama Resmî Gazete tarihine göredir. Hedefi öne çıkarmak için `number` veya `types` ile daralt.
6. RG tarih filtresi yayım tarihine bakar, yürürlük tarihine değil. Yürürlüğü kanunun yürürlük maddesinden ve değişiklik notlarından oku.
7. Bedesten yalnız ana metinleri listeler; bir yönetmelikte değişiklik yapan yönetmelik ayrı kayıt olarak görünmez, ana metne işlenir. Günlük değişiklik akışı Resmî Gazete fihristindedir (`tr_resmi_gazete_tara`), konsolide külliyat buradadır.
8. `tr_mevzuat_icinde_ara` madde metinlerinde düz kelime arar (operatör yok); her isabet madde başlığı, isabet sayısı ve alıntı taşır. Kavramsal hüküm araması için `tr_semantik_ara` yerel indeksi kullanır ve mevzuat metnini KAPSAMAZ; hüküm araması bu araçla yapılır.
9. Tebliğ, CB kararı ve genelge PDF olabilir; metin çıkarımı sunucuda yapılır (pypdf). Taranmış PDF'te metin boş dönerse yanıt bunu söyler; URL'yi kaynak olarak ver.
10. Uzun metinler `page` ve `page_chars` ile sayfalanır; devasa kanunda tam metin yerine `tr_mevzuat_icindekiler` ve `tr_mevzuat_madde_getir` ile ilgili maddeyi al.
11. Gerekçe yalnız `gerekce_id` dolu kanunlarda vardır (TBMM'ye sunulmuş kanunlar); yoksa yanıt "gerekçe yayımlanmamış" der, TBMM kaynaklarına git.
12. Bedesten hız sınırı (IP başına 30 saniyede 10 istek) mevzuat ve içtihat araçları arasında ortaktır; aynı turda 5'ten fazla çağrı gönderme, fazlasını sonraki turlara böl. Bu bir tempo kuralıdır; doğrulanacak madde sayısına üst sınır değildir.

## 4. Konu taraması: `konu` süzgeci (yerel ön eleme)

`query` harfi harfine eşleşir. Bu, bilinen bir terimi bulmak için doğrudur; bir alanı taramak için yetmez, çünkü başlıklar konu adını çoğu zaman taşımaz. Etiketli 1.414 Resmî Gazete kaleminde ölçüldü: konu adı, icra kalemlerinin yalnız yüzde 10'unun, rekabet kalemlerinin yüzde 14'ünün, enerji kalemlerinin yüzde 58'inin, vergi kalemlerinin yüzde 61'inin başlığında geçiyor. "Konkordato Gider Avansı Tarifesi" icradır ama "icra" yazmaz; "Şarj Hizmeti Yönetmeliği" enerjidir ama "enerji" yazmaz.

`konu` (`enerji`, `rekabet`, `vergi`, `icra`) başlıklara konu olasılığı veren yerel bir modeldir. Sunucunun içinde koşar; ağa çıkmaz, anahtar istemez, sorgu hiçbir üçüncü tarafa gitmez. İki katmanlıdır: dar ve gerekçeli kurallar (eşleşirse olasılık 1,0) ve karakter n-gramı üzerinde lojistik regresyon; sonuç ikisinin büyüğüdür, yani kural yalnız ekler, hiçbir kalemi eleyemez. Eğitim verisi kamuya açık Resmî Gazete fihristidir; hiçbir müvekkil verisi kullanılmamıştır.

Üç araçta vardır:

```
tr_resmi_gazete_tara(konu="enerji", date_from="2026-09-01", date_to="2026-09-19")
tr_resmi_gazete_tara(konu="icra", query="tarife")                 # ikisi VE ile birleşir
tr_resmi_gazete_fihrist(date="2026-09-18", konu="vergi")
tr_mevzuat_ara(types=["KANUN"], rg_date_from="2024-09-01", konu="icra", max_pages=3)
tr_mevzuat_ara(types=["TEBLIGLER"], rg_date_from="2026-06-01", konu="vergi")
```

Torba kanunlar. "Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanun" başlığı neyi değiştirdiğini söylemez: 7531 sayılı Kanun İcra ve İflas Kanununu ve HMK'yı, 7579 sayılı Kanun Damga Vergisi Kanununu değiştirir. `tr_mevzuat_ara` bu yüzden başlığı eşiği geçemeyen torba kanunun metnini açar, değiştirilen kanun adlarını okur ve onları skorlar; sonuçta `konu_kaynak: "degistirilen_kanunlar"` ve tetikleyen ad `konu_degistirilen` alanında döner. Bir çağrıda en çok 5 torba kanunun metni açılır. Adları okunamayan torba kanun (sınır aşıldı, metin "ilgili kanunlara işlenmiştir" diyor, istek düştü) ELENMEZ; `konu_kaynak: "belirsiz"` ile döner. Belirsiz kalemi `tr_mevzuat_getir` ile aç ve kendin karar ver.

Yanıt alanları: her kalemde `konu_skoru` ve (mevzuatta) `konu_kaynak`; üstte `konu_elenen` (atılan kalem sayısı), `konu_belirsiz`, `konu_taranan`, `pages_scanned`, `esik` ve sınırı tekrarlayan `konu_notu`. `pages_error` varsa taramanın bir sayfası alınamamıştır; sonuç eksiktir, boş değildir.

Ölçülmüş sınırlar (tahmin değil; eşik 0,20):

| Nerede | Ne ölçüldü | Sonuç |
|---|---|---|
| Resmî Gazete, kat dışı ölçüm (3.581 kalem; pozitif: enerji 179, rekabet 37, vergi 87, icra 52) | duyarlılık | enerji yüzde 97, rekabet yüzde 100, vergi yüzde 93, icra yüzde 92; kalemlerin yüzde 90'ı elenir |
| Resmî Gazete, elle etiketli 56 kalemlik sınav kümesi | yakalanan pozitif | enerji 8'de 5, rekabet, vergi ve icra tam; isabet yüzde 100 |
| Mevzuat başlıkları, eğitimde görülmüş 127 başlık | yalnız Bedesten biçimine aktarım | 26 pozitifin 26'sı, 3 yanlış pozitif |
| Mevzuat başlıkları, görülmemiş 60 başlık | genelleme | vergi 4'te 4, icra 2'de 2, enerji 3'te 0, 2 yanlış pozitif |
| Aynı 60 başlık, torba kanun geçişi kapalı | başlığın tek başına yettiği yer | vergi 4'te 3, icra 2'de 1 |

Enerjide kaçanlar ortak bir kalıp taşır: konu dünya bilgisi ister ve başlık bunu söylemez. "Hava Kalitesinin Korunması Amacıyla Katı Yakıtların Kontrolü Yönetmeliği" kömür piyasasını düzenler; "Belediyeler ve İl Özel İdarelerinin Genel Bütçe Vergi Gelirleri Payından Yapılacak Aydınlatma Gideri Kesintileri" elektrik maliyetidir; "Rüzgâr Gücü İzleme ve Tahmin Merkezine Bağlantı Yönetmeliği" yenilenebilir üretimdir. Model bunları görmez.

Kullanım kuralları:

1. `konu` bir ön elemedir, kapsam garantisi değildir. Çıktıda kaç kalemin elendiğini (`konu_elenen`) ve kaçının belirsiz kaldığını yaz; "bu dönemde başka bir şey çıkmadı" deme, "konu süzgecinden geçen kalemler bunlar, N kalem elendi" de.
2. Yayım teyidinde, süre hesabında ve "X hakkında hiçbir düzenleme yok" sonucuna varırken `konu` kullanılmaz. Orada `query` kullan veya `esik=0` ile tam listeyi al.
3. Enerji taramasında `konu`'ya tek başına güvenme: `konu="enerji"` sonucunu `query` ile yapılan ikinci bir taramayla (elektrik, doğal gaz, petrol, lisans, EPDK) tamamla.
4. Dört konu dışında süzgeç yoktur. KVKK, iş hukuku, sermaye piyasası gibi alanlar için `query` ve `types` kullan.
5. `esik=0` süzgeci kapatır ve skorları yine döndürür; eşiği düşürmek kaçanları geri getirmez (ölçüldü), yalnız ilgisiz kalemi artırır.

## 5. Tipik kullanım

Kanun ve madde numarasıyla tek çağrı (yalnız `tr_mevzuat_madde_getir` şemasında `number` ve `madde_no` görünüyorsa):

```
tr_mevzuat_madde_getir(number="6769", madde_no="120")
tr_mevzuat_madde_getir(number="6769", madde_no=["115", "117", "119"])   # şema liste kabul ediyorsa
```

Kanun numarasıyla madde (şemada yalnız `madde_id` varsa):

```
tr_mevzuat_ara(number="6098", types=["KANUN"])
tr_mevzuat_icindekiler(mevzuat_id="<mevzuat_id>")        # kanun başına sohbette bir kez
tr_mevzuat_madde_getir(madde_id="<madde 350'nin madde_id'si>")
```

Aynı kanunun birden çok maddesi aynı ağaçtaki `madde_id`'lerle, aynı turda en çok 5 çağrı olarak istenir. `tr_mevzuat_icinde_ara(query="<madde no>")` madde bulma yolu değildir. Ölçüm (21.09.2026, SMK): `query="30"` ilk sırada m. 129'u, ikinci sırada m. 30'u döndürdü; `query="120"` doğru maddeyi buldu ama alıntı madde başlığını taşımadı ve sonraki maddenin başlığıyla bitti.

Madde içinde kelime araması:

```
tr_mevzuat_icinde_ara(mevzuat_id="<mevzuat_id>", query="ihracat istisna", limit=5)
```

Konu araması, kanun numarası bilinmiyor:

```
tr_mevzuat_ara(query="kişisel veri yurt dışı aktarım", search_in="fulltext", types=["KANUN", "YONETMELIK", "KKY", "TEBLIGLER"])
```

Yönetmelik ve tebliğ:

```
tr_mevzuat_ara(query="Kişisel Verilerin Silinmesi", types=["KKY", "YONETMELIK"])
tr_mevzuat_ara(query="Enerji Piyasası", types=["KKY"])
tr_mevzuat_ara(query="Sermaye Piyasası", types=["TEBLIGLER"])
```

Cumhurbaşkanlığı kararnamesi, kararı ve genelgesi:

```
tr_mevzuat_ara(query="sermaye hareketleri", search_in="fulltext", types=["CB_KARARNAME"])
tr_mevzuat_ara(query="kamu alımları", types=["CB_GENELGE"])
```

Yürürlükten kalkmış kanun:

```
tr_mevzuat_ara(number="765", types=["MULGA"])
```

Gerekçe:

```
tr_mevzuat_ara(number="7429", types=["KANUN"])        # yanıtta gerekce_id
tr_mevzuat_gerekce(gerekce_id="<gerekce_id>", page=1)
```

Bir dönemde İcra ve İflas Kanununu değiştiren kanunlar (torba kanunlar dâhil):

```
tr_mevzuat_ara(types=["KANUN"], rg_date_from="2024-01-01", rg_date_to="2026-09-20", konu="icra", page_size=20)
tr_mevzuat_getir(mevzuat_id="<konu_kaynak belirsiz olan kalem>")     # belirsizleri kendin oku
```

Belirli bir günün Resmî Gazete'si ve konsolide metne geçiş:

```
tr_resmi_gazete_fihrist(date="2026-09-05", query="kurul")
tr_resmi_gazete_getir(url="<fihrist sonucundaki url>")
tr_mevzuat_ara(number="<değiştirilen kanun>", types=["KANUN"])
```

Tarih aralığında bilinen bir terim, sonra aynı aralıkta konu:

```
tr_resmi_gazete_tara(query="Enerji Piyasası Düzenleme Kurulu", date_from="2026-08-01", date_to="2026-09-05")
tr_resmi_gazete_tara(konu="enerji", date_from="2026-08-01", date_to="2026-09-05")
```

Resmî Gazete gün bazlıdır; RG metni yalnız değişiklik hükmüdür, yürürlükteki hâl için konsolide metne geç. Mükerrer sayı `mukerrer=1` ile alınır. Kurul kararları fihristte "KURUL KARARI" veya "KURUL KARARLARI" bölümündedir; EPDK, BDDK, SPK ve Rekabet Kurumu kararlarının yayım teyidi buradan `query` ile yapılır, `konu` ile değil.

## 6. Atıf

```
[ArthurLegal TR, 6098 sayılı TBK m. 350, GG.AA.YYYY]
[ArthurLegal TR, Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi Hakkında Yönetmelik m. 8, GG.AA.YYYY]
[ArthurLegal TR, 7429 sayılı Kanun gerekçesi, madde 3, GG.AA.YYYY]
[Resmî Gazete, 33361, 05.09.2026]
```

Alanlar virgülle ayrılır. Araç çıktısında URL varsa eklenir; mevzuat maddeleri için URL uydurulmaz, belge adı ve madde numarasıyla atıf yapılır. Madde önce çekilir; `[model bilgisi, doğrulayın]` yalnız madde çekilemediyse (connector kurulu değil, hata, iptal) ve yalnız not içindeki atıfta kullanılır. Çekilemeyen madde sözleşme, protokol, dilekçe veya karar gövdesine numarasıyla yazılmaz (bölüm 9). `konu_skoru` bir atıf unsuru değildir; çıktıya yalnız tarama yöntemini anlatırken girer.

## 7. Sınırlar

1. Yargıtay, Danıştay ve AYM kararları bu araçlarda yoktur; `yargi-mcp-rehberi.md`.
2. Kurum kararları (BDDK, SPK, EPDK, KVKK Kurulu) mevzuat değildir; `tr_kurum_karari_ara`.
3. Tasarı ve kanun teklifi aşamasındaki metinler yoktur; TBMM sitesi.
4. Belediye ve yerel idare düzenlemeleri sınırlıdır.
5. Her araç çağrısı 100 saniyede iptal edilir; dar tut, iptal olursa aynı sorguyu tekrarlama. `max_pages` büyüdükçe ve torba kanun metni açıldıkça çağrı uzar (istek başına yaklaşık 3,5 saniye); 60 günlük Resmî Gazete taraması 60 istektir, gerekirse aralığı böl.
6. `konu` süzgeci dört konuyla ve başlıkla sınırlıdır; bölüm 4'teki ölçülmüş sınırlar geçerlidir.

## 8. Birlikte kullanım

Bir hukuki soru çoğunlukla üç adımdır: `tr_mevzuat_ara`, `tr_mevzuat_icindekiler` ve `tr_mevzuat_madde_getir` ile ilgili madde; `tr_ictihat_ara` veya `tr_ictihat_semantik_ara` ile o maddenin yargı yorumu; skill playbook'u ile sentez. Atıf etiketleri korunur. Düzenleme takibinde sıra tersinedir: `tr_resmi_gazete_tara` ile akış (önce `konu`, sonra `query` ile tamamlama), `tr_resmi_gazete_getir` ile değişiklik hükmü, `tr_mevzuat_ara(number=…)` ile konsolide metin.

## 9. Madde doğrulama kapısı (teslim öncesi)

Teslim edilecek her çıktıda (not, sözleşme, protokol, ihtarname, dilekçe, gerekçe, dipnot) şu adımlar uygulanır. Bu çağrılar "en az çağrı" kuralına tabi değildir.

1. Çıktıdaki bütün madde atıflarını tara ve listele: kanun, madde, fıkra, bent; belge gövdesindekiler dâhil.
2. Her kalem için bu sohbette çekim var mı bak: `tr_mevzuat_madde_getir` yanıtı veya `tr_mevzuat_getir` ile okunmuş tam metin. Madde ağacındaki başlık tek başına yetmez; hakkın sahibi, şart ve süre metinden okunur.
3. Çekilmemişse çek: şemada `number` ve `madde_no` varsa tek çağrı, yoksa arama, ağaç ve madde yolu (bölüm 5).
4. Eşleştir: çıktının maddeye yüklediği içerik (hakkın veya yükümlülüğün sahibi, doğum şartı, süre, sonuç) madde başlığı ve metniyle örtüşüyor mu? Örtüşmüyorsa numarayı koruyup açıklamayı uydurma; doğru maddeyi bul ve çek ya da cümleyi yeniden yaz.
5. Çekilemiyorsa (connector kurulu değil, hata, iptal) madde numarasını gövdeden çıkar, hükmü numarasız ve genel ifadeyle kur, not içindeki atıfta `[model bilgisi, doğrulayın]` kullan, açık kalan noktayı İnceleme notunda adıyla yaz.
6. İnceleme notuna tek cümle ekle: "Madde kontrolü: <kanun m. X ve Y> okundu ve eşleşti; <kanun m. Z> çekilemedi, gövdeden çıkarıldı."

Knowledge dosyalarındaki madde haritaları (`smk-rehberi.md`, `hmk-rehberi.md` ve benzerleri) ve skill şablonlarındaki örnek atıflar yalnız neyin çekileceğini gösterir; doğrulama yerine geçmez.

Örnek hata: bir iş ve fikri haklar protokolünün 5.5 klozunda "SMK m. 120, ŞİRKET'in önalım hakkı" yazıldı. SMK m. 120'nin başlığı "Çalışanın önalım hakkı"dır; hak, işveren iflas ettiğinde ve iflas idaresi buluşu işletmeden ayrı devretmek istediğinde çalışana tanınır. Madde çekilseydi başlık hatayı tek bakışta gösterirdi.

*Son güncelleme: 22.09.2026. Madde doğrulama kapısı (bölüm 9) ve tek çağrılı madde okuma (`tr_mevzuat_madde_getir(number=…, madde_no=…)`, şemada görünüyorsa) eklendi. Önceki doğrulama: 20.09.2026. Parametreler ArthurLegalTR 0.4.0 kaynak kodu, 33 çevrimdışı test ve canlı Bedesten çağrılarıyla doğrulandı; `konu` ölçümleri arthurlegal-1.9.1-jev-edition deposundaki sınav kümelerine dayanır.*
