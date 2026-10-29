---
name: employment-legal-investigation-open
description: >
  Yeni iç soruşturma dosyası aç — ön görüşmeyi yürütür, m. 26 süre sayacını ve savunma
  durumunu kurar, türe uygun kaynak listesini üretir ve kalıcı soruşturma kaydını
  oluşturur. Şikâyet, ihbar ya da iddia geldiğinde ve avukat soruşturma çalışma alanını
  kurmak istediğinde kullan.
argument-hint: "[iddianın kısa tarifi]"
---

# /investigation-open

Yeni bir iç soruşturma dosyası açar: ön görüşme, süre ve usul ön-kontrolü, kaynak listesi, kalıcı kayıt.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını yükle (yoksa önce `/arthurlegal:employment-legal-cold-start-interview` öner).
2. `internal-investigation` referans skill'ini yükle ve **Mod 1 (Soruşturma aç)** uygula — önce ⏰ ÖN-KONTROL (İş K. m. 26 öğrenme tarihi, m. 19 savunma, TİS/disiplin usulü).
3. Aynı slug'la bir soruşturma varsa üzerine yazmadan önce uyar.
4. Açılış çıktısında şunları göster: klasör yolu, m. 26 son günü ("tartışmalı" notuyla), dosya sınıfı ayrımı (A — avukat çalışma ürünü / B — işveren delil dosyası), KVKK kontrolü gereken kaynaklar.

## Örnekler

```
/arthurlegal:employment-legal-investigation-open
İzmir şubesindeki bir müdür hakkında psikolojik taciz şikâyeti; İK'ya dün e-postayla ulaştı.
```

```
/arthurlegal:employment-legal-investigation-open
(skill ayrıntıları soracak)
```

> Ön görüşme soruları, gizlilik ayrımı, kaynak listeleri ve kayıt şablonları
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
