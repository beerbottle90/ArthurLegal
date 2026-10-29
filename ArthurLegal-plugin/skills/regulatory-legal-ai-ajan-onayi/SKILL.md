---
name: regulatory-legal-ai-ajan-onayi
description: >
  Yapay zekâ ajanı ya da yapay zekâ uygulaması canlıya çıkmadan önce hukuk onayı incelemesi
  (KVKK'nın terimiyle etken yapay zekâ ve YZ aracısı). Bir iş birimi ya da müvekkil şirket e-posta
  yanıtlayan, kayıt güncelleyen, müşteriyle konuşan veya çok adımlı iş yürüten bir ajan kullanmak
  istediğinde: özerklik basamağını belirler, altı asgari şartı denetler, KVKK, tedarikçi sözleşmesi
  ve AB bağlantısı varsa AI Act taramasını yapar, getiri iddiasını tartar; Uygun, Şartlı uygun,
  Pilotla sınırlı ya da Uygun değil kararıyla not üretir. Tetikleyiciler: "bu ajanı onaylayalım mı",
  "AI ajanı hukuk kontrolü", "yapay zekâ aracı canlıya çıkacak", "agentic AI onayı".
argument-hint: "[ajan ne yapacak, hangi verilere ve araçlara erişecek, tedarikçi, kimler etkilenecek]"
user-invocable: true
---

# Yapay Zekâ Ajanı Canlıya Çıkış İncelemesi

## Felsefe

Prototip kurmak kolaydır; zarar ve maliyet canlıda doğar. Bu skill, ajan canlıya çıkmadan önce aynı
asgari denetimi her seferinde uygular; böylece her yeni ajan sıfırdan bir hukuk projesine dönüşmez.
Özerklik arttıkça denetim de artar: yalnız öneri sunan bir yardımcı ile müşteriye kendi başına yazan
bir ajan aynı onayla geçmez. Karar her durumda insanındır; skill avukat incelemesi için yapılandırılmış
malzeme üretir.

Okunacak resmî belgeler (başlık, tarih ve adres 07.10.2026'da görüldü):
1. KVKK Kurumu, "Etken Yapay Zekâ (Agentic AI)", Şubat 2026 (sitede 12.03.2026):
   https://www.kvkk.gov.tr/Icerik/8683/etken-yapay-zeka-agentic-ai
2. KVKK Kurumu, "Üretken Yapay Zekâ ve Kişisel Verilerin Korunması Rehberi (15 Soruda)", 24.11.2025:
   https://www.kvkk.gov.tr/Icerik/8547/uretken-yapay-zeka-ve-kisisel-verilerin-korunmasi-rehberi-15-soruda

Bu belgeler bağlayıcı mevzuat değildir; Kurumun bakışını gösterir. Notta içeriklerine dayanılacaksa
o sohbette okunur, okunamazsa UYARI satırı yazılır.

## Ne zaman

Bir iş birimi ya da müvekkil şirket yapay zekâ destekli bir aracı veya ajanı gerçek veriyle ve gerçek
kullanıcılarla çalıştırmak istediğinde; çalışan bir ajanın yetkisi, veri kaynağı ya da tedarikçisi
değiştiğinde; tedarikçi sözleşmesi imzalanmadan önce. Soru yalnız kişisel veri işlemeyse
`/arthurlegal:privacy-legal-use-case-triage` yeterlidir; yalnız sözleşme incelemesi isteniyorsa
`/arthurlegal:commercial-legal-saas-msa-review` ya da `/arthurlegal:commercial-legal-vendor-agreement-review`.

## Girdi (eksikse sor, uydurma)

1. Görev: ajan ne yapacak; tek cümle ve bir örnek iş akışı.
2. Erişim: veri kaynakları (e-posta, müşteri kayıtları, dosya sunucusu, insan kaynakları sistemi, web),
   hesaplar ve araçlar; okuma mı yazma mı; gönderme, ödeme ya da silme yetkisi var mı.
3. Etkilenenler: çalışanlar, müşteriler, tüketiciler, başvuru sahipleri; AB'de bulunan kişiler var mı.
4. Karar: ajanın çıktısı bir insana öneri mi, yoksa doğrudan sonuç mu doğuruyor.
5. Tedarikçi ve model: kim sağlıyor, nerede barındırılıyor; sözleşme ve veri işleme eki elde mi.
6. Sahip: iş birimindeki sorumlu (rolüyle) ve teknik sorumlu.
7. Getiri: tedarikçinin ya da iş biriminin tasarruf veya getiri iddiası, varsa kaynağıyla.

Spesifik ajan, sözleşme ve veri envanteri knowledge'da yoktur; kullanıcıdan iste.

## Adımlar

### 1. Özerklik basamağı

Ajanı beş basamaktan birine yerleştir; emin değilsen üsttekini seç. Basamak, sonraki adımlarda
denetimin yoğunluğunu belirler.

| Basamak | Ne yapar | Asgari insan gözetimi |
|---|---|---|
| 1. Sohbet asistanı | Soruya cevap verir; çıktıyı insan okur ve kullanır | Kullanım kuralı ve eğitim |
| 2. Öneren yardımcı | Taslak ya da öneri sunar; insan kabul eder | Her çıktıda insan kabulü |
| 3. Araç kullanan ajan | Sınırlı yetkiyle işlem yapar (kayıt günceller, mesaj gönderir) | Yetki sınırı, işlem kaydı, geri alma yolu |
| 4. Çok adımlı iş akışı | Adımları zincirler, yeniden dener, başka ajanlara iş verir | Tanımlı onay noktaları, durdurma imkânı, adım adım kayıt |
| 5. Kendi başına çalışan ajan | Uçtan uca yürütür; kişiler hakkında sonuç doğurabilir | Basamak 4'e ek olarak düzenli insan denetimi ve olay planı |

Basamak 5'te ajan kişiler hakkında insan incelemesi olmadan sonuç doğuruyorsa sonuç en iyi ihtimalle
Şartlı uygun'dur.

KVKK'nın etken yapay zekâ belgesi, insan gözetiminin hangi koşullarda ve hangi aşamada devreye
gireceğinin açıkça tanımlanmasını öne çıkarır. Notta üç aşamayı ayrı ayrı yanıtla:
- geliştirmede ajanın erişebileceği veri türleri ve verebileceği kararlar tanımlanıp sınandı mı;
- kullanıma almada yüksek riskli işlemler için ek insan incelemesi kuruldu mu;
- kullanımdan sonra davranış izleniyor mu.

### 2. Altı asgari şart

Her şart için durum yaz: karşılanıyor, kısmen, karşılanmıyor ya da bilinmiyor. "Bilinmiyor" kalan bir
şart varken sonuç Şartlı uygun'un üstüne çıkmaz.

1. Güvenilir kaynak: ajan yalnız onaylı veri kaynaklarına mı erişiyor; özel nitelikli kişisel veri,
   ticari sır ya da avukat ile müvekkil yazışması bu kaynaklara karışıyor mu.
2. Belli sahip: ajanı kim günceller, kim onaylar, sorun çıkınca kim durdurur; geliştirici, tedarikçi ve
   ajanı kullanan kuruluş (KVKK belgesinin terimiyle yerleştirici, AI Act'te deployer) arasında görev,
   yetki ve sorumluluk yazılı mı.
3. En az yetki: hesaplar ve araçlar görev için gerekenden geniş mi; okuma ile yazma, gönderme, ödeme ve
   silme yetkileri ayrı mı; ajan kendi yetkisini genişletebiliyor mu.
4. Kaynağa izlenebilir çıktı: ajanın vardığı sonuç hangi kayda veya belgeye dayandığını gösteriyor mu;
   uydurma bir çıktı sonraki adımda girdi olarak kullanılıp hatayı büyütebiliyor mu.
5. Temel izleme: kalite, hata ve olay kaydı tutuluyor mu, ne kadar saklanıyor, kim bakıyor; veri
   ihlali fark edilince bildirim yolu belli mi.
6. Maliyet takibi: kullanım ve harcama iş akışı başına izleniyor mu; harcama sınırı var mı; ücret
   kullanıma bağlıysa beklenmedik artışa karşı sözleşmede sınır var mı.

Ajan dışarıdan gelen içeriği (e-posta, web sayfası, yüklenen belge) okuyorsa ayrıca sor: o içerikteki
yönergelerin talimat sayılmaması ve böyle bir girdiyle ajanın yetkisini aşamaması nasıl sağlanıyor.
KVKK belgesi, girdilerin manipüle edilmesiyle hassas bilginin ifşa edilebileceğini ve güvenlik
kısıtlarının aşılabileceğini ayrıca sayar.

### 3. Hukuki tarama

Aşağıdaki madde haritası 07.10.2026'da `tr_mevzuat_madde_getir` ve `eu_get_document_text` ile çekildi;
yalnız hangi maddenin çekileceğini gösterir. Nota yazmadan önce her maddeyi o sohbette yeniden çek ve
sistem talimatındaki madde doğrulama kapısından geçir.

**KVKK (6698)**
- Rol: tedarikçi veri işleyen mi, veri sorumlusu mu (m. 3/1-ğ ve ı). Tedarikçi veriyi kendi amaçları
  için (örneğin model eğitimi) kullanıyorsa rol değişebilir; değerlendirme avukatındır.
- İlke ve şart: amaçla bağlantılı, sınırlı ve ölçülü işleme (m. 4); işleme şartı (m. 5); özel nitelikli
  veri (m. 6, 7499 sayılı Kanunla değişik). KVKK belgesi, etken sistemlerde amacın ve kullanılan verinin
  süreç içinde genişleyebildiğini, başta dayanılan işleme şartının sonradan genişleyen kullanımı
  karşılamayabileceğini vurgular. Ajanın görev tanımını ve veri listesini yazılı olarak sabitle.
- Yurt dışına aktarım: model ya da altyapı yurt dışındaysa m. 9 (7499 sayılı Kanunla yeniden yazıldı)
  sırayla şunları arar:
  1. yeterlilik kararı;
  2. o yoksa uygun güvence (standart sözleşme, bağlayıcı şirket kuralları, taahhütname);
  3. o da yoksa yalnız arızi istisnalar.

  Standart sözleşme Kurulun ilan ettiği metinle, değiştirilmeden kullanılır ve beş iş günü içinde
  Kuruma bildirilir (Kanun m. 9/5). Yönetmelik bu sürenin imzaların tamamlanmasından başladığını
  söyler (Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik,
  RG 10.07.2024/32598, m. 14). Yönetmelik m. 16/1 arızi aktarımı düzenli olmayan ve süreklilik arz
  etmeyen aktarım olarak tanımlar. Sürekli çalışan bir ajan hizmeti için bu istisnaya dayanmadan önce
  avukat değerlendirmesi şarttır.
- Aydınlatma: verinin kimlere ve hangi amaçla aktarılabileceği dâhil (m. 10). Aydınlatma metni ajanı
  ve tedarikçiyi kapsıyor mu?
- Otomatik sonuç: ilgili kişi, verilerinin münhasıran otomatik sistemlerle analizi sonucu aleyhine
  çıkan sonuca itiraz edebilir (m. 11/1-g). Ajan kişiler hakkında sonuç doğuruyorsa itirazın kime ve
  nasıl yapılacağı ve insan incelemesi tanımlanmalı.
- Güvenlik: teknik ve idari tedbirler, veri işleyenle müşterek sorumluluk, ihlalin en kısa sürede
  ilgili kişiye ve Kurula bildirimi (m. 12). Yaptırım: m. 12'ye ve m. 9/5'teki bildirim yükümlülüğüne
  aykırılık idari para cezasına bağlıdır (m. 18). Tutar her yıl yeniden değerlenir; notta tutar yazma.
- Etki değerlendirmesi: KVKK belgesi, uygun durumlarda veri koruma etki değerlendirmesi gibi araçlardan
  yararlanılmasını önerir. Gerekiyorsa `/arthurlegal:privacy-legal-use-case-triage`, sonra `/arthurlegal:privacy-legal-pia-generation`.

**Tedarikçi sözleşmesi**

Ayrıntılı inceleme için `/arthurlegal:commercial-legal-saas-msa-review` ya da `/arthurlegal:commercial-legal-vendor-agreement-review`;
veri işleme eki için `/arthurlegal:privacy-legal-dpa-review`. Bu skill şunlara bakar:
- Girdiler ve çıktılar model eğitiminde kullanılacak mı; saklama ve silme süresi ne.
- Alt işleyenler ve barındırma ülkeleri kimler; yurt dışı aktarım mekanizması ne.
- Güvenlik, ihlal bildirim süresi ve denetim hakkı var mı.
- Hizmet düzeyi tanımlı mı; tedarikçinin pazarlamada vaat ettiği performans sözleşmeye ölçülebilir
  biçimde girmiş mi.
- Sorumluluk sınırı:
  - Borçlunun ağır kusurundan önceden sorumsuzluk anlaşması kesin hükümsüzdür (TBK m. 115/1).
  - Kanun ya da yetkili makam izniyle yürütülen uzmanlık işlerinde hafif kusur için de aynı kural
    geçerlidir (TBK m. 115/3).
  - Tedarikçinin yardımcı kişilerinin (alt yüklenicilerinin) fiillerinden sorumluluğu sözleşmeyle
    kaldırılmış mı (TBK m. 116)?
- Yabancı hukuk ya da yabancı tahkim seçilmişse `/arthurlegal:commercial-legal-governing-law-review`.

**AB bağlantısı varsa** (ajanın çıktısı AB'de kullanılıyor, AB'deki kişiler etkileniyor ya da AB'de
faaliyet var)
- Kapsam: AB dışında yerleşik uygulayıcı da, sistemin çıktısı AB'de kullanılıyorsa AI Act kapsamındadır
  (Regulation (EU) 2024/1689 m. 2(1)(c)). Ajanı kendi yetkisi altında kullanan kuruluş uygulayıcıdır
  (deployer, m. 3(4)).
- Takvim (07.10.2026 itibarıyla, Regulation (EU) 2026/1744 değişiklikleriyle):
  - Yasak uygulamalar (m. 5) ve yapay zekâ okuryazarlığı (m. 4) uygulanıyor. 2026/1744 sonrası m. 4,
    personelin okuryazarlığının gelişimini destekleme yükümlülüğüdür; belirli bir düzeyi garanti etmeyi
    gerektirmez.
  - Şeffaflık yükümlülükleri (m. 50) 2 Ağustos 2026'dan beri uygulanıyor.
  - Ek III'teki yüksek riskli sistemler için uygulayıcı yükümlülükleri (m. 26) ve temel haklar etki
    değerlendirmesi (m. 27) 2 Aralık 2027'den itibaren uygulanacak. Sözleşme süresi bu tarihi aşıyorsa
    şimdiden planla.
- Yüksek risk ihtimali: işe alım, terfi, fesih, görev dağıtımı, çalışan performansının ve davranışının
  izlenmesi (Ek III, 4) ile gerçek kişilerin kredi değerliliği (Ek III, 5(b)) yüksek riskli alanlardır.
  Ajan bu işlere dokunuyorsa m. 26 yükümlülükleri şunlardır:
  - talimata uygun kullanım;
  - yetkin ve yetkili kişilere verilmiş insan gözetimi;
  - girdi verisinin amaca uygunluğu;
  - izleme ve olay bildirimi;
  - otomatik kayıtların en az altı ay saklanması;
  - işyerinde kullanmadan önce çalışanların ve temsilcilerinin bilgilendirilmesi.
- Şeffaflık:
  - Kişilerle doğrudan etkileşen sistemde yapay zekâyla konuşulduğunun bildirilmesi, sağlayıcının
    tasarım yükümlülüğüdür (m. 50(1)).
  - Uygulayıcının bildirim yükümlülükleri duygu tanıma, biyometrik sınıflandırma, derin sahte içerik
    ve kamuoyunu bilgilendirme amaçlı yapay metinde doğar (m. 50(3) ve 50(4)).
- GDPR: AB'deki kişiler hakkında yalnız otomatik işlemeye dayanan ve hukuki sonuç doğuran kararlarda
  m. 22 (Regulation (EU) 2016/679).

**Kamu kurumu ise:** Türkiye Yapay Zekâ Eylem Planı (2026-2030) hakkındaki 2026/9 sayılı Genelge
(RG 18.08.2026/33344) kamu kurum ve kuruluşlarına görev verir; özel sektöre doğrudan yükümlülük
getirmez. Planın kendisi ayrıca yayımlanır; okunamazsa UYARI satırı yazılır.

**Sektör ve iç kurallar:** bankacılık, sermaye piyasası, sigorta, sağlık ve enerji kuralları ile
kuruluşun kendi yapay zekâ politikası ayrıca kontrol edilir; kurum kararları `tr_kurum_karari_ara` ile
aranır. Ajan çalışanları etkiliyorsa işyeri kullanım politikası için `/arthurlegal:employment-legal-policy-drafting`.

### 4. Getiri iddiası

Tedarikçi ya da iş birimi bir getiri veya tasarruf rakamı sunuyorsa sor:
- Rakamı kim ölçtü; tedarikçinin ısmarladığı bir çalışma mı?
- Hangi ürün ve hangi iş için ölçüldü?
- Bu kuruluşa uyarlanabilir mi?

Öneri: geniş çıkıştan önce tek bir iş akışında sınırlı bir pilot. Ölçü birimi iş başına süredir
(doğrulama süresi dâhil); kalite hep aynı örneklerle denetlenir. Kalite düşüyorsa zaman kazancı kazanç
sayılmaz. İddia karar için önemliyse sözleşmeye ölçülebilir hizmet düzeyi olarak yazdırılması önerilir.

### 5. Karar

Bulguları sistem talimatındaki dört kademeyle derecelendir (Bloklayıcı, Yüksek, Orta, Düşük) ve şu
dört sonuçtan birini ver:

1. Uygun: basamak 1 ya da 2, altı şart karşılanıyor, Bloklayıcı veya Yüksek bulgu yok.
2. Şartlı uygun: koşul listesiyle; her koşulun sahibi ve son tarihi yazılır. Koşul karşılanmadan canlıya
   çıkılmaz.
3. Pilotla sınırlı: dar kapsam, sınırlı kullanıcı, belirli süre ve ölçüm planıyla; pilot sonunda yeniden
   inceleme yapılır.
4. Uygun değil: Bloklayıcı bulgu var. Örnekler:
   - yurt dışı aktarım dayanağı yok;
   - özel nitelikli veri işleme şartı yok;
   - ajan kişiler hakkında insan incelemesi olmadan sonuç doğuruyor;
   - yasak uygulama ihtimali var.

Onay yetkisini aşan bulguda `/arthurlegal:commercial-legal-escalation-flagger`.

## Çıktı

Sistem talimatının çıktı iskeletiyle e-postaya hazır bir not yazılır. Sırası şöyledir:
1. İlk satır.
2. İlk paragrafta sonuç: karar ve özerklik basamağı.
3. Altı şartın durumu.
4. Hukuki bulgular, derecesiyle.
5. Koşullar.
6. Getiri iddiasının değerlendirmesi.
7. "İnceleme notu" (madde kontrolü cümlesi dâhil) ve "Sıradaki adım".

Kullanıcı isterse aynı içerik xlsx kontrol listesi olarak verilir:
- satırlar: basamak, altı şart, hukuki bulgular, koşullar;
- sütunlar: durum, derece, sahip, son tarih, dayanak.

## Bu skill ne yapmaz

- Teknik güvenlik denetimi ya da sızma testi yapmaz; güvenlik sorularını sorar.
- AI Act uygunluk değerlendirmesinin veya belgelendirmenin yerine geçmez.
- Tedarikçinin beyanını doğrulanmış saymaz; doğrulanmayan her beyan "bilinmiyor" olarak kalır.
- Onay vermez; karar avukatın ve kuruluşun yetkili organınındır.

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
| AZ duzenleyici degisiklik takibi — akt statusu degistiyse (`Legv olunmus`) ardil akti bul | `/arthurlegal:legal-research-az-mevzuat` |
| karsilastirmali regulasyon literaturu — **ikincil**, mevzuat yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
