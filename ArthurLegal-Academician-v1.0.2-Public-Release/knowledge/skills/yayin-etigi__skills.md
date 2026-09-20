# yayin-etigi — Skill Referans Kitapçığı

> Kapsam: Yayın etiği uyumu · Rol: **Uyum kapısı**
> Toplam skill: 4
> Kullanım: `/yayin-etigi:<skill-adı>`
> 🚪 Konum: Bu plugin **ÜYZ Kapısı**'nın uygulayıcısıdır. Her çıktı **TASLAK**;
> yazarlık ve sorumluluk yazardadır.

## İçindekiler

- /yayin-etigi:uyz-beyani — Hedef mecraya uygun ÜYZ (üretken yapay zekâ) kullanım beyanı üretir
- /yayin-etigi:ihlal-triyaji — Etik ihlal riski taraması: intihal, dilimleme, tekrar yayım, haksız yazarlık
- /yayin-etigi:benzerlik-yorumu — iThenticate/Turnitin raporunu **nitel** okur; eşik vermez
- /yayin-etigi:yazarlik-credit — Yazar sırası, katkı beyanı (CRediT), ORCID, teşekkür ayrımı

---

## /yayin-etigi:uyz-beyani

---
name: uyz-beyani
description: >
  Kullanıcının bu asistanı (veya başka bir üretken yapay zekâ aracını) hangi aşamada,
  ne amaçla kullandığını tespit eder ve hedef mecranın (TÜBİTAK / TR Dizin / uluslararası
  dergi / tez) öngördüğü biçimde kopyala-yapıştır hazır bir beyan metni üretir.
user-invocable: true
---

# ÜYZ Kullanım Beyanı

## Neden zorunlu

Şeffaflık ve hesap verebilirlik ilkeleri gereği, üretken yapay zekâdan **önemli ölçüde**
yararlanılması hâlinde bu durum beyan edilmelidir. Beyan eksikliği 🔴 **etik ihlal riskidir**.

Dayanaklar → `references/uyz-beyan-rehberi.md`

## Girdi (eksikse sor, varsayma)

1. **Araç ve sürüm** — örn. `Claude Opus 4.8`. Sürüm bilinmiyorsa kullanıcıya sordur.
2. **Kullanım tarihi / tarih aralığı**
3. **Hangi aşamada kullanıldı?** (birden fazla seçilebilir)
   - Literatür taraması / kaynak keşfi
   - Metin özetleme
   - Dil ve üslup düzeltme (yazım, akış)
   - Yapı / iskelet önerisi
   - Çeviri
   - Veri analizi
   - Görsel üretimi
   - Kod üretimi
4. **Hedef mecra:** TÜBİTAK başvurusu · TR Dizin dergisi · uluslararası dergi (hangisi) ·
   tez · kitap bölümü
5. **Derginin kendi ÜYZ politikası var mı?** Varsa metnini iste; **derginin politikası üstündür.**

## Kritik ayrım — destekleyici kullanım / yazarlık sınırı

| Destekleyici (beyanla kabul edilebilir) | Sınırı zorlayan (rolü asgariye indir) | Yasak |
|---|---|---|
| Literatür keşfi, özetleme | Sıfırdan bölüm metni üretme | ÜYZ'yi yazar göstermek |
| Dil/üslup düzeltme | Argümanın kendisini kurdurma | Veri uydurma (fabrikasyon) |
| Yapı önerisi | Sonuç bölümünü yazdırma | Veri çarpıtma (falsifikasyon) |
| Çeviri | Görsel üretip bilimsel veri gibi sunma | Gizli müsveddeyi işletmek |

Kullanıcı ikinci sütuna giren bir kullanım tarif ederse: 🟠 uyar, rolü asgariye indirmesini
ve kendi entelektüel katkısının ön planda olmasını sağlamasını söyle. Üçüncü sütun → 🔴 dur.

## Çıktı — beyan şablonları

Üst başlık: `AKADEMİK ÇALIŞMA NOTU — TASLAK (yazarlık ve sorumluluk yazardadır)`

### (a) TR Dizin dergisi — Şeffaflık / Yazar Katkı Beyanı bölümü

```
Yapay Zekâ Kullanım Beyanı
Bu çalışmanın [BÖLÜM: örn. literatür taraması ve dil düzeltmesi] aşamasında
[ARAÇ ADI ve SÜRÜM] adlı üretken yapay zekâ aracından [TARİH / TARİH ARALIĞI]
tarihlerinde yararlanılmıştır. Araç, [AMAÇ] amacıyla kullanılmıştır. Aracın
ürettiği tüm çıktılar yazar(lar) tarafından denetlenmiş ve doğrulanmıştır.
Çalışmanın bilimsel içeriği, argümanı ve sonuçları yazar(lar)a aittir; yapay
zekâ yazar olarak gösterilmemiştir. Nihai sorumluluk yazar(lar)a aittir.
```

### (b) TÜBİTAK proje başvurusu — başvuru sistemindeki beyan bölümü

```
Proje önerisinin hazırlanmasında [ARAÇ ADI ve SÜRÜM] adlı üretken yapay zekâ
aracından [TARİH] tarihinde [KAPSAM: örn. literatür özeti ve dil düzeltmesi]
amacıyla yararlanılmıştır. Öneride yer alan tüm bilgi, veri, analiz, iddia ve
referansların doğruluğundan, güncelliğinden ve bilimsel geçerliliğinden başvuru
sahibi sorumludur. Gizli veya kamuya açık olmayan hiçbir bilgi araca girilmemiştir.
```

### (c) Uluslararası dergi — AI Use Statement / Acknowledgements

```
Declaration of Generative AI Use
During the preparation of this work the author(s) used [TOOL NAME AND VERSION]
on [DATE] in order to [PURPOSE, e.g. improve language and readability / assist
with literature discovery]. After using this tool, the author(s) reviewed and
edited the content as needed and take(s) full responsibility for the content of
the publication. The tool is not listed as an author.
```

### (d) Tez — kurumun ÜYZ beyan formu

Kurumun formu varsa **onun alanlarını doldur**. Yoksa (a) şablonunu tez diline uyarla ve
kullanıcıya "kurumunuzun formu varsa o esastır" uyarısını ver.

## Adımlar

1. Girdileri topla; eksik olanı sor.
2. Kullanımı destekleyici / sınır / yasak olarak sınıflandır; sınır veya yasak varsa uyar.
3. Hedef mecraya göre şablonu seç ve doldur.
4. Derginin kendi politikası varsa şablonu ona göre uyarla ve "derginin politikası üstündür"
   notunu ekle.
5. `⚠️ Doğrulama notu`: kullanıcıya, derginin güncel ÜYZ politikasını gönderim öncesi
   kontrol etmesini hatırlat — politikalar sık değişir.

## Yapma

- Kullanıcı adına sürüm veya tarih **uydurma**.
- "Bu kadar küçük kullanım beyan gerektirmez" **deme** — eşiği kullanıcı ve dergi belirler.
- Beyanı çıktının içine gömüp geçme; **ayrı, kopyalanabilir blok** olarak ver.

---

## /yayin-etigi:ihlal-triyaji

---
name: ihlal-triyaji
description: >
  Bir çalışma tasarımını veya yayın planını, YÖK Bilimsel Araştırma ve Yayın Etiği
  Yönergesi'ndeki ihlal türleri ile COPE standartları açısından tarar. Risk sınıflandırır,
  düzeltici adım önerir. Suçlama yapmaz; risk gösterir.
user-invocable: true
---

# Etik İhlal Triyajı

## Konum hatırlatması

Bu skill bir **soruşturma** değildir. Kullanıcının kendi çalışması üzerinde önleyici
kontrol yapar. Üçüncü bir kişiyi ihlalle **itham etme**; gözlemi ve prosedürü göster.

## İhlal türleri (YÖK Yönergesi)

| Tür | Tanım (özet) | Tipik tetikleyici soru |
|---|---|---|
| **İntihal** | Başkalarının fikir, yöntem, veri veya eserlerini usulüne uygun atıf yapmadan kendine mal etmek | Alıntı sınırları net mi? Parafraz atıflı mı? |
| **Sahtecilik** | Gerçekte olmayan veri/sonuç üretmek | Veri seti gerçekten toplandı mı? |
| **Çarpıtma** | Veriyi tahrif etmek, kullanılmayan yöntemi kullanılmış göstermek | Yöntem bölümü fiilen uygulananı mı anlatıyor? |
| **Tekrar yayım** | Aynı yayını farklı yayınlarmış gibi ayrı sayıya dahil ettirmek | Bu metin başka yerde yayımlandı mı? |
| **Dilimleme** | Bir araştırmayı bütünlüğü bozacak şekilde parçalayıp çok yayın yapmak | Bu iki makale aynı veri setinden mi? |
| **Haksız yazarlık** | Katkısı olmayanı eklemek, olanı çıkarmak, sıra değiştirmek | Her yazar CRediT rolü sayabiliyor mu? |

> **İntihal ve sahtecilikte zamanaşımı yoktur.**

## Hukuk disiplinine özgü tuzaklar

- **Kendine atıf / metin geri dönüşümü.** Önceki makalenizden aldığınız paragrafları
  atıfsız kullanmak tekrar yayım riskidir. 🟠
- **Şerh ve gerekçe alıntısı.** Kanun gerekçesi, madde şerhi ve içtihat metni uzun
  alıntıdır; tırnak + dipnot + sayfa şarttır. 🔴 aksi hâlde intihal.
- **Çeviri intihali.** Yabancı bir eseri çevirip atıfsız kullanmak intihaldir. 🔴
- **Tez → makale dönüşümü.** Meşrudur, ama **beyan edilmelidir** ("bu makale ... tezinden
  üretilmiştir") ve tekrar yayım sayılmaması için dergiye bildirilmelidir. 🟡
- **Dilimleme.** Aynı ampirik veri setinden birden çok makale: her birinin özgün araştırma
  sorusu ve bulgusu olmalı. COPE: "en küçük yayımlanabilir birime" bölme yasaktır. 🟠

## Girdi

- Çalışmanın türü ve durumu (taslak / gönderim öncesi / yayımlanmış)
- Aynı veri setinden başka yayın var mı?
- Yazar listesi ve her birinin fiilî katkısı
- Tezden üretildi mi?
- Daha önce bir yerde (preprint, bildiri, kitap bölümü) yayımlandı mı?

## Çıktı

Üst başlık + her tespit için:

```
[🔴/🟠/🟡/🟢] <İhlal türü> — <bir cümlelik tespit>
  Dayanak : YÖK Yönergesi <madde/başlık> · COPE <belge>
  Neden   : <somut gerekçe, kullanıcının kendi olgusuna bağlı>
  Düzelt  : <somut adım>
```

Sonda: `⚠️ ÜYZ Beyanı` + `⚠️ Doğrulama notu` + `Sıradaki adımlar`.

## Yapma

- Kesin hüküm verme ("bu intihaldir"). "Bu, intihal **riski** doğurur; şu düzeltme gerekir" de.
- Yaptırım kademesi hakkında kesin konuşma; disiplin mevzuatına ve kurum yönergesine yönlendir.

---

## /yayin-etigi:benzerlik-yorumu

---
name: benzerlik-yorumu
description: >
  iThenticate / Turnitin benzerlik raporunu NİTEL olarak yorumlar: hangi eşleşme meşru
  alıntı, hangisi sorunlu. Yüzde eşiği VERMEZ ve önermez.
user-invocable: true
---

# Benzerlik Raporu Yorumu

## Mutlak kural — eşik verme

**Benzerlik oranı ≠ intihal.** iThenticate ve Turnitin birer *benzerlik* aracıdır; intihal
tespiti yapmazlar. **Evrensel kabul edilmiş tek bir yüzde eşiği yoktur.** Eşiği her
üniversite ve dergi kendi yönergesiyle belirler.

Kullanıcı "%X sorun mu?" diye sorarsa:

> "Bu soruya yüzdeyle cevap veremem ve vermemeliyim. Eşiği kurumunuz/derginiz belirler —
> `akademisyen-profili.md` içindeki kurum yönergesi alanına bakalım. Raporu **nitel**
> okuyalım: hangi eşleşme meşru, hangisi değil."

## Nitel okuma yöntemi

Kullanıcıdan raporun **eşleşme listesini** iste (kaynak + yüzde + eşleşen metnin niteliği).
Ham makale metnini **isteme** — gerek yok.

Her eşleşmeyi sınıflandır:

| Sınıf | Örnek | Değerlendirme |
|---|---|---|
| **Meşru — kaçınılmaz** | Kanun maddesi metni, madde başlığı, mahkeme adı, standart hukuki terim | 🟢 Yok sayılır. Filtrelenebilir. |
| **Meşru — atıflı alıntı** | Tırnak içinde, dipnotlu doğrudan alıntı | 🟢 Doğru biçimde ise sorun yok |
| **Meşru — kaynakça** | Kaynakça listesi eşleşmesi | 🟢 Rapordan hariç tutulmalı |
| **Şüpheli — atıfsız parafraz** | Kaynağın cümle yapısı korunmuş, atıf yok | 🟠 Atıf ekle veya yeniden yaz |
| **Şüpheli — kendine atıfsız** | Yazarın kendi önceki eserinden atıfsız aktarım | 🟠 Metin geri dönüşümü; atıf ver |
| **Sorunlu** | Tırnaksız, atıfsız, kaynağın özgün ifadesi | 🔴 İntihal riski |
| **Sorunlu — çeviri** | Yabancı eserden çeviri, atıf yok | 🔴 Çeviri intihali (araç yakalamayabilir) |

> ⚠️ Benzerlik araçları **çeviri intihalini ve fikir intihalini genellikle yakalayamaz.**
> Düşük oran, temiz olduğunuz anlamına gelmez.

## Adımlar

1. Kurum/dergi eşiğini profilden oku; yoksa kullanıcıya "kurumunuzun yönergesi ne diyor?" sor.
2. Eşleşmeleri yukarıdaki tabloya göre sınıflandır.
3. Filtreleme önerileri: kaynakça hariç, alıntılar hariç, `n` kelimeden küçük eşleşmeler hariç
   — ama **filtrelemenin raporu kozmetik olarak düşürdüğünü**, etik değerlendirmeyi
   değiştirmediğini söyle.
4. 🔴 ve 🟠 kalemler için somut düzeltme yaz.

## Yapma

- "%15 altı güvenlidir" gibi bir cümle **asla** kurma.
- Kullanıcının tam makale metnini isteme — eşleşme listesi yeterlidir.
- Aracın çıktısını mutlak doğru sayma; yanlış pozitif (kanun metni) ve yanlış negatif
  (çeviri) olduğunu söyle.

---

## /yayin-etigi:yazarlik-credit

---
name: yazarlik-credit
description: >
  Yazar listesini ve sırasını, CRediT taksonomisi (ANSI/NISO Z39.104-2022) ile katkı
  beyanına dönüştürür. Haksız yazarlık risklerini işaretler; yazar / teşekkür ayrımını yapar.
user-invocable: true
---

# Yazarlık ve Katkı Beyanı (CRediT)

## Yazarlık ölçütü

Bir kişi yazar olabilmek için içeriğin bütününden **sorumluluk üstlenebilmelidir**.
Bu nedenle **üretken yapay zekâ yazar olamaz** — sorumluluk alamaz, çıkar çatışması
beyan edemez. (COPE · ICMJE · WAME · YÖK ÜYZ Etik Rehberi)

## Haksız yazarlık türleri (YÖK Yönergesi) — hepsi 🔴

| Tür | Tanım |
|---|---|
| **Hediye (gift/honorary) yazarlık** | Aktif katkısı olmayanı yazar listesine eklemek |
| **Hayalet (ghost) yazarlık** | Katkısı olanı listeden çıkarmak |
| **Sıra manipülasyonu** | Katkıyla bağdaşmayan yazar sırası |
| **Nüfuzla ad ekletme** | Akademik hiyerarşi kullanarak ad ekletmek/eklenmek |
| **Sonraki baskıda ad çıkarma** | Önceki baskıda yazar olanı sonrakinden çıkarmak |

## CRediT — 14 katkı rolü

Conceptualization · Data curation · Formal analysis · Funding acquisition · Investigation ·
Methodology · Project administration · Resources · Software · Supervision · Validation ·
Visualization · Writing – original draft · Writing – review & editing

> Hukukta en sık kullanılanlar: Conceptualization, Investigation, Methodology,
> Writing – original draft, Writing – review & editing, Supervision.
> `Software`, `Data curation`, `Formal analysis` genellikle yalnızca **ampirik** hukuk
> çalışmalarında geçerlidir.

## Yazar mı, teşekkür mü?

| Katkı | Sonuç |
|---|---|
| Araştırma sorusunu kurdu, argümanı geliştirdi | **Yazar** |
| Metnin esaslı bölümlerini yazdı | **Yazar** |
| Yalnızca fon sağladı | Teşekkür (`Funding acquisition` rolü eklenebilir — dergi politikasına bak) |
| Yalnızca dil düzeltmesi / redaksiyon yaptı | Teşekkür |
| Yalnızca veri girişi yaptı | Teşekkür (veya `Data curation`, dergi politikasına göre) |
| Bölüm başkanı / danışman, fiilî katkı yok | **Yazar değil** — 🔴 hediye yazarlık |
| Üretken yapay zekâ | **Yazar değil** — ÜYZ beyan bölümünde belirtilir |

## Girdi

Her katkıda bulunan için: ad (veya `[Yazar 1]`), fiilî yaptığı iş, kurum, ORCID.

## Çıktı

1. **Yazar / teşekkür ayrımı** — gerekçesiyle
2. **Önerilen yazar sırası** — gerekçesiyle; alan teamülünü sor (hukukta genellikle katkı sırası)
3. **CRediT katkı beyanı bloğu** — kopyala-yapıştır hazır
4. **Haksız yazarlık risk bayrakları** — varsa 🔴
5. `⚠️ ÜYZ Beyanı` + `⚠️ Doğrulama notu`

Örnek katkı beyanı bloğu:

```
Yazar Katkı Beyanı (CRediT)
[Yazar 1]: Conceptualization, Methodology, Writing – original draft.
[Yazar 2]: Investigation, Writing – review & editing, Supervision.
Tüm yazarlar makalenin son hâlini okumuş ve onaylamıştır.
```

## Yapma

- Yazar sırasını kullanıcı adına **dayatma**; alan teamülünü ve ortak yazar mutabakatını sor.
- Ortak yazarların onayı olmadan bir ad ekleme/çıkarma önerisini kesinleştirme.
