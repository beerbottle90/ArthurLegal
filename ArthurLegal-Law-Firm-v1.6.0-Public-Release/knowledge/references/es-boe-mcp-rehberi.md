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
| **MCP endpoint — geçici (canlı)** | `https://revenue-see-back-villas.trycloudflare.com/mcp` |
| **MCP endpoint — yerel** | `http://127.0.0.1:8816/mcp` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/es-boe-mcp` |
| **Sürüm** | `es-boe-mcp` v1.0.0 — 6 araç |

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


## 2. Araçlar (6) — bağlanınca otomatik keşfedilir

| Araç | Ne yapar |
|---|---|
| `search_legislation` | Yerel indekste arama — **künye düzeyi** (başlık, resmî numara, bakanlık, tarih) |
| `get_act` | Konsolide akt künyesi + **ilga/iptal statü bayrakları** |
| `get_act_text` | **Konsolide** tam metin (değişiklikler uygulanmış) |
| `get_document` | Aktın **yayımlandığı hâli** (`consolidated: false` işaretli) |
| `get_daily_gazette` | Bir günde BOE'de yayımlanan her şey — düzenleme takibi |
| `server_status` | İndeks boyutu, kapsam, semantik durumu |

---

## 3. Uyulacak kurallar

**a) 🔴 İndeks madde metnini KAPSAMAZ.** Yalnız künye indekslidir (başlık, resmî
numara, bakanlık, tarih). Sebep: tek bir konsolide akt ~1 milyon karakterdir
(Ley de Sociedades de Capital 960.963). **348 bis maddesinin içindeki bir ifade
aranarak bulunamaz** — önce aktı bul, sonra `get_act_text` ile oku.

**b) 🔴 Konsolide ≠ yayımlandığı hâl.** `get_act_text` yürürlükteki (değişiklikler
uygulanmış) metni; `get_document` orijinal yayımı verir ve `consolidated: false`
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
`get_document` yolundan alındıysa `(BOE'de yayımlandığı hâli — konsolide değil)`
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
