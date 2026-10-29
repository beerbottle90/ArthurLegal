---
name: corporate-legal-diligence-issue-extraction
description: >
  Sanal veri odasındaki (VDR) belgeleri büronun kategori ve önemlilik
  eşiklerine göre okur; Türk hukuku merceğiyle (TTK pay devri, birleşme ve
  ticaret sicili hükümleri, TBK sözleşme/işletme devri, İş K. m. 6, 4054 m. 7,
  KVKK) sorunları çıkarır ve bulguları büronun not formatında yazar. "Veri
  odasını incele", "[klasör]'den sorunları çıkar", "due diligence incelemesi",
  "VDR'de ne var" denildiğinde ya da VDR belgeleri gösterildiğinde kullan.
argument-hint: "[VDR klasör yolu ya da kategori adı]"
---

# /diligence-issue-extraction — Due Diligence Sorun Çıkarımı

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`, `firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` yükle (çakışmada deal-context.md önce gelir). [Müvekkil] alıcı mı satıcı mı — deal-context.md'den al; satıcı tarafında amaç alıcının bulacaklarını önceden görmek ve açıklama notunu beslemektir.
2. Kategori yüksek hacimliyse ve araç tanımlıysa önce `ai-tool-handoff`'a bak.
3. Belgeleri oku, önemlilik süzgecini uygula, kategoriye göre çıkar.
4. Bulguları büro formatında yaz; kapanış öncesi eylem gerektirenleri closing-checklist'e aktar.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

VDR'de 2.000 belge var; işlem için önemli olan 30'u bunların içinde. Bu skill belgeleri CLAUDE.md `## M&A` bölümündeki inceleme yapısı (kategoriler, önemlilik eşikleri — `Diligence structure`) ve bulgu raporu formatı (şablon, ciddiyet şeması — `Issues memo format`) ile okur, sorunları çıkarır, büro formatında yazar. deal-context.md yoksa hangi işlem için çalıştığını sor.

## Önce işlem yapısını sabitle

Türk hukukunda sonuçların çoğu yapıya bağlıdır; deal-context.md'de yoksa sor ve notun başına yaz.

| Yapı | Sözleşmeler | Borçlar | Çalışanlar |
|---|---|---|---|
| **Pay devri** (AŞ / Ltd.) | Sözleşmenin tarafı değişmez; yalnız sözleşmedeki kontrol değişikliği (CoC) klozu tetiklenir | Geçmiş borçların tamamı şirkette kalır → tazmin, emanet (escrow), bedel tutma. Ltd. payında devreden ve devralan, devir öncesi amme alacaklarından (şirketten tahsil edilemeyen kısım, sermaye payı oranında) müteselsil sorumlu (6183 m. 35) | İşveren değişmez |
| **Malvarlığı / işletme devri** | Her sözleşme ayrıca devredilir: üç taraflı anlaşma ya da karşı tarafın önceden izni/sonradan onayı; geçerlilik devredilen sözleşmenin şekline bağlı (TBK m. 205). Ticari işletme bütün hâlinde devredilebilir; sözleşme yazılı, tescil ve ilan edilir (TTK m. 11/3) | Aktif ve pasifleriyle devralan, alacaklılara bildirim/ilan tarihinden itibaren sorumlu; önceki borçlu 2 yıl müteselsil (TBK m. 202). Yalnız seçili varlıkların devrinde m. 202'nin uygulanması **tartışmalı — içtihadı kontrol et** | İşyeri devrinde iş sözleşmeleri hak ve borçlarıyla devralana geçer; devreden 2 yıl müteselsil (İş K. m. 6; TBK m. 428) |
| **Birleşme** | Tescil anında devrolunan şirketin bütün aktif ve pasifi kendiliğinden devralana geçer (TTK m. 153/1). Sözleşmedeki devir yasağının birleşmeye uygulanıp uygulanmadığı **tartışmalı — içtihadı kontrol et** | Alacaklılar birleşmenin geçerlilik kazanmasından itibaren 3 ay içinde teminat isteyebilir (TTK m. 157) | TTK m. 178 (m. 158/4 yollamasıyla): işçi itiraz edebilir; eski ve yeni işveren müteselsil. İş K. m. 6/4: birleşmede m. 6'daki birlikte sorumluluk uygulanmaz |
| **Bölünme** (tam / kısmi, TTK m. 159) | Bölünme belgesindeki malvarlığı bölümüne göre | Alacaklı koruması ve borç dağılımı için bölünme hükümlerini ayrıca çek | TTK m. 178 |

Halka açık hedefte ayrıca: önemli nitelikte işlem ve ayrılma hakkı (6362 m. 23, 24), yönetim kontrolü edinilirse pay alım teklifi zorunluluğu (6362 m. 26); KAP açıklamalarını ve `tr_spk_bulten_icinde_ara` ile SPK bültenlerini tara.

## Akış

### Adım 1: VDR envanteri

VDR MCP'si (Box / Intralinks / Datasite) bağlıysa dizini çek; değilse kullanıcıdan dizin dökümü iste. Klasörleri talep listesi kategorilerine eşle; karşılığı olmayan kategorileri yaz.

```markdown
## VDR Envanteri: [işlem kodu]

| Talep kategorisi | VDR klasörü | Belge | Durum |
|---|---|---|---|
| Şirket ve ortaklık yapısı | /01-Sirket | 45 | İncelendi |
| Önemli sözleşmeler | /02-Sozlesmeler | 312 | Sürüyor |
| Fikrî ve sınai haklar | /03-FSMH | 89 | Başlanmadı |

**Boşluklar:** [VDR'de karşılığı olmayan kategoriler — ek talep gerekli]
```

**Kişisel veri.** VDR'de çalışan dosyaları, bordro ya da müşteri listeleri varsa: kişisel veri ancak kanuni usule ve ilkelere (hukuka uygunluk, belirli amaç, amaçla bağlantılı, sınırlı ve ölçülü olma) uygun işlenir (KVKK m. 4); açık rıza dışındaki işleme şartları m. 5/2'de sayılıdır; aktarım m. 8'e, VDR sunucusu ya da alıcı ekibi yurt dışındaysa m. 9'a tabidir. Hangi şarta dayanılacağı olaya bağlıdır — burada karar verme; maskeleme ya da anonim özet iste, `/arthurlegal:privacy-legal-use-case-triage` veya `/arthurlegal:privacy-legal-pia-generation`'a yönlendir. Bulgu metnine gereksiz kişisel veri (TCKN, sağlık bilgisi, kişi bazlı ücret) taşıma.

### Adım 2: Önemlilik süzgeci

Eşik CLAUDE.md'den, işleme özgü fark deal-context.md'den gelir. Eşik "yıllık bedeli X TL üstü" diyorsa her şeyi okuma: sözleşmeleri beyan edilen bedele (dosya adı / meta veri) ya da karşı tarafın önemine göre sırala, eşiğe ya da kategori sonuna kadar yukarıdan aşağı incele. Döviz cinsinden bedelde kur ve tarih yaz.

### Adım 3: Sorunları çıkar

**Önemli sözleşmeler:**
- **Kontrol değişikliği:** bu işlem tetikliyor mu; onay mı, fesih hakkı mı, yalnız bildirim mi? "Kontrol" nasıl tanımlı (pay çoğunluğu, YK çoğunluğunu seçme, dolaylı kontrol)? Kanunda genel bir CoC kuralı yok — sözleşmeyi oku.
- **Devir yasağı / onay şartı:** malvarlığı devrinde sözleşme alıcıya geçebilir mi (TBK m. 205)? Alacak devri yasağı var mı (TBK m. 183)?
- **Münhasırlık, rekabet yasağı, en çok kayrılan müşteri (MFN):** alıcının mevcut işini kısıtlıyor mu? Rekabet hukuku şüphesinde `tr_kurum_karari_ara(kurum="rekabet", query=...)`.
- **İşlem nedeniyle fesih hakkı** ve fesih ihbarının şekli: tacirler arasında noter, taahhütlü mektup, telgraf ya da güvenli e-imzalı KEP (TTK m. 18/3).
- **Olağandışı yükler:** sınırsız sorumluluk, tazmin, cezai şart, şirket kefaleti/garantisi.
- **Kira:** kiracı kira ilişkisini kiraya verenin yazılı rızası olmadan devredemez; işyeri kirasında kiraya veren haklı sebep olmadıkça rızadan kaçınamaz; devreden işyeri kiracısı sözleşme bitimine kadar, en fazla 2 yıl müteselsil sorumlu kalır (TBK m. 323; maddenin dipnotundaki 8 yıllık uygulanmama dönemi 1/7/2020'de doldu). Pay devrinde kiracı değişmez — CoC klozuna bak.
- **Kamu ihale sözleşmeleri:** zorunlu hâllerde ihale yetkilisinin yazılı izniyle devredilir; izinsiz devirde fesih ve yaptırım (4735 m. 16) → malvarlığı devrinde 🔴 adayı.
- **Uygulanacak hukuk / uyuşmazlık çözümü:** yabancı hukuk, yabancı mahkeme ya da yabancı tahkim yeri → tanıma-tenfiz (MÖHUK, New York Sözleşmesi) etkisi; analiz `/arthurlegal:commercial-legal-governing-law-review`'da. Yabancı kural ezberden yazılmaz: `uk_search_legislation`, `de_gesetz_ara` / `de_norm_getir`, `eu_search_eu_law`, `nl_`, `pl_`, `at_`, `ie_`, `fi_`, `es_`, `jp_`, `az_`; ABD için yalnız kuruluysa CourtListener (`${CLAUDE_PLUGIN_ROOT}/references/courtlistener-rehberi.md`); listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

**Şirket ve ortaklık yapısı:**
- **Pay sahipliği zinciri:** esas sözleşme ve değişiklikleri, ticaret sicili kayıtları ve TTSG ilanları (sicil herkese açıktır, onaylı suret alınabilir — TTK m. 35), pay defteri. Şirketle ilişkide yalnız pay defterinde kayıtlı kişi pay sahibi sayılır (AŞ, TTK m. 499/4; Ltd. pay defteri m. 594). Defter, sicil ve TTSG arasındaki tutarsızlık 🔴 adayıdır.
- **AŞ pay devri sınırlamaları:** bedeli tamamen ödenmemiş nama yazılı paylar ancak şirketin onayıyla devredilir (m. 491); esas sözleşme devri şirket onayına bağlayabilir (m. 492); borsaya kote olmayan paylarda red ancak esas sözleşmedeki önemli sebeple ya da payları gerçek değerle devralma önerisiyle (m. 493); onay verilmedikçe mülkiyet ve haklar devredende kalır, istem 3 ay içinde reddedilmezse onay verilmiş sayılır (m. 494). Nama yazılı pay senedinde devir ciro ve zilyetliğin geçirilmesiyle (m. 490/2); hamiline yazılı pay senedinde devir MKK'ya bildirimle hüküm ifade eder (m. 489). Borsaya kote paylar: m. 495.
- **Ltd. pay devri:** devir ve devir borcu doğuran işlem yazılı yapılır, imzalar noterce onanır; şirket sözleşmesinde aksi yoksa ortaklar genel kurulunun onayı şarttır ve devir bu onayla geçerli olur; başvurudan itibaren 3 ay içinde reddedilmezse onay verilmiş sayılır (m. 595). Onay genel kurulun devredilemez yetkisidir (m. 616/1-g); karar, sözleşmede aksi yoksa temsil edilen oyların salt çoğunluğuyla alınır (m. 620); geçişin tescili için müdürler sicile başvurur (m. 598). Geçmiş bir devirde noter onayı ya da genel kurul onayı eksikse zincir kırıktır → 🔴.
- **Pay sahipleri sözleşmesi** (önalım, birlikte satma / satmaya zorlama, oy anlaşması): esas sözleşmede mi, ayrı sözleşmede mi? Ayrı sözleşme kural olarak yalnız taraflarını bağlar; AŞ esas sözleşmesine konan bu tür kayıtların şirkete ve üçüncü kişilere karşı etkisi **tartışmalı — içtihadı kontrol et**. Ltd.'de önerilmeye muhatap olma, önalım, geri alım ve alım hakları pay senedinde açıkça belirtilmelidir (m. 593/2).
- **İşlemin gerektirdiği şirket onayları:** önemli miktarda şirket varlığının toptan satışı AŞ genel kurulunun devredilemez yetkisidir (m. 408/2-f); birleşme sözleşmesinin onay nisapları m. 151'de.
- **İlişkili taraf işlemleri:** YK üyesi genel kurul izni olmadan şirketle işlem yapamaz, şirket işlemin batıl olduğunu ileri sürebilir (m. 395/1); pay sahibi olmayan üyelere ve yakınlarına nakit borç ve teminat yasağı (m. 395/2).
- **Sermaye kaybı / borca batıklık:** son yıllık bilançoda sermaye ile kanuni yedek akçeler toplamının yarısı zarar sebebiyle karşılıksızsa YK genel kurulu hemen çağırır; üçte ikisi karşılıksızsa ve genel kurul sermayenin üçte biriyle yetinme ya da tamamlama kararı vermezse şirket kendiliğinden sona erer; borca batıklık şüphesinde ara bilanço ve mahkemeye bildirim (m. 376). Finansal tablolarla birlikte oku.
- **Grup yapısı:** iştirakler ve grup içi sözleşmeler; yabancı iştirak için `gleif_search_entities` / `gleif_get_group_structure` (LEI ve grup ilişkisi) — sonuç sicil kaydının yerine geçmez.

**Fikrî ve sınai haklar:**
- Sahiplik zinciri (kurucu, çalışan, yüklenici devirleri). Sınai mülkiyet hakkının devri yazılı ve noter onaylı olmalı; sicile kaydedilmeyen işlemden doğan haklar iyiniyetli üçüncü kişilere karşı ileri sürülemez (SMK m. 148/4-5). Telif (yazılım dahil) için FSEK'teki devir şekil şartlarını `tr_mevzuat_madde_getir(number="5846", ...)` ile çek; ayrıntı `/arthurlegal:ip-legal-ip-clause-review`.
- Üründe açık kaynak (copyleft) → `/arthurlegal:ip-legal-oss-review`. Kilit hak lisanslı mı, sahip olunan mı; lisansta devir/CoC.
- TÜRKPATENT sicil durumu: ArthurLegal'da TÜRKPATENT aracı yok — kaydı kurumun kendi sisteminden teyit ettir. Bekleyen ya da tehdit edilen uyuşmazlıklar.

**İş hukuku:**
- Kontrol değişikliğine bağlı ikramiye/tazminat (yönetici sözleşmeleri) ve maliyeti; kilit çalışan kaybı; rekabet yasağı geçerliliği → `/arthurlegal:employment-legal-hiring-review`.
- Yapıya göre devir sonuçları (yukarıdaki tablo). Devreden ya da devralan, iş sözleşmesini sırf işyeri devri nedeniyle feshedemez (İş K. m. 6/5).
- Bekleyen işçilik davaları, kıdem karşılıkları, SGK prim borcu, alt işveren/muvazaa, işçi görünümlü yükleniciler → `/arthurlegal:employment-legal-worker-classification`.

**Davalar ve idari süreçler:**
- Bekleyen dava, icra takibi, ihtiyati haciz/tedbir ve karşılıklar: satıcıdan güncel liste ve UYAP dökümü iste. `tr_ictihat_ara` yalnız yayımlanmış kararları kapsar; bekleyen dosyayı göstermez.
- Düzenleyici soruşturma ve idari para cezaları: `tr_kurum_karari_ara(kurum="rekabet", query="\"[hedef unvanı]\"")`; aynı şekilde `epdk`, `spk`, `bddk`, `btk`, `kvkk`. KVKK kararları çoğunlukla anonimdir — boş sonuç "yok" demek değildir.
- Örüntü uyuşmazlıklar (tüketici, ürün sorumluluğu, çevre).

**Halefiyet ve borç taşınması (alım tarafında her zaman bak):** yukarıdaki yapı tablosuna göre hangi borcun alıcıya geçtiğini yaz. Ayrıca: bekleyen/tehdit edilen haksız fiil ve ürün sorumluluğu talepleri, çevre yükümlülükleri, satıcının kapanış sonrası tasfiye planı (satıcı dağılırsa alacaklılar alıcıya yönelir), devralınan / hariç tutulan borç listesinin bilinen riskleri gerçekten kapsayıp kapsamadığı. İşletmeler aktif ve pasiflerin karşılıklı devralınması ya da katılma yoluyla birleşirse her iki işletmenin alacaklıları alacaklarını yeni işletmeden alabilir (TBK m. 203). Vergi ve SGK borcu → `/tax-legal` skill'leri; vergi ve SGK "borcu yoktur" yazılarını talep listesine koy.

### Adım 4: Her bulguyu yaz

> **Kaynak etiketi.** Kanun, içtihat ya da kurum kararına dayanan her bulguda kaynağı etiketle: `[ArthurLegal TR — 6102 m. X — GG.AA.YYYY]`, `[ArthurLegal TR — Rekabet Kurulu kararı künyesi — GG.AA.YYYY]`, `[web — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]` (VDR, işlem ekibi notu, dış avukat görüşü). Belge kaynağında VDR yolu ve dosya adı kalır. `doğrula` etiketliler önce kontrol edilir; etiketleri silme. Karar numarası ezberden yazılmaz; araçtan dönen künye birebir kullanılır.
>
> **Kullanıcının atfettiği maddeye katılmıyorsan metni getir.** Kullanıcı, işlem ekibi notu ya da satıcı açıklaması bir maddeyi senin beklemediğin bir önerme için atfediyorsa maddenin ne dediğini tahminle anlatma: `tr_mevzuat_madde_getir` ile çek ve alıntıla; çekemiyorsan "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" yaz ya da metni kullanıcıdan iste. Gerçek bir maddenin kendinden emin yanlış tarifi, "bilmiyorum"dan kötüdür.
>
> **Sessiz tamamlama yok.** Araç gereken dayanak için az sonuç dönerse dur: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç (`tr_ictihat_semantik_ara`, `tr_semantik_ara`), (3) web — `[web — doğrula]` etiketiyle, (4) doğrulanmamış diye işaretle ve dur." Düşük güvenli kaynağı kabul edip etmemeye avukat karar verir.

CLAUDE.md'deki bulgu şablonunu birebir kullan. Seed not madde imli ise madde imli yaz. Şablon yoksa:

```
Sorun #N: [Başlık]
Kategori: [talep listesi kategorisi]
Ciddiyet: [büro şemasına göre]
Belgeler: [VDR yolu + belge adı]
Bulgu: [belge ne diyor ve işlem için neden önemli]
Dayanak: [kaynak etiketi]
Öneri: [bedel düzeltmesi / tazmin / onay gerekli / beyan ve tekeffül / emanet / işlemden çekil]
Kapanış eylemi: [yok | closing-checklist kategorisi]
```

**Ciddiyet ayarı** (büro şeması yoksa):
- 🔴 **Kırmızı:** bedeli ya da yapıyı etkiler. Büyük müşteride onaya bağlı CoC; açıklanmamış önemli dava; kırık pay zinciri; fikrî hak sahiplik boşluğu; izinsiz devredilemeyen kamu sözleşmesi.
- 🟠 **Yüksek:** çözülebilir ama zamanlama riski taşır (onay uzun sürebilir, sicil düzeltmesi gerekir).
- 🟡 **Sarı:** dikkat ister, çözülebilir. Alınması muhtemel onay; düzeltilebilir açık kaynak sorunu; sınıflandırma riski.
- 🟢 **Yeşil:** dosyaya not. Beyanlarla tutarlı; beyan dışında eylem gerekmez.

### Adım 5: Kategoriye göre derle

Kategori içinde ciddiyete göre sırala. Başa CLAUDE.md `## Outputs` başlığını koy (role göre değişir; `## Who's using this`).

> Bu çıktı gizli VDR belgelerinden türetilmiştir ve onların gizlilik statüsünü devralır. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD tipi geniş bir belge koruması ("work product / privilege") değildir; avukatı bağlar, işlem ekibi dışına dağıtılan belge gizliliğini fiilen kaybeder. Dağıtımı işlem ekibiyle sınırla; başlık tek başına koruma yaratmaz.

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs]

# Due Diligence Sorunları: [işlem kodu] — [Kategori]

**İşlem yapısı:** [pay devri AŞ / pay devri Ltd. / malvarlığı-işletme devri / birleşme / bölünme]
**İncelenen belge:** [N] / [M]   **Kapsam:** [Tümü | > X TL eşiği | İlk N]
**Bulgular:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

## ⚠️ İnceleyen notu
- **Kaynaklar:** ArthurLegal MCP (`tr_`) — [madde sayısı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]

## Sonuç
[🔴 N engelleyici · 🟠 N yüksek · 🟡 N orta] — [işlem ekibinin bilmesi gereken tek şey]

[Her bulgu büro formatında]

## Boşluklar
- [Karşılığı gelmemiş talep listesi kalemi]
- [Atıf yapılan ama VDR'de olmayan belge]
```

## Aktarımlar

- **ai-tool-handoff:** CLAUDE.md `## M&A` YZ toplu inceleme aracı ayarı (`AI-assisted review`) Luminance/Kira diyorsa toplu sözleşme incelemesi oraya; bu skill ince belgeleri (yan mektuplar, tadiller, aracın zorlandığı her şey) okur.
- **deal-team-summary:** toplanan bulgular brifingi besler.
- **material-contract-schedule:** sözleşme düzeyindeki çıkarımlar ekin girdisidir.
- **closing-checklist:** kapanış öncesi ayrık eylem doğuran her bulgu kontrol listesine gider — yalnız "onay" etiketliler değil:
  - **Pay sahibi / YK işlemi:** genel kurul ya da YK onayı (TTK m. 151, 408/2-f, 492-494, 595/2), pay defteri kaydı, esas sözleşme değişikliği, tescil ve ilan. Nisabı, kanun/esas sözleşme dayanağını ve zamanlama kısıtını (çağrı süreleri, 3 aylık onay süreleri) yaz.
  - **Düzenleyici izin:** Rekabet Kurulu (4054 m. 7 ve 2010/4 sayılı Tebliğ), sektörel izinler (EPDK, BDDK, SPK, BTK, sigortacılık — kurum mevzuatından çek), halka açık hedefte SPK süreçleri.
  - **Karşı taraf onayı:** CoC, devir yasağı, kira (TBK m. 323), kamu sözleşmesi (4735 m. 16).
  - **İbra, fesih, borç kapama:** CoC'ye bağlı yönetici ibraları, kredi kapama (payoff) yazıları, rehin/ipotek fekki.
  - **Emanet / bedel tutma:** belirli bir soruna bağlı escrow ya da tazmin teminatı.

  Gri bölgedeki bulguyu (kapanış eylemi mi, kapanış sonrası taahhüt mü belirsiz) işaretleyerek aktar; closing-checklist sözleşmeye göre düşürebilir. Eksik aktarım geri alınamaz, fazla aktarım incelemede düzelir.

## Toplu işleme

Büyük kategorilerde (300 sözleşme) partiler hâlinde çalış. Her partiden sonra listeyi güncelle ve 🔴'yu hemen bildir — işlemi etkileyen sorunu kategori bitene kadar bekletme.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu çıkarıma göre uyarla (taslakla, eskalasyon, ek olgu iste, bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar. Yaklaşık 10'dan fazla sorun çıktıysa ya da istenirse panoyu öner (`## Outputs → Dashboard offer for data-heavy outputs`): ciddiyete ve kategoriye göre sayılar, önemlilik/kategori/VDR kaynağıyla sıralanabilir tablo.

## Bu skill ne yapmaz

- Sınırdaki önemlilik kararını vermez; eşiği uygular, sınırı insan çizer.
- Beyan ve tekeffülleri müzakere etmez; onları besleyen bulguları üretir.
- Toplu yapay zekâ incelemesinin yerini tutmaz; yüksek hacimli kloz çıkarımı `ai-tool-handoff` ile araca gider. Bu skill yargı katmanıdır.

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
