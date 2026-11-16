# contract-drafting-cold-start-interview

contract-drafting eklentisini ilk kez kuran kullanıcı için kısa röportaj — rol, birincil ortam (model.ai Projects / masaüstü uygulaması), varsayılan çıktı formu (redline görünümü / temiz+liste / tablo), standart klozlar/şablonlar, onay zinciri. PROFIL.md profilini doldurur. `--redo` ile yeniden çalışır.

# contract-drafting — Cold Start Interview

Amaç: `PROFIL.md` profilindeki `[DOLDUR]` alanlarını 5-7 soruda doldurmak. Önce `firm-profile.md` + `skills/arthurlegal/references/redline-konvansiyonlari-rehberi.md` okunur.

## Akış

### Adım 0 — Bağlam
`firm-profile.md` + bu plugin `PROFIL.md` oku. Dolu alanları tekrar sorma.

### Adım 1 — Kullanıcı & ortam
> 1. Adın/rolün? ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri] / diğer)
> 2. Birincil ortam: **model.ai Projects** (markdown redline) mı, **masaüstü uygulaması/VS Code** (gerçek .docx tracked-changes) mı? — çıktı yeteneğini belirler.

### Adım 2 — Çıktı tercihi
> 3. Varsayılan redline formu: (a) redline görünümü, (b) temiz revize + değişiklik/comment listesi, (c) yapılandırılmış tablo, (d) her seferinde sor.
> 4. Comment'lerde fallback pozisyon her zaman yer alsın mı? (önerilen: evet)

### Adım 3 — Şablon & onay
> 5. Sık kullandığın şablon/emsal türleri? (EPC, PPA/elektrik satış, vendor/tedarik, NDA, kredi/finansman, hissedar/JV, süre uzatım protokolü)
> 6. Standart klozlar (mücbir sebep, sınırlı sorumluluk, yaptırım/uyum, uyuşmazlık, EPDK devir, KVKK) varsayılan eklensin mi?
> 7. İmza öncesi onay eşiği? (varsayılan: Baş Hukuk Müşaviri; yüksek tutar/stratejik + Genel Müdür)

### Adım 4 — Yaz ve onayla
Cevapları `PROFIL.md` `[DOLDUR]` alanlarına işle (özet göster, onay al, yaz). Matter workspace açık mı? Varsayılan: açık.

## Çıktı
Kısa özet + güncellenen alanlar + "Artık ``contract-drafting-redline-contract` iş akışı (`sozlesme` becerisi, `references/contract-drafting-redline-contract.md`)`, `:belge-turet`, `:versiyon-karsilastir`, `:tadil-protokol` kullanabilirsin." yönlendirmesi.

## Not
`--redo`: tüm alanları yeniden sor.

---

## Kaynak katmanı — /legal-research

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
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | ``legal-research-sozlesme-emsali` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-sozlesme-emsali.md`)` |
| AZ hukuku secilmisse emredici hukum kontrolu — akt + statu | ``legal-research-az-mevzuat` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-az-mevzuat.md`)` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil) — okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `skills/arthurlegal/references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `skills/arthurlegal/references/eqanun-mcp-rehberi.md` · `skills/arthurlegal/references/lex-scholar-rehberi.md` · `skills/arthurlegal/references/resourcecontracts-rehberi.md` · `skills/arthurlegal/references/karsilastirmali-hukuk-rehberi.md` · `skills/arthurlegal/references/nl-rechtspraak-mcp-rehberi.md` · `skills/arthurlegal/references/pl-sejm-mcp-rehberi.md` · `skills/arthurlegal/references/at-ris-mcp-rehberi.md` · `skills/arthurlegal/references/ie-statutebook-mcp-rehberi.md` · `skills/arthurlegal/references/fi-finlex-mcp-rehberi.md` · `skills/arthurlegal/references/es-boe-mcp-rehberi.md`
