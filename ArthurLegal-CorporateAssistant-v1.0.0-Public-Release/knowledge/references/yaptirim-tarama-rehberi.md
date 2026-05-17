# ArthurLegal Holding – Yaptırım (Sanctions) Tarama Rehberi

> **ArthurLegal Holding'nin commercial-legal'da "the thing that hurts" olarak işaretlediği konu.** Bu rehber, ticari süreç başında ZORUNLU yapılacak yaptırım kontrolünü tanımlar. Her yeni sözleşme + her vendor onboarding + her M&A diligence + her counterparty değişikliği için tetiklenir.

---

## ⚠️ Neden Şirket için kritik

ArthurLegal Holding yaptırım taraması yapısal olarak yüksek riskli — 4 ana faktör:

1. **Yurtdışı ana ortak yapısı** — AB 833/2014 (Rusya enerji sektörü) ve CAATSA m.232 (ABD karşı-yaptırım) için "Russian-related" değerlendirmesi yapan tedarikçi/banka var. Yanlış yaptırım atribüsyonu önemli ticari kayba sebep olur (banka hesabı kapanması, AB tedarikçi reddi).
2. **Coğrafi bağlam** — Ana ortak ülkesinin **komşu ülke yaptırım/coğrafi bağlamı** → tedarik zincirinde "ikincil yaptırım (secondary sanctions)" riski.
3. **Yüksek tutarlı uluslararası enerji ticareti** — milyonluk USD transferleri, USD bazlı petrol/petrokimya — OFAC penceresi geniş açık.
4. **[Halka Açık İştirak] halka açık** — SPK Tebliğ II-15.1 kapsamında "önemli olay" olabilecek yaptırım eşleşmeleri KAP açıklama tetikler.

---

## 6 yaptırım rejimi (sırayla)

### 1. OFAC (ABD Hazine — OFAC Sanctions Lists)

**Listeler:**
- **SDN List (Specially Designated Nationals)** — kara liste, dondurulmuş varlık
- **SSI (Sectoral Sanctions Identifications)** — Rusya sektörel; finansman, enerji, savunma
- **CAPTA** (Correspondent Account or Payable-Through Account Sanctions)
- **NS-PLC** (Non-SDN Palestinian Legislative Council)

**Şirket için kritik alt-liste:**
- **CAATSA Section 232** — Rusya enerji ihracat boru hattı projeleri ([Boru Hattı Projesi] DEĞİL ama Türk Akımı/Mavi Akım komşu hatlar). CAATSA m.232 işlemleri için aday vendor/customer.
- **EO 14024** (Rusya Belirleyici İcra Emri) — finansal işlemler

**Sorgu:** https://sanctionssearch.ofac.treas.gov/ veya `WebFetch`/dedicated screening service. SDN List API'si var.

### 2. AB Konseyi (EU Consolidated Financial Sanctions List)

**Mevzuat:**
- **Council Regulation (EU) 269/2014** — Ukrayna kişi/işletme (Rusya çerçevesi)
- **Council Regulation (EU) 833/2014** — Rusya sektör (önemli: enerji, finansal, ulaşım, savunma)
- **Council Regulation (EC) 267/2012** — İran
- **Council Regulation (EU) 1183/2005** — DRC
- + Belarus, Suriye, Kuzey Kore, Venezuela rejimleri

**TR pazarına etki:** AB tedarikçiniz (örn. AB ekipman üreticisi) AB yaptırım listesindekilere ürün sağlamayı reddeder → Şirket'e "ikincil reddetme" yansıyabilir.

**Sorgu:** https://www.sanctionsmap.eu/ + Consolidated List (XML feed)

### 3. BM Güvenlik Konseyi (UN Consolidated Sanctions List)

**Kapsam:** ISIL/Al-Qaida, Sudan, DRC, Somali, Yemen, Mali, Lübnan, vs.

**Sorgu:** https://www.un.org/securitycouncil/content/un-sc-consolidated-list

### 4. UK OFSI (Office of Financial Sanctions Implementation)

**Brexit sonrası AB'den ayrı rejim.** UK Consolidated Sanctions List — Rusya, Belarus, İran, Kuzey Kore ek listeleri.

**Sorgu:** https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets

### 5. Türkiye yaptırım rejimi

- **7262 sayılı Kanun** (Kitle İmha Silahlarının Yayılmasının Finansmanının Önlenmesine İlişkin Kanun, 2020)
- **MASAK Tebliğleri**
- **BM resepsiyonu** — UNSCR'lerin TR'de uygulanması (CB Kararnamesi ile)

**Sorgu:** https://www.masak.hmb.gov.tr (donan varlık listesi)

### 6. [Yurtdışı Ana Şirket] iç compliance + yurtdışı ana ortak ülke rejimi

- **AzC (Azerbaijan) iç compliance prosedürleri** — ana ortak grup politikası
- **Yurtdışı Ana Şirket ülkesinin Maliye Bakanlığı** finansal kısıt listesi (uygulamada minimum etki)

---

## Tarama akışı — adım adım

### Adım 1: Counterparty kimlik bilgisi topla

Minimum:
- **Tüzel kişi adı (eski dahil)** + ticaret unvanı + lakap
- **Vergi numarası / MERSIS no** (TR) / EIN/CIK (US) / VAT (EU)
- **Adres** (kayıtlı + faaliyet) + ülke
- **Ana faaliyet kodu** (NACE / NAICS)
- **Yönetim Kurulu üyeleri + İmza yetkilileri** isim listesi
- **Pay Sahipleri** — %10+ pay tutan herkes
- **UBO (Ultimate Beneficial Owner)** — son intifa hakkı sahibi gerçek kişi (%25+ kontrol)
- **Bağlı şirket listesi** — counterparty'nin alt iştirakleri
- **Banka bilgileri** — gönderim/alım banka adı, ülke

### Adım 2: Liste eşleşme taraması

Yukarıdaki tüm isim/UBO/bağlı kuruluşu **her 6 rejime karşı** tara. Çift tarama:
- **Otomatik:** Screening service (LexisNexis WorldCompliance, Refinitiv World-Check, Dow Jones Risk Center, Compumark/Clarivate) — büyük şirket standardı
- **Manuel ek:** Yukarıdaki resmi liste URL'leri (false positive teyit için)

**Kesin eşleşme (exact match):** Aynı isim + aynı ülke + aynı yıl-doğum (gerçek kişi için) → **kara liste, durdur**.
**Olası eşleşme (fuzzy):** İsim benzer ama detay farklı → ek dilijans (kimlik teyit, UBO doğrulama).
**Eşleşme yok:** Devam.

### Adım 3: Coğrafi/sektörel risk değerlendirme

Counterparty veya UBO **şu ülkelerden ise** ek dilijans şart:
- Rusya (her durumda + sektörel)
- İran (her durumda)
- Kuzey Kore (kesin yasak)
- Suriye (kesin yasak)
- Belarus (sektörel)
- Venezuela (sektörel)
- Kırım, Donetsk, Lugansk, Zaporojye, Herson (kesin yasak)
- Sudan, Mali, Mianmar, DRC (sektörel)

Bu ülkelerle bağlantı varsa: 
- **Tedarik zinciri kaynak (origin) doğrulama** — ürün Rusya'dan mı geliyor?
- **End-user sertifikası** — alıcı kim, son kullanım nerede?
- **Bankayla pre-clearance** — banka bu işlemi onaylar mı?

### Adım 4: Sektörel kısıt kontrolü (Şirket'e özel)

**Enerji sektörü** AB 833/2014 m.3-5 sınıfında:
- **Rusya menşeili petrol/petrokimya ham madde ithalatı** → AB ham petrol fiyat tavanı + tedarik kısıtları
- **Rusya'ya enerji ekipmanı ihracatı** (rafineri, sondaj, LNG) → yasak/lisanslı
- **AB CBAM (Sınırda Karbon Ayarlama)** — [Halka Açık İştirak] petrokimya ihracatı için Rusya menşeli karbon yoğunluğu kontrolü

### Adım 5: Karar matrisi

| Sonuç | Aksiyon |
|---|---|
| ✅ Tüm rejimlerde temiz, coğrafi düşük risk | Standart akış, sözleşmeye devam |
| 🟡 Fuzzy eşleşme veya orta riskli coğrafi | KYC dosyası tamamla, Counsel onayı, devam |
| 🟠 Tedarik zincirinde Rusya menşeli komponen | CBAM raporlaması + AB tedarikçi pre-clearance, Counsel + Compliance onayı |
| 🔴 Listeden eşleşme veya yasak coğrafi | **DURDUR**, Hukuk Başkanı ([CLCO]) + Compliance + CEO bilgisi, eskalasyon |

### Adım 6: Belgeleme ve saklama

- Tarama raporu **5 yıl** sakla (MASAK + AB rehberleri)
- [Halka Açık İştirak] ilgiliyse — içsel bilgi listesi + KAP açıklama tetikleyici mi (SPK Tebliğ VI-104.1)
- [Yurtdışı Ana Şirket] ile paylaşılır mı (intra-group) — ayrı KVKK aktarım dokümantasyonu

---

## Kırmızı bayrak (red flag) listesi

Counterparty bunlardan birini gösteriyorsa **standart yaptırım kontrolünün ÖTESİNDE** ek dilijans yap:

- **Yeni kurulmuş şirket** (< 6 ay) yüksek tutarlı işlem
- **Off-shore yetki alanı** (BVI, Cayman, Panama, Marshall Islands)
- **Pay yapısı opak** — bearer shares, trust, nominee director
- **Ödeme rotası** karmaşık (3+ banka, farklı para birimleri, hesaplar)
- **UBO açıklamak istemiyor** — KYC reddi
- **Counterparty bildirilen "iş modeli"** ham petrol/petrokimya ticaretiyle uyumsuz
- **Counterparty Rusya'da banka hesabı tutuyor**
- **Liman/tanker rotası** Karadeniz/Hazar/Basra Körfezi'nde olağandışı dolaşım gösteriyor
- **Vendor son 12 ayda 2+ kez bahaneli teslim gecikmesi** + Rusya menşeli komponen iddiası

---

## [Halka Açık İştirak] için ek katman (halka açık)

Eğer counterparty veya yaptırım eşleşmesi **[Halka Açık İştirak]'i etkileyen bir konuysa**:

1. **İçsel bilgi listesi** güncelleme (SPK Tebliğ VI-104.1)
2. **KAP açıklama tetikleyici mi?** (SPK Tebliğ II-15.1 — örn. ana müşteri kaybı, materyal vendor, yaptırım nedeniyle iş kesintisi)
3. **Yatırımcı ilişkileri** brifingi hazır olmalı

---

## Mevzuat MCP entegrasyonu

Bu rehberin yaslandığı TR mevzuatı için MCP sorguları:

```
search_kanun(mevzuat_adi="7262")  → Kitle İmha Silahlarının Yayılmasının Finansmanı K.
search_kurum_yonetmelik(kurum="MASAK")
search_kanun(mevzuat_adi="5549")  → MASAK Suç Gelirlerinin Aklanması K.
search_cbk(query="yaptırım")
```

Yabancı yaptırım rejimleri (OFAC, AB, BM, UK) Mevzuat MCP'de YOK — doğrudan resmi sitelerden veya screening service'ten çek.

---

*Son güncelleme: 13.05.2026 — ArthurLegal Holding commercial-legal "the thing that hurts" referansı*
