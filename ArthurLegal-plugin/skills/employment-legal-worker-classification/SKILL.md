---
name: employment-legal-worker-classification
description: >
  Önerilen bir çalışma ilişkisini sınıflandırır (Türk hukuku) — işçi (iş
  sözleşmesi), serbest çalışan (eser / vekâlet / serbest meslek), geçici işçi
  (özel istihdam bürosu), alt işveren ya da hizmet alımı — bağımlılık ölçütünü
  ve İş K., TBK, 5510 hükümlerini olgulara uygular; istenen yapı ile olguların
  desteklediği yapı arasındaki boşlukları (muvazaa, 4/b danışman riski)
  işaretler. Yalnız ileriye dönük. "Danışman olarak alalım", "freelancer mı
  işçi mi", "taşeron mu geçici işçi mi", "bu kişiyi nasıl sınıflandıralım"
  denince kullan.
argument-hint: "[önerilen düzenlemeyi anlatın ya da başlayın, ben sorayım]"
---

# /worker-classification — Çalışan Sınıflandırması

En pahalı sınıflandırma kararı, kimsenin bilinçli olarak vermediği karardır: biri "danışman" der, iş başlar, iki yıl sonra olgular iş ilişkisine benzer. Bu skill, iş başlamadan önce ölçütleri olgulara uygular ve anlatılan düzenlemenin kurulmak istenen yapıya uymadığı yeri söyler. Akıl yürütme kalıbını öğretir; kuralın kendisi her seferinde `tr_mevzuat_madde_getir` ile çekilir.

## Örnekler

```
/arthurlegal:employment-legal-worker-classification
6 ay boyunca bir veri bilimciyi analiz ekibimize gömülü, bizim ofisimizde,
bizim araçlarımızla çalıştırmak istiyoruz; serbest meslek makbuzu keser.
```

```
/arthurlegal:employment-legal-worker-classification
İşe alım danışmanı yalnız bize çalışıyor, saatlerini kendi belirliyor,
kendi bilgisayarını kullanıyor, yerleştirme başına ücret alıyor.
```

## ⛔ Yalnız ileriye dönük — girişten ÖNCE sor

> Bu iş başladı mı? Kişi şu anda bu düzenleme altında herhangi bir süredir çalışıyor mu?

**Evetse DUR.** Mevcut ilişkinin sınıflandırılması planlama değil, sorumluluk değerlendirmesidir: geriye dönük işçilik alacakları (kıdem, ihbar, fazla çalışma, yıllık izin — 5 yıllık zamanaşımı, 4857 m. 32/8 ve ek m. 3), SGK hizmet tespiti ve prim/idari para cezası, muvazaa tespiti, vergi düzeltmesi. Bu iş avukat yönetiminde, gizli ve bir iyileştirme planıyla yürür. Aynen şunu yaz ve bekle:

> **Kapsam dışı — mevcut ilişki.** Bu skill bir çalışma ilişkisini *başlamadan önce* analiz eder. Anlattığınız düzenleme zaten var. Geriye dönük sınıflandırma; alacak, SGK ve vergi maruziyetini ve yeniden yapılandırmayı kapsayan ayrı bir risk değerlendirmesidir ve profilin eskalasyon matrisine göre avukata yönlendirilmelidir. Yine de yalnız ileriye dönük planlama için ("bugün sıfırdan kursaydık") analiz istiyorsanız "yine de devam" deyin; çıktı iyileştirme planı değildir, geçmiş dönem maruziyetini hesaplamaz ve avukat onayı olmadan güvenilir sayılmaz.

Yalnız açık "yine de devam" ile ilerle; tereddütlü cevapta yeniden sor. Devam edilirse bu oturumdaki her çıktının başına:

```
⚠️ KAPSAM UYUŞMAZLIĞI — İlişki zaten mevcut. Bu, yalnız planlama amaçlı
ileriye dönük analizdir; iyileştirme planı değildir, geçmiş dönem alacak /
SGK / vergi maruziyetini kapsamaz. Geriye dönük soru eskalasyona işaretlendi.
```

## Bağlamı yükle

`firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → ayak izi, eskalasyon matrisi, varsa geçmiş sınıflandırma uyuşmazlıkları, büronun/şirketin sınıflandırma politikası, `## Outputs`, `## Who's using this`.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:employment-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Bilgi toplama (tek blokta sor)

> Doğru ölçütleri uygulayabilmem için düzenlemeyi ayrıntılı anlamam gerekiyor:
>
> **İş:** Günlük olarak ne yapacak? İş [Müvekkil]'ın asıl işinin parçası mı, yardımcı iş mi? Belirli bir sonucu (eser) mi teslim edecek, yoksa süre boyunca emeğini mi sunacak? Ekipte olmayan bir uzmanlığı var mı?
> **Talimat ve organizasyon:** Saatleri kim belirliyor? Nerede çalışacak? Nasıl çalışacağına (yöntem, sıra) siz mi karar vereceksiniz, yalnız sonucu mu tanımlayacaksınız? Ekibin vardiya/toplantı düzenine dahil olacak mı? Sizin çalışanlarınızı yönetecek mi?
> **Ekonomi:** Ücret saatlik/aylık mı, iş başına mı? Ekipman kimden? Başka müşterilere çalışıyor mu? Zarar riski taşıyor mu? Vergi mükellefiyeti (serbest meslek / şirket) var mı?
> **Yapı:** Doğrudan sözleşme mi, özel istihdam bürosu (geçici işçi) mi, alt işveren mi, şirketten şirkete hizmet alımı mı? Daha önce sizde işçi olarak çalıştı mı? Yazılı sözleşme var mı? Süre?
> **Amaç:** Sınıflandırma hangi sonuç için önemli — iş hukuku hakları, SGK (4/a – 4/b), vergi, İSG? Cevaplar amaca göre ayrışabilir.
> **Yer:** İş fiilen hangi ülkede yapılacak?

Cevapları bekle. Cevaplanamayan sorular analizi etkiler; boşluk olarak not et.

### 2. Uygulanacak ölçütleri belirle (kuralı çek)

| İlişki | Çıpa | Ana ölçüt (metinden doğrula) |
|---|---|---|
| İş sözleşmesi | 4857 m. 8/1; TBK m. 393 | İşçinin işverene **bağımlı** olarak iş görmesi, işverenin ücret ödemesi |
| Eser sözleşmesi | TBK m. 470 | Yüklenicinin bir **eser meydana getirmesi** karşılığında bedel |
| Vekâlet / iş görme | TBK m. 502 | Bir işin görülmesi; düzenlenmemiş iş görme sözleşmelerine de uygulanır |
| Asıl işveren – alt işveren | 4857 m. 2/6-7 | Yardımcı iş ya da asıl işin uzmanlık gerektiren bölümü; alt işveren işçileri yalnız o işyerinde; asıl iş bölünemez (uzmanlık istisnası); eski işçiyle alt işveren ilişkisi kurulamaz, aksi muvazaa → işçiler başlangıçtan itibaren asıl işverenin işçisi |
| Geçici iş ilişkisi | 4857 m. 7; 4904 m. 17 | Yalnız İŞKUR izinli özel istihdam bürosu ya da holding/şirketler topluluğu içi görevlendirme; sınırlı hâller ve süreler |
| Belirli süreli | 4857 m. 11 | Objektif koşul + yazılı; esaslı neden olmadan zincirleme → başlangıçtan belirsiz süreli |
| Kısmi süreli / çağrı üzerine / uzaktan | 4857 m. 13, m. 14 | Çağrı üzerine çalışmada yazılı sözleşme; süre belirlenmemişse haftalık 20 saat; çağrı en az 4 gün önce; uzaktan çalışmada yazılı sözleşme ve zorunlu içerik |
| Deneme süresi | 4857 m. 15 | En çok 2 ay (TİS ile 4 aya kadar) |
| SGK statüsü | 5510 m. 4/1-a, 4/1-b | Hizmet akdiyle çalışan (4/a) – kendi adına ve hesabına bağımsız çalışan (4/b) |
| İş K. kapsamı | 4857 m. 4 | İstisna işlerde TBK hizmet sözleşmesi hükümleri |

Bağımlılığın ölçütleri (talimat altında çalışma, işverenin iş organizasyonuna katılma, süreklilik, ücretin zamana göre ödenmesi, araç-gereç ve işyerinin işverence sağlanması, tek işverene çalışma, kişisel ifa, risk taşımama) kanunda sayılmaz; **yerleşik uygulama ve doktrindir** — `tr_ictihat_ara` ve `scholar_search_legal_scholarship` ile teyit et, karar numarası ezberden yazma.

Vergi boyutu (ücret – serbest meslek kazancı) → `/tax-legal` skill'lerine yönlendir; madde numarası ezberden verilmez.

Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]`, (4) doğrulanmamış diye işaretle ve dur." Her atıf etiketli: `[ArthurLegal TR — 6098 m. 393 — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`.

### 3. Ölçütleri olgulara uygula

Her ölçüt için ayrı tablo; özetleme, puanla:

```
Ölçüt: [ad — kaynak]
Amaç: [iş hukuku / SGK / vergi / İSG]
Kaynak: [madde atfı ya da içtihat künyesi] | Güncellik: [GG.AA.YYYY]

| Unsur | Giriş olgusu | Sinyal |
|---|---|---|
| Talimat / yöntem kontrolü | ... | işçi yönünde / bağımsız yönünde |
| Organizasyona katılma | ... | ... |
| ... | ... | ... |

Ölçütün yapısı: [bütüncül değerlendirme mi, kümülatif şartlar mı — kaynaktan]
Sonuç: [işçi yönünde / bağımsız yönünde / X unsuru belirsiz]
```

Tartışmalı unsurları açıkça işaretle ("tartışmalı — içtihadı kontrol et"); yazılı sözleşmenin adı ("danışmanlık", "hizmet alımı") tek başına belirleyici değildir — olgular esas alınır (yerleşik uygulama).

### 4. Sınıflandır ve boşlukları işaretle

**Sınıflandırma:**
- **İşçi (iş sözleşmesi):** olgular bağımlılığı gösteriyor → SGK 4/a, işe giriş bildirgesi (5510 m. 8), `/arthurlegal:employment-legal-hiring-review`.
- **Bağımsız çalışan (eser / vekâlet / serbest meslek, SGK 4/b):** olgular her amaç için bağımsızlığı destekliyor.
- **Geçici işçi (özel istihdam bürosu):** işçi büronun bordrosunda; m. 7'deki hâl, süre ve oran sınırları; büronun İŞKUR izni ve geçici iş ilişkisi kurma yetkisi (4904 m. 17).
- **Alt işveren:** yalnız m. 2'deki şartlarla; asıl işverenle birlikte sorumluluk.
- **Hizmet alımı (şirketten şirkete):** kişi tedarikçinin işçisi; günlük talimat sizden geliyorsa muvazaa/geçici iş riski.
- **Belirsiz:** hangi ölçüt neden sorunlu.

Amaçlara göre farklı sonuç çıkıyorsa (ör. sözleşme eser görünümlü ama SGK açısından 4/a olgusu) açıkça yaz.

**Boşluk analizi (en önemli çıktı):**

```
İstenen yapı: [söylenen]
Olguların gösterdiği: [ölçütlerin sonucu]

🔴 [Unsur]: [anlatılan] istenen [yapı] ile çelişiyor çünkü [ölçüt + kaynak]. Düzenleme bu hâliyle başlarsa önemli risk.
🟡 [Unsur]: [ölçüt] altında zayıf nokta; tek başına belirleyici değil.
✅ [Unsur]: [yapıyı] destekliyor.
```

Türkiye'de sık görülen 🔴 kalıplar: eski işçinin "danışman" ya da alt işveren işçisi olarak devam etmesi (m. 2/7); asıl işin uzmanlık gerekçesi olmadan bölünmesi (m. 2/7); izinsiz büro üzerinden işçi temini (m. 7; 4904 m. 17); serbest meslek makbuzu kesen ama ekip içinde mesai düzeniyle çalışan kişi (4/a – 4/b).

**Eskalasyon tetikleyicileri** (profil matrisine ek): iş asıl işin parçası ve olgular bağımlılığa işaret ediyor; geçmişte sınıflandırma uyuşmazlığı/denetim; kişi işçileri yönetecek ya da bütçe yetkisi olacak; belirli bir bitişi olmayan uzun süre; sonucu değiştiren tartışmalı unsur.

### 5. Yurt dışında yapılacak iş

Uygulanacak hukuk MÖHUK 5718 m. 27. Yabancı ülkenin ölçütü ezberden yazılmaz: AB `eu_search_eu_law(query="improving working conditions in platform work")`; Hollanda `nl_search_legislation`; İngiltere `uk_search_legislation`; Almanya `de_gesetz_ara`; Azerbaycan `az_search_acts(query="Əmək Məcəlləsi", types=[107])`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

### 6. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="4857", madde_no=["2","7","8","11","14"])
tr_mevzuat_madde_getir(number="6098", madde_no=["393","470","502"])
tr_mevzuat_madde_getir(number="5510", madde_no="4")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="hizmet sözleşmesi eser sözleşmesi ayrımı bağımlılık unsuru", date_from="2022-01-01")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="asıl işveren alt işveren muvazaa uzmanlık", date_from="2022-01-01")
```

## Çıktı

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Çalışan Sınıflandırma Analizi
**Önerilen düzenleme:** [...] | **Yer:** [...] | **Amaç(lar):** [iş hukuku / SGK / vergi / İSG]
**Uygulanan ölçütler:** [liste, her biri kaynak ve güncellik tarihiyle]

## ⚠️ İnceleyen notu
- **En yakın sınıflandırma:** [İşçi / Bağımsız / Geçici işçi / Alt işveren / Hizmet alımı / Belirsiz]
- **Kaynaklar:** [çekilen maddeler, içtihat sayısı; doğrulanamayan]
- **Tartışmalı unsurlar:** [liste]
- **Eskalasyon:** [yok / [isim] — neden]

## Sonuç
[Devam edilebilir / Önce X düzeltilmeli / Dur — tek cümle]

## Ölçüt sonuçları
[Adım 3 tabloları]

## Boşluk analizi
[🔴 / 🟡 / ✅]

## Sonraki adımlar
[Bağımsız yapı uygunsa: sözleşmeye bağımsızlığı destekleyen hükümleri yansıt ve uygulamayı ona göre kur]
[Boşluk varsa: başlamadan önce giderilecekler]
[Büro/tedarikçi yapısı daha temizse: neden]
[İşçi ise: `/arthurlegal:employment-legal-hiring-review`]
```

## Sonuç doğuran işlem kapısı (sınıflandırma kararı)

Nihai "bu yapıyla devam" önerisinden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> Yanlış sınıflandırma geriye dönük işçilik alacakları, SGK primi ve idari para cezası, vergi düzeltmesi ve muvazaa tespitine yol açar. Bu sınıflandırmayı bir avukatla incelediniz mi? Hayırsa götüreceğiniz özet: düzenleme (iş, talimat, ekonomi, yapı); uygulanan ölçütler ve sonuçları; boşluk analizi; açık sorular; en olası risk teorisi; sorulacaklar (bağımsız yapı uygun mu, büro/tedarikçi üzerinden kurmak riski kaldırır mı, sözleşmede hangi hükümler gerekir). Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan nihai öneri verme; "TASLAK" işaretli analiz serbest.

## Bu skill ne yapmaz

- Mevcut ilişkiyi geriye dönük analiz etmez.
- Hizmet/danışmanlık sözleşmesini yazmaz.
- Yanlış sınıflandırma olmuşsa iyileştirme danışmanlığı yapmaz.
- Hiçbir ülkenin kuralını ezberden söylemez.
- Sınırdaki vakalarda avukatın yerini tutmaz.

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; seçimi avukat yapar.

---

## Kaynak katmani — /legal-research (v1.4.0)

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur —
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
