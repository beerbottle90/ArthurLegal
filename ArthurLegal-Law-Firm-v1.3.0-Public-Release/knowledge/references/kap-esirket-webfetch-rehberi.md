# KAP + e-ŞİRKET – WebFetch Kullanım Rehberi

> MKK'nın doğrudan API'sine [Müvekkil] aracı kurum olmadığı için erişim yok. Ancak **KAP (Kamuyu Aydınlatma Platformu)** ve **e-ŞİRKET portal** (MKK iştiraki) public bilgi sunar. WebFetch ile çekilir.

---

## 1. KAP (Kamuyu Aydınlatma Platformu)

**Ana URL:** https://www.kap.org.tr/tr/

KAP, BIST kotasındaki tüm şirketlerin **özel durum açıklamaları**, **mali tabloları**, **kurumsal yönetim bilgileri**, **içsel bilgi listeleri** gibi yasal açıklamalarını barındırır. SPK Tebliğ II-15.1 kapsamında zorunlu.

> **v1.5.0 Güncelleme (22.05.2026):** KAP arayüzü Next.js App Router'a taşındı.
> Alt sekme URL'leri (`/tr/sirket-bilgileri/ortaklik-yapisi/...` gibi) kaldırıldı.
> JSON API (`/tr/api/disclosure?...`) WAF tarafından engelleniyor.
> **Çalışan iki yöntem:** (1) `/tr/search/{TICKER}/{sayfa}` — bildirim arama,
> (2) `/tr/sirket-bilgileri/ozet/{OID}-{slug}` — şirket özet sayfası.

### Petkim için güncel çalışan URL'ler

| Konu | URL | Durum |
|---|---|---|
| Petkim bildirim araması (sayfalı) | https://www.kap.org.tr/tr/search/PETKM/1 | ✅ Aktif — WebFetch içerik döndürür |
| Petkim bildirim araması sayfa 2 | https://www.kap.org.tr/tr/search/PETKM/2 | ✅ Aktif |
| Petkim şirket özeti (ana sayfa) | https://www.kap.org.tr/tr/sirket-bilgileri/ozet/2400-petkim-petrokimya-holding-a-s | ✅ HTTP 200, JS-rendered (kısmi içerik) |
| KAP ana sayfa / navigasyon | https://www.kap.org.tr/tr/ | ✅ Aktif |
| BIST şirketler listesi | https://www.kap.org.tr/tr/bist-sirketler | ✅ Aktif |
| Detaylı bildirim sorgu sayfası | https://www.kap.org.tr/tr/bildirim-sorgu | ✅ Aktif |

### Eski URL'ler — Artık Çalışmıyor (404)

> Aşağıdaki URL'ler KAP arayüz güncellemesiyle kaldırıldı. Kullanmayın.

| Eski URL | Neden çalışmıyor |
|---|---|
| `/tr/sirket-bilgileri/ortaklik-yapisi/PETKM` | 404 — JS-rendered sekmeye taşındı |
| `/tr/sirket-bilgileri/yk-uyeleri/PETKM` | 404 — JS-rendered |
| `/tr/sirket-bilgileri/esas-sozlesme/PETKM` | 404 — JS-rendered |
| `/tr/MaliTablo/PETKM` | 404 — kaldırıldı |
| `/tr/Bildirim/PETKM` | 404 — kaldırıldı |
| `/tr/api/disclosure?id=PETKM&...` | WAF engeli (HTTP 666/500) |

> **Not:** Şirket özeti URL'sindeki ID doğru olmalı: Petkim = **2400** (eski rehberdeki 1094 yanlıştı).
> Başka şirket için ID, KAP'ta `/tr/search/{TICKER}/1` arama sonuçlarından okunabilir.

### WebFetch örnekleri (güncel)

**Örnek 1: Petkim son bildirimler — BİRİNCİL YÖNTEM**
```
WebFetch:
  url: "https://www.kap.org.tr/tr/search/PETKM/1"
  prompt: "Son 5 Petkim özel durum açıklamasını listele: tarih, başlık, kategori,
           2 cümle özet. Kaç toplam sonuç var?"
```

**Örnek 2: Petkim son bildirimler sayfa 2-5**
```
WebFetch:
  url: "https://www.kap.org.tr/tr/search/PETKM/2"   # sayfa 2, 3, 4, 5... artır
  prompt: "Bu sayfadaki Petkim bildirimlerini listele: tarih, başlık, özet."
```

**Örnek 3: Petkim şirket özeti (kısmi — JS-rendered)**
```
WebFetch:
  url: "https://www.kap.org.tr/tr/sirket-bilgileri/ozet/2400-petkim-petrokimya-holding-a-s"
  prompt: "Sayfada görünen Petkim şirket bilgilerini listele: sermaye, sektör,
           son bildirimler, yönetim kurulu bilgileri."
```
> ⚠️ Bu sayfa JavaScript ile yükleniyor. WebFetch kısmi içerik döndürür.
> Ortaklık yapısı ve YK üyeleri için şirket özeti sayfası yerine
> `/tr/search/PETKM/1` arama sonuçlarındaki bildirimlerden çıkarım yap.

**Örnek 4: Başka BIST şirketi — Ticker değiştir**
```
WebFetch:
  url: "https://www.kap.org.tr/tr/search/{TICKER}/1"   # TICKER = THYAO, TUPRS, EREGL...
  prompt: "Son 5 bildirimi listele."
```

### Saat ve gün

- KAP açıklamaları **işlem günü 09:30-18:30** arasında yayınlanır
- Hafta sonu duyuru yok (acil durumlar hariç)
- Hafta içi her sabah Petkim'in açıklamalarını tarama → reg-feed digest'e gir

### Atıf etiketi

`[KAP — Petkim — GG.AA.YYYY HH:MM]` formatı.

---

## 2. e-ŞİRKET Portal (MKK iştiraki)

**Ana URL:** https://e-sirket.mkk.com.tr/

MKK'nın halka açık şirket bilgi portalı. Aşağıdaki bilgileri **public** olarak verir:

- Çıkarılmış sermaye + bedelli/bedelsiz sermaye artırımları
- Pay alım/satım tarihçesi (özet)
- Genel Kurul gündem ve karar özetleri
- Bilgilendirme dokümanları (faaliyet raporu, yatırımcı sunumu)
- Ortaklık yapısı (KAP ile çapraz teyit)
- Pay sahipleri özet (büyük ortaklar)

### Petkim için pratik URL'ler

| Konu | Yaklaşık URL pattern |
|---|---|
| Petkim ana sayfa | https://e-sirket.mkk.com.tr/dgsystem/external/PartnerShipDetail?cguid=... (parametre Petkim için sabit) |
| Genel Kurul gündem | (Aynı sayfa, "Genel Kurul" sekmesi) |
| Sermaye yapısı | (Aynı sayfa, "Sermaye" sekmesi) |
| Bilgilendirme dokümanları | (Aynı sayfa, "Dokümanlar" sekmesi) |

### WebFetch örnekleri

**Örnek 1: Petkim sermaye yapısı + son artırım**
```
WebFetch:
  url: "https://e-sirket.mkk.com.tr/.../PartnerShipDetail?ticker=PETKM"
  prompt: "List the current çıkarılmış sermaye TL, capital structure changes 
           in last 24 months (bedelli/bedelsiz/birleşik), and latest GK kararı 
           regarding capital."
```

**Örnek 2: Genel Kurul gündem**
```
WebFetch:
  url: "https://e-sirket.mkk.com.tr/.../GeneralAssembly?ticker=PETKM"
  prompt: "Latest GK tarih, gündem maddeleri, alınan kararlar özet."
```

---

## 3. KAP vs e-ŞİRKET — hangisini kullan?

| Veri tipi | Birincil | İkincil (çapraz teyit) |
|---|---|---|
| Özel durum açıklamaları | **KAP** | — |
| Mali tablolar (UFRS) | **KAP** | e-ŞİRKET |
| Yönetim Kurulu | **KAP** | — |
| Ortaklık yapısı (anlık) | **KAP** | e-ŞİRKET |
| Sermaye artırımı detayları | e-ŞİRKET | KAP (özel durum içinde) |
| Genel Kurul kararları | e-ŞİRKET (gündem + karar zaptı) | KAP (özel durum) |
| İçsel bilgi listesi | KAP (kurumsal yönetim) | — |

**Pratik:** Çoğu Petkim sorgusu için **KAP yeterli**. e-ŞİRKET'i derinlemesine GK + sermaye detayı için kullan.

---

## 4. Diğer halka açık şirketlere de uygulanabilir

KAP ve e-ŞİRKET BIST'teki tüm halka açık şirketler için aynı yapıyı kullanır. Sözleşme/M&A süreçlerinde karşı taraf eğer BIST'te kayıtlıysa, aynı pattern'larla bilgi çekilebilir.

**Örnek:** [Müvekkil] Türkiye bir BIST şirketiyle JV yapıyor → o şirketin
- KAP özel durum geçmişi (son 1 yıl) — `WebFetch: https://www.kap.org.tr/tr/search/{TICKER}/1`
- Son bildirimler sayfa 2-5 — sayfa numarasını artırarak tarama yap
- Mali sağlığı, YK üyeleri, ortaklık yapısı — `/tr/search/{TICKER}/` bildirimlerinden çıkarım yap

> **Uyarı:** Ortaklık yapısı ve YK bilgileri için eski direkt URL'ler artık çalışmıyor.
> Bildirim metnini oku → içerisindeki ortaklık/YK değişiklik duyurularını kullan.

---

## 5. Resmi atıf ve saklama

Bu kaynaklar **resmi public records** statüsünde. M&A diligence raporlarında, hukuki memorandum'larda **doğrudan atıf yapılabilir**.

Format:
- KAP: `[KAP — PETKM — özel durum açıklaması GG.AA.YYYY HH:MM]`
- e-ŞİRKET: `[e-ŞİRKET MKK — PETKM — sermaye yapısı GG.AA.YYYY]`

---

## 6. Petkim için haftalık otomatik akış öneri

`/regulatory-legal:reg-feed-watcher` çalıştığında otomatik dahil:

```
Her Pazartesi 08:00:
  1. KAP Petkim son bildirimleri:
     WebFetch: https://www.kap.org.tr/tr/search/PETKM/1  (sayfa 1, geçen hafta tarihleri)
     WebFetch: https://www.kap.org.tr/tr/search/PETKM/2  (gerekirse sayfa 2)
  2. e-ŞİRKET Petkim sermaye yapısı (JS-rendered — değişiklik varsa kullanıcı manuel kontrol)
  3. Yönetim Kurulu üyesi değişikliği → KAP bildirimlerinden çıkar + sanctions tarama tetikleyici
  4. Çeyreklik mali tablo bildirimi → bildirim metninde "finansal tablo" anahtar kelimesiyle ara
  
Sonuç → reg-feed haftalık digest'e [Müvekkil]-Petkim bölümü
```

---

## 7. Sınırlamalar

- KAP açıklamaları **standart format değil** — şirketler farklı style + uzunluk kullanır; AI özetleme gerekli
- **KAP JSON API (`/tr/api/disclosure?...`) WAF tarafından engellendi** (Mayıs 2026 itibariyle); alternatif: `/tr/search/{TICKER}/{sayfa}` WebFetch
- **Alt sekme URL'leri kaldırıldı** (ortaklık-yapisi, yk-uyeleri, vb.) — bu bilgilere KAP üzerinden WebFetch ile doğrudan erişilemiyor; `/tr/search/` bildirimlerinden çıkarım yapılabilir
- **Şirket özet sayfası JS-rendered** — `/tr/sirket-bilgileri/ozet/{OID}-{slug}` HTTP 200 döner ama tam içerik için tarayıcı gerekli
- e-ŞİRKET arayüzü dinamik (JavaScript SPA) — WebFetch içerik döndüremiyor; kullanıcı manuel kontrol gerekli
- Tarihsel veri kapsamı KAP için iyi (2010+), e-ŞİRKET için kısıtlı
- **Anlık trading data YOK** — fiyat/hacim için BIST veya Matriks
- **Gizli ortaklar (UBO)** kamuya açık değil — KAP/e-ŞİRKET sadece tescile tabi büyük ortakları gösterir

---

*Son güncelleme: 22.05.2026 — KAP URL yapısı güncellendi (Next.js App Router geçişi; alt sekme URL'leri 404, JSON API WAF engeli, search endpoint aktif). Petkim ID düzeltildi: 1094 → 2400. MKK doğrudan API erişimi [Müvekkil] durumunda yok.*
