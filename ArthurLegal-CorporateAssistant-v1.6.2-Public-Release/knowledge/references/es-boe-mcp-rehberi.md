# İspanya Hukuku — es-boe MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** BOE konsolide mevzuatı ve günlük
> Resmî Gazete. **6 araç.**
>
> **BİRİNCİL kaynaktır.**
>
> **Neden var — erişim sorununu çözer:** BOE konsolide mevzuat API'si kamuya
> açık ve ücretsizdir ama `Accept: application/xml` başlığı **olmayan her isteği
> reddeder** (JSON ve `*/*` → 400). WebFetch özel başlık gönderemediği için
> **tüm konsolide külliyat agent'a görünmezdi.** Sunucu başlığı gönderir.
> Ayrıca liste endpoint'inde arama parametresi yoktur (`?query=` → 500), o
> yüzden arama yereldir.

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on yargı çevresi tek uçta) |
| **Araç öneki** | `es_` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/es-boe-mcp` |
| **Sürüm** | `es-boe-mcp` v1.0.0 — 6 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL'sini gir → auth "None".

> ⚠️ **Araç öneki sabittir.** Bu sunucu artık ArthurLegal MCP toplayıcısının
> arkasında; araçları **`es_`** önekiyle çağır. Önek connector adına göre
> değişmez — alttaki on sunucuda `get_act` beş ayrı şey demek, önek doğru
> yargı çevresine yönlendiren tek şeydir.


> 🔎 **Her arama yanıtı bir `retrieval` bloğu taşır:** hangi kanallar çalıştı,
> kaç belge indeksli, semantik arama gerçekten açık mı. **Bunu oku** — ince bir
> sonuç kümesini "konu kapandı" sanma.

---

## Arama mimarisi (altı sunucuda ortak)

| Kanal | Ne yapar | Her zaman var mı |
|---|---|---|
| `lexical` | SQLite FTS5 + BM25, diyakritiksiz; katı AND → prefix → OR merdiveni | ✅ |
| `fuzzy` | FTS5 trigram — alt dize / yazım hatası toleransı | ✅ |
| `semantic` | Yoğun vektör (kosinüs), **çok dilli** | ⚠️ `EMBEDDINGS_URL` gerekir |

Üçü **Reciprocal Rank Fusion** ile birleşir. `EMBEDDINGS_URL` yoksa `hybrid`
sessizce lexical+fuzzy'ye düşer ve **yanıtta `semantic: "off"` der** — anahtar
kelime eşleşmesini kavramsal eşleşme gibi sunmaz.

### ✅ Semantik kanal nasıl açılır (doğrulanmış kurulum, 30.08.2026)

Yerel, ücretsiz, API anahtarsız — **Ollama + `bge-m3`**:

```sh
ollama pull bge-m3                     # 1,2 GB, 100+ dil, 1024 boyut
export EMBEDDINGS_URL=http://127.0.0.1:11434/v1/embeddings
export EMBEDDINGS_MODEL=bge-m3
python crawl.py ... --embed            # mevcut indeksi vektörle
```

Ollama'nın `/v1/embeddings` ucu OpenAI uyumludur; sunucular olduğu gibi konuşur.

**Neden `bge-m3`:** bu paketin asıl ihtiyacı **diller arası** erişim — kullanıcı
Türkçe sorar, külliyat Felemenkçe/Lehçe/Fince/İspanyolca'dır. Tek dilli bir model
bunu yapamaz. Ölçülen ayrım (TR sorgu, çok dilli aday havuzu):

| | ortalama kosinüs |
|---|---|
| Kavramsal olarak **ilgili** (FI/PL/NL/ES karşılıkları) | **0,70** |
| **Alakasız** (aynı dillerde başka konu) | **0,41** |
| **ayrım** | **0,29** |

Canlı örnek — İrlanda Act'lerinde `"iklim değişikliği ve karbon emisyon hedefleri"`:

| Mod | İlk üç sonuç |
|---|---|
| `semantic` ✅ | Strategic Gas Reserve Act · Air Pollution (Amendment) Act · Environment (Miscellaneous Provisions) Act |
| `lexical` ❌ | Veterinary Medicinal Products · Road Traffic · Communications Regulation |

Lexical gürültü döndürüyor çünkü **Türkçe kelime İngilizce metinde geçmiyor**.
Diller arası soru soracaksan semantik kanal şart.

> ⚠️ **Model çok dilli değilse sunucu bunu anlayamaz.** `semantic: "on"` yalnız
> "bir uç yapılandırıldı" demektir, "doğru model seçildi" demek değildir. Tek
> dilli bir model bağlarsan skorlar düşük ve sonuçlar zayıf olur, ama durum
> bloğu yine `on` der. Model seçimi operatörün sorumluluğudur.

> 📌 **`score` alanı benzerlik değil, sıradır.** RRF sıra tabanlıdır
> (`1/(60+sıra)`), bu yüzden skorlar birbirine çok yakın çıkar (0,0164 · 0,0161 ·
> 0,0159). Sıralamayı oku, skor farkını "güven" gibi yorumlama.

## 2. Araçlar (6) — bağlanınca otomatik keşfedilir

| Araç | Ne yapar |
|---|---|
| `es_search_legislation` | Yerel indekste arama — **künye düzeyi** (başlık, resmî numara, bakanlık, tarih) |
| `es_get_act` | Konsolide akt künyesi + **ilga/iptal statü bayrakları** |
| `es_get_act_text` | **Konsolide** tam metin (değişiklikler uygulanmış) |
| `es_get_document` | Aktın **yayımlandığı hâli** (`consolidated: false` işaretli) |
| `es_get_daily_gazette` | Bir günde BOE'de yayımlanan her şey — düzenleme takibi |
| `status` | İndeks boyutu, kapsam, semantik durumu |

---

## 3. Uyulacak kurallar

**a) 🔴 İndeks madde metnini KAPSAMAZ.** Yalnız künye indekslidir (başlık, resmî
numara, bakanlık, tarih). Sebep: tek bir konsolide akt ~1 milyon karakterdir
(Ley de Sociedades de Capital 960.963). **348 bis maddesinin içindeki bir ifade
aranarak bulunamaz** — önce aktı bul, sonra `es_get_act_text` ile oku.

**b) 🔴 Konsolide ≠ yayımlandığı hâl.** `es_get_act_text` yürürlükteki (değişiklikler
uygulanmış) metni; `es_get_document` orijinal yayımı verir ve `consolidated: false`
işaretlidir. **As-published bir metni yürürlükteki hukuk diye atıflandırma.**

**c) Statüyü bildir.** Her akt BOE'nin kendi sinyallerini taşır:
`estatus_derogacion`, `estatus_anulacion`, `vigencia_agotada`. `vigencia_agotada:
true` ya da `estatus_derogacion: S` olan bir akt **yürürlükteki hukuk değildir**.
`only_in_force=true` ile aramada eleyebilirsin.

**d) Diyakritik gerekmez.** İndeks diyakritiksizdir — `sector electrico` sorgusu
*Sector Eléctrico*'yu bulur.

---

## 4. Atıf formatı

```
[ES Mevzuat — {metin adı} — {BOE-ID} — {statü} — GG.AA.YYYY]
```
`es_get_document` yolundan alındıysa `(BOE'de yayımlandığı hâli — konsolide değil)`
kaydını ekle. BOE-ID'yi elle kurma.

---

## 5. Connector yoksa ne olur

Bu sunucu bağlı değilse **WebFetch yedeği** `ispanya-hukuku-rehberi.md` içindedir. Yedek yol
daha dar ve daha kırılgandır; o rehberdeki uyarıları uygula ve **atıfa
`(MCP kullanılmadı)` kaydını düş**.

---

*Sunucu: `github.com/beerbottle90/es-boe-mcp` · bağımlılıksız (yalnız Python standart
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 6 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
