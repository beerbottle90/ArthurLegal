---
name: regulatory-legal-policy-diff
description: Belirli bir düzenleme değişikliğini dizinlenmiş politika kütüphanesiyle karşılaştırır. Bir kanun, yönetmelik, tebliğ ya da Kurul kararı değiştiğinde hangi politikalara dokunduğunu ve açığın ne olduğunu bulmak için; "bu düzenlemeyi politikalarımızla karşılaştır", "hangi politikayı etkiliyor", "açık analizi" denince ya da reg-feed-watcher önemli bir kalemi devrettiğinde kullan.
argument-hint: "[düzenlemenin adı ya da künyesi, veya metni/özeti yapıştırın]"
---

# /policy-diff

1. Profili yükle: `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → `## Policy library` (`**Location:**`, `**Policies indexed:**` tablosu: Policy, File, Last updated, Owner).
2. Aşağıdaki iş akışını uygula.
3. Düzenlemeden gereklilikleri çıkar; dizinlenmiş politikalarla eşle.
4. Çıktı: gereklilik bazında açık analizi ve güncellenmesi gereken politika.

---

## Matter context

Eklenti profilinde `## Matter workspaces` → `Enabled` `✗` ise (şirket içi kullanımda varsayılan) bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:regulatory-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

---

## Amaç

Bir düzenleme değişti; politikalarınız var. Bu skill değişikliğin hangi politikalara dokunduğunu ve "düzenlemenin artık istediği" ile "politikanın söylediği" arasındaki açığı bulur. Yalnız KVKK'ya dokunan ve aydınlatma, VERBİS, başvuru süreçlerine inen ayrıntılı analiz için `/arthurlegal:privacy-legal-reg-gap-analysis` daha uygundur; İK el kitabı değişikliği için `/arthurlegal:employment-legal-handbook-updates`.

## Bağlamı yükle

`## Policy library` → politikalar, dosya yerleri, sahipler. `firm-profile.md` → [Müvekkil]'ın faaliyetleri, lisansları, halka açıklığı (gerekliliğin uygulanıp uygulanmadığını anlamak için).

## Kapsam bütünlüğü

Kullanıcı bir politika bölümünü, gerekliliği ya da kategoriyi karşılaştırma dışında bırakmak isterse:

1. Bırak — kapsam kullanıcınındır.
2. Ama yüksek sesle ve kalıcı olarak işaretle: "⚠️ KAPSAM SINIRI: [X] bölümü kullanıcı isteğiyle dışarıda bırakıldı. Bu karşılaştırma politikanın tamamını yansıtmaz. Dışarıda kalan alandaki açıklar BELİRLENMEDİ." Üst başlığın üstüne koy; sonraki her çıktıya taşı.
3. gap-surfacer'a da ilet: "Bu karşılaştırmanın kapsamı daraltıldı; tam uyum resmi olarak sunulmasın." Bu karşılaştırmadan doğan her açık kaydına başlığı aynen taşı.
4. Dışarıda bırakmanın sonucunu söyle: "Tedarikçi yönetimini dışarıda bırakmak, sonuçta 'tedarikçi yönetimini ele alan politika yok' görünmesine yol açar; bu, açığı göstermekten daha kötüdür."

Açıklanmamış bir kapsam daraltmasına dayanan uyum belgesi, sonradan bir denetim ya da uyuşmazlıkta gizleme gibi görünür. İşaret "incelemeyi daralttık" ile "sorunu sakladık" arasındaki farktır.

## İş akışı

### Adım 0: Karşılaştırmadan önce kuralın durumunu doğrula

Kuralı politikaya karşı koymadan önce gerçekten yürürlükte olduğunu teyit et. Uyarı işaretleri:
- Yürürlük ya da uyum tarihi 30 günden fazla geçmiş ama ertelenmediğine dair teyit yok; ya da yürürlük ileri tarihli, geçiş süresi var.
- Kural 12 aydan eski.
- Tartışmalı bir düzenleme; dava ya da AYM başvurusu konusu olabilir.

İşaret görürsen kontrol et:
- **Konsolide metin ve dipnotlar:** `tr_mevzuat_madde_getir(number="<no>", madde_no=[...])` (kurum düzenlemesinde `mevzuat_id`) → `annotations` alanındaki "(Değişik: …)", "(Ek: …)", "(Mülga: …)", "(İptal …)" notları. Mülga hükmü yürürlükte gösterme.
- **Geçiş hükmü:** geçici maddeleri ayrıca çek (`madde_no="geçici 3"`). Örnek: 7499 sayılı Kanunla değişen KVKK m. 9'un eski birinci fıkrası, değişik hâliyle birlikte 1/9/2024'e kadar uygulanmaya devam etti (KVKK geçici m. 3/1).
- **AYM:** `tr_aym_ara(kind="norm", query="<kanun no ve adı>")`. Kanun ya da CB kararnamesi hükmü, iptal kararının Resmî Gazete'de yayımlandığı tarihte yürürlükten kalkar; AYM iptalin yürürlüğe gireceği tarihi ayrıca kararlaştırabilir (yayımdan başlayarak en çok bir yıl); iptal kararları geriye yürümez (Anayasa m. 153/3, 153/5).
- **Danıştay (yönetmelik, tebliğ, düzenleyici Kurul kararı):** `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="\"<düzenleme adı>\" iptal")`; dönen kararın künyesini birebir kullan. Dava açılması işlemin yürütülmesini durdurmaz; yürütmeyi durdurma ayrı şartlara bağlı bir karardır (İYUK m. 27/1, 27/2). Yalnız dava açılmış olması kuralı askıya almaz.
- **Sonraki değişiklik:** `tr_resmi_gazete_tara(query="<düzenleme adı>", date_from="<yayım tarihi>")` (60 günlük dilimlerle).

Teyit edersen devam et. Araç yoksa ya da teyit edemiyorsan, üst başlıktan önce, her şeyin üstüne şu başlığı koy:

> `⚠️ KURAL DURUMU DOĞRULANMADI — Bu kuralın şu anda yürürlükte olduğunu teyit edemedim. Yayımlanan düzenlemeler sonradan değiştirilebilir, ertelenebilir, iptal edilebilir ya da yürütmesi durdurulabilir. Durumunu mevzuat.gov.tr, Resmî Gazete ve AYM/Danıştay kararlarından ya da dış avukattan teyit etmeden aşağıdaki tarihleri bağlayıcı sayma.`

Her son tarihi etiketle: `[yayımlanan metne göre — durum doğrulanmadı]`. Belirsizlik aşağı akar: açığı gap-surfacer'a devrederken `status_verified: false` yaz ki yayımlanmış bir tarih tek başına onu Overdue kovasına taşımasın.

### Adım 1: Yeni gereklilikleri çıkar

**Sessiz tamamlama yok.** Düzenleme metni eksik ya da belirsizse ve tamamı kaynaktan alınamıyorsa dur ve sor. Web araması ya da model bilgisiyle doldurma: "Elimde [olan] var. Gereklilikleri doğru çıkarmak için [eksik] gerekiyor. Seçenekler: (1) tam metni yapıştırın, (2) birincil kaynağı gösterin, (3) web araması — sonuçlar `[web araması — doğrula]` etiketi taşır ve kurumun sitesinden kontrol edilmelidir, (4) burada durmak. Hangisi?" Düşük güvenilirlikteki kaynağı kabul etme kararı avukatındır.

Metni araçla çek:
- Yayımlanan değişiklik metni: `tr_resmi_gazete_getir(url="<fihrist url>")`.
- Konsolide madde: `tr_mevzuat_madde_getir(number="<no>" | mevzuat_id="<id>", madde_no=[...])` (en çok 10); kimlik için `tr_mevzuat_ara`.
- Kurul kararı: `tr_kurum_karari_getir(kurum="<kurum>", id="<id>")`.
- Yabancı: `eu_get_document_text`, `uk_get_section`, `de_norm_getir` vb.; listede olmayan ülke için "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

**Kaynak etiketi.** Düzenleme künyesi, atıflar ve politika alıntıları dâhil her öğeye nereden geldiğini yaz: `[ArthurLegal TR — <araç> — GG.AA.YYYY]`, `[politika kütüphanesi]`, `[web araması — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`. Etiketleri silme.

Her ayrık yeni ya da değişen gerekliliği listele:

| # | Gereklilik | Yürürlük / geçiş | Atıf (araçtan dönen `citation`) |
|---|---|---|---|
| 1 | [ne istiyor] | [tarih] | [madde/fıkra] |

Somut ol. "Bildirim yükümlülükleri güçlendirildi" bir gereklilik değildir. "Standart sözleşme, imzaların tamamlanmasından itibaren beş iş günü içinde Kuruma bildirilir; bildirimi kimin yapacağı sözleşmede belirlenmemişse veri aktaran bildirir" bir gerekliliktir (Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik m. 14/5).

### Adım 2: Politikalarla eşle

Her gereklilik için en yakın dizinlenmiş politika hangisi?
- **Doğrudan:** politika bu konuyu açıkça ele alıyor.
- **Dolaylı:** politika ilgili bir konuyu ele alıyor; bu yeni bir alt konu.
- **Eşleşme yok:** hiçbir politika ele almıyor — açık "politika yok"tur.

Türk mevzuatında değişiklik çoğu zaman kanundan değil ikincil düzenlemeden gelir; eşlerken dayanak zincirini izle. Doğrulanmış örnekler:

| Alan | Tipik politika | Dayanak zinciri |
|---|---|---|
| Kişisel veri (6698) | Veri güvenliği, yurt dışı aktarım, tedarikçi yönetimi | Teknik ve idari tedbir yükümlülüğü (m. 12/1); yurt dışı aktarım yeterlilik kararı → uygun güvence → arızi istisna sırasıyla (m. 9/1, 9/4, 9/6); usul ve esaslar yönetmelikle (m. 9/11) → `KKY` türünü izle. |
| Bankacılık (5411) | Müşteri sırrı, veri paylaşımı, dış hizmet | Müşteri sırrı, istisnalar dışında, açık rıza alınsa dahi müşteri talebi ya da talimatı olmadan üçüncü kişilerle paylaşılamaz (m. 73/3); paylaşımın kapsam, usul ve esaslarını Kurul belirler (m. 73/5) → BDDK düzenlemelerini izle. |
| Sermaye piyasası (6362) | İçsel bilgi ve özel durum açıklama politikası | Değeri, fiyatı ya da yatırım kararını etkileyebilecek bilgi kamuya açıklanır; açıklama, erteleme usul ve esaslarını Kurul belirler (m. 15/1, 15/2) → SPK tebliğleri ve haftalık bülten. |
| Elektrik piyasası (6446) | Lisans uyumu, Kuruma bilgi verme, piyasa işlemleri | Lisans hak ve yükümlülükleri Kurum yönetmeliğiyle düzenlenir (m. 5/1); lisans sahibi istenen bilgi ve belgeyi zamanında, tam ve doğru verir ve faaliyet alanına göre mevzuatın gereklerini yerine getirir (m. 5/2-d, 5/2-e); ikincil mevzuata, Kurul kararına aykırılık ihtar ve idari para cezasına bağlıdır (m. 16/1-b) → EPDK yönetmelik ve Kurul kararları. |
| İş sağlığı ve güvenliği (6331) | Risk değerlendirmesi, acil durum, eğitim | İşveren risk değerlendirmesi yapmak ya da yaptırmakla yükümlüdür (m. 10/1); ayrıntılar Bakanlık yönetmelikleriyle düzenlenir (m. 30/1) → `YONETMELIK` türünü izle. |
| Rekabet (4054) | Rekabet uyum programı, dağıtım ve bayilik | Rekabeti kısıtlayan anlaşma, uyumlu eylem ve teşebbüs birliği kararları yasaktır (m. 4); Kurul belirli anlaşma türleri için grup muafiyeti tebliğleri çıkarabilir (m. 5/4) → tebliğ değişikliği dağıtım sözleşmelerine ve uyum politikasına dokunur. |

Tutar ve eşikleri (idari para cezası, sermaye, ciro) politikaya sabit yazma; "güncel tutarı teyit et (dönemsel güncellenir)" de.

### Adım 3: Karşılaştır

Her doğrudan ve dolaylı eşleşmede politikayı oku ve karşılaştır:

```markdown
### Gereklilik [N]: [ad]

**Yeni kural istiyor:** [gereklilik + atıf + kaynak etiketi]

**Politikamız ([ad], son güncelleme [tarih]) diyor ki:**
> "[ilgili alıntı]"

**Açık:** [Yok — politika zaten karşılıyor | Kısmi — politika X'i ele alıyor ama Y'yi değil | Tam — politika çelişiyor ya da hiç değinmiyor]

**Gereken değişiklik:** [somut — "X hakkında paragraf ekle", "politikayı güncelle" değil]

**Politika sahibi:** [kütüphaneden]
```

Düzenleme iki türlü okunabiliyorsa ikisini de yaz ve "tartışmalı — içtihadı ve kurum kararlarını kontrol et" diye işaretle; aranacak sorguyu ver (`tr_ictihat_ara`, `tr_semantik_ara(kurum=…)`), karar numarasını ezberden yazma.

### Adım 4: Eşleşmeyen açıklar

```markdown
### Yeni politika gerekli

Gereklilik [N]: [gereklilik]

Bunu karşılayan politika yok. Seçenekler:
- Yeni politika yaz (önerilen sahip: [en yakın konunun sahibi])
- [İlgili politika]ya yeni bölüm olarak ekle
- Politika gerektirmediğine karar ver (tek seferlik uyum işi, sürekli değil)
```

## Girdi türüne göre dallar

### Kural öncesi dalı (görüşe açılmış taslak ya da istişare)

Girdi görüşe açılmış bir taslak, taslaksız bir istişare ya da TBMM'deki bir kanun teklifiyse tam açık kapatma karşılaştırması YAPMA; **ön konumlanma analizi** üret:
- Kural yayımlanırsa (bugün değil) değişmesi muhtemel politikaları say.
- Taslağın konularından biri [Müvekkil]'ın uygulamasıyla görüş vermeyi gerektirecek biçimde kesişiyor mu, işaretle.
- Görüş son tarihini ve `**Default comment decision owner:**`'ı yaz; karar için `/arthurlegal:regulatory-legal-comments`.
- Gereklilik bazında "açık yok" satırları üretme; karşılaştırılacak gereklilik yok. Gelecekteki etkiyi ve dokunacağı politikaları tek paragrafta yaz.

### Olumsuz bulgu dalı (yanlış hedef politikaya karşı karşılaştırma)

Çıkarılan her gereklilik "[adı geçen politikaya] karşı açık yok" çıkıyorsa tam analiz üretme; tek kısa paragrafa indir:

```markdown
## Politika Karşılaştırması: [Düzenleme] — [Politika]

[DÜZENLEME] [POLİTİKA] için değişiklik gerektirmiyor görünüyor. [POLİTİKA] §[X]
[Y]'yi zaten karşılıyor. Bu düzenlemenin gerçekten dokunduğu politikalar
[politika-1] ve [politika-2] — `/arthurlegal:regulatory-legal-policy-diff`'i onlara karşı yeniden çalıştırın.

[Sonraki döngüde — ör. "yıllık politika gözden geçirmesinde"] ya da
[tetikleyici — ör. "kural değişirse ya da geçiş süresi biterse"] yeniden bakın.
```

Bir paragraf, bir öneri, bir yönlendirme notu. Yanlış hedefe karşı olumsuz bulgu bir yönlendirme sorunudur, uyum analizi değildir.

### Açık dalı (en az bir açık bulunan yayımlanmış kural)

Aşağıdaki tam çıktı. Ayrıntılı biçim gerçekten açık bulan karşılaştırmalar içindir.

## Çıktı

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

## Politika Karşılaştırması: [Düzenleme adı]

**Düzenleme:** [araçtan dönen citation, bağlantı]
**Yürürlük:** [tarih; geçiş hükmü varsa]
**Kural durumu:** [doğrulandı — kaynak, tarih | doğrulanmadı — yukarıdaki başlığa bakın]
**Çıkarılan gereklilik:** [N]

### Sonuç

[N açık [tarih]e kadar işlem gerektiriyor — ilk üçü: X, Y, Z]

### Özet

| # | Gereklilik | Etkilenen politika | Açık | Sahip |
|---|---|---|---|---|
| 1 | [kısa] | [politika ya da "yok"] | Yok/Kısmi/Tam | [ad] |

### Ayrıntılı karşılaştırmalar

[Adım 3'teki bloklar]

### Gereken yeni politikalar

[Adım 4'ten, varsa]

### Açık olmayan gereklilikler

[Liste — neyin zaten karşılandığını bilmek işe yarar]

---

**Atıfları doğrula.** Yukarıdaki künyeler ve politika atıfları yapay zekâ desteğiyle üretildi. Bir gerekliliğe dayanarak işlem yapmadan önce kuralı Resmî Gazete, mevzuat.gov.tr ya da kurumun sitesinden doğruluk, yürürlük tarihi ve güncel durum bakımından kontrol et. Her gereklilikteki kaynak etiketi künyenin nereden geldiğini gösterir; `doğrula` etiketliler önce kontrol edilir.
```

## Ayar eksikse

- **Politika kütüphanesi boş:** her gerekliliği varsayılan olarak "politika eşleşmesi yok" işaretle ve ekle: "Profilinizdeki `## Policy library` boş; bu yüzden her gereklilik yeni politika açığı olarak işaretlendi. Bunları karşılayan politikalarınız varsa `/arthurlegal:regulatory-legal-cold-start-interview --redo` ile ya da profili düzenleyerek kütüphaneye ekleyin ve karşılaştırmayı yeniden çalıştırın."
- **Eşleşen politikanın sahibi yok:** Özet tablosunda Sahip hücresini boş bırak ve ekle: "[Liste] için politika sahibi tanımlı değil. gap-surfacer'ın yönlendirebilmesi için `## Policy library` tablosunun Owner sütununu doldurun."

Kütüphane doluysa ve sahipler tanımlıysa ayardan söz etme.

## Devir

gap-surfacer'a: her Kısmi ya da Tam açık, sahibi ve son tarihiyle izlenen bir kayıt olur (`status_verified` Adım 0'a göre; kapsam sınırı varsa başlığıyla).

## Kapanış

Profildeki `## Outputs` karar ağacıyla bitir; seçenekleri bu çıktıya uyarla (politika taslağını yaz → `/arthurlegal:regulatory-legal-policy-redraft`, eskale et, olgu topla, izle ve bekle, başka bir şey). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Politika güncellemelerini yazmaz; neyin güncellenmesi gerektiğini bulur. Taslak için `/arthurlegal:regulatory-legal-policy-redraft` ya da insan.
- Belirsiz düzenleyici metni kesin olarak yorumlamaz. İki türlü okunabiliyorsa söyler ve avukata işaretler.
- Tutar ve eşikleri sabitlemez; dönemsel güncellenen her rakam için güncel değerin teyidini ister.

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
| AZ duzenleyici degisiklik takibi — akt statusu degistiyse (`Legv olunmus`) ardil akti bul | `/arthurlegal:legal-research-az-mevzuat` |
| karsilastirmali regulasyon literaturu — **ikincil**, mevzuat yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
