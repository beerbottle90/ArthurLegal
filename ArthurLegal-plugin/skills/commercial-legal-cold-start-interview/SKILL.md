---
name: commercial-legal-cold-start-interview
description: >
  İlk kurulum — ticari sözleşme pratiğinizi öğrenir ve ekip profilini yazar: pratik
  ortamı (büro / şirket içi), taraf (satış / satın alma), Türk hukukuna göre standart
  duruşlar (sorumluluğun sınırlandırılması TBK m. 115, cezai şart TBK m. 179, 180, 182 ve
  TTK m. 22, veri koruma, süre ve fesih, uygulanacak hukuk ve yetki/tahkim), eskalasyon
  matrisi ve imza yetkisi, örnek sözleşmelerden fiilî duruşlar. İlk kullanımda,
  `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` yoksa ya da
  yer tutucu içeriyorsa, "eklentiyi kur", "beni tanı", "başlayalım" denince kullan.
  Yeni kurulumda çalışacak tek skill budur.
argument-hint: "[--redo | --full | --check-integrations | --side sales|purchasing]"
---

# /cold-start-interview

1. **Durum:** `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` yoksa görüşmeye başla. `<!-- SETUP PAUSED AT: -->` varsa o bölümden devam öner. `[PLACEHOLDER]` ya da `[Your Company Name]` varsa (duraklatma notu yok) baştan ya da yer tutucuların başladığı yerden devam öner. Doluysa ve `--redo` / `--side` yoksa sor: "Kurulum yapılmış görünüyor. Yeniden yapalım mı? Üzerine yazmadan önce farkı gösteririm."
2. **Taşıma:** eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/commercial-legal/*/CLAUDE.md`) dolu bir CLAUDE.md varsa ve ayar yolunda yoksa ayar yoluna kopyala; neyin taşındığını göster.
3. Görüşmeyi yürüt (önce Bölüm 0); örnek belgelerden fiilî duruşları çıkar (Bölüm 4); profili aşağıdaki iskelete göre yaz (üst klasörleri gerekirse oluştur), avukatın kendi sözleriyle.
4. Özeti göster: "Duyduklarım bunlar — profil yazıldı. Neyi yanlış anladım?" Deneme incelemesi öner; CLM bağlıysa yenileme kaydını toplu yüklemeyi öner.

**`--check-integrations`:** görüşme yapma; yalnız bağlantı kontrolünü çalıştır ve `## Available integrations` tablosunu yeniden yaz. ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse; denenmemiş bağlantı ⚪. `.mcp.json` beyanına bakarak ✓ verme.

**`--side sales` / `--side purchasing`:** yalnız Bölüm 2'yi o tarafa göre yürüt, `### Sales-side playbook` ya da `### Purchasing-side playbook` alt bölümüne yaz; Bölüm 0, 1 ve 3'ü sorma, diğer tarafa dokunma; `**Active side:**` satırını güncelle (`sales`, `purchasing`, `both`).

**Bölüm ve anahtar adlarını çevirme.** `## Who we are`, `## Who's using this`, `## Available integrations`, `## Playbook`, `**Active side:**`, `### Sales-side playbook`, `### Purchasing-side playbook`, `#### Limitation of liability` vb., `## Escalation`, `## House style`, `## Outputs`, `## Review preferences` (`confirm_routing`), `## NDA triage preferences` (`closing_action`), `## Playbook monitor settings` (`pattern_threshold`, `lookback_months`), `## Matter workspaces` adları aynen kalır — inceleme skill'leri ve ajanlar bunları birebir okur. İçerik Türkçe yazılır.

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/firm-profile.md` varsa oku ve tek satırla teyit et ("Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu?"); teyitte ortak soruları (pratik ortamı, ad, sektör, ne sattığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri) atla. Yoksa ilk kurulan eklenti budur: ortak soruları sor, paketteki `${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md` şablonuna göre yaz ve söyle: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak." Playbook, eskalasyon matrisi ve ev üslubu eklentiye özeldir.

**Kurulum kapsamı:** Çalışma klasörü ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden sözleşme okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

Kısa tut, önce hızlı/tam sor:

> **`commercial-legal`** ticari sözleşmeleri (tedarikçi/hizmet sözleşmeleri, SaaS abonelikleri, gizlilik sözleşmeleri, yenilemeler) inceleyen, müzakere eden ve yöneten ekipler içindir.
>
> **2 dakika:** rol, pratik ortamı, taraf (satış / satın alma) ve varsayılan duruşlar. **15 dakika:** gerçek playbook duruşlarınız (sorumluluk sınırı, tazmin, cezai şart, veri koruma, süre/fesih, uygulanacak hukuk ve yetki), vazgeçilmez tek şartınız, tutar eşikli eskalasyon matrisi ve imza yetkisi, ev üslubu, imzalı sözleşmelerden çıkarılan fiilî duruşlar.
>
> Hızlı mı, tam mı? (Sonra `/arthurlegal:commercial-legal-cold-start-interview --full` ile genişletebilirsiniz.)

**Hızlı yol:** yalnız Bölüm 0 ve taraf sorusu; diğer her alana `[DEFAULT]` yaz. Kapanış: "Tamam, komutları kullanabilirsiniz. Playbook duruşları, eskalasyon eşikleri ve ev üslubunda makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanacak bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--full`, tek bölüm için `--redo <bölüm>`."

**Seçimden sonra** tek paragraf oryantasyon: "Bu eklenti profilinizi (tarafınıza göre playbook, eskalasyon matrisi), fesih bildirimi son günlerini tutan yenileme kaydını, sapma günlüğünü ve playbook öneri kuyruğunu tutar. Cevaplarınızı her skill'in okuduğu düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve paylaştığınız belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** Şirket tanıtımı, playbook, eskalasyon matrisi, imza sirküleri, yetki devri belgesi için önce bağlantı/yapıştırma iste: "Belge yapıştırın, bağlantı verin ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli.
- **Uzun cevapta bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste — özellikle playbook duruşları, vazgeçilmez şart, örnek sözleşmeler]. Şimdi mi dolduralım, yer tutucu mu kalsın?" Sessiz boşluk bırakma.
- **Duraklat/devam:** "dur", "sonra devam" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /arthurlegal:commercial-legal-cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte: "Hoş geldiniz, [bölüm]de kalmıştınız. Devam mı, baştan mı?" Cevaplanmış soruyu tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre, eşik söylenirse `tr_mevzuat_madde_getir` ile çek ve karşılaştır; çelişirse: "[X] dediniz; madde metni [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnek: "Cezai şart fahişse mahkeme indirir" — tacir sıfatındaki borçlu aşırı ceza iddiasıyla indirim isteyemez (TTK m. 22); bu ayrım profile doğru girmeli. Değişen tutarları (damga vergisi oranı ve azami tutarı, faiz oranları, parasal sınırlar) profile sabit yazma; "güncel tutarı teyit et — dönemsel güncellenir" notu düş.

## Bölüm 0 — Kim kullanıyor, ne bağlı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her inceleme, değişiklik geçmişi ve yenileme çıktısındaki üst başlığı belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan** (stajyer avukat, sözleşme yöneticisi, hukuk operasyonu)
> 2. **Avukata erişimi olan, avukat olmayan** (kurucu, satın alma, satış operasyonu, finans)
> 3. **Düzenli avukat erişimi olmayan**

2 ya da 3 ise bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları 'imzalayın' hükmü değil, avukatla konuşmanız için araştırma olarak çerçevelerim; (2) hukuki sonucu olan adımlardan önce (imza, karşı tarafa redline gönderme, yenilemeyi kabul ya da fesih bildirimi) avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım." 3 ise ekle: "Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür, koşullarını baroya sorun."

### Pratik ortamı

> Hangisi size uyuyor? (Eskalasyon matrisinin dilini belirler.)
> - **Hukuk bürosu (müvekkil adına sözleşme hazırlama/inceleme)** — onay zinciri değil danışma tetikleri sorarım.
> - **Kurum içi hukuk** — eskalasyon matrisi, hukuk müşaviri/genel müdür, ne zaman iş birimine gider.
> - **Tek avukat / küçük büro** — üst kademe yerine "meslektaşa/dış avukata ne zaman danışırsınız".
> - **Kamu / klinik** — denetim modeli ve imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla yazın; kutuya zorlamam, doldurulan, uyarlanan ve boş bırakılan alanları işaretlerim.

Dallanma ve kayıt (`## Who we are` altında `**Practice setting:**` satırı):
- **Büro (her tür):** `## Matter workspaces` → `Enabled: ✓`, `Cross-matter context: off`. `## Escalation` tablosu onay seviyeleri değil danışma tetikleri gösterir. Profile `## Çıkar çatışması` notu yaz: aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat ve kendi düzenlediği sözleşmenin hükümsüzlüğünü ileri sürmek durumunda kalan avukat işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Her yeni matter'da kontrolün yapıldığını sor (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`).
- **Kurum içi:** `Enabled: ✗` (tek müvekkil; matter katmanı görünmez).
- **Kamu / klinik:** işi kim gözden geçirir, imza zinciri.

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantıyı karıştırma.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_mevzuat_madde_getir(number="6098", madde_no="115")`. Cevap geldiyse ✓.
- **Sözleşme emsali (`contracts_`)** — kloz kıyası için isteğe bağlı: `contracts_search_contracts`.
- **Yabancı ülke araçları** (`eu_`, `uk_`, `de_` …) — yalnız yabancı hukuka tabi sözleşme varsa; önce `status`.
- **CLM (Ironclad vb.), e-imza (DocuSign vb.), belge deposu (Drive, SharePoint, Box), Slack** — deneyebiliyorsan dene; deneyemiyorsan ⚪. KEP için MCP yoktur; KEP adresi varsa `## House style`'a not et.

Raporla: ✓ bağlı (denendi) · ⚪ yapılandırılmış, doğrulanmadı — MCP ayarlarından teyit edin · ✗ yok — [özellik] [manuel yönteme] düşer, nasıl bağlanır, sonra `--check-integrations`. "Hepsine gerek yok; çekirdek özellikler dosya erişimiyle çalışır." ArthurLegal MCP ✗ ise: "Her madde ve karar atfı 'doğrulanmadı' işaretlenir ve UYARI satırı taşır."

**Hemen yaz:** `## Who's using this` ve `## Available integrations` bölümlerini `## Who we are`'dan hemen sonra yaz; `## Outputs` üst başlığını role göre kur.

## Bölüm 1 — Ekip ve iş akışı (2-3 dk)

- **Ne iş yapıyorsunuz?** Ne satıyorsunuz, kime, nasıl (doğrudan, bayi/distribütör, pazaryeri, abonelik)? Web sitesi bağlantısı yeter. Büroysanız: müvekkil profiliniz ve en sık sözleşme tipleri.
- **Kim?** Şirket türü (AŞ, Ltd., şube, yabancı şirket), sözleşme ekibinin büyüklüğü, son sözü kim söylüyor (hukuk müşaviri, genel müdür, yönetici ortak)?
- **Ne geliyor?** Aylık hacim; karışım (tedarik, hizmet, SaaS, lisans, distribütörlük/acentelik, gizlilik); kendi metniniz mi karşı tarafın mı; hafif redline mı çok turlu müzakere mi; ortalama süre.
- **Ne acıtıyor?** Masaya gelince "of" dedirten ne; darboğaz inceleme mi, müzakere turu mu, onay kovalamak mı?

**Taraf sorusu** (doğrudan sor):

> Playbook duruşlarını hangi tarafa göre kurayım? (Her inceleme yalnız eşleşen tarafın playbook'unu uygular; satış duruşu satın alma sözleşmesine uygulanmaz.)
> - **Satış tarafı (sales-side)** — ürün/hizmet satıyoruz; genelde bizim metnimiz.
> - **Satın alma tarafı (purchasing-side)** — tedarikçiden alıyoruz; genelde onların metni.
> - **İkisi.**

- **Tek taraf:** `**Active side:** sales` ya da `purchasing`; Bölüm 2 cevapları eşleşen alt bölüme; diğerinde `*[Not configured — run /arthurlegal:commercial-legal-cold-start-interview --side <side> to build it]*` kalır.
- **İkisi:** önce satış tarafını kur (genelde kendi metniniz, yüzeyi küçük); sonunda `--side purchasing` öner. İkisi de dolunca `**Active side:** both`.

Soruları tarafın sesiyle sor: satışta "hangi tavanı **sunuyoruz**", satın almada "tedarikçiden hangi tavanı **kabul ediyoruz**". Karıştırma.

## Bölüm 2 — Playbook (3-4 dk)

> "Playbook'unuzu şimdi kuralım mı? İnceleme skill'leri genel varsayım yerine sizin duruş ve geri çekilme noktalarınızı bilir. 3-4 dakika. Geçerseniz varsayılan kullanılır ve kurulmamış bir duruşa gelindiğinde söylenir."

Önce sor: "Müzakere playbook'u, sözleşme standartları belgesi ya da geri çekilme notu var mı? Ekip/departman düzeyindeki ortak belge varsa onu isterim; kişisel farklarınızı ayrıca sorarım." Varsa oku, her kategori için duruşu çıkar, yalnız boşlukları sor; iki tarafı kapsıyorsa yazarken ikiye böl.

Yoksa her kategori için **standart duruş / kabul edilebilir geri çekilme / asla kabul edilmeyen** sor:

**Sorumluluğun sınırlandırılması** (`#### Limitation of liability`)
- Tavan: son 12 ay bedeli mi, sabit tutar mı (para birimi)? Dolaylı zarar ve kâr kaybı hariç mi?
- İstisnalar (tavan dışı): gizlilik ihlali, fikri mülkiyet ihlali, kişisel veri ihlali, kast ve ağır kusur.
- Hukuki sınır: borçlunun ağır kusurundan sorumlu olmayacağına ilişkin önceden yapılan anlaşma kesin hükümsüzdür; uzmanlık gerektiren ve izinle yürütülen hizmette hafif kusur için de öyledir (TBK m. 115/1, 115/3). Tavanın ağır kusur ve kastı da sınırlaması bu yüzden geçersizlik riski taşır; profile "tavan kast/ağır kusuru kapsamaz" notunu yaz.
- Karşı tarafın standart metninde (genel işlem koşulu) aleyhe kloz: açıkça bilgi verilip kabul edilmedikçe yazılmamış sayılır (TBK m. 21); dürüstlük kuralına aykırı aleyhe hüküm konulamaz (m. 25). "Her madde tartışıldı" kaydı tek başına GİK niteliğini kaldırmaz (m. 20/3).

**Tazmin (indemnity)** (`#### Indemnification`)
- Karşılıklı mı, tedarikçiden tek yönlü mü? Fikri mülkiyet ihlali tazmini zorunlu mu? Hiç kabul edilmeyen tazmin?
- Türk hukukunda "indemnity" kendi başına bir kurum değildir; üçüncü kişinin fiilini üstlenme (TBK m. 128) ya da sözleşmesel tazmin taahhüdü olarak yazılır — kapsam, bildirim ve savunmayı yönetme usulü açık olmalı.

**Cezai şart** (`#### Penalty clause`)
- Kabul ediliyor mu, hangi hâllerde, üst sınır? Seçimlik mi (borç ya da ceza), ifa ile birlikte mi (TBK m. 179)?
- Zarar olmasa da istenir; aşan zarar için kusur ispatı gerekir (m. 180). Hâkim aşırı cezayı kendiliğinden indirir (m. 182/3) — ama tacir sıfatındaki borçlu aşırılık iddiasıyla indirim isteyemez (TTK m. 22). Borçlu olduğumuz cezada (ör. satışta gecikme cezası, satın almada erken fesih cezası) yüksek tutarı kabul etmek bu yüzden "asla" ya da eskalasyon konusu olabilir.

**Veri koruma** (`#### Data protection`)
- Standart veri işleme sözleşmeniz var mı, karşı tarafınkini mi alırsınız? Veri sorumlusu, işleyenin alması gereken teknik ve idari tedbirlerden onunla müştereken sorumludur (KVKK m. 12/2) — işleyen sözleşmesi bu yüzden şart mı?
- Yurt dışı aktarım: yeterlilik kararı yoksa uygun güvence (standart sözleşme vb.) gerekir; standart sözleşme imzadan itibaren beş iş günü içinde Kurum'a bildirilir (KVKK m. 9/4-5). Bulut/SaaS tedarikçisinde kim bildirir?
- Güvenlik belgesi (ISO 27001, SOC 2) tüm tedarikçilerden mi, yalnız veri işleyenlerden mi? Alt işleyende onay mı, bildirim mi?

**Süre ve fesih** (`#### Term and termination`)
- Haklı sebeple ve olağan (sebepsiz) fesih: bildirim süresi? Otomatik yenilemede kabul edilen en uzun fesih bildirim penceresi? Fesih bedeli hiç kabul edilir mi?
- Fesih bildiriminin şekli: tacirler arasında fesih ve temerrüt ihbarları noter, taahhütlü mektup, telgraf ya da güvenli elektronik imzalı KEP ile yapılır (TTK m. 18/3). Sözleşme "e-posta yeterli" diyorsa duruşunuz ne?
- Tüketiciye satıyorsanız (B2C abonelik): belirli süreli abonelikte sözleşmenin kendiliğinden uzayacağına dair hüküm konulamaz (6502 s. TKHK m. 52/3) → satış tarafı playbook'una ayrı not.

**Uygulanacak hukuk ve uyuşmazlık çözümü** (`#### Governing law and venue` — `**Preferred:**`, `**Acceptable:**`, `**Escalate:**`, `**Never:**`)
- Sözleşmeden doğan borç ilişkileri tarafların açıkça seçtiği hukuka tabidir (MÖHUK m. 24/1); yabancılık unsuru olmayan saf iç sözleşmede yabancı hukuk seçimi **tartışmalı — içtihadı kontrol et**. Tercih / kabul / eskalasyon / asla listesi; yabancı hukuk ve yabancı yer tahkimi için ayrıntılı analiz `/arthurlegal:commercial-legal-governing-law-review`'dadır.
- Yetki sözleşmesi yalnız tacirler veya kamu tüzel kişileri arasında yapılabilir (HMK m. 17) ve yazılı olmalı, hukuki ilişki belirli ya da belirlenebilir, mahkeme gösterilmiş olmalıdır (m. 18/2). Tahkim sözleşmesi yazılıdır (HMK m. 412/3). Tercih: İstanbul mahkemeleri mi, kurumsal tahkim mi?
- Para alacağı, tazminat, itirazın iptali, menfi tespit ve istirdat konulu ticari davalarda dava öncesi arabuluculuk dava şartıdır (TTK m. 5/A) — kademeli uyuşmazlık klozu (müzakere → arabuluculuk → mahkeme/tahkim) istiyor musunuz?

**Damga vergisi** (`#### Stamp duty`) — kim öder, nüsha sayısı, imza yeri; oran ve azami tutar dönemsel güncellenir, profile sayı yazma (488 s. Damga Vergisi Kanunu — güncel tutarı teyit et).

**YZ/ML eğitim hakları** (`## AI/ML training rights` — yedi boyut, her biri ayrı yazılır; "her şeye hayır" geçerli ama yedi ayrı "hayır" olarak):
1. Açık eğitim izni — kesin hayır / dar tanımlıysa kabul / önemsiz?
2. Gizlilik politikasına atıfla örtülü izin — politika tek taraflı değişebiliyorsa red / kabul?
3. Anonimleştirme standardı — KVKK tanımı (başka verilerle eşleştirilerek dahi kişiyle ilişkilendirilemeyecek hâle getirme, m. 3/1-b) ya da adı konmuş bir standart şart mı; tanımsız "anonim" yeterli mi? AB verisi varsa: `eu_search_eu_law(query="Regulation (EU) 2016/679 recital 26 anonymous information")`.
4. Rakip kirlenmesi — tedarikçi rakiplerinize de hizmet veriyorsa yalıtım taahhüdü?
5. Opt-out kapsamı ve kalıcılığı — tüm YZ kullanımlarını kapsayan, yenileme ve şart güncellemesinden sonra da süren opt-out?
6. Çıktıların sahipliği — müşteride mi; tedarikçinin çıktıları eğitim örneği olarak tutması?
7. Düzenleyici zincir — AB YZ Tüzüğü (`eu_search_eu_law(query="Regulation (EU) 2024/1689 artificial intelligence")`) ve Türkiye'de yürürlükteki düzenleme (`tr_mevzuat_ara(query="yapay zeka", search_in="fulltext")`) bakımından tedarikçiden bildirim istenir mi?

**Vazgeçilmez tek şart** (`#### The one thing`): "Bir sözleşmede tek bir sorun olsa ve sırf o yüzden imzalamasanız, o ne?"

Playbook belgesi yüklenmediyse sonunda öner: "Bunu ekibinizle paylaşabileceğiniz ayrı bir playbook belgesi olarak da yazayım mı?"

## Bölüm 3 — Eskalasyon ve imza yetkisi (1-2 dk)

Önce sor: "Eskalasyon matrisi, onay eşikleri belgesi ya da yetki devri/iç yönerge var mı? Yapıştırın; temel alırım." Varsa doğrudan çıkar, belirsizi teyit et.

Yoksa:
- **Onay seviyeleri:** "İnceleme playbook dışı bir şey bulduğunda (daha yüksek tavan, geri çekilme dışı tazmin) ya da yetkinizi aşan bir karar gerektiğinde kime gider? İsim ya da rol, ya da 'kendim karar veririm'." (Bunu `/arthurlegal:commercial-legal-escalation-flagger` kullanır.)
- **Tutar eşikleri:** sözleşme bedeline göre kim onaylar (para birimiyle)?
- **Tutardan bağımsız otomatik eskalasyon:** tipik — sınırsız sorumluluk, fikri mülkiyetin karşı tarafa devri, tacir olarak yüksek cezai şart, yabancı hukuk + yabancı yer tahkimi, yurt dışına kişisel veri aktarımı, playbook'taki "asla" listesi.
- **İmza yetkisi:** Sözleşmeyi kim imzalar? AŞ'de esas sözleşmede aksi yoksa temsil yetkisi çift imza ile yönetim kuruluna aittir (TTK m. 370/1); temsile yetkililer ve temsil şekli ticaret siciline tescil ve ilan edilir (m. 373/1). İç onay matrisi şirketin iç düzenidir (yönetimin devri esas sözleşme hükmüyle ve iç yönergeyle yapılır, m. 367); iç sınırlamalar iyiniyetli üçüncü kişilere karşı hüküm ifade etmez — yalnız tescil ve ilan edilen merkez/şube ya da birlikte kullanma sınırlamaları geçerlidir (m. 371/3). Ltd.'de bu hükümler kıyasen uygulanır (m. 629/1). İmza sirkülerinin güncel olup olmadığını ve kimin tuttuğunu not et.
- **Kanal ve süre:** Bugün nasıl eskale ediliyor (Slack, e-posta, toplantı)? Beklenen dönüş süresi?
- **İnceleme tercihi:** İncelemeye başlarken yönlendirmeyi (hangi skill, hangi ek hangi skill'e) önce teyit edeyim mi? `confirm_routing` varsayılanı açık.
- **NDA kapanış eylemi:** NDA triyajı bitince ne yapılsın (ekip kutusuna e-posta, CLM iş akışı, sözleşme yöneticisine iletme)? Her NDA çıktısına standart talimat olarak eklerim.

Matris yüklenmediyse sonunda öner: "Bunu paylaşılabilir ayrı bir eskalasyon matrisi olarak da yazayım mı?"

## Bölüm 4 — Örnek belgeler

Önce altyapı sorusu: "İmzalı sözleşmeleriniz fiilen nerede duruyor — CLM, ortak Drive/SharePoint klasörü, fiziksel arşiv taraması? Haftalık deal-debrief ve renewal-watcher ajanları burayı tarar." CLM ise sistem adını ve "imzalandı" durumunun adını; klasörse tam yolu; dağınıksa "manuel yükleme" yaz.

> Önce: en sık kullandığınız sözleşme tipleri için kendi şablonlarınız (başlangıç duruşu). Sonra: 5-10 yakın tarihli imzalı sözleşme — 20 daha net desen verir; azsa olanı paylaşın.

Okuma sırası: (1) şablonlardan başlangıç duruşları; (2) imzalılardan fiilî şartlar; (3) fark — gerçek playbook budur; (4) sözleşme tipi ve karşı taraf büyüklüğüne göre desen (kurumsal karşı tarafta farklı geri çekilme vb.). 5'ten az imzalı sözleşmeyle kurulan her bölüme `[LIMITED DATA — N sözleşme incelendi]` yaz.

## Profili yazma

Yazmadan önce paylaşılan belgeleri yeniden oku; hafızaya güvenme. Profil avukatın okuyup düzenleyeceği bir belgedir, YAML değil. İskelet (başlıklar aynen, içerik Türkçe):

```markdown
# Commercial Contracts Practice Profile
*[TARİH] tarihinde kurulum görüşmesiyle yazıldı. Doğrudan düzenleyin — eklentideki her skill önce bunu okur.*
## Who we are
[Müvekkil] — [şirket türü]. **Practice setting:** [büro / kurum içi / tek avukat / kamu / diğer]
Ekip: [N kişi, roller]. Son karar: [isim/rol]. Aylık ~[N] sözleşme, ağırlıkla [tip]. CLM: [ad / yok].
**Acıtan şey:** [kendi sözleriyle]
## Who's using this
**Role:** [Avukat / Avukata erişimi olan avukat olmayan / Avukat erişimi olmayan]
**Attorney contact:** [isim / ekip / dış büro / —]
## Available integrations
| Integration | Status | Fallback if unavailable |
|---|---|---|
| ArthurLegal MCP (`tr_`) | [✓/⚪/✗] | Atıflar "doğrulanmadı" + UYARI satırı |
| CLM | [✓/⚪/✗] | Yerel yenileme kaydı ve manuel kayıt |
| E-imza | [✓/⚪/✗] | İmza eklenti dışında yürür |
| Belge deposu (Drive / SharePoint / Box) | [✓/⚪/✗] | Her incelemede dosya yüklenir |
| Slack | [✓/⚪/✗] | Uyarılar sohbette verilir |
## Playbook
**Active side:** [sales / purchasing / both]
> İnceleme skill'leri önce sözleşmede hangi tarafta olduğumuzu belirler (genelde kimin metni olduğundan anlaşılır; değilse sorar) ve yalnız eşleşen bölümü uygular.
### Sales-side playbook
#### Limitation of liability
**Standard position:** … **Acceptable fallbacks:** … **Never accept:** … **Carveouts we accept:** …
> *Örnek belgelerden:* [beyan ile imzalanan farkı — ör. "Standart 12 ay; incelenen 5 sözleşmenin 3'ü 24 ayda kapandı → 24 ay geri çekilme sayıldı."]
#### Indemnification
#### Penalty clause
#### Data protection
#### Term and termination
#### Governing law and venue
**Preferred:** … **Acceptable:** … **Escalate:** … **Never:** …
#### Stamp duty
#### The one thing
### Purchasing-side playbook
*[Not configured — run /arthurlegal:commercial-legal-cold-start-interview --side purchasing to build it]*
[Aynı alt bölümler; tedarikçiden kabul ettiklerimize göre]
## AI/ML training rights
[Yedi boyut, her biri ayrı duruş]
## Escalation
| Can approve | Without escalation | Escalate to | Via |
|---|---|---|---|
**Dollar thresholds:** [tutar ve para birimi]
**Automatic escalations regardless of dollar value:** [liste]
**Signing authority:** [kim imzalar, tek/çift imza, imza sirküleri tarihi, iç yönerge var mı]
## Çıkar çatışması
[Yalnız büroda — Av. K. m. 38 notu ve çatışma kontrolü pratiği]
## House style
**Tone in redlines:** … **Stakeholder summaries:** … **Where work product goes:** …
**Where signed contracts live:** [CLM + imzalı süzgeci / klasör yolu / manuel yükleme]
**Renewal alerts:** [kanal ya da e-posta listesi] · **KEP address:** [varsa]
## Outputs
- Rol avukatsa: `GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ`
- Rol avukat değilse: `ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — İŞLEM ÖNCESİ AVUKATLA GÖZDEN GEÇİRİN`
Karşı tarafa giden redline ve hukuk dışına iletilen özetlerden başlık çıkarılır. Başlık tek başına koruma yaratmaz.
## Seed documents reviewed
| Agreement | Counterparty | Date signed | Notable terms |
## Review preferences
confirm_routing: true
## NDA triage preferences
closing_action: "[her NDA triyajına eklenecek talimat]"
## Playbook monitor settings
pattern_threshold: 5
lookback_months: 12
## Matter workspaces
Enabled: [✓ / ✗]
Active matter: none — practice-level context only
Cross-matter context: off
```

## Yazdıktan sonra

> **Neler yapabildiğimi görmek ister misiniz?** Tedarikçi sözleşmesini playbook'a göre inceleme ve NDA triyajı (`/arthurlegal:commercial-legal-review`), fesih bildirimi son günleri (`/arthurlegal:commercial-legal-renewal-tracker`), bir klozun değişiklikler boyunca izi (`/arthurlegal:commercial-legal-amendment-history`), yetkiyi aşan sapmayı eskale etme (`/arthurlegal:commercial-legal-escalation-flagger`), bekleyen playbook önerileri (`/arthurlegal:commercial-legal-review-proposals`). **Önerim:** bekleyen bir NDA'yı triyaj edelim — playbook'un nasıl okunduğunu iki dakikada gösterir.

Kullanıcı somut bir iş söylediyse listeyi atla. Uygunsa ekle: "Yenilemeler gözden kaçıyor dediniz — CLM'de 90 gün içinde bitenleri tarayayım mı?" · "ArthurLegal MCP bağlı değil — bağlarsanız madde atıflarını canlı doğrularım."

**Kapanış:**
> "Tamam. Profiliniz `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` dosyasında — düz metin, doğrudan düzenleyebilirsiniz. Tam yeniden görüşme `--redo`, bağlantı kontrolü `--check-integrations`, tek değişiklik `/arthurlegal:commercial-legal-customize`. En sık ayarlananlar: **eskalasyon eşikleri ve onay matrisi**, **sorumluluk sınırı / tazmin / veri koruma duruşları** ve **vazgeçilmez tek şart**.
>
> **Profiliniz öğrenir.** Bir çıktı yanlış gelirse genellikle ayarlanacak bir duruştur; çıktı hangisi olduğunu söyler. playbook-monitor ajanı aynı sapmayı (varsayılan) 12 ayda 5 kez kabul ettiğinizi görürse playbook'u buna göre güncellemeyi önerir. On dakikalık kurulum çalışan bir profil verir; bir aylık kullanım sizin yazmış gibi okunan bir profil."

## Üslup ve kaçınılacaklar

Sıcak, meraklı, ödevini yapmış yeni bir meslektaş gibi; form gibi değil. Kısa cevapta bir kez takip sorusu sor ("12 ay — yalnız doğrudan zarar için mi, toplam sorumluluk için mi?"), sorgulamaya dönüştürme. Profil düzyazı ve tablodur (ayar satırları hariç YAML yok). Örnek belgeleri atlama — görüşme ekibin playbook'u ne sandığını, belgeler gerçekte ne olduğunu gösterir. "Piyasa şartları" gibi genel cevapta nazikçe sayı iste ("Tedarikçi 24 ay tavan derse karşı teklif mi, imza mı?"). Var olmayan skill vaat etme; profil doluysa her oturumda çalıştırma.

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
