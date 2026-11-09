# Bibliyometri Rehberi — ve Hukuktaki Sınırları

---

## Önce sınır, sonra metrik

**Hukuk, bibliyometrinin en kötü çalıştığı disiplinlerden biridir.** Nedenleri:

1. Birincil çıktı çoğu zaman **kitap / monografi**dir; atıf indeksleri kitabı zayıf kapsar.
2. Yayınların büyük kısmı **ulusal dilde** ve ulusal dergilerdedir; Scopus/WoS kapsamaz.
3. Web of Science'ta dergi ölçütleri indekse ve kategoriye göre değişir: JCR 2023'ten beri
   AHCI ve ESCI dergileri de Impact Factor alır; quartile ise yalnız bilim ve sosyal bilim
   kategorilerinde verilir, sanat ve beşeri bilimlere özgü kategorilerde **verilmez**.
4. Atıf birikimi yavaştır; 2 yıllık IF penceresi hukukta anlamsızdır.

> Sonuç: "Q1 hukuk dergisi bul" talebi çoğu zaman **kategori hatasıdır**.

---

## Metrikler

| Metrik | Ne ölçer | Kaynak | Hukukta değeri |
|---|---|---|---|
| **JIF (Impact Factor)** | Dergi atıf ortalaması, 2 yıllık pencere | Clarivate JCR | Düşük — atıf birikimi yavaş, kapsam dar |
| **Quartile (Q1–Q4)** | Kategori içinde IF sıralaması | JCR | Bilim ve sosyal bilim kategorilerinde; sanat ve beşeri bilim kategorilerinde yok |
| **CiteScore** | Dergi atıf metriği, 4 yıllık pencere | Scopus | Orta |
| **SJR** | Prestij-ağırlıklı (yüksek-sıra dergiden atıf daha değerli) | Scopus/SCImago | Orta |
| **SNIP** | Alan atıf yoğunluğuna göre normalize | Scopus/CWTS | Disiplinler arası kıyas için daha adil |
| **h-index** | Yazarın verim + etki ölçüsü | çeşitli | Düşük — hukukta yavaş birikir |

---

## İndeksler

| İndeks | Kapsam | IF/quartile? |
|---|---|---|
| **SCIE** | Fen bilimleri | Evet |
| **SSCI** | Sosyal bilimler (hukuk kısmen) | Evet |
| **AHCI** | Sanat ve beşeri bilimler | IF: evet (JCR 2023'ten beri). Quartile: beşeri bilim kategorisinde hayır; dergi bir sosyal bilim kategorisinde de yer alıyorsa o kategoride evet |
| **ESCI** | WoS'un genişletilmiş indeksi | IF: evet (JCR 2023'ten beri). Quartile: JCR 2024'ten beri bilim ve sosyal bilim kategorilerinde evet |
| **Scopus** | Geniş kapsam | CiteScore/SJR/SNIP |
| **TR Dizin** | Ulusal, ULAKBİM | Hayır |

> Bir dergi hem SSCI hem AHCI'da olabilir. Doçentlik puanlamasında hangisinden sayılacağı
> ÜAK'ın dönem PDF'indeki kurala bağlıdır.

---

## Değerlendirme reformu — neden metrik tek başına yetmez

| Girişim | Yıl | Temel iddia |
|---|---|---|
| **DORA** (San Francisco Declaration on Research Assessment) | 2013 | Journal Impact Factor, araştırma **kalitesinin vekili** olarak kullanılmamalı; içerik değerlendirilmeli |
| **Leiden Manifesto** | 2015 | Sorumlu metrik 10 ilkesi; nicel gösterge daima bağlamlandırılmalı ve nitel uzman değerlendirmesinin **yerine değil, yanında** kullanılmalı |
| **CoARA** (Coalition for Advancing Research Assessment) | 2022 | Çeşitli katkıların tanınması; nitel-öncelikli değerlendirme; JIF/h-index'in uygunsuz kullanımından kaçınma; üniversite sıralamalarının değerlendirmede kullanılmaması |

Bu üçü, hukuk gibi kitap/ulusal-dil ağırlıklı disiplinlerde **nitel değerlendirmeyi**
özellikle önerir.

---

## Asistanın davranışı

- Kullanıcı "Q1 dergi öner" derse: quartile'ın derginin JCR'deki kategorisine bağlı olduğunu
  açıkla (sosyal bilim kategorisinde var, yalnız beşeri bilim kategorisindeyse yok), dergiyi
  JCR'den teyit ettir, ama JIF/h-index'in hukukta yanıltıcı olduğunu belirt.
- Bir derginin indeks bilgisini **uydurma**; derginin kendi sayfasından veya DOAJ'dan
  doğrula, doğrulayamıyorsan `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>` yaz.
- "Impact Factor" iddiası olan bir dergiyi Clarivate teyidi olmadan kabul etme —
  sahte IF yaygındır. → `yagmaci-dergi-rehberi.md`
- **Bir dergiye JCR'de teyit etmeden quartile atfetme**; yalnız sanat ve beşeri bilim kategorisinde
  yer alan dergi için quartile yoktur. ÜAK'ın hangi indeksi nasıl saydığı dönem PDF'ine bağlıdır.

---

## İlgili

`dergi-secimi-rehberi.md` · `docentlik-hukuk-temel-alani-rehberi.md` · `yagmaci-dergi-rehberi.md`
