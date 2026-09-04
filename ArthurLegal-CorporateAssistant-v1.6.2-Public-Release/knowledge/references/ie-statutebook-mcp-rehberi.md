# İrlanda Hukuku — ie-statutebook MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Oireachtas'ın çıkardığı Act'ler,
> **madde düzeyinde**. **5 araç.**
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
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on yargı çevresi tek uçta) |
| **Araç öneki** | `ie_` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/ie-statutebook-mcp` |
| **Sürüm** | `ie-statutebook-mcp` v1.0.0 — 5 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL'sini gir → auth "None".

> ⚠️ **Araç öneki sabittir.** Bu sunucu artık ArthurLegal MCP toplayıcısının
> arkasında; araçları **`ie_`** önekiyle çağır. Önek connector adına göre
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

## 2. Araçlar (5) — bağlanınca otomatik keşfedilir

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
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 5 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
