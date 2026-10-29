---
name: privacy-legal-matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkilin ya da dosyanın bağlamının diğerine sızmamasını
  sağlar; veri sorumlusu müvekkil ile onun veri işleyeninin aynı büroda
  bulunabilmesi nedeniyle çapraz okuma kapalı tutulur. Çok müvekkilli avukat
  "yeni matter", "matter değiştir", "matter'larımı listele", "matter'ı kapat"
  dediğinde ya da yalnız uygulama düzeyinde çalışmak istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil ve dosya üzerinde çalışır. Matter çalışma alanı her dosyanın bağlamını diğerlerinden ayrı tutar. Bu skill o alanları yönetir.

## Alt komutlar

- `/arthurlegal:privacy-legal-matter-workspace new <slug>` — yeni matter oluştur, kısa ön görüşme yap, `matter.md` yaz
- `/arthurlegal:privacy-legal-matter-workspace list` — matter'ları durum ve aktiflik işaretiyle listele
- `/arthurlegal:privacy-legal-matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/arthurlegal:privacy-legal-matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/_archived/` altına taşı; asla silme)
- `/arthurlegal:privacy-legal-matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünün dolu olduğunu teyit et. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli kurum içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/arthurlegal:privacy-legal-cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok."
2. `$ARGUMENTS`'ın ilk kelimesine göre dallan:
   - `new` → ön görüşme, `matters/<slug>/matter.md` yaz, `history.md` ve `notes.md` oluştur.
   - `list` → `matters/*/matter.md` dosyalarını tara, tablo bas, aktif olanı işaretle.
   - `switch` → uygulama CLAUDE.md'sindeki `Active matter:` satırını güncelle.
   - `close` → `matters/<slug>/` klasörünü `matters/_archived/<slug>/` altına taşı, kapanış tarihini `history.md`'ye yaz.
   - `none` → `Active matter:` satırını `none — practice-level context only` yap.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` şablondaki gibi kalır; diğer skill'ler bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/privacy-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, rol, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-veri-isleyen-sozlesmesi`, `xyz-ihlal-2026`, `musteri-kurul-sikayeti`. Gerçek ad yerine takma ad kullanılabilir. Aynı slug arşivde varsa arşivdeki `_archived/<slug>/` altında korunur; yeni matter'a başka slug ver.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Veri işleyen sözleşmesinde iki taraf, ihlal dosyasında veri sorumlusu ile tedarikçisi ya da şikâyette ilgili kişi ile veri sorumlusu karşı karşıya gelebilir. Sor: "Bu matter için çatışma kontrolü yapıldı mı?" (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`.) Bu skill kontrolü kendisi yapmaz ve bu amaçla başka matter'ları okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz taraf (kurum içiyse iç birim)
   - **Müvekkilin bu işteki rolü** — veri sorumlusu / veri işleyen / ilgili kişi / ikisi (faaliyet bazında)
   - **Karşı taraf** — veri işleyen, veri sorumlusu, ilgili kişi, alt işleyen, yurt dışındaki alıcı (birden fazla olabilir)
   - **Matter türü** — PIA (işleme faaliyeti) | veri işleyen sözleşmesi incelemesi | ilgili kişi başvurusu | Kurula şikâyet / resen inceleme | veri ihlali | yurt dışı aktarım (standart sözleşme, bağlayıcı şirket kuralları, taahhütname) | VERBİS | idari para cezasına itiraz | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (yüksek, çapraz bağlamda ek dikkat demektir)
   - **Kritik süreler** — varsa, aşağıdaki listeden
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, hangi veri kategorileri (özel nitelikli var mı)
   - **Matter'a özel sapmalar** — ör. "müvekkil ihlal bildirimini 24 saatte istiyor", "karşı taraf stratejik ortak — ilişkiyi koruyan ton"
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/arthurlegal:privacy-legal-matter-workspace switch <slug>`)"

**Kritik süre listesi** (doğrulanmış; matter'a uyanı yaz):
- İlgili kişi başvurusu: en geç otuz gün (KVKK m. 13/2).
- Kurula şikâyet: veri sorumlusunun cevabını öğrenmeden itibaren otuz, her hâlde başvurudan itibaren altmış gün; başvuru yolu tüketilmeden şikâyet olmaz (m. 14/1-2). Kurul şikâyete altmış gün içinde cevap vermezse talep reddedilmiş sayılır (m. 15/4).
- Kurul incelemesi: istenen bilgi ve belgeler on beş gün içinde gönderilir; hukuka aykırılığın giderilmesi kararı tebliğden itibaren en geç otuz gün içinde yerine getirilir (m. 15/3, 15/5).
- Veri ihlali: en kısa sürede ilgilisine ve Kurula bildirim (m. 12/5). Kurul kararındaki somut süreyi araçla bul; bulunamazsa: UYARI: veri çekilemedi, teyidiniz gerekli: https://www.resmigazete.gov.tr/
- Standart sözleşme: imzaların tamamlanmasından itibaren beş iş günü içinde Kuruma bildirim; taraf ya da içerik değişikliği ve sona ermede de bildirim (KVKK m. 9/5; Yurt Dışına Aktarım Yönetmeliği m. 14/5, 14/8).
- VERBİS: kayıtlı bilgideki değişiklik yedi gün içinde (Veri Sorumluları Sicili Hakkında Yönetmelik m. 13).
- İdari para cezası: Kurulca verilen cezaya karşı idare mahkemesinde dava (KVKK m. 18/3). KVKK'nın çektiğimiz maddelerinde özel dava süresi yok; özel kanunda süre yoksa idare mahkemesinde dava açma süresi altmış gündür (İYUK m. 7/1). **Tartışmalı — içtihadı kontrol et:** `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="6698 idari para cezası dava açma süresi")`; dönen kararın künyesini birebir kullan. 1/6/2024 itibarıyla sulh ceza hâkimliklerinde görülmekte olan başvurular orada görülmeye devam eder (KVKK geçici m. 3/2).

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar:

| Slug | Müvekkil | Rol | Tür | Durum | Açılış | Aktif |
|---|---|---|---|---|---|---|

Aktif olanı `*` ile işaretle. `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

1. `matters/<slug>/matter.md` var mı bak; yoksa `new <slug>` öner.
2. `Active matter: <slug>` olarak güncelle.
3. Doğru matter'da olduğunu teyit etmesi için `matter.md` özetini göster (rol ve kritik süre dahil).

### `close <slug>`

1. `matters/<slug>/` var mı bak.
2. `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle.
3. `matters/<slug>/` → `matters/_archived/<slug>/` taşı.
4. Kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap.

### `none`

Yalnız `Active matter:` satırını `none — practice-level context only` yapar; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar
**Müvekkil:** [ad] — **Rol:** [veri sorumlusu / veri işleyen / ilgili kişi]
**Karşı taraf:** [ad(lar) ve rolleri]

## Matter türü
[tür — tek satır gerekçe]

## Kritik süreler
- [ör. başvuru tarihi: …, otuz günlük süre sonu: …; standart sözleşme imza tarihi: …, bildirim son günü: …]

## Ana olgular
[2-5 cümle; veri kategorileri, özel nitelikli veri, yurt dışı aktarım varsa ülke]

## Matter'a özel sapmalar
- [ör. "İhlal bildirimi: müvekkil 24 saat istiyor, ev standardı farklı."]

## İlgili matter'lar
- [slug — neden ilgili]

## Gizlilik notu
[Yüksek / kapalı ekipse nedeni; dosyaları kim görebilir; genel ayar açık olsa bile çapraz bağlama izin var mı]
```

## `history.md` başlangıcı

```markdown
# Geçmiş: [Müvekkil] — [kısa tarif]

Yalnız ekleme yapılan olay günlüğü; en yeni üstte.

---

## [YYYY-AA-GG] — Matter açıldı

Ön görüşme tamamlandı. Slug: `[slug]`. Durum: aktif.
[matter.md dışında saklanmaya değer ilk bağlam — ör. "Karşı tarafın sözleşme taslağı üzerine açıldı."]
```

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurma yasağını (Av. K. m. 36) ve aynı büroda zıt tarafların bulunabilmesinden doğan çatışma riskini (m. 38) destekler. Matter dosyaları da kişisel veri içerir; erişimi işin gerektirdiği kişilerle sınırlı tut.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş sözleşmede alt işleyen duruşumuzu karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil. Matter dosyalarındaki kişisel veriler, ilgili mevzuatta öngörülen veya işlendikleri amaç için gerekli olan süre kadar muhafaza edilir (KVKK m. 4/2-d); süre büronun/şirketin saklama ve imha politikasına göre belirlenir.
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.
