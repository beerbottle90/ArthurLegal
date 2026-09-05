# Avusturya Hukuku — at-ris MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.6.0).** Avusturya federal mevzuatı **ve**
> OGH/VwGH/VfGH içtihadı tek uçta. **3 araç** (artı ortak `status`).
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
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on dört yargı çevresi tek uçta) |
| **Araç öneki** | `at_` |
| **Transport** | Streamable HTTP (`POST /mcp`) · stdio da destekli |
| **Auth** | **Yok** |
| **Sunucu kaynağı** | `github.com/beerbottle90/at-ris-mcp` |
| **Sürüm** | `at-ris-mcp` v1.0.0 — 3 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → endpoint
URL'sini gir → auth "None".

> ⚠️ **Araç öneki sabittir.** Bu sunucu artık ArthurLegal MCP toplayıcısının
> arkasında; araçları **`at_`** önekiyle çağır. Önek connector adına göre
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

## 2. Araçlar (3 artı ortak `status`) — bağlanınca otomatik keşfedilir

| Araç | Ne yapar |
|---|---|
| `at_search_legislation` | Mevzuat araması — `title` (kesin) ya da `terms` (tam metin, geniş). **`as_of` ile belirli tarihteki hâli** |
| `at_search_caselaw` | OGH · VwGH · VfGH · BVwG · LVwG içtihadı |
| `at_fetch_document` | Sonuçtaki `formats` (html/xml/rtf/pdf) URL'inden tam metin |
| `status` | Geçerli külliyat/mahkeme kodları + bilinen upstream tuzakları |

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
kütüphanesi), auth yok. Canlı test: 30.08.2026 — 3 araç, gerçek sorgularla
doğrulandı. Sürüm: v1.6.0 (yeni).*
