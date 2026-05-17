# Şirket / Kullanıcı Profili (Ortak)

> Bu dosya tüm eklentilerin okuduğu **ortak profil dosyasıdır**. Şirket / kullanıcı seviyesindeki temel bilgiler buraya yazılır; pratiğe özel olanlar her eklentinin kendi profilinde (`tr-overlay/profiles/*.md`).
>
> **Bu dosya bir şablondur.** Köşeli parantezli alanları (`[Şirket]`, `[CLCO]`, `[DOLDUR]` vb.) kendi kurumunuza göre doldurun.
>
> **Kaynak etiketleri (önerilen):**
> - `[web]` — Kurumun resmi web sitesi
> - `[FR-yyyy]` — Yıllık faaliyet raporu
> - `[basın]` — Yaygın yayın organlarındaki resmi açıklamalardan
> - `[DOLDUR]` — Kullanıcının doldurması gereken alan
> - `[doğrulayın]` — Kamuya açık ama tarihi/sürümü teyit edilmesi gereken bilgi

---

## Örnek senaryo

Bu şablon, **ArthurLegal Holding A.Ş.** adlı varsayımsal bir kurumsal holding örneği üzerinden örneklendirilmiştir:

- Türkiye'de faaliyet gösteren çok-iş-birimli endüstriyel/enerji holding
- Birden fazla bağlı şirket (en az biri BIST'e kayıtlı)
- [DOLDUR — toplam çalışan sayısı] (in-house hukuk takımı: 20+ kişi)
- Yurtdışı ana ortak yapısı (yaptırım/transfer pricing/regulatory cross-border boyutu)
- Üretim sahası (İSG + ÇED + EPDK + Seveso yükümlülükleri)

Bu örnek, plugin'lerin pratik problem alanlarını (yaptırım, KAP, transfer pricing, İSG, ÇED, EPDK, ISTAC) doldurmaya elverişli bir referans noktası sağlar. Kendi kurumunuz için aşağıdaki tüm alanları kendi durumunuza göre düzenleyin.

---

## Kim olduğumuz

**Şirket adı:** `[Şirket Adı] A.Ş.` (örnek: ArthurLegal Holding A.Ş.)
**Şirket türü (entity type):** `[Anonim Şirket / Limited Şirket / Holding A.Ş.]`
**Endüstri:** `[DOLDUR — örn. entegre enerji, finans, perakende, üretim, hizmet, vd.]`
**Grubun konumu:** `[DOLDUR — sektör içindeki yeri, yatırım hacmi vb.]`
**Ana ortak / hissedarlık yapısı:** `[DOLDUR — örn. yerli aile şirketi / yurtdışı ana ortak / halka açık / private equity]`
**Çalışan sayısı:** `[DOLDUR]`
- Merkez ofis: `[DOLDUR]`
- Üretim/saha: `[DOLDUR]`
**Faaliyet gösterilen ülkeler:** `[DOLDUR — birincil + yurtdışı]`
**Borsada işlem görüyor mu:** `[DOLDUR — Evet/Hayır; halka açık bağlı şirket varsa kod ve dayanak]`

**Pratik ortamı (Practice setting):** In-house (şirket içi hukuk müşavirliği)

---

## Kurumsal yapı — iş birimleri

> İş birimi yapınızı ve önemli bağlı şirketleri burada listeleyin. Aşağıda 3-iş-birimli kurumsal holding için örnek şablon:

**1. `[İş Birimi 1 — örn. Üretim & Operasyon]`**
- `[Bağlı Şirket 1 — varsa halka açık olduğunu belirtin]`
- `[Bağlı Şirket 2]`
- `[Üretim Sahası — yer + kapasite]`

**2. `[İş Birimi 2 — örn. Enerji / Ticaret / Hizmet]`**
- `[Bağlı Şirket 3]`
- `[Bağlı Şirket 4]`

**3. `[İş Birimi 3 — örn. Portföy Yönetimi / Yatırım / Destek Hizmetleri]`**
- `[Bağlı Şirket 5]`
- `[İştirak / proje ortaklığı]`

---

## Birincil yargı çevresi (jurisdiction footprint)

- **Birincil:** Türkiye Cumhuriyeti
- **Yurtdışı bağlantı:** `[DOLDUR — ana ortak hukuku / sınır-ötesi operasyon / AB/BIT/FTA kapsamı]`
- **Tabi olunan başlıca mevzuat:**
  - 6098 sayılı Türk Borçlar Kanunu (TBK)
  - 6102 sayılı Türk Ticaret Kanunu (TTK)
  - 4857 sayılı İş Kanunu + 5510 SGK Kanunu + 6356 Sendika ve TİS + 6331 İSG
  - 6698 sayılı KVKK + EU GDPR (varsa AB iletişimi)
  - 6362 sayılı Sermaye Piyasası Kanunu **(halka açık bağlı şirket varsa)**
  - 4054 sayılı Rekabetin Korunması Hakkında Kanun
  - 6769 sayılı Sınai Mülkiyet Kanunu (SMK) + 5846 FSEK + 5651 İnternet K.
  - 2872 sayılı Çevre Kanunu + ÇED Yönetmeliği + (varsa) Büyük Endüstriyel Kaza Yön.
  - **Sektör mevzuatı:** `[DOLDUR — örn. EPDK enerji piyasası kanunları, BDDK bankacılık, SPK ek tebliğler, vd.]`
  - **Uluslararası antlaşmalar:** `[DOLDUR — varsa]`

---

## Risk duruşu (risk posture)

**Genel:** `[Muhafazakar / Dengeli / Risk-alma eğiliminde]`

> Örnek: "Dengeli — risk-getiri analizli kurumsal pratik. Kanunen zıtlaşmayan ama gri alanda kalan adımlara koşullu izin verilebilir; yaptırım / çevre / KAP / KVKK kritik alanlarda muhafazakara yaklaşır."

**Kritik kırmızı çizgiler (örnek liste — kendinize uyarlayın):**
- **OFAC / AB / BM yaptırım listeleri** — özellikle ana ortak yapısı yurtdışı veya sınır-ötesi işlem hacmi yüksekse
- **KAP açıklama yükümlülüğü** — halka açık bağlı şirket varsa SPK Tebliğ II-15.1
- **Sektör regülatörü** (EPDK / BDDK / SPK / RTÜK / KİK) lisans/yetki hükümleri
- **Çevre mevzuatı / iş güvenliği** — özellikle üretim/saha operasyonu varsa
- **KVKK / GDPR ihlali** — büyük çalışan + müşteri veri tabanı
- **Rekabet Kurumu** — dikey/yatay entegrasyon riski
- **Kara para aklama / MASAK** — yüksek tutarlı uluslararası işlem

---

## Anahtar kişiler ve onay zinciri

> Bu bölümde **gerçek isim YOKTUR** — rol bazlı yer-tutucular kullanılmıştır. Kendi kurumunuzdaki gerçek isimleri yerleştirin.

### Üst Yönetim

| Rol | İsim | Atanma | Onay yetkisi |
|---|---|---|---|
| CEO | `[DOLDUR]` | `[DOLDUR]` | `[DOLDUR]` |
| CFO | `[DOLDUR]` | `[DOLDUR]` | `[DOLDUR]` |
| COO | `[DOLDUR]` | `[DOLDUR]` | `[DOLDUR]` |
| CLCO (Chief Legal, Compliance & Corporate Governance Officer) | `[CLCO — DOLDUR]` | `[DOLDUR]` | `[DOLDUR — tipik > 50M ₺]` |

### Hukuk, Uyum ve Kurumsal Yönetim Departmanı (örnek departman yapı)

> Bu yapı, orta-büyük ölçek bir Türk holding için tipiktir. Kendi ekip yapınıza göre uyarlayın.

**Departman Başkanı:**
- `[CLCO]` — Chief Legal, Compliance & Corporate Governance Officer (CEO'ya raporlar)

**Ekip 1 — Hukuk (Corporate / Commercial):**
- `[Hukuk Direktörü A]` — Legal Corporate Director
  - `[Kullanıcı]` — Senior Counsel (örnek kullanıcı pozisyonu)
  - `[Senior Counsel 1]`
  - `[Senior Counsel 2]`
  - `[Counsel 1]`
  - `[Counsel 2]`

**Ekip 2 — Hukuk (Dava / Regulatory):**
- `[Hukuk Direktörü B]` — Legal Corporate Director
  - `[Senior Counsel 3]`
  - `[Senior Counsel 4]`
  - `[Counsel 3]`
  - `[Counsel 4]`
  - `[Junior Counsel 1]`

**Ekip 3 — Kurumsal Yönetim / Koordinasyon:**
- `[Hukuk Koordinatörü]` — Legal Coordinator
  - `[Counsel 5]`
  - `[Counsel 6]`
  - `[Junior Counsel 2]`

**Ekip 4 — Uyum (Compliance):**
- `[Uyum Direktörü]` — Compliance Corporate Director
  - `[Reg. Compliance Manager]`
  - `[Compliance Counsel 1]`
  - `[DPO]` — Veri Sorumlusu (KVKK)
  - `[Compliance Counsel 2]`

### Onay zinciri (örnek eşik şablonu)

| Tutar / işlem türü | Onay seviyesi |
|---|---|
| ≤ 5M ₺ tedarik / hizmet sözleşmesi | Manager / Senior Counsel |
| 5M – 10M ₺ | Hukuk Direktörü |
| 10M – 50M ₺ | CLCO |
| > 50M ₺ veya stratejik | CFO + CEO + (varsa) YK |
| Sulh teklifi (dava) | Tutar bazlı kademe — bkz. `tr-overlay/profiles/litigation-legal.md` |
| KAP açıklaması (varsa halka açık) | CLCO + CFO (SPK Tebliğ II-15.1) |
| Yaptırım taraması — RED bulgu | CLCO + Uyum Direktörü |

---

## Operasyonel platformlar (örnek)

| Alan | Platform | Sahibi |
|---|---|---|
| CLM (sözleşme yönetimi) | `[DOLDUR — Ironclad / iManage / yok]` | `[DOLDUR — Hukuk / Satınalma]` |
| İK (HRIS) | `[DOLDUR — SAP SuccessFactors / Workday / vd.]` | İK |
| VDR (M&A) | `[DOLDUR — Datasite / Intralinks / vd.]` | Hukuk (M&A) |
| E-imza | `[DOLDUR — KEP / DocuSign / e-mza]` | Hukuk |
| Dava yönetim | `[DOLDUR — UYAP entegrasyonu + dahili]` | Dava ekibi |
| Reg watch | `[DOLDUR — RG abone + sektör kurum siteleri]` | Regulatory |

---

## Toplu sözleşme ve özel rejimler

- **TİS / Sendika:** `[DOLDUR — varsa sendika adı, kapsam]`
- **Yabancı çalışan:** `[DOLDUR — sayı, ana milliyet]`
- **KVKK yapısı:** `[DOLDUR — tek merkezi DPO / ayrı VERBİS sicilleri, vb.]`
- **Yaptırım taraması kapsamı:** `[DOLDUR — örn. OFAC + AB + BM + UK OFSI + ulusal listeler]`
- **IP vekili:** `[DOLDUR — marka vekili firma]`
- **Vergi danışmanı / YMM:** `[DOLDUR]`
- **Dış vekil paneli:** Bkz. `tr-overlay/profiles/litigation-legal.md`

---

## "Yakıcı" stres alanları (örnek liste)

> Her kurumda 1-3 "the one thing that hurts" alanı olur. Bunları burada flag'leyin — plugin'ler bu alanlarda ekstra dikkat gösterecek.

- `[DOLDUR — örn. yaptırım taraması — yurtdışı ana ortak yapısı nedeniyle]`
- `[DOLDUR — örn. İSG kazaları — üretim sahası yüksek risk]`
- `[DOLDUR — örn. transfer pricing — intra-group sınır-ötesi işlemler]`
- `[DOLDUR — örn. KAP açıklama — halka açık iştirak]`

---

## Plugin-bazlı profil özet referansları

Her plugin'in derin profili `tr-overlay/profiles/<plugin>.md` altındadır:

- `commercial-legal.md` — NDA triage playbook, sözleşme türleri, eskalasyon
- `corporate-legal.md` — YK kararları, M&A geçmişi, kurumsal yapı
- `employment-legal.md` — TİS, fesih protokolü, iç soruşturma
- `privacy-legal.md` — VERBİS, DSAR akışı, DPO koordinasyonu
- `regulatory-legal.md` — Takip kaynakları, sektör kurumları
- `ip-legal.md` — Marka portföyü, IP vekili, UDRP geçmişi
- `litigation-legal.md` — Dava portföyü, dış vekil paneli, eskalasyon matriksi
- `tax-legal.md` — Mali İşler koordinasyon modeli, vergi davası geçmişi
- `administrative-legal.md` — İdari yargı aktif dava listesi, EPDK proaktif dialog modeli

---

*Bu şablonun ilk doldurulması için `/<plugin>:cold-start-interview` komutunu kullanın — her plugin için ayrı.*
*Author: Claude (Anthropic, Opus 4.7) — Designer: Ertuğ Demir.*