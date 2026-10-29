---
name: ip-legal-ip-clause-review
description: >
  Bir sözleşmedeki fikri mülkiyet klozlarını inceler — devir, sahiplik, lisans,
  garanti ve tazmin. İş, danışmanlık, iş paketi (SOW), tedarik ya da lisans
  sözleşmesinde fikri haklar incelenirken, devir dili ya da lisans kapsamı
  sorulduğunda ya da fikri mülkiyet hükmü içeren bir sözleşme yapıştırıldığında
  kullan. Türk hukuku tabanı: FSEK m. 18, 48-52 (yazılı şekil, hakların ayrı
  ayrı gösterilmesi, gelecekteki eserler), m. 14-16 (manevi haklar), SMK m. 73,
  148, 158, TBK m. 20-25 (genel işlem koşulları); çalışan buluşları
  /arthurlegal:ip-legal-invention-intake'e yönlendirilir.
argument-hint: "[dosya yolu | Drive bağlantısı | metin]"
---

# /ip-clause-review

Sözleşmenin fikri mülkiyet klozlarını `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` profiline göre inceler: devir boşlukları, sahiplik belirsizliği, lisans kapsamı, garanti/tazmin sorunları. Çıktı: risk sırasına dizilmiş, gerektiğinde redline önerili kloz kloz not.

## Talimat

1. **Profili yükle.** Yer tutucu varsa dur: "Önce `/arthurlegal:ip-legal-cold-start-interview` — klozları profilinize göre inceleyebilmem için pratiğinizi öğrenmeliyim."
2. **Sözleşmeyi al:** dosya, bağlantı ya da metin; yoksa iste.
3. **Akışı izle:** sözleşme türünü ve fikri haklar bakımından hangi tarafta olduğumuzu belirle (her belgede ayrı sorulur); iş/danışmanlık/SOW belgesinde önce devir boşluğu kontrolü; risk sırasına göre kloz bulguları; çapraz tutarlılık; yargı çevresi notu.
4. **Notu yaz** (şablon aşağıda): üst başlık, sonuç, devir boşluğu, önem sırasına göre klozlar, tutarlılık, yargı çevresi, onay yönlendirmesi.
5. **Karar duruşu:** bir kloz fikri hakkı iki yönde de okunabiliyorsa avukata işaretle, iki yöndeki etkenleri göster; sessizce karar verme.

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Açık ve aktif matter yoksa sor ("`/arthurlegal:ip-legal-matter-workspace switch <slug>` ya da `practice-level`"). `matter.md` sapmalarını yükle; çıktıları `matters/<matter-slug>/` altına yaz; `Cross-matter context` `on` değilse başka matter okunmaz.

## Amaç

Avukata her klozun ne yaptığını, piyasadan ya da ekibin standart duruşundan nasıl saptığını, riskini ve gerekiyorsa önerilecek redline'ı tek geçişte söyle. **En yüksek riskli klozlar sahiplik ve devirdir;** sonradan düzeltilmeleri zordur ve birleşme/devralma inceleme sürecinde, finansmanda ya da davada yıllar sonra ortaya çıkar. Devir dili olması gereken bir belgede zayıf ya da yoksa notun en üstünde yüksek sesle işaretle.

Profil şunları söyler: yargı çevresi ayak izi (manevi hak feragatinin geçerliliği, işçi eseri rejimi, örtülü lisans), sapmaları kimin hangi önemde onayladığı (`## Enforcement posture` → `Approval matrix`, `Automatic escalations`), üst başlık (`## Outputs`).

## Akış

### Adım 1: Yönlen

| Soru | Cevap |
|---|---|
| Sözleşme türü | İş / danışmanlık ya da SOW / tedarik çerçeve / lisans alma / lisans verme / iş birliği-Ar-Ge / sulh / devralma ya da varlık devri / diğer |
| Fikri haklarda tarafımız | hak veren mi alan mı / devreden mi devralan mı / lisans veren mi alan mı |
| Karşı taraf | ad; birey mi, girişim mi, büyük şirket mi |
| Fikri hak için ayrı bedel | ücret, lisans bedeli, peşin ödeme, pay, yok |
| Uygulanacak hukuk ve yetki | ne diyor; profil bu yargı çevresini eskalasyon/asla listesinde mi işaretliyor |

Taraf belirsizse (iki yönlü katkılı iş birliği, akışlı hakları olan bayilik) sor: "[Müvekkil] bu sözleşmenin fikri haklarında hangi tarafta — veren, alan, ikisi? İkisiyse iki yönü ayrı incelerim."

### Adım 2: Devir boşluğu kontrolü (en yüksek öncelik)

İş, danışmanlık, SOW, ısmarlama iş ya da şirketin karşı tarafın ürettiği işten hak alması gereken her belgede **önce** bunu yap.

**Telif (FSEK):**
- **Yazılı şekil ve hakların tek tek sayılması:** mali haklara ilişkin sözleşme ve tasarruflar yazılı olmalı ve konu olan haklar ayrı ayrı gösterilmelidir (FSEK m. 52). "Tüm fikri haklar devredilmiştir" gibi genel ifade yerine işleme, çoğaltma, yayma, temsil, umuma iletim (m. 21-25) ayrı ayrı; süre, yer ve muhteva bakımından kapsam (m. 48/1). Mali haklar birbirine bağlı değildir; birinin devri diğerini kapsamaz (m. 20/1). Sayılmayan hak geçmez → 🔴.
- **Gelecekteki eserler — ABD "hereby assigns" alışkanlığı burada ters işler:** henüz vücuda getirilmemiş ya da tamamlanacak esere ilişkin **tasarruf** batıldır (m. 48/3); aynı konudaki **taahhüt** ise eser vücuda gelmeden yapılsa da geçerlidir (m. 50/1). Doğru yapı: devir **taahhüdü** + eser teslim edildiğinde/vücuda geldiğinde yazılı **devir** (teslim tutanağına bağlanmış). Eser sahibinin ileride vücuda getireceği eserlerin bütününe ya da belirli türüne ilişkin taahhüdü her taraf, ihbardan bir yıl sonra hüküm ifade etmek üzere feshedebilir (m. 50/2) — uzun süreli çerçeve sözleşmede not et. İleride çıkacak mevzuatın tanıyacağı hakların devri batıldır (m. 51).
- **Çalışan eseri:** özel sözleşmeden ya da işin mahiyetinden aksi anlaşılmadıkça memur, hizmetli ve işçilerin **işlerini görürken** meydana getirdikleri eserler üzerindeki haklar onları çalıştıranlarca kullanılır (m. 18/2). Kapsam ("işlerini görürken") tartışmaya açık olduğundan iş sözleşmesinde açık hüküm yine de öner. **Danışman ve serbest çalışan** bu kuralın dışındadır → açık, yazılı, hakları sayan devir şart (m. 52).
- **Zincir:** mali hakkı ya da ruhsatı devralan, onu ancak eser sahibinin **yazılı muvafakatiyle** başkasına devredebilir; işleme hakkında da aynı (m. 49). Tedarikçinin çalışanlarının ya da alt yüklenicilerinin eserleri bize gelecekse: tedarikçiden hak zinciri beyanı ve gerekli muvafakatler. m. 18/2 kapsamındaki eserlerde muvafakat gereğinin kapsamı **tartışmalı — içtihadı kontrol et.**
- **Manevi haklar:** umuma arz, adın belirtilmesi ve değişikliği men yetkisi eser sahibindedir (m. 14-16). Şeref ve itibarı zedeleyen yayımı ve eserin mahiyetini bozan değişikliği men yetkisinden sözleşmeyle vazgeçmek **hükümsüzdür** (m. 14/3, 16/3). "Manevi haklardan tam feragat" klozunun bu kısmı geçersizdir; yapılabilecek olan: adın belirtilmemesine, yayım zamanı/tarzına ve teknik değişikliklere yazılı izin + hakkı kullanmama taahhüdü — sınırını notta söyle.
- **Önceden var olan haklar (background):** karşı tarafın devir dışında tuttuğu liste somut mu, açık uçlu mu? Teslim edilen işin kullanılması için gereken ölçüde lisans var mı?

**Tasarım:** çalışanın işinde yaptığı tasarımda hak sahibi, aksi kararlaştırılmadıkça işverendir; hizmet ilişkisi dışındaki iş görme sözleşmelerinde hak sahipliği sözleşmeye göre belirlenir (SMK m. 73/1, 73/4) → danışman sözleşmesinde açık hüküm şart.

**Buluş:** çalışan buluşlarına ilişkin hükümler emredicidir; işveren çalışan aleyhine düzenleme yapamaz ve sözleşme serbestliği hizmet buluşunda patent başvurusundan sonra başlar (SMK m. 117/1; hizmet buluşu tanımı m. 113). İş sözleşmesindeki "tüm buluşlar şirkete aittir" klozunu bu çerçevede **`/arthurlegal:ip-legal-invention-intake`** ile yürüt (bildirim, talep süreleri ve bedel orada). Danışmanın buluşunda sözleşme belirleyicidir — açık hüküm.

**Marka devri:** sınai haklara ilişkin hukuki işlemler yazılıdır; devir sözleşmesinin geçerliliği noter onayına bağlıdır (SMK m. 148/4). Sicile kaydedilmeyen işlemden doğan haklar iyiniyetli üçüncü kişilere karşı ileri sürülemez (m. 148/5).

Eksik ya da zayıfsa notun en üstüne:

```markdown
## ⚠️ DEVİR BOŞLUĞU
**Madde [X]** iş ürünündeki hakları devrediyor, ancak: [ör. "haklar ayrı ayrı sayılmamış (FSEK m. 52)" / "gelecekteki eserler 'şimdiden devredilmiştir' diye yazılmış (FSEK m. 48/3)" / "danışman sözleşmesinde devir hükmü yok" / "marka devri noter onaysız (SMK m. 148/4)"].
**Risk:** Yıllar sonra inceleme sürecinde çıkan türden bir boşluk; karşı tarafın ya da halefinin bizim sandığımız işte hakkı kalabilir.
**Önerilen redline:** > "[somut metin]"
**Eskalasyon:** profil gereği devir kapsamı boşlukları [onaylayan]'a gider.
```

**YZ ile üretilen içerik:** eser, sahibinin hususiyetini taşıyan ürün; sahibi onu meydana getiren kişidir (FSEK m. 1/B-a, b; m. 8). İnsan katkısı olmayan YZ çıktısının eser sayılıp sayılmadığı **tartışmalı** — devir yalnız var olan hakkı devredebilir. Danışman/geliştirici YZ kullanacaksa: YZ kullanım beyanı, bildirim yükümlülüğü ve YZ destekli kısımları ayırt edecek mekanizma var mı? Yoksa 🟠: "Devir klozu iyi ama YZ kullanım beyanı yok; YZ içeriğinin hak durumu belirsiz ve hangi kısmın etkilendiğini bilemezsiniz." `[review — YZ çıktısının eser niteliği gelişen bir alan; güncel içtihat ve doktrini kontrol et: tr_ictihat_ara(query="yapay zeka eser sahibi"), scholar_search_legal_scholarship]`. YZ'nin buluşa katkısı → `/arthurlegal:ip-legal-invention-intake`.

### Adım 3: Kloz kloz inceleme

Aranacak klozlar: devir · teslim edilen işin sahipliği · geliştirmeler ve işlenmeler (FSEK m. 1/B-c işlenme eser) · önceden var olan/yeni haklar ayrımı · **lisans** (kapsam, münhasırlık, ülke, kullanım alanı, alt lisans, süre, fesih, bedel) · fikri mülkiyet garantileri (üçüncü kişi hakkını ihlal etmeme, yetki, özgünlük) · tazmin (kapsam, tavan, usul, istisnalar) · manevi haklar · açık kaynak beyanları (→ `/arthurlegal:ip-legal-oss-review`) · marka kullanımı (kalite denetimi, kullanım rehberi) · gizlilik ve ticari sır (haksız rekabet tabanı TTK m. 55/1-d; NDA → `/arthurlegal:commercial-legal-nda-review`).

**Türk hukukunda lisansa özgü kontroller:**
- **Dava hakkı:** sözleşmede aksi kararlaştırılmamışsa inhisari (münhasır) lisans alan, hak sahibinin açabileceği davaları kendi adına açabilir; münhasır olmayan lisans alan önce hak sahibinden dava açmasını ister, üç ay içinde açılmazsa kendi adına açabilir (SMK m. 158/1-2). Lisans veren tarafsak bu hakkı sınırlamak, alan tarafsak korumak isteriz.
- **Kapsam aşımı:** lisansla verilen hakları izinsiz genişletmek ya da üçüncü kişilere devretmek marka hakkına tecavüzdür (SMK m. 29/1-ç). Telifte ruhsat sahibi de hakkı ancak eser sahibinin yazılı muvafakatiyle devredebilir (FSEK m. 49).
- **Tescil:** sicile kaydedilmeyen lisans iyiniyetli üçüncü kişilere karşı ileri sürülemez (SMK m. 148/5).
- **Yazılım lisansı:** programı hukuka uygun edinen kişinin programı yüklemesi, çalıştırması, hataları düzeltmesi ve kullanım için gerekli bir yedek kopya alması sözleşmeyle önlenemez (FSEK m. 38/4) — bunları yasaklayan kısıt geçersizlik riski taşır.
- **Standart metin (genel işlem koşulu):** karşı tarafın önceden hazırladığı lisans/kullanım şartlarındaki aleyhe hükümler, açıkça bilgi verilip kabul edilmedikçe yazılmamış sayılır; sözleşmenin niteliğine yabancı olanlar da (TBK m. 21); dürüstlüğe aykırı aleyhe hüküm konulamaz (m. 25); "her madde tartışıldı" kaydı tek başına yetmez (m. 20/3).
- **Tazmin ("indemnity"):** Türk hukukunda ayrı bir kurum olarak değil sözleşmesel tazmin taahhüdü olarak yazılır; kapsam, bildirim süresi ve savunmayı kimin yöneteceği açık olmalı (ayrıntı: `/arthurlegal:commercial-legal-vendor-agreement-review`).

Her kloz için:

```markdown
### [Madde X.X]: [Kloz adı]
**Ne diyor:** [bir-iki cümle]
**Piyasa / standart (bu tür, bu taraf, bu hukuk):** [kısa]
**Risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
**Neden önemli:** [olduğu gibi kalırsa iş için ne ters gider]
**Önerilen redline (gerekirse):** > "[somut metin]"
**Karar notu:** [kloz amaçlanan dağılımı sağlıyor mu belirsizse avukata işaretle, iki yönü göster]
```

| Seviye | Anlamı |
|---|---|
| 🔴 Kritik | Düzeltmeden imzalama. Olması gereken belgede devir yok; haklar sayılmamış (FSEK m. 52); gelecekteki eserde tasarım hatası; dar olması gereken lisans sınırsız; münhasır olmaması gereken münhasır. |
| 🟠 Yüksek | Güçlü ısrar, olmazsa eskalasyon. Belirsiz kapsam; manevi hak düzenlemesi yok ya da geçersiz feragat; hak zinciri beyanı yok; dar tazmin. |
| 🟡 Orta | İlk turda iste, son açık konuysa kabul. Kozmetik ama belirsiz dil; standarttan kısa süreler. |
| 🟢 Düşük | Not et, sermaye harcama. Dağılımı değiştirmeyen üslup farkı. |

### Adım 4: Çapraz tutarlılık

Fikri mülkiyet klozları sistem olarak bozulur: lisans verilen kapsamla uyumlu mu ("kullanma" lisansı "kullanma, değiştirme, işleme" lisansından dardır)? Garanti verilen her şeyi kapsıyor mu (yalnız patente sınırlı ihlal etmeme garantisi telif ve sırrı açıkta bırakır)? Tazmin garantinin vaat ettiğini kapsıyor mu? Fesih lisansı geri alıyor mu, bedeli ödenmiş lisans fesihten sonra sürüyor mu — niyetle uyumlu mu? SOW, sipariş formu ya da yan mektupla dağılım çelişiyor mu?

### Adım 5: Yargı çevresi notu

- **Hakkın kendisi** koruma talep edilen ülkenin hukukuna tabidir (MÖHUK m. 23/1); sözleşmenin hukuk seçimi hakkın varlığını ve kapsamını değiştirmez. Sözleşmeye uygulanacak hukuk ve yetki/tahkim için `/arthurlegal:commercial-legal-governing-law-review`.
- **Türk hukuku kontrol listesi:** yazılı şekil ve hakların sayılması (FSEK m. 52) · gelecekteki eser (m. 48/3, 50) · manevi hak sınırı (m. 14/3, 16/3) · işçi eseri kuralı ve danışman ayrımı (m. 18/2) · marka devrinde noter onayı (SMK m. 148/4) · çalışan buluşlarının emredici rejimi (SMK m. 117). Örtülü lisans (yazılı hüküm sessizken kullanım izni çıkarımı) Türk hukukunda m. 52 karşısında **tartışmalı**.
- **Yabancı hukuk:** kuralı ezberden yazma; araç kullan — AB yazılım/telif: `eu_search_eu_law(query="legal protection of computer programs")`, `eu_search_eu_law(query="copyright related rights information society")`; Birleşik Krallık: `uk_search_legislation(title="Copyright, Designs and Patents Act")`; Almanya: `de_` araçları (ör. `de_gesetz_ara` ile UrhG). Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

Hangi hukukun uygulandığını ve profilin o yargı çevresini standart / eskalasyon / asla olarak işaretleyip işaretlemediğini yaz.

## Redline ayrıntı düzeyi

**En küçük birimde düzelt.** Bütün klozu değiştirmek "metninizi attık" demektir; cerrahi redline "belirli taleplerimiz var" der ve daha hızlı kabul edilir. Sıra: kelime → ifade → alt bent → cümle → kloz. Klozu tümden yeniden yazman gerekiyorsa iletim notunda söyle: "Değişiklikler kapsamlı olduğundan 8.2'yi işaretlemek yerine yeniden yazdık; farkı birlikte geçebiliriz."

### Adım 6: Notu birleştir

Notun başına `## Outputs` üst başlığını koy (role göre). Not ve sözleşme gizli olabilir; dar çevrede dağıt, dışarı göndermeden önce başlığı çıkar.

> **Sessiz tamamlama yok.** Araç bir kural için az sonuç döndürürse bulduğunu bildir ve dur; web ya da hafızadan sessizce doldurma. Seçenek: sorguyu genişlet, başka araç, `[web araması — doğrula]` etiketiyle web, ya da "doğrulanmadı" diye bırak.
>
> **Kaynak etiketi:** `[ArthurLegal TR — 5846 FSEK m. X — GG.AA.YYYY]`, araç adı, `[kullanıcı verdi]` (karşı taraf taslağı ya da büro dosyası), `[model bilgisi — doğrula]`, `[web araması — doğrula]`. Etiketleri silme; her madde `tr_mevzuat_madde_getir` ile çekilir, çekilemeyen için UYARI satırı.

```markdown
[ÜST BAŞLIK — profil ## Outputs]
# Fikri Mülkiyet Klozu İncelemesi: [Karşı taraf] [Sözleşme türü]
**İncelendi:** [tarih] · **Fikri haklarda tarafımız:** [veren / alan / ikisi] · **Uygulanacak hukuk:** [ ]
---
## Sonuç
[İki cümle. Dağılım ayakta kalır mı? Önce ne değişmeli?]
**Bulgular:** [N]🔴 [N]🟠 [N]🟡 [N]🟢 · **Onay gereken:** [profildeki isim]
## Devir boşluğu kontrolü
[✅ Temiz | ⚠️ Boşluk var — yukarıda]
## Önem sırasına göre klozlar
[Adım 3 blokları, Kritik → Düşük]
## Çapraz tutarlılık
## Yargı çevresi notu
## Onay yönlendirmesi
[profilden — kim onaylar, otomatik eskalasyonlar]
> ⚠️ **İnceleyen notu:** Bu not avukat incelemesi içindir; gelecekteki eser, manevi hak ve YZ çıktısı başlıklarındaki "tartışmalı" işaretleri imzadan önce kapatılmalıdır.
```

## Karar duruşu

Kloz fikri hakkı iki yönde de okunabiliyorsa ya da seçilen kelimelerin amaçlanan sonucu doğurup doğurmadığı belirsizse **avukata işaretle, iki yöndeki etkenleri göster.** İmzalanmış çözümsüz bir dağılım tek yönlü kapıdır; sonradan "sorun yokmuş" denilen bir işaret iki yönlü.

## Teslimden önce kalite kontrolü

- [ ] Profil yüklendi; yargı çevresi notu profille uyumlu
- [ ] İş/danışmanlık/SOW belgesinde önce devir boşluğu kontrol edildi (m. 52, 48/3, 50, 18/2, 49)
- [ ] Her 🔴 ve 🟠 için somut redline
- [ ] Çapraz tutarlılık kontrol edildi
- [ ] Atıflar etiketli ve doğrulanmış; `doğrula` etiketleri silinmedi
- [ ] Onaylayan profildeki isimle yazıldı ("hukuka eskale et" değil)
- [ ] Üst başlık eklendi

## Sonraki adım ağacı

`## Outputs`'taki sonraki adım ağacıyla kapat; seçenekleri bu çıktıya göre özelleştir (redline'ı yaz, eskale et, olgu topla, bekle-izle, başka bir şey). Ağaç çıktıdır; avukat seçer.
