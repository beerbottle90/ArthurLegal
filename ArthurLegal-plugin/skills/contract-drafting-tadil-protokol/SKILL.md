---
name: contract-drafting-tadil-protokol
description: >
  Ana sözleşmeye bağlı EK PROTOKOL / TADİL / SÜRE UZATIMI metni üretir — ana sözleşmeye
  atıf, "X maddesi aşağıdaki şekilde değiştirilmiştir" formatı, yürürlük, değiştirilmeyen
  hükümlerin saklılığı (severability), damga vergisi, imza. TBK tadil disiplini.
  Örnek: EPC süre uzatımı/iş artışı, PPA fiyat revizyonu, kredi tadili, SHA değişiklik.
user-invocable: true
---

# Tadil / Ek Protokol / Süre Uzatımı Üretimi

> Mevcut bir sözleşmeyi **değiştiren** belgeyi üretir (yeni sözleşme değil — `belge-turet` o iş için). Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı; yüksek tutar/stratejik → Genel Müdür.

## ADIM 0 — Girdi
1. **Ana sözleşme** — kullanıcı yapıştırsın/yüklesin (en azından değişen maddeler + taraflar + tarih).
2. **İstenen değişiklik** — ne değişiyor? (süre, bedel/fiyat, kapsam/iş artışı, taraf, teminat, fesih...).
3. **Tip:** süre uzatım · fiyat/bedel revizyonu · iş artışı/azalışı · taraf değişikliği (devir) · genel tadil.

## ADIM 1 — Tadil disiplini (kritik)

- **Şekil:** Ana sözleşme hangi şekilde yapıldıysa tadil de aynı şekilde (TBK m.13 — yazılı sözleşmenin değişikliği yazılı). EPDK/kamu onayına tabi sözleşmede onay şartı.
- **Atıf:** Ana sözleşmeyi tarih/no ile tanımla ("Ana Sözleşme").
- **Değişiklik formatı:** "Ana Sözleşme'nin [N] maddesi aşağıdaki şekilde **değiştirilmiştir**" / "**eklenmiştir**" / "**yürürlükten kaldırılmıştır**" — eski + yeni metni net ver.
- **Saklılık:** "Değiştirilmeyen tüm hükümler aynen yürürlüktedir."
- **Yürürlük:** imza/tarih; geriye etki isteniyorsa açıkça yaz.
- **Damga vergisi:** tadil ayrı damga doğurabilir (DVK — değişen tutar üzerinden) → `[DOLDUR/doğrulayın]`.
- **Sektörel özel:** süre uzatımı mücbir sebebe dayanıyorsa TBK m.136 gerekçesi; **EPDK lisans şartlarını etkiliyorsa** ön-onay; **SHA tadili** ise reserved matters + ortak/finansör onayı; **kredi tadili** ise finansör covenant/onay.
- **Madde doğrulama kapısı:** tadil metnine, gerekçesine ve eski/yeni metin karşılaştırmasına yazılan her kanun maddesi `/arthurlegal:contract-drafting-belge-turet` ADIM 2'deki kapıdan geçer; ana sözleşmedeki bir madde atfına tadilde dayanılıyorsa o da çekilir.

## ADIM 2 — Taslak

```markdown
[ANA SÖZLEŞME ADI] – [TADİL / EK PROTOKOL No: N]

TARAFLAR : [Müvekkil / Şirket] ([VKN/adres]) — [Karşı Taraf]
ANA SÖZ. : GG.AA.YYYY tarihli [ad] ("Ana Sözleşme")
KONU     : Ana Sözleşme'nin aşağıdaki maddelerinin tadili / [süre uzatımı] amacıyla.

MADDE 1 — [Değişiklik]
  Ana Sözleşme'nin [N]. maddesi aşağıdaki şekilde değiştirilmiştir:
  "[yeni madde metni]"
  (Eski metin: "[eski metin]" — kayıt için)

MADDE 2 — [varsa ek değişiklik]

MADDE 3 — SAKLILIK
  İşbu [Protokol/Tadil] ile değiştirilmeyen Ana Sözleşme hükümleri aynen yürürlüktedir.

MADDE 4 — YÜRÜRLÜK VE DAMGA
  Bu belge imza tarihinde yürürlüğe girer; Ana Sözleşme'nin ayrılmaz ekidir.
  Damga vergisi [DOLDUR — DVK]. [Gerekiyorsa: EPDK/Kurul onayı şartı.]

TARİH / İMZALAR: [Müvekkil / Şirket] ([imza yetkilisi]) — [Karşı Taraf]
```

## Çıktı
```markdown
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN İMZALANMAZ

# [Tadil / Ek Protokol] — [ana sözleşme] — No: [N]

## ⚠️ İnceleyen notu
- **Ana sözleşme:** [ad, tarih] · **Tadil tipi:** [...]
- **Değişen madde sayısı:** N
- **Onay/şart tetikleyici:** [EPDK ön-onay / SHA reserved matter / finansör covenant / damga — varsa]
- **Madde kontrolü:** [tadil metnindeki her madde atfı → okundu ve eşleşti / çekilemedi, gövdeden çıkarıldı]
- **Onay:** Baş Hukuk Müşaviri (+ Genel Müdür yüksek tutarda) şart

[taslak]

## Sonraki adımlar
> 1. **Onay/şart kontrolü** — EPDK / SHA / finansör tetiklendiyse ilgili süreç
> 2. **Redline** — `/arthurlegal:contract-drafting-redline-contract` ile son kontrol
> 3. **Damga vergisi** — DVK hesabı (`tax-legal` / `yazihane-asistani`)
> 4. **Başka**

**One question I'd ask:** [örn. "Bu tadil tek seferlik mi yoksa ana sözleşmenin dengesini kalıcı değiştiriyor mu? Kalıcıysa yan etkileri (fiyat, teminat, fesih) de gözden geçirmeliyiz."]
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
