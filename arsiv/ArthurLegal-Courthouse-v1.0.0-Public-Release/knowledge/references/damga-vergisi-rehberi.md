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

## Vergi yargısında damga vergisi tarhiyatı denetimi

> ⚖️ Bu rehber, vergi mahkemesinde **damga vergisi tarhiyatı/cezası iptali** davasında hâkimin kontrol edeceği unsurları yapılandırır. Mükellef lehine optimizasyon/kaçınma stratejisi kapsam dışıdır.

### Hâkim için denetim noktaları

1. **Verginin konusu (DVK m. 1):** Tarhiyata konu kâğıt, DVK (1) sayılı tabloda sayılan bir belge mi? "Kâğıt" tanımı + imza/ibraz şartı.
2. **Düzenlenme yeri:** Belge Türkiye'de mi düzenlendi / Türkiye'de hükmünden mi yararlanıldı (yabancı kaynaklı kâğıtlar — DVK m. 1/son).
3. **Matrah:** Belli para tutarı; yabancı para günün TCMB kuruyla TL'ye çevrilir; nispi/maktu ayrımı.
4. **Nispet & nüsha:** İlgili nispet (her yıl RG'de güncel tarife — Mevzuat MCP teyidi); nüsha sayısı (DVK m. 5) ve **azami had (DVK m. 14)** doğru uygulanmış mı.
5. **İstisna (2) sayılı tablo:** İhracat ve ihracata yönelik işlemler, bazı resmî/ticari belgeler — istisna kapsamı doğru değerlendirilmiş mi.
6. **Mükellef & sorumluluk (DVK m. 3, 24):** Birden fazla imzalayan, resmî daireye ibraz eden tarafların müteselsil sorumluluğu.
7. **Usul:** Tebliğ (VUK), tarh zamanaşımı (VUK m. 114), ceza (vergi ziyaı / usulsüzlük) illiyeti.

> Sonuç (iptal/ret/kısmen iptal) **hâkim/heyet takdiridir**; norm ve tarife **Mevzuat MCP'den verbatim** teyit edilir.

---

## Damga vergisi karar matrisi

| Sözleşme tutarı | Aksiyon |
|---|---|
| < 500K TL | Standart akış, damga = sözleşme bedeli × 0,00948 |
| 500K - 5M TL | Sözleşmeler Yöneticisi onayında damga maliyeti dahil edilmeli |
| 5M - 50M TL | Counsel + CFO koordinasyonu; damga optimizasyon kontrolu |
| > 50M TL | Direktör seviyesi + vergi danışmanı görüşü zorunlu; sözleşme yeri analizi |
| Yabancı para + büyük | İlişkili taraf işlemi mi? Transfer pricing belgesi + damga birlikte |
| İhracat | (2) sayılı Tablo istisna kontrolu; **istisna yoksa damga var** |
