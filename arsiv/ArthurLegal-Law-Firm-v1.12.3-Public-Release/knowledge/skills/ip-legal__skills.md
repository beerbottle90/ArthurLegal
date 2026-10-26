# ip-legal - Skill Referans Kitapcigi

> Değişiklik bildirimi (Apache-2.0 md. 4(b)): Bu kitapçık Anthropic'in `claude-for-legal` deposundaki aynı adlı eklentiden uyarlanmıştır. ArthurLegal tarafından Türk hukuku esas alınarak Türkçe yeniden yazılmıştır (2026-10); yabancı yargı çevreleri için yalnız ArthurLegal MCP araçlarına yönlendirir. Üst kaynak ve sürüm izi: ATTRIBUTION.md.

> Alan: Fikri sinai haklar - marka, patent, OSS, takedown
> Toplam skill: 12
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /ip-legal:cease-desist (268 satir)
- /ip-legal:clearance (231 satir)
- /ip-legal:cold-start-interview (250 satir)
- /ip-legal:customize (52 satir)
- /ip-legal:fto-triage (219 satir)
- /ip-legal:infringement-triage (230 satir)
- /ip-legal:invention-intake (184 satir)
- /ip-legal:ip-clause-review (171 satir)
- /ip-legal:matter-workspace (141 satir)
- /ip-legal:oss-review (162 satir)
- /ip-legal:portfolio (284 satir)
- /ip-legal:takedown (236 satir)

---

---

## /ip-legal:cease-desist

---
name: cease-desist
description: >
  İhtarname: marka, telif ya da haksız rekabet ihlaline karşı uygulama duruşunuza
  göre ayarlı ihtarname taslağı hazırlar (--send) ya da size gelen ihtarnameyi
  seçenek notuna çevirir (--receive). Türk hukuku tabanı: SMK m. 7, 29, 149-151,
  154, 156, 159; FSEK m. 66-71, 77; TTK m. 55-56; tebliğ kanalı noter ya da KEP
  (TTK m. 18/3). Göndermeden önce yüksek sesli kapı çalışır.
argument-hint: "<--send | --receive> [bağlam, karşı taraf ya da gelen ihtarnamenin yolu]"
---

# /cease-desist — İhtarname (gönderme / gelen ihtarname triyajı)

- `/ip-legal:cease-desist --send` — duruşa göre ayarlı ihtarname taslağı; teslimden önce kapı.
- `/ip-legal:cease-desist --receive` — gelen ihtarnameyi okur, seçenekleri ve önerisiyle triyaj notu yazar.
- Bayrak yoksa bir kez sor: "İhtarname mi gönderiyoruz (hak ileri sürüyoruz), yoksa gelen bir ihtarnameyi mi değerlendiriyoruz (savunuyoruz)?"

## Talimat

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Yoksa ya da `[PLACEHOLDER]` içeriyorsa dur: "Önce `/ip-legal:cold-start-interview` çalıştırın — ihtarname skill'i uygulama duruşunuza, onay matrisinize ve pratik alanlarınıza dayanır."
2. **Matter:** `## Matter workspaces` → `Enabled` `✗` ise atla. Açık ve aktif matter yoksa sor: "Bu hangi matter için? `/ip-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasındaki `## Matter-specific overrides` uygulama varsayılanının önüne geçer. Çıktılar `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/` altına; `Cross-matter context` `on` değilse başka matter okunmaz.
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

**Pazaryeri paralel yolu:** ihlal bir pazaryerinde ya da sosyal ağdaysa platformun fikri mülkiyet bildirim formu (marka koruma programları, "IP ihlali bildir" formları) çoğu zaman günler içinde sonuç verir; ihtarname ise karşı tarafa stoku eritecek zaman tanır. İkisi birbirini dışlamaz: platform bildirimi + platform dışı (kendi sitesi, toptan, fiziki satış) için ihtarname. İnternetteki telif ihlalinde kanuni yol FSEK ek m. 4/3'tür → `/ip-legal:takedown`. Gönderim öncesi brifte paralel yolun durumu yazılır: yapıldı / sırada / reddedildi (neden).

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

Kesin cevap → `--send` (kapı yeniden çalışır) · müzakere → matter'da oyalayıcı cevap · menfi tespit/hükümsüzlük/iptal → `Outside counsel roster`'a eskale, taslak yok · matter yoksa ve önemliyse `/ip-legal:matter-workspace new <slug>` öner · uy/sessiz kal → kararı `history.md`'ye yaz, delil koruma talimatını teyit et.

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

---

## /ip-legal:clearance

---
name: clearance
description: >
  Marka ön araştırmasının (clearance) ilk elemesi: mutlak ret nedenleri
  (SMK m. 5) ve benzer marka / nispi ret nedenleri (SMK m. 6, m. 7/2) için
  bayrak listesi üretir; tescil edilebilirlik ya da kullanılabilirlik görüşü
  değildir. Yeni marka önerildiğinde, "bu marka boşta mı", "ön araştırma
  yap" denildiğinde ya da tam profesyonel araştırmadan önce karıştırılma
  ihtimali etkenleri tartılırken kullan. Bu skill bir markanın "temiz"
  olduğu sonucuna asla varmaz.
argument-hint: "[önerilen markayı, mal/hizmetleri ve ülkeleri yazın — ya da yalnız markayı, gerisini sorarım]"
---

# /clearance — Marka Ön Araştırması (İlk Eleme)

## BU BİR İLK ELEMEDİR, ÖN ARAŞTIRMA GÖRÜŞÜ DEĞİLDİR

**Her çıktının en üstüne yaz. Çıkarma, yumuşatma.**

> **Bu bir ilk elemedir, marka ön araştırma görüşü değildir.** Görüş; tam profesyonel araştırma (TÜRKPATENT sicili ve Bülten, tescilsiz kullanımlar ve ticaret unvanları, hedef ülke sicilleri, alan adı ve sosyal medya, gerektiğinde şekil ve ambalaj) ile marka vekili ya da avukatın karıştırılma ihtimali değerlendirmesini gerektirir. "Belirgin çakışma yok" sonucu, elemenin bir şey bulmadığı anlamına gelir; markanın boşta olduğu anlamına gelmez. Marka benimsenmeden, başvurusu yapılmadan ya da üzerine yatırım yapılmadan önce yetkili bir uzman değerlendirmelidir.

Çakışmayı küçük göstermek geri dönüşsüz kapıdır: logo basılır, ürün çıkar, başvuru yapılır; sorun altta kalır. Fazla bayrak geri dönüşlü kapıdır; avukat listeyi daraltır. Geri dönüşlü tarafta kal. Profil `firm-profile.md` / ip profili "Karar duruşu" tanınmış marka çakışmasında **her zaman dur** diyorsa ona uy. Profilin `## Outputs` şablonunda "✓ TEMİZ" etiketi olsa bile bu skill "TEMİZ" yazmaz; en olumlu ifade: "aranan kaynaklarda engel bulunmadı — tam araştırma gerekli".

## Destination check

Çıktı karşı tarafa, geniş bir kanala ya da basına gidecekse dur. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD'deki "privilege" gibi geniş bir belge koruması değildir; yalnız hukuk için tam sürüm, geniş kanal için arındırılmış sürüm öner. Kanonik kural: eklenti ayarında `## Shared guardrails → Destination check`.

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/ip-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıyı `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ı okuma.

## Önce profil

`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve `firm-profile.md` oku:
- `## Who's using this` → rol (avukat / avukat değil; üst başlığı ve aşağıdaki kapıyı değiştirir).
- `## IP practice profile` → `Registered in`; `## Enforcement posture` → varsayılan ülkeler.
- `## Available integrations` → hangi arama yapılabilir, yedek yol ne.
- `## Decision posture on subjective legal calls` → bu skill "karıştırılma ihtimali yok" demez.

Ayar `[PLACEHOLDER]` ya da `[Your Company Name]` içeriyorsa:

> Profiliniz henüz kurulmamış. İki seçenek: `/ip-legal:cold-start-interview` (2 dakika) ya da **"provisional"** deyin; genel varsayımlarla (Türkiye — TÜRKPATENT sicili ve tescilsiz önceki haklar, orta risk iştahı, avukat rolü, playbook yok) çalıştırıp her bulguyu `[PROVISIONAL]` diye etiketlerim.

Provisional çalıştırmanın sonuna ekle: "Bu genel varsayımlarla yapılmış bir çalıştırmaydı. `/ip-legal:cold-start-interview` ile pratiğinize göre ayarlayın."

## Girdi

Tek seferde sor:

> 1. **Marka.** Tam yazım; kelime, şekil ya da birleşik; stilizasyon; Latin dışı harf varsa karşılığı (SMK m. 11/1-f).
> 2. **Mal / hizmet.** Müşterinin gördüğü şey: tüketici uygulaması mı, kurumsal API mi, fiziksel ürün mü, hizmet mi?
> 3. **Nis sınıfları.** Biliyorsanız yazın; yoksa ben öneririm, aramadan önce teyit ederiz. Aynı sınıfta olmak benzerlik, farklı sınıfta olmak benzemezlik karinesi değildir (SMK m. 11/4).
> 4. **Ülkeler.** Türkiye / Madrid / AB / Birleşik Krallık / diğer. Söylemezseniz `Registered in`.
> 5. **Piyasadaki görünüm.** Slogan, yan ürün adları, ambalaj, renk.

Tarif muğlaksa ("yapay zekâ aracı", "platform") bir kez daha bastır: sınıflar buna göre değişir.

## Mutlak ret kontrolü (SMK m. 5)

Veritabanı aramasından önce, önceki tescillerden bağımsız olarak markayı öldüren nedenlere bak. TÜRKPATENT başvuruyu m. 5 kapsamında kendiliğinden inceler (m. 16/1). Açık bir sorunu yorumla ortadan kaldırma.

| Bent | Ne zaman işaretle |
|---|---|
| a — m. 4 kapsamında marka olamayan işaret | Ayırt etmeye yaramıyor ya da sicilde açık ve kesin gösterilemiyor (m. 4) |
| b — ayırt edici nitelik yok | Tüketici işareti kaynak göstergesi olarak algılamaz |
| c — tanımlayıcı | Cins, vasıf, kalite, amaç, değer, coğrafi kaynak, zaman ya da başka özelliği münhasıran/esas unsur olarak içeriyor |
| ç — aynı/ayırt edilemeyecek kadar benzer önceki marka | Aynı veya aynı türdeki mal/hizmette tescilli ya da önceki tarihli başvurulu marka var — itiraz beklenmeden resen incelenir (m. 16/1) |
| d — ticarette herkesçe kullanılan | Sektör ya da meslek grubunun ortak adı/işareti |
| e — şekil | Malın doğasından gelen, teknik sonuç için zorunlu ya da mala asli değerini veren şekil |
| f — yanıltıcı | Nitelik, kalite, coğrafi kaynak konusunda halkı yanıltır |
| g, ğ — Paris 6ter, arma, nişan, halka mal olmuş işaret | Devlet amblemi, izinsiz arma/nişan, tarihi-kültürel değer |
| h — dinî değer/sembol | Dinî değer ya da sembol içeriyor |
| ı — kamu düzeni/genel ahlak | Türk hukukunda bu bent yürürlüktedir (ABD'deki *Brunetti/Tam* sonrası durum buraya taşınmaz) |
| i — tescilli coğrafi işaret | Tescilli coğrafi işaretten oluşuyor ya da içeriyor |

Kurtarıcılar: kullanımla kazanılmış ayırt edicilik b, c, d bentlerine göre reddi önler (m. 5/2); önceki marka sahibinin noter onaylı açık muvafakati ç bendine göre reddi önler (m. 5/3). Her bent için ya "sorun görülmedi" ya tek satırlık gerekçeli bayrak yaz; boş "geçti" tablosu üretme.

## Benzer marka kontrolü

Amaç karıştırılmaya yol açabilecek önceki işaretleri **bulmak**; karıştırılma olup olmadığına karar vermek avukatındır.

**Arama kaynakları.**
- **TÜRKPATENT:** ArthurLegal MCP'de TÜRKPATENT aracı **yoktur** (resmî uç çalışmıyor). Aramayı TÜRKPATENT web sitesindeki marka araştırma ekranından elle yap ya da yaptır; Bülten ve sınıf/sahip aramasının pratiği için `references/turkpatent-rehberi.md`. Ekran görüntüsü ya da dışa aktarımı kullanıcıdan iste; sonuçları ondan aktar.
- **Bağlı marka arama bağlayıcısı** (`## Available integrations` — ör. Solve Intelligence ya da başka bir sicil MCP'si) varsa onu çalıştır; her sonucu kaynağına, tarihine, kapsamına (sicil, sınıf, tam/bulanık eşleşme, şekil araması) bağla.
- **Tescilsiz haklar:** ticaret unvanı ve işletme adı (m. 6/3, m. 6/6), alan adı, sosyal medya — ArthurLegal'da bunlar için araç yok; elle arama ya da kullanıcı bilgisi olarak işaretle.
- **Uyuşmazlık geçmişi:** `tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="<marka adı>", kelime_modu="hepsi")`; dönen kararın künyesini birebir kullan.

**Hiç arama yapılamadıysa** çıktıya aynen yaz:

> **Veritabanı araması yapılmadı.** Bu eleme TÜRKPATENT sicilini, Bülteni, ticaret unvanlarını, Madrid/WIPO, EUIPO ya da başka bir sicili ve tescilsiz kullanım kaynaklarını taramadı. Kullanılabilirlik hakkında sonuç için bu kaynaklarda tam araştırma gerekir. Aşağıdaki eleme mutlak ret analizi ile kullanıcının bildirdiği ya da konuşmada geçen işaretlere karşı yapılandırılmış etken analizinden ibarettir.

Sonra devam et; eleme hâlâ yararlıdır, yeter ki kapsamı dürüstçe etiketlensin.

**Her benzer işaret için:** işaret (tam yazım), kaynak (başvuru/tescil no., Bülten, ticaret unvanı, alan adı, karar künyesi), sınıflar ve mal/hizmet listesi, sahip, durum (başvuru / tescilli / reddedilmiş / sona ermiş), varsa kullanım bilgisi. **Sessizce tamamlama:** numara yalnız yaptığın aramadan gelir; kullanıcının söylediğini "kullanıcı bildirdi" diye yaz; bilinmeyen alanı "arama sonucunda yok" diye bırak. Yenilenmeyen marka için not düş: sona ermeden itibaren iki yıl içinde yapılan başvuruya, o sürede kullanılmışsa itiraz edilebilir (m. 6/8).

### Komşu aileler taraması (sonuçtan önce zorunlu)

Yalnız tam ve tama yakın eşleşmeye bakan araştırma, rakibin sizinki alındığı için seçtiği işaretleri kaçırır. 3–5 komşu aile öner, kullanıcıya teyit ettir:

> **Taranacak komşu aileler (teyit edin ya da ekleyin):**
> - Kategori eşanlamlıları (ör. "YILDIZ EV" akıllı ev için: MERKEZ / KÖPRÜ / ÇEKİRDEK / HUB / LINK)
> - Türkçe ↔ İngilizce çeviri eşdeğerleri (YILDIZ / STAR / STELLA)
> - Türkçe karakter ve yazım varyantları (ı/i, ş/s, ç/c, ğ/g, ü/u; "K"/"Q"/"C" sesleri)
> - Kök üzerindeki fonetik ikizler

Türkçe dışı dilin konuşulduğu ülke kapsamdaysa çeviri eşdeğerini, harf çevirisini (Kiril, Arap, Çin/Japon/Kore) ve Latin dışı alfabede tescilli ama okunuşu benzeyen işaretleri ekle. Yapamıyorsan söyle: "Diller arası fonetik ve çeviri eşdeğeri analizi yapılmadı; [ülke] araştırmasına dahil edilmeli." Bağlayıcı yoksa aileleri tam araştırma için "sonraki adım girdisi" olarak listele; sessizce atlama.

## Nispi ret ve karıştırılma etkenleri

Nispi ret nedenleri **itiraz üzerine** işler (m. 6); itiraz, başvurunun Bültende yayımından itibaren iki ay içinde, yazılı ve gerekçeli yapılır ve ücret aynı sürede ödenir (m. 18). İlgili fıkraları bayrakla:
- **6/1** — aynılık/benzerlik + mal/hizmet aynılığı/benzerliği nedeniyle, **ilişkilendirilme ihtimali dahil karıştırılma ihtimali** (tescilden sonraki tecavüz ölçütü de aynıdır: m. 7/2-b).
- **6/3** — tescilsiz marka ya da ticarette kullanılan işaret üzerinde önceki hak.
- **6/4 – 6/5** — tanınmış marka (Paris 6bis) ve Türkiye'de ulaştığı tanınmışlık nedeniyle haksız yarar, itibara zarar, ayırt edici karakteri zedeleme — farklı mal/hizmette de. Bu bayrak çıkarsa sonuç **KIRMIZI**.
- **6/6** — başkasının adı, ticaret unvanı, fotoğrafı, telif ya da başka fikrî hakkı.
- **6/9** — kötüniyet.

Önceki marka Türkiye'de en az beş yıldır tescilliyse itirazda kullanım ispatı istenebilir (m. 19/2); tescilden itibaren beş yıl ciddi kullanılmayan marka iptal edilebilir (m. 9/1, m. 26/1-a). Bunlar "önceki marka zayıf olabilir" bayrağıdır, karar değil.

**Etkenler — her biri bayrak, hüküm değil.** Türk uygulamasında genel izlenim üzerinden değerlendirilen başlıca etkenler (yerleşik uygulama; ayrıntıyı içtihattan doğrula: `tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="karıştırılma ihtimali ilişkilendirilme genel izlenim", kelime_modu="hepsi")`):
- İşaretlerin görsel, işitsel ve kavramsal benzerliği; esas unsur ve ortak unsur; seri/aile markası etkisi.
- Mal/hizmetlerin benzerliği — aynı kaynaktan geldiği düşünülür mü (sınıf karine değildir, m. 11/4).
- İlgili tüketici kesimi ve dikkat düzeyi (anlık alım ↔ kurumsal satın alma).
- Önceki markanın ayırt edicilik derecesi ve tanınmışlığı.
- Satış kanalları ve piyasada birlikte görünme.
- Kötüniyet / bilerek yaklaşma işaretleri; fiilî karıştırma örnekleri (yanlış yönlenen talep, yorum, şikâyet).
- Genişleme ihtimali: önceki sahip yeni markanın alanına girer mi?

Etkenlerin ağırlığı ve "esas unsur" tespiti **tartışmalı — içtihadı kontrol et**.

**Yabancı ülke kapsamdaysa** kuralı ezberden verme; araçla çek:
- AB: `eu_get_document_text(celex="32017R1001")` (AB Marka Tüzüğü 2017/1001; nispi ret ve hak kapsamı maddelerini metinden bul).
- Birleşik Krallık: `uk_get_section(year="1994", number="26", section="5")` (Trade Marks Act 1994 — nispi ret).
- Almanya: `de_norm_getir(kanun="MarkenG", norm="14")`.
- Madrid/WIPO ve listede olmayan ülkeler: "ArthurLegal'da bu kaynak yok; yerel marka vekilinin görüşünü alın." Türk ölçütünü sessizce başka ülkeye uygulama.

## Önerilen sonraki adımlar

- **Mutlak ret bayrağı:** markayı yeniden kurgula ya da kazanılmış ayırt edicilik (m. 5/2) için kullanım delili planla; benimsemeden önce avukat incelemesi.
- **Benzer işaret bulundu:** benimseme, başvuru ve pazarlamadan önce avukat incelemesi; çoğunlukla sıradaki adım tam araştırmadır.
- **Arama yapılmadı:** benimsemeden önce tam araştırma; hangi kaynakların taranacağını say (TÜRKPATENT, Bülten, ticaret unvanı, hedef ülke sicilleri, alan adı).
- **Önceki işaret zayıf/eski/kullanılmıyor görünüyor:** avukata işaretle — kullanım ispatı talebi (m. 19/2), iptal talebi (m. 26), noter onaylı muvafakat (m. 5/3) seçenekleri onun kararıdır.
- **Madrid planı:** Madrid Protokolü kapsamındaki uluslararası başvuru Türkiye bakımından Kuruma doğrudan yapılmış başvuruyla aynı sonucu doğurur (m. 14/1); WIPO tarafı için ArthurLegal'da kaynak yok.
- **Her zaman:** yatırımın büyüklüğüne uygun, yetkili uzmandan tam ön araştırma görüşü; yönlendirme `## IP practice profile` → `Outside counsel roster`.

## Çıktı

Eklenti ayarı `## Outputs` → üst başlığı en üste koy.

```markdown
[ÜST BAŞLIK]

# Marka Ön Araştırması — İlk Eleme (GÖRÜŞ DEĞİLDİR)

**Bu bir ilk elemedir, ön araştırma görüşü değildir.** "Belirgin çakışma yok" sonucu
markanın boşta olduğu anlamına gelmez. Benimseme, başvuru ya da yatırımdan önce
yetkili uzman değerlendirmelidir.

**Eleme sonucu:** [YEŞİL / SARI / KIRMIZI — tek cümle neden]

## Önerilen marka
- **Marka / türü:** [tam yazım; kelime / şekil / birleşik]
- **Mal / hizmet ve Nis sınıfları:** [liste]
- **Ülkeler:** [Türkiye / Madrid / AB / ...]
- **Uygulanan çerçeve:** [SMK m. 5, m. 6 — yabancı ülke için çekilen kaynak]

## Mutlak ret (SMK m. 5)
| Bent | Bayrak | Not |
|---|---|---|

## Benzer işaretler
**Taranan kaynaklar:** [kaynak + tarih — ya da "veritabanı araması yapılmadı"]
**Kapsam:** [sınıflar, ülkeler, tam/bulanık, şekil araması]
**Komşu aileler (kullanıcı teyitli):** [liste; taranmayanlar sonraki adım girdisi]

| İşaret | Kaynak | Sınıf / mal-hizmet | Sahip | Durum | Kullanım | Not |
|---|---|---|---|---|---|---|

## Nispi ret ve karıştırılma etkenleri — avukat için bayraklar
| Etken | Bayrak | Yön (çakışma lehine / aleyhine / karışık) |
|---|---|---|

**Karıştırılma sonucu:** *Bu skill sonuç vermez.* Şunlardan biri:
- "Benzer işaret bulundu; benimsemeden önce avukatın karıştırılma değerlendirmesi gerekli."
- "Aranan kaynaklarda benzer işaret bulunmadı; benimsemeden önce tam araştırma gerekli."
- "Etkenler iki yöne de işliyor; avukat takdiri gerekli."

## Önerilen sonraki adımlar
- [somut adım + yönlendirme]

## Atıf doğrulaması
Her başvuru/tescil numarası, sınıf, tarih ve karar künyesi yetkili kaynaktan açılarak
doğrulanır; açamadığın sonucu atfetme. Atıf: `[ArthurLegal TR — 6769 SMK m. X — GG.AA.YYYY]`,
`[TÜRKPATENT — başvuru/tescil no — GG.AA.YYYY]` (elle arama).
```

## Avukat olmayan kullanıcı kapısı

`## Who's using this` → rol avukat değilse çıktıyla birlikte ver:

> Bu çıktı bir araştırma elemesidir, hukuki görüş değildir. Yalnız buna dayanarak markayı benimsemek, başvurmak ya da yatırım yapmak hukuki sonuç doğurur — bu kontrolden "geçen" bir marka için de tecavüz davası açılabilir. Karar vermeden önce bir avukat ya da TÜRKPATENT siciline kayıtlı bir marka vekili değerlendirmeli (Kurum nezdinde işlemleri sicile kayıtlı marka vekilleri de yapabilir: SMK m. 160/1; yerleşim yeri yurt dışındaki kişiler ancak vekille temsil edilir: m. 160/3).
>
> Uzmana götüreceğiniz bir sayfalık özet: marka, mal/hizmet ve sınıflar, mutlak ret bayrakları, bulunan benzer işaretler, neyin aranıp neyin aranmadığı ve sorulacak üç soru. Avukat için bağlı olduğunuz baroya başvurabilirsiniz.

Analizi saklama; elemeyi özetle birlikte teslim et.

## Çıktı yeri

Matter etkin ve aktifse `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/clearance-<mark-slug>-YYYY-MM-DD.md`; değilse `~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/clearance-<mark-slug>-YYYY-MM-DD.md`. Yolu kullanıcıya göster; matter aktifse `history.md`'ye tek satır ekle. Marka benimsenir ve başvuru sıraya girerse `/ip-legal:portfolio --add` öner.

## Kapanış

`## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu elemeye göre uyarla (tam araştırma iste, markayı yeniden kurgula, eskalasyon, ek bilgi, bekle). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Bir markanın boşta olduğu sonucuna **asla** varmaz.
- TÜRKPATENT sicil aramasının, tescilsiz kullanım araştırmasının, yabancı sicil aramasının ya da izleme (watch) hizmetinin yerini tutmaz.
- Başvuru yapmaz; başvuru kararını besler.
- Tanınmış marka statüsünü belirlemez (m. 6/4-5); yalnız bayrak kaldırır.
- Yabancı ülkenin kuralını ezberden uygulamaz; araçla çeker ya da "kaynak yok" der.
- Çıktıyı müşteriye, karşı tarafa ya da basına aktarmaz.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6769", madde_no=["4","5","6","7","9","11","14","16","18","19"])
tr_mevzuat_madde_getir(number="6769", madde_no=["26","160"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="karıştırılma ihtimali ilişkilendirilme genel izlenim", kelime_modu="hepsi", date_from="2020-01-01")
```

Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: sorguyu genişlet / başka araç / web — `[web — doğrula]` / dur ve avukat teyidine işaretle." Ezberden gelen bilgi `[model bilgisi — doğrula]` diye etiketlenir.

---

## /ip-legal:cold-start-interview

---
name: cold-start-interview
description: >
  İlk kurulum — fikri mülkiyet pratiğinizi öğrenir ve pratik profilini yazar:
  kim kullanıyor (avukat, marka/patent vekili, avukat olmayan), pratik ortamı
  (büro / şirket içi), pratik alanları (marka, patent, telif, ticari sır, açık
  kaynak, tasarım), tescil ve uygulama coğrafyası (TÜRKPATENT, EUIPO, WIPO
  Madrid, EPO), uygulama duruşu ve onay matrisi, eskalasyon, marka izleme.
  Profil yoksa ya da yer tutucu içeriyorsa, --redo ile yeniden görüşmede,
  --check-integrations ile yalnız bağlantı kontrolünde kullan. Yeni kurulumda
  çalışacak tek skill budur.
argument-hint: "[--redo | --full | --check-integrations]"
---

# /cold-start-interview

1. **Durum:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` yoksa görüşmeye başla. `<!-- SETUP PAUSED AT: -->` varsa o bölümden devam öner. `[PLACEHOLDER]` ya da `[Your Company Name]` varsa (duraklatma notu yok) baştan ya da yer tutucuların başladığı yerden devam öner. Doluysa ve `--redo` yoksa sor: "Kurulum yapılmış görünüyor. Yeniden yapalım mı? Üzerine yazmadan önce farkı gösteririm."
2. **Taşıma:** eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/ip-legal/*/CLAUDE.md`) dolu bir profil varsa ve ayar yolunda yoksa ayar yoluna kopyala; neyin taşındığını göster. Bölüm iskeleti `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonundadır.
3. Görüşmeyi yürüt (önce Bölüm 0); paylaşılan belgelerden fiilî duruşları çıkar (Bölüm 3); profili aşağıdaki iskelete göre yaz, avukatın kendi sözleriyle.
4. Portföy dökümü paylaşıldıysa `~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml` dosyasını tohumla; paylaşılmadıysa `/ip-legal:portfolio`'nun sonra dolduracağı bir yer tutucu bırak.
5. Özeti göster: "Duyduklarım bunlar — profil yazıldı. Neyi yanlış anladım?" Deneme öner: "Bir marka adayını `/ip-legal:clearance`'tan geçirelim mi, yoksa portföyde yaklaşan süreleri mi görelim?"

**`--check-integrations`:** görüşme yapma; yalnız bağlantı kontrolünü çalıştır, `## Available integrations` tablosunu yeniden yaz. ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse; denenmemiş bağlantı ⚪ ve tek satır nasıl teyit edilir. `.mcp.json` beyanına bakarak ✓ verme.

**Bölüm ve anahtar adlarını çevirme.** `## Company profile` (`**Practice setting:**`), `## Who's using this` (`**Role:**`), `## Available integrations`, `## IP practice profile` (`Practice area mix:`, `Registered in:`, `Outside counsel roster`, `Seed documents reviewed`), `## Enforcement posture` (`Default posture:`, `When we send a C&D`, `When we send a soft letter first`, `When we just file`, `Approval matrix`, `Automatic escalations`), `## Brand protection`, `## Decision posture on subjective legal calls`, `## Shared guardrails` (`Destination check`), `## Outputs`, `## Matter workspaces` (`Enabled`, `Active matter:`, `Cross-matter context`), `Renewal alerts` adları aynen kalır — diğer skill'ler ve `ip-renewal-watcher` ajanı bunları birebir okur. İçerik Türkçe yazılır.

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/firm-profile.md` varsa oku ve tek satırla teyit et ("Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu?"); teyitte ortak soruları (pratik ortamı, ad, sektör, ne sattığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri) atla. Yoksa ilk kurulan eklenti budur: ortak soruları sor, paketteki `knowledge/firm-profile.md` şablonuna göre yaz ve söyle: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak." Uygulama duruşu, onay matrisi ve izleme ayarları bu eklentiye özeldir.

**Kurulum kapsamı:** çalışma klasörü ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden belge okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

> **`ip-legal`** marka, patent, telif, ticari sır ve açık kaynak yükümlülüklerini yönetenler içindir — marka araştırması, ihlale karşı adım (ihtarname, içerik kaldırma), portföy takibi ve sözleşmelerdeki fikri mülkiyet klozları.
>
> **2 dakika:** rol, pratik ortamı, yargı çevresi ve hangi alanlarda çalıştığınız; uygulama duruşu, onay eşikleri ve marka izleme için makul varsayılanlar. **15 dakika:** gerçek uygulama duruşunuz ve tetikleyicileri, her mektup türü için onay matrisi, izlenen markalar ve izleme hizmeti, açık kaynak politikası, dış avukat/vekil listesi ve portföy kaydı.
>
> Hızlı mı, tam mı? (Sonra `/ip-legal:cold-start-interview --full` ile genişletebilirsiniz.)

**Hızlı yol:** yalnız Bölüm 0 ve Bölüm 1; diğer her alana `[DEFAULT]` yaz. Kapanış: "Tamam, komutları kullanabilirsiniz. Uygulama duruşu, onay eşikleri ve izlemede makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanacak bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--redo`."

**Seçimden sonra** tek paragraf oryantasyon: "Bu eklenti profilinizi (izlenen markalar, onay zinciri, ihtarname tetikleyicileri), yenileme süreli bir portföy kaydını ve matter bazında araştırma ve triyaj notlarını tutar. Cevaplarınızı her skill'in okuduğu düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve açıkça paylaştığınız belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** Portföy dökümü, uygulama rehberi, onay matrisi, marka kullanım rehberi, açık kaynak politikası için önce bağlantı/yapıştırma iste: "Belge yapıştırın, yol verin ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli; mümkünse seçmeli.
- **Uzun cevapta bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste — özellikle uygulama duruşu, onay matrisi, portföy]. Şimdi mi dolduralım, yer tutucu mu kalsın?" Sessiz boşluk bırakma.
- **Duraklat/devam:** "dur", "sonra devam" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /ip-legal:cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte: "Hoş geldiniz, [bölüm]de kalmıştınız. Devam mı, baştan mı?" Cevaplanmışı tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre, eşik söylenirse `tr_mevzuat_madde_getir` ile çek ve karşılaştır; çelişirse: "[X] dediniz; madde metni [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnek: "Bülten itirazı için üç ayımız var" — marka başvurusunun yayımından itibaren itiraz süresi **iki aydır**, yazılı ve gerekçeli yapılır ve ücret aynı süre içinde ödenir (SMK m. 18). Tescil numarası söylenirse: TÜRKPATENT kayıtları ArthurLegal MCP'de yoktur; numarayı kullanıcının TÜRKPATENT dökümünden al, araçla "doğruladım" deme. Ücret ve harç tutarlarını sabit yazma — "güncel tutarı teyit et (dönemsel güncellenir)".

## Bölüm 0 — Kim kullanıyor, ne bağlı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her araştırma notu, ihtarname taslağı ve portföy notundaki üst başlığı belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan** (stajyer avukat, hukuk operasyonu, avukat gözetiminde fikri mülkiyet uzmanı)
> 2. **Marka ve/veya patent vekili (avukat değil)** — TÜRKPATENT sicilinde kayıtlı vekil
> 3. **Avukata erişimi olan, avukat olmayan** (kurucu, marka koruma yöneticisi, mühendislik lideri, açık kaynak sorumlusu)
> 4. **Düzenli avukat erişimi olmayan**

**2 ise** bir kez söyle: "Sicile kayıtlı vekiller TÜRKPATENT nezdinde işlem yapabilir (SMK m. 160/1). Kanun işlerinde ve hukuki meselelerde mütalaa vermek ve yargı organları önünde dava takibi ise baroda yazılı avukatlara aittir (Av.K. m. 35/1). Avukatın sır saklama yükümlülüğü (Av.K. m. 36) avukatlara ilişkindir; bu yüzden TÜRKPATENT işlemleri dışındaki çıktılarınızı (ihtarname, dava stratejisi, sözleşme görüşü) `GİZLİ — AVUKAT SIR SAKLAMA KAPSAMINDA DEĞİL` diye işaretler ve avukata götürülecek araştırma notu olarak çerçevelerim. Kendi meslek kurallarınızdaki gizlilik yükümlülüğünü ayrıca teyit edin."

**3 ya da 4 ise** bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları hüküm değil, avukat incelemesine götürülecek araştırma olarak çerçevelerim — 'ihtarnameyi gönderin' yerine 'taslak bu, iki yöndeki etkenler bunlar, göndermeden önce sorulacaklar bunlar'; (2) hukuki sonucu olan adımlardan önce (ihtarname, içerik kaldırma talebi, marka başvurusu, araştırma sonucuna dayalı karar) avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım." **4 ise** ekle: "Avukat bulmak için ilinizin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür. Tescil işlemleri için TÜRKPATENT'in yayımladığı marka/patent vekili sicili bir başlangıçtır."

### Pratik ortamı

> Hangisi size uyuyor? (Onay matrisinin dilini belirler.)
> - **Hukuk bürosu / fikri mülkiyet bürosu** — onay zinciri, ortak onayı, müvekkil yazılı talimatı.
> - **Şirket içi hukuk** — onay matrisi, hukuk müşaviri/genel müdür, ne zaman iş birimine ya da dış avukata gider.
> - **Tek avukat / küçük büro** — üst kademe yerine "meslektaşa/dış avukata ne zaman danışırsınız".
> - **Kamu / klinik** — denetim modeli ve imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla; kutuya zorlamam, doldurulan, uyarlanan ve boş bırakılan alanları işaretlerim.

Kayıt (`## Company profile` altında `**Practice setting:**`):
- **Büro (her tür):** `## Matter workspaces` → `Enabled: ✓`, `Cross-matter context: off`. Fikri mülkiyet matter'ları uzun ömürlüdür (tescil → yenilemeler). Profile `## Çıkar çatışması` notu yaz: aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat ve kendi düzenlediği senet ya da sözleşmenin hükümsüzlüğünü ileri sürmek durumunda kalan avukat işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Fikri mülkiyette sık doğan hâller: büronun tescil ettirdiği markaya karşı hükümsüzlük talebi, büronun hazırladığı lisans ya da devir sözleşmesine karşı geçersizlik iddiası, iki müvekkilin benzer marka başvurusu. Her yeni matter'da kontrolün yapıldığını sor (Hukuk Bürosu paketinde `/firm-operations:conflict-check`).
- **Şirket içi:** `Enabled: ✗` (tek müvekkil; matter katmanı görünmez).
- **Tek avukat / küçük büro:** onay tablosu iç onay seviyeleri değil danışma tetikleri gösterir.
- **Kamu / klinik:** işi kim gözden geçirir, ne zaman denetleyen avukata çıkar.

### Pratik alanları (sonraki her bölümü budar)

> **Hangi alanlarda çalışıyorsunuz? (Birden fazla seçin)**
> - **Patent / faydalı model** (başvuru takibi / dava / lisans)
> - **Marka** (araştırma / tescil / itiraz / ihlal / marka koruma)
> - **Telif** (lisans / içerik kaldırma / ihlal)
> - **Ticari sır** (koruma programı / ifşa / çalışan çıkışı)
> - **Açık kaynak** (uyum / lisans / politika)
> - **Tasarım** (tescil / taklit)

Her seçim için alt odağı yaz ("patent — başvuru ve lisans, dava yok"). Budama: Bölüm 2'de yalnız ilgili alt sorular; Bölüm 3'te yalnız ilgili belgeler; Bölüm 4 uygulama işi yoksa tümden atlanır (yalnız bir alanda varsa yalnız o alan için sorulur); Bölüm 5'te yalnız o alanların ürettiği bulgu türleri (araştırma çakışması yalnız marka, FTO yalnız patent, copyleft yalnız açık kaynak); Bölüm 6 marka yoksa atlanır. `## IP practice profile` → `Practice area mix:` satırına yaz; uygulanmayan alanlara açık "N/A" — yer tutucu değil. Doğru budanmış 3 dakikalık görüşme, yedi atlanmış yer tutuculu 15 dakikalık görüşmeden değerlidir.

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantıyı karıştırma.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_mevzuat_madde_getir(number="6769", madde_no="7")`. Cevap geldiyse ✓. SMK, FSEK, 5651 maddeleri ve Yargıtay içtihadı buradan doğrulanır.
- **TÜRKPATENT** — ArthurLegal MCP'de **yoktur** (resmî uç çalışmıyor); marka/patent arama, bülten ve sicil **elle** yapılır. Bunun için araç önerme; profile "TÜRKPATENT: manuel — turkpatent.gov.tr" yaz.
- **Yabancı kaynaklar** — AB (`eu_`), Birleşik Krallık (`uk_`), Almanya (`de_`) vb.; yalnız yurt dışı portföy ya da uyuşmazlık varsa; önce `status`.
- **Fikri mülkiyet yönetim sistemi** (Anaqua, CPA Global, Clarivate vb.), **belge deposu** (Drive, SharePoint, Box), **Slack** — deneyebiliyorsan dene, deneyemiyorsan ⚪. KEP için MCP yoktur; KEP adresi varsa `## Company profile`'a not et.

Raporla: ✓ bağlı (denendi) · ⚪ yapılandırılmış, doğrulanmadı — MCP ayarlarından teyit edin · ✗ yok — [özellik] [manuel yönteme] düşer; nasıl bağlanır (Cowork: Ayarlar → Bağlayıcılar; Claude Code: `/mcp`); sonra `--check-integrations`. Örnek: "Yönetim sistemi bağlı değil; portföy `portfolio.yaml`'da tutulur ve elle güncellenir; bağlarsanız renewal-watcher kaydı kendisi çeker." "Hepsine gerek yok; çekirdek özellikler dosya erişimiyle çalışır." ArthurLegal MCP ✗ ise: "Her madde ve karar atfı 'doğrulanmadı' işaretlenir ve UYARI satırı taşır."

**Hemen yaz:** `## Who's using this` ve `## Available integrations` bölümlerini `## Company profile`'dan hemen sonra yaz; `## Outputs` üst başlığını role göre kur.

## Bölüm 1 — İş ve hacim (1-2 dk)

- **Ne iş yapıyorsunuz?** Ne satıyorsunuz, kime, nasıl (doğrudan, bayi, pazaryeri, abonelik)? Web sitesi bağlantısı yeter. Büroysanız: fikri mülkiyet işini en çok yaptığınız müvekkil tipleri.
- **Hacim:** tipik bir ayda masanıza ne kadar iş geliyor (araştırma talebi, ihlal dosyası, portföy işlemi, kloz incelemesi)? Bağlam olarak yaz; kapı değildir — yalnız `ip-renewal-watcher` sıklığını etkiler.

## Bölüm 2 — Tescil ve uygulama coğrafyası (1-2 dk)

> Nerede tescilliyiz, nerede hak arıyoruz? (Araştırma, FTO ve portföy her yargı çevresini buradan okur.)
> - **Markalar:** TÜRKPATENT? EUIPO? WIPO Madrid (hangi ülkeler)? Diğer ulusal tesciller? Yalnız kullanım (tescilsiz)?
> - **Patentler:** TÜRKPATENT? EPO (hangi ülkelerde geçerli kılındı)? PCT ulusal aşama ülkeleri?
> - **Uygulama:** Türkiye'de mi, yurt dışında mı? İzleme hizmetiyle mi, yalnız önünüze gelince mi?

Yalnız seçilen alanların alt sorusunu sor. `## IP practice profile` → `Registered in:` ve `## Enforcement posture` altında uygulama coğrafyası.

**Dış vekil ve avukatlar:** "TÜRKPATENT işlemlerini kim yürütüyor — kendi kayıtlı vekiliniz mi, dış marka/patent vekili mi? Yurt dışı tesciller için yabancı muhabir? Dava için dış avukat?" → `Outside counsel roster` (ad, alan, ülke; yurt dışında yerleşik başvuru sahipleri TÜRKPATENT'te ancak vekille temsil edilir, SMK m. 160/3).

## Bölüm 3 — Pratik belgeleri (1-2 dk)

Duruş sorularından önce elde olanı çıkar:

> Şunlardan elinizde olanı yapıştırın, yol ya da bağlantı verin — yeniden yazdırmam:
> - **Portföy dökümü** (yönetim sistemi ya da tablo: marka/patent/tasarım, ülke, durum, yenileme tarihleri)
> - **Marka kullanım rehberi** (üçüncü kişiler için kurallar, marka kitabı)
> - **İhtarname şablonu**
> - **Uygulama rehberi** (ne zaman ihtarname, ne zaman dava, ne zaman bırak)
> - **Açık kaynak politikası**
> - **Standart sözleşmelerdeki fikri mülkiyet klozları** (lisans alma/verme, devir şablonu)

Her belgeyi oku, duruşları çıkar (onay eşikleri, tetikleyiciler, açık kaynak kabul/yasak listesi, kloz varsayılanları), Bölüm 4-5'te cevaplanmış soruyu tekrar sorma, belirsizi teyit et. `## IP practice profile` → `Seed documents reviewed` altına listele.

## Bölüm 4 — Uygulama duruşu (2-3 dk)

> Bir ihlal gördüğünüzde — taklit marka, kopyalanmış görsel, fazla benzer ürün — nerede durursunuz? (`/ip-legal:infringement-triage` ve `/ip-legal:cease-desist` her sonucu bu duruştan geçirir.)
> - **Aggressive** — erken ihtarname, dava açmaya hazır.
> - **Measured** — önce yumuşak mektup ya da temas; cevap yoksa ya da ticari etki gerçekse yükselt.
> - **Conservative** — yalnız dava muhtemel ve iş birimi uyuşmazlığa onay verdiyse hak ileri sür.

Sonra: **Ne zaman ihtarname?** (karıştırılma ihtimali + ticari zarar mı, tescilli markanın her kullanımı mı, platform bildirimi işe yaramayınca mı — kendi sözlerinizle) · **Ne zaman önce yumuşak mektup?** (bireyler, küçük ticari kullanıcılar, sempatik karşı taraflar?) · **Ne zaman doğrudan dava/tedbir?** (tekrarlayan ihlal, savaşmaya hazır karşı taraf, süre işliyor — ör. ceza şikâyetinde altı ay)

**Kim onaylar?** (`/ip-legal:cease-desist` ve `/ip-legal:takedown` taslağı adı geçen onaylayana götürür ve onay gelmeden hiçbir yere gitmez.)
> - **İçerik kaldırma (olağan)** — platform bildirimi, FSEK ek m. 4 başvurusu: kimde? (`DMCA takedown (ordinary)` satırı — ad çevrilmez)
> - **Yumuşak mektup** (`Soft letter`)
> - **İhtarname** (`Cease-and-desist`)
> - **Dava açma / ihtiyati tedbir** (`Filing suit`) — hukuk müşaviri mi, genel müdür mü, iş sponsoru mu; büroda yönetici ortak + müvekkilin yazılı talimatı mı?

> Hangi durum, varsayılan onaylayandan bağımsız **otomatik eskalasyon**? (Tipik: karşı taraf mevcut müşteri ya da ortak; karşı taraf bizden büyük; patent içeriyor; basına yansıyabilir; savcılık başvurusu ya da ceza şikâyeti.)

Son vurgu: "**İhtarname bir uyuşmazlık başlatır.** Bu yüzden bu eklentideki en önemli ayar budur. Her mektup türü için onaylayanı teyit edin."

## Bölüm 5 — Eskalasyon (1-2 dk)

> Araştırma gerçek bir çakışma bulduğunda, FTO engelleyici bir patent çıkardığında ya da açık kaynak incelemesi copyleft yükümlülüğü bulduğunda — notu kim alır, ne yapılacağına kim karar verir?
> - **Marka çakışması:** başvuru mu, ad değişikliği mi, muvafakat/birlikte var olma anlaşması mı?
> - **FTO engeli:** mühendislik mi, ürün mü, hukuk müşaviri mi?
> - **Copyleft:** bağımlılığı çıkarma, ürünü açma ya da mimariyi değiştirme kararı kimde?

Bugün nasıl eskale ediliyor (Slack, e-posta, bilet, toplantı), beklenen dönüş süresi? `## Enforcement posture` altına eskalasyon yönlendirmesi olarak yaz.

## Bölüm 6 — Marka koruma (yalnız marka seçildiyse)

> - **İzlenen markalar:** belirli markaları üçüncü kişi kullanımına karşı aktif izliyor musunuz? Liste ya da "yok — yalnız önümüze gelince".
> - **İzleme kaynakları:** TÜRKPATENT Resmî Marka Bülteni (elle ya da vekil üzerinden), izleme hizmeti (Corsearch, CompuMark vb.), EUIPO, pazaryeri ve alan adı taraması?
> - **Sıklık:** haftalık / aylık / üç aylık / talep üzerine? Bülten izlemesinde yayıma itiraz süresi yayımdan itibaren **iki aydır** (SMK m. 18/1) — aylıktan seyrek sıklık itiraz penceresini kaçırabilir; profile not düş.

`## Brand protection` altına yaz. Portföy uyarılarının gideceği kanal → `Renewal alerts`.

## Profili yazma

Yazmadan önce paylaşılan belgeleri yeniden oku; hafızaya güvenme. Profil avukatın okuyup düzenleyeceği bir belgedir, YAML değil (portföy kaydı YAML'dır; profil değil). Rol ve pratik ortamına göre tek varyant yaz; karıştırma. İskelet (başlıklar aynen, içerik Türkçe):

```markdown
# IP Practice Profile
*[TARİH] tarihinde kurulum görüşmesiyle yazıldı. Doğrudan düzenleyin — eklentideki her skill önce bunu okur.*
## Company profile
[Müvekkil] — [şirket türü / büro]. **Practice setting:** [büro / şirket içi / tek avukat / kamu / diğer]
[ne iş yapıyor; aylık hacim]
## Who's using this
**Role:** [Avukat / Marka-patent vekili (avukat değil) / Avukata erişimi olan avukat olmayan / Avukat erişimi olmayan]
**Attorney contact:** [isim / ekip / dış büro / —]
## Available integrations
| Integration | Status | Fallback if unavailable |
|---|---|---|
| ArthurLegal MCP (`tr_`) | [✓/⚪/✗] | Atıflar "doğrulanmadı" + UYARI satırı |
| TÜRKPATENT | manuel | turkpatent.gov.tr — elle arama, kaynak ve tarih damgası |
| IP yönetim sistemi | [✓/⚪/✗] | `portfolio.yaml` elle |
| Belge deposu | [✓/⚪/✗] | Her işte dosya yüklenir |
| Slack | [✓/⚪/✗] | Uyarılar sohbette |
## IP practice profile
**Practice area mix:** [alan — alt odak; uygulanmayanlara N/A]
**Registered in:** [TÜRKPATENT / EUIPO / WIPO Madrid: ülkeler / EPO / diğer]
**Outside counsel roster:** [ad — alan — ülke — rol (marka vekili / patent vekili / dava avukatı / yabancı muhabir)]
**OSS policy:** [yol / yok]
**Seed documents reviewed:** [liste]
## Enforcement posture
**Default posture:** [Aggressive / Measured / Conservative]
**When we send a C&D:** … **When we send a soft letter first:** … **When we just file:** …
**Enforcement geography:** [Türkiye / yurt dışı; izleme ya da reaktif]
**Approval matrix**
| Action | Approver | Notes |
|---|---|---|
| DMCA takedown (ordinary) | [ ] | Türkiye'de: FSEK ek m. 4 başvurusu, platform bildirimi; yabancı DMCA bildirimi |
| Soft letter | [ ] | |
| Cease-and-desist | [ ] | |
| Filing suit | [ ] | dava, ihtiyati tedbir, savcılık başvurusu |
**Automatic escalations:** [liste]
**Escalation routing:** [marka çakışması → …; FTO engeli → …; copyleft → …; kanal ve dönüş süresi]
## Brand protection
**Watched marks:** … **Watch jurisdictions:** … **Watch service:** … **Monitoring cadence:** …
**Renewal alerts:** [kanal / e-posta listesi]
## Çıkar çatışması
[Yalnız büroda — Av. K. m. 38 notu ve kontrol pratiği]
## Decision posture on subjective legal calls
Belirsiz öznel hukuki değerlendirmede (karıştırılma ihtimali, eser benzerliği, kanuni istisna, copyleft tetikleyicisi, iddianın savunulabilirliği) sessizce "sorun yok" denmez; avukata işaretlenir, iki yöndeki etkenler gösterilir.
## Shared guardrails
**Destination check:** Çıktı dar hukuk çevresi dışına (karşı taraf, geniş kanal, basın, sigortacı) gidecekse dur; tam sürüm yalnız hukuka, arındırılmış sürüm geniş kanala. Avukatın sır saklama yükümlülüğü (Av.K. m. 36) belgeyi koruyan genel bir kalkan değildir.
## Outputs
- Rol avukatsa: `GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ`
- Rol marka/patent vekiliyse: TÜRKPATENT işlemleri için `GİZLİ — DAHİLİ`; diğer işler için `GİZLİ — AVUKAT SIR SAKLAMA KAPSAMINDA DEĞİL — AVUKATA GÖTÜRÜN`
- Rol avukat değilse: `ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — İŞLEM ÖNCESİ AVUKATLA GÖZDEN GEÇİRİN`
Karşı tarafa giden ihtarname, kaldırma talebi ve itirazdan başlık çıkarılır. Başlık tek başına koruma yaratmaz.
**Next-steps decision tree:** taslağı yaz / eskale et / olgu topla / bekle-izle / başka bir şey.
**Dashboard offer for data-heavy outputs:** ~10 kalemi aşan portföy ve OSS çıktılarında pano öner.
## Matter workspaces
Enabled: [✓ / ✗]
Active matter: none — practice-level context only
Cross-matter context: off
```

Portföy dökümü varsa `portfolio.yaml`'ı tohumla (her kayıt: tür, ad/başlık, ülke, tescil/başvuru no, durum, sonraki işlem tarihi — kaynak: kullanıcının dökümü; TÜRKPATENT'ten araçla çekilmedi).

## Yazdıktan sonra

> **Neler yapabildiğimi görmek ister misiniz?** Marka adayı araştırması (`/ip-legal:clearance`), ihlal triyajı — platform bildirimi mi, ihtarname mi, izleme mi (`/ip-legal:infringement-triage`), FTO ön değerlendirmesi (`/ip-legal:fto-triage`), ihtarname ya da içerik kaldırma taslağı (`/ip-legal:cease-desist`, `/ip-legal:takedown`), açık kaynak uyumu (`/ip-legal:oss-review`), sözleşmedeki fikri mülkiyet klozları (`/ip-legal:ip-clause-review`), portföy yenileme durumu (`/ip-legal:portfolio`). **Önerim:** `/ip-legal:portfolio` — eklentideki kaydın gerçek portföyle örtüşüp örtüşmediğini en hızlı gösterir.

Kullanıcı somut bir iş söylediyse listeyi atla. Acıya göre öner: uygulama yavaşsa ihtarname taslağı; yenilemeler gözden kaçıyorsa önümüzdeki 90 gün; açık kaynak dağınıksa bir depo taraması. ArthurLegal MCP bağlı değilse: "Bağlarsanız madde atıflarını canlı doğrularım; bağlanmadıkça her atıf doğrulanmadı işareti taşır."

**Kapanış:**
> "Tamam. Profiliniz `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` dosyasında — düz metin, doğrudan düzenleyebilirsiniz. Tam yeniden görüşme `--redo`, bağlantı kontrolü `--check-integrations`, tek değişiklik `/ip-legal:customize`. En sık ayarlananlar: **uygulama duruşu** (gerçek tetikleyicinin yazılandan farklı olduğu çıkar), **tescil coğrafyası** (yeni başvuru, düşen tescil) ve **izlenen markalar**.
>
> **Profiliniz öğrenir.** Bir çıktı yanlış gelirse genellikle ayarlanacak bir duruştur; çıktı hangisi olduğunu söyler. `ip-renewal-watcher` ajanı portföy kaydını sıklığınıza göre izler; kaçan bir uyarı, kapatılacak bir kayıt boşluğudur. On dakikalık kurulum çalışan bir profil verir; bir aylık kullanım sizin yazmış gibi okunan bir profil."

## Üslup ve kaçınılacaklar

Sıcak, meraklı, ödevini yapmış yeni bir meslektaş gibi; form gibi değil. "Lütfen sağlayın" değil "durum ne"; "ayarlarınızı yapılandırın" değil "pratiğiniz nasıl işliyor". Kısa cevapta bir kez takip sorusu sor ("Aggressive — ilk görüşte ihtarname mi, kısa bir temastan sonra mı?"), sorgulamaya dönüştürme. Genel cevapta tetikleyiciyi iste: "Instagram'da ilgisiz mallarda neredeyse aynı markayı kullanan bir hesap gördünüz — ne yaparsınız?" Profile YAML yazma; belgeleri atlama (görüşme ne sanıldığını, belgeler gerçeği gösterir); var olmayan skill vaat etme; profil doluysa her oturumda çalıştırma. **Patent istemi yazma ve resmî görüş (mütalaa) verme** bu eklentinin dışındadır — istenirse patent vekiline ya da avukata yönlendir.

---

## /ip-legal:customize

---
name: customize
description: >
  Fikri mülkiyet pratik profilinde tek bir şeyi, kurulum görüşmesini baştan
  yapmadan değiştirir: risk iştahı, eskalasyon kişileri, dış avukat ve vekil
  listesi, portföy kapsamı, marka izleme, uygulama duruşu ve onay matrisi,
  araştırma eşikleri, açık kaynak kuralları, matter klasörleri. Kullanıcı
  "şunu değiştir", "profilimi güncelle", "ayarı değiştir" ya da "customize"
  dediğinde kullan.
argument-hint: "[bölüm adı ya da değiştirmek istediğiniz şey]"
---

# /customize

## Ne yapar

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve ortak `~/.claude/plugins/config/claude-for-legal/firm-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa: "Kurulum henüz yapılmamış. Önce `/ip-legal:cold-start-interview` çalıştırın — customize var olan profili ayarlamak içindir."

2. **Haritayı göster** — her grup için güncel değerin tek satırlık özeti:
   - **Şirket / kimlik** — ad, sektör, ülkeler, pratik ortamı *(ortak profil — tüm eklentilere yansır)*
   - **IP practice profile** — kapsamdaki alanlar (patent, marka, telif, ticari sır, açık kaynak, tasarım) ve alt odak; `Registered in:`; `Outside counsel roster` (dış avukat, marka/patent vekili, yabancı muhabir)
   - **Risk iştahı** — temkinli / orta / atak; araştırma eşiklerine, FTO değerlendirmesine ve ihtarname eskalasyonuna etkisi
   - **Kişiler** — fikri mülkiyet sorumlusu, alan bazında dış büro ve vekiller, uygulama eskalasyon zinciri, buluş değerlendirme kurulu
   - **Portföy** — patent aileleri, marka sınıfları, ana markalar, tescil ülkeleri; `portfolio.yaml` ve yenileme uyarı kanalı (`Renewal alerts`)
   - **Brand protection** — izlenen markalar, izleme kaynakları (TÜRKPATENT Bülteni elle/vekil, izleme hizmeti), sıklık; pazaryeri ve alan adı tutumu
   - **Enforcement posture** — `Default posture:`, ne zaman yumuşak mektup / ihtarname / dava; `Approval matrix` satırları (`DMCA takedown (ordinary)`, `Soft letter`, `Cease-and-desist`, `Filing suit`), `Automatic escalations`
   - **Araştırma ve FTO** — arama kaynakları, güven eşikleri, FTO notu biçimi
   - **OSS review** — kabul / inceleme / yasak lisans katmanları, gönderimi durduran lisanslar, yeni bağımlılık inceleme sıklığı, `OSS policy` yolu
   - **İş akışı** — matter klasörleri, portföy kaydı, buluş bildirim formu
   - **Entegrasyonlar** — ArthurLegal MCP, IP yönetim sistemi, belge deposu, Slack; TÜRKPATENT (her zaman manuel)

3. **Sor:** "Neyi ayarlamak istersiniz? Bir bölüm seçin ya da değişikliği kendi sözlerinizle anlatın."

4. **Değiştir:** güncel değeri göster, yenisini al, aşağı akış etkisini söyle, onay al, yaz. Örnekler:
   - *İzlemeye yeni bir sınıf:* "`/ip-legal:portfolio` izleme raporlarına bu sınıfı ekler; `/ip-legal:infringement-triage` bu sınıftaki bulguları buna göre yönlendirir."
   - *Duruş atak → ölçülü:* "`/ip-legal:cease-desist` belirsiz vakalarda ilk seçenek olarak yumuşak mektup taslağı sunar, doğrudan ihtarnameye gitmez."
   - *Yeni yasak açık kaynak lisansı:* "`/ip-legal:oss-review` bu lisansı içeren incelemeyi uyarı değil, gönderimi durduran bulgu olarak verir."
   - *İzleme sıklığı aylıktan üç aylığa:* "Bülten yayımına itiraz süresi yayımdan itibaren iki aydır (SMK m. 18/1); üç aylık izleme itiraz penceresini kaçırabilir. Yine de değiştireyim mi?"

   Kullanıcı yeni bir kanun maddesi, süre ya da eşik söylerse yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; çelişki varsa göster ve hangisinin gireceğini sor. TÜRKPATENT ücretleri ve harçlar gibi dönemsel tutarları sabit yazma.

5. **Ortak profil değişikliği** (ad, sektör, ülkeler, pratik ortamı): `firm-profile.md` dosyasına yaz ve söyle: "Bu değişiklik tüm eklentileri etkiler — yargı çevresi ayak izinizi okuyan her eklenti artık [yeni değer]'i görür." Pratik ortamı büro ↔ şirket içi değişiyorsa `## Matter workspaces` → `Enabled` değerinin ve `## Çıkar çatışması` notunun da değişmesi gerektiğini hatırlat.

6. **Kapat:** "Tamam, bir sonraki çıktı değişikliği yansıtır. Başka bir şey var mı? `/ip-legal:customize`'ı istediğiniz zaman çalıştırabilirsiniz."

## Korkuluklar

- **Bölüm silme.** Bir alan kapsamdan çıkarılmak istenirse `[Not currently in scope]` yaz ve neyin devre dışı kaldığını anlat.
- **İç tutarsızlığı işaretle** — ör. marka kapsam dışı ama marka izleme hizmeti tanımlı; atak duruş ama "her ihtarname dış avukata"; rol "marka/patent vekili" ama çıktı başlığı Av.K. m. 36 kapsamı diyor. Gerilimi göster, hangisini istediğini sor.
- **Korkuluk zayıflatmayı işaretle.** `[review]` bayrağı, kaynak etiketleri, doğrulanmamış atıflardaki `[doğrula]` etiketi ve UYARI satırı, `/ip-legal:clearance` güven derecesi yük taşır; kapatılmak istenirse neyi koruduğunu anlat ve bedeli anladığını teyit ettir.
- **Bölüm ve anahtar adlarını çevirme** — diğer skill'ler `## Enforcement posture`, `Approval matrix`, `## IP practice profile`, `Registered in:` gibi adları birebir okur.
- **Tek seferde tek değişiklik** — görüşmeyi baştan sorma.

---

## /ip-legal:fto-triage

---
name: fto-triage
description: >
  Kullanım serbestisi (freedom-to-operate, FTO) elemesi — engelleyebilecek
  patent ve faydalı modellere yapılandırılmış ilk bakış; FTO görüşü değildir.
  Türk hukuku tabanı: patent hakkının kapsamı ve sınırları (SMK m. 85),
  dolaylı kullanım (m. 86), önceki kullanım hakkı (m. 87), istemlerle
  belirlenen koruma kapsamı ve eşdeğerlik (m. 89), tecavüz fiilleri (m. 141).
  Bir ürün, usul ya da özellik engelleyici patent açısından incelenirken,
  "lansmanı durduracak bir şey var mı" sorulduğunda ya da patent vekili
  incelemesinden önce en makul patentlere karşı istem tablosu taslağı
  gerektiğinde kullan. Bu skill bir ürünün piyasaya çıkmaya hazır olduğu
  sonucuna asla varmaz.
argument-hint: "[ürünü / usulü / özelliği ve ülkeleri yazın — ya da yalnız konuyu, gerisini sorarım]"
---

# /fto-triage — Kullanım Serbestisi Elemesi

## BU BİR FTO GÖRÜŞÜ DEĞİLDİR

**Her çıktının en üstüne yaz. Çıkarma, yumuşatma, okuyucunun atlamasına izin verme.**

> **Bu bir kullanım serbestisi (FTO) görüşü değildir.** FTO görüşü; kapsamlı araştırma, istemlerin tam yorumu ve her ilgili patentin her istemine karşı unsur unsur tecavüz analizi gerektiren, genellikle patent vekili ya da bu alanda uzman avukatın verdiği mesleki bir değerlendirmedir. Bu eleme, ortada ne olabileceğine yapılandırılmış bir ilk bakıştır. "Belirgin engelleyici patent yok" sonucu, elemenin bir şey bulmadığı anlamına gelir; ürünün serbest olduğu anlamına gelmez. Üretme, kullanma, satma, ithal etme kararı resmî bir FTO çalışması ve uzman görüşüyle verilen bir iş kararıdır.

Engelleyici patenti gözden kaçırmak geri dönüşsüz kapıdır: ürün çıkar, bir yıl sonra ihtiyati tedbir ve elkoyma (m. 159/2) gelir. Fazla bayrak geri dönüşlü kapıdır. Her zaman geri dönüşlü tarafta kal.

### "Bilme" notu (ABD'deki "willfulness" yerine)

Türk hukukunda ABD'deki ayrıcalıklı FTO görüşü koruması yoktur: avukatın sır saklama yükümlülüğü (Av. K. m. 36) belgeyi müvekkilin elinde korumaz. Bu eleme belirli patentleri ortaya çıkarır; bundan sonra şirket o patentleri biliyor sayılabilir. Bu, satma/dağıtma/ithal fiillerinde ve usul patentinde aranan "bildiği ya da bilmesi gerektiği" ölçütü (m. 141/1-b, c) ve yayımdan önceki dönem için kötüniyet tespiti (m. 141/3) bakımından önemlidir. SMK m. 149-151'de ABD'deki gibi kasta bağlı tazminat katlaması yer almaz; ancak yoksun kalınan kazançta hakkaniyete uygun ek pay (m. 151/4) ve itibar tazminatı (m. 150/2) vardır. Bu yüzden çıktıyı dar çevrede tut; eleme sonrası yolu uzman yazılı olarak belirlesin.

## Destination check

Çıktı hukuk dışına, karşı tarafa ya da geniş kanala gidecekse dur; yalnız hukuk için tam sürüm, iş birimi için patent numarası içermeyen arındırılmış sürüm öner. Kanonik kural: `## Shared guardrails → Destination check`.

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/ip-legal:matter-workspace switch <slug>` ya da `practice-level`." `matter.md`'yi yükle; çıktıyı matter klasörüne yaz; `Cross-matter context` `on` değilse başka matter'ı okuma. FTO işleri sıklıkla **clean-team** ya da **heightened** gizlilik işaretiyle açılır; `matter.md`'deki işarete uy.

## Önce profil

`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve `firm-profile.md`: `## Who's using this` (rol), `## IP practice profile` → `Registered in` ve `Outside counsel roster` (patent vekili/dış uzman), `## Enforcement posture`, `## Available integrations` (patent arama bağlayıcısı var mı), `## Decision posture on subjective legal calls` (bu skill "tecavüz yok" demez).

Ayar `[PLACEHOLDER]` içeriyorsa: `/ip-legal:cold-start-interview` ya da **"provisional"** — genel varsayımlar (Türkiye, orta risk, avukat rolü, playbook yok), her bulguda `[PROVISIONAL]` etiketi ve sonda "profilinizi kurun" notu.

## Girdi

Tek seferde sor:

> 1. **Ürün, usul ya da özellik.** Ne üretilecek, kullanılacak, satılacak, ithal edilecek? Pazarlama dilini değil teknik özü yazın.
> 2. **Teknik ayrıntı.** Mimari şema, teknik şartname, ürün sayfası, kod — ne kadar ayrıntı, o kadar gerçek eleme.
> 3. **Ülkeler.** Nerede üretilecek, satılacak, ithal edilecek? Türkiye'de üretme, satma, kullanma, ithal ve bu amaçlarla elde bulundurma ayrı ayrı önlenebilir fiillerdir (m. 85/2). Söylemezseniz Türkiye.
> 4. **Bilinen patentler.** Rakip portföyü, standart (SEP) havuzu, ihtarname, mühendisin duyduğu bir patent?
> 5. **Zamanlama.** Lansmana aylar varsa tasarım değişikliği masadadır; ürün zaten satılıyorsa riski sınırlama modundayız.

Tarif muğlaksa bir kez daha bastır: "Ne yapıyor, nasıl yapıyor, yeni olduğunu düşündüğünüz parça ne? İstemler o seviyede yaşar."

## Kapsam — patent ve faydalı model

- **Patent ve faydalı model** bu skill'in konusudur. Faydalı model araştırma raporu ve itiraz/görüş değerlendirmesiyle verilir (m. 143/5-10); verilmesi Kurumun geçerlilik garantisi değildir (m. 143/13) ve verildikten sonra yalnız mahkemeden hükümsüzlük istenebilir (m. 143/11) — tehdit ve geçersizlik savunması açısından ayrı işaretle. Patent hükümleri, çelişmedikçe faydalı modele de uygulanır (m. 145/1).
- **Tasarım** (tescilli ya da tescilsiz) farklı testtir — istem tablosu çizme; `/ip-legal:infringement-triage` tasarım moduna ve tasarım uzmanına yönlendir, ayrı iş akışı olarak işaretle.
- **Görünüm riski** varsa paralel kanalları işaretle: üç boyutlu marka (m. 4 — malın/ambalajın biçimi), tescilsiz tasarım (m. 55/4) ve karıştırılmaya yol açan önlemler nedeniyle haksız rekabet (TTK m. 55/1-a-4).

## Araştırma

**ArthurLegal MCP'de patent veritabanı ve TÜRKPATENT aracı yoktur.** Seçenekler:
- `## Available integrations` içinde patent arama bağlayıcısı (ör. Solve Intelligence) bağlıysa çalıştır; tarih, sorgu, ülkeler ve tarih aralığını not et.
- Bağlı değilse elle: TÜRKPATENT web sitesindeki patent araştırma ekranı; Türkiye'yi kapsayan Avrupa ve PCT başvuruları için `references/turkpatent-rehberi.md`'de sayılan dış veri tabanları (Espacenet, PATENTSCOPE — ArthurLegal aracı değildir). Türkiye'yi belirleyen Avrupa patentlerinin Türkiye'deki geçerlilik durumunu TÜRKPATENT sicilinden elle kontrol et.
- Hiçbiri yoksa aynen yaz:

> **Patent veritabanı araması yapılmadı.** Bu eleme TÜRKPATENT sicilini, Avrupa/PCT yayınlarını ya da başka bir patent külliyatını taramadı. Kapsamdaki ülkelerde yapılandırılmış araştırma olmadan bu eleme lansman kararına dayanak olamaz. Aşağıdaki analiz kullanıcının adını verdiği ya da konuşmada geçen patent ve başvurularla sınırlıdır.

**Ek sinyaller (patent bulgusu değildir):** rakip başvuruları, ilgili standartlara SEP beyanları, teknoloji alanındaki dava geçmişi — `tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="patent tecavüz <teknoloji terimi>", kelime_modu="hepsi")`. Her biri daha dikkatli bakma nedenidir; "sinyal" diye ayrı başlıkta göster.

## Her ilgili patent için

- Numara (başvuru no. farklıysa o da), ülke/ofis, başlık, sahip, buluşu yapanlar
- Başvuru ve varsa rüçhan tarihi (patent ve faydalı model rüçhanı ilk başvurudan 12 ay: m. 93/1), veriliş tarihi
- **Koruma bitişi:** başvuru tarihinden patentte 20, faydalı modelde 10 yıl; uzatılamaz (m. 101/1)
- **Yürürlük:** yıllık ücretler başvurudan itibaren ikinci yılın sonunda ve her yıl vadesinde ödenir; vadede ödenmezse ek ücretle altı ay; o da geçerse hak vade tarihi itibarıyla sona erer, ama bildirimden itibaren iki ay içinde telafi ücretiyle yeniden geçerlilik kazanabilir (m. 101/2-4; m. 140/1-c). "Sona ermiş" görünen patenti bu pencere kapanmadan ölü sayma; yeniden geçerlilikte üçüncü kişilerin kazanılmış hakları saklıdır (m. 101/5).
- Bağımsız ve bağımlı istem sayısı; verildiği hâliyle bağımsız istemler ve itiraz/hükümsüzlük sonucu değişmiş hâli
- İlgili işlemler: verilme kararının yayımından itibaren 6 ay içinde üçüncü kişi itirazı (m. 99/1), hükümsüzlük davaları, Yargıtay kayıtları
- Dosya geçmişi: başvuru sahibinin kapsamı daraltan beyanları (m. 89/6)
- Yayımlanmış ama verilmemiş başvuru: yayımdan itibaren geçici koruma (m. 97/4); mahkeme m. 99/3 ya da /7 uyarınca yayımdan önce iddiaların geçerliliğine karar veremez (m. 141/4)

**Sessizce tamamlama.** Patent numarası, istem unsuru ya da bitiş tarihi uydurma. Yıllık ücret durumu doğrulanmadıysa yaz: "yıllık ücret durumu aramadan doğrulanmadı — TÜRKPATENT sicilinden teyit edin."

## İstem tablosu — ilk geçiş

Elemenin özü. Ürüne en yakın okunan 2–5 patenti seç; her bağımsız istemi unsur unsur yürü.

| İstem unsuru | Ürün bunu uyguluyor mu? | Dayanak |
|---|---|---|
| "[giriş kısmı]" | [evet / hayır / olabilir / yoruma bağlı] | [ürünün neresi karşılıyor; ne karşılamıyor; ne belirsiz] |
| "[unsur 1]" | | |

**Türk hukukunda tablonun kuralları:**
- **Kapsam istemlerle belirlenir;** tarifname ve resimler yorumda kullanılır (m. 89/1). İstemler kelimelerin anlamıyla sınırlı okunmaz, ama istemde talep edilmeyen özelliklere de genişletilemez (m. 89/2); örneklerle sınırlı yorumlanmaz (m. 89/7).
- **Önce lafzi okuma:** istemin her unsuru üründe var mı? Bir unsur yoksa o istem bakımından lafzi tecavüz bayrağı düşer. Unsurların tamamının aranması uygulamada yerleşik ölçüttür; sınır hâllerde **tartışmalı — içtihadı kontrol et**.
- **Eşdeğerlik ayrı geçiştir:** tecavüz iddiası tarihinde istem unsuruna eşdeğer unsurlar dikkate alınır; esas itibarıyla aynı işlevi, aynı şekilde görüp aynı sonucu doğuran unsur genel olarak eşdeğerdir (m. 89/5). "Hayır" çıkan her unsur için eşdeğerlik okumasını ayrıca işaretle; başvuru sahibinin beyanları (m. 89/6) eşdeğerliği daraltabilir — karar avukatındır.
- **İstem yorumu avukatın işidir.** Bir terim dar ya da geniş yorumlanabiliyor ve sonuç değişiyorsa iki yorumu da yaz; birini sessizce seçme.
- **Dolaylı kullanım (m. 86):** buluşun esasını oluşturan unsur ya da araçların yetkisiz kişilere verilmesi, bilme şartıyla; piyasada her zaman bulunan ürünlerde teşvik yoksa uygulanmaz (m. 86/2). Yalnız bayrak.
- **Usul patenti:** ürün yeniyse, izinsiz üretilen aynı ürünün patentli usulle elde edildiği kabul edilir ve aksini davalı ispatlar (m. 141/2) — ispat yükü bayrağı.
- **Bölünmüş tecavüz** (fiillerin farklı kişilerce yapılması): Türk hukukunda açık düzenleme yok — **tartışmalı**, yalnız bayrak.

**Yabancı ülke kapsamdaysa** Türk tablosunu oraya taşıma; kuralı araçla çek:
- Almanya: `de_norm_getir(kanun="PatG", norm="9")`; kapsam ve dolaylı kullanım normlarını `de_gesetz_ara` ile bul.
- Birleşik Krallık: `uk_get_section(year="1977", number="37", section="60")` (Patents Act 1977 — tecavüz ve istisnalar).
- AB üniter patent: `eu_get_document_text(celex="32012R1257")`. Avrupa Patent Sözleşmesi (EPC), Birleşik Patent Mahkemesi Anlaşması, ABD, Çin, Japonya patent hukuku: "ArthurLegal'da doğrulanmış kaynak yok; ilgili ülkenin patent vekilinden görüş alın."

**Karar duruşu:** bu skill "tecavüz yok" demez. Şunlardan biri:
- "Ürün İstem X'in her unsurunu lafzen uyguluyor; ilerlemeden önce uzman incelemesi gerekli."
- "Bir ya da daha çok unsur açıkça mevcut değil; lafzi tecavüz ve eşdeğerlik için uzman incelemesi gerekli."
- "[Y] unsurunda istem yorumu belirleyici; ilerlemeden önce uzman yorumu gerekli."

## Sınırlar ve savunmalar (bayrak — karar değil)

- **Hakkın kapsamı dışındaki fiiller (m. 85/3):** sınai/ticari amaç taşımayan özel fiiller; deneme amaçlı fiiller; ilaç ruhsatı için gerekli test ve deneyler; eczanede reçeteye göre seri üretim olmadan hazırlama; geçici olarak Türkiye'de bulunan taşıtlar.
- **Önceki kullanım hakkı (m. 87):** başvuru tarihinde ya da önce buluşu ülke içinde iyiniyetle kullanan ya da ciddi ve gerçek tedbir alan; işletmenin makul ihtiyaçlarıyla sınırlı, lisansla genişletilemez, ancak işletmeyle devredilir. Kullanım tarihine ilişkin delil var mı?
- **Hakkın tüketilmesi (m. 152):** hak sahibi ya da izniyle piyasaya sunulan ürünlerle ilgili fiiller kapsam dışıdır. İlk piyasaya sunmanın yurt dışında olmasının etkisi **tartışmalı — içtihadı kontrol et**.
- **Geçersizlik:** hükümsüzlük nedenleri (m. 138/1 — patentlenebilirlik şartları, yetersiz açıklama, ilk hâlin aşılması, patent isteme hakkı yokluğu, koruma kapsamının aşılması). Görüş bildirme; bilinen önceki teknik ve itiraz/hükümsüzlük sonuçlarını listele.
- **Yeniden tesis arası iyiniyetli kullanım (m. 107/3):** hakkın kaybı ile yeniden tesis kararının yayımı arasında iyiniyetle kullanan ya da ciddi tedbir alan kişinin ücretsiz kullanmaya devam hakkı.

## Açık sorular

Her patent için gerçek bir FTO çalışmasının cevaplayacağı soruları listele, örneğin: sicildeki sahip ve devirler güncel mi (devir sözleşmeleri noter onaylı ve sicile kayıtlı mı: m. 148/4-5)? Dosya geçmişinde terim [X] için ne dendi? İtiraz ya da hükümsüzlük yoluyla istemler değişti mi? Lisans (sözleşmesel, standart havuzu) mevcut mu? Sahibin Türkiye'deki dava geçmişi ne?

## Önerilen sonraki adımlar

- **Bağımsız istemin her unsuru lafzen karşılanıyor:** *dur ve uzman al.* Seçenekler: resmî FTO görüşü, tasarım değişikliği, lisans, itiraz (verilme kararının yayımından 6 ay: m. 99/1) ya da hükümsüzlük davası (koruma süresince ya da sona ermeyi izleyen 5 yıl: m. 138/5), riski bilerek ilerleme. Seçim, uzmanın bilgilendirdiği iş kararıdır.
- **Unsurlar iki yöne işliyor ya da yorum belirleyici:** uzmandan tam FTO çalışması; bu elemeyle lansman yapılmaz.
- **Belirsizliği gidermek için:** hak sahibinden görüş istenip bir ay içinde cevap gelmez ya da cevap kabul edilmezse tecavüzün mevcut olmadığının tespiti davası açılabilir; bildirim dava şartı değildir ve kendisine tecavüz davası açılmış kişi bu davayı açamaz (m. 154/1). Görüş istemek patenti "bilme"yi belgeler — avukat kararı.
- **Patent sona ermiş/ücretsiz görünüyor:** yürürlüğü uzman sicilden teyit etsin (telafi penceresi: m. 101/4).
- **Veritabanı yoktu:** sıradaki adım resmî araştırmadır, lansman kararı değil.
- **Her zaman:** "bilme" notunu tekrarla ve sonraki yolun uzman tarafından yazılı belgelenmesini öner.

## Çıktı

Eklenti ayarı `## Outputs` → üst başlık. Rol avukatsa dar dağıtımlı hukuk belgesi olarak işaretle; değilse aşağıdaki kapı.

```markdown
[ÜST BAŞLIK]

# FTO Elemesi — İlk Geçiş (GÖRÜŞ DEĞİLDİR)

**Bu bir FTO görüşü değildir.** "Belirgin engelleyici patent yok" sonucu ürünün serbest
olduğu anlamına gelmez. Ürün kararından önce patent vekili/uzman avukat değerlendirmelidir.

**Eleme sonucu:** [YEŞİL / SARI / KIRMIZI — tek cümle neden]

## Konu
- **Ürün / usul / özellik:** [teknik öz]
- **Dayanılan teknik bilgi:** [şartname, şema, sayfa, kod, mühendis anlatımı]
- **Ülkeler ve fiiller:** [üretim / satış / kullanım / ithal — m. 85/2]
- **Zamanlama:** [lansman öncesi / yakın / satışta]

## Araştırma kapsamı
- **Kaynaklar:** [bağlayıcı / TÜRKPATENT elle / Espacenet-PATENTSCOPE elle — ya da "araştırma yapılmadı"]
- **Sorgu, sınıflar, tarih aralığı:** [...]
- **Taranmayanlar:** [sahip bazlı tarama, SEP, tasarımlar, yabancı eşdeğerler]

## Bulunan patentler
| Patent | Ülke | Sahip | Rüçhan / veriliş | Bitiş | Yürürlükte mi? | Kaynak |
|---|---|---|---|---|---|---|

## İstem tabloları — ilk geçiş
### [Patent no.] — bağımsız İstem [N]
> "[İstemin tam metni]"
| Unsur | Üründe var mı? | Dayanak |
|---|---|---|
**Lafzi okuma:** [...] **Eşdeğerlik (m. 89/5, yalnız bayrak):** [...]
**Dolaylı / bölünmüş (yalnız bayrak):** [...]

## Sınırlar ve savunmalar (bayrak)
## Açık sorular
## Sinyaller (doğrulanmış patent değildir)
## Önerilen sonraki adımlar
## "Bilme" notu
## Atıf doğrulaması
Her patent numarası, istem alıntısı, tarih ve dosya geçmişi bilgisi yetkili sicilden
(TÜRKPATENT, EPO sicili, ilgili ulusal ofis) açılarak doğrulanır. İstem alıntısı en sık hata
yeridir — tek kelime analizi değiştirir.
```

## Avukat olmayan kullanıcı kapısı

`## Who's using this` → rol avukat değilse:

> Bu çıktı bir araştırma elemesidir, hukuki görüş değildir. Yalnız buna dayanarak ürünü piyasaya sürmek, satmaya devam etmek ya da yatırım yapmak hukuki sonuç doğurur: hak sahibi tecavüzün durdurulmasını, ürünlere elkonulmasını ve tazminat isteyebilir (SMK m. 149, m. 159). Karar vermeden önce sicile kayıtlı bir patent vekili ya da patent alanında uzman bir avukat değerlendirmeli (sicile kayıtlı patent vekilleri Kurum nezdinde işlem yapabilir: m. 160/1).
>
> Uzmana götüreceğiniz bir sayfalık özet: ürün tarifi, ülkeler, yapılan ve yapılmayan araştırma, bulunan patentler ve istem tablosu okumaları, açık sorular ve sorulacak üç soru. Avukat için bağlı olduğunuz baroya başvurabilirsiniz.

Analizi saklama; özetle birlikte teslim et. Elemenin dar çevrede kalması gereken bir hukuk belgesi olduğunu, hukukçu olmayan üçüncü kişilere iletilmemesini yaz.

## Çıktı yeri

Matter aktifse `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`; değilse `~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/fto-triage-<subject-slug>-YYYY-MM-DD.md`. Yolu göster; matter aktifse `history.md`'ye tek satır ekle.

## Kapanış

`## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu elemeye göre uyarla (tam FTO iste, tasarım değişikliği, lisans görüşmesi, itiraz/hükümsüzlük değerlendirmesi, ek teknik bilgi, bekle). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- **FTO görüşü vermez.** Hiçbir zaman.
- İstem yorumunu karara bağlamaz; belirleyici terimi ve iki makul yorumu işaretler.
- Geçerlilik hakkında görüş bildirmez (yenilik, buluş basamağı, açıklama yeterliliği); bilinen itiraz/hükümsüzlük sonuçlarını not eder.
- İstem yazmaz; tazminat hesaplamaz (m. 151 hesabı bilirkişi ve uzman işidir).
- Marka, tasarım ya da ticari sır analizi yapmaz — `/ip-legal:infringement-triage` ilgili modla.
- Çıktıyı karşı tarafa ya da dar çevre dışına aktarmaz.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6769", madde_no=["85","86","87","89","93","97","99","101","138","140"])
tr_mevzuat_madde_getir(number="6769", madde_no=["141","143","145","148","149","150","151","152","154","159"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="patent eşdeğerlik istem koruma kapsamı", kelime_modu="hepsi", date_from="2018-01-01")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma; seçenekleri say (sorguyu genişlet / başka araç / `[web — doğrula]` / dur ve avukata işaretle).

---

## /ip-legal:infringement-triage

---
name: infringement-triage
description: >
  Marka, telif, patent/faydalı model, tasarım ve ticari sır için tecavüz
  elemesi — her iki yöne işleyen etkenlerle bayrak listesi; tecavüz var/yok
  tespiti değildir. Türk hukuku tabanı: SMK m. 7, 29, 30 (marka), m. 85-89,
  141 (patent), m. 59, 81 (tasarım), m. 149-159 (hukuki talepler, tazminat,
  ihtiyati tedbir); TTK m. 55-56 ve TCK m. 239 (ticari sır). Birinin
  hakkınızı ihlal edip etmediğini ya da sizin başkasının hakkını ihlal edip
  etmediğinizi değerlendirirken, taklit/kopya ürün çıktığında ya da bir işin
  takibe değip değmeyeceğine karar verirken kullan.
argument-hint: "[olguları ve hangi hak olduğunu yazın — ya da yalnız olguları, hakkı ben sorarım]"
---

# /infringement-triage — Tecavüz Elemesi

## BU BİR ELEMEDİR, TESPİT DEĞİLDİR

**Her çıktının en üstüne yaz. Çıkarma, yumuşatma.**

> **Bu bir elemedir; tecavüz olduğu ya da olmadığı yönünde bir tespit değildir.** Tecavüz analizi olgulara sıkı sıkıya bağlı ve hukuken karmaşıktır. Eleme etkenleri belirler ve en önemlilerini işaretler; sonuca varmaz. "Tecavüz var/yok" demek; olgular, hakkın kapsamı, uygulanacak hukuk ve savunmalar üzerinde avukat takdiri gerektiren bir hukuki görüştür. Yalnız elemeye dayanarak ihtarname göndermek, durmayı reddetmek, dava açmak ya da açmamak; karşı tarafın tecavüzün mevcut olmadığının tespiti davasına (SMK m. 154), haksız rekabet iddiasına, yargılama giderlerine ve tazminata yol açabilir.

Çakışmayı küçük göstermek geri dönüşsüz kapıdır: ihtar gönderilmez ve marka piyasada yaygın ad hâline gelir (iptal nedeni: m. 26/1-b); talep peşine düşülmez ve zamanaşımı işler; kopyalanmış içerik sitede kalır. Fazla bayrak geri dönüşlü kapıdır. Geri dönüşlü tarafta kal.

## Destination check

Çıktı karşı tarafa, geniş kanala ya da basına gidecekse dur; avukatın sır saklama yükümlülüğü (Av. K. m. 36) belgeyi müvekkilin elinde korumaz. Yalnız hukuk için tam sürüm, iş birimi için arındırılmış sürüm öner. Kanonik kural: `## Shared guardrails → Destination check`.

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/ip-legal:matter-workspace switch <slug>` ya da `practice-level`." `matter.md`'yi yükle; çıktıyı matter klasörüne yaz; `Cross-matter context` `on` değilse başka matter'ı okuma. Eleme genelde ihtarname ya da içerik kaldırmaya gider; pratik büro ise ve matter yoksa açılmasını öner — eleme, ihtar ve cevap aynı dosyada kalsın.

## Önce profil

`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve `firm-profile.md`: `## Who's using this` (rol); `## Enforcement posture` (agresif / ölçülü / temkinli ve mektup türüne göre onaylayıcı — yönlendirme buna uyar); `## IP practice profile` → `Registered in`; `## Brand protection`; `## Available integrations`; `## Decision posture on subjective legal calls`.

Ayar `[PLACEHOLDER]` içeriyorsa: `/ip-legal:cold-start-interview` ya da **"provisional"** — Türkiye, orta risk, avukat rolü, playbook yok; her bulguda `[PROVISIONAL]` ve sonda "profilinizi kurun" notu.

## Mod seçimi

En başta sor:

> Hangi hakkı eliyoruz?
> 1. **Marka** — karıştırılma, tanınmış marka, karşılaştırmalı reklam
> 2. **Telif** — eser, mali/manevi hak, izin
> 3. **Patent / faydalı model** — istem tablosu, lafzi okuma + eşdeğerlik
> 4. **Tasarım** — genel izlenim, tescilli/tescilsiz
> 5. **Ticari sır** — sır niteliği, önlemler, hukuka aykırı elde etme/ifşa
> 6. **Karışık / emin değilim** — olguları anlatın, ben ayırırım

Aynı olgu birden çok hakkı doğurabilir (logomuz kullanılıyor → marka; ürün bizimkinin kopyası → patent/tasarım/telif; eski çalışanımız kurdu → ticari sır). **Birden çok hak varsa her birini ayrı elemeden geçir;** karıştırma — etkenler, mahkeme yolları ve talepler farklıdır.

## Ortak girdi

> 1. **Pozisyon.** Hak sahibi siz misiniz (sizinkini alıyorlar), yoksa iddia edilen taraf mı? Etkenler simetriktir ama çıktı farklıdır: biri ihtarnameye, diğeri risk notuna gider.
> 2. **Ülke.** Varsayılan Türkiye. Yabancı hukuk ihtimali varsa işaretlerim.
> 3. **Zaman.** Ne zaman öğrendiniz? Fiil ne zaman başladı? (Aşağıdaki saatler.)
> 4. **Deliller.** Ekran görüntüsü, URL, ambalaj fotoğrafı, fatura, kod parçası, eski çalışan sözleşmesi, tescil belgesi.

Cevap gelmeden etkenlere geçme.

### Saatler (her modda kontrol et)
- **Hukuki talepler:** SMK'dan doğan özel hukuk taleplerinde TBK zamanaşımı uygulanır (SMK m. 157): tazminat istemi zararı ve yükümlüyü öğrenmeden itibaren 2 yıl, her hâlde fiilden itibaren 10 yıl; fiil ceza kanunlarında daha uzun zamanaşımına tabi suçsa o süre (TBK m. 72). Sürekli tecavüzde başlangıç ve durdurma/men taleplerine zamanaşımı uygulanıp uygulanmayacağı **tartışmalı — içtihadı kontrol et**.
- **Ceza yolu:** marka suçları (SMK m. 30/6) ve TCK m. 239 kural olarak şikâyete bağlıdır; şikâyet, fiil ve failin öğrenildiği günden itibaren 6 ay içinde yapılmazsa soruşturma yapılamaz (TCK m. 73/1-2).
- **Sessiz kalma:** marka sahibi sonraki tarihli markanın kullanımını bilip 5 yıl sessiz kalırsa, kötüniyet yoksa, markasını hükümsüzlük gerekçesi yapamaz (SMK m. 25/6). Tecavüz talepleri bakımından sessiz kalmanın etkisi **tartışmalı — içtihadı kontrol et**.
- **Mahkeme:** fikri ve sınai haklar hukuk/ceza mahkemesi, yoksa asliye hukuk/ceza (m. 156/1); hak sahibinin davasında yetki davacının yerleşim yeri, fiilin gerçekleştiği ya da etkilerinin görüldüğü yer (m. 156/3). İhtiyati tedbir için tecavüzün ülke içinde gerçekleştiği ya da ciddi ve etkin hazırlık yapıldığı ispat edilmelidir (m. 159/1). Dava şartı arabuluculuğun uygulanıp uygulanmayacağı **tartışmalı — kontrol et**.

## Marka modu

**Hakkın kapsamı.** Koruma tescille doğar (m. 7/1). Marka sahibi izinsiz şu kullanımların önlenmesini isteyebilir (m. 7/2): (a) aynı işaret + tescil kapsamındaki mal/hizmet; (b) aynı/benzer işaret + aynı/benzer mal/hizmet nedeniyle **ilişkilendirilme ihtimali dahil karıştırılma ihtimali**; (c) Türkiye'de ulaştığı tanınmışlık nedeniyle haklı sebep olmaksızın itibardan haksız yarar, itibara zarar ya da ayırt edici karakteri zedeleme — farklı mal/hizmette de. Yasaklanabilecek kullanım biçimleri: mal/ambalaja koyma, piyasaya sürme ve stoklama, ithal/ihraç, iş evrakı ve reklam, internette alan adı/yönlendirici kod/anahtar sözcük, ticaret unvanı/işletme adı, hukuka aykırı karşılaştırmalı reklam (m. 7/3). Tecavüz fiilleri: m. 29/1 (izinsiz kullanım, taklit, taklit olduğunu bilerek ya da bilmesi gerekerek satış/ithal/elde bulundurma, lisans aşımı).

**Karıştırılma etkenleri** — `/ip-legal:clearance` skill'indeki listeyi yürü (işaret benzerliği ve genel izlenim, mal/hizmet benzerliği, tüketici ve dikkat düzeyi, önceki markanın ayırt edicilik/tanınmışlık derecesi, kanallar, kötüniyet, fiilî karıştırma). Her etken bir bayraktır.

**Tanınmış marka (m. 7/2-c).** Türkiye'deki tanınmışlık düzeyi ispat konusudur; yalnız sektörde bilinme yeterli mi **tartışmalı — içtihadı kontrol et**. Açık değilse "zorlama" diye işaretle.

**Karşılaştırmalı/yanıltıcı reklam.** SMK m. 7/3-f ile birlikte haksız rekabet: kötüleme, gerçek dışı/yanıltıcı açıklama, yanıltıcı ya da tanınmışlıktan gereksiz yararlanan karşılaştırma (TTK m. 55/1-a-1, 2, 5); davalar TTK m. 56. Beyan açıkça yanlış mı, ima yoluyla mı yanıltıcı, yoksa abartılı övgü mü — ayır.

**Tescilsiz işaret.** Tescil yoksa SMK tecavüz davası değil, karıştırılmaya yol açan önlemler nedeniyle haksız rekabet (TTK m. 55/1-a-4) ve önceki hakka dayalı itiraz/hükümsüzlük (SMK m. 6/3, m. 25/1) gündeme gelir.

**Savunmalar ve eşikler (bayrak):**
- Dürüst kullanım: kendi ad/adres, tanımlayıcı açıklama, yedek parça/aksesuar amacının belirtilmesi (m. 7/5).
- Kullanmama def'i: davacının markası 5 yıldır tescilliyse kullanım ispatı istenebilir; süre dava tarihine göre belirlenir (m. 29/2, m. 19/2).
- Hakkın tüketilmesi: hak sahibi ya da izniyle piyasaya sunulan ürünler (m. 152/1) — ürün değiştirilmiş/kötüleştirilmişse istisna (m. 152/2).
- Davalının kendi tescili: önceki tarihli hak sahibinin davasında savunma olarak ileri sürülemez (m. 155).
- Hakların başlangıcı: koruma tescilin yayımından itibaren; başvurunun Bültende yayımından sonraki fiiller için tazminat davası açılabilir ama mahkeme tescil yayımlanmadan karar veremez (m. 7/4).

**Ceza yolu.** İktibas ya da iltibas suretiyle tecavüz kanun metninde hapis ve adli para cezası gerektirir (m. 30/1); markanın Türkiye'de tescilli olması şarttır (m. 30/5); şikâyete bağlıdır (m. 30/6); taklit malın kaynağını bildirip üretenlerin ortaya çıkmasını sağlayan satıcıya ceza verilmez (m. 30/7). Ceza yolunu seçmek `## Enforcement posture` onayı ister.

## Telif modu

Bu skill telif analizini derinleştirmez; FSEK hükümleri bu eklentide başka skill'lerde işlenir. Eleme için şu bayrakları topla, sonra yönlendir:
- Eser niteliği ve sahiplik (yaratan, çalışan/işveren ilişkisi, devir ya da lisans sözleşmesinin yazılılığı ve hakların tek tek sayılıp sayılmadığı).
- Hangi mali/manevi hak etkileniyor; izin ya da sözleşme var mı; kanuni istisna iddiası var mı.
- Erişim + benzerlik delilleri; bağımsız yaratma ihtimali.
- İçerik internette barındırılıyorsa yer sağlayıcı/içerik sağlayıcı ayrımı.

ABD'deki dava için tescil ön şartını ve "fair use" testini Türk davasına taşıma. FSEK maddelerini `tr_mevzuat_madde_getir(number="5846", ...)` ile çek ve yönlendir: internetteki içerik → `/ip-legal:takedown`; ihtar → `/ip-legal:cease-desist`; yazılım lisansı/açık kaynak → `/ip-legal:oss-review`.

## Patent / faydalı model modu

`/ip-legal:fto-triage` ile aynı çerçeve (istem tablosu, lafzi okuma, m. 89/5 eşdeğerliği, m. 86 dolaylı kullanım), "kendi ürünümüz" yerine "iddia edilen ürün". Ek olarak:
- **Tecavüz fiilleri (m. 141/1):** izinsiz üretim yoluyla taklit; taklit olduğunu bilerek ya da bilmesi gerekerek satış, dağıtım, ithal, ticari amaçla elde bulundurma; usulün izinsiz kullanımı ve usulle doğrudan elde edilen ürünler; lisans aşımı.
- **İspat:** ürün yeniyse patentli usulle elde edildiği kabul edilir, aksini davalı ispatlar; davalının üretim ve işletme sırlarındaki haklı menfaati gözetilir (m. 141/2).
- **Başvuru dönemi:** yayımdan itibaren dava açılabilir; haberdar edilen ya da kötüniyetli tecavüzcü için yayımdan önce de (m. 141/3); mahkeme m. 99/3 ya da /7 yayımından önce karar veremez (m. 141/4).
- **Savunmalar (bayrak):** m. 85/3 istisnaları; önceki kullanım (m. 87); tüketilme (m. 152); hükümsüzlük nedenleri (m. 138) — karşı dava ya da tecavüzün mevcut olmadığının tespiti davasıyla birlikte (m. 154/3); faydalı modelin verilmesi geçerlilik garantisi değildir (m. 143/13).
- **Talepler:** tespit, önleme, durdurma, tazminat, elkoyma, imha, ilan (m. 149/1). Yoksun kalınan kazanç hak sahibinin seçimine göre muhtemel gelir, tecavüzcünün net kazancı ya da makul lisans bedeli üzerinden (m. 151/2); patent sahibi kullanma yükümlülüğünü yerine getirmemişse lisans bedeli yöntemi (m. 151/5). Hesap yapma — bilirkişi işidir.
- **Yabancı ülke:** Almanya `de_norm_getir(kanun="PatG", norm="9")`, Birleşik Krallık `uk_get_section(year="1977", number="37", section="60")`; diğerleri için "ArthurLegal'da kaynak yok".

Çıktı biçimi `fto-triage` ile aynıdır. Dava için tam istem tablosu (dayanak atıfları, bağımlı istemler, yorum bayrakları) uzmanla hazırlanır; ArthurLegal'da ayrı bir istem tablosu skill'i yok.

## Tasarım modu

**İstem tablosu çizme, unsur unsur eşleme yapma.** Tasarım; ürünün ya da parçasının çizgi, şekil, renk, malzeme, doku gibi özelliklerinden kaynaklanan görünümüdür (m. 55/1); tescilli ya da — ilk kez Türkiye'de kamuya sunulmuşsa — tescilsiz korunur (m. 55/4).
- **Ölçüt:** tasarım sahibi, kendi tasarımına kıyasla ayırt edici niteliğe sahip olmayan tasarımlara karşı hak kullanır; değerlendirmede tasarımcının seçenek özgürlüğü dikkate alınır (m. 58/1-2). Ayırt edicilik bilgilenmiş kullanıcının genel izlenimiyle ölçülür (m. 56/5-6). Önceki tasarımlar kalabalıksa koruma alanı daralır — önceki tasarımları iste.
- **Tescilsiz tasarım:** yalnız aynısının ya da genel izlenim itibarıyla ayırt edilemeyecek kadar benzerinin **kopyalanması** önlenebilir; makul yollarla bilemeyen tasarımcının bağımsız tasarımı kopya sayılmaz (m. 59/2). Koruma ilk kamuya sunmadan itibaren 3 yıl (m. 69/2).
- **Koruma dışı:** teknik fonksiyonun zorunlu kıldığı görünüm, başka ürüne mekanik bağlantı için zorunlu biçim/boyut (m. 58/4-b, c). Benzerlik bu özelliklerdeyse işaretle.
- **İstisnalar:** özel ve ticari olmayan, deneme, şartlı eğitim/referans amaçlı fiiller (m. 59/3); birleşik ürüne orijinal görünümünü kazandırmak için onarım parçası, piyasaya ilk sürülmeden itibaren 3 yıl sonra (m. 59/4).
- **Tecavüz fiilleri ve başlangıç:** m. 81/1; tescil yayımlanınca dava, haberdar edilen ya da kötüniyetli için yayımdan önce de (m. 81/2); tescil kaydı ürüne konmamış olsa da tecavüz (m. 81/3).
- **Paralel kanallar:** FSEK koruması saklıdır (m. 58/3) → telif modu; üç boyutlu marka; haksız rekabet (TTK m. 55/1-a-4).

**Malzeme iste:** "Genel izlenim karşılaştırması için (a) tescil belgesindeki tüm görseller ya da tescilsiz tasarımın ilk kamuya sunulduğu görseller ve tarihi, (b) iddia edilen ürünün aynı açılardan fotoğrafları, (c) bildiğiniz önceki tasarımlar gerekli." Görmeden genel izlenim hakkında bayrak dahi verme. İlk geçişin ötesi için tasarım uzmanına yönlendir.

## Ticari sır modu

Dayanaklar dağınıktır; kanunda genel bir ticari sır tanımı ve "makul önlem" ölçütü aranıyorsa `tr_mevzuat_icinde_ara` ile kontrol et — tanım ve önlem eşiği **tartışmalı — içtihadı kontrol et**. Karşılaştırma için AB: `eu_get_document_text(celex="32016L0943")` (Ticari Sırlar Direktifi).

**Sır mı?** Genel olarak bilinmiyor mu; sır olmasından ekonomik değer doğuyor mu; açık unsurların derlemesi mi? Her birini olguya bağla.

**Önlemler (listele, karar verme):** çalışan/yüklenici/karşı taraf gizlilik sözleşmeleri (imzalı, kapsamı, uygulanmış mı); teknik ve fiziksel erişim kısıtları; "gizli" işaretlemesi; çıkış görüşmesi ve iade; politika ve eğitim.

**Hukuka aykırı elde etme / ifşa:**
- Gizlice ve izinsiz ele geçirilen ya da hukuka aykırı öğrenilen bilgileri değerlendirmek ya da bildirmek (TTK m. 55/1-d); emanet edilmiş teklif, hesap, plan gibi iş ürününden yetkisiz yararlanma (m. 55/1-c-1, 2); işçileri işverenin sırlarını ifşaya yöneltmek (m. 55/1-b-3) — yeni işveren riski. Davalar: tespit, men, maddi durumun ortadan kaldırılması, kusur varsa tazminat (TTK m. 56/1).
- İşçi, öğrendiği üretim ve iş sırlarını hizmet süresince kullanamaz, açıklayamaz; işverenin haklı menfaati gerektirdiği ölçüde sonrasında da (TBK m. 396/4).
- Ceza: görev/meslek gereği vakıf olunan ticari sırrı yetkisiz kişilere vermek ya da hukuka aykırı elde edip ifşa etmek, şikâyet üzerine (TCK m. 239/1); fenni keşif, buluş ve sınai uygulama bilgileri dahil (m. 239/2); Türkiye'de oturmayan yabancıya açıklamada ceza artırılır ve şikâyet aranmaz (m. 239/3).
- Buluş söz konusuysa: çalışan hizmet buluşunu serbest buluş niteliği kazanana kadar gizli tutar (SMK m. 114/6) → `/ip-legal:invention-intake`.

**Eski çalışan senaryosu:** yeni işveren, iş örtüşmesi, ayrılış zamanı, götürülen ve iade edilen belgeler, erişim kayıtları, işe alım kanalı, gizlilik ve buluş devri sözleşmeleri. Rekabet yasağı sorusu → `/employment-legal:hiring-review` ya da `/employment-legal:termination-review`. Tersine mühendisliğin hukuka uygun elde etme sayılması **tartışmalı — içtihadı kontrol et**.

## Çıktı (tüm modlar)

Eklenti ayarı `## Outputs` → üst başlık.

```markdown
[ÜST BAŞLIK]

# Tecavüz Elemesi — [Marka | Telif | Patent | Tasarım | Ticari Sır] (TESPİT DEĞİLDİR)

**Bu bir elemedir; tecavüz olduğu ya da olmadığı yönünde tespit değildir.** Sonuç;
olgular, hakkın kapsamı, hukuk ve savunmalar üzerinde avukat takdiri ister.

**Eleme sonucu:** [YEŞİL / SARI / KIRMIZI — tek cümle neden]

## Pozisyon ve kapsam
- **Pozisyon:** [hak sahibi / iddia edilen taraf]  **Hak:** [...]  **Ülke:** [...]
- **Uygulanan çerçeve:** [çekilen maddeler — citation birebir]
- **Saatler:** [zamanaşımı / şikâyet süresi / sessiz kalma — durum]
- **İncelenen deliller:** [liste]

## Etken analizi
[Moda özgü tablo — her etken bayrak + yön; hüküm değil]

## Savunmalar ve eşikler
[Moda özgü: kullanmama def'i / tüketilme / m. 155 / m. 85-87 / hükümsüzlük / tasarım istisnaları / önlem eksikliği / tersine mühendislik]

## Hangi yöne işliyor — özet
| Etken | Bayrak | Yön (hak sahibi / iddia edilen / karışık) |
|---|---|---|

**Sonuç:** *Bu skill sonuç vermez.* Harekete geçmeden avukat takdiri gerekli.
[Hak sahibi lehine işleyen etkenler: ...; iddia edilen taraf lehine: ...]

## Önerilen sonraki adımlar
- [uzman görüşü / `Outside counsel roster`]
- [delil koruma: m. 150/3 belge ibrazı talebi, tespit, noter tespiti — saat işliyorsa]
- [eksik olgu: erişim kayıtları, dosya geçmişi, pazar verisi]
- [`## Enforcement posture` onay zinciri — ileri sürme kararı varsa]

## Atıf doğrulaması
Her madde, karar künyesi, tescil numarası, istem alıntısı ve delil yetkili kaynaktan
açılarak doğrulanır. Atıf: `[ArthurLegal TR — 6769 SMK m. X — GG.AA.YYYY]`.
```

## Avukat olmayan kullanıcı kapısı

`## Who's using this` → rol avukat değilse:

> Bu çıktı bir araştırma elemesidir, hukuki görüş değildir. Yalnız buna dayanarak ihtarname göndermek, durmayı reddetmek, şikâyet ya da dava yoluna gitmek veya "bu serbest kullanım" diye devam etmek hukuki sonuç doğurur: karşı taraf tecavüzün mevcut olmadığının tespitini isteyebilir (SMK m. 154), haksız bir tecavüz iddiası haksız rekabet tartışması doğurabilir (TTK m. 55/1-a-1 — **tartışmalı**), yargılama giderleri aleyhine hüküm verilen taraftan alınır (HMK m. 326/1); iddia edilen tarafsanız durdurma, elkoyma ve tazminat (SMK m. 149) gündeme gelir. Harekete geçmeden bir avukat ya da sicile kayıtlı marka/patent vekili değerlendirmeli.
>
> Götüreceğiniz bir sayfalık özet: hak, pozisyon, olgular ve deliller, bulunan etkenler, işaretlenen savunmalar, işleyen saatler ve sorulacak üç soru. Avukat için bağlı olduğunuz baroya başvurabilirsiniz.

Elemeyi özetle birlikte teslim et.

## Çıktı yeri

Matter aktifse `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/infringe-<mode>-<subject-slug>-YYYY-MM-DD.md`; değilse `~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/infringe-<mode>-<subject-slug>-YYYY-MM-DD.md` (`<mode>`: `trademark` / `copyright` / `patent` / `design` / `trade-secret`). Yolu göster; matter aktifse `history.md`'ye tek satır.

## İleri sürme skill'lerine devir

Eleme ileri sürmeye işaret ediyor ve `## Enforcement posture` destekliyorsa öner — kendiliğinden yazma:

> Bunun için ihtarname taslağı ister misiniz? `/ip-legal:cease-desist` çalıştırın; bu elemenin bayrak listesini olgusal dayanak yapar, profilinizdeki onay zincirini uygularım — onaylayıcı imzalamadan hiçbir yere gitmez.

İçerik internette barındırılıyorsa: "İçerik kaldırma için `/ip-legal:takedown`." İleri sürme kararı onaylayıcınındır, elemenin değil.

## Kapanış

`## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu elemeye göre uyarla (ihtar taslağı, eskalasyon, ek olgu, izle ve bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- **Tecavüz var/yok sonucuna varmaz.** Hiçbir zaman.
- Anket, bilirkişi ya da istem yorumunun yerini tutmaz.
- Elemenin ülke kapsamı dışındaki savunmaları değerlendirmez; olgular sınır aşıyorsa yabancı hukuk analizini işaretler, kuralı araçla çeker ya da "kaynak yok" der.
- İhtarname, içerik kaldırma talebi ya da dava dilekçesi yazmaz — bunlar onay zincirine bağlı ayrı skill'lerdir.
- Çıktıyı karşı tarafa aktarmaz.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6769", madde_no=["7","19","25","29","30","55","56","58","59","81"])
tr_mevzuat_madde_getir(number="6769", madde_no=["141","149","150","151","152","154","155","156","157","159"])
tr_mevzuat_madde_getir(number="6102", madde_no=["55","56"])
tr_mevzuat_madde_getir(number="6098", madde_no=["72","396"])
tr_mevzuat_madde_getir(number="5237", madde_no=["73","239"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="marka tecavüz karıştırılma ihtimali tanınmış", kelime_modu="hepsi", date_from="2020-01-01")
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="tasarım genel izlenim bilgilenmiş kullanıcı", kelime_modu="hepsi")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="ticari sır haksız rekabet işçi", kelime_modu="hepsi")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma; seçenekleri say.

---

## /ip-legal:invention-intake

---
name: invention-intake
description: >
  Buluş bildirimi ilk elemesi — yenilik, buluş basamağı, konu bakımından
  patentlenebilirlik (SMK m. 82-83), zararsız açıklama ve süreler (m. 84,
  m. 93), çalışan buluşu saatleri (m. 113-121), tespit edilebilirlik ve
  stratejik değer. Bir buluş bildirimi geldiğinde ve önceki teknik
  araştırması ile patent vekili incelemesine gidilip gidilmeyeceği, daha
  fazla bilgi istenip istenmeyeceği ya da reddedileceği elenecekse kullan.
argument-hint: "[buluş bildirimini yapıştırın ya da anlatın — ya da yalnız başlığı, gerisini sorarım]"
---

# /invention-intake — Buluş Bildirimi Elemesi

**Bu, uzman olmayan birinin yaptığı ilk elemedir; patentlenebilirlik görüşü değildir.** Eleme bir buluşun "patentlenebilir" olduğu sonucuna asla varmaz. Vardığı sonuç ya "ilk elemeyi geçti, önceki teknik araştırması ve patent vekili incelemesi gerekli", ya "bilgi eksik", ya da "eleyici bir sorun var" olur. Önceki teknik araştırması ayrı bir adımdır; bu skill yapmaz.

## BU BİR İLK ELEMEDİR, PATENTLENEBİLİRLİK GÖRÜŞÜ DEĞİLDİR

**Her çıktının en üstüne yaz. Çıkarma, yumuşatma.**

> **Bu, uzman olmayan birinin yaptığı ilk elemedir; patentlenebilirlik görüşü değildir.** Görüş; önceki teknik araştırması, istemlerin kurulması ve patent vekilinin ya da patent alanında uzman avukatın takdirini gerektirir. Bu eleme önceki teknik araştırması yapmaz ve istem kurmaz. Bariz eleyicileri (buluş zaten piyasada, iki yıl önce yayımlanmış, açıkça yalnız bir iş yöntemi) ve bariz olumlu işaretleri (yeni mekanizma, teknik ilerleme, yeni ve gizli tutulmuş) ayıklar; aradaki her şey araştırma ve uzman incelemesi ister.

Dosyalanması gereken bir buluşu gözden kaçırmak geri dönüşsüz kapıdır: zararsız açıklama süresi biter, yabancı haklar ilk açıklamada kaybolabilir, rakip önce başvurur, işverenin hak talebi süresi kaçar. Fazla bayrak yalnız boş dönen bir araştırma demektir. Geri dönüşlü tarafta kal.

## ⏰ ÖN-KONTROL — Süre

Elemeye başlamadan önce şu saatleri hesapla; biri 30 gün içinde doluyorsa notun **ilk satırına** "**Zaman hassas — [saat] [tarih]'te doluyor**" yaz.

1. **Çalışan buluşu (işveren tarafı saatleri)** — çalışan hizmet buluşunu işverene yazılı ve gecikmeksizin bildirir; işveren bildirimin ulaştığı tarihi çalışana yazılı bildirir (m. 114/1). İşveren bildirimin hangi hususlarda düzeltilmesi gerektiğini **iki ay** içinde bildirmezse bildirim geçerli sayılır (m. 114/4). İşveren tam ya da kısmi hak talebini bildirimin kendisine ulaşmasından itibaren **dört ay** içinde yazılı bildirmezse buluş **serbest buluş** olur (m. 115/1). Serbest buluş bildiriminde işverenin "serbest değil" itirazı **üç ay** (m. 119/2); işletmenin faaliyet alanındaki serbest buluş teklifine cevap **üç ay**, aksi hâlde işveren öncelik hakkını kaybeder (m. 119/4).
2. **Yükseköğretim kurumu** buluşlarında 115, 116, 118 ve 119/4 uygulanmaz; buluşu yapan kuruma yazılı ve gecikmeksizin bildirir, kurum hak talep ederse başvuru yapmakla yükümlüdür (m. 121/2-3, 5). **Kamu destekli projede** buluş destek veren kuruma bildirilir; destekten yararlanan kişi bildirimden itibaren **bir yıl** içinde hak sahipliği tercihini yazılı bildirmezse kurum hak sahipliğini alabilir ve süreç bitene kadar patentlenebilirliği etkileyecek açıklama yapılamaz (m. 122/1).
3. **Açıklama saati** — yenilik dünya çapında mutlaktır: başvuru tarihinden önce herhangi bir yerde toplumca erişilebilir hâle gelen her şey tekniğin bilinen durumudur (m. 83/2). İstisna: başvuru (ya da rüçhan) tarihinden önceki **on iki ay** içinde buluşu yapanın kendisinin, bir patent merciinin (sayılan hâllerde) ya da buluşu yapandan bilgi edinen üçüncü kişinin açıklaması patent/faydalı model verilmesini etkilemez; şartları ileri süren ispat eder (m. 84/1, 4).
4. **Rüçhan saati** — Türkiye'deki ya da Paris/DTÖ ülkesindeki ilk başvurudan itibaren **on iki ay** içinde aynı buluş için rüçhan hakkı (m. 93/1).
5. **Yabancı haklar** — zararsız açıklama kuralı ülkeden ülkeye farklıdır. Örneğin Almanya'da yalnız açık kötüye kullanım ya da resmî sergide teşhir kaynaklı ve başvurudan en çok altı ay önceki açıklama dışarıda bırakılır (`de_norm_getir(kanun="PatG", norm="3")`, § 3/5). Avrupa Patent Sözleşmesi, ABD ve diğerleri için ArthurLegal'da kaynak yok: yabancı başvuru planı varsa herhangi bir kamuya açıklamayı "**yabancı haklar risk altında**" diye işaretle ve ilgili ülkenin patent vekiline teyit ettir.

## Destination check

Buluş içeriği doğası gereği hassastır. Çıktıyı hukuk/patent dar çevresi dışına gönderme; özetini, alıntısını ya da varlığını geniş kanallarda anma. Kanonik kural: `## Shared guardrails → Destination check`. Çalışan buluşunu serbest buluş niteliği kazanana kadar çalışan, tam hak talep etmediği bildirimleri ise işveren gizli tutmakla yükümlüdür (m. 114/6, m. 115/5).

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/ip-legal:matter-workspace switch <slug>` ya da `practice-level`." `matter.md`'yi yükle; çıktıyı matter klasörüne yaz; `Cross-matter context` `on` değilse başka matter'ı okuma. Buluş bildirimleri sıklıkla **clean-team** ya da **heightened** gizlilikle açılır; `matter.md`'deki işarete uy.

## Önce profil

**Bildirimi okumadan önce** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve `firm-profile.md` oku. Eksikse ya da yer tutucu varsa dur ve `/ip-legal:cold-start-interview` öner. Profil şunları söyler:
- **Patent dosyalama stratejisi** — saldırı (ileri sürülecek portföy), savunma (kullanım serbestisi), karma, lisans geliri. Stratejik değer çıtası buradan gelir.
- **İlgi alanındaki teknolojiler** — alan dışı buluş teknik olarak temiz olsa da çoğu zaman reddedilir.
- **Bütçe duruşu** — eleği geçen her şeyi dosyala / en iyileri seç / yalnız işin gerektirdiğini.
- **Onay zinciri** — dosyalama kararını kim verir, geçen buluş kime yönlendirilir.
- **Ticari sır sınıflandırmasının sahibi** — tespit edilemez buluşlar ona gider.

Profil yalnız marka ya da telif pratiği gösteriyorsa (patent pratiği yok) bu yanlış araçtır; söyle ve yönlendir.

## Adım 1 — Bildirimi al

Bildirim yapıştırıldı ya da yüklendiyse oku; bir form ise alanları çıkar ve yalnız eksikleri sor. Değilse tek seferde sor:

> 1. **Buluş ne?** Sade dille — ne yapıyor, nasıl çalışıyor, ana fikir.
> 2. **Hangi sorunu çözüyor?** Önce ne bozuk ya da eksikti?
> 3. **Bilinenden farkı ne?** Önce ne yapılıyordu; bu neyi farklı yapıyor?
> 4. **Kim, ne zaman buldu?** İsimler, yaklaşık tarih; çalışan mı, öğrenci/stajyer mi (m. 113/3), yükseköğretim ya da kamu projesi mi? İşverene yazılı bildirim yapıldı mı, ne zaman ulaştı?
> 5. **Kamuya açıklandı mı?** Yayın, satış ya da satış teklifi, konferans sunumu, gizlilik sözleşmesiyle müşteriye gösterim, açık depo, makale, sürüm notu, yatırımcı sunumu. Evetse ne zaman, nerede?
> 6. **Kullanımda mı?** Satışta, pilotta, yol haritasında, kâğıt üstünde?
> 7. **Teknoloji alanı?** Yazılım, donanım, mekanik, biyoteknoloji, iş yöntemi, yapay zekâ/ML…

Yarım bildirimle eleme yapma; "kullanıcılara yardım eden yeni bir ML şeyi" elemesi hiç elememekten kötüdür.

## Adım 2 — Elemeler

Her elemenin hükmü: `✓ temiz`, `🟡 bayrak — ayrıca bakılmalı`, `🔴 kırmızı bayrak`. Gerekçe kısa.

### Eleme 1: Yenilik sinyalleri (m. 83/1-2)
Bildirimin kendi anlatımındaki bariz yenilik sorunları — tam yenilik analizi değildir.
- 🔴 "Bilinen tekniği yeni alana uyguladık"; "[ürün] gibi ama [X] için"; "rakipler benzerini yapıyor"; mevcut kamuya açık bir ürünün küçük ayarı.
- ✓ Yeni **mekanizma**; beklenmeyen sonuç veren yeni **birleşim**; alanın çözemediği sorunu, önceki yaklaşımların neden başarısız olduğunu açıklayarak çözmek.
- 🟡 Belirsiz her şey — araştırma çözer.

### Eleme 2: Buluş basamağı bayrakları (m. 83/4)
Tekniğin bilinen durumu dikkate alındığında ilgili teknik alandaki uzmana göre aşikâr mı? Bayrak koy, sonuç verme.
- 🔴 Bilinen unsurların öngörülebilir birleşimi; rutin optimizasyon ("parametreyi X'ten Y'ye çektik"); işlevsel avantajı olmayan tasarım tercihi; az sayıdaki bilinen çözümden makul başarı beklentisiyle denenen.
- ✓ Önceki teknik tersini öngörüyordu; beklenmeyen sonuç; uzun süredir duyulan ve başarısız denemelere rağmen karşılanmayan ihtiyaç.

### Eleme 3: Konu bakımından patentlenebilirlik (m. 82)
- **Buluş sayılmayanlar (m. 82/2):** keşifler, bilimsel teoriler, matematiksel yöntemler; zihni faaliyet, iş faaliyeti ve oyunlara ilişkin plan, kural ve yöntemler; bilgisayar programları; estetik mahsuller ve eserler; bilginin sunumu. **Yalnız bu konuların kendisi** dışarıdadır — teknik uygulamada kullanılmaları tek başına eleyici değildir.
- **Patent verilmeyenler (m. 82/3):** kamu düzeni/genel ahlaka aykırı buluşlar; bitki çeşitleri, hayvan ırkları ve esas olarak biyolojik üretim işlemleri (mikrobiyolojik işlemler hariç); insan ya da hayvan vücuduna uygulanacak teşhis, cerrahi ve tedavi yöntemleri — bu yöntemlerde kullanılan ürünler, özellikle madde ve terkipler hariç (m. 82/6); insan bedeni öğelerinin, gen dizisi dahil, yalnız keşfi; klonlama ve sayılan genetik işlemler.
- 🔴: "[bilinen işi] bilgisayarda yap" ve teknik iyileştirme yok; saf iş yöntemi; tek başına algoritma; teknik araç gösterilmeden yalnız işlev ("öner, sınıflandır, tahmin et") istenen yapay zekâ buluşu; doğal korelasyon ya da doğada bulunan maddenin keşfi.
- ✓: bilgisayarın kendisinde teknik iyileştirme (mimari, eğitim tekniği, donanım/yazılım arayüzü, güvenlik mekanizması); sonuç değil belirli teknik araç; teknik alanda (görüntü işleme, sıkıştırma, kriptografi, robotik) teknik araçla iyileştirme.
- Yazılım ve yapay zekâda sınır çizgisinin nerede olduğu TÜRKPATENT ve EPO uygulamasına bağlıdır; ArthurLegal'da bu uygulamanın kaynağı yok → sınırdaki her şey 🟡 "**m. 82 — uzmana yönlendir**", **tartışmalı**. Almanya'da aynı "as such" yapısı: `de_norm_getir(kanun="PatG", norm="1")` (§ 1/3-4).
- **Faydalı model alternatifi:** m. 142/1 yenilik ve sanayiye uygulanabilirlik arar, buluş basamağı şartına atıf yapmaz; ama kimyasal/biyolojik maddeler ve usuller, eczacılık, biyoteknoloji ve **usuller** faydalı modelle korunmaz (m. 142/3). Süre 10 yıl (m. 101/1). Buluş basamağı zayıf bir ürün buluşunda seçenek olarak işaretle.

### Eleme 4: Kamuya açıklama ve süreler
Ön-kontroldeki saatleri bu buluşa uygula.
- 🔴 **Muhtemelen engellenmiş:** başvurudan önce 12 aydan eski kamuya açıklama (m. 83/2; m. 84 dışında); ya da m. 84'ün saydığı hâllere girmeyen herhangi bir açıklama.
- 🟡 **Saat işliyor:** son 12 ay içinde buluşu yapanın açıklaması — Türkiye için m. 84 penceresi açık ama kapanıyor; yabancı haklar zaten risk altında olabilir. Açıklama tarihini teyit et, derhal başvuruya yönlendir.
- ✓ **Temiz:** kamuya açıklama yok. Gizlilik sözleşmesiyle müşteri gösterimi, iç kullanım, adı belli taraflara gizli beta, gönderilmemiş taslak makale genelde "toplumca erişilebilir" değildir ama olguya bağlıdır; dış tarafa her açıklamayı ayrıntısıyla başvuru ekibine işaretle.

Özellikle sor: dergi/konferans gönderimi ve ön baskı (preprint); dış katılımcılı konuşmalar; açık depo, blog, sosyal medya; sınırlı beta dahil sürümler; teklif, ihale cevabı, satış teklifi; gizlilik sözleşmesi olmayan yatırımcı veya yönetim kurulu üyesine açıklama. Buluşu içeren ürünün satış teklifi de açıklama olabilir.

### Eleme 5: Tespit edilebilirlik
Rakip bu buluşu kullansa anlayabilir misiniz? Gizli uygulanan buluş (sunucu tarafı işlem, arka ofis, iç üretim tekniği, model eğitim verisi/tekniği) patentten çok **ticari sır** olarak korunmaya uygun olabilir — patent başvurusu yayımlanır (m. 97/1) ve tespit edemeyeceğiniz bir tecavüz için buluşu rakibe vermiş olursunuz.
- 🔴 Düşük tespit edilebilirlik → **patent mi ticari sır mı kararı** için profildeki sahibine yönlendir. Ticari sır kanalları: haksız rekabet (TTK m. 55/1-d), işçinin sır saklama borcu (TBK m. 396/4), ceza (TCK m. 239/2 — fenni keşif, buluş ve sınai uygulama bilgileri).
- Hizmet buluşunda işletme sırlarının korunması başvuru yapmamayı gerektiriyorsa işverenin başvuru yükümlülüğü kalkar (m. 116/2-c); ama başvurudan kaçınılırsa çalışanın bedelinde patent alınmamasından doğan muhtemel kaybı dikkate alınır (m. 116/1).
- ✓ Yüksek: tüketici ürününde görünür; yayımlanmış API/protokol; dağıtılan üründe tersine mühendislikle anlaşılır mekanizma.

### Eleme 6: Stratejik değer
Profildeki stratejiye göre: saldırı → ileri sürmeye değer mi, kolay dolanılır mı? Savunma → rakiplerin başvurduğu bir alan mı? Lisans → kim, hangi şartla öder? Ayrıca: **çekirdek** mi **çevresel** mi; alan patent yoğun mu (önce başvuran kazanır) yoksa açık kaynak ağırlıklı mı; ilgi alanı listesinde mi?

### Eleme 7: Hak sahipliği
- Patent isteme hakkı buluşu yapana ya da halefine aittir; birlikte yapılmışsa aksine anlaşma yoksa hepsine (m. 109/1-2). Tüm buluşçular listede mi?
- Çalışansa hizmet buluşu mu serbest buluş mu (m. 113/1-2)? İşverenin hak talebi süresinde mi (m. 115/1)? Tam hak talebinde çalışanın makul bedel hakkı doğar (m. 115/6); bedelde ekonomik değerlendirilebilirlik, görev ve işletmenin payı dikkate alınır (m. 115/7).
- Çalışan buluşu hükümleri emredicidir; sözleşme serbestliği hizmet buluşunda başvurudan, serbest buluşta çalışanın bildiriminden sonra başlar (m. 117/1) — işe girişte imzalanan devir kaydına tek başına güvenme.
- Tasarım niteliğindeki çalışan katkısı için ayrı kural: m. 73.

## Adım 3 — Eleme notu

İç anlatım ("invention-intake skill'ini kullanıyorum") koyma. Eklenti ayarı `## Outputs` → üst başlık ve inceleyen notu.

```markdown
[ÜST BAŞLIK]

**Buluş eleme notu — [buluş başlığı]**
[Varsa: **Zaman hassas — [saat] [tarih]'te doluyor; yabancı haklar risk altında.**]

**Sonuç: [İLERLE (PURSUE) / ARAŞTIR (INVESTIGATE) / REDDET (DECLINE)]**
*[Tek cümle, sade dille neden.]*

| Eleme | Hüküm | Not |
|---|---|---|
| Yenilik sinyalleri (m. 83/1-2) | [✓/🟡/🔴] | |
| Buluş basamağı (m. 83/4) | | |
| Konu (m. 82) / faydalı model seçeneği (m. 142) | | |
| Kamuya açıklama ve süreler (m. 83/2, 84, 93) | | [tarihlerle] |
| Tespit edilebilirlik | | |
| Stratejik değer | | [profile atıfla] |
| Hak sahipliği ve çalışan buluşu saatleri (m. 109, 113-117) | | [tarihlerle] |

### Açık sorular
*Cevabı değiştirecek noktalar — buluşçu, başvuru ekibi ya da uzman cevaplamalı.*
- [soru]

### Sonraki adımlar (karar ağacı)
1. **Önceki teknik araştırmasını başlat** — vekile/araştırma firmasına talep taslağı (istem kavramları, buluşçular, sınıflandırma, bilinen referanslar).
2. **Buluşçuya geri dön** — açık maddeler için takip soruları.
3. **Uzmana yönlendir** (m. 82 sınırı / patent-ticari sır kararı) — bulguları ve gereken takdiri özetleyen yazı.
4. **Reddet ve teşekkür et** — buluşçuya teşekkür yazısı, ret gerekçesiyle arşiv. Çalışan buluşunda işverenin hak talep etmediğini bildirmesi buluşu serbest buluş yapar (m. 115/1) — ret yazısı bu sonucu bilerek yazılmalı.
5. **Ticari sır yoluna al** — ticari sır sahibine neden daha uygun olduğunu açıklayan not.
```

## Adım 4 — Sonuç

- **İLERLE (PURSUE)** — yeterince eleme temiz ya da kolayca düzeltilebilir; önceki teknik araştırması ve uzman incelemesi gerekli. Bu "patentlenebilir" değildir.
- **ARAŞTIR (INVESTIGATE)** — bir ya da daha çok eleme ek bilgi, uzman incelemesi ya da buluşçuya soru gerektiriyor. Açık maddeyi adıyla yaz.
- **REDDET (DECLINE)** — eleyici bir bayrak: yabancı hak kaygısı olmadan m. 84 penceresini aşmış açıklama, açıkça aşikâr, açıkça m. 82/2 kapsamında, ilgi alanı dışında, ticari sır yolu da olmayan tespit edilemez buluş.

Ret, buluşçunun anlayacağı somut gerekçe ister. "Patentlenemez" kabul edilebilir gerekçe değildir; "[tarih]'teki konferans sunumunuz m. 84'ün 12 aylık penceresini [tarih]'te kapattı" kabul edilebilir.

## Korkuluklar

- **Asla "patentlenebilir" deme.** En fazla: "ilk elemeyi geçti, araştırma gerekli".
- **Önceki teknik araştırması yapma.** "Bu var mı" web araması araştırma değildir; yaparsan söyle ve `[web — doğrula]` diye etiketle.
- **m. 82 sınırında çekil.** Yazılım/yapay zekâ/iş yöntemi sınırı uzmanların en çok ayrıştığı yerdir.
- **Stratejik değerden önce tespit edilebilirlik.** Tespit edilemez buluş için ticari sır seçeneğini ele almadan İLERLE deme.
- **Acil olanı acil işaretle.** Ön-kontroldeki saatlerden biri yakınsa notun ilk satırında.
- **Yönlendirmeye saygı.** Neyin dosyalanacağına başvurudan sorumlu patent vekili/avukat karar verir; eleme onu besler.

## Avukat olmayan kullanıcı kapısı

Rol **avukat değilse** notu şununla kapat:

> **Bu, bildiriminiz için bir eleme aracıdır, patentlenebilirlik görüşü değildir. Başvuru yapıp yapmama ve nasıl yapılacağı kararı sicile kayıtlı bir patent vekiline (Kurum nezdinde işlem yapabilir: SMK m. 160/1) ya da patent alanında uzman bir avukata aittir. Sonuç İLERLE ya da ARAŞTIR ise sonraki adımınız başvuru yapmak ya da istem yazmak değil, bu notu ve bildirimi uzmanla paylaşmaktır. Henüz uzman yoksa [profildeki kişi / bağlı olduğunuz baro] başlangıç noktasıdır. Çalışan buluşuysa işverenin dört aylık hak talebi süresini (m. 115/1) kaçırmayın.**

## Çıktı yeri

Matter aktifse matter klasörüne (`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`), değilse practice outputs klasörüne (`~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/`) yaz; yolu göster. Başvuru yapılırsa `/ip-legal:portfolio --add` öner.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6769", madde_no=["82","83","84","93","97","101","109","142"])
tr_mevzuat_madde_getir(number="6769", madde_no=["113","114","115","116","117","119","120","121","122"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="hizmet buluşu serbest buluş bedel", kelime_modu="hepsi")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz.

---

## /ip-legal:ip-clause-review

---
name: ip-clause-review
description: >
  Bir sözleşmedeki fikri mülkiyet klozlarını inceler — devir, sahiplik, lisans,
  garanti ve tazmin. İş, danışmanlık, iş paketi (SOW), tedarik ya da lisans
  sözleşmesinde fikri haklar incelenirken, devir dili ya da lisans kapsamı
  sorulduğunda ya da fikri mülkiyet hükmü içeren bir sözleşme yapıştırıldığında
  kullan. Türk hukuku tabanı: FSEK m. 18, 48-52 (yazılı şekil, hakların ayrı
  ayrı gösterilmesi, gelecekteki eserler), m. 14-16 (manevi haklar), SMK m. 73,
  148, 158, TBK m. 20-25 (genel işlem koşulları); çalışan buluşları
  /ip-legal:invention-intake'e yönlendirilir.
argument-hint: "[dosya yolu | Drive bağlantısı | metin]"
---

# /ip-clause-review

Sözleşmenin fikri mülkiyet klozlarını `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` profiline göre inceler: devir boşlukları, sahiplik belirsizliği, lisans kapsamı, garanti/tazmin sorunları. Çıktı: risk sırasına dizilmiş, gerektiğinde redline önerili kloz kloz not.

## Talimat

1. **Profili yükle.** Yer tutucu varsa dur: "Önce `/ip-legal:cold-start-interview` — klozları profilinize göre inceleyebilmem için pratiğinizi öğrenmeliyim."
2. **Sözleşmeyi al:** dosya, bağlantı ya da metin; yoksa iste.
3. **Akışı izle:** sözleşme türünü ve fikri haklar bakımından hangi tarafta olduğumuzu belirle (her belgede ayrı sorulur); iş/danışmanlık/SOW belgesinde önce devir boşluğu kontrolü; risk sırasına göre kloz bulguları; çapraz tutarlılık; yargı çevresi notu.
4. **Notu yaz** (şablon aşağıda): üst başlık, sonuç, devir boşluğu, önem sırasına göre klozlar, tutarlılık, yargı çevresi, onay yönlendirmesi.
5. **Karar duruşu:** bir kloz fikri hakkı iki yönde de okunabiliyorsa avukata işaretle, iki yöndeki etkenleri göster; sessizce karar verme.

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Açık ve aktif matter yoksa sor ("`/ip-legal:matter-workspace switch <slug>` ya da `practice-level`"). `matter.md` sapmalarını yükle; çıktıları `matters/<matter-slug>/` altına yaz; `Cross-matter context` `on` değilse başka matter okunmaz.

## Amaç

Avukata her klozun ne yaptığını, piyasadan ya da ekibin standart duruşundan nasıl saptığını, riskini ve gerekiyorsa önerilecek redline'ı tek geçişte söyle. **En yüksek riskli klozlar sahiplik ve devirdir;** sonradan düzeltilmeleri zordur ve birleşme/devralma inceleme sürecinde, finansmanda ya da davada yıllar sonra ortaya çıkar. Devir dili olması gereken bir belgede zayıf ya da yoksa notun en üstünde yüksek sesle işaretle.

Profil şunları söyler: yargı çevresi ayak izi (manevi hak feragatinin geçerliliği, işçi eseri rejimi, örtülü lisans), sapmaları kimin hangi önemde onayladığı (`## Enforcement posture` → `Approval matrix`, `Automatic escalations`), üst başlık (`## Outputs`).

## Akış

### Adım 1: Yönlen

| Soru | Cevap |
|---|---|
| Sözleşme türü | İş / danışmanlık ya da SOW / tedarik çerçeve / lisans alma / lisans verme / iş birliği-Ar-Ge / sulh / devralma ya da varlık devri / diğer |
| Fikri haklarda tarafımız | hak veren mi alan mı / devreden mi devralan mı / lisans veren mi alan mı |
| Karşı taraf | ad; birey mi, girişim mi, büyük şirket mi |
| Fikri hak için ayrı bedel | ücret, lisans bedeli, peşin ödeme, pay, yok |
| Uygulanacak hukuk ve yetki | ne diyor; profil bu yargı çevresini eskalasyon/asla listesinde mi işaretliyor |

Taraf belirsizse (iki yönlü katkılı iş birliği, akışlı hakları olan bayilik) sor: "[Müvekkil] bu sözleşmenin fikri haklarında hangi tarafta — veren, alan, ikisi? İkisiyse iki yönü ayrı incelerim."

### Adım 2: Devir boşluğu kontrolü (en yüksek öncelik)

İş, danışmanlık, SOW, ısmarlama iş ya da şirketin karşı tarafın ürettiği işten hak alması gereken her belgede **önce** bunu yap.

**Telif (FSEK):**
- **Yazılı şekil ve hakların tek tek sayılması:** mali haklara ilişkin sözleşme ve tasarruflar yazılı olmalı ve konu olan haklar ayrı ayrı gösterilmelidir (FSEK m. 52). "Tüm fikri haklar devredilmiştir" gibi genel ifade yerine işleme, çoğaltma, yayma, temsil, umuma iletim (m. 21-25) ayrı ayrı; süre, yer ve muhteva bakımından kapsam (m. 48/1). Mali haklar birbirine bağlı değildir; birinin devri diğerini kapsamaz (m. 20/1). Sayılmayan hak geçmez → 🔴.
- **Gelecekteki eserler — ABD "hereby assigns" alışkanlığı burada ters işler:** henüz vücuda getirilmemiş ya da tamamlanacak esere ilişkin **tasarruf** batıldır (m. 48/3); aynı konudaki **taahhüt** ise eser vücuda gelmeden yapılsa da geçerlidir (m. 50/1). Doğru yapı: devir **taahhüdü** + eser teslim edildiğinde/vücuda geldiğinde yazılı **devir** (teslim tutanağına bağlanmış). Eser sahibinin ileride vücuda getireceği eserlerin bütününe ya da belirli türüne ilişkin taahhüdü her taraf, ihbardan bir yıl sonra hüküm ifade etmek üzere feshedebilir (m. 50/2) — uzun süreli çerçeve sözleşmede not et. İleride çıkacak mevzuatın tanıyacağı hakların devri batıldır (m. 51).
- **Çalışan eseri:** özel sözleşmeden ya da işin mahiyetinden aksi anlaşılmadıkça memur, hizmetli ve işçilerin **işlerini görürken** meydana getirdikleri eserler üzerindeki haklar onları çalıştıranlarca kullanılır (m. 18/2). Kapsam ("işlerini görürken") tartışmaya açık olduğundan iş sözleşmesinde açık hüküm yine de öner. **Danışman ve serbest çalışan** bu kuralın dışındadır → açık, yazılı, hakları sayan devir şart (m. 52).
- **Zincir:** mali hakkı ya da ruhsatı devralan, onu ancak eser sahibinin **yazılı muvafakatiyle** başkasına devredebilir; işleme hakkında da aynı (m. 49). Tedarikçinin çalışanlarının ya da alt yüklenicilerinin eserleri bize gelecekse: tedarikçiden hak zinciri beyanı ve gerekli muvafakatler. m. 18/2 kapsamındaki eserlerde muvafakat gereğinin kapsamı **tartışmalı — içtihadı kontrol et.**
- **Manevi haklar:** umuma arz, adın belirtilmesi ve değişikliği men yetkisi eser sahibindedir (m. 14-16). Şeref ve itibarı zedeleyen yayımı ve eserin mahiyetini bozan değişikliği men yetkisinden sözleşmeyle vazgeçmek **hükümsüzdür** (m. 14/3, 16/3). "Manevi haklardan tam feragat" klozunun bu kısmı geçersizdir; yapılabilecek olan: adın belirtilmemesine, yayım zamanı/tarzına ve teknik değişikliklere yazılı izin + hakkı kullanmama taahhüdü — sınırını notta söyle.
- **Önceden var olan haklar (background):** karşı tarafın devir dışında tuttuğu liste somut mu, açık uçlu mu? Teslim edilen işin kullanılması için gereken ölçüde lisans var mı?

**Tasarım:** çalışanın işinde yaptığı tasarımda hak sahibi, aksi kararlaştırılmadıkça işverendir; hizmet ilişkisi dışındaki iş görme sözleşmelerinde hak sahipliği sözleşmeye göre belirlenir (SMK m. 73/1, 73/4) → danışman sözleşmesinde açık hüküm şart.

**Buluş:** çalışan buluşlarına ilişkin hükümler emredicidir; işveren çalışan aleyhine düzenleme yapamaz ve sözleşme serbestliği hizmet buluşunda patent başvurusundan sonra başlar (SMK m. 117/1; hizmet buluşu tanımı m. 113). İş sözleşmesindeki "tüm buluşlar şirkete aittir" klozunu bu çerçevede **`/ip-legal:invention-intake`** ile yürüt (bildirim, talep süreleri ve bedel orada). Danışmanın buluşunda sözleşme belirleyicidir — açık hüküm.

**Marka devri:** sınai haklara ilişkin hukuki işlemler yazılıdır; devir sözleşmesinin geçerliliği noter onayına bağlıdır (SMK m. 148/4). Sicile kaydedilmeyen işlemden doğan haklar iyiniyetli üçüncü kişilere karşı ileri sürülemez (m. 148/5).

Eksik ya da zayıfsa notun en üstüne:

```markdown
## ⚠️ DEVİR BOŞLUĞU
**Madde [X]** iş ürünündeki hakları devrediyor, ancak: [ör. "haklar ayrı ayrı sayılmamış (FSEK m. 52)" / "gelecekteki eserler 'şimdiden devredilmiştir' diye yazılmış (FSEK m. 48/3)" / "danışman sözleşmesinde devir hükmü yok" / "marka devri noter onaysız (SMK m. 148/4)"].
**Risk:** Yıllar sonra inceleme sürecinde çıkan türden bir boşluk; karşı tarafın ya da halefinin bizim sandığımız işte hakkı kalabilir.
**Önerilen redline:** > "[somut metin]"
**Eskalasyon:** profil gereği devir kapsamı boşlukları [onaylayan]'a gider.
```

**YZ ile üretilen içerik:** eser, sahibinin hususiyetini taşıyan ürün; sahibi onu meydana getiren kişidir (FSEK m. 1/B-a, b; m. 8). İnsan katkısı olmayan YZ çıktısının eser sayılıp sayılmadığı **tartışmalı** — devir yalnız var olan hakkı devredebilir. Danışman/geliştirici YZ kullanacaksa: YZ kullanım beyanı, bildirim yükümlülüğü ve YZ destekli kısımları ayırt edecek mekanizma var mı? Yoksa 🟠: "Devir klozu iyi ama YZ kullanım beyanı yok; YZ içeriğinin hak durumu belirsiz ve hangi kısmın etkilendiğini bilemezsiniz." `[review — YZ çıktısının eser niteliği gelişen bir alan; güncel içtihat ve doktrini kontrol et: tr_ictihat_ara(query="yapay zeka eser sahibi"), scholar_search_legal_scholarship]`. YZ'nin buluşa katkısı → `/ip-legal:invention-intake`.

### Adım 3: Kloz kloz inceleme

Aranacak klozlar: devir · teslim edilen işin sahipliği · geliştirmeler ve işlenmeler (FSEK m. 1/B-c işlenme eser) · önceden var olan/yeni haklar ayrımı · **lisans** (kapsam, münhasırlık, ülke, kullanım alanı, alt lisans, süre, fesih, bedel) · fikri mülkiyet garantileri (üçüncü kişi hakkını ihlal etmeme, yetki, özgünlük) · tazmin (kapsam, tavan, usul, istisnalar) · manevi haklar · açık kaynak beyanları (→ `/ip-legal:oss-review`) · marka kullanımı (kalite denetimi, kullanım rehberi) · gizlilik ve ticari sır (haksız rekabet tabanı TTK m. 55/1-d; NDA → `/commercial-legal:nda-review`).

**Türk hukukunda lisansa özgü kontroller:**
- **Dava hakkı:** sözleşmede aksi kararlaştırılmamışsa inhisari (münhasır) lisans alan, hak sahibinin açabileceği davaları kendi adına açabilir; münhasır olmayan lisans alan önce hak sahibinden dava açmasını ister, üç ay içinde açılmazsa kendi adına açabilir (SMK m. 158/1-2). Lisans veren tarafsak bu hakkı sınırlamak, alan tarafsak korumak isteriz.
- **Kapsam aşımı:** lisansla verilen hakları izinsiz genişletmek ya da üçüncü kişilere devretmek marka hakkına tecavüzdür (SMK m. 29/1-ç). Telifte ruhsat sahibi de hakkı ancak eser sahibinin yazılı muvafakatiyle devredebilir (FSEK m. 49).
- **Tescil:** sicile kaydedilmeyen lisans iyiniyetli üçüncü kişilere karşı ileri sürülemez (SMK m. 148/5).
- **Yazılım lisansı:** programı hukuka uygun edinen kişinin programı yüklemesi, çalıştırması, hataları düzeltmesi ve kullanım için gerekli bir yedek kopya alması sözleşmeyle önlenemez (FSEK m. 38/4) — bunları yasaklayan kısıt geçersizlik riski taşır.
- **Standart metin (genel işlem koşulu):** karşı tarafın önceden hazırladığı lisans/kullanım şartlarındaki aleyhe hükümler, açıkça bilgi verilip kabul edilmedikçe yazılmamış sayılır; sözleşmenin niteliğine yabancı olanlar da (TBK m. 21); dürüstlüğe aykırı aleyhe hüküm konulamaz (m. 25); "her madde tartışıldı" kaydı tek başına yetmez (m. 20/3).
- **Tazmin ("indemnity"):** Türk hukukunda ayrı bir kurum olarak değil sözleşmesel tazmin taahhüdü olarak yazılır; kapsam, bildirim süresi ve savunmayı kimin yöneteceği açık olmalı (ayrıntı: `/commercial-legal:vendor-agreement-review`).

Her kloz için:

```markdown
### [Madde X.X]: [Kloz adı]
**Ne diyor:** [bir-iki cümle]
**Piyasa / standart (bu tür, bu taraf, bu hukuk):** [kısa]
**Risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
**Neden önemli:** [olduğu gibi kalırsa iş için ne ters gider]
**Önerilen redline (gerekirse):** > "[somut metin]"
**Karar notu:** [kloz amaçlanan dağılımı sağlıyor mu belirsizse avukata işaretle, iki yönü göster]
```

| Seviye | Anlamı |
|---|---|
| 🔴 Kritik | Düzeltmeden imzalama. Olması gereken belgede devir yok; haklar sayılmamış (FSEK m. 52); gelecekteki eserde tasarım hatası; dar olması gereken lisans sınırsız; münhasır olmaması gereken münhasır. |
| 🟠 Yüksek | Güçlü ısrar, olmazsa eskalasyon. Belirsiz kapsam; manevi hak düzenlemesi yok ya da geçersiz feragat; hak zinciri beyanı yok; dar tazmin. |
| 🟡 Orta | İlk turda iste, son açık konuysa kabul. Kozmetik ama belirsiz dil; standarttan kısa süreler. |
| 🟢 Düşük | Not et, sermaye harcama. Dağılımı değiştirmeyen üslup farkı. |

### Adım 4: Çapraz tutarlılık

Fikri mülkiyet klozları sistem olarak bozulur: lisans verilen kapsamla uyumlu mu ("kullanma" lisansı "kullanma, değiştirme, işleme" lisansından dardır)? Garanti verilen her şeyi kapsıyor mu (yalnız patente sınırlı ihlal etmeme garantisi telif ve sırrı açıkta bırakır)? Tazmin garantinin vaat ettiğini kapsıyor mu? Fesih lisansı geri alıyor mu, bedeli ödenmiş lisans fesihten sonra sürüyor mu — niyetle uyumlu mu? SOW, sipariş formu ya da yan mektupla dağılım çelişiyor mu?

### Adım 5: Yargı çevresi notu

- **Hakkın kendisi** koruma talep edilen ülkenin hukukuna tabidir (MÖHUK m. 23/1); sözleşmenin hukuk seçimi hakkın varlığını ve kapsamını değiştirmez. Sözleşmeye uygulanacak hukuk ve yetki/tahkim için `/commercial-legal:governing-law-review`.
- **Türk hukuku kontrol listesi:** yazılı şekil ve hakların sayılması (FSEK m. 52) · gelecekteki eser (m. 48/3, 50) · manevi hak sınırı (m. 14/3, 16/3) · işçi eseri kuralı ve danışman ayrımı (m. 18/2) · marka devrinde noter onayı (SMK m. 148/4) · çalışan buluşlarının emredici rejimi (SMK m. 117). Örtülü lisans (yazılı hüküm sessizken kullanım izni çıkarımı) Türk hukukunda m. 52 karşısında **tartışmalı**.
- **Yabancı hukuk:** kuralı ezberden yazma; araç kullan — AB yazılım/telif: `eu_search_eu_law(query="legal protection of computer programs")`, `eu_search_eu_law(query="copyright related rights information society")`; Birleşik Krallık: `uk_search_legislation(title="Copyright, Designs and Patents Act")`; Almanya: `de_` araçları (ör. `de_gesetz_ara` ile UrhG). Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

Hangi hukukun uygulandığını ve profilin o yargı çevresini standart / eskalasyon / asla olarak işaretleyip işaretlemediğini yaz.

## Redline ayrıntı düzeyi

**En küçük birimde düzelt.** Bütün klozu değiştirmek "metninizi attık" demektir; cerrahi redline "belirli taleplerimiz var" der ve daha hızlı kabul edilir. Sıra: kelime → ifade → alt bent → cümle → kloz. Klozu tümden yeniden yazman gerekiyorsa iletim notunda söyle: "Değişiklikler kapsamlı olduğundan 8.2'yi işaretlemek yerine yeniden yazdık; farkı birlikte geçebiliriz."

### Adım 6: Notu birleştir

Notun başına `## Outputs` üst başlığını koy (role göre). Not ve sözleşme gizli olabilir; dar çevrede dağıt, dışarı göndermeden önce başlığı çıkar.

> **Sessiz tamamlama yok.** Araç bir kural için az sonuç döndürürse bulduğunu bildir ve dur; web ya da hafızadan sessizce doldurma. Seçenek: sorguyu genişlet, başka araç, `[web araması — doğrula]` etiketiyle web, ya da "doğrulanmadı" diye bırak.
>
> **Kaynak etiketi:** `[ArthurLegal TR — 5846 FSEK m. X — GG.AA.YYYY]`, araç adı, `[kullanıcı verdi]` (karşı taraf taslağı ya da büro dosyası), `[model bilgisi — doğrula]`, `[web araması — doğrula]`. Etiketleri silme; her madde `tr_mevzuat_madde_getir` ile çekilir, çekilemeyen için UYARI satırı.

```markdown
[ÜST BAŞLIK — profil ## Outputs]
# Fikri Mülkiyet Klozu İncelemesi: [Karşı taraf] [Sözleşme türü]
**İncelendi:** [tarih] · **Fikri haklarda tarafımız:** [veren / alan / ikisi] · **Uygulanacak hukuk:** [ ]
---
## Sonuç
[İki cümle. Dağılım ayakta kalır mı? Önce ne değişmeli?]
**Bulgular:** [N]🔴 [N]🟠 [N]🟡 [N]🟢 · **Onay gereken:** [profildeki isim]
## Devir boşluğu kontrolü
[✅ Temiz | ⚠️ Boşluk var — yukarıda]
## Önem sırasına göre klozlar
[Adım 3 blokları, Kritik → Düşük]
## Çapraz tutarlılık
## Yargı çevresi notu
## Onay yönlendirmesi
[profilden — kim onaylar, otomatik eskalasyonlar]
> ⚠️ **İnceleyen notu:** Bu not avukat incelemesi içindir; gelecekteki eser, manevi hak ve YZ çıktısı başlıklarındaki "tartışmalı" işaretleri imzadan önce kapatılmalıdır.
```

## Karar duruşu

Kloz fikri hakkı iki yönde de okunabiliyorsa ya da seçilen kelimelerin amaçlanan sonucu doğurup doğurmadığı belirsizse **avukata işaretle, iki yöndeki etkenleri göster.** İmzalanmış çözümsüz bir dağılım tek yönlü kapıdır; sonradan "sorun yokmuş" denilen bir işaret iki yönlü.

## Teslimden önce kalite kontrolü

- [ ] Profil yüklendi; yargı çevresi notu profille uyumlu
- [ ] İş/danışmanlık/SOW belgesinde önce devir boşluğu kontrol edildi (m. 52, 48/3, 50, 18/2, 49)
- [ ] Her 🔴 ve 🟠 için somut redline
- [ ] Çapraz tutarlılık kontrol edildi
- [ ] Atıflar etiketli ve doğrulanmış; `doğrula` etiketleri silinmedi
- [ ] Onaylayan profildeki isimle yazıldı ("hukuka eskale et" değil)
- [ ] Üst başlık eklendi

## Sonraki adım ağacı

`## Outputs`'taki sonraki adım ağacıyla kapat; seçenekleri bu çıktıya göre özelleştir (redline'ı yaz, eskale et, olgu topla, bekle-izle, başka bir şey). Ağaç çıktıdır; avukat seçer.

---

## /ip-legal:matter-workspace

---
name: matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Çok müvekkilli büro pratiğinde bir müvekkilin bağlamının
  (marka stratejisi, buluş içeriği, uygulama duruşu, karşı taraf bilgisi)
  diğerine sızmamasını sağlar. Matter oluşturmak, aktif matter'ı değiştirmek,
  listelemek, arşivlemek ya da uygulama düzeyine dönmek istendiğinde ya da başka
  bir skill hangi matter'da çalıştığını bilmek istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat ve vekil birçok müvekkil ve dosya üzerinde çalışır. Fikri mülkiyette bir müvekkilin marka adayı, buluş içeriği ya da uygulama planı başka bir dosyadaki müvekkilin rakibini ilgilendirebilir; matter çalışma alanı her dosyanın bağlamını ayrı tutar. Bu skill o alanları yöneten ince dosya katmanıdır.

**Varsayılan kapalıdır.** Şirket içi kullanıcı bunu hiç görmez; uygulama düzeyinde çalışır. Kurulumda büro seçen kullanıcıda açılır ya da `## Matter workspaces` elle düzenlenir.

## Alt komutlar

- `/ip-legal:matter-workspace new <slug>` — yeni matter, kısa ön görüşme, `matter.md`
- `/ip-legal:matter-workspace list` — durum ve aktiflik işaretiyle liste
- `/ip-legal:matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/ip-legal:matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/_archived/` altına taşı; asla silme)
- `/ip-legal:matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünü bul. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli şirket içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/ip-legal:cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/ip-legal:matter-workspace`'e ihtiyacınız yok."
2. `$ARGUMENTS`'ın ilk kelimesine göre aşağıdaki alt komut mantığına dallan.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context`, `none — practice-level context only` ve `matter.md` içindeki `## Matter-specific overrides` aynen kalır; diğer skill'ler ve ajanlar bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/ip-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
├── portfolio.yaml                  # portföy kaydı (uygulama düzeyi)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı; ör. cease-desist/, takedown/)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-marka-arastirma-2026`, `xyz-ihtarname`, `def-fto`. Müvekkilin gerçek adı yerine takma ad kullanılabilir. Aynı slug hem arşivde hem aktifte olamaz; arşivdeki `_archived/<slug>/` altında korunur.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Avukat; aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermişse ve kendi düzenlediği bir senet ya da sözleşmenin hükümsüzlüğünü ileri sürmek durumu ortaya çıkmışsa işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Fikri mülkiyette sık doğan örnekler: büronun başka bir müvekkil adına tescil ettirdiği markaya karşı hükümsüzlük ya da iptal talebi; büronun hazırladığı lisans/devir sözleşmesine karşı geçersizlik iddiası; aynı ya da benzer işaret için iki müvekkilin başvurusu. Sor: "Bu matter için çatışma kontrolü yapıldı mı?" (Hukuk Bürosu paketinde `/firm-operations:conflict-check`.) Bu skill çatışma kontrolünü kendisi yapmaz ve başka matter'ların dosyalarını bu amaçla okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz taraf (şirket içinde: iş birimi)
   - **Karşı taraf** — birden fazla olabilir; izleme bulgusuyla açılan dosyada "bilinmeyen üçüncü kişi"
   - **Matter türü** — marka araştırması | marka tescil/itiraz | marka ihlali ve ihtarname | içerik kaldırma (telif) | patent FTO | patent ihlali | fikri mülkiyet klozu incelemesi | açık kaynak uyumu | portföy bakımı | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (clean team; FTO ve buluş dosyalarında yaygın)
   - **Kritik tarihler** — bülten itirazı (yayımdan iki ay, SMK m. 18/1), ihtarnamedeki süre, menfi tespit için görüş talebine cevap süresi (bir ay, SMK m. 154/1), ceza şikâyeti (altı ay, TCK m. 73/1), yenileme tarihleri (`portfolio.yaml` ile eşleştir)
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, varsayılan duruştan farkı
   - **Matter'a özel sapmalar** — ör. "müvekkil bu marka için atak duruş istiyor", "karşı taraf stratejik kanal ortağı — yalnız ölçülü üslup", "buluşçu görüşmeye uygun değil — mülakat önerme"
   - **Dış vekil / avukat** — bu dosyada TÜRKPATENT işlemlerini yürüten kayıtlı vekil ya da dava avukatı (profildeki `Outside counsel roster`'dan)
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/ip-legal:matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar; tablo: Slug | Müvekkil | Matter türü | Durum | Açılış | Aktif. Aktif olanı `*` ile işaretle; `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

`matters/<slug>/matter.md` yoksa `new <slug>` öner. Varsa `Active matter: <slug>` yap ve doğru matter'da olduğunu teyit etmesi için `matter.md` özetini (gizlilik düzeyi ve kritik tarihler dahil) göster.

### `close <slug>` ve `none`

`close`: `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle, `matters/<slug>/` → `matters/_archived/<slug>/` taşı; kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap. Tescil dosyalarında kapatmadan önce sor: "Yenileme takibi `portfolio.yaml`'da sürüyor mu?" — fikri mülkiyet matter'ı tescille bitmez, yenilemelerle sürer. `none`: yalnız `Active matter:` satırını değiştirir; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar
**Müvekkil:** [ad]
**Karşı taraf:** [ad(lar) / bilinmeyen üçüncü kişi]
**Dış vekil / avukat:** [ad — rol]

## Matter türü
[tür — tek satır gerekçe]

## Kritik tarihler
- [bülten itirazı; ihtarname süresi; SMK m. 154 cevap süresi; şikâyet süresi; yenileme]

## Ana olgular
[2-5 cümle; varsayılan duruştan farkı]

## Matter-specific overrides
- [ör. "Enforcement posture: house varsayılanı atak olsa da burada ölçülü — karşı taraf ana kanal ortağı."]
- [ör. "Approval: her mektuptan önce pazarlama onayı da alınır."]
- [ör. "Kapalı ekip: çapraz bağlam açık olsa bile bu matter okunmaz."]

## İlgili matter'lar
- [slug — neden ilgili]

## Gizlilik notu
[Yüksek / kapalı ekipse nedeni; dosyaları kim görebilir; genel ayar açık olsa bile çapraz bağlama izin var mı]
```

Esaslı skill'ler (`/ip-legal:cease-desist`, `/ip-legal:takedown`, `/ip-legal:ip-clause-review` …) matter'a özel sapmaları bu başlıktan okuyup uygulama duruşunun önüne koyar; başlığı çevirme.

## `history.md` başlangıcı

`# Geçmiş: [Müvekkil] — [kısa tarif]` başlığı, "Yalnız ekleme yapılan olay günlüğü; en yeni üstte." notu ve tek girdi: `## [YYYY-AA-GG] — Matter açıldı` — "Ön görüşme tamamlandı. Slug: `[slug]`. Durum: aktif." artı matter.md dışında saklanmaya değer ilk bağlam (ör. "25. sınıfta izleme bulgusu üzerine açıldı.").

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurmama yükümlülüğünü (Av. K. m. 36) ve zıt menfaatli taraflardan doğan çatışma riskini (m. 38) destekler.

`on` iken bile yalnız kullanıcı açıkça isterse ("bu marka için gönderdiğimiz bütün ihtarnameleri matter'lar boyunca göster") çapraz okunur; varsayılan yine yalnız aktif matter'dır. Kapalı ekip matter'ında `## Gizlilik notu` çapraz okumayı yasaklıyorsa genel ayar açık olsa bile okunmaz. Kıyas çıktısında müvekkil adlarını anonimleştirmeyi öner.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil; kapalı matter'lar çatışma ve saklama amacıyla okunabilir kalır. Saklama süresi büronun/şirketin politikasıdır.
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Portföy kaydını taşımaz** — `portfolio.yaml` uygulama düzeyindedir; yenileme takibi `/ip-legal:portfolio`'dadır.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.

---

## /ip-legal:oss-review

---
name: oss-review
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

1. **Profili yükle:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Yer tutucu varsa dur: "Önce `/ip-legal:cold-start-interview` — pratik profilinizi (ve varsa açık kaynak politikanızı) öğrenmeliyim." Profil yüklü bir **OSS policy** gösteriyorsa onu da oku — kabul / inceleme / yasak lisanslar için tek doğru kaynak odur.
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
- **Hak zinciri:** kodu yazan çalışanların hakları m. 18/2 ile işverence kullanılıyor mu, dış katkıcılar (danışman, freelancer) yazılı ve hakları sayan devirle mi (FSEK m. 52) çalıştı? Eksikse yayımlamadan önce `/ip-legal:ip-clause-review`.
- Proje adı ve logosu için marka politikası (telif lisansından ayrı) — gerekirse `/ip-legal:clearance`.

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

---

## /ip-legal:portfolio

---
name: portfolio
description: >
  Fikrî mülkiyet portföyünü izler — tescil ve başvurular, marka ve tasarım
  yenilemeleri (SMK m. 23, m. 69), patent/faydalı model yıllık ücretleri
  (m. 101), kullanım denetimi (m. 9). Neyin yenileneceğine bakarken, varlık
  eklerken veya güncellerken, ödenen ücreti/yapılan yenilemeyi kaydederken ya
  da kaydı boşluk, sona erme ve kullanım soruları için denetlerken kullan.
  Başvuru ve clearance işlerinden devir alır.
argument-hint: "[--report [--days N] | --add | --update | --audit]"
---

# /portfolio — Portföy Kaydı

Yaklaşan süreleri gösterir, varlık ekler, yapılan işlemleri kaydeder, kaydı denetler.

## Talimat

1. Aşağıdaki akışı izle ve `~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml` oku.
2. **Argümansız:** `--report` ile aynı — önümüzdeki 90 günün süreleri, aciliyete göre (🔴 sona ermiş/ek sürede, ⏰ pencerede, 🟡 yaklaşan, 🌐 vekil yönetiminde, ❓ bilinmeyen).
3. **`--report [--days N]`:** Mod 2. Pencere `--days` ile (30 / 60 / 90 / 180). Üst başlığı `## Outputs`'tan koy; her raporu doğrulama satırıyla kapat.
4. **`--add`:** Mod 3. Yeni varlığı soru-cevapla ekle; yerleşik olmayan ülke için `custom_rules` yakala.
5. **`--update`:** Mod 4. Yapılan yenileme/ücret ödemesini kaydet, IPMS ile eşitle ya da durum değiştir. `filed` yazmadan önce sonuç doğuran işlem kapısını uygula.
6. **`--audit`:** Mod 5. Süre hijyeni, tescil boşlukları, kullanım denetimi (m. 9), sahiplik tutarlılığı, sona erme ufku, izlenmeyen markalar.
7. **Kayıt boşsa ve IPMS bağlıysa** Mod 1'i öner: portföyü kayıt sisteminden çek, kaydı başlat.
8. **Korkuluk:** hesaplanan süreler yalnız referanstır. Her çıktı TÜRKPATENT sicilinden ya da ilgili ofisten teyit satırıyla biter. Yanlış girilmiş süre, girilmemiş süreden kötüdür: sahte güven yaratır. IPMS eşitlenmiş değilse kullanıcının bu kaydı "kayıt sistemi" gibi kullanmasına izin verme.

## Örnekler

```
/ip-legal:portfolio
/ip-legal:portfolio --report --days 180
/ip-legal:portfolio --add
/ip-legal:portfolio --update
/ip-legal:portfolio --audit
```

## Bağlantıyla daha iyi çalışır

- **IP yönetim sistemi (IPMS) MCP ile** — Anaqua, Clarivate IPfolio, AppColl, Patrix, Alt Legal, FoundationIP. Tam dosya listesi, ücret takvimleri ve gelen yazışmalar tek yerde olur. Bağlayıcı için IPMS sağlayıcınıza sorun ya da depo kökündeki `CONNECTORS.md`'ye bakın.
- **TÜRKPATENT doğrudan:** ArthurLegal MCP'de TÜRKPATENT aracı **yoktur** (resmî uç çalışmıyor). Durum ve tarihleri TÜRKPATENT web sitesindeki sicil/araştırma ekranlarından ve EPATS'tan elle teyit edin; pratik için `references/turkpatent-rehberi.md`.

İkisi de yoksa dosya listenizi yapıştırın ya da tablo yükleyin; oradan izlerim.

## Amaç

Süresinde yenilenmeyen marka ve tasarımın hakkı sona erer (SMK m. 28/1-a, m. 69/6). Yıllık ücreti ödenmeyen patent vade tarihi itibarıyla sona erer (m. 101/4, m. 140/1-c). Süresi geçen alan adı dakikalar içinde kapılabilir. Hepsi önlenebilir; tek şartı doğru sürenin, doğru numaraya ve doğru ülkeye bağlı olarak birinin takviminde olmasıdır. Bu skill o takvimi tutar.

## Önemli: süre referansı uyarısı

> Bu skill'in uyguladığı kurallar her çalıştırmada `tr_mevzuat_madde_getir` ile çekilen SMK metnine dayanır; yabancı ülke kuralları ancak araçla çekilip `custom_rules`'a kaynağıyla yazıldığında hesaplanır. Ofis uygulamaları, ek süreler ve **ücret tutarları değişir — güncel ücret tarifesini teyit et** (TÜRKPATENT ücret tarifesi dönemsel güncellenir). **İşlem yapmadan önce her hesaplanan süreyi TÜRKPATENT sicilinden, WIPO Madrid Monitor'den, EUIPO'dan ya da ilgili ulusal ofisten elle teyit edin** (ArthurLegal'da bu siciller için araç yok). Anaqua, CPA Global, Clarivate, Alt Legal gibi bir IPMS kullanıyorsanız varlıklarınız için onun takvimi esastır; bu kayıt onu düzenler, yerine geçmez.
>
> "Yakında süre yok" çıktıları ikinci bir bakışı özellikle hak eder.

## Ülke ve tür kuralları (çekilen maddelerden)

**Türkiye — marka (m. 23, m. 9):**
- Koruma süresi **başvuru tarihinden** itibaren 10 yıl; onar yıllık dönemlerle yenilenir (m. 23/1). (Başlangıç tescil tarihi değil, başvuru tarihidir.)
- Yenileme talebi ve ücretin ödendiği bilgisi, koruma süresinin bittiği tarihten önceki **altı ay** içinde; yapılmazsa bitişten itibaren **altı ay** içinde **ek ücretle** (m. 23/2). Kısmi yenileme mümkün (m. 23/3); yenileme önceki sürenin bittiği günü izleyen günden hüküm doğurur (m. 23/5).
- Yenilemede eksik ödenen ücret için Kurum ayrıca bildirim yapmaz — m. 161/3'teki eksik ücret bildirimi m. 23 ve m. 69'u kapsam dışı bırakır. Tutarı ödemeden önce teyit et.
- Beyan/kullanım belgesi sunma takvimi yoktur; ama tescilden itibaren beş yıl içinde Türkiye'de ciddi kullanılmayan ya da kullanımına beş yıl ara verilen marka talep üzerine iptal edilebilir (m. 9/1, m. 26/1-a); kullanım iptal talebinden önce başlarsa talep reddedilir, ancak talepten önceki üç aydaki "talep düşünülerek" yapılmış kullanım sayılmaz (m. 26/4). Kullanım; ayırt edici karakteri değiştirmeyen farklı unsurlarla, yalnız ihracat amacıyla ya da izinli kullanımı da kapsar (m. 9/2-3). Bu yüzden 5. yıl bir **kullanım denetimi** kilometre taşıdır, dosyalama süresi değil.
- Yenilenmeyen markada: süresi bittikten sonraki iki yıl içinde başkasının aynı/benzer başvurusuna, o sürede kullanılmışsa itiraz edilebilir (m. 6/8).

**Türkiye — Madrid uluslararası tescili (m. 14):** Türkiye'yi belirleyen uluslararası başvuru, Kuruma doğrudan yapılmış başvuruyla aynı sonucu doğurur (m. 14/1). Uluslararası tescilin yenilenmesi WIPO'da yürür; ArthurLegal'da Madrid/WIPO kaynağı yok → `agent_managed: true`, WIPO Madrid Monitor'den elle teyit.

**Türkiye — tasarım (m. 69):** tescilli tasarım başvuru tarihinden itibaren 5 yıl; beşer yıllık dönemlerle toplam **25 yıla** kadar (m. 69/1). Yenileme pencereleri markayla aynı: bitişten önceki altı ay, sonra ek ücretle altı ay (m. 69/4). Yenilenmeyen tasarım hakkı süre bitiminde sona erer (m. 69/6). Tescilsiz tasarım: ilk kamuya sunmadan itibaren **3 yıl**; yalnız bitiş tarihi izlenir (m. 69/2).

**Türkiye — patent ve faydalı model (m. 101):**
- Süre başvuru tarihinden patentte **20**, faydalı modelde **10** yıl; uzatılamaz (m. 101/1). Patent hükümleri, çelişmedikçe faydalı modele uygulanır (m. 145/1).
- **Yıllık ücret:** başvuru tarihinden itibaren ikinci yılın sona erdiği tarihte ve sonra her yıl vadesinde; vade, başvuru tarihine tekabül eden ay ve gündür (m. 101/2).
- Vadede ödenmezse **ek ücretle altı ay** (m. 101/3). O da geçerse hak **vade tarihi itibarıyla** sona erer ve bildirim yapılır; bildirimden itibaren **iki ay** içinde telafi ücretiyle yeniden geçerlilik kazanır (m. 101/4). Bu telafi süresi için "işlemlerin devam ettirilmesi" talep edilemez (m. 107/4). Yeniden geçerlilikte üçüncü kişilerin kazanılmış hakları saklıdır (m. 101/5).
- Diğer kaçırılmış süreler için hakların yeniden tesisi: süreye uyulamama nedeninin kalkmasından itibaren iki ay, en geç sürenin bitiminden bir yıl, özen gösterilmiş olması şartıyla (m. 107/2).

**Yabancı ofisler — kuralı ezberden hesaplama.** Araçla çek, `custom_rules`'a `source` alanıyla yaz:
- AB markası ve topluluk tasarımı: `eu_get_document_text(celex="32017R1001")` (AB Marka Tüzüğü), `eu_get_document_text(celex="32002R0006")` + değişiklik `32024R2822` (topluluk tasarımları).
- Birleşik Krallık marka yenilemesi: `uk_get_section(year="1994", number="26", section="43")`.
- Almanya marka süresi ve yenileme: `de_norm_getir(kanun="MarkenG", norm="47")`.
- Diğer ülkeler (ABD dahil), EPO yıllık ücretleri, WIPO: "ArthurLegal'da kaynak yok" → `agent_managed: true`, yerel vekile teyit.

**Alan adları:** kayıt kuruluşunun bitiş tarihini kaydet; ek süre ve geri alma kuralları kayıt kuruluşuna göre değişir — kayıt kuruluşundan teyit et (ArthurLegal'da araç yok).

**Telif:** yenileme takvimi tutulmaz. Süre ya da kayıt sorusu varsa `tr_mevzuat_madde_getir(number="5846", ...)` ya da `/ip-legal:takedown`.

## Kayıt

`~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml`:

```yaml
# IP Portfolio Register
# Generated: [date]
# Last updated: [date]
# Disclaimer: hesaplanan süreler yalnız referanstır — işlem öncesi TÜRKPATENT sicili /
# WIPO / ilgili ofis ya da IPMS kayıt sisteminden teyit edin. Ücret tutarlarını teyit edin.

metadata:
  company: "[Müvekkil]"
  generated: "[date]"
  last_updated: "[date]"
  last_audit: "[date or null]"
  source_system: "[Anaqua / CPA Global / manual / none]"

custom_rules:   # yerleşik olmayan ülkeler — her kural araçla çekilen kaynağıyla
  []            # ör. {jurisdiction: "UK", type: "trademark", rule: "...", source: "TMA 1994 s.43 — uk_get_section — GG.AA.YYYY"}

assets:
  - id: "TM-TR-001"
    type: "trademark"                          # trademark / patent / utility_model / copyright / design / domain
    jurisdiction: "TR"
    mark_or_title: "[Marka ya da başlık]"
    owner: "[Sicildeki sahip — tescilli unvan]"
    status: "registered"                       # pending / registered / lapsed / abandoned / cancelled
    application_number: "[no veya null]"
    registration_number: "[no veya null]"
    classes: ["9", "42"]                       # TM için Nis; patent için IPC/CPC; diğerlerinde null
    filing_date: "[YYYY-MM-DD]"                # TR markada koruma süresi buradan işler (m. 23/1)
    registration_date: "[YYYY-MM-DD or null]"  # kullanım denetimi (m. 9/1) buradan işler
    priority_date: "[YYYY-MM-DD or null]"
    grant_date: "[YYYY-MM-DD or null]"         # patent
    next_deadlines:                            # hesaplanır; --report ve --audit'te tazelenir
      - type: "Yenileme"
        due_date: "[filing_date + 10 yıl]"
        grace_end: "[due_date + 6 ay — ek ücretli]"
        basis: "SMK m. 23/1-2 — pencere due_date'ten 6 ay önce açılır"
        action: "Yenileme talebi + ücret ödeme bilgisi (tutarı teyit et)"
        status: "upcoming"                     # upcoming / due_soon / overdue / grace / lapsed / filed
    use_in_commerce: true                      # yalnız TM — m. 9 kullanım denetimini besler
    agent_managed: false                       # yabancı vekil / dış büro yönetiyorsa true
    local_agent: null
    docket_id: "[IPMS kimliği veya null]"
    outside_counsel: "[büro veya null]"
    business_owner: "[e-posta ya da ekip]"
    notes: ""

  - id: "PAT-TR-001"
    type: "patent"
    jurisdiction: "TR"
    mark_or_title: "[Buluş başlığı]"
    owner: "[Sahip]"
    status: "granted"
    application_number: "[no]"
    registration_number: "[patent no]"
    filing_date: "[YYYY-MM-DD]"
    grant_date: "[YYYY-MM-DD]"
    priority_date: "[YYYY-MM-DD or null]"
    expiration_date: "[filing_date + 20 yıl; faydalı modelde + 10]"   # m. 101/1
    next_deadlines:
      - type: "Yıllık ücret — [N]. yıl"
        due_date: "[başvuru tarihine tekabül eden ay/gün]"
        grace_end: "[due_date + 6 ay — ek ücretli]"
        restoration_end: "[sona erme bildirimi + 2 ay — telafi ücreti; bildirim gelmeden null]"
        basis: "SMK m. 101/2-4"
        action: "Yıllık ücreti öde (tutarı teyit et)"
        status: "upcoming"
    claims_count: 20
    entity_size: null                          # TR'de kullanılmaz; yabancı ofis indirimi varsa doldur
    docket_id: null
    outside_counsel: null
    business_owner: null
    notes: ""
```

`next_deadlines` durumları:
- `upcoming` — 90 günden uzak
- `due_soon` — 90 gün içinde, yapılmadı
- `overdue` — asıl tarih geçti, ek süre içinde (varsa)
- `grace` — ek süre penceresinde (açık bayrak — **ek ücret** doğar: m. 23/2, m. 69/4, m. 101/3)
- `lapsed` — ek süre işlemsiz geçti; hak sona ermiş sayılır. Patentte `restoration_end` doluysa telafi penceresi açıktır (m. 101/4) — en yüksek aciliyet
- `filed` — bu dönemin işlemi yapıldı

## Mod 1: Başlatma

Kayıt yoksa ya da `--rebuild` ile.

**Adım 1 — Kaynak.** Ayarı oku: IPMS bağlıysa portföyü oradan çek (esas kaynak odur; bu kayıt yansıtır, onun bilmediği süre eklemez). IPMS yok ama dışa aktarım varsa iste; tescil/veriliş tarihi eksik varlığı `unknown` işaretle. Hiçbiri yoksa varlıkları tek tek sor.

**Adım 2 — Süreleri hesapla.** Önce `tr_mevzuat_madde_getir(number="6769", madde_no=["9","23","26","69","101","107","145","161"])` ile kuralları çek; değişiklik dipnotu varsa uygula. Her varlık için en yakın iki üç süreyi `next_deadlines`'a yaz; on yıllık yenilemeler gibi uzak süreleri raporda istendiğinde hesapla. Kuralı bilinmeyen ülke → `custom_rules` taslağı + `agent_managed: true` + yabancı vekile teyit TODO. Gerekli tarih eksik → `next_deadlines` boş, `notes`'a neden, özet listesinde `unknown`.

**Adım 3 — Yaz ve özetle:**

```
Portföy kaydı başlatıldı.
Varlıklar: [N] — Marka [N] ([N] tescilli / [N] başvuru) · Patent/FM [N] · Tasarım [N] · Telif [N] · Alan adı [N]
Hesaplanan süre: [N]
Vekil yönetiminde / ülke kuralı teyitsiz: [N] — yabancı vekillere teyit ettirin
Bilinmeyen (tarih eksik): [N] — raporlara güvenmeden önce tamamlayın
Ne zaman ne var: /ip-legal:portfolio --report
```

## Mod 2: Rapor

`/ip-legal:portfolio --report [--days 30|60|90|180]` — varsayılan 90 gün. Raporlamadan önce her varlığın süresini yeniden hesapla; kayıtlı tarihe tek başına güvenme. Üst başlık `## Outputs`'tan.

```
FİKRÎ MÜLKİYET PORTFÖYÜ SÜRE RAPORU — [tarih]
[Müvekkil] — pencere: önümüzdeki [N] gün

🔴 SONA ERMİŞ / EK SÜREDE ([N])
  [ID] / [Ülke] / [Tür] / [Marka ya da başlık]
    [İşlem] — asıl tarih [tarih], ek süre sonu [tarih] [patentte: telafi sonu [tarih]]
    Durum: [grace / lapsed]

⏰ [N] GÜN İÇİNDE ([N])
  [ID] / [Ülke] / [Tür] / [Marka ya da başlık]
    [İşlem] — son gün [tarih]  (yenileme penceresi açılış: [tarih])
    Dayanak: [ör. "SMK m. 23/2"]
    [Vekil: büro / dosya: kimlik — varsa]

🟡 YAKLAŞAN (30 günden sonra, [N] gün içinde)
🌐 VEKİL YÖNETİMİNDE ([N]) — [ID] / [Ülke] — [vekil] yönetiyor; doğrudan teyit edin
❓ BİLİNMEYEN ([N]) — [ID] — [alan] eksik; hesaplanamıyor

ÖZET: izlenen varlık [N] · penceredeki süre [N] · son denetim [tarih]
```

Kapanış satırı: *"Portföy kaydından hesaplandı. Ödeme ya da işlemden önce her süreyi ve ücret tutarını TÜRKPATENT sicili / WIPO / ilgili ofis kaydından teyit edin."*

Rapor ~10'dan fazla varlık listeliyorsa ya da kullanıcı isterse `## Outputs → Dashboard offer for data-heavy outputs` uyarınca pano öner: duruma göre sayılar (yürürlükte / ek sürede / sona ermiş / başvuru), süre zaman çizelgesi, ülke-tür-sonraki işlem tarihine göre sıralanabilir tablo.

## Mod 3: Ekleme

Sor: (1) tür, (2) ülke, (3) marka/başlık, (4) sicildeki sahip (devir ve yenileme için önemli), (5) tarihler (başvuru, tescil, veriliş, rüçhan, bitiş), (6) numaralar, (7) sınıflar/istem sayısı, (8) IPMS dosya kimliği, (9) dış büro / yabancı vekil, (10) iş sahibi (ürün hattı, marka yöneticisi). Süreleri hesapla; ülke yerleşik değilse `custom_rules` akışı; `assets:`'e ekle.

**Özel kural yakalama:**
> [Ülke] / [tür] için yerleşik kuralım yok; ArthurLegal aracıyla çekebiliyorsam çekip kaynağıyla yazarım, çekemiyorsam sizden alırım:
> 1. Hangi bakım olayları var (N yılda yenileme, yıllık ücret, kullanım beyanı)?
> 2. Süre neyle başlar (başvuru, tescil, veriliş, ulusal aşama)?
> 3. Ek süre var mı, maliyeti?
> 4. Yöneten yabancı vekil kim?

`custom_rules`'a kaynak alanıyla kaydet; kaynağı kullanıcı beyanıysa `source: "kullanıcı beyanı — teyitsiz"` yaz.

## Mod 4: Güncelleme

### Sonuç doğuran işlem kapısı

Yenilemeyi ya da ücret ödemesini kaydetmeden önce `## Who's using this` oku. Rol **avukat değilse**:

> Bir yenilemeyi ya da yıllık ücreti "yapıldı" (`filed`) diye kaydetmenin sonucu var. Kayıt yanlışsa — süre kaçmış, ücret eksik, yanlış dönem — süre yerinden oynamaz ve hak yine sona erebilir; yenilemede eksik ücret için Kurum ayrıca bildirim de yapmaz (SMK m. 161/3). İşlemi yapan avukat, marka/patent vekili ya da yabancı vekille veya TÜRKPATENT sicilinden teyit ettiniz mi? Evetse devam ediyorum. Hayırsa:
> - Henüz `filed` kaydetmeyin.
> - Avukata götürün: varlık kimliği, ülke, süre türü, IPMS'in gösterdiği, ne zaman ne yapıldığını düşündüğünüz ve bu bilginin kaynağı.
> Avukat için bağlı olduğunuz baroya başvurabilirsiniz; Kurum nezdinde işlemleri sicile kayıtlı marka/patent vekilleri de yapar (m. 160/1).

Açık "evet" olmadan hiçbir süreyi `filed` yapma. Durum tazeleme, rapor ve yaklaşan süre gösterimi kapı gerektirmez.

**Elle güncelleme:** "TM-TR-001'in yenilemesini 4 Mart'ta yaptık." → eşleşen süre `status: filed`, `filed_date`; yaşam döngüsündeki sonrakini hesapla (yenilemede sonraki 10 yıllık bitiş; patentte sonraki yıllık ücret).
**IPMS eşitleme:** son dosya listesini çek, karşılaştır; kayıt sistemi kazanır; kaydın bilip sistemin bilmediğini göster (terk, devir kaydı ya da veri hatası olabilir).
**Durum değişikliği:** "TM-TR-004 terk edildi." → `status` güncelle, `next_deadlines` temizle, tarihi not et. Devirde: devir sözleşmesi yazılı ve noter onaylı olmalı; sicile kaydedilmeyen işlem iyiniyetli üçüncü kişilere karşı ileri sürülemez (m. 148/4-5) — sicil kaydını sor.

## Mod 5: Denetim

**Süre hijyeni** — şu an `grace`'te olanlar (ek ücret işliyor); `lapsed` olup `abandoned`/`cancelled` işaretlenmemişler (patentte telafi penceresi açık mı?); `next_deadlines` hesaplanmamış varlıklar.
**Tescil boşlukları** (pratik eşikler, hukuki süre değil) — 18 aydan uzun süredir `pending` marka başvuruları; 4 yıldan uzun süredir `pending` patent başvuruları → ofiste durum kontrolü.
**Kullanım (yalnız TM, m. 9)** — tescilinin 5. yılını geçmiş ya da yaklaşan ve `use_in_commerce: false`/belirsiz markalar → kullanım delili derlemesi; iptal riski (m. 26/1-a), itirazda (m. 19/2) ve tecavüz davasında (m. 29/2) kullanım ispatı talebine açıklık.
**Sahiplik** — aktif olmayan tüzel kişi adına kayıtlı varlıklar (devir kaydı gerekebilir); aynı kişinin farklı yazılmış unvanları.
**Sona erme ufku** — önümüzdeki 24 ayda bitecek patent/faydalı modeller ve son 5 yıllık dönemindeki tasarımlar (25 yıl sınırı: m. 69/1) — ürün planlama, lisans penceresi.
**İzlenmeyen varlıklar** — `## Brand protection` izleme listesinde olmayan tescilli markalar; listeye alıp almama avukatın kararı.

```
PORTFÖY DENETİMİ — [tarih]
SÜRE HİJYENİ: ek sürede [N] · sona ermiş (işaretsiz) [N] · hesaplanmamış [N]
TESCİL BOŞLUKLARI: TM başvuru >18 ay [liste] · patent başvuru >4 yıl [liste]
KULLANIM (TM, m. 9): 5. yıl eşiğinde belirsiz kullanım [liste]
SAHİPLİK: tanınmayan sahip [N] · unvan tutarsızlığı [liste]
SONA ERME UFKU (24 ay): [liste]
MARKA İZLEME: izlemede olmayan tescilli markalar [liste]
ÖNERİLEN EYLEMLER: 1. [en yüksek öncelik] 2. [...]
```

## Entegrasyon: ip-renewal-watcher ajanı

`ip-renewal-watcher` ajanı bu skill'i zamanlamayla (varsayılan haftalık) çalıştırır ve Mod 2 raporunu ayarda `Renewal alerts` satırındaki kanala gönderir. 🔴 kalem (ek süre / sona ermiş) varsa zamanlamayı beklemeden hemen gönderir.

## Devirler

- **Alır:** başvuru işlerinden (başvuru yapıldığında), `/ip-legal:clearance`'tan (marka benimsenip başvuru sıraya girdiğinde), `/ip-legal:invention-intake`'ten (başvuru yapıldığında), devir kayıtlarından.
- **Gönderir:** avukata "şimdi yenile/öde" uyarısı — bu skill işlem yapmaz; süreyi ve gerekenleri söyler.

## Bu skill ne yapmaz

- Hiçbir şey dosyalamaz, ücret ödemez; her işlemi avukat ya da vekil yapar.
- Süreleri TÜRKPATENT, WIPO ya da başka sicilden doğrulamaz; verdiğiniz tarihlerden ve çekilen maddelerden hesaplar. Kayıt çalışma kopyasıdır; sicil esastır.
- Yenileyip yenilememeye karar vermez — marka hâlâ kullanılıyor mu, patent hâlâ değerli mi, alan adı hâlâ önemli mi iş kararıdır.
- Yüzlerce varlıklı portföyde IPMS'in yerini tutmaz.
- Ofis kaydını okuyup durumu teyit etmez; burada `filed` görünen bir yenileme, biri öyle söylediği içindir — Kurumun kabul ettiğini değil. Kabulü sicilden ya da IPMS'ten teyit edin.

---

## /ip-legal:takedown

---
name: takedown
description: >
  İnternetteki telif ihlali için içerik kaldırma: bilgi içerik sağlayıcısına
  başvuru ve ihlal sürerse Cumhuriyet savcısı aracılığıyla servisin durdurulması
  (FSEK ek m. 4/3), uyarı yöntemi (5651 m. 2/1-r) ve platform bildirimi (--send);
  size gelen kaldırma talebinin triyajı (--respond); içeriğiniz kaldırıldıysa
  itiraz ya da karşı bildirim taslağı (--counter). ABD DMCA mekanizmasının
  yerini alır; yabancı platform ve AB DSA notları araca yönlendirilir.
argument-hint: "<--send | --respond | --counter> [bağlam ya da gelen bildirimin yolu]"
---

# /takedown — İçerik kaldırma (telif)

- `/ip-legal:takedown --send` — FSEK ek m. 4/3 başvurusu ve platform bildirimi; istisna kapısı + teslimden önce kapı.
- `/ip-legal:takedown --respond` — size gelen kaldırma talebini triyaj: uy / itiraz et / görüş / bırak.
- `/ip-legal:takedown --counter` — içeriğiniz kaldırıldıysa itiraz ya da karşı bildirim; teslimden önce kapı.
- Bayrak yoksa bir kez sor: "Kaldırma talebi mi gönderiyoruz, gelen bir talebi mi değerlendiriyoruz, yoksa kaldırılan içeriğimiz için itiraz mı hazırlıyoruz?"

## Talimat

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Yoksa ya da `[PLACEHOLDER]` varsa dur: "Önce `/ip-legal:cold-start-interview` çalıştırın — bu skill onay matrisinize ve pratik profilinize dayanır."
2. **Matter:** `## Matter workspaces` → `Enabled` `✗` ise atla; açık ve aktif matter yoksa sor ("`/ip-legal:matter-workspace switch <slug>` ya da `practice-level`"). Çıktılar `matters/<matter-slug>/takedown/<slug>/` (uygulama düzeyinde `takedown/<slug>/`); `Cross-matter context` `on` değilse başka matter okunmaz.
3. **Bağlam:** `## IP practice profile`, `## Enforcement posture` → `Approval matrix` → `DMCA takedown (ordinary)` satırı (Türkiye'de bu satır her türlü içerik kaldırma bildirimini kapsar — FSEK ek m. 4 başvurusu, platform bildirimi, yabancı DMCA bildirimi; satır adı çevrilmez), `## Who's using this`, `## Outputs`.
4. **Kapılar:** `--send` ve `--counter`'da teslimden önce kapı her seferinde çalışır. `--send`'deki istisna kapısı daha önce çalışır; kullanım bir kanuni istisnaya "olabilir" ya da "muhtemelen" giriyorsa taslağı durdur, avukata yönlendir.
5. **Yargı çevresi:** içerik, platform ya da ihlal eden Türkiye dışındaysa taslaktan önce işaretle (aşağıda "Yabancı platform ve AB").

## Destination check

Giden bildirim ve itiraz karşı tarafa/platforma gider; üst başlık taşımaz ve bir hukuki süreç içindeki beyandır, gizli değildir. İç taslak, istisna analizi ve triyaj notu `## Outputs` üst başlığını taşır. Platform formuna yapıştırılan metin çoğu zaman karşı tarafa iletilir — kişisel veri ve strateji içermesin. Kanonik kural: `## Shared guardrails → Destination check`.

## Türk hukuku çerçevesi

**ABD'deki tek kanunlu "notice-and-takedown" (DMCA §512) sisteminin Türkiye'de birebir karşılığı yoktur.** Yollar:

1. **FSEK ek m. 4/3 — telifin kanuni yolu.** Servis ve bilgi içerik sağlayıcılar tarafından dijital iletim dahil araçlarla eser sahibi ya da bağlantılı hak sahibinin hakları ihlal edilirse, hak sahibinin başvurusu üzerine eser içerikten çıkarılır:
   - **Aşama 1:** hakkı zedelenen kişi önce **bilgi içerik sağlayıcısına** başvurur ve **üç gün** içinde ihlalin durdurulmasını ister.
   - **Aşama 2:** ihlal devam ederse **Cumhuriyet savcısına** başvurulur; savcılık üzerinden **servis sağlayıcıdan**, ihlale devam eden içerik sağlayıcıya verilen hizmetin üç gün içinde durdurulması istenir. İhlal durunca hizmet yeniden verilir. Uygulama ayrıntıları Bakanlık yönetmeliğindedir — güncel yönetmeliği `tr_mevzuat_ara(query="fikir ve sanat eserleri", search_in="title")` ile bul (yönetmelik türü KKY ya da YONETMELIK olabilir) ve çek.
   - Ek m. 4/1'deki hak yönetim bilgisini kaldırma fiilleri ile hakları ihlale devam eden bilgi içerik sağlayıcılar için ayrıca ceza hükmü vardır (FSEK m. 71 son fıkralar); şikâyete bağlıdır (m. 75), şikâyet süresi altı ay (TCK m. 73).
2. **5651 — uyarı yöntemi ve sağlayıcı sorumluluğu.** Kanun "uyarı yöntemi"ni tanımlar: hakkı ihlal edildiğini iddia eden kişi içeriğin yayından çıkarılması için önce içerik sağlayıcıya, makul sürede sonuç alınamazsa yer sağlayıcıya iletişim adresleri üzerinden bildirimde bulunur (5651 m. 2/1-r). İçerik sağlayıcı sunduğu içerikten sorumludur (m. 4/1); yer sağlayıcı içeriği kontrol etmek ya da araştırmakla yükümlü değildir (m. 5/1) ve yayından çıkarma yükümlülüğü m. 8 ve 9'a göre haberdar edilmesine bağlanmıştır (m. 5/2).
   - **Dikkat:** 5651 m. 9 Anayasa Mahkemesi kararıyla **iptal edilmiştir** (madde metnindeki not: AYM 11/10/2023, E. 2020/76, K. 2023/172) — yürürlükte gibi atıf yapma. Telif ihlali için yer sağlayıcıya 5651'den doğrudan yükümlülük yükleme; telifte dayanak FSEK ek m. 4'tür.
   - Özel hayatın gizliliği ihlalinde ayrı yol vardır (5651 m. 9/A: Siber Güvenlik Başkanlığına başvuru, sulh ceza hâkimi onayı) — telif yolu değildir.
   - Günlük erişimi bir milyonu aşan sosyal ağ sağlayıcının **48 saat** içinde gerekçeli cevap yükümlülüğü yalnız m. 9 ve 9/A içeriklerine ilişkin başvurular içindir (ek m. 4/3); telif bildirimi bu kapsamda değildir. m. 9 iptal edildiğinden yollamanın kapsamı **tartışmalı**. 7578 sayılı Kanunla ek m. 4'te yapılan değişiklikler ve yeni ek m. 5 **1/11/2026'da** yürürlüğe girer (RG 1/5/2026, sayı 33240) — o tarihten sonra metni yeniden çek.
3. **Mahkeme yolu:** ihtiyati tedbir (FSEK m. 77; dava açılmadan önce de), tecavüzün ref'i (m. 66) ve men'i (m. 69), tazminat (m. 68, 70); görevli mahkeme FSHHM (FSEK m. 76/1).
4. **Platform bildirimi (uygulama):** pazaryeri, video ve sosyal ağ platformlarının kendi telif/IP formları. Hukuki dayanak değil, kullanım koşulu sürecidir; çoğu zaman en hızlı yoldur ve FSEK ek m. 4 yoluna paralel yürür.

Her madde atfı `tr_mevzuat_madde_getir` ile çekilir (5846 ek 4: `madde_no="ek 4"`; 5651: `madde_no=["2","4","5"]`). İçtihat: `tr_ictihat_ara(courts=["YARGITAYKARARI"], query="+FSEK +\"ek 4\" +içerik")` — dönen künyeyi birebir kullan.

## Gönderme modu (--send)

### Adım 1: Eser ve hak

> - **Eser:** nedir (yazılım, görsel, metin, video, ses)? Sahibinin hususiyetini taşıyor mu (FSEK m. 1/B-a)?
> - **Sahiplik:** kim meydana getirdi (m. 8)? Çalışan eseriyse haklar kural olarak işverence kullanılır (m. 18/2) — sözleşmeyi kontrol et. Devralındıysa sözleşme yazılı ve haklar ayrı ayrı gösterilmiş mi (m. 52)?
> - **Başvuru yetkisi:** ek m. 4/3 başvuruyu "hakları haleldar olan" kişiye tanır. Münhasır olmayan ruhsat sahibinin başvurup başvuramayacağı **tartışmalı** — lisans sözleşmesine bak; şüphede hak sahibinden yetki ya da ortak başvuru al.
> - **Önceki izinler:** bu kullanıma ya da daha genişine hiç izin, lisans (Creative Commons dahil) verildi mi?

Kayıt-tescil şart değildir; varsa ispatı kolaylaştırır (m. 13/son).

### Adım 2: İhlal eden içerik ve yeri

Platform/site · tam URL'ler (her içerik için kalıcı bağlantı) · içerik sağlayıcı kim (5651 m. 2/1-f), yer sağlayıcı kim (m. 2/1-m) · nasıl ihlal ediyor (birebir kopya, işleme, izinsiz umuma iletim — FSEK m. 21-25) · delil: URL ve zaman görünür ekran görüntüleri; içerik kaybolabilecekse delil tespiti (HMK m. 400).

### Adım 3: İstisna kapısı (ABD "fair use" kapısının yerine)

Türk hukukunda ABD'deki gibi genel ve esnek bir "fair use" ölçütü yoktur; serbest kullanımlar FSEK'te tek tek düzenlenmiştir. Taslaktan önce sor:

> Bu kullanım bir kanuni istisnaya giriyor olabilir mi?
> - **İktibas** (m. 35): alenileşmiş eserden cümle/fıkra alıntısı, ilim eserinde aydınlatma amaçlı alıntı — iktibas belli olmalı, kaynak gösterilmeli.
> - **Eğitim** (m. 33 yüz yüze eğitimde kâr amaçsız temsil; m. 34 eğitim amaçlı seçme ve toplama eserler).
> - **Şahsi kullanım** (m. 38/1: kâr amaçsız şahsen kullanmaya mahsus çoğaltma — hak sahibinin meşru menfaatine haklı sebepsiz zarar vermemek ve normal yararlanmaya aykırı olmamak şartıyla).
> - **Bilgisayar programında kullanıcı hakları** (m. 38/3-7: amaca uygun kullanım, yedek kopya, gözlem-tetkik, araişlerlik).
> Değerlendirmeniz: istisna **olası değil / tartışmalı / olası**?

Cevabı dosyaya yaz. **Tartışmalı ya da olası ise taslak yazma:** "Bu olgularda istisna tartışmalı. Kanunen serbest bir kullanıma kaldırma talebi göndermek, aşağıdaki kapıdaki sorumlulukları doğurur. Önce avukata." İstisnaların kapsamının yorumu **tartışmalı — içtihadı kontrol et.**

### Adım 4: İyiniyet kontrolü

Dört soru, dördü de evet olmalı: eser bizim ya da başvuru yetkimiz var · kullanım izinli değil (lisanslar, izinler, CC lisansı kontrol edildi) · istisna kapısı yürütüldü ve sonucu kayıtta · içerik doğrudan incelendi (yalnız bir ihbara dayanılmadı). Biri hayırsa dur.

### Adım 5: Yetki ve imza

Kim kimin adına başvuruyor, yetki belgesi (vekâletname, yetki yazısı) var mı?

### Adım 6: Taslak

**Aşama 1 — içerik sağlayıcıya başvuru (FSEK ek m. 4/3) ve uyarı yöntemi bildirimi:**
1. Başvuranın kimliği ve iletişim bilgisi (vekil varsa vekâlet)
2. Eserin tanımı ve hak dayanağı (sahiplik/devir/ruhsat; tescil varsa numara)
3. İhlal eden içerik: URL'ler, kısa tarif, nasıl ihlal ettiği
4. Talep: ihlalin **üç gün** içinde durdurulması ve içeriğin yayından çıkarılması
5. Beyan: bilgilerin doğru olduğu ve başvuranın hak sahibi ya da onun adına yetkili olduğu
6. Tarih, imza
Kanal: içerik sağlayıcının iletişim adresi, KEP ya da noter (tarih ispatı); platform kullanıyorsa platformun formu paralel. Sonuç alınamazsa yer sağlayıcıya aynı içerikle bildirim (5651 m. 2/1-r).

**Aşama 2 — Cumhuriyet savcılığına başvuru** (ihlal sürerse): Aşama 1 başvurusu ve tebliğ belgesi, sürenin dolduğu, ihlalin devam ettiğine dair güncel delil, servis sağlayıcıdan hizmetin durdurulması talebi. Ceza şikâyeti de yapılacaksa bunu ayrı ve açık yaz; süre altı ay (TCK m. 73).

### Adım 7: Teslimden önce kapı

```
┌─────────────────────────────────────────────────────────────┐
│  BU KALDIRMA TALEBİ BİR YERE GİTMEDEN ÖNCE                   │
├─────────────────────────────────────────────────────────────┤
│  Kaldırma talebi yargı denetimi olmadan içerik indirtebilir; │
│  rutin bir idari adım değildir:                              │
│  • Savcılığa, işlenmediğini bildiği bir ihlali isnat etmek   │
│    iftira suçunu oluşturabilir (TCK m. 267).                 │
│  • Lisanslı, başkasına ait ya da kanunen serbest kullanıma   │
│    karşı talep: kötüleme/haksız rekabet (TTK m. 55/1-a-1,    │
│    56), hakkın kötüye kullanılması (TMK m. 2), tedbir        │
│    alınırsa haksız tedbir tazminatı (HMK m. 399).            │
│  Gitmeden önce teyit edin:                                   │
│    1. Eser bizim ya da başvuru yetkimiz var.                 │
│    2. Kullanım izinli değil — lisanslar ve izinler tarandı.  │
│    3. İstisna kapısı yürütüldü; sonuç kayıtta.               │
│    4. İmza yetkisi olan kişi gönderimi onayladı.             │
│  Onaylayan: [Approval matrix → DMCA takedown (ordinary)]     │
│  Otomatik eskalasyonlar: [profilden]                         │
└─────────────────────────────────────────────────────────────┘
```

Kullanıcı avukat değilse ekle: "Kaldırma talebi, özellikle savcılık aşaması, sorumluluk doğurur. Hukuki mütalaa ve takip avukatlara aittir (Av.K. m. 35/1). Bir avukatla gözden geçirdiniz mi? Görüşme için kısa brif: [eser, sahiplik, ihlal eden kullanım, lisans kontrolü, istisna analizi, imzalayan, platform]. Avukat bulmak için ilinizin barosuna başvurabilirsiniz." Kapıyla açık etkileşim olmadan nihai çıktıyı yazma.

### Adım 8: Çıktı

- **Asıl:** `<matter-klasörü>/takedown/<slug>/notice-v<N>.md` (platform formuna yapıştırmaya ya da KEP/noter ile göndermeye hazır metin; hangi kanalın beklendiğini yaz). Önce sohbette düz metin.
- **İnceleyen notu** (yalnız sohbette): "⚠️ Bu, avukat incelemesi için kaldırma talebi taslağıdır; gönderilmeye hazır değildir."
- **Atıf etiketleri:** `[ArthurLegal TR — 5846 FSEK ek m. 4 — GG.AA.YYYY]`, `[kullanıcı verdi]`, `[model bilgisi — doğrula]`; sessiz tamamlama yok.
- **Gönderim kaydı** `submission.md`: kanal (adres, form, KEP/noter), tarih, onay numarası, hedef URL'ler, **üç günlük süre sonu**, Aşama 2 hazırlığı, delil koruma.

## Alma modu (--respond) — size gelen talebin triyajı

### Adım 1: Oku

Gönderen (kim, imzalayan, iletişim) · hangi mekanizma: içerik sağlayıcı olarak size doğrudan FSEK ek m. 4 başvurusu mu, savcılık yazısı mı, hâkim kararı mı, platformun kendi süreci mi, yabancı platformda DMCA bildirimi mi · iddia edilen eser · hedef içeriğiniz (URL) · tarih · bildirimde eksik var mı (eser, URL, hak dayanağı, yetki).

### Adım 2: Değerlendir

Lisansımız var mı (sözleşme, CC, önceki uzlaşma, devir)? Kanuni istisna (m. 33-35, 38)? Gönderen gerçekten hak sahibi mi? Bildirim eksik mi? Savcılık ya da hâkim kararıysa — usul ve itiraz yolu avukatındır; süreleri hemen çıkar. Gönderen aşırı ve toplu talep gönderen biri mi?

### Adım 3: Seçenekler

- **A — Uy (kaldırma kalsın):** haklılar ya da değmez. Bedel: içerik kapalı kalır, hesap uyarıları, gelir kaybı. Adım: kaydet.
- **B — İtiraz / karşı bildirim:** lisans, istisna ya da hak sahipliği itirazı güçlü. Adım: `/ip-legal:takedown --counter`.
- **C — Gönderenle görüş:** lisans, atıf, daha dar kaldırma. İçerik görüşme sürerken kapalı kalabilir. Uzlaşma yazışmalarında başlık tek başına koruma sağlamaz.
- **D — Bırak, ayrıca ele al:** zarar küçük; talep haksızsa haksız rekabet (TTK m. 55-56) ya da haksız fiil tazminatı kendi takviminizle ayrı uyuşmazlıktır.

Birini iki cümle gerekçeyle öner.

### Adım 4: Triyaj notu

Çıktı: `<matter-klasörü>/takedown/inbound/<slug>/triage.md`.

```markdown
[ÜST BAŞLIK — profil ## Outputs]
[GİZLİLİK BLOĞU — /ip-legal:cease-desist alma modundaki gibi role göre]
# İçerik Kaldırma Talebi — Triyaj
> **GÖRÜŞ DEĞİL, TRİYAJ.** Esasa ilişkin karar avukatındır.
**Slug:** · **Tarih:** · **Mekanizma:** [FSEK ek m. 4 başvurusu / savcılık / hâkim kararı / platform / yabancı DMCA] · **Platform:** · **Dosya:**
## Talep
**Gönderen:** · **İddia edilen eser:** · **Hedef içeriğimiz:** · **Bildirimdeki eksikler:**
## Değerlendirme
**Lisans/izin:** · **Kanuni istisna (m. 33-35, 38):** `[avukat teyidi]` · **Gönderenin hak sahipliği:** · **Gönderenin güvenilirliği:**
## Seçenekler
### A. Uy ### B. İtiraz / karşı bildirim ### C. Görüş ### D. Bırak
**Öneri:** [harf] — [iki cümle] — `[avukat teyidi gerekli]`
## Süreler
[platformun itiraz süresi; savcılık/hâkim kararına itiraz süresi — avukat belirler; ilgili sözleşme süreleri]
## Hemen yapılacaklar
- [ ] Eser ve içeriğimizle ilgili delil koruma · [ ] İş etkisi (gelir, hesap uyarıları) · [ ] Matter · [ ] Sorumlu avukat
```

Kapanış: "Bu bir triyaj notudur, görüş değildir; bildirimin dört köşesinden ilk okumadır. İtiraz etmeden ya da cevapsız bırakmaya karar vermeden önce avukat değerlendirir."

## İtiraz modu (--counter)

**Türk hukukunda DMCA §512(g) benzeri kanuni bir karşı bildirim mekanizması yoktur.** Bu mod, kaldırmanın türüne göre doğru belgeyi hazırlar:
- **Platform süreciyle kaldırıldıysa:** platformun itiraz formu için itiraz metni.
- **Hak sahibinin doğrudan başvurusuyla (FSEK ek m. 4/3) içeriği siz kaldırdıysanız:** gönderene cevap → `/ip-legal:cease-desist --send` (cevabi ihtarname).
- **Savcılık ya da hâkim kararıyla kaldırıldıysa:** itiraz yolu ve süresi avukatındır; bu skill yalnız olgu ve delil özetini hazırlar.
- **Uyuşmazlığı kesin çözmek gerekiyorsa:** tecavüz olmadığının tespiti için tespit davası (HMK m. 106) — dış avukata eskale, taslak yok.
- **Yabancı platformda DMCA bildirimiyle kaldırıldıysa:** karşı bildirim ABD hukukudur ve kaynak kitapçığın ABD çerçevesine göre ABD federal mahkemelerinin yargı yetkisine rıza beyanı içerir. ArthurLegal'da ABD mevzuat kaynağı yoktur (kuruluysa CourtListener bağlayıcısı içtihat için); ABD'de yetkili bir avukattan görüş al.

### Adım 1: Ön şartlar

İçerik hangi mekanizmayla kaldırıldı (yukarıdaki dallanma)? Kaldırmanın hata ya da yanlış tespit olduğuna dair iyiniyetli ve delilli bir kanaat var mı (lisans, istisna, ihlal yok, gönderen hak sahibi değil)? Karar bilinçli mi verildi, avukat devrede mi?

### Adım 2: Platform itiraz metni

1. Kimlik ve iletişim · 2. Kaldırılan içerik ve kaldırılmadan önceki URL · 3. Kaldırma bildiriminin tarihi/numarası · 4. Kaldırmanın neden hatalı olduğu ve delili (lisans belgesi, istisna gerekçesi, hak zinciri) · 5. Beyanların doğruluğu beyanı · 6. Tarih, imza.

### Adım 3: Teslimden önce kapı

```
┌─────────────────────────────────────────────────────────────┐
│  BU İTİRAZ BİR YERE GİTMEDEN ÖNCE                            │
├─────────────────────────────────────────────────────────────┤
│  • İtiraz metni ve kimlik bilgileriniz çoğu zaman talebi     │
│    gönderene iletilir.                                       │
│  • İçerik geri gelirse hak sahibi ihtiyati tedbir (FSEK      │
│    m. 77) ve dava yoluna gidebilir; itiraz davadan önceki    │
│    son adımdır.                                              │
│  • Gerçeğe aykırı beyan sorumluluk doğurur.                  │
│  Teyit edin:                                                 │
│    1. Kaldırma mekanizması belirlendi (platform / FSEK ek    │
│       m. 4 / savcılık / hâkim / yabancı DMCA).               │
│    2. Hata kanaati iyiniyetli ve delilli.                    │
│    3. Dava ihtimaline bütçe, avukat ve risk iştahı hazır.    │
│    4. Gönderilmeden önce avukat inceledi.                    │
│  Onaylayan: [Approval matrix — itirazlar genellikle          │
│  DMCA takedown (ordinary) satırının üstüne yönlenir]         │
└─────────────────────────────────────────────────────────────┘
```

Kullanıcı avukat değilse: "Bu adım lisanslı mesleki muhakeme ister (Av.K. m. 35/1); Claude incelemesi bunun yerini tutmaz. Brif: [tek sayfa]. Avukat için ilinizin barosu." Açık etkileşim olmadan çıktıyı yazma.

### Adım 4: Çıktı

`<matter-klasörü>/takedown/<slug>/counter-notice-v<N>.md`; sohbette önce düz metin; inceleyen notu: "⚠️ Avukat incelemesi için itiraz taslağı; gönderilmeye hazır değildir." Gönderim sonrası `counter-submission.md`: platform, tarih, onay no, platformun karar süresi, içerik geri gelirse plan, dava/tedbir gelirse plan.

## Yabancı platform ve AB

- **AB:** çevrim içi platformlarda bildirim ve işlem usulü — `eu_get_document_text(celex="32022R2065")` (Dijital Hizmetler Tüzüğü; bildirim ve işlem, şikâyet sistemi hükümlerini metinden oku); içerik paylaşım platformlarının telif sorumluluğu — `eu_get_document_text(celex="32019L0790")` (Dijital Tek Pazarda Telif Direktifi; ilgili madde ve üye devlet iç hukuku). Kuralı ezberden yazma; metinden alıntıla.
- **Diğer ülkeler:** ArthurLegal'da kaynak varsa ilgili önekle ara (`uk_`, `de_`, `nl_`…); yoksa "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

## Karar duruşu

`## Decision posture on subjective legal calls` gereği: kullanımın istisnaya girip girmediği, hak sahibinin biz olup olmadığı, eserin gerçekten bizim olup olmadığı belirsizse sessizce karar verme. İstisna değerlendirmesi tipik belirsiz karardır; avukata işaretle, etkenleri göster. Varsayımla kaldırma talebi ya da itiraz göndermek tek yönlü kapıdır.

## Bu skill ne yapmaz

- **Göndermez** — kullanıcı platform, KEP, noter ya da savcılık kanalından gönderir.
- **İstisnaya karar vermez** — kanuni istisnaları yürütür, işaretler; avukat karar verir.
- **Kapıyı atlamaz** — `--send` ve `--counter`'da her seferinde çalışır.
- **Atıf uydurmaz** — etiketli ve doğrulanmış; sessiz tamamlama yok.
- **Yabancı rejimi Türk hukuku gibi uygulamaz** — DMCA, DSA ve diğerleri için işaretler ve araca/yerel hukukçuya yönlendirir.
