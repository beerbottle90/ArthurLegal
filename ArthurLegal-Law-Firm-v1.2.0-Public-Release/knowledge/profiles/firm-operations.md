# Firm Operations Practice Profile (Türk Hukuku — Büro işletim ekseni)

*Bu dosya `/firm-operations:cold-start-interview` ile doldurulur. **Bu plugin, diğer 8 plugin'in ÜZERİNDE çalışan büro-seviye operasyon ekseni.** firm-profile.md ile birlikte tüm büronun davranış zeminini belirler.*

---

## Kim olduğumuz

`firm-profile.md` oku. Bu eklentiye özel:

**Pratik modeli:** Büro işletim — **müvekkil intake, conflict check, fee agreement, vekalet, baro koordinasyonu, aylık fatura**
**Birincil yakıcı sorun:** `[DOLDUR — örn. müvekkil sayısı arttıkça conflict check'in derinleşmesi + AAÜT eşik kontrolünün matter bazında elle yapılması]`

**Sorumlu ortak:** **Yönetici Ortak** (varsayılan — bu eksen büronun ana operasyon hattıdır)
**Operasyon ekibi:** `[DOLDUR — Yönetici Ortak + Office Manager + (varsa) Hukuk Asistanı]`

---

## Bu plugin'in farkı

Diğer 8 plugin **müvekkil matter'larında çalışır** (dispute, advisory, ...).
`firm-operations` **büroyu çalıştırır** — müvekkil matter'ları açılmadan önceki ve sonrasındaki **tüm yatay operasyonlar:**

| Aşama | Skill | Bağlam |
|---|---|---|
| **Pre-matter** | `cold-start-interview` | İlk kurulum: büro profili + ortaklar + organizasyon |
| **Pre-matter** | `new-client-intake` | Yeni müvekkil ön sohbet + KVKK + MASAK |
| **Pre-matter** | `conflict-check` | Av. K. m. 38 + TBB MK m. 35-36 çatışma taraması |
| **Pre-matter** | `sanctions-check` | OpenSanctions yaptırım taraması (özellikle tüzel/yabancı) |
| **Pre-matter** | `kvkk-aydinlatma` | KVKK aydınlatma metni sunma |
| **Pre-matter** | `fee-agreement` | Ücret sözleşmesi taslağı |
| **Pre-matter** | `vekalet-sablon` | Vekalet (genel/özel/sınırlı) taslağı |
| **Pre-matter** | `matter-open` | Matter klasörü açma + Drive/iManage kayıt + UYAP kontrol |
| **Operations** | `baro-islem` | Baro işlemleri (CMK ödemesi, aidat, levha) |
| **Operations** | `monthly-billing` | Aylık matter bazlı fatura |
| **Operations** | `aaut-check` | Vekalet ücreti AAÜT eşik kontrolü |
| **Closing** | `matter-close` | Matter kapatma + dosya arşiv + müvekkil tebligat |
| **Closing** | `disengagement-letter` | Avukatlık ilişkisi sonlandırma mektubu |

---

## Müvekkil intake akışı (ana akış)

```
1. İlk temas (telefon/web/referans) — Office Manager kayıt
   ↓
2. Ön sohbet (avukat - en geç 24 saat içinde randevu)
   ↓
3. /firm-operations:new-client-intake
   - Müvekkil bilgisi (kimlik / tüzel kişi)
   - Talep özeti (matter tipi belirler)
   - Aciliyet (süre kontrol)
   ↓
4. /firm-operations:conflict-check  (ZORUNLU)
   ⛔ Conflict bulundu → ret
   🟠 Şüpheli → Yönetici Ortak değerlendirme
   ✓ Temiz → devam
   ↓
5. /firm-operations:masak-kontrol
   - Kimlik tespit (TC kimlik / pasaport / şirket sicil)
   - Gerçek faydalanıcı sorgu (tüzel kişi)
   - Şüpheli işlem sinyali kontrol
   ↓
6. /firm-operations:sanctions-check
   - Müvekkil + (varsa) yurtdışı bağlantı
   - OpenSanctions API
   ⛔ Hit → Yönetici Ortak + ret değerlendirme
   ↓
7. /firm-operations:kvkk-aydinlatma
   - Aydınlatma metni sunma + imza
   - VERBİS sicili kontrol (büro)
   ↓
8. /firm-operations:fee-agreement
   - Matter tipine göre ücret modeli
   - AAÜT + KDV + Stopaj + Damga hesap
   - Av. K. m. 164 başarı bonusu sınırı kontrol
   ↓
9. /firm-operations:vekalet-sablon
   - Genel / özel / sınırlı yetki
   - Noter randevusu (varsa)
   ↓
10. /firm-operations:matter-open
    - matter-slug oluştur
    - Matter klasörü açma
    - Drive/iManage paylaşım ayarı
    - UYAP'a vekalet sunumu (dava matter'larında)
   ↓
11. İlgili plugin'in cold-start (matter-spesifik)
    - /dispute-litigation:case-intake
    - /commercial-advisory:contract-intake
    - vd.
```

---

## Conflict check — derinlik tablosu

| Tetik | Tarama derinliği |
|---|---|
| Yeni müvekkil intake | **Tam tarama** — tüm aktif + tasfiye + reddedilen matter'lara karşı |
| Mevcut matter'da karşı yan netleşti | **Karşı yan ve grup** taraması |
| Mevcut müvekkilin başka bir işi | **Yan-grup** taraması (yan grup şirketler) |
| Ortak değişimi (yeni ortak alındı) | **Yeni ortağın eski büro/in-house geçmişi** taraması |
| Müvekkil yapısı değişti (M&A, pay devri) | **Yeniden tarama** — eski müvekkil yeni grup içine girdi mi |

### Av. K. m. 38 — yasaklılık çerçevesi

> "Aynı işte menfaati zıt bir tarafa vekalet eden veya hakem, hakim, savcı, savcı yardımcısı, jüri üyesi, müdür, kâtip, zabıt kâtibi, mübaşir, posta memuru, polis veya başka bir kamu görevlisi sıfatıyla bilgi sahibi olduğu bir işte vekâlet alamaz."

**Tetikleyiciler:**
- **Eski müvekkille yeni iş** — eski matter ne kadar bağlı?
- **Karşı tarafın ilişkili şirketi** — grup üyeliği
- **Stajda gördüğümüz dosya** — staj sırasında gördüğümüz dosyalar
- **Kamu görevliyken gördüğümüz işler** (eski hakim/savcı/müfettiş)

### TBB Meslek Kuralları m. 35-36

- m. 35: **Mevcut müvekkilin menfaatine aykırı iş** kabul edilemez
- m. 36: **Eski müvekkilin bilgilerini** yeni müvekkil yararına kullanamaz; **eski müvekkilin yazılı rızası** ile çatışmayan işler kabul edilebilir

### Conflict-clearance prosedürü

🟠 şüpheli durumda:
1. Eski müvekkille **yazılı rıza** iste (mümkünse — bazen yeni müvekkilin kim olduğunu açıklamak da çatışma)
2. **Ethical wall (çin duvarı)** kur — büromuzda farklı ortak/avukat ayrı dosyada çalışsın, bilgi paylaşımı yasak
3. Ortaklar Kurulu kararı
4. **Reddet** (çoğu zaman en güvenli)

Detay: `references/conflict-check-rehberi.md`

---

## MASAK Tebliğ Sıra No. 5

Avukatlık mesleki faaliyetlerinde **belirli yüksek-risk işler** için:
- **Kimlik tespit yükümlülüğü** (gerçek kişi: TC kimlik; tüzel kişi: sicil + gerçek faydalanıcı)
- **Şüpheli işlem bildirim yükümlülüğü** (MASAK'a)

**Yüksek-risk işler (Tebliğ 5):**
- Gayrimenkul alım-satım (avukatın aracı sıfatıyla iş yapması)
- Şirket kuruluş + ortaklık yapısı düzenleme
- Banka hesabı açılışı + yönetimi (müvekkil adına)
- Müvekkilin parası ile alım-satım
- Belirli tutar üzeri nakit işlem (matter ücreti vd.)

**Pratik:**
- Her yeni müvekkil intake → kimlik tespit fotoğrafı / kopya + matter dosyasında saklama (5 yıl)
- Şüpheli işlem sinyali → büronun MASAK Görevlisi (Yönetici Ortak veya atanmış) bildirim kararı

Detay: `references/masak-kimlik-tespit-rehberi.md`

---

## Ücret sözleşmesi (Av. K. m. 163-166)

**Sözleşme şart:**
- **Yazılı** olmalı (Av. K. m. 163) — yoksa AAÜT tarifesi uygulanır
- **Damga vergisi:** binde 9,48 (DVK Tablo I)
- **KDV:** %20 (avukatlık hizmeti)
- **Stopaj:** Müvekkil gerçek kişi/şirket ise **%20 gelir vergisi stopajı** (GVK m. 94)

**Başarı bonusu (success fee):**
- Av. K. m. 164/2: **Uyuşmazlığa konu değerin %25'ini geçemez**
- "Uyuşmazlığa konu değer" — para alacağında net; tespit/inşai davada AAÜT × katsayı

**Karşı yan vekalet ücreti (Av. K. m. 164/4):**
- Karşı yan aleyhine hükmedilen vekalet ücreti **vekile aittir** (sözleşmede aksi yazılmadıkça)
- Aksi sözleşmede yazılırsa vekile katsayı eklenebilir veya müvekkille paylaşılır
- **Açıkça** sözleşmede belirt — sonradan çatışma olmasın

Detay: `references/ucret-sozlesmesi-rehberi.md` + `references/aaut-rehberi.md`

---

## Vekalet türleri

| Tip | Kapsam | Noter şart? |
|---|---|---|
| **Genel vekalet** | Tüm dava ve işler | Noter onaylı (Av. K. m. 32) |
| **Özel vekalet** | Belirli matter (örn. boşanma, satım sözleşmesi imza) | Noter onaylı |
| **Sınırlı (özel) yetkili** | Yetki sınırlı (örn. sulh, ibra, ferağ — özel olarak belirt) | Noter onaylı + **özel yetkili madde** açık yazılmalı |
| **Baro onaylı vekalet** | Sadece bazı baro içi işlemler | Noterli olmasa da geçerli |

**Av. K. m. 35 müdafiilik:** Ceza dosyalarında noter vekaleti şart değil; **müvekkilin yazılı talep** veya **baro CMK atama yazısı** yeterli.

**Azil + istifa:**
- Müvekkil **azil** edebilir (her zaman) — yazılı + UYAP'a bildirim
- Avukat **istifa** edebilir — müvekkili 15 gün önce yazılı bilgilendir + dava tarafsız bırakılmayacak şekilde

Detay: `references/vekalet-uyap-rehberi.md`

---

## Baro koordinasyonu

| İş | Sıklık | Sorumlu |
|---|---|---|
| Yıllık aidat ödeme | Yıllık (Şubat/Mart) | Her ortak/avukat (kendisi) |
| Sicil dosyası bilgi güncelleme | Olayda | Office Manager |
| Levha değişikliği (asıl ↔ bağlı) | Olayda | İlgili avukat |
| CMK ödeme cetveli teslim | Aylık | İlgili avukat |
| Disiplin yazışmaları (varsa) | Olayda | Yönetici Ortak |
| Av. ortaklığı yıllık beyan | Yıllık | Yönetici Ortak |
| Hizmet süresi belgesi (HSB) talebi | Olayda (örn. yeni avukat alımı) | İlgili avukat |
| Staj evrakı (stajyer) | Periyodik | Sorumlu ortak |

Detay: `references/baro-islemleri-rehberi.md`

---

## Aylık fatura akışı

```
1. Ay sonu — tüm avukatlar matter bazlı süre + matter notlarını kapatır
   ↓
2. /firm-operations:monthly-billing
   - Matter listesi (aktif)
   - Süre toplamı (avukat × matter)
   - AAÜT eşik kontrol (her matter için)
   - Ücret modeline göre fatura tutarı:
     · Saatlik → süre × oran
     · Sabit (retainer) → aylık sabit
     · Başarı bonusu (matter kapanmışsa) → uyuşmazlığa konu değer × % (Av. K. m. 164 sınırı)
   - KDV (%20) + Stopaj uyarısı (%20)
   - Damga (binde 9,48 — fatura için DEĞİL, sözleşme için; yine fatura altında not)
   ↓
3. Müvekkile fatura sunumu (KEP veya posta)
   ↓
4. Ödeme takibi (Office Manager)
   ↓
5. Geç ödeme — temerrüt faizi (TBK m. 120 + TTK m. 1530 ticari)
```

---

## Eskalasyon ve onay matrisi

| Karar | Onay yetkisi |
|---|---|
| Yeni müvekkil kabulü (rutin) | Atanan ortak + Yönetici Ortak |
| Yeni müvekkil kabulü (🟠 incelemeli) | **Ortaklar Kurulu** |
| Conflict bulundu — yine de kabul | **Ortaklar Kurulu + yazılı feragat** |
| MASAK şüpheli işlem bildirimi | **MASAK Görevlisi + Yönetici Ortak** |
| KVKK ihlal şüphesi (büro) | Yönetici Ortak + (gerekirse) KVKK Kurulu bildirim 72 saat |
| Sanctions hit (OFAC/AB/BM) | **Yönetici Ortak + Ortaklar Kurulu + ret kararı** |
| Ücret sözleşmesi imza | Atanan ortak + Yönetici Ortak |
| Disengagement (avukatlık ilişkisini sonlandırma) | Atanan ortak + Yönetici Ortak |
| Disiplin riski (meslek kuralı çatışması) | **Ortaklar Kurulu + Baro Hukuk Müşavirliği danışma** |

---

## Outputs

**Müvekkil intake özet notu:**
```
AVUKATLIK K. m. 36 – MÜVEKKİL INTAKE NOTU – DAHİLİ VE GİZLİDİR
[Büro] – Matter ID: [matter-slug] (taslak — henüz açılmadı)
Müvekkil: [rumuz] – Tip: [Bireysel / Tüzel kişi]
Talep özeti: [...]
Conflict check: ✓ TEMİZ / 🟠 ŞÜPHELİ / ⛔ ÇATIŞMA
MASAK: ✓ TAMAM / 🟠 İNCELE
Sanctions: ✓ TEMİZ / ⛔ HIT
Önerilen plugin: [dispute-litigation / commercial-advisory / vd.]
Ücret tahmini: [TL aralık]
KARAR: ✓ KABUL / 🟠 ORTAKLAR KURULU / ⛔ RET
```

**Ücret sözleşmesi taslağı:** "TASLAK – İMZA BEKLİYOR + DAMGA VERGİSİ ÖDENMELİ" ekle.

**Vekalet metni:** Standart noter şablonu — müvekkilin noterden alacağı şablon.

**Aylık fatura paketi:** Matter bazlı, KDV/stopaj dahil, KEP teslim hazır.

### Atıf disiplini

- `[Mevzuat MCP — Av. K. m. X / TBB MK m. X / DVK Tablo I / GVK m. 94 — GG.AA.YYYY]`
- `[OpenSanctions API — match skoru — GG.AA.YYYY]`
- `[MASAK Tebliğ Sıra No. 5 — bölüm]`
- `[AAÜT — 2026 baskı — TBB onay]`
- `[KVKK m. X — Kurul kararı — GG.AA.YYYY]`

---

## Karar duruşu

Bu plugin **kapı bekçisi** rolündedir:
- ⛔ Açıkça yasak (conflict, sanctions, MASAK kırmızı) → RED ve kayıt
- 🟠 Şüpheli → Ortaklar Kurulu (insan kararı)
- ✓ Temiz → akış başlar

**"Şüphede kalırsak ret"** — büronun uzun vadeli itibarı tek bir riskli matter'dan kıymetlidir.

---

## Shared guardrails

Tüm diğer plugin'lerin de uyguladığı temel guardrail'lar (üç değer kuralı, güncellik tetikleyici, hassas karar ön-kontrol).

**Bu plugin özel:**
- **Mesleki sır mutlak** — intake notları, conflict tarama sonuçları, ücret sözleşmesi taslakları **asla** matter dışında paylaşılamaz
- **Müvekkil ret kararı** kayıt altında tutulur — gelecekteki çatışma çözümünde delil
- **MASAK + KVKK bildirim takvimi** — her gecikme = idari para cezası riski

---

## Matter workspaces

Bu plugin'in çıktıları matter klasörü açılmadan önce **`pre-matter/<tarih>__<müvekkil-rumuz>/`** geçici klasörde toplanır. Matter açıldığında (kabul kararı) `matters/<müvekkil-slug>__<matter-slug>/` altına taşınır.

**Ret kararı sonrası:** `pre-matter/<tarih>__<müvekkil-rumuz>/REJECTED.md` — sadece ret gerekçesi + temel kimlik + tarih (mesleki sır + gelecek çatışma çözümünde delil).

---

## Seed (büro tarihinden örnek matter'lar)

| Müvekkil rumuz | İlk intake | Tip | Conflict/MASAK | Karar | Açıklama |
|---|---|---|---|---|---|
| [DOLDUR] | | | | KABUL/RET | |

---

*Re-run interview:* `/firm-operations:cold-start-interview --redo*
