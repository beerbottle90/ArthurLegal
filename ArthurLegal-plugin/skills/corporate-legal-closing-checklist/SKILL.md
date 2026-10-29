---
name: corporate-legal-closing-checklist
description: >
  Kapanışı ne engelliyor — kapanış kontrol listesini durum, kritik yol ve
  kapanışa kalan günle tutar. Kendini günceller: due diligence bulgularından ve
  ek çalışmalarından yeni kalemleri alır, durumu izler, engelleri gösterir.
  Türk hukukundaki kapanış kalemlerini (Rekabet Kurulu izni — 4054 m. 7 ve
  2010/4 sayılı Tebliğ, pay devri onayları ve şekli — TTK m. 490-494, 595,
  pay defteri ve ticaret sicili tescili) kaynaklarıyla yazar. "Kapanış kontrol
  listesi", "kapanışa ne kaldı", "liste durumu", "listeye ekle" denildiğinde
  ya da zamanlanmış durum raporunda kullan.
argument-hint: "[isteğe bağlı: kalem kimliği + durum güncellemesi]"
---

# /closing-checklist — Kapanış Kontrol Listesi

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/closing-checklist.yaml` oku; aşağıdaki modları kullan.
2. Durum güncellemesi verildiyse: Mode 3.
3. Yoksa Mode 4: engelleyici kalemler, kritik yol, kapanışa kalan gün.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

İşlem, liste bittiğinde kapanır: listedeki her şey yapılmış, hiçbir şey eksik değil. Bu skill listeyi tutar, due diligence'tan gelen kalemleri ekler ve ekibe neyin engellediğini söyler.

## Liste

`~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/closing-checklist.yaml`. Anahtarlar İngilizce kalır (integration-management ve dataroom-watcher bu dosyayı okur); kalem metinleri Türkçe.

```yaml
deal_code: "Proje Şahin"
target_close: [TARİH]
signing_date: [TARİH]
last_updated: [TARİH]

conditions_precedent:
  - id: CP-001
    item: "Rekabet Kurulu izni"
    category: "Regulatory"
    responsible: "Alıcı avukatı"
    due: 2026-04-15
    status: "Bildirim 2026-03-01; bildirimin tam sayıldığı tarih teyit edilecek"
    blocking: true
    source: "SPA m. 7.1(a); 4054 m. 7; Tebliğ 2010/4 m. 7, 10"

  - id: CP-002
    item: "[Karşı taraf] onayı — çerçeve sözleşme CoC"
    category: "Third-party consents"
    responsible: "Hedef — [ad]"
    due: 2026-04-20
    status: "Talep 2026-03-10 gönderildi, cevap yok"
    blocking: true
    source: "Ek 3.12(a)(4); [Karşı taraf] sözleşmesi m. 14.2"

closing_deliverables:
  - id: CD-001
    item: "Ticaret sicili kayıt örneği / sicil tasdiknamesi — Hedef"
    category: "Corporate"
    responsible: "Satıcı avukatı"
    due: 2026-04-28
    status: "Başlanmadı"
    blocking: true
    source: "SPA m. 2.3(b)(iv); TTK m. 35/2"

  - id: CD-002
    item: "Pay devri — AŞ: ciro + teslim / Ltd.: noter onaylı devir sözleşmesi"
    category: "Corporate"
    responsible: "Satıcı avukatı"
    due: 2026-04-30
    status: "Taslak hazır"
    blocking: true
    source: "SPA m. 2.2; TTK m. 490/2 (AŞ) ya da m. 595/1 (Ltd.)"
  # ... vb.
```

ABD'deki "good standing" belgesinin karşılığı yoktur; yerine güncel sicil kaydı/tasdiknamesi, TTSG ilanları, vergi ve SGK "borcu yoktur" yazıları ve imza sirküleri istenir — sözleşmede hangisi yazıyorsa o.

## Modlar

### Mode 1: Satın alma sözleşmesinden kur

İmzalanmış (ya da son hâline yakın) sözleşmeyi oku ve çıkar: her ön koşul (yeri sözleşmeye göre değişir — gerçek başlıkları oku), her kapanış teslimi, kapanış öncesi süreli her taahhüt. Her biri sözleşme maddesine atıflı bir kalem olur.

**Şirket onayları ve şekil — yapıya göre:**

| Yapı | Kalem | Dayanak |
|---|---|---|
| AŞ pay devri | Esas sözleşmede devir sınırlaması varsa şirketin onayı (uygulamada YK kararı); borsaya kote olmayan payda red sebepleri sınırlı; 3 ay içinde reddedilmezse onay verilmiş sayılır | TTK m. 492-494 |
| AŞ pay devri | Bedeli tamamen ödenmemiş nama yazılı paylar için şirket onayı | TTK m. 491 |
| AŞ pay devri | Nama yazılı pay senedinde ciro + zilyetliğin geçirilmesi; hamiline senette MKK bildirimi | TTK m. 490/2, 489 |
| AŞ pay devri | Pay defterine kayıt — devralan ancak usulüne uygun devir ispat edilince yazılır | TTK m. 499/2 |
| Ltd. pay devri | Yazılı devir sözleşmesi, imzalar noter onaylı; ortaklar genel kurulu onayı (sözleşmede aksi yoksa); onayla geçerlilik | TTK m. 595/1-2, 616/1-g, 620 |
| Ltd. pay devri | Pay defteri kaydı; müdürlerin ticaret siciline tescil başvurusu (30 gün içinde yapılmazsa ayrılan ortak silinmeyi isteyebilir) | TTK m. 594, 598 |
| Malvarlığı / işletme devri | Önemli miktarda şirket varlığının toptan satışı için AŞ genel kurulu; ticari işletme devri sözleşmesi yazılı, tescil ve ilan; sözleşme devirleri | TTK m. 408/2-f, 11/3; TBK m. 205 |
| Birleşme | Birleşme sözleşmesi yazılı, yönetim organlarınca imza, genel kurul onayı; nisaplar (AŞ: esas/çıkarılmış sermayenin çoğunluğunu temsil şartıyla mevcut oyların 3/4'ü; Ltd.: sermayenin en az 3/4'ünü temsil eden tüm ortakların 3/4'ü); tescil başvurusu; tescille geçerlilik | TTK m. 145, 151, 152, 153 |

Tescil edilen hususlar TTSG'de ilanı izleyen iş gününden itibaren üçüncü kişilere karşı sonuç doğurur (TTK m. 36/1) — kapanış tarihini ve "yürürlük" beyanlarını buna göre kur.

**Düzenleyici kalemlerden önce araştır.** Rekabet, sektör ve yabancı yatırım onaylarının mekaniği, eşikleri ve süreleri değişir. Koşulun adını sözleşmeden al, işleyen kuralı birincil kaynaktan çek, güncelliğini doğrula; süreyi hafızadan doldurma.
- **Rekabet:** kontrolde kalıcı değişiklik yaratan işlem birleşme/devralma sayılır (Tebliğ 2010/4 m. 5); izne tabiyet ciro eşiklerine bağlıdır (m. 7 — **güncel eşikleri Tebliğ'den teyit et**; teknoloji teşebbüsü istisnası m. 7/2). İzne tabi işlem karar verilmeden hukuken geçerlilik kazanamaz (Tebliğ m. 10/4); Kurul ön incelemeyi bildirimden itibaren 15 günde yapar, nihai incelemeye alırsa işlem askıdadır; süresinde cevap yoksa bildirimden 30 gün sonra geçerlilik kazanır (4054 m. 10). Bildirim, eksiksiz bilgiler Kurul kayıtlarına girdiğinde yapılmış sayılır (Tebliğ m. 11) — süre hesabını buna göre yap. İzinsiz kapanış: idari para cezası (4054 m. 16/1-b; alt sınır yıllık güncellenir — teyit et) ve m. 11 tedbirleri. Emsal için `tr_kurum_karari_ara(kurum="rekabet", decision_type="birlesme_devralma", query="[pazar / taraf]")` — dönen künyeyi birebir kullan.
- **Sektör:** EPDK, BDDK, SPK, BTK, sigortacılık onayları → `tr_mevzuat_ara` + `tr_kurum_karari_ara`; çekemediğinde "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".
- **Halka açık hedef:** önemli nitelikte işlem usulü ve ayrılma hakkı (6362 m. 23-24), yönetim kontrolü edinilirse pay alım teklifi (m. 26); KAP açıklama takvimi.
- **Yabancı unsur:** AB birleşme kontrolü `eu_search_eu_law(query="Council Regulation 139/2004 control of concentrations")`; diğer ülkeler için `uk_`, `de_`, `nl_`, `pl_`, `at_`, `ie_`, `fi_`, `es_`, `jp_`, `az_`; listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

**MAC / esaslı olumsuz değişiklik koşulu.** Tanımı sözleşmeden al — müzakere edilmiş bir metindir, standart değildir. Türk hukukunda kanuni MAC tanımı yoktur; aşırı ifa güçlüğü (TBK m. 138: öngörülemeyen olağanüstü durumda uyarlama, olmazsa dönme/fesih) ayrı bir kurumdur ve sözleşmedeki MAC klozuyla ilişkisi **tartışmalı — içtihadı kontrol et**. Sözleşme yabancı hukuka tabiyse o hukukun yorumunu araçla çek; bir olayı MAC tetikleyicisi diye işaretlemeden önce yap.

**Önemli sözleşmelerden onay çıkarımı** yapıya ve her sözleşmenin metnine bağlıdır: pay devrinde taraf değişmez (yalnız CoC), malvarlığı devrinde sözleşme devri karşı tarafın katılımını gerektirir (TBK m. 205), birleşmede külli halefiyet (TTK m. 153/1) ile devir yasağı ilişkisi tartışmalıdır. Varsayılan kural varsayma; sözleşme başına kuralı yaz.

### Mode 2: Due diligence'tan al ("kendini güncelleyen" kısım)

Üst skill kapanış öncesi eylem gerektiren bir bulgu ürettiğinde tetiklenir:
- **`diligence-issue-extraction` bulguları** — kapanış eylemi işaretli her bulgu (onay, genel kurul/YK kararı, düzenleyici bildirim, ibra, emanet, borç kapama). Yalnız "onay" değil — o skill'in Aktarımlar bölümüne bak.
- **`material-contract-schedule` CoC / devir kalemleri** ve onay takip tablosu.
- **`deal-team-summary` çıktısı** — üst düzey brifing, tek tek notların gözden kaçırdığı bir kapanış kalemini gösterebilir (ör. birden çok yönetici sözleşmesinden toplanan CoC ikramiye ibraları, birleşik onay paketi). Klasördeki en son brifingi oku, kapanış kalemlerini listeyle uzlaştır; listede olmayanı ekle.

Aktarım şeması (anahtarlar İngilizce kalır):

```yaml
handoff:
  # Zorunlu
  item: "[Karşı taraf ya da eylem, tek satır]"
  category: "[Third-party consents | Shareholder / board action | Regulatory filing | Release / termination | Escrow / holdback | Closing deliverable]"
  source: "[Sözleşme adı / kanun maddesi / VDR yolu]"
  blocking: true  # sözleşmede önemlilik kaydı yoksa
  severity: "[🔴 / 🟠 / 🟡 / 🟢 — üst skill'den taşınır; CLAUDE.md'deki severity floor kuralı]"

  # Karşı taraf işlemi
  counterparty: "[ör. Delta Lojistik A.Ş.]"
  guarantor: "[ör. alıcı ana şirket garantisi gerekli | Yok]"
  conditions: "[karşı tarafın koştuğu şart — ör. 'onay, alıcı ana şirketin yeni garantisiyle yürürlüğe girer']"
  notice_deadline: "[ör. kapanıştan 30 gün önce | belirli tarih]"

  # Şirket işlemi
  approval_body: "[Genel kurul | Ortaklar genel kurulu | YK | Müdürler | Düzenleyici]"
  approval_threshold: "[ör. Ltd. pay devri onayı: temsil edilen oyların salt çoğunluğu, sözleşmede aksi yoksa]"
  statutory_or_charter_source: "[ör. TTK m. 595/2, 620; Şirket sözleşmesi m. 8]"

  # Zamanlama
  estimated_time_to_complete: "[ör. 30 gün]"
  must_occur_before: "[ör. kapanış | imza | Rekabet izni]"
```

Üst skill'in doldurduğu her alanı koru. "Delta onayı gerekli; yeni garanti şartı ve 30 gün bildirim" listede üç unsuruyla görünür, "Delta CoC onayı"na indirgenmez. Ciddiyeti taşı (CLAUDE.md severity floor kuralı). Tekilleştirmeyi serbest metin adına göre değil (karşı taraf + eylem türü) çiftine göre yap — Delta onayı ile Delta ibrası ayrı kalemlerdir. Birleştirirken üzerine yazma, alanları birleştir.

### Mode 3: Durum güncellemesi

Kullanıcı (ya da dataroom-watcher ajanı) güncelleme verir; kalemi bul, `status` ve `last_updated`'i güncelle.

```
/arthurlegal:corporate-legal-closing-checklist
CP-002: [Karşı taraf] cevap verdi, onay formu ekte, karşı imza gerekiyor
```

### Mode 4: Ne engelliyor

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

> Bu rapor satın alma sözleşmesi, due diligence bulguları ve iç işlem kayıtlarından türetilmiştir ve onların gizlilik statüsünü devralır. Dağıtım listesini (karşı taraf, geniş iş ekipleri) göndermeden önce teyit et.

## Kapanış Durumu — [işlem kodu] — [tarih]

**Hedef kapanış:** [tarih] ([N] gün)
**Kalemler:** [N] toplam — [N] tamam, [N] sürüyor, [N] başlanmadı

### 🔴 Engelleyici ve riskte
| ID | Kalem | Son gün | Durum | Kalan gün |
|---|---|---|---|---|
| [CP-XXX] | [kalem] | [tarih] | [durum] | **[N]** |

### 🟡 Engelleyici, yolunda
[aynı tablo]

### ✅ Tamamlanan
[N] kalem — [kısa liste]

### Engelleyici değil (kapanış sonrası, bilgi)
[N] kalem

**Kritik yol:** [kayarsa kapanış tarihini iten kalem(ler)]
```

## Kritik yol

Her engelleyici eşit değildir: 30 günde alınan onay kritik yoldadır; 2 günde çıkan sicil kaydı değildir, ikisi de engelleyici olsa bile. Her engelleyici için tamamlanma süresini tahmin et; `(son gün − bugün) < tahmini süre` olanlar riskte, her raporun en üstünde. Noter, sicil ve TTSG ilan sürelerini ve resmî/dini tatilleri tahmine kat.

Liste yaklaşık 10 kalemi aşarsa ya da istenirse panoyu öner (`## Outputs → Dashboard offer for data-heavy outputs`): duruma göre sayılar (tamam / sürüyor / başlanmadı / riskte), iş akışına göre kritik yol, kalem-sorumlu-son gün-kalan gün tablosu.

## dataroom-watcher ajanı

Ajan listeyi günlük kontrol eder, bağlıysa e-posta/Slack'ten durum güncellemelerini çeker ve "ne engelliyor" raporunu işlem kanalına gönderir. Mode 4 ajanın çıktısıdır.

## Sonuçlu eylem kapısı (kapanışı teyit)

**"Kapanışa hazır / tüm ön koşullar sağlandı" teyidi ya da kapanış notu üretmeden önce** CLAUDE.md `## Who's using this` oku. Rol **avukat değilse**:

> Ön koşulların sağlandığını teyit etmenin hukuki sonucu var — para akışını ve kapanış sonrası yükümlülükleri bu sinyal başlatır. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet:
> - Durumuyla tam ön koşul listesi (tamam, sürüyor, başlanmadı)
> - Tamamlanma delili zayıf ya da eksik kalemler
> - Zamanında kapanmayacak kalemler için gereken feragat ya da yan mektuplar
> - Açık sorular (bekleyen onaylar, MAC / beyanların kapanışta yinelenmesi riski)
> - Avukata sorulacaklar (kapanmış sayılabilir mi; atlanmaması gereken koşul var mı; istisna ekine ne girmeli)
>
> Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan nihai "kapanışa hazır" teyidi üretme. Durum takibi ve "ne engelliyor" raporları kapı gerektirmez.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu rapora göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Onay almaz, bildirim yapmaz, belge taslaklamaz; yapılması gerektiğini izler.
- Neyin engelleyici olduğuna karar vermez — onu satın alma sözleşmesi söyler; bu skill sözleşmeyi okur.
- İşlemi kapatmaz; ne zaman kapatabileceğinizi söyler.

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
