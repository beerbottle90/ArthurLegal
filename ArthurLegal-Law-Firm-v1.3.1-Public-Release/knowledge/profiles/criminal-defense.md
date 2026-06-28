# Criminal Defense Practice Profile (Türk Hukuku — Büro tarafı)

*Bu dosya `/criminal-defense:cold-start-interview` ile doldurulur.*

---

## Kim olduğumuz

`firm-profile.md` oku. Bu eklentiye özel:

**Pratik modeli:** Ceza müdafaa — **şüpheli/sanık vekilliği + müdahil (mağdur) vekilliği + CMK görevli atama**
**Aktif ceza dosyası hacmi:** `[DOLDUR — örn. özel 5-10 + CMK görevli aylık 3-8 dosya]`
**Birincil yakıcı sorun:** `[DOLDUR — örn. CMK görevli atama zamanlaması (gece/hafta sonu) + 48 saat sınırı + tutuklama duruşmaları]`
**Birincil venue:**
- Asliye Ceza Mh. (genel)
- Ağır Ceza Mh. (ağırlaştırılmış cezalı)
- Sulh Ceza Hakimliği (soruşturma — tutuklama)
- İcra Ceza Mh. (icra/iflas suçları)
- BAM Ceza Daireleri (istinaf)
- Yargıtay Ceza Daireleri (temyiz)

**Sorumlu ortak:** `[DOLDUR — örn. Kıdemli Ortak C — ceza uzmanlığı]`
**CMK görevli atama gönüllüsü olan avukatlar:** `[DOLDUR — kadrolu liste]`

---

## Kim kullanıyor

**Rol:** [DOLDUR — özellikle baroya kayıtlı + CMK gönüllüsü mü?]
**Asıl avukat irtibatı:** [DOLDUR]

---

## Entegrasyonlar

| Entegrasyon | Durum | Alternatif |
|---|---|---|
| **Yargı MCP — Yargıtay Ceza Daireleri (1-23 ceza)** | ✓ | UYAP |
| **Yargı MCP — AYM bireysel başvuru** | ✓ | AYM sitesi |
| **Mevzuat MCP** (TCK, CMK, KVKK, sektör cezası kanunları) | ✓ | mevzuat.gov.tr |
| **UYAP — ceza dosya** | [DOLDUR — müdafiilik avukatı sıfatıyla] | E-tebligat |
| **Baro CMK Servisi** | [DOLDUR — büro telefon/uygulama] | — |
| **Adli Tıp Kurumu (ATK)** rapor | Manuel | — |

---

## CMK görevli atama yönetimi

Bu plugin'in **ayırt edici** bölümü:

### CMK 5271 m. 150-156 — Müdafi atama

**Atama tipleri:**
1. **Zorunlu müdafi** (m. 150/3 — 18 yaş altı, akıl hastalığı, ceza alt sınırı > 5 yıl, vd.)
2. **İsteğe bağlı atama** (şüpheli/sanık istediği, kendi müdafii yoksa)
3. **Talimat müdafiliği** (başka yer mahkemesi talimatıyla)

**Baro CMK servisi:**
- Görev atama nöbet listesinden — baro CMK biriminin telefonu üzerinden
- Genelde **gece + hafta sonu** çok yoğun
- Atama mesajı sonrası **2 saat içinde teyit + 6 saat içinde karakola/cezaevine ulaşma**

### 48 saat kritik kontrolü (CMK m. 91)

- **Yakalama** → **24 saat içinde** savcılığa sevk (toplu yakalamada 48 saat)
- **Savcılık** → **48 saat içinde** (yakalama dahil) sulh ceza hakimine sevk (tutuklama veya salıverme)
- **Sulh ceza hakimi** → tutuklama veya salıverme kararı (en geç 48. saat doluyor)

⚠️ **Müdafi atama → 48 saat sınırı KRİTİK.** Süreyi geçirirse usul yokluğu gerekçesiyle salıverme.

### CMK ödeme takibi

- Baro CMK servisi atama → görev bittikten sonra **CMK ödeme cetveli** doldur → baroya teslim → 30-60 gün içinde ödeme
- Tarife: Adalet Bakanlığı her yıl yayımlar (genelde AAÜT'nin altında)
- **Vergi:** CMK ödemesi gelir vergisine tabi (matrah avukatın yıllık beyanına gider)

Detay: `references/cmk-gorevli-rehberi.md`

---

## Müvekkil profili

| Müvekkil tipi | Tipik suçlama | Tipik mahkeme |
|---|---|---|
| **CMK görevli (zorunlu müdafi)** | Çeşitli (tipik: yağma, hırsızlık, kasten yaralama, uyuşturucu) | Asliye Ceza / Ağır Ceza |
| Özel müvekkil — ekonomik suç | Dolandırıcılık, güveni kötüye kullanma, vergi (VUK 359) | Asliye Ceza / Ağır Ceza |
| Özel müvekkil — beyaz yaka | Hizmet nedeniyle güveni kötüye kullanma, zimmet, rüşvet | Ağır Ceza |
| **Müdahil vekilliği** (mağdur tarafı) | Yağma, dolandırıcılık, manevi tazminat (paralel hukuk davası) | Ağır/Asliye Ceza + Hukuk Mh. |
| İş kazası ceza | Taksirle yaralama/ölüm (TCK 85, 89) — işveren/işyeri yetkilisi | Asliye Ceza |
| Çevre suçu | Çevreyi kasten kirletme (TCK 181) | Asliye Ceza |
| Bilişim suçu | TCK 244, 245, 245A | Asliye Ceza |
| **Sanık vekilliği — basın suçları** | TCK 125 (hakaret), 134 (özel hayat ihlali) | Asliye Ceza |

---

## Vekalet ücreti modeli — ceza müdafaa

**CMK görevli atama:** Adalet Bakanlığı tarifesi (sabit, müzakere yok)

**Özel müvekkil:**
**Standart yaklaşım:** `[DOLDUR — örn. Aşama bazlı: soruşturma + kovuşturma + istinaf/temyiz; her aşama ayrı sözleşme]`
- **Aşama 1 — Soruşturma:** AAÜT × 1.5-2x, peşin
- **Aşama 2 — Kovuşturma (asliye/ağır ceza):** AAÜT × 2-3x, duruşma başına ek (varsa)
- **Aşama 3 — İstinaf/Temyiz:** AAÜT × 1.5x, peşin
- **Beraat halinde başarı primi:** Av. K. m. 164 sınırı (uyuşmazlığa konu değerin %25'i — ceza davasında "değer" net olmadığından **tazminat/iadeye konu tutar** referans alınır)

⚠️ **Ceza davasında "uyuşmazlığa konu değer"** çoğu zaman net değil. AAÜT × katsayı + müvekkilin maddi durumunun değerlendirmesi.

---

## Eskalasyon ve onay matrisi

| Karar | Onay yetkisi | Not |
|---|---|---|
| CMK görevli kabul/red | Atanan avukat | Reddedilmesi nadir + gerekçeli |
| Özel müvekkil ceza dosyası kabul | **Conflict check + Yönetici Ortak** | Mevzuubahis menfaat çatışması (mağdur müvekkilse?) |
| **Tutuklama itirazı** (sulh ceza hakimi kararına) | Atanan ortak (anında — 7 g süre) | Yönetici Ortak'a bildir |
| Üst yargı yolu (istinaf/temyiz) | **Müvekkil + atanan ortak** | — |
| AYM bireysel başvuru (tutukluluk) | Müvekkil + atanan ortak + Yönetici Ortak | — |
| AİHM başvurusu | Müvekkil + Ortaklar Kurulu | — |
| **Uzlaştırma kabul** (uzlaştırma kapsamına giren suç) | Müvekkil — avukat tavsiyesi | — |
| Müdahil sıfatıyla ek dava (mağdur tarafı) | Mağdur müvekkil + atanan ortak | Paralel hukuk davası kararı |

**Otomatik 🔴 eskalasyon:**
- Müvekkil veya **mağdur PEP** → Yönetici Ortak
- Basına intikal etmiş dosya → Yönetici Ortak + medya stratejisi
- Yargıtay birleştirici kararı son zamanlarda çıkmış konu → strateji revize

---

## Outputs

**Müdafaa hazırlık notu:**
```
AVUKATLIK K. m. 36 – MÜDAFİ ÇALIŞMASI – DAHİLİ VE GİZLİDİR
[Büro] – Matter: [matter-slug]
Müvekkil: [şüpheli/sanık rumuz] – [TC kimlik son 4 rakam — opsiyonel]
Suçlama: [TCK m. X — kısa tanım]
Dosya: [esas/soruşturma no]
Aşama: [Soruşturma / İlk derece / İstinaf / Temyiz / İcra]
Hazırlayan: Claude – avukat incelemesi öncesi
```

**Duruşma savunma taslağı:** "TASLAK – İMZA BEKLİYOR — sözlü duruşmaya uyarlanacak" ekle.

**Mağdur müdahil dilekçesi:** Üst başlık KALDIR; "TASLAK – İMZA BEKLİYOR" ekle.

### Atıf disiplini

- `[Yargı MCP — yargitay — ceza-X-daire — GG.AA.YYYY]`
- `[Yargı MCP — aym-bireysel — GG.AA.YYYY]`
- `[Mevzuat MCP — TCK/CMK m. X — GG.AA.YYYY]`
- `[CMK görevli atama no — Baro — GG.AA.YYYY]`
- `[ATK raporu — rapor no — GG.AA.YYYY]` (Adli Tıp Kurumu)

---

## Karar duruşu — özel guardrails

### Mesleki gizlilik — ceza dosyasında

- **Müdafi-müvekkil görüşmesi gizlidir** (CMK m. 154) — kayıt yasak, dinleme yasak
- Görüşme odası mahremiyetine dikkat (cezaevi/karakol görüşme odası)
- Müvekkilin "suç işledim ama söyleme" itirafı — **mutlak gizlilik**; avukat hakim/savcıya bunu söyleyemez

### Müdafii vs. müdahil ayrımı

Aynı olayda hem sanık hem mağdur müvekkili **EŞZAMANLI** alamayız — net çıkar çatışması, Av. K. m. 38. Her matter intake'inde `/firm-operations:conflict-check` çalıştır.

### "Suç işleniyor" durumu

Müvekkil ileride suç işlemeyi planlıyorsa: **mesleki sır istisnası** (TBB Meslek Kuralları m. 36) — suç önleme amaçlı **mağdurun korunması** için gizliliği kırma yetkisi vardır. Bu nadir durumda **Ortaklar Kurulu + Baro Hukuk Müşavirliği** danışma.

### Tutukluluk süreleri (CMK m. 102)

- **Asliye ceza:** üst sınır 1 yıl (uzatılabilir — toplam 1.5 yıl)
- **Ağır ceza:** üst sınır 2 yıl (uzatılabilir — toplam 3 yıl)
- **Çocuk:** 6 ay (üst sınır)
- Süre uzatma kararları **tutukluluğun devam zorunluluğu** + gerekçeli olmalı

Tutukluluk süreleri dolduğunda **resen salıverme** + adli kontrol.

### Uzlaştırma (CMK m. 253-255)

Bazı suçlarda **uzlaştırma şart** (örn. basit yaralama TCK 86/1, hakaret TCK 125). Uzlaştırma teklif edildiğinde:
- Müvekkile **avantajları + dezavantajları** açıkla
- Uzlaştırma kabul = ceza davası düşer
- Reddederse dava devam, ama "uzlaştırma teklifi reddedildi" karar gerekçesinde yer alır

---

## Shared guardrails

`dispute-litigation.md` ile aynı çerçeve.

**Ceza özel:**
- **CMK m. 130:** Soruşturma dosyası **savcının yetkisi altında** — kovuşturmaya geçinceye kadar müdafii erişim sınırlı (örn. kısıtlama kararı varsa)
- **Müvekkil ifade verirken müdafii hazır olmadıkça** (CMK m. 147/1-h) ifade kullanılamaz — bu kuralı her zaman koru
- **Susma hakkı** (CMK m. 147/1-e) müvekkile hatırlatılır + kayıtlı

---

## Matter workspaces

Cross-matter OFF zorunlu. Konum: `~/.claude/plugins/config/claude-for-legal-law-firm/matters/<müvekkil-slug>__<matter-slug>/`

**Özel:** CMK görevli matter'ları için `matters/cmk-<tarih>__<dosya-no>/` deseni — agregat raporlama (aylık baro CMK ödeme cetveli) için.

---

## Seed davalar

| Dava | Rol | Müvekkil | Suçlama | Aşama | Not |
|---|---|---|---|---|---|
| [DOLDUR] | sanık/mağdur/CMK | | | | |

---

*Re-run interview:* `/criminal-defense:cold-start-interview --redo`
