# regulatory-legal-gaps

Açık uyum açıkları izleyicisi — işaretlenmiş ama kapanmamış olanlar. "Hangi açıklar açık", "açık izleyici", "düzeltme durumu" denince ya da izlenen bir açık kapatılmak (--close GAP-ID) veya risk kabulüne alınmak (--accept GAP-ID) istendiğinde kullan.

# /gaps

1. `Hafıza › Pratik/regulatory-legal/gap-tracker.yaml` dosyasındaki izleyiciyi oku.
2. `--close`: açığı kapanış notuyla kapat. Önce gap-surfacer'daki uyum beyanı kapısını uygula (rol Non-lawyer ise avukat onayı sorulur).
3. `--accept`: risk kabulü gerekçesini ve kabul edeni kaydet; durum `risk-accepted`. Kabul edenin yetkisini profildeki eskalasyon yolundan kontrol et.
4. Aksi hâlde: açık kalemleri yaşa ve önemliliğe göre raporla; kural öncesi kalemleri (`watch`, `comment-decision`) ayrı kovada göster.

> İzleyici şeması, durum raporu biçimi, sahip bildirimi kuralı (gönderim başına onay, istisnasız), hatırlatma sıklığı, kapatma ve risk kabulü modları, doğrulanmamış kuralda Overdue yasağı ve uyum beyanı kapısı **gap-surfacer** referans skill'indedir; asıl işe başlamadan önce onu yükle.

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
| AZ duzenleyici degisiklik takibi — akt statusu degistiyse (`Legv olunmus`) ardil akti bul | ``legal-research-az-mevzuat` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-az-mevzuat.md`)` |
| karsilastirmali regulasyon literaturu — **ikincil**, mevzuat yerine gecmez | ``legal-research-karsilastirmali-doktrin` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-karsilastirmali-doktrin.md`)` |

Rehberler: `skills/arthurlegal/references/eqanun-mcp-rehberi.md` · `skills/arthurlegal/references/lex-scholar-rehberi.md` · `skills/arthurlegal/references/resourcecontracts-rehberi.md` · `skills/arthurlegal/references/karsilastirmali-hukuk-rehberi.md`

---
