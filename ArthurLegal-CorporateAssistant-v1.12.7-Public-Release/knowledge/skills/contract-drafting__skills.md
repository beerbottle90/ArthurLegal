# contract-drafting - Skill Referans Kitapcigi

> Alan: Sozlesme uretimi: redline, belge turet, versiyon karsilastir, tadil, playbook incelemesi, ture gore sozlesme hazirlama
> Toplam skill: 16
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.
> Aktif entite: Tum skill'ler company-profile.md -> Bolum 0 'Aktif entite' secimini baz alir
> (varsayilan: [Şirket/Büro adı] -> Bolum A). Cikti dili / onay zinciri / yargi cevresi buradan gelir.

## Icindekiler

- /contract-drafting:araci-is-birligi (77 satir)
- /contract-drafting:belge-turet (83 satir)
- /contract-drafting:cold-start-interview (40 satir)
- /contract-drafting:eser-sozlesmesi (78 satir)
- /contract-drafting:hizmet-sozlesmesi (76 satir)
- /contract-drafting:ingilizce-genel-kosullar (77 satir)
- /contract-drafting:mal-alim-sozlesmesi (79 satir)
- /contract-drafting:mutabakat-zapti (75 satir)
- /contract-drafting:playbook-inceleme (120 satir)
- /contract-drafting:redline-contract (88 satir)
- /contract-drafting:satinalma-sartnamesi (77 satir)
- /contract-drafting:sponsorluk-sozlesmesi (78 satir)
- /contract-drafting:tadil-protokol (77 satir)
- /contract-drafting:tasima-sozlesmesi (79 satir)
- /contract-drafting:veri-aktarim-protokolu (78 satir)
- /contract-drafting:versiyon-karsilastir (64 satir)

---

## Kaynak katmanı: /legal-research

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur;
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar; gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | `/legal-research:sozlesme-emsali` |
| AZ hukuku secilmisse emredici hukum kontrolu: akt + statu | `/legal-research:az-mevzuat` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil): okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `references/eqanun-mcp-rehberi.md` · `references/lex-scholar-rehberi.md` · `references/resourcecontracts-rehberi.md` · `references/karsilastirmali-hukuk-rehberi.md` · `references/nl-rechtspraak-mcp-rehberi.md` · `references/pl-sejm-mcp-rehberi.md` · `references/at-ris-mcp-rehberi.md` · `references/ie-statutebook-mcp-rehberi.md` · `references/fi-finlex-mcp-rehberi.md` · `references/es-boe-mcp-rehberi.md`

---

## /contract-drafting:araci-is-birligi

---
name: araci-is-birligi
description: >
  Aracılar (simsar, broker, emlak ya da ticari aracı) arasında iş birliği sözleşmesini sıfırdan kurar:
  portföy ve müşteri paylaşımı, bedel ve komisyonun bölüşülmesi, müşteriyle doğrudan temas yasağı,
  temsil yetkisinin bulunmaması. Simsarlık ücretinin doğma şartını ve taşınmazda yazılı şekli
  işaretler; örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Aracılar Arası İş Birliği Sözleşmesi Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** hangi aracıyı temsil ediyoruz? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Konu:** taşınmaz, sigorta, ticari mal, başka?
3. **Düzenlenmiş faaliyet mi?** Aracılık izne ya da yetki belgesine bağlıysa o mevzuat ayrıca araştırılır.
4. **Komisyon:** oran ya da tutar, paylaşım anahtarı, ödeme zamanı.
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 1'deki uzun form sırası, kısaltılmış. Türe özgü maddeler (rehber bölüm 8 madde 3.g):

- **Portföy ve müşteri:** tanım, getiren tarafın tespiti (kayıt ve tarih), ortak müşteride paylaşım.
- **Komisyon:** hangi olayla doğduğu ve ne zaman ödendiği (asıl sözleşmenin kurulması, geciktirici koşul), gider.
- **Doğrudan temas ve atlatma yasağı:** kapsam, süre, ceza koşulu.
- **Temsil yetkisinin bulunmaması** ve her tarafın kendi mevzuat yükümlülükleri.
- **Müşteri verisi:** paylaşımın dayanağı ve gerekiyorsa veri aktarım protokolü.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- TBK m. 520 (simsarlık: kural olarak vekâlet hükümleri uygulanır; taşınmaz simsarlığı yazılı yapılmadıkça geçerli olmaz)
- TBK m. 521 (simsar ancak faaliyeti sonucunda sözleşme kurulursa ücrete hak kazanır; geciktirici koşulda ücret koşul gerçekleşince ödenir; gider kararlaştırılmışsa sözleşme kurulmasa da ödenir)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Aracılar Arası İş Birliği Sözleşmesi: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Müşteri verisi paylaşılıyorsa `/contract-drafting:veri-aktarim-protokolu`.
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:belge-turet

---
name: belge-turet
description: >
  Örnek/emsal bir belgeden (şablon) yeni sözleşme/protokol TÜRETİR — şablonun yapısını
  çıkarır, yeni işin parametreleriyle uyarlar, doldurulacak alanları [DOLDUR] işaretler,
  TBK/TTK emredici hüküm + standart klozlar ile uyumlar. Tipik: süre uzatım
  protokolü, EPC/PPA/vendor sözleşmesi, NDA, hissedar/JV, kredi tadili.
user-invocable: true
---

# Şablon / Emsalden Belge Türetme

> Elindeki bir örnek belgeden (önceki bir sözleşme, standart şablon, emsal protokol) **yeni bir belge** üretir. Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı.

## ADIM 0 — Girdi

1. **Şablon/emsal belge:** kullanıcı yapıştırsın/yüklesin (yoksa: hangi belge tipini istediğini sor, `references/redline-konvansiyonlari-rehberi.md` bölüm 8'deki iskeletle başla).
2. **Yeni işin parametreleri** — taraflar, konu, tutar/süre, özel şartlar, fark eden noktalar.
3. **Hangi tip?** EPC · PPA/elektrik satış · vendor/tedarik · NDA · hissedar/JV · kredi/finansman · **süre uzatım/ek protokol** · diğer.

## ADIM 1 — Şablonu analiz et

- **Yapı haritası:** bölüm/madde başlıkları (başlangıç hükümleri, tanımlar, edimler, bedel/ödeme, süre, mücbir sebep, sorumluluk, gizlilik, fesih, uyuşmazlık, ekler).
- **Değişken alanlar:** şablondaki örneğe-özgü değerler (taraf adı, tarih, tutar, proje) → yeni parametrelerle değişecek.
- **Sabit/standart klozlar:** korunacak (boilerplate) ama şirket standardıyla kıyasla.

## ADIM 2 — Yeni belgeyi üret

- Yapıyı koru; değişken alanları yeni parametrelerle doldur; bilinmeyenleri **`[DOLDUR — ...]`** bırak.
- **Standart klozları** `references/redline-konvansiyonlari-rehberi.md` bölüm 5'teki sete göre ekle ve teyit et. Şablon verilmediyse aynı rehberin 7 ile 11. bölümlerini (iskelet, karar listesi, sık hatalar, Word düzeni) örnek al; oradaki ifadeyi birebir aktarma, işe göre yeniden kur.
- **Emredici hüküm kontrolü:** şablondaki bir kloz emredici kurala aykırıysa düzelt + flag (`[ArthurLegal TR — kanun m. X — GG.AA.YYYY]`, madde çekildikten sonra). (Örn. tüketici/iş sözleşmesinde aleyhe kloz, fahiş cezai şart TBK m.182, çalışan buluşu klozunda SMK m. 117 emredici sınırı.)
- **Madde doğrulama kapısı (teslim öncesi, zorunlu):** Belge gövdesine yazılan her kanun maddesi (şablondan gelen, bu kitapçıktaki örneklerden gelen veya yeni eklenen) `tr_mevzuat_madde_getir` ile çekilir; kloz maddeye ne yüklüyorsa (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirilir. Eşleşmiyorsa numara korunup açıklama uydurulmaz. Çekilemiyorsa madde numarası gövdeden çıkarılır, kloz numarasız kurulur ("ilgili mevzuatın emredici hükümleri saklıdır") ve eksik İnceleyen notuna yazılır. Bu kitapçıktaki örnek madde numaraları (TBK m.13, 136, 138, 182 gibi) doğrulama değildir. Yol: `references/mevzuat-mcp-rehberi.md` bölüm 9.
- Şablon eski tarihliyse: **mevzuat değişikliği** kontrolü (atıflar güncel mi?).

## ADIM 3 — Değişiklik notu

Yeni belgenin şablondan **nerede ayrıldığını** açıkça listele: hangi alanlar dolduruldu, hangi klozlar eklendi/çıkarıldı, hangi `[DOLDUR]` kaldı.

## Örnek: süre uzatım protokolü

```markdown
[ANA SÖZLEŞME ADI] – SÜRE UZATIM PROTOKOLÜ (Ek Protokol No: [N])

Taraflar: [Müvekkil / Şirket] ([adres/VKN]) ile [Karşı Taraf]
Ana Sözleşme: GG.AA.YYYY tarihli [sözleşme adı] ("Ana Sözleşme")

1. KONU: İşbu Protokol, Ana Sözleşme'nin [süre maddesi no] maddesinde düzenlenen
   süreyi uzatmak amacıyla akdedilmiştir.
2. SÜRE UZATIMI: Ana Sözleşme'nin süresi [yeni bitiş tarihi]'ne kadar uzatılmıştır.
   [Gerekçe: mücbir sebep / iş artışı / mutabakat — TBK m.136 atfı varsa]
3. BEDEL/ŞARTLAR: [değişen bedel veya "bedel/şartlar aynen geçerlidir"]
4. SAKLILIK: Ana Sözleşme'nin işbu Protokol'le değiştirilmeyen tüm hükümleri
   aynen yürürlüktedir.
5. YÜRÜRLÜK: İşbu Protokol imza tarihinde yürürlüğe girer; Ana Sözleşme'nin ayrılmaz
   ekidir. Damga vergisi: [DOLDUR — DVK kontrolü].
Tarih / İmzalar: [Müvekkil / Şirket] (yetkili: [imza yetkilisi]) — [Karşı Taraf]
```

## Çıktı
```markdown
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN İMZALANMAZ

# Türetilen Belge — [tip] — [taraflar]

## ⚠️ İnceleyen notu
- **Şablon:** [kaynak emsal] · **Tip:** [...]
- **Doldurulan / [DOLDUR] kalan:** N / N
- **Eklenen standart klozlar:** [liste]
- **Emredici hüküm/güncellik düzeltmesi:** [N adet] `[ArthurLegal TR — kanun m. X — GG.AA.YYYY]`
- **Madde kontrolü:** [belgedeki her madde atfı → okundu ve eşleşti / çekilemedi, gövdeden çıkarıldı] — belgede madde atfı varsa bu satır doldurulmadan teslim edilmez
- **Onay:** Baş Hukuk Müşaviri + dış vekil şart

[yeni belge metni]

## Şablondan farklar
[liste]

## Sonraki adımlar
> 1. **Redline incele** — `/contract-drafting:redline-contract` ile son kontrol
> 2. **[DOLDUR] alanlarını tamamla** — eksik parametreler
> 3. **Governing law / yaptırım** — yabancı taraf varsa
> 4. **Başka**

**One question I'd ask:** [örn. "Bu emsal hangi işten geldi? O işe özgü taviz/özel kloz varsa yeni belgeye sessizce taşımayalım."]
```

---

## /contract-drafting:cold-start-interview

---
name: cold-start-interview
description: >
  contract-drafting eklentisini ilk kez kuran kullanıcı için kısa röportaj — rol,
  birincil ortam (Claude.ai Projects / Claude Code), varsayılan çıktı formu (redline
  görünümü / temiz+liste / tablo), standart klozlar/şablonlar, onay zinciri.
  CLAUDE.md profilini doldurur. `--redo` ile yeniden çalışır.
user-invocable: true
---

# contract-drafting — Cold Start Interview

Amaç: `CLAUDE.md` profilindeki `[DOLDUR]` alanlarını 5-7 soruda doldurmak. Önce `company-profile.md` + `references/redline-konvansiyonlari-rehberi.md` okunur.

## Akış

### Adım 0 — Bağlam
`company-profile.md` + bu plugin `CLAUDE.md` oku. Dolu alanları tekrar sorma.

### Adım 1 — Kullanıcı & ortam
> 1. Adın/rolün? ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri] / diğer)
> 2. Birincil ortam: **Claude.ai Projects** (markdown redline) mı, **Claude Code/VS Code** (gerçek .docx tracked-changes) mı? — çıktı yeteneğini belirler.

### Adım 2 — Çıktı tercihi
> 3. Varsayılan redline formu: (a) redline görünümü, (b) temiz revize + değişiklik/comment listesi, (c) yapılandırılmış tablo, (d) her seferinde sor.
> 4. Comment'lerde fallback pozisyon her zaman yer alsın mı? (önerilen: evet)

### Adım 3 — Şablon & onay
> 5. Sık kullandığın şablon/emsal türleri? (EPC, PPA/elektrik satış, vendor/tedarik, NDA, kredi/finansman, hissedar/JV, süre uzatım protokolü)
> 6. Standart klozlar (mücbir sebep, sınırlı sorumluluk, yaptırım/uyum, uyuşmazlık, EPDK devir, KVKK) varsayılan eklensin mi?
> 7. İmza öncesi onay eşiği? (varsayılan: Baş Hukuk Müşaviri; yüksek tutar/stratejik + Genel Müdür)

### Adım 4 — Yaz ve onayla
Cevapları `CLAUDE.md` `[DOLDUR]` alanlarına işle (özet göster, onay al, yaz). Matter workspace açık mı? Varsayılan: açık.

## Çıktı
Kısa özet + güncellenen alanlar + "Artık `/contract-drafting:redline-contract`, `:belge-turet`, `:versiyon-karsilastir`, `:tadil-protokol` kullanabilirsin." yönlendirmesi.

## Not
`--redo`: tüm alanları yeniden sor.

---

## /contract-drafting:eser-sozlesmesi

---
name: eser-sozlesmesi
description: >
  Eser ya da inşaat (yapım) sözleşmesini sıfırdan kurar: uzun form iskelet, işe başlama ve
  tamamlama süreleri, iş programı, malzeme ve ekipman, geçici ve kesin kabul, mülkiyet ve hasarın
  geçişi, askıya alma, iş sağlığı ve güvenliği ile çevre, saha teslimi ve temizliği, tüm riskler
  sigortası. Standart kloz seti ve karar listesiyle; örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Eser ve İnşaat Sözleşmesi Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** iş sahibi mi, yüklenici mi? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Bedel:** götürü bedel mi, birim fiyat mı; hakediş dönemi ve kesintiler?
3. **Saha:** iş, iş sahibinin taşınmazında mı yapılacak? Alt yüklenici kullanılacak mı?
4. **Kamu ihalesi mi?** Öyleyse kamu ihale mevzuatı ve tip sözleşme uygulanır; bu akış özel hukuk sözleşmesi içindir, avukata işaretleyin.
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 1'deki uzun form sırası. Türe özgü maddeler (rehber bölüm 8 madde 3.c):

- **Süre ve iş programı:** işe başlama ve tamamlama süreleri, iş programı, gecikmede ceza koşulu ve tavanı.
- **Malzeme ve ekipman:** kimin sağladığı, kalite ve onay, artan malzemenin akıbeti.
- **Kabul:** geçici kabul tutanağı, eksik ve kusur listesi, garanti süresi, kesin kabul; kabul ile ayıp bildirimi arasındaki ilişki.
- **Mülkiyet ve hasarın geçişi, askıya alma, saha teslimi ve temizliği.**
- **İş sağlığı ve güvenliği ile çevre:** uygunsuzluk tablosu ve cezası (rehber bölüm 5 madde 19); tüm riskler sigortası.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- TBK m. 470 (eser sözleşmesinin tanımı)
- TBK m. 474 (iş sahibi eseri teslimden sonra imkân bulur bulmaz gözden geçirir ve ayıbı uygun sürede bildirir; her taraf bilirkişi incelemesi isteyebilir)
- TBK m. 475 (seçimlik haklar: dönme, bedelden indirim, ücretsiz onarım; eser iş sahibinin taşınmazındaysa ve sökülmesi aşırı zarar doğuracaksa dönme hakkı kullanılamaz)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Eser ve İnşaat Sözleşmesi: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Süre uzatımı ya da iş artışı için `/contract-drafting:tadil-protokol`.
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:hizmet-sozlesmesi

---
name: hizmet-sozlesmesi
description: >
  Hizmet, danışmanlık ya da eğitim sözleşmesini sıfırdan kurar: uzun form iskelet, hizmet planı ve
  performans denetimi, personel ve alt işveren ayrımı, hizmet tamamlama tutanağı, ilave işler;
  danışmanlıkta çıktıların mülkiyeti ve çıkar çatışması, eğitimde katılımcı verisi. Standart kloz
  seti ve ticari karar listesiyle; örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Hizmet, Danışmanlık ve Eğitim Sözleşmesi Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** hizmet alan mı, hizmet veren mi? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Tür:** hizmet, danışmanlık ya da eğitim; tek seferlik mi, süreli mi?
3. **Çalışma yeri:** hizmet veren, hizmet alanın işyerinde kendi personeliyle mi çalışacak? (alt işveren riski, ADIM 3)
4. **Kişisel veri:** hizmet sırasında kişisel veri işlenecek mi, yurt dışına aktarılacak mı?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 1'deki uzun form sırası. Türe özgü maddeler (rehber bölüm 8 madde 3.b):

- **Hizmet planı:** kapsam, performans ölçütleri ve denetimi, hizmet tamamlama tutanağı, ilave işler ve süre uzatımı.
- **Personel:** hizmet verenin personelini kendi yönetiminde çalıştırdığı, işe giriş ve SGK belgelerini sunacağı, işçilik alacağı yüzünden yapılan ödemelerde rücu hakkı. Hizmet, hizmet alanın işyerinde yürütülecekse asıl işveren ile alt işveren ilişkisinin kanuni koşullarını ve birlikte sorumluluğu avukata işaretleyin: sözleşme bu sorumluluğu işçilere karşı kaldırmaz.
- **Danışmanlık:** çıktıların mülkiyeti ve kullanım hakkı (rehber bölüm 5 madde 12), çıkar çatışması beyanı ve bildirimi.
- **Eğitim:** eğitim materyalinin kullanım hakkı; katılımcı verileri için ayrı veri aktarım protokolü (`/contract-drafting:veri-aktarim-protokolu`).

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- 4857 sayılı İş Kanunu m. 2 (asıl işveren ile alt işveren ilişkisinin tanımı ve koşulları; asıl işveren alt işverenin işçilerine karşı o işyeriyle ilgili yükümlülüklerden alt işverenle birlikte sorumludur; koşullar yoksa ilişki muvazaalı sayılır)
- KVKK m. 9 (yurt dışına aktarım)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Hizmet, Danışmanlık ve Eğitim Sözleşmesi: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Kişisel veri işleniyorsa `/contract-drafting:veri-aktarim-protokolu`; karşı tarafın taslağı geldiyse `/contract-drafting:playbook-inceleme` (hizmet ve eser playbook'u).
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:ingilizce-genel-kosullar

---
name: ingilizce-genel-kosullar
description: >
  Yabancı tedarikçi için İngilizce satınalma genel koşullarını (General Terms and Conditions of
  Purchase) sıfırdan kurar: Türkçe kısa form iskeletle aynı yapı, Türk hukuku ve uyuşmazlık çözümü,
  Incoterms 2020, dövizli alacakta güncel gösterge oran (Term SOFR, €STR) artı marj, yaptırım ve
  ihracat kontrolü. İki dilli istenirse iki sütun. Örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# İngilizce Genel Koşullar Hazırlama (Yabancı Tedarikçi)

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** alıcı mı, yabancı tedarikçi mi? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Dil:** yalnız İngilizce mi, iki dilli mi? İki dilliyse hangi metnin esas olduğu yazılır.
3. **Hukuk ve uyuşmazlık:** Türk hukuku mu; Türk mahkemesi, ISTAC ya da başka tahkim mi?
4. **Para birimi ve gecikme faizi;** yaptırım riski olan ülke ya da kişi var mı?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 2'deki kısa form sırası, İngilizce; tanımlı terimler Türkçe metinle aynı. Türe özgü maddeler (rehber bölüm 8 madde 3.i):

- **Hukuk seçimi:** açık yazılır; seçim yapılmazsa sözleşme en sıkı ilişkili hukuka, ticari sözleşmede çoğunlukla karakteristik edim borçlusunun (satıcının) işyeri hukukuna tabi olur (ADIM 3).
- **Yetki ve tahkim:** yabancı mahkeme seçimi yazılı delille ispat edilmelidir; tenfiz ve karşı taraf ülkesi için `/commercial-legal:governing-law-review`.
- **Faiz:** dövizli alacakta güncel gösterge oran artı marj; LIBOR yazılmaz.
- **Yaptırım ve ihracat kontrolü:** rehber bölüm 5 madde 7 ve `references/yaptirim-tarama-rehberi.md`.
- **Vergi:** yurt dışı ödemede stopaj ve çifte vergilendirmeyi önleme anlaşması `tax-legal` ile ayrıca incelenir; oran teyit edilmeden yazılmaz.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- 5718 sayılı MÖHUK m. 24 (sözleşmeden doğan borç ilişkisi tarafların açıkça seçtiği hukuka tabidir; seçim yoksa en sıkı ilişkili hukuk, ticari sözleşmede karakteristik edim borçlusunun işyeri hukuku)
- 5718 sayılı MÖHUK m. 47 (münhasır yetki dışında, yabancılık unsuru taşıyan borç ilişkisinde yabancı mahkeme yetkisi kararlaştırılabilir; anlaşma yazılı delille ispat edilmelidir)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# İngilizce Genel Koşullar (Yabancı Tedarikçi): [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Türkçe karşılığı için `/contract-drafting:satinalma-sartnamesi`.
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:mal-alim-sozlesmesi

---
name: mal-alim-sozlesmesi
description: >
  Mal alımı ya da çerçeve tedarik sözleşmesini sıfırdan kurar: uzun form iskelet, çerçeve ile
  sipariş emri ilişkisi, teslim yeri ve Incoterms 2020 kuralı, muayene ve kabul, ayıp ihbarı,
  mülkiyet ve hasarın geçişi, sipariş bazında fesih; standart kloz seti ve ticari karar listesiyle.
  Örneklerden yararlanır, birebir kopyalamaz; açık değerler [DOLDUR] ile işaretli, Word'e hazır.
user-invocable: true
---

# Mal Alımı ve Çerçeve Sözleşme Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** alıcı mı, satıcı (tedarikçi) mı? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Yapı:** tek seferlik alım mı, çerçeve sözleşme ve ona bağlı sipariş emirleri mi?
3. **Teslim:** teslim yeri ve Incoterms 2020 kuralı; yurt dışından alımda gümrük ve ithalat işlemleri kimde?
4. **Taraflar tacir mi?** Tacirler arası satışta ayıp ihbarı süreleri kanundan gelir (ADIM 3).
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 1'deki uzun form sırası. Kısa sipariş koşulları isteniyorsa `/contract-drafting:satinalma-sartnamesi`. Türe özgü maddeler (rehber bölüm 8 madde 3.a):

- **Çerçeve ve sipariş emri:** siparişin verilmesi ve teyidi, çerçeve hükümlerinin her siparişe uygulanması, sipariş ile çerçeve arasındaki öncelik.
- **Teslim:** teslim yeri, Incoterms 2020 kuralı ve adres; kısmi teslimin kabul edilip edilmeyeceği.
- **Muayene ve kabul:** muayene yeri, süresi ve yöntemi, kabul tutanağı, ayıp ihbarının süresi ve biçimi.
- **Mülkiyet ve hasarın geçişi:** Incoterms kuralıyla aynı ana bağlanır; iki hüküm arasında çelişki bırakılmaz.
- **Fesih:** tek siparişin feshi ile çerçevenin bütününün feshi ayrı yazılır.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.
3. Ayıp ihbarı süresini sözleşmede açıkça yazın; tacirler arası satışta kanuni süreyi (ADIM 3) çekmeden süre yazmayın.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- TBK m. 208 (yarar ve hasar: kural olarak taşınırda zilyetliğin devrine kadar satıcıda; satılan alıcının isteğiyle ifa yerinden başka yere gönderilirse taşıyıcıya teslimle alıcıya geçer)
- TBK m. 223 (alıcı satılanı imkân bulur bulmaz gözden geçirir ve ayıbı uygun sürede bildirir; bildirmezse kabul etmiş sayılır)
- TTK m. 23/1-c (tacirler arası satışta açık ayıp iki gün içinde, açık olmayan ayıp teslimden sonra sekiz gün içinde incelenip ihbar edilir)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Mal Alımı ve Çerçeve Sözleşme: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Kısa sipariş koşulları için `/contract-drafting:satinalma-sartnamesi`; yabancı tedarikçi için `/contract-drafting:ingilizce-genel-kosullar`.
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:mutabakat-zapti

---
name: mutabakat-zapti
description: >
  İş birliği sözleşmesi ya da mutabakat zaptını (MoU, niyet mektubu) sıfırdan kurar: amaç ve görevler;
  bağlayıcı hükümlerin (gizlilik, fikri mülkiyet, uygulanacak hukuk, masraflar) bağlayıcı olmayan
  ticari niyet beyanlarından açıkça ayrılması; temsilcilik ilişkisinin bulunmaması; devir yasağı.
  Ön sözleşme riskini işaretler; örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# İş Birliği Sözleşmesi ve Mutabakat Zaptı Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** hangi tarafı temsil ediyoruz, yoksa iki tarafa tarafsız bir metin mi? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Nitelik:** bağlayıcı bir iş birliği mi, yalnız niyet beyanı mı?
3. **İleride kurulacak sözleşme:** ne olacak (pay devri, taşınmaz satışı, ortak girişim)? Kanunda şekle bağlı mı?
4. **Münhasırlık ve görüşme süresi** olacak mı?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Kısa yapı: taraflar, amaç, görevler, bağlayıcı olmayan ticari niyetler, bağlayıcı hükümler, süre ve sona erme, imza. Türe özgü maddeler (rehber bölüm 8 madde 3.f):

- **Bağlayıcılık:** bağlayıcı ve bağlayıcı olmayan bölümler ayrı başlıklarla yazılır; bağlayıcı maddeler tek tek sayılır.
- **Ön sözleşme riski:** metin ileride kurulacak sözleşmenin esaslı noktalarını içeriyorsa ön sözleşme sayılabilir; o sözleşme şekle bağlıysa ön sözleşme de aynı şekle bağlıdır (ADIM 3). Bunu avukata işaretleyin.
- **İlişkinin niteliği:** temsilcilik, ortaklık ya da iş ortaklığı kurulmadığı; devir yasağı; her tarafın kendi masrafı.
- **Süre:** kendiliğinden sona erme tarihi ve sona ermeden sonra süren hükümler (gizlilik).

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- TBK m. 29 (ileride bir sözleşme kurulmasına ilişkin sözleşmeler geçerlidir; kanundaki istisnalar dışında ön sözleşmenin geçerliliği ileride kurulacak sözleşmenin şekline bağlıdır)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# İş Birliği Sözleşmesi ve Mutabakat Zaptı: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Görüşmeler ilerlerse asıl sözleşme için ilgili türün akışı; ortak girişimde `/energy-finance:jv-agreement-review`.
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:playbook-inceleme

---
name: playbook-inceleme
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
> Playbook bir başlangıç noktasıdır; büronun kendi pozisyonu `company-profile.md` ya da kullanıcının yazdığı tercihlerle değişir.

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
- Redline için: `/contract-drafting:redline-contract` ya da ArthurMask'in revize aracı (izli değişiklik).
- Karşı tarafa özet için: `/commercial-legal:stakeholder-summary`.
```

## Not
- Claude for Word'de çalışırken önerileri belgeye **izli değişiklik** olarak işleyin; her değişikliğe tek cümlelik gerekçe yazın.
- Playbook'taki pozisyonlar varsayılandır; büro profili ya da kullanıcı tercihi farklıysa onu uygulayın ve farkı özette söyleyin.

---

## /contract-drafting:redline-contract

---
name: redline-contract
description: >
  Yüklenen sözleşmeyi inceleme bulgularına göre REDLINE'la — değişiklikleri belgeye
  ekleme/silme + comment olarak işler, 3 çıktı formundan birinde teslim eder.
  commercial-legal inceleme akışıyla bütünleşir (vendor/NDA/SaaS/governing-law).
  Claude.ai Projects: markdown redline görünümü; Claude Code: gerçek .docx tracked-changes.
  TBK/TTK + standart (EPC/PPA/vendor/SHA) fallback pozisyonları.
user-invocable: true
---

# Sözleşme Redline (incele → belgeye uygula)

> Bu skill **bulguları belgeye uygular**. Henüz inceleme yapılmadıysa önce `/commercial-legal:review` (veya ilgili review skill'i) çalıştır; sonra bulguları buraya getir. Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı ile imzalanır.

## ADIM 0 — Girdi & ortam & form

1. **Belge var mı?** Kullanıcı sözleşme metnini yapıştırsın/yüklesin. "Okuma kapsamı"nı belirt; tamamını okumadıysan söyle.
2. **Bizim kağıt mı, karşı tarafın kağıdı mı?** (redline yönü/agresifliği değişir)
3. **Ortam:** Claude.ai Projects → **markdown redline**; Claude Code → **gerçek .docx tracked-changes** (python-docx) opsiyonu.
4. **Çıktı formu (sor):**
   - (a) **Redline görünümü** — madde içinde ~~silinen~~ / **eklenen** + comment dipnotları
   - (b) **Temiz revize + değişiklik/comment listesi**
   - (c) **Yapılandırılmış tablo** — `madde | mevcut | önerilen | gerekçe | severity`

## ADIM 1 — Bulguları topla / üret

Inceleme bulgusu varsa al; yoksa playbook'a göre çıkar (sözleşme tipini tespit et → `references/` + `commercial-legal` profili + `company-profile.md` standart pozisyonları). Her bulgu için:
- **Sorun** (kloz + neden) · **Severity** (🔴🟠🟡🟢) · **Önerilen redline** (somut metin) · **Fallback** ("tercih X; kabul edilmezse asgari Y") · **Hukuki dayanak** (çekilmiş madde, `[ArthurLegal TR — kanun m. X — GG.AA.YYYY]`; önerilen redline metnine yazılan madde numarası da belge-turet ADIM 2'deki doğrulama kapısından geçer, çekilemiyorsa redline numarasız yazılır).

**Standart kontrol listesi (enerji sözleşmesi):**
- Mücbir sebep + aşırı ifa güçlüğü (TBK m.136/138) — şebeke kısıtı, mevzuat değişikliği, kuraklık (HES)
- Sınırlı sorumluluk / cezai şart (TBK m.179-182 — fahiş ceza tenkisi)
- Yaptırım & uyum klozu (OFAC/AB/BM/OFSI + **uluslararası finans kuruluşu dışlama listesi**) — `references/yaptirim-tarama-rehberi.md`
- Uyuşmazlık & uygulanacak hukuk (Türk mah. vs ICC/LCIA) — `/commercial-legal:governing-law-review`
- **EPDK lisans/pay devri ön-onayı** (6446) — kontrol değişikliği klozu
- KVKK (6698) veri işleme/aktarım · gizlilik · fikri mülkiyet
- Damga vergisi / vergi gross-up · ödeme/teminat (akreditif, teminat mektubu)
- Devir/temlik · değişiklik (tadil) · fesih · süre/yenileme

## ADIM 2 — Redline'ı üret (seçilen form)

**Form (a) — Redline görünümü (Projects varsayılanı):**
```markdown
**Madde 12.3 (Mücbir Sebep)**
Taraflar, ~~savaş, grev ve doğal afet~~ **mücbir sebep hâllerinde (TBK m.136 anlamında, şebeke
operatörü kaynaklı kesinti ve mevzuat değişikliği dâhil)** edimlerini ~~7 gün~~ **30 gün** içinde
yerine getiremezse...
> 💬 [Av. — 🟠] Mücbir sebep tanımı dar; şirket için şebeke/regülasyon riskini kapsamalı.
>     Tercih: TBK m.136 atfı + açık liste. Kabul edilmezse asgari: "şebeke kesintisi" eklensin.
```

**Form (b) — Temiz revize + liste:** temiz metin (değişiklikler uygulanmış) + ayrı tablo:
```markdown
| # | Madde | Değişiklik | Gerekçe | Severity |
|---|---|---|---|---|
| 1 | 12.3 Mücbir sebep | tanım genişletildi + 30 gün | şebeke/regülasyon riski | 🟠 |
```

**Form (c) — Yapılandırılmış tablo:** `madde | mevcut | önerilen | gerekçe | severity` (uygulamayı kullanıcı yapar).

> **Claude Code yolu:** python-docx ile `w:del`/`w:ins` (yazar="ArthurLegal", tarih) + `w:comment` üretip `<dosya>_redline.docx` döndürülebilir. Projects'te dosya oluşturma açıksa aynı yol izlenir; kapalıysa metin redline ([silinen: ...] / [eklenen: ...]) + "Word'de Değişiklikleri İzle açıkken uygulayın" notu.

## ADIM 3 — Çıktı

```markdown
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN İMZALANMAZ

# Redline — [sözleşme adı] — [karşı taraf]

## ⚠️ İnceleyen notu
- **Belge / okuma kapsamı:** [tip, N sayfa okundu]
- **Kağıt:** bizim / karşı taraf · **Form:** (a)/(b)/(c) · **Ortam:** Projects/Code
- **Değişiklik sayısı:** 🔴 N · 🟠 N · 🟡 N · 🟢 N
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [✓/✗]
- **Madde kontrolü:** [redline, yorum ve gerekçedeki her madde atfı → okundu ve eşleşti / çekilemedi, çıkarıldı]
- **Onay:** Baş Hukuk Müşaviri + dış vekil şart

[seçilen formda redline]

## Sonraki adımlar
> 1. **Eksik inceleme** — `/commercial-legal:review` ile derinleştir
> 2. **Governing law / yaptırım** — `/commercial-legal:governing-law-review`
> 3. **Karşı teklif turu** — kabul/ret sonrası `/contract-drafting:versiyon-karsilastir`
> 4. **Temiz nüsha** — kabul edilen değişikliklerle final taslak
> 5. **Başka**

**One question I'd ask:** [örn. "Bu karşı tarafla ilişki sürüyor mu? Sürüyorsa redline tonu agresif değil 'işbirlikçi-ama-korumalı' olmalı."]
```

---

## /contract-drafting:satinalma-sartnamesi

---
name: satinalma-sartnamesi
description: >
  Sipariş emriyle kurulan kısa form satınalma şartnamesini ya da sipariş genel koşullarını (mal ya da
  hizmet) sıfırdan kurar: fiyat ve ödeme, teslimat ya da hizmetin tamamlanması, muayene ve testler,
  garanti, askıya alma, fesih, tazmin, mülkiyet ve riskin geçişi, sigorta, şartname ile sipariş
  emri arasındaki öncelik. Genel işlem koşulu kurallarına göre kurulur; örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Satınalma Şartnamesi ve Sipariş Genel Koşulları Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** alıcı (şartnameyi koyan) mı, tedarikçi mi? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Kapsam:** mal mı, hizmet mi, ikisi mi?
3. **Tedarikçi:** yerli mi, yabancı mı? Yabancıysa `/contract-drafting:ingilizce-genel-kosullar`.
4. **Kabul yolu:** sipariş emrinde açık atıf, imza ya da elektronik onay?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 2'deki kısa form sırası. Türe özgü maddeler (rehber bölüm 8 madde 3.a ve b):

- **Öncelik:** şartname ile sipariş emri arasındaki öncelik yazılır.
- **Hizmet içeriyorsa:** bağımsız işveren ve iş sağlığı ve güvenliği maddeleri eklenir.
- **Genel işlem koşulu:** şartname tek taraflı ve çok sayıda tedarikçi için hazırlandığından genel işlem koşuludur. Karşı tarafa varlığı açıkça bildirilmeli, içeriğini öğrenme imkânı verilmeli ve kabul ettirilmelidir (sipariş emrinde açık atıf, şartnamenin eklenmesi ya da erişim bağlantısı); alıcıya tek yanlı değiştirme yetkisi veren kayıt yazılmaz.
- **Genel hükümler:** rehber bölüm 5'teki setin kısa hâlleri.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- TBK m. 20 (genel işlem koşulunun tanımı)
- TBK m. 21 (karşı tarafa açıkça bilgi verilip içeriğini öğrenme imkânı sağlanmadıkça ve kabul edilmedikçe aleyhe koşul yazılmamış sayılır)
- TBK m. 24 (düzenleyene tek yanlı değiştirme yetkisi veren kayıt yazılmamış sayılır)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Satınalma Şartnamesi ve Sipariş Genel Koşulları: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Uzun form gerekiyorsa `/contract-drafting:mal-alim-sozlesmesi` ya da `/contract-drafting:hizmet-sozlesmesi`.
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:sponsorluk-sozlesmesi

---
name: sponsorluk-sozlesmesi
description: >
  Sponsorluk sözleşmesini sıfırdan kurar: sponsorluk bedeli ve aşamalı ödeme, karşı edimler
  (görünürlük, logo ve marka kullanımının sınırları), münhasırlık, etkinliğin iptali ya da
  ertelenmesinde bedelin akıbeti, itibar zedeleyici davranışta fesih. Standart kloz seti ve karar
  listesiyle; örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Sponsorluk Sözleşmesi Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** sponsor mu, sponsorluk alan (etkinlik, kulüp, sporcu, kurum) mı? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Konu:** etkinlik, kulüp ya da sporcu, yayın, kurum?
3. **Bedel:** nakit mi, ayni mi (ürün, hizmet); aşamalara bağlı mı?
4. **Münhasırlık:** aynı sektörden başka sponsor olmaması istenecek mi?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 1'deki uzun form sırası; sponsorluk kanunda düzenlenmiş bir sözleşme türü olmadığı için edimler ayrıntılı yazılır. Türe özgü maddeler (rehber bölüm 8 madde 3.e):

- **Bedel ve ödeme:** aşamalar ve her aşamanın karşı edime bağlanması.
- **Karşı edimler:** görünürlük listesi, yerleri ve ölçüleri, raporlama.
- **Logo ve marka kullanımı:** kapsam, süre, onay süreci, sözleşme bitince kullanımın sona ermesi.
- **İptal ve erteleme:** bedelin iadesi, mahsubu ya da yeni tarihe aktarılması; mücbir sebeple ilişkisi.
- **İtibar:** itibar zedeleyici davranışta fesih ve sonuçları, iki taraf için de.
- **Görüntü ve kişisel veri:** katılımcı ve sporcu görüntüsünün kullanımı için izinler.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.
3. Sponsorluk harcamasının vergi durumu ve damga vergisi `tax-legal` ile ayrıca incelenir (rehber bölüm 5 madde 4).

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- Bu türün kendine özgü kanun maddesi yoktur; genel hükümler rehber bölüm 5'teki gibi çekilir: TBK m. 136 ve 138 (imkânsızlık ve uyarlama), TBK m. 179 ile 182 (ceza koşulu)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Sponsorluk Sözleşmesi: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Marka lisansı geniş ya da süresizse ayrı lisans sözleşmesi önerin.
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:tadil-protokol

---
name: tadil-protokol
description: >
  Ana sözleşmeye bağlı EK PROTOKOL / TADİL / SÜRE UZATIMI metni üretir — ana sözleşmeye
  atıf, "X maddesi aşağıdaki şekilde değiştirilmiştir" formatı, yürürlük, değiştirilmeyen
  hükümlerin saklılığı (severability), damga vergisi, imza. TBK tadil disiplini.
  Örnek: EPC süre uzatımı/iş artışı, PPA fiyat revizyonu, kredi tadili, SHA değişiklik.
user-invocable: true
---

# Tadil / Ek Protokol / Süre Uzatımı Üretimi

> Mevcut bir sözleşmeyi **değiştiren** belgeyi üretir (yeni sözleşme değil — `belge-turet` o iş için). Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı; yüksek tutar/stratejik → Genel Müdür.

## ADIM 0 — Girdi
1. **Ana sözleşme** — kullanıcı yapıştırsın/yüklesin (en azından değişen maddeler + taraflar + tarih).
2. **İstenen değişiklik** — ne değişiyor? (süre, bedel/fiyat, kapsam/iş artışı, taraf, teminat, fesih...).
3. **Tip:** süre uzatım · fiyat/bedel revizyonu · iş artışı/azalışı · taraf değişikliği (devir) · genel tadil.

## ADIM 1 — Tadil disiplini (kritik)

- **Şekil:** Ana sözleşme hangi şekilde yapıldıysa tadil de aynı şekilde (TBK m.13 — yazılı sözleşmenin değişikliği yazılı). EPDK/kamu onayına tabi sözleşmede onay şartı.
- **Atıf:** Ana sözleşmeyi tarih/no ile tanımla ("Ana Sözleşme").
- **Değişiklik formatı:** "Ana Sözleşme'nin [N] maddesi aşağıdaki şekilde **değiştirilmiştir**" / "**eklenmiştir**" / "**yürürlükten kaldırılmıştır**" — eski + yeni metni net ver.
- **Saklılık:** "Değiştirilmeyen tüm hükümler aynen yürürlüktedir."
- **Yürürlük:** imza/tarih; geriye etki isteniyorsa açıkça yaz.
- **Damga vergisi:** tadil ayrı damga doğurabilir (DVK — değişen tutar üzerinden) → `[DOLDUR/doğrulayın]`.
- **Sektörel özel:** süre uzatımı mücbir sebebe dayanıyorsa TBK m.136 gerekçesi; **EPDK lisans şartlarını etkiliyorsa** ön-onay; **SHA tadili** ise reserved matters + ortak/finansör onayı; **kredi tadili** ise finansör covenant/onay.
- **Madde doğrulama kapısı:** tadil metnine, gerekçesine ve eski/yeni metin karşılaştırmasına yazılan her kanun maddesi `/contract-drafting:belge-turet` ADIM 2'deki kapıdan geçer; ana sözleşmedeki bir madde atfına tadilde dayanılıyorsa o da çekilir.

## ADIM 2 — Taslak

```markdown
[ANA SÖZLEŞME ADI] – [TADİL / EK PROTOKOL No: N]

TARAFLAR : [Müvekkil / Şirket] ([VKN/adres]) — [Karşı Taraf]
ANA SÖZ. : GG.AA.YYYY tarihli [ad] ("Ana Sözleşme")
KONU     : Ana Sözleşme'nin aşağıdaki maddelerinin tadili / [süre uzatımı] amacıyla.

MADDE 1 — [Değişiklik]
  Ana Sözleşme'nin [N]. maddesi aşağıdaki şekilde değiştirilmiştir:
  "[yeni madde metni]"
  (Eski metin: "[eski metin]" — kayıt için)

MADDE 2 — [varsa ek değişiklik]

MADDE 3 — SAKLILIK
  İşbu [Protokol/Tadil] ile değiştirilmeyen Ana Sözleşme hükümleri aynen yürürlüktedir.

MADDE 4 — YÜRÜRLÜK VE DAMGA
  Bu belge imza tarihinde yürürlüğe girer; Ana Sözleşme'nin ayrılmaz ekidir.
  Damga vergisi [DOLDUR — DVK]. [Gerekiyorsa: EPDK/Kurul onayı şartı.]

TARİH / İMZALAR: [Müvekkil / Şirket] ([imza yetkilisi]) — [Karşı Taraf]
```

## Çıktı
```markdown
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN İMZALANMAZ

# [Tadil / Ek Protokol] — [ana sözleşme] — No: [N]

## ⚠️ İnceleyen notu
- **Ana sözleşme:** [ad, tarih] · **Tadil tipi:** [...]
- **Değişen madde sayısı:** N
- **Onay/şart tetikleyici:** [EPDK ön-onay / SHA reserved matter / finansör covenant / damga — varsa]
- **Madde kontrolü:** [tadil metnindeki her madde atfı → okundu ve eşleşti / çekilemedi, gövdeden çıkarıldı]
- **Onay:** Baş Hukuk Müşaviri (+ Genel Müdür yüksek tutarda) şart

[taslak]

## Sonraki adımlar
> 1. **Onay/şart kontrolü** — EPDK / SHA / finansör tetiklendiyse ilgili süreç
> 2. **Redline** — `/contract-drafting:redline-contract` ile son kontrol
> 3. **Damga vergisi** — DVK hesabı (`tax-legal` · `references/damga-vergisi-rehberi.md`)
> 4. **Başka**

**One question I'd ask:** [örn. "Bu tadil tek seferlik mi yoksa ana sözleşmenin dengesini kalıcı değiştiriyor mu? Kalıcıysa yan etkileri (fiyat, teminat, fesih) de gözden geçirmeliyiz."]
```

---

## /contract-drafting:tasima-sozlesmesi

---
name: tasima-sozlesmesi
description: >
  Karayolu yük taşıma sözleşmesini sıfırdan kurar: sözleşme belgeleri ve öncelik, taşıma talebi
  ve araç tahsisi, yükleme ve teslim süreleri, taşıyıcının personel ve araç yükümlülükleri, kayıt
  ve raporlar, sağlık, emniyet ve çevre, teminat, ceza koşulu tablosu, taşıyıcının bağımsızlığı.
  Taşıyıcının sorumluluğu ve sınırları TTK'dan çekilerek yazılır; örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Karayolu Taşıma Sözleşmesi Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** gönderen (yük sahibi) mi, taşıyıcı mı? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Kapsam:** yurt içi mi, uluslararası mı? Uluslararası karayolu taşımasında uluslararası sözleşmeler (CMR) uygulanabilir; avukata işaretleyin.
3. **Yük:** tehlikeli madde ya da özel koşul (soğuk zincir, ağır yük) var mı?
4. **Yapı:** tek sefer mi, çerçeve sözleşme ve taşıma talepleri mi?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 1'deki uzun form sırası. Türe özgü maddeler (rehber bölüm 8 madde 3.d):

- **Belgeler ve öncelik:** sözleşme, ekler ve taşıma talepleri arasındaki öncelik.
- **Taşıma talebi ve araç tahsisi:** talep yolu, tahsis süresi, araç uygun değilse sonuç.
- **Süreler:** yükleme ve teslim süreleri, gecikmenin ölçülmesi.
- **Taşıyıcının yükümlülükleri:** personel, araç ve belgeler, kayıt ve raporlar, sağlık, emniyet ve çevre kuralları.
- **Sorumluluk:** taşıyıcının zıya, hasar ve gecikmeden sorumluluğu ve kanuni sınırları (ADIM 3). Sınırı değiştiren, kaldıran ya da değer beyanına bağlayan hüküm yazılacaksa bunun mümkün olup olmadığı TTK'nın taşıma hükümleri çekilerek kontrol edilir.
- **Teminat ve ceza koşulu tablosu; taşıyıcının bağımsızlığı** (personeli üzerinde yönetim ve sorumluluk taşıyıcıdadır).

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- TTK m. 850 (taşıyıcı eşyayı varma yerine götürüp gönderilene teslim etmeyi borçlanır; taşıma işleri ticari işletme faaliyetidir)
- TTK m. 875 (taşıyıcı eşyanın teslim alınmasından teslimine kadar zıya, hasar ve teslimdeki gecikmeden doğan zarardan sorumludur)
- TTK m. 882 (sorumluluk sınırları: zıya ya da hasarda gönderinin net olmayan ağırlığının kilogramı başına 8,33 Özel Çekme Hakkı; taşıma süresinin aşılmasında taşıma ücretinin üç katı)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Karayolu Taşıma Sözleşmesi: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Yük sigortası ve rücu için sigorta poliçesinin koşullarını ayrıca isteyin.
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:veri-aktarim-protokolu

---
name: veri-aktarim-protokolu
description: >
  Ana sözleşmeye ek kişisel veri aktarım protokolünü sıfırdan kurar: tarafların sıfatları (veri
  sorumlusu, veri işleyen), veri kategorileri ve amaç, aktarım, saklama ve imha, ilgili kişi
  başvuruları, veri güvenliği ve ihlal bildirimi, denetim, sorumluluk; yurt dışı aktarımda KVKK m. 9
  yolu. Örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Veri Aktarım Protokolü Hazırlama (Sözleşme Eki)

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/contract-drafting:belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `company-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** veri sorumlusu mu, veri işleyen mi, ortak veri sorumluları mı? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Ana sözleşme:** hangi sözleşmeye ek, veri hangi iş için aktarılıyor?
3. **Veri:** kategoriler ve ilgili kişi grupları; özel nitelikli kişisel veri var mı?
4. **Yurt dışı:** aktarım var mı; varsa ülke ve yol (yeterlilik kararı, uygun güvence, arızi aktarım)?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Kısa yapı: taraflar ve sıfatları, konu ve amaç, veri kategorileri, aktarım yolu, işleme talimatı, saklama ve imha, ilgili kişi başvuruları, veri güvenliği ve ihlal bildirimi, alt işleyen, denetim, sorumluluk, süre. Türe özgü maddeler (rehber bölüm 8 madde 3.h):

- **Saklama ve imha:** süre; sözleşme bitince iade, silme, yok etme ya da anonimleştirme ve bunun teyidi.
- **Veri güvenliği ve ihlal:** teknik ve idari tedbirler; veri işleyenin veri sorumlusuna bildirim süresi (rehber bölüm 5 madde 5), veri sorumlusunun ilgiliye ve Kurula bildirimi.
- **Yurt dışı aktarım:** yol açıkça yazılır; standart sözleşme kullanılıyorsa imzadan sonra Kuruma bildirim yükümlülüğü ve süresi (ADIM 3).
- **Alt işleyen ve denetim:** onay düzeni, denetim hakkı, maliyet.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.
3. Karşı tarafın veri işleme sözleşmesi geldiyse önce `/privacy-legal:dpa-review` ile inceleyin.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- KVKK m. 7 (işlenmesini gerektiren sebepler ortadan kalkınca kişisel veri silinir, yok edilir ya da anonim hâle getirilir)
- KVKK m. 9 (yurt dışına aktarım: yeterlilik kararı, yoksa uygun güvenceler, o da yoksa arızi hâller; m. 9/5: standart sözleşme imzadan itibaren beş iş günü içinde Kuruma bildirilir)
- KVKK m. 12 (veri güvenliği; başkası adına işlemede veri sorumlusu tedbirlerden o kişiyle müştereken sorumludur; ihlal en kısa sürede ilgiliye ve Kurula bildirilir)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Veri Aktarım Protokolü (Sözleşme Eki): [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Ana sözleşmenin KVKK maddesini bu protokole bağlayın (rehber bölüm 5 madde 5).
- Karşı taraf taslağı döndürünce `/contract-drafting:versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/contract-drafting:redline-contract`.
```

---

## /contract-drafting:versiyon-karsilastir

---
name: versiyon-karsilastir
description: >
  İki sözleşme versiyonunu (v1 ↔ v2 / bizim taslak ↔ karşı taraf revizesi) karşılaştırır —
  madde-madde track-changes/diff görünümü + her değişikliğin hukuki/ticari ETKİSİ +
  risk flag (karşı taraf ne kazandı/biz ne kaybettik). Müzakere turları ve "sessiz
  değişiklik" yakalama için. Claude.ai Projects: markdown diff; Claude Code: .docx compare.
user-invocable: true
---

# Versiyon Karşılaştırma (redline diff)

> Müzakere turunda **karşı tarafın neyi değiştirdiğini** yakalar — özellikle **sessizce eklenen/çıkarılan** klozları. Her çıktı **TASLAK**.

## ADIM 0 — Girdi
1. **İki versiyon** — v1 (örn. bizim son taslak) + v2 (örn. karşı taraf revizesi). Kullanıcı ikisini de yapıştırsın/yüklesin.
2. **Hangisi referans?** (genelde bizim son kabul ettiğimiz = baz).
3. Okuma kapsamını belirt; her ikisini de tam okuyamadıysan söyle.

## ADIM 1 — Madde eşle & diff çıkar

- Maddeleri başlık/numara ile eşle (numaralandırma kaymışsa içerikle eşle).
- Her madde için: **değişmedi / değişti / eklendi / silindi / taşındı**.
- Metin düzeyinde fark: ~~silinen~~ / **eklenen**.
- ⚠️ **Sessiz değişiklik avı:** tanım değişikliği, "shall→may", süre/eşik/tutar oynaması, istisna ekleme, sorumluluk tavanı, fesih kolaylaştırma, yetki/hukuk değişimi — küçük ama kritik.

## ADIM 2 — Etki & risk

Her değişiklik için:
- **Ne değişti** (kısa) · **Lehimize / aleyhimize / nötr** · **Severity** (🔴🟠🟡🟢) · **Etki** (hukuki/ticari sonuç) · **Aksiyon** (kabul / karşı-revize / müzakere).
- Emredici hüküm etkisi varsa `[ArthurLegal MCP (`tr_`)]`.

## ADIM 3 — Çıktı

```markdown
TASLAK – HUKUK MÜŞAVİRLİĞİ DAHİLİ

# Versiyon Karşılaştırma — [sözleşme] — v[X] ↔ v[Y]

## ⚠️ İnceleyen notu
- **Versiyonlar / okuma kapsamı:** [v1 tarih, v2 tarih, N sayfa]
- **Toplam değişiklik:** N (lehimize K · aleyhimize L · nötr M)
- **Kritik (🔴/🟠):** N adet
- **Onay:** Baş Hukuk Müşaviri (önemli değişiklik varsa)

## Özet — karşı taraf bu turda ne yaptı?
[2-4 cümle: en önemli hamleler + sessiz değişiklikler]

## Madde-madde diff
| # | Madde | Değişiklik (~~sil~~/**ekle**) | Yön | Severity | Etki | Aksiyon |
|---|---|---|---|---|---|---|
| 1 | 8.2 Sorumluluk tavanı | ~~%100~~ **%50 sözleşme bedeli** | aleyhe | 🔴 | tazminat hakkı yarıya iner | karşı-revize |

## Dikkat — sessiz/kritik değişiklikler
[🔴/🟠 maddelerin vurgusu]

## Sonraki adımlar
> 1. **Karşı-revize üret** — `/contract-drafting:redline-contract` (aleyhe maddelere)
> 2. **Müzakere notu** — iş birimi/Genel Müdür için özet
> 3. **Governing law değiştiyse** — `/commercial-legal:governing-law-review`
> 4. **Başka**

**One question I'd ask:** [örn. "Karşı taraf bu turda büyük taviz mi verdi yoksa küçük kazanımları paketleyip mi geçirdi? Cevap, kabul/itiraz stratejisini değiştirir."]
```

---
