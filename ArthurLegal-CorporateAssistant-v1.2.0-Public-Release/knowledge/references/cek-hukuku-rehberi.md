# Çek Cumhuriyeti Hukuku — Kullanım Rehberi (Sbírka MCP)

> **MCP Server:** `sbirka-mcp` — e-Sbírka.cz (Çek resmi mevzuat veri tabanı) için
> saidsurucu tarafından geliştirilen FastMCP sunucu. yargi-mcp ile aynı geliştirici.
>
> **Endpoint:** `https://sbirka-mcp.fastmcp.app/mcp`
> **Auth:** claude.ai Connectors üzerinden OAuth (doğrudan curl 401 döner — normal)
> **Lisans:** MIT | **Repo:** https://github.com/saidsurucu/sbirka-mcp
> **Kapsam:** 1848'den günümüze Çek mevzuatının tamamı + Anayasa Mahkemesi kararları
>
> **[ŞİRKET ADI] neden gerekli?** Çek Cumhuriyeti AB üyesi; Çek hukukunu governing law seçen
> sözleşmeler, Çek şirket yapıları (s.r.o. / a.s.), Prague ICC/SAC tahkimi, Çek enerji
> sektörü (ČEZ, PRE, RWE CZ) karşı taraf due diligence ve AB mevzuat uyumu referansı.

---

## Araçlar (3)

| Araç | Parametre | Kullanım |
|------|-----------|---------|
| `search_czech_legislation` | `query` (str) | Kanun numarasına, anahtar kelimeye veya madde referansına göre arama |
| `get_czech_law_text` | `stale_url` (str) | Tam metni Markdown + çapraz referanslarla getir |
| `get_czech_law_article` | `stale_url`, `article` (str) | Belirli bir maddeyi (§ veya čl.) bölüm başlıklarıyla çıkar |

---

## Kapsanan mevzuat türleri

| Çekçe | Türkçe |
|-------|--------|
| Zákony | Kanunlar (parlamento) |
| Ústavní zákony | Anayasal kanunlar |
| Nařízení vlády | Hükümet yönetmelikleri |
| Vyhlášky ministerstev | Bakanlık kararnameleri |
| Nálezy Ústavního soudu | Anayasa Mahkemesi kararları |
| Mezinárodní smlouvy | Uluslararası anlaşmalar |

---

## Tipik kullanım pattern'ları

### 1. Kanun numarasıyla arama

```
search_czech_legislation(query="89/2012 Sb.")
→ Čechy Civil Code (Nový občanský zákoník)
→ staleUrl döner → get_czech_law_text ile tam metin
```

### 2. Konu araması

```
search_czech_legislation(query="zákon o obchodních korporacích")
→ Şirketler Kanunu (90/2012 Sb.) döner

search_czech_legislation(query="zákon o ochraně osobních údajů")
→ Kişisel Veri Koruma (GDPR implementasyon kanunu)

search_czech_legislation(query="zákon o energetice")
→ Enerji Kanunu (458/2000 Sb.)

search_czech_legislation(query="zákon o rozhodčím řízení")
→ Tahkim Kanunu (216/1994 Sb.)
```

### 3. Belirli madde getir

```
get_czech_law_article(
  stale_url="<search sonucundan gelen URL>",
  article="§ 1793"
)
→ NOZ m. 1793 (aşırı fayda / laesio enormis) tam metni
```

---

## [ŞİRKET ADI] için önemli Çek kanunları

| Konu | Çekçe Ad / Numara | [ŞİRKET ADI] Bağlantısı |
|------|-------------------|-----------------|
| **Sözleşme hukuku** | Zákon č. 89/2012 Sb. (Nový OZ) | Governing law CZ seçilmişse |
| **Şirket hukuku** | Zákon č. 90/2012 Sb. (ZOK) | Çek s.r.o. / a.s. yapısı |
| **Enerji** | Zákon č. 458/2000 Sb. | ČEZ, PRE, RWE CZ ile tedarik |
| **Tahkim** | Zákon č. 216/1994 Sb. | Prague seated tahkim (SAC/ICC) |
| **Kişisel Veri** | GDPR + zákon č. 110/2019 Sb. | Çek KVKK eşdeğeri |
| **Rekabet** | Zákon č. 143/2001 Sb. | Piyasa davranışı |
| **Vergi (KV)** | Zákon č. 586/1992 Sb. | Çek kurumlar vergisi + TP |
| **Yabancı Yatırım** | Zákon č. 47/2002 Sb. | Çek'e yabancı sermaye |

---

## Connector kurulumu (claude.ai)

1. claude.ai → Settings → Connectors → **+ Add custom connector**
2. Name: `Sbírka MCP`
3. URL: `https://sbirka-mcp.fastmcp.app/mcp`
4. OAuth akışı tamamlanır → connector aktif

---

## Atıf disiplini

- `[CZ Mevzuat — Sbírka MCP — Zákon č. {no}/Sb. § {madde} — GG.AA.YYYY]`
- `[CZ Anayasa Mah. — Sbírka MCP — Nález {ref} — GG.AA.YYYY]`

**Asla:** MCP'den çekilmediğin Çek mevzuatını `[CZ Mevzuat]` etiketiyle gösterme →
`[model bilgisi — doğrulayın]` kullan.

---

## Sınırlamalar

- **Yalnızca Çekçe:** Tam metin çeviri modele kalır; kritik metinlerde `[review]` ekle.
- **connector gerekli:** Bu rehber yalnızca sbirka-mcp connector'ı eklenmiş
  oturumlarda çalışır. Connector yoksa → WebFetch ile `https://www.e-sbirka.cz/` dene.
- **Güncellik:** e-Sbírka.cz resmi kaynak; connector bu veritabanını yansıtır.

---

## Versiyon disiplini

- Bu rehber **v1.8.3** (*Sırbistan + Çek Cumhuriyeti Entegrasyonu*) ile eklendi.
- sbirka-mcp geliştirici: saidsurucu (yargi-mcp ile aynı kişi, 31.05.2026 araştırması).
- Endpoint test: `curl 401` (OAuth akışı bekleniyor — normal).

---

*Son güncelleme: 31.05.2026 — v1.8.3. Çek Cumhuriyeti hukuku Sbírka MCP entegrasyon prosedürü.*
