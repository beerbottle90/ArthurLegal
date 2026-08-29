# MCP Yol Haritası — durum: 6 sunucu YAZILDI ve test edildi

> **Güncelleme 30.08.2026:** Bu belge bir plan olarak başladı; artık büyük kısmı
> **uygulanmış** durumda. Altı yargı çevresi için ayrı ayrı MCP sunucusu yazıldı,
> canlı API'lere karşı test edildi ve GitHub'a yayımlandı. Lüksemburg maddesi ise
> **iptal edildi** — gerekçesi aşağıda.

---

## Yazılan sunucular

Hepsi ortak bir tasarımı paylaşır: **bağımlılıksız** (yalnız Python standart
kütüphanesi, `pip install` yok), **auth yok**, MCP JSON-RPC hem **stdio** hem
**Streamable HTTP** (`POST /mcp`) üzerinden, `/health` sağlık ucu ile.

| Sunucu | Yargı çevresi | Depo | Neden MCP gerekti | Araç |
|---|---|---|---|---|
| `nl-rechtspraak-mcp` | 🇳🇱 Hollanda | [repo](https://github.com/beerbottle90/nl-rechtspraak-mcp) | 3.751.381 karar **aranamıyordu**; API bilinmeyen parametreleri sessizce yok sayıyor | 6 |
| `pl-sejm-mcp` | 🇵🇱 Polonya | [repo](https://github.com/beerbottle90/pl-sejm-mcp) | API yalnız **başlık** arıyor; gövde ve konu araması yoktu | 6 |
| `at-ris-mcp` | 🇦🇹 Avusturya | [repo](https://github.com/beerbottle90/at-ris-mcp) | RIS arıyor ama **sıralamıyor** — sonuçlar alfabetik | 4 |
| `ie-statutebook-mcp` | 🇮🇪 İrlanda | [repo](https://github.com/beerbottle90/ie-statutebook-mcp) | Arama endpoint'i **yok** (`/search` 404) | 5 |
| `fi-finlex-mcp` | 🇫🇮 Finlandiya | [repo](https://github.com/beerbottle90/fi-finlex-mcp) | Tam metin araması yok + `.akn` ZIP paketi + `{lang@version}` tuzağı | 5 |
| `es-boe-mcp` | 🇪🇸 İspanya | [repo](https://github.com/beerbottle90/es-boe-mcp) | Konsolide külliyat `Accept` başlığı istiyor; WebFetch gönderemiyor | 6 |

### Arama mimarisi — üçü de her sunucuda

| Kanal | Ne yapar | Her zaman var mı |
|---|---|---|
| `lexical` | SQLite **FTS5 + BM25**, diyakritiksiz; katı AND → prefix → OR merdiveni | ✅ |
| `fuzzy` | FTS5 **trigram** — alt dize ve yazım hatası toleransı | ✅ |
| `semantic` | Yoğun vektör, kosinüs benzerliği | ⚠️ **yalnız yapılandırılırsa** |

Üç kanal **Reciprocal Rank Fusion** ile birleştirilir (BM25 sınırsız ve negatif,
kosinüs [-1,1] — skorlar doğrudan toplanamaz, sıra tabanlı birleştirme şart).

**Prefix merdiveni neden önemli:** Felemenkçe, Fince, Almanca ve Lehçe yoğun
bileşik kelime üretir. `kartel` tam kelime eşleşmesiyle `kartelverbod`'u bulmaz;
`kartel*` bulur. Sunucular önce kesin AND dener, boş dönerse prefix'e, o da
boşsa OR'a iner — kesinlik varken kesinliği korur, yokken kapsama düşer.

### Semantik arama — dürüst sınır

Standart kütüphane transformer çalıştıramaz. Yoğun vektör için dış uç gerekir:

```
EMBEDDINGS_URL=https://api.example.com/v1/embeddings
EMBEDDINGS_MODEL=text-embedding-3-small      # opsiyonel
EMBEDDINGS_API_KEY=...                       # opsiyonel
```

Yapılandırılmamışsa `mode="hybrid"` sessizce lexical+fuzzy'ye düşer ve **her
yanıtta bunu söyler** (`retrieval.semantic: "off"` + uyarı). Anahtar kelime
eşleşmesini asla kavramsal eşleşme gibi sunmaz.

⚠️ **Çok dillilik:** kullanıcı Türkçe sorar, külliyat Felemenkçe/Lehçe/Fince'dir.
Yapılandırılan modelin **kendisinin çok dilli olması** gerekir; tek dilli bir
model düşük skor üretir ama durum bloğu yine `semantic: on` der. Bunu sunucu
tespit edemez — operatörün sorumluluğudur.

### Ortak "yalan söyleme" disiplini

Her sunucu, denetimde yakalanan tuzakların aynısını kendi kullanıcısına
yaşatmamak için tasarlandı:

- **Sessizce yok sayılan parametre yok.** `nl-rechtspraak-mcp` `browse_caselaw`
  aracına anahtar kelime verilirse **reddeder** — çünkü upstream onu yok sayıp
  3,75 milyon kaydın tamamını "sonuç" gibi döndürür.
- **Boş indeks ≠ boş sonuç.** Her arama yanıtı `indexed_documents` ve
  `index_coverage` taşır; indeks boşsa açıkça hata verir.
- **Atıf uydurulmaz.** Her kayıt hazır `citation` alanı taşır; bozuk ECLI/BOE-ID/
  `lang@version` **reddedilir**, tahmin edilmez.
- **Konsolide ≠ yayımlandığı hâl.** IE `enacted`, ES `diario_boe`, FI `statute`
  ve PL statü alanları her yanıtta işaretlenir.

---

## ❌ İptal edilen: `lu-legilux-mcp` (Lüksemburg)

İlk taramada Legilux ELI URL'leri **HTTP 200** döndürdüğü için bu belgenin ilk
sürümü LU'yu `eli-search-mcp` kapsamına almıştı. **İkinci tur testte içerik
doğrulandığında yanlış olduğu görüldü:** her URL aynı **2.116 baytlık Angular
kabuğunu** ("no-script-warning") döndürüyor — hiç hukuki metin yok.

Denenen ve başarısız olan yollar: `/api/v1` (401) · `/sparql` (SPA) ·
`sitemap.xml` (404) · `/oai` (404) · `data.legilux` ELI (400) ·
`Accept: application/xml` ve `application/rdf+xml` içerik müzakeresi (yine kabuk).

> 📌 **Ders — bu denetimin en pahalı dersi:** *HTTP 200 "çalışıyor" demek
> değildir.* Bir kaynağı birincil ilan etmeden önce dönen içeriğin gerçekten
> hukuki metin olduğu doğrulanmalıdır. Bkz. `luksemburg-hukuku-rehberi.md`.

Lüksemburg şu an **İsrail ve BAE ile aynı kategoridedir**: resmî kaynak agent'a
kapalı, otomatik araştırma kapasitesi yok.

---

## Bekleyen: `ro-legislatie-mcp` (Romanya)

Yazılmadı, çünkü **ön koşulu sağlanmadı.**

`legislatie.just.ro` bu ortamdan bağlantıyı düşürüyor (TLS kuruluyor, istek
gidiyor, sunucu `close_notify` göndermeden kapatıyor); bağımsız ikinci bir
egress'ten "HTTP/2 framing layer" hatası geliyor.

⚠️ **MCP her egress engelini çözmez** — yalnız *bizim* ağımıza özgü olanı çözer.
Yazmadan önce, sunucunun koşacağı makineden şu doğrulanmalı:

```sh
curl -sS https://legislatie.just.ro/Public/DetaliiDocument/109884 | head -c 200
```

Gerçek metin dönerse sunucu yazılabilir; dönmezse sorun sitenin kendisindedir ve
MCP çözmez. O zamana kadar RO için çalışan yol **EUR-Lex CELLAR Romence tam
metin**'dir (`romanya-hukuku-rehberi.md` bölüm 1b).

---

## Dağıtım durumu

Altı depo da GitHub'da, `Dockerfile` + `railway.json` + `start.sh` ile hazır.

`start.sh` sunucuyu **hemen** başlatır ve indeks yoksa crawl'ı **arka planda**
çalıştırır — çünkü platform sağlık kontrolü crawl'ı beklerse deploy başarısız
olur. Doğrudan belge çekme ve gezinme indekssiz de çalışır.

```sh
docker build -t es-boe-mcp . && docker run -p 8000:8000 -e PORT=8000 es-boe-mcp
```

⚠️ **Railway dağıtımı yapılamadı:** hesabın deneme süresi dolmuş
("Your trial has expired. Please select a plan"). Plan seçimi bir faturalandırma
kararı olduğu için beklemede. Plan aktifleştikten sonra her depo için:

```sh
railway init --name <sunucu-adi> && railway up -d && railway domain
railway variables --set "CRAWL_ARGS=<crawl argumanlari>"
```

---

## Mevcut MCP'lerin sağlık durumu (30.08.2026 canlı test)

| MCP | Test | Sonuç |
|---|---|---|
| YargiMCP (TR) | `mevzuat_no=6698` · `+"rekabet yasağı" +"cezai şart"` | ✅ KVKK + 801 karar |
| e-qanun (AZ) | `search_acts("Mülki Məcəllə")` | ✅ 623 akt |
| OpenCaseLaw.ch | `Konkurrenzverbot…` court=bger | ✅ 57+ karar, pinpoint E. |
| Fedlex (CH) | `search_by_title("Obligationenrecht")` | ✅ RS 220 |
| de-eli (DE) | `de_search("Lieferkettensorgfaltspflichtengesetz")` | ✅ LkSG + ELI |
| CourtListener (US) | NY Convention araması | ✅ 242 opinion |
| LexScholar | TR rekabet yasağı | ✅ dergipark+doaj+openalex |
| ResourceContracts | `country=az`, Hydrocarbons | ✅ 16 PSA |

⚠️ **sbirka-mcp (CZ)** — endpoint canlı ama **401**; connector yetkilendirilmeden
Çekya rehberi çalışmaz.

---

*Oluşturuldu 30.08.2026 (v1.6.0). Altı sunucu yazıldıktan sonra güncellendi.
Sıralama ve gerekçeler canlı endpoint testlerine dayanır; yeni test yapıldıkça
güncellenmelidir.*
