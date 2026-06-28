# Yarg MCP – Kullanım Rehberi

> ⚠️ **GÜNCELLEME (21.05.2026 — v1.5.0): Birleşik MCP**
> Mevzuat MCP ve Yargı MCP tek birleşik sunucuda birleşti — **yargi-mcp-pro**.
> Yeni endpoint: `https://yargi-mcp-pro-production.up.railway.app/mcp` · Auth: OAuth 2.0 (WorkOS).
> claude.ai'da TEK custom connector olarak eklenir (Customize → Connectors → Add custom connector).
> Eski ayrı connector'lar ve no-auth endpoint'ler (`mevzuat.surucu.dev`, `yargimcp.surucu.dev`) bırakılır.
> Araç isimleri/parametreleri (v1.4.2'de doğrulanmış) geçerliliğini korur — yalnızca tek connector altında toplanmıştır.


> **Yarg MCP**, saidsurucu/yargi-mcp projesi tarafından sağlanan ücretsiz Türk yargı/idari kararlar erişim katmanıdır. Mevzuat MCP **kanun metinlerini** verir; Yarg MCP **kararları, içtihatları, görüşleri** verir. İkisi birlikte Türk hukuk asistanı için tam paket.

**Endpoint:** `https://yargi-mcp-pro-production.up.railway.app/mcp` (birleşik)
**Versiyon:** v0.2.0+ (semantic search desteği)
**Auth:** API anahtarı gerekmez (remote endpoint)
**Lisans:** MIT
**Repo:** https://github.com/saidsurucu/yargi-mcp

---

## Kapsam — 15 yargı/idari kurum, 24 araç

### Yüksek Mahkemeler

| Kurum | Kapsam | Filtre |
|---|---|---|
| **Yargıtay** | Karar arama (çift API: ana + Bedesten) | 52 daire/hukuk-ceza-CGK |
| **Danıştay** | Karar arama (üç API: keyword + ana + Bedesten) | 27 daire/IDDK/VDDK |
| **Anayasa Mahkemesi** | Norm denetimi + bireysel başvuru kararları | Konu, başvuran |

### Alt Mahkemeler ve Özel Yargı (Bedesten birleşik API)

- **İstinaf Mahkemeleri (BAM)** — hukuk + ceza istinaf
- **Yerel Mahkemeler** — hukuk + ceza yerel
- **Olağanüstü kanun yolları** — Karar Düzeltme, Yargılamanın Yenilenmesi
- **Uyuşmazlık Mahkemesi** — yargı yolu uyuşmazlıkları
- **Emsal (UYAP)** — emsal kararlar arşivi

### İdari Kurum Kararları

| Kurum | Kapsam |
|---|---|
| **KİK (Kamu İhale Kurumu)** | İtirazen şikayet kararları |
| **Rekabet Kurumu** | Kurul kararları (birleşme, ihlal, görüş) |
| **Sayıştay** | Daire kararları + Genel Kurul + Temyiz |
| **KVKK Kurulu** | Veri ihlali + ilkesel kararlar |
| **BDDK** | Bankacılık kararları |
| **GİB (Gelir İdaresi)** | 18.000+ özelge (mukteza) |
| **Sigorta Tahkim Komisyonu** | Tahkim kararları |

---

## [Müvekkil] için ne işe yarar?

| Konu | Yarg MCP'den çekilebilen |
|---|---|
| **İş davası içtihatı** | Yargıtay 9. ve 22. Hukuk Dairesi kararları — işe iade, kıdem, fazla mesai |
| **Çevre & ISG ölümlü kaza** | Yargıtay 4. ve 12. Hukuk Dairesi + Ceza Genel Kurulu + 6331 davalarına ait kararlar |
| **Petkim SPK davaları** | Danıştay 13. ve 10. Daire kararları (SPK düzenlemelerine itiraz) |
| **EPDK lisans iptali davası** | Danıştay 13. Daire — enerji idari yargı |
| **Rekabet Kurulu ihlal kararı + Danıştay temyizi** | Hem Rekabet Kurumu (orijinal) hem Danıştay (yargı incelemesi) |
| **KVKK ihlal kararı** | KVKK Kurulu — emsal idari para cezaları |
| **GİB transfer pricing özelge** | Vergi konularında [Ana ortak / ilişkili taraf] işlemleri için |
| **KİK ihale itirazı** | Devlet ihalelerinde teklif/iptal davaları |

---

## Tipik kullanım pattern'ları

### 1. Yargıtay içtihatı ara (iş davası örneği)

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="9. Hukuk Dairesi",
  arananKelime="işe iade kıdem tazminatı",
  baslangicTarihi="2023-01-01",
  bitisTarihi="2024-12-31"
)
```

Çıktı: ESAS/KARAR no + tarih + özet. İlgili karara `get_yargitay_decision_text` ile tam metin.

### 2. AYM bireysel başvuru ara

```
mcp__claude_ai_Yarg_MCP__search_anayasa_unified(
  arananKelime="özel hayatın gizliliği KVKK",
  yil="2024"
)
```

KVKK uygulaması + AYM denetimi birleşik.

### 3. KVKK Kurulu kararı + Yargıtay temyizi

```
# KVKK Kurul'un orijinal kararı
search_kvkk_decisions(arananKelime="veri ihlali bildirim 72 saat")

# Sonra Danıştay'da temyiz var mı diye kontrol
search_danistay_decisions(daire="10. Daire", arananKelime="KVKK ihlal idari para cezası")
```

### 4. Rekabet Kurulu enerji kararları

```
search_rekabet_decisions(
  arananKelime="petrol piyasası dikey entegrasyon",
  baslangicTarihi="2020-01-01"
)
```

Aliağa ÖEB / [Müvekkil] dikey yapısı emsali.

### 5. GİB özelge — transfer pricing

```
search_gib_decisions(
  arananKelime="ilişkili taraf transfer fiyatlandırması ham petrol"
)
```

[Ana ortak / ilişkili taraf] → STAR Rafineri ham petrol alım fiyat denetimi için.

### 6. KİK kararları — devlet ihale itirazı

```
search_kik_decisions(arananKelime="elektrik üretim ihalesi")
```

İÇAN gibi enerji ihaleleri.

---

## Atıf etiketleri

Yarg MCP'den alınan her atıf **mutlaka** etiketli olmalı:

- `[Yarg MCP — yargitay — GG.AA.YYYY]` — Yargıtay kararı, o oturumda çekildi
- `[Yarg MCP — danistay — GG.AA.YYYY]` — Danıştay kararı
- `[Yarg MCP — aym — GG.AA.YYYY]` — Anayasa Mahkemesi
- `[Yarg MCP — kvkk-kurulu — GG.AA.YYYY]` — KVKK Kurulu
- `[Yarg MCP — rekabet — GG.AA.YYYY]` — Rekabet Kurulu
- `[Yarg MCP — gib — GG.AA.YYYY]` — GİB özelge
- `[Yarg MCP — sayistay — GG.AA.YYYY]` — Sayıştay
- `[Yarg MCP — bddk — GG.AA.YYYY]` — BDDK
- `[Yarg MCP — kik — GG.AA.YYYY]` — KİK
- `[Yarg MCP — sigorta-tahkim — GG.AA.YYYY]` — Sigorta Tahkim
- `[Yarg MCP — bedesten — GG.AA.YYYY]` — Alt mahkeme (birleşik API)
- `[Yarg MCP — emsal — GG.AA.YYYY]` — UYAP emsal

**Asla:** Çekmediğin bir kararı MCP'den çekmiş gibi gösterme. Çekemiyorsan `[model bilgisi — doğrulayın]`.

---

## Mevzuat MCP + Yarg MCP birlikte kullanım — pratik

Tam tabloyu görmek için **iki MCP birlikte** çalışır:

```
SORU: "TBK m. 115 ağır kusur uygulaması Yargıtay nasıl yorumluyor?"

ADIM 1: Mevzuat MCP'den maddeyi getir
  search_kanun(mevzuat_adi="6098")
  → get_mevzuat_content(...)  # m. 115 tam metin

ADIM 2: Yarg MCP'den yargı yorumunu getir
  search_yargitay_decisions(
    arananKelime="TBK 115 ağır kusur sorumsuzluk şartı",
    daire="3. Hukuk Dairesi"
  )

ADIM 3: Sentezle — kanun metni + en az 3 emsal karar + güncel eğilim
```

---

## Sınırlamalar

- **Karar metinleri otomatik özet değil** — get_decision_text gerçek metni döndürür, uzun olabilir
- **Bazı kararlar gizli kısımları redacted** (özellikle KVKK/AYM bireysel başvurular)
- **Anlık karar yayını yok** — RG'de yayımlandıktan sonra MCP indeksine eklenir (1-7 gün gecikme)
- **Çok eski (1990 öncesi) kararlar eksik** olabilir
- **Karar metni yorumlama** modele kalır — MCP sadece metni getirir, içtihat ağırlığını/güncelliğini söylemez. Bu yorumu sen yapacaksın.
- **Bedesten birleşik API** alt mahkemelerin tamamını kapsamaz — bölgelere göre kapsama farklı

---

## [Müvekkil] Yarg MCP kullanım disiplini

1. **Petkim/EPDK/Rekabet kararları** araştırırken → Yarg MCP birinci kaynak
2. **İş hukuku davaları** (Aliağa kazaları, fesih, kıdem) → Yargıtay 9./22./4./12. HD
3. **Vergi/transfer pricing** → GİB özelge + Danıştay vergi daireleri
4. **KVKK ihlal değerlendirmesi** → KVKK Kurulu kararları (emsal idari para cezaları)
5. **İhaleye katılma + itiraz** → KİK
6. **Sigorta tazminat** → Sigorta Tahkim Komisyonu

Her bir araştırma — **kanun metni (Mevzuat MCP) + yargı/idari yorumu (Yarg MCP) + şirket politikası (CLAUDE.md profiller)** üçgeninde sentezlenmeli.
