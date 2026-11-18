# Mahkeme Türü Profili — Asliye Ticaret Mahkemesi

> `mahkeme-profili.md` ile birlikte okunur. Madde numaraları 27.09.2026'da ArthurLegal MCP ile çekilen metne dayanır; karar gövdesine girmeden önce yeniden çekilir.

## Kim kullanır

- **Hâkim ve heyet:** asliye ticaret mahkemesinde bir başkan ve yeteri kadar üye bulunur. Dava değeri bir milyon Türk lirasının üzerindeki dava ve işler ile değere bakılmaksızın iflas, konkordato ve yeniden yapılandırma işleri, TTK'da hâkimin kesin olarak karara bağlayacağı işler, şirketler ve kooperatifler hukukundan doğan genel kurul kararlarının iptali ve butlanı, organ sorumluluğu, organ azli ve geçici organ atanması, fesih, infisah ve tasfiye davaları ile tahkime ilişkin belirli işler heyetçe görülür; heyet işlerinde ihtiyati haciz ve tedbir de heyetçe karara bağlanır; diğer işler hâkimlerden biri tarafından görülür; parasal sınır HMK ek m. 1'e göre artırılır (5235 s.K. m. 5/3).
- Plugin: `hukuk-hakim`, `hukuk-kalem`; araştırma için `yargi-arastirma`.

## Görev ve yetki

- **Ticari dava:** her iki tarafın ticari işletmesiyle ilgili hususlardan doğan hukuk davaları ile tarafların tacir olup olmadığına bakılmaksızın TTK'da ve TTK m. 4/1'de sayılan diğer düzenlemelerde öngörülen hususlardan doğan davalar (TTK m. 4/1).
- **Görev:** dava olunan şeyin değer veya tutarına bakılmaksızın asliye ticaret mahkemesi tüm ticari davalar ile ticari nitelikteki çekişmesiz yargı işlerine bakar (TTK m. 5/1). Asliye ticaret ile asliye hukuk ve diğer hukuk mahkemeleri arasındaki ilişki görev ilişkisidir (m. 5/3). Asliye ticaret bulunmayan yargı çevresinde görev kuralına dayanılmamış olması görevsizlik gerektirmez (m. 5/4).
- **Usul:** deliller ve sunulması HMK'ya tabidir; miktar veya değeri bir milyon Türk lirasını geçmeyen ticari davalarda basit yargılama usulü uygulanır; sınır HMK ek m. 1'e göre artırılır (TTK m. 4/2).
- **Konkordato:** iflasa tabi borçlu için İİK m. 154'te yazılı yerdeki, iflasa tabi olmayan borçlu için yerleşim yerindeki asliye ticaret mahkemesi görevli ve yetkilidir (İİK m. 285).
- **Yetki:** genel kurallar (HMK m. 6); kesin olmayan yetki itirazı cevap dilekçesinde (HMK m. 19). İflas davaları için yetki sözleşmesi yapılamaz; iflas davası borçlunun muamele merkezinin bulunduğu yer ticaret mahkemesinde açılır (İİK m. 154/3).

## Tipik dosya türleri

Ticari alacak, itirazın iptali, menfi tespit ve istirdat; şirket genel kurul kararlarının iptali; yönetim organı sorumluluğu; haksız rekabet ve fikri mülkiyet kaynaklı ticari davalar (TTK m. 4/1-d kapsamı); konkordato; iflas; ihtiyati haciz; hakem kararı ve tahkim işleri.

## Dava şartı arabuluculuk

- Ticari davalardan konusu bir miktar para olan alacak, tazminat, itirazın iptali, menfi tespit ve istirdat davalarında dava açılmadan önce arabulucuya başvurulmuş olması dava şartıdır; arabulucu başvuruyu görevlendirildiği tarihten itibaren altı hafta içinde sonuçlandırır, zorunlu hâlde en çok iki hafta uzatılabilir (TTK m. 5/A).
- Son tutanak dilekçeye eklenmemişse bir haftalık kesin süre verilir, arabulucuya hiç başvurulmamışsa dava dava şartı yokluğundan usulden reddedilir (HUAK m. 18/A/2).
- Arabuluculuk bürosuna başvurudan son tutanağa kadar zamanaşımı durur, hak düşürücü süre işlemez; dava açılmadan önce verilen ihtiyati tedbir ve ihtiyati haciz için dava açma süresi de bu dönemde işlemez (HUAK m. 18/A/15, 18/A/16). Tahkim sözleşmesi varsa dava şartı arabuluculuk hükümleri uygulanmaz (m. 18/A/18).

## Usul akışı

1. Dava şartı arabuluculuk ve gider avansı kontrolü (`/hukuk-hakim:dava-sarti-kontrolu`).
2. Değer bir milyon TL'yi (güncel sınırı çekin) geçmiyorsa basit yargılama: mümkünse dosya üzerinden karar, ilk duruşmada dava şartları ve ilk itirazlar, iki duruşmada tahkikat, aralar bir ay (HMK m. 320).
3. Yazılı yargılamada dilekçeler, ön inceleme ve tahkikat (HMK m. 127, 136, 137-140); duruşma aralığı (m. 147/3).
4. Tahkim itirazı ilk itirazdır ve cevap dilekçesinde ileri sürülür (HMK m. 116/1-b, 117/1).
5. Heyet işi mi tek hâkim işi mi: her dosyada 5235 s.K. m. 5/3 ölçütü, dava tarihindeki değere göre.

## Konkordato ve iflas takvimi

- Belgeler eksiksizse mahkeme derhâl geçici mühlet verir ve geçici komiser görevlendirir; geçici mühlet üç aydır, en çok iki ay uzatılabilir, toplam beş ayı geçemez; bu kararlara karşı kanun yolu yoktur (İİK m. 287).
- Kesin mühlet kararı geçici mühlet içinde verilir; başarı mümkünse bir yıllık kesin mühlet, güçlük arz eden özel durumlarda altı aya kadar uzatma (İİK m. 289).
- İflas ve konkordato işleri adli tatilde de görülür (HMK m. 103/1-e).

## Kritik süreler

| İşlem | Süre | Madde |
|---|---|---|
| Ticari arabuluculuk | 6 hafta (+ en çok 2 hafta) | TTK m. 5/A/2 |
| Son tutanağın sunulması | 1 hafta, kesin | HUAK m. 18/A/2 |
| İhtiyati haczi tamamlayan dava veya takip | haczin uygulanmasından veya tutanağın tebliğinden 7 gün | İİK m. 264/1 |
| İhtiyati haciz kararına itiraz | 7 gün; itiraz kararına istinaf, BAM kararı kesin | İİK m. 265 |
| İhtiyati tedbire itiraz | 1 hafta | HMK m. 394/2 |
| Geçici mühlet | 3 ay + en çok 2 ay | İİK m. 287 |
| Kesin mühlet | 1 yıl + en çok 6 ay | İİK m. 289 |
| İstinaf | tebliğden 2 hafta | HMK m. 345 |

## 2026 değişiklikleri (7589 s.K., RG 31.07.2026)

- Belirsiz alacak davası maddesi kaldırıldı (HMK m. 107; eski davalar için geçici m. 1/10); kısmi davada bir defaya mahsus artırım (HMK m. 109/4).
- Kanuni faiz: TBK ve TTK'ya göre faiz ödenmesi gereken ve miktarı sözleşmeyle belirlenmemiş hâllerde TCMB'nin önceki yılın 31 Aralık reeskont oranının yüzde sekseni (3095 s.K. m. 1).
- Birleştirme ve ayırma kararlarına kanun yolu (HMK m. 168).

## Sık usul riskleri (genel)

- 🔴 Dava şartı arabuluculuk kapsamındaki para alacağında son tutanak aranmadan tebligata çıkılması.
- 🔴 Heyetle görülmesi gereken işin tek hâkimle karara bağlanması (5235 s.K. m. 5/3).
- 🟠 Tahkim itirazının süresinden sonra ileri sürüldüğü hâlde dinlenmesi veya süresinde ileri sürüldüğü hâlde incelenmemesi (HMK m. 117/1).
- 🟠 Basit yargılama sınırının dava tarihindeki güncel tutara göre belirlenmemesi (TTK m. 4/2).
- 🟡 Ticari defter ve bilirkişi incelemesinde sürelerin izlenmemesi (HMK m. 274; `bilirkisi-rapor-izleyici`).

## Kalem iş akışı

- Tüzel kişilere ve avukatlara elektronik tebligat zorunludur (7201 s.K. m. 7/a).
- Konkordato ve iflasta ilan ve bildirimler; komiser raporlarının takibi: [DOLDUR — yerel uygulama].
- Harç ve gider avansı (HMK m. 120; 492 s.K. m. 28/a, 32).
- Skill'ler: `/hukuk-kalem:tensip-zapti`, `/hukuk-kalem:tebligat`, `/hukuk-kalem:harc-hesabi`, `/hukuk-kalem:kesinlesme-serhi`.

## Hangi skill ve izleyici ne zaman

| Durum | Skill / izleyici |
|---|---|
| Dava şartı, heyet/tek hâkim ayrımı | `/hukuk-hakim:dava-sarti-kontrolu` |
| İhtiyati haciz / tedbir | `/hukuk-hakim:ihtiyati-tedbir` |
| Bilirkişi (ticari defter, hesap) | `/hukuk-hakim:bilirkisi-raporu-denetimi`, `bilirkisi-rapor-izleyici` |
| Karar | `/hukuk-hakim:gerekceli-karar`, `/yargi-arastirma:emsal-tarama` |
| Takip | `durusma-hazirlik`, `kanun-yolu-kesinlesme-izleyici`, `makul-sure-izleyici` |

## Veri hassasiyeti

- Ticari sır ve banka bilgileri; bilirkişi, kendisine tevdi edilen bilgi ve belgelerin gizliliğini sağlamakla yükümlüdür (6754 s.K. m. 3/5).
- Gizli duruşma yalnız HMK m. 28/2 koşullarında.
- Gerçek kişi ortak ve yöneticilerin kişisel verileri çıktıda maskeli kalır.

## Mahkemeye özgü alanlar

- Heyet yapısı ve iş dağılımı (başkan / üyeler): [DOLDUR]
- Deniz ticareti veya başka ihtisas görevlendirmesi var mı (TTK m. 5/2): [DOLDUR]
- Konkordato dosya sayısı ve komiser havuzu: [DOLDUR]
- Bağlı bölge adliye mahkemesi ticaret daireleri: [DOLDUR]

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): TTK m. 4, 5, 5/A; 5235 s.K. m. 5; HMK m. 6, 19, 28, 103, 107, 109, 116, 117, 120, 127, 136, 137, 138, 139, 140, 147, 168, 274, 320, 345, 394, ek m. 1; HUAK m. 18/A; İİK m. 154, 264, 265, 285, 287, 289; 3095 s.K. m. 1; 492 s.K. m. 28, 32; 6754 s.K. m. 3; 7201 s.K. m. 7/a.*
