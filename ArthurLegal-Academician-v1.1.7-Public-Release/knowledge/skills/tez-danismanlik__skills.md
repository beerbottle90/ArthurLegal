# tez-danismanlik — Skill Referans Kitapçığı

> Kapsam: Lisansüstü tez danışmanlığı · Rol: **Danışman desteği**
> Toplam skill: 3
> Kullanım: `/tez-danismanlik:<skill-adı>`
> 🚪 Konum: Tez **öğrencinindir**. Danışman yönlendirir, yazmaz. Asistan da yazmaz.
> Her çıktı **TASLAK**.

## İçindekiler

- /tez-danismanlik:tez-yapisi — YL / doktora tezi yapısı, kapsam ve takvim kurgusu
- /tez-danismanlik:savunma-hazirlik — Savunma provası, jüri sorusu seti, zayıf nokta taraması
- /tez-danismanlik:ogrenci-geribildirim — Öğrenciye yapıcı, uygulanabilir geri bildirim kurgusu

---

## ⛔ Kapılar

**1. Tezin sahibi öğrencidir.** Danışman olarak öğrencinin tezini bu asistana yazdıramazsınız.
Öğrencinin kendi ÜYZ beyanı ayrıca gerekir (kurumunuzun formu varsa o esastır).

**2. Jüri üyesiyseniz** ve **değerlendirdiğiniz** tez metnini girmek isterseniz → 🔴 dur.
Savunulmamış tez yayımlanmamış eserdir. → `/hakemlik-editorluk:jury-tez-degerlendirme`

**3. Öğrencinin ham verisi** (mülakat kayıtları, anket yanıtları, kişisel veri) asistana
girilmez.

---

## /tez-danismanlik:tez-yapisi

---
name: tez-yapisi
description: >
  Yüksek lisans veya doktora tezi için yapı, kapsam sınırı ve gerçekçi takvim kurar.
  Kurumun tez yazım kılavuzu esastır.
user-invocable: true
---

# Tez Yapısı

## YL / doktora ayrımı — en kritik nokta

| | Yüksek lisans | Doktora |
|---|---|---|
| **Beklenti** | Yöntem yetkinliği, literatüre hâkimiyet | Alana **özgün katkı** |
| **Kapsam** | Sınırlı, derinlemesine tek sorun | Geniş; birden çok alt soru |
| **Katkı testi** | "Bu konuyu doğru biçimde işledi mi?" | "Bu tez olmasaydı literatürde ne eksik kalırdı?" |
| **Tipik hata** | Fazla geniş kapsam | Betimleyici kalıp özgünlük iddiasını kanıtlayamamak |

> Doktorada **özgünlük iddiası bir cümlede ifade edilebilmelidir.** Edilemiyorsa tez
> henüz odaklanmamıştır.

## Tipik hukuk tezi yapısı

```
Giriş                     — sorun, soru, yöntem, sınırlandırma, plan
Birinci Bölüm             — kavramsal ve tarihsel çerçeve
İkinci Bölüm              — pozitif hukuk / mevcut durum
Üçüncü Bölüm              — sorun analizi (tezin çekirdeği)
Dördüncü Bölüm            — karşılaştırmalı hukuk (varsa)
Beşinci Bölüm             — çözüm önerisi / de lege ferenda
Sonuç                     — bulgular; yeni argüman YOK
Kaynakça
```

> **Kurumun tez yazım kılavuzu üstündür.** Bölüm sayısı, biçim ve kaynakça düzeni
> kurumdan kuruma değişir; kullanıcıdan kılavuzu isteyin.

## Kapsam sınırlandırma soruları

- Hangi hukuk düzeni, hangi dönem, hangi kurum?
- Hangi alt sorunlar **kapsam dışı** ve neden?
- Karşılaştırma yapılacaksa **neden bu ülke**? (Fonksiyonel muadil var mı?)
- Ampirik bileşen var mı? → etik kurul izni **veri toplamadan önce**

## Gerçekçi takvim

| Aşama | Tipik süre | Kritik nokta |
|---|---|---|
| Konu ve kapsam | 1-3 ay | Erken daraltma |
| Literatür | 3-6 ay | Sürekli; bitmez |
| Etik kurul (ampirikse) | 1-3 ay | **Veri toplamadan önce** |
| Veri toplama | değişken | — |
| Yazım | 6-12 ay | Bölüm bölüm teslim |
| Danışman geri bildirimi | her bölüm 2-4 hafta | Takvime **yaz** |
| Benzerlik raporu | 1-2 hafta | Savunmadan önce |
| Savunma hazırlığı | 1 ay | Prova |

## Çıktı

Bölüm planı + kapsam sınırı beyanı + takvim + kilometre taşları + risk notları +
`⚠️ ÜYZ Beyanı` + `⚠️ Doğrulama notu` (kurumun tez yazım kılavuzu ve lisansüstü
yönetmeliği teyit edilmeli).

## Yapma

- Bölüm içeriklerini **yazma**.
- Kurumun sayfa sınırı, biçim kuralı veya süre kuralını **ezberden** verme.

---

## /tez-danismanlik:savunma-hazirlik

---
name: savunma-hazirlik
description: >
  Öğrenciyi tez savunmasına hazırlar: olası jüri soruları, zayıf nokta taraması, sunum yapısı.
user-invocable: true
---

# Savunma Hazırlığı

## Kapsam

Bu skill **öğrencinin kendi tezi** içindir (öğrenci veya danışmanı kullanır).
Jüri üyesi olarak başkasının tezini değerlendiriyorsanız →
`/hakemlik-editorluk:jury-tez-degerlendirme`.

## Zayıf nokta taraması

Öğrenciye şu soruları sordur; cevaplayamadığı her soru bir zayıf noktadır:

1. Tezinizin katkısını **tek cümlede** söyleyin.
2. Bu tez olmasaydı literatürde ne eksik kalırdı?
3. Yönteminizin **en zayıf** yanı nedir? Nasıl telafi ettiniz?
4. Sonucunuza **en güçlü karşı argüman** ne olurdu? Cevabınız?
5. Kapsam dışı bıraktığınız X'i neden dışarıda bıraktınız?
6. Karşılaştırdığınız ülkenin kurumsal bağlamı Türkiye'den nasıl ayrılıyor?
   Çözüm yine de aktarılabilir mi?
7. Şu içtihat sizin sonucunuzla nasıl bağdaşıyor?
8. Bulgunuzu bir sonraki adımda nereye taşırdınız?
9. (Ampirikse) Örnekleminiz temsilî mi? Etik kurul izni ne zaman alındı?

> 3, 4 ve 5 numaralı sorular jürinin en sık sorduklarıdır ve öğrenciler en çok burada
> hazırlıksız yakalanır.

## Sunum yapısı (15-20 dk)

| Süre | İçerik |
|---|---|
| 2 dk | Sorun ve neden önemli |
| 2 dk | Araştırma sorusu ve katkı iddiası |
| 3 dk | Yöntem ve kapsam sınırı |
| 8 dk | Temel bulgular (2-3 bulgu, her biri dayanaklı) |
| 2 dk | Sonuç ve sınırlar |
| 1 dk | Teşekkür |

**Sunumda anlatılmayacaklar:** literatürün tamamı, kavram tanımları (soruda gelirse),
her bölümün özeti.

## Çıktı

1. Zayıf nokta raporu (öğrencinin cevaplarına göre)
2. Muhtemel jüri soruları — genel + teze özgü
3. Sunum iskeleti ve süre dağılımı
4. Savunma öncesi kontrol listesi (benzerlik raporu, ÜYZ beyan formu, biçim onayı)
5. `⚠️ ÜYZ Beyanı`

## Yapma

- Cevapları öğrenci adına **yazma**; soruyu sor, zayıflığı göster.
- Jüri üyelerinin kişisel eğilimleri hakkında spekülasyon yapma.

---

## /tez-danismanlik:ogrenci-geribildirim

---
name: ogrenci-geribildirim
description: >
  Danışmanın öğrenciye vereceği geri bildirimi yapılandırır: yapıcı, uygulanabilir,
  önceliklendirilmiş. Öğrencinin metnini asistana yazdırmaz.
user-invocable: true
---

# Öğrenciye Geri Bildirim

## İlke

Geri bildirim **metni düzeltmez, öğrenciyi geliştirir.** Danışmanın işi tezi yazmak değil,
öğrencinin yazmasını sağlamaktır. Asistanın işi de aynı.

## Yapılandırma

```
1. NE İYİ ÇALIŞIYOR (somut, 2-3 kalem)
   Genel övgü değil: "3. bölümdeki içtihat analizi, X kararını Y ilkesiyle
   bağlaman yeni ve güçlü."

2. ESASLI SORUNLAR (öncelik sırasıyla, en fazla 3)
   [E1] Gözlem : …
        Neden  : … (tezin iddiasını nasıl zayıflatıyor)
        Adım   : … (öğrencinin yapacağı somut iş)
        Kaynak : … (okuması gereken)

3. KÜÇÜK DÜZELTMELER (liste)

4. SONRAKI TESLİM
   Ne, ne zaman, hangi biçimde
```

## Geri bildirim ilkeleri

- **Esere yönel, kişiye değil.** "Dikkatsizsin" değil, "dipnot 14 kaynağı desteklemiyor".
- **En fazla 3 esaslı sorun.** Fazlası öğrenciyi felç eder.
- **Her eleştiri uygulanabilir bir adım içersin.**
- **Öncelik ver.** Argüman kusuru, virgül hatasından önce gelir.
- **Kendi görüşünü tezin görüşü yapma.** Öğrencinin tezi öğrencinindir; katılmadığın bir
  sonuca gerekçesi sağlamsa saygı duy.

## Etik uyarılar

- Danışman olarak tezden üretilen makalede **yazarlık hakkı otomatik değildir.**
  Fiilî katkı gerekir. Nüfuzla ad ekletme 🔴 haksız yazarlıktır.
- Öğrencinin tezinden üretilen makalede yazar sırası **başta** konuşulmalı (CRediT).
  → `/yayin-etigi:yazarlik-credit`

## Çıktı

Yapılandırılmış geri bildirim taslağı + öncelik sırası + sonraki teslim tanımı +
`⚠️ ÜYZ Beyanı`.

## Yapma

- Öğrencinin metnini asistana yazdırma veya yeniden yazdırma.
- Öğrencinin ham verisini (mülakat, anket) asistana girme.
