# firm-operations - Skill Referans Kitapçığı

> Alan: Büro operasyonları — müvekkil intake, çıkar çatışması, MASAK, KVKK, ücret, vekalet
> Toplam skill: 10
> Kullanım: /{plugin}:{skill-adı} komutunu yaz, aşağıdaki ilgili bölümü uygula.
> Yeni müvekkil akışı: new-client-intake → conflict-check → masak-kontrol → sanctions-check → kvkk-aydinlatma → fee-agreement → vekalet-sablon → matter-open. Ay sonu: monthly-billing.
> Madde atıfları 24.09.2026'da `tr_mevzuat_madde_getir` ile doğrulandı; her skill'in "Dayanak" bloğu atfın tam künyesini verir. "doğrulanmadı" yazan bilgi ezberden tamamlanmaz.

## İçindekiler

- /firm-operations:cold-start-interview
- /firm-operations:conflict-check
- /firm-operations:fee-agreement
- /firm-operations:kvkk-aydinlatma
- /firm-operations:masak-kontrol
- /firm-operations:matter-open
- /firm-operations:monthly-billing
- /firm-operations:new-client-intake
- /firm-operations:sanctions-check
- /firm-operations:vekalet-sablon

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
> **Meslek sirri (Av. K. m. 36):** uc MCP de PUBLIC arama aracidir — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| yabanci karsi tarafli veya AZ baglantili yeni is alimi — mevzuat kapsaminin gercekten var olup olmadigini once dogrula | `/legal-research:kaynak-secimi` |

Rehberler: `references/eqanun-mcp-rehberi.md` · `references/lex-scholar-rehberi.md` · `references/resourcecontracts-rehberi.md` · `references/karsilastirmali-hukuk-rehberi.md`

---

## /firm-operations:cold-start-interview

---
name: cold-start-interview
description: >
  Büro profilini ilk doldurma — TÜM diğer plugin'lerin okuyacağı ana profil.
  Büro kadrosu, ortaklar, organizasyon yapısı, baro kayıt durumu, müvekkil
  portföyü agregat (sektör + tip + coğrafya), pratik alanları, müvekkil intake
  politikası, vekalet ücreti modeli, mesleki sır pratikleri, operasyonel platformlar.
  Sonuç: knowledge/firm-profile.md doldurulur.
user-invocable: true
---

# Cold Start Interview — firm-operations (ANA PROFİL)

## Amaç

`knowledge/firm-profile.md` içindeki `[DOLDUR]` alanlarını doldur. ~20-30 dk (büronun tüm bilgisini topluyor).

⚠️ **Bu, paketteki TÜM diğer plugin'lerin okuyacağı ana profildir. Önce bu plugin'i çalıştırın, sonra diğer plugin'lerin cold-start'larını.**

## Adımlar

### 1. Büro temel bilgileri

- Büro adı, hukuki yapı (Avukatlık Ortaklığı / Hibrit / Bireysel)
- TBB Avukatlık Ortaklıkları Sicil no (varsa)
- Kuruluş yılı
- Vergi no, MERSİS (varsa Av. Ortaklığı tüzel kişiliği)

### 2. Ofis ve coğrafya

- Merkez ofis: il / ilçe / adres
- İrtibat ofisleri (varsa)
- Çalışma dilleri (Türkçe ana, İngilizce, başka?)

### 3. Kadro

- Yönetici Ortak (takma ad + baro/sicil + uzmanlık)
- Kıdemli Ortaklar (sayı + uzmanlık dağılımı)
- Bağlı avukat sayısı
- Stajyer sayısı
- Hukuk asistan + sekretarya sayısı
- **Toplam kadro** (0-30 bandı kontrol)

### 4. Baro kayıt

- İstanbul Barosu kaç ortak/avukat (asıl)
- Ankara Barosu kaç ortak/avukat (asıl/bağlı)
- Diğer barolar

### 5. Müvekkil portföyü (agregat — gerçek isim YOK)

- Aktif müvekkil sayısı
- Sürekli danışmanlık (retainer) sayısı
- Müvekkil tip dağılımı (bireysel / KOBİ / mid-cap / yabancı)
- Sektör dağılımı (inşaat / perakende / üretim / hizmet / teknoloji / bireysel)
- Coğrafi dağılım (İstanbul / Anadolu yakası / Ankara / başka / yurtdışı)

### 6. Pratik alanları

- Hangi plugin'ler aktif kullanılacak? (criminal-defense, firm-operations dahil)
- Aylık matter hacmi tahmini her plugin için

### 7. Müvekkil intake politikası

- Yeni müvekkil kabul akışında zorunlu adımlar
- Conflict check derinliği
- MASAK kimlik tespit alışkanlığı
- KVKK aydınlatma metni standardı var mı?
- Otomatik 🟠 incelemeli kabul tetikleyicileri

### 8. Vekalet ücreti modeli (büro seviye)

- Standart model: saatlik / götürü / hibrit / başarı bonusu?
- Saatlik oran (Yönetici/Kıdemli Ortak, Bağlı Avukat, Stajyer)
- Başarı bonusu sınırı (max %25 — Av. K. m. 164)
- Karşı yan vekalet ücreti politikası (vekile mi, paylaşılır mı)

### 9. Operasyonel platformlar

- Matter / belge yönetimi (iManage / SharePoint / Drive / dahili)
- Zaman takibi (Clio / TimeSolv / Excel)
- Fatura / muhasebe (dahili / dış muhasebeci)
- E-imza / KEP (büro + her ortak)
- CRM (varsa)
- Sanctions tarama (OpenSanctions API — API key alınmış mı?)

### 10. "Yakıcı" stres alanları

> "Bu büroda günlük operasyonu en çok zorlayan 1-3 şey nedir?"

## Çıktı

`knowledge/firm-profile.md` doldurulur.

```
✓ Büro profili tamamlandı.

Sonraki adımlar:
1. Diğer plugin'lerin cold-start-interview'larını çalıştırın:
   /litigation-legal:cold-start-interview
   /commercial-legal:cold-start-interview
   (her aktif plugin için)
2. İlk müvekkil için: /firm-operations:new-client-intake

Re-run: /firm-operations:cold-start-interview --redo
```

## Hatalar / kenar durumlar

- **Kullanıcı 30+ çalışan diyorsa** → "Bu paket 0-30 kadro için optimize edilmiş. 30+ için bazı pratikler (matter izolasyonu, ethical wall, large M&A) farklı yönetilir. Yine de devam edelim mi?"
- **Tüm soruları cevaplamak istemez** → Quick start (5 dk) vs. Full (20-30 dk) seçeneği sun
- **Müvekkil isim/şirket isteyebilir** → "ASLA gerçek müvekkil ismi yazmayın. Takma ad/agregat kullanın."

---

## /firm-operations:conflict-check

---
name: conflict-check
description: >
  Av. K. m. 38 + TBB Meslek Kuralları m. 35-36 çatışma taraması. Müvekkil + karşı
  yan + atanan avukat üç eksen tarama; eşzamanlı / eski müvekkil / grup içi /
  vekil değişimi / kamu görevi geçmişi senaryoları. Sonuç: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ.
user-invocable: true
---

# Conflict Check — Çıkar Çatışması Taraması

## Tetikleyici

- Yeni müvekkil intake (her yeni matter için zorunlu)
- Mevcut matter'da karşı yan kimliği netleştiğinde
- Mevcut müvekkilin başka bir işi
- Yeni ortak/avukat alındığında (retrospektif)
- Müvekkil yapısı değişti (M&A, pay devri)

## Tarama girdisi

### Müvekkil bilgisi
- Tip: Bireysel / Tüzel kişi
- TC kimlik / Vergi no / MERSİS no
- Ad-soyad / Ünvan
- (Tüzel) yan-grup şirketler — UBO + holding zinciri

### Karşı yan bilgisi
- Tip: Bireysel / Tüzel kişi
- TC kimlik / Vergi no / MERSİS no
- Ad-soyad / Ünvan
- (Tüzel) yan-grup şirketler

### Atanan avukat
- Sicil + baro
- Eski büro/iş geçmişi
- Kamu görevi (hakim/savcı/müfettiş) geçmişi
- Aile/yakın ilişki (büro içi)

## Tarama akışı

### 1. Müvekkilin geçmiş matter'ları taraması

Veritabanı sorgu:
- **Tam eşleşme** (TC/Vergi no)
- **Fonetik benzer ad** (Soundex TR varyasyon — Ş/S, İ/I, Ç/C, Ö/O, Ü/U, Ğ/G)
- **Tarih kapsamı:** son 10+ yıl (Av. K. m. 36 süresiz, ama 10 yıl pratik baseline)

### 2. Karşı yan taraması

- Karşı yanın geçmiş matter'ları (eski müvekkilimiz mi?)
- Karşı yanın grup ilişkileri (MERSİS sicili)

### 3. Atanan avukat taraması

- Atanan avukatın eski büro/iş geçmişi
- Hâkim/savcı/hakem/bilirkişi/memur olarak aynı işte görev (Av. K. m. 38/1-c)
- Aile/yakın ilişki — büro içi

### 4. Çatışma sınıflandırma

Dayanak: AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 38 (doğrulandı 24.09.2026). Reddetme zorunluluğu avukatın **ortaklarını ve yanında çalışan avukatları da** kapsar (m. 38/2), yani tarama büro çapındadır. TBB Meslek Kuralları m. 35-36 metni bu araçla doğrulanamadı (mevzuat.gov.tr'de yok).

| Tip | Kural | Karar |
|---|---|---|
| Aynı işte menfaati zıt tarafa avukatlık etmiş veya mütalaa vermiş (eşzamanlı ya da önceden) | Av. K. m. 38/1-b | ⛔ MUTLAK YASAK |
| Evvelce hâkim, hakem, Cumhuriyet savcısı, bilirkişi veya memur olarak o işte görev | Av. K. m. 38/1-c | ⛔ MUTLAK YASAK |
| Kendi düzenlediği senet veya sözleşmenin hükümsüzlüğünü ileri sürme durumu | Av. K. m. 38/1-d | ⛔ MUTLAK YASAK |
| Teklif yolsuz veya haksız | Av. K. m. 38/1-a | ⛔ RET |
| Eski müvekkil — farklı iş, bilgi bağlantısı var | Av. K. m. 36 (sır) + TBB MK m. 35-36 (doğrulanamadı) | 🟠 İNCELE (yazılı rıza) |
| Grup içi (aynı holding) | "aynı iş" ölçütüyle m. 38/1-b'ye göre değerlendir | 🟠 İNCELE (bilgi izolasyonu mümkün?) |
| Vekil değişimi (yeni gelen avukat) | Eski büro geçmişi; m. 38/2 büro çapında | 🟠 İNCELE (ethical wall) |
| Avukatın kendi menfaati | Self-dealing | ⛔ MUTLAK YASAK |
| Hiçbir çakışma yok | — | ✓ TEMİZ |

## Çıktı

```markdown
[ÜST BAŞLIK — CONFLICT CHECK SONUCU — DAHİLİ]

# Conflict Check — [Müvekkil takma adı] vs. [Karşı yan takma adı]
Tarih: GG.AA.YYYY
Atanan ortak: [Yönetici Ortak veya öneri]

## ⚠️ İnceleyen notu
- SONUÇ: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ

## SONUÇ
[Gerekçeli değerlendirme]

## Sonraki adımlar
[✓ TEMİZ ise] → /firm-operations:new-client-intake devam
[🟠 ise] → Ortaklar Kurulu + yazılı rıza
[⛔ ise] → Müvekkile red + REJECTED.md kaydı
```

---

## /firm-operations:fee-agreement

---
name: fee-agreement
description: >
  Avukatlık ücret sözleşmesi taslağı. Kapsam, ücret modeli, AAÜT tabanı, yüzde ücret
  tavanı (%25), karşı taraf vekâlet ücreti, azil/çekilme ve peşin ücret hükümlerini
  Av. K. m. 163-174'e göre kontrol eder. Vergi oranlarını güncel kaynaktan doğrulamadan
  yazmaz. Sonuç: imzaya hazır taslak + kontrol tablosu.
user-invocable: true
---

# Fee Agreement — Avukatlık Ücret Sözleşmesi

## Tetikleyici

- `/firm-operations:conflict-check` ✓ TEMİZ (🟠 ise Ortaklar Kurulu kararı) ve `/firm-operations:masak-kontrol` tamamlandıktan sonra
- Mevcut müvekkilin yeni işi (her iş için ayrı kapsam)
- Ücret modeli değişikliği (ek protokol)

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 41, m. 163, m. 164, m. 165, m. 166, m. 168, m. 171, m. 174
- VERGİ USUL KANUNU (Kanun No. 213, RG sayı 10705) m. 236
- GELİR VERGİSİ KANUNU (GVK) (Kanun No. 193, RG sayı 10700) m. 94
- DAMGA VERGİSİ KANUNU (Kanun No. 488, RG sayı 11751) m. 5, m. 24, (1) sayılı tablo
- Tarife: AVUKATLIK ASGARİ ÜCRET TARİFESİ GENEL HÜKÜMLER (Tebliğ No. 42687, RG 04.11.2025/33067). 24.09.2026 itibarıyla yayımlanan son tarife kaydı budur; tarife kalemleri bu skill'de doğrulanmadı.

## Girdi

- Müvekkil takma adı + tip (gerçek / tüzel); birden çok iş sahibi var mı
- İşin tanımı: hangi hukuki yardım, hangi yargı yeri veya merci, hangi aşamaya kadar
- Ücret modeli (`firm-profile.md` → vekâlet ücreti modeli): saatlik / sabit / yüzde / karma / sürekli danışmanlık
- Uyuşmazlık değeri; para ile ölçülebiliyor mu
- Peşin ücret ve ödeme takvimi

## Kontrol akışı

### 1. Kapsam
Sözleşme **belli bir hukuki yardımı** ve **meblağ yahut değeri** kapsamalıdır (Av. K. m. 163/1). "Tüm hukuki işler" gibi genel kapsam yazma. İşi, merciyi ve bitiş noktasını (ilk derece kararı / kesinleşme / icra yoluyla tahsil) yaz.

### 2. Neden yazılı yapılır
Kanun yazılı şekli geçerlilik şartı yapmaz. Sözleşme serbestçe düzenlenir; yazılı olmayan anlaşma genel hükümlere göre ispatlanır (m. 163/1). Ücret kararlaştırılmamışsa, yazılı sözleşme yoksa ya da sözleşme belirsiz veya tartışmalıysa, para ile ölçülebilen işlerde ücret itirazlarını incelemeye yetkili merci, AAÜT altında kalmamak koşuluyla, kazanılan bölüm için ilamın kesinleştiği tarihteki müddeabihin **%10'u ile %20'si** arasında bir ücret belirler. Para ile ölçülemeyen işlerde AAÜT uygulanır (m. 164/4). Yazılı sözleşme bu belirsizliği önler.

### 3. AAÜT tabanı
- Tarifenin altında vekâlet ücreti kararlaştırılamaz (m. 164/4).
- Ücretsiz iş alınırsa durum baro yönetim kuruluna bildirilir (m. 164/4).
- Ücretin takdirinde, hukuki yardımın tamamlandığı veya hükmün verildiği tarihte yürürlükte olan tarife esas alınır (m. 168). Sözleşmeye sabit bir tarife yılı yazma; "yürürlükteki AAÜT" de.

### 4. Yüzde ücret (başarıya bağlı)
- Dava veya hükmolunacak şeyin değeri yahut paranın belli bir yüzdesi ücret olarak kararlaştırılabilir; oran **%25'i aşamaz** (m. 164/2).
- Tavanı aşan sözleşme batıl değildir; **tavan miktarında geçerlidir**. İfa edilmiş sözleşmenin geçersizliği ileri sürülemez (m. 163/2).
- Dava konusu para dışındaki mal ve haklardan bir kısmının **aynen** avukata ait olacağı yazılamaz (m. 164/3).
- Kanuna aykırı olmayan şarta bağlı sözleşme geçerlidir (m. 163/1).

### 5. Karşı taraf vekâlet ücreti
- Kararla tarifeye dayanılarak karşı tarafa yüklenen vekâlet ücreti **avukata aittir**. Bu ücret iş sahibinin borcu nedeniyle takas ve mahsup edilemez, haczedilemez (m. 164/5).
- Kanun metninde "aksi kararlaştırılmadıkça" istisnası yoktur. Müvekkil lehine farklı bir paylaşım yazılacaksa geçerliliği içtihatla doğrulanmalıdır; bu pakette **doğrulanmadı**. Ücretin kime ait olduğunu sözleşmede açıkça yaz.

### 6. Birden çok iş sahibi
İş sahibi birden çoksa her biri avukatlık ücretinden **müteselsilen** sorumludur. Sulhle veya anlaşmayla biten ya da takipsiz bırakılan işlerde her iki taraf da müteselsil borçlu sayılır (m. 165). Sözleşmeyi tüm iş sahiplerine imzalat.

### 7. Peşin ücret, vazgeçme, azil, çekilme

| Durum | Sonuç | Dayanak |
|---|---|---|
| Peşin ücret ödenmedi | Avukat işe başlamak zorunda değil; doğan sorumluluk iş sahibinde | m. 174/3 |
| Avukat haklı sebep olmadan takipten vazgeçti | Ücret isteyemez, peşin aldığını iade eder | m. 174/1 |
| Müvekkil avukatı azletti | Ücretin tamamı ödenir; kusur veya ihmal nedeniyle azilde ödenmez | m. 174/2 |
| Avukat vekâletten çekildi | Vekâlet görevi, çekilmenin müvekkile tebliğinden itibaren 15 gün devam eder | m. 41/1 |

### 8. Tevkil
Vekâletnamede tevkil yetkisi varsa iş başka bir avukatla birlikte ya da başka bir avukata verilerek takip ettirilebilir (m. 171/2); avukatın müvekkile karşı sorumluluğu sürer (m. 171/3). İşe başka avukat katılırsa ayrı ücret istenmez. İş tamamen devredilirse ücret sözleşmesindeki miktar aşılamaz (m. 171/4).

### 9. Ücret alacağının güvencesi (bilgi maddesi)
Avukat, ücret ve gider ödenene kadar müvekkilin verdiği ya da onun adına aldığı mal, para ve kıymetleri alacağı oranında elinde tutabilir (hapis hakkı). Ücret alacağı, avukatın çalışmasıyla korunan veya kazanılan mallar üzerinde rüçhanlıdır (m. 166).

### 10. Vergi ve belge kalemleri
- **Makbuz:** her tahsilat için iki nüsha serbest meslek makbuzu düzenlenir, bir nüshası müvekkile verilir (VUK m. 236). Elektronik makbuz (e-SMM) zorunluluğu bu skill'de doğrulanmadı; büro muhasebecisiyle teyit et.
- **Tevkifat:** GVK m. 94 tevkifatını maddede sayılan ödeyiciler yapar (ör. ticaret şirketleri, kamu idareleri, gerçek gelirini beyan eden ticaret ve serbest meslek erbabı). Olağan bireysel müvekkil bu listede değilse tevkifat yapmaz. **Oran** Cumhurbaşkanı kararlarıyla belirlenir; doğrulanmadı.
- **KDV oranı:** doğrulanmadı.
- **Damga vergisi:** belli parayı ihtiva eden mukavelenamelerde uygulanacak oran **binde 9,48**'dir (DVK (1) sayılı tablo I/A-1; metin `tr_mevzuat_madde_getir` yanıtında m. 33 düğümünde okundu). Nispi vergiye tabi kâğıt birden çok nüsha düzenlense de **yalnız bir nüshası** vergilenir (DVK m. 5). Birden fazla kişinin imzaladığı kâğıtta imza edenler vergi ve cezadan müteselsilen sorumludur (DVK m. 24). m. 14'teki azami tutar ve olası istisnalar doğrulanmadı.
- Doğrulanmayan her oranı taslakta `[ORAN — doğrulanmadı, GG.AA.YYYY]` diye bırak; tahmin yazma.

## Çıktı

```markdown
[ÜST BAŞLIK — AVUKATLIK ÜCRET SÖZLEŞMESİ — TASLAK — İMZA BEKLİYOR]

# Ücret Sözleşmesi — [Müvekkil takma adı] — [İş kısa adı] — GG.AA.YYYY

## ⚠️ İnceleyen notu
- Ücret modeli: [...]
- AAÜT tabanı: ✓ / ⛔ (tarifenin altında)
- Yüzde ücret: %[X] (tavan %25) ✓ / ⛔
- Vergi oranları: doğrulandı [kaynak, tarih] / `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>`

## Sözleşme metni
1. Taraflar
2. Kapsam — [hukuki yardım, merci, bitiş noktası]
3. Ücret ve ödeme takvimi — [peşin / aşama / sonuç]
4. Karşı taraf vekâlet ücreti — avukata aittir (Av. K. m. 164/5)
5. Giderler (harç, bilirkişi, tebligat) — kim öder, avans usulü
6. Azil ve çekilme — Av. K. m. 174 ve m. 41
7. Birden çok iş sahibi — müteselsil sorumluluk (Av. K. m. 165)
8. Tebligat adresleri (varsa KEP)
9. İmzalar

## Kontrol tablosu
| Kontrol | Sonuç | Dayanak |
|---|---|---|
| Kapsam belli | ✓ / ⛔ | Av. K. m. 163/1 |
| AAÜT altında değil | ✓ / ⛔ | Av. K. m. 164/4 |
| Yüzde ücret ≤ %25 | ✓ / ⛔ | Av. K. m. 164/2 |
| Aynen mal/hak kaydı yok | ✓ / ⛔ | Av. K. m. 164/3 |
```

Onay: atanan ortak + Yönetici Ortak (firm-operations profili → eskalasyon matrisi).

## Hatalar

- **"Yazılı sözleşme yoksa AAÜT uygulanır"**: eksik. Para ile ölçülebilen işlerde %10-20 aralığı uygulanır, AAÜT yalnız tabandır; para ile ölçülemeyen işlerde AAÜT uygulanır (m. 164/4).
- **"%25'i aşan sözleşme batıldır"**: yanlış. Tavan miktarında geçerlidir (m. 163/2).
- **"Gerçek kişi müvekkil stopaj keser"**: yanlış genelleme. Tevkifatı GVK m. 94'te sayılan ödeyiciler yapar.
- **"Damga vergisi ödenmemiş sözleşme delil olarak kullanılamaz"**: DVK m. 24'te böyle bir kural yok; başka bir dayanak da doğrulanmadı.
- **"Her nüsha için ayrı damga"**: nispi vergide yalnız bir nüsha vergilenir (DVK m. 5).
- **Karşı taraf vekâlet ücretini müvekkil faturasından düşmek**: takas ve mahsup yasağı (m. 164/5).

Ayrıntı: `references/ucret-sozlesmesi-rehberi.md` · `references/aaut-rehberi.md`

---

## /firm-operations:kvkk-aydinlatma

---
name: kvkk-aydinlatma
description: >
  Müvekkil ilişkisi için KVKK aydınlatma metni ve dahili kontrol: işleme amaçları,
  hukuki sebep eşlemesi (m. 5 / m. 6), aktarım alıcıları, yurt dışı aktarım dayanağı
  (m. 9), VERBİS durumu (m. 16). Açık rıza gerekiyorsa aydınlatmadan ayrı alınır.
user-invocable: true
---

# KVKK Aydınlatma — Müvekkil İlişkisi

## Tetikleyici

- Yeni müvekkil intake. Aydınlatma, kişisel verinin **elde edilmesi sırasında** yapılır (KVKK m. 10).
- İşleme amacı değişti (yeni iş, yeni aktarım): yeni amaç için işlemeden önce ayrıca aydınlat (Tebliğ m. 5/1-b).
- Büro yeni bir bulut, yazılım veya yurt dışı hizmet kullanmaya başladı.

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- KİŞİSEL VERİLERİN KORUNMASI KANUNU (Kanun No. 6698, RG 07.04.2016/29677) m. 5, m. 6, m. 9, m. 10, m. 11, m. 12, m. 16
- AYDINLATMA YÜKÜMLÜLÜĞÜNÜN YERİNE GETİRİLMESİNDE UYULACAK USUL VE ESASLAR HAKKINDA TEBLİĞ (Tebliğ No. 24454, RG 10.03.2018/30356) m. 4, m. 5 — kısaca "Tebliğ"
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36

## Akış

### 1. Veri envanteri (bu iş için)

| Kategori | Örnek | Özel nitelikli mi (m. 6/1) |
|---|---|---|
| Kimlik | ad, TCKN, doğum tarihi | hayır |
| İletişim | adres, telefon, e-posta, KEP | hayır |
| Finans | banka, ücret, makbuz | hayır |
| Hukuki işlem / uyuşmazlık | olay, yazışma, belge | hayır |
| Sağlık | rapor, tıbbi belge | **evet** |
| Ceza mahkûmiyeti ve güvenlik tedbirleri | adli sicil, ceza dosyası | **evet** |
| Dernek, vakıf, sendika üyeliği; biyometrik ve genetik veri | — | **evet** |

### 2. Hukuki sebep eşlemesi

| Amaç | Hukuki sebep |
|---|---|
| Vekâlet ve ücret sözleşmesinin kurulması ve ifası | m. 5/2-c |
| Kanuni yükümlülük (MASAK kimlik tespiti, yalnız kapsamdaki işlerde; serbest meslek makbuzu) | m. 5/2-ç |
| Dava açma, savunma, hakkın korunması | m. 5/2-e |
| Özel nitelikli veri: hakkın tesisi, kullanılması veya korunması için zorunlu | m. 6/3-d |
| Başka şart yoksa | açık rıza (m. 5/1; m. 6/3-a) |

Özel nitelikli veride ayrıca Kurulun belirlediği yeterli önlemler alınır (m. 6/4).

### 3. Aydınlatma metninin asgari içeriği (KVKK m. 10; Tebliğ m. 4)

a) Veri sorumlusunun (büro / avukat) ve varsa temsilcisinin kimliği
b) İşleme amaçları: **belirli, açık, meşru**; "ve benzeri amaçlar" gibi muğlak ifade yok (Tebliğ m. 5/1-g)
c) Aktarım alıcı grupları ve aktarım amacı (Tebliğ m. 5/1-ı): mahkemeler ve icra daireleri, noterler, bilirkişi ve arabulucu, usul gereği karşı taraf ve vekili, mali müşavir, bulut ve yazılım hizmet sağlayıcıları, MASAK (yalnız 5549 kapsamındaki işlerde)
ç) Toplama yöntemi (otomatik / otomatik olmayan; Tebliğ m. 5/1-i) ve hukuki sebep, yani m. 5 veya m. 6'daki hangi şart (Tebliğ m. 5/1-h)
d) m. 11'deki haklar

Dil anlaşılır, açık ve sade olur (Tebliğ m. 5/1-ğ). Eksik, yanıltıcı veya yanlış bilgi yazılmaz (Tebliğ m. 5/1-j).

### 4. Açık rıza gerekiyorsa
Aydınlatma ve açık rıza **ayrı ayrı** alınır (Tebliğ m. 5/1-f). İkisini tek formda, tek imzayla birleştirme.

### 5. Yurt dışı aktarım kontrolü (m. 9)
Büro bulut depolama, e-posta, belge yönetimi, çeviri veya yaptırım taraması (OpenSanctions) için yurt dışındaki bir hizmete kişisel veri gönderiyorsa bu **yurt dışına aktarımdır**:
- Aktarılan ülke veya sektör için yeterlilik kararı var mı (m. 9/1-2)?
- Yoksa uygun güvence: Kurulun ilan ettiği standart sözleşme vb. (m. 9/4). Standart sözleşme imzadan itibaren **beş iş günü** içinde Kuruma bildirilir (m. 9/5).
- İkisi de yoksa yalnız arızi hâllerde aktarım yapılabilir (m. 9/6).

Büronun hangi hizmet için hangi dayanağı kullandığı `firm-profile.md`'de yazmıyorsa **"yurt dışı aktarım dayanağı belirsiz"** diye işaretle ve Yönetici Ortak'a götür. Bu paket belirli bir ülke için yeterlilik kararının varlığını doğrulamadı.

### 6. VERBİS (m. 16)
- Kural: kişisel veri işleyen gerçek ve tüzel kişiler, veri işlemeye başlamadan önce Veri Sorumluları Siciline kaydolur (m. 16/2).
- Kurul objektif kriterlerle istisna getirebilir (m. 16/2). **Avukatlara yönelik bir istisna kararının varlığı ve kapsamı bu pakette doğrulanmadı.** kvkk.gov.tr'deki sicil istisnası kararlarından kontrol et, sonucu `firm-profile.md`'ye yaz.
- Büro kayıtlıysa aydınlatmadaki bilgiler sicile bildirilen bilgilerle uyumlu olmalıdır (Tebliğ m. 5/1-ç).

### 7. İspat
- Aydınlatmanın yapıldığını ispat yükü veri sorumlusundadır (Tebliğ m. 5/1-e). İmzalı nüsha, e-posta gönderim kaydı veya KEP alındısını matter dosyasına koy.
- Aydınlatma müvekkilin talebine bağlı değildir (Tebliğ m. 5/1-d).

### 8. Güvenlik ve ihlal
- Veri sorumlusu uygun güvenlik düzeyi için teknik ve idari tedbir almak zorundadır (m. 12/1). Veriyi büro adına işleyen (ör. bulut sağlayıcı) ile tedbirlerden müştereken sorumludur (m. 12/2).
- Veriler kanuni olmayan yollarla başkalarınca elde edilirse veri sorumlusu durumu **en kısa sürede** ilgiliye ve Kurula bildirir (m. 12/5). Uygulamada anılan "72 saat" süresi bir Kurul kararına dayanır; kararın künyesi bu pakette doğrulanmadı.
- Mesleki sır (Av. K. m. 36) KVKK'dan bağımsız olarak geçerlidir. Aydınlatma metni sır saklama yükümlülüğünü daraltan bir ifade içermez.

## Çıktı

İki belge:
1. **Müvekkile verilecek aydınlatma metni** (sade dil, 1-2 sayfa)
2. **Dahili kontrol notu:**

```markdown
[ÜST BAŞLIK — KVKK AYDINLATMA KONTROLÜ — DAHİLİ]
Müvekkil: [takma ad] — Tarih: GG.AA.YYYY
- Özel nitelikli veri: var / yok → hukuki sebep: [...]
- Açık rıza gerekiyor mu: hayır / evet (ayrı form)
- Yurt dışı aktarım: yok / var → dayanak: [yeterlilik kararı / standart sözleşme (Kuruma bildirim tarihi) / belirsiz]
- VERBİS: kayıtlı / istisna (karar künyesi) / belirsiz
- Aydınlatma ispat kaydı: [imzalı nüsha / KEP / e-posta]
```

## Hatalar

- Aydınlatma ile açık rızayı tek metinde ve tek imzayla almak (Tebliğ m. 5/1-f)
- "Kanunen gereken her türlü amaçla" gibi genel amaç yazmak (Tebliğ m. 5/1-g)
- Yurt dışındaki bulutu aktarım saymamak (m. 9)
- VERBİS istisnasını doğrulamadan varsaymak

Ayrıntı: `references/kvkk-m11-cevap-sablonu.md` (ilgili kişi başvurusu) · `references/mesleki-sir-rehberi.md`

---

## /firm-operations:masak-kontrol

---
name: masak-kontrol
description: >
  5549 sayılı Kanun ve Tedbirler Yönetmeliği uyarınca kapsam testi (serbest avukat
  yalnız sayılan finansal işlemlerde yükümlüdür), kimlik tespiti, gerçek faydalanıcı,
  sıkılaştırılmış tedbir, şüpheli işlem değerlendirmesi ve sekiz yıllık muhafaza.
  Sonuç: KAPSAM DIŞI / ✓ TAMAM / 🟠 İNCELE / ⛔ İŞLEM YOK.
user-invocable: true
---

# MASAK Kontrol — Müşterinin Tanınması

## Tetikleyici

- `/firm-operations:conflict-check` sonrasında, iş kabulünden önce
- Mevcut işte avukatın müvekkil adına bir finansal işlemi gerçekleştirmesi gündeme geldiğinde
- Önceki kimlik bilgilerinin yeterliliğinden veya doğruluğundan şüphe doğduğunda

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- SUÇ GELİRLERİNİN AKLANMASININ ÖNLENMESİ HAKKINDA KANUN (Kanun No. 5549, RG 18.10.2006/26323) m. 2, m. 3, m. 4, m. 8, m. 13, m. 14
- SUÇ GELİRLERİNİN AKLANMASININ VE TERÖRÜN FİNANSMANININ ÖNLENMESİNE DAİR TEDBİRLER HAKKINDA YÖNETMELİK (Cumhurbaşkanlığı / Bakanlar Kurulu Yönetmeliği No. 200713012, RG sayı 26751) m. 4, m. 5, m. 6, m. 7, m. 17/A, m. 22, m. 26/A, m. 28, m. 29 — kısaca "Yön."
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 35, m. 36
- TÜRK CEZA KANUNU (Kanun No. 5237, RG sayı 25611) m. 282

⚠️ **MALİ SUÇLARI ARAŞTIRMA KURULU GENEL TEBLİĞİ (SIRA NO: 5) (Tebliğ No. 12073, RG 09.04.2008/26842)** avukat yükümlülüğünün dayanağı **değildir**. Konusu, Yönetmelik m. 26 uyarınca **basitleştirilmiş tedbirlerdir** (metnin ilk sayfası 24.09.2026'da okundu). Serbest avukatlar 5549'a 2008'de değil, 7262 sayılı Kanunla (2020) girdi; bu hüküm AYM'nin 18.01.2024 tarihli, E. 2021/28, K. 2024/11 sayılı kararıyla iptal edildi, bugünkü metin 7521 sayılı Kanunla (2024) geldi (5549 m. 2 dipnotları).

## Akış

### 1. Kapsam testi (5549 m. 2/1-d; Yön. m. 4/1-ş)
Serbest avukat **yalnız** şu işlere ilişkin **finansal işlemlerin gerçekleştirilmesiyle** sınırlı olarak yükümlüdür:
- taşınmaz alım satımı
- sınırlı ayni hak kurulması ve kaldırılması
- şirket, vakıf ve dernek kurulması, birleştirilmesi, idaresi, devredilmesi ve tasfiyesi
- banka, menkul kıymet ve her türlü hesap ile bu hesaplardaki varlıkların idaresi

**Hariç:** Av. K. m. 35'in birinci ve üçüncü fıkrası ile alternatif uyuşmazlık çözüm yolları kapsamında yürütülen mesleki faaliyetler sırasında edinilen bilgiler. Yükümlülük savunma hakkı ve hukuki dinlenilme hakkı bakımından diğer kanunlara aykırı olamaz; yalnız avukatların yapabileceği işlerde Av. K. m. 36 (sır saklama) saklıdır.

| Sonuç | Karar |
|---|---|
| İş, yukarıdaki finansal işlemleri **gerçekleştirmeyi** içermiyor (dava vekilliği, mütalaa, sözleşme incelemesi, arabuluculuk) | **KAPSAM DIŞI**: gerekçeyi yaz, `/firm-operations:sanctions-check` ile devam et |
| İçeriyor | 2. adıma geç |
| Belirsiz (ör. şirket kuruluşunda sermaye hesabını avukat mı yönetecek?) | 🟠 İNCELE → Yönetici Ortak |

Kapsam dışı iş için de büro politikası temel kimlik kaydı isteyebilir. Bu 5549 yükümlülüğü değil, büro kuralıdır (`firm-profile.md`).

### 2. Kimlik tespiti ne zaman yapılır (Yön. m. 5)
- Sürekli iş ilişkisi kurulurken **tutar gözetmeksizin** (m. 5/1-a)
- İşlem tutarı veya birbiriyle bağlantılı işlemlerin toplamı Yönetmelikteki eşiğe ulaşınca (m. 5/1-b). 24.09.2026 metninde eşik 185.000 TL'dir; eşik Cumhurbaşkanı kararlarıyla değişir, her kullanımda güncel metni çek.
- Şüpheli işlem bildirimini gerektiren durumlarda tutar gözetmeksizin (m. 5/1-d)
- Önceki kimlik bilgilerinin yeterliliğinden veya doğruluğundan şüphe varsa tutar gözetmeksizin (m. 5/1-e)

Tespit **iş ilişkisi kurulmadan veya işlem yapılmadan önce** tamamlanır (m. 5/2). Sürekli iş ilişkisinde ilişkinin amacı ve mahiyeti hakkında bilgi alınır (m. 5/3).

### 3. Kimlik bilgileri ve teyit

**Gerçek kişi (Yön. m. 6):** ad, soyad, doğum tarihi, uyruk, kimlik belgesinin türü ve numarası, adres, imza örneği, iş ve meslek bilgisi, varsa telefon, faks ve e-posta; Türk vatandaşı için TCKN, yabancı için doğum yeri.
- Teyit belgesi: Türk uyruklu için nüfus cüzdanı, sürücü belgesi veya pasaport (ve TCKN taşıyan, özel kanununda resmi kimlik hükmünde sayılan belgeler); yabancı için pasaport, ikamet belgesi veya Bakanlıkça uygun görülen belge (m. 6/2).
- Belgenin aslı veya noter onaylı sureti görülür; okunabilir fotokopisi veya elektronik görüntüsü alınır ya da bilgiler kaydedilir (m. 6/2).
- Sürekli iş ilişkisinde adres teyidi: yerleşim yeri belgesi, son üç ay içinde düzenlenmiş abonelik faturası, kamu kurumu belgesi vb. (m. 6/3).

**Ticaret siciline kayıtlı tüzel kişi (Yön. m. 7):** unvan, ticaret sicil numarası, vergi kimlik numarası, faaliyet konusu, açık adres, telefon, varsa faks ve e-posta; ayrıca temsile yetkili kişinin kimlik bilgileri ve imza örneği.
- Teyit: unvan, sicil numarası, faaliyet konusu ve adres için tescil belgeleri; vergi kimlik numarası için Gelir İdaresi belgeleri; temsil yetkisi için tescil belgeleri (m. 7/2-3).

**Gerçek faydalanıcı (Yön. m. 17/A):**
- Tüzel kişiliğin **%25'ini aşan** hisseye sahip gerçek kişi ortaklar (m. 17/A/2). Ölçüt "%25 ve üzeri" değildir.
- Bu ortağın gerçek faydalanıcı olmadığından şüphe varsa ya da böyle bir ortak yoksa: tüzel kişiyi nihai olarak kontrol eden gerçek kişi veya kişiler (m. 17/A/3).
- Yine tespit edilemezse: ticaret sicilinde kayıtlı en üst düzey icra yetkisine sahip gerçek kişi veya kişiler "üst düzey yönetici" sıfatıyla (m. 17/A/4).
- %25'i aşan hisseye sahip **tüzel kişi** ortakların kimliği de m. 7'ye göre tespit edilir (m. 17/A/7). Kimlik bilgilerini içeren noter onaylı imza sirküleri kullanılabilir (m. 17/A/6).

### 4. Yüksek risk: sıkılaştırılmış tedbirler (Yön. m. 26/A)
Risk temelli yaklaşımla yüksek riskli bulunan durumda, riskle orantılı olarak şunların biri, birkaçı veya tamamı uygulanır: müşteri ve gerçek faydalanıcı hakkında ilave bilgi ve daha sık güncelleme; iş ilişkisinin mahiyeti hakkında ilave bilgi; işleme konu malvarlığının ve fonların kaynağı hakkında bilgi; işlemin amacı; iş ilişkisinin **üst seviyedeki görevlinin onayına** bağlanması (büroda Yönetici Ortak); sıkı gözetim.

Uygulama örnekleri (mevzuat listesi değildir): karmaşık veya yurt dışı ortaklık zinciri, siyasi nüfuz sahibi kişi bağlantısı, nakit yoğun işlem, müvekkilin profiline uymayan işlem büyüklüğü.

### 5. Tespit yapılamıyorsa (Yön. m. 22)
Kimlik tespiti yapılamıyor ya da iş ilişkisinin amacı hakkında yeterli bilgi edinilemiyorsa **iş ilişkisi kurulmaz, talep edilen işlem yapılmaz** (m. 22/1). Önceki bilgilerden şüphe nedeniyle gereken teyit yapılamazsa iş ilişkisi **sona erdirilir** (m. 22/2). İki hâlin şüpheli işlem olup olmadığı ayrıca değerlendirilir (m. 22/3).

### 6. Şüpheli işlem değerlendirmesi
- **Ölçüt:** işleme konu malvarlığının yasa dışı yollardan elde edildiğine veya yasa dışı amaçla kullanıldığına dair **bilgi, şüphe veya şüpheyi gerektirecek bir husus** (5549 m. 4/1).
- **Süre:** şüphenin oluştuğu tarihten itibaren **en geç on iş günü** içinde Başkanlığa bildirim (Yön. m. 28/2).
- **Açıklama yasağı:** bildirimde bulunulduğu veya bulunulacağı, yükümlülük denetimi yapan denetim elemanları ve yargılamadaki mahkemeler dışında, **müvekkil dahil hiç kimseye** açıklanmaz (5549 m. 4/2; Yön. m. 29/1). Yasak, bildirime herhangi bir şekilde vakıf olan tüm personeli kapsar (Yön. m. 29/2). İhlalin cezası bir yıldan üç yıla kadar hapis ve beş bin güne kadar adli para cezasıdır (5549 m. 14/1).
- Bildirim yükümlülüğünü yerine getiren hukuki ve cezai bakımdan sorumlu tutulamaz (Yön. m. 29/4).
- Bilgi, Av. K. m. 35'in birinci veya üçüncü fıkrasındaki faaliyetten ya da alternatif uyuşmazlık çözüm yolu faaliyetinden edinildiyse yükümlülük dışındadır (5549 m. 2/1-d).
- Karar: büroda bu işi yürüten kişi (`firm-profile.md` → MASAK sorumlusu) + Yönetici Ortak. Avukatlar için uyum görevlisi atama zorunluluğu bu pakette doğrulanmadı. Değerlendirme notu matter klasörüne değil, **erişimi kısıtlı uyum kaydına** yazılır.

### 7. Muhafaza (5549 m. 8)
Belgeler düzenleme tarihinden, defter ve kayıtlar son kayıt tarihinden, **kimlik tespitine ilişkin belgeler son işlem tarihinden** itibaren **sekiz yıl** saklanır ve istenirse yetkililere ibraz edilir. Matter'ın kapanması süreyi başlatmaz; son işlem tarihine bak. Muhafaza yükümlülüğünün ihlali de adli cezaya tabidir (5549 m. 14/1).

### 8. Yaptırım (bilgi)
- 5549 m. 3 ve m. 6 yükümlülüklerinin ihlali ile m. 4/1 ihlali: idari para cezası (5549 m. 13/1). Tutarlar metinde yazılıdır; güncel tutarı her kullanımda çek.
- 5549 m. 4/2, m. 7 ve m. 8 ihlali: adli ceza (5549 m. 14/1).
- Aklama suçu TCK m. 282'dedir. Suçun belli bir meslek sahibi tarafından mesleğin icrası sırasında işlenmesi hâlinde hapis cezası yarı oranında artırılır (m. 282/3).

## Çıktı

```markdown
[ÜST BAŞLIK — MASAK KONTROL NOTU — DAHİLİ]

# MASAK Kontrol — [Müvekkil takma adı] — GG.AA.YYYY

## Kapsam (5549 m. 2/1-d)
KAPSAM DIŞI / KAPSAMDA — gerekçe: [iş türü]

## Kimlik tespiti (kapsamdaysa)
- Tip: gerçek / tüzel
- Teyit belgesi: [tür] — aslı veya noter sureti görüldü: evet / hayır
- Gerçek faydalanıcı: [takma ad] — yöntem: %25'i aşan pay / nihai kontrol / üst düzey yönetici
- Sıkılaştırılmış tedbir: gerekmedi / uygulandı: [hangileri] — onay: [Yönetici Ortak]

## Sonuç
✓ TAMAM / 🟠 İNCELE / ⛔ İŞLEM YOK (Yön. m. 22)
Muhafaza bitişi: son işlem + 8 yıl (5549 m. 8)
```

Şüpheli işlem değerlendirmesi bu notta **yer almaz**; uyum kaydına ayrı yazılır.

## Hatalar

- **Dava vekilliğini kapsam içi saymak**: avukat yalnız sayılan finansal işlemlerde yükümlüdür (5549 m. 2/1-d).
- **Kapsamdaki işte "ben sadece danışmanım" demek**: finansal işlemi avukat gerçekleştiriyorsa iş kapsam içidir.
- **5 yıl saklamak**: süre sekiz yıldır (5549 m. 8).
- **"%25 ve üzeri" pay**: ölçüt %25'i **aşan** paydır (Yön. m. 17/A/2).
- **Müvekkile "sizi bildirdik" demek**: 5549 m. 4/2 ve m. 14/1.
- **MASAK Genel Tebliği (Sıra No: 5)'i dayanak göstermek**: konusu basitleştirilmiş tedbirlerdir.

Ayrıntı: `references/masak-kimlik-tespit-rehberi.md`

---

## /firm-operations:matter-open

---
name: matter-open
description: >
  Kabul kararından sonra matter kaydını açar: ön koşul kapısı (conflict, MASAK,
  sanctions, KVKK, ücret, vekâlet), matter-slug, klasör ve erişim düzeni, süre takvimi,
  vekâletname ibrazı ve ilgili plugin'e devir.
user-invocable: true
---

# Matter Open — Dosya Açılışı

## Tetikleyici

Kabul kararı verildikten sonra (rutin dosyada atanan ortak + Yönetici Ortak; 🟠 dosyada Ortaklar Kurulu).

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36, m. 171, m. 174
- HUKUK MUHAKEMELERİ KANUNU (Kanun No. 6100, RG sayı 27836) m. 76, m. 77
- KİŞİSEL VERİLERİN KORUNMASI KANUNU (Kanun No. 6698, RG 07.04.2016/29677) m. 9, m. 12
- SUÇ GELİRLERİNİN AKLANMASININ ÖNLENMESİ HAKKINDA KANUN (Kanun No. 5549, RG 18.10.2006/26323) m. 4, m. 8

## Akış

### 1. Ön koşul kapısı

| Adım | Aranan kayıt | Eksikse |
|---|---|---|
| `/firm-operations:conflict-check` | ✓ TEMİZ ya da 🟠 + Ortaklar Kurulu kararı | ⛔ **açma**; istisnası yok |
| `/firm-operations:masak-kontrol` | KAPSAM DIŞI ya da ✓ TAMAM | ⛔ kapsamdaysa açma (Yön. m. 22) |
| `/firm-operations:sanctions-check` | ✓ TEMİZ ya da karar kaydı | ⛔ |
| `/firm-operations:kvkk-aydinlatma` | ispat kaydı | 🟠 aç, ilk yazışmada tamamla |
| `/firm-operations:fee-agreement` | imzalı sözleşme | 🟠 peşin ücret ödenmediyse avukat işe başlamak zorunda değil (Av. K. m. 174/3) |
| `/firm-operations:vekalet-sablon` | vekâletname | dava işinde bkz. adım 5 |

### 2. matter-slug
`<müvekkil-slug>__<konu-slug>__<yyyy>`. Yalnız takma ad kullanılır; gerçek isim, TCKN veya VKN slug'a girmez. Örnek: `mv-ay-insaat__kira-tahliye__2026`.

### 3. Klasör düzeni
`pre-matter/<tarih>__<müvekkil-takma-ad>/` içeriği `matters/<müvekkil-slug>__<matter-slug>/` altına taşınır:

```
00-intake/          intake notu, conflict sonucu
01-uyum/            MASAK ve sanctions notları (erişim: atanan ortak + Yönetici Ortak)
02-sozlesme/        ücret sözleşmesi, KVKK aydınlatma ispatı
03-vekalet/         vekâletname, yetki belgesi
04-yazisma/
05-taslak/
06-delil/
07-karar-tebligat/
```

Şüpheli işlem değerlendirmesi **hiçbir** matter klasörüne girmez (5549 m. 4/2, açıklama yasağı); ayrı ve kısıtlı uyum kaydında durur.

### 4. Erişim ve sır
- Erişim yalnız atanan ekipte olur. Conflict-check 🟠 ile açılan dosyada ayrı erişim grubu kurulur (ethical wall).
- Avukat, görevi dolayısıyla öğrendiklerini açığa vuramaz (Av. K. m. 36). Klasör paylaşım bağlantısı "herkese açık" olamaz.
- Veri güvenliği için teknik ve idari tedbir alınır (KVKK m. 12/1). Bulut sağlayıcı yurt dışındaysa m. 9 dayanağı `/firm-operations:kvkk-aydinlatma` kaydında yer almalıdır.

### 5. Dava veya takip işi: vekâletname
- Avukat, açtığı veya takip ettiği iş için noter onaylı ya da düzenlenmiş vekâletname aslını veya avukat onaylı örneğini dosyaya ibraz eder (HMK m. 76/1).
- Vekâletnamesiz dava açılamaz, işlem yapılamaz. Gecikmede zarar doğabilecek hâlde mahkeme kesin süre vererek izin verebilir; süre içinde vekâletname getirilmezse dava açılmamış veya işlem yapılmamış sayılır (HMK m. 77/1). Acil dosyada vekâletname tarihini takvime **ilk** kalem olarak gir.

### 6. Süre takvimi
- intake'teki aciliyet etiketiyle birlikte dosyadaki her kesin süre, zamanaşımı ve hak düşürücü süre takvime girer; iki kişi (avukat + asistan) kontrol eder.
- Süre hesabı ilgili plugin'in skill'inde yapılır; burada yalnız kayıt açılır.

### 7. Muhafaza etiketi
- MASAK kapsamındaki işte: son işlem + sekiz yıl (5549 m. 8).
- Diğer saklama süreleri (vergi, meslek kuralları) bu pakette doğrulanmadı; `firm-profile.md`'deki büro politikası uygulanır.

### 8. Devir
`/firm-operations:new-client-intake`'teki yönlendirme tablosuna göre ilgili plugin'e geç: dava için `/litigation-legal:case-intake`; diğer işlerde ilgili plugin'in skill listesi (profil boşsa önce o plugin'in `cold-start-interview`'u). Avukat, üzerine aldığı işi yazılı sözleşme olmasa bile sonuna kadar takip eder (Av. K. m. 171/1).

## Çıktı

```markdown
[ÜST BAŞLIK — MATTER AÇILIŞ KAYDI — DAHİLİ]

# [matter-slug] — açılış GG.AA.YYYY
- Atanan ortak / ekip: [...]
- Ön koşullar: conflict ✓ · MASAK [KAPSAM DIŞI / ✓] · sanctions ✓ · KVKK ✓ · ücret ✓ · vekâlet ✓ / bekliyor
- Erişim grubu: [...] — ethical wall: yok / var
- İlk 3 süre: [tarih — iş — kaynak]
- Muhafaza: [son işlem + 8 yıl / büro politikası]
- Devir: [/plugin:skill]
```

## Hatalar

- Conflict-check olmadan klasör açmak
- Slug'a gerçek isim yazmak
- Uyum notlarını, özellikle şüpheli işlem değerlendirmesini, matter klasörüne koymak
- Vekâletname gelmeden işlem yapıp HMK m. 77'deki kesin süreyi takvime yazmamak

---

## /firm-operations:monthly-billing

---
name: monthly-billing
description: >
  Ay sonu matter bazlı ücret hesabı ve tahsilat takibi: süre kayıtları × ücret modeli,
  AAÜT tabanı ve %25 tavanı, karşı taraf vekâlet ücretinin ayrı tutulması, serbest meslek
  makbuzu, tevkifat kontrolü, geç ödemede temerrüt ve faiz.
user-invocable: true
---

# Monthly Billing — Aylık Ücret ve Tahsilat

## Tetikleyici

Ay sonu. Ayrıca yüzde ücretin muaccel olduğu an (sözleşmedeki şarta göre: karar kesinleşti, tahsil edildi vb.).

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36, m. 164, m. 166, m. 174
- VERGİ USUL KANUNU (Kanun No. 213, RG sayı 10705) m. 236
- GELİR VERGİSİ KANUNU (GVK) (Kanun No. 193, RG sayı 10700) m. 94
- TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG sayı 27836) m. 117, m. 120
- KANUNİ FAİZ VE TEMERRÜT FAİZİNE İLİŞKİN KANUN (Kanun No. 3095, RG sayı 18610) m. 1, m. 2
- TÜRK TİCARET KANUNU (Kanun No. 6102, RG sayı 27846) m. 1530

## Akış

### 1. Liste
Aktif matter'lar ve her birinin `/firm-operations:fee-agreement` kaydındaki ücret modeli ile ödeme takvimi.

### 2. Tutar

| Model | Hesap | Kontrol |
|---|---|---|
| Saatlik | onaylı süre kaydı × oran | açıklamada sır içeren ayrıntı yok |
| Sabit / sürekli danışmanlık | sözleşmedeki aylık tutar | kapsam dışı iş ayrı faturalanır |
| Aşama | aşama gerçekleştiyse aşama tutarı | aşamanın kanıtı (karar, tutanak) |
| Yüzde | sözleşmedeki şart gerçekleştiyse değer × oran | **%25 tavanı** (Av. K. m. 164/2) |

Her matter için ücretin AAÜT altında kalmadığını kontrol et (Av. K. m. 164/4).

### 3. Karşı taraf vekâlet ücreti
Kararla karşı tarafa yüklenen vekâlet ücreti avukata aittir; iş sahibinin borcu nedeniyle **takas ve mahsup edilmez** (Av. K. m. 164/5). Müvekkil faturasına indirim kalemi olarak yazma, ayrı izle.

### 4. Belge
- Her tahsilat için **iki nüsha serbest meslek makbuzu** düzenlenir, bir nüshası müvekkile verilir (VUK m. 236). Elektronik makbuz (e-SMM) usulü bu pakette doğrulanmadı; muhasebeciyle teyit et.
- Makbuz ve fatura açıklaması genel kalır ("hukuki danışmanlık — Eylül 2026"). Dosya içeriği, karşı taraf adı veya strateji yazılmaz (Av. K. m. 36).

### 5. Tevkifat ve KDV
- Ödeyici GVK m. 94'te sayılanlardan biriyse (ör. ticaret şirketi, kamu idaresi, gerçek gelirini beyan eden ticaret veya serbest meslek erbabı) ödeme sırasında tevkifat yapar; makbuzda brüt, tevkifat ve net ayrı gösterilir. Olağan bireysel müvekkil tevkifat yapmaz.
- Tevkifat ve KDV **oranları** doğrulanmadı: `[ORAN — doğrulanmadı]` yaz. Muhasebeci onayı olmadan paket gönderilmez.

### 6. Tahsilat takibi ve temerrüt
- **Temerrüt:** muaccel borçta alacaklının ihtarıyla; ifa günü birlikte belirlenmişse o günün geçmesiyle (TBK m. 117). Sözleşmeye ödeme günü yaz; böylece ihtar gerekmez.
- **Oran:** sözleşmede yoksa faiz borcunun doğduğu tarihteki mevzuata göre belirlenir. Sözleşmeyle kararlaştırılan temerrüt faizi, mevzuattaki oranın **%100 fazlasını** aşamaz (TBK m. 120/1-2).
- **Mevzuattaki oran:** kanuni faiz, TCMB'nin önceki yılın 31 Aralık günü kısa vadeli kredi işlemlerinde uyguladığı reeskont oranının **%80'idir** (3095 m. 1, 16.07.2026 tarihli 7589 sayılı Kanunla değişik). Temerrüt faizi de bu orana göre işler (3095 m. 2/1). Güncel oranı her hesapta TCMB duyurusundan çek.
- **Ticari işlerde avans oranı** (3095 m. 2/2) ve **TTK m. 1530** (ticari işletmeler arasında mal ve hizmet tedarikinde geç ödeme; ihtarsız temerrüt, 30 günlük süreler): avukatlık ücret alacağının "ticari iş" ya da "ticari işletmeler arası tedarik" sayılıp sayılmadığı bu pakette **doğrulanmadı**. Uygulamadan önce içtihatla doğrula; doğrulanmadıysa TBK m. 117-120 ve 3095 m. 1 ile m. 2/1'e göre hesapla.

### 7. Ücret güvenceleri
- Peşin ücret ödenmezse avukat işe başlamak zorunda değildir (Av. K. m. 174/3).
- Hapis hakkı ve rüçhan (Av. K. m. 166).
- Ödenmeyen ücret için dava veya takip kararı: atanan ortak + Yönetici Ortak.

## Çıktı

```markdown
[ÜST BAŞLIK — AYLIK ÜCRET PAKETİ — DAHİLİ — GG.AA.YYYY]

| Matter | Model | Bu ay | AAÜT kontrolü | Tevkifat | Makbuz | Vade | Durum |
|---|---|---|---|---|---|---|---|
| [slug] | saatlik | [TL] | ✓ | evet / hayır | [no] | GG.AA | ödendi / bekliyor / temerrüt |

## Temerrüt uyarıları
- [slug] — vade GG.AA — ihtar: gerekli / gerekmez (TBK m. 117) — faiz esası: [3095 m. 1 ve m. 2/1 | sözleşme]

## Doğrulanmamış kalemler
- [oran / e-SMM / ticari iş niteliği]
```

## Hatalar

- Karşı taraf vekâlet ücretini müvekkilin ücret borcundan düşmek (Av. K. m. 164/5)
- Yüzde ücreti %25 tavanını aşan oranla hesaplamak
- Her müvekkilin tevkifat yapacağını varsaymak
- TTK m. 1530'u doğrulamadan avukatlık ücretine uygulamak
- Makbuz açıklamasına dosya ayrıntısı yazmak

---

## /firm-operations:new-client-intake

---
name: new-client-intake
description: >
  Yeni müvekkil ön sohbet sonrası intake akışı: müvekkil bilgisi alma, talep
  özeti, matter tipi belirleme + plugin yönlendirmesi, aciliyet kontrolü, sonraki
  zorunlu adımlar (conflict-check, MASAK, sanctions, KVKK, fee, vekalet) tetikleme.
user-invocable: true
---

# New Client Intake — Yeni Müvekkil Ön Sohbet

## Tetikleyici

İlk temas (telefon / web / referans) sonrası, atanan ortak müvekkille ön sohbeti yaptıktan sonra.

## Adımlar

### 1. Müvekkil bilgisi

**Gerçek kişi:**
- Takma ad (kayıt için — gerçek isim KVKK uyarınca minimum)
- TC kimlik no (kimlik tespit için sonradan MASAK)
- Telefon + e-posta (mümkünse KEP)
- Meslek + işveren

**Tüzel kişi:**
- Ünvan (kısaltılmış takma ad)
- Vergi no + MERSİS no
- Faaliyet alanı (NACE)
- Yetkili temsilci
- KEP adresi

### 2. Talep özeti

- 1-2 cümle özet
- Karşı taraf var mı?
- Tahmini değer
- Tarih + süreler (aciliyet kontrolü)

### 3. Matter tipi → plugin yönlendirmesi

| Talep | Plugin |
|---|---|
| Müvekkil davacı/davalı (ticari/medeni) | `litigation-legal` |
| Müvekkil idari kararı iptal | `administrative-legal` |
| Müvekkil vergi tarhiyatı iptal | `tax-legal` |
| Müvekkil ceza şüphelisi/sanığı | `criminal-defense` |
| Müvekkil sözleşme yazımı/inceleme | `commercial-legal` |
| Müvekkilin GK/YK/M&A işlemi | `corporate-legal` |
| Müvekkil işveren/işçi iş hukuku | `employment-legal` |
| Müvekkilin marka/patent/tasarım | `ip-legal` |
| Veri koruma / KVKK | `privacy-legal` |
| Düzenleyici kurum / lisans | `regulatory-legal` |
| Enerji M&A / proje finansmanı | `energy-finance` |
| Aile/miras/boşanma | **KAPSAM DIŞI** — başka büroya yönlendir |

### 4. Aciliyet kontrolü

| Süre durumu | Etiket |
|---|---|
| Dava süresi < 7 gün | 🔴 ACİL |
| Dava süresi < 30 gün | 🟠 Yüksek |
| Sözleşme imza < 3 gün | 🟠 Yüksek |
| Tutuklu müvekkil (ceza) | 🔴 ACİL — 48 saat sınırı |
| Süre kritik değil | 🟢 Standart akış |

### 5. Sonraki zorunlu adımlar listesi

```
ZORUNLU SONRAKI ADIMLAR:
[ ] /firm-operations:conflict-check   ← İLK + KRİTİK
[ ] /firm-operations:masak-kontrol    (önce kapsam testi: dava vekilliği çoğunlukla KAPSAM DIŞI)
[ ] /firm-operations:sanctions-check
[ ] /firm-operations:kvkk-aydinlatma
[ ] /firm-operations:fee-agreement
[ ] /firm-operations:vekalet-sablon
[ ] /firm-operations:matter-open
```

## Çıktı

```markdown
[ÜST BAŞLIK — INTAKE NOTU — DAHİLİ]

# Müvekkil Intake — [Takma ad] — [Tarih]

## ⚠️ İnceleyen notu
- Aciliyet: 🔴/🟠/🟢
- Önerilen plugin: [...]
- Sonraki zorunlu adımlar: 7 adım

## Müvekkil
- Tip: Bireysel / Tüzel kişi
- Takma ad: [...]

## Talep özeti
[1-2 cümle]

## Matter tipi
[Plugin]: [...] — gerekçe

## Aciliyet
🔴/🟠/🟢 — [neden]

## Sonraki ZORUNLU adımlar
1. /firm-operations:conflict-check (İLK)
2. /firm-operations:masak-kontrol
3. /firm-operations:sanctions-check
4. /firm-operations:kvkk-aydinlatma
5. /firm-operations:fee-agreement
6. /firm-operations:vekalet-sablon
7. /firm-operations:matter-open
```

## Hatalar

- **Müvekkilin gerçek ismini intake notuna yazma** — takma ad kullan
- **Conflict check tetiklenmeden iş başlatma** — Av. K. m. 38 ihlal riski
- **KAPSAM DIŞI matter'ı kabul etme** — yetersiz hizmet riski

---

## /firm-operations:sanctions-check

---
name: sanctions-check
description: >
  Müvekkil, temsilciler, gerçek faydalanıcılar ve (biliniyorsa) karşı taraf için yaptırım
  ve PEP taraması. OpenSanctions sonucunu ve Türk hukukundaki malvarlığı dondurma
  kararlarını (6415, 7262) ayrı raporlar. Sonuç: ✓ TEMİZ / 🟠 İNCELE / ⛔ HIT.
user-invocable: true
---

# Sanctions Check — Yaptırım Taraması

## Tetikleyici

- `/firm-operations:masak-kontrol` sonrasında (gerçek faydalanıcı listesi hazırken)
- Yabancı bağlantılı müvekkil veya karşı taraf
- Ödemeyi üçüncü bir kişi yapacaksa
- Uzun süren işte periyodik tekrar (`firm-profile.md`'deki sıklık)

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- TERÖRİZMİN FİNANSMANININ ÖNLENMESİ HAKKINDA KANUN (Kanun No. 6415, RG 16.02.2013/28561) m. 5, m. 6, m. 7
- KİTLE İMHA SİLAHLARININ YAYILMASININ FİNANSMANININ ÖNLENMESİNE İLİŞKİN KANUN (Kanun No. 7262, RG 31.12.2020/31351 (Mükerrer)) m. 1, m. 3
- KİŞİSEL VERİLERİN KORUNMASI KANUNU (Kanun No. 6698, RG 07.04.2016/29677) m. 9
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36

## Türk hukukunda dondurma kararları nereden gelir

| Kaynak | Mekanizma | Dayanak |
|---|---|---|
| BMGK 1267 (1999), 1988 (2011), 1989 (2011) ve 2253 (2015) sayılı kararlarla listelenenler | Cumhurbaşkanı kararı Resmî Gazete'de yayımlanır, gecikmeksizin uygulanır | 6415 m. 5/1 |
| Yabancı devlet hükümetinin talebi | Değerlendirme Komisyonu değerlendirir, Cumhurbaşkanı karara bağlar; karşılıklılık gözetilir | 6415 m. 6/1 |
| Türkiye'deki malvarlığı (mahkemelerce terör örgütü olduğuna kesin karar verildikten sonra) | Komisyon önerisiyle Hazine ve Maliye Bakanı ile İçişleri Bakanı birlikte karar verir; karar 48 saat içinde Ankara ağır ceza mahkemesinin onayına sunulur | 6415 m. 7/3-4 |
| BMGK'nın kitle imha silahlarının yayılmasının finansmanına ilişkin kararları | Cumhurbaşkanı kararı Resmî Gazete'de yayımlanır; nihai listeler ilgili kurumların internet sitelerinde yayımlanır | 7262 m. 3/1, m. 3/3 |

AB, ABD (OFAC) ve Birleşik Krallık listeleri 6415 m. 5 ile 7262 m. 3'teki BMGK mekanizmasının parçası değildir. Yabancı devlet talebi için 6415 m. 6 yolu vardır; bu listelerin Türkiye'de doğrudan sonuç doğurduğu başka bir yol bu pakette doğrulanmadı. Yine de müvekkilin bankaları ve yabancı karşı tarafları bakımından iş ve itibar riski taşırlar; raporda **ayrı satırda** göster.

## Akış

### 1. Taranacaklar
- Müvekkil. Gerçek kişide ad, doğum yılı, uyruk; tüzel kişide unvan, ülke, sicil numarası.
- Tüzel müvekkilde temsilciler ve `masak-kontrol`'deki gerçek faydalanıcılar
- Karşı taraf (biliniyorsa) ve ödemeyi yapacak üçüncü kişi

### 2. Veri en azı ve sır
- Sorguya **yalnız tarama için gereken alanlar** girer. İşin konusu, dosya özeti, karşı tarafla ilişki ve talep **gönderilmez** (Av. K. m. 36).
- OpenSanctions yurt dışında bir hizmettir; ona kişisel veri göndermek **yurt dışına aktarımdır** (KVKK m. 9). Büronun bu aktarım için dayanağı `/firm-operations:kvkk-aydinlatma` kaydında yoksa gerçek kişi taramasını durdur: 🟠 İNCELE → Yönetici Ortak.

### 3. OpenSanctions
- Çağrı kalıbı: `references/opensanctions-rehberi.md` (match API, `default` kapsam, curl ile).
- Anahtar `OPENSANCTIONS_API_KEY` ortam değişkenindedir; pakette yoktur. Değişken tanımlı değilse API çağrısı yapma, rehberdeki manuel kaynaklarla (OpenSanctions web araması dahil) tara. Anahtarı hiçbir çıktıya, nota, dosyaya veya sohbet metnine yazma.
- Skor 0 ile 1 arasındadır (OpenSanctions dokümanı). Yorum: ≥ 0,90 → ⛔; 0,70-0,90 → 🟠, ayırt edici bilgilerle (doğum tarihi, uyruk, sicil numarası) teyit et; < 0,70 → ✓, kaydet.
- Yalnız ad benzerliğiyle hüküm kurma. Eşleşen kaydın doğum tarihi, uyruk ve sicil bilgisini müvekkilinkiyle karşılaştır.

### 4. Türk listeleri
6415 ve 7262 kapsamında yayımlanan kararları ve 7262 m. 3/3 uyarınca kurum sitelerinde yayımlanan nihai listeleri elle kontrol et; kontrol tarihini ve kaynağı yaz. OpenSanctions'ın Türk listelerini kapsayıp kapsamadığı ve güncelliği bu pakette doğrulanmadı.

### 5. Karar

| Sonuç | Anlam | Akış |
|---|---|---|
| ✓ TEMİZ | anlamlı eşleşme yok | kayıt → `/firm-operations:kvkk-aydinlatma` |
| 🟠 İNCELE | orta skor, ad benzerliği, PEP, yabancı liste eşleşmesi | ek teyit + Yönetici Ortak |
| ⛔ HIT | kişi veya kuruluş bir Türk dondurma kararında yer alıyor ya da ≥ 0,90 skorla teyitli eşleşme var | iş kabulü durur → Yönetici Ortak + Ortaklar Kurulu; finansal işlem aracılığı yapılmaz; `/firm-operations:masak-kontrol` şüpheli işlem değerlendirmesi |

Savunma hakkı kapsamındaki temsil ile finansal işlem aracılığı ayrı değerlendirilir. Kabul veya ret kararını bu skill vermez, Ortaklar Kurulu verir.

## Çıktı

```markdown
[ÜST BAŞLIK — YAPTIRIM TARAMASI — DAHİLİ]

# Sanctions Check — [takma ad] — GG.AA.YYYY
| Taranan | Kaynak | Sonuç | Skor | Eşleşen liste | Teyit |
|---|---|---|---|---|---|
| Müvekkil | OpenSanctions | ✓ / 🟠 / ⛔ | [X] | [liste] | [doğum tarihi / uyruk / sicil karşılaştırması] |
| GF-1 | OpenSanctions | ... | | | |
| Müvekkil | TR dondurma kararları (6415 / 7262) | ✓ / ⛔ | — | [karar, RG tarihi] | elle kontrol GG.AA.YYYY |

Atıf: [OpenSanctions API — match skoru X — GG.AA.YYYY]
SONUÇ: ✓ TEMİZ / 🟠 İNCELE / ⛔ HIT
```

## Hatalar

- Dosya ayrıntısını sorguya koymak (Av. K. m. 36)
- KVKK m. 9 dayanağı olmadan gerçek kişi verisini yurt dışındaki API'ye göndermek
- Teyitsiz ad benzerliğini HIT saymak
- OFAC veya AB eşleşmesini "Türkiye'de malvarlığı dondurulmuş" diye raporlamak
- API anahtarını çıktıya yazmak

Ayrıntı: `references/opensanctions-rehberi.md` · `references/yaptirim-tarama-rehberi.md`

---

## /firm-operations:vekalet-sablon

---
name: vekalet-sablon
description: >
  İş türüne göre vekâletname yetki listesi: HMK m. 74 özel yetkileri, tevkil, ibraz
  (HMK m. 76-77), avukat onaylı örnek ve yetki belgesi (Av. K. m. 56), çekilme ve azlin
  sonuçları. Tek tip vekâletnamenin biçimini TBB ile Türkiye Noterler Birliği hazırlar;
  bu skill noter metnini değil, eklenecek yetkileri üretir.
user-invocable: true
---

# Vekâlet Şablonu — Yetki Listesi

## Tetikleyici

`/firm-operations:fee-agreement` imzalandıktan sonra, noter randevusundan önce.

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- HUKUK MUHAKEMELERİ KANUNU (Kanun No. 6100, RG sayı 27836) m. 74, m. 75, m. 76, m. 77
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 41, m. 56, m. 171, m. 174
- TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG sayı 27836) m. 512
- CEZA MUHAKEMESİ KANUNU (Kanun No. 5271, RG sayı 25673) m. 149, m. 150

⚠️ Av. K. m. 32 **mülgadır** (30/1/1979 - 2178/8); vekâletname şekline dayanak gösterilemez. Av. K. m. 35 "yalnız avukatların yapabileceği işler"i düzenler; müdafilikte vekâletname kuralı içermez.

## Akış

### 1. Biçim
Vekâletnameler Türkiye için tek tiptir; biçim ve içeriğini Türkiye Barolar Birliği ile Türkiye Noterler Birliği hazırlar (Av. K. m. 56/6). Bu skill tek tip metne eklenecek **yetkileri** belirler.

### 2. Özel yetki gerektiren işlemler (HMK m. 74)
Açıkça yetki verilmemişse vekil aşağıdakileri yapamaz. İşe göre gerekenleri işaretle:

| Yetki (HMK m. 74'teki sırayla) | Tipik iş |
|---|---|
| sulh olmak | her dava |
| hâkimi reddetmek | dava |
| davanın tamamını ıslah etmek | dava |
| yemin teklif etmek; yemini kabul, iade veya reddetmek | dava |
| başkasını tevkil etmek | her iş (bkz. 3) |
| haczi kaldırmak | icra |
| müvekkilin iflasını istemek | icra-iflas |
| tahkim ve hakem sözleşmesi yapmak | ticari uyuşmazlık |
| konkordato ya da sermaye şirketleri ve kooperatiflerin uzlaşma yoluyla yeniden yapılandırılması teklifinde bulunmak, bunlara muvafakat vermek | yeniden yapılandırma |
| alternatif uyuşmazlık çözüm yollarına başvurmak | arabuluculuk |
| davadan veya kanun yollarından feragat etmek | dava |
| karşı tarafı ibra etmek; davasını kabul etmek | dava |
| yargılamanın iadesi yoluna gitmek | kesinleşmiş karar |
| hâkimlerin fiilleri sebebiyle Devlet aleyhine tazminat davası açmak | istisnai |
| kişiye sıkı sıkıya bağlı haklarla ilgili dava açmak ve takip etmek (**hangileri olduğu açıkça yazılarak**) | kişilik hakları vb. |

Liste HMK m. 74 metnindeki kalemlerden oluşur. Listede olmayan bir yetkiyi HMK m. 74'e dayandırma.

### 3. Tevkil ve yetki belgesi
- Vekâletnamede tevkil yetkisi varsa iş başka bir avukatla birlikte veya başka bir avukata verilerek takip ettirilebilir. Genel tevkil yetkisiyle sonraki işlerde yeniden vekâlet gerekmez (Av. K. m. 171/2).
- Avukat veya avukatlık ortaklığı, tevkil yetkili tüm vekâletnamelerini kapsayan bir **yetki belgesi** verebilir; yetki belgesi vekâletname hükmündedir (Av. K. m. 56/5).
- Birden fazla vekil varsa her biri yetkilerini diğerinden bağımsız kullanır; aksi yöndeki sınırlama karşı taraf bakımından geçersizdir (HMK m. 75).

### 4. İbraz ve örnek
- Noter onaylı ya da düzenlenmiş vekâletname aslı veya avukat onaylı örneği dosyaya ibraz edilir (HMK m. 76/1).
- Avukatın onayladığı vekâletname örneği bütün yargı mercileri, resmi daireler ve kişiler için resmi örnek hükmündedir (Av. K. m. 56/1).
- Aslı olmayan vekâletnamenin örneğini onaylamak veya aslına aykırı örnek vermek üç yıldan altı yıla kadar hapis cezası gerektirir (Av. K. m. 56/3).
- Vekâletnamesiz dava açılamaz; gecikmede zarar doğabilecek hâlde mahkeme kesin süre verebilir (HMK m. 77/1).

### 5. Ceza dosyası
Şüpheli veya sanık soruşturma ve kovuşturmanın her aşamasında müdafi yardımından yararlanabilir (CMK m. 149/1). Müdafi seçebilecek durumda değilse istemi hâlinde; çocuk, kendini savunamayacak derecede malul ya da sağır ve dilsizse ve alt sınırı beş yıldan fazla hapis cezası gerektiren suçlarda istemi aranmaksızın müdafi görevlendirilir (CMK m. 150). Seçilmiş müdafinin hangi aşamada vekâletname ibraz etmesi gerektiği bu skill'de **doğrulanmadı**; bkz. `/criminal-defense:cmk-gorev-atama`.

### 6. Sona erme
- Vekâlet veren de vekil de sözleşmeyi her zaman tek taraflı sona erdirebilir; uygun olmayan zamanda sona erdiren taraf diğerinin zararını giderir (TBK m. 512).
- Avukat çekilirse vekâlet görevi, durumun müvekkile **tebliğinden itibaren 15 gün** devam eder (Av. K. m. 41/1). Bu bir "15 gün önceden bildirim" kuralı değildir.
- Azilde ücret: Av. K. m. 174/2 (bkz. `/firm-operations:fee-agreement`).

### 7. Yurt dışında düzenlenen vekâletname
Onay (apostil veya konsolosluk) ve tercüme gereklilikleri bu pakette doğrulanmadı; noterle teyit et.

## Çıktı

```markdown
[ÜST BAŞLIK — VEKÂLETNAME YETKİ LİSTESİ — NOTER / MÜVEKKİL İÇİN]

Müvekkil: [takma ad] — İş: [kısa ad] — GG.AA.YYYY
Vekil(ler): [avukat(lar) / avukatlık ortaklığı]
Genel yetki: tek tip vekâletname (Av. K. m. 56/6)
Özel yetkiler (HMK m. 74): [işaretlenenler]
Tevkil: var / yok — yetki belgesi: gerekli / gerekmez
Not: noter metni tek tip şablondan gelir; bu liste yalnız yetkileri gösterir.
```

## Hatalar

- Av. K. m. 32'yi dayanak göstermek (mülga)
- HMK m. 74'te olmayan bir yetkiyi ("kambiyo taahhüdü", "şikâyetten vazgeçme" gibi) HMK m. 74'e dayandırmak. Bunlar için başka bir kanunda özel yetki aranıp aranmadığı ayrıca doğrulanmalı.
- Tevkil yetkisini unutmak (iş devri yapılamaz)
- Çekilmedeki 15 günü "önceden bildirim" sanmak

Ayrıntı: `references/vekalet-uyap-rehberi.md`
