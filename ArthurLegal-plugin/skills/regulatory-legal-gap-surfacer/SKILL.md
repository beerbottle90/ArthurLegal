---
name: regulatory-legal-gap-surfacer
description: >
  Referans: /arthurlegal:regulatory-legal-gaps ve /arthurlegal:regulatory-legal-comments skill'lerinin dayandığı ortak
  açık ve görüş izleme çerçevesi. Açık politika açıklarını düzeltme durumuyla izler,
  policy-diff'in bulduğu açıkları alır, açık ve yaşlanan kalemleri gösterir, sahiplerine
  yönlendirir ve sahiplere gönderim başına onayla bildirim taslağı hazırlar. gaps ve comments
  skill'leri asıl işe başlamadan önce bunu yükler.
user-invocable: false
---

# Gap Surfacer

> Sahip bildirimleri varsayılan olarak açıktır. Bir sahibi çıkarmak için `owner_slack` alanını boş bırak.

## Gönderim başına onay — istisnasız

Herhangi bir mesajı (Slack, Teams ya da e-posta: atama bildirimi, gecikme hatırlatması, toplu bildirim, durum raporu) göndermeden önce:

1. Kullanıcıya tam olarak neyi kime göndereceğini göster: "Bunu [N] kişiye göndermek üzereyim: [önizleme]."
2. Açık bir "evet" bekle.
3. Mesajda künye, son tarih ya da uyum sonucu varsa ekle: "⚠️ Bu mesajdaki künyeler doğrulanmadı; güncel olduklarını teyit etmeden gönderiyorum. 'Uygulamadan önce doğrulayın' satırı ekleyeyim mi?"
4. Onaysız asla gönderme. Takvime bağlı olarak da, toplu olarak da, "dün de gönderilmişti" diye de.

Onaysız otomatik gönderim bu eklentideki en geri alınamaz eylemdir: eklentinin kendi doğrulama notunun "yanlış olabilir" dediği içeriği, kontrol imkânı olmayan kişilere gönderir. Bu ikisinin birleşimi incelemeyi atlayamaz.

## Matter context

Eklenti profilinde `## Matter workspaces` → `Enabled` `✗` ise (şirket içi kullanımda varsayılan) bu paragrafı atla; skill'ler practice-level bağlamla çalışır. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:regulatory-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

---

## Amaç

Açıklar bulunur, sonra unutulur. Bu skill açığı kapanana kadar izler ve kapatmaktan sorumlu kişiye hatırlatır.

## İzleyici

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml` dosyasındadır. Anahtarlar ve değerler İngilizce kalır; açıklamalar Türkçe.

> **comment-tracker.yaml notu:** `~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml` comments skill'inin kardeş dosyasıdır. reg-feed-watcher (taslak ve istişareleri otomatik kaydeder) ve comments (kullanıcının görüş kararlarını izler) yazar; şeması comments skill'indedir. Bu skill onu okumaz. Şemayı değiştirirsen iki kullanıcıyı da güncelle.

```yaml
gaps:
  - id: GAP-001
    requirement: "[düzenlemenin istediği, tek cümle]"
    regulation: "[ad + araçtan dönen citation]"
    policy_affected: "[politika adı ya da 'new policy needed']"
    gap_type: "partial"  # none | partial | full | new-policy | watch | comment-decision
    owner: "[politika kütüphanesindeki sahip]"
    owner_slack: "[Slack kullanıcı kimliği, biliniyorsa]"
    opened: 2026-10-26
    due: 2027-01-01  # yürürlük tarihi, geçiş süresinin sonu, kurum ihtarındaki giderme süresi, iç son tarih ya da görüş son tarihi
    status_verified: true  # policy-diff kuralın yürürlükte olduğunu teyit edemediyse false; doğrulanmamış kalem hiçbir zaman 🔴 Overdue olmaz
    status: "open"  # open | in-progress | closed | risk-accepted
    notified: false  # atama bildirimi gönderilince true
    resolution: ""  # kapanışta doldurulur
```

**`due` nereden gelir.** Düzenlemenin yürürlük maddesi ya da geçiş hükmü; kurumun yazılı ihtarındaki giderme süresi (ör. elektrik piyasasında ikincil mevzuata ya da Kurul kararına aykırılıkta aykırılığın giderilmesi için verilen ihtar süresi: 6446 m. 16/1-b); iç son tarih; taslak ve istişarede görüş son tarihi. Hangisi olduğunu `due` satırının yanına yorum olarak yaz.

**Dava açılmış olması tarihi durdurmaz.** Düzenlemeye karşı dava açılması işlemin yürütülmesini durdurmaz; yürütmeyi durdurma kararı ayrı şartlara bağlıdır (İYUK m. 27/1, 27/2). Kuralı dava edilmiş diye açığı `watch`'a çekme; yürütmeyi durdurma kararı varsa `status_verified: false` yap ve nedenini yaz.

**Doğrulanmamış kuralda Overdue yok.** 🔴 Overdue "bağlayıcı bir süreyi kaçırdık" demektir. Kuralın durumu doğrulanmadıysa (policy-diff `status_verified: false` yazdıysa, ya da kural 12 aydan eski, yürürlük tarihi geçmiş ve güncelliği teyit edilmemişse; AYM iptali, Danıştay yürütmeyi durdurma kararı, değişiklik ya da erteleme kontrol edilmediyse) süre bağlayıcı olmayabilir. 🟡 "İnceleme gerekli" kullan ve yaz: "Kural yayımlandığı hâliyle yürürlükteyse bu [N] gün gecikmiş olur. Eskale etmeden önce kuralın durumunu doğrula." Doğrulanmamış kuralı aktif gecikme ve yaklaşan son tarih kovalarına değil `watch`'a koy; `watch`'ın yeniden değerlendirme tarihi, kalem yeniden uyum açığı olarak çıkmadan önce durum kontrolünü zorlar.

**`gap_type` anlamları:**

| Değer | Anlamı | Hatırlatma |
|---|---|---|
| `none` | Politika gerekliliği zaten karşılıyor; yalnız denetim izi için kaydedilir. Seyrek olmalı; kayıtların çoğu `none` ise karşılaştırma büyük ihtimalle yanlış politikaya karşı yapılmıştır. | Otomatik hatırlatma yok. |
| `partial` | Politika konuyu ele alıyor ama yeni gerekliliği tam karşılamıyor; değişiklik gerekir. | Son tarihten 30 gün önce. |
| `full` | Politika yeni gereklilikle çelişiyor ya da hiç değinmiyor; yeniden yazım ya da yeni bölüm gerekir. | Son tarihten 30 gün önce. |
| `new-policy` | Bunu karşılayan politika yok; yazılması gerekir. | Son tarihten 30 gün önce. |
| `watch` | İleriye dönük kalem: istişare, görüşe açılmış ama yayımlanmamış taslak, TBMM'deki kanun teklifi ya da durumu doğrulanmamış kural. Bugün uyum yükümlülüğü yok. `due` yeniden değerlendirme tarihidir (beklenen yayım ya da bir yıllık ufuk), uyum son tarihi değildir. | Otomatik hatırlatma yok; kural yayımlanınca ya da tarih gelince yeniden değerlendir. |
| `comment-decision` | Görüş kararı bekleyen taslak ya da istişare. `due` görüş son tarihidir. | Son tarihten 21 gün önce (görüş hazırlama penceresi kısadır). |

`watch` ve `comment-decision` kalemleri uyum açığı değildir; kural öncesi izleme kayıtlarıdır. Durum raporunda ayrı kovada göster ki sabah okuyan avukat "kurum fark etmeden düzelt" ile "göz kulak ol"u bir bakışta ayırsın.

## Modlar

### Mod 1: policy-diff'ten alma

policy-diff açık bulunca `gap-tracker.yaml`'a ekle. Mükerrer kayıt yapma: aynı gereklilik + aynı politika = aynı açık. policy-diff kapsamı daraltılmış bir karşılaştırma ise (⚠️ KAPSAM SINIRI başlığı) o başlığı her ilgili kayda aynen taşı.

**Aldıktan sonra sahibi bilgilendir.** Slack (ya da profildeki kanal) bağlıysa ve `owner_slack` doluysa, en baştaki gönderim başına onaydan sonra:

```
📋 Size yeni bir uyum açığı atandı

Açık: [GAP-ID] — [gereklilik, tek cümle]
Düzenleme: [ad + bağlantı]
Etkilenen politika: [politika adı ya da "yeni politika gerekli"]
Son tarih: [tarih ve türü]

Açık izleyicinin tamamı: /arthurlegal:regulatory-legal-gaps
```

Gönderdikten sonra kayıtta `notified: true` yap. Kanal bağlı değilse durum raporunda bildirimin gönderilmediğini yaz ve elle takip için işaretle.

### Mod 2: Durum raporu

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

## Açık Uyum Açıkları — [tarih]

### Sonuç

[N açık [tarih]e kadar işlem gerektiriyor — ilk üçü: X, Y, Z]

### 🔴 Overdue

| ID | Gereklilik | Politika | Sahip | Son tarih | Geçen gün |
|---|---|---|---|---|---|

### 🟠 30 günden az kalan

[aynı tablo]

### 🟡 Açık

[aynı tablo; doğrulanmamış kural kaynaklı "İnceleme gerekli" satırları da burada, notuyla]

### 👀 İzleme kalemleri (kural öncesi)

[`watch` ve `comment-decision` kayıtları. Uyum açığı değildir; ayrı tutulur ki gecikme ve yaklaşan son tarih kovalarında yalnız gerçek uyum süreleri kalsın.]

| ID | Kalem | Tür (taslak / istişare / kanun teklifi / durumu doğrulanmamış) | Görüş ya da yeniden değerlendirme tarihi | Sahip |
|---|---|---|---|---|

### Devam eden

[aynı tablo]

### Yakında kapananlar

[son 5, kapanış notuyla]

---

**En eski açık:** [ID], [N] gün
**Sahibe göre:** [dağılım]
**Gönderilen sahip bildirimi:** [N] / [toplam]

---

**Her açık için sonraki adım:** `/arthurlegal:regulatory-legal-policy-redraft`, `[doğrula]` etiketli işaretli bir politika taslağı ve değişiklik özeti üretir. Politika sahibinin incelemesi için öneridir; kaynak belgeye doğrudan müdahale değildir.

---

**Atıfları doğrula.** Bu izleyicideki künyeler önceki adımlarda (reg-feed-watcher ve policy-diff) yapay zekâ desteğiyle üretildi. Bir açığı kapatmadan ya da risk kabulüne almadan — veya bir iç beyan, yönetim kurulu raporu ya da kuruma cevapta kullanmadan — dayanak kuralı Resmî Gazete, mevzuat.gov.tr ya da kurumun sitesinden doğrula. Önceki adımlardan taşınan kaynak etiketleri (ör. `[ArthurLegal TR — tr_resmi_gazete_tara — GG.AA.YYYY]`, `[web araması — doğrula]`) künyenin nereden geldiğini gösterir; `doğrula` etiketliler önce kontrol edilir. Etiketleri silme.
```

## Ayar eksikse

Bu skill açık sahiplerini `## Policy library` tablosunun Owner sütunundan, triyaj ve eskalasyonu `## Gap response process` altındaki `**Who triages regulatory changes:**` ve `**Escalation for material gaps:**` satırlarından okur. Gereken değer boşsa ya da `[PLACEHOLDER]` ise:
- **Triyaj sorumlusu yok:** atamayı açık bırak ve ekle: "`## Gap response process` altında `**Who triages regulatory changes:**` boş. Yeni açıkların yönlendirilmesi için `/arthurlegal:regulatory-legal-cold-start-interview --redo` ile ya da profili düzenleyerek atayın."
- **Yeni açığın sahibi bilinmiyor:** `owner: [unassigned]` ile kaydet ve ekle: "Politika kütüphanesi etkilenen politika için sahip göstermediğinden [N] açık sahipsiz kaydedildi. Yönlendirme için kütüphanedeki Owner sütununu doldurun."
- **Gecikmiş önemli açık için eskalasyon yolu yok:** yine gecikmiş olarak raporla ve ekle: "Gecikmiş önemli açıklar için eskalasyon yolu tanımlı değil. `/arthurlegal:regulatory-legal-cold-start-interview --redo` ile ya da profili düzenleyerek tanımlayın."

Değerler doluysa ayardan söz etme.

**Son tarih hatırlatma mantığı** (durum raporunda ve zamanlanmış ajanda çalışır). Hatırlatma sıklığı `gap_type`'a bağlıdır: uyum açığına 30 gün, görüş kararına 21 gün önceden haber; `watch`'a otomatik hatırlatma yok.

"open" ya da "in-progress" her kayıt için:
- `partial`, `full`, `new-policy`, `none`: son tarihe 30 günden az kaldıysa ve son 7 günde hatırlatma gönderilmediyse "⏰ Hatırlatma: uyum açığına [N] gün kaldı" başlıklı mesajı ÖNİZLE ve onay bekle.
- `comment-decision`: görüş son tarihine 21 günden az kaldıysa ve son 7 günde hatırlatma gönderilmediyse "💬 Görüş kararı için [N] gün kaldı" başlıklı mesajı ÖNİZLE ve onay bekle.
- `watch`: otomatik hatırlatma yok. İzleyici gözden geçirilirken ya da aynı düzenleme için kural yayımlanınca yeniden bak.
- Uyum açığının son tarihi geçtiyse: raporda gecikmiş göster, mesajı ÖNİZLE, onay bekle.
- `comment-decision` kaleminin son tarihi geçti ve görüş sunulmadıysa: gecikmiş göster, mesajı ÖNİZLE, onay bekle; sahibinden kaydı notuyla birlikte `risk-accepted` (bilinçli olarak görüş verilmedi) ya da `closed` (görüş sunuldu) yapmasını iste.
- Hatırlatma zamanlarını kayda yaz ki tekrar tekrar rahatsız etmeyesin.
- Toplu hatırlatma da onay ister: "12 mesaj göndermek üzeresiniz" önizlemesi ve "evet" yeterlidir; sessizce toplu gönderim yeterli değildir.

### Sonuç doğuran eylem kapısı (uyum beyanı)

**Bir açığı çözüldü diye kapatmadan ya da bir düzenleyici gerekliliğe uyumu beyan eden herhangi bir çıktı (iç beyan, yönetim kurulu raporu, denetim cevabı, kuruma cevap) üretmeden önce** profildeki `## Who's using this` bölümünü oku. Rol **Non-lawyer** ise:

> Uyum beyan etmek ya da bir açığı çözüldü diye kapatmak hukuki sonuç doğurur. Beyan sonradan yanlış çıkarsa şirket aleyhine kullanılabilir; erken kapanış riski açık bırakır. Kuruma verilen bilgi ayrıca yaptırıma konu olabilir: örneğin elektrik piyasasında Kurumun bilgi istemesinde yanlış, eksik ya da yanıltıcı bilgi verilmesi ihtar ve idari para cezasına bağlanmıştır (6446 m. 16/1-a). Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet:
>
> - Açık (gereklilik, kaynak, karşılaştırmanın bulduğu)
> - Önerilen çözümün neyi kapsayıp neyi kapsamadığı
> - Kalan açık ya da belirsizlik
> - Açık sorular
> - Ne ters gidebilir (fazla geniş beyan, çözülmemiş kalan yükümlülük, önceki tutumla çelişki)
> - Avukata sorulacaklar (gerçekten kapandı mı; gerekçeli risk kabulü daha mı doğru; dış avukat görüşü gerekir mi)
>
> Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık bir "evet" olmadan açığı kapalı işaretleme ve uyum beyanı üretme. Durum raporları ve izleme görünümleri kapıya tabi değildir.

### Mod 3: Açığı kapatma

```
/arthurlegal:regulatory-legal-gaps --close GAP-001
Resolution: "Politika v2.3 güncellendi, [tarih]te onaylandı"
```

Durumu `closed` yapar; kapanış notunu ve tarihini kaydeder.

### Mod 4: Risk kabulü

Bazen cevap "bunu düzeltmeyeceğiz"dir. Geçerli bir karardır ama belgelenmelidir.

```
/arthurlegal:regulatory-legal-gaps --accept GAP-002
Rationale: "Gereklilik yalnız [karşılamadığımız koşul] için geçerli. [Tetikleyici] olursa yeniden bak."
Accepted by: [yetkili kişi]
```

Durum `risk-accepted` olur. Kayıt silinmez ama açık raporundan çıkar. Önemli bir açıkta kabul edenin yetkisini `**Escalation for material gaps:**` satırıyla karşılaştır; yetkisi görünmüyorsa kaydetmeden önce eskalasyonu öner.

## Entegrasyon: reg-change-monitor ajanı

Ajanın digest'i açık sayısını ve en eski açığın yaşını içerir. Gecikmiş bir şey varsa digest'in en üstüne yazılır. Ajan son tarih hatırlatma kontrolünü de çalıştırır; ama mesajlar burada da gönderim başına onaya tabidir: gözetimsiz çalışmada göndermez, "onay bekleyen bildirimler" olarak listeler.

## Kapanış

Profildeki `## Outputs` karar ağacıyla bitir; seçenekleri bu çıktıya uyarla (X'i yaz, eskale et, olgu topla, izle ve bekle, başka bir şey). Ağaç çıktıdır; seçimi avukat yapar.

İzleyicide yaklaşık 10'dan fazla açık açık varsa ya da kullanıcı isterse panoyu öner (profil `## Outputs → Dashboard offer for data-heavy outputs`): önem derecesine göre sayılar, son tarihe göre açık zaman çizelgesi, sahip, durum ve son işlem tarihiyle sıralanabilir tablo.

## Bu skill ne yapmaz

- Açıkları kendiliğinden kapatmaz. Kapanış, kapanış notu ve notun anlattığı insan eylemiyle olur.
- Slack (ya da profildeki kanal) bağlı değilse bildirim göndermez; durum raporunda işaretler.
- Aynı açık için 7 günde birden fazla hatırlatma göndermez.
- Uyum beyanı ya da kuruma cevap metnini kapı onayı olmadan üretmez.

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
