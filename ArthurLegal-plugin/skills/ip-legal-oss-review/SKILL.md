---
name: ip-legal-oss-review
description: >
  Açık kaynak lisans uyum kontrolü: bağımlılık listesi, tek kütüphane ya da açık
  kaynak yapılacak kendi kodumuz. Manifest, SBOM ya da depo copyleft
  yükümlülükleri ve lisans uyumu bakımından incelenirken, bir kütüphanenin
  ürüne girip giremeyeceği sorulduğunda ya da kod açık kaynak yapılmadan önce
  kullan. Lisans mekaniği yargı çevresinden bağımsızdır; Türk hukuku çerçevesi:
  bilgisayar programı eserdir (FSEK m. 1/B-g, 2), lisans ruhsattır (m. 48/2),
  çoğaltma, yayma, umuma iletim hakları (m. 22-25), kullanıcı hakları (m. 38).
argument-hint: "[manifest / SBOM yolu | paket adı | depo yolu | metin]"
---

# /oss-review

Bağımlılıkları lisans ailesine göre sınıflandırır, yükümlülükleri dağıtım modeline eşler, lisansı bilinmeyen ve açık kaynak görünümlü ama OSI onaylı olmayan paketleri işaretler, eylem önerir: uy, değiştir, çıkar, avukat incelemesi, ticari lisans al.

## Talimat

1. **Profili yükle:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Yer tutucu varsa dur: "Önce `/arthurlegal:ip-legal-cold-start-interview` — pratik profilinizi (ve varsa açık kaynak politikanızı) öğrenmeliyim." Profil yüklü bir **OSS policy** gösteriyorsa onu da oku — kabul / inceleme / yasak lisanslar için tek doğru kaynak odur.
2. **Kapsam:** bağımlılık listesi (package.json, requirements.txt, go.mod, Gemfile, Cargo.toml, pom.xml, SBOM, kilit dosyası), tek kütüphane ya da açık kaynak yapılacak kendi kodumuz. Yol verildiyse dosyadan çıkar, yoksa sor.
3. **Dağıtım modelini** yükümlülükleri sınıflandırmadan önce belirle — aynı liste farklı modellerde farklı yükümlülük doğurur.
4. **Akışı izle:** metadata'ya değil gerçek lisans metnine bak; lisansı bilinmeyeni "inceleme gerekir" diye işaretle (varsayılan izinli değil); OSI onaylı olmayan kaynağı-açık lisansları (SSPL, BUSL, Commons Clause, Elastic License, fair-source) açık kaynak sayma; açık kaynak yapılacak kodda giden lisansın her gömülü bağımlılıkla uyumunu kontrol et.
5. **Notu yaz** (şablon aşağıda).
6. **Karar duruşu:** copyleft tetikleyicisi tartışmalı bir soruya dayanıyorsa (AGPL "ağ üzerinden etkileşim", GPL-3.0 "conveying", LGPL bağlama kapsamı) avukata işaretle. Güçlü copyleft ya da lisansı bilinmeyen her şey ürüne girmeden ya da kod yayımlanmadan önce avukata gider.

## Bağlantılı çalışma

Açık kaynak onay talepleri genelde bir iş takip sisteminden gelir (Jira, Linear, Asana). Bağlıysa talepleri izler, bilette eksik bilgiyi ister, lisans ailesi sınıflandırmasını döner ve onay durumunu takip eder. Bağlı değilse bileti yapıştırın, tek tek ele alırım.

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla; açık ve aktif matter yoksa sor; `matter.md` sapmalarını yükle; çıktılar `matters/<matter-slug>/`; `Cross-matter context` `on` değilse başka matter okunmaz.

## Amaç ve sınır

Bağımlılık ağacında hangi lisanslar var, dağıtım modelinde hangi yükümlülükleri tetikliyor, her biri için ne yapılmalı — avukatın (ya da avukata erişimi olan mühendisin) üzerine eylem yapabileceği not. **Bu ilk geçiş sınıflandırmadır.** Copyleft analizi dağıtım modeline, bağlama derecesine, yargı çevresine ve mahkemede sınanmamış sorulara dayanır. Güçlü copyleft ya da bilinmeyen lisans → avukat değerlendirir.

## Türk hukuku çerçevesi (kısa)

- **Bilgisayar programı eserdir:** her biçimde ifade edilen bilgisayar programları ve program sonucu doğurması koşuluyla hazırlık tasarımları ilim ve edebiyat eseridir (FSEK m. 2/1-1; tanım m. 1/B-g). Arayüz dahil, programın herhangi bir ögesine temel oluşturan düşünce ve ilkeler eser değildir (m. 2/son).
- **Lisans = ruhsat:** mali hakları kullanma yetkisi başkasına bırakılabilir (m. 48/2). Açık kaynak lisansı bu yetkiyi koşula bağlı verir.
- **Hangi fiil hangi hak:** programın yüklenmesi, görüntülenmesi, çalıştırılması, iletilmesi ve depolanması geçici çoğaltma gerektirdiği ölçüde çoğaltma hakkına girer (m. 22/3); dağıtım yayma hakkıdır (m. 23); erişime sunma umuma iletimdir (m. 25/2). Lisansların "distribution / conveying / network interaction" tetikleyicileri bu haklarla birebir örtüşmez — lisans metni belirleyicidir.
- **Lisans koşuluna aykırılığın niteliği:** koşula uymayan kullanımın sözleşmeye aykırılık mı yoksa izinsiz kullanım (FSEK m. 68 bedel talebi, m. 71 ceza) mı sayılacağı **tartışmalı — içtihadı kontrol et:** `tr_ictihat_ara(courts=["YARGITAYKARARI"], query="+açık +kaynak +lisans")`. Dönen künyeyi birebir kullan; sonuç yoksa "Türk içtihadı bulunamadı" de, uydurma.
- **Yazılı şekil:** mali haklara dair sözleşmelerin yazılı olması ve hakların ayrı ayrı gösterilmesi şartı (m. 52) imzasız, metin olarak dağıtılan açık kaynak lisanslarına nasıl uygulanır — **tartışmalı.** Giden kodda kendi lisansımızı seçerken ve katkı sözleşmelerinde (CLA) yazılı ve hakları sayan metin tercih et.
- **Kullanıcı hakları:** yasal edinen kişinin yükleme, çalıştırma, hata düzeltme ve yedek kopya hakkı sözleşmeyle önlenemez; araişlerlik için kod çevirisi şartlı serbesttir (m. 38/4-7).
- **Uygulanacak hukuk:** hak, koruma talep edilen ülkenin hukukuna tabidir (MÖHUK m. 23/1). Yabancı lisans yorumu için: AB yazılım direktifi `eu_search_eu_law(query="legal protection of computer programs")`; EUPL için `eu_search_eu_law(query="European Union Public Licence")`.

**Ev örneği:** ArthurLegal kendi kaynak kataloğunda (`knowledge/references/oss-source-catalog.json`) her lisansı **kaynağında** doğrular, doğrulama tarihini yazar ve AGPL/ticari olmayan (NC) lisansları "izolasyon ya da karar gerektirir" diye ayırır. Aynı disiplini uygula: her bulgu = lisans adı + nereden okunduğu + okuma tarihi.

## Akış

### Adım 1: Kapsam

1. **Bağımlılık listesi** → her girdiyi sınıflandır, yükümlülükleri topla.
2. **Tek kütüphane** → paketi sınıflandır, varsa geçişli bağımlılıklarını yürü.
3. **Kendi kodumuz (açık kaynak yapılacak)** → gömülü (doğrudan ve geçişli) lisansları, seçilen giden lisansla uyumu ve LICENSE/NOTICE dosyalarını kontrol et.

### Adım 2: Dağıtım modeli (lisans listesinden sonra en önemli girdi)

> Nasıl dağıtılacak? 1) **SaaS / barındırılan hizmet** 2) **Dağıtılan ikili** (masaüstü, mobil, kurulum, CLI) 3) **Yalnız şirket içi** 4) **Gömülü / donanım yazılımı**

| Dağıtım | Önemli lisanslar |
|---|---|
| SaaS | AGPL (ağ tetikleyicisi), arayüzde izinli lisans atfı, rakip hizmet olarak sunuluyorsa SSPL/BUSL/Elastic |
| Dağıtılan ikili | GPL, LGPL, MPL, EPL (dağıtımda tetiklenir), izinli lisans atfı |
| Şirket içi | Çoğu copyleft tetiklenmez (dağıtım yok); atıf yine iyi uygulama. Şirket dışı kullanıcılar ağ üzerinden etkileşiyorsa AGPL tetiklenir. Grup şirketlerine aktarım "şirket içi" mi, dağıtım mı — **tartışmalı**, ayrı işaretle. |
| Gömülü | GPL uyumu özellikle zor (kaynak + yeniden üretilebilir derleme + bazı durumlarda kurulum bilgisi). Göndermeden önce planla. |

### Adım 3: Her bağımlılığı sınıflandır

Gerçek lisans metnini oku; LICENSE dosyası yanlış, paket yöneticisi metadata'sı eski olabilir (dosya MIT der, başlıklar GPL der; README Apache der ama lisans dosyası yok).

| Grup | Örnekler | Ana yükümlülük |
|---|---|---|
| **İzinli** | MIT, BSD-2/3-Clause, Apache-2.0, ISC, Zlib | Atıf, lisans metnini koruma; Apache-2.0'da patent lisansı + NOTICE |
| **Zayıf copyleft** | LGPL-2.1/3.0, MPL-2.0, EPL-1.0/2.0, CDDL | Dosya ya da kütüphane düzeyinde kaynak açma; bağlama kuralları değişir |
| **Güçlü copyleft** | GPL-2.0, GPL-3.0, AGPL-3.0, OSL, EUPL (sürüme göre) | Geniş kaynak açma; AGPL ağ kullanımına uzanır |
| **Kamu malı / adanma** | CC0, Unlicense, WTFPL | Genelde yükümlülük yok; ama "kamu malına adama" her hukukta tanınmaz — Türk hukukunda manevi hakların devredilemez çekirdeği (FSEK m. 14/3, 16/3) karşısında etkisi **tartışmalı** |
| **OSI onaylı olmayan, kaynağı açık** | SSPL, BUSL, Commons Clause, Elastic License, Confluent Community, fair-source | Açık kaynak değil — ticari ya da rakip hizmet kullanımını kısıtlar; metni oku |
| **Diğer / özel / bilinmeyen** | üreticiye özel, lisans dosyası yok, dosya ile başlık çelişiyor | Dur — varsayılan izinli sayma |

İşaretle: çift lisanslı paketler (hangisini kullanıyoruz?) · bakımı bırakılmış paketler · kendi ağacında copyleft taşıyan izinli paketler · lisansı yakın zamanda değişenler (sabitlenen sürüm hangi lisansta?).

### Adım 4: Yükümlülükleri dağıtım modeline eşle

```markdown
### [paket@sürüm] — [Lisans] · [nereden okundu — tarih]
**Sınıf:** [İzinli / Zayıf copyleft / Güçlü copyleft / Kamu malı / OSI dışı / Bilinmeyen]
**Dağıtımımız için yükümlülükler ([SaaS / ikili / şirket içi / gömülü]):**
- [ ] [ör. "Uygulamayla birlikte NOTICES dosyasında atıf"]
- [ ] [ör. "Değiştirip dağıtırsak değişikliklerin kaynağını yayımla"]
- [ ] [ör. "AGPL ağ tetikleyicisi — değiştirilmiş sürüme ağ üzerinden erişen kullanıcıya kaynak sunulmalı"]
**Risk:** 🔴 | 🟠 | 🟡 | 🟢
**Öneri:** [Uy | [alternatif] ile değiştir | Çıkar | Göndermeden avukat | [üretici]'den ticari lisans]
```

> **Copyleft bağımlılık nasıl tüketiliyor?** Statik bağlama/birlikte derleme: tek ikili — copyleft tetiklenmesine güçlü işaret. Dinamik bağlama: LGPL açıkça izin verir; GPL'de tartışmalı (FSF türev der, karşı görüş var). Başlık dosyası/inline fonksiyon: ne kadar alındığına bağlı. Alt süreç/IPC: genelde türev değil. Ağ API çağrısı: çoğu lisansta hayır; **AGPL**'de ağ üzerinden sunmak tetikler, mikro hizmet arkasındaki AGPL bileşen de. Dosya kapsamlı copyleft (MPL): yalnız değiştirilen dosyalar.
>
> **Önem derecesi buna bağlıdır.** Kapalı üründe statik bağlı LGPL 🔴; dinamik bağlı LGPL 🟢. Aynı lisans, zıt derece.

| Seviye | Anlamı |
|---|---|
| 🔴 Kritik | Tetikleyen dağıtımda güçlü copyleft (dağıtılan ikilide GPL, SaaS'ta AGPL). İş modeliyle çatışan OSI dışı lisans (yönetilen hizmet kurarken SSPL). Taşıyıcı pakette belirlenemeyen lisans. |
| 🟠 Yüksek | Hazırlığı yapılmamış zayıf copyleft yükümlülüğü; seçilen lisansı belirsiz çift lisans; dosya ile başlık çelişkisi. |
| 🟡 Orta | Derlemeye bağlanmamış atıf yükümlülüğü (NOTICES/LICENSE eksik); tüketim biçimine göre tetiklenebilecek geçişli copyleft. |
| 🟢 Düşük | Yükümlülüğü karşılanmış izinli lisans; tetiklemeyen modelde copyleft. |

### Adım 5: Arıza kalıpları (notun en üstünde)

Lisansı bilinmeyen → "inceleme gerekir", gönderim kararını durdurur · LICENSE dosyası ile başlık çelişkisi · uyumsuz kombinasyonlar (GPL-2.0-only + Apache-2.0 bilinen uyumsuzluk; MPL/EPL/GPL birleşimlerini dikkatle kontrol et) · açık kaynak kılığında OSI dışı lisans (GitHub rozetine güvenme) · lisans değişikliği (önceki sürüm izinli, güncel sürüm kaynağı-açık — sabitleme önemli).

### Adım 6: Giden kod kontrolü (açık kaynak yapılacaksa)

- Seçilen giden lisans her gömülü bağımlılıkla uyumlu mu (GPL kod gömülüyken MIT ile yayımlanamaz — birleşik eser GPL olur)?
- LICENSE ve NOTICE dosyaları doğru mu; üçüncü kişi lisans metinleri paketlenmiş mi?
- Depo geçmişinde kapalı/gizli kod, müşteri verisi, kişisel veri ya da gömülü kimlik bilgisi yok mu?
- **Hak zinciri:** kodu yazan çalışanların hakları m. 18/2 ile işverence kullanılıyor mu, dış katkıcılar (danışman, freelancer) yazılı ve hakları sayan devirle mi (FSEK m. 52) çalıştı? Eksikse yayımlamadan önce `/arthurlegal:ip-legal-ip-clause-review`.
- Proje adı ve logosu için marka politikası (telif lisansından ayrı) — gerekirse `/arthurlegal:ip-legal-clearance`.

### Adım 7: Notu birleştir

Başa `## Outputs` üst başlığı. Not ve bağımlılık listesi gizli olabilir; dar çevrede dağıt; dar çevre dışındaki bir mühendislik biletine eklemeden önce başlığı çıkar.

> **Sessiz tamamlama yok.** Araç bir kural için az sonuç döndürürse (AGPL ağ tetikleyicisinin bir ülkede uygulanabilirliği, GPL-3.0 patent hükmünün kapsamı, yakın zamanda lisansı değişen paketin güncel metni) bulduğunu bildir ve dur; seçenek sun.
>
> **Kaynak etiketi:** `[OSI]`, `[SPDX]`, `[FSF]`, `[SFC/SFLC]`, araç adı, `[kullanıcı verdi]` (depodan okunan lisans metni), `[model bilgisi — doğrula]`, `[web araması — doğrula]`. Türk mevzuatı için `[ArthurLegal TR — 5846 FSEK m. X — GG.AA.YYYY]`. Etiketleri silme.

```markdown
[ÜST BAŞLIK — profil ## Outputs]
# OSS İncelemesi: [Proje / liste / paket]
**İncelendi:** [tarih] · **Kapsam:** [liste / tek kütüphane / giden kod] · **Dağıtım modeli:** [SaaS / ikili / şirket içi / gömülü]
## Sonuç
[İki cümle. Gönderilebilir mi? Önce ne olmalı?]
**İncelenen paket:** [N] · **Sınıflar:** [N izinli, N zayıf copyleft, N güçlü copyleft, N kamu malı, N OSI dışı, N bilinmeyen] · **Bulgular:** [N]🔴 [N]🟠 [N]🟡 [N]🟢
**Onay gereken:** [profildeki isim]
## Üst bayraklar
[bilinmeyen lisans, çelişki, OSI dışı, uyumsuz kombinasyon]
## Pakete göre
[Adım 4 blokları, önem sırasıyla]
## Yargı çevresi notu
[AGPL ağ tetikleyicisi mahkemelerde geniş ölçüde sınanmadı; GPL-3.0 patent hükmü ülkeye göre farklı okunur; kamu malına adanma her yerde tanınmaz; Türk hukukunda lisans ihlalinin niteliği ve m. 52 uygulaması tartışmalı. Aşağı akış dağıtımında (kodu içeren tedarik sözleşmeleri) hukuk seçimi ve profilde eskalasyon işaretli yargı çevreleri.]
## Giden kod kontrolü (varsa)
## Onay yönlendirmesi
> ⚠️ **İnceleyen notu:** Güçlü copyleft ve lisansı bilinmeyen paketler gönderimden önce avukat onayı ister.
```

## Karar duruşu

Lisans güvenle sınıflandırılamıyorsa **"inceleme gerekir"** de — izinli deme. Lisans riskini düşük göstermek tek yönlü kapıdır: izinli varsayımıyla verilen gönderim kararı aylar sonra kaynak açma yükümlülüğüne ya da tedbir talebine döner. Fazla işaretlemek iki yönlüdür; avukat listeyi daraltır. Tetikleyici tartışmalı bir soruya dayanıyorsa avukata işaretle, iki yönü göster.

## Teslimden önce kalite kontrolü

- [ ] Profil ve varsa OSS policy yüklendi
- [ ] Dağıtım modeli yükümlülüklerden önce belirlendi
- [ ] Her bağımlılığın (varsa geçişlilerin) sınıfı var; bilinmeyenler işaretli
- [ ] Copyleft ya da OSI dışı her bulguda lisans metni okundu (yalnız metadata değil); okuma yeri ve tarihi yazıldı
- [ ] Etiketler yerinde; onaylayan profildeki isim; üst başlık eklendi

## Kapanış

`## Outputs`'taki sonraki adım ağacıyla kapat; seçenekleri bu çıktıya göre özelleştir. Tarama ~10 paketi aştıysa ya da kullanıcı isterse panoyu öner (`## Outputs → Dashboard offer for data-heavy outputs`): lisans ailesine göre sayılar (izinli / zayıf copyleft / güçlü copyleft / AGPL / tescilli / bilinmeyen), risk dağılımı, önem ve sürümlü bulgu tablosu.
