---
name: contract-drafting-versiyon-karsilastir
description: >
  İki sözleşme versiyonunu (v1 ↔ v2 / bizim taslak ↔ karşı taraf revizesi) karşılaştırır —
  madde-madde track-changes/diff görünümü + her değişikliğin hukuki/ticari ETKİSİ +
  risk flag (karşı taraf ne kazandı/biz ne kaybettik). Müzakere turları ve "sessiz
  değişiklik" yakalama için. Claude.ai Projects: markdown diff; Claude Code: .docx compare.
user-invocable: true
---

# Versiyon Karşılaştırma (redline diff)

> Müzakere turunda **karşı tarafın neyi değiştirdiğini** yakalar — özellikle **sessizce eklenen/çıkarılan** klozları. Her çıktı **TASLAK**.

## ADIM 0 — Girdi
1. **İki versiyon** — v1 (örn. bizim son taslak) + v2 (örn. karşı taraf revizesi). Kullanıcı ikisini de yapıştırsın/yüklesin.
2. **Hangisi referans?** (genelde bizim son kabul ettiğimiz = baz).
3. Okuma kapsamını belirt; her ikisini de tam okuyamadıysan söyle.

## ADIM 1 — Madde eşle & diff çıkar

- Maddeleri başlık/numara ile eşle (numaralandırma kaymışsa içerikle eşle).
- Her madde için: **değişmedi / değişti / eklendi / silindi / taşındı**.
- Metin düzeyinde fark: ~~silinen~~ / **eklenen**.
- ⚠️ **Sessiz değişiklik avı:** tanım değişikliği, "shall→may", süre/eşik/tutar oynaması, istisna ekleme, sorumluluk tavanı, fesih kolaylaştırma, yetki/hukuk değişimi — küçük ama kritik.

## ADIM 2 — Etki & risk

Her değişiklik için:
- **Ne değişti** (kısa) · **Lehimize / aleyhimize / nötr** · **Severity** (🔴🟠🟡🟢) · **Etki** (hukuki/ticari sonuç) · **Aksiyon** (kabul / karşı-revize / müzakere).
- Emredici hüküm etkisi varsa `[ArthurLegal MCP (`tr_`)]`.

## ADIM 3 — Çıktı

```markdown
TASLAK – HUKUK MÜŞAVİRLİĞİ DAHİLİ

# Versiyon Karşılaştırma — [sözleşme] — v[X] ↔ v[Y]

## ⚠️ İnceleyen notu
- **Versiyonlar / okuma kapsamı:** [v1 tarih, v2 tarih, N sayfa]
- **Toplam değişiklik:** N (lehimize K · aleyhimize L · nötr M)
- **Kritik (🔴/🟠):** N adet
- **Onay:** Baş Hukuk Müşaviri (önemli değişiklik varsa)

## Özet — karşı taraf bu turda ne yaptı?
[2-4 cümle: en önemli hamleler + sessiz değişiklikler]

## Madde-madde diff
| # | Madde | Değişiklik (~~sil~~/**ekle**) | Yön | Severity | Etki | Aksiyon |
|---|---|---|---|---|---|---|
| 1 | 8.2 Sorumluluk tavanı | ~~%100~~ **%50 sözleşme bedeli** | aleyhe | 🔴 | tazminat hakkı yarıya iner | karşı-revize |

## Dikkat — sessiz/kritik değişiklikler
[🔴/🟠 maddelerin vurgusu]

## Sonraki adımlar
> 1. **Karşı-revize üret** — `/arthurlegal:contract-drafting-redline-contract` (aleyhe maddelere)
> 2. **Müzakere notu** — iş birimi/Genel Müdür için özet
> 3. **Governing law değiştiyse** — `/arthurlegal:commercial-legal-governing-law-review`
> 4. **Başka**

**One question I'd ask:** [örn. "Karşı taraf bu turda büyük taviz mi verdi yoksa küçük kazanımları paketleyip mi geçirdi? Cevap, kabul/itiraz stratejisini değiştirir."]
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
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | `/arthurlegal:legal-research-sozlesme-emsali` |
| AZ hukuku secilmisse emredici hukum kontrolu — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil) — okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `${CLAUDE_PLUGIN_ROOT}/references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
