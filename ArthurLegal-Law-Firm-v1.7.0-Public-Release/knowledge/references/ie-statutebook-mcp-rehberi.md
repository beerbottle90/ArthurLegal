# İrlanda Hukuku — ie-statutebook MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Oireachtas'ın çıkardığı Act'ler,
> **madde düzeyinde**. **4 araç** (artı ortak `status`).
>
> **BİRİNCİL kaynaktır** — Act'ler için. İçtihat ve SI'lar kapsam dışıdır.
>
> **Neden var:** Irish Statute Book temiz, sunucu-render ELI belgeleri yayımlıyor
> ama **arama endpoint'i yok** (`/search` ve `/searchresults.html` 404). Bu
> sunucu Act gövdelerinin tamamını yerel indeksler — bir maddenin içindeki ifade
> **aranabilir** hâle gelir.

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on dört yargı çevresi tek uçta) |
| **Araç öneki** | `ie_` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/ie-statutebook-mcp` |
| **Sürüm** | `ie-statutebook-mcp` v1.0.0 — 4 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL'sini gir → auth "None".

> ⚠️ **Araç öneki sabittir.** Bu sunucu artık ArthurLegal MCP toplayıcısının
> arkasında; araçları **`ie_`** önekiyle çağır. Önek connector adına göre
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
| `ie_search_acts` | Act **gövdelerinde** tam metin araması (İspanya'nın aksine burada gövde indekslidir) |
| `ie_get_section` | Tek madde — hemen her hüküm sorusunun doğru aracı |
| `ie_get_act` | Act'in tamamı (uzunsa kesilir, işaretlenir) |
| `ie_list_year` | Bir yılda çıkan Act'ler, künyeleriyle |
| `status` | İndeks boyutu/kapsamı, semantik durumu |

---

## 3. Uyulacak kurallar

**a) 🔴 "As enacted" ≠ yürürlükteki hukuk.** Varsayılan her şey Act'in
**çıkarıldığı hâlidir**; sonraki değişiklikler uygulanmamıştır. Revised
(konsolide) külliyat ayrıdır ve **her Act'i kapsamaz**. Her yanıt hangi sürüm
olduğunu söyler — "as enacted" bir metni yürürlükteki hukuk diye **sunma**,
sunuyorsan bunu açıkça yaz.

**b) Act değil madde çek.** İrlanda Act'leri uzundur — Companies Act 2014
**1.448 madde**, ~106.000 karakter. Hüküm sorusunda `ie_get_section` kullan;
`ie_get_act` yalnız tüm enstrüman gerçekten gerekiyorsa.

**c) Kapsam: yalnız Act'ler.** Statutory Instrument (SI) ve içtihat bu sunucuda
**yok**. İrlanda kararı için `courts.ie` ya da BAILII gerekir —
⚠️ **CourtListener ABD içtihadıdır, İrlanda için kullanma.**

**d) İndeks kapsamını oku.** `index_coverage` taranan yıl aralığını verir.

---

## 4. Atıf formatı

```
[IE Mevzuat — {Act adı} {yıl} (No. {no}) s.{madde} — as enacted — GG.AA.YYYY]
```
Revised sürüm kullanıldıysa `as enacted` yerine `revised` yaz. Sürüm
belirtilmeyen İrlanda atıfı eksiktir.

---

## 5. Connector yoksa ne olur

Bu sunucu bağlı değilse **WebFetch yedeği** `irlanda-hukuku-rehberi.md` içindedir. Yedek yol
daha dar ve daha kırılgandır; o rehberdeki uyarıları uygula ve **atıfa
`(MCP kullanılmadı)` kaydını düş**.

---

*Sunucu: `github.com/beerbottle90/ie-statutebook-mcp` · bağımlılıksız (yalnız Python standart
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 4 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
