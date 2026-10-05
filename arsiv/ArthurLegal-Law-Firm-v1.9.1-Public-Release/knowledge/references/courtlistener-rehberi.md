# CourtListener (US Case Law) — Kullanım Rehberi (MCP)

> **Resmi MCP server VAR** — *CourtListener REST*, Free Law Project tarafından
> işletilir ve **Anthropic connector dizininde** listelidir. Bu rehber MCP
> kullanım prosedürünü tanımlar.
>
> **Durum:** ✅ Aktif. Auth: **OAuth 2.0** (Dynamic Client Registration —
> ön-kayıt gerekmez). claude.ai/Claude Code bağlantı kurarken yetkilendirmeyi
> natif yönetir; API anahtarı dosyaya yazılmaz. Tüm CourtListener kullanıcılarına
> API erişimi otomatik tanınır; yoğun kullanım için Free Law Project üyeliği.
> Bu kaynak yalnızca ABD hukuku temas eden işlerde kullanılır; ev yargı çevresi
> aktif entiteye göre belirlenir (bkz. `karsilastirmali-hukuk-rehberi.md` §1).

---

## CourtListener nedir?

**CourtListener** (courtlistener.com) — Free Law Project'in açık hukuk araştırma
platformu. ABD'nin en büyük açık mahkeme kararı arşivi.

**MCP üzerinden erişilen yetenekler:**

| Yetenek | İçerik |
|---|---|
| Case Law & Opinions | Milyonlarca ABD federal/eyalet mahkeme kararı (yüzyıllar geriye) |
| PACER Data | Federal dava dosyaları, taraflar, vekiller, dilekçeler |
| Citation Network | Atıf ağı — hangi karar hangisini atıf veriyor/alıyor |
| Oral Arguments | Federal istinaf mahkemeleri sözlü duruşma ses + transkript |
| Judicial Information | Hâkim biyografi/analitik verisi |
| Search | Anahtar kelime + doğal dil araması |
| Alerts | Yeni dosyalama/atıf/sorgu için gerçek-zamanlı izleme |
| **Citation Verification** | Atıfların geçerliliğini doğrular — **AI halüsinasyonu / uydurma içtihat önleme** |

**[Müvekkil] için neden gerekli?**
- **commercial / corporate:** İngiliz/NY hukuku yönetimli sözleşmelerde
  icra-edilebilirlik içtihat teyidi (örn. liability cap, indemnity yorumu).
- **ip:** ABD patent/marka/telif içtihatı (örn. *Alice* sonrası patentability).
- **litigation:** yabancı mahkeme kararı tanıma/tenfiz, sınır-ötesi uyuşmazlık.

---

## Bağlantı

**Claude Code:** İlgili plugin'lerin `.mcp.json` dosyasında tanımlı:
```jsonc
"CourtListener": { "type": "http", "url": "https://courtlistener.com/api/rest/v4/" }
```
İlk kullanımda OAuth izin akışı tetiklenir.

**Claude.ai Projects:** Customize → Connectors → **Browse Connectors** →
"CourtListener" (Anthropic dizininde) → Add → CourtListener hesabına yetki ver.
Custom connector elle eklemeye gerek yok.

---

## Citation verification — KRİTİK kullanım

CourtListener'ın en değerli işlevi **citation verification**'dır. Bir ABD
mahkeme kararına atıf yapılacaksa:

1. Atfı (örn. *Bilski v. Kappos*, 561 U.S. 593) CourtListener'da **doğrula**.
2. Karar gerçekten var mı, citation doğru mu, **overrule/abrogate edilmiş mi** kontrol et.
3. Doğrulanmadıysa **uydurma içtihat riski** → `[review]` + atıf yapma.

⚠️ Hiçbir ABD içtihatını "biliyorum" diye doğrulanmış gibi sunma. Citation
verification yapılmadan bir karara dayanan analiz `[CourtListener — doğrulanmadı]`
ile flag edilir.

---

## Kullanım kalıbı (Claude)

1. Soru ABD içtihatı gerektiriyor mu? (governing law ABD/eyalet ise evet.)
2. CourtListener REST ile ara (anahtar kelime veya doğal dil).
3. Bulunan kararın **holding**'ini oku — dicta, dissent veya reddedilen
   argümanı holding gibi sunma (quote-to-proposition kontrolü).
4. Atfı citation verification ile teyit et.
5. Çıktıda atıf etiketi koy.

---

## Atıf disiplini

ABD içtihatı oturumda fiilen CourtListener'dan çekildiyse:

```
[CourtListener — <mahkeme> — <taraflar, citation> — GG.AA.YYYY]
```

Örnek: `[CourtListener — SCOTUS — Alice Corp. v. CLS Bank, 573 U.S. 208 — 22.05.2026]`.

Çekmediğin/doğrulamadığın bir kararı `[CourtListener]` etiketleyemezsin →
`[model bilgisi — doğrulayın]`.

---

## Sınırlamalar

- **Yalnızca ABD** — İngiliz/AB içtihatı CourtListener'da yok (UK için
  `uk-legislation-rehberi.md` mevzuat verir, İngiliz case law için BAILII).
- **PACER kapsamı** — bazı PACER belgeleri ücretli/sınırlı; üyelik elevated erişim açar.
- **İçtihat ≠ mevzuat** — statü metni için `us-legislation-rehberi.md` (GovInfo).
- **ABD doktrini Türk hukukuna doğrudan uygulanamaz** — work-product,
  attorney-client privilege gibi kavramlar Türk hukukunda yoktur veya farklıdır.
  Bkz. `karsilastirmali-hukuk-rehberi.md`.

---

## Yedek kaynaklar (MCP erişilemezse)

| Kaynak | URL | Not |
|---|---|---|
| CourtListener (web) | https://www.courtlistener.com | Manuel arama |
| CourtListener REST API | https://www.courtlistener.com/api/rest/v4/ | ❌ **WebFetch ile kullanılamaz** — aşağıya bak |
| Google Scholar (case law) | https://scholar.google.com | Resmi olmayan |
| Free Law Project | https://free.law | Kurum |

---

## ⚠️ REST API WebFetch ile kullanılamaz — atıf doğrulaması MCP'den yapılır

30.08.2026 test: `POST /api/rest/v4/citation-lookup/` →
`{"detail":"Authentication credentials were not provided."}` (**401**).
Endpoint `Authorization: Token ...` başlığı ister; **WebFetch özel header gönderemez**,
dolayısıyla bu yol pratikte kapalıdır. (`/api/rest/v4/search/` GET'i token'sız 200
dönüyor ama alan filtresi ve sayfalama yok — güvenilir değil.)

**Atıf doğrulama ve çıkarımı MCP araçlarıyla yapılır:**

| İhtiyaç | MCP aracı |
|---|---|
| Metindeki ABD atıflarını bul | `extract_citations` |
| Atıfları çözümle + doğrula (geçerli mi, hangi karar) | `analyze_citations` |
| Uzun analizde kaldığı yerden devam | `resume_citation_analysis` |
| Karar/dava arama | `search` (`type="o"` opinion · `"r"` RECAP · `"d"` docket) |
| Tek kaydın tam alanları | `get_endpoint_schema` → `get_endpoint_item` |
| Karar tam metni | `read_document` / `search_document` |

⚠️ **Alan adı tuzağı:** `search` sonuçları camelCase döner (`caseName`, `dateFiled`,
`citation`); REST endpoint alanları snake_case'tir (`case_name`, `date_filed`,
`citations` — **çoğul**). Arama sonucundaki adı doğrudan `call_endpoint`'e taşıma;
önce `get_endpoint_schema` ile doğrula.

⚠️ **Token yolu istenirse:** CourtListener hesabından kişisel token alınıp connector'a
header olarak tanımlanması gerekir — bu pakette **yapılandırılmamıştır**. Connector
yokken ABD içtihadı için atıf üretme.

---

## Versiyon disiplini

- Bu rehber **v1.6.0** (*Cross-Border Connectors*) ile eklendi.
- CourtListener REST araç listesi için Free Law Wiki teyit edilir:
  `https://wiki.free.law/c/courtlistener/help/api/mcp`.

---

*Son güncelleme: 30.08.2026 — v1.6.1. `citation-lookup/` endpoint'inin WebFetch ile kullanılamadığı (401, header gerekiyor) canlı doğrulandı; atıf doğrulaması `analyze_citations` / `extract_citations` MCP araçlarına taşındı. camelCase/snake_case alan adı tuzağı eklendi. OAuth, Anthropic connector dizininde.*
