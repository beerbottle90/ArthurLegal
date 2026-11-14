# Word'de ArthurLegal

[English](word-guide.md) · [Azərbaycan dili](word-beledcisi.md)

Anthropic'in Word eklentisi, Claude'u belgenin yanında bir panelde açar. ArthurLegal'in araştırma bağlayıcısı
claude.ai hesabınıza bağlıysa, Word'deki Claude da Türk mevzuatını ve içtihadını resmî kaynaktan canlı çeker: maddeyi
belgenin yanında okur, düzeltmeyi izli değişiklik olarak önerir, gerekçesini yorum olarak bırakır. Ayrı bir kurulum
ya da ücret yoktur; Claude aboneliğinizle çalışır.

## Gerekenler

- **Claude planı:** Pro, Max, Team ya da Enterprise.
- **Word sürümü:**
  - Word'ün web sürümü (tarayıcıda, ücretsiz Microsoft hesabıyla da olur), ya da
  - Microsoft 365 aboneliğiyle Windows'ta Word, Version 2205 (build 15202.10000) ya da sonrası, ya da
  - Mac'te Word 16.61 ya da sonrası.
- **Çalışmayanlar:** Word 2016 ve 2019 (kalıcı ya da toplu lisans), iPad ve Android'de Word, `.doc` dosyası (önce
  `.docx` olarak kaydedin). Kalıcı lisanslı Word 2021 ve 2024 resmî sayfada anılmıyor; emin değilseniz Word'ün web
  sürümünü kullanın.

Bilgisayarınızdaki Word eskiyse mağazada eklentiyi hiç görmezsiniz. Bu bir arama hatası değildir; Word'ün web
sürümüyle sorunsuz çalışır.

## Kurulum

1. **ArthurLegal bağlayıcısı:** claude.ai'de Ayarlar › Connectors bölümünde ArthurLegal bağlı olmalı. Bağlı değilse
   **Add custom connector** ile şu adresi ekleyin: `https://arthurlegal-mcp.fly.dev/mcp`
2. **Word'ü açın:** Word'ün web sürümünü (word.cloud.microsoft) ya da Microsoft 365 Word'ü açın ve bir belge açın.
3. **Eklentiyi ekleyin:** **Giriş › Eklentiler** (bazı görünümlerde **Ekle › Eklentiler**) düğmesine basın, aramaya
   `Claude` yazın. Mağazadaki adı **Claude for Microsoft 365**'tir (yayıncı Anthropic); "Claude for Word" diye aranırsa
   çıkmayabilir. **Ekle**'ye basın. Mağaza sayfası:
   [Claude for Microsoft 365](https://marketplace.microsoft.com/en-us/product/office/WA200010725)
4. **Giriş yapın:** sağda açılan Claude panelinde **Claude hesabınızla** giriş yapın. Bu, Microsoft hesabınızdan
   ayrıdır; Claude aboneliğiniz hangi hesaptaysa onu kullanın.

### Büro ya da şirket hesabında eklenti görünmüyorsa

Bazı kuruluşlarda eklenti eklemeyi yönetici açar. Microsoft 365 yönetim merkezinde:

- **Ayarlar › Kuruluş ayarları › Kullanıcıya ait uygulamalar ve hizmetler**: "Kullanıcıların Office Mağazası'na
  erişmesine izin ver" açık olmalı, ya da
- **Ayarlar › Tümleşik uygulamalar › Eklentiler**: Claude for Microsoft 365 aranır ve kuruluşa, kişilere ya da gruplara
  atanır. Kuruluş geneline yayılması 24 saate kadar sürebilir.

Mağaza kapalı tutuluyorsa Anthropic'in Word sayfası, yöneticinin yükleyebileceği bir eklenti dosyası da veriyor
(aşağıdaki kaynaklar).

## Örnek kullanımlar

Önce ilgili metni seçin, sonra panele yazın.

- **Madde incelemesi:** "Bu maddeyi Türk Borçlar Kanunu'na göre incele; dayandığın maddeyi ArthurLegal ile resmî
  metinden çek." Cevabın üstünde **Used … tools** satırı görünür; Claude'un maddeyi ezberden değil araçla çektiğini
  gösterir. Madde metni mevzuat.gov.tr bağlantısıyla gelmelidir.
- **İzli değişiklikle düzeltme:** "Bu maddeyi kanuna uygun olacak şekilde yeniden yaz, değişikliği izli değişiklik
  olarak uygula ve gerekçeyi yorum olarak ekle." Değişiklikler Word'ün kendi **Gözden Geçir** bölmesinde kabul ya da
  reddedilir; geri almak için Ctrl+Z (Mac'te Cmd+Z).
- **Yorumlara göre düzeltme:** "Belgedeki yorumları sırayla işle, her birini izli değişiklik olarak uygula." Claude
  her yorum dizisine ne yaptığını yazar.
- **Karşı tarafın değişiklikleri:** "Karşı tarafın izli değişikliklerini özetle; kanuna aykırı ya da müvekkil aleyhine
  olanları işaretle."
- **Beceriler:** Claude ayarlarınızda açık olan beceriler Word'de de çalışır. Panelde `/` yazınca listelenir.

## Sınırlar

- **Yalnız araştırma bağlayıcısı gelir.** Word'deki Claude, claude.ai hesabınızdaki bağlayıcıları kullanır.
  Bilgisayarınızda çalışan ArthurMask, UYAP Dashboard, Beyin ve ArthurLegal Masası Word'de görünmez.
- **Belge içeriği Anthropic'e gider.** Claude hesabıyla girildiğinde sohbet, Claude'un belgeden okuduğu içerik (metin,
  yorumlar, izli değişiklikler, dipnotlar, tablolar) ve eklediğiniz dosyalar Anthropic'e gönderilir. ArthurMask
  burada araya girmez: müvekkil sırrı ya da kişisel veri içeren belgede önce ArthurMask ile maskeleyin, Word'de
  maskeli belgeyle çalışın. Ayrıntı: [Verileriniz nereye gider](verileriniz.md).
- **Saklama.** Anthropic'in Word sayfasına göre girdiler ve çıktılar, gizlilik sayfasındaki istisnalar dışında 30 gün
  içinde silinir. Kuruluşunuzun özel saklama ayarları bu eklentiye uygulanmaz. Sohbet geçmişi yalnız o tarayıcıda
  durur (her uygulama için son 50 sohbet). Eklenti belgeye kendi tanıtıcısını yazar; belge paylaşılınca bu bilgi de
  belgeyle gider.
- **Son kontrol avukattadır.** Anthropic de eklentiyi yalnız güvenilir belgelerle kullanmayı ve müvekkile ya da karşı
  tarafa gidecek son metni insan kontrolünden geçirmeyi öneriyor. ArthurLegal hukuki görüş vermez; bulduğu kaynakla
  çalışmanızı hızlandırır.

## Kaynaklar

- Anthropic, Claude for Word: https://claude.com/docs/office-agents/word
- Anthropic, Connectors and skills: https://claude.com/docs/office-agents/connectors-and-skills
- Anthropic, Data storage: https://claude.com/docs/office-agents/data-storage
- Microsoft Marketplace, Claude for Microsoft 365: https://marketplace.microsoft.com/en-us/product/office/WA200010725

Resmî sayfalar değişebilir; sürüm şartında tereddüt ederseniz önce Anthropic'in Word sayfasına bakın.

---

Microsoft, Word ve Microsoft 365, Microsoft şirketler grubunun ticari markalarıdır. Claude, Anthropic'in ticari
markasıdır. ArthurLegal bu şirketlerle bağlantılı değildir; adlar yalnız uyumluluğu belirtmek için anılır.
