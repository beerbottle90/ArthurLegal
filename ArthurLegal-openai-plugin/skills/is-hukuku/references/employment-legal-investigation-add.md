# employment-legal-investigation-add

Açık bir iç soruşturmaya veri ekle — belge, görüşme notu, savunma tutanağı ya da gözlem. Partileri yazılı çekme ölçütlerine göre tarar, önemli öğeleri öne çıkarır, incelenen her belgeyi kapsama doğrulaması için kaydeder; e-posta/cihaz/kamera verisinde önce KVKK kontrolünü ister. Yeni delil, görüşme notu ya da belge geldiğinde kullan.

# /investigation-add

Açık soruşturma kaydına veri ekler. Belge partilerini yazılı çekme ölçütleriyle işler, öne çıkanları kayda geçirir, incelenen her belgeyi kapsama için kaydeder.

## Talimat

1. `Hafıza › Pratik/employment-legal/PROFIL.md` dosyasını yükle.
2. `internal-investigation` referans skill'ini yükle ve **Mod 2 (Veri ekle)** uygula.
3. Kurumsal e-posta, mesaj, cihaz, kamera ya da log verisi geldiyse ve kayıtta `kvkk_kontrol` boşsa işlemeden önce KVKK ve delil kontrolünü tamamla (KVKK m. 4, 5, 10; TBK m. 419; HMK m. 189/2).
4. İşlemden sonra öne çıkma oranını ve öne çıkan öğelerin listesini göster.
5. Veri bir kaynak listesi kalemini karşılıyorsa güncelleme için sor; kendiliğinden `tamam` işaretleme.
6. Gelen veri savunma tutanağıysa kayıttaki `savunma` alanını ve m. 26 sayacını güncelle.

## Örnekler

```
`employment-legal-investigation-add` iş akışı (`is-hukuku` becerisi, `references/employment-legal-investigation-add.md`) [matter adı]
[görüşme notunu yapıştır]
```

```
`employment-legal-investigation-add` iş akışı (`is-hukuku` becerisi, `references/employment-legal-investigation-add.md`) [matter adı]
[e-posta dışa aktarımını ekle]
```

> İğne bulma süreci, kayıt girdisi biçimi, oran kuralları ve kaynak listesi takibi
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
