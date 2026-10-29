---
name: corporate-legal-entity-compliance
description: >
  Şirket uyum takvimi — kurulum, yaklaşan son günler raporu, durum güncelleme, sağlık
  denetimi, CSV dışa aktarma. Şirket tablosundan compliance-tracker.yaml kurar;
  her şirket ve ülke için TTK takvimini hesaplar: olağan genel kurul (m. 409/1, 617/1),
  finansal tablolar ve faaliyet raporu (m. 514), defter açılış/kapanış onayları (m. 64/3),
  denetçi seçimi (m. 399), bağlılık raporu (m. 199), YK görev süresi (m. 362), tescil ve
  ilan, pay edinim bildirimleri (m. 198); 30/60/90 gün içinde ne var gösterir. Yabancı
  bağlı şirketler için ArthurLegal MCP araçlarına yönlendirir. Kullanıcı "şirket uyumu",
  "genel kurul takvimi", "defter onayı ne zaman", "tescil son günleri", "şirket
  takibi", "entity compliance", "good standing" dediğinde kullan.
argument-hint: "[--init | --report [--days N] | --update [--from-report] | --sweep | --audit | --export [--format csv|table]]"
---

# /entity-compliance

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## Entity Management` yükle (şirket tablosu, ülkeler, mali müşavir / yerel sicil ajanı).
2. Bayrağa göre mod: bayraksız ya da `--init` → Mod 1 · `--report` → Mod 2 · `--update` → Mod 3a, `--update --from-report` → 3b · `--sweep` → 3c · `--audit` → Mod 4 · `--export` → Mod 5.
3. `~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml` dosyasını oku/yaz.
4. Her güncellemeden sonra değişiklik özetini ve sıradaki eylemi göster.

## Amaç

Olağan genel kurul, finansal tablolar, defter onayları, denetçi seçimi, tescil ve ilan — her şirketin kendi takvimi ve kaçırmanın kendi sonucu var. Bu skill tek bir YAML takip dosyası tutar: hangi şirkette ne, ne zaman. Dosya sizindir; Claude komutla günceller, paylaşmak gerektiğinde dışa aktarırsınız.

## Önemli: son gün uyarısı

> Aşağıdaki süreler TTK'nın canlı çekilmiş metnine dayanır, ancak esas sözleşme, özel hesap dönemi, sektör mevzuatı (banka, sigorta, enerji, halka açık) ve ikincil düzenlemeler takvimi değiştirebilir. **Son günleri mali müşavirinizin takvimi, ticaret sicili müdürlüğü ve MERSİS kaydıyla teyit edin.** Vergi ve SGK beyannameleri bu takipte yoktur; mali müşavir takviminden izlenir. İdari para cezası tutarları her yıl güncellenir; tutarı takip dosyasına sabit yazma.

## Şirket türü ayrımı — takvim türe göre değişir

Takvim yalnız ülkeye değil **şirket türüne** bağlıdır; bir türün son gününü diğerine kopyalama. Şirket tablosunda tür yoksa `type_unknown` işaretle ve sor.

| Konu | AŞ | Ltd. | Halka açık AŞ |
|---|---|---|---|
| Olağan GK | Faaliyet dönemi sonundan itibaren 3 ay (m. 409/1) | Hesap dönemi sonundan itibaren 3 ay (m. 617/1) | AŞ gibi + SerPK |
| GK çağrısı | İlan (internet sitesi + TTSG) + iadeli taahhütlü; en az 2 hafta (m. 414/1) | En az 15 gün; sözleşmeyle 10 güne inebilir (m. 617/2) | İnternet sitesi + KAP; en az 3 hafta (SerPK m. 29/1) |
| Bakanlık temsilcisi | Gündeme göre zorunlu olabilir (m. 407/3; Yönetmelik m. 32) | Uygulanmaz (m. 617/3) | Elektronik GK uygulayanlarda zorunlu (Yönetmelik m. 32/1-b) |
| Yönetim organı süresi | YK üyeleri en çok 3 yıl için seçilir (m. 362/1) | Yönetim ve temsil şirket sözleşmesiyle düzenlenir (m. 623/1); süreyi sözleşmeden al | AŞ gibi + bağımsız üye kuralları (SerPK m. 17/1) |
| Pay defteri | m. 499 | m. 594 | MKK kaydı saklı (m. 499/5) |
| Bağımsız denetim | Cumhurbaşkanınca belirlenen şirketler (m. 397/4) | AŞ hükümleri uygulanır (m. 635) | SerPK m. 14/3 |
| İnternet sitesi | Yalnız denetime tabi olanlar (m. 1524/1, 1524/6) | Aynı | Aynı + KAP |

**Bağımsız denetim eşikleri** Cumhurbaşkanı kararıyla belirlenir ve değişir; eşik yazma. **Güncel eşikleri teyit et:** `tr_mevzuat_ara(query="bağımsız denetime tabi olacak şirketler", types=["CB_KARAR"])` ve dönen kararın son değişikliklerine bak.

**Yabancı şirketin Türkiye şubesi:** yerli işletme gibi tescil edilir ve Türkiye'de yerleşik tam yetkili bir ticari mümessil atanır (m. 40/4) — takipte `registered_agent` alanına mümessili yaz.

## Ülke varsayımı

Takip, her şirket için kayıtlı kuruluş ülkesine göre hesaplar. Gerçek ayak izi farklıysa (bildirilmemiş şube, tasfiye hâlindeki şirket, merkez nakli, yerel ajanın yönettiği yurt dışı şirket) çıktı aynen uygulanmayabilir.

**Yabancı bağlı şirket ve ana şirket:** kural ezberden yazılmaz; yerel ajan/hukukçu teyidi esastır. Araçla neyi arayacağın:
- Grup yapısı ve LEI: `gleif_search_entities(name="[tam unvan]", jurisdiction="DE")` → `gleif_get_group_structure(lei="[LEI]")` (konsolidasyon esaslı; sözleşmeyle kontrol görünmez).
- Birleşik Krallık: `uk_search_legislation(title="Companies Act 2006", text="confirmation statement")`.
- Almanya: `de_norm_getir(kanun="HGB", norm="325")` (yıllık hesapların açıklanması — teyit et), GmbH için `de_norm_getir(kanun="GmbHG", norm="[madde]")`.
- Hollanda: `nl_search_legislation(query="Burgerlijk Wetboek Boek 2")`. AB düzeyi: `eu_search_eu_law(query="Directive (EU) 2017/1132 company law")`.
- Azerbaycan, İrlanda, Polonya, Avusturya, İspanya, Finlandiya, Japonya: `az_`, `ie_`, `pl_`, `at_`, `es_`, `fi_`, `jp_` araçları.
- Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu ya da yerel sicil ajanı görüşü alın."
- **ABD bağlı ortaklığı (karşılaştırmalı not):** eyalet ve tür (corporation / LLC / LP) ayrımı takvimi ve vergiyi değiştirir; registered agent takvimi esastır. ArthurLegal'da ABD eyalet şirket sicili kaynağı yok.

## Takip dosyası

`~/.claude/plugins/config/claude-for-legal/corporate-legal/entities/compliance-tracker.yaml` — anahtarlar İngilizce kalır (diğer skill'ler birebir okur), değerler Türkçe olabilir:

```yaml
# Entity Compliance Tracker
# Generated: [tarih] · Last updated: [tarih]
# Disclaimer: son günler referanstır — mali müşavir, ticaret sicili ve MERSİS ile teyit edin

metadata:
  company: "[Müvekkil]"
  generated: "[tarih]"
  last_updated: "[tarih]"
  last_audit: "[tarih ya da null]"

custom_jurisdictions:   # yerleşik tabloda olmayan ülkeler — elle eklenir
  []

entities:
  - name: "[Ticaret unvanı]"
    type: "[AŞ / Ltd. / halka açık AŞ / yabancı şirket şubesi / GmbH / Ltd (UK) / diğer]"
    state_of_formation: "[ülke — sicil müdürlüğü, ör. TR — İstanbul]"
    formation_date: "[tarih ya da null]"
    status: "[active / dormant / dissolving]"
    registered_agent: "[mali müşavir / şirket içi / ticari mümessil (m. 40/4) / yerel ajan]"
    mersis_no: "[MERSİS numarası ya da null]"
    fiscal_year_end: "[MM-DD — çoğunlukla 12-31; özel hesap dönemi varsa onu yaz]"
    audit_required: "[yes / no / unknown — m. 397/4 eşiklerine göre]"
    board_term_ends: "[YK üyeleri / müdürlerin görev süresi bitişi]"
    notes: ""
    jurisdictions:
      - state: "[ülke / sicil müdürlüğü]"
        qualification: "[domestic / foreign — şube]"
        qualified_date: "[tescil tarihi ya da null]"
        agent_managed: false   # yurt dışında yerel ajan yönetiyorsa true
        local_agent: "[ad ya da null]"
        filings:
          - type: "[aşağıdaki listeden]"
            due_date: "[YYYY-MM-DD]"
            due_basis: "[fixed: MM-DD / fiscal-year-end + 3 ay / olay + N gün / görev süresi sonu]"
            last_filed: "[tarih ya da null]"
            last_fee: "[tutar ya da null]"
            status: "[current / due_soon / overdue / unknown]"
            confirmed_good_standing: "[sicil tasdiknamesi / faaliyet belgesi tarihi ya da null]"
            notes: ""
```

Durum değerleri: `current` (dönem için yapıldı, 90 gün içinde iş yok) · `due_soon` (90 gün içinde) · `overdue` (son gün geçti, yapıldı kaydı yok) · `unknown` (bilgi yok; teyit gerekir).

**Türkiye takvimi — `filings.type` listesi** (hesap dönemi 31.12 ise örnek tarih):

| Kalem | Kural | Örnek son gün |
|---|---|---|
| Yevmiye ve diğer fiziki defterlerin açılış onayı | Kullanılacağı dönemin ilk ayından önceki ayın sonuna kadar noter; pay defteri ile GK toplantı ve müzakere defteri yaprak yeterliyse onaysız devam eder (m. 64/3) | 31.12 |
| YK karar defteri kapanış onayı (fiziki) | İzleyen faaliyet döneminin birinci ayının sonuna kadar (m. 64/3) | 31.01 |
| Yevmiye defteri kapanış onayı (fiziki) | İzleyen faaliyet döneminin altıncı ayının sonuna kadar (m. 64/3) | 30.06 |
| Elektronik defter | Açılışta ve yevmiye ile YK karar defterinin kapanışında noter/sicil onayı aranmaz (m. 64/3); e-defter takvimini mali müşavirle teyit et | — |
| Finansal tablolar + YK yıllık faaliyet raporu | Bilanço gününü izleyen dönemin ilk üç ayı içinde hazırlanır ve GK'ya sunulur (m. 514); denetime tabi şirkette denetlenmemiş tablo düzenlenmemiş hükmündedir (m. 397/2) | 31.03 |
| Bağlılık raporu (grup şirketi) | Bağlı şirketin YK'sı faaliyet yılının ilk üç ayı içinde düzenler (m. 199/1) | 31.03 |
| GK belgelerinin incelemeye açılması | Toplantıdan en az 15 gün önce (m. 437/1) | GK − 15 gün |
| Olağan GK | Dönem sonundan itibaren 3 ay (m. 409/1, 617/1) | 31.03 |
| GK tutanağı tescil ve ilanı | Noter onaylı suret derhâl sicile; internet sitesine hemen (m. 422/2) | GK + derhâl |
| Denetçi seçimi ve tescili | Denetleyeceği faaliyet dönemi bitmeden seçilir; YK gecikmeksizin tescil ve ilan ettirir (m. 399/1); dördüncü aya kadar seçilmezse istem üzerine mahkeme atar (m. 399/6) | Dönem içinde; en geç 4. ay |
| YK / müdür görev süresi | YK en çok 3 yıl (m. 362/1); boşalan üyelik ilk GK onayına (m. 363/1) | Seçim + süre |
| Temsil yetkisi değişikliği | Noter onaylı karar sureti tescil ve ilan için sicile (m. 373/1) | Karar + derhâl |
| Pay edinim/elden çıkarma bildirimi (grup) | %5, 10, 20, 25, 33, 50, 67, 100 eşiklerinde işlemin tamamlanmasını izleyen 10 gün içinde şirkete ve makamlara; bildirim tescil ve ilan olunur; yapılmazsa oy dâhil haklar donar (m. 198/1-2; TSY m. 107/5-6). Yönetmelikte yükümlülük, payı edinen teşebbüsün bir şirketler topluluğuna dâhil olmasına bağlanmıştır (TSY m. 107/2) | İşlem + 10 gün |
| İnternet sitesi (denetime tabi) | Tescilden itibaren 3 ay içinde açılır; kanunda ayrı süre yoksa içerik en geç 5 gün içinde konur ve en az 6 ay kalır (m. 1524/1, 1524/5) | — |
| Tescil edilmiş olguda değişiklik | Her türlü değişiklik tescil edilir (TSY m. 29/1); ilan edilmeyen husus üçüncü kişiye ancak bildiği ispatlanırsa ileri sürülür (m. 36/4). Gecikmede sicil müdürlüğü 30 gün süreli davet ve idari para cezası yoluna gider (TSY m. 36/1, 36/3; m. 33/2) | Değişiklik + 15 gün; müdürlüğün yetki çevresi dışında oturanlar için 1 ay (Kanunda veya Yönetmelikte ayrı süre yoksa; TSY m. 33) |
| Belgelerin saklanması | Defterler, finansal tablolar, faaliyet raporları ve dayanak belgeler 10 yıl (m. 82/5) | — |
| Halka açık | Finansal raporlar (SerPK m. 14), özel durum açıklamaları (m. 15), kurumsal yönetim (m. 17) — SPK düzenleme takvimini `tr_kurum_karari_ara` (spk) ve `tr_spk_bulten_icinde_ara` ile kontrol et | SPK takvimi |
| VERBİS kaydı | Kişisel veri işleyen gerçek ve tüzel kişiler işlemeye başlamadan önce Veri Sorumluları Siciline kaydolur; Kurul objektif kriterlerle istisna getirebilir; bildirilen bilgilerdeki değişiklik derhâl bildirilir (KVKK m. 16/2, 16/4). İstisna kapsamını `tr_kurum_karari_ara` (kvkk) ile teyit et | Değişiklik + derhâl |

## Mod 1 — Kurulum

Takip dosyası yoksa ya da `--rebuild` ile.

**Adım 1 — Şirket tablosunu yükle:** `## Entity Management` → şirket tablosu. Boşsa `/arthurlegal:corporate-legal-cold-start-interview --module entities` öner ya da listeyi iste.

**Adım 2 — Her şirket × ülke için yükümlülükleri teyit et.** Önbellekteki takvime güvenme.
1. Mali müşavirin ya da yerel ajanın güncel takvimi var mı? En güvenilir kaynak odur.
2. Yoksa kullanıcının bildiklerini sor: hesap dönemi, denetime tabi mi, defter fiziki mi elektronik mi, son GK tarihi, YK seçim tarihi, denetçi.
3. Bilinmeyeni `unknown` yap; tarih uydurma.

Yerleşik tabloda olmayan ülke için:

> [Ülke] için takvimim yok; şimdi kaydedelim. [Şirket] için: 1. Hangi yıllık yükümlülük (yıllık bildirim, hesapların yayımı, genel kurul)? 2. Son gün nasıl hesaplanır (sabit tarih, kuruluş ayı, hesap dönemi + N ay)? 3. Tipik ücret (yaklaşık ya da "bilinmiyor")? 4. Orada işi kim yürütüyor?

Cevabı `custom_jurisdictions` bloğuna yaz (`jurisdiction`, `jurisdiction_type`, `filings` [`type`, `due_basis`, `typical_fee`, `notes`], `added_by: "manual"`, `added_date`); o ülkedeki tüm şirketlere uygulanır. Yurt dışı şirkette sor: yerel ajan var mı (`agent_managed: true` + `local_agent`), grup düzeyinde raporlama (gerçek faydalanıcı sicili, ülke bazlı raporlama) var mı. Kuruluş ayına bağlı yükümlülükte `formation_date` yoksa `unknown`.

**Adım 3 — Yaz ve özetle:**

```
Şirket uyum takibi kuruldu.
Şirket: [N] · Ülke/sicil: [N] · İzlenen kalem: [N]
  ✅ Güncel: [N]   ⏰ Yaklaşan: [N] (90 gün)   🔴 Gecikmiş: [N]   ❓ Bilinmiyor: [N]
Ne var görmek için: /arthurlegal:corporate-legal-entity-compliance --report
```

## Mod 2 — Rapor

`/arthurlegal:corporate-legal-entity-compliance --report [--days 30|60|90|180]` (varsayılan 90).

```
ŞİRKET UYUM RAPORU — [tarih] — [Müvekkil]
🔴 GECİKMİŞ ([N]):   [Şirket] / [ülke] / [kalem] — son gün [tarih] (dayanak)
⏰ [N] GÜN İÇİNDE ([N]):   [Şirket] / [ülke] / [kalem] — son gün [tarih]  [sorumlu]
✅ SON 90 GÜNDE YAPILAN ([N]):   [Şirket] / [kalem] — [tarih]
❓ BİLİNMEYEN ([N]):   [Şirket] / [kalem] — bilgi yok; mali müşavir/sicil ile teyit
🌐 YEREL AJANDA ([N]):   [Şirket] / [ülke] — [ajan]; durumu doğrudan teyit edin
SİCİL TEYİDİ:
  Son tasdikname/faaliyet belgesi: [tarih] · 12 aydan eski: [liste]
```

Takip 10'dan fazla şirket içeriyorsa ya da istenirse pano öner (CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`): duruma göre sayılar, sicil teyidi durumu, sıralanabilir şirket tablosu.

## Mod 3 — Güncelleme

### Sonuç doğuran eylem kapısı (tescil başvurusu, defter onayı, GK)

Başvuruya yönlendirmeden ya da `last_filed` kaydetmeden önce `## Who's using this` → Role **avukat değilse**:

> Ticaret siciline tescil başvurusu, defter onayı ya da genel kurul işlemi şirketin resmî beyanıdır; yanlış veya geç işlem idari para cezası, kararın üçüncü kişilere karşı ileri sürülememesi ya da iptal riski doğurur. Avukatla (ya da mali müşavirle) gözden geçirdiniz mi? Hayırsa brif: şirket, kalem, son gün · takipteki son kayıt · açık sorular (yetkililer ve temsil şekli güncel mi, merkez/adres değişti mi, esas sözleşme değişikliği var mı) · ne ters gidebilir · sorulacaklar (bu yıl gerçekten gerekli mi, kim imzalar). Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz.

Açık "evet" olmadan yeni `last_filed` kaydetme. Okuma ve rapor kapı gerektirmez.

**3a — Elle:** "[Şirket] olağan genel kurulu 25.03'te yapıldı, tutanak 28.03'te sicile verildi." → `last_filed`, `status: current`, `metadata.last_updated`; tutanak tescili için ayrı kalem aç.

**3b — Rapordan (`--from-report`):** mali müşavir takvimi, sicil tasdiknamesi, TTSG ilanı, MERSİS çıktısı ya da yurt dışı ajan raporu (PDF, CSV, Excel). Her şirket için kalem, son gün, yapılma tarihi, sicil teyidi, uyarıları çıkar; unvana göre eşleştir, yakın eşleşmeyi sor ("ABC Holding A.Ş." / "ABC HOLDİNG ANONİM ŞİRKETİ"). Sonuç: eşleşen / raporda olup takipte olmayan / takipte olup raporda olmayan.

**3c — Tarama (`--sweep`):** `unknown` ve `overdue` kalemleri tek tek sor: "[Şirket] / [kalem] — [durum]. Yapıldı mı? Ne zaman?" Her cevaptan sonra yaz, sonda özet ver.

## Mod 4 — Sağlık denetimi (`--audit`)

- **Uyum:** gecikmiş ve bilinmeyen kalemler.
- **Faaliyetsiz şirketler:** `dormant` olanlar — tasfiye adayı mı? Taşıma maliyeti ve süren yükümlülükler (GK, defter, mali müşavir). 5 yıldan uzun süredir faaliyetsizse tasfiye adayı olarak işaretle. `formation_date` eksikse veri boşluğu.
- **Sermaye kaybı:** son yıllık bilançoda sermaye ile kanuni yedek akçeler toplamının yarısı zarar nedeniyle karşılıksız kaldıysa YK GK'yı hemen toplantıya çağırır; üçte ikisi karşılıksızsa ve GK sermayenin üçte biriyle yetinme ya da tamamlama kararı vermezse şirket kendiliğinden sona erer; borca batıklık şüphesinde ara bilanço ve gerekirse mahkemeye bildirim (m. 376). Finans verisi yoksa soruyu işaretle.
- **Yönetim organı:** görev süresi dolmuş ya da 90 gün içinde dolacak YK üyeleri/müdürler (m. 362/1); tescilli temsil yetkisi güncel mi (m. 373).
- **Denetim:** denetime tabi şirkette dönem için denetçi seçilmiş ve tescil edilmiş mi (m. 399/1, 399/6); denetçi olamayacak kişi kuralları (m. 400) için denetçinin şirkete başka hizmet verip vermediği.
- **Sicil teyidi:** tasdikname/faaliyet belgesi hiç yok ya da 12 aydan eski — işlem veya finansman öncesi yenile.
- **Grup:** pay edinim bildirimleri (m. 198) ve bağlılık raporu (m. 199) eksik mi; şirketler arası sözleşmeler (hizmet, lisans, borç) var mı; yabancı ana şirketin LEI ve grup yapısı `gleif_get_group_structure` ile tabloyla tutarlı mı.
- **Şube:** yabancı şirket şubesinde ticari mümessil tescilli mi (m. 40/4).

```
ŞİRKET SAĞLIK DENETİMİ — [tarih]
UYUM: gecikmiş [N] · bilinmeyen [N] → --sweep
FAALİYETSİZ ([N]): [liste, yaş] · tasfiye adayı: [liste]
SERMAYE KAYBI / BORCA BATIKLIK: [işaretler ya da "veri yok"]
YÖNETİM ORGANI: süresi dolan [liste] · temsil tescili eski [liste]
DENETİM: denetçi seçilmemiş/tescilsiz [liste]
SİCİL TEYİDİ: kayıt yok [N] · 12 aydan eski [N]
GRUP: bildirim/bağlılık raporu eksik [liste]
ÖNERİLEN EYLEMLER: 1. [en öncelikli] 2. [..]
```

## Mod 5 — Dışa aktarma

`/arthurlegal:corporate-legal-entity-compliance --export [--format csv|table]` (varsayılan CSV). Sütunlar:
`Entity Name, Entity Type, State of Formation, MERSIS No, Formation Date, Status, Registered Agent, Jurisdiction, Qualification Type, Filing Type, Due Date, Last Filed, Last Fee, Good Standing Confirmed, Notes`
Her ülke × kalem bir satır. `--format table`: yalnız sonraki 90 günü gösteren markdown tablo.

**Formül enjeksiyonu savunması:** Excel/Sheets/CSV'ye yazmadan önce belge, araç sonucu ya da yapıştırmadan gelen her metin hücresinde `=`, `+`, `-`, `@`, sekme ya da satır başı ile başlayan değerin önüne tek tırnak koy (`'=SUM(A1:A10)`). CSV'de virgül, çift tırnak ve satır sonunu RFC 4180'e göre tırnakla. Kendi yazdığın başlıklar ve hesapladığın değerler güvenlidir. İsteğe bağlı değildir.

## Bu skill ne yapmaz

- Başvuru yapmaz, deftere onay almaz, genel kurul toplamaz; çıktı takip ve yapılacaklar listesidir.
- Sicil tasdiknamesi ya da faaliyet belgesi almaz; son teyit tarihini izler.
- Bir şirketin bağımsız denetime tabi olup olmadığına ya da şube açılması gerekip gerekmediğine karar vermez; olgulara bağlıdır, avukat ve mali müşavir teyit eder.
- Vergi, SGK ve sektör düzenleyicisi (BDDK, EPDK, SPK) takvimlerinin yerini tutmaz.
- Takvim tablosu hukuki görüş değildir; güncel olmayabilir. Güvenmeden önce teyit edin.

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
