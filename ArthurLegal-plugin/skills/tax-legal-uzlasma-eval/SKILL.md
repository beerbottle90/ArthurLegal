---
name: tax-legal-uzlasma-eval
description: >
  Maliye uzlaşma teklifi geldi veya uzlaşma talebi verilecek — değerlendirme:
  tarhiyat öncesi (VUK Ek m. 11, cezada %50'ye kadar indirim (doğrulanmadı)) vs. tarhiyat sonrası
  (Ek m. 1, cezada %75'e kadar indirim (doğrulanmadı)) karar; kabul edilebilir ceza aralığı
  (vergi aslı 7524 s.K. sonrası uzlaşma kapsamı dışında); vergi davası alternatifiyle maliyet
  karşılaştırma; [Müvekkil] onay zinciri.
user-invocable: true
---

# Uzlaşma Değerlendirme (VUK Ek m. 1 / Ek m. 11)

## Tetik

İki senaryo:
1. Maliye inceleme tutanağı/raporu sonrası **tarhiyat öncesi uzlaşma şansı** (Ek m. 11)
2. Tarhiyat tebliğ edildi, **30 gün içinde tarhiyat sonrası uzlaşma talep** edilebilir (Ek m. 1)

## Destination check

- **CFO + Hukuk + Mali İşler iç değerlendirme** → "GİZLİDİR – UZLAŞMA STRATEJİ NOTU"
- **CEO/Başkan eskalasyon** (büyük tutar) → 1 sayfa exec summary
- **Maliye'ye uzlaşma talep dilekçesi** → resmi format

## Karşılaştırma — Ek m. 11 vs Ek m. 1

| Özellik | Tarhiyat öncesi (Ek m. 11) | Tarhiyat sonrası (Ek m. 1) |
|---|---|---|
| **Süre** | İnceleme raporu sonrası, tarhiyat öncesi | Tarhiyat tebliğinden 30 gün |
| **Cezada indirim potansiyeli** | %50'ye kadar (doğrulanmadı) | **%75'e kadar (doğrulanmadı)** |
| **Pazarlık esnekliği** | Yüksek (henüz tarhiyat yapılmadı) | Düşük (tutar kesinleşmiş) |
| **Risk** | Maliye agresif tutum sergileyebilir | Sonraki dava süresi kaçırılabilir |
| **Strateji** | Hızlı çözüm istiyorsa | Pazarlık + dava seçeneği aksamadan ise |

⚠️ **KRİTİK:** Uzlaşma talep edilmişse, uzlaşma vaki olmadıkça o ceza için dava açılamaz (VUK ek m. 7/1). Uzlaşma sağlanamazsa, kesilen cezaya karşı dava **"uzlaşmanın vaki olmadığına dair tutanağın" tebliğinden itibaren genel hükümlere göre** açılır; dava açma süresi bitmiş veya 15 günden az kalmışsa süre tutanağın tebliğinden itibaren **15 gün** olarak uzar (VUK ek m. 7/4). Ayrıca tarhiyat öncesi uzlaşma temin edilemez veya sağlanamazsa, aynı ceza için tarhiyat sonrası uzlaşma talep edilemez (VUK ek m. 11/3).

## Adımlar

### 1. Hangi aşamadayız?

> Maliye'den gelen son belge nedir?
> A. İnceleme raporu (tarhiyat öncesi) — Ek m. 11 aktif
> B. Tarhiyat tebliği (vergi/ceza belirlendi) — Ek m. 1 aktif
> C. Uzlaşma toplantı çağrısı (başvurduk) — pazarlık aşaması

### 2. Tutar maruziyeti

| Kalem | Maliye iddiası | Tutar |
|---|---|---|
| Asıl vergi farkı | [...] | [...] |
| Vergi ziyaı cezası (VUK m. 344) | [%X] | [...] |
| Usulsüzlük cezası | [...] | [...] |
| **TOPLAM** | | [...] |

### 3. Uzlaşma indirim hesabı

**Tarhiyat öncesi (Ek m. 11):**
- Vergi aslı: uzlaşma kapsamı DIŞINDA (7524 s.K. m. 14 ile "vergi" ibaresi ek m. 11'den çıkarıldı; uzlaşma yalnız vergi ziyaı cezası ile eşiği aşan usulsüzlük/özel usulsüzlük cezaları için yapılır)
- Ceza: %50'ye kadar indirim (doğrulanmadı)
- Gecikme zammı: durdurulur (uzlaşma tarihine kadar)

**Tarhiyat sonrası (Ek m. 1):**
- Vergi aslı: uzlaşma kapsamı DIŞINDA (7524 s.K. m. 14 ile "vergi" ibaresi ek m. 1'den çıkarıldı; aynı kapsam sınırı geçerli)
- Ceza: **%75 indirim** (doğrulanmadı)
- Gecikme zammı: uzlaşmaya kadar işler

### 4. Dava alternatifi maliyet karşılaştırma

| Senaryo | Maliyet |
|---|---|
| Uzlaşma (Ek m. 11 ile) | Vergi aslı tam tahsil (uzlaşma kapsamı dışı) + Ceza %50 (doğrulanmadı) + zaman ~1-3 ay |
| Uzlaşma (Ek m. 1 ile) | Vergi aslı tam tahsil (uzlaşma kapsamı dışı) + Ceza %25 (doğrulanmadı) + zaman ~3-6 ay |
| Vergi davası (kazanırsa) | %0 + faiz iade (geç) + vekalet ücreti karşı tarafa |
| Vergi davası (kaybederse) | %100 vergi + %100 ceza + gecikme + dava masrafı + vekalet |
| Karma — uzlaş + dava | [kombinasyon] |

**Kazanma olasılığı tahmini:** ArthurLegal MCP (`tr_`)'den emsal kararlara bakarak.

```
tr_ictihat_ara(
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  query="<konu>",
  date_from="2022-01-01"
)
```

### 5. Kabul edilebilir uzlaşma aralığı

- **Tabakalı hesap:** En düşük (Maliye'nin kabul edebileceği) ve en yüksek (bizim red noktamız) arasında.
- **Anchor:** Maliye'nin ilk teklifi vs. son teklif görüşülmek için.
- **Walk-away noktası:** Bu tutarın üstünde uzlaşma KABUL EDİLMEZ, dava açılır.

### 6. [Müvekkil] onay matriksi

| Tutar | Yetkili |
|---|---|
| < 1M TL | Mali İşler Müdürü + Hukuk Counsel |
| 1M - 10M TL | CFO ([CFO ADI]) + Hukuk Direktörü |
| 10M - 100M TL | CFO + CEO |
| > 100M TL | CEO + YK |

**Tutardan bağımsız eskalasyon:**
- TP tarhiyatı ([Ana ortak / ilişkili taraf] ilgili) → CEO + Başkan
- [HALKA AÇIK İŞTİRAK] ilgili → KAP açıklama kontrolü + IR Başkanlığı
- VUK m. 359 kaçakçılık iddiası → ceza avukatı + CEO + YK

### 7. Uzlaşma talep dilekçesi

```markdown
[Vergi Dairesi Başkanlığı] [Uzlaşma Komisyonu]

Konu: Uzlaşma Talebi (VUK Ek m. 11 / Ek m. 1)

[Tarih, sayı] sayılı [tarhiyat / inceleme raporu] hakkında, vergi ve ceza
tutarları üzerinde uzlaşmaya varmayı talep ederiz.

İlgili işlem: [tarif]
Uzlaşmayı talep eden tutar: [...]

[Yetkili imza]
[Müvekkil]
Tarih: GG.AA.YYYY
```

### 8. Uzlaşma toplantısına hazırlık

- **Pozisyon paketi:** Hukuki argümanlar, emsal kararlar (bizim lehimize)
- **Tutar pozisyonu:** Tabaka açık, walk-away noktası net
- **Kim katılır:** Genelde Mali İşler + Hukuk Counsel + dış vergi danışmanı (Büyük 4)
- **Yetki dökümanı:** Uzlaşma kararı için yetki belgesi (yetkili tutar limiti ile)

## Çıktı

```markdown
[ÜST BAŞLIK]

# Uzlaşma Değerlendirme — [Tarhiyat sayı / Konu]

## ⚠️ İnceleyen notu
- **Aşama:** Ek m. 11 (öncesi) / Ek m. 1 (sonrası)
- **Süre:** [...] (kalan: N gün)
- **Tavsiye:** UZLAŞMA ÖNERİLİR / ÖNERİLMEZ / KARMA STRATEJİ
- **Kabul edilebilir aralık:** [TL min - TL max]
- **Yetki:** [Counsel/Direktör/CFO/CEO]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (Danıştay [N] emsal); ArthurLegal MCP (`tr_`)
- **KAP:** [N/A / gerekli]
- **Reviewer bekleyen:** N adet

## Maliye iddiası vs. [Müvekkil] pozisyonu
[tablo]

## Uzlaşma indirim hesabı
[Ek m. 11 vs Ek m. 1 karşılaştırma]

## Dava alternatifi karşılaştırma
[maliyet matrisi + kazanma olasılığı]

## Önerilen uzlaşma aralığı
**Hedef:** [TL]
**Walk-away:** [TL]
**Müzakere stratejisi:** [...]

## Uzlaşma talep dilekçesi (taslak)
[şablon — doldurulmuş]

## Sonraki adımlar

> 1. **Uzlaşma talep dilekçesini Maliye'ye sun** — yetki belgesi ile
> 2. **CFO eskalasyon notu** — pozisyon ve walk-away onayı
> 3. **Dış vergi danışmanı brief** — toplantıya katılım için
> 4. **Dava paralel hazırlık** — `/arthurlegal:tax-legal-tax-litigation-prep` (uzlaşılmazsa)
> 5. **Bekle** — Maliye karşı teklif gönderebilir

**One question I'd ask:** [örn. "Maliye komisyon üyesi geçmişte aynı tip vergi davalarında esnek mi katı mı? Bilgi varsa pozisyon ona göre."]
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
