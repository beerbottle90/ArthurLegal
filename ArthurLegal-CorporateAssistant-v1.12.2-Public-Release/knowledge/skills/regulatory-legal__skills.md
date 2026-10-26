# regulatory-legal - Skill Referans Kitapcigi

> Değişiklik bildirimi (Apache-2.0 md. 4(b)): Bu kitapçık Anthropic'in `claude-for-legal` deposundaki aynı adlı eklentiden uyarlanmıştır. ArthurLegal tarafından Türk hukuku esas alınarak Türkçe yeniden yazılmıştır (2026-10); yabancı yargı çevreleri için yalnız ArthurLegal MCP araçlarına yönlendirir. Üst kaynak ve sürüm izi: ATTRIBUTION.md.

> Alan: Regulasyon - EPDK/SPK/Rekabet, RG digest, yapay zeka ajani onayi
> Toplam skill: 10
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /regulatory-legal:ai-ajan-onayi (243 satir)
- /regulatory-legal:cold-start-interview (274 satir)
- /regulatory-legal:comments (129 satir)
- /regulatory-legal:customize (62 satir)
- /regulatory-legal:gap-surfacer (227 satir)
- /regulatory-legal:gaps (14 satir)
- /regulatory-legal:matter-workspace (172 satir)
- /regulatory-legal:policy-diff (226 satir)
- /regulatory-legal:policy-redraft (188 satir)
- /regulatory-legal:reg-feed-watcher (251 satir)

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
| AZ duzenleyici degisiklik takibi — akt statusu degistiyse (`Legv olunmus`) ardil akti bul | `/legal-research:az-mevzuat` |
| karsilastirmali regulasyon literaturu — **ikincil**, mevzuat yerine gecmez | `/legal-research:karsilastirmali-doktrin` |

Rehberler: `references/eqanun-mcp-rehberi.md` · `references/lex-scholar-rehberi.md` · `references/resourcecontracts-rehberi.md` · `references/karsilastirmali-hukuk-rehberi.md`

---

---

## /regulatory-legal:ai-ajan-onayi

---
name: ai-ajan-onayi
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
`/privacy-legal:use-case-triage` yeterlidir; yalnız sözleşme incelemesi isteniyorsa
`/commercial-legal:saas-msa-review` ya da `/commercial-legal:vendor-agreement-review`.

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
  yararlanılmasını önerir. Gerekiyorsa `/privacy-legal:use-case-triage`, sonra `/privacy-legal:pia-generation`.

**Tedarikçi sözleşmesi**

Ayrıntılı inceleme için `/commercial-legal:saas-msa-review` ya da `/commercial-legal:vendor-agreement-review`;
veri işleme eki için `/privacy-legal:dpa-review`. Bu skill şunlara bakar:
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
- Yabancı hukuk ya da yabancı tahkim seçilmişse `/commercial-legal:governing-law-review`.

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
aranır. Ajan çalışanları etkiliyorsa işyeri kullanım politikası için `/employment-legal:policy-drafting`.

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

Onay yetkisini aşan bulguda `/commercial-legal:escalation-flagger`.

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

## /regulatory-legal:cold-start-interview

---
name: cold-start-interview
description: >
  İlk kurulum — izlenecek düzenleyici kurumları (EPDK, BDDK, SPK, BTK, KVKK,
  Rekabet Kurumu, GİB, Sigorta Tahkim, Resmî Gazete'deki bakanlık ve
  Cumhurbaşkanlığı düzenlemeleri, gerekiyorsa AB/İngiltere/Almanya vb.) listeler,
  politika kütüphanesini dizinler, önemlilik eşiğini, tarama sıklığını ve özetin
  kime gideceğini öğrenir; böylece izleme gürültü değil sinyal üretir. İlk
  kurulumda, CLAUDE.md eksik ya da placeholder içeriyorsa, yeniden yapılandırmada
  (--redo) ya da bağlantıları yeniden denemek için (--check-integrations) kullan.
argument-hint: "[--redo | --full | --check-integrations]"
---

# /cold-start-interview

1. `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasına bak. Eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/regulatory-legal/*/CLAUDE.md`) doldurulmuş bir profil varsa ve ayar yolunda yoksa ayar yoluna kopyala, neyin taşındığını söyle. `--check-integrations` verildiyse görüşmeyi atla; yalnız Bölüm 0'daki "Ne bağlı?" kontrolünü çalıştır ve `## Available integrations` tablosunu yeniden yaz.
2. Görüşmeyi yürüt: önce Bölüm 0 (rol, pratik ortamı, bağlantılar), sonra izleme listesi, önemlilik, politika kütüphanesi, akışlar.
3. Politika klasörünü bağla ve dizinle.
4. Profili ayar yoluna yaz (üst klasörleri gerekirse oluştur).

Bağlantı denerken ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse verilir; yapılandırılmış ama denenmemiş bağlantı ⚪ (nasıl teyit edileceğine dair tek satırla). `.mcp.json` beyanına bakarak ✓ verme.

## Amaç

Her kurum her gün bir şey yayımlar; çoğu sizi ilgilendirmez. Bu görüşme hangi kurumların izleneceğini ve — asıl önemlisi — burada "önemli"nin ne demek olduğunu öğrenir. Her özet, karşılaştırma ve açık raporu bu profili okur; genel profil, her kurul duyurusunu idari para cezası gibi işleyen bir özet demektir.

## Kurulum durumu

- **Dosya yok** → görüşmeye başla.
- **`<!-- SETUP PAUSED AT: -->` var** → selamla, o bölümden devam etmeyi öner.
- **`[PLACEHOLDER]` var, duraklatma notu yok** → baştan başlamayı ya da placeholder'ların başladığı yerden devam etmeyi öner.
- **Dolu** → kurulmuş; `--redo` yoksa atla.

Bölüm iskeleti `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` şablonundadır. **Anahtarları çevirme:** `## Regulators we watch`, `## Who's using this`, `## Available integrations`, `## Policy library`, `## Materiality threshold`, `## Gap response process`, `## Feed configuration`, `## Outputs`, `## Matter workspaces`, `**Check cadence:**`, `**Comment tracking:**`, `**Default comment decision owner:**`, `Digest output path`, `Enabled`, `Active matter:`, `Cross-matter context` — `/regulatory-legal:reg-feed-watcher`, `/regulatory-legal:gaps`, `/regulatory-legal:comments` ve `reg-change-monitor` ajanı bunları birebir okur. İçerik Türkçe yazılır.

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/company-profile.md` dosyasına bak.
- **Varsa:** oku, tek satırla teyit et: "Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu? (Değiştirmek için 'güncelle' deyin.)" Teyit edilirse ortak soruları atla.
- **Yoksa:** ilk kurulan eklenti budur; ortak soruları sor, paketteki `knowledge/company-profile.md` şablonuna göre yaz ve söyle: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak."

Ortak profile ait sorular (varsa tekrar sorulmaz): pratik ortamı, ad, sektör, ne satıldığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri. İzleme listesinin ayrıntısı, önemlilik eşiği, politika kütüphanesi ve akışlar bu eklentide kalır.

## Kurulum kapsamı

Çalışma klasörü ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Politikalarınız başka yerdeyse kullanıcı kapsamında kurun (QUICKSTART.md)." Devam mı, yeniden kurulum mu — onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

> **`regulatory-legal`** mevzuat ve kurum kararı değişikliklerini izleyen, iç politikalardaki açıkları bulan ve uyum yükümlülüklerini yöneten ekip içindir.
>
> **2 dakika:** rolünüz, pratik ortamınız, ana düzenleyiciniz; gerisi varsayılan. **15 dakika:** tam izleme listesi, önemlilik eşiği, tarama sıklığı, özetin alıcıları, politika kütüphanesi dizini, taslak düzenleme görüş takibi.
>
> Hızlı mı, tam mı? (Sonra `/regulatory-legal:cold-start-interview --full` ile genişletebilirsiniz.)

Kullanıcının ev dizinindeki `~/CLAUDE.md`'yi ya da kişisel hafızasını okuyarak görüşmeyi önceden doldurma. Seçimden sonra tek paragraf oryantasyon: "Bu eklenti profilinizi (izleme listesi, önemlilik eşiği, tarama sıklığı), bir açık takip kaydını, politika karşılaştırma arşivini ve taslak düzenleme görüş takvimini tutar. Cevaplarınızı her seferinde okunan düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir. Kurulum yalnız sizin yazdıklarınızdan ve verdiğiniz belgelerden profil kurar; sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

**Hızlı yol:** yalnız Bölüm 0 ve izleme listesinin kapsamı; diğer alanlara `[DEFAULT]` yaz (varsayılan eşik aşağıda). Kapanış: "Tamam, komutları kullanabilirsiniz. Önemlilik eşiği, tarama sıklığı ve politika kütüphanesi için makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanması gereken bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--full`, tek bölüm için `--redo <bölüm>`."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** İzleme tablosu, uyum takvimi, eski açık analizi, politika dizini için önce bağlantı/yapıştırma iste: "Belgeyi yapıştırın ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli.
- **Uzun cevap gerekiyorsa bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste]. Şimdi doldurmak ister misiniz, placeholder olarak mı kalsın?" Sessiz boşluk bırakma.
- **Duraklat/devam:** "dur", "sonra devam" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — run /regulatory-legal:cold-start-interview to resume -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte cevaplanmış soruyu tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre ya da eşik söylerse `tr_mevzuat_madde_getir` ile çek ve karşılaştır; çelişirse: "[X] dediniz; metin [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnek: Rekabet soruşturmasında yazılı savunma süresi rapor tebliğinden itibaren otuz gündür; haklı gerekçeyle bir kez, en çok bir katına kadar uzatılabilir (4054 s. Kanun m. 45/2). İdari para cezası tutarlarını profile yazma: "güncel tutarı teyit et — dönemsel güncellenir."

## Bölüm 0 — Kim kullanıyor, ne bağlı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her çıktının üst başlığını belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan**
> 2. **Avukata erişimi olan, avukat olmayan** (uyum yöneticisi, iş birimi)
> 3. **Düzenli avukat erişimi olmayan**

2 ya da 3 ise bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları hüküm değil, avukatla konuşmanız için araştırma olarak çerçevelerim; (2) hukuki sonucu olan adımlardan önce — kuruma yazı ya da savunma, taslak düzenlemeye görüş gönderme, uyum beyanı, açığı 'kapandı' sayma — avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım." 3 ise ekle: "Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür, koşullarını baroya sorun." `## Who's using this` altına `**Role:**` ve (avukat değilse) `**Attorney contact:**` yaz.

### Pratik ortamı

> Hangisi size uyuyor? (Açık yönetimini ve eskalasyon dilini belirler.)
> - **Tek avukat / küçük büro** — onay zinciri sormam; "dış meslektaşa danış" yazarım.
> - **Orta / büyük büro** — onay zinciri, üstünüzde kim imzalar.
> - **Kurum içi hukuk / uyum** — eskalasyon matrisi, hukuk müdürü, uyum yöneticisi, ne zaman iş birimine gider.
> - **Kamu / klinik** — denetim modeli, dış yazışmada imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla yazın; profili ona göre kurar, doldurulan, uyarlanan ve boş kalan alanları işaretlerim.

Dallanma:
- **Büro (her tür):** `## Matter workspaces` → `**Enabled:** ✓`, `**Cross-matter context:** off`. Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Aynı sektörde birden fazla müvekkil izleniyorsa (ör. biri diğeri hakkında Rekabet Kurumuna başvuruyor) her yeni matter'da çatışma kontrolünü sor. İzleme taraması uygulama düzeyinde çalışır; müvekkile özgü değerlendirme matter'a yazılır.
- **Kurum içi:** `**Enabled:** ✗`.

Sonra eskalasyonu sade sor: "Bir inceleme üst onay gerektiren bir şey bulduğunda — şirket kararı gerektiren politika açığı, şirket adına görüş içeren yazı, uygulamayı değiştiren önemli bir düzenleme, yetkinizi aşan bir karar — kime gider? İsim ya da rol (hukuk müdürü, uyum yöneticisi), ya da 'kendim karar veririm'." Cevabı `**Practice setting:**` olarak `## Who's using this` altına, eskalasyonu `## Gap response process` → `**Escalation for material gaps:**` satırına yaz.

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantı farklıdır.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_resmi_gazete_fihrist()` (bugünün fihristi) ve izlenecek kurumlardan biri için `tr_kurum_karari_ara(kurum="rekabet", query="birleşme", limit=3)`. Cevap geldiyse ✓. Sonuç ince gelirse önce `status`: yüklenememiş kaynak "karar yok" demek değildir.
- **Yabancı ülke araçları** (`eu_`, `uk_`, `de_` …) — yalnız yabancı rejim izlenecekse dene.
- **Thomson Reuters Regulatory Intelligence** (ücretli, isteğe bağlı), **belge deposu** (Google Drive, SharePoint, Box), **Slack** — deneyebiliyorsan dene; deneyemiyorsan ⚪.

Rapor:
> - ✓ [Bağlantı] — bağlı (denendi)
> - ⚪ [Bağlantı] — yapılandırılmış, doğrulanmadı; MCP ayarlarınızdan teyit edin
> - ✗ [Bağlantı] — yok; [özellik] [manuel yönteme] düşer. Sonra bağlarsanız `--check-integrations` çalıştırın.

ArthurLegal MCP ✗ ise: "Türk kaynakları için otomatik akış yok; yalnız yapıştırdığınız metinle çalışırım ve her atıf 'doğrulanmadı' işaretiyle, UYARI satırıyla gelir."

**Hemen yaz:** `## Who's using this`, `## Available integrations` ve `## Outputs` (role göre üst başlık).

## Bölüm 1 — İzleme listesi (2-3 dk)

*(`/regulatory-legal:reg-feed-watcher` ve `reg-change-monitor` ajanını besler; listede olmayan kurum, siz `/regulatory-legal:policy-diff`'e yapıştırana kadar görünmez.)*

**[ŞİRKET ADI] ne yapıyor?** En önemli bağlam budur. Web sitesi, "hakkımızda" sayfası ya da faaliyet raporu bağlantısı yeter; ya da tek cümle: ne satıyorsunuz, kime, nasıl. Hangi lisans, izin ya da bildirimlerle çalışıyorsunuz? Büroysanız: izlediğiniz müvekkil sektörleri.

Önce sor: "Mevcut bir izleme tablonuz, uyum takviminiz ya da eski bir açık analizi notunuz var mı? Yapıştırın; kurumları ve önemlilik ölçütlerini ben çıkarayım." Yoksa satır satır kur (her kurum için **neden** izlendiğini de yaz):

| Kurum | Ne zaman izlenir (doğrulanmış dayanak) | ArthurLegal aracı |
|---|---|---|
| **EPDK** | Elektrik piyasasında üretim, iletim, dağıtım, toptan ve perakende satış, piyasa işletim, ithalat, ihracat ve toplayıcılık lisans almak koşuluyla yürütülür (6446 s. Kanun m. 4/1). Doğal gaz, petrol, LPG lisansı varsa ilgili kanunu `tr_mevzuat_ara(query="Doğal Gaz Piyasası", types=["KANUN"])` ile bul, maddeyi ilk konuda çek. | `tr_kurum_karari_ara(kurum="epdk", market="elektrik"\|"dogalgaz"\|"petrol"\|"lpg")` — yalnız yapısal Kurul kararları; bireysel lisans işlemleri RG fihristinde. RG: `tr_resmi_gazete_tara(konu="enerji", query=…)` |
| **BDDK** | Mevduat, katılım, kalkınma ve yatırım bankaları, yabancı bankaların Türkiye şubeleri ve finansal holding şirketleri Bankacılık Kanununa tabidir (5411 s. Kanun m. 2); Kurul ikincil düzenleme yapar (m. 88/a). | `tr_kurum_karari_ara(kurum="bddk", query=…)` (başlıkta arar); metin için `tr_semantik_ara(kurum="bddk", query=…)` |
| **TCMB** (ödeme / e-para) | Ödeme kuruluşu faaliyet iznini Merkez Bankası verir, izin kararı RG'de yayımlanır (6493 s. Kanun m. 3/1-b, m. 15/1). Fintech "BDDK" derse bu ayrımı sor. | Kurum kararı aracı yok → RG: `tr_resmi_gazete_tara(query="Merkez Bankası")`, `tr_mevzuat_ara` |
| **SPK** | Kurul, kamunun zamanında, yeterli ve doğru aydınlatılması için genel ve özel nitelikte kararlar alır (6362 s. Kanun m. 128/1-b). Halka açık şirket, aracı kurum, portföy yönetimi vb. | Kararlar haftalık bültende: `tr_kurum_karari_ara(kurum="spk", year=2026)` → `tr_spk_bulten_icinde_ara(bulten="2026/NN", query=…)`; tebliğler `tr_mevzuat_ara(query="Sermaye Piyasası")` |
| **BTK** | Elektronik haberleşme hizmeti sunmak ya da şebeke/altyapı işletmek isteyen şirket faaliyete başlamadan önce Kuruma bildirimde bulunur (5809 s. Kanun m. 9/2); Kurum, işletmeciler ile tüketicileri ilgilendiren Kurul kararlarını kamuoyuna açık tutar (m. 6/1-ç). | `tr_kurum_karari_ara(kurum="btk", date_from=…, date_to=…)`; metin için `tr_semantik_ara(kurum="btk")` |
| **KVKK** | Kurul şikâyetleri karara bağlar, resen inceler, düzenleyici işlem yapar ve idari yaptırıma karar verir (6698 s. Kanun m. 22/1-b, c, e, ğ). Kişisel veri işleyen her şirket için. | `tr_kurum_karari_ara(kurum="kvkk", params={"scan_pages": 1})`; arşiv `tr_semantik_ara(kurum="kvkk")`. Ayrıntılı KVKK uyumu: `/privacy-legal:policy-monitor` |
| **Rekabet Kurumu** | Hangi birleşme ve devralmaların izne tabi olduğunu Kurul tebliğle ilan eder (4054 s. Kanun m. 7/2); Kurul resen soruşturur, idari para cezası verir, tebliğ çıkarır (m. 27/a, f). Pazar payı yüksek, birleşme yapan ya da dağıtım ağı olan şirket için. | `tr_kurum_karari_ara(kurum="rekabet", decision_type="birlesme_devralma"\|"rekabet_ihlali"\|…)`; çok kelimeli ifadeyi tırnakla ara. RG: `konu="rekabet"` |
| **GİB** | Mükellefin izahat talebine özelgeyle cevap verilir; aynı durumdaki tüm mükellefler için sirküler yayımlanabilir; özelgeler internette yayımlanır (213 s. VUK m. 413). | `tr_kurum_karari_ara(kurum="gib", query=…, date_from=…)` — özelge kapsar, bağlayıcı değildir; sirküler için GİB sitesi. RG: `konu="vergi"` |
| **Sigorta Tahkim Komisyonu** | Sigorta ettiren ile riski üstlenen arasındaki uyuşmazlıklar için kurulur (5684 s. Kanun m. 30/1). Düzenleyici değil, hakem kararı: emsal izleme. Sigorta düzenleyicisi SEDDK için kurum kararı aracı yok → RG. | `tr_kurum_karari_ara(kurum="sigorta_tahkim", issue=…)`; arşiv `tr_semantik_ara(kurum="sigorta_tahkim")` |
| **Bakanlıklar, Cumhurbaşkanlığı** | Sektör bakanlığı yönetmelikleri, Cumhurbaşkanı kararları, kanun ve torba kanunlar | `tr_resmi_gazete_tara(date_from, date_to, query=…)` (≤60 gün, gün başına bir istek); `tr_mevzuat_ara(types=["KANUN"], rg_date_from=…, rg_date_to=…, konu=…)` |
| **Yargı** | Kanun veya CBK'yı iptal eden AYM kararı RG'de yayımlandığı tarihte yürürlüğü sona erdirir ya da en çok bir yıl ertelenir (Anayasa m. 153/3); Danıştayın düzenleyici işlem iptalleri | `tr_aym_ara(kind="norm", query="<kanun adı>")`; `tr_ictihat_ara(courts=["DANISTAYKARAR"], query=…)` |

`konu` bir ön elemedir, kapsam garantisi değildir; yayım teyidi için `query` ve fihrist kullanılır.

**ArthurLegal'da olmayanlar:** KİK, Sayıştay, TÜRKPATENT ve İSTAÇ için kaynak yok (resmî uçları cevap vermiyor). Kullanıcı bunları sayarsa açıkça söyle; RG'de yayımlanan yönetmelik ve tebliğleri `tr_resmi_gazete_tara` ile yakalayabileceğini, kurul kararları için kurumun sitesinden manuel izleme ya da RSS adresi gerektiğini ekle. Sonuç uydurma.

**Yabancı rejimler** — varsayma; AB'ye ihracat, AB'de şube, AB'li müşteri, yabancı halka arz var mı, sor.
- **AB:** `eu_search_eu_law(query="…")`, metin `eu_get_document_text(celex=…)`. **Birleşik Krallık:** `uk_search_legislation`, değişiklik etkileri `uk_get_effects`. **Almanya:** yeni yayımlar `de_recent_changes(since_iso=…)`. **Finlandiya** `fi_recent_changes`, **İspanya** günlük resmî gazete `es_get_daily_gazette`; **Hollanda, Polonya, Avusturya, İrlanda, Japonya, Azerbaycan:** ilgili önekli arama aracı (`nl_`, `pl_`, `at_`, `ie_`, `jp_`, `az_`).
- **ABD ve listede olmayan ülkeler:** "ArthurLegal'da bu ülkenin kaynağı yok; ABD kurumu izlenecekse Federal Register API (herkese açık uç) ya da kurumun RSS adresi `Free feeds` tablosuna yazılır; yorum için o ülkenin hukukçusu."

Sonda: "İzlemediğiniz ama belki izlemeniz gereken bir kurum var mı?" ve izleme listesi yüklenmediyse: "Bunu ekibe dağıtabileceğiniz ayrı bir izleme listesi notu olarak da yazayım mı?"

## Bölüm 2 — Önemlilik eşiği (asıl soru, 3-4 dk)

*(Bir gelişmenin anında mı, haftalık özette mi, hiç mi görüneceğine karar veren süzgeç. Yanlış ayar = okunmayan özet.)*

Her örnek için sor: anında mı, haftalık özette mi, hiç mi?
- İzlenen kurumun yeni yönetmeliği, tebliği ya da düzenleyici Kurul kararı
- Sektör kanununuzda değişiklik (torba kanun dahil) ya da Cumhurbaşkanı kararı
- Aleyhinize sonuç doğuran yeni düzenleyici işlem — **not:** ilanı gereken düzenleyici işlemde iptal davası süresi ilan tarihini izleyen günden başlar; özel kanunda ayrı süre yoksa idare mahkemesinde altmış, vergi mahkemesinde otuz gündür (İYUK m. 7/1, 7/4). Bu yüzden varsayılanı "anında"dır.
- Taslak düzenlemenin görüşe açılması
- Sektörünüzde bir şirkete soruşturma ya da idari para cezası; sektör dışında ama yaptığınız bir faaliyete ceza
- Rekabet Kurulu taahhüt ya da uzlaşma kararı — uzlaşma ihlalin kabulünü gerektirir, para cezasında yüzde yirmi beşe kadar indirim sağlar (4054 m. 43/5, 43/7); taahhüt açık ve ağır ihlallerde kabul edilmez (m. 43/3)
- AYM iptal kararı ya da Danıştayın yürütmeyi durdurma/iptal kararı
- GİB özelgesi (başvurana verilir) ya da sirküler (tüm mükellefler için)
- Kurum rehberi, kılavuzu, duyurusu (bağlayıcı değil); Kurul başkanı konuşması, basın açıklaması

Kalibrasyon şirketten şirkete değişir: hakkında soruşturma ya da taahhüt kararı olan şirket konuşmaları bile izler; kurumun hiç tanımadığı şirket görmezden gelebilir. Ölçüt yüklenmediyse sonda öner: "Bu önemlilik ölçütünü ekibin aynı ayarla okuması için ayrı bir not olarak yazayım mı?"

## Bölüm 3 — Politika kütüphanesi (2-3 dk)

*(`/regulatory-legal:policy-diff` ve `/regulatory-legal:gaps`'i besler; her değişiklik bu kütüphaneyle karşılaştırılır.)*

Önce: "Politika dizininiz (tablo, içindekiler, wiki sayfası) var mı? Yapıştırın; içe aktarayım." Yoksa:
- Politikalar nerede? (Drive, SharePoint, Confluence, Notion, yerel klasör) — "Klasörü gösterin, dizinleyeyim."
- Adlandırma kuralı ya da dizin var mı?
- Hangi politikanın sahibi kim? (Açıkları doğru kişiye yönlendirmek için.) İç yönetmelik, prosedür, uyum programı (rekabet, KVKK, sektör) ve sözleşme şablonlarını ayrı satır yap.

Dizin yüklenmediyse sonda öner: "Yeni gelen hukuk müdürü ya da uyum yöneticisinin ilk gün okuyacağı ayrı bir politika sahipliği dizini olarak yazayım mı?"

## Bölüm 4 — Akışlar, sıklık, alıcılar (2-3 dk)

**Adım 1 — Ücretsiz akışlar (her zaman etkin):** ArthurLegal MCP bağlıysa izleme listesindeki her Türk kurumu için yukarıdaki araç; RG için `tr_resmi_gazete_tara`. Kurumun duyuru sayfası ya da RSS adresini kullanıcıdan al — adresler değişir, ezberden adres yazma. Akışı olmayan kurum için: "Bu kurumu şimdi nasıl takip ediyorsunuz?" diye sor ve manuel girişi kaydet.

**Adım 2 — Ücretli abonelikler (ek, zorunlu değil):** Thomson Reuters Regulatory Intelligence var mı, hangi uyarılar? Ticari mevzuat veri tabanı aboneliği varsa uyarı e-postaları manuel girişle işlenir. CourtListener yalnız ABD izleniyorsa.

**Adım 3 — Manuel giriş:** "Bülten, meslek kuruluşu duyurusu ya da dış avukat notunda gördüğünüz bir gelişmeyi yapıştırın; politikalarınızla karşılaştırır, açıkları takip ederim." Profilde etkin işaretle.

**Adım 4 — Taslak görüş takibi** (`/regulatory-legal:comments`'i besler): "İzlenen bir kurum taslak düzenlemeyi görüşe açtığında son tarihi kaydedip görüş verip vermeyeceğinize karar vermeniz için işaretleyeyim mi?" Evet ise etkinleştir ve varsayılan karar sahibini yaz. Görüşe açma usulü kurumdan kuruma değişir; son tarihi kurumun duyurusundan al, uydurma.

**Adım 5 — Sıklık ve alıcılar:** Tarama günlük mü haftalık mı? (Enerji, finans gibi hareketli alanda günlük; aksi hâlde haftalık.) Özet kime gider — kişi/rol, Slack kanalı, e-posta listesi? Dosya da yazılsın mı, hangi klasöre? (Boşsa `~/regulatory-legal-digests/`.)

## Profili yazma

Şablon iskeletine göre; kısa örnek:

```markdown
# Regulatory Practice Profile
*Kurulum görüşmesiyle [TARİH] yazıldı. Doğrudan düzenlenebilir.*
## Regulators we watch
| Regulator | Jurisdiction | Why we watch | Feed source |
|---|---|---|---|
| EPDK | TR | [elektrik üretim lisansı — 6446 m. 4/1] | tr_kurum_karari_ara(kurum="epdk", market="elektrik") + RG konu="enerji" |
| [kurum] | [TR/AB/…] | [neden] | [araç / RSS / manuel] |

## Who's using this
**Role:** [...] · **Attorney contact:** [...] · **Practice setting:** [...]
## Available integrations
| Integration | Status | Fallback if unavailable |
|---|---|---|
| ArthurLegal MCP (tr_) | [✓/⚪/✗] | Yapıştırılan metin; atıflar UYARI satırıyla |
| Thomson Reuters Regulatory Intelligence | [✓/⚪/✗] | Ücretsiz akışlar + manuel giriş |
| Document storage | [✓/⚪/✗] | Yerel klasörden dizin |
| Slack | [✓/⚪/✗] | Özet yalnız dosya olarak |

## Policy library
**Location:** [...]
**Policies indexed:**
| Policy | File | Last updated | Owner |
|---|---|---|---|

## Materiality threshold
**Always material (alert immediately):**
- İzlenen kurumdan yeni yönetmelik/tebliğ/düzenleyici Kurul kararı; sektör kanununda değişiklik
- Aleyhe düzenleyici işlem (İYUK m. 7/4 — dava süresi ilandan işler)
- Sektörümüzde soruşturma ya da idari para cezası; [ŞİRKET ADI] adının geçtiği her şey
- İzlenen kanun hakkında AYM iptal kararı

**Review-worthy (weekly digest):**
- Taslak düzenlemenin görüşe açılması (son tarih comment-tracker'a)
- Sektör dışı ama faaliyetimize ilişkin ceza; Rekabet taahhüt/uzlaşma kararları
- Kurum rehberi, kılavuzu; GİB sirküleri ve konumuza ilişkin özelgeler

**FYI (monthly roundup or not at all):**
- Konuşmalar, basın açıklamaları, akademik yorum
- Yeni bir yaklaşım içermeyen rutin bireysel kararlar
## Gap response process
**Who triages regulatory changes:** [...]
**Who owns policy updates:** [...]
**How gaps get tracked:** [...]
**Escalation for material gaps:** [...]
## Feed configuration
**Free feeds (always active):**
| Regulator | Source | URL/method |
|---|---|---|
| [kurum] | ArthurLegal tr_ / RSS / manual | [araç çağrısı, adres ya da "manual entry"] |

**Paid feeds (if configured):**
| Service | Subscription | Alerts |
|---|---|---|
| TR Regulatory Intelligence | [yes/no] | [alert names] |
| CourtListener | [yes/no] | [yalnız ABD] |

**Manual entry:** Enabled — herhangi bir gelişmeyi yapıştırın; karşılaştırma ve açık takibi başlar.
**Comment tracking:** [Enabled / Disabled]
**Default comment decision owner:** [ad/rol]
**Check cadence:** [daily / weekly]
**Digest channel:** [kişi/rol, Slack kanalı, e-posta listesi]
**Digest output path:** [klasör ya da "chat only"]
## Outputs
Üst başlık — avukat: "GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ"; avukat olmayan: "ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — AVUKATLA GÖZDEN GEÇİRİN". Başlık tek başına koruma yaratmaz; kuruma giden yazıda başlık konmaz.
## Matter workspaces
**Enabled:** [✓/✗] · **Active matter:** none · **Cross-matter context:** off
```

Kaynak etiketi: `[ArthurLegal TR — <citation> — GG.AA.YYYY]`; araç veri getiremezse "UYARI: veri çekilemedi, teyidiniz gerekli: <aracın source_url'si ya da kaynağın resmî giriş sayfası>".

## Yazdıktan sonra

1. **Özeti göster:** "İzleme listesi ve eşik bunlar. Ayarlanacak kısım eşik — çok sıkı olursa kaçırırsınız, çok gevşek olursa özeti okumayı bırakırsınız."
2. **Neler yapabildiğimi görmek ister misiniz?**
   - Akışları izleme listesine ve eşiğe göre süzüp özet çıkarma — `/regulatory-legal:reg-feed-watcher`
   - Bir değişikliği politika kütüphanesiyle karşılaştırma — `/regulatory-legal:policy-diff`
   - Açık açıklar, sahipleri ve son tarihleri — `/regulatory-legal:gaps`
   - Taslak düzenleme görüş takvimi ve karar kaydı — `/regulatory-legal:comments`
   **Önerim:** `/regulatory-legal:reg-feed-watcher` ile son 30 günü deneme taraması — eşiğin doğru ayarlanıp ayarlanmadığını hemen gösterir. Kullanıcı görüşmede somut bir iş söylediyse listeyi atla. Politika kütüphanesini şimdi dizinlemeyi de öner.
3. **Kapanış:** "Profiliniz `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasında — düz metin. Doğrudan düzenleyebilir, `--redo` ile yeniden görüşebilir, `--check-integrations` ile bağlantıları yeniden deneyebilir, tek değişiklik için `/regulatory-legal:customize` kullanabilirsiniz. En sık ayarlananlar: izleme listesi, önemlilik eşiği, tarama sıklığı. Profiliniz öğrenir: bir özet çok gürültülü ya da çok sessiz gelirse ayar genellikle buradadır; `reg-change-monitor` ajanı politika kütüphanenize dokunan bir değişiklik görünce açık kontrolü için işaretler."

## Hata kalıpları

- **Kurumu kanunla eşleştirmeden listeye alma.** Her satırın bir "neden"i olsun; dayanak maddeyi `tr_mevzuat_madde_getir` ile çek.
- **Ödeme kuruluşunu BDDK'ya, Sigorta Tahkim'i düzenleyiciye yazma; ArthurLegal'da olmayan kurum (KİK, Sayıştay, TÜRKPATENT, İSTAÇ) için araç önerme.**
- **`konu` ön elemesini kapsam garantisi sayma.** "Bu hafta başka bir şey çıkmadı" deme; elenen ve belirsiz sayısını yaz.
- **Kurul kararı numarasını ya da para cezası tutarını ezberden yazma.** Yalnız araçtan dönen `citation` alanı.

---

## /regulatory-legal:comments

---
name: comments
description: Görüşe açılan düzenleme taslaklarını ve istişareleri izler, görüş son tarihlerini gösterir, görüş verme kararını kaydeder. Bir kurum ya da bakanlık taslağı görüşe açtığında son tarihi görmek, görüş verip vermeme kararını almak ya da kararı kaydetmek (--decide CMT-ID) için kullan.
argument-hint: "[isteğe bağlı: --decide CMT-ID]"
---

# /comments

## Amaç

Türkiye'de düzenleyici kurumlar ve bakanlıklar taslak düzenlemeleri çoğu zaman internet sitelerinde görüşe açar; son tarih duyuruda yazar. Görüş verip vermemek avukatın kararıdır; risk, son tarihin kayıtlı bir karar olmadan geçip gitmesidir. Bu skill açık görüş sürelerini gösterir ve kararları kaydeder. Kural Resmî Gazete'de yayımlandıktan sonra ikinci bir süre başlar: düzenleyici işleme karşı dava süresi (aşağıda); o tarih de buraya yazılır.

> ABD ile karşılaştırma: ABD'deki zorunlu "notice-and-comment" usulünün (Federal Register'da NPRM) Türkiye'de genel ve bağlayıcı bir karşılığı yoktur. Aşağıdaki çerçeve ve kurum uygulaması geçerlidir.

## Hukuki çerçeve (doğrulanmış)

Aşağıda "m." atıfları, aksi yazılmadıkça Mevzuat Hazırlama Usul ve Esasları Hakkında Yönetmelik'e (RG 24.02.2022/31760) aittir.

- **Kapsam.** Yönetmelik Cumhurbaşkanlığı, bakanlıklar, bağlı, ilgili, ilişkili kurum ve kuruluşlar ile diğer kamu kurum ve kuruluşlarının hazırladığı mevzuat taslaklarını kapsar; milletvekillerinin TBMM'ye sunduğu kanun teklifleri kapsam dışıdır (m. 1/2, 1/3).
- **Paydaş görüşü.** Taslaklar hakkında ilgili mahallî idareler, üniversiteler, sendikalar, kamu kurumu niteliğindeki meslek kuruluşları ve sivil toplum kuruluşlarının; iş ve yatırım ortamına ilişkin taslaklarda ayrıca özel sektör paydaşlarının görüşlerinden faydalanılır (m. 6/4).
- **Kamuoyuna açma takdire bağlıdır.** Kamuoyunu ilgilendiren taslaklar Cumhurbaşkanlığına iletilmeden önce internet, basın veya yayın yoluyla kamuoyunun bilgisine sunulabilir; toplanan görüşler değerlendirildikten sonra teklifte bulunulur (m. 6/5). "Sunulabilir"dir; her taslak görüşe açılmaz.
- **Meslek kuruluşu ve STK süresi.** Görüşü istenen kamu kurumu niteliğindeki meslek kuruluşu ve sivil toplum kuruluşu görüşünü on beş gün içinde bildirir; süresinde bildirilmezse olumlu görüş verilmiş sayılır (m. 7/2). [ŞİRKET ADI] görüşünü bir oda, birlik ya da sektör derneği üzerinden iletecekse iç son tarihi bu süreye göre kur.
- **Yürürlük için makul süre.** Ekonomik ve ticari alan ile yatırım ortamını etkileyen düzenlemelerde mümkün olduğunca yayım ile yürürlük arasında makul süre bırakılır (m. 17/2). Kısa uyum süresi görüşte ileri sürülebilecek bir noktadır.
- **Dayanak sınırı.** Kanun, CB kararnamesi ve Cumhurbaşkanı kararıyla yürürlüğe konulanlar dışındaki taslaklarda, dayanağında belirtilenler dışında yükümlülük getiren hükme yer verilmez (m. 24/1-a). Dayanağı aşan yükümlülük görüşün güçlü bir başlığıdır.
- **Düzenleyici etki analizi.** Kanun ve CB kararnamesi taslakları içindir (Düzenleyici Etki Analizinin Uygulanmasına İlişkin Usul ve Esaslar m. 1, 4/1-ç); ilgili taraflar ve paydaşlarla istişare edilerek yapılır ve analiz raporunda danışılan paydaşların görüş ve önerilerine yer verilir (m. 6/5, 9/4).
- **Bağımsız kurulların kendi düzenlemeleri.** EPDK, BDDK, SPK, BTK, KVKK ve Rekabet Kurumu yönetmelik ve tebliğ taslaklarını sitelerinde görüşe açabilmektedir; bu bir kurum uygulamasıdır. Kurumun kendi kanununda ya da yönetmeliğinde görüş alma hükmü varsa bul ve yalnız çektiğin maddeye atıf yap: `tr_mevzuat_icinde_ara(number="<kurum kanunu>", query="görüş taslak")`, sonra `tr_mevzuat_madde_getir`. Bulamazsan kural yazma; "kurum uygulaması" de ve gerekirse şunu ekle: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.
- **Tartışmalı — içtihadı kontrol et:** Mevzuat Hazırlama Yönetmeliği'nin görüş alma usulünün bağımsız kurulların kendi düzenlemelerine ne ölçüde uygulandığı ve görüş alınmamasının düzenleyici işlemin iptal sebebi olup olmadığı. Ara: `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="\"görüş alınmadan\" yönetmelik iptal")`; dönen kararın künyesini birebir kullan, karar numarasını ezberden yazma.

**Kural yayımlandıktan sonra.** Dava açma süresi özel kanununda ayrı süre yoksa Danıştay ve idare mahkemelerinde altmış gündür; ilanı gereken düzenleyici işlemlerde süre ilan tarihini izleyen günden başlar; ilgililer işlemin kendilerine uygulanması üzerine düzenleyici işlem ya da uygulama işlemi aleyhine de dava açabilir (İYUK m. 7/1, 7/4). Dava açılması işlemin yürütülmesini durdurmaz (İYUK m. 27/1). Özel kanunda farklı süre olup olmadığını ve görevli mercii `/administrative-legal:idari-dava-prep` ile kontrol et.

## Bağlamı yükle

- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml` → izlenen tüm taslak ve istişareler.
- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → `## Feed configuration` altındaki `**Comment tracking:**` ve `**Default comment decision owner:**`, `## Who's using this` → `**Role:**`.

Şema (anahtarlar ve değerler İngilizce kalır):

```yaml
comments:
  - id: CMT-001
    item_type: draft          # draft (görüşe açılmış taslak) | consultation (taslaksız istişare) | bill (TBMM kanun teklifi)
    regulator: "[kurum]"
    title: "[taslağın adı]"
    link: "[duyuru bağlantısı — uydurma]"
    source_tag: "[kurum sitesi]"   # ya da [kullanıcı verdi], [ikincil kaynak], [ArthurLegal TR — <araç> — GG.AA.YYYY]
    deadline: 2026-11-20      # duyurudaki son tarih; yoksa null ve not
    decision: undecided       # undecided | filing | not-filing | waived
    owner: "[ad]"
    owner_slack: "[kimlik]"
    rationale: ""
    final_publication: ""     # kural yayımlanınca: RG tarih/sayı
    challenge_deadline: ""    # kural yayımlanınca: dava süresinin son günü (hesap notuyla)
```

## Varsayılan görünüm — açık görüş süreleri

```markdown
## Görüş Süresi İzleyici — [tarih]

### ⏰ Son tarihe 14 günden az

| ID | Düzenleme | Tür | Son tarih | Kalan gün | Karar | Sahip |
|---|---|---|---|---|---|---|
| CMT-001 | [ad] | taslak | [tarih] | [N] | Karar yok | [sahip] |

### 🟡 Açık (14 günden fazla)

[aynı tablo]

### ⚖️ Yayımlanan kurallar — dava süresi işliyor

| ID | Düzenleme | RG | Dava süresinin son günü | Not |
|---|---|---|---|---|

### Son kararlar

| ID | Düzenleme | Karar | Gerekçe |
|---|---|---|---|
| CMT-002 | [ad] | not-filing | [gerekçe] |

---

**Toplam açık:** [N]  **30 günden az kalan ve kararsız:** [N]
```

Son tarihi belirtilmemiş kalemi "son tarih yok — kurumdan teyit et" diye ayrı satırda göster; tarih uydurma.

## Karar kaydet

```
/regulatory-legal:comments --decide CMT-001
Decision: [filing / not-filing / waived]
Rationale: "[kısa — ör. 'Taslak bizim faaliyetimize uygulanmıyor' ya da 'Taslağın geçiş süresi ve 4. maddesi hakkında görüş vereceğiz']"
```

İzleyiciyi günceller. Karar `filing` ise iç inceleme hatırlatması öner: görüş son tarihinden 5 iş günü önce.

**Görüş metni.** Bu skill görüş yazmaz. EPDK taslağına görüş için `/administrative-legal:epdk-proaktif-gorus`; diğer kurumlar için avukat taslağı. Görüş bir oda, birlik ya da sektör derneği üzerinden ortak verilecekse rakiplerle rekabete duyarlı bilgi (fiyat, maliyet, müşteri, kapasite planı) paylaşma: teşebbüsler arası anlaşma, uyumlu eylem ve teşebbüs birliklerinin rekabeti kısıtlayan kararları yasaktır (4054 m. 4). Ortak çalışmayı rekabet hukuku açısından avukata kontrol ettir.

## Bildirimler

Taslak ilk kez kaydedildiğinde (reg-feed-watcher tarafından) Slack ya da profildeki kanal bağlıysa ve `owner_slack` doluysa görüş karar sahibine mesaj. Kararsız kalırsa son tarihten 14 gün önce hatırlatma; hâlâ kararsızsa 3 gün önce yüksek öncelikli hatırlatma. Her mesaj gap-surfacer'daki gönderim başına onay kuralına tabidir: önizle, açık "evet" bekle, sonra gönder.

## Sonuç doğuran eylem kapısı (kuruma görüş sunma ya da cevap verme)

**Bir kararı `filing` olarak kaydetmeden önce — ve sunulmaya hazır bir görüş ya da kuruma cevap taslağı üretmeden önce her zaman:** profildeki `## Who's using this` bölümünü oku. Rol **Non-lawyer** ise:

> Bir kuruma görüş ya da cevap sunmak hukuki sonuç doğurur. Şirketin tutumunu kayda geçirir; kurum dosyasında kalır ve sonraki inceleme, denetim ya da davada şirket aleyhine kullanılabilir. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet:
>
> - Düzenleme ya da istişare (kurum, taslak, son tarih)
> - Görüşün neyi söylediği ve hangi maddelere ilişkin olduğu
> - Açık sorular
> - Ne ters gidebilir (aleyhe ikrar, önceki tutumlarla çelişki, sektör derneği üzerinden ortak görüşte rekabet hukuku riski)
> - Avukata sorulacaklar (görüş verelim mi; dernek üzerinden mi verelim; hangi tutumu almayalım)
>
> Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık bir "evet" olmadan `filing` kararı kaydetme ve sunulmaya hazır taslak üretme. İzleme görünümleri, son tarih hatırlatmaları ve `not-filing` / `waived` kararları kapıya tabi değildir.

---

## Bu skill ne yapmaz

- Görüş metnini yazmaz; ayrı bir avukat işidir (EPDK için `/administrative-legal:epdk-proaktif-gorus`).
- Görüş verme kararını vermez; kararı kaydeder, kararı avukat verir.
- Kurumların taslak duyurularını kendiliğinden bulmaz; ArthurLegal araçlarında taslak akışı yoktur. Duyuru sayfası profilde tanımlıysa reg-feed-watcher okur, değilse kullanıcı yapıştırır.
- Görüş sunulduktan sonraki süreci izlemez; kural yayımlanınca `/regulatory-legal:reg-feed-watcher` yakalar, dava süresi buraya işlenir.

> `comment-decision` `gap_type` anlamı ve gönderim başına onay kuralı **gap-surfacer** referans skill'indedir; asıl işe başlamadan önce onu yükle.

---

## /regulatory-legal:customize

---
name: customize
description: >
  Mevzuat izleme profilinde tek bir şeyi değiştir — tüm kurulum görüşmesini
  yeniden yapmadan. İzlenen kurumlar (EPDK, BDDK, SPK, BTK, KVKK, Rekabet, GİB,
  Sigorta Tahkim, Resmî Gazete, yabancı rejimler), politika kütüphanesi,
  önemlilik eşiği, açık yönetim süreci, akışlar, tarama sıklığı, özetin
  alıcıları ya da matter klasörleri. Kullanıcı "şunu değiştir", "kurum ekle",
  "izleme listemi güncelle", "eşiği değiştir" ya da "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değişikliğin tarifi]"
---

# /customize

## Ne zaman çalışır

Kullanıcı profilindeki bir şeyi — izlenen bir kurumu, önemlilik eşiğini, bir akışı, tarama sıklığını — kurulum görüşmesini baştan yapmadan ve dosyayı elle düzenlemeden değiştirmek istiyor.

## Ne yap

1. **Profili oku.** `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` ve bir üst klasördeki `~/.claude/plugins/config/claude-for-legal/company-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa:
   > Henüz kurulum yapılmamış. Önce `/regulatory-legal:cold-start-interview` çalıştırın — customize mevcut bir profili ayarlamak içindir.

2. **Haritayı göster** (her biri için tek satır mevcut değer):
   - **Kim olduğumuz** — ad, sektör, ülkeler, pratik ortamı *(tüm eklentilerle ortak — değişiklik `company-profile.md`'e yazılır)*
   - **İzlenen kurumlar** (`## Regulators we watch`) — kurum, neden, akış kaynağı; "öncelikli" (politikayı en çok etkileyen) ve "izleme" ayrımı
   - **Politika kütüphanesi** (`## Policy library`) — politikalar, yerleri, sahipleri
   - **Önemlilik eşiği** (`## Materiality threshold`) — anında / haftalık özet / FYI; `/regulatory-legal:reg-feed-watcher` çıktısını nasıl süzdüğü
   - **Açık yönetimi** (`## Gap response process`) — kim triyaj yapar, kim politikayı günceller, nerede takip edilir, eskalasyon
   - **Akışlar** (`## Feed configuration`) — ArthurLegal araçları, RSS adresleri, ücretli abonelik, `**Check cadence:**`, `**Digest channel:**`, `Digest output path`, taslak görüş takibi ve karar sahibi
   - **Kişiler** — hukuk müdürü, uyum yöneticisi, politika sahipleri, görüş yazısı hazırlayan, eskalasyon zinciri
   - **İş akışı** — matter workspaces, açık takip kaydı, `comment-tracker.yaml`, özet yayım sıklığı
   - **Entegrasyonlar** — ArthurLegal MCP, Thomson Reuters, Slack, belge deposu; düşüş yolları

3. **Sor:** "Neyi ayarlayalım? Bir bölüm seçin ya da değişikliği kendi cümlenizle anlatın."

4. **Değişikliği yap.** Mevcut değeri göster, yenisini al, aşağı akış etkisini açıkla, onay al, yaz. Örnekler:
   - *Kurum ekleme (EPDK, elektrik):* "Satıra neden ve akış yazılır: `tr_kurum_karari_ara(kurum="epdk", market="elektrik")` + `tr_resmi_gazete_tara(konu="enerji", query=…)`. `reg-feed-watcher` bir sonraki taramada bu kurumu süzer; `/regulatory-legal:policy-diff` bu kurumdan gelen düzenlemeyi girdi olarak kabul eder. Dayanak: lisanslı piyasa faaliyetleri 6446 s. Kanun m. 4/1."
   - *Kullanıcı KİK, Sayıştay, TÜRKPATENT ya da İSTAÇ eklemek istiyor:* "ArthurLegal'da bu kaynaklar yok (resmî uçları cevap vermiyor). Satırı `Feed source: manual` ile ekleyebilirim; RG'de yayımlanan yönetmelik ve tebliğleri `tr_resmi_gazete_tara(query=…)` yakalar, kurul kararları için kurumun sitesini ya da RSS adresini siz verirsiniz."
   - *Ödeme kuruluşu için BDDK ekleme talebi:* "Ödeme kuruluşu faaliyet iznini Merkez Bankası verir (6493 s. Kanun m. 3/1-b, m. 15/1); doğru satır TCMB'dir ve akışı RG'dir. BDDK'yı da tutalım mı?"
   - *Eşiği sıkılaştırma:* "Haftalık özet kısalır; yeni eşiğin altındaki kalemler özetten düşer ama aranabilir kalır."
   - *Sıklık haftalık → günlük:* "`reg-change-monitor` her gün çalışır; RG taraması gün başına bir istek atar ve tek seferde en çok 60 günlük aralık tarar."
   - *Yeni politika eklendi:* "`/regulatory-legal:policy-diff` yeni kuralları bu politikayla da karşılaştırır; görüş takibi bu politikayı etkileyen taslakları etiketler. Sahibi boşsa açıklar `owner: [unassigned]` düşer."
   - *Yabancı rejim (AB):* "Satır eklenir; kaynak `eu_search_eu_law`. ABD için ArthurLegal kaynağı yok — Federal Register API ya da kurum RSS'i `Free feeds` tablosuna, yorum için ABD'li avukat."
   - *Özet alıcısı değişti:* "`**Digest channel:**` güncellenir; Slack bağlı değilse özet yalnız dosya olarak yazılır."

   Kullanıcı bir madde, süre ya da eşik söylüyorsa yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; idari para cezası tutarlarını sabit yazma (güncel tutarı teyit et — dönemsel güncellenir).

5. **Ortak profil değişiklikleri** (ad, sektör, ülkeler, pratik ortamı) `company-profile.md`'e yazılır:
   > Bu değişiklik tüm eklentileri etkiler — ülke listesini okuyan her eklenti artık [yeni değer]i görür.

   Pratik ortamı kurum içinden büroya geçiyorsa `## Matter workspaces` → `**Enabled:** ✓` ve `**Cross-matter context:** off` önerilir; Av. K. m. 38 gereği çatışma kontrolünü hatırlat.

6. **Kapat:** "Tamam. Bir sonraki çıktı bunu yansıtacak. Başka bir şey var mı? `/regulatory-legal:customize` her zaman çalışır."

## Korkuluklar

- **Bölümü silme.** Bir kurum "çıkarılmak" istenirse `[Monitor only]` işaretini öner: akış arşivde kalır, aktif özetten çıkar.
- **İç tutarsızlığı işaretle.** Ör. izlenen kurum + o kurumun alanında faaliyet yok (EPDK var, lisans yok); "haftalık özet" + çeyrekte bir kalem bile çıkarmayacak eşik; "Sigorta Tahkim" düzenleyici gibi yazılmış (hakem kararıdır; düzenleyici SEDDK, akışı RG); KVKK izleniyor ama `/privacy-legal` profili farklı kurum listesi taşıyor.
- **Güvence kaybını işaretle.** Kaynak etiketleri, çekilemeyen veride UYARI satırı, `[verify]` etiketleri ve açık triyajındaki `[review]` işareti yük taşır — kaldırma. Eşik ayarlanabilir; ama aleyhe düzenleyici işlemi "anında"dan düşürmek isteniyorsa uyar: ilanı gereken düzenleyici işlemde dava süresi ilan tarihini izleyen günden işler (İYUK m. 7/4).
- **Anahtarları çevirme** (`## Regulators we watch`, `## Materiality threshold`, `## Feed configuration`, `**Check cadence:**`, `## Matter workspaces`, `Active matter:` vb.).
- **Tek seferde tek değişiklik.** Görüşmeyi baştan sorma.

---

## /regulatory-legal:gap-surfacer

---
name: gap-surfacer
description: >
  Referans: /regulatory-legal:gaps ve /regulatory-legal:comments skill'lerinin dayandığı ortak
  açık ve görüş izleme çerçevesi. Açık politika açıklarını düzeltme durumuyla izler,
  policy-diff'in bulduğu açıkları alır, açık ve yaşlanan kalemleri gösterir, sahiplerine
  yönlendirir ve sahiplere gönderim başına onayla bildirim taslağı hazırlar. gaps ve comments
  skill'leri asıl işe başlamadan önce bunu yükler.
user-invocable: false
---

# Gap Surfacer

> Sahip bildirimleri varsayılan olarak açıktır. Bir sahibi çıkarmak için `owner_slack` alanını boş bırak.

## Gönderim başına onay — istisnasız

Herhangi bir mesajı (Slack, Teams ya da e-posta: atama bildirimi, gecikme hatırlatması, toplu bildirim, durum raporu) göndermeden önce:

1. Kullanıcıya tam olarak neyi kime göndereceğini göster: "Bunu [N] kişiye göndermek üzereyim: [önizleme]."
2. Açık bir "evet" bekle.
3. Mesajda künye, son tarih ya da uyum sonucu varsa ekle: "⚠️ Bu mesajdaki künyeler doğrulanmadı; güncel olduklarını teyit etmeden gönderiyorum. 'Uygulamadan önce doğrulayın' satırı ekleyeyim mi?"
4. Onaysız asla gönderme. Takvime bağlı olarak da, toplu olarak da, "dün de gönderilmişti" diye de.

Onaysız otomatik gönderim bu eklentideki en geri alınamaz eylemdir: eklentinin kendi doğrulama notunun "yanlış olabilir" dediği içeriği, kontrol imkânı olmayan kişilere gönderir. Bu ikisinin birleşimi incelemeyi atlayamaz.

## Matter context

Eklenti profilinde `## Matter workspaces` → `Enabled` `✗` ise (şirket içi kullanımda varsayılan) bu paragrafı atla; skill'ler practice-level bağlamla çalışır. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/regulatory-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

---

## Amaç

Açıklar bulunur, sonra unutulur. Bu skill açığı kapanana kadar izler ve kapatmaktan sorumlu kişiye hatırlatır.

## İzleyici

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml` dosyasındadır. Anahtarlar ve değerler İngilizce kalır; açıklamalar Türkçe.

> **comment-tracker.yaml notu:** `~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml` comments skill'inin kardeş dosyasıdır. reg-feed-watcher (taslak ve istişareleri otomatik kaydeder) ve comments (kullanıcının görüş kararlarını izler) yazar; şeması comments skill'indedir. Bu skill onu okumaz. Şemayı değiştirirsen iki kullanıcıyı da güncelle.

```yaml
gaps:
  - id: GAP-001
    requirement: "[düzenlemenin istediği, tek cümle]"
    regulation: "[ad + araçtan dönen citation]"
    policy_affected: "[politika adı ya da 'new policy needed']"
    gap_type: "partial"  # none | partial | full | new-policy | watch | comment-decision
    owner: "[politika kütüphanesindeki sahip]"
    owner_slack: "[Slack kullanıcı kimliği, biliniyorsa]"
    opened: 2026-10-26
    due: 2027-01-01  # yürürlük tarihi, geçiş süresinin sonu, kurum ihtarındaki giderme süresi, iç son tarih ya da görüş son tarihi
    status_verified: true  # policy-diff kuralın yürürlükte olduğunu teyit edemediyse false; doğrulanmamış kalem hiçbir zaman 🔴 Overdue olmaz
    status: "open"  # open | in-progress | closed | risk-accepted
    notified: false  # atama bildirimi gönderilince true
    resolution: ""  # kapanışta doldurulur
```

**`due` nereden gelir.** Düzenlemenin yürürlük maddesi ya da geçiş hükmü; kurumun yazılı ihtarındaki giderme süresi (ör. elektrik piyasasında ikincil mevzuata ya da Kurul kararına aykırılıkta aykırılığın giderilmesi için verilen ihtar süresi: 6446 m. 16/1-b); iç son tarih; taslak ve istişarede görüş son tarihi. Hangisi olduğunu `due` satırının yanına yorum olarak yaz.

**Dava açılmış olması tarihi durdurmaz.** Düzenlemeye karşı dava açılması işlemin yürütülmesini durdurmaz; yürütmeyi durdurma kararı ayrı şartlara bağlıdır (İYUK m. 27/1, 27/2). Kuralı dava edilmiş diye açığı `watch`'a çekme; yürütmeyi durdurma kararı varsa `status_verified: false` yap ve nedenini yaz.

**Doğrulanmamış kuralda Overdue yok.** 🔴 Overdue "bağlayıcı bir süreyi kaçırdık" demektir. Kuralın durumu doğrulanmadıysa (policy-diff `status_verified: false` yazdıysa, ya da kural 12 aydan eski, yürürlük tarihi geçmiş ve güncelliği teyit edilmemişse; AYM iptali, Danıştay yürütmeyi durdurma kararı, değişiklik ya da erteleme kontrol edilmediyse) süre bağlayıcı olmayabilir. 🟡 "İnceleme gerekli" kullan ve yaz: "Kural yayımlandığı hâliyle yürürlükteyse bu [N] gün gecikmiş olur. Eskale etmeden önce kuralın durumunu doğrula." Doğrulanmamış kuralı aktif gecikme ve yaklaşan son tarih kovalarına değil `watch`'a koy; `watch`'ın yeniden değerlendirme tarihi, kalem yeniden uyum açığı olarak çıkmadan önce durum kontrolünü zorlar.

**`gap_type` anlamları:**

| Değer | Anlamı | Hatırlatma |
|---|---|---|
| `none` | Politika gerekliliği zaten karşılıyor; yalnız denetim izi için kaydedilir. Seyrek olmalı; kayıtların çoğu `none` ise karşılaştırma büyük ihtimalle yanlış politikaya karşı yapılmıştır. | Otomatik hatırlatma yok. |
| `partial` | Politika konuyu ele alıyor ama yeni gerekliliği tam karşılamıyor; değişiklik gerekir. | Son tarihten 30 gün önce. |
| `full` | Politika yeni gereklilikle çelişiyor ya da hiç değinmiyor; yeniden yazım ya da yeni bölüm gerekir. | Son tarihten 30 gün önce. |
| `new-policy` | Bunu karşılayan politika yok; yazılması gerekir. | Son tarihten 30 gün önce. |
| `watch` | İleriye dönük kalem: istişare, görüşe açılmış ama yayımlanmamış taslak, TBMM'deki kanun teklifi ya da durumu doğrulanmamış kural. Bugün uyum yükümlülüğü yok. `due` yeniden değerlendirme tarihidir (beklenen yayım ya da bir yıllık ufuk), uyum son tarihi değildir. | Otomatik hatırlatma yok; kural yayımlanınca ya da tarih gelince yeniden değerlendir. |
| `comment-decision` | Görüş kararı bekleyen taslak ya da istişare. `due` görüş son tarihidir. | Son tarihten 21 gün önce (görüş hazırlama penceresi kısadır). |

`watch` ve `comment-decision` kalemleri uyum açığı değildir; kural öncesi izleme kayıtlarıdır. Durum raporunda ayrı kovada göster ki sabah okuyan avukat "kurum fark etmeden düzelt" ile "göz kulak ol"u bir bakışta ayırsın.

## Modlar

### Mod 1: policy-diff'ten alma

policy-diff açık bulunca `gap-tracker.yaml`'a ekle. Mükerrer kayıt yapma: aynı gereklilik + aynı politika = aynı açık. policy-diff kapsamı daraltılmış bir karşılaştırma ise (⚠️ KAPSAM SINIRI başlığı) o başlığı her ilgili kayda aynen taşı.

**Aldıktan sonra sahibi bilgilendir.** Slack (ya da profildeki kanal) bağlıysa ve `owner_slack` doluysa, en baştaki gönderim başına onaydan sonra:

```
📋 Size yeni bir uyum açığı atandı

Açık: [GAP-ID] — [gereklilik, tek cümle]
Düzenleme: [ad + bağlantı]
Etkilenen politika: [politika adı ya da "yeni politika gerekli"]
Son tarih: [tarih ve türü]

Açık izleyicinin tamamı: /regulatory-legal:gaps
```

Gönderdikten sonra kayıtta `notified: true` yap. Kanal bağlı değilse durum raporunda bildirimin gönderilmediğini yaz ve elle takip için işaretle.

### Mod 2: Durum raporu

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

## Açık Uyum Açıkları — [tarih]

### Sonuç

[N açık [tarih]e kadar işlem gerektiriyor — ilk üçü: X, Y, Z]

### 🔴 Overdue

| ID | Gereklilik | Politika | Sahip | Son tarih | Geçen gün |
|---|---|---|---|---|---|

### 🟠 30 günden az kalan

[aynı tablo]

### 🟡 Açık

[aynı tablo; doğrulanmamış kural kaynaklı "İnceleme gerekli" satırları da burada, notuyla]

### 👀 İzleme kalemleri (kural öncesi)

[`watch` ve `comment-decision` kayıtları. Uyum açığı değildir; ayrı tutulur ki gecikme ve yaklaşan son tarih kovalarında yalnız gerçek uyum süreleri kalsın.]

| ID | Kalem | Tür (taslak / istişare / kanun teklifi / durumu doğrulanmamış) | Görüş ya da yeniden değerlendirme tarihi | Sahip |
|---|---|---|---|---|

### Devam eden

[aynı tablo]

### Yakında kapananlar

[son 5, kapanış notuyla]

---

**En eski açık:** [ID], [N] gün
**Sahibe göre:** [dağılım]
**Gönderilen sahip bildirimi:** [N] / [toplam]

---

**Her açık için sonraki adım:** `/regulatory-legal:policy-redraft`, `[doğrula]` etiketli işaretli bir politika taslağı ve değişiklik özeti üretir. Politika sahibinin incelemesi için öneridir; kaynak belgeye doğrudan müdahale değildir.

---

**Atıfları doğrula.** Bu izleyicideki künyeler önceki adımlarda (reg-feed-watcher ve policy-diff) yapay zekâ desteğiyle üretildi. Bir açığı kapatmadan ya da risk kabulüne almadan — veya bir iç beyan, yönetim kurulu raporu ya da kuruma cevapta kullanmadan — dayanak kuralı Resmî Gazete, mevzuat.gov.tr ya da kurumun sitesinden doğrula. Önceki adımlardan taşınan kaynak etiketleri (ör. `[ArthurLegal TR — tr_resmi_gazete_tara — GG.AA.YYYY]`, `[web araması — doğrula]`) künyenin nereden geldiğini gösterir; `doğrula` etiketliler önce kontrol edilir. Etiketleri silme.
```

## Ayar eksikse

Bu skill açık sahiplerini `## Policy library` tablosunun Owner sütunundan, triyaj ve eskalasyonu `## Gap response process` altındaki `**Who triages regulatory changes:**` ve `**Escalation for material gaps:**` satırlarından okur. Gereken değer boşsa ya da `[PLACEHOLDER]` ise:
- **Triyaj sorumlusu yok:** atamayı açık bırak ve ekle: "`## Gap response process` altında `**Who triages regulatory changes:**` boş. Yeni açıkların yönlendirilmesi için `/regulatory-legal:cold-start-interview --redo` ile ya da profili düzenleyerek atayın."
- **Yeni açığın sahibi bilinmiyor:** `owner: [unassigned]` ile kaydet ve ekle: "Politika kütüphanesi etkilenen politika için sahip göstermediğinden [N] açık sahipsiz kaydedildi. Yönlendirme için kütüphanedeki Owner sütununu doldurun."
- **Gecikmiş önemli açık için eskalasyon yolu yok:** yine gecikmiş olarak raporla ve ekle: "Gecikmiş önemli açıklar için eskalasyon yolu tanımlı değil. `/regulatory-legal:cold-start-interview --redo` ile ya da profili düzenleyerek tanımlayın."

Değerler doluysa ayardan söz etme.

**Son tarih hatırlatma mantığı** (durum raporunda ve zamanlanmış ajanda çalışır). Hatırlatma sıklığı `gap_type`'a bağlıdır: uyum açığına 30 gün, görüş kararına 21 gün önceden haber; `watch`'a otomatik hatırlatma yok.

"open" ya da "in-progress" her kayıt için:
- `partial`, `full`, `new-policy`, `none`: son tarihe 30 günden az kaldıysa ve son 7 günde hatırlatma gönderilmediyse "⏰ Hatırlatma: uyum açığına [N] gün kaldı" başlıklı mesajı ÖNİZLE ve onay bekle.
- `comment-decision`: görüş son tarihine 21 günden az kaldıysa ve son 7 günde hatırlatma gönderilmediyse "💬 Görüş kararı için [N] gün kaldı" başlıklı mesajı ÖNİZLE ve onay bekle.
- `watch`: otomatik hatırlatma yok. İzleyici gözden geçirilirken ya da aynı düzenleme için kural yayımlanınca yeniden bak.
- Uyum açığının son tarihi geçtiyse: raporda gecikmiş göster, mesajı ÖNİZLE, onay bekle.
- `comment-decision` kaleminin son tarihi geçti ve görüş sunulmadıysa: gecikmiş göster, mesajı ÖNİZLE, onay bekle; sahibinden kaydı notuyla birlikte `risk-accepted` (bilinçli olarak görüş verilmedi) ya da `closed` (görüş sunuldu) yapmasını iste.
- Hatırlatma zamanlarını kayda yaz ki tekrar tekrar rahatsız etmeyesin.
- Toplu hatırlatma da onay ister: "12 mesaj göndermek üzeresiniz" önizlemesi ve "evet" yeterlidir; sessizce toplu gönderim yeterli değildir.

### Sonuç doğuran eylem kapısı (uyum beyanı)

**Bir açığı çözüldü diye kapatmadan ya da bir düzenleyici gerekliliğe uyumu beyan eden herhangi bir çıktı (iç beyan, yönetim kurulu raporu, denetim cevabı, kuruma cevap) üretmeden önce** profildeki `## Who's using this` bölümünü oku. Rol **Non-lawyer** ise:

> Uyum beyan etmek ya da bir açığı çözüldü diye kapatmak hukuki sonuç doğurur. Beyan sonradan yanlış çıkarsa şirket aleyhine kullanılabilir; erken kapanış riski açık bırakır. Kuruma verilen bilgi ayrıca yaptırıma konu olabilir: örneğin elektrik piyasasında Kurumun bilgi istemesinde yanlış, eksik ya da yanıltıcı bilgi verilmesi ihtar ve idari para cezasına bağlanmıştır (6446 m. 16/1-a). Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet:
>
> - Açık (gereklilik, kaynak, karşılaştırmanın bulduğu)
> - Önerilen çözümün neyi kapsayıp neyi kapsamadığı
> - Kalan açık ya da belirsizlik
> - Açık sorular
> - Ne ters gidebilir (fazla geniş beyan, çözülmemiş kalan yükümlülük, önceki tutumla çelişki)
> - Avukata sorulacaklar (gerçekten kapandı mı; gerekçeli risk kabulü daha mı doğru; dış avukat görüşü gerekir mi)
>
> Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık bir "evet" olmadan açığı kapalı işaretleme ve uyum beyanı üretme. Durum raporları ve izleme görünümleri kapıya tabi değildir.

### Mod 3: Açığı kapatma

```
/regulatory-legal:gaps --close GAP-001
Resolution: "Politika v2.3 güncellendi, [tarih]te onaylandı"
```

Durumu `closed` yapar; kapanış notunu ve tarihini kaydeder.

### Mod 4: Risk kabulü

Bazen cevap "bunu düzeltmeyeceğiz"dir. Geçerli bir karardır ama belgelenmelidir.

```
/regulatory-legal:gaps --accept GAP-002
Rationale: "Gereklilik yalnız [karşılamadığımız koşul] için geçerli. [Tetikleyici] olursa yeniden bak."
Accepted by: [yetkili kişi]
```

Durum `risk-accepted` olur. Kayıt silinmez ama açık raporundan çıkar. Önemli bir açıkta kabul edenin yetkisini `**Escalation for material gaps:**` satırıyla karşılaştır; yetkisi görünmüyorsa kaydetmeden önce eskalasyonu öner.

## Entegrasyon: reg-change-monitor ajanı

Ajanın digest'i açık sayısını ve en eski açığın yaşını içerir. Gecikmiş bir şey varsa digest'in en üstüne yazılır. Ajan son tarih hatırlatma kontrolünü de çalıştırır; ama mesajlar burada da gönderim başına onaya tabidir: gözetimsiz çalışmada göndermez, "onay bekleyen bildirimler" olarak listeler.

## Kapanış

Profildeki `## Outputs` karar ağacıyla bitir; seçenekleri bu çıktıya uyarla (X'i yaz, eskale et, olgu topla, izle ve bekle, başka bir şey). Ağaç çıktıdır; seçimi avukat yapar.

İzleyicide yaklaşık 10'dan fazla açık açık varsa ya da kullanıcı isterse panoyu öner (profil `## Outputs → Dashboard offer for data-heavy outputs`): önem derecesine göre sayılar, son tarihe göre açık zaman çizelgesi, sahip, durum ve son işlem tarihiyle sıralanabilir tablo.

## Bu skill ne yapmaz

- Açıkları kendiliğinden kapatmaz. Kapanış, kapanış notu ve notun anlattığı insan eylemiyle olur.
- Slack (ya da profildeki kanal) bağlı değilse bildirim göndermez; durum raporunda işaretler.
- Aynı açık için 7 günde birden fazla hatırlatma göndermez.
- Uyum beyanı ya da kuruma cevap metnini kapı onayı olmadan üretmez.

---

## /regulatory-legal:gaps

---
name: gaps
description: Açık uyum açıkları izleyicisi — işaretlenmiş ama kapanmamış olanlar. "Hangi açıklar açık", "açık izleyici", "düzeltme durumu" denince ya da izlenen bir açık kapatılmak (--close GAP-ID) veya risk kabulüne alınmak (--accept GAP-ID) istendiğinde kullan.
argument-hint: "[isteğe bağlı: --close GAP-ID | --accept GAP-ID]"
---

# /gaps

1. `~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml` dosyasındaki izleyiciyi oku.
2. `--close`: açığı kapanış notuyla kapat. Önce gap-surfacer'daki uyum beyanı kapısını uygula (rol Non-lawyer ise avukat onayı sorulur).
3. `--accept`: risk kabulü gerekçesini ve kabul edeni kaydet; durum `risk-accepted`. Kabul edenin yetkisini profildeki eskalasyon yolundan kontrol et.
4. Aksi hâlde: açık kalemleri yaşa ve önemliliğe göre raporla; kural öncesi kalemleri (`watch`, `comment-decision`) ayrı kovada göster.

> İzleyici şeması, durum raporu biçimi, sahip bildirimi kuralı (gönderim başına onay, istisnasız), hatırlatma sıklığı, kapatma ve risk kabulü modları, doğrulanmamış kuralda Overdue yasağı ve uyum beyanı kapısı **gap-surfacer** referans skill'indedir; asıl işe başlamadan önce onu yükle.

---

## /regulatory-legal:matter-workspace

---
name: matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkilin mevzuat değişikliği, taslak görüş, açık
  giderme, kurum bilgi talebi ya da soruşturma dosyasının bağlamını diğerlerinden
  ayrı tutar; aynı sektörde birden fazla müvekkil izlenebildiği için çapraz okuma
  kapalıdır. Çok müvekkilli avukat "yeni matter", "matter değiştir", "matter'larımı
  listele", "matter'ı kapat" dediğinde ya da bir skill hangi matter'da çalıştığını
  bilmek istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil ve dosya üzerinde çalışır. Matter çalışma alanı her dosyanın bağlamını diğerlerinden ayrı tutar. Bu skill o alanları yöneten ince dosya katmanıdır.

## Alt komutlar

- `/regulatory-legal:matter-workspace new <slug>` — yeni matter oluştur, kısa ön görüşme yap, `matter.md` yaz
- `/regulatory-legal:matter-workspace list` — matter'ları durum ve aktiflik işaretiyle listele
- `/regulatory-legal:matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/regulatory-legal:matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/_archived/` altına taşı; asla silme)
- `/regulatory-legal:matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünün dolu olduğunu teyit et. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek şirket için kurum içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/regulatory-legal:cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok."
2. `$ARGUMENTS`'ın ilk kelimesine göre dallan:
   - `new` → ön görüşme, `matters/<slug>/matter.md` yaz, `history.md` ve `notes.md` oluştur.
   - `list` → `matters/*/matter.md` dosyalarını tara, tablo bas, aktif olanı işaretle.
   - `switch` → uygulama CLAUDE.md'sindeki `Active matter:` satırını güncelle.
   - `close` → `matters/<slug>/` klasörünü `matters/_archived/<slug>/` altına taşı, kapanış tarihini `history.md`'ye yaz.
   - `none` → `Active matter:` satırını `none — practice-level context only` yap.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` şablondaki gibi kalır; `/regulatory-legal:policy-diff`, `/regulatory-legal:policy-redraft` ve `/regulatory-legal:gaps` bunları birebir okur.

**İzleme uygulama düzeyindedir.** `reg-feed-watcher` ve `reg-change-monitor` ajanı varsayılan olarak matter'sız çalışır. Özetteki bir kalem belirli bir müvekkili ilgilendiriyorsa değerlendirme (`policy-diff`, açık kaydı, görüş kararı) o müvekkilin matter klasörüne yazılır.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/regulatory-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, kurum, tür, kritik süreler, olgular, sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-epdk-lisans-tadili`, `xyz-rekabet-sorusturma-2026`, `musteri-taslak-teblig-gorusu`. Gerçek ad yerine takma ad kullanılabilir. Aynı slug arşivde varsa arşivdeki korunur; yeni matter'a başka slug ver.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı:** Aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat teklifi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Mevzuat işlerinde tipik risk: aynı soruşturmada şikâyetçi ile soruşturulan, aynı birleşme dosyasında taraf ile itiraz eden rakip, aynı taslağa zıt görüş verecek iki müvekkil. Yalnız aynı sektörde rakip olmak "aynı iş" sayılır mı — **tartışmalı**; büronun meslek kuralı yorumuna ve politikasına bırak. Sor: "Bu matter için çatışma kontrolü yapıldı mı?". Bu skill kontrolü kendisi yapmaz ve bu amaçla başka matter'ları okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz taraf (kurum içiyse iç birim)
   - **Kurum** — EPDK, BDDK, SPK, BTK, KVKK, Rekabet, GİB, TCMB, bakanlık, AB/yabancı makam …
   - **Karşı taraf / diğer ilgililer** — şikâyetçi, rakip, karşı işlem tarafı (birden fazla olabilir)
   - **Matter türü** — mevzuat değişikliği danışmanlığı | taslak düzenlemeye görüş | açık giderme (politika güncelleme) | kurum bilgi/belge talebi ya da yerinde inceleme | soruşturma / idari yaptırım savunması | düzenleyici işleme karşı dava hazırlığı | lisans/izin/bildirim | sürekli konu | diğer
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (yüksek, çapraz bağlamda ek dikkat demektir; ör. soruşturmadaki ticari sır)
   - **Kritik süreler** — varsa, aşağıdaki listeden
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, hangi düzenleme
   - **Matter'a özel sapmalar** — uygulama profiline göre farklar; ör. "müvekkil bu kurum için günlük tarama istiyor", "bu dosyada kuruma yazılar yalnız ortak imzasıyla çıkar"
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/regulatory-legal:matter-workspace switch <slug>`)"

**Kritik süre listesi** (doğrulanmış; matter'a uyanı yaz, tarihleri tebliğ belgesinden hesapla):
- **Düzenleyici işleme dava:** özel kanunda ayrı süre yoksa Danıştayda ve idare mahkemesinde altmış, vergi mahkemesinde otuz gün (İYUK m. 7/1). İlanı gereken düzenleyici işlemde süre ilan tarihini izleyen günden başlar; düzenleyici işleme uygulama işlemiyle birlikte de dava açılabilir (m. 7/4).
- **Rekabet soruşturması:** soruşturma kararı 15 gün içinde taraflara bildirilir; soruşturma en geç 6 ayda tamamlanır, bir defaya mahsus 6 aya kadar ek süre verilebilir (4054 m. 43/1-2). Yazılı savunma soruşturma raporunun tebliğinden itibaren 30 gün; haklı gerekçeyle bir kez, en çok bir katına kadar uzatılabilir; raportörlerin ek yazılı görüşüne 30 gün içinde cevap; süresinde verilmeyen savunma dikkate alınmaz (m. 45/2-3). Uzlaşma yalnız soruşturma raporunun tebliğine kadar ve ihlalin kabulüyle; Kurulun verdiği kesin süre geçirilirse bildirim dikkate alınmaz; uzlaşılan hususlar dava konusu yapılamaz (m. 43/5, 6, 8). Taahhüt önaraştırma ya da soruşturma sürecinde sunulur (m. 43/3).
- **EPDK (elektrik):** bilgi isteme ya da yerinde incelemede aykırılık hâlinde on beş gün, mevzuata aykırılıkta otuz gün içinde düzeltme ihtarı; Kurul ihtar sürelerini fiilin niteliğine göre farklı uygulayabilir; idari para cezaları tebliğden itibaren bir ay içinde ödenir (6446 m. 16/1-a, b; 16/2; 16/8). Tutarları matter'a yazma; ihtar yazısındaki süreyi esas al.
- **KVKK dosyaları:** süreler `/privacy-legal:matter-workspace` listesinde.
- **Diğer kurumlar (BDDK, SPK, BTK, GİB, TCMB):** süreyi özel kanundan ve tebliğ edilen yazıdan çek; ezberden süre yazma. İdari para cezasına karşı yargı yolu ve süresi özel kanuna göre değişir — **tartışmalı, içtihadı kontrol et:** `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="<kurum> idari para cezası görevli yargı yeri")`; dönen kararın künyesini birebir kullan.

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar:

| Slug | Müvekkil | Kurum | Tür | En yakın süre | Durum | Açılış | Aktif |
|---|---|---|---|---|---|---|---|

Aktif olanı `*` ile işaretle. `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

1. `matters/<slug>/matter.md` var mı bak; yoksa `new <slug>` öner.
2. `Active matter: <slug>` olarak güncelle.
3. Doğru matter'da olduğunu teyit etmesi için `matter.md` özetini göster (kurum ve en yakın süre dahil).

### `close <slug>`

1. `matters/<slug>/` var mı bak.
2. `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle.
3. `matters/<slug>/` → `matters/_archived/<slug>/` taşı.
4. Kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap.

### `none`

Yalnız `Active matter:` satırını `none — practice-level context only` yapar; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar ve kurum
**Müvekkil:** [ad] · **Kurum:** [ad] · **Karşı taraf / ilgililer:** [ad(lar)]

## Matter türü
[tür — tek satır gerekçe]

## Kritik süreler
- [ör. soruşturma raporu tebliği: …, savunma son günü: …; düzenleyici işlemin RG tarihi: …, dava süresi sonu: …]

## Ana olgular
[2-5 cümle; ilgili düzenleme ve RG künyesi araçtan]

## Matter'a özel sapmalar
- [ör. "Bu kurum için günlük tarama; ev standardı haftalık."]

## İlgili matter'lar
- [slug — neden ilgili]

## Gizlilik notu
[Yüksek / kapalı ekipse nedeni; dosyaları kim görebilir; genel ayar açık olsa bile çapraz bağlama izin var mı]
```

## `history.md` başlangıcı

```markdown
# Geçmiş: [Müvekkil] — [kısa tarif]

Yalnız ekleme yapılan olay günlüğü; en yeni üstte.

---

## [YYYY-AA-GG] — Matter açıldı

Ön görüşme tamamlandı. Slug: `[slug]`. Durum: aktif.
[matter.md dışında saklanmaya değer ilk bağlam — ör. "Kurumun bilgi isteme yazısı üzerine açıldı."]
```

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurma yasağını (Av. K. m. 36) ve aynı büroda zıt tarafların bulunabilmesinden doğan çatışma riskini (m. 38) destekler. Soruşturma dosyalarındaki rakip bilgisi ve ticari sırlar özellikle ayrı tutulur.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş taslak görüşümüzde EPDK'ya karşı aldığımız duruşu karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil; kapalı matter'lar çatışma kontrolü ve saklama amacıyla okunur kalır.
- **Süre hesabını kesinleştirmez** — listedeki süreler başlangıç noktasıdır; tebliğ tarihini ve özel kanunu avukat teyit eder.
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.

---

## /regulatory-legal:policy-diff

---
name: policy-diff
description: Belirli bir düzenleme değişikliğini dizinlenmiş politika kütüphanesiyle karşılaştırır. Bir kanun, yönetmelik, tebliğ ya da Kurul kararı değiştiğinde hangi politikalara dokunduğunu ve açığın ne olduğunu bulmak için; "bu düzenlemeyi politikalarımızla karşılaştır", "hangi politikayı etkiliyor", "açık analizi" denince ya da reg-feed-watcher önemli bir kalemi devrettiğinde kullan.
argument-hint: "[düzenlemenin adı ya da künyesi, veya metni/özeti yapıştırın]"
---

# /policy-diff

1. Profili yükle: `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → `## Policy library` (`**Location:**`, `**Policies indexed:**` tablosu: Policy, File, Last updated, Owner).
2. Aşağıdaki iş akışını uygula.
3. Düzenlemeden gereklilikleri çıkar; dizinlenmiş politikalarla eşle.
4. Çıktı: gereklilik bazında açık analizi ve güncellenmesi gereken politika.

---

## Matter context

Eklenti profilinde `## Matter workspaces` → `Enabled` `✗` ise (şirket içi kullanımda varsayılan) bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/regulatory-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

---

## Amaç

Bir düzenleme değişti; politikalarınız var. Bu skill değişikliğin hangi politikalara dokunduğunu ve "düzenlemenin artık istediği" ile "politikanın söylediği" arasındaki açığı bulur. Yalnız KVKK'ya dokunan ve aydınlatma, VERBİS, başvuru süreçlerine inen ayrıntılı analiz için `/privacy-legal:reg-gap-analysis` daha uygundur; İK el kitabı değişikliği için `/employment-legal:handbook-updates`.

## Bağlamı yükle

`## Policy library` → politikalar, dosya yerleri, sahipler. `company-profile.md` → [ŞİRKET ADI]'ın faaliyetleri, lisansları, halka açıklığı (gerekliliğin uygulanıp uygulanmadığını anlamak için).

## Kapsam bütünlüğü

Kullanıcı bir politika bölümünü, gerekliliği ya da kategoriyi karşılaştırma dışında bırakmak isterse:

1. Bırak — kapsam kullanıcınındır.
2. Ama yüksek sesle ve kalıcı olarak işaretle: "⚠️ KAPSAM SINIRI: [X] bölümü kullanıcı isteğiyle dışarıda bırakıldı. Bu karşılaştırma politikanın tamamını yansıtmaz. Dışarıda kalan alandaki açıklar BELİRLENMEDİ." Üst başlığın üstüne koy; sonraki her çıktıya taşı.
3. gap-surfacer'a da ilet: "Bu karşılaştırmanın kapsamı daraltıldı; tam uyum resmi olarak sunulmasın." Bu karşılaştırmadan doğan her açık kaydına başlığı aynen taşı.
4. Dışarıda bırakmanın sonucunu söyle: "Tedarikçi yönetimini dışarıda bırakmak, sonuçta 'tedarikçi yönetimini ele alan politika yok' görünmesine yol açar; bu, açığı göstermekten daha kötüdür."

Açıklanmamış bir kapsam daraltmasına dayanan uyum belgesi, sonradan bir denetim ya da uyuşmazlıkta gizleme gibi görünür. İşaret "incelemeyi daralttık" ile "sorunu sakladık" arasındaki farktır.

## İş akışı

### Adım 0: Karşılaştırmadan önce kuralın durumunu doğrula

Kuralı politikaya karşı koymadan önce gerçekten yürürlükte olduğunu teyit et. Uyarı işaretleri:
- Yürürlük ya da uyum tarihi 30 günden fazla geçmiş ama ertelenmediğine dair teyit yok; ya da yürürlük ileri tarihli, geçiş süresi var.
- Kural 12 aydan eski.
- Tartışmalı bir düzenleme; dava ya da AYM başvurusu konusu olabilir.

İşaret görürsen kontrol et:
- **Konsolide metin ve dipnotlar:** `tr_mevzuat_madde_getir(number="<no>", madde_no=[...])` (kurum düzenlemesinde `mevzuat_id`) → `annotations` alanındaki "(Değişik: …)", "(Ek: …)", "(Mülga: …)", "(İptal …)" notları. Mülga hükmü yürürlükte gösterme.
- **Geçiş hükmü:** geçici maddeleri ayrıca çek (`madde_no="geçici 3"`). Örnek: 7499 sayılı Kanunla değişen KVKK m. 9'un eski birinci fıkrası, değişik hâliyle birlikte 1/9/2024'e kadar uygulanmaya devam etti (KVKK geçici m. 3/1).
- **AYM:** `tr_aym_ara(kind="norm", query="<kanun no ve adı>")`. Kanun ya da CB kararnamesi hükmü, iptal kararının Resmî Gazete'de yayımlandığı tarihte yürürlükten kalkar; AYM iptalin yürürlüğe gireceği tarihi ayrıca kararlaştırabilir (yayımdan başlayarak en çok bir yıl); iptal kararları geriye yürümez (Anayasa m. 153/3, 153/5).
- **Danıştay (yönetmelik, tebliğ, düzenleyici Kurul kararı):** `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="\"<düzenleme adı>\" iptal")`; dönen kararın künyesini birebir kullan. Dava açılması işlemin yürütülmesini durdurmaz; yürütmeyi durdurma ayrı şartlara bağlı bir karardır (İYUK m. 27/1, 27/2). Yalnız dava açılmış olması kuralı askıya almaz.
- **Sonraki değişiklik:** `tr_resmi_gazete_tara(query="<düzenleme adı>", date_from="<yayım tarihi>")` (60 günlük dilimlerle).

Teyit edersen devam et. Araç yoksa ya da teyit edemiyorsan, üst başlıktan önce, her şeyin üstüne şu başlığı koy:

> `⚠️ KURAL DURUMU DOĞRULANMADI — Bu kuralın şu anda yürürlükte olduğunu teyit edemedim. Yayımlanan düzenlemeler sonradan değiştirilebilir, ertelenebilir, iptal edilebilir ya da yürütmesi durdurulabilir. Durumunu mevzuat.gov.tr, Resmî Gazete ve AYM/Danıştay kararlarından ya da dış avukattan teyit etmeden aşağıdaki tarihleri bağlayıcı sayma.`

Her son tarihi etiketle: `[yayımlanan metne göre — durum doğrulanmadı]`. Belirsizlik aşağı akar: açığı gap-surfacer'a devrederken `status_verified: false` yaz ki yayımlanmış bir tarih tek başına onu Overdue kovasına taşımasın.

### Adım 1: Yeni gereklilikleri çıkar

**Sessiz tamamlama yok.** Düzenleme metni eksik ya da belirsizse ve tamamı kaynaktan alınamıyorsa dur ve sor. Web araması ya da model bilgisiyle doldurma: "Elimde [olan] var. Gereklilikleri doğru çıkarmak için [eksik] gerekiyor. Seçenekler: (1) tam metni yapıştırın, (2) birincil kaynağı gösterin, (3) web araması — sonuçlar `[web araması — doğrula]` etiketi taşır ve kurumun sitesinden kontrol edilmelidir, (4) burada durmak. Hangisi?" Düşük güvenilirlikteki kaynağı kabul etme kararı avukatındır.

Metni araçla çek:
- Yayımlanan değişiklik metni: `tr_resmi_gazete_getir(url="<fihrist url>")`.
- Konsolide madde: `tr_mevzuat_madde_getir(number="<no>" | mevzuat_id="<id>", madde_no=[...])` (en çok 10); kimlik için `tr_mevzuat_ara`.
- Kurul kararı: `tr_kurum_karari_getir(kurum="<kurum>", id="<id>")`.
- Yabancı: `eu_get_document_text`, `uk_get_section`, `de_norm_getir` vb.; listede olmayan ülke için "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

**Kaynak etiketi.** Düzenleme künyesi, atıflar ve politika alıntıları dâhil her öğeye nereden geldiğini yaz: `[ArthurLegal TR — <araç> — GG.AA.YYYY]`, `[politika kütüphanesi]`, `[web araması — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`. Etiketleri silme.

Her ayrık yeni ya da değişen gerekliliği listele:

| # | Gereklilik | Yürürlük / geçiş | Atıf (araçtan dönen `citation`) |
|---|---|---|---|
| 1 | [ne istiyor] | [tarih] | [madde/fıkra] |

Somut ol. "Bildirim yükümlülükleri güçlendirildi" bir gereklilik değildir. "Standart sözleşme, imzaların tamamlanmasından itibaren beş iş günü içinde Kuruma bildirilir; bildirimi kimin yapacağı sözleşmede belirlenmemişse veri aktaran bildirir" bir gerekliliktir (Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik m. 14/5).

### Adım 2: Politikalarla eşle

Her gereklilik için en yakın dizinlenmiş politika hangisi?
- **Doğrudan:** politika bu konuyu açıkça ele alıyor.
- **Dolaylı:** politika ilgili bir konuyu ele alıyor; bu yeni bir alt konu.
- **Eşleşme yok:** hiçbir politika ele almıyor — açık "politika yok"tur.

Türk mevzuatında değişiklik çoğu zaman kanundan değil ikincil düzenlemeden gelir; eşlerken dayanak zincirini izle. Doğrulanmış örnekler:

| Alan | Tipik politika | Dayanak zinciri |
|---|---|---|
| Kişisel veri (6698) | Veri güvenliği, yurt dışı aktarım, tedarikçi yönetimi | Teknik ve idari tedbir yükümlülüğü (m. 12/1); yurt dışı aktarım yeterlilik kararı → uygun güvence → arızi istisna sırasıyla (m. 9/1, 9/4, 9/6); usul ve esaslar yönetmelikle (m. 9/11) → `KKY` türünü izle. |
| Bankacılık (5411) | Müşteri sırrı, veri paylaşımı, dış hizmet | Müşteri sırrı, istisnalar dışında, açık rıza alınsa dahi müşteri talebi ya da talimatı olmadan üçüncü kişilerle paylaşılamaz (m. 73/3); paylaşımın kapsam, usul ve esaslarını Kurul belirler (m. 73/5) → BDDK düzenlemelerini izle. |
| Sermaye piyasası (6362) | İçsel bilgi ve özel durum açıklama politikası | Değeri, fiyatı ya da yatırım kararını etkileyebilecek bilgi kamuya açıklanır; açıklama, erteleme usul ve esaslarını Kurul belirler (m. 15/1, 15/2) → SPK tebliğleri ve haftalık bülten. |
| Elektrik piyasası (6446) | Lisans uyumu, Kuruma bilgi verme, piyasa işlemleri | Lisans hak ve yükümlülükleri Kurum yönetmeliğiyle düzenlenir (m. 5/1); lisans sahibi istenen bilgi ve belgeyi zamanında, tam ve doğru verir ve faaliyet alanına göre mevzuatın gereklerini yerine getirir (m. 5/2-d, 5/2-e); ikincil mevzuata, Kurul kararına aykırılık ihtar ve idari para cezasına bağlıdır (m. 16/1-b) → EPDK yönetmelik ve Kurul kararları. |
| İş sağlığı ve güvenliği (6331) | Risk değerlendirmesi, acil durum, eğitim | İşveren risk değerlendirmesi yapmak ya da yaptırmakla yükümlüdür (m. 10/1); ayrıntılar Bakanlık yönetmelikleriyle düzenlenir (m. 30/1) → `YONETMELIK` türünü izle. |
| Rekabet (4054) | Rekabet uyum programı, dağıtım ve bayilik | Rekabeti kısıtlayan anlaşma, uyumlu eylem ve teşebbüs birliği kararları yasaktır (m. 4); Kurul belirli anlaşma türleri için grup muafiyeti tebliğleri çıkarabilir (m. 5/4) → tebliğ değişikliği dağıtım sözleşmelerine ve uyum politikasına dokunur. |

Tutar ve eşikleri (idari para cezası, sermaye, ciro) politikaya sabit yazma; "güncel tutarı teyit et (dönemsel güncellenir)" de.

### Adım 3: Karşılaştır

Her doğrudan ve dolaylı eşleşmede politikayı oku ve karşılaştır:

```markdown
### Gereklilik [N]: [ad]

**Yeni kural istiyor:** [gereklilik + atıf + kaynak etiketi]

**Politikamız ([ad], son güncelleme [tarih]) diyor ki:**
> "[ilgili alıntı]"

**Açık:** [Yok — politika zaten karşılıyor | Kısmi — politika X'i ele alıyor ama Y'yi değil | Tam — politika çelişiyor ya da hiç değinmiyor]

**Gereken değişiklik:** [somut — "X hakkında paragraf ekle", "politikayı güncelle" değil]

**Politika sahibi:** [kütüphaneden]
```

Düzenleme iki türlü okunabiliyorsa ikisini de yaz ve "tartışmalı — içtihadı ve kurum kararlarını kontrol et" diye işaretle; aranacak sorguyu ver (`tr_ictihat_ara`, `tr_semantik_ara(kurum=…)`), karar numarasını ezberden yazma.

### Adım 4: Eşleşmeyen açıklar

```markdown
### Yeni politika gerekli

Gereklilik [N]: [gereklilik]

Bunu karşılayan politika yok. Seçenekler:
- Yeni politika yaz (önerilen sahip: [en yakın konunun sahibi])
- [İlgili politika]ya yeni bölüm olarak ekle
- Politika gerektirmediğine karar ver (tek seferlik uyum işi, sürekli değil)
```

## Girdi türüne göre dallar

### Kural öncesi dalı (görüşe açılmış taslak ya da istişare)

Girdi görüşe açılmış bir taslak, taslaksız bir istişare ya da TBMM'deki bir kanun teklifiyse tam açık kapatma karşılaştırması YAPMA; **ön konumlanma analizi** üret:
- Kural yayımlanırsa (bugün değil) değişmesi muhtemel politikaları say.
- Taslağın konularından biri [ŞİRKET ADI]'ın uygulamasıyla görüş vermeyi gerektirecek biçimde kesişiyor mu, işaretle.
- Görüş son tarihini ve `**Default comment decision owner:**`'ı yaz; karar için `/regulatory-legal:comments`.
- Gereklilik bazında "açık yok" satırları üretme; karşılaştırılacak gereklilik yok. Gelecekteki etkiyi ve dokunacağı politikaları tek paragrafta yaz.

### Olumsuz bulgu dalı (yanlış hedef politikaya karşı karşılaştırma)

Çıkarılan her gereklilik "[adı geçen politikaya] karşı açık yok" çıkıyorsa tam analiz üretme; tek kısa paragrafa indir:

```markdown
## Politika Karşılaştırması: [Düzenleme] — [Politika]

[DÜZENLEME] [POLİTİKA] için değişiklik gerektirmiyor görünüyor. [POLİTİKA] §[X]
[Y]'yi zaten karşılıyor. Bu düzenlemenin gerçekten dokunduğu politikalar
[politika-1] ve [politika-2] — `/regulatory-legal:policy-diff`'i onlara karşı yeniden çalıştırın.

[Sonraki döngüde — ör. "yıllık politika gözden geçirmesinde"] ya da
[tetikleyici — ör. "kural değişirse ya da geçiş süresi biterse"] yeniden bakın.
```

Bir paragraf, bir öneri, bir yönlendirme notu. Yanlış hedefe karşı olumsuz bulgu bir yönlendirme sorunudur, uyum analizi değildir.

### Açık dalı (en az bir açık bulunan yayımlanmış kural)

Aşağıdaki tam çıktı. Ayrıntılı biçim gerçekten açık bulan karşılaştırmalar içindir.

## Çıktı

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

## Politika Karşılaştırması: [Düzenleme adı]

**Düzenleme:** [araçtan dönen citation, bağlantı]
**Yürürlük:** [tarih; geçiş hükmü varsa]
**Kural durumu:** [doğrulandı — kaynak, tarih | doğrulanmadı — yukarıdaki başlığa bakın]
**Çıkarılan gereklilik:** [N]

### Sonuç

[N açık [tarih]e kadar işlem gerektiriyor — ilk üçü: X, Y, Z]

### Özet

| # | Gereklilik | Etkilenen politika | Açık | Sahip |
|---|---|---|---|---|
| 1 | [kısa] | [politika ya da "yok"] | Yok/Kısmi/Tam | [ad] |

### Ayrıntılı karşılaştırmalar

[Adım 3'teki bloklar]

### Gereken yeni politikalar

[Adım 4'ten, varsa]

### Açık olmayan gereklilikler

[Liste — neyin zaten karşılandığını bilmek işe yarar]

---

**Atıfları doğrula.** Yukarıdaki künyeler ve politika atıfları yapay zekâ desteğiyle üretildi. Bir gerekliliğe dayanarak işlem yapmadan önce kuralı Resmî Gazete, mevzuat.gov.tr ya da kurumun sitesinden doğruluk, yürürlük tarihi ve güncel durum bakımından kontrol et. Her gereklilikteki kaynak etiketi künyenin nereden geldiğini gösterir; `doğrula` etiketliler önce kontrol edilir.
```

## Ayar eksikse

- **Politika kütüphanesi boş:** her gerekliliği varsayılan olarak "politika eşleşmesi yok" işaretle ve ekle: "Profilinizdeki `## Policy library` boş; bu yüzden her gereklilik yeni politika açığı olarak işaretlendi. Bunları karşılayan politikalarınız varsa `/regulatory-legal:cold-start-interview --redo` ile ya da profili düzenleyerek kütüphaneye ekleyin ve karşılaştırmayı yeniden çalıştırın."
- **Eşleşen politikanın sahibi yok:** Özet tablosunda Sahip hücresini boş bırak ve ekle: "[Liste] için politika sahibi tanımlı değil. gap-surfacer'ın yönlendirebilmesi için `## Policy library` tablosunun Owner sütununu doldurun."

Kütüphane doluysa ve sahipler tanımlıysa ayardan söz etme.

## Devir

gap-surfacer'a: her Kısmi ya da Tam açık, sahibi ve son tarihiyle izlenen bir kayıt olur (`status_verified` Adım 0'a göre; kapsam sınırı varsa başlığıyla).

## Kapanış

Profildeki `## Outputs` karar ağacıyla bitir; seçenekleri bu çıktıya uyarla (politika taslağını yaz → `/regulatory-legal:policy-redraft`, eskale et, olgu topla, izle ve bekle, başka bir şey). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Politika güncellemelerini yazmaz; neyin güncellenmesi gerektiğini bulur. Taslak için `/regulatory-legal:policy-redraft` ya da insan.
- Belirsiz düzenleyici metni kesin olarak yorumlamaz. İki türlü okunabiliyorsa söyler ve avukata işaretler.
- Tutar ve eşikleri sabitlemez; dönemsel güncellenen her rakam için güncel değerin teyidini ister.

---

## /regulatory-legal:policy-redraft

---
name: policy-redraft
description: /regulatory-legal:gaps ya da /regulatory-legal:policy-diff'in bulduğu bir açığı kapatan, işaretli (redline) bir politika taslağı önerir. İç inceleme için ilk taslaktır; onaylı politika belgesine doğrudan uygulanmaz. "Politikayı yeniden yaz", "politika düzeltmesini taslakla", "politikayı işaretle" denince ya da gap-surfacer bir açığı taslak için devrettiğinde kullan.
argument-hint: "[GAP-ID ya da açığın tarifi]"
---

# /policy-redraft

1. Profili yükle: `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → `## Policy library` ve uygulama profili; ortak bilgi için `company-profile.md`.
2. Aşağıdaki iş akışını uygula.
3. Girdileri topla: açık (`/regulatory-legal:gaps` çıktısından ya da doğrudan tarif), güncel onaylı politika metni, kural metni.
4. Kuralın güncel olduğunu doğrula (policy-diff Adım 0). Doğrulayamazsan `⚠️ KURAL DURUMU DOĞRULANMADI` başlığını koy.
5. Etkilenen politika bölümlerinin işaretli taslağını üret: mümkün olan en küçük değişiklik, `[doğrula]` etiketleri taşınır, her değişikliğin NEDENİ satır içi yorumla açıklanır.
6. Politika Yeniden Yazım Notu üret. `[policy-name]-proposed-redraft-[YYYY-MM-DD].md` adlı yeni bir dosyaya yaz — kaynak politika belgesine asla yazma.
7. İzleyicide açığı KAPATMA. Açık, taslak uygulanıp ONAYLANDIĞINDA kapanır; bu politika sahibinin işidir.

---

> Bu skill bir **öneri** üretir, düzenleme yapmaz. Açıkça taslak olduğu belli bir adla yeni dosyaya yazar. Kaynak politika belgesinin üzerine asla yazmaz ve izleyicide açığı asla kapatmaz — açık, taslak politika sahibince uygulanıp onaylandığında kapanır.

## Matter context

Eklenti profilinde `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/regulatory-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

---

## Amaç

gap-surfacer açığı bulur; policy-diff neyin değişmesi gerektiğini söyler. Bu skill bir adım ileri gider ve etkilenen politika bölümünün işaretli taslağını üretir: küçük, somut, etiketli; politika sahibinin incelemesi için ilk taslak.

## Kesin sınırlar — önce bunları oku

Bunlardan biri çiğnenecekse dur ve sor.

1. **Bu bir ÖNERİDİR, düzenleme değil.** Kaynak politika belgesine asla doğrudan yazma. Çıktı `[policy-name]-proposed-redraft-[YYYY-MM-DD].md` adlı yeni dosyaya ya da matter çalışma alanına gider; `[policy-name].md`'ye değil.
2. **İzleyicide açığı asla kapatma.** Açıklar taslak UYGULANIP ONAYLANDIĞINDA kapanır; bu politika sahibinin işidir. Kullanıcı "taslağı yazdın, açığı kapat" derse reddet: "Ben öneriyi üretiyorum. Açık, değişikliği inceleyip uygulayıp onayladığınızda kapanır. O zaman söyleyin, izleyiciyi güncellerim."
3. **"Bunu benim yerime uygula" kapsam dışıdır.** Kullanıcı taslağı kaynak politikaya uygulamamı isterse: "Politika değişikliğini ben uygulamam; inceleme ve onaydan sonra politika sahibinin işidir. Öneriyi ben üretirim. İncelenip onaylandığında söyleyin, açık izleyiciyi güncellerim."
4. **Taslaktan önce politika sürümünü teyit et.** Dosya verildiyse sor: "Bu politikanın onaylı ve en güncel sürümü mü? Eski bir sürüme karşı yazılan taslak ayrışma yaratır." Metin yapıştırıldıysa güven ama inceleyen notunda işaretle.
5. **Mümkün olan en küçük değişiklik.** Cümleden önce kelime, paragraftan önce cümle, bölümden önce paragraf çiz. Yalnız açıktan etkilenen bölümlere dokun. Politikanın üslubunu yeniden düzenleme.
6. **`[doğrula]` etiketlerini taşı.** Model bilgisinden ya da doğrulanmamış kaynaktan gelen her yürürlük tarihi, eşik, atıf ya da gereklilik yalnız notta değil, taslağın içinde de etiketlenir. Dönemsel güncellenen tutarları (idari para cezası, parasal sınırlar) politikaya sabit yazma; "güncel tutar [doğrula]" diye bırak.

## Adım 1: Girdileri topla

Üç girdi gerekir. Biri eksikse sor; çıkarsama yapma.

### 1a. Açık

Biri:
- İzleyiciden bir `GAP-ID` — kaydı `~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml` dosyasından (ya da matter düzeyindeki karşılığından) yükle.
- Kullanıcının mesajında tarif edilen açık — gerekliliği, düzenlemeyi ve etkilenen politikayı yakala.
- `/regulatory-legal:policy-diff` çıktısından yapıştırılan karşılaştırma özeti.

### 1b. Güncel politika metni

Biri:
- Dosya yolu — oku, sonra sor: "Bu politikanın onaylı ve en güncel sürümü mü?" Cevabı inceleyen notuna yaz.
- Yapıştırılmış metin — güven ama inceleyen notunda işaretle: "Politika metni doğrudan yapıştırıldı; güncel onaylı sürüm olduğunu varsaydım. Uygulamadan önce teyit edin."
- Hiçbiri — iste. Politika metnini izleyiciden ya da web aramasından tahmin etme.

### 1c. Kural metni

Biri:
- Karşılaştırma çıktısı (kural çıkarılmış ve etiketlenmiş).
- Araçla çekilmiş düzenleme: `tr_mevzuat_madde_getir`, `tr_resmi_gazete_getir`, `tr_kurum_karari_getir` — `citation` alanı birebir, kaynak etiketiyle.
- Kullanıcının yapıştırdığı kural metni — `[kullanıcı verdi]`.

Kural metni eksik ya da belirsizse **sessiz tamamlama yok** kuralını uygula: seçenekleri sun (tam metni yapıştır, birincil kaynağı göster, `doğrula` etiketli web araması, dur) ve bekle.

## Adım 2: Kuralın güncel olduğunu doğrula

policy-diff Adım 0'daki kontrolü aynen uygula: konsolide metindeki "(Değişik/Ek/Mülga/İptal)" notları ve geçici maddeler, AYM norm denetimi (`tr_aym_ara(kind="norm", …)`), Danıştay iptal ya da yürütmeyi durdurma (`tr_ictihat_ara(courts=["DANISTAYKARAR"], …)`), sonraki RG değişiklikleri. Uyarı işaretleri: yürürlük tarihi 30 günden fazla geçmiş ve ertelenmediği teyit edilmemiş; kural 12 aydan eski; tartışmalı ve dava konusu olabilecek bir düzenleme.

Doğrulayamazsan:

> `⚠️ KURAL DURUMU DOĞRULANMADI — Bu kuralın şu anda yürürlükte olduğunu teyit edemedim. Yayımlanan düzenlemeler sonradan değiştirilebilir, ertelenebilir, iptal edilebilir ya da yürütmesi durdurulabilir. Durumunu mevzuat.gov.tr, Resmî Gazete ve AYM/Danıştay kararlarından ya da dış avukattan teyit etmeden bu taslağı uygulamayın.`

Bu başlığı üst başlığın üstüne koy. Taslaktaki her yürürlük ve uyum tarihini `[yayımlanan metne göre — durum doğrulanmadı]` diye etiketle.

## Adım 3: Taslağı üret

Etkilenen politika bölümünün işaretli hâli.

### Kural

- Çizilen metin: `~~çizilen metin~~`
- Eklenen metin: **eklenen metin**
- Her değişiklik NEDENİNİ açıklayan satır içi yorum taşır — kural, atıf, kapanan açık:

  > `[Değişiklik: standart sözleşmenin Kuruma bildirimi eklendi — imzaların tamamlanmasından itibaren beş iş günü; bildirim tarafı sözleşmede belirlenmemişse veri aktaran (Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik m. 14/5) [ArthurLegal TR — tr_mevzuat_madde_getir — GG.AA.YYYY]]`

- Model bilgisinden ya da doğrulanmamış kaynaktan gelen her yürürlük tarihi, eşik, atıf ya da gereklilik satır içinde `[doğrula]` etiketi alır; yalnız değişiklik özetinde değil.
- Karşılaştırmadan gelen kaynak etiketlerini taşı: `[ArthurLegal TR — <araç> — GG.AA.YYYY]`, `[web araması — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`. Karşılaştırmadan taslağa geçerken silme.

### Kapsam disiplini

Politikanın bir bölümü açıktan etkilenmiyorsa ona dokunma. Açığın dışındaki bölümlere dokunan taslak, yapay zekânın sorulmadığı konularda görüş bildirdiği izlenimini verir ve incelemeyi zorlaştırır.

Taslağı yazarken ikinci bir açık görürsen (kuralla açıkça uyumsuz ama asıl açıkta olmayan bir hüküm) sessizce düzeltme. İnceleyen notunda işaretle: "[GAP-ID] için taslak yazarken [diğer hüküm]ün [gereklilik] ile ilgili bir sorunu olduğunu fark ettim. Bu taslağa dahil edilmedi. Ayrı bir açık açılmasını düşünün."

## Adım 4: Çıktı — Politika Yeniden Yazım Notu

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

> **⚠️ İnceleyen notu**
> - **Kaynaklar:** [ArthurLegal MCP (`tr_`) ✓ doğrulandı | bağlı değil — atıflar model bilgisinden, dayanmadan önce doğrula]
> - **Okunan:** [politikanın incelenen bölümleri; okunmayanlar]
> - **Takdirinize bırakılan:** [satır içinde `[incele]` işaretli N kalem | yok]
> - **Güncellik:** [kural durumu [kaynak], [tarih] itibarıyla doğrulandı | doğrulanmadı — yukarıdaki başlığa bakın]
> - **Dayanmadan önce:** bunun politikanın güncel onaylı sürümü olduğunu teyit et; kuralın durumunu ve yürürlük tarihini doğrula; politika sahibinin incelemesini al; politika değişikliği onay sürecini izle; açık izleyiciyi yalnız uygulanıp onaylandığında güncelle.

## Politika Yeniden Yazımı: [Politika adı]

**Açık:** [GAP-ID ya da kısa tarif]
**Düzenleme:** [araçtan dönen citation, yürürlük tarihi]
**Politika:** [ad, son güncelleme tarihi]
**Durum:** ÖNERİ — henüz incelenmedi ya da onaylanmadı

### Sonuç

[Bir cümle: açık ne. Bir cümle: taslak ne yapıyor. Bir cümle: neyin incelenmesi gerekiyor.]

### İşaretli politika bölüm(ler)i

[Satır içi `[Değişiklik: ...]` yorumlarıyla işaretli metin. Yalnız etkilenen bölümler.]

### Değişiklik özeti

| # | Hüküm | Mevcut | Önerilen | Neden | Kaynak |
|---|---|---|---|---|---|
| 1 | §3.2 Yurt dışı aktarım dayanağı | "…kişisel verileri ilgili kişinin açık rızasıyla yurt dışına aktarırız…" | "…yeterlilik kararı bulunan ülkelere; yoksa Kurulun ilan ettiği standart sözleşme gibi uygun güvencelerden biriyle; bunlar da yoksa yalnız arızi hâllerde aktarırız…" | 7499 s. Kanunla değişen KVKK m. 9: yeterlilik kararı → uygun güvence → arızi istisna (m. 9/1, 9/4, 9/6) | `[ArthurLegal TR — tr_mevzuat_madde_getir — GG.AA.YYYY]` |
| 2 | §3.5 Bildirim | (yok) | "Standart sözleşme değiştirilmeden kullanılır ve imzaların tamamlanmasından itibaren beş iş günü içinde Kuruma bildirilir." | KVKK m. 9/5; Yönetmelik m. 14/3, 14/5 | `[ArthurLegal TR — tr_mevzuat_madde_getir — GG.AA.YYYY]` |
| 3 | §6.1 İdari para cezası | "[tutar] TL'ye kadar" | "kanunda öngörülen idari para cezası" | Tutar dönemsel güncellenir; politikaya sabit yazılmaz | `[doğrula — güncel tutar]` |

### Uygulamadan önce — kontrol listesi

- [ ] Taslağın yazıldığı metnin politikanın güncel onaylı sürümü olduğunu teyit et.
- [ ] Kuralın durumunu ve yürürlük tarihini doğrula (mevzuat.gov.tr, Resmî Gazete, AYM/Danıştay ya da dış avukat).
- [ ] Politika sahibinin incelemesini al.
- [ ] Politika değişikliği onay sürecini izle.
- [ ] Açık izleyiciyi uygulanıp onaylandığında güncelle — öncesinde değil.

---

**Sırada ne var? Birini seçin, birlikte ilerletelim:**

1. **Uygula ve onay al** — siz incelersiniz, politika sahibine iletirsiniz, onay sürecinden geçirirsiniz. Onaylanınca söyleyin, açığı kapalı işaretlerim.
2. **[X] hakkında daha fazla bilgi** — bir değişikliğin dayanağı güçlendirilmeli mi (atıf doğrulama, tutar kontrolü, yabancı hukuk sorusu), hangisi olduğunu söyleyin, araştırayım.
3. **[Sahip / hukuk müdürü]ne eskale et** — taslak politika sahibinin yetkisini aşan bir şey doğuruyorsa olguları, önerilen değişikliği ve gereken kararı içeren kısa bir eskalasyon yazayım.
4. **İzle ve bekle** — kuralın durumu belirsizse ya da politika sahibine ulaşılamıyorsa açık izleyiciye yeniden değerlendirme notu ekleyeyim.
5. **Başka bir şey** — ne yapmak istediğinizi söyleyin.
```

## Dosya adı

Çıktı dosyasının adı taslak olduğunu açıkça göstermelidir:

`[policy-name]-proposed-redraft-[YYYY-MM-DD].md`

`[policy-name].md` değil. `[policy-name]-v2.md` değil. "proposed-redraft" sözcüğü ve tarih taşıyıcıdır; taslağın güncel sürümle karıştırılmasını önler.

Aktif matter varsa matter çalışma alanına; yoksa çalışma klasörüne ya da kullanıcının gösterdiği yere yaz. Politika kütüphanesinin kaynak klasörüne yazma.

## Ayar eksikse

- **Politika sahibi yok:** taslağı yine üret. İnceleyen notuna yaz: "`## Policy library` tablosunda [politika] için Owner tanımlı değil. Onay yolunun yönlendirilebilmesi için `/regulatory-legal:cold-start-interview --redo` ile atayın."
- **Politika kütüphanesi boş ve açık belirli bir politika göstermiyor:** dur ve sor: "Taslak için güncel politika metnine ihtiyacım var. Etkilenen politikanın metnini yapıştırın ya da dosyayı gösterin."

Değerler doluysa ayardan söz etme.

## Diğer skill'lerle ilişki

- **Girdiler** `policy-diff`ten (gereklilik bazında açık analizi) ve `gap-surfacer`dan (izleyici) gelir. Kaynak etiketlerini ve `[doğrula]` işaretlerini taşı.
- **İzleyici durumu:** bu skill izleyiciyi DEĞİŞTİRMEZ. Açığı kapalı ya da devam ediyor işaretlemez, `notified` alanına dokunmaz. Taslağın varlığına iz bırakmak istenirse, taslak uygulanıp onaylandığında politika sahibi ya da kullanıcı kapanış notuyla kaydı günceller — bkz. `/regulatory-legal:gaps --close`.
- **Önem tabanı:** yukarı akıştaki açık 🔴 ya da 🟠 ise notun Sonuç bölümü o önemi taşır. Sessizce düşürmek, inceleyen avukatın göremeyeceği bir çelişkidir. Bkz. profil `## Cross-skill severity floor`.
- **Konu skill'leri:** İK politikası için `/employment-legal:policy-drafting`; aydınlatma metni için `/privacy-legal:policy-monitor`.

## Kapanış

Karar ağacı yukarıdaki çıktı şablonunun içindedir. Seçenekleri taslağın gerçekte ürettiğine göre uyarla: kuralın durumu doğrulanmadıysa 2. seçenek (daha fazla bilgi) öne çıkar; politika sahibi tanımlı değilse 3. seçenek (eskalasyon) somutlaşır.

## Bu skill ne yapmaz

- Taslağı kaynak politikaya uygulamaz; bu politika sahibinin işidir.
- İzleyicide açığı kapatmaz; açıklar taslak uygulanıp onaylandığında kapanır.
- Politikanın tamamını yeniden yazmaz; açığı kapatan en küçük değişikliği yapar.
- Birden çok politikayı tek seferde yazmaz: bir açık, bir politika, bir not.
- "Uygula" iş akışını yürütmez; onay kapılı bir uygulama komutu ileride ayrı bir skill olabilir.

---

## /regulatory-legal:reg-feed-watcher

---
name: reg-feed-watcher
description: >
  Düzenleyici akışları şimdi kontrol eder (Resmî Gazete, mevzuat, sekiz düzenleyici kurumun
  kararları, AYM norm denetimi, izlenen yabancı yargı çevreleri) ve son kontrolden bu yana
  yeni olanı önemlilik eşiğine göre süzerek raporlar. "Akışları kontrol et", "yeni ne var",
  "mevzuat güncellemesi", "bu haftanın Resmî Gazete'si" denince, zamanlanmış ajan
  çalıştırdığında ya da kullanıcı bir düzenleyici gelişmeyi sınıflandırma ve politika
  karşılaştırması için yapıştırdığında kullan.
argument-hint: "[isteğe bağlı: --since YYYY-AA-GG]"
---

# /reg-feed-watcher

1. Profili yükle: `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → `## Regulators we watch` (watchlist), `## Materiality threshold`, `## Feed configuration`.
2. Aşağıdaki iş akışını uygula.
3. Her akışı çek; önemlilik eşiğine göre süz.
4. Çıktı: yeni olanlar, önem kademesine göre.

---

## Amaç

Akışı çek, önemliliğe göre süz, kalanı göster. Değer süzgeçtedir; süzülmemiş Resmî Gazete gürültüdür.

## Bağlamı yükle

- Eklenti profili (başlık ve anahtar adları İngilizce kalır; çevirme):
  - `## Regulators we watch` — watchlist tablosu (Regulator, Jurisdiction, Why we watch, Feed source).
  - `## Materiality threshold` — üç kademe: `**Always material (alert immediately):**`, `**Review-worthy (weekly digest):**`, `**FYI (monthly roundup or not at all):**`.
  - `## Feed configuration` — `**Free feeds (always active):**` tablosu (araç çağrısı, RSS ya da kurum duyuru sayfası), `**Paid feeds (if configured):**`, `**Manual entry:**`, `**Comment tracking:**`, `**Default comment decision owner:**`, `**Check cadence:**`, `**Digest channel:**`, `**Digest output path:**`.
- Ortak profil `company-profile.md`: [ŞİRKET ADI]'ın sektörü, lisansları, halka açık olup olmadığı, denetime tabi olduğu kurumlar. Watchlist'te eksik kurum varsa buradan anla.
- `source-catalog.md`: Türkiye, AB, Birleşik Krallık ve yaptırım kaynaklarının küratörlü listesi. Yeni kaynak yapılandırırken ya da kapsam boşluğu görürken kullan (Adım 0).
- `mevzuat-mcp-rehberi.md` bölüm 4: `konu` süzgecinin ölçülmüş sınırları.
- `reg-feed-haftalik-sablon.md`: müvekkile ya da şirket içine haftalık bülten biçimi isteniyorsa.

## İş akışı

### Adım 0: Kapsam kontrolü (çekmeden önce)

Watchlist ve feed yapılandırmasını `source-catalog.md` ile karşılaştır:
- Kullanıcı hangi kategorileri izliyor (Türk mevzuatı, Türk kurumları, AB/Birleşik Krallık, diğer yabancı, yaptırım)?
- Bunlardan hangisinde hiç ya da çok az kaynak yapılandırılmış?

Belirgin boşluk varsa digest'in başında **bir kez** göster. Türkiye'de sık görülenler:
- [ŞİRKET ADI] EPDK lisans sahibi ama `epdk` kurum akışı yapılandırılmamış.
- Halka açık ama SPK bülteni izlenmiyor; banka ya da finansal kuruluş ama BDDK yok.
- `**Comment tracking:**` Enabled ama `**Free feeds (always active):**` tablosunda hiçbir kurumun taslak duyuru sayfası yok. Görüşe açılan taslaklar Resmî Gazete'de yayımlanmaz ve ArthurLegal araçlarında taslak akışı yoktur; bu sayfa tanımlanmadan görüş süreleri kaçar.

> **Kapsam boşluğu:** Watchlist'inizde [kategori] var ama yalnız [N] kaynak yapılandırılmış. `source-catalog.md` bu kategoride [ör. 2-3 ad] öneriyor. Ekleyeyim mi? `/regulatory-legal:cold-start-interview --redo` çalıştırın ya da `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasını düzenleyin.

Aynı boşluğu her çalışmada tekrarlama. Kullanıcı "şimdilik X'i atla" dediyse uy ve bunu profile not et.

### Adım 1: Çek

Yapılandırılmış her katmandan çek. Tier 1 her kurulumda vardır; Tier 2 ve 3 eklenir.

Genel kurallar:
- `tr_` çağrılarını sırayla yap, aralarında birkaç saniye bırak (hız sınırı ortaktır).
- Her araç çağrısı 100 saniyede iptal edilir. Dar tut; iptal olursa aynı sorguyu tekrarlama, aralığı böl.
- Araç veri getiremezse (hata, `unavailable`, `upstream_blocked`) boş sonuç sayma. O kalem için şunu yaz: `UYARI: veri çekilemedi, teyidiniz gerekli: <aracın source_url'si ya da resmî giriş sayfası>`. Bağlantı uydurma.
- Pencere: `--since` verildiyse o tarih, yoksa son kontrol zamanı, o da yoksa son 7 gün.

**Tier 1 — Ücretsiz akışlar (her zaman açık): ArthurLegal MCP**

1. **Resmî Gazete (birincil akış).** Neyin yayımlandığının ölçüsü fihristtir; mevzuat araması RG akışını vermez.
   ```
   tr_resmi_gazete_tara(date_from="2026-10-19", date_to="2026-10-25", konu="enerji")
   tr_resmi_gazete_tara(date_from="2026-10-19", date_to="2026-10-25", query="Elektrik")
   tr_resmi_gazete_tara(date_from="2026-10-19", date_to="2026-10-25", query="Kişisel Veri")
   ```
   - `konu` yalnız `enerji`, `rekabet`, `vergi`, `icra` alır. Başlığında konu adı geçmeyen kalemi de bulur ama bir ön elemedir. Sonucu `query` ile tamamla; enerji taramasında `konu`'ya tek başına güvenme (elektrik, doğal gaz, petrol, lisans, EPDK ile ikinci tarama).
   - Dört konu dışındaki alanlar (KVKK, iş hukuku ve İSG, sermaye piyasası, bankacılık) yalnız `query` ile taranır.
   - Yanıttaki `konu_elenen` sayısını digest'e yaz. "Bu hafta başka bir şey çıkmadı" deme; "konu süzgecinden geçenler bunlar, N kalem elendi" de.
   - Tek çağrı en çok 60 gün tarar; uzun pencereyi böl.
   - Tek gün ya da mükerrer sayı: `tr_resmi_gazete_fihrist(date="2026-10-24", mukerrer=1)`.
   - Değişiklik metni, yürürlük maddesi ve geçiş hükmü: `tr_resmi_gazete_getir(url="<fihristteki url>")`.
   - Sonuçtaki `section` alanı (YÖNETMELİKLER, KURUL KARARLARI, CUMHURBAŞKANI KARARLARI vb.) sınıflandırmada ilk ipucudur.
2. **Mevzuat (kimlik ve konsolide metin).**
   ```
   tr_mevzuat_ara(types=["KANUN"], rg_date_from="2026-10-01", rg_date_to="2026-10-25", konu="vergi", max_pages=2)
   tr_mevzuat_ara(query="Elektrik Piyasası", types=["YONETMELIK", "KKY", "TEBLIGLER"], rg_date_from="2026-10-01")
   tr_mevzuat_ara(number="6446", types=["KANUN"])
   ```
   - Türler: `KANUN`, `KHK`, `CB_KARARNAME`, `CB_KARAR`, `CB_YONETMELIK`, `CB_GENELGE`, `YONETMELIK`, `KKY`, `UY`, `TEBLIGLER`.
   - RG tarih süzgeci RG tarihi boş kayıtları hiç getirmez ve konsolide veri tabanı yayımın gerisinde kalabilir. Boş sonuç "o dönemde düzenleme yok" demek değildir; yayımı RG fihristinden teyit et.
   - Torba kanun: `konu_kaynak: "degistirilen_kanunlar"` dönen kanunun hangi kanunları değiştirdiği `konu_degistirilen` alanındadır; `konu_kaynak: "belirsiz"` dönen kanunu `tr_mevzuat_getir` ile aç ve kendin karar ver.
3. **Kurum kararları** (yalnız watchlist'teki kurumlar):

   | Kurum | Çağrı | Not |
   |---|---|---|
   | EPDK | `tr_kurum_karari_ara(kurum="epdk", market="elektrik", year=2026, limit=20)` | `market`: elektrik, dogalgaz, petrol, lpg. Yalnız yapısal Kurul kararları; lisans tadilleri RG fihristindedir. Karar tarihi ile RG tarihi farklıdır; ikisini de yaz. |
   | Rekabet | `tr_kurum_karari_ara(kurum="rekabet", query="\"dikey anlaşma\"", decision_type="rekabet_ihlali")` | Çok kelimeli ifadeyi tırnakla. Kılavuz ve tebliğler mevzuattadır (`tr_mevzuat_ara`). |
   | SPK | `tr_kurum_karari_ara(kurum="spk", year=2026)` → son bülten no, sonra `tr_spk_bulten_icinde_ara(bulten="2026/74", query="idari para cezası")` | Kurul kararları haftalık bültendedir. |
   | BDDK | `tr_kurum_karari_ara(kurum="bddk", query="destek hizmeti", year=2026)` | Canlı arama başlıkta; metin için `tr_semantik_ara(kurum="bddk", query=…)`. |
   | KVKK | `tr_kurum_karari_ara(kurum="kvkk", params={"scan_pages": 3}, limit=30)` | Liste tarihe göre sıralı değil; `date` alanına bak. |
   | BTK | `tr_kurum_karari_ara(kurum="btk", date_from="2026-10-01", date_to="2026-10-25")` | Canlı arama başlıkta; gerekçe PDF'te. |
   | GİB | `tr_kurum_karari_ara(kurum="gib", query="<konu>", date_from="2026-10-01")` | Özelge bağlayıcı değildir; idarenin görüşüdür. |
   | Sigorta Tahkim | `tr_kurum_karari_ara(kurum="sigorta_tahkim", issue=<dergi sayısı>)` | Hakem kararı dergisi. |

   Arşivde ya da tarih aralığında konu araması: `tr_semantik_ara(kurum="<kurum>", query="<konu>", date_from="YYYY-AA-GG")`. Tam metin: `tr_kurum_karari_getir(kurum="<kurum>", id="<id>")`. Filtreleri görmek için `tr_kurum_listesi`.
4. **AYM norm denetimi** (watchlist'in dayandığı temel kanunlar için): `tr_aym_ara(kind="norm", query="6446 sayılı Elektrik Piyasası Kanunu")`. İptal kararları RG'de de yayımlanır; RG taramasında `query="Anayasa Mahkemesi"` ile yakalanır. İptal hükmü yayım tarihinde ya da AYM'nin belirlediği ileri tarihte yürürlükten kalkar (Anayasa m. 153/3); bu tarihi ayrıca yaz.
5. **Yabancı yargı çevreleri** (yalnız watchlist'te varsa):
   - AB: `eu_search_eu_law(query="electricity market", date_from="2026-10-01")`
   - Birleşik Krallık: `uk_search_legislation(title="Energy", year="2026")`; bir kanunun işlenmemiş değişiklikleri: `uk_get_effects(year="<yıl>", number="<no>", unapplied_only=true)`
   - Almanya: `de_recent_changes(since_iso="2026-10-19")`
   - Finlandiya: `fi_recent_changes()` (yalnız son değişen beş akt)
   - Hollanda, Polonya, Avusturya, İrlanda, İspanya, Japonya, Azerbaycan: kendi arama araçlarıyla (`nl_`, `pl_`, `at_`, `ie_`, `es_`, `jp_`, `az_`).
   - Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."
6. **Araç dışı kaynaklar.** KİK, Sayıştay, TÜRKPATENT ve İSTAÇ ArthurLegal'da yoktur (resmî uçları cevap vermiyor); bunlar için araç önerme, sonuç uydurma. TBMM'deki kanun teklifleri, KAP bildirimleri, kurumların taslak duyuruları, MASAK, KGK ve bakanlık duyuruları da araçlarda yoktur. Profilde sayfa adresi tanımlıysa (ajanda WebFetch ile) oku ve `[kurum sitesi]` etiketi koy; tanımlı değilse kullanıcının manuel girişine bırak. Yaptırım listeleri (OFAC, AB, Birleşik Krallık) için `source-catalog.md`.

**Tier 2 — Ek bağlayıcılar (`**Paid feeds (if configured):**`)**

Bağlıysa Thomson Reuters Regulatory Intelligence (son kontrolden bu yana, watchlist kurumlarına süzülmüş), kullanıcının kendi aboneliğiyle bağladığı başka veri tabanları ya da ABD için CourtListener (`courtlistener-rehberi.md`). Aynı belge birden çok kaynaktan gelebilir: teke indir, en zengin kaynağı kullan.

**Sessiz tamamlama yok.** Bir watchlist kurumu için akış az ya da hiç sonuç döndürürse bulduğunu raporla ve dur. Boşluğu web araması ya da model bilgisiyle doldurma; sor:
> "Akış kontrolü [N] kalem döndürdü ([kaynaklar]). [Kurum / konu] için kapsam ince görünüyor. Seçenekler: (1) tarih aralığını genişletmek, (2) başka bir araç ya da kaynak denemek, (3) web araması — sonuçlar `[web araması — doğrula]` etiketi taşır ve kullanılmadan önce kurumun sitesinden kontrol edilmelidir, (4) burada durmak. Hangisi?"

Daha düşük güvenilirlikteki kaynağı kabul etme kararı avukatındır.

**Kaynak etiketi.** Her kaleme nereden geldiğini yaz. Araçtan gelen kalem: `[ArthurLegal TR — <araç> — GG.AA.YYYY]` (ör. `[ArthurLegal TR — tr_resmi_gazete_tara — 26.10.2026]`, `[ArthurLegal TR — tr_kurum_karari_ara:epdk — 26.10.2026]`); yabancı araçta önek değişir (`[ArthurLegal EU — eu_search_eu_law — …]`). Diğerleri: `[TR Regulatory Intelligence]`, `[kurum sitesi]`, `[web araması — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`. `doğrula` etiketli kalemlerin uydurma riski daha yüksektir; önce onlar kontrol edilir. Etiketleri silme ya da birleştirme.

**İkincil kaynak.** Büro bültenleri, meslek kuruluşu ve dernek duyuruları, haber siteleri, Lexology ve benzeri yorumcular birincil kaynak değildir. Bunlardan gelen kaleme ayrıca `[ikincil kaynak]` etiketi koy ve şu notu ekle: "→ Birincil kaynağa git: RG fihristi ya da ilgili kurumun kararı; bulunmadan güvenme." İkincil kaynağa dayanan kalemi tek başına Always material yapma; birincil kaynak bulunana kadar bir kademe aşağıda tut.

**Tier 3 — Manuel giriş**

Kullanıcı düzenleme metnini ya da özetini yapıştırdıysa onu tek kalem say, Adım 2'ye geç, kaynağı `[kullanıcı verdi]` olarak kaydet. Akış çekmek gerekmez; abonelikten bağımsız çalışır.

Çektikten sonra kontrol zamanını kaydet; sonraki çalışma oradan başlar.

### Adım 2: Sınıflandır

Her kalem profildeki `## Materiality threshold` kademelerinden birine girer: `**Always material (alert immediately):**`, `**Review-worthy (weekly digest):**`, `**FYI (monthly roundup or not at all):**`. Profildeki madde listeleri aşağıdaki tablodan önce gelir; tablo yalnız profilin sessiz kaldığı kalem türleri için varsayılandır. Kademe etiketleri İngilizce kalır.

| Kalem türü | Eşik karşılığı |
|---|---|
| RG'de yayımlanan kanun, CB kararnamesi, CB kararı ya da yönetmeliği, kurum yönetmeliği, tebliğ | İzlenen faaliyete dokunuyorsa genelde Always material. Yürürlük tarihini ve geçiş hükmünü metnin kendisinden yaz. |
| RG'de yayımlanan ya da kurumun ilan ettiği düzenleyici Kurul kararı | [ŞİRKET ADI]'ın lisansı ya da faaliyetiyle eşleşiyorsa Always material. Örnek: elektrik piyasasında lisans sahibi faaliyet alanına göre mevzuatın gereklerini yerine getirmekle yükümlüdür ve ikincil mevzuata, Kurul kararlarına aykırılık ihtar ve idari para cezasına bağlanır (6446 m. 5/2-e, 16/1-b). |
| AYM iptal kararı; Danıştay yürütmeyi durdurma ya da iptal kararı | İzlenen kuralı etkiliyorsa Always material. Bu bir durum değişikliğidir: ilgili açıkların `status_verified` alanını yeniden değerlendir (`/regulatory-legal:gaps`). |
| Görüşe açılan düzenleme taslağı | Genelde Review-worthy; görüş son tarihini her zaman kaydet (`item_type: draft`). |
| Taslaksız istişare, tartışma metni, görüş çağrısı | Uyum için değil strateji için Review-worthy (`item_type: consultation`). |
| TBMM'ye sunulan kanun teklifi | İzleme (`item_type: bill`). ArthurLegal'da TBMM kaynağı yok; teklif metnini kullanıcı verir. |
| Bireysel Kurul kararı, idari para cezası | Sektör eşleşmesi → material; benzer uygulama → Review-worthy; ikisi de yoksa FYI ya da atla. |
| Kılavuz, rehber, ilke kararı, duyuru | Review-worthy. |
| Konuşma, sunum, basın açıklaması | Eşiğe göre FYI ya da atla. |
| Taahhüt ya da uzlaşma kararı (ör. Rekabet Kurulu) | Yeni bir yaklaşım ya da yüksek tutar → Review-worthy; rutin → atla. |
| [ŞİRKET ADI]'ın adının geçtiği her kalem | Always material. |

**Taslak ve istişare dalı.** Taslak ve istişare kalemleri hukuku henüz değiştirmez ama görüş son tarihi gerçektir ve kurumun yönünü gösterir. Bu yüzden ayrı ele alınır:
- İstişare ya da taslağı Always material yapma; uyum etkisi kural yayımlanana kadar sıfırdır.
- Konusu watchlist'in Always material kategorilerinden birine dokunuyorsa Review-worthy yap.
- `**Comment tracking:**` Enabled ise son tarihi `~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml` dosyasına yaz (şema `/regulatory-legal:comments`'te): `item_type` (`draft`, `consultation` ya da `bill`), `decision: undecided`, `owner` = `**Default comment decision owner:**`. Son tarih kurumun duyurusundan alınır; duyuruda yoksa "son tarih belirtilmemiş — kurumdan teyit et" yaz, tarih uydurma.
- Digest satırına açıkça yaz: "Kural öncesi. Görüş son tarihi [tarih]. `/regulatory-legal:policy-diff`'e yalnız ön konumlanma analizi için yönlendir (henüz uyum açığı yok)."
- Bunlar uyum açığı değildir: açık izleyiciye (gap tracker) değil görüş izleyicisine (comment tracker) gider. `gap-surfacer` bunları `comment-decision` `gap_type` ile tutar ya da hiç almaz.

### Adım 3: Zenginleştir

FYI üstündeki her kalem için:
- Tek satır: ne değişti.
- Neden önemli: "bu, [[ŞİRKET ADI]'ın yaptığı iş] hakkında".
- Bağlantı: araçtan dönen `url` / `source_url`; künye için araçtan dönen `citation` birebir.
- Yürürlük tarihi, geçiş süresi ya da görüş son tarihi. Yürürlük tarihini yürürlük maddesinden oku; "yayımı tarihinde" varsayma.

FYI kalemlerini tek tek özetleme; yalnız say.

## Çıktı

Digest varsayılan olarak sohbete yazılır. FYI üstünde en az bir kalem varsa, `**Digest output path:**` değeri "chat only" değilse **ayrıca paylaşılabilir bir dosyaya da yaz**:

1. `**Digest output path:**` bir klasörse oraya `reg-digest-YYYY-MM-DD.md`; boşsa `~/regulatory-legal-digests/reg-digest-YYYY-MM-DD.md`.
2. Üst klasör yoksa oluştur.
3. Sohbetteki içeriğin aynısını Markdown olarak yaz (üst başlık, kaynak etiketleri, doğrulama notu dâhil).
4. O gün için dosya varsa üzerine yazma; zaman damgalı yeni bir alt başlık ekle.
5. Sonra söyle: "Digest `<yol>` dosyasına yazıldı. Olduğu gibi paylaşabilir ya da Pandoc ile .docx'e çevirebilirsiniz: `pandoc <yol> -o <yol>.docx`."
6. Yazma başarısız olursa (izin, klasör, disk) yalnız sohbete yaz ve bunu söyle; dosya isteğini sessizce düşürme.
7. `**Digest channel:**` dolu ve kanal bağlıysa digest'i oraya göndermeyi öner; kişiye özel mesajlar gap-surfacer'daki gönderim başına onay kuralına tabidir.

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

## Düzenleyici Akış Kontrolü — [tarih]

**Dönem:** [son kontrol] – [şimdi]
**Taranan akışlar:** [ör. "RG fihristi (konu=enerji + query), tr_mevzuat_ara, EPDK, SPK bülteni 2026/74"]
**Konu süzgeci:** elenen [n], belirsiz [n] — kapsam garantisi değildir
**Bulunan kalem:** [N]

### Sonuç

[N kalem [tarih]e kadar işlem gerektiriyor — ilk üçü: X, Y, Z]

### 🔴 Always material (alert immediately)

**[Kurum] — [Başlık]** `[kaynak etiketi]`
[Tek satır özet]. [Neden önemli]. Yürürlük [tarih]; geçiş [varsa].
[Bağlantı]
→ Öneri: [etkilenmesi muhtemel politika] için `/regulatory-legal:policy-diff`

### 🟡 Review-worthy (weekly digest)

**[Kurum] — [Başlık]** `[kaynak etiketi]`
[Tek satır]. [Neden önemli]. [Son tarih varsa].
[Bağlantı]
[Taslak / istişare: "💬 Görüş son tarihi: [tarih] — karar bekliyor"]

### 📝 FYI (monthly roundup or not at all)

[N] kalem — [başlık + bağlantı listesi, özetsiz]

### UYARI satırları

[Veri çekilemeyen her kaynak için: UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>]

---

**Son kontrol güncellendi:** [zaman damgası]
**Görüş izleyici:** kararı bekleyen [N] taslak/istişare — `/regulatory-legal:comments`

---

**Atıfları doğrula.** Buradaki künyeler yapay zekâ desteğiyle derlendi. Bir düzenlemeye, karara ya da kılavuza dayanmadan önce Resmî Gazete, mevzuat.gov.tr ya da kurumun sitesinden doğruluğunu, yürürlük tarihini ve güncel durumunu kontrol et. Kaynak etiketleri her künyenin nereden geldiğini gösterir; `doğrula` etiketliler önce kontrol edilir.
```

## Ayar eksikse

Profilde gereken değer boşsa ya da `[PLACEHOLDER]` ise genel değil somut söyle:
- **Watchlist boş (`## Regulators we watch`):** dur. "Profilinizdeki izleme listesi boş; hangi kurumları izleyeceğimi bilmeden akış çekemem. `/regulatory-legal:cold-start-interview --redo` çalıştırın ya da `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasına en az bir kurum ekleyin."
- **Materiality threshold boş:** yukarıdaki varsayılan kademeleri kullan ve ekle: "Profilinizde özel eşik olmadığı için varsayılan kademeler kullanıldı. `/regulatory-legal:cold-start-interview --redo` ile ya da profili düzenleyerek ayarlayın."
- **Feed configuration boş:** yalnız Resmî Gazete taramasını (watchlist'teki kurum ve kanun adlarıyla `query`) çalıştır ve ekle: "Profilinizde kurum akışı ya da duyuru sayfası tanımlı olmadığı için yalnız Resmî Gazete fihristi tarandı. Kurum akışlarını `/regulatory-legal:cold-start-interview --redo` ile ekleyin."

Değerler doluysa ayardan hiç söz etme.

FYI üstünde kalem yoksa: "Sakin. [N] FYI kalem, dikkat gerektiren yok. Konu süzgeci [n] kalem eledi."

## Devir

- **policy-diff'e:** politika etkisi muhtemel her Always material kalem için karşılaştırmayı öner.
- **gap-surfacer'a:** karşılaştırma açık bulursa izlenir.
- **Görüş izleyiciye:** FYI üstündeki her taslak ve istişare, `**Comment tracking:**` Enabled ise son tarihiyle otomatik kaydedilir.
- **Uzman skill'ler:** yalnız KVKK'ya dokunan ayrıntılı açık analizi `/privacy-legal:reg-gap-analysis`; EPDK taslağına görüş metni `/administrative-legal:epdk-proaktif-gorus`.

## Kapanış

Profildeki `## Outputs` karar ağacıyla bitir. Seçenekleri bu çıktıya uyarla; beş varsayılan dal (X'i yaz, eskale et, olgu topla, izle ve bekle, başka bir şey) başlangıçtır, kalıp değildir. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Her kalemi baştan sona okumaz. Sınıflandırır ve zenginleştirir; derin okuma süzgeçten geçenler içindir.
- Önemlilik eşiğini değiştirmez. Süzgeç yanlışsa profil düzenlenir.
- Ücretli kaynak gerektirmez. ArthurLegal araçları tabandır; ek bağlayıcılar derinlik katar.
- Taslakları kendiliğinden bulmaz. Kurum duyuru sayfası profilde tanımlı değilse taslak ancak kullanıcı yapıştırınca girer.
