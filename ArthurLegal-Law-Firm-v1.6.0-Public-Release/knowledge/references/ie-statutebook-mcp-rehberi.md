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
| **MCP endpoint — geçici (canlı)** | `https://retreat-secretariat-referred-testament.trycloudflare.com/mcp` |
| **MCP endpoint — yerel** | `http://127.0.0.1:8814/mcp` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/ie-statutebook-mcp` |
| **Sürüm** | `ie-statutebook-mcp` v1.0.0 — 5 araç |

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
| `search_acts` | Act **gövdelerinde** tam metin araması (İspanya'nın aksine burada gövde indekslidir) |
| `get_section` | Tek madde — hemen her hüküm sorusunun doğru aracı |
| `get_act` | Act'in tamamı (uzunsa kesilir, işaretlenir) |
| `list_year` | Bir yılda çıkan Act'ler, künyeleriyle |
| `server_status` | İndeks boyutu/kapsamı, semantik durumu |

---

## 3. Uyulacak kurallar

**a) 🔴 "As enacted" ≠ yürürlükteki hukuk.** Varsayılan her şey Act'in
**çıkarıldığı hâlidir**; sonraki değişiklikler uygulanmamıştır. Revised
(konsolide) külliyat ayrıdır ve **her Act'i kapsamaz**. Her yanıt hangi sürüm
olduğunu söyler — "as enacted" bir metni yürürlükteki hukuk diye **sunma**,
sunuyorsan bunu açıkça yaz.

**b) Act değil madde çek.** İrlanda Act'leri uzundur — Companies Act 2014
**1.448 madde**, ~106.000 karakter. Hüküm sorusunda `get_section` kullan;
`get_act` yalnız tüm enstrüman gerçekten gerekiyorsa.

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
