# Hollanda Hukuku — Kullanım Rehberi (açık API yöntemi)

> ✅ **Bu yargı çevresi için artık custom MCP server VAR (v1.6.0):**
> **`nl-rechtspraak MCP`** → `references/nl-rechtspraak-mcp-rehberi.md`. **Önce onu kullan** —
> arama, atıf sözleşmesi ve statü disiplini orada hazırdır.
>
> Bu dosya **WebFetch yedeğidir**: connector bağlı değilse kullanılır.
> Yedek yol daha dar ve kırılgandır — buradan üretilen atıfa
> **`(MCP kullanılmadı)`** kaydını düş.

> **Erişim tipi:** WebFetch (GET) — auth yok, API anahtarı yok
> **Durum:** ✅ Mevzuat **tam metin aranabilir** · ✅ İçtihat **3,75 milyon ECLI** erişilebilir
> **Test:** 30.08.2026 — tüm endpoint'ler canlı doğrulandı
> **[ŞİRKET ADI] bağlamı:** NL, TR/AZ enerji yapılarının **varsayılan holding yargı çevresi**
> (B.V./N.V., katılım istisnası, vergi anlaşması ağı). Hisse devri, JV kurulumu,
> temettü akışı ve grup içi finansman NL hukukuna dokunur.

---

## Kaynak haritası

| Kaynak | İçerik | Arama tipi | Durum (30.08.2026) |
|---|---|---|---|
| **KOOP SRU** (`repository.overheid.nl/sru`) | Mevzuat + resmî yayınlar | ✅ **tam metin** (CQL) | ✅ 200 |
| **Rechtspraak Open Data** (`data.rechtspraak.nl`) | 3.751.381 ECLI karar | ⚠️ **yalnız yapılandırılmış filtre** | ✅ 200 |
| `wetten.overheid.nl/{BWB-ID}` | Konsolide kanun metni | doğrudan URL | ✅ 200 |
| EUR-Lex CELLAR | AB-türevli NL mevzuatı, NLD dilinde | SPARQL | ✅ (`eurlex-cellar-rehberi.md`) |

---

## 1. Mevzuat araması — KOOP SRU (BİRİNCİL ✅)

**SRU 2.0 protokolü, CQL sorgu dili, auth yok.**

```
GET https://repository.overheid.nl/sru
      ?operation=searchRetrieve
      &version=2.0
      &query=cql.textAndIndexes={ARAMA}
      &maximumRecords=20
```

**Canlı doğrulama (30.08.2026):**
- `query=cql.textAndIndexes=energiewet` → `<sru:numberOfRecords>1961`
- `query=cql.textAndIndexes=mededinging` → `<sru:numberOfRecords>20991`

Farklı sonuç sayıları döndüğü için **arama gerçekten çalışıyor** (parametre sessizce
yok sayılmıyor). Yanıt SRU/Dublin Core XML'idir; her kayıt `dcterms:identifier`
ile `wetten.overheid.nl` BWB kimliğini taşır.

```
WebFetch:
  URL: https://repository.overheid.nl/sru?operation=searchRetrieve&version=2.0&query=cql.textAndIndexes=warmtewet&maximumRecords=10
  prompt: "Bulunan mevzuat kayıtlarını başlık + BWB kimliği + yayın tarihi olarak listele"
```

### Konsolide metne inme

```
GET https://wetten.overheid.nl/{BWB-ID}
örnek: https://wetten.overheid.nl/BWBR0005291    ✅ 200
```

---

## 2. İçtihat — Rechtspraak Open Data

### ⚠️ ÖNCE BUNU OKU: serbest metin araması YOK

Açık API'nin `zoeken` endpoint'i **anahtar kelime aramasını desteklemez** ve
**tanınmayan parametreleri sessizce yok sayar** — bu, kolayca fark edilmeyen bir tuzaktır.

30.08.2026 doğrulaması (hepsi filtresiz toplamı döndürdü = parametre yok sayıldı):

| Denenen | Sonuç |
|---|---|
| `?max=1` (baseline) | 3.751.381 |
| `?keyword=energie` | 3.751.381 ❌ |
| `?q=energie` | 3.751.381 ❌ |
| `?text=energie` | 3.751.381 ❌ |
| `?subject=...#bestuursrecht` | 1.562.145 ✅ (gerçek filtre) |

> 🔴 **Kural:** `keyword`/`q`/`text` yazıp dönen sonucu "arama sonucu" sanma.
> Sayı filtresizle aynıysa **filtre uygulanmamıştır**. Her zaman baseline ile karşılaştır.

### Çalışan parametreler

```
GET https://data.rechtspraak.nl/uitspraken/zoeken
      ?max=20                 # sayfa boyutu
      &from=0                 # offset
      &type=Uitspraak         # Uitspraak | Conclusie
      &date=2025-01-15        # tek tarih; iki kez yazılırsa aralık
      &subject={rechtsgebied URI}
      &creator={instantie}
      &return=DOC             # META (varsayılan) | DOC
```
Doğrulandı: `?max=2&type=Uitspraak&date=2025-01-15` → 867 karar ✅

### Tek kararın tam metni

```
GET https://data.rechtspraak.nl/uitspraken/content?id={ECLI}
örnek: https://data.rechtspraak.nl/uitspraken/content?id=ECLI:NL:HR:2024:1   ✅
```
RDF + Akoma-Ntoso benzeri XML döner; `dcterms:` alanları atıf için hazırdır.

### Kontrollü sözlükler (filtre değerleri buradan)

```
https://data.rechtspraak.nl/Waardelijst/Rechtsgebieden   ✅ 200
https://data.rechtspraak.nl/Waardelijst/Instanties       ✅ 200
```
Örnek: `http://psi.rechtspraak.nl/rechtsgebied#bestuursrecht`

### Anahtar kelimeyle NL kararı bulmak gerekiyorsa

Açık API veremez. Sıralama:
1. **Konu + tarih + merci** ile daralt (`subject` + `creator` + `date`), sonra
   `content` ile tek tek oku — dar bir sorgu için uygulanabilir.
2. **LexScholar MCP** — NL doktrini kararlara atıf verir; ECLI'yi oradan yakala,
   sonra `content` ile tam metni çek.
3. **Kullanıcıdan ECLI iste.**
4. ⚠️ `uitspraken.rechtspraak.nl/api/zoek` **kullanma** — POST isteği bir duyuru
   sayfasına yönlendiriyor (30.08.2026), kullanılabilir değil.

> 🔧 **MCP fırsatı:** NL içtihadında serbest metin/semantik arama eksikliği,
> kendi indeksini kuran bir `nl-rechtspraak-mcp` için **en güçlü gerekçedir**.
> Bkz. `MCP-ROADMAP.md`.

---

## 3. [ŞİRKET ADI] için kritik NL mevzuatı

| Konu | Kanun | Bağlantı |
|---|---|---|
| Şirketler hukuku (B.V./N.V.) | Burgerlijk Wetboek Boek 2 | Holding kurulumu, yönetim sorumluluğu |
| Sözleşme/borçlar | BW Boek 6 | Grup içi sözleşmeler, tazminat |
| Enerji piyasası | Energiewet (2024 reformu) | Şebeke erişimi, tedarik lisansı |
| Isı tedariki | Warmtewet | Bölgesel ısıtma yatırımları |
| Rekabet | Mededingingswet | ACM soruşturmaları |
| Kurumlar vergisi | Wet Vpb 1969 — **deelnemingsvrijstelling** | Katılım istisnası: temettü/sermaye kazancı |
| İş hukuku | BW Boek 7 titel 10 | Yönetici sözleşmeleri, rekabet yasağı |

---

## Atıf formatı

```
[NL Mevzuat — {kanun adı} art. {madde} — wetten.overheid.nl/{BWB-ID} — GG.AA.YYYY]
[NL İçtihat — {ECLI} — {merci} — {tarih}]
```
⚠️ **ECLI'yi asla elle kurma** — `zoeken`/`content` çıktısındaki `<id>` alanından
birebir kopyala. "Muhtemelen ECLI:NL:HR:2024:..." tarzı tahmin **yasaktır**.

⚠️ Konsolide sürüm tarihi doğrulanamadıysa atıfa `(konsolidasyon doğrulanmadı)` düş.

---

*Test: 30.08.2026 — KOOP SRU tam metin ✅ (1961/20991 ayrışması doğrulandı) ·
rechtspraak `zoeken` 3.751.381 ECLI ✅ · `content?id=ECLI:NL:HR:2024:1` ✅ ·
Waardelijst Rechtsgebieden/Instanties ✅ · wetten.overheid.nl/BWBR0005291 ✅.
Serbest metin aramasının bulunmadığı ve tanınmayan parametrelerin sessizce yok
sayıldığı tespit edildi. Sürüm: v1.6.0 (yeni).*
