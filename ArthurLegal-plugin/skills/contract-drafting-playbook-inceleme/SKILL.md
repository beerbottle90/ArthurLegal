---
name: contract-drafting-playbook-inceleme
description: >
  Sözleşmeyi Türk hukuku playbook'uyla inceler: her konu için başlangıç pozisyonu, vazgeçilmez
  ve geri çekilme noktası; emredici sınırlar (TBK, İş K., TTK, KVKK) resmî metinden teyitli.
  Dört hazır playbook: işyeri/konut kirası, hizmet ve eser sözleşmesi, iş sözleşmesi, gizlilik
  sözleşmesi. Hangi tarafı temsil ettiğinizi sorar; çıktı Uygun / Pazarlık / Kırmızı tablosu ve
  önerilen metin. Claude for Word'de açık belge üzerinde de çalışır.
user-invocable: true
---

# Türk Hukuku Playbook İncelemesi

> Sözleşmeyi büronun pozisyonuna göre konu konu tarar. Her çıktı **TASLAK**: avukat okur, karşı tarafla pazarlığı avukat yürütür.
> Playbook bir başlangıç noktasıdır; büronun kendi pozisyonu `firm-profile.md` ya da kullanıcının yazdığı tercihlerle değişir.

## ADIM 0 — Girdi ve netleştirme

1. **Belge:** kullanıcı yüklesin ya da açık Word belgesi (Claude for Word). Müvekkil bilgisi içeriyorsa önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.
2. **Sözleşme türü:** işyeri/konut kirası · hizmet ve eser · iş sözleşmesi · gizlilik (NDA). Başka türse en yakın playbook'u söyleyip yalnız genel hükümleri (aşağıda "Her sözleşmede") uygulayın.
3. **Taraf:** kimi temsil ediyoruz? (kiraya veren / kiracı, hizmet alan / veren, işveren / işçi, ifşa eden / alan). Belirsizse **seçenekli sorun**; taraf belli olmadan pozisyon yazılmaz.
4. **Tacir mi?** Borçlu tacirse ceza koşulunun indirimi istenemez (aşağıda). Belirsizse sorun.

## ADIM 1 — Madde doğrulama kapısı

Aşağıdaki tablolarda geçen her madde 14.11.2026'da `tr_mevzuat_madde_getir` ile resmî metinden okundu. Çıktıya yazmadan önce
yine çekin ve `citation` alanını birebir kullanın; maddeye yüklediğiniz içerik (hakkın sahibi, şart, süre, sonuç) başlık ve metinle
örtüşmeli. Çekilemeyen maddeyi yazmayın: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 2 — Playbook'u uygula

Her konu için sözleşmede ne yazdığını bulun, playbook'la karşılaştırın, durumu işaretleyin:
**Uygun** (başlangıç pozisyonunda ya da daha iyi) · **Pazarlık** (geri çekilme aralığında) · **Kırmızı** (vazgeçilmezin altında ya da emredici hükme aykırı).

### Her sözleşmede

| Konu | Başlangıç pozisyonu | Vazgeçilmez | Geri çekilme |
|---|---|---|---|
| Sorumsuzluk kaydı | Karşı tarafın sorumluluğu sınırsız; bizimki doğrudan zararla sınırlı | Ağır kusurdan sorumsuzluk kaydı kesin hükümsüzdür (TBK m. 115/1); dayanmayın, karşı taraf yazdıysa işaretleyin | Sınırı sözleşme bedeline bağlayın; kast ve ağır kusur dışarıda kalsın |
| Ceza koşulu | Lehimize ceza; aleyhimize ceza yok | Alacaklı kural olarak ya ifayı ya cezayı ister (TBK m. 179/1); fahiş ceza hâkimce indirilir (TBK m. 182/3), ama **tacir borçlu indirim isteyemez** (TTK m. 22) | Tutarı zarara yakın tutun; ceza ve ifanın birlikte istenebileceği hâli açıkça yazın (TBK m. 179/2) |
| Standart (matbu) koşullar | Kendi metnimiz | Karşı tarafın matbu koşulları açıkça bilgi verilip kabul edilmedikçe yazılmamış sayılır (TBK m. 21); dürüstlüğe aykırı ağırlaştırıcı hüküm konamaz (TBK m. 25) | Önemli koşulları ayrıca imzalatın, kalın yazın |
| Uyarlama ve imkânsızlık | Bizim yükümüz için uyarlama hakkı açık | Öngörülemeyen olağanüstü durumda uyarlama ya da dönme/fesih hakkı (TBK m. 138); kusursuz imkânsızlıkta borç sona erer (TBK m. 136/1) | Mücbir sebep listesi ve bildirim süresi yazın |

### İşyeri ve konut kirası

| Konu | Kiraya veren lehine başlangıç | Vazgeçilmez (emredici) | Geri çekilme |
|---|---|---|---|
| Kira artışı | Her yıl endekse bağlı artış | Yenilenen dönemde artış bir önceki yılın TÜFE on iki aylık ortalama değişimini geçemez (TBK m. 344/1) | Beş yıldan sonra hâkimin belirlemesine dayanmak (TBK m. 344/3) |
| Güvence (depozito) | Üç aylık kira | Güvence üç aylık kira bedelini aşamaz; para ise vadeli hesaba yatırılır (TBK m. 342) | İki aylık güvence + banka teminat mektubu |
| Gecikme | Ceza koşulu ve muacceliyet | Kiracıya kira ve yan gider dışında ödeme yükü konamaz; gecikmede ceza koşulu ve sonraki kiraların muaccel olması geçersizdir (TBK m. 346) | Gecikme faizi; iki haklı ihtar yolu (TBK m. 352/2) |
| Süre ve fesih | Uzun süre, kiracıya erken fesihte bedel | Belirli süreli sözleşmede kiracı 15 gün önce bildirmezse sözleşme bir yıl uzar; kiraya veren süre bitimine dayanarak sona erdiremez, on yıllık uzama sonunda üç ay önceden bildirimle sona erdirebilir (TBK m. 347/1) | Erken çıkışta makul bir devir/kiracı bulma düzeni |
| Tahliye taahhüdü | Sözleşmeyle birlikte imzalatmak | Taahhüt **kiralanan teslim edildikten sonra** yazılı verilmelidir; taahhüt tarihinden başlayarak bir ay içinde icra ya da dava (TBK m. 352/1) | Teslimden sonra ayrı tarihli belge |
| Kiracı aleyhine değişiklik | — | Kira bedelinin belirlenmesi dışında kiracı aleyhine değişiklik yapılamaz (TBK m. 343) | — |
| Kapsam | — | Konut ve çatılı işyeri hükümleri, geçici kullanıma özgülenmiş taşınmazın altı ay ve daha kısa kiralanmasında uygulanmaz (TBK m. 339/1) | — |

Kiracıyı temsil ediyorsanız sütunları ters okuyun: vazgeçilmezler kiracının kalkanıdır; aykırı hükmü **Kırmızı** işaretleyip çıkarılmasını isteyin.

### Hizmet ve eser sözleşmesi

| Konu | Hizmet alan lehine başlangıç | Vazgeçilmez | Geri çekilme |
|---|---|---|---|
| Sorumluluk | Hizmet verenin sorumluluğu sınırsız | Ağır kusurdan sorumsuzluk kaydı kesin hükümsüz (TBK m. 115/1); izne bağlı uzmanlık hizmetinde hafif kusurdan sorumsuzluk da kesin hükümsüz (TBK m. 115/3) | Sözleşme bedeli kadar üst sınır, kast ve ağır kusur hariç |
| Gecikme cezası | Günlük gecikme cezası, ifa ile birlikte istenebilir | TBK m. 179/2'deki birlikte isteme hakkını açık yazın; hizmet veren tacirse fahiş ceza indirimi istenemez (TTK m. 22) | Toplam cezaya üst sınır |
| Fikrî haklar | Bütün çıktılar hizmet alana devredilir | Devir ve lisansın kapsamı (hangi haklar, süre, yer) açıkça yazılmalı | Önceden var olan araçlar için lisans |
| Kişisel veri | Hizmet veren veri işleyen, talimatla işler | Yurt dışına aktarım KVKK m. 9'daki şartlara bağlıdır (yeterlilik kararı ya da maddedeki öteki yollar) | Aktarım yoksa açıkça yazın; varsa dayanak ve alıcı listesi |
| Uyarlama | Fiyat sabit | Öngörülemeyen olağanüstü durumda borçlu hâkimden uyarlama, olmazsa dönme ya da fesih isteyebilir (TBK m. 138/1); sözleşmede formül yoksa bu yola kalınır | Endeks ya da döviz uyarlama formülü |

### İş sözleşmesi

| Konu | İşveren lehine başlangıç | Vazgeçilmez (emredici) | Geri çekilme |
|---|---|---|---|
| Deneme süresi | İki ay | En çok iki ay; yalnız toplu iş sözleşmesiyle dört aya kadar; deneme süresinde bildirimsiz ve tazminatsız fesih (İş K. m. 15) | — |
| Rekabet yasağı | İki yıl, geniş bölge ve iş türü | Yazılı olmalı; işçi müşteri çevresine ya da üretim sırlarına erişebiliyor ve kullanımı önemli zarar doğuracaksa geçerli (TBK m. 444); yer, zaman ve iş türüyle sınırlı, özel durumlar dışında iki yılı aşamaz; hâkim aşırı yasağı daraltabilir (TBK m. 445) | Bir yıl, ilgili il ve iş kolu; karşılığında ödeme |
| Ceza koşulu | Rekabet ve gizlilik ihlaline ceza | Yalnız işçi aleyhine konan ceza koşulu geçersiz (TBK m. 420/1): ceza karşılıklı olmalı | Karşılıklı, makul tutarda ceza |
| İbra | Ayrılışta genel ibraname | İbra yazılı, sözleşme bitiminden en az bir ay sonra, alacak türü ve miktarı açık, ödeme tam ve bankadan olmalı; aksi kesin hükümsüz (TBK m. 420/2) | — |
| Fazla çalışma | Ücrete dahil | Haftalık 45 saati aşan çalışma fazla çalışmadır; her saat yüzde elli zamlı ödenir (İş K. m. 41) | Yasal sınırlar içinde serbest zaman seçeneği |

İşçiyi temsil ediyorsanız: vazgeçilmezlere aykırı her hüküm **Kırmızı**; rekabet yasağında m. 444 koşullarının bulunup bulunmadığını ayrıca sorun.

### Gizlilik sözleşmesi (NDA)

| Konu | İfşa eden lehine başlangıç | Vazgeçilmez | Geri çekilme |
|---|---|---|---|
| Gizli bilgi tanımı | Geniş: sözlü ve yazılı her bilgi | Kamuya açık, önceden bilinen, bağımsız geliştirilen ve yasal zorunlulukla açıklanan bilgi istisna olmalı | Sözlü bilgi için yazılı teyit süresi |
| Süre | Belirsiz | Gizlilik yükümünün sözleşme bitiminden sonra ne kadar süreceği ve ticari sırların ayrıca korunup korunmadığı açıkça yazılmalı | Üç ila beş yıl |
| Ceza koşulu | Her ihlal için yüksek ceza | Fahiş ceza indirilir (TBK m. 182/3); alan taraf tacirse indirim istenemez (TTK m. 22) | Ceza + ispatlanan zararın fazlası |
| Kişisel veri | — | Gizli bilgi kişisel veri içeriyorsa işleme ve yurt dışı aktarım KVKK'ya tabi (m. 9) | Kişisel veri paylaşılmayacağını yazın ya da veri işleme ekini ekleyin |
| İade ve imha | Talep hâlinde iade ve imha, yazılı teyit | — | Yasal saklama zorunluluğu istisnası |

## ADIM 3 — Çıktı

```markdown
TASLAK – AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Playbook İncelemesi — [sözleşme türü] — [temsil edilen taraf]

## Özet
- Uygun: N · Pazarlık: N · Kırmızı: N
- En önemli üç konu: …

## Konu konu
| # | Konu | Sözleşmede | Playbook | Durum | Önerilen metin |
|---|---|---|---|---|---|

## Madde kontrolü
[her atıf → resmî metinden okundu ve içerikle eşleşti / çekilemedi, UYARI satırı]

## Sonraki adımlar
- Redline için: `/arthurlegal:contract-drafting-redline-contract` ya da ArthurMask'in revize aracı (izli değişiklik).
- Karşı tarafa özet için: `/arthurlegal:commercial-legal-stakeholder-summary`.
```

## Not
- Claude for Word'de çalışırken önerileri belgeye **izli değişiklik** olarak işleyin; her değişikliğe tek cümlelik gerekçe yazın.
- Playbook'taki pozisyonlar varsayılandır; büro profili ya da kullanıcı tercihi farklıysa onu uygulayın ve farkı özette söyleyin.

---

## Kaynak katmanı — /legal-research

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
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | `/arthurlegal:legal-research-sozlesme-emsali` |
| AZ hukuku secilmisse emredici hukum kontrolu — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil) — okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `${CLAUDE_PLUGIN_ROOT}/references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
