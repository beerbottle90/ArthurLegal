# expert-opinion - Skill Referans Kitapcigi

> Alan: Bilirkisi raporu + uzman mutalaasi uretimi
> Toplam skill: 3
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.
> Aktif entite: Tum skill'ler company-profile.md -> Bolum 0 'Aktif entite' secimini baz alir
> (varsayilan: [Şirket/Büro adı] -> Bolum A). Cikti dili / onay zinciri / yargi cevresi buradan gelir.

## Icindekiler

- /expert-opinion:bilirkisi-raporu (117 satir)
- /expert-opinion:cold-start-interview (40 satir)
- /expert-opinion:uzman-mutalaasi (94 satir)

---

## /expert-opinion:bilirkisi-raporu

---
name: bilirkisi-raporu
description: >
  Bilirkişi raporu ÜRETİMİ ve karşı rapora İTİRAZ — (a) teknik bilirkişi rapor
  taslağı (Bilirkişilik K. 6754 + HMK m.266-287 / CMK m.62-73), (b) mahkeme/karşı
  bilirkişi raporuna itiraz & ek rapor talebi (HMK m.281). HMK m.266 sınırı: yalnız
  teknik/özel bilgi, hukuki nitelendirme YASAK. Tipik teknik alanlar:
  elektrik/şebeke, EPC hakediş-gecikme, HES su/debi, çevre, İSG kusur, mali zarar.
user-invocable: true
---

# Bilirkişi Raporu Üretimi & İtiraz

> **Şirket içi (in-house) gerçeği:** Şirket personeli kendi davasında bilirkişi atanmaz (çıkar çatışması, HMK m.272 red). Bu skill'in **birincil kullanımı (b) karşı/mahkeme bilirkişi raporuna İTİRAZ**; ikincil (a) bağımsız/dış teknik bilirkişinin rapor **taslaklaması**. Her çıktı **TASLAK** + dış uzman + [Baş Hukuk Müşaviri] onayı.

## İlk soru: hangi mod?
- **(a) Rapor taslağı** — atanmış (dış/bağımsız) bilirkişi adına teknik rapor iskeleti.
- **(b) Rapora itiraz** — eldeki bilirkişi raporunu eleştir + ek rapor/yeni bilirkişi talebi (HMK m.281).

## KRİTİK İLKE (her iki modda)

**HMK m.266 / m.279:** Bilirkişi yalnızca **özel veya teknik bilgi** gerektiren konuda görüş verir. **Hâkimlik mesleğinin gerektirdiği genel ve hukuki bilgiyle** çözülecek konuda bilirkişiye gidilemez; **bilirkişi hukuki nitelendirme/değerlendirme yapamaz** (kusurun hukuki sonucu, sözleşmenin yorumu, tazminata hükmedilmesi → hâkimin işi). Rapor bunu aşıyorsa = **itiraz sebebi**.

## MOD (a) — Teknik bilirkişi rapor taslağı

### Yapı (6754 + BDB rapor standardı)
```markdown
[MAHKEME] — Esas No: [...] — BİLİRKİŞİ RAPORU
Bilirkişi: [ad, uzmanlık alanı, sicil no]   Tarih: GG.AA.YYYY

1. GÖREVLENDİRME VE İNCELEME KONUSU
   [Mahkemenin sorduğu teknik sorular — aynen]
2. DOSYA KAPSAMI / İNCELENEN BELGELER
   [klasör/sayfa, keşif, numune — neyin incelendiği]
3. TEKNİK TESPİTLER (olgu)
   [ölçülebilir, metodolojili: hesap/standart/norm atfı]
4. DEĞERLENDİRME (özel/teknik bilgi — HUKUKİ NİTELENDİRME YOK)
   [sorulara teknik cevap; varsayımlar açık; alternatif senaryolar]
5. SONUÇ (teknik)
   [her soruya net teknik karşılık; takdir mahkemenindir notu]
EKLER: hesap tabloları, standartlar, fotoğraf, kroki
```
- Metodoloji + standart (TS/IEC/şebeke yönetmeliği/EPDK tebliği/YEKDEM hesap esasları) atıfla; `[Mevzuat MCP / doğrulayın]`.
- Belirsizlik/varsayım → açıkça yaz. "Takdir mahkemenindir."

## MOD (b) — Bilirkişi raporuna itiraz (HMK m.281)

### İtiraz sebepleri kontrol listesi (raporu bunlara karşı tara)
- [ ] **Görev/kapsam aşımı** — bilirkişi **hukuki nitelendirme** yapmış mı? (m.266 ihlali)
- [ ] **Eksik inceleme** — dosyadaki belge/keşif/numune dikkate alınmamış
- [ ] **Metodoloji hatası** — yanlış standart/hesap/varsayım; kontrol edilebilir değil
- [ ] **Dosya kapsamı dışı veri** — dayanaksız kabul, taraflardan birine ait varsayım
- [ ] **Çelişki** — rapor içi veya dosyadaki diğer delil/raporla çelişki
- [ ] **Soruların yanıtsızlığı** — mahkeme sorularına cevap vermemiş
- [ ] **Güncel mevzuat/standart** — yürürlükten kalkmış norm kullanımı

### İtiraz dilekçesi taslağı
```markdown
[MAHKEME] SAYIN HAKİMLİĞİ'NE — Esas No: [...]
KONU: GG.AA.YYYY tarihli bilirkişi raporuna İTİRAZLARIMIZ ve EK RAPOR / YENİ
      BİLİRKİŞİ İNCELEMESİ talebimizdir. (HMK m.281)

I. RAPORUN ÖZETİ [bilirkişinin sonucu]
II. İTİRAZLARIMIZ
  1. [Görev aşımı — hukuki nitelendirme: rapor m.266'yı aşmış; örnek alıntı]
  2. [Eksik inceleme — dikkate alınmayan EK-... belgesi]
  3. [Metodoloji/hesap hatası — doğru hesap: ...]
  4. [Çelişki — ...]
III. SONUÇ VE TALEP
  1. İtirazlarımız doğrultusunda **aynı bilirkişiden EK RAPOR** alınmasına,
     (kabul görmezse) **yeni bir bilirkişi/heyetten rapor** alınmasına,
  2. [gerekirse uzman görüşümüzün (HMK m.293) dosyaya kabulüne],
  karar verilmesini talep ederiz. GG.AA.YYYY — Vekil
EKLER: itiraza esas belgeler, (varsa) uzman görüşü
```

## Emsal / dayanak (TR Legal MCP)
```
search_bedesten_unified(phrase="bilirkişi raporu eksik inceleme <teknik konu>",
  birimAdi="<ilgili HD/CD>", kararTarihiStart="2021-01-01")
```
Yerleşik içtihat: "denetime elverişli olmayan rapor hükme esas alınamaz" vb. — yalnızca çekileni işle.

## CMK bilirkişisi (ceza dosyası)
İş kazası/çevre ceza dosyasında bilirkişi → CMK m.62-73; kusur dağılımı raporuna itiraz aynı mantık + CMK usulü. `/advocacy-legal:ceza-dilekce` ile koordine.

## Teknik alan ipuçları
- **Elektrik/şebeke:** kurulu güç, kapasite faktörü, şebeke kısıtı, sayaç/uzlaştırma (EPİAŞ), YEKDEM hesabı `[references/elektrik-uretim-rehberi.md]`
- **EPC/inşaat:** hakediş, gecikme/uzatma analizi (delay), iş artışı, ayıp/kusur
- **HES:** su kullanım hakkı, çevre debisi (can suyu), üretim kaybı hesabı
- **İSG/iş kazası:** kusur dağılımı, kişisel koruyucu, SGK/iş müfettişi raporuyla tutarlılık
- **Mali:** zarar/yoksun kalınan kâr hesabı, faiz, ıskonto

## Çıktı
```markdown
[ÜST BAŞLIK]
# Bilirkişi [Raporu Taslağı / Rapora İtiraz] — [dosya/esas no]

## ⚠️ İnceleyen notu
- **Mod:** (a) rapor taslağı / (b) itiraz
- **İncelenen rapor kapsamı:** [okunan sayfa/bölüm]
- **m.266 sınırı:** [rapor hukuki nitelendirme yapmış mı? evet→güçlü itiraz]
- **Kaynaklar:** Mevzuat/standart [✓/✗]; Yargı MCP emsal [✓ N / ✗]
- **Onay:** dış uzman + [Baş Hukuk Müşaviri] şart

## [Rapor taslağı / İtiraz dilekçesi]
[doldurulmuş]

## Sonraki adımlar
> 1. **Uzman görüşü ile güçlendir** — `/expert-opinion:uzman-mutalaasi`
> 2. **İtirazı dilekçeye bağla** — `/advocacy-legal:ozel-hukuk-dilekce` (HMK m.281)
> 3. **Dış teknik uzman** revizesi
> 4. **Süre takibi** — `/advocacy-legal:yazihane-asistani` (itiraz 2 hafta, HMK m.281)
> 5. **Başka**

**One question I'd ask:** [örn. "Raporun yanlış olduğunu düşündüğümüz teknik nokta, dosyadaki hangi somut belge/ölçümle çürütülüyor? İtiraz ancak somut dayanakla güçlü olur."]
```

---

## /expert-opinion:cold-start-interview

---
name: cold-start-interview
description: >
  expert-opinion eklentisini ilk kez kuran kullanıcı için kısa röportaj — rol,
  tipik teknik alanlar (elektrik/şebeke/EPC/su/çevre/İSG/mali), bilirkişi itirazı mı
  uzman görüşü üretimi mi ağırlıklı, dış uzman/akademisyen havuzu, onay zinciri.
  CLAUDE.md profilini doldurur. `--redo` ile yeniden çalışır.
user-invocable: true
---

# expert-opinion — Cold Start Interview

Amaç: Bu eklentinin `CLAUDE.md` profilindeki `[DOLDUR]` alanlarını 5-7 soruda doldurmak. Önce `company-profile.md` ([Şirket/Büro adı]) okunur.

## Akış

### Adım 0 — Bağlam
`company-profile.md` + bu plugin `CLAUDE.md` + `references/bilirkisilik-rehberi.md` oku. Dolu alanları tekrar sorma.

### Adım 1 — Kullanıcı
> 1. Adın/rolün? ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri] / teknik birim)
> 2. Avukat mısın, hukuk müşaviri mi, teknik uzman mı? (mütalaa imza/sunum farkı için)

### Adım 2 — Kullanım profili
> 3. Daha çok hangisi: (a) karşı/mahkeme **bilirkişi raporuna itiraz**, (b) şirket lehine **uzman görüşü üretimi**, (c) ikisi de?
> 4. En sık teknik alanlar? (elektrik üretim/şebeke · EPİAŞ/YEKDEM fiyatlama · EPC/inşaat hakediş-gecikme · HES su/debi · çevre/ÇED · iş kazası/İSG kusur · mali/zarar hesabı · bilişim)

### Adım 3 — Dış uzman & onay
> 5. Dış uzman/akademisyen havuzu var mı? (alan + isim/kurum, varsa)
> 6. Mütalaa/itiraz sunum öncesi onay zinciri? (varsayılan: dış uzman + [Baş Hukuk Müşaviri] + dış vekil)
> 7. Hukuki mütalaa (legal opinion) da üretilecek mi, yoksa yalnız teknik mi?

### Adım 4 — Yaz ve onayla
Cevapları `CLAUDE.md` `[DOLDUR]` alanlarına işle (özet göster, onay al, yaz). Matter workspace açık mı? Varsayılan: açık.

## Çıktı
Kısa özet + güncellenen alanlar + "Artık `/expert-opinion:bilirkisi-raporu` ve `/expert-opinion:uzman-mutalaasi` kullanabilirsin." yönlendirmesi.

## Not
`--redo`: tüm alanları yeniden sor.

---

## /expert-opinion:uzman-mutalaasi

---
name: uzman-mutalaasi
description: >
  Uzman mütalaası / uzman görüşü ÜRETİMİ (HMK m.293) — şirket lehine taraf delili
  olarak bilimsel/teknik veya hukuki mütalaa taslağı. Yapı: konu & sorular, özet
  görüş, gerekçeli analiz (mevzuat + içtihat + doktrin), sonuç. Bilirkişiden farkı:
  taraf delili, her aşamada sunulabilir. Hukuki mütalaada (legal opinion) doktrin +
  yerleşik içtihat sentezi. Tipik alanlar: enerji/EPC/su/çevre/İSG + ticari hukuk.
user-invocable: true
---

# Uzman Mütalaası (Uzman Görüşü — HMK m.293)

> **HMK m.293:** Taraf, dava konusu uyuşmazlığa ilişkin **kendi seçtiği uzmandan** bilimsel mütalaa (uzman görüşü) alıp dosyaya sunabilir — **taraf delilidir**, her aşamada sunulabilir, ücretini talep eden taraf öder. Bilirkişiden farkı: mahkeme atamaz, tarafsızlık iddiası taşımaz ama **bilimsel/metodolojik** olmak zorundadır (zayıf görüş karşı tarafça çürütülür). Her çıktı **TASLAK** — fiilen mütalaayı **uzman/akademisyen imzalar**; şirket/büro için [Baş Hukuk Müşaviri] onayı.

## İlk soru: mütalaa türü?
- **Teknik/bilimsel mütalaa** — mühendislik/mali/aktüeryal (örn. HES üretim kaybı hesabı, EPC gecikme analizi, kusur dağılımı, zarar/yoksun kâr).
- **Hukuki mütalaa (legal opinion)** — bir hukuki sorunun doktrin + yerleşik içtihat ışığında analizi (örn. sözleşme hükmünün yorumu, lisans devri rejimi, force majeure, zamanaşımı). *Not: mahkemeye sunulan uzman görüşü genelde teknik konuda güçlüdür; hukuki mütalaa daha çok strateji/ikna + emsal akademik destek içindir.*

## Yapı (her iki tür için iskelet)

```markdown
UZMAN GÖRÜŞÜ (HMK m. 293)
Hazırlayan: [Uzman ad — unvan/akademik kariyer — uzmanlık alanı]
Talep eden: [Müvekkil / Şirket] vekili Av. [ad]
İlgili dava: [Mahkeme — Esas No]   Tarih: GG.AA.YYYY

I. KONU VE YÖNELTİLEN SORULAR
   [Cevaplanması istenen somut soru(lar) — net]
II. İNCELENEN BELGELER / VERİ
   [dosya kapsamı, teknik veri, sözleşme]
III. ÖZET GÖRÜŞ (yönetici özeti)
   [2-4 cümlede ana sonuç]
IV. GEREKÇELİ ANALİZ
   [Teknik: metodoloji + hesap + standart/norm atfı + alternatif senaryolar]
   [Hukuki: ilgili mevzuat `[Mevzuat MCP]` + yerleşik içtihat `[Yargı MCP]`
    + doktrin `[yazar/eser — doğrulayın]` sentezi; karşı argümanların ele alınması]
V. SONUÇ
   [Soru(lar)a net, gerekçeli cevap; varsayım/sınırlamalar açık]
   [İmza/kaşe alanı — uzman]
EKLER: özgeçmiş (uzmanlık ispatı), hesap tabloları, kaynak listesi
```

## İlkeler (mütalaayı güçlü kılan)
- **Metodoloji şeffaf:** her sonuç izlenebilir hesap/standart/kaynağa dayanmalı.
- **Karşı argümanı ele al:** güçlü mütalaa, aleyhe görüşü tartışıp neden zayıf olduğunu gösterir (yalnızca lehe seçmece değil).
- **Aşırılıktan kaçın:** abartılı/tek yanlı görüş itibar kaybettirir; "taraf delili ama bilimsel" dengesi.
- **Hukuki nitelendirme:** uzman görüşü (özellikle hukuki mütalaa) bilirkişiden farklı olarak hukuki yorum yapabilir, ama **mahkemeyi bağlamaz**; "nihai takdir mahkemenindir".
- **Atıf disiplini:** içtihat/madde **TR Legal MCP'den çekilir**; doktrin atfı doğrulanır. **Uydurma kaynak = mütalaanın çürütülmesi.**

## Kaynak (TR Legal MCP)
```
search_mevzuat / get_mevzuat_document   # dayanak madde metni
search_bedesten_unified(phrase="<hukuki sorun>", birimAdi="<ilgili daire>")  # yerleşik içtihat
search_anayasa_unified                  # AYM (anayasal boyut varsa)
```
Sektörel teknik dayanak: `references/elektrik-uretim-rehberi.md`, `references/ced-rehberi.md`, `references/isg-dava-rehberi.md`, `references/bilirkisilik-rehberi.md`.

## Tipik mütalaa konuları
- HES üretim/su kullanım kaybı, çevre debisi etkisi hesabı (teknik)
- EPC gecikme/uzatma hakkı, hakediş/iş artışı, ayıp analizi (teknik)
- EPDK lisans devri / pay devri rejimi, YEKDEM hak kazanımı yorumu (hukuki)
- Force majeure / aşırı ifa güçlüğü (TBK m.138) enerji sözleşmesinde (hukuki)
- İş kazası kusur dağılımı + tazminat hesabı (teknik+mali)
- Sözleşme yorumu / sınırlı sorumluluk klozu geçerliliği (hukuki)

## Bilirkişi raporuna karşı mütalaa
Karşı/mahkeme bilirkişi raporu zayıfsa, **uzman görüşü** o raporu çürütmek için güçlü araçtır → `/expert-opinion:bilirkisi-raporu` (itiraz) ile **birlikte** sunulur (itiraz dilekçesi + ekinde uzman görüşü).

## Çıktı
```markdown
[ÜST BAŞLIK]
# Uzman Görüşü Taslağı — [tür] — [konu]

## ⚠️ İnceleyen notu
- **Tür:** teknik / hukuki
- **Yöneltilen soru(lar):** [N adet]
- **Kaynaklar:** Mevzuat MCP [✓ N / ✗]; Yargı MCP [✓ N emsal / ✗]; doktrin [✓/doğrulanmalı]
- **Metodoloji:** [hesap/standart belirtildi mi]
- **Sınırlama/varsayım:** [N adet]
- **Onay:** uzman/akademisyen imzası + [Baş Hukuk Müşaviri] şart (taslak imzasız geçersiz)

## Uzman görüşü taslağı
[doldurulmuş iskelet]

## Sonraki adımlar
> 1. **Dış uzman/akademisyen** ile içeriği teyit + imza
> 2. **Bilirkişi raporu itirazına ekle** — `/expert-opinion:bilirkisi-raporu`
> 3. **Dilekçeye delil olarak bağla** — `/advocacy-legal:ozel-hukuk-dilekce` / `:kamu-hukuku-dilekce`
> 4. **Emsal/doktrin güçlendir** — TR Legal MCP
> 5. **Başka**

**One question I'd ask:** [örn. "Bu mütalaayı imzalayacak uzmanın alandaki tanınırlığı/akademik ağırlığı ne? Uzman görüşünün ikna gücü, imzalayanın otoritesiyle doğru orantılı."]
```

---
