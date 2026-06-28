# tax-legal - Skill Referans Kitapcigi

> Alan: Vergi hukuku - VUK, GIB ozelge, TP, KDV/OTV
> Toplam skill: 7
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /tax-legal:cold-start-interview (103 satir)
- /tax-legal:gib-ozelge-request (151 satir)
- /tax-legal:kdv-otv-iade-review (196 satir)
- /tax-legal:tax-litigation-prep (198 satir)
- /tax-legal:transfer-pricing-review (171 satir)
- /tax-legal:uzlasma-eval (175 satir)
- /tax-legal:vergi-incelemesi-response (152 satir)

---

## /tax-legal:cold-start-interview

---
name: cold-start-interview
description: >
  Tax pratiğini bilgisayara öğret — tax modeli (Mali İşler ana / Büyük 4 ortak /
  karma), dış vergi danışmanı + vergi avukatı paneli, eskalasyon eşikleri (özellikle
  uzlaşma yetkisi), aktif Danıştay davaları envanteri, yakıcı stres alanları
  (TP / KDV iade / ÖTV). 2dk hızlı veya 10dk tam mod.
user-invocable: true
---

# Cold-Start Interview — Tax Practice

## Amaç

Diğer skill'ler bu profil olmadan körce çalışır. Yeni kurulumda veya pratik değişikliğinde çalıştır.

## Modlar

Argümansız çağrılırsa sor:

> İki mod:
> - **Hızlı (2 dakika)** — 6 kritik soru
> - **Tam (10 dakika)** — 20+ soru, tüm profil
>
> Hangisini istersin? (`--redo` mevcut sıfırlar; `--check-integrations` sadece bağlantı testi)

## Hızlı mod (6 soru)

1. **Tax modeli:** Mali İşler ana / Büyük 4 ortak / Karma / İçeride tax ekibi var
2. **Hukukun rolü:** Sadece dava aşamasında / planlama dahil / tüm aşamalarda
3. **Birincil yakıcı stres:** TP / KDV iade / ÖTV / damga / karma
4. **Aktif Danıştay dava sayısı:** yaklaşık
5. **Büyük 4 firma:** PwC / Deloitte / EY / KPMG / başka
6. **Uzlaşma onay matrisi:** Mali İşler özerk mi, hukuk dahil mi, CFO'da mı

## Tam mod (20+ soru, batch'ler)

### Batch 1 — Tax pratik modeli
- Tax modeli + iç rol
- Mali İşler içinde dedicated vergi yöneticisi var mı
- Hukuk müşaviri devreye giriş eşiği (otomatik vs. çağrı üzerine)
- Yakıcı stres alanları (sıralı)
- Aktif vergi davaları envanteri (yaklaşık adet + tip)

### Batch 2 — Dış vergi danışmanı + avukat paneli
- Büyük 4 ana firma + sözleşme tipi (yıllık paket vs. iş başı)
- Transfer pricing dokümantasyon — hazırlayan, onaylayan
- YMM (Yeminli Mali Müşavir) — kim, hangi konularda
- Vergi davası dış avukat (Danıştay) — Ankara mı, İstanbul mı, uzman büro mu
- AYM bireysel başvuru için ayrı uzman var mı

### Batch 3 — Eskalasyon ve onay matrisi
- Özelge talebi onay
- İdari itiraz onay
- Tarhiyat öncesi/sonrası uzlaşma onay (tutar kademeli)
- Danıştay dava açma onay
- AYM bireysel başvuru onay
- VUK m. 359 kaçakçılık iddiasında ceza savunma

### Batch 4 — Sistem ve entegrasyonlar
- SAP ERP vergi modülü
- e-Beyanname / GİB İBİS portalı
- iManage / SharePoint vergi dosyaları
- Büyük 4 firma portal entegrasyonu
- Vergi dava case management

### Batch 5 — Halka açık ve özel
- Petkim KDV iade büyüklüğü (yıllık tahmin)
- STAR ÖTV mahsubu hacmi
- [Ana ortak / ilişkili taraf] intra-group işlem hacmi (TP risk)
- KAP açıklama tetikleyici tutar (büyük tarhiyat → özel durum açıklama)
- MASAK koordinasyon (yüksek tutarlı uluslararası işlem)

## Çıktı

```markdown
## ✓ Tax practice profile dolduruldu

**Doldurulan:**
- Tax modeli: [özet]
- Yakıcı stres: [özet]
- Outside panel: [özet]
- Eskalasyon: [özet]
- ...

**Hala [DOLDUR]:**
- [liste]

**Sonraki adım önerisi:**
- /tax-legal:transfer-pricing-review — yıllık TP dokümantasyon dönemi
- /tax-legal:vergi-incelemesi-response — Maliye inceleme geldi
- /tax-legal:tax-litigation-prep — aktif Danıştay dosyaları
- Manuel: ~/.claude/plugins/config/claude-for-legal/tax-legal/CLAUDE.md
```

## --check-integrations

1. **Yarg MCP** — test: `search_gib_decisions(arananKelime="transfer fiyatlandırma")` → cevap geliyor mu?
2. **Mevzuat MCP** — test: `search_mevzuat(mevzuat_no="213", mevzuat_tur="KANUN")` → VUK dönüyor mu?
3. **iManage** — test
4. **(SAP ERP)** — bağlantı raporu

Rapor formatı litigation-legal'daki ile aynı.

---

## /tax-legal:gib-ozelge-request

---
name: gib-ozelge-request
description: >
  GİB (Gelir İdaresi Başkanlığı) özelge (mukteza) talep dilekçesi hazırlama: VUK m.
  369 + Genel Tebliğ formatı, benzer özelgeleri Yarg MCP'den çekme, talep dilekçesi
  taslağı, beklenen cevap süresi (6-9 ay) ve risk yönetimi.
user-invocable: true
---

# GİB Özelge Talep Hazırlama

## Amaç

Vergi mevzuatında belirsiz bir konuda **bağlayıcı yorum** almak için GİB'den özelge talep edilir (VUK m. 369 + 395 Sıra No.lu VUK Genel Tebliği).

**Önemli:**
- GİB özelgesi **sadece talep eden mükellefi** bağlar (kişiye özel)
- Süre: ortalama 6-9 ay
- Olumsuz cevap halinde **idari itiraz yolu var değil**, ama **dava açılabilir**
- **Risk:** GİB olumsuz cevap verirse pozisyon zayıflar

## Destination check

- **Mali İşler iç değerlendirme** → "GİZLİDİR – HUKUK + MALİ İŞLER ÖZELGE TALEP DEĞERLENDİRMESİ"
- **GİB'e sunulacak dilekçe** → resmi format
- **Büyük 4 firma koordinasyon** → "TAX BRIEF"

## Adımlar

### 1. Özelge talep gerekli mi?

Sor:

> Bu konu için özelge talep etmek istiyorsun. Önce:
> 1. Konuda zaten var olan bir özelge var mı? → Yarg MCP'den ara
> 2. Cevap olumsuz çıkarsa ne kaybedersin? (özelge'siz pozisyon koru → kovuşturma riski; ya da farklı yaklaş)
> 3. Süre kritik mi? (6-9 ay beklemek mümkün mü?)

### 2. Yarg MCP — benzer özelge tarama

```
mcp__claude_ai_Yarg_MCP__search_gib_ozelge(
  arananKelime="<konu anahtar kelimeleri>"
)
```

Bulunan benzer özelgelerden:
- GİB'in yaklaşımı (genelde mükellefe karşı muhafazakar mı, esnek mi)
- Atıf edilen mevzuat
- Cevap argümantasyonu

### 3. Dilekçe taslağı

```markdown
GELİR İDARESİ BAŞKANLIĞI
[İlgili Vergi Dairesi Başkanlığı veya GİB Genel Müdürlüğü]
ANKARA / İSTANBUL

Konu: Mukteza Talebi — [konunun kısa tarifi]

Sayın Yetkilisi,

Şirketimiz **[Müvekkil]** [vergi kimlik no, sicil no, adres] olarak,
[konu] hususunda aşağıda açıklanan duruma ilişkin GİB görüşüne ihtiyaç duymaktayız.

I. FİİLİ DURUM

[İşlemin/konunun ayrıntılı tarifi — taraflar, tutar, sıklık, fiziksel veya ekonomik gerçekçilik]

II. HUKUKİ DEĞERLENDİRME

Konuyla ilgili mevzuat:
- [Kanun maddesi]
- [Tebliğ]
- [Genelge]

Şirketimiz görüşü: [...]

III. TALEP

Yukarıda açıklanan duruma ilişkin **GİB görüşünüzü** ve özelgenin tarafımıza
ibrazını talep ederiz.

Saygılarımızla,

[Yetkili imza]
[Müvekkil]
Tarih: GG.AA.YYYY

Ekler:
1. [İlgili belge]
2. [Sözleşme örneği — varsa]
3. [Benzer GİB özelge örnekleri — bizim pozisyonumuzu destekler]
```

### 4. Yarg MCP — Danıştay vergi içtihatı

Eğer özelge red gelirse dava açılır → şimdiden Danıştay eğilimini bil:

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="<ilgili>",
  arananKelime="<konu> mukteza GİB",
  baslangicTarihi="2022-01-01"
)
```

### 5. sektöre-özel notlar

- **Petkim ilgili özelge** — KAP açıklama tetikleyici olabilir (büyük mali etki)
- **TANAP işlem özelgesi** — hükümetlerarası anlaşma + GİB ortak görüşü
- **[Ana ortak / ilişkili taraf] intra-group** — özelge talep edersek Maliye'nin dikkati çekiyor, risk

### 6. Risk analizi

Özelge talep etmenin riskleri:
- **Olumsuz cevap = pozisyonu zayıflatır** (sonraki incelemede Maliye bu özelgeyi kullanabilir)
- **Bekleme süresi** (6-9 ay) operasyonel karar geciktirebilir
- **Konunun açığa çıkması** — özelge talep ettiğin işlem GİB'in dikkatini çeker

## Çıktı

```markdown
[ÜST BAŞLIK]

# GİB Özelge Talep Değerlendirme — [Konu]

## ⚠️ İnceleyen notu
- **Tavsiye:** Özelge TALEP EDİLSİN / EDİLMESİN / FARKLI YOL
- **Kaynaklar:** Yarg MCP (benzer özelge [N]); Mevzuat MCP (madde [N])
- **Olumlu/olumsuz cevap olasılığı:** [tahmin]
- **Süre tahmini:** [6-9 ay]
- **Reviewer karar bekleyen:** N adet

## Mevcut özelge taraması (Yarg MCP'den)
[tablo: özelge no, tarih, konu, sonuç, bizim için anlamı]

## Özelge talep dilekçesi taslağı
[yukarıdaki şablon — doldurulmuş]

## Risk değerlendirmesi
[olumsuz cevap senaryosu + alternatif yollar]

## Sonraki adımlar

> 1. Dilekçeyi GİB'e gönder — Mali İşler imza
> 2. Hukuk dava planı paralel hazırla — olumsuz cevap senaryosuna
> 3. Büyük 4 ile koordinasyon — onların görüşü
> 4. Bekle ve izle — 6-9 ay
> 5. Farklı yol — Büyük 4'ün muktezasız tutarlı uygulaması (risk al)
```

---

## /tax-legal:kdv-otv-iade-review

---
name: kdv-otv-iade-review
description: >
  KDV iadesi (Petkim ihracat) ve ÖTV mahsubu/iadesi ([büyük enerji tesisi] akaryakıt
  ihracat) için iade dosyası hazırlık review: KDVK m. 32 + m. 9 KDV iade rejimi,
  ÖTV m. 5 ihracat istisnası, YMM raporu gereksinimi, Maliye'nin red gerekçesi
  analizi, dava prep.
user-invocable: true
---

# KDV / ÖTV İade Review

## Tetik

İki ana akış:
1. **Petkim KDV iadesi** — petrokimya ihracatı sonucu yüksek tutarlı KDV iade talebi
2. **[büyük enerji tesisi] ÖTV mahsubu/iadesi** — akaryakıt ihracatı sonucu ÖTV mahsubu

## Destination check

- **Mali İşler iç değerlendirme** → "GİZLİDİR – HUKUK + MALİ İŞLER DAHİLİ İADE NOTU"
- **YMM (Yeminli Mali Müşavir) firmasıyla koordinasyon** → "TAX BRIEF"
- **Maliye'ye sunulacak iade talep / itiraz dilekçesi** → resmi format
- **Dış vergi avukatı (iade reddi → dava)** → "VERGİ DAVA BRIEF"

## KDV iadesi (KDVK m. 32 + 9)

### Genel rejim
- **m. 32 — İhracat istisnası:** Mal/hizmet ihracatı KDV'den müstesna
- **m. 9 — KDV iadesi:** İndirim hakkı oluşmayan KDV iade alınır
- İhracatçı KDV'yi mahsuben veya nakden iade alır

### Süreç
1. **Beyanname** — ay/dönem sonu KDV beyannamesinde iade tutarı belirlenir
2. **YMM raporu** — Yeminli Mali Müşavir tasdiki gerekli (kademe tutar üstü)
3. **Maliye inceleme** — iade talebi otomatik incelemeye girer
4. **İade kararı** — onay (nakit/mahsuben), red, veya bekletme

### Maliye'nin red gerekçeleri (tipik)
- Faturalar usulüne uygun değil (gerçek fatura kontrolü)
- KDV indirimi geçerli değil (KDVK m. 30 — indirim sınırı)
- İhracat fiilen gerçekleşmedi / muvazaalı
- İlişkili kişi işlemi (TP riski)
- YMM raporu eksik/hatalı

### [Müvekkil] Petkim için özel
- Yıllık iade tutarı muhtemelen **milyarlık TL** (yüksek tutar = uzun inceleme)
- Maliye bekletme rejimi: 6-18 ay normal, daha uzun olabilir
- Bekletme süresince zaman değeri (faiz) kaybı
- **KAP açıklama:** Önemli iade kararı (büyük tutar) açıklama gerekir mi?

### Dava alternatifi
İade reddi/bekletme zarara yol açıyorsa:
- **İYUK m. 27 — Yürütmenin durdurulması** Maliye'nin bekletme kararına karşı
- **Davanın açılması** Maliye'ye süresinde başvurmamış olma riskini ortadan kaldırır

## ÖTV mahsubu / iadesi (4760 sayılı)

### Genel rejim
- **m. 5 — İhracat istisnası:** İhraç edilen akaryakıt ÖTV'den müstesna
- **Mahsuben iade:** Sonraki dönem ÖTV borcundan mahsup
- **Nakden iade:** Süreç KDV'den daha karmaşık (ÖTV teknik özellikler — fiziksel ürün tespiti)

### Süreç
1. **STAR ihracat:** Akaryakıt ihracatı (gemiyle, boru hattıyla) → ihracat beyannamesi
2. **Gümrük + Maliye koordinasyon** — fiziksel teslim ispatı (gümrük çıkış belgesi)
3. **ÖTV mahsubu beyannamesi** — sonraki dönem ÖTV beyannamesinde mahsup
4. **Maliye inceleme** — ürün miktarı, kalite, fiili ihracat kontrolü
5. **Mahsup veya iade**

### Maliye'nin red gerekçeleri
- Ürün miktarı uyumsuz (fiziksel ile beyanlı)
- Gümrük çıkış belgesi eksik
- Antrepo / depo dökümanları yetersiz
- İlişkili kişiye satış (TP riski)
- Petrol piyasası mevzuatı uyum sorunu (EPDK)

### [Müvekkil] STAR için özel
- Aylık ihracat hacmi yüksek → süreç sürekli işliyor
- EPDK lisans bilgileri ile uyum (5015 Petrol Piyasası K.)
- Gümrük müşavirliği koordinasyonu kritik
- **Devalüasyon etkisi:** Bekletme sürecinde ÖTV TL değer kaybı

## Adımlar

### 1. Hangi iade?

> Bu review hangi iade için?
> A. Petkim KDV iadesi
> B. STAR ÖTV mahsubu/iadesi
> C. Diğer (Bursagaz/Kayserigaz dönemi KDV, vs.)

### 2. Aşama tespiti

> Şu an hangi aşamadayız?
> A. İade talep dilekçesi henüz hazırlanıyor
> B. Maliye inceleme başladı/sürüyor
> C. Maliye red kararı verdi/iade reddi geldi
> D. Bekletme uzun sürüyor, müdahale gerek

### 3. Dokümantasyon checklist (Petkim KDV iade)

- [ ] Aylık KDV beyannameleri
- [ ] İndirim KDV listesi (gerçek faturalar)
- [ ] İhracat faturaları + ihracat beyannamesi + gümrük çıkış belgesi
- [ ] YMM raporu (tasdiki)
- [ ] İndirilen KDV'nin maliyetle uyumu (alım sözleşmeleri)
- [ ] İlişkili kişi işlemleri ayrıştırması (TP dokümantasyonu paralel)

### 4. Dokümantasyon checklist (STAR ÖTV mahsubu)

- [ ] Aylık ÖTV beyannameleri
- [ ] Üretim raporları (rafineri çıkış miktarı)
- [ ] İhracat beyannameleri + gümrük çıkış belgeleri
- [ ] Antrepo / depo dökümanları
- [ ] EPDK lisans bilgileri (lisans kapsam uyumu)
- [ ] Müşteri sözleşmeleri (ilişkili-bağımsız ayrım)

### 5. Yarg MCP — emsal arama

```
# KDV iade reddi davaları
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="3. Daire",
  arananKelime="KDV iade ihracat petrokimya bekletme",
  baslangicTarihi="2022-01-01"
)

# ÖTV mahsubu davaları
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="3. Daire",
  arananKelime="ÖTV mahsup akaryakıt ihracat istisna",
  baslangicTarihi="2022-01-01"
)

# GİB özelgeleri
mcp__claude_ai_Yarg_MCP__search_gib_ozelge(
  arananKelime="KDV iade petrokimya"
)
```

### 6. Mali etki hesabı

- **Beklenen iade tutarı:** [TL]
- **Bekletme süresi (tahmin):** N ay
- **Zaman değeri kaybı** (yıllık faiz × bekletme): [TL]
- **Dava açma maliyeti** (vekalet, harç): [TL]
- **Dava kazanma olasılığı:** %X (emsal kararlardan)

### 7. sektöre-özel kontroller

- [ ] **Petkim yıllık KDV iadesi > [X] TL** → KAP açıklama riski + IR Başkanlığı
- [ ] **Müşteri portföyü:** İlişkili kişi satışları ayrı raporlanmış mı (TP)
- [ ] **EPDK lisans uyumu:** Lisans kapsamında ihracat yapıldı mı (STAR)
- [ ] **Gümrük belgesi** orijinalleri arşivde mi
- [ ] **YMM firma** çıkar çatışması yok mu (büyük tutarda YMM/firma değişikliği etkisi)

## Çıktı

```markdown
[ÜST BAŞLIK]

# KDV/ÖTV İade Review — [Dönem / Tip]

## ⚠️ İnceleyen notu
- **İade tipi:** Petkim KDV / STAR ÖTV / Diğer
- **Aşama:** A/B/C/D
- **Beklenen tutar:** [TL]
- **Tavsiye:** İade talep tamamla / İtiraz dilekçesi sun / Dava aç / Bekleme kabul
- **Süre kalan:** [N gün — dava açılacaksa İYUK m. 7]
- **Kaynaklar:** Yarg MCP (Danıştay [N], GİB özelge [N])
- **KAP:** [N/A / hazırlanıyor]
- **Reviewer bekleyen:** N adet

## Dokümantasyon checklist
[checklist — eksik kalemler kırmızı]

## Maliye red gerekçesi (varsa) analizi
[gerekçe + savunma argümanı]

## Emsal Danıştay kararları
[Yarg MCP'den]

## Mali etki ve karar matrisi
[bekletme / dava / itiraz karşılaştırma]

## Sonraki adımlar

> 1. **YMM raporu tamamla** (eksik ise)
> 2. **İtiraz dilekçesi taslak** — Maliye'ye karşı
> 3. **Dava prep** — `/tax-legal:tax-litigation-prep`
> 4. **CFO eskalasyon notu** (büyük tutar)
> 5. **Daha fazla bilgi** — [...]

**One question I'd ask:** [örn. "[halka açık iştirak] KAP'a iade beklentisini açıklamış mı? Beklenti karşılanamazsa yatırımcı algısı etkilenebilir."]
```

---

## /tax-legal:tax-litigation-prep

---
name: tax-litigation-prep
description: >
  Danıştay vergi davası hazırlık: İYUK m. 7 (30 gün dava süresi) kontrolü, görevli
  daire seçimi (3.=KDV/ÖTV, 4.=Kurumlar, 7.=Damga, 9.=Vergi cezası), dava dilekçesi
  taslağı, yürütmenin durdurulması talebi (İYUK m. 27), emsal Danıştay kararları.
  Dış vergi avukatı brief'i ile entegre.
user-invocable: true
---

# Tax Litigation Preparation — Danıştay Vergi Davası

## ⏰ ÖN-KONTROL — Süre

Bu skill her çalıştırıldığında **ilk işlem süre hesabı**:

> Vergi tarhiyat / idari para cezası tebliğ tarihi nedir?
> İYUK m. 7 — **30 gün** içinde Danıştay'a iptal davası açılmalı.
> Bu süre **hak düşürücü**dür.

Eğer kalan süre < 5 gün → 🔴 ACİL — dış vekille derhal koordinasyon.

## Destination check

- **Mali İşler + Hukuk değerlendirme** → "GİZLİDİR – HUKUK + MALİ İŞLER VERGİ DAVA STRATEJİ"
- **Dış vergi avukatı brief'i** → "VERGİ DAVA BRIEF – AVUKATLIK K. m. 36 KAPSAMINDA"
- **Danıştay'a sunulacak dilekçe taslağı** → resmi format, "TASLAK" + dış vekil onayı sonrası

## Adımlar

### 1. Görevli daire tespiti

| Daire | Konu |
|---|---|
| **Danıştay 3. Daire** | KDV, ÖTV, gümrük vergileri |
| **Danıştay 4. Daire** | Gelir ve kurumlar vergisi (yıllık beyanname kaynaklı) |
| **Danıştay 7. Daire** | Damga vergisi, banka muameleleri, MTV, harçlar |
| **Danıştay 9. Daire** | Vergi cezaları (her vergi türü için ceza), tarhiyat, vergi kaçakçılığı |
| **Vergi Daireleri DDK** | Daire çelişkilerini birleştirme |

**[Müvekkil] örnek:**
- Petkim KDV iadesi reddi → **3. Daire**
- STAR ÖTV mahsubu reddi → **3. Daire**
- TP tarhiyatı (KVK m. 13) → **4. Daire**
- Büyük sözleşme damga vergisi tarhiyatı → **7. Daire**
- Vergi ziyaı cezası → **9. Daire**

### 2. Dava dilekçesi şablonu (İYUK m. 3)

```markdown
DANIŞTAY [X.] DAİRESİ BAŞKANLIĞINA
ANKARA

DAVACI:
[Müvekkil] — [VKN, sicil, adres]
Vekili: [Av. ad, baro sicil, adres, KEP]

DAVALI:
T.C. Maliye Bakanlığı / [Vergi Dairesi Başkanlığı]
Vekili: [Bakanlık genel olarak Hazine ve Maliye Bakanlığı vekili]

DAVA KONUSU:
[Tarihli, sayılı] tarhiyat işlemi / idari para cezası kararının iptali ile yürütmenin durdurulması talebidir.

İŞLEMİN TARİFİ:
[Maliye'nin tebliğ ettiği belge — tarih, sayı, tutar, ceza]
Tarafımıza tebliğ tarihi: GG.AA.YYYY
Dava açma süresi: [tebliğden 30 gün sonu — tarih]

I. OLAYLAR

[Tarihsel olarak — vergi konusu işlem, beyanname, inceleme, tarhiyat]

II. HUKUKİ DAYANAĞIMIZ

A. Tarhiyatın hukuki dayanaktan yoksun olduğu
   [Argüman 1] — Dayanak: [VUK m. X, KVK m. Y, KDVK m. Z]

B. [Argüman 2] — [Emsal Danıştay kararı: `[Yarg MCP — danistay — esas/karar — GG.AA.YYYY]`]

C. [Argüman 3 — yedek]

III. YÜRÜTMENİN DURDURULMASI TALEBİMİZ (İYUK m. 27)

Aşağıdaki sebeplerle yürütmenin durdurulması talep edilmektedir:
1. [Telafisi güç zarar] — örn. tahsil edilirse şirket nakit akışı bozulur, üretim etkilenir
2. [Açık hukuka aykırılık] — yukarıdaki argümanlardan en güçlüsü

IV. SONUÇ VE TALEP

Yukarıdaki açıklamalar ışığında:
1. Yürütmenin durdurulmasına,
2. [İşlemin/cezaın] iptaline,
3. Yargılama gideri ve vekalet ücretinin davalıya yüklenmesine,

karar verilmesi saygıyla arz ve talep olunur.

Tarih: GG.AA.YYYY

Davacı Vekili: [imza]

EKLER:
1. Vekaletname
2. Tarhiyat kararı (tebliğ örneği)
3. [İlgili sözleşme/belge]
4. [Emsal Danıştay kararları]
```

### 3. Yürütmenin durdurulması (İYUK m. 27) — KRİTİK

Davacıya **otomatik tahsil tehiri** sağlamaz. Talep edilmesi şart. Şartlar:
- **Telafisi güç veya imkansız zararlar doğacağı**
- **İdari işlemin uygulanması halinde açıkça hukuka aykırılığın var olduğu**

İkisi de gerekli. Yüksek tutarlı tarhiyatlarda **telafisi güç zarar** kolay ispatlanır (nakit etkisi, sektör operasyonu).

**Tehir-i icra (AATUHK)** — vergi tahsil aşamasına girdiyse ayrı bir paralel yol.

### 4. Yarg MCP — emsal Danıştay kararları

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="<seçilen daire>",
  arananKelime="<dava konusu>",
  baslangicTarihi="2022-01-01"
)
```

Ayrıca **VDDK kararları** (birleştirici):

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="Vergi Dava Daireleri Kurulu",
  arananKelime="<konu>",
  baslangicTarihi="2020-01-01"
)
```

### 5. sektöre-özel notlar

- **Tutar > 10M TL** → CFO + Başkan + CEO eskalasyon
- **Petkim ilgili** → KAP açıklama (önemli dava — SPK Tebliğ II-15.1)
- **Yüksek tutarlı Maliye davası** → MASAK bildirim eşiği? (UNSCR/AML kontrolleri)
- **AYM bireysel başvuru** — Danıştay temyizi reddi sonrası mülkiyet hakkı ihlali argümanı

### 6. Dış vergi avukatı brief'i

`/litigation-legal:outside-counsel-brief` pattern'ını kullan ama vergi-spesifik:

- **Daire deneyimi:** Bu büronun ilgili daire ile geçmişi (oranı?)
- **VDDK kararına itiraz deneyimi**
- **Tarihsel kazanma oranı (büronun)** — kendileri verir mi?

## Çıktı

```markdown
[ÜST BAŞLIK]

# Tax Litigation Prep — [Tarhiyat sayı / Konu]

## ⚠️ İnceleyen notu
- **Tebliğ tarihi:** GG.AA.YYYY
- **Dava süresi sonu:** GG.AA.YYYY (kalan: N gün) 🔴 🟠 🟡
- **Görevli daire:** Danıştay [X.] Daire
- **Yürütmenin durdurulması talep edilecek:** evet
- **Kaynaklar:** Yarg MCP (Danıştay [N] emsal); Mevzuat MCP (VUK/KDVK m. [N])
- **Eskalasyon zinciri:** [tetiklendi?]
- **KAP açıklama:** [N/A / hazırlanıyor]
- **Reviewer bekleyen:** N adet

## Tarhiyatın özeti

| Kalem | Maliye iddiası | Bizim pozisyon | Tutar |
|---|---|---|---|
| ... | ... | ... | ... |

## Hukuki argümanlar
[A, B, C — emsal kararlarla]

## Dava dilekçesi taslağı (dış vekil revize için)
[yukarıdaki şablon]

## Yürütmenin durdurulması analizi
[telafisi güç zarar + hukuka aykırılık]

## Emsal Danıştay kararları
[Yarg MCP'den çıkan tablolar]

## Sonraki adımlar

> 1. **Dış vergi avukatı brief'i** — `/litigation-legal:outside-counsel-brief` (vergi davası için)
> 2. **CFO + Başkan eskalasyon paketi**
> 3. **KAP açıklama metni** (Petkim ilgili büyük tarhiyat)
> 4. **Uzlaşma paralel değerlendirme** — `/tax-legal:uzlasma-eval` (alternatif yol)
> 5. **Daha fazla bilgi** — [...]

**One question I'd ask:** [örn. "Aynı daire son 12 ayda benzer [Müvekkil]/sektör davalarında nasıl karar verdi? Maliye lehine eğilim varsa strateji değişir."]
```

---

## /tax-legal:transfer-pricing-review

---
name: transfer-pricing-review
description: >
  Intra-group işlem fiyatlandırması analizi: [Ana ortak / ilişkili taraf] ile ham petrol alımı, royalty,
  hizmet ücretleri için KVK m. 13 (örtülü kazanç dağıtımı) + OECD Transfer Pricing
  Guidelines uyum kontrolü. Yıllık TP dokümantasyon çıkarma, emsallere uygun fiyat
  analizi, Maliye inceleme öncesi pozisyon hazırlama.
user-invocable: true
---

# Transfer Pricing Review

## Matter context

TP genellikle **yıllık dokümantasyon dönemi** (kurumlar vergisi beyanname öncesi, Nisan) veya **özel işlem-bazlı** çalışılır.

> Bu TP review: (a) yıllık dokümantasyon hazırlık mı, (b) belirli bir intra-group işlem değerlendirmesi mi, (c) Maliye TP incelemesine cevap mı?

## Destination check

- **Mali İşler iç pozisyon** → "GİZLİDİR – HUKUK + MALİ İŞLER DAHİLİ TP NOTU"
- **Büyük 4 firma briefing** → "TAX BRIEF – CONFIDENTIAL"
- **Maliye'ye sunulacak dokümantasyon** → resmi format, üst başlık çıkar
- **CEO/CFO eskalasyon notu** → 1 sayfa executive summary

## Amaç

**KVK m. 13 — Örtülü Kazanç Dağıtımı:** İlişkili kişilerle (ana ortak, bağlı ortaklar, yöneticiler, ortak hisseli şirketler) yapılan işlemlerde fiyat **emsallere uygun (arm's length)** olmalı. Aksi halde:
- Aradaki fark **örtülü kazanç dağıtımı** sayılır
- Kurumlar vergisi matrahına eklenir
- Vergi ziyaa cezası + gecikme zammı
- Tekrarlı ise **kaçakçılık (VUK m. 359)** iddiası olabilir

**sektöre-özel risk üçlüsü:**
1. **Ham petrol alımı ([Ana ortak / ilişkili taraf] → [büyük enerji tesisi])** — yüksek tutar, fiyat dalgalanması (Brent benchmark)
2. **Royalty / lisans / marka** ([Ana ortak / ilişkili taraf] → [Müvekkil] + bağlı şirketler)
3. **Yönetim hizmeti, IT, mali danışmanlık** ([Ana ortak / ilişkili taraf] → [Müvekkil])

## Adımlar

### 1. İşlemleri envanterle

| İlişkili kişi | İşlem tipi | Yıllık tutar (TL) | Para birimi | Sıklık |
|---|---|---|---|---|
| [Müvekkil] (Bakü) | Ham petrol satın alım | [...] | USD | sürekli |
| [Müvekkil] | Royalty | [...] | USD | yıllık |
| [Müvekkil] | Yönetim hizmeti | [...] | USD | yıllık |
| Bağlı şirket X | Intra-group hizmet | [...] | TL | [...] |

**Eşik kontrolü:** Bir ilişkili işlem ≥ 50.000 TL ise dokümantasyon zorunlu (Kurumlar Vergisi Genel Tebliği).

### 2. Yöntem seçimi (5 yöntem)

KVK m. 13/3 ve OECD TPG:

| Yöntem | Uygulama | [Müvekkil] örneği |
|---|---|---|
| **Karşılaştırılabilir Fiyat (KKF / CUP)** | Aynı/benzer mal/hizmet bağımsız işlemi | Ham petrol — Brent/Urals/Azeri Light benchmark |
| **Maliyet Artı (Cost Plus)** | Maliyet + makul kâr marjı | Yönetim hizmeti, IT |
| **Yeniden Satış Fiyatı (RPM)** | Satış fiyatı - brüt marj | Ticaret/distribütör işlemleri |
| **Kâr Bölüşümü (Profit Split)** | Toplam kârın paylaşımı | Karmaşık entegre işlemler (TANAP gibi) |
| **İşlemsel Net Kâr Marjı (TNMM)** | Net kâr marjı karşılaştırma | Yaygın — bilgi yetersiz ise |

**[Müvekkil] önerisi:** Ham petrol için **KKF** (Brent + Azeri Light premium) en güçlü; royalty için **TNMM**; hizmet için **Maliyet Artı**.

### 3. Emsal analizi (benchmark study)

- **Bağımsız işlem verileri:** S&P Platts, Argus Media, IHS Markit (petrol fiyatları)
- **Royalty benchmarks:** RoyaltyStat, ktMINE, RoyaltySource
- **Hizmet benchmark:** Bureau van Dijk Amadeus (Avrupa), TP Catalyst (Refinitiv)

**Sorun:** Bu veri tabanlarına [Müvekkil]'ın **lisans abonelikleri** var mı? — `[DOLDUR]`. Yoksa Büyük 4 firma genelde abone ve raporu hazırlar.

### 4. Yarg MCP — GİB özelge + Danıştay emsali

```
mcp__claude_ai_Yarg_MCP__search_gib_ozelge(
  arananKelime="transfer fiyatlandırma ham petrol ilişkili"
)

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="4. Daire",  # Kurumlar vergisi
  arananKelime="örtülü kazanç dağıtımı transfer pricing",
  baslangicTarihi="2022-01-01"
)
```

GİB özelgeleri TP konusunda **yorumlama kaynağı**. Önceki Maliye yaklaşımını öğren.

### 5. OECD TPG ve BEPS Action

Türkiye OECD üyesi, OECD TPG'yi referans alır:
- **OECD TPG 2022** (güncel revizyon)
- **BEPS Action 8-10** — Intangibles, services, financial transactions
- **BEPS Action 13** — Country-by-Country Reporting (CbCR — [Müvekkil] dahil)

Atıf: `[OECD TPG — Chapter X — 2022]`, `[BEPS Action — sayı]`.

### 6. [Ana ortak / ilişkili taraf]-özel kontroller

- [ ] **Azerbaycan-Türkiye Çifte Vergilendirmeyi Önleme Anlaşması** (1994) — varsayılan tutar ve emsal
- [ ] **TANAP işlem rejimi** — hükümetlerarası anlaşma kapsamında özel tarife
- [ ] **[halka açık iştirak] KAP açıklama** — büyük tarhiyat halinde özel durum
- [ ] **MASAK** — yüksek tutarlı uluslararası işlem (yıllık 1B USD+ ham petrol)
- [ ] **OFAC/AB yaptırım** — Azerbaycan ile işlem ama bağlantılı taraf kontrolü

### 7. Dokümantasyon paketi (yıllık)

Kurumlar Vergisi Genel Tebliği uyarınca:

- **Master File** — grup yapısı, intra-group işlem haritası (BEPS Action 13)
- **Local File** — [Müvekkil] spesifik: işlemler, yöntem, emsal analizi, fonksiyonel analiz
- **Country-by-Country Reporting (CbCR)** — global [Müvekkil] (Bakü ana şirket tarafından)

### 8. Pozisyon paketi (Maliye savunmasına hazır)

Her intra-group işlem için:
- İşlem tarifi (ne, ne kadar, hangi koşullarda)
- Fonksiyonel analiz (kim ne yapıyor, kim risk alıyor)
- Seçilen yöntem + gerekçe
- Emsal işlem aralığı (interquartile range)
- Test sonucu (fiyat aralık içinde mi)
- Sapma varsa gerekçe (örn. piyasa koşulları)

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Transfer Pricing Review — [Dönem / İşlem]

## ⚠️ İnceleyen notu
- **Kapsam:** Yıllık dokümantasyon / Spesifik işlem / Maliye inceleme cevabı
- **Risk seviyesi:** 🔴/🟠/🟡/🟢
- **Kaynaklar:** Yarg MCP (GİB özelge [N], Danıştay [N]); OECD TPG referansları
- **Mali İşler koordinasyon:** [✓/✗ + kim]
- **CFO bilgi:** [✓/✗]
- **Reviewer karar bekleyen:** N adet

## İlişkili işlem envanteri
[tablo]

## Yöntem seçimi ve gerekçe
[seçilen yöntem + alternatif değerlendirme]

## Emsal analizi
[benchmark sonuçları + aralık]

## [Ana ortak / ilişkili taraf]-özel notlar
[BIT anlaşması, TANAP rejimi, KAP, MASAK, yaptırım]

## Risk değerlendirmesi
| İşlem | Risk | Maliye saldırı vektörü | Savunma |
|---|---|---|---|
| ... | ... | ... | ... |

## Dokümantasyon checklist
- [ ] Master File hazır
- [ ] Local File hazır
- [ ] CbCR (global [Müvekkil] tarafından)
- [ ] Pozisyon paketi (savunmaya hazır)

## Sonraki adımlar

> 1. **Büyük 4 firma ile koordinasyon** — dokümantasyon revizyon
> 2. **CFO bilgi notu** — yıllık TP raporu özet
> 3. **Maliye'ye proaktif özelge talebi** — risk yüksek bir işlem için
> 4. **Daha fazla bilgi** — şu noktaları araştırmadan ilerleyemem: [...]

**One question I'd ask:** [örn. "Maliye RIA programında [Müvekkil]'ın yer aldığına dair bir gösterge var mı? Yıllık denetim seçim olasılığını bilmek strateji değiştirir."]
```

---

## /tax-legal:uzlasma-eval

---
name: uzlasma-eval
description: >
  Maliye uzlaşma teklifi geldi veya uzlaşma talebi verilecek — değerlendirme:
  tarhiyat öncesi (VUK Ek m. 11, cezada %50'ye kadar indirim) vs. tarhiyat sonrası
  (Ek m. 1, cezada %75'e kadar indirim) karar; kabul edilebilir vergi/ceza aralığı;
  Danıştay dava alternatifiyle maliyet karşılaştırma; [Müvekkil] onay zinciri.
user-invocable: true
---

# Uzlaşma Değerlendirme (VUK Ek m. 1 / Ek m. 11)

## Tetik

İki senaryo:
1. Maliye inceleme tutanağı/raporu sonrası **tarhiyat öncesi uzlaşma şansı** (Ek m. 11)
2. Tarhiyat tebliğ edildi, **30 gün içinde tarhiyat sonrası uzlaşma talep** edilebilir (Ek m. 1)

## Destination check

- **CFO + Hukuk + Mali İşler iç değerlendirme** → "GİZLİDİR – UZLAŞMA STRATEJİ NOTU"
- **CEO/Başkan eskalasyon** (büyük tutar) → 1 sayfa exec summary
- **Maliye'ye uzlaşma talep dilekçesi** → resmi format

## Karşılaştırma — Ek m. 11 vs Ek m. 1

| Özellik | Tarhiyat öncesi (Ek m. 11) | Tarhiyat sonrası (Ek m. 1) |
|---|---|---|
| **Süre** | İnceleme raporu sonrası, tarhiyat öncesi | Tarhiyat tebliğinden 30 gün |
| **Cezada indirim potansiyeli** | %50'ye kadar | **%75'e kadar** |
| **Pazarlık esnekliği** | Yüksek (henüz tarhiyat yapılmadı) | Düşük (tutar kesinleşmiş) |
| **Risk** | Maliye agresif tutum sergileyebilir | Sonraki dava süresi kaçırılabilir |
| **Strateji** | Hızlı çözüm istiyorsa | Pazarlık + dava seçeneği aksamadan ise |

⚠️ **KRİTİK:** Tarhiyat sonrası uzlaşma için başvuru = dava süresi durmaz. Uzlaşma sağlanmazsa "uzlaşmama tutanağı" tarihinden itibaren dava süresi devam eder ama **30 gün hesabı tebliğden başlar, uzlaşma için harcanan gün bu süreden düşülür** (VUK Ek m. 4). Çok az süre kalabilir.

## Adımlar

### 1. Hangi aşamadayız?

> Maliye'den gelen son belge nedir?
> A. İnceleme raporu (tarhiyat öncesi) — Ek m. 11 aktif
> B. Tarhiyat tebliği (vergi/ceza belirlendi) — Ek m. 1 aktif
> C. Uzlaşma toplantı çağrısı (başvurduk) — pazarlık aşaması

### 2. Tutar maruziyeti

| Kalem | Maliye iddiası | Tutar |
|---|---|---|
| Asıl vergi farkı | [...] | [...] |
| Vergi ziyaı cezası (VUK m. 344) | [%X] | [...] |
| Usulsüzlük cezası | [...] | [...] |
| **TOPLAM** | | [...] |

### 3. Uzlaşma indirim hesabı

**Tarhiyat öncesi (Ek m. 11):**
- Vergi: pazarlığa açık (genelde %0-30 indirim)
- Ceza: %50'ye kadar indirim
- Gecikme zammı: durdurulur (uzlaşma tarihine kadar)

**Tarhiyat sonrası (Ek m. 1):**
- Vergi: pazarlığa açık (daha az esneklik)
- Ceza: **%75 indirim** (resmi tarife)
- Gecikme zammı: uzlaşmaya kadar işler

### 4. Dava alternatifi maliyet karşılaştırma

| Senaryo | Maliyet |
|---|---|
| Uzlaşma (Ek m. 11 ile) | Vergi pazarlık × X% + Ceza %50 + zaman ~1-3 ay |
| Uzlaşma (Ek m. 1 ile) | Vergi pazarlık × X% + Ceza %25 + zaman ~3-6 ay |
| Danıştay dava (kazanırsa) | %0 + faiz iade (geç) + vekalet ücreti karşı tarafa |
| Danıştay dava (kaybederse) | %100 vergi + %100 ceza + gecikme + dava masrafı + vekalet |
| Karma — uzlaş + dava | [kombinasyon] |

**Kazanma olasılığı tahmini:** Yarg MCP'den emsal kararlara bakarak.

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="<ilgili>",
  arananKelime="<konu>",
  baslangicTarihi="2022-01-01"
)
```

### 5. Kabul edilebilir uzlaşma aralığı

- **Tabakalı hesap:** En düşük (Maliye'nin kabul edebileceği) ve en yüksek (bizim red noktamız) arasında.
- **Anchor:** Maliye'nin ilk teklifi vs. son teklif görüşülmek için.
- **Walk-away noktası:** Bu tutarın üstünde uzlaşma KABUL EDİLMEZ, dava açılır.

### 6. [Müvekkil] onay matriksi

| Tutar | Yetkili |
|---|---|
| < 1M TL | Mali İşler Müdürü + Hukuk Counsel |
| 1M - 10M TL | CFO (Hasanov) + Hukuk Direktörü |
| 10M - 100M TL | CFO + CEO |
| > 100M TL | CEO + YK |

**Tutardan bağımsız eskalasyon:**
- TP tarhiyatı ([Ana ortak / ilişkili taraf] ilgili) → CEO + Başkan
- Petkim ilgili → KAP açıklama kontrolü + IR Başkanlığı
- VUK m. 359 kaçakçılık iddiası → ceza avukatı + CEO + YK

### 7. Uzlaşma talep dilekçesi

```markdown
[Vergi Dairesi Başkanlığı] [Uzlaşma Komisyonu]

Konu: Uzlaşma Talebi (VUK Ek m. 11 / Ek m. 1)

[Tarih, sayı] sayılı [tarhiyat / inceleme raporu] hakkında, vergi ve ceza
tutarları üzerinde uzlaşmaya varmayı talep ederiz.

İlgili işlem: [tarif]
Uzlaşmayı talep eden tutar: [...]

[Yetkili imza]
[Müvekkil]
Tarih: GG.AA.YYYY
```

### 8. Uzlaşma toplantısına hazırlık

- **Pozisyon paketi:** Hukuki argümanlar, emsal kararlar (bizim lehimize)
- **Tutar pozisyonu:** Tabaka açık, walk-away noktası net
- **Kim katılır:** Genelde Mali İşler + Hukuk Counsel + dış vergi danışmanı (Büyük 4)
- **Yetki dökümanı:** Uzlaşma kararı için yetki belgesi (yetkili tutar limiti ile)

## Çıktı

```markdown
[ÜST BAŞLIK]

# Uzlaşma Değerlendirme — [Tarhiyat sayı / Konu]

## ⚠️ İnceleyen notu
- **Aşama:** Ek m. 11 (öncesi) / Ek m. 1 (sonrası)
- **Süre:** [...] (kalan: N gün)
- **Tavsiye:** UZLAŞMA ÖNERİLİR / ÖNERİLMEZ / KARMA STRATEJİ
- **Kabul edilebilir aralık:** [TL min - TL max]
- **Yetki:** [Counsel/Direktör/CFO/CEO]
- **Kaynaklar:** Yarg MCP (Danıştay [N] emsal); Mevzuat MCP
- **KAP:** [N/A / gerekli]
- **Reviewer bekleyen:** N adet

## Maliye iddiası vs. [Müvekkil] pozisyonu
[tablo]

## Uzlaşma indirim hesabı
[Ek m. 11 vs Ek m. 1 karşılaştırma]

## Dava alternatifi karşılaştırma
[maliyet matrisi + kazanma olasılığı]

## Önerilen uzlaşma aralığı
**Hedef:** [TL]
**Walk-away:** [TL]
**Müzakere stratejisi:** [...]

## Uzlaşma talep dilekçesi (taslak)
[şablon — doldurulmuş]

## Sonraki adımlar

> 1. **Uzlaşma talep dilekçesini Maliye'ye sun** — yetki belgesi ile
> 2. **CFO eskalasyon notu** — pozisyon ve walk-away onayı
> 3. **Dış vergi danışmanı brief** — toplantıya katılım için
> 4. **Dava paralel hazırlık** — `/tax-legal:tax-litigation-prep` (uzlaşılmazsa)
> 5. **Bekle** — Maliye karşı teklif gönderebilir

**One question I'd ask:** [örn. "Maliye komisyon üyesi geçmişte aynı tip vergi davalarında esnek mi katı mı? Bilgi varsa pozisyon ona göre."]
```

---

## /tax-legal:vergi-incelemesi-response

---
name: vergi-incelemesi-response
description: >
  Maliye Bakanlığı vergi inceleme süreci yönetimi: inceleme tutanağı analizi,
  savunma argümantasyonu, tarhiyat öncesi uzlaşma vs. dava karar matrisi, ön
  rapora itiraz dilekçesi taslağı. VUK m. 134-141 inceleme + VUK Ek m. 11 tarhiyat
  öncesi uzlaşma.
user-invocable: true
---

# Vergi İncelemesi Response

## Tetik

Maliye'den **vergi inceleme başlama yazısı** veya **inceleme tutanağı** veya **inceleme raporu** geldiğinde.

## Destination check

- **Mali İşler iç değerlendirme** → "GİZLİDİR – HUKUK + MALİ İŞLER DAHİLİ"
- **CFO/CEO eskalasyon** → 1 sayfa exec summary
- **Dış vergi avukatı brief'i** → "TAX BRIEF – ATM K. m. 36"
- **Maliye'ye sunulacak ön rapora itiraz** → resmi format

## Süreç haritası (VUK m. 134-141)

```
Maliye inceleme başlama →
İnceleme tutanağı (mükellef ve yetkili imza) →
İnceleme raporu (denetçi hazırlar, Bakanlık onayı) →
[Tarhiyat öncesi: VUK Ek m. 11 uzlaşma şansı] →
Tarhiyat (vergi/ceza belirlenir, tebliğ) →
[Tarhiyat sonrası: VUK Ek m. 1 uzlaşma | İYUK m. 7 — 30 gün dava] →
Danıştay dava
```

## Adımlar

### 1. Hangi aşamadayız?

Sor:

> Şu an hangi belge elimizde?
> A. İnceleme başlama yazısı (henüz inceleme başlamadı)
> B. İnceleme tutanağı (denetçi şirkette, kayıt tutuyor)
> C. İnceleme raporu (denetçi raporunu yazdı, henüz tarhiyat yok)
> D. Tarhiyat tebliğ edildi (vergi/ceza belirlendi)

Aşamaya göre stratejisi çok farklıdır.

### A. İnceleme başlama (denetçi gelecek)

- [ ] **Hazırlık dosyası** — incelemeye konu döneme ait beyanname + defter + sözleşmeler + faturalar derhal hazırlanır
- [ ] **Mali İşler + Hukuk koordinasyon** toplantısı
- [ ] **Büyük 4 firma çağrı** — daha önce bu firma TP/genel vergi danışmanı ise koordine
- [ ] **Denetçi ile iletişim diiplini** — sözlü ifade verme yerine yazılı talep, "düşüneceğiz, cevap vereceğiz" formülü
- [ ] **Olası riskler envanteri** — denetçinin nelere bakacağı tahmini (önceki yıl raporlar, BBR sektör analizleri)

### B. İnceleme tutanağı imzalanmadan

İmza ATILMAMASI ÖNERİSİ: tutanaktaki tespitler yanlış/eksik ise itirazlar yazılmadan imza atma. **İmza atılırsa kabul edilmiş sayılabilir.**

- [ ] Her tespiti madde madde değerlendir
- [ ] Yanlış olanlara "İHTİRAZİ KAYITLA" ibaresi
- [ ] Eksik kalanlara "Şu belgeler eklenecektir" şerhi
- [ ] Hukuki dayanağı sorgulanır olanlara "Bu konudaki görüşümüzü ayrıca yazılı sunacağız"

### C. İnceleme raporu — pre-tarhiyat strateji

Bu aşama **kritik**. Raporda önerilen tarhiyat fiilen yapılmadan önce:

**Option 1: Tarhiyat öncesi uzlaşma (VUK Ek m. 11)**
- Daha avantajlı zamanlama
- Cezada %50'ye kadar indirim
- Pazarlık alanı geniş
- Sonra "kabul ediyorum" yazısı

**Option 2: Tarhiyatın yapılmasını bekle, dava aç**
- Yazılı pozisyon güçlü ise
- Danıştay'da kazanma olasılığı yüksek ise
- Maliye'nin agresif yorum yaptığını ispatlayabilirsen

**Option 3: Karma — bazı tespitleri kabul, bazılarına itiraz**
- Risk düşük olan tespitleri uzlaş
- Asıl yüksek tutarlı tespitler için dava

**Karar matrisi (bu skill bunu üretir):**

| Tespit | Maliye iddiası | Kazanma olasılığı | Tutar | Önerilen yol |
|---|---|---|---|---|
| ... | ... | %X | TL | Uzlaş / Dava / Karma |

### D. Tarhiyat tebliğ edildi

⚠️ **30 GÜN SÜRE BAŞLADI** (İYUK m. 7). Aksiyon:

- [ ] **Tarhiyat sonrası uzlaşma (VUK Ek m. 1)** — 30 gün içinde başvur (cezada %75'e kadar indirim)
- [ ] **Veya dava** — 30 gün içinde Danıştay'a → `/tax-legal:tax-litigation-prep`
- [ ] **Veya ikisi** — uzlaşma başvur, görüşme tamamlanırsa kabul/red; uzlaşılmazsa tarhiyat kesinleşir ve sonrasında dava süresi kalmaz! Bu nedenle uzlaşmaya gidersen dava süresi kaçırma riski VAR.

### Yarg MCP — emsal arama

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="<ilgili>",
  arananKelime="<tespitin konusu>",
  baslangicTarihi="2022-01-01"
)

mcp__claude_ai_Yarg_MCP__search_gib_ozelge(
  arananKelime="<tespitin konusu>"
)
```

### sektöre-özel kontroller

- [ ] **Tarhiyat tutarı > 10M TL** → CFO + CEO + Başkan eskalasyon
- [ ] **Petkim ilgili tarhiyat** → KAP açıklama kontrolü
- [ ] **TP konusu** → [Ana ortak / ilişkili taraf] ile koordinasyon
- [ ] **VUK m. 359 kaçakçılık iddiası** → derhal ceza avukatı + CEO
- [ ] **STAR ÖTV / Petkim KDV iade reddi** → kaza-bazlı dava + uzlaşma kombinasyonu

## Çıktı

```markdown
[ÜST BAŞLIK]

# Vergi İncelemesi Response — [İnceleme dönemi / Konu]

## ⚠️ İnceleyen notu
- **Aşama:** A/B/C/D
- **Süre kalan:** [İYUK m. 7 30 gün / VUK Ek 30 gün — N gün kaldı]
- **Karar matrisi:** [Uzlaş / Dava / Karma]
- **Tutar maruziyet:** [TL toplam / vergi + ceza]
- **Reviewer bekleyen:** N adet

## Maliye tespitleri envanteri
[tablo: tespit, iddia, dayanak, savunma argümanı]

## Tarhiyat öncesi vs. sonrası uzlaşma karşılaştırma
[Ek m. 11 avantajı + Ek m. 1 indirim]

## Dava açma analizi
[Danıştay daire, emsal kararlar, kazanma olasılığı]

## Sonraki adımlar
> 1. **Tarhiyat öncesi uzlaşma başvurusu** — daire başvurusu hazırla
> 2. **Hukuk Direktörü + CFO eskalasyon notu**
> 3. **Dış vergi avukatı brief** (dava açılacaksa)
> 4. **Daha fazla bilgi** — şu noktaları aydınlatalım: [...]

**One question I'd ask:** [örn. "Maliye denetçisi geçmişte [Müvekkil]'a karşı agresif mi yumuşak mı yorum yaptı? İlişki sürdürmek karar değiştirebilir."]
```

---

