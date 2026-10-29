---
name: tax-legal-transfer-pricing-review
description: >
  Intra-group işlem fiyatlandırması analizi: [Ana ortak / ilişkili taraf] ile ham petrol alımı, royalty,
  hizmet ücretleri için KVK m. 13 (örtülü kazanç dağıtımı) + OECD Transfer Pricing
  Guidelines uyum kontrolü. Yıllık TP dokümantasyon çıkarma, emsallere uygun fiyat
  analizi, Maliye inceleme öncesi pozisyon hazırlama.
user-invocable: true
---

# Transfer Pricing Review

## Matter context

TP genellikle **yıllık dokümantasyon dönemi** (kurumlar vergisi beyanname öncesi, Nisan) veya **özel işlem-bazlı** çalışılır.

> Bu TP review: (a) yıllık dokümantasyon hazırlık mı, (b) belirli bir intra-group işlem değerlendirmesi mi, (c) Maliye TP incelemesine cevap mı?

## Destination check

- **Mali İşler iç pozisyon** → "GİZLİDİR – HUKUK + MALİ İŞLER DAHİLİ TP NOTU"
- **Büyük 4 firma briefing** → "TAX BRIEF – CONFIDENTIAL"
- **Maliye'ye sunulacak dokümantasyon** → resmi format, üst başlık çıkar
- **CEO/CFO eskalasyon notu** → 1 sayfa executive summary

## Amaç

**KVK m. 13 — Örtülü Kazanç Dağıtımı:** İlişkili kişilerle (ana ortak, bağlı ortaklar, yöneticiler, ortak hisseli şirketler) yapılan işlemlerde fiyat **emsallere uygun (arm's length)** olmalı. Aksi halde:
- Aradaki fark **örtülü kazanç dağıtımı** sayılır
- Kurumlar vergisi matrahına eklenir
- Vergi ziyaa cezası + gecikme zammı
- Tekrarlı ise **kaçakçılık (VUK m. 359)** iddiası olabilir

**sektöre-özel risk üçlüsü:**
1. **Ham petrol alımı ([Ana ortak / ilişkili taraf] → [büyük enerji tesisi])** — yüksek tutar, fiyat dalgalanması (Brent benchmark)
2. **Royalty / lisans / marka** ([Ana ortak / ilişkili taraf] → [Müvekkil] + bağlı şirketler)
3. **Yönetim hizmeti, IT, mali danışmanlık** ([Ana ortak / ilişkili taraf] → [Müvekkil])

## Adımlar

### 1. İşlemleri envanterle

| İlişkili kişi | İşlem tipi | Yıllık tutar (TL) | Para birimi | Sıklık |
|---|---|---|---|---|
| [Müvekkil] ([ANA ORTAK MERKEZİ]) | Ham petrol satın alım | [...] | USD | sürekli |
| [Müvekkil] | Royalty | [...] | USD | yıllık |
| [Müvekkil] | Yönetim hizmeti | [...] | USD | yıllık |
| Bağlı şirket X | Intra-group hizmet | [...] | TL | [...] |

**Eşik kontrolü:** Bir ilişkili işlem ≥ 50.000 TL ise dokümantasyon zorunlu (Kurumlar Vergisi Genel Tebliği — tutar doğrulanmadı).

### 2. Yöntem seçimi (5 yöntem)

KVK m. 13/3 ve OECD TPG:

| Yöntem | Uygulama | [Müvekkil] örneği |
|---|---|---|
| **Karşılaştırılabilir Fiyat (KKF / CUP)** | Aynı/benzer mal/hizmet bağımsız işlemi | Ham petrol — Brent/Urals/Azeri Light benchmark |
| **Maliyet Artı (Cost Plus)** | Maliyet + makul kâr marjı | Yönetim hizmeti, IT |
| **Yeniden Satış Fiyatı (RPM)** | Satış fiyatı - brüt marj | Ticaret/distribütör işlemleri |
| **Kâr Bölüşümü (Profit Split)** | Toplam kârın paylaşımı | Karmaşık entegre işlemler ([BORU HATTI PROJESİ] gibi) |
| **İşlemsel Net Kâr Marjı (TNMM)** | Net kâr marjı karşılaştırma | Yaygın — bilgi yetersiz ise |

**[Müvekkil] önerisi:** Ham petrol için **KKF** (Brent + Azeri Light premium) en güçlü; royalty için **TNMM**; hizmet için **Maliyet Artı**.

### 3. Emsal analizi (benchmark study)

- **Bağımsız işlem verileri:** S&P Platts, Argus Media, IHS Markit (petrol fiyatları)
- **Royalty benchmarks:** RoyaltyStat, ktMINE, RoyaltySource
- **Hizmet benchmark:** Bureau van Dijk Amadeus (Avrupa), TP Catalyst (Refinitiv)

**Sorun:** Bu veri tabanlarına [Müvekkil]'ın **lisans abonelikleri** var mı? — `[DOLDUR]`. Yoksa Büyük 4 firma genelde abone ve raporu hazırlar.

### 4. ArthurLegal MCP (`tr_`) — GİB özelge + Danıştay emsali

```
tr_kurum_karari_ara(
  kurum="gib",
  query="transfer fiyatlandırma ham petrol ilişkili"
)

tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="D4",  # Kurumlar vergisi
  query="+örtülü +kazanç +dağıtımı +transfer +pricing",
  date_from="2022-01-01"
)
```

GİB özelgeleri TP konusunda **yorumlama kaynağı**. Önceki Maliye yaklaşımını öğren.

### 5. OECD TPG ve BEPS Action

Türkiye OECD üyesi, OECD TPG'yi referans alır:
- **OECD TPG 2022** (güncel revizyon)
- **BEPS Action 8-10** — Intangibles, services, financial transactions
- **BEPS Action 13** — Country-by-Country Reporting (CbCR — [Müvekkil] dahil)

Atıf: `[OECD TPG — Chapter X — 2022]`, `[BEPS Action — sayı]`.

### 6. [Ana ortak / ilişkili taraf]-özel kontroller

- [ ] **Azerbaycan-Türkiye Çifte Vergilendirmeyi Önleme Anlaşması** (1994) — varsayılan tutar ve emsal
- [ ] **[BORU HATTI PROJESİ] işlem rejimi** — hükümetlerarası anlaşma kapsamında özel tarife
- [ ] **[halka açık iştirak] KAP açıklama** — büyük tarhiyat halinde özel durum
- [ ] **MASAK** — yüksek tutarlı uluslararası işlem (yıllık 1B USD+ ham petrol)
- [ ] **OFAC/AB yaptırım** — Azerbaycan ile işlem ama bağlantılı taraf kontrolü

### 7. Dokümantasyon paketi (yıllık)

Kurumlar Vergisi Genel Tebliği uyarınca:

- **Master File** — grup yapısı, intra-group işlem haritası (BEPS Action 13)
- **Local File** — [Müvekkil] spesifik: işlemler, yöntem, emsal analizi, fonksiyonel analiz
- **Country-by-Country Reporting (CbCR)** — global [Müvekkil] ([ANA ORTAK MERKEZİ] ana şirket tarafından)

### 8. Pozisyon paketi (Maliye savunmasına hazır)

Her intra-group işlem için:
- İşlem tarifi (ne, ne kadar, hangi koşullarda)
- Fonksiyonel analiz (kim ne yapıyor, kim risk alıyor)
- Seçilen yöntem + gerekçe
- Emsal işlem aralığı (interquartile range)
- Test sonucu (fiyat aralık içinde mi)
- Sapma varsa gerekçe (örn. piyasa koşulları)

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Transfer Pricing Review — [Dönem / İşlem]

## ⚠️ İnceleyen notu
- **Kapsam:** Yıllık dokümantasyon / Spesifik işlem / Maliye inceleme cevabı
- **Risk seviyesi:** 🔴/🟠/🟡/🟢
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (GİB özelge [N], Danıştay [N]); OECD TPG referansları
- **Mali İşler koordinasyon:** [✓/✗ + kim]
- **CFO bilgi:** [✓/✗]
- **Reviewer karar bekleyen:** N adet

## İlişkili işlem envanteri
[tablo]

## Yöntem seçimi ve gerekçe
[seçilen yöntem + alternatif değerlendirme]

## Emsal analizi
[benchmark sonuçları + aralık]

## [Ana ortak / ilişkili taraf]-özel notlar
[BIT anlaşması, [BORU HATTI PROJESİ] rejimi, KAP, MASAK, yaptırım]

## Risk değerlendirmesi
| İşlem | Risk | Maliye saldırı vektörü | Savunma |
|---|---|---|---|
| ... | ... | ... | ... |

## Dokümantasyon checklist
- [ ] Master File hazır
- [ ] Local File hazır
- [ ] CbCR (global [Müvekkil] tarafından)
- [ ] Pozisyon paketi (savunmaya hazır)

## Sonraki adımlar

> 1. **Büyük 4 firma ile koordinasyon** — dokümantasyon revizyon
> 2. **CFO bilgi notu** — yıllık TP raporu özet
> 3. **Maliye'ye proaktif özelge talebi** — risk yüksek bir işlem için
> 4. **Daha fazla bilgi** — şu noktaları araştırmadan ilerleyemem: [...]

**One question I'd ask:** [örn. "Maliye RIA programında [Müvekkil]'ın yer aldığına dair bir gösterge var mı? Yıllık denetim seçim olasılığını bilmek strateji değiştirir."]
```

---

## Kaynak katmani — /legal-research (v1.4.0)

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
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| AZ Vergi Mecellesi, intra-group transfer fiyatlandirmasi — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| transfer pricing ve uluslararasi vergi ogretisi — **ikincil**; ozelge ve Danistay karari yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
