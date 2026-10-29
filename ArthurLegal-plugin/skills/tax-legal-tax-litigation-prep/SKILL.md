---
name: tax-legal-tax-litigation-prep
description: >
  Vergi davası hazırlık: İYUK m. 7 (vergi mahkemesinde 30 gün) süre kontrolü, görevli
  ve yetkili vergi mahkemesi, kanun yolu (BİM istinafı, Danıştay temyizi, parasal
  sınırlar), dava dilekçesi taslağı, tahsilin durması ve yürütmenin durdurulması
  (İYUK m. 27/4), emsal Danıştay kararları.
  Dış vergi avukatı brief'i ile entegre.
user-invocable: true
---

# Tax Litigation Preparation — Vergi Davası (Vergi Mahkemesi → BİM → Danıştay)

## ⏰ ÖN-KONTROL — Süre

Bu skill her çalıştırıldığında **ilk işlem süre hesabı**:

> Vergi tarhiyat / idari para cezası tebliğ tarihi nedir?
> İYUK m. 7 — **30 gün** içinde **vergi mahkemesinde** iptal davası açılmalı (ilk derece vergi mahkemesidir — 2576 s.K. m. 6).
> Bu süre **hak düşürücü**dür.

Eğer kalan süre < 5 gün → 🔴 ACİL — dış vekille derhal koordinasyon.

## Destination check

- **Mali İşler + Hukuk değerlendirme** → "GİZLİDİR – HUKUK + MALİ İŞLER VERGİ DAVA STRATEJİ"
- **Dış vergi avukatı brief'i** → "VERGİ DAVA BRIEF – AVUKATLIK K. m. 36 KAPSAMINDA"
- **Vergi mahkemesine sunulacak dilekçe taslağı** → resmi format, "TASLAK" + dış vekil onayı sonrası

## Adımlar

### 1. Görevli mahkeme, yetki ve kanun yolu

| Aşama | Merci | Süre | Dayanak |
|---|---|---|---|
| İlk derece | **Vergi mahkemesi** — vergiyi tarh ve tahakkuk ettiren / cezayı kesen dairenin bulunduğu yerdeki vergi mahkemesi | Tebliğden itibaren 30 gün | İYUK m. 7/1, m. 37; 2576 s.K. m. 6 |
| İstinaf | Bölge idare mahkemesi | Kararın tebliğinden itibaren 30 gün | İYUK m. 45/1 — konusu parasal sınırı (kanun metninde 31.000 TL) geçmeyen vergi davası kararları kesindir |
| Temyiz | Danıştay | Kararın tebliğinden itibaren 30 gün | İYUK m. 46/1-b — yalnız konusu parasal sınırı (kanun metninde 920.000 TL) aşan vergi davalarında; ayrıca BİM'in ilk derece kararını kaldırıp yeniden karar verdiği hallerde (m. 46/2; istisnaları maddede) |

**Parasal sınırlar** her yıl yeniden değerleme oranında artırılır; istinaf ve temyiz açısından **davanın açıldığı tarihteki** sınır esas alınır (İYUK ek m. 1). Güncel tutarı her dosyada teyit et.

**Temyiz aşamasında Danıştay vergi dava daireleri** — ⚠️ daire iş bölümü değişebilir; aşağıdaki tablo doğrulanmadı, temyizden önce güncel iş bölümünü teyit et:

| Daire | Konu |
|---|---|
| **Danıştay 3. Daire** | KDV, ÖTV, gümrük vergileri |
| **Danıştay 4. Daire** | Gelir ve kurumlar vergisi (yıllık beyanname kaynaklı) |
| **Danıştay 7. Daire** | Damga vergisi, banka muameleleri, MTV, harçlar |
| **Danıştay 9. Daire** | Vergi cezaları (her vergi türü için ceza), tarhiyat, vergi kaçakçılığı |
| **Vergi Daireleri DDK** | Daire çelişkilerini birleştirme |

**[Müvekkil] örnek (temyiz aşamasında olası daire — teyit et):**
- [HALKA AÇIK İŞTİRAK] KDV iadesi reddi → **3. Daire**
- [RAFİNERİ] ÖTV mahsubu reddi → **3. Daire**
- TP tarhiyatı (KVK m. 13) → **4. Daire**
- Büyük sözleşme damga vergisi tarhiyatı → **7. Daire**
- Vergi ziyaı cezası → **9. Daire**

### 2. Dava dilekçesi şablonu (İYUK m. 3)

```markdown
[İL] ( ). VERGİ MAHKEMESİ BAŞKANLIĞINA

DAVACI:
[Müvekkil] — [VKN, sicil, adres]
Vekili: [Av. ad, baro sicil, adres, KEP]

DAVALI:
[Tarhiyatı yapan / cezayı kesen] Vergi Dairesi Müdürlüğü (ya da Başkanlığı) — [adres]

DAVA KONUSU:
[Tarihli, sayılı] tarhiyat işlemi / idari para cezası kararının iptali [ve — yalnız İYUK m. 27/4 istisnalarında — yürütmenin durdurulması] talebidir.

İŞLEMİN TARİFİ:
[Maliye'nin tebliğ ettiği belge — tarih, sayı, tutar, ceza]
Tarafımıza tebliğ tarihi: GG.AA.YYYY
Dava açma süresi: [tebliğden 30 gün sonu — tarih]

I. OLAYLAR

[Tarihsel olarak — vergi konusu işlem, beyanname, inceleme, tarhiyat]

II. HUKUKİ DAYANAĞIMIZ

A. Tarhiyatın hukuki dayanaktan yoksun olduğu
   [Argüman 1] — Dayanak: [VUK m. X, KVK m. Y, KDVK m. Z]

B. [Argüman 2] — [Emsal Danıştay kararı: `[ArthurLegal MCP (`tr_`) — danistay — esas/karar — GG.AA.YYYY]`]

C. [Argüman 3 — yedek]

III. YÜRÜTMENİN DURDURULMASI TALEBİMİZ (İYUK m. 27) — [YALNIZ m. 27/4 İSTİSNALARINDA; tarhiyata karşı davada dava konusu kısmın tahsili kendiliğinden durduğundan bu bölümü çıkarın]

Aşağıdaki sebeplerle yürütmenin durdurulması talep edilmektedir:
1. [Telafisi güç zarar] — örn. tahsil edilirse şirket nakit akışı bozulur, üretim etkilenir
2. [Açık hukuka aykırılık] — yukarıdaki argümanlardan en güçlüsü

IV. SONUÇ VE TALEP

Yukarıdaki açıklamalar ışığında:
1. [Yalnız m. 27/4 istisnasında:] Yürütmenin durdurulmasına,
2. [İşlemin/cezanın] iptaline,
3. Yargılama gideri ve vekalet ücretinin davalıya yüklenmesine,

karar verilmesi saygıyla arz ve talep olunur.

Tarih: GG.AA.YYYY

Davacı Vekili: [imza]

EKLER:
1. Vekaletname
2. Tarhiyat kararı (tebliğ örneği)
3. [İlgili sözleşme/belge]
4. [Emsal Danıştay kararları]
```

### 3. Tahsilin durması ve yürütmenin durdurulması (İYUK m. 27) — KRİTİK

**Kural (m. 27/4):** Vergi mahkemesinde vergi uyuşmazlığından doğan davanın açılması, tarh edilen vergi, resim, harç ve benzeri mali yükümler ile bunların zam ve cezalarının **dava konusu edilen bölümünün tahsilini kendiliğinden durdurur**. Bu davalarda ayrıca yürütmenin durdurulması istemeye gerek yoktur.

**İstisnalar — tahsil durmaz, yürütmenin durdurulması istenir (m. 27/4):**
- İhtirazi kayıtla verilen beyannameler üzerine yapılan işlemlere karşı davalar
- Tahsilat işlemlerine karşı açılan davalar (ör. ödeme emri)
- m. 26/3'e göre işlemden kaldırılan ve yeniden işleme konulan dosyalar

Yürütmenin durdurulması şartları (m. 27/2), ikisi birlikte:
- **Telafisi güç veya imkânsız zararlar doğacağı**
- **İdari işlemin açıkça hukuka aykırı olduğu**

İstisna hallerinde yüksek tutarlarda **telafisi güç zarar** daha kolay gösterilir (nakit etkisi, operasyon).

**Tehir-i icra (AATUHK)** — vergi tahsil aşamasına girdiyse ayrı bir paralel yol.

### 4. ArthurLegal MCP (`tr_`) — emsal Danıştay kararları

```
tr_ictihat_ara(
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  query="<dava konusu>",
  date_from="2022-01-01"
)
```

Ayrıca **VDDK kararları** (birleştirici):

```
tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="VDDK",
  query="<konu>",
  date_from="2020-01-01"
)
```

### 5. sektöre-özel notlar

- **Tutar > 10M TL** → CFO + Başkan + CEO eskalasyon
- **[HALKA AÇIK İŞTİRAK] ilgili** → KAP açıklama (önemli dava — SPK Tebliğ II-15.1)
- **Yüksek tutarlı Maliye davası** → MASAK bildirim eşiği? (UNSCR/AML kontrolleri)
- **AYM bireysel başvuru** — kanun yolları tükendikten sonra (BİM kesin kararı ya da Danıştay temyiz kararı) mülkiyet hakkı ihlali argümanı

### 6. Dış vergi avukatı brief'i

`/arthurlegal:litigation-legal-outside-counsel-brief` pattern'ını kullan ama vergi-spesifik:

- **Daire deneyimi:** Bu büronun ilgili daire ile geçmişi (oranı?)
- **VDDK kararına itiraz deneyimi**
- **Tarihsel kazanma oranı (büronun)** — kendileri verir mi?

## Çıktı

```markdown
[ÜST BAŞLIK]

# Tax Litigation Prep — [Tarhiyat sayı / Konu]

## ⚠️ İnceleyen notu
- **Tebliğ tarihi:** GG.AA.YYYY
- **Dava süresi sonu:** GG.AA.YYYY (kalan: N gün) 🔴 🟠 🟡
- **Görevli mahkeme:** [İL] ( ). Vergi Mahkemesi — kanun yolu: [BİM istinafı / kesin] → [Danıştay temyizi: m. 46'ya göre açık mı?]
- **Tahsil kendiliğinden durdu mu (m. 27/4):** [evet / hayır — istisna: …] · **YD talebi:** [yalnız istisnada]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (Danıştay [N] emsal); ArthurLegal MCP (`tr_`) (VUK/KDVK m. [N])
- **Eskalasyon zinciri:** [tetiklendi?]
- **KAP açıklama:** [N/A / hazırlanıyor]
- **Reviewer bekleyen:** N adet

## Tarhiyatın özeti

| Kalem | Maliye iddiası | Bizim pozisyon | Tutar |
|---|---|---|---|
| ... | ... | ... | ... |

## Hukuki argümanlar
[A, B, C — emsal kararlarla]

## Dava dilekçesi taslağı (dış vekil revize için)
[yukarıdaki şablon]

## Yürütmenin durdurulması analizi
[telafisi güç zarar + hukuka aykırılık]

## Emsal Danıştay kararları
[ArthurLegal MCP (`tr_`)'den çıkan tablolar]

## Sonraki adımlar

> 1. **Dış vergi avukatı brief'i** — `/arthurlegal:litigation-legal-outside-counsel-brief` (vergi davası için)
> 2. **CFO + Başkan eskalasyon paketi**
> 3. **KAP açıklama metni** ([HALKA AÇIK İŞTİRAK] ilgili büyük tarhiyat)
> 4. **Uzlaşma paralel değerlendirme** — `/arthurlegal:tax-legal-uzlasma-eval` (alternatif yol)
> 5. **Daha fazla bilgi** — [...]

**One question I'd ask:** [örn. "Aynı daire son 12 ayda benzer [Müvekkil]/sektör davalarında nasıl karar verdi? Maliye lehine eğilim varsa strateji değişir."]
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
