# Lüksemburg Hukuku — Kullanım Rehberi (Legilux ELI yöntemi)

> **Erişim tipi:** WebFetch (GET) — auth yok
> **Durum:** ✅ ELI URL'leri + **konsolide sürümler** çalışıyor · ⚠️ makine-okunur arama API'si yok
> **Test:** 30.08.2026
> **[Müvekkil] bağlamı:** LU, Hollanda ile birlikte enerji grubu yapılarının iki ana
> holding yargı çevresinden biri — SOPARFI rejimi, fon yapıları, grup içi finansman.
> Hollanda rehberiyle (`hollanda-hukuku-rehberi.md`) **birlikte okunur**.

---

## Kaynak haritası

| Kaynak | İçerik | Durum (30.08.2026) |
|---|---|---|
| **legilux.public.lu ELI** | Resmî mevzuat, JO + **konsolide** | ✅ 200 |
| legilux.public.lu/search | Web araması (sunucu-render) | ✅ 200 |
| data.legilux.public.lu/sparql | ⚠️ SPARQL **UI'si** (Casemates SPA) — ham GET sorgusu HTML döner | ⚠️ kullanma |
| data.legilux.public.lu/api/v1 | ❌ 401 — auth gerekiyor, pakette anahtar yok | ❌ |
| EUR-Lex CELLAR | AB-türevli LU mevzuatı, FRA dilinde | ✅ |

---

## 1. ELI URL deseni — BİRİNCİL ✅

Lüksemburg **tam ELI uyumludur**; kimliği bilinen bir metne doğrudan inilir.

```
# Resmî Gazete'de yayımlandığı hâli
https://legilux.public.lu/eli/etat/leg/{tür}/{yyyy}/{mm}/{gg}/{no}/jo

# Konsolide (yürürlükteki) hâli — TARİHLİ
https://legilux.public.lu/eli/etat/leg/{tür}/{yyyy}/{mm}/{gg}/{no}/consolide/{YYYYMMDD}
```

**Doğrulanmış (30.08.2026):**
- `.../loi/1915/08/10/n1/jo` → 1915 tarihli **ticaret şirketleri kanunu** ✅ 200
- `.../loi/1915/08/10/n1/consolide/20230101` → konsolide sürüm ✅ 200

`{tür}`: `loi` (kanun) · `rgd` (büyük dük kararnamesi) · `agd` · `regl`

> ✅ **Konsolide URL'nin tarih taşıması LU'nun güçlü yanıdır** — hangi tarihli metne
> baktığın URL'de yazılıdır, atıfta bunu belirt.

---

## 2. Arama

Makine-okunur arama API'si **yok**. Sıralama:

1. `https://legilux.public.lu/search?query={terim}` ✅ 200 — sunucu-render, WebFetch okur.
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

*Test: 30.08.2026 — ELI `jo` ✅ · ELI `consolide/20230101` ✅ · `/search` ✅ ·
`data.legilux .../api/v1` 401 ❌ · `/sparql` SPA ⚠️. Sürüm: v1.6.0 (yeni).*
