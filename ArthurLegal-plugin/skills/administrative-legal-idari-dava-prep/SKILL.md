---
name: administrative-legal-idari-dava-prep
description: >
  İdari işleme karşı dava açılacak — KRİTİK İLK ADIM görevli mahkeme tespiti
  (İdare Mahkemesi mi, Danıştay mı ilk derece?), İYUK m. 7 (60/30 gün hak düşürücü)
  süre kontrolü, dava dilekçesi taslağı, yürütmenin durdurulması (m. 27),
  yetkili yer (HMK/İYUK), emsal kararlar (ArthurLegal MCP (`tr_`)). 3 dereceli idari yargı
  yapısına göre.
user-invocable: true
---

# İdari Dava Hazırlık

## ⏰ ÖN-KONTROL — SÜRE (her çalıştırmada)

> İdari işlem/karar **tarafa tebliğ tarihi** nedir?
> İYUK m. 7/1:
> - **İdare mahkemeleri: 60 GÜN** (özel kanun aksini belirtmedikçe)
> - **Vergi mahkemeleri: 30 GÜN** (2021 değişikliği)
> - **ÇED kararları: 30 GÜN** (İYUK m. 20/A ivedi yargılama — özel rejim)
> - **Diğer özel rejim** (kamu ihale belirli kategoriler, özelleştirme): m. 20/A kontrolü

Kalan < 5 gün → 🔴 ACİL. Dış vekille derhal koordinasyon.

⚠️ **Sık yapılan hata:** Vergi mahkemesi 30 günü idare mahkemesi davalarına yanlış uygulamak. Her zaman görevli mahkemeyi önce tespit et, sonra süreyi.

## Destination check

- **Mali İşler + Hukuk iç değerlendirme** → "GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ"
- **Dış idari hukuk avukatı brief** → "İDARİ DAVA BRIEF – AVUKATLIK K. m. 36"
- **CEO/Başkan eskalasyon** → 1 sayfa exec summary
- **Mahkemeye sunulacak dilekçe taslak** → "TASLAK" + dış vekil onayı sonrası

## ⚠️ ADIM 0 — GÖREVLİ MAHKEME TESPİTİ (en kritik)

Türk idari yargı **3 dereceli**: İdare Mahkemesi → BİM → Danıştay. **Danıştay genelde TEMYİZ mercii**, sadece dar istisnalarda ilk derece.

### Danıştay ilk derece görevli mi? (Danıştay K. m. 24)

İdari işlem bir aşağıdakilerden biri mi?
- [ ] **Cumhurbaşkanı Kararı** (tek karar, atama, vs.)
- [ ] **CB Kararıyla yürürlüğe konulan düzenleyici işlem** (Bakanlar Kurulu kararı muadili — genel norm)
- [ ] **Bakanlık veya kamu kurumu müsteşarına ilişkin müşterek kararname**
- [ ] **Bakanlık genel tebliği** veya **bakanlık yönetmeliği** (normatif düzenleyici işlem — bireysel idari işlem DEĞİL)
- [ ] EPDK / Rekabet Kurumu / BDDK / SPK gibi **kurumun genel TEBLİĞİ veya YÖNETMELİĞİ** (normatif)

**Evet** → **Doğrudan Danıştay**'a dava (ilgili daire — enerji/finans 13., çevre 10./14., diğer 5./8.)
**Hayır** → **İdare Mahkemesi**'nde ilk derece dava (sonra BİM istinaf, sonra Danıştay temyiz)

### Yetkili yer İdare Mahkemesi (eğer ilk derece İdare Mah. ise)

- **Genel kural (İYUK m. 32):** Davalı idarenin bulunduğu yer İdare Mahkemesi
  - EPDK / Rekabet / KVKK / KİK / BDDK / SPK = **Ankara** (kurumlar Ankara merkez)
  - Bakanlık merkez kararları = **Ankara**
  - İl müdürlüğü kararları (örn. İzmir Çevre İl Müdürlüğü idari ceza) = **İzmir İdare Mahkemesi**
  - [tesis yeri] Belediyesi imar kararları = **İzmir İdare Mahkemesi** ([TESİS LOKASYONU] bağlı)

- **Özel yetki kuralları (İYUK m. 33-37):**
  - Vergi davası: vergi dairesinin bulunduğu yer (tax-legal kapsamında)
  - Memur statü: memurun görev yaptığı yer veya idarenin yeri
  - Kamulaştırma: taşınmazın bulunduğu yer

⚠️ **Yanlış mahkemeye dava:** İdari yargı içinde görevsiz veya yetkisiz mahkemeye açılan dava görev/yetki yönünden reddedilir ve **dosya görevli/yetkili mahkemeye gönderilir** (İYUK m. 15/1-a); dava ilk açıldığı tarihte açılmış sayılır. Adli yargıya açılıp görevsizlikle reddedilen davada, kararın kesinleşmesinden itibaren **30 gün** içinde görevli idari mahkemede dava açılabilir; görevsiz yargı yerine başvurma tarihi idari yargıya başvurma tarihi sayılır (m. 9/1). Bu 30 gün geçse de idari dava süresi henüz dolmamışsa o süre içinde dava açılabilir (m. 9/2).

## Adımlar

### 1. İdari işlemi analiz et

| Soru | Cevap |
|---|---|
| İdari işlem tipi | Bireysel (lisans iptali, ceza, ret) / Düzenleyici (tebliğ, yönetmelik) |
| İdari işlemi yapan kurum | EPDK / Çevre Bakanlığı / Rekabet / KVKK / KİK / vs. |
| Tebliğ tarihi | GG.AA.YYYY |
| Tebliğ şekli | KEP / e-tebligat (UYAP) / yazılı / Resmi Gazete (düzenleyici işlem için) |
| Hukuki dayanak (idarenin gösterdiği) | [Kanun/Yönetmelik madde no'ları] |
| Talep edilen tutar (varsa) | TL |

### 2. Görevli mahkeme tespiti (ADIM 0 sonucu)

```markdown
**Görevli mahkeme:**
[Ankara X. İdare Mahkemesi — bireysel idari işlem için] VEYA
[Danıştay X. Daire — istisna kapsamında düzenleyici işlem için]

**Yetki gerekçesi:** [İYUK m. 32 — Ankara EPDK Kurul kararı için]
             VEYA  [Danıştay K. m. 24 — bakanlık yönetmeliği için]
```

### 3. Süre hesabı

```markdown
**Tebliğ tarihi:** GG.AA.YYYY
**Dava süresi sonu:** GG.AA.YYYY (kalan: N gün)
**İYUK m. 7 — 60 gün** (vergi mahkemesinde 30; özel kanunda ayrı süre ya da İYUK m. 20/A ivedi usul varsa o) [hak düşürücü]
```

### 4. Hukuki argümanlar

İdari işlemin iptali için klasik gerekçeler:
- **Yetkisizlik:** İdare bu işlemi yapma yetkisinde mi?
- **Şekil eksikliği:** Usul kurallarına uyuldu mu (kanunla aranan açıklamalar, gerekçe, oybirliği/oyçokluğu)?
- **Sebep yokluğu:** İdarenin dayandığı sebep hukuki/fiili olarak var mı?
- **Konu hukuka aykırılığı:** Kanunun açık metnine ters mi?
- **Amaç hukuka aykırılığı:** Kamu yararı dışında bir amaç gözetilmiş mi (örtülü amaç)?

### 5. Yürütmenin durdurulması (İYUK m. 27) — KRİTİK

Talep şart, **otomatik gelmez**. İki şart birden:
- **Telafisi güç veya imkansız zararlar:** EPDK lisans askıya alma → üretim duruş → milyon TL gelir kaybı; ÇED ret → yatırım dondurulur
- **Açıkça hukuka aykırılık:** Yukarıdaki argümanlardan en güçlüsü

**Talep dilekçenin içinde** ayrı bölüm olarak.

### 6. ArthurLegal MCP (`tr_`) — emsal arama

```
# Bireysel idari işlem için Danıştay temyiz emsali
tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="D13",  # EPDK/Rekabet/BDDK/SPK/KİK için
  query="<konu> iptal yürütmenin durdurulması",
  date_from="2022-01-01"
)

# Çevre/ÇED için
tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="D10",
  query="+çevre +ÇED +idari +para +cezası",
  date_from="2022-01-01"
)

# İdare Mahkemesi/BİM kararları
tr_ictihat_ara(
  query="<konu>",
  date_from="2022-01-01"
)

# İdari kurum birincil kararları
tr_kurum_karari_ara(kurum="rekabet", query="<konu>")
kurum_karari_ara(kurum="kik", keywords="<konu>")
tr_kurum_karari_ara(kurum="kvkk", query="<konu>")
```

### 7. Dava dilekçesi taslağı

```markdown
[GÖREVLİ MAHKEME BAŞLIĞI — örn. ANKARA X. İDARE MAHKEMESİ BAŞKANLIĞINA
veya DANIŞTAY X. DAİRESİ BAŞKANLIĞINA]

DAVACI:
[Müvekkil] — VKN, sicil, adres
Vekili: [Av. ad, baro sicil, KEP]

DAVALI:
T.C. [Bakanlık / EPDK / Rekabet Kurumu / vs.]
Vekili: [İlgili Bakanlık vekili veya Hazine ve Maliye Bakanlığı genel olarak]

DAVA KONUSU:
[Kurum] tarafından tesis edilen [GG.AA.YYYY tarih, ... sayılı] [karar/işlem]
nın **iptali** ile **yürütmenin durdurulması** talebidir.

İŞLEMİN TARİFİ:
[İdari işlemin tam tarifi, tarih, sayı, içerik]
Tebliğ tarihi: GG.AA.YYYY
Dava süresi: [60 gün — İYUK m. 7; vergi mahkemesinde 30; özel kanun / m. 20/A ivedi usulde 30] → son tarih GG.AA.YYYY

I. OLAYLAR
[Kronoljik olay özeti]

II. HUKUKİ DAYANAKLARIMIZ

A. **Yetkisizlik** (eğer varsa) [argüman]
B. **Şekil eksikliği** [varsa]
C. **Sebep yokluğu** [argüman + emsal Danıştay kararı: `[ArthurLegal MCP (`tr_`) — danistay — daire — esas/karar — GG.AA.YYYY]`]
D. **Konu hukuka aykırılığı** [argüman]
E. **Amaç hukuka aykırılığı** [varsa]

III. YÜRÜTMENİN DURDURULMASI TALEBİMİZ (İYUK m. 27)

1. **Telafisi güç zararlar:**
   [EPDK lisans askıya alma → üretim duruş → günlük X TL kayıp]
   [veya benzeri somut zarar]

2. **Açıkça hukuka aykırılık:**
   [Yukarıdaki en güçlü argüman]

IV. SONUÇ VE TALEP

1. Yürütmenin durdurulmasına,
2. Dava konusu idari işlemin iptaline,
3. Yargılama gideri ve vekalet ücretinin davalı idareye yüklenmesine,

karar verilmesi saygıyla arz ve talep olunur.

Tarih: GG.AA.YYYY
Davacı Vekili: [imza]

EKLER:
1. Vekaletname
2. İdari işlemin tebliğ örneği
3. Konuya ilişkin belgeler
4. Emsal kararlar (Danıştay/BİM)
```

### 8. sektöre-özel kontroller

- [ ] **Tutar > 10M TL** veya **stratejik önem** → CEO + Başkan eskalasyon
- [ ] **halka açık iştirak ilgili** → KAP açıklama kontrolü + IR Başkanlığı
- [ ] **EPDK lisans askıya alma riski** → derhal Başkan + CEO + iş birimi
- [ ] **[TESİS LOKASYONU] İSG/çevre olayı sonrası idari ceza** → litigation-legal `isg-incident-response` ile koordine (üçlü-paralel dava)
- [ ] **Üst yönetim ismi var** → CEO + YK
- [ ] **Basın takibi** → İletişim Başkanlığı ([İletişim Başkanlığı]) koordinasyon
- [ ] **[BORU HATTI PROJESİ] / hükümetlerarası anlaşma alanı** → dış uzman + üst yönetim

## Çıktı

```markdown
[ÜST BAŞLIK]

# İdari Dava Hazırlık — [İdari işlem]

## ⚠️ İnceleyen notu
- **Görevli mahkeme:** [tespit] (gerekçe: [...])
- **Tebliğ tarihi:** GG.AA.YYYY → **Süre sonu: GG.AA.YYYY (kalan: N gün)** 🔴/🟠/🟡
- **Yürütmenin durdurulması:** evet (gerekçe: [...])
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (Danıştay [N] + kurum [N]); ArthurLegal MCP (`tr_`)
- **Eskalasyon:** [tetiklendi mi?]
- **KAP açıklama:** [N/A / hazırlanıyor]
- **Reviewer bekleyen:** N adet

## İdari işlem analizi
[tablo: işlem tipi, kurum, tarih, talep, dayanak]

## Görevli mahkeme tespiti
[karar + İYUK madde gerekçesi]

## Hukuki argümanlar
[A-E: yetkisizlik, şekil, sebep, konu, amaç]

## Yürütmenin durdurulması analizi
[telafisi güç zarar + hukuka aykırılık argümanları]

## Emsal Danıştay/kurum kararları
[ArthurLegal MCP (`tr_`)'den çekilen tablolar]

## Dava dilekçesi taslağı (dış vekil revize için)
[yukarıdaki şablon — doldurulmuş]

## Sonraki adımlar

> 1. **Dış idari avukatı brief** — `/arthurlegal:litigation-legal-outside-counsel-brief` (idari dava varyantı)
> 2. **Eskalasyon notu** — Başkan/CEO için 1 sayfa
> 3. **KAP açıklama metni** (halka açık iştirak ilgili büyük etki)
> 4. **EPDK proaktif görüş** alternatifi düşünme — `/arthurlegal:administrative-legal-epdk-proaktif-gorus` (dava açmadan önce dialog şansı)
> 5. **Daha fazla bilgi** — [...]

**One question I'd ask:** [örn. "Bu daire son 12 ayda benzer [Müvekkil]/sektör davalarında bir eğilim gösterdi mi? Davayı kazanma ihtimalini değiştirir."]
```

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
| idare hukuku ogretisi — DergiPark *Idare Hukuku ve Ilimleri* dergisi router tarafindan secilir; **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
