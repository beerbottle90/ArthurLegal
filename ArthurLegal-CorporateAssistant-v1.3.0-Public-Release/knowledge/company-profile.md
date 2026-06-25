# Şirket / Kullanıcı Profili — Kurulum Şablonu

> Bu dosya tüm eklentiler tarafından okunur. Şirket ve kullanıcı seviyesindeki temel bilgiler buraya yazılır; pratiğe özel bilgiler her eklentinin kendi skill dosyasındadır.
>
> **Bu dosya bir şablondur.** `[DOLDUR]` etiketli tüm alanları şirketinize özgü gerçek bilgilerle doldurun.
> `/<plugin>:cold-start-interview` komutuyla asistan bu bilgileri sizden adım adım toplayabilir.

---

## Kim olduğumuz

**Şirket adı:** [DOLDUR — Tam ticaret unvanı, örn. "XYZ Enerji A.Ş."]
**Şirket türü (entity type):** [DOLDUR — A.Ş. / Ltd. Şti. / Şube / vs.]
**Endüstri / Sektör:** [DOLDUR — örn. enerji, finans, teknoloji, üretim, perakende]
**Grubun konumu:** [DOLDUR — Türkiye'deki konumu, grup içindeki yeri]
**Ana ortak / Hissedar yapısı:** [DOLDUR — varsa ana ortak adı ve ülkesi]
**Çalışan sayısı:** [DOLDUR — toplam; opsiyonel: lokasyona göre dağılım]
**Faaliyet gösterilen ülkeler:** [DOLDUR — birincil ve ikincil yargı çevreleri]
**Borsada işlem görüyor mu:** [DOLDUR — Evet/Hayır; evet ise BIST kodu ve halka açık iştiraklerin listesi]

**Pratik ortamı (Practice setting):** [DOLDUR — In-house / Law firm / Karma]

---

## Kurumsal yapı

> Bu bölümü şirketinizin iş birimleri, bağlı ortaklıklar ve iştiraklerine göre doldurun.

**İş Birimi 1:** [DOLDUR — ad ve kısa açıklama]
- [DOLDUR — bağlı iştirakleri, tesisler, ürün/hizmetler]

**İş Birimi 2:** [DOLDUR]
- [DOLDUR]

**İş Birimi 3 (varsa):** [DOLDUR]
- [DOLDUR]

---

## Birincil yargı çevresi (jurisdiction footprint)

- **Birincil:** [DOLDUR — örn. Türkiye Cumhuriyeti]
- **İkincil:** [DOLDUR — ana ortak ülkesi, AB, vs.]
- **Tabi olunan başlıca mevzuat:**
  - [DOLDUR — sektöre göre: TBK, TTK, İş K., KVKK, EPDK, SPK, vs.]
  - [DOLDUR — sektöre özgü düzenleyici mevzuat]

---

## Risk duruşu (risk posture)

**Genel:** [DOLDUR — örn. muhafazakâr / dengeli / büyüme odaklı]

**Kritik kırmızı çizgiler:**
- [DOLDUR — sektöre göre: yaptırım uyumu, KAP açıklama, sektör regülatörü, vb.]
- [DOLDUR]
- [DOLDUR]

---

## Anahtar kişiler ve onay zinciri

> Üst yönetim ve hukuk ekibi bilgilerini buraya girin. Gerçek isimleri yerel kullanım için doldurun; bu dosya public repoda ŞABLON olarak kalır.

### Üst Yönetim

| Rol | İsim | Onay yetkisi |
|---|---|---|
| **CEO / Genel Müdür** | [DOLDUR] | [DOLDUR] |
| **CFO / Mali İşler Başkanı** | [DOLDUR] | [DOLDUR] |
| **CLO / Hukuk Başkanı (CLCO)** | [DOLDUR] | [DOLDUR] |
| **[Diğer C-suite]** | [DOLDUR] | [DOLDUR] |

### Legal & Compliance Departmanı

| Pozisyon | İsim | Sorumluluk alanı |
|---|---|---|
| **Hukuk Direktörü / GC** | [DOLDUR] | [DOLDUR] |
| **Uyum Direktörü** | [DOLDUR] | [DOLDUR] |
| **KVKK Sorumlusu / DPO** | [DOLDUR] | KVKK, GDPR |
| **Kıdemli Hukuk Müşaviri 1** | [DOLDUR] | [DOLDUR] |
| **Kıdemli Hukuk Müşaviri 2** | [DOLDUR] | [DOLDUR] |
| **[Diğer pozisyonlar]** | [DOLDUR] | [DOLDUR] |

**Onay matriksi (tutara göre kademeli):**
- Counsel düzeyi: [DOLDUR — örn. ≤5M TL]
- Direktör düzeyi: [DOLDUR — örn. ≤20M TL]
- CLO / GC: [DOLDUR — örn. ≤50M TL]
- CEO: [DOLDUR — örn. >50M TL]

---

## Kullanıcı rolü

> Bu bölüm `/<plugin>:cold-start-interview` skill'i ile her kullanıcı için ayrı ayrı doldurulur.
> Alanlar `[DOLDUR]` olduğu sürece asistan kimin kullandığını bilemez.

**Bu asistanı kullanan kişi:** [DOLDUR — ad soyad]
**Pozisyon / Ekip:** [DOLDUR — örn. Kıdemli Hukuk Müşaviri, Ticari Hukuk]
**Rol tipi:** [DOLDUR — Avukat (baroya kayıtlı) / Stajyer / Legal Analyst / vs.]
**Risk duruşu:** [DOLDUR — bireysel tercih: muhafazakâr / dengeli / girişimci]
**Doğrudan amir:** [DOLDUR — hangi Direktör / GC]
**Öncelikli pratik alanlar:** [DOLDUR — hangi plugin'leri en çok kullanacaksınız]

---

## Çıktı dili ve tonu

- **Birincil dil:** [DOLDUR — örn. Türkçe]
- **İkincil dil:** [DOLDUR — örn. İngilizce (yabancı counterparty ile)]
- **Ton:** [DOLDUR — örn. profesyonel ve doğrudan; gereksiz formaliteden uzak]
- **Tarih formatı:** [DOLDUR — örn. GG.AA.YYYY]
- **Para birimi:** [DOLDUR — örn. TL; uluslararası işlemler için USD/EUR]

---

## Privilege & gizlilik notları (Türk hukuku özellikleri)

> US "attorney work product" doktrini Türkiye'de YOKTUR. İn-house hukuk müşavirleri için:

- **Avukat–müvekkil gizliliği:** 1136 sayılı Avukatlık Kanunu m. 36 kapsamında. İn-house counsel bu korumadan **sınırlı** yararlanır; Rekabet Kurumu in-house yazışmaları için AB Akzo-Nobel paraleli geçerlidir.
- **TBK m. 6, TTK m. 18 — ticari sır** — şirketin hassas ticari bilgilerinin korunması.
- **KVKK m. 28 — yargı süreci istisnası** — kurul soruşturmalarında savunma hakkı çerçevesinde belgeler açılabilir.

**Önerilen üst başlık (iç memorandumlar için):**

```
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU
[ŞİRKET ADI]
Bu belge yalnızca hukuk müşavirliği değerlendirmesi içindir.
```

---

## Mevzuat takip kanalları

- **Resmi Gazete:** https://www.resmigazete.gov.tr/ (günlük 09:30)
- **TR Legal MCP:** Birleşik yargi-mcp-pro connector — kanun/mevzuat + yargı/içtihat araçları
- **Sektör düzenleyicileri:** [DOLDUR — şirketinize göre: EPDK, SPK, BDDK, Rekabet Kurumu, KVKK Kurulu, vs.]

---

## Yaptırım uyumu

> Uluslararası iş yapan şirketler için bu bölümü doldurun.

- **OFAC (ABD):** [DOLDUR — evet/hayır; yüksek riskli işlemlerde kontrol politikası]
- **AB Yaptırım Rejimi:** [DOLDUR — evet/hayır]
- **BM Güvenlik Konseyi:** [DOLDUR]
- **TR yaptırım rejimi (7262 sayılı K.):** [DOLDUR]

---

## Litigation profili

**Litigation modeli:** [DOLDUR — dış vekil ağırlıklı / hibrit / in-house]
**Aktif dava hacmi:** [DOLDUR — yaklaşık sayı ve ağırlıklı türler]
**Birincil yargı yerleri:** [DOLDUR — İstanbul / Ankara / yerel mahkemeler / tahkim]
**Dış vekil paneli:** [DOLDUR — pratik alanlara göre tercih edilen büro/lar]
**Case management yazılımı:** [DOLDUR — varsa]

---

## Tax profili

**Tax pratik modeli:** [DOLDUR — Mali İşler ana / Hukuk-Mali İşler hibrit]
**Birincil yakıcı vergi alanları:** [DOLDUR — KDV, ÖTV, kurumlar vergisi, TP, vb.]
**Dış vergi danışmanı:** [DOLDUR — varsa]

---

## Bilinen risk olayları / aktif konular (snapshot)

| Tarih | Konu | Durum | Sahibi |
|---|---|---|---|
| [DOLDUR] | | | |

*Bu tablo cold-start ile veya manuel güncellenir.*

---

*Bu şablon ArthurLegal Corporate Assistant v1.2.0 ile birlikte dağıtılmaktadır.*
*Gerçek şirket verileri bu repo'da saklanmaz — yerel olarak doldurun ve güvende tutun.*
