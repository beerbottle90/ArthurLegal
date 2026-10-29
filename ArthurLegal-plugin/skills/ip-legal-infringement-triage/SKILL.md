---
name: ip-legal-infringement-triage
description: >
  Marka, telif, patent/faydalı model, tasarım ve ticari sır için tecavüz
  elemesi — her iki yöne işleyen etkenlerle bayrak listesi; tecavüz var/yok
  tespiti değildir. Türk hukuku tabanı: SMK m. 7, 29, 30 (marka), m. 85-89,
  141 (patent), m. 59, 81 (tasarım), m. 149-159 (hukuki talepler, tazminat,
  ihtiyati tedbir); TTK m. 55-56 ve TCK m. 239 (ticari sır). Birinin
  hakkınızı ihlal edip etmediğini ya da sizin başkasının hakkını ihlal edip
  etmediğinizi değerlendirirken, taklit/kopya ürün çıktığında ya da bir işin
  takibe değip değmeyeceğine karar verirken kullan.
argument-hint: "[olguları ve hangi hak olduğunu yazın — ya da yalnız olguları, hakkı ben sorarım]"
---

# /infringement-triage — Tecavüz Elemesi

## BU BİR ELEMEDİR, TESPİT DEĞİLDİR

**Her çıktının en üstüne yaz. Çıkarma, yumuşatma.**

> **Bu bir elemedir; tecavüz olduğu ya da olmadığı yönünde bir tespit değildir.** Tecavüz analizi olgulara sıkı sıkıya bağlı ve hukuken karmaşıktır. Eleme etkenleri belirler ve en önemlilerini işaretler; sonuca varmaz. "Tecavüz var/yok" demek; olgular, hakkın kapsamı, uygulanacak hukuk ve savunmalar üzerinde avukat takdiri gerektiren bir hukuki görüştür. Yalnız elemeye dayanarak ihtarname göndermek, durmayı reddetmek, dava açmak ya da açmamak; karşı tarafın tecavüzün mevcut olmadığının tespiti davasına (SMK m. 154), haksız rekabet iddiasına, yargılama giderlerine ve tazminata yol açabilir.

Çakışmayı küçük göstermek geri dönüşsüz kapıdır: ihtar gönderilmez ve marka piyasada yaygın ad hâline gelir (iptal nedeni: m. 26/1-b); talep peşine düşülmez ve zamanaşımı işler; kopyalanmış içerik sitede kalır. Fazla bayrak geri dönüşlü kapıdır. Geri dönüşlü tarafta kal.

## Destination check

Çıktı karşı tarafa, geniş kanala ya da basına gidecekse dur; avukatın sır saklama yükümlülüğü (Av. K. m. 36) belgeyi müvekkilin elinde korumaz. Yalnız hukuk için tam sürüm, iş birimi için arındırılmış sürüm öner. Kanonik kural: `## Shared guardrails → Destination check`.

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:ip-legal-matter-workspace switch <slug>` ya da `practice-level`." `matter.md`'yi yükle; çıktıyı matter klasörüne yaz; `Cross-matter context` `on` değilse başka matter'ı okuma. Eleme genelde ihtarname ya da içerik kaldırmaya gider; pratik büro ise ve matter yoksa açılmasını öner — eleme, ihtar ve cevap aynı dosyada kalsın.

## Önce profil

`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve `firm-profile.md`: `## Who's using this` (rol); `## Enforcement posture` (agresif / ölçülü / temkinli ve mektup türüne göre onaylayıcı — yönlendirme buna uyar); `## IP practice profile` → `Registered in`; `## Brand protection`; `## Available integrations`; `## Decision posture on subjective legal calls`.

Ayar `[PLACEHOLDER]` içeriyorsa: `/arthurlegal:ip-legal-cold-start-interview` ya da **"provisional"** — Türkiye, orta risk, avukat rolü, playbook yok; her bulguda `[PROVISIONAL]` ve sonda "profilinizi kurun" notu.

## Mod seçimi

En başta sor:

> Hangi hakkı eliyoruz?
> 1. **Marka** — karıştırılma, tanınmış marka, karşılaştırmalı reklam
> 2. **Telif** — eser, mali/manevi hak, izin
> 3. **Patent / faydalı model** — istem tablosu, lafzi okuma + eşdeğerlik
> 4. **Tasarım** — genel izlenim, tescilli/tescilsiz
> 5. **Ticari sır** — sır niteliği, önlemler, hukuka aykırı elde etme/ifşa
> 6. **Karışık / emin değilim** — olguları anlatın, ben ayırırım

Aynı olgu birden çok hakkı doğurabilir (logomuz kullanılıyor → marka; ürün bizimkinin kopyası → patent/tasarım/telif; eski çalışanımız kurdu → ticari sır). **Birden çok hak varsa her birini ayrı elemeden geçir;** karıştırma — etkenler, mahkeme yolları ve talepler farklıdır.

## Ortak girdi

> 1. **Pozisyon.** Hak sahibi siz misiniz (sizinkini alıyorlar), yoksa iddia edilen taraf mı? Etkenler simetriktir ama çıktı farklıdır: biri ihtarnameye, diğeri risk notuna gider.
> 2. **Ülke.** Varsayılan Türkiye. Yabancı hukuk ihtimali varsa işaretlerim.
> 3. **Zaman.** Ne zaman öğrendiniz? Fiil ne zaman başladı? (Aşağıdaki saatler.)
> 4. **Deliller.** Ekran görüntüsü, URL, ambalaj fotoğrafı, fatura, kod parçası, eski çalışan sözleşmesi, tescil belgesi.

Cevap gelmeden etkenlere geçme.

### Saatler (her modda kontrol et)
- **Hukuki talepler:** SMK'dan doğan özel hukuk taleplerinde TBK zamanaşımı uygulanır (SMK m. 157): tazminat istemi zararı ve yükümlüyü öğrenmeden itibaren 2 yıl, her hâlde fiilden itibaren 10 yıl; fiil ceza kanunlarında daha uzun zamanaşımına tabi suçsa o süre (TBK m. 72). Sürekli tecavüzde başlangıç ve durdurma/men taleplerine zamanaşımı uygulanıp uygulanmayacağı **tartışmalı — içtihadı kontrol et**.
- **Ceza yolu:** marka suçları (SMK m. 30/6) ve TCK m. 239 kural olarak şikâyete bağlıdır; şikâyet, fiil ve failin öğrenildiği günden itibaren 6 ay içinde yapılmazsa soruşturma yapılamaz (TCK m. 73/1-2).
- **Sessiz kalma:** marka sahibi sonraki tarihli markanın kullanımını bilip 5 yıl sessiz kalırsa, kötüniyet yoksa, markasını hükümsüzlük gerekçesi yapamaz (SMK m. 25/6). Tecavüz talepleri bakımından sessiz kalmanın etkisi **tartışmalı — içtihadı kontrol et**.
- **Mahkeme:** fikri ve sınai haklar hukuk/ceza mahkemesi, yoksa asliye hukuk/ceza (m. 156/1); hak sahibinin davasında yetki davacının yerleşim yeri, fiilin gerçekleştiği ya da etkilerinin görüldüğü yer (m. 156/3). İhtiyati tedbir için tecavüzün ülke içinde gerçekleştiği ya da ciddi ve etkin hazırlık yapıldığı ispat edilmelidir (m. 159/1). Dava şartı arabuluculuğun uygulanıp uygulanmayacağı **tartışmalı — kontrol et**.

## Marka modu

**Hakkın kapsamı.** Koruma tescille doğar (m. 7/1). Marka sahibi izinsiz şu kullanımların önlenmesini isteyebilir (m. 7/2): (a) aynı işaret + tescil kapsamındaki mal/hizmet; (b) aynı/benzer işaret + aynı/benzer mal/hizmet nedeniyle **ilişkilendirilme ihtimali dahil karıştırılma ihtimali**; (c) Türkiye'de ulaştığı tanınmışlık nedeniyle haklı sebep olmaksızın itibardan haksız yarar, itibara zarar ya da ayırt edici karakteri zedeleme — farklı mal/hizmette de. Yasaklanabilecek kullanım biçimleri: mal/ambalaja koyma, piyasaya sürme ve stoklama, ithal/ihraç, iş evrakı ve reklam, internette alan adı/yönlendirici kod/anahtar sözcük, ticaret unvanı/işletme adı, hukuka aykırı karşılaştırmalı reklam (m. 7/3). Tecavüz fiilleri: m. 29/1 (izinsiz kullanım, taklit, taklit olduğunu bilerek ya da bilmesi gerekerek satış/ithal/elde bulundurma, lisans aşımı).

**Karıştırılma etkenleri** — `/arthurlegal:ip-legal-clearance` skill'indeki listeyi yürü (işaret benzerliği ve genel izlenim, mal/hizmet benzerliği, tüketici ve dikkat düzeyi, önceki markanın ayırt edicilik/tanınmışlık derecesi, kanallar, kötüniyet, fiilî karıştırma). Her etken bir bayraktır.

**Tanınmış marka (m. 7/2-c).** Türkiye'deki tanınmışlık düzeyi ispat konusudur; yalnız sektörde bilinme yeterli mi **tartışmalı — içtihadı kontrol et**. Açık değilse "zorlama" diye işaretle.

**Karşılaştırmalı/yanıltıcı reklam.** SMK m. 7/3-f ile birlikte haksız rekabet: kötüleme, gerçek dışı/yanıltıcı açıklama, yanıltıcı ya da tanınmışlıktan gereksiz yararlanan karşılaştırma (TTK m. 55/1-a-1, 2, 5); davalar TTK m. 56. Beyan açıkça yanlış mı, ima yoluyla mı yanıltıcı, yoksa abartılı övgü mü — ayır.

**Tescilsiz işaret.** Tescil yoksa SMK tecavüz davası değil, karıştırılmaya yol açan önlemler nedeniyle haksız rekabet (TTK m. 55/1-a-4) ve önceki hakka dayalı itiraz/hükümsüzlük (SMK m. 6/3, m. 25/1) gündeme gelir.

**Savunmalar ve eşikler (bayrak):**
- Dürüst kullanım: kendi ad/adres, tanımlayıcı açıklama, yedek parça/aksesuar amacının belirtilmesi (m. 7/5).
- Kullanmama def'i: davacının markası 5 yıldır tescilliyse kullanım ispatı istenebilir; süre dava tarihine göre belirlenir (m. 29/2, m. 19/2).
- Hakkın tüketilmesi: hak sahibi ya da izniyle piyasaya sunulan ürünler (m. 152/1) — ürün değiştirilmiş/kötüleştirilmişse istisna (m. 152/2).
- Davalının kendi tescili: önceki tarihli hak sahibinin davasında savunma olarak ileri sürülemez (m. 155).
- Hakların başlangıcı: koruma tescilin yayımından itibaren; başvurunun Bültende yayımından sonraki fiiller için tazminat davası açılabilir ama mahkeme tescil yayımlanmadan karar veremez (m. 7/4).

**Ceza yolu.** İktibas ya da iltibas suretiyle tecavüz kanun metninde hapis ve adli para cezası gerektirir (m. 30/1); markanın Türkiye'de tescilli olması şarttır (m. 30/5); şikâyete bağlıdır (m. 30/6); taklit malın kaynağını bildirip üretenlerin ortaya çıkmasını sağlayan satıcıya ceza verilmez (m. 30/7). Ceza yolunu seçmek `## Enforcement posture` onayı ister.

## Telif modu

Bu skill telif analizini derinleştirmez; FSEK hükümleri bu eklentide başka skill'lerde işlenir. Eleme için şu bayrakları topla, sonra yönlendir:
- Eser niteliği ve sahiplik (yaratan, çalışan/işveren ilişkisi, devir ya da lisans sözleşmesinin yazılılığı ve hakların tek tek sayılıp sayılmadığı).
- Hangi mali/manevi hak etkileniyor; izin ya da sözleşme var mı; kanuni istisna iddiası var mı.
- Erişim + benzerlik delilleri; bağımsız yaratma ihtimali.
- İçerik internette barındırılıyorsa yer sağlayıcı/içerik sağlayıcı ayrımı.

ABD'deki dava için tescil ön şartını ve "fair use" testini Türk davasına taşıma. FSEK maddelerini `tr_mevzuat_madde_getir(number="5846", ...)` ile çek ve yönlendir: internetteki içerik → `/arthurlegal:ip-legal-takedown`; ihtar → `/arthurlegal:ip-legal-cease-desist`; yazılım lisansı/açık kaynak → `/arthurlegal:ip-legal-oss-review`.

## Patent / faydalı model modu

`/arthurlegal:ip-legal-fto-triage` ile aynı çerçeve (istem tablosu, lafzi okuma, m. 89/5 eşdeğerliği, m. 86 dolaylı kullanım), "kendi ürünümüz" yerine "iddia edilen ürün". Ek olarak:
- **Tecavüz fiilleri (m. 141/1):** izinsiz üretim yoluyla taklit; taklit olduğunu bilerek ya da bilmesi gerekerek satış, dağıtım, ithal, ticari amaçla elde bulundurma; usulün izinsiz kullanımı ve usulle doğrudan elde edilen ürünler; lisans aşımı.
- **İspat:** ürün yeniyse patentli usulle elde edildiği kabul edilir, aksini davalı ispatlar; davalının üretim ve işletme sırlarındaki haklı menfaati gözetilir (m. 141/2).
- **Başvuru dönemi:** yayımdan itibaren dava açılabilir; haberdar edilen ya da kötüniyetli tecavüzcü için yayımdan önce de (m. 141/3); mahkeme m. 99/3 ya da /7 yayımından önce karar veremez (m. 141/4).
- **Savunmalar (bayrak):** m. 85/3 istisnaları; önceki kullanım (m. 87); tüketilme (m. 152); hükümsüzlük nedenleri (m. 138) — karşı dava ya da tecavüzün mevcut olmadığının tespiti davasıyla birlikte (m. 154/3); faydalı modelin verilmesi geçerlilik garantisi değildir (m. 143/13).
- **Talepler:** tespit, önleme, durdurma, tazminat, elkoyma, imha, ilan (m. 149/1). Yoksun kalınan kazanç hak sahibinin seçimine göre muhtemel gelir, tecavüzcünün net kazancı ya da makul lisans bedeli üzerinden (m. 151/2); patent sahibi kullanma yükümlülüğünü yerine getirmemişse lisans bedeli yöntemi (m. 151/5). Hesap yapma — bilirkişi işidir.
- **Yabancı ülke:** Almanya `de_norm_getir(kanun="PatG", norm="9")`, Birleşik Krallık `uk_get_section(year="1977", number="37", section="60")`; diğerleri için "ArthurLegal'da kaynak yok".

Çıktı biçimi `fto-triage` ile aynıdır. Dava için tam istem tablosu (dayanak atıfları, bağımlı istemler, yorum bayrakları) uzmanla hazırlanır; ArthurLegal'da ayrı bir istem tablosu skill'i yok.

## Tasarım modu

**İstem tablosu çizme, unsur unsur eşleme yapma.** Tasarım; ürünün ya da parçasının çizgi, şekil, renk, malzeme, doku gibi özelliklerinden kaynaklanan görünümüdür (m. 55/1); tescilli ya da — ilk kez Türkiye'de kamuya sunulmuşsa — tescilsiz korunur (m. 55/4).
- **Ölçüt:** tasarım sahibi, kendi tasarımına kıyasla ayırt edici niteliğe sahip olmayan tasarımlara karşı hak kullanır; değerlendirmede tasarımcının seçenek özgürlüğü dikkate alınır (m. 58/1-2). Ayırt edicilik bilgilenmiş kullanıcının genel izlenimiyle ölçülür (m. 56/5-6). Önceki tasarımlar kalabalıksa koruma alanı daralır — önceki tasarımları iste.
- **Tescilsiz tasarım:** yalnız aynısının ya da genel izlenim itibarıyla ayırt edilemeyecek kadar benzerinin **kopyalanması** önlenebilir; makul yollarla bilemeyen tasarımcının bağımsız tasarımı kopya sayılmaz (m. 59/2). Koruma ilk kamuya sunmadan itibaren 3 yıl (m. 69/2).
- **Koruma dışı:** teknik fonksiyonun zorunlu kıldığı görünüm, başka ürüne mekanik bağlantı için zorunlu biçim/boyut (m. 58/4-b, c). Benzerlik bu özelliklerdeyse işaretle.
- **İstisnalar:** özel ve ticari olmayan, deneme, şartlı eğitim/referans amaçlı fiiller (m. 59/3); birleşik ürüne orijinal görünümünü kazandırmak için onarım parçası, piyasaya ilk sürülmeden itibaren 3 yıl sonra (m. 59/4).
- **Tecavüz fiilleri ve başlangıç:** m. 81/1; tescil yayımlanınca dava, haberdar edilen ya da kötüniyetli için yayımdan önce de (m. 81/2); tescil kaydı ürüne konmamış olsa da tecavüz (m. 81/3).
- **Paralel kanallar:** FSEK koruması saklıdır (m. 58/3) → telif modu; üç boyutlu marka; haksız rekabet (TTK m. 55/1-a-4).

**Malzeme iste:** "Genel izlenim karşılaştırması için (a) tescil belgesindeki tüm görseller ya da tescilsiz tasarımın ilk kamuya sunulduğu görseller ve tarihi, (b) iddia edilen ürünün aynı açılardan fotoğrafları, (c) bildiğiniz önceki tasarımlar gerekli." Görmeden genel izlenim hakkında bayrak dahi verme. İlk geçişin ötesi için tasarım uzmanına yönlendir.

## Ticari sır modu

Dayanaklar dağınıktır; kanunda genel bir ticari sır tanımı ve "makul önlem" ölçütü aranıyorsa `tr_mevzuat_icinde_ara` ile kontrol et — tanım ve önlem eşiği **tartışmalı — içtihadı kontrol et**. Karşılaştırma için AB: `eu_get_document_text(celex="32016L0943")` (Ticari Sırlar Direktifi).

**Sır mı?** Genel olarak bilinmiyor mu; sır olmasından ekonomik değer doğuyor mu; açık unsurların derlemesi mi? Her birini olguya bağla.

**Önlemler (listele, karar verme):** çalışan/yüklenici/karşı taraf gizlilik sözleşmeleri (imzalı, kapsamı, uygulanmış mı); teknik ve fiziksel erişim kısıtları; "gizli" işaretlemesi; çıkış görüşmesi ve iade; politika ve eğitim.

**Hukuka aykırı elde etme / ifşa:**
- Gizlice ve izinsiz ele geçirilen ya da hukuka aykırı öğrenilen bilgileri değerlendirmek ya da bildirmek (TTK m. 55/1-d); emanet edilmiş teklif, hesap, plan gibi iş ürününden yetkisiz yararlanma (m. 55/1-c-1, 2); işçileri işverenin sırlarını ifşaya yöneltmek (m. 55/1-b-3) — yeni işveren riski. Davalar: tespit, men, maddi durumun ortadan kaldırılması, kusur varsa tazminat (TTK m. 56/1).
- İşçi, öğrendiği üretim ve iş sırlarını hizmet süresince kullanamaz, açıklayamaz; işverenin haklı menfaati gerektirdiği ölçüde sonrasında da (TBK m. 396/4).
- Ceza: görev/meslek gereği vakıf olunan ticari sırrı yetkisiz kişilere vermek ya da hukuka aykırı elde edip ifşa etmek, şikâyet üzerine (TCK m. 239/1); fenni keşif, buluş ve sınai uygulama bilgileri dahil (m. 239/2); Türkiye'de oturmayan yabancıya açıklamada ceza artırılır ve şikâyet aranmaz (m. 239/3).
- Buluş söz konusuysa: çalışan hizmet buluşunu serbest buluş niteliği kazanana kadar gizli tutar (SMK m. 114/6) → `/arthurlegal:ip-legal-invention-intake`.

**Eski çalışan senaryosu:** yeni işveren, iş örtüşmesi, ayrılış zamanı, götürülen ve iade edilen belgeler, erişim kayıtları, işe alım kanalı, gizlilik ve buluş devri sözleşmeleri. Rekabet yasağı sorusu → `/arthurlegal:employment-legal-hiring-review` ya da `/arthurlegal:employment-legal-termination-review`. Tersine mühendisliğin hukuka uygun elde etme sayılması **tartışmalı — içtihadı kontrol et**.

## Çıktı (tüm modlar)

Eklenti ayarı `## Outputs` → üst başlık.

```markdown
[ÜST BAŞLIK]

# Tecavüz Elemesi — [Marka | Telif | Patent | Tasarım | Ticari Sır] (TESPİT DEĞİLDİR)

**Bu bir elemedir; tecavüz olduğu ya da olmadığı yönünde tespit değildir.** Sonuç;
olgular, hakkın kapsamı, hukuk ve savunmalar üzerinde avukat takdiri ister.

**Eleme sonucu:** [YEŞİL / SARI / KIRMIZI — tek cümle neden]

## Pozisyon ve kapsam
- **Pozisyon:** [hak sahibi / iddia edilen taraf]  **Hak:** [...]  **Ülke:** [...]
- **Uygulanan çerçeve:** [çekilen maddeler — citation birebir]
- **Saatler:** [zamanaşımı / şikâyet süresi / sessiz kalma — durum]
- **İncelenen deliller:** [liste]

## Etken analizi
[Moda özgü tablo — her etken bayrak + yön; hüküm değil]

## Savunmalar ve eşikler
[Moda özgü: kullanmama def'i / tüketilme / m. 155 / m. 85-87 / hükümsüzlük / tasarım istisnaları / önlem eksikliği / tersine mühendislik]

## Hangi yöne işliyor — özet
| Etken | Bayrak | Yön (hak sahibi / iddia edilen / karışık) |
|---|---|---|

**Sonuç:** *Bu skill sonuç vermez.* Harekete geçmeden avukat takdiri gerekli.
[Hak sahibi lehine işleyen etkenler: ...; iddia edilen taraf lehine: ...]

## Önerilen sonraki adımlar
- [uzman görüşü / `Outside counsel roster`]
- [delil koruma: m. 150/3 belge ibrazı talebi, tespit, noter tespiti — saat işliyorsa]
- [eksik olgu: erişim kayıtları, dosya geçmişi, pazar verisi]
- [`## Enforcement posture` onay zinciri — ileri sürme kararı varsa]

## Atıf doğrulaması
Her madde, karar künyesi, tescil numarası, istem alıntısı ve delil yetkili kaynaktan
açılarak doğrulanır. Atıf: `[ArthurLegal TR — 6769 SMK m. X — GG.AA.YYYY]`.
```

## Avukat olmayan kullanıcı kapısı

`## Who's using this` → rol avukat değilse:

> Bu çıktı bir araştırma elemesidir, hukuki görüş değildir. Yalnız buna dayanarak ihtarname göndermek, durmayı reddetmek, şikâyet ya da dava yoluna gitmek veya "bu serbest kullanım" diye devam etmek hukuki sonuç doğurur: karşı taraf tecavüzün mevcut olmadığının tespitini isteyebilir (SMK m. 154), haksız bir tecavüz iddiası haksız rekabet tartışması doğurabilir (TTK m. 55/1-a-1 — **tartışmalı**), yargılama giderleri aleyhine hüküm verilen taraftan alınır (HMK m. 326/1); iddia edilen tarafsanız durdurma, elkoyma ve tazminat (SMK m. 149) gündeme gelir. Harekete geçmeden bir avukat ya da sicile kayıtlı marka/patent vekili değerlendirmeli.
>
> Götüreceğiniz bir sayfalık özet: hak, pozisyon, olgular ve deliller, bulunan etkenler, işaretlenen savunmalar, işleyen saatler ve sorulacak üç soru. Avukat için bağlı olduğunuz baroya başvurabilirsiniz.

Elemeyi özetle birlikte teslim et.

## Çıktı yeri

Matter aktifse `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/infringe-<mode>-<subject-slug>-YYYY-MM-DD.md`; değilse `~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/infringe-<mode>-<subject-slug>-YYYY-MM-DD.md` (`<mode>`: `trademark` / `copyright` / `patent` / `design` / `trade-secret`). Yolu göster; matter aktifse `history.md`'ye tek satır.

## İleri sürme skill'lerine devir

Eleme ileri sürmeye işaret ediyor ve `## Enforcement posture` destekliyorsa öner — kendiliğinden yazma:

> Bunun için ihtarname taslağı ister misiniz? `/arthurlegal:ip-legal-cease-desist` çalıştırın; bu elemenin bayrak listesini olgusal dayanak yapar, profilinizdeki onay zincirini uygularım — onaylayıcı imzalamadan hiçbir yere gitmez.

İçerik internette barındırılıyorsa: "İçerik kaldırma için `/arthurlegal:ip-legal-takedown`." İleri sürme kararı onaylayıcınındır, elemenin değil.

## Kapanış

`## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu elemeye göre uyarla (ihtar taslağı, eskalasyon, ek olgu, izle ve bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- **Tecavüz var/yok sonucuna varmaz.** Hiçbir zaman.
- Anket, bilirkişi ya da istem yorumunun yerini tutmaz.
- Elemenin ülke kapsamı dışındaki savunmaları değerlendirmez; olgular sınır aşıyorsa yabancı hukuk analizini işaretler, kuralı araçla çeker ya da "kaynak yok" der.
- İhtarname, içerik kaldırma talebi ya da dava dilekçesi yazmaz — bunlar onay zincirine bağlı ayrı skill'lerdir.
- Çıktıyı karşı tarafa aktarmaz.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6769", madde_no=["7","19","25","29","30","55","56","58","59","81"])
tr_mevzuat_madde_getir(number="6769", madde_no=["141","149","150","151","152","154","155","156","157","159"])
tr_mevzuat_madde_getir(number="6102", madde_no=["55","56"])
tr_mevzuat_madde_getir(number="6098", madde_no=["72","396"])
tr_mevzuat_madde_getir(number="5237", madde_no=["73","239"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="marka tecavüz karıştırılma ihtimali tanınmış", kelime_modu="hepsi", date_from="2020-01-01")
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="tasarım genel izlenim bilgilenmiş kullanıcı", kelime_modu="hepsi")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="ticari sır haksız rekabet işçi", kelime_modu="hepsi")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma; seçenekleri say.
