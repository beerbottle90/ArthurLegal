---
name: regulatory-legal-cold-start-interview
description: >
  İlk kurulum — izlenecek düzenleyici kurumları (EPDK, BDDK, SPK, BTK, KVKK,
  Rekabet Kurumu, GİB, Sigorta Tahkim, Resmî Gazete'deki bakanlık ve
  Cumhurbaşkanlığı düzenlemeleri, gerekiyorsa AB/İngiltere/Almanya vb.) listeler,
  politika kütüphanesini dizinler, önemlilik eşiğini, tarama sıklığını ve özetin
  kime gideceğini öğrenir; böylece izleme gürültü değil sinyal üretir. İlk
  kurulumda, CLAUDE.md eksik ya da placeholder içeriyorsa, yeniden yapılandırmada
  (--redo) ya da bağlantıları yeniden denemek için (--check-integrations) kullan.
argument-hint: "[--redo | --full | --check-integrations]"
---

# /cold-start-interview

1. `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasına bak. Eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/regulatory-legal/*/CLAUDE.md`) doldurulmuş bir profil varsa ve ayar yolunda yoksa ayar yoluna kopyala, neyin taşındığını söyle. `--check-integrations` verildiyse görüşmeyi atla; yalnız Bölüm 0'daki "Ne bağlı?" kontrolünü çalıştır ve `## Available integrations` tablosunu yeniden yaz.
2. Görüşmeyi yürüt: önce Bölüm 0 (rol, pratik ortamı, bağlantılar), sonra izleme listesi, önemlilik, politika kütüphanesi, akışlar.
3. Politika klasörünü bağla ve dizinle.
4. Profili ayar yoluna yaz (üst klasörleri gerekirse oluştur).

Bağlantı denerken ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse verilir; yapılandırılmış ama denenmemiş bağlantı ⚪ (nasıl teyit edileceğine dair tek satırla). `.mcp.json` beyanına bakarak ✓ verme.

## Amaç

Her kurum her gün bir şey yayımlar; çoğu sizi ilgilendirmez. Bu görüşme hangi kurumların izleneceğini ve — asıl önemlisi — burada "önemli"nin ne demek olduğunu öğrenir. Her özet, karşılaştırma ve açık raporu bu profili okur; genel profil, her kurul duyurusunu idari para cezası gibi işleyen bir özet demektir.

## Kurulum durumu

- **Dosya yok** → görüşmeye başla.
- **`<!-- SETUP PAUSED AT: -->` var** → selamla, o bölümden devam etmeyi öner.
- **`[PLACEHOLDER]` var, duraklatma notu yok** → baştan başlamayı ya da placeholder'ların başladığı yerden devam etmeyi öner.
- **Dolu** → kurulmuş; `--redo` yoksa atla.

Bölüm iskeleti `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonundadır. **Anahtarları çevirme:** `## Regulators we watch`, `## Who's using this`, `## Available integrations`, `## Policy library`, `## Materiality threshold`, `## Gap response process`, `## Feed configuration`, `## Outputs`, `## Matter workspaces`, `**Check cadence:**`, `**Comment tracking:**`, `**Default comment decision owner:**`, `Digest output path`, `Enabled`, `Active matter:`, `Cross-matter context` — `/arthurlegal:regulatory-legal-reg-feed-watcher`, `/arthurlegal:regulatory-legal-gaps`, `/arthurlegal:regulatory-legal-comments` ve `reg-change-monitor` ajanı bunları birebir okur. İçerik Türkçe yazılır.

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/firm-profile.md` dosyasına bak.
- **Varsa:** oku, tek satırla teyit et: "Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu? (Değiştirmek için 'güncelle' deyin.)" Teyit edilirse ortak soruları atla.
- **Yoksa:** ilk kurulan eklenti budur; ortak soruları sor, paketteki `${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md` şablonuna göre yaz ve söyle: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak."

Ortak profile ait sorular (varsa tekrar sorulmaz): pratik ortamı, ad, sektör, ne satıldığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri. İzleme listesinin ayrıntısı, önemlilik eşiği, politika kütüphanesi ve akışlar bu eklentide kalır.

## Kurulum kapsamı

Çalışma klasörü ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Politikalarınız başka yerdeyse kullanıcı kapsamında kurun (QUICKSTART.md)." Devam mı, yeniden kurulum mu — onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

> **`regulatory-legal`** mevzuat ve kurum kararı değişikliklerini izleyen, iç politikalardaki açıkları bulan ve uyum yükümlülüklerini yöneten ekip içindir.
>
> **2 dakika:** rolünüz, pratik ortamınız, ana düzenleyiciniz; gerisi varsayılan. **15 dakika:** tam izleme listesi, önemlilik eşiği, tarama sıklığı, özetin alıcıları, politika kütüphanesi dizini, taslak düzenleme görüş takibi.
>
> Hızlı mı, tam mı? (Sonra `/arthurlegal:regulatory-legal-cold-start-interview --full` ile genişletebilirsiniz.)

Kullanıcının ev dizinindeki `~/CLAUDE.md`'yi ya da kişisel hafızasını okuyarak görüşmeyi önceden doldurma. Seçimden sonra tek paragraf oryantasyon: "Bu eklenti profilinizi (izleme listesi, önemlilik eşiği, tarama sıklığı), bir açık takip kaydını, politika karşılaştırma arşivini ve taslak düzenleme görüş takvimini tutar. Cevaplarınızı her seferinde okunan düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir. Kurulum yalnız sizin yazdıklarınızdan ve verdiğiniz belgelerden profil kurar; sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

**Hızlı yol:** yalnız Bölüm 0 ve izleme listesinin kapsamı; diğer alanlara `[DEFAULT]` yaz (varsayılan eşik aşağıda). Kapanış: "Tamam, komutları kullanabilirsiniz. Önemlilik eşiği, tarama sıklığı ve politika kütüphanesi için makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanması gereken bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--full`, tek bölüm için `--redo <bölüm>`."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** İzleme tablosu, uyum takvimi, eski açık analizi, politika dizini için önce bağlantı/yapıştırma iste: "Belgeyi yapıştırın ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli.
- **Uzun cevap gerekiyorsa bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste]. Şimdi doldurmak ister misiniz, placeholder olarak mı kalsın?" Sessiz boşluk bırakma.
- **Duraklat/devam:** "dur", "sonra devam" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — run /arthurlegal:regulatory-legal-cold-start-interview to resume -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte cevaplanmış soruyu tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre ya da eşik söylerse `tr_mevzuat_madde_getir` ile çek ve karşılaştır; çelişirse: "[X] dediniz; metin [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnek: Rekabet soruşturmasında yazılı savunma süresi rapor tebliğinden itibaren otuz gündür; haklı gerekçeyle bir kez, en çok bir katına kadar uzatılabilir (4054 s. Kanun m. 45/2). İdari para cezası tutarlarını profile yazma: "güncel tutarı teyit et — dönemsel güncellenir."

## Bölüm 0 — Kim kullanıyor, ne bağlı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her çıktının üst başlığını belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan**
> 2. **Avukata erişimi olan, avukat olmayan** (uyum yöneticisi, iş birimi)
> 3. **Düzenli avukat erişimi olmayan**

2 ya da 3 ise bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları hüküm değil, avukatla konuşmanız için araştırma olarak çerçevelerim; (2) hukuki sonucu olan adımlardan önce — kuruma yazı ya da savunma, taslak düzenlemeye görüş gönderme, uyum beyanı, açığı 'kapandı' sayma — avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım." 3 ise ekle: "Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür, koşullarını baroya sorun." `## Who's using this` altına `**Role:**` ve (avukat değilse) `**Attorney contact:**` yaz.

### Pratik ortamı

> Hangisi size uyuyor? (Açık yönetimini ve eskalasyon dilini belirler.)
> - **Tek avukat / küçük büro** — onay zinciri sormam; "dış meslektaşa danış" yazarım.
> - **Orta / büyük büro** — onay zinciri, üstünüzde kim imzalar.
> - **Kurum içi hukuk / uyum** — eskalasyon matrisi, hukuk müdürü, uyum yöneticisi, ne zaman iş birimine gider.
> - **Kamu / klinik** — denetim modeli, dış yazışmada imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla yazın; profili ona göre kurar, doldurulan, uyarlanan ve boş kalan alanları işaretlerim.

Dallanma:
- **Büro (her tür):** `## Matter workspaces` → `**Enabled:** ✓`, `**Cross-matter context:** off`. Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Aynı sektörde birden fazla müvekkil izleniyorsa (ör. biri diğeri hakkında Rekabet Kurumuna başvuruyor) her yeni matter'da çatışma kontrolünü sor (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`). İzleme taraması uygulama düzeyinde çalışır; müvekkile özgü değerlendirme matter'a yazılır.
- **Kurum içi:** `**Enabled:** ✗`.

Sonra eskalasyonu sade sor: "Bir inceleme üst onay gerektiren bir şey bulduğunda — şirket kararı gerektiren politika açığı, şirket adına görüş içeren yazı, uygulamayı değiştiren önemli bir düzenleme, yetkinizi aşan bir karar — kime gider? İsim ya da rol (hukuk müdürü, uyum yöneticisi), ya da 'kendim karar veririm'." Cevabı `**Practice setting:**` olarak `## Who's using this` altına, eskalasyonu `## Gap response process` → `**Escalation for material gaps:**` satırına yaz.

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantı farklıdır.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_resmi_gazete_fihrist()` (bugünün fihristi) ve izlenecek kurumlardan biri için `tr_kurum_karari_ara(kurum="rekabet", query="birleşme", limit=3)`. Cevap geldiyse ✓. Sonuç ince gelirse önce `status`: yüklenememiş kaynak "karar yok" demek değildir.
- **Yabancı ülke araçları** (`eu_`, `uk_`, `de_` …) — yalnız yabancı rejim izlenecekse dene.
- **Thomson Reuters Regulatory Intelligence** (ücretli, isteğe bağlı), **belge deposu** (Google Drive, SharePoint, Box), **Slack** — deneyebiliyorsan dene; deneyemiyorsan ⚪.

Rapor:
> - ✓ [Bağlantı] — bağlı (denendi)
> - ⚪ [Bağlantı] — yapılandırılmış, doğrulanmadı; MCP ayarlarınızdan teyit edin
> - ✗ [Bağlantı] — yok; [özellik] [manuel yönteme] düşer. Sonra bağlarsanız `--check-integrations` çalıştırın.

ArthurLegal MCP ✗ ise: "Türk kaynakları için otomatik akış yok; yalnız yapıştırdığınız metinle çalışırım ve her atıf 'doğrulanmadı' işaretiyle, UYARI satırıyla gelir."

**Hemen yaz:** `## Who's using this`, `## Available integrations` ve `## Outputs` (role göre üst başlık).

## Bölüm 1 — İzleme listesi (2-3 dk)

*(`/arthurlegal:regulatory-legal-reg-feed-watcher` ve `reg-change-monitor` ajanını besler; listede olmayan kurum, siz `/arthurlegal:regulatory-legal-policy-diff`'e yapıştırana kadar görünmez.)*

**[Müvekkil] ne yapıyor?** En önemli bağlam budur. Web sitesi, "hakkımızda" sayfası ya da faaliyet raporu bağlantısı yeter; ya da tek cümle: ne satıyorsunuz, kime, nasıl. Hangi lisans, izin ya da bildirimlerle çalışıyorsunuz? Büroysanız: izlediğiniz müvekkil sektörleri.

Önce sor: "Mevcut bir izleme tablonuz, uyum takviminiz ya da eski bir açık analizi notunuz var mı? Yapıştırın; kurumları ve önemlilik ölçütlerini ben çıkarayım." Yoksa satır satır kur (her kurum için **neden** izlendiğini de yaz):

| Kurum | Ne zaman izlenir (doğrulanmış dayanak) | ArthurLegal aracı |
|---|---|---|
| **EPDK** | Elektrik piyasasında üretim, iletim, dağıtım, toptan ve perakende satış, piyasa işletim, ithalat, ihracat ve toplayıcılık lisans almak koşuluyla yürütülür (6446 s. Kanun m. 4/1). Doğal gaz, petrol, LPG lisansı varsa ilgili kanunu `tr_mevzuat_ara(query="Doğal Gaz Piyasası", types=["KANUN"])` ile bul, maddeyi ilk konuda çek. | `tr_kurum_karari_ara(kurum="epdk", market="elektrik"\|"dogalgaz"\|"petrol"\|"lpg")` — yalnız yapısal Kurul kararları; bireysel lisans işlemleri RG fihristinde. RG: `tr_resmi_gazete_tara(konu="enerji", query=…)` |
| **BDDK** | Mevduat, katılım, kalkınma ve yatırım bankaları, yabancı bankaların Türkiye şubeleri ve finansal holding şirketleri Bankacılık Kanununa tabidir (5411 s. Kanun m. 2); Kurul ikincil düzenleme yapar (m. 88/a). | `tr_kurum_karari_ara(kurum="bddk", query=…)` (başlıkta arar); metin için `tr_semantik_ara(kurum="bddk", query=…)` |
| **TCMB** (ödeme / e-para) | Ödeme kuruluşu faaliyet iznini Merkez Bankası verir, izin kararı RG'de yayımlanır (6493 s. Kanun m. 3/1-b, m. 15/1). Fintech "BDDK" derse bu ayrımı sor. | Kurum kararı aracı yok → RG: `tr_resmi_gazete_tara(query="Merkez Bankası")`, `tr_mevzuat_ara` |
| **SPK** | Kurul, kamunun zamanında, yeterli ve doğru aydınlatılması için genel ve özel nitelikte kararlar alır (6362 s. Kanun m. 128/1-b). Halka açık şirket, aracı kurum, portföy yönetimi vb. | Kararlar haftalık bültende: `tr_kurum_karari_ara(kurum="spk", year=2026)` → `tr_spk_bulten_icinde_ara(bulten="2026/NN", query=…)`; tebliğler `tr_mevzuat_ara(query="Sermaye Piyasası")` |
| **BTK** | Elektronik haberleşme hizmeti sunmak ya da şebeke/altyapı işletmek isteyen şirket faaliyete başlamadan önce Kuruma bildirimde bulunur (5809 s. Kanun m. 9/2); Kurum, işletmeciler ile tüketicileri ilgilendiren Kurul kararlarını kamuoyuna açık tutar (m. 6/1-ç). | `tr_kurum_karari_ara(kurum="btk", date_from=…, date_to=…)`; metin için `tr_semantik_ara(kurum="btk")` |
| **KVKK** | Kurul şikâyetleri karara bağlar, resen inceler, düzenleyici işlem yapar ve idari yaptırıma karar verir (6698 s. Kanun m. 22/1-b, c, e, ğ). Kişisel veri işleyen her şirket için. | `tr_kurum_karari_ara(kurum="kvkk", params={"scan_pages": 1})`; arşiv `tr_semantik_ara(kurum="kvkk")`. Ayrıntılı KVKK uyumu: `/arthurlegal:privacy-legal-policy-monitor` |
| **Rekabet Kurumu** | Hangi birleşme ve devralmaların izne tabi olduğunu Kurul tebliğle ilan eder (4054 s. Kanun m. 7/2); Kurul resen soruşturur, idari para cezası verir, tebliğ çıkarır (m. 27/a, f). Pazar payı yüksek, birleşme yapan ya da dağıtım ağı olan şirket için. | `tr_kurum_karari_ara(kurum="rekabet", decision_type="birlesme_devralma"\|"rekabet_ihlali"\|…)`; çok kelimeli ifadeyi tırnakla ara. RG: `konu="rekabet"` |
| **GİB** | Mükellefin izahat talebine özelgeyle cevap verilir; aynı durumdaki tüm mükellefler için sirküler yayımlanabilir; özelgeler internette yayımlanır (213 s. VUK m. 413). | `tr_kurum_karari_ara(kurum="gib", query=…, date_from=…)` — özelge kapsar, bağlayıcı değildir; sirküler için GİB sitesi. RG: `konu="vergi"` |
| **Sigorta Tahkim Komisyonu** | Sigorta ettiren ile riski üstlenen arasındaki uyuşmazlıklar için kurulur (5684 s. Kanun m. 30/1). Düzenleyici değil, hakem kararı: emsal izleme. Sigorta düzenleyicisi SEDDK için kurum kararı aracı yok → RG. | `tr_kurum_karari_ara(kurum="sigorta_tahkim", issue=…)`; arşiv `tr_semantik_ara(kurum="sigorta_tahkim")` |
| **Bakanlıklar, Cumhurbaşkanlığı** | Sektör bakanlığı yönetmelikleri, Cumhurbaşkanı kararları, kanun ve torba kanunlar | `tr_resmi_gazete_tara(date_from, date_to, query=…)` (≤60 gün, gün başına bir istek); `tr_mevzuat_ara(types=["KANUN"], rg_date_from=…, rg_date_to=…, konu=…)` |
| **Yargı** | Kanun veya CBK'yı iptal eden AYM kararı RG'de yayımlandığı tarihte yürürlüğü sona erdirir ya da en çok bir yıl ertelenir (Anayasa m. 153/3); Danıştayın düzenleyici işlem iptalleri | `tr_aym_ara(kind="norm", query="<kanun adı>")`; `tr_ictihat_ara(courts=["DANISTAYKARAR"], query=…)` |

`konu` bir ön elemedir, kapsam garantisi değildir; yayım teyidi için `query` ve fihrist kullanılır.

**ArthurLegal'da olmayanlar:** KİK, Sayıştay, TÜRKPATENT ve İSTAÇ için kaynak yok (resmî uçları cevap vermiyor). Kullanıcı bunları sayarsa açıkça söyle; RG'de yayımlanan yönetmelik ve tebliğleri `tr_resmi_gazete_tara` ile yakalayabileceğini, kurul kararları için kurumun sitesinden manuel izleme ya da RSS adresi gerektiğini ekle. Sonuç uydurma.

**Yabancı rejimler** — varsayma; AB'ye ihracat, AB'de şube, AB'li müşteri, yabancı halka arz var mı, sor.
- **AB:** `eu_search_eu_law(query="…")`, metin `eu_get_document_text(celex=…)`. **Birleşik Krallık:** `uk_search_legislation`, değişiklik etkileri `uk_get_effects`. **Almanya:** yeni yayımlar `de_recent_changes(since_iso=…)`. **Finlandiya** `fi_recent_changes`, **İspanya** günlük resmî gazete `es_get_daily_gazette`; **Hollanda, Polonya, Avusturya, İrlanda, Japonya, Azerbaycan:** ilgili önekli arama aracı (`nl_`, `pl_`, `at_`, `ie_`, `jp_`, `az_`).
- **ABD ve listede olmayan ülkeler:** "ArthurLegal'da bu ülkenin kaynağı yok; ABD kurumu izlenecekse Federal Register API (herkese açık uç) ya da kurumun RSS adresi `Free feeds` tablosuna yazılır; yorum için o ülkenin hukukçusu."

Sonda: "İzlemediğiniz ama belki izlemeniz gereken bir kurum var mı?" ve izleme listesi yüklenmediyse: "Bunu ekibe dağıtabileceğiniz ayrı bir izleme listesi notu olarak da yazayım mı?"

## Bölüm 2 — Önemlilik eşiği (asıl soru, 3-4 dk)

*(Bir gelişmenin anında mı, haftalık özette mi, hiç mi görüneceğine karar veren süzgeç. Yanlış ayar = okunmayan özet.)*

Her örnek için sor: anında mı, haftalık özette mi, hiç mi?
- İzlenen kurumun yeni yönetmeliği, tebliği ya da düzenleyici Kurul kararı
- Sektör kanununuzda değişiklik (torba kanun dahil) ya da Cumhurbaşkanı kararı
- Aleyhinize sonuç doğuran yeni düzenleyici işlem — **not:** ilanı gereken düzenleyici işlemde iptal davası süresi ilan tarihini izleyen günden başlar; özel kanunda ayrı süre yoksa idare mahkemesinde altmış, vergi mahkemesinde otuz gündür (İYUK m. 7/1, 7/4). Bu yüzden varsayılanı "anında"dır.
- Taslak düzenlemenin görüşe açılması
- Sektörünüzde bir şirkete soruşturma ya da idari para cezası; sektör dışında ama yaptığınız bir faaliyete ceza
- Rekabet Kurulu taahhüt ya da uzlaşma kararı — uzlaşma ihlalin kabulünü gerektirir, para cezasında yüzde yirmi beşe kadar indirim sağlar (4054 m. 43/5, 43/7); taahhüt açık ve ağır ihlallerde kabul edilmez (m. 43/3)
- AYM iptal kararı ya da Danıştayın yürütmeyi durdurma/iptal kararı
- GİB özelgesi (başvurana verilir) ya da sirküler (tüm mükellefler için)
- Kurum rehberi, kılavuzu, duyurusu (bağlayıcı değil); Kurul başkanı konuşması, basın açıklaması

Kalibrasyon şirketten şirkete değişir: hakkında soruşturma ya da taahhüt kararı olan şirket konuşmaları bile izler; kurumun hiç tanımadığı şirket görmezden gelebilir. Ölçüt yüklenmediyse sonda öner: "Bu önemlilik ölçütünü ekibin aynı ayarla okuması için ayrı bir not olarak yazayım mı?"

## Bölüm 3 — Politika kütüphanesi (2-3 dk)

*(`/arthurlegal:regulatory-legal-policy-diff` ve `/arthurlegal:regulatory-legal-gaps`'i besler; her değişiklik bu kütüphaneyle karşılaştırılır.)*

Önce: "Politika dizininiz (tablo, içindekiler, wiki sayfası) var mı? Yapıştırın; içe aktarayım." Yoksa:
- Politikalar nerede? (Drive, SharePoint, Confluence, Notion, yerel klasör) — "Klasörü gösterin, dizinleyeyim."
- Adlandırma kuralı ya da dizin var mı?
- Hangi politikanın sahibi kim? (Açıkları doğru kişiye yönlendirmek için.) İç yönetmelik, prosedür, uyum programı (rekabet, KVKK, sektör) ve sözleşme şablonlarını ayrı satır yap.

Dizin yüklenmediyse sonda öner: "Yeni gelen hukuk müdürü ya da uyum yöneticisinin ilk gün okuyacağı ayrı bir politika sahipliği dizini olarak yazayım mı?"

## Bölüm 4 — Akışlar, sıklık, alıcılar (2-3 dk)

**Adım 1 — Ücretsiz akışlar (her zaman etkin):** ArthurLegal MCP bağlıysa izleme listesindeki her Türk kurumu için yukarıdaki araç; RG için `tr_resmi_gazete_tara`. Kurumun duyuru sayfası ya da RSS adresini kullanıcıdan al — adresler değişir, ezberden adres yazma. Akışı olmayan kurum için: "Bu kurumu şimdi nasıl takip ediyorsunuz?" diye sor ve manuel girişi kaydet.

**Adım 2 — Ücretli abonelikler (ek, zorunlu değil):** Thomson Reuters Regulatory Intelligence var mı, hangi uyarılar? Ticari mevzuat veri tabanı aboneliği varsa uyarı e-postaları manuel girişle işlenir. CourtListener yalnız ABD izleniyorsa.

**Adım 3 — Manuel giriş:** "Bülten, meslek kuruluşu duyurusu ya da dış avukat notunda gördüğünüz bir gelişmeyi yapıştırın; politikalarınızla karşılaştırır, açıkları takip ederim." Profilde etkin işaretle.

**Adım 4 — Taslak görüş takibi** (`/arthurlegal:regulatory-legal-comments`'i besler): "İzlenen bir kurum taslak düzenlemeyi görüşe açtığında son tarihi kaydedip görüş verip vermeyeceğinize karar vermeniz için işaretleyeyim mi?" Evet ise etkinleştir ve varsayılan karar sahibini yaz. Görüşe açma usulü kurumdan kuruma değişir; son tarihi kurumun duyurusundan al, uydurma.

**Adım 5 — Sıklık ve alıcılar:** Tarama günlük mü haftalık mı? (Enerji, finans gibi hareketli alanda günlük; aksi hâlde haftalık.) Özet kime gider — kişi/rol, Slack kanalı, e-posta listesi? Dosya da yazılsın mı, hangi klasöre? (Boşsa `~/regulatory-legal-digests/`.)

## Profili yazma

Şablon iskeletine göre; kısa örnek:

```markdown
# Regulatory Practice Profile
*Kurulum görüşmesiyle [TARİH] yazıldı. Doğrudan düzenlenebilir.*
## Regulators we watch
| Regulator | Jurisdiction | Why we watch | Feed source |
|---|---|---|---|
| EPDK | TR | [elektrik üretim lisansı — 6446 m. 4/1] | tr_kurum_karari_ara(kurum="epdk", market="elektrik") + RG konu="enerji" |
| [kurum] | [TR/AB/…] | [neden] | [araç / RSS / manuel] |

## Who's using this
**Role:** [...] · **Attorney contact:** [...] · **Practice setting:** [...]
## Available integrations
| Integration | Status | Fallback if unavailable |
|---|---|---|
| ArthurLegal MCP (tr_) | [✓/⚪/✗] | Yapıştırılan metin; atıflar UYARI satırıyla |
| Thomson Reuters Regulatory Intelligence | [✓/⚪/✗] | Ücretsiz akışlar + manuel giriş |
| Document storage | [✓/⚪/✗] | Yerel klasörden dizin |
| Slack | [✓/⚪/✗] | Özet yalnız dosya olarak |

## Policy library
**Location:** [...]
**Policies indexed:**
| Policy | File | Last updated | Owner |
|---|---|---|---|

## Materiality threshold
**Always material (alert immediately):**
- İzlenen kurumdan yeni yönetmelik/tebliğ/düzenleyici Kurul kararı; sektör kanununda değişiklik
- Aleyhe düzenleyici işlem (İYUK m. 7/4 — dava süresi ilandan işler)
- Sektörümüzde soruşturma ya da idari para cezası; [Müvekkil] adının geçtiği her şey
- İzlenen kanun hakkında AYM iptal kararı

**Review-worthy (weekly digest):**
- Taslak düzenlemenin görüşe açılması (son tarih comment-tracker'a)
- Sektör dışı ama faaliyetimize ilişkin ceza; Rekabet taahhüt/uzlaşma kararları
- Kurum rehberi, kılavuzu; GİB sirküleri ve konumuza ilişkin özelgeler

**FYI (monthly roundup or not at all):**
- Konuşmalar, basın açıklamaları, akademik yorum
- Yeni bir yaklaşım içermeyen rutin bireysel kararlar
## Gap response process
**Who triages regulatory changes:** [...]
**Who owns policy updates:** [...]
**How gaps get tracked:** [...]
**Escalation for material gaps:** [...]
## Feed configuration
**Free feeds (always active):**
| Regulator | Source | URL/method |
|---|---|---|
| [kurum] | ArthurLegal tr_ / RSS / manual | [araç çağrısı, adres ya da "manual entry"] |

**Paid feeds (if configured):**
| Service | Subscription | Alerts |
|---|---|---|
| TR Regulatory Intelligence | [yes/no] | [alert names] |
| CourtListener | [yes/no] | [yalnız ABD] |

**Manual entry:** Enabled — herhangi bir gelişmeyi yapıştırın; karşılaştırma ve açık takibi başlar.
**Comment tracking:** [Enabled / Disabled]
**Default comment decision owner:** [ad/rol]
**Check cadence:** [daily / weekly]
**Digest channel:** [kişi/rol, Slack kanalı, e-posta listesi]
**Digest output path:** [klasör ya da "chat only"]
## Outputs
Üst başlık — avukat: "GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ"; avukat olmayan: "ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — AVUKATLA GÖZDEN GEÇİRİN". Başlık tek başına koruma yaratmaz; kuruma giden yazıda başlık konmaz.
## Matter workspaces
**Enabled:** [✓/✗] · **Active matter:** none · **Cross-matter context:** off
```

Kaynak etiketi: `[ArthurLegal TR — <citation> — GG.AA.YYYY]`; araç veri getiremezse "UYARI: veri çekilemedi, teyidiniz gerekli: <aracın source_url'si ya da kaynağın resmî giriş sayfası>".

## Yazdıktan sonra

1. **Özeti göster:** "İzleme listesi ve eşik bunlar. Ayarlanacak kısım eşik — çok sıkı olursa kaçırırsınız, çok gevşek olursa özeti okumayı bırakırsınız."
2. **Neler yapabildiğimi görmek ister misiniz?**
   - Akışları izleme listesine ve eşiğe göre süzüp özet çıkarma — `/arthurlegal:regulatory-legal-reg-feed-watcher`
   - Bir değişikliği politika kütüphanesiyle karşılaştırma — `/arthurlegal:regulatory-legal-policy-diff`
   - Açık açıklar, sahipleri ve son tarihleri — `/arthurlegal:regulatory-legal-gaps`
   - Taslak düzenleme görüş takvimi ve karar kaydı — `/arthurlegal:regulatory-legal-comments`
   **Önerim:** `/arthurlegal:regulatory-legal-reg-feed-watcher` ile son 30 günü deneme taraması — eşiğin doğru ayarlanıp ayarlanmadığını hemen gösterir. Kullanıcı görüşmede somut bir iş söylediyse listeyi atla. Politika kütüphanesini şimdi dizinlemeyi de öner.
3. **Kapanış:** "Profiliniz `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasında — düz metin. Doğrudan düzenleyebilir, `--redo` ile yeniden görüşebilir, `--check-integrations` ile bağlantıları yeniden deneyebilir, tek değişiklik için `/arthurlegal:regulatory-legal-customize` kullanabilirsiniz. En sık ayarlananlar: izleme listesi, önemlilik eşiği, tarama sıklığı. Profiliniz öğrenir: bir özet çok gürültülü ya da çok sessiz gelirse ayar genellikle buradadır; `reg-change-monitor` ajanı politika kütüphanenize dokunan bir değişiklik görünce açık kontrolü için işaretler."

## Hata kalıpları

- **Kurumu kanunla eşleştirmeden listeye alma.** Her satırın bir "neden"i olsun; dayanak maddeyi `tr_mevzuat_madde_getir` ile çek.
- **Ödeme kuruluşunu BDDK'ya, Sigorta Tahkim'i düzenleyiciye yazma; ArthurLegal'da olmayan kurum (KİK, Sayıştay, TÜRKPATENT, İSTAÇ) için araç önerme.**
- **`konu` ön elemesini kapsam garantisi sayma.** "Bu hafta başka bir şey çıkmadı" deme; elenen ve belirsiz sayısını yaz.
- **Kurul kararı numarasını ya da para cezası tutarını ezberden yazma.** Yalnız araçtan dönen `citation` alanı.

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
