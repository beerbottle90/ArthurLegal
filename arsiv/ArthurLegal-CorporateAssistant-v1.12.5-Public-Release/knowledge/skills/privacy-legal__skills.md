# privacy-legal - Skill Referans Kitapcigi

> Değişiklik bildirimi (Apache-2.0 md. 4(b)): Bu kitapçık Anthropic'in `claude-for-legal` deposundaki aynı adlı eklentiden uyarlanmıştır. ArthurLegal tarafından Türk hukuku esas alınarak Türkçe yeniden yazılmıştır (2026-10); yabancı yargı çevreleri için yalnız ArthurLegal MCP araçlarına yönlendirir. Üst kaynak ve sürüm izi: ATTRIBUTION.md.

> Alan: KVKK/GDPR - DSAR, DPIA, DPA review
> Toplam skill: 9
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /privacy-legal:cold-start-interview (255 satir)
- /privacy-legal:customize (62 satir)
- /privacy-legal:dpa-review (205 satir)
- /privacy-legal:dsar-response (256 satir)
- /privacy-legal:matter-workspace (171 satir)
- /privacy-legal:pia-generation (196 satir)
- /privacy-legal:policy-monitor (192 satir)
- /privacy-legal:reg-gap-analysis (166 satir)
- /privacy-legal:use-case-triage (190 satir)

---

---

## /privacy-legal:cold-start-interview

---
name: cold-start-interview
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

`~/.claude/plugins/config/claude-for-legal/company-profile.md` dosyasına bak.
- **Varsa:** oku ve tek satırla teyit et: "Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu? (Değiştirmek için 'güncelle' deyin.)" Teyit edilirse ortak soruları atla.
- **Yoksa:** ilk kurulan eklenti budur. Oryantasyondan sonra ortak soruları sor ve paketteki `knowledge/company-profile.md` şablonuna göre yaz: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak."

Ortak profile ait sorular (varsa tekrar sorulmaz): pratik ortamı, büro/şirket adı, sektör, ne satıldığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri. Eklentiye özel sorular (rol haritası, sözleşme duruşları, PIA üslubu, başvuru süreci) burada kalır.

## Kurulum kapsamı

Çalışma klasörü ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden belge okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Devam mı, yeniden kurulum mu — onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

Kısa tut, önce hızlı/tam sor:

> **`privacy-legal`** kişisel veri uyum programını yürütenler içindir: PIA, veri işleyen sözleşmesi incelemesi, ilgili kişi başvuruları, mevzuat açık analizi, aydınlatma metni takibi.
>
> **2 dakika:** rolünüz, veri sorumlusu mu veri işleyen mi olduğunuz, temel yükümlülük haritası (VERBİS, yurt dışı aktarım, sektör); geri kalanı varsayılan. **15 dakika:** veri işleyen sözleşmesi duruşları (iki taraf için), örnek PIA'dan ev üslubu, tam mevzuat haritası, ilgili kişi başvuru süreci.
>
> Hızlı mı, tam mı? (Sonra `/privacy-legal:cold-start-interview --full` ile genişletebilirsiniz.)

**Hızlı yol:** yalnız Bölüm 0 ve Bölüm 1; diğer alanlara `[DEFAULT]` yaz. Kapanış: "Tamam, komutları kullanabilirsiniz. Sözleşme duruşları, başvuru süreci ve PIA eşikleri için makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanması gereken bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--full`, tek bölüm için `--redo <bölüm>`."

**Seçimden sonra** tek paragraf oryantasyon: "Bu eklenti profilinizi (sözleşme duruşları, PIA üslubu, yükümlülük haritası), kişisel veri işleme envanterine bağlı bir faaliyet kaydını ve faaliyet bazında PIA ile sözleşme incelemelerini tutar. Cevaplarınızı her seferinde okunan düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve yüklediğiniz belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** VERBİS kaydı, envanter, aydınlatma metni, sözleşme şablonu, eskalasyon matrisi için önce bağlantı/yapıştırma iste: "Bağlantı ya da belge yapıştırın, ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli.
- **Uzun cevap gerekiyorsa bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste]. Şimdi doldurmak ister misiniz, placeholder olarak mı kalsın?" Sessiz boşluk bırakma. Sözleşme şablonu ya da PIA geçildiyse `[POSITIONS UNTESTED]` yaz.
- **Duraklat/devam:** "dur", "sonra devam" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /privacy-legal:cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte cevaplanmış soruyu tekrar sorma.
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

> **[ŞİRKET ADI] ne yapıyor?** Ne satıyorsunuz, kime, nasıl — web sitesi ya da "hakkımızda" sayfası bağlantısı yeter. Büroysanız: tipik müvekkil profiliniz.

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

**Açık Kurul süreçleri:** Hakkınızda şikâyet, resen inceleme, idari para cezası ya da dava var mı? Kurulca verilen idari para cezalarına karşı idare mahkemesinde dava açılabilir (KVKK m. 18/3); varsa `/privacy-legal:matter-workspace new` ile ayrı matter açın.

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
[ŞİRKET ADI] [iş modeli]. Rol: [veri sorumlusu / veri işleyen / ikisi — faaliyet bazında]. Veri yeri: [Türkiye / AB bulutu / …]. Ekip: [N]. İrtibat kişisi: [ad]. Eskalasyon: [ad/rol].
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
   - Veri işleyen sözleşmesini playbook'a göre inceleme — `/privacy-legal:dpa-review`
   - Yeni işleme faaliyeti triyajı (PIA gerekli mi, aydınlatma çatışıyor mu) — `/privacy-legal:use-case-triage`
   - Ev formatında PIA — `/privacy-legal:pia-generation`
   - İlgili kişi başvurusu (doğrulama, bulma, istisna, cevap yazısı) — `/privacy-legal:dsar-response`
   - Yeni düzenlemeye göre açık analizi — `/privacy-legal:reg-gap-analysis`
   - Aydınlatma metni ile uygulama arasındaki kaymayı ve Kurul gelişmelerini tarama — `/privacy-legal:policy-monitor`

   **Önerim:** gerçek bir faaliyette `/use-case-triage`. Kullanıcı görüşmede somut bir iş söylediyse listeyi atla.
3. **Boşlukları işaretle:** "VERBİS kaydınızın son güncellemesi aydınlatma metninizle uyumsuz görünüyor"; "Yurt dışı bulut kullanıyorsunuz ama standart sözleşme bildirimi kaydı yok"; "Sözleşme şablonunuz yok — ilk müşteri talebinde sıfırdan müzakere edeceksiniz, taslak ister misiniz?"
4. **Kapanış:** "Profiliniz `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasında — düz metin. Tam yeniden görüşme `--redo`, bağlantı kontrolü `--check-integrations`, tek değişiklik `/privacy-legal:customize`. En sık ayarlananlar: **sözleşme duruşları**, **yükümlülük haritası** (yeni ülke, yeni sektör, yeni aktarım) ve **başvuru sistemleri listesi**. Profiliniz öğrenir: bir çıktı yanlış gelirse genellikle ayarlanacak bir duruştur ve çıktı hangisi olduğunu söyler."

## Hata kalıpları

- **GDPR'ı varsayma.** AB'de ilgili kişi ya da faaliyet yoksa yazma.
- **Rol sorusunu geçirme.** Veri sorumlusu / veri işleyen ayrımı faaliyet bazındadır; tek etiketle geçme.
- **VERBİS istisnasını kullanıcının sözüyle yazma.** İstisnanın dayandığı Kurul kararını `tr_resmi_gazete_tara` / `tr_semantik_ara(kurum="kvkk")` ile bul, künyeyi araçtan al; bulamazsan UYARI satırı.
- **Genel duruşlardan playbook yazma.** Az sözleşme müzakere edildiyse `[POSITIONS UNTESTED]`.
- **Kurul karar numarasını ezberden yazma.** Yalnız araçtan dönen `citation` alanını kullan.

---

## /privacy-legal:customize

---
name: customize
description: >
  Kişisel veri koruma profilinde tek bir şeyi değiştir — tüm kurulum görüşmesini
  yeniden yapmadan. Rol haritası (veri sorumlusu / veri işleyen), yükümlülük
  haritası (VERBİS, yurt dışı aktarım, sektör, yabancı rejim), risk duruşu,
  eskalasyon kişileri, veri işleyen sözleşmesi playbook'u, aydınlatma metni
  taahhütleri, PIA üslubu, ilgili kişi başvuru süreci ya da matter klasörleri.
  Kullanıcı "şunu değiştir", "profilimi güncelle", "playbook'umu düzenle" ya da
  "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değişikliğin tarifi]"
---

# /customize

## Ne zaman çalışır

Kullanıcı profilindeki bir şeyi — bir sözleşme duruşu, bir aktarım yolu, eskalasyon kişisi, başvuru süresi — kurulum görüşmesini baştan yapmadan ve dosyayı elle düzenlemeden değiştirmek istiyor.

## Ne yap

1. **Profili oku.** `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` ve bir üst klasördeki `~/.claude/plugins/config/claude-for-legal/company-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa:
   > Henüz kurulum yapılmamış. Önce `/privacy-legal:cold-start-interview` çalıştırın — customize mevcut bir profili ayarlamak içindir.

2. **Haritayı göster** (her biri için tek satır mevcut değer):
   - **Kim olduğumuz** — ad, sektör, ülkeler, pratik ortamı *(tüm eklentilerle ortak — değişiklik `company-profile.md`'e yazılır)*
   - **Rol haritası** — hangi faaliyette veri sorumlusu, hangisinde veri işleyen
   - **Yükümlülük haritası** (`## Regulatory footprint`) — VERBİS durumu ve irtibat kişisi, envanter ve imha politikası, aydınlatma metinleri, özel nitelikli veri, yurt dışı aktarım yolları, sektör satırları, yabancı rejimler
   - **Risk duruşu** — temkinli / orta / atak; aktarım, saklama süresi ve sözleşme redline'ına etkisi
   - **Kişiler** — irtibat kişisi, uyum ekibi, bilgi güvenliği, dış avukat, eskalasyon zinciri
   - **Sözleşme playbook'u** (`## DPA playbook`) — denetim, ihlal bildirimi, alt işleyen, veri yeri, silme/iade, sorumluluk; veri işleyen ve veri sorumlusu tarafı ayrı
   - **Aydınlatma taahhütleri** (`## Privacy policy commitments`) — `/policy-monitor`'ün uygulamayla karşılaştırdığı metinler
   - **PIA üslubu** — bölüm sırası, risk puanlama, tetikler
   - **Başvuru süreci** (`## DSAR process`) — kanallar, kimlik doğrulama, iç SLA, sistemler, cevap şablonu
   - **İş akışı** — matter workspaces, `/policy-monitor` tarama sıklığı ve son tarama tarihleri
   - **Entegrasyonlar** — ArthurLegal MCP, belge deposu, Slack; düşüş yolları

3. **Sor:** "Neyi ayarlayalım? Bir bölüm seçin ya da değişikliği kendi cümlenizle anlatın."

4. **Değişikliği yap.** Mevcut değeri göster, yenisini al, aşağı akış etkisini açıkla, onay al, yaz. Örnekler:
   - *Alt işleyen bildirim süresi 30 gün → 14 gün:* "`/dpa-review` artık 14 günden kısa her bildirimi sapma olarak işaretleyecek. Mevcut sözleşmeler kaydedildiği gibi kalır."
   - *Yeni yurt dışı aktarım (AB'de barındırılan bulut):* "Yükümlülük haritasına satır eklenir: yeterlilik kararı yoksa uygun güvence gerekir (KVKK m. 9/4). Standart sözleşme seçilirse metin değiştirilmeden kullanılır ve imzaların tamamlanmasından itibaren beş iş günü içinde Kuruma bildirilir (Yurt Dışına Aktarım Yönetmeliği m. 14/3, 14/5). `/dpa-review` bildirimi kimin yapacağını sözleşmede arar."
   - *Rol: yalnız veri sorumlusu → veri sorumlusu + veri işleyen:* "Playbook'un veri işleyen yarısı devreye girer; `/dpa-review` her sözleşmede tarafı yeniden tespit eder."
   - *VERBİS: kayıtlı → istisna:* "Dayanak Kurul kararının künyesini araçtan getirelim (`tr_semantik_ara(kurum="kvkk", query="Sicile kayıt yükümlülüğünden istisna")` ya da `tr_resmi_gazete_tara`); künye bulunamazsa satıra UYARI satırı eklenir. İstisna, Kanundaki diğer yükümlülükleri kaldırmaz (Veri Sorumluları Sicili Hakkında Yönetmelik m. 5/1-f)."
   - *Risk duruşu orta → temkinli:* "Daha çok faaliyet PIA'ya yönlenir, aktarımda arızi istisnaya daha az dayanılır, saklama süreleri daha kısa önerilir."
   - *Yeni ülke (Almanya):* "Yabancı rejim satırı eklenir; kaynak `de_` araçları. GDPR satırı yoksa `eu_` kontrolü önerilir."

   Kullanıcı bir madde, süre ya da eşik söylüyorsa yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; idari para cezası tutarlarını sabit yazma (güncel tutarı teyit et — dönemsel güncellenir).

5. **Ortak profil değişiklikleri** (ad, sektör, ülkeler, pratik ortamı) `company-profile.md`'e yazılır:
   > Bu değişiklik tüm eklentileri etkiler — ülke listesini okuyan her eklenti artık [yeni değer]i görür.

6. **Kapat:** "Tamam. Bir sonraki çıktı bunu yansıtacak. Başka bir şey var mı? `/privacy-legal:customize` her zaman çalışır."

## Korkuluklar

- **Bölümü silme.** Bir rejim kapsamdan "çıkarılmak" istenirse `[Şu an kapsam dışı]` işaretini öner ve hangi işaretlemelerin düşeceğini açıkla.
- **İç tutarsızlığı işaretle.** Ör. "yalnız veri işleyen" + veri sorumlusu playbook'u etkin; "yurt dışı aktarım yok" + bulut sağlayıcısı yurt dışında; "VERBİS istisnası" + saklama ve imha politikası hiç yok (politika yükümlülüğü yoksa da silme yükümlülüğü sürer: Silme Yönetmeliği m. 5/3); bankacılıkta "açık rızayla paylaşırız" (müşteri sırrı, maddedeki istisnalar dışında, açık rıza alınsa dahi müşteri talebi ya da talimatı olmaksızın paylaşılamaz: 5411 s. Kanun m. 73/3).
- **Kanuni sınırın altına inme.** İç başvuru cevap süresi otuz günü aşacak şekilde ayarlanamaz (KVKK m. 13/2); periyodik imha aralığı altı ayı aşamaz (Silme Yönetmeliği m. 11/2); standart sözleşme bildirimi beş iş gününü aşamaz (KVKK m. 9/5). Böyle bir talebi reddet ve nedenini açıkla.
- **Güvence kaybını işaretle.** `tr_mevzuat_madde_getir` doğrulaması, çekilemeyen veride UYARI satırı, kaynak etiketleri, `[review]` işareti ve `/use-case-triage`'daki zorunlu PIA kontrolü yük taşır — kaldırma; ayarlamadan önce bedelini açıkla.
- **Bölüm anahtarlarını çevirme** (`## Regulatory footprint`, `## DPA playbook`, `## Outputs`, `## Matter workspaces`, `Active matter:` vb.).
- **Tek seferde tek değişiklik.** Görüşmeyi baştan sorma.

---

## /privacy-legal:dpa-review

---
name: dpa-review
description: >
  Veri işleme sözleşmesi (DPA; veri sorumlusu–veri işleyen sözleşmesi)
  incelemesi — tarafın veri işleyen mi veri sorumlusu mu olduğunu belirler,
  sözleşmeyi DPA playbook'unun ilgili yarısına ve KVKK tabanına (m. 3 roller,
  m. 12 veri güvenliği ve müşterek sorumluluk, m. 8–9 aktarım, standart
  sözleşmenin 5 iş günü içinde bildirimi) göre madde madde tarar, en küçük
  ölçekte redline önerir. "Bu DPA'yı incele", "veri işleme sözleşmesi",
  "müşteri kendi DPA'sını gönderdi", "tedarikçi sözleşmesindeki KVKK eki",
  "bu DPA uygun mu" denince ya da bir DPA eklendiğinde kullan.
argument-hint: "[dosya | bağlantı | metni yapıştırın]"
---

# /dpa-review — Veri İşleme Sözleşmesi İncelemesi

DPA iki türlüdür ve inceleme ikisinde neredeyse terstir: müşteri kendi DPA'sını gönderdiğinde operasyonel esnekliğimizi savunuruz; tedarikçiyle sözleşirken kendi (ve müşterilerimizin) verisini koruruz. İkisi de aynı playbook'tan, karşı satırlardan okunur.

KVKK, veri işleyenle yapılacak sözleşmenin asgari içeriğini saymaz. Taban; rol tanımları (m. 3), veri güvenliği yükümlülükleri ve müşterek sorumluluk (m. 12), aktarım kuralları (m. 8–9) ve Yurt Dışına Aktarım Yönetmeliği'nden gelir; rakamlar (bildirim saatleri, süreler) playbook'tan. AB rejimi de uygulanıyorsa asgari içerik için GDPR Art. 28'i araçla çek. Her madde atfından önce `tr_mevzuat_madde_getir`.

## ⏰ ÖN-KONTROL — Süre

| Durum | Süre | Dayanak |
|---|---|---|
| Yurt dışı aktarım standart sözleşmeyle | İmzaların tamamlanmasından itibaren **5 iş günü** içinde Kuruma bildirim (fiziki, KEP ya da Kurul'un belirlediği yöntem); kimin bildireceği sözleşmede belirlenebilir, belirlenmemişse veri aktaran bildirir | 6698 m. 9/5; Yurt Dışına Aktarım Yön. m. 14/5 |
| Bildirim yapılmazsa | İdari para cezası (tutar yazma — kanun metnindeki sınırlar her yıl yeniden değerlenir) | 6698 m. 18/1-d; 5326 m. 17/7 |
| Veri ihlali | Veri sorumlusu ilgilisine ve Kurula **en kısa sürede** bildirir | 6698 m. 12/5 |
| İhlal — Kurul uygulaması | Kurul karar özetleri ihlalin **tespitinden itibaren 72 saat** ölçütünü uygular; ölçütü koyan düzenleyici kararın metni araçla bulunamadı → atıf yapmadan önce yeniden ara, bulunamazsa UYARI satırı | `tr_semantik_ara(kurum="kvkk", query="veri ihlali bildirimi 72 saat")` |
| VERBİS bilgisi değişirse (yeni alıcı grubu, yurt dışı aktarım) | Kanun: derhâl; Yönetmelik: değişiklikten itibaren 7 gün içinde VERBİS üzerinden | 6698 m. 16/3-ç, d, m. 16/4; Veri Sorumluları Sicili Hakkında Yön. m. 13/1 |

72 saat Kanun'da değildir; "Kanun 72 saat öngörür" yazma (GDPR'daki 72 saat ayrı bir kuraldır: Art. 33 — AB tarafında araçla çek). Veri işleyenden veri sorumlusuna bildirim süresini, veri sorumlusunun bu uygulamaya yetişeceği şekilde playbook'tan kur.

## Destination check

- **Dahili inceleme notu** → profilin `## Outputs` bölümündeki role göre üst başlık.
- **Karşı tarafa giden redline ya da açıklama** → iç gerekçe, risk puanı, fallback ve "kabul edebileceğimiz en kötü pozisyon" çıkarılır; başlık konmaz.
- **İş birimine özet** → hukuki analiz kısaltılır; "imzalanabilir mi, neyin değişmesi gerekir" iki cümleyle.

## ADIM 0 — Yön: veri işleyen mi, veri sorumlusu mu?

- Veri sorumlusu: işleme amaçlarını ve vasıtalarını belirleyen, veri kayıt sisteminin kurulmasından ve yönetilmesinden sorumlu kişi (m. 3/1-ı). Veri işleyen: veri sorumlusunun verdiği yetkiye dayanarak onun adına işleyen kişi (m. 3/1-ğ).
- [ŞİRKET ADI] veri işleyen → müşterinin DPA'sı → playbook'un veri işleyen tarafı → **savunma**.
- [ŞİRKET ADI] veri sorumlusu → tedarikçinin DPA'sı ya da bizim şablon → playbook'un veri sorumlusu tarafı → **koruma**.
- Etiket gerçeği belirlemez: "veri işleyen" diye adlandırılan taraf veriyi kendi amacıyla (hizmet geliştirme, model eğitimi, pazarlama) kullanıyorsa o kullanımda veri sorumlusudur → aktarım (m. 8) ve aydınlatma (m. 10) sorunu. "Ortak veri sorumluluğu" KVKK'da tanımlanmamıştır — **tartışmalı; Kurul kararlarını ara**.
- Belirsizse sor. Yön yanlışsa her öneri tersine döner.

## Bağlamı yükle

- `company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DPA playbook` (veri işleyen tarafı | veri sorumlusu tarafı | otomatik ret), `## Privacy policy commitments` (aydınlatma metinleri), `## Regulatory footprint` (sektör ve yabancı rejim satırları), `## Escalation`, `## Outputs`, `## Who's using this`. Yer tutucu varsa dur ve `/privacy-legal:cold-start-interview` öner.
- **Önceki çıktılar** (`## Outputs` klasörü): aynı karşı taraf ya da faaliyet için `use-case-triage`, `pia-generation`, önceki `dpa-review`. Bulunursa incelemede an: "Önceki triage ([tarih]) [risk] dedi ve onayı [X] şartına bağladı; bu inceleme onunla tutarlı / şu nedenle ayrılıyor: [yeni olgu, kapsam, kloz]." **Ciddiyet tabanı:** önceki çıktının 🔴'si sessizce 🟢'ye inmez; her düşürme gerekçesiyle yazılır. Bulunamazsa açıkça yaz: "Bu karşı taraf/faaliyet için önceki triage veya PIA yok."

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/privacy-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Sektörel katman (madde madde incelemeden önce sor)

Genel KVKK tabanının üstüne sektör kuralı binebilir; KVKK'ya uygun bir DPA sektör kuralına kör olabilir.

| Veri | Ek kural | Ara |
|---|---|---|
| Banka müşteri verisi | Bankacılık faaliyetine özgü müşteri ilişkisi verileri müşteri sırrıdır; istisnalar dışında, KVKK uyarınca açık rıza alınsa dahi müşteriden talep ya da talimat olmaksızın yurt içi/yurt dışı üçüncü kişilerle paylaşılamaz; BDDK yurt dışına paylaşımı yasaklamaya ve bilgi sistemleri ile yedeklerin yurt içinde tutulmasına karar verebilir; destek/hizmet alımına ilişkin istisna ve şartları m. 73/4'te | `tr_mevzuat_madde_getir(number="5411", madde_no=["73"], max_chars_per_article=8000)`; `tr_kurum_karari_ara(kurum="bddk", query="destek hizmeti")` |
| Sağlık verisi | Özel nitelikli (m. 6/1); m. 6/3-e; Kişisel Sağlık Verileri Hakkında Yönetmelik | `tr_mevzuat_ara(query="Kişisel Sağlık Verileri", types=["KKY"])` |
| Elektronik haberleşme | Elektronik Haberleşme Sektöründe Kişisel Verilerin İşlenmesi ve Gizliliğin Korunmasına İlişkin Yönetmelik | `tr_mevzuat_ara(query="Elektronik Haberleşme Sektöründe Kişisel Verilerin", types=["KKY"])` |
| Sigorta, sermaye piyasası, ödeme hizmetleri | Sektör mevzuatındaki sır ve dış hizmet kuralları | `tr_mevzuat_ara(query=..., search_in="fulltext")`; `tr_kurum_karari_ara(kurum="spk"/"bddk", ...)` |
| Özel nitelikli veri (her sektör) | Kurul'un belirlediği yeterli önlemler şarttır (m. 6/4) | `tr_semantik_ara(kurum="kvkk", query="özel nitelikli kişisel veri yeterli önlemler")` — düzenleyici kararın metni indekste yoksa UYARI satırı |

Hiçbiri yoksa açıkça yaz: "sektörel katman yok — kontrol edildi."

## Madde madde inceleme (her DPA)

Rakamlar playbook'tan, yasal taban Kanun'dan. Taban az sonuç dönerse sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle."

| Konu | Aranan | KVKK / TBK tabanı | Tipik kavga |
|---|---|---|---|
| Roller | Gerçeğe uygun rol | m. 3/1-ğ, ı | "Ortak sorumlu" etiketi; karşı tarafın kendi amaçları |
| Kapsam ve talimat | Belgelenmiş talimat, tanımlı amaç | m. 3/1-ğ ("verdiği yetkiye dayanarak onun adına"); m. 12/4 (amaç dışı kullanım ve açıklama yasağı) | "ve ilgili amaçlar" genişletmesi |
| Alt veri işleyenler | Güncel liste, değişiklik usulü | Kanun'da ayrı hüküm yok → playbook; yurt dışındaysa sonraki aktarım (m. 9/8) | Toptan onay / veto / yalnız bildirim |
| Güvenlik | Somut tedbir eki | m. 12/1 (teknik ve idari tedbirler); m. 12/2 (veri sorumlusu, adına işleyenle birlikte **müştereken sorumlu**) | Eki olmayan "uygun tedbirler" |
| Denetim | Yöntem, sıklık, bildirim, maliyet | m. 12/3 (veri sorumlusu denetim yapmak veya yaptırmak zorunda) | Kısa bildirimli yerinde denetim |
| Gizlilik | Çalışanlar dahil, sözleşme sonrası | m. 12/4 (görevden ayrıldıktan sonra da sürer) | Süre sınırı |
| İhlal bildirimi | Tetik ("öğrenme" mi "teyit" mi), süre, içerik, iş birliği | m. 12/5 "en kısa sürede" + Kurul uygulaması (yukarıda) | Belirsiz "gecikmeksizin" |
| Yurt dışı aktarım | Mekanizma | m. 9 (aşağıda) | Mekanizma yok; değiştirilmiş standart sözleşme |
| Silme / iade | Sona ermede süre, tutanak, yedek | m. 7; Silme Yönetmeliği | "Ticari olarak makul" silme |
| Sorumluluk | Ana sözleşme tavanı mı, ayrı mı; istisnalar | TBK m. 115/1 (ağır kusurdan önceden sorumsuzluk anlaşması kesin hükümsüz); m. 18/2 (cezanın muhatabı) | Sınırsız veri sorumluluğu; ceza tazmini |

- **m. 12/2 "müştereken"**: bunun ilgili kişiye karşı müteselsil sorumluluk anlamına gelip gelmediği ve iç ilişkide kusur dağılımı **tartışmalı — doktrin ve içtihadı kontrol et** (`scholar_search_legal_scholarship`, `tr_ictihat_semantik_ara`). Rücu ve tazmin klozunu bu belirsizliği gözeterek kur.
- **İdari para cezası:** m. 18/1-a–ç cezaları veri sorumlusuna, (d) bendindeki standart sözleşme bildirim cezası veri sorumlusu ya da veri işleyen gerçek kişi ve özel hukuk tüzel kişilerine uygulanır (m. 18/2). Cezanın sözleşmeyle karşı tarafa yansıtılabilirliği (tazmin klozu) **tartışmalı — içtihadı kontrol et**.
- **Tavan klozu:** kast ve ağır kusur tavan dışında kalmalı (TBK m. 115/1).
- **Karşı tarafın matbu DPA'sı:** tek başına önceden hazırlanıp sunulan hükümler genel işlem koşuludur (TBK m. 20); karşı tarafın menfaatine aykırı koşul, açıkça bilgi verilip içeriği öğrenme imkânı sağlanmadıysa yazılmamış sayılır (TBK m. 21/1). Tacirler arası uygulamadaki etkisi için içtihadı kontrol et.

### Yurt dışı aktarım (m. 9 — 7499 s.K. ile değişik)

Sırayla:
1. **Yeterlilik kararı** (ülke, ülke içindeki sektör ya da uluslararası kuruluş; Kurul verir, RG'de yayımlanır) + m. 5 ya da m. 6 şartlarından biri (m. 9/1-2).
2. Yoksa **uygun güvence** + m. 5/6 şartı + ilgili kişinin aktarım ülkesinde de haklarını kullanma ve etkili kanun yollarına başvurma imkânı (m. 9/4): (a) kamu kurumları arası anlaşma + Kurul izni; (b) Kurul onaylı bağlayıcı şirket kuralları; (c) Kurul'un ilan ettiği **standart sözleşme**; (ç) yazılı taahhütname + Kurul izni.
   - Standart sözleşme metni **hiç değiştirilmeden** kullanılır; yabancı dilde de akdedilirse Türkçe metin esastır (Yön. m. 14/3). Taraflarca ya da temsile ve imzaya yetkililerce imzalanır (m. 14/4). Bildirime yetki belgeleri ve yabancı dildeki her belgenin noter onaylı çevirisi eklenir (m. 14/6). Değiştirilmiş metin ya da eksik imza → Kurul incelemesi (m. 14/7). Taraf/içerik değişikliği ya da sona ermede yeniden bildirim (m. 14/8). → DPA'da standart sözleşmeyi "uyarlayan" ya da onunla çelişen kloz 🔴; ticari hükümleri ayrı belgeye taşı.
   - Hangi standart sözleşme metninin (aktarım yönüne göre) kullanılacağını Kurul'un ilan ettiği metinlerden kullanıcıya teyit ettir; metin araçta yoksa "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.kvkk.gov.tr/".
3. O da yoksa **arızi aktarım** (m. 9/6-a–f) — yalnız arızi: düzenli olmayan, tek ya da birkaç sefer gerçekleşen, süreklilik arz etmeyen ve olağan faaliyet akışında bulunmayan aktarım (Yön. m. 16/1). Süregelen bulut/SaaS ilişkisi arızi değildir.
4. **Veri işleyenin aktarımı** veri sorumlusunun sorumluluğunu kaldırmaz; veri sorumlusu tedbirlerin veri işleyence alınmasını sağlamakla yükümlüdür (Yön. m. 7/2); bildirim yükümlüsü veri işleyense talimat beklemeden bildirir (Yön. m. 7/3).
5. **Sonraki aktarımlar** (alt işleyen zinciri) için de aynı güvenceler (m. 9/8).

- Yurt dışındaki sunucuda barındırmanın yurt dışı aktarım sayılması **yerleşik Kurul uygulaması — kararı çek** (`tr_semantik_ara(kurum="kvkk", query="yurt dışında bulunan sunucu bulut hizmeti aktarım")`).
- Yurt dışı aktarım var, mekanizma yok → 🔴 (hukuka uygun aktarım yolu yok).
- **AB tarafı** (veri aktaran AB'de ya da GDPR uygulanıyor): `eu_search_eu_law(query="standard contractual clauses transfer of personal data to third countries")` → CELEX 32021D0914; veri sorumlusu–veri işleyen klozları için `eu_search_eu_law(query="standard contractual clauses controllers processors")`; Türkiye hakkında AB yeterlilik kararı olup olmadığını araçla kontrol et, ezberden söyleme. **İngiltere:** `uk_search_legislation(query="Data Protection Act 2018")`. Aktarım etki değerlendirmesi gerekip gerekmediğini işaretle; değerlendirmeyi bu skill yapmaz.

### Veri işleyen olduğumuzda — savunma

| Kloz | Risk | Pozisyon |
|---|---|---|
| Alt işleyen veto hakkı | Altyapıyı müşteri müşteri onaya bağlar | Playbook (bildirim + itiraz) |
| Kısa bildirimli yerinde denetim | Ölçekte yürümez | Rapor/sertifika + sınırlı yerinde denetim; m. 12/3 makul bir denetim hakkını haklı kılar |
| Aşırı kısa ihlal bildirimi | Olay anlaşılmadan bildirim | Playbook süresi; içerik kademeli tamamlanır |
| Katı veri yerelleştirme | Mimari uymayabilir | Gerçekte taahhüt edilebilen; bankacılıkta 5411 m. 73 BDDK kararları |
| Sınırsız sorumluluk / ceza tazmini | Şirketi batırabilir | Playbook; kast/ağır kusur dışında tavan (TBK m. 115/1) |
| Açık uçlu "talimat" yetkisi | Sınırsız operasyonel kontrol | "Sözleşmede belgelenen ya da yazılı kararlaştırılan talimat" |
| Çok kısa silme süresi | Yedek/log nedeniyle imkânsız | Playbook; yedek rotasyonu istisnası belgelenir |
| Standart sözleşmeyi değiştiren kloz | Kurul incelemesi, m. 18/1-d riski | Metin değiştirilmeden; ticari hükümler ayrı |

### Veri sorumlusu olduğumuzda — koruma

| Kloz | Açık | Talep |
|---|---|---|
| Alt işleyen listesi yok | Verimize kim dokunuyor bilinmez | Yayımlanmış güncel liste + önceden bildirim |
| "Sektör standardı güvenlik" | m. 12/2 müşterek sorumluluk bizde | Somut tedbir eki ya da adlandırılmış standart (ISO 27001, SOC 2) |
| İhlal bildirim süresi yok | m. 12/5 yükü bizde | Playbook süresi (Kurul uygulamasına yetişecek kadar kısa) |
| Denetim hakkı yok | m. 12/3 yerine getirilemez | En az bağımsız denetim raporu |
| "Hizmet geliştirme" / model eğitimi | Tedarikçi o amaçla veri sorumlusu olur; m. 8, m. 10 | Sil; işleme yalnız hizmet sunumu için |
| Yurt dışı aktarım mekanizması yok | m. 9 | Standart sözleşme + 5 iş günü bildirim takvimi + bildirimi kimin yapacağı |
| Silme taahhüdü yok | m. 7 | Süre + talep üzerine imha tutanağı |

## Aydınlatma metni ve gizlilik politikası tutarlılığı

- DPA'daki amaçlar aydınlatma metninde var mı (m. 10/1-b)? Aktarılan alıcılar ve amaçları (m. 10/1-c)? VERBİS'teki alıcı grupları ve yurt dışı aktarım bilgisi (m. 16/3-ç, d) DPA ile örtüşüyor mu?
- Politika "verilerinizi yurt dışına aktarmayız" diyor, DPA yurt dışı bulut içeriyor → çelişki.

Uyumsuzluğu bayrakla; çoğunlukla eski olan politikadır, ama biri değişmeli (→ `/privacy-legal:reg-gap-analysis`). *Karşılaştırmalı not:* ABD eyalet yasalarındaki "satış/paylaşım" nitelendirmesinin Türk hukukundaki karşılığı aktarım şartlarıdır (m. 8–9).

## Redline inceliği

En küçük düzeltme: kelime → ifade → alt bent → cümle → ancak gerekirse tüm madde. Tüm maddeyi değiştirdiysen ileti notunda söyle: "8.2'yi değişiklikler kapsamlı olduğu için işaretlemek yerine yeniden yazdık; farkı birlikte geçebiliriz." Küçük redline dikkatli okunduğunu gösterir.

## ArthurLegal MCP

```
tr_mevzuat_madde_getir(number="6698", madde_no=["3","6","8","9","10","12","16","18"])
tr_mevzuat_ara(query="Kişisel Verilerin Yurt Dışına Aktarılmasına", types=["KKY"])      → mevzuat_id
tr_mevzuat_madde_getir(mevzuat_id=<yukarıdaki>, madde_no=["7","14","15","16"])
tr_mevzuat_madde_getir(number="6098", madde_no=["20","21","115"])
tr_semantik_ara(kurum="kvkk", query="veri ihlali bildirimi 72 saat")
tr_kurum_karari_ara(kurum="kvkk", query="veri ihlal bildirimi")   ← yalnız son sayfaları tarar; sıra tarihe göre değil
eu_get_document_text(celex="32016R0679", offset=211000)           ← GDPR Art. 28 (veri işleyen sözleşmesi); Art. 33 (ihlal) ≈ offset 221500
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde için: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/". Atıf etiketi: `[ArthurLegal TR — 6698 m. X — GG.AA.YYYY]`, `[ArthurLegal EU — CELEX … — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`.

## Çıktı

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# DPA İncelemesi: [Karşı taraf]

**Yön:** [Veri işleyeniz / Veri sorumlusuyuz]   **Tarih:** [GG.AA.YYYY]   **Bağlı olduğu sözleşme:** [ana sözleşme / tek başına]

## ⚠️ İnceleyen notu
- **Önceki çıktılar:** [triage/PIA/DPA — tarih ve sonuç / yok]
- **Sektörel katman:** [yok — kontrol edildi / 5411 / sağlık / …]
- **Yurt dışı aktarım:** [yok / yeterlilik / standart sözleşme — bildirim son günü GG.AA.YYYY / BCR / taahhütname / arızi]
- **Kaynaklar:** ArthurLegal MCP — [madde sayısı, Kurul kararı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]
- **Eskalasyon:** [yok / [isim] — hangi kloz]

## Sonuç
[İki cümle: imzalanabilir mi, neyin değişmesi gerekir.]
**Bulgular:** [N]🟢 [N]🟡 [N]🟠 [N]🔴

## Madde madde
[Her konu için kısa blok: karşı tarafın metni · playbook · fark · risk · önerilen redline]

## Aydınlatma / politika tutarlılığı
[🟢 Tutarlı | 🟡 Bayraklar: liste]

## Önerilen redline'lar
[Toplu, gönderilmeye hazır — iç gerekçe olmadan]

## Karşı taraf kabul etmezse
[Her konu için playbook fallback'i ya da `## Escalation` yönlendirmesi]
```

## Sonuç doğuran işlem kapısı (DPA'nın imzalanması)

İnceleme araştırmadır; **imza** (ya da imzalı nüshayı iade, karşı tarafın platformunda otomatik kabul, imzacıya talimat) hukuki işlemdir. Bu aşamaya geçmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> DPA imzalamak şirketi ilgili kişilere ve Kurula karşı somut veri koruma yükümlülüklerine bağlar; standart sözleşme içeriyorsa 5 iş günlük bildirim süresi imzayla başlar. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: karşı taraf, yön (veri işleyen / veri sorumlusu), playbook'tan sapan klozlar ve nasıl çözüldükleri, yurt dışı aktarım yolu ve bildirim takvimi, açık fallback kararları; avukata sorulacak üç soru. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan imzaya yönlendirme.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu incelemeye göre uyarla (redline'ı gönder, eskalasyon, ek olgu iste — ör. alt işleyen listesi, standart sözleşme bildirimini takvime al, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Sıfırdan DPA yazmaz; cevap "şablonumuzu kullanalım" ise şablonu profildeki `## Seed documents` yolundan alır.
- Aktarım etki değerlendirmesini kendisi yapmaz; gerektiğini işaretler.
- Fallback dışındaki şartları kabul etmeye karar vermez; `## Escalation`'a göre yönlendirir.

---

## /privacy-legal:dsar-response

---
name: dsar-response
description: >
  İlgili kişi başvurusu (KVKK m. 11, m. 13) — talebi m. 11 haklarına ayırır,
  başvuru şeklini ve kimliği (Veri Sorumlusuna Başvuru Usul ve Esasları
  Hakkında Tebliğ) kontrol eder, 30 günlük cevap süresini izler, veriyi sistem
  sistem bulur, m. 28 istisnalarını ve silmenin sınırlarını (m. 7, kanuni
  saklama süreleri) değerlendirir; alındı ve esas cevap yazılarını taslak
  olarak çıkarır. "Başvuru geldi", "verilerimi istiyor", "verilerimin
  silinmesini istiyor", "KVKK başvurusu", "DSAR", "unutulma hakkı" denince ya
  da bir başvuru metni yapıştırıldığında kullan.
argument-hint: "[başvuruyu yapıştırın ya da anlatın]"
---

# /dsar-response — İlgili Kişi Başvurusu (KVKK)

İlgili kişi başvurusunun bir süresi (30 gün), bir usulü (kimlik → veri → istisna → cevap) ve ters gidebileceği çok yeri vardır. Bu skill her adımı yürütür ve cevabı **taslak** olarak hazırlar; göndermez. Esas cevabın gövdesi paketteki `kvkk-m11-cevap-sablonu.md`'dir. Kural ezberden söylenmez: atıf yapılan her madde `tr_mevzuat_madde_getir` ile çekilir.

**Başvuruyu yapıştırmadan önce:** başvuru ilgili kişinin kişisel verisini taşır. Gereksiz ekleri (kimlik fotokopisi, ilgisiz yazışma) çıkar ya da maskele (`pii-redaksiyon-rehberi.md`, `arthur-mask-rehberi.md`); dosya adlarına ilgili kişinin adını yazma.

## ⏰ ÖN-KONTROL — Süre (her çalıştırmada)

| Durum | Süre | Dayanak |
|---|---|---|
| Başvurunun sonuçlandırılması | Talebin niteliğine göre en kısa sürede, **en geç 30 gün**; kural olarak ücretsiz | 6698 m. 13/2; Tebliğ m. 6/5 |
| Sürenin başlangıcı | Yazılı başvuruda evrakın veri sorumlusuna/temsilcisine tebliğ tarihi; diğer yöntemlerde başvurunun ulaştığı tarih | Tebliğ m. 5/4-5 |
| Ret, yetersiz cevap ya da cevapsızlık → Kurula şikâyet | İlgili kişi cevabı öğrendiği tarihten **30 gün**, her hâlde başvuru tarihinden **60 gün** içinde; başvuru yolu tüketilmeden şikâyet olmaz | 6698 m. 14/1-2 |
| Kurul bilgi/belge isterse | **15 gün** içinde gönderme; gerekirse yerinde inceleme imkânı | 6698 m. 15/3 |
| Kurul ihlal kararı verirse | Tebliğden itibaren gecikmeksizin, en geç **30 gün** içinde yerine getirme | 6698 m. 15/5 |
| Ticari elektronik iletiyi reddetme | Talep ulaştıktan sonra **3 iş günü** içinde gönderimi durdurma | 6563 m. 8/3 |

- 30 günü takvim günü olarak say (ihtiyatlı yol). Son güne ≤ 5 gün → 🔴 ACİL.
- Kimlik teyidi ya da eksik bilgi yazışmasının 30 günü durdurup durdurmadığı Kanun'da ve Tebliğ'de düzenlenmemiştir — **tartışmalı, Kurul kararlarını kontrol et**. İhtiyatlı yol: süre başvuru tarihinden işler; teyit isteğini ilk günlerde gönder.
- Eklenti ayarındaki iç SLA daha kısaysa onu uygula, kanuni sınırı not et.

## Destination check

- **İlgili kişiye alındı yazısı ve esas cevap** → dış belge: `## Outputs` başlığı **konmaz**; iç değerlendirme, risk notu, istisna tartışması girmez.
- **İstisna analizi, sistem tarama tablosu, iç not** → profilin `## Outputs` bölümündeki role göre üst başlık (avukatta "GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ"; sır saklama: Av. K. m. 36); mektuplardan ayrı dosya.
- **Kurula şikâyet üzerine savunma** → bu skill'in kapsamı dışında; burada yalnız olgu ve belge dökümü hazırlanır.

## ADIM 0 — Rol ve kapsam

- [ŞİRKET ADI] bu veri için **veri sorumlusu** mu, **veri işleyen** mi (6698 m. 3/1-ğ, ı)? Başvuru veri sorumlusuna yapılır (m. 13/1). [ŞİRKET ADI] veri işleyense talebi kendisi cevaplamaz; veri işleme sözleşmesindeki usulle veri sorumlusuna iletir ve sözleşmedeki yardım yükümlülüğünü yerine getirir (sözleşme için `/privacy-legal:dpa-review` çıktısına bak).
- Başvuran kendi verisini mi istiyor? m. 11 "kendisiyle ilgili" haklar tanır. Aile üyesi, vekil ya da işveren adına gelen talepte yetki belgesi ara; başkasının verisini verme.
- İlgili kişi ya da işleme AB/İngiltere'ye bağlıysa → aşağıda **Yabancı rejimler**.

## Bağlamı yükle

`company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DSAR process` (sistem listesi, kimlik teyidi yöntemi, iç SLA, rutin iş / eskalasyon ayrımı), `## Escalation`, `## Regulatory footprint` (yabancı rejim ve sektör satırları), `## Outputs`, `## Who's using this`. Sistem listesi boş ya da eskiyse bayrakla: nerede arayacağını bilmeden eksiksiz cevap verilemez.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/privacy-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Talebi sınıflandır (m. 11/1)

| Bent | Hak | Pratikte |
|---|---|---|
| a | Kişisel veri işlenip işlenmediğini öğrenme | "Hakkımda veri var mı?" |
| b | İşlenmişse buna ilişkin bilgi talep etme | Kategoriler, içerik, kopya talebi |
| c | İşlenme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme | |
| ç | Yurt içinde veya yurt dışında aktarıldığı üçüncü kişileri bilme | Alıcı listesi |
| d | Eksik veya yanlış işlenmişse düzeltilmesini isteme | |
| e | m. 7 şartları çerçevesinde silinmesini veya yok edilmesini isteme | Hesap kapatma, "unutulma" |
| f | (d) ve (e) işlemlerinin aktarıldığı üçüncü kişilere bildirilmesini isteme | Veri işleyenler, alıcılar |
| g | Münhasıran otomatik sistemlerle analiz sonucu aleyhe sonuca itiraz | Otomatik skor/kredi kararı |
| ğ | Kanuna aykırı işleme nedeniyle zararın giderilmesini talep etme | → eskalasyon |

- KVKK'da GDPR'daki **veri taşınabilirliği** ve **işlemenin kısıtlanması** ayrı haklar olarak sayılmamıştır; böyle bir talebi m. 11/1-b ve e çerçevesinde değerlendir, rejim farkını iç notta yaz. GDPR uygulanıyorsa aşağıya bak.
- Pazarlama iletisinden çıkma talebi KVKK başvurusu kılığında gelebilir; ticari elektronik iletide ret hakkı ayrıca 6563 m. 8'dedir (3 iş günü).
- Birleşik talep ("önce verilerimi gönderin, sonra silin") iki bağlı talep olarak yürür: önce bilgi/kopya, sonra silme.

### 2. Başvurunun şekli ve kimlik

- **Şekil:** yazılı ya da Kurul'un belirlediği yöntemler (m. 13/1). Tebliğ m. 5/1: yazılı; KEP; güvenli elektronik imza; mobil imza; ilgili kişinin daha önce bildirdiği ve sistemde kayıtlı e-posta; başvuru amaçlı yazılım/uygulama.
- **Zorunlu unsurlar (Tebliğ m. 5/2):** ad-soyad (yazılıysa imza); T.C. kimlik no, yabancılar için uyruk + pasaport ya da kimlik no; tebligata esas adres; varsa e-posta/telefon/faks; talep konusu. Eksikse hemen tamamlatma iste; eksikliğin süreye etkisi **tartışmalı**.
- **Dil:** Tebliğ m. 4/2 başvurunun Türkçe yapılmasını arar. Yabancı dildeki başvuruyu yalnız bu gerekçeyle reddetmenin Kurul önündeki sonucu **tartışmalı** — ihtiyatlı yol: cevapla ya da Türkçe başvuru iste, gerekçeyi kayda geçir.
- **Teyidi riske göre ayarla:** oturum açmış kullanıcı ya da kayıtlı e-postadan gelen bilgi talebi → çoğunlukla yeterli; silme, özel nitelikli veri ya da yüksek değerli hesap → ek teyit. Teyit için gerekenden fazla belge toplamak ölçülülük ilkesiyle (m. 4/2-ç) çatışabilir. Aşırı teyit başvuruyu engele çevirir; eksik teyit veriyi dolandırıcıya verir.
- Vekil → vekâletnamenin kapsamı; kanuni temsilci → temsil belgesi.

Teyit edilemezse (ilk günlerde gönder, 29. günde değil):

```
Başvurunuzun, kişisel verileri konu olan kişiden geldiğini teyit edemedik.
İşleme devam edebilmemiz için lütfen [teyit adımı]. Kimliği teyit edilemeyen
başvurular üzerine kişisel veri paylaşamıyoruz.
```

### 3. Veriyi bul

Eklenti ayarındaki sistem listesini tara; VERBİS kaydındaki veri kategorileri ve alıcı gruplarıyla (m. 16/3-c, ç, d) karşılaştır. Kayıtta olmayan bir işleme çıkarsa değişiklik derhâl bildirilir (m. 16/4); Veri Sorumluları Sicili Hakkında Yönetmelik m. 13/1: değişikliğin meydana geldiği tarihten itibaren 7 gün içinde VERBİS üzerinden → iç notta bayrakla.

| Sistem | Sorgulandı mı? | Veri var mı? | Ne |
|---|---|---|---|
| Ana veritabanı / ERP | | | |
| CRM | | | |
| Destek kayıtları / çağrı merkezi | | | |
| E-posta / SMS pazarlama | | | |
| Analitik | | | |
| Loglar | | | |
| Yedekler | | | (silmede rotasyon tarihi ayrıca yazılır) |
| Veri işleyenler (bulut, bordro, muhasebe) | | | (silme/düzeltmede bildirim — m. 11/1-f) |
| Fiziki arşiv (veri kayıt sisteminin parçasıysa) | | | m. 3/1-e, h |

### 4. İstisna ve sınır analizi

İyi niyetli dayanağı olan her istisnayı **öner**, belirsizleri işaretle; listeyi avukat daraltır. Açıklanan veri geri alınamaz; fazla önerilen istisna incelemede düzeltilir. Her önerinin yanına yaz: **"önerilen — ileri sürmeden önce avukat incelemesi gerekir; Kurul toptan istisna iddiasını sıkı inceler."**

| Dayanak | Kapsam | Etkisi |
|---|---|---|
| m. 28/1-a–d | Kanun hiç uygulanmaz: ev içi faaliyet; anonimleştirilerek resmî istatistik/araştırma; sanat, tarih, edebiyat, bilim ve ifade özgürlüğü (sınırlarıyla); kanunla yetkili kamu kurumlarının önleyici/istihbari faaliyetleri; yargı ve infaz makamlarının işlemleri | Özel şirkette nadir; yayın faaliyetinde (c) bendini değerlendir |
| m. 28/2-a | Suç işlenmesinin önlenmesi veya suç soruşturması için gerekli işleme | m. 10, m. 11 (zararın giderilmesi hariç) ve m. 16 uygulanmaz — **Kanun'un amacına ve temel ilkelerine uygun ve orantılı olmak kaydıyla** |
| m. 28/2-b | İlgili kişinin kendisinin alenileştirdiği veri | aynı |
| m. 28/2-c | Kamu kurumları ve kamu kurumu niteliğindeki meslek kuruluşlarının denetleme/düzenleme görevi, disiplin soruşturma veya kovuşturması | aynı |
| m. 28/2-ç | Bütçe, vergi ve mali konularda Devletin ekonomik ve mali çıkarlarının korunması | aynı |

**Silme talebinin sınırları:**
- Silme, işlenmesini gerektiren sebepler ortadan kalkınca doğar; diğer kanunlardaki hükümler saklıdır (m. 7/1-2). Usul: Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi Hakkında Yönetmelik (madde atfı yapacaksan maddeyi çek).
- Kanuni saklama örnekleri: VUK m. 253 (defter ve belgeler, ilgili yılı izleyen takvim yılından başlayarak 5 yıl); TTK m. 82/5 (m. 82/1-a–d'deki defter ve belgeler 10 yıl; başlangıç m. 82/6). Saklanan her kategori için dayanağı cevapta yaz.
- Uyuşmazlık: bir hakkın tesisi, kullanılması veya korunması için zorunlu işleme (m. 5/2-e; özel nitelikli veride m. 6/3-d). Bekleyen ya da muhtemel davada silme talebi + delil koruma çatışması → avukat karar verir.
- Gerekçesiz silmeme ceza riskidir: m. 7'ye aykırı olarak silmeyen veya anonim hâle getirmeyen TCK m. 138'e göre cezalandırılır (6698 m. 17/2).

**Diğer sorular:**
- Kayıtta başkasının verisi var mı (destek yazışmasındaki diğer kişiler, CC listeleri)? → karart.
- Ticari sır, iç değerlendirme notu, avukat yazışması: m. 28'de açık bir ticari sır ya da meslek sırrı istisnası yoktur — **tartışmalı; Kurul kararlarını ara**. Avukatın kendi sır saklama yükümlülüğü Av. K. m. 36'dadır.
- Yedekler: teknik imkânsızlık genel bahane değildir; rotasyon tarihiyle belgelenir.

**Paket şablonu:** `kvkk-m11-cevap-sablonu.md` m. 28/1 – m. 28/2 ayrımına ve m. 14/1 şikâyet sürelerine (öğrenmeden 30 gün, her hâlde başvurudan 60 gün) göre günceldir; ret paragrafında bendi somut gerekçeyle yaz.

### 5. Cevap — iki yazı

KVKK ayrı bir alındı yazısı istemez; ama erken alındı yazısı mükerrer başvuruyu ve erken şikâyeti azaltır (iyi uygulama). İkisini birleştirip 30. günde tek yazı gönderme.

**5a — Alındı yazısı** (aynı gün – 3 iş günü):

```
Konu: [GG.AA.YYYY] tarihli kişisel veri başvurunuz

Sayın [Ad Soyad],

[Başvuru tarihi] tarihinde ulaşan başvurunuzu aldık.

Başvurunuzu şöyle anlıyoruz: [tek cümle — ör. "hesabınızla ilişkili kişisel
verilerin ve aktarıldığı üçüncü kişilerin bildirilmesi, ardından hesabınızın
silinmesi"].

Başvurunuzu 6698 sayılı Kanun'un 13. maddesi uyarınca en geç [başvuru tarihi
+ 30 gün] tarihine kadar sonuçlandıracağız. [Teyit eksikse: İşleme devam
edebilmemiz için [teyit adımı] gerekmektedir; bu arada çalışmaya devam ediyoruz.]

Başvurunuz ücretsizdir. [İşlem ayrıca maliyet gerektirirse: Kurulca belirlenen
tarifedeki ücret söz konusu olabilir; bu durumda önceden bilgi vereceğiz.]

İletişim: [veri sorumlusu irtibat bilgisi]
```

**5b — Esas cevap:** gövde `kvkk-m11-cevap-sablonu.md`. Zorunlu unsurlar (Tebliğ m. 6/4): veri sorumlusu/temsilci bilgisi; başvuru sahibinin kimlik ve iletişim bilgileri; talep konusu; veri sorumlusunun açıklamaları. Talep kabul edilir ya da **gerekçesi açıklanarak** reddedilir; cevap yazılı veya elektronik ortamda bildirilir (m. 13/3). Kabulde gereği en kısa sürede yerine getirilir ve ilgili kişiye bilgi verilir (Tebliğ m. 6/6). Ücret: yazılı cevapta 10 sayfaya kadar ücret yok; aşan sayfa ve kayıt ortamı için Tebliğ m. 7 (sayfa başı tutar Tebliğ metninde — güncelliğini teyit et); başvuru veri sorumlusunun hatasından kaynaklanıyorsa ücret iade edilir (m. 13/3).

Silme cevabına ek tablolar:

```
Silinen / yok edilen / anonim hâle getirilen:
| Kategori | Sistem | Yöntem | Tarih |

Saklanan ve nedeni:
| Kategori | Dayanak (kanun + madde) | Saklama sonu |

Bildirim yapılan üçüncü kişiler (m. 11/1-f): [liste]
```

Her iki yazı da **TASLAK**: gönderilen cevap veri sorumlusunu bir pozisyona bağlar, istisnadan fiilen vazgeçme sonucu doğurabilir ve m. 14 şikâyet süresini başlatır. Avukat onayı olmadan gönderilmez.

### 6. Kayıt

Başvuru tarihi ve kanalı; kimlik teyit tarihi; alındı ve cevap tarihleri; verilen / silinen / saklanan; ileri sürülen istisna ve dayanağı; işi yürüten. Takip aracı yoksa matter klasöründe log dosyası (ilgili kişinin adı dosya adında olmaz).

## Eskalasyon tetikleyicileri

Profilin `## Escalation` bölümüne göre, en az şu hâllerde:
- Başvuran ya da vekili karşı taraf, muhtemel davacı, gazeteci ya da çalışan/eski çalışan uyuşmazlığının tarafı
- Olağandışı kapsam ("hakkımdaki tüm iç yazışmalar")
- Zararın giderilmesi talebi (m. 11/1-ğ) ya da tazminat imâsı
- Bekleyen dava veya delil koruma ihtiyacı varken silme talebi
- Önceki cevaba itiraz; Kurul'a şikâyet ya da Kurul yazısı
- Özel nitelikli veri (m. 6/1), çocuk verisi, toplu/kampanya başvurusu

## Yabancı rejimler

- **AB (GDPR):** `eu_get_document_text(celex="32016R0679")` ile süre ve uzatma (Art. 12), haklar (Art. 15–22) ve sınırlamalar (Art. 23) metnini çek; ezberden yazma. KVKK ile birlikte uygulanıyorsa her hak ve süre için iki rejimi yan yana koy, farkı iç notta yaz.
- **İngiltere:** `uk_search_legislation(query="Data Protection Act 2018")`, ardından `uk_get_section`.
- **Almanya ek kuralları:** `de_gesetz_ara(sorgu="Bundesdatenschutzgesetz")`.
- Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."
- *Karşılaştırmalı not:* ABD eyalet gizlilik yasalarının kendi cevap süreleri ve uzatma mekanizmaları vardır; yalnız CourtListener bağlayıcısı kuruluysa `courtlistener-rehberi.md` üzerinden araştırılır, ezberden yazılmaz.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6698", madde_no=["3","7","11","13","14","15","28"])
tr_mevzuat_ara(query="Veri Sorumlusuna Başvuru Usul ve Esasları", types=["TEBLIGLER"])  → tr_mevzuat_getir(mevzuat_id=...)
tr_mevzuat_ara(query="Kişisel Verilerin Silinmesi, Yok Edilmesi", types=["KKY"])
tr_mevzuat_madde_getir(number="213", madde_no=["253"])
tr_mevzuat_madde_getir(number="6102", madde_no=["82"])
tr_semantik_ara(kurum="kvkk", query="ilgili kişinin başvurusuna süresinde cevap verilmemesi")
tr_semantik_ara(kurum="kvkk", query="silme talebi kanuni saklama yükümlülüğü")
tr_kurum_karari_ara(kurum="kvkk", query="başvuru")   ← yalnız son ~30 özeti tarar; arşiv için tr_semantik_ara
tr_kurum_karari_getir(kurum="kvkk", id=<sonuçtaki id>)
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Araç veri getiremezse: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" (Kurul kararında https://www.kvkk.gov.tr/). Atıf etiketi: `[ArthurLegal TR — 6698 m. X — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`.

## Çıktı (iç not — mektuplardan ayrı)

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# İlgili Kişi Başvurusu — [Başvuru no / takma ad] — [Tarih]

## ⚠️ İnceleyen notu
- **Talep:** [m. 11/1 bentleri]
- **Süre:** başvuru GG.AA.YYYY → son gün GG.AA.YYYY 🔴/🟠/🟡
- **Kimlik:** [teyit edildi / bekliyor — adım]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) — [madde sayısı, Kurul kararı sayısı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]
- **Eskalasyon:** [yok / [isim] — neden]

## Sistem taraması
[tablo]

## Önerilen istisnalar ve saklama gerekçeleri
[her biri: dayanak (madde/fıkra/bent), olgu, "önerilen — avukat incelemesi"]

## Yazılar
[5a ve 5b taslaklarının dosya yolları]

## Açık işler
- [ ] ...
```

## Sonuç doğuran işlem kapısı (cevabın gönderilmesi)

Herhangi bir yazıyı ilgili kişiye gönderme aşamasına geçmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> İlgili kişi başvurusuna verilen cevabın hukuki sonucu vardır: içerik, ileri sürülen istisnalar ve eksik bırakılanlar Kurul incelemesine açıktır; yanlış beyan idari yaptırım riskine dönüşür. Bu cevabı bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: ilgili kişi (takma adla), talep edilen haklar, uygulanacak rejim(ler), sistem taramasının sonucu, verilmeyen kısım ve dayandığı istisna, kimlik teyidi durumu, son gün; avukata sorulacak üç soru (istisnalar sağlam mı, silme mi saklama mı, cevap şikâyete hazır mı). Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan gönderime hazır metin üretme; "TASLAK" işaretli çıktı serbest.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu başvuruya göre uyarla (cevabı tamamla, kimlik teyidi iste, eskalasyon, veri işleyene bildirim, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Sistemleri kendisi sorgulamaz; kontrol listesini yürütür, sorguyu insan ya da bağlı araç yapar.
- Sınırdaki istisnada karar vermez; avukata işaretler.
- Cevabı göndermez: taslak → inceleme → gönderimi insan yapar.

---

## /privacy-legal:matter-workspace

---
name: matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkilin ya da dosyanın bağlamının diğerine sızmamasını
  sağlar; veri sorumlusu müvekkil ile onun veri işleyeninin aynı büroda
  bulunabilmesi nedeniyle çapraz okuma kapalı tutulur. Çok müvekkilli avukat
  "yeni matter", "matter değiştir", "matter'larımı listele", "matter'ı kapat"
  dediğinde ya da yalnız uygulama düzeyinde çalışmak istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil ve dosya üzerinde çalışır. Matter çalışma alanı her dosyanın bağlamını diğerlerinden ayrı tutar. Bu skill o alanları yönetir.

## Alt komutlar

- `/privacy-legal:matter-workspace new <slug>` — yeni matter oluştur, kısa ön görüşme yap, `matter.md` yaz
- `/privacy-legal:matter-workspace list` — matter'ları durum ve aktiflik işaretiyle listele
- `/privacy-legal:matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/privacy-legal:matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/_archived/` altına taşı; asla silme)
- `/privacy-legal:matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünün dolu olduğunu teyit et. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli kurum içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/privacy-legal:cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok."
2. `$ARGUMENTS`'ın ilk kelimesine göre dallan:
   - `new` → ön görüşme, `matters/<slug>/matter.md` yaz, `history.md` ve `notes.md` oluştur.
   - `list` → `matters/*/matter.md` dosyalarını tara, tablo bas, aktif olanı işaretle.
   - `switch` → uygulama CLAUDE.md'sindeki `Active matter:` satırını güncelle.
   - `close` → `matters/<slug>/` klasörünü `matters/_archived/<slug>/` altına taşı, kapanış tarihini `history.md`'ye yaz.
   - `none` → `Active matter:` satırını `none — practice-level context only` yap.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` şablondaki gibi kalır; diğer skill'ler bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/privacy-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, rol, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-veri-isleyen-sozlesmesi`, `xyz-ihlal-2026`, `musteri-kurul-sikayeti`. Gerçek ad yerine takma ad kullanılabilir. Aynı slug arşivde varsa arşivdeki `_archived/<slug>/` altında korunur; yeni matter'a başka slug ver.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Veri işleyen sözleşmesinde iki taraf, ihlal dosyasında veri sorumlusu ile tedarikçisi ya da şikâyette ilgili kişi ile veri sorumlusu karşı karşıya gelebilir. Sor: "Bu matter için çatışma kontrolü yapıldı mı?" Bu skill kontrolü kendisi yapmaz ve bu amaçla başka matter'ları okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz taraf (kurum içiyse iç birim)
   - **Müvekkilin bu işteki rolü** — veri sorumlusu / veri işleyen / ilgili kişi / ikisi (faaliyet bazında)
   - **Karşı taraf** — veri işleyen, veri sorumlusu, ilgili kişi, alt işleyen, yurt dışındaki alıcı (birden fazla olabilir)
   - **Matter türü** — PIA (işleme faaliyeti) | veri işleyen sözleşmesi incelemesi | ilgili kişi başvurusu | Kurula şikâyet / resen inceleme | veri ihlali | yurt dışı aktarım (standart sözleşme, bağlayıcı şirket kuralları, taahhütname) | VERBİS | idari para cezasına itiraz | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (yüksek, çapraz bağlamda ek dikkat demektir)
   - **Kritik süreler** — varsa, aşağıdaki listeden
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, hangi veri kategorileri (özel nitelikli var mı)
   - **Matter'a özel sapmalar** — ör. "müvekkil ihlal bildirimini 24 saatte istiyor", "karşı taraf stratejik ortak — ilişkiyi koruyan ton"
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/privacy-legal:matter-workspace switch <slug>`)"

**Kritik süre listesi** (doğrulanmış; matter'a uyanı yaz):
- İlgili kişi başvurusu: en geç otuz gün (KVKK m. 13/2).
- Kurula şikâyet: veri sorumlusunun cevabını öğrenmeden itibaren otuz, her hâlde başvurudan itibaren altmış gün; başvuru yolu tüketilmeden şikâyet olmaz (m. 14/1-2). Kurul şikâyete altmış gün içinde cevap vermezse talep reddedilmiş sayılır (m. 15/4).
- Kurul incelemesi: istenen bilgi ve belgeler on beş gün içinde gönderilir; hukuka aykırılığın giderilmesi kararı tebliğden itibaren en geç otuz gün içinde yerine getirilir (m. 15/3, 15/5).
- Veri ihlali: en kısa sürede ilgilisine ve Kurula bildirim (m. 12/5). Kurul kararındaki somut süreyi araçla bul; bulunamazsa: UYARI: veri çekilemedi, teyidiniz gerekli: https://www.resmigazete.gov.tr/
- Standart sözleşme: imzaların tamamlanmasından itibaren beş iş günü içinde Kuruma bildirim; taraf ya da içerik değişikliği ve sona ermede de bildirim (KVKK m. 9/5; Yurt Dışına Aktarım Yönetmeliği m. 14/5, 14/8).
- VERBİS: kayıtlı bilgideki değişiklik yedi gün içinde (Veri Sorumluları Sicili Hakkında Yönetmelik m. 13).
- İdari para cezası: Kurulca verilen cezaya karşı idare mahkemesinde dava (KVKK m. 18/3). KVKK'nın çektiğimiz maddelerinde özel dava süresi yok; özel kanunda süre yoksa idare mahkemesinde dava açma süresi altmış gündür (İYUK m. 7/1). **Tartışmalı — içtihadı kontrol et:** `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="6698 idari para cezası dava açma süresi")`; dönen kararın künyesini birebir kullan. 1/6/2024 itibarıyla sulh ceza hâkimliklerinde görülmekte olan başvurular orada görülmeye devam eder (KVKK geçici m. 3/2).

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar:

| Slug | Müvekkil | Rol | Tür | Durum | Açılış | Aktif |
|---|---|---|---|---|---|---|

Aktif olanı `*` ile işaretle. `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

1. `matters/<slug>/matter.md` var mı bak; yoksa `new <slug>` öner.
2. `Active matter: <slug>` olarak güncelle.
3. Doğru matter'da olduğunu teyit etmesi için `matter.md` özetini göster (rol ve kritik süre dahil).

### `close <slug>`

1. `matters/<slug>/` var mı bak.
2. `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle.
3. `matters/<slug>/` → `matters/_archived/<slug>/` taşı.
4. Kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap.

### `none`

Yalnız `Active matter:` satırını `none — practice-level context only` yapar; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar
**Müvekkil:** [ad] — **Rol:** [veri sorumlusu / veri işleyen / ilgili kişi]
**Karşı taraf:** [ad(lar) ve rolleri]

## Matter türü
[tür — tek satır gerekçe]

## Kritik süreler
- [ör. başvuru tarihi: …, otuz günlük süre sonu: …; standart sözleşme imza tarihi: …, bildirim son günü: …]

## Ana olgular
[2-5 cümle; veri kategorileri, özel nitelikli veri, yurt dışı aktarım varsa ülke]

## Matter'a özel sapmalar
- [ör. "İhlal bildirimi: müvekkil 24 saat istiyor, ev standardı farklı."]

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
[matter.md dışında saklanmaya değer ilk bağlam — ör. "Karşı tarafın sözleşme taslağı üzerine açıldı."]
```

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurma yasağını (Av. K. m. 36) ve aynı büroda zıt tarafların bulunabilmesinden doğan çatışma riskini (m. 38) destekler. Matter dosyaları da kişisel veri içerir; erişimi işin gerektirdiği kişilerle sınırlı tut.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş sözleşmede alt işleyen duruşumuzu karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil. Matter dosyalarındaki kişisel veriler, ilgili mevzuatta öngörülen veya işlendikleri amaç için gerekli olan süre kadar muhafaza edilir (KVKK m. 4/2-d); süre büronun/şirketin saklama ve imha politikasına göre belirlenir.
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.

---

## /privacy-legal:pia-generation

---
name: pia-generation
description: >
  Yeni bir özellik, ürün ya da veri işleme faaliyeti için ev formatında kişisel
  veri etki değerlendirmesi (PIA) yazar. KVKK'da genel bir etki değerlendirmesi
  yükümlülüğü yoktur; değerlendirme m. 4 ilkeleri, m. 5–6 işleme şartları,
  m. 10 aydınlatma, m. 12 veri güvenliği ve m. 9 aktarım ekseninde iyi uygulama
  olarak kurulur; AB'ye dönük işlemede GDPR Art. 35 araçla çekilir. "PIA yaz",
  "etki değerlendirmesi", "bu özellik için PIA gerekir mi", "gizlilik
  incelemesi" denince ya da yeni bir veri işleme faaliyeti anlatıldığında
  kullan.
argument-hint: "[özellik adı ya da açıklaması; varsa ürün gereksinim belgesi]"
---

# /pia-generation — Kişisel Veri Etki Değerlendirmesi (PIA)

PIA, ürün ekibiyle yapılan bir konuşmanın kaydıdır: hangi veri, neden, ne kadar süre, kim görüyor, ne ters gidebilir. Bu skill konuşmayı yapılandırır ve sonucu ekibin formatında (kurulumda örnek PIA'dan öğrenilen) yazar. Kural ezberden söylenmez; her madde araçtan çekilir.

## Hukuki çerçeve (önce bunu bil)

- **KVKK:** 6698'de GDPR Art. 35 benzeri genel bir etki değerlendirmesi yükümlülüğü yoktur; Kanun metninde "etki değerlendirmesi" ifadesi geçmez (`tr_mevzuat_icinde_ara(number="6698", query="etki değerlendirmesi")` — yeni değişiklik ihtimaline karşı yeniden tara). PIA burada **iyi uygulama ve ispat aracıdır**: m. 4 ilkelerine uyumu ve m. 12/1'deki "uygun güvenlik düzeyi"ne yönelik tedbirleri belgelemenin düzenli yolu. PIA'yı "kanunen zorunlu" diye sunma.
- **Kurul:** karar özetleri `tr_semantik_ara(kurum="kvkk", …)` ile aranır (`tr_kurum_karari_ara(kurum="kvkk")` yalnız son sayfaları tarar). Kurum'un yayımladığı rehberler ArthurLegal araçlarında yoktur; bir rehbere dayanacaksan kullanıcıdan teyit iste ve "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.kvkk.gov.tr/" yaz.
- **AB'ye dönük işleme:** GDPR'ın uygulanıp uygulanmadığını Art. 3'ü çekerek belirle. Uygulanıyorsa veri koruma etki değerlendirmesi (VKED/DPIA) zorunlu olabilir; metni ezberden yazma: `eu_get_document_text(celex="32016R0679", offset=224000)` ile Art. 35–36'yı çek. Çekilen metne göre Art. 35(3) özellikle üç hâli sayar (otomatik işlemeye dayalı, hukuki ya da benzeri önemli etki doğuran sistematik ve kapsamlı değerlendirme; özel kategori ya da mahkûmiyet verisinin büyük ölçekte işlenmesi; kamuya açık alanın büyük ölçekte sistematik izlenmesi); Art. 35(4) denetim makamlarının listelerini, Art. 35(7) asgari içeriği, Art. 36 yüksek kalıntı riskte önceden danışmayı düzenler `[ArthurLegal EU — CELEX 32016R0679 — 26.10.2026]`. Üye devlet listeleri ve uygulaması için ilgili ülke aracı (`de_gesetz_ara`, `nl_search_legislation`, `at_search_legislation`, `ie_search_acts` …); İngiltere `uk_search_legislation`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

## Destination check

Çıktı nereye gidiyor? Kullanıcı bir hedef söylediyse (kanal, dağıtım listesi, karşı taraf, "herkes") sır çevresinin içinde mi diye sor. Şirket geneli liste, karşı taraf, tedarikçi ve müvekkile giden iç çalışma ürünü korumayı zayıflatır. Hedef dışarıdaysa üç seçenek sun: (a) yalnız hukuk için başlıklı tam sürüm, (b) geniş dağıtım için arındırılmış sürüm, (c) ikisi. Başlık koyup metnin başlığın korumadığı yere yapıştırılmasına sessizce yardım etme.

## Bağlamı yükle

- `company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## PIA house style` (PIA'yı ne tetikler, örnek PIA'dan çıkarılan yapı, derinlik, kim onaylar), `## Regulatory footprint`, `## Privacy policy commitments`, `## Escalation`, `## Outputs`, `## Who's using this`. Örnek PIA yapısı varsa **onu kullan**: bu PIA ekibin diğer PIA'larına benzemeli.
- **Önceki çıktılar** (`## Outputs` klasörü): aynı faaliyet için `use-case-triage` (risk derecesi ve koşulları PIA'nın giriş noktasıdır), önceki `pia-generation` (yenisi neyin değiştiğini, neyin taşındığını söyler), kapsamdaki tedarikçiler için `dpa-review`. Bulunursa an: "Önceki triage ([tarih]) [risk] dedi ve [koşullar] istedi; bu PIA [hangisi karşılandı, hangisi kaldı]." / "Bu PIA [tarih] PIA'sının yerine geçer, çünkü [kapsam, yeni veri kategorisi, tedarikçi, mevzuat değişikliği]." **Ciddiyet tabanı:** triage yüksek risk dediyse PIA neyin değiştiğini söylemeden düşük risk sonucuna varamaz. Bulunamazsa yaz: "Bu faaliyet için önceki triage veya PIA yok; soğuk başlangıç."

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/privacy-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adım 0 — PIA gerekli mi?

1. **Ev tetiği** (`## PIA house style`) — ekibin cevabı.
2. **Zorunlu rejim:** KVKK tek başına zorunluluk doğurmaz. `## Regulatory footprint`'te GDPR/UK GDPR varsa Art. 35'i araçla kontrol et (yukarıda). Sektör mevzuatında risk değerlendirmesi hükmü olabilir (ör. bankacılık, sağlık, elektronik haberleşme) → `tr_mevzuat_icinde_ara(mevzuat_id=..., query="risk değerlendirmesi")`.
3. **Güçlü göstergeler** (zorunlu olmasa da yap): yeni teknoloji ya da yapay zekâ; çocuk verisi; özel nitelikli veri (m. 6/1 — biyometrik ve genetik dahil); ayrı toplanmış veri setlerinin birleştirilmesi; ayrımcılığa elverişli veri ya da çıkarım; münhasıran otomatik sistemlerle analiz edilip kişi aleyhine sonuç doğurabilecek işleme (m. 11/1-g itiraz hakkı); çalışan izleme; yurt dışı aktarım (m. 9); ilgili kişinin beklemeyeceği işleme.

Araştırma az sonuç verirse sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Ne zorunlu tetik ne ev tetiği varsa: "Bu faaliyet PIA gerektirmiyor görünüyor; soran olursa diye dosya için tek paragraflık gerekçe notu:" ve notu yaz.

## Mülakat (ürün ekibiyle)

Yazmadan önce cevapları al. Sohbet havasında olabilir; ekibe form gönderme. Ürün gereksinim belgesi varsa önce oradan çek.

### Ne ve neden
- Özellik/ürün/değişiklik ne? Kullanıcı için hangi sorunu çözüyor?
- Hangi kişisel veri? Alan alan say — "kullanıcı verisi" cevap değildir.
- Yeni toplama mı, eldeki verinin yeni amaçla kullanımı mı (m. 4/2-c, ç)?
- İşleme türü: saklama, analiz, paylaşma, otomatik karar?

### Hukuki sebep (m. 5–6)
- Her amaç için ayrı ayrı: m. 5/2-a–f şartlarından hangisi? Hiçbiri yoksa açık rıza (m. 5/1) — tanımı: belirli bir konuya ilişkin, bilgilendirilmeye dayanan ve özgür iradeyle açıklanan rıza (m. 3/1-a).
- **Sözleşme** (m. 5/2-c): sözleşmenin kurulması ya da ifasıyla **doğrudan** ilgili ve sözleşmenin taraflarına ait veri.
- **Meşru menfaat** (m. 5/2-f): işleme veri sorumlusunun meşru menfaati için **zorunlu** olmalı ve ilgili kişinin temel hak ve özgürlüklerine zarar vermemeli → denge testini yazılı yap (menfaat, zorunluluk, kişiye etkisi, makul beklenti, tedbirler).
- **Özel nitelikli veri** (m. 6/3, 7499 s.K. ile değişik): işleme yasaktır, ancak (a) açık rıza, (b) kanunlarda açıkça öngörülme, (c) fiili imkânsızlıkta hayat/beden bütünlüğü, (ç) ilgili kişinin alenileştirdiği ve alenileştirme iradesine uygun veri, (d) bir hakkın tesisi, kullanılması veya korunması, (e) sır saklama yükümlüsü kişi ya da yetkili kurumca sağlık hizmetleri, (f) istihdam, iş sağlığı ve güvenliği, sosyal güvenlik, sosyal hizmetler ve sosyal yardım alanlarındaki hukuki yükümlülük, (g) siyasi/felsefi/dini/sendikal amaçlı kâr amacı gütmeyen kuruluşlarda mevcut/eski üyeler hâllerinde mümkündür; her durumda Kurul'un belirlediği **yeterli önlemler** şarttır (m. 6/4) → `tr_semantik_ara(kurum="kvkk", query="özel nitelikli kişisel veri yeterli önlemler")`; düzenleyici kararın metni bulunamazsa UYARI satırı.
- Açık rızanın bir hizmetin ön şartı yapılması ve başka bir hukuki sebep varken ayrıca açık rıza alınması Kurul uygulamasında sorunlu görülür — **Kurul kararlarını ara** (`tr_semantik_ara(kurum="kvkk", query="açık rızanın hizmet şartına bağlanması")`).
- Ticari elektronik ileti varsa önceden onay şartı (6563 m. 6/1) ve ret hakkı (6563 m. 8) KVKK'dan ayrıca uygulanır.
- GDPR uygulanıyorsa hukuki sebepler için Art. 6 ve 9'u araçla çek; ezberden eşleme yapma.

### Kim ve nerede
- Şirket içinde kim görüyor (mühendis, destek, analist)? Erişim kontrolü ve kayıt (log) var mı?
- Üçüncü kişi ya da veri işleyen var mı (tedarikçi, iş ortağı, analitik)? → aktarım şartı (m. 8) ve sözleşme (`/privacy-legal:dpa-review`).
- Nerede saklanıyor; sunucu yurt dışında mı? → m. 9 yolu ve standart sözleşme bildirimi.
- Ne kadar süre? Saklama süresi gerekli süreyle sınırlı mı (m. 4/2-d); silme/anonimleştirme mekanizması var mı (m. 7)?

### Ne ters gidebilir
- Veri sızarsa kişiye zararı ne?
- Kazara da olsa ayrımcılığa yol açabilir mi?
- Kullanıcı bunun olduğunu öğrense şaşırır mı? ("Tüyler ürpertici" testi — hukuki ölçüt değil, faydalı.)
- Vazgeçme/itiraz imkânı var mı, olmalı mı?

## PIA'yı yaz

Profildeki örnek PIA yapısını kullan; yoksa aşağıdaki varsayılan. Başa profilin `## Outputs` bölümündeki role göre üst başlığı koy.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Kişisel Veri Etki Değerlendirmesi (PIA): [Özellik/Ürün]

**Hazırlayan:** [ad] | **Tarih:** [GG.AA.YYYY] | **Durum:** TASLAK / ONAYLANDI
**Ürün sahibi:** [ad] | **Gizlilik incelemesi:** [ad]

## ⚠️ İnceleyen notu
- **Önceki çıktılar:** [triage/PIA/DPA — tarih ve sonuç / soğuk başlangıç]
- **Rejimler:** KVKK [+ GDPR Art. 35 — zorunlu / değil] [+ sektör]
- **Kaynaklar:** ArthurLegal MCP — [madde, Kurul kararı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]

## Yönetici özeti
[İki cümle: ne olduğu, uygun olup olmadığı.]
**Genel risk:** [İnceleyen belirler: 🟢 Düşük / 🟡 Orta / 🟠 Yüksek / 🔴 Çok yüksek]

## 1. İşlemenin tanımı
**Ne:** [düz dille] · **Veri kategorileri:** [alanlar] · **İlgili kişiler:** [müşteri / son kullanıcı / çalışan …] · **Amaç:** [kullanıcıya faydasıyla] · **Yeni toplama mı?** [evet — alanlar / hayır]

## 2. Hukuki sebep
| Amaç | Şart (m. 5/2 bendi, m. 6/3 bendi ya da açık rıza) | Not (denge testi özeti / rızanın nasıl alındığı) |

## 3. Veri akışı
**Toplama · Saklama (sistem, konum, şifreleme) · Erişim · Paylaşım (alıcı, amaç, hangi sözleşme) · Yurt dışı aktarım (m. 9 yolu, bildirim tarihi) · Saklama süresi ve imha**

## 4. Genel ilkeler (m. 4/2)
| İlke | Karşılanıyor mu? | Not |
| Hukuka ve dürüstlük kurallarına uygunluk | | |
| Doğru ve gerektiğinde güncel | | |
| Belirli, açık ve meşru amaç | | |
| Amaçla bağlantılı, sınırlı ve ölçülü | | |
| Gerekli süre kadar muhafaza | | |

## 5. Aydınlatma ve politika tutarlılığı
| Taahhüt (aydınlatma metni / politika) | Tutarlı mı? | Not |
[m. 10/1 kalemleri: kimlik, amaç, alıcılar ve amaçları, yöntem ve hukuki sebep, m. 11 hakları]
[🟡 varsa: lansmandan önce metin güncellenir ya da işleme değişir]

## 6. Riskler ve tedbirler
| # | Risk (tasarıma bağlı, somut) | Olasılık | Etki | Tedbir | Durum (Tamam / Planlı / Açık) | Sahibi |
**Tedbirlerden sonra kalan risk:** [değerlendirme]

## 7. İlgili kişi hakları (m. 11)
| Hak | Kullanılabilir mi? | Nasıl |
| Bilgi ve erişim (a–ç) | | |
| Düzeltme (d) | | |
| Silme / yok etme (e) ve üçüncü kişilere bildirim (f) | | |
| Otomatik analiz sonucuna itiraz (g) | | |

## 8. Kayıt ve bildirimler
VERBİS güncellemesi gerekir mi (m. 16/3-4)? Standart sözleşme bildirimi (m. 9/5)? Aydınlatma metni güncellemesi?

## 9. Öneri
[ONAY / KOŞULLU ONAY / DEĞİŞİKLİK GEREKLİ / ONAY YOK]
**Koşullar:** - [ ] [lansmandan önce yapılacak somut iş — sahibi — tarih]
**Onay:** [ad, tarih]
```

## Risk kalitesi

Risk **somut ve tasarıma bağlı** olmalı; genel risk belgeyi şişirir ve okuru göz gezdirmeye alıştırır.

| Kötü | Neden kötü | Daha iyi |
|---|---|---|
| "Veri ihlali" | Her şeye uyar, bir şey söylemez | "Destek ekibi konum geçmişine yönetim panelinden erişim kaydı tutulmadan ulaşabiliyor; kötü niyetli bir çalışan kullanıcıyı fark edilmeden izleyebilir" |
| "KVKK'ya aykırılık" | Döngüsel — PIA uyumu değerlendirmek için var | Maddeyi ve açığı adlandır (ör. "m. 10 aydınlatmasında bu amaç yok") |
| "Kullanıcılar beğenmeyebilir" | Belirsiz | "Pazarlama iletisini reddetmiş kullanıcılar bu akışta da ileti alabilir; ret işareti bu akışta kontrol edilmiyor (6563 m. 8)" |

2–5 gerçek risk; 15 dolgu risk değil.

## Aydınlatma metni / politika farkı

Her PIA profildeki `## Privacy policy commitments` ile karşılaştırılır. Sık kayma:
- Metin "X, Y, Z'yi topluyoruz" diyor; yeni özellik W'yi topluyor → metin güncellenir ya da W toplanmaz.
- Metin "yurt dışına aktarmıyoruz" diyor; yeni özellik yurt dışı bulut kullanıyor → m. 9 yolu + metin güncellemesi.
- Metin saklamayı "üyelik süresince" diyor; yeni özellik hesap silindikten sonra da saklıyor.

Her uyumsuzluğu bayrakla; biri lansmandan önce değişmeli.

## Devir

- **Ürün ekibine:** sahibi ve tarihi olan koşul listesi. "Güvenliği artırın" değil: "yönetim panelindeki konum sorgusuna erişim kaydı ekleyin — sahibi: [mühendislik lideri] — lansmandan önce."
- **`/privacy-legal:reg-gap-analysis`:** PIA bir politika uyumsuzluğu bulduysa güncellemeyi o izler.
- **Onay süreci:** `## PIA house style`'daki onaylayan.

## Sonuç doğuran işlem kapısı (değerlendirmenin bir makama sunulması)

İç PIA araştırma ve belgelemedir. KVKK'da Kurul'a önceden danışma mekanizması yoktur; ama değerlendirme bir **AB denetim makamına** sunulabilir (Art. 36 önceden danışma) ya da Kurul bir inceleme/şikâyet sürecinde bilgi ve belge isteyebilir (Kurul'un istediği bilgi ve belge 15 gün içinde gönderilir: 6698 m. 15/3). Bu aşamaya geçmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> Bir makama sunulan değerlendirme denetim dosyasının parçası olur; önemli bir eksik ya da hata yaptırım riskine dönüşür. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: rejim ve makam, sunumun nedeni (zorunlu / talep üzerine / gönüllü), tespit edilen riskler, tedbirlerden sonra kalan risk, belirsiz noktalar; avukata sorulacak üç soru. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan sunuma yönlendirme.

## ArthurLegal MCP

```
tr_mevzuat_madde_getir(number="6698", madde_no=["3","4","5","6","7","9","10","11","12","16"])
tr_mevzuat_icinde_ara(number="6698", query="etki değerlendirmesi")
tr_semantik_ara(kurum="kvkk", query="meşru menfaat denge testi")
tr_semantik_ara(kurum="kvkk", query="açık rızanın hizmet şartına bağlanması")
tr_semantik_ara(kurum="kvkk", query="çalışanların izlenmesi kamera")
tr_mevzuat_madde_getir(number="6563", madde_no=["6","8"])
eu_get_document_text(celex="32016R0679", offset=224000)    ← Art. 35–36; Art. 3 (uygulama alanı) ≈ offset 156000; Art. 6 ve 9 ikisinin arasında
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde için "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/". Atıf etiketi: `[ArthurLegal TR — 6698 m. X — GG.AA.YYYY]`, `[ArthurLegal EU — CELEX … — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`; etiketleri silme ya da birleştirme.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu PIA'ya göre uyarla (koşul listesini ürün ekibine gönder, eskalasyon, ek olgu iste, DPA incelemesi başlat, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- İşlemeyi onaylamaz; PIA'yı insan imzalar.
- Bir denetim makamına sunulacak resmî VKED'yi kendiliğinden yazmaz; bu iç değerlendirmedir (resmî sürüm için GDPR Art. 35(7) asgari içeriğini araçla çekip ayrıca hazırla).
- Tedbiri tasarlamaz; neyin tedbir gerektirdiğini söyler, çözümü mühendislik tasarlar.

---

## /privacy-legal:policy-monitor

---
name: policy-monitor
description: >
  Aydınlatma metinlerini ve diğer gizlilik yüzeylerini uygulamayla güncel tutar;
  KVKK gelişmelerini (Kurul karar özetleri, Resmî Gazete, ikincil mevzuat, sektör
  kurumları) gerçek araçlarla izler. Üç mod: kayıtlı PIA, sözleşme incelemesi ve
  triyaj çıktılarını tarayarak kaymayı bulma; önerilen yeni bir uygulama için
  doğrudan sorgu; son taramadan bu yana dış gelişme taraması. "Aydınlatma metnimiz
  bunu kapsıyor mu", "X yapmaya başlayacağız, metin değişmeli mi", "politika
  taraması", "Kurul'dan yeni ne var" denince kullan.
argument-hint: "[önerilen uygulamanın tarifi | --sweep | --mevzuat]"
---

# /policy-monitor

**Tarama modu** (argümansız ya da `--sweep`): profilden çıktı klasörünü, aydınlatma metinlerini ve son tarama tarihini oku → o tarihten sonraki çıktıları tara → onaylanan uygulamaları metinlerle karşılaştır → açıkları ZORUNLU / TAVSİYE diye sınıflandır → her açık için mevcut metni alıntıla, açığı anlat, önerilen metni yaz → `Last policy sweep` tarihini güncelle. Sonunda dış gelişme taramasını öner.

**Doğrudan sorgu modu** (tarif ile): önerilen uygulamayı ayrıştır → veri kategorisi, amaç, hukuki sebep, alıcı grubu, yurt dışı aktarım, saklama, haklar ve bildirim bakımından metinle karşılaştır → kapsanan / eksik / çatışan + önerilen metin + zamanlama.

**Dış gelişme modu** (`--mevzuat`): `Last regulatory scan` tarihinden bugüne KVKK ve sektör gelişmelerini tara → her kalem için "bize dokunur mu?" → dokunanları `/privacy-legal:reg-gap-analysis`'e yönlendir → tarihi güncelle.

```
/privacy-legal:policy-monitor
/privacy-legal:policy-monitor "Davranışsal veriyi karşılama e-postalarını kişiselleştirmek için kullanacağız"
/privacy-legal:policy-monitor --mevzuat
```

---

# Aydınlatma ve Gelişme İzleyici

## Amaç

Metin uygulamanın gerisinde kalır: bir PIA yeni bir veri kategorisini onaylar, aydınlatmada geçmeyen bir alt işleyenle sözleşme imzalanır, bir triyaj sonucu metinde olmayan bir bildirim koşulu koyar. Aydınlatma yükümlülüğü yerine getirilirken eksik, yanıltıcı ve yanlış bilgiye yer verilmez ve işleme amacı değişirse işlemeden önce ayrıca aydınlatma yapılır (Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ m. 5/1-b, j). Bu skill kaymayı sorun olmadan yakalar; dışarıdaki değişikliği de `reg-gap-analysis`'e taşır. Çıktı hep aynıdır: açık burada, önerilen metin bu.

## Mevcut durumu yükle

`~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`:
- `## Regulatory footprint` — kapsamdaki rejimler (KVKK, sektör satırları, GDPR/UK)
- `## Privacy policy commitments` — aydınlatma metinlerinden çıkarılan taahhütler
- `## Outputs` — çıktı klasörü, metin yerleri, `Last policy sweep`, `Last regulatory scan`

`## Outputs` `[PLACEHOLDER]` içeriyorsa: "Çıktı klasörü ayarlanmamış. Yine de doğrudan sorgu yapabilirim — ne planladığınızı anlatın. Taramayı açmak için `/privacy-legal:cold-start-interview` ile klasör yolunu verin."

Asıl metni `## Outputs` → **Privacy policy document** yolundan oku. Profildeki özet yalnız özettir; öneri yazmak için asıl metin esastır.

### Taahhütler birden çok yüzeydedir — hepsini tara

Profile her yüzeyin yerini ve son güncelleme tarihini yaz; tarama her birini güncel metinle karşılaştırır ve ayrışmayı bildirir ("Aydınlatma [tarih]te güncellendi; mobil uygulama etiketi [daha eski tarih] — yeni veri kategorisini yansıtmıyor olabilir").

1. **Aydınlatma metinleri** — web, mobil uygulama, çalışan, aday, ziyaretçi/kamera, tedarikçi. Sözlü, yazılı, ses kaydı, çağrı merkezi gibi ortamlarda yapılan aydınlatmalar da aynı usule tabidir (Tebliğ m. 5/1); çağrı merkezi metni de taranır.
2. **Açık rıza metinleri ve onay akışları** — açık rızaya dayanan faaliyette aydınlatma ve açık rıza ayrı ayrı yapılır (Tebliğ m. 5/1-f). Rıza ekranındaki amaç ile aydınlatmadaki amaç aynı mı?
3. **VERBİS kaydı** — kayıt yükümlüsüyse aydınlatmada verilen bilgiler Sicile açıklananlarla uyumlu olmalı (Tebliğ m. 5/1-ç); Sicildeki bilgilerdeki değişiklik yedi gün içinde bildirilir (Veri Sorumluları Sicili Hakkında Yönetmelik m. 13). Yeni amaç, kategori, alıcı grubu ya da yabancı ülkeye aktarım = VERBİS güncellemesi de gerekebilir.
4. **Çerez paneli** — paneldeki çerez kategorileri ve amaçları aydınlatma ile çerez politikasındakiyle aynı mı? Kurumun çerez uygulamalarına ilişkin rehberine dayanacaksan güncel sürümünü Kurumun sitesinden teyit et; UYARI: veri çekilemedi, teyidiniz gerekli: https://www.kvkk.gov.tr/
5. **Uygulama mağazası gizlilik etiketleri** (Apple, Google) — kendi beyanınızdır; aydınlatmadaki kategori, amaç ve paylaşımla uyumlu mu, en son ne zaman güncellendi?
6. **Ticari elektronik ileti onayları** — ticari elektronik ileti önceden onayla gönderilir; esnaf ve tacirlere onaysız gönderilebilir (6563 s. Kanun m. 6). Yeni pazarlama kanalı = onay metni ve aydınlatma birlikte kontrol.

### Sektör bildirimleri de kapsamdadır

`## Regulatory footprint`'te sektör satırı varsa tarama o kurala göre de bakar; bildirim/metin ayarlanmamışsa her taramada **kalıcı açık** olarak göster, tek seferlik bulgu değil:

| Sektör | Neye bakılır | Ne işaretlenir |
|---|---|---|
| **Bankacılık** | Müşteri sırrı paylaşımları | Yeni bir üçüncü kişiye paylaşımı ima eden çıktı: müşteri sırrı, maddedeki istisnalar dışında, açık rıza alınsa dahi müşteri talebi ya da talimatı olmaksızın paylaşılamaz (5411 s. Kanun m. 73/3). Aydınlatmada "açık rızanızla paylaşırız" demek yetmez. |
| **Elektronik haberleşme (işletmeci)** | Abone rıza kayıtları, trafik/konum verisi | Terminal cihazda bilgi saklama/erişim için açık ve kapsamlı bilgilendirme ve açık rıza; trafik ve konum verisinin yurt dışına aktarımı için açık rıza; rıza kayıtları asgari abonelik süresince saklanır (5809 s. Kanun m. 51/3, 51/6, 51/10-c). |
| **Sağlık** | Hasta aydınlatması, özel nitelikli veri | Kişisel Sağlık Verileri Hakkında Yönetmelik (RG 21.06.2019/30808) — madde atfı gerekirse `tr_mevzuat_madde_getir(mevzuat_id="105551", madde_no=...)`; çekilemezse UYARI satırı. Özel nitelikli veride Kurulun belirlediği yeterli önlemler de şarttır (KVKK m. 6/4). |

**Kapsam belirsizse sor.** Profilde sektör satırı yok ama çıktılarda sağlık, finans ya da abone/trafik verisi görünüyorsa önce sor: "Profilinizde [sektör] yok ama bu tarama [kategori] içeren çıktılara bakıyor. Haritaya ekleyelim mi, karşılaştıracağımız ayrı bir metin var mı?" Bildirimi bulamıyorsan sessizce yalnız web aydınlatmasına bakma; açığı yüksek sesle söyle.

---

## Mod 1: Tarama

### Kapsam

`Last policy sweep` tarihinden sonraki çıktı dosyalarını tara. Tarih yoksa hepsini tara ve not düş: "İlk tarama — tüm çıktılar." Yeni dosya yoksa: "[tarih]ten bu yana yeni çıktı yok. Metin yakın uygulamayla güncel görünüyor." Tarama bitince `Last policy sweep`'i bugünün tarihiyle güncelle.

### Her çıktıda ne okunur

- **PIA:** veri kategorileri, amaçlar, hukuki sebepler (KVKK m. 5 ya da m. 6), alıcılar/alt işleyenler, yurt dışı aktarım, saklama süreleri, haklara etkisi, konulan koşullar → metinde olmayanı işaretle.
- **Sözleşme incelemeleri (imzalanmış/onaylanmış):** eklenen alt işleyenler, kabul edilen veri yerleri ve aktarım yolu (yeterlilik, standart sözleşme, bağlayıcı şirket kuralları, taahhütname, arızi istisna — KVKK m. 9), kapsanan amaçlar → aydınlatmada alıcı grubu ve aktarım amacı belirtilmiş mi (KVKK m. 10/1-c; Tebliğ m. 5/1-ı), VERBİS'te yabancı ülkelere aktarım bilgisi güncel mi (Veri Sorumluları Sicili Hakkında Yönetmelik m. 9/1-d), standart sözleşme bildirildi mi (KVKK m. 9/5)?
- **Triyaj sonuçları (PIA GEREKLİ / DEVAM):** onaylanan uygulama ve kamuya dönük taahhüt ima eden koşullar ("lansmandan önce ilgili kişiler aydınlatılmalı") → metinde karşılığı yoksa işaretle.
- **Başvuru cevapları:** önceki cevaplarda olmayan yeni veri kategorileri, sistem listesine eklenen sistemler → aydınlatmada geçmeyen kategori.

### Açık sınıflandırması

**ZORUNLU** — metin bu çıktıyla çelişiyor ya da işleme sürüyor ve metinde hiç karşılığı yok. Güncellenmezse eksik veya yanıltıcı aydınlatma olur (Tebliğ m. 5/1-j); aydınlatma yükümlülüğünü yerine getirmemek idari para cezası gerektirir (KVKK m. 18/1-a — kanun metnindeki aralık; güncel tutarı teyit et, dönemsel güncellenir).
> Örnek: Metin "ad, e-posta ve ödeme bilgisi topluyoruz" diyor; bir PIA konum verisini onayladı. Konum hiç geçmiyor → ZORUNLU.

**TAVSİYE** — metin sessiz ama çelişmiyor; savunulabilir, güncellenirse daha temiz.
> Örnek: Metin "hizmet aldığımız tedarikçilere aktarabiliriz" diyor; yeni bir analitik tedarikçisiyle sözleşme imzalandı, alıcı grubu kapsanıyor → isim listesi tutuluyorsa ekle.

**Tartışmalı — içtihadı ve Kurul kararlarını kontrol et:** alıcı grubunun ne kadar genel yazılabileceği; yurt dışındaki bulut sağlayıcısının barındırmasının "aktarım" sayılıp aydınlatmada ayrıca belirtilmesi gereği. `tr_semantik_ara(kurum="kvkk", query="aydınlatma metni alıcı grupları genel ifade")` ile ara; dönen karar özetinin `citation` alanını birebir kullan.

### Tarama çıktısı

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

# Aydınlatma İzleyici — Tarama Raporu
**Tarih:** [tarih] · **Taranan çıktı:** [N] · **Son taramadan beri yeni:** [N]
**Açık:** [N] ZORUNLU | [N] TAVSİYE
**Yüzey uyumu:** aydınlatma [tarih] · açık rıza [tarih] · VERBİS [tarih] · çerez paneli [tarih] · mağaza etiketi [tarih]
**Sektör bildirimleri:** [sektör]: [yol + tarih / AYARLANMADI — çözülene dek her taramada işaretlenir]

## ZORUNLU güncellemeler
### [Açık 1 kısa adı]
**Kaynak:** [dosya / çıktı türü]
**Ne oluyor:** [yeni uygulamanın sade tarifi]
**Mevcut metin:** [ilgili bölümden alıntı — ya da "Karşılığı yok"]
**Açık:** [eksik ya da tutarsız olan]
**Etkilenen diğer yüzeyler:** [VERBİS / açık rıza / çerez paneli / mağaza etiketi]
**Önerilen metin:**
> *[bölüm adı]na ekle:* "[metnin üslubuna uygun, somut taslak]"

## TAVSİYE güncellemeler
[aynı biçim, kısaltılmış]

## İşlem gerekmeyen
[açık bulunmayan taranmış çıktılar — incelendiklerini teyit eder]

## Sonraki adımlar
- [ ] ZORUNLU'lar: ilgili özellik/işleme canlıya çıkmadan önce (zaten canlıysa hemen) karar
- [ ] TAVSİYE'ler: sonraki metin yenilemesinde
- [ ] Dış gelişme taraması: `/privacy-legal:policy-monitor --mevzuat` (son: [tarih])
```

---

## Mod 2: Doğrudan sorgu

Tariften çıkar: hangi veri, hangi amaç, hangi hukuki sebep, kimler dahil (tedarikçi, ortak, yurt dışı alıcı), ilgili kişi kim (çalışan, müşteri, çocuk), otomatik karar var mı (ilgili kişinin münhasıran otomatik analizle aleyhe sonuca itiraz hakkı: KVKK m. 11/1-g), yeni bildirim gerekiyor mu. Tarif belirsizse **tek** netleştirici soru sor; uzun ön görüşme yapma.

| Kontrol | Metin ne diyor | Önerilen uygulama | Sonuç |
|---|---|---|---|
| Veri kategorileri | | | 🟢 Kapsanıyor / 🟡 Açık / 🔴 Çelişki |
| Amaçlar | | | |
| Hukuki sebep (m. 5 / m. 6) | | | |
| Alıcı grupları ve aktarım amacı | | | |
| Yurt dışı aktarım ve yolu (m. 9) | | | |
| Saklama süresi (imha politikası) | | | |
| Haklar (m. 11) | | | |
| Açık rıza gerekiyor mu, ayrı alınıyor mu | | | |
| VERBİS etkisi | | | |

Çıktı: **Sonuç** (GÜNCELLEME ZORUNLU / TAVSİYE / GEREKMEZ) → kapsananlar (kısa) → eksikler (mevcut metin, neden önemli, önerilen metin, hangi bölüme) → çelişkiler (hangisi değişmeli ve neden; çoğu zaman uygulama metne uyar ya da metin savunulabilir yeni bir duruşa güncellenir) → **Zamanlama:** ZORUNLU varsa "amaç değiştiği için işlemeden önce ayrıca aydınlatma gerekir (Tebliğ m. 5/1-b)"; yalnız TAVSİYE ise "devam edilebilir, sonraki yenilemede güncelleyin".

---

## Mod 3: Dış gelişme taraması

Pencere: `Last regulatory scan` → bugün (ilk taramada son 90 gün). `tr_` çağrılarını sırayla yap, aralarında birkaç saniye bırak (hız sınırı ortaktır). Araç veri getiremezse (hata, `unavailable`, `upstream_blocked`) boş sonuç sayma; o kalem için UYARI satırını aracın `source_url`'si ya da resmî giriş sayfasıyla yaz.

1. **Kurul karar özetleri** (canlı liste son sayfaları tarar; sıra tarihe göre değildir, `date` ve `decision_no` alanına bak):
   `tr_kurum_karari_ara(kurum="kvkk", params={"scan_pages": 3}, limit=30)`
   Konu bazlı: `tr_kurum_karari_ara(kurum="kvkk", query="çerez", params={"scan_pages": 5})`. Arşiv ve tarih aralığı için: `tr_semantik_ara(kurum="kvkk", query="yurt dışına aktarım standart sözleşme", date_from="YYYY-AA-GG")`. Metni oku: `tr_kurum_karari_getir(kurum="kvkk", id="<id>")`.
2. **Resmî Gazete** (Kurul düzenleyici kararları, yeterlilik kararları — yeterlilik kararı Resmî Gazete'de yayımlanır: KVKK m. 9/2 — ve yeni yönetmelikler). Tek çağrı en çok 60 gün; uzun pencereyi böl:
   `tr_resmi_gazete_tara(date_from="YYYY-AA-GG", date_to="YYYY-AA-GG", query="Kişisel Veri")`
   Tek gün: `tr_resmi_gazete_fihrist(date="YYYY-AA-GG", query="Kişisel Veri")`.
3. **İkincil mevzuat** (KVKK yönetmelikleri `KKY`, tebliğler `TEBLIGLER` türündedir):
   `tr_mevzuat_ara(query="Kişisel Veri", types=["KKY", "TEBLIGLER"], rg_date_from="YYYY-AA-GG")`
   Uyarı: RG tarihi boş kayıtlar tarih süzgecine girmez; boş sonuç "değişiklik yok" demek değildir. İzlenen metinlerin değişiklik tablosunu ayrıca kontrol et: `tr_mevzuat_getir(mevzuat_id="108729")` (Aydınlatma Tebliği), `"106248"` (Silme Yönetmeliği), `"106135"` (Sicil Yönetmeliği), `"328537"` (Yurt Dışına Aktarım Yönetmeliği), `"108728"` (Başvuru Tebliği) — metin sonundaki "Değişiklik Yapan" listesinde yeni tarih var mı?
4. **Kanun değişikliği:** `tr_mevzuat_madde_getir(number="6698", madde_no=["6", "9", "10", "12", "16", "18"])` → `annotations` alanındaki "(Değişik: …)" / "(Ek: …)" notlarını önceki taramanın listesiyle karşılaştır.
5. **Sektör** (yalnız haritadaysa): `tr_kurum_karari_ara(kurum="bddk", query="bilgi sistemleri")`; `tr_kurum_karari_ara(kurum="btk", query="kişisel veri", date_from="YYYY-AA-GG")`.
6. **Yabancı rejim** (yalnız haritadaysa): AB — `eu_search_eu_law(query="data protection", date_from="YYYY-AA-GG")` ve `eu_search_eu_law(query="adequate protection of personal data", date_from="YYYY-AA-GG")`; Birleşik Krallık — `uk_search_legislation(title="Data", year="YYYY")`, değişiklik için `uk_get_effects`.

**Kalem başına tek satır:** `[tarih] · [künye — araçtan birebir] · [konu] · Bize dokunur mu: Evet/Hayır/Belirsiz — [gerekçe] · Sonraki adım`. "Evet/Belirsiz" olanlara: `/privacy-legal:reg-gap-analysis "[künye]"`. Bitince `Last regulatory scan`'i güncelle. Kurul karar numarasını asla ezberden yazma; yalnız araçtan dönen `citation`.

---

## Önerilen metnin kalitesi

- Asıl metnin sesine ve üslubuna uy (profil özetini değil, asıl belgeyi oku).
- Amaç belirli, açık ve meşru olsun; genel ve muğlak ifade ya da "ileride başka amaçlar için de işlenebilir" izlenimi veren ifade kullanma; dil anlaşılır, açık ve sade olsun (Tebliğ m. 5/1-g, ğ).
- Hukuki sebebi açıkça yaz — KVKK m. 5 ve 6'daki hangi şarta dayanıldığı (Tebliğ m. 5/1-h).
- Ekibin tutamayacağı taahhüt yazma ("konum verisini asla paylaşmayız" yazma, mimari analitik tedarikçisine akıtıyorsa).
- Tek cümle eklemek yetmiyor, duruş değişikliği gerekiyorsa söyle. Hangi bölüme ekleneceğini hep belirt; bölüm yoksa açılmasını öner.

## Zamanlama

Eklenti kendini zamanlamaz. Kullanıcıya önce: "Takviminize ya da görev yöneticinize haftalık `/privacy-legal:policy-monitor` ve aylık `--mevzuat` hatırlatıcısı koyun." Her çalışma `Last policy sweep` / `Last regulatory scan` tarihini günceller; sonraki çalışma yalnız yenilere bakar.

## Kapanış

Profildeki `## Outputs` karar ağacıyla bitir; seçenekleri bu çıktıya uyarla (metni yaz, eskale et, olgu topla, izle ve bekle, başka bir şey). Ağaç çıktıdır; seçimi avukat yapar. On'dan fazla bulgu varsa ya da istenirse yüzeye ve önem derecesine göre sayımlı, sıralanabilir bir tablo öner.

## Bu skill ne yapmaz

- Metni kendisi değiştirmez; önerir, her değişikliği insan onaylar.
- Dış değişikliğin açık analizini yapmaz — `--mevzuat` yalnız tespit eder ve `reg-gap-analysis`'e yönlendirir.
- Çıktıların kaydedilmesini zorlamaz; klasöre kaydedilmeyen PIA'yı bulamaz (doğrudan sorgu yine çalışır).
- E-posta ya da Slack'teki gayriresmî kararları okumaz; yalnız klasördeki yapılandırılmış çıktıları okur.

---

## /privacy-legal:reg-gap-analysis

---
name: reg-gap-analysis
description: >
  Yeni ya da değişen bir düzenlemeyi (KVKK değişikliği, yönetmelik, tebliğ, Kurul
  kararı, sektör kuralı ya da yabancı rejim) mevcut aydınlatma metinleri ve
  uygulamayla karşılaştırır; açık listesi ve sorumlu ile tarih içeren düzeltme
  planı üretir. Yeni bir düzenleme çıktığında, "[düzenleme] bizi etkiliyor mu",
  "[yönetmelik] için açık analizi", "KVKK uyum kontrolü" denince ya da düzenleme
  metni yapıştırıldığında kullan.
argument-hint: "[düzenleme adı ya da künyesi, veya metni yapıştırın]"
---

# /reg-gap-analysis

1. Profili yükle: aydınlatma taahhütleri, yükümlülük haritası, başvuru sistemleri.
2. Kapsam: düzenleme bize uygulanır mı (kişi, sektör, eşik, istisna, yürürlük)?
3. Gereklilikleri araçla çek → mevcut durumla karşılaştır → açık listesi.
4. Önceliklendir; sorumlu ve tarihli düzeltme planı yaz.
5. Tarihli belge olarak kaydet. "Açık yok" sonucu da belgelenir.

```
/privacy-legal:reg-gap-analysis "Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik"
/privacy-legal:reg-gap-analysis
[Kurul kararı ya da düzenleme metni]
```

---

# Düzenleme–Uygulama Açık Analizi

## Amaç

Bir şey değişir — kanun değişikliği, yeni yönetmelik, Kurulun ilan ettiği standart sözleşme ya da yeni bir karar özeti — ve neyi değiştirmeniz gerektiğini bilmeniz gerekir. Bu skill yeni gerekliliği mevcut uygulamayla (profil → `## Privacy policy commitments`, `## Regulatory footprint`, `## DSAR process` ve PIA'larda belgelenen uygulamalar) karşılaştırır, açık listesi ve düzeltme planı üretir. `/policy-monitor --mevzuat` tespit eder; analiz burada yapılır.

## Mevcut durumu yükle

`~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`: aydınlatma taahhütleri, yükümlülük haritası (VERBİS, aktarım yolları, sektör, yabancı rejim), başvuru sistemleri listesi. Düzenleme size uygulanmıyorsa analiz tek satırdır: "Uygulanmaz. Nedeni: [gerekçe]. İşlem gerekmez." — yine kaydet.

## Adım 1 — Kapsam

- **Uygulanır mı?** Kişi (veri sorumlusu / veri işleyen — 7499 sonrası yurt dışı aktarım ve standart sözleşme bildirimi veri işleyeni de doğrudan bağlar: KVKK m. 9/1, 9/5, 18/1-d ve 18/2), sektör, eşik, istisna. Kanunun hiç uygulanmadığı hâller ile aydınlatma (m. 10), haklar (m. 11, tazminat hariç) ve VERBİS (m. 16) hükümlerinin uygulanmadığı hâller ayrıdır (KVKK m. 28/1, 28/2) — hangisine girdiğini ayrı yaz. VERBİS istisnası Kurul kararıyla belirlenir ve diğer yükümlülükleri kaldırmaz (KVKK m. 16/2; Veri Sorumluları Sicili Hakkında Yönetmelik m. 5/1-f, 16).
- **Ne zaman?** Yürürlük tarihi, geçiş hükmü. Örnek: 7499 s. Kanunla değişen m. 9 yürürlüğe girdi; eski m. 9/1 değişik hâliyle birlikte 1/9/2024'e kadar uygulanmaya devam etti; 1/6/2024 itibarıyla sulh ceza hâkimliklerinde görülen başvurular orada görülmeye devam eder (KVKK geçici m. 3). Yürürlük maddesini metinden çek (ör. Yurt Dışına Aktarım Yönetmeliği m. 18: yayımı tarihinde).
- **Gerçekten yeni olan ne?** Tüm metni değil, zaten uyduğunuz şeyden farkı (delta) çıkar. GDPR'a uyuyor olmak KVKK'ya uyduğunuz anlamına gelmez; farkı her kalemde ayrıca kontrol et.

## Adım 2 — Gereklilikleri çıkar (araçla)

Metni ezberden özetleme; çek:
- Bul: `tr_mevzuat_ara(query="<başlıktan kelimeler>", types=["KKY", "TEBLIGLER"])` (KVKK yönetmelikleri `KKY`, tebliğler `TEBLIGLER` türündedir; kanun için `types=["KANUN"]`).
- Oku: `tr_mevzuat_madde_getir(mevzuat_id="<id>", madde_no=["5", "6", ...])` (en çok 10). Madde ağacı yoksa (`tr_mevzuat_icindekiler` hata verebilir) tam metin: `tr_mevzuat_getir(mevzuat_id="<id>")`.
- Kurul kararı / ilan: `tr_semantik_ara(kurum="kvkk", query="<konu>")`, `tr_kurum_karari_ara(kurum="kvkk", query="<konu>", params={"scan_pages": 5})`, `tr_kurum_karari_getir(kurum="kvkk", id="<id>")`; Resmî Gazete'de yayımlananlar için `tr_resmi_gazete_tara(date_from, date_to, query="Kişisel Veri")`.
- Sektör: `tr_kurum_karari_ara(kurum="bddk" | "btk", query=...)`, ilgili kanun maddesi `tr_mevzuat_madde_getir`.

| # | Gereklilik | Atıf (araçtan dönen `citation`) | Kategori |
|---|---|---|---|

**Kategoriler:** Aydınlatma · Haklar ve başvuru · Güvenlik ve ihlal · Veri işleyen ve aktarım · Rıza · Kayıt ve yönetişim (VERBİS, envanter) · Saklama ve imha.

### Çapa kontrol listesi (doğrulanmış; karşılaştırmanın tabanı)

| Alan | Doğrulanmış kural |
|---|---|
| İlkeler | Hukuka ve dürüstlüğe uygunluk, doğruluk, belirli/açık/meşru amaç, amaçla bağlantılı-sınırlı-ölçülü olma, gerekli süre kadar muhafaza (KVKK m. 4/2). |
| Hukuki sebep | Kural açık rıza; m. 5/2'deki şartlardan biri varsa aranmaz (m. 5). Özel nitelikli veri yasak; m. 6/3 hâllerinde ve Kurulun yeterli önlemleriyle (m. 6/3-4). |
| Aydınlatma | Asgari içerik (m. 10; Aydınlatma Tebliği m. 4); her işlemede, amaç değişince önceden ayrıca; talebe bağlı değil; ispat veri sorumlusunda; açık rızadan ayrı; hukuki sebep ve alıcı grupları açıkça; anlaşılır ve sade dil (Tebliğ m. 5/1). Veri ilgili kişiden alınmadıysa makul süre / ilk iletişim / en geç ilk aktarım (Tebliğ m. 6). |
| Haklar ve başvuru | m. 11 hakları; en geç otuz gün, kural olarak ücretsiz (m. 13/2); Türkçe başvuru, kanallar, cevabın asgari içeriği, ücret (Başvuru Tebliği m. 4-7); şikâyet süreleri (m. 14). |
| Güvenlik ve ihlal | Teknik ve idari tedbir; veri işleyenle müşterek sorumluluk; iç denetim; ihlalde en kısa sürede ilgilisine ve Kurula bildirim (m. 12). |
| Aktarım | Genel kural: açık rıza ya da m. 5/2 şartları; özel nitelikli veride yeterli önlemlerle m. 6/3 şartları (m. 8). Yurt dışı: yeterlilik kararı → uygun güvence → arızi istisna; standart sözleşme beş iş günü içinde bildirim; sonraki aktarımlarda da aynı güvenceler (m. 9). Usul: Yurt Dışına Aktarım Yönetmeliği m. 5-7, 14 (standart sözleşme değiştirilmeden kullanılır, bildirim usulü), 15 (taahhütnamede Kurul izni), 16 (arızi: düzenli olmayan, tek veya birkaç sefer, süreklilik arz etmeyen). |
| Kayıt ve yönetişim | Veri işlemeye başlamadan önce VERBİS kaydı; Kurul istisnası (m. 16); envanter, irtibat kişisi, değişiklikte yedi gün (Sicil Yönetmeliği m. 5, 11, 13). |
| Saklama ve imha | Sebep ortadan kalkınca silme/yok etme/anonimleştirme (m. 7); kayıt yükümlüsü için saklama ve imha politikası (Silme Yönetmeliği m. 5-6); işlem kayıtları en az üç yıl (m. 7/3); periyodik imha en fazla altı ay, politikası olmayan için üç ay (m. 11); talep hâlinde otuz gün (m. 12). |
| Yaptırım | İdari para cezaları: aydınlatma, veri güvenliği, Kurul kararına uymama, VERBİS, standart sözleşme bildirimi (KVKK m. 18/1 a-d — kanun metnindeki aralıklar; güncel tutarı teyit et, dönemsel güncellenir); cezaya karşı idare mahkemesi (m. 18/3). Suçlar için TCK 135-140; silmeyen/anonimleştirmeyen TCK 138'e göre (KVKK m. 17). |
| Sektör | Bankacılık müşteri sırrı (5411 m. 73/3); elektronik haberleşme (5809 m. 51); sağlık (Kişisel Sağlık Verileri Hakkında Yönetmelik — madde atfı için önce çek). |

## Adım 3 — Mevcut durumla karşılaştır

```markdown
### Gereklilik #N: [kısa ad]
**Düzenleme diyor ki:** [alıntı ya da yakın özet + atıf]
**Bizde şu an:** [profil / aydınlatma metni / uygulama ne gösteriyor]
**Açık:** [Yok | Kısmi | Tam]
**Eksik olan (kısmi/tam ise):** [somut]
**Kapatma eforu:** [Yalnız metin | Ürün değişikliği | Sözleşme yeniden müzakeresi | Yeni süreç | Kuruma bildirim/başvuru]
**Uyumsuzluk riski:** [yaptırım türü ve dayanağı; Kurulun yakın kararlarında görülen eğilim — araçtan; itibar]
```

## Adım 4 — Önceliklendir

1. **Dişli son tarih** — yürürlük + yaptırım + kısa süreli yükümlülük (ör. standart sözleşme bildirimi, VERBİS değişikliği).
2. **Efor/etki oranı** — metin güncellemesi ucuz, ürün yeniden yapımı pahalı.
3. **Yarısı yapılmış olan** — mevcut uyum (GDPR dahil) farkı küçültebilir, ama farkı kalem kalem göster.

## Adım 5 — Düzeltme planı

Profildeki `## Outputs` üst başlığını ekle (role göre değişir).

**Araştırma bağlantısı ön kontrolü.** Planı yazmadan önce bu oturumda ArthurLegal MCP'nin cevap verip vermediğini kontrol et. Vermediyse inceleyen notunun **Kaynaklar:** satırına yaz: "ArthurLegal MCP bağlı değil — atıflar model bilgisinden; önce yürürlük/geçiş tarihlerini, madde-fıkra-bent numaralarını ve Kurul kararı künyelerini kontrol edin." Satır içi etiketler kalır; çıktının üstüne ayrı afiş koyma.

```markdown
[ÜST BAŞLIK — ## Outputs]

## Düzeltme Planı: [düzenleme — künye]
**Yürürlük:** [tarih — maddeden] · **Geçiş hükmü:** [varsa]

### Yürürlükten / son tarihten önce yapılacaklar
| Açık | Çözüm | Sorumlu | Son tarih | Durum |
|---|---|---|---|---|

### Yapılması iyi olanlar (engelleyici değil)
[aynı tablo]

### Zaten uyumlu
[açık = Yok olan gereklilikler]

### Kabul edilen açıklar (risk kabul edildi)
[gerekçe ve riski kabul eden kişi]

> ⚠️ **İnceleyen notu** — Kaynaklar: [araçlar / bağlı değil]. Tartışmalı noktalar: [liste]. Avukat incelemesi olmadan dışa gönderilmez.
```

## Kaynak etiketleri ve sessiz tamamlama yasağı

Her atfı kaynağıyla etiketle; etiketleri silme ya da birleştirme:
- `[ArthurLegal TR — <citation> — GG.AA.YYYY]` — `tr_` aracından birebir.
- `[eu_ — CELEX <no>]`, `[uk_ — <citation>]` — yabancı rejim araçlarından.
- `[kullanıcı verdi]` — kullanıcının sağladığı metin.
- `[model bilgisi — doğrula]` — araçla doğrulanamayan; tarih, eşik, yürürlük, Kurul kararı.
- `[model bilgisi — doğrula-pinpoint]` — fıkra/bent numarası; en yüksek uydurma riski, her zaman birincil kaynakla kontrol.
- `[web — doğrula]` — yalnız kullanıcı izin verdiyse.

**Sessiz tamamlama yok.** Araç bir düzenleme ya da karar için az veya hiç sonuç döndürürse bulduğunu söyle ve dur: "[araç] [N] sonuç döndürdü; [konu] için kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç (`tr_semantik_ara`, `tr_resmi_gazete_tara`), (3) web araması — sonuçlar `[web — doğrula]` etiketli, (4) doğrulanmadı diye işaretle ve dur. Hangisi?" Çekilemeyen maddeye: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`; Kurul kararına aracın `source_url`'si ya da https://www.kvkk.gov.tr/Icerik/5406/kurul-karar-ozetleri. Kurul karar numarasını ve yabancı madde numarasını ezberden yazma.

## Yabancı rejimle karşılaştırma

Yalnız haritada varsa ve araçla:
- **GDPR:** `eu_search_eu_law(query="General Data Protection Regulation")` → CELEX 32016R0679; metin `eu_get_document_text(celex="32016R0679", offset=..., max_chars=...)` (~350.000 karakter; `next_offset` ile ilerle). Madde numarasını dönen metinden al.
- **Birleşik Krallık:** `uk_search_legislation(title="Data Protection", year="2018", type="ukpga")`, `uk_get_section(year="2018", number="12", section="...")`; alıntıdan önce `uk_get_effects` ile güncelliği kontrol et.
- **ABD (karşılaştırmalı not):** eyalet gizlilik yasaları için ArthurLegal'da mevzuat kaynağı yok; yerel hukukçu görüşü al. Yalnız yapı benzetmesi yapılabilir (ör. "çoğu yeni eyalet yasası tek bir temel modelin varyantıdır; farkı çıkar") — kural olarak atıf yapma.

## Tartışmalı — içtihadı ve Kurul kararlarını kontrol et

- Meşru menfaat dengesi (m. 5/2-f) ve "sözleşmenin ifası için gerekli" (m. 5/2-c) ile açık rıza arasındaki sınır.
- 7499 sonrası özel nitelikli verinin m. 6/3 hâllerine (ör. istihdam, sağlık) dayanılarak işlenmesinin kapsamı.
- Yurt dışındaki bulut barındırmasının aktarım sayılması ve "arızi" aktarımın sınırı (Yönetmelik m. 16/1 tanımına rağmen uygulama).
- Aydınlatmada alıcı gruplarının ne kadar genel yazılabileceği.
- İdari para cezasına karşı dava açma süresi (`/privacy-legal:matter-workspace` kritik süreler notu).

Her biri için sorgu: `tr_semantik_ara(kurum="kvkk", query="<konu>")`, `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="<konu>")`; dönen künyeyi birebir kullan, "yerleşik uygulama" diyorsan karar numarası verme. Düzenleme belirsizse söyle: "[hüküm] [A] ya da [B] okunabilir; [A] temkinli okuma. Önemliyse dış avukat görüşü önerilir."

## Diğer skill'lerle bağlantı

- **`/pia-generation`:** PIA'ların bulduğu metin tutarsızlıkları buraya bilinen açık olarak gelir.
- **`/policy-monitor --mevzuat`:** dış gelişmeyi tespit eder ve buraya yönlendirir.
- **regulatory-legal eklentisi (kuruluysa):** kaynakları izler; bu skill elle tetiklenen sürümdür.

## Çıktı

Tarihli markdown belge olarak kaydet; plan tablosu takipçidir, kalemler kapandıkça durumu güncelle. "Açık yok, uyumluyuz" sonucu da yazılır — sonradan baktığınızın kanıtıdır.

**Atıf doğrulama notuyla bitir:** "Bu çıktıdaki atıflar bir yapay zekâ modeliyle hazırlandı; `tr_` etiketli olanlar araçla çekildi, diğerleri birincil kaynakla doğrulanmadı. Bir düzenlemeye, karara ya da yaptırıma dayanmadan önce resmî kaynakla (mevzuat.gov.tr, resmigazete.gov.tr, kvkk.gov.tr) doğruluğunu ve güncelliğini kontrol edin; `doğrula` etiketlileri önce kontrol edin."

Profildeki `## Outputs` karar ağacıyla kapat; seçenekleri bu çıktıya uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Belirsiz düzenleyici dili bağlayıcı biçimde yorumlamaz; okuma seçeneklerini gösterir.
- Değişiklikleri kendiliğinden izlemez — işaret edildiğinde çalışır (`/policy-monitor --mevzuat` ya da regulatory-legal).
- Düzeltmeleri uygulamaz; planlar.

---

## /privacy-legal:use-case-triage

---
name: use-case-triage
description: >
  Bir veri işleme faaliyetinin hızlı ön elemesi — KVKK tabanında (m. 4 genel
  ilkeler, m. 5–6 işleme şartları, m. 10 aydınlatma, m. 16 VERBİS, m. 8–9
  aktarım) faaliyetin devam edebileceğine, PIA gerektiğine, AB'ye dönükse GDPR
  etki değerlendirmesinin zorunlu olduğuna ya da durması gerektiğine karar
  verir; aydınlatma metni ve gizlilik politikasıyla çelişkiyi yakalar, doğru
  sonraki adıma yönlendirir. "PIA gerekir mi", "bu özelliği triage et", "KVKK
  açısından sorun var mı", "gizlilik kontrolü" denince ya da yeni bir veri
  işleme faaliyeti, ürün özelliği veya tedarikçi ilişkisi anlatıldığında kullan.
argument-hint: "[veri işleme faaliyetini ya da özelliği anlatın]"
---

# /use-case-triage — Veri İşleme Ön Elemesi

PIA'dan önce gelen soruyu cevaplar: "Buna değerlendirme gerekir mi; gerekirse hangisi ve önünde ne var?" Triage PIA'dan hızlıdır ve onun yukarısındadır: değerlendirmeyi yazmaz, gerekip gerekmediğini ve hangi şartla ilerleneceğini belirler. Derin iş `/privacy-legal:pia-generation`'ındır.

Dört sonuç:
- **DEVAM (PROCEED)** — PIA gerekmez; standart güvenceler yeter.
- **PIA GEREKLİ (PIA REQUIRED)** — devreye almadan önce ya da birlikte değerlendirme.
- **VKED ZORUNLU (DPIA MANDATORY)** — yalnız zorunlu etki değerlendirmesi öngören bir rejim (GDPR Art. 35, UK GDPR) uygulanıyor ve tetiği oluşmuşsa. KVKK tek başına bu sınıfı doğurmaz; 6698'de genel bir etki değerlendirmesi yükümlülüğü yoktur.
- **DUR (STOP)** — hukuki sebep yok, genel ilkeye aykırı, aktarım yolu yok ya da aydınlatma metni/gizlilik politikasıyla doğrudan çelişki; yeniden tasarım gerekir.

## Destination check

Çıktı nereye gidiyor? Kullanıcı bir hedef söylediyse (kanal, dağıtım listesi, karşı taraf, "herkes") sır çevresinin içinde mi diye sor. Hedef dışarıdaysa üç seçenek sun: (a) yalnız hukuk için başlıklı tam sürüm, (b) geniş dağıtım için arındırılmış sürüm, (c) ikisi. Başlık koyup metnin başlığın korumadığı yere yapıştırılmasına sessizce yardım etme.

## Önce ayarı oku

`company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## PIA house style` (tetikler), `## Regulatory footprint` (VERBİS durumu, yurt dışı aktarım yolları, sektör, yabancı rejim), `## Privacy policy commitments` (aydınlatma metinleri), `## Escalation`, `## Outputs`, `## Who's using this`. Bunlar belirleyicidir; genel hukuk akıl yürütmesi şirketin gerçekten taahhüt ettiğinin yerini tutmaz.

Dosya yoksa ya da `[PLACEHOLDER]` içeriyorsa:

> Pratik profiliniz henüz kurulmamış — PIA tetiklerini, yükümlülük haritasını ve aydınlatma taahhütlerini oradan alıyorum.
> **İki seçenek:**
> - `/privacy-legal:cold-start-interview` çalıştırın (birkaç dakika), sonra triage'ı size göre yapayım.
> - **"geçici"** deyin; genel varsayımlarla (Türkiye — KVKK, orta risk iştahı, avukat rolü, playbook yok) triage edeyim ve her çıktıyı `[GEÇİCİ — profilinizi kurun]` diye etiketleyeyim.

**Geçici mod:** triage'ı bu varsayımlarla normal yürüt; taahhütlerle eşleme yerine genel KVKK ilkelerinden sınıflandır. İnceleyen notunu ve her bulgu bloğunu `[GEÇİCİ]` diye etiketle. Sonuna ekle: "Bu, varsayılan kabullerle genel bir çalıştırmaydı. Yükümlülük haritanıza, aydınlatma taahhütlerinize ve risk iştahınıza göre çıktı için `/privacy-legal:cold-start-interview` çalıştırın."

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/privacy-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Faaliyeti anla

Açıklama belirsizse sınıflandırmadan önce sor:
- Hangi veri, hangi kategoriler? Özel nitelikli veri (m. 6/1) var mı?
- İlgili kişiler kim — müşteri, çalışan, aday, üçüncü kişi, çocuk?
- Amaç ne; hangi sorunu çözüyor?
- Yeni toplama mı, eldeki verinin yeni amaçla kullanımı mı?
- Tedarikçi var mı; yeni mi, mevcut mu? Sunucu nerede?
- Otomatik karar var mı; çıktı birini etkiliyor mu?
- Kullanım bağlamı: yalnız şirket içi mi, müşteriye dönük mü, herkese açık mı?

"Yeni özellik" ya da "veri işleme faaliyeti" doğru sınıflandırma için yetmez.

### 2. Ev tetikleri

`## PIA house style` → tetikleri uygula. Tetik oluştuysa en az **PIA GEREKLİ**. Oluşmadıysa DEVAM demeden önce 3–5'i bitir; bazı faaliyetler iç politika ne derse desin değerlendirme ister.

### 3. KVKK taban kontrolü

| Kontrol | Soru | Dayanak | Açık çıkarsa |
|---|---|---|---|
| Kapsam | Gerçek kişiye ilişkin veri mi; otomatik ya da veri kayıt sisteminin parçası olarak otomatik olmayan yolla mı işleniyor; m. 28/1 istisnası var mı? | m. 2; m. 3/1-d, e; m. 28/1 | Kapsam dışıysa DEVAM (gerekçeyi yaz) |
| Genel ilkeler | Hukuka ve dürüstlük kurallarına uygun; doğru ve gerektiğinde güncel; belirli, açık, meşru amaç; amaçla bağlantılı, sınırlı, ölçülü; gerekli süre kadar muhafaza | m. 4/2-a–d | Aykırılık → DUR ya da tasarım koşulu |
| Hukuki sebep | Her amaç için m. 5/2 şartı ya da açık rıza; özel nitelikli veride m. 6/3 hâli + Kurul'un yeterli önlemleri | m. 5; m. 6/3-4 | Sebep yok → DUR |
| Aydınlatma | Elde etme sırasında: veri sorumlusunun kimliği, amaç, alıcılar ve amacı, toplama yöntemi ve hukuki sebep, m. 11 hakları | m. 10/1-a–d | Eksik → koşul (metin güncellemesi lansmandan önce) |
| Aktarım | Yurt içi üçüncü kişi (m. 8); yurt dışı: yeterlilik → uygun güvence (standart sözleşme 5 iş günü bildirim) → yalnız arızi istisna | m. 8; m. 9/1, 4, 5, 6 | Yol yok → DUR |
| VERBİS | Kayıt yükümlüsü mü, Kurul istisnasında mı? Yeni amaç, kişi grubu, alıcı, yurt dışı aktarım ya da saklama süresi sicil bilgisini değiştiriyor mu? | m. 16/2-4; Veri Sorumluları Sicili Hakkında Yön. m. 13/1 (değişiklikten itibaren 7 gün) | Güncelleme → koşul |
| Veri işleyen | Tedarikçi adına mı işliyor? Sözleşme ve m. 12/2 müşterek sorumluluk | m. 12/1-2 | → `/privacy-legal:dpa-review` |
| Ticari ileti | Pazarlama iletisi varsa önceden onay ve ret hakkı | 6563 m. 6, m. 8 | Onay yok (m. 6/1 son cümle ve m. 6/2 esnaf-tacir istisnası dışında) → DUR |

VERBİS istisnası Kurul kararıyla getirilir (m. 16/2) → `tr_semantik_ara(kurum="kvkk", query="Veri Sorumluları Siciline kayıt yükümlülüğünden istisna")`; künyeyi araçtan al, ezberden yazma.

**Sektörel katman (önce sor):** banka müşteri verisi → 5411 m. 73/3 (müşteri sırrı; istisnalar dışında açık rıza alınsa dahi müşteriden talep ya da talimat olmaksızın üçüncü kişilerle paylaşılamaz; BDDK yurt dışı paylaşımı yasaklayabilir ve sistemlerin yurt içinde tutulmasına karar verebilir); sağlık → Kişisel Sağlık Verileri Hakkında Yönetmelik + m. 6/3-e; elektronik haberleşme → sektör yönetmeliği (`tr_mevzuat_ara(query="Elektronik Haberleşme Sektöründe Kişisel Verilerin", types=["KKY"])`); çocuk verisi → KVKK'da ayrı bir rejim yok; açık rızayı kimin vereceği (ayırt etme gücü, veli) **tartışmalı — Kurul kararlarını ara**. Sektör satırı yoksa yaz: "sektörel katman yok — kontrol edildi."

**Yaptırım bağlamı** (risk derecesi için; **tutar yazma**): m. 18/1 — aydınlatma yükümlülüğü (a), veri güvenliği (b), Kurul kararlarına uymama (c), VERBİS kayıt ve bildirim (ç), standart sözleşme bildirimi (d; 7499 s.K. ile eklendi) idari para cezası öngörür. Kanun metnindeki alt ve üst sınırlar her takvim yılı başında yeniden değerleme oranında artırılarak uygulanır (5326 m. 17/7) → güncel tutarı Kurum duyurusundan teyit et. Kurul'un idari para cezasına karşı idare mahkemesinde dava açılabilir (m. 18/3). Ceza hukuku: kişisel verilere ilişkin suçlarda TCK m. 135–140; m. 7'ye aykırı olarak silmeme TCK m. 138 (6698 m. 17).

### 4. Zorunlu değerlendirme kontrolü

- **KVKK:** zorunlu etki değerlendirmesi yok → bu adım KVKK için "uygulanmaz".
- **GDPR** `## Regulatory footprint`'te varsa: uygulama alanı için Art. 3'ü, tetikler için Art. 35'i `eu_get_document_text(celex="32016R0679")` ile çek (Art. 3 ≈ offset 156000, Art. 35 ≈ offset 224000). Art. 35(3)'teki hâllerden biri ya da ilgili üye devlet denetim makamının listesi (Art. 35(4)) tetikleniyorsa → **VKED ZORUNLU**. Üye devlet listesi için ilgili ülke aracı (`de_gesetz_ara`, `nl_search_legislation` …); bulunamazsa "ArthurLegal'da bu listenin kaynağı yok; yerel hukukçu görüşü al."
- **UK GDPR:** `uk_search_legislation(query="Data Protection Act 2018")` → `uk_get_section`.
- *Karşılaştırmalı not:* ABD eyalet yasalarının kendi risk değerlendirmesi tetikleri vardır; yalnız CourtListener kuruluysa `courtlistener-rehberi.md` üzerinden, ezberden değil.

**Güçlü göstergeler** (zorunlu olmasa da değerlendirme yap): yeni teknoloji ya da yapay zekâ; çocuk verisi; özel nitelikli veri; ayrı toplanmış veri setlerinin birleştirilmesi; ayrımcılığa elverişli veri ya da çıkarım; münhasıran otomatik analizle kişi aleyhine sonuç (m. 11/1-g); çalışan izleme; ilgili kişinin beklemeyeceği işleme; davranışsal reklam, benzer kitle (lookalike) ve bağlamlar arası takip (aktarım, aydınlatma ve 6563 onay sorunlarını düzenli olarak açığa çıkarır). Zorunlu tetik yok ama gösterge var → **PIA GEREKLİ** (çıktıda göstergeyi belirt).

### 5. Aydınlatma metni / gizlilik politikası çelişkisi

`## Privacy policy commitments`'taki her taahhüdü faaliyetle karşılaştır:
- Metin "X, Y, Z'yi topluyoruz" diyor; faaliyet W'yi topluyor → lansmandan önce metin güncellenir ya da W toplanmaz.
- Metin "üçüncü kişilerle paylaşmıyoruz" diyor; faaliyet veriyi tedarikçinin kendi amaçları için geçiriyor → aktarım şartı (m. 8) ve rol sorunu.
- Metin "yurt dışına aktarmıyoruz" diyor; faaliyet yurt dışı bulut kullanıyor → m. 9 yolu + metin.
- Metinde saklama süresi var; faaliyet daha uzun saklıyor (m. 4/2-d).
- Metin veriyi yalnız belirli amaçla kullanacağını söylüyor; faaliyet yeni amaç ekliyor → yeni hukuki sebep ve aydınlatma.
- Faaliyet, hak başvuru sürecinin kapsamadığı yeni bir veri kategorisi yaratıyor (m. 11, m. 13).

Doğrudan çelişki → **DUR**. "Dikkatle devam" değil: çelişki (metin güncellemesi ya da yeniden tasarım) çözülmeden ilerlenmez.

### 6. Sınıflandırma ve çıktı

Başa profilin `## Outputs` bölümündeki role göre üst başlığı koy.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

### Sonuç
[PIA gerekli / VKED zorunlu / Devam / Dur — tek cümle neden]

**FAALİYET:** [anladığın hâliyle]
**SINIF:** [DEVAM / PIA GEREKLİ / VKED ZORUNLU / DUR]
**Ev tetiği:** [Evet / Hayır]
**KVKK tabanı:** [temiz / açıklar: m. … — kısa]
**GDPR Art. 35 tetiği:** [Evet — hangi hâl / Hayır / Uygulanmaz (GDPR kapsam dışı)]
**Aydınlatma/politika çelişkisi:** [Yok / Var — hangi taahhüt]
**Hukuki sebep:** [m. 5/2-… / m. 6/3-… / açık rıza / "belirsiz — PIA'da belirlenecek"]
**Gerekçe:** [1–3 cümle]
**Kaynaklar:** ArthurLegal MCP — [madde, Kurul kararı]; doğrulanamayan: [liste] · **Tartışmalı:** [liste]

*PIA GEREKLİ ya da VKED ZORUNLU ise — ilerlemeden önce koşullar:*
| Gereklilik | Sahibi | Tamam? |
|---|---|---|
| [PIA — VKED formatında ise belirt] | [gizlilik hukukçusu] | ☐ |
| [Meşru menfaat denge testi (m. 5/2-f)] | [gizlilik hukukçusu] | ☐ |
| [Veri işleyen sözleşmesi / standart sözleşme + 5 iş günü bildirim] | [hukuk] | ☐ |
| [Aydınlatma metni güncellemesi] | [gizlilik hukukçusu] | ☐ |
| [VERBİS güncellemesi] | [irtibat kişisi] | ☐ |
| [Açık rıza mekanizması kuruldu ve test edildi] | [ürün] | ☐ |
| [Hak başvuru süreci yeni veri kategorisini kapsıyor] | [gizlilik / ürün] | ☐ |

*DUR ise:*
**Çelişki:** [taahhüt ya da ilke ve madde]
**İlerlemek için biri değişmeli:** (A) faaliyeti çelişki doğurmayacak şekilde yeniden tasarla · (B) aydınlatma metnini/politikayı güncelle (güncellemenin hukuki sebeple tutarlılığı ayrıca incelenir)
```

Yol yoksa yol uydurma: faaliyet taahhütlerle ya da hukuki sebeple bağdaşmıyorsa bunu açıkça söyle.

PIA GEREKLİ ya da VKED ZORUNLU sonucundan sonra her zaman sor: "PIA'ya şimdi başlayayım mı? Ayrı komut çalıştırmadan mülakat sorularını sorup değerlendirmeyi yazabilirim." Evet → `pia-generation` skill'ini yükle, faaliyet tanımını ve bulunan tetikleri aktararak aynı konuşmada devam et. Hayır → sonuç geçerli; PIA her zaman `/privacy-legal:pia-generation [faaliyet]` ile çalıştırılabilir.

### 7. Eklentiler arası devir

Yalnız gerçekten ilgiliyse ekle; ikisini birden kalıp olarak ekleme.
- **Yapay zekâ kararı:** faaliyette kişiler hakkında karar veren ya da karara etki eden bir yapay zekâ sistemi varsa: "PIA'ya ek olarak yapay zekâ etki değerlendirmesi gerekebilir. `/ai-governance-legal:aia-generation [faaliyet]` (ArthurLegal'de hazırlanıyor: Faz 1 İş 5; o zamana kadar yapay zekâ etki değerlendirmesini bu PIA içinde ayrı bir bölüm olarak yürüt) — ikisi birbirinin yerine geçmez."
- **Ürün lansmanı:** yeni ürün özelliği ise: "Lansmansa ürün hukukçusunu dahil et. `/product-legal:launch-review` (ArthurLegal'de hazırlanıyor; o zamana kadar ürün hukukçusuyla doğrudan koordine et)."

## Toplu triage

Özellik listesi, yol haritası ya da iş listesi gelirse önce özet tablo, sonra DEVAM olmayan her satırı aç:

| # | Faaliyet | Sınıf | Ana koşul / engel |
|---|---|---|---|
| 1 | [faaliyet] | 🟢 Devam | — |
| 2 | [faaliyet] | 🟡 PIA gerekli | Meşru menfaat denge testi; veri işleyen sözleşmesi yok |
| 3 | [faaliyet] | 🟠 VKED zorunlu | AB'deki kişilerin özel nitelikli verisi, büyük ölçek |
| 4 | [faaliyet] | 🔴 Dur | Aydınlatma metniyle çelişki — amaç sınırlaması (m. 4/2-c) |

## Uç durumlar

- **"Anonim" otomatik DEVAM değildir.** Anonimleştirme, başka verilerle eşleştirilerek dahi kimliği belirli veya belirlenebilir bir kişiyle ilişkilendirilemeyecek hâle getirmedir (m. 3/1-b). Nasıl yapıldığını ve yeniden tanımlamanın gerçekçi olup olmadığını sor; kimliği "belirlenebilir" kaldıkça veri kişisel veridir (m. 3/1-d).
- **"Benzerini zaten yapıyoruz" triage değildir.** Hiç değerlendirilmemiş mevcut işleme yeni işlemeyi korumaz; ölçek, amaç ya da veri kategorisi belirgin biçimde farklıysa yeniden triage.
- **"Sadece pilot" triage'ı atlatmaz.** Gerçek kullanıcı ya da çalışan verisine dokunan pilot aynı tetiklere tabidir.
- **"Tedarikçi gizliliği hallediyor."** Tedarikçi altyapıyı yönetir; amaçları belirleyen veri sorumlusu sizsiniz (m. 3/1-ı) ve güvenlik tedbirlerinden onunla müştereken sorumlusunuz (m. 12/2). Sözleşme gerekir, triage amaç için yine uygulanır.
- **Çıkarım ve türetilmiş veri sayılır.** Davranış skoru, tahmini tercih gibi kişi hakkında üretilen bilgi, belirlenebilir kişiye ilişkin her türlü bilgi olarak kişisel veridir (m. 3/1-d). "Sadece skor hesaplıyoruz" skorun neyi temsil ettiğini gizlemesin.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6698", madde_no=["2","3","4","5","6","8","9","10","16","18"])
tr_mevzuat_madde_getir(number="5326", madde_no=["17"])
tr_mevzuat_ara(query="Veri Sorumluları Sicili", types=["KKY"])  → tr_mevzuat_icinde_ara(mevzuat_id=..., query="değişiklik")
tr_semantik_ara(kurum="kvkk", query="aydınlatma yükümlülüğünün yerine getirilmemesi idari para cezası")
tr_semantik_ara(kurum="kvkk", query="açık rıza alınmadan pazarlama")
tr_kurum_karari_ara(kurum="kvkk", query="aydınlatma")   ← yalnız son sayfaları tarar; sıra tarihe göre değil; arşiv için tr_semantik_ara
tr_kurum_karari_getir(kurum="kvkk", id=<sonuçtaki id>)
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde için "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" (Kurul kararında https://www.kvkk.gov.tr/). Atıf etiketi: `[ArthurLegal TR — 6698 m. X — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu triage'a göre uyarla (PIA'yı başlat, DPA incelemesi, aydınlatma metni güncellemesi, eskalasyon, ek olgu iste, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Değerlendirmeyi yazmaz; gerekip gerekmediğini söyler (yazım `pia-generation`'da).
- İşlemeyi onaylamaz; sınıf bir öneridir, karar avukatın.
- Ceza tutarı söylemez; tutarlar her yıl değişir, güncel kaynaktan teyit edilir.
