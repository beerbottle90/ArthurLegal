<img src="varlik/banner.png" alt="ArthurLegal — açık kaynak hukuk yapay zekâsı" width="900">

# ArthurLegal Setup v2.6.2

**Tek dosyalık kurulum, Windows ve macOS.** Kullanıcı indirir (Windows'ta `ArthurLegal-Kurulum.exe`, Mac'te
`ArthurLegal-Kurulum.pkg`), çift tıklar, modül ekranında işine yarayan paketleri (Hukuk Bürosu, Kurumsal Asistan,
Courthouse, Akademisyen) ve araçları (ArthurLegal Tapu, Arthur Mask) seçer; seçtikleri, araştırma bağlantısıyla
birlikte Claude Desktop'a kendiliğinden bağlanır. Yönetici yetkisi gerekmez. Sonraki sürümler arka planda, imzası
doğrulanarak sessizce kurulur. İki kurulum aynı paketleri, aynı modülleri ve aynı güncelleme kanalını kullanır.

> Paketlerin kendisi (SYSTEM_PROMPT + knowledge) bu deponun kökündedir ve Claude.ai'de elle de
> kurulabilir: her paketin `KURULUM.md` dosyası. Bu klasör, o kurulumu tek tıka indiren ve
> güncel tutan Windows paketidir.

## Ne kurulur

Lisans sayfasından sonraki **Modülleri seçin** ekranında her modül bir onay kutusu ve altında kısa açıklamadır.
İlk kurulumda hiçbir kutu işaretli gelmez, en az bir paket gerekir; kurulum yeniden açılınca son seçim işaretli
gelir. Seçim kurulum klasöründeki `moduller.json`'a yazılır ve güncellemelerde korunur. 2.5.0'dan önceki
kurulumlarda bu dosya yoktur; onlar eski modülleriyle (Hukuk Bürosu, Kurumsal, Tapu, Arthur Mask) sürer.

| Modül | Kod | Masaüstü simgesi | Ne yapar |
|---|---|---|---|
| **Hukuk Bürosu** | `hukuk-burosu` | ArthurLegal | Law Firm paketi: avukatlar ve hukuk büroları |
| **Kurumsal Asistan** | `kurumsal` | ArthurLegal | Corporate paketi: şirket hukuk birimleri |
| **Courthouse** | `adliye` | ArthurLegal - Courthouse | Hâkim ve kalem için tarafsız taslak paketi |
| **Akademisyen** | `akademisyen` | ArthurLegal - Akademisyen | Academician paketi: hukuk akademisyenleri |
| **ArthurLegal Tapu** | `tapu` | ArthurLegal - Tapu | Yerel `arthur-tapu` sunucusu (aşağıda) |
| **Arthur Mask** | `mask` | Arthur Mask (kendi kurulumundan) | Kurulum sırasında indirilir; kuruluysa kutu işaretli ve kilitli görünür |

macOS'ta simgeler Uygulamalar klasöründe (`~/Applications`, Launchpad'de) küçük uygulamalardır, masaüstünde birer
takma adları durur; adlarda tire ve sürüm numarası yoktur: **ArthurLegal**, **ArthurLegal Courthouse**,
**ArthurLegal Akademisyen**, **ArthurLegal Tapu**. Arthur Mask'in masaüstü takma adını da kurulum koyar.

Bileşenler:

| Bileşen | Nerede çalışır | Ne yapar |
|---|---|---|
| **arthurlegal-yerel** | Claude Desktop · kurulumun Python 3.12'si | Seçilen paketlerin sistem talimatını ve bilgi dosyalarını araç olarak sunar; `arthurlegal-mcp.fly.dev` araştırma araçlarını (TR + 14 yargı çevresi, 100+ araç) köprüler. Ayrıca connector eklemeye gerek kalmaz. Tek paket seçildiyse o varsayılandır; birden çoksa talimat, hangi işte hangi profilin çağrılacağını söyler |
| **arthur-tapu** | Claude Desktop + masaüstü kısayolu | Yalnız Tapu seçildiyse. tkgm-mcp 0.5.2: TKGM Parsel Sorgu'dan canlı parsel (il/ilçe/mahalle listeden, ada/parsel ayrı kutularda) (dakikada en çok 30 istek, sohbet başına onay kartı), parsel raporu, kroki, harç, tapu kaydı maskeleme, Word/Excel çıktı, yerel tarayıcı arayüzü |
| **arthur-mask** | Claude Desktop + kendi arayüzü | Müvekkil ya da dosya belgelerini bilgisayarda maskeleyen gizlilik kapısı. Seçildiyse kurulum sırasında indirilir (≈1 GB); seçilmediyse güncelleyici de indirmez |
| *arthur-uyap* | (bu pakette yok) | UYAP köprüsü ayrı dağıtılır; kurulum, bilgisayarda varsa kendiliğinden bağlar. Köprünün yerel ekranı varsa ve Arthur Mask kuruluysa masaüstüne ve Başlat menüsüne UYAP için tek simge ekler: "ArthurLegal - UYAP Dashboard" (büro kurulumunda markadaki kısa adla). UYAP'a giriş tarayıcısını Dashboard kendisi açar |

Claude Desktop kurulu değilse Windows'ta `winget` ile kullanıcı kapsamında kurulur; Mac'te başlangıç paneli
[claude.ai/download](https://claude.ai/download) adresini gösterir.

## Kurulum

1. **[ArthurLegal-Kurulum.exe](https://github.com/beerbottle90/ArthurLegal/releases/latest/download/ArthurLegal-Kurulum.exe)**
   dosyasını indirin (bağlantı her zaman en son sürümü verir) ve çift tıklayın. Edge ya da Windows uyarı
   verirse resimli anlatım [ana sayfanın indirme bölümünde](https://github.com/beerbottle90/ArthurLegal#indir);
   kısaca Edge'de **⋯ → Sakla**, sonra mavi **Sil** düğmesinin yanındaki ok **→ Yine de sakla**; mavi
   "Windows kişisel bilgisayarınızı korudu" penceresinde **Ek bilgi → Yine de çalıştır**. Kurulum İngilizce ve
   Türkçedir: açılışta dil sorulur, Windows'un diline uyan dil seçili gelir. Kısayol adları ve başlangıç rehberi
   seçilen dilde yazılır. Lisanstan sonra modülleri seçin (yukarıda).
2. Claude Desktop'ta **yeni bir sohbet açıp hukuki sorunuzu doğrudan yazın.** Proje ya da yapıştırma
   gerekmez: `arthurlegal_talimat` aracının açıklaması ve sunucunun `instructions` alanı modele "hukukla
   ilgili her soruda önce beni çağır" der; profil verilmezse kurulumdaki varsayılan kullanılır.
3. Claude bir aracı ilk kez kullanırken izin sorarsa **Always allow**'u (Her zaman izin ver) seçin; Claude
   Desktop'un menüleri İngilizcedir. Araç izinleri Claude Desktop'ın kendi deposunda tutulur; kurulum bunları
   önceden işaretleyemez. Araştırma araçları salt okunur diye işaretlenir (2.4.4), böylece Claude kalıcı izin
   sunabilir.

**Yedek yollar.** (1) Kurulum seçilen her paket için `%USERPROFILE%\ArthurLegal\` altında bir proje klasörü
hazırlar (`Hukuk Bürosu`, `Kurumsal`, `Courthouse`, `Akademisyen`; içinde `CLAUDE.md`, `SYSTEM_PROMPT.md`,
`knowledge/`; güncelleyici her sürümde yeniler, kullanıcının kendi dosyalarına dokunmaz): Claude'da
**Projects → New project → Use a folder** ile seçilir. (2) Başlangıç panelindeki kısa talimat bir projenin
**Instructions** alanına yapıştırılır. (3) Sohbette **+** menüsünden `arthurlegal-yerel` altındaki paketin istemi
(`hukuk-burosu`, `kurumsal`, `adliye`, `akademisyen`) seçilir.

**Sessiz kurulum.** `ArthurLegal-Kurulum.exe /VERYSILENT /SUPPRESSMSGBOXES /MODULLER=adliye,tapu,mask`. Liste
geçersizse (bilinmeyen ad, derlemede olmayan modül ya da hiç paket yok) kurulum hiçbir şey kurmadan durur.
`/MODULLER` verilmezse önceki kurulumun seçimi, o da yoksa 2.5.0 öncesinin modülleri kullanılır.

**Windows 11 Akıllı Uygulama Denetimi (Smart App Control) açıksa** imzasız kurulum motoru engellenir
(`Hata 4551`). O bilgisayarda [`ArthurLegal-Kurulum.zip`](https://github.com/beerbottle90/ArthurLegal/releases/latest/download/ArthurLegal-Kurulum.zip) dosyasını indirin;
ayıklamadan önce **Özellikler → Engellemeyi Kaldır** (denetim internetten gelen `.cmd` dosyasını engeller, Gezgin
bu işareti zipten çıkan dosyalara taşır), sonra klasöre çıkarın ve `KUR.cmd` dosyasına çift tıklayın: aynı
kurulumu imzalı Python ile yapar, modülleri konsolda numarayla sorar (Arthur Mask bu yolla kurulamaz). Zip'in içinde Türkçe `BENIOKU.txt` ve İngilizce `README.txt` vardır. Denetim
açıkken Arthur Mask kurulamaz; güncelleyici onu indirmeye çalışmaz (2.4.4). Denetim durumu:
`(Get-MpComputerStatus).SmartAppControlState`.

Kaldırma: **Ayarlar → Uygulamalar → ArthurLegal**, ya da zip yoluyla kurulduysa kurulum klasöründeki
`KALDIR.cmd`.

## macOS

**[ArthurLegal-Kurulum.pkg](https://github.com/beerbottle90/ArthurLegal/releases/latest/download/ArthurLegal-Kurulum.pkg)**
macOS 11 ve sonrası; Apple Silicon ve Intel için tek paket. Resimli anlatım
[ana sayfanın Mac bölümünde](https://github.com/beerbottle90/ArthurLegal#mac).

- **İlk açılış.** Paket henüz Apple noter onayı (notarization) taşımaz: macOS ilk açılışta durdurur, bir kez
  **Sistem Ayarları → Gizlilik ve Güvenlik → Yine de Aç** ile izin verilir.
- **Sihirbaz.** macOS Installer: karşılama, lisans, **Yükleme Türü** ekranında modüller (Windows sihirbazıyla aynı
  ad ve açıklamalar, `kurulum/ArthurLegal.iss`'ten), kurulum, bitiş. Kurulum yalnız kullanıcının ev klasörüne
  yapılır, yönetici şifresi istemez. Yeniden açılınca son seçim işaretli gelir.
- **Nereye.** `~/Library/Application Support/ArthurLegal` (Windows'taki `%LOCALAPPDATA%\Programs\ArthurLegal`'ın
  karşılığı; içinde `runtime/bin/python3`, `bin/al.py`, `surumler/`). Claude Desktop kaydı
  `~/Library/Application Support/Claude/claude_desktop_config.json`'a, proje klasörleri `~/ArthurLegal`'a yazılır.
  Paket iki Python taşır (Apple Silicon ve Intel); kurulumun son adımı bilgisayara uyanı bırakır.
- **Güncelleme.** Oturum açılışında ve altı saatte bir `~/Library/LaunchAgents/com.arthurlegal.guncelleme.plist`
  çalıştırır; paket ve imza denetimi Windows'takiyle aynıdır. Elle: Uygulamalar → ArthurLegal →
  **Güncellemeleri Denetle**.
- **Arthur Mask.** Seçildiyse kurulumdan sonra güncelleyici disk görüntüsünü (≈1,2 GB) indirir, sha256'sını imzalı
  manifestle doğrular, Uygulamalar'a kopyalar ve Claude Desktop'a kaydettirir; bitince bildirim gelir. Arthur Mask'in
  Mac sürümü Apple Silicon ve macOS 14 ister; öteki Mac'lerde seçenek soluk gelir.
- **Kaldırma.** Uygulamalar → ArthurLegal → **ArthurLegal'i Kaldır**: onay sorar; Claude Desktop kaydını,
  uygulamaları, masaüstü takma adlarını, oturum açılışı görevini ve kurulum klasörünü siler. Proje klasörlerindeki
  kendi dosyalarınız kalır.
- **Sessiz kurulum.** `installer -pkg ArthurLegal-Kurulum.pkg -target CurrentUserHomeDirectory
  -applyChoiceChangesXML secim.xml` (seçim dosyasının biçimi: `installer -showChoicesXML`; modül kimlikleri
  Windows'takilerle aynı: `adliye`, `tapu`, `mask` ...).

## Güncelleme

Oturum açılışında ve Claude Desktop açıkken altı saatte bir, en son yayındaki `arthurlegal-manifest.json`
denetlenir. Manifest **Ed25519** ile imzalıdır: imza güvenilen anahtarlardan biriyle doğrulanmazsa hiçbir
şey kurulmaz. Yeni sürüm ayrı bir klasöre açılır, `aktif.txt` tek adımda değişir, bir önceki sürüm geri
dönüş için kalır ve yeni sürüm Claude Desktop'ın bir sonraki açılışında devreye girer.

**İki anahtar (2.4.3).** Kurulumlar iki anahtara güvenir: günlük yayın anahtarı ve kasada duran yedek
anahtar. Liste paketin içinde, imzalı güncellemeyle gelir. Günlük anahtar kaybolursa yayın kasadaki
anahtarla imzalanır; anahtar değişikliği de yeniden kurulum gerektirmez. Adımlar `yayin/yayinla.py`'nin
başındaki açıklamada.

**2.4.2'de yayın anahtarı yenilendi.** 2.4.2'den eski kurulumlar yeni imzayı tanımaz ve hiçbir şey kurmaz;
güncelleme durumunda "manifest imzası geçersiz" görünür. `ArthurLegal-Kurulum.exe`'yi bir kez çalıştırın:
eski sürümün üzerine kurar, sonraki güncellemeler yine sessiz gelir.

## Gizlilik

- Paket dosyaları, büro katmanı ve tapu kayıtları bilgisayardan çıkmaz; yerel sunucular yalnız
  stdio üzerinden Claude Desktop ile konuşur.
- Araştırma araçları, modelin yazdığı arama sorgularını ArthurLegal araştırma sunucusuna iletir.
  Bu sorgulara müvekkil adı veya gizli bilgi yazılmaz; talimat bunu ayrıca hatırlatır.
- Bulut tarafındaki `tkgm_` araçları kuruluma dahil edilmez: tapu kaydı metni yalnız yereldeki
  `arthur-tapu` ile işlenir.
- Güncelleyicinin tek dış bağlantısı GitHub'dır; günlüklere sorgu veya belge içeriği yazılmaz.

## Derleme

Gerekenler: Python 3.10+, git, [Inno Setup 6](https://jrsoftware.org/isinfo.php)
(`winget install -e --id JRSoftware.InnoSetup --scope user`), bu deponun yanında
[`arthurlegal-mcp`](https://github.com/beerbottle90/arthurlegal-mcp) ve
[`arthur-mask`](https://github.com/beerbottle90/arthur-mask) klonları (`kaynaklar.json` → `depolar`).

```bash
python varlik/gorseller.py             # pixel art simge ve görseller
python yayin/derle.py                  # yayin/cikti/ArthurLegal-Kurulum.exe + .zip + güncelleme paketi
python -m unittest discover -s tests   # 82 test, ağa çıkmaz (macOS'a özgü olanlar Windows'ta da sınanır)
python yayin/yayinla.py v2.6.2         # imzalı manifest + dosyalar → taslak yayın → yayımla (Latest)
```

**Paket denetimi.** `yayin/paket_denetimi.py`, paketlere dokunan her push'ta ve PR'da GitHub Actions'ta
([`paket-denetimi.yml`](../.github/workflows/paket-denetimi.yml)) ve yukarıdaki testlerle birlikte çalışır; pakette
tanımlı olmayan skill'e atfı, klasör adıyla uyuşmayan sürümü, gerçek dosya sayısını tutmayan sayımı ve paketler
arasında yeni ayrışmayı yakalar, bilinen eski sorunlar `tests/paket_denetimi_taban.json`'da durduğu için yalnız
yenileri testi kırar (rapor: `python yayin/paket_denetimi.py --ayrinti`).

**macOS paketi** yalnız macOS'ta derlenir (`pkgbuild`, `productbuild`, `iconutil`, [uv](https://docs.astral.sh/uv/)):
`python yayin/derle_macos.py` → `yayin/cikti/ArthurLegal-Kurulum.pkg` ve `derleme-macos.json`. Bunu GitHub Actions
yapar ([`macos-kurulum.yml`](../.github/workflows/macos-kurulum.yml)): her derlemede paketi Apple Silicon bir Mac'te
kurar (Courthouse, Tapu ve Arthur Mask seçili), `tests/mac_kurulum_denetimi.py` ile denetler, kaldırır ve paketi iş
çıktısı olarak saklar. Yayında `.pkg`'yi `yayin/cikti`'ye koymak yeter: `yayinla.py` onu yalnız Windows derlemesiyle
aynı sürümün ve aynı commit'lerin (ArthurLegal, Tapu) derlemesiyse yükler.

**Ortak rehberler.** Birden çok pakete giren rehberlerin tek kaynağı [`ortak-rehberler/`](ortak-rehberler/README.md)'dadır; paketlerdeki kopyalar `python yayin/ortak_uret.py` ile oradan üretilir. Paketin içindeki kopyayı elle düzeltmek `tests/test_ortak.py`'de yakalanır.

Derleme her deponun **commitlenmiş HEAD**'inden yapılır; yarım kalan iş kuruluma girmez
(`--calisma-agaci` ile tersi). `kurulum/ArthurLegal.iss` ve lisans metni **UTF-8 BOM** ile
kaydedilir, yoksa Inno Setup Türkçe karakterleri bozar (derle.py denetler).

**Kendi bürona özel kurulum.** `firma/<kod>/firma.json` ve `firma/<kod>/knowledge/firm-profile.md`
oluşturup `python yayin/derle.py --firma <kod>` derlerseniz büro profiliniz kuruluma gömülür ve
paketteki boş şablonun yerine geçer; güncellemeler onu ezmez. `firma/<kod>/marka/simge.ico` konursa
kurulum dosyası, kısayollar ve kaldırma girdisi büronun simgesini taşır; güncellemeler onu da ezmez.
`firma/<kod>/marka/tema.json` bir `urun` adı veriyorsa kısayollar, Başlat menüsü, başlangıç sayfası ve
programlar listesi ArthurLegal yerine o adı taşır. Simge kısayollara adı içeriğinin özetini taşıyan bir
dosyayla (`bin/buro-<özet>.ico`) verilir: Windows simgeleri dosya yoluna göre önbelleğe aldığı için simge
değiştiğinde eski resim kalmaz.
İsterseniz kendi kurulumunuzu private
bir depodan dağıtabilirsiniz: `kaynaklar.json` → `dagitim_deposu` + `yayin/jeton_ayarla.py`.

**İmzalama.** `kaynaklar.json` → `imzalama.komut` (ya da `ARTHURLEGAL_IMZA_KOMUTU`) verilirse kurulum
ve kaldırıcı signtool ile imzalanır (`$f` dosya, `$q` tırnak); bulut imzalamanın hız sınırına karşı
yeniden deneme ayarları betikte hazırdır. Örnek (Certum SimplySign, oturum açıkken):

```
signtool.exe sign /sha1 <PARMAK-IZI> /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 $f
```

Paketin içinde imzasız çalıştırılabilir dosya yoktur: gömülü Python ve DLL'leri Python Software
Foundation imzalar, gerisi `.py` ve metindir. Dolayısıyla kurulum ve kaldırıcıyı imzalamak yeter.
İmzalı kurulum Akıllı Uygulama Denetimi'ne takılmaz; SmartScreen uyarısı ise (Microsoft'un 2024'te
EV ayrıcalığını kaldırmasından beri) ancak aynı imza kimliğiyle sürüm dağıtıldıkça, haftalar içinde
kalkar. Bu yüzden sertifika bir kez alınır ve değiştirilmez.

## Lisans

ArthurLegal paketleri ve bu kurulum: deponun kökündeki [LICENSE](../LICENSE) (hukuk bürolarında
kullanım, ücretli müvekkil işi dâhil, serbesttir; ürün veya hizmet olarak yeniden dağıtım ayrı yazılı
izne bağlıdır). ArthurLegal Tapu MIT, gömülü Python PSF lisanslıdır; kurulumdaki lisans sayfası
hepsini birlikte gösterir.

---

**English.** One-click installer for the ArthurLegal legal-AI packages, for Windows (`ArthurLegal-Kurulum.exe`)
and macOS (`ArthurLegal-Kurulum.pkg`, Apple Silicon and Intel), in English and Turkish (on Windows the language is
asked at start, on a Mac it follows the system; shortcut names and the start guide follow it). It installs a
private Python 3.12, registers local MCP servers with Claude Desktop (package knowledge + a bridge to
the public ArthurLegal research endpoint, plus the Turkish land-registry tools), optionally installs
the Arthur Mask local privacy gate, and keeps itself up to date from signed GitHub releases
(Ed25519). No admin rights. The only manual step is pasting a short, never-changing bootstrap prompt
into a Claude Project. Build it yourself with `python yayin/derle.py`.
