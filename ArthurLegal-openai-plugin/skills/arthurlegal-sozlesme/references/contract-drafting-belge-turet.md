# contract-drafting-belge-turet

Örnek/emsal bir belgeden (şablon) yeni sözleşme/protokol TÜRETİR — şablonun yapısını çıkarır, yeni işin parametreleriyle uyarlar, doldurulacak alanları [DOLDUR] işaretler, TBK/TTK emredici hüküm + standart klozlar ile uyumlar. Tipik: süre uzatım protokolü, EPC/PPA/vendor sözleşmesi, NDA, hissedar/JV, kredi tadili.

# Şablon / Emsalden Belge Türetme

> Elindeki bir örnek belgeden (önceki bir sözleşme, standart şablon, emsal protokol) **yeni bir belge** üretir. Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı.

## ADIM 0 — Girdi

1. **Şablon/emsal belge:** kullanıcı yapıştırsın/yüklesin (yoksa: hangi belge tipini istediğini sor, `../arthurlegal/references/redline-konvansiyonlari-rehberi.md` bölüm 8'deki iskeletle başla).
2. **Yeni işin parametreleri** — taraflar, konu, tutar/süre, özel şartlar, fark eden noktalar.
3. **Hangi tip?** EPC · PPA/elektrik satış · vendor/tedarik · NDA · hissedar/JV · kredi/finansman · **süre uzatım/ek protokol** · diğer.

## ADIM 1 — Şablonu analiz et

- **Yapı haritası:** bölüm/madde başlıkları (başlangıç hükümleri, tanımlar, edimler, bedel/ödeme, süre, mücbir sebep, sorumluluk, gizlilik, fesih, uyuşmazlık, ekler).
- **Değişken alanlar:** şablondaki örneğe-özgü değerler (taraf adı, tarih, tutar, proje) → yeni parametrelerle değişecek.
- **Sabit/standart klozlar:** korunacak (boilerplate) ama şirket standardıyla kıyasla.

## ADIM 2 — Yeni belgeyi üret

- Yapıyı koru; değişken alanları yeni parametrelerle doldur; bilinmeyenleri **`[DOLDUR — ...]`** bırak.
- **Standart klozları** `../arthurlegal/references/redline-konvansiyonlari-rehberi.md` bölüm 5'teki sete göre ekle ve teyit et. Şablon verilmediyse aynı rehberin 7 ile 11. bölümlerini (iskelet, karar listesi, sık hatalar, Word düzeni) örnek al; oradaki ifadeyi birebir aktarma, işe göre yeniden kur.
- **Emredici hüküm kontrolü:** şablondaki bir kloz emredici kurala aykırıysa düzelt + flag (`[ArthurLegal TR — kanun m. X — GG.AA.YYYY]`, madde çekildikten sonra). (Örn. tüketici/iş sözleşmesinde aleyhe kloz, fahiş cezai şart TBK m.182, çalışan buluşu klozunda SMK m. 117 emredici sınırı.)
- **Madde doğrulama kapısı (teslim öncesi, zorunlu):** Belge gövdesine yazılan her kanun maddesi (şablondan gelen, bu kitapçıktaki örneklerden gelen veya yeni eklenen) `tr_mevzuat_madde_getir` ile çekilir; kloz maddeye ne yüklüyorsa (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirilir. Eşleşmiyorsa numara korunup açıklama uydurulmaz. Çekilemiyorsa madde numarası gövdeden çıkarılır, kloz numarasız kurulur ("ilgili mevzuatın emredici hükümleri saklıdır") ve eksik İnceleyen notuna yazılır. Bu kitapçıktaki örnek madde numaraları (TBK m.13, 136, 138, 182 gibi) doğrulama değildir. Yol: `../arthurlegal/references/mevzuat-mcp-rehberi.md` bölüm 9.
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
> 1. **Redline incele** — ``contract-drafting-redline-contract` iş akışı (`arthurlegal-sozlesme` becerisi, `../arthurlegal-sozlesme/references/contract-drafting-redline-contract.md`)` ile son kontrol
> 2. **[DOLDUR] alanlarını tamamla** — eksik parametreler
> 3. **Governing law / yaptırım** — yabancı taraf varsa
> 4. **Başka**

**One question I'd ask:** [örn. "Bu emsal hangi işten geldi? O işe özgü taviz/özel kloz varsa yeni belgeye sessizce taşımayalım."]
```

---

## Kaynak katmanı — /legal-research

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
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | ``legal-research-sozlesme-emsali` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-sozlesme-emsali.md`)` |
| AZ hukuku secilmisse emredici hukum kontrolu — akt + statu | ``legal-research-az-mevzuat` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-az-mevzuat.md`)` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil) — okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `../arthurlegal/references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `../arthurlegal/references/eqanun-mcp-rehberi.md` · `../arthurlegal/references/lex-scholar-rehberi.md` · `../arthurlegal/references/resourcecontracts-rehberi.md` · `../arthurlegal/references/karsilastirmali-hukuk-rehberi.md` · `../arthurlegal/references/nl-rechtspraak-mcp-rehberi.md` · `../arthurlegal/references/pl-sejm-mcp-rehberi.md` · `../arthurlegal/references/at-ris-mcp-rehberi.md` · `../arthurlegal/references/ie-statutebook-mcp-rehberi.md` · `../arthurlegal/references/fi-finlex-mcp-rehberi.md` · `../arthurlegal/references/es-boe-mcp-rehberi.md`
