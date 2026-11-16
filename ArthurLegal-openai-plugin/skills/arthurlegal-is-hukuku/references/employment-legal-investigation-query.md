# employment-legal-investigation-query

Açık bir soruşturma kaydına soru sor — tanıklar ne dedi, anlatımlar nerede çelişiyor, hangi boşluklar var, her konuda en güçlü delil ne, savunma ve m. 26 süresi ne durumda. Avukat her girdiyi yeniden okumadan kayda soru sormak istediğinde kullan.

# /investigation-query

Soruşturma kaydına karşı soruları cevaplar: tanık anlatımları, çelişkiler, boşluklar, konu bazında en güçlü delil, usul durumu.

## Talimat

1. `internal-investigation` referans skill'ini yükle ve **Mod 3 (Kayda soru sor)** uygula.
2. Her cevapta kayıt ID'lerini göster.
3. Kayıtta ilgili bilgi yoksa açıkça söyle — "Bu soruşturma kaydında ([N] girdi) [konu] hakkında bilgi görmedim" — ve boşluk olarak işaretlemeyi öner.
4. Usul sorularında (savunma, m. 26, açılış bildirimleri, KVKK kontrolü) tarihleri kayıttan ver; hesapladığın son günü "tartışmalı — içtihadı kontrol et" notuyla yaz.

## Örnekler

```
`employment-legal-investigation-query` iş akışı (`arthurlegal-is-hukuku` becerisi, `../arthurlegal-is-hukuku/references/employment-legal-investigation-query.md`) [matter adı]
Hakkında iddia olan kişi Aralık ayındaki ekip yemeği hakkında ne dedi?
```

```
`employment-legal-investigation-query` iş akışı (`arthurlegal-is-hukuku` becerisi, `../arthurlegal-is-hukuku/references/employment-legal-investigation-query.md`) [matter adı]
Şikâyetçinin ve hakkında iddia olanın anlatımları nerede çelişiyor?
```

```
`employment-legal-investigation-query` iş akışı (`arthurlegal-is-hukuku` becerisi, `../arthurlegal-is-hukuku/references/employment-legal-investigation-query.md`) [matter adı]
Neyi eksik? Savunma alındı mı, m. 26 için kaç iş günü kaldı?
```

> Sorgu süreci, atıf kuralları ve boşluk işaretleme şablonları `internal-investigation`
> referans skill'indedir — esaslı işe başlamadan önce yükle.

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
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | ``legal-research-az-mevzuat` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-az-mevzuat.md`)` |

Rehberler: `../arthurlegal/references/eqanun-mcp-rehberi.md` · `../arthurlegal/references/lex-scholar-rehberi.md` · `../arthurlegal/references/resourcecontracts-rehberi.md` · `../arthurlegal/references/karsilastirmali-hukuk-rehberi.md`

---
