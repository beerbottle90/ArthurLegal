---
name: ip-legal-cease-desist
description: >
  İhtarname: marka, telif ya da haksız rekabet ihlaline karşı uygulama duruşunuza
  göre ayarlı ihtarname taslağı hazırlar (--send) ya da size gelen ihtarnameyi
  seçenek notuna çevirir (--receive). Türk hukuku tabanı: SMK m. 7, 29, 149-151,
  154, 156, 159; FSEK m. 66-71, 77; TTK m. 55-56; tebliğ kanalı noter ya da KEP
  (TTK m. 18/3). Göndermeden önce yüksek sesli kapı çalışır.
argument-hint: "<--send | --receive> [bağlam, karşı taraf ya da gelen ihtarnamenin yolu]"
---

# /cease-desist — İhtarname (gönderme / gelen ihtarname triyajı)

- `/arthurlegal:ip-legal-cease-desist --send` — duruşa göre ayarlı ihtarname taslağı; teslimden önce kapı.
- `/arthurlegal:ip-legal-cease-desist --receive` — gelen ihtarnameyi okur, seçenekleri ve önerisiyle triyaj notu yazar.
- Bayrak yoksa bir kez sor: "İhtarname mi gönderiyoruz (hak ileri sürüyoruz), yoksa gelen bir ihtarnameyi mi değerlendiriyoruz (savunuyoruz)?"

## Talimat

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Yoksa ya da `[PLACEHOLDER]` içeriyorsa dur: "Önce `/arthurlegal:ip-legal-cold-start-interview` çalıştırın — ihtarname skill'i uygulama duruşunuza, onay matrisinize ve pratik alanlarınıza dayanır."
2. **Matter:** `## Matter workspaces` → `Enabled` `✗` ise atla. Açık ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:ip-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasındaki `## Matter-specific overrides` uygulama varsayılanının önüne geçer. Çıktılar `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/` altına; `Cross-matter context` `on` değilse başka matter okunmaz.
3. **Bağlam:** `## Enforcement posture` (`Default posture:`, `When we send a C&D`, `When we send a soft letter first`, `When we just file`, `Approval matrix`, `Automatic escalations`), `## IP practice profile` (`Practice area mix:`, `Registered in:`, `Outside counsel roster`), `## Who's using this`, `## Outputs`. Profilde ihtarname şablonu varsa (`Seed documents reviewed`) yapısını izle.
4. **Kapıya uy:** gönderme modunda kapı, nihai taslak diske yazılmadan önce her seferinde çalışır.
5. **Onay matrisine uy:** `Approval matrix` → `Cease-and-desist` satırındaki onaylayanı ve `Automatic escalations` listesini kapıda göster; gizleme.
6. **Devret:** alma modunda öneri "kesin cevap" ise `--send` moduna cevabi ihtarname olarak geç; dava, menfi tespit, hükümsüzlük ya da iptal öneriliyorsa `Outside counsel roster`'daki avukata/vekile eskale et — taslak yazma.

**Anahtarları çevirme:** `## Enforcement posture`, `Default posture:`, `Approval matrix`, `Cease-and-desist`, `Automatic escalations`, `## IP practice profile`, `Registered in:`, `## Decision posture on subjective legal calls` adları aynen kalır.

## ⏰ ÖN-KONTROL — Süre (her çalıştırmada)

**Alma modunda:**
- İhtarnamenin tebliğ tarihi? Gönderenin koyduğu süre kanuni süre değildir; ama dava çoğu zaman o süreden sonra gelir.
- Karşı tarafın hakkı tescilli sınai hak ise SMK m. 154 yolu açıktır: hak sahibinden görüş istenir; talebin tebliğinden itibaren **bir ay** içinde cevap gelmez ya da cevap kabul edilmezse tecavüzün mevcut olmadığının tespiti davası açılabilir. Size karşı tecavüz davası **açılmışsa** bu dava açılamaz — erken karar önemli.

**Gönderme modunda:**
- Tazminat zamanaşımı: SMK m. 157 TBK'nın zamanaşımı hükümlerine yollar; FSEK m. 70/2 mali hak tazminatını haksız fiil hükümlerine bağlar → TBK m. 72: zararı ve faili öğrenmeden **iki yıl**, her hâlde fiilden **on yıl** (ceza zamanaşımı daha uzunsa o).
- Ceza yolu düşünülüyorsa: marka (SMK m. 30/6) ve telif (FSEK m. 75) suçları şikâyete bağlıdır; şikâyet süresi fiili ve faili öğrenmeden **altı ay** (TCK m. 73/1-2). Telifte hak belgeleri bu süre içinde başsavcılığa verilmezse kovuşturmaya yer olmadığı kararı verilir (FSEK m. 75/1).
- Karşı tarafın **tescilli** sonraki markasına beş yıl üst üste bilerek sessiz kaldıysanız, kötüniyet yoksa markanızı hükümsüzlük gerekçesi yapamazsınız (SMK m. 25/6) — gecikmeyi kayda geçir.

Kalan süre < 15 gün → 🔴 ACİL; `Outside counsel roster`'daki avukatla hemen koordine et.

## Destination check

Çıktının nereye gideceğine bak. **Giden ihtarname** karşı tarafa gider: üst başlık ve iç not taşımaz. İç taslak, gönderim öncesi brif ve triyaj notu `## Outputs` üst başlığını taşır. Kullanıcı geniş bir kanal (şirket geneli, satış ekibi, sigortacı, karşı taraf) söylerse: avukatın sır saklama yükümlülüğü (Av.K. m. 36) ABD'deki "privilege" gibi belgeyi koruyan genel bir kalkan değildir; dar çevre dışına çıkan metin gizliliğini fiilen kaybeder. (a) hukuk için tam sürüm, (b) geniş kanal için arındırılmış sürüm ya da (c) ikisini öner. Kanonik kural: `## Shared guardrails → Destination check`.

## Türk hukuku çerçevesi (kısa)

| Hak | Dayanak | Hukuki talepler | Ceza |
|---|---|---|---|
| Tescilli marka | SMK m. 7/2 (aynılık; benzerlik + karıştırılma ihtimali; tanınmış markada itibardan haksız yarar), m. 29 (tecavüz fiilleri) | m. 149: tespit, önleme, durdurma, kaldırma + maddi/manevi tazminat, el koyma, imha, ilan; m. 150-151 tazminat ve yoksun kalınan kazanç (üç hesap yolu); m. 159 ihtiyati tedbir | m. 30: Türkiye'de tescil şart (30/5), şikâyete bağlı (30/6) |
| Tescilsiz işaret | Marka koruması tescille doğar (SMK m. 7/1) → haksız rekabet: karıştırılmaya yol açan önlemler (TTK m. 55/1-a-4) | TTK m. 56: tespit, men, maddi durumun ortadan kaldırılması, kusur varsa tazminat | — |
| Telif (eser) | Eser = sahibinin hususiyetini taşıyan fikir ve sanat ürünü (FSEK m. 1/B-a); sahibi onu meydana getiren (m. 8); mali haklar m. 21-25 | m. 66 tecavüzün ref'i (kusur şart değil), m. 69 men'i, m. 68 izinsiz kullanımda sözleşme ya da rayiç bedelin en çok üç kat fazlası, m. 70 tazminat ve kâr devri, m. 77 ihtiyati tedbir | m. 71, şikâyete bağlı (m. 75) |
| İş ürünü / görünüm | TTK m. 55/1-c (başkasının iş ürününden yetkisiz yararlanma, teknik çoğaltma) | TTK m. 56 | — |

- **Görevli mahkeme:** fikri ve sınai haklar hukuk/ceza mahkemesi, yoksa asliye (SMK m. 156/1; FSEK davalarında da bu mahkemeler, FSEK m. 76/1). **Yetki:** hak sahibinin davası için davacının yerleşim yeri, fiilin gerçekleştiği ya da etkilerinin görüldüğü yer (SMK m. 156/3).
- **Ülkesellik:** fikri mülkiyet hakları koruma talep edilen ülkenin hukukuna tabidir (MÖHUK m. 23/1). Fiil ya da karşı taraf `Registered in:` dışındaysa taslaktan önce işaretle; o ülke için ArthurLegal'da kaynak varsa ilgili önekle ara (ör. AB marka: `eu_search_eu_law(query="European Union trade mark")`), yoksa "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."
- **Tescil teyidi:** TÜRKPATENT kayıtları ArthurLegal MCP'de **yoktur**; tescil no, sınıf ve durum TÜRKPATENT'in kendi arama ekranından elle çekilir ve kaynağıyla tarih damgası alır. Çekilmediyse "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.turkpatent.gov.tr/" yaz.
- **İçtihat:** karar numarasını ezberden yazma. Ara: `tr_ictihat_ara(courts=["YARGITAYKARARI"], query="+marka +karıştırılma +ihtimali")`, `tr_ictihat_ara(courts=["YARGITAYKARARI"], query="+FSEK +tecavüzün +men'i")`; anlamsal: `tr_ictihat_semantik_ara(initial_keyword="ihtarname marka tecavüz", query="ihtarnamede aşırı talep kötüniyet sayılır mı")`. Dönen künyeyi birebir kullan.

## Gönderme modu — ihtarname taslağı

### Adım 1: Hak

> Hangi hakkı ileri sürüyoruz?
> - **Marka** — tescilli mi? TÜRKPATENT / EUIPO / WIPO Madrid tescil no, Nice sınıf(lar)ı, tescil yayım tarihi? Tescilsizse ilk kullanım tarihi, kullanım bölgesi ve tanınmışlık delili?
> - **Telif** — eser nedir, kim meydana getirdi (FSEK m. 8), haklar size nasıl geçti (sözleşme, FSEK m. 18/2 işçi eseri)? Kayıt-tescil isteğe bağlıdır ve hak doğurmaz; ispat kolaylığıdır (FSEK m. 13/son).
> - **Haksız rekabet** — hangi TTK m. 55 hâli?

Tescilli hak tescil numarasıyla, tescilsiz hak delil paragrafıyla yazılır. Tescil kapsamı ile şikâyet edilen kullanım farklı sınıftaysa söyle — tescilin kapsamını şişirme.

### Adım 2: Fiil

Kim (unvan, MERSİS no, kişi, platform hesabı), ne (işaret, kopya, ürün; örnek ekle), nerede (URL, pazaryeri ilanı, mağaza, sosyal medya), ne zamandan beri, hangi delil (ekran görüntüsü, fatura, izleme hizmeti bulgusu, müşteri karışıklığı bildirimi). Sıfat değil olgu: "[tarih]'te [URL]'de [X] markalı ürünü sattınız" sıfatlardan güçlüdür. Delil kaybolabilecekse dava öncesi **delil tespiti** (HMK m. 400) ya da tazminat için belge sunumu talebi (SMK m. 150/3) değerlendir.

### Adım 3: İlişki

Rakip (standart) · bayi/kanal ortağı (yumuşak mektup yolunu düşün) · eski lisans alan/eski çalışan/eski ortak (sözleşmeyi oku; lisans haklarını izinsiz genişletmek de tecavüzdür, SMK m. 29/1-ç) · tanımadığımız kişi (standart) · **mevcut müşteri/ortak** (profil gereği otomatik eskalasyon; taslaktan önce işaretle).

### Adım 4: Talep

Durdurma · hesap verme (satış, kâr, miktar — tazminat tabanı) · stok imhası/toplatma · tazminat · alan adı/hesap devri · yayından kaldırma ve düzeltme ilanı · belirli tarihe kadar yazılı taahhüt. **Talep orantılı olmalı:** fiilin gerektirmediği talepler ileride hakkın kötüye kullanılması (TMK m. 2/2) ve kötüniyet tartışması doğurur.

**Pazaryeri paralel yolu:** ihlal bir pazaryerinde ya da sosyal ağdaysa platformun fikri mülkiyet bildirim formu (marka koruma programları, "IP ihlali bildir" formları) çoğu zaman günler içinde sonuç verir; ihtarname ise karşı tarafa stoku eritecek zaman tanır. İkisi birbirini dışlamaz: platform bildirimi + platform dışı (kendi sitesi, toptan, fiziki satış) için ihtarname. İnternetteki telif ihlalinde kanuni yol FSEK ek m. 4/3'tür → `/arthurlegal:ip-legal-takedown`. Gönderim öncesi brifte paralel yolun durumu yazılır: yapıldı / sırada / reddedildi (neden).

### Adım 5: Duruşa göre ayar

`Default posture:` değerine göre:
- **Aggressive** — kesin dil, kısa süre (çoğunlukla 7 gün), açık sonuç dili (FSHHM'de tespit, men, tazminat davası ve ihtiyati tedbir).
- **Measured** — kesin ama profesyonel, 15-30 gün, sonuçlar abartısız, cevap gelirse görüşmeye açık.
- **Conservative** — yumuşak mektup, uzun ya da süresiz, "görüşmek isteriz" açılışı, sonuç dili yok denecek kadar az.

`When we send a C&D`, `When we send a soft letter first`, `When we just file` satırlarını da oku. Olgu yumuşak mektup ya da doğrudan dava desenine uyuyorsa taslaktan önce sor. `matter.md` sapmaları uygulama varsayılanını yener.

### Adım 5.5: Karşı taraf incelemesi — ZORUNLU ÖN ŞART

Taslaktan önce aşağıdakini tek blokta göster ve kullanıcının onayını al:

```
## Karşı taraf incelemesi — [Unvan]
- **Kimlik:** [tam unvan, MERSİS no, merkez; Ticaret Sicili Gazetesi kaydı; yabancıysa LEI — `gleif_search_entities` ile; kaynak, teyitsizse `[doğrula]`]
- **Büyüklük:** [çalışan bandı, ciro bandı biliniyorsa, grup şirketi mi — kaynak]
- **Kendi fikri mülkiyet portföyü:** [TÜRKPATENT/EUIPO aramasında komşu sınıflarda marka, patent — elle; bulunamadıysa "bulunamadı"]
- **Dava geçmişi:** [Türkiye'de taraf adıyla açık dosya araması yok; yayımlanan kararlar anonimdir — "kamuya açık kaynaktan belirlenemedi" de, uydurma]
- **Vekili:** [bilinen avukat/marka vekili ya da "belirlenemedi"]
- **Karşı hamle riski:** [yüksek/orta/düşük — menfi tespit (SMK m. 154; telifte HMK m. 106), hükümsüzlük/iptal talebi, kötüleme iddiası; bir cümle gerekçe]
- **İlişki riski:** [müşterimiz mi, ortak yatırımcı, olası alıcı/ortak — ya da "yok"]
**Tetiklenen otomatik eskalasyonlar:** [profildeki listeden]
**Taslaktan önce teyit:** Bu karşı tarafa ihtarname istiyor muyuz? Eskalasyon varsa onaylayan taslaktan ÖNCE onay verir.
```

Boş bir "tamam" yetmez: "Taslaktan önce — incelemede hesabı değiştiren bir şey var mı? Büyüklük, vekil, ilişki?" Kimlik ya da büyüklük doğrulanamıyorsa söyle ve sor: "[x]'i mevcut kaynaklardan teyit edemiyorum; sizde var mı, yoksa teyit gelene kadar bekleyelim mi?"

**Not:** ABD'deki "alıcı kendi seçtiği mahkemede dava açar" riski Türkiye'de daha dardır: üçüncü kişinin sınai hak sahibine karşı davası kural olarak hak sahibinin (davalının) yerleşim yerinde açılır (SMK m. 156/5). Telifte bu özel kural yoktur; genel yetki kuralları uygulanır.

### Adım 6: Taslak

**Biçim — ihtarname:**
1. **İHTAR EDEN** — [Müvekkil], adres; vekili (varsa) ve vekâletname bilgisi
2. **MUHATAP** — unvan, MERSİS no, adres (KEP adresi varsa)
3. **KONU** — kısa, stratejiyi ele vermeyen: "[MARKA] markasına (TÜRKPATENT tescil no [•]) tecavüzün durdurulması talebidir."
4. **AÇIKLAMALAR** — (a) hak: tescil no, sınıf, tescil tarihi / eser ve hak zinciri / tescilsiz kullanım delili; (b) fiil: kim, ne, nerede, ne zaman, delil; (c) hukuki dayanak: doğrulanmış maddeler (ör. SMK m. 7, 29, 149; FSEK m. 66, 68; TTK m. 55, 56)
5. **SONUÇ VE İSTEM** — numaralı, somut, orantılı talepler; son tarih (takvim günü) ve teyit biçimi
6. **Sonuç ihtarı** — duruşa göre ayarlı
7. **Delilleri koruma çağrısı** — ilgili kayıt, yazışma ve stok bilgisinin korunması
8. **Hakların saklı tutulması** — "Her türlü hukuki ve cezai hakkımız saklıdır."
9. **İmza** — profildeki onaylayana göre

**Tebliğ kanalı:** ispat ve tarih için noter ya da güvenli elektronik imzalı KEP. İhtar, tacirler arasında temerrüde düşürme, fesih ya da sözleşmeden dönme içeriyorsa bu kanallardan biri zorunludur (TTK m. 18/3: noter, taahhütlü mektup, telgraf, KEP). Kanalı brifte yaz.

**Taslak kuralları:**
- **Olgu sıfattan önce.** Tarih, URL, tescil no, örnek.
- **Kapsamı şişirme.** Başka sınıftaki kullanımı tescil kapsamındaymış gibi yazma. Karşı tarafın müşterilerine ya da platformlara giden yanlış veya gereksiz incitici beyan, kötüleme sayılan haksız rekabet (TTK m. 55/1-a-1) iddiasına dönebilir.
- **Ceza şikâyetini pazarlık kozu yapma.** "Şu tutarı ödemezseniz şikâyet ederiz" dili, hakkı olan bir şeyi yapacağından bahisle haksız çıkar sağlamaya zorlama olarak şantaj (TCK m. 107/1) tartışması doğurabilir — **tartışmalı; avukat değerlendirsin.** Ceza yolunu sonuç ihtarında genel olarak "saklı haklar" içinde an.
- **Atıflar:** her madde `tr_mevzuat_madde_getir` ile çekilir ve `[ArthurLegal TR — 6769 SMK m. X — GG.AA.YYYY]` etiketi alır; kullanıcının verdiği `[kullanıcı verdi]`, hafızadan `[model bilgisi — doğrula]`, web'den `[web araması — doğrula]`. Etiketleri silme. Çekilemeyen madde: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".
- **Sonuç dili duruşa göre:** Aggressive → somut yollar (tespit, men, tazminat davası; ihtiyati tedbir). Measured → "her türlü hakkımız saklıdır." Conservative → "başka adım düşünmeden önce görüşmek isteriz."

### Adım 7: Teslimden önce kapı

Taslağı sohbette göstermeden ya da .docx yazmadan önce aynen göster. **Kullanıcı kapıyla gerçekten ilgilenmeli** — boş bir onay, kapı olmamasından kötüdür.

```
┌─────────────────────────────────────────────────────────────┐
│  BU TASLAK BİR YERE GİTMEDEN ÖNCE                            │
├─────────────────────────────────────────────────────────────┤
│  Bu, avukat incelemesi için taslaktır — gönderilecek mektup  │
│  değildir. İhtarname bir hak iddiasıdır ve sonuç doğurur:    │
│  • Karşı taraf tecavüzün mevcut olmadığının tespitini        │
│    (SMK m. 154; telifte HMK m. 106) ya da markanızın         │
│    hükümsüzlüğünü/iptalini (SMK m. 25, 26) isteyebilir.      │
│  • Aşırı ya da kötüniyetli iddia aleyhinize döner: kötüleme  │
│    (TTK m. 55/1-a-1), hakkın kötüye kullanılması (TMK m. 2), │
│    tedbir alınırsa haksız tedbir tazminatı (HMK m. 399).     │
│  • Ucuz kapanmayabilecek bir uyuşmazlık başlatır.            │
│  Gitmeden önce teyit edin:                                   │
│    1. Hak geçerli — tescil sicilden çekildi (varsayılmadı)   │
│       ya da tescilsiz hak delille sağlam.                    │
│    2. İddia savunulabilir — makul bir meslektaş bu olgularla │
│       aynı iddiayı ileri sürerdi.                            │
│    3. Talep orantılı — fiilin gerektirdiği kadar.            │
│    4. Uyuşmazlık başlatma yetkisi olan kişi onayladı.        │
│    5. Karşı taraf incelemesi (Adım 5.5) gösterildi ve        │
│       teyit edildi. Koşullu değil, zorunlu.                  │
│  Onaylayan: [Approval matrix → Cease-and-desist satırı]      │
│  Otomatik eskalasyonlar: [Adım 5.5'te çıkanlar]              │
│  Paralel yol (pazaryeri): [yapıldı/sırada/reddedildi/yok]    │
└─────────────────────────────────────────────────────────────┘
```

Kullanıcı avukat değilse (`## Who's using this`) ekle: "İhtarname karşı tarafın cevabının ötesinde sonuç doğurur; aleyhinize kullanılabilecek bir hak iddiasıdır. Hukuki mütalaa ve dava takibi baroda yazılı avukatlara aittir (Av.K. m. 35/1). Bir avukatla gözden geçirdiniz mi? Görüşme için tek sayfalık brif: [taraflar, hak, fiil, talep, duruş, yukarıdaki riskler, ters gidebilecekler, avukata sorulacaklar]. Avukat bulmak için ilinizin barosuna başvurabilirsiniz; tescil işlemleri için TÜRKPATENT'in yayımladığı marka/patent vekili sicili bir başlangıçtır."

Kapı ile açık etkileşim olmadan .docx yazma ve taslağı "hazır" işaretleme.

### Adım 8: Çıktı

- **Asıl:** `<matter-klasörü>/cease-desist/<slug>/draft-v<N>.docx` (uygulama düzeyinde `cease-desist/<slug>/draft-v<N>.docx`), `docx` skill'iyle, Adım 6 yapısında; üst başlık giden mektuptan çıkarılır. Önce sohbette düz metin göster, yinele, sonra diske yaz.
- **İnceleyen notu** (yalnız sohbet önizlemesinde): "⚠️ Bu, avukat incelemesi için ihtarname taslağıdır; gönderilmeye hazır değildir. Gönderim, kapıda sayılan sonuçları doğurur. Avukat inceler, düzeltir ve mesleki sorumluluğu üstlenir."
- **Sessiz tamamlama yok:** bağlı araç bir dayanak için az sonuç döndürürse bulduğunu bildir ve dur; web ya da hafızadan sessizce doldurma. Seçenek sun: sorguyu genişlet, başka araç, etiketli web araması, yer tutucu bırak.
- **Gönderim sonrası kontrol listesi** `<matter-klasörü>/cease-desist/<slug>/checklist.md`: onaylayanın son okuması, tüm `[doğrula]` etiketleri çözüldü, atıflar doğrulandı, üst başlık çıkarıldı, imza, tebliğ kanalı (noter/KEP) ve tebliğ belgesi saklandı, son tarih takvimde, cevap gelmezse eskalasyon planı, matter açıldı mı.

## Alma modu — gelen ihtarnamenin triyajı

### Adım 1: Oku

Gönderen (unvan, imzalayan, vekil) · muhatap (hangi şirketimiz/kişimiz) · tebliğ kanalı ve tarihi (noter, KEP, e-posta) · ileri sürülen hak (tescil no, ülke) · iddia edilen fiil · dayanak (madde, sözleşme) · talepler ve süre · tehditler · ton (yumuşak / kesin / sert; vekil imzası genelde ciddiyet işaretidir).

### Adım 2: İddiayı değerlendir (hukuki görüş değil, yapılandırılmış okuma)

- **Hak geçerli mi?** Tescil gerçek ve yürürlükte mi — TÜRKPATENT/EUIPO aramasından elle; ArthurLegal'da TÜRKPATENT yok. Sınıflar fiili kapsıyor mu? Tescilsiz iddiada hangi delil var?
- **Karıştırılma / benzerlik:** markada karıştırılma ihtimali (SMK m. 7/2-b) içtihatla şekillenen bir değerlendirmedir — `tr_ictihat_ara` ile emsal çek. Dürüst kullanım istisnaları: kendi ad/adres, tanımlayıcı açıklama, yedek parça ve aksesuarda kullanım amacını belirtme (SMK m. 7/5). Telifte: eser niteliği (hususiyet, FSEK m. 1/B-a), fikir-ifade ayrımı (bilgisayar programında temel düşünce ve ilkeler eser değildir, m. 2/son), kanuni istisnalar (m. 33-35, 38).
- **Aşırılık:** talepler fiili aşıyor mu (yalnız etiket değişikliği gerekirken marka devri; tek kanal ihlalinde tüm satışlar)?
- **Zaman:** karşı taraf markasını beş yıldır kullanmıyorsa kullanmama def'i (SMK m. 29/2'nin yollamasıyla m. 19/2); bilerek beş yıl sessiz kaldıysa (m. 25/6); tazminat zamanaşımı (TBK m. 72).
- **Mahkeme:** hak sahibi davacının yerleşim yeri, fiil ya da etki yerinde dava açabilir (SMK m. 156/3); bizim menfi tespit davamız karşı tarafın yerleşim yerinde (m. 156/5).

### Adım 3: Maruziyetimiz

Gerçekten ihlal ediyor muyuz (dürüst bakış)? Uyum maliyeti mi, uyuşmazlık maliyeti mi büyük? Gönderen gerçek hak sahibi mi, toplu ihtarname gönderen mi? Davanın ötesinde ne var (marka değeri, müşteriler, benzer ihtarnameler için emsal)? Para talebi davaya dönerse: fikri mülkiyet mevzuatından doğan davalar ticari davadır (TTK m. 4/1-d; ticari işletmeyi ilgilendirmeyen fikir ve sanat eseri davaları hariç) ve konusu para olan alacak/tazminat davalarında dava öncesi arabuluculuk dava şartıdır (TTK m. 5/A) — FSHHM'deki tazminat taleplerine uygulanış biçimi **tartışmalı; içtihadı kontrol et**.

### Adım 4: Seçenekler

- **A — Hızla uy:** iddia savunulabilir, uyum ucuz. Bedel: sonra gösterilebilecek bir kabul. Adım: dar yazılı teyit; geniş teoriyi kabul etme.
- **B — Müzakere:** lisans, birlikte var olma (coexistence), geçiş takvimi. Bedel: zaman. Adım: oyalayıcı cevap + müzakere; uzlaşma yazışmalarını "sulh görüşmesi" başlığı tek başına korumaz — içerik ve bağlamla değerlendirilir.
- **C — Kesin cevap (reddet):** iddia zayıf, aşırı ya da olgusal olarak yanlış. Bedel: pozisyon kilitlenir; iddia aslında sağlamsa cevabımız delil olur. Adım: cevabi ihtarname → `--send`.
- **D — Cevapsız bırak + delili koru:** iddia temelsiz, gönderenin dava kapasitesi görünmüyor. Bedel: dava gelebilir; sessizliğin delil değerlendirmesindeki etkisi duruma göre değişir — **tartışmalı**. Adım: delil koruma talimatı, kayıt, devam.
- **E — Önden git (menfi tespit):** belirsizlik işi etkiliyor, iddia zayıf. Marka/patent/tasarımda SMK m. 154 yolu (görüş talebi → bir ay → tecavüzün mevcut olmadığının tespiti davası; hükümsüzlük davasıyla birlikte de açılabilir); telifte hukuki yarar şartıyla tespit davası (HMK m. 106). Bedel: artık bir dava var; bütçe ve yönetim onayı. Adım: dış avukata eskale — taslak yazma.
- **F — Onların hakkını düşür:** hükümsüzlük davası (SMK m. 25 — mahkeme) ya da TÜRKPATENT'ten iptal talebi (SMK m. 26 — ör. kullanmama, yaygın ad hâline gelme). Bedel: yavaş, masraflı, kamuya açık. Adım: dış avukat/marka vekiline eskale.

Birini iki cümle gerekçeyle öner.

### Adım 5: Süre triyajı

Gönderenin süresi (bağlamaz ama not et) · iç karar tarihimiz (cevap taslağı + onay payı) · kanuni süreler (SMK m. 154 bir ay, zamanaşımı, sözleşmesel düzeltme süreleri). Süreyi tümüyle yok saymak bir tercihtir, varsayılan değil.

### Adım 6: Triyaj notu

Çıktı: `<matter-klasörü>/cease-desist/inbound/<slug>/triage.md`.

```markdown
[ÜST BAŞLIK — profil ## Outputs; role göre]
[GİZLİLİK BLOĞU — aşağıdan role göre tek biri]

# Gelen İhtarname — Triyaj
> **GÖRÜŞ DEĞİL, TRİYAJ.** Yönlendirme ve cevap kararı için yapılandırılmış okuma; esasa ilişkin görüş avukatındır. Her atıf doğrulama etiketi taşır.

**Slug:** · **Tebliğ:** [GG.AA.YYYY, kanal] · **Muhatap:** · **Dosya:**
## İddia
**Gönderen:** · **Hak:** [marka/telif/haksız rekabet — tescil no, ülke] · **Fiil (onların anlatımı):** · **Talepler:** · **Süre:** · **Ton:**
## Hakkın geçerliliği
[sicilden çekildi mi — kaynak ve tarih; çekilmediyse UYARI satırı]
## Dayanak gösterilen hukuk
[her atıf: `[ArthurLegal TR — … — tarih]` ya da `[doğrula]`]
## Makullük
- Karıştırılma/benzerlik/tecavüz: · Aşırılık: · Zaman (kullanmama, sessiz kalma, zamanaşımı): · Mahkeme ve menfi tespit imkânı:
## Maruziyetimiz
- Gerçekten ihlal? · Uyum vs uyuşmazlık maliyeti: · Gönderenin güvenilirliği: · Yan riskler:
**Triyaj derecesi:** [ciddi / tartışmalı / zayıf / temelsiz] — yönlendirme içindir, esas görüşü değildir
## Seçenekler
### A. Uy ### B. Müzakere ### C. Kesin cevap ### D. Cevapsız + koru ### E. Menfi tespit ### F. Hükümsüzlük / iptal
**Öneri:** [harf] — [iki cümle] — `[avukat teyidi gerekli]`
## Süreler
- Gönderenin süresi: · İç karar tarihi: · Kanuni süreler:
## Hemen yapılacaklar
- [ ] Delil koruma talimatı · [ ] Matter açıldı mı · [ ] Sorumlu avukat · [ ] Sigorta bildirimi (varsa) · [ ] İç eskalasyon
```

**Gizlilik bloğu — role göre tek biri:**
- **Avukat:** "Bu triyaj, ters bir iddiaya ilk esas okumamızı ve cevap duruşumuzu kaydeder; avukatın sır saklama yükümlülüğü (Av.K. m. 36) kapsamındaki iş ürünüdür. Türk hukukunda belgeyi her durumda koruyan genel bir 'privilege' kurumu yoktur; karşı tarafa, sigortacıya ya da dar çevre dışına arındırmadan iletmeyin."
- **Marka/patent vekili (avukat değil):** "GİZLİ — AVUKAT SIR SAKLAMA KAPSAMINDA DEĞİL. Av.K. m. 36 avukatlara ilişkindir. Vekil, TÜRKPATENT nezdinde işlem yapabilir (SMK m. 160/1); hukuki mütalaa ve dava takibi ise avukatlara aittir (Av.K. m. 35/1). Belgeyi gizli tutun ve bir avukata götürün."
- **Avukat olmayan:** "GİZLİ — AVUKAT İNCELEMESİNDEN GEÇMEDİ. Avukat görene kadar sır saklama kapsamında sayılmaz; inceleme zinciri dışına iletmeyin."

Sohbeti şu cümleyle kapat: "Bu bir triyaj notudur, görüş değildir. Değerlendirme yalnız mektuba dayanır; bana söylemediğiniz olguları, doğrulayamadığım tescilleri ve yargı çevresi sorunlarını hesaba katmaz. Cevap vermeden, sessiz kalmaya karar vermeden ya da bir yola girmeden önce avukat değerlendirir." Avukat değilse gönderme modundaki baro paragrafını ekle.

### Adım 7: Devir

Kesin cevap → `--send` (kapı yeniden çalışır) · müzakere → matter'da oyalayıcı cevap · menfi tespit/hükümsüzlük/iptal → `Outside counsel roster`'a eskale, taslak yok · matter yoksa ve önemliyse `/arthurlegal:ip-legal-matter-workspace new <slug>` öner · uy/sessiz kal → kararı `history.md`'ye yaz, delil koruma talimatını teyit et.

## Karar duruşu

`## Decision posture on subjective legal calls` gereği: tecavüz olup olmadığı, karıştırılma ihtimali, eser benzerliği, iddianın savunulabilirliği ya da göndermenin güvenli olup olmadığı belirsizse sessizce "sorun yok" deme; avukata işaretle, iki yöndeki etkenleri göster. Varsayımla ihtarname göndermek tek yönlü kapıdır; şüpheyi göstermek iki yönlü.

## Bu skill ne yapmaz

- **Göndermez** — yalnız taslak; onaydan sonra kullanıcı gönderir.
- **Atıf uydurmaz** — doğrulanmamış dayanak yer tutucu kalır.
- **Kapıyı atlamaz** — her gönderme modunda çalışır.
- **Alma tarafında esası kesin karara bağlamaz** — derece yönlendirme içindir.
- **Gönderenin dayanağını kendiliğinden geçerli/geçersiz saymaz** — işaretler.
- **Matter açma kararını vermez** — önerir, kullanıcı karar verir.
- **TÜRKPATENT kaydını araçla çekmez** — o kaynak ArthurLegal MCP'de yoktur; elle teyit edilir.
