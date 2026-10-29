---
name: ip-legal-fto-triage
description: >
  Kullanım serbestisi (freedom-to-operate, FTO) elemesi — engelleyebilecek
  patent ve faydalı modellere yapılandırılmış ilk bakış; FTO görüşü değildir.
  Türk hukuku tabanı: patent hakkının kapsamı ve sınırları (SMK m. 85),
  dolaylı kullanım (m. 86), önceki kullanım hakkı (m. 87), istemlerle
  belirlenen koruma kapsamı ve eşdeğerlik (m. 89), tecavüz fiilleri (m. 141).
  Bir ürün, usul ya da özellik engelleyici patent açısından incelenirken,
  "lansmanı durduracak bir şey var mı" sorulduğunda ya da patent vekili
  incelemesinden önce en makul patentlere karşı istem tablosu taslağı
  gerektiğinde kullan. Bu skill bir ürünün piyasaya çıkmaya hazır olduğu
  sonucuna asla varmaz.
argument-hint: "[ürünü / usulü / özelliği ve ülkeleri yazın — ya da yalnız konuyu, gerisini sorarım]"
---

# /fto-triage — Kullanım Serbestisi Elemesi

## BU BİR FTO GÖRÜŞÜ DEĞİLDİR

**Her çıktının en üstüne yaz. Çıkarma, yumuşatma, okuyucunun atlamasına izin verme.**

> **Bu bir kullanım serbestisi (FTO) görüşü değildir.** FTO görüşü; kapsamlı araştırma, istemlerin tam yorumu ve her ilgili patentin her istemine karşı unsur unsur tecavüz analizi gerektiren, genellikle patent vekili ya da bu alanda uzman avukatın verdiği mesleki bir değerlendirmedir. Bu eleme, ortada ne olabileceğine yapılandırılmış bir ilk bakıştır. "Belirgin engelleyici patent yok" sonucu, elemenin bir şey bulmadığı anlamına gelir; ürünün serbest olduğu anlamına gelmez. Üretme, kullanma, satma, ithal etme kararı resmî bir FTO çalışması ve uzman görüşüyle verilen bir iş kararıdır.

Engelleyici patenti gözden kaçırmak geri dönüşsüz kapıdır: ürün çıkar, bir yıl sonra ihtiyati tedbir ve elkoyma (m. 159/2) gelir. Fazla bayrak geri dönüşlü kapıdır. Her zaman geri dönüşlü tarafta kal.

### "Bilme" notu (ABD'deki "willfulness" yerine)

Türk hukukunda ABD'deki ayrıcalıklı FTO görüşü koruması yoktur: avukatın sır saklama yükümlülüğü (Av. K. m. 36) belgeyi müvekkilin elinde korumaz. Bu eleme belirli patentleri ortaya çıkarır; bundan sonra şirket o patentleri biliyor sayılabilir. Bu, satma/dağıtma/ithal fiillerinde ve usul patentinde aranan "bildiği ya da bilmesi gerektiği" ölçütü (m. 141/1-b, c) ve yayımdan önceki dönem için kötüniyet tespiti (m. 141/3) bakımından önemlidir. SMK m. 149-151'de ABD'deki gibi kasta bağlı tazminat katlaması yer almaz; ancak yoksun kalınan kazançta hakkaniyete uygun ek pay (m. 151/4) ve itibar tazminatı (m. 150/2) vardır. Bu yüzden çıktıyı dar çevrede tut; eleme sonrası yolu uzman yazılı olarak belirlesin.

## Destination check

Çıktı hukuk dışına, karşı tarafa ya da geniş kanala gidecekse dur; yalnız hukuk için tam sürüm, iş birimi için patent numarası içermeyen arındırılmış sürüm öner. Kanonik kural: `## Shared guardrails → Destination check`.

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:ip-legal-matter-workspace switch <slug>` ya da `practice-level`." `matter.md`'yi yükle; çıktıyı matter klasörüne yaz; `Cross-matter context` `on` değilse başka matter'ı okuma. FTO işleri sıklıkla **clean-team** ya da **heightened** gizlilik işaretiyle açılır; `matter.md`'deki işarete uy.

## Önce profil

`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve `firm-profile.md`: `## Who's using this` (rol), `## IP practice profile` → `Registered in` ve `Outside counsel roster` (patent vekili/dış uzman), `## Enforcement posture`, `## Available integrations` (patent arama bağlayıcısı var mı), `## Decision posture on subjective legal calls` (bu skill "tecavüz yok" demez).

Ayar `[PLACEHOLDER]` içeriyorsa: `/arthurlegal:ip-legal-cold-start-interview` ya da **"provisional"** — genel varsayımlar (Türkiye, orta risk, avukat rolü, playbook yok), her bulguda `[PROVISIONAL]` etiketi ve sonda "profilinizi kurun" notu.

## Girdi

Tek seferde sor:

> 1. **Ürün, usul ya da özellik.** Ne üretilecek, kullanılacak, satılacak, ithal edilecek? Pazarlama dilini değil teknik özü yazın.
> 2. **Teknik ayrıntı.** Mimari şema, teknik şartname, ürün sayfası, kod — ne kadar ayrıntı, o kadar gerçek eleme.
> 3. **Ülkeler.** Nerede üretilecek, satılacak, ithal edilecek? Türkiye'de üretme, satma, kullanma, ithal ve bu amaçlarla elde bulundurma ayrı ayrı önlenebilir fiillerdir (m. 85/2). Söylemezseniz Türkiye.
> 4. **Bilinen patentler.** Rakip portföyü, standart (SEP) havuzu, ihtarname, mühendisin duyduğu bir patent?
> 5. **Zamanlama.** Lansmana aylar varsa tasarım değişikliği masadadır; ürün zaten satılıyorsa riski sınırlama modundayız.

Tarif muğlaksa bir kez daha bastır: "Ne yapıyor, nasıl yapıyor, yeni olduğunu düşündüğünüz parça ne? İstemler o seviyede yaşar."

## Kapsam — patent ve faydalı model

- **Patent ve faydalı model** bu skill'in konusudur. Faydalı model araştırma raporu ve itiraz/görüş değerlendirmesiyle verilir (m. 143/5-10); verilmesi Kurumun geçerlilik garantisi değildir (m. 143/13) ve verildikten sonra yalnız mahkemeden hükümsüzlük istenebilir (m. 143/11) — tehdit ve geçersizlik savunması açısından ayrı işaretle. Patent hükümleri, çelişmedikçe faydalı modele de uygulanır (m. 145/1).
- **Tasarım** (tescilli ya da tescilsiz) farklı testtir — istem tablosu çizme; `/arthurlegal:ip-legal-infringement-triage` tasarım moduna ve tasarım uzmanına yönlendir, ayrı iş akışı olarak işaretle.
- **Görünüm riski** varsa paralel kanalları işaretle: üç boyutlu marka (m. 4 — malın/ambalajın biçimi), tescilsiz tasarım (m. 55/4) ve karıştırılmaya yol açan önlemler nedeniyle haksız rekabet (TTK m. 55/1-a-4).

## Araştırma

**ArthurLegal MCP'de patent veritabanı ve TÜRKPATENT aracı yoktur.** Seçenekler:
- `## Available integrations` içinde patent arama bağlayıcısı (ör. Solve Intelligence) bağlıysa çalıştır; tarih, sorgu, ülkeler ve tarih aralığını not et.
- Bağlı değilse elle: TÜRKPATENT web sitesindeki patent araştırma ekranı; Türkiye'yi kapsayan Avrupa ve PCT başvuruları için `${CLAUDE_PLUGIN_ROOT}/references/turkpatent-rehberi.md`'de sayılan dış veri tabanları (Espacenet, PATENTSCOPE — ArthurLegal aracı değildir). Türkiye'yi belirleyen Avrupa patentlerinin Türkiye'deki geçerlilik durumunu TÜRKPATENT sicilinden elle kontrol et.
- Hiçbiri yoksa aynen yaz:

> **Patent veritabanı araması yapılmadı.** Bu eleme TÜRKPATENT sicilini, Avrupa/PCT yayınlarını ya da başka bir patent külliyatını taramadı. Kapsamdaki ülkelerde yapılandırılmış araştırma olmadan bu eleme lansman kararına dayanak olamaz. Aşağıdaki analiz kullanıcının adını verdiği ya da konuşmada geçen patent ve başvurularla sınırlıdır.

**Ek sinyaller (patent bulgusu değildir):** rakip başvuruları, ilgili standartlara SEP beyanları, teknoloji alanındaki dava geçmişi — `tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="patent tecavüz <teknoloji terimi>", kelime_modu="hepsi")`. Her biri daha dikkatli bakma nedenidir; "sinyal" diye ayrı başlıkta göster.

## Her ilgili patent için

- Numara (başvuru no. farklıysa o da), ülke/ofis, başlık, sahip, buluşu yapanlar
- Başvuru ve varsa rüçhan tarihi (patent ve faydalı model rüçhanı ilk başvurudan 12 ay: m. 93/1), veriliş tarihi
- **Koruma bitişi:** başvuru tarihinden patentte 20, faydalı modelde 10 yıl; uzatılamaz (m. 101/1)
- **Yürürlük:** yıllık ücretler başvurudan itibaren ikinci yılın sonunda ve her yıl vadesinde ödenir; vadede ödenmezse ek ücretle altı ay; o da geçerse hak vade tarihi itibarıyla sona erer, ama bildirimden itibaren iki ay içinde telafi ücretiyle yeniden geçerlilik kazanabilir (m. 101/2-4; m. 140/1-c). "Sona ermiş" görünen patenti bu pencere kapanmadan ölü sayma; yeniden geçerlilikte üçüncü kişilerin kazanılmış hakları saklıdır (m. 101/5).
- Bağımsız ve bağımlı istem sayısı; verildiği hâliyle bağımsız istemler ve itiraz/hükümsüzlük sonucu değişmiş hâli
- İlgili işlemler: verilme kararının yayımından itibaren 6 ay içinde üçüncü kişi itirazı (m. 99/1), hükümsüzlük davaları, Yargıtay kayıtları
- Dosya geçmişi: başvuru sahibinin kapsamı daraltan beyanları (m. 89/6)
- Yayımlanmış ama verilmemiş başvuru: yayımdan itibaren geçici koruma (m. 97/4); mahkeme m. 99/3 ya da /7 uyarınca yayımdan önce iddiaların geçerliliğine karar veremez (m. 141/4)

**Sessizce tamamlama.** Patent numarası, istem unsuru ya da bitiş tarihi uydurma. Yıllık ücret durumu doğrulanmadıysa yaz: "yıllık ücret durumu aramadan doğrulanmadı — TÜRKPATENT sicilinden teyit edin."

## İstem tablosu — ilk geçiş

Elemenin özü. Ürüne en yakın okunan 2–5 patenti seç; her bağımsız istemi unsur unsur yürü.

| İstem unsuru | Ürün bunu uyguluyor mu? | Dayanak |
|---|---|---|
| "[giriş kısmı]" | [evet / hayır / olabilir / yoruma bağlı] | [ürünün neresi karşılıyor; ne karşılamıyor; ne belirsiz] |
| "[unsur 1]" | | |

**Türk hukukunda tablonun kuralları:**
- **Kapsam istemlerle belirlenir;** tarifname ve resimler yorumda kullanılır (m. 89/1). İstemler kelimelerin anlamıyla sınırlı okunmaz, ama istemde talep edilmeyen özelliklere de genişletilemez (m. 89/2); örneklerle sınırlı yorumlanmaz (m. 89/7).
- **Önce lafzi okuma:** istemin her unsuru üründe var mı? Bir unsur yoksa o istem bakımından lafzi tecavüz bayrağı düşer. Unsurların tamamının aranması uygulamada yerleşik ölçüttür; sınır hâllerde **tartışmalı — içtihadı kontrol et**.
- **Eşdeğerlik ayrı geçiştir:** tecavüz iddiası tarihinde istem unsuruna eşdeğer unsurlar dikkate alınır; esas itibarıyla aynı işlevi, aynı şekilde görüp aynı sonucu doğuran unsur genel olarak eşdeğerdir (m. 89/5). "Hayır" çıkan her unsur için eşdeğerlik okumasını ayrıca işaretle; başvuru sahibinin beyanları (m. 89/6) eşdeğerliği daraltabilir — karar avukatındır.
- **İstem yorumu avukatın işidir.** Bir terim dar ya da geniş yorumlanabiliyor ve sonuç değişiyorsa iki yorumu da yaz; birini sessizce seçme.
- **Dolaylı kullanım (m. 86):** buluşun esasını oluşturan unsur ya da araçların yetkisiz kişilere verilmesi, bilme şartıyla; piyasada her zaman bulunan ürünlerde teşvik yoksa uygulanmaz (m. 86/2). Yalnız bayrak.
- **Usul patenti:** ürün yeniyse, izinsiz üretilen aynı ürünün patentli usulle elde edildiği kabul edilir ve aksini davalı ispatlar (m. 141/2) — ispat yükü bayrağı.
- **Bölünmüş tecavüz** (fiillerin farklı kişilerce yapılması): Türk hukukunda açık düzenleme yok — **tartışmalı**, yalnız bayrak.

**Yabancı ülke kapsamdaysa** Türk tablosunu oraya taşıma; kuralı araçla çek:
- Almanya: `de_norm_getir(kanun="PatG", norm="9")`; kapsam ve dolaylı kullanım normlarını `de_gesetz_ara` ile bul.
- Birleşik Krallık: `uk_get_section(year="1977", number="37", section="60")` (Patents Act 1977 — tecavüz ve istisnalar).
- AB üniter patent: `eu_get_document_text(celex="32012R1257")`. Avrupa Patent Sözleşmesi (EPC), Birleşik Patent Mahkemesi Anlaşması, ABD, Çin, Japonya patent hukuku: "ArthurLegal'da doğrulanmış kaynak yok; ilgili ülkenin patent vekilinden görüş alın."

**Karar duruşu:** bu skill "tecavüz yok" demez. Şunlardan biri:
- "Ürün İstem X'in her unsurunu lafzen uyguluyor; ilerlemeden önce uzman incelemesi gerekli."
- "Bir ya da daha çok unsur açıkça mevcut değil; lafzi tecavüz ve eşdeğerlik için uzman incelemesi gerekli."
- "[Y] unsurunda istem yorumu belirleyici; ilerlemeden önce uzman yorumu gerekli."

## Sınırlar ve savunmalar (bayrak — karar değil)

- **Hakkın kapsamı dışındaki fiiller (m. 85/3):** sınai/ticari amaç taşımayan özel fiiller; deneme amaçlı fiiller; ilaç ruhsatı için gerekli test ve deneyler; eczanede reçeteye göre seri üretim olmadan hazırlama; geçici olarak Türkiye'de bulunan taşıtlar.
- **Önceki kullanım hakkı (m. 87):** başvuru tarihinde ya da önce buluşu ülke içinde iyiniyetle kullanan ya da ciddi ve gerçek tedbir alan; işletmenin makul ihtiyaçlarıyla sınırlı, lisansla genişletilemez, ancak işletmeyle devredilir. Kullanım tarihine ilişkin delil var mı?
- **Hakkın tüketilmesi (m. 152):** hak sahibi ya da izniyle piyasaya sunulan ürünlerle ilgili fiiller kapsam dışıdır. İlk piyasaya sunmanın yurt dışında olmasının etkisi **tartışmalı — içtihadı kontrol et**.
- **Geçersizlik:** hükümsüzlük nedenleri (m. 138/1 — patentlenebilirlik şartları, yetersiz açıklama, ilk hâlin aşılması, patent isteme hakkı yokluğu, koruma kapsamının aşılması). Görüş bildirme; bilinen önceki teknik ve itiraz/hükümsüzlük sonuçlarını listele.
- **Yeniden tesis arası iyiniyetli kullanım (m. 107/3):** hakkın kaybı ile yeniden tesis kararının yayımı arasında iyiniyetle kullanan ya da ciddi tedbir alan kişinin ücretsiz kullanmaya devam hakkı.

## Açık sorular

Her patent için gerçek bir FTO çalışmasının cevaplayacağı soruları listele, örneğin: sicildeki sahip ve devirler güncel mi (devir sözleşmeleri noter onaylı ve sicile kayıtlı mı: m. 148/4-5)? Dosya geçmişinde terim [X] için ne dendi? İtiraz ya da hükümsüzlük yoluyla istemler değişti mi? Lisans (sözleşmesel, standart havuzu) mevcut mu? Sahibin Türkiye'deki dava geçmişi ne?

## Önerilen sonraki adımlar

- **Bağımsız istemin her unsuru lafzen karşılanıyor:** *dur ve uzman al.* Seçenekler: resmî FTO görüşü, tasarım değişikliği, lisans, itiraz (verilme kararının yayımından 6 ay: m. 99/1) ya da hükümsüzlük davası (koruma süresince ya da sona ermeyi izleyen 5 yıl: m. 138/5), riski bilerek ilerleme. Seçim, uzmanın bilgilendirdiği iş kararıdır.
- **Unsurlar iki yöne işliyor ya da yorum belirleyici:** uzmandan tam FTO çalışması; bu elemeyle lansman yapılmaz.
- **Belirsizliği gidermek için:** hak sahibinden görüş istenip bir ay içinde cevap gelmez ya da cevap kabul edilmezse tecavüzün mevcut olmadığının tespiti davası açılabilir; bildirim dava şartı değildir ve kendisine tecavüz davası açılmış kişi bu davayı açamaz (m. 154/1). Görüş istemek patenti "bilme"yi belgeler — avukat kararı.
- **Patent sona ermiş/ücretsiz görünüyor:** yürürlüğü uzman sicilden teyit etsin (telafi penceresi: m. 101/4).
- **Veritabanı yoktu:** sıradaki adım resmî araştırmadır, lansman kararı değil.
- **Her zaman:** "bilme" notunu tekrarla ve sonraki yolun uzman tarafından yazılı belgelenmesini öner.

## Çıktı

Eklenti ayarı `## Outputs` → üst başlık. Rol avukatsa dar dağıtımlı hukuk belgesi olarak işaretle; değilse aşağıdaki kapı.

```markdown
[ÜST BAŞLIK]

# FTO Elemesi — İlk Geçiş (GÖRÜŞ DEĞİLDİR)

**Bu bir FTO görüşü değildir.** "Belirgin engelleyici patent yok" sonucu ürünün serbest
olduğu anlamına gelmez. Ürün kararından önce patent vekili/uzman avukat değerlendirmelidir.

**Eleme sonucu:** [YEŞİL / SARI / KIRMIZI — tek cümle neden]

## Konu
- **Ürün / usul / özellik:** [teknik öz]
- **Dayanılan teknik bilgi:** [şartname, şema, sayfa, kod, mühendis anlatımı]
- **Ülkeler ve fiiller:** [üretim / satış / kullanım / ithal — m. 85/2]
- **Zamanlama:** [lansman öncesi / yakın / satışta]

## Araştırma kapsamı
- **Kaynaklar:** [bağlayıcı / TÜRKPATENT elle / Espacenet-PATENTSCOPE elle — ya da "araştırma yapılmadı"]
- **Sorgu, sınıflar, tarih aralığı:** [...]
- **Taranmayanlar:** [sahip bazlı tarama, SEP, tasarımlar, yabancı eşdeğerler]

## Bulunan patentler
| Patent | Ülke | Sahip | Rüçhan / veriliş | Bitiş | Yürürlükte mi? | Kaynak |
|---|---|---|---|---|---|---|

## İstem tabloları — ilk geçiş
### [Patent no.] — bağımsız İstem [N]
> "[İstemin tam metni]"
| Unsur | Üründe var mı? | Dayanak |
|---|---|---|
**Lafzi okuma:** [...] **Eşdeğerlik (m. 89/5, yalnız bayrak):** [...]
**Dolaylı / bölünmüş (yalnız bayrak):** [...]

## Sınırlar ve savunmalar (bayrak)
## Açık sorular
## Sinyaller (doğrulanmış patent değildir)
## Önerilen sonraki adımlar
## "Bilme" notu
## Atıf doğrulaması
Her patent numarası, istem alıntısı, tarih ve dosya geçmişi bilgisi yetkili sicilden
(TÜRKPATENT, EPO sicili, ilgili ulusal ofis) açılarak doğrulanır. İstem alıntısı en sık hata
yeridir — tek kelime analizi değiştirir.
```

## Avukat olmayan kullanıcı kapısı

`## Who's using this` → rol avukat değilse:

> Bu çıktı bir araştırma elemesidir, hukuki görüş değildir. Yalnız buna dayanarak ürünü piyasaya sürmek, satmaya devam etmek ya da yatırım yapmak hukuki sonuç doğurur: hak sahibi tecavüzün durdurulmasını, ürünlere elkonulmasını ve tazminat isteyebilir (SMK m. 149, m. 159). Karar vermeden önce sicile kayıtlı bir patent vekili ya da patent alanında uzman bir avukat değerlendirmeli (sicile kayıtlı patent vekilleri Kurum nezdinde işlem yapabilir: m. 160/1).
>
> Uzmana götüreceğiniz bir sayfalık özet: ürün tarifi, ülkeler, yapılan ve yapılmayan araştırma, bulunan patentler ve istem tablosu okumaları, açık sorular ve sorulacak üç soru. Avukat için bağlı olduğunuz baroya başvurabilirsiniz.

Analizi saklama; özetle birlikte teslim et. Elemenin dar çevrede kalması gereken bir hukuk belgesi olduğunu, hukukçu olmayan üçüncü kişilere iletilmemesini yaz.

## Çıktı yeri

Matter aktifse `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`; değilse `~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`. Yolu göster; matter aktifse `history.md`'ye tek satır ekle.

## Kapanış

`## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu elemeye göre uyarla (tam FTO iste, tasarım değişikliği, lisans görüşmesi, itiraz/hükümsüzlük değerlendirmesi, ek teknik bilgi, bekle). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- **FTO görüşü vermez.** Hiçbir zaman.
- İstem yorumunu karara bağlamaz; belirleyici terimi ve iki makul yorumu işaretler.
- Geçerlilik hakkında görüş bildirmez (yenilik, buluş basamağı, açıklama yeterliliği); bilinen itiraz/hükümsüzlük sonuçlarını not eder.
- İstem yazmaz; tazminat hesaplamaz (m. 151 hesabı bilirkişi ve uzman işidir).
- Marka, tasarım ya da ticari sır analizi yapmaz — `/arthurlegal:ip-legal-infringement-triage` ilgili modla.
- Çıktıyı karşı tarafa ya da dar çevre dışına aktarmaz.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6769", madde_no=["85","86","87","89","93","97","99","101","138","140"])
tr_mevzuat_madde_getir(number="6769", madde_no=["141","143","145","148","149","150","151","152","154","159"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="patent eşdeğerlik istem koruma kapsamı", kelime_modu="hepsi", date_from="2018-01-01")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma; seçenekleri say (sorguyu genişlet / başka araç / `[web — doğrula]` / dur ve avukata işaretle).
