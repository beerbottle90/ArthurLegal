# CourtListener (US Case Law) — Kullanım Rehberi (MCP)

> **Resmi MCP server VAR** — *CourtListener REST*, Free Law Project tarafından
> işletilir ve **Anthropic connector dizininde** listelidir. Bu rehber MCP
> kullanım prosedürünü tanımlar.
>
> **Durum:** ✅ Aktif. Auth: **OAuth 2.0** (Dynamic Client Registration —
> ön-kayıt gerekmez). claude.ai/Claude Code bağlantı kurarken yetkilendirmeyi
> natif yönetir; API anahtarı dosyaya yazılmaz. Tüm CourtListener kullanıcılarına
> API erişimi otomatik tanınır; yoğun kullanım için Free Law Project üyeliği.
> Birincil yargı çevresi Türkiye'dir; bu kaynak yalnızca ABD hukuku temas eden
> işlerde kullanılır (bkz. `karsilastirmali-hukuk-rehberi.md`).

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

**Bu rehber neden gerekli?**
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
| CourtListener REST API | https://www.courtlistener.com/api/rest/v4/ | WebFetch (token) |
| Google Scholar (case law) | https://scholar.google.com | Resmi olmayan |
| Free Law Project | https://free.law | Kurum |

---

## Versiyon disiplini

- Bu rehber **v1.6.0** (*Cross-Border Connectors*) ile eklendi.
- CourtListener REST araç listesi için Free Law Wiki teyit edilir:
  `https://wiki.free.law/c/courtlistener/help/api/mcp`.

---

*Son güncelleme: 22.05.2026 — v1.6.0. CourtListener REST entegrasyon prosedürü; OAuth, Anthropic connector dizininde.*
