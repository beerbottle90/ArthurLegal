# Hollanda Hukuku — nl-rechtspraak MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Hollanda içtihadı ve mevzuatı artık
> WebFetch kazımasıyla değil bu sunucu üzerinden okunuyor. **6 araç.**
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
| **MCP endpoint — geçici (canlı)** | `https://heroes-traveling-worcester-pierce.trycloudflare.com/mcp` |
| **MCP endpoint — yerel** | `http://127.0.0.1:8811/mcp` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/nl-rechtspraak-mcp` |
| **Sürüm** | `nl-rechtspraak-mcp` v1.0.0 — 6 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL'sini gir → auth "None".

> ⚠️ **Yukarıdaki `*.trycloudflare.com` adresi geçicidir** — sunucu her yeniden
> başlatıldığında **değişir** ve connector sessizce kırılır: tanım doğru görünür,
> çağrılar düşer. Kalıcı kullanım için Smithery deploy'u (repoda `smithery.yaml`
> hazır) veya adlandırılmış tünel gerekir. Araç çağrısı sessizce boş dönüyorsa
> **önce endpoint'in hâlâ geçerli olduğunu kontrol et.**

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

**İçtihat**

| Araç | Ne yapar |
|---|---|
| `search_caselaw` | **Yerel indekste** anahtar kelime/kavram araması — Hollanda içtihadını kelimeyle aramanın tek yolu |
| `browse_caselaw` | Resmî API'nin **gerçekten uyguladığı** filtrelerle gezinme: tarih, mahkeme, hukuk alanı, belge tipi |
| `get_decision` | ECLI ile tam metin + künye (mahkeme, tarih, dosya no, usul, hukuk alanı) |
| `list_vocabulary` | Filtre için kontrollü değerler: 4 hukuk alanı, 261 merci |

**Mevzuat**

| Araç | Ne yapar |
|---|---|
| `search_legislation` | KOOP SRU 2.0 — **gerçek upstream tam metin araması**, tüm külliyat |

**Durum**

| Araç | Ne yapar |
|---|---|
| `server_status` | İndeks boyutu, hangi tarih aralığı hangi derinlikte tarandı, semantik açık mı |

---

## 3. Uyulacak kurallar

**a) `browse_caselaw`'a anahtar kelime verme.** Sunucu bunu **reddeder** — çünkü
upstream onu yok sayıp 3,75 milyon kaydın tamamını "sonuç" gibi döndürür.
Kelimeyle arama `search_caselaw`'dur.

**b) İndeks kapsamı ≠ Hollanda hukukunun tamamı.** `search_caselaw` yanıtındaki
`index_coverage` alanı hangi tarih aralığının tarandığını söyler. **Bir kararın
bu sonuçlarda çıkmaması, var olmadığının kanıtı değildir.** Kapsam dışıysa
`browse_caselaw` ile tarih/mahkeme daraltıp `get_decision` ile tek tek oku.

**c) İçtihat ile mevzuat farklı davranır.** `search_legislation` **tüm** KOOP
külliyatını arar (indeks sınırı yok); `search_caselaw` yalnız yerel indeksi.

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
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 6 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
