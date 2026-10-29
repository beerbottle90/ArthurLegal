---
name: employment-legal-investigation-add
description: >
  Açık bir iç soruşturmaya veri ekle — belge, görüşme notu, savunma tutanağı ya da
  gözlem. Partileri yazılı çekme ölçütlerine göre tarar, önemli öğeleri öne çıkarır,
  incelenen her belgeyi kapsama doğrulaması için kaydeder; e-posta/cihaz/kamera
  verisinde önce KVKK kontrolünü ister. Yeni delil, görüşme notu ya da belge
  geldiğinde kullan.
argument-hint: "[matter adı ya da slug; ardından veriyi yapıştır veya ekle]"
---

# /investigation-add

Açık soruşturma kaydına veri ekler. Belge partilerini yazılı çekme ölçütleriyle işler, öne çıkanları kayda geçirir, incelenen her belgeyi kapsama için kaydeder.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını yükle.
2. `internal-investigation` referans skill'ini yükle ve **Mod 2 (Veri ekle)** uygula.
3. Kurumsal e-posta, mesaj, cihaz, kamera ya da log verisi geldiyse ve kayıtta `kvkk_kontrol` boşsa işlemeden önce KVKK ve delil kontrolünü tamamla (KVKK m. 4, 5, 10; TBK m. 419; HMK m. 189/2).
4. İşlemden sonra öne çıkma oranını ve öne çıkan öğelerin listesini göster.
5. Veri bir kaynak listesi kalemini karşılıyorsa güncelleme için sor; kendiliğinden `tamam` işaretleme.
6. Gelen veri savunma tutanağıysa kayıttaki `savunma` alanını ve m. 26 sayacını güncelle.

## Örnekler

```
/arthurlegal:employment-legal-investigation-add [matter adı]
[görüşme notunu yapıştır]
```

```
/arthurlegal:employment-legal-investigation-add [matter adı]
[e-posta dışa aktarımını ekle]
```

> İğne bulma süreci, kayıt girdisi biçimi, oran kuralları ve kaynak listesi takibi
> `internal-investigation` referans skill'indedir — esaslı işe başlamadan önce yükle.

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
