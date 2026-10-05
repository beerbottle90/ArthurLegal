# Fikri ve Sınai Haklar – Pratik Profili (Türkiye Overlay)

> Hedef: `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`

---

## Kim olduğumuz

Bkz. `company-profile.md`. Bu eklentiye özel:

**Portföy büyüklüğü** (kamuya açık verilerden tahmin — gerçek sayılar IP koordinatöründen):
- **Marka tescili (TR):** Yüksek sayıda — Şirket, [Halka Açık İştirak], [Rafineri Tesisi] (rafineri), [Enerji Ticareti A], [Telekom A], [Liman İştiraki], [Boru Hattı Projesi], **[Elektrik İştiraki] (yakın geçmişte iştirak portföyüne katılan)** markaları + alt ürün markaları + petrokimya ürün serileri (etilen, propilen, PET vs.). Onlarca aktif marka tahmini. *[Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] markaları portföyden çıkarıldı / çıkarılıyor (devir kapsamında).* [DOLDUR — TÜRKPATENT'ten kesin sayı]
- **Marka (Madrid Protokolü, EUIPO, USPTO):** Ana Şirket markası WIPO Madrid + EUIPO'da uluslararası tescil olası. [DOLDUR]
- **Patent (TR):** Petrokimya proses patentleri olası (polimer üretim, katalizör, vb.). [DOLDUR]
- **Patent (PCT, EPO, USPTO):** Stratejik proseslerde uluslararası başvuru olası. [DOLDUR]
- **Endüstriyel tasarım:** Petrokimya ürün ambalajı, [Şirket] istasyon tasarımı ([Şirket] akaryakıt istasyonu Türkiye'de yaygın değil ama varsa marka kimliği). [DOLDUR]
- **Faydalı model:** [DOLDUR]

**Domain portföyü:** [sirket].com.tr, [halka-acik-istirak].com.tr, [rafineri].com.tr, [boru-hatti].com, [elektrik-istiraki].com (eklenecek), vb. — siber-squatting koruması için global domain monitoring gerekli. *[Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] domainleri devir kapsamında.*

**Vekil:** **[Marka Vekili Firma]** — TR marka + patent + endüstriyel tasarım işlemlerinde birincil vekil.
**Watching service:** [DOLDUR — Clarivate (Compumark) veya Corsearch beklenir; [Marka Vekili Firma] üzerinden de yürütülüyor olabilir]

---

## Türkiye IP mevzuatı

- **6769 Sınai Mülkiyet Kanunu (SMK)** — marka, patent, faydalı model, endüstriyel tasarım, coğrafi işaret
- **5846 Fikir ve Sanat Eserleri Kanunu (FSEK)** — telif
- **5651 İnternet Kanunu** — DMCA muadili "URL kaldırma" rejimi
- **6502 TKHK** — markaya yönelik tüketici aldatma

### Kritik süreler

| İşlem | Süre |
|---|---|
| Marka tescil yayımına itiraz | 2 ay (SMK m. 18) |
| Marka tescil kararına itiraz | 2 ay |
| Patent araştırma raporu | başvurudan 12 ay |
| Patent inceleme talebi | araştırma yayımından 3 ay |
| Marka yenileme | tescil tarihinden 10 yıl + 6 ay grace |
| Patent yıllık ücret | tescil yıldönümü, 6 ay grace |

---

## Sık yapılan işler

### 1. Marka clearance (TÜRKPATENT araması)

- **Resmi araç:** https://www.turkpatent.gov.tr/marka-arama
- **Mukayese sınıfı (Nice):** 1-45 (45 hizmet sınıfı dahil)
- **Yargı testi:** Karıştırılma ihtimali (SMK m. 6) — Yargıtay 11. HD içtihatları
- Sonuç çıktısı: aynı / benzer / farklı + sınıf önerisi + risk değerlendirmesi

### 2. FTO (Freedom to Operate) — Patent

- TÜRKPATENT patent arama (sınırlı; Espacenet daha güçlü)
- TR patent + EPO TR validation + Türkiye'ye uzanan PCT'leri tara
- Açık + reddedilen + iptal edilen patentleri ayrı sınıfla

### 3. İhtarname / Cease-and-desist

- TR pratiği: **noter ihtarnamesi** (Noterlik Kanunu m. 86 vd.) zaman damgalı tebligat
- KEP üzerinden de gönderilebilir; alıcı tüzel kişi ise KEP zorunluluğu (TTK 18/3)
- Tipik: 7-30 gün cevap süresi + sürmemesi halinde mahkemeye başvuru
- İhtiyati tedbir talebi (HMK 389) — pazar dışına çıkarma

### 4. 5651 URL kaldırma — DMCA muadili

- İçerik sahibi → erişim sağlayıcı / yer sağlayıcı uyarı
- 24 saat içinde kaldırma yükümlülüğü
- Süreç: uyarı → kaldırma → itiraz → sulh ceza hâkimliği kararı (gerekirse)
- 6769 SMK m. 7/d — markaya tecavüz internet özelinde

### 5. Açık kaynak uyumu

- Türk yargısında yeterli içtihat yok ama GPL, MIT, Apache lisans hükümleri "tip sözleşme" olarak yorumlanır.
- Risk değerlendirmesi US/AB ağırlıklı yapılır; Türk firma çıktısı bu çerçevede sunulur.

---

## Çıktı standardı

Bkz. `commercial-legal.md`. IP özel:

- Marka clearance çıktısında her benzer markaya: TÜRKPATENT tescil no + sınıf + sahibi + risk renkkodu
- Patent çıktıları: TR + EPO + WIPO numara üçlü gösterimi
- İhtarname taslakları: noter onaylı versiyon + KEP versiyon her ikisi de
- Yenileme alarmları: tarih + grace + ücret + atılacak aksiyon

---

## Eskalasyon

- 🔴 Aktif tecavüz (rakip ürün satışta — [Halka Açık İştirak] ürün taklit, Şirket marka taklit istasyon, [Şehir Gazı Dağıtım A] logo benzerliği vs.), ihtiyati tedbir talebi → Hukuk Başkanı ([CLCO]) + dış IP vekili 24h
- 🟠 İhtarname + ihtilaf, **[Halka Açık İştirak] ürün marka itirazı** (SPK/KAP içerik düşüncesi) → Counsel + dış IP vekili
- 🟡 Standart tescil işlemi, yenileme, klasik clearance → IP koordinatörü + vekil

**Şirket'e özel ek:**
- **[Halka Açık İştirak] ile ilgili IP işlemleri** (yeni ürün markası tescili, lisans verilmesi) — halka açık şirket için **KAP içsel bilgi kontrolü** gerekli
- **Uluslararası enerji projelerinde IP klozu** ([Boru Hattı Projesi], ortak girişimler) — JV anlaşmasındaki IP paylaşımı + lisans
- **Domain monitoring:** Şirket/[Halka Açık İştirak]/[Rafineri Tesisi] markalarına benzer domain kayıtları için aylık tarama

---

## Mevzuat MCP kullanım örüntüleri

- `search_kanun(mevzuat_adi="6769")` — SMK
- `search_kanun(mevzuat_adi="5846")` — FSEK
- `search_kanun(mevzuat_adi="5651")` — İnternet K.
- `search_kurum_yonetmelik(kurum="Türk Patent")` — Yönetmelikler

## Yargı MCP kullanım örüntüleri (IP içtihatı)

- `search_yargitay_decisions(daire="11. Hukuk Dairesi", arananKelime="marka iltibas karıştırılma ihtimali")` — marka davaları
- `search_yargitay_decisions(daire="11. Hukuk Dairesi", arananKelime="patent tecavüz")` — patent davaları
- `search_yargitay_decisions(daire="11. Hukuk Dairesi", arananKelime="haksız rekabet")` — TTK 54 vd. uygulamaları
- `search_danistay_decisions(arananKelime="TÜRKPATENT itiraz iptal")` — idari yargı

Her atıfta `[Yargı MCP — yargitay/danistay — GG.AA.YYYY]` etiketi.
