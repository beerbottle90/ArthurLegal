---
name: privacy-legal-pia-generation
description: >
  Yeni bir özellik, ürün ya da veri işleme faaliyeti için ev formatında kişisel
  veri etki değerlendirmesi (PIA) yazar. KVKK'da genel bir etki değerlendirmesi
  yükümlülüğü yoktur; değerlendirme m. 4 ilkeleri, m. 5–6 işleme şartları,
  m. 10 aydınlatma, m. 12 veri güvenliği ve m. 9 aktarım ekseninde iyi uygulama
  olarak kurulur; AB'ye dönük işlemede GDPR Art. 35 araçla çekilir. "PIA yaz",
  "etki değerlendirmesi", "bu özellik için PIA gerekir mi", "gizlilik
  incelemesi" denince ya da yeni bir veri işleme faaliyeti anlatıldığında
  kullan.
argument-hint: "[özellik adı ya da açıklaması; varsa ürün gereksinim belgesi]"
---

# /pia-generation — Kişisel Veri Etki Değerlendirmesi (PIA)

PIA, ürün ekibiyle yapılan bir konuşmanın kaydıdır: hangi veri, neden, ne kadar süre, kim görüyor, ne ters gidebilir. Bu skill konuşmayı yapılandırır ve sonucu ekibin formatında (kurulumda örnek PIA'dan öğrenilen) yazar. Kural ezberden söylenmez; her madde araçtan çekilir.

## Hukuki çerçeve (önce bunu bil)

- **KVKK:** 6698'de GDPR Art. 35 benzeri genel bir etki değerlendirmesi yükümlülüğü yoktur; Kanun metninde "etki değerlendirmesi" ifadesi geçmez (`tr_mevzuat_icinde_ara(number="6698", query="etki değerlendirmesi")` — yeni değişiklik ihtimaline karşı yeniden tara). PIA burada **iyi uygulama ve ispat aracıdır**: m. 4 ilkelerine uyumu ve m. 12/1'deki "uygun güvenlik düzeyi"ne yönelik tedbirleri belgelemenin düzenli yolu. PIA'yı "kanunen zorunlu" diye sunma.
- **Kurul:** karar özetleri `tr_semantik_ara(kurum="kvkk", …)` ile aranır (`tr_kurum_karari_ara(kurum="kvkk")` yalnız son sayfaları tarar). Kurum'un yayımladığı rehberler ArthurLegal araçlarında yoktur; bir rehbere dayanacaksan kullanıcıdan teyit iste ve "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.kvkk.gov.tr/" yaz.
- **AB'ye dönük işleme:** GDPR'ın uygulanıp uygulanmadığını Art. 3'ü çekerek belirle. Uygulanıyorsa veri koruma etki değerlendirmesi (VKED/DPIA) zorunlu olabilir; metni ezberden yazma: `eu_get_document_text(celex="32016R0679", offset=224000)` ile Art. 35–36'yı çek. Çekilen metne göre Art. 35(3) özellikle üç hâli sayar (otomatik işlemeye dayalı, hukuki ya da benzeri önemli etki doğuran sistematik ve kapsamlı değerlendirme; özel kategori ya da mahkûmiyet verisinin büyük ölçekte işlenmesi; kamuya açık alanın büyük ölçekte sistematik izlenmesi); Art. 35(4) denetim makamlarının listelerini, Art. 35(7) asgari içeriği, Art. 36 yüksek kalıntı riskte önceden danışmayı düzenler `[ArthurLegal EU — CELEX 32016R0679 — 26.10.2026]`. Üye devlet listeleri ve uygulaması için ilgili ülke aracı (`de_gesetz_ara`, `nl_search_legislation`, `at_search_legislation`, `ie_search_acts` …); İngiltere `uk_search_legislation`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

## Destination check

Çıktı nereye gidiyor? Kullanıcı bir hedef söylediyse (kanal, dağıtım listesi, karşı taraf, "herkes") sır çevresinin içinde mi diye sor. Şirket geneli liste, karşı taraf, tedarikçi ve müvekkile giden iç çalışma ürünü korumayı zayıflatır. Hedef dışarıdaysa üç seçenek sun: (a) yalnız hukuk için başlıklı tam sürüm, (b) geniş dağıtım için arındırılmış sürüm, (c) ikisi. Başlık koyup metnin başlığın korumadığı yere yapıştırılmasına sessizce yardım etme.

## Bağlamı yükle

- `firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## PIA house style` (PIA'yı ne tetikler, örnek PIA'dan çıkarılan yapı, derinlik, kim onaylar), `## Regulatory footprint`, `## Privacy policy commitments`, `## Escalation`, `## Outputs`, `## Who's using this`. Örnek PIA yapısı varsa **onu kullan**: bu PIA ekibin diğer PIA'larına benzemeli.
- **Önceki çıktılar** (`## Outputs` klasörü): aynı faaliyet için `use-case-triage` (risk derecesi ve koşulları PIA'nın giriş noktasıdır), önceki `pia-generation` (yenisi neyin değiştiğini, neyin taşındığını söyler), kapsamdaki tedarikçiler için `dpa-review`. Bulunursa an: "Önceki triage ([tarih]) [risk] dedi ve [koşullar] istedi; bu PIA [hangisi karşılandı, hangisi kaldı]." / "Bu PIA [tarih] PIA'sının yerine geçer, çünkü [kapsam, yeni veri kategorisi, tedarikçi, mevzuat değişikliği]." **Ciddiyet tabanı:** triage yüksek risk dediyse PIA neyin değiştiğini söylemeden düşük risk sonucuna varamaz. Bulunamazsa yaz: "Bu faaliyet için önceki triage veya PIA yok; soğuk başlangıç."

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:privacy-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adım 0 — PIA gerekli mi?

1. **Ev tetiği** (`## PIA house style`) — ekibin cevabı.
2. **Zorunlu rejim:** KVKK tek başına zorunluluk doğurmaz. `## Regulatory footprint`'te GDPR/UK GDPR varsa Art. 35'i araçla kontrol et (yukarıda). Sektör mevzuatında risk değerlendirmesi hükmü olabilir (ör. bankacılık, sağlık, elektronik haberleşme) → `tr_mevzuat_icinde_ara(mevzuat_id=..., query="risk değerlendirmesi")`.
3. **Güçlü göstergeler** (zorunlu olmasa da yap): yeni teknoloji ya da yapay zekâ; çocuk verisi; özel nitelikli veri (m. 6/1 — biyometrik ve genetik dahil); ayrı toplanmış veri setlerinin birleştirilmesi; ayrımcılığa elverişli veri ya da çıkarım; münhasıran otomatik sistemlerle analiz edilip kişi aleyhine sonuç doğurabilecek işleme (m. 11/1-g itiraz hakkı); çalışan izleme; yurt dışı aktarım (m. 9); ilgili kişinin beklemeyeceği işleme.

Araştırma az sonuç verirse sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Ne zorunlu tetik ne ev tetiği varsa: "Bu faaliyet PIA gerektirmiyor görünüyor; soran olursa diye dosya için tek paragraflık gerekçe notu:" ve notu yaz.

## Mülakat (ürün ekibiyle)

Yazmadan önce cevapları al. Sohbet havasında olabilir; ekibe form gönderme. Ürün gereksinim belgesi varsa önce oradan çek.

### Ne ve neden
- Özellik/ürün/değişiklik ne? Kullanıcı için hangi sorunu çözüyor?
- Hangi kişisel veri? Alan alan say — "kullanıcı verisi" cevap değildir.
- Yeni toplama mı, eldeki verinin yeni amaçla kullanımı mı (m. 4/2-c, ç)?
- İşleme türü: saklama, analiz, paylaşma, otomatik karar?

### Hukuki sebep (m. 5–6)
- Her amaç için ayrı ayrı: m. 5/2-a–f şartlarından hangisi? Hiçbiri yoksa açık rıza (m. 5/1) — tanımı: belirli bir konuya ilişkin, bilgilendirilmeye dayanan ve özgür iradeyle açıklanan rıza (m. 3/1-a).
- **Sözleşme** (m. 5/2-c): sözleşmenin kurulması ya da ifasıyla **doğrudan** ilgili ve sözleşmenin taraflarına ait veri.
- **Meşru menfaat** (m. 5/2-f): işleme veri sorumlusunun meşru menfaati için **zorunlu** olmalı ve ilgili kişinin temel hak ve özgürlüklerine zarar vermemeli → denge testini yazılı yap (menfaat, zorunluluk, kişiye etkisi, makul beklenti, tedbirler).
- **Özel nitelikli veri** (m. 6/3, 7499 s.K. ile değişik): işleme yasaktır, ancak (a) açık rıza, (b) kanunlarda açıkça öngörülme, (c) fiili imkânsızlıkta hayat/beden bütünlüğü, (ç) ilgili kişinin alenileştirdiği ve alenileştirme iradesine uygun veri, (d) bir hakkın tesisi, kullanılması veya korunması, (e) sır saklama yükümlüsü kişi ya da yetkili kurumca sağlık hizmetleri, (f) istihdam, iş sağlığı ve güvenliği, sosyal güvenlik, sosyal hizmetler ve sosyal yardım alanlarındaki hukuki yükümlülük, (g) siyasi/felsefi/dini/sendikal amaçlı kâr amacı gütmeyen kuruluşlarda mevcut/eski üyeler hâllerinde mümkündür; her durumda Kurul'un belirlediği **yeterli önlemler** şarttır (m. 6/4) → `tr_semantik_ara(kurum="kvkk", query="özel nitelikli kişisel veri yeterli önlemler")`; düzenleyici kararın metni bulunamazsa UYARI satırı.
- Açık rızanın bir hizmetin ön şartı yapılması ve başka bir hukuki sebep varken ayrıca açık rıza alınması Kurul uygulamasında sorunlu görülür — **Kurul kararlarını ara** (`tr_semantik_ara(kurum="kvkk", query="açık rızanın hizmet şartına bağlanması")`).
- Ticari elektronik ileti varsa önceden onay şartı (6563 m. 6/1) ve ret hakkı (6563 m. 8) KVKK'dan ayrıca uygulanır.
- GDPR uygulanıyorsa hukuki sebepler için Art. 6 ve 9'u araçla çek; ezberden eşleme yapma.

### Kim ve nerede
- Şirket içinde kim görüyor (mühendis, destek, analist)? Erişim kontrolü ve kayıt (log) var mı?
- Üçüncü kişi ya da veri işleyen var mı (tedarikçi, iş ortağı, analitik)? → aktarım şartı (m. 8) ve sözleşme (`/arthurlegal:privacy-legal-dpa-review`).
- Nerede saklanıyor; sunucu yurt dışında mı? → m. 9 yolu ve standart sözleşme bildirimi.
- Ne kadar süre? Saklama süresi gerekli süreyle sınırlı mı (m. 4/2-d); silme/anonimleştirme mekanizması var mı (m. 7)?

### Ne ters gidebilir
- Veri sızarsa kişiye zararı ne?
- Kazara da olsa ayrımcılığa yol açabilir mi?
- Kullanıcı bunun olduğunu öğrense şaşırır mı? ("Tüyler ürpertici" testi — hukuki ölçüt değil, faydalı.)
- Vazgeçme/itiraz imkânı var mı, olmalı mı?

## PIA'yı yaz

Profildeki örnek PIA yapısını kullan; yoksa aşağıdaki varsayılan. Başa profilin `## Outputs` bölümündeki role göre üst başlığı koy.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Kişisel Veri Etki Değerlendirmesi (PIA): [Özellik/Ürün]

**Hazırlayan:** [ad] | **Tarih:** [GG.AA.YYYY] | **Durum:** TASLAK / ONAYLANDI
**Ürün sahibi:** [ad] | **Gizlilik incelemesi:** [ad]

## ⚠️ İnceleyen notu
- **Önceki çıktılar:** [triage/PIA/DPA — tarih ve sonuç / soğuk başlangıç]
- **Rejimler:** KVKK [+ GDPR Art. 35 — zorunlu / değil] [+ sektör]
- **Kaynaklar:** ArthurLegal MCP — [madde, Kurul kararı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]

## Yönetici özeti
[İki cümle: ne olduğu, uygun olup olmadığı.]
**Genel risk:** [İnceleyen belirler: 🟢 Düşük / 🟡 Orta / 🟠 Yüksek / 🔴 Çok yüksek]

## 1. İşlemenin tanımı
**Ne:** [düz dille] · **Veri kategorileri:** [alanlar] · **İlgili kişiler:** [müşteri / son kullanıcı / çalışan …] · **Amaç:** [kullanıcıya faydasıyla] · **Yeni toplama mı?** [evet — alanlar / hayır]

## 2. Hukuki sebep
| Amaç | Şart (m. 5/2 bendi, m. 6/3 bendi ya da açık rıza) | Not (denge testi özeti / rızanın nasıl alındığı) |

## 3. Veri akışı
**Toplama · Saklama (sistem, konum, şifreleme) · Erişim · Paylaşım (alıcı, amaç, hangi sözleşme) · Yurt dışı aktarım (m. 9 yolu, bildirim tarihi) · Saklama süresi ve imha**

## 4. Genel ilkeler (m. 4/2)
| İlke | Karşılanıyor mu? | Not |
| Hukuka ve dürüstlük kurallarına uygunluk | | |
| Doğru ve gerektiğinde güncel | | |
| Belirli, açık ve meşru amaç | | |
| Amaçla bağlantılı, sınırlı ve ölçülü | | |
| Gerekli süre kadar muhafaza | | |

## 5. Aydınlatma ve politika tutarlılığı
| Taahhüt (aydınlatma metni / politika) | Tutarlı mı? | Not |
[m. 10/1 kalemleri: kimlik, amaç, alıcılar ve amaçları, yöntem ve hukuki sebep, m. 11 hakları]
[🟡 varsa: lansmandan önce metin güncellenir ya da işleme değişir]

## 6. Riskler ve tedbirler
| # | Risk (tasarıma bağlı, somut) | Olasılık | Etki | Tedbir | Durum (Tamam / Planlı / Açık) | Sahibi |
**Tedbirlerden sonra kalan risk:** [değerlendirme]

## 7. İlgili kişi hakları (m. 11)
| Hak | Kullanılabilir mi? | Nasıl |
| Bilgi ve erişim (a–ç) | | |
| Düzeltme (d) | | |
| Silme / yok etme (e) ve üçüncü kişilere bildirim (f) | | |
| Otomatik analiz sonucuna itiraz (g) | | |

## 8. Kayıt ve bildirimler
VERBİS güncellemesi gerekir mi (m. 16/3-4)? Standart sözleşme bildirimi (m. 9/5)? Aydınlatma metni güncellemesi?

## 9. Öneri
[ONAY / KOŞULLU ONAY / DEĞİŞİKLİK GEREKLİ / ONAY YOK]
**Koşullar:** - [ ] [lansmandan önce yapılacak somut iş — sahibi — tarih]
**Onay:** [ad, tarih]
```

## Risk kalitesi

Risk **somut ve tasarıma bağlı** olmalı; genel risk belgeyi şişirir ve okuru göz gezdirmeye alıştırır.

| Kötü | Neden kötü | Daha iyi |
|---|---|---|
| "Veri ihlali" | Her şeye uyar, bir şey söylemez | "Destek ekibi konum geçmişine yönetim panelinden erişim kaydı tutulmadan ulaşabiliyor; kötü niyetli bir çalışan kullanıcıyı fark edilmeden izleyebilir" |
| "KVKK'ya aykırılık" | Döngüsel — PIA uyumu değerlendirmek için var | Maddeyi ve açığı adlandır (ör. "m. 10 aydınlatmasında bu amaç yok") |
| "Kullanıcılar beğenmeyebilir" | Belirsiz | "Pazarlama iletisini reddetmiş kullanıcılar bu akışta da ileti alabilir; ret işareti bu akışta kontrol edilmiyor (6563 m. 8)" |

2–5 gerçek risk; 15 dolgu risk değil.

## Aydınlatma metni / politika farkı

Her PIA profildeki `## Privacy policy commitments` ile karşılaştırılır. Sık kayma:
- Metin "X, Y, Z'yi topluyoruz" diyor; yeni özellik W'yi topluyor → metin güncellenir ya da W toplanmaz.
- Metin "yurt dışına aktarmıyoruz" diyor; yeni özellik yurt dışı bulut kullanıyor → m. 9 yolu + metin güncellemesi.
- Metin saklamayı "üyelik süresince" diyor; yeni özellik hesap silindikten sonra da saklıyor.

Her uyumsuzluğu bayrakla; biri lansmandan önce değişmeli.

## Devir

- **Ürün ekibine:** sahibi ve tarihi olan koşul listesi. "Güvenliği artırın" değil: "yönetim panelindeki konum sorgusuna erişim kaydı ekleyin — sahibi: [mühendislik lideri] — lansmandan önce."
- **`/arthurlegal:privacy-legal-reg-gap-analysis`:** PIA bir politika uyumsuzluğu bulduysa güncellemeyi o izler.
- **Onay süreci:** `## PIA house style`'daki onaylayan.

## Sonuç doğuran işlem kapısı (değerlendirmenin bir makama sunulması)

İç PIA araştırma ve belgelemedir. KVKK'da Kurul'a önceden danışma mekanizması yoktur; ama değerlendirme bir **AB denetim makamına** sunulabilir (Art. 36 önceden danışma) ya da Kurul bir inceleme/şikâyet sürecinde bilgi ve belge isteyebilir (Kurul'un istediği bilgi ve belge 15 gün içinde gönderilir: 6698 m. 15/3). Bu aşamaya geçmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> Bir makama sunulan değerlendirme denetim dosyasının parçası olur; önemli bir eksik ya da hata yaptırım riskine dönüşür. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: rejim ve makam, sunumun nedeni (zorunlu / talep üzerine / gönüllü), tespit edilen riskler, tedbirlerden sonra kalan risk, belirsiz noktalar; avukata sorulacak üç soru. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan sunuma yönlendirme.

## ArthurLegal MCP

```
tr_mevzuat_madde_getir(number="6698", madde_no=["3","4","5","6","7","9","10","11","12","16"])
tr_mevzuat_icinde_ara(number="6698", query="etki değerlendirmesi")
tr_semantik_ara(kurum="kvkk", query="meşru menfaat denge testi")
tr_semantik_ara(kurum="kvkk", query="açık rızanın hizmet şartına bağlanması")
tr_semantik_ara(kurum="kvkk", query="çalışanların izlenmesi kamera")
tr_mevzuat_madde_getir(number="6563", madde_no=["6","8"])
eu_get_document_text(celex="32016R0679", offset=224000)    ← Art. 35–36; Art. 3 (uygulama alanı) ≈ offset 156000; Art. 6 ve 9 ikisinin arasında
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde için "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/". Atıf etiketi: `[ArthurLegal TR — 6698 m. X — GG.AA.YYYY]`, `[ArthurLegal EU — CELEX … — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`; etiketleri silme ya da birleştirme.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu PIA'ya göre uyarla (koşul listesini ürün ekibine gönder, eskalasyon, ek olgu iste, DPA incelemesi başlat, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- İşlemeyi onaylamaz; PIA'yı insan imzalar.
- Bir denetim makamına sunulacak resmî VKED'yi kendiliğinden yazmaz; bu iç değerlendirmedir (resmî sürüm için GDPR Art. 35(7) asgari içeriğini araçla çekip ayrıca hazırla).
- Tedbiri tasarlamaz; neyin tedbir gerektirdiğini söyler, çözümü mühendislik tasarlar.
