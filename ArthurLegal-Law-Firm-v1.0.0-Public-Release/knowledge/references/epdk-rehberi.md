# EPDK (Enerji Piyasası Düzenleme Kurumu) Rehberi — Şirket Dialog Modeli

> ArthurLegal Holding için günlük operasyonel düzenleyici. [Rafineri Tesisi] (petrol piyasası), [Halka Açık İştirak] (petrokimya), [Elektrik İştiraki] (elektrik üretim), eski [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] (doğal gaz dağıtım) — hepsi EPDK lisans + tebliğ kapsamında.

## Hukuki çerçeve

| Kanun | Sektör |
|---|---|
| **5015 Petrol Piyasası Kanunu** | Rafineri, akaryakıt — [Rafineri Tesisi] + Enerji Ticaret A.Ş. |
| **4646 Doğal Gaz Piyasası Kanunu** | Doğal gaz dağıtım (eski [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B]) + iletim ([Boru Hattı Projesi]) + ticaret |
| **6446 Elektrik Piyasası Kanunu** | Elektrik üretim — **[Elektrik İştiraki]** + [Halka Açık İştirak] RES |
| **5346 Yenilenebilir Enerji Kaynakları K.** | RES, GES (rüzgar/güneş) |
| **4628 sayılı EPDK Kanunu** (kuruluş) | Kurumsal yapı |

## EPDK Kurul yapısı

- **Kurul:** 7 üye (Cumhurbaşkanı tarafından atanır), kararlar oyçoğunluğu
- **Daire Başkanlıkları:** Petrol, Doğal Gaz, Elektrik, Lisans, vd.
- **Kurul kararları:** Bireysel (lisans) veya genel (Tebliğ, Yönetmelik)

## Lisans tipleri (Şirket ilgili)

| Lisans | Şirket'te |
|---|---|
| Rafinaj | [Rafineri Tesisi] |
| Depolama | Depolama A.Ş. |
| Dağıtım (petrol) | Enerji Ticaret A.Ş. |
| Bayilik | (akaryakıt istasyonları varsa) |
| Doğal gaz dağıtım | Eski [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] (devir) |
| Doğal gaz toptan satış | Enerji Ticaret A.Ş. |
| **Elektrik üretim** | **[Elektrik İştiraki]** ([DOLDUR — kapasite] kombine çevrim, yakın geçmiş) |
| Boru hattı (iletim) | [Boru Hattı Projesi] (özel rejim) |

## Şirket EPDK dialog modeli (proaktif)

1. **Günlük operasyon:** Lisans şartlarına uyum, periyodik raporlama (üretim, satış, stok)
2. **Yapısal dialog:** EPDK ile periyodik toplantı (sektör temsili), informal yazışma
3. **Tebliğ taslakları:** Kamuoyu istişaresi sürecinde **Şirket görüş sunumu** (Compliance + Hukuk)
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

## EPDK ile çatışma senaryoları (Şirket'e özel)

### [Rafineri Tesisi]
- Üretim kapasitesi-lisans uyumu
- Çevre uyum (ÇED + EPDK ortak)
- Akaryakıt satış pazar payı (Rekabet ile ortak dikkat)

### [Halka Açık İştirak]
- Petrokimya hammadde lisans
- Üretim duruşu bildirimleri
- Halka açık raporlama uyumu (SPK + KAP paralel)

### [Elektrik İştiraki] (yeni — yakın geçmiş)
- 6446 EPK kapsamında elektrik üretim lisansı
- devir sonrası **6 adım** EPDK süreci (lisans transferi)
- Detay: `references/elektrik-uretim-istiraki-rehberi.md`

### Eski [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B]
- Devir süreci tamamlandı/tamamlanıyor (2024-2026)
- VERBİS + lisans + müşteri bilgi geçişi paralel
- Yeni sahibe geçiş yükümlülükleri

## EPDK koordinasyon ([Şirket] Hukuk & Compliance)

- **Compliance Direktörü [Uyum Direktörü]** — EPDK ile genel ilişki sahibi
- **Regulatory Compliance Manager [Reg. Compliance Manager]** — günlük EPDK dosyaları
- **Senior Legal Counsel** ([Hukuk Direktörü A]/[Hukuk Direktörü B] ekipleri) — hukuki argümantasyon
- **İlgili iş birimi başkanı** ([Rafineri/Petrokimya Birim Başkanı]; [Doğal Gaz/Enerji Birim Başkanı]) — operasyonel
- **CLCO ([CLCO])** — kritik politika kararları imzası

## Yargı MCP

```
mcp__claude_ai_Yargi_MCP__search_danistay_decisions(
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
- [Şirket [Elektrik İştiraki] elektrik üretim rehberi](elektrik-uretim-istiraki-rehberi.md)
- [Şirket [Halka Açık İştirak] KAP rehberi](halka-acik-istirak-kap-rehberi.md)
