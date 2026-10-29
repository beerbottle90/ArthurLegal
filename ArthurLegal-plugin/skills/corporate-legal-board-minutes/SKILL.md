---
name: corporate-legal-board-minutes
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

`## Matter workspaces` bölümüne bak (uygulama düzeyi CLAUDE.md). `Enabled` `✗` ise (şirket içi kullanıcıda varsayılan) bu paragrafı atla; matter katmanı görünmez. Açık ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Tutanak ve karar şirketin hukuki kaydıdır; finansman, denetim, sicil işlemi ve M&A veri odasında incelenir. Türk hukukunda şekil geçerlilik meselesidir: YK kararlarının geçerliliği yazılıp imzalanmalarına bağlıdır (TTK m. 390/5); YK karar defteri ve genel kurul toplantı ve müzakere defteri ticari defterdir (m. 64/4) ve bunların tutulması YK'nın devredilemez görevidir (m. 375/1-f). Genel kurul tutanağı toplantı başkanlığınca ve (temsilci bulunan toplantıda) Bakanlık temsilcisince imzalanmazsa geçersizdir (m. 422/1). Bu skill taslağı ev formatında hazırlar; avukat inceler ve düzeltir.

**Kapsam:** AŞ YK toplantı kararı ve komite tutanağı · AŞ olağan/olağanüstü genel kurul tutanağı · Ltd. müdürler kurulu kararı · Ltd. genel kurul tutanağı. Toplantısız (elden dolaştırma) karar → `/arthurlegal:corporate-legal-written-consent`.

## Bağlamı yükle

`~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## Board & Secretary`: tutanak biçimi (uzun anlatı / yalnız karar / karma), `**Minutes template:**` (örnek tutanaklardan çıkarılan yapı, karar dili, başlık), YK ve komite yapısı, karar defteri türü (fiziki / elektronik), elden dolaştırma kullanımı. Biçim kayıtlı değilse önce `/arthurlegal:corporate-legal-cold-start-interview --module board` çalıştır; genel şablonla devam etme.

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
[Müvekkil] (ticaret unvanı)
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

**AŞ GK tutanağı:** başlık ("[Müvekkil] (ticaret unvanı) [YIL] YILINA AİT OLAĞAN GENEL KURUL TOPLANTI TUTANAĞI"); toplantı tarihi, yeri, Bakanlık temsilcisinin adı ve görevlendirme yazısı (varsa); çağrının nasıl yapıldığı; hazır bulunanlar listesine göre nisap; başkanlık oluşturulması; her gündem maddesi için görüşme özeti, sorulan sorular ve verilen cevaplar, karar ve **olumlu ve olumsuz oy sayıları**; karşı oy ve muhalefet şerhleri. Tutanak; pay sahiplerini ya da temsilcilerini, paylarını, gruplarını, sayılarını ve itibarî değerlerini de içerir (m. 422/1). Olağan GK gündeminde tipik başlıklar: organların seçimi, finansal tablolar, YK yıllık raporu, kârın kullanım şekli ve dağıtılacak kâr payı oranları, YK üyelerinin ibrası (m. 409/1). İmza: toplantı başkanlığı ve toplantıda bulunuyorsa Bakanlık temsilcisi (m. 422/1; temsilcinin zorunlu olduğu toplantılar Yönetmelik m. 32).

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

YK'nın elden dolaştırma yoluyla kararı (m. 390/4), Ltd. GK'nın yazılı onayla kararı (m. 617/4) ve tek pay sahipli/tek ortaklı şirketin yazılı kararı → `/arthurlegal:corporate-legal-written-consent`.

## Bu skill ne yapmaz

- Toplantıya katılmaz, anlık görüşmeyi yakalamaz; materyallerden ve avukat girdisinden yazar.
- Kararın hukuken geçerli ya da yeterli olduğuna karar vermez; nisap ve şekil işaretleri avukatın değerlendirmesi içindir.
- Tutanağı kesinleştirmez, deftere işlemez, sicile başvurmaz, dağıtmaz.

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
