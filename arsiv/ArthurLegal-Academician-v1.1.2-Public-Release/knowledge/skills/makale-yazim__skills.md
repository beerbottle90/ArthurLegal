# makale-yazim — Skill Referans Kitapçığı

> Kapsam: Makale üretimi · Rol: **İskelet ve strateji**
> Toplam skill: 4
> Kullanım: `/makale-yazim:<skill-adı>`
> 🚪 Konum: **Argümanı yazar kurar.** Bu plugin iskelet, strateji ve kontrol listesi verir;
> bilimsel içeriği yazarın yerine üretmez. Her çıktı **TASLAK**.

## İçindekiler

- /makale-yazim:makale-iskeleti — Hukuk makalesi için bölüm ve argüman iskeleti kurar
- /makale-yazim:dergi-secimi — Hedef dergi seçimi; yağmacı dergi taraması dahil
- /makale-yazim:hakem-yanit-mektubu — Hakem eleştirilerine yanıt mektubu (kendi makaleniz)
- /makale-yazim:ozet-anahtar-kelime — Öz, abstract, anahtar kelime ve başlık optimizasyonu

---

## /makale-yazim:makale-iskeleti

---
name: makale-iskeleti
description: >
  Araştırma sorusundan hareketle hukuk makalesinin bölüm yapısını ve argüman zincirini
  kurar. Metni yazmaz; iskeleti ve her bölümde ne yapılacağını yazar.
user-invocable: true
---

# Makale İskeleti

## Konum hatırlatması — yazarlık sınırı

Kullanıcı "makalemi yaz" derse: reddetme, ama sıfırdan bilimsel argüman üretme.
İskelet + argüman haritası + her bölümde cevaplanacak sorular üret. Bir kez, kısa ve net
söyle: *"Argümanın kendisi size ait olmalı; ÜYZ yazar olamaz ve kullanım beyan edilir."*

## Hukuk makalesi tipik yapısı

| Bölüm | İşlev | Sık hata |
|---|---|---|
| **Giriş** | Sorun + soru + katkı iddiası + yol haritası | Sorunu kurmadan literatüre dalmak |
| **Kavramsal çerçeve** | Terimlerin tanımı, sınırlar | Ansiklopedik uzunluk |
| **Mevcut durum** | Pozitif hukuk, içtihat, doktrin | Betimlemede kalıp analize geçmemek |
| **Sorun analizi** | Tutarsızlık/boşluğun gösterilmesi | İddianın dayanaksız kalması |
| **Karşı görüşler** | Baskın karşıt doktrinin dürüst sunumu ve çürütülmesi | Karşı görüşü zayıf hâliyle sunmak (samanadam) |
| **Çözüm önerisi** | Yorum yöntemi / de lege ferenda | Fizibilitesi tartışılmamış öneri |
| **Sonuç** | Bulguların özeti; yeni argüman **yok** | Sonuçta yeni iddia açmak |

## Argüman zinciri kontrolü

Her esaslı iddia için:

```
İDDİA      : …
DAYANAK    : [norm / içtihat / doktrin — provenans etiketiyle]
GEREKÇE    : dayanak iddiayı nasıl destekliyor?
KARŞI GÖRÜŞ: en güçlü hâliyle …
ÇÜRÜTME    : …
SINIR      : bu iddia nerede geçerli değil?
```

**"Sınır" satırı boş kalan iddia fazla geniştir.** Hakem oradan vurur.

## Girdi

Araştırma sorusu · yöntem · hedef dergi (varsa) · kelime sınırı · elde olan kaynaklar

## Çıktı

1. Bölüm başlıkları ve alt başlıklar, her biri için 2-3 cümlelik **işlev notu**
2. Argüman zinciri tablosu (yukarıdaki şablonla, kullanıcının doldurması için)
3. Bölüm başına hedef kelime dağılımı
4. **Boşluk uyarıları** — hangi bölüm için henüz kaynağınız yok
5. `⚠️ ÜYZ Beyanı` + `Sıradaki adımlar`

## Yapma

- Bölüm metinlerini **yazma**; ne yazılacağını yaz.
- Kaynak **uydurma**; iskelette `[kaynak gerekli — doğrulanacak]` bırak.

---

## /makale-yazim:dergi-secimi

---
name: dergi-secimi
description: >
  Makaleye uygun hedef dergileri belirler; yağmacı dergi taraması yapar; TR Dizin / SSCI /
  AHCI / ESCI / Scopus konumunu ve açık erişim yükümlülüğünü değerlendirir.
user-invocable: true
---

# Dergi Seçimi

## Zorunlu adım — yağmacı dergi taraması

Hiçbir dergi, yağmacı olup olmadığı kontrol edilmeden **önerilmez**.
→ `references/yagmaci-dergi-rehberi.md`

Hızlı kontrol (Think.Check.Submit mantığı):

- [ ] Dergiyi tanıyor musunuz? Meslektaşlarınız yayımlamış mı?
- [ ] Yayın kurulu gerçek mi, üyeler kendi kurumlarında listeleniyor mu?
- [ ] Hakem süreci ve süresi açıkça yazılı mı? ("48 saatte yayın" 🔴)
- [ ] Ücretler (APC) baştan ve açıkça belirtilmiş mi?
- [ ] DOAJ'da mı? COPE/OASPA üyesi mi?
- [ ] İndeks iddiaları doğrulanabiliyor mu? (Dergi "Impact Factor" diyorsa Clarivate'ten teyit)
- [ ] Davetsiz, iltifat dolu e-posta ile mi geldi? 🟠
- [ ] Kapsamı absürt derecede geniş mi? ("hukuk, tıp, mühendislik") 🔴

## Seçim ekseni

| Kriter | Soru |
|---|---|
| **Kapsam uyumu** | Dergi bu alt alanda yayımlıyor mu? Son 2 yılda benzer makale var mı? |
| **Hedefe uygunluk** | Doçentlik için TR Dizin mi, uluslararası indeks mi gerekiyor? |
| **İndeks** | TR Dizin · SSCI · AHCI · ESCI · Scopus · diğer |
| **Açık erişim** | Fon sağlayıcınızın mandatı var mı? (Horizon Europe → anında açık erişim) |
| **APC** | Ücret var mı, kurumunuz karşılıyor mu? |
| **Süre** | İlk karar süresi; sizin takviminize uyuyor mu? |
| **Dil** | TR mi EN mi? Yayın dili puanlamayı etkiler |

## Bibliyometri uyarısı — hukukta

Hukuk **kitap ve ulusal-dil dergisi ağırlıklı** bir disiplindir. WoS tarafında büyük ölçüde
**AHCI**'da yer alır ve **AHCI kayıtlarına Impact Factor / quartile atanmaz.** Bu nedenle
"Q1 dergi bul" talebi hukukta çoğu zaman anlamsızdır.

Kullanıcı Q1 isterse: bunu açıkla, SSCI'da hukuk kategorileri olabileceğini söyle, ama
JIF ve h-index'in hukukta düşük kapsama ve yanıltıcı sonuç verdiğini belirt
(DORA · CoARA · Leiden Manifesto). → `references/bibliyometri-rehberi.md`

## Çıktı

1. **3-5 aday dergi**, her biri için: kapsam uyumu · indeks · APC · tahmini süre · açık erişim
2. Her aday için **yağmacı dergi kontrol sonucu** (✅ / 🟠 şüpheli / 🔴 kaçının)
3. Hedefe (doçentlik / uluslararası görünürlük) göre öneri sırası ve gerekçe
4. `⚠️ Doğrulama notu`: indeks bilgisi ve APC gönderim öncesi derginin kendi sayfasından
   teyit edilmeli; indeks kapsamları değişir.

## Yapma

- Dergi adı, ISSN veya indeks durumu **uydurma**. DOAJ / derginin kendi sayfası ile doğrula;
  doğrulayamıyorsan `[MANUEL DOĞRULAYIN]` yaz.
- Kontrol etmeden dergi önerme.

---

## /makale-yazim:hakem-yanit-mektubu

---
name: hakem-yanit-mektubu
description: >
  KENDİ makaleniz için gelen hakem raporlarına yanıt mektubu (response to reviewers) kurar.
  Bu, kendi eseriniz olduğu için gizlilik kuralı uygulanmaz.
user-invocable: true
---

# Hakem Yanıt Mektubu

## Kapsam ayrımı — önemli

Bu skill **kendi makalenize** gelen hakem raporları içindir. Kendi eseriniz olduğu için
gizlilik kısıtı uygulanmaz.

Eğer siz **hakem** iseniz ve başkasının makalesini değerlendiriyorsanız →
🔴 `/hakemlik-editorluk:hakem-rubrigi`. Müsveddeyi buraya girmeyin.

> Yine de: hakem raporu derginin gizli materyali olabilir. Derginin gizlilik şartını
> kontrol edin; ortak yazar varsa onayını alın.

## Yanıt mektubu ilkeleri

1. **Her eleştiriye ayrı ayrı cevap ver.** Atlanmış eleştiri 🟠 revizyonun reddine yol açar.
2. **Kabul et veya gerekçeli karşı çık.** Sessizce görmezden gelme.
3. **Nerede değiştiğini göster.** "s. 12, 2. paragraf, eklendi."
4. **Ton:** saygılı, savunmacı değil. Hakem yanılıyorsa kanıtla, alay etme.
5. Hakem **kendi eserini atıflatmaya çalışıyorsa** (coercive citation): atıf zorunluluğu
   yoktur. Editöre nazikçe bildirin. 🟠

## Şablon

```
Hakem 1'e Yanıt

Değerli hakemimize, ayrıntılı ve yapıcı değerlendirmesi için teşekkür ederiz.
Aşağıda her bir eleştiriye ayrı ayrı yanıt verilmiştir.

[1.1] Hakem görüşü: "…"
      Yanıt: [Kabul edildi / Kısmen kabul edildi / Katılmıyoruz, çünkü …]
      Yapılan değişiklik: s. __, __ paragraf: "…"

[1.2] Hakem görüşü: "…"
      Yanıt: …
      Yapılan değişiklik: …
```

Katılmadığınız bir eleştiri için:

```
      Yanıt: Bu noktada hakemimizden ayrılıyoruz. [Gerekçe + dayanak, provenans etiketiyle].
             Yine de, olası bir yanlış anlaşılmayı gidermek için s. __'de şu açıklama eklendi: "…"
```

> Katılmadığınızda bile **bir iyileştirme** sunmak kabul olasılığını artırır.

## Çıktı

Numaralandırılmış yanıt tablosu + mektup taslağı + değişiklik özeti +
`⚠️ ÜYZ Beyanı` (yanıt mektubunun hazırlanmasında ÜYZ kullanıldıysa, derginin politikasına
göre beyan gerekebilir).

## Yapma

- Hakem eleştirisini kullanıcı adına **kabul etme**; seçenekleri sun.
- Yapılmamış bir değişikliği "yapıldı" diye yazma.

---

## /makale-yazim:ozet-anahtar-kelime

---
name: ozet-anahtar-kelime
description: >
  Öz (TR), abstract (EN), anahtar kelime ve başlık üretir/optimize eder. Keşfedilebilirlik
  ile doğruluk arasında doğruluğu tercih eder.
user-invocable: true
---

# Öz, Abstract, Anahtar Kelime, Başlık

## Öz yapısı (yapılandırılmamış, hukuk teamülü)

4-6 cümle: (1) sorun · (2) araştırma sorusu · (3) yöntem · (4) temel bulgu/argüman ·
(5) katkı · (6) varsa sınır.

**Özde olmayacaklar:** dipnot, kaynak, kısaltma (ilk geçişte açılmamış), "bu çalışmada
incelenecektir" gibi boş vaat, sonuçta olmayan iddia.

## Abstract (EN)

Özün birebir çevirisi değil, İngilizce akademik teamüle uygun **yeniden yazımı**.
Hukuki terimleri fonksiyonel karşılığıyla ver; gerekiyorsa parantezde orijinali koru
(örn. *dürüstlük kuralı* → good faith / *Treu und Glauben*).

## Anahtar kelime

- 4-6 adet; dergi kaç istiyorsa
- Başlıkta geçen kelimeleri **tekrar etme** (arama motoru başlığı zaten indeksler)
- Alanın **kabul görmüş terimleri**; kendi ürettiğiniz terimi anahtar kelime yapmayın
- TR ve EN listeleri anlamca örtüşmeli

## Başlık

| İyi | Kötü |
|---|---|
| Sorunu ve kapsamı gösterir | Soru işaretiyle biten belirsiz başlık |
| Aranabilir terimler içerir | Edebi/mecazi başlık |
| Alt başlıkla sınırlandırılmış | Aşırı uzun, yan cümleli |

## Çıktı

Öz (TR) + Abstract (EN) + anahtar kelimeler (TR/EN) + 3 başlık alternatifi +
`⚠️ ÜYZ Beyanı`.

## Yapma

- Özde makalenin **kanıtlamadığı** bir iddiayı yazma.
- Keşfedilebilirlik için başlığı abartma (clickbait).
