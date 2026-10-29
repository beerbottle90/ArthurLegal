---
name: employment-legal-cold-start-interview
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

`~/.claude/plugins/config/claude-for-legal/firm-profile.md` dosyasına bak.
- **Varsa:** oku ve tek satırla teyit et: "Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [iller/ülkeler]. Doğru mu? (Değiştirmek için 'güncelle' deyin.)" Teyit edilirse ortak soruları atla.
- **Yoksa:** ilk kurulan eklenti budur. Oryantasyondan sonra ortak soruları sor ve paketteki `${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md` şablonuna göre yaz: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak."

Ortak profile ait sorular (varsa tekrar sorulmaz): pratik ortamı, büro/şirket adı, sektör, büyüklük, iller ve ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri. Eklentiye özel sorular (taraf modeli, eşik tablosu, tetikler, şablonlar) burada kalır.

## Kurulum kapsamı

Çalışma klasörü kullanıcının ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden belge okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Devam mı, yeniden kurulum mu — onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

Kısa tut (3-4 satır), önce hızlı/tam sor:

> **`employment-legal`** işe alım, fesih, iç soruşturma, izin, politika/yönetmelik, çalışan sınıflandırması ve yurt dışı genişleme işleri içindir.
>
> **2 dakika:** rol, pratik ortamı, taraf modeli, işyeri/işçi sayısı haritası; geri kalanı varsayılan. **15 dakika:** gerçek fesih tetikleri ve yüksek risk bayrakları, örnek belgelerden çıkarım, sözleşme/savunma/fesih şablonları, TİS ve disiplin yönetmeliği, entegrasyonlar.
>
> Hızlı mı, tam mı? (Sonra `/arthurlegal:employment-legal-cold-start-interview --full` ile genişletebilirsiniz.)

**Hızlı yol:** yalnız Bölüm 0 ve Bölüm 1; diğer her alana `[DEFAULT]` yaz. Kapanış: "Tamam, komutları kullanabilirsiniz. Fesih risk eşikleri, savunma usulü ve yönetmelik konularında makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanması gereken bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--full`, tek bölüm için `--redo <bölüm>`."

**Seçimden sonra** tek paragraf oryantasyon: "Bu eklenti iş hukuku profilinizi (taraf modeli, işyeri/eşik tablosu, fesih bayrakları, yönetmelik referansları), izin kaydını ve iç soruşturma dosya yapısını tutar. Cevaplarınızı her seferinde okunan düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve yüklediğiniz belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** Yönetmelik, eskalasyon matrisi, işyeri listesi gibi şeyler için önce bağlantı/yapıştırma iste: "Bağlantı ya da belge yapıştırın, ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli.
- **Uzun cevap gerekiyorsa bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste]. Şimdi doldurmak ister misiniz, placeholder olarak mı kalsın?" Sessiz boşluk bırakma; `[LIMITED DATA]` yalnız kullanıcının geçtiği belgeler içindir.
- **Duraklat/devam:** Kullanıcı "dur", "sonra devam" derse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /arthurlegal:employment-legal-cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte: "Hoş geldiniz, [bölüm]de kalmıştınız. Devam mı, baştan mı?" Cevaplanmış soruyu tekrar sorma.
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
- **İşçi ve işveren tarafı birlikte:** profile `## Çıkar çatışması` bölümü yaz — aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Her yeni matter'da çatışma kontrolünün yapıldığını sor (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`).
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
> - **İş sözleşmesi ve rekabet yasağı incelemesi** — `/arthurlegal:employment-legal-hiring-review`
> - **Fesih incelemesi ve risk bayrakları** — savunma, süre, geçerli/haklı neden, arabuluculuk — `/arthurlegal:employment-legal-termination-review`
> - **Çalışan sınıflandırması** — işçi / serbest meslek / geçici iş ilişkisi / alt işveren — `/arthurlegal:employment-legal-worker-classification`
> - **İşyerine göre ücret ve çalışma süresi sorusu** — `/arthurlegal:employment-legal-wage-hour-qa`
> - **Yurt dışı genişleme** — Türkiye'den yurt dışına ya da yabancı işverenin Türkiye'ye girişi — `/arthurlegal:employment-legal-expansion-kickoff`
> - **İç soruşturma açma** — `/arthurlegal:employment-legal-investigation-open`
>
> **Önerim:** varsayımsal bir fesihte `/arthurlegal:employment-legal-termination-review` — risk ayarınızın nasıl okunduğunu en iyi o gösterir. Ya da gündeminizdekini söyleyin.

Kullanıcı görüşmede somut bir iş söylediyse bu listeyi atla. Uygunsa ekle: "Eşik tablonuz hazır; [işyeri] satırını bir kez kontrol edin." · "Yönetmeliğinizde psikolojik taciz politikası yok — taslak ister misiniz?" · "Manuel izin takibi: açık izinleri `/arthurlegal:employment-legal-log-leave` ile ekleyin."

**Kapanış:**
> "Tamam. Profiliniz `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasında — düz metin, doğrudan düzenleyebilirsiniz. Tam yeniden görüşme için `--redo`, bağlantı kontrolü için `--check-integrations`, tek değişiklik için `/arthurlegal:employment-legal-customize`. En sık ayarlananlar: **işyeri/eşik tablosu** (işçi sayısı değiştikçe), **yüksek risk bayrakları** ve **eskalasyon matrisi**.
>
> **Profiliniz öğrenir.** Bir çıktı yanlış gelirse genellikle ayarlanacak bir duruştur; çıktı hangisi olduğunu söyler. 'Eskalasyon eşiğini şuna çek' demeniz yeterli. On dakikalık kurulum çalışan bir profil verir; bir aylık kullanım sizin yazmış gibi okunan bir profil."

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
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
