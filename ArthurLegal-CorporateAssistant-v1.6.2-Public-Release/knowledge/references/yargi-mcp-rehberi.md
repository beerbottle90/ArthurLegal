# TR Legal MCP (yargi-mcp-pro): Yargı, AYM, AİHM ve Kurum Kararları Rehberi

> Bu rehber içtihat ve idari karar araçlarını anlatır. Mevzuat ve Resmî Gazete araçları `mevzuat-mcp-rehberi.md` içindedir; ikisi aynı connector'dır.
> Araç adları ve parametreler 05.09.2026'da canlı bağlantıdan doğrulanmıştır. `search_bedesten_unified`, `search_yargitay_decisions`, `search_gib_ozelge`, `search_anayasa_unified` gibi eski adlar artık yoktur; bu rehberde yalnız güncel adlar kullanılır.

## 0. Bağlantı

| Alan | Değer |
|------|-------|
| Endpoint | `https://yargi-mcp-pro-production.up.railway.app/mcp` |
| Auth | OAuth 2.0 (WorkOS); claude.ai ilk bağlantıda izin akışını yönetir |
| Kurulum | claude.ai, Settings, Connectors, Add custom connector; tek connector |
| Araç adı | claude.ai aracın önüne connector adını koyar; önek sabit varsayılmaz, aşağıdaki temel adlar kullanılır |
| Kaynak | saidsurucu/yargi-mcp (MIT) |

## 1. Araçlar

| Araç | Ne yapar | Kritik parametreler |
|---|---|---|
| `ictihat_ara` | Yargıtay, Danıştay, yerel hukuk, istinaf hukuk ve KYB kararlarında arama | `phrase` (Bedesten Solr diyalekti), `court_types`, `birimAdi`, `esas_no`, `karar_no`, `kararTarihiStart`, `kararTarihiEnd`, `pageNumber`, `page_size` (en çok 100), `include_snippets`, `sort_by` |
| `semantik_ictihat_ara` | Kavram araması; doğal dil sorguyu anlamla eşler | `query` (Türkçe cümle, operatörsüz), `court_types`, `birimAdi`, `karar_yil_start`, `karar_yil_end`, `limit` (en çok 50) |
| `aym_ictihat_ara` | Anayasa Mahkemesi: norm denetimi, bireysel başvuru, siyasi parti, Yüce Divan | `query` (düz kelime), `decision_type`, `esas_no`, `karar_no`, `basvuru_no`, `decision_date_start`, `decision_date_end` |
| `aihm_ictihat_ara` | AİHM kararları ve kabul edilebilirlik kararları (HUDOC) | `keywords`, `ulke` (varsayılan TUR), `dil`, `madde`, `ihlal`, `ihlal_yok`, `basvuru_no`, `dava_adi`, `onem_duzeyi`, tarih |
| `ictihat_getir` | Bir kararın tam metni (Bedesten, AYM `anayasa:<guid>`, AİHM `aihm:<itemid>`) | `documentId`, `page_number` (40.000 karakter üstü sayfalanır) |
| `kurum_karari_ara` | 15 idari kurumun kararlarında arama | `kurum` (zorunlu), `keywords`, kuruma özgü filtreler |
| `kurum_karari_getir` | Kurum kararının tam metni | `document_id` (ör. `gib:12345`), `page_number` |
| `spk_icinde_ara` | Bir SPK ilke kararı, rehberi veya bülteni içinde arama | `document_id`, `keywords` |
| `sigorta_dergi_icinde_ara` | Sigorta Tahkim Hakem Karar Dergisi sayısı içinde arama | `dergi_no` (1 ile 64), `keywords` |
| `reklam_bulten_icinde_ara` | Reklam Kurulu bülteni içinde arama | `bulten_no`, `keywords` |
| `legal_research_guide` | Sunucunun kendi araştırma kılavuzu (yaklaşık 6.000 kelime) | parametre yok; sohbette en fazla bir kez, o da yalnız diyalekt tereddüdünde |
| `udf_tiff_pdf_guide` | UYAP UDF, çok sayfalı TIFF ve PDF okuma kılavuzu | `topic`; yalnız o dosya türü işlenecekse |

`kurum` değerleri: `gib` (özelgeler), `btk`, `rekabet`, `uyusmazlik` (Uyuşmazlık Mahkemesi), `kik`, `sayistay`, `bddk`, `kvkk`, `sigorta` (Sigorta Tahkim), `reklam` (Reklam Kurulu bültenleri), `kdk` (Kamu Denetçiliği), `spk`, `tbb` (Barolar Birliği Disiplin Kurulu), `epdk`, `hsk`.

## 2. Üç arama diyalekti, birbirine taşınmaz

1. `ictihat_ara.phrase` Bedesten Solr'dır. Çıplak kelimeler arasındaki boşluk OR demektir: `etkin pişmanlık nitelikli dolandırıcılık` dört kelimenin birleşimini döndürür. Birden çok kavramı zorunlu kılmak için her birini `+` ile işaretle: `+"etkin pişmanlık" +"nitelikli dolandırıcılık"`. Tırnak tam öbek, `-` dışlama, büyük harf `AND`, `OR`, `NOT` ve parantez çalışır; joker, fuzzy ve yakınlık operatörü yoktur. Kullanıcının cümlesini yapıştırma; 2 ile 5 hukuki terim çıkar.
2. `aym_ictihat_ara.query` düz Türkçe kelime alır; operatör yok, tırnak operatör değil. Her ek kelime sonuç kümesini daraltır.
3. `aihm_ictihat_ara.keywords` HUDOC diyalektidir: boşluk AND demektir, tırnak tam öbek, büyük harf OR ve NOT ile parantez çalışır, alan sözdizimi (`:` `=`) reddedilir.
4. `semantik_ictihat_ara.query` operatör almaz; hukuki fikri tek cümleyle anlat (`kira sözleşmesinde tahliye taahhüdünün geçerlilik şartları`). Tek kelime çok geniştir, sohbet cümlesi gürültüdür.

Türkçe diyakritikler her diyalektte korunur (ç ş ğ ı İ ö ü).

## 3. Filtreler

Mahkeme türü: `court_types` varsayılanı `["YARGITAYKARARI", "DANISTAYKARAR"]`, yani yalnız yüksek mahkemeler. İstinaf için `ISTINAFHUKUK`, yerel için `YERELHUKUK`, Yargıtay Cumhuriyet Başsavcılığı kanun yararına bozma için `KYB` açıkça verilir. İstinaf kapsamı kısmidir; sıfır sonuç yokluğun kanıtı değildir.

Daire: `birimAdi` kod alır, ad değil. Yargıtay hukuk daireleri `H1` ile `H23`, ceza daireleri `C1` ile `C23`, Hukuk Genel Kurulu `HGK`, Ceza Genel Kurulu `CGK`, Büyük Genel Kurul `BGK`. Danıştay daireleri `D1` ile `D17`, İdari Dava Daireleri Kurulu `IDDK`, Vergi Dava Daireleri Kurulu `VDDK`, İçtihadı Birleştirme Kurulu `IBK`. Genel kurul kararı tek daire kararından ağırdır; çelişkide üst kurulu tercih et.

Dosya numarası: `esas_no` ve `karar_no` `YIL/SIRA` biçimindedir (`2025/13348`). Kullanıcı numara veriyorsa kelime araması yerine bunlarla hedefle; `court_types` ve gerekirse `birimAdi` ile birleştir.

Tarih: ISO `YYYY-MM-DD`, karar tarihine göre. Sayfalama `ictihat_ara`'da `pageNumber`, mevzuat araçlarında `page`; karıştırınca ilk sayfada takılırsın. `sort_by`: `phrase` varsa varsayılan ilgi sırası; kronoloji için `date`.

Snippet: önbellekteki kararlar ücretsiz `snippet` taşır; `include_snippets: true` en fazla 5 önbelleksiz üst sonucu kotasız getirir (PDF kararlar atlanır). Üst sonuçları elerken aç, geniş taramada kapalı tut; tam metni yalnız seçtiğin karar için `ictihat_getir` ile al.

`date_suspect: true` taşıyan bir tarihe güvenme; belgeyi getir ve tarihi metinden oku.

## 4. Tipik kullanım

İş davası içtihadı (Yargıtay 9. Hukuk Dairesi, 2023 ile 2024):

```
ictihat_ara(
  phrase="+\"işe iade\" +\"kıdem tazminatı\"",
  court_types=["YARGITAYKARARI"],
  birimAdi="H9",
  kararTarihiStart="2023-01-01",
  kararTarihiEnd="2024-12-31",
  include_snippets=true
)
```

AYM bireysel başvuru (mülkiyet hakkı, kamulaştırma):

```
aym_ictihat_ara(
  decision_type="bireysel_basvuru",
  query="mülkiyet hakkı kamulaştırma",
  decision_date_start="2023-01-01"
)
ictihat_getir(documentId="anayasa:<guid>")
```

KVKK Kurulu kararı ve Danıştay denetimi:

```
kurum_karari_ara(kurum="kvkk", keywords="veri ihlali bildirim 72 saat")
ictihat_ara(phrase="+KVKK +\"idari para cezası\"", court_types=["DANISTAYKARAR"], birimAdi="D10")
```

Rekabet Kurulu kararı (karar türü filtresiyle):

```
kurum_karari_ara(kurum="rekabet", keywords="petrol piyasası dikey entegrasyon", karar_turu="rekabet_ihlali")
```

GİB özelgesi ve Danıştay vergi dairesi:

```
kurum_karari_ara(kurum="gib", keywords="transfer fiyatlandırması ilişkili taraf", tarih_baslangic="2023-01-01")
kurum_karari_getir(document_id="gib:<id>")
ictihat_ara(phrase="+\"transfer fiyatlandırması\" +\"örtülü kazanç\"", court_types=["DANISTAYKARAR"], birimAdi="D4")
```

KİK kararı (ihale itirazı):

```
kurum_karari_ara(kurum="kik", keywords="elektrik üretim ihalesi", karar_tipi="uyusmazlik", tarih_baslangic="2024-01-01")
```

EPDK kurul kararı (piyasa filtresi; ilk arama 15 ile 25 saniye sürebilir, yalnız başlık ve açıklamada arar):

```
kurum_karari_ara(kurum="epdk", keywords="lisans iptal", karar_tipi="elektrik")
```

AİHM (Türkiye davalı, madde 10 ihlali, Türkçe çeviri satırı):

```
aihm_ictihat_ara(keywords="ifade özgürlüğü gazeteci", ihlal="10", dil="TUR", onem_duzeyi="1")
ictihat_getir(documentId="aihm:<itemid>")
```

Kavram araması ve doğrulama:

```
semantik_ictihat_ara(query="kira sözleşmesinde ihtiyaç sebebiyle tahliyede samimiyet ve zorunluluk şartı", limit=5)
```

Semantik sonuçtaki `related_quotes` terimleriyle `ictihat_ara`'yı yeniden çalıştır; atıf yapılacak kararı oradan doğrula. Boşluktan sonraki ilk semantik sorgu 20 saniye kadar sürebilir.

## 5. Kurum kararlarında bilinmesi gerekenler

1. `bddk`, `kvkk`, `sigorta` ve `reklam` dış web aramasıyla (Tavily) keşfedilir: yalnız `keywords`, tarih filtresi yok, tek sayfa; sorgu kelimeleri üçüncü tarafa gider. Bu dört kuruma müvekkil adı veya kişiyi tanımlayan ayrıntı yazılmaz. Sunucuda arama anahtarı yoksa `not_configured` döner; kullanıcıya söyle.
2. `sigorta` ve `reklam` sonuçları bir dergi sayısı veya bülten döndürür; içindeki kararı `sigorta_dergi_icinde_ara` ve `reklam_bulten_icinde_ara` ile bul.
3. `sayistay` ve `tbb` birebir öbek arar; kelimeler yan yana ve aynı sırada geçmeli, tek güçlü terim kullan.
4. `hsk` külliyatı anonimdir: taraf adı, esas ve karar numarası ve karar tarihi silinmiştir, tarih filtresi yoktur.
5. `btk`, `rekabet` ve `uyusmazlik` sonuçları belge içeriği taşımaz (PDF); belge metnini yalnız gerçekten gereken karar için `kurum_karari_getir` ile al.
6. Seçtiğin `kurum`'a ait olmayan bir filtre `invalid_params` döndürür (ör. `gib`'e `karar_turu`). Tarih filtresi yalnız `gib`, `kik`, `kdk`, `epdk` ve `btk`'de vardır.
7. `spk` için `arama_alani: "icerik"` belge PDF metninde arar; yüzlerce sayfalık rehberde bölümü `spk_icinde_ara` ile bul.

## 6. Atıf

Kararı yalnız o oturumda fiilen çektiysen etiketle; alanlar virgülle ayrılır:

```
[Yargı MCP, Yargıtay 9. HD, E. 2023/1234 K. 2024/567, 12.03.2024]
[Yargı MCP, Danıştay 13. D, E. 2022/456 K. 2023/789, 05.06.2023]
[Yargı MCP, AYM bireysel başvuru, B. No 2021/30620, 14.09.2023]
[Yargı MCP, Rekabet Kurulu, karar no 24-11/123-45, 28.02.2024]
[Yargı MCP, GİB özelge, no, GG.AA.YYYY]
[ECHR, dava adı, başvuru no, GG.AA.YYYY]
```

Araç çıktısında `source_url` varsa atıfa eklenir; yoksa URL uydurulmaz. Çekmediğin kararı çekmiş gibi gösterme; çekemiyorsan `[model bilgisi, doğrulayın]` veya `[UYAP/Lexpera, manuel doğrulayın]`.

## 7. Disiplin

1. Önce kanun, sonra karar: `mevzuat_ara` ile maddeyi bul, sonra o maddenin yorumunu ara. Karar bulunca atıf yaptığı maddenin güncel metnini, değişiklik notlarını ve geçici maddeleri kontrol et; kontrol edilmemiş içtihada dayanmak ağır hatadır.
2. Yürürlükten kaldırma önceki içtihadı kendiliğinden geçersiz kılmaz; eski kanun döneminde doğan uyuşmazlıklar geçici maddelerle o kanuna tabi olabilir. Lex mitior yalnız ceza hukuku ilkesidir (TCK m. 7).
3. İçtihadı Birleştirme kararlarının ayrı aracı yoktur; yayım tarihini biliyorsan `resmi_gazete_fihrist` ile o günün Yargı bölümünden bul, bilmiyorsan söyle.
4. Her araç çağrısı 100 saniyede iptal edilir ve hiçbir şey döndürmez; sorguyu dar tut, iptal olursa aynı sorguyu tekrarlama, böl ve hangi kısmın kapsanmadığını söyle.
5. Her araştırma kanun metni (mevzuat araçları), yargı veya idari yorum (bu rehber) ve şirket playbook'u üçgeninde sentezlenir.

## 8. [ŞİRKET ADI] için tipik başvurular

| Konu | Araç ve filtre |
|---|---|
| İş davası içtihadı (işe iade, kıdem, fazla mesai) | `ictihat_ara`, `birimAdi` `H9` veya `H22` |
| İş kazası tazminatı ve ceza boyutu | `ictihat_ara`, hukuk için `H10`, ceza için `C12`, genel kurul için `HGK` ve `CGK` |
| EPDK lisans iptali, enerji idari yargısı | `ictihat_ara`, `court_types` `DANISTAYKARAR`, `birimAdi` `D13`; kurul kararı için `kurum_karari_ara(kurum="epdk")` |
| SPK düzenlemesine itiraz | `ictihat_ara`, `D13` veya `D10`; ilke kararı için `kurum_karari_ara(kurum="spk")` |
| Rekabet Kurulu kararı ve Danıştay denetimi | `kurum_karari_ara(kurum="rekabet")`, sonra `ictihat_ara` `D13` |
| KVKK idari para cezası emsali | `kurum_karari_ara(kurum="kvkk")` |
| Vergi ve transfer fiyatlandırması | `kurum_karari_ara(kurum="gib")`, `ictihat_ara` `D3`, `D4`, `VDDK` |
| İhale itirazı | `kurum_karari_ara(kurum="kik")` |
| ÇED ve çevre cezası | `ictihat_ara`, `D14` ve `D10` |
| Bilirkişi raporuna itiraz, uzman görüşü | `ictihat_ara`, `HGK` ve ilgili hukuk dairesi |

## 9. Sınırlar

1. Karar metinleri özet değildir; uzun olabilir, sayfalıdır.
2. Bazı kararlarda gizli kısımlar karartılmıştır (özellikle KVKK ve AYM bireysel başvuru).
3. Yeni kararlar yayımdan sonra indekse girer; birkaç gün gecikme olabilir. 1990 öncesi kararlar eksik olabilir.
4. Araç metni getirir; içtihat ağırlığını ve güncelliğini sen değerlendirirsin.
5. Yerel ve istinaf kapsamı bölgeye göre değişir; yokluk kanıtı değildir.

*Son güncelleme: 05.09.2026. Araç listesi ve parametreler canlı bağlantıdan doğrulandı.*
