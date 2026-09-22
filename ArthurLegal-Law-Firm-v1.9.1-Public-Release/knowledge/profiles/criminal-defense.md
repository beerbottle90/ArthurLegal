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
| **ArthurLegal MCP (`tr_`) — Yargıtay Ceza Daireleri (1-23 ceza)** | ✓ | UYAP |
| **ArthurLegal MCP (`tr_`) — AYM bireysel başvuru** | ✓ | AYM sitesi |
| **ArthurLegal MCP (`tr_`)** (TCK, CMK, KVKK, sektör cezası kanunları) | ✓ | mevzuat.gov.tr |
| **UYAP — ceza dosya** | [DOLDUR — müdafiilik avukatı sıfatıyla] | E-tebligat |
| **Baro CMK Servisi** | [DOLDUR — büro telefon/uygulama] | — |
| **Adli Tıp Kurumu (ATK)** rapor | Manuel | — |

---

## CMK görevli atama yönetimi

Bu plugin'in **ayırt edici** bölümü:

### CMK 5271 m. 150-156 — Müdafi atama

**Atama tipleri:**
1. **Zorunlu müdafi** (m. 150/2 — çocuk, kendisini savunamayacak derecede malul, sağır ve dilsiz; m. 150/3 — alt sınırı 5 yıldan fazla hapis gerektiren suç; tutuklama istemi — m. 101/3)
2. **İsteğe bağlı atama** (şüpheli/sanık istediği, kendi müdafii yoksa)
3. **Talimat müdafiliği** (başka yer mahkemesi talimatıyla)

**Baro CMK servisi:**
- Görev atama nöbet listesinden — baro CMK biriminin telefonu üzerinden
- Genelde **gece + hafta sonu** çok yoğun
- Atama mesajı sonrası **2 saat içinde teyit + 6 saat içinde karakola/cezaevine ulaşma**

### Gözaltı süresi kritik kontrolü (CMK m. 91 — kural 24 saat; toplu suçta en çok 4 gün)

- **Yakalama** → gözaltı süresi yakalamadan itibaren **24 saat** (zorunlu yol süresi hariç, o da en çok 12 saat — m. 91/1); toplu suçlarda C. savcısı her defasında 1 günü geçmemek üzere **3 gün** uzatabilir (m. 91/3) → en çok 4 gün
- **Süre sonunda** → bırakılmayan şüpheli sulh ceza hâkimi önüne çıkarılıp sorguya çekilir (m. 91/7) (tutuklama veya salıverme); suçüstü kolluk gözaltısında en geç 48 saat / toplu suçta 4 gün (m. 91/4; AY m. 19)
- **Sulh ceza hakimi** → tutuklama veya salıverme kararı (şüpheli gözaltı süresi — m. 91/1, 91/3 — sonunda hâkim önüne çıkarılmış olmalı)

⚠️ **Müdafi atama → gözaltı süresi (m. 91) KRİTİK.** Süre aşılırsa gözaltı hukuka aykırıdır: serbest bırakılma için sulh ceza hâkimine başvuru (m. 91/5); kanuni gözaltı süresinde hâkim önüne çıkarılmama tazminat sebebidir (m. 141/1-b).

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
| **Tutuklama itirazı** (sulh ceza hakimi kararına) | Atanan ortak (anında — iki hafta süre, CMK m. 268/1) | Yönetici Ortak'a bildir |
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
Müvekkil: [şüpheli/sanık takma adı] – [TC kimlik son 4 rakam — opsiyonel]
Suçlama: [TCK m. X — kısa tanım]
Dosya: [esas/soruşturma no]
Aşama: [Soruşturma / İlk derece / İstinaf / Temyiz / İcra]
Hazırlayan: Claude – avukat incelemesi öncesi
```

**Duruşma savunma taslağı:** "TASLAK – İMZA BEKLİYOR — sözlü duruşmaya uyarlanacak" ekle.

**Mağdur müdahil dilekçesi:** Üst başlık KALDIR; "TASLAK – İMZA BEKLİYOR" ekle.

### Atıf disiplini

- `[ArthurLegal TR — yargitay — ceza-X-daire — GG.AA.YYYY]`
- `[ArthurLegal TR — aym-bireysel — GG.AA.YYYY]`
- `[ArthurLegal TR — TCK/CMK m. X — GG.AA.YYYY]`
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
- **Ağır ceza:** üst sınır 2 yıl (uzatma toplam en çok 3 yıl → azami 5 yıl; TCK 2. Kitap 4. Kısım 4-7. Bölüm ve TMK kapsamı suçlarda uzatma en çok 5 yıl → azami 7 yıl — m. 102/2)
- **Çocuk:** fiil tarihinde 15 yaşını doldurmamışsa süreler yarı, 18 yaşını doldurmamışsa dörtte üç oranında uygulanır (m. 102/5)
- Süre uzatma kararları **tutukluluğun devam zorunluluğu** + gerekçeli olmalı

Tutukluluk süreleri dolduğunda **resen salıverme** + adli kontrol.

### Uzlaştırma (CMK m. 253-255)

Bazı suçlarda **uzlaştırma şart** (örn. kasten yaralama TCK 86/1, taksirle yaralama TCK 89, tehdit TCK 106/1 — CMK m. 253/1). **Hakaret (TCK 125) şikâyete bağlı olsa da uzlaştırma kapsamı dışındadır** (CMK m. 253/3; 7531 ve 7571 s.K.). Uzlaştırma teklif edildiğinde:
- Müvekkile **avantajları + dezavantajları** açıkla
- Uzlaşma + edimin def'aten ifası = dava düşer (kovuşturma, CMK m. 254/2) / KYOK (soruşturma, m. 253/19); edim ileri tarihli/taksitli ise durma kararı (m. 254/2, 7531 s.K.) veya kamu davasının açılmasının ertelenmesi (m. 253/19)
- Reddederse dava devam, ama "uzlaştırma teklifi reddedildi" karar gerekçesinde yer alır

---

## Shared guardrails

`dispute-litigation.md` ile aynı çerçeve.

**Ceza özel:**
- **CMK m. 153:** Müdafi soruşturma evresinde dosya içeriğini inceleyip belge örneği alabilir (m. 153/1); bu yetki yalnız m. 153/2'de sayılan suçlarda, soruşturmanın amacını tehlikeye düşürebilecekse C. savcısının istemi üzerine **hâkim kararıyla** kısıtlanabilir; ifade tutanakları ve bilirkişi raporları kısıtlanamaz (m. 153/3); iddianamenin kabulünden itibaren tam erişim (m. 153/4)
- **Müdafi hazır bulunmaksızın kollukça alınan ifade**, hâkim veya mahkeme huzurunda doğrulanmadıkça hükme esas alınamaz (CMK m. 148/4) — bu kuralı her zaman koru
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
