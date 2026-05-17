# İSG Davaları Rehberi – [Üretim Sahası] Rafineri & Petrokimya Bağlamı

> ArthurLegal Holding için yakıcı dava kategorisi. üretim kompleksindeki ölümlü/ciddi yaralanma kazalarında üçlü-paralel risk: cezai, tazminat, idari.

## Üçlü-paralel risk yapısı

Bir İSG kazası genelde **3 paralel dava süreci** doğurur — her biri ayrı mahkeme, ayrı vekil, ayrı strateji:

```
              İSG KAZASI
                  ↓
   ┌──────────────┼──────────────┬──────────────────┐
   ↓              ↓              ↓                  ↓
1. CEZAİ      2. TAZMİNAT     3. ÇEVRE          4. İDARİ
   (savcılık →    (mağdur/aile →   BAKANLIK CEZA      (EPDK lisans
   Asliye Ceza)   İş Mahkemesi     (Çevre K. 2872)    yaptırım)
                  veya Asliye HM)
```

## 1. Cezai dava

### Hukuki temel
- **TCK m. 85** — Taksirle öldürme (1-6 yıl hapis)
- **TCK m. 89** — Taksirle yaralama (3 ay - 1 yıl + ağırlatıcı sebepler)
- **TCK m. 257** — Görevi kötüye kullanma (memur sıfatlı için)
- **6331 sayılı İSG Kanunu m. 30, 31, 32** — İşveren ceza sorumluluğu
- **TCK m. 22/4** — Bilinçli taksir = ağırlatıcı

### Olası sanık
- Tesis müdürü
- İş güvenliği uzmanı (A sınıfı uzman zorunlu — büyük tesis)
- Vardiya amiri
- Yönetici sıfatıyla CEO/COO (büyük olaylar)
- Şirket tüzel kişiliği (CMK m. 138 — tüzel kişiye güvenlik tedbiri)

### Süreç
1. **Savcılık soruşturma açar** — 6 ay (uzatılabilir 2 ay daha)
2. **İddianame hazırlanır** — kabul/red mahkemece
3. **Asliye Ceza Mahkemesi'nde dava** — [Üretim Sahası] veya Karşıyaka (yer)
4. **Karar** — beraat / mahkumiyet / hükmün açıklanmasının geri bırakılması (HAGB)
5. **İstinaf** (BAM) — 2 hafta
6. **Temyiz** (Yargıtay Ceza) — 2 hafta

### Tipik karar tutarları (Yargıtay emsal)
- Bilinçsiz taksir: 1-3 yıl hapis (ertelenebilir)
- Bilinçli taksir: 3-6 yıl hapis (ertelemesiz)
- Birden fazla ölü: ağırlatma

Yargı MCP ile teyit:
```
mcp__claude_ai_Yargi_MCP__search_yargitay_decisions(
  arananKelime="taksirle öldürme iş kazası rafineri yönetici sorumluluk",
  daire="12. Ceza Dairesi",  # iş kazası temyizi
  baslangicTarihi="2023-01-01"
)
```

## 2. Tazminat davası

### Hukuki temel
- **TBK m. 49** — Haksız fiil tazminatı (genel)
- **TBK m. 50-52** — Tazminat hesaplanması
- **TBK m. 53** — Destek tazminatı (ölüm halinde aile)
- **TBK m. 54-56** — Bedensel zarar
- **TBK m. 56-58** — Manevi tazminat
- **4857 İş K. m. 77** — İşverenin iş güvenliği yükümlülüğü
- **5510 SGK Kanunu m. 13** — İş kazası tanımı

### Mağdur taraf
- **Yaralı kendisi:** Bedensel ve manevi tazminat
- **Ölüm halinde:**
  - Eş: destek tazminatı + manevi tazminat
  - Çocuklar: destek tazminatı + manevi tazminat
  - Anne/baba: destek tazminatı (öğrenim devam ediyorsa) + manevi tazminat

### Hesap kalemleri (KRİTİK)
| Kalem | Hesap metodu |
|---|---|
| Maddi zarar (tedavi) | Faturalar, geçici işgöremezlik geliri farkı |
| Maluliyet (varsa) | Pasif sermaye yöntemi (Yargıtay HGK) |
| **Destek tazminatı (ölüm)** | (Beklenen yaşam süresi - mevcut yaş) × destek oranı × pasif sermaye katsayısı (Yargıtay HGK 2017/123 metod) |
| **Manevi tazminat** | Yargıtay HGK eğilim: ölümlü kazada 50K-500K TL aralık, ağırlık takdiri |
| **Faiz** | Yasal faiz (TBK 88 + 3095 → değişken; 2026'da yıllık ~%X) |
| Vekalet ücreti | AAÜT — davacı vekiline %12-15 (mahkemece) |
| Yargılama gideri | Bilirkişi, tanık, harç |

### Mahkeme
- **İş Mahkemesi** — işçi-işveren iş kazası (4857 + İş Mahkemeleri K.)
- **Asliye Hukuk** — işçi olmayan mağdur (örn. ziyaretçi, vendor çalışanı)
- **Asliye Ticaret** — vendor sözleşme sorumluluğu paralel

### Süreç
- Cevap süresi: 2 hafta (HMK m. 127)
- Bilirkişi: 3 kişilik heyet (rafineri için petrol mühendisi, güvenlik uzmanı, hukukçu)
- Karar: 1-3 yıl (yerel)
- İstinaf + Temyiz: 1-2 yıl daha

## 3. Çevre Bakanlığı idari ceza

### Hukuki temel
- **2872 sayılı Çevre Kanunu m. 20-22** — Hava, su, toprak kirlilik cezaları
- **ÇED Yönetmeliği** — kaza sonrası ÇED inceleme zorunlu
- Tutarlar yıllık güncellenir (2026: kademe kademe milyonlarca TL'ye kadar)

### Süreç
1. Bakanlık denetçileri keşif yapar
2. **İdari para cezası kararı** tebliğ edilir
3. **60 gün içinde** Danıştay 10. ve 14. Daire'ye iptal davası
4. Karar: 1-2 yıl

## 4. EPDK lisans yaptırımı

### Hukuki temel
- **5015 Petrol Piyasası Kanunu** — petrol rafineri lisansı
- **EPDK Kurulu kararı** — uyarı, idari para cezası, geçici askıya alma, iptal

### Süreç
1. EPDK denetim raporu → kurul kararı
2. Şirket'e tebliğ → 60 gün Danıştay
3. **Lisans askıya alma = üretim durur** → büyük gelir kaybı

## [Üretim Sahası]-özel notlar

### Tesis bilgisi (kamuya açık veri)
- **[Rafineri Tesisi]:** 10 milyon ton/yıl ham petrol işleme. Yüksek riskli (Seveso II direktif kapsamı eşdeğer Türk mevzuatı).
- **[Halka Açık İştirak]:** Petrokimya, etilen + propilen üretim. Yangın/patlama riski yüksek.
- **Depolama A.Ş. / [Liman İştiraki] Terminal:** Yakıt depolama; yangın + çevre kirlilik riski.
- **[Üretim Sahası] ÖEB:** [DOLDUR — alan]; çoklu tesis, kazada birden fazla şirket etki.

### Yerel mahkemeler
- **[Üretim Sahası] Asliye Hukuk Mahkemesi**
- **[Üretim Sahası] İş Mahkemesi**
- **[Yerel] Asliye Hukuk / Asliye Ceza** (yetki paylaşımı)
- **Bergama** (bazı eski dosyalar)

### Yerel dış vekil
- [Bölge Şehri] merkezli pratisyenler — uzun süreli mahkeme ilişkisi avantaj
- İstanbul'dan büyük büro koordineli; günlük takip için yerel

### Sendika
- **[Sektör Sendikası]** — [Halka Açık İştirak] ana sendikası, agresif tutum
- **[Birincil sendika] — üretim sahası ana sendikası
- TİS müzakerelerinde geçmiş İSG davaları argüman

## In-house akış (İSG kazası sonrası, ilk 72 saat)

`/litigation-legal:isg-incident-response` skill'i detaylı runbook verir. Özet:

1. **0-1 saat:** Delil koruma, yasal bildirimler, üst yönetim, dış vekil mobilize
2. **1-24 saat:** Savcılık beklenti planlaması, çalışan vekalet, belge kontrol, iletişim
3. **24-72 saat:** Olay raporu inceleme, stratejik karar, KAP açıklama ([Halka Açık İştirak])

## Mevzuat MCP — temel maddeler

```
search_mevzuat(mevzuat_no="6331", mevzuat_tur="KANUN")  # İSG K.
search_mevzuat(mevzuat_no="6098", mevzuat_tur="KANUN")  # TBK
search_mevzuat(mevzuat_no="5237", mevzuat_tur="KANUN")  # TCK
search_mevzuat(mevzuat_no="2872", mevzuat_tur="KANUN")  # Çevre K.
search_mevzuat(mevzuat_no="4857", mevzuat_tur="KANUN")  # İş K.
search_mevzuat(mevzuat_no="5510", mevzuat_tur="KANUN")  # SGK K.
```

## Bağlantılı

- [HMK rehberi](hmk-rehberi.md)
- [Yargı MCP rehberi](yargi-mcp-rehberi.md)
- [Şirket profili → litigation-legal](../profiles/litigation-legal.md)
