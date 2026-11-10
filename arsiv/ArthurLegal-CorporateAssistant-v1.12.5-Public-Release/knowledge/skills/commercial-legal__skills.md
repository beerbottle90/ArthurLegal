# commercial-legal - Skill Referans Kitapcigi

> Değişiklik bildirimi (Apache-2.0 md. 4(b)): Bu kitapçık Anthropic'in `claude-for-legal` deposundaki aynı adlı eklentiden uyarlanmıştır. ArthurLegal tarafından Türk hukuku esas alınarak Türkçe yeniden yazılmıştır (2026-10); yabancı yargı çevreleri için yalnız ArthurLegal MCP araçlarına yönlendirir. Üst kaynak ve sürüm izi: ATTRIBUTION.md.

> Alan: Ticari sozlesmeler - NDA, MSA, SaaS, vendor
> Toplam skill: 13
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /commercial-legal:amendment-history (160 satir)
- /commercial-legal:cold-start-interview (274 satir)
- /commercial-legal:customize (50 satir)
- /commercial-legal:escalation-flagger (137 satir)
- /commercial-legal:governing-law-review (224 satir)
- /commercial-legal:matter-workspace (135 satir)
- /commercial-legal:nda-review (215 satir)
- /commercial-legal:renewal-tracker (183 satir)
- /commercial-legal:review (103 satir)
- /commercial-legal:review-proposals (29 satir)
- /commercial-legal:saas-msa-review (210 satir)
- /commercial-legal:stakeholder-summary (149 satir)
- /commercial-legal:vendor-agreement-review (268 satir)

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
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/legal-research:az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/legal-research:sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/legal-research:karsilastirmali-doktrin` |

Rehberler: `references/eqanun-mcp-rehberi.md` · `references/lex-scholar-rehberi.md` · `references/resourcecontracts-rehberi.md` · `references/karsilastirmali-hukuk-rehberi.md`

---

---

## /commercial-legal:amendment-history

---
name: amendment-history
description: >
  Bir sözleşmenin ana metni ve tüm değişiklikleri (ek protokol, tadil
  protokolü, zeyilname) boyunca nasıl değiştiğini izler — ya zaman içindeki
  tüm değişikliklerin özeti ya da belirli bir hükmün bugün geçerli metnine
  kadar izi. Değişikliğin şeklini (TBK m. 13, 17), taraf değişikliğini (TBK
  m. 205) ve yeniden düzenlenmiş metnin yenileme etkisini (TBK m. 133)
  işaretler. "Bu sözleşme zamanla nasıl değişti", "değişiklik geçmişini
  göster", "[hüküm]ün son hâli nerede", "[hüküm] nasıl evrildi" denince ya
  da bir sözleşmenin birden çok sürümü yüklendiğinde kullan.
argument-hint: "[dosya(lar) | [CLM ID (yakında)] | [depo bağlantısı (yakında)]] [--provision <hüküm adı>]"
---

# /amendment-history — Değişiklik Geçmişi

Ana sözleşmeyi ve tüm değişikliklerini yükler; ya zaman içindeki değişiklikleri özetler ya da belirli bir hükmü bugün geçerli metnine kadar izler. Üçüncü değişiklikten sonra kimse ana metnin ne dediğini ya da hangi sürümün geçerli olduğunu hatırlamaz; bu skill belgeleri kronolojik okur.

## Adımlar

1. **Belgeleri al:** yükleme, [CLM ID (yakında)] ya da [depo bağlantısı (yakında)]. Tek çağrıda birden çok dosya kabul et. Yoksa iste.
2. **Modu belirle** (aşağıdaki kurallar). Hüküm adı açıkça söylendiyse doğrudan Mod 2; söylenmediyse Mod 1. Yalnız gerçekten belirsizse sor.
3. **Akışı eksiksiz uygula.**
4. **Takip öner:** "Başka bir hükmü izleyeyim mi?" · "Değişikliklerle birlikte bugünkü sözleşmenin tam playbook incelemesi?" (→ vendor-agreement-review) · "Önemli değişikliklerin iş birimi özeti?" (→ stakeholder-summary)

```
/commercial-legal:amendment-history ana-sozlesme.pdf ek-protokol-1.pdf ek-protokol-2.pdf
/commercial-legal:amendment-history --provision tazmin
```

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/commercial-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Mod tespiti

**Mod 1 — Özet** (belirli hüküm yok): "ne değişti", "değişiklik geçmişi", "zaman içindeki değişiklikler", "değişiklikleri özetle", "sözleşmenin bugünkü hâli".

**Mod 2 — Hüküm izi** (belirli hüküm/konu): "[hüküm] nerede", "son [hüküm]", "[şart] nasıl değişti", "tazmini bul", "[konu] hakkında şimdi ne diyor".

Eşlemeler: "tazmin" → tazmin maddesi · "sorumluluk", "tavan" → sorumluluğun sınırlandırılması · "fesih", "süre" → süre ve sona erme · "veri", "KVKK", "kişisel veri eki" → veri koruma hükümleri · "fikrî hak", "lisans" → fikrî haklar · "fiyat", "bedel", "ödeme" → ödeme şartları · "yenileme" → yenileme düzeni · "cezai şart" → ceza koşulu · "yetki", "tahkim" → uyuşmazlık çözümü.

Terim birden çok hükme denk geliyorsa: "[terim] ile ilgili [N] hüküm buldum — [liste]. Hangisi?" Mod belirsizse tek soru: "Sözleşmedeki tüm değişikliklerin özeti mi, yoksa tazmin, sorumluluk ya da fesih gibi belirli bir hükmün izi mi?"

## Adım 1: Belgeleri yükle ve sırala

- **[CLM] (yakında):** karşı taraf ya da sözleşme adıyla ara; imza tarihleri meta veride.
- **[Belge deposu] (yakında):** "Ek Protokol", "Tadil Protokolü", "Zeyilname", "Değişiklik Sözleşmesi", "Ek-1", "Amendment No. 1", "Addendum" gibi adları ara; dosya tarihi ya da numarayla sırala.
- **Doğrudan yükleme:** sıra genelde başlıktan ("1 No.lu Ek Protokol", "İkinci Tadil Protokolü") ya da tarihten bellidir — sormadan devam et.

Yalnız şu hâllerde sırayı teyit ettir: dosya adları sıra vermiyor ("sozlesme-son.pdf", "sozlesme-v2.pdf"); dosya adında ve başlıkta tarih yok; iki belge aynı değişikliğin sürümleri gibi görünüyor. Sıra çıkarımsa yalnız emin olmadığın yerde not düş: "Sıra başlıklardan çıkarıldı — emin olmadığım belge: [belge]. İncelemenizi etkiliyorsa teyit edin."

Sıralama kuralları: içeriği okumadan önce kronolojiyi kur; meta verideki imza tarihi → başlık ya da girişteki tarih ("işbu Ek Protokol [tarih] tarihinde…") → atıf zinciri ("[tarih] tarihli Hizmet Sözleşmesi'nde değişiklik yapan…").

## Gizlilik

Ana sözleşme ve değişiklikler çoğu zaman gizlidir; çıktı kaynağın statüsünü devralır. Her çıktının başına eklenti ayarı `## Outputs` → üst başlığı koy, yalnız dar çevrede dağıt; dışa gidecek teslimde başlığı çıkar.

## Adım 2: Oku ve indeksle

Her belgeyi kronolojik oku ve çıkar: belge türü (ana sözleşme, kaçıncı değişiklik, ek), imza tarihi, taraflar, açıkça değiştirilen / eklenen / silinen hükümler. Çalışma indeksini çıktıyı yönetmek için kullan; kullanıcıya gösterme.

Okurken şu Türk hukuku işaretlerini topla (yorumlama; **izleme maddesi** olarak yaz):

- **Değişikliğin şekli.** Kanunda yazılı şekle bağlı bir sözleşmenin değiştirilmesi de yazılı olmalıdır; sözleşme metniyle çelişmeyen tamamlayıcı yan hükümler hariç (TBK m. 13). Taraflar kanunda şekle bağlı olmayan sözleşme için belirli bir şekil (ör. "değişiklikler yalnız iki tarafça imzalı yazılı ek protokolle yapılır") kararlaştırdıysa, o şekle uyulmadan yapılan değişiklik tarafları bağlamaz (TBK m. 17/1). E-postayla, sipariş formuyla ya da tek tarafın imzasıyla yapılmış "değişiklik" → işaretle.
- **İmza.** Değişiklik ana sözleşmedeki imza düzeniyle (yetkili temsilci, ıslak imza ya da güvenli e-imza — 5070 m. 5) imzalanmış mı?
- **Taraf değişikliği.** Bir değişiklikte taraf adı farklıysa: yalnız unvan değişikliği mi, sözleşmenin devri mi (devralan, devreden ve kalan tarafın anlaşması ya da kalan tarafın önceden izni/sonradan onayı; devredilen sözleşmenin şekline tabi — TBK m. 205), yoksa birleşme/bölünme gibi kanundan doğan halefiyet mi (m. 205/4; TTK'daki hükmü çek: `tr_mevzuat_icinde_ara(number="6102", query="külli halefiyet")`)? Resmî devir belgesi yoksa işaretle.
- **"Tadil edilmiş ve yeniden düzenlenmiş" metin.** Yeni bir borçla mevcut borcun sona erdirilmesi (yenileme) ancak tarafların açık iradesiyle olur (TBK m. 133/1). Yeniden düzenlenmiş metnin ana sözleşmenin yerine mi geçtiği yoksa onu mu değiştirdiği, bağlı teminatlara (kefalet, garanti, rehin) etkisi → **izleme maddesi; değerlendirme avukatın**.
- **Bedeli artıran değişiklik** damga vergisi doğurabilir → oran ve tutar yazma; `/tax-legal` skill'leri.
- **Bölüm numarası kayması:** aynı hüküm farklı numaraya taşınmış mı?

## Mod 1: Tüm değişikliklerin özeti

**Bölüm atfı kuralı:** Her bulguda satır içi madde atfı olsun ki okuyan kaynakta aramadan doğrulayabilsin: "İsteğe bağlı fesih (m. 12.3): Eklendi. İlk süreden sonra Müşteri 90 gün önceden yazılı bildirimle, bedelsiz feshedebilir." Numara değiştiyse hepsini yaz: "Tazmin (ana sözleşme m. 9.1; 5 No.lu Ek Protokol ile yeniden düzenlenen m. 9.1)."

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Değişiklik Geçmişi: [Karşı taraf] — [Sözleşme türü]

**Ana sözleşme:** [tarih]
**Değişiklikler:** [N] ([ilk tarih] → [son tarih])
**Son değişiklik:** [tarih]

## Ne değişti — kronolojik

### 1 No.lu Ek Protokol — [tarih]
**Amaç:** [tek cümle — girişte ya da bağlamdan açıksa; değilse yazma, tahmin etme]
**Önemli değişiklikler:**
- [Hüküm] (m. [X.X]): [eskiden ne diyordu → şimdi ne diyor, sade dille]
- [Eklenen hüküm] (m. [X.X]): [ne yapıyor]
- [Silinen hüküm] (m. [X.X]): [ne kaldırıldı ve neden önemli]

[her değişiklik için tekrarla]

## Bugünkü durum

| Hüküm | Güncel pozisyon | Madde | Son değişiklik |
|---|---|---|---|
| [kloz] | [sade özet] | m. [X.X] | [N] No.lu Ek Protokol, [tarih] |
| [kloz] | [ana sözleşmeden değişmedi] | m. [X.X] | Ana sözleşme |

## İzleme maddeleri
[Tutarsız görünen her şey, madde atfıyla: zaten silinmiş hükmü değiştiren değişiklik; değişiklikler arasında çelişen ifade; resmî devir olmadan değişen taraf adı; kararlaştırılan şekle (TBK m. 17) uymayan değişiklik; yeniden düzenlenmiş metnin yenileme sorusu (TBK m. 133); belgeler arasında kayan madde numarası.]
```

## Mod 2: Hüküm izi

Yalnız değişeni göster; hükme dokunmayan değişiklikleri tamamen atla.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Hüküm İzi: [Hüküm adı]
## [Karşı taraf] — [Sözleşme türü]

### Ana metin — [Ana sözleşme tarihi], m. [X.X]
> "[birebir alıntı]"
*Sade dille:* [tek cümle]

### [N] No.lu Ek Protokol — [tarih], m. [X.X]
**Eski:**
> "[önceki metnin birebir alıntısı]"
**Yeni:**
> "[yeni metnin birebir alıntısı]"
*Ne değişti:* [tek cümle — taraflar için pratik etkisi]

[Yalnız bu hükme dokunan sonraki değişiklikler.]

## Bugün geçerli metin
**m. [X.X] — [kaynak belge, tarih]**
> "[birebir alıntı]"
*Sade dille:* [tek cümle]

## İzleme maddeleri
[Madde atıflı bayraklar, tutarsızlıklar, açık sorular. Sık bakılanlar: hüküm sorumluluk tavanına tabi mi, tavan dışında mı; madde numarası kaydı mı; değişiklik ifadesi başka bir hükümle çelişiyor mu; değişiklik kararlaştırılan şekle uygun mu.]
```

Hüküm ana sözleşmeden sonra hiç değişmediyse: "Bu hüküm hiçbir değişiklikle değiştirilmemiştir. Ana metin geçerlidir. m. [X.X], ana sözleşme, [tarih]."

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["13","17","19","23","133","205"])
tr_mevzuat_madde_getir(number="5070", madde_no="5")
tr_mevzuat_icinde_ara(number="6102", query="külli halefiyet")
```

Atıf etiketi: `[ArthurLegal TR — 6098 m. X — GG.AA.YYYY]`. Çekilemeyen madde: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu çıktıya göre uyarla (yeni değişiklik taslağı, eskalasyon, eksik belge iste, bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Ana sözleşme ile değişiklik çeliştiğinde hangisinin geçerli olduğuna karar vermez — bu yorum sorusudur (tarafların gerçek ve ortak iradesi, TBK m. 19/1; matbu koşulda belirsizlik düzenleyen aleyhine, TBK m. 23). Çelişkiyi işaretler, hukuka yönlendirir.
- Yeni değişiklik yazmaz.
- Playbook'la karşılaştırmaz — o vendor-agreement-review'un işidir; bu skill yalnız tarihseldir.
- Belirsiz değişiklik ifadesine anlam yüklemez; birebir alıntılar ve belirsizliği hukuka işaretler.

---

## /commercial-legal:cold-start-interview

---
name: cold-start-interview
description: >
  İlk kurulum — ticari sözleşme pratiğinizi öğrenir ve ekip profilini yazar: pratik
  ortamı (büro / şirket içi), taraf (satış / satın alma), Türk hukukuna göre standart
  duruşlar (sorumluluğun sınırlandırılması TBK m. 115, cezai şart TBK m. 179, 180, 182 ve
  TTK m. 22, veri koruma, süre ve fesih, uygulanacak hukuk ve yetki/tahkim), eskalasyon
  matrisi ve imza yetkisi, örnek sözleşmelerden fiilî duruşlar. İlk kullanımda,
  `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` yoksa ya da
  yer tutucu içeriyorsa, "eklentiyi kur", "beni tanı", "başlayalım" denince kullan.
  Yeni kurulumda çalışacak tek skill budur.
argument-hint: "[--redo | --full | --check-integrations | --side sales|purchasing]"
---

# /cold-start-interview

1. **Durum:** `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` yoksa görüşmeye başla. `<!-- SETUP PAUSED AT: -->` varsa o bölümden devam öner. `[PLACEHOLDER]` ya da `[Your Company Name]` varsa (duraklatma notu yok) baştan ya da yer tutucuların başladığı yerden devam öner. Doluysa ve `--redo` / `--side` yoksa sor: "Kurulum yapılmış görünüyor. Yeniden yapalım mı? Üzerine yazmadan önce farkı gösteririm."
2. **Taşıma:** eski önbellek yolunda (`~/.claude/plugins/cache/claude-for-legal/commercial-legal/*/CLAUDE.md`) dolu bir CLAUDE.md varsa ve ayar yolunda yoksa ayar yoluna kopyala; neyin taşındığını göster.
3. Görüşmeyi yürüt (önce Bölüm 0); örnek belgelerden fiilî duruşları çıkar (Bölüm 4); profili aşağıdaki iskelete göre yaz (üst klasörleri gerekirse oluştur), avukatın kendi sözleriyle.
4. Özeti göster: "Duyduklarım bunlar — profil yazıldı. Neyi yanlış anladım?" Deneme incelemesi öner; CLM bağlıysa yenileme kaydını toplu yüklemeyi öner.

**`--check-integrations`:** görüşme yapma; yalnız bağlantı kontrolünü çalıştır ve `## Available integrations` tablosunu yeniden yaz. ✓ yalnız gerçek bir MCP çağrısı başarılı döndüyse; denenmemiş bağlantı ⚪. `.mcp.json` beyanına bakarak ✓ verme.

**`--side sales` / `--side purchasing`:** yalnız Bölüm 2'yi o tarafa göre yürüt, `### Sales-side playbook` ya da `### Purchasing-side playbook` alt bölümüne yaz; Bölüm 0, 1 ve 3'ü sorma, diğer tarafa dokunma; `**Active side:**` satırını güncelle (`sales`, `purchasing`, `both`).

**Bölüm ve anahtar adlarını çevirme.** `## Who we are`, `## Who's using this`, `## Available integrations`, `## Playbook`, `**Active side:**`, `### Sales-side playbook`, `### Purchasing-side playbook`, `#### Limitation of liability` vb., `## Escalation`, `## House style`, `## Outputs`, `## Review preferences` (`confirm_routing`), `## NDA triage preferences` (`closing_action`), `## Playbook monitor settings` (`pattern_threshold`, `lookback_months`), `## Matter workspaces` adları aynen kalır — inceleme skill'leri ve ajanlar bunları birebir okur. İçerik Türkçe yazılır.

## Ortak profil

`~/.claude/plugins/config/claude-for-legal/company-profile.md` varsa oku ve tek satırla teyit et ("Siz [ad], [pratik ortamı], [büro/şirket], [sektör], [ülkeler]. Doğru mu?"); teyitte ortak soruları (pratik ortamı, ad, sektör, ne sattığı, büyüklük, ülkeler, düzenleyiciler, risk iştahı, eskalasyon isimleri) atla. Yoksa ilk kurulan eklenti budur: ortak soruları sor, paketteki `knowledge/company-profile.md` şablonuna göre yaz ve söyle: "Profilinizi kaydettim — diğer eklentiler okuyup bu soruları atlayacak." Playbook, eskalasyon matrisi ve ev üslubu eklentiye özeldir.

**Kurulum kapsamı:** Çalışma klasörü ev dizini değil de bir proje klasörüyse bir kez söyle: "Eklenti proje kapsamında kurulmuş görünüyor; yalnız [klasör] içindeki dosyaları okuyabilirim. Başka klasörlerden sözleşme okumamı isterseniz kullanıcı kapsamında kurun (QUICKSTART.md)." Onay al. Ev dizinindeysen sessizce geç.

## Başlamadan önce

Kısa tut, önce hızlı/tam sor:

> **`commercial-legal`** ticari sözleşmeleri (tedarikçi/hizmet sözleşmeleri, SaaS abonelikleri, gizlilik sözleşmeleri, yenilemeler) inceleyen, müzakere eden ve yöneten ekipler içindir.
>
> **2 dakika:** rol, pratik ortamı, taraf (satış / satın alma) ve varsayılan duruşlar. **15 dakika:** gerçek playbook duruşlarınız (sorumluluk sınırı, tazmin, cezai şart, veri koruma, süre/fesih, uygulanacak hukuk ve yetki), vazgeçilmez tek şartınız, tutar eşikli eskalasyon matrisi ve imza yetkisi, ev üslubu, imzalı sözleşmelerden çıkarılan fiilî duruşlar.
>
> Hızlı mı, tam mı? (Sonra `/commercial-legal:cold-start-interview --full` ile genişletebilirsiniz.)

**Hızlı yol:** yalnız Bölüm 0 ve taraf sorusu; diğer her alana `[DEFAULT]` yaz. Kapanış: "Tamam, komutları kullanabilirsiniz. Playbook duruşları, eskalasyon eşikleri ve ev üslubunda makul varsayımlar kullandım. Bir çıktı yanlış gelirse genellikle ayarlanacak bir varsayımdır — çıktı hangisi olduğunu söyler. Tam görüşme için `--full`, tek bölüm için `--redo <bölüm>`."

**Seçimden sonra** tek paragraf oryantasyon: "Bu eklenti profilinizi (tarafınıza göre playbook, eskalasyon matrisi), fesih bildirimi son günlerini tutan yenileme kaydını, sapma günlüğünü ve playbook öneri kuyruğunu tutar. Cevaplarınızı her skill'in okuduğu düz bir metin dosyasına yazar; her şey sonradan değiştirilebilir." Ardından: "Kurulum yalnız sizin yazdıklarınızdan ve paylaştığınız belgelerden profil kurar; kişisel Claude geçmişinizi, başka sohbetleri ya da ev dizininizdeki CLAUDE.md'yi okumaz. Sohbette daha önce geçen bir bilgiyi kullanmadan önce sorarım."

## Görüşme temposu

- **Cevap bir yerde yazılıdır varsay.** Şirket tanıtımı, playbook, eskalasyon matrisi, imza sirküleri, yetki devri belgesi için önce bağlantı/yapıştırma iste: "Belge yapıştırın, bağlantı verin ya da kısa hâlini söyleyin."
- **Bir turda 2-3 cevaplanabilir soru** (alt sorular da sayılır); ekranı kaydırmadan cevaplanabilmeli.
- **Uzun cevapta bekle:** "Bu soru yazılı cevap istiyor — bekliyorum." Yüklemede: "Yapıştırın, dosya yolu verin ya da 'şimdilik geç' deyin; geçerseniz profilde boşluğu işaretlerim."
- **Yazmadan önce açıkları say:** "Profili yazmadan önce açık kalanlar: [liste — özellikle playbook duruşları, vazgeçilmez şart, örnek sözleşmeler]. Şimdi mi dolduralım, yer tutucu mu kalsın?" Sessiz boşluk bırakma.
- **Duraklat/devam:** "dur", "sonra devam" denirse kısmi profili `<!-- SETUP PAUSED AT: [bölüm] — devam için /commercial-legal:cold-start-interview -->` notuyla ve cevapsız alanlarda `[PENDING]` ile yaz. Dönüşte: "Hoş geldiniz, [bölüm]de kalmıştınız. Devam mı, baştan mı?" Cevaplanmış soruyu tekrar sorma.
- **Kullanıcının söylediği hukuki olguyu doğrula.** Madde, süre, eşik söylenirse `tr_mevzuat_madde_getir` ile çek ve karşılaştır; çelişirse: "[X] dediniz; madde metni [Y] diyor — profile hangisi girsin? `[premise flagged — verify]`" Örnek: "Cezai şart fahişse mahkeme indirir" — tacir sıfatındaki borçlu aşırı ceza iddiasıyla indirim isteyemez (TTK m. 22); bu ayrım profile doğru girmeli. Değişen tutarları (damga vergisi oranı ve azami tutarı, faiz oranları, parasal sınırlar) profile sabit yazma; "güncel tutarı teyit et — dönemsel güncellenir" notu düş.

## Bölüm 0 — Kim kullanıyor, ne bağlı

### Kim kullanıyor?

> Eklentiyi günlük kim kullanacak? (Her inceleme, değişiklik geçmişi ve yenileme çıktısındaki üst başlığı belirler.)
> 1. **Avukat ya da avukat gözetiminde çalışan** (stajyer avukat, sözleşme yöneticisi, hukuk operasyonu)
> 2. **Avukata erişimi olan, avukat olmayan** (kurucu, satın alma, satış operasyonu, finans)
> 3. **Düzenli avukat erişimi olmayan**

2 ya da 3 ise bir kez söyle: "Tüm özellikleri kullanabilirsiniz; iki şey değişir: (1) çıktıları 'imzalayın' hükmü değil, avukatla konuşmanız için araştırma olarak çerçevelerim; (2) hukuki sonucu olan adımlardan önce (imza, karşı tarafa redline gönderme, yenilemeyi kabul ya da fesih bildirimi) avukatla görüşüp görüşmediğinizi sorar, görüşmeyi hızlandıracak kısa bir brif hazırlarım." 3 ise ekle: "Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz; barolar adli yardım hizmeti de yürütür, koşullarını baroya sorun."

### Pratik ortamı

> Hangisi size uyuyor? (Eskalasyon matrisinin dilini belirler.)
> - **Hukuk bürosu (müvekkil adına sözleşme hazırlama/inceleme)** — onay zinciri değil danışma tetikleri sorarım.
> - **Kurum içi hukuk** — eskalasyon matrisi, hukuk müşaviri/genel müdür, ne zaman iş birimine gider.
> - **Tek avukat / küçük büro** — üst kademe yerine "meslektaşa/dış avukata ne zaman danışırsınız".
> - **Kamu / klinik** — denetim modeli ve imza zinciri.
> - **Hiçbiri** — kendi anlatımınızla yazın; kutuya zorlamam, doldurulan, uyarlanan ve boş bırakılan alanları işaretlerim.

Dallanma ve kayıt (`## Who we are` altında `**Practice setting:**` satırı):
- **Büro (her tür):** `## Matter workspaces` → `Enabled: ✓`, `Cross-matter context: off`. `## Escalation` tablosu onay seviyeleri değil danışma tetikleri gösterir. Profile `## Çıkar çatışması` notu yaz: aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermiş avukat ve kendi düzenlediği sözleşmenin hükümsüzlüğünü ileri sürmek durumunda kalan avukat işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Her yeni matter'da kontrolün yapıldığını sor.
- **Kurum içi:** `Enabled: ✗` (tek müvekkil; matter katmanı görünmez).
- **Kamu / klinik:** işi kim gözden geçirir, imza zinciri.

### Ne bağlı?

Yapılandırılmış ile **çalışan** bağlantıyı karıştırma.
- **ArthurLegal MCP (`tr_`)** — dene: `tr_mevzuat_madde_getir(number="6098", madde_no="115")`. Cevap geldiyse ✓.
- **Sözleşme emsali (`contracts_`)** — kloz kıyası için isteğe bağlı: `contracts_search_contracts`.
- **Yabancı ülke araçları** (`eu_`, `uk_`, `de_` …) — yalnız yabancı hukuka tabi sözleşme varsa; önce `status`.
- **CLM (Ironclad vb.), e-imza (DocuSign vb.), belge deposu (Drive, SharePoint, Box), Slack** — deneyebiliyorsan dene; deneyemiyorsan ⚪. KEP için MCP yoktur; KEP adresi varsa `## House style`'a not et.

Raporla: ✓ bağlı (denendi) · ⚪ yapılandırılmış, doğrulanmadı — MCP ayarlarından teyit edin · ✗ yok — [özellik] [manuel yönteme] düşer, nasıl bağlanır, sonra `--check-integrations`. "Hepsine gerek yok; çekirdek özellikler dosya erişimiyle çalışır." ArthurLegal MCP ✗ ise: "Her madde ve karar atfı 'doğrulanmadı' işaretlenir ve UYARI satırı taşır."

**Hemen yaz:** `## Who's using this` ve `## Available integrations` bölümlerini `## Who we are`'dan hemen sonra yaz; `## Outputs` üst başlığını role göre kur.

## Bölüm 1 — Ekip ve iş akışı (2-3 dk)

- **Ne iş yapıyorsunuz?** Ne satıyorsunuz, kime, nasıl (doğrudan, bayi/distribütör, pazaryeri, abonelik)? Web sitesi bağlantısı yeter. Büroysanız: müvekkil profiliniz ve en sık sözleşme tipleri.
- **Kim?** Şirket türü (AŞ, Ltd., şube, yabancı şirket), sözleşme ekibinin büyüklüğü, son sözü kim söylüyor (hukuk müşaviri, genel müdür, yönetici ortak)?
- **Ne geliyor?** Aylık hacim; karışım (tedarik, hizmet, SaaS, lisans, distribütörlük/acentelik, gizlilik); kendi metniniz mi karşı tarafın mı; hafif redline mı çok turlu müzakere mi; ortalama süre.
- **Ne acıtıyor?** Masaya gelince "of" dedirten ne; darboğaz inceleme mi, müzakere turu mu, onay kovalamak mı?

**Taraf sorusu** (doğrudan sor):

> Playbook duruşlarını hangi tarafa göre kurayım? (Her inceleme yalnız eşleşen tarafın playbook'unu uygular; satış duruşu satın alma sözleşmesine uygulanmaz.)
> - **Satış tarafı (sales-side)** — ürün/hizmet satıyoruz; genelde bizim metnimiz.
> - **Satın alma tarafı (purchasing-side)** — tedarikçiden alıyoruz; genelde onların metni.
> - **İkisi.**

- **Tek taraf:** `**Active side:** sales` ya da `purchasing`; Bölüm 2 cevapları eşleşen alt bölüme; diğerinde `*[Not configured — run /commercial-legal:cold-start-interview --side <side> to build it]*` kalır.
- **İkisi:** önce satış tarafını kur (genelde kendi metniniz, yüzeyi küçük); sonunda `--side purchasing` öner. İkisi de dolunca `**Active side:** both`.

Soruları tarafın sesiyle sor: satışta "hangi tavanı **sunuyoruz**", satın almada "tedarikçiden hangi tavanı **kabul ediyoruz**". Karıştırma.

## Bölüm 2 — Playbook (3-4 dk)

> "Playbook'unuzu şimdi kuralım mı? İnceleme skill'leri genel varsayım yerine sizin duruş ve geri çekilme noktalarınızı bilir. 3-4 dakika. Geçerseniz varsayılan kullanılır ve kurulmamış bir duruşa gelindiğinde söylenir."

Önce sor: "Müzakere playbook'u, sözleşme standartları belgesi ya da geri çekilme notu var mı? Ekip/departman düzeyindeki ortak belge varsa onu isterim; kişisel farklarınızı ayrıca sorarım." Varsa oku, her kategori için duruşu çıkar, yalnız boşlukları sor; iki tarafı kapsıyorsa yazarken ikiye böl.

Yoksa her kategori için **standart duruş / kabul edilebilir geri çekilme / asla kabul edilmeyen** sor:

**Sorumluluğun sınırlandırılması** (`#### Limitation of liability`)
- Tavan: son 12 ay bedeli mi, sabit tutar mı (para birimi)? Dolaylı zarar ve kâr kaybı hariç mi?
- İstisnalar (tavan dışı): gizlilik ihlali, fikri mülkiyet ihlali, kişisel veri ihlali, kast ve ağır kusur.
- Hukuki sınır: borçlunun ağır kusurundan sorumlu olmayacağına ilişkin önceden yapılan anlaşma kesin hükümsüzdür; uzmanlık gerektiren ve izinle yürütülen hizmette hafif kusur için de öyledir (TBK m. 115/1, 115/3). Tavanın ağır kusur ve kastı da sınırlaması bu yüzden geçersizlik riski taşır; profile "tavan kast/ağır kusuru kapsamaz" notunu yaz.
- Karşı tarafın standart metninde (genel işlem koşulu) aleyhe kloz: açıkça bilgi verilip kabul edilmedikçe yazılmamış sayılır (TBK m. 21); dürüstlük kuralına aykırı aleyhe hüküm konulamaz (m. 25). "Her madde tartışıldı" kaydı tek başına GİK niteliğini kaldırmaz (m. 20/3).

**Tazmin (indemnity)** (`#### Indemnification`)
- Karşılıklı mı, tedarikçiden tek yönlü mü? Fikri mülkiyet ihlali tazmini zorunlu mu? Hiç kabul edilmeyen tazmin?
- Türk hukukunda "indemnity" kendi başına bir kurum değildir; üçüncü kişinin fiilini üstlenme (TBK m. 128) ya da sözleşmesel tazmin taahhüdü olarak yazılır — kapsam, bildirim ve savunmayı yönetme usulü açık olmalı.

**Cezai şart** (`#### Penalty clause`)
- Kabul ediliyor mu, hangi hâllerde, üst sınır? Seçimlik mi (borç ya da ceza), ifa ile birlikte mi (TBK m. 179)?
- Zarar olmasa da istenir; aşan zarar için kusur ispatı gerekir (m. 180). Hâkim aşırı cezayı kendiliğinden indirir (m. 182/3) — ama tacir sıfatındaki borçlu aşırılık iddiasıyla indirim isteyemez (TTK m. 22). Borçlu olduğumuz cezada (ör. satışta gecikme cezası, satın almada erken fesih cezası) yüksek tutarı kabul etmek bu yüzden "asla" ya da eskalasyon konusu olabilir.

**Veri koruma** (`#### Data protection`)
- Standart veri işleme sözleşmeniz var mı, karşı tarafınkini mi alırsınız? Veri sorumlusu, işleyenin alması gereken teknik ve idari tedbirlerden onunla müştereken sorumludur (KVKK m. 12/2) — işleyen sözleşmesi bu yüzden şart mı?
- Yurt dışı aktarım: yeterlilik kararı yoksa uygun güvence (standart sözleşme vb.) gerekir; standart sözleşme imzadan itibaren beş iş günü içinde Kurum'a bildirilir (KVKK m. 9/4-5). Bulut/SaaS tedarikçisinde kim bildirir?
- Güvenlik belgesi (ISO 27001, SOC 2) tüm tedarikçilerden mi, yalnız veri işleyenlerden mi? Alt işleyende onay mı, bildirim mi?

**Süre ve fesih** (`#### Term and termination`)
- Haklı sebeple ve olağan (sebepsiz) fesih: bildirim süresi? Otomatik yenilemede kabul edilen en uzun fesih bildirim penceresi? Fesih bedeli hiç kabul edilir mi?
- Fesih bildiriminin şekli: tacirler arasında fesih ve temerrüt ihbarları noter, taahhütlü mektup, telgraf ya da güvenli elektronik imzalı KEP ile yapılır (TTK m. 18/3). Sözleşme "e-posta yeterli" diyorsa duruşunuz ne?
- Tüketiciye satıyorsanız (B2C abonelik): belirli süreli abonelikte sözleşmenin kendiliğinden uzayacağına dair hüküm konulamaz (6502 s. TKHK m. 52/3) → satış tarafı playbook'una ayrı not.

**Uygulanacak hukuk ve uyuşmazlık çözümü** (`#### Governing law and venue` — `**Preferred:**`, `**Acceptable:**`, `**Escalate:**`, `**Never:**`)
- Sözleşmeden doğan borç ilişkileri tarafların açıkça seçtiği hukuka tabidir (MÖHUK m. 24/1); yabancılık unsuru olmayan saf iç sözleşmede yabancı hukuk seçimi **tartışmalı — içtihadı kontrol et**. Tercih / kabul / eskalasyon / asla listesi; yabancı hukuk ve yabancı yer tahkimi için ayrıntılı analiz `/commercial-legal:governing-law-review`'dadır.
- Yetki sözleşmesi yalnız tacirler veya kamu tüzel kişileri arasında yapılabilir (HMK m. 17) ve yazılı olmalı, hukuki ilişki belirli ya da belirlenebilir, mahkeme gösterilmiş olmalıdır (m. 18/2). Tahkim sözleşmesi yazılıdır (HMK m. 412/3). Tercih: İstanbul mahkemeleri mi, kurumsal tahkim mi?
- Para alacağı, tazminat, itirazın iptali, menfi tespit ve istirdat konulu ticari davalarda dava öncesi arabuluculuk dava şartıdır (TTK m. 5/A) — kademeli uyuşmazlık klozu (müzakere → arabuluculuk → mahkeme/tahkim) istiyor musunuz?

**Damga vergisi** (`#### Stamp duty`) — kim öder, nüsha sayısı, imza yeri; oran ve azami tutar dönemsel güncellenir, profile sayı yazma (488 s. Damga Vergisi Kanunu — güncel tutarı teyit et).

**YZ/ML eğitim hakları** (`## AI/ML training rights` — yedi boyut, her biri ayrı yazılır; "her şeye hayır" geçerli ama yedi ayrı "hayır" olarak):
1. Açık eğitim izni — kesin hayır / dar tanımlıysa kabul / önemsiz?
2. Gizlilik politikasına atıfla örtülü izin — politika tek taraflı değişebiliyorsa red / kabul?
3. Anonimleştirme standardı — KVKK tanımı (başka verilerle eşleştirilerek dahi kişiyle ilişkilendirilemeyecek hâle getirme, m. 3/1-b) ya da adı konmuş bir standart şart mı; tanımsız "anonim" yeterli mi? AB verisi varsa: `eu_search_eu_law(query="Regulation (EU) 2016/679 recital 26 anonymous information")`.
4. Rakip kirlenmesi — tedarikçi rakiplerinize de hizmet veriyorsa yalıtım taahhüdü?
5. Opt-out kapsamı ve kalıcılığı — tüm YZ kullanımlarını kapsayan, yenileme ve şart güncellemesinden sonra da süren opt-out?
6. Çıktıların sahipliği — müşteride mi; tedarikçinin çıktıları eğitim örneği olarak tutması?
7. Düzenleyici zincir — AB YZ Tüzüğü (`eu_search_eu_law(query="Regulation (EU) 2024/1689 artificial intelligence")`) ve Türkiye'de yürürlükteki düzenleme (`tr_mevzuat_ara(query="yapay zeka", search_in="fulltext")`) bakımından tedarikçiden bildirim istenir mi?

**Vazgeçilmez tek şart** (`#### The one thing`): "Bir sözleşmede tek bir sorun olsa ve sırf o yüzden imzalamasanız, o ne?"

Playbook belgesi yüklenmediyse sonunda öner: "Bunu ekibinizle paylaşabileceğiniz ayrı bir playbook belgesi olarak da yazayım mı?"

## Bölüm 3 — Eskalasyon ve imza yetkisi (1-2 dk)

Önce sor: "Eskalasyon matrisi, onay eşikleri belgesi ya da yetki devri/iç yönerge var mı? Yapıştırın; temel alırım." Varsa doğrudan çıkar, belirsizi teyit et.

Yoksa:
- **Onay seviyeleri:** "İnceleme playbook dışı bir şey bulduğunda (daha yüksek tavan, geri çekilme dışı tazmin) ya da yetkinizi aşan bir karar gerektiğinde kime gider? İsim ya da rol, ya da 'kendim karar veririm'." (Bunu `/commercial-legal:escalation-flagger` kullanır.)
- **Tutar eşikleri:** sözleşme bedeline göre kim onaylar (para birimiyle)?
- **Tutardan bağımsız otomatik eskalasyon:** tipik — sınırsız sorumluluk, fikri mülkiyetin karşı tarafa devri, tacir olarak yüksek cezai şart, yabancı hukuk + yabancı yer tahkimi, yurt dışına kişisel veri aktarımı, playbook'taki "asla" listesi.
- **İmza yetkisi:** Sözleşmeyi kim imzalar? AŞ'de esas sözleşmede aksi yoksa temsil yetkisi çift imza ile yönetim kuruluna aittir (TTK m. 370/1); temsile yetkililer ve temsil şekli ticaret siciline tescil ve ilan edilir (m. 373/1). İç onay matrisi şirketin iç düzenidir (yönetimin devri esas sözleşme hükmüyle ve iç yönergeyle yapılır, m. 367); iç sınırlamalar iyiniyetli üçüncü kişilere karşı hüküm ifade etmez — yalnız tescil ve ilan edilen merkez/şube ya da birlikte kullanma sınırlamaları geçerlidir (m. 371/3). Ltd.'de bu hükümler kıyasen uygulanır (m. 629/1). İmza sirkülerinin güncel olup olmadığını ve kimin tuttuğunu not et.
- **Kanal ve süre:** Bugün nasıl eskale ediliyor (Slack, e-posta, toplantı)? Beklenen dönüş süresi?
- **İnceleme tercihi:** İncelemeye başlarken yönlendirmeyi (hangi skill, hangi ek hangi skill'e) önce teyit edeyim mi? `confirm_routing` varsayılanı açık.
- **NDA kapanış eylemi:** NDA triyajı bitince ne yapılsın (ekip kutusuna e-posta, CLM iş akışı, sözleşme yöneticisine iletme)? Her NDA çıktısına standart talimat olarak eklerim.

Matris yüklenmediyse sonunda öner: "Bunu paylaşılabilir ayrı bir eskalasyon matrisi olarak da yazayım mı?"

## Bölüm 4 — Örnek belgeler

Önce altyapı sorusu: "İmzalı sözleşmeleriniz fiilen nerede duruyor — CLM, ortak Drive/SharePoint klasörü, fiziksel arşiv taraması? Haftalık deal-debrief ve renewal-watcher ajanları burayı tarar." CLM ise sistem adını ve "imzalandı" durumunun adını; klasörse tam yolu; dağınıksa "manuel yükleme" yaz.

> Önce: en sık kullandığınız sözleşme tipleri için kendi şablonlarınız (başlangıç duruşu). Sonra: 5-10 yakın tarihli imzalı sözleşme — 20 daha net desen verir; azsa olanı paylaşın.

Okuma sırası: (1) şablonlardan başlangıç duruşları; (2) imzalılardan fiilî şartlar; (3) fark — gerçek playbook budur; (4) sözleşme tipi ve karşı taraf büyüklüğüne göre desen (kurumsal karşı tarafta farklı geri çekilme vb.). 5'ten az imzalı sözleşmeyle kurulan her bölüme `[LIMITED DATA — N sözleşme incelendi]` yaz.

## Profili yazma

Yazmadan önce paylaşılan belgeleri yeniden oku; hafızaya güvenme. Profil avukatın okuyup düzenleyeceği bir belgedir, YAML değil. İskelet (başlıklar aynen, içerik Türkçe):

```markdown
# Commercial Contracts Practice Profile
*[TARİH] tarihinde kurulum görüşmesiyle yazıldı. Doğrudan düzenleyin — eklentideki her skill önce bunu okur.*
## Who we are
[ŞİRKET ADI] — [şirket türü]. **Practice setting:** [büro / kurum içi / tek avukat / kamu / diğer]
Ekip: [N kişi, roller]. Son karar: [isim/rol]. Aylık ~[N] sözleşme, ağırlıkla [tip]. CLM: [ad / yok].
**Acıtan şey:** [kendi sözleriyle]
## Who's using this
**Role:** [Avukat / Avukata erişimi olan avukat olmayan / Avukat erişimi olmayan]
**Attorney contact:** [isim / ekip / dış büro / —]
## Available integrations
| Integration | Status | Fallback if unavailable |
|---|---|---|
| ArthurLegal MCP (`tr_`) | [✓/⚪/✗] | Atıflar "doğrulanmadı" + UYARI satırı |
| CLM | [✓/⚪/✗] | Yerel yenileme kaydı ve manuel kayıt |
| E-imza | [✓/⚪/✗] | İmza eklenti dışında yürür |
| Belge deposu (Drive / SharePoint / Box) | [✓/⚪/✗] | Her incelemede dosya yüklenir |
| Slack | [✓/⚪/✗] | Uyarılar sohbette verilir |
## Playbook
**Active side:** [sales / purchasing / both]
> İnceleme skill'leri önce sözleşmede hangi tarafta olduğumuzu belirler (genelde kimin metni olduğundan anlaşılır; değilse sorar) ve yalnız eşleşen bölümü uygular.
### Sales-side playbook
#### Limitation of liability
**Standard position:** … **Acceptable fallbacks:** … **Never accept:** … **Carveouts we accept:** …
> *Örnek belgelerden:* [beyan ile imzalanan farkı — ör. "Standart 12 ay; incelenen 5 sözleşmenin 3'ü 24 ayda kapandı → 24 ay geri çekilme sayıldı."]
#### Indemnification
#### Penalty clause
#### Data protection
#### Term and termination
#### Governing law and venue
**Preferred:** … **Acceptable:** … **Escalate:** … **Never:** …
#### Stamp duty
#### The one thing
### Purchasing-side playbook
*[Not configured — run /commercial-legal:cold-start-interview --side purchasing to build it]*
[Aynı alt bölümler; tedarikçiden kabul ettiklerimize göre]
## AI/ML training rights
[Yedi boyut, her biri ayrı duruş]
## Escalation
| Can approve | Without escalation | Escalate to | Via |
|---|---|---|---|
**Dollar thresholds:** [tutar ve para birimi]
**Automatic escalations regardless of dollar value:** [liste]
**Signing authority:** [kim imzalar, tek/çift imza, imza sirküleri tarihi, iç yönerge var mı]
## Çıkar çatışması
[Yalnız büroda — Av. K. m. 38 notu ve çatışma kontrolü pratiği]
## House style
**Tone in redlines:** … **Stakeholder summaries:** … **Where work product goes:** …
**Where signed contracts live:** [CLM + imzalı süzgeci / klasör yolu / manuel yükleme]
**Renewal alerts:** [kanal ya da e-posta listesi] · **KEP address:** [varsa]
## Outputs
- Rol avukatsa: `GİZLİDİR — AVUKATLIK K. m. 36 KAPSAMINDA — DAHİLİ`
- Rol avukat değilse: `ARAŞTIRMA NOTU — HUKUKİ GÖRÜŞ DEĞİLDİR — İŞLEM ÖNCESİ AVUKATLA GÖZDEN GEÇİRİN`
Karşı tarafa giden redline ve hukuk dışına iletilen özetlerden başlık çıkarılır. Başlık tek başına koruma yaratmaz.
## Seed documents reviewed
| Agreement | Counterparty | Date signed | Notable terms |
## Review preferences
confirm_routing: true
## NDA triage preferences
closing_action: "[her NDA triyajına eklenecek talimat]"
## Playbook monitor settings
pattern_threshold: 5
lookback_months: 12
## Matter workspaces
Enabled: [✓ / ✗]
Active matter: none — practice-level context only
Cross-matter context: off
```

## Yazdıktan sonra

> **Neler yapabildiğimi görmek ister misiniz?** Tedarikçi sözleşmesini playbook'a göre inceleme ve NDA triyajı (`/commercial-legal:review`), fesih bildirimi son günleri (`/commercial-legal:renewal-tracker`), bir klozun değişiklikler boyunca izi (`/commercial-legal:amendment-history`), yetkiyi aşan sapmayı eskale etme (`/commercial-legal:escalation-flagger`), bekleyen playbook önerileri (`/commercial-legal:review-proposals`). **Önerim:** bekleyen bir NDA'yı triyaj edelim — playbook'un nasıl okunduğunu iki dakikada gösterir.

Kullanıcı somut bir iş söylediyse listeyi atla. Uygunsa ekle: "Yenilemeler gözden kaçıyor dediniz — CLM'de 90 gün içinde bitenleri tarayayım mı?" · "ArthurLegal MCP bağlı değil — bağlarsanız madde atıflarını canlı doğrularım."

**Kapanış:**
> "Tamam. Profiliniz `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` dosyasında — düz metin, doğrudan düzenleyebilirsiniz. Tam yeniden görüşme `--redo`, bağlantı kontrolü `--check-integrations`, tek değişiklik `/commercial-legal:customize`. En sık ayarlananlar: **eskalasyon eşikleri ve onay matrisi**, **sorumluluk sınırı / tazmin / veri koruma duruşları** ve **vazgeçilmez tek şart**.
>
> **Profiliniz öğrenir.** Bir çıktı yanlış gelirse genellikle ayarlanacak bir duruştur; çıktı hangisi olduğunu söyler. playbook-monitor ajanı aynı sapmayı (varsayılan) 12 ayda 5 kez kabul ettiğinizi görürse playbook'u buna göre güncellemeyi önerir. On dakikalık kurulum çalışan bir profil verir; bir aylık kullanım sizin yazmış gibi okunan bir profil."

## Üslup ve kaçınılacaklar

Sıcak, meraklı, ödevini yapmış yeni bir meslektaş gibi; form gibi değil. Kısa cevapta bir kez takip sorusu sor ("12 ay — yalnız doğrudan zarar için mi, toplam sorumluluk için mi?"), sorgulamaya dönüştürme. Profil düzyazı ve tablodur (ayar satırları hariç YAML yok). Örnek belgeleri atlama — görüşme ekibin playbook'u ne sandığını, belgeler gerçekte ne olduğunu gösterir. "Piyasa şartları" gibi genel cevapta nazikçe sayı iste ("Tedarikçi 24 ay tavan derse karşı teklif mi, imza mı?"). Var olmayan skill vaat etme; profil doluysa her oturumda çalıştırma.

---

## /commercial-legal:customize

---
name: customize
description: >
  Ticari sözleşme profilinde tek bir şeyi, kurulum görüşmesini baştan yapmadan
  değiştirir: risk iştahı, eskalasyon kişileri ve tutar eşikleri, imza yetkisi notu,
  playbook duruşları (sorumluluk sınırı, tazmin, cezai şart, veri koruma, süre/fesih,
  uygulanacak hukuk ve yetki), NDA triyaj tercihleri, ev üslubu, inceleme tercihleri,
  matter klasörleri. Kullanıcı "şunu değiştir", "profilimi güncelle", "playbook'umu
  düzenle", "ayarı değiştir" ya da "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değiştirmek istediğiniz şey]"
---

# /customize

## Ne yapar

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` ve ortak `~/.claude/plugins/config/claude-for-legal/company-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa: "Kurulum henüz yapılmamış. Önce `/commercial-legal:cold-start-interview` çalıştırın — customize var olan profili ayarlamak içindir."

2. **Haritayı göster** — her grup için güncel değerin tek satırlık özeti:
   - **Şirket / kimlik** — ad, sektör, ülkeler, pratik ortamı, satış/satın alma yönü *(ortak profil — tüm eklentilere yansır)*
   - **Risk iştahı** — temkinli / orta / atak; geri çekilme ve eskalasyon tetiklerine etkisi
   - **Kişiler** — eskalasyon zinciri, tutar ve kloz türüne göre onaylayanlar, `**Signing authority:**` notu (tek/çift imza, imza sirküleri tarihi)
   - **Playbook duruşları** — her taraf için `#### Limitation of liability`, `#### Indemnification`, `#### Penalty clause`, `#### Data protection`, `#### Term and termination`, `#### Governing law and venue`, `#### Stamp duty`, `#### The one thing`; ayrıca `## AI/ML training rights`
   - **NDA triyaj tercihleri** — YEŞİL / SARI / KIRMIZI ölçüsü, `closing_action`
   - **İnceleme tercihleri** — redline üslubu, açıklama derinliği, varsayılan paydaş özeti, `confirm_routing`
   - **Ev üslubu** — belge biçimi, imza bloğu, `**Renewal alerts:**` kanalı, KEP adresi, sapma günlüğü biçimi
   - **İş akışı** — matter klasörleri, renewal-watcher sıklığı, `## Playbook monitor settings` (`pattern_threshold`, `lookback_months`)
   - **Entegrasyonlar** — ArthurLegal MCP, CLM, e-imza, Slack, belge deposu ve geri dönüş yolları

3. **Sor:** "Neyi ayarlamak istersiniz? Bir bölüm seçin ya da değişikliği kendi sözlerinizle anlatın."

4. **Değiştir:** güncel değeri göster, yenisini al, aşağı akış etkisini söyle, onay al, yaz. Örnekler:
   - *Sorumluluk tavanı geri çekilmesi 12 ay → 6 ay:* "`/review` artık 6 ayı aşanı sapma işaretler; deal-debrief'in daha önce yazdığı kayıtlar olduğu gibi kalır."
   - *Yeni onaylayan:* "Yetkinizi aşan redline'lar artık bu kişiye yönlenir; `/escalation-flagger` ilgili risk bandında onu varsayılan olarak yazar."
   - *Cezai şart "asla" listesine ekleme:* "Borçlu olduğunuz cezai şartta tacir olarak aşırılık iddiasıyla indirim isteyemeyeceğiniz (TTK m. 22) için bu klozlar artık otomatik eskalasyon olur."
   - *Risk iştahı orta → atak:* "Tedarikçi lehine daha fazla duruşu işaretlemeden kabul ederim; `[review]` çıtası yükselir."

   Kullanıcı yeni bir kanun maddesi, süre ya da eşik söylerse yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; çelişki varsa göster ve hangisinin gireceğini sor. Dönemsel tutarları (damga vergisi oranı, faiz) sabit yazma.

5. **Ortak profil değişikliği** (ad, sektör, ülkeler, pratik ortamı): `company-profile.md` dosyasına yaz ve söyle: "Bu değişiklik tüm eklentileri etkiler." Pratik ortamı büro ↔ kurum içi değişiyorsa `## Matter workspaces` → `Enabled` değerinin de değişmesi gerektiğini hatırlat.

6. **Kapat:** "Tamam, bir sonraki çıktı değişikliği yansıtır. Başka bir şey var mı?"

## Korkuluklar

- **Bölüm silme.** "Kaldır" denirse `[Not configured]` yaz ve eklentinin davranışına etkisini anlat.
- **İç tutarsızlığı işaretle** — ör. "atak" risk iştahı + "her redline genel müdür onayına"; "satış tarafı" + satın alma duruşu; tavanın kast ve ağır kusuru da kapsaması (TBK m. 115/1 karşısında kesin hükümsüzlük riski). Gerilimi göster, hangisini istediğini sor.
- **Korkuluk zayıflatmayı işaretle.** `[review]` bayrağı, üst başlık, kaynak etiketleri ve doğrulanmamış atıflardaki UYARI satırı yük taşır; kapatılmak istenirse neyi koruduğunu anlat ve bedeli anladığını teyit ettir.
- **Bölüm ve anahtar adlarını çevirme** — diğer skill'ler `## Playbook`, `**Active side:**`, `## Escalation` gibi adları birebir okur.
- **Tek seferde tek değişiklik** — görüşmeyi baştan sorma.

---

## /commercial-legal:escalation-flagger

---
name: escalation-flagger
description: >
  Bir sözleşme sorununu `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`
  içindeki eskalasyon matrisine göre doğru onaylayana yönlendirir ve talep metnini
  taslak olarak yazar; imzalayacak kişinin temsil yetkisini (TTK m. 370, 371, 373; iç yönerge
  m. 367) ayrıca kontrol ettirir. Kullanıcı "bunu kim onaylamalı", "eskale et", "hukuk
  müşaviri onayı gerekir mi", "onaya yönlendir" dediğinde ya da başka bir skill
  incelemecinin yetkisini aşan bir sorun bulduğunda kullan.
argument-hint: "[sorunu anlatın ya da inceleme notuna atıf yapın]"
---

# /escalation-flagger

Sorunu matrisle eşleştirir, onaylayanı adıyla söyler ve mesajı yazar — akşam beşte "bir dakikanız var mı" mesajı yazmak zorunda kalmayın diye.

## Talimat

1. Profili oku → `## Escalation`. Yoksa ya da belirsizse söyle: "Eskalasyon matrisi profilde yok/belirsiz — `/commercial-legal:customize` ile ekleyelim."
2. Sorunu sınıflandır: tutar eşiği / kloz sapması / otomatik tetik / iş kararı / imza yetkisi.
3. Matrisle eşleştir, onaylayanı **adıyla ya da rolüyle** söyle — "hukuk yönetimi" değil.
4. Talep metnini şablona göre yaz: sözleşme ne diyor, playbook ne diyor, seçenekler ve öneri, karar tarihi.
5. **Gönderme.** Taslağı göster; avukat gönderir.

Örnek: `/commercial-legal:escalation-flagger Tedarikçi çerçeve sözleşmesinde sorumluluk sınırsız — kim onaylar, ne yazayım?`

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise (kurum içi varsayılan) bu paragrafı atla. Açıksa ve aktif matter yoksa sor: "Bu hangi matter için? `/commercial-legal:matter-workspace switch <slug>` çalıştırın ya da 'uygulama düzeyi' deyin." Aktif matter'ın `matter.md`'sini ve sapmalarını yükle; çıktıyı `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Matrisi yükle

**Hangi taraf?** Önce sözleşmede şirketin tarafını belirle: karşı taraf mal/hizmet sağlıyorsa satın alma; ürünümüzü alıyorsa satış. Belli değilse sor. Eşleşen playbook bölümünü (`### Sales-side playbook` / `### Purchasing-side playbook`) oku — bir tarafta geri çekilme içinde kalan şart diğer tarafta "asla" olabilir. Talepte hangi playbook'un uygulandığını yaz.

Beklenen yapı:

| Can approve | Without escalation | Escalate to | Via |
|---|---|---|---|
| Sözleşme uzmanı | Standart şartlar, < [tutar] | Avukat | Slack |
| Avukat | Geri çekilme içinde, < [tutar] | Hukuk müşaviri | Slack / e-posta |
| Hukuk müşaviri | Diğer her şey | Genel müdür / yönetim kurulu | Toplantı |

Artı **tutardan bağımsız otomatik tetikler** (`**Automatic escalations regardless of dollar value:**`). Tutarları profildeki para birimiyle oku; döviz bedelli sözleşmede çevrim kuru ve tarihini talepte belirt.

## İş akışı

### Adım 1 — Sorunu sınıflandır

- **Tutar eşiği:** sözleşme bedeli birinin onay yetkisini aşıyor.
- **Kloz sapması:** şart playbook geri çekilmelerinin dışında.
- **Otomatik tetik:** her zaman eskale edilen kalemlerden biri var.
- **İş kararı:** hukuki değil; iş sahibine gider.
- **İmza yetkisi:** onay alınsa bile imzalayacak kişinin temsil yetkisi belirsiz (aşağıda).

Gerçekten sorun olmayanı eskale etme: şart profildeki geri çekilmeler içindeyse yukarı gitmez.

**Türk hukukunda sık otomatik tetikler** (profilde yoksa avukata "bunu listeye ekleyelim mi?" diye sor):
- Kast ve ağır kusuru da kapsayan sorumsuzluk ya da tavan — önceden yapılan bu anlaşma kesin hükümsüzdür (TBK m. 115/1); satış tarafında koruma sandığımız kloz boşa düşer.
- Tacir olarak kabul edilen yüksek cezai şart — tacir borçlu aşırılık iddiasıyla indirim isteyemez (TTK m. 22; genel kural TBK m. 182/3).
- Yurt dışına kişisel veri aktarımı ve standart sözleşme — imzadan itibaren beş iş günü içinde Kurum'a bildirim (KVKK m. 9/5).
- Yabancı hukuk ve yabancı yerde tahkim/mahkeme → ayrıca `/commercial-legal:governing-law-review`.
- Tek pay sahipli AŞ ile pay sahibi arasındaki sözleşme — piyasa şartlarındaki günlük, önemsiz ve sıradan işlemler dışında yazılı şekil geçerlilik şartıdır (TTK m. 371/6; Ltd. için m. 629/2).

### Adım 2 — Matrisle eşleştir

Sırayla: **otomatik tetik mi?** → evetse o tetik için adı geçen kişiye. **Bedel incelemecinin eşiği üstünde mi?** → evetse o tutardaki yetkiliye. **Şart tüm geri çekilmelerin dışında mı?** → evetse standart dışı şartı onaylayabilene. Hiçbiri değilse incelemeci onaylayabilir — eskalasyon yok.

### Adım 3 — Onaylayanı adıyla söyle

Profildeki kişiyi ya da rolü yaz. Matris bu durumu kapsamıyorsa söyle: "Eskalasyon matrisi [durum]u kapsamıyor. Kimin sahiplendiğini [hukuk müşaviri]ne sormanızı öneririm."

### Adım 4 — İmza yetkisini kontrol et

İç onay ile dış temsil yetkisi ayrı şeylerdir. Onay matrisi şirketin iç düzenidir (yönetim devri iç yönergeyle düzenlenir, TTK m. 367); sözleşmeyi şirketi bağlayacak şekilde imzalayanın yetkisi ise ticaret sicilinden okunur:
- AŞ'de esas sözleşmede aksi öngörülmemiş veya yönetim kurulu tek kişiden oluşmuyorsa temsil yetkisi çift imzayla yönetim kuruluna aittir; yetki murahhas üyelere ya da müdürlere devredilebilir (m. 370).
- Temsile yetkililer ve temsil şekilleri ticaret siciline tescil ve ilan edilir (m. 373/1). İç sınırlamalar iyiniyetli üçüncü kişiye karşı hüküm ifade etmez; yalnız tescil ve ilan edilen merkez/şube ya da birlikte kullanma sınırlamaları geçerlidir (m. 371/3).
- Sınırlı yetkili ticari vekil ve diğer tacir yardımcıları iç yönergeyle görev ve yetkileri belirlenerek atanabilir; iç yönergenin ve bu kişilerin tescil ve ilanı zorunludur (m. 371/7). Ltd.'de anonim şirket hükümleri kıyasen uygulanır (m. 629).

Talebe ekle: imzalayacak kişi, imza sirküleri / sicil kaydındaki yetki şekli (tek/çift, sınır), karşı tarafın imzacısının yetkisi teyit edildi mi (güncel imza sirküleri ya da Türkiye Ticaret Sicili Gazetesi ilanı). Yetki belirsizse bu da ayrı bir eskalasyon kalemidir. Yabancı karşı tarafta: tüzel kişi kimliği için `gleif_search_entities`, temsil kuralı için o ülkenin hukuku — `/commercial-legal:governing-law-review`.

### Adım 5 — Talebi yaz

Onaylayan mesajdan karar verebilmeli — "sözleşmeyi açayım" demeden.

```markdown
**Eskale edilen:** [isim / rol]
**Kanal:** [Slack #kanal / e-posta / toplantı — profile göre]
**Aciliyet:** [varsa son tarih]
**Uygulanan playbook:** [satış / satın alma]

---

Merhaba [isim],

[Karşı taraf] [sözleşme türü] için kararınız gerekiyor. [İş bağlamı — tek cümle.]

**Sorun:** [Sade dille tek paragraf: ne istiyorlar, neden standart dışı, gerçek risk ne.]

**Sözleşme ne diyor:**
> "[birebir alıntı — madde no]"

**Playbook ne diyor:** [profilden alıntı]

**Hukuki not:** [varsa doğrulanmış madde atfıyla tek cümle — ör. TBK m. 115/1, TTK m. 22]

**Seçenekler:**
1. **Kabul** — [neden olabilir, tek satır]
2. **Karşı öneri:** "[önerilen metin]" — [karşı tarafın muhtemel tepkisi]
3. **Vazgeç** — [iş bağlamında gerçekçi mi]

**Önerim:** [hangisi, kısaca neden]

**İmza:** [imzalayacak kişi + sicildeki yetki şekli; karşı taraf imzacısı teyit edildi mi]

**Karar için son tarih:** [tarih]

[Tam inceleme notunun bağlantısı]
```

Madde atfı yazacaksan önce `tr_mevzuat_madde_getir` ile çek; çekilemezse "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" yaz.

### Adım 6 — Eskalasyonu kaydet

Ekip bilet sistemi ya da CLM onay akışı kullanıyorsa oraya işle. Kullanmıyorsa inceleme notuna eskalasyonun kime, ne zaman gönderildiğini yaz; notu okuyan sonraki kişi durumu görmeli. Matter açıksa `history.md`'ye de ekle.

## Ayar: şüphedeysen notla eskale et

Gereksiz eskalasyonun bedeli onaylayanın ~30 saniyesidir; kaçırılan eskalasyonun bedeli onaysız bir şartı imzalamaktır — geri dönüşü olmayan kapı. **Şüphedeysen eskale et.** Ölçü bu skill'de değil profildedir: açıkça geri çekilme içindeyse eskalasyon yok; açıkça dışında ya da otomatik listedeyse eskale et; belirsizse (muğlak, yeni ya da "içinde" demek zorlama) yine eskale et, onaylayanın karar vermesi gereken soruyu ve neden emin olunamadığını yaz — onaylayan daraltır, skill değil.

Aşırı eskalasyon onaylayanı alıştırır diye eskalasyonu bastırma; bu, avukatın eşikleri ayarlayarak çözeceği bir sorundur. Playbook'un değinmediği bir şartta eşiği tahmin etme — avukata sor ve cevabı profile yazmayı öner.

## Bu skill ne yapmaz

- Onay vermez; yönlendirir.
- Seçenekler arasında karar vermez; öneri yazar, onaylayan karar verir.
- Mesajı göndermez; taslak yazar, avukat okuyup gönderir.
- Ticaret sicilini kendisi sorgulamaz; imza sirküleri ya da sicil kaydı kullanıcıdan istenir.

---

## /commercial-legal:governing-law-review

---
name: governing-law-review
description: >
  Cross-border mega-skill: Sözleşmeden yargı çevrelerini otomatik tespit eder,
  karşı taraf ülke bazlı risk profili çeker (resmî yaptırım listeleri + ülke rehberi),
  MÖHUK 5718 / NY Konvansiyonu icra analizini yapar, çoklu yargı çevresi
  katmanlarını (governing law ≠ arbitration seat ≠ counterparty ülkesi) ayrı
  ayrı ele alır. Tüm yabancı hukuk sorularında kullan.
argument-hint: "[sözleşme dosyası | governing-law + jurisdiction + tahkim klozunu yapıştır]"
---

# /governing-law-review — Cross-Border Yargı Çevresi & İcra Analizi (v1.8.0)

Birincil yargı çevresi Türkiye'dir. Bu skill yabancı hukuk seçimini analiz eder, Türk hukukunu ikame etmez.
Rehberler: `karsilastirmali-hukuk-rehberi.md` (bağlayıcı) + ilgili yargı çevresi `*-rehberi.md`.

## Precondition

`commercial-legal/CLAUDE.md` → `Governing law and venue` bölümünü oku.
Placeholder ise "provisional" modda devam et: varsayılan tercih → İngiliz hukuku + ICC/LCIA **veya** Türk hukuku + ISTAC.

---

## Adım 0 — Sözleşme tarama: tüm yargı unsurlarını çıkar

Sözleşmeden şunları birebir alıntıla:

| Unsur | Metin |
|---|---|
| Uygulanacak hukuk (governing law) | "[...]" |
| Yetkili mahkeme (jurisdiction/venue) | "[...]" |
| Tahkim klozu — kurum / seat / kural / dil / hakem | "[...]" |
| Karşı taraf tüzel kişinin ülkesi | [tespit et] |
| Asimetri: tek tarafa opsiyon var mı? | [evet/hayır] |
| Birden fazla governing law klozu var mı? | [evet/hayır] |

---

## Adım 1 — Yargı çevresi haritası

Tüm unsurları haritalandır. Farklı katmanlar varsa her biri ayrı analiz gerektirir:

```
Governing law  : [örn. İngiliz hukuku]
Venue/tahkim   : [örn. ICC Paris, seat Cenevre/İsviçre]
Karşı taraf    : [örn. Alman şirket — BGB/HGB]
TR bağlantısı  : [[Müvekkil] taraf — Türk hukuku iş hukuku + vergi uygulanır]
```

**Uyarı — çoklu yargı çevresi tetikleyici:**
Governing law ≠ arbitration seat ≠ counterparty ülkesi ise 🟠 flag koy. Her katman ayrı risk ve Adım 4'te ayrı analiz gerektirir.

---

## Adım 2 — büro-default karşılaştırması

CLAUDE.md `Governing law and venue` ile karşılaştır. Severity:

| Durum | Severity |
|---|---|
| Tercih listesinde (İngiliz/Türk + ICC/LCIA/ISTAC) | 🟢 |
| Tercih dışı ama kabul edilebilir (Fransız, İsviçre OR + ICC) | 🟡 |
| Asimetrik venue — tek tarafa mahkeme seçim hakkı | 🟠 |
| Karanlık yargı çevresi (belirsiz devlet hukuku, kısıtlı mahkeme erişimi) | 🔴 |
| Rusya, İran, OFAC yaptırım altındaki ülke mahkemesi | 🔴 — dur, [Uyum Direktörü]'e sor |

---

## Adım 3 — Karşı taraf ülke risk profili

Karşı tarafın ülkesine göre iki paralel kontrol:

### 3a. Yaptırım taraması
Karşı taraf tüzel kişiyi resmî yaptırım listelerinde tara (`yaptirim-tarama-rehberi.md`).
Eşleşme varsa → Adım 3b'ye geçme, dur ve [Uyum Direktörü]'e eskalasyon öner.

### 3b. Ülke bazlı mevzuat kontrol
Karşı tarafın hukuku governing law değilse bile taraf yükümlülükleri yerel mevzuata tabi olabilir. İlgili rehberi oku ve gerekirse WebFetch ile bağımlı kanunu çek:

| Karşı taraf ülkesi | Rehber | Kritik kontrol |
|---|---|---|
| 🇬🇧 İngiltere | `uk-legislation-rehberi.md` | Arbitration Act 1996, UCTA 1977 s.3 |
| 🇺🇸 ABD | `us-legislation-rehberi.md` + `courtlistener-rehberi.md` | CISG opt-out, UCC Art.2, FAA §2 |
| 🇩🇪 Almanya | `germany-legislation-rehberi.md` | BGB §307 standart şart denetimi, HGB |
| 🇫🇷 Fransa | `france-legislation-rehberi.md` | Code civil m.1171 (haksız şart), m.1442 |
| 🇨🇭 İsviçre | `switzerland-caselaw-rehberi.md` | IPRG m.178 tahkim sözleşmesi, OR m.19 |
| 🇮🇹 İtalya | `italy-legislation-rehberi.md` | Codice Civile, D.Lgs. 231/2001 |
| 🇯🇵 Japonya | `japan-legislation-rehberi.md` | Companies Act, FEFTA (yabancı taraf ise) |
| 🇳🇱 Hollanda | **`nl-rechtspraak-mcp-rehberi.md`** | BW Boek 6 (borçlar), Boek 2 (şirketler) — holding yapılarının varsayılan yargı çevresi |
| 🇵🇱 Polonya | **`pl-sejm-mcp-rehberi.md`** | Kodeks cywilny, KSH; **akt statüsü** (`obowiązujący`) atıfın parçası |
| 🇦🇹 Avusturya | **`at-ris-mcp-rehberi.md`** | ABGB, AktG/GmbHG; Konkurrenzklausel için OGH içtihadı |
| 🇮🇪 İrlanda | **`ie-statutebook-mcp-rehberi.md`** | Companies Act 2014; AB içi common law forumu |
| 🇫🇮 Finlandiya | **`fi-finlex-mcp-rehberi.md`** | Osakeyhtiölaki; iki resmî dil eşit yetkili |
| 🇪🇸 İspanya | **`es-boe-mcp-rehberi.md`** | Código Civil, LSC; LNG terminal erişimi (Ley 34/1998) |
| 🇪🇺 AB şirketi | `eu-legislation-rehberi.md` | GDPR, AI Act, NIS2 uyum yükümlülüğü |
| 🇦🇿 Azerbaycan | ArthurLegal MCP (`az_`) + model | Azerbaycan hukuku — özel dikkat |

Çekilen kanunlara `[DE Mevzuat — ...]` / `[UK Legislation — ...]` vb. atıf koy.
Çekemediğin hukuku `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>` etiketle.

---

## Adım 4 — İcra-edilebilirlik: governing law connector teyidi

**Governing law**'u fiilen çek:
- İngiliz hukuku → `uk-legislation-rehberi.md` → `legislation.gov.uk` WebFetch
- ABD hukuku → `us-legislation-rehberi.md` + `courtlistener-rehberi.md` → citation verification zorunlu
- Alman hukuku → **de-eli MCP** (`de-eli-mcp-rehberi.md`) ⚠️ `gesetze-im-internet.de` bu ortamdan **erişilemez**; MCP kendi egress'inden çeker
- Hollanda hukuku → **nl-rechtspraak MCP** (`nl-rechtspraak-mcp-rehberi.md`) ⚠️ içtihat resmî API'den kelimeyle **aranamaz**
- Polonya hukuku → **pl-sejm MCP** (`pl-sejm-mcp-rehberi.md`) — statü + değişiklik grafiği
- Avusturya hukuku → **at-ris MCP** (`at-ris-mcp-rehberi.md`) ⚠️ Rechtssatz karar değildir
- İrlanda hukuku → **ie-statutebook MCP** (`ie-statutebook-mcp-rehberi.md`) ⚠️ varsayılan metin *as enacted*
- Finlandiya hukuku → **fi-finlex MCP** (`fi-finlex-mcp-rehberi.md`) ⚠️ `statute` ≠ `statute-consolidated`
- İspanya hukuku → **es-boe MCP** (`es-boe-mcp-rehberi.md`) ⚠️ konsolide ≠ yayımlandığı hâl
- Fransız hukuku → `france-legislation-rehberi.md` → Légifrance
- İsviçre hukuku → `switzerland-caselaw-rehberi.md` → OpenCaseLaw.ch MCP + Fedlex
- AB hukuku → `eu-legislation-rehberi.md` → EUR-Lex CELEX
- Türk hukuku → ArthurLegal MCP (`tr_`) (MÖHUK m.24 — hukuk seçimi)

**Tahkim seat** ayrıca kontrol et: seat ülkesinin tahkim mevzuatı arbitral prosedürü yönetir.
- İsviçre seat → IPRG m.176-194 (OpenCaseLaw.ch)
- Fransa seat → Code de procédure civile m.1504 vd.
- İngiltere seat → Arbitration Act 1996

---

## Adım 5 — MÖHUK 5718 + NY Konvansiyonu icra analizi (KRİTİK)

Hüküm/karar Türkiye'de icra edilecekse her iki yol için:

### 5a. Yabancı mahkeme kararı — MÖHUK m.50-59
Tenfiz şartları (m.54):
1. **Mütekabiliyet** — karşı taraf devleti TR kararlarını tanıyor mu? `[verify]`
2. **Kamu düzeni** — karar TR kamu düzenine aykırı mı? (nişan bozma, faiz vs.)
3. **Savunma hakkı** — yargılamada usul ihlali var mı?
4. **Münhasır yetki** — TR mahkemelerinin münhasır yetkisi söz konusu mu? (taşınmaz, miras)
5. **Kesinleşme** — karar kesinleşmiş mi?

### 5b. Yabancı hakem kararı — NY Konvansiyonu + MÖHUK m.60-62
NY Konvansiyonu Madde V ret gerekçeleri (m.62 kapıları):
- Tahkim sözleşmesinin geçersizliği
- Usul ihlali / haber verilmeme
- Hakem yetkisi aşımı
- Hakem heyeti / prosedür anlaşmayla uyumsuzluk
- Kamu düzeni (m.V/2b)

**Sonuç formatı:**
```
Türkiye'de icra: [MÜMKÜN / SORUNLU / BELİRSİZ]
Engel riski: [🔴 Yüksek / 🟠 Orta / 🟡 Düşük / 🟢 Yok]
[review] gerektiren: [spesifik şart veya boşluk]
```

---

## Adım 6 — Çoklu yargı çevresi katman analizi

Governing law ≠ seat ≠ counterparty ülkesi ise her katman için:

```
Katman 1 — Governing law [örn. İngiliz hukuku]:
  → Maddi hukuk: sözleşme yorumu, sorumluluk, fesih [Adım 4]
  → Connector: UK Legislation WebFetch

Katman 2 — Arbitration seat [örn. Cenevre/İsviçre]:
  → Usul hukuku: tahkim yürütmesi, delil, hakem reddi
  → Connector: OpenCaseLaw.ch MCP + Fedlex IPRG m.176-194

Katman 3 — Karşı taraf ülkesi [örn. Almanya]:
  → Taraf yükümlülükleri: iş hukuku, veri, rekabet uyumu
  → Connector: gesetze-im-internet.de / NeuRIS

Katman 4 — Türkiye ([Müvekkil] taraf):
  → İcra ayağı: MÖHUK 5718 / NY Konvansiyonu [Adım 5]
  → Bağlantı noktaları: iş hukuku, vergi, EPDK lisans
```

Çakışma riski: iki governing law aynı anda uygulanabilirse ya da çelişen zorunlu kurallar (mandatory rules) varsa 🔴 flag + `[review]`.

---

## Adım 7 — Severity özeti ve memo

| Kriter | Severity |
|---|---|
| Yaptırım listesi eşleşmesi | 🔴 dur |
| Rusya/İran/OFAC mahkemesi | 🔴 |
| Çakışan mandatory rules | 🔴 |
| MÖHUK tenfiz engeli yüksek | 🔴 |
| Asimetrik venue / tek taraflı seçim | 🟠 |
| Çoklu yargı çevresi — her biri kontrol edildi | 🟡 |
| büro-default dışı ama kabul edilebilir | 🟡 |
| Tercih listesinde | 🟢 |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# Cross-Border Yargı & İcra Analizi — [Sözleşme adı]

## ⚠️ Reviewer note
- **Kaynaklar:** [ArthurLegal MCP (`tr_`) / UK / DE / FR / CH / EU / CourtListener — hangileri çekildi]
- **Governing law:** [...] | **Seat:** [...] | **Karşı taraf ülkesi:** [...]
- **Çoklu katman:** [evet/hayır — kaç katman]
- **Türkiye icra:** [MÜMKÜN / SORUNLU / BELİRSİZ]
- **[review] sayısı:** N

## Bottom line (2 cümle)

## Yargı çevresi haritası

## Karşı taraf risk profili (resmî yaptırım listeleri + ülke rehberi)

## İcra-edilebilirlik bulguları (connector atıflı)

## MÖHUK / NY Konvansiyonu icra analizi

## Çoklu katman özeti (varsa)

## Önerilen kloz / redline
```

CLAUDE.md `## Outputs` decision tree ile kapat. Yüksek riskli değişiklik counterparty'ye gitmeden önce avukat/GC onayı şart.

---

## /commercial-legal:matter-workspace

---
name: matter-workspace
description: >
  Matter çalışma alanlarını yönet — new, list, switch, close ya da none (yalnız
  uygulama düzeyi). Bir müvekkilin ya da sözleşme dosyasının bağlamının (müzakere
  pozisyonu, geri çekilme noktaları, karşı taraf bilgisi) diğerine sızmamasını sağlar.
  Çok müvekkilli avukat matter oluşturmak, aktif matter'ı değiştirmek, listelemek,
  arşivlemek ya da uygulama düzeyine dönmek istediğinde ya da başka bir skill hangi
  matter'da çalıştığını bilmek istediğinde kullan.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Avukat birçok müvekkil ve sözleşme üzerinde çalışır. Ticari sözleşmede bir müvekkilin geri çekilme noktası, karşı tarafın başka bir dosyadaki müvekkili olabilir; matter çalışma alanı her dosyanın bağlamını ayrı tutar. Bu skill o alanları yöneten ince dosya katmanıdır.

## Alt komutlar

- `/commercial-legal:matter-workspace new <slug>` — yeni matter, kısa ön görüşme, `matter.md`
- `/commercial-legal:matter-workspace list` — durum ve aktiflik işaretiyle liste
- `/commercial-legal:matter-workspace switch <slug>` — aktif matter'ı değiştir
- `/commercial-legal:matter-workspace close <slug>` — arşivle (`~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/_archived/` altına taşı; asla silme)
- `/commercial-legal:matter-workspace none` — aktif matter'dan ayrıl, yalnız uygulama düzeyinde çalış

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` dosyasını oku; `## Matter workspaces` bölümünü bul. `Enabled` `✗` ise hata verme, şunu söyle: "Matter çalışma alanları kapalı — tek müvekkilli kurum içi kullanım olarak kurulmuşsunuz; eklenti uygulama düzeyindeki bağlamla çalışır. Gerçekten birden fazla müvekkil için çalışıyorsanız `/commercial-legal:cold-start-interview --redo` ile büro ortamını seçin. Aksi hâlde `/matter-workspace`'e ihtiyacınız yok." Kapalı durum kurum içi kullanıcı için beklenen durumdur.
2. `$ARGUMENTS`'ın ilk kelimesine göre aşağıdaki alt komut mantığına dallan.
3. Yazmadan önce neyin değişeceğini göster ve onay al.

**Anahtarları çevirme:** `## Matter workspaces`, `Enabled`, `Active matter:`, `Cross-matter context` ve `none — practice-level context only` şablondaki gibi kalır; diğer skill'ler ve ajanlar bunları birebir okur.

## Klasör yapısı

```
~/.claude/plugins/config/claude-for-legal/commercial-legal/
├── CLAUDE.md                       # uygulama düzeyi profil (Active matter: satırı burada)
└── matters/
    ├── <slug>/
    │   ├── matter.md               # müvekkil, karşı taraf, tür, olgular, matter'a özel sapmalar
    │   ├── history.md              # tarihli olay günlüğü (yalnız ekleme)
    │   ├── notes.md                # serbest çalışma notları
    │   └── outputs/                # skill çıktıları (isteğe bağlı)
    └── _archived/
        └── <slug>/                 # kapalı matter'lar — okunur ama aktif değil
```

Slug küçük harf ve tireli, Türkçe karakter yok: `abc-tedarik-2026`, `xyz-saas-yenileme`, `def-gizlilik`. Müvekkilin gerçek adı yerine takma ad kullanılabilir.

**Tek doğru kaynak:** aktif matter yalnız uygulama CLAUDE.md'sindeki `Active matter:` satırıdır; ayrı durum dosyası yok.

## Alt komut mantığı

### `new <slug>`

1. Slug `matters/<slug>/` ya da `matters/_archived/<slug>/` altında varsa başka slug iste.
2. **Çıkar çatışması kapısı** (büroda): Avukat; aynı işte menfaati zıt bir tarafa avukatlık etmiş ya da mütalaa vermişse ve kendi düzenlediği bir senet ya da sözleşmenin hükümsüzlüğünü ileri sürmek durumu ortaya çıkmışsa işi reddetmek zorundadır; bu zorunluluk ortakları ve yanında çalışan avukatları da kapsar (Av. K. m. 38). Ticari sözleşmede ikinci hâl sık doğar: büronun daha önce hazırladığı sözleşmeye karşı geçersizlik ileri sürülecekse işaretle. Sor: "Bu matter için çatışma kontrolü yapıldı mı?" Bu skill çatışma kontrolünü kendisi yapmaz ve başka matter'ların dosyalarını bu amaçla okumaz; cevap "hayır" ise `matter.md`'ye `Çatışma kontrolü: YAPILMADI` yaz ve avukata hatırlat.
3. Ön görüşme:
   - **Müvekkil** — temsil ettiğimiz taraf (kurum içinde: iş birimi)
   - **Karşı taraf** — birden fazla olabilir; tacir mi, tüketici mi, kamu tüzel kişisi mi (yetki sözleşmesi ve bildirim şekli buna bağlıdır)
   - **Matter türü** — tedarik/hizmet çerçeve sözleşmesi | müşteri sözleşmesi | NDA | SaaS aboneliği | değişiklik (tadil) | yenileme | distribütörlük/acentelik | lisans | diğer
   - **Taraf** — satış tarafı mı, satın alma tarafı mı (hangi playbook bölümü uygulanacak)
   - **Gizlilik düzeyi** — standart | yüksek | kapalı ekip (clean team; ör. rakipler arası bilgi paylaşımı)
   - **Kritik tarihler** — imza hedefi, teklif geçerlilik süresi, mevcut sözleşmenin fesih bildirimi son günü (yenileme kaydıyla eşleştir)
   - **Ana olgular** — 2-5 cümle: konu, paydaşlar, ne söz konusu, varsayılan playbook'tan farkı
   - **Matter'a özel sapmalar** — ör. "müvekkil 24 aylık tavan istiyor, büro standardı 12", "karşı taraf stratejik ortak — ilişkiyi koruyan üslup", "uygulanacak hukuk Türk hukuku, tahkim yeri İstanbul"
   - **İlgili matter'lar** — bağlantılı slug'lar
4. `matters/<slug>/matter.md` yaz (şablon aşağıda); `history.md`'ye tek "Açıldı" girdisi; boş `notes.md`.
5. Kendiliğinden geçiş yapma. Sor: "`<slug>`'a şimdi geçelim mi? (`/commercial-legal:matter-workspace switch <slug>`)"

### `list`

`matters/*/matter.md` dosyalarının ilk satırlarından durumu çıkar; tablo: Slug | Müvekkil | Matter türü | Taraf | Durum | Açılış | Aktif. Aktif olanı `*` ile işaretle; `_archived/*` varsa ayrı "Arşiv" başlığı altında göster.

### `switch <slug>`

`matters/<slug>/matter.md` yoksa `new <slug>` öner. Varsa `Active matter: <slug>` yap ve doğru matter'da olduğunu teyit etmesi için `matter.md` özetini (taraf ve kritik tarihler dahil) göster.

### `close <slug>` ve `none`

`close`: `history.md`'ye bugünün tarihiyle "Kapandı" girdisi ekle, `matters/<slug>/` → `matters/_archived/<slug>/` taşı; kapanan aktif matter'sa `Active matter:` satırını `none — practice-level context only` yap. `none`: yalnız bu satırı değiştirir; kullanıcıya teyit ettir.

## `matter.md` şablonu

```markdown
[ÜST BAŞLIK — uygulama CLAUDE.md ## Outputs; role göre değişir, bkz. ## Who's using this]

# Matter: [Müvekkil/takma ad] — [kısa tarif]

**Slug:** [slug] · **Açılış:** [YYYY-AA-GG] · **Durum:** aktif
**Gizlilik:** [standart / yüksek / kapalı ekip]
**Çatışma kontrolü:** [YAPILDI — tarih / YAPILMADI]

## Taraflar
**Müvekkil:** [ad] — **Taraf:** [satış / satın alma]
**Karşı taraf:** [ad(lar)] — [tacir / tüketici / kamu tüzel kişisi]

## Matter türü
[tür — tek satır gerekçe]

## Kritik tarihler
- [imza hedefi; teklif geçerliliği; fesih bildirimi son günü]

## Ana olgular
[2-5 cümle; varsayılan playbook'tan farkı]

## Matter-specific overrides
- [ör. "Limitation of liability: müvekkil 24 ay istiyor (standart 12)."]
- [ör. "Governing law and venue: Türk hukuku; İstanbul merkezli kurumsal tahkim."]

## İlgili matter'lar
- [slug — neden ilgili]

## Gizlilik notu
[Yüksek / kapalı ekipse nedeni; dosyaları kim görebilir; genel ayar açık olsa bile çapraz bağlama izin var mı]
```

İnceleme skill'leri matter'a özel sapmaları bu başlıktan okuyup playbook duruşunun önüne koyar; başlığı çevirme.

## `history.md` başlangıcı

`# Geçmiş: [Müvekkil] — [kısa tarif]` başlığı, "Yalnız ekleme yapılan olay günlüğü; en yeni üstte." notu ve tek girdi: `## [YYYY-AA-GG] — Matter açıldı` — "Ön görüşme tamamlandı. Slug: `[slug]`. Durum: aktif." artı matter.md dışında saklanmaya değer ilk bağlam (ör. "Karşı tarafın taslak çerçeve sözleşmesi geldi.").

## Çapraz matter bağlamı

Uygulama CLAUDE.md'sinde `Cross-matter context:` bayrağı vardır. `off` iken (varsayılan) A matter'ında çalışan bir skill başka hiçbir `matters/B/` klasörünü **okumaz**. Bayrağın varlık nedeni bu gizlilik güvencesidir; avukatın görevi dolayısıyla öğrendiklerini açığa vurmama yükümlülüğünü (Av. K. m. 36) ve zıt menfaatli taraflardan doğan çatışma riskini (m. 38) destekler.

`on` iken bile yalnız kullanıcı açıkça isterse ("son beş tedarik matter'ında sorumluluk tavanlarını karşılaştır") çapraz okunur; varsayılan yine yalnız aktif matter'dır. Kıyas çıktısında müvekkil adlarını ve müzakere pozisyonlarını anonimleştirmeyi öner.

## Bu skill ne yapmaz

- **Çatışma kontrolü yapmaz** — yalnız yapılıp yapılmadığını sorar ve kaydeder.
- **Saklama politikası uygulamaz** — kapatmak arşivlemektir, silmek değil. Saklama süresi büronun/şirketin politikasıdır (kişisel veride KVKK m. 4/2-d: ilgili mevzuatta öngörülen ya da işlendikleri amaç için gerekli süre kadar muhafaza).
- **Çıktıları yönlendirmez** — esaslı skill nereye yazacağına karar verir; bu skill yalnız hangi klasörün aktif olduğunu söyler.
- **Çapraz bağlamın uygun olup olmadığına karar vermez** — bayrağı okur ve uyar.

---

## /commercial-legal:nda-review

---
name: nda-review
description: >
  Referans: gelen gizlilik sözleşmelerini (NDA) YEŞİL / SARI / KIRMIZI olarak
  hızla ayırır; avukat zamanı yalnız gereken sözleşmeye harcanır. Satış ve iş
  geliştirme ekiplerinin hukuka gelmeden önce kendi başına kullanabilmesi
  için tasarlandı. Türk hukuku tabanı: haksız rekabet ve sır (TTK m. 55),
  cezai şart (TBK m. 179-182, TTK m. 22), yetki ve tahkim (HMK m. 17-18, 412).
  NDA tespit edildiğinde /commercial-legal:review tarafından yüklenir.
user-invocable: false
---

# /nda-review — Gizlilik Sözleşmesi Triajı

Gelen NDA'ların çoğu sorunsuzdur; birkaçında mayın vardır. Bu skill onları bir dakikada ayırır. **Hedef:** YEŞİL bir NDA'ya imzadan başka bir şey gerekmez; SARI bir NDA'da avukatın bir iki belirli noktaya bakması gerekir; KIRMIZI bir NDA kimse vakit kaybetmeden durdurulur. (Profil ve diğer skill'ler GREEN / YELLOW / RED etiketlerini de kullanabilir; anlamları aynıdır.)

## Destination check

Çıktının nereye gideceğine bak. Kullanıcı bir hedef söylediyse (kanal, dağıtım listesi, karşı taraf, "herkes") bunun dar gizlilik çevresinde olup olmadığını sor. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD'deki "privilege" gibi geniş bir belge koruması değildir; şirket geneli kanala, karşı tarafa ya da tedarikçiye giden metin gizliliğini fiilen kaybeder. Hedef çevre dışındaysa (a) yalnız hukuk için tam sürüm, (b) geniş kanal için arındırılmış sürüm ya da (c) ikisini öner; üst başlığı koyup başlığın korumayacağı yere yapıştırılmasına yardım etme. Kanonik kural: eklenti ayarında `## Shared guardrails → Destination check`.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/commercial-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Önce playbook

**Hangi taraftayız?** Karşı taraf ürününüzü değerlendiriyorsa satış tarafı; siz onunkini değerlendiriyorsanız alım tarafı. Karşılıklı NDA'nın da tarafı vardır: kâğıt kimin, değerlendirme hangi yönde? Belli değilse sor. Eşleşen bölümü oku (`### Sales-side playbook` ya da `### Purchasing-side playbook`) ve çıktıda hangisini uyguladığını yaz. Eşleşen taraf `[Not configured]` ise dur: "`/commercial-legal:cold-start-interview --side <side>` çalıştırılmadan bu triaj yapılamaz."

**Triajdan önce** `## Playbook` → eşleşen taraf → `NDA triage positions` bölümünü oku. YEŞİL/SARI/KIRMIZI ölçütleri oradan gelir; bu skill NDA şartları için varsayılan pozisyon taşımaz. Bölüm yoksa ya da NDA'daki bir şart hakkında sessizse sor:

> Playbook'unuz [şart — ör. "residuals kaydı", "gizliliğin sözleşme sonrası süresi", "alıcı olduğunuz tek taraflı NDA", "cezai şart tutarı"] hakkında bir şey söylemiyor. Varsayılan pozisyonunuz ne — ne zaman YEŞİL, ne zaman SARI, ne zaman KIRMIZI? Eklenti ayarına ekleyeyim ki sonraki inceleme tutarlı olsun.

Cevabı eklenti ayarına yaz ve yeni pozisyonla devam et.

## Kapsam kontrolü

NDA'ya özgü hükümlere geçmeden önce belgenin adından fazlasını yapıp yapmadığına bak. "Karşılıklı ticari NDA" şunları saklayabilir: standstill, lisans verilmesi, münhasırlık, çalışan/müşteri ayartmama, rekabet yasağı, fikrî hak devri, önalım hakkı, en çok kayrılan müşteri kaydı, gizlilik dışındaki uyuşmazlıkları da kapsayan geniş tahkim/yetki kaydı, yüksek tutarlı cezai şart, kişisel veri işleme talimatları.

Gizlilik dışında yükümlülük varsa: **NDA analizinden bağımsız olarak otomatik SARI.**

> Bu belge NDA olarak adlandırılmış ama [standstill / lisans / ayartmama / münhasırlık / fikrî hak devri / önalım / en çok kayrılan / geniş tahkim] içeriyor. NDA'dan fazlası. Avukat incelemesine yönlendirin.

NDA kılığındaki hizmet sözleşmesi, ön protokol ya da taahhüt paketini sessizce NDA triajından geçirme.

## Türk hukuku tabanı (kısa)

NDA olmasa da bilgi tamamen korumasız değildir; NDA bu tabanın **üstüne** sözleşmesel yükümlülük ve yaptırım ekler:
- Kendisine emanet edilmiş teklif, hesap, plan gibi iş ürününden yetkisiz yararlanma (TTK m. 55/1-c) ve üretim ve iş sırlarını hukuka aykırı ifşa (TTK m. 55/1-d) haksız rekabettir; tespit, men, eski hâle getirme ve tazminat davaları TTK m. 56'dadır.
- Ticari sır, bankacılık sırrı ya da müşteri sırrını yetkisiz kişilere veren kişi şikâyet üzerine cezalandırılır (TCK m. 239). Kanunda genel bir "ticari sır" tanımı yoktur; NDA'daki tanım uygulamada belirleyicidir.
- Alıcı tarafın işçileri, hizmet ilişkisi süresince ve işverenin haklı menfaati gerektirdiği ölçüde sonrasında da sır saklamakla yükümlüdür (TBK m. 396/4). Bu yükümlülük işverene karşıdır; NDA'yı açıklayan tarafın işçiye doğrudan başvuru hakkı doğurmaz → NDA'da "çalışan ve yardımcılarını aynı yükümlülükle bağlama ve onların ihlalinden sorumluluk" kaydı aranır (yardımcı kişi sorumluluğu: TBK m. 116).
- NDA kanunda şekle bağlı değildir (TBK m. 12/1); ispat için yazılı ve imzalı nüsha tut.

## Triaj

Kova tanımları sabittir; her kovayı dolduran ölçütler playbook'tandır. Her çıktının başına eklenti ayarı `## Outputs` → üst başlığı koy (role göre değişir — `## Who's using this`).

### YEŞİL — imzaya yönlendir

NDA playbook'taki her pozisyonu karşılıyor ve hiçbir şart KIRMIZI tetikleyicisine düşmüyor. Playbook'un genelde kapsadığı kontroller: karşılıklılık, süre, sözleşme sonrası gizlilik süresi, istisnalar, cezai şart, uygulanacak hukuk ve yetki, kısıtlayıcı taahhütler, ücret yükleme. Hepsini eklenti ayarına karşı teyit et.

**YEŞİL, avukatın gözden geçirdiği pozisyon ister.** YEŞİL, avukat incelemesi olmadan imzaya giden tek yoldur; varsayılan ya da eksik pozisyonla verilemez. Profilde avukatın gözden geçirdiği `NDA triage positions` yoksa:

> Profilinizde avukatın gözden geçirdiği NDA pozisyonları olmadan YEŞİL veremem. Ticari avukatınızla `/commercial-legal:cold-start-interview --full` çalıştırın ya da bu NDA'yı avukat incelemesine gönderin. Varsayılana göre YEŞİL vermek, sonraki hukukçu olmayanın güveneceği pozisyonu bir hukukçu olmayanın koyması demektir.

Pozisyon eksikse doğru karar SARI'dır.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

## NDA Triajı: [Karşı taraf] — [Satış / Alım tarafı playbook'u]

YEŞİL — imzaya yönlendir

### Özet
Playbook'a göre kırmızı bayrak yok. Standart süreçle imzaya yönlendirin.

| Kontrol | Durum | Playbook bölümü |
|---|---|---|
| [her kontrol] | geçti | [eklenti ayarı bölümü] |

**Sonraki adım:** [[CLM] standart NDA akışına gönder | [eklenti ayarındaki onaylayıcı]'ya imzaya gönder]
```

### SARI — avukat belirli noktalara baksın

Bir ya da birkaç şart playbook'tan sapıyor ama kesin ret değil, YA DA playbook'un hiç değinmediği bir şart var. Her noktayı ayrı ayrı göster ki onaylayıcı karar verebilsin.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

## NDA Triajı: [Karşı taraf] — [taraf]

SARI — [eklenti ayarındaki onaylayıcı]'ya işaretle

### Özet
- [Tek satırlık mekanik düzeltme, ör. "Madde 6'daki ayartmama kaydını sil"]

### İşaretlenen noktalar
**1. [Konu]** — Madde [X]
   Ne: [tek satır]
   Neden: [hangi playbook pozisyonu ya da "playbook sessiz"]
   **Hukuki risk:** [🔴/🟠/🟡/🟢] | **İş sürtünmesi:** [🔴 Anlaşmayı durdurur / 🟠 Yavaşlatır / 🟡 Kafa karıştırır / 🟢 Görünmez]
   Muhtemel çözüm: [kabul / X'e itiraz / bağlama göre]

### Geri kalanı
| Kontrol | Durum | Playbook bölümü |
|---|---|---|

**Sonraki adım:** İşaretli noktaları [onaylayıcı]'ya sorun; uygun görürse imzaya yönlendirin.
```

### KIRMIZI — dur, önce hukuka danış

Şart playbook'un "asla kabul etme" listesinde ya da yapı ekibin standart duruşuyla bağdaşmıyor (ör. playbook karşılıklı isterken tek taraflı NDA; süreli gizlilik isterken süresiz; "never" listesindeki hukuk ya da yargı yeri).

```markdown
[ÜST BAŞLIK — profil ## Outputs]

## NDA Triajı: [Karşı taraf] — [taraf]

KIRMIZI — göndermeyin, önce hukuka danışın

### Özet
- [ör. "Madde 4 — hukuk incelemesine yönlendirin"]

### Kritik sorunlar
**1. [Konu]** — Madde [X]
   > "[birebir alıntı]"
   Neden sorun: [somut risk; ihlal edilen playbook pozisyonu]
   **Hukuki risk:** [...] | **İş sürtünmesi:** [...]
   Önerilen cevap: [bizim metni kullanalım | şu ifadeyle itiraz | vazgeç]

**Sonraki adım:** Bu triajı [GC ya da eklenti ayarındaki eskalasyon kişisi]'ne gönderin. [CLM]'e ya da onay akışına sokmayın. Karşı tarafa imzalayacağımızı söylemeyin.
```

## Kontrol rehberi

Her kontrolün kovası playbook'tan gelir; bu liste yalnız **neye bakılacağını** ve Türk hukukunun koyduğu sınırları söyler.

**Karşılıklılık.** Tek taraflıysa hemen KIRMIZI deme; sor: (1) Bu ilişkide bilgi veren yalnız siz misiniz? (2) Sınırlı, belirli bir açıklama mı (ör. teknolojinizi üzerinde çalışacak tedarikçiye vermek)? (3) Şirket alımı, işçi ya da yatırımla mı ilgili? (Evetse dur — bu skill yalnız ticari NDA içindir; hukuka yönlendir.) Playbook bu olguya pozisyon almıyorsa SARI ve cevapları onaylayıcıya göster.

**Gizli bilgi tanımı.** Yalnız işaretli mi, açıklanan her şey mi; işaretleme şartı; sözlü açıklamanın yazılı teyit süresi. Tanım dar ve işaretlemeye bağlıysa korunmak istenen bilgi TTK m. 55 tabanına düşer — playbook'a göre değerlendir.

**İstisnalar.** Tipik beş istisna: (1) ihlal dışında kamuya açık olan/olacak bilgi, (2) alıcının zaten sahip olduğu, (3) gizli bilgiye başvurmadan bağımsız geliştirilen, (4) üçüncü kişiden kısıtsız alınan, (5) kanun, mahkeme, savcılık ya da düzenleyici kurum (ör. SPK, BDDK, Rekabet Kurumu, KVKK) kararıyla açıklanması zorunlu olan — hukuken izin verildiği ölçüde açıklayana önceden bildirimle. Hangisinin şart olduğu playbook sorusudur.

**Residuals.** Alıcının yardımsız hafızasında kalan bilgiyi kullanma hakkı. Dar ("unaided memory") ya da geniş (not ve kopyalar dahil) olması playbook'a göre. Geniş residuals, TTK m. 55/1-c,d korumasını sözleşmeyle fiilen bertaraf edebilir → en az SARI.

**Süre ve sonrası.** Sözleşme süresi, sona erme sonrası gizlilik süresi, ticari sırlar için daha uzun koruma. Türk hukukunda süresiz gizlilik yükümlülüğünün sınırı (kişilik hakları, TBK m. 27/1) **tartışmalı — içtihadı kontrol et**; playbook süreli istiyorsa süreyi ve ticari sır istisnasını ayrı yaz.

**Kısıtlayıcı taahhütler.** Çalışan/müşteri ayartmama, rekabet yasağı, münhasırlık.
- Rakipler arasında ayartmama ya da münhasırlık rekabeti kısıtlayıcı anlaşma sayılabilir (4054 m. 4). Rekabet Kurulu'nun işgücü piyasası uygulamasını ezberden söyleme; ara: `tr_kurum_karari_ara(kurum="rekabet", query="işgücü piyasası centilmenlik anlaşması ayartmama")`.
- Bir gerçek kişiyi (ör. alıcının yöneticisi, danışmanı) bağlayan rekabet yasağı işçi için ancak yazılı ve TBK m. 444/2 şartlarıyla geçerlidir → `/employment-legal:hiring-review`.
- Playbook sessizse sor; bu taahhütler yargı çevresine duyarlıdır.

**Cezai şart.** Türk NDA'larında sık görülür. Alacaklı ya ifayı ya cezayı ister; ifa zamanı/yeri için kararlaştırılan cezada ikisini birden isteyebilir (TBK m. 179/1-2). Zarar olmasa da ceza ödenir; zarar cezayı aşarsa aşan kısım için borçlunun kusurunu ispat gerekir (TBK m. 180). Hâkim aşırı cezayı kendiliğinden indirir (TBK m. 182/3), ama **tacir borçlu** aşırılık iddiasıyla indirim isteyemez (TTK m. 22). Tacirler arası NDA'da yüksek tek yönlü ceza → playbook'a göre en az SARI. Tacir aleyhine indirim yasağının sınırı (ekonomik çöküş hâli) **tartışmalı — içtihadı kontrol et**.

**Yargılama giderleri ve avukatlık ücreti.** Kanunda aleyhine hüküm verilen taraf yargılama giderlerini öder; giderler arasında kanuna göre takdir edilen vekâlet ücreti vardır (HMK m. 323/1-ğ, m. 326/1). Gerçek avukatlık ücretinin sözleşmeyle karşı tarafa yüklenmesi ve tek yönlü yükleme kaydının talep edilebilirliği **tartışmalı — içtihadı kontrol et**. Karşılıklı mı, tek yönlü mü, playbook'a göre değerlendir.

**İhtiyati tedbir.** "Teminatsız tedbir istenebilir" kaydı mahkemeyi bağlamaz: tedbir isteyen kural olarak teminat gösterir; mahkeme gerekçe göstererek teminat almayabilir (HMK m. 389, m. 392/1). Kaydı silmek gerekmez, ama ona güvenerek hesap yapma.

**İade/imha, yedek ve yasal saklama.** İade/imha kaydında standart yedek ve arşiv sistemleri istisnası var mı? Ayrıca tacir ticari mektuplarını (bir ticari işe ilişkin tüm yazışmalar) on yıl saklamakla yükümlüdür (TTK m. 82/1-b,c, m. 82/2, m. 82/5) → "kanunen saklanması zorunlu kayıtlar gizlilik yükümlülüğü sürmek kaydıyla saklanabilir" istisnası yoksa ekle. Playbook bu istisnayı zorunlu tutuyor mu, bak.

**Kişisel veri.** NDA kapsamında kişisel veri aktarılacaksa NDA bir veri işleme sözleşmesi değildir → `/privacy-legal:dpa-review` öner; yurt dışı aktarım varsa KVKK m. 9 orada incelenir.

**Uygulanacak hukuk, yetki, tahkim.** `## Playbook` → `Governing law and venue`. Türk hukukunda yetki sözleşmesini yalnız tacirler ya da kamu tüzel kişileri yapabilir; yazılı olmalı, hukuki ilişki belirli/belirlenebilir olmalı ve mahkeme gösterilmelidir (HMK m. 17-18). Tahkim kaydı yazılı olmalıdır (HMK m. 412/3; yabancılık unsuru varsa MTK m. 4). Gizlilik ihlalinden doğan para alacağı ticari davaysa dava öncesi arabuluculuk dava şartıdır (TTK m. 5/A). Yabancı hukuk ya da yabancı mahkeme seçilmişse (MÖHUK m. 24, m. 47) → `/commercial-legal:governing-law-review`.

**İmza.** Güvenli elektronik imza elle atılan imzayla aynı sonucu doğurur (5070 m. 5/1); platform tıklamalı "basit" e-imza güvenli e-imza değildir. NDA şekle bağlı olmadığından geçerlilik sorunu çıkmaz, ispat sorunu çıkabilir → imza yöntemini profildeki tercihe göre not et.

## Redline inceliği

Redline bir müzakere belgesidir, yeniden yazım değildir. En küçük düzeltme: kelime → ifade → alt bent → cümle → ancak gerekirse tüm madde. ("on iki (12)" → "yirmi dört (24)"). Tüm maddeyi değiştirdiysen ileti notunda söyle: "8.2'yi değişiklikler kapsamlı olduğu için işaretlemek yerine yeniden yazdık; farkı birlikte geçebiliriz." Şüphede, daha küçük.

**Yargı çevresi varsayımı:** triaj eklenti ayarındaki hukuk ve kısıtlayıcı taahhüt pozisyonlarını uygular; NDA profilin dışında bir yargı çevresine bağlıysa çıktıda işaretle, triajın olduğu gibi aktarılamayacağını yaz; yabancı kural ezberden yazılmaz (`/commercial-legal:governing-law-review`).

## Çıktı kuralları

- **Karmaşıklık filtresi:** Bir sorunu çözmek yeni ifade yazmayı, maddeyi yeniden kurmayı ya da esaslı yeni hüküm eklemeyi gerektiriyorsa deneme; yaz: "Madde [X] — hukuk incelemesine yönlendirin." Özette yalnız mekanik işlemler (sil, çıkar, kelime/ifade değiştir).
- **Temiz NDA kuralı:** Hiç bayrak yoksa özet yalnız şunu der: "Kırmızı bayrak yok. Standart süreçle imzaya yönlendirin." Temiz NDA için uzun rapor yazma.

## Karşı taraf bağlamı ve CLM

**Büyük kurumsal karşı taraf** NDA'sını genelde müzakere etmez: KIRMIZI gerçekten anlaşma bozucu mu, "bizim formdan farklı" mı? İlişki önemliyse onların metnini kabul kararını eskalasyona götür, kendin verme. **Girişimler** genelde bizim metni kabul eder; en hızlı yol çoğu zaman "bizimkini kullanalım"dır. **CLM** bağlıysa: YEŞİL → standart NDA akışında kayıt öner; SARI → işaretli noktaları not olarak ekleyip öner; KIRMIZI → kayıt açma, sonraki adıma avukat karar verir.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6102", madde_no=["5/A","22","55","56","82"])
tr_mevzuat_madde_getir(number="6098", madde_no=["12","27","116","179","180","182","396","444"])
tr_mevzuat_madde_getir(number="6100", madde_no=["17","18","323","326","389","392","412"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="gizlilik sözleşmesi cezai şart tacir indirim", date_from="2020-01-01")
tr_kurum_karari_ara(kurum="rekabet", query="işgücü piyasası centilmenlik anlaşması ayartmama")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Atıf etiketi: `[ArthurLegal TR — 6102 m. X — GG.AA.YYYY]`; ezberden gelen için `[model bilgisi — doğrula]`.

## Sonuç doğuran işlem kapısı (imza)

YEŞİL'den imzaya geçmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> Bu adımın hukuki sonucu var: NDA'yı imzalamak şirketi bağlar; cezai şart varsa ihlalde zarar ispatı gerekmeden ödenir. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz bir sayfalık özet: karşı taraf, NDA yönü (karşılıklı / tek taraflı), yapılan playbook kontrolleri, playbook'un kapsamadığı noktalar, olduğu gibi imzalanırsa ne ters gidebilir ve avukata sorulacak üç soru. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan bu kapıdan geçme.

## Kapanış eylemi

`## NDA triage preferences` → `closing_action` oku. Tanımlıysa her çıktının sonuna aynen ekle (ör. "Bu analizi ve NDA'yı imzadan önce son teyit için hukuka gönderin." / "Standart NDA akışıyla [CLM]'e gönderin." / "Bu çıktıyı ve NDA'yı sözleşme yöneticinize iletin."). Tanımlı değilse ekle: "NDA'yı standart onay sürecinizden geçirin." Cold-start görüşmesi bunu sorar: "NDA triajını bitiren kişi çıktıyla ne yapsın?"

Ardından profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu triaja göre uyarla (redline gönder, eskalasyon, ek olgu iste, bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Müzakere etmez; ayırır.
- NDA yazmaz; cevap "bizim metni kullanalım" ise form [CLM ya da belge sistemi]nden alınır.
- SARI noktalarda karar vermez; insana gösterir.
- NDA şartları hakkında kendi pozisyonunu koymaz; pozisyonlar eklenti ayarındadır. Türk hukukunun sınırlarını ise her seferinde araçtan çeker.

---

## /commercial-legal:renewal-tracker

---
name: renewal-tracker
description: >
  Fesih bildirimi son günü yaklaşan sözleşmeleri gösterir ve bildirim penceresi
  kapanmadan uyarır; tutulan yenileme kaydından çalışır. Son günü Türk hukukuna göre
  hesaplar (TBK m. 92-93 süre ve tatil kuralı, 2429 s. Kanun genel tatilleri), tacirler
  arası ihbar şeklini (TTK m. 18/3) ve tebliğ süresini tampona katar, tüketici
  aboneliklerinde otomatik uzama yasağını (6502 m. 52) işaretler. Kullanıcı "yakında ne
  yenileniyor", "hangi yenilemeler geldi", "fesih süresini kaçırdık mı", "bunu yenileme
  takibine ekle" dediğinde ya da zamanlanmış çalışmada kullan. saas-msa-review'dan
  devir alır.
argument-hint: "[--days N pencereyi değiştirir | --missed kaçan pencereler]"
---

# /renewal-tracker

Neyin ne zaman yenilendiğini ve en geç ne zaman fesih bildirimi **gönderilmesi** gerektiğini gösterir.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-register.yaml` dosyasını oku (ayar klasörü — eklenti güncellemelerinden etkilenmez).
2. **Varsayılan:** Mod 2 — önümüzdeki 90 gün, aciliyete göre yarı açık aralıklarla: 🔴 0–13 gün, 🟠 14–44 gün, 🟡 45–89 gün. 14., 45. ve 90. gün sınırdır; her son gün tek bir banda düşer.
3. **`--days N`:** pencereyi değiştir. **`--missed`:** Mod 4 — kayıtlı fesih olmadan geçen son günler.
4. **Kayıt boşsa ve CLM bağlıysa:** Mod 3'ü öner (toplu yükleme).
5. Çıktıya önerilen eylemleri ekle: kime sorulacak (kayıttaki iş sahibi), hangilerinde yenileme fiyatı sınırsız/endekssiz (pencere kapanmadan pazarlık gücü).

## Matter bağlamı

`## Matter workspaces` → `Enabled` `✗` ise atla. Açıksa ve aktif matter varsa yalnız o matter'ın kayıtlarını göster (`matter` alanı); `Cross-matter context` `on` değilse diğer müvekkillerin satırlarını raporlama.

## Kayıt

`renewal-register.yaml` — **anahtarlar İngilizce kalır** (saas-msa-review, vendor-agreement-review ve renewal-watcher bu adları okur); değerler Türkçe olabilir:

```yaml
- counterparty: "ABC Yazılım A.Ş."
  agreement: "ABC Platform Abonelik Sözleşmesi"
  signed_date: 2025-06-15
  initial_term_end: 2026-06-15
  current_term_end: 2026-06-15     # her otomatik yenilemede ileri alınır; cancel_by_* bundan hesaplanır
  renewal_mechanism: "yıllık otomatik yenileme"
  notice_period_days: 60
  notice_method: "KEP"             # noter / taahhütlü mektup / telgraf / KEP / e-posta / portal / sözleşme m. X
  transit_buffer_days: 1           # aşağıdaki tabloya göre ya da sözleşmedeki tebliğ kuralına göre
  cancel_by_calendar: 2026-04-16   # current_term_end eksi notice_period_days
  cancel_by_effective: 2026-04-16  # gerekiyorsa son iş gününe GERİ çekilmiş
  send_by_effective: 2026-04-15    # cancel_by_effective eksi transit_buffer_days — bildirimin GÖNDERİLECEĞİ son gün
  cancel_by_roll_note: ""          # ör. "Pazar 2026-11-01'den geri çekildi; sözleşmedeki iş günü tanımıyla teyit et"
  cancel_by_provenance: "[model hesabı — fesih bildirimi klozuyla teyit et]"
  price_on_renewal: "güncel liste fiyatı (sınırsız)"   # ya da "TÜFE endeksli" vb.
  annual_value: 480000
  currency: "TRY"                  # isteğe bağlı; yoksa notes'a yaz
  business_owner: "ayse@sirket.com"
  clm_id: "IC-12345"               # bağlıysa
  docusign_envelope: "abc-123"     # bağlıysa
  status: "active"                 # active | cancelled | renewed | lapsed
  matter: "abc-tedarik-2026"       # isteğe bağlı; yalnız matter çalışma alanları açıksa
  notes: "Fiyat sınırsız — yenilemeden önce gözden geçir. Alternatif: X, Y."
```

**Uyarıyı `send_by_effective`'ten ver, `cancel_by_effective`'ten değil.** Noter kanalıyla 60 günlük pencere fiilen 50 küsur gündür; "ulaşma" tarihine göre uyaran kayıt son günü kaçırır. Mod 2'nin aciliyet sütunu `send_by_effective`'i gösterir; ayrıntı sütunu `cancel_by_effective`, `notice_method` ve `transit_buffer_days`'i gösterir ki okuyan tamponu sorgulayabilsin.

**Yuvarlanan yenilemeler.** `initial_term_end` kayıt içindir; `cancel_by_*` daima `current_term_end`'den hesaplanır. Pencere bildirimsiz geçip yenileme gerçekleşince sor:

> Bu sözleşme [tarih]'te otomatik yenilendi. Kaydı güncelleyelim: yeni `current_term_end` [tarih + yenileme süresi], yeni `cancel_by_effective` [hesap], yeni `send_by_effective` [hesap]. Onaylıyor musunuz?

## Son gün hesabı — Türk hukuku

Kayıttaki son gün, bildirimin hüküm doğurduğu **son iş günüdür**, takvim günü değil. Hafta sonuna ya da bayrama düşen tarih son günü kaçırmanın en yaygın yoludur; kayıt bunu bir kez, girişte yakalar.

1. **Takvim tarihini hesapla.** `cancel_by_calendar = current_term_end − notice_period_days` (ya da klozun söylediği). Süre ay olarak belirlenmişse ay hesabı TBK m. 92 (bent 3) mantığıyla yapılır (son ayın karşılık gelen günü; o gün yoksa ayın son günü). TBK m. 92 ileriye doğru sayım için yazılmıştır; "bitişten iki ay önce" gibi geriye sayımda aynı mantığı uygula ve hesabı `cancel_by_roll_note`'a yaz.
2. **Geri çek — asla ileri alma.** Sözleşme Türk hukukuna tabiyse tatil takvimi: hafta tatili Pazar (2429 s. Kanun m. 3); genel tatiller 1 Ocak, 23 Nisan, 1 Mayıs, 19 Mayıs, 15 Temmuz, 30 Ağustos, Ramazan Bayramı (arefe 13.00'ten itibaren 3,5 gün), Kurban Bayramı (arefe 13.00'ten itibaren 4,5 gün) (m. 2) ve 29 Ekim (28 Ekim 13.00'ten itibaren, m. 1). Dini bayram tarihleri her yıl değişir — o yılın takvimini teyit et. Arefe yarım gününü ve Cumartesi'yi de iş günü sayma (Cumartesi genel tatil değildir ama hafta tatili en geç Cumartesi 13.00'te başlar, m. 3; Cumartesi'nin TBK m. 93 anlamında "tatil" sayılıp sayılmadığı **tartışmalı**). Kamu idari izin günlerinde noterin ve postanın çalışıp çalışmadığını ayrıca teyit et.
3. **TBK m. 93'e güvenme.** Kanuna göre ifa zamanı ya da sürenin son günü tatile rastlarsa izleyen ilk iş gününe geçer; aksine anlaşma geçerlidir (TBK m. 93). Kayıt bu ileri kaymayı **kullanmaz**: kuralın bildirim süresine uygulanması klozun ifadesine bağlıdır ve sözleşme bunu dışlamış olabilir. Geri çekilmiş tarih her durumda güvenlidir.
4. **Sözleşmenin kendi gün kuralını kontrol et.** "İş günü", "tebliğ edilmiş sayılır", "saat 17.00'ye kadar", bildirim adresleri ve kanal klozu varsa o kontrol eder. Varsayılan geri çekme ile sözleşme kuralı arasındaki farkı işaretle.
5. **İki tarihi de yaz.** `cancel_by_calendar` ham hesap; `cancel_by_effective` son iş günü; `cancel_by_roll_note` farkın nedeni. Her hesaplanan `cancel_by_effective` `cancel_by_provenance: "[model hesabı — fesih bildirimi klozuyla teyit et]"` taşır; doğrulama bayrağı tarihle birlikte gider.
6. **Uyarıyı etkin tarihten ver.** Bantlar `send_by_effective`'e göre hesaplanır; geri çekme olduysa ayrıntı sütununda `cancel_by_calendar` ve `cancel_by_roll_note` görünür.

**Yabancı hukuka tabi sözleşme:** o ülkenin tatil takvimini yerel kaynaktan teyit et (ArthurLegal araçları tatil takvimi vermez); bildirim ve süre kuralı için ilgili önek (ör. `uk_search_legislation`, `de_gesetz_ara`, `eu_search_eu_law`) ya da `/commercial-legal:governing-law-review`. Takvim belirlenemiyorsa: "Uygulanacak hukuk [X] — geri çekme yer tutucu olarak Türkiye tatilleriyle yapıldı; [ülke] takvimiyle teyit edin."

Mod 2'de haftanın günü ve uyarı olmadan basılan `cancel_by: 2026-11-01` (Pazar) sessizce yanlış bir son gündür.

## Bildirim şekli ve tampon

Tacirler arasında temerrüde düşürme, fesih ve dönme ihbarları noter, taahhütlü mektup, telgraf ya da güvenli elektronik imzalı KEP ile yapılır (TTK m. 18/3). Bu şeklin geçerlilik şartı mı ispat aracı mı olduğu **tartışmalı — içtihadı kontrol et** (`tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H11", query="TTK 18/3 ihbar şekli fesih")`; dönen kararın künyesini birebir kullan). Sözleşme "e-posta yeterli" diyorsa bile karşı taraf tacirse KEP ya da noter öner.

| `notice_method` | Önerilen `transit_buffer_days` | Neden |
|---|---|---|
| KEP | 1 | Anlık iletim; teslim kaydını almak için bir gün pay |
| Noter ihtarnamesi (karşı taraf şirket) | ≥ 7 | Noter tebligatı Tebligat Kanunu'na göre yapılır (m. 1); özel hukuk tüzel kişilerine elektronik tebligat zorunludur ve adrese ulaştığı tarihi izleyen beşinci günün sonunda yapılmış sayılır (m. 7/a); noter işlem süresi eklenir |
| Taahhütlü mektup (yurt içi) | 5–7 | Posta süresi ve teslim belirsizliği |
| Yurt dışı (kurye / uluslararası taahhütlü) | ≥ 10 | Ya da sözleşmedeki tebliğ kuralı |
| E-posta / portal | 0 | Ancak tacirler arasında şekil riski — notlara yaz |

Bildirimin "ulaşma" tarihinde mi, tebliğin "yapılmış sayıldığı" tarihte mi süreyi karşıladığı sözleşmenin diline bağlıdır; belirsizse ihtiyatlı olanı (geç tarihi) esas al.

## Otomatik yenileme ve belirsiz süreye dönüşme

- **Ticari (B2B):** Otomatik yenileme sözleşme serbestisi içindedir. Ancak karşı tarafın standart metnine gömülü yenileme klozu genel işlem koşuluysa: karşı tarafa açıkça bilgi verilip kabul edilmedikçe yazılmamış sayılır (TBK m. 21), dürüstlük kuralına aykırı aleyhe hüküm konulamaz (m. 25). Kaçırılan pencerede bu bir pazarlık aracıdır, güvence değil.
- **Tüketiciye satış (B2C abonelik):** tüketici, ticari veya mesleki olmayan amaçlarla hareket eden kişidir (6502 m. 3/1-k). Belirli süreli abonelik sözleşmesine sözleşmenin kendiliğinden uzayacağına ilişkin hüküm konulamaz; uzatma ancak tüketicinin talebi ya da onayıyla olur (m. 52/3). Belirsiz süreli ya da bir yıldan uzun belirli süreli abonelikte tüketici gerekçesiz ve cezai şartsız her zaman feshedebilir; bildirim kâğıt üzerinde ya da kalıcı veri saklayıcısıyla yeterlidir (m. 52/4). Satış tarafı B2C kayıtlarında `renewal_mechanism`'e "otomatik uzama yasak — onay gerekir" yaz. Yönetmeliğin güncel metni: `tr_mevzuat_ara(query="Abonelik Sözleşmeleri Yönetmeliği", types=["YONETMELIK"])`.
- **Örtülü sürdürme:** süre bitip taraflar ilişkiyi sürdürürse sözleşme belirsiz süreliye dönüşebilir — kira (TBK m. 327/2) ve acentelik (TTK m. 121/2) için açık hüküm var; acentelikte belirsiz süreli sözleşme üç ay önceden ihbarla feshedilir (m. 121/1). **TBK'da belirsiz süreli sürekli sözleşmelerin olağan feshine ilişkin tek bir genel madde yoktur;** sözleşmede fesih hükmü yoksa süre ve usul **tartışmalı — içtihadı kontrol et**: `tr_ictihat_semantik_ara(query="belirsiz süreli sürekli borç ilişkisinin olağan feshi makul bildirim süresi")`. Böyle kayıtlarda `renewal_mechanism: "belirsiz süreli — fesih süresi teyitsiz"` yaz.

## Modlar

### Mod 1 — Yenileme ekle (incelemeden devir)

saas-msa-review ya da vendor-agreement-review bir yenileme klozu bulunca kaydı devreder. Kayda ekle ve yukarıdaki hesabı yap. Karşı tarafın kaydı zaten varsa sor: yenilenmiş sözleşme mi (değiştir), ek sözleşme mi (ekle)?

### Mod 2 — Yaklaşanlar

Varsayılan 90 gün. Bantlar `send_by_effective − bugün` ile hesaplanır:
- 🔴 **0–13 gün** (bugün dahil) · 🟠 **14–44 gün** · 🟡 **45–89 gün** · 90+ yalnız `--days` ile.

```markdown
## Yenilemeler — önümüzdeki 90 gün

### 🔴 Gönderim son günü 0–13 gün içinde

| Karşı taraf | Gönder (son) | Fesih son günü | Kanal / tampon | Yenileme | Yıllık bedel | Sorumlu | Not |
|---|---|---|---|---|---|---|---|
| [ad] | **[tarih, gün adı]** | [tarih] | [KEP / 1] | [tarih] | [tutar + para birimi] | [e-posta] | [geri çekme notu] |

### 🟠 14–44 gün
[aynı tablo]

### 🟡 45–89 gün
[aynı tablo]

---

**Önerilen eylemler:**
- [ ] [Karşı taraf] — [iş sahibi]'ne sor: devam mı?
- [ ] [Karşı taraf] — yenileme fiyatı sınırsız; pazarlık gücü kaybolmadan alternatif teklif al
- [ ] [Karşı taraf] — karşı taraf tacir, kayıtta kanal e-posta: KEP ya da noterle gönder
```

Pencerede ~10'dan fazla kayıt varsa ya da kullanıcı isterse: profilde `## Outputs → Dashboard offer for data-heavy outputs` varsa ona göre pano öner — banda göre sayılar, son gün zaman çizelgesi ve sıralanabilir kayıt.

### Mod 3 — CLM / e-imza taramasıyla kaydı doldur

MCP'ler bağlıysa ve kayıt boş ya da eskiyse (tek seferlik toplu yükleme; sonra giriş inceleme anında olur): (1) CLM'de durumu "aktif" ve yenileme tarihi dolu sözleşmeleri sorgula; (2) e-imza aracında son 24 ayın tamamlanmış zarflarında "abonelik", "yenileme", "otomatik" geçenleri sorgula; (3) her biri için yenileme mekaniğini çıkar, yukarıdaki hesabı yap, kayda ekle; (4) meta veriden tarihi belirlenemeyenleri işaretle — sözleşmeyi bir insanın okuması gerekir.

### Mod 4 — Kaçan pencereler

```markdown
## Kaçan fesih pencereleri

Aşağıdakilerin fesih bildirimi son günü geçti ve kayıtlı fesih yok:

| Karşı taraf | Son gün | Yenileme tarihi | Durum |
|---|---|---|---|
| [ad] | [tarih] | [tarih] | [tarih]'te otomatik yenilenecek |

**Seçenekler:**
- Geç fesih için müzakere (nadiren tutar, sormaya değer)
- Yenilemeyi kabul et, gelecek yılın son gününü şimdiden işaretle
- Sözleşmedeki diğer fesih haklarını kontrol et (sebepsiz fesih, haklı sebeple fesih)
- Yenileme klozu karşı tarafın genel işlem koşuluysa TBK m. 21/25 değerlendirmesi — avukatla
- B2C abonelikte tüketici otomatik uzamaya bağlı tutulamaz (6502 m. 52/3)
```

## Kapı: yenilemeyi kabul ya da fesih

Tarihi izlemek araştırmadır; **harekete geçmek** — fesih bildirimi göndermek, otomatik yenilemenin işlemesine izin vermek, yenileme formunu imzalamak — hukuki sonuçlu adımdır.

Bu adımdan önce profilde `## Who's using this` → Role'e bak. Avukat değilse:

> Bu adımın hukuki sonucu var (ya yeni bir döneme bağlanıyorsunuz ya da ilişkiyi sona erdiriyorsunuz). Bir avukatla görüştünüz mü? Evetse devam edelim. Hayırsa götürmeniz için kısa brif:
>
> [Tek sayfa: karşı taraf, mevcut dönem sonu ve gönderim son günü, kanal ve tampon, yenileme fiyat mekaniği, hiçbir şey yapmazsak ne olur, alternatif tedarikçiler, pencere kapanmadan avukata sorulacak üç soru.]
>
> Avukat bulmak için bulunduğunuz ilin barosuna başvurabilirsiniz.

Açık bir "evet" olmadan bu kapıyı geçme.

## renewal-watcher ajanıyla bağlantı

renewal-watcher ajanı bu skill'i zamanlanmış olarak (varsayılan haftalık) çalıştırır ve Mod 2 raporunu profildeki `## House style` → `**Renewal alerts:**` kanalına (yoksa `**Where work product goes:**`) gönderir.

## Bu skill ne yapmaz

- Sözleşme feshetmez ve yenileyip yenilememeye karar vermez; son günü ve iş sahibini gösterir.
- Yenileme tarihini bulmak için sözleşme okumaz — bu inceleme anında olur; kayıtta tarihi olmayan satır elle eklenmiştir ve doldurulmalıdır.
- Fesih bildirimini göndermez ya da noter/KEP işlemi yapmaz.

---

## /commercial-legal:review

---
name: review
description: >
  Gelen ticari sözleşmeyi (hizmet/tedarikçi sözleşmesi, gizlilik sözleşmesi,
  SaaS/abonelik) playbook'a göre inceler. Önce belge yapısını başlıklardan
  okur, doğru inceleme skill'ine (vendor-agreement-review, nda-review,
  saas-msa-review) yönlendirir, tarafların tacir olup olmadığını ve seçilen
  hukuku tarar, çıktıyı tek notta birleştirir. "Bu sözleşmeyi incele",
  "çerçeve sözleşmeye bak", "bu NDA uygun mu", "SaaS sözleşmesini kontrol et"
  denince ya da gelen bir sözleşme eklendiğinde kullan.
argument-hint: '[dosya yolu | Drive bağlantısı | [CLM ID] | metni yapıştırın]'
---

# /review — Sözleşme İncelemesi (yönlendirici)

Gelen sözleşmeyi `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`'deki playbook'a göre inceler. Hangi skill'in çalışacağına belge başlıklarından karar verir; `confirm_routing` açıksa önce kullanıcıya teyit ettirir. Esas Türk hukukudur; yabancı hukuk ya da yabancı yargı yeri seçilmişse tespitler o hukuka taşınmaz, `/commercial-legal:governing-law-review`e yönlendirilir.

## Adımlar

1. **Eklenti ayarını ve `company-profile.md`'i yükle.** Yer tutucu varsa dur: "Önce `/commercial-legal:cold-start-interview` çalıştırın — playbook'unuzu öğrenmeden ona göre inceleyemem." `## Review preferences` → `confirm_routing` oku; alan yoksa `true` say.

2. **Sözleşmeyi al:** dosya, Drive bağlantısı, [CLM ID] ya da yapıştırılmış metin. Yoksa iste.

3. **Önce başlıkları oku.** Gövdeye geçmeden çıkar: ana sözleşmenin başlığı; tüm ek, ek protokol, sipariş formu, teknik şartname, iş emri başlıkları. Yönlendirme sinyali budur — 40 sayfalık çerçeve sözleşmede "gizli" kelimesinin sık geçmesi onu NDA yapmaz.

4. **Skill'i belge yapısına göre seç.**

   | Başlıkta geçen | Skill |
   |---|---|
   | Gizlilik Sözleşmesi, Gizlilik Taahhütnamesi, NDA, Confidentiality Agreement (*ana* sözleşme olarak) | **nda-review** |
   | Hizmet Sözleşmesi, Çerçeve Sözleşme, Master Services Agreement, Danışmanlık, Proje Sözleşmesi, İş Emri / Statement of Work, Satın Alma Sözleşmesi | **vendor-agreement-review** |
   | Abonelik, SaaS, Bulut Hizmeti, Kullanım Koşulları, otomatik yenilemeli Sipariş Formu, yinelenen bedelli Yazılım Lisansı | **saas-msa-review** (vendor-agreement-review'un üstüne katman) |
   | Kişisel Verilerin İşlenmesine İlişkin Ek Protokol, Veri İşleme Sözleşmesi, DPA (ek ya da ayrı) | vendor-agreement-review'da veri koruma başlığında işaretle + `/privacy-legal:dpa-review` öner |
   | Hizmet Seviyesi Sözleşmesi (HSS), SLA (ek olarak) | saas-msa-review → HSS bölümü |
   | NDA ama bağlam işçi, yatırım ya da şirket alımı | Bu eklentinin işi değil → `/employment-legal:hiring-review` ya da `/corporate-legal:` skill'leri; avukata |

   Birden çok skill uygulanabilir: çerçeve sözleşme + KVKK eki → vendor-agreement-review (veri eki işaretli); abonelik + sipariş formu + HSS eki → saas-msa-review (üçünü kapsar); çerçeve sözleşme + otomatik yenilemeli sipariş formu → vendor-agreement-review + saas-msa-review katmanı. Başlıklar yetmiyorsa (yalnız "Sözleşme", ek listesi yok) gövdenin ilk iki sayfasını oku, karar ver, dur.

5. **Ön tarama (yönlendirmeyle birlikte, her sözleşmede):**
   - **Taraflar tacir mi?** Bir ticari işletmeyi ilgilendiren işlem ticari iştir (TTK m. 3); her iki tarafın ticari işletmesiyle ilgili uyuşmazlık ticari davadır (TTK m. 4/1). Sonuçları: fesih ve temerrüt bildirimlerinin şekli (TTK m. 18/3), cezai şartın indirilememesi (TTK m. 22), para alacaklarında dava şartı arabuluculuk (TTK m. 5/A). İnceleme skill'leri bunları kullanır; tacir sıfatını notun başına yaz.
   - **Karşı taraf tüketici mi?** Ticari veya mesleki olmayan amaçla hareket eden kişi tüketicidir (6502 m. 3/1-k). O zaman playbook yetmez: haksız şartlar kesin hükümsüzdür (6502 m. 5/2), abonelikte otomatik uzatma ve fesih kuralları emredicidir (6502 m. 52/3-4) → avukata, ayrıca işaretle.
   - **Uygulanacak hukuk ve uyuşmazlık çözümü.** Türk hukuku dışında bir hukuk, yabancı mahkeme ya da yurt dışında tahkim seçilmişse ya da yetki kaydı tek tarafa seçim hakkı veriyorsa → hukuk seçimi MÖHUK m. 24/1'e tabidir; yabancılık unsuru olmayan saf iç sözleşmede yabancı hukuk seçiminin geçerliliği **tartışmalı — içtihadı kontrol et**. Bu incelemenin Türk hukuku tespitlerinin o hukuka geçmediğini nota yaz ve `/commercial-legal:governing-law-review` öner.

6. **Yönlendirmeyi teyit et** (`confirm_routing: true` ya da alan yoksa):

   ```
   Bunu şöyle inceleyeceğim: [sözleşme türü/türleri]. Taraflar: [tacir–tacir / tüketici var].

   Tespit edilen belgeler:
   - [Ana sözleşme başlığı] → [skill]
   - [Ek 1 başlığı] → [nasıl ele alınacak]
   - [Ek 2 başlığı] → [nasıl ele alınacak]

   Doğru mu? (evet / hayır — ya da neyi yanlış anladığımı söyleyin)
   ```

   Teyit bekle; kullanıcı düzeltirse onun talimatıyla devam et. `confirm_routing: false` ise sessizce devam et, yönlendirme kararını notun en üstüne yaz.

7. **Skill(ler)i çalıştır.** Her birinin akışını eksiksiz izle. Birden çok skill varsa sırayla çalıştır ve **tek not** üret; ayrı notlar çıkarma.

8. **Eskalasyon:** Bir bulgu inceleyenin yetkisini aşıyorsa (`## Escalation` matrisi) `/commercial-legal:escalation-flagger` ile yönlendir ve talebi taslakla.

9. **Takip öner:**
   - İş birimine özet → `/commercial-legal:stakeholder-summary`
   - İzlenen değişikliklerle redline .docx
   - [CLM] kaydı (bağlıysa)
   - Otomatik yenileme bulunduysa yenileme kaydı → `/commercial-legal:renewal-tracker`
   - Yabancı hukuk, yabancı yargı yeri ya da asimetrik yetki/tahkim → `/commercial-legal:governing-law-review` (yabancı kural araçla çekilir: İngiltere `uk_search_legislation`, Almanya `de_gesetz_ara`, AB `eu_search_eu_law`; listede olmayan ülke için "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al")
   - Damga vergisi sorusu → `/tax-legal` skill'leri (oran ve tutar bu eklentide yazılmaz)

## confirm_routing ayarı

`~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## Review preferences`:

```markdown
## Review preferences

confirm_routing: true   # Set to false to skip routing confirmation and proceed automatically
```

Cold-start görüşmesi bu tercihi sorar. Varsayılan `true`; güven oluştukça kullanıcı `false` yapabilir.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6102", madde_no=["3","4","5/A","18","22"])
tr_mevzuat_madde_getir(number="6502", madde_no=["3","5","52"])
```

Atıf etiketi: `[ArthurLegal TR — 6102 m. X — GG.AA.YYYY]`; ezberden gelen için `[model bilgisi — doğrula]`; kullanıcıdan gelen için `[kullanıcı verdi]`. Çekilemeyen madde: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".

## Örnekler

```
/commercial-legal:review hizmet-cerceve-sozlesmesi.pdf
/commercial-legal:review https://drive.google.com/file/d/ABC123
/commercial-legal:review
[sözleşme metnini yapıştırın]
```

## Çıktı

İlgili skill'in biçiminde tam inceleme notu. En üstte: yönlendirme kararı, uygulanan playbook tarafı (satış / alım), taraf sıfatı (tacir / tüketici), seçilen hukuk. Sapma sapma bulgu, somut redline metni, adıyla onaylayıcı. Not, `## House style` → iş ürününün gideceği yere kaydedilir.

---

## /commercial-legal:review-proposals

---
name: review-proposals
description: >
  playbook-monitor ajanının bekleyen playbook güncelleme önerilerini tek tek gözden
  geçirir; avukat kabul, ret, düzenleme ya da erteleme seçer ve onaylanan değişiklik
  profile yazılır. playbook-monitor öneri çıkardığında, kullanıcı "playbook önerilerini
  gözden geçir", "bekleyen playbook güncellemeleri ne" dediğinde ya da sapmaya dayalı
  değişiklikleri adım adım görmek istediğinde kullan.
argument-hint: "[argüman gerekmez — bekleyen öneri dosyasından çalışır]"
---

# /review-proposals

`~/.claude/plugins/config/claude-for-legal/commercial-legal/playbook-proposals.md` dosyasındaki önerileri tek tek gösterir ve onaylananları `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` dosyasına uygular.

## Talimat

1. **playbook-monitor ajanının Adım 5'ini (gözden geçirme ve onay akışı) yükle ve çalıştır.**
2. **Öneri dosyası yoksa ya da boşsa:** "Bekleyen öneri yok. Playbook güncel." de ve dur.
3. **Önerileri tek tek göster.** Her biri için tam öneri bloğunu ve dört seçeneği ver: **[K] Kabul**, **[R] Ret**, **[D] Düzenle**, **[E] Ertele**.
4. **Kabul ya da Düzenle:** yazmadan önce profildeki tam farkı göster (`- eski` / `+ yeni`); yalnız avukat açıkça onaylarsa yaz. Yalnız ilgili tarafın (`### Sales-side playbook` / `### Purchasing-side playbook`) ilgili alt bölümünü değiştir; başlık ve anahtar adlarını çevirme.
5. **Ret ya da Ertele:** kararı (varsa gerekçesiyle) `playbook-monitor-log.yaml`'a işle; profili değiştirme. Reddedilen öneri, ret tarihinden sonra yeni bir desen oluşmadıkça yeniden önerilmez.
6. **Hukuki sınır kontrolü:** Önerilen yeni duruş emredici bir hükme takılıyorsa kabulden önce söyle ve maddeyi `tr_mevzuat_madde_getir` ile çekip göster. Örnekler: tavanın kast ve ağır kusuru da kapsaması (önceden yapılan bu anlaşma kesin hükümsüzdür, TBK m. 115/1); borçlu olduğumuz yüksek cezai şartı "kabul edilebilir geri çekilme" yapmak (tacir borçlu aşırılık iddiasıyla indirim isteyemez, TTK m. 22); tüketici aboneliğinde otomatik uzama (6502 m. 52/3). Uygulamada sık kabul edilmiş olması, duruşu hukuken geçerli kılmaz.
7. **Hepsi bitince:** neyin değiştiğinin özetini göster, sonra öneri dosyasını `playbook-proposals-[YYYYMMDD].md` adıyla arşivle.

```
/commercial-legal:review-proposals
(playbook-monitor bildirim gönderdikten sonra çalıştırın)
```

---

## /commercial-legal:saas-msa-review

---
name: saas-msa-review
description: >
  Referans: SaaS / abonelik sözleşmelerini abonelik ilişkisinde en çok can
  yakan şartlara odaklanarak inceler — otomatik yenileme ve fesih bildiriminin
  şekli (TTK m. 18/3), fiyat artışı ve döviz (TBK m. 99), tek taraflı
  değişiklik (TBK m. 24), veri çıkışı, hizmet seviyesi, alt işleyenler, yapay
  zekâ eğitim hakları. Tüketici karşı tarafta ise 6502 m. 52'yi işaretler.
  SaaS ya da abonelik sözleşmesi tespit edildiğinde /commercial-legal:review
  tarafından yüklenir.
user-invocable: false
---

# /saas-msa-review — SaaS / Abonelik Sözleşmesi İncelemesi

SaaS sözleşmesinin risk profili tek seferlik tedarikten farklıdır: bedel yenilemelerle katlanır, veri birikir, geçiş maliyeti her ay büyür. Bu skill playbook'un standart kontrolünü (`/commercial-legal:vendor-agreement-review`) çalıştırır ve üstüne abonelikte en çok can yakan şartlar için bir katman ekler.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/commercial-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Yargı çevresi varsayımı ve kaynak disiplini

Otomatik yenileme, fiyat, veri taşınabilirliği ve alt işleyen kuralları yargı çevresine duyarlıdır. Bu inceleme eklenti ayarındaki pozisyonları ve Türk hukukunu esas alır. Sözleşme başka bir hukuku seçmişse ya da kullanıcılar AB'deyse işaretle; analiz olduğu gibi aktarılamaz → `/commercial-legal:governing-law-review` (AB: `eu_search_eu_law`; İngiltere: `uk_search_legislation`; Almanya: `de_gesetz_ara`).

- **Sessiz tamamlama yok.** Araç bir emredici kural için az sonuç dönerse dur: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle." Düşük güvenli kaynağı kabul kararını avukat verir.
- **Kaynak etiketi:** `[ArthurLegal TR — 6098 m. X — GG.AA.YYYY]`, yabancı araç için `[ArthurLegal UK/DE/EU — … — GG.AA.YYYY]`, `[web — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`. Etiketleri silme ya da birleştirme.

## Playbook'u yükle

**Hangi taraftayız?** Karşı taraf size platformunu satıyorsa alım tarafı; siz SaaS sağlayıcısıysanız ve karşı taraf müşterinizse satış tarafı. Belli değilse (bayilik, beyaz etiket) sor: "[[ŞİRKET ADI]] bu sözleşmede hangi tarafta — sağlayıcı mı, müşteri mi?" Eşleşen bölümü oku (`### Sales-side playbook` / `### Purchasing-side playbook`), çıktıda yaz. `[Not configured]` ise dur ve `/commercial-legal:cold-start-interview --side <side>` öner.

Önce eşleşen tarafın genel playbook'unu (sorumluluk, tazmin, fesih, hukuk) vendor-agreement-review'daki gibi eksiksiz uygula. Sonra `## Playbook` → eşleşen taraf → `SaaS positions` bölümüne bak: yenileme bildirim penceresi, kabul edilebilir fiyat artışı, veri ihracı, HSS eşikleri, alt işleyen onayı, özellik kaldırma bildirimi. Bu skill bunlar için varsayılan rakam taşımaz. Bölüm bir şart hakkında sessizse sor:

> Playbook'unuz [şart — ör. "kabul edilebilir en uzun yenileme bildirim süresi", "sağlayıcının anonimleştirilmiş türev veriyi saklaması"] hakkında bir şey söylemiyor. Pozisyonunuz ne? Eklenti ayarına ekleyeyim.

Cevabı kaydet ve devam et.

## Sözleşmenin niteliği ve standart koşullar

- **Nitelendirme.** SaaS sözleşmesi Türk hukukunda kanunda düzenlenmemiş (isimsiz/karma) bir sözleşme olarak görülür; hangi tipin (kira, lisans, eser, vekâlet) hükümlerinin kıyasen uygulanacağı **tartışmalı — doktrin ve içtihadı kontrol et**. Uygulanacak boşluk doldurucu kural sonucu değiştirir (ör. fesih); sözleşmede açık düzenleme ara.
- **Lisans.** Kurulumlu yazılımda bilgisayar programı eserdir (FSEK m. 2/1-1); kullanma yetkisi ruhsattır (FSEK m. 48/2); mali haklara dair sözleşme yazılı olmalı ve haklar ayrı ayrı gösterilmelidir (FSEK m. 52). Kullanma ruhsatını üçüncü kişiye (grup şirketleri dahil) devretmek eser sahibinin yazılı muvafakatini ister (FSEK m. 49/1) → grup şirketlerinin kullanımını açıkça yaz. Kopya teslim edilmeyen saf SaaS'ta FSEK lisans şeklinin aranıp aranmadığı **tartışmalı**.
- **Tıkla-kabul / matbu koşullar.** Sağlayıcının tek başına hazırlayıp sunduğu koşullar genel işlem koşuludur (TBK m. 20). Aleyhe koşul, açıkça bilgi verilip içeriği öğrenme imkânı sağlanmadıkça yazılmamış sayılır (m. 21/1); belirsiz koşul düzenleyen aleyhine yorumlanır (m. 23); düzenleyene tek yanlı değiştirme yetkisi veren kayıt yazılmamış sayılır (m. 24); dürüstlük kuralına aykırı aleyhe hüküm konulamaz (m. 25). Yanıltıcı biçimde kanundan önemli ölçüde ayrılan genel işlem şartı kullanmak haksız rekabettir (TTK m. 55/1-f). Alım tarafında güçlü kaldıraç; satış tarafında kendi koşullarınız için risk.
- **Tüketici.** Müşteri tüketiciyse (6502 m. 3/1-k): belirli süreli abonelikte "süre kadar uzar" kaydı konulamaz; uzatma ancak tüketicinin talebi ya da onayıyla olur (6502 m. 52/3); belirsiz süreli ya da bir yıldan uzun abonelik gerekçesiz ve cezai şartsız feshedilebilir (m. 52/4); haksız şartlar kesin hükümsüzdür (m. 5/2). Bu durumda playbook'un B2B pozisyonları uygulanmaz → avukata.

## SaaS katmanı

Her başlıkta sözleşmede bulduğunu yaz ve `SaaS positions` ile karşılaştır. Bu skill'den sabit eşik uygulama.

### 1. Otomatik yenileme

SaaS anlaşmasının en sık bozulduğu yer: kimse bildirim penceresini fark etmez, bir yıl daha ve daha yüksek fiyatla bağlanırsınız.
- **Yenileme süresi** (ilk süreyle aynı, daha uzun, çok yıllığa dönüşen)
- **Fesih bildirim penceresi** (yenilemeden kaç gün önce)
- **Bildirim yöntemi.** Tacirler arasında temerrüde düşürme, fesih ve sözleşmeden dönme ihbarları noter, taahhütlü mektup, telgraf ya da güvenli e-imzalı KEP ile yapılır (TTK m. 18/3). Sözleşmenin "e-posta ya da portal bildirimi yeterlidir" demesinin bu şekli karşılayıp karşılamadığı ve m. 18/3'ün geçerlilik mi ispat şartı mı olduğu **tartışmalı — içtihadı kontrol et**. Pratik: iptali her zaman TTK m. 18/3'teki yollardan biriyle gönder; sözleşmedeki KEP/tebligat adresini kaydet.
- **Yenilemede fiyat** (aynı, endeks tavanlı, o günkü liste fiyatı, sınırsız takdir)

Herhangi bir bayrak olsun olmasın **yenileme tarihini ve bildirim penceresini çıkar ve kaydet** → renewal-tracker.

### 2. Fiyat artışı

- **Yıllık artış** (sabit oran, TÜFE/ÜFE gibi endeks — hangi endeks ve hangi ay, tavan var mı, sınırsız)
- **Tek taraflı fiyat değişikliği.** Matbu koşullarda sağlayıcıya tek yanlı fiyat/koşul değiştirme yetkisi veren kayıt yazılmamış sayılır (TBK m. 24) — müzakere edilmiş sözleşmede bu koruma zayıflar; açık tavan ve fesih hakkı iste.
- **Döviz.** Bedel yabancı parayla belirlenmişse ve "aynen ödeme" kaydı yoksa borç ödeme günündeki rayiçle TL olarak da ödenebilir; temerrütte alacaklı aynen ya da vade/fiilî ödeme günü rayicinden TL ister (TBK m. 99/2-3). İki Türkiye yerleşiği arasında döviz cinsinden ya da dövize endeksli bedel için Türk Parası Kıymetini Koruma Hakkında 32 sayılı Karar ve tebliğlerindeki yasak ve istisnaları ayrıca çek (`tr_mevzuat_ara(query="Türk Parası Kıymetini Koruma Hakkında 32 Sayılı Karara İlişkin Tebliğ")`); madde atfını ancak çektiğin metinden yap.
- **Kullanım aşımı** (yayımlanmış tarife, yüksek oran, belirsiz) ve **"ücret"in kapsamı** (yalnız abonelik mi, geniş tanımlı "ek hizmetler" mi).
- **Fatura itirazı.** Faturayı alan sekiz gün içinde içeriğine itiraz etmezse kabul etmiş sayılır (TTK m. 21/2) → aşım faturaları için iç kontrol süreci gerektiğini iş birimine yaz.
- Sonradan beklenmedik olağanüstü durum: tek kanuni araç aşırı ifa güçlüğüdür (TBK m. 138; sürekli edimlide kural olarak fesih); sözleşmede ayrıca uyarlama/yeniden müzakere kaydı ara.

### 3. Veri taşınabilirliği ve çıkış

Bu sağlayıcıdan bir gün ayrılacağız; verimizi alabilecek miyiz?
- **İhraç biçimi** (açık/standart, belgelenmiş özel biçim, "ticari olarak makul")
- **Ne zaman** (her an self-servis, süre içinde talep üzerine, yalnız sona ermede)
- **Sona erme sonrası erişim** (kaç gün), **maliyet** (ücretsiz, iş-zaman, GB/kayıt başına)
- **Silme teyidi** (talep üzerine tutanak, yok, sağlayıcı türev veriyi saklıyor). Kişisel verinin silinmesi, yok edilmesi ya da anonim hâle getirilmesi veri sorumlusunun yükümlülüğüdür (KVKK m. 7) → silme süresi ve tutanak `/privacy-legal:dpa-review` ile uyumlu olmalı.
- Sağlayıcının "anonimleştirilmiş" ya da "toplulaştırılmış" türev veri saklaması esaslı bir pozisyondur; KVKK'da anonim hâle getirme, başka verilerle eşleştirilerek dahi kimliği belirlenebilir kişiyle ilişkilendirilemeyecek hâle getirmedir (KVKK m. 3/1-b). Ekibin tutumunu playbook'tan teyit et; her iki yönde de işaretle.

### 4. Erişilebilirlik ve hizmet seviyesi (HSS)

Yalnız iş bu hizmetin ayakta olmasına gerçekten bağlıysa önemlidir; anket aracı için müzakere sermayesi harcama.
- **Erişilebilirlik taahhüdü** (yüzde ya da "ticari olarak makul çaba"), **ölçüm dönemi** (aylık, üç aylık, yıllık)
- **Telafi.** Hizmet kredisi nasıl hesaplanıyor, tavanı var mı, "tek çare" mi? Hizmet kredisinin cezai şart mı (TBK m. 179-182), bedel indirimi mi sayılacağı **tartışmalı**; nitelendirme tavana ve ek tazminata etki eder. "Tek ve münhasır çare" kaydı önceden sorumsuzluk anlaşmasıdır: ağır kusurdan sorumsuzluk kesin hükümsüzdür (TBK m. 115/1).
- **Planlı bakım istisnası** (tanımlı pencere, önceden bildirim, sınırsız)
- Tek çare kaydının sorumluluk tavanıyla etkileşimi (aşağıda).

### 5. Alt işleyenler

Veri koruma konusudur ama SaaS'a özgüdür, çünkü liste abonelik boyunca **değişir**.
- **Güncel liste** (yayımlanmış, talep üzerine, yok), **değişiklik bildirimi** (önceden süre, yok), **itiraz hakkı** (engelleme, bildirip feshetme, yalnız bildirim, yok)
- Yurt dışındaki alt işleyen ya da bulut → kişisel veri yurt dışı aktarımı (KVKK m. 9). Mekanizmayı bu skill değerlendirmez → `/privacy-legal:dpa-review` (sektörel katman ve aktarım orada).

### 6. Hizmet değişiklikleri ve özellik kaldırma

- **Esaslı olumsuz değişiklik** (feshetme hakkı, yalnız bildirim, sınırsız) — matbu koşulda tek yanlı değiştirme yetkisi için TBK m. 24
- Dayandığınız özellikler için **kaldırma bildirim süresi**; **yerine gelen özellik** aynı paket mi, üst paket mi

## Yapay zekâ ve makine öğrenmesi hakları

SaaS müzakeresinin en hızlı değişen başlığı; tek satırlık "var mı" kontrolü yetmez. Yedi boyutun her birini profilin `## AI/ML training rights` bölümündeki pozisyonla eşleştir:

1. **Açık izin.** Müşteri verisi / içeriği / kullanım verisi YZ eğitimi, model geliştirme için kullanılabiliyor mu? Alım tarafında genelde HAYIR (müşteri sağlayıcının ürününü sübvanse eder, rekabete duyarlı bilgi sızabilir). Satış tarafında gelir, kötüye kullanımda itibar riski.
2. **Politika yoluyla örtülü izin.** Sözleşme sağlayıcının gizlilik politikasını ya da kullanım koşullarını "güncellendiği şekliyle" mi içeriyor? Tek yanlı güncelleme yoluyla eğitim hakkı eklenebiliyor mu? Matbu koşulda bu yetki yazılmamış sayılır (TBK m. 24), ama kayda güvenme; açık yasak iste. "Hizmet geliştirme", "analitik" gibi torba ifadelere ve log/telemetriyi müşteri verisi tanımından çıkaran "kullanım verisi" tanımlarına bak.
3. **Anonimleştirme standardı.** "Anonim" tanımsızsa zayıftır; KVKK m. 3/1-b ölçütüne bağla. AB bağlantısı varsa GDPR ölçütünü araçla çek (`eu_get_document_text(celex="32016R0679")`, gerekçe 26). Geri döndürülebilir mi?
4. **Rekabet açısından bulaşma.** Sağlayıcı rakiplerinize de hizmet veriyor mu? Verinizle eğitilen model rakibin çıktısına sızabilir; emanet iş ürününden yetkisiz yararlanma ve sır ifşası TTK m. 55/1-c,d tabanıdır ama sözleşmesel izolasyon taahhüdü iste.
5. **Vazgeçme (opt-out) kapsamı ve kalıcılığı.** Tüm YZ kullanımlarını mı kapsıyor, yenilemelerden ve koşul güncellemelerinden sonra sürüyor mu, kullanıcı mı kurum mu düzeyinde? Varsayılan açık mı kapalı mı — sözleşmede yazılı mı?
6. **Çıktı sahipliği.** Ürün YZ çıktısı üretiyorsa çıktı kimin, sağlayıcı çıktıyı eğitim örneği olarak kullanabilir mi? YZ çıktısının FSEK anlamında eser sayılıp sayılmadığı **tartışmalı**; hakları sözleşmeyle açıkça düzenle. Üçüncü taraf YZ alt işleyenleri (büyük dil modeli sağlayıcıları) alt işleyen listesinde görünür.
7. **Düzenleyici zincir.** Sağlayıcının veriyi YZ için kullanması sizin için düzenleyici risk doğuruyor mu? Türkiye'de amaç dışı işleme ve aktarım → `/privacy-legal:use-case-triage`; AB bağlantısı varsa YZ Tüzüğü yükümlülükleri araçla çekilir (`eu_search_eu_law(query="Regulation (EU) 2024/1689 artificial intelligence")`); sektörel kurum kararları için `tr_kurum_karari_ara`.

Sözleşme yedisinde de sessizse bu da bulgudur: "Sözleşme YZ/ML eğitim hakları konusunda sessiz — açık yasak ya da yedi boyuta bağlı tanımlı istisna isteyin."

## Sorumluluk tavanı ve Türk hukuku sınırları

Tavan için vendor-agreement-review'daki dört boyutlu karar prosedürünü uygula (doğrudan/dolaylı zarar, tavan tabanının birebir alıntısı, tavan dışı kalemler, boyut başına playbook). SaaS'ta tavan dışı kalemler genelde veri ihlali, gizlilik ve fikrî hak tazminidir; bunlar tavan dışındaysa kalan "tavanlı alan"ın anlamlı mı göstermelik mi olduğunu yaz.

**Yargı çevresi farkı.** Playbook tek bir hukuk tercihini her yere uygular; geçerlilik ise hukuka göre değişir. Türk hukukunun tipik sınırları:

| Konu | Türk hukuku | Dayanak |
|---|---|---|
| Sorumsuzluk / tavan | Ağır kusurdan önceden sorumsuzluk kesin hükümsüz; izinle yürütülen uzmanlık hizmetinde hafif kusur için de | TBK m. 115/1, 115/3 |
| Yardımcı kişi (alt yüklenici, alt işleyen) | Sorumluluk önceden kaldırılabilir; izinle yürütülen uzmanlık hizmetinde kaldırılamaz | TBK m. 116/2-3 |
| Otomatik yenileme | B2B'de kanuni üst sınır yok, bildirim şekli TTK m. 18/3; tüketicide emredici kural | TTK m. 18/3; 6502 m. 52 |
| Cezai şart | Tacir borçlu aşırılık iddiasıyla indirim isteyemez | TTK m. 22 |
| Zamanaşımı | TBK'daki zamanaşımı süreleri sözleşmeyle değiştirilemez; "talepler 1 yıl içinde ileri sürülür" kaydının sözleşmesel hak düşürücü süre olarak geçerliliği **tartışmalı** | TBK m. 148 |
| Rekabet yasağı / ayartmama | Rakipler arasında 4054 m. 4 riski | 4054 m. 4 |

Playbook pozisyonu seçilen hukukta uygulanamıyorsa işaretle: "Playbook'unuz [X] istiyor, ama bu sözleşme [Y] hukukuna tabi ve orada [X] [geçersiz / sınırlı / emredici kurala tabi]." Yabancı hukuk için kural araçtan çekilir, ezberden değil → `/commercial-legal:governing-law-review`.

## Redline inceliği

vendor-agreement-review'daki kural: en küçük düzeltme (kelime → ifade → alt bent → cümle → madde); tüm maddeyi değiştirdiysen ileti notunda söyle.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["20","21","23","24","25","99","115","116","138","148"])
tr_mevzuat_madde_getir(number="6102", madde_no=["18","21","22","55"])
tr_mevzuat_madde_getir(number="5846", madde_no=["2","48","49","52"])
tr_mevzuat_madde_getir(number="6502", madde_no=["3","5","52"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="18/3 fesih ihbarı noter aracılığıyla ispat şartı", date_from="2020-01-01")
tr_ictihat_semantik_ara(initial_keyword="genel işlem koşulu tek taraflı değişiklik", query="tacirler arası sözleşmede TBK 24 değiştirme yasağı uygulanır mı")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".

## Çıktı

vendor-agreement-review not yapısını kullan (üst başlık orada); standart playbook kontrollerinden sonra SaaS bölümü ekle.

**Çift ciddiyet** (eklenti ayarı `## Dual severity`): her SaaS bulgusunda iki eksen —
- **Hukuki risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
- **İş sürtünmesi:** 🔴 Anlaşmayı durdurur | 🟠 Yavaşlatır | 🟡 Kafa karıştırır | 🟢 Görünmez

Veri çıkışı, otomatik yenileme ve fiyat artışı bulguları çoğu zaman 🟢 hukuki / 🔴 iş sürtünmesidir: kloz geçerlidir ama müşterinin ayrılamamasının ya da finansın yenilemede şaşırmasının nedenidir. Bunları iş sürtünmesi ciddiyetiyle öne çıkar.

```markdown
### Sonuç
[İmzalanabilir / Önce X için mücadele / Vazgeç — tek cümle neden]
**Taraflar:** [tacir–tacir / tüketici var]   **Playbook:** [Satış / Alım tarafı]

### YZ ve makine öğrenmesi hakları
[Açık eğitim kaydı, torba "hizmet geliştirme", kullanım verisi tanımı, çıktı sahipliği, üçüncü taraf YZ alt işleyenleri, opt-out / opt-in. Sessizse: "YZ/ML eğitim hakları konusunda sessiz — açık yasak ya da tanımlı istisna isteyin."]

## SaaS'a özgü bulgular

### Otomatik yenileme
**Yenileme tarihi:** [tarih]
**Bildirim penceresi:** [tarih]'e kadar iptal ([N] gün önce) — yöntem: [sözleşmedeki] / TTK m. 18/3 uyumu: [evet / hayır / tartışmalı]
**Yenileme fiyatı:** [yazıldığı gibi]
**Playbook uyumu:** [pozisyon içinde / sapma / değinilmemiş]
**Yenileme takibine:** [evet — kayıt alanları aşağıda]

### Fiyat artışı
### Veri çıkışı
[iş biriminin okuması gereken bölüm]
### HSS
[bulgular ya da "Atlandı — [paydaş]'a göre hizmet iş açısından kritik değil"]
### Alt işleyenler
### Hizmet değişiklikleri
```

## Devirler

**renewal-tracker'a:** Yenileme tarihi ve bildirim penceresi bulununca devret. Kayıt şu alanları bekler (tam şema: `skills/renewal-tracker/references/renewal-register.yaml`; alan adları değişmez):

```yaml
counterparty:         [ad]
agreement:            [başlık]
signed_date:          [ISO tarih]
initial_term_end:     [ISO tarih]
renewal_mechanism:    [ör. "auto-renew annual"]
notice_period_days:   [tam sayı]
cancel_by_effective:  [ISO tarih — initial_term_end eksi notice_period_days]
price_on_renewal:     [yazıldığı gibi]
annual_value:         [tam sayı, belirtilmişse]
business_owner:       [e-posta, biliniyorsa]
clm_id:               [varsa]
status:               active
```

Belirlenemeyen alanı boş bırak ve hangilerinin eksik olduğunu yaz (`clm_id`, `annual_value`, `business_owner` çoğu zaman insandan gelir). Bildirim yönteminin TTK m. 18/3'e uyup uymadığını kayıt notuna ekle.

**escalation-flagger'a:** Bir SaaS kontrolü `## Escalation`'daki "asla kabul etme" ya da eskalasyon tetikleyicisine düşerse `/commercial-legal:escalation-flagger` yönlendirir.

## Neyle kavga edilir

Büyük SaaS sağlayıcıları kâğıtlarını, havayolunun bilet koşullarını müzakere ettiği kadar müzakere eder. Savaşı playbook'a göre seç: `SaaS positions` her zaman itiraz edilen, yalnız büyük anlaşmada itiraz edilen ve bırakılan şartları ayırmalı; ayırmıyorsa sor. Sözleşme değeri ve geçiş maliyetine göre kalibre et: kolay ikamesi olan küçük bir araç, üzerine iş kurulacak büyük bir platformdan daha hafif ele alınır.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu incelemeye göre uyarla (redline'ı gönder, eskalasyon, ek olgu iste — ör. alt işleyen listesi, yenileme kaydını aç, bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.

---

## /commercial-legal:stakeholder-summary

---
name: stakeholder-summary
description: >
  Tamamlanmış bir sözleşme incelemesini iş biriminin gerçekten okuyacağı bir
  özete çevirir. Hukuki not değil — "bunu imzalayabilir miyim, neyi bilmem
  gerekiyor" sorusuna iki dakikalık cevap. Eskalasyonların gerçekten
  yönlendirilip yönlendirilmediğini de sayar. "İş birimi için özetle",
  "[paydaş] için yaz", "satın almaya anlat", "hukukçu olmayan özet" denince ya
  da inceleme bitip hukuk dışına gidecekken kullan.
---

# /stakeholder-summary — İş Birimi Özeti

Sözleşmeyi isteyen iş birimi sahibi hukuki not istemez. Bilmek istediği: imzalayabilir miyim, püf noktası ne, benim ne yapmam gerekiyor. Bu skill tamamlanmış incelemeyi buna çevirir. Sözleşmeyi yeniden incelemez — incelemeyi okur.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/commercial-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Destination check

Özet çoğu zaman hukuk dışına gider. Kullanıcı bir hedef söylediyse (kanal, dağıtım listesi, karşı taraf, "herkes") dar gizlilik çevresinde mi diye sor. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD'deki "privilege" gibi geniş bir koruma değildir; şirket geneli kanala ya da karşı tarafa giden metin gizliliğini fiilen kaybeder. Çevre dışıysa (a) hukuk için tam sürüm, (b) arındırılmış sürüm ya da (c) ikisini öner. Arındırılmış sürümde iç müzakere pozisyonu, geri çekilme noktası ve "kabul edebileceğimiz en kötü" yazılmaz. Kanonik kural: `## Shared guardrails → Destination check`.

## Hangi taraf?

Alttaki inceleme satış ya da alım tarafı playbook'uyla yapıldı; bu çerçeveyi koru. Alım tarafı özeti "ne alıyoruz ve karşılığında neyden vazgeçtik", satış tarafı özeti "ne satıyoruz ve neyi taahhüt ettik" der. İnceleme notunun başında yazar; yazmıyorsa özetlemeden önce avukata sor.

## Okur kalibrasyonu

Eklenti ayarı `## House style` → iş birimi özetlerini kim okur, uzunluk ne olmalı. Yazmıyorsa varsayılan: satın alma ya da birim yöneticisi, en fazla iki paragraf, hukuk terimi yok.

| Okur | Önemsediği | Önemsemediği |
|---|---|---|
| **Satın alma** | Fiyat, yenileme düzeni, onay sırası, ödeme vadesi | Tavanın yapısı |
| **Birim yöneticisi (bütçe sahibi)** | Ekibi kullanabilir mi, bozulursa ne olur, maliyet | Tazminin kapsamı |
| **Finans** | Toplam sahip olma maliyeti, yenilemede fiyat riski, döviz/kur riski, fatura itiraz süresi | Uygulanacak hukuk |
| **Bilgi güvenliği / BT** | Veri nerede, alt işleyenler, yurt dışı aktarım, ISO 27001 / SOC 2 | Geri kalan her şey |
| **Üst yönetim sponsoru** | Bizi zor duruma sokar mı, hukuk engel mi | Ayrıntı |

Bağlamdan belli değilse kimin için olduğunu sor.

## Özet

### Uzunluk sınırı — uygulanır

- **Bir paragraf:** karar ve bu ne (ticari dille)
- **Bir paragraf:** püf noktası — kimse şimdi söylemezse paydaşın sonra şaşıracağı şey
- **2-3 maddelik yapılacaklar listesi** (en fazla üç; dördüncüyü istiyorsan ilk üçü yeterince sıkı değildir)
- **Tek satır kapanış:** onay ve zamanlama

**Toplam 200 kelimenin altında.** Fazlası paydaşın ihtiyaç duymadığı ayrıntıdır — onun için not var. Kapanış üçüncü paragrafa dönüşüyorsa listeye kat.

### Alıntı disiplini

Bir kloz alıntılanacaksa **şartlı cümlenin tamamını** alıntıla. "Sipariş Formunda aksi öngörülmedikçe, kampanyalı ya da tek seferlik fiyatlı aboneliklerin yenilemesi liste fiyatından yapılır" ile "yenileme liste fiyatından yapılır" farklı şeylerdir; kesmek istisnayı kurala çevirir. Tam alıntı sığmıyorsa kesme, yeniden ifade et: "Kampanyalı fiyatta yenileme liste fiyatına döner" adil bir özettir.

### Biçim

```markdown
[ÜST BAŞLIK — profil ## Outputs]
<!-- Dar gizlilik çevresi dışına (iş birimi, karşı taraf, tedarikçi) gönderiyorsanız yukarıdaki başlığı kaldırın. Başlık tek başına koruma yaratmaz. -->

**[Karşı taraf] [Sözleşme türü]** — [İMZAYA HAZIR | DÜZELTME GEREKLİ | DURDURULDU]

[Bir paragraf: sözleşme ne yapıyor, ticari dille. "Bulut tabanlı analitik hizmetlerin sunumuna ilişkin çerçeve sözleşme" değil — "pazarlama ekibinin istediği pano aracının sözleşmesi."]

[Bir paragraf: bilmesi gereken. Varsa püf noktası. Ör.: "Dikkat: her yıl otomatik yenileniyor; iptal için yenilemeden 60 gün önce noter, taahhütlü mektup ya da KEP ile bildirim göndermemiz gerekiyor — e-posta yetmeyebilir." Ya da: "Temiz sözleşme, sürpriz yok, imzalanabilir."]

**Yapmanız gerekenler:**
- [ ] [Varsa iş — "verinin AB'de tutulmasında ekip için sorun var mı, teyit edin" ya da "hiçbir şey — imzaya ben yönlendiriyorum"]

**Onay:** [kim onaylıyor, beklenen zaman]
```

**Takip kaydını iddia etmeden önce doğrula.** Özet "yenileme takibine ekledim" (ya da "takipte", "hatırlatıcı kuruldu") demeden önce bu sözleşme için `renewal-tracker`'ın gerçekten çalıştırıldığını kontrol et: çıktı ya da matter klasöründe bu karşı tarafı/sözleşmeyi adlandıran bir `renewal-tracker` çıktısı ara. Yoksa ya önce `renewal-tracker`'ı çalıştır, ya da özeti kayıt iddiası olmadan yaz ve listeye ekle: "Yenileme takibine ekle — henüz yapılmadı." Hiç çalmayacak bir hatırlatıcıya paydaşı güvendirmek, güvenceyi hiç vermemekten kötüdür.

### Ne nasıl çevrilir

| Hukuki bulgu | İş dili |
|---|---|
| "Sorumluluk 12 aylık bedelle sınırlı" | "Bir şeyi bozarlarsa alabileceğimiz en fazla, onlara bir yılda ödediğimiz kadar." |
| "İsteğe bağlı fesih yok" | "İmzaladıktan sonra süre sonuna kadar bağlıyız; kullanmayı bırakırsak da iptal edemeyiz." |
| "60 gün bildirimli otomatik yenileme" | "Her yıl kendiliğinden yenileniyor. İptal için yenileme tarihinden iki ay önce noter, taahhütlü mektup ya da KEP ile bildirmemiz gerekiyor." |
| "Fikrî hak tazmini yok" | "Biri bu aracın kendi hakkını ihlal ettiğini söyleyip bize dava açarsa, tedarikçi bizi savunmak zorunda değil." |
| "Alt işleyen listesi açıklanmamış" | "Verimize onların üzerinden başka hangi şirketlerin erişeceğini bilmiyoruz." |
| "Sona ermeden itibaren 30 gün içinde veri silinir" | "İptal edince verimizi bir ay içinde siliyorlar. Gereken her şeyi ondan önce dışarı alın." |
| "HSS kredisi aylık bedelin %10'uyla sınırlı" | "Hizmet çökerse küçük bir indirim alırız; kesintinin işe maliyetini karşılamaz." |
| "Fatura 8 gün içinde itiraz edilmezse kabul sayılır" | "Faturadaki bir hataya 8 gün içinde itiraz etmezsek kabul etmiş sayılıyoruz — faturaları hemen kontrol edin." |
| "Bedel USD; TL ile ödeme rayice göre" | "Fiyat dolar; kur yükselirse TL maliyetimiz de yükselir." |
| "Ödeme vadesi 90 gün" (alım tarafı) | "Ödeme vadesi kanuni sınırı aşabilir; satın alma şartlarında değişiklik gerekebilir." |

Son üç satırın hukuki dayanağı (TTK m. 21/2, TBK m. 99, TTK m. 1530/5) incelemede yazılıdır; özette madde numarası verme.

### Ne yazılmaz

- Madde numaraları
- Tırnak içinde tanımlı terimler
- "Tazmin" kelimesi ("şu olursa onlar bizi karşılar" / "biz onları karşılarız" de)
- "Aksine hüküm bulunmadıkça", "işbu", "mezkûr" gibi kalıplar
- Renkli noktalı risk matrisleri (paydaş daha önce özellikle istemediyse)
- "Bu hukuki görüş değildir" uyarıları — paydaş kimin gönderdiğini biliyor

## İnceleme sorun bulduysa

🔴 ya da 🟠 sorun varsa özet yine iki paragraftır; ikinci paragraf "neye itiraz ediyoruz ve neden" olur.

```markdown
[ÜST BAŞLIK — profil ## Outputs]
<!-- Dar gizlilik çevresi dışına gönderiyorsanız başlığı kaldırın. -->

**[Karşı taraf] [Sözleşme türü]** — DÜZELTME GEREKLİ

[Ne olduğu, bir paragraf.]

Hazır olmadan önce [N] konuda geri dönüyoruz. Asıl olanı: [kritik sorun sade dille — "verimizi kendi ürünlerini geliştirmek için kullanmak istiyorlar; yani rakiplerimizin kullandığı sürüm bizim verimizle akıllanıyor"]. Silinmesini istedik. [Gerçekçi değerlendirme: "Büyük ihtimalle kabul ederler" / "Tıkanma noktası olabilir — haber veririm."]

**Yapmanız gerekenler:**
- [ ] Şimdilik hiçbir şey — cevap gelince haber veririm.
  YA DA
- [ ] [Vermeleri gereken iş kararı: "X'te geri adım atmazlarsa Y'yi kabul eder misiniz, yoksa vazgeçelim mi?"]
```

## Eskalasyon uzlaştırması

Üstteki inceleme birden çok onaylayıcı adlandırabilir (GC yardımcısı, bilgi güvenliği yöneticisi, kişisel veri sorumlusu irtibat kişisi, finans direktörü, iş birimi sahibi); `escalation-flagger` ise bulguları tek tek yönlendirir. Uzlaştırma olmadan bir kişi notu görür, diğerleri hiç görmez. Özetten önce:

1. **İncelemenin adlandırdığı hedefleri say** — sondaki yönlendirme bloğu ya da bulgu bazındaki "[X]'e eskalasyon" etiketleri; aynı kişi bir kez sayılır (N).
2. **Gerçekten yönlendirilenleri say** — inceleme ya da matter klasöründe, inceleme yazıldıktan sonra `escalation-flagger`'ın ürettiği `escalation-*.md` taslakları (M).
3. **Uzlaştır** — N − M eskalasyon yönlendirilmemiş demektir.

Püf noktası paragrafının altına, listenin üstüne:

```markdown
**Eskalasyon durumu:** [N] hedeften [M]'i yönlendirildi. Şunlar yönlendirilmedi ve işlem bekliyor:
- [Onaylayıcı] — [onu adlandıran bulgu, tek satır]
```

Hepsi yönlendirildiyse: `**Eskalasyon durumu:** [N] hedeften [N]'i yönlendirildi.` İnceleme eskalasyon adlandırmadıysa bloğu çıkar. Taslak hiç yoksa M = 0 say ve N'nin tamamını listele — bulgu budur.

**Paydaş tanımıyor diye bir onaylayıcıyı uzlaştırmadan çıkarma.** Uzlaştırma iç kullanım içindir: özeti gönderen avukata yönlendirmenin bitip bitmediğini söyler. Paydaşa giden metin dar kalacaksa uzlaştırma "yönlendirme durumu" dipnotunda ya da ayrı notta durabilir, ama var olmalıdır. Yönlendirme bitmemişken bitmiş izlenimi veren özet, hiç özet olmamasından kötüdür. **Kelime sınırı istisnası:** uzlaştırma bloğu 200 kelimeye dahil değildir.

## Devirler

- **vendor-agreement-review / saas-msa-review'dan:** onlar tam notu üretir; bu skill notu okur ve sıkıştırır. Sözleşmeyi yeniden inceleme.
- **Paydaşa:** eklenti ayarının söylediği kanaldan. Anlık mesajlaşma kanalıysa 150 kelimenin altında; e-postaysa yukarıdaki biçim yeterli.

## Ton

Paydaşlar hukuk hakkında iki şeyi hatırlar: beni durdurdu mu, anlamlı mıydı. Bu skill hukukun anlamlı olduğu yerdir. Kahve içerken zeki bir iş arkadaşına anlatır gibi yaz, dosyaya not yazar gibi değil. Dürüst özet "sorun yok, imzalayın" ise bunu söyle; temiz bir incelemeyi titiz görünmek için üç paragrafa şişirme.

---

## /commercial-legal:vendor-agreement-review

---
name: vendor-agreement-review
description: >
  Referans: gelen tedarikçi/hizmet sözleşmesini `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`
  playbook'una ve Türk hukukunun emredici sınırlarına (TBK m. 115-116
  sorumsuzluk, m. 179-182 cezai şart, TTK m. 1530 ödeme süresi, m. 18/3
  bildirim şekli, FSEK m. 48-52 fikrî haklar, HMK yetki/tahkim) göre inceler;
  sapmaları bulur, riski iki eksende puanlar, yapıştırılmaya hazır redline
  yazar ve doğru onaylayıcıya yönlendirir. Çerçeve hizmet sözleşmesi ya da
  benzeri tespit edildiğinde /commercial-legal:review tarafından yüklenir.
user-invocable: false
---

# /vendor-agreement-review — Tedarikçi / Hizmet Sözleşmesi İncelemesi

Sözleşmeyi bu ekibin gerçekten kullandığı playbook'a göre oku, sapan her şartı bul ve avukata her biri için ne yapacağını söyle — "gözden geçirilmesi düşünülebilir" değil, somut redline metniyle. Çıktı avukatın tek geçişte işleyebileceği bir nottur: her sorunun ciddiyeti, iş etkisi, önerilen düzeltmesi ve gerekiyorsa eskalasyonu var.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/commercial-legal:matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Destination check

Kullanıcı bir hedef söylediyse (kanal, liste, karşı taraf, "herkes") dar gizlilik çevresinde mi diye sor. Avukatın sır saklama yükümlülüğü (Av. K. m. 36) ABD tipi geniş bir belge koruması değildir; karşı tarafa, tedarikçiye ya da şirket geneline giden metin gizliliğini fiilen kaybeder. Çevre dışıysa (a) hukuk için tam sürüm, (b) arındırılmış sürüm ya da (c) ikisini öner. Kanonik kural: `## Shared guardrails → Destination check`.

## Ön koşul: playbook

**Sözleşmeyi okumadan önce eklenti ayarını ve `company-profile.md`'i oku.** Ayar yoksa ya da yer tutucu taşıyorsa:

> Profilinizi henüz yapılandırmamışsınız — playbook pozisyonlarını, eskalasyonu ve üslubu buradan öğreniyorum.
> - `/commercial-legal:cold-start-interview` çalıştırın (2 dakika), sonra sizin playbook'unuza göre inceleyeyim.
> - Ya da **"provisional"** deyin; genel varsayılanlarla (Türk hukuku, orta risk iştahı, avukat rolü, playbook yok — yaygın tedarikçi risklerini ilk ilkelerden işaretlerim) incelerim ve her çıktıyı `[PROVISIONAL — profili yapılandırınca size göre ayarlanır]` diye etiketlerim.

**Provisional mod:** Sınırsız sorumluluk, veri ihlali istisnası yokluğu, tavansız tazmin, bildirimsiz otomatik yenileme gibi yaygın riskleri ilk ilkelerden işaretle; inceleyen notunu ve her bulgu bloğunu `[PROVISIONAL]` ile etiketle; sonuna ekle: "Bu, varsayılanlarla yapılmış genel bir çalışmaydı. Kendi playbook'unuz, hukukunuz ve risk iştahınızla çıktı için `/commercial-legal:cold-start-interview` çalıştırın — 2 dakika."

**Hangi taraftayız?** Karşı taraf mal/hizmet sağlıyorsa alım tarafı; ürününüzü satın alan müşteriyse satış tarafı. Belli değilse (bayilik, ortaklık, gelir paylaşımı) sor: "[[ŞİRKET ADI]] bu sözleşmede hangi tarafta — tedarikçi mi, müşteri mi?" Eşleşen bölümü oku (`### Sales-side playbook` / `### Purchasing-side playbook`), çıktıda yaz. `[Not configured]` ise dur, `/commercial-legal:cold-start-interview --side <side>` öner.

Playbook doğruluğun kaynağıdır: ekibin standart pozisyonları (piyasa standardı değil, *onların* standardı), daha önce kabul ettikleri geri çekilme pozisyonları, asla kabul etmedikleri, kimin neyi onayladığı ve önce bakılacak tek anlaşma bozucu (`#### The one thing`). Sözleşmede anlaşma bozucu varsa notun başında işaretle ve ayrıntılı incelemeyi durdur.

## Akış

### Adım 1: Yönlen

Sözleşmeyi bir kez hızla oku:

| Soru | Cevap |
|---|---|
| Sözleşme türü | Çerçeve hizmet / SaaS / proje (eser) / danışmanlık (vekâlet) / lisans / diğer |
| Biz kimiz | Müşteri / tedarikçi (bu skill genelde müşteri tarafıdır — değilse işaretle) |
| Karşı taraf | Unvan; büyük kurumsal (müzakere etmez) mi, girişim (eder) mi? |
| Taraflar tacir mi | Ticari iş (TTK m. 3) → TTK m. 18/3, 22, 1530, 5/A uygulanır |
| İmza yetkisi | İmza sirküleri / ticaret sicili kaydıyla teyit edildi mi? |
| Bedel | Yıllık / toplam; para birimi (TL / döviz) |
| Süre | Uzunluk, yenileme düzeni |
| Kişisel veri eki | Ekli / bağlantıyla atıf / yok |
| Sipariş formu | Ayrı belge / gövdede |
| Dil | Türkçe / yabancı dil / iki dilli (hangi metin esas) |

**Sözleşmenin niteliği.** Türk hukukunda sonuçlar türe göre değişir: eser sözleşmesinde (TBK m. 470) iş sahibi eser tamamlanmadan, yapılan kısmın karşılığını ödeyip yüklenicinin bütün zararını gidererek sözleşmeyi feshedebilir (TBK m. 484); vekâlet ve kanunda düzenlenmemiş iş görme sözleşmelerinde (TBK m. 502/2) taraflar her zaman sona erdirebilir, uygun olmayan zamanda sona erdiren zararı giderir (TBK m. 512). "Süre bitmeden feshedilemez" kaydının vekâlet niteliğindeki ilişkide geçerliliği **tartışmalı — içtihadı kontrol et**. Niteliği nota yaz.

**Bedel belirsizse dur ve sor.** Çerçeve sözleşme bedeli göstermiyor, sipariş formu gösteriyorsa (tipik), eskalasyon eşiğini uygulamadan önce:

> Çerçeve sözleşme yıllık bedeli göstermiyor; bedel sipariş formunda. Eskalasyon eşiğiniz [matristen X]. Yönlendirmeden önce bedele ihtiyacım var: (1) sipariş formundaki bedeli yapıştırın (tercih), (2) eşiğin altında mı üstünde mi söyleyin — not, bedel görülmeden bu varsayımla yönlendirildiğini yazar, (3) her hâlükârda üst onaylayıcıya yönlendirelim.

Varsayılan bir bedeli sessizce yönlendirmede kullanma.

**Kişisel veri eki bağlantıyla atıfla eklenmişse** ("[URL]'de yer alan veri işleme eki"): ek sözleşmenin parçasıdır ama önünde değildir. Tabloda ve notta açıkça yaz; veri koruma analizinin kısmi olduğunu belirt ve `/privacy-legal:dpa-review` öner (yüklüyse: "Eki hazır olduğunuzda `/privacy-legal:dpa-review`'a vereyim mi? Alt işleyen, yurt dışı aktarım ve ihlal bildirimini o yakalar."). Eksik ek ile okunmamış eki ayrı etiketle.

### Adım 2: Anlaşma bozucu kontrolü

`#### The one thing`'i önce kontrol et. Varsa:

```markdown
## ⛔ ANLAŞMA BOZUCU VAR

**Madde [X.X]** [anlaşma bozucu]yu içeriyor. Playbook'a göre kesin hayır. Öneri:
- [ ] İtiraz — [somut alternatif metin] öner
- [ ] Vazgeç — karşı taraf geri adım atmazsa imzalamıyoruz

Aşağıdaki ayrıntılı inceleme bütünlük için verilmiştir; bu çözülmedikçe anlamsızdır.
```

### Adım 3: Madde madde karşılaştırma

Eklenti ayarındaki her playbook kategorisi için karşılık gelen maddeyi bul ve karşılaştır. Her sapma için:

```markdown
### [Madde X.X]: [Konu]

**Playbook:** [standart pozisyon, eklenti ayarından alıntı]
**Sözleşme:**
> "[birebir alıntı]"
**Fark:** [Eksik şart | Standarttan zayıf | Geri çekilme pozisyonundan zayıf | Standart dışı yapı | Kabul edilemez]
**Türk hukuku sınırı:** [varsa — madde atfıyla; yoksa "yok"]
**Hukuki risk:** 🔴 Kritik | 🟠 Yüksek | 🟡 Orta | 🟢 Düşük
**İş sürtünmesi:** 🔴 Anlaşmayı durdurur | 🟠 Yavaşlatır | 🟡 Kafa karıştırır | 🟢 Görünmez
**Neden önemli:** [bir iki cümle, sade dille]
**Önerilen redline:**
> "[yapıştırılmaya hazır metin]"
**Kabul etmezlerse:** [playbook geri çekilme pozisyonu ya da "[kişi]'ye eskalasyon"]
```

| Düzey | Anlamı |
|---|---|
| 🔴 Kritik | Düzeltilmeden imzalanmaz. "Asla kabul etme" listesinde ya da anlaşma bozucu; ya da Türk hukukunda kesin hükümsüz bir kayda dayanılıyor. |
| 🟠 Yüksek | Güçlü itiraz; geri adım yoksa eskalasyon. Geri çekilme aralığının dışında. |
| 🟡 Orta | İlk turda itiraz; son açık nokta ise kabul. Aralık içinde ama standardın altında. |
| 🟢 Düşük | Not et, sermaye harcama. Playbook'un açıkça tolere ettiği ya da üslup farkı. |

Ciddiyet her zaman eklenti ayarına göre verilir. Bir şart hiçbir pozisyona oturmuyorsa kullanıcıya hangi kovaya ait olduğunu sor ve cevabı ayara kaydetmeyi öner.

#### Türk hukukunun emredici sınırları (her incelemede tara)

| Kloz | Sınır / kural | Dayanak |
|---|---|---|
| Sorumluluk istisnası ve tavan | Ağır kusurdan önceden sorumsuzluk kesin hükümsüz; izinle yürütülen uzmanlık hizmetinde hafif kusurdan sorumsuzluk da kesin hükümsüz. Tavanın da bu sınıra tabi olduğu yerleşik görüştür — doktrini kontrol et | TBK m. 115/1, 115/3 |
| Yardımcı kişiler (alt yüklenici) | Borçlu yardımcısının işi yürütürken verdiği zarardan sorumludur; bu sorumluluk önceden kaldırılabilir, izinle yürütülen uzmanlık hizmetinde kaldırılamaz. Ağır kusur sınırının burada da uygulanıp uygulanmadığı **tartışmalı** | TBK m. 116 |
| "Dolaylı zarar" istisnası | Kanunda "dolaylı / netice zararı" tanımı yok; sorumluluğun kapsamına haksız fiil hükümleri kıyasen uygulanır. Kâr kaybı, veri kaybı, itibar kaybı, üçüncü kişi talepleri gibi kalemleri tek tek say; tanımsız istisnanın kapsamı **tartışmalı** | TBK m. 112, 114 |
| Cezai şart | Seçimlik/ifaya eklenen ceza; zarar olmasa da ödenir; aşan zarar için kusur ispatı; hâkim aşırıyı indirir — tacir borçlu indirim isteyemez | TBK m. 179, 180, 182; TTK m. 22 |
| Ödeme süresi (alım tarafında kritik) | Ticari işletmeler arası mal/hizmet tedarikinde sözleşmesel ödeme süresi en fazla 60 gün; açık anlaşmayla ve alacaklı aleyhine ağır haksızlık yaratmamak kaydıyla daha uzun olabilir, ama alacaklı KOBİ ya da borçlu büyük işletmeyse 60 günü aşamaz. Süresinde ödemeyen ihtarsız temerrüde düşer; gecikme faizini ya da geç ödeme zararından sorumluluğu kaldıran/sınırlayan hüküm geçersiz; oran ve asgari giderimi TCMB her yıl ocakta ilan eder (güncel oranı teyit et) | TTK m. 1530/2, 1530/5-7 |
| Temerrüt ve faiz | Belirli vade gününün geçmesiyle temerrüt; ticari işlerde faiz oranı serbest; sözleşmede oran yoksa kanuni/avans oranı (TCMB'ye bağlı, 3095 m. 1 7589 s.K. ile 2026'da değişti — güncel oranı teyit et). Sözleşmesel temerrüt faizi sınırının (TBK m. 120/2) tacirler arasında uygulanıp uygulanmadığı **tartışmalı** | TBK m. 117/2, 120; TTK m. 8/1; 3095 m. 1-2 |
| Döviz | "Aynen ödeme" kaydı yoksa TL ile ödenebilir; iki Türkiye yerleşiği arasında döviz bedel için 32 sayılı Karar mevzuatını ayrıca çek | TBK m. 99 |
| Fesih ve temerrüt | İfasına başlanmış sürekli edimli sözleşmede borçlu temerrüdünde alacaklı feshedip erken sona ermeden doğan zararını isteyebilir | TBK m. 126 |
| Fesih / ihtar bildirimi | Tacirler arasında temerrüt, fesih, dönme ihbarları noter, taahhütlü mektup, telgraf ya da güvenli e-imzalı KEP ile | TTK m. 18/3 |
| Mücbir sebep | Kanunda tanım yok: borçlunun sorumlu olmadığı imkânsızlıkta borç sona erer, gecikmeksizin bildirim yükümlülüğü var; öngörülemeyen olağanüstü durumda uyarlama, olmazsa dönme/fesih. Sözleşmede olay listesi, bildirim süresi, askı ve fesih eşiği ara | TBK m. 136, 138 |
| Alacağın devri / sözleşmenin devri | Sözleşmeyle devir yasaklanabilir (yasak içermeyen yazılı borç tanımasına güvenen devralan hariç); devir yazılı. Sözleşmenin devri üç taraflı ya da diğer tarafın önceden izni/onayıyla; devredilen sözleşmenin şekline tabi. "Kontrol değişikliği" kanunda yok — sözleşmede ara | TBK m. 183, 184, 205 |
| Tazmin (indemnity) | Türk hukukunda kanuni karşılığı yok; sözleşmesel tazmin taahhüdü ya da üçüncü kişinin fiilini üstlenme olarak nitelendirilebilir — **tartışmalı**. Kapsam, bildirim süresi, savunmanın yönetimi, sulh yetkisi, tavanla ilişki açık yazılmalı; tazmin edilenin kendi ağır kusurunu kapsayan kayıt TBK m. 115/1 riski taşır | TBK m. 128, 115 |
| Fikrî haklar / teslim edilenler | Bilgisayar programı eserdir. İşçilerin işlerini görürken meydana getirdiği eserdeki haklar işverence kullanılır → hak önce tedarikçide toplanır, müşteriye ancak devirle geçer. Mali hak devri/ruhsatı yazılı olmalı ve haklar ayrı ayrı gösterilmeli; henüz meydana getirilmemiş eser üzerindeki tasarruf batıl, ama devir taahhüdü geçerli → "teslimde devreder ve devri teslim tutanağıyla teyit eder" kurgusu; gelecekteki tüm eserlere ilişkin taahhüt 1 yıl önceden ihbarla feshedilebilir | FSEK m. 2/1-1, 18/2, 48, 50, 52 |
| Zamanaşımı | Genel 10 yıl; dönemsel edimler, vekâlet ve (ağır kusur hariç) eser sözleşmesi alacakları 5 yıl; süreler sözleşmeyle değiştirilemez | TBK m. 146, 147, 148 |
| Matbu koşullar | Tedarikçinin tek başına hazırlayıp sunduğu koşullar GİK: bilgilendirme + kabul yoksa yazılmamış sayılır, belirsizlik düzenleyen aleyhine, tek yanlı değiştirme yetkisi yazılmamış, dürüstlüğe aykırı aleyhe hüküm konulamaz | TBK m. 20-25 |
| Yetki / tahkim | Yetki sözleşmesi yalnız tacirler ya da kamu tüzel kişileri arasında, yazılı, ilişki belirli/belirlenebilir; tahkim yazılı. Yabancılık unsuru varsa milletlerarası tahkim (MTK) ve yabancı mahkeme yetkisi (MÖHUK m. 47) → `/commercial-legal:governing-law-review` | HMK m. 17-18, 407, 412; MTK m. 1-2, 4; MÖHUK m. 24, 47 |
| Arabuluculuk | Ticari davalarda para alacağı, tazminat, itirazın iptali, menfi tespit ve istirdat davalarında dava şartı; "önce müzakere, sonra dava" kaydı bunun yerine geçmez | TTK m. 5/A |
| İmza ve teminat | Güvenli e-imza ıslak imzayla eşdeğer; resmî şekle tabi işlemler ve (banka teminat mektubu ile yerleşik sigorta şirketinin kefalet senedi dışındaki) teminat sözleşmeleri güvenli e-imzayla yapılamaz → ana şirket garantisi/kefalet varsa ıslak imza ve kefalete özgü şekil şartlarını ayrıca çek | 5070 m. 5 |
| Dil | Türk şirketleri Türkiye'deki sözleşmelerini Türkçe tutmakla yükümlü; yabancı şirket için yükümlülük Türk kuruluşlarla ilişkisine özgü. Yalnız yabancı dildeki sözleşmenin sonucu **tartışmalı — içtihadı kontrol et** → iki dilli metin ve "Türkçe metin esastır" ya da en az Türkçe nüsha öner | 805 m. 1-2 |
| Kişisel veri | Veri işleyen sözleşmesi, güvenlik ve yurt dışı aktarım bu skill'in konusu değil | → `/privacy-legal:dpa-review` |
| Damga vergisi | Oran ve tutar yazma; nüsha, imza yeri, tutarın belirlenmesi (profilde `#### Stamp duty` varsa ona göre) | → `/tax-legal` skill'leri |

#### Sorumluluk tavanı karar prosedürü

**Tavan tutarı tavanın en önemsiz parçasıdır.** Tek satırlık "tavanı playbook'la karşılaştır" yazma; dört boyutu bulguda açıkça yaz:

1. **Doğrudan / dolaylı zarar.** Tavan tüm sorumluluğa mı, yalnız doğrudan zarara mı? Doğrudan zararda 12 aylık tavan + tavansız dolaylı zarar ile 12 aylık toplam tavan bambaşka pozisyonlardır. Türk hukukunda "dolaylı zarar"ın kanuni tanımı olmadığından istisna edilen kalemlerin sayılıp sayılmadığını ayrıca yaz.
2. **Tavan tabanı — birebir alıntıla.** "12 aylık tavan" şunlardan biri olabilir: (a) talepten önceki 12 ayda ödenen bedel, (b) içinde bulunulan 12 aylık dönemde ödenecek bedel, (c) son 12 aylık kullanım bedeli, (d) güncel sipariş formu bedeli, (e) bugüne kadar ödenen toplam. Belirsizse: "Tavan tabanı belirsiz — `[alıntı]` — [X] ya da [Y] anlamına gelebilir. İmzadan önce teyit edin." Döviz cinsinden tavanda kur ve tarih.
3. **Tavan–istisna etkileşimi.** Veri ihlali, fikrî hak tazmini ve gizlilik tavansızsa, gerçek uyuşmazlıklar bakımından sözleşme fiilen tavansızdır. Tavanın ÜSTÜNDE kalanları (istisnalar), ALTINDA kalanları sırala ve tavanlı alanın anlamlı mı göstermelik mi olduğunu yaz. Kast ve ağır kusur her hâlükârda tavan dışında kalır (TBK m. 115/1) — bunu playbook "istisnası" gibi sayma.
4. **Boyut başına playbook.** Profil şu pozisyonları tutmalı: doğrudan tavan (bedelin katı), dolaylı zarar (hariç / tavanlı / tavansız), tavan üstü kabul edilebilir istisnalar, kabul edilebilir tavan tabanı. Tek bir "standart pozisyon" varsa not et: "Playbook'unuzda tek tavan pozisyonu var — doğrudan/dolaylı/istisna/taban olarak bölmeyi düşünün."

#### Yargı çevresi farkı

Playbook tek bir hukuk tercihini her yere uygular; geçerlilik hukuka göre değişir. Sözleşme Türk hukuku dışında bir hukuka tabiyse yukarıdaki tablo o hukuka aktarılamaz. Kural ezberden yazılmaz; araçla çekilir ve `/commercial-legal:governing-law-review` ile derinleştirilir:
- İngiltere: `uk_search_legislation(query="Unfair Contract Terms Act 1977")` → `uk_get_section`
- Almanya: `de_gesetz_ara` / `de_norm_getir` (ör. BGB § 307 standart şart denetimi)
- AB: `eu_search_eu_law(query="late payment in commercial transactions")`
- Hollanda `nl_`, Polonya `pl_`, Avusturya `at_`, İrlanda `ie_`, Finlandiya `fi_`, İspanya `es_`, Japonya `jp_`, Azerbaycan `az_`
- ABD: yalnız kuruluysa üçüncü taraf CourtListener bağlayıcısı (`courtlistener-rehberi.md`)
- Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

Çektiğin kurala araç etiketi koy (`[ArthurLegal UK — … — GG.AA.YYYY]`); çekemediğini "UYARI: veri çekilemedi, teyidiniz gerekli: <aracın source_url'si ya da resmî giriş sayfası>" diye bırak. Karar Türkiye'de icra edilecekse (yabancı mahkeme ya da hakem kararı) bunu da işaretle → governing-law-review Adım 5.

### Adım 4: Lehte şartlar ve eksikler

**Standardımızdan iyi:** tedarikçinin istediğimizden fazlasını verdiği şartlar — başka yerde taviz gerekirse pazarlık malzemesi.
**Hiç yok:** sık eksikler — devir yasağı, denetim hakkı, mücbir sebep, sigorta, kişisel veri eki, TTK m. 18/3'e uygun tebligat/KEP adresleri, Türkçe esas metin, arabuluculuk ve yetki düzeni.

### Adım 5: Onay yönlendirmesi

Eklenti ayarındaki eskalasyon matrisini sözleşme bedeli, 🔴 sorunların varlığı ve otomatik eskalasyon tetikleyicilerine (sınırsız sorumluluk, fikrî hak devri vb.) karşı kontrol et:

```markdown
## Onay yönlendirmesi

[Bedel / ciddiyet]'e göre bu sözleşme şunları gerektirir:
- [ ] **[İsim/rol]** onayı — [neden]
- [ ] **İş birimi sahibi** onayı — [tartması gereken ticari şart]

**Önerilen sonraki adım:** [Redline'ı karşı tarafa gönder | Cevaptan önce GC'ye eskalasyon | Hukuk cevap vermeden önce X ticari şartı için iş biriminin görüşünü al]
```

**Redline'ı karşı tarafa göndermeden önce** `## Who's using this` oku. Rol avukat değilse:

> Redline göndermek hukuki bir adımdır — karşı taraf her değişikliği müzakere pozisyonumuz sayar. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz bir sayfalık özet: karşı taraf, sözleşme türü, önerilen redline'lar ve arkalarındaki playbook pozisyonları, geri çekilme pozisyonları, paket çıkmadan avukata sorulacaklar. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan geçme.

## Redline inceliği

Redline müzakere belgesidir, yeniden yazım değil. Toptan madde değişikliği "yazdığınızı çöpe attık" der, karşı tarafı tüm maddeyi yeniden okumaya zorlar ve iyi kısımları da atar. En küçük düzeltme: kelime → ifade ("Alıcı tarafından ödenen" → "Alıcı tarafından ödenen ve ödenecek") → alt bent ((a)/(b) ile ayır) → cümle → ancak gerekirse tüm madde; o durumda ileti notunda söyle: "8.2'yi değişiklikler kapsamlı olduğu için işaretlemek yerine yeniden yazdık; farkı birlikte geçebiliriz." Şüphede, daha küçük.

### Adım 6: Notu derle

Başa eklenti ayarı `## Outputs` → üst başlığı koy (role göre). Not ve sözleşme gizli olabilir; çıktı kaynağın statüsünü devralır. Yalnız dar çevrede dağıt; dışa giden teslimlerde (karşı taraf redline'ı, iş birimi özeti) başlığı çıkar. Başlık tek başına koruma yaratmaz.

Uygulanan pozisyonlar eklenti ayarındaki `Governing law and venue`'ya göredir; farklı hukuk ya da hukuk seçimi sorusu varsa notta işaretle.

- **Sessiz tamamlama yok:** Araç gereken bir kural için az sonuç dönerse dur: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle."
- **Kaynak etiketi:** `[ArthurLegal TR — 6098 m. X — GG.AA.YYYY]`, `[web — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`; `doğrula` etiketliler önce kontrol edilir; etiketleri silme.

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# Tedarikçi Sözleşmesi İncelemesi: [Karşı taraf] [Sözleşme türü]

**İnceleme:** [GG.AA.YYYY]   **Bedel:** [tutar ve para birimi] / [süre]   **Rolümüz:** [Müşteri / Tedarikçi]
**Playbook:** [Satış / Alım tarafı]   **Taraflar:** [tacir–tacir]   **Nitelik:** [eser / vekâlet / karma]   **Hukuk / yargı yeri:** [...]

## ⚠️ İnceleyen notu
- **Kaynaklar:** ArthurLegal MCP (`tr_`) — [madde sayısı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]
- **Eksik belge:** [sipariş formu / veri eki (atıfla, okunmadı) / yok]

## Sonuç
[İki cümle: imzalanabilir mi, önce ne değişmeli?]
**Sorunlar (hukuki risk):** [N]🔴 [N]🟠 [N]🟡 [N]🟢
**Sorunlar (iş sürtünmesi):** [N]🔴 [N]🟠 [N]🟡 [N]🟢
**Onay:** [isim]

## Anlaşma bozucu kontrolü
[✅ Temiz | ⛔ Var — yukarıda]

## Ciddiyete göre sorunlar
[Adım 3 blokları, Kritik → Düşük]

## Lehte şartlar
## Eksik hükümler
## Onay yönlendirmesi
## Redline paketi
[İstenirse: tüm değişiklikler için işaretlemeye hazır toplu metin — iç gerekçe olmadan]
```

## Entegrasyonlar

**[CLM]** bağlıysa: karşı tarafla önceki sözleşmelere bak ("geçen sefer 24 aylık tavan verdik"); bu türe uyan iş akışı şablonunu çek; not ekli ve onaylayıcıları atanmış kayıt aç.

**E-imza (DocuSign vb.)** bağlıysa ve sözleşme imzaya hazırsa zarf oluşturmayı ve imzacıları matris sırasına göre yönlendirmeyi öner. Açık talimat olmadan hiçbir şeyi imzaya gönderme; "imzaya hazır" kararı avukatındır. Platformun imzası güvenli e-imza değilse (5070 m. 5) bunu ve teminat sözleşmesi varsa ıslak imza gereğini not et.

**Zarf oluşturmadan ya da karşı imzaya yönlendirmeden önce** `## Who's using this` oku. Rol avukat değilse:

> Bu adımın hukuki sonucu var: imza şirketi sözleşmenin tamamına bağlar. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: karşı taraf, bedel, bulunan sorunlar ve nasıl çözüldükleri, avukatın kabul ettiği riskler, zarf çıkmadan sorulacaklar. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan geçme.

## Çıktı biçimleri

- **Tam not (varsayılan):** yukarıdaki gibi; [CLM] kaydına ya da `## House style` klasörüne.
- **Kanal özeti:** iki satır ve bağlantı — `[Karşı taraf] [tür] — DÜZELTME GEREKLİ. 1🔴 (sınırsız sorumluluk m. 8.2), 2🟠. Tam inceleme: [bağlantı]. [GC] onayı gerekli.`
- **Redline belgesi:** istenirse izlenen değişikliklerle .docx (docx skill'i); her değişikliğin yorumu playbook pozisyonuna atıf yapar.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["99","112","114","115","116","117","120","126","128","136"])   ← en çok 10 madde/çağrı; kalanlar (138, 146-148, 179-184, 205, 20-25, 470, 484, 502, 512) ayrı çağrılarla
tr_mevzuat_madde_getir(number="6102", madde_no=["3","5/A","8","18","22","1530"], max_chars_per_article=6000)
tr_mevzuat_madde_getir(number="5846", madde_no=["2","18","48","50","52"])
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="sorumluluğun sınırlandırılması ağır kusur dolaylı zarar", date_from="2020-01-01")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="yabancı dilde düzenlenen sözleşme 805 sayılı Kanun")
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".

## Teslim öncesi kalite kontrolü

- [ ] Eklenti ayarı yüklendi ve alıntılandı (genel piyasa pozisyonu değil); anlaşma bozucu önce kontrol edildi
- [ ] Emredici sınırlar tablosu tarandı, atıflar araçtan; tartışmalı noktalar inceleyen notunda
- [ ] Her sorunun somut redline metni var; ciddiyetler kalibre (her şey Kritik değil)
- [ ] Onaylayıcı adıyla yazıldı; karşı taraf bağlamı (büyük kurumsal / girişim) gözetildi

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu incelemeye göre uyarla (redline'ı taslakla, eskalasyon, ek olgu iste, bekle, diğer). Ağaç çıktıdır; seçimi avukat yapar.
