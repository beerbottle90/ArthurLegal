# employment-legal-investigation-open

Yeni iç soruşturma dosyası aç — ön görüşmeyi yürütür, m. 26 süre sayacını ve savunma durumunu kurar, türe uygun kaynak listesini üretir ve kalıcı soruşturma kaydını oluşturur. Şikâyet, ihbar ya da iddia geldiğinde ve avukat soruşturma çalışma alanını kurmak istediğinde kullan.

# /investigation-open

Yeni bir iç soruşturma dosyası açar: ön görüşme, süre ve usul ön-kontrolü, kaynak listesi, kalıcı kayıt.

## Talimat

1. `Hafıza › Pratik/employment-legal/PROFIL.md` dosyasını yükle (yoksa önce ``employment-legal-cold-start-interview` iş akışı (`is-hukuku` becerisi, `references/employment-legal-cold-start-interview.md`)` öner).
2. `internal-investigation` referans skill'ini yükle ve **Mod 1 (Soruşturma aç)** uygula — önce ⏰ ÖN-KONTROL (İş K. m. 26 öğrenme tarihi, m. 19 savunma, TİS/disiplin usulü).
3. Aynı slug'la bir soruşturma varsa üzerine yazmadan önce uyar.
4. Açılış çıktısında şunları göster: klasör yolu, m. 26 son günü ("tartışmalı" notuyla), dosya sınıfı ayrımı (A — avukat çalışma ürünü / B — işveren delil dosyası), KVKK kontrolü gereken kaynaklar.

## Örnekler

```
`employment-legal-investigation-open` iş akışı (`is-hukuku` becerisi, `references/employment-legal-investigation-open.md`)
İzmir şubesindeki bir müdür hakkında psikolojik taciz şikâyeti; İK'ya dün e-postayla ulaştı.
```

```
`employment-legal-investigation-open` iş akışı (`is-hukuku` becerisi, `references/employment-legal-investigation-open.md`)
(skill ayrıntıları soracak)
```

> Ön görüşme soruları, gizlilik ayrımı, kaynak listeleri ve kayıt şablonları
> `internal-investigation` referans skill'indedir — esaslı işe başlamadan önce yükle.

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
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | ``legal-research-az-mevzuat` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-az-mevzuat.md`)` |

Rehberler: `skills/arthurlegal/references/eqanun-mcp-rehberi.md` · `skills/arthurlegal/references/lex-scholar-rehberi.md` · `skills/arthurlegal/references/resourcecontracts-rehberi.md` · `skills/arthurlegal/references/karsilastirmali-hukuk-rehberi.md`

---
