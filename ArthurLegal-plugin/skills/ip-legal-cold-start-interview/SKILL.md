---
name: ip-legal-cold-start-interview
description: >
  İlk kurulum — fikri mülkiyet pratiğinizi öğrenir ve pratik profilini yazar:
  kim kullanıyor (avukat, marka/patent vekili, avukat olmayan), pratik ortamı
  (büro / şirket içi), pratik alanları (marka, patent, telif, ticari sır, açık
  kaynak, tasarım), tescil ve uygulama coğrafyası (TÜRKPATENT, EUIPO, WIPO
  Madrid, EPO), uygulama duruşu ve onay matrisi, eskalasyon, marka izleme.
  Profil yoksa ya da yer tutucu içeriyorsa, --redo ile yeniden görüşmede,
  --check-integrations ile yalnız bağlantı kontrolünde kullan. Yeni kurulumda
  çalışacak tek skill budur.
argument-hint: "[--redo | --full | --check-integrations]"
---

# /cold-start-interview

1. **Durum:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` yoksa görüşmeye başla. `<!-- SETUP PAUSED AT: -->` varsa o bölümden devam öner. `[PLACEHOLDER]` ya da `[Your Company Name]` varsa (duraklatma notu yok) baştan ya da yer tutucuların başladığı yerden devam öner. Doluysa ve `--redo` yoksa sor: "Kurulum yapılmış görünüyor. Yeniden yapalım mı? Üzerine yazmadan önce farkı gösteririm."
2. **Taşıma:** eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/ip-legal/*/CLAUDE.md`) dolu bir profil varsa ve ayar yolunda yoksa ayar yoluna kopyala; neyin taşındığını göster. Bölüm iskeleti `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonundadır.
3. Görüşmeyi yürüt (önce Bölüm 0); paylaşılan belgelerden fiilî duruşları çıkar (Bölüm 3); profili aşağıdaki iskelete göre yaz, avukatın kendi sözleriyle.
4. Portföy dökümü paylaşıldıysa `~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml` dosyasını tohumla; paylaşılmadıysa `/arthurlegal:ip-legal-portfolio`'nun sonra dolduracağı bir yer tutucu bırak.
5. Özeti göster: "Duyduklarım bunlar — profil yazıldı. Neyi yanlış anladım?" Deneme öner: "Bir marka adayını `/arthurlegal:ip-legal-clearance`'tan geçirelim mi, yoksa portföyde yaklaşan süreleri mi görelim?"

**`--check-integrations`:** görüşme yapma; yalnız bağlantı kontrolünü çalıştır, `## Available integrations` tablosunu yeniden yaz. ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse; denenmemiş bağlantı ⚪ ve tek satır nasıl teyit edilir. `.mcp.json` beyanına bakarak ✓ verme.

**Bölüm ve anahtar adlarını çevirme.** `## Company profile` (`**Practice setting:**`), `## Who's using this` (`**Role:**`), `## Available integrations`, `## IP practice profile` (`Practice area mix:`, `Registered in:`, `Outside counsel roster`, `Seed documents reviewed`), `## Enforcement posture` (`Default posture:`, `When we send a C&D`, `When we send a soft letter first`, `When we just file`, `Approval matrix`, `Automatic escalations`), `## Brand protection`, `## Decision posture on subjective legal calls`, `## Shared guardrails` (`Destination check`), `## Outputs`, `## Matter workspaces` (`Enabled`, `Active matter:`, `Cross-matter context`), `Renewal alerts` adları aynen kalır — diğer skill'ler ve `ip-renewal-watcher` ajanı bunları birebir okur. İçerik Türkçe yazılır.

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/firm-profile.md` varsa oku ve tek satırla teyit et ("Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu?"); teyitte ortak soruları (pratik ortamı, ad, sektör, ne sattığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri) atla. Yoksa ilk kurulan eklenti budur: ortak soruları sor, paketteki `${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md` şablonuna göre yaz ve söyle: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak." Uygulama duruşu, onay matrisi ve izleme ayarları bu eklentiye özeldir.

**Kurulum kapsamı:** çalışma klasörü ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden belge okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

> **`ip-legal`** marka, patent, telif, ticari sır ve açık kaynak yükümlülüklerini yönetenler içindir — marka araştırması, ihlale karşı adım (ihtarname, içerik kaldırma), portföy takibi ve sözleşmelerdeki fikri mülkiyet klozları.
>
> **2 dakika:** rol, pratik ortamı, yargı çevresi ve hangi alanlarda çalıştığınız; uygulama duruşu, onay eşikleri ve marka izleme için makul varsayılanlar. **15 dakika:** gerçek uygulama duruşunuz ve tetikleyicileri, her mektup türü için onay matrisi, izlenen markalar ve izleme hizmeti, açık kaynak politikası, dış avukat/vekil listesi ve portföy kaydı.
>
> Hızlı mı, tam mı? (Sonra `/arthurlegal:ip-legal-cold-start-interview --full` ile genişletebilirsiniz.)

**Hızlı yol:** yalnız Bölüm 0 ve Bölüm 1; diğer her alana `[DEFAULT]` yaz. Kapanış: "Tamam, komutları kullanabilirsiniz. Uygulama duruşu, onay eşikleri ve izlemede makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanacak bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--redo`."

**Seçimden sonra** tek paragraf oryantasyon: "Bu eklenti profilinizi (izlenen markalar, onay zinciri, ihtarname tetikleyicileri), yenileme süreli bir portföy kaydını ve matter bazında araştırma ve triyaj notlarını tutar. Cevaplarınızı her skill'in okuduğu düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve açıkça paylaştığınız belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** Portföy dökümü, uygulama rehberi, onay matrisi, marka kullanım rehberi, açık kaynak politikası için önce bağlantı/yapıştırma iste: "Belge yapıştırın, yol verin ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli; mümkünse seçmeli.
- **Uzun cevapta bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste — özellikle uygulama duruşu, onay matrisi, portföy]. Şimdi mi dolduralım, yer tutucu mu kalsın?" Sessiz boşluk bırakma.
- **Duraklat/devam:** "dur", "sonra devam" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /arthurlegal:ip-legal-cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte: "Hoş geldiniz, [bölüm]de kalmıştınız. Devam mı, baştan mı?" Cevaplanmışı tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre, eşik söylenirse `tr_mevzuat_madde_getir` ile çek ve karşılaştır; çelişirse: "[X] dediniz; madde metni [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnek: "Bülten itirazı için üç ayımız var" — marka başvurusunun yayımından itibaren itiraz süresi **iki aydır**, yazılı ve gerekçeli yapılır ve ücret aynı süre içinde ödenir (SMK m. 18). Tescil numarası söylenirse: TÜRKPATENT kayıtları ArthurLegal MCP'de yoktur; numarayı kullanıcının TÜRKPATENT dökümünden al, araçla "doğruladım" deme. Ücret ve harç tutarlarını sabit yazma — "güncel tutarı teyit et (dönemsel güncellenir)".

## Bölüm 0 — Kim kullanıyor, ne bağlı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her araştırma notu, ihtarname taslağı ve portföy notundaki üst başlığı belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan** (stajyer avukat, hukuk operasyonu, avukat gözetiminde fikri mülkiyet uzmanı)
> 2. **Marka ve/veya patent vekili (avukat değil)** — TÜRKPATENT sicilinde kayıtlı vekil
> 3. **Avukata erişimi olan, avukat olmayan** (kurucu, marka koruma yöneticisi, mühendislik lideri, açık kaynak sorumlusu)
> 4. **Düzenli avukat erişimi olmayan**

**2 ise** bir kez söyle: "Sicile kayıtlı vekiller TÜRKPATENT nezdinde işlem yapabilir (SMK m. 160/1). Kanun işlerinde ve hukuki meselelerde mütalaa vermek ve yargı organları önünde dava takibi ise baroda yazılı avukatlara aittir (Av.K. m. 35/1). Avukatın sır saklama yükümlülüğü (Av.K. m. 36) avukatlara ilişkindir; bu yüzden TÜRKPATENT işlemleri dışındaki çıktılarınızı (ihtarname, dava stratejisi, sözleşme görüşü) `GİZLİ — AVUKAT SIR SAKLAMA KAPSAMINDA DEĞİL` diye işaretler ve avukata götürülecek araştırma notu olarak çerçevelerim. Kendi meslek kurallarınızdaki gizlilik yükümlülüğünü ayrıca teyit edin."

**3 ya da 4 ise** bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları hüküm değil, avukat incelemesine götürülecek araştırma olarak çerçevelerim — 'ihtarnameyi gönderin' yerine 'taslak bu, iki yöndeki etkenler bunlar, göndermeden önce sorulacaklar bunlar'; (2) hukuki sonucu olan adımlardan önce (ihtarname, içerik kaldırma talebi, marka başvurusu, araştırma sonucuna dayalı karar) avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım." **4 ise** ekle: "Avukat bulmak için ilinizin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür. Tescil işlemleri için TÜRKPATENT'in yayımladığı marka/patent vekili sicili bir başlangıçtır."

### Pratik ortamı

> Hangisi size uyuyor? (Onay matrisinin dilini belirler.)
> - **Hukuk bürosu / fikri mülkiyet bürosu** — onay zinciri, ortak onayı, müvekkil yazılı talimatı.
> - **Şirket içi hukuk** — onay matrisi, hukuk müşaviri/genel müdür, ne zaman iş birimine ya da dış avukata gider.
> - **Tek avukat / küçük büro** — üst kademe yerine "meslektaşa/dış avukata ne zaman danışırsınız".
> - **Kamu / klinik** — denetim modeli ve imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla; kutuya zorlamam, doldurulan, uyarlanan ve boş bırakılan alanları işaretlerim.

Kayıt (`## Company profile` altında `**Practice setting:**`):
- **Büro (her tür):** `## Matter workspaces` → `Enabled: ✓`, `Cross-matter context: off`. Fikri mülkiyet matter'ları uzun ömürlüdür (tescil → yenilemeler). Profile `## Çıkar çatışması` notu yaz: aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat ve kendi düzenlediği senet ya da sözleşmenin hükümsüzlüğünü ileri sürmek durumunda kalan avukat işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Fikri mülkiyette sık doğan hâller: büronun tescil ettirdiği markaya karşı hükümsüzlük talebi, büronun hazırladığı lisans ya da devir sözleşmesine karşı geçersizlik iddiası, iki müvekkilin benzer marka başvurusu. Her yeni matter'da kontrolün yapıldığını sor (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`).
- **Şirket içi:** `Enabled: ✗` (tek müvekkil; matter katmanı görünmez).
- **Tek avukat / küçük büro:** onay tablosu iç onay seviyeleri değil danışma tetikleri gösterir.
- **Kamu / klinik:** işi kim gözden geçirir, ne zaman denetleyen avukata çıkar.

### Pratik alanları (sonraki her bölümü budar)

> **Hangi alanlarda çalışıyorsunuz? (Birden fazla seçin)**
> - **Patent / faydalı model** (başvuru takibi / dava / lisans)
> - **Marka** (araştırma / tescil / itiraz / ihlal / marka koruma)
> - **Telif** (lisans / içerik kaldırma / ihlal)
> - **Ticari sır** (koruma programı / ifşa / çalışan çıkışı)
> - **Açık kaynak** (uyum / lisans / politika)
> - **Tasarım** (tescil / taklit)

Her seçim için alt odağı yaz ("patent — başvuru ve lisans, dava yok"). Budama: Bölüm 2'de yalnız ilgili alt sorular; Bölüm 3'te yalnız ilgili belgeler; Bölüm 4 uygulama işi yoksa tümden atlanır (yalnız bir alanda varsa yalnız o alan için sorulur); Bölüm 5'te yalnız o alanların ürettiği bulgu türleri (araştırma çakışması yalnız marka, FTO yalnız patent, copyleft yalnız açık kaynak); Bölüm 6 marka yoksa atlanır. `## IP practice profile` → `Practice area mix:` satırına yaz; uygulanmayan alanlara açık "N/A" — yer tutucu değil. Doğru budanmış 3 dakikalık görüşme, yedi atlanmış yer tutuculu 15 dakikalık görüşmeden değerlidir.

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantıyı karıştırma.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_mevzuat_madde_getir(number="6769", madde_no="7")`. Cevap geldiyse ✓. SMK, FSEK, 5651 maddeleri ve Yargıtay içtihadı buradan doğrulanır.
- **TÜRKPATENT** — ArthurLegal MCP'de **yoktur** (resmî uç çalışmıyor); marka/patent arama, bülten ve sicil **elle** yapılır. Bunun için araç önerme; profile "TÜRKPATENT: manuel — turkpatent.gov.tr" yaz.
- **Yabancı kaynaklar** — AB (`eu_`), Birleşik Krallık (`uk_`), Almanya (`de_`) vb.; yalnız yurt dışı portföy ya da uyuşmazlık varsa; önce `status`.
- **Fikri mülkiyet yönetim sistemi** (Anaqua, CPA Global, Clarivate vb.), **belge deposu** (Drive, SharePoint, Box), **Slack** — deneyebiliyorsan dene, deneyemiyorsan ⚪. KEP için MCP yoktur; KEP adresi varsa `## Company profile`'a not et.

Raporla: ✓ bağlı (denendi) · ⚪ yapılandırılmış, doğrulanmadı — MCP ayarlarından teyit edin · ✗ yok — [özellik] [manuel yönteme] düşer; nasıl bağlanır (Cowork: Ayarlar → Bağlayıcılar; Claude Code: `/mcp`); sonra `--check-integrations`. Örnek: "Yönetim sistemi bağlı değil; portföy `portfolio.yaml`'da tutulur ve elle güncellenir; bağlarsanız renewal-watcher kaydı kendisi çeker." "Hepsine gerek yok; çekirdek özellikler dosya erişimiyle çalışır." ArthurLegal MCP ✗ ise: "Her madde ve karar atfı 'doğrulanmadı' işaretlenir ve UYARI satırı taşır."

**Hemen yaz:** `## Who's using this` ve `## Available integrations` bölümlerini `## Company profile`'dan hemen sonra yaz; `## Outputs` üst başlığını role göre kur.

## Bölüm 1 — İş ve hacim (1-2 dk)

- **Ne iş yapıyorsunuz?** Ne satıyorsunuz, kime, nasıl (doğrudan, bayi, pazaryeri, abonelik)? Web sitesi bağlantısı yeter. Büroysanız: fikri mülkiyet işini en çok yaptığınız müvekkil tipleri.
- **Hacim:** tipik bir ayda masanıza ne kadar iş geliyor (araştırma talebi, ihlal dosyası, portföy işlemi, kloz incelemesi)? Bağlam olarak yaz; kapı değildir — yalnız `ip-renewal-watcher` sıklığını etkiler.

## Bölüm 2 — Tescil ve uygulama coğrafyası (1-2 dk)

> Nerede tescilliyiz, nerede hak arıyoruz? (Araştırma, FTO ve portföy her yargı çevresini buradan okur.)
> - **Markalar:** TÜRKPATENT? EUIPO? WIPO Madrid (hangi ülkeler)? Diğer ulusal tesciller? Yalnız kullanım (tescilsiz)?
> - **Patentler:** TÜRKPATENT? EPO (hangi ülkelerde geçerli kılındı)? PCT ulusal aşama ülkeleri?
> - **Uygulama:** Türkiye'de mi, yurt dışında mı? İzleme hizmetiyle mi, yalnız önünüze gelince mi?

Yalnız seçilen alanların alt sorusunu sor. `## IP practice profile` → `Registered in:` ve `## Enforcement posture` altında uygulama coğrafyası.

**Dış vekil ve avukatlar:** "TÜRKPATENT işlemlerini kim yürütüyor — kendi kayıtlı vekiliniz mi, dış marka/patent vekili mi? Yurt dışı tesciller için yabancı muhabir? Dava için dış avukat?" → `Outside counsel roster` (ad, alan, ülke; yurt dışında yerleşik başvuru sahipleri TÜRKPATENT'te ancak vekille temsil edilir, SMK m. 160/3).

## Bölüm 3 — Pratik belgeleri (1-2 dk)

Duruş sorularından önce elde olanı çıkar:

> Şunlardan elinizde olanı yapıştırın, yol ya da bağlantı verin — yeniden yazdırmam:
> - **Portföy dökümü** (yönetim sistemi ya da tablo: marka/patent/tasarım, ülke, durum, yenileme tarihleri)
> - **Marka kullanım rehberi** (üçüncü kişiler için kurallar, marka kitabı)
> - **İhtarname şablonu**
> - **Uygulama rehberi** (ne zaman ihtarname, ne zaman dava, ne zaman bırak)
> - **Açık kaynak politikası**
> - **Standart sözleşmelerdeki fikri mülkiyet klozları** (lisans alma/verme, devir şablonu)

Her belgeyi oku, duruşları çıkar (onay eşikleri, tetikleyiciler, açık kaynak kabul/yasak listesi, kloz varsayılanları), Bölüm 4-5'te cevaplanmış soruyu tekrar sorma, belirsizi teyit et. `## IP practice profile` → `Seed documents reviewed` altına listele.

## Bölüm 4 — Uygulama duruşu (2-3 dk)

> Bir ihlal gördüğünüzde — taklit marka, kopyalanmış görsel, fazla benzer ürün — nerede durursunuz? (`/arthurlegal:ip-legal-infringement-triage` ve `/arthurlegal:ip-legal-cease-desist` her sonucu bu duruştan geçirir.)
> - **Aggressive** — erken ihtarname, dava açmaya hazır.
> - **Measured** — önce yumuşak mektup ya da temas; cevap yoksa ya da ticari etki gerçekse yükselt.
> - **Conservative** — yalnız dava muhtemel ve iş birimi uyuşmazlığa onay verdiyse hak ileri sür.

Sonra: **Ne zaman ihtarname?** (karıştırılma ihtimali + ticari zarar mı, tescilli markanın her kullanımı mı, platform bildirimi işe yaramayınca mı — kendi sözlerinizle) · **Ne zaman önce yumuşak mektup?** (bireyler, küçük ticari kullanıcılar, sempatik karşı taraflar?) · **Ne zaman doğrudan dava/tedbir?** (tekrarlayan ihlal, savaşmaya hazır karşı taraf, süre işliyor — ör. ceza şikâyetinde altı ay)

**Kim onaylar?** (`/arthurlegal:ip-legal-cease-desist` ve `/arthurlegal:ip-legal-takedown` taslağı adı geçen onaylayana götürür ve onay gelmeden hiçbir yere gitmez.)
> - **İçerik kaldırma (olağan)** — platform bildirimi, FSEK ek m. 4 başvurusu: kimde? (`DMCA takedown (ordinary)` satırı — ad çevrilmez)
> - **Yumuşak mektup** (`Soft letter`)
> - **İhtarname** (`Cease-and-desist`)
> - **Dava açma / ihtiyati tedbir** (`Filing suit`) — hukuk müşaviri mi, genel müdür mü, iş sponsoru mu; büroda yönetici ortak + müvekkilin yazılı talimatı mı?

> Hangi durum, varsayılan onaylayandan bağımsız **otomatik eskalasyon**? (Tipik: karşı taraf mevcut müşteri ya da ortak; karşı taraf bizden büyük; patent içeriyor; basına yansıyabilir; savcılık başvurusu ya da ceza şikâyeti.)

Son vurgu: "**İhtarname bir uyuşmazlık başlatır.** Bu yüzden bu eklentideki en önemli ayar budur. Her mektup türü için onaylayanı teyit edin."

## Bölüm 5 — Eskalasyon (1-2 dk)

> Araştırma gerçek bir çakışma bulduğunda, FTO engelleyici bir patent çıkardığında ya da açık kaynak incelemesi copyleft yükümlülüğü bulduğunda — notu kim alır, ne yapılacağına kim karar verir?
> - **Marka çakışması:** başvuru mu, ad değişikliği mi, muvafakat/birlikte var olma anlaşması mı?
> - **FTO engeli:** mühendislik mi, ürün mü, hukuk müşaviri mi?
> - **Copyleft:** bağımlılığı çıkarma, ürünü açma ya da mimariyi değiştirme kararı kimde?

Bugün nasıl eskale ediliyor (Slack, e-posta, bilet, toplantı), beklenen dönüş süresi? `## Enforcement posture` altına eskalasyon yönlendirmesi olarak yaz.

## Bölüm 6 — Marka koruma (yalnız marka seçildiyse)

> - **İzlenen markalar:** belirli markaları üçüncü kişi kullanımına karşı aktif izliyor musunuz? Liste ya da "yok — yalnız önümüze gelince".
> - **İzleme kaynakları:** TÜRKPATENT Resmî Marka Bülteni (elle ya da vekil üzerinden), izleme hizmeti (Corsearch, CompuMark vb.), EUIPO, pazaryeri ve alan adı taraması?
> - **Sıklık:** haftalık / aylık / üç aylık / talep üzerine? Bülten izlemesinde yayıma itiraz süresi yayımdan itibaren **iki aydır** (SMK m. 18/1) — aylıktan seyrek sıklık itiraz penceresini kaçırabilir; profile not düş.

`## Brand protection` altına yaz. Portföy uyarılarının gideceği kanal → `Renewal alerts`.

## Profili yazma

Yazmadan önce paylaşılan belgeleri yeniden oku; hafızaya güvenme. Profil avukatın okuyup düzenleyeceği bir belgedir, YAML değil (portföy kaydı YAML'dır; profil değil). Rol ve pratik ortamına göre tek varyant yaz; karıştırma. İskelet (başlıklar aynen, içerik Türkçe):

```markdown
# IP Practice Profile
*[TARİH] tarihinde kurulum görüşmesiyle yazıldı. Doğrudan düzenleyin — eklentideki her skill önce bunu okur.*
## Company profile
[Müvekkil] — [şirket türü / büro]. **Practice setting:** [büro / şirket içi / tek avukat / kamu / diğer]
[ne iş yapıyor; aylık hacim]
## Who's using this
**Role:** [Avukat / Marka-patent vekili (avukat değil) / Avukata erişimi olan avukat olmayan / Avukat erişimi olmayan]
**Attorney contact:** [isim / ekip / dış büro / —]
## Available integrations
| Integration | Status | Fallback if unavailable |
|---|---|---|
| ArthurLegal MCP (`tr_`) | [✓/⚪/✗] | Atıflar "doğrulanmadı" + UYARI satırı |
| TÜRKPATENT | manuel | turkpatent.gov.tr — elle arama, kaynak ve tarih damgası |
| IP yönetim sistemi | [✓/⚪/✗] | `portfolio.yaml` elle |
| Belge deposu | [✓/⚪/✗] | Her işte dosya yüklenir |
| Slack | [✓/⚪/✗] | Uyarılar sohbette |
## IP practice profile
**Practice area mix:** [alan — alt odak; uygulanmayanlara N/A]
**Registered in:** [TÜRKPATENT / EUIPO / WIPO Madrid: ülkeler / EPO / diğer]
**Outside counsel roster:** [ad — alan — ülke — rol (marka vekili / patent vekili / dava avukatı / yabancı muhabir)]
**OSS policy:** [yol / yok]
**Seed documents reviewed:** [liste]
## Enforcement posture
**Default posture:** [Aggressive / Measured / Conservative]
**When we send a C&D:** … **When we send a soft letter first:** … **When we just file:** …
**Enforcement geography:** [Türkiye / yurt dışı; izleme ya da reaktif]
**Approval matrix**
| Action | Approver | Notes |
|---|---|---|
| DMCA takedown (ordinary) | [ ] | Türkiye'de: FSEK ek m. 4 başvurusu, platform bildirimi; yabancı DMCA bildirimi |
| Soft letter | [ ] | |
| Cease-and-desist | [ ] | |
| Filing suit | [ ] | dava, ihtiyati tedbir, savcılık başvurusu |
**Automatic escalations:** [liste]
**Escalation routing:** [marka çakışması → …; FTO engeli → …; copyleft → …; kanal ve dönüş süresi]
## Brand protection
**Watched marks:** … **Watch jurisdictions:** … **Watch service:** … **Monitoring cadence:** …
**Renewal alerts:** [kanal / e-posta listesi]
## Çıkar çatışması
[Yalnız büroda — Av. K. m. 38 notu ve kontrol pratiği]
## Decision posture on subjective legal calls
Belirsiz öznel hukuki değerlendirmede (karıştırılma ihtimali, eser benzerliği, kanuni istisna, copyleft tetikleyicisi, iddianın savunulabilirliği) sessizce "sorun yok" denmez; avukata işaretlenir, iki yöndeki etkenler gösterilir.
## Shared guardrails
**Destination check:** Çıktı dar hukuk çevresi dışına (karşı taraf, geniş kanal, basın, sigortacı) gidecekse dur; tam sürüm yalnız hukuka, arındırılmış sürüm geniş kanala. Avukatın sır saklama yükümlülüğü (Av.K. m. 36) belgeyi koruyan genel bir kalkan değildir.
## Outputs
- Rol avukatsa: `GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ`
- Rol marka/patent vekiliyse: TÜRKPATENT işlemleri için `GİZLİ — DAHİLİ`; diğer işler için `GİZLİ — AVUKAT SIR SAKLAMA KAPSAMINDA DEĞİL — AVUKATA GÖTÜRÜN`
- Rol avukat değilse: `ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — İŞLEM ÖNCESİ AVUKATLA GÖZDEN GEÇİRİN`
Karşı tarafa giden ihtarname, kaldırma talebi ve itirazdan başlık çıkarılır. Başlık tek başına koruma yaratmaz.
**Next-steps decision tree:** taslağı yaz / eskale et / olgu topla / bekle-izle / başka bir şey.
**Dashboard offer for data-heavy outputs:** ~10 kalemi aşan portföy ve OSS çıktılarında pano öner.
## Matter workspaces
Enabled: [✓ / ✗]
Active matter: none — practice-level context only
Cross-matter context: off
```

Portföy dökümü varsa `portfolio.yaml`'ı tohumla (her kayıt: tür, ad/başlık, ülke, tescil/başvuru no, durum, sonraki işlem tarihi — kaynak: kullanıcının dökümü; TÜRKPATENT'ten araçla çekilmedi).

## Yazdıktan sonra

> **Neler yapabildiğimi görmek ister misiniz?** Marka adayı araştırması (`/arthurlegal:ip-legal-clearance`), ihlal triyajı — platform bildirimi mi, ihtarname mi, izleme mi (`/arthurlegal:ip-legal-infringement-triage`), FTO ön değerlendirmesi (`/arthurlegal:ip-legal-fto-triage`), ihtarname ya da içerik kaldırma taslağı (`/arthurlegal:ip-legal-cease-desist`, `/arthurlegal:ip-legal-takedown`), açık kaynak uyumu (`/arthurlegal:ip-legal-oss-review`), sözleşmedeki fikri mülkiyet klozları (`/arthurlegal:ip-legal-ip-clause-review`), portföy yenileme durumu (`/arthurlegal:ip-legal-portfolio`). **Önerim:** `/arthurlegal:ip-legal-portfolio` — eklentideki kaydın gerçek portföyle örtüşüp örtüşmediğini en hızlı gösterir.

Kullanıcı somut bir iş söylediyse listeyi atla. Acıya göre öner: uygulama yavaşsa ihtarname taslağı; yenilemeler gözden kaçıyorsa önümüzdeki 90 gün; açık kaynak dağınıksa bir depo taraması. ArthurLegal MCP bağlı değilse: "Bağlarsanız madde atıflarını canlı doğrularım; bağlanmadıkça her atıf doğrulanmadı işareti taşır."

**Kapanış:**
> "Tamam. Profiliniz `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` dosyasında — düz metin, doğrudan düzenleyebilirsiniz. Tam yeniden görüşme `--redo`, bağlantı kontrolü `--check-integrations`, tek değişiklik `/arthurlegal:ip-legal-customize`. En sık ayarlananlar: **uygulama duruşu** (gerçek tetikleyicinin yazılandan farklı olduğu çıkar), **tescil coğrafyası** (yeni başvuru, düşen tescil) ve **izlenen markalar**.
>
> **Profiliniz öğrenir.** Bir çıktı yanlış gelirse genellikle ayarlanacak bir duruştur; çıktı hangisi olduğunu söyler. `ip-renewal-watcher` ajanı portföy kaydını sıklığınıza göre izler; kaçan bir uyarı, kapatılacak bir kayıt boşluğudur. On dakikalık kurulum çalışan bir profil verir; bir aylık kullanım sizin yazmış gibi okunan bir profil."

## Üslup ve kaçınılacaklar

Sıcak, meraklı, ödevini yapmış yeni bir meslektaş gibi; form gibi değil. "Lütfen sağlayın" değil "durum ne"; "ayarlarınızı yapılandırın" değil "pratiğiniz nasıl işliyor". Kısa cevapta bir kez takip sorusu sor ("Aggressive — ilk görüşte ihtarname mi, kısa bir temastan sonra mı?"), sorgulamaya dönüştürme. Genel cevapta tetikleyiciyi iste: "Instagram'da ilgisiz mallarda neredeyse aynı markayı kullanan bir hesap gördünüz — ne yaparsınız?" Profile YAML yazma; belgeleri atlama (görüşme ne sanıldığını, belgeler gerçeği gösterir); var olmayan skill vaat etme; profil doluysa her oturumda çalıştırma. **Patent istemi yazma ve resmî görüş (mütalaa) verme** bu eklentinin dışındadır — istenirse patent vekiline ya da avukata yönlendir.
