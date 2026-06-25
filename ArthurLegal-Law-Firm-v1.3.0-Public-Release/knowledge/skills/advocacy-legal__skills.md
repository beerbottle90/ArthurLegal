# advocacy-legal - Skill Referans Kitapcigi

> Alan: Dava dilekcesi uretimi (ozel/kamu/ceza) + yazihane asistanligi
> Toplam skill: 5
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.
> Aktif entite: Tum skill'ler company-profile.md -> Bolum 0 'Aktif entite' secimini baz alir
> (varsayilan: [Şirket/Büro adı] -> Bolum A). Cikti dili / onay zinciri / yargi cevresi buradan gelir.

## Icindekiler

- /advocacy-legal:ceza-dilekce (123 satir)
- /advocacy-legal:cold-start-interview (43 satir)
- /advocacy-legal:kamu-hukuku-dilekce (149 satir)
- /advocacy-legal:ozel-hukuk-dilekce (173 satir)
- /advocacy-legal:yazihane-asistani (91 satir)

---

## /advocacy-legal:ceza-dilekce

---
name: ceza-dilekce
description: >
  Ceza muhakemesi (CMK 5271) dilekçesi ÜRETİMİ — suç duyurusu/şikayet (m.158),
  katılma/müştekilik (m.237), şüpheli/sanık savunması, tutuklamaya/adli kontrole
  itiraz (m.267-268), KYOK'a itiraz (m.173), esas hakkında savunma, istinaf
  (m.272+, 7 gün), temyiz (m.286+), CMK m.141 koruma tedbiri tazminatı. Örnek senaryolar:
  iş kazası (TCK taksir + 6331), çevre suçu, bilişim, kaçakçılık — müşteki veya
  çalışan müdafii desteği.
user-invocable: true
---

# Ceza Dilekçesi Üretimi (CMK)

> Bu skill ceza muhakemesi **dilekçe/beyan metnini** üretir. **Kurumsal/in-house bağlam:** şirket genelde **müşteki/katılan** (örn. hırsızlık, bilişim, dolandırıcılık, ekipman/altyapı sabotajı) veya **çalışan/yönetici müdafiine destek** (iş kazası TCK m.85/89 taksir, çevre TCK m.181-182). **Sanık müdafiliği baroya kayıtlı avukat işidir** — in-house counsel destek/taslak üretir, fiili müdafilik için dış ceza avukatı + [Baş Hukuk Müşaviri] onayı.

## ⏰ ÖN-KONTROL — SÜRE (her çalıştırmada)

| İşlem | Süre | Dayanak |
|---|---|---|
| **İstinaf** (ilk derece hükme karşı) | **7 gün** (tefhim/tebliğ) | CMK m.273 |
| **Temyiz** (BAM kararına karşı) | **15 gün** (tebliğ) | CMK m.291 |
| **İtiraz** (tutuklama/adli kontrol/KYOK vb.) | **7 gün** | CMK m.268 |
| **KYOK'a itiraz** (Sulh Ceza Hâkimliği) | **15 gün** (tebliğ) | CMK m.173 |
| **Şikayet** (şikayete bağlı suçlar) | **6 ay** (fail+fiili öğrenme) | TCK m.73 |
| Koruma tedbiri **tazminatı** (m.141) | karar kesinleşmesinden **3 ay / her halde 1 yıl** | CMK m.142 |

Kalan < 2 gün (7 günlük sürelerde) → 🔴. Süreler kesin; kaçırma = hak kaybı.

## ADIM 1 — Evre + rol + dilekçe tipi

**Evre:** Soruşturma (Cumhuriyet Başsavcılığı) → İddianame/KYOK → Kovuşturma (mahkeme).

| Rolümüz | Dilekçe/işlem | Madde |
|---|---|---|
| Mağdur/müşteki (şirket suçtan zarar gören) | **Suç duyurusu / şikayet dilekçesi** | CMK m.158 / TCK m.73 |
| Müşteki | **Katılma (müdahale) talebi** | CMK m.237-239 |
| KYOK verildi | **KYOK'a itiraz** (Sulh Ceza Hâkimliği) | CMK m.173 |
| Şüpheli/sanık (çalışan-yönetici) | **Savunma / sorgu beyanı / esas hakkında savunma** | CMK m.147, m.191 |
| Tutuklama/adli kontrol | **Tahliye talebi / itiraz** | CMK m.104, m.267-268 |
| Aleyhe hüküm | **İstinaf dilekçesi** | CMK m.273 |
| Aleyhe BAM kararı | **Temyiz dilekçesi** | CMK m.291 |
| Haksız koruma tedbiri | **m.141 tazminat davası** (Ağır Ceza) | CMK m.141 |

## ADIM 2 — Görevli/yetkili mahkeme + uzlaştırma süzgeci

- **Görev:** Asliye Ceza (genel) / **Ağır Ceza** (TCK'da üst sınırı 10 yıl+ suçlar, örn. nitelikli yağma, kasten öldürme) / Sulh Ceza Hâkimliği (soruşturma koruma tedbirleri + KYOK itirazı).
- **Yetki:** suçun işlendiği yer (CMK m.12) — santral/saha ili.
- **Uzlaştırma (CMK m.253):** uzlaştırma kapsamındaki suçlarda (örn. taksirle yaralama, mala zarar, güveni kötüye kullanma) **soruşturma/kovuşturma şartı**; kapsamı kontrol et. Şirket müşteki ise uzlaşma kabul/ret stratejisi.

## ADIM 3 — Maddi olay + suç vasfı + delil

- **Olay:** somut, tarih/yer/kişi; iş kazasında olay yeri/SGK/iş müfettişi raporu, çevre olayında ölçüm/tutanak.
- **Suç vasfı (müşteki isek):** TCK'daki karşılığı (örn. m.142 nitelikli hırsızlık, m.157-158 dolandırıcılık, m.243-244 bilişim, m.151-152 mala zarar). Savunma isek: kast/taksir ayrımı, kusurun bulunmadığı/iştirak/illiyet.
- **Delil:** tutanak, kamera, bilirkişi (CMK m.62-73), tanık, SGK/iş müfettişi/ÇŞB raporu, dijital delil. **CMK m.130** — savunma hakkı kapsamında dosya erişimi (müdafi sıfatı gerekir).

## ADIM 4 — Emsal (TR Legal MCP)

```
search_bedesten_unified(phrase="<suç + somut konu>",
  birimAdi="<ilgili Yargıtay CD, örn. 12. CD (taksirle ölüm), 15. CD, 11. CD>",
  kararTarihiStart="2021-01-01")
```
Yalnızca çekileni işle: `[Yargı MCP — Yargıtay 12.CD — Esas/Karar — GG.AA.YYYY]`.

## ADIM 5 — Dilekçe taslakları

**(a) Suç duyurusu / şikayet (müşteki — [Müvekkil / Şirket]):**
```markdown
[YER] CUMHURİYET BAŞSAVCILIĞI'NA

ŞİKAYETÇİ/MÜŞTEKİ : [Müvekkil / Şirket] — [VKN], [adres]
VEKİLİ            : Av. [ad], [baro/sicil], [KEP]
ŞÜPHELİ           : [varsa kimlik / "tespit edilecek"]
SUÇ               : [örn. hırsızlık TCK m.141-142 / bilişim sistemine girme m.243 /
                    mala zarar m.151] [şikayete bağlıysa: süresi içinde]
SUÇ TARİHİ/YERİ   : GG.AA.YYYY — [santral/saha]

OLAYLAR           : [kronolojik somut anlatım + delil atfı]
DELİLLER          : kamera kaydı (EK), tutanak, bilirkişi, tanık, [SGK/ÇŞB raporu]
HUKUKİ NEDENLER   : TCK m.[...], CMK `[Mevzuat MCP — GG.AA.YYYY]`
TALEP             : Şüpheli/şüpheliler hakkında soruşturma başlatılmasına, gerekli
                    koruma/delil tedbirlerine, kamu davası açılmasına karar verilmesini
                    ve şikayetçi/müşteki sıfatımızın kabulünü saygıyla talep ederiz.
                                                  GG.AA.YYYY — Vekil Av. [ad]
EKLER: vekaletname, deliller
```

**(b) Esas hakkında savunma / istinaf (savunma — çalışan-yönetici müdafiine destek):** sanığın kimliği, isnat, **lehe deliller + kast/taksir-kusur değerlendirmesi + illiyet bağı + iştirak** + emsal beraat/HAGB; istinafta hükmün özeti + bozma/kaldırma sebepleri (eksik inceleme, hukuka aykırı delil, vasıf hatası, ceza tayini).

## ADIM 6 — Sektörel/örnek senaryolar kontrolleri

- [ ] **İş kazası (santral/saha)** → TCK m.85/89 taksir + 6331; paralel **iş mahkemesi tazminat** + **idari (SGK/iş müfettişi)** dosyaları → `/litigation-legal` ile üçlü-paralel koordinasyon. İSG ilk müdahale: `/litigation-legal:isg-incident-response`.
- [ ] **Çevre olayı** → TCK m.181-182 + 2872 idari ceza paralel.
- [ ] **Sanık müdafiliği** → baroya kayıtlı (dış) avukat şart; in-house destek üretir.
- [ ] **Üst yönetim/YK adı geçiyor** → [Baş Hukuk Müşaviri] + [Genel Müdür]; basın riski → iletişim koordinasyon.
- [ ] **CMK m.130 dosya erişimi** → müdafi sıfatı yoksa tam erişim yok; hatırlat.

## Çıktı

```markdown
[ÜST BAŞLIK]
# Ceza Dilekçesi — [tip] — [dosya/soruşturma no]

## ⚠️ İnceleyen notu
- **Evre/rol:** [soruşturma/kovuşturma] — [müşteki/savunma]
- **Süre:** [işlem] son tarih GG.AA.YYYY (kalan N gün) 🔴/🟠/🟡
- **Görev/uzlaştırma:** [mahkeme] · uzlaştırma [kapsamda/değil]
- **Kaynaklar:** Mevzuat MCP [✓/✗]; Yargı MCP (CD) [✓ N / ✗]
- **Onay:** dış ceza avukatı + [Baş Hukuk Müşaviri] şart (sanık müdafiliğinde zorunlu)

## Dilekçe taslağı
[doldurulmuş]

## Sonraki adımlar
> 1. **Dış ceza avukatı brief** — `/litigation-legal:outside-counsel-brief`
> 2. **İSG paralel dosyalar** — `/litigation-legal:isg-incident-response` (iş kazası)
> 3. **Tazminat ayağı** — `/advocacy-legal:ozel-hukuk-dilekce` (iş mahkemesi/haksız fiil)
> 4. **Süre/duruşma takvimi** — `/advocacy-legal:yazihane-asistani`
> 5. **Başka**

**One question I'd ask:** [örn. "Bu iş kazası dosyasında SGK/iş müfettişi raporu kusur dağılımını nasıl belirledi? Ceza, tazminat ve idari dosyalardaki kusur tezimiz tutarlı olmalı."]
```

---

## /advocacy-legal:cold-start-interview

---
name: cold-start-interview
description: >
  advocacy-legal eklentisini ilk kez kuran kullanıcı için kısa röportaj —
  kullanıcı rolü ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri] / diğer), dilekçe
  üretim tercihleri, onay/eskalasyon, dış vekil dağılımı, varsayılan çıktı modu.
  CLAUDE.md profilini doldurur. `--redo` ile yeniden çalışır.
user-invocable: true
---

# advocacy-legal — Cold Start Interview

Amaç: Bu eklentinin `CLAUDE.md` profilindeki `[DOLDUR]` alanlarını kullanıcıyla 5-8 soruda doldurmak. Önce knowledge'daki `company-profile.md` ([Şirket/Büro adı]) okunur — şirket bilgisi oradan gelir, burada **tekrar sorulmaz**.

## Akış

### Adım 0 — Bağlamı oku
- `company-profile.md` ([Şirket/Büro adı]) + bu plugin `CLAUDE.md`'yi oku. Zaten dolu alanları tekrar sorma; yalnızca `[DOLDUR]` olanları sor.

### Adım 1 — Kullanıcı kim?
> 1. Adın ve rolün? (örn. **[Baş Hukuk Müşaviri]** — Baş Hukuk Müşaviri / **[Kıdemli Hukuk Müşaviri]** — Senior Legal Counsel / **[Hukuk Müşaviri]** — Junior Legal Counsel / diğer)
> 2. Baroya kayıtlı avukat mısın, yoksa hukuk müşaviri/legal counsel mı? (vekaletname/imza yetkisi farkı için)
> 3. Doğrudan amirin? (varsayılan: [Baş Hukuk Müşaviri])

### Adım 2 — Dilekçe üretim tercihleri
> 4. Hangi dilekçe tiplerini en çok üretiyorsun? (özel hukuk HMK / idari İYUK / ceza CMK / karma)
> 5. Dilekçe taslakları **dış vekil revizesi öncesi mi** (in-house first-draft) yoksa **doğrudan sunum için mi** üretilecek? (onay zinciri buna göre)
> 6. Varsayılan çıktı: tam dilekçe metni mi, yoksa önce iskelet/argüman haritası mı?

### Adım 3 — Onay ve dış vekil
> 7. Yüksek tutarlı/stratejik dilekçelerde onay eşiği? (tutar veya "her istinaf/temyiz/AYM" gibi)
> 8. Dış vekil paneli (ticari / idari-Danıştay / ceza / tahkim) — büro adları varsa.

### Adım 4 — Yaz ve onayla
- Cevapları `CLAUDE.md`'deki ilgili `[DOLDUR]` alanlarına işle (kullanıcıya özetini göster, onay al, sonra yaz).
- Matter workspace kullanımı (dilekçe dosya-bazlı) açık mı? Varsayılan: açık.

## Çıktı
Kısa özet + güncellenen `CLAUDE.md` alanları listesi + "Artık `/advocacy-legal:ozel-hukuk-dilekce`, `:kamu-hukuku-dilekce`, `:ceza-dilekce`, `:yazihane-asistani` komutlarını kullanabilirsin." yönlendirmesi.

## Notlar
- `--redo`: tüm alanları yeniden sor.
- Bu eklenti **kurumsal in-house** içindir; kullanıcı serbest avukatlık bağlamı tarif ederse, çıktı başlıklarını ona göre uyarlamayı öner ama varsayılan in-house kalır.

---

## /advocacy-legal:kamu-hukuku-dilekce

---
name: kamu-hukuku-dilekce
description: >
  Kamu (idari/anayasa) hukuku dilekçesi ÜRETİMİ — idari dava dilekçesi (İYUK m.3:
  iptal + tam yargı), yürütmenin durdurulması (m.27), istinaf BİM (m.45), temyiz
  Danıştay (m.46), AYM bireysel başvuru (6216, 30 gün). Süre haritası (m.7: 60/30,
  ÇED 30 m.20/A), görevli mahkeme (İdare Mah./Danıştay ilk derece). Örnek senaryolar:
  EPDK Kurul kararı iptali, ÇED ret/itiraz, idari para cezası, tam yargı tazminat.
user-invocable: true
---

# Kamu Hukuku Dilekçesi Üretimi (İYUK + AYM)

> Bu skill idari/anayasa yargısı **dilekçe metnini** üretir. Görevli mahkeme/süre/strateji *tespiti* için `/administrative-legal:idari-dava-prep` (önce onu çalıştırmak güçlü olur); bu skill tespiti alıp **dilekçeyi yazar**. Her taslak **dış idari avukat + [Baş Hukuk Müşaviri] onayı** ile sunulur.

## ⏰ ÖN-KONTROL — SÜRE (her çalıştırmada, HAK DÜŞÜRÜCÜ)

| İşlem | Süre | Dayanak |
|---|---|---|
| İdare mahkemesi iptal davası | **60 gün** (tebliğ/öğrenme) | İYUK m.7 |
| **Vergi** mahkemesi davası | **30 gün** | İYUK m.7 (tax-legal) |
| **ÇED** kararı (RES/HES/jeotermal) | **30 gün** — m.20/A ivedi yargılama (BİM YOK, doğrudan Danıştay temyiz **15 gün**) | İYUK m.20/A |
| İstinaf (BİM) | **30 gün** | İYUK m.45 |
| Temyiz (Danıştay) | **30 gün** (ÇED ivedi: 15 gün) | İYUK m.46 / m.20/A |
| **AYM bireysel başvuru** | **30 gün** (kesinleşmeden/öğrenmeden) | 6216 m.47/5 |
| Üst makama başvuru (m.11) | 60 gün içinde; cevap/zımni ret sonrası dava süresi işler | İYUK m.11 |

⚠️ **m.11 üst makama başvuru ÇED ivedi yargılama süresini DURDURMAZ.** Kalan < 5 gün → 🔴.

## ADIM 0 — Görevli mahkeme (kritik; idari-dava-prep ile teyit)

Türk idari yargı **3 dereceli**: İdare Mahkemesi → BİM → Danıştay (temyiz). **Danıştay ilk derece sadece istisnada** (Danıştay K. m.24): CB Kararı/kararnamesi, bakanlık/kurum **genel tebliğ/yönetmeliği** (normatif düzenleyici işlem).
- **EPDK bireysel Kurul kararı (lisans iptali/ceza/ret)** → **Ankara İdare Mahkemesi** (kurum Ankara) → BİM → Danıştay 13. Daire (temyiz)
- **EPDK/bakanlık genel yönetmelik/tebliğ** → doğrudan **Danıştay** (ilk derece)
- **ÇED ret/«ÇED gerekli değildir» iptali** → yer İdare Mahkemesi (projenin ili) → m.20/A ivedi → Danıştay 10./14. Daire
- **İdari para cezası (ÇŞB/EPDK/Rekabet)** → İdare Mahkemesi (idari yaptırımın türüne göre; bazı cezalar sulh ceza/idare ayrımı — kontrol)

## ADIM 1 — Dava türü ve dilekçe tipi

| Talep | Tür | Not |
|---|---|---|
| İdari işlemin **iptali** | İptal davası (İYUK m.2/1-a) | + yürütmeyi durdurma (m.27) |
| İdari işlem/eylemden **zarar tazmini** | Tam yargı davası (m.2/1-b) | iptal ile birlikte veya ayrı |
| Aleyhe ilk derece kararı | İstinaf dilekçesi (m.45) | BİM |
| Aleyhe BİM kararı | Temyiz dilekçesi (m.46) | Danıştay |
| İç hukuk tükendi + temel hak ihlali | **AYM bireysel başvuru** (6216) | 30 gün |

## ADIM 2 — İptal sebepleri (yetki/şekil/sebep/konu/maksat)

Klasik beş sakatlık (her birini somutla):
- **Yetki:** İdare/Kurul bu işlemi yapma yetkisinde mi? (görev gaspı, fonksiyon/yer/zaman yetkisizliği)
- **Şekil:** usul kuralları (gerekçe, savunma hakkı, oybirliği/çoğunluk, süre, ilan) — EPDK soruşturmasında savunma alınmış mı?
- **Sebep:** dayanılan maddi/hukuki sebep gerçek ve doğru mu?
- **Konu:** işlemin sonucu kanuna aykırı mı?
- **Maksat:** kamu yararı dışında amaç (örtülü amaç)?

## ADIM 3 — Yürütmenin durdurulması (İYUK m.27 — KRİTİK)

Talep şart, otomatik gelmez. **İki şart birlikte:**
1. **Telafisi güç/imkansız zarar:** EPDK lisans askısı → üretim duruşu → günlük X TL gelir kaybı; ÇED ret → yatırım dondurma; idari ceza tahsili.
2. **Açıkça hukuka aykırılık:** en güçlü iptal sebebi.
→ Dilekçede ayrı başlık. (İYUK m.20/A ivedi yargılamada YD rejimi özeldir — tek dilekçe, kısa süreler.)

## ADIM 4 — Emsal (TR Legal MCP)

```
search_bedesten_unified(phrase="<konu> iptal yürütmenin durdurulması",
  birimAdi="13. Daire" /* EPDK/Rekabet */ veya "10. Daire"/"14. Daire" /* ÇED/çevre */,
  kararTarihiStart="2022-01-01")
search_rekabet_kurumu_decisions / search_kik_v2_decisions / search_kvkk_decisions  /* kurum birincil */
```
Yalnızca çekileni dilekçeye işle: `[Yargı MCP — Danıştay 13.D — Esas/Karar — GG.AA.YYYY]`.

## ADIM 5 — İdari dava dilekçesi taslağı (İYUK m.3 zorunlu unsurlar)

```markdown
[GÖREVLİ MAHKEME] BAŞKANLIĞI'NA
[örn. ANKARA NÖBETÇİ İDARE MAHKEMESİ / DANIŞTAY ( ) DAİRESİ BAŞKANLIĞI'NA]
                                         — YÜRÜTMENİN DURDURULMASI TALEPLİDİR —

DAVACI            : [Müvekkil / Şirket] — [VKN], [adres]
VEKİLİ            : Av. [ad], [baro/sicil], [KEP]
DAVALI            : [T.C. EPDK / Çevre, Şehircilik ve İklim Değişikliği Bakanlığı / ...]
D. KONUSU         : Davalı idarenin [GG.AA.YYYY tarih, [...] sayılı] [Kurul kararı/işlemi]
                    nın İPTALİ ile öncelikle YÜRÜTMENİN DURDURULMASI [ve uğranılan
                    [tutar] TL zararın tam yargı olarak tazmini] talebidir.
TEBLİĞ/ÖĞRENME    : GG.AA.YYYY → dava süresi [60/30] gün → son tarih GG.AA.YYYY

I. OLAYLAR (idari süreç kronolojisi, işlemin tarif ve tarih/sayısı)

II. HUKUKA AYKIRILIK NEDENLERİ
  A. Yetki yönünden  B. Şekil/usul yönünden (savunma hakkı/gerekçe)
  C. Sebep yönünden  D. Konu yönünden  E. Maksat yönünden
  [her biri + emsal: [Yargı MCP — Danıştay …]]

III. YÜRÜTMENİN DURDURULMASI (İYUK m.27)
  1. Telafisi güç/imkansız zarar [somut: üretim/lisans/gelir]
  2. Açıkça hukuka aykırılık [en güçlü sebep]

IV. [TAM YARGI — varsa zarar kalemleri ve hesap]

HUKUKİ SEBEPLER   : 2577 İYUK, 6446 EPDK/Elektrik Piyasası K., 2872 Çevre K.,
                    ilgili yönetmelikler `[Mevzuat MCP — GG.AA.YYYY]`
DELİLLER          : Dava konusu işlem ve tebliği (EK), idari dosya (m.20 ara kararı
                    ile celbi talebi), bilirkişi, keşif, her tür yasal delil.

SONUÇ VE TALEP    : 1. Öncelikle yürütmenin durdurulmasına,
                    2. Dava konusu işlemin iptaline,
                    3. [Tazminata,] 4. Yargılama gideri + vekalet ücretinin
                    davalı idareye yükletilmesine karar verilmesini arz/talep ederiz.
                                                          GG.AA.YYYY — Davacı Vekili
EKLER: 1. Vekaletname  2. İşlem/tebliğ örneği  3. ...
```

> İstinaf/temyiz dilekçesinde: kararın özeti + bozma/kaldırma sebepleri (hukuka aykırılık + eksik inceleme) + YD talebi. **AYM bireysel başvuruda:** resmi başvuru formu, ihlal edilen Anayasa/AİHS hakkı (mülkiyet m.35, adil yargılanma m.36), olağan yolların tüketildiği, 30 gün, esasa etki/anayasal önem ölçütü.

## ADIM 6 — Sektörel/örnek senaryolar kontrolleri

- [ ] **EPDK lisans askısı/iptali riski** → derhal [Baş Hukuk Müşaviri] + [Genel Müdür]; üretim/gelir etkisi YD gerekçesi
- [ ] **ÇED ivedi yargılama (m.20/A)** → BİM yok, süreler kısa (30/15 gün) — takvime işle
- [ ] **HES su kullanım (DSİ) / orman izni** paralel dava → süre/merci ayrı kontrol
- [ ] **Rekabet/KVKK Kurulu kararı** → ilgili Daire (13.) + kurum birincil karar emsali
- [ ] **Finansör/kreditör ilgili veya yüksek etki** → eskalasyon + (gerekirse) ESG/PS bağlamı

## Çıktı

```markdown
[ÜST BAŞLIK]
# Kamu Hukuku Dilekçesi — [tip] — [işlem]

## ⚠️ İnceleyen notu
- **Görevli mahkeme:** [tespit] (gerekçe) `[review]`
- **Süre:** son tarih GG.AA.YYYY (kalan N gün) — [60/30/15/AYM 30] 🔴/🟠/🟡
- **Yürütmeyi durdurma:** [evet — gerekçe]
- **Kaynaklar:** Mevzuat MCP [✓/✗]; Yargı MCP (Danıştay/kurum) [✓ N / ✗]
- **Onay:** dış idari avukat + [Baş Hukuk Müşaviri] şart

## Dilekçe taslağı
[doldurulmuş]

## Sonraki adımlar
> 1. **idari-dava-prep ile strateji teyidi** — `/administrative-legal:idari-dava-prep`
> 2. **EPDK proaktif görüş** (dava yerine dialog şansı) — `/administrative-legal:epdk-proaktif-gorus`
> 3. **Dış idari avukat brief** — `/litigation-legal:outside-counsel-brief`
> 4. **Süre/duruşma takvimi** — `/advocacy-legal:yazihane-asistani`
> 5. **Başka**

**One question I'd ask:** [örn. "İşlem kesinleşmeden önce m.11 üst makama başvuru ile çözüm denenmeli mi? ÇED ivedi rejiminde süreyi durdurmaz; bunu bilerek karar vermeliyiz."]
```

---

## /advocacy-legal:ozel-hukuk-dilekce

---
name: ozel-hukuk-dilekce
description: >
  Özel hukuk (HMK 6100) dava dilekçesi ÜRETİMİ — dava dilekçesi (m.119), cevap
  dilekçesi (m.129), replik/düplik, istinaf (m.341+, 2 hafta), temyiz (m.361+),
  ihtiyati tedbir (m.389). Görevli/yetkili mahkeme, TTK m.5/A zorunlu arabuluculuk
  dava şartı, zamanaşımı, deliller, emsal içtihat (TR Legal MCP). Örnek senaryolar:
  EPC/vendor ticari, tazminat, alacak, tespit, iş davası (işveren), HES su/ecrimisil.
user-invocable: true
---

# Özel Hukuk Dilekçesi Üretimi (HMK)

> Bu skill dava **dilekçe metnini** üretir. Dava *stratejisi/ön-değerlendirmesi* için `/litigation-legal:case-intake`. Her taslak **dış vekil + Baş Hukuk Müşaviri ([Baş Hukuk Müşaviri]) onayı** ile sunulur.

## ⏰ ÖN-KONTROL — SÜRE (her çalıştırmada)

| Dilekçe | Süre | Dayanak |
|---|---|---|
| **Cevap dilekçesi** | **2 hafta** (tebliğden) — bir defaya mahsus 1 ay ek süre (m.127) | HMK m.127 |
| Replik (davacı cevaba cevap) | 2 hafta | HMK m.136 |
| Düplik (davalı ikinci cevap) | 2 hafta | HMK m.136 |
| **İstinaf** | **2 hafta** (gerekçeli karar tebliği) | HMK m.345 |
| **Temyiz** | **2 hafta** (BAM kararı tebliği) | HMK m.361 |
| İstinaf/temyiz **cevap** | 2 hafta | HMK m.347/m.366 |
| Bilirkişi raporuna itiraz | 2 hafta | HMK m.281 |

Kalan < 5 gün → 🔴 ACİL (dış vekille derhal koordine). Süre hak düşürücü/kesin — kaçırma = hak kaybı.

⚠️ Cevap süresi **dava dilekçesinin tebliğinden** işler; tensiple verilen süreyi teyit et.

## Destination check

- **Mahkemeye sunulacak dilekçe** → üst başlık YOK; en üste `TASLAK – DIŞ VEKİL/BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN SUNMAYINIZ`
- **İç değerlendirme / Baş Hukuk Müşaviri onayı** → `GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU`
- **Dış vekile revize için** → `DAVA BRIEF – AVUKATLIK K. m. 36 KAPSAMINDA`

## ADIM 1 — Dilekçe tipini ve rolü belirle

| Rolümüz | Tip | Not |
|---|---|---|
| Davacı (biz açıyoruz) | **Dava dilekçesi** (HMK m.119) | + gerekirse ihtiyati tedbir (m.389) |
| Davalı (bize açıldı) | **Cevap dilekçesi** (HMK m.129) | süre kritik |
| Davacı | Replik (cevaba cevap) | yeni vakıa/itiraz |
| Davalı | Düplik | |
| Aleyhe karar | **İstinaf dilekçesi** (m.342) | BAM |
| Aleyhe BAM kararı | **Temyiz dilekçesi** (m.361) | Yargıtay |

## ADIM 2 — Görevli ve yetkili mahkeme (dava dilekçesi ise)

**Görev (kesin, re'sen):**
- **Asliye Ticaret Mahkemesi (ATM)** — TTK m.4 mutlak/nispi ticari iş (EPC, vendor, tedarik, toptan satış uyuşmazlığı) — dosyaların çoğu
- Asliye Hukuk — genel
- İş Mahkemesi — 4857 (işçi-işveren; santral/saha personeli)
- Sulh Hukuk — kira, paylı/elbirliği mülkiyet
- Tüketici Mahkemesi/Hakem Heyeti — TKHK (nadir)

**Yetki (HMK):**
- Genel: davalı yerleşim yeri (m.6) / şirket merkezi (m.14)
- Sözleşmesel yetki klozu (m.17 — tacirler arası geçerli) → öncelik
- Haksız fiil: fiilin işlendiği/zararın doğduğu yer (m.16)
- Taşınmaz (HES/arazi/ecrimisil): taşınmazın bulunduğu yer (m.12) — **kesin yetki**

`[Mevzuat MCP]` ile teyit. Yanlış görev/yetki → görevsizlik/yetkisizlik kararı + gönderme (m.20); süre korunsa da gecikme/masraf.

## ADIM 3 — TTK m.5/A zorunlu arabuluculuk (DAVA ŞARTI)

Konusu **alacak veya tazminat** olan **ticari uyuşmazlıkta** dava açmadan önce **zorunlu arabuluculuk** (dava şartı).
- [ ] Ticari iş mi (TTK m.4)? [ ] Talep para alacağı/tazminat mı? [ ] Kapsam dışı mı? (ihtiyati tedbir/haciz tek başına açılabilir)
- Kapsama giriyorsa: arabuluculuk **anlaşmama tutanağı** dava dilekçesi ekinde olmalı; yoksa **dava şartı yokluğundan usulden ret** (HMK m.114/m.115).

> İş davaları (7036) ve tüketici davaları için de ayrı zorunlu arabuluculuk rejimi vardır — kontrol et.

## ADIM 4 — Zamanaşımı / hak düşürücü süre

| Talep | Süre | Madde |
|---|---|---|
| Sözleşmeye aykırılık (genel) | 10 yıl | TBK m.146 |
| Ticari satım/eser/hizmet | 5 yıl (eser m.147) / 10 yıl | TBK m.147/146 |
| Haksız fiil tazminatı | 2 yıl (öğrenme) / 10 yıl (mutlak) | TBK m.72 |
| İş alacağı (kıdem/ihbar/ücret) | 5 yıl | 4857 / TBK |
| Ecrimisil | 5 yıl geriye | Yargıtay içtihadı |

Kullanıcı zamanaşımı tarihi verdiyse **önce doğrula** (no silent supplement).

## ADIM 5 — Vakıa + hukuki sebep + delil iskeleti

- **Vakıalar:** kronolojik, somut, tarih/sayı/tutar ile. Her vakıaya bağlanacak delil.
- **Hukuki sebepler:** ilgili TBK/TTK/HMK maddeleri — `[Mevzuat MCP]` ile metni çek.
- **Deliller (HMK m.119/1-f):** sözleşme, ihtarname, e-yazışma/KEP, fatura, ticari defterler (TTK m.222), tanık (m.240), bilirkişi (m.266), keşif (m.288), yemin. **Somutlaştırma yükü** (m.194) — her delili hangi vakıa için gösterdiğini belirt.

## ADIM 6 — Emsal içtihat (TR Legal MCP)

```
search_bedesten_unified(phrase="<uyuşmazlık konusu anahtar kelimeler>",
  birimAdi="<ilgili Yargıtay HD, örn. 11. HD/15. HD/9. HD>", kararTarihiStart="2022-01-01")
```
Lehte/aleyhte eğilimi göster, dilekçeye **yalnızca çekilen** kararı işle: `[Yargı MCP — Yargıtay X.HD — Esas/Karar — GG.AA.YYYY]`. **Uydurma içtihat yazma.**

## ADIM 7 — Dilekçe taslağı (HMK m.119 zorunlu unsurlar)

```markdown
[NÖBETÇİ/İLGİLİ] ... MAHKEMESİ SAYIN HAKİMLİĞİ'NE
[ATM ise: ... ASLİYE TİCARET MAHKEMESİ'NE]

DAVACI            : [Müvekkil / Şirket] — [VKN], [adres]
VEKİLİ            : Av. [ad soyad], [baro] Baro sicil [no], [KEP/adres]
DAVALI            : [ad/unvan] — [adres]
KONU              : [örn. fazlaya ilişkin haklar saklı kalmak kaydıyla
                    [tutar] TL alacağın/tazminatın temerrüt faiziyle tahsili] talebidir.
HARCA ESAS DEĞER  : [tutar] TL
ARABULUCULUK      : [Anlaşmama tutanağı tarih/no — EK-1] (TTK m.5/A)

AÇIKLAMALAR
1. [Vakıa — kronolojik, delil atfı] (EK-...)
2. [Vakıa ...]
...
[Karşı tarafın temerrüdü / ihlal / zarar — somut]

HUKUKİ SEBEPLER   : TBK m. [...], TTK m. [...], HMK ve ilgili mevzuat.
                    `[Mevzuat MCP — GG.AA.YYYY]`
DELİLLER          : Sözleşme (EK-...), ihtarname (EK-...), e-yazışma/KEP,
                    fatura, ticari defterler (TTK m.222), bilirkişi, tanık,
                    keşif, yemin ve her türlü yasal delil.
EMSAL             : [Yargı MCP — Yargıtay X.HD — Esas/Karar — GG.AA.YYYY] (varsa)

SONUÇ VE TALEP    : Yukarıda açıklanan nedenlerle;
  1. Fazlaya ilişkin haklarımız saklı kalmak kaydıyla [tutar] TL'nin
     [temerrüt/avans faizi] ile davalıdan tahsiline,
  2. Yargılama giderleri ve vekalet ücretinin davalıya yükletilmesine,
  karar verilmesini saygıyla vekaleten talep ederiz. GG.AA.YYYY

                                              Davacı Vekili
                                              Av. [ad soyad] [imza/e-imza]
EKLER: 1. Vekaletname  2. Arabuluculuk anlaşmama tutanağı  3. Sözleşme  4. ...
```

> Cevap dilekçesinde: davaya/yetkiye/göreve **ilk itirazlar** (HMK m.116 — kesin/sözleşmesel yetki itirazı, tahkim itirazı, derdestlik), zamanaşımı def'i, vakıaların ayrı ayrı cevabı (m.129/c — inkar/kabul/bilmeme), karşı deliller.

## ADIM 8 — Sektörel/örnek senaryolar kontrolleri

- [ ] **EPC/vendor uluslararası** → governing law/tahkim klozu var mı? (ICC/LCIA) → `/commercial-legal:governing-law-review`; varsa Türk mahkemesinde **tahkim ilk itirazı** (m.116/c)
- [ ] **HES su kullanım / ecrimisil / kamulaştırma** → taşınmaz kesin yetki + DSİ/idare tarafı varsa idari yargı ayrımı (`/advocacy-legal:kamu-hukuku-dilekce`)
- [ ] **Yaptırım taraflı / finansör-kreditör ilgili / yüksek tutar** → [Baş Hukuk Müşaviri] + [Genel Müdür] eskalasyon
- [ ] **İş davası** → işyeri (santral/saha ili) yetki + arabuluculuk (7036)

## Çıktı

```markdown
[ÜST BAŞLIK — destination'a göre]

# Özel Hukuk Dilekçesi — [tip] — [dosya/konu]

## ⚠️ İnceleyen notu
- **Kaynaklar:** Mevzuat MCP [✓ N madde / ✗]; Yargı MCP [✓ N emsal / ✗]
- **Süre:** [dilekçe tipi] son tarih GG.AA.YYYY (kalan: N gün) 🔴/🟠/🟡
- **Görev/yetki:** [mahkeme] — HMK m.[X] `[review]`
- **Arabuluculuk dava şartı:** [N/A / tutanak EK-1 var / gerekli]
- **Reviewer bekleyen [review]:** N madde
- **Onay:** dış vekil + [Baş Hukuk Müşaviri] (Baş Hukuk Müşaviri) onayı şart

## Dilekçe taslağı
[doldurulmuş şablon]

## Sonraki adımlar
> 1. **Dış vekil revizesi** — `/litigation-legal:outside-counsel-brief`
> 2. **İhtiyati tedbir** ekle (HMK m.389) — gerekiyorsa
> 3. **Emsal güçlendir** — TR Legal MCP'den ek karar
> 4. **Yazıhane** — süre/duruşma takvimine işle `/advocacy-legal:yazihane-asistani`
> 5. **Başka**

**One question I'd ask:** [örn. "Karşı tarafla aktif bir EPC/çerçeve sözleşme ilişkisi sürüyor mu? Sürüyorsa dilekçe tonu/talep yapısı ticari ilişkiyi koruyacak şekilde kalibre edilmeli."]
```

---

## /advocacy-legal:yazihane-asistani

---
name: yazihane-asistani
description: >
  Hukuk yazıhanesi / in-house hukuk birimi iş akışı asistanı — süre & duruşma
  takvimi (HMK/İYUK/CMK süreleri otomatik hesap), dava dosyası özeti, gelen-giden
  evrak listesi, dilekçe/ek kontrol listesi, harç & gider avansı hesabı, vekaletname/
  yetki kontrolü, UYAP/e-tebligat takibi, müvekkil/iş birimi bilgilendirme notu.
  Şirket/büro hukuk biriminin günlük operasyonu için.
user-invocable: true
---

# Yazıhane Asistanı

> Şirket/büro Hukuk birimi ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri]) günlük iş akışı için. Dilekçe ÜRETİMİ değil; dosyaları **organize, takip ve raporlama**. Hukuki içerik gerektiren çıktılarda `/advocacy-legal:*-dilekce` veya `/litigation-legal:*` skill'lerine yönlendir.

## Ne için kullanılır (menü)

Kullanıcı ne istediğini söylemezse sor: aşağıdakilerden hangisi?

1. **Süre & duruşma takvimi** — tarih ver, kalan günleri ve kritik eşikleri çıkar
2. **Dosya özeti** — bir davanın 1 sayfalık durumu
3. **Evrak / ek kontrol listesi** — bir dilekçe/başvuru için ek envanteri
4. **Harç & gider avansı hesabı** — yaklaşık tutar
5. **Vekaletname / yetki kontrolü** — yetki kapsamı yeterli mi
6. **UYAP / e-tebligat takibi** — ne yapılmalı, neyi teyit et
7. **Müvekkil / iş birimi bilgilendirme notu** — hukuk dışı okuyucu için sade durum

## 1) Süre & duruşma takvimi

Kullanıcı tebliğ/tefhim/karar tarihini verir; uygula:

| Yargı | Tipik süreler |
|---|---|
| **HMK (özel)** | Cevap 2 hafta (m.127, +1 ay ek) · replik/düplik 2 hafta · bilirkişi itiraz 2 hafta (m.281) · istinaf 2 hafta (m.345) · temyiz 2 hafta (m.361) |
| **İYUK (idari)** | İlk dava 60 gün (vergi 30; ÇED 30 m.20/A) · istinaf 30 gün (m.45) · temyiz 30 gün (ÇED 15) |
| **CMK (ceza)** | İstinaf 7 gün (m.273) · temyiz 15 gün (m.291) · itiraz 7 gün (m.268) · KYOK itiraz 15 gün (m.173) |
| **AYM bireysel** | 30 gün (6216 m.47/5) |
| **İcra/İİK** | itiraz 7 gün · şikayet 7 gün · istihkak süreleri |

Çıktı: tarih satırı + **son tarih + kalan gün + renk (🔴<5 / 🟠<10 / 🟡<20 / 🟢)**. Hafta sonu/resmi tatil son güne denk gelirse **sonraki iş günü** (HMK m.93). Süreyi kullanıcı verdiyse **mevzuattan teyit et** (no silent supplement); emin değilsen ilgili rehbere bak (`references/hmk-rehberi.md` / `iyuk-rehberi.md` / `cmk-rehberi.md`).

```markdown
| Dosya | İşlem | Tetik tarihi | Süre | SON TARİH | Kalan | Durum |
|---|---|---|---|---|---|---|
| [esas no] | Cevap dilekçesi | 12.06.2026 (tebliğ) | 2 hafta | 26.06.2026 | 1 gün | 🔴 |
```

## 2) Dosya özeti (1 sayfa)

Kullanıcı dosya/yığın yüklerse: taraflar · mahkeme/esas no · dava konusu/talep · aşama (tensip/ön inceleme/tahkikat/karar/istinaf) · son işlem · **bir sonraki kritik tarih** · dış vekil · risk/şiddet (🔴🟠🟡🟢) · bekleyen aksiyon. "Okuma kapsamı"nı belirt; tamamını okumadıysan söyle.

## 3) Evrak / ek kontrol listesi

Dilekçe tipine göre standart ekler:
- **HMK dava:** vekaletname · arabuluculuk anlaşmama tutanağı (ticari alacak/tazminat) · sözleşme/ihtarname · deliller · harç/gider avansı dekontu
- **İdari dava:** vekaletname · dava konusu işlem + tebliğ örneği · (varsa m.11 başvuru) · idari dosya celp talebi
- **Ceza:** vekaletname/müdafi görevlendirme · deliller · (müşteki) zarar belgeleri
- Eksikleri 🔴/🟡 işaretle.

## 4) Harç & gider avansı (yaklaşık)

- **Nispi harç:** konusu para olan davalarda dava değeri üzerinden (peşin ¼) — güncel **Harçlar Kanunu (492) tarifesi** `[Mevzuat MCP / doğrulayın]`
- **Maktu harç:** idari dava, tespit, bazı davalarda
- **Başvurma harcı** + **gider avansı** (HMK m.120 — tebligat/bilirkişi/keşif için tarifeyle)
- ⚠️ Tutarları **güncel tarifeden teyit et**; tahmini ver ve `[doğrulayın]` etiketle. Vekalet ücreti için **AAÜT** (Türkiye Barolar Birliği).

## 5) Vekaletname / yetki kontrolü

Yapılacak işlem için vekaletnamede özel yetki gerekiyor mu? (örn. **davadan feragat, kabul, sulh, tahkim, ahzu kabz, temyiz/istinaftan feragat** → HMK m.74 özel yetki). Şirket imza sirküleri + **[Baş Hukuk Müşaviri] imza yetkisi** ile uyum. Eksik yetki → 🔴 + "işlem öncesi vekaletname güncellensin".

## 6) UYAP / e-tebligat takibi

- e-Tebligat (7201 + UYAP) → tebliğ tarihi süreyi başlatır; **tebliğ tarihini teyit et**.
- UYAP'tan derkenar/ara karar/bilirkişi raporu indi mi? Dış vekil portal erişimi kimde?
- Yapılacaklar listesi + teyit edilecek tarih. (Asistan UYAP'a bağlanmaz; **ne yapılacağını** söyler.)

## 7) Müvekkil / iş birimi bilgilendirme notu

Hukuk dışı okuyucu ([Genel Müdür] / iş birimi) için: ne oldu · ne anlama geliyor · ne yapıyoruz · ne gerekiyor (karar/imza/bilgi) · sonraki tarih. Jargon sadeleştir; gizli ise üst başlık koru.

## Çıktı ilkeleri

- Süreyi yanlış hesaplamak = hak kaybı: emin değilsen **hesaplama varsayımını yaz** ve `[doğrulayın]`.
- Bu skill **takip ve organizasyon**; hukuki argüman/strateji başka skill'lerin işi.
- Tekrarlayan/periyodik takip gerekiyorsa kullanıcıya **takvim/hatırlatıcı** kurmasını öner (asistan kalıcı hatırlatma tutmaz).

## Sonraki adımlar (tipik)
> 1. **Dilekçe üret** — `/advocacy-legal:ozel-hukuk-dilekce` / `:kamu-hukuku-dilekce` / `:ceza-dilekce`
> 2. **Dava ön-değerlendirme** — `/litigation-legal:case-intake`
> 3. **Dış vekil brief** — `/litigation-legal:outside-counsel-brief`
> 4. **Başka**

---
