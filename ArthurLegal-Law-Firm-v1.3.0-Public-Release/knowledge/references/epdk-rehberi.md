# EPDK (Enerji Piyasası Düzenleme Kurumu) Rehberi — [Müvekkil] Dialog Modeli

> [Müvekkil] Türkiye için günlük operasyonel düzenleyici. STAR Rafineri (petrol piyasası), Petkim (petrokimya), İÇAN (elektrik üretim), eski Bursagaz/Kayserigaz (doğal gaz dağıtım) — hepsi EPDK lisans + tebliğ kapsamında.

## Hukuki çerçeve

| Kanun | Sektör |
|---|---|
| **5015 Petrol Piyasası Kanunu** | Rafineri, akaryakıt — STAR + [Müvekkil] Enerji Ticaret |
| **4646 Doğal Gaz Piyasası Kanunu** | Doğal gaz dağıtım (eski Bursagaz/Kayserigaz) + iletim (TANAP) + ticaret |
| **6446 Elektrik Piyasası Kanunu** | Elektrik üretim — **İÇAN** + Petkim RES |
| **5346 Yenilenebilir Enerji Kaynakları K.** | RES, GES (rüzgar/güneş) |
| **4628 sayılı EPDK Kanunu** (kuruluş) | Kurumsal yapı |

## EPDK Kurul yapısı

- **Kurul:** 7 üye (Cumhurbaşkanı tarafından atanır), kararlar oyçoğunluğu
- **Daire Başkanlıkları:** Petrol, Doğal Gaz, Elektrik, Lisans, vd.
- **Kurul kararları:** Bireysel (lisans) veya genel (Tebliğ, Yönetmelik)

## Lisans tipleri ([Müvekkil] ilgili)

| Lisans | [Müvekkil]'da |
|---|---|
| Rafinaj | STAR Rafineri |
| Depolama | [müvekkil depolama tesisi] |
| Dağıtım (petrol) | [Müvekkil] Enerji Ticaret |
| Bayilik | (akaryakıt istasyonları varsa) |
| Doğal gaz dağıtım | Eski Bursagaz/Kayserigaz (devir) |
| Doğal gaz toptan satış | [Müvekkil] Enerji Ticaret |
| **Elektrik üretim** | **İÇAN** (870 MW kombine çevrim, Şubat 2025) |
| Boru hattı (iletim) | TANAP (özel rejim) |

## [Müvekkil] EPDK dialog modeli (proaktif)

1. **Günlük operasyon:** Lisans şartlarına uyum, periyodik raporlama (üretim, satış, stok)
2. **Yapısal dialog:** EPDK ile periyodik toplantı (sektör temsili), informal yazışma
3. **Tebliğ taslakları:** Kamuoyu istişaresi sürecinde **[Müvekkil] görüş sunumu** (Compliance + Hukuk)
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

## EPDK ile çatışma senaryoları ([Müvekkil]'a özel)

### STAR Rafineri
- Üretim kapasitesi-lisans uyumu
- Çevre uyum (ÇED + EPDK ortak)
- Akaryakıt satış pazar payı (Rekabet ile ortak dikkat)

### Petkim
- Petrokimya hammadde lisans
- Üretim duruşu bildirimleri
- Halka açık raporlama uyumu (SPK + KAP paralel)

### İÇAN (yeni — Şubat 2025)
- 6446 EPK kapsamında elektrik üretim lisansı
- Şubat 2025 devir sonrası **6 adım** EPDK süreci (lisans transferi)
- Detay: `references/epdk-rehberi.md`

### Eski Bursagaz/Kayserigaz
- Devir süreci tamamlandı/tamamlanıyor (2024-2026)
- VERBİS + lisans + müşteri bilgi geçişi paralel
- Yeni sahibe geçiş yükümlülükleri

## EPDK koordinasyon ([Müvekkil] Legal & Compliance)

- **Compliance Direktörü [Uyum Direktörü]** — EPDK ile genel ilişki sahibi
- **Regulatory Compliance Manager [Regulatory Compliance Manager]** — günlük EPDK dosyaları
- **Senior Legal Counsel** ([Hukuk Müdürlüğü]) — hukuki argümantasyon
- **İlgili iş birimi başkanı** [İş Birimi Başkanı] — operasyonel
- **CLCO ([CLCO])** — kritik politika kararları imzası

## Yarg MCP

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
- [[Müvekkil] İÇAN elektrik üretim rehberi](socar-ican-elektrik-uretim-rehberi.md)
- [[Müvekkil] Petkim KAP rehberi](socar-petkim-kap-rehberi.md)
