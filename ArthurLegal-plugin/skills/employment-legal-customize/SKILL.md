---
name: employment-legal-customize
description: >
  İş hukuku profilinde tek bir şeyi değiştir — tüm kurulum görüşmesini yeniden
  yapmadan. Taraf modeli, işyeri/eşik tablosu, risk duruşu, eskalasyon kişileri,
  işe alım ve fesih kuralları, yönetmelik duruşları, soruşturma tercihleri ya da
  matter klasörleri. Kullanıcı "şunu değiştir", "işyeri ekle", "profilimi güncelle",
  "ayarlarımı düzenle" ya da "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değişikliğin tarifi]"
---

# /customize

## Ne zaman çalışır

Kullanıcı profilindeki bir şeyi — bir işyeri, risk duruşu, eskalasyon kişisi, yönetmelik duruşu — kurulum görüşmesini baştan yapmadan ve dosyayı elle düzenlemeden değiştirmek istiyor.

## Ne yap

1. **Profili oku.** `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` ve bir üst klasördeki `~/.claude/plugins/config/claude-for-legal/firm-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa:
   > Henüz kurulum yapılmamış. Önce `/arthurlegal:employment-legal-cold-start-interview` çalıştırın — customize mevcut bir profili ayarlamak içindir.

2. **Haritayı göster** (her biri için tek satır mevcut değer):
   - **Kim olduğumuz** — ad, sektör, pratik ortamı, iller/ülkeler *(tüm eklentilerle ortak — değişiklik `firm-profile.md`'e yazılır)*
   - **Taraf modeli** — işveren / işçi / ikisi; çıkar çatışması kuralı ve kontrol adımı
   - **İşyeri/eşik tablosu** — işyerleri, işçi sayıları, tetiklenen eşikler (30 işçi iş güvencesi, toplu işçi çıkarma, 50 işçi engelli kontenjanı), TİS/sendika, yurt dışı satırları
   - **Risk duruşu** — temkinli / orta / atak; fesih risk işaretleme, rekabet yasağı ve sulh yaklaşımına etkisi
   - **Kişiler** — İK muhatapları, dış avukat, eskalasyon zinciri, soruşturma sorumlusu
   - **İşe alım** — sözleşme şablonu, deneme süresi, rekabet yasağı duruşu, gizlilik/buluş klozları
   - **Fesih** — savunma usulü ve süresi, ihtar kademesi, ikale/ibraname, arabuluculukta sulh yetkisi, yüksek risk bayrakları
   - **Yönetmelik** — dosya yolu, TİS, gözden geçirme sıklığı
   - **Soruşturma** — gizlilik başlığı, A/B dosya ayrımı, görüşme açılış bildirimi metni, özet şablonları
   - **İş akışı** — matter workspaces, izin takibi sıklığı, genişleme takip dosyaları
   - **Entegrasyonlar** — ArthurLegal MCP, İK/bordro sistemi, belge deposu, Slack; düşüş yolları

3. **Sor:** "Neyi ayarlayalım? Bir bölüm seçin ya da değişikliği kendi cümlenizle anlatın."

4. **Değişikliği yap.** Mevcut değeri göster, yenisini al, aşağı akış etkisini açıkla, onay al, yaz. Örnekler:
   - *Yeni işyeri, toplam işçi 28 → 34 (aynı işkolu):* "İş güvencesi eşiği aşıldı (İş K. m. 18). `/termination-review` artık her davranış/verim nedenli fesihte geçerli sebep ve savunma (m. 19) kontrolü yapacak ve işe iade riskini hesaba katacak."
   - *Taraf modeli işveren → işveren + işçi:* "Her yeni matter'da çıkar çatışması kontrolü sorulacak (Av. K. m. 38); `Cross-matter context` `off` kalmalı."
   - *Savunma süresi yönetmelikte 3 iş günü → TİS'te 5 iş günü:* "`/investigation-open` ve `/termination-review` savunma istem yazısında TİS süresini kullanacak."
   - *Risk duruşu orta → temkinli:* "Daha çok fesih eskalasyona gider, ikale/ibraname dili daha korumacı olur, rekabet yasağına daha sıkı bakılır."
   - *Yeni ülke (Almanya):* "Eşik tablosuna yurt dışı satırı eklenir; kaynak `de_` araçları (ör. `de_norm_getir(kanun=\"KSchG\", norm=\"1\")`). `/expansion-kickoff Almanya` önerilir."

   Kullanıcı bir madde, eşik ya da süre söylüyorsa yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; değişen tutarları (kıdem tazminatı tavanı, asgari ücret) sabit yazma.

5. **Ortak profil değişiklikleri** (ad, sektör, iller/ülkeler, pratik ortamı) `~/.claude/plugins/config/claude-for-legal/firm-profile.md`'e yazılır:
   > Bu değişiklik tüm eklentileri etkiler — iller/ülkeler listesini okuyan her eklenti artık [yeni değer]i görür.

6. **Kapat:** "Tamam. Bir sonraki çıktı bunu yansıtacak. Başka bir şey var mı? `/arthurlegal:employment-legal-customize` her zaman çalışır."

## Korkuluklar

- **Bölümü silme.** Bir işyeri "kaldırılmak" istenirse `[Şu an çalışan yok — yeniden açılış için kurallar saklı]` işaretini öner; `[Not configured]` yapmanın o işyerine özgü işaretlemeyi düşüreceğini açıkla.
- **İç tutarsızlığı işaretle.** Ör. "işçi sayısı 30'un altında" + "her fesih işe iade riskiyle değerlendirilsin"; "işveren ve işçi tarafı" + `Cross-matter context: on`; "atak risk duruşu" + "her fesih dış avukata".
- **Güvence kaybını işaretle.** Madde atıflarının `tr_mevzuat_madde_getir` ile doğrulanması, çekilemeyen veride UYARI satırı, kaynak etiketleri ve `[review]` işareti yük taşır — kaldırma; ayarlamadan önce bedelini açıkla.
- **Bölüm anahtarlarını çevirme** (`## Outputs`, `## Matter workspaces`, `Active matter:` vb.) — diğer skill'ler bunları okur.
- **Tek seferde tek değişiklik.** Görüşmeyi baştan sorma.

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
