---
name: employment-legal-investigation-summary
description: >
  Soruşturma notundan hedef kitleye özel özet yaz — İK, yönetim/YK, dış avukat ya da
  şikâyetçiye sonuç bildirimi. Notun tamamını görmemesi gereken bir kitleye sonucun
  iletilmesi gerektiğinde kullan.
argument-hint: "[matter adı] [kitle: ik / yonetim / dis-avukat / ilgili]"
---

# /investigation-summary

Soruşturma notundan kitleye uygun, sadeleştirilmiş özet üretir. İK özeti hukuki analiz içermez; yönetim özeti üst düzeydedir; dış avukat brifingi tam bağlamı taşır; ilgiliye bildirim yalnız sonuç ve önlemleri söyler.

## Talimat

1. `internal-investigation` referans skill'ini yükle ve **Mod 5 (Hedef kitle özeti)** uygula.
2. Henüz not yoksa önce notu yazmayı öner (`/arthurlegal:employment-legal-investigation-memo`).
3. İK özetine avukat izlenimleri, güvenilirlik yöntemi ve hukuki risk analizi girmez; İK özetinin davada sunulabileceğini varsayarak olgusal yaz.
4. İlgiliye bildirimde başka kişilerin kişisel verisini ve tanık beyanlarını açma (KVKK m. 4/2-ç, İş K. m. 75/2).
5. Özet bir dış merciye (arabuluculuk, ihtarname cevabı, iş müfettişi, KVKK, savcılık) gidecekse referans skill'deki **sonuçlu işlem kapısını** uygula.

## Örnekler

```
/arthurlegal:employment-legal-investigation-summary [matter adı] ik
```

```
/arthurlegal:employment-legal-investigation-summary [matter adı] yonetim
```

```
/arthurlegal:employment-legal-investigation-summary [matter adı] dis-avukat
```

> Kitleye göre ayıklama kuralları ve özet şablonları `internal-investigation` referans
> skill'indedir — esaslı işe başlamadan önce yükle.

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
