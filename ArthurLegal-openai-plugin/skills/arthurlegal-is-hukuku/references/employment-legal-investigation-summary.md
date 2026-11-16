# employment-legal-investigation-summary

Soruşturma notundan hedef kitleye özel özet yaz — İK, yönetim/YK, dış avukat ya da şikâyetçiye sonuç bildirimi. Notun tamamını görmemesi gereken bir kitleye sonucun iletilmesi gerektiğinde kullan.

# /investigation-summary

Soruşturma notundan kitleye uygun, sadeleştirilmiş özet üretir. İK özeti hukuki analiz içermez; yönetim özeti üst düzeydedir; dış avukat brifingi tam bağlamı taşır; ilgiliye bildirim yalnız sonuç ve önlemleri söyler.

## Talimat

1. `internal-investigation` referans skill'ini yükle ve **Mod 5 (Hedef kitle özeti)** uygula.
2. Henüz not yoksa önce notu yazmayı öner (``employment-legal-investigation-memo` iş akışı (`arthurlegal-is-hukuku` becerisi, `../arthurlegal-is-hukuku/references/employment-legal-investigation-memo.md`)`).
3. İK özetine avukat izlenimleri, güvenilirlik yöntemi ve hukuki risk analizi girmez; İK özetinin davada sunulabileceğini varsayarak olgusal yaz.
4. İlgiliye bildirimde başka kişilerin kişisel verisini ve tanık beyanlarını açma (KVKK m. 4/2-ç, İş K. m. 75/2).
5. Özet bir dış merciye (arabuluculuk, ihtarname cevabı, iş müfettişi, KVKK, savcılık) gidecekse referans skill'deki **sonuçlu işlem kapısını** uygula.

## Örnekler

```
`employment-legal-investigation-summary` iş akışı (`arthurlegal-is-hukuku` becerisi, `../arthurlegal-is-hukuku/references/employment-legal-investigation-summary.md`) [matter adı] ik
```

```
`employment-legal-investigation-summary` iş akışı (`arthurlegal-is-hukuku` becerisi, `../arthurlegal-is-hukuku/references/employment-legal-investigation-summary.md`) [matter adı] yonetim
```

```
`employment-legal-investigation-summary` iş akışı (`arthurlegal-is-hukuku` becerisi, `../arthurlegal-is-hukuku/references/employment-legal-investigation-summary.md`) [matter adı] dis-avukat
```

> Kitleye göre ayıklama kuralları ve özet şablonları `internal-investigation` referans
> skill'indedir — esaslı işe başlamadan önce yükle.

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
