# akademik-yukselme — Skill Referans Kitapçığı

> Kapsam: Doçentlik ve akademik atama · Rol: **Dosya analizi**
> Toplam skill: 3
> Kullanım: `/akademik-yukselme:<skill-adı>`
> 🔴 Konum: Bu plugin **doğrulama kapısı** ile korunur. Ölçütler dönemden döneme değişir;
> hiçbir puan, başvuru dönemi ÜAK belgesi teyit edilmeden kesin sunulmaz.

## İçindekiler

- /akademik-yukselme:docentlik-puan-analizi — ÜAK Hukuk Temel Alanı ölçütlerine göre dosya analizi
- /akademik-yukselme:dosya-eksik-analizi — Eksik kalemleri ve en verimli tamamlama yolunu gösterir
- /akademik-yukselme:atama-kriter-kontrol — Dr. Öğr. Üyesi / Doçent kadrosu / Profesör atama ölçütleri

---

## ⛔ Doğrulama kapısı — her skill'den önce çalışır

ÜAK **Hukuk Temel Alanı** doçentlik başvuru ölçütleri **her başvuru dönemi için ayrı
yayımlanır** ve değişir. Bu paketteki tablo bir **referanstır, kesin kaynak değildir**.

Her hesaplamadan önce sor:

> "Başvuru döneminizi ve o döneme ait ÜAK *Hukuk Temel Alanı* başvuru şartları PDF'ini
> teyit ettiniz mi? (`akademisyen-profili.md` → *Başvuru dönemi ÜAK PDF'i teyit edildi mi?*)"

- Cevap **Hayır** ise: hesaplama yapma. ÜAK'ın resmî sayfasına yönlendir
  (`uak.gov.tr` → Doçentlik Başvuru Şartları → dönem → Hukuk Temel Alanı PDF).
  İstenirse **yöntemi** anlat, **sayı verme**.
- Cevap **Evet** ise: kullanıcıdan teyit ettiği PDF'in **tarihini ve eşik değerlerini**
  al ve **onları** kullan. Paketteki tabloyla çeliştiğinde **kullanıcının PDF'i üstündür**.

Referans tablo ve zorunlu koşullar → `references/docentlik-hukuk-temel-alani-rehberi.md`

---

## /akademik-yukselme:docentlik-puan-analizi

---
name: docentlik-puan-analizi
description: >
  Adayın yayın listesini ÜAK Hukuk Temel Alanı ölçütlerine göre kategorize eder, puanlar ve
  zorunlu koşulların karşılanıp karşılanmadığını kontrol eder. Doğrulama kapısına tabidir.
user-invocable: true
---

# Doçentlik Puan Analizi

## Önkoşul

Doğrulama kapısı geçilmiş olmalı (yukarıya bakın). Geçilmediyse **hesaplama yapma**.

## Girdi

Her yayın için:

| Alan | Neden gerekli |
|---|---|
| Tür | makale / kitap / bölüm / bildiri / patent / ödül / proje / tez danışmanlığı |
| İndeks | SSCI · AHCI · ESCI · Scopus · TR Dizin · diğer hakemli |
| Quartile (varsa) | Q1-Q4 (yalnızca IF atanan indekslerde; **AHCI'ya quartile atanmaz**) |
| Yazar sayısı | Çok yazarlıda puan bölünür |
| **Doktora öncesi/sonrası** | Puanın büyük kısmı doktora sonrası olmalı |
| Tezden üretildi mi | Ayrı kategori |
| Atıf sayısı ve kaynağı | Atıf kalemi için |

Ayrıca: doktora tarihi (profilden), yabancı dil belgesi ve puanı.

## Analiz adımları

1. Her yayını **tek bir kategoriye** yerleştir. (Bir çalışma yalnızca bir bölümde puanlanır.)
2. Doktora tarihini eşik alarak öncesi/sonrası ayır.
3. Yazar sayısına göre puanı böl.
4. Kategori tavanlarını uygula (atıf, tez danışmanlığı, proje, bildiri, editörlük vb.
   üst sınırları vardır).
5. **Zorunlu koşulları ayrı kontrol et** — puandan bağımsızdır ve puan yetse bile
   karşılanmazsa başvuru reddedilir. Hukukta ulusal makale, tezden üretilmiş yayın ve
   kitap kalemlerinde zorunluluklar bulunur.
6. Yabancı dil ön koşulunu kontrol et (belge ve puan; ölçüt yönetmelikte, puan tablosunda değil).

## Çıktı

```
DOÇENTLİK DOSYA ANALİZİ — [Başvuru dönemi]
Kullanılan ölçüt kaynağı: [Kullanıcının teyit ettiği ÜAK PDF, tarih: ...]

TOPLAM PUAN            : [x]  / asgari [y]
DOKTORA SONRASI PUAN   : [x]  / asgari [y]

ZORUNLU KOŞULLAR
[✅/🔴] Ulusal makale zorunluluğu   : [durum]
[✅/🔴] Tezden üretilmiş yayın      : [durum]
[✅/🔴] Kitap / kitap bölümü        : [durum]
[✅/🔴] Atıf (doktora sonrası)      : [durum]
[✅/🔴] Bildiri                     : [durum]
[✅/🔴] Eğitim-öğretim              : [durum]
[✅/🔴] Yabancı dil belgesi         : [durum]

KATEGORİ DÖKÜMÜ
[tablo]

🔴 KARŞILANMAYAN ZORUNLU KOŞULLAR
[liste + ne gerekiyor]
```

Sonda: `⚠️ Doğrulama notu` — *"Bu analiz, sizin teyit ettiğiniz [tarih] tarihli ÜAK
belgesine dayanır. Nihai değerlendirme ÜAK'a aittir; bu çıktı bir taslaktır."*

## Yapma

- Doğrulama kapısı geçilmeden **sayı verme**.
- AHCI kayıtlarına quartile **atfetme**.
- "Bu puanla geçersiniz" **deme**. Nihai takdir ÜAK'tadır.
- Kullanıcının verdiği indeks bilgisini doğrulamadan kabul etme; şüpheliyse teyit ettir.

---

## /akademik-yukselme:dosya-eksik-analizi

---
name: dosya-eksik-analizi
description: >
  Puan analizinden sonra, hedefe ulaşmak için en verimli tamamlama yollarını gösterir.
  Etik ve gerçekçi olmayan kısayolları reddeder.
user-invocable: true
---

# Dosya Eksik Analizi

## Önkoşul

`/akademik-yukselme:docentlik-puan-analizi` çıktısı.

## Yöntem

Eksik puanı ve karşılanmayan **zorunlu koşulları** ayır. Zorunlu koşul, puandan önce gelir:
puan fazlası bir zorunlu koşulun eksikliğini **kapatmaz**.

Her tamamlama seçeneği için:

| Boyut | Soru |
|---|---|
| Puan getirisi | Kaç puan? |
| Süre | Ne kadar sürer? (dergi karar süresi + revizyon + yayın) |
| Gerçekçilik | Elinizde hangi ham malzeme var? |
| Zorunlu koşulu karşılar mı? | Evet/hayır |
| Risk | Yağmacı dergi, dilimleme, tekrar yayım riski |

## 🔴 Reddedilecek kısayollar

Kullanıcı şunları önerirse **etik risk uyarısı ver ve yapma**:

- **Dilimleme:** "Tezi 4 makaleye böleyim." → Her makalenin özgün araştırma sorusu ve
  bulgusu olmalı. COPE: "en küçük yayımlanabilir birime" bölmek yasaktır. 🔴
- **Tekrar yayım:** "Aynı çalışmayı TR ve EN olarak iki dergiye vereyim." → Tekrar yayımdır;
  ancak her iki dergiye de bildirip izin alınırsa ve ikincil yayın olduğu belirtilirse
  istisnaî olarak mümkündür. Kesinlikle kendi başına yapılmamalı. 🔴
- **Hediye yazarlık:** "Hocamı yazar ekleyeyim." → Haksız yazarlık. 🔴
- **Yağmacı dergi:** "Hızlı yayımlayan bir dergi bul." → 🔴
  → `/makale-yazim:dergi-secimi` ile tarama zorunlu
- **Coercive citation'a boyun eğme:** hakemin kendi eserini atıflatma baskısı. 🟠

## Çıktı

1. Karşılanmayan zorunlu koşullar (öncelik sırasıyla)
2. Eksik puan ve kapatma seçenekleri tablosu
3. **Önerilen sıra** — en kısa yoldan zorunlu koşulları kapatmak, sonra puan
4. Gerçekçi zaman çizelgesi (dergi süreleri dahil)
5. 🔴 Reddedilen kısayollar ve nedenleri (kullanıcı önerdiyse)
6. `⚠️ Doğrulama notu`

---

## /akademik-yukselme:atama-kriter-kontrol

---
name: atama-kriter-kontrol
description: >
  Dr. Öğr. Üyesi, doçent kadrosu ve profesörlük atamaları için yasal çerçeve ve
  üniversitenin kendi ölçütlerini birlikte kontrol eder.
user-invocable: true
---

# Atama Kriter Kontrolü

## İki katmanlı yapı — kritik

| Katman | Kaynak | Not |
|---|---|---|
| **Yasal asgari** | 2547 sayılı Kanun + Öğretim Üyeliğine Yükseltilme ve Atanma Yönetmeliği | Her yerde geçerli |
| **Üniversite ölçütü** | Hedef üniversitenin kendi atama yönergesi | **Yasal asgarinin üstüne ek koşul koyar** |

> ⚠️ **Üniversite yönergeleri birbirinden çok farklıdır.** Asistan hiçbir üniversitenin
> yönergesini ezberden bilmez. Kullanıcıdan **hedef üniversitenin yönergesini** isteyin;
> yoksa yönergeye yönlendirin (genellikle üniversitenin personel dairesi sayfasında).

## Kadro türleri

| Kadro | Yasal çerçeve (özet) |
|---|---|
| **Dr. Öğretim Üyesi** | Doktora / uzmanlık tamamlanmış olmak; yabancı dil; üniversitenin asgari ölçütleri. Süreli atama, uzatmalı. |
| **Doçent kadrosu** | ÜAK doçentlik unvanı (veya denklik). Unvan ≠ kadro: unvanı alan herkes kadroya atanmaz. |
| **Profesör** | Doçent unvanından sonra ilgili alanda belirli süre çalışmış olmak; alanında uluslararası düzeyde özgün eserler; bir başlıca araştırma eseri. |

> **Unvan ile kadro farkı** akademisyenlerin en sık karıştırdığı noktadır. ÜAK doçentlik
> **unvanını** verir; doçent **kadrosuna** atama üniversitenin işidir ve ayrı ölçütlere tabidir.

## Çıktı

1. Hedef kadro için yasal asgari koşullar
2. Üniversite yönergesi kontrol listesi (kullanıcının yönergesinden çıkarılır)
3. Adayın durumu ile karşılaştırma
4. Eksikler ve tamamlama yolu
5. `⚠️ Doğrulama notu` — *"Yasal çerçeve mevzuattan, ek ölçütler hedef üniversitenin
   yönergesinden okunmalıdır. Süreler ve sayılar mevzuat değişikliğiyle değişir;
   mevzuat.gov.tr üzerinden güncel metni teyit edin."*

## Yapma

- Bir üniversitenin ölçütlerini **ezberden** söyleme.
- Süre ve sayı gibi mevzuat değerlerini doğrulamadan kesinleştirme; Mevzuat MCP'den çek
  veya `[MANUEL DOĞRULAYIN]` işaretle.
