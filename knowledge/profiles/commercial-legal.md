# Ticari Sözleşmeler – Pratik Profili (Türkiye Overlay)

> Bu dosya `commercial-legal` eklentisinin TR ön-doldurulmuş profilidir.
> Hedef konum: `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`
> `tr-overlay/install.ps1` ile oraya kopyalanır.

---

## Kim olduğumuz

Şirket bilgileri için `~/.claude/plugins/config/claude-for-legal/company-profile.md` dosyasını oku.

**Organizasyonel yapı (KRİTİK):** ArthurLegal Holding'de CLM ve sözleşme yaşam döngüsü işini **Satınalma–Sözleşme Departmanı** yürütür (hukukta değil). Hukuk, Uyum ve Kurumsal Yönetişim Başkanlığı ([CLCO]) **review/onay rolünde** — son hukuki onay ve eskalasyon noktası olarak süreç içine girer.

**Pratik sonuçlar:**
- "Sözleşmeler ekibi" = **Satınalma–Sözleşme** birimi; ~5-10 kişi. Bu ekip register tutar, müzakere koordine eder, taraf koordinasyonunu yapar.
- Hukukta sözleşme review için ayrı ekip/kişi(ler) var (Counsel + Manager seviyesi).
- **Hukukun en çok karşılaştığı sorun:** İş birimi + satınalma müzakereyi bitirdikten sonra "imzaya hazırız, son hukuki onay gerek" diye getiriyorlar — geç müdahale.
- **Renewal/cancel takvimi** Satınalma'nın sorumluluğunda, **ama CLM yok** (kağıt+manuel) → hukukun feedback'i: "yenileme takibi yapısal olarak risk".

**Sözleşmeler ekibi büyüklüğü:** Satınalma–Sözleşme departmanında 5-10 kişi (CLM yürüten). Hukukta sözleşme review için ek küçük ekip.
**Aylık ortalama sözleşme adedi:** Aylık 50-200 sözleşme review ediliyor (her üç iş birimi: rafineri/petrokimya, doğal gaz, terminal/depolama)
**Çoğunlukla:** **KARMA** — hem satıcı hem alıcı:
- *Satıcı tarafta:* [Halka Açık İştirak] petrokimya ürün satışı, [Rafineri Tesisi] akaryakıt teslimatı, [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] doğal gaz tedariki, Terminal A.Ş. liman hizmetleri
- *Alıcı tarafta:* Ham petrol tedariki ([Yurtdışı Ana Şirket] dahil), endüstriyel hizmet, MRO (maintenance/repair/ops), IT/SaaS abonelikleri, danışmanlık, hukuk dış vekil hizmetleri
- *Intra-group:* [Yurtdışı Ana Şirket] ana ortak ile transfer pricing'e tabi işlemler

**CLM (sözleşme yaşam döngüsü sistemi):** **YOK** — Satınalma–Sözleşme departmanı **kağıt + Excel + SharePoint** ile manuel yürütüyor. Yapısal eksiklik: renewal/cancel ihbar pencereleri manuel takvimle takip ediliyor, kaçırma riski yüksek.
**En yakıcı sorun (the thing that hurts):** **YAPTIRIM TARAMASI (sanctions screening).** [Yurtdışı Ana Şirket] ana ortak yapısı + ana ortak ülkesinin yaptırımlı komşu ülkeleri nedeniyle OFAC SDN, CAATSA m.232, AB 833/2014 (Rusya), İran rejimi, BM ve UK OFSI listelerinde counterparty + son intifa hakkı sahibi (UBO) taraması kritik. Hâlihazırda bu kontrol manuel + eksik yapılıyor. Tedarik zincirinde Rusya menşeili komponenler için CBAM ile birlikte ek karmaşıklık geliyor.

**İkincil yakıcı sorunlar:**
- Yenileme tarih takibi (CLM yok) — gaz dağıtım sözleşmeleri çoklu, kaçırma riski
- İş birimi + satınalma legal'ı son anda çağırıyor (müzakere bittikten sonra "imzaya hazırız")
- Intra-group [Yurtdışı Ana Şirket] işlemlerinde transfer pricing belgelenmesi

---

## Kim kullanıyor

**Rol:** [DOLDUR — bkz. company-profile.md]
**Avukat irtibat:** [DOLDUR]

---

## Entegrasyonlar (TR bağlamı)

| Entegrasyon | Durum | Alternatif |
|---|---|---|
| CLM | ✗ **YOK** (Satınalma kağıt + Excel + SharePoint) | Kullanıcı her sözleşmeyi manuel yükler; legal kendi register'ını tutar |
| **KEP (kayıtlı elektronik posta)** | ✓ (birincil e-imza/tebligat — TTK 18/3 zorunlu) | Noter ihtarname |
| DocuSign | [DOLDUR ✓/✗ — uluslararası counterparty için olabilir] | Manuel ıslak imza + tarama |
| Doküman deposu (SharePoint) | ✓ büyük kurum standardı | — |
| Microsoft Teams | ✓ kurumsal standart | E-posta |
| **Mevzuat MCP** | ✓ | — |
| SAP SuccessFactors (İK) | ✓ — çalışan veri kaynağı (employment-legal'a entegre) | — |
| ERP (satınalma sipariş ↔ sözleşme) | [DOLDUR ✓/✗ — SAP ERP muhtemel ama CLM tarafı yok] | Manuel sipariş takip |

---

## Türk hukuku konumu — Playbook

### Genel ilkeler (Türkiye)

- **Sözleşme serbestisi (TBK m. 26):** Genel kural — taraflar serbest. Sınırı: emredici hükümler, kamu düzeni, kişilik hakları, ahlak.
- **Genel işlem koşulları (TBK m. 20-25):** Tek taraflı önceden hazırlanmış koşullar müzakere edilmeden sözleşmeye konuluyorsa "şaşırtıcı" hükümler yazılmamış sayılır. Tüketici ile veya zayıf konumdaki tacirle olan sözleşmelerde önemli.
- **Türk Ticaret Kanunu (6102 TTK) tacir hükümleri:** İki tacir arasında ihtar şartı esnek (m. 18/3), faiz oranı daha yüksek (m. 9 — avans/temerrüt), basiretli iş adamı gibi davranma yükümlülüğü (m. 18/2).
- **Damga vergisi:** Sözleşme bedeli üzerinden binde 9,48 (2026 — güncelle). Çoğu B2B sözleşmesi konusu. KEP/e-imza ile damga doğar; sözleşmenin Türkiye'de düzenlenmesi gerekir. **Her review'da damga maliyeti hesabını dahil et.**

### Limitation of Liability (Sorumluluğun Sınırlandırılması)

**Türk hukukunda emredici sınır (TBK m. 115):**
- **Ağır kusur ve kasıttan sorumluluğu sınırlandıran/kaldıran anlaşmalar BATILIDIR.**
- Hafif ihmal için sınırlama mümkün, fakat kişilik haklarına veya hayata yönelik zararlarda dahi tartışmalı.
- Tüketici sözleşmesinde sınırlama tüketiciye karşı geçersiz (TKHK m. 5).

**Standart konum (satıcı taraf — bizim kâğıt: [Halka Açık İştirak]/[Rafineri Tesisi]/gaz satışları):**
- Direct cap: 12 aylık sözleşme bedeli (FOB/CIF ürün satışlarında); hizmet sözleşmelerinde ödenmiş 12 aylık ücret
- Dolaylı/sonuç zararı: hariç tutulur — *ancak hayat, beden, ağır kusur saklı (TBK 115 emredici)*
- Carveout (cap üstü): Ağır kusur, kasıt, gizlilik ihlali, fikri mülkiyet ihlali, veri ihlali, ürün ayıbı (kanuni garanti), çevre kirlenmesi tazmini (Çevre K. m. 28)
- Enerji satışında özel: Ürün spesifikasyon uymaması durumunda OPTI (offtake price index) düzeltmesi cap altında

**Standart konum (alıcı taraf — onların kâğıdı: ham petrol, hizmet, IT):**
- Vendor cap: 24 ay ücret (kritik tedarikçi); standart hizmette 12 ay
- Vendor consequential carveout: Veri ihlali, IP, gizlilik, ağır kusur — **TBK 115 emredici; sözleşmede de açıkça belirtelim**
- Rafineri/petrokimya duruş süresine sebep olan vendor kusuru — özel tazminat klozu (production loss)
- IT/SaaS'da: veri ihlali için ayrı cap (genelde 2x annual fee)

**Asla kabul etme:**
- "Tüm zararlar dahil sınırsız muafiyet" — TBK 115 nedeniyle zaten geçersiz
- Cap bazı "son 3 aylık ücret" gibi vendor-favored tanımlar
- Rafineri kompleksinde çevre kirlenmesi tazminini sınırlayan vendor klozları (2872 ÇK + 6098 TBK)
- ISG vakası bedensel zararı sınırlayan klozlar (TBK 115 + 6331 ISG)

### Tazminat / İndemnification

- Türk hukukunda "indemnify" doğrudan kavram değil; **tazminat taahhüdü + garanti yükümlülüğü** karması olarak yorumlanır.
- Defense yükümlülüğü ayrı bir taahhüt (yargılama harcı + avukat ücreti dahil) — açıkça yazılmalı.
- IP infringement claim: vendor'dan tam tazminat + ürün değişikliği / lisans alma / iade hakkı klasik üçlü.

### Veri Koruma (KVKK + GDPR)

- **Standart konum:** KVKK'ya uygun veri işleyen sözleşmesi (Türkiye'de işlenen veri için) + GDPR DPA (AB'ye veri akışı varsa)
- **Zorunlu:** İşleyen ile ayrı veri işleme sözleşmesi (KVKK m. 12), VERBİS kayıt teyidi, yurt dışı aktarım için açık rıza VEYA yeterlilik kararı VEYA standart sözleşme.
- 2024-2025 değişiklik (m.9): Yurt dışı aktarım rejimi ESCC + BCR + onaylı sertifika modeli ile gevşedi. Yeni rejim için bkz. `references/kvkk-yurtdisi-aktarim-2024.md`.

### Süre ve Fesih

- **Belirli süreli sözleşme (TBK m. 327):** Otomatik sona erer; haklı sebepsiz fesih varsa tazminat.
- **Belirsiz süreli (TBK m. 328):** Her zaman makul süreli ihbar ile fesih hakkı.
- **Otomatik yenileme:** Türk hukukunda geçerli ama tüketici sözleşmesinde "açık irade" şartı katı.
- **Haklı sebeple fesih (TBK m. 117):** Sözleşmesel tanımdan bağımsız olarak emredici — sözleşmeyle elden alınamaz.

### Geçerli hukuk ve yargı yeri

- **Tercih:** Türk hukuku, İstanbul ATM (Anadolu / Çağlayan) veya [DOLDUR — şirket merkezi mahkemeleri]
- **Tahkim varsa:** ISTAC (İstanbul Tahkim Merkezi) – TL anlaşmazlıkları; ICC – uluslararası anlaşmazlıklar.
- **Kabul edilebilir:** İngiliz hukuku + Londra (LCIA), İsviçre hukuku + ICC Cenevre.
- **Eskalasyon:** New York / Delaware – sadece counterparty ABD ana şirket ise.
- **Asla:** Counterparty'nin kendi yerel yargısı + kendi hukuku (asimetrik).

### "The one thing" (her review'da ilk bakılan) — Şirket için **YAPTIRIM TARAMASI** dominant

Bu profil için kullanıcı yaptırım taramasını birincil yakıcı sorun olarak işaretledi. Her review'da **sırayla**:

**1. Yaptırım taraması (sanctions screening) — KRİTİK BİRİNCİ ADIM:**
- Counterparty + son intifa hakkı sahibi (UBO) + bağlı tarafları aşağıdaki listelere karşı tara:
  - **OFAC SDN List + Sectoral Sanctions Identification (SSI) + CAATSA m.232** (Rusya enerji sektörü ile işbirliği)
  - **AB Council Regulation 269/2014** (Ukrayna kişi/işletme), **833/2014** (Rusya sektör), **267/2012** (İran), 1183/2005 (DRC), vd.
  - **BM Güvenlik Konseyi yaptırımları**
  - **UK OFSI Consolidated List**
  - **TR 7262 sayılı Kanun** (kitle imha silahları yayılmasının finansmanı) + UNSCR resepsiyonu
- Ek kontrol: Tedarik zinciri — Rusya menşeili komponen var mı? AB CBAM ile birlikte raporlama yükümlülüğü doğar mı?
- **Karşı taraf veya UBO listede ✗ → DURDUR. Üst yönetim bilgilendir, devam etme. Counsel/Başkan onayı şart.**
- Liste **belirsizse** (ad benzerliği var ama UBO net değil) → KYC dokümanı talep, ek dilijans, "yeşil ışık" yazılı gelene kadar imza yok.

**2. Damga vergisi:** Sözleşme tutarı × 0,00948 = damga. Kim ödeyecek? "Eşit paylaşır" → standart kabul. Vendor üstlenirse → iyi. Tek başına biz üstlenirsek → tutara göre eskalasyon (5M TL üstü Counsel, üstü Direktör).

**3. [Halka Açık İştirak] halka açık kontrol:** Sözleşmenin tarafı veya konusu [Halka Açık İştirak] ise → içsel bilgi listesi + KAP açıklama gereksinimi tetiklenir mi? (SPK Tebliğ VI-104.1 + II-15.1)

---

## Eskalasyon

Bkz. company-profile.md anahtar kişiler tablosu. Bu eklentiye özel:

| Onaylayan | Eşik | Eskalasyon | Yöntem |
|---|---|---|---|
| Satınalma–Sözleşme Yöneticisi | 5M TL'ye kadar standart (sözleşme akış sahibi) | Hukuk Counsel (review) | Teams/E-posta |
| Hukuk Counsel | 10M TL'ye kadar hukuki onay | Hukuk Direktörü | E-posta |
| Hukuk Direktörü | [DOLDUR — şirket politikası, kamuya açık değil] | Hukuk, Uyum ve Kurumsal Yönetişim Başkanı ([CLCO]) | E-posta |
| Başkan ([CLCO]) | Direktör eşiği üstü veya stratejik / kırmızı çizgi | CEO ([CEO]) | Yönetim toplantısı |

*Not: Tutar eşikleri Şirket iç politikasının gerçek değerleri ile teyit edilmeli — yukarıdaki rakamlar kullanıcının belirttiği ön kabuldür. **Direktör seviyesi eşik [DOLDUR] olarak kalıyor.***

**Tutardan bağımsız otomatik eskalasyon:**
- **OFAC / AB / BM / UK / TR yaptırım listesi eşleşmesi** (kesin durdurma)
- **[Halka Açık İştirak] ile ilgili** sözleşmeler (halka açık şirket — içsel bilgi / KAP riski)
- **Intra-group [Yurtdışı Ana Şirket] işlemleri** (transfer pricing + Maliye + yatırım teşvik)
- TBK 115 ihlali görüldüğünde (sorumsuzluk şartı geçersiz)
- KVKK yurt dışı aktarım yeterlilik kararı dışı bir ülke
- Rafineri/petrokimya kompleksini etkileyecek ÇED + ISG + Çevre vendor riski
- EPDK lisansı kapsamında değişiklik gerektiren sözleşmeler
- Yabancı mahkeme + yabancı hukuk asimetrik durum
- Tahkim klozu Türkçe değil ve Türk tarafı için zor erişim
- **[Boru Hattı Projesi] / hükümetlerarası anlaşma** alanına giren işlemler

---

## Ev tarzı (House style)

**Redline tonu:** Direkt, kısa açıklamalı. "Önerimiz:" / "Burada riski şuna düşürüyoruz:" şeklinde rationale ekle.

**Paydaş özeti:** İş birimi için 1 sayfayı geçmeyen; yeşil/sarı/kırmızı bayraklı; "imzalanabilir / pazarlık / imzalanamaz" sonucu.

**Çalışma çıktısı nereye:** [DOLDUR — örn. Drive/Legal/Contracts/<yıl>/<counterparty>]

**Yenileme alarmı:** [DOLDUR — Slack #legal-renewals veya [hukuk@şirket-email]]

---

## Çıktı

### Çalışma ürünü başlığı (Türkçe)

```
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU
Hazırlayan: Claude (Hukuk Asistanı) – İnsan avukat incelemesi öncesi taslak
Tarih: [GG.AA.YYYY]
```

Dış paydaş gidecek belgelerde:
```
TASLAK – İNCELEME İÇİNDİR – HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN PAYLAŞMAYINIZ
```

### Reviewer note (inceleyen notu) standardı

```markdown
⚠️ İnceleyen notu
- Kaynaklar: [Mevzuat MCP ✓ / değil — model bilgisi, doğrulayın]
- Okudum: [örn. "1-25 sayfa, toplam 40"]
- İnceleyen kararı bekleyen ([review] etiketli): N adet
- Güncellik: [Mevzuat MCP'de [konu] son arandı: GG.AA.YYYY]
- Bağlayıcı karar öncesi: [1-2 maddelik somut adım]
```

---

## Diğer guardrails

Orijinal İngilizce CLAUDE.md template'indeki tüm guardrails (no silent supplement, citation hygiene, severity floor, jurisdiction recognition, retrieved content trust, large input/output rules) **aynen geçerlidir** — bu Türk overlay onları override etmez, sadece TR bağlamına özelleştirir.

Türkiye için özel ek kural:
- **Karar / kanun atıflarında çift kaynak:** Yargıtay/Danıştay/AYM kararları için **Yargı MCP** kullan, kanun metinleri için **Mevzuat MCP**. Daire + tarih + esas/karar (yargı) ve Resmi Gazete sayı + tarih (mevzuat) zorunlu. `[Mevzuat MCP]` / `[Yargı MCP — kurum]` / `[Resmi Gazete]` etiketi olmayan atıflar `[model bilgisi — doğrulayın]`.
- **Dil:** Tüm çıktılar Türkçe (counterparty yabancı ise hem Türkçe hem İngilizce versiyonu üret).

---

*Re-run interview:* `/commercial-legal:cold-start-interview --redo`
