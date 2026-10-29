---
name: ip-legal-takedown
description: >
  İnternetteki telif ihlali için içerik kaldırma: bilgi içerik sağlayıcısına
  başvuru ve ihlal sürerse Cumhuriyet savcısı aracılığıyla servisin durdurulması
  (FSEK ek m. 4/3), uyarı yöntemi (5651 m. 2/1-r) ve platform bildirimi (--send);
  size gelen kaldırma talebinin triyajı (--respond); içeriğiniz kaldırıldıysa
  itiraz ya da karşı bildirim taslağı (--counter). ABD DMCA mekanizmasının
  yerini alır; yabancı platform ve AB DSA notları araca yönlendirilir.
argument-hint: "<--send | --respond | --counter> [bağlam ya da gelen bildirimin yolu]"
---

# /takedown — İçerik kaldırma (telif)

- `/arthurlegal:ip-legal-takedown --send` — FSEK ek m. 4/3 başvurusu ve platform bildirimi; istisna kapısı + teslimden önce kapı.
- `/arthurlegal:ip-legal-takedown --respond` — size gelen kaldırma talebini triyaj: uy / itiraz et / görüş / bırak.
- `/arthurlegal:ip-legal-takedown --counter` — içeriğiniz kaldırıldıysa itiraz ya da karşı bildirim; teslimden önce kapı.
- Bayrak yoksa bir kez sor: "Kaldırma talebi mi gönderiyoruz, gelen bir talebi mi değerlendiriyoruz, yoksa kaldırılan içeriğimiz için itiraz mı hazırlıyoruz?"

## Talimat

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Yoksa ya da `[PLACEHOLDER]` varsa dur: "Önce `/arthurlegal:ip-legal-cold-start-interview` çalıştırın — bu skill onay matrisinize ve pratik profilinize dayanır."
2. **Matter:** `## Matter workspaces` → `Enabled` `✗` ise atla; açık ve aktif matter yoksa sor ("`/arthurlegal:ip-legal-matter-workspace switch <slug>` ya da `practice-level`"). Çıktılar `matters/<matter-slug>/takedown/<slug>/` (uygulama düzeyinde `takedown/<slug>/`); `Cross-matter context` `on` değilse başka matter okunmaz.
3. **Bağlam:** `## IP practice profile`, `## Enforcement posture` → `Approval matrix` → `DMCA takedown (ordinary)` satırı (Türkiye'de bu satır her türlü içerik kaldırma bildirimini kapsar — FSEK ek m. 4 başvurusu, platform bildirimi, yabancı DMCA bildirimi; satır adı çevrilmez), `## Who's using this`, `## Outputs`.
4. **Kapılar:** `--send` ve `--counter`'da teslimden önce kapı her seferinde çalışır. `--send`'deki istisna kapısı daha önce çalışır; kullanım bir kanuni istisnaya "olabilir" ya da "muhtemelen" giriyorsa taslağı durdur, avukata yönlendir.
5. **Yargı çevresi:** içerik, platform ya da ihlal eden Türkiye dışındaysa taslaktan önce işaretle (aşağıda "Yabancı platform ve AB").

## Destination check

Giden bildirim ve itiraz karşı tarafa/platforma gider; üst başlık taşımaz ve bir hukuki süreç içindeki beyandır, gizli değildir. İç taslak, istisna analizi ve triyaj notu `## Outputs` üst başlığını taşır. Platform formuna yapıştırılan metin çoğu zaman karşı tarafa iletilir — kişisel veri ve strateji içermesin. Kanonik kural: `## Shared guardrails → Destination check`.

## Türk hukuku çerçevesi

**ABD'deki tek kanunlu "notice-and-takedown" (DMCA §512) sisteminin Türkiye'de birebir karşılığı yoktur.** Yollar:

1. **FSEK ek m. 4/3 — telifin kanuni yolu.** Servis ve bilgi içerik sağlayıcılar tarafından dijital iletim dahil araçlarla eser sahibi ya da bağlantılı hak sahibinin hakları ihlal edilirse, hak sahibinin başvurusu üzerine eser içerikten çıkarılır:
   - **Aşama 1:** hakkı zedelenen kişi önce **bilgi içerik sağlayıcısına** başvurur ve **üç gün** içinde ihlalin durdurulmasını ister.
   - **Aşama 2:** ihlal devam ederse **Cumhuriyet savcısına** başvurulur; savcılık üzerinden **servis sağlayıcıdan**, ihlale devam eden içerik sağlayıcıya verilen hizmetin üç gün içinde durdurulması istenir. İhlal durunca hizmet yeniden verilir. Uygulama ayrıntıları Bakanlık yönetmeliğindedir — güncel yönetmeliği `tr_mevzuat_ara(query="fikir ve sanat eserleri", search_in="title")` ile bul (yönetmelik türü KKY ya da YONETMELIK olabilir) ve çek.
   - Ek m. 4/1'deki hak yönetim bilgisini kaldırma fiilleri ile hakları ihlale devam eden bilgi içerik sağlayıcılar için ayrıca ceza hükmü vardır (FSEK m. 71 son fıkralar); şikâyete bağlıdır (m. 75), şikâyet süresi altı ay (TCK m. 73).
2. **5651 — uyarı yöntemi ve sağlayıcı sorumluluğu.** Kanun "uyarı yöntemi"ni tanımlar: hakkı ihlal edildiğini iddia eden kişi içeriğin yayından çıkarılması için önce içerik sağlayıcıya, makul sürede sonuç alınamazsa yer sağlayıcıya iletişim adresleri üzerinden bildirimde bulunur (5651 m. 2/1-r). İçerik sağlayıcı sunduğu içerikten sorumludur (m. 4/1); yer sağlayıcı içeriği kontrol etmek ya da araştırmakla yükümlü değildir (m. 5/1) ve yayından çıkarma yükümlülüğü m. 8 ve 9'a göre haberdar edilmesine bağlanmıştır (m. 5/2).
   - **Dikkat:** 5651 m. 9 Anayasa Mahkemesi kararıyla **iptal edilmiştir** (madde metnindeki not: AYM 11/10/2023, E. 2020/76, K. 2023/172) — yürürlükte gibi atıf yapma. Telif ihlali için yer sağlayıcıya 5651'den doğrudan yükümlülük yükleme; telifte dayanak FSEK ek m. 4'tür.
   - Özel hayatın gizliliği ihlalinde ayrı yol vardır (5651 m. 9/A: Siber Güvenlik Başkanlığına başvuru, sulh ceza hâkimi onayı) — telif yolu değildir.
   - **Sosyal ağ sağlayıcının 48 saatlik cevap yükümlülüğü (ek m. 4/3).** Türkiye'den günlük erişimi bir milyonu aşan yurt içi ya da yurt dışı kaynaklı sosyal ağ sağlayıcı, kişilerin başvurusuna başvurudan itibaren en geç **48 saat** içinde olumlu ya da olumsuz cevap verir; olumsuz cevap gerekçeli olur. Kapsam tarihe göre değişir — başvuru tarihine bak:
     - **31.10.2026'ya kadar:** yükümlülük yalnız m. 9 ve 9/A kapsamındaki içeriklere ilişkin başvurular içindir; telif bildirimi bu kapsamda değildir. m. 9 iptal edildiğinden yollamanın kapsamı **tartışmalı**.
     - **1.11.2026'dan itibaren:** 7578 sayılı Kanunun 22. maddesi "9 uncu ve 9/A maddeleri kapsamındaki içeriklere yönelik olarak" ibaresini çıkarır (yürürlük: aynı Kanun m. 27/1-a, yayımdan altı ay sonra; RG 1/5/2026, sayı 33240). Lafzen kişilerin her başvurusu kapsama girer; büyük bir sosyal ağa yapılan telif bildirimine de 48 saat içinde, olumsuzsa gerekçeli cevap beklenebilir. Uygulama henüz oluşmadı: **tartışmalı — Başkanlık düzenlemesini ve içtihadı kontrol et.** Başvurunun tarih ve saatini kayda geçir; süre başvurudan işler.
   - **Yeniden yayının önlenmesi (1.11.2026'dan itibaren, ek m. 4'e eklenen 23. fıkra):** günlük erişimi on milyonu aşan sosyal ağ sağlayıcı, 5651 uyarınca verilen içeriğin çıkarılması ve/veya erişimin engellenmesi kararlarına konu yayının kendi sitesinde yayınlanmaması için gerekli tedbirleri alır. Yalnız 5651 kapsamında verilmiş kararlar içindir; FSEK ek m. 4 yoluyla kaldırılan içerik için dayanak sayma.
   - **Oyun platformları (yeni ek m. 5, 1.11.2026'dan itibaren):** Türkiye'den günlük erişimi yüz bini aşan yurt dışı kaynaklı oyun platformu Türkiye'de gerçek ya da tüzel kişi temsilci belirler ve iletişim bilgilerini sitesinde yayımlar (ek m. 5/2). Oyun içindeki ihlalde bildirimi platformun formuna ek olarak bu temsilciye de gönder.
   - 1.11.2026'dan sonra ek m. 4 ve ek m. 5'in işlenmiş metnini `tr_mevzuat_madde_getir(number="5651", madde_no=["ek 4", "ek 5"])` ile çek: ek m. 4'te on dokuzuncu fıkradan sonra dört fıkra eklendiği için sonraki fıkraların numarası değişti. Mevzuat Bilgi Sistemi değişikliği o gün işler; işlenmemişse 7578 sayılı Kanunun 22 ve 23. maddelerini çek.
3. **Mahkeme yolu:** ihtiyati tedbir (FSEK m. 77; dava açılmadan önce de), tecavüzün ref'i (m. 66) ve men'i (m. 69), tazminat (m. 68, 70); görevli mahkeme FSHHM (FSEK m. 76/1).
4. **Platform bildirimi (uygulama):** pazaryeri, video ve sosyal ağ platformlarının kendi telif/IP formları. Hukuki dayanak değil, kullanım koşulu sürecidir; çoğu zaman en hızlı yoldur ve FSEK ek m. 4 yoluna paralel yürür.

Her madde atfı `tr_mevzuat_madde_getir` ile çekilir (5846 ek 4: `madde_no="ek 4"`; 5651: `madde_no=["2","4","5","ek 4"]`, 1.11.2026'dan sonra `"ek 5"` de). İçtihat: `tr_ictihat_ara(courts=["YARGITAYKARARI"], query="+FSEK +\"ek 4\" +içerik")` — dönen künyeyi birebir kullan.

## Gönderme modu (--send)

### Adım 1: Eser ve hak

> - **Eser:** nedir (yazılım, görsel, metin, video, ses)? Sahibinin hususiyetini taşıyor mu (FSEK m. 1/B-a)?
> - **Sahiplik:** kim meydana getirdi (m. 8)? Çalışan eseriyse haklar kural olarak işverence kullanılır (m. 18/2) — sözleşmeyi kontrol et. Devralındıysa sözleşme yazılı ve haklar ayrı ayrı gösterilmiş mi (m. 52)?
> - **Başvuru yetkisi:** ek m. 4/3 başvuruyu "hakları haleldar olan" kişiye tanır. Münhasır olmayan ruhsat sahibinin başvurup başvuramayacağı **tartışmalı** — lisans sözleşmesine bak; şüphede hak sahibinden yetki ya da ortak başvuru al.
> - **Önceki izinler:** bu kullanıma ya da daha genişine hiç izin, lisans (Creative Commons dahil) verildi mi?

Kayıt-tescil şart değildir; varsa ispatı kolaylaştırır (m. 13/son).

### Adım 2: İhlal eden içerik ve yeri

Platform/site · tam URL'ler (her içerik için kalıcı bağlantı) · içerik sağlayıcı kim (5651 m. 2/1-f), yer sağlayıcı kim (m. 2/1-m) · nasıl ihlal ediyor (birebir kopya, işleme, izinsiz umuma iletim — FSEK m. 21-25) · delil: URL ve zaman görünür ekran görüntüleri; içerik kaybolabilecekse delil tespiti (HMK m. 400).

### Adım 3: İstisna kapısı (ABD "fair use" kapısının yerine)

Türk hukukunda ABD'deki gibi genel ve esnek bir "fair use" ölçütü yoktur; serbest kullanımlar FSEK'te tek tek düzenlenmiştir. Taslaktan önce sor:

> Bu kullanım bir kanuni istisnaya giriyor olabilir mi?
> - **İktibas** (m. 35): alenileşmiş eserden cümle/fıkra alıntısı, ilim eserinde aydınlatma amaçlı alıntı — iktibas belli olmalı, kaynak gösterilmeli.
> - **Eğitim** (m. 33 yüz yüze eğitimde kâr amaçsız temsil; m. 34 eğitim amaçlı seçme ve toplama eserler).
> - **Şahsi kullanım** (m. 38/1: kâr amaçsız şahsen kullanmaya mahsus çoğaltma — hak sahibinin meşru menfaatine haklı sebepsiz zarar vermemek ve normal yararlanmaya aykırı olmamak şartıyla).
> - **Bilgisayar programında kullanıcı hakları** (m. 38/3-7: amaca uygun kullanım, yedek kopya, gözlem-tetkik, araişlerlik).
> Değerlendirmeniz: istisna **olası değil / tartışmalı / olası**?

Cevabı dosyaya yaz. **Tartışmalı ya da olası ise taslak yazma:** "Bu olgularda istisna tartışmalı. Kanunen serbest bir kullanıma kaldırma talebi göndermek, aşağıdaki kapıdaki sorumlulukları doğurur. Önce avukata." İstisnaların kapsamının yorumu **tartışmalı — içtihadı kontrol et.**

### Adım 4: İyiniyet kontrolü

Dört soru, dördü de evet olmalı: eser bizim ya da başvuru yetkimiz var · kullanım izinli değil (lisanslar, izinler, CC lisansı kontrol edildi) · istisna kapısı yürütüldü ve sonucu kayıtta · içerik doğrudan incelendi (yalnız bir ihbara dayanılmadı). Biri hayırsa dur.

### Adım 5: Yetki ve imza

Kim kimin adına başvuruyor, yetki belgesi (vekâletname, yetki yazısı) var mı?

### Adım 6: Taslak

**Aşama 1 — içerik sağlayıcıya başvuru (FSEK ek m. 4/3) ve uyarı yöntemi bildirimi:**
1. Başvuranın kimliği ve iletişim bilgisi (vekil varsa vekâlet)
2. Eserin tanımı ve hak dayanağı (sahiplik/devir/ruhsat; tescil varsa numara)
3. İhlal eden içerik: URL'ler, kısa tarif, nasıl ihlal ettiği
4. Talep: ihlalin **üç gün** içinde durdurulması ve içeriğin yayından çıkarılması
5. Beyan: bilgilerin doğru olduğu ve başvuranın hak sahibi ya da onun adına yetkili olduğu
6. Tarih, imza
Kanal: içerik sağlayıcının iletişim adresi, KEP ya da noter (tarih ispatı); platform kullanıyorsa platformun formu paralel. Sonuç alınamazsa yer sağlayıcıya aynı içerikle bildirim (5651 m. 2/1-r).

**Aşama 2 — Cumhuriyet savcılığına başvuru** (ihlal sürerse): Aşama 1 başvurusu ve tebliğ belgesi, sürenin dolduğu, ihlalin devam ettiğine dair güncel delil, servis sağlayıcıdan hizmetin durdurulması talebi. Ceza şikâyeti de yapılacaksa bunu ayrı ve açık yaz; süre altı ay (TCK m. 73).

### Adım 7: Teslimden önce kapı

```
┌─────────────────────────────────────────────────────────────┐
│  BU KALDIRMA TALEBİ BİR YERE GİTMEDEN ÖNCE                   │
├─────────────────────────────────────────────────────────────┤
│  Kaldırma talebi yargı denetimi olmadan içerik indirtebilir; │
│  rutin bir idari adım değildir:                              │
│  • Savcılığa, işlenmediğini bildiği bir ihlali isnat etmek   │
│    iftira suçunu oluşturabilir (TCK m. 267).                 │
│  • Lisanslı, başkasına ait ya da kanunen serbest kullanıma   │
│    karşı talep: kötüleme/haksız rekabet (TTK m. 55/1-a-1,    │
│    56), hakkın kötüye kullanılması (TMK m. 2), tedbir        │
│    alınırsa haksız tedbir tazminatı (HMK m. 399).            │
│  Gitmeden önce teyit edin:                                   │
│    1. Eser bizim ya da başvuru yetkimiz var.                 │
│    2. Kullanım izinli değil — lisanslar ve izinler tarandı.  │
│    3. İstisna kapısı yürütüldü; sonuç kayıtta.               │
│    4. İmza yetkisi olan kişi gönderimi onayladı.             │
│  Onaylayan: [Approval matrix → DMCA takedown (ordinary)]     │
│  Otomatik eskalasyonlar: [profilden]                         │
└─────────────────────────────────────────────────────────────┘
```

Kullanıcı avukat değilse ekle: "Kaldırma talebi, özellikle savcılık aşaması, sorumluluk doğurur. Hukuki mütalaa ve takip avukatlara aittir (Av.K. m. 35/1). Bir avukatla gözden geçirdiniz mi? Görüşme için kısa brif: [eser, sahiplik, ihlal eden kullanım, lisans kontrolü, istisna analizi, imzalayan, platform]. Avukat bulmak için ilinizin barosuna başvurabilirsiniz." Kapıyla açık etkileşim olmadan nihai çıktıyı yazma.

### Adım 8: Çıktı

- **Asıl:** `<matter-klasörü>/takedown/<slug>/notice-v<N>.md` (platform formuna yapıştırmaya ya da KEP/noter ile göndermeye hazır metin; hangi kanalın beklendiğini yaz). Önce sohbette düz metin.
- **İnceleyen notu** (yalnız sohbette): "⚠️ Bu, avukat incelemesi için kaldırma talebi taslağıdır; gönderilmeye hazır değildir."
- **Atıf etiketleri:** `[ArthurLegal TR — 5846 FSEK ek m. 4 — GG.AA.YYYY]`, `[kullanıcı verdi]`, `[model bilgisi — doğrula]`; sessiz tamamlama yok.
- **Gönderim kaydı** `submission.md`: kanal (adres, form, KEP/noter), tarih, onay numarası, hedef URL'ler, **üç günlük süre sonu**, Aşama 2 hazırlığı, delil koruma.

## Alma modu (--respond) — size gelen talebin triyajı

### Adım 1: Oku

Gönderen (kim, imzalayan, iletişim) · hangi mekanizma: içerik sağlayıcı olarak size doğrudan FSEK ek m. 4 başvurusu mu, savcılık yazısı mı, hâkim kararı mı, platformun kendi süreci mi, yabancı platformda DMCA bildirimi mi · iddia edilen eser · hedef içeriğiniz (URL) · tarih · bildirimde eksik var mı (eser, URL, hak dayanağı, yetki).

### Adım 2: Değerlendir

Lisansımız var mı (sözleşme, CC, önceki uzlaşma, devir)? Kanuni istisna (m. 33-35, 38)? Gönderen gerçekten hak sahibi mi? Bildirim eksik mi? Savcılık ya da hâkim kararıysa — usul ve itiraz yolu avukatındır; süreleri hemen çıkar. Gönderen aşırı ve toplu talep gönderen biri mi?

### Adım 3: Seçenekler

- **A — Uy (kaldırma kalsın):** haklılar ya da değmez. Bedel: içerik kapalı kalır, hesap uyarıları, gelir kaybı. Adım: kaydet.
- **B — İtiraz / karşı bildirim:** lisans, istisna ya da hak sahipliği itirazı güçlü. Adım: `/arthurlegal:ip-legal-takedown --counter`.
- **C — Gönderenle görüş:** lisans, atıf, daha dar kaldırma. İçerik görüşme sürerken kapalı kalabilir. Uzlaşma yazışmalarında başlık tek başına koruma sağlamaz.
- **D — Bırak, ayrıca ele al:** zarar küçük; talep haksızsa haksız rekabet (TTK m. 55-56) ya da haksız fiil tazminatı kendi takviminizle ayrı uyuşmazlıktır.

Birini iki cümle gerekçeyle öner.

### Adım 4: Triyaj notu

Çıktı: `<matter-klasörü>/takedown/inbound/<slug>/triage.md`.

```markdown
[ÜST BAŞLIK — profil ## Outputs]
[GİZLİLİK BLOĞU — /arthurlegal:ip-legal-cease-desist alma modundaki gibi role göre]
# İçerik Kaldırma Talebi — Triyaj
> **GÖRÜŞ DEĞİL, TRİYAJ.** Esasa ilişkin karar avukatındır.
**Slug:** · **Tarih:** · **Mekanizma:** [FSEK ek m. 4 başvurusu / savcılık / hâkim kararı / platform / yabancı DMCA] · **Platform:** · **Dosya:**
## Talep
**Gönderen:** · **İddia edilen eser:** · **Hedef içeriğimiz:** · **Bildirimdeki eksikler:**
## Değerlendirme
**Lisans/izin:** · **Kanuni istisna (m. 33-35, 38):** `[avukat teyidi]` · **Gönderenin hak sahipliği:** · **Gönderenin güvenilirliği:**
## Seçenekler
### A. Uy ### B. İtiraz / karşı bildirim ### C. Görüş ### D. Bırak
**Öneri:** [harf] — [iki cümle] — `[avukat teyidi gerekli]`
## Süreler
[platformun itiraz süresi; savcılık/hâkim kararına itiraz süresi — avukat belirler; ilgili sözleşme süreleri]
## Hemen yapılacaklar
- [ ] Eser ve içeriğimizle ilgili delil koruma · [ ] İş etkisi (gelir, hesap uyarıları) · [ ] Matter · [ ] Sorumlu avukat
```

Kapanış: "Bu bir triyaj notudur, görüş değildir; bildirimin dört köşesinden ilk okumadır. İtiraz etmeden ya da cevapsız bırakmaya karar vermeden önce avukat değerlendirir."

## İtiraz modu (--counter)

**Türk hukukunda DMCA §512(g) benzeri kanuni bir karşı bildirim mekanizması yoktur.** Bu mod, kaldırmanın türüne göre doğru belgeyi hazırlar:
- **Platform süreciyle kaldırıldıysa:** platformun itiraz formu için itiraz metni.
- **Hak sahibinin doğrudan başvurusuyla (FSEK ek m. 4/3) içeriği siz kaldırdıysanız:** gönderene cevap → `/arthurlegal:ip-legal-cease-desist --send` (cevabi ihtarname).
- **Savcılık ya da hâkim kararıyla kaldırıldıysa:** itiraz yolu ve süresi avukatındır; bu skill yalnız olgu ve delil özetini hazırlar.
- **Uyuşmazlığı kesin çözmek gerekiyorsa:** tecavüz olmadığının tespiti için tespit davası (HMK m. 106) — dış avukata eskale, taslak yok.
- **Yabancı platformda DMCA bildirimiyle kaldırıldıysa:** karşı bildirim ABD hukukudur ve kaynak kitapçığın ABD çerçevesine göre ABD federal mahkemelerinin yargı yetkisine rıza beyanı içerir. ArthurLegal'da ABD mevzuat kaynağı yoktur (kuruluysa CourtListener bağlayıcısı içtihat için); ABD'de yetkili bir avukattan görüş al.

### Adım 1: Ön şartlar

İçerik hangi mekanizmayla kaldırıldı (yukarıdaki dallanma)? Kaldırmanın hata ya da yanlış tespit olduğuna dair iyiniyetli ve delilli bir kanaat var mı (lisans, istisna, ihlal yok, gönderen hak sahibi değil)? Karar bilinçli mi verildi, avukat devrede mi?

### Adım 2: Platform itiraz metni

1. Kimlik ve iletişim · 2. Kaldırılan içerik ve kaldırılmadan önceki URL · 3. Kaldırma bildiriminin tarihi/numarası · 4. Kaldırmanın neden hatalı olduğu ve delili (lisans belgesi, istisna gerekçesi, hak zinciri) · 5. Beyanların doğruluğu beyanı · 6. Tarih, imza.

### Adım 3: Teslimden önce kapı

```
┌─────────────────────────────────────────────────────────────┐
│  BU İTİRAZ BİR YERE GİTMEDEN ÖNCE                            │
├─────────────────────────────────────────────────────────────┤
│  • İtiraz metni ve kimlik bilgileriniz çoğu zaman talebi     │
│    gönderene iletilir.                                       │
│  • İçerik geri gelirse hak sahibi ihtiyati tedbir (FSEK      │
│    m. 77) ve dava yoluna gidebilir; itiraz davadan önceki    │
│    son adımdır.                                              │
│  • Gerçeğe aykırı beyan sorumluluk doğurur.                  │
│  Teyit edin:                                                 │
│    1. Kaldırma mekanizması belirlendi (platform / FSEK ek    │
│       m. 4 / savcılık / hâkim / yabancı DMCA).               │
│    2. Hata kanaati iyiniyetli ve delilli.                    │
│    3. Dava ihtimaline bütçe, avukat ve risk iştahı hazır.    │
│    4. Gönderilmeden önce avukat inceledi.                    │
│  Onaylayan: [Approval matrix — itirazlar genellikle          │
│  DMCA takedown (ordinary) satırının üstüne yönlenir]         │
└─────────────────────────────────────────────────────────────┘
```

Kullanıcı avukat değilse: "Bu adım lisanslı mesleki muhakeme ister (Av.K. m. 35/1); Claude incelemesi bunun yerini tutmaz. Brif: [tek sayfa]. Avukat için ilinizin barosu." Açık etkileşim olmadan çıktıyı yazma.

### Adım 4: Çıktı

`<matter-klasörü>/takedown/<slug>/counter-notice-v<N>.md`; sohbette önce düz metin; inceleyen notu: "⚠️ Avukat incelemesi için itiraz taslağı; gönderilmeye hazır değildir." Gönderim sonrası `counter-submission.md`: platform, tarih, onay no, platformun karar süresi, içerik geri gelirse plan, dava/tedbir gelirse plan.

## Yabancı platform ve AB

- **AB:** çevrim içi platformlarda bildirim ve işlem usulü — `eu_get_document_text(celex="32022R2065")` (Dijital Hizmetler Tüzüğü; bildirim ve işlem, şikâyet sistemi hükümlerini metinden oku); içerik paylaşım platformlarının telif sorumluluğu — `eu_get_document_text(celex="32019L0790")` (Dijital Tek Pazarda Telif Direktifi; ilgili madde ve üye devlet iç hukuku). Kuralı ezberden yazma; metinden alıntıla.
- **Diğer ülkeler:** ArthurLegal'da kaynak varsa ilgili önekle ara (`uk_`, `de_`, `nl_`…); yoksa "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

## Karar duruşu

`## Decision posture on subjective legal calls` gereği: kullanımın istisnaya girip girmediği, hak sahibinin biz olup olmadığı, eserin gerçekten bizim olup olmadığı belirsizse sessizce karar verme. İstisna değerlendirmesi tipik belirsiz karardır; avukata işaretle, etkenleri göster. Varsayımla kaldırma talebi ya da itiraz göndermek tek yönlü kapıdır.

## Bu skill ne yapmaz

- **Göndermez** — kullanıcı platform, KEP, noter ya da savcılık kanalından gönderir.
- **İstisnaya karar vermez** — kanuni istisnaları yürütür, işaretler; avukat karar verir.
- **Kapıyı atlamaz** — `--send` ve `--counter`'da her seferinde çalışır.
- **Atıf uydurmaz** — etiketli ve doğrulanmış; sessiz tamamlama yok.
- **Yabancı rejimi Türk hukuku gibi uygulamaz** — DMCA, DSA ve diğerleri için işaretler ve araca/yerel hukukçuya yönlendirir.
