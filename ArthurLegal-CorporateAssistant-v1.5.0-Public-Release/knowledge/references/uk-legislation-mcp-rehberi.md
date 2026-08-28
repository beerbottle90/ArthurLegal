# UK Legislation MCP (legislation-mcp-ts) — Kullanım Rehberi (MCP yöntemi)

> ✅ **Resmî MCP server VAR** — `legislation-mcp-ts`, legislation.gov.uk'nin
> işletmecisi **The National Archives** tarafından yayımlanan resmî MCP
> sunucusudur. 14 yargı çevresi içinde kaynağın **kendi operatörünün** MCP
> sunduğu ilk örnek budur.
>
> **Durum:** ✅ Açık erişim — çekirdek araçlar için **API anahtarı gerekmez**
> (yalnızca opsiyonel Research API / semantik arama katmanları kimlik ister).
> Self-hosted, **loopback stdio** süreci olarak çalıştırılır.
>
> Birincil yargı çevresi Türkiye'dir; bu kaynak yalnızca İngiliz hukuku temas
> eden işlerde kullanılır (bkz. `karsilastirmali-hukuk-rehberi.md`). Bu rehber,
> `uk-legislation-rehberi.md` (WebFetch yöntemi) rehberini **tamamlar**; URI
> şeması ve tür kodları tabloları orada durur, burada tekrarlanmaz.

---

## legislation-mcp-ts nedir?

**legislation-mcp-ts** — The National Archives'ın (TNA) legislation.gov.uk
verisi için yayımladığı, TypeScript ile yazılmış **resmî Model Context
Protocol sunucusu**. Kaynak: `github.com/legislation/legislation-mcp-ts`.

**Kapsam:**
- UK mevzuatında anahtar kelime + metadata filtreli arama (`search_legislation`)
- Tam metin çekme — text / XML (CLML) / HTML / Akoma Ntoso (`get_legislation`)
- Madde/bölüm düzeyinde parça çekme (`get_legislation_fragment`)
- Yapılandırılmış metadata: yürürlük durumu + **işlenmemiş tadiller**
  (`get_legislation_metadata`)
- Tadil/ilga/ekleme takibi (`search_effects`)
- İleri XML sorguları (`search_legislation_advanced` — opsiyonel Research API
  kimliği ister) ve **deneysel** semantik arama

**ArthurLegal için neden gerekli?** Uluslararası sözleşmelerde (alım-satım,
charter party, EPC, finansman) governing-law klozu sıklıkla İngiliz hukukudur;
tahkim genelde Londra'dır. WebFetch rotasında her statü için URL kurup XML
ayrıştırmak gerekiyordu; MCP rotası aynı veriyi **araç tabanlı, yapılandırılmış
ve yürürlük-metadatalı** verir. Özellikle `search_effects`, "bu statü şu
tarihten beri tadil edildi mi?" sorusunu WebFetch'in veremediği kesinlikte
yanıtlar. Detay bağlam: `karsilastirmali-hukuk-rehberi.md`.

---

## Kurulum ve bağlantı şeması

Sunucu self-hosted çalışır; ürün politikası gereği **yalnızca loopback**
(tünel/uzak host reddedilir):

```
git clone https://github.com/legislation/legislation-mcp-ts
npm install && npm run build
npm start                # stdio (varsayılan, önerilen)
```

Claude Code / Desktop kaydı (stdio):

```json
{
  "mcpServers": {
    "uk-legislation": {
      "command": "node",
      "args": ["<repo-yolu>/build/index.js"]
    }
  }
}
```

| Katman | Kimlik | Not |
|---|---|---|
| Çekirdek araçlar (arama, metin, effects) | Gerekmez | Varsayılan kullanım |
| `search_legislation_advanced` | `RESEARCH_API_USERNAME` / `RESEARCH_API_PASSWORD` | Opsiyonel |
| Semantik arama (deneysel) | `SEMANTIC_API_KEY` | Opsiyonel, deneysel |
| HTTP transport | `MCP_SERVER_KEY` (bearer) | Kullanılmaz — stdio tercih |

---

## Araçlar

| Araç | Ne yapar |
|---|---|
| `search_legislation` | Arama — parametreler: `q`, `type`, `year`, `startYear`, `endYear`, `subject`, `department`, `extent`, `language`, `sort`, `page` |
| `get_legislation` | Tam metin (text / CLML XML / HTML / Akoma Ntoso) |
| `get_legislation_fragment` | Belirli parça: `section/12`, `part/2/chapter/1` |
| `get_legislation_metadata` | JSON metadata — yürürlük durumu + işlenmemiş tadiller |
| `get_legislation_table_of_contents` | İçindekiler (JSON) |
| `search_effects` | Tadil/ilga/ekleme kayıtları — `applied` filtresi, kaynak/hedef mevzuat |
| `search_legislation_advanced` / `count_legislation_advanced` | Research API üzerinden yapısal XML sorguları (kimlik ister) |
| `search_legislation_semantic` / `search_legislation_sections_semantic` | **Deneysel** vektör arama |

Araç listesi sürümle değişebilir — entegrasyonda README'deki güncel liste esas
alınır (entegrasyon öncesi doğrulanmalı).

---

## Uygulamalı örnekler

**Örnek 1 — Arbitration Act 1996'nın güncel durumu (tahkim klozu incelemesi):**

```
search_legislation:
  q: "arbitration"
  type: "ukpga"
  year: 1996
→ Arbitration Act 1996 (ukpga/1996/23) bulunur

get_legislation_metadata: ukpga/1996/23
→ yürürlük durumu + "changes not yet applied" listesi

get_legislation_fragment: ukpga/1996/23, "section/9"
→ s.9 (stay of legal proceedings) metni
```

Tanımlayıcı biçimi (`ukpga/1996/23`) ve fragment yolu, legislation.gov.uk URI
şemasıyla aynıdır; çağrı parametrelerinin tam JSON adları entegrasyon öncesi
README'den doğrulanmalı. WebFetch karşılığı (yedek rota, doğrulanmış URL):
`https://www.legislation.gov.uk/ukpga/1996/23/section/9`.

**Örnek 2 — UCTA 1977 tadil taraması (governing-law risk notu):**

```
search_effects:
  target: ukpga/1977/50
  applied: false
→ UCTA 1977'ye işaret eden, henüz metne işlenmemiş tadiller

get_legislation: ukpga/1977/50 (format: text)
→ konsolide tam metin; işlenmemiş tadil varsa çıktıda [review] flag'i
```

Eski rotadaki `/data.rdf` sürüm-zinciri incelemesinin araç karşılığı budur;
RDF ayrıntısı gerekiyorsa `uk-legislation-rehberi.md` geçerli kalır.

---

## İçtihat ayrımı — SERT KAPI (değişmedi)

Bu MCP **yalnızca mevzuat** kapsar. TNA'nın **Find Case Law** servisi
(İngiliz mahkeme kararları) **Open Justice Licence** altındadır: tekil karar
okuma/indirme serbesttir, ancak lisans metni açıkça **"computational analysis
of the Information (including indexing by search engines)"** kullanımını
kapsam dışı bırakır — bunun için ayrı, **başvuru temelli** (ücretsiz) bir
lisans alınması gerekir. Bu lisans alınana kadar UK içtihadı **belge-başına
WebFetch** rotasında kalır; MCP/toplu analiz rotasına **taşınamaz**. Bu bir
tercih değil, lisans kapısıdır.

---

## Atıf disiplini

Metin oturumda fiilen bu MCP (veya WebFetch yedeği) ile çekildiyse:

```
[UK Legislation — {tür yıl c./no} s.{madde} — çekim: GG.AA.YYYY — OGL v3.0]
```

Örnek: `[UK Legislation — Arbitration Act 1996 s.9 — çekim: 13.08.2026 — OGL v3.0]`.

- **OGL atfı zorunludur** — lisans gereği çıktıda "Contains public sector
  information licensed under the Open Government Licence v3.0" ibaresi (veya
  kısa `OGL v3.0` etiketi + bu ibarenin belge sonunda bir kez verilmesi) taşınır.
- Çekilmemiş bir İngiliz statüsü `[UK Legislation]` etiketi alamaz →
  `[model bilgisi — doğrulayın]`.
- `get_legislation_metadata` "changes not yet applied" veriyorsa atıfın yanına
  `[review]` eklenir; deneysel semantik arama sonuçları tek başına atıf
  dayanağı olamaz — tam metin çekimiyle teyit edilir.

---

## Lisans ve sınırlar

- **Lisans (kaynakta doğrulandı, 13.08.2026):** Repo — "Licensed under the
  Open Government Licence v3.0"; içerik — "Contains public sector information
  licensed under the Open Government Licence v3.0." OGL atfı her çıktıda taşınır.
- **Yalnızca loopback:** Ürün, tünel/uzak host'ları reddeder; sunucu yerel
  stdio süreci olarak çalıştırılır. HTTP modu kullanılmaz.
- **Sürüm sabitleme:** 13.08.2026 itibarıyla repoda yayımlanmış release **yok**
  — release çıkana kadar belirli bir **commit'e sabitlenir**; entegrasyonda
  release durumu yeniden kontrol edilir (entegrasyon öncesi doğrulanmalı).
- **Deneysel araçlar:** Semantik arama araçları deneyseldir ve ayrı API
  anahtarı ister; üretim iş akışına alınmaz.
- **İçtihat yok:** Yukarıdaki sert kapı — Find Case Law ayrı lisans rejimindedir.
- **Revised metin gecikmesi:** legislation.gov.uk'nin "changes not yet applied"
  sınırı MCP'de de aynen geçerlidir; metadata aracı bunu görünür kılar, ortadan
  kaldırmaz.

---

## Karar kaydı (mini-ADR)

**Bağlam.** UK, 14 yargı çevresi içinde WebFetch katmanındaydı: statü metni
URL kurgusuyla çekiliyor, sürüm/tadil durumu `/data.rdf` üzerinden elle
ayrıştırılıyordu. Bu, tadil taramasını yavaş ve hataya açık bırakıyordu; kaynak
operatörünün kendi arayüzü yoktu.

**Karar.** TNA'nın resmî `legislation-mcp-ts` sunucusu **MCP katmanına** kabul
edildi — Fedlex kalıbının ders kitabı örneği: kaynağın kendi operatöründen,
kimliksiz çekirdek araçlarla. Koşullar: (1) yalnızca loopback stdio, (2) her
atıfta OGL v3.0 ibaresi, (3) sürüm sabitleme (release yoksa commit).

**Sonuçlar.** Kazanım: yapılandırılmış arama, yürürlük metadatası ve
`search_effects` ile tadil takibi. Eski rotada kalanlar: UK **içtihadı**
(Open Justice Licence sert kapısı nedeniyle belge-başına WebFetch) ve RDF
sürüm-zinciri ayrıntısı (`uk-legislation-rehberi.md`). Entegrasyonda yeniden
doğrulanacaklar: güncel araç listesi, `get_legislation` parametre adları,
release/commit durumu.

---

## İlgili rehberler

- `uk-legislation-rehberi.md` — WebFetch yöntemi: URI şeması, tür kodları,
  content negotiation, RDF; bu MCP'nin **yedek rotası** ve içtihat rotası.
- `karsilastirmali-hukuk-rehberi.md` — İngiliz hukukunun ne zaman devreye
  girdiği; birincil yargı çevresi Türkiye kuralı.

---

*Son güncelleme: 13.08.2026. legislation-mcp-ts (The National Archives, resmî)
MCP entegrasyon rehberi; OGL v3.0, loopback-only, çekirdek araçlar anahtarsız.*