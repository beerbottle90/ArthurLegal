---
name: firm-operations-masak-kontrol
description: >
  5549 sayılı Kanun ve Tedbirler Yönetmeliği uyarınca kapsam testi (serbest avukat
  yalnız sayılan finansal işlemlerde yükümlüdür), kimlik tespiti, gerçek faydalanıcı,
  sıkılaştırılmış tedbir, şüpheli işlem değerlendirmesi ve sekiz yıllık muhafaza.
  Sonuç: KAPSAM DIŞI / ✓ TAMAM / 🟠 İNCELE / ⛔ İŞLEM YOK.
user-invocable: true
---

# MASAK Kontrol — Müşterinin Tanınması

## Tetikleyici

- `/arthurlegal:firm-operations-conflict-check` sonrasında, iş kabulünden önce
- Mevcut işte avukatın müvekkil adına bir finansal işlemi gerçekleştirmesi gündeme geldiğinde
- Önceki kimlik bilgilerinin yeterliliğinden veya doğruluğundan şüphe doğduğunda

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- SUÇ GELİRLERİNİN AKLANMASININ ÖNLENMESİ HAKKINDA KANUN (Kanun No. 5549, RG 18.10.2006/26323) m. 2, m. 3, m. 4, m. 8, m. 13, m. 14
- SUÇ GELİRLERİNİN AKLANMASININ VE TERÖRÜN FİNANSMANININ ÖNLENMESİNE DAİR TEDBİRLER HAKKINDA YÖNETMELİK (Cumhurbaşkanlığı / Bakanlar Kurulu Yönetmeliği No. 200713012, RG sayı 26751) m. 4, m. 5, m. 6, m. 7, m. 17/A, m. 22, m. 26/A, m. 28, m. 29 — kısaca "Yön."
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 35, m. 36
- TÜRK CEZA KANUNU (Kanun No. 5237, RG sayı 25611) m. 282

⚠️ **MALİ SUÇLARI ARAŞTIRMA KURULU GENEL TEBLİĞİ (SIRA NO: 5) (Tebliğ No. 12073, RG 09.04.2008/26842)** avukat yükümlülüğünün dayanağı **değildir**. Konusu, Yönetmelik m. 26 uyarınca **basitleştirilmiş tedbirlerdir** (metnin ilk sayfası 24.09.2026'da okundu). Serbest avukatlar 5549'a 2008'de değil, 7262 sayılı Kanunla (2020) girdi; bu hüküm AYM'nin 18.01.2024 tarihli, E. 2021/28, K. 2024/11 sayılı kararıyla iptal edildi, bugünkü metin 7521 sayılı Kanunla (2024) geldi (5549 m. 2 dipnotları).

## Akış

### 1. Kapsam testi (5549 m. 2/1-d; Yön. m. 4/1-ş)
Serbest avukat **yalnız** şu işlere ilişkin **finansal işlemlerin gerçekleştirilmesiyle** sınırlı olarak yükümlüdür:
- taşınmaz alım satımı
- sınırlı ayni hak kurulması ve kaldırılması
- şirket, vakıf ve dernek kurulması, birleştirilmesi, idaresi, devredilmesi ve tasfiyesi
- banka, menkul kıymet ve her türlü hesap ile bu hesaplardaki varlıkların idaresi

**Hariç:** Av. K. m. 35'in birinci ve üçüncü fıkrası ile alternatif uyuşmazlık çözüm yolları kapsamında yürütülen mesleki faaliyetler sırasında edinilen bilgiler. Yükümlülük savunma hakkı ve hukuki dinlenilme hakkı bakımından diğer kanunlara aykırı olamaz; yalnız avukatların yapabileceği işlerde Av. K. m. 36 (sır saklama) saklıdır.

| Sonuç | Karar |
|---|---|
| İş, yukarıdaki finansal işlemleri **gerçekleştirmeyi** içermiyor (dava vekilliği, mütalaa, sözleşme incelemesi, arabuluculuk) | **KAPSAM DIŞI**: gerekçeyi yaz, `/arthurlegal:firm-operations-sanctions-check` ile devam et |
| İçeriyor | 2. adıma geç |
| Belirsiz (ör. şirket kuruluşunda sermaye hesabını avukat mı yönetecek?) | 🟠 İNCELE → Yönetici Ortak |

Kapsam dışı iş için de büro politikası temel kimlik kaydı isteyebilir. Bu 5549 yükümlülüğü değil, büro kuralıdır (`firm-profile.md`).

### 2. Kimlik tespiti ne zaman yapılır (Yön. m. 5)
- Sürekli iş ilişkisi kurulurken **tutar gözetmeksizin** (m. 5/1-a)
- İşlem tutarı veya birbiriyle bağlantılı işlemlerin toplamı Yönetmelikteki eşiğe ulaşınca (m. 5/1-b). 24.09.2026 metninde eşik 185.000 TL'dir; eşik Cumhurbaşkanı kararlarıyla değişir, her kullanımda güncel metni çek.
- Şüpheli işlem bildirimini gerektiren durumlarda tutar gözetmeksizin (m. 5/1-d)
- Önceki kimlik bilgilerinin yeterliliğinden veya doğruluğundan şüphe varsa tutar gözetmeksizin (m. 5/1-e)

Tespit **iş ilişkisi kurulmadan veya işlem yapılmadan önce** tamamlanır (m. 5/2). Sürekli iş ilişkisinde ilişkinin amacı ve mahiyeti hakkında bilgi alınır (m. 5/3).

### 3. Kimlik bilgileri ve teyit

**Gerçek kişi (Yön. m. 6):** ad, soyad, doğum tarihi, uyruk, kimlik belgesinin türü ve numarası, adres, imza örneği, iş ve meslek bilgisi, varsa telefon, faks ve e-posta; Türk vatandaşı için TCKN, yabancı için doğum yeri.
- Teyit belgesi: Türk uyruklu için nüfus cüzdanı, sürücü belgesi veya pasaport (ve TCKN taşıyan, özel kanununda resmi kimlik hükmünde sayılan belgeler); yabancı için pasaport, ikamet belgesi veya Bakanlıkça uygun görülen belge (m. 6/2).
- Belgenin aslı veya noter onaylı sureti görülür; okunabilir fotokopisi veya elektronik görüntüsü alınır ya da bilgiler kaydedilir (m. 6/2).
- Sürekli iş ilişkisinde adres teyidi: yerleşim yeri belgesi, son üç ay içinde düzenlenmiş abonelik faturası, kamu kurumu belgesi vb. (m. 6/3).

**Ticaret siciline kayıtlı tüzel kişi (Yön. m. 7):** unvan, ticaret sicil numarası, vergi kimlik numarası, faaliyet konusu, açık adres, telefon, varsa faks ve e-posta; ayrıca temsile yetkili kişinin kimlik bilgileri ve imza örneği.
- Teyit: unvan, sicil numarası, faaliyet konusu ve adres için tescil belgeleri; vergi kimlik numarası için Gelir İdaresi belgeleri; temsil yetkisi için tescil belgeleri (m. 7/2-3).

**Gerçek faydalanıcı (Yön. m. 17/A):**
- Tüzel kişiliğin **%25'ini aşan** hisseye sahip gerçek kişi ortaklar (m. 17/A/2). Ölçüt "%25 ve üzeri" değildir.
- Bu ortağın gerçek faydalanıcı olmadığından şüphe varsa ya da böyle bir ortak yoksa: tüzel kişiyi nihai olarak kontrol eden gerçek kişi veya kişiler (m. 17/A/3).
- Yine tespit edilemezse: ticaret sicilinde kayıtlı en üst düzey icra yetkisine sahip gerçek kişi veya kişiler "üst düzey yönetici" sıfatıyla (m. 17/A/4).
- %25'i aşan hisseye sahip **tüzel kişi** ortakların kimliği de m. 7'ye göre tespit edilir (m. 17/A/7). Kimlik bilgilerini içeren noter onaylı imza sirküleri kullanılabilir (m. 17/A/6).

### 4. Yüksek risk: sıkılaştırılmış tedbirler (Yön. m. 26/A)
Risk temelli yaklaşımla yüksek riskli bulunan durumda, riskle orantılı olarak şunların biri, birkaçı veya tamamı uygulanır: müşteri ve gerçek faydalanıcı hakkında ilave bilgi ve daha sık güncelleme; iş ilişkisinin mahiyeti hakkında ilave bilgi; işleme konu malvarlığının ve fonların kaynağı hakkında bilgi; işlemin amacı; iş ilişkisinin **üst seviyedeki görevlinin onayına** bağlanması (büroda Yönetici Ortak); sıkı gözetim.

Uygulama örnekleri (mevzuat listesi değildir): karmaşık veya yurt dışı ortaklık zinciri, siyasi nüfuz sahibi kişi bağlantısı, nakit yoğun işlem, müvekkilin profiline uymayan işlem büyüklüğü.

### 5. Tespit yapılamıyorsa (Yön. m. 22)
Kimlik tespiti yapılamıyor ya da iş ilişkisinin amacı hakkında yeterli bilgi edinilemiyorsa **iş ilişkisi kurulmaz, talep edilen işlem yapılmaz** (m. 22/1). Önceki bilgilerden şüphe nedeniyle gereken teyit yapılamazsa iş ilişkisi **sona erdirilir** (m. 22/2). İki hâlin şüpheli işlem olup olmadığı ayrıca değerlendirilir (m. 22/3).

### 6. Şüpheli işlem değerlendirmesi
- **Ölçüt:** işleme konu malvarlığının yasa dışı yollardan elde edildiğine veya yasa dışı amaçla kullanıldığına dair **bilgi, şüphe veya şüpheyi gerektirecek bir husus** (5549 m. 4/1).
- **Süre:** şüphenin oluştuğu tarihten itibaren **en geç on iş günü** içinde Başkanlığa bildirim (Yön. m. 28/2).
- **Açıklama yasağı:** bildirimde bulunulduğu veya bulunulacağı, yükümlülük denetimi yapan denetim elemanları ve yargılamadaki mahkemeler dışında, **müvekkil dahil hiç kimseye** açıklanmaz (5549 m. 4/2; Yön. m. 29/1). Yasak, bildirime herhangi bir şekilde vakıf olan tüm personeli kapsar (Yön. m. 29/2). İhlalin cezası bir yıldan üç yıla kadar hapis ve beş bin güne kadar adli para cezasıdır (5549 m. 14/1).
- Bildirim yükümlülüğünü yerine getiren hukuki ve cezai bakımdan sorumlu tutulamaz (Yön. m. 29/4).
- Bilgi, Av. K. m. 35'in birinci veya üçüncü fıkrasındaki faaliyetten ya da alternatif uyuşmazlık çözüm yolu faaliyetinden edinildiyse yükümlülük dışındadır (5549 m. 2/1-d).
- Karar: büroda bu işi yürüten kişi (`firm-profile.md` → MASAK sorumlusu) + Yönetici Ortak. Avukatlar için uyum görevlisi atama zorunluluğu bu pakette doğrulanmadı. Değerlendirme notu matter klasörüne değil, **erişimi kısıtlı uyum kaydına** yazılır.

### 7. Muhafaza (5549 m. 8)
Belgeler düzenleme tarihinden, defter ve kayıtlar son kayıt tarihinden, **kimlik tespitine ilişkin belgeler son işlem tarihinden** itibaren **sekiz yıl** saklanır ve istenirse yetkililere ibraz edilir. Matter'ın kapanması süreyi başlatmaz; son işlem tarihine bak. Muhafaza yükümlülüğünün ihlali de adli cezaya tabidir (5549 m. 14/1).

### 8. Yaptırım (bilgi)
- 5549 m. 3 ve m. 6 yükümlülüklerinin ihlali ile m. 4/1 ihlali: idari para cezası (5549 m. 13/1). Tutarlar metinde yazılıdır; güncel tutarı her kullanımda çek.
- 5549 m. 4/2, m. 7 ve m. 8 ihlali: adli ceza (5549 m. 14/1).
- Aklama suçu TCK m. 282'dedir. Suçun belli bir meslek sahibi tarafından mesleğin icrası sırasında işlenmesi hâlinde hapis cezası yarı oranında artırılır (m. 282/3).

## Çıktı

```markdown
[ÜST BAŞLIK — MASAK KONTROL NOTU — DAHİLİ]

# MASAK Kontrol — [Müvekkil takma adı] — GG.AA.YYYY

## Kapsam (5549 m. 2/1-d)
KAPSAM DIŞI / KAPSAMDA — gerekçe: [iş türü]

## Kimlik tespiti (kapsamdaysa)
- Tip: gerçek / tüzel
- Teyit belgesi: [tür] — aslı veya noter sureti görüldü: evet / hayır
- Gerçek faydalanıcı: [takma ad] — yöntem: %25'i aşan pay / nihai kontrol / üst düzey yönetici
- Sıkılaştırılmış tedbir: gerekmedi / uygulandı: [hangileri] — onay: [Yönetici Ortak]

## Sonuç
✓ TAMAM / 🟠 İNCELE / ⛔ İŞLEM YOK (Yön. m. 22)
Muhafaza bitişi: son işlem + 8 yıl (5549 m. 8)
```

Şüpheli işlem değerlendirmesi bu notta **yer almaz**; uyum kaydına ayrı yazılır.

## Hatalar

- **Dava vekilliğini kapsam içi saymak**: avukat yalnız sayılan finansal işlemlerde yükümlüdür (5549 m. 2/1-d).
- **Kapsamdaki işte "ben sadece danışmanım" demek**: finansal işlemi avukat gerçekleştiriyorsa iş kapsam içidir.
- **5 yıl saklamak**: süre sekiz yıldır (5549 m. 8).
- **"%25 ve üzeri" pay**: ölçüt %25'i **aşan** paydır (Yön. m. 17/A/2).
- **Müvekkile "sizi bildirdik" demek**: 5549 m. 4/2 ve m. 14/1.
- **MASAK Genel Tebliği (Sıra No: 5)'i dayanak göstermek**: konusu basitleştirilmiş tedbirlerdir.

Ayrıntı: `${CLAUDE_PLUGIN_ROOT}/references/masak-kimlik-tespit-rehberi.md`

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
> **Meslek sirri (Av. K. m. 36):** uc MCP de PUBLIC arama aracidir — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| yabanci karsi tarafli veya AZ baglantili yeni is alimi — mevzuat kapsaminin gercekten var olup olmadigini once dogrula | `/arthurlegal:legal-research-kaynak-secimi` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
