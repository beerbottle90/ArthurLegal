# ArthurLegal MCP (`tr_`): Yargı, AYM, Uyuşmazlık ve Kurum Kararları Rehberi

> Türkiye artık ArthurLegal MCP'nin içindedir: aynı connector, `tr_` öneki, kimlik doğrulama yok. Bu rehber içtihat, AYM, Uyuşmazlık Mahkemesi ve düzenleyici kurum araçlarını anlatır; mevzuat ve Resmî Gazete araçları `mevzuat-mcp-rehberi.md` içindedir.
> Araç adları ve parametreler 06.09.2026'da canlı uçtan (`arthurlegal-mcp.fly.dev/mcp`) doğrulanmıştır. `search_bedesten_unified`, `ictihat_ara`, `semantik_ictihat_ara`, `aym_ictihat_ara` gibi öneksiz adlar bu connector'da yoktur; her araç `tr_` ile başlar.

## 0. Bağlantı

| Alan | Değer |
|------|-------|
| Endpoint | `https://arthurlegal-mcp.fly.dev/mcp` (tek uç: Türkiye + 14 yargı çevresi) |
| Auth | Yok; adresi bilen herkes çağırabilir, kamuya açık kaynaklarda arar |
| Önek | `tr_` (23 araç). `status` tek çağrıda TR indeksini ve vektör durumunu verir |
| Kaynak | `github.com/beerbottle90/arthurlegal-mcp/tree/main/ArthurLegalTR` (MIT); uç bilgisi saidsurucu/yargi-mcp ve mevzuat-mcp'den (MIT), transport yeniden yazıldı |
| İlk çağrı | Karmaşık soruda `tr_hukuk_arastirma_rehberi` (hangi soru için hangi araç); kurum filtreleri için `tr_kurum_listesi` |

## 1. Araçlar

| Araç | Ne yapar | Kritik parametreler |
|---|---|---|
| `tr_ictihat_ara` | Yargıtay, Danıştay, yerel hukuk, istinaf hukuk ve KYB kararlarında arama (Bedesten) | `query` (Bedesten diyalekti), `courts` (`YARGITAYKARARI`, `DANISTAYKARAR`, `YERELHUKUK`, `ISTINAFHUKUK`, `KYB`; varsayılan ilk ikisi), `chamber` (daire kodu), `date_from`, `date_to` (ISO), `page`, `page_size` (en çok 10), `sort` |
| `tr_ictihat_getir` | Bir kararın tam metni, sayfalı | `document_id` (aramadan), `page`, `page_chars` |
| `tr_ictihat_semantik_ara` | Anahtar kelimeyle bulunan ilk kararları (en çok 10) çekip doğal dil sorusuna göre anlamsal sıralar | `query` (doğal dil cümle), `initial_keyword` (Bedesten'e gidecek 1 ile 3 terim), `courts`, `chamber`, `date_from`, `max_docs` (varsayılan 5; karar başına 4 saniye) |
| `tr_aym_ara` | Anayasa Mahkemesi norm denetimi veya bireysel başvuru | `query` (düz kelime), `kind` (`norm` veya `bireysel`), `page`, `page_size` |
| `tr_aym_getir` | AYM karar tam metni | `id` (aramadan, UUID), `kind`, `page` |
| `tr_uyusmazlik_ara` | Uyuşmazlık Mahkemesi kararları (adli, idari görev uyuşmazlığı) | `query`, `scope` (`All`, `EsasNo`, `KararNo`), `page` |
| `tr_uyusmazlik_getir` | Karar PDF metni | `document_url` (aramadan) |
| `tr_kurum_karari_ara` | Sekiz düzenleyici kurumun kararlarında arama, tek arayüz | `kurum` (zorunlu), `query`, kuruma özgü filtreler (aşağıda) |
| `tr_kurum_karari_getir` | Kurum kararı veya belgesi tam metni, sayfalı | `kurum`, `id` (aramadan), `page` |
| `tr_kurum_listesi` | Kurumlar, kapsamları, canlı veya yerel durumu, arama parametreleri | parametre yok |
| `tr_spk_bulten_icinde_ara` | Bir SPK haftalık bülteni içinde bölüm bazında arama | `bulten` (`2026/27` biçimi), `query`, `limit` |
| `tr_semantik_ara` | Yerel indekste hibrit arama (BM25, trigram, vektör): kurum kararları, SPK bültenleri, Sigorta Tahkim dergileri | `query`, `kurum` (daraltma), `mode` (`hybrid`, `lexical`, `semantic`, `fuzzy`), `limit`, `date_from`, `date_to` |
| `tr_belge_getir` | Yerel indeksteki belgenin tam metni | `ref` (semantik aramadan) |
| `tr_hukuk_arastirma_rehberi` | Sunucunun kendi yönlendirme kılavuzu | parametre yok; sohbette en çok bir kez |

`kurum` değerleri (06.09.2026): `rekabet` (Rekabet Kurulu), `epdk` (EPDK Kurul kararları), `spk` (SPK haftalık bültenleri), `bddk` (BDDK Kurul kararları), `kvkk` (KVK Kurulu karar özetleri), `btk` (BTK Kurul kararları), `gib` (GİB özelgeleri), `sigorta_tahkim` (Hakem Karar Dergisi).

Bu connector'da olmayanlar ve neden: KİK (EKAP v2 imzalı API 500 döndürüyor), Sayıştay (WAF her sorguya 418 veriyor), TÜRKPATENT (karar veritabanı yok, portal reCAPTCHA'lı), İSTAÇ (site erişilemez), AİHM, Reklam Kurulu, KDK, TBB, HSK (kapsam dışı). Bunlar için isteğe bağlı ikinci connector TR Legal MCP (yargi-mcp-pro, OAuth) kurulmuşsa oradaki `aihm_ictihat_ara` ve `kurum_karari_ara(kurum="kik" | "sayistay" | "reklam" | "kdk" | "tbb" | "hsk")` kullanılır; kurulu değilse kaynak WebFetch ile veya hiç çekilemez ve çıktıda "çekilmedi" denir. Çalışmayan kaynak çalışıyormuş gibi gösterilmez.

## 2. Arama diyalekti

1. `tr_ictihat_ara.query` Bedesten diyalektidir: çıplak kelimeler, `"tam öbek"`, `+zorunlu`, `-hariç`, büyük harf `AND`, `OR`, `NOT`; joker ve yakınlık operatörü yoktur. Kullanıcının cümlesini yapıştırma; 2 ile 5 hukuki terim çıkar ve kavramları `+` ile zorunlu kıl: `+"işe iade" +"kıdem tazminatı"`.
2. `tr_aym_ara.query` düz kelime alır; operatör yok. Her ek kelime kümeyi daraltır.
3. `tr_ictihat_semantik_ara.query` operatör almaz; hukuki fikri tek cümleyle anlat. `initial_keyword` Bedesten'e gider ve adayları belirler; anlamsal sıralama yalnız çekilen metinler üzerindedir, keşif aracı değildir.
4. `tr_semantik_ara.query` doğal dil; kelime paylaşmayan belgeyi de bulur. Yanıttaki `retrieval.semantic` alanı `off` ise sonuçlar anahtar kelime eşleşmesidir; `mode="semantic"` ile tekrar dene veya eş anlamlı terim kullan.

Türkçe diyakritikler korunur; klavyesiz yazılan `aydinlatma` da `aydınlatma`yı bulur (noktasız ı genişletmesi yalnız yerel indekste).

## 3. Filtreler

Mahkeme: `courts` varsayılanı Yargıtay ve Danıştay. İstinaf için `ISTINAFHUKUK`, yerel için `YERELHUKUK`, kanun yararına bozma için `KYB` açıkça verilir. İstinaf ve yerel kapsam kısmidir; sıfır sonuç yokluğun kanıtı değildir.

Daire: `chamber` kod alır: Yargıtay hukuk `H1` ile `H23`, ceza `C1` ile `C23`, `HGK`, `CGK`, `BGK`; Danıştay `D1` ile `D17`, `IDDK`, `VDDK`, `IBK`. Tam Türkçe ad da kabul edilir. Genel kurul kararı tek daire kararından ağırdır.

Dosya numarası: ayrı `esas_no` filtresi yoktur; numarayı tırnak içinde `query`'ye yaz (`"2023/1234"`) ve `courts` ile daralt.

Tarih: `date_from` ve `date_to` ISO `YYYY-MM-DD`, karar tarihine göre. Sayfalama `page`; `page_size` en çok 10 (Bedesten sınırı).

Hız sınırı: Bedesten IP başına 30 saniyede 10 istek kabul eder; sunucu istekleri 3,5 saniye aralıkla gönderir. Art arda 5'ten fazla arama yapma; `retry: true` gelirse birkaç saniye bekle. Karar listesi metin içermez: yorum yapmadan önce `tr_ictihat_getir` ile metni oku.

## 4. Kurum filtreleri

| `kurum` | Kapsam | Filtreler | `id` (getir) |
|---|---|---|---|
| `rekabet` | Rekabet Kurulu kararları, PDF metninde arama (10.368 karar) | `query`, `decision_type` (`birlesme_devralma`, `rekabet_ihlali`, `muafiyet_menfi_tespit`, `ozellestirme`, `diger`), `decision_number`, `decision_date`, `page` | `karar_id` |
| `epdk` | EPDK Kurul kararları ağacı: elektrik, doğal gaz, petrol, LPG, denetim (3.744 karar) | `query` (konu ve kategori satırında), `market`, `category` (`lisans`, `tarife`, `YEKDEM`), `decision_no`, `year`, `limit` | `documents[0].url` |
| `spk` | SPK haftalık bültenleri 2005 ile 2026 | `year`, `number`; bülten içi arama `tr_spk_bulten_icinde_ara` | bülten no `2026/27` |
| `bddk` | BDDK Kurul kararları, RG'de yayımlanan ve yayımlanmayan iki liste (962 karar) | `query` (başlıkta), `list` (`rg`, `diger`), `year`, `limit` | `id` (DokumanGetir kimliği) |
| `kvkk` | KVK Kurulu karar özetleri (291 özet) | `query`, `scan_pages` (canlı tarama son sayfalar; arşiv için `tr_semantik_ara`) | `id` (içerik kimliği) |
| `btk` | BTK Kurul kararları (1.904 karar) | `query`, `decision_no`, `decision_date`, `date_from`, `date_to`, `unit`, `page` | `pdf_url` |
| `gib` | GİB özelgeleri (18.000'den fazla) | `query`, `ozelge_no`, `kanun_id`, `date_from`, `date_to`, `page` | `ozelge_no` |
| `sigorta_tahkim` | Hakem Karar Dergisi, 66 sayı, 2010 ile 2026 (652 karar indeksli) | `query`, `issue` (sayı, varsayılan son), `limit` | `"<sayı>:<karar başlığı>"` |

Parantezli sayılar 06.09.2026 tarihli yerel indeks büyüklükleridir; canlı arama bunlarla sınırlı değildir, yerel indeksi `tr_semantik_ara` kullanır.

## 5. Tipik kullanım

İş davası içtihadı (Yargıtay 9. Hukuk Dairesi, 2023 ile 2024):

```
tr_ictihat_ara(
  query="+\"işe iade\" +\"kıdem tazminatı\"",
  courts=["YARGITAYKARARI"],
  chamber="H9",
  date_from="2023-01-01",
  date_to="2024-12-31"
)
tr_ictihat_getir(document_id="<document_id>")
```

AYM bireysel başvuru (mülkiyet hakkı, kamulaştırma):

```
tr_aym_ara(query="mülkiyet hakkı kamulaştırma", kind="bireysel")
tr_aym_getir(id="<uuid>", kind="bireysel")
```

KVKK Kurulu kararı ve Danıştay denetimi:

```
tr_kurum_karari_ara(kurum="kvkk", query="veri ihlali bildirim")
tr_semantik_ara(query="veri ihlali bildiriminin 72 saat içinde yapılmaması", kurum="kvkk", limit=5)
tr_ictihat_ara(query="+KVKK +\"idari para cezası\"", courts=["DANISTAYKARAR"], chamber="D10")
```

Rekabet Kurulu kararı (karar türü filtresiyle) ve tam metin:

```
tr_kurum_karari_ara(kurum="rekabet", query="dikey entegrasyon petrol", decision_type="rekabet_ihlali")
tr_kurum_karari_getir(kurum="rekabet", id="<karar_id>", page=1)
```

GİB özelgesi ve Danıştay vergi dairesi:

```
tr_kurum_karari_ara(kurum="gib", query="transfer fiyatlandırması ilişkili taraf", date_from="2023-01-01")
tr_kurum_karari_getir(kurum="gib", id="<ozelge_no>")
tr_ictihat_ara(query="+\"transfer fiyatlandırması\" +\"örtülü kazanç\"", courts=["DANISTAYKARAR"], chamber="D4")
```

EPDK Kurul kararı (piyasa ve kategori filtresi; ilk çağrı piyasa başına onlarca istek atar, sonra önbellek):

```
tr_kurum_karari_ara(kurum="epdk", query="lisans iptal", market="elektrik", category="lisans")
tr_kurum_karari_getir(kurum="epdk", id="<documents[0].url>")
tr_resmi_gazete_fihrist(date="<rg_date>")
```

SPK bülteni:

```
tr_kurum_karari_ara(kurum="spk", year=2026)
tr_spk_bulten_icinde_ara(bulten="2026/27", query="halka arz")
```

Sigorta Tahkim (tek sayı canlı, arşiv semantik):

```
tr_kurum_karari_ara(kurum="sigorta_tahkim", query="kasko", issue=66)
tr_semantik_ara(query="araç hasarında sigortacının ödeme yükümlülüğü", kurum="sigorta_tahkim", mode="semantic", limit=5)
tr_kurum_karari_getir(kurum="sigorta_tahkim", id="66:<karar başlığı>")
```

Kavram araması ve doğrulama:

```
tr_ictihat_semantik_ara(query="kira sözleşmesinde ihtiyaç sebebiyle tahliyede samimiyet şartı", initial_keyword="ihtiyaç tahliye samimiyet", courts=["YARGITAYKARARI"], max_docs=5)
```

## 6. Atıf

Kararı yalnız o oturumda fiilen çektiysen etiketle; alanlar virgülle ayrılır ve araç çıktısındaki `citation` alanı birebir kullanılır:

```
[ArthurLegal TR, Yargıtay 9. Hukuk Dairesi, E. 2023/1234, K. 2024/567, 12.03.2024]
[ArthurLegal TR, Danıştay 13. Daire, E. 2022/456, K. 2023/789, 05.06.2023]
[ArthurLegal TR, AYM, B. No: 2021/30620, 14.09.2023]
[ArthurLegal TR, Rekabet Kurulu, 28.02.2024 tarih ve 24-11/123-45 sayılı karar]
[ArthurLegal TR, EPDK, 18.06.2026 tarihli ve 14681 sayılı Kurul Kararı (RG 20.06.2026/33286)]
[ArthurLegal TR, GİB, GG.AA.YYYY tarih ve <no> sayılı özelge]
```

Araç çıktısında `source_url` varsa atıfa eklenir; yoksa URL uydurulmaz. Çekmediğin kararı çekmiş gibi gösterme; çekemiyorsan `[model bilgisi, doğrulayın]` veya `[UYAP/Lexpera, manuel doğrulayın]`.

## 7. Disiplin

1. Önce kanun, sonra karar: `tr_mevzuat_ara` ile maddeyi bul, sonra o maddenin yorumunu ara. Karar bulunca atıf yaptığı maddenin güncel metnini ve geçici maddeleri kontrol et.
2. Yürürlükten kaldırma önceki içtihadı kendiliğinden geçersiz kılmaz; geçici maddelere bak. Lex mitior yalnız ceza hukuku ilkesidir (TCK m. 7).
3. `error`, `upstream_blocked` veya `unavailable` alanı taşıyan yanıt boş sonuç değildir; kaynağın erişilemediğini söyle.
4. Özelge bağlayıcı değildir, idarenin görüşüdür. Rekabet, EPDK ve BDDK kararlarının RG'de yayımlandığını `tr_resmi_gazete_fihrist` ile teyit et.
5. Her araç çağrısı 100 saniyede iptal edilir ve hiçbir şey döndürmez; sorguyu dar tut, iptal olursa böl.
6. Her araştırma kanun metni (mevzuat araçları), yargı veya idari yorum (bu rehber) ve playbook üçgeninde sentezlenir.

## 8. Tipik başvurular

| Konu | Araç ve filtre |
|---|---|
| İş davası içtihadı (işe iade, kıdem, fazla mesai) | `tr_ictihat_ara`, `chamber` `H9` veya `H22` |
| İş kazası tazminatı ve ceza boyutu | `tr_ictihat_ara`, hukuk için `H10`, ceza için `C12`, genel kurul için `HGK` ve `CGK` |
| EPDK lisans iptali, enerji idari yargısı | `tr_kurum_karari_ara(kurum="epdk")`, sonra `tr_ictihat_ara` `courts` `DANISTAYKARAR`, `chamber` `D13` |
| SPK düzenlemesine itiraz | `tr_kurum_karari_ara(kurum="spk")` ve `tr_spk_bulten_icinde_ara`; sonra `tr_ictihat_ara` `D13` veya `D10` |
| Rekabet Kurulu kararı ve Danıştay denetimi | `tr_kurum_karari_ara(kurum="rekabet")`, sonra `tr_ictihat_ara` `D13` |
| KVKK idari para cezası emsali | `tr_kurum_karari_ara(kurum="kvkk")`, arşiv için `tr_semantik_ara(kurum="kvkk")` |
| Vergi ve transfer fiyatlandırması | `tr_kurum_karari_ara(kurum="gib")`, `tr_ictihat_ara` `D3`, `D4`, `VDDK` |
| Banka ve finans kuruluşu izinleri | `tr_kurum_karari_ara(kurum="bddk")` |
| Telekomünikasyon | `tr_kurum_karari_ara(kurum="btk")` |
| Sigorta tazminatı hakem kararı | `tr_kurum_karari_ara(kurum="sigorta_tahkim")` |
| Adli ve idari yargı görev uyuşmazlığı | `tr_uyusmazlik_ara` |
| ÇED ve çevre cezası | `tr_ictihat_ara`, `D14` ve `D10` |
| İhale itirazı (KİK), Sayıştay, AİHM, Reklam Kurulu | Bu connector'da yok; isteğe bağlı TR Legal MCP veya WebFetch, aksi hâlde "çekilmedi" |

## 9. Sınırlar

1. Karar metinleri özet değildir; uzun olabilir, sayfalıdır.
2. Bazı kararlarda gizli kısımlar karartılmıştır (KVKK, AYM bireysel başvuru).
3. Yeni kararlar yayımdan sonra indekse girer; birkaç gün gecikme olabilir.
4. Araç metni getirir; içtihat ağırlığını ve güncelliğini sen değerlendirirsin.
5. Yerel ve istinaf kapsamı bölgeye göre değişir; yokluk kanıtı değildir.
6. Yerel indeks (`tr_semantik_ara`) taranmış kadarıyla vardır; kapsamı `status` söyler.

*Son güncelleme: 06.09.2026. Araç listesi ve parametreler canlı uçtan doğrulandı.*
