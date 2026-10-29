---
name: corporate-legal-written-consent
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

`## Matter workspaces` bölümüne bak. `Enabled` `✗` ise bu paragrafı atla. Açık ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` ya da `practice-level`." Aktif matter'ın `matter.md`'sini yükle; çıktıyı `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter okuma.

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
[Müvekkil] (ticaret unvanı)
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
