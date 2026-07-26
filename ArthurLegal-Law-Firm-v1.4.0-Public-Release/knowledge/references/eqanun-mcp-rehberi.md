# Azerbaycan Mevzuatı — e-qanun MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.4.0).** Azerbaycan mevzuatı artık WebFetch
> kazımasıyla değil, Adalet Bakanlığı'nın (Ədliyyə Nazirliyi) resmî
> `api.e-qanun.az` veritabanını saran bir MCP sunucusu üzerinden okunuyor.
>
> **BİRİNCİL kaynaktır.** Doktrin araçlarının aksine buradan dönen bir akt
> hukukun kendisidir ve — **statüsü doğrulanmışsa** — bir sonucun dayanağı
> olabilir.
>
> **Kapsam uyarısı:** yalnız **mevzuat**. Azerbaycan içtihadı bu API'de YOK →
> `azerbaycan-hukuk-rehberi.md` (constcourt.gov.az, CODICES).

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint — uzak** | `https://<DEPLOY-FQDN>/mcp` ⟵ deploy sonrası doldur |
| **MCP endpoint — yerel** | `http://127.0.0.1:8020/mcp` |
| **Transport** | Streamable HTTP (`/mcp`, SSE-or-JSON) |
| **Auth** | **Yok** (upstream public) |
| **Sunucu kaynağı** | `github.com/beerbottle90/eqanun-api` |
| **Mimari** | Bağımlılıksız (yalnız Python stdlib) MCP sunucusu |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → MCP
endpoint URL'sini gir → auth "None". Araçlar bağlantı sonrası otomatik keşfedilir.
Tool isim prefiksi verdiğin connector adına göre üretilir — **prefiksi sabit
varsayma**, aşağıdaki base isimleri kullan.

> ⚠️ Host geçici bir tünel (`*.trycloudflare.com`) ise **her yeniden başlatmada
> değişir**; kalıcı pilot için adlandırılmış tünel veya sabit deploy gerekir.
> Bağlantı koparsa önce host'u yenile, sonra `azerbaycan-hukuk-rehberi.md`
> WebFetch yollarına düş.

---

## 1. Araçlar (6 adet)

| Araç | Ne yapar | Önemli parametreler |
|------|----------|---------------------|
| `search_acts` | Akt arama | `query`, `scope` (`title`\|`text`), `status` (`in_force`\|`cancelled`\|`all`), `exact`, `start`, `length` |
| `count_acts` | Yalnız sonuç sayısı — konuyu ucuza boyutlar | aynı filtreler |
| `get_act` | **Künye + STATÜ** + yürürlük tarihleri + `htmlUrl` | `act_id` |
| `get_act_fulltext` | Temiz tam metin, karakterle sayfalanır | `act_id`, `offset`, `max_chars` |
| `list_types` | Akt türü taksonomisi | — |
| `list_sections` | Üst düzey konu bölümleri | — |

---

## 2. ⚠️ STATÜ DOĞRULAMA — opsiyonel DEĞİL

**Bu rehberin var olma sebebi tek bir hata:** yürürlükten kalkmış bir aktı
yürürlükteymiş gibi göstermek. `search_acts` bunu sana söyleyemez; **yalnız
`get_act` söyler.**

Zorunlu sıra:

1. `search_acts(query, scope="title", status="in_force")` ile ara.
   Başlık araması zayıf dönerse `scope="text"`e genişlet (daha geniş, daha yavaş).
2. Dönen `id` ile **`get_act(id)`** çağır ve `statusName` alanını oku:
   - **`Qüvvədədir`** → yürürlükte.
   - **`Ləğv olunmuş`** → **yürürlükten kalkmış — DAYANAK YAPMA.** Ardıl aktı ara.
   - Yürürlük tarihini de kontrol et: bir akt yürürlükte olup **henüz
     uygulanabilir olmayabilir**.
3. Ancak bundan sonra `get_act_fulltext(id)` ile lafzı çek.
   Mecelleler büyüktür (Mülki Məcəllə ~1,96M karakter) → hepsini birden çekme,
   `offset` ile sayfala.
4. **Fiilen okuduğun maddeyi alıntıla.** Başlıktan parafraz yapma.

---

## 3. Dil — Azerbaycanca terimle ara

Külliyat Azerbaycancadır. İndeks maddenin **kendi dilindeki** kelimesini eşler,
çeviri yapmaz. Türkçe veya İngilizce sorgu eksik rapor eder.

| Konu | Azerbaycanca terim |
|---|---|
| Petrol | `neft` |
| Gaz | `qaz` |
| İş / emek | `əmək` |
| Vergi | `vergi` |
| Medeni | `mülki` |
| Toprak / arazi | `torpaq` |
| Yer altı serveti | `yerin təki` |
| Rekabet / antitröst | `antiinhisar` |
| Muhasebe | `mühasibat` |
| Gümrük | `gömrük` |

Diakritiksiz Türkçe klavye girişi genellikle yine eşleşir (`emek` → `Əmək`) ama
gerçek terimi tercih et.

---

## 4. Tipik kullanım

```
count_acts("neft və qaz", status="in_force")        # konuyu boyutla
search_acts("Əmək Məcəlləsi", scope="title", status="in_force")
get_act(<id>)                                        # ← STATÜ burada
get_act_fulltext(<id>, offset=0, max_chars=20000)    # sayfalı lafız
search_acts("transfer qiymətləri", scope="text")     # başlık zayıfsa tam metin
```

**Şirket bağlamında hangi kanunlar?**

| Azerbaycan Kanunu | Konu | Tipik bağlantı |
|---|---|---|
| Neft və qaz haqqında Qanun | Petrol/gaz rejimi | [ANA ORTAK] upstream hakları |
| Mülki Məcəllə | Medeni Kanun | [ANA ORTAK] ile sözleşmeler |
| Əmək Məcəlləsi | İş Kanunu | AZ'da istihdam edilen personel |
| Vergi Məcəlləsi | Vergi Kanunu | Transfer fiyatlandırması, intra-group |
| Mühasibat uçotu haqqında Qanun | Muhasebe | Intra-group mali raporlama |
| Antiinhisar Qanunu | Rekabet | Piyasa davranışı |

---

## 5. ATIF DİSİPLİNİ (zorunlu)

```
[AZ Mevzuat — e-qanun MCP — {belge adı} — id:{id} — {statü} — GG.AA.YYYY]
```

Örnek:
`[AZ Mevzuat — e-qanun MCP — Əmək Məcəlləsi — id:26559 — Qüvvədədir — 26.07.2026]`

- **Statü atıfın İÇİNDEDİR.** Okuyucu, aktın yürürlükte olduğunu yeniden
  kontrol etmeden görebilmeli.
- Araç döndürmediyse **UYDURMA** → `[model bilgisi — doğrulayın]`.
- Azerbaycanca metni alıntılarken **Türkçe çevirisini yanına koy** ve çevirinin
  **sana ait, resmî olmadığını** işaretle. Kritik metinde `[review]` flag.
- Çıktı **hukuki tavsiye değildir** — nitelikli avukat incelemesi için taslaktır.

---

## 6. Kapsam dürüstlüğü

Bu araç **mevzuat tutar.** Cevap gerçekte mahkemelerin o kuralı nasıl
uyguladığına dayanıyorsa:

> "İçtihat kontrol edilmedi — Azerbaycan Anayasa Mahkemesi kararları bu araçta
> yok. `azerbaycan-hukuk-rehberi.md` → constcourt.gov.az / CODICES."

**Kontrol edilmiş gibi ima etme.**

---

## 7. Diğer rehberlerle ilişki

| İhtiyaç | Kaynak |
|---|---|
| AZ mevzuat lafzı + statü | **bu MCP** (BİRİNCİL) |
| AZ Anayasa Mahkemesi kararı | `azerbaycan-hukuk-rehberi.md` (constcourt.gov.az, CODICES) |
| AZ enerji sektörü mevzuatı EN | `azerbaycan-hukuk-rehberi.md` (minenergy.gov.az) |
| AZ iş hukuku EN/RU | `azerbaycan-hukuk-rehberi.md` (NATLEX/ILO) |
| AZ hakkında akademik doktrin | `lex-scholar-rehberi.md` (İKİNCİL — AZ'de açık erişim hukuk dergisi yok, yalnız OpenAlex) |
| İmzalı AZ sözleşme emsali (PSA/JOA) | `resourcecontracts-rehberi.md` |
| TR mevzuat / içtihat | `mevzuat-mcp-rehberi.md`, `yargi-mcp-rehberi.md` |

---

## 8. Sınırlamalar

- **Yalnız mevzuat** — içtihat yok.
- Host geçici tünelse efemeral; bağlantı koparsa WebFetch yedeğine düş.
- Her araç çağrısı **100 saniyede iptal edilir** (platform limiti). Sorguyu dar
  tut: tek konu, makul `length`, tam metni `offset` ile sayfala. İptal olursa
  **aynı sorguyu tekrarlama** — böl ve hangi kısmın kapsanmadığını söyle.
- Resmî çeviri yok; Türkçe/İngilizce aktarım **senin çevirin** olarak işaretlenir.
- Yürürlük ≠ uygulanabilirlik: `Qüvvədədir` bir akt gelecekte yürürlüğe girecek
  olabilir — tarihi oku.

---

## Versiyon disiplini

- Bu rehber **v1.4.0** (*LC Digital Twin MCP Senkronu*) ile eklendi.
- Öncesinde AZ mevzuatı yalnız WebFetch ile okunuyordu ve `e-qanun.az` anti-bot
  koruması nedeniyle `cis-legislation.com` yedeğine düşülüyordu; MCP sunucusu
  resmî API'yi kullandığı için o kısıt ortadan kalktı.
- Araç listesi / API tuzakları için sunucu repo dokümantasyonu teyit edilir.

---

*Son güncelleme: 26.07.2026 — v1.4.0. e-qanun MCP — self-hosted, bağımlılıksız,
auth'suz. Companion skill: `skills/legal-research__skills.md` →
`/legal-research:az-mevzuat`.*
