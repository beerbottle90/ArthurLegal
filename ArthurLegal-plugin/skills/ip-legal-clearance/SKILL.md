---
name: ip-legal-clearance
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

`## Matter workspaces` → `Enabled` `✗` ise atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:ip-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıyı `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ı okuma.

## Önce profil

`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve `firm-profile.md` oku:
- `## Who's using this` → rol (avukat / avukat değil; üst başlığı ve aşağıdaki kapıyı değiştirir).
- `## IP practice profile` → `Registered in`; `## Enforcement posture` → varsayılan ülkeler.
- `## Available integrations` → hangi arama yapılabilir, yedek yol ne.
- `## Decision posture on subjective legal calls` → bu skill "karıştırılma ihtimali yok" demez.

Ayar `[PLACEHOLDER]` ya da `[Your Company Name]` içeriyorsa:

> Profiliniz henüz kurulmamış. İki seçenek: `/arthurlegal:ip-legal-cold-start-interview` (2 dakika) ya da **"provisional"** deyin; genel varsayımlarla (Türkiye — TÜRKPATENT sicili ve tescilsiz önceki haklar, orta risk iştahı, avukat rolü, playbook yok) çalıştırıp her bulguyu `[PROVISIONAL]` diye etiketlerim.

Provisional çalıştırmanın sonuna ekle: "Bu genel varsayımlarla yapılmış bir çalıştırmaydı. `/arthurlegal:ip-legal-cold-start-interview` ile pratiğinize göre ayarlayın."

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
- **TÜRKPATENT:** ArthurLegal MCP'de TÜRKPATENT aracı **yoktur** (resmî uç çalışmıyor). Aramayı TÜRKPATENT web sitesindeki marka araştırma ekranından elle yap ya da yaptır; Bülten ve sınıf/sahip aramasının pratiği için `${CLAUDE_PLUGIN_ROOT}/references/turkpatent-rehberi.md`. Ekran görüntüsü ya da dışa aktarımı kullanıcıdan iste; sonuçları ondan aktar.
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

Matter etkin ve aktifse `~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/clearance-<mark-slug>-YYYY-MM-DD.md`; değilse `~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/clearance-<mark-slug>-YYYY-MM-DD.md`. Yolu kullanıcıya göster; matter aktifse `history.md`'ye tek satır ekle. Marka benimsenir ve başvuru sıraya girerse `/arthurlegal:ip-legal-portfolio --add` öner.

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
