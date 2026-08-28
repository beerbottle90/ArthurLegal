# İsviçre Emtia Ticareti Hukuku & Uyum — Kullanım Rehberi

> **Erişim:** OpenCaseLaw.ch MCP (İsviçre kanunları + içtihat, auth yok ✅) + SECO WebFetch +
> OpenSanctions API. Bu rehber İsviçre **emtia ticareti** (commodity trading) uyum çerçevesini
> ve canlı kaynak prosedürünü tanımlar.
>
> **Ne zaman gerekir?** Grubun **İsviçre merkezli bir emtia ticaret kolu** varsa — ham
> petrol, rafine ürün, LNG, doğal gaz veya karbon (emisyon) ticareti. Cenevre küresel ham
> petrol ticaretinin merkezidir (Vitol, Gunvor, Trafigura, Mercuria bu şehirde kuruludur) ve
> İsviçre'nin AML, yaptırım ve kurumsal due diligence mevzuatı böyle bir kolun operasyonlarını
> **doğrudan** yönetir. Çok ofisli bir ticaret masası varsa yargı çevresi çakışmaları da bu
> rehberin konusudur.

---

## 1. İsviçre emtia ticareti rejiminin mantığı

**Lisans yok, ama genişleyen bir uyum ağı.** FINMA (finansal piyasa otoritesi) **fiziksel** emtia
ticaretini (petrol, metal, tarım) düzenlemez — Cenevre merkezli bir ham petrol trader'ı prensipte
FINMA lisansı olmadan çalışır. Ancak şu yükümlülükler giderek artar:

1. **Kara para aklama (AML/GwG)** — finansman/ödeme aracılığı yapıldığında
2. **Yaptırım uyumu (SECO/Embargo Act)** — özellikle Rusya-komşu akışlarda kritik
3. **Kurumsal due diligence (OR 964)** — gayrı-finansal raporlama, çatışma mineralleri, çocuk işçiliği
4. **Finansal hizmet (FinSA/FinIA)** — türev/finansal enstrüman masaları kapsama girerse

> **Dil notu:** İsviçre federal kanunları DE/FR/IT resmî dillerde. OpenCaseLaw.ch hepsini çeker —
> dil kısıtı koyma, üç dilde de ara. Atıfta orijinal + TR çeviri birlikte sun.

---

## 2. Kritik kanunlar + canlı kaynak

| Konu | Kanun (SR) | Çekme yöntemi |
|------|-----------|---------------|
| **Kara para aklama** | GwG/AMLA — **SR 955.0** | `get_law(sr_number="955.0", article="...")` |
| **Yaptırım temeli** | Embargo Act (EmbG) — **SR 946.231** | `get_law(sr_number="946.231")` |
| **Kurumsal due diligence** | OR (Borçlar) Art. **964a–964l** — SR 220 | `get_law(sr_number="220", article="964a")` |
| **Finansal hizmet** | FinSA/FIDLEG — SR 950.1 | `get_law(sr_number="950.1")` |
| **Finansal kurum** | FinIA/FINIG — SR 954.1 | `get_law(sr_number="954.1")` |
| **Tahkim (ticari uyuşmazlık)** | IPRG m.176-194 — SR 291 | `get_law(sr_number="291", article="176")` |

**OpenCaseLaw.ch araçları (bağlı, auth yok):**
- `search_laws(query="...", sr_number="955.0")` — kanun içinde tam metin arama (DE/FR/IT)
- `get_law(sr_number="...", article="...", language="de|fr|it")` — madde tam metni
- `search_decisions(query="...")` — emtia/ticaret uyuşmazlığı içtihadı

---

## 3. SECO — Yaptırım & İhracat Kontrolü (BİRİNCİL — trading uyumu)

**State Secretariat for Economic Affairs (SECO)** Embargo Act (SR 946.231) uyarınca İsviçre
yaptırımlarını yönetir. [ŞİRKET ADI] Trading karşı taraf taramasında kritik.

**Resmi kaynak (WebFetch ✅):**
```
https://www.seco.admin.ch/seco/en/home/Aussenwirtschaftspolitik_Wirtschaftliche_Zusammenarbeit/Wirtschaftsbeziehungen/exportkontrollen-und-sanktionen/sanktionen-embargos.html
```
- **Consolidated XML listesi** (06.12.2023'ten yeni format) — otomatik tarama için
- Excel tam veritabanı + XSD şeması + örnek dosyalar
- Online arama uygulaması (yaptırım adresi sorgulama)

**OpenSanctions entegrasyonu:** SECO listesi `ch_seco_sanctions` dataset'i olarak OpenSanctions'ta
da var — mevcut `POST /match/default` taraması SECO'yu kapsar (bkz. `opensanctions-rehberi.md`).

**İhlal yaptırımı:** 5 yıla kadar hapis + 1M CHF'ye kadar para cezası.

---

## 4. [ŞİRKET ADI] Trading için tipik kullanım pattern'ları

### 4.1 Karşı taraf KYC + yaptırım taraması (ham petrol/LNG alım-satım)

```
ADIM 1: OpenSanctions POST /match → karşı taraf (OFAC+AB+BM+SECO ch_seco)
ADIM 2: SECO WebFetch → İsviçre özel önlemleri/donmalar teyit
ADIM 3: GwG SR 955.0 → finansman/ödeme aracılığı AML yükümlülüğü doğuyor mu?
ADIM 4: Atıf → [CH Mevzuat — GwG SR 955.0 Art.X — OpenCaseLaw — GG.AA.YYYY]
        + [SECO — yaptırım taraması — GG.AA.YYYY] + [OpenSanctions API — skor X]
```

### 4.2 Trade finance / ödeme yapısı (akreditif, prepayment)

```
ADIM 1: GwG kapsamı — trader ödeme aracısı/finansör konumunda mı?
ADIM 2: Akreditif/garanti → İsviçre OR (Borçlar) hükümleri (get_law SR 220)
ADIM 3: Yaptırım klozu (sanctions clause) — SECO + OFAC + AB çakışması
```

### 4.3 Kurumsal due diligence raporlaması (OR 964)

```
ADIM 1: get_law(sr_number="220", article="964a") → eşik (500 FTE, 20M bilanço / 40M ciro)
ADIM 2: 964j → çatışma mineralleri + çocuk işçiliği due diligence (varsa)
ADIM 3: Ticaret kolu eşiği aşıyorsa → yıllık gayrı-finansal rapor yükümlülüğü
```

---

## 5. Atıf disiplini

- `[CH Mevzuat — {kanun} SR:{no} Art.{no} — OpenCaseLaw — GG.AA.YYYY]` — OpenCaseLaw'dan çekilen kanun
- `[SECO — yaptırım/embargo — {konu} — GG.AA.YYYY]` — seco.admin.ch'ten çekilen
- `[OpenSanctions API — ch_seco match skoru X — GG.AA.YYYY]` — SECO dahil OpenSanctions taraması
- `[OpenCaseLaw.ch — {mahkeme} — {ref} — GG.AA.YYYY]` — ticaret uyuşmazlığı içtihadı

**Asla** çekmediğin İsviçre kaynağına atıf koyma — `[model bilgisi — doğrulayın]` kullan.

---

## 6. Sınırlamalar

- **Lisans yok ≠ düzenleme yok:** Fiziksel ticaret lisanssız ama AML/sanctions/due-diligence
  yükümlülükleri gerçek ve artıyor (FINMA AMLO-FINMA revizyonu — yürürlük 01.01.2027).
- **GwG kapsamı nüanslı:** Trader sadece fiziksel alım-satım yapıyorsa GwG dışı olabilir; ama
  finansman/ödeme/aracılık eklenince kapsama girer — her vakada ayrı değerlendir, `[review]`.
- **Türev/financial enstrüman:** Kâğıt ticareti (paper trading, futures, swaps) FinSA/FinIA
  kapsamına girebilir — fiziksel masadan farklı rejim.
- **Çok ülkeli çakışma:** Ticaret masasının farklı ülkelerdeki ofisleri farklı
  yaptırım rejimlerine tabi — İsviçre SECO + ABD OFAC + UK OFSI + AB aynı anda; en katı uygula.
- **Singapur rakip merkez:** Aynı emtia için Singapur hukuku alternatif olabilir (governing-law seçimi).

---

## 7. İlgili rehberler

- `switzerland-caselaw-rehberi.md` — İsviçre içtihat + Fedlex + fedlex-connector MCP
- `opensanctions-rehberi.md` — yaptırım taraması (SECO dahil)
- `yaptirim-tarama-rehberi.md` — [ŞİRKET ADI] yaptırım prosedürü
- `karsilastirmali-hukuk-rehberi.md` — governing-law seçimi (CH vs Singapur)
- energy-finance: `commodity-trade-compliance` skill (bu rehberi operasyonel kullanır)

---

## Versiyon disiplini

- Bu rehber **v1.10.0** (*Emtia Ticareti & Çok Dilli Kurulum*) ile eklendi.
- Kaynaklar 08.06.2026'da test edildi: OpenCaseLaw get_law (GwG 955.0, OR 964a) ✅ · SECO WebFetch ✅.

---

*Son güncelleme: 29.08.2026. İsviçre merkezli emtia ticaret kolları için uyum çerçevesi: AML/GwG + SECO yaptırım + OR 964 due diligence + FinSA. OpenCaseLaw.ch + SECO + OpenSanctions.*
