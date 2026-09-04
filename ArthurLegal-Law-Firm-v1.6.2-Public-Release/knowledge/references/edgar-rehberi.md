# SEC EDGAR — Kullanım Rehberi (WebFetch)

> **Resmi MCP server yok** — SEC EDGAR, WebFetch ile doğrudan `efts.sec.gov` /
> `data.sec.gov` / `www.sec.gov/Archives` uçlarından kullanılır.
>
> **Durum:** ✅ Açık erişim — API anahtarı gerekmez. Ancak SEC "fair access"
> politikası gereği **beyan edilmiş User-Agent header zorunludur** (aşağıda).
> Birincil yargı çevresi Türkiye'dir; bu kaynak yalnızca ABD hukuku (halka açık
> şirket beyanları, M&A/HSR, securities) temas eden işlerde kullanılır
> (bkz. `karsilastirmali-hukuk-rehberi.md`). Türk analoğu: `kap-esirket-webfetch-rehberi.md`.

---

## SEC EDGAR nedir?

**EDGAR** (Electronic Data Gathering, Analysis, and Retrieval) — ABD sermaye
piyasası düzenleyicisi **U.S. Securities and Exchange Commission (SEC)**
tarafından işletilen resmi beyan sistemi. ABD'de halka açık tüm şirketler
(yabancı ihraççılar — foreign private issuer — dahil) kayıt beyannamelerini,
dönemsel raporlarını ve özel durum bildirimlerini EDGAR'a elektronik verir.

**Kapsam:**
- Dönemsel raporlar: `10-K` (yıllık), `10-Q` (çeyreklik), `8-K` (özel durum — KAP bildirimi analoğu)
- Yabancı ihraççılar: `20-F` (yıllık), `6-K` (ara bildirim) — bazı TR/JP/CN grupları dahil (ör. Turkcell, CIK 1071321)
- M&A belgeleri: `S-4` (birleşme kayıt beyannamesi), `SC 13D/13G` (pay edinimi), `DEFM14A` (birleşme genel kurul çağrısı)
- Ekler (exhibits): `EX-2` (birleşme sözleşmesi), `EX-10` (önemli sözleşmeler — material contracts), `EX-21` (bağlı ortaklık listesi)
- Tam metin arama endeksi: **2001'den bu yana** verilen beyanlar + tüm ekleri

**ArthurLegal için neden gerekli?** ABD paketinde birincil kaynak kurumsal
beyan delili sağlar: birleşme duyurusu `8-K`'ları, `10-K` risk faktörlerindeki
antitrust/HSR (Hart-Scott-Rodino) dili, `EX-10` önemli sözleşme ekleri.
**Rekabet Gözcüsü** için karşı taraf / pazar bağlamı üretir (ABD'de işlem
gören bir grubun birleşme geçmişi, beyan edilmiş rekabet soruşturmaları) —
**yalnızca bağlam olarak: EDGAR verisi deterministik skora asla girmez.**

---

## Endpoint / URI şeması

**1. Tam metin arama (JSON API):**

```
https://efts.sec.gov/LATEST/search-index?q={sorgu}&forms={FORM}&startdt=YYYY-MM-DD&enddt=YYYY-MM-DD
```

| Parametre | Anlamı | Örnek |
|---|---|---|
| `q` | Arama terimi; tam ifade için `%22...%22` (tırnak) | `q=%22merger%20agreement%22` |
| `forms` | Form tipi filtresi | `forms=8-K` |
| `startdt` / `enddt` | Veriliş tarihi aralığı | `startdt=2025-01-01&enddt=2025-12-31` |

Dönen JSON'da her isabet için: `adsh` (accession number), `file_date`, `form`,
`display_names` (şirket + ticker + CIK), `file_type` (ör. `EX-99.1`), `items`
(8-K madde numaraları). Web arayüzü: `https://www.sec.gov/edgar/search/` —
API SSS: `https://www.sec.gov/edgar/search/efts-faq.html`. Boolean (`AND`,
`OR`, `-` hariç tutma), tam ifade ve wildcard desteklenir; doğal dil sorgusu
desteklenmez. **Endeks yalnızca 2001 sonrasını kapsar.**

**2. Yapılandırılmış beyan listesi (CIK bazlı JSON):**

```
https://data.sec.gov/submissions/CIK{10 haneli, sıfır dolgulu CIK}.json
```

Örnek: `https://data.sec.gov/submissions/CIK0001071321.json` (Turkcell).
`filings.recent` altında form tipi, accession number, veriliş tarihi ve ana
belge adı dizileri döner. XBRL finansal veri uçları
(`data.sec.gov/api/xbrl/companyfacts/...`) ayrıca mevcuttur (entegrasyon
öncesi doğrulanmalı).

**3. Belge arşivi:**

```
https://www.sec.gov/Archives/edgar/data/{CIK}/{accession-tiresiz}/{belge}
https://www.sec.gov/Archives/edgar/data/{CIK}/{accession-tiresiz}/{accession}-index.htm
```

**Zorunlu header (fair access):** Tüm otomatik erişimlerde SEC'in örnek
formatına uygun User-Agent beyan edilir:

```
User-Agent: Sirket/Uygulama Adi iletisim@alanadi.com
```

> ⚠️ Beyansız/varsayılan User-Agent ile `www.sec.gov` sayfaları **HTTP 403**
> dönebilir (13.08.2026'da doğrulandı). WebFetch 403 alırsa neden büyük
> olasılıkla budur; uygulama tarafında (Rekabet Gözcüsü dahil) header'ı
> açıkça ayarla. `efts.sec.gov` ve `data.sec.gov` uçları beyan edilmiş
> User-Agent ile sorunsuz JSON döndürür.

---

## Uygulamalı örnekler

**Örnek 1: 10-K risk faktörlerinde HSR/antitrust dili taraması (2025)**

```
WebFetch:
  url: "https://efts.sec.gov/LATEST/search-index?q=%22Hart-Scott-Rodino%22&forms=10-K&startdt=2025-01-01&enddt=2025-12-31"
  prompt: "İlk 10 isabeti listele: şirket adı (display_names), accession number
           (adsh), veriliş tarihi (file_date). Toplam isabet sayısını belirt."
```

Doğrulanmış çıktı örneği (çekim: 13.08.2026): 233 isabet; ilki
`VISHAY INTERTECHNOLOGY INC (VSH, CIK 0000103730)`, accession
`0000103730-25-000017`, veriliş 14.02.2025. Belge dizinine gitmek için:
`https://www.sec.gov/Archives/edgar/data/103730/000010373025000017/0000103730-25-000017-index.htm`

**Örnek 2: Yabancı ihraççı — Turkcell'in güncel 20-F'i**

Adım 1 — beyan listesi:

```
WebFetch:
  url: "https://data.sec.gov/submissions/CIK0001071321.json"
  prompt: "filings.recent içinden en güncel 20-F'in accessionNumber,
           filingDate ve primaryDocument değerlerini ver."
```

Adım 2 — belgenin kendisi (doğrulanmış: 20-F, accession `0001104659-26-044740`,
veriliş 17.04.2026):

```
WebFetch:
  url: "https://www.sec.gov/Archives/edgar/data/1071321/000110465926044740/tkc-20251231x20f.htm"
  prompt: "Risk Factors bölümünde rekabet hukuku / Rekabet Kurumu soruşturmalarına
           ilişkin beyanları özetle; bölüm başlıklarıyla birlikte aktar."
```

**Örnek 3: Birleşme 8-K'ları (bağlam taraması)**

```
WebFetch:
  url: "https://efts.sec.gov/LATEST/search-index?q=%22merger%20agreement%22&forms=8-K"
  prompt: "İsabetleri listele: şirket, accession, tarih, items alanı
           (1.01 = önemli sözleşme akdi)."
```

---

## Atıf disiplini

EDGAR beyanları **accession number + veriliş tarihi** ile anılır; oturumda
fiilen çekildiyse etiket:

```
[SEC EDGAR — {Şirket} {Form} — acc. {accession number} — veriliş GG.AA.YYYY — çekim: GG.AA.YYYY]
```

Örnek: `[SEC EDGAR — Turkcell 20-F — acc. 0001104659-26-044740 — veriliş 17.04.2026 — çekim: 13.08.2026]`

- Çekilmemiş bir beyan `[SEC EDGAR]` etiketi alamaz → `[model bilgisi — doğrulayın]`.
- Tam metin arama sonucu (isabet listesi) tek başına içerik atfı değildir;
  içerik ancak belgenin kendisi çekildiğinde aktarılır.
- Eval/test verisi hiçbir zaman atıf kaynağı olarak kullanılmaz.

---

## Lisans ve sınırlar

- **Kamu malı / public information:** ABD federal hükümet çalışması; SEC'in
  resmi beyanı (sec.gov Privacy Policy, "Website Dissemination", çekim
  13.08.2026): *"Information presented on sec.gov is considered public
  information and may be copied or further distributed by users of the web
  site without the SEC's permission. Please consider appropriate citation to
  the SEC as the source."* İstisna: SEC mührü/logoları ile "SEC" ve "EDGAR"
  tescilli markaları kullanılamaz.
- **Fair access politikası:** azami **10 istek/saniye** (IP bazlı; aşımda
  geçici engel), beyan edilmiş **User-Agent zorunlu**, botnet/kontrolsüz
  crawler yasak. Politika değişebilir — toplu iş öncesi güncel metni doğrula:
  `https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data`
- **Resmi dokümantasyon incedir:** tam metin arama API'sinin yayımlanmış
  resmi yanıt şeması yoktur — entegrasyon gözlemlenen davranışa göre
  sabitlenir (pin) ve alan adları (`adsh`, `display_names`, `items`...)
  değişikliğe karşı izlenir.
- **Tam metin endeksi 2001'den başlar** — daha eski beyanlar arşivde durur
  ama tam metin aranamaz; CIK/form bazlı tarama gerekir.
- **Beyanlar, beyan sahibinin ifadeleridir** — yargısal olarak tespit edilmiş
  vaka değildir. Bir 10-K'daki "soruşturma riski" ifadesi hukuki sonuç olarak
  değil, şirket beyanı olarak aktarılır.
- **Rekabet Gözcüsü sınırı:** EDGAR verisi yalnızca bağlam katmanındadır;
  deterministik skora hiçbir koşulda girmez.
- **Uygulama tarafı kütüphane:** `dgunning/edgartools` (**MIT lisansı**;
  13.08.2026 itibarıyla aktif geliştirme, 2.500+ yıldız) — AGPL lisanslı
  `sec-edgar-mcp`'ye permissive alternatif olarak tercih edilir.

---

## İlgili rehberler

- `us-legislation-rehberi.md` — ABD federal mevzuat (GovInfo); HSR Act, Securities Act statü zemini
- `courtlistener-rehberi.md` — ABD mahkeme kararları; beyanla anılan davanın yargısal kaydı
- `kap-esirket-webfetch-rehberi.md` — Türk analoğu (KAP özel durum açıklamaları); aynı "beyan ≠ tespit" disiplini
- `karsilastirmali-hukuk-rehberi.md` — yabancı hukuk kaynaklarının devreye girme koşulları

---

*Son güncelleme: 13.08.2026 — endpoint'ler, fair-access politikası, kamu malı beyanı ve örnek URL'ler canlı doğrulandı.*

---

## MCP connector olarak eklemek

**Bugünkü durum:** Bu kaynağın hazır bir MCP sunucusu **yoktur**; yukarıdaki
prosedür `WebFetch` ile çalışır ve bağlayıcı kurulumu gerektirmez. claude.ai'daki
"custom connector" **MCP tabanlıdır** — dolayısıyla bu kaynağı connector olarak
eklemek, önce REST ucunu bir MCP sunucusuyla sarmayı gerektirir.

Aşağıdaki bilgi o sarmalamayı yapabilmeniz içindir. **Hazır bir endpoint
verilmemiştir; olmayan bir adres yazmak yerine sarmalanacak sözleşme verilmiştir.**

### Sarmalanacak sözleşme

| Alan | Değer |
|---|---|
| **Base URL** | ``https://efts.sec.gov` (tam metin) · `https://data.sec.gov` · `https://www.sec.gov/Archives`` |
| **Auth** | **Yok**, ancak **beyan edilmiş `User-Agent` header ZORUNLU** (SEC fair-access) |
| **Hız sınırı** | **~10 istek/saniye** — aşımda engellenirsiniz |
| **Yanıt** | JSON |
| **Lisans** | **Kamu malı** (ABD federal hükümet eseri) |

**Açılacak araç yüzeyi:**

| Araç | Uç | Ne döndürür |
|---|---|---|
| `edgar_full_text_search` | `efts.sec.gov/LATEST/search-index?q=` | 2001'den bu yana beyanlarda tam metin arama (ek'ler dahil) |
| `edgar_get_submissions` | `data.sec.gov/submissions/CIK{cik}.json` | Bir ihraççının beyan geçmişi |
| `edgar_get_document` | `www.sec.gov/Archives/...` | Beyan veya ek belgenin kendisi |

> Sarmalayıcı **User-Agent header'ını zorunlu kılmalı** — header'sız çağrı SEC
> tarafından reddedilir. Bunu sunucu tarafında sabitle, istemciye bırakma.

### Kanıtlanmış sarma kalıbı

Bu ekosistemde üç MCP sunucusu (`eqanun-api`, `lex-scholar-api`,
`resourcecontracts-api`) tam olarak bu işi yapıyor: public bir REST API'yi
bağımlılıksız (yalnız Python stdlib) bir MCP sunucusuyla sarıyorlar. Kalıp:

- **Transport:** Streamable HTTP, `/mcp` yolunda (`x-ms-agentic-protocol:
  mcp-streamable-1.0` muadili; claude.ai için düz Streamable HTTP yeterli)
- **Auth:** yok (upstream public olduğu için)
- **Port:** her sunucu kendi portunda; bu kaynak için önerilen **`8040`**.
  Aynı porta ikinci sunucu başlatmak açıkça hata verir. Mevcut on sunucu artık
  tek bir toplayıcının (`arthurlegal-mcp`) içinde süreç içi yükleniyor, ayrı
  portlarda değil.
- **Araç adları:** yukarıdaki yüzeyi birebir yansıt; **jenerik ad kullanma**.
  Başka bir sunucuda aynı adda bir araç varsa istemci şemaları karıştırır ve
  çağrılar düşer — bu ekosistemde bir kez yaşandı (`search_articles` çakışması).

Referans uygulamalar: `github.com/beerbottle90/eqanun-api` ·
`github.com/beerbottle90/lex-scholar-api` ·
`github.com/beerbottle90/resourcecontracts-api` ·
`github.com/beerbottle90/de-eli-mcp`

### claude.ai'a bağlama (sunucu ayağa kalktıktan sonra)

1. Settings → Connectors → **Add custom connector**
2. MCP endpoint URL'sini gir (`https://<DEPLOY-FQDN>/mcp`)
3. Auth: **None**
4. Araçlar bağlantı sonrası otomatik keşfedilir. Tek sunucu olarak bağlarsan
   önek connector adına göre üretilir — **sabit varsayma**. ArthurLegal MCP
   toplayıcısına eklenirse önek orada sabitlenir (`edgar_` gibi).

> ⚠️ Geçici tünel (`*.trycloudflare.com`) kullanma: adres **her yeniden
> başlatmada değişir** ve connector sessizce kırılır — tanım doğru görünür,
> çağrılar düşer. Bu ekosistemde bir kez yaşandı; on sunucu bu yüzden kalıcı
> adresli tek bir deploy'a taşındı (`https://arthurlegal-mcp.fly.dev/mcp`).

**Sarmadan da çalışır.** Connector zorunlu değildir; yukarıdaki `WebFetch`
prosedürü bu kaynağın tam işlevini verir. Sarmalama, yapılandırılmış araç
çağrısı ve tekrarlanabilir parametre disiplini istendiğinde değer katar.
