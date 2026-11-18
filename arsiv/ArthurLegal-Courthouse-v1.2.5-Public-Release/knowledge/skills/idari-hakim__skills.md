# idari-hakim — Skill Referans Kitapçığı

> Dal: İdari yargı (idare mahkemesi) · Rol: **Hâkim** · Usul: İYUK 2577
> Toplam skill: 5
> Kullanım: `/idari-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Re'sen araştırma ilkesi (İYUK m. 20) geçerlidir. Çıktılar değerlendirme iskeletidir; **takdir hâkim/heyettedir**. Her çıktı **TASLAK**.

## İçindekiler

- /idari-hakim:idari-karar — iptal / tam yargı davası karar iskeleti (İYUK)
- /idari-hakim:yurutmenin-durdurulmasi — İYUK m. 27 iki şart değerlendirmesi
- /idari-hakim:ehliyet-husumet — İYUK m. 14-15 ilk inceleme (ehliyet, husumet, süre)
- /idari-hakim:ivedi-yargilama — İYUK m. 20/A ivedi + m. 20/B merkezî sınav özel rejimleri
- /idari-hakim:ara-karar-bilgi-belge — İYUK m. 20 re'sen araştırma; bilgi ve belge ara kararı, uymamanın etkisi, devlet sırrı istisnası

---

## /idari-hakim:idari-karar

---
name: idari-karar
description: >
  İptal (İYUK m. 2/1-a) veya tam yargı (m. 2/1-b) davasında karar iskeleti üretir:
  idari işlemin beş unsuru üzerinden hukuka uygunluk denetimi, re'sen araştırma,
  iptal/ret veya tazminat değerlendirmesi. Sonucu DAYATMAZ.
user-invocable: true
---

# İdari Karar — İptal / Tam Yargı İskeleti

## Konum hatırlatması

İdari yargı **hukuka uygunluk** denetimi yapar; yerindelik denetimi yapamaz (İYUK m. 2/2). Re'sen araştırma ilkesi geçerli (m. 20). Sonuç hâkim/heyet takdiridir.

## Çıktı yapısı

1. **Dava konusu işlem** — hangi idari işlem/eylem, hangi makam.
2. **İlk inceleme sonucu** — (aşağıdaki `ehliyet-husumet` skill'i) süre/ehliyet/husumet temiz mi.
3. **İşlemin beş unsuru üzerinden denetim:**
   - **Yetki** — makam yetkili mi
   - **Şekil** — usul/şekil kuralları (gerekçe, savunma alma)
   - **Sebep** — maddi/hukuki sebep var ve doğru mu
   - **Konu** — işlemin sonucu hukuka uygun mu
   - **Maksat** — kamu yararı / yetki saptırması var mı
4. **Re'sen araştırma (m. 20):** eksik bilgi/belge ara kararla istenir.
5. **Tam yargıda** ayrıca: idarenin hizmet kusuru/kusursuz sorumluluğu + illiyet + zarar + tazminat hesabı (ölçütlü, miktar dayatılmadan).
6. **Hüküm (iskelet):** iptal / ret / kısmen iptal / tazminat — **seçenekli**, sonuç boş.

## Adımlar

1. İlgili mevzuatı (ilgili kanun + yönetmelik) MCP'den çek, atıf et.
2. Danıştay emsali varsa ArthurLegal MCP (`tr_`)'den çek (`[ArthurLegal TR — Danıştay — Esas/Karar — GG.AA.YYYY]`).
3. Beş unsuru tek tek denetle; iptal ve ret gerekçesini **ayrı** kur.

## İnceleyen notu

- Kullanılan mevzuat + Danıştay emsali (atıflı)
- Re'sen araştırılması gereken eksikler
- ⚠️ "Sonuç ve takdir hâkime/heyete aittir; yerindelik denetimi yapılmaz."

---

## /idari-hakim:yurutmenin-durdurulmasi

---
name: yurutmenin-durdurulmasi
description: >
  İYUK m. 27 çerçevesinde yürütmenin durdurulması talebini iki şart (açıkça hukuka
  aykırılık + telafisi güç/imkânsız zarar) yönünden değerlendirir; teminat ve gerekçe
  zorunluluğunu vurgular.
user-invocable: true
---

# Yürütmenin Durdurulması — İYUK m. 27

## Konum hatırlatması

YD **istisnai** tedbirdir ve **gerekçeli** olmak zorundadır (m. 27/2). İki şart **birlikte** aranır.

## İki şart

1. **Açıkça hukuka aykırılık** — işlemin uygulanmasının açık hukuka aykırılığı.
2. **Telafisi güç veya imkânsız zarar** — uygulanması hâlinde doğacak zarar.

> Her ikisi birlikte gerçekleşmezse YD verilemez (m. 27/2). Gerekçe somut olmalı.

## Ek noktalar

- **Teminat (m. 27/6):** kural olarak teminat karşılığı; istisnaları.
- **Vergi davalarında özel rejim (m. 27/4):** tarh/ceza işlemlerinde dava açılması tahsilatı kendiliğinden durdurur (ihtirazi kayıt/teminat ayrımı) — `vergi-yargisi-rehberi.md`.
- **İvedi yargılama (m. 20/A)** ve **merkezî sınav (m. 20/B)** özel süre rejimleri.
- **İtiraz:** YD kararına itiraz mercii (BİM/Danıştay).

## Çıktı

İki-şart değerlendirme tablosu + somut gerekçe iskeleti + teminat notu. Karar hâkim/heyettedir. TASLAK ibareli.

---

## /idari-hakim:ehliyet-husumet

---
name: ehliyet-husumet
description: >
  İYUK m. 14-15 ilk inceleme: görev-yetki, ehliyet (menfaat ihlali), husumet (doğru
  idare), süre (m. 7 — 60/30 gün), idari merci tecavüzü gibi sebepleri kontrol eder.
user-invocable: true
---

# İlk İnceleme — İYUK m. 14-15

## Amaç

Dava dilekçesini esastan önce m. 14 yönlerinden incele; m. 15 ret/işlem sonuçlarını uygula.

## Kontrol (m. 14/3 sıralı)

1. **Görev ve yetki** — idari yargı + yetkili mahkeme.
2. **İdari merci tecavüzü** — önce başvurulması gereken idari merci (özel kanunda zorunlu idari başvuru öngörülmüşse) → m. 15/1-e dilekçe görevli idare merciine tevdi. (m. 11'deki üst makama başvuru isteğe bağlıdır; yapılırsa işlemeye başlamış dava açma süresini durdurur, otuz gün içinde cevap verilmezse istek reddedilmiş sayılır.)
3. **Ehliyet** — menfaat ihlali / kişisel-meşru-güncel menfaat (iptal); hak ihlali (tam yargı).
4. **İdari davaya konu kesin ve yürütülebilir işlem** mi.
5. **Süre (m. 7):** **idare 60 gün, vergi 30 gün**; ÇED ivedi 30 gün (m. 20/A). Süre aşımı 🔴 m. 15/1-b ret.
6. **Husumet** — doğru idareye yöneltilmiş mi; değilse m. 15/1-c re'sen husumet düzeltme.
7. **Dilekçe usulü (m. 3-5)** — şekil, aynı dilekçeyle dava açma şartları.

## Çıktı

m. 14 kontrol tablosu + m. 15 sonuç önerisi (ret / tevdi / düzeltme), 🔴🟠🟡 işaretli. Karar hâkimindir. TASLAK ibareli. Detay: `iyuk-rehberi.md`, `idari-yargi-yapisi-rehberi.md`.

---

## /idari-hakim:ivedi-yargilama

---
name: ivedi-yargilama
description: >
  İYUK m. 20/A ivedi yargılama ve m. 20/B merkezî sınav özel usulleri:
  kısalmış süreler, sınırlı/değişik kanun yolu, YD özellikleri. Hangi davaların
  bu rejime tabi olduğunu ve usul sapmalarını yapılandırır.
user-invocable: true
---

# İvedi Yargılama — İYUK m. 20/A ve 20/B

## m. 20/A — ivedi yargılama usulü

Kanunda sayılan işlemlerden doğan uyuşmazlıklarda uygulanır (m. 20/A/1): ihaleden yasaklama kararları hariç ihale işlemleri; acele kamulaştırma işlemleri; Özelleştirme Yüksek Kurulu kararları; 2634 s. Turizmi Teşvik K. uyarınca yapılan satış, tahsis ve kiralama işlemleri; 2872 s. Çevre K. uyarınca idari yaptırım kararları hariç ÇED sonucu alınan kararlar; 6306 s.K. uyarınca alınan Cumhurbaşkanı kararları.

**Genel rejimden sapmalar:**
- **Dava açma süresi 30 gün** (genel 60 gün yerine).
- Savunma/ara işlem süreleri kısa.
- **İstinaf yok** — ilk derece kararına karşı doğrudan **Danıştay'da temyiz** (kısa süre).
- **YD kararına itiraz edilemez** (m. 20/A özelliği).

## m. 20/B — merkezî sınav usulü

Merkezî sınav (ÖSYM vb.) iş ve işlemlerine ilişkin davalarda toplu/kısa süreli özel usul.

## Hâkim/kalem kontrolü

1. Dava bu özel rejimlerden birine giriyor mu? (Kanuni sayım — ArthurLegal MCP (`tr_`) teyidi.)
2. Süreler (dava açma, savunma, temyiz) genel rejimden farklı uygulandı mı?
3. Kanun yolu doğru mu (istinaf yok, m. 45/8; nihai karara tebliğden itibaren 15 gün içinde temyiz, m. 20/A/2-g)?
4. YD itiraz yasağı gözetildi mi?

## Çıktı

Rejim tespiti + süre/kanun-yolu sapma tablosu + usul kontrol listesi. TASLAK ibareli. Detay: `iyuk-rehberi.md`, `ced-rehberi.md`, `yurutmenin-durdurulmasi-rehberi.md`.

---

## /idari-hakim:ara-karar-bilgi-belge

---
name: ara-karar-bilgi-belge
description: >
  İdari yargıda re'sen araştırma ilkesi uyarınca verilecek bilgi ve belge ara kararını
  yapılandırır: işlemin unsurlarına göre eksik bilgi haritası, muhatap, süre ve uzatma,
  ara karara uymamanın etkisinin önceden belirtilmesi, devlet güvenliği istisnası,
  cevabın taraflara bildirilmesi. Kararı VERMEZ; ara karar iskeleti kurar.
user-invocable: true
---

# Bilgi ve Belge Ara Kararı — İYUK m. 20

## Konum hatırlatması

Danıştay, bölge idare mahkemeleri ile idare ve vergi mahkemeleri bakmakta oldukları davalara ait her türlü incelemeyi kendiliğinden yapar (İYUK m. 20/1). Ara karar iki tarafa da yöneltilebilir ve cevabı karşı tarafa bildirilir; yalnız bir tarafın dosyasının tamamlandığı izlenimi verilmez. Ara karara uymamanın sonucu önceden belirtilir; **bu sonucun belirlenmesi için hâkim/heyet takdiri ve onayı şarttır.** Asistan UYAP'a bağlanmaz, kayıt eklemez; dosya bilgisi kullanıcıdan gelir.

## Amaç

Re'sen araştırma ilkesi gereği istenecek bilgi ve belgeleri, işlemin unsurlarına göre eksik bilgi haritası çıkararak belirlemek; ara karar iskeletini muhatap, süre ve sonuç bilgisiyle birlikte hazırlamak.

## Dayanak (bu sohbette çekilir)

- **İYUK m. 20/1** — mahkemeler belirlenen süre içinde lüzum gördükleri evrakın gönderilmesini ve her türlü bilginin verilmesini taraflardan ve ilgili diğer yerlerden isteyebilir; ilgililer süresinde yerine getirmek zorundadır; haklı sebeplerle süre bir defaya mahsus uzatılabilir.
- **İYUK m. 20/2** — taraflardan biri ara kararının icaplarını yerine getirmezse, bunun verilecek karar üzerindeki etkisi mahkemece önceden takdir edilir ve ara kararında ayrıca belirtilir.
- **İYUK m. 20/3** — istenen bilgi ve belgeler Devletin güvenliğine veya yüksek menfaatlerine ilişkinse Cumhurbaşkanı ya da ilgili Cumhurbaşkanı yardımcısı veya bakan gerekçesini bildirerek vermeyebilir; verilmeyen bilgi ve belgelere dayanılarak ileri sürülen savunmaya göre karar verilemez.
- **İYUK m. 20/5** — dosyalar öncelikli işler gözetilerek geliş tarihlerine göre incelenir ve tekemmül sırasına göre karara bağlanır; diğer dosyalar tekemmülden itibaren en geç altı ay içinde sonuçlandırılır. **m. 19** — ara kararı verilen hâllerde kararın yerine getirilmesi üzerine dosya öncelikle incelenir.
- **İYUK m. 20/6** — istinaf incelemelerinde ve heyet hâlinde görülen davalarda bilgi ve belge istenmesine ve ek süre verilmesine ilişkin ara kararları daire başkanı, mahkeme başkanı veya dosyanın havale edildiği üye de verebilir.
- **İYUK m. 16/5** — davalara ilişkin işlem dosyalarının aslı veya onaylı örneği idarenin savunmasıyla birlikte gönderilir.
- **İYUK m. 27/5** — yürütmenin durdurulması istemli davalarda m. 16'daki süreler kısaltılabilir, tebliğin memur eliyle yapılmasına karar verilebilir.
- **İYUK m. 31** — bilirkişi, keşif ve delil tespiti gibi hususlarda HMK uygulanır; bilirkişiler bilirkişilik bölge kurulu listelerinden seçilir.
- **İYUK m. 2/1-a, 2/2** — iptal davasında yetki, şekil, sebep, konu ve maksat yönleri; idari yargı yetkisi hukuka uygunluk denetimiyle sınırlıdır, yerindelik denetimi yapılamaz.

## Girdi

- Dava türü, dava konusu işlem ve dayanağı
- Dosyadaki mevcut belgeler (işlem dosyası geldi mi), savunma
- Tartışmalı olgular; YD istemi var mı

## Adımlar

1. **Eksik bilgi haritası — işlemin unsurları:**
   - Yetki: işlemi yapan makamın yetkisi, yetki devri veya imza yetkisi belgesi
   - Şekil: usul adımları (savunma alınması, bildirim, kurul toplantı tutanağı, gerekçe)
   - Sebep: işlemin dayandığı olgular ve belgeler (tutanak, rapor, inceleme sonucu)
   - Konu: işlemin içeriği ve mevzuata uygunluğu
   - Maksat: kamu yararı ve takdir yetkisinin sınırları
   Tam yargı davasında ayrıca zarar ve illiyet belgeleri.
2. **Muhatap:** davalı idare / davacı / üçüncü kurum; her muhatap için ayrı kalem.
3. **Süre:** belirli ve makul; YD istemli işte kısaltma (m. 27/5); uzatma yalnız haklı sebeple ve bir defa (m. 20/1).
4. **Etki bildirimi (m. 20/2):** ara karara uyulmamasının karar üzerindeki etkisi önceden yazılır (örnek seçenek: "dosyadaki mevcut bilgi ve belgelere göre karar verileceği"); etki, taraflardan birine peşin sonuç yükleyecek biçimde değil, kanunun izin verdiği çerçevede yazılır.
5. **m. 20/3 kontrolü:** istenen belge Devletin güvenliği veya yüksek menfaatleri kapsamında olabilir mi; verilmezse o belgeye dayanan savunma karar temeli olamaz.
6. **Bilirkişi veya keşif gerekiyor mu:** İYUK m. 31 yoluyla HMK → `/hukuk-hakim:bilirkisi-raporu-denetimi`.
7. **Cevabın bildirimi:** gelen bilgi ve belgeler karşı tarafa bildirilir; görüş için süre (çelişmeli yargılama).

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Eksik bilgi matrisi:** | Unsur | Eksik bilgi / belge | Muhatap | Neden gerekli (hangi iddia veya savunma) | Süre | Risk |
2. **Ara karar iskeleti:**

```
T.C. [DOLDUR] [İDARE / VERGİ] MAHKEMESİ
ARA KARARI
Esas No: [DOLDUR]
Davacı: [DOLDUR]        Davalı: [DOLDUR]
Dava konusu işlem: [DOLDUR]

Dava dosyasının incelenmesinden, uyuşmazlığın çözümü için aşağıda belirtilen bilgi ve
belgelere ihtiyaç duyulduğu anlaşıldığından, 2577 sayılı Kanun'un 20. maddesi uyarınca;
1- Davalı idareden: [DOLDUR — bilgi / belge; işlem dosyasının aslı veya onaylı örneği]
2- Davacıdan: [DOLDUR]
3- [Üçüncü kurum]'dan: [DOLDUR]
istenilmesine; istenilen bilgi ve belgelerin ara kararın tebliğinden itibaren [DOLDUR]
gün içinde gönderilmesine; ara kararın gereğinin süresinde yerine getirilmemesi hâlinde
[DOLDUR — m. 20/2 uyarınca önceden belirtilen etki] hususunun bildirilmesine,
[tarih]'de [oybirliğiyle / oyçokluğuyla] karar verildi.
Başkan / Üye / Üye [DOLDUR]
```

3. **Takip satırı:** tebliğ tarihi, süre sonu, uzatma talebi, cevap, karşı tarafa bildirim.

**Risk skalası:**
- 🔴 Ara karar cevabı karşı tarafa bildirilmeden karar; m. 20/3 kapsamında verilmeyen belgeye dayanan savunmayla karar.
- 🟠 Uymamanın etkisi önceden belirtilmemiş; istenen belgenin işlemin hangi unsuruyla ilgili olduğu kurulmamış (gereksiz ara karar, süre kaybı).
- 🟡 Süre belirsiz; uzatma talebinin karara bağlanmaması.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: İYUK m. 2, 16, 19, 20, 27, 31 — bu sohbette çekildi mi, eşleşti mi.
- Süre hesapları hatırlatmadır; son günü hâkim/kalem teyit eder. Tebliğ tarihi gibi bilinmeyen bir olguda en erken olası gün esas alınır ve bu açıkça uyarı olarak yazılır.
- ⚠️ "Ara karar ve uymamanın etkisi hâkim/heyet takdirindedir; yerindelik denetimi yapılmaz."

## Sıradaki adımlar

- `/idari-kalem:dosya-tekemmul` — ara karar takibi ve tekemmül
- `/idari-hakim:idari-karar` — işlemin unsurları üzerinden denetim
- `/idari-hakim:yurutmenin-durdurulmasi` — YD istemli işte

---

> 🚧 v1.0.0 — `idari-hakim` 4 skill; v1.2.0'da bilgi ve belge ara kararı eklendi (toplam 5). Kalıp: `hukuk-hakim__skills.md`.
