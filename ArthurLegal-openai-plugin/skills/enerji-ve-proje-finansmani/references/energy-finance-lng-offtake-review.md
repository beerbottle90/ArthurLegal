# energy-finance-lng-offtake-review

LNG ve uzun vadeli enerji tedarik sözleşmelerini inceler. Take-or-pay yükümlülüğü, force majeure, price review, destination klozu, sanction compliance ve Japon/Koreli alıcı özel dikkat noktaları.

# /lng-offtake-review — LNG & Uzun Vadeli Enerji Tedarik Sözleşmesi

## Adım 1 — Sözleşme yapısı tespiti

| Unsur | Değer |
|---|---|
| Sözleşme türü | FOB / DES / DAP / EXW |
| [Müvekkil] tarafı | Alıcı (buyer) / Satıcı (seller) |
| Karşı taraf | [örn. Mitsui, JERA, Shell, BP] |
| Sözleşme süresi | [yıl] |
| Hacim (yıllık, MTPA veya MMBtu) | |
| Governing law + tahkim | |
| Referans fiyat | JKM / TTF / Henry Hub / Brent-linked / sabit |

## Adım 2 — Take-or-pay analizi (KRİTİK)

- **Yıllık kontrat miktarı (ACQ):** [MTPA]
- **Minimum take yükümlülüğü:** % ACQ — ceza = difference × fiyat?
- **Make-up hakkı:** var mı, kullanım süresi?
- **Carry-forward / carry-back:** kaç yıl?
- **Force majeure istisnaları:** take-or-pay'i askıya alıyor mu?
- **Downward quantity tolerance (DQT):** [Müvekkil] satıcıysa, teslimat esnekliği
- **Upward quantity tolerance (UQT):** alıcı fazla alabilir mi?

## Adım 3 — Fiyat formülü ve price review

- **Fiyat formülü:** [P = a×JKM + b×TTF + c gibi]
- **Fiyat revizyonu:** kaç yılda bir, mekanizma (arbitration / expert / karşılıklı anlaşma)
- **Cap / floor:** var mı?
- **Döviz:** USD / EUR — kur riski müvekkilde mi?
- **Damga vergisi:** çok yıllı yüksek tutarlı sözleşme → DVK hesabı gerekli (rehber: `skills/arthurlegal/references/damga-vergisi-rehberi.md`)

## Adım 4 — Force majeure ve hardship

- FM tanımı kapsamı: doğal afet / siyasi / pandemi / siber
- **Yaptırım (sanctions) FM:** OFAC/AB/BM yaptırım listesine giriş FM sayılıyor mu?
- **İlişkili taraf riski:** Rusya veya yaptırım altındaki ülke bağlantılı FM senaryoları
- Hardship klozu ayrı mı? Hükümler farklı mı?
- FM ihbar süresi ve belgeleme yükümlülüğü

## Adım 5 — Destination kloz & diversion

- Destination klozu var mı? (yeniden satış / diversion yasağı)
- Japon/Koreli alıcılar ile tipik katı destination → Avrupa piyasasına diversion mümkün mü?
- Avrupa hukuku açısından destination klozu geçerliliği — AB Rekabet (TFEU m.102)

## Adım 6 — Sanction compliance

1. Resmî yaptırım listeleri: karşı taraf tara (`yaptirim-tarama-rehberi.md`)
2. CAATSA m.232: Rusya kaynaklı LNG mı? (Yamal LNG gibi)
3. OFAC SDGT: transit ülkeler (Türkiye Boğazları, Hürmüz)
4. AB 833/2014: Rusya LNG kısıtlamaları ve istisnaları
5. Sözleşmedeki sanction clause: tek taraflı fesih hakkı var mı?
6. Escrow / payment restriction: yaptırım ülkesine ödeme kanalı

## Adım 7 — Japon alıcı özel notlar (MITSUI/JERA/JAPEX)

- **FEFTA bildirimi:** Japon tarafın yapacağı yabancı yatırım bildirimi
- **METI onayı:** enerji güvenliği kapsamında METI'nin bireysel onayı gerekebilir
- **Japon şirket hukuku (会社法):** board karar mekanizması — JLT: `japan-legislation-rehberi.md`
- **Arbitration:** Tokyo / Singapore / Londra — ICC veya JIAC

## Findings

| # | Kloz | Severity | Not |
|---|---|---|---|
| | Take-or-pay | 🔴/🟠/🟡/🟢 | |
| | Force majeure | | |
| | Sanctions | | |
| | Price review | | |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# LNG Offtake İncelemesi — [Sözleşme / Karşı taraf / Tarih]

## ⚠️ Reviewer note

## Bottom line

## Yapı özeti (taraf, hacim, süre, fiyat)

## Take-or-pay analizi

## Fiyat formülü & review mekanizması

## Force majeure & sanctions klozu

## Destination & diversion

## İlişkili taraf / özel alıcı notları

## Findings

## Önerilen kloz değişiklikleri / redline
```

---

## Kaynak katmanı — /legal-research

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur —
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| **bu plugin icin birincil kullanim** — PSA/JOA, cost recovery, profit split, stabilizasyon, DMO, decommissioning, yerel icerik benchmark'i | ``legal-research-sozlesme-emsali` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-sozlesme-emsali.md`)` |
| AZ upstream/yer alti serveti rejimi, JV ve enerji mevzuati — akt + statu | ``legal-research-az-mevzuat` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-az-mevzuat.md`)` |
| Energy Charter Treaty, yatirim tahkimi, stabilizasyon klozu ogretisi — **ikincil** | ``legal-research-karsilastirmali-doktrin` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-karsilastirmali-doktrin.md`)` |

Rehberler: `skills/arthurlegal/references/eqanun-mcp-rehberi.md` · `skills/arthurlegal/references/lex-scholar-rehberi.md` · `skills/arthurlegal/references/resourcecontracts-rehberi.md` · `skills/arthurlegal/references/karsilastirmali-hukuk-rehberi.md` · `skills/arthurlegal/references/nl-rechtspraak-mcp-rehberi.md` · `skills/arthurlegal/references/pl-sejm-mcp-rehberi.md` · `skills/arthurlegal/references/at-ris-mcp-rehberi.md` · `skills/arthurlegal/references/ie-statutebook-mcp-rehberi.md` · `skills/arthurlegal/references/fi-finlex-mcp-rehberi.md` · `skills/arthurlegal/references/es-boe-mcp-rehberi.md`
