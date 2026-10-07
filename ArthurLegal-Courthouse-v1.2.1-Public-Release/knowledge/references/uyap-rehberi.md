# UYAP (Ulusal Yargı Ağı Bilişim Sistemi) — Mahkeme Pratiği Rehberi

> Türk yargısının elektronik altyapısı. Mahkeme hâkimleri ve kalem personeli dosya açma, inceleme, karar yazma/imzalama, tebligat ve müzekkere çıkışını UYAP üzerinden yürütür.
> ⚖️ Bu rehber mahkeme (hâkim + kalem) bakışındandır; taraf/vekil erişimi yalnızca bağlam olarak anılır.

## UYAP modülleri (mahkeme tarafı)

| Modül | Kullanan | İşlev |
|---|---|---|
| **Hâkim/Savcı ekranı** | Hâkim | Dosya inceleme, ara karar, karar yazımı + e-imza, duruşma yönetimi |
| **Personel (kalem) ekranı** | Yazı işleri/zabıt kâtibi | Dosya açma, tevzi, tebligat/müzekkere çıkışı, harç/gider, tutanak |
| **e-Duruşma / SEGBİS** | Hâkim + kalem | Sesli-görüntülü duruşma, istinabe, uzaktan ifade/tanık |
| **Bilirkişi Portalı** | Bilirkişi (atama mahkemece) | Atama, rapor sunumu, ücret |
| **Avukat / Vatandaş Portalı** | Taraf/vekil | Dilekçe sunma, dosya görüntüleme (mahkeme dışı taraf) |
| **EBYS entegrasyonu** | Kalem | Elektronik belge yönetimi, gelen-giden evrak |

## UYAP'a giriş yolları (hâkim, savcı, kalem, Bakanlık personeli)

Hâkim, savcı ve kalemin UYAP'ı iç ağdadır; herkese açık bir adresi yoktur. Bakanlığın yayımladığı girişler aşağıdadır; 28.09.2026'da kaynaklarından teyit edildi. Adres uydurulmaz, tabloda olmayan bir giriş önerilmez.

| Giriş | Kimin için | Nasıl | Kaynak |
|---|---|---|---|
| Adliye ağındaki UYAP | Hâkim, savcı, kalem; Bakanlık merkez ve taşra teşkilatı | Kurumun bilgisayarında, e-imzayla | Adalet Bakanlığı PGM, *Adli Yargı Hâkim ve Savcı Adayları İçin UYAP Ekranları Kullanım Kılavuzu*: https://adaylik.adalet.gov.tr/Resimler/311220201541adli-yargi-h-kim-ve-savci-adaylari-icin-uyap-kullanim-kilavuzupdf.pdf |
| VPN ile dışarıdan | E-imzasında VPN yetkisi tanımlı kullanıcı | Cisco AnyConnect'te sunucu `vpn.uyap.gov.tr`; e-imza PIN'i, sonra bilgisayar açılış kullanıcı adı ve şifresi | Adliye bilgi işlem kılavuzu: https://rayp.adalet.gov.tr/resimler/86/dosya/vpnanlatim03-09-202113-52.pdf |
| UYAP Mobil | Hâkim, Cumhuriyet savcısı, yazı işleri müdürü, kâtip, mübaşir, icra müdürü, icra memuru | Portal şifresi ve SMS doğrulaması; Google Play ve App Store | Bilgi İşlem Genel Müdürlüğü duyurusu (22.10.2021): https://bigm.adalet.gov.tr/Home/SayfaDetay/uyap-mobil-yargi-personelimizin-kullanimina-sunulmustur22102021085235 · Google Play: https://play.google.com/store/apps/details?id=tr.gov.adalet.uyapmobil · App Store: https://apps.apple.com/tr/app/uyap-mobil/id1585416362?l=tr |

- **Şifre işlemleri.** Portal, e-posta, haberci ve bilgisayar açılış (domain) şifresi https://sifre.uyap.gov.tr üzerinden sicil numarasıyla değiştirilir. Kaynak: https://gaziantepecik.adalet.gov.tr/uyap-portal-ve-domain-bilgisayar-acilis-sifre-islemleri
- **Bu kullanıcılar için olmayan portallar.** Kurum Portal (`kurum.uyap.gov.tr`) kamu kurumları ve davada taraf şirketler içindir (https://kurum.uyap.gov.tr/main/kurum/sss.jsp). Avukat, Vatandaş, Bilirkişi, Arabulucu ve E-Satış portalları da başka kullanıcılar içindir.
- **UYARI satırında.** Dosya bilgisi alınamadığında bağlantı yerine şu yazılır: `UYARI: veri çekilemedi, teyidiniz gerekli: UYAP'taki kendi ekranınız (adliyede UYAP; dışarıda VPN ile vpn.uyap.gov.tr ya da UYAP Mobil)`.

## Hâkim tarafında tipik akış

1. **Tevzi edilen dosya** hâkim ekranına düşer; taraflar, esas no, talep, tebligatlar görülür.
2. **İnceleme** — dilekçeler, deliller, bilirkişi raporu, ara kararlar tek ekranda.
3. **Ara karar / tensip** — UYAP üzerinden oluşturulur, kaleme havale edilir.
4. **Karar yazımı** — gerekçeli karar UYAP'ta yazılır, **e-imza** ile imzalanır.
5. **Tefhim/tebliğ** — karar UYAP üzerinden taraflara/vekillere tebliğe çıkar; süreler tebliğden işler.

## Kalem tarafında tipik akış

1. **Dosya açılış & tevzi** — yeni dava kaydı, otomatik tevzi.
2. **Tebligat çıkışı** — UYAP + UETS (e-tebligat) → `tebligat-7201-rehberi.md`, `kep-etebligat-rehberi.md`.
3. **Müzekkere** — kurum yazışmaları UYAP üzerinden.
4. **Harç/gider** — tahsilat kaydı, eksik harç muhtırası → `harc-gider-rehberi.md`.
5. **Duruşma tutanağı** — zabıt kâtibi tutanağı UYAP'ta tutar; SEGBİS kaydı.

## Belge & sunum (HMK/CMK/İYUK + UYAP)

| Belge | Format | UYAP |
|---|---|---|
| Dava/cevap dilekçesi (taraf) | PDF (e-imzalı) | Avukat portalından sunulur |
| Ara karar / tensip | UYAP | Hâkim oluşturur |
| Bilirkişi raporu | PDF (bilirkişi e-imzası) | Bilirkişi portalı |
| Gerekçeli karar | UYAP + e-imza | Hâkim imzalar, tebliğe çıkar |
| Tebligat mazbatası | UYAP/UETS/fiziksel | Kalem takip eder |

## UYAP Emsal — içtihat arşivi (ArthurLegal MCP (`tr_`) üzerinden)

UYAP karar arşivindeki emsal kararlara **ArthurLegal MCP (`tr_`)** ile erişilir (gerekçe/karar yazımında emsal taraması için):

```
mevzuat/yargı araçları → Bedesten/Emsal birleşik arama (konu + tarih aralığı)
```

> Bu **karar arşivi** araştırmasıdır; canlı dosya durumu hâkim/kalem ekranındadır. Emsal atıfları daima **verbatim** çekilir: `[ArthurLegal TR — kurum — Esas/Karar — GG.AA.YYYY]`.

## Tipik teknik sorunlar (mahkeme)

| Sorun | Not |
|---|---|
| e-İmza süresi dolmuş | Karar imzalanamaz; e-imza yenileme |
| e-Tebligat okunmamış ama süre işliyor | UETS'te muhatabın elektronik adresine ulaştığı tarihi izleyen 5. günün sonunda tebliğ sayılır (Teb. K. m. 7/a; süre işler) |
| SEGBİS/e-duruşma bağlantı sorunu | İstinabe/uzaktan ifade için yedek plan; tutanağa şerh |
| Fiziksel sunulan evrak | Taranıp dosyaya eklenir; UYAP kaydı tutulur |

## Bağlantılı referanslar

- [HMK rehberi](hmk-rehberi.md) · [CMK rehberi](cmk-rehberi.md) · [İYUK rehberi](iyuk-rehberi.md)
- [Tebligat 7201 rehberi](tebligat-7201-rehberi.md) · [KEP/e-tebligat rehberi](kep-etebligat-rehberi.md)
- [ArthurLegal MCP TR rehberi](yargi-mcp-rehberi.md)
