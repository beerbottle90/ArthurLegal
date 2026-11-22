# contract-drafting-versiyon-karsilastir

İki sözleşme versiyonunu (v1 ↔ v2 / bizim taslak ↔ karşı taraf revizesi) karşılaştırır — madde-madde track-changes/diff görünümü + her değişikliğin hukuki/ticari ETKİSİ + risk flag (karşı taraf ne kazandı/biz ne kaybettik). Müzakere turları ve "sessiz değişiklik" yakalama için. model.ai Projects: markdown diff; masaüstü uygulaması: .docx compare.

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
> 1. **Karşı-revize üret** — ``contract-drafting-redline-contract` iş akışı (`arthurlegal-sozlesme` becerisi, `../arthurlegal-sozlesme/references/contract-drafting-redline-contract.md`)` (aleyhe maddelere)
> 2. **Müzakere notu** — iş birimi/Genel Müdür için özet
> 3. **Governing law değiştiyse** — ``commercial-legal-governing-law-review` iş akışı (`arthurlegal-sozlesme` becerisi, `../arthurlegal-sozlesme/references/commercial-legal-governing-law-review.md`)`
> 4. **Başka**

**One question I'd ask:** [örn. "Karşı taraf bu turda büyük taviz mi verdi yoksa küçük kazanımları paketleyip mi geçirdi? Cevap, kabul/itiraz stratejisini değiştirir."]
```

---

## Kaynak katmanı: /legal-research

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur;
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar; gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | ``legal-research-sozlesme-emsali` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-sozlesme-emsali.md`)` |
| AZ hukuku secilmisse emredici hukum kontrolu: akt + statu | ``legal-research-az-mevzuat` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-az-mevzuat.md`)` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil): okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `../arthurlegal/references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `../arthurlegal/references/eqanun-mcp-rehberi.md` · `../arthurlegal/references/lex-scholar-rehberi.md` · `../arthurlegal/references/resourcecontracts-rehberi.md` · `../arthurlegal/references/karsilastirmali-hukuk-rehberi.md` · `../arthurlegal/references/nl-rechtspraak-mcp-rehberi.md` · `../arthurlegal/references/pl-sejm-mcp-rehberi.md` · `../arthurlegal/references/at-ris-mcp-rehberi.md` · `../arthurlegal/references/ie-statutebook-mcp-rehberi.md` · `../arthurlegal/references/fi-finlex-mcp-rehberi.md` · `../arthurlegal/references/es-boe-mcp-rehberi.md`
