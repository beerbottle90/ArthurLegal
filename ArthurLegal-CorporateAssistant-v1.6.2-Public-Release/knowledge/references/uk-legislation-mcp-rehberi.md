# UK Legislation MCP (legislation-mcp-ts) — Kullanım Rehberi (MCP yöntemi)

> **Birincil yol ArthurLegal MCP `uk_` araçlarıdır** (aşağıdaki "ArthurLegal MCP"
> bölümü): `uk_search_legislation`, `uk_get_legislation`, `uk_get_section`,
> `uk_get_contents`, `uk_get_effects`. The National Archives'ın kendi
> `legislation-mcp-ts` sunucusu vardır ama ürün politikası gereği yalnız
> loopback'e bağlanır; barındırılamaz. Bu yüzden aynı kamuya açık veriye sitenin
> açık XML ve Atom uçlarından gidilir. Bu rehberin geri kalanı TNA sunucusunun
> araç yüzeyini belgeler; örneklerdeki araç adları `uk_` karşılıklarıdır.
>
> **Durum:** Açık erişim, API anahtarı gerekmez.
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

## ArthurLegal MCP — `uk_` araçları

| Alan | Değer |
|------|-------|
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on dört yargı çevresi tek uçta) |
| **Araç öneki** | `uk_` |
| **Auth** | **Yok** |
| **Kaynak** | legislation.gov.uk (The National Archives), Open Government Licence v3.0 |

> **Neden TNA'nın kendi MCP sunucusu değil?** `legislation-mcp-ts` ürün politikası
> gereği **yalnızca loopback**'e bağlıdır; başkaları için barındırılmak üzere
> tasarlanmamıştır. Bu yüzden aynı kamuya açık veriye sitenin açık XML ve Atom
> uçlarından gidiliyor — hiçbir şey yeniden dağıtılmıyor.

| Araç | Ne yapar |
|---|---|
| `uk_search_legislation` | Başlık / tam metin / tür / **tek yıl** araması |
| `uk_get_legislation` | Statü (revised · as enacted), metnin güncel olduğu tarih, extent |
| `uk_get_section` | Tek bir maddenin metni |
| `uk_get_contents` | İçindekiler |
| `uk_get_effects` | Sonraki mevzuatın yaptığı tadiller — **işlenmemişler dâhil** |

> ⚠️ **TADİL TUZAĞI.** Revize metin yalnızca `text_current_to` tarihine
> günceldir. O tarihten sonra çıkan ya da editoryal işlemi bekleyen tadiller
> okuduğun metinde **yoktur**. `uk_get_effects` + `unapplied_only` bunu yanıtlar
> ve **tüm beslemeyi** tarar: Equality Act 2010'da 24 işlenmemiş tadil var, tek
> sayfa bakan "yok" der. Yürürlükteki bir hükmü alıntılamadan önce kontrol et.
> `complete_scan: false` ise sayı bir tabandır, toplam değil.

> ⚠️ **Yıl aralığı yoktur.** legislation.gov.uk yılı **yolda** filtreler; sorgu
> dizesindeki `year=` kabul edilip **sessizce yok sayılır**. Tek yıl sor.

> ⚠️ **`extent` ≠ uygulama.** E+W+S+N.I. hükmün hangi ülkenin hukukunun parçası
> olduğunu söyler, olayda uygulanacağını değil.

---

## Uygulamalı örnekler

**Örnek 1 — Arbitration Act 1996'nın güncel durumu (tahkim klozu incelemesi):**

```
uk_search_legislation:
  query: "arbitration"
  type: "ukpga"
  year: 1996
→ Arbitration Act 1996 (ukpga/1996/23) bulunur

uk_get_legislation: ukpga/1996/23
→ statü (revised / as enacted), metnin güncel olduğu tarih (text_current_to), extent

uk_get_effects: ukpga/1996/23, unapplied_only: true
→ metne henüz işlenmemiş tadiller; complete_scan false ise sayı tabandır

uk_get_section: ukpga/1996/23, section 9
→ s.9 (stay of legal proceedings) metni
```

Tanımlayıcı biçimi (`ukpga/1996/23`) ve fragment yolu, legislation.gov.uk URI
şemasıyla aynıdır; çağrı parametrelerinin tam JSON adları entegrasyon öncesi
README'den doğrulanmalı. WebFetch karşılığı (yedek rota, doğrulanmış URL):
`https://www.legislation.gov.uk/ukpga/1996/23/section/9`.

**Örnek 2 — UCTA 1977 tadil taraması (governing-law risk notu):**

```
uk_get_effects: ukpga/1977/50, unapplied_only: true
→ UCTA 1977'ye işaret eden, henüz metne işlenmemiş tadiller

uk_get_legislation: ukpga/1977/50
→ konsolide metin ve text_current_to; işlenmemiş tadil varsa çıktıda [review] flag'i
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
- `uk_get_effects` işlenmemiş tadil veriyorsa atıfın yanına
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
doğrulanacaklar: güncel araç listesi, `uk_get_legislation` parametre adları,
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