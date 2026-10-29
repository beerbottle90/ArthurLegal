---
name: employment-legal-internal-investigation
description: >
  Referans: iç soruşturmanın açılıştan nihai nota kadar yönetimi — soruşturma kaydı,
  belge taraması ("iğne bulma"), kaynak kapsama takibi, kayda karşı soru-cevap,
  soruşturma notu ve hedef kitle özetleri. Türk hukuku kontrol noktaları: savunma
  (İş K. m. 19), altı iş günlük hak düşürücü süre (m. 26), KVKK ölçülülüğü, avukatın
  sır saklama yükümlülüğü (Av. K. m. 36). /investigation-open, -add, -query, -memo ve
  -summary tarafından yüklenir; doğrudan çağrılmaz.
user-invocable: false
---

# İç Soruşturma — Ortak Çerçeve

## Matter bağlamı

Uygulama CLAUDE.md'sinde `## Matter workspaces` bölümüne bak. `Enabled` `✗` ise (kurum içi kullanımda varsayılan) bu paragrafın gerisini atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:employment-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

**Soruşturma klasörü (`<SORUŞTURMA>`):** matter workspace kapalıysa `~/.claude/plugins/config/claude-for-legal/employment-legal/investigation-<slug>/`; açıksa `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/investigation-<slug>/`.

## Bağlam ve üst başlık

- `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → eskalasyon tablosu, soruşturma protokolü, taraf rolü ([Müvekkil] işveren mi), `## Who's using this`, `## Outputs`.
- `~/.claude/plugins/config/claude-for-legal/firm-profile.md` → büro/şirket bilgisi.
- Her dosya (kayıt, not, özet) `## Outputs` bölümündeki üst başlıkla açılır; başlık kullanıcı rolüne göre değişir.

## ⚠️ Gizlilik — Türk hukukunda "privileged investigation" yok

ABD'deki attorney-client privilege ve work product doktrininin Türk hukukunda birebir karşılığı yoktur. Koruma üç ayrı ve sınırlı dayanaktan gelir:

| Dayanak | Ne korur | Ne korumaz |
|---|---|---|
| Av. K. m. 36 — avukat görevi dolayısıyla öğrendiklerini açığa vuramaz; tanıklığı iş sahibinin muvafakatine bağlıdır, muvafakat olsa da çekinebilir | Avukatın notları, değerlendirmesi, müvekkilden öğrendikleri | Avukat olmayan İK/yöneticinin tuttuğu notlar; sonradan avukata gönderilmesi onları korumaz |
| İş K. m. 75/2 — işveren işçi hakkında edindiği bilgiyi dürüstlük kuralına ve hukuka uygun kullanır, gizli kalmasında işçinin haklı çıkarı olanı açıklamaz | Özlük ve soruşturma bilgisinin gereksiz paylaşımı | İşverenin bu bilgiyi kendi davasında delil olarak sunması |
| KVKK m. 12 — veri güvenliği; öğrenilen veriyi açıklamama, amaç dışı kullanmama | Erişim, saklama, sızıntıya karşı önlem | — |

**Sonuç — dosyayı ikiye ayır** (her girdide `dosya_sinifi` alanı):
- **A — avukat çalışma ürünü** (`avukat-calisma-urunu`): avukat notları, güvenilirlik değerlendirmesi, hukuki risk analizi, soruşturma notu. Yalnız avukat ve soruşturma ekibi görür.
- **B — işveren delil dosyası** (`isveren-delil`): savunma istem yazısı, savunma tutanağı, tanık tutanakları, olay tutanağı, fesih bildirimi taslağı. **İşe iade ya da alacak davasında mahkemeye sunulacağı varsayımıyla** tarafsız ve olgusal dil; avukat görüşü ve risk yorumu bu belgelere girmez.

Başlık koymak koruma yaratmaz. Soruşturmayı İK yürütüyor, avukat yalnız danışmansa A sınıfı daralır — dosya açılmadan avukata sor; emin değilsen "tartışmalı — avukat karar versin" diye işaretle.

**Dağıtım disiplini:** Dosyaları soruşturma ekibi dışına (İK geneli, iş birimi, CC zincirleri) gönderme; her dağıtımı bilinçli karar olarak kayda geçir. Kişisel veriyi amaçla bağlantılı, sınırlı ve ölçülü işle, gerekli süre kadar tut (KVKK m. 4/2).

## Amaç

İç soruşturma iki yerden çöker: **kapsama boşluğu** (hiç toplanmamış kaynak) ve **sentez boşluğu** (toplanmış ama bağlanmamış delil). Türk hukukunda üçüncüsü **süre ve usuldür**: savunma alınmadan ya da hak düşürücü süre geçtikten sonra yapılan fesih, sağlam bulguyu boşa çıkarır. Bu skill kaynakları izler, belge yığınını avukatı boğmadan tarar ve her an nota dönüştürülebilecek bir kayıt tutar.

## ⏰ ÖN-KONTROL — Süre ve usul (her modda ilk iş)

1. **Hak düşürücü süre — İş K. m. 26:** Ahlak ve iyi niyet kurallarına aykırılığa (m. 24/II, m. 25/II) dayalı derhal fesih yetkisi, karşı tarafın öğrendiği günden itibaren **altı iş günü** ve her hâlde fiilden itibaren **bir yıl** geçtikten sonra kullanılamaz; işçi olayda maddi çıkar sağladıysa bir yıllık süre uygulanmaz.
   - Kayda öğrenme tarihini ve **kimin** öğrendiğini yaz. Tüzel kişi işverende sürenin fesih yetkisi olan kişi ya da organın öğrenmesiyle, soruşturma gerekiyorsa sonucun ona sunulmasıyla başladığı **yerleşik uygulamadır — tartışmalı, içtihadı kontrol et**:
     `tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="altı iş günlük hak düşürücü süre soruşturma öğrenme", date_from="2020-01-01")`
   - Kalan ≤ 2 iş günü → 🔴 ACİL; avukata hemen bildir.
2. **Savunma — İş K. m. 19:** Fesih bildirimi yazılı yapılır, sebep açık ve kesin belirtilir. Belirsiz süreli sözleşme, işçinin davranışı veya verimiyle ilgili nedenle, iddialara karşı savunması alınmadan feshedilemez; m. 25/II'ye uygun fesih hakkı saklıdır. m. 25/II'ye dayanılacak olsa da savunma almak ispat bakımından güvenlidir (yerleşik uygulama). Savunma istem yazısı somut iddia, tarih ve süre içerir; kanunda süre yoktur, TİS/yönetmelik süresine uy — **tartışmalı, içtihadı kontrol et**.
3. **TİS / disiplin yönetmeliği:** Disiplin kurulu veya özel usul varsa ona uy. İşyeri sendika temsilcisinin sözleşmesi haklı neden olmadıkça ve nedeni yazılı, açık ve kesin belirtilmedikçe feshedilemez; temsilci ya da sendikası bir ay içinde dava açabilir (6356 s. Kanun m. 24).
4. **İspat yükü:** İşe iade davasında feshin geçerli sebebe dayandığını işveren ispatlar (İş K. m. 20/2). Ayrımcılık iddiasında işçi ihlal ihtimalini güçlü biçimde gösterirse yük işverene geçer (m. 5 son fıkra). Kaydı bu yükü taşıyacak biçimde tut.

## KVKK ve delil kontrolü — e-posta, cihaz, kamera, log

Çalışanın e-postası, mesajları, cihazı, kamera kaydı veya sistem logu incelenmeden önce sırayla sor; cevabı kayda `kvkk_kontrol` olarak yaz:

1. **Önceden aydınlatma:** Kurumsal hesap/cihazların denetlenebileceği çalışana önceden bildirildi mi (KVKK m. 10 — amaç, aktarım, yöntem, hukuki sebep, haklar)? Politika metnini iste.
2. **Hukuki sebep — KVKK m. 5/2:** özellikle (ç) hukuki yükümlülük, (e) bir hakkın tesisi, kullanılması veya korunması, (f) ilgili kişinin temel hak ve özgürlüklerine zarar vermemek kaydıyla meşru menfaat. Sağlık, cinsel hayat, sendika üyeliği gibi özel nitelikli veri (m. 6/1) çıkarsa m. 6/3'teki dar şartlar ve Kurulun belirlediği yeterli önlemler (m. 6/4) gerekir.
3. **Ölçülülük — m. 4/2-ç:** yalnız kurumsal hesap/cihaz, iddia dönemiyle sınırlı tarih aralığı, iddiaya bağlı anahtar kelimeler; özel yazışma içeriğine girme. İşveren işçi verisini yalnız işe yatkınlık veya sözleşmenin ifası için zorunlu olduğu ölçüde kullanabilir (TBK m. 419).
4. **Anayasal sınır:** özel hayatın gizliliği ve kişisel verilerin korunması (Anayasa m. 20), haberleşmenin gizliliği (m. 22).
5. **Delil sonucu:** Hukuka aykırı elde edilen delil mahkemece bir vakıanın ispatında dikkate alınamaz (HMK m. 189/2). Hukuka aykırı kayıt ve ele geçirme ayrıca suç oluşturabilir (TCK m. 135, m. 136).
6. **Güvenlik — KVKK m. 12:** inceleme kopyası sınırlı ekipte, erişim kayıtlı, saklama süresi belli.

Orantılılık çizgisini ezberden çizme; her dosyada ara ve dönen kararın künyesini birebir kullan:
```
tr_aym_ara(kind="bireysel", query="işveren kurumsal e-posta yazışmaları incelenmesi özel hayat")
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="kurumsal e-posta delil feshin geçerliliği")
tr_kurum_karari_ara(kurum="kvkk", query="çalışan e-posta kamera")
```

---

## Mod 1 — Soruşturma aç

`/arthurlegal:employment-legal-investigation-open` ya da "soruşturma aç", "şu iddiayı soruştur" ile tetiklenir.

### Adım 1 — Ön görüşme (tek blokta sor)

> Soruşturma kaydını açmak için birkaç bilgi gerekiyor:
>
> **Olay**
> - İddia ya da endişe nedir (sade dille)?
> - Kim bildirdi / ne tetikledi (şikâyet, ihbar hattı, denetim, yönetici gözlemi)? **Hangi tarihte, kime ulaştı?** (m. 26 sayacı)
> - Hakkında iddia bulunan kişi kim (rol, kıdem, sözleşme türü)?
> - İddia edilen fiillerin yaklaşık dönemi?
> - Soruşturmayı kim yönetiyor: avukat mı (büro / şirket avukatı), İK mı (avukat danışman)?
>
> **Tür** (kaynak listesini buna göre öneririm)
> - İK: cinsel taciz / psikolojik taciz (mobbing) / ayrımcılık / misilleme
> - Mali: masraf, satın alma, zimmet, güveni kötüye kullanma
> - Üst yönetici: çıkar çatışması, rekabet, yönetim zafiyeti
> - İhbar/bildirim sonrası aleyhe işlem
> - Diğer
>
> **Paralel çerçeveler** (görüşme usulünü değiştirir)
> - Taraflardan biri sendika üyesi ya da işyeri sendika temsilcisi mi; TİS veya disiplin yönetmeliğinde özel usul var mı?
> - İşveren kamu kurumu mu? Hakkında iddia olan memursa 657 sayılı Devlet Memurları Kanunu disiplin rejimi uygulanır — bu skill kapsamı dışı; idari hukuk ekibine yönlendir.
> - Olay suç olabilir mi (ör. cinsel taciz — TCK m. 105, şikâyete bağlı; hırsızlık, zimmet)? Savcılık süreci başladı mı?
> - Yurt dışındaki ana şirkete veri gidecek mi (KVKK m. 9 — yurt dışına aktarım şartları)?

Paralel ceza süreci varsa: ceza soruşturmasının sonucunu beklemenin m. 26 süresine etkisi **tartışmalı — içtihadı kontrol et**; beklemeden önce avukata sor.

### Adım 2 — Klasör ve dosyalar

Aynı slug varsa üzerine yazmadan önce uyar. `<SORUŞTURMA>/` altında oluştur:

`kayit.yaml`
```yaml
# [ÜST BAŞLIK — CLAUDE.md ## Outputs; role göre değişir]
matter: "[ad]"
slug: "[slug]"
acilis: "[ISO tarih]"
yoneten: "[avukat | İK + avukat danışman]"
iddia: "[sade özet]"
sikayetci: "[ad/rol ya da anonim]"
hakkinda_iddia_olan: "[ad/rol]"
fiil_donemi: "[yaklaşık tarihler]"
ogrenme: {tarih: "[ISO]", kim: "[kişi/organ]", m26_son_gun: "[ISO — 'tartışmalı' notuyla]"}
savunma: {istem_tarihi: null, alinma_tarihi: null, tutanak: null}
kvkk_kontrol: {aydinlatma: null, hukuki_sebep: null, kapsam: null}
tur: "[ik | mali | yonetici | ihbar | diger]"
durum: acik
son_guncelleme: "[ISO]"
konular:
  - "[Konu 1 — ör. 'iş arkadaşına cinsel taciz iddiası']"
kayitlar: []
delil_bosluklari: []
```

`incelenen-belgeler.yaml`
```yaml
# [ÜST BAŞLIK]
matter: "[ad]"
toplam_incelenen: 0
toplam_one_cikan: 0
son_guncelleme: "[ISO]"
belgeler: []
```

`kaynak-listesi.yaml` — Adım 3'teki türe uygun liste. Her satır: `{id, kaynak, durum: acik|devam|tamam|uygulanmaz, not}`.

### Adım 3 — Kaynak listesi

Türe uygun listeyi göster ve sor: "Dosyanıza uyuyor mu? Uygulanmayanları 'uygulanmaz' işaretlerim; eklemek istediğiniz kaynak var mı?" Sonra `kaynak-listesi.yaml`'a yaz.

**İK (taciz / mobbing / ayrımcılık / misilleme):**
1. Şikâyetçi görüşmesi
2. Hakkında iddia olanın savunması — yazılı istem + tutanak (İş K. m. 19)
3. Tanık görüşmeleri — tarafların anlatımlarından belirle
4. Kurumsal e-posta/mesaj incelemesi — **KVKK kontrolü tamamlandıktan sonra**
5. Özlük dosyası — önceki ihtar, disiplin, performans (İş K. m. 75)
6. Önceki şikâyetler ve ihbar hattı kayıtları
7. Emsal uygulama — benzer olaylarda verilen kararlar (eşit davranma, m. 5)
8. Politikalar — taciz/mobbing politikası, disiplin yönetmeliği, TİS (**olay tarihindeki sürüm**)
9. Organizasyon şeması ve raporlama ilişkileri (olay tarihinde)
10. Takvim kayıtları — anlatımlarda geçen toplantı/etkinlikler
11. Şikâyetçiyi koruma tedbirleri — ne zaman, hangi önlem (TBK m. 417: işveren işçilerin psikolojik ve cinsel tacize uğramaması ve uğrayanların daha fazla zarar görmemesi için önlem almakla yükümlü)
12. Görüşme açılış bildirimleri — her görüşmede verildi ve imzalandı mı

**Mali usulsüzlük:** masraf raporları (ilgili dönem); onay kayıtları; tedarikçi sözleşme/fatura/ödeme kayıtları; muhasebe kayıtları; e-posta (KVKK kontrolü sonrası); hakkında iddia olanın savunması; onaylayan görüşmeleri; tedarikçi görüşmeleri (erişilebilirse); sistem erişim logları; önceki denetimler; maddi çıkar tespiti (varsa m. 26'daki bir yıllık süre uygulanmaz); görüşme açılış bildirimleri.

**Üst yönetici:** savunma/görüşme; YK ve komite kararları; iş sözleşmesi ve ekleri; prim ve pay planı kayıtları; masraf ve onaylar; e-posta (KVKK kontrolü sonrası); çıkar çatışması beyanları (ya da yokluğu); dış faaliyet ve rakiple ilişki kayıtları (TBK m. 396 — sadakat ve rekabet etmeme); tanıklar (astlar, eş düzey, YK üyeleri); önceki şikâyetler; **statü notu** — işletmenin bütününü sevk ve idare eden işveren vekili mi (İş K. m. 18 son fıkra: m. 18, 19 ve 21 uygulanmaz); görüşme açılış bildirimleri.

**İhbar/bildirim sonrası aleyhe işlem:** bildiren görüşmesi; ilk bildirimin yazılı hâli; bildirilen konuya ait kayıtlar; bildirenin aleyhine sonradan yapılan işlemler; bu işlemlerin karar vericileriyle görüşme; emsal — bildirimde bulunmayan benzer çalışanlara muamele; karar vericilerin yazışmaları (KVKK kontrolü sonrası); zaman analizi — bildirim ile işlem arasındaki yakınlık (işveren aleyhine idari veya adli makamlara başvurmak fesih için geçerli sebep değildir, İş K. m. 18/3-c); görüşme açılış bildirimleri. Genel bir ihbarcı koruma düzenlemesi olup olmadığını ezberden söyleme: `tr_mevzuat_ara(query="ihbarcı", search_in="fulltext")` ile güncel durumu kontrol et.

### Adım 4 — Görüşme açılış bildirimi (ABD'deki "Upjohn uyarısı" yerine)

Her görüşmenin başında söylenir, tutanağa yazılır ve imzalatılır:
- Görüşmeyi yapan kişi işverenin/şirketin avukatı (ya da İK) — çalışanın avukatı değildir.
- Görüşmenin amacı; içerik gizli tutulmaya çalışılır ama işveren kararlarında kullanılabilir ve yargılamada delil olarak sunulabilir; bu kararı işveren verir.
- Kişisel verilerin hangi amaçla işleneceği, kime aktarılabileceği, hukuki sebebi ve ilgili kişinin hakları (KVKK m. 10, m. 11).
- Misilleme yasağı; görüşmenin gizli tutulması ricası.
- Hakkında iddia olan kişiyle görüşmede: bu görüşme **m. 19 savunması mı, ön bilgi görüşmesi mi** — açıkça ayır. Savunmaysa yazılı istem ve süre verilir.

---

## Mod 2 — Veri ekle

`/arthurlegal:employment-legal-investigation-add`, "şu soruşturmaya ekle" ya da avukat görüşme notu/belge yapıştırdığında tetiklenir.

1. **Matter:** Birden fazla `investigation-*` klasörü varsa hangisi olduğunu sor; tek klasör varsa devam et.
2. **Veri türü** (açık değilse sor): görüşme notu (kimin?), belge partisi, avukat notu/gözlemi, savunma istemi/tutanağı, açılış bildirimi teyidi. E-posta/cihaz/kamera partisi geldiyse ve `kvkk_kontrol` boşsa **önce KVKK kontrolünü tamamla**; tamamlanmadan işleme alma.
3. **Çekme ölçütleri.** Belge aşağıdakilerden **herhangi birini** karşılıyorsa öne çıkarılır (bilerek biraz agresif — kaçırmaktansa yanlış pozitif):
   1. Soruşturmanın taraflarından birinin (şikâyetçi, hakkında iddia olan, kayıtta geçen tanıklar) adını içeriyor.
   2. Kilit fiil döneminde bir tarafça yazılmış ya da alınmış.
   3. İddia türüne ilişkin anahtar kelime içeriyor (kelime listesi açılışta ve yeni anlatımlarla güncellenir).
   4. Açık ya da örtülü ikrar içeriyor ("yapmamalıydım", "yazıya dökme", "bunu sil").
   5. Kayıttaki bir anlatımla çelişiyor — çelişkiyi ve ilgili `kayit_id`'yi belirt.
   6. Yargılamada hassas olacak dil içeriyor: ayrımcı ifade, tehdit, korunan özellik veya sendikal faaliyet tartışması, iddia kalıbına uyan mali usulsüzlük.
   7. Anlatımlarda geçen ama belge setinde henüz görünmeyen bir belge türü (ör. görüşmede anılan toplantının davet kaydı yok) → öne çıkan belge değil, **delil boşluğu** olarak kaydet.

   Her belgenin sonucu: `one_cikti` (kayda girdi olarak eklenir) ya da `incelendi-onemsiz` (`incelenen-belgeler.yaml`'a tek satır açıklamayla).

   Parti sonrası rapor:
   ```
   Belge incelemesi tamamlandı.
   İncelenen: [N] | Öne çıkan: [N] | Önemsiz olarak kaydedilen: [N]
   Yeni delil boşluğu: [N]
   Öne çıkanlar: [tek satır açıklama — tetikleyen ölçüt no]
   ```
   Bu rapor "kaçan iğne" sorusunun cevabıdır: ölçütler yazılı, oran görünür. Sorgu modunda "[N] belgede [konu] hakkında belge görmedim" cümlesi ancak her incelenen belge kaydedildiği için anlamlıdır.
4. **Kayıt girdisi** — öne çıkan her öğe için `kayit.yaml`'a ekle:
   ```yaml
   - kayit_id: [otomatik artan]
     kayit_turu: [gorusme | belge | avukat-notu | savunma | bosluk]
     olay_tarihi: "[olayın tarihi — kayıt tarihi değil]"
     kayit_tarihi: "[ISO tarih-saat]"
     kaynak: "[kişi/rol ya da belge adı]"
     kaynak_turu: [sikayetci | hakkinda-iddia-olan | tanik | belge | avukat-notu]
     konular: ["[ilgili konu]"]
     onem: [yuksek | orta | arka-plan]
     ozet: "[kayda kattığı şey — 2-5 cümle]"
     alinti: "[önemliyse birebir alıntı]"
     celistigi_kayit: [kayit_id | null]
     destekledigi_kayit: [kayit_id | null]
     guvenilirlik_notu: ""
     tetikleyen_olcut: "[belgeler için ölçüt no]"
     dosya_sinifi: [avukat-calisma-urunu | isveren-delil]
   ```
   Delil boşluğu:
   ```yaml
   - bosluk_id: [otomatik artan]
     aciklama: "[var olması gereken ama bulunamayan belge/kaynak]"
     kaynagi: "[hangi kayıt ya da anlatım ortaya çıkardı]"
     nereden_alinir: "[kaynak]"
     oncelik: [yuksek | orta | dusuk]
     durum: acik
   ```
5. **Kaynak listesi:** Eklenen veri bir liste kalemine karşılık geliyorsa "tamam mı, devam mı?" diye sor. Kendiliğinden `tamam` işaretlemesi **yapma** — yeterliliğe avukat karar verir.

---

## Mod 3 — Kayda soru sor

`/arthurlegal:employment-legal-investigation-query` ya da soruşturmaya yöneltilen her soru ("X ne dedi", "neler destekliyor", "neyi eksik", "her konuda en güçlü delil") ile tetiklenir. Cevaplamadan önce kaydın tamamını oku; her cevapta `kayit_id` göster.

- **Olgu sorusu:** İlgili girdilerden cevapla. Kayıtta yoksa: "Bu soruşturma kaydında ([N] girdi) [konu] hakkında bilgi görmedim; boşluk olarak işaretleyebilirim."
- **Çelişki sorusu:** Tüm `celistigi_kayit` bağlarını çıkar; her biri için çelişkinin ne olduğu, hangi girdiler, varsa hangi belgenin çelişkiye ışık tuttuğu.
- **Kapsama sorusu:** `kaynak-listesi.yaml`'daki açık kalemler, `delil_bosluklari`, anlatımlarda geçip toplanmamış kaynaklar.
- **Güç sorusu:** Konu konu: en yüksek önemdeki girdiler, belgesel destek, çözülmemiş çelişkiler.
- **Usul sorusu:** Savunma istendi/alındı mı (tarihleriyle), m. 26 son günü ve kalan iş günü, açılış bildirimleri tamam mı, KVKK kontrolü yapıldı mı. Eksik varsa işaretle.

---

## Mod 4 — Soruşturma notu (taslak / güncelleme)

`/arthurlegal:employment-legal-investigation-memo`, "notu yaz" ya da "notu güncelle" ile tetiklenir.

**İlk taslak — ön şartlar** (eksikse uyar, avukat isterse yine yaz): her açık konu için en az bir girdi; şikâyetçi ve hakkında iddia olan girdileri; savunma durumu belli; yüksek öncelikli açık kaynaklar işaretli.

`<SORUŞTURMA>/not.md` dosyasına şu yapıyla yaz (A sınıfı):

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs]

**İÇ SORUŞTURMA NOTU**
Kime: [avukat doldurur] | Kimden: [avukat doldurur] | Tarih: [tarih]
Konu: İç soruşturma — [matter] | Durum: ÖN TASLAK

## Yönetici özeti
[2-3 paragraf: iddia, kapsam ve yöntem, konu bazında bulgular (Sabit / Sabit değil / Belirsiz), önerilen işlem. En son yazılır, en başta durur.]

## Arka plan ve kapsam
Tetikleyen olay · İncelenen iddialar (numaralı) · Kapsam dışı olanlar ve nedeni · Fiil dönemi · Soruşturma dönemi · Öğrenme tarihi, öğrenen kişi/organ ve m. 26 son günü

## Yöntem
| Kişi | Rol | Tarih | Açılış bildirimi | Savunma mı? |
|---|---|---|---|---|
İncelenen belgeler (tür, adet, tarih aralığı; tam liste ayrı) · KVKK kontrolü özeti (aydınlatma, hukuki sebep, kapsam) · Sınırlamalar (istenip alınamayanlar)

## Bulgular — konu bazında
### Konu 1: [iddia]
[Delilin gösterdiği; kayıt ID'leri köşeli parantezde. Çelişkiyi düzleştirme, açıkça yaz.]

## Güvenilirlik değerlendirmesi
[Yalnız bulgunun hangi anlatıma itibar edildiğine bağlı olduğu kişiler]
İç tutarlılık · Belgesel destek / çürütme · Saik · Gözlem (yüz yüzeyse) · Değerlendirme (itibar / itibar yok / kısmen — gerekçesiyle)

## İlgili politikalar
[Olay tarihinde yürürlükteki sürüm; sonradan kabul edileni anma]

## Hukuki çerçeve (avukat teyit eder)
- Olgunun eşleştiği dayanak: m. 25/II bendi (haklı fesih) / m. 18 geçerli sebep / disiplin cezası
- Usul: savunma (m. 19); yazılı ve gerekçeli fesih bildirimi taslağı
- Süre: m. 26 — öğrenme tarihi, son gün, risk
- İşverenin koruma yükümlülüğü (TBK m. 417) ve alınan önlemler; cinsel taciz bildirimine rağmen gerekli önlem alınmazsa şikâyetçi işçinin derhal fesih hakkı (İş K. m. 24/II-d)
- İspat: m. 20/2, m. 5 son fıkra; hukuka aykırı delil (HMK m. 189/2)
- Her madde atfı `tr_mevzuat_madde_getir` ile teyit edildi mi: [evet / hayır — hangileri]

## Sonuçlar
| Konu | Bulgu | Dayanak (tek cümle) |
|---|---|---|
*Kanunda iç soruşturma için ispat ölçütü yok; bulgular eldeki delilin ağırlığına göre verildi. Mahkemedeki ispat yükü ve ölçüsü ayrıdır — tartışmalı, içtihadı kontrol et.*

## Öneriler
Disiplin işlemi (sonuç değil dayanak) · Şikâyetçiyi koruma tedbirleri · Politika/süreç · Eğitim · Ek soruşturma · İzleme

## Ek A — Kronoloji (olay_tarihi sırasıyla: Tarih | Özet | Kaynak [ID])
## Ek B — İncelenen belgeler (incelenen-belgeler.yaml özeti)
```

**Güncelleme:** Notu ve kaydı oku; notun son güncellemesinden sonra eklenen girdileri bul ve raporla:
```
Son taslaktan ([tarih]) bu yana: [N] yeni girdi | Yeni konu: [..] | Yeni çelişki: [..] | Kapanan boşluk: [..]
Güncellenecek bölümler: Bulgular [konular] · Güvenilirlik [..] · Sonuçlar [..] · Ek A: [N] yeni kronoloji girdisi
```
Sor: "Tüm notu mu, yalnız etkilenen bölümleri mi güncelleyeyim?" Önceki metni koru; değişen bölümleri avukat inceleyene kadar `[GÜNCELLENDİ: tarih]` ile işaretle.

---

## Mod 5 — Hedef kitle özeti

`/arthurlegal:employment-legal-investigation-summary` ya da "[kitle] için özet" ile tetiklenir. Sor: kitle kim, bu özet hangi kararı destekleyecek? Not yoksa önce not yazmayı öner.

- **İK özeti** (disiplin kararı için): olgusal özet (hukuki analiz yok), her iddia için bulgu, önerilen işlem. **Girmez:** güvenilirlik yöntemi, hukuki risk, avukat izlenimleri, kayıt ID'leri ve belge atıfları. Başlık: "GİZLİDİR — YALNIZ İK KULLANIMI — DAĞITILMAZ". İK özeti davada sunulabilir; B sınıfı dikkatle, olgusal yaz.
- **Yönetim / YK özeti:** tek paragrafta iddia ve kapsam, ana bulgular, iş etkisi (genel düzeyde, hukuki analiz yok), alınan önlemler. Başlık: `## Outputs`.
- **Dış avukat brifingi:** tam bağlam ve hukuki risk, açık iplikler, tartışmalı güvenilirlik, davada en önemli olacak belgeler, süreler (m. 26 son günü; fesih olursa işçinin fesih bildiriminin tebliğinden itibaren bir ay içinde arabulucuya başvurma hakkı — İş K. m. 20/1). Başlık: `## Outputs`.
- **Şikâyetçiye / ilgiliye sonuç bildirimi** (istenirse): sonuç ve alınan önlemler düzeyinde; başkalarının kişisel verisini ve tanık beyanlarını açma (KVKK m. 4/2-ç, İş K. m. 75/2).

## Sonuçlu işlem kapısı — dış merciye yanıt

Arabuluculuk için yazılı pozisyon, karşı taraf avukatının ihtarnamesine cevap, iş müfettişi incelemesi, KVKK ilgili kişi başvurusu (m. 11) veya Kurul şikâyeti, savcılık ifadesi gibi **dış yanıt** hazırlanmadan önce `## Who's using this` bölümünü oku. Rol **avukat değilse**:

> Bir iddiaya, başvuruya ya da ihtara verilen cevabın hukuki sonucu vardır: burada alınan pozisyon sonraki yargılamada aleyhinize kullanılabilir, savunma imkânı farkında olmadan kaybedilebilir. Bu cevabı bir avukatla gözden geçirdiniz mi? Evetse devam ediyorum. Hayırsa avukata götürmeniz için kısa bir brif hazırlarım: iddia, merci ve süre; soruşturmanın bulguları (iddia bazında, incelenen belgeler, görüşülen kişiler, açılış bildirimleri); çözülmemiş çelişkiler; önerilen cevabın neyi örtülü kabul ettiği; açık sorular; ne ters gidebilir (gizliliğin kaybı, çelişkili olgu beyanı, kaçırılan süre); avukata sorulacaklar.
>
> Avukat bulmak için bağlı olduğunuz ilin barosuna başvurabilirsiniz.

Açık "evet" olmadan dış yanıt taslağı üretme. Kurum içi not, İK özeti ve yönetim brifingi bu kapıya takılmaz (gizlilik uyarısı yine geçerlidir).

## Bu skill ne yapmaz

- Disiplin kararı vermez — avukatın bulgularını destekler.
- Gizlilik garantisi vermez — koruma soruşturmanın nasıl kurulduğuna bağlıdır, başlığa değil.
- Okuyamadığı formatı işlemez — elle inceleme için işaretler.
- Görüşme yapmaz, savunma almaz — tutanakları kaydeder; açılış bildiriminin ve savunmanın yapılıp yapılmadığını izler.

## Sonraki adımlar

CLAUDE.md `## Outputs`'taki sonraki adım ağacıyla bitir; seçenekleri üretilen işe göre uyarla (ör. savunma istem yazısı taslağı, fesih değerlendirmesi için `/arthurlegal:employment-legal-termination-review`, avukata eskalasyon, ek delil, bekle-izle, başka bir şey). Seçimi avukat yapar.

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
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
