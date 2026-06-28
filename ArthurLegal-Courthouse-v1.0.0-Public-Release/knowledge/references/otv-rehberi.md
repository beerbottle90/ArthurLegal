# ÖTV (Özel Tüketim Vergisi) Rehberi

> 4760 sayılı Özel Tüketim Vergisi Kanunu. Vergi yargısında ÖTV tarhiyatı/iade uyuşmazlıklarının değerlendirilmesinde başvurulur.

## Kapsam (ÖTV listeleri)

ÖTV Kanunu'nda **4 sayılı liste** vardır:

- **(I) sayılı liste:** Petrol ürünleri, motor yağları, doğal gaz
- (II) sayılı: Motorlu taşıt
- (III) sayılı: Alkol, tütün
- (IV) sayılı: Lüks tüketim malları

## (I) Sayılı liste — Petrol ürünleri ÖTV

| Ürün | Tutar (yıllık güncellenir, 2026: değişken) |
|---|---|
| Benzin | TL/litre |
| Motorin | TL/litre |
| LPG | TL/kg |
| Fuel-oil | TL/kg |
| Jet yakıtı | TL/litre (istisnalar) |
| Doğal gaz | TL/m³ (sektöre göre değişken) |
| Petrokimya hammadde | İstisna durumlar |

**Maliye Bakanlığı Genel Tebliği** ile tutarlar yıllık güncellenir.

## İhracat istisnası (ÖTV m. 5)

İhraç edilen akaryakıt için **ÖTV mahsubu/iadesi:**

1. **Mahsuben iade:** Sonraki dönem ÖTV borcundan mahsup
2. **Nakden iade:** Daha uzun süreç, daha sıkı denetim

**Şartlar:**
- Fiziksel ihracat gerçekleşmeli (gümrük çıkış belgesi)
- Beyannamede ihracat istisnası belirtilmeli
- Ürün miktarı doğrulanmalı (tartım, hacim)
- İhracat 3 ay içinde tamamlanmalı (bazı istisnalar)

## Tipik akaryakıt akışı (ÖTV doğuşu)

```
Ham petrol alım →
Rafineriye giriş →
Üretim (benzin, motorin, jet yakıtı, vs.) →
İç piyasa satışı (ÖTV doğar) | İhracat (ÖTV istisnası)
                                ↓
                            Mahsuben/nakden iade
```

## İdarenin tipik iade red gerekçeleri (yargıda denetlenen)

- **Miktar uyumsuzluğu** — beyan ile fiili çelişki
- **Gümrük çıkış belgesi eksik/şüpheli**
- **Müşteri ihracatçı statüsü** kontrolü
- **İlişkili kişi satışı** (TP riski)
- **Antrepo / depo dökümanları** yetersiz

## EPDK paralel sorumluluk

5015 sayılı **Petrol Piyasası Kanunu**:
- Rafineri lisansı kapsamında üretim/satış
- EPDK lisans şartlarına uygunluk
- Aylık raporlama (üretim, satış, stok)
- **EPDK + GİB ortak denetim** yapabilir

## Dava prep (Danıştay 3. Daire)

ÖTV mahsubu reddedilirse:
- **İYUK m. 7 — 30 gün** Danıştay'a iptal davası
- **Danıştay 3. Daire** — KDV/ÖTV uzmanı
- **Yürütmenin durdurulması** talep et (bekletme zarara yol açıyorsa)

## Yarg MCP

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="3. Daire",
  arananKelime="ÖTV mahsup akaryakıt ihracat istisna rafineri",
  baslangicTarihi="2022-01-01"
)

mcp__claude_ai_Yarg_MCP__search_gib_ozelge(
  arananKelime="ÖTV mahsup rafineri"
)
```

## Mevzuat MCP

```
search_mevzuat(mevzuat_no="4760", mevzuat_tur="KANUN")  # ÖTV K.
search_mevzuat(mevzuat_no="5015", mevzuat_tur="KANUN")  # Petrol Piyasası K.
```

## Bağlantılı

- [VUK rehberi](vuk-rehberi.md)
- [GİB özelge rehberi](gib-ozelge-rehberi.md)
- [Vergi yargısı rehberi](vergi-yargisi-rehberi.md)
- [Mevzuat MCP rehberi](mevzuat-mcp-rehberi.md)
