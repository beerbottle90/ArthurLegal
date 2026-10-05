# hakemlik-editorluk — Skill Referans Kitapçığı

> Kapsam: Hakemlik, editörlük, panel değerlendirmesi, tez jüriliği
> Toplam skill: 4
> Kullanım: `/hakemlik-editorluk:<skill-adı>`
>
> 🔴 **BU PLUGIN MÜSVEDDE METNİ İSTEMEZ VE KABUL ETMEZ.**
> Metin okumaz; **süreç yürütür.** Bu bir eksiklik değil, mevzuatın gereğidir.

---

## ⛔ Gizlilik kapısı — her skill'den önce çalışır

Değerlendirme altındaki **yayımlanmamış** müsvedde, proje önerisi, tez metni veya hakem
raporu materyalinin **herhangi bir kısmının** üretken yapay zekâ araçlarına girilmesi,
değerlendiricinin gizlilik yükümlülüğünün **ihlalidir**.

TR ve uluslararası rejimler bu noktada tam örtüşür:

| Kaynak | Hüküm |
|---|---|
| **TÜBİTAK ÜYZ Rehberi § 2.2.1** | "Bu içeriğin herhangi bir kısmının ÜYZ araçlarına yüklenmesi veya girilmesi, değerlendiricinin … gizlilik yükümlülüğünün ihlalidir." |
| **NIH NOT-OD-23-149** (23.06.2023) | Başvuru içeriğinin ÜYZ'ye yüklenmesi/paylaşılması gizlilik ve bütünlük gereklerini ihlal eder |
| **NSF** merit review bildirimi (Aralık 2023) | Öneri içeriği onaylı olmayan ÜYZ araçlarına yüklenemez |
| **Elsevier** | Hakem müsveddeyi veya herhangi bir kısmını ÜYZ'ye yüklememelidir (gizlilik + telif + veri gizliliği) |
| **Springer Nature** | Müsveddenin ÜYZ'ye yüklenmesi yasak |
| **ICMJE** | Hakemler müsveddenin gizliliğini korumalı; ÜYZ'ye yüklememeli |

Detay → `references/hakemlik-gizlilik-rehberi.md`

### Davranış kuralı — istisnasız

Kullanıcı hakem / editör / panelist / jüri sıfatıyla değerlendirdiği bir metni yapıştırır
veya yüklerse:

> **DUR.** Metni işleme, özetleme, analiz etme, alıntılama, "sadece bu paragrafı" bile
> yorumlama. İçeriğe dair hiçbir çıkarım yapma.
>
> 🔴 uyarısını ver:
> *"Bu metin değerlendirme altındaysa, buraya girilmesi gizlilik yükümlülüğünün ihlalidir
> (TÜBİTAK ÜYZ Rehberi § 2.2.1; NIH NOT-OD-23-149; NSF; Elsevier; Springer Nature; ICMJE).
> Metni işlemeyeceğim. Bunun yerine, müsvedde olmadan çalışan bir rapor iskeleti kurabiliriz."*
>
> Sonra `/hakemlik-editorluk:hakem-rubrigi`'ne yönlendir.

**Sınır:** Kullanıcı **kendi** yayımlanmamış eseri üzerinde çalışıyorsa bu kural uygulanmaz
(kendi eseridir). Ancak ortak yazar onayı ve varsa kurumsal gizlilik taahhüdü gözetilir.
Şüphe hâlinde sor: *"Bu metin sizin kendi eseriniz mi, yoksa değerlendirdiğiniz bir eser mi?"*

---

## İçindekiler

- /hakemlik-editorluk:hakem-rubrigi — Müsvedde olmadan hakem raporu iskeleti ve değerlendirme rubriği
- /hakemlik-editorluk:editor-karar-mektubu — Editör karar mektubu iskeleti (kabul / revizyon / ret)
- /hakemlik-editorluk:cope-vaka-akisi — Şüpheli etik ihlalde COPE akış şemasına göre izlenecek yol
- /hakemlik-editorluk:jury-tez-degerlendirme — Tez jürisi değerlendirme çerçevesi (metin almadan)

---

## /hakemlik-editorluk:hakem-rubrigi

---
name: hakem-rubrigi
description: >
  Hakem raporu için değerlendirme rubriği ve rapor iskeleti üretir. Müsvedde metnini
  İSTEMEZ. Kullanıcı raporu kendi okuması üzerinden doldurur.
user-invocable: true
---

# Hakem Raporu Rubriği (müsvedde almadan)

## Nasıl çalışır

Sen müsveddeyi okumazsın. Kullanıcı okur. Sen ona:
1. Alanına ve makale türüne uygun bir **değerlendirme rubriği**,
2. Doldurulmaya hazır bir **rapor iskeleti**,
3. Kaçırılması muhtemel noktalar için bir **kontrol listesi**

verirsin. Kullanıcı kendi gözlemlerini yazar.

## Girdi (metin İSTEME)

- Makale **türü**: kuramsal/dogmatik · karşılaştırmalı · ampirik · olay incelemesi · derleme
- **Alan**: örn. ceza hukuku, vergi hukuku
- **Dergi düzeyi**: TR Dizin · SSCI/AHCI · uluslararası hakemli
- **Derginin hakem formu** var mı? Varsa alanlarını iste (form yapısı gizli değildir).
- Kaç kelime rapor bekleniyor?

> Başlık, özet veya herhangi bir cümle **isteme**. Bunlar da müsveddenin parçasıdır.

## Rubrik — hukuk makalesi için

| Boyut | Sorulacak sorular |
|---|---|
| **Özgünlük** | Literatürde boşluk gerçekten var mı? Katkı artımsal mı, esaslı mı? |
| **Araştırma sorusu** | Açıkça formüle edilmiş mi? Cevaplanabilir mi? |
| **Yöntem** | Dogmatik/karşılaştırmalı/ampirik yöntem beyan edilmiş mi, tutarlı uygulanmış mı? |
| **Kaynak yeterliliği** | Temel monografiler ve güncel içtihat var mı? Yabancı literatür gerekliyse kullanılmış mı? |
| **Atıf disiplini** | Dipnotlar doğrulanabilir mi? Kaynak eskimiş mi? İkincil kaynaktan birincil kaynağa atıf yapılmış mı? |
| **Argüman yapısı** | İddia → dayanak → karşı görüş → çürütme zinciri kurulu mu? |
| **Karşı görüş** | Baskın karşıt doktrin ele alınmış mı, yoksa görmezden mi gelinmiş? |
| **İçtihat kullanımı** | Kararlar bağlamıyla mı, cherry-picking mi? Güncel mi? |
| **Sonuç** | Bulgulardan çıkıyor mu, yoksa fazla mı iddialı? |
| **Etik** | Ampirik ise etik kurul izni beyan edilmiş mi? ÜYZ beyanı var mı? |
| **Biçim** | Derginin yazım kurallarına uygun mu? |

## Rapor iskeleti (kullanıcı doldurur)

```
HAKEM RAPORU — [Dergi] — [Makale kodu]

1. ÖZET DEĞERLENDİRME (3-5 cümle)
   Makalenin ne yaptığı ve genel kanaat.

2. GÜÇLÜ YÖNLER
   - …

3. ESASLI ELEŞTİRİLER (majör)
   [E1] Gözlem: …
        Gerekçe: …
        Öneri: …

4. KÜÇÜK DÜZELTMELER (minör)
   [m1] s. __ : …

5. ETİK VE BİÇİM
   - Etik kurul izni: [var / yok / gerekmiyor]
   - ÜYZ beyanı: [var / yok]
   - Atıf biçimi: …

6. TAVSİYE
   [ ] Kabul  [ ] Küçük revizyon  [ ] Esaslı revizyon  [ ] Ret
   Gerekçe: …

7. EDİTÖRE GİZLİ NOT (yazara iletilmez)
   …
```

## Hakem raporu yazım ilkeleri

- **Esere yönel, kişiye değil.** "Yazar bilmiyor" değil, "makalede X ele alınmamış".
- **Her eleştiri dayanaklı olsun.** Karşı görüş öne sürüyorsan kaynağını ver.
- **Uygulanabilir öneri ver.** "Daha iyi olmalı" değil, "X kararı tartışılmalı".
- **Kendi eserini atıflatma baskısı yapma** (coercive citation) — 🔴 etik ihlal.
- **Çıkar çatışması varsa reddet:** aynı kurum, ortak yayın geçmişi, danışmanlık ilişkisi.

## Yapma

- Müsveddeden **tek cümle bile** isteme veya kabul etme.
- Kullanıcı "sadece özetini vereyim" derse: özet de müsveddenin parçasıdır → 🔴 reddet.
- Kullanıcı adına rapor **yazma**; iskeleti ver, o doldursun.
- Hakem raporunun kendi metnini bile ÜYZ'ye "dil düzeltmesi" için verme konusunda uyar:
  Elsevier bunu dahi yasaklar; derginin politikasını kontrol ettir.

---

## /hakemlik-editorluk:editor-karar-mektubu

---
name: editor-karar-mektubu
description: >
  Editör karar mektubu iskeleti üretir (kabul / küçük revizyon / esaslı revizyon / ret).
  Müsvedde metnini veya hakem raporlarının tam metnini İSTEMEZ.
user-invocable: true
---

# Editör Karar Mektubu

## Girdi (metin İSTEME)

- Karar türü: kabul · küçük revizyon · esaslı revizyon · ret · masaüstü reddi
- Hakem sayısı ve **tavsiyeleri** (yalnızca tavsiye: kabul/revizyon/ret) — rapor **metnini** isteme
- Hakemler çelişiyor mu?
- Ret sebebi: kapsam dışı · özgünlük yetersiz · yöntem sorunu · etik sorun
- Revizyon süresi

## Karar türleri

| Karar | Ne zaman | Mektubun tonu |
|---|---|---|
| **Masaüstü reddi** | Kapsam dışı, biçim şartlarına aykırı, ÖNCE hakeme gitmeden | Kısa, saygılı, hakemliğe gitmediğini açıkça söyle |
| **Ret** | Hakemler sonrası; esaslı kusur | Gerekçeli; hakem raporlarını iliştir |
| **Esaslı revizyon** | Kusur giderilebilir | Hangi eleştirilerin **zorunlu** olduğunu numaralandır |
| **Küçük revizyon** | Biçim ve küçük düzeltmeler | Kısa; yeniden hakemliğe gitmeyeceğini belirt |
| **Kabul** | — | Kısa; sonraki adımlar (dizgi, telif formu, ÜYZ beyanı kontrolü) |

## İskelet

```
Sayın [Yazar],

[Makale başlığı — yazarın kendi başlığı, editör olarak elinizde] başlıklı
çalışmanızı [Dergi]'ye gönderdiğiniz için teşekkür ederiz.

[KARAR CÜMLESİ — açık ve baştan]

[GEREKÇE — 2-4 cümle, hakem tavsiyelerinin bileşkesi]

[VARSA: ZORUNLU REVİZYON KALEMLERİ, numaralı]

[VARSA: SÜRE ve YENİDEN GÖNDERİM YÖNTEMİ]

[Hakem raporları ilişiktedir / ekte sunulmuştur.]

Saygılarımızla,
[Editör]
```

## Hakemler çelişirse

1. Üçüncü hakeme gönder, veya
2. Editör olarak gerekçeli tercih yap ve bunu mektupta **açıkla**, veya
3. Yazardan hakem eleştirilerine karşı görüş iste.

Hangisini seçtiğini yazara söyle. Sessizce bir hakemi yok saymak 🟠 şeffaflık sorunudur.

## Yapma

- Hakem kimliğini ifşa etme (çift-kör süreçte).
- Hakem raporlarının **tam metnini** bu asistana verme — tavsiye ve tema düzeyinde konuş.
- Kendi dergine atıf yapmasını yazara şart koşma (coercive citation) — 🔴.

---

## /hakemlik-editorluk:cope-vaka-akisi

---
name: cope-vaka-akisi
description: >
  Editör veya kurum, yayımlanmış ya da gönderilmiş bir çalışmada etik ihlal şüphesiyle
  karşılaştığında izlenecek prosedürü COPE akış şemalarına göre kurar. Vaka metnini İSTEMEZ.
user-invocable: true
---

# COPE Vaka Akışı

## Kapsam

Şu şüphelerde uygulanır: intihal · veri sahteciliği · tekrar yayım / dilimleme ·
haksız yazarlık · sahte hakemlik · açıklanmamış çıkar çatışması · açıklanmamış ÜYZ katılımı.

## Temel prosedür (COPE)

1. **Şüpheyi belgele.** Somut, doğrulanabilir gözlem; kanaat değil.
2. **Yazara sor.** Suçlama değil, açıklama talebi. Makul süre ver.
3. **Cevabı değerlendir.** Tatmin edici mi?
4. **Gerekirse kurumu bilgilendir.** Yazarın kurumu soruşturmayı yürütür; dergi değil.
5. **Karar:** düzeltme (correction) · endişe bildirimi (expression of concern) ·
   geri çekme (retraction).
6. **Şeffaflık.** Geri çekme bildirimi **ücretsiz erişilebilir** ve makaleye **bağlantılı**
   olmalıdır; gerekçesi açıkça yazılmalıdır.

## Düzeltme mi, geri çekme mi?

| Durum | Sonuç |
|---|---|
| Küçük hata, sonuçları etkilemiyor | **Correction** |
| Ciddi şüphe var ama soruşturma sürüyor | **Expression of concern** |
| Bulgular güvenilmez (sahtecilik, ciddi hata) | **Retraction** |
| İntihal | **Retraction** |
| Tekrar yayım | **Retraction** |
| Etik ihlalle elde edilmiş veri | **Retraction** |

> Geri çekme bir **ceza değil, kaydın düzeltilmesidir**. COPE bunu açıkça söyler.

## Çıktı

- Vakanın sınıflandırması
- Adım adım prosedür ve her adımda **kim sorumlu** (dergi / editör / kurum)
- Yazara gönderilecek **açıklama talebi mektubu iskeleti**
- Zaman çizelgesi önerisi
- `⚠️ Doğrulama notu`: COPE'un güncel akış şemasını ve derginin kendi yönergesini teyit et

## Yapma

- Vakanın metnini veya yazarın kimliğini isteme.
- Suçlayıcı dil kullanma; "şüphe", "açıklama talebi", "inceleme" de.
- Soruşturmayı derginin yürütmesini önerme — **yazarın kurumu** yürütür.

---

## /hakemlik-editorluk:jury-tez-degerlendirme

---
name: jury-tez-degerlendirme
description: >
  Tez jürisi üyesi için değerlendirme çerçevesi ve soru seti üretir. Tez metnini İSTEMEZ.
user-invocable: true
---

# Tez Jürisi Değerlendirme Çerçevesi (metin almadan)

## Gizlilik

Savunulmamış tez metni **yayımlanmamış eserdir**. Jüri üyesi olarak metni bu asistana
giremezsiniz. Metni siz okursunuz; buradan **çerçeve** ve **soru seti** alırsınız.

## Değerlendirme boyutları

| Boyut | Ne aranır |
|---|---|
| **Özgünlük** | Doktora: alana özgün katkı zorunlu. YL: yetkinlik yeterli. |
| **Problem kurgusu** | Araştırma sorusu net, sınırlandırılmış, cevaplanabilir mi? |
| **Yöntem** | Beyan edilmiş ve tutarlı uygulanmış mı? Ampirikse etik kurul izni var mı? |
| **Literatür hâkimiyeti** | Temel eserler ve güncel tartışma kapsanmış mı? |
| **Atıf disiplini** | Dipnotlar doğrulanabilir mi? İntihal/benzerlik raporu sunuldu mu? |
| **ÜYZ beyanı** | Kurumun formu dolduruldu mu? |
| **Argümanın bağımsızlığı** | Öğrencinin kendi tezi mi, danışmanın tezi mi? |
| **Yazım ve biçim** | Kurumun tez yazım kılavuzuna uygunluk |

## Savunma soru seti (uyarlanabilir)

- "Araştırma sorunuzu bir cümlede nasıl ifade edersiniz?"
- "Bu tezin literatüre eklediği tek cümlelik katkı nedir?"
- "Yönteminizin en zayıf noktası nedir ve bunu nasıl telafi ettiniz?"
- "Tezinizin sonucuna en güçlü karşı argüman ne olurdu?"
- "Şu içtihat/doktrin sizin sonucunuzla nasıl bağdaşıyor?"
- "Bu bulguyu bir sonraki adımda nereye taşırdınız?"

## Karar seçenekleri

`Kabul` · `Düzeltme (süreli)` · `Ret` — kurumun lisansüstü yönetmeliği esastır; süreler
ve yeniden savunma usulü kurumdan kuruma değişir.

## Çıktı

Çerçeve + soru seti + değerlendirme formu iskeleti + `⚠️ Doğrulama notu`
(kurumun lisansüstü eğitim yönetmeliğini teyit et).

## Yapma

- Tez metnini, özetini veya bölüm başlıklarını isteme.
- Öğrenci hakkında kişisel değerlendirme üretme; esere odaklan.
