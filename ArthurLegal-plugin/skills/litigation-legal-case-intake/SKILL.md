---
name: litigation-legal-case-intake
description: >
  Yeni bir dava dosyası / ihtarname / dava açma kararı geldiğinde ön-değerlendirme:
  yargı yeri & görevli mahkeme tespiti (HMK), husumet, zamanaşımı, ön delil envanteri,
  ilk strateji önerileri, eskalasyon kararı. Dış vekil brief'i için temel oluşturur.
user-invocable: true
---

# Case Intake — Dava Ön-Değerlendirme

## Matter context

Practice-level CLAUDE.md `## Matter workspaces` bölümünü kontrol et. Litigation için matter workspaces **default ON**. Aktif matter yoksa:

> Bu yeni bir dava mı? `/arthurlegal:litigation-legal-case-intake` ile dosya aç (önerilen) veya `practice-level` cevapla. Aktif dosyada çalışırken dosya-spesifik `matter.md` öncelik kazanır.

## Destination check

Çıktının nereye gideceğini sor. Tipik destinasyonlar:
- **Dış vekil brief'i** → `[Dış vekil — büro adı]` etiketli, AVUKATLIK K. m. 36 üst başlığı
- **Hukuk Direktörü onayı** → "GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU" üst başlığı
- **İş birimi / yönetim bilgilendirme** → Quiet mode, hukuki jargon sadeleştir
- **Mahkemeye sunulacak dilekçe taslağı** → `/arthurlegal:litigation-legal-hearing-prep` skill'i daha uygun

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
- **Şirketler için yetki (m. 6/1 + TMK m. 51; şube işlemleri ve ortaklık/üyelik davaları için m. 14):** Şirket merkezi ([Müvekkil] için İstanbul)
- **Yetki sözleşmesi (HMK m. 17-18):** Yalnız tacirler veya kamu tüzel kişileri arasında ve yazılı yapılırsa geçerli; aksi kararlaştırılmadıkça dava yalnız seçilen mahkemede açılır
- **Tüketici davalarında (TKHK m. 73/5):** Tüketicinin yerleşim yerindeki tüketici mahkemesi de yetkili (seçimlik, kesin yetki değil; HMK m. 19 = yetki itirazının ileri sürülmesi)
- **İş davaları (7036 m. 6):** Davalının yerleşim yeri veya işin yapıldığı yer (iş kazası tazminatında kaza/zarar yeri ve işçinin yerleşim yeri de; aykırı yetki sözleşmesi geçersiz) ([TESİS LOKASYONU], Yalova, vs.)
- **Tahkim klozu (HMK m. 412 vd. + ISTAC/MTK kuralları):** Geçerliyse mahkeme yerine tahkim

**Görevli mahkeme:**
- Asliye Hukuk Mahkemesi — genel görevli
- Asliye Ticaret Mahkemesi (ATM) — TTK kapsamı (m. 4 — mutlak/nispi ticari iş)
- İş Mahkemesi — 4857 İş Kanunu uyuşmazlıkları
- Sulh Hukuk — kira, paylı mülkiyet
- Tüketici Hakem Heyeti — TKHK eşik altı

ArthurLegal MCP (`tr_`)'den HMK ve görevli mahkeme yönetmeliklerini çek, atıf et: `[ArthurLegal TR — GG.AA.YYYY]`.

### 3. Husumet (taraf sıfatı)

- **Aktif husumet:** Davayı açan taraf gerçekten davacı sıfatına sahip mi?
- **Pasif husumet:** Davalı olarak [Müvekkil] mi, yoksa bir bağlı şirket ([HALKA AÇIK İŞTİRAK], [RAFİNERİ], [Müvekkil] Enerji Ticaret, vs.)?
- **Tüzel kişilik perdesi:** Karşı taraf ana ortaktan değil de bağlı şirketten talepte bulunabilir mi?
- **[ÖZEL ENDÜSTRİ BÖLGESİ] özelliği:** [ÖZEL ENDÜSTRİ BÖLGESİ] içindeki tesisler ayrı tüzel kişiler — husumet doğru tespit edilmeli

Yanlış husumet → davanın reddi (taraf değişikliği, ek dava açma, zamanaşımı riski).

### 4. Zamanaşımı kontrolü (KRİTİK)

| Dava tipi | Zamanaşımı | Madde |
|---|---|---|
| Sözleşme aykırılığı (genel) | 10 yıl | TBK m. 146 |
| Ticari satım/hizmet sözleşme | 10 yıl; 5 yıl: dönemsel edimler, vekâlet/komisyon/acentelik ve (yüklenicinin ağır kusuru hariç) eser alacakları — TBK m. 147; satımda ayıp davaları devirden 2 yıl (satıcının ağır kusuru hariç) — TBK m. 231 | TBK m. 146-147, 231 |
| Haksız fiil tazminatı | 2 yıl (öğrenme) / 10 yıl (mutlak) | TBK m. 72 |
| **İSG kazası — bedensel zarar** | **2/10 + ceza zamanaşımı uzaması (TBK m. 72/1, 2. cümle)** | TBK m. 72 |
| İş davası — alacak (kıdem, ihbar, ücret) | **5 yıl** | İş K. m. 32 son fıkra (ücret) + Ek m. 3 (kıdem, ihbar, kötüniyet tazminatı, yıllık izin ücreti) |
| Vergi davası (vergi mahkemesi) | **30 gün** tebligattan | İYUK m. 7/1 |
| İdari işlem iptal (genel) | 60 gün | İYUK m. 7 |
| İstirdat (icra takibinde ödenen borç) | 1 yıl (ödeme tarihinden) | İİK m. 72/7 (menfi tespit için ayrı süre yok) |
| Marka ihlali (SMK) — tazminat | 2 yıl (öğrenme) / 10 yıl (fiil); fiil SMK m. 30 suçu ise daha uzun ceza zamanaşımı (TBK m. 72/1, 2. cümle) | SMK m. 157 → TBK m. 72 (5 yıl sessiz kalma yalnız hükümsüzlük için: SMK m. 25/6) |
| KVKK ihlali — Kurula şikâyet / tazminat | Şikâyet: veri sorumlusunun cevabının öğrenildiği tarihten itibaren 30 gün, her hâlde başvuru tarihinden itibaren 60 gün (önce veri sorumlusuna m. 13 başvurusu şart — m. 14/2); tazminat: genel hükümler (2/10 yıl) | KVKK m. 14 + TBK m. 72 |

⚠️ **ArthurLegal MCP (`tr_`)'den ilgili maddeyi çek ve atıfta bulun**. Zamanaşımı kullanıcı tarafından söylenmişse **önce doğrula** (no silent supplement).

### 5. Ön delil envanteri

- Hangi belgeler elimizde? (sözleşme, ihtarname, e-yazışma, KEP, fatura)
- Hangileri karşı tarafın elinde olabilir? (delil isteme — HMK m. 220)
- Tanık ihtiyacı? (HMK m. 240)
- Bilirkişi ihtiyacı? (HMK m. 266)
- Keşif? (HMK m. 288)

### 6. ArthurLegal MCP (`tr_`) — emsal içtihat ara

Karşı tarafın iddiasının hukuki dayanağı ne ise, **ArthurLegal MCP (`tr_`)'den** o konudaki son 2-3 yıl emsal Yargıtay/Danıştay kararını çek:

```
tr_ictihat_ara(
  query="<konu anahtar kelimeleri>",
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  date_from="2023-01-01"
)
```

Karşı tarafa olumlu mu, bize olumlu mu eğilim? Bir kaç emsal göster, atıfla: `[ArthurLegal MCP (`tr_`) — yargitay — GG.AA.YYYY]`.

### 6.5. TTK m. 5/A Zorunlu Arabuluculuk Kontrolü (ticari uyuşmazlıklar)

**6102 TTK m. 5/A:** Ticari davalardan konusu bir miktar para olan **alacak, tazminat, itirazın iptali, menfi tespit ve istirdat** davalarında dava açmadan önce **zorunlu arabuluculuk dava şartı** (7445 s. K. ile genişletilmiş hâli).

**Bu dosya kapsama giriyor mu?**
- [ ] Uyuşmazlık ticari dava mı? (TTK m. 4/1 — her iki tarafın ticari işletmesiyle ilgili nispi ticari dava veya taraflara bakılmaksızın m. 4/1-a–f mutlak ticari dava)
- [ ] Dava konusu bir miktar para mı (alacak, tazminat, itirazın iptali, menfi tespit veya istirdat)?
- [ ] Konu TTK m. 5/A dışında mı? (ihtiyati tedbir/haciz arabuluculuk beklenmeden istenebilir — HUAK m. 18/A/16; tüketici davası TKHK m. 73/A, iş davası 7036 m. 3 uyarınca KENDİ dava şartı arabuluculuğuna tabidir — iş kazası tazminatı hariç, 7036 m. 3/3)

**Kapsama giriyorsa:**
- Dava açmadan önce **Adalet Bakanlığı Arabuluculuk Daire Başkanlığı**'na başvur
- Arabulucu atama (3 gün) + ilk toplantı (3 hafta) + tutanak (6 hafta tipik)
- Anlaşma → ilam niteliğinde icra edilebilir
- Anlaşmama → son tutanak dava dilekçesine eklenir; eklenmemişse mahkeme 1 haftalık kesin süre verir, sunulmazsa usulden ret; hiç başvurulmamışsa doğrudan usulden ret (HUAK m. 18/A/2)

**büro pratiği:**
- Vendor 80M TL gibi büyük ticari talepte zorunlu
- Paralel olarak ihtiyati tedbir gerekiyorsa (HMK m. 389 vd.) tedbir tek başına dava açılabilir, ana dava arabuluculuk sonrası
- Sulh teklifi açılış stratejisi `/arthurlegal:litigation-legal-settlement-eval` skill ile birlikte düşünülmeli

⚠️ Yanlışlıkla atlanırsa **dava şartı yokluğu nedeniyle dava reddi** — ek 6 hafta + ek vekalet ücreti maliyeti.

### 7. sektöre-özel kontroller

Bu listeden geçir, gereken eskalasyonu tetikle:

- [ ] **halka açık iştirak ilgili mi?** → KAP açıklama kontrolü gerekli mi? (`${CLAUDE_PLUGIN_ROOT}/references/kap-esirket-webfetch-rehberi.md`)
- [ ] **[TESİS LOKASYONU] İSG kazası mı?** → `/arthurlegal:litigation-legal-isg-incident-response` skill'i ÇOK DAHA UYGUN
- [ ] **EPDK lisansını etkiliyor mu?** → Compliance + EPDK ön-incelemesi
- [ ] **OFAC/AB yaptırım listesi karşı taraf?** → Compliance + Hukuk Başkanı, devam etme
- [ ] **[BORU HATTI PROJESİ] / hükümetlerarası anlaşma alanı?** → Dış hukuk panel + üst yönetim
- [ ] **Üst yönetim ismi sanık?** → CEO + YK bilgi
- [ ] **Basına intikal etmiş veya etme riski?** → İletişim Başkanlığı ([İletişim Başkanlığı]) koordinasyon
- [ ] **Yabancı hukuk / yabancı mahkeme-tahkim ayağı var mı?** → Uyuşmazlık yabancı hukuk yönetimliyse (İngiliz/NY hukuku) veya bir **yabancı mahkeme kararı Türkiye'de tanıma-tenfiz** gerektiriyorsa: MÖHUK 5718 (m. 50 vd. tenfiz, m. 58 vd. tanıma) uygulanır; yabancı hakem kararı için New York Konvansiyonu (`${CLAUDE_PLUGIN_ROOT}/references/istac-rehberi.md`). İngiliz statüsü → `${CLAUDE_PLUGIN_ROOT}/references/uk-legislation-rehberi.md` (legislation.gov.uk WebFetch); ABD statüsü/içtihatı → `${CLAUDE_PLUGIN_ROOT}/references/us-legislation-rehberi.md` (GovInfo) + `${CLAUDE_PLUGIN_ROOT}/references/courtlistener-rehberi.md`. Yönlendirme: `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`. Yabancı hukukun kesin yorumu için dış yabancı-hukuk uzmanı flag et.

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
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [✓ N emsal / ✗]; ArthurLegal MCP (`tr_`) [✓ X madde / ✗]
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

**Önerilen:** [mahkeme] — HMK m. [X] kapsamında. `[ArthurLegal TR — GG.AA.YYYY]`
**Alternatif/itiraz mümkün:** [varsa]

## Husumet

- Aktif husumet: [değerlendirme]
- Pasif husumet: [Müvekkil] mi, yoksa [bağlı şirket]? `[review]`

## Zamanaşımı

- **Hesaplanan zamanaşımı tarihi:** GG.AA.YYYY (kalan: N gün)
- **Dayanak:** [TBK/TTK/İş K. madde] — `[ArthurLegal TR — GG.AA.YYYY]`
- **Risk:** [yorum]

## Ön delil envanteri

| Delil | Bizde mi? | Gerekli? | Not |
|---|---|---|---|
| [...] | ✓/✗ | ✓ | [...] |

## Emsal içtihat (ArthurLegal MCP (`tr_`))

| Karar | Tarih | Daire | Eğilim | Bizim için |
|---|---|---|---|---|
| [esas/karar no] | [...] | [...] | bize/aleyhe/karma | [yorum] `[ArthurLegal MCP (`tr_`) — yargitay — GG.AA.YYYY]` |

## sektöre-özel kontroller

- [ ] [halka açık iştirak] KAP: [N/A veya açıklanan]
- [ ] [TESİS LOKASYONU] İSG: [N/A veya yönlendir]
- [ ] EPDK lisans riski: [yok/var]
- [ ] Yaptırım: [yok/var]
- [ ] Üst yönetim sanık: [yok/var]
- [ ] Basın riski: [yok/var]

## Şiddet ataması: [emoji]

[Gerekçe]

## Önerilen sonraki adımlar (decision tree)

> **What next? Pick one and I'll help you build it out:**
> 1. **Dış vekil brief'i hazırla** — bu dosyayı `/arthurlegal:litigation-legal-outside-counsel-brief` ile [büro] için briefle
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
- **Karşı taraf vekili tanıdık ama dosya tanımıyor** → "Bu vekille daha önce yaşadığımız başka davalar var mı? `/arthurlegal:litigation-legal-case-intake list` ile bakayım?"
- **Zamanaşımı çok yakın** → 🔴 + büyük uyarı: "⚠️ Zamanaşımı [X] gün içinde doluyor. Bu dava açma kararı **bu hafta** verilmeli."
- **Tahkim klozu var ama mahkemede dava açıldı** → 🟠 + "Tahkim itirazı (HMK m. 116/1-b) cevap dilekçesinde sunulmalı (m. 117/1); aksi halde itiraz dinlenemez."

---

## Kaynak katmani — /legal-research (v1.4.0)

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur —
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| Turk doktrini (DergiPark 19 hukuk dergisi) + karsilastirmali ogreti — **ikincil**; bir karar kademesini yukseltmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| uyusmazlik AZ hukukuna tabiyse akt + statu. **AZ ictihadi bu araclarda YOK** — `azerbaycan-hukuk-rehberi.md` | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
