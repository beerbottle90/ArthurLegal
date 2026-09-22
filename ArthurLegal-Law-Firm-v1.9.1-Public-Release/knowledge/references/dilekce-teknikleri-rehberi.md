# Dava Dilekçesi Yazım Teknikleri – Pratik Rehber

> **Durum:** 📐 Tasarım referansı — `advocacy-legal` plugin'inin 3 dilekçe skill'ini destekler: **özel hukuk dava dilekçesi** (HMK), **idari dava dilekçesi** (İYUK), **ceza dilekçeleri** (CMK — şikâyet/iddia, savunma, kanun yolu). Plugin bu repoda henüz kurulu değil (mevcut: `litigation-legal`, `administrative-legal`); bu rehber skill'ler için ortak iskelet, zorunlu unsur ve atıf disiplinini sabitler. Mevzuat ve emsal her zaman **ArthurLegal MCP (`tr_`)** (ArthurLegal MCP (`tr_`) + ArthurLegal MCP (`tr_`)) üzerinden doğrulanır — ezbere madde/karar yazılmaz.

## Üç dilekçe türü hangi skill'e

| Skill | Yargı kolu | Usul kanunu | Tipik kullanım örneği |
|---|---|---|---|
| **Özel hukuk dilekçesi** | Adli yargı (hukuk) | **HMK 6100** m. 119 | Ticari alacak, tazminat, iş kazası bedensel zarar (Asliye Hukuk), istirdat |
| **İdari dava dilekçesi** | İdari yargı | **İYUK 2577** m. 3 | EPDK kurul kararı iptali, ÇED iptali, idari para cezası, KİK/Rekabet kararı |
| **Ceza dilekçesi** | Ceza yargısı | **CMK 5271** | Şikâyet/suç duyurusu (m. 158), savunma/esas hakkında beyan, istinaf-temyiz (m. 273, 291) |

## Zorunlu unsurlar — karşılaştırma tablosu

| Unsur | HMK m. 119 (dava dilekçesi) | İYUK m. 3 (idari dava dilekçesi) | CMK (ilgili maddeler) |
|---|---|---|---|
| Mahkeme başlığı | ✅ m. 119/1-a | ✅ m. 3/1 (Danıştay/mahkeme başkanlığına hitaben) | ✅ ilgili mahkeme/C. Başsavcılığı |
| Davacı/şikâyetçi kimlik + adres | ✅ m. 119/1-b | ✅ m. 3/2-a | ✅ (şikâyette m. 158; sanık/müşteki bilgisi) |
| TC kimlik no | ✅ m. 119/1-c (davacı TCKN) | ✅ m. 3/2-a (gerçek kişilerin TCKN) | ✅ uygulamada |
| Davalı/karşı taraf + adres | ✅ m. 119/1-b | ✅ m. 3/2-a (davalı idare) | C. Başsavcılığı şüpheli; mahkemede sanık |
| Vekil (varsa) + adres/KEP | ✅ m. 119/1-ç | ✅ m. 3/2-a | ✅ müdafi/vekil |
| **Konu** (talep özeti) | ✅ m. 119/1-d (konu + malvarlığı davalarında dava değeri) | ✅ m. 3/2-b (dava konusu) + m. 3/2-c (işlemin yazılı bildirim tarihi) | ✅ dilekçe konusu |
| **Açıklamalar / vakıalar** | ✅ m. 119/1-e (dayanılan vakıalar, sıra no'lu) | ✅ m. 3/2-b (davanın konu ve sebepleri) | ✅ olayların anlatımı |
| Her vakıanın hangi delille ispatı | ✅ m. 119/1-f | uygulamada | uygulamada |
| **Hukuki sebepler** | ✅ m. 119/1-g | ✅ m. 3/2-ç (hukuki sebepler) | ✅ ilgili TCK/CMK maddeleri |
| **Deliller** | ✅ m. 119/1-f | ✅ m. 3/2-b (dayanılan deliller) + m. 3/3 (ekler) | ✅ delil listesi |
| **Sonuç ve talep (netice-i talep)** | ✅ m. 119/1-ğ | ✅ uygulamada (m. 3'te ayrı bent yok; vergi ve tam yargı davalarında uyuşmazlık konusu miktar m. 3/2-d) | ✅ açık talep |
| İmza | ✅ m. 119/1-h (taraf/vekil) | ✅ m. 3/1 (imzalı dilekçe) | ✅ |
| Ekler / dayanak belgeler | ✅ (delil ekleri) | ✅ m. 3/3 (idari işlem + ekleri) | ✅ |

> **HMK m. 119/2 uyarısı:** (1)-a (mahkemenin adı), (1)-d (dava konusu ve değeri), (1)-e (vakıalar), (1)-f (vakıaların delili) ve (1)-g (hukuki sebepler) **dışındaki** eksiklikler için hâkim 1 haftalık **kesin süre** verir; giderilmezse dava açılmamış sayılır. İYUK'ta dilekçe ret rejimi **m. 15/1-d + m. 3/2** üzerinden işler (30 gün içinde yenileme) — ama **dava açma süresi durmaz**, bu yüzden ret kararı kritiktir.

## Ortak iskelet (üç türde de aynı omurga)

```
1. MAHKEME BAŞLIĞI
   "... NÖBETÇİ ASLİYE HUKUK MAHKEMESİ'NE" /
   "... İDARE MAHKEMESİ BAŞKANLIĞI'NA" /
   "... AĞIR CEZA MAHKEMESİ'NE" — (idari yargıda "BAŞKANLIĞINA")

2. TARAFLAR
   DAVACI / ŞİKÂYETÇİ : Ad-soyad/unvan, TCKN/MERSİS, adres
   VEKİLİ            : Av. ..., baro sicil, adres + KEP + (varsa) e-Tebligat
   DAVALI / KARŞI TARAF : ... (idari davada DAVALI İDARE)

3. KONU
   Tek cümlede ne istendiği (örn. "... sayılı EPDK kurul kararının iptali istemidir.")
   İdari davada: dava konusu işlem + TEBLİĞ/ÖĞRENME TARİHİ mutlaka yazılır (süre için).

4. AÇIKLAMALAR (VAKIALAR)
   Numaralı paragraflar. Her maddi vakıa → hangi delille ispatlanacağı.
   Kronolojik, yalın, çelişkisiz. Hukuki niteleme bu bölümde değil, "hukuki sebepler"de.

5. HUKUKİ SEBEPLER
   Dayanılan mevzuat (kanun + madde) + emsal içtihat. (ArthurLegal MCP (`tr_`) ile doğrula.)

6. DELİLLER
   Belge, tanık, bilirkişi, keşif, yemin, isticvap... "ve sair her türlü yasal delil"
   (HMK'da delillerin somut gösterilmesi esastır; "her türlü delil" tek başına yetmez.)

7. SONUÇ VE TALEP (NETİCE-İ TALEP)
   Asıl talep + (varsa) terditli/yedek talep + yargılama gideri + vekâlet ücreti.
   İdari davada: yürütmenin durdurulması talebi (İYUK m. 27) ayrı ve açık.

8. EKLER
   Numaralı ek listesi (vekâletname, dayanak belgeler, idari işlem örneği...).

9. TARİH – İMZA
   Tarih + davacı/vekil ıslak veya e-imza.
```

## Harç ve giderler

| Kalem | Adli yargı (HMK) | İdari yargı (İYUK) |
|---|---|---|
| **Başvurma harcı** | Maktu — Harçlar K. (492) tarifesi | Maktu |
| **Peşin harç** | Konusu para/para ile ölçülebilen davada **nispi** (dava değerinin binde'si, peşin ¼); değilse **maktu** | Genelde **maktu** (iptal davası); tam yargıda tazminat tutarına göre nispi olabilir |
| **Karar/ilam harcı** | Hüküm sonrası tamamlanır | — |
| **Gider avansı** | HMK m. 120 — dava açarken yatırılır; dava sırasında yetersiz kalırsa 2 haftalık kesin süre (m. 120/2); tamamlanmazsa dava şartı (m. 114/1-g) yokluğundan usulden ret (m. 115/2) | İYUK m. 6 — harç + posta ücreti; eksikse 30 gün içinde tamamlanması tebliğ edilir (bir kez tekrarlanır), tamamlanmazsa dava açılmamış sayılır (m. 6/4); dava sırasında posta ücreti azalırsa işlemden kaldırma, 3 ay içinde tamamlanmazsa dava açılmamış sayılır (m. 6/5) |
| **Tanık/bilirkişi/keşif** | Avanstan veya ayrıca | Avanstan |

- Nispi harçta **dava değeri** netice-i talepteki tutarla bağlıdır; eksik harç → **harç ikmali** istenir, yatmazsa dava görülmez. Değer düşük gösterip sonra **ıslahla** artırmak harç ikmali doğurur.
- İdari davada yürütmenin durdurulması talebi ek harca tabi değildir ama teminat istenebilir (m. 27/6).

## UYAP / e-imza / e-Tebligat

- Dilekçeler **UYAP Avukat Portalı** üzerinden, **e-imzalı PDF** olarak sunulur (fiziksel sunum istisna). Bkz. [uyap-rehberi.md](uyap-rehberi.md).
- Müvekkil şirket (özel hukuk tüzel kişisi) ise **elektronik tebligat (UETS) zorunludur** (Tebligat K. m. 7/a); mahkeme tebligatı bu adrese gelir. TTK m. 18/3 ise yalnızca tacirler arası temerrüt/fesih/dönme ihbar ve ihtarlarının noter, taahhütlü mektup, telgraf veya güvenli e-imzalı **KEP** ile yapılmasını düzenler; genel bir KEP zorunluluğu getirmez. e-Tebligat **okunmasa bile 5. günün sonunda tebliğ edilmiş sayılır** (Tebligat K. m. 7/a) — süre buradan işler.
- Vekil bilgisinde adres + **KEP/UETS adresi** yazılır; tebligata esas adres budur.
- Ekler ayrı PDF olarak UYAP'a yüklenir; boyut/format sınırına dikkat (taranmış belgede OCR'lı PDF tercih).

## Dil ve üslup

- **Resmî, açık, sade** Türkçe. Kısa cümle, tek fikir. Pasif yığınından ve gereksiz **Osmanlıca/eskimiş** ifadelerden kaçın ("işbu", "marûz", "ber-mucib", "salifü'l-arz" yerine güncel karşılık).
- Korunan teknik terimler sorun değil: *netice-i talep, terditli talep, müddeabih, def'i, ıslah, husumet* — bunlar yerleşik usul terimleridir.
- Vakıa ile hukuki niteleme ayrılır: "Açıklamalar"da olgu, "Hukuki sebepler"de niteleme.
- Saldırgan/hakaret içeren üslup yok; karşı tarafa saygı, mahkemeye "Sayın Mahkeme".
- Talep sonucu **emir kipinde ve sayısal olarak net**: kalemleri tek tek say (asıl alacak, faiz türü+başlangıcı, yargılama gideri, vekâlet ücreti).

## Atıf disiplini (ArthurLegal MCP (`tr_`))

Mevzuat ve emsal **doğrulanmadan** dilekçeye girmez.

```
# Mevzuat maddesi
tr_mevzuat_ara(number="6100", types=["KANUN"])
tr_mevzuat_icindekiler(mevzuat_id=<id>)
→ Atıf: [ArthurLegal TR — HMK m. 119 — GG.AA.YYYY]

# Emsal içtihat (Yargıtay / Danıştay / BAM-BİM)
tr_ictihat_ara(
  courts=["YARGITAYKARARI"],
  query="<konu> <madde>",
  chamber="HGK",      # en bağlayıcı; idari için "İDDK"/ilgili Danıştay dairesi
  date_from="2022-01-01"
)
→ Atıf: [ArthurLegal MCP (`tr_`) — Yargıtay HGK E.YYYY/.. K.YYYY/.. — GG.AA.YYYY]
```

- Emsal kararı **esas/karar no + daire + tarih** ile göster; gerekçeden alıntı yapıyorsan birebir tırnak içinde ver.
- HGK / İDDK kararları birleştirici/bağlayıcıdır — öncelikle bunları ara.
- Yabancı hukuk gerekirse ayrı MCP'ler (CourtListener, Fedlex vb.) — ama TR dilekçesinde dayanak TR mevzuatı + TR içtihadıdır.

## Sık hatalar (önlem)

- ❌ **Süre kaçırma** — HMK'da kanun yolu süreleri tebliğden 2 hafta (istinaf m. 345); İYUK ilk derece **60 gün** / vergi **30 gün** (m. 7), istinaf-temyiz **30 gün** (m. 45-46); ivedi yargılamada **30/15 gün** (m. 20/A). CMK istinaf ve temyiz **iki hafta** (m. 273, 291 — gerekçeli hükmün tebliğinden; 7499 s.K.). **Her zaman tebliğ/öğrenme tarihinden hesapla.**
- ❌ **Görev/yetki hatası** — bireysel idari işlemi (EPDK kurul kararı, idari ceza) doğrudan Danıştay'a açmak; tahkim klozu varken mahkemede dava açmak (HMK m. 116/1-b); yanlış yer mahkemesi. Yanlış mahkeme → gönderme ama süre koruması sınırlı.
- ❌ **Taraf teşkili / husumet** — davalıyı yanlış göstermek (idari davada **davalı idare** doğru tüzel kişilik olmalı; iş kazasında işveren + varsa müteselsil sorumlular). Husumetten ret riski.
- ❌ **Talep sonucu netliğinde belirsizlik** — "fazlaya ilişkin haklar saklı" demeden tüm tutarı talep etmek; faiz türü/başlangıcını yazmamak; terditli talebi unutmak (sonradan ıslah gerektirir). HMK m. 107 (belirsiz alacak davası) 7589 s.K. ile 31.07.2026'dan itibaren **mülga**; alacak tam belirlenemiyorsa **kısmi dava (HMK m. 109)** açılır — talep, aynı davada bir defaya mahsus, iddianın genişletilmesi yasağına tabi olmaksızın tahkikat sonuna kadar artırılabilir; artırılan kısım için zamanaşımı dava tarihinden kesilmiş sayılır (m. 109/4).
- ❌ **Vakıa-delil bağını kurmamak** — m. 119/1-f gereği her vakıanın hangi delille ispatlanacağı gösterilmeli; "her türlü delil" tek başına yetersiz.
- ❌ **Yürütmenin durdurulmasını istememek** (idari) — işlem uygulanmaya devam eder; İYUK m. 27, ayrı ve gerekçeli talep.
- ❌ **Harç/gider avansı eksiği** — dava açılmamış sayılma veya işlemden kaldırma riski.

## Islah ve dilekçeler teatisi (replik–düplik)

**Dilekçeler teatisi (HMK m. 126-136) — adli yargı dört dilekçe sistemi:**

```
1. DAVA DİLEKÇESİ        (davacı)              — m. 119
2. CEVAP DİLEKÇESİ       (davalı, 2 hafta)     — m. 126-129
3. CEVABA CEVAP / REPLİK (davacı, 2 hafta)     — m. 136
4. İKİNCİ CEVAP / DÜPLİK (davalı, 2 hafta)     — m. 136
→ Sonra ön inceleme (m. 137 vd.); bu aşamadan sonra iddia/savunma genişletme yasağı.
```

- **Replik:** davacının, cevaba karşı; **düplik:** davalının, replike karşı. İddia/savunmanın **serbestçe** genişletilebileceği son tur burasıdır; ön incelemeden sonra karşı tarafın açık muvafakati veya **ıslah** şart.
- **Islah (HMK m. 176-182):** Tahkikat bitene kadar **bir kez**, dava dilekçesi/taleple bağlı kalmadan değiştirme. Talep artışı → **harç ikmali**. Tamamen ıslah (dava sebebini değiştirme) veya kısmen ıslah (örn. müddeabihi artırma) mümkün. Karşı taraf zararı varsa gider/tazminat.
- **İdari yargıda (İYUK):** Dört dilekçe yok; **dava dilekçesi → savunma → davacı cevabı (replik) → ikinci savunma (düplik)** (m. 16). Süre kural 30 gün, idare için ek süre verilebilir. İdari davada **ıslah İYUK m. 16/4** ile sınırlı tanınmıştır (tam yargıda tazminat miktarını bir kez artırma).
- **Ceza yargısında:** Teati/ıslah kavramı yok; iddianame → savunma → delil tartışması → esas hakkında mütalaa/beyan akışı (CMK). Değişen suç vasfı için **ek savunma hakkı** (m. 226).

## Bağlantılı referanslar

- [hmk-rehberi.md](hmk-rehberi.md) — HMK madde haritası, dilekçe/teati/ıslah maddeleri
- [iyuk-rehberi.md](iyuk-rehberi.md) — İYUK süreler, m. 3 dilekçe, m. 15 ret, m. 27 yürütme durdurma
- [idari-yargi-yapisi-rehberi.md](idari-yargi-yapisi-rehberi.md) — görev/yetki, daire haritası
- [uyap-rehberi.md](uyap-rehberi.md) — UYAP avukat portalı, e-imza, e-Tebligat sunumu
- [damga-vergisi-rehberi.md](damga-vergisi-rehberi.md) — belge/sözleşme damga (dilekçe eki belgelerde)
- [mevzuat-mcp-rehberi.md](mevzuat-mcp-rehberi.md) — madde çekme pattern'ları
- [yargi-mcp-rehberi.md](yargi-mcp-rehberi.md) — emsal içtihat çekme pattern'ları
- [kanun-kisaltmalar.md](kanun-kisaltmalar.md) — HMK/İYUK/CMK kısaltma sözlüğü
