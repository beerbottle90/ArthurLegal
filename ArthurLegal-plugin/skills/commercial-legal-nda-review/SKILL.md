---
name: commercial-legal-nda-review
description: >
  Referans: gelen gizlilik sözleşmelerini (NDA) YEŞİL / SARI / KIRMIZI olarak
  hızla ayırır; avukat zamanı yalnız gereken sözleşmeye harcanır. Satış ve iş
  geliştirme ekiplerinin hukuka gelmeden önce kendi başına kullanabilmesi
  için tasarlandı. Türk hukuku tabanı: haksız rekabet ve sır (TTK m. 55),
  cezai şart (TBK m. 179-182, TTK m. 22), yetki ve tahkim (HMK m. 17-18, 412).
  NDA tespit edildiğinde /arthurlegal:commercial-legal-review tarafından yüklenir.
user-invocable: false
---

# /nda-review — Gizlilik Sözleşmesi Triajı

Gelen NDA'ların çoğu sorunsuzdur; birkaçında mayın vardır. Bu skill onları bir dakikada ayırır. **Hedef:** YEŞİL bir NDA'ya imzadan başka bir şey gerekmez; SARI bir NDA'da avukatın bir iki belirli noktaya bakması gerekir; KIRMIZI bir NDA kimse vakit kaybetmeden durdurulur. (Profil ve diğer skill'ler GREEN / YELLOW / RED etiketlerini de kullanabilir; anlamları aynıdır.)

## Destination check

Çıktının nereye gideceğine bak. Kullanıcı bir hedef söylediyse (kanal, dağıtım listesi, karşı taraf, "herkes") bunun dar gizlilik çevresinde olup olmadığını sor. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD'deki "privilege" gibi geniş bir belge koruması değildir; şirket geneli kanala, karşı tarafa ya da tedarikçiye giden metin gizliliğini fiilen kaybeder. Hedef çevre dışındaysa (a) yalnız hukuk için tam sürüm, (b) geniş kanal için arındırılmış sürüm ya da (c) ikisini öner; üst başlığı koyup başlığın korumayacağı yere yapıştırılmasına yardım etme. Kanonik kural: eklenti ayarında `## Shared guardrails → Destination check`.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:commercial-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Önce playbook

**Hangi taraftayız?** Karşı taraf ürününüzü değerlendiriyorsa satış tarafı; siz onunkini değerlendiriyorsanız alım tarafı. Karşılıklı NDA'nın da tarafı vardır: kâğıt kimin, değerlendirme hangi yönde? Belli değilse sor. Eşleşen bölümü oku (`### Sales-side playbook` ya da `### Purchasing-side playbook`) ve çıktıda hangisini uyguladığını yaz. Eşleşen taraf `[Not configured]` ise dur: "`/arthurlegal:commercial-legal-cold-start-interview --side <side>` çalıştırılmadan bu triaj yapılamaz."

**Triajdan önce** `## Playbook` → eşleşen taraf → `NDA triage positions` bölümünü oku. YEŞİL/SARI/KIRMIZI ölçütleri oradan gelir; bu skill NDA şartları için varsayılan pozisyon taşımaz. Bölüm yoksa ya da NDA'daki bir şart hakkında sessizse sor:

> Playbook'unuz [şart — ör. "residuals kaydı", "gizliliğin sözleşme sonrası süresi", "alıcı olduğunuz tek taraflı NDA", "cezai şart tutarı"] hakkında bir şey söylemiyor. Varsayılan pozisyonunuz ne — ne zaman YEŞİL, ne zaman SARI, ne zaman KIRMIZI? Eklenti ayarına ekleyeyim ki sonraki inceleme tutarlı olsun.

Cevabı eklenti ayarına yaz ve yeni pozisyonla devam et.

## Kapsam kontrolü

NDA'ya özgü hükümlere geçmeden önce belgenin adından fazlasını yapıp yapmadığına bak. "Karşılıklı ticari NDA" şunları saklayabilir: standstill, lisans verilmesi, münhasırlık, çalışan/müşteri ayartmama, rekabet yasağı, fikrî hak devri, önalım hakkı, en çok kayrılan müşteri kaydı, gizlilik dışındaki uyuşmazlıkları da kapsayan geniş tahkim/yetki kaydı, yüksek tutarlı cezai şart, kişisel veri işleme talimatları.

Gizlilik dışında yükümlülük varsa: **NDA analizinden bağımsız olarak otomatik SARI.**

> Bu belge NDA olarak adlandırılmış ama [standstill / lisans / ayartmama / münhasırlık / fikrî hak devri / önalım / en çok kayrılan / geniş tahkim] içeriyor. NDA'dan fazlası. Avukat incelemesine yönlendirin.

NDA kılığındaki hizmet sözleşmesi, ön protokol ya da taahhüt paketini sessizce NDA triajından geçirme.

## Türk hukuku tabanı (kısa)

NDA olmasa da bilgi tamamen korumasız değildir; NDA bu tabanın **üstüne** sözleşmesel yükümlülük ve yaptırım ekler:
- Kendisine emanet edilmiş teklif, hesap, plan gibi iş ürününden yetkisiz yararlanma (TTK m. 55/1-c) ve üretim ve iş sırlarını hukuka aykırı ifşa (TTK m. 55/1-d) haksız rekabettir; tespit, men, eski hâle getirme ve tazminat davaları TTK m. 56'dadır.
- Ticari sır, bankacılık sırrı ya da müşteri sırrını yetkisiz kişilere veren kişi şikâyet üzerine cezalandırılır (TCK m. 239). Kanunda genel bir "ticari sır" tanımı yoktur; NDA'daki tanım uygulamada belirleyicidir.
- Alıcı tarafın işçileri, hizmet ilişkisi süresince ve işverenin haklı menfaati gerektirdiği ölçüde sonrasında da sır saklamakla yükümlüdür (TBK m. 396/4). Bu yükümlülük işverene karşıdır; NDA'yı açıklayan tarafın işçiye doğrudan başvuru hakkı doğurmaz → NDA'da "çalışan ve yardımcılarını aynı yükümlülükle bağlama ve onların ihlalinden sorumluluk" kaydı aranır (yardımcı kişi sorumluluğu: TBK m. 116).
- NDA kanunda şekle bağlı değildir (TBK m. 12/1); ispat için yazılı ve imzalı nüsha tut.

## Triaj

Kova tanımları sabittir; her kovayı dolduran ölçütler playbook'tandır. Her çıktının başına eklenti ayarı `## Outputs` → üst başlığı koy (role göre değişir — `## Who's using this`).

### YEŞİL — imzaya yönlendir

NDA playbook'taki her pozisyonu karşılıyor ve hiçbir şart KIRMIZI tetikleyicisine düşmüyor. Playbook'un genelde kapsadığı kontroller: karşılıklılık, süre, sözleşme sonrası gizlilik süresi, istisnalar, cezai şart, uygulanacak hukuk ve yetki, kısıtlayıcı taahhütler, ücret yükleme. Hepsini eklenti ayarına karşı teyit et.

**YEŞİL, avukatın gözden geçirdiği pozisyon ister.** YEŞİL, avukat incelemesi olmadan imzaya giden tek yoldur; varsayılan ya da eksik pozisyonla verilemez. Profilde avukatın gözden geçirdiği `NDA triage positions` yoksa:

> Profilinizde avukatın gözden geçirdiği NDA pozisyonları olmadan YEŞİL veremem. Ticari avukatınızla `/arthurlegal:commercial-legal-cold-start-interview --full` çalıştırın ya da bu NDA'yı avukat incelemesine gönderin. Varsayılana göre YEŞİL vermek, sonraki hukukçu olmayanın güveneceği pozisyonu bir hukukçu olmayanın koyması demektir.

Pozisyon eksikse doğru karar SARI'dır.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

## NDA Triajı: [Karşı taraf] — [Satış / Alım tarafı playbook'u]

YEŞİL — imzaya yönlendir

### Özet
Playbook'a göre kırmızı bayrak yok. Standart süreçle imzaya yönlendirin.

| Kontrol | Durum | Playbook bölümü |
|---|---|---|
| [her kontrol] | geçti | [eklenti ayarı bölümü] |

**Sonraki adım:** [[CLM] standart NDA akışına gönder | [eklenti ayarındaki onaylayıcı]'ya imzaya gönder]
```

### SARI — avukat belirli noktalara baksın

Bir ya da birkaç şart playbook'tan sapıyor ama kesin ret değil, YA DA playbook'un hiç değinmediği bir şart var. Her noktayı ayrı ayrı göster ki onaylayıcı karar verebilsin.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

## NDA Triajı: [Karşı taraf] — [taraf]

SARI — [eklenti ayarındaki onaylayıcı]'ya işaretle

### Özet
- [Tek satırlık mekanik düzeltme, ör. "Madde 6'daki ayartmama kaydını sil"]

### İşaretlenen noktalar
**1. [Konu]** — Madde [X]
   Ne: [tek satır]
   Neden: [hangi playbook pozisyonu ya da "playbook sessiz"]
   **Hukuki risk:** [🔴/🟠/🟡/🟢] | **İş sürtünmesi:** [🔴 Anlaşmayı durdurur / 🟠 Yavaşlatır / 🟡 Kafa karıştırır / 🟢 Görünmez]
   Muhtemel çözüm: [kabul / X'e itiraz / bağlama göre]

### Geri kalanı
| Kontrol | Durum | Playbook bölümü |
|---|---|---|

**Sonraki adım:** İşaretli noktaları [onaylayıcı]'ya sorun; uygun görürse imzaya yönlendirin.
```

### KIRMIZI — dur, önce hukuka danış

Şart playbook'un "asla kabul etme" listesinde ya da yapı ekibin standart duruşuyla bağdaşmıyor (ör. playbook karşılıklı isterken tek taraflı NDA; süreli gizlilik isterken süresiz; "never" listesindeki hukuk ya da yargı yeri).

```markdown
[ÜST BAŞLIK — profil ## Outputs]

## NDA Triajı: [Karşı taraf] — [taraf]

KIRMIZI — göndermeyin, önce hukuka danışın

### Özet
- [ör. "Madde 4 — hukuk incelemesine yönlendirin"]

### Kritik sorunlar
**1. [Konu]** — Madde [X]
   > "[birebir alıntı]"
   Neden sorun: [somut risk; ihlal edilen playbook pozisyonu]
   **Hukuki risk:** [...] | **İş sürtünmesi:** [...]
   Önerilen cevap: [bizim metni kullanalım | şu ifadeyle itiraz | vazgeç]

**Sonraki adım:** Bu triajı [GC ya da eklenti ayarındaki eskalasyon kişisi]'ne gönderin. [CLM]'e ya da onay akışına sokmayın. Karşı tarafa imzalayacağımızı söylemeyin.
```

## Kontrol rehberi

Her kontrolün kovası playbook'tan gelir; bu liste yalnız **neye bakılacağını** ve Türk hukukunun koyduğu sınırları söyler.

**Karşılıklılık.** Tek taraflıysa hemen KIRMIZI deme; sor: (1) Bu ilişkide bilgi veren yalnız siz misiniz? (2) Sınırlı, belirli bir açıklama mı (ör. teknolojinizi üzerinde çalışacak tedarikçiye vermek)? (3) Şirket alımı, işçi ya da yatırımla mı ilgili? (Evetse dur — bu skill yalnız ticari NDA içindir; hukuka yönlendir.) Playbook bu olguya pozisyon almıyorsa SARI ve cevapları onaylayıcıya göster.

**Gizli bilgi tanımı.** Yalnız işaretli mi, açıklanan her şey mi; işaretleme şartı; sözlü açıklamanın yazılı teyit süresi. Tanım dar ve işaretlemeye bağlıysa korunmak istenen bilgi TTK m. 55 tabanına düşer — playbook'a göre değerlendir.

**İstisnalar.** Tipik beş istisna: (1) ihlal dışında kamuya açık olan/olacak bilgi, (2) alıcının zaten sahip olduğu, (3) gizli bilgiye başvurmadan bağımsız geliştirilen, (4) üçüncü kişiden kısıtsız alınan, (5) kanun, mahkeme, savcılık ya da düzenleyici kurum (ör. SPK, BDDK, Rekabet Kurumu, KVKK) kararıyla açıklanması zorunlu olan — hukuken izin verildiği ölçüde açıklayana önceden bildirimle. Hangisinin şart olduğu playbook sorusudur.

**Residuals.** Alıcının yardımsız hafızasında kalan bilgiyi kullanma hakkı. Dar ("unaided memory") ya da geniş (not ve kopyalar dahil) olması playbook'a göre. Geniş residuals, TTK m. 55/1-c,d korumasını sözleşmeyle fiilen bertaraf edebilir → en az SARI.

**Süre ve sonrası.** Sözleşme süresi, sona erme sonrası gizlilik süresi, ticari sırlar için daha uzun koruma. Türk hukukunda süresiz gizlilik yükümlülüğünün sınırı (kişilik hakları, TBK m. 27/1) **tartışmalı — içtihadı kontrol et**; playbook süreli istiyorsa süreyi ve ticari sır istisnasını ayrı yaz.

**Kısıtlayıcı taahhütler.** Çalışan/müşteri ayartmama, rekabet yasağı, münhasırlık.
- Rakipler arasında ayartmama ya da münhasırlık rekabeti kısıtlayıcı anlaşma sayılabilir (4054 m. 4). Rekabet Kurulu'nun işgücü piyasası uygulamasını ezberden söyleme; ara: `tr_kurum_karari_ara(kurum="rekabet", query="işgücü piyasası centilmenlik anlaşması ayartmama")`.
- Bir gerçek kişiyi (ör. alıcının yöneticisi, danışmanı) bağlayan rekabet yasağı işçi için ancak yazılı ve TBK m. 444/2 şartlarıyla geçerlidir → `/arthurlegal:employment-legal-hiring-review`.
- Playbook sessizse sor; bu taahhütler yargı çevresine duyarlıdır.

**Cezai şart.** Türk NDA'larında sık görülür. Alacaklı ya ifayı ya cezayı ister; ifa zamanı/yeri için kararlaştırılan cezada ikisini birden isteyebilir (TBK m. 179/1-2). Zarar olmasa da ceza ödenir; zarar cezayı aşarsa aşan kısım için borçlunun kusurunu ispat gerekir (TBK m. 180). Hâkim aşırı cezayı kendiliğinden indirir (TBK m. 182/3), ama **tacir borçlu** aşırılık iddiasıyla indirim isteyemez (TTK m. 22). Tacirler arası NDA'da yüksek tek yönlü ceza → playbook'a göre en az SARI. Tacir aleyhine indirim yasağının sınırı (ekonomik çöküş hâli) **tartışmalı — içtihadı kontrol et**.

**Yargılama giderleri ve avukatlık ücreti.** Kanunda aleyhine hüküm verilen taraf yargılama giderlerini öder; giderler arasında kanuna göre takdir edilen vekâlet ücreti vardır (HMK m. 323/1-ğ, m. 326/1). Gerçek avukatlık ücretinin sözleşmeyle karşı tarafa yüklenmesi ve tek yönlü yükleme kaydının talep edilebilirliği **tartışmalı — içtihadı kontrol et**. Karşılıklı mı, tek yönlü mü, playbook'a göre değerlendir.

**İhtiyati tedbir.** "Teminatsız tedbir istenebilir" kaydı mahkemeyi bağlamaz: tedbir isteyen kural olarak teminat gösterir; mahkeme gerekçe göstererek teminat almayabilir (HMK m. 389, m. 392/1). Kaydı silmek gerekmez, ama ona güvenerek hesap yapma.

**İade/imha, yedek ve yasal saklama.** İade/imha kaydında standart yedek ve arşiv sistemleri istisnası var mı? Ayrıca tacir ticari mektuplarını (bir ticari işe ilişkin tüm yazışmalar) on yıl saklamakla yükümlüdür (TTK m. 82/1-b,c, m. 82/2, m. 82/5) → "kanunen saklanması zorunlu kayıtlar gizlilik yükümlülüğü sürmek kaydıyla saklanabilir" istisnası yoksa ekle. Playbook bu istisnayı zorunlu tutuyor mu, bak.

**Kişisel veri.** NDA kapsamında kişisel veri aktarılacaksa NDA bir veri işleme sözleşmesi değildir → `/arthurlegal:privacy-legal-dpa-review` öner; yurt dışı aktarım varsa KVKK m. 9 orada incelenir.

**Uygulanacak hukuk, yetki, tahkim.** `## Playbook` → `Governing law and venue`. Türk hukukunda yetki sözleşmesini yalnız tacirler ya da kamu tüzel kişileri yapabilir; yazılı olmalı, hukuki ilişki belirli/belirlenebilir olmalı ve mahkeme gösterilmelidir (HMK m. 17-18). Tahkim kaydı yazılı olmalıdır (HMK m. 412/3; yabancılık unsuru varsa MTK m. 4). Gizlilik ihlalinden doğan para alacağı ticari davaysa dava öncesi arabuluculuk dava şartıdır (TTK m. 5/A). Yabancı hukuk ya da yabancı mahkeme seçilmişse (MÖHUK m. 24, m. 47) → `/arthurlegal:commercial-legal-governing-law-review`.

**İmza.** Güvenli elektronik imza elle atılan imzayla aynı sonucu doğurur (5070 m. 5/1); platform tıklamalı "basit" e-imza güvenli e-imza değildir. NDA şekle bağlı olmadığından geçerlilik sorunu çıkmaz, ispat sorunu çıkabilir → imza yöntemini profildeki tercihe göre not et.

## Redline inceliği

Redline bir müzakere belgesidir, yeniden yazım değildir. En küçük düzeltme: kelime → ifade → alt bent → cümle → ancak gerekirse tüm madde. ("on iki (12)" → "yirmi dört (24)"). Tüm maddeyi değiştirdiysen ileti notunda söyle: "8.2'yi değişiklikler kapsamlı olduğu için işaretlemek yerine yeniden yazdık; farkı birlikte geçebiliriz." Şüphede, daha küçük.

**Yargı çevresi varsayımı:** triaj eklenti ayarındaki hukuk ve kısıtlayıcı taahhüt pozisyonlarını uygular; NDA profilin dışında bir yargı çevresine bağlıysa çıktıda işaretle, triajın olduğu gibi aktarılamayacağını yaz; yabancı kural ezberden yazılmaz (`/arthurlegal:commercial-legal-governing-law-review`).

## Çıktı kuralları

- **Karmaşıklık filtresi:** Bir sorunu çözmek yeni ifade yazmayı, maddeyi yeniden kurmayı ya da esaslı yeni hüküm eklemeyi gerektiriyorsa deneme; yaz: "Madde [X] — hukuk incelemesine yönlendirin." Özette yalnız mekanik işlemler (sil, çıkar, kelime/ifade değiştir).
- **Temiz NDA kuralı:** Hiç bayrak yoksa özet yalnız şunu der: "Kırmızı bayrak yok. Standart süreçle imzaya yönlendirin." Temiz NDA için uzun rapor yazma.

## Karşı taraf bağlamı ve CLM

**Büyük kurumsal karşı taraf** NDA'sını genelde müzakere etmez: KIRMIZI gerçekten anlaşma bozucu mu, "bizim formdan farklı" mı? İlişki önemliyse onların metnini kabul kararını eskalasyona götür, kendin verme. **Girişimler** genelde bizim metni kabul eder; en hızlı yol çoğu zaman "bizimkini kullanalım"dır. **CLM** bağlıysa: YEŞİL → standart NDA akışında kayıt öner; SARI → işaretli noktaları not olarak ekleyip öner; KIRMIZI → kayıt açma, sonraki adıma avukat karar verir.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6102", madde_no=["5/A","22","55","56","82"])
tr_mevzuat_madde_getir(number="6098", madde_no=["12","27","116","179","180","182","396","444"])
tr_mevzuat_madde_getir(number="6100", madde_no=["17","18","323","326","389","392","412"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="gizlilik sözleşmesi cezai şart tacir indirim", date_from="2020-01-01")
tr_kurum_karari_ara(kurum="rekabet", query="işgücü piyasası centilmenlik anlaşması ayartmama")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Atıf etiketi: `[ArthurLegal TR — 6102 m. X — GG.AA.YYYY]`; ezberden gelen için `[model bilgisi — doğrula]`.

## Sonuç doğuran işlem kapısı (imza)

YEŞİL'den imzaya geçmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> Bu adımın hukuki sonucu var: NDA'yı imzalamak şirketi bağlar; cezai şart varsa ihlalde zarar ispatı gerekmeden ödenir. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz bir sayfalık özet: karşı taraf, NDA yönü (karşılıklı / tek taraflı), yapılan playbook kontrolleri, playbook'un kapsamadığı noktalar, olduğu gibi imzalanırsa ne ters gidebilir ve avukata sorulacak üç soru. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan bu kapıdan geçme.

## Kapanış eylemi

`## NDA triage preferences` → `closing_action` oku. Tanımlıysa her çıktının sonuna aynen ekle (ör. "Bu analizi ve NDA'yı imzadan önce son teyit için hukuka gönderin." / "Standart NDA akışıyla [CLM]'e gönderin." / "Bu çıktıyı ve NDA'yı sözleşme yöneticinize iletin."). Tanımlı değilse ekle: "NDA'yı standart onay sürecinizden geçirin." Cold-start görüşmesi bunu sorar: "NDA triajını bitiren kişi çıktıyla ne yapsın?"

Ardından profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu triaja göre uyarla (redline gönder, eskalasyon, ek olgu iste, bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Müzakere etmez; ayırır.
- NDA yazmaz; cevap "bizim metni kullanalım" ise form [CLM ya da belge sistemi]nden alınır.
- SARI noktalarda karar vermez; insana gösterir.
- NDA şartları hakkında kendi pozisyonunu koymaz; pozisyonlar eklenti ayarındadır. Türk hukukunun sınırlarını ise her seferinde araçtan çeker.

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
