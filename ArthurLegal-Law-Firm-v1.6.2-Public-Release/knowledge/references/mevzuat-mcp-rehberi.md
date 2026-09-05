# TR Legal MCP (yargi-mcp-pro): Mevzuat ve Resmî Gazete Rehberi

> Bu rehber mevzuat ve Resmî Gazete araçlarını anlatır. Yargı, AYM, AİHM ve kurum kararları `yargi-mcp-rehberi.md` içindedir; ikisi aynı connector'dır (endpoint ve kurulum orada).
> Araç adları ve parametreler 05.09.2026'da canlı bağlantıdan doğrulanmıştır. `search_mevzuat`, `get_mevzuat_content`, `search_within_mevzuat`, `get_mevzuat_madde_tree`, `search_kanun`, `search_teblig`, `search_cbk` gibi eski adlar artık yoktur.

## 1. Araçlar

| Araç | Ne yapar | Kritik parametreler |
|---|---|---|
| `mevzuat_ara` | mevzuat.gov.tr üzerinde 12 tür mevzuatta arama | `mevzuat_adi` (başlıkta arar), `mevzuat_no` (resmî numara, en kesin yol), `phrase` (gövdede arar, operatörsüz), `mevzuat_tur_list` (bir çağrıda en çok 4 tür), `resmi_gazete_tarihi_start`, `resmi_gazete_tarihi_end`, `page`, `page_size` (en çok 20) |
| `mevzuat_getir` | Tam metin, tek madde veya madde ağacı | `id` (`mevzuat_ara`'dan gelen `mevzuat_id`), `id_type` (`mevzuat`, `madde`, `outline`), `madde_no`, `chunk` |
| `mevzuat_icinde_ara` | Tek bir mevzuat içinde boolean arama | `mevzuat_id`, `query` (BÜYÜK HARF `AND`, `OR`, `NOT`, tırnak, parantez), `page`, `page_size` (en çok 50), `sort_by` |
| `resmi_gazete_fihrist` | Bir günün Resmî Gazete içindekiler listesi | `tarih` (ISO; verilmezse bugün), `mukerrer_no`, `include_ilan` |
| `resmi_gazete_getir` | Fihristteki bir maddenin tam metni | `document_id` (yalnız `resmi_gazete:` kimliği) |

Mevzuat türleri: `KANUN`, `KHK`, `TUZUK`, `YONETMELIK` (Bakanlar Kurulu yönetmelikleri), `CB_KARARNAME`, `CB_YONETMELIK`, `CB_KARAR`, `CB_GENELGE`, `KKY` (kurum ve kuruluş yönetmelikleri), `UY` (üniversite yönetmelikleri), `TEBLIGLER`, `MULGA` (yürürlükten kalkmış kanunlar, kısmi kapsam). `mevzuat_tur_list` verilmezse yalnız `KANUN`, `KHK`, `CB_KARARNAME` ve `TUZUK` aranır; yanıt atlanan türleri `aranmayan_turler` alanında söyler. Yönetmelik, tebliğ veya kurum yönetmeliği arıyorsan türü açıkça yaz.

## 2. Kimlik disiplini

1. `mevzuat_no` resmî kanun numarasıdır (6698 KVKK, 6102 TTK, 6098 TBK, 213 VUK, 5237 TCK, 5271 CMK, 6100 HMK, 2577 İYUK, 4857 İş K., 3065 KDVK). Emin değilsen numarayı uydurma; önce `mevzuat_adi` ile ara, numarayı yanıttan al.
2. `mevzuat_id` sunucunun iç kimliğidir ve yalnız `mevzuat_ara` yanıtından gelir (`mevzuatgov:kanun:5:6698` biçimi). Kendin kurma; ortadaki tertip numarası tahmin edilemez. Eski sayısal kimlikler (`103161` gibi) çözümlenmez, `unsupported_legacy_id` alırsan yeniden ara.
3. Madde kimliği mevzuat kimliğinin madde ekli hâlidir (`mevzuatgov:kanun:5:6698:m6`). Normal numaralı maddelerde `mevzuat_getir(id=<mevzuat_id>, id_type="madde", madde_no=6)` tek çağrıda çözer. EK ve GEÇİCİ maddeler ayrı numara dizisi kullanır; onlarda önce `id_type="outline"` ile `madde_id` al.

## 3. Arama davranışı

1. `phrase` operatör almaz: tırnak, `+`, `-`, joker ve AND/OR/NOT birebir metin olarak aranır. Önce tam öbek denenir, sonuç yoksa kelimeler AND'lenir ve yanıt `note` ile bildirir. 2 ile 5 terim yaz; uzun sorgu sıfır sonuç verir.
2. Sıralama Resmî Gazete tarihine göredir, ilgi sıralaması yoktur. Hedefi öne çıkarmak için `mevzuat_adi` veya `mevzuat_no` ile daralt.
3. Resmî Gazete tarih filtresi yayım tarihine bakar, yürürlük tarihine değil. Yürürlüğü kanunun `Yürürlük` maddesinden ve değişiklik notlarından oku.
4. `mevzuat_icinde_ara` operatörleri BÜYÜK HARF ister ve kök kelime ister (`tazminat`, `tazminatı` değil): `"açık rıza" AND sağlık`, `(ihracat OR ithalat) AND NOT istisna`. Bitişik kelimeler AND sayılır. İsabetler tüm küme üzerinde sıralanır; ilk sayfa en güçlüsüdür. Her isabet `snippet` ve varsa `madde_id` ile `madde_no` taşır.
5. Tebliğler, Cumhurbaşkanlığı kararları ve genelgeler maddeye bölünmez; `madde` ve `outline` bunlarda `outline_desteklenmiyor` döner. Tam metni getir ya da `mevzuat_icinde_ara` kullan (tek tam metin eşleşmesi döner). Genelge ve karar PDF'leri ilk çağrıda OCR ile açılır, 2 ile 3 saniye sürebilir.
6. 50 KB üstü tam metin parçalanır: ilk çağrı `chunk: {index, total}` döndürür, kalanı `chunk: 2..total` ile al. Devasa kanunlarda tam metni çekmek yerine `mevzuat_icinde_ara` ile ilgili üç maddeyi bul.
7. Gerekçe yoktur; mevzuat.gov.tr yasama gerekçesi yayımlamaz. Gerekçe için TBMM kaynaklarına git.
8. Sayfalama parametresi `page`'dir; `ictihat_ara`'daki `pageNumber` ile karıştırma.

## 4. Tipik kullanım

Kanun numarasıyla madde:

```
mevzuat_ara(mevzuat_no="6098", mevzuat_tur_list=["KANUN"])
mevzuat_getir(id="mevzuatgov:kanun:5:6098", id_type="madde", madde_no=350)
```

Madde ağacı ve konu başlığı:

```
mevzuat_getir(id="mevzuatgov:kanun:5:6098", id_type="outline")
```

Kanun içinde boolean arama:

```
mevzuat_icinde_ara(mevzuat_id="mevzuatgov:kanun:5:4691", query="yazılım AND (ihracat OR \"hizmet ihracı\") AND istisna")
```

Konu araması, kanun numarası bilinmiyor:

```
mevzuat_ara(phrase="kişisel veri yurt dışı aktarım", mevzuat_tur_list=["KANUN", "YONETMELIK", "KKY", "TEBLIGLER"])
```

Yönetmelik ve tebliğ (tür açıkça verilir):

```
mevzuat_ara(mevzuat_adi="Kişisel Verilerin Silinmesi", mevzuat_tur_list=["KKY", "YONETMELIK"])
mevzuat_ara(phrase="veri ihlali bildirim", mevzuat_tur_list=["TEBLIGLER"])
```

Cumhurbaşkanlığı kararnamesi ve genelgesi:

```
mevzuat_ara(phrase="sermaye hareketleri", mevzuat_tur_list=["CB_KARARNAME"])
mevzuat_ara(phrase="kamu alımları", mevzuat_tur_list=["CB_GENELGE"])
```

Yürürlükten kalkmış kanun:

```
mevzuat_ara(mevzuat_no="765", mevzuat_tur_list=["MULGA"])
```

Belirli bir günün Resmî Gazete'si ve konsolide metne geçiş:

```
resmi_gazete_fihrist(tarih="2026-08-06")
resmi_gazete_getir(document_id="resmi_gazete:20260806/3.htm")
mevzuat_ara(mevzuat_no="<değiştirilen kanun>", mevzuat_tur_list=["KANUN"])
```

Resmî Gazete gün bazlıdır; konu araması yoktur. "Şu konuda ne yayımlandı" sorusu ya tarihle ya da `mevzuat_ara`'nın Resmî Gazete tarih filtresiyle yanıtlanır. RG metni yalnız değişiklik hükmüdür; yürürlükteki hâl için konsolide metne geç. İlan bölümü varsayılan kapalıdır; icra, tebligat ve ihale ilanları için `include_ilan: true` ver. Mükerrer sayı gün içinde sonradan çıkabilir; aynı gün tekrar sorabilirsin.

## 5. Atıf

```
[Mevzuat MCP, 6098 sayılı TBK m. 350, 05.09.2026]
[Mevzuat MCP, KVKK Uygulama Yönetmeliği m. 8, 05.09.2026]
[Resmî Gazete, 32.891, 06.08.2026]
```

Alanlar virgülle ayrılır. Araç çıktısında URL varsa eklenir; mevzuat maddeleri için URL uydurulmaz, belge adı ve madde numarasıyla atıf yapılır. Çekilmediyse `[model bilgisi, doğrulayın]`.

## 6. Sınırlar

1. Yargıtay, Danıştay ve AYM kararları bu araçlarda yoktur; `yargi-mcp-rehberi.md`.
2. Kurum kararları (BDDK, SPK, EPDK, KVKK Kurulu) mevzuat değildir; `kurum_karari_ara`.
3. Tasarı ve kanun teklifi aşamasındaki metinler yoktur; TBMM sitesi.
4. Belediye ve yerel idare düzenlemeleri sınırlıdır.
5. Her araç çağrısı 100 saniyede iptal edilir; dar tut, iptal olursa aynı sorguyu tekrarlama.

## 7. Birlikte kullanım

Bir hukuki soru çoğunlukla üç adımdır: `mevzuat_ara` ve `mevzuat_getir` ile ilgili madde ve fıkralar; `ictihat_ara` veya `semantik_ictihat_ara` ile o maddenin yargı yorumu; skill playbook'u ile sentez. Atıf etiketleri korunur.

*Son güncelleme: 05.09.2026. Araç listesi ve parametreler canlı bağlantıdan doğrulandı.*
