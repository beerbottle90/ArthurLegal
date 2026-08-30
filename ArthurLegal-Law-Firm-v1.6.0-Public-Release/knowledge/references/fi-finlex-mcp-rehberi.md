# Finlandiya Hukuku — fi-finlex MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Finlex Akoma Ntoso külliyatı,
> **iki resmî dilde**. **5 araç.**
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
| **MCP endpoint — geçici (canlı)** | `https://consistent-headquarters-whom-jesus.trycloudflare.com/mcp` |
| **MCP endpoint — yerel** | `http://127.0.0.1:8815/mcp` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/fi-finlex-mcp` |
| **Sürüm** | `fi-finlex-mcp` v1.0.0 — 5 araç |

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
| `semantic` | Yoğun vektör (kosinüs) | ⚠️ yalnız `EMBEDDINGS_URL` tanımlıysa |

Üçü **Reciprocal Rank Fusion** ile birleşir. `EMBEDDINGS_URL` yoksa `hybrid`
sessizce lexical+fuzzy'ye düşer ve **yanıtta `semantic: "off"` der** — anahtar
kelime eşleşmesini kavramsal eşleşme gibi sunmaz.


## 2. Araçlar (5) — bağlanınca otomatik keşfedilir

| Araç | Ne yapar |
|---|---|
| `search_acts` | Yerel indekste tam metin araması; `language` ile tek dile daraltılabilir |
| `browse_year` | Bir yılın aktları, sayfa başına 5 (Finlex'in sabit sayfa boyutu). `get_act`'in istediği `{lang@version}` **buradan alınır** |
| `get_act` | Tek aktın tam metni |
| `recent_changes` | Finlex değişiklik akışı — düzenleme takibi + geçerli bir `{lang@version}` kaynağı |
| `server_status` | İndeks, kapsam, upstream tuzakları |

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

**c) 🔴 `{lang@version}` uydurma.** `get_act` `fin@20221099` gibi bir değer ister;
sondaki rakamlar sürüm damgasıdır. **`browse_year` ya da `recent_changes`
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
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 5 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
