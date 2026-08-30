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
| **MCP endpoint — geçici (canlı)** | `https://pointed-emerald-prisoners-agreement.trycloudflare.com/mcp` |
| **MCP endpoint — yerel** | `http://127.0.0.1:8812/mcp` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/pl-sejm-mcp` |
| **Sürüm** | `pl-sejm-mcp` v1.0.0 — 6 araç |

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
| `search_by_title` | Canlı API'de **başlık** araması — akt adını biliyorsan en kesin yol |
| `search_indexed` | **Yerel indeks**: başlık + akt tipi + çıkaran kurum + Sejm konu anahtarları. "Hangi kanun X'i düzenliyor" sorusu bunun |
| `get_act` | Tam künye + **`references` değişiklik grafiği** + transpoze edilen AB direktifleri |
| `get_act_text` | Metin (`html`) ya da PDF URL'i |
| `list_year` | Bir yılda yayımlanan her şey — düzenleme takibi için |
| `server_status` | İndeks boyutu/kapsamı, semantik durumu |

---

## 3. Uyulacak kurallar

**a) Statü atıfın parçasıdır.** Her akt yayıncının kendi etiketini taşır:
`obowiązujący` = yürürlükte, `uchylony` = ilga. **Statüsüz Polonya atıfı eksik
atıftır.**

```
✅ [PL Mevzuat — Dz.U. 2024 poz. 1984 — obowiązujący — 30.08.2026]
❌ [PL Mevzuat — Dz.U. 2024 poz. 1984]
```

**b) `references` grafiğini oku.** `get_act` yayıncının kendi ilişki adlarını
döndürür: `Akty zmieniające` (değiştiren aktlar), `Akty uchylone` (ilga edilenler),
`Akty wykonawcze` (uygulama aktları). Bir akt `obowiązujący` olup **defalarca
değiştirilmiş** olabilir — metni güncel saymadan önce grafiğe bak.

**c) Hiçbiri madde metnini aramaz.** Polonya aktlarının çoğu **yalnız PDF**
(`textHTML: false`), dolayısıyla indekslenecek HTML gövde yok. Madde düzeyi iş
için aktın PDF'ini aç.

**d) İki aramanın erişimi farklıdır.** `search_by_title` canlı API'yi (yalnız
başlık), `search_indexed` yerel indeksi (başlık + konu) tarar. `coverage`
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
