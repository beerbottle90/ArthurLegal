# energy-finance - Skill Referans Kitapçığı

> Alan: Enerji M&A, proje finansmanı, JV, LNG offtake, enerji altyapısı danışmanlığı
> Toplam skill: 5
> Kullanım: /{plugin}:{skill-adı} komutunu yaz, aşağıdaki ilgili bölümü uygula.

## İçindekiler

- /energy-finance:cold-start-interview
- /energy-finance:jv-agreement-review
- /energy-finance:lng-offtake-review
- /energy-finance:ma-diligence-energy
- /energy-finance:project-finance-review

---

## /energy-finance:cold-start-interview

---
name: cold-start-interview
description: >
  Energy Finance & M&A plugin'ini yapılandır. Aktif işlem portföyü, dış vekil paneli,
  onay matrisi ve proje finansmanı modeli sorgulanır. 5 dakika.
user-invocable: true
---

# Cold-Start Interview — Energy Finance & M&A Practice

## Amaç

Diğer skill'ler bu profil olmadan körce çalışır. Yeni kurulumda çalıştır.

## Hızlı mod (5 soru)

1. **Aktif işlem türleri:** M&A devralma / proje finansmanı / JV kurma / LNG offtake / karma
2. **Tipik işlem büyüklüğü:** <50M USD / 50-500M / >500M
3. **Dış vekil modeli:** Global büro (Clifford Chance vb.) / Türk büro / karma
4. **Yönetim dili:** İngilizce ağırlıklı (uluslararası karşı taraf) / Türkçe ağırlıklı
5. **VDR platformu:** Datasite / Intralinks / SharePoint / başka

## Tam mod (ek sorular)

### Portföy
- Aktif M&A dosyası sayısı ve aşamaları
- Aktif proje finansmanı dosyaları (pre-financial close / construction / refinancing)
- Aktif JV müzakereleri
- LNG offtake portföyü (mevcut + müzakere halinde)

### Dış vekil ve danışman
- Finansman hukuku ana büro + yerel ofis bağlantısı
- Vergi danışmanı (TP + transfer vergisi)
- Teknik danışman (lender's engineer, owner's engineer)
- Sigorta danışmanı
- VDR yöneticisi

### Onay ve eskalasyon
- Hangi tutarda Yönetici Ortak devreye giriyor?
- SPK/EPDK bildirim tetikleyici eşiği (müvekkil halka açıksa)
- Kamu açıklaması tetikleyici (varsa)

## Çıktı

```markdown
## ✓ Energy Finance profile dolduruldu

**Portföy:** [özet]
**Dış vekil:** [özet]
**Onay matrisi:** [özet]

**Önerilen ilk skill:**
- /energy-finance:ma-diligence-energy — aktif devralma varsa
- /energy-finance:project-finance-review — finansman kapatma yakınsa
- /energy-finance:jv-agreement-review — JV müzakere aşamasındaysa
- /energy-finance:lng-offtake-review — LNG sözleşmesi inceleme gerekiyorsa
```

---

## /energy-finance:jv-agreement-review

---
name: jv-agreement-review
description: >
  Enerji sektörü ortak girişim (JV) ve hissedar sözleşmelerini inceler.
  Yönetim yapısı, kilitlenme mekanizmaları, çıkış hakları, rekabet yasağı,
  EPDK lisans uyumu ve çok taraflı/uluslararası JV özel dikkat noktaları.
argument-hint: "[JVA / SHA / konsorsiyum sözleşmesi dosyası]"
---

# /jv-agreement-review — JV & Hissedar Sözleşmesi İncelemesi

## Adım 1 — Yapı haritası

| Unsur | Değer |
|---|---|
| JV türü | SPV kurulumu / Var olan şirkete katılım / Konsorsiyum |
| Taraflar + hisse oranları | [Müvekkil]: % / Karşı taraf: % |
| Governing law | [belirle] |
| Tahkim | |
| JV amacı ve süresi | |
| Karşı taraf ülkesi | [belirle — yabancı ortak varsa hukuk sistemi notu] |

## Adım 2 — Yönetim yapısı & kilit karar mekanizmaları

- **Board kompozisyonu:** [Müvekkil] atama hakkı, veto hakları
- **Süper çoğunluk kararlar:** neler var, eşik nedir?
- **Deadlock mekanizması:** Russian roulette / Texas shoot-out / mediasyon / fesih
- **CEO/CFO atama:** [Müvekkil] belirliyor mu, müşterek mi?
- **Operasyonel kararlar:** günlük işletme, capex eşiği, borçlanma onay

## Adım 3 — Çıkış hakları ve transfer kısıtlamaları

- **Tag-along / drag-along:** şartlar, fiyat hesabı
- **Ön alım hakkı (right of first refusal):** süre, şekil
- **Kilit-up (lock-up):** süre, istisnalar
- **Change of control:** JVA fesih tetikler mi?
- **Put/call opsiyonları:** tetikleyiciler (performance, EPDK lisans kaybı, deadlock)
- **Çıkış valuation:** EBITDA multiple / DCF / third party appraisal

## Adım 4 — Rekabet yasağı & münhasırlık

- Rekabet yasağı süresi, coğrafi kapsamı — 4054 sayılı RKHK m.4 sınırı aşıyor mu?
- AB Rekabet Tüzüğü (ECMR) — AB cirosu varsa Komisyon bildirimi tetiklenir mi?
- Müvekkilin mevcut enerji portföyü ile örtüşme riski?
- Münhasır teknoloji / know-how lisansı var mı?

## Adım 5 — EPDK & düzenleyici uyum

- JV yapısının EPDK lisans şartlarını etkileyip etkilemediği
- Çoklu lisans sahibi JV'lerde konsolidasyon ve pazar payı bildirimi
- Müvekkil halka açıksa: önemli işlem bildirimi eşiği (SPK/KAP)

## Adım 6 — İlişkili taraf & uluslararası ortak özel dikkat

Karşı taraf ilişkili kuruluş veya yabancı ortak ise:
- Transfer fiyatlandırması (TP) riski — KVK m.13
- Yaptırım riski (OFAC/AB) — özellikle CIS, İran, Rusya bağlantılı taraf varsa
- Yabancı ortağın kurumsal yönetim gereksinimleri
- Döviz kontrol kuralları (ilgili ülke mevzuatı)

## Findings özeti

| # | Kloz | Severity | Not |
|---|---|---|---|
| | | 🔴/🟠/🟡/🟢 | |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# JV & Hissedar Sözleşmesi İncelemesi — [JV adı / tarih]

## ⚠️ Reviewer note

## Bottom line

## Yapı haritası

## Yönetim & karar mekanizmaları

## Çıkış hakları

## Rekabet & düzenleyici

## İlişkili taraf notları (varsa)

## Findings

## Önerilen kloz değişiklikleri
```

---

## /energy-finance:lng-offtake-review

---
name: lng-offtake-review
description: >
  LNG ve uzun vadeli enerji tedarik sözleşmelerini inceler. Take-or-pay yükümlülüğü,
  force majeure, price review, destination klozu, sanction compliance ve Japon/Koreli
  alıcı özel dikkat noktaları.
argument-hint: "[LNG SPA | gas supply agreement | offtake agreement]"
---

# /lng-offtake-review — LNG & Uzun Vadeli Enerji Tedarik Sözleşmesi

## Adım 1 — Sözleşme yapısı tespiti

| Unsur | Değer |
|---|---|
| Sözleşme türü | FOB / DES / DAP / EXW |
| [Müvekkil] tarafı | Alıcı (buyer) / Satıcı (seller) |
| Karşı taraf | [örn. Mitsui, JERA, Shell, BP] |
| Sözleşme süresi | [yıl] |
| Hacim (yıllık, MTPA veya MMBtu) | |
| Governing law + tahkim | |
| Referans fiyat | JKM / TTF / Henry Hub / Brent-linked / sabit |

## Adım 2 — Take-or-pay analizi (KRİTİK)

- **Yıllık kontrat miktarı (ACQ):** [MTPA]
- **Minimum take yükümlülüğü:** % ACQ — ceza = difference × fiyat?
- **Make-up hakkı:** var mı, kullanım süresi?
- **Carry-forward / carry-back:** kaç yıl?
- **Force majeure istisnaları:** take-or-pay'i askıya alıyor mu?
- **Downward quantity tolerance (DQT):** [Müvekkil] satıcıysa, teslimat esnekliği
- **Upward quantity tolerance (UQT):** alıcı fazla alabilir mi?

## Adım 3 — Fiyat formülü ve price review

- **Fiyat formülü:** [P = a×JKM + b×TTF + c gibi]
- **Fiyat revizyonu:** kaç yılda bir, mekanizma (arbitration / expert / karşılıklı anlaşma)
- **Cap / floor:** var mı?
- **Döviz:** USD / EUR — kur riski müvekkilde mi?
- **Damga vergisi:** çok yıllı yüksek tutarlı sözleşme → DVK hesabı gerekli (rehber: `references/damga-vergisi-rehberi.md`)

## Adım 4 — Force majeure ve hardship

- FM tanımı kapsamı: doğal afet / siyasi / pandemi / siber
- **Yaptırım (sanctions) FM:** OFAC/AB/BM yaptırım listesine giriş FM sayılıyor mu?
- **İlişkili taraf riski:** Rusya veya yaptırım altındaki ülke bağlantılı FM senaryoları
- Hardship klozu ayrı mı? Hükümler farklı mı?
- FM ihbar süresi ve belgeleme yükümlülüğü

## Adım 5 — Destination kloz & diversion

- Destination klozu var mı? (yeniden satış / diversion yasağı)
- Japon/Koreli alıcılar ile tipik katı destination → Avrupa piyasasına diversion mümkün mü?
- Avrupa hukuku açısından destination klozu geçerliliği — AB Rekabet (TFEU m.102)

## Adım 6 — Sanction compliance

1. OpenSanctions: karşı taraf tara
2. CAATSA m.232: Rusya kaynaklı LNG mı? (Yamal LNG gibi)
3. OFAC SDGT: transit ülkeler (Türkiye Boğazları, Hürmüz)
4. AB 833/2014: Rusya LNG kısıtlamaları ve istisnaları
5. Sözleşmedeki sanction clause: tek taraflı fesih hakkı var mı?
6. Escrow / payment restriction: yaptırım ülkesine ödeme kanalı

## Adım 7 — Japon alıcı özel notlar (MITSUI/JERA/JAPEX)

- **FEFTA bildirimi:** Japon tarafın yapacağı yabancı yatırım bildirimi
- **METI onayı:** enerji güvenliği kapsamında METI'nin bireysel onayı gerekebilir
- **Japon şirket hukuku (会社法):** board karar mekanizması — JLT: `japan-legislation-rehberi.md`
- **Arbitration:** Tokyo / Singapore / Londra — ICC veya JIAC

## Findings

| # | Kloz | Severity | Not |
|---|---|---|---|
| | Take-or-pay | 🔴/🟠/🟡/🟢 | |
| | Force majeure | | |
| | Sanctions | | |
| | Price review | | |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# LNG Offtake İncelemesi — [Sözleşme / Karşı taraf / Tarih]

## ⚠️ Reviewer note

## Bottom line

## Yapı özeti (taraf, hacim, süre, fiyat)

## Take-or-pay analizi

## Fiyat formülü & review mekanizması

## Force majeure & sanctions klozu

## Destination & diversion

## İlişkili taraf / özel alıcı notları

## Findings

## Önerilen kloz değişiklikleri / redline
```

---

## /energy-finance:ma-diligence-energy

---
name: ma-diligence-energy
description: >
  Enerji sektörü M&A durum tespiti — EPDK lisans, ÇED, yaptırım, vergi borcu,
  iş güvenliği sicil, rekabet eşiği ve SPK bildirim kontrolü içerir.
argument-hint: "[VDR index | due diligence request list | target company profile]"
---

# /ma-diligence-energy — Enerji M&A Due Diligence

## Adım 0 — Hedef şirket profili

| Unsur | Değer |
|---|---|
| Hedef şirket adı + tüzel kişilik | |
| Varlık türü | Elektrik üretim / doğal gaz / rafineri / terminal / karma |
| EPDK lisans türü | Üretim / Dağıtım / İletim / Depolama / İhracat-İthalat |
| Kapasite (MW / m³/yıl) | |
| Halka açık mı? (BIST) | |
| Tahmini işlem büyüklüğü (USD) | |

## Adım 1 — Düzenleyici & lisans tarama (KRİTİK)

**EPDK:**
- Lisans geçerliliği + süresi + kapasite kısıtları
- Lisans devri için EPDK izni gerekiyor mu? (genellikle gerekli)
- Ön bildirim süresi ve koşulları
- Aktif soruşturma / yaptırım prosedürü var mı?
- TR Legal MCP: `search_rekabet_kurumu_decisions` (enerji piyasası) çek

**ÇED ve çevre:**
- ÇED izni mevcut mu? Kapsamı yeterli mi?
- Emisyon, atık, izin şartları ihlali var mı?
- Seveso/Büyük Endüstriyel Kaza statüsü? (Rehber: `references/seveso-buyuk-kaza-rehberi.md`)

**Rekabet:**
- İşlem rekabet eşiği aşıyor mu? (Rekabet Kurumu 4054/2010/4 kararı)
- Müvekkilin/alıcının halihazırdaki pazar payı + hedef = eşik aşımı?
- Avrupa Komisyonu AB Birleşme Tüzüğü (ECMR) — AB cirosu eşiği kontrolü

## Adım 2 — Yaptırım & KYC taraması

1. Hedef şirket ve gerçek yararlanan sahipleri OpenSanctions'da tara
2. Türk ortaklar: MKK teyit
3. Yabancı ortak: CAATSA m.232 riski değerlendirmesi (Rusya/CIS bağlantılı ise)
4. Yaptırım eşleşmesi → **Yönetici Ortak / Uyum görevlisine eskalasyon, işleme devam etme**

## Adım 3 — Vergi durum tespiti

- Vergi borcunun tespiti: Gelir İdaresi GİB sorgusu (TR Legal MCP: `search_gib_ozelge`)
- Aktif Danıştay vergi davaları
- Transfer pricing pozisyonu (intra-group bağlantı varsa özel dikkat)
- KDV iade alacakları — devralma sonrası talep edilebilir mi?
- Değer artış kazancı — satıcı tarafında vergi yükü → fiyata etkisi

## Adım 4 — İş güvenliği & iş hukuku

- İSGK 6331 iş güvenliği sicil — son 5 yıl kaza kaydı
- İş kazası + meslek hastalığı davaları — HMK süreçleri
- Sendika yapısı: TİS döngüsü, grev/lokavt tarihi
- Toplu işçi çıkarma geçmişi
- Yabancı çalışan varsa çalışma izni uyumu

## Adım 5 — Sözleşme portföyü & bağlı yükümlülükler

- Temel offtake / satış sözleşmeleri: change of control klozu var mı?
- EPC, O&M sözleşmeleri: devir halinde yeniden müzakere tetikler mi?
- Finansman sözleşmeleri: cross-default, prepayment riski
- Kilit personel tutma anlaşmaları
- Çevresel yükümlülükler (atık bertaraf, restorasyon)

## Adım 6 — Findings tablosu

| # | Bulgu | Kategori | Severity | Eylem |
|---|---|---|---|---|
| 1 | | Lisans / Vergi / Yaptırım / ISG / Sözleşme | 🔴/🟠/🟡/🟢 | |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# Enerji M&A Due Diligence — [Hedef şirket / tarih]

## ⚠️ Reviewer note
- Kapsam: [okunan belgeler, erişilemeyen alanlar]
- Bloklayıcı bulgu: [evet/hayır]
- [review] sayısı: N

## Bottom line

## Findings tablosu (özet)

## Düzenleyici & lisans (EPDK/ÇED/Rekabet)

## Yaptırım & KYC

## Vergi

## İş güvenliği & iş hukuku

## Sözleşme portföyü

## Önerilen adımlar
```

---

## /energy-finance:project-finance-review

---
name: project-finance-review
description: >
  Enerji altyapısı proje finansmanı belgelerini inceler: facility agreement, security
  package, conditions precedent checklist, lender's due diligence.
  EPDK lisans teyidi ve SPK bildirim kontrolü dahil.
argument-hint: "[facility agreement | info memo | CP checklist | term sheet]"
---

# /project-finance-review — Proje Finansmanı Belge İncelemesi

Birincil yargı çevresi Türkiye'dir. Finansman belgelerinde İngiliz hukuku + Londra
tahkimi yaygın; governing law analizi için `/commercial-legal:governing-law-review` çalıştır.

## Adım 0 — Belge tespiti

| Belge | Mevcut mu? |
|---|---|
| Facility Agreement (ana kredi) | [evet/hayır] |
| Security Package (teminat belgeleri) | [evet/hayır] |
| CP Checklist (conditions precedent) | [evet/hayır] |
| Term Sheet | [evet/hayır] |
| Technical Due Diligence raporu | [evet/hayır] |
| EPDK lisans belgesi | [evet/hayır] |
| Insurance programme | [evet/hayır] |

## Adım 1 — Yapı analizi

- **Borçlu yapısı:** SPV mi, doğrudan müvekkil mi, JV şirketi mi?
- **Borç/öz kaynak oranı:** D/E ratio — müvekkil / büroin risk eşiği
- **Borç türü:** Proje finansmanı (non-recourse) / kurumsal kredi (recourse) / karma
- **Kredi verenler:** Ticari banka konsorsiyumu / DFI (EBRD, IFC, AIIB) / tahvil / karma
- **Para birimi:** USD / EUR / TL / karma — döviz riski hedge

## Adım 2 — Conditions Precedent tarama

Kritik CP'ler:
- EPDK lisans alındı mı ve finansman için ön koşul mu?
- Halka açık müvekkil varsa KAP bildirimi tamamlandı mı?
- Çevre/ÇED izni finalize edildi mi?
- Temel sözleşmeler (EPC, O&M, offtake) imzalandı mı?
- Yatırımcı onayları (board resolution, shareholders') alındı mı?
- Sigortalar yerleştirildi mi?

Her eksik CP: `[review]` + finansal kapanış engelleyici mi tespit et.

## Adım 3 — Temel finansman şartları incelemesi

Facility Agreement'dan çıkar:
- **Faiz:** SOFR/EURIBOR + margin, PIK var mı
- **Taahhüt ücreti + düzenleme ücreti**
- **Geri ödeme profili:** sculpting mi, bullet mu, balloon mı
- **DSCR covenant:** minimum, test periyodu
- **Kısıtlayıcı taahhütler:** capex limit, dividend lock-up, change of control
- **Cross-default / cross-acceleration** — diğer müvekkil borç belgelerini etkiler mi?
- **Temerrüt olayları:** material adverse change (MAC) tanımı dar mı?

## Adım 4 — Teminat (security package) analizi

- İpotek: taşınmaz, makine-teçhizat
- Temlik: proje gelirleri, sigorta poliçeleri, sözleşmeler
- Rehin: SPV hisseleri, banka hesapları
- Kefalet: müvekkil / ana ortak garantisi — recourse seviyesi nedir?
- Türk hukukunda tescil: Tapu Sicili / Ticaret Sicili kayıtlı mı?

## Adım 5 — EPDK & SPK bildirim kontrolü

- **EPDK:** Lisans devri veya değişikliği gerektiriyor mu? Üretim/iletim/dağıtım lisans türü — kapasite ve sahiplik eşikleri. Rehber: `references/epdk-rehberi.md`.
- **SPK/KAP:** Müvekkil veya iştiraki halka açıksa — önemli ilişkili taraf işlemi, maddi gelişme bildirimi. Rehber: `references/kap-esirket-webfetch-rehberi.md`.
- **Yabancı yatırımcı:** FEFTA (Japonya), FIRPA (ABD) — DFI kredi verenlerin uyum yükümlülüğü.

## Adım 6 — Risk matrisi

🔴 Bloklayıcı: CP eksik + kapanış tarihi kısa / recourse covenant ihlali / EPDK lisans bekliyor
🟠 Yüksek: MAC tanımı geniş / dividend lock-up çok uzun / cross-default riski
🟡 Orta: Margin yüksek ama piyasa normunda / minor CP
🟢 Düşük: İdari, standart

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# Proje Finansmanı İncelemesi — [Proje adı / tarih]

## ⚠️ Reviewer note
- Belgeler: [okunanlar, atlanlar]
- CP durumu: N/M tamamlandı
- Flagged: N [review]

## Bottom line (2 cümle)

## Yapı özeti

## CP tarama tablosu

## Temel finansman şartları

## Teminat analizi

## EPDK/SPK bildirim durumu

## Risk matrisi

## Önerilen adımlar
```
