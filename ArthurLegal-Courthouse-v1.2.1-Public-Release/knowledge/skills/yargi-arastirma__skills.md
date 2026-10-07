# yargi-arastirma — Skill Referans Kitapçığı

> Alan: Ortak araştırma katmanı (dal fark etmez: hukuk, ceza, idari, vergi) · Rol: **Hâkim + kalem** · Araç: ArthurLegal MCP (`tr_`)
> Toplam skill: 4
> Kullanım: `/yargi-arastirma:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Bu plugin kendi başına karar metni üretmez; gerekçe ve usul skill'lerinin dayanağını bulur ve doğrular. Araştırma iki yönlüdür: taslaktaki yönü destekleyen ve ona aykırı içtihat birlikte raporlanır. Her çıktı **TASLAK — hâkim/heyet onayı şart**.
> Rehber: `yargi-mcp-rehberi.md` (içtihat araçları, tarih süzgeci), `mevzuat-mcp-rehberi.md` bölüm 9 (madde doğrulama kapısı).

## İçindekiler

- /yargi-arastirma:ictihat-dogrulama — künyesi verilen kararı (kurum/daire, E., K., tarih) araçla bulma; künye parçalarının aynı karara ait olduğunu doğrulama
- /yargi-arastirma:karsi-gorus-taramasi — taslaktaki yöne aykırı ve çelişen içtihat; genel kurul ve içtihadı birleştirme kararları; iki yönlü rapor
- /yargi-arastirma:emsal-tarama — yerleşik içtihat taraması; tarih süzgeci kuralı ve ağırlık sıralaması
- /yargi-arastirma:aym-aihm-standart-kontrolu — gerekçeli karar, makul süre, silahların eşitliği gibi standartların taslak karara uygulanması

---

## /yargi-arastirma:ictihat-dogrulama

---
name: ictihat-dogrulama
description: >
  Dilekçede, bilirkişi raporunda, taslak gerekçede ya da hafızada geçen bir karar
  künyesini (kurum/daire, esas, karar, tarih) ArthurLegal MCP ile bulur; künyenin
  bütün parçalarının aynı karara ait olduğunu ve kararın kendisine yüklenen ilkeyi
  gerçekten içerdiğini denetler. Doğrulanamayan künye gövdeye girmez.
user-invocable: true
---

# İçtihat Doğrulama — Künye → Karar Eşleştirmesi

## Konum hatırlatması

Doğrulama tarafsız bir kontroldür. Bir tarafın gösterdiği künyenin doğrulanamaması o tarafın hukuki iddiasının yanlış olduğunu göstermez; yalnız o kararın dayanak olarak kullanılamayacağını gösterir. İddianın kendisi norm ve başka içtihatla ayrıca incelenir. Asistan UYAP'a bağlanmaz; künye kullanıcıdan gelir.

## Amaç

Gerekçeye, ara karara veya herhangi bir usul belgesine girecek her karar atfının gerçek, tek bir karara ait ve içerikçe isabetli olduğunu teslimden önce tespit etmek.

## Girdi

Kullanıcıdan (eksikse iste, varsayma):
- Künye, verildiği biçimiyle: kurum, daire/kurul, E., K., karar tarihi (AYM'de başvuru numarası ve karar tarihi)
- Künyenin nereden geldiği: taraf dilekçesi, bilirkişi raporu, taslak gerekçe, önceki not
- Karara yüklenen ilke: "Bu karar şunu söylüyor" cümlesi (varsa alıntı)

## Adımlar

1. **Künyeyi parçala.** Kurum, daire/kurul, E., K., tarih ayrı alanlara yazılır. Eksik alan varsa belirtilir; tahminle doldurulmaz.
2. **Aracı seç.**
   - Yargıtay, Danıştay, bölge adliye mahkemesi hukuk dairesi, yerel hukuk mahkemesi, kanun yararına bozma → `tr_ictihat_ara` (`courts`: `YARGITAYKARARI`, `DANISTAYKARAR`, `ISTINAFHUKUK`, `YERELHUKUK`, `KYB`; `chamber`: `H1`–`H23`, `C1`–`C23`, `HGK`, `CGK`, `BGK`, `D1`–`D17`, `IDDK`, `VDDK`)
   - Anayasa Mahkemesi → `tr_aym_ara` (`kind="bireysel"` veya `kind="norm"`)
   - Uyuşmazlık Mahkemesi → `tr_uyusmazlik_ara`
3. **Numarayı doğru yaz.** Bedesten eğik çizgi içeren sorguyu reddeder. Ölçüm (27.09.2026): `query="\"2024/4785\""` → "Sadece harf ve rakam içeren aramalar yapılabilir." Numara boşlukla yazılır ve daireyle daraltılır: `tr_ictihat_ara(query="\"2024 4785\"", courts=["YARGITAYKARARI"], chamber="H7")`. AYM aracında eğik çizgili başvuru numarası çalışır: `tr_aym_ara(query="2017/18458", kind="bireysel")` (aynı gün ölçüldü).
4. **Dört alanı aynı satırda eşleştir.** Sonuç satırındaki `chamber`, `esas_no`, `karar_no`, `karar_tarihi` künyeyle birlikte örtüşmelidir. Ölçüm (27.09.2026): bir Yargıtay dairesinde tek numarayla yapılan aramada aynı sayı bir kararda esas numarası, başka bir kararda karar numarası olarak döndü; üçüncü sonuç sayıyı yalnız metninde geçiriyordu. Yani "E. X, K. Y" künyesinin parçaları iki ayrı gerçek karara ait olabilir. Dört alanı birlikte taşıyan tek satır yoksa künye **doğrulanmamıştır**; E. ve K. için ayrı ayrı arama yapılır, çıkan kayıtlar yan yana konur.
5. **Metni oku.** Karar listesi metin taşımaz: `tr_ictihat_getir(document_id)` (AYM'de `tr_aym_getir(id, kind)`). Kontrol: karar künyeye yüklenen ilkeyi içeriyor mu; hangi olay, hangi norm ve hangi norm sürümü üzerine verilmiş; alıntı yapılacaksa cümle metinden birebir alınır.
6. **Durumu işaretle.** Bölge adliye mahkemesi sonuçlarında `kesinlesme` alanı (`KESİNLEŞTİ` / `KESİNLEŞMEDİ`) okunur; kesinleşmemiş karar kanun yolunda değişebilir. Kararın dayandığı madde sonradan değiştiyse (`tr_mevzuat_madde_getir` yanıtındaki değişiklik notları) bu ayrıca yazılır.
7. **Sınıflandır.**
   - **Doğrulandı:** dört alan aynı kararda, içerik örtüşüyor.
   - **Künye doğru, içerik örtüşmüyor:** karar var ama iddia edilen ilkeyi taşımıyor ya da başka bir olay veya norma ilişkin.
   - **Künye karışık:** parçalar farklı kararlara ait.
   - **Bulunamadı:** araç sonuç döndürmedi. Bu "karar yok" demek değildir; Bedesten'de istinaf ve yerel mahkeme kapsamı kısmidir.
   - **Kaynak erişilemedi:** yanıt `error`, `unavailable` veya `upstream_blocked` taşıyor.
8. **Doğrulanamayan künye gövdeye girmez.** "Doğrulanamadı" yazılır ve hemen ardından kaynağa uygun satır bırakılır: Yargıtay `UYARI: veri çekilemedi, teyidiniz gerekli: https://karararama.yargitay.gov.tr/`; Danıştay `UYARI: veri çekilemedi, teyidiniz gerekli: https://karararama.danistay.gov.tr/`; bölge adliye, bölge idare ve yerel mahkeme `UYARI: veri çekilemedi, teyidiniz gerekli: https://emsal.uyap.gov.tr/`; AYM `UYARI: veri çekilemedi, teyidiniz gerekli: https://kararlarbilgibankasi.anayasa.gov.tr/`; Uyuşmazlık Mahkemesi `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.uyusmazlik.gov.tr/`.

> Tempo: Bedesten IP başına 30 saniyede 10 istek kabul eder; aynı turda 5'ten fazla arama gönderilmez, `retry: true` gelirse beklenir ve sürdürülür. Doğrulama hız gerekçesiyle atlanmaz.

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Künye doğrulama tablosu**

| # | Verilen künye | Kaynağı | Araç ve sorgu | Bulunan kayıt (`citation`) | Daire / E. / K. / tarih | İçerik örtüşmesi | Sonuç | Risk |
|---|---|---|---|---|---|---|---|---|
| 1 | [DOLDUR] | dilekçe / rapor / taslak | `tr_ictihat_ara(...)` | [araç çıktısı] | ✓ / ✗ her alan için | örtüşüyor / örtüşmüyor | doğrulandı / karışık / bulunamadı | 🟢/🟠/🔴 |

2. **İçerik notu:** doğrulanan her karar için ilke cümlesi (metinden), olay özeti, dayandığı norm ve sürümü.
3. **Gerekçeye aktarım:** yalnız "doğrulandı" satırları; atıf biçimi `[ArthurLegal TR — kurum — E./K. — GG.AA.YYYY]`, AYM için `[ArthurLegal TR — AYM — B. No — GG.AA.YYYY]`. Taraf ve başvurucu adı yazılmaz.

**Risk skalası:**
- 🔴 Taslak gerekçenin taşıyıcı dayanağı doğrulanamadı veya künye karışık; gövdeden çıkarılmadan imzaya gidemez.
- 🟠 Künye doğru ama içerik iddiayı karşılamıyor; gerekçedeki cümle yeniden kurulmalı.
- 🟡 Kesinleşmemiş bölge adliye mahkemesi kararı ya da dayandığı madde sonradan değişmiş karar; ağırlığı düşük gösterilmeli.
- 🟢 Doğrulandı.

## İnceleyen notu

- Kullanılan araçlar ve sorgular (birebir), çağrı tarihi.
- "Künye kontrolü: N künye verildi; X doğrulandı, Y karışık, Z bulunamadı, W erişilemedi."
- Bulunamayan ve erişilemeyen her künye için UYARI satırı (yukarıdaki bağlantılarla).
- Tarafsızlık notu: doğrulanamayan künye, ilgili tarafın hukuki iddiası hakkında sonuç doğurmaz; iddia norm ve başka içtihatla ayrıca değerlendirilir.
- ⚠️ "Hangi kararın gerekçede kullanılacağı hâkim/heyet takdirindedir."

## Sıradaki adımlar

- `/yargi-arastirma:karsi-gorus-taramasi` — doğrulanan kararın aksi yönde içtihat var mı
- `/yargi-arastirma:emsal-tarama` — aynı ilkenin yerleşik olup olmadığı
- Gerekçe skill'ine dönüş (`/hukuk-hakim:gerekceli-karar`, `/ceza-hakim:hukum-taslagi`, `/idari-hakim:idari-karar`, `/vergi-hakim:vergi-karar`)
- `/karar-yayim:karar-kunye-ozeti` — doğrulanan kararın emsal kaydı

---

## /yargi-arastirma:karsi-gorus-taramasi

---
name: karsi-gorus-taramasi
description: >
  Taslakta benimsenen hukuki yönün aksine verilmiş ve birbiriyle çelişen içtihadı,
  genel kurul ve içtihadı birleştirme kararlarını tarar; iki yönü de aynı ölçütlerle
  raporlar. Doğrulama yanlılığını önlemek için gerekçe imzadan önce çalıştırılır.
  Hangi yönün benimseneceğini SEÇMEZ.
user-invocable: true
---

# Karşı Görüş Taraması — İki Yönlü İçtihat Raporu

## Konum hatırlatması

Tarama bir tarafı güçlendirmek için değil, gerekçenin karşılaması gereken aykırı içtihadı görünür kılmak için yapılır. "Destekleyen" ve "aykırı" nitelemesi taslaktaki yöne göredir, taraflara göre değil. Asistan yön seçmez; ağırlık ölçütlerini ve çelişki noktalarını sunar. Takdir hâkim/heyettedir. Asistan UYAP'a bağlanmaz; dosya bilgisi kullanıcıdan gelir, içtihat yalnız araçla çekilir.

## Amaç

Taslak gerekçenin dayandığı hukuki önermenin aksini söyleyen kararları, varsa uyuşmazlığı çözen genel kurul veya içtihadı birleştirme kararını ve aradaki farkı (olay, norm sürümü, usul) ortaya koymak.

## Girdi

- Hukuki mesele, soyut ve tarafsız 1-2 cümle (taraf adı, kişisel veri, Arthur Mask etiketi sorguya konmaz)
- Taslakta benimsenen yön (varsa) ve dayandığı kararlar (önce `/yargi-arastirma:ictihat-dogrulama`)
- Dal, ilgili daire/kurul, uygulanan norm

## Bağlayıcılık ve ağırlık (bu sohbette çekilerek teyit edilir)

- **Yargıtay içtihadı birleştirme kararları** benzer hukuki konularda Yargıtay genel kurullarını, dairelerini ve adliye mahkemelerini bağlar (2797 s. Yargıtay K. m. 45). Daireler arası içtihat uyuşmazlıklarının ve yerleşmiş içtihattan dönmenin içtihatların birleştirilmesi yoluyla çözümü: m. 15; genel kurullar ve daireler arası uyuşmazlıklar: m. 16.
- **Danıştay İçtihatları Birleştirme Kurulu kararlarına** Danıştay daire ve kurulları ile idari mahkemeler ve idare uymak zorundadır; kararlar Resmî Gazete'de yayımlanır (2575 s. Danıştay K. m. 39, 40).
- **Anayasa Mahkemesi kararları** yasama, yürütme ve yargı organlarını, idare makamlarını, gerçek ve tüzel kişileri bağlar (AY m. 153).
- **Israr kararının temyizinde** Danıştay İdari veya Vergi Dava Daireleri Kurulu kararlarına uyulması zorunludur (İYUK m. 50).
- **Kesin istinaf kararları arasında aykırılık:** bölge adliye mahkemesinde başkanlar kurulu (5235 s.K. m. 35/1-3), bölge idare mahkemesinde başkanlar kurulu (2576 s.K. m. 3/C) uyuşmazlığın giderilmesini Yargıtay'dan veya Danıştay'dan ister. Taramada aynı meselede farklı bölgelerin kesin kararları ayrışıyorsa bu yol ayrıca not edilir.
- Bunların dışında genel kurul kararı tek daire kararından, güncel ve süreklilik gösteren daire içtihadı tekil karardan ağır tartılır (bu bir ağırlık ölçütüdür, bağlayıcılık hükmü değildir).

## Adımlar

1. **Meseleyi iki önermeye çevir.** "X hâlinde Y sonucu doğar" / "X hâlinde Y sonucu doğmaz". Her önerme için ayrı terim seti (2-5 terim, `+` zorunlu, `"tam öbek"`).
2. **Önce kurullar.**
   - Yargıtay: `chamber="HGK"` / `"CGK"`; birleştirme için `chamber="BGK"`. Ölçüm (27.09.2026): `BGK` ve `+"içtihadı birleştirme"` yalnız 2 karar döndürdü; kapsam dardır, yokluk kanıtı değildir.
   - Danıştay: `chamber="IDDK"` / `"VDDK"`. Ölçüm (27.09.2026): `chamber="IBK"` iki ayrı sorguda 0 sonuç döndürdü. Danıştay birleştirme kararı Resmî Gazete'de yayımlandığından `tr_resmi_gazete_tara(query="İçtihatları Birleştirme", date_from=…, date_to=…)` ile aranır (en çok 60 gün; aralık bölünür); bulunamazsa `UYARI: veri çekilemedi, teyidiniz gerekli: https://karararama.danistay.gov.tr/`.
   - AYM: `tr_aym_ara(query=…, kind="norm")` — ilgili hükmün iptali veya iptal isteminin reddi; `kind="bireysel"` — hak ihlali standardı.
3. **Sonra daireler, iki yönde ayrı ayrı.** Aynı daire (ve iş bölümü değişmişse önceki daire) için her önermeyle ayrı arama; tarih süzgecinin iki ucu da verilir, dönen `karar_tarihi` alanları kontrol edilir (aralık dışı sonuç = süzgeç çalışmamış).
4. **Metni oku.** Listede metin yoktur; `tr_ictihat_getir` ile okunur. Olay, uygulanan norm, normun o tarihteki metni, sonuç ve gerekçenin taşıyıcı cümlesi not edilir.
5. **Norm sürümünü kontrol et.** Kararın uyguladığı madde sonradan değiştiyse (`tr_mevzuat_madde_getir` yanıtındaki değişiklik notları; usul kanunlarında 7251, 7499, 7589 sayılı Kanunlarla yapılan değişiklikler gibi) eski içtihat yeni metne kendiliğinden aktarılmaz.
6. **Ayırt et.** Çelişki gerçek mi, yoksa olay farkı mı (farklı olgu, farklı dava türü, kesin / kesin olmayan karar, farklı norm sürümü)?

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Mesele** (tarafsız cümle) ve iki önerme.
2. **Kurul düzeyi:** birleştirme / genel kurul / AYM kararı var mı → künye (yalnız çekilen), yön, özet; yoksa "bulunamadı" + kapsam notu + UYARI satırı.
3. **Yön A — taslaktaki yönü destekleyen** ve **Yön B — taslaktaki yöne aykırı**, aynı sütunlarla:

| Künye (`citation`) | Kurul/daire | Tarih | Olay benzerliği | Norm ve sürümü | Kesinleşme | Taşıyıcı cümle (metinden) |
|---|---|---|---|---|---|---|

4. **Çelişki haritası:** ayrışma hangi noktada; hangi karar hangi farka dayanıyor.
5. **Gerekçe için karşılama listesi:** taslağın, aykırı yöndeki hangi kararları hangi gerekçeyle ayırt etmesi gerektiği (seçenekli).
6. ⚠️ "Hangi yönün benimseneceği hâkim/heyet takdirindedir."

**Risk skalası:**
- 🔴 Taslak, bağlayıcı bir birleştirme veya AYM kararına aykırı yönü tartışmadan benimsemiş.
- 🟠 Güncel ve süreklilik gösteren aykırı kurul veya daire içtihadı gerekçede karşılanmamış.
- 🟡 Daireler arası çelişki var; gerekçede ayırt etme gerekir.
- 🟢 Aykırı içtihat bulunamadı (kapsam notuyla birlikte).

## İnceleyen notu

- Sorgular, süzgeçler, tarih kontrolü sonucu, kapsam sınırı ("aykırı karar bulunamadı" ≠ "aykırı karar yok").
- Madde kontrolü: 2797 m. 15, 16, 45; 2575 m. 39, 40; AY m. 153; İYUK m. 50; 5235 m. 35; 2576 m. 3/C — çıktıya girecekse bu sohbette `tr_mevzuat_madde_getir` ile çekilir ve eşleştirilir.
- Çekilemeyen karar için UYARI satırı; köşeli ayraç etiketi kullanılmaz.

## Sıradaki adımlar

- `/yargi-arastirma:emsal-tarama` — seçilen yönün yerleşikliği
- `/yargi-arastirma:ictihat-dogrulama` — taraf dilekçelerindeki künyeler
- İlgili gerekçe skill'i — "aykırı içtihadın karşılanması" paragrafı

---

## /yargi-arastirma:emsal-tarama

---
name: emsal-tarama
description: >
  Bir hukuki meselede yerleşik içtihadı arar: önce güncel norm, sonra kurul ve daire
  kararları; tarih süzgecini iki uçlu kullanır ve dönen tarihleri denetler. Tek karara
  "yerleşik" demez; ağırlık sıralaması ve kapsam sınırıyla raporlar.
user-invocable: true
---

# Emsal Tarama — Yerleşik İçtihat

## Konum hatırlatması

Emsal, gerekçeyi destekleyen bir ölçüttür; hâkimi bağlayan kararlar (içtihadı birleştirme, AYM) dışında sonucu belirlemez. Asistan kararı yazmaz; emsali okur ve sınıflandırır. Kişisel veri, taraf adı ve Arthur Mask etiketi arama sorgusuna konmaz. Asistan UYAP'a bağlanmaz; dosya bilgisi kullanıcıdan gelir, içtihat yalnız araçla çekilir.

## Amaç

Gerekçeye girecek içtihadın güncel, isabetli, okunmuş ve ağırlığı doğru gösterilmiş olmasını sağlamak.

## Girdi

- Hukuki mesele (soyut), ilgili norm(lar)
- Dal, ilgili daire/kurul; zaman penceresi ve gerekçesi (örn. ilgili maddenin değiştiği tarihten sonrası)
- Varsa kullanıcının elindeki kararlar (önce `/yargi-arastirma:ictihat-dogrulama`)

## Adımlar

1. **Önce norm.** İlgili madde `tr_mevzuat_madde_getir` ile çekilir; değişiklik notlarından yürürlük tarihleri okunur. Zaman penceresi buna göre kurulur: değişiklikten önceki kararlar eski metni uygular.
2. **Kurul ve daire.** `chamber` kodlarıyla (`HGK`, `CGK`, `IDDK`, `VDDK`, ilgili daire). Dairelerin iş bölümü dönem dönem değişir; iş bölümünün hangi dönemde hangi dairede olduğu kullanıcıdan teyit edilir ya da ilgili resmî karar arama sayfasıyla UYARI satırı bırakılır.
3. **Sorgu.** 2-5 hukuki terim; `+` zorunlu, `"tam öbek"`, gerekirse `-` hariç. Kullanıcının cümlesi yapıştırılmaz. Dosya numarası aranacaksa eğik çizgi yerine boşluk (`/yargi-arastirma:ictihat-dogrulama` adım 3).
4. **Tarih süzgeci kuralı.** `date_from` ve `date_to` birlikte verilir; dönen her sonucun `karar_tarihi` alanı kontrol edilir. Aralık dışı karar görülürse süzgeç uygulanmamıştır: iki uç açıkça verilerek yeniden aranır ve bu çıktıda yazılır. "En güncel içtihat" sonucuna bu kontrol yapılmadan varılmaz. `tr_ictihat_semantik_ara` yalnız `date_from` alır; o araçta da tarih sonuçtan denetlenir.
5. **Sıralama ve yerleşiklik.** `sort="desc"` en yeniyi öne getirir, yerleşikliği göstermez. Yerleşik içtihat için ölçüt: aynı kurul veya dairede farklı yıllara yayılan birden fazla karar aynı ilkeyi tekrar ediyor ve aynı dönemde aykırı karar bulunmuyor (`/yargi-arastirma:karsi-gorus-taramasi`). Tek karar "yerleşik" diye nitelenmez.
6. **Oku.** `tr_ictihat_getir(document_id)`; ilke cümlesi metinden birebir, olay özeti, uygulanan norm ve sürümü.
7. **Kapsam.** `ISTINAFHUKUK` ve `YERELHUKUK` kısmidir; bölge adliye mahkemesi sonuçlarında `kesinlesme` alanı okunur. Bölge idare mahkemesi kararları için bu araçta ayrı bir mahkeme türü yoktur; gerekiyorsa `UYARI: veri çekilemedi, teyidiniz gerekli: https://emsal.uyap.gov.tr/`. `tr_ictihat_semantik_ara` bir keşif aracı değil, anahtar kelimeyle çekilen ilk kararları anlamsal olarak sıralayan araçtır.

## Ağırlık sıralaması (gerekçede gösterim için)

| Sıra | Kaynak | Not |
|---|---|---|
| 1 | Yargıtay içtihadı birleştirme; Danıştay İçtihatları Birleştirme Kurulu; AYM | Bağlayıcı (2797 m. 45; 2575 m. 40; AY m. 153) |
| 2 | HGK / CGK / IDDK / VDDK | Genel kurul, tek daireden ağır |
| 3 | Daire — süreklilik gösteren | "Yerleşik" nitelemesi yalnız burada |
| 4 | Daire — tekil | "Bu yönde bir karar" diye gösterilir |
| 5 | Bölge adliye mahkemesi — kesinleşmiş / kesinleşmemiş | `kesinlesme` alanıyla |
| 6 | Yerel mahkeme | Yalnız bilgi |

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Mesele ve norm** (çekilen metin, sürüm).
2. **Emsal tablosu:**

| # | Künye (`citation`) | Ağırlık | Tarih | İlke (metinden) | Olay benzerliği | Norm sürümü | Durum |
|---|---|---|---|---|---|---|---|

3. **Yerleşiklik değerlendirmesi:** yerleşik / dağınık / aykırı kararlar mevcut / tespit edilemedi.
4. **Tarama yöntemi:** sorgular, süzgeçler, tarih kontrolü sonucu, kapsam sınırı.
5. **Gerekçeye aktarım önerisi:** yalnız okunan kararlar; atıf `[ArthurLegal TR — kurum — E./K. — GG.AA.YYYY]`.

**Risk skalası:**
- 🔴 Gerekçede okunmamış karara atıf var ya da doğrulanmamış künye kullanılmış.
- 🟠 Tarih süzgeci kontrol edilemedi veya aralık dışı sonuç çıktı; "güncel" nitelemesi dayanaksız.
- 🟡 Tek karara dayalı "yerleşik içtihat" nitelemesi; kesinleşmemiş bölge adliye mahkemesi kararı.
- 🟢 Bilgi notu.

## İnceleyen notu

- Kullanılan araç, sorgu ve süzgeçler; tarih kontrolü; kapsam.
- Madde kontrolü: meseleye ait madde(ler) bu sohbette çekildi mi; ağırlık tablosundaki 2797 m. 45, 2575 m. 40, AY m. 153 çıktıya girecekse çekilir.
- Çekilemeyen emsal için UYARI satırı (Yargıtay https://karararama.yargitay.gov.tr/, Danıştay https://karararama.danistay.gov.tr/, bölge adliye, bölge idare ve yerel mahkeme https://emsal.uyap.gov.tr/).
- ⚠️ "Emsalin gerekçede nasıl kullanılacağı hâkim/heyet takdirindedir."

## Sıradaki adımlar

- `/yargi-arastirma:karsi-gorus-taramasi`
- `/yargi-arastirma:ictihat-dogrulama` — tablodaki künyelerin son kontrolü
- `/karar-yayim:karar-kunye-ozeti` — emsal kaydı

---

## /yargi-arastirma:aym-aihm-standart-kontrolu

---
name: aym-aihm-standart-kontrolu
description: >
  Taslak kararı (gerekçe, ara karar, tutukluluk kararı, istinaf kararı) Anayasa ve
  AİHS'in adil yargılanma ve kişi özgürlüğü standartlarına göre denetler: gerekçeli
  karar hakkı, silahların eşitliği ve çelişmeli yargılama, makul süre, masumiyet
  karinesi, hukuka aykırı delil, aleniyet, kanun yolunun gösterilmesi. Somut AYM veya
  AİHM kararı yalnız araçla çekilip okunduysa anılır.
user-invocable: true
---

# AYM / AİHM Standart Kontrolü — Taslak Karar Denetimi

## Konum hatırlatması

Bu skill ihlal tespiti yapmaz, karar yazmaz. Taslağı imzadan önce, sonradan bireysel başvuruda ihlal veya kanun yolunda bozma sebebi olabilecek noktalar yönünden tarar. Değerlendirme ve takdir hâkim/heyettedir.

## Amaç

Taslak kararı imzadan önce Anayasa ve AİHS'in adil yargılanma ve kişi özgürlüğü standartları yönünden taramak; sonradan ihlal veya bozma sebebi olabilecek noktaları önem derecesiyle göstermek.

## Dayanak (bu sohbette çekilir)

- **AY m. 36** — herkes meşru vasıta ve yollardan faydalanarak yargı mercileri önünde iddia ve savunma ile adil yargılanma hakkına sahiptir.
- **AY m. 141** — duruşmaların açıklığı ve istisnası; bütün mahkemelerin her türlü kararlarının gerekçeli yazılması; davaların en az giderle ve mümkün olan süratle sonuçlandırılmasının yargının görevi olması.
- **AY m. 19** — kişi hürriyeti ve güvenliği; tutuklananların makul süre içinde yargılanmayı ve serbest bırakılmayı isteme hakkı.
- **AY m. 38** — suçluluğu hükmen sabit oluncaya kadar kimse suçlu sayılamaz; kanuna aykırı olarak elde edilmiş bulgular delil olarak kabul edilemez.
- **AY m. 40** — devlet, işlemlerinde ilgililerin hangi kanun yollarına ve mercilere başvuracağını ve sürelerini belirtmek zorundadır.
- **AY m. 90** — temel hak ve özgürlüklere ilişkin usulüne göre yürürlüğe konulmuş milletlerarası andlaşmalarla kanunlar çatışırsa andlaşma hükümleri esas alınır.
- **AY m. 148; 6216 s.K. m. 45, 50** — bireysel başvuru (AİHS kapsamındaki haklar, olağan kanun yollarının tüketilmesi); ihlal bir mahkeme kararından kaynaklanmışsa yeniden yargılama için dosya ilgili mahkemeye gönderilir.
- **AİHS m. 6/1** — herkes davasının, yasayla kurulmuş, bağımsız ve tarafsız bir mahkeme tarafından, adil ve kamuya açık olarak ve makul bir süre içinde görülmesini isteme hakkına sahiptir. Mevzuat aracında yoktur; madde Sözleşme'nin resmî Türkçe metninden ya da AYM kararındaki alıntıdan (`tr_aym_getir`) okunur. Okunamadıysa: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.echr.coe.int/documents/d/echr/convention_tur`. AİHM kararları için: `UYARI: veri çekilemedi, teyidiniz gerekli: https://hudoc.echr.coe.int/`.

## Girdi

- Taslak metin (gerekçe, ara karar, tutukluluk kararı veya istinaf kararı)
- Taraf iddiaları özeti: hangileri sonucu değiştirebilecek nitelikte (esaslı)
- Usul geçmişi: hangi belge kime tebliğ edildi, cevap ve itiraz süreleri, duruşma tarihleri, dosyanın toplam süresi
- UYAP'a bağlanılmaz; bu bilgiler kullanıcıdan gelir.

## Standart kontrol listesi

1. **Gerekçeli karar hakkı.** AYM içtihadına göre mahkeme her iddiaya ayrıntılı yanıt vermek zorunda değildir; ancak davanın sonucunu değiştirebilecek nitelikteki esaslı iddialara ilgili ve yeterli bir yanıt verilmeli, davanın esas sorunlarının incelendiği gerekçeden anlaşılmalıdır `[ArthurLegal TR — AYM — B. No: 2014/8891 — 10.05.2017]` (27.09.2026'da çekildi). Yöntem: taslaktaki esaslı iddia listesi → her biri için gerekçede karşılık var mı. Dal bağlantısı: HMK m. 297/1-c; CMK m. 34, 230 ve m. 289/1-g (hükmün m. 230 gereğince gerekçeyi içermemesi hukuka kesin aykırılıktır); idari ve vergi yargısında AY m. 141.
2. **Silahların eşitliği ve çelişmeli yargılama.** Her delil, rapor ve görüş taraflara bildirildi mi; görüş bildirme ve itiraz imkânı tanındı mı (bilirkişi raporu tebliği ve itiraz: HMK m. 280-281; istinaf dilekçesine cevap: HMK m. 347, CMK m. 277; idari yargıda dilekçe teatisi: İYUK m. 16). AYM'ye göre bu ilkeler mutlak değildir; aykırılığın yargılamanın bütünü içinde hakkaniyeti zedeleyip zedelemediğine bakılır. Doğrulanmış örnek: istinaf dilekçesine cevap süresi dolmadan dosyanın bölge adliye mahkemesine gönderilmesi ve dairenin bu süre dolmadan kesin karar vermesi, silahların eşitliği ve çelişmeli yargılama ilkelerinin ihlali sayılmıştır `[ArthurLegal TR — AYM — B. No: 2017/18458 — 10.02.2021]` (27.09.2026'da çekildi). Çıktıya girecekse `tr_aym_getir` ile yeniden çekilir.
3. **Makul süre.** AYM'nin kullandığı ölçütler: davanın karmaşıklığı, yargılamanın kaç dereceli olduğu, tarafların ve ilgili makamların yargılama sürecindeki tutumu, başvurucunun davanın hızla sonuçlandırılmasındaki menfaatinin niteliği; ceza muhakemesinde sürenin başlangıcı isnadın bildirilmesi, tedbir uygulanması veya kamu davasının açılmasıdır `[ArthurLegal TR — AYM — B. No: 2014/176 — 09.09.2015]` (27.09.2026'da çekildi). Taslak aşamasında somut kontroller: duruşmalar arası süre (HMK m. 147/3: üç aydan uzun olamaz, zorunlu hâlde gerekçeyle daha uzun), bilirkişi süresi (HMK m. 274), idari yargıda tekemmül sırası ve altı ay (İYUK m. 20/5), tutuklu işlerde azami süreler (CMK m. 102).
4. **Masumiyet karinesi (ceza).** Ara kararlarda, tutukluluk kararlarında ve gerekçede suçluluğu peşin kabul eden ifade var mı (AY m. 38); "yüklenen suçun sanık tarafından işlendiğinin sabit olmaması" beraat nedenidir (CMK m. 223/2-e).
5. **Hukuka aykırı delil.** Hükme esas alınan delillerin hukuka uygun elde edildiği tartışıldı mı; hukuka aykırı deliller gerekçede ayrıca ve açıkça gösterildi mi (AY m. 38; CMK m. 206/2-a, 217/2, 230/1-b, 289/1-i).
6. **Kişi özgürlüğü (tutukluluk).** Kuvvetli suç şüphesi, tutuklama nedeni, ölçülülük ve adli kontrolün yetersizliği somut olgularla gösterilmiş mi (CMK m. 101/2); matbu ifade var mı → `/ceza-hakim:tutukluluk-incelemesi`.
7. **Aleniyet.** Kapalı duruşma kararı gerekçeli ve kanuni hâle dayanıyor mu (AY m. 141; HMK m. 28; CMK m. 182, 185).
8. **Kanun yolunun gösterilmesi.** Kanun yolu, mercii ve süresi hükümde açık mı (AY m. 40; HMK m. 297/1-ç; CMK m. 34/2, 232/6).

## Çıktı yapısı

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

| Standart | Dayanak | Taslaktaki karşılığı (paragraf) | Risk | Giderme seçenekleri |
|---|---|---|---|---|
| Gerekçeli karar | AY m. 36, 141 | [DOLDUR] | 🔴/🟠/🟡/🟢 | [seçenekli] |
| Silahların eşitliği / çelişmeli yargılama | AY m. 36 | [DOLDUR] | | |
| Makul süre | AY m. 36, 141, 19 | [DOLDUR] | | |
| … | | | | |

- **Karşılanmamış esaslı iddialar listesi** (her biri için "kabul yönünde / ret yönünde karşılama" iki seçenek; hangisinin yazılacağı hâkim takdiri).
- **Çekilen AYM kararları** (yalnız bu sohbette okunanlar; B. No ve tarih; taraf veya başvurucu adı yazılmaz).

**Risk skalası:**
- 🔴 Esaslı bir iddia karşılanmamış; bir tarafa cevap veya itiraz imkânı tanınmadan aleyhine karar kurulmuş; hukuka aykırı delil tartışılmadan esas alınmış.
- 🟠 Matbu veya soyut gerekçe; kapalı duruşma gerekçesiz; kanun yolu bilgisi eksik.
- 🟡 Makul süre risk işaretleri; masumiyet karinesiyle bağdaşmayabilecek ifade.
- 🟢 Bilgi notu.

## İnceleyen notu

- Madde kontrolü: AY m. 19, 36, 38, 40, 90, 141, 148; 6216 m. 45, 50; ilgili usul maddeleri — bu sohbette çekildi mi, eşleşti mi.
- AİHS metni ve AİHM kararları bu connector'da yok. AİHS maddesi resmî Türkçe metinden ya da AYM kararındaki alıntıdan okunmadıysa `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.echr.coe.int/documents/d/echr/convention_tur`; AİHM kararı için `UYARI: veri çekilemedi, teyidiniz gerekli: https://hudoc.echr.coe.int/`.
- Taraf ve başvurucu adı yazılmaz; AYM kararı B. No ve tarihle anılır.
- ⚠️ "Bu kontrol ihlal tespiti değildir; değerlendirme ve takdir hâkim/heyettedir."

## Sıradaki adımlar

- İlgili gerekçe skill'ine dönüş (karşılanmamış iddialar paragrafı)
- `/ceza-hakim:gerekce-denetimi` (ceza) veya `/hukuk-hakim:bilirkisi-raporu-denetimi` (itirazların karşılanması)
- `/yargi-arastirma:emsal-tarama` — ilgili standartta güncel AYM çizgisi

---

> v1.2.0 — `yargi-arastirma` ortak araştırma katmanı, 4 skill. Kalıp: `hukuk-hakim__skills.md`.
