---
name: corporate-legal-deal-team-summary
description: >
  Due diligence bulgularını okuyucuya uygun yükseklikte bir işlem ekibi
  brifingine toplar — yönetim/YK için yönetici özeti, işlem lideri için açık
  sorunlar ve kararlar, çalışma ekibi için tam ayrıntı. "İşlem ekibini
  bilgilendir", "due diligence ne durumda", "[kitle] için bulguları özetle",
  "işlem güncellemesi" denildiğinde ya da brifing takviminde kullan.
---

# /deal-team-summary — İşlem Ekibi Brifingi

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

İşlem lideri 200 bulgu okumaz; önemli olanı, son brifingten beri değişeni ve karar bekleyeni okur. Bu skill due diligence çıktısını okuyucunun seviyesine sıkıştırır.

## Bağlam

- `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → `## M&A` işlem ekibi bilgilendirmesi (`Deal team briefing`: takvim, kanal, iş tarafının ne okuduğu)
- `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` → işlem lideri, takvim, işlem yapısı; `firm-profile.md` → sorumlu ortak, müvekkil bilgisi
- `diligence-issue-extraction` çıktısındaki güncel bulgular; varsa `closing-checklist.yaml` (kapanış kalemlerinin durumu)

## Kitle katmanları

CLAUDE.md'deki "iş tarafı neyi okur, ne dosya için" ayrımına göre; yoksa varsayılan:

| Kitle | Alır | Almaz |
|---|---|---|
| **YK / yönetici sponsor** ([Müvekkil] tarafı) | En önemli 3-5 sorun, bedel/yapı etkisi, karar kalemleri | Kategori ayrıntısı, yeşil bulgular, süreç |
| **İşlem lideri** (sorumlu ortak) | Tüm kırmızı ve sarılar, ilerleme, kararlar, sonraki adımlar | Yeşil bulgu ayrıntısı |
| **Çalışma ekibi** | Her şey — tam bulgular, kategori durumu, boşluklar | Hiçbir şey saklanmaz |

Belli değilse hangi katman olduğunu sor.

**Dağıtım.** Brifing gizli due diligence bulgularını toplar ve onların gizlilik statüsünü devralır. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD tipi geniş bir belge koruması ("privilege") değildir; avukatı bağlar, müvekkilin geniş iş ekiplerine ya da danışmanlarına dağıtılan brifing gizliliğini fiilen kaybeder. Göndermeden önce dağıtım listesinin işlem ekibiyle örtüştüğünü teyit et; YK katmanı için ayrı, arındırılmış sürüm öner. Aile şirketinde paydaşlar arasında çıkar ayrılığı varsa (profildeki `Aile çatışması` notu) brifingin kime gittiğini sorumlu ortağa sor.

## Brifing

### Yönetici katmanı

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

# [işlem kodu] — Due Diligence Brifingi — [tarih]

**Durum:** [Yolunda / Sorunlar belirlendi / Önemli bulgular]
**Kapsam:** VDR'nin %[X]'i incelendi
**İşlem yapısı:** [pay devri / malvarlığı devri / birleşme]

## Önemli bulgular
[En çok 3-5. Her biri tek paragraf: ne, işlem için neden önemli, ne yapıyoruz.]

## Gereken kararlar
- [ ] [Somut karar — bedel düzeltmesi, tazmin/emanet talebi, işlemden çekilme eşiği] — [kim karar verir] — [ne zamana kadar]

## Son brifingten beri
[Değişenler: yeni bulgular, çözülenler, kapsam ilerlemesi.]
```

### İşlem lideri katmanı

Yukarıdakine ek olarak:

```markdown
## Kategoriye göre açık sorunlar
### 🔴 Kırmızı
[Bulgu başlığı + tek satır — tam bulguya bağlantı]
### 🟡 Sarı
[aynı]

## İlerleme
| Kategori | İncelenen | Kapsam | Kırmızı | Sarı | Durum |
|---|---|---|---|---|---|
| [ad] | [N/M] | [%] | [N] | [N] | [Tamam / Sürüyor / Engelli] |

## Kapanış yolu
[Rekabet izni, pay devri onayları, kritik karşı taraf onayları — closing-checklist Mode 4'ten kritik yol]

## Boşluklar ve takip
- [Bekleyen ek talep kalemleri]
- [Yönetime sorular]

## Önümüzdeki 72 saat
[Ne inceleniyor, hangi görüşmeler planlı]
```

### Çalışma ekibi katmanı

Tam bulgu ayrıntısı: aynı yapı, ama her bulgu tek satır yerine büro formatındaki tam bloğuyla (dayanak etiketleri ve tartışmalı notlar dahil).

## Farklar

Brifing tekrarlayan ise (CLAUDE.md takvimi) değişenle başla: son brifingten beri yeni bulgular, ciddiyeti yükselen/düşenler, çözülenler (onay alındı, sorun açıklandı), kapsam hareketi. İşlem liderleri durumdan çok harekete bakar: "hâlâ 12 sarı" yerine "2 yeni sarı, 3 çözüldü".

## Kaynak disiplini

Brifing yeni hukuki tespit üretmez; bulgulardaki etiketleri (`[ArthurLegal TR — 6102 m. X — GG.AA.YYYY]`, `[kullanıcı verdi]`, `[model bilgisi — doğrula]`) taşır, silmez. Yönetici katmanında madde numarasını sadeleştirebilirsin ama `doğrula` etiketli bir dayanağa dayanan bulguyu "doğrulanmadı" notuyla ver. Tartışmalı işaretli noktalar (ör. birleşmede devir yasağının uygulanması) karar kalemi olarak görünür, kesin sonuç gibi değil.

## Aktarımlar

- **diligence-issue-extraction'dan:** biriken bulgular okunur.
- **closing-checklist'e:** kapanış koşuluna dönüşen her "gereken karar" kalemi listeye gider (closing-checklist Mode 2 son brifingi okur).

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu brifinge göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Önemlilik kararı vermez — çıkarım sırasında verilen kararları raporlar.
- Ekibin bulguyla ne yapacağına karar vermez — kararı görünür kılar.
- Brifingi dağıtmaz — taslaklar, insan gönderir.

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
