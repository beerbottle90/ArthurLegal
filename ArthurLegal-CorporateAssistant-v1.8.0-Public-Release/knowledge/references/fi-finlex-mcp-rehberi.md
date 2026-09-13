# Finlandiya Hukuku — fi-finlex MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Finlex Akoma Ntoso külliyatı,
> **iki resmî dilde**. **4 araç** (artı ortak `status`).
>
> **BİRİNCİL kaynaktır.**
>
> **Neden var:** API temiz ama tam metin araması yok, üç tuzağı var ve iki eşit
> yetkili dili. Sunucu `.akn` paketini açar, iki dili de indeksler ve sürüm
> kimliğinin uydurulmasını **engeller**.

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on dört yargı çevresi tek uçta) |
| **Araç öneki** | `fi_` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/fi-finlex-mcp` |
| **Sürüm** | `fi-finlex-mcp` v1.0.0 — 4 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL'sini gir → auth "None".

> ⚠️ **Araç öneki sabittir.** Bu sunucu artık ArthurLegal MCP toplayıcısının
> arkasında; araçları **`fi_`** önekiyle çağır. Önek connector adına göre
> değişmez — alttaki on dört sunucuda `get_act` beş ayrı şey demek, önek doğru
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
| `semantic` | Yoğun vektör (kosinüs), **çok dilli** | üretim ucunda Voyage `voyage-4-lite`; `status` ile doğrula |

Üçü **Reciprocal Rank Fusion** ile birleşir. `EMBEDDINGS_URL` yoksa `hybrid`
sessizce lexical+fuzzy'ye düşer ve **yanıtta `semantic: "off"` der** — anahtar
kelime eşleşmesini kavramsal eşleşme gibi sunmaz.

### Semantik kanal: üretim ucunda nasıl çalışır

Tek uçtaki sunucu Voyage AI `voyage-4-lite` (çok dilli, 1024 boyut) ile
yapılandırılmıştır ve beş yerel indeksin tamamı bu modelle vektörlenmiştir.
Kanalın o an açık olup olmadığını iki yerden oku: `status` çıktısındaki
`semantic` alanı ve her arama yanıtındaki `retrieval.semantic`. `off` ise sebep
`reason` alanında yazar (uç erişilemiyor, anahtar reddedildi, kota) ve sonuçlar
yalnız anahtar kelime eşleşmesidir; eş anlamlı ve hedef dildeki terimle ikinci
bir arama yap. Kendi makinende çalıştırıyorsan `EMBEDDINGS_URL`,
`EMBEDDINGS_MODEL` ve `EMBEDDINGS_API_KEY` ile herhangi bir OpenAI uyumlu
`/v1/embeddings` ucu (Voyage ya da Ollama + `bge-m3`) bağlanabilir; model
değişince indeks yeniden vektörlenir (`crawl.py --embed`).

**Neden çok dilli model:** bu paketin asıl ihtiyacı **diller arası** erişim — kullanıcı
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

## 2. Araçlar (4 artı ortak `status`) — bağlanınca otomatik keşfedilir

| Araç | Ne yapar |
|---|---|
| `fi_search_acts` | Yerel indekste tam metin araması; `language` ile tek dile daraltılabilir |
| `fi_browse_year` | Bir yılın aktları, sayfa başına 5 (Finlex'in sabit sayfa boyutu). `fi_get_act`'in istediği `{lang@version}` **buradan alınır** |
| `fi_get_act` | Tek aktın tam metni |
| `fi_recent_changes` | Finlex değişiklik akışı — düzenleme takibi + geçerli bir `{lang@version}` kaynağı |
| `status` | İndeks, kapsam, upstream tuzakları |

---

## 3. Uyulacak kurallar

**a) 🔴 İki külliyat vardır, karıştırma.**
- `statute-consolidated` — **değişiklikleri uygulanmış** metin. Çoğu soruda "hukuk" budur.
- `statute` — aktın **yayımlandığı hâli**, değişiklikler uygulanmamış.
Her yanıt hangisinden geldiğini söyler.

**b) İki resmî dil eşit yetkilidir.** Fince (`fin@`) ve İsveççe (`swe@`) metinler
aynı ölçüde bağlayıcıdır ve ikisi de indekslidir. Arama her ikisini de
döndürebilir; `lang` alanı hangisi olduğunu söyler — **bu hata değil, doğru
davranıştır.**

**c) 🔴 `{lang@version}` uydurma.** `fi_get_act` `fin@20221099` gibi bir değer ister;
sondaki rakamlar sürüm damgasıdır. **`fi_browse_year` ya da `fi_recent_changes`
çıktısından kopyala.** Uydurulan değer reddedilir — sunucu tahmin etmez.

**d) Bilinen upstream tuzakları** (sunucu üçünü de halleder, ama bilmen gerek):
`main.akn` XML değil **içinde `main.xml` olan bir ZIP paketidir**; `/list` bir
5 kayıtlık değişiklik akışıdır, külliyat değil; kök adres 403 verir ama
`/finlex/avoindata/v1/...` yolları çalışır.

---

## 4. Atıf formatı

```
[FI Mevzuat — {kanun adı} ({no}/{yıl}) — {akn_uri} — {statü} — GG.AA.YYYY]
```
⚠️ `akn_uri` ve statüyü çıktıdan birebir kopyala. Hangi dildeki ifadeye
dayandığını da belirt (fin / swe).

---

## 5. Connector yoksa ne olur

Bu sunucu bağlı değilse **WebFetch yedeği** `finlandiya-hukuku-rehberi.md` içindedir. Yedek yol
daha dar ve daha kırılgandır; o rehberdeki uyarıları uygula ve **atıfa
`(MCP kullanılmadı)` kaydını düş**.

---

*Sunucu: `github.com/beerbottle90/fi-finlex-mcp` · bağımlılıksız (yalnız Python standart
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 4 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
