# EPDK (Enerji Piyasası Düzenleme Kurumu) Rehberi — [ŞİRKET ADI] Dialog Modeli

> [ŞİRKET ADI] için günlük operasyonel düzenleyici. [RAFİNERİ] (petrol piyasası), [HALKA AÇIK İŞTİRAK] (petrokimya), [ELEKTRİK SANTRALİ] (elektrik üretim), eski [DAĞITIM İŞTİRAK 1]/[DAĞITIM İŞTİRAK 2] (doğal gaz dağıtım) — hepsi EPDK lisans + tebliğ kapsamında.

## Hukuki çerçeve

| Kanun | Sektör |
|---|---|
| **5015 Petrol Piyasası Kanunu** | Rafineri, akaryakıt — STAR + [ŞİRKET ADI] Enerji Ticaret |
| **4646 Doğal Gaz Piyasası Kanunu** | Doğal gaz dağıtım (eski [DAĞITIM İŞTİRAK 1]/[DAĞITIM İŞTİRAK 2]) + iletim ([BORU HATTI PROJESİ]) + ticaret |
| **6446 Elektrik Piyasası Kanunu** | Elektrik üretim — **[ELEKTRİK SANTRALİ]** + [HALKA AÇIK İŞTİRAK] RES |
| **5346 Yenilenebilir Enerji Kaynakları K.** | RES, GES (rüzgar/güneş) |
| **4628 sayılı EPDK Kanunu** (kuruluş) | Kurumsal yapı |

## EPDK Kurul yapısı

- **Kurul:** 7 üye (Cumhurbaşkanı tarafından atanır), kararlar oyçoğunluğu
- **Daire Başkanlıkları:** Petrol, Doğal Gaz, Elektrik, Lisans, vd.
- **Kurul kararları:** Bireysel (lisans) veya genel (Tebliğ, Yönetmelik)

## Lisans tipleri ([ŞİRKET ADI] ilgili)

| Lisans | [ŞİRKET ADI]'da |
|---|---|
| Rafinaj | [RAFİNERİ] |
| Depolama | [ŞİRKET ADI] Depolama |
| Dağıtım (petrol) | [ŞİRKET ADI] Enerji Ticaret |
| Bayilik | (akaryakıt istasyonları varsa) |
| Doğal gaz dağıtım | Eski [DAĞITIM İŞTİRAK 1]/[DAĞITIM İŞTİRAK 2] (devir) |
| Doğal gaz toptan satış | [ŞİRKET ADI] Enerji Ticaret |
| **Elektrik üretim** | **[ELEKTRİK SANTRALİ]** (870 MW kombine çevrim, Şubat 2025) |
| Boru hattı (iletim) | [BORU HATTI PROJESİ] (özel rejim) |

## [ŞİRKET ADI] EPDK dialog modeli (proaktif)

1. **Günlük operasyon:** Lisans şartlarına uyum, periyodik raporlama (üretim, satış, stok)
2. **Yapısal dialog:** EPDK ile periyodik toplantı (sektör temsili), informal yazışma
3. **Tebliğ taslakları:** Kamuoyu istişaresi sürecinde **[ŞİRKET ADI] görüş sunumu** (Compliance + Hukuk)
4. **Belirsiz konularda:** Yorum talebi yazısı (informal)
5. **Sorunlu konularda:** Dava ÖNCESİ pozisyon sunma + diyalog
6. **Son çare:** Kurul kararına karşı dava (Ankara İdare Mah. → BİM → Danıştay 13. Daire)

`/administrative-legal:epdk-proaktif-gorus` skill — operasyonel araç.

## EPDK Kurul kararı tipleri

| Tip | İdari işlem niteliği | Dava yolu |
|---|---|---|
| Lisans verme/red/iptal | Bireysel | Ankara İdare Mah. ilk derece |
| İdari para cezası | Bireysel | Ankara İdare Mah. (`idari-para-cezasi-itiraz`) |
| Tarife düzenleme | Genel düzenleyici | Ankara İdare Mah. (etkilenen mükellef) veya Danıştay (normatif ise) |
| Tebliğ / Yönetmelik | Normatif düzenleyici | Doğrudan Danıştay |
| Lisans şartı yorumu | Bağlayıcı yorum | İlgili yol |

## EPDK ile çatışma senaryoları ([ŞİRKET ADI]'a özel)

### [RAFİNERİ]
- Üretim kapasitesi-lisans uyumu
- Çevre uyum (ÇED + EPDK ortak)
- Akaryakıt satış pazar payı (Rekabet ile ortak dikkat)

### [HALKA AÇIK İŞTİRAK]
- Petrokimya hammadde lisans
- Üretim duruşu bildirimleri
- Halka açık raporlama uyumu (SPK + KAP paralel)

### [ELEKTRİK SANTRALİ] (yeni — Şubat 2025)
- 6446 EPK kapsamında elektrik üretim lisansı
- Şubat 2025 devir sonrası **6 adım** EPDK süreci (lisans transferi)
- Detay: `references/socar-ican-elektrik-uretim-rehberi.md`

### Eski [DAĞITIM İŞTİRAK 1]/[DAĞITIM İŞTİRAK 2]
- Devir süreci tamamlandı/tamamlanıyor (2024-2026)
- VERBİS + lisans + müşteri bilgi geçişi paralel
- Yeni sahibe geçiş yükümlülükleri

## EPDK koordinasyon ([ŞİRKET ADI] Hukuk & Compliance)

- **Compliance Direktörü [UYUM DİREKTÖRÜ]** — EPDK ile genel ilişki sahibi
- **Regulatory Compliance Manager [REGULATORY COMPLIANCE MÜDÜRÜ]** — günlük EPDK dosyaları
- **Senior Legal Counsel** ([HUKUKİ DİREKTÖR 1]/[HUKUKİ DİREKTÖR 2] ekipleri) — hukuki argümantasyon
- **İlgili iş birimi başkanı** (Mirzayev rafineri/[petrokimya iştiraki]; İbrahimov doğal gaz) — operasyonel
- **CLCO ([CLCO ADI])** — kritik politika kararları imzası

## TR Legal MCP

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="13. Daire",
  arananKelime="EPDK lisans iptal idari ceza",
  baslangicTarihi="2022-01-01"
)
```

## Mevzuat MCP

```
search_mevzuat(mevzuat_no="5015", mevzuat_tur="KANUN")  # PPK
search_mevzuat(mevzuat_no="4646", mevzuat_tur="KANUN")  # DGPK
search_mevzuat(mevzuat_no="6446", mevzuat_tur="KANUN")  # EPK
search_mevzuat(mevzuat_no="4628", mevzuat_tur="KANUN")  # EPDK K.
search_mevzuat(mevzuat_adi="EPDK", mevzuat_tur="YONETMELIK")
search_mevzuat(mevzuat_adi="EPDK", mevzuat_tur="TEBLIGLER")
```

## Bağlantılı

- [İYUK rehberi](iyuk-rehberi.md)
- [İdari yargı yapısı](idari-yargi-yapisi-rehberi.md)
- [[ŞİRKET ADI] [ELEKTRİK SANTRALİ] elektrik üretim rehberi](socar-ican-elektrik-uretim-rehberi.md)
- [[ŞİRKET ADI] [HALKA AÇIK İŞTİRAK] KAP rehberi](socar-[petrokimya iştiraki]-kap-rehberi.md)
