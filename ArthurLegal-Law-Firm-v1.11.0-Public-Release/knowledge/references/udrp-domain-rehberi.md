# UDRP / Domain Takedown — Sahte Site Müdahale Rehberi

> Müvekkilin markasını taklit eden sahte domain'ler için müdahale prosedürü. `[marka]-sahte.com` benzeri vakalar.

## 3 paralel müdahale kanalı

Sahte domain (örn. `[marka]-sahte.com`) tespit edildiğinde **3 ayrı hukuki rejim** paralel işler:

### 1. Marka tecavüzü (SMK)
- **SMK m. 7/3** — alan adında ticari amaçla marka kullanımı
- **SMK m. 29-30** — tecavüz halleri + dava türleri
- **SMK m. 149-150** — cezai sorumluluk

### 2. Tüketici yanıltma + haksız rekabet
- **TTK m. 54-63** — haksız rekabet
- **6502 TKHK m. 61-62** — yanıltıcı reklam
- **5651 İnternet K. m. 8/A, m. 9** — içerik kaldırma / erişim engelleme

### 3. Dolandırıcılık (cezai)
- **TCK m. 158/1-f** — bilişim sistemi araç edilerek dolandırıcılık (4-10 yıl)
- **TCK m. 243, 245** — bilişim güvenliği, banka kartı kötüye kullanma
- **MASAK 5549** — organize finansal dolandırıcılık

## Hızlı müdahale akışı — saat bazlı

### ⏰ İlk 1 saat
- [ ] **Pazarlama-Satış'tan teyit:** Bayi/distribütör kayıtlarında bu domain sahibi VAR mı? (Cevap genelde "yok" — sahte)
- [ ] **Whois sorgusu:** Registrar, kayıt sahibi (genelde proxy/gizli), kayıt tarihi, hosting → kanıt dosyası
- [ ] **Site arşivi:** Wayback Machine (`https://web.archive.org/save/<URL>`) — bağımsız tanıklık delil
- [ ] **Tam ekran görüntüleri:** Tüm sayfalar (anasayfa, iletişim, ödeme, bayi başvurusu) — Adobe PDF kayıt
- [ ] **Ödeme/iletişim bilgisi tespit:** IBAN, telefon, e-posta — sahtekarın izleri
- [ ] **Şikayet taraması:** şikayetvar.com, sikayetonline, sosyal medya — gerçek mağdur var mı?
- [ ] **İletişim Başkanlığı ([İletişim Başkanı]) ön-bilgi:** Basına çıkmış mı?

### ⏰ İlk 24 saat

#### Domain takedown — paralel iki kanal

**Kanal 1 — Registrar/Hosting abuse şikayeti (en hızlı):**
- **`.com` için:** GoDaddy, Namecheap, vb. registrar'ın `abuse@` adresine şikayet
  - Marka ihlali kanıtı (TÜRKPATENT tescil belgesi)
  - Dolandırıcılık kanıtı (yanıltıcı içerik ekranları)
  - **Süre: 24-72 saat askıya alma** genelde
- **Hosting sağlayıcısı:** İçerik kaldırma için ayrı şikayet
- **CloudFlare** (eğer arkasında):  abuse formu

**Kanal 2 — Hukuki süreç:**
- **5651 m. 9 başvurusu** — Sulh Ceza Hakimliği'ne URL bazlı erişim engelleme
  - Kişilik hakkı + ticari itibar ihlali argümanı
  - **24 saat içinde karar**
  - Hâkim kararı sonrası BTK 4 saatte erişimi engeller
- **5651 m. 8/A (acil prosedür):** Mali tehlike + yaşamsal/güvenlik tehdidi varsa (yüksek hacimli dolandırıcılık)
  - BTK + savcılık → **4 saat** içinde engelleme

#### Cezai şikayet
- **Cumhuriyet Başsavcılığına suç duyurusu** (TCK m. 158/1-f + SMK m. 149)
- Yetki: **dolandırıcılık eyleminin gerçekleştiği yer** veya **[Müvekkil] merkez = İstanbul**
- Birim: **İstanbul Cumhuriyet Başsavcılığı Bilişim Suçları Bürosu**
- Ekleri: whois, ekran görüntüleri, bayi olmadığı teyit yazısı, marka tescil belgesi, varsa mağdur ifadeleri

#### Resmi açıklama
- [Müvekkil] resmi web + sosyal medya: "Bu site [Müvekkil] ile bağlantılı değildir. Resmi bayilerimiz [müvekkil-web-sitesi]'den teyit edilebilir. Ödeme YAPMAYIN."
- İletişim Başkanlığı ([İletişim Başkanı]) ile koordineli — kategorik açık mesaj

### ⏰ İlk 1 hafta

#### UDRP (Uniform Domain Name Dispute Resolution Policy) — kalıcı çözüm
- **`.com / .net / .org` için:** ICANN UDRP rejimi
- **WIPO Arbitration and Mediation Center** (en yaygın) veya FORUM, ADNDRC
- Süre: **2-3 ay** içinde transfer/iptal
- Maliyet: ~**1.500 USD** (tek hakem; üç hakem ~4.000 USD)
- Dış marka vekili sunar (Truva Patent veya UDRP uzmanı)

**UDRP testi (3 koşul):**
1. Domain marka ile aynı veya karıştırılır
2. Domain sahibinin meşru menfaati yok
3. Domain kötü niyetle kayıt edilmiş veya kullanılıyor

**Sahte domain örneği:** Hepsi sağlanır — kazanma olasılığı %90+

#### `.com.tr` için
- TRABIS (TR Alan Adı Yönetimi) süreci ayrı
- Uyuşmazlık çözümü mekanizması yerel
- Bilirkişi heyeti — süre ~1-2 ay

### ⏰ Devamı

#### Alternatif mekanizmalar
- **Google brand abuse şikayeti** (sahte site Google Ads kullanıyorsa) — saatler içinde reklam kapanır
- **Sosyal medya platformları** (LinkedIn, Instagram, X) — sahte [Müvekkil] profilleri kategorik takedown
- **Apple App Store / Google Play** (sahte [Müvekkil] app var ise) — store policy ihlali şikayeti

#### Hukuki sonuç davası (SMK m. 30 tazminat)
- Somut zarar varsa **Asliye Hukuk** veya **Fikri ve Sınai Haklar Mahkemesi**
- Cost-benefit analizi: dava maliyeti vs. tazminat olasılığı
- Sahtekarın kim olduğu çoğu zaman belirsiz — tazminat tahsil edilemez
- **Cezai yol genelde daha caydırıcı** (TCK 158/1-f hapis cezası)

#### KVKK ihbar
- Sahte site [Müvekkil] adıyla kişisel veri topluyor (ad, telefon, ödeme) → **KVKK Kurulu'na re'sen inceleme talebi**
- 6698 m. 5 hukuka aykırı veri işleme
- **[DPO / Veri Koruma Sorumlusu] (DPO)** üzerinden

#### Reklam Kurulu şikayet
- **TKHK m. 77/12 — Reklam Kurulu** — yanıltıcı reklam idari para cezası + içerik durdurma
- Hızlı ek caydırıcılık

## Pattern attack (toplu)

Tek bir sahte domain'le yetinmemek için:

- **Domain taraması:** [[marka]-*] pattern'larında
- Araç: DomainTools, BrandShield, MarkMonitor
- **Toplu takedown** sahte ailesi varsa

### Defensive registration
- Anahtar varyantlar [Müvekkil] adına alın (defensive):
  - `[[marka]-sahte.com.tr]`, `.com`, `.net`, `.org`, `.eu`
  - Önemli pazarlar (Azerbaycan: `.az`, Türkiye: `.com.tr`)
- Yıllık bütçe — küçük ama önemli koruma

## [Müvekkil] koordinasyon

| Aksiyon | Onay |
|---|---|
| Registrar abuse + 5651 m. 9 başvurusu | Senior Legal Counsel [kuran kişi — company-profile: Kullanıcı rolü] |
| Suç duyurusu hazırlık + savcılığa sunum | Counsel + Direktör imza [company-profile: Doğrudan amir] |
| Resmi açıklama içeriği | Counsel + [İletişim Başkanı] (İletişim) + [Hukuk Direktörü] onay |
| UDRP başvurusu (dış avukatla) | [Hukuk Direktörü] + [CLCO] (CLCO) bilgi (tutar < 50K TL) |
| SMK m. 30 tazminat dava açma | [CLCO] onay (litigation eskalasyon matriksi) |
| KVKK Kurulu ihbarı | DPO [DPO / Veri Koruma Sorumlusu] + [Uyum Direktörü] (Compliance) |
| MASAK ihbar (büyük çaplı) | Compliance + CFO koordinasyon |

## Bağlantılı

- [SMK rehberi](smk-rehberi.md)
- [TÜRKPATENT rehberi](turkpatent-rehberi.md)
- ip-legal plugin overlay
- litigation-legal plugin (dava boyutu)
