---
name: ip-legal-portfolio
description: >
  Fikrî mülkiyet portföyünü izler — tescil ve başvurular, marka ve tasarım
  yenilemeleri (SMK m. 23, m. 69), patent/faydalı model yıllık ücretleri
  (m. 101), kullanım denetimi (m. 9). Neyin yenileneceğine bakarken, varlık
  eklerken veya güncellerken, ödenen ücreti/yapılan yenilemeyi kaydederken ya
  da kaydı boşluk, sona erme ve kullanım soruları için denetlerken kullan.
  Başvuru ve clearance işlerinden devir alır.
argument-hint: "[--report [--days N] | --add | --update | --audit]"
---

# /portfolio — Portföy Kaydı

Yaklaşan süreleri gösterir, varlık ekler, yapılan işlemleri kaydeder, kaydı denetler.

## Talimat

1. Aşağıdaki akışı izle ve `~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml` oku.
2. **Argümansız:** `--report` ile aynı — önümüzdeki 90 günün süreleri, aciliyete göre (🔴 sona ermiş/ek sürede, ⏰ pencerede, 🟡 yaklaşan, 🌐 vekil yönetiminde, ❓ bilinmeyen).
3. **`--report [--days N]`:** Mod 2. Pencere `--days` ile (30 / 60 / 90 / 180). Üst başlığı `## Outputs`'tan koy; her raporu doğrulama satırıyla kapat.
4. **`--add`:** Mod 3. Yeni varlığı soru-cevapla ekle; yerleşik olmayan ülke için `custom_rules` yakala.
5. **`--update`:** Mod 4. Yapılan yenileme/ücret ödemesini kaydet, IPMS ile eşitle ya da durum değiştir. `filed` yazmadan önce sonuç doğuran işlem kapısını uygula.
6. **`--audit`:** Mod 5. Süre hijyeni, tescil boşlukları, kullanım denetimi (m. 9), sahiplik tutarlılığı, sona erme ufku, izlenmeyen markalar.
7. **Kayıt boşsa ve IPMS bağlıysa** Mod 1'i öner: portföyü kayıt sisteminden çek, kaydı başlat.
8. **Korkuluk:** hesaplanan süreler yalnız referanstır. Her çıktı TÜRKPATENT sicilinden ya da ilgili ofisten teyit satırıyla biter. Yanlış girilmiş süre, girilmemiş süreden kötüdür: sahte güven yaratır. IPMS eşitlenmiş değilse kullanıcının bu kaydı "kayıt sistemi" gibi kullanmasına izin verme.

## Örnekler

```
/arthurlegal:ip-legal-portfolio
/arthurlegal:ip-legal-portfolio --report --days 180
/arthurlegal:ip-legal-portfolio --add
/arthurlegal:ip-legal-portfolio --update
/arthurlegal:ip-legal-portfolio --audit
```

## Bağlantıyla daha iyi çalışır

- **IP yönetim sistemi (IPMS) MCP ile** — Anaqua, Clarivate IPfolio, AppColl, Patrix, Alt Legal, FoundationIP. Tam dosya listesi, ücret takvimleri ve gelen yazışmalar tek yerde olur. Bağlayıcı için IPMS sağlayıcınıza sorun ya da depo kökündeki `CONNECTORS.md`'ye bakın.
- **TÜRKPATENT doğrudan:** ArthurLegal MCP'de TÜRKPATENT aracı **yoktur** (resmî uç çalışmıyor). Durum ve tarihleri TÜRKPATENT web sitesindeki sicil/araştırma ekranlarından ve EPATS'tan elle teyit edin; pratik için `${CLAUDE_PLUGIN_ROOT}/references/turkpatent-rehberi.md`.

İkisi de yoksa dosya listenizi yapıştırın ya da tablo yükleyin; oradan izlerim.

## Amaç

Süresinde yenilenmeyen marka ve tasarımın hakkı sona erer (SMK m. 28/1-a, m. 69/6). Yıllık ücreti ödenmeyen patent vade tarihi itibarıyla sona erer (m. 101/4, m. 140/1-c). Süresi geçen alan adı dakikalar içinde kapılabilir. Hepsi önlenebilir; tek şartı doğru sürenin, doğru numaraya ve doğru ülkeye bağlı olarak birinin takviminde olmasıdır. Bu skill o takvimi tutar.

## Önemli: süre referansı uyarısı

> Bu skill'in uyguladığı kurallar her çalıştırmada `tr_mevzuat_madde_getir` ile çekilen SMK metnine dayanır; yabancı ülke kuralları ancak araçla çekilip `custom_rules`'a kaynağıyla yazıldığında hesaplanır. Ofis uygulamaları, ek süreler ve **ücret tutarları değişir — güncel ücret tarifesini teyit et** (TÜRKPATENT ücret tarifesi dönemsel güncellenir). **İşlem yapmadan önce her hesaplanan süreyi TÜRKPATENT sicilinden, WIPO Madrid Monitor'den, EUIPO'dan ya da ilgili ulusal ofisten elle teyit edin** (ArthurLegal'da bu siciller için araç yok). Anaqua, CPA Global, Clarivate, Alt Legal gibi bir IPMS kullanıyorsanız varlıklarınız için onun takvimi esastır; bu kayıt onu düzenler, yerine geçmez.
>
> "Yakında süre yok" çıktıları ikinci bir bakışı özellikle hak eder.

## Ülke ve tür kuralları (çekilen maddelerden)

**Türkiye — marka (m. 23, m. 9):**
- Koruma süresi **başvuru tarihinden** itibaren 10 yıl; onar yıllık dönemlerle yenilenir (m. 23/1). (Başlangıç tescil tarihi değil, başvuru tarihidir.)
- Yenileme talebi ve ücretin ödendiği bilgisi, koruma süresinin bittiği tarihten önceki **altı ay** içinde; yapılmazsa bitişten itibaren **altı ay** içinde **ek ücretle** (m. 23/2). Kısmi yenileme mümkün (m. 23/3); yenileme önceki sürenin bittiği günü izleyen günden hüküm doğurur (m. 23/5).
- Yenilemede eksik ödenen ücret için Kurum ayrıca bildirim yapmaz — m. 161/3'teki eksik ücret bildirimi m. 23 ve m. 69'u kapsam dışı bırakır. Tutarı ödemeden önce teyit et.
- Beyan/kullanım belgesi sunma takvimi yoktur; ama tescilden itibaren beş yıl içinde Türkiye'de ciddi kullanılmayan ya da kullanımına beş yıl ara verilen marka talep üzerine iptal edilebilir (m. 9/1, m. 26/1-a); kullanım iptal talebinden önce başlarsa talep reddedilir, ancak talepten önceki üç aydaki "talep düşünülerek" yapılmış kullanım sayılmaz (m. 26/4). Kullanım; ayırt edici karakteri değiştirmeyen farklı unsurlarla, yalnız ihracat amacıyla ya da izinli kullanımı da kapsar (m. 9/2-3). Bu yüzden 5. yıl bir **kullanım denetimi** kilometre taşıdır, dosyalama süresi değil.
- Yenilenmeyen markada: süresi bittikten sonraki iki yıl içinde başkasının aynı/benzer başvurusuna, o sürede kullanılmışsa itiraz edilebilir (m. 6/8).

**Türkiye — Madrid uluslararası tescili (m. 14):** Türkiye'yi belirleyen uluslararası başvuru, Kuruma doğrudan yapılmış başvuruyla aynı sonucu doğurur (m. 14/1). Uluslararası tescilin yenilenmesi WIPO'da yürür; ArthurLegal'da Madrid/WIPO kaynağı yok → `agent_managed: true`, WIPO Madrid Monitor'den elle teyit.

**Türkiye — tasarım (m. 69):** tescilli tasarım başvuru tarihinden itibaren 5 yıl; beşer yıllık dönemlerle toplam **25 yıla** kadar (m. 69/1). Yenileme pencereleri markayla aynı: bitişten önceki altı ay, sonra ek ücretle altı ay (m. 69/4). Yenilenmeyen tasarım hakkı süre bitiminde sona erer (m. 69/6). Tescilsiz tasarım: ilk kamuya sunmadan itibaren **3 yıl**; yalnız bitiş tarihi izlenir (m. 69/2).

**Türkiye — patent ve faydalı model (m. 101):**
- Süre başvuru tarihinden patentte **20**, faydalı modelde **10** yıl; uzatılamaz (m. 101/1). Patent hükümleri, çelişmedikçe faydalı modele uygulanır (m. 145/1).
- **Yıllık ücret:** başvuru tarihinden itibaren ikinci yılın sona erdiği tarihte ve sonra her yıl vadesinde; vade, başvuru tarihine tekabül eden ay ve gündür (m. 101/2).
- Vadede ödenmezse **ek ücretle altı ay** (m. 101/3). O da geçerse hak **vade tarihi itibarıyla** sona erer ve bildirim yapılır; bildirimden itibaren **iki ay** içinde telafi ücretiyle yeniden geçerlilik kazanır (m. 101/4). Bu telafi süresi için "işlemlerin devam ettirilmesi" talep edilemez (m. 107/4). Yeniden geçerlilikte üçüncü kişilerin kazanılmış hakları saklıdır (m. 101/5).
- Diğer kaçırılmış süreler için hakların yeniden tesisi: süreye uyulamama nedeninin kalkmasından itibaren iki ay, en geç sürenin bitiminden bir yıl, özen gösterilmiş olması şartıyla (m. 107/2).

**Yabancı ofisler — kuralı ezberden hesaplama.** Araçla çek, `custom_rules`'a `source` alanıyla yaz:
- AB markası ve topluluk tasarımı: `eu_get_document_text(celex="32017R1001")` (AB Marka Tüzüğü), `eu_get_document_text(celex="32002R0006")` + değişiklik `32024R2822` (topluluk tasarımları).
- Birleşik Krallık marka yenilemesi: `uk_get_section(year="1994", number="26", section="43")`.
- Almanya marka süresi ve yenileme: `de_norm_getir(kanun="MarkenG", norm="47")`.
- Diğer ülkeler (ABD dahil), EPO yıllık ücretleri, WIPO: "ArthurLegal'da kaynak yok" → `agent_managed: true`, yerel vekile teyit.

**Alan adları:** kayıt kuruluşunun bitiş tarihini kaydet; ek süre ve geri alma kuralları kayıt kuruluşuna göre değişir — kayıt kuruluşundan teyit et (ArthurLegal'da araç yok).

**Telif:** yenileme takvimi tutulmaz. Süre ya da kayıt sorusu varsa `tr_mevzuat_madde_getir(number="5846", ...)` ya da `/arthurlegal:ip-legal-takedown`.

## Kayıt

`~/.claude/plugins/config/claude-for-legal/ip-legal/portfolio.yaml`:

```yaml
# IP Portfolio Register
# Generated: [date]
# Last updated: [date]
# Disclaimer: hesaplanan süreler yalnız referanstır — işlem öncesi TÜRKPATENT sicili /
# WIPO / ilgili ofis ya da IPMS kayıt sisteminden teyit edin. Ücret tutarlarını teyit edin.

metadata:
  company: "[Müvekkil]"
  generated: "[date]"
  last_updated: "[date]"
  last_audit: "[date or null]"
  source_system: "[Anaqua / CPA Global / manual / none]"

custom_rules:   # yerleşik olmayan ülkeler — her kural araçla çekilen kaynağıyla
  []            # ör. {jurisdiction: "UK", type: "trademark", rule: "...", source: "TMA 1994 s.43 — uk_get_section — GG.AA.YYYY"}

assets:
  - id: "TM-TR-001"
    type: "trademark"                          # trademark / patent / utility_model / copyright / design / domain
    jurisdiction: "TR"
    mark_or_title: "[Marka ya da başlık]"
    owner: "[Sicildeki sahip — tescilli unvan]"
    status: "registered"                       # pending / registered / lapsed / abandoned / cancelled
    application_number: "[no veya null]"
    registration_number: "[no veya null]"
    classes: ["9", "42"]                       # TM için Nis; patent için IPC/CPC; diğerlerinde null
    filing_date: "[YYYY-MM-DD]"                # TR markada koruma süresi buradan işler (m. 23/1)
    registration_date: "[YYYY-MM-DD or null]"  # kullanım denetimi (m. 9/1) buradan işler
    priority_date: "[YYYY-MM-DD or null]"
    grant_date: "[YYYY-MM-DD or null]"         # patent
    next_deadlines:                            # hesaplanır; --report ve --audit'te tazelenir
      - type: "Yenileme"
        due_date: "[filing_date + 10 yıl]"
        grace_end: "[due_date + 6 ay — ek ücretli]"
        basis: "SMK m. 23/1-2 — pencere due_date'ten 6 ay önce açılır"
        action: "Yenileme talebi + ücret ödeme bilgisi (tutarı teyit et)"
        status: "upcoming"                     # upcoming / due_soon / overdue / grace / lapsed / filed
    use_in_commerce: true                      # yalnız TM — m. 9 kullanım denetimini besler
    agent_managed: false                       # yabancı vekil / dış büro yönetiyorsa true
    local_agent: null
    docket_id: "[IPMS kimliği veya null]"
    outside_counsel: "[büro veya null]"
    business_owner: "[e-posta ya da ekip]"
    notes: ""

  - id: "PAT-TR-001"
    type: "patent"
    jurisdiction: "TR"
    mark_or_title: "[Buluş başlığı]"
    owner: "[Sahip]"
    status: "granted"
    application_number: "[no]"
    registration_number: "[patent no]"
    filing_date: "[YYYY-MM-DD]"
    grant_date: "[YYYY-MM-DD]"
    priority_date: "[YYYY-MM-DD or null]"
    expiration_date: "[filing_date + 20 yıl; faydalı modelde + 10]"   # m. 101/1
    next_deadlines:
      - type: "Yıllık ücret — [N]. yıl"
        due_date: "[başvuru tarihine tekabül eden ay/gün]"
        grace_end: "[due_date + 6 ay — ek ücretli]"
        restoration_end: "[sona erme bildirimi + 2 ay — telafi ücreti; bildirim gelmeden null]"
        basis: "SMK m. 101/2-4"
        action: "Yıllık ücreti öde (tutarı teyit et)"
        status: "upcoming"
    claims_count: 20
    entity_size: null                          # TR'de kullanılmaz; yabancı ofis indirimi varsa doldur
    docket_id: null
    outside_counsel: null
    business_owner: null
    notes: ""
```

`next_deadlines` durumları:
- `upcoming` — 90 günden uzak
- `due_soon` — 90 gün içinde, yapılmadı
- `overdue` — asıl tarih geçti, ek süre içinde (varsa)
- `grace` — ek süre penceresinde (açık bayrak — **ek ücret** doğar: m. 23/2, m. 69/4, m. 101/3)
- `lapsed` — ek süre işlemsiz geçti; hak sona ermiş sayılır. Patentte `restoration_end` doluysa telafi penceresi açıktır (m. 101/4) — en yüksek aciliyet
- `filed` — bu dönemin işlemi yapıldı

## Mod 1: Başlatma

Kayıt yoksa ya da `--rebuild` ile.

**Adım 1 — Kaynak.** Ayarı oku: IPMS bağlıysa portföyü oradan çek (esas kaynak odur; bu kayıt yansıtır, onun bilmediği süre eklemez). IPMS yok ama dışa aktarım varsa iste; tescil/veriliş tarihi eksik varlığı `unknown` işaretle. Hiçbiri yoksa varlıkları tek tek sor.

**Adım 2 — Süreleri hesapla.** Önce `tr_mevzuat_madde_getir(number="6769", madde_no=["9","23","26","69","101","107","145","161"])` ile kuralları çek; değişiklik dipnotu varsa uygula. Her varlık için en yakın iki üç süreyi `next_deadlines`'a yaz; on yıllık yenilemeler gibi uzak süreleri raporda istendiğinde hesapla. Kuralı bilinmeyen ülke → `custom_rules` taslağı + `agent_managed: true` + yabancı vekile teyit TODO. Gerekli tarih eksik → `next_deadlines` boş, `notes`'a neden, özet listesinde `unknown`.

**Adım 3 — Yaz ve özetle:**

```
Portföy kaydı başlatıldı.
Varlıklar: [N] — Marka [N] ([N] tescilli / [N] başvuru) · Patent/FM [N] · Tasarım [N] · Telif [N] · Alan adı [N]
Hesaplanan süre: [N]
Vekil yönetiminde / ülke kuralı teyitsiz: [N] — yabancı vekillere teyit ettirin
Bilinmeyen (tarih eksik): [N] — raporlara güvenmeden önce tamamlayın
Ne zaman ne var: /arthurlegal:ip-legal-portfolio --report
```

## Mod 2: Rapor

`/arthurlegal:ip-legal-portfolio --report [--days 30|60|90|180]` — varsayılan 90 gün. Raporlamadan önce her varlığın süresini yeniden hesapla; kayıtlı tarihe tek başına güvenme. Üst başlık `## Outputs`'tan.

```
FİKRÎ MÜLKİYET PORTFÖYÜ SÜRE RAPORU — [tarih]
[Müvekkil] — pencere: önümüzdeki [N] gün

🔴 SONA ERMİŞ / EK SÜREDE ([N])
  [ID] / [Ülke] / [Tür] / [Marka ya da başlık]
    [İşlem] — asıl tarih [tarih], ek süre sonu [tarih] [patentte: telafi sonu [tarih]]
    Durum: [grace / lapsed]

⏰ [N] GÜN İÇİNDE ([N])
  [ID] / [Ülke] / [Tür] / [Marka ya da başlık]
    [İşlem] — son gün [tarih]  (yenileme penceresi açılış: [tarih])
    Dayanak: [ör. "SMK m. 23/2"]
    [Vekil: büro / dosya: kimlik — varsa]

🟡 YAKLAŞAN (30 günden sonra, [N] gün içinde)
🌐 VEKİL YÖNETİMİNDE ([N]) — [ID] / [Ülke] — [vekil] yönetiyor; doğrudan teyit edin
❓ BİLİNMEYEN ([N]) — [ID] — [alan] eksik; hesaplanamıyor

ÖZET: izlenen varlık [N] · penceredeki süre [N] · son denetim [tarih]
```

Kapanış satırı: *"Portföy kaydından hesaplandı. Ödeme ya da işlemden önce her süreyi ve ücret tutarını TÜRKPATENT sicili / WIPO / ilgili ofis kaydından teyit edin."*

Rapor ~10'dan fazla varlık listeliyorsa ya da kullanıcı isterse `## Outputs → Dashboard offer for data-heavy outputs` uyarınca pano öner: duruma göre sayılar (yürürlükte / ek sürede / sona ermiş / başvuru), süre zaman çizelgesi, ülke-tür-sonraki işlem tarihine göre sıralanabilir tablo.

## Mod 3: Ekleme

Sor: (1) tür, (2) ülke, (3) marka/başlık, (4) sicildeki sahip (devir ve yenileme için önemli), (5) tarihler (başvuru, tescil, veriliş, rüçhan, bitiş), (6) numaralar, (7) sınıflar/istem sayısı, (8) IPMS dosya kimliği, (9) dış büro / yabancı vekil, (10) iş sahibi (ürün hattı, marka yöneticisi). Süreleri hesapla; ülke yerleşik değilse `custom_rules` akışı; `assets:`'e ekle.

**Özel kural yakalama:**
> [Ülke] / [tür] için yerleşik kuralım yok; ArthurLegal aracıyla çekebiliyorsam çekip kaynağıyla yazarım, çekemiyorsam sizden alırım:
> 1. Hangi bakım olayları var (N yılda yenileme, yıllık ücret, kullanım beyanı)?
> 2. Süre neyle başlar (başvuru, tescil, veriliş, ulusal aşama)?
> 3. Ek süre var mı, maliyeti?
> 4. Yöneten yabancı vekil kim?

`custom_rules`'a kaynak alanıyla kaydet; kaynağı kullanıcı beyanıysa `source: "kullanıcı beyanı — teyitsiz"` yaz.

## Mod 4: Güncelleme

### Sonuç doğuran işlem kapısı

Yenilemeyi ya da ücret ödemesini kaydetmeden önce `## Who's using this` oku. Rol **avukat değilse**:

> Bir yenilemeyi ya da yıllık ücreti "yapıldı" (`filed`) diye kaydetmenin sonucu var. Kayıt yanlışsa — süre kaçmış, ücret eksik, yanlış dönem — süre yerinden oynamaz ve hak yine sona erebilir; yenilemede eksik ücret için Kurum ayrıca bildirim de yapmaz (SMK m. 161/3). İşlemi yapan avukat, marka/patent vekili ya da yabancı vekille veya TÜRKPATENT sicilinden teyit ettiniz mi? Evetse devam ediyorum. Hayırsa:
> - Henüz `filed` kaydetmeyin.
> - Avukata götürün: varlık kimliği, ülke, süre türü, IPMS'in gösterdiği, ne zaman ne yapıldığını düşündüğünüz ve bu bilginin kaynağı.
> Avukat için bağlı olduğunuz baroya başvurabilirsiniz; Kurum nezdinde işlemleri sicile kayıtlı marka/patent vekilleri de yapar (m. 160/1).

Açık "evet" olmadan hiçbir süreyi `filed` yapma. Durum tazeleme, rapor ve yaklaşan süre gösterimi kapı gerektirmez.

**Elle güncelleme:** "TM-TR-001'in yenilemesini 4 Mart'ta yaptık." → eşleşen süre `status: filed`, `filed_date`; yaşam döngüsündeki sonrakini hesapla (yenilemede sonraki 10 yıllık bitiş; patentte sonraki yıllık ücret).
**IPMS eşitleme:** son dosya listesini çek, karşılaştır; kayıt sistemi kazanır; kaydın bilip sistemin bilmediğini göster (terk, devir kaydı ya da veri hatası olabilir).
**Durum değişikliği:** "TM-TR-004 terk edildi." → `status` güncelle, `next_deadlines` temizle, tarihi not et. Devirde: devir sözleşmesi yazılı ve noter onaylı olmalı; sicile kaydedilmeyen işlem iyiniyetli üçüncü kişilere karşı ileri sürülemez (m. 148/4-5) — sicil kaydını sor.

## Mod 5: Denetim

**Süre hijyeni** — şu an `grace`'te olanlar (ek ücret işliyor); `lapsed` olup `abandoned`/`cancelled` işaretlenmemişler (patentte telafi penceresi açık mı?); `next_deadlines` hesaplanmamış varlıklar.
**Tescil boşlukları** (pratik eşikler, hukuki süre değil) — 18 aydan uzun süredir `pending` marka başvuruları; 4 yıldan uzun süredir `pending` patent başvuruları → ofiste durum kontrolü.
**Kullanım (yalnız TM, m. 9)** — tescilinin 5. yılını geçmiş ya da yaklaşan ve `use_in_commerce: false`/belirsiz markalar → kullanım delili derlemesi; iptal riski (m. 26/1-a), itirazda (m. 19/2) ve tecavüz davasında (m. 29/2) kullanım ispatı talebine açıklık.
**Sahiplik** — aktif olmayan tüzel kişi adına kayıtlı varlıklar (devir kaydı gerekebilir); aynı kişinin farklı yazılmış unvanları.
**Sona erme ufku** — önümüzdeki 24 ayda bitecek patent/faydalı modeller ve son 5 yıllık dönemindeki tasarımlar (25 yıl sınırı: m. 69/1) — ürün planlama, lisans penceresi.
**İzlenmeyen varlıklar** — `## Brand protection` izleme listesinde olmayan tescilli markalar; listeye alıp almama avukatın kararı.

```
PORTFÖY DENETİMİ — [tarih]
SÜRE HİJYENİ: ek sürede [N] · sona ermiş (işaretsiz) [N] · hesaplanmamış [N]
TESCİL BOŞLUKLARI: TM başvuru >18 ay [liste] · patent başvuru >4 yıl [liste]
KULLANIM (TM, m. 9): 5. yıl eşiğinde belirsiz kullanım [liste]
SAHİPLİK: tanınmayan sahip [N] · unvan tutarsızlığı [liste]
SONA ERME UFKU (24 ay): [liste]
MARKA İZLEME: izlemede olmayan tescilli markalar [liste]
ÖNERİLEN EYLEMLER: 1. [en yüksek öncelik] 2. [...]
```

## Entegrasyon: ip-renewal-watcher ajanı

`ip-renewal-watcher` ajanı bu skill'i zamanlamayla (varsayılan haftalık) çalıştırır ve Mod 2 raporunu ayarda `Renewal alerts` satırındaki kanala gönderir. 🔴 kalem (ek süre / sona ermiş) varsa zamanlamayı beklemeden hemen gönderir.

## Devirler

- **Alır:** başvuru işlerinden (başvuru yapıldığında), `/arthurlegal:ip-legal-clearance`'tan (marka benimsenip başvuru sıraya girdiğinde), `/arthurlegal:ip-legal-invention-intake`'ten (başvuru yapıldığında), devir kayıtlarından.
- **Gönderir:** avukata "şimdi yenile/öde" uyarısı — bu skill işlem yapmaz; süreyi ve gerekenleri söyler.

## Bu skill ne yapmaz

- Hiçbir şey dosyalamaz, ücret ödemez; her işlemi avukat ya da vekil yapar.
- Süreleri TÜRKPATENT, WIPO ya da başka sicilden doğrulamaz; verdiğiniz tarihlerden ve çekilen maddelerden hesaplar. Kayıt çalışma kopyasıdır; sicil esastır.
- Yenileyip yenilememeye karar vermez — marka hâlâ kullanılıyor mu, patent hâlâ değerli mi, alan adı hâlâ önemli mi iş kararıdır.
- Yüzlerce varlıklı portföyde IPMS'in yerini tutmaz.
- Ofis kaydını okuyup durumu teyit etmez; burada `filed` görünen bir yenileme, biri öyle söylediği içindir — Kurumun kabul ettiğini değil. Kabulü sicilden ya da IPMS'ten teyit edin.
