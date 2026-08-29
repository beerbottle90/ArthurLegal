# İspanya Hukuku — Kullanım Rehberi (BOE açık veri yöntemi)

> **Erişim tipi:** WebFetch (GET) — auth yok
> **Durum:** ✅ Belge XML'i ve günlük fihrist WebFetch ile çalışıyor ·
> ⚠️ Konsolide mevzuat API'si **`Accept` başlığı ister** → WebFetch ile erişilemez
> **Test:** 30.08.2026
> **[ŞİRKET ADI] bağlamı:** ES, Avrupa'nın en büyük **LNG yeniden gazlaştırma**
> kapasitesine sahip ülkesi (Enagás terminalleri); LNG kargo satışı, terminal erişimi
> ve Naturgy/Repsol karşı tarafları ES hukukuna dokunur.

---

## Kaynak haritası

| Kaynak | İçerik | WebFetch | Not |
|---|---|---|---|
| **`boe.es/diario_boe/xml.php?id=`** | Tek belgenin **yapılandırılmış XML'i** | ✅ 200 | **BİRİNCİL** |
| **`datosabiertos/api/boe/sumario/{YYYYMMDD}`** | Günlük BOE fihristi | ✅ 200 | Yeni düzenleme takibi |
| `datosabiertos/api/legislacion-consolidada/id/{ID}` | **Konsolide** kanun | ⚠️ **başlık gerekir** | Aşağıya bak |
| EUR-Lex CELLAR | AB-türevli ES mevzuatı (SPA) | ✅ | `eurlex-cellar-rehberi.md` |
| CENDOJ (poderjudicial.es) | İçtihat | manuel | |

---

## 1. Tek belge — `xml.php` (BİRİNCİL ✅)

```
GET https://www.boe.es/diario_boe/xml.php?id={BOE-ID}
```
Doğrulandı: `?id=BOE-A-2010-1792` → temiz XML ✅

Dönen yapı:
```xml
<documento fecha_actualizacion="...">
  <metadatos>
    <identificador>BOE-A-2010-1792</identificador>
    <departamento codigo="...">Ministerio de ...</departamento>
    <rango codigo="...">Resolución</rango>
    <fecha_disposicion>...</fecha_disposicion>
  </metadatos>
  <texto>...</texto>
</documento>
```

**BOE-ID formatı:** `BOE-A-{yıl}-{sıra}` (A = disposición) · `BOE-B-...` (ilanlar)

---

## 2. Konsolide mevzuat API'si — ⚠️ WebFetch ile ERİŞİLEMEZ

```
GET https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{BOE-ID}
Accept: application/xml          ← ZORUNLU
```

30.08.2026 test sonuçları:

| İstek | Sonuç |
|---|---|
| `Accept: application/xml` + `BOE-A-2010-10544` | ✅ **200** (Ley de Sociedades de Capital) |
| `Accept: application/xml` + `BOE-A-1889-4763` | ✅ 200 (Código Civil) |
| `Accept: application/xml` + `BOE-A-2015-10565` | ✅ 200 |
| `Accept: application/json` | ❌ 400 — *"No soportado ningún mime type"* |
| `Accept: */*` veya başlıksız | ❌ 400 |

> 🔴 **WebFetch özel başlık gönderemez** → bu endpoint bu ortamdan kullanılamaz.
> **Konsolide ES metni için:**
> 1. `xml.php` ile **yayımlandığı hâli** al + `(konsolide değil)` kaydını düş; ya da
> 2. AB-türevli konuysa **EUR-Lex CELLAR** `lang:SPA` ile al (konsolide AB metni); ya da
> 3. Kullanıcıdan metni iste.
>
> 🔧 Kendi egress'i olan bir MCP sunucusu bu başlığı gönderebilir — ES konsolide
> mevzuatı **MCP ile tamamen çözülebilir bir eksiktir** (bkz. `MCP-ROADMAP.md`).

**Bilinen konsolide ID'ler (doğrulandı):**

| Metin | BOE-ID |
|---|---|
| Ley de Sociedades de Capital | `BOE-A-2010-10544` |
| Código Civil | `BOE-A-1889-4763` |

---

## 3. Günlük takip — `sumario`

```
GET https://www.boe.es/datosabiertos/api/boe/sumario/{YYYYMMDD}
```
Doğrulandı: `/20260828` → `<status><code>200</code></status>` + `<sumario>` ✅
(başlıksız da çalışır)

> 💡 ES enerji düzenlemesini izlemek için haftalık `sumario` taraması,
> `reg-change-monitor` agent'ına eklenebilecek düşük maliyetli bir kaynaktır.

---

## 4. [ŞİRKET ADI] için kritik ES mevzuatı

| Konu | Metin | Bağlantı |
|---|---|---|
| Hidrokarbonlar | Ley 34/1998 del sector de hidrocarburos | **LNG terminal erişimi**, tedarik |
| Elektrik | Ley 24/2013 del Sector Eléctrico | Şebeke, üretim |
| Şirketler | Ley de Sociedades de Capital (`BOE-A-2010-10544`) | S.A./S.L., JV |
| Borçlar | Código Civil (`BOE-A-1889-4763`) | Sözleşme, force majeure |
| Rekabet | Ley 15/2007 | CNMC birleşme bildirimi |

---

## Atıf formatı

```
[ES Mevzuat — {metin adı} — {BOE-ID} — GG.AA.YYYY]
```
`xml.php` yolundan alındıysa: `(BOE'de yayımlandığı hâli — konsolidasyon doğrulanmadı)`.

---

*Test: 30.08.2026 — `xml.php?id=BOE-A-2010-1792` ✅ · `sumario/20260828` ✅ ·
`legislacion-consolidada` `Accept: application/xml` ile 200 ✅ ama başlıksız/json 400 ❌
(WebFetch ile erişilemez, MCP gerekiyor). Sürüm: v1.6.0 (yeni).*
