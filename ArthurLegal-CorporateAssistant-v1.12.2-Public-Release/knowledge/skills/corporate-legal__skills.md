# corporate-legal - Skill Referans Kitapcigi

> Değişiklik bildirimi (Apache-2.0 md. 4(b)): Bu kitapçık Anthropic'in `claude-for-legal` deposundaki aynı adlı eklentiden uyarlanmıştır. ArthurLegal tarafından Türk hukuku esas alınarak Türkçe yeniden yazılmıştır (2026-10); yabancı yargı çevreleri için yalnız ArthurLegal MCP araçlarına yönlendirir. Üst kaynak ve sürüm izi: ATTRIBUTION.md.

> Alan: Kurumsal ve M&A - due diligence, board, entity
> Toplam skill: 13
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /corporate-legal:ai-tool-handoff (112 satir)
- /corporate-legal:board-minutes (168 satir)
- /corporate-legal:closing-checklist (219 satir)
- /corporate-legal:cold-start-interview (207 satir)
- /corporate-legal:customize (51 satir)
- /corporate-legal:deal-team-summary (116 satir)
- /corporate-legal:diligence-issue-extraction (186 satir)
- /corporate-legal:entity-compliance (230 satir)
- /corporate-legal:integration-management (294 satir)
- /corporate-legal:material-contract-schedule (132 satir)
- /corporate-legal:matter-workspace (136 satir)
- /corporate-legal:tabular-review (193 satir)
- /corporate-legal:written-consent (193 satir)

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
| AZ istirak / JV yapisi, Azerbaycanli karsi taraf islemleri — akt + statu | `/legal-research:az-mevzuat` |
| yabanci sirketler hukuku karsilastirmasi, M&A yapisi ogretisi — **ikincil** | `/legal-research:karsilastirmali-doktrin` |
| hedef sirketin maddi sozlesmelerinde kloz benchmark (diligence) | `/legal-research:sozlesme-emsali` |

Rehberler: `references/eqanun-mcp-rehberi.md` · `references/lex-scholar-rehberi.md` · `references/resourcecontracts-rehberi.md` · `references/karsilastirmali-hukuk-rehberi.md` · `references/nl-rechtspraak-mcp-rehberi.md` · `references/pl-sejm-mcp-rehberi.md` · `references/at-ris-mcp-rehberi.md` · `references/ie-statutebook-mcp-rehberi.md` · `references/fi-finlex-mcp-rehberi.md` · `references/es-boe-mcp-rehberi.md`

---

---

## /corporate-legal:ai-tool-handoff

---
name: ai-tool-handoff
description: >
  Luminance, Kira ya da benzeri bir toplu inceleme aracı kullanıldığını tespit
  eder, yüksek hacimli kloz çıkarımını ona devreder ve dönen çıktıyı
  `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`'deki
  güven düzeyine göre kalite kontrolünden geçirir; ardından Türk hukuku
  yargı katmanını (işlem yapısına göre CoC/devir gerçekten tetikleniyor mu —
  TBK m. 205, TTK m. 153) uygular. "Luminance'a gönder", "toplu inceleme",
  "yapay zekâ çıkarımı" denildiğinde ya da diligence-issue-extraction yüksek
  hacimli bir kategoriye geldiğinde kullan.
---

# /ai-tool-handoff — Toplu İnceleme Aracına Devir

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Luminance ve Kira tek bir işte iyidir: 500 sözleşmeyi okuyup her kontrol değişikliği klozunu bulmak. Yargıda zayıftır: belirli bir CoC hükmünün bu işlem yapısında gerçekten tetiklenip tetiklenmediğine karar vermek. Bu skill toplu çıkarımı doğru araca verir, dönen sonuca kalite kontrolü ve yargı katmanını uygular.

**Devretmeden önce:** `/corporate-legal:tabular-review`'i dene. Ortamın kaldırabildiği işte (birkaç yüz belge, tanımlı sütun şeması) yerel tablolu inceleme daha hızlı kurulur, belge başı maliyeti yoktur ve iş ürünü yerelde kalır. Korpus gerçekten çok büyükse, ekibin lisansı ve iş akışı zaten varsa ya da matter doğrulanmış bir köken zinciri olan araç gerektiriyorsa devret.

## Bağlam

CLAUDE.md → `## M&A` YZ toplu inceleme aracı ayarı (`AI-assisted review`): kullanılan araç (Luminance / Kira / yok), ne için kullanıldığı (hangi kloz türleri), güven düzeyi (olduğu gibi kullan / örneklem kontrolü / tam yeniden inceleme), devir süreci (kim yükler, kim kontrol eder). CLAUDE.md araç yok diyorsa bu skill işlem yapmaz; her şey doğrudan diligence-issue-extraction'dan geçer.

## Ne zaman devret

Hepsi birlikte varsa: kategoride 50'den fazla belge (altında okumak daha hızlı); çıkarım hedefi aracın iyi olduğu kloz türü (CoC, devir, münhasırlık, MFN, fesih, otomatik yenileme); belgeler makul ölçüde tek tip (aynı kâğıt üzerinde müşteri sözleşmeleri — sözleşme, mektup ve YK kararı karışımı değil).

Devretme: özel ya da yoğun müzakere edilmiş belgeler; yan mektuplar ve tadiller (ana sözleşmeyle etkileşimi araç kaçırır); sorunun "bu kloz var mı" değil "bu işlem için ne anlama geliyor" olduğu her şey.

**Türkçe belgeler.** Aracın Türkçe metinde (özellikle taranmış, OCR'lı belgelerde ve Türkçe karakterlerde) başarısı bu ekipte ölçülmediyse "olduğu gibi kullan" güven düzeyini uygulama; en az örneklem kontrolü öner ve CLAUDE.md'ye not düşmeyi teklif et.

**Kişisel veri ve gizlilik.** Kişisel veri içeren belgeleri üçüncü taraf platforma yüklemek, platformla veri işleyen ilişkisini ve aktarım kurallarını (KVKK m. 8) gündeme getirir — yurt içi hizmet sağlayıcıya iletimin nitelendirilmesi **tartışmalı**; platform sunucusu yurt dışındaysa veri işleyenleri de kapsayan yurt dışına aktarım kuralları uygulanır (KVKK m. 9: yeterlilik kararı ya da uygun güvenceler, standart sözleşmenin 5 iş günü içinde Kurula bildirimi). Hangi işleme ve aktarım şartının uygulanacağı olaya bağlıdır — yüklemeden önce `/privacy-legal:dpa-review` ile platform sözleşmesini kontrol ettir; gerekirse çalışan dosyaları gibi kişisel veri yoğun klasörleri partiden çıkar ya da maskele. Müvekkil sırrı için de aynı dikkat: platformun hizmet koşulları gizliliği nasıl düzenliyor?

## Devir

### Adım 1: Partiyi hazırla

VDR envanterinden belgeleri seç; CLAUDE.md'ye göre çıkarım hedeflerini belirt; çıktının süzülebilmesi için önemlilik eşiğini not et.

### Adım 2: Yükle (ya da yükleyene talimat ver)

CLAUDE.md kimin yüklediğini söyler. Sen isen yükleme talimatını üret; başkasıysa talebi:

```markdown
## [Araç] Yükleme Talebi — [işlem kodu] — [kategori]

**Belgeler:** VDR klasörü [yol]'dan [N] belge
**Yüklenecek yer:** [araç çalışma alanı / matter]
**Çıkarım hedefleri:**
- Kontrol değişikliği / devir (birleşme, bölünme, tür değiştirmeye atıflar dahil)
- Münhasırlık
- [CLAUDE.md'ye göre diğerleri]
**Çıktı süzgeci:** yalnız hedefin bulunduğu belgeleri işaretle — her belge için "CoC yok" satırı gerekmez.
**Dönüş tarihi:** [tarih]
```

### Adım 3: Kalite kontrolü

Araç sonuç döndürünce güven düzeyini uygula:
- **"Olduğu gibi kullan":** doğrudan bulgulara al. (Yalnız CLAUDE.md böyle diyorsa — nadirdir.)
- **"%X örneklem kontrolü":** işaretlenen belgelerin %X'ini rastgele seç; her birinde gerçek klozu oku ve aracın çıkarımıyla karşılaştır. Hata oranı düşükse partiyi kabul et; hata varsa örneklemi genişlet.
- **"İşaretlenenlerin tamamını insan okur":** araç evreni daraltır (500 belge → CoC'li 80); insan 80'in hepsini okur. Araç temiz 420'yi okuma zamanını kazandırmıştır.

### Adım 4: Yargı katmanı

Araç klozları buldu; şimdi her CoC/devir hükmü için sor: **bu işlem onu gerçekten tetikliyor mu?**
- **İşlem yapısı:** pay devrinde sözleşmenin tarafı değişmez — yalnız CoC klozu tetiklenir, devir yasağı tetiklenmez. Malvarlığı/işletme devrinde sözleşmenin devri karşı tarafın katılımını ya da izni/onayını gerektirir (TBK m. 205) — devir hükmü sessiz olsa bile. Birleşmede tescille aktif ve pasif kendiliğinden geçer (TTK m. 153/1); sözleşmedeki devir yasağının birleşmeye uygulanması **tartışmalı — içtihadı kontrol et**, metin birleşmeyi açıkça anıyorsa ona göre.
- **"Kontrol" tanımı:** pay çoğunluğu mu, YK çoğunluğunu seçme hakkı mı, dolaylı kontrol mü, başka bir şey mi? Üst şirket düzeyindeki işlem dolaylı kontrolü değiştiriyor mu?
- **İstisna:** grup içi yeniden yapılanma, halka arz ya da bu tür işlem için bir istisna var mı?
- **Uygulanacak hukuk:** sözleşme yabancı hukuka tabiyse yorumu o hukuka göre çek (`uk_`, `de_`, `eu_`, `nl_` …) ya da `/commercial-legal:governing-law-review`.

Bu, aracın yapamadığı kısımdır. Sonuç büro formatında due diligence bulgularına gider.

## Çıktı

> Aşağıdaki kalite kontrol özeti gizli VDR belgelerinden türetilmiştir ve onların gizlilik statüsünü devralır; dağıtımı işlem ekibiyle sınırla (Av. K. m. 36 dağıtılan belgeyi korumaz).

```markdown
## Toplu İnceleme Devri Özeti — [kategori]

**Araç:** [Luminance / Kira]   **İşlenen belge:** [N]   **Hedefler:** [kloz türleri]
**İşlem yapısı:** [pay devri / malvarlığı devri / birleşme]

### Kalite kontrolü
**Güven düzeyi:** [CLAUDE.md'ye göre]
**Örneklem:** [N] belge   **Hata oranı:** %[X] — [Kabul / Örneklem genişletildi / Tam yeniden inceleme]

### Sonuçlar
| Kloz türü | İşaretlenen | Yargı katmanı sonrası | Önemli |
|---|---|---|---|
| Kontrol değişikliği | [N] | [N — bu yapıda gerçekten tetiklenen] | [N — eşik üstü] |
| Devir | [N] | [N] | [N] |

**→ due diligence bulgularına [N] sorun eklendi**
**→ kapanış listesine [N] onay eklendi**
```

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu çıktıya göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Luminance ya da Kira'yı çalıştırmaz — devri ve kalite kontrolünü yönetir; çıkarımı insan ya da aracın kendi arayüzü yapar.
- Aracın çıktısını tamamen kendi yargısıyla değiştirmez — CLAUDE.md %10 diyorsa %10 kontrol eder, %100 değil.
- Güven düzeyine karar vermez — o, cold-start'ta ekibin araç deneyimine göre CLAUDE.md'ye yazılmıştır.

---

## /corporate-legal:board-minutes

---
name: board-minutes
description: >
  Yönetim kurulu kararı, YK/komite toplantı tutanağı, genel kurul toplantı tutanağı
  ve limited şirkette müdürler kurulu / ortaklar genel kurulu kararlarını ev
  formatında taslaklar. Takvimden yaklaşan YK, komite ve genel kurul toplantılarını
  bulur, gündem ve sunumları ister; TTK'ya göre nisabı (m. 390, 418, 620, 624),
  müzakereye katılma yasağını (m. 393), Bakanlık temsilcisi gerekliliğini (m. 407/3 ve
  Yönetmelik m. 32), tutanak içeriğini ve tescil adımlarını (m. 422) kontrol eder.
  Toplantısız karar için written-consent'e yönlendirir. Tetikleyiciler: "yönetim kurulu
  kararı", "YK tutanağı", "genel kurul tutanağı", "komite tutanağı", "board minutes",
  "yaklaşan YK toplantısı" ya da takvimde YK/GK toplantısı görülmesi.
---

# Yönetim Kurulu ve Genel Kurul Tutanakları

## Matter context

`## Matter workspaces` bölümüne bak (uygulama düzeyi CLAUDE.md). `Enabled` `✗` ise (şirket içi kullanıcıda varsayılan) bu paragrafı atla; matter katmanı görünmez. Açık ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Tutanak ve karar şirketin hukuki kaydıdır; finansman, denetim, sicil işlemi ve M&A veri odasında incelenir. Türk hukukunda şekil geçerlilik meselesidir: YK kararlarının geçerliliği yazılıp imzalanmalarına bağlıdır (TTK m. 390/5); YK karar defteri ve genel kurul toplantı ve müzakere defteri ticari defterdir (m. 64/4) ve bunların tutulması YK'nın devredilemez görevidir (m. 375/1-f). Genel kurul tutanağı toplantı başkanlığınca ve (temsilci bulunan toplantıda) Bakanlık temsilcisince imzalanmazsa geçersizdir (m. 422/1). Bu skill taslağı ev formatında hazırlar; avukat inceler ve düzeltir.

**Kapsam:** AŞ YK toplantı kararı ve komite tutanağı · AŞ olağan/olağanüstü genel kurul tutanağı · Ltd. müdürler kurulu kararı · Ltd. genel kurul tutanağı. Toplantısız (elden dolaştırma) karar → `/corporate-legal:written-consent`.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## Board & Secretary`: tutanak biçimi (uzun anlatı / yalnız karar / karma), `**Minutes template:**` (örnek tutanaklardan çıkarılan yapı, karar dili, başlık), YK ve komite yapısı, karar defteri türü (fiziki / elektronik), elden dolaştırma kullanımı. Biçim kayıtlı değilse önce `/corporate-legal:cold-start-interview --module board` çalıştır; genel şablonla devam etme.

## ⏰ ÖN-KONTROL — Süre ve takvim

Her çalıştırmada organa göre kontrol et; kalan süre 5 günden azsa 🔴 işaretle:

- **Olağan genel kurul:** her faaliyet dönemi sonundan itibaren üç ay içinde (AŞ m. 409/1; Ltd. hesap döneminin sona ermesinden itibaren üç ay, m. 617/1).
- **Çağrı:** AŞ'de esas sözleşmedeki şekilde, internet sitesinde ve Türkiye Ticaret Sicili Gazetesinde ilanla, ilan ve toplantı günleri hariç en az iki hafta önce; pay defterinde kayıtlı ve adres bildirmiş pay sahiplerine iadeli taahhütlü mektup (m. 414/1). Ltd.'de en az on beş gün önce; şirket sözleşmesi uzatabilir ya da on güne kadar kısaltabilir (m. 617/2). Halka açık ortaklıkta internet sitesi ve KAP ilanıyla en az üç hafta önce (SerPK m. 29/1).
- **İnceleme:** finansal tablolar, faaliyet raporu, denetleme raporları ve kâr dağıtım önerisi toplantıdan en az on beş gün önce merkez ve şubelerde hazır bulundurulur (m. 437/1).
- **Toplantı sonrası:** YK, GK tutanağının noterce onaylı suretini derhâl ticaret sicili müdürlüğüne verir, tescil ve ilana tabi hususları tescil ve ilan ettirir; tutanak hemen internet sitesine konur (m. 422/2).
- **İptal riski:** kanun, esas sözleşme ya da dürüstlük kuralına aykırı GK kararına karşı m. 446'da sayılan kişiler karar tarihinden itibaren üç ay içinde iptal davası açabilir (m. 445). Tutanaktaki oy sayıları ve karşı oylar bu yüzden eksiksiz olmalı.

## Destination check

- **Tutanak / karar metni** (sicile, deftere, veri odasına gidecek) → şirket kaydıdır; üst başlık konmaz.
- **Taslak notları, yer tutucu listesi, kontrol listesi** → `## Outputs`'taki üst başlık (role göre değişir; bkz. `## Who's using this`).
- **Müvekkile / yönetime kapak notu** → kısa özet; üst başlık taşır.

## Adım 1 — Toplantıyı belirle

**Takvim taraması** (bağlantı varsa): "Yönetim Kurulu", "YK Toplantısı", "Genel Kurul", "Olağan Genel Kurul", "Olağanüstü Genel Kurul", "Denetimden Sorumlu Komite", "Riskin Erken Saptanması Komitesi", "Kurumsal Yönetim Komitesi", "Müdürler Kurulu", "Ortaklar Kurulu"; çift dilli şirkette "Board Meeting", "Audit Committee". 30 gün ileri; bulunamazsa 14 gün geri (tutanak çoğu zaman sonradan yazılır). Bulduklarını listele, hangisi olduğunu sor. Bağlantı yoksa doğrudan sor: hangi organ, hangi tarih.

**Teyit edilecek bilgiler:**
- Organ: AŞ YK / komite (adı) / AŞ GK (olağan, olağanüstü) / Ltd. müdürler kurulu / Ltd. GK
- Tarih, saat, yer: GK esas sözleşmede aksi yoksa şirket merkezinin bulunduğu yerde toplanır (m. 409/3)
- Fiziki mi, elektronik mi: YK ve müdürler kurulunun tamamen ya da kısmen elektronik ortamda toplanması şirket sözleşmesinde ya da esas sözleşmede düzenlenmiş olmasına bağlıdır; nisaplar aynen uygulanır (m. 1527/1). AŞ GK'ya elektronik katılım fizikî katılımın tüm sonuçlarını doğurur (m. 1527/5).
- Çağrı: usulüne uygun mu? Çağrısız GK: bütün payların sahipleri ya da temsilcileri itiraz etmeden toplanabilir; toplantı nisabı sürdükçe karar alır; gündeme ancak oybirliğiyle madde eklenir (m. 416).

## Adım 2 — Katılım ve nisap

**AŞ yönetim kurulu**
- Esas sözleşmede ağırlaştırıcı hüküm yoksa YK üye tam sayısının çoğunluğuyla toplanır, toplantıda hazır bulunanların çoğunluğuyla karar alır; elektronik toplantıda da aynı (m. 390/1).
- Üyeler birbirini temsilen oy veremez, vekille katılamaz (m. 390/2). Tüzel kişi üye adına yalnız tescil edilmiş gerçek kişi katılıp oy kullanır (m. 359/2).
- Oylar eşitse konu gelecek toplantıya kalır; ikincide de eşitlikse öneri reddedilmiş sayılır (m. 390/3).
- **Müzakereye katılma yasağı:** üyenin (ya da eşinin, alt-üst soyunun, üçüncü derece dâhil kan ve kayın hısımlarının) şirket dışı kişisel menfaati şirket menfaatiyle çatışıyorsa üye müzakereye katılamaz; tereddütte kararı YK verir, bu oylamaya ilgili üye katılamaz; katılmama sebebi ve ilgili işlemler karara yazılır (m. 393/1, 393/3). Nisap hesabını buna göre yap ve avukata işaretle.
- YK üyesinin şirketle kendisi ya da başkası adına işlem yapması **genel kurul izni** gerektirir (m. 395/1); YK kararı bunun yerine geçmez.

**AŞ genel kurul**
- Hazır bulunanlar listesi: katılabilecekler listesi YK başkanınca imzalanıp toplantı yerinde bulundurulur; katılanların imzaladığı liste "hazır bulunanlar listesi"dir (m. 417/3-4).
- Kanun ya da esas sözleşmede daha ağır nisap yoksa sermayenin en az dörtte birini karşılayan payların sahipleri ya da temsilcileriyle toplanır; nisap toplantı boyunca korunur; ilk toplantıda sağlanamazsa ikinci toplantıda nisap aranmaz; kararlar hazır bulunan oyların çoğunluğuyla verilir (m. 418). Ağırlaştırılmış nisap gerektiren kararı (esas sözleşme değişikliği vb.) kanun ve esas sözleşmeden ayrıca kontrol et.
- Murahhas üyeler ve en az bir YK üyesi hazır bulunur; denetçi hazır bulunur (m. 407/2).
- **Bakanlık temsilcisi:** Bakanlık izniyle kurulan şirketlerin (m. 333) bütün GK'larında; diğer şirketlerde gündeminde sermaye artırımı/azaltımı, kayıtlı sermaye sistemine geçiş/çıkış ya da tavan artırımı, faaliyet konusu değişikliği, birleşme, bölünme veya tür değişikliği bulunan toplantılarda; elektronik GK uygulayan şirketlerde ve yurt dışındaki toplantılarda zorunludur. Zorunlu olduğu toplantıda temsilcinin yokluğunda alınan kararlar geçerli değildir (m. 407/3; Yönetmelik m. 32/1, 32/4). Gündemi buna göre tara.

**Limited şirket**
- Müdürler kurulu: çoğunlukla karar alır; eşitlikte başkanın oyu üstündür; şirket sözleşmesi farklı düzenleyebilir (m. 624/3).
- Genel kurul: kararlar toplantıda temsil edilen oyların salt çoğunluğuyla (m. 620); m. 621'deki önemli kararlar (işletme konusu ve merkez değişikliği, sermaye artırımı, pay devrinin sınırlandırılması, fesih vb.) temsil edilen oyların en az üçte ikisi ve oy hakkı bulunan esas sermayenin salt çoğunluğuyla. Oy hakkı itibarî değere göre hesaplanır (m. 618/1); müdürlerin ibrasında yönetime katılmış olanlar oy kullanamaz (m. 619/1). AŞ'nin çağrı, gündem, çağrısız GK ve tutanak hükümleri kıyasen uygulanır, Bakanlık temsilcisine ilişkin olanlar hariç (m. 617/3).

**Nisap yoksa dur.** Geçerli toplantı yapılmış izlenimi veren tutanak üretme. Durumu avukata yaz; çözüm yolu (yeniden toplantı, YK için elden dolaştırma, sonraki GK) esas sözleşmeye ve işlemin niteliğine bağlıdır.

**Diğer katılımcılar:** yöneticiler, dış avukat, denetçi, danışmanlar (yalnız belirli gündem maddesine katıldıysa bunu yaz). Toplantı başkanı ve tutanak yazmanı: GK'yı esas sözleşmede aksi yoksa genel kurulca seçilen başkan yönetir; başkan tutanak yazmanını ve gerekirse oy toplama memurunu belirler (m. 419/1).

## Adım 3 — Materyaller

> Toplantının gündemini ve ön okuma materyallerini paylaşabilir misiniz? Kaba bir gündem de yeter. YK sunumu, finansal tablo, faaliyet raporu taslağı varsa yükleyin; gündem maddesi özetlerini bunlardan çıkarırım. Materyal yoksa gündem maddelerini söyleyin, her biri için yer tutucu koyarım.

Çıkar: sıralı gündem maddeleri; önerilen kararlar ("onaylanmasına", "seçilmesine", "yetkilendirilmesine", "ibra edilmesine"); ekler (sunum, finansal tablo, değerleme, sözleşme taslağı); beklenen oylamalar. **GK'da gündemde bulunmayan konu müzakere edilemez ve karara bağlanamaz** (kanuni istisnalar saklı); YK üyelerinin görevden alınması ve yenilerinin seçimi yılsonu finansal tablolarının müzakeresiyle ilgili sayılır (m. 413/2-3). Gündem dışı karar varsa işaretle.

## Adım 4 — Taslak

Ev formatını kullan (`**Minutes template:**`); örnek tutanakların yapısını, başlığını, karar dilini ve tartışma derinliğini birebir izle. Aşağıdaki iskeletler yalnız varsayılandır.

**AŞ YK kararı (toplantılı):**
```
[ŞİRKET ADI] (ticaret unvanı)
YÖNETİM KURULU KARARI
Karar Tarihi: [GG.AA.YYYY]   Karar No: [YYYY/NN]
Toplantı yeri / şekli: [şirket merkezi / elektronik ortam — esas sözleşme m. [..]]
Toplantıya katılanlar: [ad soyad — sıfat]   Katılmayanlar: [..]
Nisap: Üye tam sayısı [N]; hazır bulunan [N] (TTK m. 390/1)

Gündem:
1. [..]

Şirket yönetim kurulu yukarıdaki tarihte toplanarak aşağıdaki kararları almıştır:
1. [Kesin karar metni — kim, ne, hangi tutar, hangi belge (Ek-1)] hususunun
   [oybirliği / oyçokluğu ([N] kabul, [N] ret)] ile kabulüne.
   [Müzakereye katılmayan üye ve sebebi — TTK m. 393/3]
2. [..]

[İmza blokları — toplantıya katılan üyeler]
```

**AŞ GK tutanağı:** başlık ("[ŞİRKET ADI] (ticaret unvanı) [YIL] YILINA AİT OLAĞAN GENEL KURUL TOPLANTI TUTANAĞI"); toplantı tarihi, yeri, Bakanlık temsilcisinin adı ve görevlendirme yazısı (varsa); çağrının nasıl yapıldığı; hazır bulunanlar listesine göre nisap; başkanlık oluşturulması; her gündem maddesi için görüşme özeti, sorulan sorular ve verilen cevaplar, karar ve **olumlu ve olumsuz oy sayıları**; karşı oy ve muhalefet şerhleri. Tutanak; pay sahiplerini ya da temsilcilerini, paylarını, gruplarını, sayılarını ve itibarî değerlerini de içerir (m. 422/1). Olağan GK gündeminde tipik başlıklar: organların seçimi, finansal tablolar, YK yıllık raporu, kârın kullanım şekli ve dağıtılacak kâr payı oranları, YK üyelerinin ibrası (m. 409/1). İmza: toplantı başkanlığı ve toplantıda bulunuyorsa Bakanlık temsilcisi (m. 422/1; temsilcinin zorunlu olduğu toplantılar Yönetmelik m. 32).

**Ltd.:** müdürler kurulu kararında AŞ YK iskeletini kullan, nisap satırını m. 624/3'e ve şirket sözleşmesine göre yaz; GK tutanağında Bakanlık temsilcisi satırını çıkar (m. 617/3).

**Yazım notları**
- **Tartışma derinliği:** *uzun anlatı* — sunulan bilgi, sorulan sorular, kurulun gözettiği etkenler; kişiye söz atfı yalnız hukuken önemliyse. *Yalnız karar* — "konu görüşüldü" ve karar. *Karma* — önemli maddelerde anlatı, rutinde yalnız karar. Seed tutanaklara uy.
- Materyal varsa özetleri sunumlardan çıkar ("kurul [konu] hakkındaki sunumu inceledi"). Materyal yoksa `[YER TUTUCU — görüşme özeti]` yaz ve işaretle; **görüşme içeriği uydurma**.
- **Karar dili ev üslubudur** ("... kabulüne", "... onaylanmasına karar verildi", "... yetkili kılınmasına"); bir tutanak içinde değiştirme.
- **Ekler** sırayla numaralanır (Ek-1, Ek-2): sunum, finansal tablolar, değerleme raporu, hazır bulunanlar listesi, vekâletnameler.
- **Tescil gerektiren kararlar** ayrı işaretlenir: temsile yetkili kişiler ve temsil şekli (noter onaylı suret sicile, m. 373/1); denetçi seçimi (m. 399/1); GK iç yönergesi (m. 419/2); GK tutanağındaki tescile tabi hususlar (m. 422/2).

## Adım 4.5 — Sonuç doğuran eylem kapısı (tutanağı kesinleştirme)

`## Who's using this` → Role **avukat değilse**:

> İmzalanan tutanak ve deftere geçen karar, kurulun ne karar verdiğinin resmî kaydıdır; işlemlerin yetkilendirildiğinin birincil delilidir. Bunu bir avukatla gözden geçirdiniz mi? Evetse devam ederim. Hayırsa avukata götürmeniz için kısa brif:
> - Ne karara bağlandı (kararlar, oylar, kimler hazırdı)
> - Taslak neyi yakaladı, neler hâlâ yer tutucu
> - Açık sorular (nisap, müzakereye katılma yasağı, Bakanlık temsilcisi, gündem dışı madde)
> - Ne ters gidebilir (geçersiz karar, iptal davası, eksik oy sayısı, tescil gecikmesi)
> - Avukata sorulacaklar (tartışma derinliği doğru mu; hangi kararlar tescil ve ilan gerektiriyor)
>
> Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz.

Açık "evet" olmadan imzaya hazır sürüm üretme; avukat incelemesi için TASLAK işaretli metin serbest.

## Adım 5 — Çıktı ve kontrol listesi

Tam taslağı üret. Tutanağın kendisi şirket kaydıdır, üst başlık almaz; taslak notları ve aşağıdaki liste alır:

```
[ÜST BAŞLIK — ## Outputs; role göre]
İMZA ÖNCESİ KONTROL
□ Katılan/katılmayan üyeler fiilî katılımla örtüşüyor
□ Toplantı ve karar nisabı doğru (m. 390/1, 418, 620-621, 624/3; esas sözleşme)
□ Karar metni onaylanan şeyle birebir aynı
□ Oy sayıları, karşı oylar ve muhalefet şerhleri yazıldı
□ Müzakereye katılma yasağı ve sebebi karara yazıldı (m. 393/3)
□ GK: hazır bulunanlar listesi ekli; gündem dışı karar yok; Bakanlık temsilcisi gerekliyse hazırdı
□ Ekler numaralandı ve atıfta bulunuldu
□ Karar defterine yazım / yapıştırma yapılacak; defter onay durumu (fiziki / elektronik)
□ Tescil-ilan ve internet sitesi adımları planlandı (m. 373/1, 422/2)
□ Kapanış saati ve imza blokları dolduruldu
```

Yer tutucu bölümleri ayrıca listele. Taslağın başına (kesinleşmeden önce çıkarılacak) not koy:

> **⚠️ İnceleyen notu:** Bu metin avukat incelemesi için taslaktır, kesinleşmiş karar ya da tutanak değildir. İmzalanan tutanak şirket organının işleminin resmî kaydıdır ve hukuki sonuç doğurur; avukat inceleyip düzeltmeden ve sorumluluğu üstlenmeden imzaya sunmayın.

## Toplantısız kararlar

YK'nın elden dolaştırma yoluyla kararı (m. 390/4), Ltd. GK'nın yazılı onayla kararı (m. 617/4) ve tek pay sahipli/tek ortaklı şirketin yazılı kararı → `/corporate-legal:written-consent`.

## Bu skill ne yapmaz

- Toplantıya katılmaz, anlık görüşmeyi yakalamaz; materyallerden ve avukat girdisinden yazar.
- Kararın hukuken geçerli ya da yeterli olduğuna karar vermez; nisap ve şekil işaretleri avukatın değerlendirmesi içindir.
- Tutanağı kesinleştirmez, deftere işlemez, sicile başvurmaz, dağıtmaz.

---

## /corporate-legal:closing-checklist

---
name: closing-checklist
description: >
  Kapanışı ne engelliyor — kapanış kontrol listesini durum, kritik yol ve
  kapanışa kalan günle tutar. Kendini günceller: due diligence bulgularından ve
  ek çalışmalarından yeni kalemleri alır, durumu izler, engelleri gösterir.
  Türk hukukundaki kapanış kalemlerini (Rekabet Kurulu izni — 4054 m. 7 ve
  2010/4 sayılı Tebliğ, pay devri onayları ve şekli — TTK m. 490-494, 595,
  pay defteri ve ticaret sicili tescili) kaynaklarıyla yazar. "Kapanış kontrol
  listesi", "kapanışa ne kaldı", "liste durumu", "listeye ekle" denildiğinde
  ya da zamanlanmış durum raporunda kullan.
argument-hint: "[isteğe bağlı: kalem kimliği + durum güncellemesi]"
---

# /closing-checklist — Kapanış Kontrol Listesi

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/closing-checklist.yaml` oku; aşağıdaki modları kullan.
2. Durum güncellemesi verildiyse: Mode 3.
3. Yoksa Mode 4: engelleyici kalemler, kritik yol, kapanışa kalan gün.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

İşlem, liste bittiğinde kapanır: listedeki her şey yapılmış, hiçbir şey eksik değil. Bu skill listeyi tutar, due diligence'tan gelen kalemleri ekler ve ekibe neyin engellediğini söyler.

## Liste

`~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/closing-checklist.yaml`. Anahtarlar İngilizce kalır (integration-management ve dataroom-watcher bu dosyayı okur); kalem metinleri Türkçe.

```yaml
deal_code: "Proje Şahin"
target_close: [TARİH]
signing_date: [TARİH]
last_updated: [TARİH]

conditions_precedent:
  - id: CP-001
    item: "Rekabet Kurulu izni"
    category: "Regulatory"
    responsible: "Alıcı avukatı"
    due: 2026-04-15
    status: "Bildirim 2026-03-01; bildirimin tam sayıldığı tarih teyit edilecek"
    blocking: true
    source: "SPA m. 7.1(a); 4054 m. 7; Tebliğ 2010/4 m. 7, 10"

  - id: CP-002
    item: "[Karşı taraf] onayı — çerçeve sözleşme CoC"
    category: "Third-party consents"
    responsible: "Hedef — [ad]"
    due: 2026-04-20
    status: "Talep 2026-03-10 gönderildi, cevap yok"
    blocking: true
    source: "Ek 3.12(a)(4); [Karşı taraf] sözleşmesi m. 14.2"

closing_deliverables:
  - id: CD-001
    item: "Ticaret sicili kayıt örneği / sicil tasdiknamesi — Hedef"
    category: "Corporate"
    responsible: "Satıcı avukatı"
    due: 2026-04-28
    status: "Başlanmadı"
    blocking: true
    source: "SPA m. 2.3(b)(iv); TTK m. 35/2"

  - id: CD-002
    item: "Pay devri — AŞ: ciro + teslim / Ltd.: noter onaylı devir sözleşmesi"
    category: "Corporate"
    responsible: "Satıcı avukatı"
    due: 2026-04-30
    status: "Taslak hazır"
    blocking: true
    source: "SPA m. 2.2; TTK m. 490/2 (AŞ) ya da m. 595/1 (Ltd.)"
  # ... vb.
```

ABD'deki "good standing" belgesinin karşılığı yoktur; yerine güncel sicil kaydı/tasdiknamesi, TTSG ilanları, vergi ve SGK "borcu yoktur" yazıları ve imza sirküleri istenir — sözleşmede hangisi yazıyorsa o.

## Modlar

### Mode 1: Satın alma sözleşmesinden kur

İmzalanmış (ya da son hâline yakın) sözleşmeyi oku ve çıkar: her ön koşul (yeri sözleşmeye göre değişir — gerçek başlıkları oku), her kapanış teslimi, kapanış öncesi süreli her taahhüt. Her biri sözleşme maddesine atıflı bir kalem olur.

**Şirket onayları ve şekil — yapıya göre:**

| Yapı | Kalem | Dayanak |
|---|---|---|
| AŞ pay devri | Esas sözleşmede devir sınırlaması varsa şirketin onayı (uygulamada YK kararı); borsaya kote olmayan payda red sebepleri sınırlı; 3 ay içinde reddedilmezse onay verilmiş sayılır | TTK m. 492-494 |
| AŞ pay devri | Bedeli tamamen ödenmemiş nama yazılı paylar için şirket onayı | TTK m. 491 |
| AŞ pay devri | Nama yazılı pay senedinde ciro + zilyetliğin geçirilmesi; hamiline senette MKK bildirimi | TTK m. 490/2, 489 |
| AŞ pay devri | Pay defterine kayıt — devralan ancak usulüne uygun devir ispat edilince yazılır | TTK m. 499/2 |
| Ltd. pay devri | Yazılı devir sözleşmesi, imzalar noter onaylı; ortaklar genel kurulu onayı (sözleşmede aksi yoksa); onayla geçerlilik | TTK m. 595/1-2, 616/1-g, 620 |
| Ltd. pay devri | Pay defteri kaydı; müdürlerin ticaret siciline tescil başvurusu (30 gün içinde yapılmazsa ayrılan ortak silinmeyi isteyebilir) | TTK m. 594, 598 |
| Malvarlığı / işletme devri | Önemli miktarda şirket varlığının toptan satışı için AŞ genel kurulu; ticari işletme devri sözleşmesi yazılı, tescil ve ilan; sözleşme devirleri | TTK m. 408/2-f, 11/3; TBK m. 205 |
| Birleşme | Birleşme sözleşmesi yazılı, yönetim organlarınca imza, genel kurul onayı; nisaplar (AŞ: esas/çıkarılmış sermayenin çoğunluğunu temsil şartıyla mevcut oyların 3/4'ü; Ltd.: sermayenin en az 3/4'ünü temsil eden tüm ortakların 3/4'ü); tescil başvurusu; tescille geçerlilik | TTK m. 145, 151, 152, 153 |

Tescil edilen hususlar TTSG'de ilanı izleyen iş gününden itibaren üçüncü kişilere karşı sonuç doğurur (TTK m. 36/1) — kapanış tarihini ve "yürürlük" beyanlarını buna göre kur.

**Düzenleyici kalemlerden önce araştır.** Rekabet, sektör ve yabancı yatırım onaylarının mekaniği, eşikleri ve süreleri değişir. Koşulun adını sözleşmeden al, işleyen kuralı birincil kaynaktan çek, güncelliğini doğrula; süreyi hafızadan doldurma.
- **Rekabet:** kontrolde kalıcı değişiklik yaratan işlem birleşme/devralma sayılır (Tebliğ 2010/4 m. 5); izne tabiyet ciro eşiklerine bağlıdır (m. 7 — **güncel eşikleri Tebliğ'den teyit et**; teknoloji teşebbüsü istisnası m. 7/2). İzne tabi işlem karar verilmeden hukuken geçerlilik kazanamaz (Tebliğ m. 10/4); Kurul ön incelemeyi bildirimden itibaren 15 günde yapar, nihai incelemeye alırsa işlem askıdadır; süresinde cevap yoksa bildirimden 30 gün sonra geçerlilik kazanır (4054 m. 10). Bildirim, eksiksiz bilgiler Kurul kayıtlarına girdiğinde yapılmış sayılır (Tebliğ m. 11) — süre hesabını buna göre yap. İzinsiz kapanış: idari para cezası (4054 m. 16/1-b; alt sınır yıllık güncellenir — teyit et) ve m. 11 tedbirleri. Emsal için `tr_kurum_karari_ara(kurum="rekabet", decision_type="birlesme_devralma", query="[pazar / taraf]")` — dönen künyeyi birebir kullan.
- **Sektör:** EPDK, BDDK, SPK, BTK, sigortacılık onayları → `tr_mevzuat_ara` + `tr_kurum_karari_ara`; çekemediğinde "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".
- **Halka açık hedef:** önemli nitelikte işlem usulü ve ayrılma hakkı (6362 m. 23-24), yönetim kontrolü edinilirse pay alım teklifi (m. 26); KAP açıklama takvimi.
- **Yabancı unsur:** AB birleşme kontrolü `eu_search_eu_law(query="Council Regulation 139/2004 control of concentrations")`; diğer ülkeler için `uk_`, `de_`, `nl_`, `pl_`, `at_`, `ie_`, `fi_`, `es_`, `jp_`, `az_`; listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

**MAC / esaslı olumsuz değişiklik koşulu.** Tanımı sözleşmeden al — müzakere edilmiş bir metindir, standart değildir. Türk hukukunda kanuni MAC tanımı yoktur; aşırı ifa güçlüğü (TBK m. 138: öngörülemeyen olağanüstü durumda uyarlama, olmazsa dönme/fesih) ayrı bir kurumdur ve sözleşmedeki MAC klozuyla ilişkisi **tartışmalı — içtihadı kontrol et**. Sözleşme yabancı hukuka tabiyse o hukukun yorumunu araçla çek; bir olayı MAC tetikleyicisi diye işaretlemeden önce yap.

**Önemli sözleşmelerden onay çıkarımı** yapıya ve her sözleşmenin metnine bağlıdır: pay devrinde taraf değişmez (yalnız CoC), malvarlığı devrinde sözleşme devri karşı tarafın katılımını gerektirir (TBK m. 205), birleşmede külli halefiyet (TTK m. 153/1) ile devir yasağı ilişkisi tartışmalıdır. Varsayılan kural varsayma; sözleşme başına kuralı yaz.

### Mode 2: Due diligence'tan al ("kendini güncelleyen" kısım)

Üst skill kapanış öncesi eylem gerektiren bir bulgu ürettiğinde tetiklenir:
- **`diligence-issue-extraction` bulguları** — kapanış eylemi işaretli her bulgu (onay, genel kurul/YK kararı, düzenleyici bildirim, ibra, emanet, borç kapama). Yalnız "onay" değil — o skill'in Aktarımlar bölümüne bak.
- **`material-contract-schedule` CoC / devir kalemleri** ve onay takip tablosu.
- **`deal-team-summary` çıktısı** — üst düzey brifing, tek tek notların gözden kaçırdığı bir kapanış kalemini gösterebilir (ör. birden çok yönetici sözleşmesinden toplanan CoC ikramiye ibraları, birleşik onay paketi). Klasördeki en son brifingi oku, kapanış kalemlerini listeyle uzlaştır; listede olmayanı ekle.

Aktarım şeması (anahtarlar İngilizce kalır):

```yaml
handoff:
  # Zorunlu
  item: "[Karşı taraf ya da eylem, tek satır]"
  category: "[Third-party consents | Shareholder / board action | Regulatory filing | Release / termination | Escrow / holdback | Closing deliverable]"
  source: "[Sözleşme adı / kanun maddesi / VDR yolu]"
  blocking: true  # sözleşmede önemlilik kaydı yoksa
  severity: "[🔴 / 🟠 / 🟡 / 🟢 — üst skill'den taşınır; CLAUDE.md'deki severity floor kuralı]"

  # Karşı taraf işlemi
  counterparty: "[ör. Delta Lojistik A.Ş.]"
  guarantor: "[ör. alıcı ana şirket garantisi gerekli | Yok]"
  conditions: "[karşı tarafın koştuğu şart — ör. 'onay, alıcı ana şirketin yeni garantisiyle yürürlüğe girer']"
  notice_deadline: "[ör. kapanıştan 30 gün önce | belirli tarih]"

  # Şirket işlemi
  approval_body: "[Genel kurul | Ortaklar genel kurulu | YK | Müdürler | Düzenleyici]"
  approval_threshold: "[ör. Ltd. pay devri onayı: temsil edilen oyların salt çoğunluğu, sözleşmede aksi yoksa]"
  statutory_or_charter_source: "[ör. TTK m. 595/2, 620; Şirket sözleşmesi m. 8]"

  # Zamanlama
  estimated_time_to_complete: "[ör. 30 gün]"
  must_occur_before: "[ör. kapanış | imza | Rekabet izni]"
```

Üst skill'in doldurduğu her alanı koru. "Delta onayı gerekli; yeni garanti şartı ve 30 gün bildirim" listede üç unsuruyla görünür, "Delta CoC onayı"na indirgenmez. Ciddiyeti taşı (CLAUDE.md severity floor kuralı). Tekilleştirmeyi serbest metin adına göre değil (karşı taraf + eylem türü) çiftine göre yap — Delta onayı ile Delta ibrası ayrı kalemlerdir. Birleştirirken üzerine yazma, alanları birleştir.

### Mode 3: Durum güncellemesi

Kullanıcı (ya da dataroom-watcher ajanı) güncelleme verir; kalemi bul, `status` ve `last_updated`'i güncelle.

```
/corporate-legal:closing-checklist
CP-002: [Karşı taraf] cevap verdi, onay formu ekte, karşı imza gerekiyor
```

### Mode 4: Ne engelliyor

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

> Bu rapor satın alma sözleşmesi, due diligence bulguları ve iç işlem kayıtlarından türetilmiştir ve onların gizlilik statüsünü devralır. Dağıtım listesini (karşı taraf, geniş iş ekipleri) göndermeden önce teyit et.

## Kapanış Durumu — [işlem kodu] — [tarih]

**Hedef kapanış:** [tarih] ([N] gün)
**Kalemler:** [N] toplam — [N] tamam, [N] sürüyor, [N] başlanmadı

### 🔴 Engelleyici ve riskte
| ID | Kalem | Son gün | Durum | Kalan gün |
|---|---|---|---|---|
| [CP-XXX] | [kalem] | [tarih] | [durum] | **[N]** |

### 🟡 Engelleyici, yolunda
[aynı tablo]

### ✅ Tamamlanan
[N] kalem — [kısa liste]

### Engelleyici değil (kapanış sonrası, bilgi)
[N] kalem

**Kritik yol:** [kayarsa kapanış tarihini iten kalem(ler)]
```

## Kritik yol

Her engelleyici eşit değildir: 30 günde alınan onay kritik yoldadır; 2 günde çıkan sicil kaydı değildir, ikisi de engelleyici olsa bile. Her engelleyici için tamamlanma süresini tahmin et; `(son gün − bugün) < tahmini süre` olanlar riskte, her raporun en üstünde. Noter, sicil ve TTSG ilan sürelerini ve resmî/dini tatilleri tahmine kat.

Liste yaklaşık 10 kalemi aşarsa ya da istenirse panoyu öner (`## Outputs → Dashboard offer for data-heavy outputs`): duruma göre sayılar (tamam / sürüyor / başlanmadı / riskte), iş akışına göre kritik yol, kalem-sorumlu-son gün-kalan gün tablosu.

## dataroom-watcher ajanı

Ajan listeyi günlük kontrol eder, bağlıysa e-posta/Slack'ten durum güncellemelerini çeker ve "ne engelliyor" raporunu işlem kanalına gönderir. Mode 4 ajanın çıktısıdır.

## Sonuçlu eylem kapısı (kapanışı teyit)

**"Kapanışa hazır / tüm ön koşullar sağlandı" teyidi ya da kapanış notu üretmeden önce** CLAUDE.md `## Who's using this` oku. Rol **avukat değilse**:

> Ön koşulların sağlandığını teyit etmenin hukuki sonucu var — para akışını ve kapanış sonrası yükümlülükleri bu sinyal başlatır. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet:
> - Durumuyla tam ön koşul listesi (tamam, sürüyor, başlanmadı)
> - Tamamlanma delili zayıf ya da eksik kalemler
> - Zamanında kapanmayacak kalemler için gereken feragat ya da yan mektuplar
> - Açık sorular (bekleyen onaylar, MAC / beyanların kapanışta yinelenmesi riski)
> - Avukata sorulacaklar (kapanmış sayılabilir mi; atlanmaması gereken koşul var mı; istisna ekine ne girmeli)
>
> Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan nihai "kapanışa hazır" teyidi üretme. Durum takibi ve "ne engelliyor" raporları kapı gerektirmez.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu rapora göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Onay almaz, bildirim yapmaz, belge taslaklamaz; yapılması gerektiğini izler.
- Neyin engelleyici olduğuna karar vermez — onu satın alma sözleşmesi söyler; bu skill sözleşmeyi okur.
- İşlemi kapatmaz; ne zaman kapatabileceğinizi söyler.

---

## /corporate-legal:cold-start-interview

---
name: cold-start-interview
description: >
  Kurumsal pratiğin ilk kurulum görüşmesi ya da `--new-deal` ile işleme özgü bağlam.
  Modülerdir: hangi alanların canlı olduğunu belirler (M&A, Yönetim Kurulu ve Sekretarya,
  Halka Açık Şirket, Şirket Yönetimi) ve yalnız etkin modüllerin sorularını sorup profil
  dosyasına yalnız ilgili bölümleri yazar. Türk pratiğine göre kurulur: büro / şirket içi,
  şirket türü (AŞ, Ltd., halka açık AŞ, yabancı şirket şubesi), grup yapısı, YK karar ve
  GK tutanak formatı, elden dolaştırma emsalleri, şirket uyum takvimi. Yeni kurulumda,
  CLAUDE.md'de hâlâ [PLACEHOLDER] varsa, yeni bir işlem başlarken ya da bağlantıları
  yeniden kontrol etmek veya bir modülü tazelemek için kullan.
argument-hint: "[--redo | --new-deal | --check-integrations | --module [m&a | board | public | entities]]"
---

# /cold-start-interview

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasına bak. `--new-deal` ise doğrudan işlem kurulumuna geç. `--check-integrations` ise görüşme yapma; yalnız Bölüm 0'daki bağlantı kontrolünü yap ve `## Available integrations` tablosunu yeniden yaz — ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse; yapılandırılmış ama denenmemiş bağlantı ⚪ ve tek satır teyit yolu. `.mcp.json` beyanına bakarak ✓ verme.
2. Görüşmeyi yürüt (önce Bölüm 0 — rol ve bağlantılar — sonra modüller).
3. Seed belgeler: etkin modüle göre (M&A: talep listesi + önceki bulgu raporu; Board: YK kararları ve GK tutanakları; Entities: şirket listesi/organizasyon şeması).
4. Çıkar: kategoriler, önemlilik eşikleri, rapor formatı, karar/tutanak formatı, YZ aracı ayarı.
5. **Taşıma:** eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/corporate-legal/*/CLAUDE.md`) `[PLACEHOLDER]` içermeyen bir CLAUDE.md varsa ve ayar yolunda yoksa ayar yoluna kopyala; neyin taşındığını söyle.
6. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` yaz (üst klasörleri oluştur). `--new-deal` için `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` yaz.

**Bölüm ve anahtar adlarını çevirme.** `## Company profile`, `## Who's using this`, `## Available integrations`, `## Outputs`, `## M&A`, `## Board & Secretary`, `## Public Company`, `## Entity Management`, `## Matter workspaces`, `*Active modules:*`, `**Practice setting:**`, `**Escalation:**`, `**Minutes template:**`, `**Consents repository:**`, `**Consent format:**`, `deal-context.md`, `compliance-tracker.yaml`, `closing-checklist.yaml` adları aynen kalır; diğer skill'ler bunları birebir okur. İçerik Türkçe yazılır.

## Kurulum durumu

- Dosya **yok** → görüşmeye başla.
- **`<!-- SETUP PAUSED AT: -->` var** → selamla, o bölümden devam öner.
- **`[PLACEHOLDER]` var, duraklatma notu yok** → baştan ya da yer tutucuların başladığı yerden devam öner.
- **Dolu** → `--redo` ya da `--module [ad]` yoksa çalıştırma.

Bölüm iskeleti `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonundadır. Bayraklar: `--redo` (tam yeniden görüşme), `--module [m&a | board | public | entities]` (tek modül ekle/tazele), `--new-deal` (yalnız işlem bağlamı; M&A modülü), `--full` (hızlı kurulumu genişlet).

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/company-profile.md` varsa oku ve tek satırla teyit et: "Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu? ('güncelle' derseniz ortak profili değiştiririm.)" Teyitte ortak soruları (pratik ortamı, ad, sektör, ne sattığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri) atla. Yoksa ilk kurulan eklenti budur: bu soruları sor, paketteki `knowledge/company-profile.md` şablonuna göre yaz, söyle: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak." Modül soruları eklentiye özeldir.

**Kurulum kapsamı:** çalışma klasörü ev dizini değil bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden belge okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

> **`corporate-legal`**, M&A işlemleri, yönetim kurulu ve genel kurul işleri, halka açık şirket uyumu ve grup şirketlerinin yönetimiyle uğraşanlar içindir.
>
> **2 dakika:** rol, pratik ortamı, şirket türü ve modül seçimi; önemlilik eşiği, bulgu raporu, YK karar formatı ve açıklama listesi için çalışan varsayılanlar. **15 dakika:** gerçek önemlilik eşikleriniz, örnek kararlardan ev formatınız, şirket listeniz ve uyum takviminiz, işlem ekibi bilgilendirme sıklığı, eskalasyon matrisi.
>
> Hızlı mı, tam mı? (Sonra `/corporate-legal:cold-start-interview --full` ile genişletebilirsiniz.)

Seçimi bekle. **Hızlı yol:** yalnız Bölüm 0 ve modül seçimi; diğer her alana `[DEFAULT]`. Kapanış: "Tamam, komutları kullanabilirsiniz. Önemlilik eşiği, açıklama listesi ve karar formatında makul varsayımlar kullandım; bir çıktı yanlış gelirse çoğunlukla ayarlanacak bir varsayımdır ve çıktı hangisi olduğunu söyler. Tam görüşme `--full`, tek bölüm `--redo <bölüm>`."

**Seçimden sonra** tek paragraf: "Bu eklenti profilinizi (önemlilik eşikleri, karar ve tutanak formatı), işlem klasörlerini (inceleme tabloları, kapanış listesi, açıklama listeleri) ve şirket uyum takvimini tutar. Cevaplarınızı her skill'in okuduğu düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve açıkça paylaştığınız belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** Şirket tanıtımı, yetki devri/iç yönerge, imza sirküleri, organizasyon şeması, esas sözleşme için önce belge iste: "Yapıştırın, dosya yolu verin ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular sayılır); ekranı kaydırmadan cevaplanmalı.
- **Uzun cevapta bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, yol verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim." Seed belge atlanırsa çıktılar genel şablonla gelir; bunu söyle.
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste — özellikle etkin modüllerin seed belgeleri]. Şimdi mi, yer tutucu mu?" Sessiz boşluk bırakma.
- **Duraklat/devam:** "dur" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /corporate-legal:cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte: "Hoş geldiniz, [bölüm]de kalmıştınız. Devam mı, baştan mı?" Cevaplanmış soruyu tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre, nisap, eşik söylenirse `tr_mevzuat_madde_getir` ile çek ve karşılaştır; çelişirse: "[X] dediniz; madde metni [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnekler: "Sirküler YK kararı oybirliği ister" — m. 390/4 en az üye tam sayısının çoğunluğunun yazılı onayını yeterli sayar; esas sözleşmede farklı hüküm varsa ayrıca not et. "Limited şirkette olağan GK'yı yıl içinde istediğimiz zaman yaparız" — hesap döneminin sona ermesinden itibaren üç ay içinde yapılır (m. 617/1). Değişen tutar ve eşikleri (bağımsız denetim eşikleri, Rekabet Kurulu izin eşikleri, idari para cezaları) profile sabit yazma: "güncel eşiği teyit et — dönemsel güncellenir".

## Bölüm 0 — Kim kullanıyor, ne bağlı, pratik ortamı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her rapor, karar ve tutanak taslağındaki üst başlığı belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan** (stajyer avukat, hukuk operasyonu, şirket sekreteryası)
> 2. **Avukata erişimi olan, avukat olmayan** (kurucu, CFO, yatırım ekibi, şirket sekreteri)
> 3. **Düzenli avukat erişimi olmayan**

2 ya da 3 ise bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları hüküm değil, avukatla konuşmanız için araştırma olarak çerçevelerim; (2) hukuki sonucu olan adımlardan önce (kararı imzaya sunma, tutanağı kesinleştirme, sicile başvuru, imza/kapanış) avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım. Bu bir feragat metni değil; doğru anda birkaç saatlik avukat görüşü genellikle hatadan ucuzdur." 3 ise ekle: "Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür, koşullarını baroya sorun."

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantıyı karıştırma.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_mevzuat_madde_getir(number="6102", madde_no="390")`. Cevap geldiyse ✓.
- **Tüzel kişi/LEI (`gleif_`)** — yabancı ana şirket ya da bağlı şirket varsa: `gleif_autocomplete` ile dene.
- **Yabancı ülke araçları** (`uk_`, `de_`, `nl_`, `eu_` …) — yalnız yabancı bağlı şirket varsa; önce `status`.
- **Veri odası (Intralinks, Datasite, Box), YK portalı, belge deposu, takvim, Slack** — deneyebiliyorsan dene; deneyemiyorsan ⚪.

Raporla: ✓ bağlı (denendi) · ⚪ yapılandırılmış, doğrulanmadı — MCP ayarlarından teyit edin · ✗ yok — [özellik] [manuel yönteme] düşer, nasıl bağlanır (ör. "Box bağlı değil. Cowork: Ayarlar → Bağlayıcılar → Box. Claude Code: `/mcp`. Belgeleri yapıştırarak da çalışır."), sonra `--check-integrations`. "Hepsine gerek yok; çekirdek özellikler dosya erişimiyle çalışır." ArthurLegal MCP ✗ ise: "Her madde ve karar atfı 'doğrulanmadı' işaretlenir ve UYARI satırı taşır."

### Pratik ortamı

> Hangisi size uyuyor? (Her skill'in eskalasyon dilini belirler.)
> - **Hukuk bürosu (müvekkil şirketlere kurumsal danışmanlık)** — onay zinciri değil danışma tetikleri sorarım.
> - **Şirket içi hukuk** — eskalasyon matrisi, hukuk müşaviri/genel müdür, ne zaman YK'ya gider.
> - **Tek avukat / küçük büro** — "dış avukata ya da meslektaşa ne zaman danışırsınız".
> - **Kamu / klinik** — denetim modeli ve imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla yazın; kutuya zorlamam, doldurulan/uyarlanan/boş bırakılan alanları işaretlerim.

Dallanma ve kayıt (`## Company profile` altında `**Practice setting:**`):
- **Büro (her tür):** `## Matter workspaces` → `Enabled: ✓`, `Cross-matter context: off`. `**Escalation:**` satırı onay seviyeleri değil danışma tetikleridir. Profile **çıkar çatışması notu** yaz: aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat ve kendi düzenlediği senet veya sözleşmenin hükümsüzlüğünü ileri sürmek durumunda kalan avukat işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Kurumsal işte tipik risk: aynı aile şirketinde pay sahipleri arası uyuşmazlık, büronun daha önce hazırladığı esas sözleşme ya da pay devri sözleşmesine karşı geçersizlik iddiası. Her yeni matter'da kontrolün yapıldığını sor.
- **Şirket içi:** `Enabled: ✗` (tek müvekkil; matter katmanı görünmez). `**Escalation:**` onay zinciridir.
- **Kamu / klinik:** işi kim gözden geçirir, imza zinciri.

**Hemen yaz:** `## Who's using this`, `## Available integrations` ve `## Outputs` bölümlerini profilin ilk bölümünden hemen sonra yaz.

## Bölüm 0.5 — Modül seçimi

> Hangileri düzenli işiniz? (Profilde hangi bölümlerin kurulacağını ve hangi skill'lerin açılacağını belirler; yalnız M&A seçerseniz diğer görüşmeler atlanır.)
> 1. **M&A** — pay/şirket alımı-satımı, yatırım, birleşme, bölünme, iş kolu devri
> 2. **Board & Secretary** — YK toplantı hazırlığı, YK kararları, GK tutanakları, elden dolaştırma kararları, komiteler
> 3. **Public Company** — halka açık ortaklık: KAP açıklamaları, SPK finansal raporlama, kurumsal yönetim
> 4. **Entity Management** — grup şirketleri, şirket uyum takvimi, pay defteri, tescil-ilan
>
> Numaraları söyleyin. Sonra `--module [ad]` ile ekleyebilirsiniz.

Etkin modülleri profilin başındaki `*Active modules:*` satırına yaz; yalnız onların bölümüne geç.

## Bölüm 1 — Şirket profili (her zaman, 2 dk)

Önce: "Yetki devri iç yönergesi (m. 367), imza sirküleri, onay matrisi ya da önceki bir kurumsal yönetim notu var mı? Paylaşırsanız onay seviyelerini ve eskalasyonu oradan çıkarırım." Varsa oku, bulduğunu teyit et, ilgili soruları atla.

Yoksa:
- **Ne iş yapıyor?** Web sitesi, faaliyet raporu ya da KAP sayfası bağlantısı yeter; ya da tek cümle: ne satıyor, kime, nasıl.
- **Kim?** Ticaret unvanı ([ŞİRKET ADI]), şirket türü (AŞ / Ltd. / halka açık AŞ / yabancı şirket şubesi), sicil müdürlüğü, sektör ve düzenleyici (BDDK, EPDK, SPK, BTK, Rekabet), hesap dönemi.
- **Grup:** ana şirket ve bağlı şirketler; yabancı ana şirket varsa LEI'yi `gleif_search_entities` / `gleif_get_group_structure` ile teyit et; aile şirketi mi, kurumsal yatırımcı var mı, pay sahipleri sözleşmesi var mı.
- **Hukuk ekibi:** yalnız siz mi, ekip mi?
- **Eskalasyon:** "Bir inceleme yetkinizi aşan bir şey bulduğunda — yeni bir bulgu, önemlilik kararı, menfaat çatışmalı YK kararı, açıklama listesinde takdir gerektiren kalem — kime gider? İsim ya da rol (hukuk müşaviri, yönetici ortak, işlem lideri) ya da 'kendim karar veririm'." (Bunu `/corporate-legal:diligence-issue-extraction`, `/corporate-legal:material-contract-schedule`, `/corporate-legal:written-consent` ve diğerleri kullanır.)

Yetki belgesi yüklenmediyse sonunda öner: "Bunları paylaşılabilir ayrı bir yetki ve eskalasyon notu olarak da yazayım mı?" `## Company profile`'a yaz.

## Bölüm 2M — M&A (etkinse, 4-6 dk)

- **Duruş:** alıcı, satıcı, ikisi? (Ev varsayılanıdır; işlemdeki taraf `--new-deal`'de belirlenir.) Seri alıcı mısınız, her işlem baştan mı? İşlemi kim yürütür — kurumsal gelişim, hukuk, dış büro?
- **İnceleme yapısı:** önce "Standart talep listeniz ya da kapanmış bir işlemin bulgu raporu var mı?" Varsa kategori yapısını, önemlilik eşiklerini, ciddiyet ölçeğini, bulgu biçimini, muhatabı çıkar. Yoksa sor: talep listesi işleve mi belge türüne mi göre; sözleşme incelemesinde önemlilik eşiği (tümü mü, [tutar ve para birimi] üstü mü, gelire göre ilk N mi) — bunu `/corporate-legal:diligence-issue-extraction` ve `/corporate-legal:material-contract-schedule` kullanır; veri odası; YZ toplu inceleme aracı (Luminance, Kira vb.) ve güven düzeyi.
- **Türk pratiği soruları:** pay devri mi malvarlığı devri mi tercih; Rekabet Kurulu izni değerlendirmesini kim yapar (eşikleri profile sabit yazma; `tr_kurum_karari_ara` ile Rekabet kararlarına bakılabilir); yabancı yatırımcı taraf oluyor mu.
- **Satıcı tarafı (varsa):** veri odasına neyin gireceğine kim karar verir; alıcının bulacaklarını öngören bir açıklama notu hazırlanıyor mu; iş tarafında kimle koordine edilir. Satıcı tarafı, alıcı tarafının tersi değildir: gelen belge incelemesi değil, dışarı giden bilginin yönetimidir.
- **Kapanış ve bilgilendirme:** kapanış listesi nerede (Excel, `closing-checklist.yaml`, işlem aracı), kim günceller; işlem ekibi ne sıklıkla, hangi kanaldan bilgilendirilir; iş tarafı neyi gerçekten okur.

Seed belge yoksa öner: "Söylediklerinize göre başlangıç talep listesi ve bulgu raporu iskeleti yazayım mı?" `## M&A`'ya yaz.

## Bölüm 2B — Board & Secretary (etkinse, 3-4 dk)

- **Rol:** YK sekreteri, hukuk müşaviri, dış büro olarak karar hazırlayan?
- **Organlar:** YK üye sayısı ve yapısı (tüzel kişi üye ve adına tescilli gerçek kişi, m. 359/2; halka açıksa bağımsız üyeler); komiteler (denetimden sorumlu, riskin erken saptanması, kurumsal yönetim, diğer); Ltd. ise müdürler ve müdürler kurulu başkanı (m. 624/1).
- **Takvim:** yılda kaç YK toplantısı, hangi aylar; olağan GK genellikle hangi ay (son sınır dönem sonundan itibaren 3 ay, m. 409/1).
- **Araçlar:** YK portalı ya da e-posta; elektronik toplantı/oy esas sözleşmede öngörülmüş mü (m. 1527/1); GK iç yönergesi tescilli mi (m. 419/2).
- **Defterler:** YK karar defteri ve GK toplantı ve müzakere defteri fiziki mi, elektronik mi (m. 64/3-4); kim tutar?
- **Tutanak/karar biçimi:** uzun anlatı, yalnız karar, karma? Ne kadar sürede yazılır, nasıl onaylanır (dolaştırma, sonraki toplantı)?
- **Elden dolaştırma:** rutin olarak hangi işler için (imza yetkisi, banka, müdür atama, GK çağrısı)? Toplantı şartı koyan esas sözleşme hükmü ya da iç kural var mı?

**Seed kararlar ve tutanaklar (board-minutes için gerekli):**

> Kapanmış toplantılardan 5-6 YK kararı ve en az bir GK tutanağı yükleyin; komite tutanağınız varsa onu da. Bunlar ev formatınızı öğretir: başlık, katılım ve nisap kaydı, tartışma derinliği, karar dili, ek numaralandırma, imza blokları. Şimdi yoksa sonra `--module board` ile eklenir; board-minutes eksikse ister.

Çıkar ve `## Board & Secretary` → `**Minutes template:**` bloğuna yaz: yapı ve sıra; başlık; katılım/nisap kaydı; tartışma derinliği; karar dili ("... kabulüne", "... onaylanmasına karar verildi"); ek atfı; imza bloğu; her tutanakta tekrarlanan kalıp cümleler.

**Emsal kararlar deposu (written-consent için gerekli):**

> İmzalanmış elden dolaştırma kararlarının durduğu bir klasör var mı? (written-consent en yakın emsali orada arar.) Varsa yolunu söyleyin. Yoksa 3-5 örnek karar yükleyin; biçimi öğrenirim, emsal araması depo kurulunca açılır.

Çıkar: karar dili, gerekçe yapısı, yetkilendirme kalıbı, onay/imza bloğu, deftere geçirme notu. `**Consents repository:**` ve `**Consent format:**` satırlarına yaz.

**Yıllık döngü:** olağan GK gündemi (finansal tablolar, faaliyet raporu, ibra, YK seçimi ve ücretler, kâr dağıtımı, denetçi seçimi — m. 409/1, 408/2), YK görev süresi bitişleri (m. 362/1), bağlılık raporu (m. 199/1). `## Board & Secretary`'ye yaz.

## Bölüm 2P — Public Company (etkinse, 3-4 dk)

- Borsa İstanbul pazarı; hesap dönemi; ara dönem finansal rapor takvimi (SerPK m. 14 çerçevesinde SPK düzenlemesine göre — tarihleri SPK düzenlemesinden teyit et).
- **Özel durum açıklamaları (SerPK m. 15):** KAP açıklamasını kim hazırlar, kim onaylar; erteleme kararı süreci; hukuk ne zaman devreye girer.
- **Kurumsal yönetim (SerPK m. 17):** bağımsız üyeler, komiteler, ilişkili taraf işlemlerinde bağımsız üye onayı süreci (m. 17/3).
- **İçeriden bilgi ve işlem yasakları:** içsel bilgiye erişenler listesi, yönetici işlem bildirimleri, kapalı dönemler — ilgili SPK düzenlemesini `tr_kurum_karari_ara` (spk) ve `tr_spk_bulten_icinde_ara` ile teyit et; kuralı profile ezberden yazma.
- **GK:** çağrı en az üç hafta önce internet sitesi ve KAP ile (SerPK m. 29/1); elektronik GK.

`## Public Company`'ye yaz.

## Bölüm 2E — Entity Management (etkinse, 2-3 dk)

> Organizasyon şeması ya da şirket listesi varsa (kaba bir tablo da olur) yükleyin; unvanları, türleri, ülkeleri, pay oranlarını ve faaliyetsiz şirketleri çıkarırım. (entity-compliance uyum takvimini bu listeden kurar.)

Yükleme yoksa sor: kaç aktif şirket; ülkeler (yalnız Türkiye mi); her şirketin türü ve sicil müdürlüğü, MERSİS numarası; hesap dönemi; bağımsız denetime tabi mi (eşikler Cumhurbaşkanı kararıyla belirlenir, m. 397/4 — güncel eşiği teyit et); defterler fiziki mi elektronik mi; pay defterini kim tutar (m. 499, 594); rutin işleri kim yürütür (mali müşavir, şirket içi, dış büro); yurt dışı şirketlerde yerel ajan; şube varsa ticari mümessil (m. 40/4); grup içi sözleşmeler (hizmet, lisans, borç).

`## Entity Management`'a şirket tablosuyla yaz: | Unvan | Tür | Ülke/sicil | MERSİS | Pay sahibi ve oran | Hesap dönemi | Denetim | Durum |.

## Profili yazma — Outputs

`## Outputs` üst başlığı role göre:
- Rol avukatsa: `GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ` (avukatın görevi dolayısıyla öğrendiklerini açığa vurma yasağı, Av. K. m. 36).
- Rol avukat değilse: `ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — İŞLEM ÖNCESİ AVUKATLA GÖZDEN GEÇİRİN`
Sicile, deftere ya da karşı tarafa gidecek karar, tutanak ve açıklama listelerinden başlık çıkarılır. Başlık tek başına koruma yaratmaz.

## Yazdıktan sonra

> **Neler yapabildiğimi görmek ister misiniz?** Veri odasından bulgu çıkarma (`/corporate-legal:diligence-issue-extraction`), önemli sözleşmeler listesi (`/corporate-legal:material-contract-schedule`), elden dolaştırma kararı (`/corporate-legal:written-consent`), YK kararı ve GK tutanağı (`/corporate-legal:board-minutes`), şirket uyum takvimi (`/corporate-legal:entity-compliance`), kapanış listesi (`/corporate-legal:closing-checklist`), kapanış sonrası entegrasyon (`/corporate-legal:integration-management`). **Önerim:** canlı işlem varsa `/corporate-legal:closing-checklist`; yoksa yaklaşan olağan GK için `/corporate-legal:entity-compliance --report`.

Kullanıcı somut bir iş söylediyse listeyi atla. Sonra etkin modülleri ve kontrol edilecekleri göster: zayıf/belirsiz cevaplar; M&A etkin ve seed yoksa "talep listesi ve bulgu raporunu gönderince bölümü güncellerim"; M&A etkinse "yeni işlemde `--new-deal`"; Board etkinse written-consent ve board-minutes hazır; Entities etkinse `/corporate-legal:entity-compliance --init`; Public etkinse "bu modülün skill'leri sonraki sürümde; profil bölümü hazır". ArthurLegal MCP bağlı değilse: "Bağlarsanız madde atıflarını canlı doğrularım."

**Kapanış:**
> "Profiliniz `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasında — düz metin, doğrudan düzenleyebilirsiniz. Tam yeniden görüşme `--redo`, tek modül `--module [m&a | board | public | entities]`, bağlantı kontrolü `--check-integrations`, tek değişiklik `/corporate-legal:customize`. En sık ayarlananlar: M&A önemlilik eşikleri, açıklama listesi ve bulgu raporu biçimi, şirket takvimi sıklığı.
>
> **Profiliniz öğrenir.** Bir çıktı yanlış gelirse çoğunlukla ayarlanacak bir duruştur; çıktı hangisi olduğunu söyler. On dakikalık kurulum çalışan bir profil verir; bir aylık kullanım sizin yazmış gibi okunan bir profil."

## İşlem kurulumu (`--new-deal`, yalnız M&A)

Ev yaklaşımı profilde kalır; yalnız işleme özgü bağlamı sor: işlem kod adı · bu işlemdeki taraf (alıcı/satıcı) · hedef ya da alıcı · işlem yapısı (pay devri, malvarlığı devri, birleşme, sermaye artırımıyla giriş) · veri odası yeri · işlem lideri · imza ve kapanış tarihleri · işleme özgü eşik farkı · dış büro ve sorumlu avukat · Rekabet Kurulu izni ya da sektör düzenleyicisi onayı gerekiyor mu (değerlendirme avukatta; eşik yazma) · büroda çatışma kontrolü yapıldı mı. `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code-name]/deal-context.md` yaz. Skill'ler profili (ev) ve `deal-context.md`'yi (işlem) okur; çelişkide `deal-context.md` önce gelir. Matter çalışma alanı açıksa ilgili matter'ın `matter.md`'sine deal kodunu yaz.

## Profil kalite kontrolü ve kaçınılacaklar

Bitirmeden yazılanı yeniden oku: yer tutucu kalan bölüm (sor), seed belgesi olmayan etkin modül (not et), `*Active modules:*` satırı tam mı.

- **Tüm modülleri etkin varsayma;** önce sor.
- **Alıcı tarafını sabitleme;** ev profili taraftan bağımsız, taraf `--new-deal`'de.
- **Genel yer tutucu yazma;** "standart eşikler" denirse sayıyı ve para birimini iste.
- **Satıcı tarafı alıcı tarafının tersi değildir;** satıcı tarafı etkinse bu ayrımı işaretle.
- **Etkin olmayan modül için seed isteme.**
- Var olmayan skill vaat etme; profil doluysa her oturumda çalıştırma.

---

## /corporate-legal:customize

---
name: customize
description: >
  Kurumsal pratik profilinde tek bir şeyi, kurulum görüşmesini baştan yapmadan
  değiştirir: risk iştahı, eskalasyon kişileri, etkin modüller (M&A / Yönetim Kurulu ve
  Sekretarya / Halka Açık Şirket / Şirket Yönetimi), önemlilik eşikleri, açıklama listesi
  biçimi, YK karar ve GK tutanak formatı, elden dolaştırma emsalleri, şirket tablosu ve
  uyum takvimi, matter klasörleri. Kullanıcı "şunu değiştir", "profilimi güncelle",
  "ayarı değiştir" ya da "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değiştirmek istediğiniz şey]"
---

# /customize

## Ne yapar

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` ve bir üst düzeydeki ortak `~/.claude/plugins/config/claude-for-legal/company-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa: "Kurulum henüz yapılmamış. Önce `/corporate-legal:cold-start-interview` çalıştırın — customize var olan profili ayarlamak içindir."

2. **Haritayı göster** — her grup için güncel değerin tek satırlık özeti:
   - **Şirket / kimlik** — ad, sektör, ülkeler, şirket türü, halka açık mı, pratik ortamı *(ortak profil — tüm eklentilere yansır)*
   - **Active modules** — M&A, Board & Secretary, Public Company, Entity Management hangileri açık; açıp kapatmak hangi skill'in kurulum isteyeceğini değiştirir
   - **Risk iştahı** — temkinli / orta / atak; inceleme önemliliğine ve açıklama listesi kapsamına etkisi
   - **Kişiler** — işlem ekibi, YK sekreteri, şirket uyumu sorumlusu, mali müşavir, eskalasyon zinciri (`**Escalation:**`)
   - **M&A** — önemlilik eşikleri (sözleşme bedeli, çalışan sayısı, gelir; para birimiyle), güvenilen veri odaları, YZ toplu inceleme güven düzeyi (Luminance / Kira), işlem ekibi bilgilendirme sıklığı
   - **Board & Secretary** — `**Minutes template:**`, `**Consents repository:**`, `**Consent format:**`, karar defteri türü (fiziki / elektronik), komiteler, elden dolaştırma kapsamı
   - **Public Company** — KAP açıklama süreci, SPK finansal raporlama takvimi, kurumsal yönetim komiteleri
   - **Entity Management** — şirket tablosu, mali müşavir / yerel ajan, ülkeler, `compliance-tracker.yaml` rapor sıklığı
   - **İş akışı** — matter klasörleri, `closing-checklist.yaml` yeri, dataroom-watcher sıklığı
   - **Entegrasyonlar** — ArthurLegal MCP, `gleif_`, Box / Intralinks / Datasite, takvim, Slack ve geri dönüş yolları

3. **Sor:** "Neyi ayarlamak istersiniz? Bir bölüm seçin ya da değişikliği kendi sözlerinizle anlatın."

4. **Değiştir:** güncel değeri göster, yenisini al, aşağı akış etkisini söyle, onay al, yaz. Örnekler:
   - *Önemlilik eşiği 5 milyon TL → 10 milyon TL:* "`/diligence-issue-extraction` ve `/material-contract-schedule` artık 10 milyon TL'yi eşik alır; kayıtlı bulgular olduğu gibi kalır, geriye dönük uygulamak için yeniden çalıştırın."
   - *Public Company modülünü açma:* "O alanda bir şey çalıştırdığınızda KAP süreci ve SPK takvimini sorarım."
   - *YZ toplu inceleme güveni "her satırı kontrol et" → "%10 örneklem":* "`/ai-tool-handoff` artık çıkarımların %10'unu kontrol eder."
   - *Karar defteri fiziki → elektronik:* "entity-compliance YK karar defteri kapanış onayı kalemini takvimden düşürür (elektronik defterde açılış ve kapanış onayı aranmaz, TTK m. 64/3); written-consent onayların deftere geçirilmesini e-defter pratiğine göre not eder."

   Kullanıcı yeni bir kanun maddesi, nisap, süre ya da eşik söylerse yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; çelişki varsa göster ve hangisinin gireceğini sor. Dönemsel değişen eşikleri (bağımsız denetim eşikleri, Rekabet Kurulu izin eşikleri, idari para cezaları) sabit yazma.

5. **Ortak profil değişikliği** (ad, sektör, ülkeler, pratik ortamı, şirket türü): `company-profile.md` dosyasına yaz ve söyle: "Bu değişiklik tüm eklentileri etkiler." Pratik ortamı büro ↔ şirket içi değişiyorsa `## Matter workspaces` → `Enabled` değerinin de değişmesi gerektiğini hatırlat.

6. **Kapat:** "Tamam, bir sonraki çıktı değişikliği yansıtır. Başka bir şey var mı? `/corporate-legal:customize` her zaman çalışır."

## Korkuluklar

- **Bölüm silme.** "Kaldır" denirse `[Not configured]` yaz ve eklentinin davranışına etkisini anlat.
- **İç tutarsızlığı işaretle** — ör. Public Company modülü kapalı ama şirket halka açık; "atak" risk iştahı + çok düşük önemlilik eşiği; Ltd. şirket için GK'da Bakanlık temsilcisi adımı (Ltd.'de uygulanmaz, TTK m. 617/3); "sirküler karar oybirliğiyle" ev kuralı ile kanunun çoğunluk kuralı (m. 390/4) — ev kuralı esas sözleşmeden geliyorsa kaynağını yaz. Gerilimi göster, hangisini istediğini sor.
- **Korkuluk zayıflatmayı işaretle.** `[review]` bayrağı, üst başlık, kaynak etiketleri ve doğrulanmamış atıflardaki UYARI satırı yük taşır; kapatılmak istenirse neyi koruduğunu anlat ve bedeli anladığını teyit ettir.
- **Bölüm ve anahtar adlarını çevirme** — diğer skill'ler `## Board & Secretary`, `## Entity Management`, `*Active modules:*` gibi adları birebir okur.
- **Tek seferde tek değişiklik** — görüşmeyi baştan sorma.

---

## /corporate-legal:deal-team-summary

---
name: deal-team-summary
description: >
  Due diligence bulgularını okuyucuya uygun yükseklikte bir işlem ekibi
  brifingine toplar — yönetim/YK için yönetici özeti, işlem lideri için açık
  sorunlar ve kararlar, çalışma ekibi için tam ayrıntı. "İşlem ekibini
  bilgilendir", "due diligence ne durumda", "[kitle] için bulguları özetle",
  "işlem güncellemesi" denildiğinde ya da brifing takviminde kullan.
---

# /deal-team-summary — İşlem Ekibi Brifingi

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

İşlem lideri 200 bulgu okumaz; önemli olanı, son brifingten beri değişeni ve karar bekleyeni okur. Bu skill due diligence çıktısını okuyucunun seviyesine sıkıştırır.

## Bağlam

- `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## M&A` işlem ekibi bilgilendirmesi (`Deal team briefing`: takvim, kanal, iş tarafının ne okuduğu)
- `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` → işlem lideri, takvim, işlem yapısı; `company-profile.md` → sorumlu ortak, müvekkil bilgisi
- `diligence-issue-extraction` çıktısındaki güncel bulgular; varsa `closing-checklist.yaml` (kapanış kalemlerinin durumu)

## Kitle katmanları

CLAUDE.md'deki "iş tarafı neyi okur, ne dosya için" ayrımına göre; yoksa varsayılan:

| Kitle | Alır | Almaz |
|---|---|---|
| **YK / yönetici sponsor** ([ŞİRKET ADI] tarafı) | En önemli 3-5 sorun, bedel/yapı etkisi, karar kalemleri | Kategori ayrıntısı, yeşil bulgular, süreç |
| **İşlem lideri** (sorumlu ortak) | Tüm kırmızı ve sarılar, ilerleme, kararlar, sonraki adımlar | Yeşil bulgu ayrıntısı |
| **Çalışma ekibi** | Her şey — tam bulgular, kategori durumu, boşluklar | Hiçbir şey saklanmaz |

Belli değilse hangi katman olduğunu sor.

**Dağıtım.** Brifing gizli due diligence bulgularını toplar ve onların gizlilik statüsünü devralır. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD tipi geniş bir belge koruması ("privilege") değildir; avukatı bağlar, müvekkilin geniş iş ekiplerine ya da danışmanlarına dağıtılan brifing gizliliğini fiilen kaybeder. Göndermeden önce dağıtım listesinin işlem ekibiyle örtüştüğünü teyit et; YK katmanı için ayrı, arındırılmış sürüm öner. Aile şirketinde paydaşlar arasında çıkar ayrılığı varsa (profildeki `Aile çatışması` notu) brifingin kime gittiğini sorumlu ortağa sor.

## Brifing

### Yönetici katmanı

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

# [işlem kodu] — Due Diligence Brifingi — [tarih]

**Durum:** [Yolunda / Sorunlar belirlendi / Önemli bulgular]
**Kapsam:** VDR'nin %[X]'i incelendi
**İşlem yapısı:** [pay devri / malvarlığı devri / birleşme]

## Önemli bulgular
[En çok 3-5. Her biri tek paragraf: ne, işlem için neden önemli, ne yapıyoruz.]

## Gereken kararlar
- [ ] [Somut karar — bedel düzeltmesi, tazmin/emanet talebi, işlemden çekilme eşiği] — [kim karar verir] — [ne zamana kadar]

## Son brifingten beri
[Değişenler: yeni bulgular, çözülenler, kapsam ilerlemesi.]
```

### İşlem lideri katmanı

Yukarıdakine ek olarak:

```markdown
## Kategoriye göre açık sorunlar
### 🔴 Kırmızı
[Bulgu başlığı + tek satır — tam bulguya bağlantı]
### 🟡 Sarı
[aynı]

## İlerleme
| Kategori | İncelenen | Kapsam | Kırmızı | Sarı | Durum |
|---|---|---|---|---|---|
| [ad] | [N/M] | [%] | [N] | [N] | [Tamam / Sürüyor / Engelli] |

## Kapanış yolu
[Rekabet izni, pay devri onayları, kritik karşı taraf onayları — closing-checklist Mode 4'ten kritik yol]

## Boşluklar ve takip
- [Bekleyen ek talep kalemleri]
- [Yönetime sorular]

## Önümüzdeki 72 saat
[Ne inceleniyor, hangi görüşmeler planlı]
```

### Çalışma ekibi katmanı

Tam bulgu ayrıntısı: aynı yapı, ama her bulgu tek satır yerine büro formatındaki tam bloğuyla (dayanak etiketleri ve tartışmalı notlar dahil).

## Farklar

Brifing tekrarlayan ise (CLAUDE.md takvimi) değişenle başla: son brifingten beri yeni bulgular, ciddiyeti yükselen/düşenler, çözülenler (onay alındı, sorun açıklandı), kapsam hareketi. İşlem liderleri durumdan çok harekete bakar: "hâlâ 12 sarı" yerine "2 yeni sarı, 3 çözüldü".

## Kaynak disiplini

Brifing yeni hukuki tespit üretmez; bulgulardaki etiketleri (`[ArthurLegal TR — 6102 m. X — GG.AA.YYYY]`, `[kullanıcı verdi]`, `[model bilgisi — doğrula]`) taşır, silmez. Yönetici katmanında madde numarasını sadeleştirebilirsin ama `doğrula` etiketli bir dayanağa dayanan bulguyu "doğrulanmadı" notuyla ver. Tartışmalı işaretli noktalar (ör. birleşmede devir yasağının uygulanması) karar kalemi olarak görünür, kesin sonuç gibi değil.

## Aktarımlar

- **diligence-issue-extraction'dan:** biriken bulgular okunur.
- **closing-checklist'e:** kapanış koşuluna dönüşen her "gereken karar" kalemi listeye gider (closing-checklist Mode 2 son brifingi okur).

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu brifinge göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Önemlilik kararı vermez — çıkarım sırasında verilen kararları raporlar.
- Ekibin bulguyla ne yapacağına karar vermez — kararı görünür kılar.
- Brifingi dağıtmaz — taslaklar, insan gönderir.

---

## /corporate-legal:diligence-issue-extraction

---
name: diligence-issue-extraction
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

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`, `company-profile.md` ve `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` yükle (çakışmada deal-context.md önce gelir). [ŞİRKET ADI] alıcı mı satıcı mı — deal-context.md'den al; satıcı tarafında amaç alıcının bulacaklarını önceden görmek ve açıklama notunu beslemektir.
2. Kategori yüksek hacimliyse ve araç tanımlıysa önce `ai-tool-handoff`'a bak.
3. Belgeleri oku, önemlilik süzgecini uygula, kategoriye göre çıkar.
4. Bulguları büro formatında yaz; kapanış öncesi eylem gerektirenleri closing-checklist'e aktar.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

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

**Kişisel veri.** VDR'de çalışan dosyaları, bordro ya da müşteri listeleri varsa: kişisel veri ancak kanuni usule ve ilkelere (hukuka uygunluk, belirli amaç, amaçla bağlantılı, sınırlı ve ölçülü olma) uygun işlenir (KVKK m. 4); açık rıza dışındaki işleme şartları m. 5/2'de sayılıdır; aktarım m. 8'e, VDR sunucusu ya da alıcı ekibi yurt dışındaysa m. 9'a tabidir. Hangi şarta dayanılacağı olaya bağlıdır — burada karar verme; maskeleme ya da anonim özet iste, `/privacy-legal:use-case-triage` veya `/privacy-legal:pia-generation`'a yönlendir. Bulgu metnine gereksiz kişisel veri (TCKN, sağlık bilgisi, kişi bazlı ücret) taşıma.

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
- **Uygulanacak hukuk / uyuşmazlık çözümü:** yabancı hukuk, yabancı mahkeme ya da yabancı tahkim yeri → tanıma-tenfiz (MÖHUK, New York Sözleşmesi) etkisi; analiz `/commercial-legal:governing-law-review`'da. Yabancı kural ezberden yazılmaz: `uk_search_legislation`, `de_gesetz_ara` / `de_norm_getir`, `eu_search_eu_law`, `nl_`, `pl_`, `at_`, `ie_`, `fi_`, `es_`, `jp_`, `az_`; ABD için yalnız kuruluysa CourtListener (`references/courtlistener-rehberi.md`); listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

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
- Sahiplik zinciri (kurucu, çalışan, yüklenici devirleri). Sınai mülkiyet hakkının devri yazılı ve noter onaylı olmalı; sicile kaydedilmeyen işlemden doğan haklar iyiniyetli üçüncü kişilere karşı ileri sürülemez (SMK m. 148/4-5). Telif (yazılım dahil) için FSEK'teki devir şekil şartlarını `tr_mevzuat_madde_getir(number="5846", ...)` ile çek; ayrıntı `/ip-legal:ip-clause-review`.
- Üründe açık kaynak (copyleft) → `/ip-legal:oss-review`. Kilit hak lisanslı mı, sahip olunan mı; lisansta devir/CoC.
- TÜRKPATENT sicil durumu: ArthurLegal'da TÜRKPATENT aracı yok — kaydı kurumun kendi sisteminden teyit ettir. Bekleyen ya da tehdit edilen uyuşmazlıklar.

**İş hukuku:**
- Kontrol değişikliğine bağlı ikramiye/tazminat (yönetici sözleşmeleri) ve maliyeti; kilit çalışan kaybı; rekabet yasağı geçerliliği → `/employment-legal:hiring-review`.
- Yapıya göre devir sonuçları (yukarıdaki tablo). Devreden ya da devralan, iş sözleşmesini sırf işyeri devri nedeniyle feshedemez (İş K. m. 6/5).
- Bekleyen işçilik davaları, kıdem karşılıkları, SGK prim borcu, alt işveren/muvazaa, işçi görünümlü yükleniciler → `/employment-legal:worker-classification`.

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

## /corporate-legal:entity-compliance

---
name: entity-compliance
description: >
  Şirket uyum takvimi — kurulum, yaklaşan son günler raporu, durum güncelleme, sağlık
  denetimi, CSV dışa aktarma. Şirket tablosundan compliance-tracker.yaml kurar;
  her şirket ve ülke için TTK takvimini hesaplar: olağan genel kurul (m. 409/1, 617/1),
  finansal tablolar ve faaliyet raporu (m. 514), defter açılış/kapanış onayları (m. 64/3),
  denetçi seçimi (m. 399), bağlılık raporu (m. 199), YK görev süresi (m. 362), tescil ve
  ilan, pay edinim bildirimleri (m. 198); 30/60/90 gün içinde ne var gösterir. Yabancı
  bağlı şirketler için ArthurLegal MCP araçlarına yönlendirir. Kullanıcı "şirket uyumu",
  "genel kurul takvimi", "defter onayı ne zaman", "tescil son günleri", "şirket
  takibi", "entity compliance", "good standing" dediğinde kullan.
argument-hint: "[--init | --report [--days N] | --update [--from-report] | --sweep | --audit | --export [--format csv|table]]"
---

# /entity-compliance

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## Entity Management` yükle (şirket tablosu, ülkeler, mali müşavir / yerel sicil ajanı).
2. Bayrağa göre mod: bayraksız ya da `--init` → Mod 1 · `--report` → Mod 2 · `--update` → Mod 3a, `--update --from-report` → 3b · `--sweep` → 3c · `--audit` → Mod 4 · `--export` → Mod 5.
3. `~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml` dosyasını oku/yaz.
4. Her güncellemeden sonra değişiklik özetini ve sıradaki eylemi göster.

## Amaç

Olağan genel kurul, finansal tablolar, defter onayları, denetçi seçimi, tescil ve ilan — her şirketin kendi takvimi ve kaçırmanın kendi sonucu var. Bu skill tek bir YAML takip dosyası tutar: hangi şirkette ne, ne zaman. Dosya sizindir; Claude komutla günceller, paylaşmak gerektiğinde dışa aktarırsınız.

## Önemli: son gün uyarısı

> Aşağıdaki süreler TTK'nın canlı çekilmiş metnine dayanır, ancak esas sözleşme, özel hesap dönemi, sektör mevzuatı (banka, sigorta, enerji, halka açık) ve ikincil düzenlemeler takvimi değiştirebilir. **Son günleri mali müşavirinizin takvimi, ticaret sicili müdürlüğü ve MERSİS kaydıyla teyit edin.** Vergi ve SGK beyannameleri bu takipte yoktur; mali müşavir takviminden izlenir. İdari para cezası tutarları her yıl güncellenir; tutarı takip dosyasına sabit yazma.

## Şirket türü ayrımı — takvim türe göre değişir

Takvim yalnız ülkeye değil **şirket türüne** bağlıdır; bir türün son gününü diğerine kopyalama. Şirket tablosunda tür yoksa `type_unknown` işaretle ve sor.

| Konu | AŞ | Ltd. | Halka açık AŞ |
|---|---|---|---|
| Olağan GK | Faaliyet dönemi sonundan itibaren 3 ay (m. 409/1) | Hesap dönemi sonundan itibaren 3 ay (m. 617/1) | AŞ gibi + SerPK |
| GK çağrısı | İlan (internet sitesi + TTSG) + iadeli taahhütlü; en az 2 hafta (m. 414/1) | En az 15 gün; sözleşmeyle 10 güne inebilir (m. 617/2) | İnternet sitesi + KAP; en az 3 hafta (SerPK m. 29/1) |
| Bakanlık temsilcisi | Gündeme göre zorunlu olabilir (m. 407/3; Yönetmelik m. 32) | Uygulanmaz (m. 617/3) | Elektronik GK uygulayanlarda zorunlu (Yönetmelik m. 32/1-b) |
| Yönetim organı süresi | YK üyeleri en çok 3 yıl için seçilir (m. 362/1) | Yönetim ve temsil şirket sözleşmesiyle düzenlenir (m. 623/1); süreyi sözleşmeden al | AŞ gibi + bağımsız üye kuralları (SerPK m. 17/1) |
| Pay defteri | m. 499 | m. 594 | MKK kaydı saklı (m. 499/5) |
| Bağımsız denetim | Cumhurbaşkanınca belirlenen şirketler (m. 397/4) | AŞ hükümleri uygulanır (m. 635) | SerPK m. 14/3 |
| İnternet sitesi | Yalnız denetime tabi olanlar (m. 1524/1, 1524/6) | Aynı | Aynı + KAP |

**Bağımsız denetim eşikleri** Cumhurbaşkanı kararıyla belirlenir ve değişir; eşik yazma. **Güncel eşikleri teyit et:** `tr_mevzuat_ara(query="bağımsız denetime tabi olacak şirketler", types=["CB_KARAR"])` ve dönen kararın son değişikliklerine bak.

**Yabancı şirketin Türkiye şubesi:** yerli işletme gibi tescil edilir ve Türkiye'de yerleşik tam yetkili bir ticari mümessil atanır (m. 40/4) — takipte `registered_agent` alanına mümessili yaz.

## Ülke varsayımı

Takip, her şirket için kayıtlı kuruluş ülkesine göre hesaplar. Gerçek ayak izi farklıysa (bildirilmemiş şube, tasfiye hâlindeki şirket, merkez nakli, yerel ajanın yönettiği yurt dışı şirket) çıktı aynen uygulanmayabilir.

**Yabancı bağlı şirket ve ana şirket:** kural ezberden yazılmaz; yerel ajan/hukukçu teyidi esastır. Araçla neyi arayacağın:
- Grup yapısı ve LEI: `gleif_search_entities(name="[tam unvan]", jurisdiction="DE")` → `gleif_get_group_structure(lei="[LEI]")` (konsolidasyon esaslı; sözleşmeyle kontrol görünmez).
- Birleşik Krallık: `uk_search_legislation(title="Companies Act 2006", text="confirmation statement")`.
- Almanya: `de_norm_getir(kanun="HGB", norm="325")` (yıllık hesapların açıklanması — teyit et), GmbH için `de_norm_getir(kanun="GmbHG", norm="[madde]")`.
- Hollanda: `nl_search_legislation(query="Burgerlijk Wetboek Boek 2")`. AB düzeyi: `eu_search_eu_law(query="Directive (EU) 2017/1132 company law")`.
- Azerbaycan, İrlanda, Polonya, Avusturya, İspanya, Finlandiya, Japonya: `az_`, `ie_`, `pl_`, `at_`, `es_`, `fi_`, `jp_` araçları.
- Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu ya da yerel sicil ajanı görüşü alın."
- **ABD bağlı ortaklığı (karşılaştırmalı not):** eyalet ve tür (corporation / LLC / LP) ayrımı takvimi ve vergiyi değiştirir; registered agent takvimi esastır. ArthurLegal'da ABD eyalet şirket sicili kaynağı yok.

## Takip dosyası

`~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml` — anahtarlar İngilizce kalır (diğer skill'ler birebir okur), değerler Türkçe olabilir:

```yaml
# Entity Compliance Tracker
# Generated: [tarih] · Last updated: [tarih]
# Disclaimer: son günler referanstır — mali müşavir, ticaret sicili ve MERSİS ile teyit edin

metadata:
  company: "[ŞİRKET ADI]"
  generated: "[tarih]"
  last_updated: "[tarih]"
  last_audit: "[tarih ya da null]"

custom_jurisdictions:   # yerleşik tabloda olmayan ülkeler — elle eklenir
  []

entities:
  - name: "[Ticaret unvanı]"
    type: "[AŞ / Ltd. / halka açık AŞ / yabancı şirket şubesi / GmbH / Ltd (UK) / diğer]"
    state_of_formation: "[ülke — sicil müdürlüğü, ör. TR — İstanbul]"
    formation_date: "[tarih ya da null]"
    status: "[active / dormant / dissolving]"
    registered_agent: "[mali müşavir / şirket içi / ticari mümessil (m. 40/4) / yerel ajan]"
    mersis_no: "[MERSİS numarası ya da null]"
    fiscal_year_end: "[MM-DD — çoğunlukla 12-31; özel hesap dönemi varsa onu yaz]"
    audit_required: "[yes / no / unknown — m. 397/4 eşiklerine göre]"
    board_term_ends: "[YK üyeleri / müdürlerin görev süresi bitişi]"
    notes: ""
    jurisdictions:
      - state: "[ülke / sicil müdürlüğü]"
        qualification: "[domestic / foreign — şube]"
        qualified_date: "[tescil tarihi ya da null]"
        agent_managed: false   # yurt dışında yerel ajan yönetiyorsa true
        local_agent: "[ad ya da null]"
        filings:
          - type: "[aşağıdaki listeden]"
            due_date: "[YYYY-MM-DD]"
            due_basis: "[fixed: MM-DD / fiscal-year-end + 3 ay / olay + N gün / görev süresi sonu]"
            last_filed: "[tarih ya da null]"
            last_fee: "[tutar ya da null]"
            status: "[current / due_soon / overdue / unknown]"
            confirmed_good_standing: "[sicil tasdiknamesi / faaliyet belgesi tarihi ya da null]"
            notes: ""
```

Durum değerleri: `current` (dönem için yapıldı, 90 gün içinde iş yok) · `due_soon` (90 gün içinde) · `overdue` (son gün geçti, yapıldı kaydı yok) · `unknown` (bilgi yok; teyit gerekir).

**Türkiye takvimi — `filings.type` listesi** (hesap dönemi 31.12 ise örnek tarih):

| Kalem | Kural | Örnek son gün |
|---|---|---|
| Yevmiye ve diğer fiziki defterlerin açılış onayı | Kullanılacağı dönemin ilk ayından önceki ayın sonuna kadar noter; pay defteri ile GK toplantı ve müzakere defteri yaprak yeterliyse onaysız devam eder (m. 64/3) | 31.12 |
| YK karar defteri kapanış onayı (fiziki) | İzleyen faaliyet döneminin birinci ayının sonuna kadar (m. 64/3) | 31.01 |
| Yevmiye defteri kapanış onayı (fiziki) | İzleyen faaliyet döneminin altıncı ayının sonuna kadar (m. 64/3) | 30.06 |
| Elektronik defter | Açılışta ve yevmiye ile YK karar defterinin kapanışında noter/sicil onayı aranmaz (m. 64/3); e-defter takvimini mali müşavirle teyit et | — |
| Finansal tablolar + YK yıllık faaliyet raporu | Bilanço gününü izleyen dönemin ilk üç ayı içinde hazırlanır ve GK'ya sunulur (m. 514); denetime tabi şirkette denetlenmemiş tablo düzenlenmemiş hükmündedir (m. 397/2) | 31.03 |
| Bağlılık raporu (grup şirketi) | Bağlı şirketin YK'sı faaliyet yılının ilk üç ayı içinde düzenler (m. 199/1) | 31.03 |
| GK belgelerinin incelemeye açılması | Toplantıdan en az 15 gün önce (m. 437/1) | GK − 15 gün |
| Olağan GK | Dönem sonundan itibaren 3 ay (m. 409/1, 617/1) | 31.03 |
| GK tutanağı tescil ve ilanı | Noter onaylı suret derhâl sicile; internet sitesine hemen (m. 422/2) | GK + derhâl |
| Denetçi seçimi ve tescili | Denetleyeceği faaliyet dönemi bitmeden seçilir; YK gecikmeksizin tescil ve ilan ettirir (m. 399/1); dördüncü aya kadar seçilmezse istem üzerine mahkeme atar (m. 399/6) | Dönem içinde; en geç 4. ay |
| YK / müdür görev süresi | YK en çok 3 yıl (m. 362/1); boşalan üyelik ilk GK onayına (m. 363/1) | Seçim + süre |
| Temsil yetkisi değişikliği | Noter onaylı karar sureti tescil ve ilan için sicile (m. 373/1) | Karar + derhâl |
| Pay edinim/elden çıkarma bildirimi (grup) | %5, 10, 20, 25, 33, 50, 67, 100 eşiklerinde işlemin tamamlanmasını izleyen 10 gün içinde şirkete ve makamlara; bildirim tescil ve ilan olunur; yapılmazsa oy dâhil haklar donar (m. 198/1-2; TSY m. 107/5-6). Yönetmelikte yükümlülük, payı edinen teşebbüsün bir şirketler topluluğuna dâhil olmasına bağlanmıştır (TSY m. 107/2) | İşlem + 10 gün |
| İnternet sitesi (denetime tabi) | Tescilden itibaren 3 ay içinde açılır; kanunda ayrı süre yoksa içerik en geç 5 gün içinde konur ve en az 6 ay kalır (m. 1524/1, 1524/5) | — |
| Tescil edilmiş olguda değişiklik | Her türlü değişiklik tescil edilir (TSY m. 29/1); ilan edilmeyen husus üçüncü kişiye ancak bildiği ispatlanırsa ileri sürülür (m. 36/4). Gecikmede sicil müdürlüğü 30 gün süreli davet ve idari para cezası yoluna gider (TSY m. 36/1, 36/3; m. 33/2) | Değişiklik + kanuni süre (teyit et) |
| Belgelerin saklanması | Defterler, finansal tablolar, faaliyet raporları ve dayanak belgeler 10 yıl (m. 82/5) | — |
| Halka açık | Finansal raporlar (SerPK m. 14), özel durum açıklamaları (m. 15), kurumsal yönetim (m. 17) — SPK düzenleme takvimini `tr_kurum_karari_ara` (spk) ve `tr_spk_bulten_icinde_ara` ile kontrol et | SPK takvimi |
| VERBİS kaydı | Kişisel veri işleyen gerçek ve tüzel kişiler işlemeye başlamadan önce Veri Sorumluları Siciline kaydolur; Kurul objektif kriterlerle istisna getirebilir; bildirilen bilgilerdeki değişiklik derhâl bildirilir (KVKK m. 16/2, 16/4). İstisna kapsamını `tr_kurum_karari_ara` (kvkk) ile teyit et | Değişiklik + derhâl |

## Mod 1 — Kurulum

Takip dosyası yoksa ya da `--rebuild` ile.

**Adım 1 — Şirket tablosunu yükle:** `## Entity Management` → şirket tablosu. Boşsa `/corporate-legal:cold-start-interview --module entities` öner ya da listeyi iste.

**Adım 2 — Her şirket × ülke için yükümlülükleri teyit et.** Önbellekteki takvime güvenme.
1. Mali müşavirin ya da yerel ajanın güncel takvimi var mı? En güvenilir kaynak odur.
2. Yoksa kullanıcının bildiklerini sor: hesap dönemi, denetime tabi mi, defter fiziki mi elektronik mi, son GK tarihi, YK seçim tarihi, denetçi.
3. Bilinmeyeni `unknown` yap; tarih uydurma.

Yerleşik tabloda olmayan ülke için:

> [Ülke] için takvimim yok; şimdi kaydedelim. [Şirket] için: 1. Hangi yıllık yükümlülük (yıllık bildirim, hesapların yayımı, genel kurul)? 2. Son gün nasıl hesaplanır (sabit tarih, kuruluş ayı, hesap dönemi + N ay)? 3. Tipik ücret (yaklaşık ya da "bilinmiyor")? 4. Orada işi kim yürütüyor?

Cevabı `custom_jurisdictions` bloğuna yaz (`jurisdiction`, `jurisdiction_type`, `filings` [`type`, `due_basis`, `typical_fee`, `notes`], `added_by: "manual"`, `added_date`); o ülkedeki tüm şirketlere uygulanır. Yurt dışı şirkette sor: yerel ajan var mı (`agent_managed: true` + `local_agent`), grup düzeyinde raporlama (gerçek faydalanıcı sicili, ülke bazlı raporlama) var mı. Kuruluş ayına bağlı yükümlülükte `formation_date` yoksa `unknown`.

**Adım 3 — Yaz ve özetle:**

```
Şirket uyum takibi kuruldu.
Şirket: [N] · Ülke/sicil: [N] · İzlenen kalem: [N]
  ✅ Güncel: [N]   ⏰ Yaklaşan: [N] (90 gün)   🔴 Gecikmiş: [N]   ❓ Bilinmiyor: [N]
Ne var görmek için: /corporate-legal:entity-compliance --report
```

## Mod 2 — Rapor

`/corporate-legal:entity-compliance --report [--days 30|60|90|180]` (varsayılan 90).

```
ŞİRKET UYUM RAPORU — [tarih] — [ŞİRKET ADI]
🔴 GECİKMİŞ ([N]):   [Şirket] / [ülke] / [kalem] — son gün [tarih] (dayanak)
⏰ [N] GÜN İÇİNDE ([N]):   [Şirket] / [ülke] / [kalem] — son gün [tarih]  [sorumlu]
✅ SON 90 GÜNDE YAPILAN ([N]):   [Şirket] / [kalem] — [tarih]
❓ BİLİNMEYEN ([N]):   [Şirket] / [kalem] — bilgi yok; mali müşavir/sicil ile teyit
🌐 YEREL AJANDA ([N]):   [Şirket] / [ülke] — [ajan]; durumu doğrudan teyit edin
SİCİL TEYİDİ:
  Son tasdikname/faaliyet belgesi: [tarih] · 12 aydan eski: [liste]
```

Takip 10'dan fazla şirket içeriyorsa ya da istenirse pano öner (CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`): duruma göre sayılar, sicil teyidi durumu, sıralanabilir şirket tablosu.

## Mod 3 — Güncelleme

### Sonuç doğuran eylem kapısı (tescil başvurusu, defter onayı, GK)

Başvuruya yönlendirmeden ya da `last_filed` kaydetmeden önce `## Who's using this` → Role **avukat değilse**:

> Ticaret siciline tescil başvurusu, defter onayı ya da genel kurul işlemi şirketin resmî beyanıdır; yanlış veya geç işlem idari para cezası, kararın üçüncü kişilere karşı ileri sürülememesi ya da iptal riski doğurur. Avukatla (ya da mali müşavirle) gözden geçirdiniz mi? Hayırsa brif: şirket, kalem, son gün · takipteki son kayıt · açık sorular (yetkililer ve temsil şekli güncel mi, merkez/adres değişti mi, esas sözleşme değişikliği var mı) · ne ters gidebilir · sorulacaklar (bu yıl gerçekten gerekli mi, kim imzalar). Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz.

Açık "evet" olmadan yeni `last_filed` kaydetme. Okuma ve rapor kapı gerektirmez.

**3a — Elle:** "[Şirket] olağan genel kurulu 25.03'te yapıldı, tutanak 28.03'te sicile verildi." → `last_filed`, `status: current`, `metadata.last_updated`; tutanak tescili için ayrı kalem aç.

**3b — Rapordan (`--from-report`):** mali müşavir takvimi, sicil tasdiknamesi, TTSG ilanı, MERSİS çıktısı ya da yurt dışı ajan raporu (PDF, CSV, Excel). Her şirket için kalem, son gün, yapılma tarihi, sicil teyidi, uyarıları çıkar; unvana göre eşleştir, yakın eşleşmeyi sor ("ABC Holding A.Ş." / "ABC HOLDİNG ANONİM ŞİRKETİ"). Sonuç: eşleşen / raporda olup takipte olmayan / takipte olup raporda olmayan.

**3c — Tarama (`--sweep`):** `unknown` ve `overdue` kalemleri tek tek sor: "[Şirket] / [kalem] — [durum]. Yapıldı mı? Ne zaman?" Her cevaptan sonra yaz, sonda özet ver.

## Mod 4 — Sağlık denetimi (`--audit`)

- **Uyum:** gecikmiş ve bilinmeyen kalemler.
- **Faaliyetsiz şirketler:** `dormant` olanlar — tasfiye adayı mı? Taşıma maliyeti ve süren yükümlülükler (GK, defter, mali müşavir). 5 yıldan uzun süredir faaliyetsizse tasfiye adayı olarak işaretle. `formation_date` eksikse veri boşluğu.
- **Sermaye kaybı:** son yıllık bilançoda sermaye ile kanuni yedek akçeler toplamının yarısı zarar nedeniyle karşılıksız kaldıysa YK GK'yı hemen toplantıya çağırır; üçte ikisi karşılıksızsa ve GK sermayenin üçte biriyle yetinme ya da tamamlama kararı vermezse şirket kendiliğinden sona erer; borca batıklık şüphesinde ara bilanço ve gerekirse mahkemeye bildirim (m. 376). Finans verisi yoksa soruyu işaretle.
- **Yönetim organı:** görev süresi dolmuş ya da 90 gün içinde dolacak YK üyeleri/müdürler (m. 362/1); tescilli temsil yetkisi güncel mi (m. 373).
- **Denetim:** denetime tabi şirkette dönem için denetçi seçilmiş ve tescil edilmiş mi (m. 399/1, 399/6); denetçi olamayacak kişi kuralları (m. 400) için denetçinin şirkete başka hizmet verip vermediği.
- **Sicil teyidi:** tasdikname/faaliyet belgesi hiç yok ya da 12 aydan eski — işlem veya finansman öncesi yenile.
- **Grup:** pay edinim bildirimleri (m. 198) ve bağlılık raporu (m. 199) eksik mi; şirketler arası sözleşmeler (hizmet, lisans, borç) var mı; yabancı ana şirketin LEI ve grup yapısı `gleif_get_group_structure` ile tabloyla tutarlı mı.
- **Şube:** yabancı şirket şubesinde ticari mümessil tescilli mi (m. 40/4).

```
ŞİRKET SAĞLIK DENETİMİ — [tarih]
UYUM: gecikmiş [N] · bilinmeyen [N] → --sweep
FAALİYETSİZ ([N]): [liste, yaş] · tasfiye adayı: [liste]
SERMAYE KAYBI / BORCA BATIKLIK: [işaretler ya da "veri yok"]
YÖNETİM ORGANI: süresi dolan [liste] · temsil tescili eski [liste]
DENETİM: denetçi seçilmemiş/tescilsiz [liste]
SİCİL TEYİDİ: kayıt yok [N] · 12 aydan eski [N]
GRUP: bildirim/bağlılık raporu eksik [liste]
ÖNERİLEN EYLEMLER: 1. [en öncelikli] 2. [..]
```

## Mod 5 — Dışa aktarma

`/corporate-legal:entity-compliance --export [--format csv|table]` (varsayılan CSV). Sütunlar:
`Entity Name, Entity Type, State of Formation, MERSIS No, Formation Date, Status, Registered Agent, Jurisdiction, Qualification Type, Filing Type, Due Date, Last Filed, Last Fee, Good Standing Confirmed, Notes`
Her ülke × kalem bir satır. `--format table`: yalnız sonraki 90 günü gösteren markdown tablo.

**Formül enjeksiyonu savunması:** Excel/Sheets/CSV'ye yazmadan önce belge, araç sonucu ya da yapıştırmadan gelen her metin hücresinde `=`, `+`, `-`, `@`, sekme ya da satır başı ile başlayan değerin önüne tek tırnak koy (`'=SUM(A1:A10)`). CSV'de virgül, çift tırnak ve satır sonunu RFC 4180'e göre tırnakla. Kendi yazdığın başlıklar ve hesapladığın değerler güvenlidir. İsteğe bağlı değildir.

## Bu skill ne yapmaz

- Başvuru yapmaz, deftere onay almaz, genel kurul toplamaz; çıktı takip ve yapılacaklar listesidir.
- Sicil tasdiknamesi ya da faaliyet belgesi almaz; son teyit tarihini izler.
- Bir şirketin bağımsız denetime tabi olup olmadığına ya da şube açılması gerekip gerekmediğine karar vermez; olgulara bağlıdır, avukat ve mali müşavir teyit eder.
- Vergi, SGK ve sektör düzenleyicisi (BDDK, EPDK, SPK) takvimlerinin yerini tutmaz.
- Takvim tablosu hukuki görüş değildir; güncel olmayabilir. Güvenmeden önce teyit edin.

---

## /corporate-legal:integration-management

---
name: integration-management
description: >
  Kapanış sonrası M&A entegrasyon takibi — evreli iş planı, onay takibi, toplu
  sözleşme devri, haftalık durum raporu. Eldeki işlem belgelerinden (satın alma
  sözleşmesi, işlem özeti, kapanış listesi) başlar; M&A cold-start'ın
  deal-context.md ve closing-checklist.yaml dosyalarına bağlanır. Türk hukukundaki
  kapanış sonrası kalemleri (ticaret sicili tescil/ilan, pay defteri, SGK işyeri
  bildirgesi — 5510 m. 11, işyeri devri — İş K. m. 6, sözleşme devri — TBK m.
  205, SMK m. 148 sicil kaydı, birleşmede alacaklıya çağrı — TTK m. 157) iş
  planına yerleştirir. "Entegrasyon", "kapanış sonrası", "bekleyen onaylar",
  "sözleşme devri", "entegrasyon durumu", "işlemde ne kaldı" denildiğinde kullan.
argument-hint: "[--init | --contracts | --report | --update | --export [--format csv|table] [--section all|consents|contracts|workplan]] [--deal [code]]"
---

# /integration-management — Kapanış Sonrası Entegrasyon

1. `deal-context.md`'yi ve `company-profile.md`'i yükle (işlem kodu, [ŞİRKET ADI] ve hedef, kapanış tarihi, işlem lideri, işlem yapısı).
2. `integration-tracker.yaml` varsa yükle (`--init`'te oluştur).
3. Bayrağa göre: `--init` Mode 1 (iş planı + onay takibi), `--contracts` Mode 2 (sözleşme listesi, katman), `--report` Mode 3 (durum raporu), `--update` Mode 4 (güncelleme), `--export` Mode 5 (CSV/tablo).
4. `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/integration-tracker.yaml` oku/yaz.
5. Her yazmadan sonra değişiklik özetini ve yeni işaretleri göster.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

İşlem kapanır, hukuki dağınıklık kalır. Bu skill kapanış sonrası entegrasyonun hukuk iş akışını yönetir — iş entegrasyonunu, BT sistemlerini, İK organizasyonunu değil: onaylar, sözleşme devirleri, şirket yapısının sadeleştirilmesi, sınai mülkiyet sicil kayıtları, satın alma sözleşmesinden (SPA/APA) doğan yükümlülükler. Neyin bittiğini, neyin vadesinin geldiğini, neyin engelli olduğunu ve neyin karar beklediğini izler.

## Takip dosyası

`deals/[code]/integration-tracker.yaml`. `closing-checklist.yaml` varsa kapanış sonrası kalemleri devral. Anahtarlar ve durum değerleri İngilizce kalır (dışa aktarım ve diğer skill'ler okur); açıklamalar Türkçe.

```yaml
metadata:
  deal_code: "[kod]"
  target: "[unvan]"
  structure: "[share_deal_as / share_deal_ltd / asset_deal / merger / demerger]"
  close_date: "[YYYY-MM-DD]"
  deal_lead: "[ad]"
  outside_counsel: "[büro ve sorumlu avukat]"
  last_updated: "[tarih]"
  last_status_report: "[tarih ya da null]"

pa_dates:
  required_consents_deadline: "[YYYY-MM-DD — sözleşmeden]"
  rep_survival_expires: "[YYYY-MM-DD — her beyan türü ayrı]"
  escrow_release: "[YYYY-MM-DD ya da null]"
  earnout_milestones:
    - description: "[kilometre taşı]"
      measurement_date: "[YYYY-MM-DD]"
      payment_date: "[YYYY-MM-DD]"
      owner: "finance"   # her zaman finans — hukuk yalnız tarihi izler

workplan:
  day_1:   { target_date: "[close_date + 7 gün]",   items: [] }
  day_30:  { target_date: "[close_date + 30 gün]",  items: [] }
  day_90:  { target_date: "[close_date + 90 gün]",  items: [] }
  day_180: { target_date: "[close_date + 180 gün]", items: [] }

required_consents: []
desired_consents: []

contracts:
  source: "[repository / manual-upload / disclosure-schedule]"
  repository_path: "[yol ya da null]"
  last_imported: "[tarih]"
  total: 0
  tier_1: []
  tier_2: []
  tier_3: []
  tier_4: []
```

**İş planı kalemi:** `id` (W-001), `description`, `phase` (day_1/day_30/day_90/day_180), `owner` (legal-owns / legal-supports), `workstream` (legal / hr / it / finance / real-estate / other), `priority` (critical / high / medium / low), `deadline`, `deadline_basis` (pa-obligation / regulatory / best-practice), `status` (not_started / in_progress / complete / blocked / deferred), `blocker`, `depends_on`, `notes`.

**Onay kaydı:** `id` (CON-001), `counterparty`, `contract_type` (customer / vendor / lease / IP-license / financial / public / other), `required_consent` (true = sözleşmenin Gerekli Onaylar ekinde), `pa_deadline` (yalnız true için), `status` (not_started / outreach_sent / in_negotiation / obtained / waived / refused), `assigned_to`, `outreach_date`, `obtained_date`, `notes`.

**Sözleşme kaydı:** `id` (C-001), `name`, `counterparty`, `contract_type`, `annual_value` (tutar + para birimi ya da unknown), `assignment_mechanism` (auto-assign / consent-required / coc-provision / silent / not_reviewed), `tier` (1-4), `required_consent`, `pa_deadline`, `status` (not_reviewed / no_action / consent_pending / outreach_sent / in_negotiation / consent_obtained / assignment_complete / waived / refused / coc_triggered), `assigned_to`, `notes`, `last_updated`.

## Mode 1: Başlat (`--init`)

### Adım 1: İşlem bağlamı

`deals/[code]/deal-context.md`'yi oku; yoksa işlem kodu, hedef, **işlem yapısı**, kapanış tarihi, işlem lideri ve dış avukatı sor ve yaz. `closing-checklist.yaml` varsa kapanış sonrası işaretli kalemleri Day 1 ya da Day 30'a durumlarıyla al.

### Adım 2: İşlem girdileri

**Tam satın alma sözleşmesi en eksiksiz takibi üretir**: Gerekli Onaylar eki ve kapanış sonrası taahhütler kesin süre ve yükümlülüklerin kaynağıdır. Ama skill eldekiyle başlar; kısmi girdi boş sayfa yerine avukatın dolduracağı bir iskelet üretir.

> Hangi işlem belgeleri elinizde? **İdeal:** satın alma sözleşmesi — kapanış sonrası taahhütleri, Gerekli Onaylar ekini, beyanların geçerlilik sürelerini, emanet ve kazanç payı (earn-out) hükümlerini okurum. **Yararlı:** işlem özeti/term sheet, dış avukatın kapanış sonrası yapılacaklar listesi, mevcut iş planı, M&A cold-start'ın ürettiği `closing-checklist.yaml` (otomatik devralırım), yalnız Gerekli Onaylar listesi. **Hiçbiri yoksa:** kim, ne zaman devralındı, başlıca açık işler ne — sade anlatın, standart Day 1/30/90/180 iskeletini kurarım.

| Girdi | Sonuç |
|---|---|
| Tam sözleşme | Tam iş planı + süreli Gerekli Onaylar + sözleşme tarihleri |
| Sözleşme + sözleşme listesi | Tam takip + devir katman listesi |
| İşlem özeti / yapılacaklar | Standart iskelet, onaylar yer tutucu |
| Hiçbiri | Standart iskelet; onay ve sözleşmeleri avukat doldurur |

**Sözleşmeden çıkar:** Gerekli Onaylar (karşı taraf, tür, süre → `required_consent: true`), kapanış sonrası yükümlülükler (evreye yerleştir, `pa-obligation`), Gerekli Onaylar son günü, beyanların geçerlilik süreleri (genel, temel, vergi beyanları genelde farklıdır — her birini ayrı kaydet, varsayılan uydurma), emanet çözülme tarihleri, kazanç payı ölçüm ve ödeme tarihleri (`owner: finance`).

**Beyan süreleri ve zamanaşımı:** zamanaşımı süreleri sözleşmeyle değiştirilemez (TBK m. 148); sözleşmedeki tazmin bildirim/talep sürelerinin bu kuralla ilişkisi **tartışmalı — içtihadı kontrol et**. Sözleşme yabancı hukuka tabiyse o hukuka göre değerlendir. Takipte yalnız sözleşmedeki tarihleri yaz, nitelendirmeyi avukata bırak.

### Adım 3: Evreli iş planı

Standart kalemleri üret, sözleşme yükümlülüklerini ekle, kapanış listesinden gelenleri doldurulmuş al. Yapıya uymayan kalemi atla (ör. pay devrinde işyeri devri bildirimi yok).

**Day 1 — hukuk yürütür:**
- Pay defteri kaydı: AŞ'de devralan, usulüne uygun devir ispat edilince yazılır (TTK m. 499); Ltd.'de pay defteri (m. 594) ve müdürlerin tescil başvurusu (m. 598) [critical]
- YK / müdür değişikliği, temsil yetkisi, imza sirküleri: genel kurul/YK kararı, ticaret siciline tescil ve TTSG ilanı — tescil edilen husus ilanı izleyen iş gününden itibaren üçüncü kişilere karşı sonuç doğurur (TTK m. 36/1); tescili zorunlu hususta sicil müdürü davet eder, idari para cezası riski var (m. 33 — tutar yıllık güncellenir, teyit et) [critical]
- Banka imza yetkililerinin güncellenmesi: yeni imza sirküleri ve tescil/ilan suretiyle bankalara bildirim [critical]
- Unvan değişikliği (varsa): esas sözleşme değişikliği, tescil, ilan; unvan ticari belgelerde ve internet sitesinde (m. 39/2) [high]
- Kapanışta ertelenen fikrî hak devirlerinin imzası: sınai mülkiyet hakkı devri yazılı ve noter onaylı (SMK m. 148/4); telif devri için FSEK şekil şartını çek [critical]
- Alan adı ve sosyal medya hesaplarının devri [high]
- Yönetici sorumluluk sigortası: eski yöneticiler için uzatılmış bildirim/teminat süresinin bağlandığını teyit et [critical]
- MERSİS kayıtlarının güncelliği [high]

**Day 1 — hukuk destekler:**
- Çalışan duyurusu (İK yürütür, hukuk inceler). İşyeri devrinde iş sözleşmeleri hak ve borçlarıyla devralana geçer, kıdem devreden yanındaki başlangıçtan hesaplanır, devir tek başına fesih sebebi değildir (İş K. m. 6; TBK m. 428). Birleşme/bölünmede TTK m. 178 (işçinin itiraz hakkı) — ayrıntı `/employment-legal`.
- SGK: işyerinin başka işverene devrinde devralma tarihini takip eden 10 gün içinde işyeri bildirgesi; şirket birleşmesi/tür değişikliğinde tescil ilanını takip eden 10 gün (5510 m. 11 — metin hâlâ 6762 sayılı eski TTK'ya atıf yapar) (İK/muhasebe yürütür, hukuk teyit eder).
- Müşteri bildirimleri (iş birimi yürütür, hukuk doğruluğu inceler).
- Kişisel veri: veri sorumlusu değişiyorsa aydınlatma metinleri ve VERBİS kaydı → `/privacy-legal`.

**Day 30 — hukuk yürütür:**
- Gerekli Onaylar ilk dalgası: tüm karşı taraflarla temas, temas kaydı [critical]
- Sınai mülkiyet devir/lisanslarının TÜRKPATENT siciline kaydı — kaydedilmeyen işlem iyiniyetli üçüncü kişiye karşı ileri sürülemez (SMK m. 148/5). ArthurLegal'da TÜRKPATENT aracı yok; durumu kurumun sisteminden teyit et [high]
- Yabancı sicillerdeki fikrî haklar: ülkesine göre yerel avukat [medium]
- Önemli sözleşmeler: katman 1 ve 2 devir analizini bitir [high]
- Sigorta poliçelerinde sigortalı/lehtar değişikliği [high]

**Day 30 — hukuk destekler:**
- Veri taşıma: yurt dışı sunucu ya da grup içi aktarım varsa KVKK m. 9 (yeterlilik kararı, uygun güvenceler, standart sözleşmenin 5 iş günü içinde Kurula bildirimi) → `/privacy-legal:dpa-review`
- Kira sözleşmeleri: malvarlığı devrinde kira ilişkisinin devri kiraya verenin yazılı rızasına bağlı; işyerinde haklı sebep olmadıkça reddedilemez (TBK m. 323) (tesis yönetimi yürütür, hukuk danışır)

**Day 90 — hukuk yürütür:**
- Gerekli Onaylar son günü: hepsi alınmış ya da eskale edilmiş olmalı [critical, deadline: pa_dates.required_consents_deadline]
- Şirket yapısı kararı: ayrı tut / birleştir / tasfiye et / tür değiştir (birleşme TTK m. 134 vd.; tür değiştirme m. 180 vd.) [high]
- İkinci onay dalgası [high]
- Katman 3 (CoC) sözleşmelerin çözümü [critical]

**Day 90 — hukuk destekler:**
- İK uyumlaştırma (çalışma koşulu değişikliği, TİS, yan haklar) → `/employment-legal`

**Day 180 — hukuk yürütür:**
- Birleşme (karar verildiyse): yazılı birleşme sözleşmesi, genel kurul onayı ve nisaplar (TTK m. 145, 151), tescil (m. 152) — tescille aktif ve pasif devralana geçer (m. 153); alacaklılara TTSG'de yedişer gün arayla üç ilan + internet sitesi ilanı, alacaklılar 3 ay içinde teminat isteyebilir (m. 157) [high]
- Tasfiye (karar verildiyse) [high]
- Sözleşme devirleri: devralanın adına geçmesi gereken sözleşmeler — üç taraflı devir ya da karşı tarafın izni/onayı, devredilen sözleşmenin şekliyle (TBK m. 205) [high]
- Beyan sürelerinin takibi: yaklaşan bitişi not et [medium]

Özet:

```
Entegrasyon takibi başlatıldı — [işlem kodu] / [hedef] ([yapı])
Kapanış: [tarih]
Gerekli Onaylar son günü: [tarih] (bugünden [N] gün)
Beyan süreleri: [tür — tarih, ...]
İş planı kalemleri: [N] ([N] hukuk yürütür, [N] hukuk destekler)
Gerekli Onaylar: [N] (sözleşme ekinden)
İstenen onaylar: [N] (due diligence'tan — sözleşme süresi yok)
Sözleşme devri: henüz alınmadı — --contracts çalıştırın
Sonraki adım: /corporate-legal:integration-management --contracts, sonra --report
```

## Mode 2: Sözleşme devri (`--contracts`)

Ana başlatmadan ayrı çalışır; sözleşme listesi değiştikçe yeniden çalıştırılır.

### Adım 1: Sözleşme listesi

- **Yol A — bağlı depo** (Drive, Box, SharePoint ya da kapanış sonrası erişilebilen VDR): klasörü al; her belge için dosya adı ve yolu, karşı taraf, sözleşme türü, devir klozu metni, varsa CoC klozu metni, belirtilmişse yıllık bedel.
- **Yol B — liste yükleme:** sözleşmenin Önemli Sözleşmeler eki, sözleşme yönetim sistemi dökümü (CSV/Excel) ya da elle hazırlanmış liste. Asgari sütunlar: Sözleşme adı, Karşı taraf. Devir klozu metni yoksa `assignment_mechanism: not_reviewed` ve takip işareti.
- **Yol C — açıklama eki:** hiçbiri yoksa `--init`'te yüklenen sözleşmenin Önemli Sözleşmeler ekinden asgari liste; devir klozları elle incelenir.

### Adım 2: Devir mekanizması

| Mekanizma | Tanım | Katman |
|---|---|---|
| `consent-required` | Karşı taraf onayı olmadan devri yasaklayan açık kloz | 1 ya da 2 |
| `coc-provision` | İşlemle tetiklenen, karşı tarafa fesih ya da onay hakkı veren kontrol değişikliği klozu | 3 |
| `auto-assign` | Sınırlama yok ya da bağlı şirkete/halefe devre açık izin | 4 |
| `silent` | Devir hükmü yok — sonuç yapıya bağlı (aşağıya bak); avukat incelemesine işaretle | 2 |
| `not_reviewed` | Devir klozu okunamadı/bulunamadı | Elle inceleme |

**`silent` sözleşmede Türk hukuku varsayılanı (sözleşme Türk hukukuna tabiyse):** alacak, kanun, sözleşme ya da işin niteliği engel olmadıkça borçlunun rızası aranmadan devredilebilir (TBK m. 183) — ama sözleşmenin, yani taraf sıfatının devri karşı tarafın katılımını ya da önceden izni/sonradan onayını gerektirir (TBK m. 205). Bu yüzden malvarlığı devrinde sessiz sözleşme de onay ister. Pay devrinde taraf değişmez, devir gerekmez. Birleşmede tescille külli halefiyet doğar (TTK m. 153/1); sözleşmedeki devir yasağının buna uygulanması **tartışmalı**. Yabancı hukuka tabi sözleşmede varsayılanı araçla çek (`uk_`, `de_`, `eu_` …) ya da yerel avukata işaretle. Özel rejimler: kira (TBK m. 323), kamu ihale sözleşmesi (4735 m. 16 — izinsiz devirde fesih).

Sözleşmenin Gerekli Onaylar ekindeki sözleşmeler mekanizmadan bağımsız katman 1'dir.

### Adım 3: Katmanlar

```
Katman 1 — Gerekli Onaylar: [N]   Sözleşme ekinde, kesin süre [tarih], onay şart
Katman 2 — Önemli, onay gerekli: [N]   Devir sınırlaması var, ekte değil; Day 90 içinde al
Katman 3 — Kontrol değişikliği: [N] ⚠️   Kapanışla tetiklenmiş olabilir — karşı tarafla HEMEN temas
Katman 4 — Kendiliğinden / işlem yok: [N]   Yalnız takip
İncelenmedi: [N]   Mekanizma belirlenemedi — elle inceleme
```

Katman 3'ü ayrı ve belirgin göster: CoC kapanış gününde tetiklenmiş olabilir; karşı tarafın fesih hakkı şu anda işliyor olabilir. Karşı taraf fesih ya da dönme ihbarı gönderirse tacirler arasında şeklini kontrol et (noter, taahhütlü mektup, telgraf ya da güvenli e-imzalı KEP — TTK m. 18/3).

### Adım 4: Kayıtlar

Her sözleşme için tüm alanlarla kayıt. Başlangıç durumu: katman 4 → `no_action`; katman 3 → `coc_triggered`; katman 1/2 → `consent_pending`; incelenmeyen → `not_reviewed`. Katman 1'de `pa_deadline` Gerekli Onaylar ekinden.

## Mode 3: Durum raporu (`--report`)

Takibin güncel hâlini okur:

```
[ÜST BAŞLIK — CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

> Bu rapor satın alma sözleşmesi, due diligence bulguları ve entegrasyon kayıtlarından türetilmiştir ve onların gizlilik statüsünü devralır. Alıcı listesini göndermeden önce teyit et.

ENTEGRASYON DURUMU — [işlem kodu] / [hedef]
[Tarih] — Kapanıştan sonra [N]. gün
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YÖNETİCİ ÖZETİ
[2-3 cümle: genel durum, en büyük risk, son rapordan beri kazanım]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GEREKLİ ONAYLAR  [son gün: TARİH — N gün kaldı]
  Alındı: [N]/[toplam] ████████░░ [%]   Müzakerede: [N]   Temas edildi: [N]
  Başlanmadı: [N]   Reddedildi: [N] ⚠️
⚠️ RİSKTE: [karşı taraf] — son güne [N] gün, temasa cevap yok
⚠️ REDDEDİLDİ: [karşı taraf] — sözleşme yükümlülüğü karşılanmadı; dış avukata eskale et
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SÖZLEŞME DEVRİ
  Katman 1: [N] tamam / [N] sürüyor / [N] bekliyor
  Katman 2: [N] tamam / [N] sürüyor / [N] bekliyor
  Katman 3 (CoC): [N] çözüldü / [N] açık ⚠️
  Katman 4: [N] — işlem gerekmez
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
İŞ PLANI — HUKUK YÜRÜTÜR
  🔴 GECİKMİŞ ([N]): [kalem] — son gün [tarih]
  ⏰ BU HAFTA ([N]): [kalem] — [tarih]
  ✅ SON RAPORDAN BERİ TAMAMLANAN ([N]): [kalem] — [tarih]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENGELLER VE KARARLAR
  [kalem] — engel: [açıklama] — sorumlu: [ad]
  [kalem] — karar gerekli: [açıklama] — öneri: [seçenek]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YAKLAŞAN TARİHLER
  [tarih] — [kilometre taşı / son gün]
  [tarih] — Beyan süresi doluyor — bekleyen tazmin talebi olmadığını teyit et
```

## Mode 4: Güncelleme (`--update`)

**Elle:** avukat neyin değiştiğini söyler.
> "[Karşı taraf] onayı geldi; alındı yap, sorumlu [ad], tarih bugün."
> "Şirket yapısı kararı birleşme; durumu güncelle, birleşme tescilini Day 180'e ekle."
> "[Karşı taraf] onayı reddetti; işaretle, bunun tazmin talebi doğurup doğurmadığı için dış avukat gerektiğini not et."

İlgili kaydı güncelle, bağımlı durumları yeniden hesapla (ör. tüm katman 1 onayları alındıysa sözleşme yükümlülüğünü karşılandı işaretle), değişeni göster.

**Yükleme:** iş akışı sahibinin ya da dış avukatın durum belgesini oku; kalemleri karşı taraf adına ya da iş planı açıklamasına göre eşle; eşleşmeyen kalemi yeni kalem adayı olarak işaretle.

```
[N] kalem güncellendi.
Değişiklikler:
  CON-003 [Karşı taraf]: not_started → obtained
  W-014 Şirket yapısı kararı: in_progress → complete
Yeni işaretler:
  CON-007 [Karşı taraf]: refused — sözleşme yükümlülüğü karşılanmamış olabilir; tazmin talebi için dış avukat incelemesi ⚠️
```

## Mode 5: Dışa aktarım (`--export`)

```
/corporate-legal:integration-management --export [--format csv|table] [--section all|consents|contracts|workplan]
```

Düz CSV ya da markdown tablo; varsayılan tüm bölümler, CSV. Satır başına bir kalem, `section` sütunu bölümü gösterir.
- *Workplan:* id, phase, description, owner, workstream, priority, deadline, status, blocker
- *Consents:* id, counterparty, contract_type, required_consent, pa_deadline, status, assigned_to, obtained_date, notes
- *Contracts:* id, name, counterparty, contract_type, annual_value, assignment_mechanism, tier, required_consent, pa_deadline, status, assigned_to, notes

Paylaşılabilir format budur (dış avukat, kurumsal gelişim, YK entegrasyon güncellemesi) — ama gizlilik statüsünü devralır; alıcıyı teyit et.

## Formül enjeksiyonu savunması

Excel, Sheets ya da CSV'ye hücre yazmadan önce: karşı taraftan gelen metin (sözleşme alıntısı, taraf adı, sicil verisi, CLM dökümü) saldırgan kontrolündedir. `=`, `+`, `-`, `@`, sekme, satır başı ya da satır sonuyla başlayan hücrenin başına tek tırnak koy (`'=SUM(A1:A10)` metin olarak görünür, çalışmaz). Belgeden, araç sonucundan ya da kullanıcı yapıştırmasından gelen her metin hücresine uygulanır; senin kontrol ettiğin başlıklar ve hesapladığın değerler güvenlidir. CSV'de virgül, çift tırnak ve satır sonlarını RFC 4180'e göre tırnakla. Bu isteğe bağlı değildir.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu çıktıya göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- İş entegrasyonu akışlarını (BT, İK, finans, gayrimenkul) yönetmez; hukukun temas noktalarını izler, hukuk görüşü gerektiğinde işaretler. Sahiplik iş biriminde kalır.
- Onay talep yazılarını ya da sözleşme devir anlaşmalarını taslaklamaz — dış avukat ya da ilgili taslak skill'i üretir.
- Tazmin talepleri ya da sözleşme ihlali konusunda görüş vermez; onay reddedildiğinde ya da süre kaçtığında durumu işaretler, sonuç analizi avukatındır.
- Kazanç payı performansını izlemez; tarihleri finans sahipli referans olarak tutar.
- Rapor sırasında sözleşmeleri yeniden okumaz; avukatın güncellediği takibi okur.

---

## /corporate-legal:material-contract-schedule

---
name: material-contract-schedule
description: >
  Pay/malvarlığı devir sözleşmesindeki (SPA/APA) "Önemli Sözleşme" tanımını
  due diligence bulgularına uygulayarak önemli sözleşmeler ekini kurar ve
  sözleşmenin ek formatına göre biçimlendirir; onay gerektirenleri (TBK m. 205,
  m. 323, 4735 m. 16, sözleşmedeki CoC) ayrı iç takip tablosuyla
  closing-checklist'e aktarır. "Sözleşmeler ekini kur", "açıklama eki",
  "Ek 3.X", "önemli sözleşmeler listesi" denildiğinde ya da açıklama ekleri
  taslaklanırken kullan.
argument-hint: "[satın alma sözleşmesi yolu ya da Önemli Sözleşme tanımını yapıştırın]"
---

# /material-contract-schedule — Önemli Sözleşmeler Eki

1. Satın alma sözleşmesini yükle → "Önemli Sözleşme" tanımı + ek formatı.
2. Tanımı due diligence bulgularına uygula; sınır vakaları işaretle.
3. Sözleşmenin formatına göre biçimlendir.
4. Onay takip tablosu closing-checklist'i besler.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Satın alma sözleşmesinde bir beyan var: "Ek 3.X tüm Önemli Sözleşmeleri listeler." Bu skill o eki due diligence bulgularından kurar — sözleşmenin tanımına göre hangi sözleşmeler önemli, sözleşmenin istediği formatta. Türk hukukunda açıklama eki kanuni bir kurum değildir; içerik ve sonuç (beyan ve tekeffül ihlali, tazmin) tamamen satın alma sözleşmesine bağlıdır. Sözleşme yabancı hukuka tabiyse yorum o hukuka göre yapılır → `/commercial-legal:governing-law-review`.

## Bağlam

- Satın alma sözleşmesi taslağı — "Önemli Sözleşme" tanımı ve ek formatı (İngilizce ya da iki dilli sözleşmede tanımlı terimi aynen kullan)
- `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → önemlilik eşikleri (sözleşme tanımından farklı olabilir — **sözleşmenin tanımı geçerlidir**)
- `diligence-issue-extraction` ve varsa `tabular-review` çıktısı — sözleşme düzeyinde veri
- `deals/[code]/deal-context.md` → işlem yapısı; [ŞİRKET ADI] satıcıysa ek onun beyanıdır (eksik ek = beyan ihlali riski), alıcıysa ekin eksiksizliğini due diligence'la karşılaştır

## Akış

### Adım 1: Tanımı al

Tanımı sözleşmeden çek; tanım belirleyicidir. İşlem yapısı (pay devri / malvarlığı devri / birleşme) bir kolun yorumunu değiştirebilir: pay devrinde "devri onaya bağlı sözleşme" kolu çoğu zaman CoC klozuyla birlikte okunur; malvarlığı devrinde her sözleşmenin devri karşı tarafın katılımını gerektirir (TBK m. 205). Düzenlenmiş sektör ya da kamu sözleşmesi varsa onay kuralları sözleşmenin dışında da yaşar:

| Katman | Kural | Dayanak |
|---|---|---|
| Kamu ihale sözleşmesi | Zorunlu hâllerde ihale yetkilisinin yazılı izniyle devir; devralanda ilk ihaledeki şartlar aranır; izinsiz devirde fesih ve yaptırım | 4735 m. 16 |
| İşyeri kirası | Kira ilişkisinin devri kiraya verenin yazılı rızasına bağlı; işyerinde haklı sebep olmadıkça rıza reddedilemez; devreden en fazla 2 yıl müteselsil | TBK m. 323 |
| Sınai mülkiyet lisansı/devri | Hukuki işlem yazılı; devir noter onaylı; sicile kaydedilmeyen işlem iyiniyetli üçüncü kişiye karşı ileri sürülemez | SMK m. 148/4-5 |
| Lisanslı faaliyet (enerji, bankacılık, sermaye piyasası, elektronik haberleşme, sigorta) | Pay devri ya da kontrol değişikliği için kurum onayı gerekebilir — ezberden yazma, kurum mevzuatını çek | `tr_mevzuat_ara`, `tr_kurum_karari_ara(kurum="epdk"/"bddk"/"spk"/"btk")` |

Tanımda sık görülen kollar — sözleşmeyi okumanın yerini tutmaz, sözleşmedeki liste geçerlidir: parasal eşik (yıllık / toplam), süre, CoC ya da devir yasağı, münhasırlık / rekabet yasağı, ilk N müşteri / tedarikçi, taşınmaz kiraları, fikrî hak lisansları (gelen / giden), ilişkili taraf sözleşmeleri, kamu sözleşmeleri, olağan iş akışı dışındaki sözleşmeler. Tanımı mekanik uygula: herhangi bir kolu karşılayan her sözleşme eke girer.

### Adım 2: Tanımı bulgulara uygula

| Sözleşme | Karşıladığı kol(lar) | Eke girer |
|---|---|---|
| [ad] | [yıllık X TL üstü; CoC m. 12.2] | Evet |
| [ad] | [yok] | Hayır |

**İnsan kararına işaretle:** eşiğin hemen altında ama iş için önemli; bir kolu karşılıyor ama zaten feshediliyor; sözlü anlaşma ya da yan mektup; dövizli bedelin TL karşılığı kura göre eşiğin iki yanına düşüyor (sözleşmenin kur ve tarih kuralını uygula, yoksa sor).

### Adım 3: Ek verisini topla

| Alan | Kaynak |
|---|---|
| Karşı taraf unvanı | Sözleşme (ticaret sicili kaydıyla teyit edilmiş unvan) |
| Sözleşme adı / türü | Sözleşme |
| Tarih | Sözleşme |
| Süre / bitiş | Sözleşme |
| Yıllık / toplam bedel ve para birimi | Sözleşme ya da yönetim verisi |
| Karşıladığı önemlilik kolu | Adım 2 |
| İşlem için onay gerekli mi | Due diligence bulgusu |
| VDR atfı | Due diligence envanteri |

Mevcut çıkarımlardan al. Eksik alanı işaretle — tahmin etme.

### Adım 4: Sözleşmenin formatına göre biçimlendir

Taslaktaki diğer eklerin biçimine uy (numaralı liste ya da tablo, sözleşme türüne göre alt bölümler).

```markdown
## Ek 3.[X] — Önemli Sözleşmeler

İşbu tarih itibarıyla Önemli Sözleşmeler aşağıdadır:

### (a) Müşteri Sözleşmeleri

1. [Hedef] ile [Karşı taraf] arasında [tarih] tarihli [Sözleşme Adı].
   [Format gerektiriyorsa kısa açıklama.]
   [VDR: yol]

### (b) Tedarikçi Sözleşmeleri
### (c) Taşınmaz Kiraları
### (d) Fikrî Hak Lisansları
[sözleşmedeki tanım yapısına göre alt bölümler]
```

Sözleşme İngilizce ya da iki dilliyse eki de aynı dilde/düzende kur; Türkçe karşılığı yalnız format gerektiriyorsa ekle.

### Adım 5: Onay takip tablosu

Ekin içinde değil, ayrı ve dahili olarak: hangi listelenmiş sözleşme onay gerektiriyor.

> Onay tablosu ve ekin teslim öncesi çalışma taslağı gizli due diligence malzemesinden türetilmiştir ve onun gizlilik statüsünü devralır; dağıtımı işlem ekibiyle sınırla (Av. K. m. 36 dağıtılan belgeyi korumaz). İmzalanan sözleşmeye eklenen ek ise işlem belgesidir, karşı tarafla paylaşılır — teslimden önce iç notları sil.

| Ek no | Karşı taraf | Onay gerekli | Dayanak | Durum | Sorumlu | Son gün |
|---|---|---|---|---|---|---|
| 3.X(a)(1) | [ad] | Evet — CoC | Sözleşme m. 12.2 | Talep edildi | [ad] | [tarih] |
| 3.X(c)(2) | [ad] | Evet — kira devri | TBK m. 323; kira m. 9 | Hazırlanıyor | [ad] | [tarih] |

Bu tablo closing-checklist'i besler (Mode 2 aktarım şeması: `counterparty`, `conditions`, `notice_deadline` alanlarını doldur).

## Çapraz kontrol

Teslimden önce:
- Bir kolu karşılayan her sözleşme ekte (eksiksizlik).
- Ekte, hiçbir kolu karşılamayan sözleşme yok (aşırı açıklama yok — bu bir beyandır, veri yığını değil).
- Ek diğer beyanlarla tutarlı (ekteki bir sözleşme rehin/teminat doğuruyorsa teminatlar ekinde de görünmeli).
- Her kaydın VDR atfı var; alıcı avukatı belgeyi bulabilmeli.

## Aktarımlar

- **diligence-issue-extraction'dan:** sözleşme düzeyindeki bulgular girdidir.
- **closing-checklist'e:** onay kalemleri kontrol listesine gider.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu eke göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Önemlilik tanımını belirlemez — o satın alma sözleşmesindedir.
- Onay almaz — hangilerinin gerektiğini izler.
- Beyanı taslaklamaz — beyanın atıf yaptığı eki doldurur.

---

## /corporate-legal:matter-workspace

---
name: matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkil şirketin ya da işlemin bağlamının (pay sahibi yapısı,
  işlem pozisyonu, veri odası bulguları, aile içi uyuşmazlık bilgisi) diğerine
  sızmamasını sağlar. Çok müvekkilli avukat matter oluşturmak, aktif matter'ı
  değiştirmek, listelemek, arşivlemek ya da uygulama düzeyine dönmek istediğinde ya da
  başka bir skill hangi matter'da çalıştığını bilmek istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil şirket ve işlem üzerinde çalışır. Kurumsal işte bir müvekkilin satış hazırlığı, başka bir dosyada alıcı adayı olan müvekkilin ilgisini çeker; aile şirketinde bir pay sahibinin bilgisi diğerinin dosyasına geçmemelidir. Matter çalışma alanı her dosyanın bağlamını ayrı tutar; bu skill o alanları yöneten ince dosya katmanıdır.

## Alt komutlar

- `/corporate-legal:matter-workspace new <slug>` — yeni matter, kısa ön görüşme, `matter.md`
- `/corporate-legal:matter-workspace list` — durum ve aktiflik işaretiyle liste
- `/corporate-legal:matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/corporate-legal:matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/_archived/` altına taşı; asla silme)
- `/corporate-legal:matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünü bul. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli şirket içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/corporate-legal:cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok." Kapalı durum şirket içi kullanıcı için beklenen durumdur.
2. `$ARGUMENTS`'ın ilk kelimesine göre aşağıdaki alt komut mantığına dallan.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` şablondaki gibi kalır; diğer skill'ler ve ajanlar bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/corporate-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
├── deals/<code>/deal-context.md    # --new-deal ile yazılan işlem bağlamı (M&A)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-pay-alimi-2026`, `xyz-olagan-gk-2026`, `def-birlesme`. Müvekkilin gerçek adı yerine takma ad kullanılabilir.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Avukat; aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermişse ve kendi düzenlediği bir senet ya da sözleşmenin hükümsüzlüğünü ileri sürmek durumu ortaya çıkmışsa işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Kurumsal işte sık görülen hâller: aynı şirketin pay sahipleri arasında uyuşmazlık (büro daha önce şirkete ya da bir pay sahibine danışmanlık verdiyse), büronun hazırladığı esas sözleşme, pay devri ya da pay sahipleri sözleşmesine karşı geçersizlik ileri sürülecekse, aynı satış sürecinde birden fazla alıcı adayı (m. 38 kapsamına girip girmediği olaya göre değerlendirilir — avukata işaretle). Sor: "Bu matter için çatışma kontrolü yapıldı mı?" Bu skill çatışma kontrolünü kendisi yapmaz ve bu amaçla başka matter'ların dosyalarını okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve avukata hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz şirket ya da pay sahibi (şirket içinde: iş birimi veya grup şirketi); şirket türü (AŞ / Ltd. / halka açık AŞ / yabancı)
   - **Karşı taraf** — birden fazla olabilir (alıcı/satıcı, yatırımcı, diğer pay sahipleri); yabancıysa LEI ve grup yapısı için `gleif_search_entities` / `gleif_get_group_structure`
   - **Matter türü** — M&A alıcı | M&A satıcı | yatırım/finansman | YK/GK işi | esas sözleşme değişikliği | pay devri | birleşme/bölünme/tür değişikliği | grup yeniden yapılanması | entegrasyon | şirket uyumu | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (clean team; ör. rakipler arası işlemde rekabet açısından hassas bilgi)
   - **Kritik tarihler** — GK tarihi ve çağrı son günü, imza ve kapanış hedefi, düzenleyici onay (Rekabet Kurulu, sektör kurumu) beklentisi, tescil son günü
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, varsayılan yaklaşımdan farkı
   - **Matter'a özel sapmalar** — ör. "önemlilik eşiği bu işlemde 2 milyon TL", "müvekkil aile şirketi — pay sahiplerine giden notlarda ayrı dil", "esas sözleşmede YK nisabı ağırlaştırılmış"
   - **İlgili matter'lar ve deal kodu** — bağlantılı slug'lar; M&A ise `deals/<code>/deal-context.md` kodu
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/corporate-legal:matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar; tablo: Slug | Müvekkil | Matter türü | Durum | Açılış | Aktif. Aktif olanı `*` ile işaretle; `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

`matters/<slug>/matter.md` yoksa `new <slug>` öner. Varsa `Active matter: <slug>` yap ve doğru matter'da olduğunu teyit etmesi için `matter.md` özetini (müvekkil, tür, kritik tarihler) göster.

### `close <slug>` ve `none`

`close`: `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle, `matters/<slug>/` → `matters/_archived/<slug>/` taşı; kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap. M&A matter'ları uzun ömürlüdür; kapanış sonrası kontroller (bedel düzeltmesi, tazmin talepleri, entegrasyon) bitmeden kapatmayı önerme. `none`: yalnız bu satırı değiştirir; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]
**Deal kodu:** [code / —]

## Taraflar
**Müvekkil:** [ad] — [AŞ / Ltd. / halka açık AŞ / yabancı] — [rolü: alıcı / satıcı / şirket / pay sahibi]
**Karşı taraf:** [ad(lar)] — [rol; yabancıysa LEI]

## Matter türü
[tür — tek satır gerekçe]

## Kritik tarihler
- [GK / çağrı son günü; imza; kapanış; düzenleyici onay; tescil]

## Ana olgular
[2-5 cümle; varsayılan yaklaşımdan farkı]

## Matter-specific overrides
- [ör. "M&A materiality: 2 milyon TL (ev standardı 5 milyon TL)."]
- [ör. "Board: esas sözleşme m. [..] — YK toplantı nisabı üye tam sayısının üçte ikisi."]

## İlgili matter'lar
- [slug — neden ilgili]

## Gizlilik notu
[Yüksek / kapalı ekipse nedeni; dosyaları kim görebilir; genel ayar açık olsa bile çapraz bağlama izin var mı]
```

Esaslı skill'ler matter'a özel sapmaları bu başlıktan okuyup profil duruşunun önüne koyar; başlığı çevirme.

## `history.md` başlangıcı

`# Geçmiş: [Müvekkil] — [kısa tarif]` başlığı, "Yalnız ekleme yapılan olay günlüğü; en yeni üstte." notu ve tek girdi: `## [YYYY-AA-GG] — Matter açıldı` — "Ön görüşme tamamlandı. Slug: `[slug]`. Durum: aktif." artı `matter.md` dışında saklanmaya değer ilk bağlam (ör. "Alıcı adayının niyet mektubu geldi.").

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurma yasağını (Av. K. m. 36) ve zıt menfaatli taraflardan doğan çatışma riskini (m. 38) destekler.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş pay alım işleminde tazmin tavanlarını karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır. Kıyas çıktısında müvekkil adlarını ve işlem bedellerini anonimleştirmeyi öner.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil; saklama süresi büronun politikasıdır.
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.

---

## /corporate-legal:tabular-review

---
name: tabular-review
description: >
  Tablolu inceleme — her belgeye bir satır, her veri noktasına bir sütun, her
  hücre kaynağa atıflı. M&A due diligence için kuruldu ("bu 200 hedef
  sözleşmede kontrol değişikliği, devir ve MAC klozlarını çıkar") ama sonunda
  tablo isteyen her toplu incelemede çalışır. "Tablolu inceleme", "inceleme
  tablosu", "grid kur", "bu sözleşmelerden şu alanları çıkar", "bu belgeleri X,
  Y, Z için incele", "bana tablo ver", "toplu inceleme" denildiğinde ya da bir
  belge klasörü gösterilip karşılaştırma istendiğinde kullan.
---

# /tabular-review — Tablolu İnceleme

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` yükle → `## M&A` inceleme yapısı (`Diligence structure`), eşikler, büro formatı.
2. Teyit et: hangi belgeler, hangi sütunlar, çıktı nereye.
3. Tipli şemayı kur, `.review-schema.yaml` olarak yaz, kullanıcıya onaylat.
4. Örnek çalıştırma (3–5 belge). Şemayı düzelt, onaylat.
5. Dağıt — belge başına bir alt ajan, paralel. Her hücre: değer + durum + birebir alıntı + yer.
6. Normalleştirme geçişi. Aykırı ve tutarsız değerleri işaretle.
7. Çıktı: `.xlsx` ya da Google Sheets (sor), ayrıca her zaman `.csv` + `_sources.csv` + markdown. Üst başlık.
8. Özet: doğrulama yükü (sütun başına not_present / unclear / needs_review), işaretli sütunlar, dosya yerleri, "her hücre bulgu değil ipucudur" hatırlatması.

```
/corporate-legal:tabular-review
/corporate-legal:tabular-review --schema .review-schema.yaml --docs ./vdr/02-Sozlesmeler/
/corporate-legal:tabular-review --template ma-diligence
```

`--schema <yol>` mevcut şemayı kullanır (yeniden çalıştırma, ekleme). `--template <ad>` `references/` altındaki şablondan başlar (şimdilik `ma-diligence`). `--docs <yol>` yerel klasör, Drive klasör kimliği ya da VDR yolu; yoksa sorar. `--output <xlsx|gsheets|csv>` yoksa sorar. `--sample <n>` örnek boyutu (varsayılan 5).

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Elinde bir yığın belge ve her birine tutarlı biçimde sorulacak bir soru listesi var: due diligence talep listesi, tedarikçi sözleşmesi denetimi, kira portföyü. Çıktı bir tablodur: satırlar belge, sütunlar veri noktası, her hücre kaynaktaki kelimelere kadar izlenebilir.

Bu sorun avcılığı değildir: `diligence-issue-extraction` 2.000 belgedeki 30 sorunu bulur; bu skill aynı 15 soruyu 2.000 belgenin hepsine sorar. Bu, belgeyi okumanın yerini de tutmaz: her hücre **doğrulanması gereken bir ipucudur**. Çıktı doğrulamayı hızlandırmak için tasarlanır, atlamak için değil.

Bağlam: CLAUDE.md, belirli işlemde `deals/[code]/deal-context.md` (işlem yapısı sütunların yorumunu değiştirir: pay devrinde devir klozu değil CoC klozu önemlidir), varsa mevcut `.review-schema.yaml`.

## Sütun tipleri

Tablonun değeri, C sütununun 1. satırda ve 200. satırda aynı şeyi ifade etmesidir. Serbest metin kayar; tip tutar.

| Tip | Döndürdüğü | Kullanım |
|---|---|---|
| `verbatim` | Belgeden karakteri karakterine alıntı | Tanımlı terimler, işletici kloz metni, kelimelerin önemli olduğu her yer |
| `classify` | Sabit listeden tek değer | Evet/Hayır, var/yok, kloz varyantları |
| `date` | ISO tarih | Yürürlük, bitiş, fesih bildirimi son günü |
| `duration` | Sayı + birim | Süre, bildirim süresi, beyanların geçerlilik süresi |
| `currency` | Sayı + para birimi kodu | Tavan, eşik, bedel (TRY, EUR, USD…) |
| `number` | Yalın sayı | Adet, yüzde, sayfa |
| `free` | Kısa serbest özet | Az kullan — kayan tip budur |

**Birebir kuralı:** `verbatim` dışındaki her sütun, cevabı destekleyen kaynak alıntısını yan alan olarak taşır. Hücredeki cevap yorumdur; alıntı delildir. "consent_not_unreasonably_withheld" diyen bir hücre, geldiği cümle olmadan işe yaramaz.

## "Bulunamadı"nın üç durumu

Boş hücre bilgi saklar. Olumlu cevap üretemiyorsan üç açık durumdan birini kullan:

| Durum | Anlamı |
|---|---|
| `not_present` | Belge okundu, hüküm yok |
| `unclear` | Bir şey var ama güvenle sınıflanamıyor (belirsiz, kısmi ya da çelişen hükümler) |
| `needs_review` | Bir şey bulundu ama kararı insan vermeli (sıra dışı metin, şemanın yakalamadığı takdir) |

"Sözleşme devir konusunda sessiz" ile "devir klozu belirsiz" işlem ekibi için bambaşka işlerdir; tek boş hücrede birleştirme.

## Akış

### Adım 0: Ne ve nerede

1. **Belgeler:** VDR MCP'si (Box, Datasite, iManage), yerel klasör, Drive ya da dosya listesi. Kaç adet? 200'ü aşarsa uyar ve önemlilik süzgeçli alt küme öner.
2. **Şema:** `references/` şablonu (varsayılan M&A due diligence) ya da kullanıcının doğal dilde tarif ettiği sütunlar → tipli şema.
3. **Çıktı:** Excel mi Google Sheets mi — sor, tahmin etme. CSV ve markdown her zaman yazılır.

### Adım 1: Şemayı kur ve onaylat

Her sütun için kalıcı `id`, insan okunur `label`, `type`, `prompt` (belgeyi okuyan incelemecinin soracağı soru) ve `classify` için `options`. `id` ve `options` değerleri İngilizce kalır (başka skill'ler ve dışa aktarımlar bunları okur); `label` ve `prompt` Türkçe olur.

```yaml
schema:
  name: "M&A Due Diligence — Proje [Kod]"
  created: 2026-10-26
  columns:
    - id: counterparty
      label: "Karşı taraf"
      type: verbatim
      prompt: "Hedef dışındaki sözleşme tarafı kim (unvanıyla)?"
    - id: effective_date
      label: "Yürürlük tarihi"
      type: date
      prompt: "Sözleşme hangi tarihte yürürlüğe girdi?"
    - id: change_of_control
      label: "Kontrol değişikliği"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, automatic_termination, termination_right, notice_only]
      prompt: "Sözleşme hedefin kontrolünün değişmesini düzenliyor mu? Ne gerektiriyor?"
    - id: assignment
      label: "Devir sınırlaması"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, freely_assignable, assignable_to_affiliates]
      prompt: "Hedef bu sözleşmeyi devredebilir mi? Hangi sınırlama var?"
    - id: merger_reference
      label: "Birleşme/bölünmeye atıf"
      type: classify
      options: [silent, treated_as_assignment, permitted, termination_right]
      prompt: "Devir/CoC hükmü birleşme, bölünme ya da tür değiştirmeyi açıkça anıyor mu?"
    - id: governing_law
      label: "Uygulanacak hukuk"
      type: verbatim
      prompt: "Sözleşmeye hangi hukuk uygulanır?"
    - id: dispute_forum
      label: "Uyuşmazlık yeri"
      type: classify
      options: [turkish_courts, turkish_arbitration, foreign_courts, foreign_arbitration, silent]
      prompt: "Uyuşmazlıklar hangi mahkemede ya da tahkimde çözülür?"
    # ... diğer sütunlar
```

`merger_reference` sütununu birleşme/bölünme yapısında ekle: sözleşmedeki devir yasağının külli halefiyete (TTK m. 153/1) uygulanıp uygulanmadığı **tartışmalı** olduğundan açık metin önemlidir. Kira için `lease_assignment` (TBK m. 323), kamu sözleşmeleri için `public_contract` (4735 m. 16) sütunlarını düşün. Şemayı çıktının yanına yaz; kullanıcı düzenleyip yeni belgelerle yeniden çalıştırabilir. Dağıtmadan önce göster ve onay al.

### Adım 2: Örnek çalıştırma

Denenmemiş şemayı 200 belgeye dağıtma. Önce 3–5 belge çalıştır, satırları göster. Bak:
- Çoğu cevabı `unclear` olan sütun → istem belirsiz, yeniden yaz.
- Seçeneklere uymayan `classify` cevapları → seçenek ekle ya da `free`'ye çevir.
- Parafraz dönen `verbatim` sütun → karakteri karakterine kuralını pekiştir.
- Türkçe ve yabancı dilde karışık belgeler → alıntı belgenin kendi dilinde kalır, çeviri yapılmaz; iki dilli sözleşmede hangi metnin esas olduğunu ayrı sütunda yakala.

Şemayı düzelt, örneği yeniden çalıştır, onay al.

### Adım 3: Dağıt

Belge başına bir alt ajan, paralel. Her alt ajan belgenin tamamını okur (RAG parçası değil), her sütun için ilgili hükmü bulur ve şunu döndürür: `{value, state, quote, location}` — `value` tipli cevap (`state` `answered` değilse null), `state` `answered | not_present | unclear | needs_review`, `quote` birebir destek metni, `location` madde numarası / başlık / sayfa.

**Alıntı isteğe bağlı değildir; birebir kuralı mekaniktir.** `state: answered` döndürmeden önce:
- `quote`, kaynaktaki bitişik metnin karakteri karakterine kopyası olmalı ve belirtilen `location`'da bulunabilmeli. Başlık + beklenen kalıp metinden alıntı kurma; parafraza "birebir" deme; "bu klozlar genelde şöyledir" bilgisinden alıntı yeniden üretme; bitişik olmayan metni üç noktayla dikme. Keseceksen cümle sınırında kes ve işaretle.
- `location`, normalleştirme geçişinin aynı yeri yeniden açabileceği kadar belirli olmalı.
- Kesin metin bulunup kopyalanamıyorsa (kaynak kesik, OCR bozuk, hüküm ima ediliyor ama yazılı değil) durum `needs_review`, `value` null ve `notes` içinde `quote_unavailable: <sebep>`. Kurgulanmış alıntıyla `answered` asla kabul edilmez.
- Aynı kural `verbatim` sütunlara ve diğer tiplerin yan alıntılarına aynen uygulanır.
- Kişisel veri (çalışan adı, TCKN, ücret) yalnız sütunun gerektirdiği ölçüde alınır (KVKK m. 4/2-ç: amaçla bağlantılı, sınırlı ve ölçülü).

### Adım 4: Normalleştir

Tabloyu sütun sütun oku; her tablolu inceleme aracının hata modu aynı klozun belgeler arasında farklı yorumlanmasıdır.
- **`classify`:** her `answered` değer seçenek listesinde mi? Kümelenmeye bak: 180 `consent_required` / 20 `consent_not_unreasonably_withheld` muhtemelen gerçektir; 195 / 5 `freely_assignable` ise o 5'e bak.
- **`date` / `duration` / `currency`:** biçimi eşitle; makul olmayanları (99 yıllık süre, 1 TL tavan) `needs_review` yap.
- **`verbatim` ve tüm yan alıntılar:** rastgele örnekte (sütun başına en az 3–5 satır ya da satırların %10'u, hangisi büyükse) kaynağı belirtilen yerde yeniden aç, alıntıyı karakteri karakterine karşılaştır. Uyuşmazlıkta hücreyi `needs_review` + `quote_mismatch` yap ve tüm sütunu genişletilmiş kontrole al — bir alt ajan alıntı kurguladıysa diğerleri de kurgulamış olabilir. Uyuşmayan alıntılı `answered` hücre, `unclear`'dan ağır bir hatadır.

### Adım 5: Çıktı

**Markdown** (her zaman, oturum içi inceleme):
```markdown
| Belge | Karşı taraf | Yürürlük | Kontrol değişikliği | Devir | ⚠️ İşaret |
|---|---|---|---|---|---|
| Hizmet Sözleşmesi — Alfa | Alfa A.Ş. | 2023-04-01 | consent_required | consent_required | — |
| Tedarik Sözleşmesi — Beta | Beta Ltd. Şti. | 2021-11-15 | ⚠️ unclear | silent | CoC belirsiz m. 14.2 |
```

**CSV** (her zaman): değerler için bir dosya, alıntı ve yerler için `_sources.csv`.

**Excel ya da Google Sheets** (kullanıcının çalıştığı; sor). Yapı `references/excel-output.md` ve `references/gsheets-output.md`'de. Excel: Claude in Excel varsa o, yoksa `openpyxl`; Sheets: Sheets MCP, ADC ile Sheets API ya da CSV içe aktarma. Her veri sütununun yanında alıntı + yer taşıyan gizli sütun; görünür hücrede açıklama/not olarak alıntı. Renk: beyaz = answered, sarı = unclear/needs_review, gri = not_present. Her veri sütunu için varsayılan boş `Verified` sütunu — incelemeci işaretler; insanın neyi kontrol ettiği bir bakışta görünür. Sütun tanımlarını içeren `_schema` sayfası.

**Formül enjeksiyonu:** belgeden ya da araçtan gelen ve `=`, `+`, `-`, `@`, sekme ya da satır sonuyla başlayan her hücrenin başına tek tırnak koy; CSV'de virgül, çift tırnak ve satır sonlarını RFC 4180'e göre tırnakla.

En üst satıra CLAUDE.md `## Outputs` başlığını koy ve yanına ekle:

> Bu inceleme gizli kaynak belgelerden türetilmiştir ve onların gizlilik statüsünü devralır. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) dağıtılan belgeyi korumaz; dağıtımı işlem ekibiyle sınırla.

### Adım 6: Özet

Belge, sütun ve tamamlanan satır sayısı; sütun başına `not_present` / `unclear` / `needs_review` sayıları (doğrulama yükü budur); normalleştirmede satırların %10'undan fazlası işaretlenen sütunlar; dosyaların yeri; hatırlatma: her hücre ipucudur, beyan, ek ya da not beslemeden önce doğrulanmalıdır.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu tabloya göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Belgeleri okumanın yerini tutmaz; nereye bakacağını söyler.
- Güven puanı üretmez. 0,73 bilgi değildir; güven sinyali `unclear` / `needs_review` durumları ve birebir alıntılardır.
- Belgeyi sessizce atlamaz: gösterilen her belge bir satır alır; okunamayan belge `needs_review` satırı ve notu alır.
- Parafrazı alıntı gibi sunmaz; delil izi işin kendisidir.

## Diğer skill'lerle ilişki

- `diligence-issue-extraction` sorun bulur; bu skill veri noktası çıkarır. Çıkarım bir sorun gösterirse (belirli bir kazanç hedefine bağlı MAC tanımı, olağandışı fesih hakkı) not et ve o belge için diligence-issue-extraction öner.
- `material-contract-schedule` tek bir tabloyu (önemli sözleşmeler eki) kurar ve bu skill'in çıktısını doğrudan kullanabilir — ek, tablolu incelemenin süzülmüş ve biçimlenmiş görünümüdür.
- `ai-tool-handoff` korpus çok büyükse ya da ekip özel platform tercih ediyorsa toplu incelemeyi Luminance/Kira'ya verir. Önce bu skill'i çalıştır, kalanı devret.

---

## /corporate-legal:written-consent

---
name: written-consent
description: >
  Toplantı yapılmadan alınan kararı ev formatında taslaklar: AŞ yönetim kurulunda
  elden dolaştırma (sirküler) karar (TTK m. 390/4), limited şirket genel kurulunda
  yazılı onayla karar (m. 617/4), tek pay sahipli AŞ / tek ortaklı Ltd. yazılı kararı
  (m. 408/3, 616/3). Emsal kararlar deposunda en yakın örneği arar; çok maddeli kararı,
  müzakereye katılma yasağını (m. 393), devredilemez yetki sınırlarını (m. 375, 408),
  esas sözleşmedeki ek şartları ve onay takibini ele alır; büyük tek seferlik işlemlerde
  kapsam uyarısı verir. Kullanıcı "sirküler karar", "elden dolaştırma", "toplantısız YK
  kararı", "yazılı karar", "written consent", "UWC" dediğinde ya da toplantı yapmadan
  kurul onayı gereken bir işlem anlattığında kullan.
argument-hint: "[kurul onayı gereken işlemi anlatın]"
---

# /written-consent

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## Board & Secretary` yükle (`**Consents repository:**`, `**Consent format:**`, karar dili, şirket türü, YK/müdür yapısı).
2. İşlemi ve organı belirle; rutin / inceleme bayrağı olarak sınıflandır.
3. İnceleme bayrağıysa dış avukat uyarısını göster, onay al.
4. Emsal depoda en yakın kararı ara; depo yoksa seed kararları kullan.
5. Kanun ve esas sözleşme kontrolünü yap; ev formatında taslakla.
6. Çıktı: karar taslağı + onay takip listesi + kontrol listesi + mevzuat notu.

## Matter context

`## Matter workspaces` bölümüne bak. `Enabled` `✗` ise bu paragrafı atla. Açık ve aktif matter yoksa sor: "Bu hangi matter için? `/corporate-legal:matter-workspace switch <slug>` ya da `practice-level`." Aktif matter'ın `matter.md`'sini yükle; çıktıyı `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter okuma.

## Türk hukukunda toplantısız karar — önce bunu bil

ABD'deki "unanimous written consent" kalıbı Türk hukukuna taşınmaz. Hangi organın, hangi şartla toplantısız karar alabileceği kanunda ayrı ayrı düzenlenmiştir:

| Organ | Dayanak | Şartlar |
|---|---|---|
| AŞ yönetim kurulu | TTK m. 390/4 | Hiçbir üye toplantı istememeli · bir üyenin belirli konuda **karar şeklinde yazılmış önerisi** · aynı önerinin **tüm** üyelere yapılması (geçerlilik şartı) · **en az üye tam sayısının çoğunluğunun** yazılı onayı (oybirliği şart değil) · onay kâğıtlarının karar defterine yapıştırılması ya da imzaları içeren karara dönüştürülüp deftere geçirilmesi (geçerlilik şartı) |
| Ltd. genel kurulu | m. 617/4 | Hiçbir ortak sözlü görüşme istememeli · bir ortağın gündem maddesine ilişkin önerisine diğer ortakların yazılı onayı · aynı önerinin **tüm** ortakların onayına sunulması (geçerlilik şartı) |
| Tek pay sahipli AŞ / tek ortaklı Ltd. | m. 408/3, 616/3 | Tek pay sahibi/ortak GK'nın tüm yetkilerine sahiptir; kararları geçerlilik için yazılı olmalı |
| AŞ genel kurulu (çok pay sahipli) | — | Kanunda elden dolaştırma yolu yoktur; en hızlı yol çağrısız genel kuruldur (m. 416) ve o da **toplantıdır** |
| Ltd. müdürler kurulu | m. 624/3 | Şirket sözleşmesi karar alma usulünü düzenleyebilir; sözleşmede hüküm yoksa m. 390/4'ün kıyasen uygulanması **tartışmalı — içtihadı ve şirket sözleşmesini kontrol et** |

Her durumda: YK kararlarının geçerliliği yazılıp imza edilmelerine bağlıdır (m. 390/5).

**Tartışmalı noktalar (avukata işaretle):** (1) m. 617/4'te karar için ortakların tamamının mı yoksa m. 620-621 nisaplarının mı arandığı — **tartışmalı, içtihadı kontrol et** (`tr_ictihat_ara(query="limited şirket genel kurul yazılı onay 617")`); (2) esas sözleşmenin m. 390/4 onay sayısını ağırlaştırıp ağırlaştıramayacağı; (3) elektronik imzalı onayların deftere geçirilme pratiği.

## Kapsam uyarısı — taslaktan önce oku

> **Bu skill, emsali olan günlük kararlar içindir:** imza yetkisi ve temsil şekli güncellemesi, banka yetkilendirmesi, müdür atama, olağan GK çağrı ve gündem kararı, emsal koşullu grup içi hizmet sözleşmesi, eşik altı sözleşme onayı.
>
> **Büyük tek seferlik işlemlerde dış avukat incelemesi, bu skill ne üretirse üretsin, ihtiyatlıdır:** pay/şirket alımı-satımı, birleşme, bölünme, tür değişikliği, sermaye artırımı ya da yeni yatırımcıya pay, finansman ve teminat, yönetim kontrolü değişikliği, tasfiye, önemli taşınmaz işlemi, ileride bir veri odasında inceleneceği belli her karar.
>
> Bayrak engel değildir; emsalden uyarlanmış temiz bir taslağın bu işlem için yeterli olup olmadığını düşünme çağrısıdır.

## Büyük işlem + aynı gün imza = dur

İki koşul birlikte varsa: (1) işlem aşağıdaki **inceleme bayrağı** listesinde; (2) kullanıcı aynı turda imzaya bağlıyor ("bugün e-imzaya gönder", "akşam noterde", "kapanıştan önce lazım", "KAP açıklamasından önce imzalansın").

Çıktı ver ve dur:

> ⛔ **Büyük işlem + aynı gün imza — bunu imzaya hazır işaretlemeyeceğim.**
>
> Bu [işlem türü]; geri dönüşü zor bir karar. Bugün imzalanmasını istiyorsunuz; kurul kararında hatanın en zor düzeltildiği an tam budur. Taslağı memnuniyetle hazırlarım ama dış avukat bakmadan imzaya hazır işaretlemem.
>
> 1. **Ben taslaklarım, dış avukat inceler, sonra imza** — olağan yol. "Taslakla" deyin.
> 2. **Dış avukat zaten bu işte ve taslak yolunu onayladı** — kim, ne zaman inceledi söyleyin; devam eder ve taslağın dış avukatta olduğunu not ederim.

Açık seçim olmadan Adım 1'e geçme. Aynı gün baskısı olmayan büyük işlemde bayrak geçerlidir ama durdurmaz.

## Bağlamı yükle — emsalsiz kesin duruş

`## Board & Secretary` → emsal kararlar deposu yoksa **ve** bu oturumda seed karar paylaşılmamışsa (ya da `**Consent format:**` belirli bir seed'den çıkarılmış dil içermiyorsa) taslaklama. Aynen şunu yaz ve bekle:

> **Emsal yok — taslaktan önce duruyorum.**
>
> Ev formatınız olmadan yazılan karar, kazandırdığından fazla düzeltme ister; karar dili, gerekçe derinliği, yetkilendirme kalıbı ve imza bloğu şirketinize özgüdür.
> 1. **Önceki bir kararı yapıştırın ya da yükleyin** (bu şirketin herhangi bir sirküler kararı — içeriği değil biçimi alırım), YA DA
> 2. **"Genel şablonla yaz, şekli ben düzeltirim"** deyin — açıkça söylemeniz gerekir; varsaymam.

## Adım 1 — İşlemi belirle

Sor: ne onaylanacak (tek cümle); destekleyici ayrıntı (atanacak kişi, banka ve yetki sınırı, karşı taraf ve bedel); yürürlük tarihi; organ (YK, Ltd. GK, tek pay sahibi); kurulda menfaat çatışması var mı.

**Organ ve yetki kontrolü (taslaktan önce):**
- **GK'nın devredilemez yetkisi mi?** Esas sözleşme değişikliği, YK üyelerinin seçimi/ücreti/ibrası/görevden alınması, denetçi seçimi, finansal tablolar ve kâr, fesih, önemli miktarda şirket varlığının toptan satışı GK'nındır (m. 408/2). Diğer organların devredilemez yetkilerine giren YK kararları batıldır (m. 391/1-d). Ltd.'de GK'nın devredilemez yetkileri: m. 616 (ör. müdür atama, esas sermaye payı devrinin onayı).
- **YK'nın devredilemez görevi mi?** Üst düzey yönetim, yönetim teşkilatı, muhasebe ve finans düzeni, şube müdürleri hariç müdürlerin atanması ve görevden alınması, üst gözetim, defterler ve faaliyet raporu, borca batıklık bildirimi (m. 375/1). Bunlar YK kararıyla alınır; yönetimin devri ancak esas sözleşme hükmü ve iç yönergeyle mümkündür (m. 367/1).
- **YK üyesiyle işlem mi?** YK üyesinin şirketle işlemi GK izni gerektirir; aksi hâlde şirket işlemin batıl olduğunu ileri sürebilir (m. 395/1). Pay sahibi olmayan üyeye ve yakınlarına nakit borç, kefalet, garanti, teminat yasağı (m. 395/2); grup şirketleri birbirine kefil olabilir (m. 395/3). YK sirküler kararı GK izninin yerine geçmez.
- **Halka açık ortaklık + ilişkili taraf işlemi mi?** SPK'nın belirlediği nitelikteki işlemler için önceden YK kararı ve bağımsız üyelerin çoğunluğunun onayı aranır; aykırı karar geçerli sayılmaz (SerPK m. 17/3).
- **Menfaat çatışması:** ilgili üye müzakereye katılamaz; tereddütte YK karar verir, ilgili üye o oylamaya katılamaz; katılmama sebebi karara yazılır (m. 393/1, 393/3). Elden dolaştırmada ilgili üyenin onayının sayıya katılıp katılmayacağı **tartışmalı** — onayı saymadan çoğunluğun sağlandığını göster ve avukata işaretle.

**Sınıflandır:**

*Rutin — emsal büyük olasılıkla var:* temsile yetkili kişiler ve temsil şekli (karar noter onaylı suretle tescil ve ilan için sicile verilir, m. 373/1); banka hesabı ve yetki limitleri; müdür atama/görevden alma (m. 375/1-d); olağan GK çağrısı ve gündemi (gündemi çağıran belirler, m. 413/1); emsal koşullu grup içi hizmet/lisans; eşik altı sözleşme; şube açılışı (sicile tescil).

*İnceleme bayrağı — dış avukat ihtiyatlı:* pay ya da şirket alımı-satımı, yatırım; birleşme, bölünme, tür değişikliği; sermaye artırımı, yeni yatırımcıya pay; kredi, teminat, kefalet; YK üyesiyle ya da ilişkili tarafla işlem; önemli varlık satışı (GK yetkisi, m. 408/2-f); fesih, tasfiye, konkordato ya da borca batıklık bildirimi (m. 376/3); sermaye kaybı nedeniyle GK çağrısı (m. 376/1-2); ileride veri odasına girecek her karar.

Bayraklıysa:

> ⚠️ **Dış avukat incelemesi önerilir.** Bu [işlem türü] görünüyor; emsalden uyarlanmış taslak yetmeyebilir. Dağıtmadan önce dış avukat incelemesini düşünün. Yine de taslaklayayım mı?

## Adım 2 — Emsal ara

**Depo bağlıysa:** işlem türüyle ara ("imza yetkisi", "banka", "müdür atama", "grup içi"); en yeniyi ya da kullanıcının seçtiğini al:

> [N] emsal buldum: 1. [konu] — [tarih] 2. [konu] — [tarih]. Hangisi en yakın? Yoksa en yenisini mi kullanayım?

Seçileni oku; karar dili, gerekçe yapısı, yetkilendirme kalıbı ve özel kayıtları çıkar; önceki işlemle bugünkü arasındaki farkları listele.

**Depo yoksa:** biçimi `**Consent format:**`'tan al ve söyle: "Emsal deposu bağlı değil; biçim seed kararlarınızdan. Bu işlem türü için önceden alınmış bir karar varsa içerik için onu da paylaşın."

## Adım 3 — Taslak

Emsalin ya da seed'in biçimini birebir izle. Varsayılan iskelet (AŞ YK, m. 390/4):

```
[ŞİRKET ADI] (ticaret unvanı)
YÖNETİM KURULU KARARI
Karar Tarihi: [GG.AA.YYYY]   Karar No: [YYYY/NN]
Karar şekli: Toplantı yapılmaksızın, TTK m. 390/4 uyarınca elden dolaştırma yoluyla

Öneri sahibi üye: [Ad Soyad]
Karar şeklinde yazılmış öneri [tarih] tarihinde [yöntem] ile yönetim kurulunun tüm
üyelerine iletilmiştir. Hiçbir üye toplantı yapılması isteminde bulunmamıştır.

Konu: [..]
Gerekçe: [1-2 cümle — olgular ve kurulun neden karar vermesi gerektiği]

KARAR:
1. [Kesin karar: kim, ne, hangi tutar ve para birimi, hangi belge — "Ek-1'deki [tarih]
   tarihli [sözleşme adı]"];
2. [Uygulama yetkisi: Şirketi temsile yetkili [ad/unvan]'ın bu kararın uygulanması için
   gerekli her türlü belgeyi Şirket adına imzalamaya yetkili kılınmasına];
3. [Gerekiyorsa: işbu kararın noter onaylı suretinin tescil ve ilan için ticaret sicili
   müdürlüğüne verilmesine].

Onaylar — üye tam sayısı: [N]; gerekli asgari yazılı onay: [N'nin çoğunluğu /
esas sözleşme m. [..]]
[Ad Soyad] — Kabul / Ret — İmza — Tarih
[...]
Müzakereye katılmayan üye ve sebebi (TTK m. 393/3): [Yok / Ad — sebep]

Defter kaydı: Onay imzalarını içeren bu karar yönetim kurulu karar defterine geçirilmiştir /
onay kâğıtları deftere yapıştırılmıştır (TTK m. 390/4). Sayfa: [..]
```

**Ltd. GK (m. 617/4):** "Öneri sahibi ortak", "öneri tüm ortakların onayına [tarih]te sunulmuştur; hiçbir ortak sözlü görüşme isteminde bulunmamıştır", gündem maddesi, karar, ortak bazında esas sermaye payı ve oy (m. 618/1) ile onay/ret. **Tek pay sahibi / tek ortak:** "[Ad], şirketin tek pay sahibi/ortağı sıfatıyla genel kurul yetkisini kullanarak aşağıdaki kararı almıştır" + imza (m. 408/3, 616/3).

**Yazım notları:** belirsiz karar ("işlem onaylandı") veri odasında sorun çıkarır — tarafları, tutarı, belgeyi adlandır. Belirli bir yetki için "yetkililer" değil, kişi adı yaz. Onaylanan belgeyi eke koy ve atıf yap. Karar dilini emsalden al; bir kararda karıştırma.

## Adım 4 — Kanun ve esas sözleşme kontrolü

Kanunun varsayılanını esas sözleşme ya da şirket sözleşmesi değiştirebilir. **Şirketin kendi esas sözleşmesindeki ek şartlar uygulanır; esas sözleşmeyi okumadan "hazır" deme.** Kontrol et:
- Esas sözleşmede ağırlaştırılmış YK nisabı (m. 390/1) ya da belirli konular için toplantı şartı var mı?
- Elektronik toplantı/oy esas sözleşmede öngörülmüş mü (m. 1527/1)?
- İmtiyazlı pay grubunun YK'da temsil ya da onay hakkı var mı?
- Pay sahipleri sözleşmesinde veto veya onay listesi var mı? Şirkete karşı ileri sürülebilirliği **tartışmalı** — avukata işaretle.
- Karar defteri fiziki mi, elektronik mi (m. 64/3-4)? Onayların deftere nasıl geçirileceği buna göre belirlenir.

`## Board & Secretary`'de ev duruşu varsa uygula ve dayandığın kuralı yaz. Çıktıya kısa **"Mevzuat notu"** ekle: hangi organ, hangi madde, gereken onay sayısı, esas sözleşmede bulunan/bulunamayan hüküm, açık kalan tartışmalı nokta. Madde atfını yazmadan önce `tr_mevzuat_madde_getir(number="6102", madde_no=["390","393"])` ile güncel metni çek.

## Adım 4.5 — Sonuç doğuran eylem kapısı

`## Who's using this` → Role **avukat değilse**:

> Kararın imzalanması şirketi bağlar ve şirket kaydı olur. Bir avukatla gözden geçirdiniz mi? Evetse devam. Hayırsa avukata götürmeniz için brif: işlem (karar metni) · bulgular (organ, onay sayısı, esas sözleşme, işaretlenen çatışma) · açık sorular · ne ters gidebilir (batıl karar, geçersiz onay, defter kaydı eksikliği, GK izni gereken işlem, tescil yapılmaması) · avukata sorulacaklar (doğru organ ve yol bu mu; esas sözleşme bu işlemi toplantısız karara izin veriyor mu). Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz.

Açık "evet" olmadan imzaya hazır sürüm üretme; araştırma, biçim çıkarma ve TASLAK serbest.

## Adım 5 — Çıktı

1. **Karar taslağı** — imzalanan karar şirket kaydıdır, üst başlık almaz. Aşağıdakiler `## Outputs` üst başlığını taşır.
2. **Onay takip listesi:**
```
[ÜST BAŞLIK — ## Outputs; role göre]
ONAY TAKİBİ — [işlem] — [tarih]
Öneri tüm üyelere/ortaklara iletildi: □ [tarih, yöntem, kanıt]
Toplantı/sözlü görüşme istemi: □ yok
Gerekli asgari onay: [sayı ve dayanak]
□ [Üye/ortak 1]  □ [Üye/ortak 2]  □ [...]
Menfaat çatışması: [Yok / Ad — müzakereye katılmadı; sebep karara yazıldı]
Deftere geçirme: □ [tarih, sayfa]   Tescil-ilan: □ gerekli değil / □ başvuru [tarih]
```
3. **Kontrol listesi:** karar işlemi kesin tanımlıyor · doğru organ ve yetki (m. 375, 408, 616) · tarih doğru · ekler ekli · yetkililer adıyla yazıldı · çatışma açıklandı · esas sözleşme kontrol edildi · büyük işlemde dış avukat inceledi.
4. **Taslağın başına not** (imzadan önce çıkarılır):

> **⚠️ İnceleyen notu:** Bu metin avukat incelemesi için taslaktır, alınmış bir karar değildir. İmzalanması şirketi bağlar ve şirket kaydı olur; avukat inceleyip gerekirse düzeltmeden ve sorumluluğu üstlenmeden imzaya göndermeyin.

**Karşılaştırmalı not (ABD):** ABD kalıbı ("unanimous written consent") adı üstünde oybirliğine dayanır; Türk AŞ'sinde m. 390/4 çoğunluk onayıyla yetinir ama önerinin herkese yapılmasını ve deftere geçirmeyi geçerlilik şartı sayar. ABD kalıbındaki "counterparts" ve "WHEREAS/RESOLVED" dili ev üslubunuz değilse kullanma.

## Bu skill ne yapmaz

- İşlemin kurul onayı gerektirip gerektirmediğine karar vermez; avukatın işidir.
- Özen ve bağlılık yükümü ya da menfaat çatışmasının çözümü hakkında görüş vermez; işaretler, avukat çözer.
- Büyük işlemlerde dış avukat incelemesinin yerini tutmaz.
- Kararı dağıtmaz, imzaları toplamaz, deftere işlemez, sicile başvurmaz; takip listesi başlangıç noktasıdır.
