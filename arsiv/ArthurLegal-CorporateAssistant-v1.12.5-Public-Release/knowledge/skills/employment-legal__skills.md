# employment-legal - Skill Referans Kitapcigi

> Değişiklik bildirimi (Apache-2.0 md. 4(b)): Bu kitapçık Anthropic'in `claude-for-legal` deposundaki aynı adlı eklentiden uyarlanmıştır. ArthurLegal tarafından Türk hukuku esas alınarak Türkçe yeniden yazılmıştır (2026-10); yabancı yargı çevreleri için yalnız ArthurLegal MCP araçlarına yönlendirir. Üst kaynak ve sürüm izi: ATTRIBUTION.md.

> Alan: Is hukuku - ise iade, sorusturma, politika
> Toplam skill: 20
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /employment-legal:cold-start-interview (201 satir)
- /employment-legal:customize (58 satir)
- /employment-legal:expansion-kickoff (44 satir)
- /employment-legal:expansion-update (69 satir)
- /employment-legal:handbook-updates (118 satir)
- /employment-legal:hiring-review (149 satir)
- /employment-legal:internal-investigation (345 satir)
- /employment-legal:international-expansion (239 satir)
- /employment-legal:investigation-add (38 satir)
- /employment-legal:investigation-memo (35 satir)
- /employment-legal:investigation-open (35 satir)
- /employment-legal:investigation-query (40 satir)
- /employment-legal:investigation-summary (37 satir)
- /employment-legal:leave-tracker (31 satir)
- /employment-legal:log-leave (68 satir)
- /employment-legal:matter-workspace (160 satir)
- /employment-legal:policy-drafting (130 satir)
- /employment-legal:termination-review (219 satir)
- /employment-legal:wage-hour-qa (122 satir)
- /employment-legal:worker-classification (200 satir)

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
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/legal-research:az-mevzuat` |

Rehberler: `references/eqanun-mcp-rehberi.md` · `references/lex-scholar-rehberi.md` · `references/resourcecontracts-rehberi.md` · `references/karsilastirmali-hukuk-rehberi.md`

---

---

## /employment-legal:cold-start-interview

---
name: cold-start-interview
description: >
  İlk kurulum — iş hukuku pratiğinizi öğrenir: taraf modeli (işveren / işçi / ikisi),
  işyeri ve işçi sayısı haritası (İş K. eşikleri: 30 işçi iş güvencesi, toplu işçi
  çıkarma, 50 işçi engelli kontenjanı), TİS/sendika durumu, işe alım ve fesih tetikleri,
  çıkar çatışması kuralı (Av. K. m. 38), eskalasyon. Personel/disiplin yönetmeliğinden ve
  örnek fesih/savunma belgelerinden öğrenir. İlk kurulumda, CLAUDE.md'de [PLACEHOLDER]
  kaldıysa ya da --redo / --check-integrations ile kullan.
argument-hint: "[--redo | --full | --check-integrations]"
---

# /cold-start-interview

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasına bak. `--check-integrations` verildiyse görüşmeyi atla; yalnız Bölüm 0'daki "Ne bağlı?" kontrolünü çalıştır ve bu yoldaki `## Available integrations` tablosunu yeniden yaz. ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse; yapılandırılmış ama denenmemiş bağlantı ⚪ (tek satır teyit yolu ile). `.mcp.json` beyanına bakarak ✓ verme.
2. Görüşmeyi yürüt (önce Bölüm 0 — rol, pratik ortamı, entegrasyonlar; sonra harita).
3. Örnek belgeler: personel/disiplin yönetmeliği + örnek fesih, savunma ve sözleşme belgeleri.
4. İşyeri/eşik tablosunu ve eskalasyon tablosunu kur.
5. Eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/employment-legal/*/CLAUDE.md`) doldurulmuş (placeholder'sız) bir CLAUDE.md varsa ve ayar yolunda yoksa ayar yoluna kopyala ve kullanıcıya neyin taşındığını söyle.
6. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını yaz; üst klasörleri gerekirse oluştur.

# Kurulum Görüşmesi — İş Hukuku

## Amaç

Türk iş hukukunda doğru cevap çoğu zaman **sayıya ve tarafa** bağlıdır: işyerinde kaç işçi var, aynı işkolunda kaç işyeri var, TİS var mı, hangi tarafı temsil ediyoruz. Bu görüşme haritayı çıkarır ve her skill'in okuyacağı eşik ve eskalasyon tablosunu kurar.

## Kurulum durumu

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`:
- **Yok** → görüşmeye başla.
- **`<!-- SETUP PAUSED AT: -->` içeriyor** → selamla, o bölümden devam etmeyi öner.
- **`[PLACEHOLDER]` var, duraklatma notu yok** → şablon hiç tamamlanmamış; baştan başlamayı ya da placeholder'ların başladığı yerden devam etmeyi öner.
- **Dolu** → kurulmuş; `--redo` yoksa atla.

Bölüm iskeleti `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonundadır. **Bölüm anahtarlarını çevirme:** `## Who's using this`, `## Available integrations`, `## Outputs`, `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` adlarını şablondaki gibi bırak — diğer skill'ler bu anahtarları okur. İçerik Türkçe yazılır.

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/company-profile.md` dosyasına bak.
- **Varsa:** oku ve tek satırla teyit et: "Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [iller/ülkeler]. Doğru mu? (Değiştirmek için 'güncelle' deyin.)" Teyit edilirse ortak soruları atla.
- **Yoksa:** ilk kurulan eklenti budur. Oryantasyondan sonra ortak soruları sor ve paketteki `knowledge/company-profile.md` şablonuna göre yaz: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak."

Ortak profile ait sorular (varsa tekrar sorulmaz): pratik ortamı, büro/şirket adı, sektör, büyüklük, iller ve ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri. Eklentiye özel sorular (taraf modeli, eşik tablosu, tetikler, şablonlar) burada kalır.

## Kurulum kapsamı

Çalışma klasörü kullanıcının ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden belge okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Devam mı, yeniden kurulum mu — onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

Kısa tut (3-4 satır), önce hızlı/tam sor:

> **`employment-legal`** işe alım, fesih, iç soruşturma, izin, politika/yönetmelik, çalışan sınıflandırması ve yurt dışı genişleme işleri içindir.
>
> **2 dakika:** rol, pratik ortamı, taraf modeli, işyeri/işçi sayısı haritası; geri kalanı varsayılan. **15 dakika:** gerçek fesih tetikleri ve yüksek risk bayrakları, örnek belgelerden çıkarım, sözleşme/savunma/fesih şablonları, TİS ve disiplin yönetmeliği, entegrasyonlar.
>
> Hızlı mı, tam mı? (Sonra `/employment-legal:cold-start-interview --full` ile genişletebilirsiniz.)

**Hızlı yol:** yalnız Bölüm 0 ve Bölüm 1; diğer her alana `[DEFAULT]` yaz. Kapanış: "Tamam, komutları kullanabilirsiniz. Fesih risk eşikleri, savunma usulü ve yönetmelik konularında makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanması gereken bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--full`, tek bölüm için `--redo <bölüm>`."

**Seçimden sonra** tek paragraf oryantasyon: "Bu eklenti iş hukuku profilinizi (taraf modeli, işyeri/eşik tablosu, fesih bayrakları, yönetmelik referansları), izin kaydını ve iç soruşturma dosya yapısını tutar. Cevaplarınızı her seferinde okunan düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve yüklediğiniz belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** Yönetmelik, eskalasyon matrisi, işyeri listesi gibi şeyler için önce bağlantı/yapıştırma iste: "Bağlantı ya da belge yapıştırın, ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli.
- **Uzun cevap gerekiyorsa bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste]. Şimdi doldurmak ister misiniz, placeholder olarak mı kalsın?" Sessiz boşluk bırakma; `[LIMITED DATA]` yalnız kullanıcının geçtiği belgeler içindir.
- **Duraklat/devam:** Kullanıcı "dur", "sonra devam" derse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /employment-legal:cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte: "Hoş geldiniz, [bölüm]de kalmıştınız. Devam mı, baştan mı?" Cevaplanmış soruyu tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde numarası, eşik, süre ya da tutar söylerse `tr_mevzuat_madde_getir` ile çek ve karşılaştır. Çelişirse: "[X] dediniz; madde metni [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnek: iş güvencesinde işçi sayısı, işverenin aynı işkolunda birden fazla işyeri varsa bunların toplamına göre belirlenir (İş K. m. 18). Değişen tutarları (kıdem tazminatı tavanı, asgari ücret, idari para cezaları) profile sabit yazma; "güncel tutarı teyit et — dönemsel güncellenir" notu düş.

## Bölüm 0 — Kim kullanıyor, ne bağlı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her fesih notu, yönetmelik taslağı ve soruşturma özetindeki üst başlığı belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan** (stajyer avukat, hukuk asistanı)
> 2. **Avukata erişimi olan, avukat olmayan** (İK, kurucu, yönetici)
> 3. **Düzenli avukat erişimi olmayan**

2 ya da 3 ise bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları hüküm değil, avukatla konuşmanız için araştırma olarak çerçevelerim; (2) hukuki sonucu olan adımlardan önce (fesih, ihtarname, dış merciye cevap, sözleşme imzası) avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım." 3 ise ekle: "Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür, koşullarını baroya sorun."

### Pratik ortamı

> Hangisi size uyuyor? (Her skill'in eskalasyon dilini belirler.)
> - **Hukuk bürosu — işveren tarafı / işçi tarafı / ikisi**
> - **Kurum içi hukuk** (şirketin işveren tarafı)
> - **Tek avukat / küçük büro**
> - **Kamu / adli yardım / klinik**
> - **Hiçbiri** — kendi anlatımınızla yazın, profili ona göre kurarım (kutuya zorlamam; doldurulan, uyarlanan ve boş bırakılan alanları işaretlerim).

Dallanma:
- **Büro (her tür):** `## Matter workspaces` → `Enabled: ✓`, `Cross-matter context: off`. Eskalasyon "onay" değil "danışma" diliyle kurulur; tek avukatta üst kademe yerine "dış meslektaş / sigortacı / eskalasyon yok".
- **İşçi ve işveren tarafı birlikte:** profile `## Çıkar çatışması` bölümü yaz — aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Her yeni matter'da çatışma kontrolünün yapıldığını sor.
- **Kurum içi:** `Enabled: ✗` (tek müvekkil; matter katmanı görünmez).
- **Kamu / klinik:** denetim modeli — işi kim gözden geçirir, müvekkil yazışmasında imza zinciri.

**Eskalasyon sorusu:** "Ekibinizin ortak eskalasyon matrisi ya da yetki devri belgesi varsa onu yapıştırın; temel alırım. Bir inceleme üst onay gerektiren bir şey bulduğunda — ayrımcılık/misilleme riski taşıyan fesih, büyüyen soruşturma, sınırda sınıflandırma, toplu işçi çıkarma, yetkinizi aşan karar — kime gider? İsim ya da rol (ortak, hukuk müşaviri, İK direktörü) ya da 'kendim karar veririm'." `## Practice setting` (ya da `## Who we are`) altına yaz.

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantı farklıdır; karıştırma.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_mevzuat_madde_getir(number="4857", madde_no="18")` ve `tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="işe iade geçerli neden")`. Cevap geldiyse ✓.
- **Yabancı ülke araçları** (`eu_`, `de_`, `uk_` …) — yalnız yurt dışı çalışan/genişleme varsa; önce `status`.
- **İK/bordro sistemi, belge deposu (Google Drive, SharePoint, Box), Slack** — deneyebiliyorsan dene; deneyemiyorsan ⚪.

Rapor:
> - ✓ [Bağlantı] — bağlı (denendi)
> - ⚪ [Bağlantı] — yapılandırılmış, doğrulanmadı; MCP ayarlarınızdan teyit edin
> - ✗ [Bağlantı] — yok; [özellik] [manuel yönteme] düşer. [Nasıl bağlanır.] Sonra bağlarsanız `--check-integrations` çalıştırın.

ArthurLegal MCP ✗ ise: "Her madde ve karar atfı 'doğrulanmadı' işaretlenir ve UYARI satırı taşır."

**Hemen yaz:** `## Who's using this`, `## Available integrations` ve `## Outputs` bölümlerini (şablona göre) profilin ilk bölümünden sonra yaz. `## Outputs` önerisi — avukat: "GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ"; avukat olmayan: "ARAŞTIRMA NOTU — AVUKATLA GÖZDEN GEÇİRİN". Başlığın koruma yaratmadığını not et.

## Bölüm 1 — Harita (2-3 dk)

> **Ne iş yapıyorsunuz?** Şirketseniz: ne satıyorsunuz, kime, nasıl — web sitesi bağlantısı yeter. Büroysanız: işveren müvekkilleriniz hangi sektörlerde, işçi tarafı hacminiz ne?

> İşyeri listeniz var mı (SGK işyeri listesi, İK raporu)? Yapıştırın; yoksa tek tek sorarım. (Bu harita /wage-hour-qa, /worker-classification, /hiring-review, /termination-review ve /policy-drafting'in hepsini besler.)

Liste yoksa:
- İşyerleri (il/ilçe), her birinde işçi sayısı; aynı işkolunda mı?
- TİS var mı, hangi işyerlerinde; işyeri sendika temsilcisi var mı?
- Alt işveren ya da özel istihdam bürosu üzerinden geçici işçi kullanımı?
- Yabancı uyruklu çalışan (çalışma izni), yurt dışında çalışan personel, yakında yurt dışı genişleme planı?
- Kamu işvereni mi?

Büroda bu harita müvekkil bazında `matter.md`'ye yazılır; profile yalnız büronun tipik müvekkil profili girer.

### Eşik tablosu (çekirdek çıktı)

| İşyeri / işveren | İşçi sayısı | Tetiklenen eşikler | TİS / sendika | Otomatik eskalasyon |
|---|---|---|---|---|

Satırları şu doğrulanmış eşiklere göre doldur:
- **30+ işçi** (işverenin aynı işkolundaki işyerlerinin toplamı) → iş güvencesi: en az altı ay kıdemli, belirsiz süreli işçinin feshi geçerli sebebe dayanmalı (İş K. m. 18); işçi fesih bildiriminin tebliğinden itibaren bir ay içinde işe iade için arabulucuya başvurur (m. 20/1).
- **Toplu işçi çıkarma** → 20-100 işçide en az 10, 101-300'de en az yüzde on, 301+'da en az 30 işçinin bir ay içinde çıkarılması; en az otuz gün önceden yazılı bildirim (m. 29).
- **50+ işçi (özel sektör)** → yüzde üç engelli çalıştırma; aynı il sınırlarındaki işyerlerinin toplam işçi sayısına göre (m. 30).
- **İşyeri sendika temsilcisi** → fesih ancak haklı nedenle ve yazılı, açık, kesin gerekçeyle (6356 s. Kanun m. 24).
- **Yabancı çalışan** → çalışma izni olmaksızın çalıştırma yasak (6735 s. Kanun m. 6/2).
- **Her bireysel iş uyuşmazlığı** → alacak, tazminat ve işe iade davalarında arabuluculuk dava şartı; iş kazası ve meslek hastalığı tazminatları hariç (7036 s. Kanun m. 3/1, 3/3).
- **Yurt dışı satırı** → "[Ülke]: ArthurLegal kaynağı `eu_` / `de_` / … — ilk konuda araştır" ya da "ArthurLegal'da kaynak yok — yerel hukukçu görüşü".

Hakkında hiç geçmiş olmayan işyeri için kural uydurma: `[İşyeri: N işçi, geçmiş yok — ilk konuda araştır]`. Liste yüklenmediyse sonunda öner: "Bunu güncelleyebileceğiniz ayrı bir işyeri/eşik tablosu olarak da yazayım mı?"

## Bölüm 2 — Tetikler ve duruşlar (2-3 dk)

> "Duruşlarınızı şimdi kurmak ister misiniz? İnceleme skill'leri (hiring-review, termination-review, policy-drafting) genel varsayım yerine sizin çizginizi bilir. 3-4 dakika. Geçerseniz varsayılan kullanılır ve kurulmamış bir duruşa gelindiğinde söylenir." Ortak playbook, fesih kontrol listesi, sözleşme şablonu varsa önce onu iste.

**İşe alım:** Hukuk hangi sözleşmeyi görür (hepsi / yönetici / rekabet yasağı içeren / hiçbiri)? Standart sözleşmede: süre tipi, deneme süresi, rekabet yasağı, gizlilik, çalışan buluşları ve eser klozları (ilgili SMK/FSEK maddelerini çekmeden yazma).

**Fesih:** Hangi fesihler hukuktan geçer (hepsi / performans / toplu çıkarma / üst yönetici)? Savunma usulü (yazılı istem, süre, tutanak)? İhtar kademesi? İkale (bozma sözleşmesi) ve ibraname pratiği? Arabuluculukta sulh yetkisi kimde?

**Yüksek risk bayrakları** (/termination-review her fesihte bunlara bakar):
- Şikâyet ya da işveren aleyhine idari/adli başvuru sonrası fesih (İş K. m. 18/3-c)
- Hamilelik, doğum, aile yükümlülüğü, sendika üyeliği, cinsiyet, din gibi nedenlerle bağlantı şüphesi (m. 18/3-a, d; m. 5)
- İşyeri sendika temsilcisi (6356 m. 24)
- Hastalık/kaza bekleme süresinde devamsızlık nedeniyle fesih (m. 18/3-f)
- Açık taciz veya mobbing şikâyeti olan çalışan (TBK m. 417)
- Savunma alınmamış davranış nedenli fesih (İş K. m. 19)
- Öğrenmeden itibaren altı iş günü geçmiş haklı fesih (m. 26)
- Sizi daha önce ne yaktı?

Şablon yüklenmediyse sonunda öner: "Bunu İK'nın okuyabileceği ayrı bir fesih kontrol listesi olarak da yazayım mı?"

## Bölüm 3 — Örnek belgeler (3-4 dk)

**Özlük ve izin verisi nerede?** İK/bordro sistemi var mı, hukukun okuma erişimi var mı (SGK e-Bildirge dahil)? Varsa adını yaz; yoksa "manuel" — izin takibi yerel kayıtla çalışır.

> En önemli kısım bu — politikanın ne dediğini değil, ekibin fiilen nasıl çalıştığını görmek istiyorum:
> 1. **Personel/disiplin yönetmeliği ve varsa TİS** — güncel sürüm. (/policy-drafting ve /hiring-review her taslağı bununla karşılaştırır.)
> 2. **Son dönem iş hukuku belgeleri** — 10 iyi taban, 20 daha iyi: fesih bildirimleri, savunma istem yazıları ve tutanakları, ihtarlar, iş sözleşmeleri, ikale/ibraname, arabuluculuk tutanakları, çalışan KVKK aydınlatma metni. Mümkünse kişisel verileri maskeleyerek yükleyin.

10'dan az belgeden kurulan her bölüme `[LIMITED DATA — N belge incelendi]` yaz.

**Yönetmelikten:** disiplin usulü ve savunma süresi, izin kuralları, eksikler (ör. psikolojik taciz politikası yok, uzaktan çalışma kuralı yok). **Belgelerden:** fesih gerekçesi kalıpları, savunma pratiği, sözleşme ve rekabet yasağı dili, sulh/ibraname pratiği, yönetmelik ile fiili uygulama arasındaki fark.

## Profili yazma

Şablona göre yaz; ana bölümler: taraf modeli, çıkar çatışması kuralı (büro), işyeri/eşik tablosu, işe alım ve fesih tetikleri, yüksek risk bayrakları, eskalasyon, `## Matter workspaces`. Kaynak etiketi: `[ArthurLegal TR — 4857 m. X — GG.AA.YYYY]`.

## Yazdıktan sonra

> **Neler yapabildiğimi görmek ister misiniz?**
> - **İş sözleşmesi ve rekabet yasağı incelemesi** — `/employment-legal:hiring-review`
> - **Fesih incelemesi ve risk bayrakları** — savunma, süre, geçerli/haklı neden, arabuluculuk — `/employment-legal:termination-review`
> - **Çalışan sınıflandırması** — işçi / serbest meslek / geçici iş ilişkisi / alt işveren — `/employment-legal:worker-classification`
> - **İşyerine göre ücret ve çalışma süresi sorusu** — `/employment-legal:wage-hour-qa`
> - **Yurt dışı genişleme** — Türkiye'den yurt dışına ya da yabancı işverenin Türkiye'ye girişi — `/employment-legal:expansion-kickoff`
> - **İç soruşturma açma** — `/employment-legal:investigation-open`
>
> **Önerim:** varsayımsal bir fesihte `/employment-legal:termination-review` — risk ayarınızın nasıl okunduğunu en iyi o gösterir. Ya da gündeminizdekini söyleyin.

Kullanıcı görüşmede somut bir iş söylediyse bu listeyi atla. Uygunsa ekle: "Eşik tablonuz hazır; [işyeri] satırını bir kez kontrol edin." · "Yönetmeliğinizde psikolojik taciz politikası yok — taslak ister misiniz?" · "Manuel izin takibi: açık izinleri `/employment-legal:log-leave` ile ekleyin."

**Kapanış:**
> "Tamam. Profiliniz `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasında — düz metin, doğrudan düzenleyebilirsiniz. Tam yeniden görüşme için `--redo`, bağlantı kontrolü için `--check-integrations`, tek değişiklik için `/employment-legal:customize`. En sık ayarlananlar: **işyeri/eşik tablosu** (işçi sayısı değiştikçe), **yüksek risk bayrakları** ve **eskalasyon matrisi**.
>
> **Profiliniz öğrenir.** Bir çıktı yanlış gelirse genellikle ayarlanacak bir duruştur; çıktı hangisi olduğunu söyler. 'Eskalasyon eşiğini şuna çek' demeniz yeterli. On dakikalık kurulum çalışan bir profil verir; bir aylık kullanım sizin yazmış gibi okunan bir profil."

---

## /employment-legal:customize

---
name: customize
description: >
  İş hukuku profilinde tek bir şeyi değiştir — tüm kurulum görüşmesini yeniden
  yapmadan. Taraf modeli, işyeri/eşik tablosu, risk duruşu, eskalasyon kişileri,
  işe alım ve fesih kuralları, yönetmelik duruşları, soruşturma tercihleri ya da
  matter klasörleri. Kullanıcı "şunu değiştir", "işyeri ekle", "profilimi güncelle",
  "ayarlarımı düzenle" ya da "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değişikliğin tarifi]"
---

# /customize

## Ne zaman çalışır

Kullanıcı profilindeki bir şeyi — bir işyeri, risk duruşu, eskalasyon kişisi, yönetmelik duruşu — kurulum görüşmesini baştan yapmadan ve dosyayı elle düzenlemeden değiştirmek istiyor.

## Ne yap

1. **Profili oku.** `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` ve bir üst klasördeki `~/.claude/plugins/config/claude-for-legal/company-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa:
   > Henüz kurulum yapılmamış. Önce `/employment-legal:cold-start-interview` çalıştırın — customize mevcut bir profili ayarlamak içindir.

2. **Haritayı göster** (her biri için tek satır mevcut değer):
   - **Kim olduğumuz** — ad, sektör, pratik ortamı, iller/ülkeler *(tüm eklentilerle ortak — değişiklik `company-profile.md`'e yazılır)*
   - **Taraf modeli** — işveren / işçi / ikisi; çıkar çatışması kuralı ve kontrol adımı
   - **İşyeri/eşik tablosu** — işyerleri, işçi sayıları, tetiklenen eşikler (30 işçi iş güvencesi, toplu işçi çıkarma, 50 işçi engelli kontenjanı), TİS/sendika, yurt dışı satırları
   - **Risk duruşu** — temkinli / orta / atak; fesih risk işaretleme, rekabet yasağı ve sulh yaklaşımına etkisi
   - **Kişiler** — İK muhatapları, dış avukat, eskalasyon zinciri, soruşturma sorumlusu
   - **İşe alım** — sözleşme şablonu, deneme süresi, rekabet yasağı duruşu, gizlilik/buluş klozları
   - **Fesih** — savunma usulü ve süresi, ihtar kademesi, ikale/ibraname, arabuluculukta sulh yetkisi, yüksek risk bayrakları
   - **Yönetmelik** — dosya yolu, TİS, gözden geçirme sıklığı
   - **Soruşturma** — gizlilik başlığı, A/B dosya ayrımı, görüşme açılış bildirimi metni, özet şablonları
   - **İş akışı** — matter workspaces, izin takibi sıklığı, genişleme takip dosyaları
   - **Entegrasyonlar** — ArthurLegal MCP, İK/bordro sistemi, belge deposu, Slack; düşüş yolları

3. **Sor:** "Neyi ayarlayalım? Bir bölüm seçin ya da değişikliği kendi cümlenizle anlatın."

4. **Değişikliği yap.** Mevcut değeri göster, yenisini al, aşağı akış etkisini açıkla, onay al, yaz. Örnekler:
   - *Yeni işyeri, toplam işçi 28 → 34 (aynı işkolu):* "İş güvencesi eşiği aşıldı (İş K. m. 18). `/termination-review` artık her davranış/verim nedenli fesihte geçerli sebep ve savunma (m. 19) kontrolü yapacak ve işe iade riskini hesaba katacak."
   - *Taraf modeli işveren → işveren + işçi:* "Her yeni matter'da çıkar çatışması kontrolü sorulacak (Av. K. m. 38); `Cross-matter context` `off` kalmalı."
   - *Savunma süresi yönetmelikte 3 iş günü → TİS'te 5 iş günü:* "`/investigation-open` ve `/termination-review` savunma istem yazısında TİS süresini kullanacak."
   - *Risk duruşu orta → temkinli:* "Daha çok fesih eskalasyona gider, ikale/ibraname dili daha korumacı olur, rekabet yasağına daha sıkı bakılır."
   - *Yeni ülke (Almanya):* "Eşik tablosuna yurt dışı satırı eklenir; kaynak `de_` araçları (ör. `de_norm_getir(kanun=\"KSchG\", norm=\"1\")`). `/expansion-kickoff Almanya` önerilir."

   Kullanıcı bir madde, eşik ya da süre söylüyorsa yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; değişen tutarları (kıdem tazminatı tavanı, asgari ücret) sabit yazma.

5. **Ortak profil değişiklikleri** (ad, sektör, iller/ülkeler, pratik ortamı) `~/.claude/plugins/config/claude-for-legal/company-profile.md`'e yazılır:
   > Bu değişiklik tüm eklentileri etkiler — iller/ülkeler listesini okuyan her eklenti artık [yeni değer]i görür.

6. **Kapat:** "Tamam. Bir sonraki çıktı bunu yansıtacak. Başka bir şey var mı? `/employment-legal:customize` her zaman çalışır."

## Korkuluklar

- **Bölümü silme.** Bir işyeri "kaldırılmak" istenirse `[Şu an çalışan yok — yeniden açılış için kurallar saklı]` işaretini öner; `[Not configured]` yapmanın o işyerine özgü işaretlemeyi düşüreceğini açıkla.
- **İç tutarsızlığı işaretle.** Ör. "işçi sayısı 30'un altında" + "her fesih işe iade riskiyle değerlendirilsin"; "işveren ve işçi tarafı" + `Cross-matter context: on`; "atak risk duruşu" + "her fesih dış avukata".
- **Güvence kaybını işaretle.** Madde atıflarının `tr_mevzuat_madde_getir` ile doğrulanması, çekilemeyen veride UYARI satırı, kaynak etiketleri ve `[review]` işareti yük taşır — kaldırma; ayarlamadan önce bedelini açıkla.
- **Bölüm anahtarlarını çevirme** (`## Outputs`, `## Matter workspaces`, `Active matter:` vb.) — diğer skill'ler bunları okur.
- **Tek seferde tek değişiklik.** Görüşmeyi baştan sorma.

---

## /employment-legal:expansion-kickoff

---
name: expansion-kickoff
description: >
  Yeni bir ülke için uluslararası genişleme planlamasını başlat — yönü belirler
  (Türkiye'den dışarı / dışarıdan Türkiye'ye), ön bilgiyi toplar, yapı seçeneklerini
  çerçeveler (Türkiye'de İş K. m. 7 sınırları), vergi/finans/İK sorularını taslaklar,
  ArthurLegal MCP ile hedef ülke mevzuatını arar ya da kaynak yoksa yerel avukata
  yönlendirir ve kalıcı takip dosyası oluşturur. "[Ülke]de işe alıyoruz", "[ülke]ye
  genişleme", "[ülke]de ilk çalışan" ya da "yabancı şirket Türkiye'de işe alacak"
  denildiğinde kullan.
argument-hint: "[ülke adı] [yön: disari | turkiye]"
---

# /expansion-kickoff

Yeni bir ülke için genişleme projesini başlatır: yön ve ön bilgi, yapı çerçevesi, paydaş soruları, ülke kaynağı ya da yerel avukat brifi, kalıcı takip dosyası.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → eşik tablosu (yurt dışı satırları), eskalasyon. Matter workspace etkinse aktif matter'ı teyit et.
2. `international-expansion` referans skill'ini yükle ve tüm akışı uygula (Adım 0 yön → Adım 6 çıktı).
3. Takip dosyası yolu: matter workspace kapalıysa `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-<ulke-slug>.yaml`; açıksa aktif matter klasöründe aynı ad. Bu ülke için dosya zaten varsa uyar: "[Ülke] için bir genişleme takip dosyası zaten var. Güncellemek için `/employment-legal:expansion-update [ülke]` kullanın ya da baştan başlamak istediğinizi teyit edin."
4. Hedef ülke ArthurLegal MCP kapsamında değilse (önek tablosunda yoksa) açıkça yaz: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al." Kural uydurma.
5. Türkiye'ye ilişkin her madde atfını yazmadan önce `tr_mevzuat_madde_getir` ile çek; çekilemeyen için UYARI satırı.
6. Bitişte takip dosyasını oluştur ve yolunu göster.

## Örnekler

```
/employment-legal:expansion-kickoff Almanya disari
```

```
/employment-legal:expansion-kickoff Türkiye turkiye
(yabancı ana şirket İstanbul'da ilk iki mühendisi işe alacak)
```

```
/employment-legal:expansion-kickoff
(skill ülkeyi ve yönü soracak)
```

> Yapı çerçevesi, paydaş soruları, ArthurLegal önek tablosu, brif şablonu ve takip dosyası
> şeması `international-expansion` referans skill'indedir — esaslı işe başlamadan önce yükle.

---

## /employment-legal:expansion-update

---
name: expansion-update
description: >
  Süren bir uluslararası genişleme projesinin durumunu güncelle — neyin önünün
  açıldığını yeniden hesaplar, gecikenleri işaretler, sıradaki öncelikleri çıkarır;
  çalışma izni, SGK tescili gibi süreli Türkiye kalemlerini ve yerel avukat brifini
  izler. Son oturumdan bu yana iş ilerlediğinde ve takip dosyası güncel durumu
  yansıtmalıyken kullan.
argument-hint: "[ülke adı]"
---

# /expansion-update

Açık bir genişleme takip dosyasına döner ve son oturumdan bu yana olanlara göre kalemleri günceller: önü açılanlar, gecikenler, sıradaki öncelikler.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını yükle; matter workspace etkinse aktif matter'ı teyit et.

2. Takip dosyasını bul: `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-<ulke-slug>.yaml` (matter workspace açıksa aktif matter klasöründe). Yoksa: "[Ülke] için genişleme takip dosyası yok. Başlatmak için `/employment-legal:expansion-kickoff [ülke]` çalıştırın." Birden fazla dosya varsa ve ülke verilmediyse hangisi olduğunu sor.

3. Dosyayı oku ve durumu göster:

```
[Ülke] genişlemesi ([yön]) — son güncelleme [tarih]
Açık: [N] | Devam: [N] | Tamam: [N] | Blokeli: [N]

Sıradaki öncelikler (en yakın son tarih ya da en çok kalemi bekleten):
  [kalem] — sahibi: [sahip]
  [kalem] — sahibi: [sahip]
  [kalem] — sahibi: [sahip]
```

4. Güncellemeleri **tek seferde** iste — kalem kalem sorma:

   > Son baktığımızdan beri neler ilerledi? Değişenleri söyleyin (ör. "yapı kararı verildi — İstanbul'da şirket kuruluyor", "yerel avukat tutuldu, perşembe görüşme", "çalışma izni başvurusu yapıldı", "işyeri riski analizi vergide bekliyor"). Yeni kalem ekleyebilir, son tarih değiştirebilirsiniz.

5. Güncellemeleri dosyaya uygula. `tamam` olan her kalem için `bagimli_oldugu` alanında onu bekleyen kalemleri bul ve "artık yapılabilir" diye işaretle. Örnek bağımlılıklar: şirket kuruluşu → SGK işyeri bildirgesi (5510 m. 11) → işe giriş bildirgeleri (5510 m. 8); çalışma izni (6735 m. 6) → yabancı çalışanın başlangıç tarihi; yerel avukat brifinin cevabı → yerel sözleşme taslağı.

6. Son tarihi geçmiş ve hâlâ `acik` ya da `devam` olan kalemleri işaretle:

```
⚠️ Gecikti: [kalem] — son tarih [tarih], sahibi: [sahip]
```

   Türkiye kalemlerinde kanuni süreyi kaçırma riski varsa (ör. işyeri bildirgesi en geç sigortalı çalıştırmaya başlanan tarihte, işe giriş bildirgesi sigortalılık başlangıcından önce) 🔴 ile ayrıca işaretle ve eskalasyon tablosundaki kişiye bildirmeyi öner.

7. Yeni bir yasal dayanak girilecekse yazmadan önce doğrula: Türkiye maddesi için `tr_mevzuat_madde_getir`; yabancı ülke için ilgili ArthurLegal aracı (kaynak yoksa "yerel hukukçu görüşü"). Yerel avukat cevabı geldiyse kaleme özetini ve atıflarını işle; tarihini `dayanak` alanına yaz.

8. Dosyayı yaz ve teyit et:

```
Takip dosyası güncellendi — [N] kalem kapandı, [N] açık.
Sıradaki öncelik: [en üstteki açık kalem].
```

## Örnekler

```
/employment-legal:expansion-update Almanya
```

```
/employment-legal:expansion-update
(birden fazla takip dosyası varsa ülkeyi sorar)
```

> Takip dosyası şeması, durum kuralları ve bağımlılık mantığı `international-expansion`
> referans skill'indedir — esaslı işe başlamadan önce yükle.

---

## /employment-legal:handbook-updates

---
name: handbook-updates
description: >
  Personel yönetmeliği / çalışan el kitabı değişikliğini mevcut sürümle
  karşılaştırır; çapraz atıf kırılmalarını, ülke/işyeri/TİS eklerine etkisini
  ve işçi aleyhine esaslı değişiklik riskini (İş K. m. 22: yazılı bildirim, 6
  iş günü içinde yazılı kabul, geçmişe etkisizlik) işaretler. "El kitabını
  güncelle", "bunu yönetmeliğe ekle", "personel yönetmeliği değişikliği"
  denince ya da yerleştirilmeye hazır bir politika olduğunda kullan.
---

# /handbook-updates — Personel Yönetmeliği Güncellemesi

El kitabı değişikliğinin dalga etkisi vardır: yıllık izin bölümünü değiştirirsin, fesihteki izin ücreti hesabı, izin politikası atfı ve iki işyeri eki etkilenir. Türk hukukunda bir de m. 22 boyutu vardır: personel yönetmeliği iş sözleşmesinin eki niteliğinde olabilir ve işçi aleyhine esaslı değişiklik tek taraflı yapılamaz. Bu skill dalgaları tutarsızlığa dönüşmeden bulur.

## Bağlamı yükle

`company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → el kitabı/personel yönetmeliği yeri, ekler listesi (ülke/işyeri/TİS), güncelleme sıklığı.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/employment-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Değişikliği al

- Hangi bölüm değişiyor? Yeni metin ne?
- Neden: kanuni zorunluluk (hangi madde, hangi değişiklik), şirket kararı, temizlik?
- Kimlere uygulanacak; yürürlük tarihi ne?

### 2. Mevcutla karşılaştır

```diff
- [eski metin]
+ [yeni metin]
```

Değişiklik bir kanun değişikliğine dayanıyorsa ilgili maddeyi `tr_mevzuat_madde_getir` ile çek ve madde metnindeki değişiklik notunu (tarih, değiştiren kanun) yaz. Örnek: analık izni ve babalık izni süreleri 2026'da değişti (4857 m. 74 ve ek m. 2'deki değişiklik notları) — eski sürelerle kalmış bölümleri ara.

### 3. Çapraz atıfları bul

- Bu bölüme atıf yapan diğer politikalar ("izin süreleri için bkz. ...")
- Bu bölümün tanımladığı ya da kullandığı tanımlı terimler
- Bu bölümü değiştiren ekler
- İş sözleşmesi şablonu ve teklif mektubu şablonundaki atıflar

Her atıf değişiklikten sonra hâlâ doğru mu? Kırılanı işaretle.

### 4. Eklere etkisi

Eklenti ayarındaki her ülke/işyeri/TİS eki için:
- Ek, değişen bölümü değiştiriyor mu?
- Değişiklik eki eskitiyor, yanlış ya da eksik bırakıyor mu?
- Daha önce ek gerektirmeyen bir yerde yeni ek gerekiyor mu? (Türkiye dışı ülke için kural ezberden yazılmaz; ilgili önekle ara: `eu_`, `uk_`, `de_`, `nl_`, `az_` …; listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al.")
- TİS'li işyerinde yeni metin TİS hükmüyle çatışıyor mu?

### 5. Söz kontrolü — İş K. m. 22

Değişiklik eski sürümün verdiği bir şeyi azaltıyor mu?

- Personel yönetmeliği, iş sözleşmesi ya da işyeri uygulamasıyla oluşan çalışma koşullarında **esaslı değişiklik** ancak işçiye **yazılı bildirimle** yapılabilir; işçi **6 iş günü** içinde yazılı kabul etmezse değişiklik onu bağlamaz (m. 22/1).
- Kabul edilmezse işveren, değişikliğin geçerli nedene dayandığını ya da başka geçerli fesih nedeni olduğunu yazılı açıklayıp bildirim süresine uyarak feshedebilir; işçi m. 17–21'e göre dava açabilir (m. 22/1).
- Taraflar anlaşarak her zaman değiştirebilir; değişiklik **geçmişe etkili** yürürlüğe konamaz (m. 22/2).
- Neyin "esaslı" sayıldığı ve işyeri uygulamasının ne zaman çalışma koşulu hâline geldiği **tartışmalı — içtihadı kontrol et**.
- İşçi lehine değişiklikler ve salt düzenleme/talimat niteliğindeki kurallar (TBK m. 399) için yazılı kabul gerekmez; yine de duyuru ve imza kaydı tut.

Engelleme; ama işaretle ve hangi çalışan grubunun yazılı kabulünün gerektiğini yaz.

### 6. Yan yükümlülükler

- **KVKK:** değişiklik yeni bir kişisel veri işlemesi getiriyorsa aydınlatma metni güncellenir (6698 m. 10).
- **İSG:** risk ya da çalışma yöntemi değişiyorsa çalışanlar bilgilendirilir, gerekiyorsa eğitim yenilenir (6331 m. 16, m. 17).

### 7. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="4857", madde_no="22")
tr_mevzuat_madde_getir(number="6098", madde_no="399")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="işyeri uygulaması çalışma koşulu esaslı değişiklik", date_from="2022-01-01")
```

Atıf etiketleri: `[ArthurLegal TR — 4857 m. 22 — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`.

## Çıktı

```markdown
## El Kitabı Güncellemesi: [Bölüm adı]

### Değişiklik
[diff]

### Çapraz atıf etkisi
| Bölüm | Değişen bölüme atıf | Hâlâ doğru mu? | Gereken düzeltme |
|---|---|---|---|
| [ad] | [nasıl] | ✅/⚠️ | [ne] |

### Ek etkisi
| Ülke / işyeri / TİS | Mevcut ek | Değişiklikten sonra | Eylem |
|---|---|---|---|
| [ad] | [ne diyor] | [geçerli / eskidi / güncellenmeli] | [yok / güncelle / yeni ek] |

### m. 22 söz kontrolü
[Aleyhe esaslı değişiklik yok / var → yazılı bildirim + 6 iş günü yazılı kabul gereken grup; geçmişe etki yok]

### Yayına hazır
- [ ] Çapraz atıflar güncellendi
- [ ] Ekler güncellendi
- [ ] [Aleyhe değişiklikse: yazılı bildirim gönderildi, kabul/ret kayıtları toplandı]
- [ ] Yürürlük tarihi ileriye dönük
- [ ] KVKK aydınlatma / İSG bilgilendirmesi (gerekiyorsa)
- [ ] Sürüm numarası ve tarih güncellendi
- [ ] Tebliğ ve imza kaydı
```

## Bu skill ne yapmaz

- Değişikliği onaylamaz; İK/hukuk yönetimi onaylar.
- Çalışanlara duyurmaz.
- Kabul/imza takibini yürütmez.

---

## /employment-legal:hiring-review

---
name: hiring-review
description: >
  İş teklifi ve iş sözleşmesi incelemesi (Türk hukuku) — sözleşme türü ve
  şekli, deneme süresi, ücret ve çalışma süresi hükümleri, rekabet yasağı
  (TBK m. 444-447), gizlilik ve ceza koşulu, işe alımda ayrımcılık yasağı,
  aday verisinin KVKK uyumu, işe giriş zorunlulukları (SGK bildirimi, yabancı
  çalışma izni, engelli kotası). "Bu teklifi incele", "rekabet yasağı koyabilir
  miyiz", "iş sözleşmesine bak", "yurt dışından işe alım" denince ya da teklif
  eklendiğinde kullan.
argument-hint: "[teklif mektubu / iş sözleşmesi dosyası ya da işe alımı anlatın]"
---

# /hiring-review — İşe Alım İncelemesi

Teklif mektupları çoğunlukla kalıptır; ta ki olmayana kadar. Değer üreten yerler sözleşme türü/şekli, rekabet yasağı ve işe alım sürecinin ayrımcılık + kişisel veri boyutudur. Kural ezberden söylenmez; her madde `tr_mevzuat_madde_getir` ile çekilir.

## Destination check

- **Müvekkile / İK'ya inceleme notu** → profil `## Outputs` başlığı
- **Adaya gidecek teklif / sözleşme** → yalnız temiz metin; iç yorumlar, risk notları ve pazarlık pozisyonu çıkarılır
- **İlan metni** → ayrımcılık kontrolünden geçmiş, aday aydınlatma metniyle birlikte

## Bağlamı yükle

`company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → ayak izi, işe alım inceleme tetikleyicileri, rekabet yasağı politikası, teklif şablonu yeri, `## Outputs`, `## Who's using this`.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/employment-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Yer ve uygulanacak hukuk

İş nerede yapılacak — merkezin değil, kişinin bulunduğu yer. Türkiye dışında ise: tarafların seçtiği hukuk, işçinin mutad işyeri hukukunun emredici asgari koruması saklı kalmak üzere uygulanır (MÖHUK 5718 m. 27). Yabancı ülke kuralı ezberden yazılmaz: İngiltere `uk_search_legislation(query="Employment Rights Act 1996")`, Almanya `de_gesetz_ara`, Hollanda `nl_search_legislation`, İrlanda `ie_search_acts`, AB `eu_search_eu_law(query="transparent and predictable working conditions")`, Azerbaycan `az_search_acts(query="Əmək Məcəlləsi", types=[107])`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al." Ayak izinde olmayan yeni bir ülke ise işaretle: "Bu ülkede ilk işe alım; teklif gitmeden önce araştırma gerekli."

### 2. Sözleşme türü ve şekli (4857 s.K.)

| Kontrol | Kural (metinden doğrula) | Çıpa |
|---|---|---|
| Şekil | Süresi 1 yıl ve daha fazla sözleşme yazılı; yazılı sözleşme yoksa en geç 2 ay içinde çalışma koşullarını gösteren yazılı belge | m. 8/2-3 |
| Belirli süre | Objektif koşul + yazılı; esaslı neden olmadan zincirleme yapılamaz | m. 11 |
| Kısmi / çağrı üzerine / uzaktan | Ayrımcılık yasağı, orantılı ödeme; çağrı ve uzaktan çalışmada yazılı sözleşme ve zorunlu içerik | m. 13, m. 14 |
| Deneme süresi | En çok 2 ay (TİS ile 4 aya kadar); bu sürede bildirimsiz ve tazminatsız fesih | m. 15 |
| Bağımsız çalışan mı? | Olgular bağımlılık gösteriyorsa iş sözleşmesidir | → `/employment-legal:worker-classification` |

**ABD'deki "at-will" kavramı Türk hukukunda yoktur.** Türk teklifine "her an sebepsiz feshedilebilir" dili ekleme: bildirim süreleri asgaridir ve yalnız işçi lehine artırılabilir (m. 17), 30+ işçili işyerinde 6 aydan sonra iş güvencesi vardır (m. 18). Yerine bildirim süresi, deneme süresi ve fesih hükümlerinin kanuna uygunluğunu kontrol et.

### 3. Ücret ve çalışma süresi hükümleri

- Ücret brüt mü net mi açık; asgari ücretin altında değil (m. 39 — güncel tutarı teyit et).
- Haftalık süre ve dağılımı (m. 63); fazla çalışma için işçi onayı (m. 41).
- "Fazla çalışma ücrete dahildir" klozu: kapsamı ve sınırı **tartışmalı — içtihadı kontrol et** → `/employment-legal:wage-hour-qa`.
- Prim/ikramiye: takdirî mi, kazanılmış hak mı açıkça yazılmalı; belirsizlik işçi lehine yorumlanma riski taşır (yerleşik uygulama — kontrol et).
- Yıllık izin süresi kanuni asgarinin altında olamaz (m. 53).

### 4. Rekabet yasağı, gizlilik, ceza koşulu

Teklif rekabet yasağı, müşteri/çalışan ayartmama, gizlilik ya da fikri hak devri içeriyorsa:

| Kontrol | Kural | Çıpa |
|---|---|---|
| Şekil ve ehliyet | Fiil ehliyetine sahip işçi, **yazılı** olarak üstlenir | TBK m. 444/1 |
| Geçerlilik şartı | İş ilişkisi müşteri çevresi ya da üretim sırları / işverenin işleri hakkında bilgi edinme imkânı veriyor **ve** bu bilginin kullanılması işverene önemli zarar verebilecek nitelikte | TBK m. 444/2 |
| Sınır | Yer, zaman ve iş türü bakımından işçinin ekonomik geleceğini hakkaniyete aykırı tehlikeye düşürmeyecek; süre özel durumlar dışında **2 yılı aşamaz**; hâkim aşırı yasağı sınırlayabilir, işverenin karşı edimini dikkate alır | TBK m. 445 |
| Aykırılığın sonucu | Zararın tazmini; ceza koşulu varsa işçi ödeyerek kurtulabilir (aksi kararlaştırılmadıkça); yasağa son verilmesi ancak yazılı olarak açıkça saklı tutulmuşsa | TBK m. 446 |
| Sona erme | İşverenin gerçek yararı kalmazsa; işveren haklı sebep olmaksızın feshederse ya da işçi işverene yüklenebilen nedenle feshederse | TBK m. 447 |
| Ceza koşulu | Hizmet sözleşmesine yalnız işçi aleyhine konan ceza koşulu geçersiz | TBK m. 420/1 |

TBK m. 420/1 ile m. 446/2 arasındaki ilişki (rekabet yasağına bağlanan tek taraflı ceza koşulunun geçerliliği) **tartışmalı — içtihadı kontrol et**. Profilin rekabet yasağı politikasını önce uygula (bu işe alıma yasak gerekiyor mu?), sonra kanuni sınırları. Çalışan buluşu ve fikri hak klozları için profilin "Çalışan buluşları ve fikri haklar klozları" bölümünü uygula; kloza yazılacak her madde ayrıca çekilir.

### 5. İşe alım süreci: ayrımcılık ve aday verisi

- **Eşit davranma (4857 m. 5):** dil, ırk, renk, cinsiyet, engellilik, siyasi düşünce, felsefi inanç, din, mezhep ve benzeri sebeplerle ayrım yasak; sözleşmenin yapılmasında cinsiyet ya da gebelik nedeniyle farklı işlem yasak (biyolojik/işin niteliği zorunlulukları hariç).
- **TİHEK (6701 m. 3, m. 6):** iş ilanı, başvuru, seçim kriterleri ve işe alım şartları dahil tüm süreçlerde ayrımcılık yasağı; başvuru gebelik, annelik ve çocuk bakımı gerekçesiyle reddedilemez (m. 6/3); yaş ve sağlık durumu da korunan temellerdendir (m. 3/2). İlan metnini bu gözle oku.
- **KVKK (6698):** aday verisi ilkelere uygun işlenir — amaçla bağlantılı, sınırlı, ölçülü, gerekli süre kadar saklanır (m. 4/2); hukuki sebep çoğunlukla sözleşmenin kurulmasıyla doğrudan ilgili işleme (m. 5/2-c) ya da açık rıza (m. 5/1); sağlık ve ceza mahkûmiyeti verisi özel niteliklidir (m. 6/1), ancak m. 6/3'teki hâllerde (ör. istihdam ve İSG alanındaki hukuki yükümlülük, m. 6/3-f) işlenir; veri elde edilirken aydınlatma (m. 10). Referans araması, sosyal medya taraması, sabıka kaydı talebi → hukuki sebep ve ölçülülük testi; gerekirse `/privacy-legal:use-case-triage`.

### 6. İşe giriş zorunlulukları

| Zorunluluk | Kural | Çıpa |
|---|---|---|
| SGK işe giriş bildirgesi | Sigortalılık başlangıcından **önce** (inşaat, balıkçılık, tarımda en geç çalışmaya başlatıldığı gün) | 5510 m. 8/1 |
| Yabancı işçi | Çalışma izni olmadan çalışmak ve çalıştırmak yasak (kanun/anlaşma istisnaları saklı) | 6735 m. 6/2-3 |
| Engelli istihdamı | 50+ işçili özel sektör işyerinde %3 engelli işçi; aynı ildeki işyerleri toplanır | 4857 m. 30/1 |
| İSG eğitimi | İşe başlamadan önce; tehlikeli/çok tehlikeli işlerde mesleki eğitim belgesi olmayan çalıştırılamaz | 6331 m. 17/1, 17/3 |
| Kişisel veri | Çalışan aydınlatma metni | 6698 m. 10 |

Tutar içeren yükümlülükler (idari para cezaları, kota cezası) dönemsel güncellenir → güncel tutarı teyit et.

### 7. Teklif / sözleşme metni

- Başlama tarihi, unvan, görev tanımı, çalışma yeri, ücret (brüt/net), ödeme dönemi, çalışma süresi — yazılı belgede bulunması gereken unsurlarla karşılaştır (m. 8/3).
- Koşullar (sağlık raporu, referans, diploma, çalışma izni) açık ve KVKK'ya uygun.
- Bildirim süreleri kanuni asgarinin altında değil (m. 17); deneme süresi m. 15'e uygun.
- Personel yönetmeliğine atıf varsa → yönetmelik iş sözleşmesinin eki niteliğinde; sonraki aleyhe değişiklikler m. 22 rejimine tabidir (`/employment-legal:handbook-updates`).
- Hak ve yükümlülükleri tek metinde toplayan bütünlük hükmü.

### 8. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["420","444","445","446","447"])
tr_mevzuat_madde_getir(number="4857", madde_no=["5","8","11","15","30"])
tr_mevzuat_madde_getir(number="6698", madde_no=["4","5","6","10"])
tr_kurum_karari_ara(kurum="kvkk", query="işe alım aday kişisel veri")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="rekabet yasağı cezai şart işçi aleyhine", date_from="2022-01-01")
```

Sonuç azsa sessizce doldurma; seçenekleri sun (sorguyu genişlet / başka araç / `[web — doğrula]` / dur). Atıf etiketleri: `[ArthurLegal TR — 6098 m. 444 — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`.

## Çıktı

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# İşe Alım İncelemesi: [Aday takma adı] — [Pozisyon] — [Yer]

## ⚠️ İnceleyen notu
- **Genel:** [Gönderilebilir / Değişiklik gerekli / Eskalasyon]
- **Uygulanacak hukuk:** [Türk hukuku / seçim + mutad işyeri — gerekçe]
- **Kaynaklar:** [çekilen maddeler; doğrulanamayan]
- **Tartışmalı noktalar:** [liste]

## Sözleşme türü ve şekli
## Ücret ve çalışma süresi
## Rekabet yasağı / gizlilik / ceza koşulu
[Geçerlilik değerlendirmesi, önerilen metin değişiklikleri]
## Ayrımcılık ve aday verisi
## İşe giriş zorunlulukları
## Metin sorunları

### Yapılacaklar
- [ ] [göndermeden önce somut değişiklik]
```

## Sonuç doğuran işlem kapısı (teklif gönderme)

"Gönderilebilir" önerisinden ya da imzaya hazır metinden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> Teklif bir sözleşmedir; rekabet yasağı, sözleşme türü ve zorunlu işlemler gönderildikten sonra kolay düzeltilmez. Bu teklifi bir avukatla incelediniz mi? Hayırsa götüreceğiniz özet: aday, pozisyon, işin yapılacağı yer; sözleşme türü ve gerekçesi; rekabet yasağı ve geçerlilik analizi; ayrımcılık/KVKK bulguları; işe giriş zorunlulukları; açık sorular; ters gidebilecek şey (geçersiz rekabet yasağı, belirsiz süreli sayılma, eksik SGK bildirimi, izinsiz yabancı çalıştırma); sorulacaklar. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan "Gönderilebilir" yazma; "TASLAK" işaretli inceleme serbest.

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; seçimi avukat yapar.

## Bu skill ne yapmaz

- Teklifi yazmaz; inceler.
- İşe alım kararını vermez.
- Rekabet yasağı ya da başka bir kuralı ezberden söylemez.
- Yeni bir ülkeyi derinlemesine kendisi araştırmaz; araştırma gerektiğini işaretler ve `wage-hour-qa` ya da yerel hukukçuya yönlendirir.

---

## /employment-legal:internal-investigation

---
name: internal-investigation
description: >
  Referans: iç soruşturmanın açılıştan nihai nota kadar yönetimi — soruşturma kaydı,
  belge taraması ("iğne bulma"), kaynak kapsama takibi, kayda karşı soru-cevap,
  soruşturma notu ve hedef kitle özetleri. Türk hukuku kontrol noktaları: savunma
  (İş K. m. 19), altı iş günlük hak düşürücü süre (m. 26), KVKK ölçülülüğü, avukatın
  sır saklama yükümlülüğü (Av. K. m. 36). /investigation-open, -add, -query, -memo ve
  -summary tarafından yüklenir; doğrudan çağrılmaz.
user-invocable: false
---

# İç Soruşturma — Ortak Çerçeve

## Matter bağlamı

Uygulama CLAUDE.md'sinde `## Matter workspaces` bölümüne bak. `Enabled` `✗` ise (kurum içi kullanımda varsayılan) bu paragrafın gerisini atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/employment-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

**Soruşturma klasörü (`<SORUŞTURMA>`):** matter workspace kapalıysa `~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-<slug>/`; açıksa `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/investigation-<slug>/`.

## Bağlam ve üst başlık

- `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → eskalasyon tablosu, soruşturma protokolü, taraf rolü ([ŞİRKET ADI] işveren mi), `## Who's using this`, `## Outputs`.
- `~/.claude/plugins/config/claude-for-legal/company-profile.md` → büro/şirket bilgisi.
- Her dosya (kayıt, not, özet) `## Outputs` bölümündeki üst başlıkla açılır; başlık kullanıcı rolüne göre değişir.

## ⚠️ Gizlilik — Türk hukukunda "privileged investigation" yok

ABD'deki attorney-client privilege ve work product doktrininin Türk hukukunda birebir karşılığı yoktur. Koruma üç ayrı ve sınırlı dayanaktan gelir:

| Dayanak | Ne korur | Ne korumaz |
|---|---|---|
| Av. K. m. 36 — avukat görevi dolayısıyla öğrendiklerini açığa vuramaz; tanıklığı iş sahibinin muvafakatine bağlıdır, muvafakat olsa da çekinebilir | Avukatın notları, değerlendirmesi, müvekkilden öğrendikleri | Avukat olmayan İK/yöneticinin tuttuğu notlar; sonradan avukata gönderilmesi onları korumaz |
| İş K. m. 75/2 — işveren işçi hakkında edindiği bilgiyi dürüstlük kuralına ve hukuka uygun kullanır, gizli kalmasında işçinin haklı çıkarı olanı açıklamaz | Özlük ve soruşturma bilgisinin gereksiz paylaşımı | İşverenin bu bilgiyi kendi davasında delil olarak sunması |
| KVKK m. 12 — veri güvenliği; öğrenilen veriyi açıklamama, amaç dışı kullanmama | Erişim, saklama, sızıntıya karşı önlem | — |

**Sonuç — dosyayı ikiye ayır** (her girdide `dosya_sinifi` alanı):
- **A — avukat çalışma ürünü** (`avukat-calisma-urunu`): avukat notları, güvenilirlik değerlendirmesi, hukuki risk analizi, soruşturma notu. Yalnız avukat ve soruşturma ekibi görür.
- **B — işveren delil dosyası** (`isveren-delil`): savunma istem yazısı, savunma tutanağı, tanık tutanakları, olay tutanağı, fesih bildirimi taslağı. **İşe iade ya da alacak davasında mahkemeye sunulacağı varsayımıyla** tarafsız ve olgusal dil; avukat görüşü ve risk yorumu bu belgelere girmez.

Başlık koymak koruma yaratmaz. Soruşturmayı İK yürütüyor, avukat yalnız danışmansa A sınıfı daralır — dosya açılmadan avukata sor; emin değilsen "tartışmalı — avukat karar versin" diye işaretle.

**Dağıtım disiplini:** Dosyaları soruşturma ekibi dışına (İK geneli, iş birimi, CC zincirleri) gönderme; her dağıtımı bilinçli karar olarak kayda geçir. Kişisel veriyi amaçla bağlantılı, sınırlı ve ölçülü işle, gerekli süre kadar tut (KVKK m. 4/2).

## Amaç

İç soruşturma iki yerden çöker: **kapsama boşluğu** (hiç toplanmamış kaynak) ve **sentez boşluğu** (toplanmış ama bağlanmamış delil). Türk hukukunda üçüncüsü **süre ve usuldür**: savunma alınmadan ya da hak düşürücü süre geçtikten sonra yapılan fesih, sağlam bulguyu boşa çıkarır. Bu skill kaynakları izler, belge yığınını avukatı boğmadan tarar ve her an nota dönüştürülebilecek bir kayıt tutar.

## ⏰ ÖN-KONTROL — Süre ve usul (her modda ilk iş)

1. **Hak düşürücü süre — İş K. m. 26:** Ahlak ve iyi niyet kurallarına aykırılığa (m. 24/II, m. 25/II) dayalı derhal fesih yetkisi, karşı tarafın öğrendiği günden itibaren **altı iş günü** ve her hâlde fiilden itibaren **bir yıl** geçtikten sonra kullanılamaz; işçi olayda maddi çıkar sağladıysa bir yıllık süre uygulanmaz.
   - Kayda öğrenme tarihini ve **kimin** öğrendiğini yaz. Tüzel kişi işverende sürenin fesih yetkisi olan kişi ya da organın öğrenmesiyle, soruşturma gerekiyorsa sonucun ona sunulmasıyla başladığı **yerleşik uygulamadır — tartışmalı, içtihadı kontrol et**:
     `tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="altı iş günlük hak düşürücü süre soruşturma öğrenme", date_from="2020-01-01")`
   - Kalan ≤ 2 iş günü → 🔴 ACİL; avukata hemen bildir.
2. **Savunma — İş K. m. 19:** Fesih bildirimi yazılı yapılır, sebep açık ve kesin belirtilir. Belirsiz süreli sözleşme, işçinin davranışı veya verimiyle ilgili nedenle, iddialara karşı savunması alınmadan feshedilemez; m. 25/II'ye uygun fesih hakkı saklıdır. m. 25/II'ye dayanılacak olsa da savunma almak ispat bakımından güvenlidir (yerleşik uygulama). Savunma istem yazısı somut iddia, tarih ve süre içerir; kanunda süre yoktur, TİS/yönetmelik süresine uy — **tartışmalı, içtihadı kontrol et**.
3. **TİS / disiplin yönetmeliği:** Disiplin kurulu veya özel usul varsa ona uy. İşyeri sendika temsilcisinin sözleşmesi haklı neden olmadıkça ve nedeni yazılı, açık ve kesin belirtilmedikçe feshedilemez; temsilci ya da sendikası bir ay içinde dava açabilir (6356 s. Kanun m. 24).
4. **İspat yükü:** İşe iade davasında feshin geçerli sebebe dayandığını işveren ispatlar (İş K. m. 20/2). Ayrımcılık iddiasında işçi ihlal ihtimalini güçlü biçimde gösterirse yük işverene geçer (m. 5 son fıkra). Kaydı bu yükü taşıyacak biçimde tut.

## KVKK ve delil kontrolü — e-posta, cihaz, kamera, log

Çalışanın e-postası, mesajları, cihazı, kamera kaydı veya sistem logu incelenmeden önce sırayla sor; cevabı kayda `kvkk_kontrol` olarak yaz:

1. **Önceden aydınlatma:** Kurumsal hesap/cihazların denetlenebileceği çalışana önceden bildirildi mi (KVKK m. 10 — amaç, aktarım, yöntem, hukuki sebep, haklar)? Politika metnini iste.
2. **Hukuki sebep — KVKK m. 5/2:** özellikle (ç) hukuki yükümlülük, (e) bir hakkın tesisi, kullanılması veya korunması, (f) ilgili kişinin temel hak ve özgürlüklerine zarar vermemek kaydıyla meşru menfaat. Sağlık, cinsel hayat, sendika üyeliği gibi özel nitelikli veri (m. 6/1) çıkarsa m. 6/3'teki dar şartlar ve Kurulun belirlediği yeterli önlemler (m. 6/4) gerekir.
3. **Ölçülülük — m. 4/2-ç:** yalnız kurumsal hesap/cihaz, iddia dönemiyle sınırlı tarih aralığı, iddiaya bağlı anahtar kelimeler; özel yazışma içeriğine girme. İşveren işçi verisini yalnız işe yatkınlık veya sözleşmenin ifası için zorunlu olduğu ölçüde kullanabilir (TBK m. 419).
4. **Anayasal sınır:** özel hayatın gizliliği ve kişisel verilerin korunması (Anayasa m. 20), haberleşmenin gizliliği (m. 22).
5. **Delil sonucu:** Hukuka aykırı elde edilen delil mahkemece bir vakıanın ispatında dikkate alınamaz (HMK m. 189/2). Hukuka aykırı kayıt ve ele geçirme ayrıca suç oluşturabilir (TCK m. 135, m. 136).
6. **Güvenlik — KVKK m. 12:** inceleme kopyası sınırlı ekipte, erişim kayıtlı, saklama süresi belli.

Orantılılık çizgisini ezberden çizme; her dosyada ara ve dönen kararın künyesini birebir kullan:
```
tr_aym_ara(kind="bireysel", query="işveren kurumsal e-posta yazışmaları incelenmesi özel hayat")
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="kurumsal e-posta delil feshin geçerliliği")
tr_kurum_karari_ara(kurum="kvkk", query="çalışan e-posta kamera")
```

---

## Mod 1 — Soruşturma aç

`/employment-legal:investigation-open` ya da "soruşturma aç", "şu iddiayı soruştur" ile tetiklenir.

### Adım 1 — Ön görüşme (tek blokta sor)

> Soruşturma kaydını açmak için birkaç bilgi gerekiyor:
>
> **Olay**
> - İddia ya da endişe nedir (sade dille)?
> - Kim bildirdi / ne tetikledi (şikâyet, ihbar hattı, denetim, yönetici gözlemi)? **Hangi tarihte, kime ulaştı?** (m. 26 sayacı)
> - Hakkında iddia bulunan kişi kim (rol, kıdem, sözleşme türü)?
> - İddia edilen fiillerin yaklaşık dönemi?
> - Soruşturmayı kim yönetiyor: avukat mı (büro / şirket avukatı), İK mı (avukat danışman)?
>
> **Tür** (kaynak listesini buna göre öneririm)
> - İK: cinsel taciz / psikolojik taciz (mobbing) / ayrımcılık / misilleme
> - Mali: masraf, satın alma, zimmet, güveni kötüye kullanma
> - Üst yönetici: çıkar çatışması, rekabet, yönetim zafiyeti
> - İhbar/bildirim sonrası aleyhe işlem
> - Diğer
>
> **Paralel çerçeveler** (görüşme usulünü değiştirir)
> - Taraflardan biri sendika üyesi ya da işyeri sendika temsilcisi mi; TİS veya disiplin yönetmeliğinde özel usul var mı?
> - İşveren kamu kurumu mu? Hakkında iddia olan memursa 657 sayılı Devlet Memurları Kanunu disiplin rejimi uygulanır — bu skill kapsamı dışı; idari hukuk ekibine yönlendir.
> - Olay suç olabilir mi (ör. cinsel taciz — TCK m. 105, şikâyete bağlı; hırsızlık, zimmet)? Savcılık süreci başladı mı?
> - Yurt dışındaki ana şirkete veri gidecek mi (KVKK m. 9 — yurt dışına aktarım şartları)?

Paralel ceza süreci varsa: ceza soruşturmasının sonucunu beklemenin m. 26 süresine etkisi **tartışmalı — içtihadı kontrol et**; beklemeden önce avukata sor.

### Adım 2 — Klasör ve dosyalar

Aynı slug varsa üzerine yazmadan önce uyar. `<SORUŞTURMA>/` altında oluştur:

`kayit.yaml`
```yaml
# [ÜST BAŞLIK — CLAUDE.md ## Outputs; role göre değişir]
matter: "[ad]"
slug: "[slug]"
acilis: "[ISO tarih]"
yoneten: "[avukat | İK + avukat danışman]"
iddia: "[sade özet]"
sikayetci: "[ad/rol ya da anonim]"
hakkinda_iddia_olan: "[ad/rol]"
fiil_donemi: "[yaklaşık tarihler]"
ogrenme: {tarih: "[ISO]", kim: "[kişi/organ]", m26_son_gun: "[ISO — 'tartışmalı' notuyla]"}
savunma: {istem_tarihi: null, alinma_tarihi: null, tutanak: null}
kvkk_kontrol: {aydinlatma: null, hukuki_sebep: null, kapsam: null}
tur: "[ik | mali | yonetici | ihbar | diger]"
durum: acik
son_guncelleme: "[ISO]"
konular:
  - "[Konu 1 — ör. 'iş arkadaşına cinsel taciz iddiası']"
kayitlar: []
delil_bosluklari: []
```

`incelenen-belgeler.yaml`
```yaml
# [ÜST BAŞLIK]
matter: "[ad]"
toplam_incelenen: 0
toplam_one_cikan: 0
son_guncelleme: "[ISO]"
belgeler: []
```

`kaynak-listesi.yaml` — Adım 3'teki türe uygun liste. Her satır: `{id, kaynak, durum: acik|devam|tamam|uygulanmaz, not}`.

### Adım 3 — Kaynak listesi

Türe uygun listeyi göster ve sor: "Dosyanıza uyuyor mu? Uygulanmayanları 'uygulanmaz' işaretlerim; eklemek istediğiniz kaynak var mı?" Sonra `kaynak-listesi.yaml`'a yaz.

**İK (taciz / mobbing / ayrımcılık / misilleme):**
1. Şikâyetçi görüşmesi
2. Hakkında iddia olanın savunması — yazılı istem + tutanak (İş K. m. 19)
3. Tanık görüşmeleri — tarafların anlatımlarından belirle
4. Kurumsal e-posta/mesaj incelemesi — **KVKK kontrolü tamamlandıktan sonra**
5. Özlük dosyası — önceki ihtar, disiplin, performans (İş K. m. 75)
6. Önceki şikâyetler ve ihbar hattı kayıtları
7. Emsal uygulama — benzer olaylarda verilen kararlar (eşit davranma, m. 5)
8. Politikalar — taciz/mobbing politikası, disiplin yönetmeliği, TİS (**olay tarihindeki sürüm**)
9. Organizasyon şeması ve raporlama ilişkileri (olay tarihinde)
10. Takvim kayıtları — anlatımlarda geçen toplantı/etkinlikler
11. Şikâyetçiyi koruma tedbirleri — ne zaman, hangi önlem (TBK m. 417: işveren işçilerin psikolojik ve cinsel tacize uğramaması ve uğrayanların daha fazla zarar görmemesi için önlem almakla yükümlü)
12. Görüşme açılış bildirimleri — her görüşmede verildi ve imzalandı mı

**Mali usulsüzlük:** masraf raporları (ilgili dönem); onay kayıtları; tedarikçi sözleşme/fatura/ödeme kayıtları; muhasebe kayıtları; e-posta (KVKK kontrolü sonrası); hakkında iddia olanın savunması; onaylayan görüşmeleri; tedarikçi görüşmeleri (erişilebilirse); sistem erişim logları; önceki denetimler; maddi çıkar tespiti (varsa m. 26'daki bir yıllık süre uygulanmaz); görüşme açılış bildirimleri.

**Üst yönetici:** savunma/görüşme; YK ve komite kararları; iş sözleşmesi ve ekleri; prim ve pay planı kayıtları; masraf ve onaylar; e-posta (KVKK kontrolü sonrası); çıkar çatışması beyanları (ya da yokluğu); dış faaliyet ve rakiple ilişki kayıtları (TBK m. 396 — sadakat ve rekabet etmeme); tanıklar (astlar, eş düzey, YK üyeleri); önceki şikâyetler; **statü notu** — işletmenin bütününü sevk ve idare eden işveren vekili mi (İş K. m. 18 son fıkra: m. 18, 19 ve 21 uygulanmaz); görüşme açılış bildirimleri.

**İhbar/bildirim sonrası aleyhe işlem:** bildiren görüşmesi; ilk bildirimin yazılı hâli; bildirilen konuya ait kayıtlar; bildirenin aleyhine sonradan yapılan işlemler; bu işlemlerin karar vericileriyle görüşme; emsal — bildirimde bulunmayan benzer çalışanlara muamele; karar vericilerin yazışmaları (KVKK kontrolü sonrası); zaman analizi — bildirim ile işlem arasındaki yakınlık (işveren aleyhine idari veya adli makamlara başvurmak fesih için geçerli sebep değildir, İş K. m. 18/3-c); görüşme açılış bildirimleri. Genel bir ihbarcı koruma düzenlemesi olup olmadığını ezberden söyleme: `tr_mevzuat_ara(query="ihbarcı", search_in="fulltext")` ile güncel durumu kontrol et.

### Adım 4 — Görüşme açılış bildirimi (ABD'deki "Upjohn uyarısı" yerine)

Her görüşmenin başında söylenir, tutanağa yazılır ve imzalatılır:
- Görüşmeyi yapan kişi işverenin/şirketin avukatı (ya da İK) — çalışanın avukatı değildir.
- Görüşmenin amacı; içerik gizli tutulmaya çalışılır ama işveren kararlarında kullanılabilir ve yargılamada delil olarak sunulabilir; bu kararı işveren verir.
- Kişisel verilerin hangi amaçla işleneceği, kime aktarılabileceği, hukuki sebebi ve ilgili kişinin hakları (KVKK m. 10, m. 11).
- Misilleme yasağı; görüşmenin gizli tutulması ricası.
- Hakkında iddia olan kişiyle görüşmede: bu görüşme **m. 19 savunması mı, ön bilgi görüşmesi mi** — açıkça ayır. Savunmaysa yazılı istem ve süre verilir.

---

## Mod 2 — Veri ekle

`/employment-legal:investigation-add`, "şu soruşturmaya ekle" ya da avukat görüşme notu/belge yapıştırdığında tetiklenir.

1. **Matter:** Birden fazla `investigation-*` klasörü varsa hangisi olduğunu sor; tek klasör varsa devam et.
2. **Veri türü** (açık değilse sor): görüşme notu (kimin?), belge partisi, avukat notu/gözlemi, savunma istemi/tutanağı, açılış bildirimi teyidi. E-posta/cihaz/kamera partisi geldiyse ve `kvkk_kontrol` boşsa **önce KVKK kontrolünü tamamla**; tamamlanmadan işleme alma.
3. **Çekme ölçütleri.** Belge aşağıdakilerden **herhangi birini** karşılıyorsa öne çıkarılır (bilerek biraz agresif — kaçırmaktansa yanlış pozitif):
   1. Soruşturmanın taraflarından birinin (şikâyetçi, hakkında iddia olan, kayıtta geçen tanıklar) adını içeriyor.
   2. Kilit fiil döneminde bir tarafça yazılmış ya da alınmış.
   3. İddia türüne ilişkin anahtar kelime içeriyor (kelime listesi açılışta ve yeni anlatımlarla güncellenir).
   4. Açık ya da örtülü ikrar içeriyor ("yapmamalıydım", "yazıya dökme", "bunu sil").
   5. Kayıttaki bir anlatımla çelişiyor — çelişkiyi ve ilgili `kayit_id`'yi belirt.
   6. Yargılamada hassas olacak dil içeriyor: ayrımcı ifade, tehdit, korunan özellik veya sendikal faaliyet tartışması, iddia kalıbına uyan mali usulsüzlük.
   7. Anlatımlarda geçen ama belge setinde henüz görünmeyen bir belge türü (ör. görüşmede anılan toplantının davet kaydı yok) → öne çıkan belge değil, **delil boşluğu** olarak kaydet.

   Her belgenin sonucu: `one_cikti` (kayda girdi olarak eklenir) ya da `incelendi-onemsiz` (`incelenen-belgeler.yaml`'a tek satır açıklamayla).

   Parti sonrası rapor:
   ```
   Belge incelemesi tamamlandı.
   İncelenen: [N] | Öne çıkan: [N] | Önemsiz olarak kaydedilen: [N]
   Yeni delil boşluğu: [N]
   Öne çıkanlar: [tek satır açıklama — tetikleyen ölçüt no]
   ```
   Bu rapor "kaçan iğne" sorusunun cevabıdır: ölçütler yazılı, oran görünür. Sorgu modunda "[N] belgede [konu] hakkında belge görmedim" cümlesi ancak her incelenen belge kaydedildiği için anlamlıdır.
4. **Kayıt girdisi** — öne çıkan her öğe için `kayit.yaml`'a ekle:
   ```yaml
   - kayit_id: [otomatik artan]
     kayit_turu: [gorusme | belge | avukat-notu | savunma | bosluk]
     olay_tarihi: "[olayın tarihi — kayıt tarihi değil]"
     kayit_tarihi: "[ISO tarih-saat]"
     kaynak: "[kişi/rol ya da belge adı]"
     kaynak_turu: [sikayetci | hakkinda-iddia-olan | tanik | belge | avukat-notu]
     konular: ["[ilgili konu]"]
     onem: [yuksek | orta | arka-plan]
     ozet: "[kayda kattığı şey — 2-5 cümle]"
     alinti: "[önemliyse birebir alıntı]"
     celistigi_kayit: [kayit_id | null]
     destekledigi_kayit: [kayit_id | null]
     guvenilirlik_notu: ""
     tetikleyen_olcut: "[belgeler için ölçüt no]"
     dosya_sinifi: [avukat-calisma-urunu | isveren-delil]
   ```
   Delil boşluğu:
   ```yaml
   - bosluk_id: [otomatik artan]
     aciklama: "[var olması gereken ama bulunamayan belge/kaynak]"
     kaynagi: "[hangi kayıt ya da anlatım ortaya çıkardı]"
     nereden_alinir: "[kaynak]"
     oncelik: [yuksek | orta | dusuk]
     durum: acik
   ```
5. **Kaynak listesi:** Eklenen veri bir liste kalemine karşılık geliyorsa "tamam mı, devam mı?" diye sor. Kendiliğinden `tamam` işaretlemesi **yapma** — yeterliliğe avukat karar verir.

---

## Mod 3 — Kayda soru sor

`/employment-legal:investigation-query` ya da soruşturmaya yöneltilen her soru ("X ne dedi", "neler destekliyor", "neyi eksik", "her konuda en güçlü delil") ile tetiklenir. Cevaplamadan önce kaydın tamamını oku; her cevapta `kayit_id` göster.

- **Olgu sorusu:** İlgili girdilerden cevapla. Kayıtta yoksa: "Bu soruşturma kaydında ([N] girdi) [konu] hakkında bilgi görmedim; boşluk olarak işaretleyebilirim."
- **Çelişki sorusu:** Tüm `celistigi_kayit` bağlarını çıkar; her biri için çelişkinin ne olduğu, hangi girdiler, varsa hangi belgenin çelişkiye ışık tuttuğu.
- **Kapsama sorusu:** `kaynak-listesi.yaml`'daki açık kalemler, `delil_bosluklari`, anlatımlarda geçip toplanmamış kaynaklar.
- **Güç sorusu:** Konu konu: en yüksek önemdeki girdiler, belgesel destek, çözülmemiş çelişkiler.
- **Usul sorusu:** Savunma istendi/alındı mı (tarihleriyle), m. 26 son günü ve kalan iş günü, açılış bildirimleri tamam mı, KVKK kontrolü yapıldı mı. Eksik varsa işaretle.

---

## Mod 4 — Soruşturma notu (taslak / güncelleme)

`/employment-legal:investigation-memo`, "notu yaz" ya da "notu güncelle" ile tetiklenir.

**İlk taslak — ön şartlar** (eksikse uyar, avukat isterse yine yaz): her açık konu için en az bir girdi; şikâyetçi ve hakkında iddia olan girdileri; savunma durumu belli; yüksek öncelikli açık kaynaklar işaretli.

`<SORUŞTURMA>/not.md` dosyasına şu yapıyla yaz (A sınıfı):

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs]

**İÇ SORUŞTURMA NOTU**
Kime: [avukat doldurur] | Kimden: [avukat doldurur] | Tarih: [tarih]
Konu: İç soruşturma — [matter] | Durum: ÖN TASLAK

## Yönetici özeti
[2-3 paragraf: iddia, kapsam ve yöntem, konu bazında bulgular (Sabit / Sabit değil / Belirsiz), önerilen işlem. En son yazılır, en başta durur.]

## Arka plan ve kapsam
Tetikleyen olay · İncelenen iddialar (numaralı) · Kapsam dışı olanlar ve nedeni · Fiil dönemi · Soruşturma dönemi · Öğrenme tarihi, öğrenen kişi/organ ve m. 26 son günü

## Yöntem
| Kişi | Rol | Tarih | Açılış bildirimi | Savunma mı? |
|---|---|---|---|---|
İncelenen belgeler (tür, adet, tarih aralığı; tam liste ayrı) · KVKK kontrolü özeti (aydınlatma, hukuki sebep, kapsam) · Sınırlamalar (istenip alınamayanlar)

## Bulgular — konu bazında
### Konu 1: [iddia]
[Delilin gösterdiği; kayıt ID'leri köşeli parantezde. Çelişkiyi düzleştirme, açıkça yaz.]

## Güvenilirlik değerlendirmesi
[Yalnız bulgunun hangi anlatıma itibar edildiğine bağlı olduğu kişiler]
İç tutarlılık · Belgesel destek / çürütme · Saik · Gözlem (yüz yüzeyse) · Değerlendirme (itibar / itibar yok / kısmen — gerekçesiyle)

## İlgili politikalar
[Olay tarihinde yürürlükteki sürüm; sonradan kabul edileni anma]

## Hukuki çerçeve (avukat teyit eder)
- Olgunun eşleştiği dayanak: m. 25/II bendi (haklı fesih) / m. 18 geçerli sebep / disiplin cezası
- Usul: savunma (m. 19); yazılı ve gerekçeli fesih bildirimi taslağı
- Süre: m. 26 — öğrenme tarihi, son gün, risk
- İşverenin koruma yükümlülüğü (TBK m. 417) ve alınan önlemler; cinsel taciz bildirimine rağmen gerekli önlem alınmazsa şikâyetçi işçinin derhal fesih hakkı (İş K. m. 24/II-d)
- İspat: m. 20/2, m. 5 son fıkra; hukuka aykırı delil (HMK m. 189/2)
- Her madde atfı `tr_mevzuat_madde_getir` ile teyit edildi mi: [evet / hayır — hangileri]

## Sonuçlar
| Konu | Bulgu | Dayanak (tek cümle) |
|---|---|---|
*Kanunda iç soruşturma için ispat ölçütü yok; bulgular eldeki delilin ağırlığına göre verildi. Mahkemedeki ispat yükü ve ölçüsü ayrıdır — tartışmalı, içtihadı kontrol et.*

## Öneriler
Disiplin işlemi (sonuç değil dayanak) · Şikâyetçiyi koruma tedbirleri · Politika/süreç · Eğitim · Ek soruşturma · İzleme

## Ek A — Kronoloji (olay_tarihi sırasıyla: Tarih | Özet | Kaynak [ID])
## Ek B — İncelenen belgeler (incelenen-belgeler.yaml özeti)
```

**Güncelleme:** Notu ve kaydı oku; notun son güncellemesinden sonra eklenen girdileri bul ve raporla:
```
Son taslaktan ([tarih]) bu yana: [N] yeni girdi | Yeni konu: [..] | Yeni çelişki: [..] | Kapanan boşluk: [..]
Güncellenecek bölümler: Bulgular [konular] · Güvenilirlik [..] · Sonuçlar [..] · Ek A: [N] yeni kronoloji girdisi
```
Sor: "Tüm notu mu, yalnız etkilenen bölümleri mi güncelleyeyim?" Önceki metni koru; değişen bölümleri avukat inceleyene kadar `[GÜNCELLENDİ: tarih]` ile işaretle.

---

## Mod 5 — Hedef kitle özeti

`/employment-legal:investigation-summary` ya da "[kitle] için özet" ile tetiklenir. Sor: kitle kim, bu özet hangi kararı destekleyecek? Not yoksa önce not yazmayı öner.

- **İK özeti** (disiplin kararı için): olgusal özet (hukuki analiz yok), her iddia için bulgu, önerilen işlem. **Girmez:** güvenilirlik yöntemi, hukuki risk, avukat izlenimleri, kayıt ID'leri ve belge atıfları. Başlık: "GİZLİDİR — YALNIZ İK KULLANIMI — DAĞITILMAZ". İK özeti davada sunulabilir; B sınıfı dikkatle, olgusal yaz.
- **Yönetim / YK özeti:** tek paragrafta iddia ve kapsam, ana bulgular, iş etkisi (genel düzeyde, hukuki analiz yok), alınan önlemler. Başlık: `## Outputs`.
- **Dış avukat brifingi:** tam bağlam ve hukuki risk, açık iplikler, tartışmalı güvenilirlik, davada en önemli olacak belgeler, süreler (m. 26 son günü; fesih olursa işçinin fesih bildiriminin tebliğinden itibaren bir ay içinde arabulucuya başvurma hakkı — İş K. m. 20/1). Başlık: `## Outputs`.
- **Şikâyetçiye / ilgiliye sonuç bildirimi** (istenirse): sonuç ve alınan önlemler düzeyinde; başkalarının kişisel verisini ve tanık beyanlarını açma (KVKK m. 4/2-ç, İş K. m. 75/2).

## Sonuçlu işlem kapısı — dış merciye yanıt

Arabuluculuk için yazılı pozisyon, karşı taraf avukatının ihtarnamesine cevap, iş müfettişi incelemesi, KVKK ilgili kişi başvurusu (m. 11) veya Kurul şikâyeti, savcılık ifadesi gibi **dış yanıt** hazırlanmadan önce `## Who's using this` bölümünü oku. Rol **avukat değilse**:

> Bir iddiaya, başvuruya ya da ihtara verilen cevabın hukuki sonucu vardır: burada alınan pozisyon sonraki yargılamada aleyhinize kullanılabilir, savunma imkânı farkında olmadan kaybedilebilir. Bu cevabı bir avukatla gözden geçirdiniz mi? Evetse devam ediyorum. Hayırsa avukata götürmeniz için kısa bir brif hazırlarım: iddia, merci ve süre; soruşturmanın bulguları (iddia bazında, incelenen belgeler, görüşülen kişiler, açılış bildirimleri); çözülmemiş çelişkiler; önerilen cevabın neyi örtülü kabul ettiği; açık sorular; ne ters gidebilir (gizliliğin kaybı, çelişkili olgu beyanı, kaçırılan süre); avukata sorulacaklar.
>
> Avukat bulmak için bağlı olduğunuz ilin barosuna başvurabilirsiniz.

Açık "evet" olmadan dış yanıt taslağı üretme. Kurum içi not, İK özeti ve yönetim brifingi bu kapıya takılmaz (gizlilik uyarısı yine geçerlidir).

## Bu skill ne yapmaz

- Disiplin kararı vermez — avukatın bulgularını destekler.
- Gizlilik garantisi vermez — koruma soruşturmanın nasıl kurulduğuna bağlıdır, başlığa değil.
- Okuyamadığı formatı işlemez — elle inceleme için işaretler.
- Görüşme yapmaz, savunma almaz — tutanakları kaydeder; açılış bildiriminin ve savunmanın yapılıp yapılmadığını izler.

## Sonraki adımlar

CLAUDE.md `## Outputs`'taki sonraki adım ağacıyla bitir; seçenekleri üretilen işe göre uyarla (ör. savunma istem yazısı taslağı, fesih değerlendirmesi için `/employment-legal:termination-review`, avukata eskalasyon, ek delil, bekle-izle, başka bir şey). Seçimi avukat yapar.

---

## /employment-legal:international-expansion

---
name: international-expansion
description: >
  Referans: sınır ötesi işe alım için uygulama planı çerçevesi — iki yön: (A) Türk
  işverenin yurt dışında işe alımı ya da personel göndermesi, (B) yabancı işverenin
  Türkiye'de işe alımı. Yapı seçeneklerinin çerçevelenmesi (Türkiye'de ABD tarzı EOR
  yerine İş K. m. 7 sınırları), Türkiye ilk gün yükümlülükleri (sözleşme, SGK, çalışma
  izni, KVKK aktarımı), ArthurLegal MCP ile yabancı mevzuat araması, vergi/finans/İK
  soruları, yerel avukat brif talebi ve kalıcı takip dosyası. /expansion-kickoff ve
  /expansion-update tarafından yüklenir; doğrudan çağrılmaz.
user-invocable: false
---

# Uluslararası Genişleme — Ortak Çerçeve

## Matter bağlamı

Uygulama CLAUDE.md'sinde `## Matter workspaces` bölümüne bak. `Enabled` `✗` ise bu paragrafın gerisini atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/employment-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Sınır ötesi işe alım dağınık yürür: hukuk iş hukuku sorularını bilir ama vergi bakımından işyeri riskini bilmez; finans maliyeti bilir ama çalışma izni süresini bilmez; İK ücreti bilir ama ilk gün tescil yükümlülüklerini bilmez. Bu skill haritayı çıkarır, her paydaşa doğru soruyu taslaklar, yerel avukata brif hazırlar ve oturumlar arası süren bir takip dosyası kurar. Genişleme kararı verilmiş varsayılır; "genişlemeli miyiz?" çerçevesi değildir.

**Kaynak kuralı.** Türkiye kuralları `tr_mevzuat_madde_getir` ile doğrulanmış maddelere dayanır; uygularken metni yeniden çek ve değişiklik dipnotlarını oku. Yabancı ülke kuralı **ezberden yazılmaz**: ArthurLegal MCP'nin ulaştığı ülkelerde araçla aranır; diğerlerinde "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al". Araç sonucu olsa bile her ülke için yerel avukat brifi gönderilir — uygulama bilgisi ve güncellik onunla teyit edilir.

## Bağlam ve üst başlık

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → eşik tablosu (yurt dışı satırları dahil), eskalasyon, önceki genişleme notları. Her çıktı `## Outputs` başlığıyla açılır.

## Adım 0 — Yön

> Hangi yön?
> - **A — Türkiye'den dışarı:** [ŞİRKET ADI] yurt dışında işe alıyor ya da Türkiye'deki personelini yurt dışına gönderiyor.
> - **B — Dışarıdan Türkiye'ye:** yabancı işveren Türkiye'de işe alıyor ya da yabancı uyruklu personel Türkiye'de çalışacak.

İkisi birlikte olabilir; her ülke-yön çifti ayrı takip dosyasıdır.

## Adım 1 — Bilgi toplama (tek blokta sor, cevap bekle)

> Planı kurmadan önce genişlemenin şeklini anlamam gerekiyor; cevaplayamadıklarınız da bilgi verir:
>
> **Genişleme** — Hangi ülke? Hangi roller (satış kapatan biri ile kod yazan mühendis farklı risk doğurur)? 12 ayda kaç kişi? İlk kişi ne zaman başlamalı? Çalışanların uyruğu (Türk, yerel, üçüncü ülke)?
>
> **Mevcut durum** — O ülkede şirket/şube var mı? Aynı grupta orada ya da Türkiye'de şirket var mı? Aracı (EOR) ya da özel istihdam bürosu düşünülüyor mu? Vergi/finans haberdar mı? Yerel avukat var mı?
>
> **Yapı** — Yerel işe alım mı, Türkiye'den (ya da ana şirketten) geçici görevlendirme mi; ne kadar süre?
>
> **Stratejik bağlam** — Kalıcı ekip mi, pazar testi mi? Yapı kararını hangi yönetici verecek?

## Adım 2 — Yapı seçenekleri (karar verme, çerçevele)

Kararı CFO ve vergi ekibinin verebileceği netlikte çerçevele.

| Faktör | Aracı modeli lehine | Şirket/şube lehine |
|---|---|---|
| 12 aylık kişi sayısı | Az | Çok |
| İlk işe alıma kalan süre | Kısa | Uzun |
| Stratejik bağlılık | Pazar testi | Kalıcı varlık |
| Maliyet | Aracı payı kabul edilebilir | Ölçek şirketi verimli kılar |
| Kontrol ihtiyacı | Düşük | Yüksek — doğrudan işveren ilişkisi |
| Fikri hak hassasiyeti | Düşük | Yüksek — sahiplik daha temiz |

Başa baş sayısı, aracı payı, kuruluş maliyeti ve süresi ülkeye ve sağlayıcıya göre değişir — sabit yazma; vergi/finans ve sağlayıcıya sor.

### B yönü — Türkiye'de yapı seçenekleri

| Seçenek | Ne gerektirir | Dikkat |
|---|---|---|
| Türkiye'de şirket/şube kurup doğrudan istihdam | Şirket kuruluşu (kurumsal ekip); işyeri bildirimi ve SGK tescili (Adım 4B) | Asıl yol; eşikler işçi sayısıyla büyür |
| Grup şirketinden geçici devir | Türkiye'de grup şirketi varsa: devir sırasında işçinin yazılı rızası; yazılı olarak en çok altı ay, en fazla iki yenileme; devreden işverenin ücret ödeme yükümlülüğü sürer, devralan ödenmeyen ücret ve prim için birlikte sorumlu (İş K. m. 7 son fıkra) | Yalnız holding ya da aynı şirketler topluluğu içinde |
| Özel istihdam bürosu üzerinden geçici işçi | İŞKUR izinli büro; yalnız m. 7/2'de sayılan hâllerde; (a)-(c) dışındaki hâllerde en fazla dört ay, (g) hariç toplam sekiz ayı geçmemek üzere en fazla iki yenileme; işveren özel istihdam bürosudur (İş K. m. 7) | **ABD tarzı süresiz EOR'un Türkiye'de doğrudan karşılığı yok.** Sürekli işi bu yolla gördürmek m. 7 sınırlarını aşar; gerçek işverenin kim sayılacağı riski — tartışmalı, içtihadı kontrol et |
| Yabancı şirketin Türkiye'de tüzel kişilik/şube olmadan işçi çalıştırması | SGK işyeri tescili, bordro ve vergi uygulaması | Uygulamada sorunlu — SGK/vergi uzmanıyla teyit et; tartışmalı |
| Serbest meslek / yüklenici | Gerçek bağımsızlık | Bağımlı çalışma varsa iş sözleşmesidir (İş K. m. 8 tanımı) → `/employment-legal:worker-classification` |

```
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="geçici iş ilişkisi özel istihdam bürosu muvazaa")
```
Dönen kararların künyesini birebir kullan; karar numarası ezberden yazma.

### A yönü — Türkiye'den dışarı

- **Yerel işe alım** (hedef ülkedeki şirket ya da aracı): hedef ülke hukuku — Adım 4A.
- **Türkiye'den personel götürme:** İŞKUR'dan izin almadan kendi işlerinde çalıştıracakları işçileri yurt dışına götürenlere ve Kuruma onaylatılmayan her yurt dışı hizmet akdine idari para cezası öngörülür (4904 s. Kanun m. 20/1-g). İzin usulünü ilgili yönetmelikte bul: `tr_mevzuat_ara(query="yurt dışına işçi", types=["YONETMELIK"])`. Ceza tutarlarını yazma — yeniden değerleme ile güncellenir, teyit et.
- **Sosyal güvenlik:** hedef ülkeyle ikili sosyal güvenlik sözleşmesi var mı: `tr_mevzuat_ara(query="sosyal güvenlik sözleşmesi [ülke]")`. Yoksa çifte prim riski → finans.

### Uygulanacak hukuk ve yetki (her iki yön)

- Taraflar hukuk seçebilir; ancak işçinin mutad işyeri hukukunun emredici hükümlerinin sağlayacağı asgari koruma saklıdır. Seçim yoksa işçinin işini mutad olarak yaptığı işyeri hukuku uygulanır; başka ülkede geçici çalışma mutad işyerini değiştirmez; devamlı birden fazla ülkede çalışmada işverenin esas işyeri hukuku; hâlin bütün şartlarına göre sözleşmeyle daha sıkı ilişkili bir hukuk varsa — işin yapıldığı yerin zorunlu uygulanan hükümleri saklı kalmak üzere — o uygulanabilir (MÖHUK m. 27). **m. 27, 4/6/2025 tarihli 7550 s. Kanunla değişti — eski metne dayanan kaynak ve şablonları kullanma.**
- Türk mahkemesinin yetkisi: mutad işyeri Türkiye'deyse orası; işçinin işverene karşı davasında işverenin ya da işçinin Türkiye'deki yerleşim yeri veya mutad meskeni mahkemesi de yetkilidir (MÖHUK m. 44).

### Vergi bakımından işyeri riski (vergi ekibine)

Satış, iş geliştirme, müşteri yönetimi ya da şirket adına sözleşme müzakere/imza yetkisi olan roller varsa açıkça işaretle:

> **İşyeri riski:** [rol], [ülke]de şirket kurulmadan vergi bakımından işyeri ya da daimi temsilci doğurabilir. Bu iş hukuku değil vergi sorusudur; ilk işe alımdan önce vergi ekibi değerlendirmeli (`tax-legal` eklentisi), çifte vergilendirmeyi önleme anlaşması kontrol edilmeli.

## Adım 3 — Paydaşlar: ne yapacaklar, hukuk ne soracak

"Finansa haber verin" deme; soruyu taslakla.

**CFO / vergi** (ilk işe alımdan önce zorunlu) — yapı ekonomisi, işyeri analizi, pay/opsiyon vergisi.
- 12 ayda [N] kişide, aracı payı, kuruluş maliyeti ve uyum yükü hesaba katıldığında hangi sayıda şirket kurmak daha ekonomik? Aracıdan şirkete geçişte mevcut çalışanların devri nasıl olur (B yönünde m. 7 süre sınırları)? Sağlayıcının yerel uyum geçmişi incelendi mi?
- [Rol] [ülke]de şirket kurulmadan işyeri ya da vergisel bağ doğurur mu; doğurursa şirket takvimi değişir mi? Soru çözülmeden işe alırsak risk penceresi ne?
- Pay/opsiyon planımız [ülke]de nasıl vergilenir; çalışana tahsis ve hak edişte yerel danışman gerekir mi?
- Şirket kurulursa ana şirketle hangi grup içi hizmet sözleşmesi ve transfer fiyatlandırması gerekir? (`/tax-legal:transfer-pricing-review`)

**Finans / bordro** (ilk maaştan önce) — bordro sağlayıcı, zorunlu işveren katkıları, banka.
- Yerel bordro sağlayıcı belli mi (aracıysa sosyal katkılar dahil bordroyu üstleniyor mu)?
- Zorunlu işveren katkıları (emeklilik, sosyal sigorta, sağlık) ücret modelinde var mı? Oranları sabit yazma; güncel oranı teyit et. B yönünde SGK primleri dahil.
- Pay planında hak edişte işveren tarafı vergi kesintisi modellendi mi?

**İK / ücret ve yan haklar** (teklif öncesi) — yan hak ve ücret karşılaştırması, zorunlu ve piyasa standardı haklar.
- [Ülke]de hangi haklar kanunen zorunlu, hangileri piyasa standardı? (Zorunludan az ya da piyasadan fazla vaat etmeyelim.)
- Standart pay paketimiz bu pazarda rekabetçi mi?
- Günlük yönetici yerel mi, merkezden uzaktan mı? (Bazı ülkelerde temsil ve sözleşme şartlarını etkiler.)

**Yerel avukat** (zorunlu — atlanmaz): Adım 4A'daki brif bu işin gündemidir; baştan tek seferde gönder.

**B yönünde Türk hukuku ekibi:** Adım 4B kontrol listesi.

## Adım 4A — Yabancı ülke: önce ArthurLegal, sonra yerel avukat

| Ülke | Önek | Başlangıç çağrısı |
|---|---|---|
| AB üyesi (ortak çerçeve) | `eu_` | `eu_search_eu_law(query="transparent and predictable working conditions")` → `eu_get_document_text(celex="32019L1152")`; gönderme: `eu_search_eu_law(query="posting of workers")`; uygulanacak hukuk: `eu_search_eu_law(query="law applicable to contractual obligations")`; çalışan verisi: `eu_search_eu_law(query="protection of natural persons processing of personal data")` |
| Almanya | `de_` | `de_norm_getir(kanun="KSchG", norm="1")` (fesih koruması); `de_gesetz_ara(sorgu="Nachweisgesetz")`; işyeri temsili: `de_norm_getir(kanun="BetrVG", norm="1")`; içtihat: `de_rii_case_search(query={"court": "BAG", "date_from": "2022-01-01"})` |
| Birleşik Krallık | `uk_` | `uk_search_legislation(title="Employment Rights Act", type="ukpga")`; `uk_get_section(year="1996", number="18", section="94")`; alıntıdan önce `uk_get_effects` |
| Hollanda | `nl_` | `nl_search_legislation(query="Burgerlijk Wetboek Boek 7")` |
| Polonya | `pl_` | `pl_search_by_title(title="Kodeks pracy", in_force_only=true)` → `pl_get_act_text(publisher="DU", year=..., pos=...)` (güncel birleştirilmiş metni sonuçlardan seç) |
| Avusturya | `at_` | `at_search_legislation(title="Arbeitsverfassungsgesetz")`; konu araması: `at_search_legislation(terms="Kündigung Arbeitnehmer")` |
| İrlanda | `ie_` | `ie_search_acts(query="unfair dismissals")` → `ie_get_section(year=..., number=..., section=...)` |
| Finlandiya | `fi_` | `fi_search_acts(query="työsopimuslaki")` → `fi_get_act(year=..., number=...)` |
| İspanya | `es_` | `es_search_legislation(query="Estatuto de los Trabajadores", only_in_force=true)` → `es_get_act_text(boe_id=...)` |
| Japonya | `jp_` | `jp_search_laws(keyword="労働基準法")` (law_id `322AC0000000049`) → `jp_get_article(law_id="322AC0000000049", article=...)`; ayrıca `jp_search_laws(keyword="労働契約法")` |
| Azerbaycan | `az_` | `az_search_acts(query="Əmək Məcəlləsi", types=[107])` → `az_get_act_fulltext(act_id=...)` |
| Diğer tüm ülkeler (ABD, BAE, İsviçre, Rusya …) | — | **ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al.** (ABD için yalnız kuruluysa üçüncü taraf CourtListener bağlayıcısı.) |

Kurallar: sonuç ince görünürse önce `status` çağır (yüklenmemiş kaynak ≠ boş sonuç). Dizin kapsamı yıl aralığıyla sınırlı araçlarda (`ie_`, `fi_`, `pl_search_indexed`) kapsamı rapora yaz. Aracın döndürdüğü atıf ve bağlantıyı birebir kullan; veri gelmezse "UYARI: veri çekilemedi, teyidiniz gerekli: <aracın source_url'si>". Sağlayıcı ya da grup şirketi kimliği için `gleif_search_entities(name="[tam unvan]", jurisdiction="[ISO kodu]")`.

**Yerel avukat brif talebi — [Ülke]** (takip dosyasına tek açık kalem: sahibi Yerel avukat, sorular alanında brifin tamamı; ülke daha önce sorulduysa yine gönder — bu bir güncellik kontrolüdür):

> [Ülke]de [tarih]ten itibaren [roller] için [N] kişi istihdam etmeyi planlıyoruz; 12 ay hedefi [N]. Tercih edilen yapı (görüşünüze ve vergi ekibine bağlı): [aracı / şirket / görevlendirme / belirsiz]. Lütfen her soruyu birincil kaynak atfıyla, tablo değil soru-cevap olarak yanıtlayın — değişiklikleri izleyebilmek istiyoruz:
> 1. **Yapı** — şirket, aracı, yüklenici seçenekleri ve bu sayı ve roller için ödünleşim.
> 2. **Sözleşme** — zorunlu şekil ve içerik, geçersiz hükümler, dil/çeviri şartı.
> 3. **Fesih** — bildirim süresi ve tazminat, korunan sebepler, toplu çıkarmada seçim kuralları; ilk günden kurulacak belge standardı.
> 4. **Zorunlu haklar ve işveren katkıları** — emeklilik, sosyal sigorta, sağlık, ücretli izin, ikramiye; güncel oranlar ve dayanak.
> 5. **Rekabet yasağı, gizlilik, fikri haklar** — geçerlilik şartları, tazminat zorunluluğu.
> 6. **Çalışan temsili** — işyeri konseyi, sendika, toplu sözleşme; hangi sayıda tetiklenir; sendikasız olsak da sektörel sözleşmeye tabi miyiz?
> 7. **Çalışan verisi** — yerel yükümlülükler ve Türkiye'ye veri aktarım mekanizması.
> 8. **Çalışma ve oturma izni** — Türk ve üçüncü ülke vatandaşları için izin türleri ve süreler.
> 9. **Sektörel kurallar.**
> 10. **Yüklenici sınıflandırması** — ölçüt ve yeniden nitelendirme riski.
> 11. **Pay/opsiyon** — yerel vergi, sermaye piyasası ve iş hukuku kuralları.
> 12. **İlk gün uyumu** — tescil, bildirim, ilan yükümlülükleri.
> 13. **Bu ülkede ilk kez işe alan Türk işverenleri en çok neyi şaşırtıyor** ve yakın zamanda ne değişti?

A yönünde Türk tarafında ayrıca: KVKK m. 9 (çalışan verisinin yurt dışına aktarımı — aşağıdaki 4B/7. satır), MÖHUK m. 27 hukuk seçimi klozu, 4904 m. 20 İŞKUR izni.

## Adım 4B — Türkiye (B yönü): ilk gün kontrol listesi

| # | Kalem | Dayanak | Sahibi |
|---|---|---|---|
| 1 | İş sözleşmesi — süresi bir yıl ve daha fazla olan sözleşme yazılı; yazılı sözleşme yoksa en geç iki ay içinde çalışma koşullarını gösteren yazılı belge | İş K. m. 8 | Hukuk |
| 2 | İşyeri bildirimi — işyerini kuran işveren bir ay içinde bölge müdürlüğüne; şirketlerde tescil kaydı ticaret sicilinin gönderdiği belgelerle | İş K. m. 3 | Hukuk / kurumsal |
| 3 | SGK işyeri bildirgesi — en geç sigortalı çalıştırmaya başlanan tarihte; şirket kuruluşunun ticaret siciline bildirimi SGK'ya yapılmış sayılır | 5510 m. 11 | Bordro |
| 4 | Sigortalı işe giriş bildirgesi — sigortalılık başlangıcından önce (kanundaki istisnalar saklı) | 5510 m. 8 | Bordro |
| 5 | Yabancı çalışan — çalışma izni olmaksızın çalışma ve çalıştırma yasak; başvuru yurt içinde Bakanlığa, yurt dışında konsolosluğa; belgeler tamsa otuz günde değerlendirme; ilk izin en çok bir yıl ve belirli işyeri için; yabancı ortak-müdür/YK üyesi izinle çalışabilir; nitelikli işgücü, proje çalışanı, AB vatandaşı gibi istisnai kategoriler | 6735 m. 6, 7, 10, 16 | İK / hukuk |
| 6 | İzinsiz çalıştırma yaptırımı — idari para cezası (tutarları teyit et — yeniden değerleme), sınır dışı ve dönüş masraflarının işverence karşılanması | 6735 m. 23 | Hukuk |
| 7 | Çalışan aydınlatması ve ana şirkete veri aktarımı — yeterlilik kararı yoksa uygun güvence: standart sözleşme (imzadan itibaren beş iş günü içinde Kuruma bildirim), bağlayıcı şirket kuralları ya da diğer m. 9 yolları | KVKK m. 10, m. 9 | Hukuk / uyum |
| 8 | Uygulanacak hukuk ve yetki klozu | MÖHUK m. 27, m. 44 | Hukuk |
| 9 | Büyüme eşikleri — 30 işçi iş güvencesi (m. 18), toplu işçi çıkarma (m. 29), 50 işçi engelli kontenjanı (m. 30); CLAUDE.md eşik tablosuna satır ekle | İş K. | Hukuk / İK |
| 10 | Uyuşmazlıkta arabuluculuk dava şartı | 7036 m. 3 | Hukuk |
| 11 | Vergi, SGK prim oranları, asgari ücret, kıdem tazminatı tavanı — sabit yazma; güncel değeri teyit et | — | Finans |

Açık sorular (Türk hukuku ekibi + SGK/vergi uzmanı): şube mi şirket mi; tüzel kişilik kurulmadan istihdamın SGK ve vergi uygulaması; grup içi geçici devirde ücretin hangi şirketten ödeneceği ve bordro düzeni.

## Adım 5 — Takip dosyası

Yol: matter workspace kapalıysa `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-<ulke-slug>.yaml`; açıksa aktif matter klasöründe aynı ad. Dosya oturumlar arası kalır. Adım 2-4'te çıkan her eylem **ayrı kalem** olur; her kalem tek sahibe atanır ve tamamlanabilir olur.

```yaml
# [ÜST BAŞLIK — CLAUDE.md ## Outputs]
ulke: [ad]
ulke_slug: [kucuk-harf-tireli]
yon: [TR-yurtdisi | yurtdisi-TR]
arthurlegal_kaynak: [eu_ / de_ / ... | yok — yerel hukukçu]
baslangic: [ISO tarih]
ilk_ise_alim_hedefi: [ISO tarih | belirsiz]
kisi_12_ay: [N]
roller: [liste]
stratejik: [test | kalici]
yapi: [sirket | grup-ici-devir | ozel-istihdam-burosu | araci | yuklenici | belirsiz]
yerel_avukat: [true | false]
vergi_isyeri_riski: [true | false]
son_guncelleme: [ISO tarih]

acik_kalemler:
  - id: 1
    kategori: [yapi | vergi | finans | ik | yerel-avukat | uyum | izin]
    kalem: "[ne yapılacak]"
    sahibi: "[birim ya da kişi]"
    durum: [acik | devam | tamam | blokeli]
    son_tarih: [ISO tarih | null]
    bagimli_oldugu: []        # önce kapanması gereken kalem id'leri
    dayanak: "[doğrulanmış madde ya da araç sonucu atfı]"
    sorular:
      - "[Adım 2-4'te taslaklanan soru]"
    notlar: ""
```

## Adım 6 — Çıktı

> **Yargı çevresi varsayımı.** Bu plan ön görüşmedeki tek ülke ve yön içindir. Yerel iş hukuku, vergi, çalışan temsili ve veri koruma kuralları ülkeye, bölgeye, sektöre ve kişi sayısına göre değişir ve sık değişir. Yabancı ülkeye ilişkin esaslı cevap ArthurLegal araç sonucundan ve yerel avukat brifinden gelir; bu skill'in kendi bilgisinden gelmez. Plan başka ülkeye uyarlanırsa brifi yeniden gönder.

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs]
## Uluslararası Genişleme: [Ülke] ([yön]) — [Tarih]
**İlk işe alım hedefi:** [tarih] · **12 ay:** [N] kişi · **Roller:** [liste]
**ArthurLegal kaynağı:** [önek | yok — yerel hukukçu] · **Takip dosyası:** [yol]
⚠️ İnceleyen notu: doğrulanamayan madde / çekilemeyen yabancı kaynak: [liste | yok] · tartışmalı: [liste]

### Yapı seçenekleri — [Adım 2 tablosu; B yönünde m. 7 notu; işyeri riski işareti]
### Uygulanacak hukuk ve yetki — [MÖHUK m. 27 / m. 44 özeti; önerilen klozun ana hatları]
### Kimler devreye girmeli — Vergi [N] soru · Finans/bordro [N] · İK [N] · Yerel avukat (brif aşağıda)
### [A yönü] ArthurLegal notları + yerel avukat brifi — [çağrılar, dönen atıflar; brifin tamamı]
### [B yönü] Türkiye ilk gün kontrol listesi — [Adım 4B tablosu, doğrulama tarihiyle]
### Açık kalemler ([N])
| # | Kalem | Sahibi | Durum | Son tarih |
|---|---|---|---|---|

Kalemler kapandıkça `/employment-legal:expansion-update [ülke]` çalıştırın.
```

## Bu skill ne yapmaz

- Yabancı ülkenin iş hukuku hakkında kendi bilgisinden kural söylemez — ArthurLegal aracı ve yerel avukat brifi üzerinden gider.
- Yapı kararını vermez — doğru karar vericiler için çerçeveler.
- Yerel iş sözleşmesini yazmaz — yerel avukatın yazması gerektiğini işaretler. (B yönünde Türk iş sözleşmesi için `/employment-legal:hiring-review`.)
- Yerel avukatın yerini tutmaz — ArthurLegal'ın kaynağı olan ülkelerde de her yeni ülke yerel teyit ister.

---

## /employment-legal:investigation-add

---
name: investigation-add
description: >
  Açık bir iç soruşturmaya veri ekle — belge, görüşme notu, savunma tutanağı ya da
  gözlem. Partileri yazılı çekme ölçütlerine göre tarar, önemli öğeleri öne çıkarır,
  incelenen her belgeyi kapsama doğrulaması için kaydeder; e-posta/cihaz/kamera
  verisinde önce KVKK kontrolünü ister. Yeni delil, görüşme notu ya da belge
  geldiğinde kullan.
argument-hint: "[matter adı ya da slug; ardından veriyi yapıştır veya ekle]"
---

# /investigation-add

Açık soruşturma kaydına veri ekler. Belge partilerini yazılı çekme ölçütleriyle işler, öne çıkanları kayda geçirir, incelenen her belgeyi kapsama için kaydeder.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını yükle.
2. `internal-investigation` referans skill'ini yükle ve **Mod 2 (Veri ekle)** uygula.
3. Kurumsal e-posta, mesaj, cihaz, kamera ya da log verisi geldiyse ve kayıtta `kvkk_kontrol` boşsa işlemeden önce KVKK ve delil kontrolünü tamamla (KVKK m. 4, 5, 10; TBK m. 419; HMK m. 189/2).
4. İşlemden sonra öne çıkma oranını ve öne çıkan öğelerin listesini göster.
5. Veri bir kaynak listesi kalemini karşılıyorsa güncelleme için sor; kendiliğinden `tamam` işaretleme.
6. Gelen veri savunma tutanağıysa kayıttaki `savunma` alanını ve m. 26 sayacını güncelle.

## Örnekler

```
/employment-legal:investigation-add [matter adı]
[görüşme notunu yapıştır]
```

```
/employment-legal:investigation-add [matter adı]
[e-posta dışa aktarımını ekle]
```

> İğne bulma süreci, kayıt girdisi biçimi, oran kuralları ve kaynak listesi takibi
> `internal-investigation` referans skill'indedir — esaslı işe başlamadan önce yükle.

---

## /employment-legal:investigation-memo

---
name: investigation-memo
description: >
  Soruşturma kaydından iç soruşturma notunu yaz ya da güncelle — konu bazında
  bulgular, güvenilirlik değerlendirmesi, Türk hukuku çerçevesi (m. 25/II eşleşmesi,
  m. 19 savunma, m. 26 süre, TBK m. 417). Soruşturma ilk taslak için yeterince
  ilerlediğinde ya da yeni veri eklendikten sonra kullan.
argument-hint: "[matter adı]"
---

# /investigation-memo

Soruşturma kaydından notun ilk taslağını yazar ya da yeni veri eklendiğinde mevcut taslağı günceller.

## Talimat

1. `internal-investigation` referans skill'ini yükle ve **Mod 4 (Soruşturma notu)** uygula.
2. İlk taslakta: yüksek öncelikli kaynaklar açıksa, savunma alınmamışsa ya da m. 26 son günü yaklaşıyorsa en üstte uyar.
3. Güncellemede: yeniden yazmadan önce neyin değiştiğini göster.
4. Not A sınıfı dosyadır (avukat çalışma ürünü); `## Outputs`'taki gizlilik başlığıyla açılır. Başlık koruma yaratmaz — gizlilik notunu koru.
5. "Hukuki çerçeve" bölümündeki her madde atfını `tr_mevzuat_madde_getir` ile doğrula; çekilemeyen için "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" yaz.

## Örnekler

```
/employment-legal:investigation-memo [matter adı]
```

```
/employment-legal:investigation-memo [matter adı]
(not varsa günceller)
```

> Not yapısı, güvenilirlik çerçevesi ve güncelleme kuralları `internal-investigation`
> referans skill'indedir — esaslı işe başlamadan önce yükle.

---

## /employment-legal:investigation-open

---
name: investigation-open
description: >
  Yeni iç soruşturma dosyası aç — ön görüşmeyi yürütür, m. 26 süre sayacını ve savunma
  durumunu kurar, türe uygun kaynak listesini üretir ve kalıcı soruşturma kaydını
  oluşturur. Şikâyet, ihbar ya da iddia geldiğinde ve avukat soruşturma çalışma alanını
  kurmak istediğinde kullan.
argument-hint: "[iddianın kısa tarifi]"
---

# /investigation-open

Yeni bir iç soruşturma dosyası açar: ön görüşme, süre ve usul ön-kontrolü, kaynak listesi, kalıcı kayıt.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını yükle (yoksa önce `/employment-legal:cold-start-interview` öner).
2. `internal-investigation` referans skill'ini yükle ve **Mod 1 (Soruşturma aç)** uygula — önce ⏰ ÖN-KONTROL (İş K. m. 26 öğrenme tarihi, m. 19 savunma, TİS/disiplin usulü).
3. Aynı slug'la bir soruşturma varsa üzerine yazmadan önce uyar.
4. Açılış çıktısında şunları göster: klasör yolu, m. 26 son günü ("tartışmalı" notuyla), dosya sınıfı ayrımı (A — avukat çalışma ürünü / B — işveren delil dosyası), KVKK kontrolü gereken kaynaklar.

## Örnekler

```
/employment-legal:investigation-open
İzmir şubesindeki bir müdür hakkında psikolojik taciz şikâyeti; İK'ya dün e-postayla ulaştı.
```

```
/employment-legal:investigation-open
(skill ayrıntıları soracak)
```

> Ön görüşme soruları, gizlilik ayrımı, kaynak listeleri ve kayıt şablonları
> `internal-investigation` referans skill'indedir — esaslı işe başlamadan önce yükle.

---

## /employment-legal:investigation-query

---
name: investigation-query
description: >
  Açık bir soruşturma kaydına soru sor — tanıklar ne dedi, anlatımlar nerede
  çelişiyor, hangi boşluklar var, her konuda en güçlü delil ne, savunma ve m. 26
  süresi ne durumda. Avukat her girdiyi yeniden okumadan kayda soru sormak
  istediğinde kullan.
argument-hint: "[matter adı] [soru]"
---

# /investigation-query

Soruşturma kaydına karşı soruları cevaplar: tanık anlatımları, çelişkiler, boşluklar, konu bazında en güçlü delil, usul durumu.

## Talimat

1. `internal-investigation` referans skill'ini yükle ve **Mod 3 (Kayda soru sor)** uygula.
2. Her cevapta kayıt ID'lerini göster.
3. Kayıtta ilgili bilgi yoksa açıkça söyle — "Bu soruşturma kaydında ([N] girdi) [konu] hakkında bilgi görmedim" — ve boşluk olarak işaretlemeyi öner.
4. Usul sorularında (savunma, m. 26, açılış bildirimleri, KVKK kontrolü) tarihleri kayıttan ver; hesapladığın son günü "tartışmalı — içtihadı kontrol et" notuyla yaz.

## Örnekler

```
/employment-legal:investigation-query [matter adı]
Hakkında iddia olan kişi Aralık ayındaki ekip yemeği hakkında ne dedi?
```

```
/employment-legal:investigation-query [matter adı]
Şikâyetçinin ve hakkında iddia olanın anlatımları nerede çelişiyor?
```

```
/employment-legal:investigation-query [matter adı]
Neyi eksik? Savunma alındı mı, m. 26 için kaç iş günü kaldı?
```

> Sorgu süreci, atıf kuralları ve boşluk işaretleme şablonları `internal-investigation`
> referans skill'indedir — esaslı işe başlamadan önce yükle.

---

## /employment-legal:investigation-summary

---
name: investigation-summary
description: >
  Soruşturma notundan hedef kitleye özel özet yaz — İK, yönetim/YK, dış avukat ya da
  şikâyetçiye sonuç bildirimi. Notun tamamını görmemesi gereken bir kitleye sonucun
  iletilmesi gerektiğinde kullan.
argument-hint: "[matter adı] [kitle: ik / yonetim / dis-avukat / ilgili]"
---

# /investigation-summary

Soruşturma notundan kitleye uygun, sadeleştirilmiş özet üretir. İK özeti hukuki analiz içermez; yönetim özeti üst düzeydedir; dış avukat brifingi tam bağlamı taşır; ilgiliye bildirim yalnız sonuç ve önlemleri söyler.

## Talimat

1. `internal-investigation` referans skill'ini yükle ve **Mod 5 (Hedef kitle özeti)** uygula.
2. Henüz not yoksa önce notu yazmayı öner (`/employment-legal:investigation-memo`).
3. İK özetine avukat izlenimleri, güvenilirlik yöntemi ve hukuki risk analizi girmez; İK özetinin davada sunulabileceğini varsayarak olgusal yaz.
4. İlgiliye bildirimde başka kişilerin kişisel verisini ve tanık beyanlarını açma (KVKK m. 4/2-ç, İş K. m. 75/2).
5. Özet bir dış merciye (arabuluculuk, ihtarname cevabı, iş müfettişi, KVKK, savcılık) gidecekse referans skill'deki **sonuçlu işlem kapısını** uygula.

## Örnekler

```
/employment-legal:investigation-summary [matter adı] ik
```

```
/employment-legal:investigation-summary [matter adı] yonetim
```

```
/employment-legal:investigation-summary [matter adı] dis-avukat
```

> Kitleye göre ayıklama kuralları ve özet şablonları `internal-investigation` referans
> skill'indedir — esaslı işe başlamadan önce yükle.

---

## /employment-legal:leave-tracker

---
name: leave-tracker
description: >
  Açık izin ve raporları kanuni süre uyarıları ve karar noktaları için tarar
  (Türk hukuku) — hastalık/kaza bekleme süresi (İş K. m. 25/I), iş kazası SGK
  bildirimi (5510 m. 13), analık izni ve sonrası haklar (m. 74, m. 13/5),
  askerlik ve kanuni ödev (m. 31), uzun izin dönüşü İSG eğitimi. Yalnız
  eylem gerektiren izinleri gösterir ve nedenini söyler; durum panosu değildir.
  Haftalık ya da avukat hangi izinde yaklaşan süre olduğunu bilmek istediğinde
  kullan.
argument-hint: "[argüman yok — İK sisteminden ya da leave-register.yaml'dan çalışır]"
---

# /leave-tracker — İzin Süreleri Takibi

Kanuni saati işleyen tüm açık izinleri kontrol eder; yalnız karar ya da işlem gerektirenleri gösterir. Durum panosu değildir: ne yapmanız gerektiğini ve nedenini söyler.

## Talimat

1. `leave-tracker` ajanını yükle ve tam iş akışını çalıştır.
2. İK sistemi bağlı değilse ve `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` yoksa, avukattan izin listesini (tablo) yüklemesini ya da `/employment-legal:log-leave` ile tek tek kayıt eklemesini iste.
3. Uyarı yalnız eylem gerektiren izinler için; temiz izinler birer satırla özetlenir.
4. Her süre, `tr_mevzuat_madde_getir` ile çekilen maddeye dayanır; değişiklik notu taşıyan maddelerde (ör. 4857 m. 74 ve ek m. 2 — 2026 değişiklikleri) güncel metni esas al.

## Örnek

```
/employment-legal:leave-tracker
```

Haftalık çalıştır — Pazartesi sabahı için bir hatırlatıcı kur. Otomatik zamanlama ayrı bir entegrasyon gerektirir (takvim hatırlatıcısı, zamanlanmış görev vb.); Claude Code ajanları kendi kendini zamanlamaz.

---

## /employment-legal:log-leave

---
name: log-leave
description: >
  İzin kaydına yeni bir izin/rapor ekler (Türk hukuku) — süre takibini
  başlatmak için gereken asgari bilgiyle: hastalık ya da iş kazası raporu,
  analık izni, yarım çalışma ya da ücretsiz izin (m. 74), askerlik/kanuni ödev
  (m. 31), mazeret izni (ek m. 2), uzun ücretsiz izin. Bir çalışan izne ya da
  rapora çıktığında, takipçinin saatleri ilk günden izlemesi için kullan.
argument-hint: "[izni anlatın — çalışan/rol, izin türü, işyeri, başlangıç tarihi]"
---

# /log-leave — İzin Kaydı Ekle

`~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` dosyasına, süre takibini başlatacak asgari bilgiyle yeni kayıt ekler.

## Talimat

1. `company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → ayak izi, `## Systems` (İK sistemi), eskalasyon matrisi.

2. Aşağıdakilerin hepsini tek seferde sor — tek tek sorma:

   > İzin takibini kurmak için birkaç soru:
   >
   > - Çalışan adı ya da rolü (anonim olabilir)
   > - İşyeri (Türkiye dışındaysa ülke) ve işe giriş tarihi (kıdem → bildirim süresi ve bekleme süresi)
   > - İzin türü: hastalık raporu / iş kazası / analık (doğum öncesi-sonrası) / yarım çalışma ya da 6 aya kadar ücretsiz izin (m. 74) / süt izni / kısmi süreli çalışma talebi (m. 13/5) / askerlik veya kanuni ödev (m. 31) / mazeret izni (ek m. 2) / anlaşmalı ücretsiz izin
   > - Başlangıç tarihi; rapor varsa rapor bitiş tarihi
   > - Analıkta tahmini (ya da gerçek) doğum tarihi, çoğul gebelik mi, hekim onayıyla doğuma yakın çalışma talebi var mı
   > - İş kazasında kaza tarihi ve SGK'ya bildirildi mi (ne zaman)
   > - Beklenen dönüş tarihi (biliniyorsa)

3. Maddeleri `tr_mevzuat_madde_getir` ile çek ve ilk yaklaşan süreyi hesapla:

   | İzin türü | İlk süre | Dayanak |
   |---|---|---|
   | İş kazası | Kolluğa derhal; SGK'ya kazadan sonraki **3 iş günü** içinde (işveren kontrolü dışındaki yerde: öğrenmeden itibaren) | 5510 m. 13 |
   | Hastalık / kaza raporu | **Bekleme süresi sonu** = rapor başlangıcı + m. 17'ye göre bildirim süresi (kıdeme göre 2/4/6/8 hafta) + **6 hafta**; bu tarihten önce bu gerekçeyle bildirimsiz fesih hakkı doğmaz | 4857 m. 25/I, m. 17, m. 18/3-f |
   | Analık — doğum öncesi | Tahmini doğumdan **8 hafta** önce (çoğulda 10); hekim onayı ve işçinin isteğiyle doğuma 2 hafta kalana kadar çalışabilir, çalışılan süre doğum sonrasına eklenir | 4857 m. 74/1 |
   | Analık — doğum sonrası | Doğumdan itibaren **16 hafta**; erken doğumda kullanılamayan doğum öncesi süre eklenir; bitişte işçinin talebini al: yarım çalışma ücretsiz izni (ilk doğumda 60, ikincide 120, sonrakilerde 180 gün; çoğulda +30; engelli doğumda 360) ya da 6 aya kadar ücretsiz izin; süt izni çocuk 1 yaşına kadar günde 1,5 saat | 4857 m. 74/1, 74/2, 74/6, 74/7 |
   | Kısmi süreli çalışma talebi | İşçi en az **1 ay önce** yazılı bildirir; talep karşılanır; mecburi ilköğretim çağının başladığı tarihi izleyen ay başına kadar | 4857 m. 13/5 |
   | Askerlik / kanuni ödev | İki ayrı saat: (a) sözleşme ayrılıştan **2 ay** sonra (1 yılı aşan her yıl için +2 gün, toplam en çok 90 gün) işverence feshedilmiş sayılır — en az 1 yıl kıdem şartı; (b) ödev bitince işçinin **2 ay** içinde işe dönüş başvurusu | 4857 m. 31 |
   | Mazeret izni (ücretli) | Evlenme, evlat edinme, ana/baba/eş/kardeş/çocuk ölümü 3 gün; eşin doğumu **10 gün**; %70+ engelli ya da süreğen hastalıklı çocuk için yılda 10 güne kadar (bir ebeveyn) — kaydet, uyarı yok | 4857 ek m. 2 |
   | Uzun izin (6 aydan fazla) | Dönüşten önce İSG bilgi yenileme eğitimi | 6331 m. 17/4 |

   Kayıtta olmayan bilgi (işe giriş tarihi gibi) bekleme süresini etkiliyorsa hesaplama; boş bırak ve "eksik bilgi" diye işaretle. Aralıklı raporların bekleme süresinde toplanıp toplanmayacağı **tartışmalı — içtihadı kontrol et**.

4. Yeni kaydı `leave-tracker` ajanındaki kayıt biçimiyle `leave-register.yaml` dosyasına yaz; dosya yoksa oluştur. `kontrol_eden_kaynaklar` alanına çekilen maddelerin `citation` değerini yaz.

5. Tek satırla onayla:
   > "Kaydedildi. [Çalışan/Rol] — [İzin türü] — [İşyeri] — başlangıç [tarih]. İlk süre: [ne ve ne zaman] ([dayanak]). İzin takipçisi bu tarihi izleyecek."

## Örnekler

```
/employment-legal:log-leave
```

```
/employment-legal:log-leave
Kıdemli mühendis, İstanbul işyeri, 4 yıllık kıdem; bugün 20 günlük hastalık
raporu getirdi, daha önce de bu yıl iki kez rapor almıştı.
```

```
/employment-legal:log-leave
Muhasebe uzmanı, tahmini doğum 15 Mart, tek gebelik; hekim onayıyla doğuma
2 hafta kalana kadar çalışmak istiyor.
```

---

## /employment-legal:matter-workspace

---
name: matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkilin ya da dosyanın bağlamının diğerine sızmamasını
  sağlar; iş hukukunda işveren ve işçi tarafının aynı büroda bulunabilmesi nedeniyle
  çapraz okuma kapalı tutulur. Çok müvekkilli avukat "yeni matter", "matter değiştir",
  "matter'larımı listele", "matter'ı kapat" dediğinde ya da aktif matter'ı yönetmesi
  gerektiğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil ve dosya üzerinde çalışır. Matter çalışma alanı her dosyanın bağlamını diğerlerinden ayrı tutar. Bu skill o alanları yönetir.

## Alt komutlar

- `/employment-legal:matter-workspace new <slug>` — yeni matter oluştur, kısa ön görüşme yap, `matter.md` yaz
- `/employment-legal:matter-workspace list` — matter'ları durum ve aktiflik işaretiyle listele
- `/employment-legal:matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/employment-legal:matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/employment-legal/matters/_archived/` altına taşı; asla silme)
- `/employment-legal:matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünün dolu olduğunu teyit et. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli kurum içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/employment-legal:cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok."
2. `$ARGUMENTS`'ın ilk kelimesine göre dallan:
   - `new` → ön görüşme, `matters/<slug>/matter.md` yaz, `history.md` ve `notes.md` oluştur.
   - `list` → `matters/*/matter.md` dosyalarını tara, tablo bas, aktif olanı işaretle.
   - `switch` → uygulama CLAUDE.md'sindeki `Active matter:` satırını güncelle.
   - `close` → `matters/<slug>/` klasörünü `matters/_archived/<slug>/` altına taşı, kapanış tarihini `history.md`'ye yaz.
   - `none` → `Active matter:` satırını `none — practice-level context only` yap.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` değerleri şablondaki gibi kalır; diğer skill'ler bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/employment-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   ├── investigation-<slug>/   # iç soruşturma dosyaları (varsa)
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-isverenlik-fesih-2026`, `isci-ise-iade-x`, `xyz-ic-sorusturma`. Müvekkil gerçek adını slug'a koymak zorunda değilsin; takma ad kullanılabilir.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Sor: "Bu matter için çatışma kontrolü yapıldı mı?" Bu skill çatışma kontrolünü kendisi yapmaz ve başka matter'ların dosyalarını bu amaçla okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve avukata hatırlat.
3. Ön görüşme:
   - **Müvekkil ve taraf rolü** — temsil ettiğimiz taraf (işveren / işçi / kurum içi birim)
   - **Karşı taraf** — işveren, işçi(ler), alt işveren, özel istihdam bürosu (birden fazla olabilir)
   - **Matter türü** — işe alım | fesih danışmanlığı | işe iade / arabuluculuk | alacak hesabı | iç soruşturma | taciz-mobbing | sınıflandırma | toplu işçi çıkarma | yurt dışı genişleme | yönetmelik/politika | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (yüksek, çapraz bağlamda ek dikkat demektir)
   - **Kritik süre** — varsa: m. 26 son günü, fesih tebliğ tarihi (işe iade için bir aylık arabuluculuk süresi, İş K. m. 20/1), arabuluculuk son tutanak tarihi
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu
   - **Matter'a özel sapmalar** — ör. "müvekkil TİS'i 5 iş günü savunma süresi öngörüyor", "işçi tarafı: sulh alt sınırı müvekkil yazılı onayıyla"
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/employment-legal:matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar:

| Slug | Müvekkil | Taraf | Tür | Durum | Açılış | Aktif |
|---|---|---|---|---|---|---|

Aktif olanı `*` ile işaretle. `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

1. `matters/<slug>/matter.md` var mı bak; yoksa `new <slug>` öner.
2. `Active matter: <slug>` olarak güncelle.
3. Doğru matter'da olduğunu teyit etmesi için `matter.md` özetini göster (taraf rolü ve kritik süre dahil).

### `close <slug>`

1. `matters/<slug>/` var mı bak.
2. `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle.
3. `matters/<slug>/` → `matters/_archived/<slug>/` taşı.
4. Kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap.

`none`: yalnız `Active matter:` satırını `none — practice-level context only` yapar; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar
**Müvekkil:** [ad] — **Taraf rolü:** [işveren / işçi / kurum içi]
**Karşı taraf:** [ad(lar)]

## Matter türü
[tür — tek satır gerekçe]

## Kritik süreler
- [ör. m. 26 son günü: …; fesih tebliğ tarihi: …; arabuluculuk son tutanak: …]

## Ana olgular
[2-5 cümle; işyeri ve işçi sayısı, TİS durumu dahil]

## Matter'a özel sapmalar
- [ör. "Savunma süresi: TİS'e göre 5 iş günü."]

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
[matter.md dışında saklanmaya değer ilk bağlam]
```

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan; işveren ve işçi tarafını birlikte yürüten büroda **zorunlu**) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın sır saklama yükümlülüğünü (Av. K. m. 36) ve aynı büroda zıt tarafların bulunabilmesinden doğan çatışma riskini (m. 38) destekler.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş işveren dosyasında savunma süresini karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil. Saklama süresi büronun/şirketin politikasıdır (kişisel veride KVKK m. 4/2-d: işlendikleri amaç için gerekli süre kadar muhafaza).
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.

---

## /employment-legal:policy-drafting

---
name: policy-drafting
description: >
  İşyeri politikası / personel yönetmeliği bölümü taslağı (Türk hukuku) —
  çekirdek politika + gerektiğinde ülke, işyeri ya da TİS ekleri; dayanak
  maddeler (İş K., TBK m. 399 ve 417, 6331 İSG, KVKK aydınlatma) canlı çekilir,
  m. 22 esaslı değişiklik riski işaretlenir. "[konu] politikası hazırla",
  "şuna dair bir politikamız olmalı", "[konu] politikasını güncelle" denince ya
  da bir politika boşluğu adlandırıldığında kullan.
argument-hint: "[politika konusu — ör. 'uzaktan çalışma', 'taciz ve mobbing', 'yıllık izin']"
---

# /policy-drafting — Politika Taslağı

Türkiye için doğru olan bir politika, ayak izindeki başka bir ülke ya da TİS'li bir işyeri için eksik kalabilir. Bu skill tek bir çekirdek politika yazar; yalnız kuralın farklılaştığı yerde ek üretir. Personel yönetmeliği iş sözleşmesinin eki sayılabildiğinden (4857 m. 22/1) yazılan her cümle bir sözdür.

## Bağlamı yükle

`company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → ayak izi (ülkeler, işyerleri, TİS'ler), el kitabı/personel yönetmeliği yeri ve biçimi.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/employment-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Kapsam

- Politika ne için? Neden şimdi (kanuni zorunluluk, olay, büyüme, fark edilen boşluk)?
- Kime uygulanır (tüm çalışanlar, belirli işyerleri, alt işveren/geçici işçiler)?
- Yeni bir hak mı tanıyor, mevcut bir hakkı mı daraltıyor? Daraltma → Adım 5'teki m. 22 kontrolü zorunlu.

### 2. Mevzuat taraması

Konunun çıpa maddelerini `tr_mevzuat_madde_getir` ile çek; aşağıdaki tablo başlangıçtır:

| Konu | Çıpa (metinden doğrula) |
|---|---|
| Genel düzenleme yetkisi | TBK m. 399 — işveren işin görülmesi ve işyerindeki davranışlarla ilgili genel düzenleme ve özel talimat verebilir; işçi dürüstlük kurallarının gerektirdiği ölçüde uyar |
| Taciz, mobbing, kişiliğin korunması | TBK m. 417 — psikolojik ve cinsel tacizi önleme ve mağdurun daha fazla zarar görmemesi için önlem; 4857 m. 24/II-b, d (işçinin haklı fesih hâlleri), m. 25/II-c (işverenin haklı fesih hâli) |
| İş sağlığı ve güvenliği | 6331 m. 4 (işverenin genel yükümlülüğü, risk değerlendirmesi), m. 16 (bilgilendirme), m. 17 (eğitim), m. 19 (çalışanın yükümlülükleri) |
| Kişisel veri, izleme (e-posta, kamera, cihaz) | 6698 m. 4 (ölçülülük), m. 5–6 (hukuki sebep, özel nitelikli veri), m. 10 (aydınlatma) |
| Çalışma süresi, fazla çalışma | 4857 m. 41, m. 63, m. 68, m. 69 |
| Yıllık izin | 4857 m. 53–60 (bölünme m. 56; izin kayıt belgesi m. 56) |
| Analık, ebeveynlik, mazeret izni | 4857 m. 74, m. 13/5, ek m. 2 |
| Uzaktan çalışma | 4857 m. 14 (yazılı sözleşme, zorunlu içerik, İSG bilgilendirmesi) + Bakanlık yönetmeliği |
| Disiplin, ücret kesme cezası | 4857 m. 38 (yalnız TİS/iş sözleşmesindeki sebepler; ayda 2 gündelik sınırı), m. 19 (savunma), m. 25 |
| Eşit davranma | 4857 m. 5; 6701 m. 3, m. 6 |

Konunun mevzuatta özel karşılığı yoksa (ör. kıyafet kuralı) yalnız TBK m. 399 ölçülülük ve KVKK boyutunu kontrol et, bu adımı kısa geç.

Ayak izinde Türkiye dışı ülke varsa her biri için ayrı ek gerekip gerekmediğine bak; kural ezberden yazılmaz: AB `eu_search_eu_law(query="work-life balance for parents and carers")`, İngiltere `uk_search_legislation`, Almanya `de_gesetz_ara`, Hollanda `nl_search_legislation`, Azerbaycan `az_search_acts(query="Əmək Məcəlləsi", types=[107])`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

### 3. Çekirdek politikayı yaz

Tek politika, her yerde geçerli; çalışan avukatsız anlayabilmeli. Yapı:
- **Amaç** (tek cümle)
- **Kapsam** (kime)
- **Kural** (ne zorunlu / serbest / yasak)
- **Süreç** (nasıl talep edilir, kim onaylar, ihlalde ne olur — disiplin yaptırımı varsa m. 38 ve savunma hakkı)
- **Kişisel veri** (politika veri işliyorsa aydınlatma metnine atıf)
- **Sorular** (kime sorulur)

Kaçın: "işbu", "mezkûr", iç içe istisnalar. Bu bir personel politikasıdır, sözleşme metni değil.

### 4. Ekler (yalnız farklılık varsa)

```markdown
### [Ülke / işyeri / TİS] Eki

[Ülke/işyeri/TİS kapsamındaki] çalışanlara çekirdek politikaya ek olarak / yerine şunlar uygulanır:
- [Somut fark]
- [Dayanak — yalnız araçla doğrulanmışsa]
```

Ekler kısa: yalnız farklı olan; çekirdeği tekrar etme. TİS'li işyerinde politikanın TİS hükümleriyle çatışıp çatışmadığını ayrıca kontrol et.

### 5. Çapraz kontrol

- **Esaslı değişiklik (4857 m. 22):** politika mevcut çalışma koşullarını (iş sözleşmesi, personel yönetmeliği, işyeri uygulaması) işçi aleyhine esaslı biçimde değiştiriyor mu? Öyleyse yazılı bildirim ve işçinin 6 iş günü içinde yazılı kabulü gerekir; kabul etmeyeni bağlamaz; değişiklik geçmişe etkili olamaz (m. 22/2). Neyin "esaslı" olduğu **tartışmalı — içtihadı kontrol et**.
- **Söz kontrolü:** şirketin vermek istemediği bir hakkı vaat ediyor mu? İşyeri uygulamasına dönüşebilecek tekrar eden ödemeler/izinler var mı?
- **Mevcut el kitabıyla çatışma:** aynı konuyu düzenleyen başka bölüm var mı?
- **KVKK:** yeni bir veri işleme getiriyorsa aydınlatma metni güncellenmeli (6698 m. 10).
- **İSG:** risk değerlendirmesini değiştiriyorsa bilgilendirme ve eğitim (6331 m. 16, m. 17).

### 6. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["399","417"])
tr_mevzuat_madde_getir(number="4857", madde_no=["22","38"])
tr_mevzuat_madde_getir(number="6331", madde_no=["4","16","17","19"])
tr_kurum_karari_ara(kurum="kvkk", query="çalışan e-posta kamera izleme")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="personel yönetmeliği esaslı değişiklik işçi aleyhine", date_from="2022-01-01")
```

Sonuç azsa sessizce doldurma; seçenekleri sun. Atıf etiketleri: `[ArthurLegal TR — 4857 m. 22 — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`.

## Çıktı

```markdown
# [Politika Adı]

## Çekirdek Politika
[Tam metin]

## Ekler
### [Ülke / işyeri / TİS 1]
[Ek]

---

## Taslak notları (dahili — yönetmeliğe eklemeden önce çıkar)
- **Mevzuat taraması:** [çekilen maddeler; farklılık çıkan ülke/işyeri/TİS]
- **m. 22 değerlendirmesi:** [aleyhe esaslı değişiklik yok / var — yazılı kabul süreci]
- **Mevcut el kitabıyla çatışma:** [yok / liste]
- **KVKK / İSG etkisi:** [aydınlatma, bilgilendirme, eğitim]
- **Değişen mevzuat:** [madde notlarında görülen yakın değişiklikler]
- **Tartışmalı noktalar:** [liste]
- **Gözden geçirme sıklığı:** [yıllık / X olunca]
```

> **Taslak, yürürlükteki politika değil.** Bu metin avukat incelemesi için bir yardımcıdır. Personel politikası yayımlamak hukuki sonuç doğurur: iş sözleşmesinin eki sayılabilir, aleyhe değişiklikler m. 22'ye tabidir, ücret/izin/disiplin hükümleri işveren aleyhine yorumlanabilir. Yetkili bir avukat inceleyip sorumluluğu üstlenmeden yayımlama ve dağıtma.

## Devir

Politika onaylanınca `/employment-legal:handbook-updates` mevcut el kitabıyla karşılaştırır ve değişiklikleri işaretler.

## Bu skill ne yapmaz

- Politikayı onaylamaz; taslak yazar, insan onaylar.
- Çalışanlara duyurmaz; bu İK süreci (yazılı tebliğ ve gerekiyorsa kabul imzası İK'da).
- Ayak izi dışındaki ülkeleri kapsamaz; ayak izi genişlerse yeniden çalıştır.

---

## /employment-legal:termination-review

---
name: termination-review
description: >
  Fesih incelemesi (Türk iş hukuku) — fesih türünü (geçerli sebep İş K. m. 18,
  haklı sebep m. 25, süreli fesih m. 17, ikale) belirler, yüksek risk
  bayraklarını tarar, süreleri (haklı fesihte 6 iş günü, işe iadede 1 ay
  arabuluculuk) kontrol eder; ihbar-kıdem-izin ücreti kalemlerini, ibraname
  (TBK m. 420) ve arabuluculuk anlaşması yolunu ve fesih günü kontrol listesini
  çıkarır. "Bu işçiyi çıkarabilir miyiz", "fesih incelemesi", "işten çıkarma",
  "işe iade riski" denince ya da bir fesih senaryosu anlatıldığında kullan.
argument-hint: "[feshi anlatın ya da belgeleri ekleyin]"
---

# /termination-review — Fesih İncelemesi

Çoğu fesih sorunsuzdur; birkaçı hazır bir işe iade ya da alacak davasıdır. Bu skill, karar kesinleşmeden önce ikinci türü yakalar. Kural ezberden söylenmez: atıf yapılan her madde `tr_mevzuat_madde_getir` ile çekilir; değişen tutarlar (kıdem tavanı, asgari ücret) her incelemede teyit edilir.

## ⏰ ÖN-KONTROL — Süre (her çalıştırmada)

| Durum | Süre | Dayanak |
|---|---|---|
| İşveren ahlak ve iyiniyet kurallarına aykırılık nedeniyle derhal fesih | Öğrenmeden itibaren **6 iş günü**; her hâlde fiilden itibaren **1 yıl** (işçi maddi çıkar sağladıysa 1 yıl uygulanmaz) | 4857 m. 26 |
| İşçi işe iade isteyecek | Fesih bildiriminin tebliğinden itibaren **1 ay** içinde arabulucuya başvuru; son tutanaktan itibaren **2 hafta** içinde dava | 4857 m. 20/1 |
| Toplu işçi çıkarma | Sendika temsilcileri, bölge müdürlüğü ve İŞKUR'a en az **30 gün** önce yazılı bildirim; fesihler bölge müdürlüğüne bildirimden 30 gün sonra hüküm doğurur | 4857 m. 29 |
| SGK işten ayrılış bildirimi | Sözleşmenin sona ermesinden itibaren en geç **10 gün** | 5510 m. 9 |
| İbraname | Sözleşmenin sona ermesinden **en az 1 ay sonra** | TBK m. 420/2 |

6 iş günü süresinde ≤ 2 gün kaldı → 🔴 ACİL. "Öğrenme"nin feshe yetkili kişi/organın öğrenmesi olarak arandığı yerleşik uygulamadır — içtihadı kontrol et. Süre kaçtıysa haklı fesih yerine geçerli sebep + bildirim süreli fesih yolunu değerlendir.

## Destination check

- **Müvekkile / İK'ya fesih notu** → profilin `## Outputs` bölümündeki işveren tarafı fesih notu başlığı ("AVUKATLIK K. m. 36 – DAHİLİ"; sır saklama: Av. K. m. 36)
- **Yöneticinin fesih görüşmesi konuşma metni** → hukuki değerlendirme ve risk notları çıkarılır
- **İşçiye tebliğ edilecek fesih bildirimi** → "TASLAK"; avukat onayından sonra
- **Arabulucuya / karşı tarafa gidecek metin** → iç hesap, risk puanı ve strateji çıkarılır

## ADIM 0 — Taraf ve çıkar çatışması

- [ŞİRKET ADI] işveren mi, işçi mi? Aynı işte menfaati zıt tarafa avukatlık etmiş avukat işi reddetmek zorundadır (Av. K. m. 38/1-b). Çatışma kontrolü yapılmadan devam etme.
- İşveren tarafı → aşağıdaki akış. İşçi tarafı → en sondaki **İşçi tarafı varyantı**.

## Bağlamı yükle

`company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → fesih tetikleyicileri, yüksek risk bayrakları, ayrılış paketi pratiği, eskalasyon matrisi, `## Outputs` ve `## Who's using this`.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/employment-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Temel olgular

| Soru | Neden önemli |
|---|---|
| İşçi (ad ya da unvan takma adı), işin yapıldığı yer | Yurt dışındaysa uygulanacak hukuk (aşağıda) |
| İşyerindeki ve aynı işkolundaki işyerlerinde toplam işçi sayısı | 30 eşiği iş güvencesi için toplam sayıyla belirlenir (m. 18/1, m. 18/4) |
| Kıdem (işe giriş tarihi) | 6 ay eşiği; ihbar süresi; kıdem tazminatı |
| Sözleşme türü | Belirsiz / belirli süreli (m. 11); iş güvencesi belirsiz süreliye uygulanır |
| Pozisyon | İşletmenin bütününü sevk ve idare eden işveren vekili mi (m. 18 son fıkra) |
| Fesih nedeni | Yeterlilik / davranış / işletme gerekleri / haklı neden / anlaşma |
| Sendika üyeliği, temsilcilik, TİS | m. 18/3-a,b; TİS'teki disiplin usulü |
| Aynı dönemde başka çıkarma | Toplu çıkarma eşiği (m. 29/2) |
| Planlanan tarih | Süreler, izin ve rapor çakışması |

### 2. Fesih türünü belirle

- **Geçerli sebep (m. 18):** işçinin yeterliliği, davranışı ya da işletme/işyeri/iş gerekleri. Bildirim yazılı, sebep açık ve kesin (m. 19/1); davranış ya da verim nedeniyle fesihte önce savunma alınır (m. 19/2; m. 25/II hâlleri hariç). Savunma şartının iş güvencesi dışındaki işçiye de uygulanıp uygulanmadığı **tartışmalı — içtihadı kontrol et**; şüphede savunma al. İspat yükü işverendedir (m. 20/2). Bildirim süresine uyulur ya da ücreti peşin ödenir (m. 17).
- **Haklı sebep (m. 25):** I sağlık, II ahlak ve iyiniyet kurallarına aykırılık, III zorlayıcı sebep, IV gözaltı/tutukluluğun bildirim süresini aşması. II için m. 26 süresi işler.
- **İş güvencesi dışındaki işçinin süreli feshi (m. 17):** fesih hakkı kötüye kullanılırsa bildirim süresinin üç katı tutarında tazminat (m. 17/6).
- **Esaslı değişikliğin reddi üzerine fesih (m. 22/1):** geçerli nedenin yazılı açıklanması ve bildirim süresi şart.
- **İkale (bozma sözleşmesi):** kanunda düzenlenmemiş, karşılıklı anlaşmaya dayanan uygulama kavramı. İşveren önerdiyse işçiye "makul yarar" sağlanması ve irade sakatlığı denetimi yerleşik uygulamadır — **tartışmalı, içtihadı kontrol et** (sorgu aşağıda).
- **İş K. kapsamı dışındaki işçi** (m. 4 istisnaları, ör. ev hizmetleri): TBK hükümleri; ör. haklı sebep olmaksızın derhal fesihte TBK m. 438.

### 3. Yüksek risk bayrakları (en önemli adım)

Eklenti ayarındaki bayrakların hepsini işaretle. Varsayılan set:

| Bayrak | Neden riskli | Kontrol | Dayanak |
|---|---|---|---|
| Yakın tarihli şikâyet / resmî başvuru | Geçerli sebep sayılmaz; misilleme algısı | İşveren aleyhine idari/adli makama başvurdu ya da sürece katıldı mı? | m. 18/3-c |
| Sendika üyeliği / temsilcilik | Geçerli sebep sayılmaz; sendikal tazminat | Üyelik, faaliyet → 6356 s.K. ilgili maddesini çek | m. 18/3-a,b |
| Gebelik, doğum, aile yükümlülükleri, din, cinsiyet, engellilik vb. | Geçerli sebep sayılmaz; 4 aya kadar ücret tutarında ayrımcılık tazminatı + yoksun kalınan haklar; ispat yükü kayar | Yakın zamanda bildirilen gebelik, izin talebi, sağlık durumu | m. 5/6-7; m. 18/3-d; 6701 m. 3, 6 |
| Analık izni ya da raporlu bekleme süresinde devamsızlık | Geçerli sebep sayılmaz; hastalıkta bildirimsiz fesih hakkı ancak bildirim süresi + 6 hafta aşılınca doğar | Rapor tarihleri, kıdem → `/employment-legal:leave-tracker` | m. 18/3-e,f; m. 25/I; m. 74 |
| Savunma alınmadı | Davranış/verim nedenli fesih yapılamaz | Yazılı davet, makul süre, tutanak | m. 19/2 |
| Sebep yazılı ve açık değil | Geçersizlik | Bildirim metni | m. 19/1 |
| Zayıf belge ("neden şimdi?") | İspat yükü işverende | Uyarılar, performans kayıtları; yakın tarihli olumlu değerlendirme, prim, terfi çelişkisi | m. 20/2 |
| Emsal sorunu | Eşit davranma ihlali | Aynı davranışı yapan başkası çıkarılmıyor mu? | m. 5 |
| İç prosedür sözü | Sözleşmesel usul ihlali | TİS, personel yönetmeliği, iş sözleşmesindeki disiplin aşamaları izlendi mi? | yerleşik uygulama — kontrol et |
| Ödenmemiş ücret / fazla çalışma | İşçinin haklı fesih hakkı ve alacak davası | Bordro, puantaj → `/employment-legal:wage-hour-qa` | m. 24/II-e; m. 34 |
| Mobbing / taciz iddiası | TBK m. 417 sorumluluğu; basın riski | Açık şikâyet var mı → profil eskalasyonu | TBK m. 417 |
| İşletmesel karar | Feshin son çare olması, tutarlılık, keyfilik denetimi | İşletme kararı belgelendi mi, kadro gerçekten kaldırıldı mı? | yerleşik uygulama — içtihadı kontrol et |
| Toplu çıkarma eşiği | Usul ihlali; m. 18-21'i dolanmak yasak | 1 ay içindeki çıkarmaların toplamı | m. 29 |
| Alt işveren işçisi | Asıl işverenle birlikte sorumluluk, muvazaa | → `/employment-legal:worker-classification` | m. 2 |

**Herhangi bir bayrak 🔴 → fesihten ÖNCE profilin eskalasyon matrisine göre onay.** Sonra değil.

### 4. İşe iade riskinin sonucu

İş güvencesi kapsamı: 30+ işçi, 6 ay kıdem, belirsiz süreli sözleşme, işveren vekili istisnası (m. 18). Geçersizlik kararında (m. 21): işveren işçiyi 1 ay içinde işe başlatır; başlatmazsa en az 4, en çok 8 aylık ücret tutarında tazminat; kesinleşmeye kadar en çok 4 aylık boşta geçen süre ücreti ve diğer haklar; işçi kesinleşen kararın tebliğinden itibaren 10 iş günü içinde başvurmazsa fesih geçerli sayılır (m. 21/6). Arabuluculukta işe başlatma anlaşması işe başlatma tarihini, boşta geçen süre alacağını ve işe başlatmama tazminatını parasal olarak içermek zorundadır (m. 21/7). Bu hükümler sözleşmeyle değiştirilemez.

### 5. Parasal kalemler (hesap iskeleti)

```
İhbar süresi (m. 17/2, asgari): <6 ay → 2 hf | 6 ay–1,5 yıl → 4 hf | 1,5–3 yıl → 6 hf | 3 yıl+ → 8 hf
İhbar tazminatı  = giydirilmiş günlük ücret × bildirim süresi (gün)          [m. 17/4, m. 17/7]
Kıdem tazminatı  = giydirilmiş son brüt ücret (tavanla sınırlı) × 30 gün × hizmet yılı (küsurat orantılı)  [1475 m. 14]
Kıdem tavanı     = güncel tutarı teyit et (dönemsel güncellenir)
Yıllık izin ücreti = kullanılmayan izin günü × sözleşmenin sona erdiği tarihteki ücret  [m. 59/1]
Kötüniyet (iş güvencesi dışı) = 3 × bildirim süresi ücreti                    [m. 17/6]
```

- Kıdem doğuran hâller 1475 m. 14'te sayılıdır: işveren feshi (ahlak ve iyiniyet hâlleri hariç), işçinin haklı feshi, muvazzaf askerlik, emeklilik/yaşlılık aylığı, yaş dışındaki şartların tamamlanması, kadının evlenmeden itibaren 1 yıl içinde ayrılması, ölüm. 1475'in yalnız m. 14'ü yürürlüktedir (4857 m. 120); m. 14'teki eski madde atıflarının 4857'deki karşılıklarla okunduğu yerleşik uygulamadır. Bir yılı doldurmayan çalışmada kıdem doğmadığı da yerleşik uygulamadır — teyit et.
- Sona ermede ücret ve para ile ölçülebilen tüm menfaatler tam ödenir (m. 32/6); kıdem gecikirse mevduata uygulanan en yüksek faiz (1475 m. 14).
- Bildirim süresi içinde günde en az 2 saat ücretli iş arama izni (m. 27); bildirim süresi yıllık izinle iç içe giremez (m. 59/2).
- İşsizlik ödeneği fesih nedenine bağlıdır (4447 m. 51; madde hâlâ 1475 numaralarına atıf yapar) → SGK çıkış kodu doğru seçilmeli. İkalenin işsizlik ödeneğine etkisi **tartışmalı** — SGK/İŞKUR uygulamasını ve içtihadı kontrol et.
- Her tutar satırına: `[doğrula — avukat/uzman kontrolünden geçmeden müvekkile verilmez]`.

### 6. Ayrılış paketi: ikale, ibraname, arabuluculuk anlaşması

ABD'deki "kıdem ödemesi + feragat (release)" kurgusunun Türk karşılıkları:

- **İbraname (TBK m. 420/2):** yazılı; sözleşmenin sona ermesinden en az 1 ay sonra; alacağın türü ve miktarı açık; ödeme hak tutarına göre noksansız ve banka aracılığıyla. Eksik unsur → kesin hükümsüz. Gerçek tutarı içermeyen belge yalnız ödenen miktar kadar makbuz hükmündedir (m. 420/3). **Fesih günü imzalatılan ibranameye güvenme.**
- **İkale + ek ödeme:** yazılı protokol; ödenecek kalemler tek tek; makul yarar ve irade sakatlığı riski (yukarıda).
- **Arabuluculuk anlaşması:** iş alacakları ve işe iade davalarında arabuluculuk dava şartıdır (7036 m. 3/1). Taraflar ve avukatları ile arabulucunun imzaladığı anlaşma belgesi ilam niteliğindedir (6325 m. 18/4); anlaşılan hususlar hakkında dava açılamaz (6325 m. 18/5). Anlaşılan kalemleri ve tutarları tek tek yaz; genel "tüm haklardan feragat" ifadesinin kapsamı **tartışmalı — içtihadı kontrol et**.
- **Gizlilik / karalamama klozu:** yalnız işçi aleyhine konan ceza koşulu geçersizdir (TBK m. 420/1) → karşılıklı kur.
- **Rekabet yasağı varsa:** işveren haklı sebep olmaksızın feshederse yasak sona erer (TBK m. 447/2).
- *Karşılaştırmalı not:* ABD'de 40 yaş üstü işçi için kanuni düşünme/cayma süreleri vardır; Türk hukukunda bunun karşılığı TBK m. 420'nin 1 aylık bekleme şartı ve arabuluculuk anlaşmasıdır.

### 7. Belge kontrolü

Uyarılar, savunma tutanakları, performans kayıtları tutarlı bir hikâye anlatıyor mu? Gerekçeyle çelişen yazılı bir şey (yakın tarihli olumlu değerlendirme, prim, terfi) var mı? "Bir yıldır düşük performans varsa ne değişti?" sorusunun cevabı yazılı olmalı.

### 8. Yurt dışında çalışan işçi

Uygulanacak hukuk: tarafların seçtiği hukuk, işçinin mutad işyeri hukukunun emredici asgari koruması saklı kalmak üzere (MÖHUK 5718 m. 27). Yabancı kural ezberden yazılmaz: AB `eu_search_eu_law(query="collective redundancies")`; İngiltere `uk_search_legislation`; Almanya `de_gesetz_ara`; Azerbaycan `az_search_acts(query="Əmək Məcəlləsi", types=[107])`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

### 9. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="4857", madde_no=["17","18","19","20","21","25","26"])
tr_mevzuat_madde_getir(number="1475", madde_no="14")
tr_mevzuat_madde_getir(number="6098", madde_no=["420","447"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="feshin son çare olması ilkesi işletmesel karar", date_from="2022-01-01")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="ikale makul yarar irade fesadı", date_from="2022-01-01")
tr_ictihat_semantik_ara(initial_keyword="savunma alınmadan fesih", query="iş güvencesi dışındaki işçide savunma zorunluluğu")
```

Daire dağılımı değişebilir; sonuç ince ise `chamber` boş bırakıp tekrar dene. Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Atıf etiketi: `[ArthurLegal TR — 4857 m. X — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`.

## Çıktı

Eklenti ayarında örnek fesih notu varsa onun biçimini izle; yoksa:

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Fesih İncelemesi — [Unvan/takma ad] — [Tarih]

## ⚠️ İnceleyen notu
- **Fesih türü:** [Geçerli m. 18 / Haklı m. 25 / Süreli m. 17 / İkale]
- **Süre:** [6 iş günü sonu GG.AA.YYYY / işe iade başvuru penceresi] 🔴/🟠/🟡
- **İş güvencesi:** [kapsamda / dışında — gerekçe]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) — [madde sayısı, içtihat sayısı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]
- **Eskalasyon:** [yok / [isim] — hangi bayrak]

## Sonuç
[Devam edilebilir / Önce X düzeltilmeli / Dur — tek cümle neden]

## Yüksek risk bayrakları
[Her bayrak: ✅ temiz ya da 🔴 BAYRAK + ayrıntı]

## İşe iade riski
[Kapsam + olası parasal sonuç aralığı]

## Parasal kalemler
[İhbar, kıdem (tavan teyidi), yıllık izin, diğer — formül + girdiler + doğrula etiketi]

## Ayrılış paketi
[İkale / ibraname zamanlaması / arabuluculuk anlaşması kalemleri]

## Belgeler
[Değerlendirme, eksikler]

## Karar
[Devam / Değişikliklerle devam / Bekle — eskalasyon]

### Fesih günü kontrol listesi
- [ ] Yazılı fesih bildirimi, sebep açık ve kesin (m. 19/1); tebliğ kanıtı
- [ ] Savunma tutanağı (davranış/verim nedenli fesihte, m. 19/2)
- [ ] Bildirim süresi ya da peşin ihbar ücreti (m. 17); iş arama izni planı (m. 27)
- [ ] Son ücret, yıllık izin ücreti, kıdem — banka yoluyla (m. 32, m. 59, 1475 m. 14)
- [ ] SGK işten ayrılış bildirimi 10 gün içinde, doğru çıkış kodu (5510 m. 9; 4447 m. 51)
- [ ] Çalışma belgesi (m. 28)
- [ ] Zimmet iadesi, sistem erişiminin kapatılması, kişisel verilerin saklama süresi
- [ ] İbraname gerekiyorsa en erken sona ermeden 1 ay sonra (TBK m. 420)
```

## Sonuç doğuran işlem kapısı (işçinin işine son verme)

"Devam edilebilir" ya da hazır kontrol listesi üretmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> İşten çıkarma işe iade, ayrımcılık, kötüniyet ve işçilik alacağı davalarına yol açabilir. Bu feshi bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: işçi, işyeri ve işçi sayısı, kıdem, fesih nedeni ve tarihi; çıkan her bayrak ve ayrıntısı; süre hesabı; parasal kalemler ve hangi kaynaktan çekildiği; ayrılış paketi önerisi; açık sorular; ters gidebilecek şey (bu olguların desteklediği dava teorisi); avukata sorulacaklar (fesih temiz mi, önce savunma/belge mi gerekir, arabuluculuk anlaşması nasıl kurulmalı). Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan "Devam edilebilir" yazma; avukat incelemesi için "TASLAK" işaretli çıktı serbest.

## İşçi tarafı varyantı

[ŞİRKET ADI] işçiyse: (1) tebliğ tarihini sabitle → işe iade için 1 aylık arabuluculuk penceresi (m. 20/1); alacaklar için zamanaşımı 5 yıl (m. 32/8; ek m. 3); arabuluculuk süresince zamanaşımı durur ve hak düşürücü süre işlemez (7036 m. 3/17). (2) Alacak kalemlerini `/employment-legal:wage-hour-qa` ile hesapla; hesap doğru olmadan başvurma (profil uyarısı). (3) İmzalatılmış ibraname varsa TBK m. 420 şartlarıyla test et. (4) İlk arabuluculuk toplantısına mazeretsiz katılmamanın masraf ve vekâlet ücreti sonucu vardır (7036 m. 3/12).

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu incelemenin sonucuna göre uyarla (fesih bildirimi taslağı, eskalasyon, ek olgu, bekle-izle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Fesih kararını vermez; kararı denetler.
- Fesih görüşmesini yapmaz.
- Kural ya da tutarı ezberden vermez; her madde araçtan, her tutar güncel kaynaktan.
- Dava çıkmayacağını garanti etmez; bariz sorunları yakalayarak riski azaltır.

---

## /employment-legal:wage-hour-qa

---
name: wage-hour-qa
description: >
  Ücret, çalışma süresi ve iş hukuku soru-cevabı (Türk hukuku) — ücretin
  ödenmesi, asgari ücret, fazla çalışma ve fazla sürelerle çalışma, ara
  dinlenmesi, gece çalışması, hafta tatili, genel tatil, yıllık izin,
  zamanaşımı ve alacak hesabı; kontrol eden kural canlı çekilip atıfla verilir,
  ezberden söylenmez. "Fazla mesai ödemek zorunda mıyız", "kural ne", "izin kaç
  gün", "alacağı hesapla" ya da herhangi bir iş hukuku sorusunda kullan.
argument-hint: "[soru]"
---

# /wage-hour-qa — Ücret ve Çalışma Süresi Soru-Cevap

"Duruma göre değişir" doğru ama işe yaramaz. Bu skill soruya, kontrol eden maddeyi canlı çekip atıfla cevap verir ve sorunun insan muhakemesi gerektirecek kadar sınırda olduğunu açıkça söyler. Tutarlar (asgari ücret, kıdem tavanı, faiz oranları) dönemsel değişir; hiçbiri sabit yazılmaz.

## Bağlamı yükle

`company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → yargı çevresi ayak izi, [ŞİRKET ADI] tarafı (işveren/işçi), TİS bilgisi.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/employment-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Hangi hukuk, hangi rejim?

- İş nerede yapılıyor? Türkiye dışındaysa uygulanacak hukuk MÖHUK 5718 m. 27 (hukuk seçimi + mutad işyeri emredici asgari koruması).
- İşçi 4857 kapsamında mı? m. 4 istisnaları (ör. ev hizmetleri, 50 ve daha az işçili tarım işyerleri, sporcular) → TBK hizmet sözleşmesi hükümleri. Basın ve deniz iş ilişkileri ayrı kanunlara tabidir — ilgili kanunu `tr_mevzuat_ara` ile bul.
- TİS var mı? TİS ve iş sözleşmesi kanuni asgarileri işçi lehine artırabilir.

### 2. Kuralı çek, sonra söyle

Önce `tr_mevzuat_madde_getir` ile maddeyi çek, sonra tek paragrafta atıfla söyle. Sık soruların çıpaları (4857 s.K.):

| Konu | Çıpa | Kural özeti (metinden doğrula) |
|---|---|---|
| Ücretin ödenmesi | m. 32 | Türk parası, işyerinde ya da bankada; en geç ayda bir; sona ermede tam ödeme (m. 32/6); ücret alacağında zamanaşımı 5 yıl (m. 32/8) |
| Gecikme | m. 34 | Ödeme gününden itibaren 20 gün içinde ödenmezse işçi çalışmaktan kaçınabilir; gününde ödenmeyen ücrete mevduata uygulanan en yüksek faiz |
| Ücretin saklı kısmı | m. 35 | Aylık ücretin dörtte birinden fazlası haczedilemez/devredilemez (nafaka saklı) |
| Ücret hesap pusulası | m. 37 | Her ödemede ekler ve kesintiler ayrı ayrı gösterilir |
| Ücret kesme cezası | m. 38 | Yalnız TİS/iş sözleşmesinde gösterilen sebeplerle; ayda 2 gündeliği aşamaz; derhal sebebiyle bildirilir |
| Asgari ücret | m. 39 | Komisyonca en geç iki yılda bir belirlenir, RG'de yayımlanır → güncel tutarı teyit et (`tr_resmi_gazete_tara`) |
| Haftalık çalışma süresi | m. 63 | En çok 45 saat; anlaşmayla günde 11 saati aşmadan farklı dağıtım; denkleştirme 2 ay (TİS ile 4 aya kadar; turizmde ayrı) |
| Fazla çalışma | m. 41 | 45 saati aşan çalışma → saat ücreti %50 zamlı; sözleşmeyle 45'in altında süre varsa fazla sürelerle çalışma → %25 zamlı; işçi isterse 1 s 30 dk / 1 s 15 dk serbest zaman (6 ay içinde); işçinin onayı gerekir; yılda en çok 270 saat |
| Ara dinlenmesi | m. 68 | 4 saate kadar 15 dk; 4–7,5 saat 30 dk; 7,5 saat üstü 1 saat; çalışma süresinden sayılmaz |
| Gece çalışması | m. 69 | 7,5 saati geçemez (sayılı sektörlerde yazılı onayla istisna); gece çalışmasında fazla çalışma yapılamaz (m. 41/6) |
| Çalışma süresinden sayılanlar | m. 66 | Hazır bekleme, görevle başka yere gönderilme, süt izni vb. |
| Hafta tatili | m. 46 | 7 günlük dilimde kesintisiz en az 24 saat; çalışılmayan hafta tatili günü ücreti tam ödenir |
| Genel tatil | m. 47 | Çalışılmazsa o günün ücreti tam; çalışılırsa ayrıca bir günlük ücret |
| Yıllık izin | m. 53–60 | 1–5 yıl (5 dahil) en az 14 gün; 5 yıldan fazla 15 yıldan az en az 20 gün; 15 yıl (dahil) ve fazlası en az 26 gün; 18 yaş ve altı ile 50 yaş ve üstü en az 20 gün; vazgeçilemez; bölünmesi tarafların anlaşmasıyla, bir bölüm en az 10 gün (m. 56); izin ücreti izinden önce peşin (m. 57); sona ermede kullanılmayan izin son ücretle ödenir (m. 59) |
| Zamanaşımı | m. 32/8; ek m. 3 | Ücret 5 yıl; yıllık izin ücreti, kıdem, ihbar, kötüniyet ve eşit davranmama tazminatı 5 yıl; izin ücretinde zamanaşımı sözleşmenin sona ermesinden başlar (m. 59/1) |

ABD'deki "muaf (exempt) çalışan" testinin (maaş eşiği + görev testi) Türk hukukunda karşılığı yoktur. Benzer sorular Türkiye'de şöyle sorulur — hepsi **tartışmalı / yerleşik uygulamaya bağlı, içtihadı kontrol et**:
- "Fazla çalışma ücrete dahildir" klozu geçerli mi, hangi sınırla? (yıllık 270 saat sınırıyla bağlantı kurulması yerleşik uygulamadır)
- Kendi çalışma saatini belirleyen üst düzey yönetici fazla çalışma isteyebilir mi?
- İmzalı bordroda tahakkuk görünen aylar için daha fazlası nasıl ispatlanır?

### 2a. Alacak hesabı iskeleti (fazla çalışma ve benzeri)

Çıplak "ücret × saat" hesabı yapma. Önce varsayımları yaz, eksik girdi varsa **hesaplamadan önce sor**: ücretin brüt/net olduğu, prim ve ek ödemelerin niteliği, puantaj ya da tanık dayanağı, bordroda tahakkuk ve ödeme görünen aylar, izin/rapor haftaları, arabuluculuk başvuru tarihi.

```
Saat ücreti               = aylık brüt ücret ÷ 225            [yerleşik uygulama — teyit et]
Fazla çalışma saat ücreti = saat ücreti × 1,5                 [m. 41/2]
Fazla sürelerle çalışma   = saat ücreti × 1,25                [m. 41/3]
Haftalık fazla saat       = fiilî çalışma − ara dinlenmeleri (m. 68) − 45
Alacak                    = Σ haftalık fazla saat × fazla çalışma saat ücreti
                            − bordroda tahakkuk edip ödenen tutar (mahsup)
Hafta tatili / genel tatil çalışması: ayrı kalem (m. 46, m. 47)
Dönem                     = başvuru tarihinden geriye 5 yıl (m. 32/8); arabuluculuk süresince zamanaşımı durur (7036 m. 3/17)
Faiz                      = ücret alacağında mevduata uygulanan en yüksek faiz (m. 34); kalem bazında faiz türü tartışmalı — içtihadı kontrol et
```

- Formülü ve girdileri her zaman yaz; formülsüz rakam avukatın işine yaramaz.
- Tanık beyanına dayanan fazla çalışmada mahkemelerin hakkaniyet indirimi uyguladığı yerleşik uygulamadır — oran ezberden verilmez.
- Rakamın yanına: `[doğrula — iş hukuku uzmanı kontrolünden geçmeden iddia edilmez/ödenmez]`.
- Arabuluculuk dava şartıdır (7036 m. 3/1); hesap başvurudan önce bitmeli (profil: sonradan ek alacak riski).

### 3. Bayrak

- **Açık:** "m. 41'e göre 45 saati aşan her saat %50 zamlı ödenir."
- **Sınırda:** "Kloz yerleşik uygulamaya göre tartışmalı; risk şu — formal görüş önerilir."
- **Değişmiş/değişen mevzuat:** madde metnindeki değişiklik notunu oku (ör. 2026 değişiklikleri) ve yürürlük tarihini yaz.
- **Teyit edilemedi:** "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" — tahmin etme.

### 4. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="4857", madde_no=["41","63","68","69"])
tr_mevzuat_madde_getir(number="4857", madde_no=["32","34","ek 3"])
tr_resmi_gazete_tara(query="Asgari Ücret Tespit Komisyonu Kararı")
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="fazla çalışma ücretin içinde 270 saat", date_from="2022-01-01")
tr_ictihat_semantik_ara(initial_keyword="imzalı bordro fazla mesai", query="imzalı bordroda fazla çalışma tahakkuku varsa ispat")
```

Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) doğrulanmamış diye işaretle ve dur." Etiketler: `[ArthurLegal TR — 4857 m. X — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`; etiketleri silme.

Yabancı yargı çevresi: kural ezberden verilmez. AB çalışma süresi: `eu_search_eu_law(query="organisation of working time")`; Azerbaycan: `az_search_acts(query="Əmək Məcəlləsi", types=[107])`; İngiltere: `uk_search_legislation(query="Working Time Regulations")`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

## Çıktı

Sohbet biçiminde; not değil.

```
**[Hukuk / rejim]:** [Kural, tek paragraf, madde atfı ve güncellik notu.]

[Sınırda ya da değişen mevzuat varsa: bayrak.]

[Ayak izindeki başka bir ülkede ya da TİS'te fark varsa: tek satır, farkın önemli olup olmadığı.]
```

> **Atıfları doğrula.** Yukarıdaki madde ve karar atıfları yapay zekâ desteğiyle üretildi. Dilekçe ya da resmî görüşte kullanmadan önce mevzuat.gov.tr, UYAP Emsal ya da büro araştırma aracıyla doğruluk ve güncelliği kontrol et.

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları cevaba göre uyarla.

## Bu skill ne yapmaz

- Kuralı ezberden söylemez; her cevap çekilen maddeye dayanır.
- Sınırdaki sınıflandırma ya da kloz geçerliliği kararını vermez; kuralı söyler, sınırı işaretler.
- İstenmedikçe çok ülkeli tarama yapmaz.
- Tutar değişikliklerini takip etmez; cevap eskiyebilir, güncel için yeniden sor.
- İşçi/serbest çalışan ayrımında → `/employment-legal:worker-classification`.

---

## /employment-legal:worker-classification

---
name: worker-classification
description: >
  Önerilen bir çalışma ilişkisini sınıflandırır (Türk hukuku) — işçi (iş
  sözleşmesi), serbest çalışan (eser / vekâlet / serbest meslek), geçici işçi
  (özel istihdam bürosu), alt işveren ya da hizmet alımı — bağımlılık ölçütünü
  ve İş K., TBK, 5510 hükümlerini olgulara uygular; istenen yapı ile olguların
  desteklediği yapı arasındaki boşlukları (muvazaa, 4/b danışman riski)
  işaretler. Yalnız ileriye dönük. "Danışman olarak alalım", "freelancer mı
  işçi mi", "taşeron mu geçici işçi mi", "bu kişiyi nasıl sınıflandıralım"
  denince kullan.
argument-hint: "[önerilen düzenlemeyi anlatın ya da başlayın, ben sorayım]"
---

# /worker-classification — Çalışan Sınıflandırması

En pahalı sınıflandırma kararı, kimsenin bilinçli olarak vermediği karardır: biri "danışman" der, iş başlar, iki yıl sonra olgular iş ilişkisine benzer. Bu skill, iş başlamadan önce ölçütleri olgulara uygular ve anlatılan düzenlemenin kurulmak istenen yapıya uymadığı yeri söyler. Akıl yürütme kalıbını öğretir; kuralın kendisi her seferinde `tr_mevzuat_madde_getir` ile çekilir.

## Örnekler

```
/employment-legal:worker-classification
6 ay boyunca bir veri bilimciyi analiz ekibimize gömülü, bizim ofisimizde,
bizim araçlarımızla çalıştırmak istiyoruz; serbest meslek makbuzu keser.
```

```
/employment-legal:worker-classification
İşe alım danışmanı yalnız bize çalışıyor, saatlerini kendi belirliyor,
kendi bilgisayarını kullanıyor, yerleştirme başına ücret alıyor.
```

## ⛔ Yalnız ileriye dönük — girişten ÖNCE sor

> Bu iş başladı mı? Kişi şu anda bu düzenleme altında herhangi bir süredir çalışıyor mu?

**Evetse DUR.** Mevcut ilişkinin sınıflandırılması planlama değil, sorumluluk değerlendirmesidir: geriye dönük işçilik alacakları (kıdem, ihbar, fazla çalışma, yıllık izin — 5 yıllık zamanaşımı, 4857 m. 32/8 ve ek m. 3), SGK hizmet tespiti ve prim/idari para cezası, muvazaa tespiti, vergi düzeltmesi. Bu iş avukat yönetiminde, gizli ve bir iyileştirme planıyla yürür. Aynen şunu yaz ve bekle:

> **Kapsam dışı — mevcut ilişki.** Bu skill bir çalışma ilişkisini *başlamadan önce* analiz eder. Anlattığınız düzenleme zaten var. Geriye dönük sınıflandırma; alacak, SGK ve vergi maruziyetini ve yeniden yapılandırmayı kapsayan ayrı bir risk değerlendirmesidir ve profilin eskalasyon matrisine göre avukata yönlendirilmelidir. Yine de yalnız ileriye dönük planlama için ("bugün sıfırdan kursaydık") analiz istiyorsanız "yine de devam" deyin; çıktı iyileştirme planı değildir, geçmiş dönem maruziyetini hesaplamaz ve avukat onayı olmadan güvenilir sayılmaz.

Yalnız açık "yine de devam" ile ilerle; tereddütlü cevapta yeniden sor. Devam edilirse bu oturumdaki her çıktının başına:

```
⚠️ KAPSAM UYUŞMAZLIĞI — İlişki zaten mevcut. Bu, yalnız planlama amaçlı
ileriye dönük analizdir; iyileştirme planı değildir, geçmiş dönem alacak /
SGK / vergi maruziyetini kapsamaz. Geriye dönük soru eskalasyona işaretlendi.
```

## Bağlamı yükle

`company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → ayak izi, eskalasyon matrisi, varsa geçmiş sınıflandırma uyuşmazlıkları, büronun/şirketin sınıflandırma politikası, `## Outputs`, `## Who's using this`.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/employment-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Bilgi toplama (tek blokta sor)

> Doğru ölçütleri uygulayabilmem için düzenlemeyi ayrıntılı anlamam gerekiyor:
>
> **İş:** Günlük olarak ne yapacak? İş [ŞİRKET ADI]'ın asıl işinin parçası mı, yardımcı iş mi? Belirli bir sonucu (eser) mi teslim edecek, yoksa süre boyunca emeğini mi sunacak? Ekipte olmayan bir uzmanlığı var mı?
> **Talimat ve organizasyon:** Saatleri kim belirliyor? Nerede çalışacak? Nasıl çalışacağına (yöntem, sıra) siz mi karar vereceksiniz, yalnız sonucu mu tanımlayacaksınız? Ekibin vardiya/toplantı düzenine dahil olacak mı? Sizin çalışanlarınızı yönetecek mi?
> **Ekonomi:** Ücret saatlik/aylık mı, iş başına mı? Ekipman kimden? Başka müşterilere çalışıyor mu? Zarar riski taşıyor mu? Vergi mükellefiyeti (serbest meslek / şirket) var mı?
> **Yapı:** Doğrudan sözleşme mi, özel istihdam bürosu (geçici işçi) mi, alt işveren mi, şirketten şirkete hizmet alımı mı? Daha önce sizde işçi olarak çalıştı mı? Yazılı sözleşme var mı? Süre?
> **Amaç:** Sınıflandırma hangi sonuç için önemli — iş hukuku hakları, SGK (4/a – 4/b), vergi, İSG? Cevaplar amaca göre ayrışabilir.
> **Yer:** İş fiilen hangi ülkede yapılacak?

Cevapları bekle. Cevaplanamayan sorular analizi etkiler; boşluk olarak not et.

### 2. Uygulanacak ölçütleri belirle (kuralı çek)

| İlişki | Çıpa | Ana ölçüt (metinden doğrula) |
|---|---|---|
| İş sözleşmesi | 4857 m. 8/1; TBK m. 393 | İşçinin işverene **bağımlı** olarak iş görmesi, işverenin ücret ödemesi |
| Eser sözleşmesi | TBK m. 470 | Yüklenicinin bir **eser meydana getirmesi** karşılığında bedel |
| Vekâlet / iş görme | TBK m. 502 | Bir işin görülmesi; düzenlenmemiş iş görme sözleşmelerine de uygulanır |
| Asıl işveren – alt işveren | 4857 m. 2/6-7 | Yardımcı iş ya da asıl işin uzmanlık gerektiren bölümü; alt işveren işçileri yalnız o işyerinde; asıl iş bölünemez (uzmanlık istisnası); eski işçiyle alt işveren ilişkisi kurulamaz, aksi muvazaa → işçiler başlangıçtan itibaren asıl işverenin işçisi |
| Geçici iş ilişkisi | 4857 m. 7; 4904 m. 17 | Yalnız İŞKUR izinli özel istihdam bürosu ya da holding/şirketler topluluğu içi görevlendirme; sınırlı hâller ve süreler |
| Belirli süreli | 4857 m. 11 | Objektif koşul + yazılı; esaslı neden olmadan zincirleme → başlangıçtan belirsiz süreli |
| Kısmi süreli / çağrı üzerine / uzaktan | 4857 m. 13, m. 14 | Çağrı üzerine çalışmada yazılı sözleşme; süre belirlenmemişse haftalık 20 saat; çağrı en az 4 gün önce; uzaktan çalışmada yazılı sözleşme ve zorunlu içerik |
| Deneme süresi | 4857 m. 15 | En çok 2 ay (TİS ile 4 aya kadar) |
| SGK statüsü | 5510 m. 4/1-a, 4/1-b | Hizmet akdiyle çalışan (4/a) – kendi adına ve hesabına bağımsız çalışan (4/b) |
| İş K. kapsamı | 4857 m. 4 | İstisna işlerde TBK hizmet sözleşmesi hükümleri |

Bağımlılığın ölçütleri (talimat altında çalışma, işverenin iş organizasyonuna katılma, süreklilik, ücretin zamana göre ödenmesi, araç-gereç ve işyerinin işverence sağlanması, tek işverene çalışma, kişisel ifa, risk taşımama) kanunda sayılmaz; **yerleşik uygulama ve doktrindir** — `tr_ictihat_ara` ve `scholar_search_legal_scholarship` ile teyit et, karar numarası ezberden yazma.

Vergi boyutu (ücret – serbest meslek kazancı) → `/tax-legal` skill'lerine yönlendir; madde numarası ezberden verilmez.

Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]`, (4) doğrulanmamış diye işaretle ve dur." Her atıf etiketli: `[ArthurLegal TR — 6098 m. 393 — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`.

### 3. Ölçütleri olgulara uygula

Her ölçüt için ayrı tablo; özetleme, puanla:

```
Ölçüt: [ad — kaynak]
Amaç: [iş hukuku / SGK / vergi / İSG]
Kaynak: [madde atfı ya da içtihat künyesi] | Güncellik: [GG.AA.YYYY]

| Unsur | Giriş olgusu | Sinyal |
|---|---|---|
| Talimat / yöntem kontrolü | ... | işçi yönünde / bağımsız yönünde |
| Organizasyona katılma | ... | ... |
| ... | ... | ... |

Ölçütün yapısı: [bütüncül değerlendirme mi, kümülatif şartlar mı — kaynaktan]
Sonuç: [işçi yönünde / bağımsız yönünde / X unsuru belirsiz]
```

Tartışmalı unsurları açıkça işaretle ("tartışmalı — içtihadı kontrol et"); yazılı sözleşmenin adı ("danışmanlık", "hizmet alımı") tek başına belirleyici değildir — olgular esas alınır (yerleşik uygulama).

### 4. Sınıflandır ve boşlukları işaretle

**Sınıflandırma:**
- **İşçi (iş sözleşmesi):** olgular bağımlılığı gösteriyor → SGK 4/a, işe giriş bildirgesi (5510 m. 8), `/employment-legal:hiring-review`.
- **Bağımsız çalışan (eser / vekâlet / serbest meslek, SGK 4/b):** olgular her amaç için bağımsızlığı destekliyor.
- **Geçici işçi (özel istihdam bürosu):** işçi büronun bordrosunda; m. 7'deki hâl, süre ve oran sınırları; büronun İŞKUR izni ve geçici iş ilişkisi kurma yetkisi (4904 m. 17).
- **Alt işveren:** yalnız m. 2'deki şartlarla; asıl işverenle birlikte sorumluluk.
- **Hizmet alımı (şirketten şirkete):** kişi tedarikçinin işçisi; günlük talimat sizden geliyorsa muvazaa/geçici iş riski.
- **Belirsiz:** hangi ölçüt neden sorunlu.

Amaçlara göre farklı sonuç çıkıyorsa (ör. sözleşme eser görünümlü ama SGK açısından 4/a olgusu) açıkça yaz.

**Boşluk analizi (en önemli çıktı):**

```
İstenen yapı: [söylenen]
Olguların gösterdiği: [ölçütlerin sonucu]

🔴 [Unsur]: [anlatılan] istenen [yapı] ile çelişiyor çünkü [ölçüt + kaynak]. Düzenleme bu hâliyle başlarsa önemli risk.
🟡 [Unsur]: [ölçüt] altında zayıf nokta; tek başına belirleyici değil.
✅ [Unsur]: [yapıyı] destekliyor.
```

Türkiye'de sık görülen 🔴 kalıplar: eski işçinin "danışman" ya da alt işveren işçisi olarak devam etmesi (m. 2/7); asıl işin uzmanlık gerekçesi olmadan bölünmesi (m. 2/7); izinsiz büro üzerinden işçi temini (m. 7; 4904 m. 17); serbest meslek makbuzu kesen ama ekip içinde mesai düzeniyle çalışan kişi (4/a – 4/b).

**Eskalasyon tetikleyicileri** (profil matrisine ek): iş asıl işin parçası ve olgular bağımlılığa işaret ediyor; geçmişte sınıflandırma uyuşmazlığı/denetim; kişi işçileri yönetecek ya da bütçe yetkisi olacak; belirli bir bitişi olmayan uzun süre; sonucu değiştiren tartışmalı unsur.

### 5. Yurt dışında yapılacak iş

Uygulanacak hukuk MÖHUK 5718 m. 27. Yabancı ülkenin ölçütü ezberden yazılmaz: AB `eu_search_eu_law(query="improving working conditions in platform work")`; Hollanda `nl_search_legislation`; İngiltere `uk_search_legislation`; Almanya `de_gesetz_ara`; Azerbaycan `az_search_acts(query="Əmək Məcəlləsi", types=[107])`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

### 6. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="4857", madde_no=["2","7","8","11","14"])
tr_mevzuat_madde_getir(number="6098", madde_no=["393","470","502"])
tr_mevzuat_madde_getir(number="5510", madde_no="4")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="hizmet sözleşmesi eser sözleşmesi ayrımı bağımlılık unsuru", date_from="2022-01-01")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="asıl işveren alt işveren muvazaa uzmanlık", date_from="2022-01-01")
```

## Çıktı

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Çalışan Sınıflandırma Analizi
**Önerilen düzenleme:** [...] | **Yer:** [...] | **Amaç(lar):** [iş hukuku / SGK / vergi / İSG]
**Uygulanan ölçütler:** [liste, her biri kaynak ve güncellik tarihiyle]

## ⚠️ İnceleyen notu
- **En yakın sınıflandırma:** [İşçi / Bağımsız / Geçici işçi / Alt işveren / Hizmet alımı / Belirsiz]
- **Kaynaklar:** [çekilen maddeler, içtihat sayısı; doğrulanamayan]
- **Tartışmalı unsurlar:** [liste]
- **Eskalasyon:** [yok / [isim] — neden]

## Sonuç
[Devam edilebilir / Önce X düzeltilmeli / Dur — tek cümle]

## Ölçüt sonuçları
[Adım 3 tabloları]

## Boşluk analizi
[🔴 / 🟡 / ✅]

## Sonraki adımlar
[Bağımsız yapı uygunsa: sözleşmeye bağımsızlığı destekleyen hükümleri yansıt ve uygulamayı ona göre kur]
[Boşluk varsa: başlamadan önce giderilecekler]
[Büro/tedarikçi yapısı daha temizse: neden]
[İşçi ise: `/employment-legal:hiring-review`]
```

## Sonuç doğuran işlem kapısı (sınıflandırma kararı)

Nihai "bu yapıyla devam" önerisinden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> Yanlış sınıflandırma geriye dönük işçilik alacakları, SGK primi ve idari para cezası, vergi düzeltmesi ve muvazaa tespitine yol açar. Bu sınıflandırmayı bir avukatla incelediniz mi? Hayırsa götüreceğiniz özet: düzenleme (iş, talimat, ekonomi, yapı); uygulanan ölçütler ve sonuçları; boşluk analizi; açık sorular; en olası risk teorisi; sorulacaklar (bağımsız yapı uygun mu, büro/tedarikçi üzerinden kurmak riski kaldırır mı, sözleşmede hangi hükümler gerekir). Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan nihai öneri verme; "TASLAK" işaretli analiz serbest.

## Bu skill ne yapmaz

- Mevcut ilişkiyi geriye dönük analiz etmez.
- Hizmet/danışmanlık sözleşmesini yazmaz.
- Yanlış sınıflandırma olmuşsa iyileştirme danışmanlığı yapmaz.
- Hiçbir ülkenin kuralını ezberden söylemez.
- Sınırdaki vakalarda avukatın yerini tutmaz.

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; seçimi avukat yapar.
