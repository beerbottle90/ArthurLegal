# Kurulum — ArthurLegal Courthouse

**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web)
**Sürüm:** v1.0.2 · 2026-09-13
**Süre:** ~10 dakika (Arthur Mask ile ~20 dakika)

> ⚠️ Bu paket **yargı mensupları** (mahkeme hâkimleri + kalem memurlukları) içindir. Tüm çıktılar **taslaktır** ve **hâkim / heyet onayı** gerektirir; hiçbir çıktı yargısal karar yerine geçmez.

## 4 adım

1. **Yeni Claude.ai Project oluşturun** — [claude.ai/projects](https://claude.ai/projects) → "+ New Project".
2. **`SYSTEM_PROMPT.md`** içeriğini Custom Instructions alanına yapıştırın.
3. **`knowledge/`** klasöründeki dosyaları Project Knowledge'a sürükle-bırak ile yükleyin.
4. **`knowledge/mahkeme-profili.md`** içindeki `[DOLDUR]` alanlarını kendi mahkemenize göre özelleştirin (opsiyonel).

## ArthurLegal MCP bağlantısı (önerilir)

Yargı ve mevzuat araçları için Claude.ai → Settings → Connectors → **Add custom connector**:
ad `arthurlegal`, URL `https://arthurlegal-mcp.fly.dev/mcp`, auth yok. Türk hukuku bu
connector'da `tr_` önekiyle gelir (23 araç: Yargıtay, Danıştay, BAM, yerel, KYB, AYM,
Uyuşmazlık Mahkemesi, mevzuat, Resmî Gazete, 8 düzenleyici kurum, semantik arşiv). Detay:
`knowledge/references/yargi-mcp-rehberi.md` ve `mevzuat-mcp-rehberi.md`. MCP olmadan da
çalışır; ancak güncel içtihat/mevzuat çekimi için MCP şarttır. AİHM, KİK ve Sayıştay bu
connector'da yoktur; gerekiyorsa TR Legal MCP (yargi-mcp-pro, OAuth) ikinci connector olarak
eklenir.

## Arthur Mask (önerilir, isteğe bağlı: dosya belgelerini bilgisayarınızda maskeleyin)

Arthur Mask, dava, soruşturma ve kovuşturma dosyalarındaki belgeleri Claude'a vermeden önce
**kendi bilgisayarınızda** maskeler: taraf, şüpheli, sanık, mağdur ve tanık adları, TCKN,
adres, telefon, dosya numarası gibi bilgiler `{{KİŞİ-01}}`, `{{TCKN-01}}` gibi etiketlere
dönüşür; gerçek değerler bilgisayardaki şifreli kasada kalır. Claude yalnız maskeli metni
görür; cevap bilgisayarınızda gerçek adlarla Word veya UYAP editöründe (UDF) açılır. Program
çevrimdışı çalışır.

> ⚠️ **Yalnız Claude Desktop (Windows).** claude.ai web sürümünde ve mobil uygulamalarda
> çalışmaz: claude.ai'deki connector'lar Anthropic'in bulutundan çağrılır ve bulut,
> bilgisayarınızdaki programa ulaşamaz. Project'inizi Claude Desktop'tan açın; Project'ler
> web ile masaüstü arasında ortaktır.

**Gereksinim:** Windows 10 veya 11 (64 bit) · [Claude Desktop](https://claude.ai/download) ·
yaklaşık 4 GB boş disk · 8 GB RAM önerilir. Kurumsal bilgisayarlarda yazılım kurma ve harici
yapay zekâ hizmeti kullanma kurum kurallarına tabidir.

1. **İndirin.** **[⬇ Arthur Mask kurulum dosyasını indirmek için buraya tıklayın](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** (Windows, yaklaşık 1 GB).
   GitHub hesabı ya da GitHub bilgisi gerekmez: bağlantıya tıklayınca `ArthurMask-Kurulum.exe` dosyası
   doğrudan bilgisayarınızın **İndirilenler** klasörüne iner. İnternet hızınıza göre birkaç dakika sürebilir.
   Tarayıcı "Sakla / Keep" diye sorarsa **Sakla**'yı seçin. İndirme bitince İndirilenler klasöründe dosyaya çift tıklayın.
2. **Çalıştırın.** Kurulum dosyası kod imzalı değildir; SmartScreen **"Windows bilgisayarınızı
   korudu"** derse **Ek bilgi** → **Yine de çalıştır**. Antivirüs dosyayı bir süre tarayabilir.
3. **Kurun.** Yönetici yetkisi gerekmez (`%LOCALAPPDATA%\Programs\Arthur Mask`). Kurulum
   `arthur-mask` connector'ını Claude Desktop yapılandırmasına kendiliğinden ekler ve önceki
   yapılandırmanın yedeğini tutar.
4. **Claude Desktop'u yeniden başlatın:** sistem tepsisi simgesi dâhil **tamamen** çıkın, yeniden açın.
5. **Doğrulayın:** Claude Desktop → **Ayarlar → Geliştirici**'de `arthur-mask` çalışıyor
   görünür; sohbette araçlar menüsünde Arthur Mask araçları listelenir.
6. **Kurtarma anahtarını saklayın:** Arthur Mask → **Kurtarma anahtarı** → yazdırın veya
   güvenli yerde saklayın → **Sakladım**. Anahtarı Claude'a yazmayın.

Günlük kullanım, kırmızı hat, sızıntı denetimi ve sorun giderme: [ARTHUR-MASK.md](ARTHUR-MASK.md).
Knowledge'a `knowledge/references/arthur-mask-rehberi.md` dosyasını da yükleyin.

## İlk kullanım

```text
/hukuk-hakim:gerekceli-karar
[dosya özetini / uyuşmazlığı yapıştır]
```

Bir plugin'in tüm komutlarını görmek için yeni konuşmada sadece `/<plugin>:` yazın (örn. `/hukuk-hakim:`).

## Komut haritası (v1.0.2)

| Plugin | Skill'ler |
|---|---|
| `/hukuk-hakim:` | gerekceli-karar · on-inceleme · delil-degerlendirme · ihtiyati-tedbir |
| `/hukuk-kalem:` | tensip-zapti · tebligat · harc-hesabi |
| `/ceza-hakim:` | hukum-taslagi · iddianame-degerlendirme · tutuklama-degerlendirme · hagb-degerlendirme · uzlastirma-denetimi |
| `/ceza-kalem:` | muzekkere · ceza-tebligat · infaz-evraki |
| `/idari-hakim:` | idari-karar · yurutmenin-durdurulmasi · ehliyet-husumet · ivedi-yargilama |
| `/idari-kalem:` | dosya-tekemmul · idari-tebligat · karar-uygulama-takip |
| `/vergi-hakim:` | vergi-karar · tarhiyat-degerlendirme · odeme-emri-itiraz |
| `/vergi-kalem:` | vergi-tebligat · vergi-sure-takip · karar-uygulama-iade |

## Sık sorulan sorular

**S: Dosya belgesini Claude'a nasıl güvenle veririm?**
A: Önce kurum kurallarınızın harici bir yapay zekâ hizmetinin kullanılmasına izin verip vermediğini kontrol edin; gizlilik veya kısıtlama kararı bulunan dosyaların içeriği maskeli olsa bile verilmemelidir. İzin varsa ve Claude Desktop (Windows) kullanıyorsanız belgeyi (UDF, Word, PDF, tarama) önce Arthur Mask'e bırakın, incelemeyi onaylayın ve yalnız gösterilen komutu sohbete yapıştırın; orijinal belgeyi sohbete eklemeyin. Maskeleme takma adlandırmadır, anonim hâle getirme değildir ve tespit olasılığa dayalıdır: göndermeden önce maskeli kopyaya bakın ve sızıntı denetimini kullanın. claude.ai web ve mobilde Arthur Mask çalışmaz. Ayrıntı: [ARTHUR-MASK.md](ARTHUR-MASK.md).

## Güncelleme notları

Bu sürüm **v1.0.2**'dir. v1.0.1'den geçiş: `SYSTEM_PROMPT.md` yeniden yapıştırılır (yeni Arthur Mask bölümü); `knowledge/references/arthur-mask-rehberi.md` Project knowledge'a eklenir. Arthur Mask kullanacaksanız yukarıdaki adımları uygulayın ve Project'i Claude Desktop'tan açın. Değişiklikler: [CHANGELOG.md](CHANGELOG.md).

## Kişisel veri uyarısı

Mahkeme dosyaları yoğun **kişisel ve özel nitelikli veri** içerir. Bu pakete gerçek dosya verisi yüklemeden önce kurumsal gizlilik kurallarınızı ve veri minimizasyonu ilkesini gözetin. Belgeler Claude'a verilmeden önce Arthur Mask ile bilgisayarınızda maskelenebilir (yalnız Claude Desktop, Windows); maskeleme kurum kurallarının ve gizlilik kararlarının yerine geçmez.
