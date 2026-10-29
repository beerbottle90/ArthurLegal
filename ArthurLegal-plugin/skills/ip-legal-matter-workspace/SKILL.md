---
name: ip-legal-matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Çok müvekkilli büro pratiğinde bir müvekkilin bağlamının
  (marka stratejisi, buluş içeriği, uygulama duruşu, karşı taraf bilgisi)
  diğerine sızmamasını sağlar. Matter oluşturmak, aktif matter'ı değiştirmek,
  listelemek, arşivlemek ya da uygulama düzeyine dönmek istendiğinde ya da başka
  bir skill hangi matter'da çalıştığını bilmek istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat ve vekil birçok müvekkil ve dosya üzerinde çalışır. Fikri mülkiyette bir müvekkilin marka adayı, buluş içeriği ya da uygulama planı başka bir dosyadaki müvekkilin rakibini ilgilendirebilir; matter çalışma alanı her dosyanın bağlamını ayrı tutar. Bu skill o alanları yöneten ince dosya katmanıdır.

**Varsayılan kapalıdır.** Şirket içi kullanıcı bunu hiç görmez; uygulama düzeyinde çalışır. Kurulumda büro seçen kullanıcıda açılır ya da `## Matter workspaces` elle düzenlenir.

## Alt komutlar

- `/arthurlegal:ip-legal-matter-workspace new <slug>` — yeni matter, kısa ön görüşme, `matter.md`
- `/arthurlegal:ip-legal-matter-workspace list` — durum ve aktiflik işaretiyle liste
- `/arthurlegal:ip-legal-matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/arthurlegal:ip-legal-matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/_archived/` altına taşı; asla silme)
- `/arthurlegal:ip-legal-matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünü bul. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli şirket içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/arthurlegal:ip-legal-cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/arthurlegal:ip-legal-matter-workspace`'e ihtiyacınız yok."
2. `$ARGUMENTS`'ın ilk kelimesine göre aşağıdaki alt komut mantığına dallan.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context`, `none — practice-level context only` ve `matter.md` içindeki `## Matter-specific overrides` aynen kalır; diğer skill'ler ve ajanlar bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/ip-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
├── portfolio.yaml                  # portföy kaydı (uygulama düzeyi)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı; ör. cease-desist/, takedown/)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-marka-arastirma-2026`, `xyz-ihtarname`, `def-fto`. Müvekkilin gerçek adı yerine takma ad kullanılabilir. Aynı slug hem arşivde hem aktifte olamaz; arşivdeki `_archived/<slug>/` altında korunur.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Avukat; aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermişse ve kendi düzenlediği bir senet ya da sözleşmenin hükümsüzlüğünü ileri sürmek durumu ortaya çıkmışsa işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Fikri mülkiyette sık doğan örnekler: büronun başka bir müvekkil adına tescil ettirdiği markaya karşı hükümsüzlük ya da iptal talebi; büronun hazırladığı lisans/devir sözleşmesine karşı geçersizlik iddiası; aynı ya da benzer işaret için iki müvekkilin başvurusu. Sor: "Bu matter için çatışma kontrolü yapıldı mı?" (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`.) Bu skill çatışma kontrolünü kendisi yapmaz ve başka matter'ların dosyalarını bu amaçla okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz taraf (şirket içinde: iş birimi)
   - **Karşı taraf** — birden fazla olabilir; izleme bulgusuyla açılan dosyada "bilinmeyen üçüncü kişi"
   - **Matter türü** — marka araştırması | marka tescil/itiraz | marka ihlali ve ihtarname | içerik kaldırma (telif) | patent FTO | patent ihlali | fikri mülkiyet klozu incelemesi | açık kaynak uyumu | portföy bakımı | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (clean team; FTO ve buluş dosyalarında yaygın)
   - **Kritik tarihler** — bülten itirazı (yayımdan iki ay, SMK m. 18/1), ihtarnamedeki süre, menfi tespit için görüş talebine cevap süresi (bir ay, SMK m. 154/1), ceza şikâyeti (altı ay, TCK m. 73/1), yenileme tarihleri (`portfolio.yaml` ile eşleştir)
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, varsayılan duruştan farkı
   - **Matter'a özel sapmalar** — ör. "müvekkil bu marka için atak duruş istiyor", "karşı taraf stratejik kanal ortağı — yalnız ölçülü üslup", "buluşçu görüşmeye uygun değil — mülakat önerme"
   - **Dış vekil / avukat** — bu dosyada TÜRKPATENT işlemlerini yürüten kayıtlı vekil ya da dava avukatı (profildeki `Outside counsel roster`'dan)
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/arthurlegal:ip-legal-matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar; tablo: Slug | Müvekkil | Matter türü | Durum | Açılış | Aktif. Aktif olanı `*` ile işaretle; `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

`matters/<slug>/matter.md` yoksa `new <slug>` öner. Varsa `Active matter: <slug>` yap ve doğru matter'da olduğunu teyit etmesi için `matter.md` özetini (gizlilik düzeyi ve kritik tarihler dahil) göster.

### `close <slug>` ve `none`

`close`: `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle, `matters/<slug>/` → `matters/_archived/<slug>/` taşı; kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap. Tescil dosyalarında kapatmadan önce sor: "Yenileme takibi `portfolio.yaml`'da sürüyor mu?" — fikri mülkiyet matter'ı tescille bitmez, yenilemelerle sürer. `none`: yalnız `Active matter:` satırını değiştirir; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar
**Müvekkil:** [ad]
**Karşı taraf:** [ad(lar) / bilinmeyen üçüncü kişi]
**Dış vekil / avukat:** [ad — rol]

## Matter türü
[tür — tek satır gerekçe]

## Kritik tarihler
- [bülten itirazı; ihtarname süresi; SMK m. 154 cevap süresi; şikâyet süresi; yenileme]

## Ana olgular
[2-5 cümle; varsayılan duruştan farkı]

## Matter-specific overrides
- [ör. "Enforcement posture: house varsayılanı atak olsa da burada ölçülü — karşı taraf ana kanal ortağı."]
- [ör. "Approval: her mektuptan önce pazarlama onayı da alınır."]
- [ör. "Kapalı ekip: çapraz bağlam açık olsa bile bu matter okunmaz."]

## İlgili matter'lar
- [slug — neden ilgili]

## Gizlilik notu
[Yüksek / kapalı ekipse nedeni; dosyaları kim görebilir; genel ayar açık olsa bile çapraz bağlama izin var mı]
```

Esaslı skill'ler (`/arthurlegal:ip-legal-cease-desist`, `/arthurlegal:ip-legal-takedown`, `/arthurlegal:ip-legal-ip-clause-review` …) matter'a özel sapmaları bu başlıktan okuyup uygulama duruşunun önüne koyar; başlığı çevirme.

## `history.md` başlangıcı

`# Geçmiş: [Müvekkil] — [kısa tarif]` başlığı, "Yalnız ekleme yapılan olay günlüğü; en yeni üstte." notu ve tek girdi: `## [YYYY-AA-GG] — Matter açıldı` — "Ön görüşme tamamlandı. Slug: `[slug]`. Durum: aktif." artı matter.md dışında saklanmaya değer ilk bağlam (ör. "25. sınıfta izleme bulgusu üzerine açıldı.").

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurmama yükümlülüğünü (Av. K. m. 36) ve zıt menfaatli taraflardan doğan çatışma riskini (m. 38) destekler.

`on` iken bile yalnız kullanıcı açıkça isterse ("bu marka için gönderdiğimiz bütün ihtarnameleri matter'lar boyunca göster") çapraz okunur; varsayılan yine yalnız aktif matter'dır. Kapalı ekip matter'ında `## Gizlilik notu` çapraz okumayı yasaklıyorsa genel ayar açık olsa bile okunmaz. Kıyas çıktısında müvekkil adlarını anonimleştirmeyi öner.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil; kapalı matter'lar çatışma ve saklama amacıyla okunabilir kalır. Saklama süresi büronun/şirketin politikasıdır.
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Portföy kaydını taşımaz** — `portfolio.yaml` uygulama düzeyindedir; yenileme takibi `/arthurlegal:ip-legal-portfolio`'dadır.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.
