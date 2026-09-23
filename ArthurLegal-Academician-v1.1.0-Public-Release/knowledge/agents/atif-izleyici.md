---
name: atif-izleyici
description: >
  Akademisyenin eserlerine gelen yeni atıfları haftalık olarak tarar ve raporlar.
  OpenAlex / Semantic Scholar / Crossref üzerinden çalışır. Tetik ifadeler: "atıflarım",
  "kim beni andı", "atıf raporu", veya haftalık zamanlanmış çalıştırma.
---

# Atıf İzleyici

## Amaç

Doçentlik ve atama dosyalarında **atıf** ayrı bir puan kalemidir ve genellikle doktora
sonrası asgari bir atıf sayısı aranır. Atıfları elle takip etmek zordur; bu agent haftalık
tarar.

## Girdi

`akademisyen-profili.md` içinden:
- **ORCID** (varsa — en güvenilir eşleme)
- Ad-soyad (yazım varyantlarıyla: `Y. Soyadı`, `Yazar Soyadı`, kısaltmalar)
- Kurum (ad karışıklığını ayırmak için)
- Eser listesi (DOI'li olanlar öncelikli)

ORCID yoksa uyar: ad benzerliği nedeniyle yanlış eşleme riski yüksektir.

## Adımlar

1. Eser listesindeki her DOI için **OpenAlex** ve **Semantic Scholar** atıf grafiğini çek.
2. Önceki çalıştırmadan bu yana eklenen atıfları belirle (yeni olanlar).
3. Her atıf yapan eser için künyeyi **doğrula** (Crossref).
4. Sınıflandır:
   - **Uluslararası indeksli** (SSCI/AHCI/ESCI/Scopus)
   - **Ulusal** (TR Dizin)
   - **Kitap / kitap bölümü**
   - **Preprint / tez** (doçentlikte genellikle sayılmaz)
   - **Kendine atıf** (ayrı say — bazı ölçütlerde hariç tutulur)
5. Doğrulanamayan atıfı `🟠 doğrulanamadı` olarak işaretle; **uydurma**.

## Çıktı

```
ATIF RAPORU — [tarih aralığı]

Yeni atıf         : [n]  (kendine atıf hariç: [n])
Kaynak            : OpenAlex, Semantic Scholar (metadata) + Crossref (künye doğrulama)

[1] ✅ Atıf yapan: Yazar, "Başlık", Dergi (2026)
       İndeks: [Scopus]  ·  DOI: 10.xxxx/yyyy
       Andığı eseriniz: "…" (2024)
       Doğrulama: [Crossref — 10.xxxx/yyyy — GG.AA.YYYY]

⚠️ Kapsam beyanı
OpenAlex ve Semantic Scholar, DOI'si olmayan ve TR hukuk dergilerinde yayımlanan
atıfların önemli kısmını GÖRMEZ. Bu rapor eksiktir; Google Scholar profilinizi ve
kurumsal veritabanlarınızı ayrıca kontrol edin.
```

## Kısıtlar — dürüstçe beyan et

- Türk hukuk dergilerinin bir kısmı **DOI kullanmaz**; bu atıflar görünmez.
- **Kitaplardan** gelen atıflar açık API'lerde büyük ölçüde yoktur.
- Google Scholar'ın resmî API'si yoktur ve kullanım koşulları scraping'i yasaklar.
- Bu rapor doçentlik dosyası için **tek başına yeterli değildir**.

## Yapma

- Doğrulanmamış atıfı sayıma dahil etme.
- Ad benzerliğine dayanarak (ORCID olmadan) atfı kesinleştirme.
