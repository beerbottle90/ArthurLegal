---
name: employment-legal-hiring-review
description: >
  İş teklifi ve iş sözleşmesi incelemesi (Türk hukuku) — sözleşme türü ve
  şekli, deneme süresi, ücret ve çalışma süresi hükümleri, rekabet yasağı
  (TBK m. 444-447), gizlilik ve ceza koşulu, işe alımda ayrımcılık yasağı,
  aday verisinin KVKK uyumu, işe giriş zorunlulukları (SGK bildirimi, yabancı
  çalışma izni, engelli kotası). "Bu teklifi incele", "rekabet yasağı koyabilir
  miyiz", "iş sözleşmesine bak", "yurt dışından işe alım" denince ya da teklif
  eklendiğinde kullan.
argument-hint: "[teklif mektubu / iş sözleşmesi dosyası ya da işe alımı anlatın]"
---

# /hiring-review — İşe Alım İncelemesi

Teklif mektupları çoğunlukla kalıptır; ta ki olmayana kadar. Değer üreten yerler sözleşme türü/şekli, rekabet yasağı ve işe alım sürecinin ayrımcılık + kişisel veri boyutudur. Kural ezberden söylenmez; her madde `tr_mevzuat_madde_getir` ile çekilir.

## Destination check

- **Müvekkile / İK'ya inceleme notu** → profil `## Outputs` başlığı
- **Adaya gidecek teklif / sözleşme** → yalnız temiz metin; iç yorumlar, risk notları ve pazarlık pozisyonu çıkarılır
- **İlan metni** → ayrımcılık kontrolünden geçmiş, aday aydınlatma metniyle birlikte

## Bağlamı yükle

`firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → ayak izi, işe alım inceleme tetikleyicileri, rekabet yasağı politikası, teklif şablonu yeri, `## Outputs`, `## Who's using this`.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:employment-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Yer ve uygulanacak hukuk

İş nerede yapılacak — merkezin değil, kişinin bulunduğu yer. Türkiye dışında ise: tarafların seçtiği hukuk, işçinin mutad işyeri hukukunun emredici asgari koruması saklı kalmak üzere uygulanır (MÖHUK 5718 m. 27). Yabancı ülke kuralı ezberden yazılmaz: İngiltere `uk_search_legislation(query="Employment Rights Act 1996")`, Almanya `de_gesetz_ara`, Hollanda `nl_search_legislation`, İrlanda `ie_search_acts`, AB `eu_search_eu_law(query="transparent and predictable working conditions")`, Azerbaycan `az_search_acts(query="Əmək Məcəlləsi", types=[107])`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al." Ayak izinde olmayan yeni bir ülke ise işaretle: "Bu ülkede ilk işe alım; teklif gitmeden önce araştırma gerekli."

### 2. Sözleşme türü ve şekli (4857 s.K.)

| Kontrol | Kural (metinden doğrula) | Çıpa |
|---|---|---|
| Şekil | Süresi 1 yıl ve daha fazla sözleşme yazılı; yazılı sözleşme yoksa en geç 2 ay içinde çalışma koşullarını gösteren yazılı belge | m. 8/2-3 |
| Belirli süre | Objektif koşul + yazılı; esaslı neden olmadan zincirleme yapılamaz | m. 11 |
| Kısmi / çağrı üzerine / uzaktan | Ayrımcılık yasağı, orantılı ödeme; çağrı ve uzaktan çalışmada yazılı sözleşme ve zorunlu içerik | m. 13, m. 14 |
| Deneme süresi | En çok 2 ay (TİS ile 4 aya kadar); bu sürede bildirimsiz ve tazminatsız fesih | m. 15 |
| Bağımsız çalışan mı? | Olgular bağımlılık gösteriyorsa iş sözleşmesidir | → `/arthurlegal:employment-legal-worker-classification` |

**ABD'deki "at-will" kavramı Türk hukukunda yoktur.** Türk teklifine "her an sebepsiz feshedilebilir" dili ekleme: bildirim süreleri asgaridir ve yalnız işçi lehine artırılabilir (m. 17), 30+ işçili işyerinde 6 aydan sonra iş güvencesi vardır (m. 18). Yerine bildirim süresi, deneme süresi ve fesih hükümlerinin kanuna uygunluğunu kontrol et.

### 3. Ücret ve çalışma süresi hükümleri

- Ücret brüt mü net mi açık; asgari ücretin altında değil (m. 39 — güncel tutarı teyit et).
- Haftalık süre ve dağılımı (m. 63); fazla çalışma için işçi onayı (m. 41).
- "Fazla çalışma ücrete dahildir" klozu: kapsamı ve sınırı **tartışmalı — içtihadı kontrol et** → `/arthurlegal:employment-legal-wage-hour-qa`.
- Prim/ikramiye: takdirî mi, kazanılmış hak mı açıkça yazılmalı; belirsizlik işçi lehine yorumlanma riski taşır (yerleşik uygulama — kontrol et).
- Yıllık izin süresi kanuni asgarinin altında olamaz (m. 53).

### 4. Rekabet yasağı, gizlilik, ceza koşulu

Teklif rekabet yasağı, müşteri/çalışan ayartmama, gizlilik ya da fikri hak devri içeriyorsa:

| Kontrol | Kural | Çıpa |
|---|---|---|
| Şekil ve ehliyet | Fiil ehliyetine sahip işçi, **yazılı** olarak üstlenir | TBK m. 444/1 |
| Geçerlilik şartı | İş ilişkisi müşteri çevresi ya da üretim sırları / işverenin işleri hakkında bilgi edinme imkânı veriyor **ve** bu bilginin kullanılması işverene önemli zarar verebilecek nitelikte | TBK m. 444/2 |
| Sınır | Yer, zaman ve iş türü bakımından işçinin ekonomik geleceğini hakkaniyete aykırı tehlikeye düşürmeyecek; süre özel durumlar dışında **2 yılı aşamaz**; hâkim aşırı yasağı sınırlayabilir, işverenin karşı edimini dikkate alır | TBK m. 445 |
| Aykırılığın sonucu | Zararın tazmini; ceza koşulu varsa işçi ödeyerek kurtulabilir (aksi kararlaştırılmadıkça); yasağa son verilmesi ancak yazılı olarak açıkça saklı tutulmuşsa | TBK m. 446 |
| Sona erme | İşverenin gerçek yararı kalmazsa; işveren haklı sebep olmaksızın feshederse ya da işçi işverene yüklenebilen nedenle feshederse | TBK m. 447 |
| Ceza koşulu | Hizmet sözleşmesine yalnız işçi aleyhine konan ceza koşulu geçersiz | TBK m. 420/1 |

TBK m. 420/1 ile m. 446/2 arasındaki ilişki (rekabet yasağına bağlanan tek taraflı ceza koşulunun geçerliliği) **tartışmalı — içtihadı kontrol et**. Profilin rekabet yasağı politikasını önce uygula (bu işe alıma yasak gerekiyor mu?), sonra kanuni sınırları. Çalışan buluşu ve fikri hak klozları için profilin "Çalışan buluşları ve fikri haklar klozları" bölümünü uygula; kloza yazılacak her madde ayrıca çekilir.

### 5. İşe alım süreci: ayrımcılık ve aday verisi

- **Eşit davranma (4857 m. 5):** dil, ırk, renk, cinsiyet, engellilik, siyasi düşünce, felsefi inanç, din, mezhep ve benzeri sebeplerle ayrım yasak; sözleşmenin yapılmasında cinsiyet ya da gebelik nedeniyle farklı işlem yasak (biyolojik/işin niteliği zorunlulukları hariç).
- **TİHEK (6701 m. 3, m. 6):** iş ilanı, başvuru, seçim kriterleri ve işe alım şartları dahil tüm süreçlerde ayrımcılık yasağı; başvuru gebelik, annelik ve çocuk bakımı gerekçesiyle reddedilemez (m. 6/3); yaş ve sağlık durumu da korunan temellerdendir (m. 3/2). İlan metnini bu gözle oku.
- **KVKK (6698):** aday verisi ilkelere uygun işlenir — amaçla bağlantılı, sınırlı, ölçülü, gerekli süre kadar saklanır (m. 4/2); hukuki sebep çoğunlukla sözleşmenin kurulmasıyla doğrudan ilgili işleme (m. 5/2-c) ya da açık rıza (m. 5/1); sağlık ve ceza mahkûmiyeti verisi özel niteliklidir (m. 6/1), ancak m. 6/3'teki hâllerde (ör. istihdam ve İSG alanındaki hukuki yükümlülük, m. 6/3-f) işlenir; veri elde edilirken aydınlatma (m. 10). Referans araması, sosyal medya taraması, sabıka kaydı talebi → hukuki sebep ve ölçülülük testi; gerekirse `/arthurlegal:privacy-legal-use-case-triage`.

### 6. İşe giriş zorunlulukları

| Zorunluluk | Kural | Çıpa |
|---|---|---|
| SGK işe giriş bildirgesi | Sigortalılık başlangıcından **önce** (inşaat, balıkçılık, tarımda en geç çalışmaya başlatıldığı gün) | 5510 m. 8/1 |
| Yabancı işçi | Çalışma izni olmadan çalışmak ve çalıştırmak yasak (kanun/anlaşma istisnaları saklı) | 6735 m. 6/2-3 |
| Engelli istihdamı | 50+ işçili özel sektör işyerinde %3 engelli işçi; aynı ildeki işyerleri toplanır | 4857 m. 30/1 |
| İSG eğitimi | İşe başlamadan önce; tehlikeli/çok tehlikeli işlerde mesleki eğitim belgesi olmayan çalıştırılamaz | 6331 m. 17/1, 17/3 |
| Kişisel veri | Çalışan aydınlatma metni | 6698 m. 10 |

Tutar içeren yükümlülükler (idari para cezaları, kota cezası) dönemsel güncellenir → güncel tutarı teyit et.

### 7. Teklif / sözleşme metni

- Başlama tarihi, unvan, görev tanımı, çalışma yeri, ücret (brüt/net), ödeme dönemi, çalışma süresi — yazılı belgede bulunması gereken unsurlarla karşılaştır (m. 8/3).
- Koşullar (sağlık raporu, referans, diploma, çalışma izni) açık ve KVKK'ya uygun.
- Bildirim süreleri kanuni asgarinin altında değil (m. 17); deneme süresi m. 15'e uygun.
- Personel yönetmeliğine atıf varsa → yönetmelik iş sözleşmesinin eki niteliğinde; sonraki aleyhe değişiklikler m. 22 rejimine tabidir (`/arthurlegal:employment-legal-handbook-updates`).
- Hak ve yükümlülükleri tek metinde toplayan bütünlük hükmü.

### 8. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["420","444","445","446","447"])
tr_mevzuat_madde_getir(number="4857", madde_no=["5","8","11","15","30"])
tr_mevzuat_madde_getir(number="6698", madde_no=["4","5","6","10"])
tr_kurum_karari_ara(kurum="kvkk", query="işe alım aday kişisel veri")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="rekabet yasağı cezai şart işçi aleyhine", date_from="2022-01-01")
```

Sonuç azsa sessizce doldurma; seçenekleri sun (sorguyu genişlet / başka araç / `[web — doğrula]` / dur). Atıf etiketleri: `[ArthurLegal TR — 6098 m. 444 — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`.

## Çıktı

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# İşe Alım İncelemesi: [Aday takma adı] — [Pozisyon] — [Yer]

## ⚠️ İnceleyen notu
- **Genel:** [Gönderilebilir / Değişiklik gerekli / Eskalasyon]
- **Uygulanacak hukuk:** [Türk hukuku / seçim + mutad işyeri — gerekçe]
- **Kaynaklar:** [çekilen maddeler; doğrulanamayan]
- **Tartışmalı noktalar:** [liste]

## Sözleşme türü ve şekli
## Ücret ve çalışma süresi
## Rekabet yasağı / gizlilik / ceza koşulu
[Geçerlilik değerlendirmesi, önerilen metin değişiklikleri]
## Ayrımcılık ve aday verisi
## İşe giriş zorunlulukları
## Metin sorunları

### Yapılacaklar
- [ ] [göndermeden önce somut değişiklik]
```

## Sonuç doğuran işlem kapısı (teklif gönderme)

"Gönderilebilir" önerisinden ya da imzaya hazır metinden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> Teklif bir sözleşmedir; rekabet yasağı, sözleşme türü ve zorunlu işlemler gönderildikten sonra kolay düzeltilmez. Bu teklifi bir avukatla incelediniz mi? Hayırsa götüreceğiniz özet: aday, pozisyon, işin yapılacağı yer; sözleşme türü ve gerekçesi; rekabet yasağı ve geçerlilik analizi; ayrımcılık/KVKK bulguları; işe giriş zorunlulukları; açık sorular; ters gidebilecek şey (geçersiz rekabet yasağı, belirsiz süreli sayılma, eksik SGK bildirimi, izinsiz yabancı çalıştırma); sorulacaklar. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan "Gönderilebilir" yazma; "TASLAK" işaretli inceleme serbest.

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; seçimi avukat yapar.

## Bu skill ne yapmaz

- Teklifi yazmaz; inceler.
- İşe alım kararını vermez.
- Rekabet yasağı ya da başka bir kuralı ezberden söylemez.
- Yeni bir ülkeyi derinlemesine kendisi araştırmaz; araştırma gerektiğini işaretler ve `wage-hour-qa` ya da yerel hukukçuya yönlendirir.

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
