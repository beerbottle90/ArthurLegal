# Polonya Hukuku — pl-sejm MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Dziennik Ustaw ve Monitor Polski
> külliyatı bu sunucu üzerinden okunuyor. **6 araç.**
>
> **BİRİNCİL, statü doğrulamalı** — e-qanun (AZ) kalıbının aynısı.
>
> **Neden var:** Sejm ELI API'si iyi ama **yalnız başlık arıyor**; gövde ve konu
> araması yok. Bu sunucu, Sejm'in kendi kontrollü konu anahtarları üzerinden
> yerel indeks ekler ve değişiklik grafiğini yüzeye çıkarır.

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on yargı çevresi tek uçta) |
| **Araç öneki** | `pl_` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/pl-sejm-mcp` |
| **Sürüm** | `pl-sejm-mcp` v1.0.0 — 6 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL'sini gir → auth "None".

> ⚠️ **Araç öneki sabittir.** Bu sunucu artık ArthurLegal MCP toplayıcısının
> arkasında; araçları **`pl_`** önekiyle çağır. Önek connector adına göre
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
| `pl_search_by_title` | Canlı API'de **başlık** araması — akt adını biliyorsan en kesin yol |
| `pl_search_indexed` | **Yerel indeks**: başlık + akt tipi + çıkaran kurum + Sejm konu anahtarları. "Hangi kanun X'i düzenliyor" sorusu bunun |
| `pl_get_act` | Tam künye + **`references` değişiklik grafiği** + transpoze edilen AB direktifleri |
| `pl_get_act_text` | Metin (`html`) ya da PDF URL'i |
| `pl_list_year` | Bir yılda yayımlanan her şey — düzenleme takibi için |
| `status` | İndeks boyutu/kapsamı, semantik durumu |

---

## 3. Uyulacak kurallar

**a) Statü atıfın parçasıdır.** Her akt yayıncının kendi etiketini taşır:
`obowiązujący` = yürürlükte, `uchylony` = ilga. **Statüsüz Polonya atıfı eksik
atıftır.**

```
✅ [PL Mevzuat — Dz.U. 2024 poz. 1984 — obowiązujący — 30.08.2026]
❌ [PL Mevzuat — Dz.U. 2024 poz. 1984]
```

**b) `references` grafiğini oku.** `pl_get_act` yayıncının kendi ilişki adlarını
döndürür: `Akty zmieniające` (değiştiren aktlar), `Akty uchylone` (ilga edilenler),
`Akty wykonawcze` (uygulama aktları). Bir akt `obowiązujący` olup **defalarca
değiştirilmiş** olabilir — metni güncel saymadan önce grafiğe bak.

**c) Hiçbiri madde metnini aramaz.** Polonya aktlarının çoğu **yalnız PDF**
(`textHTML: false`), dolayısıyla indekslenecek HTML gövde yok. Madde düzeyi iş
için aktın PDF'ini aç.

**d) İki aramanın erişimi farklıdır.** `pl_search_by_title` canlı API'yi (yalnız
başlık), `pl_search_indexed` yerel indeksi (başlık + konu) tarar. `coverage`
alanını kontrol et.

---

## 4. Atıf formatı

```
[PL Mevzuat — {displayAddress} — {status} — {başlık} — GG.AA.YYYY]
```
⚠️ `displayAddress` (ör. `Dz.U. 2024 poz. 1984`) ve `status` alanlarını **API
çıktısından birebir kopyala** — Dz.U. numarasını elle kurma.

---

## 5. Connector yoksa ne olur

Bu sunucu bağlı değilse **WebFetch yedeği** `polonya-hukuku-rehberi.md` içindedir. Yedek yol
daha dar ve daha kırılgandır; o rehberdeki uyarıları uygula ve **atıfa
`(MCP kullanılmadı)` kaydını düş**.

---

*Sunucu: `github.com/beerbottle90/pl-sejm-mcp` · bağımlılıksız (yalnız Python standart
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 6 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
