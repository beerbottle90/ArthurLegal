---
name: commercial-legal-renewal-tracker
description: >
  Fesih bildirimi son günü yaklaşan sözleşmeleri gösterir ve bildirim penceresi
  kapanmadan uyarır; tutulan yenileme kaydından çalışır. Son günü Türk hukukuna göre
  hesaplar (TBK m. 92-93 süre ve tatil kuralı, 2429 s. Kanun genel tatilleri), tacirler
  arası ihbar şeklini (TTK m. 18/3) ve tebliğ süresini tampona katar, tüketici
  aboneliklerinde otomatik uzama yasağını (6502 m. 52) işaretler. Kullanıcı "yakında ne
  yenileniyor", "hangi yenilemeler geldi", "fesih süresini kaçırdık mı", "bunu yenileme
  takibine ekle" dediğinde ya da zamanlanmış çalışmada kullan. saas-msa-review'dan
  devir alır.
argument-hint: "[--days N pencereyi değiştirir | --missed kaçan pencereler]"
---

# /renewal-tracker

Neyin ne zaman yenilendiğini ve en geç ne zaman fesih bildirimi **gönderilmesi** gerektiğini gösterir.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-register.yaml` dosyasını oku (ayar klasörü — eklenti güncellemelerinden etkilenmez).
2. **Varsayılan:** Mod 2 — önümüzdeki 90 gün, aciliyete göre yarı açık aralıklarla: 🔴 0–13 gün, 🟠 14–44 gün, 🟡 45–89 gün. 14., 45. ve 90. gün sınırdır; her son gün tek bir banda düşer.
3. **`--days N`:** pencereyi değiştir. **`--missed`:** Mod 4 — kayıtlı fesih olmadan geçen son günler.
4. **Kayıt boşsa ve CLM bağlıysa:** Mod 3'ü öner (toplu yükleme).
5. Çıktıya önerilen eylemleri ekle: kime sorulacak (kayıttaki iş sahibi), hangilerinde yenileme fiyatı sınırsız/endekssiz (pencere kapanmadan pazarlık gücü).

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Açıksa ve aktif matter varsa yalnız o matter'ın kayıtlarını göster (`matter` alanı); `Cross-matter context` `on` değilse diğer müvekkillerin satırlarını raporlama.

## Kayıt

`renewal-register.yaml` — **anahtarlar İngilizce kalır** (saas-msa-review, vendor-agreement-review ve renewal-watcher bu adları okur); değerler Türkçe olabilir:

```yaml
- counterparty: "ABC Yazılım A.Ş."
  agreement: "ABC Platform Abonelik Sözleşmesi"
  signed_date: 2025-06-15
  initial_term_end: 2026-06-15
  current_term_end: 2026-06-15     # her otomatik yenilemede ileri alınır; cancel_by_* bundan hesaplanır
  renewal_mechanism: "yıllık otomatik yenileme"
  notice_period_days: 60
  notice_method: "KEP"             # noter / taahhütlü mektup / telgraf / KEP / e-posta / portal / sözleşme m. X
  transit_buffer_days: 1           # aşağıdaki tabloya göre ya da sözleşmedeki tebliğ kuralına göre
  cancel_by_calendar: 2026-04-16   # current_term_end eksi notice_period_days
  cancel_by_effective: 2026-04-16  # gerekiyorsa son iş gününe GERİ çekilmiş
  send_by_effective: 2026-04-15    # cancel_by_effective eksi transit_buffer_days — bildirimin GÖNDERİLECEĞİ son gün
  cancel_by_roll_note: ""          # ör. "Pazar 2026-11-01'den geri çekildi; sözleşmedeki iş günü tanımıyla teyit et"
  cancel_by_provenance: "[model hesabı — fesih bildirimi klozuyla teyit et]"
  price_on_renewal: "güncel liste fiyatı (sınırsız)"   # ya da "TÜFE endeksli" vb.
  annual_value: 480000
  currency: "TRY"                  # isteğe bağlı; yoksa notes'a yaz
  business_owner: "ayse@sirket.com"
  clm_id: "IC-12345"               # bağlıysa
  docusign_envelope: "abc-123"     # bağlıysa
  status: "active"                 # active | cancelled | renewed | lapsed
  matter: "abc-tedarik-2026"       # isteğe bağlı; yalnız matter çalışma alanları açıksa
  notes: "Fiyat sınırsız — yenilemeden önce gözden geçir. Alternatif: X, Y."
```

**Uyarıyı `send_by_effective`'ten ver, `cancel_by_effective`'ten değil.** Noter kanalıyla 60 günlük pencere fiilen 50 küsur gündür; "ulaşma" tarihine göre uyaran kayıt son günü kaçırır. Mod 2'nin aciliyet sütunu `send_by_effective`'i gösterir; ayrıntı sütunu `cancel_by_effective`, `notice_method` ve `transit_buffer_days`'i gösterir ki okuyan tamponu sorgulayabilsin.

**Yuvarlanan yenilemeler.** `initial_term_end` kayıt içindir; `cancel_by_*` daima `current_term_end`'den hesaplanır. Pencere bildirimsiz geçip yenileme gerçekleşince sor:

> Bu sözleşme [tarih]'te otomatik yenilendi. Kaydı güncelleyelim: yeni `current_term_end` [tarih + yenileme süresi], yeni `cancel_by_effective` [hesap], yeni `send_by_effective` [hesap]. Onaylıyor musunuz?

## Son gün hesabı — Türk hukuku

Kayıttaki son gün, bildirimin hüküm doğurduğu **son iş günüdür**, takvim günü değil. Hafta sonuna ya da bayrama düşen tarih son günü kaçırmanın en yaygın yoludur; kayıt bunu bir kez, girişte yakalar.

1. **Takvim tarihini hesapla.** `cancel_by_calendar = current_term_end − notice_period_days` (ya da klozun söylediği). Süre ay olarak belirlenmişse ay hesabı TBK m. 92 (bent 3) mantığıyla yapılır (son ayın karşılık gelen günü; o gün yoksa ayın son günü). TBK m. 92 ileriye doğru sayım için yazılmıştır; "bitişten iki ay önce" gibi geriye sayımda aynı mantığı uygula ve hesabı `cancel_by_roll_note`'a yaz.
2. **Geri çek — asla ileri alma.** Sözleşme Türk hukukuna tabiyse tatil takvimi: hafta tatili Pazar (2429 s. Kanun m. 3); genel tatiller 1 Ocak, 23 Nisan, 1 Mayıs, 19 Mayıs, 15 Temmuz, 30 Ağustos, Ramazan Bayramı (arefe 13.00'ten itibaren 3,5 gün), Kurban Bayramı (arefe 13.00'ten itibaren 4,5 gün) (m. 2) ve 29 Ekim (28 Ekim 13.00'ten itibaren, m. 1). Dini bayram tarihleri her yıl değişir — o yılın takvimini teyit et. Arefe yarım gününü ve Cumartesi'yi de iş günü sayma (Cumartesi genel tatil değildir ama hafta tatili en geç Cumartesi 13.00'te başlar, m. 3; Cumartesi'nin TBK m. 93 anlamında "tatil" sayılıp sayılmadığı **tartışmalı**). Kamu idari izin günlerinde noterin ve postanın çalışıp çalışmadığını ayrıca teyit et.
3. **TBK m. 93'e güvenme.** Kanuna göre ifa zamanı ya da sürenin son günü tatile rastlarsa izleyen ilk iş gününe geçer; aksine anlaşma geçerlidir (TBK m. 93). Kayıt bu ileri kaymayı **kullanmaz**: kuralın bildirim süresine uygulanması klozun ifadesine bağlıdır ve sözleşme bunu dışlamış olabilir. Geri çekilmiş tarih her durumda güvenlidir.
4. **Sözleşmenin kendi gün kuralını kontrol et.** "İş günü", "tebliğ edilmiş sayılır", "saat 17.00'ye kadar", bildirim adresleri ve kanal klozu varsa o kontrol eder. Varsayılan geri çekme ile sözleşme kuralı arasındaki farkı işaretle.
5. **İki tarihi de yaz.** `cancel_by_calendar` ham hesap; `cancel_by_effective` son iş günü; `cancel_by_roll_note` farkın nedeni. Her hesaplanan `cancel_by_effective` `cancel_by_provenance: "[model hesabı — fesih bildirimi klozuyla teyit et]"` taşır; doğrulama bayrağı tarihle birlikte gider.
6. **Uyarıyı etkin tarihten ver.** Bantlar `send_by_effective`'e göre hesaplanır; geri çekme olduysa ayrıntı sütununda `cancel_by_calendar` ve `cancel_by_roll_note` görünür.

**Yabancı hukuka tabi sözleşme:** o ülkenin tatil takvimini yerel kaynaktan teyit et (ArthurLegal araçları tatil takvimi vermez); bildirim ve süre kuralı için ilgili önek (ör. `uk_search_legislation`, `de_gesetz_ara`, `eu_search_eu_law`) ya da `/arthurlegal:commercial-legal-governing-law-review`. Takvim belirlenemiyorsa: "Uygulanacak hukuk [X] — geri çekme yer tutucu olarak Türkiye tatilleriyle yapıldı; [ülke] takvimiyle teyit edin."

Mod 2'de haftanın günü ve uyarı olmadan basılan `cancel_by: 2026-11-01` (Pazar) sessizce yanlış bir son gündür.

## Bildirim şekli ve tampon

Tacirler arasında temerrüde düşürme, fesih ve dönme ihbarları noter, taahhütlü mektup, telgraf ya da güvenli elektronik imzalı KEP ile yapılır (TTK m. 18/3). Bu şeklin geçerlilik şartı mı ispat aracı mı olduğu **tartışmalı — içtihadı kontrol et** (`tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="TTK 18/3 ihbar şekli fesih")`; dönen kararın künyesini birebir kullan). Sözleşme "e-posta yeterli" diyorsa bile karşı taraf tacirse KEP ya da noter öner.

| `notice_method` | Önerilen `transit_buffer_days` | Neden |
|---|---|---|
| KEP | 1 | Anlık iletim; teslim kaydını almak için bir gün pay |
| Noter ihtarnamesi (karşı taraf şirket) | ≥ 7 | Noter tebligatı Tebligat Kanunu'na göre yapılır (m. 1); özel hukuk tüzel kişilerine elektronik tebligat zorunludur ve adrese ulaştığı tarihi izleyen beşinci günün sonunda yapılmış sayılır (m. 7/a); noter işlem süresi eklenir |
| Taahhütlü mektup (yurt içi) | 5–7 | Posta süresi ve teslim belirsizliği |
| Yurt dışı (kurye / uluslararası taahhütlü) | ≥ 10 | Ya da sözleşmedeki tebliğ kuralı |
| E-posta / portal | 0 | Ancak tacirler arasında şekil riski — notlara yaz |

Bildirimin "ulaşma" tarihinde mi, tebliğin "yapılmış sayıldığı" tarihte mi süreyi karşıladığı sözleşmenin diline bağlıdır; belirsizse ihtiyatlı olanı (geç tarihi) esas al.

## Otomatik yenileme ve belirsiz süreye dönüşme

- **Ticari (B2B):** Otomatik yenileme sözleşme serbestisi içindedir. Ancak karşı tarafın standart metnine gömülü yenileme klozu genel işlem koşuluysa: karşı tarafa açıkça bilgi verilip kabul edilmedikçe yazılmamış sayılır (TBK m. 21), dürüstlük kuralına aykırı aleyhe hüküm konulamaz (m. 25). Kaçırılan pencerede bu bir pazarlık aracıdır, güvence değil.
- **Tüketiciye satış (B2C abonelik):** tüketici, ticari veya mesleki olmayan amaçlarla hareket eden kişidir (6502 m. 3/1-k). Belirli süreli abonelik sözleşmesine sözleşmenin kendiliğinden uzayacağına ilişkin hüküm konulamaz; uzatma ancak tüketicinin talebi ya da onayıyla olur (m. 52/3). Belirsiz süreli ya da bir yıldan uzun belirli süreli abonelikte tüketici gerekçesiz ve cezai şartsız her zaman feshedebilir; bildirim kâğıt üzerinde ya da kalıcı veri saklayıcısıyla yeterlidir (m. 52/4). Satış tarafı B2C kayıtlarında `renewal_mechanism`'e "otomatik uzama yasak — onay gerekir" yaz. Yönetmeliğin güncel metni: `tr_mevzuat_ara(query="Abonelik Sözleşmeleri Yönetmeliği", types=["YONETMELIK"])`.
- **Örtülü sürdürme:** süre bitip taraflar ilişkiyi sürdürürse sözleşme belirsiz süreliye dönüşebilir — kira (TBK m. 327/2) ve acentelik (TTK m. 121/2) için açık hüküm var; acentelikte belirsiz süreli sözleşme üç ay önceden ihbarla feshedilir (m. 121/1). **TBK'da belirsiz süreli sürekli sözleşmelerin olağan feshine ilişkin tek bir genel madde yoktur;** sözleşmede fesih hükmü yoksa süre ve usul **tartışmalı — içtihadı kontrol et**: `tr_ictihat_semantik_ara(query="belirsiz süreli sürekli borç ilişkisinin olağan feshi makul bildirim süresi")`. Böyle kayıtlarda `renewal_mechanism: "belirsiz süreli — fesih süresi teyitsiz"` yaz.

## Modlar

### Mod 1 — Yenileme ekle (incelemeden devir)

saas-msa-review ya da vendor-agreement-review bir yenileme klozu bulunca kaydı devreder. Kayda ekle ve yukarıdaki hesabı yap. Karşı tarafın kaydı zaten varsa sor: yenilenmiş sözleşme mi (değiştir), ek sözleşme mi (ekle)?

### Mod 2 — Yaklaşanlar

Varsayılan 90 gün. Bantlar `send_by_effective − bugün` ile hesaplanır:
- 🔴 **0–13 gün** (bugün dahil) · 🟠 **14–44 gün** · 🟡 **45–89 gün** · 90+ yalnız `--days` ile.

```markdown
## Yenilemeler — önümüzdeki 90 gün

### 🔴 Gönderim son günü 0–13 gün içinde

| Karşı taraf | Gönder (son) | Fesih son günü | Kanal / tampon | Yenileme | Yıllık bedel | Sorumlu | Not |
|---|---|---|---|---|---|---|---|
| [ad] | **[tarih, gün adı]** | [tarih] | [KEP / 1] | [tarih] | [tutar + para birimi] | [e-posta] | [geri çekme notu] |

### 🟠 14–44 gün
[aynı tablo]

### 🟡 45–89 gün
[aynı tablo]

---

**Önerilen eylemler:**
- [ ] [Karşı taraf] — [iş sahibi]'ne sor: devam mı?
- [ ] [Karşı taraf] — yenileme fiyatı sınırsız; pazarlık gücü kaybolmadan alternatif teklif al
- [ ] [Karşı taraf] — karşı taraf tacir, kayıtta kanal e-posta: KEP ya da noterle gönder
```

Pencerede ~10'dan fazla kayıt varsa ya da kullanıcı isterse: profilde `## Outputs → Dashboard offer for data-heavy outputs` varsa ona göre pano öner — banda göre sayılar, son gün zaman çizelgesi ve sıralanabilir kayıt.

### Mod 3 — CLM / e-imza taramasıyla kaydı doldur

MCP'ler bağlıysa ve kayıt boş ya da eskiyse (tek seferlik toplu yükleme; sonra giriş inceleme anında olur): (1) CLM'de durumu "aktif" ve yenileme tarihi dolu sözleşmeleri sorgula; (2) e-imza aracında son 24 ayın tamamlanmış zarflarında "abonelik", "yenileme", "otomatik" geçenleri sorgula; (3) her biri için yenileme mekaniğini çıkar, yukarıdaki hesabı yap, kayda ekle; (4) meta veriden tarihi belirlenemeyenleri işaretle — sözleşmeyi bir insanın okuması gerekir.

### Mod 4 — Kaçan pencereler

```markdown
## Kaçan fesih pencereleri

Aşağıdakilerin fesih bildirimi son günü geçti ve kayıtlı fesih yok:

| Karşı taraf | Son gün | Yenileme tarihi | Durum |
|---|---|---|---|
| [ad] | [tarih] | [tarih] | [tarih]'te otomatik yenilenecek |

**Seçenekler:**
- Geç fesih için müzakere (nadiren tutar, sormaya değer)
- Yenilemeyi kabul et, gelecek yılın son gününü şimdiden işaretle
- Sözleşmedeki diğer fesih haklarını kontrol et (sebepsiz fesih, haklı sebeple fesih)
- Yenileme klozu karşı tarafın genel işlem koşuluysa TBK m. 21/25 değerlendirmesi — avukatla
- B2C abonelikte tüketici otomatik uzamaya bağlı tutulamaz (6502 m. 52/3)
```

## Kapı: yenilemeyi kabul ya da fesih

Tarihi izlemek araştırmadır; **harekete geçmek** — fesih bildirimi göndermek, otomatik yenilemenin işlemesine izin vermek, yenileme formunu imzalamak — hukuki sonuçlu adımdır.

Bu adımdan önce profilde `## Who's using this` → Role'e bak. Avukat değilse:

> Bu adımın hukuki sonucu var (ya yeni bir döneme bağlanıyorsunuz ya da ilişkiyi sona erdiriyorsunuz). Bir avukatla görüştünüz mü? Evetse devam edelim. Hayırsa götürmeniz için kısa brif:
>
> [Tek sayfa: karşı taraf, mevcut dönem sonu ve gönderim son günü, kanal ve tampon, yenileme fiyat mekaniği, hiçbir şey yapmazsak ne olur, alternatif tedarikçiler, pencere kapanmadan avukata sorulacak üç soru.]
>
> Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz.

Açık bir "evet" olmadan bu kapıyı geçme.

## renewal-watcher ajanıyla bağlantı

renewal-watcher ajanı bu skill'i zamanlanmış olarak (varsayılan haftalık) çalıştırır ve Mod 2 raporunu profildeki `## House style` → `**Renewal alerts:**` kanalına (yoksa `**Where work product goes:**`) gönderir.

## Bu skill ne yapmaz

- Sözleşme feshetmez ve yenileyip yenilememeye karar vermez; son günü ve iş sahibini gösterir.
- Yenileme tarihini bulmak için sözleşme okumaz — bu inceleme anında olur; kayıtta tarihi olmayan satır elle eklenmiştir ve doldurulmalıdır.
- Fesih bildirimini göndermez ya da noter/KEP işlemi yapmaz.

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
