---
name: privacy-legal-dsar-response
description: >
  İlgili kişi başvurusu (KVKK m. 11, m. 13) — talebi m. 11 haklarına ayırır,
  başvuru şeklini ve kimliği (Veri Sorumlusuna Başvuru Usul ve Esasları
  Hakkında Tebliğ) kontrol eder, 30 günlük cevap süresini izler, veriyi sistem
  sistem bulur, m. 28 istisnalarını ve silmenin sınırlarını (m. 7, kanuni
  saklama süreleri) değerlendirir; alındı ve esas cevap yazılarını taslak
  olarak çıkarır. "Başvuru geldi", "verilerimi istiyor", "verilerimin
  silinmesini istiyor", "KVKK başvurusu", "DSAR", "unutulma hakkı" denince ya
  da bir başvuru metni yapıştırıldığında kullan.
argument-hint: "[başvuruyu yapıştırın ya da anlatın]"
---

# /dsar-response — İlgili Kişi Başvurusu (KVKK)

İlgili kişi başvurusunun bir süresi (30 gün), bir usulü (kimlik → veri → istisna → cevap) ve ters gidebileceği çok yeri vardır. Bu skill her adımı yürütür ve cevabı **taslak** olarak hazırlar; göndermez. Esas cevabın gövdesi paketteki `kvkk-m11-cevap-sablonu.md`'dir. Kural ezberden söylenmez: atıf yapılan her madde `tr_mevzuat_madde_getir` ile çekilir.

**Başvuruyu yapıştırmadan önce:** başvuru ilgili kişinin kişisel verisini taşır. Gereksiz ekleri (kimlik fotokopisi, ilgisiz yazışma) çıkar ya da maskele (`pii-redaksiyon-rehberi.md`, `arthur-mask-rehberi.md`); dosya adlarına ilgili kişinin adını yazma.

## ⏰ ÖN-KONTROL — Süre (her çalıştırmada)

| Durum | Süre | Dayanak |
|---|---|---|
| Başvurunun sonuçlandırılması | Talebin niteliğine göre en kısa sürede, **en geç 30 gün**; kural olarak ücretsiz | 6698 m. 13/2; Tebliğ m. 6/5 |
| Sürenin başlangıcı | Yazılı başvuruda evrakın veri sorumlusuna/temsilcisine tebliğ tarihi; diğer yöntemlerde başvurunun ulaştığı tarih | Tebliğ m. 5/4-5 |
| Ret, yetersiz cevap ya da cevapsızlık → Kurula şikâyet | İlgili kişi cevabı öğrendiği tarihten **30 gün**, her hâlde başvuru tarihinden **60 gün** içinde; başvuru yolu tüketilmeden şikâyet olmaz | 6698 m. 14/1-2 |
| Kurul bilgi/belge isterse | **15 gün** içinde gönderme; gerekirse yerinde inceleme imkânı | 6698 m. 15/3 |
| Kurul ihlal kararı verirse | Tebliğden itibaren gecikmeksizin, en geç **30 gün** içinde yerine getirme | 6698 m. 15/5 |
| Ticari elektronik iletiyi reddetme | Talep ulaştıktan sonra **3 iş günü** içinde gönderimi durdurma | 6563 m. 8/3 |

- 30 günü takvim günü olarak say (ihtiyatlı yol). Son güne ≤ 5 gün → 🔴 ACİL.
- Kimlik teyidi ya da eksik bilgi yazışmasının 30 günü durdurup durdurmadığı Kanun'da ve Tebliğ'de düzenlenmemiştir — **tartışmalı, Kurul kararlarını kontrol et**. İhtiyatlı yol: süre başvuru tarihinden işler; teyit isteğini ilk günlerde gönder.
- Eklenti ayarındaki iç SLA daha kısaysa onu uygula, kanuni sınırı not et.

## Destination check

- **İlgili kişiye alındı yazısı ve esas cevap** → dış belge: `## Outputs` başlığı **konmaz**; iç değerlendirme, risk notu, istisna tartışması girmez.
- **İstisna analizi, sistem tarama tablosu, iç not** → profilin `## Outputs` bölümündeki role göre üst başlık (avukatta "GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ"; sır saklama: Av. K. m. 36); mektuplardan ayrı dosya.
- **Kurula şikâyet üzerine savunma** → bu skill'in kapsamı dışında; burada yalnız olgu ve belge dökümü hazırlanır.

## ADIM 0 — Rol ve kapsam

- [Müvekkil] bu veri için **veri sorumlusu** mu, **veri işleyen** mi (6698 m. 3/1-ğ, ı)? Başvuru veri sorumlusuna yapılır (m. 13/1). [Müvekkil] veri işleyense talebi kendisi cevaplamaz; veri işleme sözleşmesindeki usulle veri sorumlusuna iletir ve sözleşmedeki yardım yükümlülüğünü yerine getirir (sözleşme için `/arthurlegal:privacy-legal-dpa-review` çıktısına bak).
- Başvuran kendi verisini mi istiyor? m. 11 "kendisiyle ilgili" haklar tanır. Aile üyesi, vekil ya da işveren adına gelen talepte yetki belgesi ara; başkasının verisini verme.
- İlgili kişi ya da işleme AB/İngiltere'ye bağlıysa → aşağıda **Yabancı rejimler**.

## Bağlamı yükle

`firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DSAR process` (sistem listesi, kimlik teyidi yöntemi, iç SLA, rutin iş / eskalasyon ayrımı), `## Escalation`, `## Regulatory footprint` (yabancı rejim ve sektör satırları), `## Outputs`, `## Who's using this`. Sistem listesi boş ya da eskiyse bayrakla: nerede arayacağını bilmeden eksiksiz cevap verilemez.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:privacy-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Talebi sınıflandır (m. 11/1)

| Bent | Hak | Pratikte |
|---|---|---|
| a | Kişisel veri işlenip işlenmediğini öğrenme | "Hakkımda veri var mı?" |
| b | İşlenmişse buna ilişkin bilgi talep etme | Kategoriler, içerik, kopya talebi |
| c | İşlenme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme | |
| ç | Yurt içinde veya yurt dışında aktarıldığı üçüncü kişileri bilme | Alıcı listesi |
| d | Eksik veya yanlış işlenmişse düzeltilmesini isteme | |
| e | m. 7 şartları çerçevesinde silinmesini veya yok edilmesini isteme | Hesap kapatma, "unutulma" |
| f | (d) ve (e) işlemlerinin aktarıldığı üçüncü kişilere bildirilmesini isteme | Veri işleyenler, alıcılar |
| g | Münhasıran otomatik sistemlerle analiz sonucu aleyhe sonuca itiraz | Otomatik skor/kredi kararı |
| ğ | Kanuna aykırı işleme nedeniyle zararın giderilmesini talep etme | → eskalasyon |

- KVKK'da GDPR'daki **veri taşınabilirliği** ve **işlemenin kısıtlanması** ayrı haklar olarak sayılmamıştır; böyle bir talebi m. 11/1-b ve e çerçevesinde değerlendir, rejim farkını iç notta yaz. GDPR uygulanıyorsa aşağıya bak.
- Pazarlama iletisinden çıkma talebi KVKK başvurusu kılığında gelebilir; ticari elektronik iletide ret hakkı ayrıca 6563 m. 8'dedir (3 iş günü).
- Birleşik talep ("önce verilerimi gönderin, sonra silin") iki bağlı talep olarak yürür: önce bilgi/kopya, sonra silme.

### 2. Başvurunun şekli ve kimlik

- **Şekil:** yazılı ya da Kurul'un belirlediği yöntemler (m. 13/1). Tebliğ m. 5/1: yazılı; KEP; güvenli elektronik imza; mobil imza; ilgili kişinin daha önce bildirdiği ve sistemde kayıtlı e-posta; başvuru amaçlı yazılım/uygulama.
- **Zorunlu unsurlar (Tebliğ m. 5/2):** ad-soyad (yazılıysa imza); T.C. kimlik no, yabancılar için uyruk + pasaport ya da kimlik no; tebligata esas adres; varsa e-posta/telefon/faks; talep konusu. Eksikse hemen tamamlatma iste; eksikliğin süreye etkisi **tartışmalı**.
- **Dil:** Tebliğ m. 4/2 başvurunun Türkçe yapılmasını arar. Yabancı dildeki başvuruyu yalnız bu gerekçeyle reddetmenin Kurul önündeki sonucu **tartışmalı** — ihtiyatlı yol: cevapla ya da Türkçe başvuru iste, gerekçeyi kayda geçir.
- **Teyidi riske göre ayarla:** oturum açmış kullanıcı ya da kayıtlı e-postadan gelen bilgi talebi → çoğunlukla yeterli; silme, özel nitelikli veri ya da yüksek değerli hesap → ek teyit. Teyit için gerekenden fazla belge toplamak ölçülülük ilkesiyle (m. 4/2-ç) çatışabilir. Aşırı teyit başvuruyu engele çevirir; eksik teyit veriyi dolandırıcıya verir.
- Vekil → vekâletnamenin kapsamı; kanuni temsilci → temsil belgesi.

Teyit edilemezse (ilk günlerde gönder, 29. günde değil):

```
Başvurunuzun, kişisel verileri konu olan kişiden geldiğini teyit edemedik.
İşleme devam edebilmemiz için lütfen [teyit adımı]. Kimliği teyit edilemeyen
başvurular üzerine kişisel veri paylaşamıyoruz.
```

### 3. Veriyi bul

Eklenti ayarındaki sistem listesini tara; VERBİS kaydındaki veri kategorileri ve alıcı gruplarıyla (m. 16/3-c, ç, d) karşılaştır. Kayıtta olmayan bir işleme çıkarsa değişiklik derhâl bildirilir (m. 16/4); Veri Sorumluları Sicili Hakkında Yönetmelik m. 13/1: değişikliğin meydana geldiği tarihten itibaren 7 gün içinde VERBİS üzerinden → iç notta bayrakla.

| Sistem | Sorgulandı mı? | Veri var mı? | Ne |
|---|---|---|---|
| Ana veritabanı / ERP | | | |
| CRM | | | |
| Destek kayıtları / çağrı merkezi | | | |
| E-posta / SMS pazarlama | | | |
| Analitik | | | |
| Loglar | | | |
| Yedekler | | | (silmede rotasyon tarihi ayrıca yazılır) |
| Veri işleyenler (bulut, bordro, muhasebe) | | | (silme/düzeltmede bildirim — m. 11/1-f) |
| Fiziki arşiv (veri kayıt sisteminin parçasıysa) | | | m. 3/1-e, h |

### 4. İstisna ve sınır analizi

İyi niyetli dayanağı olan her istisnayı **öner**, belirsizleri işaretle; listeyi avukat daraltır. Açıklanan veri geri alınamaz; fazla önerilen istisna incelemede düzeltilir. Her önerinin yanına yaz: **"önerilen — ileri sürmeden önce avukat incelemesi gerekir; Kurul toptan istisna iddiasını sıkı inceler."**

| Dayanak | Kapsam | Etkisi |
|---|---|---|
| m. 28/1-a–d | Kanun hiç uygulanmaz: ev içi faaliyet; anonimleştirilerek resmî istatistik/araştırma; sanat, tarih, edebiyat, bilim ve ifade özgürlüğü (sınırlarıyla); kanunla yetkili kamu kurumlarının önleyici/istihbari faaliyetleri; yargı ve infaz makamlarının işlemleri | Özel şirkette nadir; yayın faaliyetinde (c) bendini değerlendir |
| m. 28/2-a | Suç işlenmesinin önlenmesi veya suç soruşturması için gerekli işleme | m. 10, m. 11 (zararın giderilmesi hariç) ve m. 16 uygulanmaz — **Kanun'un amacına ve temel ilkelerine uygun ve orantılı olmak kaydıyla** |
| m. 28/2-b | İlgili kişinin kendisinin alenileştirdiği veri | aynı |
| m. 28/2-c | Kamu kurumları ve kamu kurumu niteliğindeki meslek kuruluşlarının denetleme/düzenleme görevi, disiplin soruşturma veya kovuşturması | aynı |
| m. 28/2-ç | Bütçe, vergi ve mali konularda Devletin ekonomik ve mali çıkarlarının korunması | aynı |

**Silme talebinin sınırları:**
- Silme, işlenmesini gerektiren sebepler ortadan kalkınca doğar; diğer kanunlardaki hükümler saklıdır (m. 7/1-2). Usul: Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi Hakkında Yönetmelik (madde atfı yapacaksan maddeyi çek).
- Kanuni saklama örnekleri: VUK m. 253 (defter ve belgeler, ilgili yılı izleyen takvim yılından başlayarak 5 yıl); TTK m. 82/5 (m. 82/1-a–d'deki defter ve belgeler 10 yıl; başlangıç m. 82/6). Saklanan her kategori için dayanağı cevapta yaz.
- Uyuşmazlık: bir hakkın tesisi, kullanılması veya korunması için zorunlu işleme (m. 5/2-e; özel nitelikli veride m. 6/3-d). Bekleyen ya da muhtemel davada silme talebi + delil koruma çatışması → avukat karar verir.
- Gerekçesiz silmeme ceza riskidir: m. 7'ye aykırı olarak silmeyen veya anonim hâle getirmeyen TCK m. 138'e göre cezalandırılır (6698 m. 17/2).

**Diğer sorular:**
- Kayıtta başkasının verisi var mı (destek yazışmasındaki diğer kişiler, CC listeleri)? → karart.
- Ticari sır, iç değerlendirme notu, avukat yazışması: m. 28'de açık bir ticari sır ya da meslek sırrı istisnası yoktur — **tartışmalı; Kurul kararlarını ara**. Avukatın kendi sır saklama yükümlülüğü Av. K. m. 36'dadır.
- Yedekler: teknik imkânsızlık genel bahane değildir; rotasyon tarihiyle belgelenir.

**Paket şablonu:** `kvkk-m11-cevap-sablonu.md` m. 28/1 – m. 28/2 ayrımına ve m. 14/1 şikâyet sürelerine (öğrenmeden 30 gün, her hâlde başvurudan 60 gün) göre günceldir; ret paragrafında bendi somut gerekçeyle yaz.

### 5. Cevap — iki yazı

KVKK ayrı bir alındı yazısı istemez; ama erken alındı yazısı mükerrer başvuruyu ve erken şikâyeti azaltır (iyi uygulama). İkisini birleştirip 30. günde tek yazı gönderme.

**5a — Alındı yazısı** (aynı gün – 3 iş günü):

```
Konu: [GG.AA.YYYY] tarihli kişisel veri başvurunuz

Sayın [Ad Soyad],

[Başvuru tarihi] tarihinde ulaşan başvurunuzu aldık.

Başvurunuzu şöyle anlıyoruz: [tek cümle — ör. "hesabınızla ilişkili kişisel
verilerin ve aktarıldığı üçüncü kişilerin bildirilmesi, ardından hesabınızın
silinmesi"].

Başvurunuzu 6698 sayılı Kanun'un 13. maddesi uyarınca en geç [başvuru tarihi
+ 30 gün] tarihine kadar sonuçlandıracağız. [Teyit eksikse: İşleme devam
edebilmemiz için [teyit adımı] gerekmektedir; bu arada çalışmaya devam ediyoruz.]

Başvurunuz ücretsizdir. [İşlem ayrıca maliyet gerektirirse: Kurulca belirlenen
tarifedeki ücret söz konusu olabilir; bu durumda önceden bilgi vereceğiz.]

İletişim: [veri sorumlusu irtibat bilgisi]
```

**5b — Esas cevap:** gövde `kvkk-m11-cevap-sablonu.md`. Zorunlu unsurlar (Tebliğ m. 6/4): veri sorumlusu/temsilci bilgisi; başvuru sahibinin kimlik ve iletişim bilgileri; talep konusu; veri sorumlusunun açıklamaları. Talep kabul edilir ya da **gerekçesi açıklanarak** reddedilir; cevap yazılı veya elektronik ortamda bildirilir (m. 13/3). Kabulde gereği en kısa sürede yerine getirilir ve ilgili kişiye bilgi verilir (Tebliğ m. 6/6). Ücret: yazılı cevapta 10 sayfaya kadar ücret yok; aşan sayfa ve kayıt ortamı için Tebliğ m. 7 (sayfa başı tutar Tebliğ metninde — güncelliğini teyit et); başvuru veri sorumlusunun hatasından kaynaklanıyorsa ücret iade edilir (m. 13/3).

Silme cevabına ek tablolar:

```
Silinen / yok edilen / anonim hâle getirilen:
| Kategori | Sistem | Yöntem | Tarih |

Saklanan ve nedeni:
| Kategori | Dayanak (kanun + madde) | Saklama sonu |

Bildirim yapılan üçüncü kişiler (m. 11/1-f): [liste]
```

Her iki yazı da **TASLAK**: gönderilen cevap veri sorumlusunu bir pozisyona bağlar, istisnadan fiilen vazgeçme sonucu doğurabilir ve m. 14 şikâyet süresini başlatır. Avukat onayı olmadan gönderilmez.

### 6. Kayıt

Başvuru tarihi ve kanalı; kimlik teyit tarihi; alındı ve cevap tarihleri; verilen / silinen / saklanan; ileri sürülen istisna ve dayanağı; işi yürüten. Takip aracı yoksa matter klasöründe log dosyası (ilgili kişinin adı dosya adında olmaz).

## Eskalasyon tetikleyicileri

Profilin `## Escalation` bölümüne göre, en az şu hâllerde:
- Başvuran ya da vekili karşı taraf, muhtemel davacı, gazeteci ya da çalışan/eski çalışan uyuşmazlığının tarafı
- Olağandışı kapsam ("hakkımdaki tüm iç yazışmalar")
- Zararın giderilmesi talebi (m. 11/1-ğ) ya da tazminat imâsı
- Bekleyen dava veya delil koruma ihtiyacı varken silme talebi
- Önceki cevaba itiraz; Kurul'a şikâyet ya da Kurul yazısı
- Özel nitelikli veri (m. 6/1), çocuk verisi, toplu/kampanya başvurusu

## Yabancı rejimler

- **AB (GDPR):** `eu_get_document_text(celex="32016R0679")` ile süre ve uzatma (Art. 12), haklar (Art. 15–22) ve sınırlamalar (Art. 23) metnini çek; ezberden yazma. KVKK ile birlikte uygulanıyorsa her hak ve süre için iki rejimi yan yana koy, farkı iç notta yaz.
- **İngiltere:** `uk_search_legislation(query="Data Protection Act 2018")`, ardından `uk_get_section`.
- **Almanya ek kuralları:** `de_gesetz_ara(sorgu="Bundesdatenschutzgesetz")`.
- Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."
- *Karşılaştırmalı not:* ABD eyalet gizlilik yasalarının kendi cevap süreleri ve uzatma mekanizmaları vardır; yalnız CourtListener bağlayıcısı kuruluysa `courtlistener-rehberi.md` üzerinden araştırılır, ezberden yazılmaz.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6698", madde_no=["3","7","11","13","14","15","28"])
tr_mevzuat_ara(query="Veri Sorumlusuna Başvuru Usul ve Esasları", types=["TEBLIGLER"])  → tr_mevzuat_getir(mevzuat_id=...)
tr_mevzuat_ara(query="Kişisel Verilerin Silinmesi, Yok Edilmesi", types=["KKY"])
tr_mevzuat_madde_getir(number="213", madde_no=["253"])
tr_mevzuat_madde_getir(number="6102", madde_no=["82"])
tr_semantik_ara(kurum="kvkk", query="ilgili kişinin başvurusuna süresinde cevap verilmemesi")
tr_semantik_ara(kurum="kvkk", query="silme talebi kanuni saklama yükümlülüğü")
tr_kurum_karari_ara(kurum="kvkk", query="başvuru")   ← yalnız son ~30 özeti tarar; arşiv için tr_semantik_ara
tr_kurum_karari_getir(kurum="kvkk", id=<sonuçtaki id>)
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Araç veri getiremezse: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" (Kurul kararında https://www.kvkk.gov.tr/). Atıf etiketi: `[ArthurLegal TR — 6698 m. X — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`.

## Çıktı (iç not — mektuplardan ayrı)

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# İlgili Kişi Başvurusu — [Başvuru no / takma ad] — [Tarih]

## ⚠️ İnceleyen notu
- **Talep:** [m. 11/1 bentleri]
- **Süre:** başvuru GG.AA.YYYY → son gün GG.AA.YYYY 🔴/🟠/🟡
- **Kimlik:** [teyit edildi / bekliyor — adım]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) — [madde sayısı, Kurul kararı sayısı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]
- **Eskalasyon:** [yok / [isim] — neden]

## Sistem taraması
[tablo]

## Önerilen istisnalar ve saklama gerekçeleri
[her biri: dayanak (madde/fıkra/bent), olgu, "önerilen — avukat incelemesi"]

## Yazılar
[5a ve 5b taslaklarının dosya yolları]

## Açık işler
- [ ] ...
```

## Sonuç doğuran işlem kapısı (cevabın gönderilmesi)

Herhangi bir yazıyı ilgili kişiye gönderme aşamasına geçmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> İlgili kişi başvurusuna verilen cevabın hukuki sonucu vardır: içerik, ileri sürülen istisnalar ve eksik bırakılanlar Kurul incelemesine açıktır; yanlış beyan idari yaptırım riskine dönüşür. Bu cevabı bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: ilgili kişi (takma adla), talep edilen haklar, uygulanacak rejim(ler), sistem taramasının sonucu, verilmeyen kısım ve dayandığı istisna, kimlik teyidi durumu, son gün; avukata sorulacak üç soru (istisnalar sağlam mı, silme mi saklama mı, cevap şikâyete hazır mı). Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan gönderime hazır metin üretme; "TASLAK" işaretli çıktı serbest.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu başvuruya göre uyarla (cevabı tamamla, kimlik teyidi iste, eskalasyon, veri işleyene bildirim, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Sistemleri kendisi sorgulamaz; kontrol listesini yürütür, sorguyu insan ya da bağlı araç yapar.
- Sınırdaki istisnada karar vermez; avukata işaretler.
- Cevabı göndermez: taslak → inceleme → gönderimi insan yapar.
