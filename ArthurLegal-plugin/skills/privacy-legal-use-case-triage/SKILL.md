---
name: privacy-legal-use-case-triage
description: >
  Bir veri işleme faaliyetinin hızlı ön elemesi — KVKK tabanında (m. 4 genel
  ilkeler, m. 5–6 işleme şartları, m. 10 aydınlatma, m. 16 VERBİS, m. 8–9
  aktarım) faaliyetin devam edebileceğine, PIA gerektiğine, AB'ye dönükse GDPR
  etki değerlendirmesinin zorunlu olduğuna ya da durması gerektiğine karar
  verir; aydınlatma metni ve gizlilik politikasıyla çelişkiyi yakalar, doğru
  sonraki adıma yönlendirir. "PIA gerekir mi", "bu özelliği triage et", "KVKK
  açısından sorun var mı", "gizlilik kontrolü" denince ya da yeni bir veri
  işleme faaliyeti, ürün özelliği veya tedarikçi ilişkisi anlatıldığında kullan.
argument-hint: "[veri işleme faaliyetini ya da özelliği anlatın]"
---

# /use-case-triage — Veri İşleme Ön Elemesi

PIA'dan önce gelen soruyu cevaplar: "Buna değerlendirme gerekir mi; gerekirse hangisi ve önünde ne var?" Triage PIA'dan hızlıdır ve onun yukarısındadır: değerlendirmeyi yazmaz, gerekip gerekmediğini ve hangi şartla ilerleneceğini belirler. Derin iş `/arthurlegal:privacy-legal-pia-generation`'ındır.

Dört sonuç:
- **DEVAM (PROCEED)** — PIA gerekmez; standart güvenceler yeter.
- **PIA GEREKLİ (PIA REQUIRED)** — devreye almadan önce ya da birlikte değerlendirme.
- **VKED ZORUNLU (DPIA MANDATORY)** — yalnız zorunlu etki değerlendirmesi öngören bir rejim (GDPR Art. 35, UK GDPR) uygulanıyor ve tetiği oluşmuşsa. KVKK tek başına bu sınıfı doğurmaz; 6698'de genel bir etki değerlendirmesi yükümlülüğü yoktur.
- **DUR (STOP)** — hukuki sebep yok, genel ilkeye aykırı, aktarım yolu yok ya da aydınlatma metni/gizlilik politikasıyla doğrudan çelişki; yeniden tasarım gerekir.

## Destination check

Çıktı nereye gidiyor? Kullanıcı bir hedef söylediyse (kanal, dağıtım listesi, karşı taraf, "herkes") sır çevresinin içinde mi diye sor. Hedef dışarıdaysa üç seçenek sun: (a) yalnız hukuk için başlıklı tam sürüm, (b) geniş dağıtım için arındırılmış sürüm, (c) ikisi. Başlık koyup metnin başlığın korumadığı yere yapıştırılmasına sessizce yardım etme.

## Önce ayarı oku

`firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## PIA house style` (tetikler), `## Regulatory footprint` (VERBİS durumu, yurt dışı aktarım yolları, sektör, yabancı rejim), `## Privacy policy commitments` (aydınlatma metinleri), `## Escalation`, `## Outputs`, `## Who's using this`. Bunlar belirleyicidir; genel hukuk akıl yürütmesi şirketin gerçekten taahhüt ettiğinin yerini tutmaz.

Dosya yoksa ya da `[PLACEHOLDER]` içeriyorsa:

> Pratik profiliniz henüz kurulmamış — PIA tetiklerini, yükümlülük haritasını ve aydınlatma taahhütlerini oradan alıyorum.
> **İki seçenek:**
> - `/arthurlegal:privacy-legal-cold-start-interview` çalıştırın (birkaç dakika), sonra triage'ı size göre yapayım.
> - **"geçici"** deyin; genel varsayımlarla (Türkiye — KVKK, orta risk iştahı, avukat rolü, playbook yok) triage edeyim ve her çıktıyı `[GEÇİCİ — profilinizi kurun]` diye etiketleyeyim.

**Geçici mod:** triage'ı bu varsayımlarla normal yürüt; taahhütlerle eşleme yerine genel KVKK ilkelerinden sınıflandır. İnceleyen notunu ve her bulgu bloğunu `[GEÇİCİ]` diye etiketle. Sonuna ekle: "Bu, varsayılan kabullerle genel bir çalıştırmaydı. Yükümlülük haritanıza, aydınlatma taahhütlerinize ve risk iştahınıza göre çıktı için `/arthurlegal:privacy-legal-cold-start-interview` çalıştırın."

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:privacy-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Faaliyeti anla

Açıklama belirsizse sınıflandırmadan önce sor:
- Hangi veri, hangi kategoriler? Özel nitelikli veri (m. 6/1) var mı?
- İlgili kişiler kim — müşteri, çalışan, aday, üçüncü kişi, çocuk?
- Amaç ne; hangi sorunu çözüyor?
- Yeni toplama mı, eldeki verinin yeni amaçla kullanımı mı?
- Tedarikçi var mı; yeni mi, mevcut mu? Sunucu nerede?
- Otomatik karar var mı; çıktı birini etkiliyor mu?
- Kullanım bağlamı: yalnız şirket içi mi, müşteriye dönük mü, herkese açık mı?

"Yeni özellik" ya da "veri işleme faaliyeti" doğru sınıflandırma için yetmez.

### 2. Ev tetikleri

`## PIA house style` → tetikleri uygula. Tetik oluştuysa en az **PIA GEREKLİ**. Oluşmadıysa DEVAM demeden önce 3–5'i bitir; bazı faaliyetler iç politika ne derse desin değerlendirme ister.

### 3. KVKK taban kontrolü

| Kontrol | Soru | Dayanak | Açık çıkarsa |
|---|---|---|---|
| Kapsam | Gerçek kişiye ilişkin veri mi; otomatik ya da veri kayıt sisteminin parçası olarak otomatik olmayan yolla mı işleniyor; m. 28/1 istisnası var mı? | m. 2; m. 3/1-d, e; m. 28/1 | Kapsam dışıysa DEVAM (gerekçeyi yaz) |
| Genel ilkeler | Hukuka ve dürüstlük kurallarına uygun; doğru ve gerektiğinde güncel; belirli, açık, meşru amaç; amaçla bağlantılı, sınırlı, ölçülü; gerekli süre kadar muhafaza | m. 4/2-a–d | Aykırılık → DUR ya da tasarım koşulu |
| Hukuki sebep | Her amaç için m. 5/2 şartı ya da açık rıza; özel nitelikli veride m. 6/3 hâli + Kurul'un yeterli önlemleri | m. 5; m. 6/3-4 | Sebep yok → DUR |
| Aydınlatma | Elde etme sırasında: veri sorumlusunun kimliği, amaç, alıcılar ve amacı, toplama yöntemi ve hukuki sebep, m. 11 hakları | m. 10/1-a–d | Eksik → koşul (metin güncellemesi lansmandan önce) |
| Aktarım | Yurt içi üçüncü kişi (m. 8); yurt dışı: yeterlilik → uygun güvence (standart sözleşme 5 iş günü bildirim) → yalnız arızi istisna | m. 8; m. 9/1, 4, 5, 6 | Yol yok → DUR |
| VERBİS | Kayıt yükümlüsü mü, Kurul istisnasında mı? Yeni amaç, kişi grubu, alıcı, yurt dışı aktarım ya da saklama süresi sicil bilgisini değiştiriyor mu? | m. 16/2-4; Veri Sorumluları Sicili Hakkında Yön. m. 13/1 (değişiklikten itibaren 7 gün) | Güncelleme → koşul |
| Veri işleyen | Tedarikçi adına mı işliyor? Sözleşme ve m. 12/2 müşterek sorumluluk | m. 12/1-2 | → `/arthurlegal:privacy-legal-dpa-review` |
| Ticari ileti | Pazarlama iletisi varsa önceden onay ve ret hakkı | 6563 m. 6, m. 8 | Onay yok (m. 6/1 son cümle ve m. 6/2 esnaf-tacir istisnası dışında) → DUR |

VERBİS istisnası Kurul kararıyla getirilir (m. 16/2) → `tr_semantik_ara(kurum="kvkk", query="Veri Sorumluları Siciline kayıt yükümlülüğünden istisna")`; künyeyi araçtan al, ezberden yazma.

**Sektörel katman (önce sor):** banka müşteri verisi → 5411 m. 73/3 (müşteri sırrı; istisnalar dışında açık rıza alınsa dahi müşteriden talep ya da talimat olmaksızın üçüncü kişilerle paylaşılamaz; BDDK yurt dışı paylaşımı yasaklayabilir ve sistemlerin yurt içinde tutulmasına karar verebilir); sağlık → Kişisel Sağlık Verileri Hakkında Yönetmelik + m. 6/3-e; elektronik haberleşme → sektör yönetmeliği (`tr_mevzuat_ara(query="Elektronik Haberleşme Sektöründe Kişisel Verilerin", types=["KKY"])`); çocuk verisi → KVKK'da ayrı bir rejim yok; açık rızayı kimin vereceği (ayırt etme gücü, veli) **tartışmalı — Kurul kararlarını ara**. Sektör satırı yoksa yaz: "sektörel katman yok — kontrol edildi."

**Yaptırım bağlamı** (risk derecesi için; **tutar yazma**): m. 18/1 — aydınlatma yükümlülüğü (a), veri güvenliği (b), Kurul kararlarına uymama (c), VERBİS kayıt ve bildirim (ç), standart sözleşme bildirimi (d; 7499 s.K. ile eklendi) idari para cezası öngörür. Kanun metnindeki alt ve üst sınırlar her takvim yılı başında yeniden değerleme oranında artırılarak uygulanır (5326 m. 17/7) → güncel tutarı Kurum duyurusundan teyit et. Kurul'un idari para cezasına karşı idare mahkemesinde dava açılabilir (m. 18/3). Ceza hukuku: kişisel verilere ilişkin suçlarda TCK m. 135–140; m. 7'ye aykırı olarak silmeme TCK m. 138 (6698 m. 17).

### 4. Zorunlu değerlendirme kontrolü

- **KVKK:** zorunlu etki değerlendirmesi yok → bu adım KVKK için "uygulanmaz".
- **GDPR** `## Regulatory footprint`'te varsa: uygulama alanı için Art. 3'ü, tetikler için Art. 35'i `eu_get_document_text(celex="32016R0679")` ile çek (Art. 3 ≈ offset 156000, Art. 35 ≈ offset 224000). Art. 35(3)'teki hâllerden biri ya da ilgili üye devlet denetim makamının listesi (Art. 35(4)) tetikleniyorsa → **VKED ZORUNLU**. Üye devlet listesi için ilgili ülke aracı (`de_gesetz_ara`, `nl_search_legislation` …); bulunamazsa "ArthurLegal'da bu listenin kaynağı yok; yerel hukukçu görüşü al."
- **UK GDPR:** `uk_search_legislation(query="Data Protection Act 2018")` → `uk_get_section`.
- *Karşılaştırmalı not:* ABD eyalet yasalarının kendi risk değerlendirmesi tetikleri vardır; yalnız CourtListener kuruluysa `courtlistener-rehberi.md` üzerinden, ezberden değil.

**Güçlü göstergeler** (zorunlu olmasa da değerlendirme yap): yeni teknoloji ya da yapay zekâ; çocuk verisi; özel nitelikli veri; ayrı toplanmış veri setlerinin birleştirilmesi; ayrımcılığa elverişli veri ya da çıkarım; münhasıran otomatik analizle kişi aleyhine sonuç (m. 11/1-g); çalışan izleme; ilgili kişinin beklemeyeceği işleme; davranışsal reklam, benzer kitle (lookalike) ve bağlamlar arası takip (aktarım, aydınlatma ve 6563 onay sorunlarını düzenli olarak açığa çıkarır). Zorunlu tetik yok ama gösterge var → **PIA GEREKLİ** (çıktıda göstergeyi belirt).

### 5. Aydınlatma metni / gizlilik politikası çelişkisi

`## Privacy policy commitments`'taki her taahhüdü faaliyetle karşılaştır:
- Metin "X, Y, Z'yi topluyoruz" diyor; faaliyet W'yi topluyor → lansmandan önce metin güncellenir ya da W toplanmaz.
- Metin "üçüncü kişilerle paylaşmıyoruz" diyor; faaliyet veriyi tedarikçinin kendi amaçları için geçiriyor → aktarım şartı (m. 8) ve rol sorunu.
- Metin "yurt dışına aktarmıyoruz" diyor; faaliyet yurt dışı bulut kullanıyor → m. 9 yolu + metin.
- Metinde saklama süresi var; faaliyet daha uzun saklıyor (m. 4/2-d).
- Metin veriyi yalnız belirli amaçla kullanacağını söylüyor; faaliyet yeni amaç ekliyor → yeni hukuki sebep ve aydınlatma.
- Faaliyet, hak başvuru sürecinin kapsamadığı yeni bir veri kategorisi yaratıyor (m. 11, m. 13).

Doğrudan çelişki → **DUR**. "Dikkatle devam" değil: çelişki (metin güncellemesi ya da yeniden tasarım) çözülmeden ilerlenmez.

### 6. Sınıflandırma ve çıktı

Başa profilin `## Outputs` bölümündeki role göre üst başlığı koy.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

### Sonuç
[PIA gerekli / VKED zorunlu / Devam / Dur — tek cümle neden]

**FAALİYET:** [anladığın hâliyle]
**SINIF:** [DEVAM / PIA GEREKLİ / VKED ZORUNLU / DUR]
**Ev tetiği:** [Evet / Hayır]
**KVKK tabanı:** [temiz / açıklar: m. … — kısa]
**GDPR Art. 35 tetiği:** [Evet — hangi hâl / Hayır / Uygulanmaz (GDPR kapsam dışı)]
**Aydınlatma/politika çelişkisi:** [Yok / Var — hangi taahhüt]
**Hukuki sebep:** [m. 5/2-… / m. 6/3-… / açık rıza / "belirsiz — PIA'da belirlenecek"]
**Gerekçe:** [1–3 cümle]
**Kaynaklar:** ArthurLegal MCP — [madde, Kurul kararı]; doğrulanamayan: [liste] · **Tartışmalı:** [liste]

*PIA GEREKLİ ya da VKED ZORUNLU ise — ilerlemeden önce koşullar:*
| Gereklilik | Sahibi | Tamam? |
|---|---|---|
| [PIA — VKED formatında ise belirt] | [gizlilik hukukçusu] | ☐ |
| [Meşru menfaat denge testi (m. 5/2-f)] | [gizlilik hukukçusu] | ☐ |
| [Veri işleyen sözleşmesi / standart sözleşme + 5 iş günü bildirim] | [hukuk] | ☐ |
| [Aydınlatma metni güncellemesi] | [gizlilik hukukçusu] | ☐ |
| [VERBİS güncellemesi] | [irtibat kişisi] | ☐ |
| [Açık rıza mekanizması kuruldu ve test edildi] | [ürün] | ☐ |
| [Hak başvuru süreci yeni veri kategorisini kapsıyor] | [gizlilik / ürün] | ☐ |

*DUR ise:*
**Çelişki:** [taahhüt ya da ilke ve madde]
**İlerlemek için biri değişmeli:** (A) faaliyeti çelişki doğurmayacak şekilde yeniden tasarla · (B) aydınlatma metnini/politikayı güncelle (güncellemenin hukuki sebeple tutarlılığı ayrıca incelenir)
```

Yol yoksa yol uydurma: faaliyet taahhütlerle ya da hukuki sebeple bağdaşmıyorsa bunu açıkça söyle.

PIA GEREKLİ ya da VKED ZORUNLU sonucundan sonra her zaman sor: "PIA'ya şimdi başlayayım mı? Ayrı komut çalıştırmadan mülakat sorularını sorup değerlendirmeyi yazabilirim." Evet → `pia-generation` skill'ini yükle, faaliyet tanımını ve bulunan tetikleri aktararak aynı konuşmada devam et. Hayır → sonuç geçerli; PIA her zaman `/arthurlegal:privacy-legal-pia-generation [faaliyet]` ile çalıştırılabilir.

### 7. Eklentiler arası devir

Yalnız gerçekten ilgiliyse ekle; ikisini birden kalıp olarak ekleme.
- **Yapay zekâ kararı:** faaliyette kişiler hakkında karar veren ya da karara etki eden bir yapay zekâ sistemi varsa: "PIA'ya ek olarak yapay zekâ etki değerlendirmesi gerekebilir. `/ai-governance-legal:aia-generation [faaliyet]` (ArthurLegal'de hazırlanıyor: Faz 1 İş 5; o zamana kadar yapay zekâ etki değerlendirmesini bu PIA içinde ayrı bir bölüm olarak yürüt) — ikisi birbirinin yerine geçmez."
- **Ürün lansmanı:** yeni ürün özelliği ise: "Lansmansa ürün hukukçusunu dahil et. `/product-legal:launch-review` (ArthurLegal'de hazırlanıyor; o zamana kadar ürün hukukçusuyla doğrudan koordine et)."

## Toplu triage

Özellik listesi, yol haritası ya da iş listesi gelirse önce özet tablo, sonra DEVAM olmayan her satırı aç:

| # | Faaliyet | Sınıf | Ana koşul / engel |
|---|---|---|---|
| 1 | [faaliyet] | 🟢 Devam | — |
| 2 | [faaliyet] | 🟡 PIA gerekli | Meşru menfaat denge testi; veri işleyen sözleşmesi yok |
| 3 | [faaliyet] | 🟠 VKED zorunlu | AB'deki kişilerin özel nitelikli verisi, büyük ölçek |
| 4 | [faaliyet] | 🔴 Dur | Aydınlatma metniyle çelişki — amaç sınırlaması (m. 4/2-c) |

## Uç durumlar

- **"Anonim" otomatik DEVAM değildir.** Anonimleştirme, başka verilerle eşleştirilerek dahi kimliği belirli veya belirlenebilir bir kişiyle ilişkilendirilemeyecek hâle getirmedir (m. 3/1-b). Nasıl yapıldığını ve yeniden tanımlamanın gerçekçi olup olmadığını sor; kimliği "belirlenebilir" kaldıkça veri kişisel veridir (m. 3/1-d).
- **"Benzerini zaten yapıyoruz" triage değildir.** Hiç değerlendirilmemiş mevcut işleme yeni işlemeyi korumaz; ölçek, amaç ya da veri kategorisi belirgin biçimde farklıysa yeniden triage.
- **"Sadece pilot" triage'ı atlatmaz.** Gerçek kullanıcı ya da çalışan verisine dokunan pilot aynı tetiklere tabidir.
- **"Tedarikçi gizliliği hallediyor."** Tedarikçi altyapıyı yönetir; amaçları belirleyen veri sorumlusu sizsiniz (m. 3/1-ı) ve güvenlik tedbirlerinden onunla müştereken sorumlusunuz (m. 12/2). Sözleşme gerekir, triage amaç için yine uygulanır.
- **Çıkarım ve türetilmiş veri sayılır.** Davranış skoru, tahmini tercih gibi kişi hakkında üretilen bilgi, belirlenebilir kişiye ilişkin her türlü bilgi olarak kişisel veridir (m. 3/1-d). "Sadece skor hesaplıyoruz" skorun neyi temsil ettiğini gizlemesin.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6698", madde_no=["2","3","4","5","6","8","9","10","16","18"])
tr_mevzuat_madde_getir(number="5326", madde_no=["17"])
tr_mevzuat_ara(query="Veri Sorumluları Sicili", types=["KKY"])  → tr_mevzuat_icinde_ara(mevzuat_id=..., query="değişiklik")
tr_semantik_ara(kurum="kvkk", query="aydınlatma yükümlülüğünün yerine getirilmemesi idari para cezası")
tr_semantik_ara(kurum="kvkk", query="açık rıza alınmadan pazarlama")
tr_kurum_karari_ara(kurum="kvkk", query="aydınlatma")   ← yalnız son sayfaları tarar; sıra tarihe göre değil; arşiv için tr_semantik_ara
tr_kurum_karari_getir(kurum="kvkk", id=<sonuçtaki id>)
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde için "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" (Kurul kararında https://www.kvkk.gov.tr/). Atıf etiketi: `[ArthurLegal TR — 6698 m. X — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu triage'a göre uyarla (PIA'yı başlat, DPA incelemesi, aydınlatma metni güncellemesi, eskalasyon, ek olgu iste, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Değerlendirmeyi yazmaz; gerekip gerekmediğini söyler (yazım `pia-generation`'da).
- İşlemeyi onaylamaz; sınıf bir öneridir, karar avukatın.
- Ceza tutarı söylemez; tutarlar her yıl değişir, güncel kaynaktan teyit edilir.
