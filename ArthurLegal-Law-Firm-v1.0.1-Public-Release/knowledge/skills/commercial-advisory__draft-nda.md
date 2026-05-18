---
name: draft-nda
description: >
  NDA (gizlilik sözleşmesi) yazma/inceleme: tek/iki yönlü, sınırlı/genel kapsam,
  süre, ihlal yaptırımı, uyuşmazlık çözüm klozu, TBK m. 115 sorumsuzluk sınırı
  kontrolü, damga vergisi hesabı, KEP teslim notu. GREEN/YELLOW/RED triage.
user-invocable: true
---

# NDA Yazma / İnceleme

## Müvekkil pozisyonu

İlk soru: **Müvekkil bilgi sağlayan mı (A-tarafı) yoksa bilgi alan mı (C-tarafı)?**

- **Bilgi sağlayan (Disclosing Party):** sıkı koruma + ihlal yaptırımı + uzun süre + geniş kapsam
- **Bilgi alan (Receiving Party):** kapsam sınırı + makul önlem + kısa süre + standart yaptırım
- **Karşılıklı (Mutual):** her iki yönde dengeli — genelde iş ortaklığı + JV görüşmesi öncesi

## NDA türleri

| Tip | Senaryo |
|---|---|
| **One-way (tek yönlü)** | A bilgi verir, B alır (örn. satıcı diligence) |
| **Mutual (iki yönlü)** | A ↔ B karşılıklı (örn. JV görüşmesi) |
| **Multi-party** | 3+ taraf (örn. konsorsiyum) |
| **NDA + non-compete** | Gizlilik + rekabet etmeme (ihtiyatlı — TBK 27 sınırı) |
| **NDA + non-solicit** | Personel transferi yasak |

## Standart maddeler

### 1. Taraflar + amaç

- Net taraf tanımı (tüzel kişi + adres + KEP)
- **Amaç** dar tanım — "X anlaşması müzakeresi" (genel "iş görüşmesi" zayıf)

### 2. "Gizli bilgi" tanımı

- **Yazılı veya sözlü, [N] gün içinde "GİZLİ" işaretiyle yazılı teyit edilen** bilgi
- **Hariç tutulan:** (a) zaten kamuya açık, (b) alıcının önceden bildiği, (c) üçüncü taraftan yasal yolla edinilen, (d) bağımsız geliştirilen

### 3. Yükümlülükler

- **Makul önlem** (taraflar kendi gizli bilgilerine gösterdikleri özen)
- Belirli personel ile sınırlı paylaşım ("need-to-know")
- Yazılı izin olmadan kopyalama / 3. taraf paylaşımı yasak

### 4. Süre

- **Geçerlilik:** sözleşme tarihi - [N] yıl
- **Yükümlülük:** süre + post-termination [N] yıl (genelde 2-5 yıl)
- Çok uzun süre (10+ yıl) → TBK m. 27 hükümsüzlük riski

### 5. **TBK m. 115 — sorumsuzluk şartı sınırı**

⚠️ "Her türlü sorumluluğun reddi" tipi cümleler:
- **Ağır kusur** ile sebep olunan zarar için **kesin hükümsüzdür** (TBK m. 115/1)
- **Hafif kusur** için **yardımcı kişiler** (örn. avukat, mali müşavir) sınırlanabilir (m. 115/2)
- **Müvekkil bilgi sağlayan ise:** ihlal sonucu **gerçek zararının** karşılanmasını talep edebilmeli
- **Müvekkil bilgi alan ise:** sorumluluk sınırı (örn. "sözleşme bedeli × 2") kabul edilebilir

### 6. İhlal yaptırımı

- **Cezai şart (TBK m. 179):** belirli tutar — "her ihlal için X TL"
- **Tazminat:** fiili zararın tazmini (cezai şart üstüne)
- **İhtiyati tedbir** (HMK m. 389): ihlal devam ediyorsa mahkemeden tedbir

### 7. Uyuşmazlık çözüm klozu

| Senaryo | Önerilen kloz |
|---|---|
| Yurtiçi karşı yan | İstanbul mahkemeleri |
| Yurtdışı karşı yan | **ISTAC** İstanbul Tahkim Merkezi |
| Uluslararası — TR/EN | **ICC** Paris |

### 8. Diğer klozlar

- **Bütünlük (entire agreement):** Önceki müzakereler geçersiz
- **Bölünebilirlik:** Bir maddenin hükümsüzlüğü sözleşmenin tümünü etkilemez
- **Devir yasağı** (assignment): Karşı yan NDA yükümlülüğünü 3. tarafa devredemez
- **Hukuk seçimi:** Türk Hukuku
- **Damga vergisi:** Hangi taraf öder? (genelde her iki taraf kendi nüshası)

## Damga vergisi

NDA → **binde 9,48** (DVK Tablo I, sözleşme genel, 2026 varsayımsal).

**Bedelsiz NDA** (ön müzakere, "iş yapma yükümlülüğü" yoksa):
- Bazı yorumlara göre damga doğmaz (TBK m. 502 vd. vekalet ücreti tartışmalı)
- Güvenli yaklaşım: yine de damga öde (4 kat ceza riskinden kaçın)

## KEP teslim

Müvekkilin KEP adresi varsa imzalı PDF'i KEP üzerinden gönder → delil değeri 5070 sayılı K. çerçevesinde.

## GREEN / YELLOW / RED triage

| Renk | Anlamı | Eylem |
|---|---|---|
| 🟢 GREEN | Standart, makul, müzakereye uygun | İmza tavsiye edilebilir |
| 🟡 YELLOW | Kabul edilebilir ama 1-3 madde fix | Karşı yana redline gönder |
| 🟠 ORANGE | Önemli sorunlar — müzakere şart | Müvekkile detaylı brief |
| 🔴 RED | TBK 115 ihlali, ağır asimetri, kanuna aykırı kloz | **İmzalama** — alternatif öner |

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# NDA İnceleme / Yazımı — [Matter]
Müvekkil pozisyonu: A-tarafı / B-tarafı / C-tarafı (Disclosing / Mutual / Receiving)
NDA tipi: One-way / Mutual

## ⚠️ İnceleyen notu
- Kaynaklar: Mevzuat MCP [✓ TBK m. 27/115/179] / Yargı MCP [✓ N emsal]
- Damga vergisi tahmini: [TL]
- Bulgu sınıflandırma: 🔴 N – 🟠 N – 🟡 N – 🟢 N
- Genel sınıflandırma: 🟢 GREEN / 🟡 YELLOW / 🟠 ORANGE / 🔴 RED

## Madde bazlı bulgular
| Madde | Bulgu | Severity | Önerilen düzeltme |
|---|---|---|---|
| 4 — Gizli bilgi tanımı | "Tüm bilgi" çok geniş | 🟡 | "[N] gün içinde GİZLİ işaretli teyit" ekle |
| 7 — Süre | 20 yıl çok uzun (TBK 27 risk) | 🟠 | 5 yıl + post-termination 2 yıl |
| 9 — Sorumsuzluk | "Her türlü sorumluluk reddi" (TBK 115 ihlal) | 🔴 | Ağır kusur istisnası ekle |

## Önerilen aksiyon
[İmza tavsiye / Redline gönder / Müvekkille konuş / İmzalama]

## Sonraki adımlar
- /commercial-advisory:review-contract (yeni taslak hazırla)
- KEP teslim hazır → müvekkilin onayı sonra karşı yana
```
