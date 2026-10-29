---
name: regulatory-legal-policy-redraft
description: /arthurlegal:regulatory-legal-gaps ya da /arthurlegal:regulatory-legal-policy-diff'in bulduğu bir açığı kapatan, işaretli (redline) bir politika taslağı önerir. İç inceleme için ilk taslaktır; onaylı politika belgesine doğrudan uygulanmaz. "Politikayı yeniden yaz", "politika düzeltmesini taslakla", "politikayı işaretle" denince ya da gap-surfacer bir açığı taslak için devrettiğinde kullan.
argument-hint: "[GAP-ID ya da açığın tarifi]"
---

# /policy-redraft

1. Profili yükle: `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → `## Policy library` ve uygulama profili; ortak bilgi için `firm-profile.md`.
2. Aşağıdaki iş akışını uygula.
3. Girdileri topla: açık (`/arthurlegal:regulatory-legal-gaps` çıktısından ya da doğrudan tarif), güncel onaylı politika metni, kural metni.
4. Kuralın güncel olduğunu doğrula (policy-diff Adım 0). Doğrulayamazsan `⚠️ KURAL DURUMU DOĞRULANMADI` başlığını koy.
5. Etkilenen politika bölümlerinin işaretli taslağını üret: mümkün olan en küçük değişiklik, `[doğrula]` etiketleri taşınır, her değişikliğin NEDENİ satır içi yorumla açıklanır.
6. Politika Yeniden Yazım Notu üret. `[policy-name]-proposed-redraft-[YYYY-MM-DD].md` adlı yeni bir dosyaya yaz — kaynak politika belgesine asla yazma.
7. İzleyicide açığı KAPATMA. Açık, taslak uygulanıp ONAYLANDIĞINDA kapanır; bu politika sahibinin işidir.

---

> Bu skill bir **öneri** üretir, düzenleme yapmaz. Açıkça taslak olduğu belli bir adla yeni dosyaya yazar. Kaynak politika belgesinin üzerine asla yazmaz ve izleyicide açığı asla kapatmaz — açık, taslak politika sahibince uygulanıp onaylandığında kapanır.

## Matter context

Eklenti profilinde `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:regulatory-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

---

## Amaç

gap-surfacer açığı bulur; policy-diff neyin değişmesi gerektiğini söyler. Bu skill bir adım ileri gider ve etkilenen politika bölümünün işaretli taslağını üretir: küçük, somut, etiketli; politika sahibinin incelemesi için ilk taslak.

## Kesin sınırlar — önce bunları oku

Bunlardan biri çiğnenecekse dur ve sor.

1. **Bu bir ÖNERİDİR, düzenleme değil.** Kaynak politika belgesine asla doğrudan yazma. Çıktı `[policy-name]-proposed-redraft-[YYYY-MM-DD].md` adlı yeni dosyaya ya da matter çalışma alanına gider; `[policy-name].md`'ye değil.
2. **İzleyicide açığı asla kapatma.** Açıklar taslak UYGULANIP ONAYLANDIĞINDA kapanır; bu politika sahibinin işidir. Kullanıcı "taslağı yazdın, açığı kapat" derse reddet: "Ben öneriyi üretiyorum. Açık, değişikliği inceleyip uygulayıp onayladığınızda kapanır. O zaman söyleyin, izleyiciyi güncellerim."
3. **"Bunu benim yerime uygula" kapsam dışıdır.** Kullanıcı taslağı kaynak politikaya uygulamamı isterse: "Politika değişikliğini ben uygulamam; inceleme ve onaydan sonra politika sahibinin işidir. Öneriyi ben üretirim. İncelenip onaylandığında söyleyin, açık izleyiciyi güncellerim."
4. **Taslaktan önce politika sürümünü teyit et.** Dosya verildiyse sor: "Bu politikanın onaylı ve en güncel sürümü mü? Eski bir sürüme karşı yazılan taslak ayrışma yaratır." Metin yapıştırıldıysa güven ama inceleyen notunda işaretle.
5. **Mümkün olan en küçük değişiklik.** Cümleden önce kelime, paragraftan önce cümle, bölümden önce paragraf çiz. Yalnız açıktan etkilenen bölümlere dokun. Politikanın üslubunu yeniden düzenleme.
6. **`[doğrula]` etiketlerini taşı.** Model bilgisinden ya da doğrulanmamış kaynaktan gelen her yürürlük tarihi, eşik, atıf ya da gereklilik yalnız notta değil, taslağın içinde de etiketlenir. Dönemsel güncellenen tutarları (idari para cezası, parasal sınırlar) politikaya sabit yazma; "güncel tutar [doğrula]" diye bırak.

## Adım 1: Girdileri topla

Üç girdi gerekir. Biri eksikse sor; çıkarsama yapma.

### 1a. Açık

Biri:
- İzleyiciden bir `GAP-ID` — kaydı `~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml` dosyasından (ya da matter düzeyindeki karşılığından) yükle.
- Kullanıcının mesajında tarif edilen açık — gerekliliği, düzenlemeyi ve etkilenen politikayı yakala.
- `/arthurlegal:regulatory-legal-policy-diff` çıktısından yapıştırılan karşılaştırma özeti.

### 1b. Güncel politika metni

Biri:
- Dosya yolu — oku, sonra sor: "Bu politikanın onaylı ve en güncel sürümü mü?" Cevabı inceleyen notuna yaz.
- Yapıştırılmış metin — güven ama inceleyen notunda işaretle: "Politika metni doğrudan yapıştırıldı; güncel onaylı sürüm olduğunu varsaydım. Uygulamadan önce teyit edin."
- Hiçbiri — iste. Politika metnini izleyiciden ya da web aramasından tahmin etme.

### 1c. Kural metni

Biri:
- Karşılaştırma çıktısı (kural çıkarılmış ve etiketlenmiş).
- Araçla çekilmiş düzenleme: `tr_mevzuat_madde_getir`, `tr_resmi_gazete_getir`, `tr_kurum_karari_getir` — `citation` alanı birebir, kaynak etiketiyle.
- Kullanıcının yapıştırdığı kural metni — `[kullanıcı verdi]`.

Kural metni eksik ya da belirsizse **sessiz tamamlama yok** kuralını uygula: seçenekleri sun (tam metni yapıştır, birincil kaynağı göster, `doğrula` etiketli web araması, dur) ve bekle.

## Adım 2: Kuralın güncel olduğunu doğrula

policy-diff Adım 0'daki kontrolü aynen uygula: konsolide metindeki "(Değişik/Ek/Mülga/İptal)" notları ve geçici maddeler, AYM norm denetimi (`tr_aym_ara(kind="norm", …)`), Danıştay iptal ya da yürütmeyi durdurma (`tr_ictihat_ara(courts=["DANISTAYKARAR"], …)`), sonraki RG değişiklikleri. Uyarı işaretleri: yürürlük tarihi 30 günden fazla geçmiş ve ertelenmediği teyit edilmemiş; kural 12 aydan eski; tartışmalı ve dava konusu olabilecek bir düzenleme.

Doğrulayamazsan:

> `⚠️ KURAL DURUMU DOĞRULANMADI — Bu kuralın şu anda yürürlükte olduğunu teyit edemedim. Yayımlanan düzenlemeler sonradan değiştirilebilir, ertelenebilir, iptal edilebilir ya da yürütmesi durdurulabilir. Durumunu mevzuat.gov.tr, Resmî Gazete ve AYM/Danıştay kararlarından ya da dış avukattan teyit etmeden bu taslağı uygulamayın.`

Bu başlığı üst başlığın üstüne koy. Taslaktaki her yürürlük ve uyum tarihini `[yayımlanan metne göre — durum doğrulanmadı]` diye etiketle.

## Adım 3: Taslağı üret

Etkilenen politika bölümünün işaretli hâli.

### Kural

- Çizilen metin: `~~çizilen metin~~`
- Eklenen metin: **eklenen metin**
- Her değişiklik NEDENİNİ açıklayan satır içi yorum taşır — kural, atıf, kapanan açık:

  > `[Değişiklik: standart sözleşmenin Kuruma bildirimi eklendi — imzaların tamamlanmasından itibaren beş iş günü; bildirim tarafı sözleşmede belirlenmemişse veri aktaran (Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik m. 14/5) [ArthurLegal TR — tr_mevzuat_madde_getir — GG.AA.YYYY]]`

- Model bilgisinden ya da doğrulanmamış kaynaktan gelen her yürürlük tarihi, eşik, atıf ya da gereklilik satır içinde `[doğrula]` etiketi alır; yalnız değişiklik özetinde değil.
- Karşılaştırmadan gelen kaynak etiketlerini taşı: `[ArthurLegal TR — <araç> — GG.AA.YYYY]`, `[web araması — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`. Karşılaştırmadan taslağa geçerken silme.

### Kapsam disiplini

Politikanın bir bölümü açıktan etkilenmiyorsa ona dokunma. Açığın dışındaki bölümlere dokunan taslak, yapay zekânın sorulmadığı konularda görüş bildirdiği izlenimini verir ve incelemeyi zorlaştırır.

Taslağı yazarken ikinci bir açık görürsen (kuralla açıkça uyumsuz ama asıl açıkta olmayan bir hüküm) sessizce düzeltme. İnceleyen notunda işaretle: "[GAP-ID] için taslak yazarken [diğer hüküm]ün [gereklilik] ile ilgili bir sorunu olduğunu fark ettim. Bu taslağa dahil edilmedi. Ayrı bir açık açılmasını düşünün."

## Adım 4: Çıktı — Politika Yeniden Yazım Notu

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

> **⚠️ İnceleyen notu**
> - **Kaynaklar:** [ArthurLegal MCP (`tr_`) ✓ doğrulandı | bağlı değil — atıflar model bilgisinden, dayanmadan önce doğrula]
> - **Okunan:** [politikanın incelenen bölümleri; okunmayanlar]
> - **Takdirinize bırakılan:** [satır içinde `[incele]` işaretli N kalem | yok]
> - **Güncellik:** [kural durumu [kaynak], [tarih] itibarıyla doğrulandı | doğrulanmadı — yukarıdaki başlığa bakın]
> - **Dayanmadan önce:** bunun politikanın güncel onaylı sürümü olduğunu teyit et; kuralın durumunu ve yürürlük tarihini doğrula; politika sahibinin incelemesini al; politika değişikliği onay sürecini izle; açık izleyiciyi yalnız uygulanıp onaylandığında güncelle.

## Politika Yeniden Yazımı: [Politika adı]

**Açık:** [GAP-ID ya da kısa tarif]
**Düzenleme:** [araçtan dönen citation, yürürlük tarihi]
**Politika:** [ad, son güncelleme tarihi]
**Durum:** ÖNERİ — henüz incelenmedi ya da onaylanmadı

### Sonuç

[Bir cümle: açık ne. Bir cümle: taslak ne yapıyor. Bir cümle: neyin incelenmesi gerekiyor.]

### İşaretli politika bölüm(ler)i

[Satır içi `[Değişiklik: ...]` yorumlarıyla işaretli metin. Yalnız etkilenen bölümler.]

### Değişiklik özeti

| # | Hüküm | Mevcut | Önerilen | Neden | Kaynak |
|---|---|---|---|---|---|
| 1 | §3.2 Yurt dışı aktarım dayanağı | "…kişisel verileri ilgili kişinin açık rızasıyla yurt dışına aktarırız…" | "…yeterlilik kararı bulunan ülkelere; yoksa Kurulun ilan ettiği standart sözleşme gibi uygun güvencelerden biriyle; bunlar da yoksa yalnız arızi hâllerde aktarırız…" | 7499 s. Kanunla değişen KVKK m. 9: yeterlilik kararı → uygun güvence → arızi istisna (m. 9/1, 9/4, 9/6) | `[ArthurLegal TR — tr_mevzuat_madde_getir — GG.AA.YYYY]` |
| 2 | §3.5 Bildirim | (yok) | "Standart sözleşme değiştirilmeden kullanılır ve imzaların tamamlanmasından itibaren beş iş günü içinde Kuruma bildirilir." | KVKK m. 9/5; Yönetmelik m. 14/3, 14/5 | `[ArthurLegal TR — tr_mevzuat_madde_getir — GG.AA.YYYY]` |
| 3 | §6.1 İdari para cezası | "[tutar] TL'ye kadar" | "kanunda öngörülen idari para cezası" | Tutar dönemsel güncellenir; politikaya sabit yazılmaz | `[doğrula — güncel tutar]` |

### Uygulamadan önce — kontrol listesi

- [ ] Taslağın yazıldığı metnin politikanın güncel onaylı sürümü olduğunu teyit et.
- [ ] Kuralın durumunu ve yürürlük tarihini doğrula (mevzuat.gov.tr, Resmî Gazete, AYM/Danıştay ya da dış avukat).
- [ ] Politika sahibinin incelemesini al.
- [ ] Politika değişikliği onay sürecini izle.
- [ ] Açık izleyiciyi uygulanıp onaylandığında güncelle — öncesinde değil.

---

**Sırada ne var? Birini seçin, birlikte ilerletelim:**

1. **Uygula ve onay al** — siz incelersiniz, politika sahibine iletirsiniz, onay sürecinden geçirirsiniz. Onaylanınca söyleyin, açığı kapalı işaretlerim.
2. **[X] hakkında daha fazla bilgi** — bir değişikliğin dayanağı güçlendirilmeli mi (atıf doğrulama, tutar kontrolü, yabancı hukuk sorusu), hangisi olduğunu söyleyin, araştırayım.
3. **[Sahip / hukuk müdürü]ne eskale et** — taslak politika sahibinin yetkisini aşan bir şey doğuruyorsa olguları, önerilen değişikliği ve gereken kararı içeren kısa bir eskalasyon yazayım.
4. **İzle ve bekle** — kuralın durumu belirsizse ya da politika sahibine ulaşılamıyorsa açık izleyiciye yeniden değerlendirme notu ekleyeyim.
5. **Başka bir şey** — ne yapmak istediğinizi söyleyin.
```

## Dosya adı

Çıktı dosyasının adı taslak olduğunu açıkça göstermelidir:

`[policy-name]-proposed-redraft-[YYYY-MM-DD].md`

`[policy-name].md` değil. `[policy-name]-v2.md` değil. "proposed-redraft" sözcüğü ve tarih taşıyıcıdır; taslağın güncel sürümle karıştırılmasını önler.

Aktif matter varsa matter çalışma alanına; yoksa çalışma klasörüne ya da kullanıcının gösterdiği yere yaz. Politika kütüphanesinin kaynak klasörüne yazma.

## Ayar eksikse

- **Politika sahibi yok:** taslağı yine üret. İnceleyen notuna yaz: "`## Policy library` tablosunda [politika] için Owner tanımlı değil. Onay yolunun yönlendirilebilmesi için `/arthurlegal:regulatory-legal-cold-start-interview --redo` ile atayın."
- **Politika kütüphanesi boş ve açık belirli bir politika göstermiyor:** dur ve sor: "Taslak için güncel politika metnine ihtiyacım var. Etkilenen politikanın metnini yapıştırın ya da dosyayı gösterin."

Değerler doluysa ayardan söz etme.

## Diğer skill'lerle ilişki

- **Girdiler** `policy-diff`ten (gereklilik bazında açık analizi) ve `gap-surfacer`dan (izleyici) gelir. Kaynak etiketlerini ve `[doğrula]` işaretlerini taşı.
- **İzleyici durumu:** bu skill izleyiciyi DEĞİŞTİRMEZ. Açığı kapalı ya da devam ediyor işaretlemez, `notified` alanına dokunmaz. Taslağın varlığına iz bırakmak istenirse, taslak uygulanıp onaylandığında politika sahibi ya da kullanıcı kapanış notuyla kaydı günceller — bkz. `/arthurlegal:regulatory-legal-gaps --close`.
- **Önem tabanı:** yukarı akıştaki açık 🔴 ya da 🟠 ise notun Sonuç bölümü o önemi taşır. Sessizce düşürmek, inceleyen avukatın göremeyeceği bir çelişkidir. Bkz. profil `## Cross-skill severity floor`.
- **Konu skill'leri:** İK politikası için `/arthurlegal:employment-legal-policy-drafting`; aydınlatma metni için `/arthurlegal:privacy-legal-policy-monitor`.

## Kapanış

Karar ağacı yukarıdaki çıktı şablonunun içindedir. Seçenekleri taslağın gerçekte ürettiğine göre uyarla: kuralın durumu doğrulanmadıysa 2. seçenek (daha fazla bilgi) öne çıkar; politika sahibi tanımlı değilse 3. seçenek (eskalasyon) somutlaşır.

## Bu skill ne yapmaz

- Taslağı kaynak politikaya uygulamaz; bu politika sahibinin işidir.
- İzleyicide açığı kapatmaz; açıklar taslak uygulanıp onaylandığında kapanır.
- Politikanın tamamını yeniden yazmaz; açığı kapatan en küçük değişikliği yapar.
- Birden çok politikayı tek seferde yazmaz: bir açık, bir politika, bir not.
- "Uygula" iş akışını yürütmez; onay kapılı bir uygulama komutu ileride ayrı bir skill olabilir.

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
