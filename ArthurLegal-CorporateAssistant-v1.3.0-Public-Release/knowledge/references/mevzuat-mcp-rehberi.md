# Mevzuat MCP – Kullanım Rehberi

> ⚠️ **GÜNCELLEME (21.05.2026 — v1.5.0): Birleşik MCP**
> Mevzuat MCP ve Yargı MCP tek birleşik sunucuda birleşti — **yargi-mcp-pro**.
> Yeni endpoint: `https://yargi-mcp-pro-production.up.railway.app/mcp` · Auth: OAuth 2.0 (WorkOS).
> claude.ai'da TEK custom connector olarak eklenir (Customize → Connectors → Add custom connector).
> Eski ayrı connector'lar ve no-auth endpoint'ler (`mevzuat.surucu.dev`, `yargimcp.surucu.dev`) bırakılır.
> Araç isimleri/parametreleri (v1.4.2'de doğrulanmış) geçerliliğini korur — yalnızca tek connector altında toplanmıştır.


> Mevzuat MCP, Türk mevzuatına Claude'dan doğrudan erişim sağlar. Tüm skill'ler atıfları teyit ederken bu MCP'yi kullanmalıdır.

## İki kaynak — hangisini kullan?

### mevzuat.gov.tr (Playwright — yavaş ama tam içerik)
**21 araç**, 9 mevzuat tipi için search + search_within çiftleri.

Tipleri:
- Kanun (`search_kanun`, `search_within_kanun`)
- KHK
- Tüzük
- Kurum Yönetmeliği
- Tebliğ
- CB Kararnamesi (`search_cbk`)
- CB Kararı (`search_cbbaskankarar`)
- CB Yönetmeliği
- CB Genelgesi

**Önemli:** Anahtar kelime tabanlıdır, kanun numarasıyla aramada zayıftır.
- ✓ "katma değer vergisi"
- ✗ "3065"

### bedesten.adalet.gov.tr (REST — hızlı, kanun no destekli)
**5 araç**, 12 mevzuat tipini tek arayüzde.

Tipleri:
- `search_mevzuat(mevzuat_no="6098", mevzuat_turu="KANUN")` — birleşik arama
- `get_mevzuat_content(...)` — tam metin
- `search_within_mevzuat(...)` — madde içi kelime
- `get_mevzuat_gerekce(...)` — gerekçe (KANUN için)
- `get_mevzuat_madde_tree(...)` — madde ağacı/içindekiler

**Solr operatörleri destekli:**
- `"tam ifade"` — exact phrase
- `+gerekli +ikinci` — AND (boşlukla AND **DEĞİL**; + kullan)
- `-istenmeyen` — NOT
- `joker*` — wildcard
- `yakın~3` — fuzzy
- `"iki kelime"~5` — proximity (5 kelime içinde)

## Tipik patternler

### 1. Kanun maddesi tam metin getir
```
search_mevzuat(mevzuat_no="6098", mevzuat_turu="KANUN")
→ get_mevzuat_content(mevzuat_id=<id>)
→ search_within_mevzuat(mevzuat_id=<id>, query="+sorumluluğun +sınırlandırılması")
```

### 2. Kanun maddesi ağacını gör (içindekiler tablosu)
```
get_mevzuat_madde_tree(mevzuat_id=<id>)
→ M.115 ve civarını oku
```

### 3. Konu bazlı arama (kanun no bilinmiyor)
```
search_mevzuat(query="kişisel veri yurt dışı aktarım", mevzuat_turu="KANUN")
veya
search_mevzuat(query="+kişisel +veri +aktarım")
```

### 4. KVKK Kurul kararı / tebliğ ara
```
search_teblig(query="veri ihlal bildirim")
search_kurum_yonetmelik(kurum="Kişisel Verileri")
```

### 5. Yeni regülasyon takibi (CB Kararnamesi)
```
search_cbk(query="sermaye hareketleri")
search_cbgenelge(query="kamu alımları")
```

### 6. Kanun gerekçe sorgusu (madde mantığı)
```
get_mevzuat_gerekce(mevzuat_id=<6698 KVKK id>)
→ KVKK gerekçesi için 2016 Adalet Komisyonu raporu
```

## Atıf etiketleri

Mevzuat MCP'den alınan her atıf **mutlaka** şu etiketlerden biriyle gelmeli:

- `[Mevzuat MCP — GG.AA.YYYY]` — bedesten veya mevzuat.gov.tr'den o oturumda çekildi
- `[Mevzuat MCP — gerekçe]` — gerekçe metni  
- `[model bilgisi — doğrulayın]` — MCP'den çekilmediyse

**Asla:** MCP'den çekildiğini iddia eden ama gerçekte sadece model bilgisi olan atıflar verme.

## Sınırlamalar

- **Yargıtay/Danıştay/AYM kararları** Mevzuat MCP'de YOK — **bunlar için Yarg MCP kullanın** (bkz. `yargi-mcp-rehberi.md`). İkisi tamamlayıcıdır.
- **Kurum kararları (BDDK, SPK, EPDK, KVKK Kurulu) zaman zaman Mevzuat MCP'de eksik** — KVKK Kurulu + BDDK için Yarg MCP daha güçlü; SPK için kurum sitesine + KAP'a fallback; EPDK için kurum sitesi.
- **Tasarı/Kanun teklifi** aşamasındaki düzenlemeler MCP'de yok — TBMM sitesi
- **Yerel idari düzenleme** (belediye yönetmelikleri) MCP'de kapsamı sınırlı

---

## Mevzuat MCP + Yarg MCP — birlikte kullan

Türk hukuk araştırmasında iki MCP **tamamlayıcı**:

| MCP | Verdiği |
|---|---|
| **Mevzuat MCP** | Kanun, KHK, tüzük, yönetmelik, CB kararname/genelge, tebliğ — **norm metinleri** |
| **TR Legal MCP** | Yargıtay, Danıştay, AYM, KVKK Kurulu, Rekabet, KİK, BDDK, GİB, Sayıştay, Sigorta Tahkim, alt mahkemeler — **kararlar/yorumlar** |

Bir hukuki sorgu çoğunlukla ikisini birlikte gerektirir:
1. **Mevzuat MCP**'den ilgili madde + tüm fıkraları getir
2. **TR Legal MCP**'den o maddenin yargı/idari yorumunu getir
3. Sentezle ve atıf etiketlerini koru

Detay: bkz. `yargi-mcp-rehberi.md`
