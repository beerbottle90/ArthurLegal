---
name: commercial-legal-saas-msa-review
description: >
  Referans: SaaS / abonelik sözleşmelerini abonelik ilişkisinde en çok can
  yakan şartlara odaklanarak inceler — otomatik yenileme ve fesih bildiriminin
  şekli (TTK m. 18/3), fiyat artışı ve döviz (TBK m. 99), tek taraflı
  değişiklik (TBK m. 24), veri çıkışı, hizmet seviyesi, alt işleyenler, yapay
  zekâ eğitim hakları. Tüketici karşı tarafta ise 6502 m. 52'yi işaretler.
  SaaS ya da abonelik sözleşmesi tespit edildiğinde /arthurlegal:commercial-legal-review
  tarafından yüklenir.
user-invocable: false
---

# /saas-msa-review — SaaS / Abonelik Sözleşmesi İncelemesi

SaaS sözleşmesinin risk profili tek seferlik tedarikten farklıdır: bedel yenilemelerle katlanır, veri birikir, geçiş maliyeti her ay büyür. Bu skill playbook'un standart kontrolünü (`/arthurlegal:commercial-legal-vendor-agreement-review`) çalıştırır ve üstüne abonelikte en çok can yakan şartlar için bir katman ekler.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:commercial-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Yargı çevresi varsayımı ve kaynak disiplini

Otomatik yenileme, fiyat, veri taşınabilirliği ve alt işleyen kuralları yargı çevresine duyarlıdır. Bu inceleme eklenti ayarındaki pozisyonları ve Türk hukukunu esas alır. Sözleşme başka bir hukuku seçmişse ya da kullanıcılar AB'deyse işaretle; analiz olduğu gibi aktarılamaz → `/arthurlegal:commercial-legal-governing-law-review` (AB: `eu_search_eu_law`; İngiltere: `uk_search_legislation`; Almanya: `de_gesetz_ara`).

- **Sessiz tamamlama yok.** Araç bir emredici kural için az sonuç dönerse dur: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Düşük güvenli kaynağı kabul kararını avukat verir.
- **Kaynak etiketi:** `[ArthurLegal TR — 6098 m. X — GG.AA.YYYY]`, yabancı araç için `[ArthurLegal UK/DE/EU — … — GG.AA.YYYY]`, `[web — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`. Etiketleri silme ya da birleştirme.

## Playbook'u yükle

**Hangi taraftayız?** Karşı taraf size platformunu satıyorsa alım tarafı; siz SaaS sağlayıcısıysanız ve karşı taraf müşterinizse satış tarafı. Belli değilse (bayilik, beyaz etiket) sor: "[[Müvekkil]] bu sözleşmede hangi tarafta — sağlayıcı mı, müşteri mi?" Eşleşen bölümü oku (`### Sales-side playbook` / `### Purchasing-side playbook`), çıktıda yaz. `[Not configured]` ise dur ve `/arthurlegal:commercial-legal-cold-start-interview --side <side>` öner.

Önce eşleşen tarafın genel playbook'unu (sorumluluk, tazmin, fesih, hukuk) vendor-agreement-review'daki gibi eksiksiz uygula. Sonra `## Playbook` → eşleşen taraf → `SaaS positions` bölümüne bak: yenileme bildirim penceresi, kabul edilebilir fiyat artışı, veri ihracı, HSS eşikleri, alt işleyen onayı, özellik kaldırma bildirimi. Bu skill bunlar için varsayılan rakam taşımaz. Bölüm bir şart hakkında sessizse sor:

> Playbook'unuz [şart — ör. "kabul edilebilir en uzun yenileme bildirim süresi", "sağlayıcının anonimleştirilmiş türev veriyi saklaması"] hakkında bir şey söylemiyor. Pozisyonunuz ne? Eklenti ayarına ekleyeyim.

Cevabı kaydet ve devam et.

## Sözleşmenin niteliği ve standart koşullar

- **Nitelendirme.** SaaS sözleşmesi Türk hukukunda kanunda düzenlenmemiş (isimsiz/karma) bir sözleşme olarak görülür; hangi tipin (kira, lisans, eser, vekâlet) hükümlerinin kıyasen uygulanacağı **tartışmalı — doktrin ve içtihadı kontrol et**. Uygulanacak boşluk doldurucu kural sonucu değiştirir (ör. fesih); sözleşmede açık düzenleme ara.
- **Lisans.** Kurulumlu yazılımda bilgisayar programı eserdir (FSEK m. 2/1-1); kullanma yetkisi ruhsattır (FSEK m. 48/2); mali haklara dair sözleşme yazılı olmalı ve haklar ayrı ayrı gösterilmelidir (FSEK m. 52). Kullanma ruhsatını üçüncü kişiye (grup şirketleri dahil) devretmek eser sahibinin yazılı muvafakatini ister (FSEK m. 49/1) → grup şirketlerinin kullanımını açıkça yaz. Kopya teslim edilmeyen saf SaaS'ta FSEK lisans şeklinin aranıp aranmadığı **tartışmalı**.
- **Tıkla-kabul / matbu koşullar.** Sağlayıcının tek başına hazırlayıp sunduğu koşullar genel işlem koşuludur (TBK m. 20). Aleyhe koşul, açıkça bilgi verilip içeriği öğrenme imkânı sağlanmadıkça yazılmamış sayılır (m. 21/1); belirsiz koşul düzenleyen aleyhine yorumlanır (m. 23); düzenleyene tek yanlı değiştirme yetkisi veren kayıt yazılmamış sayılır (m. 24); dürüstlük kuralına aykırı aleyhe hüküm konulamaz (m. 25). Yanıltıcı biçimde kanundan önemli ölçüde ayrılan genel işlem şartı kullanmak haksız rekabettir (TTK m. 55/1-f). Alım tarafında güçlü kaldıraç; satış tarafında kendi koşullarınız için risk.
- **Tüketici.** Müşteri tüketiciyse (6502 m. 3/1-k): belirli süreli abonelikte "süre kadar uzar" kaydı konulamaz; uzatma ancak tüketicinin talebi ya da onayıyla olur (6502 m. 52/3); belirsiz süreli ya da bir yıldan uzun abonelik gerekçesiz ve cezai şartsız feshedilebilir (m. 52/4); haksız şartlar kesin hükümsüzdür (m. 5/2). Bu durumda playbook'un B2B pozisyonları uygulanmaz → avukata.

## SaaS katmanı

Her başlıkta sözleşmede bulduğunu yaz ve `SaaS positions` ile karşılaştır. Bu skill'den sabit eşik uygulama.

### 1. Otomatik yenileme

SaaS anlaşmasının en sık bozulduğu yer: kimse bildirim penceresini fark etmez, bir yıl daha ve daha yüksek fiyatla bağlanırsınız.
- **Yenileme süresi** (ilk süreyle aynı, daha uzun, çok yıllığa dönüşen)
- **Fesih bildirim penceresi** (yenilemeden kaç gün önce)
- **Bildirim yöntemi.** Tacirler arasında temerrüde düşürme, fesih ve sözleşmeden dönme ihbarları noter, taahhütlü mektup, telgraf ya da güvenli e-imzalı KEP ile yapılır (TTK m. 18/3). Sözleşmenin "e-posta ya da portal bildirimi yeterlidir" demesinin bu şekli karşılayıp karşılamadığı ve m. 18/3'ün geçerlilik mi ispat şartı mı olduğu **tartışmalı — içtihadı kontrol et**. Pratik: iptali her zaman TTK m. 18/3'teki yollardan biriyle gönder; sözleşmedeki KEP/tebligat adresini kaydet.
- **Yenilemede fiyat** (aynı, endeks tavanlı, o günkü liste fiyatı, sınırsız takdir)

Herhangi bir bayrak olsun olmasın **yenileme tarihini ve bildirim penceresini çıkar ve kaydet** → renewal-tracker.

### 2. Fiyat artışı

- **Yıllık artış** (sabit oran, TÜFE/ÜFE gibi endeks — hangi endeks ve hangi ay, tavan var mı, sınırsız)
- **Tek taraflı fiyat değişikliği.** Matbu koşullarda sağlayıcıya tek yanlı fiyat/koşul değiştirme yetkisi veren kayıt yazılmamış sayılır (TBK m. 24) — müzakere edilmiş sözleşmede bu koruma zayıflar; açık tavan ve fesih hakkı iste.
- **Döviz.** Bedel yabancı parayla belirlenmişse ve "aynen ödeme" kaydı yoksa borç ödeme günündeki rayiçle TL olarak da ödenebilir; temerrütte alacaklı aynen ya da vade/fiilî ödeme günü rayicinden TL ister (TBK m. 99/2-3). İki Türkiye yerleşiği arasında döviz cinsinden ya da dövize endeksli bedel için Türk Parası Kıymetini Koruma Hakkında 32 sayılı Karar ve tebliğlerindeki yasak ve istisnaları ayrıca çek (`tr_mevzuat_ara(query="Türk Parası Kıymetini Koruma Hakkında 32 Sayılı Karara İlişkin Tebliğ")`); madde atfını ancak çektiğin metinden yap.
- **Kullanım aşımı** (yayımlanmış tarife, yüksek oran, belirsiz) ve **"ücret"in kapsamı** (yalnız abonelik mi, geniş tanımlı "ek hizmetler" mi).
- **Fatura itirazı.** Faturayı alan sekiz gün içinde içeriğine itiraz etmezse kabul etmiş sayılır (TTK m. 21/2) → aşım faturaları için iç kontrol süreci gerektiğini iş birimine yaz.
- Sonradan beklenmedik olağanüstü durum: tek kanuni araç aşırı ifa güçlüğüdür (TBK m. 138; sürekli edimlide kural olarak fesih); sözleşmede ayrıca uyarlama/yeniden müzakere kaydı ara.

### 3. Veri taşınabilirliği ve çıkış

Bu sağlayıcıdan bir gün ayrılacağız; verimizi alabilecek miyiz?
- **İhraç biçimi** (açık/standart, belgelenmiş özel biçim, "ticari olarak makul")
- **Ne zaman** (her an self-servis, süre içinde talep üzerine, yalnız sona ermede)
- **Sona erme sonrası erişim** (kaç gün), **maliyet** (ücretsiz, iş-zaman, GB/kayıt başına)
- **Silme teyidi** (talep üzerine tutanak, yok, sağlayıcı türev veriyi saklıyor). Kişisel verinin silinmesi, yok edilmesi ya da anonim hâle getirilmesi veri sorumlusunun yükümlülüğüdür (KVKK m. 7) → silme süresi ve tutanak `/arthurlegal:privacy-legal-dpa-review` ile uyumlu olmalı.
- Sağlayıcının "anonimleştirilmiş" ya da "toplulaştırılmış" türev veri saklaması esaslı bir pozisyondur; KVKK'da anonim hâle getirme, başka verilerle eşleştirilerek dahi kimliği belirlenebilir kişiyle ilişkilendirilemeyecek hâle getirmedir (KVKK m. 3/1-b). Ekibin tutumunu playbook'tan teyit et; her iki yönde de işaretle.

### 4. Erişilebilirlik ve hizmet seviyesi (HSS)

Yalnız iş bu hizmetin ayakta olmasına gerçekten bağlıysa önemlidir; anket aracı için müzakere sermayesi harcama.
- **Erişilebilirlik taahhüdü** (yüzde ya da "ticari olarak makul çaba"), **ölçüm dönemi** (aylık, üç aylık, yıllık)
- **Telafi.** Hizmet kredisi nasıl hesaplanıyor, tavanı var mı, "tek çare" mi? Hizmet kredisinin cezai şart mı (TBK m. 179-182), bedel indirimi mi sayılacağı **tartışmalı**; nitelendirme tavana ve ek tazminata etki eder. "Tek ve münhasır çare" kaydı önceden sorumsuzluk anlaşmasıdır: ağır kusurdan sorumsuzluk kesin hükümsüzdür (TBK m. 115/1).
- **Planlı bakım istisnası** (tanımlı pencere, önceden bildirim, sınırsız)
- Tek çare kaydının sorumluluk tavanıyla etkileşimi (aşağıda).

### 5. Alt işleyenler

Veri koruma konusudur ama SaaS'a özgüdür, çünkü liste abonelik boyunca **değişir**.
- **Güncel liste** (yayımlanmış, talep üzerine, yok), **değişiklik bildirimi** (önceden süre, yok), **itiraz hakkı** (engelleme, bildirip feshetme, yalnız bildirim, yok)
- Yurt dışındaki alt işleyen ya da bulut → kişisel veri yurt dışı aktarımı (KVKK m. 9). Mekanizmayı bu skill değerlendirmez → `/arthurlegal:privacy-legal-dpa-review` (sektörel katman ve aktarım orada).

### 6. Hizmet değişiklikleri ve özellik kaldırma

- **Esaslı olumsuz değişiklik** (feshetme hakkı, yalnız bildirim, sınırsız) — matbu koşulda tek yanlı değiştirme yetkisi için TBK m. 24
- Dayandığınız özellikler için **kaldırma bildirim süresi**; **yerine gelen özellik** aynı paket mi, üst paket mi

## Yapay zekâ ve makine öğrenmesi hakları

SaaS müzakeresinin en hızlı değişen başlığı; tek satırlık "var mı" kontrolü yetmez. Yedi boyutun her birini profilin `## AI/ML training rights` bölümündeki pozisyonla eşleştir:

1. **Açık izin.** Müşteri verisi / içeriği / kullanım verisi YZ eğitimi, model geliştirme için kullanılabiliyor mu? Alım tarafında genelde HAYIR (müşteri sağlayıcının ürününü sübvanse eder, rekabete duyarlı bilgi sızabilir). Satış tarafında gelir, kötüye kullanımda itibar riski.
2. **Politika yoluyla örtülü izin.** Sözleşme sağlayıcının gizlilik politikasını ya da kullanım koşullarını "güncellendiği şekliyle" mi içeriyor? Tek yanlı güncelleme yoluyla eğitim hakkı eklenebiliyor mu? Matbu koşulda bu yetki yazılmamış sayılır (TBK m. 24), ama kayda güvenme; açık yasak iste. "Hizmet geliştirme", "analitik" gibi torba ifadelere ve log/telemetriyi müşteri verisi tanımından çıkaran "kullanım verisi" tanımlarına bak.
3. **Anonimleştirme standardı.** "Anonim" tanımsızsa zayıftır; KVKK m. 3/1-b ölçütüne bağla. AB bağlantısı varsa GDPR ölçütünü araçla çek (`eu_get_document_text(celex="32016R0679")`, gerekçe 26). Geri döndürülebilir mi?
4. **Rekabet açısından bulaşma.** Sağlayıcı rakiplerinize de hizmet veriyor mu? Verinizle eğitilen model rakibin çıktısına sızabilir; emanet iş ürününden yetkisiz yararlanma ve sır ifşası TTK m. 55/1-c,d tabanıdır ama sözleşmesel izolasyon taahhüdü iste.
5. **Vazgeçme (opt-out) kapsamı ve kalıcılığı.** Tüm YZ kullanımlarını mı kapsıyor, yenilemelerden ve koşul güncellemelerinden sonra sürüyor mu, kullanıcı mı kurum mu düzeyinde? Varsayılan açık mı kapalı mı — sözleşmede yazılı mı?
6. **Çıktı sahipliği.** Ürün YZ çıktısı üretiyorsa çıktı kimin, sağlayıcı çıktıyı eğitim örneği olarak kullanabilir mi? YZ çıktısının FSEK anlamında eser sayılıp sayılmadığı **tartışmalı**; hakları sözleşmeyle açıkça düzenle. Üçüncü taraf YZ alt işleyenleri (büyük dil modeli sağlayıcıları) alt işleyen listesinde görünür.
7. **Düzenleyici zincir.** Sağlayıcının veriyi YZ için kullanması sizin için düzenleyici risk doğuruyor mu? Türkiye'de amaç dışı işleme ve aktarım → `/arthurlegal:privacy-legal-use-case-triage`; AB bağlantısı varsa YZ Tüzüğü yükümlülükleri araçla çekilir (`eu_search_eu_law(query="Regulation (EU) 2024/1689 artificial intelligence")`); sektörel kurum kararları için `tr_kurum_karari_ara`.

Sözleşme yedisinde de sessizse bu da bulgudur: "Sözleşme YZ/ML eğitim hakları konusunda sessiz — açık yasak ya da yedi boyuta bağlı tanımlı istisna isteyin."

## Sorumluluk tavanı ve Türk hukuku sınırları

Tavan için vendor-agreement-review'daki dört boyutlu karar prosedürünü uygula (doğrudan/dolaylı zarar, tavan tabanının birebir alıntısı, tavan dışı kalemler, boyut başına playbook). SaaS'ta tavan dışı kalemler genelde veri ihlali, gizlilik ve fikrî hak tazminidir; bunlar tavan dışındaysa kalan "tavanlı alan"ın anlamlı mı göstermelik mi olduğunu yaz.

**Yargı çevresi farkı.** Playbook tek bir hukuk tercihini her yere uygular; geçerlilik ise hukuka göre değişir. Türk hukukunun tipik sınırları:

| Konu | Türk hukuku | Dayanak |
|---|---|---|
| Sorumsuzluk / tavan | Ağır kusurdan önceden sorumsuzluk kesin hükümsüz; izinle yürütülen uzmanlık hizmetinde hafif kusur için de | TBK m. 115/1, 115/3 |
| Yardımcı kişi (alt yüklenici, alt işleyen) | Sorumluluk önceden kaldırılabilir; izinle yürütülen uzmanlık hizmetinde kaldırılamaz | TBK m. 116/2-3 |
| Otomatik yenileme | B2B'de kanuni üst sınır yok, bildirim şekli TTK m. 18/3; tüketicide emredici kural | TTK m. 18/3; 6502 m. 52 |
| Cezai şart | Tacir borçlu aşırılık iddiasıyla indirim isteyemez | TTK m. 22 |
| Zamanaşımı | TBK'daki zamanaşımı süreleri sözleşmeyle değiştirilemez; "talepler 1 yıl içinde ileri sürülür" kaydının sözleşmesel hak düşürücü süre olarak geçerliliği **tartışmalı** | TBK m. 148 |
| Rekabet yasağı / ayartmama | Rakipler arasında 4054 m. 4 riski | 4054 m. 4 |

Playbook pozisyonu seçilen hukukta uygulanamıyorsa işaretle: "Playbook'unuz [X] istiyor, ama bu sözleşme [Y] hukukuna tabi ve orada [X] [geçersiz / sınırlı / emredici kurala tabi]." Yabancı hukuk için kural araçtan çekilir, ezberden değil → `/arthurlegal:commercial-legal-governing-law-review`.

## Redline inceliği

vendor-agreement-review'daki kural: en küçük düzeltme (kelime → ifade → alt bent → cümle → madde); tüm maddeyi değiştirdiysen ileti notunda söyle.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["20","21","23","24","25","99","115","116","138","148"])
tr_mevzuat_madde_getir(number="6102", madde_no=["18","21","22","55"])
tr_mevzuat_madde_getir(number="5846", madde_no=["2","48","49","52"])
tr_mevzuat_madde_getir(number="6502", madde_no=["3","5","52"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="18/3 fesih ihbarı noter aracılığıyla ispat şartı", date_from="2020-01-01")
tr_ictihat_semantik_ara(initial_keyword="genel işlem koşulu tek taraflı değişiklik", query="tacirler arası sözleşmede TBK 24 değiştirme yasağı uygulanır mı")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".

## Çıktı

vendor-agreement-review not yapısını kullan (üst başlık orada); standart playbook kontrollerinden sonra SaaS bölümü ekle.

**Çift ciddiyet** (eklenti ayarı `## Dual severity`): her SaaS bulgusunda iki eksen —
- **Hukuki risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
- **İş sürtünmesi:** 🔴 Anlaşmayı durdurur | 🟠 Yavaşlatır | 🟡 Kafa karıştırır | 🟢 Görünmez

Veri çıkışı, otomatik yenileme ve fiyat artışı bulguları çoğu zaman 🟢 hukuki / 🔴 iş sürtünmesidir: kloz geçerlidir ama müşterinin ayrılamamasının ya da finansın yenilemede şaşırmasının nedenidir. Bunları iş sürtünmesi ciddiyetiyle öne çıkar.

```markdown
### Sonuç
[İmzalanabilir / Önce X için mücadele / Vazgeç — tek cümle neden]
**Taraflar:** [tacir–tacir / tüketici var]   **Playbook:** [Satış / Alım tarafı]

### YZ ve makine öğrenmesi hakları
[Açık eğitim kaydı, torba "hizmet geliştirme", kullanım verisi tanımı, çıktı sahipliği, üçüncü taraf YZ alt işleyenleri, opt-out / opt-in. Sessizse: "YZ/ML eğitim hakları konusunda sessiz — açık yasak ya da tanımlı istisna isteyin."]

## SaaS'a özgü bulgular

### Otomatik yenileme
**Yenileme tarihi:** [tarih]
**Bildirim penceresi:** [tarih]'e kadar iptal ([N] gün önce) — yöntem: [sözleşmedeki] / TTK m. 18/3 uyumu: [evet / hayır / tartışmalı]
**Yenileme fiyatı:** [yazıldığı gibi]
**Playbook uyumu:** [pozisyon içinde / sapma / değinilmemiş]
**Yenileme takibine:** [evet — kayıt alanları aşağıda]

### Fiyat artışı
### Veri çıkışı
[iş biriminin okuması gereken bölüm]
### HSS
[bulgular ya da "Atlandı — [paydaş]'a göre hizmet iş açısından kritik değil"]
### Alt işleyenler
### Hizmet değişiklikleri
```

## Devirler

**renewal-tracker'a:** Yenileme tarihi ve bildirim penceresi bulununca devret. Kayıt şu alanları bekler (tam şema: `skills/renewal-tracker/references/renewal-register.yaml`; alan adları değişmez):

```yaml
counterparty:         [ad]
agreement:            [başlık]
signed_date:          [ISO tarih]
initial_term_end:     [ISO tarih]
renewal_mechanism:    [ör. "auto-renew annual"]
notice_period_days:   [tam sayı]
cancel_by_effective:  [ISO tarih — initial_term_end eksi notice_period_days]
price_on_renewal:     [yazıldığı gibi]
annual_value:         [tam sayı, belirtilmişse]
business_owner:       [e-posta, biliniyorsa]
clm_id:               [varsa]
status:               active
```

Belirlenemeyen alanı boş bırak ve hangilerinin eksik olduğunu yaz (`clm_id`, `annual_value`, `business_owner` çoğu zaman insandan gelir). Bildirim yönteminin TTK m. 18/3'e uyup uymadığını kayıt notuna ekle.

**escalation-flagger'a:** Bir SaaS kontrolü `## Escalation`'daki "asla kabul etme" ya da eskalasyon tetikleyicisine düşerse `/arthurlegal:commercial-legal-escalation-flagger` yönlendirir.

## Neyle kavga edilir

Büyük SaaS sağlayıcıları kâğıtlarını, havayolunun bilet koşullarını müzakere ettiği kadar müzakere eder. Savaşı playbook'a göre seç: `SaaS positions` her zaman itiraz edilen, yalnız büyük anlaşmada itiraz edilen ve bırakılan şartları ayırmalı; ayırmıyorsa sor. Sözleşme değeri ve geçiş maliyetine göre kalibre et: kolay ikamesi olan küçük bir araç, üzerine iş kurulacak büyük bir platformdan daha hafif ele alınır.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu incelemeye göre uyarla (redline'ı gönder, eskalasyon, ek olgu iste — ör. alt işleyen listesi, yenileme kaydını aç, bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

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
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/arthurlegal:legal-research-az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/arthurlegal:legal-research-sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
