# ArthurLegal MCP (`tr_`): Mevzuat ve Resmî Gazete Rehberi

> Bu rehber mevzuat ve Resmî Gazete araçlarını anlatır. Yargı, AYM, Uyuşmazlık ve kurum kararları `yargi-mcp-rehberi.md` içindedir; ikisi aynı connector'dır (endpoint `arthurlegal-mcp.fly.dev/mcp`, auth yok, önek `tr_`).
> Araç adları ve parametreler 06.09.2026'da canlı uçtan doğrulanmıştır. `search_mevzuat`, `mevzuat_ara`, `mevzuat_getir(id_type=...)`, `search_kanun`, `search_teblig` gibi öneksiz veya eski adlar bu connector'da yoktur.

## 1. Araçlar

| Araç | Ne yapar | Kritik parametreler |
|---|---|---|
| `tr_mevzuat_ara` | Bedesten (mevzuat.adalet.gov.tr) üzerinde 12 tür mevzuatta arama | `query` (varsayılan başlıkta; `search_in="fulltext"` ile metinde), `number` (mevzuat numarası, en kesin yol), `types` (tür listesi), `exact_phrase`, `rg_date_from`, `rg_date_to`, `rg_number`, `page`, `page_size` (en çok 50) |
| `tr_mevzuat_getir` | Tam metin, sayfalı | `mevzuat_id` (aramadan), `page`, `page_chars` |
| `tr_mevzuat_icindekiler` | Madde ağacı: bölüm ve madde başlıkları, `madde_id`'ler | `mevzuat_id` |
| `tr_mevzuat_madde_getir` | Tek madde metni | `madde_id` (`tr_mevzuat_icindekiler` sonucundan) |
| `tr_mevzuat_icinde_ara` | Bir mevzuatın maddelerinde anahtar kelime arama; isabete göre sıralı madde listesi | `mevzuat_id`, `query` (düz kelimeler), `limit` |
| `tr_mevzuat_gerekce` | Kanun gerekçesi: genel gerekçe, komisyon raporları, madde gerekçeleri | `gerekce_id` (aramada `gerekce_id` alanı dolu olan kanunlar), `page` |
| `tr_resmi_gazete_fihrist` | Bir günün Resmî Gazete fihristi: bölüm, başlık, link | `date` (ISO; verilmezse bugün), `mukerrer`, `query` (başlık filtresi) |
| `tr_resmi_gazete_getir` | Fihristteki bir belgenin tam metni | `url` (fihrist sonucundaki `url`), `page` |
| `tr_resmi_gazete_tara` | Tarih aralığında (en çok 60 gün) fihrist başlıklarında arama; gün başına bir istek | `query`, `date_from`, `date_to` |

Mevzuat türleri (`types`): `KANUN`, `KHK`, `TUZUK`, `CB_KARARNAME`, `CB_KARAR`, `CB_YONETMELIK`, `CB_GENELGE`, `YONETMELIK` (Bakanlar Kurulu yönetmelikleri), `KKY` (kurum ve kuruluş yönetmelikleri), `UY` (üniversite yönetmelikleri), `TEBLIGLER`, `MULGA`. `types` verilmezse tüm türlerde aranır. Sektörel ikincil düzenleme (EPDK, SPK, BDDK yönetmelik ve tebliğleri) `types=["KKY", "TEBLIGLER"]` ile ve kurum adıyla bulunur.

## 2. Kimlik disiplini

1. `number` resmî kanun numarasıdır (6698 KVKK, 6102 TTK, 6098 TBK, 213 VUK, 5237 TCK, 5271 CMK, 6100 HMK, 2577 İYUK, 4857 İş K., 3065 KDVK, 6446 EPK, 5015 PPK, 4646 DGPK). Emin değilsen numarayı uydurma; önce `query` ile ara, numarayı yanıttan al.
2. `mevzuat_id` Bedesten'in sayısal kimliğidir (`103045` gibi) ve yalnız `tr_mevzuat_ara` yanıtından gelir; kendin kurma.
3. `madde_id` yalnız `tr_mevzuat_icindekiler` yanıtından gelir. Madde numarası ve RG künyesi kayıttan okunur; ezberden yazılmaz.
4. Her arama sonucu hazır bir `citation` alanı taşır (`<Ad> (Kanun No. 6446, RG 30.03.2013/28603)`); birebir kullanılır.

## 3. Arama davranışı

1. Varsayılan arama BAŞLIKTADIR. Hüküm metni için `search_in="fulltext"` ver; Bedesten Solr diyalekti geçerlidir (`"tam öbek"`, `+zorunlu`, `-hariç`, `AND`, `OR`, `NOT`). 2 ile 5 terim yaz.
2. Sıralama Resmî Gazete tarihine göredir. Hedefi öne çıkarmak için `number` veya `types` ile daralt.
3. RG tarih filtresi yayım tarihine bakar, yürürlük tarihine değil. Yürürlüğü kanunun yürürlük maddesinden ve değişiklik notlarından oku.
4. `tr_mevzuat_icinde_ara` madde metinlerinde düz kelime arar (operatör yok); her isabet madde başlığı, isabet sayısı ve alıntı taşır. Kavramsal hüküm araması için `tr_semantik_ara` yerel indeksi kullanır ve mevzuat metnini KAPSAMAZ; hüküm araması bu araçla yapılır.
5. Tebliğ, CB kararı ve genelge PDF olabilir; metin çıkarımı sunucuda yapılır (pypdf). Taranmış PDF'te metin boş dönerse yanıt bunu söyler; URL'yi kaynak olarak ver.
6. Uzun metinler `page` ve `page_chars` ile sayfalanır; devasa kanunda tam metin yerine `tr_mevzuat_icindekiler` ve `tr_mevzuat_madde_getir` ile ilgili maddeyi al.
7. Gerekçe yalnız `gerekce_id` dolu kanunlarda vardır (TBMM'ye sunulmuş kanunlar); yoksa yanıt "gerekçe yayımlanmamış" der, TBMM kaynaklarına git.
8. Bedesten hız sınırı (IP başına 30 saniyede 10 istek) mevzuat ve içtihat araçları arasında ortaktır; art arda 5'ten fazla çağrı yapma.

## 4. Tipik kullanım

Kanun numarasıyla madde:

```
tr_mevzuat_ara(number="6098", types=["KANUN"])
tr_mevzuat_icindekiler(mevzuat_id="<mevzuat_id>")
tr_mevzuat_madde_getir(madde_id="<madde 350'nin madde_id'si>")
```

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

Belirli bir günün Resmî Gazete'si ve konsolide metne geçiş:

```
tr_resmi_gazete_fihrist(date="2026-09-05", query="kurul")
tr_resmi_gazete_getir(url="<fihrist sonucundaki url>")
tr_mevzuat_ara(number="<değiştirilen kanun>", types=["KANUN"])
```

Tarih aralığında konu:

```
tr_resmi_gazete_tara(query="Enerji Piyasası Düzenleme Kurulu", date_from="2026-08-01", date_to="2026-09-05")
```

Resmî Gazete gün bazlıdır; RG metni yalnız değişiklik hükmüdür, yürürlükteki hâl için konsolide metne geç. Mükerrer sayı `mukerrer=1` ile alınır. Kurul kararları fihristte "KURUL KARARI" veya "KURUL KARARLARI" bölümündedir; EPDK, BDDK, SPK ve Rekabet Kurumu kararlarının yayım teyidi buradan yapılır.

## 5. Atıf

```
[ArthurLegal TR, 6098 sayılı TBK m. 350, GG.AA.YYYY]
[ArthurLegal TR, Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi Hakkında Yönetmelik m. 8, GG.AA.YYYY]
[ArthurLegal TR, 7429 sayılı Kanun gerekçesi, madde 3, GG.AA.YYYY]
[Resmî Gazete, 33361, 05.09.2026]
```

Alanlar virgülle ayrılır. Araç çıktısında URL varsa eklenir; mevzuat maddeleri için URL uydurulmaz, belge adı ve madde numarasıyla atıf yapılır. Çekilmediyse `[model bilgisi, doğrulayın]`.

## 6. Sınırlar

1. Yargıtay, Danıştay ve AYM kararları bu araçlarda yoktur; `yargi-mcp-rehberi.md`.
2. Kurum kararları (BDDK, SPK, EPDK, KVKK Kurulu) mevzuat değildir; `tr_kurum_karari_ara`.
3. Tasarı ve kanun teklifi aşamasındaki metinler yoktur; TBMM sitesi.
4. Belediye ve yerel idare düzenlemeleri sınırlıdır.
5. Her araç çağrısı 100 saniyede iptal edilir; dar tut, iptal olursa aynı sorguyu tekrarlama.

## 7. Birlikte kullanım

Bir hukuki soru çoğunlukla üç adımdır: `tr_mevzuat_ara`, `tr_mevzuat_icindekiler` ve `tr_mevzuat_madde_getir` ile ilgili madde; `tr_ictihat_ara` veya `tr_ictihat_semantik_ara` ile o maddenin yargı yorumu; skill playbook'u ile sentez. Atıf etiketleri korunur.

*Son güncelleme: 06.09.2026. Araç listesi ve parametreler canlı uçtan doğrulandı.*
