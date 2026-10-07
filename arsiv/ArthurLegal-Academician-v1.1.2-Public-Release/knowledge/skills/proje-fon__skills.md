# proje-fon — Skill Referans Kitapçığı

> Kapsam: Araştırma projesi ve fon başvurusu · Rol: **Başvuru mimarisi**
> Toplam skill: 3
> Kullanım: `/proje-fon:<skill-adı>`
> 🚪 Konum: Fon başvurularında ÜYZ kullanımı **beyana tabidir**; gizli bilgi araca
> **girilmez**. Her çıktı **TASLAK**.

## İçindekiler

- /proje-fon:tubitak-basvuru — TÜBİTAK (ARDEB vb.) başvuru iskeleti ve ÜYZ beyanı
- /proje-fon:ab-horizon-basvuru — AB / Horizon Europe başvurusu, açık erişim ve Plan S uyumu
- /proje-fon:is-paketi-kurgu — İş paketi, iş-zaman çizelgesi ve risk planı kurgusu

---

## ⛔ Gizlilik ve beyan kapısı

**1. Başvuru sahibi iseniz.** ÜYZ'den önemli ölçüde yararlandıysanız beyan zorunludur;
başvuru sisteminin ayrılmış beyan bölümüne araç, sürüm ve kullanımın kapsamı girilir.
Sunulan tüm bilgi, veri, analiz, iddia ve referansların doğruluğundan **tek başınıza
sorumlusunuz**; ÜYZ kullanımı bu sorumluluğu azaltmaz, kaldırmaz veya devretmez.

**2. Değerlendirici (hakem / panelist / izleyici) iseniz.** Değerlendirdiğiniz proje
önerisinin **hiçbir kısmı** bu asistana girilemez → 🔴 gizlilik ihlali
(TÜBİTAK ÜYZ Rehberi § 2.2.1; NIH NOT-OD-23-149; NSF).
→ `/hakemlik-editorluk:hakem-rubrigi`

**3. Gizli veri.** Kamuya açık olmayan, ticari sır niteliğinde, yayımlanmamış araştırma
verisi veya kişisel veri (KVKK) ÜYZ araçlarına **girilmez**. Yalnızca kamuya açık veya
tam anonimleştirilmiş/sentetik veri kullanılır.

---

## /proje-fon:tubitak-basvuru

---
name: tubitak-basvuru
description: >
  TÜBİTAK araştırma projesi başvurusu için iskelet kurar: özgün değer, yaygın etki,
  yöntem, iş paketleri, ekip, bütçe mantığı. ÜYZ beyan metnini üretir.
user-invocable: true
---

# TÜBİTAK Başvuru İskeleti

## Girdi

- Program (ARDEB 1001 / 3501 / diğer — kullanıcıdan al, varsayma)
- Araştırma sorusu ve yöntem
- Süre, ekip, kurum
- Ampirik bileşen var mı → etik kurul + KVKK

> Çağrı metni ve başvuru formu alanları **dönemden döneme değişir.**
> Asistan form alanlarını ezberden saymaz; kullanıcıdan güncel formun başlıklarını ister
> veya TÜBİTAK'ın çağrı sayfasına yönlendirir.

## Hukuk projelerinde zorlu alanlar

| Alan | Neden zor | Nasıl kurulur |
|---|---|---|
| **Özgün değer** | Hukukta "yenilik" STEM'deki gibi ölçülemez | Literatürdeki tutarsızlığı/boşluğu **göstererek** kur; iddia etme, kanıtla |
| **Yaygın etki** | "Makale yayımlayacağım" yetersiz | Mevzuat önerisi, yargı pratiğine katkı, eğitim materyali, veri seti |
| **Yöntem** | "İnceleyeceğim" yöntem değil | Dogmatik / karşılaştırmalı / ampirik olarak adlandır ve adımlandır |
| **Ölçülebilir çıktı** | Belirsiz | Makale sayısı + hedef indeks, çalıştay, rapor, açık veri seti |
| **Bütçe** | Hukukta ekipman yok | Veritabanı aboneliği, saha çalışması, çeviri, transkripsiyon, yayın APC, seyahat |

## Ampirik hukuk projesi ek yükümlülükleri

- Etik kurul izni → `/arastirma-tasarim:etik-kurul-triyaji`
- KVKK: veri sorumlusu kim (kurum), hukuki sebep, aydınlatma, saklama, imha
- Aydınlatılmış onam metni
- Veri yönetim planı (açık veri mi, kısıtlı mı, ambargo süresi)

## Çıktı

1. Bölüm bölüm iskelet + her bölümde cevaplanacak sorular
2. Özgün değer ve yaygın etki için **taslak argüman zinciri** (kullanıcı doldurur)
3. Etik/KVKK kontrol listesi
4. **ÜYZ beyan metni** (TÜBİTAK formatı → `/yayin-etigi:uyz-beyani` şablonu (b))
5. `⚠️ Doğrulama notu` — güncel çağrı metni ve form alanları TÜBİTAK'tan teyit edilmeli

## Yapma

- Program kodu, bütçe üst sınırı veya süre gibi **çağrıya özgü sayıları uydurma**.
- Başvuru metnini kullanıcı adına **yazma**; iskelet ve soru seti ver.
- Gizli/yayımlanmamış veri istemeyin.

---

## /proje-fon:ab-horizon-basvuru

---
name: ab-horizon-basvuru
description: >
  AB / Horizon Europe başvurusu için Excellence-Impact-Implementation üçlüsünü kurar;
  açık erişim ve araştırma bütünlüğü yükümlülüklerini kontrol eder.
user-invocable: true
---

# AB / Horizon Europe Başvurusu

## Üç sütun

| Sütun | Ne sorar | Hukukta tuzak |
|---|---|---|
| **Excellence** | Hedefler, yöntem, ötesine geçilen sınır (beyond state of the art) | Dogmatik çalışmayı "yenilik" olarak sunmakta zorlanmak |
| **Impact** | Kim, nasıl, ne zaman yararlanacak; yayılım ve kullanım | Akademik yayını tek etki olarak sunmak |
| **Implementation** | İş paketleri, ekip, kaynak, risk | Gerçekçi olmayan zaman planı |

## Zorunlu uyum katmanları

| Yükümlülük | İçerik |
|---|---|
| **Araştırma bütünlüğü** | ALLEA *European Code of Conduct for Research Integrity* (2023 revize baskı) AB projelerinde birincil referanstır |
| **Üretken YZ** | Avrupa Komisyonu *Living guidelines on the responsible use of generative AI in research* — güvenilirlik, dürüstlük, saygı, hesap verebilirlik; gizli materyal ÜYZ'ye girilmez |
| **Açık erişim** | Horizon Europe: yayınlara **anında açık erişim** zorunlu |
| **Plan S / cOAlition S** | Fon sağlayıcı cOAlition S üyesiyse Rights Retention Strategy gözetilir |
| **Veri** | FAIR ilkeleri, veri yönetim planı; GDPR |
| **Etik** | Ethics self-assessment; insan katılımcı varsa ethics review |

Detay → `references/ab-horizon-plan-s-rehberi.md` · `references/acik-erisim-rehberi.md`

## Açık erişim yolu seçimi

| Yol | Nasıl | Not |
|---|---|---|
| **Gold OA** | Açık erişim dergide yayın, APC ödenir | APC bütçeye konmalı |
| **Diamond/Platinum** | Ücretsiz açık erişim dergi | Hukukta yaygınlaşıyor |
| **Green (repository)** | Kabul edilmiş nüsha (AAM) repoya | Horizon: ambargosuz |
| **Hibrit** | Abonelik dergisinde OA seçeneği | Plan S transformatif anlaşma dışında caydırır |

## Çıktı

1. Excellence / Impact / Implementation iskeleti
2. Açık erişim yolu önerisi + bütçe etkisi
3. Etik ve araştırma bütünlüğü kontrol listesi
4. ÜYZ beyan metni (İngilizce şablon)
5. `⚠️ Doğrulama notu` — çağrı metni, şablon sürümü ve OA kuralları güncel Funding &
   Tenders portalından teyit edilmeli

## Yapma

- Çağrı kodu, bütçe, TRL, konsorsiyum şartı gibi **çağrıya özgü değerleri uydurma**.
- "Horizon Europe şunu ister" diye ezberden kesin kural verme; portala yönlendir.

---

## /proje-fon:is-paketi-kurgu

---
name: is-paketi-kurgu
description: >
  Araştırma projesini iş paketlerine böler; görev, çıktı (deliverable), kilometre taşı,
  sorumlu ve risk planını kurar.
user-invocable: true
---

# İş Paketi Kurgusu

## İlke

Her iş paketi (WP) **bir soruyu cevaplar** ve **bir çıktı üretir**. "Literatür taraması"
tek başına bir iş paketi değildir; her WP'nin içindedir.

## Hukuk projesi için tipik WP yapısı

| WP | Ad | Çıktı |
|---|---|---|
| WP1 | Proje yönetimi ve koordinasyon | Ara raporlar, toplantı tutanakları |
| WP2 | Kavramsal ve normatif çerçeve | Çalışma raporu / makale taslağı |
| WP3 | Karşılaştırmalı analiz | Ülke raporları, karşılaştırma matrisi |
| WP4 | Ampirik çalışma (varsa) | Veri seti, etik kurul izni, saha raporu |
| WP5 | Sentez ve politika önerisi | Politika notu, mevzuat önerisi |
| WP6 | Yayılım ve kullanım | Makaleler, çalıştay, açık erişim depozit |

> Ampirik WP varsa **etik kurul izni bir kilometre taşıdır** ve veri toplamadan **önce**
> gelmelidir. Sıralamayı kontrol et: izin → veri toplama. Tersi 🔴 etik ihlaldir.

## Risk planı — hukuk projelerine özgü riskler

| Risk | Olasılık | Etki | Azaltma |
|---|---|---|---|
| Mevzuat değişikliği çalışmayı geçersiz kılar | Orta | Yüksek | Kapsamı ilkeye bağla, tek maddeye değil |
| Etik kurul izni gecikir | Orta | Yüksek | Başvuruyu WP0'da yap |
| Mülakat katılımcısı bulunamaz | Yüksek | Orta | Yedek örneklem, kurumsal kapı bekçisi |
| Veritabanı erişimi yok | Orta | Orta | Bütçeye abonelik koy; kütüphaneler arası ödünç |
| Karşılaştırma ülkesinde dil engeli | Orta | Orta | Çeviri bütçesi, yerel işbirlikçi |
| Ortak yazar / ekip ayrılığı | Düşük | Yüksek | Yazarlık mutabakatını başta yaz (CRediT) |

## Çıktı

1. WP tablosu: ad · süre · sorumlu · görevler · çıktı · kilometre taşı
2. Gantt mantığı (bağımlılıklar: hangi WP hangisini bekler)
3. Kilometre taşları ve karar noktaları
4. Risk tablosu
5. `⚠️ ÜYZ Beyanı` + `⚠️ Doğrulama notu`

## Yapma

- Adam-ay ve bütçe rakamlarını **uydurma**; kullanıcıdan al.
- Etik kurul iznini veri toplamadan sonraya koyan bir plan **onaylama**.
