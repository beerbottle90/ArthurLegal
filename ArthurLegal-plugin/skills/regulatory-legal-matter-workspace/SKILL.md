---
name: regulatory-legal-matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkilin mevzuat değişikliği, taslak görüş, açık
  giderme, kurum bilgi talebi ya da soruşturma dosyasının bağlamını diğerlerinden
  ayrı tutar; aynı sektörde birden fazla müvekkil izlenebildiği için çapraz okuma
  kapalıdır. Çok müvekkilli avukat "yeni matter", "matter değiştir", "matter'larımı
  listele", "matter'ı kapat" dediğinde ya da bir skill hangi matter'da çalıştığını
  bilmek istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil ve dosya üzerinde çalışır. Matter çalışma alanı her dosyanın bağlamını diğerlerinden ayrı tutar. Bu skill o alanları yöneten ince dosya katmanıdır.

## Alt komutlar

- `/arthurlegal:regulatory-legal-matter-workspace new <slug>` — yeni matter oluştur, kısa ön görüşme yap, `matter.md` yaz
- `/arthurlegal:regulatory-legal-matter-workspace list` — matter'ları durum ve aktiflik işaretiyle listele
- `/arthurlegal:regulatory-legal-matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/arthurlegal:regulatory-legal-matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/_archived/` altına taşı; asla silme)
- `/arthurlegal:regulatory-legal-matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünün dolu olduğunu teyit et. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek şirket için kurum içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/arthurlegal:regulatory-legal-cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok."
2. `$ARGUMENTS`'ın ilk kelimesine göre dallan:
   - `new` → ön görüşme, `matters/<slug>/matter.md` yaz, `history.md` ve `notes.md` oluştur.
   - `list` → `matters/*/matter.md` dosyalarını tara, tablo bas, aktif olanı işaretle.
   - `switch` → uygulama CLAUDE.md'sindeki `Active matter:` satırını güncelle.
   - `close` → `matters/<slug>/` klasörünü `matters/_archived/<slug>/` altına taşı, kapanış tarihini `history.md`'ye yaz.
   - `none` → `Active matter:` satırını `none — practice-level context only` yap.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` şablondaki gibi kalır; `/arthurlegal:regulatory-legal-policy-diff`, `/arthurlegal:regulatory-legal-policy-redraft` ve `/arthurlegal:regulatory-legal-gaps` bunları birebir okur.

**İzleme uygulama düzeyindedir.** `reg-feed-watcher` ve `reg-change-monitor` ajanı varsayılan olarak matter'sız çalışır. Özetteki bir kalem belirli bir müvekkili ilgilendiriyorsa değerlendirme (`policy-diff`, açık kaydı, görüş kararı) o müvekkilin matter klasörüne yazılır.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/regulatory-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, kurum, tür, kritik süreler, olgular, sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-epdk-lisans-tadili`, `xyz-rekabet-sorusturma-2026`, `musteri-taslak-teblig-gorusu`. Gerçek ad yerine takma ad kullanılabilir. Aynı slug arşivde varsa arşivdeki korunur; yeni matter'a başka slug ver.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı:** Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Mevzuat işlerinde tipik risk: aynı soruşturmada şikâyetçi ile soruşturulan, aynı birleşme dosyasında taraf ile itiraz eden rakip, aynı taslağa zıt görüş verecek iki müvekkil. Yalnız aynı sektörde rakip olmak "aynı iş" sayılır mı — **tartışmalı**; büronun meslek kuralı yorumuna ve politikasına bırak. Sor: "Bu matter için çatışma kontrolü yapıldı mı?" (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`). Bu skill kontrolü kendisi yapmaz ve bu amaçla başka matter'ları okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz taraf (kurum içiyse iç birim)
   - **Kurum** — EPDK, BDDK, SPK, BTK, KVKK, Rekabet, GİB, TCMB, bakanlık, AB/yabancı makam …
   - **Karşı taraf / diğer ilgililer** — şikâyetçi, rakip, karşı işlem tarafı (birden fazla olabilir)
   - **Matter türü** — mevzuat değişikliği danışmanlığı | taslak düzenlemeye görüş | açık giderme (politika güncelleme) | kurum bilgi/belge talebi ya da yerinde inceleme | soruşturma / idari yaptırım savunması | düzenleyici işleme karşı dava hazırlığı | lisans/izin/bildirim | sürekli konu | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (yüksek, çapraz bağlamda ek dikkat demektir; ör. soruşturmadaki ticari sır)
   - **Kritik süreler** — varsa, aşağıdaki listeden
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, hangi düzenleme
   - **Matter'a özel sapmalar** — uygulama profiline göre farklar; ör. "müvekkil bu kurum için günlük tarama istiyor", "bu dosyada kuruma yazılar yalnız ortak imzasıyla çıkar"
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/arthurlegal:regulatory-legal-matter-workspace switch <slug>`)"

**Kritik süre listesi** (doğrulanmış; matter'a uyanı yaz, tarihleri tebliğ belgesinden hesapla):
- **Düzenleyici işleme dava:** özel kanunda ayrı süre yoksa Danıştayda ve idare mahkemesinde altmış, vergi mahkemesinde otuz gün (İYUK m. 7/1). İlanı gereken düzenleyici işlemde süre ilan tarihini izleyen günden başlar; düzenleyici işleme uygulama işlemiyle birlikte de dava açılabilir (m. 7/4).
- **Rekabet soruşturması:** soruşturma kararı 15 gün içinde taraflara bildirilir; soruşturma en geç 6 ayda tamamlanır, bir defaya mahsus 6 aya kadar ek süre verilebilir (4054 m. 43/1-2). Yazılı savunma soruşturma raporunun tebliğinden itibaren 30 gün; haklı gerekçeyle bir kez, en çok bir katına kadar uzatılabilir; raportörlerin ek yazılı görüşüne 30 gün içinde cevap; süresinde verilmeyen savunma dikkate alınmaz (m. 45/2-3). Uzlaşma yalnız soruşturma raporunun tebliğine kadar ve ihlalin kabulüyle; Kurulun verdiği kesin süre geçirilirse bildirim dikkate alınmaz; uzlaşılan hususlar dava konusu yapılamaz (m. 43/5, 6, 8). Taahhüt önaraştırma ya da soruşturma sürecinde sunulur (m. 43/3).
- **EPDK (elektrik):** bilgi isteme ya da yerinde incelemede aykırılık hâlinde on beş gün, mevzuata aykırılıkta otuz gün içinde düzeltme ihtarı; Kurul ihtar sürelerini fiilin niteliğine göre farklı uygulayabilir; idari para cezaları tebliğden itibaren bir ay içinde ödenir (6446 m. 16/1-a, b; 16/2; 16/8). Tutarları matter'a yazma; ihtar yazısındaki süreyi esas al.
- **KVKK dosyaları:** süreler `/arthurlegal:privacy-legal-matter-workspace` listesinde.
- **Diğer kurumlar (BDDK, SPK, BTK, GİB, TCMB):** süreyi özel kanundan ve tebliğ edilen yazıdan çek; ezberden süre yazma. İdari para cezasına karşı yargı yolu ve süresi özel kanuna göre değişir — **tartışmalı, içtihadı kontrol et:** `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="<kurum> idari para cezası görevli yargı yeri")`; dönen kararın künyesini birebir kullan.

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar:

| Slug | Müvekkil | Kurum | Tür | En yakın süre | Durum | Açılış | Aktif |
|---|---|---|---|---|---|---|---|

Aktif olanı `*` ile işaretle. `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

1. `matters/<slug>/matter.md` var mı bak; yoksa `new <slug>` öner.
2. `Active matter: <slug>` olarak güncelle.
3. Doğru matter'da olduğunu teyit etmesi için `matter.md` özetini göster (kurum ve en yakın süre dahil).

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

## Taraflar ve kurum
**Müvekkil:** [ad] · **Kurum:** [ad] · **Karşı taraf / ilgililer:** [ad(lar)]

## Matter türü
[tür — tek satır gerekçe]

## Kritik süreler
- [ör. soruşturma raporu tebliği: …, savunma son günü: …; düzenleyici işlemin RG tarihi: …, dava süresi sonu: …]

## Ana olgular
[2-5 cümle; ilgili düzenleme ve RG künyesi araçtan]

## Matter'a özel sapmalar
- [ör. "Bu kurum için günlük tarama; ev standardı haftalık."]

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
[matter.md dışında saklanmaya değer ilk bağlam — ör. "Kurumun bilgi isteme yazısı üzerine açıldı."]
```

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurma yasağını (Av. K. m. 36) ve aynı büroda zıt tarafların bulunabilmesinden doğan çatışma riskini (m. 38) destekler. Soruşturma dosyalarındaki rakip bilgisi ve ticari sırlar özellikle ayrı tutulur.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş taslak görüşümüzde EPDK'ya karşı aldığımız duruşu karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil; kapalı matter'lar çatışma kontrolü ve saklama amacıyla okunur kalır.
- **Süre hesabını kesinleştirmez** — listedeki süreler başlangıç noktasıdır; tebliğ tarihini ve özel kanunu avukat teyit eder.
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
| AZ duzenleyici degisiklik takibi — akt statusu degistiyse (`Legv olunmus`) ardil akti bul | `/arthurlegal:legal-research-az-mevzuat` |
| karsilastirmali regulasyon literaturu — **ikincil**, mevzuat yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
