---
name: commercial-legal-matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkilin ya da sözleşme dosyasının bağlamının (müzakere
  pozisyonu, geri çekilme noktaları, karşı taraf bilgisi) diğerine sızmamasını sağlar.
  Çok müvekkilli avukat matter oluşturmak, aktif matter'ı değiştirmek, listelemek,
  arşivlemek ya da uygulama düzeyine dönmek istediğinde ya da başka bir skill hangi
  matter'da çalıştığını bilmek istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil ve sözleşme üzerinde çalışır. Ticari sözleşmede bir müvekkilin geri çekilme noktası, karşı tarafın başka bir dosyadaki müvekkili olabilir; matter çalışma alanı her dosyanın bağlamını ayrı tutar. Bu skill o alanları yöneten ince dosya katmanıdır.

## Alt komutlar

- `/arthurlegal:commercial-legal-matter-workspace new <slug>` — yeni matter, kısa ön görüşme, `matter.md`
- `/arthurlegal:commercial-legal-matter-workspace list` — durum ve aktiflik işaretiyle liste
- `/arthurlegal:commercial-legal-matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/arthurlegal:commercial-legal-matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/_archived/` altına taşı; asla silme)
- `/arthurlegal:commercial-legal-matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünü bul. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli kurum içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/arthurlegal:commercial-legal-cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok." Kapalı durum kurum içi kullanıcı için beklenen durumdur.
2. `$ARGUMENTS`'ın ilk kelimesine göre aşağıdaki alt komut mantığına dallan.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` şablondaki gibi kalır; diğer skill'ler ve ajanlar bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/commercial-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-tedarik-2026`, `xyz-saas-yenileme`, `def-gizlilik`. Müvekkilin gerçek adı yerine takma ad kullanılabilir.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Avukat; aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermişse ve kendi düzenlediği bir senet ya da sözleşmenin hükümsüzlüğünü ileri sürmek durumu ortaya çıkmışsa işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Ticari sözleşmede ikinci hâl sık doğar: büronun daha önce hazırladığı sözleşmeye karşı geçersizlik ileri sürülecekse işaretle. Sor: "Bu matter için çatışma kontrolü yapıldı mı?" (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`.) Bu skill çatışma kontrolünü kendisi yapmaz ve başka matter'ların dosyalarını bu amaçla okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve avukata hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz taraf (kurum içinde: iş birimi)
   - **Karşı taraf** — birden fazla olabilir; tacir mi, tüketici mi, kamu tüzel kişisi mi (yetki sözleşmesi ve bildirim şekli buna bağlıdır)
   - **Matter türü** — tedarik/hizmet çerçeve sözleşmesi | müşteri sözleşmesi | NDA | SaaS aboneliği | değişiklik (tadil) | yenileme | distribütörlük/acentelik | lisans | diğer
   - **Taraf** — satış tarafı mı, satın alma tarafı mı (hangi playbook bölümü uygulanacak)
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (clean team; ör. rakipler arası bilgi paylaşımı)
   - **Kritik tarihler** — imza hedefi, teklif geçerlilik süresi, mevcut sözleşmenin fesih bildirimi son günü (yenileme kaydıyla eşleştir)
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, varsayılan playbook'tan farkı
   - **Matter'a özel sapmalar** — ör. "müvekkil 24 aylık tavan istiyor, büro standardı 12", "karşı taraf stratejik ortak — ilişkiyi koruyan üslup", "uygulanacak hukuk Türk hukuku, tahkim yeri İstanbul"
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/arthurlegal:commercial-legal-matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar; tablo: Slug | Müvekkil | Matter türü | Taraf | Durum | Açılış | Aktif. Aktif olanı `*` ile işaretle; `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

`matters/<slug>/matter.md` yoksa `new <slug>` öner. Varsa `Active matter: <slug>` yap ve doğru matter'da olduğunu teyit etmesi için `matter.md` özetini (taraf ve kritik tarihler dahil) göster.

### `close <slug>` ve `none`

`close`: `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle, `matters/<slug>/` → `matters/_archived/<slug>/` taşı; kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap. `none`: yalnız bu satırı değiştirir; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar
**Müvekkil:** [ad] — **Taraf:** [satış / satın alma]
**Karşı taraf:** [ad(lar)] — [tacir / tüketici / kamu tüzel kişisi]

## Matter türü
[tür — tek satır gerekçe]

## Kritik tarihler
- [imza hedefi; teklif geçerliliği; fesih bildirimi son günü]

## Ana olgular
[2-5 cümle; varsayılan playbook'tan farkı]

## Matter-specific overrides
- [ör. "Limitation of liability: müvekkil 24 ay istiyor (standart 12)."]
- [ör. "Governing law and venue: Türk hukuku; İstanbul merkezli kurumsal tahkim."]

## İlgili matter'lar
- [slug — neden ilgili]

## Gizlilik notu
[Yüksek / kapalı ekipse nedeni; dosyaları kim görebilir; genel ayar açık olsa bile çapraz bağlama izin var mı]
```

İnceleme skill'leri matter'a özel sapmaları bu başlıktan okuyup playbook duruşunun önüne koyar; başlığı çevirme.

## `history.md` başlangıcı

`# Geçmiş: [Müvekkil] — [kısa tarif]` başlığı, "Yalnız ekleme yapılan olay günlüğü; en yeni üstte." notu ve tek girdi: `## [YYYY-AA-GG] — Matter açıldı` — "Ön görüşme tamamlandı. Slug: `[slug]`. Durum: aktif." artı matter.md dışında saklanmaya değer ilk bağlam (ör. "Karşı tarafın taslak çerçeve sözleşmesi geldi.").

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurmama yükümlülüğünü (Av. K. m. 36) ve zıt menfaatli taraflardan doğan çatışma riskini (m. 38) destekler.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş tedarik matter'ında sorumluluk tavanlarını karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır. Kıyas çıktısında müvekkil adlarını ve müzakere pozisyonlarını anonimleştirmeyi öner.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil. Saklama süresi büronun/şirketin politikasıdır (kişisel veride KVKK m. 4/2-d: ilgili mevzuatta öngörülen ya da işlendikleri amaç için gerekli süre kadar muhafaza).
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
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/arthurlegal:legal-research-az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/arthurlegal:legal-research-sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
