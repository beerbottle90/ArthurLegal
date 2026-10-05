# contract-drafting - Skill Referans Kitapcigi

> Alan: Sozlesme uretimi - redline, belge turet, versiyon karsilastir, tadil
> Toplam skill: 5
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.
> Aktif entite: Tum skill'ler company-profile.md -> Bolum 0 'Aktif entite' secimini baz alir
> (varsayilan: [Şirket/Büro adı] -> Bolum A). Cikti dili / onay zinciri / yargi cevresi buradan gelir.

## Icindekiler

- /contract-drafting:belge-turet (83 satir)
- /contract-drafting:cold-start-interview (40 satir)
- /contract-drafting:redline-contract (88 satir)
- /contract-drafting:tadil-protokol (77 satir)
- /contract-drafting:versiyon-karsilastir (64 satir)

---

## /contract-drafting:belge-turet

---
name: belge-turet
description: >
  Örnek/emsal bir belgeden (şablon) yeni sözleşme/protokol TÜRETİR — şablonun yapısını
  çıkarır, yeni işin parametreleriyle uyarlar, doldurulacak alanları [DOLDUR] işaretler,
  TBK/TTK emredici hüküm + standart klozlar ile uyumlar. Tipik: süre uzatım
  protokolü, EPC/PPA/vendor sözleşmesi, NDA, hissedar/JV, kredi tadili.
user-invocable: true
---

# Şablon / Emsalden Belge Türetme

> Elindeki bir örnek belgeden (önceki bir sözleşme, standart şablon, emsal protokol) **yeni bir belge** üretir. Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı.

## ADIM 0 — Girdi

1. **Şablon/emsal belge** — kullanıcı yapıştırsın/yüklesin (yoksa: hangi belge tipini istediğini sor, standart iskeletle başla).
2. **Yeni işin parametreleri** — taraflar, konu, tutar/süre, özel şartlar, fark eden noktalar.
3. **Hangi tip?** EPC · PPA/elektrik satış · vendor/tedarik · NDA · hissedar/JV · kredi/finansman · **süre uzatım/ek protokol** · diğer.

## ADIM 1 — Şablonu analiz et

- **Yapı haritası:** bölüm/madde başlıkları (başlangıç hükümleri, tanımlar, edimler, bedel/ödeme, süre, mücbir sebep, sorumluluk, gizlilik, fesih, uyuşmazlık, ekler).
- **Değişken alanlar:** şablondaki örneğe-özgü değerler (taraf adı, tarih, tutar, proje) → yeni parametrelerle değişecek.
- **Sabit/standart klozlar:** korunacak (boilerplate) ama şirket standardıyla kıyasla.

## ADIM 2 — Yeni belgeyi üret

- Yapıyı koru; değişken alanları yeni parametrelerle doldur; bilinmeyenleri **`[DOLDUR — ...]`** bırak.
- **Standart klozları** ekle/teyit et (mücbir sebep TBK m.136/138, sınırlı sorumluluk, yaptırım/uyum, KVKK, EPDK lisans/devir, uyuşmazlık, damga vergisi).
- **Emredici hüküm kontrolü:** şablondaki bir kloz emredici kurala aykırıysa düzelt + flag (`[Mevzuat MCP — GG.AA.YYYY]`). (Örn. tüketici/iş sözleşmesinde aleyhe kloz, fahiş cezai şart TBK m.182.)
- Şablon eski tarihliyse: **mevzuat değişikliği** kontrolü (atıflar güncel mi?).

## ADIM 3 — Değişiklik notu

Yeni belgenin şablondan **nerede ayrıldığını** açıkça listele: hangi alanlar dolduruldu, hangi klozlar eklendi/çıkarıldı, hangi `[DOLDUR]` kaldı.

## Örnek: süre uzatım protokolü

```markdown
[ANA SÖZLEŞME ADI] – SÜRE UZATIM PROTOKOLÜ (Ek Protokol No: [N])

Taraflar: [Müvekkil / Şirket] ([adres/VKN]) ile [Karşı Taraf]
Ana Sözleşme: GG.AA.YYYY tarihli [sözleşme adı] ("Ana Sözleşme")

1. KONU: İşbu Protokol, Ana Sözleşme'nin [süre maddesi no] maddesinde düzenlenen
   süreyi uzatmak amacıyla akdedilmiştir.
2. SÜRE UZATIMI: Ana Sözleşme'nin süresi [yeni bitiş tarihi]'ne kadar uzatılmıştır.
   [Gerekçe: mücbir sebep / iş artışı / mutabakat — TBK m.136 atfı varsa]
3. BEDEL/ŞARTLAR: [değişen bedel veya "bedel/şartlar aynen geçerlidir"]
4. SAKLILIK: Ana Sözleşme'nin işbu Protokol'le değiştirilmeyen tüm hükümleri
   aynen yürürlüktedir.
5. YÜRÜRLÜK: İşbu Protokol imza tarihinde yürürlüğe girer; Ana Sözleşme'nin ayrılmaz
   ekidir. Damga vergisi: [DOLDUR — DVK kontrolü].
Tarih / İmzalar: [Müvekkil / Şirket] (yetkili: [imza yetkilisi]) — [Karşı Taraf]
```

## Çıktı
```markdown
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN İMZALANMAZ

# Türetilen Belge — [tip] — [taraflar]

## ⚠️ İnceleyen notu
- **Şablon:** [kaynak emsal] · **Tip:** [...]
- **Doldurulan / [DOLDUR] kalan:** N / N
- **Eklenen standart klozlar:** [liste]
- **Emredici hüküm/güncellik düzeltmesi:** [N adet] `[Mevzuat MCP]`
- **Onay:** Baş Hukuk Müşaviri + dış vekil şart

[yeni belge metni]

## Şablondan farklar
[liste]

## Sonraki adımlar
> 1. **Redline incele** — `/contract-drafting:redline-contract` ile son kontrol
> 2. **[DOLDUR] alanlarını tamamla** — eksik parametreler
> 3. **Governing law / yaptırım** — yabancı taraf varsa
> 4. **Başka**

**One question I'd ask:** [örn. "Bu emsal hangi işten geldi? O işe özgü taviz/özel kloz varsa yeni belgeye sessizce taşımayalım."]
```

---

## /contract-drafting:cold-start-interview

---
name: cold-start-interview
description: >
  contract-drafting eklentisini ilk kez kuran kullanıcı için kısa röportaj — rol,
  birincil ortam (Claude.ai Projects / Claude Code), varsayılan çıktı formu (redline
  görünümü / temiz+liste / tablo), standart klozlar/şablonlar, onay zinciri.
  CLAUDE.md profilini doldurur. `--redo` ile yeniden çalışır.
user-invocable: true
---

# contract-drafting — Cold Start Interview

Amaç: `CLAUDE.md` profilindeki `[DOLDUR]` alanlarını 5-7 soruda doldurmak. Önce `company-profile.md` + `references/redline-konvansiyonlari-rehberi.md` okunur.

## Akış

### Adım 0 — Bağlam
`company-profile.md` + bu plugin `CLAUDE.md` oku. Dolu alanları tekrar sorma.

### Adım 1 — Kullanıcı & ortam
> 1. Adın/rolün? ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri] / diğer)
> 2. Birincil ortam: **Claude.ai Projects** (markdown redline) mı, **Claude Code/VS Code** (gerçek .docx tracked-changes) mı? — çıktı yeteneğini belirler.

### Adım 2 — Çıktı tercihi
> 3. Varsayılan redline formu: (a) redline görünümü, (b) temiz revize + değişiklik/comment listesi, (c) yapılandırılmış tablo, (d) her seferinde sor.
> 4. Comment'lerde fallback pozisyon her zaman yer alsın mı? (önerilen: evet)

### Adım 3 — Şablon & onay
> 5. Sık kullandığın şablon/emsal türleri? (EPC, PPA/elektrik satış, vendor/tedarik, NDA, kredi/finansman, hissedar/JV, süre uzatım protokolü)
> 6. Standart klozlar (mücbir sebep, sınırlı sorumluluk, yaptırım/uyum, uyuşmazlık, EPDK devir, KVKK) varsayılan eklensin mi?
> 7. İmza öncesi onay eşiği? (varsayılan: Baş Hukuk Müşaviri; yüksek tutar/stratejik + Genel Müdür)

### Adım 4 — Yaz ve onayla
Cevapları `CLAUDE.md` `[DOLDUR]` alanlarına işle (özet göster, onay al, yaz). Matter workspace açık mı? Varsayılan: açık.

## Çıktı
Kısa özet + güncellenen alanlar + "Artık `/contract-drafting:redline-contract`, `:belge-turet`, `:versiyon-karsilastir`, `:tadil-protokol` kullanabilirsin." yönlendirmesi.

## Not
`--redo`: tüm alanları yeniden sor.

---

## /contract-drafting:redline-contract

---
name: redline-contract
description: >
  Yüklenen sözleşmeyi inceleme bulgularına göre REDLINE'la — değişiklikleri belgeye
  ekleme/silme + comment olarak işler, 3 çıktı formundan birinde teslim eder.
  commercial-legal inceleme akışıyla bütünleşir (vendor/NDA/SaaS/governing-law).
  Claude.ai Projects: markdown redline görünümü; Claude Code: gerçek .docx tracked-changes.
  TBK/TTK + standart (EPC/PPA/vendor/SHA) fallback pozisyonları.
user-invocable: true
---

# Sözleşme Redline (incele → belgeye uygula)

> Bu skill **bulguları belgeye uygular**. Henüz inceleme yapılmadıysa önce `/commercial-legal:review` (veya ilgili review skill'i) çalıştır; sonra bulguları buraya getir. Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı ile imzalanır.

## ADIM 0 — Girdi & ortam & form

1. **Belge var mı?** Kullanıcı sözleşme metnini yapıştırsın/yüklesin. "Okuma kapsamı"nı belirt; tamamını okumadıysan söyle.
2. **Bizim kağıt mı, karşı tarafın kağıdı mı?** (redline yönü/agresifliği değişir)
3. **Ortam:** Claude.ai Projects → **markdown redline**; Claude Code → **gerçek .docx tracked-changes** (python-docx) opsiyonu.
4. **Çıktı formu (sor):**
   - (a) **Redline görünümü** — madde içinde ~~silinen~~ / **eklenen** + comment dipnotları
   - (b) **Temiz revize + değişiklik/comment listesi**
   - (c) **Yapılandırılmış tablo** — `madde | mevcut | önerilen | gerekçe | severity`

## ADIM 1 — Bulguları topla / üret

Inceleme bulgusu varsa al; yoksa playbook'a göre çıkar (sözleşme tipini tespit et → `references/` + `commercial-legal` profili + `company-profile.md` standart pozisyonları). Her bulgu için:
- **Sorun** (kloz + neden) · **Severity** (🔴🟠🟡🟢) · **Önerilen redline** (somut metin) · **Fallback** ("tercih X; kabul edilmezse asgari Y") · **Hukuki dayanak** (`[Mevzuat MCP]` emredici hüküm / `[Yargı MCP]` kloz geçerliliği).

**Standart kontrol listesi (enerji sözleşmesi):**
- Mücbir sebep + aşırı ifa güçlüğü (TBK m.136/138) — şebeke kısıtı, mevzuat değişikliği, kuraklık (HES)
- Sınırlı sorumluluk / cezai şart (TBK m.179-182 — fahiş ceza tenkisi)
- Yaptırım & uyum klozu (OFAC/AB/BM/OFSI + **uluslararası finans kuruluşu dışlama listesi**) — `references/yaptirim-tarama-rehberi.md`
- Uyuşmazlık & uygulanacak hukuk (Türk mah. vs ICC/LCIA) — `/commercial-legal:governing-law-review`
- **EPDK lisans/pay devri ön-onayı** (6446) — kontrol değişikliği klozu
- KVKK (6698) veri işleme/aktarım · gizlilik · fikri mülkiyet
- Damga vergisi / vergi gross-up · ödeme/teminat (akreditif, teminat mektubu)
- Devir/temlik · değişiklik (tadil) · fesih · süre/yenileme

## ADIM 2 — Redline'ı üret (seçilen form)

**Form (a) — Redline görünümü (Projects varsayılanı):**
```markdown
**Madde 12.3 (Mücbir Sebep)**
Taraflar, ~~savaş, grev ve doğal afet~~ **mücbir sebep hâllerinde (TBK m.136 anlamında, şebeke
operatörü kaynaklı kesinti ve mevzuat değişikliği dâhil)** edimlerini ~~7 gün~~ **30 gün** içinde
yerine getiremezse...
> 💬 [Av. — 🟠] Mücbir sebep tanımı dar; şirket için şebeke/regülasyon riskini kapsamalı.
>     Tercih: TBK m.136 atfı + açık liste. Kabul edilmezse asgari: "şebeke kesintisi" eklensin.
```

**Form (b) — Temiz revize + liste:** temiz metin (değişiklikler uygulanmış) + ayrı tablo:
```markdown
| # | Madde | Değişiklik | Gerekçe | Severity |
|---|---|---|---|---|
| 1 | 12.3 Mücbir sebep | tanım genişletildi + 30 gün | şebeke/regülasyon riski | 🟠 |
```

**Form (c) — Yapılandırılmış tablo:** `madde | mevcut | önerilen | gerekçe | severity` (uygulamayı kullanıcı yapar).

> **Claude Code yolu:** python-docx ile `w:del`/`w:ins` (yazar="[Şirket/Büro adı] Hukuk", tarih) + `w:comment` üretip `<dosya>_redline.docx` döndürülebilir. Projects'te bu üretilemez → markdown redline + "Word'de Track Changes açıkken uygula" notu.

## ADIM 3 — Çıktı

```markdown
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN İMZALANMAZ

# Redline — [sözleşme adı] — [karşı taraf]

## ⚠️ İnceleyen notu
- **Belge / okuma kapsamı:** [tip, N sayfa okundu]
- **Kağıt:** bizim / karşı taraf · **Form:** (a)/(b)/(c) · **Ortam:** Projects/Code
- **Değişiklik sayısı:** 🔴 N · 🟠 N · 🟡 N · 🟢 N
- **Kaynaklar:** Mevzuat MCP [✓/✗]; Yargı MCP [✓/✗]
- **Onay:** Baş Hukuk Müşaviri + dış vekil şart

[seçilen formda redline]

## Sonraki adımlar
> 1. **Eksik inceleme** — `/commercial-legal:review` ile derinleştir
> 2. **Governing law / yaptırım** — `/commercial-legal:governing-law-review`
> 3. **Karşı teklif turu** — kabul/ret sonrası `/contract-drafting:versiyon-karsilastir`
> 4. **Temiz nüsha** — kabul edilen değişikliklerle final taslak
> 5. **Başka**

**One question I'd ask:** [örn. "Bu karşı tarafla ilişki sürüyor mu? Sürüyorsa redline tonu agresif değil 'işbirlikçi-ama-korumalı' olmalı."]
```

---

## /contract-drafting:tadil-protokol

---
name: tadil-protokol
description: >
  Ana sözleşmeye bağlı EK PROTOKOL / TADİL / SÜRE UZATIMI metni üretir — ana sözleşmeye
  atıf, "X maddesi aşağıdaki şekilde değiştirilmiştir" formatı, yürürlük, değiştirilmeyen
  hükümlerin saklılığı (severability), damga vergisi, imza. TBK tadil disiplini.
  Örnek: EPC süre uzatımı/iş artışı, PPA fiyat revizyonu, kredi tadili, SHA değişiklik.
user-invocable: true
---

# Tadil / Ek Protokol / Süre Uzatımı Üretimi

> Mevcut bir sözleşmeyi **değiştiren** belgeyi üretir (yeni sözleşme değil — `belge-turet` o iş için). Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı; yüksek tutar/stratejik → Genel Müdür.

## ADIM 0 — Girdi
1. **Ana sözleşme** — kullanıcı yapıştırsın/yüklesin (en azından değişen maddeler + taraflar + tarih).
2. **İstenen değişiklik** — ne değişiyor? (süre, bedel/fiyat, kapsam/iş artışı, taraf, teminat, fesih...).
3. **Tip:** süre uzatım · fiyat/bedel revizyonu · iş artışı/azalışı · taraf değişikliği (devir) · genel tadil.

## ADIM 1 — Tadil disiplini (kritik)

- **Şekil:** Ana sözleşme hangi şekilde yapıldıysa tadil de aynı şekilde (TBK m.13 — yazılı sözleşmenin değişikliği yazılı). EPDK/kamu onayına tabi sözleşmede onay şartı.
- **Atıf:** Ana sözleşmeyi tarih/no ile tanımla ("Ana Sözleşme").
- **Değişiklik formatı:** "Ana Sözleşme'nin [N] maddesi aşağıdaki şekilde **değiştirilmiştir**" / "**eklenmiştir**" / "**yürürlükten kaldırılmıştır**" — eski + yeni metni net ver.
- **Saklılık:** "Değiştirilmeyen tüm hükümler aynen yürürlüktedir."
- **Yürürlük:** imza/tarih; geriye etki isteniyorsa açıkça yaz.
- **Damga vergisi:** tadil ayrı damga doğurabilir (DVK — değişen tutar üzerinden) → `[DOLDUR/doğrulayın]`.
- **Sektörel özel:** süre uzatımı mücbir sebebe dayanıyorsa TBK m.136 gerekçesi; **EPDK lisans şartlarını etkiliyorsa** ön-onay; **SHA tadili** ise reserved matters + ortak/finansör onayı; **kredi tadili** ise finansör covenant/onay.

## ADIM 2 — Taslak

```markdown
[ANA SÖZLEŞME ADI] – [TADİL / EK PROTOKOL No: N]

TARAFLAR : [Müvekkil / Şirket] ([VKN/adres]) — [Karşı Taraf]
ANA SÖZ. : GG.AA.YYYY tarihli [ad] ("Ana Sözleşme")
KONU     : Ana Sözleşme'nin aşağıdaki maddelerinin tadili / [süre uzatımı] amacıyla.

MADDE 1 — [Değişiklik]
  Ana Sözleşme'nin [N]. maddesi aşağıdaki şekilde değiştirilmiştir:
  "[yeni madde metni]"
  (Eski metin: "[eski metin]" — kayıt için)

MADDE 2 — [varsa ek değişiklik]

MADDE 3 — SAKLILIK
  İşbu [Protokol/Tadil] ile değiştirilmeyen Ana Sözleşme hükümleri aynen yürürlüktedir.

MADDE 4 — YÜRÜRLÜK VE DAMGA
  Bu belge imza tarihinde yürürlüğe girer; Ana Sözleşme'nin ayrılmaz ekidir.
  Damga vergisi [DOLDUR — DVK]. [Gerekiyorsa: EPDK/Kurul onayı şartı.]

TARİH / İMZALAR: [Müvekkil / Şirket] ([imza yetkilisi]) — [Karşı Taraf]
```

## Çıktı
```markdown
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN İMZALANMAZ

# [Tadil / Ek Protokol] — [ana sözleşme] — No: [N]

## ⚠️ İnceleyen notu
- **Ana sözleşme:** [ad, tarih] · **Tadil tipi:** [...]
- **Değişen madde sayısı:** N
- **Onay/şart tetikleyici:** [EPDK ön-onay / SHA reserved matter / finansör covenant / damga — varsa]
- **Onay:** Baş Hukuk Müşaviri (+ Genel Müdür yüksek tutarda) şart

[taslak]

## Sonraki adımlar
> 1. **Onay/şart kontrolü** — EPDK / SHA / finansör tetiklendiyse ilgili süreç
> 2. **Redline** — `/contract-drafting:redline-contract` ile son kontrol
> 3. **Damga vergisi** — DVK hesabı (`tax-legal` / `yazihane-asistani`)
> 4. **Başka**

**One question I'd ask:** [örn. "Bu tadil tek seferlik mi yoksa ana sözleşmenin dengesini kalıcı değiştiriyor mu? Kalıcıysa yan etkileri (fiyat, teminat, fesih) de gözden geçirmeliyiz."]
```

---

## /contract-drafting:versiyon-karsilastir

---
name: versiyon-karsilastir
description: >
  İki sözleşme versiyonunu (v1 ↔ v2 / bizim taslak ↔ karşı taraf revizesi) karşılaştırır —
  madde-madde track-changes/diff görünümü + her değişikliğin hukuki/ticari ETKİSİ +
  risk flag (karşı taraf ne kazandı/biz ne kaybettik). Müzakere turları ve "sessiz
  değişiklik" yakalama için. Claude.ai Projects: markdown diff; Claude Code: .docx compare.
user-invocable: true
---

# Versiyon Karşılaştırma (redline diff)

> Müzakere turunda **karşı tarafın neyi değiştirdiğini** yakalar — özellikle **sessizce eklenen/çıkarılan** klozları. Her çıktı **TASLAK**.

## ADIM 0 — Girdi
1. **İki versiyon** — v1 (örn. bizim son taslak) + v2 (örn. karşı taraf revizesi). Kullanıcı ikisini de yapıştırsın/yüklesin.
2. **Hangisi referans?** (genelde bizim son kabul ettiğimiz = baz).
3. Okuma kapsamını belirt; her ikisini de tam okuyamadıysan söyle.

## ADIM 1 — Madde eşle & diff çıkar

- Maddeleri başlık/numara ile eşle (numaralandırma kaymışsa içerikle eşle).
- Her madde için: **değişmedi / değişti / eklendi / silindi / taşındı**.
- Metin düzeyinde fark: ~~silinen~~ / **eklenen**.
- ⚠️ **Sessiz değişiklik avı:** tanım değişikliği, "shall→may", süre/eşik/tutar oynaması, istisna ekleme, sorumluluk tavanı, fesih kolaylaştırma, yetki/hukuk değişimi — küçük ama kritik.

## ADIM 2 — Etki & risk

Her değişiklik için:
- **Ne değişti** (kısa) · **Lehimize / aleyhimize / nötr** · **Severity** (🔴🟠🟡🟢) · **Etki** (hukuki/ticari sonuç) · **Aksiyon** (kabul / karşı-revize / müzakere).
- Emredici hüküm etkisi varsa `[Mevzuat MCP]`.

## ADIM 3 — Çıktı

```markdown
TASLAK – HUKUK MÜŞAVİRLİĞİ DAHİLİ

# Versiyon Karşılaştırma — [sözleşme] — v[X] ↔ v[Y]

## ⚠️ İnceleyen notu
- **Versiyonlar / okuma kapsamı:** [v1 tarih, v2 tarih, N sayfa]
- **Toplam değişiklik:** N (lehimize K · aleyhimize L · nötr M)
- **Kritik (🔴/🟠):** N adet
- **Onay:** Baş Hukuk Müşaviri (önemli değişiklik varsa)

## Özet — karşı taraf bu turda ne yaptı?
[2-4 cümle: en önemli hamleler + sessiz değişiklikler]

## Madde-madde diff
| # | Madde | Değişiklik (~~sil~~/**ekle**) | Yön | Severity | Etki | Aksiyon |
|---|---|---|---|---|---|---|
| 1 | 8.2 Sorumluluk tavanı | ~~%100~~ **%50 sözleşme bedeli** | aleyhe | 🔴 | tazminat hakkı yarıya iner | karşı-revize |

## Dikkat — sessiz/kritik değişiklikler
[🔴/🟠 maddelerin vurgusu]

## Sonraki adımlar
> 1. **Karşı-revize üret** — `/contract-drafting:redline-contract` (aleyhe maddelere)
> 2. **Müzakere notu** — iş birimi/Genel Müdür için özet
> 3. **Governing law değiştiyse** — `/commercial-legal:governing-law-review`
> 4. **Başka**

**One question I'd ask:** [örn. "Karşı taraf bu turda büyük taviz mi verdi yoksa küçük kazanımları paketleyip mi geçirdi? Cevap, kabul/itiraz stratejisini değiştirir."]
```

---
