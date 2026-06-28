# Damga Vergisi – Sözleşme Maliyeti Hesabı (Hızlı Rehber)

> 488 sayılı Damga Vergisi Kanunu (DVK) + (1) sayılı Tablo.
> **2026 oranları için Mevzuat MCP'den teyit alın.**

## Temel oran (B2B sözleşmeleri)

**Genel sözleşmeler:** binde 9,48 (2025 — 2026 için Mevzuat MCP teyit)
**Hesap:** Sözleşme bedeli × 0,00948 = Damga vergisi

**Örnek:**
- Sözleşme bedeli: 1.000.000 TL
- Damga: 1.000.000 × 0,00948 = **9.480 TL**

## Önemli özelliği

- **Her nüsha ayrı vergiye tabi.** İki nüsha imzalanırsa damga × 2.
- **Sözleşmenin TR'de düzenlenmesi yeterli** — bedel yabancı paradaysa kur ile çevrilir.
- **Tarafların eşit paylaşımı varsayılır** (DVK m. 24) — sözleşmede aksine hüküm yoksa.
- **E-imza / KEP'le imzalanan da damga konusu** — fiziki nüsha şart değil.

## İstisnalar (kontrol edilmesi gerekenler)

DVK (2) sayılı Tablo bazı işlemleri muaf tutar:
- Kamu kurumlarıyla yapılan bazı sözleşmeler
- İhracat / serbest bölge işlemleri (kısmi)
- Bazı kredi sözleşmeleri (BSMV ile değişim)
- Yargı süreci belgeleri (mahkeme kararı ayrı vergi)

**Pratik:** Bir sözleşmeyi imzalamadan önce DVK (1) ve (2) tablolarına bakmadan "muaf" deme. Mevzuat MCP'den `search_kanun(mevzuat_adi="488")` ile teyit.

## En sık sözleşme türleri ve oranları

| Sözleşme türü | Oran |
|---|---|
| Genel hizmet/ürün sözleşmesi | binde 9,48 |
| Kira sözleşmesi | binde 1,89 (yıllık kira bedeli üzerinden) |
| Süresiz kira | yıllık kira × 9,48 binde |
| İş sözleşmesi (belirli süreli) | binde 9,48 (toplam bedel üzerinden) |
| Kefalet sözleşmesi | binde 9,48 (kefalet tutarı) |
| Vekalet (ücretli) | binde 9,48 |
| Hizmet alım/satım | binde 9,48 |

## Hesaplama akışı (her contract review'da)

1. Sözleşme bedeli netleştir (KDV hariç tutar — DVK matrahı KDV'yi içermez)
2. Yıllık mı toplam mı belirsizse: süresiz/uzun süreli sözleşme = yıllık matrah × 9,48
3. Nüsha sayısı × damga = toplam damga maliyeti
4. Taraflar arası paylaşımı sözleşmede ara — yoksa varsayılan 50/50
5. Beyan ve ödeme: sözleşme imza tarihinden 30 gün içinde (DVK m. 22)

## Çıktı şablonu

```
DAMGA VERGİSİ MALİYETİ
────────────────────────────────
Sözleşme bedeli (KDV hariç):    [TL]
Oran:                           binde 9,48
Hesaplanan damga (tek nüsha):   [TL]
Nüsha sayısı:                   [N]
Toplam damga:                   [TL]

Paylaşım: [Eşit / Karşı taraf / Bizim] 
Şirket payı (tahmini):           [TL]

⚠ İstisnaya tabi mi? [Evet/Hayır — neden]
⚠ KDV iadesi varsa damga geri alınamaz (öder, gider yazılır)
```

## 2026 yılı güncel parametreler

Aşağıdaki tutarlar yıllık güncellenir — **her yıl Ocak'ta Mevzuat MCP'den teyit:**

- Damga vergisi azami had (her bir kağıt için): [Mevzuat MCP — doğrulayın]
- Genel oran (binde): [Mevzuat MCP — doğrulayın]
- 488 (1) sayılı Tablo güncel tutarları: [Mevzuat MCP — search_kanun("488")]

---

## [ŞİRKET ADI] için özel örnek senaryolar

### Örnek 1: Ham petrol ithalat sözleşmesi ([ANA ORTAK] → [RAFİNERİ])

**Senaryo:** [ŞİRKET ADI] A.Ş. (STAR adına), [ŞİRKET ADI] Trading SA Cenevre'den 200M USD'lik ham petrol alıyor (1 yıllık çerçeve).

**Damga analizi:**
- Sözleşme TR'de mi düzenleniyor? → **EVET ise** damga konusu (sözleşme yeri TR — DVK m. 1)
- Yabancı para → günün TCMB kuruyla TL'ye çevrilir
- 200M USD × 35 TL/USD (örnek) = 7 milyar TL
- 7M TL × 0,00948 = **66.360.000 TL damga** (tek nüsha)
- 2 nüsha → **132.720.000 TL**
- DVK m. 14 — azami had var (her yıl güncel — 2026 için Mevzuat MCP'den teyit)

**Pratik:** Bu büyüklükte damga eskalasyon eşiğini aşar — Hukuk Direktörü + Counsel + CFO koordinasyonu zorunlu. Alternatifler:
- **Sözleşmeyi yurt dışında düzenle** (örn. Cenevre'de imza) → damga doğmaz
- **İlişkili taraf işlemi tanımı** + transfer pricing belgesi → vergi inceleme dosyasını da kapsa
- **İmzayla ifadeyi farklı tut** — DVK yorumu için danışman

### Örnek 2: [HALKA AÇIK İŞTİRAK] → AB müşteri petrokimya satışı

**Senaryo:** [HALKA AÇIK İŞTİRAK], Almanya'da BASF'a 50M EUR'luk etilen satışı (yıllık çerçeve).

**Damga:**
- Sözleşme TR'de mi düzenleniyor? Genelde EVET ([HALKA AÇIK İŞTİRAK] Türk şirketi)
- 50M EUR × 38 TL/EUR = 1,9 milyar TL
- 1,9M TL × 0,00948 = **18 milyon TL damga** (tek nüsha)

**İhracat istisnası kontrolü:**
- DVK (2) sayılı Tablo m. 38: "İhracat ve ihracata yönelik bazı işlemler" — bazı belge tipleri muaf, ama **satış sözleşmesi genel olarak DEĞİL**.
- Sözleşme = damga konusu; fatura = damga konusu DEĞİL.

**Pratik:** [HALKA AÇIK İŞTİRAK] için kontrat strüktürü kritik — uzun yıllık çerçeve sözleşme yerine **bireysel sipariş bazlı** çalışma damga matrahını ürün-bazlı küçük tutarlara böler.

### Örnek 3: [İşletme Yeri] Özel Endüstri Bölgesi (ÖEB) — vendor sözleşmesi

**Senaryo:** [HALKA AÇIK İŞTİRAK], [ÖZEL ENDÜSTRİ BÖLGESİ]'de bir bakım hizmeti vendor'ı ile 5M TL'lik sözleşme.

**Damga:**
- 5M TL × 0,00948 = **47.400 TL** (tek nüsha)
- 2 nüsha → 94.800 TL
- ÖEB statüsü → 4737 sayılı kanunun ek istisnaları kontrol — bazı işlemlerde teşvik var, **ama genel damga rejimi devam eder**

### Örnek 4: [ELEKTRİK SANTRALİ] elektrik üretim — gün öncesi piyasası (EPİAŞ)

**Senaryo:** [ELEKTRİK SANTRALİ], EPİAŞ üzerinden günlük elektrik satışı yapıyor. Sözleşme yapısı: çerçeve EPİAŞ üyelik + günlük teklifler.

**Damga:**
- **EPİAŞ üyelik sözleşmesi** → damga konusu (bir kez ödenir)
- **Günlük teklifler** → "sözleşme" sayılır mı? EPİAŞ kuralları gereği "platform üzerinden eşleşme" olduğu için her gün ayrı damga doğmaz (DVK m. 1 yorumu — Maliye Bakanlığı görüşleri).
- **Pratik:** EPİAŞ üyelik damgaya tabi; günlük işlemler değil.

### Örnek 5: Damga optimizasyon — KEP üzerinden imza

**[ŞİRKET ADI] pratiği:** Kurumsal e-imza için KEP kullanılıyor (TTK 18/3). KEP imzalı sözleşme:
- DVK m. 1 ve 22 — KEP imzalı belge fiziki belge ile aynı statüde
- **Tek bir e-nüsha damgaya tabi** — fiziki nüsha sayısı arttırılamaz
- → **KEP imza damga maliyetini düşürür** (2 fiziki nüsha yerine 1 e-nüsha)

---

## [ŞİRKET ADI] için damga vergisi karar matrisi

| Sözleşme tutarı | Aksiyon |
|---|---|
| < 500K TL | Standart akış, damga = sözleşme bedeli × 0,00948 |
| 500K - 5M TL | Sözleşmeler Yöneticisi onayında damga maliyeti dahil edilmeli |
| 5M - 50M TL | Counsel + CFO koordinasyonu; damga optimizasyon kontrolu |
| > 50M TL | Direktör seviyesi + vergi danışmanı görüşü zorunlu; sözleşme yeri analizi |
| Yabancı para + büyük | İlişkili taraf işlemi mi? Transfer pricing belgesi + damga birlikte |
| İhracat | (2) sayılı Tablo istisna kontrolu; **istisna yoksa damga var** |
