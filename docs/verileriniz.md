# Verileriniz nereye gider

[English](your-data.md) · [Azərbaycan dili](melumatlariniz.md)

ArthurLegal ücretsiz ve açık kaynaktır; sizinle bir hizmet sözleşmesi yapmaz. Bu yüzden aşağıdakiler bir sözleşme
taahhüdü değil, **tasarımın kendisidir**: her satırın dayanağı açık koddadır ve denetlenebilir.

## Tek tabloda

| Ne | Nerede durur | Kime gider |
|---|---|---|
| Sorunuz ve Claude'un cevabı | Claude'da (Anthropic). Masanın geçmişi ayrıca kendi cihazınızda: bilgisayarınızda ArthurLegal kuruluysa kurulumun klasöründe, değilse masanın tarayıcı deposunda; 90 gün sonra silinir. | Anthropic'e, Claude kullanımınızın kendi koşullarıyla (aşağıda "Claude ayarınız"). |
| Araştırma isteği (arama sözcükleri, kanun ve madde numarası, karar künyesi) | ArthurLegal sunucusu arama metnini saklamaz ve istek kaydı tutmaz. İstisnalar (Alman ve Azerbaycan araçlarının kısa önbelleği) [sunucunun gizlilik belgesinde](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md). | ArthurLegal MCP sunucusuna (Fly.io, Amsterdam), oradan yalnız gerekli parametrelerle resmî kaynağa: mevzuat.gov.tr, Resmî Gazete, Yargıtay, Danıştay, AYM ve kurumlar. Anlamsal aramada arama metni anlam hesabı için Voyage AI'a gider. |
| Müvekkil belgesi (ArthurMask ile) | Asıl belge ve gerçek adlar, numaralar yalnız bilgisayarınızda. | Claude'a yalnız etiketli metin gider (ör. `{{KİŞİ-01}}`). Etiketin gerçek karşılığı Claude'a gönderilmez. |
| UYAP | ArthurLegal UYAP'a hiçbir şey yazmaz; UYAP'ta açtığınız listeleri bilgisayarınızda okur. | Claude'a dosya numaraları etiketli gider; gerçek değerler yalnız sizin ekranınızda görünür. |
| ArthurLegal Hafıza (Beyin) | Bilgisayarınızda. | Claude'a, sohbet açılırken yalnız tercihleriniz, düzeltmeleriniz ve son oturum özeti. |
| Tapu (TKGM) parsel sorgusu | Parsel kimliği ve verisi sunucunun belleğinde en çok 24 saat; diske ya da kayda yazılmaz. | TKGM Parsel Sorgu'ya, sunucudan. |
| Masanın dili ve teması | Cihazınızda. | Hiçbir yere. |

## Claude ayarınız

ArthurLegal sizin Claude hesabınızla çalışır ve bu hesabın ayarlarını göremez, değiştiremez. Claude'u **Free, Pro
ya da Max** planıyla kullanıyorsanız, **Ayarlar › Gizlilik** bölümündeki model geliştirme ayarı açık olduğu sürece yeni
sohbetleriniz Anthropic'in modellerini geliştirmede kullanılabilir. Müvekkil bilgisi girmeden önce bu ayarı kontrol
edin ve müvekkil belgesini ArthurMask'ten geçirin. Team, Enterprise ve API kullanımı Anthropic'in ticari koşullarına
tabidir. Kaynak: [Anthropic, model geliştirme gizlilik ayarı](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings).

## Çıktı hakkında

- ArthurLegal'in ve Claude'un çıktısı **hukuki görüş değildir**.
- Çıktı **hatalı ya da eksik olabilir**.
- **Avukat kullanmadan önce resmî kaynaktan doğrular**; mesleki sorumluluk avukattadır.

Masadaki atıf teyidi, madde numarasının ve başlığının resmî metinde bulunduğunu gösterir. Maddenin, cümlede ona
yüklenen içeriği (hakkın sahibi, şart, süre, sonuç) gerçekten söyleyip söylemediğini avukat okur; masanın "Metni
göster" düğmesi cümleyi ve resmî metni yan yana açar. Bir kaynak veri vermezse ArthurLegal boşluğu doldurmaz,
şu satırı yazar: `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>`.

## Denetlemek isterseniz

- Uzak sunucunun ayrıntılı gizlilik belgesi: [arthurlegal-mcp/PRIVACY.md](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md)
- ArthurMask'in nasıl çalıştığı: [arthur-mask](https://github.com/beerbottle90/arthur-mask)
- Bu depo: kurulumun ve masanın bütün kodu.

Bu sayfa her sürümle birlikte gözden geçirilir; değişiklik geçmişi depodadır.
