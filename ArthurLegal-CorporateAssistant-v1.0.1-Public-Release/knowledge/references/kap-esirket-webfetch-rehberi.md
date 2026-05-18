# KAP + e-ŞİRKET – WebFetch Kullanım Rehberi

> MKK'nın doğrudan API'sine Şirket aracı kurum olmadığı için erişim yok. Ancak **KAP (Kamuyu Aydınlatma Platformu)** ve **e-ŞİRKET portal** (MKK iştiraki) public bilgi sunar. WebFetch ile çekilir.

---

## 1. KAP (Kamuyu Aydınlatma Platformu)

**Ana URL:** https://www.kap.org.tr/tr/

KAP, BIST kotasındaki tüm şirketlerin **özel durum açıklamaları**, **mali tabloları**, **kurumsal yönetim bilgileri**, **içsel bilgi listeleri** gibi yasal açıklamalarını barındırır. SPK Tebliğ II-15.1 kapsamında zorunlu.

### [Halka Açık İştirak] için pratik URL'ler

| Konu | URL |
|---|---|
| [Halka Açık İştirak] ana sayfa | https://www.kap.org.tr/tr/sirket-bilgileri/ozet/2400-[halka-acik-istirak]-petrokimya-holding-a-s |
| Özel durum açıklamaları | https://www.kap.org.tr/tr/Bildirim/[BIST-KOD] (son N) |
| Tüm bildirimler (filtre) | https://www.kap.org.tr/tr/api/disclosure?id=[BIST-KOD]&offset=0&limit=20 (JSON public) |
| Mali tablolar | https://www.kap.org.tr/tr/MaliTablo/[BIST-KOD] |
| Yönetim Kurulu | https://www.kap.org.tr/tr/sirket-bilgileri/yk-uyeleri/[BIST-KOD] |
| Hissedarlar (ortaklık yapısı) | https://www.kap.org.tr/tr/sirket-bilgileri/ortaklik-yapisi/[BIST-KOD] |
| Esas sözleşme | https://www.kap.org.tr/tr/sirket-bilgileri/esas-sozlesme/[BIST-KOD] |
| Ana sözleşme değişiklikleri | (Aynı URL, "değişiklik" sekmesi) |
| Bağımsız denetim raporları | (Mali Tablo sayfası ek olarak) |

### WebFetch örnekleri

**Örnek 1: [Halka Açık İştirak] son 5 KAP açıklaması**
```
WebFetch:
  url: "https://www.kap.org.tr/tr/Bildirim/[BIST-KOD]"
  prompt: "Liste the most recent 5 disclosures (özel durum açıklamaları) by date.
           For each: date, title, category (e.g., 'önemli olay', 'pay alım/satım'), 
           summary in 2 sentences."
```

**Örnek 2: [Halka Açık İştirak] ortaklık yapısı**
```
WebFetch:
  url: "https://www.kap.org.tr/tr/sirket-bilgileri/ortaklik-yapisi/[BIST-KOD]"
  prompt: "List all shareholders with pay ratio %, including ArthurLegal Holding A.Ş.'s 
           direct + indirect total stake. Note any change vs previous filing if shown."
```

**Örnek 3: [Halka Açık İştirak] son yönetim kurulu üyeleri**
```
WebFetch:
  url: "https://www.kap.org.tr/tr/sirket-bilgileri/yk-uyeleri/[BIST-KOD]"
  prompt: "List current YK üyeleri with name, role (başkan/üye/bağımsız), 
           appointment date, term end date."
```

### Saat ve gün

- KAP açıklamaları **işlem günü 09:30-18:30** arasında yayınlanır
- Hafta sonu duyuru yok (acil durumlar hariç)
- Hafta içi her sabah [Halka Açık İştirak]'in açıklamalarını tarama → reg-feed digest'e gir

### Atıf etiketi

`[KAP — [Halka Açık İştirak] — GG.AA.YYYY HH:MM]` formatı.

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

### [Halka Açık İştirak] için pratik URL'ler

| Konu | Yaklaşık URL pattern |
|---|---|
| [Halka Açık İştirak] ana sayfa | https://e-sirket.mkk.com.tr/dgsystem/external/PartnerShipDetail?cguid=... (parametre [Halka Açık İştirak] için sabit) |
| Genel Kurul gündem | (Aynı sayfa, "Genel Kurul" sekmesi) |
| Sermaye yapısı | (Aynı sayfa, "Sermaye" sekmesi) |
| Bilgilendirme dokümanları | (Aynı sayfa, "Dokümanlar" sekmesi) |

### WebFetch örnekleri

**Örnek 1: [Halka Açık İştirak] sermaye yapısı + son artırım**
```
WebFetch:
  url: "https://e-sirket.mkk.com.tr/.../PartnerShipDetail?ticker=[BIST-KOD]"
  prompt: "List the current çıkarılmış sermaye TL, capital structure changes 
           in last 24 months (bedelli/bedelsiz/birleşik), and latest GK kararı 
           regarding capital."
```

**Örnek 2: Genel Kurul gündem**
```
WebFetch:
  url: "https://e-sirket.mkk.com.tr/.../GeneralAssembly?ticker=[BIST-KOD]"
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

**Pratik:** Çoğu [Halka Açık İştirak] sorgusu için **KAP yeterli**. e-ŞİRKET'i derinlemesine GK + sermaye detayı için kullan.

---

## 4. Diğer halka açık şirketlere de uygulanabilir

KAP ve e-ŞİRKET BIST'teki tüm halka açık şirketler için aynı yapıyı kullanır. Sözleşme/M&A süreçlerinde karşı taraf eğer BIST'te kayıtlıysa, aynı pattern'larla bilgi çekilebilir.

**Örnek:** ArthurLegal Holding bir BIST şirketiyle JV yapıyor → o şirketin
- KAP özel durum geçmişi (son 1 yıl)
- Mali sağlığı
- Ortaklık yapısı
- YK üyeleri (sanctions cross-check için)
- Açık davaları

hepsi WebFetch ile çekilebilir.

---

## 5. Resmi atıf ve saklama

Bu kaynaklar **resmi public records** statüsünde. M&A diligence raporlarında, hukuki memorandum'larda **doğrudan atıf yapılabilir**.

Format:
- KAP: `[KAP — [BIST-KOD] — özel durum açıklaması GG.AA.YYYY HH:MM]`
- e-ŞİRKET: `[e-ŞİRKET MKK — [BIST-KOD] — sermaye yapısı GG.AA.YYYY]`

---

## 6. [Halka Açık İştirak] için haftalık otomatik akış öneri

`/regulatory-legal:reg-feed-watcher` çalıştığında otomatik dahil:

```
Her Pazartesi 08:00:
  1. KAP'tan [Halka Açık İştirak]'in geçen haftaki tüm özel durum açıklamaları (WebFetch)
  2. e-ŞİRKET'ten [Halka Açık İştirak]'in son sermaye yapısı (değişiklik varsa)
  3. Yönetim Kurulu üyesi değişikliği (CV güncelleme + sanctions tarama tetikleyici)
  4. Bağımsız denetim raporu (çeyreklik mali tablo)
  
Sonuç → reg-feed haftalık digest'e Şirket-[Halka Açık İştirak] bölümü
```

---

## 7. Sınırlamalar

- KAP açıklamaları **standart format değil** — şirketler farklı style + uzunluk kullanır; AI özetleme gerekli
- e-ŞİRKET arayüzü dinamik (JavaScript) — bazı sayfalarda WebFetch içerik döndürmeyebilir; alternatif: kullanıcı manuel kontrol
- Tarihsel veri kapsamı KAP için iyi (2010+), e-ŞİRKET için kısıtlı
- **Anlık trading data YOK** — fiyat/hacim için BIST veya Matriks
- **Gizli ortaklar (UBO)** kamuya açık değil — KAP/e-ŞİRKET sadece tescile tabi büyük ortakları gösterir

---

*Son güncelleme: 13.05.2026 — [Halka Açık İştirak] halka açık raporlama erişimi (KAP + e-ŞİRKET). MKK doğrudan API erişimi Şirket durumunda yok.*
