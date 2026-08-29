# Lüksemburg Hukuku — Kullanım Rehberi (Legilux ELI yöntemi)

> 🔴 **DÜZELTME (30.08.2026, ikinci tur test):** İlk testte ELI URL'lerine **HTTP 200**
> geldiği için "çalışıyor" yazılmıştı. **Yanlıştı.** İçerik doğrulandığında her ELI
> URL'inin aynı **2.116 baytlık Angular kabuğunu** ("no-script-warning") döndürdüğü
> görüldü — `.../jo`, `.../jo/fr/pdf`, `.../consolide/20230101` hepsi aynı boş kabuk.
> **Legilux tamamen JavaScript ile render ediliyor; agent'a hiçbir hukuki metin vermiyor.**
>
> Denenen ve başarısız olan tüm yollar: `data.legilux.public.lu/api/v1` (401) ·
> `/sparql` (Angular SPA) · `sitemap.xml` (404) · `/oai` (404) · `data.legilux` ELI (400) ·
> `Accept: application/xml` ve `application/rdf+xml` içerik müzakeresi (yine 2.118 baytlık kabuk).
>
> **Sonuç: Lüksemburg şu an İsrail ve BAE ile aynı kategoridedir** — resmî kaynak
> agent'a kapalı, otomatik araştırma kapasitesi yok. Aşağıdaki ELI desenleri
> **tarayıcıda** geçerlidir ve **atıf kimliği** olarak kullanılabilir; metin çekmek için değil.

> **Erişim tipi:** ❌ WebFetch çalışmıyor (JS-render) · tarayıcı veya kullanıcı yapıştırması
> **Test:** 30.08.2026 (ikinci tur — içerik doğrulamalı)
> **[Müvekkil] bağlamı:** LU, Hollanda ile birlikte enerji grubu yapılarının iki ana
> holding yargı çevresinden biri — SOPARFI rejimi, fon yapıları, grup içi finansman.
> Hollanda rehberiyle (`hollanda-hukuku-rehberi.md`) **birlikte okunur**.

---

## Kaynak haritası

| Kaynak | İçerik | Durum (30.08.2026) |
|---|---|---|
| **legilux.public.lu ELI** | Resmî mevzuat, JO + konsolide | ❌ **boş SPA kabuğu** (2.116 B) — metin yok |
| legilux.public.lu/search | Web araması | ❌ **boş SPA kabuğu** (2.116 B) — sunucu-render DEĞİL |
| data.legilux.public.lu/sparql | ⚠️ SPARQL **UI'si** (Casemates SPA) — ham GET sorgusu HTML döner | ⚠️ kullanma |
| data.legilux.public.lu/api/v1 | ❌ 401 — auth gerekiyor, pakette anahtar yok | ❌ |
| EUR-Lex CELLAR | AB-türevli LU mevzuatı, FRA dilinde | ✅ |

---

## 1. ELI URL deseni — ⚠️ ATIF KİMLİĞİ olarak geçerli, METİN çekmez

Lüksemburg **tam ELI uyumludur**; kimliği bilinen bir metne doğrudan inilir.

```
# Resmî Gazete'de yayımlandığı hâli
https://legilux.public.lu/eli/etat/leg/{tür}/{yyyy}/{mm}/{gg}/{no}/jo

# Konsolide (yürürlükteki) hâli — TARİHLİ
https://legilux.public.lu/eli/etat/leg/{tür}/{yyyy}/{mm}/{gg}/{no}/consolide/{YYYYMMDD}
```

**İkinci tur doğrulama (30.08.2026) — içerik kontrollü:**
- `.../loi/1915/08/10/n1/jo` → 200 ama **2.116 B boş kabuk** ❌
- `.../loi/1915/08/10/n1/consolide/20230101` → 200 ama **2.499 B boş kabuk** ❌

> 📌 **Ders:** HTTP 200 "çalışıyor" demek değildir. Bir kaynağı birincil ilan etmeden
> önce **dönen içeriğin gerçekten hukuki metin olduğunu** doğrula. Bu rehberin ilk
> sürümü tam olarak bu hatayı yaptı.

`{tür}`: `loi` (kanun) · `rgd` (büyük dük kararnamesi) · `agd` · `regl`

> ✅ **Konsolide URL'nin tarih taşıması LU'nun güçlü yanıdır** — hangi tarihli metne
> baktığın URL'de yazılıdır, atıfta bunu belirt.

---

## 2. Arama

Ne arama API'si ne de okunabilir arama sayfası var. Sıralama:

1. ❌ `https://legilux.public.lu/search?query={terim}` — **kullanma**, boş kabuk döner.
2. **EUR-Lex CELLAR** (`lang:FRA`) — AB-türevli LU mevzuatı için
   (`eurlex-cellar-rehberi.md` bölüm "Örnek 3").
3. **LexScholar MCP** — LU/FR doktrini üzerinden mevzuata atıf yakala.
4. Kullanıcıdan ELI/kanun tarihi iste.

⚠️ `data.legilux.public.lu/api/v1/...` **401** döndürüyor — bu pakette kimlik bilgisi
yok, çağırma. `/sparql` yolu bir **arayüz** (Angular SPA); GET ile SPARQL sorgusu
gönderme, HTML alırsın.

---

## 3. [Müvekkil] için kritik LU mevzuatı

| Konu | Metin | Bağlantı |
|---|---|---|
| Ticaret şirketleri | Loi du 10 août 1915 (LSC) | S.A./S.à r.l., JV, hisse devri |
| SOPARFI / katılım | LIR art. 166 + RGD 21.12.2001 | Temettü & sermaye kazancı istisnası |
| Borçlar | Code civil (FR kökenli) | Sözleşme, force majeure |
| Finansal teminat | Loi du 5 août 2005 | Proje finansmanı teminat paketi |
| Menkul kıymetleştirme | Loi du 22 mars 2004 | Yapılandırılmış finansman |

---

## Atıf formatı

```
[LU Mevzuat — {metin adı} — ELI {eli_url} — konsolide {YYYYMMDD} — GG.AA.YYYY]
```
Konsolide değil JO sürümüne bakıldıysa `(JO sürümü — sonraki değişiklikler
kontrol edilmedi)` kaydını düş.

---

*Test: 30.08.2026 (ikinci tur, içerik doğrulamalı) — **tüm Legilux yolları boş
Angular kabuğu döndürüyor**: ELI `jo` (2.116 B), `consolide` (2.499 B), `/search`
(2.116 B), `Accept: application/xml|rdf+xml` (2.118 B). `data.legilux/api/v1` 401,
`/sparql` SPA, `sitemap.xml` ve `/oai` 404. **Otomatik erişim yolu yoktur.**
İlk sürümdeki "✅ çalışıyor" değerlendirmesi yalnızca HTTP durum koduna dayanıyordu
ve hatalıydı. `MCP-ROADMAP.md`'deki `eli-search-mcp` maddesinden LU çıkarıldı.
Sürüm: v1.6.0.*
