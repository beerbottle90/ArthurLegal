---
name: employment-legal-log-leave
description: >
  İzin kaydına yeni bir izin/rapor ekler (Türk hukuku) — süre takibini
  başlatmak için gereken asgari bilgiyle: hastalık ya da iş kazası raporu,
  analık izni, yarım çalışma ya da ücretsiz izin (m. 74), askerlik/kanuni ödev
  (m. 31), mazeret izni (ek m. 2), uzun ücretsiz izin. Bir çalışan izne ya da
  rapora çıktığında, takipçinin saatleri ilk günden izlemesi için kullan.
argument-hint: "[izni anlatın — çalışan/rol, izin türü, işyeri, başlangıç tarihi]"
---

# /log-leave — İzin Kaydı Ekle

`~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` dosyasına, süre takibini başlatacak asgari bilgiyle yeni kayıt ekler.

## Talimat

1. `firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → ayak izi, `## Systems` (İK sistemi), eskalasyon matrisi.

2. Aşağıdakilerin hepsini tek seferde sor — tek tek sorma:

   > İzin takibini kurmak için birkaç soru:
   >
   > - Çalışan adı ya da rolü (anonim olabilir)
   > - İşyeri (Türkiye dışındaysa ülke) ve işe giriş tarihi (kıdem → bildirim süresi ve bekleme süresi)
   > - İzin türü: hastalık raporu / iş kazası / analık (doğum öncesi-sonrası) / yarım çalışma ya da 6 aya kadar ücretsiz izin (m. 74) / süt izni / kısmi süreli çalışma talebi (m. 13/5) / askerlik veya kanuni ödev (m. 31) / mazeret izni (ek m. 2) / anlaşmalı ücretsiz izin
   > - Başlangıç tarihi; rapor varsa rapor bitiş tarihi
   > - Analıkta tahmini (ya da gerçek) doğum tarihi, çoğul gebelik mi, hekim onayıyla doğuma yakın çalışma talebi var mı
   > - İş kazasında kaza tarihi ve SGK'ya bildirildi mi (ne zaman)
   > - Beklenen dönüş tarihi (biliniyorsa)

3. Maddeleri `tr_mevzuat_madde_getir` ile çek ve ilk yaklaşan süreyi hesapla:

   | İzin türü | İlk süre | Dayanak |
   |---|---|---|
   | İş kazası | Kolluğa derhal; SGK'ya kazadan sonraki **3 iş günü** içinde (işveren kontrolü dışındaki yerde: öğrenmeden itibaren) | 5510 m. 13 |
   | Hastalık / kaza raporu | **Bekleme süresi sonu** = rapor başlangıcı + m. 17'ye göre bildirim süresi (kıdeme göre 2/4/6/8 hafta) + **6 hafta**; bu tarihten önce bu gerekçeyle bildirimsiz fesih hakkı doğmaz | 4857 m. 25/I, m. 17, m. 18/3-f |
   | Analık — doğum öncesi | Tahmini doğumdan **8 hafta** önce (çoğulda 10); hekim onayı ve işçinin isteğiyle doğuma 2 hafta kalana kadar çalışabilir, çalışılan süre doğum sonrasına eklenir | 4857 m. 74/1 |
   | Analık — doğum sonrası | Doğumdan itibaren **16 hafta**; erken doğumda kullanılamayan doğum öncesi süre eklenir; bitişte işçinin talebini al: yarım çalışma ücretsiz izni (ilk doğumda 60, ikincide 120, sonrakilerde 180 gün; çoğulda +30; engelli doğumda 360) ya da 6 aya kadar ücretsiz izin; süt izni çocuk 1 yaşına kadar günde 1,5 saat | 4857 m. 74/1, 74/2, 74/6, 74/7 |
   | Kısmi süreli çalışma talebi | İşçi en az **1 ay önce** yazılı bildirir; talep karşılanır; mecburi ilköğretim çağının başladığı tarihi izleyen ay başına kadar | 4857 m. 13/5 |
   | Askerlik / kanuni ödev | İki ayrı saat: (a) sözleşme ayrılıştan **2 ay** sonra (1 yılı aşan her yıl için +2 gün, toplam en çok 90 gün) işverence feshedilmiş sayılır — en az 1 yıl kıdem şartı; (b) ödev bitince işçinin **2 ay** içinde işe dönüş başvurusu | 4857 m. 31 |
   | Mazeret izni (ücretli) | Evlenme, evlat edinme, ana/baba/eş/kardeş/çocuk ölümü 3 gün; eşin doğumu **10 gün**; %70+ engelli ya da süreğen hastalıklı çocuk için yılda 10 güne kadar (bir ebeveyn) — kaydet, uyarı yok | 4857 ek m. 2 |
   | Uzun izin (6 aydan fazla) | Dönüşten önce İSG bilgi yenileme eğitimi | 6331 m. 17/4 |

   Kayıtta olmayan bilgi (işe giriş tarihi gibi) bekleme süresini etkiliyorsa hesaplama; boş bırak ve "eksik bilgi" diye işaretle. Aralıklı raporların bekleme süresinde toplanıp toplanmayacağı **tartışmalı — içtihadı kontrol et**.

4. Yeni kaydı `leave-tracker` ajanındaki kayıt biçimiyle `leave-register.yaml` dosyasına yaz; dosya yoksa oluştur. `kontrol_eden_kaynaklar` alanına çekilen maddelerin `citation` değerini yaz.

5. Tek satırla onayla:
   > "Kaydedildi. [Çalışan/Rol] — [İzin türü] — [İşyeri] — başlangıç [tarih]. İlk süre: [ne ve ne zaman] ([dayanak]). İzin takipçisi bu tarihi izleyecek."

## Örnekler

```
/arthurlegal:employment-legal-log-leave
```

```
/arthurlegal:employment-legal-log-leave
Kıdemli mühendis, İstanbul işyeri, 4 yıllık kıdem; bugün 20 günlük hastalık
raporu getirdi, daha önce de bu yıl iki kez rapor almıştı.
```

```
/arthurlegal:employment-legal-log-leave
Muhasebe uzmanı, tahmini doğum 15 Mart, tek gebelik; hekim onayıyla doğuma
2 hafta kalana kadar çalışmak istiyor.
```

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
