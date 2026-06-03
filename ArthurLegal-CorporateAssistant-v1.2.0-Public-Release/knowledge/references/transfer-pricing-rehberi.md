# Transfer Pricing Rehberi — [ANA ORTAK] Intra-Group

> KVK m. 13 + OECD TPG. [ŞİRKET ADI]'nin ana ortağı [ŞİRKET ADI] (Bakü) ile yaptığı intra-group işlemler Maliye için en hassas alanlardan biri.

## Yasal çerçeve

### Türk hukuku
- **KVK m. 13 — Örtülü Kazanç Dağıtımı:**
  - İlişkili kişi (m. 12) tanımı geniş: ortak, ortağın eşi/akrabaları, ana ortak, hâkim ortak, yönetici, %25 üstü hisseli şirket, vd.
  - **Emsallere uygun fiyat ilkesi** (arm's length)
  - 5 yöntem (KKF, Maliyet Artı, Yeniden Satış, Kâr Bölüşümü, TNMM)
  - Yıllık TP dokümantasyon zorunlu

### Genel Tebliğ
- **Kurumlar Vergisi Genel Tebliği (1 Seri No)** — TP dokümantasyon kapsamı
- **Genel Tebliğ (6 Seri No)** — CbCR (Country-by-Country Reporting)

### OECD ve uluslararası
- **OECD Transfer Pricing Guidelines 2022** (güncel)
- **BEPS Action 8-10** — Intangibles, services, financial transactions
- **BEPS Action 13** — Master File + Local File + CbCR
- **Çifte Vergilendirmeyi Önleme Anlaşmaları** — Türkiye 80+ ülkeyle (Azerbaycan 1994)

## [ŞİRKET ADI]-özel TP haritası

### Ham petrol alımı ([ANA ORTAK] → [RAFİNERİ])
- **Yöntem önerisi:** KKF (Brent + Azeri Light premium)
- **Risk:** Maliye'nin "emsallerden sapma" iddiası — fiyat dalgalı dönemlerde
- **Dokümantasyon:** Sözleşme + S&P Platts/Argus benchmarks + günlük fiyat raporları

### Royalty / lisans / marka
- **[ŞİRKET ADI] brand royalty** — BEPS Action 8 (intangibles) hassas
- **Yöntem önerisi:** TNMM veya CUP (varsa)
- **Risk:** "Marka değeri makul mü" sorgulanır — Maliye agresif olabilir
- **Dokümantasyon:** Brand valuation raporu + emsal royalty oranları (RoyaltyStat)

### Yönetim hizmeti, IT, mali danışmanlık
- **Yöntem:** Maliyet Artı (cost plus 5-15% mark-up)
- **Risk:** Hizmet **fiili olarak yararlanıldı mı** ispat (BEPS Action 10 low value-adding services)
- **Dokümantasyon:** Hizmet sözleşmesi + time sheets + deliverable listesi + benefit testi

## Dokümantasyon paketi (yıllık)

### Master File (BEPS Action 13)
- Grup organizasyon yapısı
- İşletme faaliyetleri tanımı
- Intangibles (marka, patent, know-how)
- Intra-group finansman
- Mali ve vergi pozisyonu

→ Bu **[ŞİRKET ADI] (Bakü) ana şirket tarafından hazırlanır** (Azerbaycan'da merkezdir).

### Local File
- [ŞİRKET ADI] spesifik
- İlişkili işlemler envanteri
- Her işlem için yöntem + emsal analizi + fonksiyonel analiz
- Karşı taraf bilgileri

→ Türkiye'de [ŞİRKET ADI] + Büyük 4 firma birlikte hazırlar.

### CbCR (Country-by-Country Reporting)
- Konsolide grup ana şirket ([ANA ORTAK]) hazırlar
- Türkiye yetkilisi: GİB (Yetkili Otorite — Türkiye-Azerbaycan arası bilgi paylaşımı)

## Maliye saldırı vektörleri (TP incelemesinde)

1. **Fiyat sapması:** Aralık (interquartile range) dışında
2. **Yöntem yanlış seçimi:** TNMM yerine CUP, vs.
3. **Fonksiyonel analiz hatalı:** Risk/yararlanma tarafı yanlış tarafa yüklendi
4. **Hizmetin fiilen yapılmadığı:** Management services'de duplicating function
5. **İntangibles overcharged:** Marka değeri abartılı
6. **Loss-making entity:** [ŞİRKET ADI] sürekli zarar ediyorsa intra-group fiyat sorgulanır

## Savunma araçları

- **APA (Advanced Pricing Agreement)** — Maliye ile peşin fiyat anlaşması. Türkiye'de süreç yavaş ama uygun.
- **MAP (Mutual Agreement Procedure)** — Çifte vergilendirme yaşandıysa, Türkiye-Azerbaycan yetkili makamlar görüşmesi.
- **Cost contribution arrangements** — Ortak fayda projeleri için (R&D, IT)
- **Cost sharing agreement** — Maliyet bölüşüm

## TR Legal MCP — TP içtihatı

```
mcp__claude_ai_Yarg_MCP__search_gib_ozelge(
  arananKelime="transfer fiyatlandırma örtülü kazanç ham petrol"
)

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="4. Daire",
  arananKelime="KVK 13 transfer pricing emsal fiyat",
  baslangicTarihi="2022-01-01"
)
```

## Mevzuat MCP

```
search_mevzuat(mevzuat_no="5520", mevzuat_tur="KANUN")  # KVK
```

## Bağlantılı

- [VUK rehberi](vuk-rehberi.md)
- [GİB özelge rehberi](gib-ozelge-rehberi.md)
- [ŞİRKET ADI] profili → tax-legal (bu plugin)
