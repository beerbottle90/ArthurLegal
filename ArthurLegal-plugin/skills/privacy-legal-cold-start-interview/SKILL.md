---
name: privacy-legal-cold-start-interview
description: >
  İlk kurulum — kişisel veri koruma pratiğinizi öğrenir ve profil dosyasını yazar:
  veri sorumlusu / veri işleyen rolü (KVKK m. 3), VERBİS kayıt durumu ve irtibat
  kişisi (m. 16), aydınlatma metinleri (m. 10), yurt dışına aktarım yolu (m. 9),
  sektörel kurallar (bankacılık, elektronik haberleşme, sağlık), hangi yabancı
  rejimlerin (GDPR, UK) önemli olduğu, veri işleyen sözleşmesi duruşları ve PIA
  ev üslubu. Aydınlatma metninizden, sözleşme şablonunuzdan ve örnek bir PIA'dan
  öğrenir. İlk kurulumda, CLAUDE.md eksik ya da placeholder içeriyorsa, "gizlilik
  eklentisini kur", "beni tanı", "KVKK ayarlarını yap" denince ya da --redo /
  --check-integrations ile kullan.
argument-hint: "[--redo | --full | --check-integrations]"
---

# /cold-start-interview

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasına bak; doluysa ve `--redo` yoksa üzerine yazmadan önce onay al. `--check-integrations` verildiyse görüşmeyi atla; yalnız Bölüm 0'daki "Ne bağlı?" kontrolünü çalıştır ve `## Available integrations` tablosunu yeniden yaz. ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse; yapılandırılmış ama denenmemiş bağlantı ⚪. `.mcp.json` beyanına bakarak ✓ verme.
2. Görüşmeyi yürüt (Bölüm 0 → 5).
3. Örnek belgeler: aydınlatma metni (bağlantı ya da dosya), veri işleyen sözleşmesi şablonu, örnek bir PIA. Üçünü de oku.
4. Çıkar: aydınlatma metnindeki taahhütler, sözleşme duruşları (söylenenle şablon arasındaki farkları not et), PIA yapısı.
5. Eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/privacy-legal/*/CLAUDE.md`) doldurulmuş bir CLAUDE.md varsa ve ayar yolunda yoksa ayar yoluna kopyala; neyin taşındığını göster.
6. Ayar yolundaki CLAUDE.md'yi yaz (üst klasörleri gerekirse oluştur). Özeti göster, ilk işi öner.

# Kurulum Görüşmesi — Kişisel Verilerin Korunması

## Amaç

Bu ekibin fiilen nasıl çalıştığını öğren: hangi rejimler gerçekten uygulanıyor, veri işleyen sözleşmesinde neyi kabul edip neyi etmiyorlar, burada iyi bir PIA neye benziyor. Hepsini her skill'in okuyacağı profil dosyasına yaz. B2B bulut hizmeti veren bir **veri işleyen** ile tüketiciye hizmet veren bir **veri sorumlusu** neredeyse hiçbir ortak noktaya sahip değildir; görüşme önce hangisi olduğunu bulur.

## Kurulum durumu

- **Dosya yok** → görüşmeye başla.
- **`<!-- SETUP PAUSED AT: -->` var** → selamla, o bölümden devam etmeyi öner.
- **`[PLACEHOLDER]` var, duraklatma notu yok** → baştan başlamayı ya da placeholder'ların başladığı yerden devam etmeyi öner.
- **Dolu** → kurulmuş; `--redo` yoksa atla.

Bölüm iskeleti `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonundadır. **Bölüm anahtarlarını çevirme:** `## Who we are`, `## Regulatory footprint`, `## Who's using this`, `## Available integrations`, `## DPA playbook`, `## Privacy policy commitments`, `## PIA house style`, `## DSAR process`, `## Escalation`, `## Seed documents`, `## Outputs`, `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` — diğer skill'ler bu anahtarları birebir okur. İçerik Türkçe yazılır.

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/firm-profile.md` dosyasına bak.
- **Varsa:** oku ve tek satırla teyit et: "Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu? (Değiştirmek için 'güncelle' deyin.)" Teyit edilirse ortak soruları atla.
- **Yoksa:** ilk kurulan eklenti budur. Oryantasyondan sonra ortak soruları sor ve paketteki `${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md` şablonuna göre yaz: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak."

Ortak profile ait sorular (varsa tekrar sorulmaz): pratik ortamı, büro/şirket adı, sektör, ne satıldığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri. Eklentiye özel sorular (rol haritası, sözleşme duruşları, PIA üslubu, başvuru süreci) burada kalır.

## Kurulum kapsamı

Çalışma klasörü ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden belge okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Devam mı, yeniden kurulum mu — onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

Kısa tut, önce hızlı/tam sor:

> **`privacy-legal`** kişisel veri uyum programını yürütenler içindir: PIA, veri işleyen sözleşmesi incelemesi, ilgili kişi başvuruları, mevzuat açık analizi, aydınlatma metni takibi.
>
> **2 dakika:** rolünüz, veri sorumlusu mu veri işleyen mi olduğunuz, temel yükümlülük haritası (VERBİS, yurt dışı aktarım, sektör); geri kalanı varsayılan. **15 dakika:** veri işleyen sözleşmesi duruşları (iki taraf için), örnek PIA'dan ev üslubu, tam mevzuat haritası, ilgili kişi başvuru süreci.
>
> Hızlı mı, tam mı? (Sonra `/arthurlegal:privacy-legal-cold-start-interview --full` ile genişletebilirsiniz.)

**Hızlı yol:** yalnız Bölüm 0 ve Bölüm 1; diğer alanlara `[DEFAULT]` yaz. Kapanış: "Tamam, komutları kullanabilirsiniz. Sözleşme duruşları, başvuru süreci ve PIA eşikleri için makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanması gereken bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--full`, tek bölüm için `--redo <bölüm>`."

**Seçimden sonra** tek paragraf oryantasyon: "Bu eklenti profilinizi (sözleşme duruşları, PIA üslubu, yükümlülük haritası), kişisel veri işleme envanterine bağlı bir faaliyet kaydını ve faaliyet bazında PIA ile sözleşme incelemelerini tutar. Cevaplarınızı her seferinde okunan düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve yüklediğiniz belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** VERBİS kaydı, envanter, aydınlatma metni, sözleşme şablonu, eskalasyon matrisi için önce bağlantı/yapıştırma iste: "Bağlantı ya da belge yapıştırın, ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli.
- **Uzun cevap gerekiyorsa bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste]. Şimdi doldurmak ister misiniz, placeholder olarak mı kalsın?" Sessiz boşluk bırakma. Sözleşme şablonu ya da PIA geçildiyse `[POSITIONS UNTESTED]` yaz.
- **Duraklat/devam:** "dur", "sonra devam" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /arthurlegal:privacy-legal-cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte cevaplanmış soruyu tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre ya da eşik söylerse `tr_mevzuat_madde_getir` ile çek ve karşılaştır. Çelişirse: "[X] dediniz; metin [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnekler: standart sözleşme imzalanmasından itibaren beş iş günü içinde Kuruma bildirilir (KVKK m. 9/5); VERBİS'e kayıt yükümlülüğünden istisnayı kanun değil Kurul, objektif kriterlere göre getirir (m. 16/2). İdari para cezası tutarlarını profile sabit yazma: "kanun metnindeki aralık; güncel tutarı teyit et — dönemsel güncellenir."

## Bölüm 0 — Kim kullanıyor, ne bağlı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her çıktının üst başlığını ve çerçevesini belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan** (stajyer, hukuk asistanı, avukat gözetiminde uyum ekibi)
> 2. **Avukata erişimi olan, avukat olmayan** (uyum yöneticisi, irtibat kişisi, kurucu)
> 3. **Düzenli avukat erişimi olmayan**

2 ya da 3 ise bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları hüküm değil, avukatla konuşmanız için araştırma olarak çerçevelerim; (2) hukuki sonucu olan adımlardan önce (ilgili kişiye cevap, sözleşme imzası, Kurula ihlal bildirimi, standart sözleşme bildirimi, Kurula yazı) avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım." 3 ise ekle: "Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür, koşullarını baroya sorun."

### Pratik ortamı

> Hangisi size uyuyor? (Eskalasyon dilini belirler.)
> - **Tek avukat / küçük büro** — onay zinciri sormam; "dış meslektaşa danış" ya da "eskalasyon yok" yazarım.
> - **Orta / büyük büro** — onay zinciri, üstünüzde kim imzalar.
> - **Kurum içi hukuk** — eskalasyon matrisi, hukuk müdürü, irtibat kişisi, ihlalde bilgi güvenliği ekibi.
> - **Kamu / klinik** — denetim modeli, dış yazışmadan önce imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla yazın; profili ona göre kurar, doldurulan, uyarlanan ve boş bırakılan alanları işaretlerim.

Dallanma:
- **Büro (her tür):** `## Matter workspaces` → `Enabled: ✓`, `Cross-matter context: off`. Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Veri sorumlusu müvekkil ile onun veri işleyeni aynı büroda olabileceğinden her yeni matter'da çatışma kontrolünü sor.
- **Kurum içi:** `Enabled: ✗`.
- **Kamu / klinik:** kim gözden geçirir, dış yazışmada imza zinciri.

Cevabı `## Who we are` altına `**Practice setting:**` olarak yaz.

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantı farklıdır.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_mevzuat_madde_getir(number="6698", madde_no="10")` ve `tr_kurum_karari_ara(kurum="kvkk", params={"scan_pages": 1}, limit=3)`. Cevap geldiyse ✓.
- **Yabancı ülke araçları** — yalnız ilgili kişileri ya da şirket grubu yurt dışındaysa: AB için `eu_search_eu_law`, Birleşik Krallık için `uk_search_legislation`; sonuç ince gelirse önce `status`.
- **Belge deposu (Google Drive, SharePoint, Box), Slack, zamanlanmış görev** — deneyebiliyorsan dene; deneyemiyorsan ⚪.

Rapor:
> - ✓ [Bağlantı] — bağlı (denendi)
> - ⚪ [Bağlantı] — yapılandırılmış, doğrulanmadı; MCP ayarlarınızdan teyit edin
> - ✗ [Bağlantı] — yok; [özellik] [manuel yönteme] düşer. Sonra bağlarsanız `--check-integrations` çalıştırın.

ArthurLegal MCP ✗ ise: "Her madde ve Kurul kararı atfı 'doğrulanmadı' işaretlenir ve UYARI satırı taşır."

**Hemen yaz:** `## Who's using this`, `## Available integrations` ve `## Outputs` (role göre üst başlık) bölümlerini `## Who we are`'dan sonra yaz.

## Bölüm 1 — Nasıl bir veri koruma pratiği? (2-3 dk)

> **[Müvekkil] ne yapıyor?** Ne satıyorsunuz, kime, nasıl — web sitesi ya da "hakkımızda" sayfası bağlantısı yeter. Büroysanız: tipik müvekkil profiliniz.

**Rol sorusu (her şeyi belirler):** Veri sorumlusu, işleme amaçlarını ve vasıtalarını belirleyen ve veri kayıt sisteminden sorumlu olan; veri işleyen ise veri sorumlusunun verdiği yetkiye dayanarak onun adına işleyen kişidir (KVKK m. 3/1-ı, ğ). Sor: "Müşterinizin kullanıcı verisi sisteminize girdiğinde amaç ve vasıtayı kim belirliyor — siz mi, müşteri mi?" Çoğu şirket bazı faaliyetlerde veri sorumlusu (çalışan, kendi müşterisi), bazılarında veri işleyendir. Bu cevap `/dpa-review`'un hangi tarafa göre inceleme yapacağını belirler. Kullanıcı emin değilse geçirme; birlikte faaliyet faaliyet çıkar.

Sonra B2B / B2C, kurumsal / KOBİ müşteri.

### Yükümlülük haritası (çekirdek çıktı → `## Regulatory footprint`)

Belge varsa önce iste (VERBİS kaydı ekran çıktısı, kişisel veri işleme envanteri, saklama ve imha politikası). Yoksa satır satır sor:

| Kalem | Soru | Doğrulanmış dayanak |
|---|---|---|
| **VERBİS** | Kayıtlı mı? İstisnada mı (hangi Kurul kararına göre)? Son güncelleme? | Veri işlemeye başlamadan önce Sicile kayıt zorunlu; istisnayı Kurul getirir (KVKK m. 16/2). Sicildeki bilgilerdeki değişiklik yedi gün içinde VERBİS'ten bildirilir (Veri Sorumluları Sicili Hakkında Yönetmelik m. 13). Sonradan yükümlü hâle gelen otuz gün içinde kaydolur (aynı Yön. m. 8/2). |
| **İrtibat kişisi** | Kim? | Sicile kayıtta bildirilen, Kurumla iletişimi sağlayan gerçek kişi; veri sorumlusunu temsile yetkili değildir (aynı Yön. m. 4/1-ç, m. 11/4). |
| **Yurt dışında yerleşik veri sorumlusu** | Türkiye'de veri sorumlusu temsilcisi var mı? | Temsilci marifetiyle, veri işlemeye başlamadan önce kayıt (aynı Yön. m. 5/1-b, m. 11/2-3). |
| **Envanter ve imha politikası** | Envanter var mı? Saklama ve imha politikası? Periyodik imha aralığı? | Kayıt yükümlüsü envanter hazırlar (aynı Yön. m. 5/1-ç) ve envantere uygun saklama ve imha politikası hazırlar (Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi Hakkında Yönetmelik m. 5/1); periyodik imha aralığı altı ayı geçemez (aynı Yön. m. 11/2). |
| **Aydınlatma metinleri** | Hangi kişi grupları için (müşteri, çalışan, aday, ziyaretçi/kamera, tedarikçi)? Nerede yayımlı? | Elde etme sırasında asgari bilgiler (KVKK m. 10); hukuki sebep açıkça belirtilir, açık rıza ile aydınlatma ayrı ayrı yapılır, Sicile açıklanan bilgilerle uyumlu olur (Aydınlatma Tebliği m. 5/1-ç, f, h). |
| **Açık rıza** | Hangi faaliyetler açık rızaya dayanıyor? | Açık rıza: belirli konuya ilişkin, bilgilendirmeye dayanan, özgür iradeyle açıklanan rıza (m. 3/1-a); m. 5/2 şartlarından biri varsa aranmaz. |
| **Özel nitelikli veri** | Sağlık, biyometrik, sendika üyeliği vb. işleniyor mu? | İşlenmesi yasak; m. 6/3'teki hâllerde mümkün, ayrıca Kurulun belirlediği yeterli önlemler şart (m. 6/3-4; 7499 s. Kanunla 2024'te değişti). |
| **Yurt dışına aktarım** | Hangi alıcılar/ülkeler? Hangi yolla? | Yeterlilik kararı → yoksa uygun güvence (standart sözleşme, bağlayıcı şirket kuralları, Kurul izinli taahhütname, kamu kuruluşları arası anlaşma) → yoksa yalnız arızi istisna (KVKK m. 9/1, 4, 6). Standart sözleşme beş iş günü içinde Kuruma bildirilir (m. 9/5); metni değiştirilmeden kullanılır (Yurt Dışına Aktarım Yönetmeliği m. 14/3). Taahhütnamede aktarım Kurul izninden sonra başlar (aynı Yön. m. 15/3). |
| **İhlal hazırlığı** | Olay müdahale planı, Kurula bildirimi kim yapar? | Veriler kanuni olmayan yollarla elde edilirse veri sorumlusu en kısa sürede ilgilisine ve Kurula bildirir (m. 12/5). Kurulun bildirim usul ve süresini somutlaştıran düzenleyici kararı araçla bulunamadı; süreyi profile yazmadan önce teyit et — UYARI: veri çekilemedi, teyidiniz gerekli: https://www.resmigazete.gov.tr/ |

**Sektör satırları** (yalnız ilgiliyse):
- **Bankacılık:** müşteri sırrı niteliğindeki bilgiler, istisnalar dışında, KVKK uyarınca açık rıza alınsa dahi müşteriden talep ya da talimat olmaksızın yurt içi/yurt dışı üçüncü kişilerle paylaşılamaz; BDDK bilgi sistemlerinin ve yedeklerinin yurt içinde tutulmasına karar verebilir (5411 s. Bankacılık Kanunu m. 73/3). BDDK kararları: `tr_kurum_karari_ara(kurum="bddk", query="bilgi sistemleri")`.
- **Elektronik haberleşme (işletmeci):** trafik ve konum verisi ancak açık rızayla yurt dışına aktarılabilir; abone rıza kayıtları asgari abonelik süresince saklanır (5809 s. Elektronik Haberleşme Kanunu m. 51/6, 51/10-c). Sektör yönetmeliği: Elektronik Haberleşme Sektöründe Kişisel Verilerin İşlenmesi ve Gizliliğin Korunmasına İlişkin Yönetmelik (RG 04.12.2020/31324) — madde atfı gerekiyorsa önce `tr_mevzuat_madde_getir(mevzuat_id="104558", madde_no=...)`.
- **Sağlık:** sağlık verisi m. 6/3-e kapsamında sır saklama yükümlülüğü altındaki kişiler veya yetkili kurumlarca işlenebilir; ayrıca Kişisel Sağlık Verileri Hakkında Yönetmelik (RG 21.06.2019/30808) — madde atfı gerekiyorsa `tr_mevzuat_madde_getir(mevzuat_id="105551", madde_no=...)` ile çek; çekilemezse UYARI satırı.
- **Diğer sektör** (sigorta, sermaye piyasası, e-ticaret): kuralı ezberden yazma; `tr_mevzuat_ara(query=..., search_in="fulltext")` ile ara, ilk konuda doğrula.

**Yabancı rejimler** — "GDPR uygulanır mı?" diye varsayma; AB'de ilgili kişiniz, AB'de kuruluşunuz ya da AB'li müşteriye veri işleyenliğiniz var mı, sor.
- **AB (GDPR):** kaynak `eu_search_eu_law(query="General Data Protection Regulation")` → CELEX 32016R0679; hüküm gerekirse `eu_get_document_text(celex="32016R0679", offset=...)`. Madde numarasını ezberden verme.
- **Birleşik Krallık:** `uk_search_legislation(title="Data Protection", year="2018", type="ukpga")` → Data Protection Act 2018; bölüm için `uk_get_section`.
- **Almanya, Hollanda, Polonya, Avusturya, İrlanda, Finlandiya, İspanya, Japonya, Azerbaycan:** ilgili önekli araçla ara (`de_`, `nl_`, `pl_`, `at_`, `ie_`, `fi_`, `es_`, `jp_`, `az_`).
- **ABD ve listede olmayan ülkeler:** "ArthurLegal'da bu ülkenin mevzuat kaynağı yok; yerel hukukçu görüşü alın." (ABD içtihadı yalnız kuruluysa CourtListener bağlayıcısıyla.)

Satır kuramadığın yer için kural uydurma: `[Ülke/sektör: ilk konuda araştır]`.

**Açık Kurul süreçleri:** Hakkınızda şikâyet, resen inceleme, idari para cezası ya da dava var mı? Kurulca verilen idari para cezalarına karşı idare mahkemesinde dava açılabilir (KVKK m. 18/3); varsa `/arthurlegal:privacy-legal-matter-workspace new` ile ayrı matter açın.

**Ekip:** Kaç kişi? İrtibat kişisi ile uyum sorumlusu aynı kişi mi? Bir inceleme üst onay gerektiren bir şey bulduğunda — onay sınırınızı aşan sözleşme duruşu, istisna içeren başvuru, şablona uymayan yeni faaliyet, Kurul yazısı, ihlal — kime gider? İsim ya da rol, ya da "kendim karar veririm".

## Bölüm 2 — Veri işleyen sözleşmesi duruşları (3-4 dk)

*(Bu duruşlar `/dpa-review`'u besler; yanlış duruş her seferinde yanlış redline demektir.)*

Önce: "Sözleşme şablonunuz, müzakere playbook'unuz ya da geri çekilme notunuz var mı? Yapıştırın; duruşları ben çıkarayım." Yüklenirse oku, bulduğunu teyit ettir, ilgili soruları atla. Yüklenmediyse sonda öner: "Bunu ekibe dağıtabileceğiniz ayrı bir sözleşme playbook'u olarak da yazayım mı?"

**Veri işleyen olduğunuzda (müşteri sözleşmesi):** kendi şablonunuz mu, müşterininki mi? Denetim: rapor/sertifika mı, yerinde denetim mi? İhlali müşteriye bildirme süreniz? Alt işleyen değişikliği: bildirim mi, itiraz hakkı mı, onay mı? Veri yeri: Türkiye'de tutma taahhüdü verebiliyor musunuz, yoksa yurt dışı bulut mu (o zaman aktarım yolu ve standart sözleşme bildirimini kimin yapacağı — taraflar belirleyebilir, belirlemezlerse veri aktaran bildirir: Yurt Dışına Aktarım Yön. m. 14/5)? Sözleşme sonunda silme/iade süresi ve tutanak? Sorumluluk sınırı?

**Veri sorumlusu olduğunuzda (tedarikçi sözleşmesi):** aynı sorular ters yönde. Hatırlat: veri sorumlusu, kendi adına işleyenlerle güvenlik tedbirlerinden müştereken sorumludur (KVKK m. 12/2); veri işleyen yurt dışına aktarırsa da veri sorumlusunun sorumluluğu kalkmaz (Yurt Dışına Aktarım Yön. m. 7/2).

**Otomatik ret:** Sözleşmede sizi anında "hayır" dedirten şart ne?

## Bölüm 3 — Ev üslubu (1-2 dk)

**PIA** (`/pia-generation`'ı besler): KVKK'nın çektiğimiz maddelerinde (m. 4-16) genel bir etki değerlendirmesi yükümlülüğü yok; PIA burada m. 4 ilkelerine ve m. 12 tedbirlerine uyumun belgelenmesi ve iyi uygulama olarak yapılır. GDPR kapsamındaysanız AB'nin etki değerlendirmesi kuralını `eu_get_document_text` ile ayrıca kontrol edin. Sor: PIA'yı ne tetikler? Ne uzunlukta? Kim onaylar?

**İlgili kişi başvuruları** (`/dsar-response`'u besler): hacim; kim yürütür; verinin bulunduğu sistemler; kimlik doğrulama yöntemi; başvuru kanalları. Doğrulanmış çerçeve: talep en geç otuz günde ücretsiz sonuçlandırılır, işlem ayrıca maliyet gerektirirse Kurul tarifesindeki ücret alınabilir (KVKK m. 13/2); başvuru Türkçe yapılır ve yazılı, KEP, güvenli elektronik imza, mobil imza, sistemde kayıtlı e-posta ya da başvuru uygulamasıyla iletilir (Başvuru Tebliği m. 4/2, 5/1); yazılı cevapta on sayfaya kadar ücret alınmaz (Tebliğ m. 7/1, tarifedeki sayfa ücreti Tebliğ metninde). İç SLA otuz günü aşamaz. Ret ya da yetersiz cevapta ilgili kişi, cevabı öğrendiği tarihten itibaren otuz ve her hâlde başvurudan itibaren altmış gün içinde Kurula şikâyet edebilir (m. 14/1).

## Bölüm 4 — Örnek belgeler (3-4 dk)

> Üç şey görmek istiyorum; nasıl çalıştığınızı en iyi bunlar gösterir:
> 1. **Güncel aydınlatma metni** (web sitesi; varsa çalışan ve kamera metinleri). Her PIA ve sözleşme bununla tutarlı olmalı.
> 2. **Veri işleyen sözleşmesi şablonunuz** — söylediklerinizle karşılaştıracağım.
> 3. **Beğendiğiniz bir PIA** — mükemmel değil, temsil edici olanı. Yapınızı ve derinliğinizi öğreneceğim.
>
> Varsa ek olarak: VERBİS kaydı, envanter, saklama ve imha politikası, açık rıza metinleri, çerez paneli ayarları, standart sözleşme bildirimleri.

**Okuma:** Aydınlatma metninden her taahhüdü çıkar (veri kategorileri, amaçlar, hukuki sebepler, alıcı grupları, yurt dışı aktarım, saklama, haklar) ve VERBİS kaydıyla uyumunu not et (Aydınlatma Tebliği m. 5/1-ç). Sözleşme şablonunu duruşlarla eşle; farkları sor: "İhlali 24 saatte bildiririz dediniz, şablonda 'gecikmeksizin' yazıyor — gerçek duruş hangisi?" PIA'dan başlıkları, derinliği, risk ifadesi biçimini çıkar.

## Bölüm 5 — Çıktılar ve belge yerleri (1 dk)

- Tamamlanan PIA, sözleşme incelemesi ve triyaj çıktıları nereye kaydediliyor? (`/policy-monitor` bu klasörü tarar; yolsuz yalnız doğrudan sorgu modu çalışır.)
- Yayımlanan aydınlatma metni(leri)nin asıl dosyası/bağlantısı?
- Dosya adlandırma kuralı (ör. `PIA_Ozellik_YYYY-AA-GG`) var mı?

## Profili yazma

Şablon iskeletine göre yaz; kısa örnek:

```markdown
# Kişisel Veri Koruma Pratik Profili
*Kurulum görüşmesiyle [TARİH] yazıldı. Doğrudan düzenlenebilir.*

## Who we are
[Müvekkil] [iş modeli]. Rol: [veri sorumlusu / veri işleyen / ikisi — faaliyet bazında]. Veri yeri: [Türkiye / AB bulutu / …]. Ekip: [N]. İrtibat kişisi: [ad]. Eskalasyon: [ad/rol].
**Practice setting:** [...]

## Regulatory footprint
| Kalem | Durum | Dayanak / not |
|---|---|---|
| KVKK | Uygulanır | [ArthurLegal TR — 6698 — GG.AA.YYYY] |
| VERBİS | [Kayıtlı / istisna — Kurul kararı künyesi araçtan / kayıtsız] | m. 16 |
| Yurt dışı aktarım | [ülke → yol: yeterlilik / standart sözleşme (bildirim tarihi) / BCR / taahhütname / arızi] | m. 9 |
| Sektör | [5411 / 5809 / sağlık / yok] | |
| Yabancı rejim | [GDPR — eu_ / UK — uk_ / yok] | |
**Open regulatory matters:** [yok / liste]

## Who's using this
## Available integrations
## DPA playbook        (veri işleyen tarafı | veri sorumlusu tarafı | otomatik ret)
## Privacy policy commitments   (aydınlatma metinleri: kategoriler, amaçlar, hukuki sebepler, alıcı grupları, saklama, haklar)
## PIA house style
## DSAR process        (hacim, sorumlu, sistemler, kimlik doğrulama, iç SLA ≤ 30 gün)
## Escalation          (Kurul yazısı ve ihlal: her zaman, derhâl)
## Seed documents
## Outputs
Outputs folder · Naming convention · Privacy policy document · Policy last updated · Last policy sweep · Last regulatory scan
Üst başlık — avukat: "GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ"; avukat olmayan: "ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — AVUKATLA GÖZDEN GEÇİRİN". Başlık tek başına koruma yaratmaz. İlgili kişiye cevap, Kurula yazı gibi dışa giden belgelerde başlık konmaz.
## Matter workspaces
Enabled: [✓/✗] · Active matter: none — practice-level context only · Cross-matter context: off
```

Kaynak etiketi: `[ArthurLegal TR — <citation> — GG.AA.YYYY]`. Sözleşme duruşları az müzakereden geliyorsa: `[POSITIONS UNTESTED — başlangıç noktası, yerleşik duruş değil]`.

## Yazdıktan sonra

1. **Özeti göster:** "Duyduklarım bunlar. En sıkı kontrol edilecek kısım sözleşme duruşları — doğru mu?"
2. **Neler yapabildiğimi görmek ister misiniz?**
   - Veri işleyen sözleşmesini playbook'a göre inceleme — `/arthurlegal:privacy-legal-dpa-review`
   - Yeni işleme faaliyeti triyajı (PIA gerekli mi, aydınlatma çatışıyor mu) — `/arthurlegal:privacy-legal-use-case-triage`
   - Ev formatında PIA — `/arthurlegal:privacy-legal-pia-generation`
   - İlgili kişi başvurusu (doğrulama, bulma, istisna, cevap yazısı) — `/arthurlegal:privacy-legal-dsar-response`
   - Yeni düzenlemeye göre açık analizi — `/arthurlegal:privacy-legal-reg-gap-analysis`
   - Aydınlatma metni ile uygulama arasındaki kaymayı ve Kurul gelişmelerini tarama — `/arthurlegal:privacy-legal-policy-monitor`

   **Önerim:** gerçek bir faaliyette `/use-case-triage`. Kullanıcı görüşmede somut bir iş söylediyse listeyi atla.
3. **Boşlukları işaretle:** "VERBİS kaydınızın son güncellemesi aydınlatma metninizle uyumsuz görünüyor"; "Yurt dışı bulut kullanıyorsunuz ama standart sözleşme bildirimi kaydı yok"; "Sözleşme şablonunuz yok — ilk müşteri talebinde sıfırdan müzakere edeceksiniz, taslak ister misiniz?"
4. **Kapanış:** "Profiliniz `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasında — düz metin. Tam yeniden görüşme `--redo`, bağlantı kontrolü `--check-integrations`, tek değişiklik `/arthurlegal:privacy-legal-customize`. En sık ayarlananlar: **sözleşme duruşları**, **yükümlülük haritası** (yeni ülke, yeni sektör, yeni aktarım) ve **başvuru sistemleri listesi**. Profiliniz öğrenir: bir çıktı yanlış gelirse genellikle ayarlanacak bir duruştur ve çıktı hangisi olduğunu söyler."

## Hata kalıpları

- **GDPR'ı varsayma.** AB'de ilgili kişi ya da faaliyet yoksa yazma.
- **Rol sorusunu geçirme.** Veri sorumlusu / veri işleyen ayrımı faaliyet bazındadır; tek etiketle geçme.
- **VERBİS istisnasını kullanıcının sözüyle yazma.** İstisnanın dayandığı Kurul kararını `tr_resmi_gazete_tara` / `tr_semantik_ara(kurum="kvkk")` ile bul, künyeyi araçtan al; bulamazsan UYARI satırı.
- **Genel duruşlardan playbook yazma.** Az sözleşme müzakere edildiyse `[POSITIONS UNTESTED]`.
- **Kurul karar numarasını ezberden yazma.** Yalnız araçtan dönen `citation` alanını kullan.
