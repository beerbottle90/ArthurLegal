---
name: commercial-legal-escalation-flagger
description: >
  Bir sözleşme sorununu `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`
  içindeki eskalasyon matrisine göre doğru onaylayana yönlendirir ve talep metnini
  taslak olarak yazar; imzalayacak kişinin temsil yetkisini (TTK m. 370, 371, 373; iç yönerge
  m. 367) ayrıca kontrol ettirir. Kullanıcı "bunu kim onaylamalı", "eskale et", "hukuk
  müşaviri onayı gerekir mi", "onaya yönlendir" dediğinde ya da başka bir skill
  incelemecinin yetkisini aşan bir sorun bulduğunda kullan.
argument-hint: "[sorunu anlatın ya da inceleme notuna atıf yapın]"
---

# /escalation-flagger

Sorunu matrisle eşleştirir, onaylayanı adıyla söyler ve mesajı yazar — akşam beşte "bir dakikanız var mı" mesajı yazmak zorunda kalmayın diye.

## Talimat

1. Profili oku → `## Escalation`. Yoksa ya da belirsizse söyle: "Eskalasyon matrisi profilde yok/belirsiz — `/arthurlegal:commercial-legal-customize` ile ekleyelim."
2. Sorunu sınıflandır: tutar eşiği / kloz sapması / otomatik tetik / iş kararı / imza yetkisi.
3. Matrisle eşleştir, onaylayanı **adıyla ya da rolüyle** söyle — "hukuk yönetimi" değil.
4. Talep metnini şablona göre yaz: sözleşme ne diyor, playbook ne diyor, seçenekler ve öneri, karar tarihi.
5. **Gönderme.** Taslağı göster; avukat gönderir.

Örnek: `/arthurlegal:commercial-legal-escalation-flagger Tedarikçi çerçeve sözleşmesinde sorumluluk sınırsız — kim onaylar, ne yazayım?`

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise (kurum içi varsayılan) bu paragrafı atla. Açıksa ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:commercial-legal-matter-workspace switch <slug>` çalıştırın ya da 'uygulama düzeyi' deyin." Aktif matter'ın `matter.md`'sini ve sapmalarını yükle; çıktıyı `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Matrisi yükle

**Hangi taraf?** Önce sözleşmede şirketin tarafını belirle: karşı taraf mal/hizmet sağlıyorsa satın alma; ürünümüzü alıyorsa satış. Belli değilse sor. Eşleşen playbook bölümünü (`### Sales-side playbook` / `### Purchasing-side playbook`) oku — bir tarafta geri çekilme içinde kalan şart diğer tarafta "asla" olabilir. Talepte hangi playbook'un uygulandığını yaz.

Beklenen yapı:

| Can approve | Without escalation | Escalate to | Via |
|---|---|---|---|
| Sözleşme uzmanı | Standart şartlar, < [tutar] | Avukat | Slack |
| Avukat | Geri çekilme içinde, < [tutar] | Hukuk müşaviri | Slack / e-posta |
| Hukuk müşaviri | Diğer her şey | Genel müdür / yönetim kurulu | Toplantı |

Artı **tutardan bağımsız otomatik tetikler** (`**Automatic escalations regardless of dollar value:**`). Tutarları profildeki para birimiyle oku; döviz bedelli sözleşmede çevrim kuru ve tarihini talepte belirt.

## İş akışı

### Adım 1 — Sorunu sınıflandır

- **Tutar eşiği:** sözleşme bedeli birinin onay yetkisini aşıyor.
- **Kloz sapması:** şart playbook geri çekilmelerinin dışında.
- **Otomatik tetik:** her zaman eskale edilen kalemlerden biri var.
- **İş kararı:** hukuki değil; iş sahibine gider.
- **İmza yetkisi:** onay alınsa bile imzalayacak kişinin temsil yetkisi belirsiz (aşağıda).

Gerçekten sorun olmayanı eskale etme: şart profildeki geri çekilmeler içindeyse yukarı gitmez.

**Türk hukukunda sık otomatik tetikler** (profilde yoksa avukata "bunu listeye ekleyelim mi?" diye sor):
- Kast ve ağır kusuru da kapsayan sorumsuzluk ya da tavan — önceden yapılan bu anlaşma kesin hükümsüzdür (TBK m. 115/1); satış tarafında koruma sandığımız kloz boşa düşer.
- Tacir olarak kabul edilen yüksek cezai şart — tacir borçlu aşırılık iddiasıyla indirim isteyemez (TTK m. 22; genel kural TBK m. 182/3).
- Yurt dışına kişisel veri aktarımı ve standart sözleşme — imzadan itibaren beş iş günü içinde Kurum'a bildirim (KVKK m. 9/5).
- Yabancı hukuk ve yabancı yerde tahkim/mahkeme → ayrıca `/arthurlegal:commercial-legal-governing-law-review`.
- Tek pay sahipli AŞ ile pay sahibi arasındaki sözleşme — piyasa şartlarındaki günlük, önemsiz ve sıradan işlemler dışında yazılı şekil geçerlilik şartıdır (TTK m. 371/6; Ltd. için m. 629/2).

### Adım 2 — Matrisle eşleştir

Sırayla: **otomatik tetik mi?** → evetse o tetik için adı geçen kişiye. **Bedel incelemecinin eşiği üstünde mi?** → evetse o tutardaki yetkiliye. **Şart tüm geri çekilmelerin dışında mı?** → evetse standart dışı şartı onaylayabilene. Hiçbiri değilse incelemeci onaylayabilir — eskalasyon yok.

### Adım 3 — Onaylayanı adıyla söyle

Profildeki kişiyi ya da rolü yaz. Matris bu durumu kapsamıyorsa söyle: "Eskalasyon matrisi [durum]u kapsamıyor. Kimin sahiplendiğini [hukuk müşaviri]ne sormanızı öneririm."

### Adım 4 — İmza yetkisini kontrol et

İç onay ile dış temsil yetkisi ayrı şeylerdir. Onay matrisi şirketin iç düzenidir (yönetim devri iç yönergeyle düzenlenir, TTK m. 367); sözleşmeyi şirketi bağlayacak şekilde imzalayanın yetkisi ise ticaret sicilinden okunur:
- AŞ'de esas sözleşmede aksi öngörülmemiş veya yönetim kurulu tek kişiden oluşmuyorsa temsil yetkisi çift imzayla yönetim kuruluna aittir; yetki murahhas üyelere ya da müdürlere devredilebilir (m. 370).
- Temsile yetkililer ve temsil şekilleri ticaret siciline tescil ve ilan edilir (m. 373/1). İç sınırlamalar iyiniyetli üçüncü kişiye karşı hüküm ifade etmez; yalnız tescil ve ilan edilen merkez/şube ya da birlikte kullanma sınırlamaları geçerlidir (m. 371/3).
- Sınırlı yetkili ticari vekil ve diğer tacir yardımcıları iç yönergeyle görev ve yetkileri belirlenerek atanabilir; iç yönergenin ve bu kişilerin tescil ve ilanı zorunludur (m. 371/7). Ltd.'de anonim şirket hükümleri kıyasen uygulanır (m. 629).

Talebe ekle: imzalayacak kişi, imza sirküleri / sicil kaydındaki yetki şekli (tek/çift, sınır), karşı tarafın imzacısının yetkisi teyit edildi mi (güncel imza sirküleri ya da Türkiye Ticaret Sicili Gazetesi ilanı). Yetki belirsizse bu da ayrı bir eskalasyon kalemidir. Yabancı karşı tarafta: tüzel kişi kimliği için `gleif_search_entities`, temsil kuralı için o ülkenin hukuku — `/arthurlegal:commercial-legal-governing-law-review`.

### Adım 5 — Talebi yaz

Onaylayan mesajdan karar verebilmeli — "sözleşmeyi açayım" demeden.

```markdown
**Eskale edilen:** [isim / rol]
**Kanal:** [Slack #kanal / e-posta / toplantı — profile göre]
**Aciliyet:** [varsa son tarih]
**Uygulanan playbook:** [satış / satın alma]

---

Merhaba [isim],

[Karşı taraf] [sözleşme türü] için kararınız gerekiyor. [İş bağlamı — tek cümle.]

**Sorun:** [Sade dille tek paragraf: ne istiyorlar, neden standart dışı, gerçek risk ne.]

**Sözleşme ne diyor:**
> "[birebir alıntı — madde no]"

**Playbook ne diyor:** [profilden alıntı]

**Hukuki not:** [varsa doğrulanmış madde atfıyla tek cümle — ör. TBK m. 115/1, TTK m. 22]

**Seçenekler:**
1. **Kabul** — [neden olabilir, tek satır]
2. **Karşı öneri:** "[önerilen metin]" — [karşı tarafın muhtemel tepkisi]
3. **Vazgeç** — [iş bağlamında gerçekçi mi]

**Önerim:** [hangisi, kısaca neden]

**İmza:** [imzalayacak kişi + sicildeki yetki şekli; karşı taraf imzacısı teyit edildi mi]

**Karar için son tarih:** [tarih]

[Tam inceleme notunun bağlantısı]
```

Madde atfı yazacaksan önce `tr_mevzuat_madde_getir` ile çek; çekilemezse "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" yaz.

### Adım 6 — Eskalasyonu kaydet

Ekip bilet sistemi ya da CLM onay akışı kullanıyorsa oraya işle. Kullanmıyorsa inceleme notuna eskalasyonun kime, ne zaman gönderildiğini yaz; notu okuyan sonraki kişi durumu görmeli. Matter açıksa `history.md`'ye de ekle.

## Ayar: şüphedeysen notla eskale et

Gereksiz eskalasyonun bedeli onaylayanın ~30 saniyesidir; kaçırılan eskalasyonun bedeli onaysız bir şartı imzalamaktır — geri dönüşü olmayan kapı. **Şüphedeysen eskale et.** Ölçü bu skill'de değil profildedir: açıkça geri çekilme içindeyse eskalasyon yok; açıkça dışında ya da otomatik listedeyse eskale et; belirsizse (muğlak, yeni ya da "içinde" demek zorlama) yine eskale et, onaylayanın karar vermesi gereken soruyu ve neden emin olunamadığını yaz — onaylayan daraltır, skill değil.

Aşırı eskalasyon onaylayanı alıştırır diye eskalasyonu bastırma; bu, avukatın eşikleri ayarlayarak çözeceği bir sorundur. Playbook'un değinmediği bir şartta eşiği tahmin etme — avukata sor ve cevabı profile yazmayı öner.

## Bu skill ne yapmaz

- Onay vermez; yönlendirir.
- Seçenekler arasında karar vermez; öneri yazar, onaylayan karar verir.
- Mesajı göndermez; taslak yazar, avukat okuyup gönderir.
- Ticaret sicilini kendisi sorgulamaz; imza sirküleri ya da sicil kaydı kullanıcıdan istenir.

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
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/arthurlegal:legal-research-az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/arthurlegal:legal-research-sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
