# Claude.ai Projects – Kurulum Rehberi

## ArthurLegal Corporate Assistant v1.10.0

Çok yargı çevreli (multi-jurisdiction) 12-eklenti kurumsal hukuk asistanı.
Claude.ai Projects üzerinde çalışır.

**İçerik:** 12 birleşik skill dosyası · 84 referans (28 yargı çevresi, tapu-kadastro dâhil) · 7 ajan · company-profile şablonu
**MCP connector:** 5'e kadar — **ArthurLegal** (tek uçta Türkiye + 14 yargı çevresi + tapu-kadastro, 121 araç) · OpenCaseLaw.ch · **CourtListener** · **Fedlex** · TR Legal (isteğe bağlı)
(ArthurLegal dışındakiler isteğe bağlıdır · ayrıca OpenSanctions REST API)
**Yerel gizlilik kapısı:** Arthur Mask (isteğe bağlı, önerilir; Windows 10/11 64 bit + Claude Desktop, Adım 5)

> **22 yargı çevresi** = 12 ulusal (TR · CH · US · AZ · UK · DE · FR · IT ·
> JP · RU · CN · RS) + 2 supranasyonel hukuk düzeni (AB/CJEU · ECHR).

---

## Adım 1 — Yeni Proje Oluştur

1. https://claude.ai/projects → **+ New Project**
2. **İsim:** `TR Legal Assistant` (veya şirketinize özel bir isim)
3. **Açıklama (opsiyonel):** "Multi-jurisdiction in-house hukuk asistanı — 12 pratik alan, 22 yargı çevresi, 7 MCP connector'a kadar"

---

## Adım 2 — System Prompt'u Yapıştır

1. **Project → Settings → Custom Instructions**
2. `SYSTEM_PROMPT.md` dosyasının tüm içeriğini kopyalayıp yapıştırın
3. Save.

> Not: Custom instructions limiti ~32K karakter. v1.4.0 SYSTEM_PROMPT.md **~27K** —
> sığar ama marj daralmıştır. Kendi eklemelerinizi yaparken karakter sayısını kontrol edin.

---

## Adım 3 — Knowledge Dosyalarını Yükle

`knowledge/` klasörünün altında **103 dosya** var (4 kategori):

```
knowledge/
  skills/      ← 12 dosya (birleşik skill kitapçıkları — legal-research dâhil)
  references/  ← 83 dosya (TR mevzuat, yargı çevresi ve MCP rehberleri, arthur-mask-rehberi.md)
  agents/      ← 7 dosya (periyodik ajan tanımları)
  company-profile.md
```

> ⚠️ **Claude.ai Projects yükleme kısıtlaması:** Tüm dosyaları tek seferde sürüklemek
> çalışmıyor. **Klasör başına bir toplu sürükleme** yapın.

### Yükleme adımları

Project → **+ Add content** → **Files** ekranını açık tutun.

1. `knowledge/skills/` klasörünü aç → `Ctrl+A` (12 dosya) → sürükle → bekle
2. `knowledge/references/` klasörünü aç → `Ctrl+A` (83 dosya) → sürükle → bekle
3. `knowledge/agents/` klasörünü aç → `Ctrl+A` (7 dosya) → sürükle → bekle
4. `knowledge/company-profile.md`'yi ayrıca sürükle

> **İpucu:** Her yüklemeden sonra dosyaların listede göründüğünü teyit et.
> Boyut limiti aşılırsa yalnızca kullandığın pratik alanın skill dosyasını yükle.

---

## Adım 4 — ArthurLegal MCP Connector Ekle (Türkiye + 14 yargı çevresi, tek uç)

**Customize → Connectors → + Add custom connector**

| | |
|---|---|
| **Ad** | `arthurlegal` |
| **URL** | `https://arthurlegal-mcp.fly.dev/mcp` |
| **Auth** | **None** — kimlik doğrulama yok |

Tek uç, 16 backend, 121 araç. Türkiye `tr_`, tapu-kadastro `tkgm_` önekiyle bu connector'ın içindedir; ayrı bir Türk hukuku ya da tapu connector'ı gerekmez. Tapu araçlarının ilk canlı sorgusu sohbet başına bir kez onay kartı gösterir; ayrıntı `knowledge/references/tapu-kadastro-rehberi.md`.

| Önek | Kapsam |
|---|---|
| `tr_` | 🇹🇷 Türkiye — Yargıtay, Danıştay, BAM, yerel, KYB (Bedesten) · AYM · Uyuşmazlık Mah. · 12 tür mevzuat, madde ağacı, gerekçe · Resmî Gazete · 8 düzenleyici kurum (Rekabet, EPDK, SPK, BDDK, KVKK, BTK, GİB, Sigorta Tahkim) · 19.498 belgelik semantik arşiv (23 araç) |
| `es_` | 🇪🇸 İspanya — BOE konsolide mevzuat (12.376 akt, indeksli) |
| `pl_` | 🇵🇱 Polonya — Dz.U. mevzuat (indeksli) |
| `nl_` | 🇳🇱 Hollanda — içtihat + mevzuat (KOOP tam metin araması) |
| `fi_` | 🇫🇮 Finlandiya — konsolide kanunlar (indeksli) |
| `ie_` | 🇮🇪 İrlanda — Acts of the Oireachtas (indeksli) |
| `at_` | 🇦🇹 Avusturya — RIS mevzuat + içtihat |
| `de_` | 🇩🇪 Almanya — federal mevzuat + BVerfG/BGH/BAG/BFH/BVerwG |
| `az_` | 🇦🇿 Azerbaycan — e-qanun, **yürürlük statüsü doğrulamalı** |
| `scholar_` | 🌍 Hukuk doktrini — 10 indeks, DergiPark dahil 19 Türk hukuk dergisi |
| `contracts_` | 🌍 5.125 imzalı PSA/JOA sözleşmesi |
| `uk_` | 🇬🇧 Birleşik Krallık — mevzuat + **işlenmemiş tadiller** |
| `eu_` | 🇪🇺 AB — mevzuat + CJEU içtihadı (CELLAR) |
| `jp_` | 🇯🇵 Japonya — mevzuat, yürürlük statüsü hesaplanmış |
| `gleif_` | 🌍 Tüzel kişi kimliği + grup yapısı (LEI) |
| `tkgm_` | 🇹🇷 Tapu-kadastro — TKGM Parsel Sorgu'dan canlı parsel (ada/parsel, koordinat, yer adı), parsel raporu, ölçekli kroki, dayanak köprüsü; dakikada en çok 30 istek, sohbet başına onay kartı |

> ⚠️ **Önek zorunlu.** Alttaki sunucularda `get_act` **beş ayrı şey** demek. Önek,
> İspanyol hukuku sorusunun Fin mevzuatıyla cevaplanmasını engelleyen tek şeydir.
> Araçları önekli adlarıyla çağır: `tr_ictihat_ara`, `az_get_act`, `es_search_legislation`.

> ⚠️ **Kimlik doğrulama yok.** Adresi bilen herkes tüm araçları çağırabilir.
> Kamuya açık kaynaklarda arama yaparlar; şirket sırrı, müvekkil adı, müzakere
> pozisyonu veya gizli taslak **gönderilmez**.

**Kapsamı kendin doğrula.** `status` aracı her yargı çevresi için indeks
büyüklüğünü, `index_coverage` aralığını ve semantiğin açık olup olmadığını verir.
Türkiye satırında sekiz kurumun kaçar belgesinin indekslendiği görünür.

**Test:**
```
"TBK m. 6'yı getir"                          → tr_mevzuat_ara + tr_mevzuat_madde_getir
"Yargıtay 9. HD iş kazası kararı"             → tr_ictihat_ara(chamber="H9")
"EPDK lisanssız üretim kararları"             → tr_kurum_karari_ara(kurum="epdk")
"bir bankanın faaliyet izninin kaldırılması"  → tr_semantik_ara(kurum="bddk", mode="semantic")
"kişisel verilerin korunması" (İspanya)       → es_search_legislation, LO 15/1999 ve LO 7/2021 dönmeli
```

**Kaynak:** `github.com/beerbottle90/arthurlegal-mcp` (Türkiye backend'i: `github.com/beerbottle90/arthurlegal-mcp/tree/master/arthur-tr-hukuk-mcp`) — Fly.io'da barındırılıyor,
indeksler image'a gömülü, semantik arama Voyage AI (`voyage-4-lite`) ile.

> **Paket kullanmadan doğrudan bağlanmak.** Aynı uç, ArthurLegal paketi yüklemeden herhangi bir MCP
> istemcisinde tek başına çalışır (Streamable HTTP, auth yok):
> - **Claude (claude.ai / Claude Desktop):** Settings → Connectors → Add custom connector, URL `https://arthurlegal-mcp.fly.dev/mcp`
> - **Claude Code:** `claude mcp add --transport http arthurlegal https://arthurlegal-mcp.fly.dev/mcp`
> - **Cursor, VS Code gibi JSON yapılandırmalı istemciler:** `{"mcpServers": {"arthurlegal": {"url": "https://arthurlegal-mcp.fly.dev/mcp"}}}`
> - **Yalnız yerel (stdio) sunucu başlatan istemciler:** komut olarak `npx -y mcp-remote https://arthurlegal-mcp.fly.dev/mcp`
>
> Bağlandıktan sonra `status` aracını çağırın. Ayrıntı: [github.com/beerbottle90/arthurlegal-mcp](https://github.com/beerbottle90/arthurlegal-mcp#use-it-directly)

> **Kurulmazsa ne olur?** Paket çalışmaya devam eder: Türkiye dâhil bu on beş yargı çevresi
> WebFetch yoluna düşer (Türkiye'de içtihat araması yapılamaz, AZ'de **statü doğrulanmaz**),
> doktrin ve sözleşme emsali kapsam dışı kalır — asistan bunu çıktısında belirtir.

---

## Adım 4b — Ek MCP connector'ları (isteğe bağlı)

Üç ayrı connector: İsviçre içtihadı + İsviçre mevzuatı + ABD içtihadı.

### 4b-1 · OpenCaseLaw.ch — İsviçre İçtihadı

Swiss OR sözleşmeleri, ICC/Swiss tahkim kararları için.

1. **Customize → Connectors → + Add custom connector**
2. **Name:** `OpenCaseLaw.ch`
3. **URL:** `https://mcp.opencaselaw.ch/sse`
4. Auth bölümünü **boş bırak** (auth yok)

**Kapsam:** 972K+ BGer/BVGer/26 kanton kararı, Fedlex mevzuat entegrasyonu (CC0).

### 4b-2 · CourtListener — ABD İçtihadı

**Resmi MCP sunucusu vardır ve Anthropic connector dizininde listelidir** —
custom connector eklemek gerekmez:

1. **Customize → Connectors → Browse Connectors**
2. Listeden **CourtListener**'ı seç → **Add**
3. CourtListener hesabına yetki ver — **OAuth 2.0** (Dynamic Client Registration;
   ön-kayıt ve API anahtarı gerekmez)

**Kapsam:** ABD federal/eyalet mahkeme kararları, PACER dosyaları, atıf ağı,
sözlü duruşma kayıtları ve **citation verification**. Free Law Project işletir.

> ⚠️ **Citation verification zorunludur.** Bir ABD kararına atıf yapılacaksa önce
> CourtListener'da doğrulanır (karar var mı, citation doğru mu, overrule edilmiş
> mi). Doğrulanmayan karar `[model bilgisi — doğrulayın]` ile işaretlenir, asla
> `[CourtListener]` etiketi almaz. Ayrıntı: `courtlistener-rehberi.md`.

### 4b-3 · Fedlex — İsviçre Mevzuatı

Verbatim madde metni ve değişiklik geçmişi için; Anthropic connector dizininde:

1. **Customize → Connectors → Browse Connectors**
2. Listeden **Fedlex**'i seç → **Add**

**Kapsam:** İsviçre federal mevzuatı — madde metni, kanun tam metni, değişiklik
listesi, başlığa göre arama. Tahkim ve Swiss OR işlerinde madde metninin
verbatim gerekmesi hâlinde OpenCaseLaw.ch entegrasyonuna göre daha doğrudandır.

> Connector kurulmazsa Fedlex WebFetch ile de çalışır (`fedlex.admin.ch`) —
> bkz. `switzerland-caselaw-rehberi.md`.

---

## Adım 4c — Connector gerektirmeyen yargı çevreleri

Aşağıdakiler WebFetch veya doğrudan API ile otomatik çalışır:

| Yargı | Auth | Rehber |
|---|---|---|
| 🇬🇧 UK | Yok | `uk-legislation-rehberi.md` |
| 🇺🇸 US Mevzuat (GovInfo) | Ücretsiz API key | `us-legislation-rehberi.md` |
| 🇪🇺 AB/EU + CJEU + ECHR | Yok | `eu-legislation-rehberi.md` |
| 🇩🇪 Almanya | Yok | `germany-legislation-rehberi.md` |
| 🇫🇷 Fransa | Yok | `france-legislation-rehberi.md` |
| 🇮🇹 İtalya | Yok | `italy-legislation-rehberi.md` |
| 🇯🇵 Japonya | Yok | `japan-legislation-rehberi.md` |
| 🇷🇺 Rusya ⚠️ (yalnız yaptırım/KYC) | Yok | `russia-legislation-rehberi.md` |
| 🇦🇿 Azerbaycan (içtihat/EN — mevzuat için Adım 4d) | Yok | `azerbaycan-hukuk-rehberi.md` |
| 🇨🇳 Çin (HuggingFace/twang2218) | Yok | `cin-hukuku-rehberi.md` |
| 🇷🇸 Sırbistan (paragraf.rs) | Yok | `sirbistan-hukuku-rehberi.md` |

> 🇺🇸 **ABD içtihadı bu tabloda değildir** — CourtListener MCP connector'ı ile
> gelir (Adım 4b-2). 🇨🇭 **İsviçre** de öyle: içtihat 4b-1, mevzuat 4b-3.

---

## Adım 4d — TR Legal MCP (isteğe bağlı: AİHM, KİK, Sayıştay, Reklam Kurulu, KDK, TBB, HSK)

ArthurLegal MCP'nin Türkiye backend'i şu kaynakları bilinçli olarak taşımaz, çünkü
resmî uçları güvenilir cevap vermiyor ya da kapsam dışı: **KİK** (EKAP v2 imzalı API 500
döndürüyor), **Sayıştay** (WAF her sorguya 418 veriyor), **TÜRKPATENT** (karar veritabanı yok,
portal reCAPTCHA'lı), **İSTAÇ** (site erişilemez), **AİHM**, **Reklam Kurulu**, **KDK**,
**TBB**, **HSK**. Bunlara ihtiyacınız varsa saidsurucu'nun ücretli **yargi-mcp-pro**
sunucusunu ikinci bir connector olarak ekleyebilirsiniz:

1. **Customize → Connectors → + Add custom connector**
2. **Name:** `TR Legal MCP`
3. **URL:** `https://yargi-mcp-pro-production.up.railway.app/mcp`
4. **Add** → WorkOS izin sayfasında giriş yap / hesap oluştur

Asistan bu connector'ı yalnız yukarıdaki kaynaklar için kullanır (`aihm_ictihat_ara`,
`kurum_karari_ara(kurum="kik" | "sayistay" | "reklam" | "kdk" | "tbb" | "hsk")`); mevzuat,
içtihat ve diğer kurum kararları için `tr_` araçları önceliklidir. Kurulu değilse bu
kaynaklar WebFetch ile çekilir veya çıktıda "çekilmedi" denir; çalışmayan kaynak çalışıyormuş
gibi gösterilmez.

---

## Adım 5 — Arthur Mask (önerilir, isteğe bağlı: belgeleri bilgisayarınızda maskeleyin)

Arthur Mask, şirket belgelerini (sözleşme, yazışma, ihtarname, dava evrakı) Claude'a vermeden önce **kendi bilgisayarınızda**
maskeler: adlar, şirketler, TCKN, VKN, IBAN, adres, telefon, e-posta, dosya numarası gibi
bilgiler `{{KİŞİ-01}}`, `{{ŞİRKET-02}}` gibi etiketlere dönüşür, gerçek değerler
bilgisayarınızdaki şifreli kasada kalır. Claude yalnız maskeli metni görür; cevap yine
bilgisayarınızda gerçek adlarla Word veya UDF olarak açılır. Program çevrimdışı çalışır.

> ⚠️ **Yalnız Claude Desktop (Windows).** claude.ai web sürümünde ve mobil uygulamalarda
> çalışmaz: claude.ai'deki connector'lar Anthropic'in bulutundan çağrılır ve bulut,
> bilgisayarınızdaki programa ulaşamaz. ArthurLegal Project'inizi Claude Desktop'tan açın;
> Project'ler web ile masaüstü arasında ortaktır.

**Gereksinim:** Windows 10 veya 11 (64 bit) · [Claude Desktop](https://claude.ai/download) ·
yaklaşık 4 GB boş disk · 8 GB RAM önerilir.

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

**Test:** Arthur Mask'e bir örnek belge bırakın, incelemeyi onaylayın, gösterilen komutu
(`Arthur Mask'teki belge-1'i incele`) Claude Desktop'taki ArthurLegal Project sohbetine
yapıştırın. Orijinal belgeyi sohbete ayrıca eklemeyin.

Günlük kullanım, kırmızı hat, sızıntı denetimi ve sorun giderme: [ARTHUR-MASK.md](ARTHUR-MASK.md).

> **Kurulmazsa ne olur?** Paket aynen çalışır. Asistan, sohbete tanımlanabilir kişisel veri
> yapıştırıldığında sohbet başına bir kez kısa bir hatırlatma yapar; işi durdurmaz.
> Arthur Mask takma adlandırma yapar, anonim hâle getirmez; KVKK, ticari sır ve gizlilik
> yükümlülükleri kullanıcıda ve şirkette kalır.

---

## Adım 6 — company-profile.md'yi Doldur

`knowledge/company-profile.md` dosyasındaki `[DOLDUR]` alanlarını şirketinize özgü bilgilerle tamamlayın:

1. Dosyayı bir metin editöründe açın
2. `[DOLDUR]` etiketli tüm alanları gerçek bilgilerle değiştirin
3. Eski dosyayı projeden silin → güncellenmiş dosyayı yeniden yükleyin

**Alternatif:** Proje chat'inde `/<plugin>:cold-start-interview` yazarak asistanın soruları size yönlendirmesini ve yanıtları company-profile formatına dönüştürmesini sağlayabilirsiniz.

> ⚠️ Gerçek şirket verilerini bu klasörün GitHub kopyasına eklemeyin — sadece yerel kullanım için doldurun.

---

## Adım 7 — İlk Komutu Dene

```
/commercial-legal:nda-review

[NDA metnini yapıştır veya yükle]
```

veya doğrudan:
```
SaaS sözleşmesi inceleyeceğim, vendor olarak biz, customer Avrupa'dan.
Limitation of liability ve KVKK maddelerine odaklan.
```

---

## Kullanılabilir Plugin'ler ve Skill'ler

Her plugin için `knowledge/skills/<plugin>__skills.md` dosyasını açıp `## Icindekiler` bölümüne bakın.

| Plugin | Örnek skill'ler |
|---|---|
| `commercial-legal` | `nda-review`, `governing-law-review`, `saas-msa-review`, `vendor-agreement-review` |
| `corporate-legal` | `closing-checklist`, `board-minutes`, `diligence-issue-extraction`, `tabular-review` |
| `employment-legal` | `internal-investigation`, `termination-review`, `international-expansion`, `leave-tracker` |
| `privacy-legal` | `dsar-response`, `pia-generation`, `dpa-review`, `reg-gap-analysis` |
| `regulatory-legal` | `reg-feed-watcher`, `gap-surfacer`, `policy-diff`, `comments` |
| `ip-legal` | `cease-desist`, `clearance`, `fto-triage`, `portfolio` |
| `litigation-legal` | `isg-incident-response`, `outside-counsel-brief`, `case-intake`, `settlement-eval` |
| `tax-legal` | `tax-litigation-prep`, `kdv-otv-iade-review`, `transfer-pricing-review`, `gib-ozelge-request` |
| `administrative-legal` | `ced-itiraz`, `epdk-proaktif-gorus`, `idari-dava-prep` |
| `energy-finance` | `project-finance-review`, `ma-diligence-energy`, `jv-agreement-review`, `lng-offtake-review` |
| `contract-drafting` | `redline-contract`, `belge-turet`, `versiyon-karsilastir`, `tadil-protokol` |
| `legal-research` **(YENİ)** | `kaynak-secimi`, `az-mevzuat`, `karsilastirmali-doktrin`, `sozlesme-emsali` |

---

## Sınırlamalar (Claude Code'a Kıyasla)

| Özellik | Claude Code | Claude.ai Projects |
|---|---|---|
| `/<plugin>:<skill>` slash command | ✓ resmi | ⚠ simüle (system prompt anlar) |
| **ArthurLegal MCP** (Türkiye + 14 yargı çevresi + tapu-kadastro, 121 araç) | ✓ `.mcp.json` | ✓ tek custom connector (auth yok) |
| **TR Legal MCP** (isteğe bağlı: AİHM, KİK, Sayıştay…) | ✓ `.mcp.json` | ✓ custom connector (OAuth) |
| **OpenCaseLaw.ch MCP** | ✓ `.mcp.json` | ✓ custom connector |
| Araç çağrısı zaman aşımı | uzun | **100 saniye — sabit** |
| Tüm WebFetch kaynakları | ✓ | ✓ |
| Hook'lar (pre/post tool) | ✓ | ✗ |
| Local dosya okuma | ✓ | Drive connector + upload |
| Memory persist (matter workspaces) | ✓ | Sınırlı — knowledge statik |

---

## Sık sorulan sorular

**S: Şirket belgesini Claude'a nasıl güvenle veririm?**
A: Claude Desktop (Windows) kullanıyorsanız belgeyi önce Arthur Mask'e bırakın, incelemeyi onaylayın ve yalnız gösterilen komutu sohbete yapıştırın; orijinal belgeyi sohbete eklemeyin. Claude yalnız maskeli metni görür. Maskeleme takma adlandırmadır, anonim hâle getirme değildir ve tespit olasılığa dayalıdır: göndermeden önce maskeli kopyaya bakın, "Claude'a giden" panelini ve sızıntı denetimini kullanın. KVKK, ticari sır, gizlilik sözleşmeleri (NDA) ve şirketin bilgi güvenliği politikasından doğan sorumluluk kullanıcıda ve şirkette kalır. claude.ai web ve mobilde Arthur Mask çalışmaz; orada tanımlanabilir kişisel veriyi ve ticari sırrı paylaşmadan önce kendiniz ayıklayın. Ayrıntı: [ARTHUR-MASK.md](ARTHUR-MASK.md).

**S: Arthur Mask'i kurmazsam paket çalışır mı?**
A: Evet. Arthur Mask isteğe bağlıdır; paket, connector'lar ve skill'ler aynen çalışır.

---

## Güncelleme

Yeni bir sürüm geldiğinde:

1. Değişen dosyaları yerel olarak güncelleyin
2. Claude.ai projesinde ilgili dosyaları silin → güncellenmiş halleri yeniden yükleyin
3. `SYSTEM_PROMPT.md` değiştiyse Custom Instructions'ı güncelleyin

v1.9.1'den v1.10.0'a geçiş: `SYSTEM_PROMPT.md` yeniden yapıştırılır (bölüm 5 ile 8: tapu-kadastro `tkgm_` araçları, Türkiye 0.5.0). Project knowledge'a `knowledge/references/tapu-kadastro-rehberi.md` eklenir; `knowledge/references/yargi-mcp-rehberi.md` ve `knowledge/references/mevzuat-mcp-rehberi.md` yenilenir. Doldurduğunuz `company-profile.md` dosyasını değiştirmeyin; isterseniz mevzuat takip kanallarına ArthurLegal Tapu (`tkgm_`) satırını elle ekleyin. ArthurLegal yerel kurulumu (2.1.0) paket dosyalarını kendiliğinden yeniler.

v1.8.0'dan v1.9.0'a geçiş: `SYSTEM_PROMPT.md` yeniden yapıştırılır (bölüm 6 ve 7: `konu` taraması, tarih aralığı, arşiv kapsamı). Project knowledge'da şu beş dosyayı yenileyin: `knowledge/references/mevzuat-mcp-rehberi.md`, `knowledge/references/yargi-mcp-rehberi.md`, `knowledge/references/reg-feed-haftalik-sablon.md`, `knowledge/references/source-catalog.md`, `knowledge/skills/regulatory-legal__skills.md`. Connector adresi değişmedi; bağlandıktan sonra `status` çağırın, `backend_status.tr.version` 0.4.0 veya üstü olmalıdır.

v1.7.0'dan v1.8.0'a geçiş: `SYSTEM_PROMPT.md` yeniden yapıştırılır (yeni bölüm 9, Arthur Mask); `knowledge/references/arthur-mask-rehberi.md` Project knowledge'a eklenir. Arthur Mask kullanacaksanız Adım 5'i uygulayın ve Project'i Claude Desktop'tan açın. Connector adresleri değişmedi.

---

*ArthurLegal Corporate Assistant v1.10.0 — https://github.com/beerbottle90/ArthurLegal*
