---
name: commercial-legal-stakeholder-summary
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

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:commercial-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

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
