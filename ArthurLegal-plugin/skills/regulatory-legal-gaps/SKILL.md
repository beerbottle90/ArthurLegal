---
name: regulatory-legal-gaps
description: Açık uyum açıkları izleyicisi — işaretlenmiş ama kapanmamış olanlar. "Hangi açıklar açık", "açık izleyici", "düzeltme durumu" denince ya da izlenen bir açık kapatılmak (--close GAP-ID) veya risk kabulüne alınmak (--accept GAP-ID) istendiğinde kullan.
argument-hint: "[isteğe bağlı: --close GAP-ID | --accept GAP-ID]"
---

# /gaps

1. `~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml` dosyasındaki izleyiciyi oku.
2. `--close`: açığı kapanış notuyla kapat. Önce gap-surfacer'daki uyum beyanı kapısını uygula (rol Non-lawyer ise avukat onayı sorulur).
3. `--accept`: risk kabulü gerekçesini ve kabul edeni kaydet; durum `risk-accepted`. Kabul edenin yetkisini profildeki eskalasyon yolundan kontrol et.
4. Aksi hâlde: açık kalemleri yaşa ve önemliliğe göre raporla; kural öncesi kalemleri (`watch`, `comment-decision`) ayrı kovada göster.

> İzleyici şeması, durum raporu biçimi, sahip bildirimi kuralı (gönderim başına onay, istisnasız), hatırlatma sıklığı, kapatma ve risk kabulü modları, doğrulanmamış kuralda Overdue yasağı ve uyum beyanı kapısı **gap-surfacer** referans skill'indedir; asıl işe başlamadan önce onu yükle.

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
| AZ duzenleyici degisiklik takibi — akt statusu degistiyse (`Legv olunmus`) ardil akti bul | `/arthurlegal:legal-research-az-mevzuat` |
| karsilastirmali regulasyon literaturu — **ikincil**, mevzuat yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
