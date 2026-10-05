# Regülasyon & Uyum – Pratik Profili (Türkiye Overlay)

> Hedef: `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`

---

## Kim olduğumuz

Bkz. `company-profile.md`. Bu eklentiye özel — ArthurLegal Holding'nin tabi olduğu düzenleyiciler **çok geniş çünkü 3 iş birimi + 17 iştirak**:

**Birincil (her hafta takip edilmesi gereken):**
- ✅ **EPDK** — [Halka Açık İştirak], [Rafineri Tesisi], Enerji Ticaret A.Ş., Depolama A.Ş., **[Elektrik İştiraki] (elektrik üretim lisansı — [DOLDUR — kapasite], doğal gaz yakıtlı)**. *[Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] dağıtım lisansları devir sürecinde — devralan şirkete geçişe kadar EPDK bildirim takibi sürer.*
- ✅ **SPK + KAP** — [Halka Açık İştirak] halka açık (BIST: [BIST-KOD]); özel durum açıklamaları, içsel bilgi
- ✅ **Rekabet Kurulu** — [Üretim Sahası] ÖEB dikey entegrasyon; doğal gaz pazar payı
- ✅ **Çevre, Şehircilik ve İklim Değişikliği Bakanlığı** — [Üretim Sahası] rafineri/petrokimya ÇED, emisyon, atık, sera gazı
- ✅ **KVKK Kurulu** — milyonlarca ilgili kişi
- ✅ **ÇSGB** — yabancı çalışan izinleri (AZ kökenli yönetim) + 6331 ISG denetim
- ✅ **Hazine ve Maliye / MASAK** — uluslararası enerji ticareti, transfer pricing

**İkincil (periyodik):**
- ✅ **KGK (Kamu Gözetimi)** — [Halka Açık İştirak] bağımsız denetim (TFRS)
- ✅ **BTK** — [Telekom A] (telekom) + Fiber A.Ş.
- ✅ **Sanayi ve Teknoloji Bakanlığı** — [Üretim Sahası] Özel Endüstri Bölgesi (4737)
- ✅ **TÜRKPATENT** — Şirket/[Halka Açık İştirak]/[Rafineri Tesisi] marka ve patent portföyü
- ✅ **Türkiye Petrolleri (TPAO) + BOTAŞ** — sektör koordinasyonu
- [ ] BDDK — yalnızca ArthurLegal Holding Finance operations varsa
- [ ] RTÜK — uygulamada yok

**Uluslararası:**
- ✅ **OFAC** (ABD Hazine), **AB Council** (yaptırım rejimleri), **UK OFSI**
- ✅ **[Yurtdışı Ana Şirket]** — ana ortak corporate governance + Yurtdışı ana ortak ülke mevzuatı bilgilendirmesi

**Politika kütüphanesi konumu:** **SharePoint + Intranet portal** — Politikalar SharePoint "Hukuk ve Uyum" sayfasında merkezi olarak tutulur; çalışanlara intranet portalı üzerinden duyurulur. Versiyon kontrolü + onay iş akışı SharePoint üzerinden.

---

## Türkiye'ye özgü regülatif manzara

### Birincil kaynaklar

- **Resmi Gazete:** https://www.resmigazete.gov.tr — günlük; mükerrer + yardımcı + ana
- **Mevzuat Bilgi Sistemi:** https://www.mevzuat.gov.tr — Mevzuat MCP buradan çekiyor
- **CB Kararnameleri ve Genelgeleri:** Mevzuat MCP `search_cbk`, `search_cbgenelge`
- **Kurum kararları:** EPDK, BDDK, SPK gibi kurumlar kararlarını kendi sitelerinde yayınlar — Mevzuat MCP'de tüm kurum kararları olmayabilir.

### Kritik ritimler

- **Resmi Gazete günlük tarama:** sabah 09:30'da yayınlanır; mevzuat değişiklikleri burada
- **Cumhurbaşkanlığı kararnameleri:** Sayı + tarih takip kritik (eski "torba yasa" yerine yeni kararname rejimi)
- **Sektör düzenleyici tebliğleri:** Aylık veya çeyreklik toplantı kararları + yayın

---

## Sık kullanılan iş akışları

### 1. Reg-feed digest (haftalık özet)

**İşleyiş:**
1. Pazartesi 08:00'de geçen haftanın Resmi Gazetelerini Mevzuat MCP üzerinden tara
2. İlgili kurum kararlarını (EPDK, BDDK vs.) tara — bunlar genelde kurum sitesinde ayrı
3. Politika kütüphanesi içeriklerine karşı diff
4. Çıktı şablonu: `references/reg-feed-haftalik-sablon.md`

### 2. Policy drift detection

İç politika dokümanı vs yürürlükteki mevzuat farkı:
- Politika atıflarındaki kanun maddelerini Mevzuat MCP'den teyit
- Numerik eşikler (TL tutarları, oran %) güncel mi
- Tebliğ değişikliği olmuş mu

### 3. Comment / görüş bildirimi

- T.C. Cumhurbaşkanlığı Strateji ve Bütçe Başkanlığı — Düzenleyici Etki Analizi taslakları
- Kurum görüş istemeleri (kamuoyu duyurusu)
- Süre: tipik 15-30 gün
- Görüş yapısı: konu - mevzuat referansı - sektör etkisi - öneri

### 4. Gap analizi

Yeni regülasyon → şirket içi politika güncellemesi → eğitim → denetim

---

## Çıktı standardı

Bkz. `commercial-legal.md`. Regülasyon özel:

- **Her digest'te "etki sınıflaması":**
  - 🔴 Zorunlu uyum (ceza riski / lisans iptali)
  - 🟠 Süreçle uyum (politika güncellemesi gerekli)
  - 🟡 İzleme (sektör yorumu yapılacak)
  - 🟢 Bilgilendirme
- **Sürelere otomatik flagging:** [Mevzuat MCP — yürürlük tarihi GG.AA.YYYY]
- Mevzuat MCP atıfında her zaman **kanun adı + madde no + RG sayı/tarih**

---

## Eskalasyon

- 🔴 Yeni cezai hüküm getiren mevzuat, **EPDK lisans iptali riski**, **OFAC/AB yeni yaptırım kararı**, [Halka Açık İştirak]'i etkileyen SPK değişikliği, **karbon vergisi / ETS mevzuatı** → Hukuk Başkanı ([CLCO]) + CEO ([CEO])
- 🟠 Politika değiştirilmesi gereken regülasyon, ÇED Yönetmeliği değişikliği, KVKK Kurul tebliğ, yeni AB Green Deal/CBAM (sınırda karbon ayarlama) düzenlemesi → Counsel + ilgili iş birimi başkanı ([Rafineri/Petrokimya Birim Başkanı]/[Doğal Gaz/Enerji Birim Başkanı])
- 🟡 Bilgilendirme amaçlı değişiklik, sektörel görüş çağrısı → İlgili iş birimine forward

**Şirket'e özel takip listesi (her Pazartesi):**
- **EPDK Kurul kararları** (Petrol Piyasası + Doğal Gaz + Elektrik) — kurum sitesi + **Yargı MCP `search_danistay_decisions` (13. Daire)** yargısal temyiz takibi
- **[Halka Açık İştirak] KAP yayınları** — kap.org.tr (WebFetch + `kap-esirket-webfetch-rehberi.md`)
- **Rekabet Kurulu kararları** — **Yargı MCP `search_rekabet_decisions`** + kurum sitesi
- **KVKK Kurul kararları** — **Yargı MCP `search_kvkk_decisions`** (emsal idari para cezaları)
- **BDDK + SPK + GİB kararları** — **Yargı MCP `search_bddk_decisions`, GİB özelgeleri**
- **AB CBAM** (Carbon Border Adjustment Mechanism) — özellikle petrokimya ihracatı için kritik
- **AB Yeşil Mutabakat** + **TR İklim Kanunu** taslağı (TBMM süreçte)
- **OFAC SDN ve Sectoral Sanctions** güncellemeleri — OpenSanctions API (aktif, 13.05.2026'dan beri) + manuel yedek
- **[Üretim Sahası] ÖEB** + Endüstri Bölgeleri Yönetmeliği güncellemeleri
