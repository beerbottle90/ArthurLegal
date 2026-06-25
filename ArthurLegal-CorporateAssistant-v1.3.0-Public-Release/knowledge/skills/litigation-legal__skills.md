# litigation-legal - Skill Referans Kitapcigi

> Alan: Dava yonetimi - HMK, ISG runbook, dis vekil
> Toplam skill: 7
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /litigation-legal:case-intake (245 satir)
- /litigation-legal:cold-start-interview (122 satir)
- /litigation-legal:evidence-collection (244 satir)
- /litigation-legal:hearing-prep (190 satir)
- /litigation-legal:isg-incident-response (314 satir)
- /litigation-legal:outside-counsel-brief (281 satir)
- /litigation-legal:settlement-eval (234 satir)

---

## /litigation-legal:case-intake

---
name: case-intake
description: >
  Yeni bir dava dosyası / ihtarname / dava açma kararı geldiğinde ön-değerlendirme:
  yargı yeri & görevli mahkeme tespiti (HMK), husumet, zamanaşımı, ön delil envanteri,
  ilk strateji önerileri, eskalasyon kararı. Dış vekil brief'i için temel oluşturur.
user-invocable: true
---

# Case Intake — Dava Ön-Değerlendirme

## Matter context

Practice-level CLAUDE.md `## Matter workspaces` bölümünü kontrol et. Litigation için matter workspaces **default ON**. Aktif matter yoksa:

> Bu yeni bir dava mı? `/litigation-legal:matter-workspace new <dosya-slug>` ile dosya aç (önerilen) veya `practice-level` cevapla. Aktif dosyada çalışırken dosya-spesifik `matter.md` öncelik kazanır.

## Destination check

Çıktının nereye gideceğini sor. Tipik destinasyonlar:
- **Dış vekil brief'i** → `[Dış vekil — büro adı]` etiketli, AVUKATLIK K. m. 36 üst başlığı
- **Hukuk Direktörü onayı** → "GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU" üst başlığı
- **İş birimi / yönetim bilgilendirme** → Quiet mode, hukuki jargon sadeleştir
- **Mahkemeye sunulacak dilekçe taslağı** → `/litigation-legal:hearing-prep` skill'i daha uygun

## Amaç

Yeni gelen bir dava materyalini **30 dakikalık ön-okumada** kategorize et:
- **🔴 Acil dış vekil + üst yönetim eskalasyon** — yaptırım, halka açık, üst yönetim sanık, basın
- **🟠 Standart dış vekil briefing** — normal dava akışı
- **🟡 Cevap stratejisi tartışılmalı** — ihtarnameye cevap veya açma kararı henüz net değil
- **🟢 Rutin / template ile cevaplanır** — örn. küçük tutarlı icra takipleri, ödenmiş borçlar için iflas erteleme

## Adımlar

### 1. Materyali oku ve özet çıkar

Kullanıcı bir dosya (dilekçe, ihtarname, mahkeme tebligatı, dış vekil ön-rapor) yapıştırırsa veya yüklerse:

- **Karşı tarafın iddiası nedir?** (1 cümle özet)
- **Talep edilen nedir?** (tutar, davanın türü — eda/tespit/inşai/men)
- **Hukuki dayanak ne olarak gösteriliyor?** (madde no'lar)
- **Süreler nedir?** (cevap süresi HMK m. 127 — 2 hafta; ihtarname süresi)

### 2. Yargı yeri ve görevli mahkeme tespiti

HMK ile teyit:

- **Genel yetki (m. 6):** Davalı yerleşim yeri
- **Şirketler için yetki (m. 14):** Şirket merkezi ([ŞİRKET ADI] için İstanbul)
- **Sözleşmesel yetki (m. 17):** Sözleşmede yetki klozu varsa öncelik (TBK + HMK)
- **Tüketici sözleşmesinde (m. 19):** Tüketicinin lehine kesin
- **İş davaları (4857 + HMK):** İşyerinin bulunduğu yer ([İşletme Yeri], Yalova, vs.)
- **Tahkim klozu (HMK m. 412 vd. + ISTAC/MTK kuralları):** Geçerliyse mahkeme yerine tahkim

**Görevli mahkeme:**
- Asliye Hukuk Mahkemesi — genel görevli
- Asliye Ticaret Mahkemesi (ATM) — TTK kapsamı (m. 4 — mutlak/nispi ticari iş)
- İş Mahkemesi — 4857 İş Kanunu uyuşmazlıkları
- Sulh Hukuk — kira, paylı mülkiyet
- Tüketici Hakem Heyeti — TKHK eşik altı

Mevzuat MCP'den HMK ve görevli mahkeme yönetmeliklerini çek, atıf et: `[Mevzuat MCP — GG.AA.YYYY]`.

### 3. Husumet (taraf sıfatı)

- **Aktif husumet:** Davayı açan taraf gerçekten davacı sıfatına sahip mi?
- **Pasif husumet:** Davalı olarak [ŞİRKET ADI] mi, yoksa bir bağlı şirket ([HALKA AÇIK İŞTİRAK], STAR, [ŞİRKET ADI] Enerji Ticaret, vs.)?
- **Tüzel kişilik perdesi:** Karşı taraf ana ortaktan değil de bağlı şirketten talepte bulunabilir mi?
- **[ÖZEL ENDÜSTRİ BÖLGESİ] özelliği:** [ÖZEL ENDÜSTRİ BÖLGESİ] içindeki tesisler ayrı tüzel kişiler — husumet doğru tespit edilmeli

Yanlış husumet → davanın reddi (taraf değişikliği, ek dava açma, zamanaşımı riski).

### 4. Zamanaşımı kontrolü (KRİTİK)

| Dava tipi | Zamanaşımı | Madde |
|---|---|---|
| Sözleşme aykırılığı (genel) | 10 yıl | TBK m. 146 |
| Ticari satım/hizmet sözleşme | 10 yıl | TBK m. 146 + TTK m. 21 |
| Haksız fiil tazminatı | 2 yıl (öğrenme) / 10 yıl (mutlak) | TBK m. 72 |
| **İSG kazası — bedensel zarar** | **2/10 + ceza zamanaşımı uzaması (TBK m. 72/2)** | TBK m. 72 |
| İş davası — alacak (kıdem, ihbar, ücret) | **5 yıl** (kıdem değişti) | İş K. m. 32 / 4857 + TBK |
| Vergi davası (Danıştay) | **30 gün** tebligattan | İYUK m. 7 |
| İdari işlem iptal (genel) | 60 gün | İYUK m. 7 |
| Sözleşmeden doğan menfi tespit | 1 yıl | TTK çek/bono özel |
| Marka ihlali (SMK) | 5 yıl (öğrenme) / 10 yıl (eylem) | 6769 SMK |
| KVKK ihlal (m. 14/2) | 10 yıl idari para | KVKK 6698 |

⚠️ **Mevzuat MCP'den ilgili maddeyi çek ve atıfta bulun**. Zamanaşımı kullanıcı tarafından söylenmişse **önce doğrula** (no silent supplement).

### 5. Ön delil envanteri

- Hangi belgeler elimizde? (sözleşme, ihtarname, e-yazışma, KEP, fatura)
- Hangileri karşı tarafın elinde olabilir? (delil isteme — HMK m. 220)
- Tanık ihtiyacı? (HMK m. 240)
- Bilirkişi ihtiyacı? (HMK m. 266)
- Keşif? (HMK m. 288)

### 6. Yarg MCP — emsal içtihat ara

Karşı tarafın iddiasının hukuki dayanağı ne ise, **Yarg MCP'den** o konudaki son 2-3 yıl emsal Yargıtay/Danıştay kararını çek:

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="<konu anahtar kelimeleri>",
  daire="<ilgili daire>",
  baslangicTarihi="2023-01-01"
)
```

Karşı tarafa olumlu mu, bize olumlu mu eğilim? Bir kaç emsal göster, atıfla: `[Yarg MCP — yargitay — GG.AA.YYYY]`.

### 6.5. TTK m. 5/A Zorunlu Arabuluculuk Kontrolü (ticari uyuşmazlıklar)

**6102 TTK m. 5/A:** Konusu **alacak + tazminat** olan **ticari uyuşmazlıklarda** dava açmadan önce **zorunlu arabuluculuk dava şartı**.

**Bu dosya kapsama giriyor mu?**
- [ ] Uyuşmazlık ticari mi? (TTK m. 4 — iki tacir + ticari iş)
- [ ] Talep "miktarı para" (alacak veya tazminat) mı?
- [ ] Konu KAPSAM DIŞI mı? (tüketici, iş davası, ihtiyati tedbir/haciz, ihbar — bunlar arabulucusuz dava açılabilir)

**Kapsama giriyorsa:**
- Dava açmadan önce **Adalet Bakanlığı Arabuluculuk Daire Başkanlığı**'na başvur
- Arabulucu atama (3 gün) + ilk toplantı (3 hafta) + tutanak (6 hafta tipik)
- Anlaşma → ilam niteliğinde icra edilebilir
- Anlaşmama → tutanak alınır, dava dilekçesine ekle (yoksa dava reddi — HMK m. 114)

**[ŞİRKET ADI] pratiği:**
- Vendor 80M TL gibi büyük ticari talepte zorunlu
- Paralel olarak ihtiyati tedbir gerekiyorsa (HMK m. 389 vd.) tedbir tek başına dava açılabilir, ana dava arabuluculuk sonrası
- Sulh teklifi açılış stratejisi `/litigation-legal:settlement-eval` skill ile birlikte düşünülmeli

⚠️ Yanlışlıkla atlanırsa **dava şartı yokluğu nedeniyle dava reddi** — ek 6 hafta + ek vekalet ücreti maliyeti.

### 7. [ŞİRKET ADI]-özel kontroller

Bu listeden geçir, gereken eskalasyonu tetikle:

- [ ] **[HALKA AÇIK İŞTİRAK] ilgili mi?** → KAP açıklama kontrolü gerekli mi? (`references/socar-[petrokimya iştiraki]-kap-rehberi.md`)
- [ ] **[İşletme Yeri] İSG kazası mı?** → `/litigation-legal:isg-incident-response` skill'i ÇOK DAHA UYGUN
- [ ] **EPDK lisansını etkiliyor mu?** → Compliance + EPDK ön-incelemesi
- [ ] **OFAC/AB yaptırım listesi karşı taraf?** → Compliance + Hukuk Başkanı, devam etme
- [ ] **[BORU HATTI PROJESİ] / hükümetlerarası anlaşma alanı?** → Dış hukuk panel + üst yönetim
- [ ] **Üst yönetim ismi sanık?** → CEO + YK bilgi
- [ ] **Basına intikal etmiş veya etme riski?** → İletişim Başkanlığı ([İLETİŞİM YÖNETİCİSİ]) koordinasyon
- [ ] **Yabancı hukuk / yabancı mahkeme-tahkim ayağı var mı?** → Uyuşmazlık yabancı hukuk yönetimliyse (İngiliz/NY hukuku) veya bir **yabancı mahkeme kararı Türkiye'de tanıma-tenfiz** gerektiriyorsa: MÖHUK 5718 (m. 50 vd. tenfiz, m. 58 vd. tanıma) uygulanır; yabancı hakem kararı için New York Konvansiyonu (`references/istac-rehberi.md`). İngiliz statüsü → `references/uk-legislation-rehberi.md` (legislation.gov.uk WebFetch); ABD statüsü/içtihatı → `references/us-legislation-rehberi.md` (GovInfo) + `references/courtlistener-rehberi.md`. Yönlendirme: `references/karsilastirmali-hukuk-rehberi.md`. Yabancı hukukun kesin yorumu için dış yabancı-hukuk uzmanı flag et.

### 8. Sınıflandırma ve eskalasyon önerisi

Yukarıdaki tüm bilgileri sentezle ve **şiddet ataması yap:**

🔴 / 🟠 / 🟡 / 🟢

Eskalasyon önerisi:
- Counsel seviyesinde mi karar verilir?
- Direktör onayı şart mı?
- Başkan / CEO eskalasyonu mu?

Bu ön kabuldür — Direktör/Başkan zaten onaylama yapmak için tam paketi göreceksen.

## Çıktı şablonu

```markdown
[ÜST BAŞLIK — practice profile ## Outputs'tan]

# Dava Ön-Değerlendirme — [Dosya Slug / Esas No]

## ⚠️ İnceleyen notu
- **Kaynaklar:** Yarg MCP [✓ N emsal / ✗]; Mevzuat MCP [✓ X madde / ✗]
- **Okuma kapsamı:** [yapılan oku — örn. "dilekçe + ekler 1-12 sayfa"]
- **Şiddet ataması:** 🔴/🟠/🟡/🟢
- **Acil aksiyonlar (önceki turda yapılmalı):** [N adet]
- **Güncellik:** [son arama tarihi]

## Özet

**Karşı taraf:** [...]
**İddia (1 cümle):** [...]
**Talep:** [tutar/tür]
**Hukuki dayanak:** [madde no'lar]
**Cevap süresi:** [tarih + kalan gün]

## Yargı yeri ve görevli mahkeme

**Önerilen:** [mahkeme] — HMK m. [X] kapsamında. `[Mevzuat MCP — GG.AA.YYYY]`
**Alternatif/itiraz mümkün:** [varsa]

## Husumet

- Aktif husumet: [değerlendirme]
- Pasif husumet: [ŞİRKET ADI] A.Ş. mi, yoksa [bağlı şirket]? `[review]`

## Zamanaşımı

- **Hesaplanan zamanaşımı tarihi:** GG.AA.YYYY (kalan: N gün)
- **Dayanak:** [TBK/TTK/İş K. madde] — `[Mevzuat MCP — GG.AA.YYYY]`
- **Risk:** [yorum]

## Ön delil envanteri

| Delil | Bizde mi? | Gerekli? | Not |
|---|---|---|---|
| [...] | ✓/✗ | ✓ | [...] |

## Emsal içtihat (Yarg MCP)

| Karar | Tarih | Daire | Eğilim | Bizim için |
|---|---|---|---|---|
| [esas/karar no] | [...] | [...] | bize/aleyhe/karma | [yorum] `[Yarg MCP — yargitay — GG.AA.YYYY]` |

## [ŞİRKET ADI]-özel kontroller

- [ ] [HALKA AÇIK İŞTİRAK] KAP: [N/A veya açıklanan]
- [ ] [İşletme Yeri] İSG: [N/A veya yönlendir]
- [ ] EPDK lisans riski: [yok/var]
- [ ] Yaptırım: [yok/var]
- [ ] Üst yönetim sanık: [yok/var]
- [ ] Basın riski: [yok/var]

## Şiddet ataması: [emoji]

[Gerekçe]

## Önerilen sonraki adımlar (decision tree)

> **What next? Pick one and I'll help you build it out:**
> 1. **Dış vekil brief'i hazırla** — bu dosyayı `/litigation-legal:outside-counsel-brief` ile [büro] için briefle
> 2. **Hukuk Direktörü eskalasyon notu** — bu özetin üst yönetime gidecek versiyonu
> 3. **Daha fazla bilgi al** — şu soruları araştırmadan strateji koyamam: [3 soru]
> 4. **Bekle ve izle** — cevap süresi dolmadan ek bilgi gelirse revize edeceğim (tarih: GG.AA.YYYY)
> 5. **Başka** — bana ne yapmamı istediğini söyle

**One question I'd ask that isn't in my checklist:** [örn. "Karşı taraf vekilinin sözlü/yazılı iletişim üslubu nasıl? Daha önce sulha yatkın mıydı, agresif miydi? Bu strateji tercihimi etkiler."]
```

## Reviewer note format

İcra sırasında `## ⚠️ İnceleyen notu` deliverable'ın üstüne yerleştirilir, yukarıdaki şablonda gösterildiği gibi.

## Hatalar / kenar durumlar

- **Kullanıcı sadece "yeni dava geldi" der, dosya yüklemez** → Sor: "Dilekçe metni veya ihtarnameyi yapıştırır mısın? Veya bir özet ver."
- **Karşı taraf vekili tanıdık ama dosya tanımıyor** → "Bu vekille daha önce yaşadığımız başka davalar var mı? `/litigation-legal:matter-workspace list` ile bakayım?"
- **Zamanaşımı çok yakın** → 🔴 + büyük uyarı: "⚠️ Zamanaşımı [X] gün içinde doluyor. Bu dava açma kararı **bu hafta** verilmeli."
- **Tahkim klozu var ama mahkemede dava açıldı** → 🟠 + "Tahkim itirazı (HMK m. 116/c) sunulmalı; aksi halde tahkim hakkı düşer."

---

## /litigation-legal:cold-start-interview

---
name: cold-start-interview
description: >
  Litigation pratiğini bilgisayara öğret — dava modeli, dış vekil paneli, eskalasyon
  matriksi, settlement yetkisi, takip sistemi, yakıcı sorun. 2-dakikalık hızlı vs.
  10-dakikalık tam mod. Çıktı: practice profile CLAUDE.md'nin doldurulması.
user-invocable: true
---

# Cold-Start Interview — Litigation Practice

## Amaç

Bu eklentinin diğer tüm skill'leri practice profile'a (`~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`) dayanır. Yeni kurulumda veya pratik değişikliğinde bu skill'i çalıştır — sorulara cevap ver, profil otomatik dolar.

## Modlar

Kullanıcı bir argüman vermezse, sor:

> İki mod:
> - **Hızlı (2 dakika)** — sadece kritik 6 soru. Çoğu alan `[DOLDUR]` kalır; sonra elinle doldurursun.
> - **Tam (10 dakika)** — 20+ soru; tüm profili doldurur. Önerilen.
>
> Hangisini istersin? Veya `--side` (taraf) gibi spesifik argüman var mı? (`--redo` mevcut profili sıfırlar, `--check-integrations` sadece MCP ve sistem bağlantıları kontrol eder.)

## Hızlı mod (6 soru)

1. **Dava modeli:** "Tüm davalar dış vekille mi, içeride ekip mi, karma mı?"
2. **Aktif dava hacmi:** "Yaklaşık kaç aktif dava? 10-50, 50-200, 200+?"
3. **Yakıcı sorun:** "En yakıcı dava kategorisi: İSG/çevre, iş davaları hacim, vendor/ticari, regulator itirazları?"
4. **Birincil venue:** "Çoğu dava nereye gidiyor? (İstanbul/Ankara/İzmir/karma)"
5. **Birincil dış vekil:** "Ana büro(lar) — isim ver veya [DOLDUR]"
6. **Settlement onay matriksi:** "Tutara göre kademeli mi, hep üst yönetim mi, daha gevşek mi?"

Cevaplara göre profil doldurulur. Eksik kalan kısımlar açıkça `[DOLDUR]` etiketli kalır.

## Tam mod (20+ soru, batch'ler halinde)

### Batch 1 — Pratik modeli ve hacim
- Dava modeli (içeri/dış/karma)
- Aktif dava sayısı + tip dağılımı (iş, ticari, İSG, regulator, idari, ceza)
- Birincil yakıcı sorun + ikincil yakıcı sorunlar
- Trend (artıyor/azalıyor/sabit)

### Batch 2 — Outside counsel paneli
- Her pratik alan için birincil + ikincil büro
- Aylık rapor cadence + format
- Brief verme süreci
- Vekalet ücreti modeli (saatlik / başarı / sabit / karma)
- KEP iletişim disiplini

### Batch 3 — Eskalasyon ve onay
- Sulh teklifi yetkisi (tutar kademeleri)
- İstinaf/temyiz başvuru yetkisi
- AYM bireysel başvuru yetkisi
- Ceza dosyası savunma stratejisi onayı
- **Tutardan bağımsız otomatik eskalasyon listesi** ([HALKA AÇIK İŞTİRAK], üst yönetim isim, basın, EPDK lisans riski, yaptırım, vs.)

### Batch 4 — Venue ve teknoloji
- Birincil mahkemeler (davacı/davalı sıfat ayrı)
- Tahkim politikası (ISTAC/ICC/ad hoc)
- UYAP erişimi (kim, nasıl)
- Case management yazılımı (var/yok, hangi)
- iManage / SharePoint / Drive tercihi

### Batch 5 — Halka açık ve özel kontroller
- Halka açık şirket varsa (örn. [HALKA AÇIK İŞTİRAK]) — KAP açıklama disiplini
- Yatırımcı ilişkileri koordinasyonu
- Compliance ekibi ile interaction (MASAK, OFAC vs.)
- Crisis communications protokolü (basın, sosyal medya)

## Çıktı

Profil dolduktan sonra:

1. **CLAUDE.md güncellenir** — `[DOLDUR]` kalanlar açıkça gösterilir
2. **Özet** kullanıcıya gösterilir:

```markdown
## ✓ Practice profile dolduruldu

**Doldurulan:**
- Dava modeli: [özet]
- Hacim: [özet]
- Yakıcı sorun: [özet]
- Outside counsel paneli: [özet]
- Eskalasyon: [özet]
- ...

**Hala [DOLDUR]:**
- [liste]

**Sonraki adım önerisi:**
- /litigation-legal:case-intake — yeni dosya geldi
- /litigation-legal:isg-incident-response — İSG/çevre olayı oldu
- Manuel: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
```

## Bağımsız çağırma (--check-integrations)

Sadece şu kontrolleri yap:

1. **TR Legal MCP** — test sorgu: `search_yargitay_decisions(arananKelime="işe iade", baslangicTarihi="2025-01-01")` → cevap geliyor mu?
2. **Mevzuat MCP** — test sorgu: `search_mevzuat(mevzuat_no="6100", mevzuat_tur="KANUN")` → HMK dönüyor mu?
3. **iManage** (varsa) — bağlantı testi
4. **Slack / Teams** (varsa) — bağlantı testi

Rapor:
```markdown
## Entegrasyon kontrolü

| Entegrasyon | Durum | Not |
|---|---|---|
| Yarg MCP | ✅ N karar döndü | Aktif |
| Mevzuat MCP | ✅ HMK 6100 bulundu | Aktif |
| iManage | ⚠️/❌ | [neden] |
```

## Reviewer note

Profil doldurma çıktısı için:
> ⚠️ İnceleyen notu: Cold-start interview ile dolduruldu. Profil eksik alanlar `[DOLDUR]` etiketli. İlk gerçek skill çağrısı öncesi en azından dış vekil paneli + eskalasyon matriksi doldurulmalı.

---

## /litigation-legal:evidence-collection

---
name: evidence-collection
description: >
  Dava açılması veya beklenmesi durumunda delil toplama protokolü: Türk hukuku
  legal hold (ABD doktrini DEĞİL — TBK + TTK + KVKK üzerinden), UYAP belge çekme
  listesi, tanık listesi (HMK m. 240), bilirkişi (HMK m. 266), keşif (HMK m. 288),
  delil tespit davası (HMK m. 400). Dış vekille koordineli.
user-invocable: true
---

# Evidence Collection — Delil Toplama Protokolü

## Matter context

Matter workspaces ON. Bu skill aktif bir matter'da çalışır:

> Hangi dosya için delil topluyoruz? Aktif matter: [slug] veya yeni `/litigation-legal:matter-workspace new`?

## Destination check

- **İç hukuk müşaviri raporu** → "GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ"
- **Dış vekile transmit** → "AVUKATLIK K. m. 36 — DIŞ VEKİL BRIEF" üst başlığı
- **Mahkemeye delil dilekçesi taslağı** → üst başlık çıkar, "TASLAK" ekle

## Amaç

İki senaryo:

1. **Dava açılmış veya başlama beklentisi yüksek** → derhal **delil koruma** (Türk versiyonu legal hold)
2. **Mahkemede delil sunumu hazırlık** → HMK delil çekme prosedürleri (m. 219 vd.)

## A. DELİL KORUMA (Litigation Hold)

### ABD doktrini Türkiye'de DOĞRUDAN yok

⚠️ **Önemli:** ABD "litigation hold" doktrini doğrudan Türk hukukunda yoktur. Buna karşı şu kanuni ödevler vardır:

| Hukuki temel | Yükümlülük |
|---|---|
| **TCK m. 281** | Suç delilini yok etme — cezai sorumluluk |
| **TBK m. 50-52** | Tazminat sorumluluğu için delil koruma |
| **TTK m. 64 + 82** | Ticari defter ve belgelerin 10 yıl saklama |
| **HMK m. 219-220** | Hasım tarafın elinde olan delili sunma yükümlülüğü |
| **6698 KVKK m. 7** | Veri saklama süresi (ama dava varsa daha uzun saklanır) |
| **Vergi Usul Kanunu m. 253** | 5 yıl ticari belge saklama |
| **SGK Kanunu** | İş kazası belgeleri 10 yıl saklama |

**Pratik:** Bir dava açıldığında veya başlama beklentisi gerçekleşince:
1. **İlgili belgelerin silinmesi/yok edilmesi → TCK m. 281 ve HMK m. 217 kapsamında ihlal**
2. KVKK saklama süresi geçmiş olsa bile **dava nedeniyle saklanır** (KVKK Kurul kararı çeşitli)
3. Belge silinirse mahkeme **aleyhe karine** kurabilir (HMK m. 220)

### Legal hold notice taslağı (Türk versiyonu)

Kullanıcı bu skill'i tetiklediğinde, **konuyla ilgili çalışanlara gidecek "delil koruma duyurusu"** taslağını üret:

```markdown
[ÜST BAŞLIK: ŞİRKET İÇİ — GİZLİDİR]
[Tarih]

Konu: [Dosya / olay] ile ilgili delil koruma duyurusu

Sayın [çalışan/birim],

[Olay/uyuşmazlık] ile ilgili dava süreci başlamıştır / başlama beklenmektedir.
Bu süreçle ilgili tüm doküman, e-posta, yazışma, fiziksel belge, kamera kaydı
ve dijital veri **derhal koruma altına alınmalıdır**.

**Kapsam (örneklemeli, sınırlama değildir):**
- [Olay/sözleşme/işlem] ile ilgili tüm yazışmalar (e-posta, KEP, mesajlaşma)
- [İlgili dönem] kontrol listeleri, raporlar, tutanaklar
- [İlgili kişiler] tarafından oluşturulan tüm dokümanlar
- [İlgili sistem/teçhizat] log kayıtları
- Bu konuyla ilgili olduğunu düşündüğünüz HER doküman

**Yapılması gerekenler:**
1. Mevcut dosyaları **silmeyiniz, değiştirmeyiniz, yok etmeyiniz.**
2. Bilgisayar / e-posta / Teams / SharePoint'te otomatik silme varsa **devre dışı bırakınız** veya BT'den **istisna** isteyiniz.
3. Fiziksel belgeleri **ayrı bir dosyada saklayınız**.
4. Yeni gelen ilgili belge veya yazışmaları aynı dosyaya ekleyiniz.

**Süre:** Bu koruma talimatı **yazılı olarak Hukuk Müşavirliği tarafından kaldırılmadıkça** geçerlidir.

**Sorumluluk:** Bu talimata aykırı hareket TCK m. 281 (suç delilini yok etme)
kapsamında **kişisel cezai sorumluluk** doğurabilir; ayrıca şirket aleyhine
HMK m. 220 kapsamında **aleyhe karine** oluşur.

**Sorular için:** [Hukuk Counsel] — [e-posta/Teams]

Saygılarımla,
[Hukuk Direktörü adı]
[ŞİRKET ADI] A.Ş.
Hukuk, Uyum ve Kurumsal Yönetişim Başkanlığı
```

Çıktıda hangi alanların `[DOLDUR]` olduğu net olsun.

### BT koordinasyonu

- [ ] **E-posta arşivi:** İlgili kullanıcıların e-postaları "litigation hold" işaretlensin (otomatik silme devre dışı)
- [ ] **Teams / Slack mesajları:** Aynı şekilde
- [ ] **SharePoint / Drive:** İlgili dosyalar version history'si korunsun
- [ ] **ERP / case management sistemi:** İlgili kayıtlar audit log'la
- [ ] **Kamera sistemleri:** Otomatik silme cycle'ı uzatılsın
- [ ] **Backup tape'ler / soğuk depolama:** İlgili dönem backupları segregate edilsin

## B. MAHKEMEDE DELİL SUNUMU (HMK)

### Delil çeşitleri (HMK m. 192-294)

| Delil tipi | HMK madde | Kullanım | [ŞİRKET ADI]-spesifik |
|---|---|---|---|
| **Belge (yazılı delil)** | m. 199-224 | Sözleşme, ihtarname, e-posta (KEP), fatura, raporlar | KEP çıktısı **kesin delil** (TTK m. 18/3) |
| **Tanık** | m. 240-265 | Olaya tanıklık eden gerçek kişi | İSG kazasında işçi/teknisyen kritik |
| **Bilirkişi** | m. 266-287 | Teknik/uzmanlık gerektiren mesele | Rafineri/[petrokimya iştiraki] teknik konular, çevre etkisi, vergi hesabı |
| **Keşif** | m. 288-292 | Mahkemenin yerinde inceleme | [İşletme Yeri] tesisi kaza sonrası keşif |
| **Yemin** | m. 225-239 | Kesin delil ikamesi (nadir) | Genelde ticari uyuşmazlıkta |
| **Bilirkişi heyeti raporu** | m. 281 | Karmaşık konularda 3+ kişi | Rafineri kazası standart 3 kişilik heyet |

### HMK m. 220 — Hasım tarafın elindeki delil

Karşı tarafta olan ama bize lazım olan bir delil için (örn. karşı tarafın iç yazışması, denetim raporu):

```markdown
Mahkemeye dilekçeyle başvurarak [HMK m. 220]:
- Belgenin niteliğini ve içeriğini tarif et
- Karşı tarafın elinde olduğunu kanıtla / gösteren delil
- İbraz edilmemesi halinde sonuçları talep et:
  - Mahkeme aleyhe karine kurabilir
  - Belgenin içeriğinin iddia edildiği gibi olduğu kabul edilebilir
```

Bu talep dilekçesinin **taslağını üret** (kullanıcıdan dosya bilgisi al → format).

### Tanık listesi (HMK m. 240)

```markdown
**Tanık listesi hazırlama:**

| Sıra | İsim | Adres | Tanıklık edeceği konu | Sıralama mantığı |
|---|---|---|---|---|
| 1 | [...] | [...] | [...] | "Olayın oluş şekli" |
| 2 | [...] | | | "Sözleşmenin kuruluşu" |

**[ŞİRKET ADI]-özel:**
- Şirket çalışanı tanıklık edebilir mi? → HMK m. 248 — yakınlık ilişkisi varsa hâkim takdiri
- Yabancı uyruklu üst yönetici tanıklığı → tercüman gerekli (HMK m. 263), KEP/Apostille gerekebilir
- Sendika temsilcisi tanıklığı → [SEKTÖR SENDİKASI] ile koordinasyon
```

### Bilirkişi (HMK m. 266)

Karmaşık teknik konular (rafineri patlama nedeni, çevre kirlilik kaynağı, marka benzerlik, vergi hesabı) için bilirkişi şart.

```markdown
**Bilirkişi talep dilekçesi hazırlama:**

- Hangi konuda? (örn. "Patlamanın teknik nedeni, sorumluluk taksiri")
- Bilirkişinin nitelik şartları (örn. "Petrol rafinasyon mühendisliği ihtisası")
- Bilirkişi listesinden mi yoksa serbest meslek mensuplarından mı?
- Ön rapor vs. duruşmada savunma?
```

### Keşif (HMK m. 288)

Mahkemenin yerinde inceleme yapması:

- **Avantaj:** Soyut analiz yerine somut görme; karşı tarafın hatalı iddiasını kırma
- **Risk:** Mahkeme bizim aleyhimize bir şey görebilir
- **[ŞİRKET ADI]-özel:** [İşletme Yeri] tesisinde keşif → güvenlik prosedürleri (yangın eğitimi, koruyucu ekipman); EPDK lisans kapsamında izinler

## TR Legal MCP — emsal aramaları

Delil sunumu prosedürlerinde benzer dava emsallerini Yarg MCP'den çek:

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="HMK 220 belge ibraz aleyhe karine",
  daire="Hukuk Genel Kurulu",
  baslangicTarihi="2022-01-01"
)
```

KEP'in delil değeri için özel arama:

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="kayıtlı elektronik posta KEP delil",
  baslangicTarihi="2020-01-01"
)
```

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Delil Toplama Protokolü — [Dosya slug]

## ⚠️ İnceleyen notu
- **Senaryo:** Delil koruma (legal hold) / Mahkeme delil sunumu / Karma
- **Acil aksiyonlar:** [liste]
- **Mevzuat referansları:** HMK m. [...], TCK m. 281, TTK m. 64, KVKK m. 7 `[Mevzuat MCP — GG.AA.YYYY]`
- **Emsal:** [N karar] `[Yarg MCP — yargitay — GG.AA.YYYY]`

## A. Delil koruma duyurusu (taslak)

[duyuru taslağı — yukarıdaki şablon]

**Dağıtım listesi:**
- [İlgili çalışan listesi]

**BT koordinasyonu yapılacaklar:**
- [checklist]

## B. Mahkemeye sunulacak delil planı

### B1. Belge envanteri
[tablo: belge, kaynak, ibraz edilebilir mi, m. 220 talep mi]

### B2. Tanık listesi
[tablo]

### B3. Bilirkişi talebi
[varsa — konu, nitelik]

### B4. Keşif talebi
[varsa — yer, neden]

## Sonraki adımlar (decision tree)

> **What next? Pick one and I'll help you build it out:**
> 1. **Delil koruma duyurusunu dağıt** — IT + İK koordineli; dağıtım listesini onayla
> 2. **HMK m. 220 ibraz talep dilekçesi** — karşı tarafa karşı [belge için]
> 3. **Tanık çağrı dilekçesi taslağı**
> 4. **Bilirkişi seçim önerisi** — listeden 3 isim
> 5. **Daha fazla bilgi al** — şu soruları cevaplayalım: [...]

**One question I'd ask that isn't in my checklist:** [örn. "Karşı tarafın iç soruşturmasından sızabilecek bir belge var mı? Whistleblower kanalına gitmiş olabilir mi?"]
```

## Reviewer note format

İnceleyen notu standardı `practice profile → ## Outputs` bölümündeki [ŞİRKET ADI] formatına göre.

---

## /litigation-legal:hearing-prep

---
name: hearing-prep
description: >
  Duruşma öncesi hazırlık paketi: 1 sayfa dava özeti, karşı taraf iddia haritası,
  cevap/beyan dilekçesi taslağı, delil sunum sırası, tanık soru listesi, "olası
  hakim soruları" hazırlığı. Dış vekil ile koordineli — in-house tarafından dış
  vekile gönderilen "duruşma günü brief'i".
user-invocable: true
---

# Hearing Preparation — Duruşma Hazırlık Paketi

## Matter context

Aktif matter şart. `matter.md`'den son durum çekilir.

## Destination check

- **Dış vekile gidecek duruşma brief'i** → AVUKATLIK K. m. 36 üst başlığı
- **İç değerlendirme (Hukuk Direktörü bilgi)** → GİZLİDİR HUKUK MÜŞAVİRLİĞİ
- **Mahkemeye sunulacak cevap dilekçesi taslağı** → "TASLAK" + dış vekil onayı sonrası

## Amaç

Duruşma günü dış vekilin elinde olması gereken **tek-paketlik özet:** mahkemenin görüşeceği konuların özeti, bizim pozisyonumuz, karşı tarafın muhtemel hamleleri, hazır cevaplar.

## Adımlar

### 1. Dava 1-sayfa özeti

```markdown
# [Dosya] - Duruşma Brief'i

**Esas no:** | **Mahkeme:** | **Hâkim:** | **Tarih:** | **Saat:**
**Taraflar:** | **Karşı vekil:** | **[ŞİRKET ADI] vekili:** | **Konu özeti:**

**Bu duruşmanın gündemi (tahmin):**
- [Mahkeme talebi, varsa]
- [Bilirkişi raporu sonrası tartışma]
- [Tanık dinlenmesi]
- [Yeni delil sunumu]
- [Beyan / cevap dilekçesi alımı]

**Bugün karar verilebilecek meseleler:**
- [...]
```

### 2. Karşı taraf iddia haritası

Karşı tarafın muhtemel argümanlarını ve hazır cevapları:

| Karşı argüman | Bizim cevap | Dayanak (madde/içtihat) |
|---|---|---|
| [...] | [...] | `[Mevzuat MCP / Yarg MCP — GG.AA.YYYY]` |

### 3. Cevap dilekçesi / beyan taslağı (HMK)

Eğer beyan veya cevap dilekçesi sunulacaksa, **dış vekil için ön-taslak:**

```markdown
**[Mahkeme adı] HÂKİMLİĞİNE**

ESAS NO: [...]
KARAR NO: (varsa)

DAVALI / DAVACI: [[ŞİRKET ADI] A.Ş.]
VEKİLİ: [dış vekil, baro sicil no]

DAVACI / DAVALI: [karşı taraf]
VEKİLİ: [karşı vekil]

KONU: [Cevap dilekçesi / beyan / ek beyan]

---

I. OLAYLAR

[Olay özeti — bizim açımızdan]

II. HUKUKİ DEĞERLENDİRME

A. [Argüman 1] — [TBK m. ... / TTK m. ... / HMK m. ...]
B. [Argüman 2] — [...]
C. [Argüman 3] — [...]

III. DELİLLERİMİZ

1. [Belge]
2. [Tanık]
3. [Bilirkişi raporuna itirazlarımız]

IV. SONUÇ

Yukarıdaki açıklamalar ışığında, [davanın reddi / kabulü / kısmen kabulü] talep edilir.

Tarih: GG.AA.YYYY

Vekil: [imza]
```

**ÖNEMLİ:** Bu taslak DİREKT mahkemeye sunulmaz — dış vekil revize edip, baro pulu / e-imza ile kendi sunar.

### 4. Delil sunum sırası

Hangi delil, ne zaman, neden bu sırada?

| Sıra | Delil | Sunum anı | Sebep |
|---|---|---|---|
| 1 | [Sözleşme] | İlk beyan | "Pozisyonumuzun temeli" |
| 2 | [E-yazışma] | Karşı taraf X iddiasını yaparsa | "Karşı tarafın bilgi sahibi olduğunu kanıtlar" |

### 5. Tanık soru listesi

Eğer tanık dinlenecekse:

```markdown
**Tanık:** [İsim, sıfat]
**Bizim için sorulması gereken sorular:**
1. [Olayın yaşandığı tarihte siz neredeydiniz?]
2. [Karşı tarafla yazışma kanıtınız var mı?]
3. [...]

**Karşı taraf vekilinin tanığa soracağı muhtemel sorular:**
1. [...]

**Tanığın güçlü yönü:** [...]
**Tanığın zayıf yönü:** [bize karşı sorular bunu hedefleyebilir]
```

### 6. "Olası hakim soruları" hazırlığı

Hâkim duruşmada şu soruları sorabilir; cevaplar:

```markdown
- Hâkim: "Karşı tarafın iddia ettiği [olay] gerçekten yaşandı mı?"
  Cevap: [...]
- Hâkim: "Sulh yolunu denediniz mi?"
  Cevap: [Pratik profili → settlement-eval skill çıktısından]
- Hâkim: "Bilirkişi raporuna itirazınız nedir?"
  Cevap: [...]
```

### 7. Stratejik notlar

```markdown
- **Hâkim eğilimi:** [Önceki dosyalarda Yargıtay/HGK kararlarına bakış, sulh önerisi yapma eğilimi, vs.]
- **Karşı vekil eğilimi:** [Agresif mi, sulha açık mı, formaliteye dikkat eder mi]
- **Bu duruşmada bizim hedefimiz:** [Bilirkişi raporuna itiraz / Sulh teklifini açıkça reddetmemek / Süre kazanma / Karar talebi]
- **Risk:** [Duruşmadan kötü çıkma olasılığı varsa, neden]
```

## TR Legal MCP

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="<dava konusu> bilirkişi rapor itiraz",
  daire="<ilgili daire>",
  baslangicTarihi="2023-01-01"
)
```

Benzer dosyaların **bu aşamada nasıl gittiğini** öğren — strateji şekillenir.

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Duruşma Hazırlık — [Esas No / Dosya Slug]

## ⚠️ İnceleyen notu
- **Duruşma tarihi:** GG.AA.YYYY (kalan: N gün)
- **Mahkeme:** [...]
- **Karar verilebilecek:** [N adet]
- **Hazırlık tamlık:** [%X] (eksik: ...)
- **Dış vekil onayı:** [tarih]
- **Reviewer karar bekleyen:** N adet

[1-sayfa özet, iddia haritası, cevap dilekçesi taslağı, delil sırası, tanık soruları, hâkim soruları, stratejik notlar]

## Sonraki adımlar

> 1. **Cevap dilekçesini dış vekile transmit et** — KEP ile
> 2. **Stratejik karar paketi** — Hukuk Direktörü onayı için
> 3. **Bilirkişi raporu detay analizi** — `/litigation-legal:evidence-collection`
> 4. **Sulh hazırlığı** — `/litigation-legal:settlement-eval` (hâkim sulh önerirse)
> 5. **Daha fazla bilgi** — şu soruları cevaplayalım: [...]

**One question I'd ask that isn't in my checklist:** [örn. "Karşı tarafın bilirkişi raporuna olan tutumu nasıl? Reddetmiş mi, kabul mu etmiş? Bu duruşmada strateji değiştirebilirler mi?"]
```

---

## /litigation-legal:isg-incident-response

---
name: isg-incident-response
description: >
  İSG (iş sağlığı güvenliği) veya çevre olayı sonrası ilk 24-72 saat runbook'u —
  [İşletme Yeri] rafineri/[petrokimya iştiraki] kompleksi gibi yüksek riskli tesislerde ölümlü/ciddi kaza
  sonrası hukuk müşavirinin ATMASI gereken adımlar: delil koruma, savcılık beklenti
  planlaması, çalışan vekalet teklifi, dış vekil + crisis comms tetikleyici, EPDK/
  Çevre Bakanlığı/KAP bildirim takvimi, üst yönetim eskalasyon zinciri.
user-invocable: true
---

# İSG / Çevre Olayı — İlk 24-72 Saat Runbook

> **⚠️ Bu skill [ŞİRKET ADI] için yakıcı sorun olarak işaretlenmiştir.** [İşletme alanı]nde geçmişte ölümlü/ciddi kaza dosyaları yaşandı; her olayda doğru ilk müdahale tazminat tutarını, ceza dosyasının yönünü ve EPDK lisans riskini doğrudan etkiler.

## ⚠️ KAP açıklama tetik haritası — STAR vs [HALKA AÇIK İŞTİRAK] ayrımı (KRİTİK)

Olay hangi tüzel kişinin tesisinde / faaliyet alanında oldu, ona göre KAP yükümlülüğü değişir:

| Tüzel kişi | Halka açık mı? | KAP açıklama doğrudan? |
|---|---|---|
| **[HALKA AÇIK İŞTİRAK] Petrokimya Holding A.Ş.** | ✅ **EVET (BIST: [BIST KOD])** | **DOĞRUDAN — SPK Tebliğ II-15.1 m. 5 "önemli olay"** |
| **[RAFİNERİ] A.Ş.** | ❌ Hayır ([ŞİRKET ADI] Rafineri A.Ş.'ye bağlı) | Doğrudan değil — ancak **[HALKA AÇIK İŞTİRAK] ile entegre operasyon etkisi varsa [HALKA AÇIK İŞTİRAK] üzerinden dolaylı KAP** |
| **[ŞİRKET ADI] A.Ş.** (holding) | ❌ Hayır | Doğrudan değil |
| **[ŞİRKET ADI] Depolama / Terminal / Enerji Ticaret** | ❌ Hayır | Doğrudan değil |
| **[ELEKTRİK SANTRALİ]** | ❌ Hayır | EPDK bildirim, KAP değil |
| **[DAĞITIM İŞTİRAK 1] / [DAĞITIM İŞTİRAK 2] (devir öncesi/sonrası)** | ❌ Hayır | KAP değil; devir aşamasında etki [HALKA AÇIK İŞTİRAK]'e yansıyorsa dolaylı |

**Karar matrisi:**

1. Olay **[HALKA AÇIK İŞTİRAK] tesisinde** veya **[HALKA AÇIK İŞTİRAK] faaliyetiyle doğrudan ilgili** mi? → **KAP açıklama derhal** (Yatırımcı İlişkileri + [HALKA AÇIK İŞTİRAK] YK Sekreterya)
2. Olay **STAR/[ŞİRKET ADI]-bağlı şirkette** ama **[HALKA AÇIK İŞTİRAK] üretim/satış zincirini etkiliyor** mu? (örn. STAR'dan etilen tedariki kesilirse [HALKA AÇIK İŞTİRAK] üretimini durdurur) → **[HALKA AÇIK İŞTİRAK] üzerinden dolaylı KAP değerlendirmesi** — Yatırımcı İlişkileri ile materyalite testi
3. Olay **STAR/[ŞİRKET ADI]-bağlı** ama **[HALKA AÇIK İŞTİRAK]'i etkilemiyor** → KAP açıklama **N/A**, sadece iç eskalasyon + basın koordinasyonu

**[ŞİRKET ADI] uygulama:** "[HALKA AÇIK İŞTİRAK] etkisi yok ise KAP N/A" kararı **yazılı dokümante edilmeli** (sonradan SPK denetiminde gerekçe olarak gösterilir). IR Başkanlığı + Hukuk ortak imzalı not.

---

## Matter context

Matter workspaces ON. İSG olayı yeni bir matter'dır:

> Bu yeni bir İSG/çevre olayı. Dosya açayım mı? Slug: `isg-YYYY-MM-DD-<tesis>` (örn. `isg-2026-05-17-aliaga-[petrokimya iştiraki]`). Cevap: evet/hayır/manuel slug.

## Destination check

Bu skill çıktısının iki ayrı versiyonu olur — destinasyona göre seç:

| Destinasyon | Versiyon |
|---|---|
| **İçeride hukuk müşavirliği + dış vekil (gizlilik içinde)** | Tam runbook, Avukatlık K. m. 36 üst başlığı |
| **Operasyonel yönetim (tesis müdürü, ISG, HSE) bilgi notu** | "Hukuki riskler & bildirim takvimi" kısaltılmış versiyon, hukuki strateji çıkar |
| **CEO/YK eskalasyon notu** | 1 sayfa executive summary + decision points |
| **KAP açıklama metni ([HALKA AÇIK İŞTİRAK] ilgili ise)** | Ayrı bir çıktı; bu skill başlatır, son halini SPK uzman avukat onayı sonrası |

## Olayın ciddiyet ataması (SEVERITY)

İlk olarak kullanıcıya sor:

```
Olayın seviyesi nedir?
A. 🔴 ÖLÜMLÜ veya ÇOK CİDDİ — bir veya birden fazla ölü, kalıcı sakatlık, büyük çevre kirlenmesi, basında haber
B. 🟠 CİDDİ — hastane sevki, üretim duruş, lokal çevre etki
C. 🟡 ORTA — yaralanma var ama ayakta tedavi, üretim devam, sınırlı etki
D. 🟢 KÜÇÜK — ramak kala, hafif yaralanma, raporlama amaçlı

Hangisi?
```

Cevaba göre **runbook ölçeği değişir.** A/B = tam runbook, C = sadeleştirilmiş, D = sadece raporlama checklist.

---

## TAM RUNBOOK (A/B seviyesi için)

### ⏰ İLK 1 SAAT

> **Hedef:** Kanıtların korunduğundan emin ol; üst yönetim haberdar olsun; dış vekil yola çıksın.

#### 1. Olay yeri delil koruma (KRİTİK)

**Hukuki temel:** TCK m. 281 (suç delillerini yok etme); CMK m. 161 (savcılığın delil isteme yetkisi); 6331 İSG K. m. 14 (raporlama).

Operasyonel ekibe (tesis müdürü, ISG uzmanı) **derhal iletilmesi gereken yönergeler:**

- [ ] **Olay yerini KORU** — kazadan etkilenen alana giriş kısıtlansın, fotoğraf ve video ile tüm haliyle belgelendir
- [ ] **Kamera kayıtları YEDEKLE** — kazadan önce/sonra 24 saatlik kamera kayıtları **derhal** ayrı diske kopyalansın (genelde sistem 7-30 gün geriye dönüşlü; geç kalınırsa silinir)
- [ ] **Vardiya defteri, kontrol listeleri, iş emirleri, JSA (Job Safety Analysis)** — kazaya yol açan süreçle ilgili tüm belgeler **kopyalanıp asıllar arşivlensin**
- [ ] **İlgili çalışanların eğitim dosyaları, sertifikalar, periyodik sağlık raporları, vardiya çizelgeleri** — savcılık talep etmeden hazırlansın
- [ ] **Olay öncesi 30 günlük HSE raporu / yakın kaza (near miss) raporları** — pattern olarak gelebilir
- [ ] **Olay yerine giren her kişi, saat saat log** — savcılık delil ihlali iddiasını önler

#### 2. Bildirimler (KANUNİ ZORUNLU)

| Kuruma | Yasal süre | Kim | Nasıl |
|---|---|---|---|
| **SGK** (iş kazası bildirimi) | 3 iş günü | İşveren | EBYS / SGK portalı |
| **Çalışma ve Sosyal Güvenlik Bakanlığı** | 3 iş günü | İşveren | Online |
| **Polise/Savcılığa** (ölümlü/ciddi yaralanma) | DERHAL | İşveren / 112 | Telefon + yazılı tutanak |
| **Çevre Bakanlığı** (çevre etkisi varsa) | DERHAL | Tesis müdürü | İl Çevre Müdürlüğü + telefon |
| **EPDK** (lisansa konu tesisin durması) | 24 saat (lisans şartlarına göre) | Lisans sahibi | EPDK portal + yazılı |
| **AKUT/AFAD** (büyük çevre / sosyal etki) | DERHAL | İl Acil Durum | — |
| **KAP** ([HALKA AÇIK İŞTİRAK] ilgili önemli olay) | DERHAL özel durum açıklaması | [HALKA AÇIK İŞTİRAK] | KAP üzerinden, SPK Tebliğ II-15.1 |
| **[BORU HATTI PROJESİ]** ([BORU HATTI PROJESİ] altyapı etkilendiyse) | 24 saat | İşletmeci | [BORU HATTI PROJESİ] işletme sözleşmesi |

⚠️ Bu süreler **yasal**, gecikme idari para cezası + ceza dosyasında ağırlatıcı.

#### 3. Üst yönetim eskalasyon zinciri

| Saat | Kim haberdar olmalı | Nasıl |
|---|---|---|
| 0-15 dk | Tesis müdürü, ISG uzmanı, HSE Başkanı | Telefon |
| 15-30 dk | İş Birimi Başkanı (Mirzayev — rafineri/[petrokimya iştiraki]; veya İbrahimov — doğal gaz) | Telefon |
| 30-60 dk | **Hukuk Direktörü** (Group GC) → **Hukuk Başkanı (Ismayilbayli)** → **CEO (Ibadov)** | Telefon zinciri |
| 60-90 dk | İletişim Başkanlığı ([İLETİŞİM YÖNETİCİSİ]) — basın hazırlık | Telefon + brief |
| 90 dk - 2 saat | Compliance + Yatırımcı İlişkileri ([HALKA AÇIK İŞTİRAK] ise) | E-posta + telefon |

`company-profile.md` anahtar kişiler tablosunu kontrol et — son atamalar değişebilir.

#### 4. Dış vekil mobilizasyonu

- [ ] **İSG/iş kazası uzmanı dış vekil** derhal aranır — `practice profile → outside counsel paneli → İSG / iş kazası` ([İşletme Yeri] için yerel firma kritik; İstanbul'dan sadece koordinasyon)
- [ ] **Ceza avukatı** — vekalet hazırlanır, ilgili olabilecek yöneticiler (tesis müdürü, ISG uzmanı) için **müdafilik onay formu** alınır
- [ ] **Çevre uzmanı dış vekil** (çevre etkisi varsa)
- [ ] **Sermaye piyasası uzmanı dış vekil** ([HALKA AÇIK İŞTİRAK] ise)

### ⏰ İLK 24 SAAT

> **Hedef:** Savcılık geliş anına hazır ol; çalışan haklarını koru; resmi bildirimler tamamla; iletişim koordine et.

#### 5. Savcılık beklenti planlaması

**CMK m. 130 — savunma hakkı sınırı:** Sanık vekili olarak resmen atanmadan, savcılık dosyasına tam erişim YOK. Bu nedenle:

- [ ] Ceza avukatı olabilecek müdafilerin **derhal vekalet ile sanık adayı yöneticiler için** atanması
- [ ] **Yöneticilere "ifade verme hakkı"** hatırlatılır:
  - Şüpheli sıfatıyla ifade verirken (CMK m. 147) **susma hakkı** var (m. 147/2-e)
  - Kendisi aleyhinde delil vermeme hakkı (m. 147/2-d)
  - Müdafi olmadan ifade vermemesi şiddetle önerilir
- [ ] İçeriği bilinmeyen tutanak / ifade tutanağına **imza atılmaması** önerisi

#### 6. Çalışan tarafı koordinasyon

- [ ] **Mağdur ailesi ile İK + İletişim koordineli** — taziye + acil destek (PR ve hukuki risk dengeli)
- [ ] **Diğer çalışan ifadeleri** — ısrarcı tanık ifadesi tutarsızlık doğurabilir, **avukat eşliğinde** verilmeli
- [ ] **Sendika ile koordinasyon** ([SEKTÖR SENDİKASI] başta) — TİS hükümleri + çalışan hakları
- [ ] Mağdur ailesinin **kendi vekili yoksa**, "size avukat öneririz" deme — etik sorun + savunmada zayıflık

#### 7. Belge / yazışma kontrol

- [ ] Olaya ilişkin **iç yazışmalar** (e-posta, Teams) — privilege/gizlilik kapsamı NETLEŞTİR (bkz. Avukatlık K. m. 36 sınırı in-house için)
- [ ] **"Olay anı" e-postaları** — kontrolsüz "biz suçluyuz" tarzı yazışmalar olabilir, hukuk bunu yönetilebilir formata çevirir
- [ ] Tüm operasyonel yazışmalar artık **avukat aracılığıyla** yapılır mesajı geçilir

#### 8. İletişim (basın, sosyal medya, yatırımcı)

- [ ] **Basın bildirisi** — İletişim Başkanlığı + Hukuk koordineli
  - Empati + sorumluluk kabul vs. soğukkanlı bilgi verme dengesi
  - "Sorumluluğu kabul ediyoruz" demek hukuki sorumluluğu artırabilir
  - "Sebepleri araştırıyoruz" güvenli formül
- [ ] **Sosyal medya monitoring** — yanıltıcı/abartılı haberlere düzeltme
- [ ] **KAP açıklaması** ([HALKA AÇIK İŞTİRAK] ise) — finansal etki + üretim duruş açıklanır

### ⏰ İLK 72 SAAT

> **Hedef:** Tablo netleşir; strateji sabitlenir; bildirimler tamamlanır.

#### 9. Olay raporu inceleme

- [ ] **İlk olay raporu (HSE/ISG uzmanı tarafından)** — hukukun gözüyle değerlendir, yanlış yorum veya zayıf nokta düzeltilsin
- [ ] **Bağımsız uzman keşfi** (kendi tarafımız) — bilirkişi ön-değerlendirmesi gerekir mi?
- [ ] **Operasyonel düzeltici aksiyon** — tekrar olmaması için derhal alınan tedbirler dökümante edilir (bu sonraki davalarda "öğrendiğimiz dersler" olarak savunmada kullanılır)

#### 10. Stratejik karar — dava beklentisi

- **Mağdur tarafı tazminat davası açar mı?** (1-2 yıl içinde muhtemel)
- **Savcılık ceza davası açacak mı?** (KAP m. 170 vd. — iddianame değerlendirme süreci)
- **Çevre Bakanlığı idari para cezası kesilecek mi?** (60 gün içinde itiraz hakkı — Danıştay 10. Daire)
- **EPDK lisans askıya alma yapacak mı?** (lisans hükümleri + EPDK kurul kararı süreci)

Her biri için ön-strateji:
- Sulh hazırlığı (mağdurla aktif veya tazminat fonu)
- Ceza savunması (taksir derecesi argümantı, fail-vendor/altışveren ayırımı)
- İdari ceza itirazı (Danıştay)
- EPDK lisans savunması (düzeltici aksiyon ispatı)

#### 11. Yarg MCP — emsal kararlar

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="iş kazası ölümlü 6331 işveren sorumluluk",
  daire="9. Hukuk Dairesi",  # iş kazası tazminat
  baslangicTarihi="2023-01-01"
)

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="taksirle öldürme rafineri patlama yönetici sorumluluk",
  baslangicTarihi="2020-01-01"
)  # Ceza Genel Kurulu kararları

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="10. Daire",
  arananKelime="çevre kirletme idari para cezası iptali",
  baslangicTarihi="2023-01-01"
)
```

Bu emsal kararlar mağdur/savcılık/çevre bakanlığı eğilimini gösterir; strateji buna göre.

---

## SADELEŞTİRİLMİŞ RUNBOOK (C seviyesi için)

C = orta seviye olay. Tam runbook'un alt-kümesi:
- Delil koruma (1, 7)
- Yasal bildirimler (2)
- Hukuk Direktörü eskalasyon (3 — sadece Counsel + Direktör)
- Dış vekil mobilizasyon (4 — sadece İSG uzmanı)
- Olay raporu inceleme (9)

Üst yönetim eskalasyon, basın koordinasyon, KAP açıklaması GENELDE gerekmez ([HALKA AÇIK İŞTİRAK] ilgili değilse).

## SADECE RAPORLAMA (D seviyesi için)

D = küçük olay / ramak kala. Bildirim checklist + iç dosyalama yeterli:
- SGK 3 iş günü
- HSE iç raporu
- Düzeltici aksiyon takip
- Hukuk müşavirliği bilgi notu (Counsel arşivine)

---

## Çıktı şablonu

```markdown
[ÜST BAŞLIK — practice profile ## Outputs'tan]

# İSG/Çevre Olayı Runbook — [Olay slug / Tesis / Tarih]

## ⚠️ İnceleyen notu
- **Olay seviyesi:** 🔴/🟠/🟡/🟢
- **Tetiklenen runbook:** Tam / Sadeleştirilmiş / Sadece raporlama
- **Kaynaklar:** Yarg MCP [✓ N emsal / not yet]; Mevzuat MCP [✓ X madde]
- **Acil aksiyonlar (sonraki 1 saat):** [liste]
- **Acil aksiyonlar (sonraki 24 saat):** [liste]
- **KAP açıklama:** [N/A / hazırlanıyor / tamamlandı]
- **Eskalasyon zinciri tetiklendi:** [evet, son durağı: ...]

---

## 🚨 SONRAKI 1 SAAT

[Checklist - ☐ formatında]

## ⏰ SONRAKI 24 SAAT

[Checklist + sorumlular]

## ⏰ SONRAKI 72 SAAT

[Checklist + stratejik kararlar]

## Yasal bildirimler tablosu

[tablo — kim, ne zaman, kime, nasıl]

## Eskalasyon zinciri ([ŞİRKET ADI])

[Saat saat kim bilgilendirildi]

## Dış vekil mobilizasyonu

| Pratik alan | Büro | İletişim | Durum |
|---|---|---|---|
| İSG/iş kazası | [...] | [...] | mobilize edildi/edilmedi |
| Ceza | [...] | [...] | [...] |
| Çevre | [...] | [...] | [...] |
| KAP/SPK | [...] ([HALKA AÇIK İŞTİRAK] ilgili ise) | [...] | [...] |

## Emsal içtihat (Yarg MCP)

[İlgili Yargıtay/Danıştay emsal kararları]

## Stratejik karar matrisi

| Risk vektörü | Olasılık | Etki | Hazırlık |
|---|---|---|---|
| Tazminat davası | Yüksek/Orta/Düşük | [$X-Y aralık] | [...] |
| Ceza davası | [...] | [yöneticiler için] | [...] |
| Çevre idari ceza | [...] | [...] | [...] |
| EPDK lisans riski | [...] | [...] | [...] |

## Sonraki adımlar (decision tree)

> **What next? Pick one and I'll help you build it out:**
> 1. **İlk basın bildirisi taslağı** — İletişim ile koordineli
> 2. **CEO eskalasyon notu** — 1 sayfa
> 3. **KAP açıklama metni** — [HALKA AÇIK İŞTİRAK] için
> 4. **Dış vekil brief'i** — `/litigation-legal:outside-counsel-brief`
> 5. **Bekle ve izle** — 24 saat sonra revize et

**One question I'd ask that isn't in my checklist:** [örn. "Mağdur ailesinin sosyal medyasında ne paylaşılıyor? Hukuki argümanı doğrudan etkileyen bir görüntü/itham var mı?"]
```

## Hatalı kullanım

- **"Küçük bir kaza, runbook gerek yok" diye atlama** — D seviyesi runbook'u en azından çağrılmalı; ramak kala olay listesi sonraki davada pattern olarak kullanılır.
- **"Sorumluluğu hemen kabul edelim" → savcılığın işini kolaylaştırır.** "Sebepleri araştırıyoruz" güvenli formül.
- **Çalışana "imzala" deme** — savunma hakkı ihlal edilebilir, sonraki davada baş ağrısı.
- **KAP'ı atlama** ([HALKA AÇIK İŞTİRAK] ise) — SPK yaptırımı + yatırımcı davası açar.

## Reviewer note

Bu skill çalıştığında **Hukuk Direktörü** ve **Hukuk Başkanı** otomatik bilgilendirme listesine eklenir (`outputs/escalation-notification.md` taslağı üretilir).

---

## /litigation-legal:outside-counsel-brief

---
name: outside-counsel-brief
description: >
  Dış vekile yeni bir dava dosyası iletiliyorken veya stratejik talimat verilirken
  standardize brief paketi: dosya özeti, sorulan sorular, beklentiler (timeline,
  bütçe, raporlama), iç hukuk pozisyonu, kritik notlar, escalation eşikleri. [ŞİRKET ADI]
  dış-vekil ağırlıklı modelin temel iş akışı. KEP üzerinden gönderim hazır.
user-invocable: true
---

# Outside Counsel Brief — Dış Vekil Brief'i

## Matter context

Bu skill **aktif matter** içinde çalışır (yeni dosya açıldıysa cold-start veya case-intake'den geliyor olabilir).

## Destination check

**Destinasyon: dış vekil (avukatlık bürosu)** — Avukatlık K. m. 36 + ticari sır rejimi kapsamında. Üst başlık:

```
DAVA BRIEF – DAHİLİ VE GİZLİDİR – AVUKATLIK K. m. 36 KAPSAMINDA
[ŞİRKET ADI] A.Ş. - Sayın [vekil adı / büro] dikkatine
Esas no: [...] | Taraflar: [...] | Mahkeme: [...]
Tarih: GG.AA.YYYY | Briefer: [in-house Counsel adı]
[ŞİRKET ADI] iç onay: [Hukuk Direktörü/Başkan onayı geçtiyse "Onaylı" + tarih]
```

KEP üzerinden gönderim için: brief tek dosyalık PDF olmalı (in-house tarafından oluşturulup KEP attachment olarak gönderilir).

## Amaç

[ŞİRKET ADI]'da **tüm davalar dış vekille yürütülüyor**. In-house ekibinin işi dış vekile **standardize edilmiş, eksiksiz, tek-istek paketleri** vermek. İyi brief = kısa iş ücreti + iyi cevap + daha az takip e-posta.

**Kötü brief'in maliyeti:** Dış vekil 5 ek soru sormak için saatlik ücret yazıyor; doğru bilgi olmayınca yanlış strateji; eksikten dolayı dosya kaybediliyor.

## Brief paketinin yapısı

### 1. Genel bilgi başlığı

```markdown
**Dosya bilgisi:**
- [ŞİRKET ADI] dosya no: [iç sistem]
- Esas no (varsa): [mahkemeden]
- Taraflar: [Davacı/Davalı [ŞİRKET ADI] mı?]
- Mahkeme/yargı yeri: [...]
- Konuya tarihi: [...]
- Cevap/itiraz süresi: [tarih + kalan gün]

**[ŞİRKET ADI] organizasyon bilgisi:**
- İlgili iş birimi: [Rafineri & Petrokimya / Doğal Gaz & Enerji / Portföy]
- İlgili tüzel kişi: [[ŞİRKET ADI] A.Ş. / [HALKA AÇIK İŞTİRAK] / [RAFİNERİ] / [ŞİRKET ADI] Enerji Ticaret / ...]
- İçeride dosya sahibi (in-house Counsel): [isim, iletişim]
- Eskalasyon zinciri: [Counsel → Direktör → ... → CEO]

**KAP / yatırımcı bilgi ([HALKA AÇIK İŞTİRAK] ilgili ise):**
- KAP açıklama gerekli mi? [evet/hayır/değerlendiriliyor]
- İçsel bilgi listesine giren bilgi var mı? [evet/hayır]
```

### 2. Olay/uyuşmazlık özeti (Background)

Maks 1 sayfa — dış vekil bunu hızla okur. **Zaman çizgisi (timeline)** kronolojik:

```markdown
## Background

[Tarih başlangıç]: [Olay başladı / sözleşme imzalandı / kaza yaşandı]
[Tarih]: [İhtarname geldi / cevap verildi]
[Tarih]: [Dava açıldı / cevap dilekçesi verildi]
[Tarih]: [Bilirkişi atandı / keşif yapıldı]
[Bugün]: [Şu an neredeyiz]

**Karşı taraf iddiası özeti:**
[1-2 paragraf]

**Talep edilen:**
- Tutar: [...]
- Diğer: [özür, men, vs.]

**Hukuki dayanak (karşı tarafın gösterdiği):**
- [Kanun madde no'ları + içtihat]
```

### 3. İç hukuk pozisyonu

```markdown
## İç hukuk pozisyonu

### [ŞİRKET ADI]'ın pozisyonu (savunma argümanları)
1. [Argüman 1] — dayanak: [...]
2. [Argüman 2] — dayanak: [...]
3. [Argüman 3 — yedek] — dayanak: [...]

### Zayıf noktalarımız (counter-argumentation öngörüsü)
- [Zayıf nokta 1] — karşı taraf bunu nasıl kullanır
- [Zayıf nokta 2]

### İçerideki ilgili emsal davalar
- [Önceki dosya / sonuç / vekili]

### İç araştırma (Yarg MCP'den çekilenler)
- [Karar 1] `[Yarg MCP — daire — GG.AA.YYYY]` — [özet/eğilim]
- [Karar 2] — [...]
```

### 4. Dış vekilden talep ettiklerimiz

KRİTİK BÖLÜM — net olmalı, eksik kalmamalı:

```markdown
## Dış vekilden talepler

### Aksiyon (somut yapılacaklar)
1. [Cevap dilekçesi hazırla / itiraz dilekçesi sun / sulh teklifi cevapla / vs.]
2. [Tanık listesi öner]
3. [Bilirkişi seçim önerisi sun]
4. [Stratejik görüş ver]

### Sorularımız (cevap bekleniyor)
1. [Hukuki yorumlama sorusu]
2. [Strateji sorusu]
3. [Pratik soru — örn. "Sulh için hangi tutar makul olur?"]

### Hangi belge gönderildi (ek listesi)
- Ek 1: [...] (PDF/DOCX, sayfa sayısı)
- Ek 2: [...]
- Ek 3: [...]

### Cevap süresi
**Hangi tarihe kadar:** GG.AA.YYYY (en geç)
**Format:** Yazılı brief + Teams toplantı (önerilen) / sadece yazılı

### Bütçe
- Saatlik ücret: [TL/saat] — anlaşıldı
- Toplam tavan: [TL] — onaylı veya [Direktör/Başkan onayına gidecek]
- Aşma durumunda: önceden bilgi şart
```

### 5. Raporlama beklentisi

```markdown
## Raporlama disiplini ([ŞİRKET ADI] standardı)

- **Aylık rapor:** Her ayın 5'inde Excel formatında — dosya durumu, sonraki adım, yapılan iş saati, beklenen masraf
- **Acil bildirim:** Şu olaylar olduğunda derhal:
  - Karşı taraftan sulh teklifi
  - Mahkemenin önemli ara kararı
  - Bilirkişi raporu (aleyhe veya bize avantajlı)
  - Tarihsel duruşma günü değişikliği
  - Cevap süresinde kaçırma riski
- **Çıkar çatışması:** Yeni bir [ŞİRKET ADI] davası ile çakışma riski olursa derhal bildirin
- **KAP / yatırımcı etkili gelişme:** [HALKA AÇIK İŞTİRAK] ilgili tüm önemli gelişmeler derhal ([HALKA AÇIK İŞTİRAK] dosyalarında)
```

### ⚠️ ZORUNLU ÖN-KONTROL: TTK m. 5/A Zorunlu Arabuluculuk (ticari uyuşmazlıklarda)

**6102 sayılı TTK m. 5/A:** "Konusu bir miktar paranın ödenmesi olan alacak ve tazminat talepleri hakkında, dava açılmadan önce **arabulucuya başvurulmuş olması dava şartıdır**." (2018 değişikliği — 7155 sayılı K.)

**Kapsam:**
- ✅ Ticari uyuşmazlıklar (TTK m. 4 — mutlak/nispi ticari iş)
- ✅ Alacak + tazminat talepli davalar (vendor uyuşmazlığı, EPC, satım, lojistik)
- ❌ KAPSAM DIŞI: İhtiyati tedbir, ihtiyati haciz, geçici hukuki koruma; tüketici davaları; iş davaları (4857 İş K. m. 3 zorunlu arabuluculuk paraleli)

**[ŞİRKET ADI]/[HALKA AÇIK İŞTİRAK] için pratik:**
- Vendor 80M TL gibi büyük ticari uyuşmazlık → **dava açmadan önce arabuluculuk dava şartı**
- Arabuluculuk başlangıç: **Adalet Bakanlığı Arabuluculuk Daire Başkanlığı sistemi** üzerinden başvuru
- Süre: arabulucu atama 3 gün + ilk toplantı 3 hafta + tutanak 6 hafta tipik
- **Anlaşma sağlanırsa:** ilam niteliğinde icra edilebilir tutanak
- **Anlaşma sağlanmazsa:** "anlaşmama tutanağı" alınır → bu tutanak dava dilekçesine eklenir (yoksa dava reddi)

**Brief'te HBÖ'ye sorulacak:** "TTK m. 5/A zorunlu arabuluculuk için başvuru tarihi + arabulucu atama + müzakere stratejisi (sulh açılış teklifimiz) — dava dilekçesinden önce paralel hazırlık."

⚠️ **Bu adım atlanırsa dava reddi** (HMK m. 114 + TTK m. 5/A). Hızlı dava ihtiyacı varsa ihtiyati tedbir + arabuluculuk paralel.

### 6. [ŞİRKET ADI]-özel notlar

```markdown
## [ŞİRKET ADI]-özel notlar

- **Avukatlık K. m. 36 kapsamında gizlilik:** Bu brief ve tüm yazışmalar dahildir.
- **TBK m. 6 + TTK m. 18 ticari sır:** İhlal halinde tazminat sorumluluğu.
- **Ana ortak [ANA ORTAK] ile koordinasyon:** Stratejik dosyalarda Bakü ile bilgi paylaşımı yapılmadan önce onay alınmalı (intra-group işlemler).
- **EPDK lisans riski:** Karar EPDK lisansını etkileyebilir mi? Etkilemesi mümkünse derhal in-house Counsel'a bildirin.
- **Üst yönetim ismi:** Üst yönetim adının açıkça geçtiği bir gelişme olursa derhal CEO + Hukuk Başkanı bilgi.
- **Basın takibi:** Bu davanın basına yansıma olasılığı [yüksek/orta/düşük]. Basından bir gelişme olursa İletişim Başkanlığı ([İLETİŞİM BAŞKANI]) ile koordineli — kendi başınıza basına açıklama yapmayın.
```

### 7. Çıkar çatışması beyanı

```markdown
## Çıkar çatışması (vekil tarafından doldurulacak)

Bu brief'i kabul etmeden önce lütfen kontrol edin:
- Karşı taraf [...]: bürodaki başka avukatlar tarafından temsil ediliyor mu?
- Aynı kategorideki başka dava: ileride çatışma yaratır mı?
- Yatırımcılar arası: aktif hisse sahibi misiniz?

Yazılı çıkar çatışması beyanı brief'in kabulüyle birlikte alınır.
```

## TR Legal MCP — emsal araştırması

Brief hazırlanırken **mutlaka** karşı tarafın hukuki dayanağına ilişkin son emsal kararları çek:

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="<davanın hukuki konu>",
  daire="<ilgili daire>",
  baslangicTarihi="2023-01-01"
)
```

Bunları brief'in **"İç araştırma"** bölümünde özetle — dış vekilin işini hızlandırır.

## Çıktı şablonu (tek dosyalık PDF için)

```markdown
[ÜST BAŞLIK]

# DAVA BRIEF — [Esas No / Dosya Slug]

## ⚠️ İnceleyen notu (bu sayfa brief'in içinde değil, eşlik eden iç memo)
- **Hazırlayan:** [in-house Counsel]
- **İç onay:** [Hukuk Direktörü onayı tarihi]
- **Dış vekil seçimi:** [Büro] — [Pratik alan uygunluğu kontrolü]
- **Cevap süresi:** [tarih + kalan gün]
- **Bütçe onayı:** [tutar + onaylayan]

---

## 1. Genel bilgi
[başlık bölümü — esas no, taraflar, mahkeme, vs.]

## 2. Background
[olay özeti + timeline]

## 3. İç hukuk pozisyonu
[argümanlar + Yarg MCP'den çekilen emsal]

## 4. Dış vekilden talepler
[aksiyonlar + sorular + ekler + bütçe]

## 5. Raporlama disiplini
[[ŞİRKET ADI] standardı]

## 6. [ŞİRKET ADI]-özel notlar
[Avukatlık K. m. 36 + ticari sır + EPDK + üst yönetim + basın]

## 7. Çıkar çatışması beyanı
[vekil tarafından]

## Ekler
- Ek 1: [...]
- Ek 2: [...]

---

İletişim:
[Counsel adı]
[E-posta]
[Telefon]
KEP: [[ŞİRKET ADI] KEP adresi]
```

## Sonraki adımlar (decision tree)

```markdown
> **What next? Pick one and I'll help you build it out:**
> 1. **Brief'i PDF formatına çevir** ve KEP gönderim metni hazırla
> 2. **Hukuk Direktörü onay notu** — brief'in özet hali, onay imzası için
> 3. **Dış vekil seçim önerisi** — practice profile'dan 2-3 büro karşılaştırma
> 4. **Bütçe onay paketi** — Direktör/Başkan'a tutar onayı
> 5. **Brief tasarımı revize** — eksik bilgi var, şu soruları tekrar gözden geçirelim: [...]

**One question I'd ask that isn't in my checklist:** [örn. "Bu büronun karşı taraf veya karşı taraf vekiliyle daha önceki ilişkisi nedir? Reciprocal etkisi olabilir."]
```

## Reviewer note format

Brief hazırlanırken in-house Counsel'in **mutlaka bizzat okuduğu** belge olmalı — AI sadece taslak verir. Cevap kalitesi brief'in eksiksizliğine doğru orantılı.

---

## /litigation-legal:settlement-eval

---
name: settlement-eval
description: >
  Sulh teklifi geldiğinde veya verilecekken kapsamlı değerlendirme: tutar pencere
  analizi (TBK m. 53 destek tazminatı, AAÜT vekalet ücreti, yargılama masrafı,
  damga vergisi), risk-benefit matriksi, emsal sulh tutarları (Yarg MCP),
  eskalasyon kararı, müzakere paketi. [ŞİRKET ADI] sulh yetki matriksine entegre.
user-invocable: true
---

# Settlement Evaluation — Sulh Teklifi Değerlendirme

## Matter context

Aktif matter zorunlu — sulh tek bir davaya ait olur.

## Destination check

- **İç değerlendirme + Hukuk Direktörü onayı** → "GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ"
- **CEO/Başkan eskalasyon paketi** → "GİZLİDİR – CEO/BAŞKAN ONAYI İÇİN"
- **Karşı tarafa karşı sulh teklif metni** → üst başlık çıkar, "TASLAK" + dış vekil onayı sonrası

## Amaç

Sulh kararı en az 5 boyutta hesaplanır:

1. **Hukuki maruziyet** — eğer dava devam ederse muhtemel mahkeme kararı tutarı
2. **Maliyetler** — vekalet ücreti, yargılama gideri, dış vekil saatleri, içeride harcanan zaman
3. **Vergi/damga** — sulh anlaşmasının damga vergisi (DVK Tablo I)
4. **Reputational risk** — basın, müşteri algısı, çalışan moral
5. **Ekosistem etkisi** — emsal oluşturma riski, sektörde diğer dosyalar

## Adımlar

### 1. Karşı tarafın teklifini incele (veya kendi teklifimizi oluştur)

| Soru | Cevap |
|---|---|
| Karşı tarafın talebi (dava açılışındaki rakam) | [tutar] |
| Şu anda sunduğu sulh rakamı | [tutar] |
| **Düşüş %** | (talep - sulh) / talep × 100 |
| Talep edilen vade | peşin / taksit / koşullu |
| Eklenen koşullar | (gizlilik, ibra, ödül kabulü) |
| Vekalet ücreti dahil mi? | evet/hayır |
| Damga vergisi kim öder? | [açıkça yazılı mı?] |

Karşı taraftan gelen teklifte **gizli koşullar** olabilir (örn. "şirketin halka açıklaması yasak", "diğer çalışanlara öneri yapılmaz"). Bunlar hukukidan çok ticari/itibar etkisi taşır.

### 2. Hukuki maruziyet — kötümser senaryo

Eğer dava devam ederse, **muhtemel mahkeme kararı** ne olur?

- **Emsal Yargıtay/Danıştay kararları** (Yarg MCP):
```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="<dava konusu>",
  daire="<ilgili daire>",
  baslangicTarihi="2023-01-01"
)
```
- Kazanma olasılığı %
- Kaybedersek hangi tutarı ödemek zorundayız

**İSG kazasında tazminat hesabı (KRİTİK):**

| Kalem | Hesap |
|---|---|
| **Maddi zarar** (tedavi, kayıp ücret) | Belgeli, kesin |
| **Manevi tazminat** | Yargıtay HGK eğilim (genelde 50K-500K TL arası ölümlü kazada; ağırlık takdiri) |
| **Destek tazminatı (TBK m. 53)** | Yaşam süresi × destek oranı × pasif sermaye katsayısı (Yargıtay HGK 2017/123 metod) |
| **Faiz** | Yasal faiz (TBK + 3095 — değişken) |
| **Vekalet ücreti** | AAÜT (Türkiye Barolar Birliği) — genelde davacı vekiline %12-15 |
| **Yargılama gideri** | Bilirkişi, tanık masrafı |

**Toplam beklenen maruziyet:** [TL]

### 3. Maliyet hesabı (sulh yaparsa vs. devam ederse)

| Kalem | Sulh yaparsak | Dava devam ederse |
|---|---|---|
| Karşı tarafa ödeme | [sulh tutarı] | [muhtemel karar tutarı] |
| Karşı taraf vekalet (AAÜT) | dahil / hariç | %12-15 × karar tutarı |
| Dış vekil ücreti (bizim) | [bittiği tutar] | [tahmin: + N saat × saat ücreti] |
| Yargılama masrafı | yok | [bilirkişi, harç, posta] |
| Damga vergisi (DVK Tablo I) | sulh tutarı × ‰9,48 | yok (mahkeme kararı muaf — bkz. DVK m. 6) |
| İç zaman (in-house) | düşük | yüksek (her duruşma 1-2 gün) |
| **TOPLAM** | [...] | [...] |

⚠️ **Damga vergisi unutulmaz:** 5M TL sulh = ~47.400 TL damga. Sulh anlaşmasında "kim ödeyecek?" netleştirilmeli. Standart: yarı yarıya.

### 4. Reputational ve stratejik risk

- [ ] **Basına yansıma riski:** Dava devam ederse duruşma açık, basın takibi olabilir. Sulh ise gizlilik klozu eklenebilir.
- [ ] **Çalışan algısı (İSG davasında):** Düşük sulh = "şirket çalışana değer vermiyor" algısı; yüksek sulh = "şirket sorumluluk kabul ediyor" algısı.
- [ ] **Sendika etkisi ([SEKTÖR SENDİKASI]):** TİS müzakerelerinde geçmiş davalar argüman.
- [ ] **Yatırımcı algısı ([HALKA AÇIK İŞTİRAK]):** Yüksek tutarlı sulh KAP açıklaması gerektirebilir, hisse fiyatına etki.
- [ ] **Emsal oluşturma riski:** Bu sulhten sonra benzer davalar açılır mı? (örn. [İşletme Yeri]'da bir çalışana 5M TL sulh = diğer çalışan davaları için baseline)
- [ ] **Düzenleyici dikkat:** EPDK / Çevre Bakanlığı / SPK dikkatini çekebilir mi?

### 5. [ŞİRKET ADI] sulh yetki matriksi kontrolü

Practice profile → `## Eskalasyon ve onay matrisi` → sulh tutar kademelerine bak:

- < 500K TL → Counsel + Direktör
- 500K - 5M TL → Direktör onay, Başkan bilgi
- 5M - 50M TL → Başkan onay, CEO bilgi
- > 50M TL veya stratejik → CEO + YK

**Tutardan bağımsız eskalasyon kontrolü:**
- [ ] [HALKA AÇIK İŞTİRAK] ilgili mi? → KAP açıklama hazırlığı
- [ ] [İşletme Yeri] İSG kazası mı? → otomatik Başkan
- [ ] Üst yönetim ismi var mı? → CEO + YK
- [ ] Basına yansımış mı? → İletişim Başkanlığı koordinasyon

### 6. Müzakere stratejisi

Sulh kararı verildikten sonra **müzakere paketi:**

- **Yürürlüğe giriş ön-koşul** (örn. ibra mektubu, KAP onayı)
- **Ödeme takvimi** (peşin avantajlı mı, taksitli mi)
- **Gizlilik klozu** (genelde her iki tarafın talebi)
- **Karşılıklı feragat** (gelecekteki dava açma hakkı)
- **Cezai şart** (sulhe aykırı paylaşım için)
- **Vergi yansımaları** (KDV, stopaj, gelir vergisi — tarafların pozisyonu)
- **Yetki ve hukuk seçimi** (genelde Türk hukuku + İstanbul ATM)

### 7. Yazılı sulh anlaşması taslağı

Karar verildiyse:

```markdown
SULH ANLAŞMASI

Taraflar:
- [ŞİRKET ADI] A.Ş. ("[ŞİRKET ADI]")
- [Karşı taraf] ("Mağdur" / "Karşı Taraf")

Konu: [İhtilaf konusu]

Açıklamalar:
[önceki dava bilgisi, esas no, mahkeme]

Anlaşma maddeleri:
1. [ŞİRKET ADI], Mağdur'a [tutar] TL ödemeyi kabul eder; ödeme tarihi [tarih].
2. Mağdur, ödemenin alınmasının ardından [ŞİRKET ADI]'a karşı bu konudaki tüm taleplerinden feragat ettiğini ve ibra ettiğini beyan eder.
3. Bu anlaşma ve içeriği taraflarca gizli tutulacaktır; ihlali halinde [cezai şart] TL cezai şart ödenir.
4. Damga vergisi taraflarca yarı yarıya ödenir.
5. Uygulanacak hukuk: Türk hukuku. Yetki: [mahkeme/tahkim].

İmza:
[[ŞİRKET ADI] yetkilisi] _______
[Mağdur / vekili] _______
Tarih: GG.AA.YYYY
```

**Bu taslak DIŞ VEKİL ONAYINDAN GEÇMEDEN imzalanmaz.**

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Sulh Teklifi Değerlendirme — [Dosya slug]

## ⚠️ İnceleyen notu
- **Karar:** Sulh ÖNERİLİR / SULH ÖNERİLMEZ / Müzakere DEVAM
- **Önerilen sulh tutarı aralığı:** [TL min - TL max]
- **Eskalasyon noktası:** [Counsel/Direktör/Başkan/CEO]
- **Kaynaklar:** Yarg MCP [N emsal], Mevzuat MCP [X madde]
- **KAP açıklama:** [N/A / gerekli / hazırlanıyor]
- **Reviewer karar bekleyen:** N adet
- **Önerilen son aksiyon:** [1 cümle]

## Karşı tarafın teklifi

| Kalem | Değer |
|---|---|
| Talep edilen | [TL] |
| Sulh teklifi | [TL] (düşüş %X) |
| Vade | [...] |
| Gizlilik klozu | [...] |
| Vekalet ücreti dahil mi? | [...] |
| Damga vergisi | [...] |

## Hukuki maruziyet (kötümser senaryo)

**Emsal kararlar:** `[Yarg MCP — yargitay/danistay — GG.AA.YYYY]`

[tablo: emsal davanın özelliği, karar tutarı, bizim davaya benzerlik]

**Beklenen maruziyet:** [TL aralık] — [%] kazanma olasılığı

## Maliyet karşılaştırma

| Kalem | Sulh | Devam |
|---|---|---|
| ... | ... | ... |
| **TOPLAM** | [TL] | [TL] |

**Sulh net avantaj/dezavantaj:** [TL]

## Reputational ve stratejik

- Basın riski: [değerlendirme]
- Çalışan algısı: [değerlendirme] (İSG ise kritik)
- Yatırımcı ([HALKA AÇIK İŞTİRAK]): [değerlendirme + KAP gereği]
- Emsal oluşturma: [değerlendirme]
- Düzenleyici: [değerlendirme]

## Önerilen sulh tutarı

**Aralık:** [TL min] - [TL max]
**Hedef:** [TL]
**Yetkisi:** [Counsel/Direktör/Başkan/CEO seviyesinde — neden]

## Müzakere stratejisi

[Anahtar koşullar tablosu]

## Sonraki adımlar (decision tree)

> **What next? Pick one and I'll help you build it out:**
> 1. **Hukuk Direktörü eskalasyon notu** (sulh önerisi resmi)
> 2. **CEO/Başkan paket** (büyük tutar / stratejik dava ise)
> 3. **Müzakere paketi taslağı** — karşı tarafa karşı kontroffer
> 4. **Sulh anlaşması taslağı** — onaylandıysa, dış vekil revize için
> 5. **Bekle ve izle** — karşı taraf revize teklif yapsın

**One question I'd ask that isn't in my checklist:** [örn. "Karşı taraf vekiline kişisel bonus tarzı bir çıkar bağlanmış mı? Sulh oranını yapay yükseltebilir; geçmişte böyle pattern var mı?"]
```

## Reviewer note format

Reviewer note standardı — sulh kararı **kesinlikle dış vekil görüşü + Direktör onayı** olmadan finalize edilmez; AI çıktısı bağlayıcı önerme değildir.

---

