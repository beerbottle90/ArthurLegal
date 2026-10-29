---
name: administrative-legal-idari-para-cezasi-itiraz
description: >
  Çevre Bakanlığı, EPDK, KVKK, Rekabet, BDDK, SPK gibi düzenleyici kurumların
  idari para cezası kararlarına karşı iptal davası hazırlık. İYUK m. 7 + m. 27
  yürütmenin durdurulması, görevli mahkeme (ilgili il İdare Mahkemesi veya Ankara).
  `idari-dava-prep` skill'inin idari ceza odaklı varyantı.
user-invocable: true
---

# İdari Para Cezası İptal Davası

## ⏰ Süre

İdari para cezası tebliğinden, özel kanunda ayrı süre yoksa **60 gün** (İYUK m. 7 — idare mahkemesi genel kuralı); **Çevre Kanunu idari yaptırımlarında 30 gün** (2872 m. 25 özel hükmü). Kurum bazında özel süre kontrolü şart. Hak düşürücü.

⚠️ **Önce yol:** Dayanak kanun idari yargıyı göstermiyorsa idari para cezasına karşı yol iptal davası değil, Kabahatler K. m. 27'ye göre tebliğden itibaren **15 gün** içinde sulh ceza hâkimliğine başvurudur. KVKK Kurul cezalarında 2024'ten beri idare mahkemesi (6698 m. 18/3).

## Tetik

> Hangi kurumun idari para cezası?
> - Çevre Bakanlığı (2872 ÇK) — [tesis yeri] çevre ihlali
> - EPDK (5015 PPK / 4646 DGPK / 6446 EPK) — lisans şartı ihlali
> - KVKK (6698) — veri ihlali
> - Rekabet Kurumu (4054) — Rekabet ihlali
> - BDDK / SPK / KGK — finansal düzenleyici
> - Çalışma Bakanlığı / SGK — İSG ihlali / sigorta primi

## Önemli: Tahsil + ceza ayrı

İdari para cezası kararı iki ayrı süreç:
1. **İptal davası** (İYUK m. 7 — 60 gün genel / 2872 m. 25 — çevre cezasında 30 gün) → İdare Mahkemesi
2. **Tahsil** (AATUHK 6183) → Vergi Dairesi tarafından

**Tahsil paralel başlar.** İptal davasında **yürütmenin durdurulması (İYUK m. 27)** alınmazsa, dava sürerken para tahsil edilebilir.

## Görevli mahkeme

| Ceza kaynağı | İlk derece |
|---|---|
| Çevre Bakanlığı merkez | Ankara İdare Mah. |
| Çevre İl Müdürlüğü ([tesis yeri]) | İzmir İdare Mah. |
| EPDK Kurul kararı | Ankara İdare Mah. |
| KVKK Kurul | Ankara İdare Mah. |
| Rekabet Kurulu | Ankara İdare Mah. |
| BDDK | Ankara İdare Mah. |
| SPK | Ankara İdare Mah. |
| ÇSGB (İSG cezası) | İlgili il İdare Mah. ([tesis yeri] için ilgili il) — doğrulanmadı: 6331'de özel yol yoksa Kabahatler K. m. 27 (sulh ceza, 15 gün) |

## Adımlar

### 1. Ceza analiz

| Soru | Cevap |
|---|---|
| Kurum | [...] |
| Karar tarihi + sayı | [...] |
| Ceza tutarı | TL |
| Hukuki dayanak (idarenin gösterdiği) | [Kanun madde] |
| Tebliğ tarihi | GG.AA.YYYY |
| Süre sonu | GG.AA.YYYY (kalan: N gün) |

### 2. Bir önceki uygulama / emsal

```
tr_ictihat_ara(
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  query="<kurum> idari para cezası iptal",
  date_from="2022-01-01"
)
```

### 3. Hukuki argümanlar (idari ceza-spesifik)

- **Yetkisizlik** — kurum bu cezayı vermeye yetkili mi?
- **Şekil eksikliği** — savunma alınmadı, tebligat hatalı, gerekçe yetersiz
- **Sebep yokluğu** — ihlal fiilen gerçekleşti mi (delil yetersiz)?
- **Konu hukuka aykırılığı** — ceza miktarı kanunda öngörülen aralık dışında
- **Amaç hukuka aykırılığı** — kurum başka bir amaç güdüyor
- **Mücbir sebep** — ihlal mücbir sebepten kaynaklandı mı?
- **İdarenin bekletme süresi** — soruşturma çok uzadıysa zaman aşımı

### 4. Yürütmenin durdurulması (m. 27)

**Telafisi güç zarar:** Ceza tutarı yüksekse nakit etkisi; EPDK lisans askıya alma ek tehdit; çevre cezası yatırım+itibar etkisi.

**Açıkça hukuka aykırılık:** Yukarıdaki en güçlü argüman.

### 5. sektöre-özel kontroller

- [ ] **Ceza tutarı > 10M TL** → CLCO + CEO eskalasyon
- [ ] **[TESİS LOKASYONU] İSG/çevre olayı kaynaklı** → litigation-legal `isg-incident-response` ile koordine
- [ ] **halka açık iştirak ilgili** → KAP açıklama kontrolü
- [ ] **EPDK lisans askıya alma riskini içeriyor mu** → derhal CLCO + iş birimi başkanı
- [ ] **Basın etkili** → İletişim Başkanlığı
- [ ] **Compliance koordinasyon** (KVKK → [DPO / Veri Koruma Sorumlusu]; Rekabet/EPDK → [Uyum Direktörü]/[Compliance Manager])

## Çıktı

```markdown
[ÜST BAŞLIK]

# İdari Para Cezası İptal — [Kurum / Karar no]

## ⚠️ İnceleyen notu
- **Kurum + ceza tutarı:** [...]
- **Süre kalan:** [N gün] 🔴/🟠
- **Görevli mahkeme:** [Ankara/İzmir İdare Mah.]
- **Yürütmenin durdurulması:** evet (gerekçe: [...])
- **Tahsil paralel başladı mı:** evet/hayır → AATUHK tehir-i icra ek yol
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (Danıştay [N])
- **Reviewer bekleyen:** N adet

[Ceza analizi + argümanlar + dilekçe taslak]

## Sonraki adımlar

> 1. **Dış idari avukatı brief**
> 2. **CLCO + CFO eskalasyon** (büyük tutar)
> 3. **Compliance koordinasyon** (kurum bazlı)
> 4. **KAP açıklama metni** (halka açık iştirak ilgili)
> 5. **Tehir-i icra paralel** (tahsil başladıysa)

**One question I'd ask:** [örn. "Bu ceza kurumun yıllık ortalamasının üstünde mi? Cezalar genelde benzer ölçekte mi yoksa [Müvekkil]'a karşı agresif mi?"]
```

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
| idare hukuku ogretisi — DergiPark *Idare Hukuku ve Ilimleri* dergisi router tarafindan secilir; **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
