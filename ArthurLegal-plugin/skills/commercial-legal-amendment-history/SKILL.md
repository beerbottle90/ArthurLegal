---
name: commercial-legal-amendment-history
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
/arthurlegal:commercial-legal-amendment-history ana-sozlesme.pdf ek-protokol-1.pdf ek-protokol-2.pdf
/arthurlegal:commercial-legal-amendment-history --provision tazmin
```

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:commercial-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

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
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/arthurlegal:legal-research-az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/arthurlegal:legal-research-sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
