---
name: employment-legal-matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkilin ya da dosyanın bağlamının diğerine sızmamasını
  sağlar; iş hukukunda işveren ve işçi tarafının aynı büroda bulunabilmesi nedeniyle
  çapraz okuma kapalı tutulur. Çok müvekkilli avukat "yeni matter", "matter değiştir",
  "matter'larımı listele", "matter'ı kapat" dediğinde ya da aktif matter'ı yönetmesi
  gerektiğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil ve dosya üzerinde çalışır. Matter çalışma alanı her dosyanın bağlamını diğerlerinden ayrı tutar. Bu skill o alanları yönetir.

## Alt komutlar

- `/arthurlegal:employment-legal-matter-workspace new <slug>` — yeni matter oluştur, kısa ön görüşme yap, `matter.md` yaz
- `/arthurlegal:employment-legal-matter-workspace list` — matter'ları durum ve aktiflik işaretiyle listele
- `/arthurlegal:employment-legal-matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/arthurlegal:employment-legal-matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/employment-legal/matters/_archived/` altına taşı; asla silme)
- `/arthurlegal:employment-legal-matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünün dolu olduğunu teyit et. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli kurum içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/arthurlegal:employment-legal-cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok."
2. `$ARGUMENTS`'ın ilk kelimesine göre dallan:
   - `new` → ön görüşme, `matters/<slug>/matter.md` yaz, `history.md` ve `notes.md` oluştur.
   - `list` → `matters/*/matter.md` dosyalarını tara, tablo bas, aktif olanı işaretle.
   - `switch` → uygulama CLAUDE.md'sindeki `Active matter:` satırını güncelle.
   - `close` → `matters/<slug>/` klasörünü `matters/_archived/<slug>/` altına taşı, kapanış tarihini `history.md`'ye yaz.
   - `none` → `Active matter:` satırını `none — practice-level context only` yap.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` değerleri şablondaki gibi kalır; diğer skill'ler bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/employment-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   ├── investigation-<slug>/   # iç soruşturma dosyaları (varsa)
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-isverenlik-fesih-2026`, `isci-ise-iade-x`, `xyz-ic-sorusturma`. Müvekkil gerçek adını slug'a koymak zorunda değilsin; takma ad kullanılabilir.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Sor: "Bu matter için çatışma kontrolü yapıldı mı?" (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`.) Bu skill çatışma kontrolünü kendisi yapmaz ve başka matter'ların dosyalarını bu amaçla okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve avukata hatırlat.
3. Ön görüşme:
   - **Müvekkil ve taraf rolü** — temsil ettiğimiz taraf (işveren / işçi / kurum içi birim)
   - **Karşı taraf** — işveren, işçi(ler), alt işveren, özel istihdam bürosu (birden fazla olabilir)
   - **Matter türü** — işe alım | fesih danışmanlığı | işe iade / arabuluculuk | alacak hesabı | iç soruşturma | taciz-mobbing | sınıflandırma | toplu işçi çıkarma | yurt dışı genişleme | yönetmelik/politika | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (yüksek, çapraz bağlamda ek dikkat demektir)
   - **Kritik süre** — varsa: m. 26 son günü, fesih tebliğ tarihi (işe iade için bir aylık arabuluculuk süresi, İş K. m. 20/1), arabuluculuk son tutanak tarihi
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu
   - **Matter'a özel sapmalar** — ör. "müvekkil TİS'i 5 iş günü savunma süresi öngörüyor", "işçi tarafı: sulh alt sınırı müvekkil yazılı onayıyla"
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/arthurlegal:employment-legal-matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar:

| Slug | Müvekkil | Taraf | Tür | Durum | Açılış | Aktif |
|---|---|---|---|---|---|---|

Aktif olanı `*` ile işaretle. `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

1. `matters/<slug>/matter.md` var mı bak; yoksa `new <slug>` öner.
2. `Active matter: <slug>` olarak güncelle.
3. Doğru matter'da olduğunu teyit etmesi için `matter.md` özetini göster (taraf rolü ve kritik süre dahil).

### `close <slug>`

1. `matters/<slug>/` var mı bak.
2. `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle.
3. `matters/<slug>/` → `matters/_archived/<slug>/` taşı.
4. Kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap.

`none`: yalnız `Active matter:` satırını `none — practice-level context only` yapar; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar
**Müvekkil:** [ad] — **Taraf rolü:** [işveren / işçi / kurum içi]
**Karşı taraf:** [ad(lar)]

## Matter türü
[tür — tek satır gerekçe]

## Kritik süreler
- [ör. m. 26 son günü: …; fesih tebliğ tarihi: …; arabuluculuk son tutanak: …]

## Ana olgular
[2-5 cümle; işyeri ve işçi sayısı, TİS durumu dahil]

## Matter'a özel sapmalar
- [ör. "Savunma süresi: TİS'e göre 5 iş günü."]

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
[matter.md dışında saklanmaya değer ilk bağlam]
```

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan; işveren ve işçi tarafını birlikte yürüten büroda **zorunlu**) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın sır saklama yükümlülüğünü (Av. K. m. 36) ve aynı büroda zıt tarafların bulunabilmesinden doğan çatışma riskini (m. 38) destekler.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş işveren dosyasında savunma süresini karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil. Saklama süresi büronun/şirketin politikasıdır (kişisel veride KVKK m. 4/2-d: işlendikleri amaç için gerekli süre kadar muhafaza).
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.

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
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
