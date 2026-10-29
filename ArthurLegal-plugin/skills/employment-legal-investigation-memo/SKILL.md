---
name: employment-legal-investigation-memo
description: >
  Soruşturma kaydından iç soruşturma notunu yaz ya da güncelle — konu bazında
  bulgular, güvenilirlik değerlendirmesi, Türk hukuku çerçevesi (m. 25/II eşleşmesi,
  m. 19 savunma, m. 26 süre, TBK m. 417). Soruşturma ilk taslak için yeterince
  ilerlediğinde ya da yeni veri eklendikten sonra kullan.
argument-hint: "[matter adı]"
---

# /investigation-memo

Soruşturma kaydından notun ilk taslağını yazar ya da yeni veri eklendiğinde mevcut taslağı günceller.

## Talimat

1. `internal-investigation` referans skill'ini yükle ve **Mod 4 (Soruşturma notu)** uygula.
2. İlk taslakta: yüksek öncelikli kaynaklar açıksa, savunma alınmamışsa ya da m. 26 son günü yaklaşıyorsa en üstte uyar.
3. Güncellemede: yeniden yazmadan önce neyin değiştiğini göster.
4. Not A sınıfı dosyadır (avukat çalışma ürünü); `## Outputs`'taki gizlilik başlığıyla açılır. Başlık koruma yaratmaz — gizlilik notunu koru.
5. "Hukuki çerçeve" bölümündeki her madde atfını `tr_mevzuat_madde_getir` ile doğrula; çekilemeyen için "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" yaz.

## Örnekler

```
/arthurlegal:employment-legal-investigation-memo [matter adı]
```

```
/arthurlegal:employment-legal-investigation-memo [matter adı]
(not varsa günceller)
```

> Not yapısı, güvenilirlik çerçevesi ve güncelleme kuralları `internal-investigation`
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
