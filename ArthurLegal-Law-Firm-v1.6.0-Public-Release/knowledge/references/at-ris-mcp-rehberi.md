# Avusturya Hukuku — at-ris MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Avusturya federal mevzuatı **ve**
> OGH/VwGH/VfGH içtihadı tek uçta. **4 araç.**
>
> **BİRİNCİL kaynaktır.**
>
> **Neden var:** RIS külliyatını doğru arıyor ama **sıralamıyor** —
> `Suchworte=Aktiengesetz` 1.423 gerçek sonucu **alfabetik** döndürür, dolayısıyla
> Aktiengesetz'in kendisi ilk sayfada değildir (ilk üç: "2. Wohnrechts-
> änderungsgesetz" ve iki AB ortaklık anlaşması). Bu sunucu yanıtlamadan önce
> **BM25 ile yeniden sıralar**. İndeks/crawl gerekmez.

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint — geçici (canlı)** | `https://arbor-davidson-miscellaneous-runtime.trycloudflare.com/mcp` |
| **MCP endpoint — yerel** | `http://127.0.0.1:8813/mcp` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/at-ris-mcp` |
| **Sürüm** | `at-ris-mcp` v1.0.0 — 4 araç |

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


## 2. Araçlar (4) — bağlanınca otomatik keşfedilir

| Araç | Ne yapar |
|---|---|
| `search_legislation` | Mevzuat araması — `title` (kesin) ya da `terms` (tam metin, geniş). **`as_of` ile belirli tarihteki hâli** |
| `search_caselaw` | OGH · VwGH · VfGH · BVwG · LVwG içtihadı |
| `fetch_document` | Sonuçtaki `formats` (html/xml/rtf/pdf) URL'inden tam metin |
| `server_status` | Geçerli külliyat/mahkeme kodları + bilinen upstream tuzakları |

---

## 3. Uyulacak kurallar

**a) Sıralama bu sunucunundur, RIS'in değil.** `total_upstream` RIS'in gerçek
sonuç sayısıdır; gördüğün, o sayfanın **yeniden sıralanmış** üstüdür.

**b) 🔴 Rechtssatz ≠ karar.** OGH külliyatının büyük kısmı *Rechtssatz*'tır —
bir karar dizisinden soyutlanmış **hukuki ilke**, yargı kararı değil.
`doc_type: "Rechtssatz"` olan sonuç, kendisini uygulayan kararların listesini
(`decisions`) taşır. **Karara atıf gerekiyorsa oradan birini seç.** Test edilen
bir örnek 114 kararı kapsıyordu — "OGH şöyle karar verdi" demek yanlış olurdu.

**c) `Kurztitel` parametresini kullanma.** RIS onu **sessizce yok sayar**:
gönderirsen hata değil, **441.066 kayıt** (tüm külliyat) döner. Sunucu bunu hiç
göndermez; sen de isteme — başlık için `title` (Titel) kullan.

**d) Geçmiş işlem varsa `as_of` kullan.** Sorunun konusu geçmiş bir işlemse
kanunun **o tarihteki** hâli gerekir; bugünkü konsolide metin yanıltır.

**e) API v2.5 emekliye ayrıldı** (404). Bu sunucu v2.6 kullanır.

---

## 4. Atıf formatı

```
[AT Mevzuat — {Kurztitel} — {ELI} — GG.AA.YYYY]
[AT İçtihat — {mahkeme} — {Geschäftszahl} — {ECLI} — GG.AA.YYYY]
```
⚠️ ELI, Geschäftszahl ve ECLI'yi **çıktıdan birebir kopyala** — Avusturya dosya
numarası formatı elle kurulamaz.

---

## 5. Connector yoksa ne olur

Bu sunucu bağlı değilse **WebFetch yedeği** `avusturya-hukuku-rehberi.md` içindedir. Yedek yol
daha dar ve daha kırılgandır; o rehberdeki uyarıları uygula ve **atıfa
`(MCP kullanılmadı)` kaydını düş**.

---

*Sunucu: `github.com/beerbottle90/at-ris-mcp` · bağımlılıksız (yalnız Python standart
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 4 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
