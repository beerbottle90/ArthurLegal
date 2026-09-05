# Hollanda Hukuku — nl-rechtspraak MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Hollanda içtihadı ve mevzuatı artık
> WebFetch kazımasıyla değil bu sunucu üzerinden okunuyor. **5 araç** (artı ortak `status`).
>
> **BİRİNCİL kaynaktır.** Buradan dönen karar ya da kanun hukukun kendisidir.
>
> **Neden var:** Resmî Hollanda içtihat API'si 3.751.381 karar taşıyor ve
> **hiç serbest metin araması yok** — dahası, tanımadığı parametreleri
> **sessizce yok sayıyor**: `?q=energie` tüm külliyatı döndürür ve arama sonucu
> gibi görünür. Bu sunucu kendi indeksinde arar ve anahtar kelimeyi o API'ye
> **iletmeyi reddeder**.

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on dört yargı çevresi tek uçta) |
| **Araç öneki** | `nl_` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/nl-rechtspraak-mcp` |
| **Sürüm** | `nl-rechtspraak-mcp` v1.0.0 — 5 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL'sini gir → auth "None".

> ⚠️ **Araç öneki sabittir.** Bu sunucu artık ArthurLegal MCP toplayıcısının
> arkasında; araçları **`nl_`** önekiyle çağır. Önek connector adına göre
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

## 2. Araçlar (5 artı ortak `status`) — bağlanınca otomatik keşfedilir

**İçtihat**

| Araç | Ne yapar |
|---|---|
| `nl_search_caselaw` | **Yerel indekste** anahtar kelime/kavram araması — Hollanda içtihadını kelimeyle aramanın tek yolu |
| `nl_browse_caselaw` | Resmî API'nin **gerçekten uyguladığı** filtrelerle gezinme: tarih, mahkeme, hukuk alanı, belge tipi |
| `nl_get_decision` | ECLI ile tam metin + künye (mahkeme, tarih, dosya no, usul, hukuk alanı) |
| `nl_list_vocabulary` | Filtre için kontrollü değerler: 4 hukuk alanı, 261 merci |

**Mevzuat**

| Araç | Ne yapar |
|---|---|
| `nl_search_legislation` | KOOP SRU 2.0 — **gerçek upstream tam metin araması**, tüm külliyat |

**Durum**

| Araç | Ne yapar |
|---|---|
| `status` | İndeks boyutu, hangi tarih aralığı hangi derinlikte tarandı, semantik açık mı |

---

## 3. Uyulacak kurallar

**a) `nl_browse_caselaw`'a anahtar kelime verme.** Sunucu bunu **reddeder** — çünkü
upstream onu yok sayıp 3,75 milyon kaydın tamamını "sonuç" gibi döndürür.
Kelimeyle arama `nl_search_caselaw`'dur.

**b) İndeks kapsamı ≠ Hollanda hukukunun tamamı.** `nl_search_caselaw` yanıtındaki
`index_coverage` alanı hangi tarih aralığının tarandığını söyler. **Bir kararın
bu sonuçlarda çıkmaması, var olmadığının kanıtı değildir.** Kapsam dışıysa
`nl_browse_caselaw` ile tarih/mahkeme daraltıp `nl_get_decision` ile tek tek oku.

**c) İçtihat ile mevzuat farklı davranır.** `nl_search_legislation` **tüm** KOOP
külliyatını arar (indeks sınırı yok); `nl_search_caselaw` yalnız yerel indeksi.

**d) Metinsiz karar normaldir.** Rechtspraak, metnini yayımladığından çok daha
fazla kararın künyesini yayımlar. Boş gövde işaretlenir; davanın yokluğu değildir.

---

## 4. Atıf formatı

```
[NL İçtihat — {ECLI} — {mahkeme} — GG.AA.YYYY]
[NL Mevzuat — {kanun adı} — {identifier} — GG.AA.YYYY]
```
⚠️ **ECLI'yi asla elle kurma.** Aracın döndürdüğü `citation` alanından birebir
kopyala; bozuk ECLI sunucu tarafından **reddedilir**, tahmin edilmez.

---

## 5. Connector yoksa ne olur

Bu sunucu bağlı değilse **WebFetch yedeği** `hollanda-hukuku-rehberi.md` içindedir. Yedek yol
daha dar ve daha kırılgandır; o rehberdeki uyarıları uygula ve **atıfa
`(MCP kullanılmadı)` kaydını düş**.

---

*Sunucu: `github.com/beerbottle90/nl-rechtspraak-mcp` · bağımlılıksız (yalnız Python standart
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 5 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
