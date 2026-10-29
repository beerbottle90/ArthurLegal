---
name: tax-legal-vergi-incelemesi-response
description: >
  Maliye Bakanlığı vergi inceleme süreci yönetimi: inceleme tutanağı analizi,
  savunma argümantasyonu, tarhiyat öncesi uzlaşma vs. dava karar matrisi, ön
  rapora itiraz dilekçesi taslağı. VUK m. 134-141 inceleme + VUK Ek m. 11 tarhiyat
  öncesi uzlaşma.
user-invocable: true
---

# Vergi İncelemesi Response

## Tetik

Maliye'den **vergi inceleme başlama yazısı** veya **inceleme tutanağı** veya **inceleme raporu** geldiğinde.

## Destination check

- **Mali İşler iç değerlendirme** → "GİZLİDİR – HUKUK + MALİ İŞLER DAHİLİ"
- **CFO/CEO eskalasyon** → 1 sayfa exec summary
- **Dış vergi avukatı brief'i** → "TAX BRIEF – AVUKATLIK K. m. 36"
- **Maliye'ye sunulacak ön rapora itiraz** → resmi format

## Süreç haritası (VUK m. 134-141)

```
Maliye inceleme başlama →
İnceleme tutanağı (mükellef ve yetkili imza) →
İnceleme raporu (denetçi hazırlar, Bakanlık onayı) →
[Tarhiyat öncesi: VUK Ek m. 11 uzlaşma şansı] →
Tarhiyat (vergi/ceza belirlenir, tebliğ) →
[Tarhiyat sonrası: VUK Ek m. 1 uzlaşma | İYUK m. 7 — 30 gün dava] →
Vergi mahkemesi → BİM istinafı → Danıştay temyizi (parasal sınırlara bağlı — İYUK m. 45/1, 46)
```

## Adımlar

### 1. Hangi aşamadayız?

Sor:

> Şu an hangi belge elimizde?
> A. İnceleme başlama yazısı (henüz inceleme başlamadı)
> B. İnceleme tutanağı (denetçi şirkette, kayıt tutuyor)
> C. İnceleme raporu (denetçi raporunu yazdı, henüz tarhiyat yok)
> D. Tarhiyat tebliğ edildi (vergi/ceza belirlendi)

Aşamaya göre stratejisi çok farklıdır.

### A. İnceleme başlama (denetçi gelecek)

- [ ] **Hazırlık dosyası** — incelemeye konu döneme ait beyanname + defter + sözleşmeler + faturalar derhal hazırlanır
- [ ] **Mali İşler + Hukuk koordinasyon** toplantısı
- [ ] **Büyük 4 firma çağrı** — daha önce bu firma TP/genel vergi danışmanı ise koordine
- [ ] **Denetçi ile iletişim diiplini** — sözlü ifade verme yerine yazılı talep, "düşüneceğiz, cevap vereceğiz" formülü
- [ ] **Olası riskler envanteri** — denetçinin nelere bakacağı tahmini (önceki yıl raporlar, BBR sektör analizleri)

### B. İnceleme tutanağı imzalanmadan

İmza ATILMAMASI ÖNERİSİ: tutanaktaki tespitler yanlış/eksik ise itirazlar yazılmadan imza atma. **İmza atılırsa kabul edilmiş sayılabilir.**

- [ ] Her tespiti madde madde değerlendir
- [ ] Yanlış olanlara "İHTİRAZİ KAYITLA" ibaresi
- [ ] Eksik kalanlara "Şu belgeler eklenecektir" şerhi
- [ ] Hukuki dayanağı sorgulanır olanlara "Bu konudaki görüşümüzü ayrıca yazılı sunacağız"

### C. İnceleme raporu — pre-tarhiyat strateji

Bu aşama **kritik**. Raporda önerilen tarhiyat fiilen yapılmadan önce:

**Option 1: Tarhiyat öncesi uzlaşma (VUK Ek m. 11)**
- Daha avantajlı zamanlama
- Cezada %50'ye kadar indirim (doğrulanmadı) — yalnız ceza; vergi aslı uzlaşma kapsamı dışında (7524 s.K.)
- Pazarlık alanı geniş
- Sonra "kabul ediyorum" yazısı

**Option 2: Tarhiyatın yapılmasını bekle, dava aç**
- Yazılı pozisyon güçlü ise
- Davada kazanma olasılığı yüksek ise
- Maliye'nin agresif yorum yaptığını ispatlayabilirsen

**Option 3: Karma — bazı tespitleri kabul, bazılarına itiraz**
- Risk düşük olan tespitleri uzlaş
- Asıl yüksek tutarlı tespitler için dava

**Karar matrisi (bu skill bunu üretir):**

| Tespit | Maliye iddiası | Kazanma olasılığı | Tutar | Önerilen yol |
|---|---|---|---|---|
| ... | ... | %X | TL | Uzlaş / Dava / Karma |

### D. Tarhiyat tebliğ edildi

⚠️ **30 GÜN SÜRE BAŞLADI** (İYUK m. 7). Aksiyon:

- [ ] **Tarhiyat sonrası uzlaşma (VUK Ek m. 1)** — 30 gün içinde başvur (cezada %75'e kadar indirim (doğrulanmadı); yalnız ceza için, vergi aslı uzlaşma kapsamı dışında — 7524 s.K.)
- [ ] **Veya dava** — 30 gün içinde vergi mahkemesine → `/arthurlegal:tax-legal-tax-litigation-prep`
- [ ] **Veya ikisi** — uzlaşma başvur; uzlaşma vaki olmadıkça o ceza için dava açılamaz (VUK ek m. 7/1). Uzlaşılmazsa dava, tutanağın tebliğinden itibaren genel hükümlere göre açılır; süre bitmiş veya 15 günden az kalmışsa tutanağın tebliğinden itibaren 15 gün olarak uzar (VUK ek m. 7/4) — yine de süre kısalabileceğinden derhal aksiyon al.

### ArthurLegal MCP (`tr_`) — emsal arama

```
tr_ictihat_ara(
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  query="<tespitin konusu>",
  date_from="2022-01-01"
)

tr_kurum_karari_ara(
  kurum="gib",
  query="<tespitin konusu>"
)
```

### sektöre-özel kontroller

- [ ] **Tarhiyat tutarı > 10M TL** → CFO + CEO + Başkan eskalasyon
- [ ] **[HALKA AÇIK İŞTİRAK] ilgili tarhiyat** → KAP açıklama kontrolü
- [ ] **TP konusu** → [Ana ortak / ilişkili taraf] ile koordinasyon
- [ ] **VUK m. 359 kaçakçılık iddiası** → derhal ceza avukatı + CEO
- [ ] **[RAFİNERİ] ÖTV / [HALKA AÇIK İŞTİRAK] KDV iade reddi** → kaza-bazlı dava + uzlaşma kombinasyonu

## Çıktı

```markdown
[ÜST BAŞLIK]

# Vergi İncelemesi Response — [İnceleme dönemi / Konu]

## ⚠️ İnceleyen notu
- **Aşama:** A/B/C/D
- **Süre kalan:** [İYUK m. 7 30 gün / VUK Ek 30 gün — N gün kaldı]
- **Karar matrisi:** [Uzlaş / Dava / Karma]
- **Tutar maruziyet:** [TL toplam / vergi + ceza]
- **Reviewer bekleyen:** N adet

## Maliye tespitleri envanteri
[tablo: tespit, iddia, dayanak, savunma argümanı]

## Tarhiyat öncesi vs. sonrası uzlaşma karşılaştırma
[Ek m. 11 avantajı + Ek m. 1 indirim]

## Dava açma analizi
[Danıştay daire, emsal kararlar, kazanma olasılığı]

## Sonraki adımlar
> 1. **Tarhiyat öncesi uzlaşma başvurusu** — daire başvurusu hazırla
> 2. **Hukuk Direktörü + CFO eskalasyon notu**
> 3. **Dış vergi avukatı brief** (dava açılacaksa)
> 4. **Daha fazla bilgi** — şu noktaları aydınlatalım: [...]

**One question I'd ask:** [örn. "Maliye denetçisi geçmişte [Müvekkil]'a karşı agresif mi yumuşak mı yorum yaptı? İlişki sürdürmek karar değiştirebilir."]
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
