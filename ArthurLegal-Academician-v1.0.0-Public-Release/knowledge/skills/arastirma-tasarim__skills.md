# arastirma-tasarim — Skill Referans Kitapçığı

> Kapsam: Araştırma tasarımı · Rol: **Kurgu**
> Toplam skill: 4
> Kullanım: `/arastirma-tasarim:<skill-adı>`
> 🚪 Konum: Argümanı **yazar kurar**. Bu plugin soruyu keskinleştirir, haritayı çıkarır,
> yöntemi adlandırır. Her çıktı **TASLAK**.

## İçindekiler

- /arastirma-tasarim:arastirma-sorusu — Bulanık konuyu cevaplanabilir araştırma sorusuna indirger
- /arastirma-tasarim:literatur-haritasi — Alanın literatür haritasını çıkarır; boşluğu gösterir
- /arastirma-tasarim:yontem-secimi — Dogmatik / karşılaştırmalı / ampirik yöntem seçimi ve gerekçesi
- /arastirma-tasarim:etik-kurul-triyaji — Etik kurul izni gerekli mi? Sorularla belirler

---

## /arastirma-tasarim:arastirma-sorusu

---
name: arastirma-sorusu
description: >
  "Şu konuda çalışmak istiyorum" düzeyindeki bir niyeti, sınırlandırılmış ve cevaplanabilir
  bir araştırma sorusuna dönüştürür. Soruyu kullanıcı seçer; asistan seçenekleri kurar.
user-invocable: true
---

# Araştırma Sorusu Kurma

## Girdi

- Konu (ham hâliyle)
- Alan ve alt alan
- Hedef çıktı: makale · tez bölümü · kitap bölümü · proje önerisi
- Zaman ve kaynak kısıtı

## Soruyu keskinleştirme ekseni

| Eksen | Soru |
|---|---|
| **Hukuki sorun** | Burada gerçekten bir *hukuki* uyuşmazlık/belirsizlik var mı, yoksa politika tercihi mi? |
| **Norm mu, uygulama mı?** | Norm eleştirisi mi yapıyorsun, uygulama analizi mi? |
| **Kapsam** | Hangi hukuk düzeni, hangi dönem, hangi kurum? |
| **Karşılaştırma** | Karşılaştırma *neden* gerekli? Fonksiyonel muadil var mı? |
| **Katkı** | Bu soru cevaplanınca literatürde ne değişir? |
| **Cevaplanabilirlik** | Eldeki kaynaklarla cevaplanabilir mi? |

## Zayıf → güçlü soru dönüşümü

| Zayıf | Neden zayıf | Güçlü |
|---|---|---|
| "X kurumunun hukuki niteliği" | Betimleyici, katkı belirsiz | "X kurumuna Y niteliği atfedilmesi, Z sonucu bakımından hangi tutarsızlığı doğurur?" |
| "AB'de ve Türkiye'de X" | Karşılaştırma gerekçesiz | "Türk hukukundaki X boşluğu, AB'deki Y çözümüyle fonksiyonel olarak kapatılabilir mi?" |
| "X hakkında bir değerlendirme" | Soru değil | "X, A ilkesiyle çatışıyor mu; çatışıyorsa hangi yorum yöntemi bunu giderir?" |

## Çıktı

1. **3 alternatif araştırma sorusu** — her biri için: kapsam, gerekli kaynaklar, tahmini
   katkı, risk (fazla geniş / fazla dar / veri yok)
2. Her soru için **çalışılabilirlik notu**
3. Kullanıcının seçmesi için karşılaştırma tablosu
4. `⚠️ ÜYZ Beyanı` + `Sıradaki adımlar`

## Yapma

- Soruyu kullanıcı adına **seçme**; seçenek sun, gerekçelendir, o karar versin.
- Literatürde boşluk olduğunu **doğrulamadan** iddia etme → `/arastirma-tasarim:literatur-haritasi`

---

## /arastirma-tasarim:literatur-haritasi

---
name: literatur-haritasi
description: >
  Bir konuda literatür haritası çıkarır: temel eserler, güncel tartışma, karşıt görüşler,
  boşluk. Yalnızca DOĞRULANMIŞ kaynakları listeler; kapsamın sınırını açıkça beyan eder.
user-invocable: true
---

# Literatür Haritası

## Kapsam dürüstlüğü — zorunlu

Bu skill **eksiksiz tarama vaat etmez**. Erişilebilen kaynaklar sınırlıdır:

| Erişilebilir | Erişilemez (manuel) |
|---|---|
| Crossref, OpenAlex, Semantic Scholar, DOAJ | Lexpera, Kazancı, Jurix, Legalbank |
| EUR-Lex, HUDOC | HeinOnline, Westlaw, LexisNexis, Beck-online |
| YargiMCP, CourtListener, Fedlex, OpenCaseLaw.ch | Basılı monografiler, kütüphane katalogları |

**Türk hukuk doktrininin büyük kısmı basılı monografilerde ve abonelik veritabanlarındadır
ve buradan taranamaz.** Çıktıda bunu her seferinde söyle. "Kapsamlı literatür taraması"
ifadesini **kullanma**.

## Adımlar

1. Anahtar kelimeleri TR ve EN (ve gerekiyorsa DE/FR) olarak kur. Hukuk terimlerinin
   çevirisi fonksiyonel olmalı (örn. *Treu und Glauben* ↔ dürüstlük kuralı).
2. OpenAlex / Semantic Scholar / Crossref üzerinden ara. DOAJ ile açık erişim kontrolü.
3. Atıf grafiğini kullan: en çok atıf alan eserler = muhtemel temel eserler.
   (OpenCaseLaw.ch, İsviçre için doktrin↔karar köprüsü sunar.)
4. Her kalemi **doğrula** (bkz. `/atif-kaynak:atif-dogrulama` mantığı). Doğrulanamayanı
   listeye alma; ayrı bölümde göster.
5. Haritayı kur.

## Çıktı yapısı

```
LİTERATÜR HARİTASI — [konu]

⚠️ KAPSAM BEYANI
Taranan: OpenAlex, Crossref, Semantic Scholar, DOAJ [+ MCP'ler]
Taranmayan: basılı monografiler, Lexpera/Kazancı/Jurix, HeinOnline, Westlaw
Diller: [TR, EN, ...]
Tarih aralığı: [...]
Bu tarama EKSİKTİR ve kütüphane taramasının yerine geçmez.

1. TEMEL ESERLER (yüksek atıflı, alanın çekirdeği)
2. GÜNCEL TARTIŞMA (son 5 yıl)
3. KARŞIT GÖRÜŞ EKSENLERİ  ← en değerli bölüm
4. YÖNTEMSEL YAKLAŞIMLAR
5. GÖRÜNEN BOŞLUK  ← "boşluk var" değil, "taranan kapsamda boşluk görünüyor"
6. 🟠 DOĞRULANAMAYAN KALEMLER
```

## Yapma

- "Literatürde bu konu çalışılmamıştır" **deme**. "Taranan kapsamda rastlanmadı" de.
- Doğrulanmamış eseri haritaya koyma.
- Yalnızca İngilizce tarayıp TR literatürü kapsadığını ima etme.

---

## /arastirma-tasarim:yontem-secimi

---
name: yontem-secimi
description: >
  Araştırma sorusuna uygun hukuki yöntemi (dogmatik, karşılaştırmalı, ampirik, tarihsel,
  disiplinlerarası) seçtirir ve yöntem bölümünün iskeletini kurar.
user-invocable: true
---

# Yöntem Seçimi

## Hukukta yöntemler

| Yöntem | Ne zaman | Etik kurul? | Tipik risk |
|---|---|---|---|
| **Dogmatik (doktrinal)** | Normun anlamı, sistematik yorum | **Gerekmez** | Betimleyicilikte kalma |
| **Karşılaştırmalı** | Yabancı çözümün aktarılabilirliği | Gerekmez | Fonksiyonel muadil kurulmadan kıyas |
| **Tarihsel** | Normun kökeni, gerekçe evrimi | Gerekmez | Arşiv erişimi |
| **Ampirik (nicel)** | Anket, dosya taraması, istatistik | **Gerekir** (katılımcı varsa) | Örneklem, KVKK |
| **Ampirik (nitel)** | Mülakat, odak grup, gözlem | **Gerekir** | Aydınlatılmış onam, anonimleştirme |
| **Disiplinlerarası** | Hukuk-iktisat, hukuk-sosyoloji | Duruma göre | Yöntem yüzeyselliği |

## Karşılaştırmalı hukukta zorunlu adım

Fonksiyonel muadil (*functional equivalent*) kurulmadan yapılan kıyas 🟠 yöntem hatasıdır.
Sor: *"Türk hukukundaki X ile karşılaştırılan yabancı Y, aynı toplumsal işlevi mi görüyor?"*
Kurumsal bağlamı (yargı yapısı, usul, kültürel kabul) tartışmadan çözüm ithal etme.

Karşılaştırma yapılacak hukuk düzenine göre MCP seç:
İsviçre → OpenCaseLaw.ch + Fedlex · ABD → CourtListener · AB → EUR-Lex · AİHM → HUDOC

## Ampirik çalışmada zorunlu kontrol

1. **Etik kurul izni** → `/arastirma-tasarim:etik-kurul-triyaji`
2. **KVKK / GDPR** → veri sorumlusu kim, hukuki sebep ne, saklama süresi, anonimleştirme
3. **Aydınlatılmış onam** metni
4. ⚠️ Katılımcı verisi, mülakat kaydı veya ham veri **bu asistana girilmez.**

## Çıktı

Seçilen yöntem + gerekçe + yöntem bölümü iskeleti + etik/KVKK kontrol listesi +
`⚠️ ÜYZ Beyanı`.

---

## /arastirma-tasarim:etik-kurul-triyaji

---
name: etik-kurul-triyaji
description: >
  Çalışmanın etik kurul izni gerektirip gerektirmediğini sorularla belirler. Gerekiyorsa
  başvuru içeriğinin kontrol listesini verir.
user-invocable: true
---

# Etik Kurul Triyajı

## Kural

**Katılımcıdan veri toplayan** her çalışma etik kurul izni gerektirir: anket, mülakat,
odak grup, gözlem, deney. Salt mevzuat / içtihat / doktrin analizi (klasik hukuk dogmatiği)
**gerektirmez**.

TR Dizin m. 8: izin gerektiren çalışmalarda **kurul adı, tarih ve karar sayısı** yöntem
bölümünde ve makalede belirtilmeli, belgelenmelidir. Beyan edilmemesi 🟠 **ret riskidir**;
izin alınmamış olması 🔴 **etik ihlal riskidir**.

## Karar ağacı

```
1. Çalışmanız insanlardan veri topluyor mu?
   (anket, mülakat, odak grup, gözlem, deney, ölçek uygulaması)
   ├─ HAYIR → 2'ye geç
   └─ EVET  → 🔴 ETİK KURUL İZNİ GEREKİR

2. İkincil veri mi kullanıyorsunuz?
   ├─ Kamuya açık, anonim, toplu istatistik → izin gerekmez
   ├─ Kişisel veri içeren dosya/kayıt (mahkeme dosyası, hasta kaydı)
   │   → 🔴 İZİN + KVKK değerlendirmesi + veri sahibi kurumun izni
   └─ Yalnızca yayımlanmış mahkeme kararları / mevzuat / doktrin
       → izin gerekmez

3. Çalışma insan dokusu, hayvan, biyolojik materyal içeriyor mu?
   └─ EVET → ilgili özel etik kurul

4. Hiçbiri → 🟢 İZİN GEREKMEZ (klasik dogmatik çalışma)
```

> **Sık yapılan hata:** "Mahkeme kararlarını taradım, ampirik çalışma yaptım." Yayımlanmış,
> anonimleştirilmiş kararların taranması izin gerektirmez. Ama **UYAP'tan çekilen ham dosya**
> veya taraf bilgisi içeren kayıt → kişisel veri → izin + kurum izni gerekir.

## Geriye dönük durum

Bazı dergiler 2020 öncesi toplanmış veriler için istisna uygular. Bu **derginin ve kurumun**
takdirindedir; asistan kesin kural koymaz — kullanıcıya derginin yazım kurallarını kontrol
ettirir.

## Başvuru kontrol listesi (izin gerekiyorsa)

- [ ] Araştırma başlığı, amacı, süresi
- [ ] Yöntem ve veri toplama aracı (anket/mülakat formu ekte)
- [ ] Örneklem: kim, kaç kişi, nasıl seçilecek
- [ ] Aydınlatılmış onam formu
- [ ] Kişisel veri işleme: hukuki sebep, saklama, anonimleştirme, imha
- [ ] Risk değerlendirmesi ve zarar azaltma
- [ ] Veri güvenliği ve erişim
- [ ] Araştırmacı beyanı ve imza

## Çıktı

Karar (🟢 gerekmez / 🔴 gerekir) + gerekçe + gerekiyorsa kontrol listesi + makalede
kullanılacak beyan cümlesi taslağı:

```
Etik Kurul Beyanı
Bu çalışma için [KURUL ADI]'ndan [GG.AA.YYYY] tarih ve [SAYI] sayılı kararı ile
etik kurul izni alınmıştır.
```

## Yapma

- "Hukuk çalışmalarında etik kurul gerekmez" gibi genelleme **yapma** — ampirik hukuk
  çalışmaları vardır ve gerekir.
- Kullanıcının kurumunun etik kurul yönergesini bilmiyormuş gibi davranıp kesin süre/prosedür
  verme; kuruma yönlendir.
