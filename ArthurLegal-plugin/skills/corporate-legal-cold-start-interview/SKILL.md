---
name: corporate-legal-cold-start-interview
description: >
  Kurumsal pratiğin ilk kurulum görüşmesi ya da `--new-deal` ile işleme özgü bağlam.
  Modülerdir: hangi alanların canlı olduğunu belirler (M&A, Yönetim Kurulu ve Sekretarya,
  Halka Açık Şirket, Şirket Yönetimi) ve yalnız etkin modüllerin sorularını sorup profil
  dosyasına yalnız ilgili bölümleri yazar. Türk pratiğine göre kurulur: büro / şirket içi,
  şirket türü (AŞ, Ltd., halka açık AŞ, yabancı şirket şubesi), grup yapısı, YK karar ve
  GK tutanak formatı, elden dolaştırma emsalleri, şirket uyum takvimi. Yeni kurulumda,
  CLAUDE.md'de hâlâ [PLACEHOLDER] varsa, yeni bir işlem başlarken ya da bağlantıları
  yeniden kontrol etmek veya bir modülü tazelemek için kullan.
argument-hint: "[--redo | --new-deal | --check-integrations | --module [m&a | board | public | entities]]"
---

# /cold-start-interview

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasına bak. `--new-deal` ise doğrudan işlem kurulumuna geç. `--check-integrations` ise görüşme yapma; yalnız Bölüm 0'daki bağlantı kontrolünü yap ve `## Available integrations` tablosunu yeniden yaz — ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse; yapılandırılmış ama denenmemiş bağlantı ⚪ ve tek satır teyit yolu. `.mcp.json` beyanına bakarak ✓ verme.
2. Görüşmeyi yürüt (önce Bölüm 0 — rol ve bağlantılar — sonra modüller).
3. Seed belgeler: etkin modüle göre (M&A: talep listesi + önceki bulgu raporu; Board: YK kararları ve GK tutanakları; Entities: şirket listesi/organizasyon şeması).
4. Çıkar: kategoriler, önemlilik eşikleri, rapor formatı, karar/tutanak formatı, YZ aracı ayarı.
5. **Taşıma:** eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/corporate-legal/*/CLAUDE.md`) `[PLACEHOLDER]` içermeyen bir CLAUDE.md varsa ve ayar yolunda yoksa ayar yoluna kopyala; neyin taşındığını söyle.
6. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` yaz (üst klasörleri oluştur). `--new-deal` için `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` yaz.

**Bölüm ve anahtar adlarını çevirme.** `## Company profile`, `## Who's using this`, `## Available integrations`, `## Outputs`, `## M&A`, `## Board & Secretary`, `## Public Company`, `## Entity Management`, `## Matter workspaces`, `*Active modules:*`, `**Practice setting:**`, `**Escalation:**`, `**Minutes template:**`, `**Consents repository:**`, `**Consent format:**`, `deal-context.md`, `compliance-tracker.yaml`, `closing-checklist.yaml` adları aynen kalır; diğer skill'ler bunları birebir okur. İçerik Türkçe yazılır.

## Kurulum durumu

- Dosya **yok** → görüşmeye başla.
- **`<!-- SETUP PAUSED AT: -->` var** → selamla, o bölümden devam öner.
- **`[PLACEHOLDER]` var, duraklatma notu yok** → baştan ya da yer tutucuların başladığı yerden devam öner.
- **Dolu** → `--redo` ya da `--module [ad]` yoksa çalıştırma.

Bölüm iskeleti `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonundadır. Bayraklar: `--redo` (tam yeniden görüşme), `--module [m&a | board | public | entities]` (tek modül ekle/tazele), `--new-deal` (yalnız işlem bağlamı; M&A modülü), `--full` (hızlı kurulumu genişlet).

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/firm-profile.md` varsa oku ve tek satırla teyit et: "Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu? ('güncelle' derseniz ortak profili değiştiririm.)" Teyitte ortak soruları (pratik ortamı, ad, sektör, ne sattığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri) atla. Yoksa ilk kurulan eklenti budur: bu soruları sor, paketteki `${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md` şablonuna göre yaz, söyle: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak." Modül soruları eklentiye özeldir.

**Kurulum kapsamı:** çalışma klasörü ev dizini değil bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden belge okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

> **`corporate-legal`**, M&A işlemleri, yönetim kurulu ve genel kurul işleri, halka açık şirket uyumu ve grup şirketlerinin yönetimiyle uğraşanlar içindir.
>
> **2 dakika:** rol, pratik ortamı, şirket türü ve modül seçimi; önemlilik eşiği, bulgu raporu, YK karar formatı ve açıklama listesi için çalışan varsayılanlar. **15 dakika:** gerçek önemlilik eşikleriniz, örnek kararlardan ev formatınız, şirket listeniz ve uyum takviminiz, işlem ekibi bilgilendirme sıklığı, eskalasyon matrisi.
>
> Hızlı mı, tam mı? (Sonra `/arthurlegal:corporate-legal-cold-start-interview --full` ile genişletebilirsiniz.)

Seçimi bekle. **Hızlı yol:** yalnız Bölüm 0 ve modül seçimi; diğer her alana `[DEFAULT]`. Kapanış: "Tamam, komutları kullanabilirsiniz. Önemlilik eşiği, açıklama listesi ve karar formatında makul varsayımlar kullandım; bir çıktı yanlış gelirse çoğunlukla ayarlanacak bir varsayımdır ve çıktı hangisi olduğunu söyler. Tam görüşme `--full`, tek bölüm `--redo <bölüm>`."

**Seçimden sonra** tek paragraf: "Bu eklenti profilinizi (önemlilik eşikleri, karar ve tutanak formatı), işlem klasörlerini (inceleme tabloları, kapanış listesi, açıklama listeleri) ve şirket uyum takvimini tutar. Cevaplarınızı her skill'in okuduğu düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve açıkça paylaştığınız belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** Şirket tanıtımı, yetki devri/iç yönerge, imza sirküleri, organizasyon şeması, esas sözleşme için önce belge iste: "Yapıştırın, dosya yolu verin ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular sayılır); ekranı kaydırmadan cevaplanmalı.
- **Uzun cevapta bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, yol verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim." Seed belge atlanırsa çıktılar genel şablonla gelir; bunu söyle.
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste — özellikle etkin modüllerin seed belgeleri]. Şimdi mi, yer tutucu mu?" Sessiz boşluk bırakma.
- **Duraklat/devam:** "dur" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /arthurlegal:corporate-legal-cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte: "Hoş geldiniz, [bölüm]de kalmıştınız. Devam mı, baştan mı?" Cevaplanmış soruyu tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre, nisap, eşik söylenirse `tr_mevzuat_madde_getir` ile çek ve karşılaştır; çelişirse: "[X] dediniz; madde metni [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnekler: "Sirküler YK kararı oybirliği ister" — m. 390/4 en az üye tam sayısının çoğunluğunun yazılı onayını yeterli sayar; esas sözleşmede farklı hüküm varsa ayrıca not et. "Limited şirkette olağan GK'yı yıl içinde istediğimiz zaman yaparız" — hesap döneminin sona ermesinden itibaren üç ay içinde yapılır (m. 617/1). Değişen tutar ve eşikleri (bağımsız denetim eşikleri, Rekabet Kurulu izin eşikleri, idari para cezaları) profile sabit yazma: "güncel eşiği teyit et — dönemsel güncellenir".

## Bölüm 0 — Kim kullanıyor, ne bağlı, pratik ortamı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her rapor, karar ve tutanak taslağındaki üst başlığı belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan** (stajyer avukat, hukuk operasyonu, şirket sekreteryası)
> 2. **Avukata erişimi olan, avukat olmayan** (kurucu, CFO, yatırım ekibi, şirket sekreteri)
> 3. **Düzenli avukat erişimi olmayan**

2 ya da 3 ise bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları hüküm değil, avukatla konuşmanız için araştırma olarak çerçevelerim; (2) hukuki sonucu olan adımlardan önce (kararı imzaya sunma, tutanağı kesinleştirme, sicile başvuru, imza/kapanış) avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım. Bu bir feragat metni değil; doğru anda birkaç saatlik avukat görüşü genellikle hatadan ucuzdur." 3 ise ekle: "Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür, koşullarını baroya sorun."

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantıyı karıştırma.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_mevzuat_madde_getir(number="6102", madde_no="390")`. Cevap geldiyse ✓.
- **Tüzel kişi/LEI (`gleif_`)** — yabancı ana şirket ya da bağlı şirket varsa: `gleif_autocomplete` ile dene.
- **Yabancı ülke araçları** (`uk_`, `de_`, `nl_`, `eu_` …) — yalnız yabancı bağlı şirket varsa; önce `status`.
- **Veri odası (Intralinks, Datasite, Box), YK portalı, belge deposu, takvim, Slack** — deneyebiliyorsan dene; deneyemiyorsan ⚪.

Raporla: ✓ bağlı (denendi) · ⚪ yapılandırılmış, doğrulanmadı — MCP ayarlarından teyit edin · ✗ yok — [özellik] [manuel yönteme] düşer, nasıl bağlanır (ör. "Box bağlı değil. Cowork: Ayarlar → Bağlayıcılar → Box. Claude Code: `/mcp`. Belgeleri yapıştırarak da çalışır."), sonra `--check-integrations`. "Hepsine gerek yok; çekirdek özellikler dosya erişimiyle çalışır." ArthurLegal MCP ✗ ise: "Her madde ve karar atfı 'doğrulanmadı' işaretlenir ve UYARI satırı taşır."

### Pratik ortamı

> Hangisi size uyuyor? (Her skill'in eskalasyon dilini belirler.)
> - **Hukuk bürosu (müvekkil şirketlere kurumsal danışmanlık)** — onay zinciri değil danışma tetikleri sorarım.
> - **Şirket içi hukuk** — eskalasyon matrisi, hukuk müşaviri/genel müdür, ne zaman YK'ya gider.
> - **Tek avukat / küçük büro** — "dış avukata ya da meslektaşa ne zaman danışırsınız".
> - **Kamu / klinik** — denetim modeli ve imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla yazın; kutuya zorlamam, doldurulan/uyarlanan/boş bırakılan alanları işaretlerim.

Dallanma ve kayıt (`## Company profile` altında `**Practice setting:**`):
- **Büro (her tür):** `## Matter workspaces` → `Enabled: ✓`, `Cross-matter context: off`. `**Escalation:**` satırı onay seviyeleri değil danışma tetikleridir. Profile **çıkar çatışması notu** yaz: aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat ve kendi düzenlediği senet veya sözleşmenin hükümsüzlüğünü ileri sürmek durumunda kalan avukat işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Kurumsal işte tipik risk: aynı aile şirketinde pay sahipleri arası uyuşmazlık, büronun daha önce hazırladığı esas sözleşme ya da pay devri sözleşmesine karşı geçersizlik iddiası. Her yeni matter'da kontrolün yapıldığını sor (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`).
- **Şirket içi:** `Enabled: ✗` (tek müvekkil; matter katmanı görünmez). `**Escalation:**` onay zinciridir.
- **Kamu / klinik:** işi kim gözden geçirir, imza zinciri.

**Hemen yaz:** `## Who's using this`, `## Available integrations` ve `## Outputs` bölümlerini profilin ilk bölümünden hemen sonra yaz.

## Bölüm 0.5 — Modül seçimi

> Hangileri düzenli işiniz? (Profilde hangi bölümlerin kurulacağını ve hangi skill'lerin açılacağını belirler; yalnız M&A seçerseniz diğer görüşmeler atlanır.)
> 1. **M&A** — pay/şirket alımı-satımı, yatırım, birleşme, bölünme, iş kolu devri
> 2. **Board & Secretary** — YK toplantı hazırlığı, YK kararları, GK tutanakları, elden dolaştırma kararları, komiteler
> 3. **Public Company** — halka açık ortaklık: KAP açıklamaları, SPK finansal raporlama, kurumsal yönetim
> 4. **Entity Management** — grup şirketleri, şirket uyum takvimi, pay defteri, tescil-ilan
>
> Numaraları söyleyin. Sonra `--module [ad]` ile ekleyebilirsiniz.

Etkin modülleri profilin başındaki `*Active modules:*` satırına yaz; yalnız onların bölümüne geç.

## Bölüm 1 — Şirket profili (her zaman, 2 dk)

Önce: "Yetki devri iç yönergesi (m. 367), imza sirküleri, onay matrisi ya da önceki bir kurumsal yönetim notu var mı? Paylaşırsanız onay seviyelerini ve eskalasyonu oradan çıkarırım." Varsa oku, bulduğunu teyit et, ilgili soruları atla.

Yoksa:
- **Ne iş yapıyor?** Web sitesi, faaliyet raporu ya da KAP sayfası bağlantısı yeter; ya da tek cümle: ne satıyor, kime, nasıl.
- **Kim?** Ticaret unvanı ([Müvekkil]), şirket türü (AŞ / Ltd. / halka açık AŞ / yabancı şirket şubesi), sicil müdürlüğü, sektör ve düzenleyici (BDDK, EPDK, SPK, BTK, Rekabet), hesap dönemi.
- **Grup:** ana şirket ve bağlı şirketler; yabancı ana şirket varsa LEI'yi `gleif_search_entities` / `gleif_get_group_structure` ile teyit et; aile şirketi mi, kurumsal yatırımcı var mı, pay sahipleri sözleşmesi var mı.
- **Hukuk ekibi:** yalnız siz mi, ekip mi?
- **Eskalasyon:** "Bir inceleme yetkinizi aşan bir şey bulduğunda — yeni bir bulgu, önemlilik kararı, menfaat çatışmalı YK kararı, açıklama listesinde takdir gerektiren kalem — kime gider? İsim ya da rol (hukuk müşaviri, yönetici ortak, işlem lideri) ya da 'kendim karar veririm'." (Bunu `/arthurlegal:corporate-legal-diligence-issue-extraction`, `/arthurlegal:corporate-legal-material-contract-schedule`, `/arthurlegal:corporate-legal-written-consent` ve diğerleri kullanır.)

Yetki belgesi yüklenmediyse sonunda öner: "Bunları paylaşılabilir ayrı bir yetki ve eskalasyon notu olarak da yazayım mı?" `## Company profile`'a yaz.

## Bölüm 2M — M&A (etkinse, 4-6 dk)

- **Duruş:** alıcı, satıcı, ikisi? (Ev varsayılanıdır; işlemdeki taraf `--new-deal`'de belirlenir.) Seri alıcı mısınız, her işlem baştan mı? İşlemi kim yürütür — kurumsal gelişim, hukuk, dış büro?
- **İnceleme yapısı:** önce "Standart talep listeniz ya da kapanmış bir işlemin bulgu raporu var mı?" Varsa kategori yapısını, önemlilik eşiklerini, ciddiyet ölçeğini, bulgu biçimini, muhatabı çıkar. Yoksa sor: talep listesi işleve mi belge türüne mi göre; sözleşme incelemesinde önemlilik eşiği (tümü mü, [tutar ve para birimi] üstü mü, gelire göre ilk N mi) — bunu `/arthurlegal:corporate-legal-diligence-issue-extraction` ve `/arthurlegal:corporate-legal-material-contract-schedule` kullanır; veri odası; YZ toplu inceleme aracı (Luminance, Kira vb.) ve güven düzeyi.
- **Türk pratiği soruları:** pay devri mi malvarlığı devri mi tercih; Rekabet Kurulu izni değerlendirmesini kim yapar (eşikleri profile sabit yazma; `tr_kurum_karari_ara` ile Rekabet kararlarına bakılabilir); yabancı yatırımcı taraf oluyor mu.
- **Satıcı tarafı (varsa):** veri odasına neyin gireceğine kim karar verir; alıcının bulacaklarını öngören bir açıklama notu hazırlanıyor mu; iş tarafında kimle koordine edilir. Satıcı tarafı, alıcı tarafının tersi değildir: gelen belge incelemesi değil, dışarı giden bilginin yönetimidir.
- **Kapanış ve bilgilendirme:** kapanış listesi nerede (Excel, `closing-checklist.yaml`, işlem aracı), kim günceller; işlem ekibi ne sıklıkla, hangi kanaldan bilgilendirilir; iş tarafı neyi gerçekten okur.

Seed belge yoksa öner: "Söylediklerinize göre başlangıç talep listesi ve bulgu raporu iskeleti yazayım mı?" `## M&A`'ya yaz.

## Bölüm 2B — Board & Secretary (etkinse, 3-4 dk)

- **Rol:** YK sekreteri, hukuk müşaviri, dış büro olarak karar hazırlayan?
- **Organlar:** YK üye sayısı ve yapısı (tüzel kişi üye ve adına tescilli gerçek kişi, m. 359/2; halka açıksa bağımsız üyeler); komiteler (denetimden sorumlu, riskin erken saptanması, kurumsal yönetim, diğer); Ltd. ise müdürler ve müdürler kurulu başkanı (m. 624/1).
- **Takvim:** yılda kaç YK toplantısı, hangi aylar; olağan GK genellikle hangi ay (son sınır dönem sonundan itibaren 3 ay, m. 409/1).
- **Araçlar:** YK portalı ya da e-posta; elektronik toplantı/oy esas sözleşmede öngörülmüş mü (m. 1527/1); GK iç yönergesi tescilli mi (m. 419/2).
- **Defterler:** YK karar defteri ve GK toplantı ve müzakere defteri fiziki mi, elektronik mi (m. 64/3-4); kim tutar?
- **Tutanak/karar biçimi:** uzun anlatı, yalnız karar, karma? Ne kadar sürede yazılır, nasıl onaylanır (dolaştırma, sonraki toplantı)?
- **Elden dolaştırma:** rutin olarak hangi işler için (imza yetkisi, banka, müdür atama, GK çağrısı)? Toplantı şartı koyan esas sözleşme hükmü ya da iç kural var mı?

**Seed kararlar ve tutanaklar (board-minutes için gerekli):**

> Kapanmış toplantılardan 5-6 YK kararı ve en az bir GK tutanağı yükleyin; komite tutanağınız varsa onu da. Bunlar ev formatınızı öğretir: başlık, katılım ve nisap kaydı, tartışma derinliği, karar dili, ek numaralandırma, imza blokları. Şimdi yoksa sonra `--module board` ile eklenir; board-minutes eksikse ister.

Çıkar ve `## Board & Secretary` → `**Minutes template:**` bloğuna yaz: yapı ve sıra; başlık; katılım/nisap kaydı; tartışma derinliği; karar dili ("... kabulüne", "... onaylanmasına karar verildi"); ek atfı; imza bloğu; her tutanakta tekrarlanan kalıp cümleler.

**Emsal kararlar deposu (written-consent için gerekli):**

> İmzalanmış elden dolaştırma kararlarının durduğu bir klasör var mı? (written-consent en yakın emsali orada arar.) Varsa yolunu söyleyin. Yoksa 3-5 örnek karar yükleyin; biçimi öğrenirim, emsal araması depo kurulunca açılır.

Çıkar: karar dili, gerekçe yapısı, yetkilendirme kalıbı, onay/imza bloğu, deftere geçirme notu. `**Consents repository:**` ve `**Consent format:**` satırlarına yaz.

**Yıllık döngü:** olağan GK gündemi (finansal tablolar, faaliyet raporu, ibra, YK seçimi ve ücretler, kâr dağıtımı, denetçi seçimi — m. 409/1, 408/2), YK görev süresi bitişleri (m. 362/1), bağlılık raporu (m. 199/1). `## Board & Secretary`'ye yaz.

## Bölüm 2P — Public Company (etkinse, 3-4 dk)

- Borsa İstanbul pazarı; hesap dönemi; ara dönem finansal rapor takvimi (SerPK m. 14 çerçevesinde SPK düzenlemesine göre — tarihleri SPK düzenlemesinden teyit et).
- **Özel durum açıklamaları (SerPK m. 15):** KAP açıklamasını kim hazırlar, kim onaylar; erteleme kararı süreci; hukuk ne zaman devreye girer.
- **Kurumsal yönetim (SerPK m. 17):** bağımsız üyeler, komiteler, ilişkili taraf işlemlerinde bağımsız üye onayı süreci (m. 17/3).
- **İçeriden bilgi ve işlem yasakları:** içsel bilgiye erişenler listesi, yönetici işlem bildirimleri, kapalı dönemler — ilgili SPK düzenlemesini `tr_kurum_karari_ara` (spk) ve `tr_spk_bulten_icinde_ara` ile teyit et; kuralı profile ezberden yazma.
- **GK:** çağrı en az üç hafta önce internet sitesi ve KAP ile (SerPK m. 29/1); elektronik GK.

`## Public Company`'ye yaz.

## Bölüm 2E — Entity Management (etkinse, 2-3 dk)

> Organizasyon şeması ya da şirket listesi varsa (kaba bir tablo da olur) yükleyin; unvanları, türleri, ülkeleri, pay oranlarını ve faaliyetsiz şirketleri çıkarırım. (entity-compliance uyum takvimini bu listeden kurar.)

Yükleme yoksa sor: kaç aktif şirket; ülkeler (yalnız Türkiye mi); her şirketin türü ve sicil müdürlüğü, MERSİS numarası; hesap dönemi; bağımsız denetime tabi mi (eşikler Cumhurbaşkanı kararıyla belirlenir, m. 397/4 — güncel eşiği teyit et); defterler fiziki mi elektronik mi; pay defterini kim tutar (m. 499, 594); rutin işleri kim yürütür (mali müşavir, şirket içi, dış büro); yurt dışı şirketlerde yerel ajan; şube varsa ticari mümessil (m. 40/4); grup içi sözleşmeler (hizmet, lisans, borç).

`## Entity Management`'a şirket tablosuyla yaz: | Unvan | Tür | Ülke/sicil | MERSİS | Pay sahibi ve oran | Hesap dönemi | Denetim | Durum |.

## Profili yazma — Outputs

`## Outputs` üst başlığı role göre:
- Rol avukatsa: `GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ` (avukatın görevi dolayısıyla öğrendiklerini açığa vurma yasağı, Av. K. m. 36).
- Rol avukat değilse: `ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — İŞLEM ÖNCESİ AVUKATLA GÖZDEN GEÇİRİN`
Sicile, deftere ya da karşı tarafa gidecek karar, tutanak ve açıklama listelerinden başlık çıkarılır. Başlık tek başına koruma yaratmaz.

## Yazdıktan sonra

> **Neler yapabildiğimi görmek ister misiniz?** Veri odasından bulgu çıkarma (`/arthurlegal:corporate-legal-diligence-issue-extraction`), önemli sözleşmeler listesi (`/arthurlegal:corporate-legal-material-contract-schedule`), elden dolaştırma kararı (`/arthurlegal:corporate-legal-written-consent`), YK kararı ve GK tutanağı (`/arthurlegal:corporate-legal-board-minutes`), şirket uyum takvimi (`/arthurlegal:corporate-legal-entity-compliance`), kapanış listesi (`/arthurlegal:corporate-legal-closing-checklist`), kapanış sonrası entegrasyon (`/arthurlegal:corporate-legal-integration-management`). **Önerim:** canlı işlem varsa `/arthurlegal:corporate-legal-closing-checklist`; yoksa yaklaşan olağan GK için `/arthurlegal:corporate-legal-entity-compliance --report`.

Kullanıcı somut bir iş söylediyse listeyi atla. Sonra etkin modülleri ve kontrol edilecekleri göster: zayıf/belirsiz cevaplar; M&A etkin ve seed yoksa "talep listesi ve bulgu raporunu gönderince bölümü güncellerim"; M&A etkinse "yeni işlemde `--new-deal`"; Board etkinse written-consent ve board-minutes hazır; Entities etkinse `/arthurlegal:corporate-legal-entity-compliance --init`; Public etkinse "bu modülün skill'leri sonraki sürümde; profil bölümü hazır". ArthurLegal MCP bağlı değilse: "Bağlarsanız madde atıflarını canlı doğrularım."

**Kapanış:**
> "Profiliniz `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasında — düz metin, doğrudan düzenleyebilirsiniz. Tam yeniden görüşme `--redo`, tek modül `--module [m&a | board | public | entities]`, bağlantı kontrolü `--check-integrations`, tek değişiklik `/arthurlegal:corporate-legal-customize`. En sık ayarlananlar: M&A önemlilik eşikleri, açıklama listesi ve bulgu raporu biçimi, şirket takvimi sıklığı.
>
> **Profiliniz öğrenir.** Bir çıktı yanlış gelirse çoğunlukla ayarlanacak bir duruştur; çıktı hangisi olduğunu söyler. On dakikalık kurulum çalışan bir profil verir; bir aylık kullanım sizin yazmış gibi okunan bir profil."

## İşlem kurulumu (`--new-deal`, yalnız M&A)

Ev yaklaşımı profilde kalır; yalnız işleme özgü bağlamı sor: işlem kod adı · bu işlemdeki taraf (alıcı/satıcı) · hedef ya da alıcı · işlem yapısı (pay devri, malvarlığı devri, birleşme, sermaye artırımıyla giriş) · veri odası yeri · işlem lideri · imza ve kapanış tarihleri · işleme özgü eşik farkı · dış büro ve sorumlu avukat · Rekabet Kurulu izni ya da sektör düzenleyicisi onayı gerekiyor mu (değerlendirme avukatta; eşik yazma) · büroda çatışma kontrolü yapıldı mı (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`). `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code-name]/deal-context.md` yaz. Skill'ler profili (ev) ve `deal-context.md`'yi (işlem) okur; çelişkide `deal-context.md` önce gelir. Matter çalışma alanı açıksa ilgili matter'ın `matter.md`'sine deal kodunu yaz.

## Profil kalite kontrolü ve kaçınılacaklar

Bitirmeden yazılanı yeniden oku: yer tutucu kalan bölüm (sor), seed belgesi olmayan etkin modül (not et), `*Active modules:*` satırı tam mı.

- **Tüm modülleri etkin varsayma;** önce sor.
- **Alıcı tarafını sabitleme;** ev profili taraftan bağımsız, taraf `--new-deal`'de.
- **Genel yer tutucu yazma;** "standart eşikler" denirse sayıyı ve para birimini iste.
- **Satıcı tarafı alıcı tarafının tersi değildir;** satıcı tarafı etkinse bu ayrımı işaretle.
- **Etkin olmayan modül için seed isteme.**
- Var olmayan skill vaat etme; profil doluysa her oturumda çalıştırma.

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
