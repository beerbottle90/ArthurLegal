---
name: corporate-legal-integration-management
description: >
  Kapanış sonrası M&A entegrasyon takibi — evreli iş planı, onay takibi, toplu
  sözleşme devri, haftalık durum raporu. Eldeki işlem belgelerinden (satın alma
  sözleşmesi, işlem özeti, kapanış listesi) başlar; M&A cold-start'ın
  deal-context.md ve closing-checklist.yaml dosyalarına bağlanır. Türk hukukundaki
  kapanış sonrası kalemleri (ticaret sicili tescil/ilan, pay defteri, SGK işyeri
  bildirgesi — 5510 m. 11, işyeri devri — İş K. m. 6, sözleşme devri — TBK m.
  205, SMK m. 148 sicil kaydı, birleşmede alacaklıya çağrı — TTK m. 157) iş
  planına yerleştirir. "Entegrasyon", "kapanış sonrası", "bekleyen onaylar",
  "sözleşme devri", "entegrasyon durumu", "işlemde ne kaldı" denildiğinde kullan.
argument-hint: "[--init | --contracts | --report | --update | --export [--format csv|table] [--section all|consents|contracts|workplan]] [--deal [code]]"
---

# /integration-management — Kapanış Sonrası Entegrasyon

1. `deal-context.md`'yi ve `firm-profile.md`'i yükle (işlem kodu, [Müvekkil] ve hedef, kapanış tarihi, işlem lideri, işlem yapısı).
2. `integration-tracker.yaml` varsa yükle (`--init`'te oluştur).
3. Bayrağa göre: `--init` Mode 1 (iş planı + onay takibi), `--contracts` Mode 2 (sözleşme listesi, katman), `--report` Mode 3 (durum raporu), `--update` Mode 4 (güncelleme), `--export` Mode 5 (CSV/tablo).
4. `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/integration-tracker.yaml` oku/yaz.
5. Her yazmadan sonra değişiklik özetini ve yeni işaretleri göster.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

İşlem kapanır, hukuki dağınıklık kalır. Bu skill kapanış sonrası entegrasyonun hukuk iş akışını yönetir — iş entegrasyonunu, BT sistemlerini, İK organizasyonunu değil: onaylar, sözleşme devirleri, şirket yapısının sadeleştirilmesi, sınai mülkiyet sicil kayıtları, satın alma sözleşmesinden (SPA/APA) doğan yükümlülükler. Neyin bittiğini, neyin vadesinin geldiğini, neyin engelli olduğunu ve neyin karar beklediğini izler.

## Takip dosyası

`deals/[code]/integration-tracker.yaml`. `closing-checklist.yaml` varsa kapanış sonrası kalemleri devral. Anahtarlar ve durum değerleri İngilizce kalır (dışa aktarım ve diğer skill'ler okur); açıklamalar Türkçe.

```yaml
metadata:
  deal_code: "[kod]"
  target: "[unvan]"
  structure: "[share_deal_as / share_deal_ltd / asset_deal / merger / demerger]"
  close_date: "[YYYY-MM-DD]"
  deal_lead: "[ad]"
  outside_counsel: "[büro ve sorumlu avukat]"
  last_updated: "[tarih]"
  last_status_report: "[tarih ya da null]"

pa_dates:
  required_consents_deadline: "[YYYY-MM-DD — sözleşmeden]"
  rep_survival_expires: "[YYYY-MM-DD — her beyan türü ayrı]"
  escrow_release: "[YYYY-MM-DD ya da null]"
  earnout_milestones:
    - description: "[kilometre taşı]"
      measurement_date: "[YYYY-MM-DD]"
      payment_date: "[YYYY-MM-DD]"
      owner: "finance"   # her zaman finans — hukuk yalnız tarihi izler

workplan:
  day_1:   { target_date: "[close_date + 7 gün]",   items: [] }
  day_30:  { target_date: "[close_date + 30 gün]",  items: [] }
  day_90:  { target_date: "[close_date + 90 gün]",  items: [] }
  day_180: { target_date: "[close_date + 180 gün]", items: [] }

required_consents: []
desired_consents: []

contracts:
  source: "[repository / manual-upload / disclosure-schedule]"
  repository_path: "[yol ya da null]"
  last_imported: "[tarih]"
  total: 0
  tier_1: []
  tier_2: []
  tier_3: []
  tier_4: []
```

**İş planı kalemi:** `id` (W-001), `description`, `phase` (day_1/day_30/day_90/day_180), `owner` (legal-owns / legal-supports), `workstream` (legal / hr / it / finance / real-estate / other), `priority` (critical / high / medium / low), `deadline`, `deadline_basis` (pa-obligation / regulatory / best-practice), `status` (not_started / in_progress / complete / blocked / deferred), `blocker`, `depends_on`, `notes`.

**Onay kaydı:** `id` (CON-001), `counterparty`, `contract_type` (customer / vendor / lease / IP-license / financial / public / other), `required_consent` (true = sözleşmenin Gerekli Onaylar ekinde), `pa_deadline` (yalnız true için), `status` (not_started / outreach_sent / in_negotiation / obtained / waived / refused), `assigned_to`, `outreach_date`, `obtained_date`, `notes`.

**Sözleşme kaydı:** `id` (C-001), `name`, `counterparty`, `contract_type`, `annual_value` (tutar + para birimi ya da unknown), `assignment_mechanism` (auto-assign / consent-required / coc-provision / silent / not_reviewed), `tier` (1-4), `required_consent`, `pa_deadline`, `status` (not_reviewed / no_action / consent_pending / outreach_sent / in_negotiation / consent_obtained / assignment_complete / waived / refused / coc_triggered), `assigned_to`, `notes`, `last_updated`.

## Mode 1: Başlat (`--init`)

### Adım 1: İşlem bağlamı

`deals/[code]/deal-context.md`'yi oku; yoksa işlem kodu, hedef, **işlem yapısı**, kapanış tarihi, işlem lideri ve dış avukatı sor ve yaz. `closing-checklist.yaml` varsa kapanış sonrası işaretli kalemleri Day 1 ya da Day 30'a durumlarıyla al.

### Adım 2: İşlem girdileri

**Tam satın alma sözleşmesi en eksiksiz takibi üretir**: Gerekli Onaylar eki ve kapanış sonrası taahhütler kesin süre ve yükümlülüklerin kaynağıdır. Ama skill eldekiyle başlar; kısmi girdi boş sayfa yerine avukatın dolduracağı bir iskelet üretir.

> Hangi işlem belgeleri elinizde? **İdeal:** satın alma sözleşmesi — kapanış sonrası taahhütleri, Gerekli Onaylar ekini, beyanların geçerlilik sürelerini, emanet ve kazanç payı (earn-out) hükümlerini okurum. **Yararlı:** işlem özeti/term sheet, dış avukatın kapanış sonrası yapılacaklar listesi, mevcut iş planı, M&A cold-start'ın ürettiği `closing-checklist.yaml` (otomatik devralırım), yalnız Gerekli Onaylar listesi. **Hiçbiri yoksa:** kim, ne zaman devralındı, başlıca açık işler ne — sade anlatın, standart Day 1/30/90/180 iskeletini kurarım.

| Girdi | Sonuç |
|---|---|
| Tam sözleşme | Tam iş planı + süreli Gerekli Onaylar + sözleşme tarihleri |
| Sözleşme + sözleşme listesi | Tam takip + devir katman listesi |
| İşlem özeti / yapılacaklar | Standart iskelet, onaylar yer tutucu |
| Hiçbiri | Standart iskelet; onay ve sözleşmeleri avukat doldurur |

**Sözleşmeden çıkar:** Gerekli Onaylar (karşı taraf, tür, süre → `required_consent: true`), kapanış sonrası yükümlülükler (evreye yerleştir, `pa-obligation`), Gerekli Onaylar son günü, beyanların geçerlilik süreleri (genel, temel, vergi beyanları genelde farklıdır — her birini ayrı kaydet, varsayılan uydurma), emanet çözülme tarihleri, kazanç payı ölçüm ve ödeme tarihleri (`owner: finance`).

**Beyan süreleri ve zamanaşımı:** zamanaşımı süreleri sözleşmeyle değiştirilemez (TBK m. 148); sözleşmedeki tazmin bildirim/talep sürelerinin bu kuralla ilişkisi **tartışmalı — içtihadı kontrol et**. Sözleşme yabancı hukuka tabiyse o hukuka göre değerlendir. Takipte yalnız sözleşmedeki tarihleri yaz, nitelendirmeyi avukata bırak.

### Adım 3: Evreli iş planı

Standart kalemleri üret, sözleşme yükümlülüklerini ekle, kapanış listesinden gelenleri doldurulmuş al. Yapıya uymayan kalemi atla (ör. pay devrinde işyeri devri bildirimi yok).

**Day 1 — hukuk yürütür:**
- Pay defteri kaydı: AŞ'de devralan, usulüne uygun devir ispat edilince yazılır (TTK m. 499); Ltd.'de pay defteri (m. 594) ve müdürlerin tescil başvurusu (m. 598) [critical]
- YK / müdür değişikliği, temsil yetkisi, imza sirküleri: genel kurul/YK kararı, ticaret siciline tescil ve TTSG ilanı — tescil edilen husus ilanı izleyen iş gününden itibaren üçüncü kişilere karşı sonuç doğurur (TTK m. 36/1); tescili zorunlu hususta sicil müdürü davet eder, idari para cezası riski var (m. 33 — tutar yıllık güncellenir, teyit et) [critical]
- Banka imza yetkililerinin güncellenmesi: yeni imza sirküleri ve tescil/ilan suretiyle bankalara bildirim [critical]
- Unvan değişikliği (varsa): esas sözleşme değişikliği, tescil, ilan; unvan ticari belgelerde ve internet sitesinde (m. 39/2) [high]
- Kapanışta ertelenen fikrî hak devirlerinin imzası: sınai mülkiyet hakkı devri yazılı ve noter onaylı (SMK m. 148/4); telif devri için FSEK şekil şartını çek [critical]
- Alan adı ve sosyal medya hesaplarının devri [high]
- Yönetici sorumluluk sigortası: eski yöneticiler için uzatılmış bildirim/teminat süresinin bağlandığını teyit et [critical]
- MERSİS kayıtlarının güncelliği [high]

**Day 1 — hukuk destekler:**
- Çalışan duyurusu (İK yürütür, hukuk inceler). İşyeri devrinde iş sözleşmeleri hak ve borçlarıyla devralana geçer, kıdem devreden yanındaki başlangıçtan hesaplanır, devir tek başına fesih sebebi değildir (İş K. m. 6; TBK m. 428). Birleşme/bölünmede TTK m. 178 (işçinin itiraz hakkı) — ayrıntı `/employment-legal`.
- SGK: işyerinin başka işverene devrinde devralma tarihini takip eden 10 gün içinde işyeri bildirgesi; şirket birleşmesi/tür değişikliğinde tescil ilanını takip eden 10 gün (5510 m. 11 — metin hâlâ 6762 sayılı eski TTK'ya atıf yapar) (İK/muhasebe yürütür, hukuk teyit eder).
- Müşteri bildirimleri (iş birimi yürütür, hukuk doğruluğu inceler).
- Kişisel veri: veri sorumlusu değişiyorsa aydınlatma metinleri ve VERBİS kaydı → `/privacy-legal`.

**Day 30 — hukuk yürütür:**
- Gerekli Onaylar ilk dalgası: tüm karşı taraflarla temas, temas kaydı [critical]
- Sınai mülkiyet devir/lisanslarının TÜRKPATENT siciline kaydı — kaydedilmeyen işlem iyiniyetli üçüncü kişiye karşı ileri sürülemez (SMK m. 148/5). ArthurLegal'da TÜRKPATENT aracı yok; durumu kurumun sisteminden teyit et [high]
- Yabancı sicillerdeki fikrî haklar: ülkesine göre yerel avukat [medium]
- Önemli sözleşmeler: katman 1 ve 2 devir analizini bitir [high]
- Sigorta poliçelerinde sigortalı/lehtar değişikliği [high]

**Day 30 — hukuk destekler:**
- Veri taşıma: yurt dışı sunucu ya da grup içi aktarım varsa KVKK m. 9 (yeterlilik kararı, uygun güvenceler, standart sözleşmenin 5 iş günü içinde Kurula bildirimi) → `/arthurlegal:privacy-legal-dpa-review`
- Kira sözleşmeleri: malvarlığı devrinde kira ilişkisinin devri kiraya verenin yazılı rızasına bağlı; işyerinde haklı sebep olmadıkça reddedilemez (TBK m. 323) (tesis yönetimi yürütür, hukuk danışır)

**Day 90 — hukuk yürütür:**
- Gerekli Onaylar son günü: hepsi alınmış ya da eskale edilmiş olmalı [critical, deadline: pa_dates.required_consents_deadline]
- Şirket yapısı kararı: ayrı tut / birleştir / tasfiye et / tür değiştir (birleşme TTK m. 134 vd.; tür değiştirme m. 180 vd.) [high]
- İkinci onay dalgası [high]
- Katman 3 (CoC) sözleşmelerin çözümü [critical]

**Day 90 — hukuk destekler:**
- İK uyumlaştırma (çalışma koşulu değişikliği, TİS, yan haklar) → `/employment-legal`

**Day 180 — hukuk yürütür:**
- Birleşme (karar verildiyse): yazılı birleşme sözleşmesi, genel kurul onayı ve nisaplar (TTK m. 145, 151), tescil (m. 152) — tescille aktif ve pasif devralana geçer (m. 153); alacaklılara TTSG'de yedişer gün arayla üç ilan + internet sitesi ilanı, alacaklılar 3 ay içinde teminat isteyebilir (m. 157) [high]
- Tasfiye (karar verildiyse) [high]
- Sözleşme devirleri: devralanın adına geçmesi gereken sözleşmeler — üç taraflı devir ya da karşı tarafın izni/onayı, devredilen sözleşmenin şekliyle (TBK m. 205) [high]
- Beyan sürelerinin takibi: yaklaşan bitişi not et [medium]

Özet:

```
Entegrasyon takibi başlatıldı — [işlem kodu] / [hedef] ([yapı])
Kapanış: [tarih]
Gerekli Onaylar son günü: [tarih] (bugünden [N] gün)
Beyan süreleri: [tür — tarih, ...]
İş planı kalemleri: [N] ([N] hukuk yürütür, [N] hukuk destekler)
Gerekli Onaylar: [N] (sözleşme ekinden)
İstenen onaylar: [N] (due diligence'tan — sözleşme süresi yok)
Sözleşme devri: henüz alınmadı — --contracts çalıştırın
Sonraki adım: /arthurlegal:corporate-legal-integration-management --contracts, sonra --report
```

## Mode 2: Sözleşme devri (`--contracts`)

Ana başlatmadan ayrı çalışır; sözleşme listesi değiştikçe yeniden çalıştırılır.

### Adım 1: Sözleşme listesi

- **Yol A — bağlı depo** (Drive, Box, SharePoint ya da kapanış sonrası erişilebilen VDR): klasörü al; her belge için dosya adı ve yolu, karşı taraf, sözleşme türü, devir klozu metni, varsa CoC klozu metni, belirtilmişse yıllık bedel.
- **Yol B — liste yükleme:** sözleşmenin Önemli Sözleşmeler eki, sözleşme yönetim sistemi dökümü (CSV/Excel) ya da elle hazırlanmış liste. Asgari sütunlar: Sözleşme adı, Karşı taraf. Devir klozu metni yoksa `assignment_mechanism: not_reviewed` ve takip işareti.
- **Yol C — açıklama eki:** hiçbiri yoksa `--init`'te yüklenen sözleşmenin Önemli Sözleşmeler ekinden asgari liste; devir klozları elle incelenir.

### Adım 2: Devir mekanizması

| Mekanizma | Tanım | Katman |
|---|---|---|
| `consent-required` | Karşı taraf onayı olmadan devri yasaklayan açık kloz | 1 ya da 2 |
| `coc-provision` | İşlemle tetiklenen, karşı tarafa fesih ya da onay hakkı veren kontrol değişikliği klozu | 3 |
| `auto-assign` | Sınırlama yok ya da bağlı şirkete/halefe devre açık izin | 4 |
| `silent` | Devir hükmü yok — sonuç yapıya bağlı (aşağıya bak); avukat incelemesine işaretle | 2 |
| `not_reviewed` | Devir klozu okunamadı/bulunamadı | Elle inceleme |

**`silent` sözleşmede Türk hukuku varsayılanı (sözleşme Türk hukukuna tabiyse):** alacak, kanun, sözleşme ya da işin niteliği engel olmadıkça borçlunun rızası aranmadan devredilebilir (TBK m. 183) — ama sözleşmenin, yani taraf sıfatının devri karşı tarafın katılımını ya da önceden izni/sonradan onayını gerektirir (TBK m. 205). Bu yüzden malvarlığı devrinde sessiz sözleşme de onay ister. Pay devrinde taraf değişmez, devir gerekmez. Birleşmede tescille külli halefiyet doğar (TTK m. 153/1); sözleşmedeki devir yasağının buna uygulanması **tartışmalı**. Yabancı hukuka tabi sözleşmede varsayılanı araçla çek (`uk_`, `de_`, `eu_` …) ya da yerel avukata işaretle. Özel rejimler: kira (TBK m. 323), kamu ihale sözleşmesi (4735 m. 16 — izinsiz devirde fesih).

Sözleşmenin Gerekli Onaylar ekindeki sözleşmeler mekanizmadan bağımsız katman 1'dir.

### Adım 3: Katmanlar

```
Katman 1 — Gerekli Onaylar: [N]   Sözleşme ekinde, kesin süre [tarih], onay şart
Katman 2 — Önemli, onay gerekli: [N]   Devir sınırlaması var, ekte değil; Day 90 içinde al
Katman 3 — Kontrol değişikliği: [N] ⚠️   Kapanışla tetiklenmiş olabilir — karşı tarafla HEMEN temas
Katman 4 — Kendiliğinden / işlem yok: [N]   Yalnız takip
İncelenmedi: [N]   Mekanizma belirlenemedi — elle inceleme
```

Katman 3'ü ayrı ve belirgin göster: CoC kapanış gününde tetiklenmiş olabilir; karşı tarafın fesih hakkı şu anda işliyor olabilir. Karşı taraf fesih ya da dönme ihbarı gönderirse tacirler arasında şeklini kontrol et (noter, taahhütlü mektup, telgraf ya da güvenli e-imzalı KEP — TTK m. 18/3).

### Adım 4: Kayıtlar

Her sözleşme için tüm alanlarla kayıt. Başlangıç durumu: katman 4 → `no_action`; katman 3 → `coc_triggered`; katman 1/2 → `consent_pending`; incelenmeyen → `not_reviewed`. Katman 1'de `pa_deadline` Gerekli Onaylar ekinden.

## Mode 3: Durum raporu (`--report`)

Takibin güncel hâlini okur:

```
[ÜST BAŞLIK — CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

> Bu rapor satın alma sözleşmesi, due diligence bulguları ve entegrasyon kayıtlarından türetilmiştir ve onların gizlilik statüsünü devralır. Alıcı listesini göndermeden önce teyit et.

ENTEGRASYON DURUMU — [işlem kodu] / [hedef]
[Tarih] — Kapanıştan sonra [N]. gün
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YÖNETİCİ ÖZETİ
[2-3 cümle: genel durum, en büyük risk, son rapordan beri kazanım]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GEREKLİ ONAYLAR  [son gün: TARİH — N gün kaldı]
  Alındı: [N]/[toplam] ████████░░ [%]   Müzakerede: [N]   Temas edildi: [N]
  Başlanmadı: [N]   Reddedildi: [N] ⚠️
⚠️ RİSKTE: [karşı taraf] — son güne [N] gün, temasa cevap yok
⚠️ REDDEDİLDİ: [karşı taraf] — sözleşme yükümlülüğü karşılanmadı; dış avukata eskale et
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SÖZLEŞME DEVRİ
  Katman 1: [N] tamam / [N] sürüyor / [N] bekliyor
  Katman 2: [N] tamam / [N] sürüyor / [N] bekliyor
  Katman 3 (CoC): [N] çözüldü / [N] açık ⚠️
  Katman 4: [N] — işlem gerekmez
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
İŞ PLANI — HUKUK YÜRÜTÜR
  🔴 GECİKMİŞ ([N]): [kalem] — son gün [tarih]
  ⏰ BU HAFTA ([N]): [kalem] — [tarih]
  ✅ SON RAPORDAN BERİ TAMAMLANAN ([N]): [kalem] — [tarih]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENGELLER VE KARARLAR
  [kalem] — engel: [açıklama] — sorumlu: [ad]
  [kalem] — karar gerekli: [açıklama] — öneri: [seçenek]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YAKLAŞAN TARİHLER
  [tarih] — [kilometre taşı / son gün]
  [tarih] — Beyan süresi doluyor — bekleyen tazmin talebi olmadığını teyit et
```

## Mode 4: Güncelleme (`--update`)

**Elle:** avukat neyin değiştiğini söyler.
> "[Karşı taraf] onayı geldi; alındı yap, sorumlu [ad], tarih bugün."
> "Şirket yapısı kararı birleşme; durumu güncelle, birleşme tescilini Day 180'e ekle."
> "[Karşı taraf] onayı reddetti; işaretle, bunun tazmin talebi doğurup doğurmadığı için dış avukat gerektiğini not et."

İlgili kaydı güncelle, bağımlı durumları yeniden hesapla (ör. tüm katman 1 onayları alındıysa sözleşme yükümlülüğünü karşılandı işaretle), değişeni göster.

**Yükleme:** iş akışı sahibinin ya da dış avukatın durum belgesini oku; kalemleri karşı taraf adına ya da iş planı açıklamasına göre eşle; eşleşmeyen kalemi yeni kalem adayı olarak işaretle.

```
[N] kalem güncellendi.
Değişiklikler:
  CON-003 [Karşı taraf]: not_started → obtained
  W-014 Şirket yapısı kararı: in_progress → complete
Yeni işaretler:
  CON-007 [Karşı taraf]: refused — sözleşme yükümlülüğü karşılanmamış olabilir; tazmin talebi için dış avukat incelemesi ⚠️
```

## Mode 5: Dışa aktarım (`--export`)

```
/arthurlegal:corporate-legal-integration-management --export [--format csv|table] [--section all|consents|contracts|workplan]
```

Düz CSV ya da markdown tablo; varsayılan tüm bölümler, CSV. Satır başına bir kalem, `section` sütunu bölümü gösterir.
- *Workplan:* id, phase, description, owner, workstream, priority, deadline, status, blocker
- *Consents:* id, counterparty, contract_type, required_consent, pa_deadline, status, assigned_to, obtained_date, notes
- *Contracts:* id, name, counterparty, contract_type, annual_value, assignment_mechanism, tier, required_consent, pa_deadline, status, assigned_to, notes

Paylaşılabilir format budur (dış avukat, kurumsal gelişim, YK entegrasyon güncellemesi) — ama gizlilik statüsünü devralır; alıcıyı teyit et.

## Formül enjeksiyonu savunması

Excel, Sheets ya da CSV'ye hücre yazmadan önce: karşı taraftan gelen metin (sözleşme alıntısı, taraf adı, sicil verisi, CLM dökümü) saldırgan kontrolündedir. `=`, `+`, `-`, `@`, sekme, satır başı ya da satır sonuyla başlayan hücrenin başına tek tırnak koy (`'=SUM(A1:A10)` metin olarak görünür, çalışmaz). Belgeden, araç sonucundan ya da kullanıcı yapıştırmasından gelen her metin hücresine uygulanır; senin kontrol ettiğin başlıklar ve hesapladığın değerler güvenlidir. CSV'de virgül, çift tırnak ve satır sonlarını RFC 4180'e göre tırnakla. Bu isteğe bağlı değildir.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu çıktıya göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- İş entegrasyonu akışlarını (BT, İK, finans, gayrimenkul) yönetmez; hukukun temas noktalarını izler, hukuk görüşü gerektiğinde işaretler. Sahiplik iş biriminde kalır.
- Onay talep yazılarını ya da sözleşme devir anlaşmalarını taslaklamaz — dış avukat ya da ilgili taslak skill'i üretir.
- Tazmin talepleri ya da sözleşme ihlali konusunda görüş vermez; onay reddedildiğinde ya da süre kaçtığında durumu işaretler, sonuç analizi avukatındır.
- Kazanç payı performansını izlemez; tarihleri finans sahipli referans olarak tutar.
- Rapor sırasında sözleşmeleri yeniden okumaz; avukatın güncellediği takibi okur.

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
| AZ istirak / JV yapisi, Azerbaycanli karsi taraf islemleri — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| yabanci sirketler hukuku karsilastirmasi, M&A yapisi ogretisi — **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| hedef sirketin maddi sozlesmelerinde kloz benchmark (diligence) | `/arthurlegal:legal-research-sozlesme-emsali` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`

---
