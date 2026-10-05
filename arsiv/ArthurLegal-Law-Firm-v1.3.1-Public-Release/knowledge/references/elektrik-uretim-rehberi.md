# Elektrik Üretim Rehberi — Enerji Uyuşmazlıklarında Teknik Claim Bağlamı

> Bu rehber **sektörel teknik dayanak** referansıdır: elektrik üretim
> uyuşmazlıklarında (bilirkişi raporu, mütalaa, tazminat/yoksun kalınan kâr hesabı)
> kullanılan **teknik kavramların hukuki karşılığı**. Amaç, hukukçunun teknik
> bilirkişi diliyle konuşabilmesi ve raporun **denetime elverişliliğini** teknik
> yönden sorgulayabilmesidir. Müvekkile özel santral verisi için
> `sirket-elektrik-uretim-rehberi.md` (varsa) ile birlikte kullan.

## Hukuki çerçeve

| Dayanak | Kapsam |
|---|---|
| **6446 sayılı Elektrik Piyasası Kanunu** | Üretim lisansı, önlisans, piyasa faaliyetleri, EPDK yetkisi |
| **5346 sayılı Yenilenebilir Enerji Kaynaklarının Elektrik Enerjisi Üretimi Amaçlı Kullanımına İlişkin Kanun** | YEK Belgesi, **YEKDEM** destek mekanizması, alım garantisi |
| **Elektrik Piyasası Dengeleme ve Uzlaştırma Yönetmeliği** (EPDK) | Saatlik uzlaştırma, dengeleme, gün öncesi/gün içi piyasa, **EPİAŞ** işletimi |
| **Elektrik Piyasası Lisans Yönetmeliği** (EPDK) | Lisans tadili, tahsis, süre, kurulu güç değişikliği |
| **Elektrik Şebeke Yönetmeliği** (EPDK) | Şebekeye bağlantı, sistem kullanım, kısıt yönetimi (TEİAŞ) |

**Kurumsal harita:** **EPDK** (düzenleyici) · **EPİAŞ** (piyasa işletmecisi — uzlaştırma/faturalama) · **TEİAŞ** (iletim sistem işletmecisi — şebeke kısıtı, YAL/YAT talimatı) · dağıtım şirketleri (DSO).

## Teknik kavram → hukuki karşılık

| Teknik kavram | Tanım | Uyuşmazlıkta önemi |
|---|---|---|
| **Kurulu güç (MWe/MWm)** | Santralin nominal üretim kapasitesi | Lisans kapsamı; kurulu güç aşımı/değişikliği tadil gerektirir |
| **Kapasite faktörü** | Fiili üretim ÷ (kurulu güç × dönem saati) | Üretim kaybı/yoksun kalınan kâr hesabının temel çarpanı |
| **Emre amadelik (availability)** | Tesisin üretime hazır olduğu süre oranı | Kesinti kimden kaynaklı — bakım, arıza, şebeke? Kusur tahsisi |
| **Şebeke kısıtı (kısıt/kısıntı)** | TEİAŞ'ın sistem güvenliği için üretimi sınırlaması (YAL/YAT) | Üretim kaybı **operatör kaynaklı mı** — tazminat sorumluluğu ayrımı |
| **Sayaç / uzlaştırma (EPİAŞ)** | Saatlik ölçüm verisinin piyasa faturasına dönüşmesi | Alacak/borç ihtilafında **birincil delil**: uzlaştırma verisi |
| **YEKDEM** | Yenilenebilir üretime USD bazlı alım garantisi (5346) | Alım fiyatı, YEKDEM'e giriş/çıkış, yerli katkı ilavesi ihtilafı |
| **Dengeleme (dengesizlik)** | Tahmin ile gerçekleşen üretim farkının maliyeti | Dengesizlik maliyeti kimin — üretici tahmin hatası mı, mücbir sebep mi |

## Uyuşmazlık tipleri (üretim tarafı)

1. **Üretim kaybı / yoksun kalınan kâr** — arıza, şebeke kısıtı veya üçüncü kişi kusuru nedeniyle üretilemeyen enerji. Hesap: `kayıp saat × kurulu güç × kapasite faktörü × birim fiyat (PTF/YEKDEM)`.
2. **Uzlaştırma alacağı ihtilafı** — EPİAŞ uzlaştırma verisi ile üretici kaydı arasında fark; sayaç/ölçüm doğruluğu.
3. **YEKDEM ihtilafı** — YEKDEM'e giriş tarihi, USD alım fiyatı, yerli aksam desteği, süre.
4. **Lisans/kurulu güç uyuşmazlığı** — EPDK tadil kararına karşı iptal davası (idari yargı → `iyuk-rehberi.md`).
5. **EPC / santral inşaatı** — gecikme, üretime geçiş (COD) sapması, performans garantisi (hakediş/delay analizi).

## Bilirkişi raporuna teknik itiraz kontrol listesi

- Rapor **kapasite faktörünü** hangi veriye dayandırıyor? (santral geçmişi mi, teorik mi?)
- Üretim kaybı **şebeke kısıtından** mı kaynaklı — TEİAŞ YAL/YAT kayıtları çekildi mi?
- Birim fiyat **hangi referans**: PTF (gün öncesi), ikili anlaşma fiyatı, yoksa YEKDEM tarifesi?
- **EPİAŞ uzlaştırma** çıktısı rapora eklenmiş mi — yoksa rapor denetime elverişsizdir.
- Dengesizlik maliyeti ayrıştırılmış mı (üretici tahmin hatası ≠ mücbir sebep)?
- Bakım/emre amadelik verisi **sözleşmedeki garanti** ile karşılaştırıldı mı?

> Not: "Denetime elverişli olmayan rapor hükme esas alınamaz" ilkesi enerji
> dosyalarında özellikle uzlaştırma/ölçüm verisi eksikliğinde işler.
> İçtihat için `yargi-mcp-rehberi.md` pattern'ları ile ilgili Daire kararlarını çek.

## Mevzuat MCP

```
mevzuat_ara(mevzuat_no="6446")                       # Elektrik Piyasası Kanunu
mevzuat_ara(mevzuat_no="5346")                       # YEK Kanunu (YEKDEM)
mevzuat_ara(phrase="dengeleme uzlaştırma elektrik")  # uzlaştırma yönetmeliği
mevzuat_icinde_ara(mevzuat_id=..., query="...")      # ilgili madde metni
```

## Yargı MCP

```
ictihat_ara(phrase="üretim kaybı yoksun kalınan kâr elektrik", birimAdi="<ilgili HD>")
ictihat_ara(phrase="YEKDEM uzlaştırma alacak")
semantik_ictihat_ara(...)                             # kavramsal arama
```

## Bağlantılı

- [Bilirkişilik rehberi](bilirkisilik-rehberi.md) — rapora itiraz + denetime elverişlilik
- [EPDK rehberi](epdk-rehberi.md) — lisans + düzenleyici dialog
- [ÇED rehberi](ced-rehberi.md) — santral izin/çevre boyutu
- [İSG dava rehberi](isg-dava-rehberi.md) — santral iş kazası + kusur dağılımı
- [İYUK rehberi](iyuk-rehberi.md) — EPDK kararına karşı idari dava
- [Mevzuat MCP rehberi](mevzuat-mcp-rehberi.md) — madde çekme pattern'ları
- [Yargı MCP rehberi](yargi-mcp-rehberi.md) — içtihat çekme pattern'ları
- [Kanun kısaltmalar](kanun-kisaltmalar.md) — 6446 / 5346 kısaltma standardı
