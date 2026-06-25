# Büro Profili — [BÜRO_ADI]

> Bu dosya tüm plugin'ler tarafından okunur. Büro ve kullanıcı seviyesindeki temel bilgiler buraya yazılır.
>
> **`[DOLDUR]` etiketli alanlar kurulum sırasında doldurulmalıdır.**
> Doldurmak için: `/firm-operations:cold-start-interview` komutunu çalıştırın.
>
> **Kaynak etiketleri:**
> - `[büro]` — Büronun kendi verisi (iç bilgi)
> - `[baro]` — Baro sicil kaydından (kamuya açık)
> - `[DOLDUR]` — Kurulum sırasında kullanıcı tarafından doldurulacak

---

## Kim olduğumuz

**Büro adı:** [DOLDUR — tam resmi ünvan]
**Hukuki yapı:** [DOLDUR — Avukatlık Ortaklığı / Bireysel Avukatlık Bürosu / Hibrit]
**TBB Avukatlık Ortaklıkları Sicil no:** [DOLDUR — varsa]
**Kuruluş yılı:** [DOLDUR]
**Vergi no:** [DOLDUR]
**Pratik ortamı:** Dışarıdan danışmanlık (law firm / dış avukatlık bürosu)

---

## Ofis ve coğrafya

**Merkez ofis:** [DOLDUR — il / ilçe / cadde]
**İrtibat ofisleri:** [DOLDUR — varsa; yoksa "Yok"]
**Çalışma dilleri:** [DOLDUR — örn. Türkçe (ana), İngilizce]

---

## Kadro

**Yönetici Ortak:** [DOLDUR — rumuz + baro sicil no + uzmanlık]
**Kıdemli Ortaklar:** [DOLDUR — sayı + uzmanlık dağılımı]
**Bağlı avukat sayısı:** [DOLDUR]
**Stajyer sayısı:** [DOLDUR]
**Hukuk asistan + sekretarya:** [DOLDUR]
**Toplam kadro:** [DOLDUR — 0-30 bandı öngörülmüş]

### Baro kayıt

| Baro | Ortak/Avukat sayısı | Kayıt tipi |
|---|---|---|
| [DOLDUR — örn. İstanbul Barosu] | [N] | Asıl |
| [DOLDUR — örn. Ankara Barosu] | [N] | Asıl/Bağlı |

---

## Müvekkil portföyü (agregat — gerçek isim YOK)

**Aktif müvekkil sayısı:** [DOLDUR]
**Sürekli danışmanlık (retainer) sayısı:** [DOLDUR]

**Müvekkil tip dağılımı:**
- Bireysel: [%]
- KOBİ: [%]
- Mid-cap / büyük kurumsal: [%]
- Yabancı müvekkil: [%]

**Sektör dağılımı:** [DOLDUR — örn. inşaat %30 / perakende %20 / üretim %20 / hizmet %30]

**Coğrafi dağılım:** [DOLDUR — örn. İstanbul %70 / Ankara %15 / diğer %15]

---

## Aktif pratik alanları

> Kurulum sırasında hangi plugin'lerin aktif kullanılacağını işaretle.

| Plugin | Aktif mi? | Aylık matter tahmini |
|---|---|---|
| `commercial-legal` | [Evet/Hayır] | [N] |
| `corporate-legal` | [Evet/Hayır] | [N] |
| `employment-legal` | [Evet/Hayır] | [N] |
| `privacy-legal` | [Evet/Hayır] | [N] |
| `regulatory-legal` | [Evet/Hayır] | [N] |
| `ip-legal` | [Evet/Hayır] | [N] |
| `litigation-legal` | [Evet/Hayır] | [N] |
| `tax-legal` | [Evet/Hayır] | [N] |
| `administrative-legal` | [Evet/Hayır] | [N] |
| `energy-finance` | [Evet/Hayır] | [N] |
| `criminal-defense` | [Evet/Hayır] | [N] |
| `firm-operations` | Evet (her büro) | — |

---

## Risk duruşu

**Genel:** [DOLDUR — örn. Dengeli / Muhafazakâr / Dinamik]

**Kritik kırmızı çizgiler (büro seviyesi):**
- **OFAC / AB / BM yaptırım listeleri** — yaptırım altındaki karşı tarafla işlem yok
- **Çıkar çatışması (Av. K. m. 38)** — conflict check her yeni matter'da zorunlu
- **MASAK kimlik tespit (5549 sayılı Kanun)** — her yeni müvekkilde kimlik + UBO
- **Avukatlık Kanunu m. 164** — başarı bonusu max %25
- [DOLDUR — büro-spesifik ek kırmızı çizgiler]

---

## Müvekkil intake politikası

**Conflict check derinliği:** [DOLDUR — son N yıl, fonetik tarama var mı?]
**MASAK kimlik tespit standardı:** [DOLDUR — zorunlu belgeler listesi]
**Sanctions tarama:** OpenSanctions API (`opensanctions-rehberi.md`) — tüzel ve yabancı müvekkil zorunlu
**KVKK aydınlatma:** [DOLDUR — standart metin var mı?]
**Otomatik 🟠 inceleme tetikleyicileri:**
- PEP (siyasi açıdan önemli kişi) müvekkil
- Yabancı uyruklu müvekkil
- Tahmini değer > [DOLDUR — TL eşiği]
- [DOLDUR — ek tetikleyiciler]

---

## Vekalet ücreti modeli

**Standart model:** [DOLDUR — saatlik / götürü / hibrit / başarı bonusu]

| Kademe | Saatlik oran (TL/saat) |
|---|---|
| Yönetici Ortak | [DOLDUR] |
| Kıdemli Ortak | [DOLDUR] |
| Bağlı Avukat | [DOLDUR] |
| Stajyer | [DOLDUR] |

**Başarı bonusu:** Max %25 (Av. K. m. 164)
**Karşı yan vekalet ücreti:** [DOLDUR — büro politikası]

---

## Birincil yargı çevresi

- **Birincil:** Türkiye Cumhuriyeti
- **İkincil:** [DOLDUR — müvekkil portföyüne göre: UK / AB / ABD / diğer]
- **Tahkim:** [DOLDUR — ISTAC / ICC / başka]

**Tabi olunan başlıca mevzuat:**
- 6098 sayılı Türk Borçlar Kanunu (TBK)
- 6102 sayılı Türk Ticaret Kanunu (TTK)
- 4857 sayılı İş Kanunu + 5510 SGK Kanunu
- 6698 sayılı KVKK
- 6362 sayılı Sermaye Piyasası Kanunu (halka açık müvekkil varsa)
- 4054 sayılı Rekabetin Korunması Hakkında Kanun
- 6769 sayılı Sınai Mülkiyet Kanunu (SMK)
- 1136 sayılı Avukatlık Kanunu
- [DOLDUR — sektöre özel ek mevzuat]

---

## Litigation profili (özet)

**Litigation modeli:** [DOLDUR — Doğrudan temsil / Dış vekil ağırlıklı / Karma]
**Aktif dava hacmi:** [DOLDUR — tahmini]
**Birincil yargı yerleri:** [DOLDUR — örn. İstanbul, Ankara, ISTAC]

**Dış vekil paneli (varsa):**
- Ticari uyuşmazlık: [DOLDUR]
- İdari / Danıştay: [DOLDUR]
- Tahkim: [DOLDUR]

---

## Operasyonel platformlar

| Platform | Araç |
|---|---|
| Matter / belge yönetimi | [DOLDUR — iManage / SharePoint / Drive / dahili] |
| Zaman takibi | [DOLDUR — Clio / TimeSolv / Excel] |
| Fatura / muhasebe | [DOLDUR] |
| E-imza / KEP | [DOLDUR] |
| CRM | [DOLDUR — varsa] |
| Sanctions tarama | OpenSanctions API — `OPENSANCTIONS_API_KEY` [kuruldu mu?] |

---

## Kullanıcı rolü

> Bu bölüm kurulum sırasında `/<plugin>:cold-start-interview` skill'i ile her kullanıcı için ayrı ayrı doldurulur.

**Bu asistanı kullanan kişi:** [DOLDUR — rumuz veya rol tanımı; gerçek isim yazmayın]
**Pozisyon:** [DOLDUR — örn. Kıdemli Avukat / Ortak / Stajyer Avukat]
**Rol tipi:** [DOLDUR — Avukat (baroya kayıtlı) / Stajyer / Legal Analyst]
**Doğrudan amir:** [DOLDUR — Yönetici Ortak / Kıdemli Ortak]
**Aktif pratik alanları:** [DOLDUR — hangi plugin'leri kullanıyor]
**Risk duruşu:** [DOLDUR — büro genel duruşunu devral veya özelleştir]

---

## Resmi Gazete / mevzuat takip kanalları

- **Resmi Gazete:** https://www.resmigazete.gov.tr/ (günlük 09:30)
- **TR Legal MCP:** Birleşik connector (`yargi-mcp-pro`) üzerinden yürürlükteki kanun/KHK/yönetmelik/tebliğ + Yargıtay/Danıştay/AYM ve kurul kararları.
- **Sektör düzenleyicileri (müvekkil portföyüne göre):**
  - **EPDK** — https://www.epdk.gov.tr
  - **Rekabet Kurumu** — https://www.rekabet.gov.tr
  - **SPK + KAP** — https://www.spk.gov.tr, https://www.kap.org.tr (halka açık müvekkil için)
  - **KVKK Kurulu** — https://www.kvkk.gov.tr
  - **TÜRKPATENT** — https://www.turkpatent.gov.tr (IP pratik alanı için)
  - [DOLDUR — büro müvekkil portföyüne göre ek regülatörler]

---

## Privilege & gizlilik notları (Türk hukuku özellikleri)

- **Avukat–müvekkil görüşme gizliliği:** 1136 sayılı Avukatlık Kanunu m. 36
- **TBK m. 6, TTK m. 18 — ticari sır**
- **KVKK m. 28 — yargı süreci istisnası**

**Önerilen üst başlık (iç memorandumlar için):**

```
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU
[BÜRO_ADI]
Bu belge yalnızca hukuk müşavirliği değerlendirmesi içindir.
Üçüncü kişilere iletilmeden önce Yönetici Ortak onayı alınmalıdır.
```

---

## Bilinen risk olayları / aktif konular (snapshot)

| Tarih | Konu | Durum | Sahibi |
|---|---|---|---|
| [DOLDUR] | | | |

*Bu tablo cold-start ile veya manuel güncellenir.*

---

*Kurulum tarihi:* [DOLDUR — GG.AA.YYYY]
*Son güncelleme:* [DOLDUR — GG.AA.YYYY]
*Bu dosyayı dolduran:* [DOLDUR — /firm-operations:cold-start-interview çıktısı]
