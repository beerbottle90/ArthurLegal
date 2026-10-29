---
name: corporate-legal-tabular-review
description: >
  Tablolu inceleme — her belgeye bir satır, her veri noktasına bir sütun, her
  hücre kaynağa atıflı. M&A due diligence için kuruldu ("bu 200 hedef
  sözleşmede kontrol değişikliği, devir ve MAC klozlarını çıkar") ama sonunda
  tablo isteyen her toplu incelemede çalışır. "Tablolu inceleme", "inceleme
  tablosu", "grid kur", "bu sözleşmelerden şu alanları çıkar", "bu belgeleri X,
  Y, Z için incele", "bana tablo ver", "toplu inceleme" denildiğinde ya da bir
  belge klasörü gösterilip karşılaştırma istendiğinde kullan.
---

# /tabular-review — Tablolu İnceleme

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` yükle → `## M&A` inceleme yapısı (`Diligence structure`), eşikler, büro formatı.
2. Teyit et: hangi belgeler, hangi sütunlar, çıktı nereye.
3. Tipli şemayı kur, `.review-schema.yaml` olarak yaz, kullanıcıya onaylat.
4. Örnek çalıştırma (3–5 belge). Şemayı düzelt, onaylat.
5. Dağıt — belge başına bir alt ajan, paralel. Her hücre: değer + durum + birebir alıntı + yer.
6. Normalleştirme geçişi. Aykırı ve tutarsız değerleri işaretle.
7. Çıktı: `.xlsx` ya da Google Sheets (sor), ayrıca her zaman `.csv` + `_sources.csv` + markdown. Üst başlık.
8. Özet: doğrulama yükü (sütun başına not_present / unclear / needs_review), işaretli sütunlar, dosya yerleri, "her hücre bulgu değil ipucudur" hatırlatması.

```
/arthurlegal:corporate-legal-tabular-review
/arthurlegal:corporate-legal-tabular-review --schema .review-schema.yaml --docs ./vdr/02-Sozlesmeler/
/arthurlegal:corporate-legal-tabular-review --template ma-diligence
```

`--schema <yol>` mevcut şemayı kullanır (yeniden çalıştırma, ekleme). `--template <ad>` `references/` altındaki şablondan başlar (şimdilik `ma-diligence`). `--docs <yol>` yerel klasör, Drive klasör kimliği ya da VDR yolu; yoksa sorar. `--output <xlsx|gsheets|csv>` yoksa sorar. `--sample <n>` örnek boyutu (varsayılan 5).

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Elinde bir yığın belge ve her birine tutarlı biçimde sorulacak bir soru listesi var: due diligence talep listesi, tedarikçi sözleşmesi denetimi, kira portföyü. Çıktı bir tablodur: satırlar belge, sütunlar veri noktası, her hücre kaynaktaki kelimelere kadar izlenebilir.

Bu sorun avcılığı değildir: `diligence-issue-extraction` 2.000 belgedeki 30 sorunu bulur; bu skill aynı 15 soruyu 2.000 belgenin hepsine sorar. Bu, belgeyi okumanın yerini de tutmaz: her hücre **doğrulanması gereken bir ipucudur**. Çıktı doğrulamayı hızlandırmak için tasarlanır, atlamak için değil.

Bağlam: CLAUDE.md, belirli işlemde `deals/[code]/deal-context.md` (işlem yapısı sütunların yorumunu değiştirir: pay devrinde devir klozu değil CoC klozu önemlidir), varsa mevcut `.review-schema.yaml`.

## Sütun tipleri

Tablonun değeri, C sütununun 1. satırda ve 200. satırda aynı şeyi ifade etmesidir. Serbest metin kayar; tip tutar.

| Tip | Döndürdüğü | Kullanım |
|---|---|---|
| `verbatim` | Belgeden karakteri karakterine alıntı | Tanımlı terimler, işletici kloz metni, kelimelerin önemli olduğu her yer |
| `classify` | Sabit listeden tek değer | Evet/Hayır, var/yok, kloz varyantları |
| `date` | ISO tarih | Yürürlük, bitiş, fesih bildirimi son günü |
| `duration` | Sayı + birim | Süre, bildirim süresi, beyanların geçerlilik süresi |
| `currency` | Sayı + para birimi kodu | Tavan, eşik, bedel (TRY, EUR, USD…) |
| `number` | Yalın sayı | Adet, yüzde, sayfa |
| `free` | Kısa serbest özet | Az kullan — kayan tip budur |

**Birebir kuralı:** `verbatim` dışındaki her sütun, cevabı destekleyen kaynak alıntısını yan alan olarak taşır. Hücredeki cevap yorumdur; alıntı delildir. "consent_not_unreasonably_withheld" diyen bir hücre, geldiği cümle olmadan işe yaramaz.

## "Bulunamadı"nın üç durumu

Boş hücre bilgi saklar. Olumlu cevap üretemiyorsan üç açık durumdan birini kullan:

| Durum | Anlamı |
|---|---|
| `not_present` | Belge okundu, hüküm yok |
| `unclear` | Bir şey var ama güvenle sınıflanamıyor (belirsiz, kısmi ya da çelişen hükümler) |
| `needs_review` | Bir şey bulundu ama kararı insan vermeli (sıra dışı metin, şemanın yakalamadığı takdir) |

"Sözleşme devir konusunda sessiz" ile "devir klozu belirsiz" işlem ekibi için bambaşka işlerdir; tek boş hücrede birleştirme.

## Akış

### Adım 0: Ne ve nerede

1. **Belgeler:** VDR MCP'si (Box, Datasite, iManage), yerel klasör, Drive ya da dosya listesi. Kaç adet? 200'ü aşarsa uyar ve önemlilik süzgeçli alt küme öner.
2. **Şema:** `references/` şablonu (varsayılan M&A due diligence) ya da kullanıcının doğal dilde tarif ettiği sütunlar → tipli şema.
3. **Çıktı:** Excel mi Google Sheets mi — sor, tahmin etme. CSV ve markdown her zaman yazılır.

### Adım 1: Şemayı kur ve onaylat

Her sütun için kalıcı `id`, insan okunur `label`, `type`, `prompt` (belgeyi okuyan incelemecinin soracağı soru) ve `classify` için `options`. `id` ve `options` değerleri İngilizce kalır (başka skill'ler ve dışa aktarımlar bunları okur); `label` ve `prompt` Türkçe olur.

```yaml
schema:
  name: "M&A Due Diligence — Proje [Kod]"
  created: 2026-10-26
  columns:
    - id: counterparty
      label: "Karşı taraf"
      type: verbatim
      prompt: "Hedef dışındaki sözleşme tarafı kim (unvanıyla)?"
    - id: effective_date
      label: "Yürürlük tarihi"
      type: date
      prompt: "Sözleşme hangi tarihte yürürlüğe girdi?"
    - id: change_of_control
      label: "Kontrol değişikliği"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, automatic_termination, termination_right, notice_only]
      prompt: "Sözleşme hedefin kontrolünün değişmesini düzenliyor mu? Ne gerektiriyor?"
    - id: assignment
      label: "Devir sınırlaması"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, freely_assignable, assignable_to_affiliates]
      prompt: "Hedef bu sözleşmeyi devredebilir mi? Hangi sınırlama var?"
    - id: merger_reference
      label: "Birleşme/bölünmeye atıf"
      type: classify
      options: [silent, treated_as_assignment, permitted, termination_right]
      prompt: "Devir/CoC hükmü birleşme, bölünme ya da tür değiştirmeyi açıkça anıyor mu?"
    - id: governing_law
      label: "Uygulanacak hukuk"
      type: verbatim
      prompt: "Sözleşmeye hangi hukuk uygulanır?"
    - id: dispute_forum
      label: "Uyuşmazlık yeri"
      type: classify
      options: [turkish_courts, turkish_arbitration, foreign_courts, foreign_arbitration, silent]
      prompt: "Uyuşmazlıklar hangi mahkemede ya da tahkimde çözülür?"
    # ... diğer sütunlar
```

`merger_reference` sütununu birleşme/bölünme yapısında ekle: sözleşmedeki devir yasağının külli halefiyete (TTK m. 153/1) uygulanıp uygulanmadığı **tartışmalı** olduğundan açık metin önemlidir. Kira için `lease_assignment` (TBK m. 323), kamu sözleşmeleri için `public_contract` (4735 m. 16) sütunlarını düşün. Şemayı çıktının yanına yaz; kullanıcı düzenleyip yeni belgelerle yeniden çalıştırabilir. Dağıtmadan önce göster ve onay al.

### Adım 2: Örnek çalıştırma

Denenmemiş şemayı 200 belgeye dağıtma. Önce 3–5 belge çalıştır, satırları göster. Bak:
- Çoğu cevabı `unclear` olan sütun → istem belirsiz, yeniden yaz.
- Seçeneklere uymayan `classify` cevapları → seçenek ekle ya da `free`'ye çevir.
- Parafraz dönen `verbatim` sütun → karakteri karakterine kuralını pekiştir.
- Türkçe ve yabancı dilde karışık belgeler → alıntı belgenin kendi dilinde kalır, çeviri yapılmaz; iki dilli sözleşmede hangi metnin esas olduğunu ayrı sütunda yakala.

Şemayı düzelt, örneği yeniden çalıştır, onay al.

### Adım 3: Dağıt

Belge başına bir alt ajan, paralel. Her alt ajan belgenin tamamını okur (RAG parçası değil), her sütun için ilgili hükmü bulur ve şunu döndürür: `{value, state, quote, location}` — `value` tipli cevap (`state` `answered` değilse null), `state` `answered | not_present | unclear | needs_review`, `quote` birebir destek metni, `location` madde numarası / başlık / sayfa.

**Alıntı isteğe bağlı değildir; birebir kuralı mekaniktir.** `state: answered` döndürmeden önce:
- `quote`, kaynaktaki bitişik metnin karakteri karakterine kopyası olmalı ve belirtilen `location`'da bulunabilmeli. Başlık + beklenen kalıp metinden alıntı kurma; parafraza "birebir" deme; "bu klozlar genelde şöyledir" bilgisinden alıntı yeniden üretme; bitişik olmayan metni üç noktayla dikme. Keseceksen cümle sınırında kes ve işaretle.
- `location`, normalleştirme geçişinin aynı yeri yeniden açabileceği kadar belirli olmalı.
- Kesin metin bulunup kopyalanamıyorsa (kaynak kesik, OCR bozuk, hüküm ima ediliyor ama yazılı değil) durum `needs_review`, `value` null ve `notes` içinde `quote_unavailable: <sebep>`. Kurgulanmış alıntıyla `answered` asla kabul edilmez.
- Aynı kural `verbatim` sütunlara ve diğer tiplerin yan alıntılarına aynen uygulanır.
- Kişisel veri (çalışan adı, TCKN, ücret) yalnız sütunun gerektirdiği ölçüde alınır (KVKK m. 4/2-ç: amaçla bağlantılı, sınırlı ve ölçülü).

### Adım 4: Normalleştir

Tabloyu sütun sütun oku; her tablolu inceleme aracının hata modu aynı klozun belgeler arasında farklı yorumlanmasıdır.
- **`classify`:** her `answered` değer seçenek listesinde mi? Kümelenmeye bak: 180 `consent_required` / 20 `consent_not_unreasonably_withheld` muhtemelen gerçektir; 195 / 5 `freely_assignable` ise o 5'e bak.
- **`date` / `duration` / `currency`:** biçimi eşitle; makul olmayanları (99 yıllık süre, 1 TL tavan) `needs_review` yap.
- **`verbatim` ve tüm yan alıntılar:** rastgele örnekte (sütun başına en az 3–5 satır ya da satırların %10'u, hangisi büyükse) kaynağı belirtilen yerde yeniden aç, alıntıyı karakteri karakterine karşılaştır. Uyuşmazlıkta hücreyi `needs_review` + `quote_mismatch` yap ve tüm sütunu genişletilmiş kontrole al — bir alt ajan alıntı kurguladıysa diğerleri de kurgulamış olabilir. Uyuşmayan alıntılı `answered` hücre, `unclear`'dan ağır bir hatadır.

### Adım 5: Çıktı

**Markdown** (her zaman, oturum içi inceleme):
```markdown
| Belge | Karşı taraf | Yürürlük | Kontrol değişikliği | Devir | ⚠️ İşaret |
|---|---|---|---|---|---|
| Hizmet Sözleşmesi — Alfa | Alfa A.Ş. | 2023-04-01 | consent_required | consent_required | — |
| Tedarik Sözleşmesi — Beta | Beta Ltd. Şti. | 2021-11-15 | ⚠️ unclear | silent | CoC belirsiz m. 14.2 |
```

**CSV** (her zaman): değerler için bir dosya, alıntı ve yerler için `_sources.csv`.

**Excel ya da Google Sheets** (kullanıcının çalıştığı; sor). Yapı `${CLAUDE_PLUGIN_ROOT}/references/excel-output.md` ve `${CLAUDE_PLUGIN_ROOT}/references/gsheets-output.md`'de. Excel: Claude in Excel varsa o, yoksa `openpyxl`; Sheets: Sheets MCP, ADC ile Sheets API ya da CSV içe aktarma. Her veri sütununun yanında alıntı + yer taşıyan gizli sütun; görünür hücrede açıklama/not olarak alıntı. Renk: beyaz = answered, sarı = unclear/needs_review, gri = not_present. Her veri sütunu için varsayılan boş `Verified` sütunu — incelemeci işaretler; insanın neyi kontrol ettiği bir bakışta görünür. Sütun tanımlarını içeren `_schema` sayfası.

**Formül enjeksiyonu:** belgeden ya da araçtan gelen ve `=`, `+`, `-`, `@`, sekme ya da satır sonuyla başlayan her hücrenin başına tek tırnak koy; CSV'de virgül, çift tırnak ve satır sonlarını RFC 4180'e göre tırnakla.

En üst satıra CLAUDE.md `## Outputs` başlığını koy ve yanına ekle:

> Bu inceleme gizli kaynak belgelerden türetilmiştir ve onların gizlilik statüsünü devralır. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) dağıtılan belgeyi korumaz; dağıtımı işlem ekibiyle sınırla.

### Adım 6: Özet

Belge, sütun ve tamamlanan satır sayısı; sütun başına `not_present` / `unclear` / `needs_review` sayıları (doğrulama yükü budur); normalleştirmede satırların %10'undan fazlası işaretlenen sütunlar; dosyaların yeri; hatırlatma: her hücre ipucudur, beyan, ek ya da not beslemeden önce doğrulanmalıdır.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu tabloya göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Belgeleri okumanın yerini tutmaz; nereye bakacağını söyler.
- Güven puanı üretmez. 0,73 bilgi değildir; güven sinyali `unclear` / `needs_review` durumları ve birebir alıntılardır.
- Belgeyi sessizce atlamaz: gösterilen her belge bir satır alır; okunamayan belge `needs_review` satırı ve notu alır.
- Parafrazı alıntı gibi sunmaz; delil izi işin kendisidir.

## Diğer skill'lerle ilişki

- `diligence-issue-extraction` sorun bulur; bu skill veri noktası çıkarır. Çıkarım bir sorun gösterirse (belirli bir kazanç hedefine bağlı MAC tanımı, olağandışı fesih hakkı) not et ve o belge için diligence-issue-extraction öner.
- `material-contract-schedule` tek bir tabloyu (önemli sözleşmeler eki) kurar ve bu skill'in çıktısını doğrudan kullanabilir — ek, tablolu incelemenin süzülmüş ve biçimlenmiş görünümüdür.
- `ai-tool-handoff` korpus çok büyükse ya da ekip özel platform tercih ediyorsa toplu incelemeyi Luminance/Kira'ya verir. Önce bu skill'i çalıştır, kalanı devret.

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
