---
name: employment-legal-investigation-query
description: >
  Açık bir soruşturma kaydına soru sor — tanıklar ne dedi, anlatımlar nerede
  çelişiyor, hangi boşluklar var, her konuda en güçlü delil ne, savunma ve m. 26
  süresi ne durumda. Avukat her girdiyi yeniden okumadan kayda soru sormak
  istediğinde kullan.
argument-hint: "[matter adı] [soru]"
---

# /investigation-query

Soruşturma kaydına karşı soruları cevaplar: tanık anlatımları, çelişkiler, boşluklar, konu bazında en güçlü delil, usul durumu.

## Talimat

1. `internal-investigation` referans skill'ini yükle ve **Mod 3 (Kayda soru sor)** uygula.
2. Her cevapta kayıt ID'lerini göster.
3. Kayıtta ilgili bilgi yoksa açıkça söyle — "Bu soruşturma kaydında ([N] girdi) [konu] hakkında bilgi görmedim" — ve boşluk olarak işaretlemeyi öner.
4. Usul sorularında (savunma, m. 26, açılış bildirimleri, KVKK kontrolü) tarihleri kayıttan ver; hesapladığın son günü "tartışmalı — içtihadı kontrol et" notuyla yaz.

## Örnekler

```
/arthurlegal:employment-legal-investigation-query [matter adı]
Hakkında iddia olan kişi Aralık ayındaki ekip yemeği hakkında ne dedi?
```

```
/arthurlegal:employment-legal-investigation-query [matter adı]
Şikâyetçinin ve hakkında iddia olanın anlatımları nerede çelişiyor?
```

```
/arthurlegal:employment-legal-investigation-query [matter adı]
Neyi eksik? Savunma alındı mı, m. 26 için kaç iş günü kaldı?
```

> Sorgu süreci, atıf kuralları ve boşluk işaretleme şablonları `internal-investigation`
> referans skill'indedir — esaslı işe başlamadan önce yükle.

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
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
