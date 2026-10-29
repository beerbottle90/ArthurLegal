---
name: contract-drafting-cold-start-interview
description: >
  contract-drafting eklentisini ilk kez kuran kullanıcı için kısa röportaj — rol,
  birincil ortam (Claude.ai Projects / Claude Code), varsayılan çıktı formu (redline
  görünümü / temiz+liste / tablo), standart klozlar/şablonlar, onay zinciri.
  CLAUDE.md profilini doldurur. `--redo` ile yeniden çalışır.
user-invocable: true
---

# contract-drafting — Cold Start Interview

Amaç: `CLAUDE.md` profilindeki `[DOLDUR]` alanlarını 5-7 soruda doldurmak. Önce `firm-profile.md` + `${CLAUDE_PLUGIN_ROOT}/references/redline-konvansiyonlari-rehberi.md` okunur.

## Akış

### Adım 0 — Bağlam
`firm-profile.md` + bu plugin `CLAUDE.md` oku. Dolu alanları tekrar sorma.

### Adım 1 — Kullanıcı & ortam
> 1. Adın/rolün? ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri] / diğer)
> 2. Birincil ortam: **Claude.ai Projects** (markdown redline) mı, **Claude Code/VS Code** (gerçek .docx tracked-changes) mı? — çıktı yeteneğini belirler.

### Adım 2 — Çıktı tercihi
> 3. Varsayılan redline formu: (a) redline görünümü, (b) temiz revize + değişiklik/comment listesi, (c) yapılandırılmış tablo, (d) her seferinde sor.
> 4. Comment'lerde fallback pozisyon her zaman yer alsın mı? (önerilen: evet)

### Adım 3 — Şablon & onay
> 5. Sık kullandığın şablon/emsal türleri? (EPC, PPA/elektrik satış, vendor/tedarik, NDA, kredi/finansman, hissedar/JV, süre uzatım protokolü)
> 6. Standart klozlar (mücbir sebep, sınırlı sorumluluk, yaptırım/uyum, uyuşmazlık, EPDK devir, KVKK) varsayılan eklensin mi?
> 7. İmza öncesi onay eşiği? (varsayılan: Baş Hukuk Müşaviri; yüksek tutar/stratejik + Genel Müdür)

### Adım 4 — Yaz ve onayla
Cevapları `CLAUDE.md` `[DOLDUR]` alanlarına işle (özet göster, onay al, yaz). Matter workspace açık mı? Varsayılan: açık.

## Çıktı
Kısa özet + güncellenen alanlar + "Artık `/arthurlegal:contract-drafting-redline-contract`, `:belge-turet`, `:versiyon-karsilastir`, `:tadil-protokol` kullanabilirsin." yönlendirmesi.

## Not
`--redo`: tüm alanları yeniden sor.

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
