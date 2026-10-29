---
name: commercial-legal-vendor-agreement-review
description: >
  Referans: gelen tedarikçi/hizmet sözleşmesini `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`
  playbook'una ve Türk hukukunun emredici sınırlarına (TBK m. 115-116
  sorumsuzluk, m. 179-182 cezai şart, TTK m. 1530 ödeme süresi, m. 18/3
  bildirim şekli, FSEK m. 48-52 fikrî haklar, HMK yetki/tahkim) göre inceler;
  sapmaları bulur, riski iki eksende puanlar, yapıştırılmaya hazır redline
  yazar ve doğru onaylayıcıya yönlendirir. Çerçeve hizmet sözleşmesi ya da
  benzeri tespit edildiğinde /arthurlegal:commercial-legal-review tarafından yüklenir.
user-invocable: false
---

# /vendor-agreement-review — Tedarikçi / Hizmet Sözleşmesi İncelemesi

Sözleşmeyi bu ekibin gerçekten kullandığı playbook'a göre oku, sapan her şartı bul ve avukata her biri için ne yapacağını söyle — "gözden geçirilmesi düşünülebilir" değil, somut redline metniyle. Çıktı avukatın tek geçişte işleyebileceği bir nottur: her sorunun ciddiyeti, iş etkisi, önerilen düzeltmesi ve gerekiyorsa eskalasyonu var.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:commercial-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Destination check

Kullanıcı bir hedef söylediyse (kanal, liste, karşı taraf, "herkes") dar gizlilik çevresinde mi diye sor. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD tipi geniş bir belge koruması değildir; karşı tarafa, tedarikçiye ya da şirket geneline giden metin gizliliğini fiilen kaybeder. Çevre dışıysa (a) hukuk için tam sürüm, (b) arındırılmış sürüm ya da (c) ikisini öner. Kanonik kural: `## Shared guardrails → Destination check`.

## Ön koşul: playbook

**Sözleşmeyi okumadan önce eklenti ayarını ve `firm-profile.md`'i oku.** Ayar yoksa ya da yer tutucu taşıyorsa:

> Profilinizi henüz yapılandırmamışsınız — playbook pozisyonlarını, eskalasyonu ve üslubu buradan öğreniyorum.
> - `/arthurlegal:commercial-legal-cold-start-interview` çalıştırın (2 dakika), sonra sizin playbook'unuza göre inceleyeyim.
> - Ya da **"provisional"** deyin; genel varsayılanlarla (Türk hukuku, orta risk iştahı, avukat rolü, playbook yok — yaygın tedarikçi risklerini ilk ilkelerden işaretlerim) incelerim ve her çıktıyı `[PROVISIONAL — profili yapılandırınca size göre ayarlanır]` diye etiketlerim.

**Provisional mod:** Sınırsız sorumluluk, veri ihlali istisnası yokluğu, tavansız tazmin, bildirimsiz otomatik yenileme gibi yaygın riskleri ilk ilkelerden işaretle; inceleyen notunu ve her bulgu bloğunu `[PROVISIONAL]` ile etiketle; sonuna ekle: "Bu, varsayılanlarla yapılmış genel bir çalışmaydı. Kendi playbook'unuz, hukukunuz ve risk iştahınızla çıktı için `/arthurlegal:commercial-legal-cold-start-interview` çalıştırın — 2 dakika."

**Hangi taraftayız?** Karşı taraf mal/hizmet sağlıyorsa alım tarafı; ürününüzü satın alan müşteriyse satış tarafı. Belli değilse (bayilik, ortaklık, gelir paylaşımı) sor: "[[Müvekkil]] bu sözleşmede hangi tarafta — tedarikçi mi, müşteri mi?" Eşleşen bölümü oku (`### Sales-side playbook` / `### Purchasing-side playbook`), çıktıda yaz. `[Not configured]` ise dur, `/arthurlegal:commercial-legal-cold-start-interview --side <side>` öner.

Playbook doğruluğun kaynağıdır: ekibin standart pozisyonları (piyasa standardı değil, *onların* standardı), daha önce kabul ettikleri geri çekilme pozisyonları, asla kabul etmedikleri, kimin neyi onayladığı ve önce bakılacak tek anlaşma bozucu (`#### The one thing`). Sözleşmede anlaşma bozucu varsa notun başında işaretle ve ayrıntılı incelemeyi durdur.

## Akış

### Adım 1: Yönlen

Sözleşmeyi bir kez hızla oku:

| Soru | Cevap |
|---|---|
| Sözleşme türü | Çerçeve hizmet / SaaS / proje (eser) / danışmanlık (vekâlet) / lisans / diğer |
| Biz kimiz | Müşteri / tedarikçi (bu skill genelde müşteri tarafıdır — değilse işaretle) |
| Karşı taraf | Unvan; büyük kurumsal (müzakere etmez) mi, girişim (eder) mi? |
| Taraflar tacir mi | Ticari iş (TTK m. 3) → TTK m. 18/3, 22, 1530, 5/A uygulanır |
| İmza yetkisi | İmza sirküleri / ticaret sicili kaydıyla teyit edildi mi? |
| Bedel | Yıllık / toplam; para birimi (TL / döviz) |
| Süre | Uzunluk, yenileme düzeni |
| Kişisel veri eki | Ekli / bağlantıyla atıf / yok |
| Sipariş formu | Ayrı belge / gövdede |
| Dil | Türkçe / yabancı dil / iki dilli (hangi metin esas) |

**Sözleşmenin niteliği.** Türk hukukunda sonuçlar türe göre değişir: eser sözleşmesinde (TBK m. 470) iş sahibi eser tamamlanmadan, yapılan kısmın karşılığını ödeyip yüklenicinin bütün zararını gidererek sözleşmeyi feshedebilir (TBK m. 484); vekâlet ve kanunda düzenlenmemiş iş görme sözleşmelerinde (TBK m. 502/2) taraflar her zaman sona erdirebilir, uygun olmayan zamanda sona erdiren zararı giderir (TBK m. 512). "Süre bitmeden feshedilemez" kaydının vekâlet niteliğindeki ilişkide geçerliliği **tartışmalı — içtihadı kontrol et**. Niteliği nota yaz.

**Bedel belirsizse dur ve sor.** Çerçeve sözleşme bedeli göstermiyor, sipariş formu gösteriyorsa (tipik), eskalasyon eşiğini uygulamadan önce:

> Çerçeve sözleşme yıllık bedeli göstermiyor; bedel sipariş formunda. Eskalasyon eşiğiniz [matristen X]. Yönlendirmeden önce bedele ihtiyacım var: (1) sipariş formundaki bedeli yapıştırın (tercih), (2) eşiğin altında mı üstünde mi söyleyin — not, bedel görülmeden bu varsayımla yönlendirildiğini yazar, (3) her hâlükârda üst onaylayıcıya yönlendirelim.

Varsayılan bir bedeli sessizce yönlendirmede kullanma.

**Kişisel veri eki bağlantıyla atıfla eklenmişse** ("[URL]'de yer alan veri işleme eki"): ek sözleşmenin parçasıdır ama önünde değildir. Tabloda ve notta açıkça yaz; veri koruma analizinin kısmi olduğunu belirt ve `/arthurlegal:privacy-legal-dpa-review` öner (yüklüyse: "Eki hazır olduğunuzda `/arthurlegal:privacy-legal-dpa-review`'a vereyim mi? Alt işleyen, yurt dışı aktarım ve ihlal bildirimini o yakalar."). Eksik ek ile okunmamış eki ayrı etiketle.

### Adım 2: Anlaşma bozucu kontrolü

`#### The one thing`'i önce kontrol et. Varsa:

```markdown
## ⛔ ANLAŞMA BOZUCU VAR

**Madde [X.X]** [anlaşma bozucu]yu içeriyor. Playbook'a göre kesin hayır. Öneri:
- [ ] İtiraz — [somut alternatif metin] öner
- [ ] Vazgeç — karşı taraf geri adım atmazsa imzalamıyoruz

Aşağıdaki ayrıntılı inceleme bütünlük için verilmiştir; bu çözülmedikçe anlamsızdır.
```

### Adım 3: Madde madde karşılaştırma

Eklenti ayarındaki her playbook kategorisi için karşılık gelen maddeyi bul ve karşılaştır. Her sapma için:

```markdown
### [Madde X.X]: [Konu]

**Playbook:** [standart pozisyon, eklenti ayarından alıntı]
**Sözleşme:**
> "[birebir alıntı]"
**Fark:** [Eksik şart | Standarttan zayıf | Geri çekilme pozisyonundan zayıf | Standart dışı yapı | Kabul edilemez]
**Türk hukuku sınırı:** [varsa — madde atfıyla; yoksa "yok"]
**Hukuki risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
**İş sürtünmesi:** 🔴 Anlaşmayı durdurur | 🟠 Yavaşlatır | 🟡 Kafa karıştırır | 🟢 Görünmez
**Neden önemli:** [bir iki cümle, sade dille]
**Önerilen redline:**
> "[yapıştırılmaya hazır metin]"
**Kabul etmezlerse:** [playbook geri çekilme pozisyonu ya da "[kişi]'ye eskalasyon"]
```

| Düzey | Anlamı |
|---|---|
| 🔴 Kritik | Düzeltilmeden imzalanmaz. "Asla kabul etme" listesinde ya da anlaşma bozucu; ya da Türk hukukunda kesin hükümsüz bir kayda dayanılıyor. |
| 🟠 Yüksek | Güçlü itiraz; geri adım yoksa eskalasyon. Geri çekilme aralığının dışında. |
| 🟡 Orta | İlk turda itiraz; son açık nokta ise kabul. Aralık içinde ama standardın altında. |
| 🟢 Düşük | Not et, sermaye harcama. Playbook'un açıkça tolere ettiği ya da üslup farkı. |

Ciddiyet her zaman eklenti ayarına göre verilir. Bir şart hiçbir pozisyona oturmuyorsa kullanıcıya hangi kovaya ait olduğunu sor ve cevabı ayara kaydetmeyi öner.

#### Türk hukukunun emredici sınırları (her incelemede tara)

| Kloz | Sınır / kural | Dayanak |
|---|---|---|
| Sorumluluk istisnası ve tavan | Ağır kusurdan önceden sorumsuzluk kesin hükümsüz; izinle yürütülen uzmanlık hizmetinde hafif kusurdan sorumsuzluk da kesin hükümsüz. Tavanın da bu sınıra tabi olduğu yerleşik görüştür — doktrini kontrol et | TBK m. 115/1, 115/3 |
| Yardımcı kişiler (alt yüklenici) | Borçlu yardımcısının işi yürütürken verdiği zarardan sorumludur; bu sorumluluk önceden kaldırılabilir, izinle yürütülen uzmanlık hizmetinde kaldırılamaz. Ağır kusur sınırının burada da uygulanıp uygulanmadığı **tartışmalı** | TBK m. 116 |
| "Dolaylı zarar" istisnası | Kanunda "dolaylı / netice zararı" tanımı yok; sorumluluğun kapsamına haksız fiil hükümleri kıyasen uygulanır. Kâr kaybı, veri kaybı, itibar kaybı, üçüncü kişi talepleri gibi kalemleri tek tek say; tanımsız istisnanın kapsamı **tartışmalı** | TBK m. 112, 114 |
| Cezai şart | Seçimlik/ifaya eklenen ceza; zarar olmasa da ödenir; aşan zarar için kusur ispatı; hâkim aşırıyı indirir — tacir borçlu indirim isteyemez | TBK m. 179, 180, 182; TTK m. 22 |
| Ödeme süresi (alım tarafında kritik) | Ticari işletmeler arası mal/hizmet tedarikinde sözleşmesel ödeme süresi en fazla 60 gün; açık anlaşmayla ve alacaklı aleyhine ağır haksızlık yaratmamak kaydıyla daha uzun olabilir, ama alacaklı KOBİ ya da borçlu büyük işletmeyse 60 günü aşamaz. Süresinde ödemeyen ihtarsız temerrüde düşer; gecikme faizini ya da geç ödeme zararından sorumluluğu kaldıran/sınırlayan hüküm geçersiz; oran ve asgari giderimi TCMB her yıl ocakta ilan eder (güncel oranı teyit et) | TTK m. 1530/2, 1530/5-7 |
| Temerrüt ve faiz | Belirli vade gününün geçmesiyle temerrüt; ticari işlerde faiz oranı serbest; sözleşmede oran yoksa kanuni/avans oranı (TCMB'ye bağlı, 3095 m. 1 7589 s.K. ile 2026'da değişti — güncel oranı teyit et). Sözleşmesel temerrüt faizi sınırının (TBK m. 120/2) tacirler arasında uygulanıp uygulanmadığı **tartışmalı** | TBK m. 117/2, 120; TTK m. 8/1; 3095 m. 1-2 |
| Döviz | "Aynen ödeme" kaydı yoksa TL ile ödenebilir; iki Türkiye yerleşiği arasında döviz bedel için 32 sayılı Karar mevzuatını ayrıca çek | TBK m. 99 |
| Fesih ve temerrüt | İfasına başlanmış sürekli edimli sözleşmede borçlu temerrüdünde alacaklı feshedip erken sona ermeden doğan zararını isteyebilir | TBK m. 126 |
| Fesih / ihtar bildirimi | Tacirler arasında temerrüt, fesih, dönme ihbarları noter, taahhütlü mektup, telgraf ya da güvenli e-imzalı KEP ile | TTK m. 18/3 |
| Mücbir sebep | Kanunda tanım yok: borçlunun sorumlu olmadığı imkânsızlıkta borç sona erer, gecikmeksizin bildirim yükümlülüğü var; öngörülemeyen olağanüstü durumda uyarlama, olmazsa dönme/fesih. Sözleşmede olay listesi, bildirim süresi, askı ve fesih eşiği ara | TBK m. 136, 138 |
| Alacağın devri / sözleşmenin devri | Sözleşmeyle devir yasaklanabilir (yasak içermeyen yazılı borç tanımasına güvenen devralan hariç); devir yazılı. Sözleşmenin devri üç taraflı ya da diğer tarafın önceden izni/onayıyla; devredilen sözleşmenin şekline tabi. "Kontrol değişikliği" kanunda yok — sözleşmede ara | TBK m. 183, 184, 205 |
| Tazmin (indemnity) | Türk hukukunda kanuni karşılığı yok; sözleşmesel tazmin taahhüdü ya da üçüncü kişinin fiilini üstlenme olarak nitelendirilebilir — **tartışmalı**. Kapsam, bildirim süresi, savunmanın yönetimi, sulh yetkisi, tavanla ilişki açık yazılmalı; tazmin edilenin kendi ağır kusurunu kapsayan kayıt TBK m. 115/1 riski taşır | TBK m. 128, 115 |
| Fikrî haklar / teslim edilenler | Bilgisayar programı eserdir. İşçilerin işlerini görürken meydana getirdiği eserdeki haklar işverence kullanılır → hak önce tedarikçide toplanır, müşteriye ancak devirle geçer. Mali hak devri/ruhsatı yazılı olmalı ve haklar ayrı ayrı gösterilmeli; henüz meydana getirilmemiş eser üzerindeki tasarruf batıl, ama devir taahhüdü geçerli → "teslimde devreder ve devri teslim tutanağıyla teyit eder" kurgusu; gelecekteki tüm eserlere ilişkin taahhüt 1 yıl önceden ihbarla feshedilebilir | FSEK m. 2/1-1, 18/2, 48, 50, 52 |
| Zamanaşımı | Genel 10 yıl; dönemsel edimler, vekâlet ve (ağır kusur hariç) eser sözleşmesi alacakları 5 yıl; süreler sözleşmeyle değiştirilemez | TBK m. 146, 147, 148 |
| Matbu koşullar | Tedarikçinin tek başına hazırlayıp sunduğu koşullar GİK: bilgilendirme + kabul yoksa yazılmamış sayılır, belirsizlik düzenleyen aleyhine, tek yanlı değiştirme yetkisi yazılmamış, dürüstlüğe aykırı aleyhe hüküm konulamaz | TBK m. 20-25 |
| Yetki / tahkim | Yetki sözleşmesi yalnız tacirler ya da kamu tüzel kişileri arasında, yazılı, ilişki belirli/belirlenebilir; tahkim yazılı. Yabancılık unsuru varsa milletlerarası tahkim (MTK) ve yabancı mahkeme yetkisi (MÖHUK m. 47) → `/arthurlegal:commercial-legal-governing-law-review` | HMK m. 17-18, 407, 412; MTK m. 1-2, 4; MÖHUK m. 24, 47 |
| Arabuluculuk | Ticari davalarda para alacağı, tazminat, itirazın iptali, menfi tespit ve istirdat davalarında dava şartı; "önce müzakere, sonra dava" kaydı bunun yerine geçmez | TTK m. 5/A |
| İmza ve teminat | Güvenli e-imza ıslak imzayla eşdeğer; resmî şekle tabi işlemler ve (banka teminat mektubu ile yerleşik sigorta şirketinin kefalet senedi dışındaki) teminat sözleşmeleri güvenli e-imzayla yapılamaz → ana şirket garantisi/kefalet varsa ıslak imza ve kefalete özgü şekil şartlarını ayrıca çek | 5070 m. 5 |
| Dil | Türk şirketleri Türkiye'deki sözleşmelerini Türkçe tutmakla yükümlü; yabancı şirket için yükümlülük Türk kuruluşlarla ilişkisine özgü. Yalnız yabancı dildeki sözleşmenin sonucu **tartışmalı — içtihadı kontrol et** → iki dilli metin ve "Türkçe metin esastır" ya da en az Türkçe nüsha öner | 805 m. 1-2 |
| Kişisel veri | Veri işleyen sözleşmesi, güvenlik ve yurt dışı aktarım bu skill'in konusu değil | → `/arthurlegal:privacy-legal-dpa-review` |
| Damga vergisi | Oran ve tutar yazma; nüsha, imza yeri, tutarın belirlenmesi (profilde `#### Stamp duty` varsa ona göre) | → `/tax-legal` skill'leri |

#### Sorumluluk tavanı karar prosedürü

**Tavan tutarı tavanın en önemsiz parçasıdır.** Tek satırlık "tavanı playbook'la karşılaştır" yazma; dört boyutu bulguda açıkça yaz:

1. **Doğrudan / dolaylı zarar.** Tavan tüm sorumluluğa mı, yalnız doğrudan zarara mı? Doğrudan zararda 12 aylık tavan + tavansız dolaylı zarar ile 12 aylık toplam tavan bambaşka pozisyonlardır. Türk hukukunda "dolaylı zarar"ın kanuni tanımı olmadığından istisna edilen kalemlerin sayılıp sayılmadığını ayrıca yaz.
2. **Tavan tabanı — birebir alıntıla.** "12 aylık tavan" şunlardan biri olabilir: (a) talepten önceki 12 ayda ödenen bedel, (b) içinde bulunulan 12 aylık dönemde ödenecek bedel, (c) son 12 aylık kullanım bedeli, (d) güncel sipariş formu bedeli, (e) bugüne kadar ödenen toplam. Belirsizse: "Tavan tabanı belirsiz — `[alıntı]` — [X] ya da [Y] anlamına gelebilir. İmzadan önce teyit edin." Döviz cinsinden tavanda kur ve tarih.
3. **Tavan–istisna etkileşimi.** Veri ihlali, fikrî hak tazmini ve gizlilik tavansızsa, gerçek uyuşmazlıklar bakımından sözleşme fiilen tavansızdır. Tavanın ÜSTÜNDE kalanları (istisnalar), ALTINDA kalanları sırala ve tavanlı alanın anlamlı mı göstermelik mi olduğunu yaz. Kast ve ağır kusur her hâlükârda tavan dışında kalır (TBK m. 115/1) — bunu playbook "istisnası" gibi sayma.
4. **Boyut başına playbook.** Profil şu pozisyonları tutmalı: doğrudan tavan (bedelin katı), dolaylı zarar (hariç / tavanlı / tavansız), tavan üstü kabul edilebilir istisnalar, kabul edilebilir tavan tabanı. Tek bir "standart pozisyon" varsa not et: "Playbook'unuzda tek tavan pozisyonu var — doğrudan/dolaylı/istisna/taban olarak bölmeyi düşünün."

#### Yargı çevresi farkı

Playbook tek bir hukuk tercihini her yere uygular; geçerlilik hukuka göre değişir. Sözleşme Türk hukuku dışında bir hukuka tabiyse yukarıdaki tablo o hukuka aktarılamaz. Kural ezberden yazılmaz; araçla çekilir ve `/arthurlegal:commercial-legal-governing-law-review` ile derinleştirilir:
- İngiltere: `uk_search_legislation(query="Unfair Contract Terms Act 1977")` → `uk_get_section`
- Almanya: `de_gesetz_ara` / `de_norm_getir` (ör. BGB § 307 standart şart denetimi)
- AB: `eu_search_eu_law(query="late payment in commercial transactions")`
- Hollanda `nl_`, Polonya `pl_`, Avusturya `at_`, İrlanda `ie_`, Finlandiya `fi_`, İspanya `es_`, Japonya `jp_`, Azerbaycan `az_`
- ABD: yalnız kuruluysa üçüncü taraf CourtListener bağlayıcısı (`courtlistener-rehberi.md`)
- Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

Çektiğin kurala araç etiketi koy (`[ArthurLegal UK — … — GG.AA.YYYY]`); çekemediğini "UYARI: veri çekilemedi, teyidiniz gerekli: <aracın source_url'si ya da resmî giriş sayfası>" diye bırak. Karar Türkiye'de icra edilecekse (yabancı mahkeme ya da hakem kararı) bunu da işaretle → governing-law-review Adım 5.

### Adım 4: Lehte şartlar ve eksikler

**Standardımızdan iyi:** tedarikçinin istediğimizden fazlasını verdiği şartlar — başka yerde taviz gerekirse pazarlık malzemesi.
**Hiç yok:** sık eksikler — devir yasağı, denetim hakkı, mücbir sebep, sigorta, kişisel veri eki, TTK m. 18/3'e uygun tebligat/KEP adresleri, Türkçe esas metin, arabuluculuk ve yetki düzeni.

### Adım 5: Onay yönlendirmesi

Eklenti ayarındaki eskalasyon matrisini sözleşme bedeli, 🔴 sorunların varlığı ve otomatik eskalasyon tetikleyicilerine (sınırsız sorumluluk, fikrî hak devri vb.) karşı kontrol et:

```markdown
## Onay yönlendirmesi

[Bedel / ciddiyet]'e göre bu sözleşme şunları gerektirir:
- [ ] **[İsim/rol]** onayı — [neden]
- [ ] **İş birimi sahibi** onayı — [tartması gereken ticari şart]

**Önerilen sonraki adım:** [Redline'ı karşı tarafa gönder | Cevaptan önce GC'ye eskalasyon | Hukuk cevap vermeden önce X ticari şartı için iş biriminin görüşünü al]
```

**Redline'ı karşı tarafa göndermeden önce** `## Who's using this` oku. Rol avukat değilse:

> Redline göndermek hukuki bir adımdır — karşı taraf her değişikliği müzakere pozisyonumuz sayar. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz bir sayfalık özet: karşı taraf, sözleşme türü, önerilen redline'lar ve arkalarındaki playbook pozisyonları, geri çekilme pozisyonları, paket çıkmadan avukata sorulacaklar. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan geçme.

## Redline inceliği

Redline müzakere belgesidir, yeniden yazım değil. Toptan madde değişikliği "yazdığınızı çöpe attık" der, karşı tarafı tüm maddeyi yeniden okumaya zorlar ve iyi kısımları da atar. En küçük düzeltme: kelime → ifade ("Alıcı tarafından ödenen" → "Alıcı tarafından ödenen ve ödenecek") → alt bent ((a)/(b) ile ayır) → cümle → ancak gerekirse tüm madde; o durumda ileti notunda söyle: "8.2'yi değişiklikler kapsamlı olduğu için işaretlemek yerine yeniden yazdık; farkı birlikte geçebiliriz." Şüphede, daha küçük.

### Adım 6: Notu derle

Başa eklenti ayarı `## Outputs` → üst başlığı koy (role göre). Not ve sözleşme gizli olabilir; çıktı kaynağın statüsünü devralır. Yalnız dar çevrede dağıt; dışa giden teslimlerde (karşı taraf redline'ı, iş birimi özeti) başlığı çıkar. Başlık tek başına koruma yaratmaz.

Uygulanan pozisyonlar eklenti ayarındaki `Governing law and venue`'ya göredir; farklı hukuk ya da hukuk seçimi sorusu varsa notta işaretle.

- **Sessiz tamamlama yok:** Araç gereken bir kural için az sonuç dönerse dur: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle."
- **Kaynak etiketi:** `[ArthurLegal TR — 6098 m. X — GG.AA.YYYY]`, `[web — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`; `doğrula` etiketliler önce kontrol edilir; etiketleri silme.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Tedarikçi Sözleşmesi İncelemesi: [Karşı taraf] [Sözleşme türü]

**İnceleme:** [GG.AA.YYYY]   **Bedel:** [tutar ve para birimi] / [süre]   **Rolümüz:** [Müşteri / Tedarikçi]
**Playbook:** [Satış / Alım tarafı]   **Taraflar:** [tacir–tacir]   **Nitelik:** [eser / vekâlet / karma]   **Hukuk / yargı yeri:** [...]

## ⚠️ İnceleyen notu
- **Kaynaklar:** ArthurLegal MCP (`tr_`) — [madde sayısı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]
- **Eksik belge:** [sipariş formu / veri eki (atıfla, okunmadı) / yok]

## Sonuç
[İki cümle: imzalanabilir mi, önce ne değişmeli?]
**Sorunlar (hukuki risk):** [N]🔴 [N]🟠 [N]🟡 [N]🟢
**Sorunlar (iş sürtünmesi):** [N]🔴 [N]🟠 [N]🟡 [N]🟢
**Onay:** [isim]

## Anlaşma bozucu kontrolü
[✅ Temiz | ⛔ Var — yukarıda]

## Ciddiyete göre sorunlar
[Adım 3 blokları, Kritik → Düşük]

## Lehte şartlar
## Eksik hükümler
## Onay yönlendirmesi
## Redline paketi
[İstenirse: tüm değişiklikler için işaretlemeye hazır toplu metin — iç gerekçe olmadan]
```

## Entegrasyonlar

**[CLM]** bağlıysa: karşı tarafla önceki sözleşmelere bak ("geçen sefer 24 aylık tavan verdik"); bu türe uyan iş akışı şablonunu çek; not ekli ve onaylayıcıları atanmış kayıt aç.

**E-imza (DocuSign vb.)** bağlıysa ve sözleşme imzaya hazırsa zarf oluşturmayı ve imzacıları matris sırasına göre yönlendirmeyi öner. Açık talimat olmadan hiçbir şeyi imzaya gönderme; "imzaya hazır" kararı avukatındır. Platformun imzası güvenli e-imza değilse (5070 m. 5) bunu ve teminat sözleşmesi varsa ıslak imza gereğini not et.

**Zarf oluşturmadan ya da karşı imzaya yönlendirmeden önce** `## Who's using this` oku. Rol avukat değilse:

> Bu adımın hukuki sonucu var: imza şirketi sözleşmenin tamamına bağlar. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: karşı taraf, bedel, bulunan sorunlar ve nasıl çözüldükleri, avukatın kabul ettiği riskler, zarf çıkmadan sorulacaklar. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan geçme.

## Çıktı biçimleri

- **Tam not (varsayılan):** yukarıdaki gibi; [CLM] kaydına ya da `## House style` klasörüne.
- **Kanal özeti:** iki satır ve bağlantı — `[Karşı taraf] [tür] — DÜZELTME GEREKLİ. 1🔴 (sınırsız sorumluluk m. 8.2), 2🟠. Tam inceleme: [bağlantı]. [GC] onayı gerekli.`
- **Redline belgesi:** istenirse izlenen değişikliklerle .docx (docx skill'i); her değişikliğin yorumu playbook pozisyonuna atıf yapar.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["99","112","114","115","116","117","120","126","128","136"])   ← en çok 10 madde/çağrı; kalanlar (138, 146-148, 179-184, 205, 20-25, 470, 484, 502, 512) ayrı çağrılarla
tr_mevzuat_madde_getir(number="6102", madde_no=["3","5/A","8","18","22","1530"], max_chars_per_article=6000)
tr_mevzuat_madde_getir(number="5846", madde_no=["2","18","48","50","52"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="sorumluluğun sınırlandırılması ağır kusur dolaylı zarar", date_from="2020-01-01")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="yabancı dilde düzenlenen sözleşme 805 sayılı Kanun")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".

## Teslim öncesi kalite kontrolü

- [ ] Eklenti ayarı yüklendi ve alıntılandı (genel piyasa pozisyonu değil); anlaşma bozucu önce kontrol edildi
- [ ] Emredici sınırlar tablosu tarandı, atıflar araçtan; tartışmalı noktalar inceleyen notunda
- [ ] Her sorunun somut redline metni var; ciddiyetler kalibre (her şey Kritik değil)
- [ ] Onaylayıcı adıyla yazıldı; karşı taraf bağlamı (büyük kurumsal / girişim) gözetildi

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu incelemeye göre uyarla (redline'ı taslakla, eskalasyon, ek olgu iste, bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

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
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/arthurlegal:legal-research-az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/arthurlegal:legal-research-sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
