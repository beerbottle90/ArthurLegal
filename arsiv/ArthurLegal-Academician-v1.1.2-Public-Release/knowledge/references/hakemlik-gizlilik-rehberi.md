# Hakemlik ve Editörlük Gizliliği — ÜYZ Yasağı

> Bu paketin en sert kuralıdır. `hakemlik-editorluk` plugin'inin bütün tasarımı buna dayanır.

---

## Kural

**Değerlendirme altındaki yayımlanmamış müsvedde, proje önerisi, tez metni veya hakem
raporu materyalinin herhangi bir kısmının üretken yapay zekâ araçlarına girilmesi,
değerlendiricinin gizlilik yükümlülüğünün ihlalidir.**

Bu, tavsiye değil **yasaktır** ve Türkiye ile uluslararası rejimlerde örtüşür.

---

## Dayanaklar

| Kaynak | Tarih | Hüküm |
|---|---|---|
| **TÜBİTAK — ÜYZ Rehberi § 2.2.1 (Gizlilik Yükümlülüğü)** | — | *"Proje önerileri, yayınlanmamış özgün fikirler, metodolojiler, potansiyel buluşlar ve başvuru sahipleri ile ekip üyelerine ait kişisel veriler gibi son derece hassas ve gizli bilgiler içerir. Bu içeriğin herhangi bir kısmının, ÜYZ araçlarına yüklenmesi veya girilmesi, değerlendiricinin TÜBİTAK Mevzuatı çerçevesinde üstlendiği gizlilik yükümlülüğünün ihlalidir."* |
| **NIH — NOT-OD-23-149**, *The Use of Generative AI Technologies is Prohibited for the NIH Peer Review Process* | 23.06.2023 | Başvuru içeriğinin veya özgün fikirlerin çevrimiçi ÜYZ araçlarına yüklenmesi/paylaşılması, NIH hakemlik gizlilik ve bütünlük gereklerini ihlal eder. Yaptırım: hakem hizmetinin sonlandırılması, devlet çapında men, cezai/hukuki takip. |
| **NSF** — *Use of Generative AI Technology in the NSF Merit Review Process* | Aralık 2023 | Hakemler öneri/değerlendirme içeriğini onaylı olmayan ÜYZ araçlarına yükleyemez; merit review'ın gizlilik ve bütünlük ilkelerini ihlal eder. |
| **Elsevier** — *The use of generative AI and AI-assisted technologies in the review process* | 2023– | *"Reviewers should not upload the manuscript or any part thereof into a generative AI tool"* — gizlilik, telif/mülkiyet ve veri gizliliği haklarını ihlal edebilir. Hakem raporunun kendi metninin bile ÜYZ'ye yüklenmesi yasaktır. |
| **Springer Nature** — Editorial policies | 2023– | Müsveddenin ÜYZ'ye yüklenmesi yasak; yalnızca hakemin kendi rapor metninin dil iyileştirmesi sınırlı izinli. |
| **Wiley** — AI guidelines | 2023– | Hakem sürecinde gizlilik ihlaline karşı yasak/uyarı. |
| **ICMJE Recommendations** | — | Hakemler müsveddenin gizliliğini korumalı; müsveddeyi ÜYZ araçlarına yüklememeli. |
| **Avrupa Komisyonu — Living guidelines** | 2024– | Hakem/değerlendirme süreçlerinde gizli materyal ÜYZ'ye yüklenmemeli. |

> Bazı yayıncı politikalarının güncel metni doğrulanmalıdır; derginin kendi sayfası esastır.

---

## Gerekçe

Akran değerlendirmesinin temel taşı **gizliliktir**. Değerlendirme materyali şunları içerir:

- Yayımlanmamış özgün fikirler ve hipotezler
- Metodolojiler ve potansiyel buluşlar
- Başvuru sahibi ve ekip üyelerine ait kişisel veriler
- Ticari sır niteliğinde bilgiler

Bunların üçüncü taraf bir araca girilmesi, verinin başka amaçlarla kullanılması riskini
doğurur; telif ve fikri mülkiyet haklarını ihlal edebilir; kişisel veriler bakımından
KVKK / GDPR ihlali oluşturur.

---

## Kapsanan roller

| Rol | Kapsanır mı |
|---|---|
| Dergi **hakemi** | ✅ Evet |
| Dergi **editörü** / yayın kurulu üyesi | ✅ Evet |
| Fon **panelisti**, dış danışman, izleyici, raportör | ✅ Evet |
| Tez **jüri** üyesi (savunulmamış tez) | ✅ Evet |
| Doçentlik/atama jüri üyesi (yayımlanmamış eser) | ✅ Evet |
| Kendi yayımlanmamış eseri üzerinde çalışan **yazar** | ❌ Hayır (kendi eseridir) |

---

## Kapsanan materyal

Yasak **metnin bütününe değil, herhangi bir kısmına** ilişkindir:

- ❌ Müsveddenin tamamı
- ❌ Tek bir bölüm veya paragraf
- ❌ **Özet / abstract**
- ❌ **Başlık**
- ❌ Yazar adları ve kurumları
- ❌ Şekil, tablo, veri seti
- ❌ Hakem raporunun kendi metni (Elsevier: dil düzeltmesi için dahi)

> "Sadece özetini vereyim" **istisna değildir.** Özet de müsveddenin parçasıdır.

---

## Yasak OLMAYAN kullanımlar

Bu kural, hakemliğin **süreç** boyutunu kapsamaz. Aşağıdakiler serbesttir çünkü gizli
materyal içermez:

- ✅ Alanınıza uygun bir **değerlendirme rubriği** kurmak
- ✅ Boş bir **hakem raporu iskeleti** üretmek
- ✅ Genel hakemlik ilkeleri, COPE prosedürleri hakkında bilgi almak
- ✅ Derginin **kamuya açık** hakem formunun alanlarını tartışmak
- ✅ Çıkar çatışması kurallarını sorgulamak
- ✅ Editör karar mektubu **şablonu** kurmak (karar türü + hakem tavsiyesi düzeyinde)

Bu paketteki `hakemlik-editorluk` plugin'i tam olarak bu alanda çalışır.

---

## Bu asistanın davranışı

Kullanıcı hakem/editör/panelist/jüri sıfatıyla değerlendirdiği bir metni yapıştırırsa
veya yüklerse, asistan:

1. **Durur.** Metni işlemez, özetlemez, analiz etmez, alıntılamaz; içeriğe dair hiçbir
   çıkarım yapmaz.
2. 🔴 uyarısını verir ve dayanağı gösterir.
3. `/hakemlik-editorluk:hakem-rubrigi`'ne yönlendirir.

Şüphe hâlinde sorar: *"Bu metin sizin kendi eseriniz mi, yoksa değerlendirdiğiniz bir eser mi?"*

---

## Çıkar çatışması (ayrı konu, aynı disiplin)

ÜYZ'den bağımsız olarak, hakemlik teklifini şu hâllerde reddedin:

- Aynı kurumdansınız
- Son yıllarda ortak yayınınız var
- Danışmanlık/danışan ilişkiniz var
- Ticari veya kişisel çıkar ilişkisi var
- Yazarın kimliğini biliyorsanız ve tarafsız olamayacaksanız

**Coercive citation** (hakemin kendi eserlerini atıflatmaya zorlaması) 🔴 etik ihlaldir.

---

## İlgili

`uyz-beyan-rehberi.md` · `yayin-etigi-rehberi.md`
