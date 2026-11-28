# Verileriniz nereye gider

[English](your-data.md) · [Azərbaycan dili](melumatlariniz.md)

ArthurLegal ücretsiz ve açık kaynaktır; sizinle bir hizmet sözleşmesi yapmaz. Bu yüzden aşağıdakiler bir sözleşme
taahhüdü değil, **tasarımın kendisidir**: her satırın dayanağı açık koddadır ve denetlenebilir.

ArthurLegal, kurulumda seçtiğiniz yapay zekâ uygulamasının içinde çalışır: Claude Desktop, ChatGPT masaüstü
uygulaması ya da ikisi. Tablo ikisini de kapsar; ChatGPT'ye özgü olanlar ayrıca yazılıdır.

## Tek tabloda

| Ne | Nerede durur | Kime gider |
|---|---|---|
| Sorunuz ve Claude'un cevabı | Claude'da (Anthropic). Masanın geçmişi ayrıca kendi cihazınızda: bilgisayarınızda ArthurLegal kuruluysa kurulumun klasöründe, değilse masanın tarayıcı deposunda; 90 gün sonra silinir. | Anthropic'e, Claude kullanımınızın kendi koşullarıyla (aşağıda "Claude ayarınız"). |
| Sorunuz ve ChatGPT'nin cevabı (ChatGPT'yi seçtiyseniz) | ChatGPT'de (OpenAI). Masanın geçmişi ayrıca bilgisayarınızda, kurulumun klasöründe; 90 gün sonra silinir. | OpenAI'a, ChatGPT kullanımınızın kendi koşullarıyla (aşağıda "ChatGPT ayarınız"). Sorunuzla birlikte ChatGPT'nin araçlardan aldığı sonuçlar da (mevzuat, içtihat, kararlar gibi resmî kaynaklardan gelen metinler) ChatGPT'ye gider. |
| Araştırma isteği (arama sözcükleri, kanun ve madde numarası, karar künyesi) | ArthurLegal sunucusu arama metnini saklamaz ve istek kaydı tutmaz. İstisnalar (Alman ve Azerbaycan araçlarının kısa önbelleği) [sunucunun gizlilik belgesinde](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md). | ArthurLegal MCP sunucusuna (Fly.io, Amsterdam), oradan yalnız gerekli parametrelerle resmî kaynağa: mevzuat.gov.tr, Resmî Gazete, Yargıtay, Danıştay, AYM ve kurumlar. Anlamsal aramada arama metni anlam hesabı için Voyage AI'a gider. |
| Müvekkil belgesi (ArthurMask ile) | Asıl belge ve gerçek adlar, numaralar (ArthurMask'in gerçek adlar tablosu) yalnız bilgisayarınızda. Gerçek adlar tablosu siz silene kadar durur; maskeli ara kopyalar 30 gün sonra kendiliğinden silinir. | Claude'a ya da ChatGPT'ye yalnız etiketli metin gider (ör. `{{KİŞİ-01}}`). Etiketin gerçek karşılığı yapay zekâya gönderilmez. |
| UYAP | ArthurLegal UYAP'a hiçbir şey yazmaz; UYAP'ta açtığınız listeleri bilgisayarınızda okur. | Claude'a ya da ChatGPT'ye dosya numaraları etiketli gider; gerçek değerler yalnız sizin ekranınızda görünür. |
| ArthurLegal Hafıza (Beyin) | Bilgisayarınızda; siz silene kadar durur (ArthurLegal'i kaldırmak da silmez). | Claude'a ya da ChatGPT'ye, sohbet açılırken yalnız tercihleriniz, düzeltmeleriniz ve son oturum özeti. |
| Claude'un hazırladığı dosyalar (Word, Excel ve benzeri) | Bilgisayarınızda, Belgeler içindeki ArthurLegal klasöründe; siz silene kadar durur. | Hiçbir yere. |
| Tapu (TKGM) parsel sorgusu | Parsel kimliği ve verisi sunucunun belleğinde en çok 24 saat; diske ya da kayda yazılmaz. | TKGM Parsel Sorgu'ya, sunucudan. |
| Masanın dili ve teması | Cihazınızda. | Hiçbir yere. |

## Bu bilgisayarda kalan kayıtlar ve nasıl silinir

TBB'nin yapay zekâ rehberi, prompt, çıktı ve yüklenen belgelerin saklama süresi sonunda silinmesini önerir (s. 22).
ArthurLegal'in bilgisayarınızda bıraktığı her kayıt, ne kadar kaldığı ve elle nasıl silineceği:

| Kayıt | Nerede | Ne kadar kalır | Elle silme |
|---|---|---|---|
| Masanın geçmişi (sorular, cevaplar, araştırmalar) | Kurulumun `veri\masa-gecmisi` klasörü (Windows: `%LOCALAPPDATA%\Programs\ArthurLegal`, macOS: `~/Library/Application Support/ArthurLegal`); kurulum yoksa masanın tarayıcı deposu | 90 gün ya da en çok 2.000 kayıt; eskisi kendiliğinden silinir | Masanın Geçmiş ekranında kaydın yanındaki Sil düğmesi ya da Geçmişi temizle |
| İş akışlarım (kaydettiğiniz iş akışları) | Aynı klasör | Süresiz (en çok 200); Geçmişi temizle bunları silmez | Masanın İş akışları ekranında tek tek Sil |
| Claude'un hazırladığı dosyalar | Belgeler içindeki ArthurLegal klasörü | Siz silene kadar | Klasördeki dosyayı silin |
| ArthurLegal Hafıza | Ev klasörünüzdeki `ArthurLegal-Hafiza` (ya da kurulumda seçtiğiniz klasör) | Siz silene kadar; ArthurLegal'i kaldırmak silmez | Klasördeki Markdown dosyalarını silin |
| ArthurMask: maskeli ara kopyalar | Belgeler içindeki ArthurMask klasöründe her dosyanın `maskeli` klasörü (macOS: `~/ArthurMask`) | 30 gün; ArthurMask köprüsü her başladığında süresi dolanlar kendiliğinden silinir | Klasördeki dosyayı silin |
| ArthurMask: gerçek adlar tablosu (kasa), çözülmüş cevaplar, `claude-giden.jsonl` (Claude'a gönderilen maskeli araç yanıtları) ve `kirmizi-hat.jsonl` (kırmızı hat onayları) | Aynı dosyanın klasörü | Siz silene kadar | Dosyanın (davanın) klasörünü silin; ArthurMask'te ayrıca silme düğmesi yok |
| Masanın "Genel web" ayarı (sohbet başına açık ya da kapalı) | Sohbetin kayıtları ve masanın tarayıcı deposu; müvekkil verisi içermez | Sohbetin kayıtları kadar | Sohbetin kayıtlarını silin; ayar onlarla silinir |
| UYAP köprüsünün şifreli arşivi (dosya listeleri, safahat, evrak) | Ev klasörünüzdeki `.arthurlegal\uyap\arsiv` (`arsiv.sqlite` ve şifreli `bloblar`) | Dosya UYAP listelerinde son görüldükten sonra hukuk, icra ve idari dosyada 1.095 gün, ceza dosyasında 730 gün; köprü her başladığında süresi dolanlar silinir | Claude Desktop'u kapatıp `arsiv` klasörünü silin; köprü bir sonraki açılışta boş arşivle başlar |

ArthurLegal bu kayıtları sizin yerinize başka bir sürede silmez; büronuzun saklama ve imha düzeni uzun ya da kısa bir
süre öngörüyorsa silmeyi o düzene göre siz yaparsınız.

## Claude ayarınız

ArthurLegal sizin Claude hesabınızla çalışır ve bu hesabın ayarlarını göremez, değiştiremez. Claude'u **Free, Pro
ya da Max** planıyla kullanıyorsanız, **Ayarlar › Gizlilik** bölümündeki model geliştirme ayarı açık olduğu sürece yeni
sohbetleriniz Anthropic'in modellerini geliştirmede kullanılabilir. Müvekkil bilgisi girmeden önce bu ayarı kontrol
edin ve müvekkil belgesini ArthurMask'ten geçirin. Team, Enterprise ve API kullanımı Anthropic'in ticari koşullarına
tabidir. Kaynak: [Anthropic, model geliştirme gizlilik ayarı](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings).

## ChatGPT ayarınız

Kurulumda ChatGPT'yi seçtiyseniz ArthurLegal sizin ChatGPT hesabınızla, ChatGPT masaüstü uygulamasında çalışır.
ChatGPT'ye sorunuz, ChatGPT'nin araçlardan aldığı sonuçlar (mevzuat, içtihat, kararlar gibi resmî kaynaklardan gelen
metinler) ve ArthurMask'le **maskelenmiş** belge metni gider. ArthurMask'in gerçek adlar tablosu, Hafıza klasörü,
masa geçmişi, UYAP verisi ve Tapu kayıt metni Claude'daki gibi bilgisayarınızda kalır. ArthurLegal'in uzak araştırma
sunucusu soru içeriğini kaydetmez. ChatGPT'nin veri ve gizlilik ayarları, OpenAI'ın hesabınıza uyguladığı koşullara
tabidir; ArthurLegal bunları değiştirmez. Kurulum ChatGPT'ye yalnız ArthurLegal'in sunucularını ve becerilerini
ekler. Müvekkil bilgisi girmeden önce ChatGPT'nin veri ve gizlilik ayarlarını kontrol edin.

Kişisel verilerin yurt dışına aktarılması (6698 sayılı Kişisel Verilerin Korunması Kanunu m. 9) yönünden
değerlendirme, Claude'da olduğu gibi ChatGPT'de de kullanıcıya aittir; müvekkil belgesini ArthurMask'ten geçirin.

KVKK'nın avukat rehberine göre sağlayıcı Türkiye'de olsa da kişisel veri içeren belgeyi bir yapay zekâ aracına
vermek yurt içi aktarım (m. 8) sayılabilir. Arama kutusuna ve araştırma isteğine de müvekkil adı ya da dosya
ayrıntısı yazmayın: ArthurLegal'in araştırma sunucusu Amsterdam'dadır ve anlamsal arama metni Voyage AI'a gider.

## Çıktı hakkında

- ArthurLegal'in, Claude'un ve ChatGPT'nin çıktısı **hukuki görüş değildir**.
- Çıktı **hatalı ya da eksik olabilir**.
- **Avukat kullanmadan önce resmî kaynaktan doğrular**; mesleki sorumluluk avukattadır.

Masadaki atıf teyidi, madde numarasının ve başlığının resmî metinde bulunduğunu gösterir. Maddenin, cümlede ona
yüklenen içeriği (hakkın sahibi, şart, süre, sonuç) gerçekten söyleyip söylemediğini avukat okur; masanın "Metni
göster" düğmesi cümleyi ve resmî metni yan yana açar. Bir kaynak veri vermezse ArthurLegal boşluğu doldurmaz,
şu satırı yazar: `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>`.

## Denetlemek isterseniz

- Uzak sunucunun ayrıntılı gizlilik belgesi: [arthurlegal-mcp/PRIVACY.md](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md)
- ArthurMask'in nasıl çalıştığı: [arthur-mask](https://github.com/beerbottle90/arthur-mask)
- Kurulumun ChatGPT'ye ne yazdığı: [codex_ayari.py](../ArthurLegal-setup/istemci/codex_ayari.py) (ayar dosyasına yalnız ArthurLegal'in satırları yazılır, dosya değiştirilmeden önce yedeklenir; beceriler adı `arthurlegal` ile başlayan klasörlerdir)
- Bu depo: kurulumun ve masanın bütün kodu.

Bu sayfa her sürümle birlikte gözden geçirilir; değişiklik geçmişi depodadır.

<sub>ChatGPT ve OpenAI, OpenAI'ın markalarıdır.</sub>
