# US Legislation (GovInfo WebFetch) — Kullanım Rehberi

> **Resmi MCP server VAR** — *GovInfo WebFetch*, ABD Government Publishing Office (GPO)
> tarafından işletilir. Ocak 2026'dan beri **public preview**. Bu rehber hem MCP
> hem WebFetch fallback prosedürünü tanımlar.
>
> **Durum:** ✅ Aktif. **api.data.gov API anahtarı gerekir** (ücretsiz).
> Anahtar güvenli ortam değişkeninde tutulur (`GOVINFO_API_KEY`) — bu rehbere
> veya paylaşılan dosyalara **asla** yazılmaz. Birincil yargı çevresi
> Türkiye'dir; bu kaynak yalnızca ABD hukuku temas eden işlerde kullanılır
> (bkz. `karsilastirmali-hukuk-rehberi.md`).

---

## GovInfo nedir?

**GovInfo** (govinfo.gov) — ABD federal devletinin resmi yayın platformu. Federal
mevzuatın, yönetmeliğin ve kongre belgelerinin otantik (dijital imzalı) kaynağı.

**MCP üzerinden erişilen koleksiyonlar:**

| Koleksiyon | İçerik |
|---|---|
| `USCODE` | United States Code — yürürlükteki federal kanunlar (ör. Title 26 IRC, Title 35 Patent, Title 17 Copyright, Title 15 Ticaret) |
| `PLAW` | Public Laws — kabul edilen kanunlar (Statutes at Large) |
| `FR` | Federal Register — günlük resmi gazete (kural taslakları, nihai kurallar, başkanlık belgeleri) |
| `CFR` / `ECFR` | Code of Federal Regulations — yürürlükteki federal yönetmelik |
| `BILLS` / `BILLSTATUS` | Kongre tasarıları ve durumu |
| `COMPS` | Statute Compilations — tadilli birleşik kanun metinleri |

**[ŞİRKET ADI] için neden gerekli?**
- **commercial:** ABD ihracat kontrol / yaptırım rejimi (örn. IEEPA, ECRA — OFAC
  taramasının statü zemini), NY hukuku yönetimli sözleşmeler.
- **corporate:** sınır-ötesi M&A, ABD securities (Securities Act / Exchange Act).
- **tax:** Internal Revenue Code (Title 26) — uluslararası vergi, treaty.
- **ip:** 35 USC (patent), 17 USC (copyright), 15 USC (Lanham — marka).
- **regulatory:** Federal Register günlük takip, karşılaştırmalı düzenleme.

---

## Bağlantı — Claude Code (.mcp.json)

İlgili plugin'lerin `.mcp.json` dosyasında GovInfo connector'ı tanımlıdır:

```jsonc
"GovInfo": {
  "type": "http",
  "url": "https://api.govinfo.gov",
  "headers": { "x-api-key": "${GOVINFO_API_KEY}" }
}
```

`${GOVINFO_API_KEY}` ortam değişkeninden çözümlenir. Kurulum:
- `~/.claude/settings.local.json` → `env` bölümü, **veya**
- OS ortam değişkeni `GOVINFO_API_KEY`

Anahtar **`.mcp.json`'a, `CLAUDE.md`'ye veya `SYSTEM_PROMPT.md`'ye yazılmaz.**

## Bağlantı — Claude.ai Projects (WebFetch fallback)

claude.ai Projects custom connector'da header-bazlı API anahtarı yönetimi
sınırlı olabileceğinden, Projects ortamında GovInfo **WebFetch** ile kullanılır.
GovInfo REST API'si `api_key` sorgu parametresini destekler:

```
GET https://api.govinfo.gov/collections?api_key={GOVINFO_API_KEY}
GET https://api.govinfo.gov/search?api_key={GOVINFO_API_KEY}   (POST body ile sorgu)
GET https://api.govinfo.gov/packages/{packageId}/summary?api_key={GOVINFO_API_KEY}
```

---

## API anahtarı prosedürü

**Adım 1:** https://www.govinfo.gov/api-signup → `api.data.gov` anahtarı talep
(ücretsiz; aynı anahtar birçok ABD federal API'sinde çalışır).

**Adım 2:** Anahtar e-posta ile gelir → güvenli ortam değişkenine kaydedilir
(`GOVINFO_API_KEY`).

**⚠️ Asla:** Anahtarı repoya commit edilen herhangi bir dosyaya yazma.

---

## Kullanım kalıbı (Claude)

1. Hangi koleksiyon? (statü → `USCODE`, yönetmelik → `CFR`, güncel kural → `FR`).
2. GovInfo WebFetch ile `api.govinfo.gov`.
3. Sonucu **otantik GPO metni** olarak işle; package/granule ID'sini not al.
4. Çıktıda atıf etiketi koy.

**Congress.gov yedeği:** Tasarı/yasama süreci ayrıntısı için Congress.gov API
(`api.congress.gov`, aynı `api.data.gov` anahtarı) WebFetch ile kullanılabilir —
GovInfo `BILLSTATUS` yetersiz kalırsa.

---

## Atıf disiplini

ABD mevzuatı oturumda fiilen GovInfo'dan (WebFetch) çekildiyse:

```
[US Legislation — GovInfo — <koleksiyon/atıf> — GG.AA.YYYY]
```

Örnek: `[US Legislation — GovInfo — 35 U.S.C. §101 — 22.05.2026]`,
`[US Legislation — GovInfo — Federal Register 90 FR 12345 — 22.05.2026]`.

Çekmediğin bir ABD statüsünü `[US Legislation]` etiketleyemezsin →
`[model bilgisi — doğrulayın]`. GovInfo **içtihat içermez**; ABD mahkeme
kararları için `courtlistener-rehberi.md`.

---

## Sınırlamalar

- **Public preview** — GovInfo WebFetch geliştirme aşamasında; araç şeması
  değişebilir. Sorun olursa WebFetch fallback'e geç.
- **api.data.gov kota** — anahtar başına saatlik istek limiti var; toplu işte
  dikkat.
- **İçtihat yok** — yalnızca mevzuat/yönetmelik/kongre belgesi.
- **Eyalet hukuku yok** — GovInfo yalnız **federal**. ABD eyalet kanunu (örn.
  Delaware General Corporation Law, California Civil Code) bu kaynakta değil;
  gerektiğinde web search + `[verify]`.

---

## Yedek kaynaklar (MCP + WebFetch erişilemezse)

| Kaynak | URL | Not |
|---|---|---|
| GovInfo (web) | https://www.govinfo.gov | Manuel arama |
| eCFR | https://www.ecfr.gov | Yürürlükteki CFR |
| Cornell LII | https://www.law.cornell.edu/uscode | US Code (resmi olmayan ama güvenilir) |
| Congress.gov | https://www.congress.gov | Tasarı / yasama süreci |
| Federal Register | https://www.federalregister.gov | Günlük resmi gazete |

---

## Versiyon disiplini

- Bu rehber **v1.6.0** (*Cross-Border Connectors*) ile eklendi.
- GovInfo WebFetch public preview olduğundan, araç adları/şeması için GPO'nun resmi
  deposu teyit edilir: `https://github.com/usgpo/api` (`docs/mcp.md`).

---

*Son güncelleme: 22.05.2026 — v1.6.0. GovInfo WebFetch + WebFetch entegrasyon prosedürü; api.data.gov anahtarı env değişkeninde.*
