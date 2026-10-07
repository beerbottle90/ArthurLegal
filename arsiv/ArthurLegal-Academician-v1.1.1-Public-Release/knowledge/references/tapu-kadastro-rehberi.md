# Tapu-Kadastro — ArthurLegal Tapu (`tkgm_`) Kullanım Rehberi

> Araç adları, parametreler ve davranış 23.09.2026'da canlı uçtan (ArthurLegal MCP, `tkgm-mcp` 0.5.0) doğrulanmıştır.
> Kaynak: `github.com/beerbottle90/arthurlegal-mcp/tree/master/tkgm-mcp`. Tasarım ve sınırlar:
> `tkgm-mcp/docs/MANIFESTO.md`.

**Ne yapar.** Kullanıcı sohbette bir yer, bir koordinat ya da il, ilçe, mahalle ile ada ve parsel söyler; parsel TKGM
Parsel Sorgu'nun herkese açık verisinden canlı gelir. Sonra ölçü, ölçekli kroki, harita, parsel raporu ve dayanak
maddelerinin adresi üretilir. **Kullanıcıdan GeoJSON/KML dosyası isteme**; dosya yalnız kullanıcı kendiliğinden
getirirse okunur.

---

## 1. Araç adları: nerede hangi ad

| Ortam | Araçlar nasıl görünür |
|---|---|
| claude.ai (ArthurLegal MCP connector'ı) | `tkgm_` önekiyle: `tkgm_parsel_sorgula`, `tkgm_konumdan_parsel`, `tkgm_yer_bul`, `tkgm_parsel_raporu` … |
| Claude Desktop, ArthurLegal yerel kurulumu | Yerel **ArthurLegal Tapu** sunucusundan **öneksiz**: `parsel_sorgula`, `konumdan_parsel`, `yer_bul`, `parsel_raporu` … `tkgm_` araçları orada yerel köprüden aktarılmaz; tapu kaydı metni bilgisayardan çıkmaz |

Bu rehberde araçlar `tkgm_` önekiyle yazılır; Claude Desktop'ta öneki atarak kullan. Araç yoksa `status` çağır; araç
yokken parsel bilgisi, ölçü, kroki ya da harç tutarı **uydurma**.

## 2. Onay kartı (sohbet başına bir kez)

Bir sohbetteki ilk canlı çağrı (`tkgm_parsel_sorgula`, `tkgm_konumdan_parsel`, `tkgm_yer_bul`, getiren
`tkgm_parsel_raporu`) `onay_gerekli` ve bir `kart` döndürür. Kartı kullanıcıya **olduğu gibi** göster. Kabul ederse aynı
çağrıyı `onay=true` ile yinele ve o sohbetin sonraki canlı çağrılarında da `onay=true` gönder; kartı bir daha gösterme.
Kabul etmezse canlı sorgu yapma.

## 3. Parsel nasıl gelir

1. **Ada/parsel biliniyorsa:** `tkgm_parsel_sorgula(il, ilce, mahalle, ada, parsel)` ya da
   `tkgm_parsel_sorgula(metin="İstanbul Kadıköy Caferağa 123 ada 45 parsel")`. İl söylenmemişse ilçeden çıkarıp sen
   doldur (Kadıköy → İstanbul). Köy parsellerinde ada **0**'dır.
2. **Yer ya da adres biliniyorsa:** `tkgm_yer_bul(sorgu)` → adaylar (OpenStreetMap) → doğru adayla
   `tkgm_konumdan_parsel(enlem, boylam)`. Aday mahalle ya da ilçe gibi geniş bir yerse nokta rastgele bir parsele düşer:
   kullanıcıdan ada/parsel ya da kesin adres iste.
3. **Belirsizlik:** yanıt `belirsiz` ve `adaylar` taşırsa kullanıcıya sor, seçilen `mahalle_id` ile yinele (ada ve parsel
   yanıtta hazır). Tahminle seçme.
4. Her yol bir `ref` döndürür; `tkgm_parsel_raporu`, `tkgm_kroki`, `tkgm_harita`, `tkgm_geometri`,
   `tkgm_dayanak_koprusu` o `ref` ile çağrılır. claude.ai'de yanıttaki `ref_kodu` bellek düşse de parseli taşır.

**Hız ve sınırlar.** TKGM'ye tek sıra, dakikada en çok 30 istek (bütün kullanıcıların toplamı); aynı parsel bir gün
önbellekten gelir. Yanıt "sırası dolu" ya da "bekliyor" diyorsa belirtilen süreden önce yineleme, süreyi kullanıcıya
söyle. Aynı adada parsel numaralarını tek tek **tarama**: ardışık altı numarada ada bir saat kapanır. Toplu döküm yapılmaz.

## 4. Araçlar

| Araç | İş |
|---|---|
| `tkgm_baslangic` | Akış, sınırlar, kapsam dışı kalanlar (~300 token) |
| `tkgm_parsel_sorgula` | Canlı parsel: il/ilçe/mahalle + ada/parsel ya da serbest `metin` |
| `tkgm_konumdan_parsel` | Koordinattaki parsel (canlı) |
| `tkgm_yer_bul` | Yer adı/adres → en çok 5 koordinat adayı (OpenStreetMap) |
| `tkgm_parsel_raporu` | Tek parsel raporu (markdown): kimlik, ölçü, kenarlar, konum bağlantıları, hukuki işaretler; `konu` ile dayanak adresleri |
| `tkgm_geometri` / `tkgm_kroki` / `tkgm_harita` | Ölçü, A4 ölçekli SVG kroki, OpenStreetMap altlıklı harita |
| `tkgm_koridor_kesisim` | Hat + genişlik → parsel başına kesilen alan (irtifak, kamulaştırma ham verisi) |
| `tkgm_disa_aktar` / `tkgm_koordinat_donustur` | GeoJSON/KML/DXF/CSV; coğrafi ↔ ITRF96 TM 3° / UTM |
| `tkgm_tarife_kalemi` / `tkgm_harc_hesapla` | 2026 tapu harcı ve döner sermaye kalemi; ön hesap, her kalem kaynağıyla |
| `tkgm_dayanak_koprusu` | Uyuşmazlık konusuna göre dayanak madde adresleri ve hazır `tr_` çağrıları |
| `tkgm_parsel_oku` | Kullanıcının kendiliğinden getirdiği GeoJSON/KML |
| Yalnız yerel (Claude Desktop) | `tapu_kaydi_oku` (maskeli), `parsel_foyu` (Word), `portfoy_tablosu` (Excel), `arazi_3d` |

## 5. Tipik akışlar

- **"Şu parsel ne?"** `tkgm_parsel_sorgula` → kısa özet (nitelik, kayıtlı alan, konum bağlantısı, rejim uyarıları) →
  ayrıntı istenirse `tkgm_parsel_raporu(ref)`.
- **Dava dosyası (tapu iptal-tescil, ortaklığın giderilmesi, ecrimisil, önalım).** Parsel ve komşuları getirilir →
  `tkgm_kroki(ref, komsular)` → `tkgm_dayanak_koprusu(konu=…, ref=…)` → köprünün önerdiği `tr_mevzuat_madde_getir` ve
  `tr_ictihat_ara` çağrıları → yerelde `parsel_foyu`.
- **Kamulaştırma / irtifak güzergâhı.** Parseller tek tek getirilir → `tkgm_koridor_kesisim` → bedel hesabına girecek alan
  için yine harita mühendisi ölçüsü gerekir.
- **İşlem masrafı.** `tkgm_tarife_kalemi` → `tkgm_harc_hesapla`; tutarı yazarken `dayanak` ve `alinti` alanlarını da aktar.

## 6. Disiplin

- **Bilgi amaçlıdır.** Parsel Sorgu verisi resmî işlemde kullanılamaz; malik, şerh, beyan ve rehin **içermez**. Bunlar
  için kullanıcı kendi e-Devlet / Web Tapu kaydını alır (Claude Desktop'ta `tapu_kaydi_oku` maskeleyerek yapılandırır).
- **Kroki resmî belge değildir**; aplikasyon ya da röperli kroki yerine geçmez. Hesap alanı ile kayıtlı alan farkı bir
  işarettir, hata tespiti değildir (düzeltme 3402 s. K. m. 41 yolu ve kadastro kayıtlarıyla).
- **`tkgm_dayanak_koprusu` adres verir, metin vermez.** Maddeyi `tr_mevzuat_madde_getir` ile çekmeden alıntılama
  (madde doğrulama kapısı).
- **Atıf:** `[TKGM Parsel Sorgu, İl/İlçe/Mahalle ada/parsel, GG.AA.YYYY, bilgi amaçlı]`.
- **Meslek sırrı:** `tkgm_yer_bul` sorgusu OpenStreetMap'e gider; müvekkil adı, dosya numarası yazma. Ada/parsel taşınmazı
  tanımlar; kişiyi değil.

## 7. Kapsam dışı

| İstenen | Durum |
|---|---|
| Toplu indirme, güzergâh boyunca yüzlerce parsel | Yapılmaz: çağrı başına tek parsel, tarama deseni durdurulur |
| Malik/şerh bilgisini sunucunun çekmesi | Yapılmaz; yalnız kullanıcının kendi oturumundan aldığı belge |
| İmar durumu | Belediyelerin e-imar sistemleri ayrıdır; kapsamda değil |
