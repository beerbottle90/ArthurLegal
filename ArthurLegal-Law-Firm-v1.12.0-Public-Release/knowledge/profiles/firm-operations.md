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
| **Operations** | `baro-islem` | Baro işlemleri (CMK ödemesi, aidat, levha). *Hazırlanıyor; henüz skill değil.* |
| **Operations** | `monthly-billing` | Aylık matter bazlı fatura |
| **Operations** | `aaut-check` | Vekalet ücreti AAÜT eşik kontrolü. *Ayrı skill değil; `fee-agreement` ve `monthly-billing` içinde yapılır.* |
| **Closing** | `matter-close` | Matter kapatma + dosya arşiv + müvekkil tebligat. *Hazırlanıyor; henüz skill değil.* |
| **Closing** | `disengagement-letter` | Avukatlık ilişkisi sonlandırma mektubu. *Hazırlanıyor; henüz skill değil.* |

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
11. İlgili plugin'e devir (matter-spesifik)
    - dava: /litigation-legal:case-intake
    - diğer işler: ilgili plugin'in skill listesi (profil boşsa önce o plugin'in cold-start-interview'u)
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

### Av. K. m. 38 — işin reddi zorunluluğu

Dayanak: AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 38 (metin 24.09.2026'da `tr_mevzuat_madde_getir` ile doğrulandı). Avukat şu hâllerde teklifi reddetmek zorundadır:

- (a) teklifi yolsuz veya haksız görür ya da sonradan böyle olduğu kanısına varırsa,
- (b) aynı işte menfaati zıt bir tarafa avukatlık etmiş veya mütalaa vermişse,
- (c) evvelce hâkim, hakem, Cumhuriyet savcısı, bilirkişi veya memur olarak o işte görev yapmışsa,
- (d) kendi düzenlediği bir senet veya sözleşmenin hükümsüzlüğünü ileri sürmek durumu ortaya çıkmışsa,
- (f) görmesi istenen iş TBB'nin tespit ettiği mesleki dayanışma ve düzen gereklerine uygun değilse.

(e) bendi Anayasa Mahkemesince iptal edilmiştir. Bu zorunluluk avukatın **ortaklarını ve yanında çalışan avukatları da** kapsar (m. 38/2); çatışma taraması bu yüzden büro çapında yapılır.

**Tetikleyiciler:**
- **Eski müvekkille yeni iş** — eski matter ne kadar bağlı?
- **Karşı tarafın ilişkili şirketi** — grup üyeliği
- **Stajda gördüğümüz dosya** — staj sırasında gördüğümüz dosyalar
- **Kamu görevliyken gördüğümüz işler** (eski hakim/savcı/müfettiş)

### TBB Meslek Kuralları m. 35-36

*Metin mevzuat.gov.tr'de bulunmadığı için bu araçla doğrulanamadı; aşağıdaki özet kaynağıyla karşılaştırılmadan atıf olarak kullanılmaz.*

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

## MASAK — 5549 sayılı Kanun ve Tedbirler Yönetmeliği

Dayanak (24.09.2026'da `tr_mevzuat_madde_getir` ile doğrulandı): SUÇ GELİRLERİNİN AKLANMASININ ÖNLENMESİ HAKKINDA KANUN (Kanun No. 5549, RG 18.10.2006/26323) m. 2, m. 3, m. 4, m. 8 ve SUÇ GELİRLERİNİN AKLANMASININ VE TERÖRÜN FİNANSMANININ ÖNLENMESİNE DAİR TEDBİRLER HAKKINDA YÖNETMELİK (Cumhurbaşkanlığı / Bakanlar Kurulu Yönetmeliği No. 200713012, RG sayı 26751) m. 4, m. 5, m. 17/A, m. 28.

> Bu bölüm eskiden "MASAK Tebliğ Sıra No. 5"e dayanıyordu. O Tebliğin (RG 09.04.2008/26842) konusu **basitleştirilmiş tedbirlerdir**; avukat yükümlülüğünü düzenlemez.

Serbest avukat **yalnız** şu işlere ilişkin **finansal işlemlerin gerçekleştirilmesiyle** sınırlı olarak yükümlüdür (5549 m. 2/1-d; Yön. m. 4/1-ş):
- taşınmaz alım satımı
- sınırlı ayni hak kurulması ve kaldırılması
- şirket, vakıf ve dernek kurulması, birleştirilmesi, idaresi, devredilmesi ve tasfiyesi
- banka, menkul kıymet ve her türlü hesap ile bu hesaplardaki varlıkların idaresi

Av. K. m. 35'in birinci ve üçüncü fıkrası ile alternatif uyuşmazlık çözüm yolları kapsamındaki mesleki faaliyetler sırasında edinilen bilgiler **hariçtir**. Dava vekilliği ve mütalaa bu yüzden çoğunlukla kapsam dışıdır.

Kapsamdaki işte:
- **Kimlik tespiti** iş ilişkisi kurulmadan önce, sürekli iş ilişkisinde tutar gözetmeksizin (Yön. m. 5)
- **Gerçek faydalanıcı:** tüzel kişiliğin %25'ini **aşan** hisseye sahip gerçek kişi ortaklar; yoksa nihai kontrol eden kişi; o da yoksa en üst düzey icra yetkilisi (Yön. m. 17/A)
- **Şüpheli işlem bildirimi:** şüphenin oluştuğu tarihten itibaren en geç on iş günü içinde (Yön. m. 28/2); bildirim müvekkil dahil kimseye açıklanamaz (5549 m. 4/2)
- **Muhafaza:** kimlik tespiti belgeleri son işlem tarihinden itibaren **sekiz yıl** (5549 m. 8)

Uygulama: `/firm-operations:masak-kontrol`.

Detay: `references/masak-kimlik-tespit-rehberi.md`

---

## Ücret sözleşmesi (Av. K. m. 163-166)

Dayanak: AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 163, m. 164 (24.09.2026'da doğrulandı).

**Şekil:**
- Kanun yazılı şekli geçerlilik şartı yapmaz; yazılı olmayan anlaşma genel hükümlere göre ispatlanır (Av. K. m. 163/1). Yine de **yazılı yap**: ücret kararlaştırılmamışsa veya yazılı sözleşme yoksa, para ile ölçülebilen işlerde AAÜT altında kalmamak üzere müddeabihin %10-20'si arasında ücret belirlenir; para ile ölçülemeyen işlerde AAÜT uygulanır (m. 164/4).
- **Damga vergisi:** belli parayı ihtiva eden sözleşmede binde 9,48; nispi vergide yalnız bir nüsha vergilenir (DAMGA VERGİSİ KANUNU (Kanun No. 488, RG sayı 11751) m. 5 ve (1) sayılı tablo I/A-1; 24.09.2026'da doğrulandı).
- **KDV ve tevkifat oranları** bu pakette doğrulanmadı; her sözleşmede güncel kaynaktan kontrol edilir.
- **Tevkifat:** GVK m. 94'te sayılan ödeyiciler yapar (ör. ticaret şirketleri, kamu idareleri, gerçek gelirini beyan eden ticaret ve serbest meslek erbabı). Olağan bireysel müvekkil tevkifat yapmaz.

**Yüzde ücret (başarıya bağlı):**
- Dava veya hükmolunacak şeyin değeri yahut paranın belli bir yüzdesi, **%25'i aşmamak üzere** kararlaştırılabilir (Av. K. m. 164/2).
- Tavanı aşan sözleşme tavan miktarında geçerlidir (m. 163/2).

**Karşı taraf vekâlet ücreti (Av. K. m. 164/5):**
- Kararla karşı tarafa yüklenen vekâlet ücreti **avukata aittir**; iş sahibinin borcu nedeniyle takas ve mahsup edilemez, haczedilemez.
- Kanun metni "sözleşmede aksi yazılmadıkça" istisnası içermez. Farklı bir paylaşım yazılacaksa geçerliliği içtihatla doğrulanmalı (doğrulanmadı).
- Sözleşmede **açıkça** belirt.

Uygulama: `/firm-operations:fee-agreement`.

Detay: `references/ucret-sozlesmesi-rehberi.md` + `references/aaut-rehberi.md`

---

## Vekalet türleri

Dayanak: HUKUK MUHAKEMELERİ KANUNU (Kanun No. 6100, RG sayı 27836) m. 74, m. 76, m. 77; AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 41, m. 56, m. 174; TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG sayı 27836) m. 512 (24.09.2026'da doğrulandı).

| Tip | Kapsam | Şekil |
|---|---|---|
| **Genel vekalet** | Tüm dava ve işler | Tek tip vekâletname (Av. K. m. 56/6); dosyaya noter onaylı/düzenlenmiş aslı veya avukat onaylı örneği ibraz edilir (HMK m. 76/1) |
| **Özel vekalet** | Belirli iş | Aynı |
| **Özel yetkili** | HMK m. 74'teki işlemler (sulh, ibra, feragat, kabul, tevkil vb.) | Yetki **açıkça** yazılmalı (HMK m. 74) |
| **Yetki belgesi** | Avukatın tevkil yetkili tüm vekâletnamelerini kapsar | Vekâletname hükmünde (Av. K. m. 56/5) |

- Av. K. m. 32 **mülgadır** (30/1/1979 - 2178/8); vekâletname şekline dayanak değildir.
- Av. K. m. 35 "yalnız avukatların yapabileceği işler"dir; müdafilikte vekâletname kuralı içermez. Ceza dosyasında müdafi seçimi ve görevlendirilmesi CMK m. 149-150'dedir; seçilmiş müdafinin vekâletname ibraz zamanı bu pakette doğrulanmadı.

**Azil + çekilme:**
- Vekâlet veren de vekil de sözleşmeyi her zaman tek taraflı sona erdirebilir; uygun olmayan zamanda sona erdiren zararı giderir (TBK m. 512).
- Azilde ücretin tamamı ödenir; kusur veya ihmal nedeniyle azilde ödenmez (Av. K. m. 174/2).
- Avukat çekilirse vekâlet görevi, durumun müvekkile **tebliğinden itibaren 15 gün** devam eder (Av. K. m. 41/1).

Uygulama: `/firm-operations:vekalet-sablon`.

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
     · Yüzde ücret (şart gerçekleşmişse) → değer × % (Av. K. m. 164/2: en çok %25)
   - Serbest meslek makbuzu (VUK m. 236) + tevkifat kontrolü (GVK m. 94; oranlar doğrulanmadı)
   ↓
3. Müvekkile fatura sunumu (KEP veya posta)
   ↓
4. Ödeme takibi (Office Manager)
   ↓
5. Geç ödeme — temerrüt (TBK m. 117) ve faiz (TBK m. 120; 3095 m. 1-2). TTK m. 1530'un avukatlık ücretine uygulanıp uygulanmadığı doğrulanmadı.
```

---

## Eskalasyon ve onay matrisi

| Karar | Onay yetkisi |
|---|---|
| Yeni müvekkil kabulü (rutin) | Atanan ortak + Yönetici Ortak |
| Yeni müvekkil kabulü (🟠 incelemeli) | **Ortaklar Kurulu** |
| Conflict bulundu — yine de kabul | **Ortaklar Kurulu + yazılı feragat** |
| MASAK şüpheli işlem bildirimi | **MASAK Görevlisi + Yönetici Ortak** |
| KVKK ihlal şüphesi (büro) | Yönetici Ortak + ilgiliye ve Kurula **en kısa sürede** bildirim (KVKK m. 12/5; "72 saat" bir Kurul kararına dayanır, künyesi doğrulanmadı) |
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
Müvekkil: [takma ad] – Tip: [Bireysel / Tüzel kişi]
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

- Madde atfı: `tr_mevzuat_madde_getir` yanıtındaki `citation` alanı birebir (ör. `AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 164`). Çekilemeyen madde "doğrulanmadı" diye işaretlenir.
- `[OpenSanctions API — match skoru — GG.AA.YYYY]`
- `[5549 m. X / Tedbirler Yön. m. X — GG.AA.YYYY]`
- `[AAÜT — RG tarih/sayı]` (24.09.2026 itibarıyla son kayıt: RG 04.11.2025/33067)
- `[KVKK m. X — Kurul kararı künyesi — GG.AA.YYYY]`
- TBB Meslek Kuralları mevzuat.gov.tr'de yok; atıf yapılacaksa kaynağı ayrıca gösterilir.

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

Bu plugin'in çıktıları matter klasörü açılmadan önce **`pre-matter/<tarih>__<müvekkil-takma-ad>/`** geçici klasörde toplanır. Matter açıldığında (kabul kararı) `matters/<müvekkil-slug>__<matter-slug>/` altına taşınır.

**Ret kararı sonrası:** `pre-matter/<tarih>__<müvekkil-takma-ad>/REJECTED.md` — sadece ret gerekçesi + temel kimlik + tarih (mesleki sır + gelecek çatışma çözümünde delil).

---

## Seed (büro tarihinden örnek matter'lar)

| Müvekkil takma adı | İlk intake | Tip | Conflict/MASAK | Karar | Açıklama |
|---|---|---|---|---|---|
| [DOLDUR] | | | | KABUL/RET | |

---

*Re-run interview:* `/firm-operations:cold-start-interview --redo*
