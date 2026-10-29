---
name: corporate-legal-matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkil şirketin ya da işlemin bağlamının (pay sahibi yapısı,
  işlem pozisyonu, veri odası bulguları, aile içi uyuşmazlık bilgisi) diğerine
  sızmamasını sağlar. Çok müvekkilli avukat matter oluşturmak, aktif matter'ı
  değiştirmek, listelemek, arşivlemek ya da uygulama düzeyine dönmek istediğinde ya da
  başka bir skill hangi matter'da çalıştığını bilmek istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil şirket ve işlem üzerinde çalışır. Kurumsal işte bir müvekkilin satış hazırlığı, başka bir dosyada alıcı adayı olan müvekkilin ilgisini çeker; aile şirketinde bir pay sahibinin bilgisi diğerinin dosyasına geçmemelidir. Matter çalışma alanı her dosyanın bağlamını ayrı tutar; bu skill o alanları yöneten ince dosya katmanıdır.

## Alt komutlar

- `/arthurlegal:corporate-legal-matter-workspace new <slug>` — yeni matter, kısa ön görüşme, `matter.md`
- `/arthurlegal:corporate-legal-matter-workspace list` — durum ve aktiflik işaretiyle liste
- `/arthurlegal:corporate-legal-matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/arthurlegal:corporate-legal-matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/_archived/` altına taşı; asla silme)
- `/arthurlegal:corporate-legal-matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünü bul. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli şirket içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/arthurlegal:corporate-legal-cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok." Kapalı durum şirket içi kullanıcı için beklenen durumdur.
2. `$ARGUMENTS`'ın ilk kelimesine göre aşağıdaki alt komut mantığına dallan.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` şablondaki gibi kalır; diğer skill'ler ve ajanlar bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/corporate-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
├── deals/<code>/deal-context.md    # --new-deal ile yazılan işlem bağlamı (M&A)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-pay-alimi-2026`, `xyz-olagan-gk-2026`, `def-birlesme`. Müvekkilin gerçek adı yerine takma ad kullanılabilir.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Avukat; aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermişse ve kendi düzenlediği bir senet ya da sözleşmenin hükümsüzlüğünü ileri sürmek durumu ortaya çıkmışsa işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Kurumsal işte sık görülen hâller: aynı şirketin pay sahipleri arasında uyuşmazlık (büro daha önce şirkete ya da bir pay sahibine danışmanlık verdiyse), büronun hazırladığı esas sözleşme, pay devri ya da pay sahipleri sözleşmesine karşı geçersizlik ileri sürülecekse, aynı satış sürecinde birden fazla alıcı adayı (m. 38 kapsamına girip girmediği olaya göre değerlendirilir — avukata işaretle). Sor: "Bu matter için çatışma kontrolü yapıldı mı?" (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`.) Bu skill çatışma kontrolünü kendisi yapmaz ve bu amaçla başka matter'ların dosyalarını okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve avukata hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz şirket ya da pay sahibi (şirket içinde: iş birimi veya grup şirketi); şirket türü (AŞ / Ltd. / halka açık AŞ / yabancı)
   - **Karşı taraf** — birden fazla olabilir (alıcı/satıcı, yatırımcı, diğer pay sahipleri); yabancıysa LEI ve grup yapısı için `gleif_search_entities` / `gleif_get_group_structure`
   - **Matter türü** — M&A alıcı | M&A satıcı | yatırım/finansman | YK/GK işi | esas sözleşme değişikliği | pay devri | birleşme/bölünme/tür değişikliği | grup yeniden yapılanması | entegrasyon | şirket uyumu | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (clean team; ör. rakipler arası işlemde rekabet açısından hassas bilgi)
   - **Kritik tarihler** — GK tarihi ve çağrı son günü, imza ve kapanış hedefi, düzenleyici onay (Rekabet Kurulu, sektör kurumu) beklentisi, tescil son günü
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, varsayılan yaklaşımdan farkı
   - **Matter'a özel sapmalar** — ör. "önemlilik eşiği bu işlemde 2 milyon TL", "müvekkil aile şirketi — pay sahiplerine giden notlarda ayrı dil", "esas sözleşmede YK nisabı ağırlaştırılmış"
   - **İlgili matter'lar ve deal kodu** — bağlantılı slug'lar; M&A ise `deals/<code>/deal-context.md` kodu
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/arthurlegal:corporate-legal-matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar; tablo: Slug | Müvekkil | Matter türü | Durum | Açılış | Aktif. Aktif olanı `*` ile işaretle; `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

`matters/<slug>/matter.md` yoksa `new <slug>` öner. Varsa `Active matter: <slug>` yap ve doğru matter'da olduğunu teyit etmesi için `matter.md` özetini (müvekkil, tür, kritik tarihler) göster.

### `close <slug>` ve `none`

`close`: `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle, `matters/<slug>/` → `matters/_archived/<slug>/` taşı; kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap. M&A matter'ları uzun ömürlüdür; kapanış sonrası kontroller (bedel düzeltmesi, tazmin talepleri, entegrasyon) bitmeden kapatmayı önerme. `none`: yalnız bu satırı değiştirir; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]
**Deal kodu:** [code / —]

## Taraflar
**Müvekkil:** [ad] — [AŞ / Ltd. / halka açık AŞ / yabancı] — [rolü: alıcı / satıcı / şirket / pay sahibi]
**Karşı taraf:** [ad(lar)] — [rol; yabancıysa LEI]

## Matter türü
[tür — tek satır gerekçe]

## Kritik tarihler
- [GK / çağrı son günü; imza; kapanış; düzenleyici onay; tescil]

## Ana olgular
[2-5 cümle; varsayılan yaklaşımdan farkı]

## Matter-specific overrides
- [ör. "M&A materiality: 2 milyon TL (ev standardı 5 milyon TL)."]
- [ör. "Board: esas sözleşme m. [..] — YK toplantı nisabı üye tam sayısının üçte ikisi."]

## İlgili matter'lar
- [slug — neden ilgili]

## Gizlilik notu
[Yüksek / kapalı ekipse nedeni; dosyaları kim görebilir; genel ayar açık olsa bile çapraz bağlama izin var mı]
```

Esaslı skill'ler matter'a özel sapmaları bu başlıktan okuyup profil duruşunun önüne koyar; başlığı çevirme.

## `history.md` başlangıcı

`# Geçmiş: [Müvekkil] — [kısa tarif]` başlığı, "Yalnız ekleme yapılan olay günlüğü; en yeni üstte." notu ve tek girdi: `## [YYYY-AA-GG] — Matter açıldı` — "Ön görüşme tamamlandı. Slug: `[slug]`. Durum: aktif." artı `matter.md` dışında saklanmaya değer ilk bağlam (ör. "Alıcı adayının niyet mektubu geldi.").

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurma yasağını (Av. K. m. 36) ve zıt menfaatli taraflardan doğan çatışma riskini (m. 38) destekler.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş pay alım işleminde tazmin tavanlarını karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır. Kıyas çıktısında müvekkil adlarını ve işlem bedellerini anonimleştirmeyi öner.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil; saklama süresi büronun politikasıdır.
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
| AZ istirak / JV yapisi, Azerbaycanli karsi taraf islemleri — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| yabanci sirketler hukuku karsilastirmasi, M&A yapisi ogretisi — **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| hedef sirketin maddi sozlesmelerinde kloz benchmark (diligence) | `/arthurlegal:legal-research-sozlesme-emsali` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`

---
