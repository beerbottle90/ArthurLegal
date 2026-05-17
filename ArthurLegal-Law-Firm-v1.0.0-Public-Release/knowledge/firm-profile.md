# Hukuk Bürosu Profili (Ortak)

> Bu dosya tüm eklentilerin okuduğu **ortak büro profil dosyasıdır**. Büro / kullanıcı / müvekkil portföyü seviyesindeki temel bilgiler buraya yazılır; pratiğe özel olanlar her eklentinin kendi profilinde (`tr-overlay/profiles/*.md`).
>
> **Bu dosya bir şablondur.** Köşeli parantezli alanları (`[Büro]`, `[Yönetici Ortak]`, `[Kıdemli Ortak A]`, `[DOLDUR]` vb.) kendi büronuza göre doldurun.
>
> ⚠️ **MESLEKİ SIR UYARISI:** Bu dosyaya gerçek müvekkil isimleri/dosya bilgileri yazmadan önce iki kez düşünün — yedeksiz paylaşılırsa **Avukatlık K. m. 36** ihlali doğabilir. Müvekkil verisi için **matter klasörleri** (`matters/<matter-id>/`) ayrı tutulur; bu dosya sadece **agregat sektör/yargı çevresi/iş hacmi** bilgisini taşır.
>
> **Kaynak etiketleri (önerilen):**
> - `[web]` — Büronun resmi web sitesi (varsa)
> - `[baro]` — Baro levha kaydından
> - `[DOLDUR]` — Kullanıcının doldurması gereken alan
> - `[doğrulayın]` — Tarihi/sürümü teyit edilmesi gereken bilgi

---

## Örnek senaryo

Bu şablon, **ArthurLegal Hukuk Bürosu** adlı varsayımsal bir orta ölçekli hukuk bürosu üzerinden örneklendirilmiştir:

- **0-30 çalışan bandında** (varsayımsal ~18-22 kişi)
- **Dava + danışmanlık dengeli** çalışan, **karma müvekkil portföyü** (KOBİ + bireysel + birkaç mid-cap kurumsal)
- **İstanbul merkez + Ankara irtibat** (Danıştay/idari davalar için)
- **Yönetici Ortak + 3 Kıdemli Ortak** modeli; bağlı avukat + stajyer + sekretarya
- 9 pratik alan: 4 dava (genel/idari/vergi/ceza) + 4 danışmanlık (ticari/kurumsal/iş/IP) + 1 büro işletim

Bu örnek, plugin'lerin pratik problem alanlarını (conflict check, AAÜT, CMK görevli, KEP, vekalet, baro koordinasyonu) doldurmaya elverişli bir referans noktası sağlar. Kendi büronuz için aşağıdaki tüm alanları kendi durumunuza göre düzenleyin.

---

## Kim olduğumuz — büro

**Büro adı:** `[Büro Adı] Hukuk Bürosu` (örnek: ArthurLegal Hukuk Bürosu)
**Hukuki yapı (entity type):** `[Avukatlık Ortaklığı (Av. K. m. 44/B) / Hibrit (yönetici ortak + bağlı avukatlar) / Bireysel + ortaklık] `
**Avukatlık Ortaklığı sicil no:** `[DOLDUR — varsa, TBB sicili]`
**Vergi no:** `[DOLDUR]`
**Kuruluş yılı:** `[DOLDUR]`
**Web sitesi:** `[DOLDUR — varsa]` `[web]`

**Pratik ayarı (Practice setting):** Hukuk bürosu — **danışman** (advisor) tarafı

---

## Ofis ve coğrafi yapı

**Merkez ofis:** `[DOLDUR — İl + İlçe + Adres]`
- Örnek: İstanbul / [İlçe] / [Adres]
**İrtibat ofisi 1:** `[DOLDUR — Ankara (Danıştay için)]` (varsa)
**İrtibat ofisi 2:** `[DOLDUR]` (varsa)
**Çalışma dilleri:** Türkçe (ana), İngilizce (sözleşme/iletişim), `[DOLDUR — diğer]`

**Müvekkil ziyareti rejimi:** `[DOLDUR — yalnız ofis / saha ziyareti mümkün / hibrit]`

---

## Kadro ve organizasyon yapısı

> Bu bölüm **rol-bazlı yer-tutucularla** yapılmıştır. Gerçek isimleri kendi büronuzdan yerleştirin.

### Ortaklar

| Rol | İsim | Baro/Sicil | Uzmanlık | Sorumlu olduğu plugin'ler |
|---|---|---|---|---|
| Yönetici Ortak (Managing Partner) | `[Yönetici Ortak]` | `[İstanbul Barosu — sicil no]` | `[DOLDUR — örn. ticari+kurumsal]` | firm-operations + commercial-advisory |
| Kıdemli Ortak A | `[Kıdemli Ortak A]` | `[DOLDUR]` | `[DOLDUR — örn. dava]` | dispute-litigation + employment-advisory |
| Kıdemli Ortak B | `[Kıdemli Ortak B]` | `[DOLDUR]` | `[DOLDUR — örn. idari+vergi]` | administrative-litigation + tax-litigation |
| Kıdemli Ortak C | `[Kıdemli Ortak C]` | `[DOLDUR — Ankara Barosu (irtibat ofis)]` | `[DOLDUR — örn. ceza+IP]` | criminal-defense + ip-advisory |

### Bağlı avukat kadrosu

| Sayı | Rol | Tipik seniorluk | Atandığı alanlar |
|---|---|---|---|
| `[DOLDUR — örn. 6-8]` | Bağlı Avukat (Associate) | 2-7 yıl | Birden fazla, rotasyonel |
| `[DOLDUR — örn. 3-4]` | Stajyer Avukat | Staj 1.+2. yıl | Şarjör — birden fazla matter |
| `[DOLDUR — örn. 2-3]` | Hukuk Asistanı | n/a | Belge yönetimi, takvim, UYAP işlemleri |
| `[DOLDUR — örn. 1]` | Sekretarya / Office Manager | n/a | Müvekkil giriş, telefon, randevu, fatura |

**Toplam kadro:** `[DOLDUR — 0-30 bandı]`

### Baro kayıt durumu

| Baro | Üye sayısı | Asıl/bağlı kayıt |
|---|---|---|
| İstanbul Barosu | `[DOLDUR]` | Ortakların çoğu asıl |
| Ankara Barosu | `[DOLDUR — 1-2]` | İrtibat ofisi ortağı asıl |
| `[Diğer Baro]` | `[DOLDUR]` | `[DOLDUR — bağlı]` |

> **Levha değişikliği** (asıl → bağlı veya tersi) — yıl içinde yapılırsa **`/firm-operations:baro-islem`** ile takip edilir; harç + sicil dosyası taşıma + yeni levha basımı kaleminden geçer.

---

## Müvekkil portföyü — agregat

> ⚠️ **Gerçek müvekkil isimleri burada YOK.** Bu bölüm sadece sektör/büyüklük/coğrafya dağılımı için. Müvekkil-spesifik bilgi `matters/<matter-id>/` altındadır.

### Aktif müvekkil sayısı

- **Toplam aktif müvekkil:** `[DOLDUR — örn. 80-120]`
- **Sürekli danışmanlık (retainer) müvekkili:** `[DOLDUR — örn. 8-12 müvekkil]`
- **Tek-iş (matter-bazlı) müvekkil:** `[DOLDUR — örn. 60-100]`
- **Tasfiye / arşiv müvekkili:** `[DOLDUR — örn. 200+]`

### Müvekkil tipi dağılımı

| Tip | % | Tipik plugin'ler |
|---|---|---|
| Bireysel (gerçek kişi) | `[DOLDUR — örn. %25]` | dispute / criminal / employment / aile (varsa) |
| KOBİ (tüzel kişi, < 250 çalışan) | `[DOLDUR — örn. %50]` | commercial-advisory + employment-advisory + corporate-advisory |
| Mid-cap kurumsal | `[DOLDUR — örn. %20]` | commercial + corporate + dispute (büyük) + administrative + tax |
| Yabancı / yurtdışı bağlantı | `[DOLDUR — örn. %5]` | commercial (uluslararası) + ip (Madrid) + sanctions check kritik |

### Sektör dağılımı (yaklaşık)

| Sektör | % | Not |
|---|---|---|
| `[Sektör 1 — örn. inşaat / gayrimenkul]` | `[%X]` | `[DOLDUR — alan notu]` |
| `[Sektör 2 — örn. perakende / e-ticaret]` | `[%X]` | |
| `[Sektör 3 — örn. üretim]` | `[%X]` | |
| `[Sektör 4 — örn. hizmet / danışmanlık]` | `[%X]` | |
| `[Sektör 5 — örn. teknoloji / yazılım]` | `[%X]` | |
| Bireysel (sektör-yok) | `[%X]` | |

### Coğrafi dağılım

- **İstanbul müvekkilleri:** `[%X]`
- **Anadolu yakası (Bursa/İzmit/Adapazarı):** `[%X]`
- **Ankara:** `[%X]`
- **Diğer iller:** `[%X]`
- **Yurtdışı (yabancı müvekkil):** `[%X]`

---

## Pratik alanları — hangi alanda ne kadar iş?

> Bu agregat, plugin önceliklerini belirler.

| Plugin | Aylık matter hacmi | Aktif dava/dosya | Aylık yeni intake |
|---|---|---|---|
| `dispute-litigation` | `[DOLDUR]` | `[DOLDUR — örn. 40-60]` | `[DOLDUR — 3-5]` |
| `administrative-litigation` | `[DOLDUR]` | `[DOLDUR — örn. 8-15]` | `[DOLDUR — 1-2]` |
| `tax-litigation` | `[DOLDUR]` | `[DOLDUR — örn. 5-10]` | `[DOLDUR — 1-2]` |
| `criminal-defense` | `[DOLDUR]` | `[DOLDUR — özel + CMK görevli]` | `[DOLDUR — CMK haftalık değişir]` |
| `commercial-advisory` | `[DOLDUR — sözleşme sayısı/ay]` | n/a | `[DOLDUR — 10-20 sözleşme/ay]` |
| `corporate-advisory` | `[DOLDUR]` | n/a | `[DOLDUR — 2-4 işlem/ay]` |
| `employment-advisory` | `[DOLDUR]` | `[DOLDUR — dava+danışmanlık]` | `[DOLDUR]` |
| `ip-advisory` | `[DOLDUR]` | `[DOLDUR — TÜRKPATENT tescil sayısı]` | `[DOLDUR]` |
| `firm-operations` | n/a (her gün) | n/a | n/a |

---

## Birincil yargı çevresi

- **Birincil:** Türkiye Cumhuriyeti
- **Birincil venue (mahkemeler):**
  - İstanbul: Çağlayan (asıl), Anadolu, Bakırköy
  - Ankara: Danıştay, Vergi Mahkemeleri, ATB
  - `[DOLDUR — diğer iller müvekkil bazlı]`
- **Tahkim:** ISTAC İstanbul (birincil), ICC Paris (yabancı müvekkil), `[DOLDUR — diğer]`
- **Tabi olunan başlıca mevzuat (büro pratiği):**
  - **1136 sayılı Avukatlık Kanunu** (mesleki çerçeve)
  - **TBB Meslek Kuralları** (etik)
  - 6098 TBK + 6102 TTK (ticari pratik)
  - 6100 HMK + 5271 CMK + 5237 TCK (dava pratiği)
  - 4857 + 5510 + 6356 + 6331 (iş pratiği)
  - 6698 KVKK + GDPR (müvekkil aydınlatma + büro VERBİS sicili)
  - 6362 SPK / 6769 SMK / 5846 FSEK (sektör bazlı)
  - 2577 İYUK + 213 VUK (idari + vergi davası)
  - MASAK Tebliğ Sıra No. 5 (kimlik tespit + şüpheli işlem)

---

## Müvekkil intake politikası

**Yeni müvekkil kabul matrisi:**

| Adım | Skill | Sorumluluk |
|---|---|---|
| 1. İlk temas + ön sohbet | n/a | Sekretarya / Office Manager |
| 2. **Conflict check** (otomatik tarama) | `/firm-operations:conflict-check` | Yönetici Ortak onayı |
| 3. **MASAK kimlik tespit** + tebliğ 5 kontrolü | `/firm-operations:masak-kontrol` | Atanan ortak |
| 4. **OpenSanctions taraması** (tüzel kişi/yurtdışı) | `/firm-operations:sanctions-check` | Atanan ortak |
| 5. **KVKK aydınlatma metni** sunumu | `/firm-operations:kvkk-aydinlatma` | Atanan ortak |
| 6. **Ücret sözleşmesi** taslağı | `/firm-operations:fee-agreement` | Atanan ortak + Yönetici Ortak imza |
| 7. **Vekalet** alımı (noter) | `/firm-operations:vekalet-sablon` | Müvekkil + atanan ortak |
| 8. **Matter açma + UYAP/iManage kayıt** | `/firm-operations:matter-open` | Hukuk Asistanı |
| 9. İlk strateji ön-değerlendirme (matter tipine göre) | `/<plugin>:case-intake` veya `/<plugin>:advisory-intake` | Atanan ortak |

**Otomatik RED tetikleyiciler (müvekkil kabul edilmez):**
- ⛔ **Conflict bulundu** (mevcut/eski müvekkille çatışan iş) — Av. K. m. 38
- ⛔ **OpenSanctions hit** (OFAC/AB/BM listede) — MASAK + ahlaki
- ⛔ **MASAK şüpheli işlem** sinyali — bildirim + kabul incelemesi
- ⛔ **Hukuka aykırı iş talebi** (örn. açıkça suç işleme amacı) — Av. K. m. 38 + meslek kuralı

**🟠 İncelemeli kabul (ortaklar kurulu kararı):**
- 🟠 PEP (Politically Exposed Person) — ekstra due diligence
- 🟠 Yüksek tutar (> `[DOLDUR — örn. 5M TL]`) — sigorta + ekip yapısı
- 🟠 Basına intikal etmiş veya etme riski olan dosya
- 🟠 Yabancı uyruklu müvekkil — kimlik + yurtdışı oturum izni teyit

---

## Risk duruşu (büro seviyesi)

**Genel:** `[Muhafazakar / Dengeli / Risk-alma eğiliminde]`

> Örnek: "Dengeli — meslek kurallarına ve müvekkil menfaatine sıkı bağlılık. Conflict check + KVKK + MASAK güvenli tarafta tutulur. Müvekkil talimatı + yargısal başarı arasındaki dengede, **müvekkili bilgilendirip karar müvekkile bırakma** prensibi."

**Kritik kırmızı çizgiler:**
- **Çıkar çatışması** — Av. K. m. 38'in dar yorumu (eski müvekkil bilgisinin kullanılabilirliği dahil)
- **MASAK + suç gelirleri** — şüpheli işlem bildirim yükümlülüğü
- **OFAC/AB/BM yaptırım listesi** — paid OpenSanctions üyeliği üzerinden
- **Mesleki sır** — yedeksiz paylaşım, açık kanal iletişim, gönderim hatası
- **KVKK** — müvekkil + karşı taraf + tanık + sağlık verisi
- **Vekalet ücreti şişirme** — AAÜT eşik altı + Av. K. m. 164 sınırı

---

## Operasyonel platformlar

| Alan | Platform | Sahibi / Yetkili |
|---|---|---|
| Matter / belge yönetimi | `[DOLDUR — iManage / Worldox / SharePoint / Drive / dahili]` | Yönetici Ortak |
| Vakıa-zaman takibi | `[DOLDUR — TimeSolv / Clio / Excel / dahili]` | Office Manager |
| Fatura / muhasebe | `[DOLDUR — Logo / Mikro / SAP / muhasebeci dış]` | Office Manager + dış muhasebe |
| E-imza / KEP | `[DOLDUR — KEP + e-mza]` | Yönetici Ortak (büro) + her ortak (bireysel) |
| UYAP avukat portalı | UYAP | Her ortak + bağlı avukatlar |
| MERSİS | TBB Avukatlık Ortaklıkları Sicili | Yönetici Ortak |
| CRM (müvekkil ilişki) | `[DOLDUR — Clio / HubSpot / Excel]` | Sekretarya |
| Sanctions tarama | OpenSanctions API | `/firm-operations:sanctions-check` |
| İçtihat | UYAP + Lexpera + Kazancı + Yargı MCP | Tüm avukatlar |

---

## Vekalet ücreti modeli (genel)

> Plugin başına detay `tr-overlay/profiles/<plugin>.md` altında, ama büro seviyesinde tercih:

**Standart model:** `[DOLDUR — Saatlik / Götürü matter / Hibrit (peşin + başarı bonusu)]`
- Saatlik oran (kıdem bazlı):
  - Yönetici/Kıdemli Ortak: `[DOLDUR — örn. 8.000-15.000 TL/saat]`
  - Bağlı Avukat: `[DOLDUR — örn. 3.000-6.000 TL/saat]`
  - Stajyer: `[DOLDUR — n/a veya 1.000-2.000 TL/saat]`
- Götürü matter: AAÜT × katsayı `[DOLDUR — örn. 1.5x-3x]`
- Başarı bonusu (success fee): **Av. K. m. 164** sınırı — uyuşmazlığa konu değerin **%25**'ini geçemez

**KDV:** %20 (genel oran)
**Stopaj:** Müvekkil gerçek kişi/şirket ise %20 stopaj
**Damga:** Ücret sözleşmesi binde 9,48 (DVK Tablo I)

Detay: `references/aaut-rehberi.md` + `references/ucret-sozlesmesi-rehberi.md`

---

## Eskalasyon ve onay matrisi (büro içi)

| Karar | Onay yetkisi | Eskalasyon |
|---|---|---|
| Yeni müvekkil kabulü (rutin) | Atanan ortak + Yönetici Ortak | — |
| Yeni müvekkil kabulü (🟠 incelemeli) | **Ortaklar Kurulu** | — |
| Conflict bulundu — yine de kabul | **Ortaklar Kurulu + yazılı feragat** | — |
| Dava açma (müvekkil adına) | Atanan ortak + müvekkil yazılı talimat | Yönetici Ortak'a bildir |
| Sulh teklif kabul/red | **Müvekkil kararı** (atanan ortak müzakere) | Strateji önerisi: Yönetici Ortak |
| İstinaf/Temyiz başvurusu | Müvekkil kararı + atanan ortak | Yönetici Ortak'a bildir |
| Ücret sözleşmesi imza | Atanan ortak + Yönetici Ortak | Ortaklar Kurulu (büyük matter) |
| Azil / istifa kararı | Atanan ortak + Yönetici Ortak | Ortaklar Kurulu |
| Disiplin riski olan iş (müvekkil talimatı meslek kuralı çatışıyor) | **Ortaklar Kurulu** | Baro Hukuk Müşavirliği danışma |

---

## Müvekkil iletişim politikası

**Resmi kanallar:**
- **KEP** (en güvenli — Av. K. m. 36 koruması + 5070 sayılı K. delil değeri)
- **E-tebligat** (mahkeme/idare ile)
- **Şifreli e-posta** (`[DOLDUR — ProtonMail / standart SSL]`)
- **Telefon** (kayıt yok — sonra not düşülür)

**Kullanılmayan kanallar (mesleki sır riski):**
- ❌ Açık Gmail / Hotmail standart e-posta (büyük dosya alışverişi için)
- ❌ WhatsApp Business — `[DOLDUR — büro politikası: kullanılır mı?]`
- ❌ Genel bulut paylaşımı (link bazlı, şifresiz)

**Müvekkil bilgi paylaşım sınırı:**
- Sözlü iletişimde tanık bulunmamalı (müvekkil dışında)
- Yazılı iletişim KEP veya şifreli (büyük belge için)
- Mahkemeden gelen tebligat müvekkile aynı gün iletilir
- Karar tarihinde müvekkile aynı gün özet + tarama yollanır

---

## "Yakıcı" stres alanları (örnek liste)

> Her büroda 1-3 "the one thing that hurts" alanı olur. Bunları burada flag'leyin — plugin'ler bu alanlarda ekstra dikkat gösterecek.

- `[DOLDUR — örn. CMK görevli atama yoğunluğu — bağlı avukatların yükü]`
- `[DOLDUR — örn. büyük dava müvekkilinin aylık raporlama beklentisi]`
- `[DOLDUR — örn. Ankara ofisi tek ortak — Danıştay duruşma günleri trafik]`
- `[DOLDUR — örn. KEP/UYAP kesintileri — son gün dosyalama riski]`

---

## Plugin-bazlı profil özet referansları

Her plugin'in derin profili `tr-overlay/profiles/<plugin>.md` altındadır:

- `dispute-litigation.md` — Dava playbook, AAÜT uygulaması, tahkim klozu yorumu
- `administrative-litigation.md` — İdari yargı 3 derece, İYUK m. 27 yürütmenin durdurulması taktiği
- `tax-litigation.md` — Vergi davası 30 g süre, uzlaşma matrisi, Danıştay vergi daireleri
- `criminal-defense.md` — CMK 48 saat, müdafiilik, müdahil vekilliği, CMK görevli atama yönetimi
- `commercial-advisory.md` — Sözleşme yazma şablonları, damga, KEP, ISTAC klozu
- `corporate-advisory.md` — TTK GK/YK, pay devri, küçük M&A, aile şirketi
- `employment-advisory.md` — İş davası dava şartı arabuluculuk, işveren/işçi taraf farkı
- `ip-advisory.md` — TÜRKPATENT, Madrid, YİDK itiraz, UDRP
- `firm-operations.md` — Conflict check, MASAK, KVKK aydınlatma, fee, vekalet, baro koord.

---

*Bu şablonun ilk doldurulması için `/firm-operations:cold-start-interview` komutunu kullanın — büro seviyesi için. Sonra her plugin için ayrı `/<plugin>:cold-start-interview`.*

*Author: Claude (Anthropic, Opus 4.7) — Designer: Ertuğ Demir.*
