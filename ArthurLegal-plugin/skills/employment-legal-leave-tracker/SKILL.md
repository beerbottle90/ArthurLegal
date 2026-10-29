---
name: employment-legal-leave-tracker
description: >
  Açık izin ve raporları kanuni süre uyarıları ve karar noktaları için tarar
  (Türk hukuku) — hastalık/kaza bekleme süresi (İş K. m. 25/I), iş kazası SGK
  bildirimi (5510 m. 13), analık izni ve sonrası haklar (m. 74, m. 13/5),
  askerlik ve kanuni ödev (m. 31), uzun izin dönüşü İSG eğitimi. Yalnız
  eylem gerektiren izinleri gösterir ve nedenini söyler; durum panosu değildir.
  Haftalık ya da avukat hangi izinde yaklaşan süre olduğunu bilmek istediğinde
  kullan.
argument-hint: "[argüman yok — İK sisteminden ya da leave-register.yaml'dan çalışır]"
---

# /leave-tracker — İzin Süreleri Takibi

Kanuni saati işleyen tüm açık izinleri kontrol eder; yalnız karar ya da işlem gerektirenleri gösterir. Durum panosu değildir: ne yapmanız gerektiğini ve nedenini söyler.

## Talimat

1. `leave-tracker` ajanını yükle ve tam iş akışını çalıştır.
2. İK sistemi bağlı değilse ve `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` yoksa, avukattan izin listesini (tablo) yüklemesini ya da `/arthurlegal:employment-legal-log-leave` ile tek tek kayıt eklemesini iste.
3. Uyarı yalnız eylem gerektiren izinler için; temiz izinler birer satırla özetlenir.
4. Her süre, `tr_mevzuat_madde_getir` ile çekilen maddeye dayanır; değişiklik notu taşıyan maddelerde (ör. 4857 m. 74 ve ek m. 2 — 2026 değişiklikleri) güncel metni esas al.

## Örnek

```
/arthurlegal:employment-legal-leave-tracker
```

Haftalık çalıştır — Pazartesi sabahı için bir hatırlatıcı kur. Otomatik zamanlama ayrı bir entegrasyon gerektirir (takvim hatırlatıcısı, zamanlanmış görev vb.); Claude Code ajanları kendi kendini zamanlamaz.

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
