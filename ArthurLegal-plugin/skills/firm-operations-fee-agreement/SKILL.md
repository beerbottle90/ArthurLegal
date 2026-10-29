---
name: firm-operations-fee-agreement
description: >
  Avukatlık ücret sözleşmesi taslağı. Kapsam, ücret modeli, AAÜT tabanı, yüzde ücret
  tavanı (%25), karşı taraf vekâlet ücreti, azil/çekilme ve peşin ücret hükümlerini
  Av. K. m. 163-174'e göre kontrol eder. Vergi oranlarını güncel kaynaktan doğrulamadan
  yazmaz. Sonuç: imzaya hazır taslak + kontrol tablosu.
user-invocable: true
---

# Fee Agreement — Avukatlık Ücret Sözleşmesi

## Tetikleyici

- `/arthurlegal:firm-operations-conflict-check` ✓ TEMİZ (🟠 ise Ortaklar Kurulu kararı) ve `/arthurlegal:firm-operations-masak-kontrol` tamamlandıktan sonra
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

Ayrıntı: `${CLAUDE_PLUGIN_ROOT}/references/ucret-sozlesmesi-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/aaut-rehberi.md`

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
> Ayrica bkz. `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| yabanci karsi tarafli veya AZ baglantili yeni is alimi — mevzuat kapsaminin gercekten var olup olmadigini once dogrula | `/arthurlegal:legal-research-kaynak-secimi` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
