---
name: firm-operations-kvkk-aydinlatma
description: >
  Müvekkil ilişkisi için KVKK aydınlatma metni ve dahili kontrol: işleme amaçları,
  hukuki sebep eşlemesi (m. 5 / m. 6), aktarım alıcıları, yurt dışı aktarım dayanağı
  (m. 9), VERBİS durumu (m. 16). Açık rıza gerekiyorsa aydınlatmadan ayrı alınır.
user-invocable: true
---

# KVKK Aydınlatma — Müvekkil İlişkisi

## Tetikleyici

- Yeni müvekkil intake. Aydınlatma, kişisel verinin **elde edilmesi sırasında** yapılır (KVKK m. 10).
- İşleme amacı değişti (yeni iş, yeni aktarım): yeni amaç için işlemeden önce ayrıca aydınlat (Tebliğ m. 5/1-b).
- Büro yeni bir bulut, yazılım veya yurt dışı hizmet kullanmaya başladı.

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- KİŞİSEL VERİLERİN KORUNMASI KANUNU (Kanun No. 6698, RG 07.04.2016/29677) m. 5, m. 6, m. 9, m. 10, m. 11, m. 12, m. 16
- AYDINLATMA YÜKÜMLÜLÜĞÜNÜN YERİNE GETİRİLMESİNDE UYULACAK USUL VE ESASLAR HAKKINDA TEBLİĞ (Tebliğ No. 24454, RG 10.03.2018/30356) m. 4, m. 5 — kısaca "Tebliğ"
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36

## Akış

### 1. Veri envanteri (bu iş için)

| Kategori | Örnek | Özel nitelikli mi (m. 6/1) |
|---|---|---|
| Kimlik | ad, TCKN, doğum tarihi | hayır |
| İletişim | adres, telefon, e-posta, KEP | hayır |
| Finans | banka, ücret, makbuz | hayır |
| Hukuki işlem / uyuşmazlık | olay, yazışma, belge | hayır |
| Sağlık | rapor, tıbbi belge | **evet** |
| Ceza mahkûmiyeti ve güvenlik tedbirleri | adli sicil, ceza dosyası | **evet** |
| Dernek, vakıf, sendika üyeliği; biyometrik ve genetik veri | — | **evet** |

### 2. Hukuki sebep eşlemesi

| Amaç | Hukuki sebep |
|---|---|
| Vekâlet ve ücret sözleşmesinin kurulması ve ifası | m. 5/2-c |
| Kanuni yükümlülük (MASAK kimlik tespiti, yalnız kapsamdaki işlerde; serbest meslek makbuzu) | m. 5/2-ç |
| Dava açma, savunma, hakkın korunması | m. 5/2-e |
| Özel nitelikli veri: hakkın tesisi, kullanılması veya korunması için zorunlu | m. 6/3-d |
| Başka şart yoksa | açık rıza (m. 5/1; m. 6/3-a) |

Özel nitelikli veride ayrıca Kurulun belirlediği yeterli önlemler alınır (m. 6/4).

### 3. Aydınlatma metninin asgari içeriği (KVKK m. 10; Tebliğ m. 4)

a) Veri sorumlusunun (büro / avukat) ve varsa temsilcisinin kimliği
b) İşleme amaçları: **belirli, açık, meşru**; "ve benzeri amaçlar" gibi muğlak ifade yok (Tebliğ m. 5/1-g)
c) Aktarım alıcı grupları ve aktarım amacı (Tebliğ m. 5/1-ı): mahkemeler ve icra daireleri, noterler, bilirkişi ve arabulucu, usul gereği karşı taraf ve vekili, mali müşavir, bulut ve yazılım hizmet sağlayıcıları, MASAK (yalnız 5549 kapsamındaki işlerde)
ç) Toplama yöntemi (otomatik / otomatik olmayan; Tebliğ m. 5/1-i) ve hukuki sebep, yani m. 5 veya m. 6'daki hangi şart (Tebliğ m. 5/1-h)
d) m. 11'deki haklar

Dil anlaşılır, açık ve sade olur (Tebliğ m. 5/1-ğ). Eksik, yanıltıcı veya yanlış bilgi yazılmaz (Tebliğ m. 5/1-j).

### 4. Açık rıza gerekiyorsa
Aydınlatma ve açık rıza **ayrı ayrı** alınır (Tebliğ m. 5/1-f). İkisini tek formda, tek imzayla birleştirme.

### 5. Yurt dışı aktarım kontrolü (m. 9)
Büro bulut depolama, e-posta, belge yönetimi, çeviri veya yaptırım taraması için yurt dışındaki bir hizmete kişisel veri gönderiyorsa bu **yurt dışına aktarımdır**:
- Aktarılan ülke veya sektör için yeterlilik kararı var mı (m. 9/1-2)?
- Yoksa uygun güvence: Kurulun ilan ettiği standart sözleşme vb. (m. 9/4). Standart sözleşme imzadan itibaren **beş iş günü** içinde Kuruma bildirilir (m. 9/5).
- İkisi de yoksa yalnız arızi hâllerde aktarım yapılabilir (m. 9/6).

Büronun hangi hizmet için hangi dayanağı kullandığı `firm-profile.md`'de yazmıyorsa **"yurt dışı aktarım dayanağı belirsiz"** diye işaretle ve Yönetici Ortak'a götür. Bu paket belirli bir ülke için yeterlilik kararının varlığını doğrulamadı.

### 6. VERBİS (m. 16)
- Kural: kişisel veri işleyen gerçek ve tüzel kişiler, veri işlemeye başlamadan önce Veri Sorumluları Siciline kaydolur (m. 16/2).
- Kurul objektif kriterlerle istisna getirebilir (m. 16/2). **Avukatlara yönelik bir istisna kararının varlığı ve kapsamı bu pakette doğrulanmadı.** kvkk.gov.tr'deki sicil istisnası kararlarından kontrol et, sonucu `firm-profile.md`'ye yaz.
- Büro kayıtlıysa aydınlatmadaki bilgiler sicile bildirilen bilgilerle uyumlu olmalıdır (Tebliğ m. 5/1-ç).

### 7. İspat
- Aydınlatmanın yapıldığını ispat yükü veri sorumlusundadır (Tebliğ m. 5/1-e). İmzalı nüsha, e-posta gönderim kaydı veya KEP alındısını matter dosyasına koy.
- Aydınlatma müvekkilin talebine bağlı değildir (Tebliğ m. 5/1-d).

### 8. Güvenlik ve ihlal
- Veri sorumlusu uygun güvenlik düzeyi için teknik ve idari tedbir almak zorundadır (m. 12/1). Veriyi büro adına işleyen (ör. bulut sağlayıcı) ile tedbirlerden müştereken sorumludur (m. 12/2).
- Veriler kanuni olmayan yollarla başkalarınca elde edilirse veri sorumlusu durumu **en kısa sürede** ilgiliye ve Kurula bildirir (m. 12/5). Uygulamada anılan "72 saat" süresi bir Kurul kararına dayanır; kararın künyesi bu pakette doğrulanmadı.
- Mesleki sır (Av. K. m. 36) KVKK'dan bağımsız olarak geçerlidir. Aydınlatma metni sır saklama yükümlülüğünü daraltan bir ifade içermez.

## Çıktı

İki belge:
1. **Müvekkile verilecek aydınlatma metni** (sade dil, 1-2 sayfa)
2. **Dahili kontrol notu:**

```markdown
[ÜST BAŞLIK — KVKK AYDINLATMA KONTROLÜ — DAHİLİ]
Müvekkil: [takma ad] — Tarih: GG.AA.YYYY
- Özel nitelikli veri: var / yok → hukuki sebep: [...]
- Açık rıza gerekiyor mu: hayır / evet (ayrı form)
- Yurt dışı aktarım: yok / var → dayanak: [yeterlilik kararı / standart sözleşme (Kuruma bildirim tarihi) / belirsiz]
- VERBİS: kayıtlı / istisna (karar künyesi) / belirsiz
- Aydınlatma ispat kaydı: [imzalı nüsha / KEP / e-posta]
```

## Hatalar

- Aydınlatma ile açık rızayı tek metinde ve tek imzayla almak (Tebliğ m. 5/1-f)
- "Kanunen gereken her türlü amaçla" gibi genel amaç yazmak (Tebliğ m. 5/1-g)
- Yurt dışındaki bulutu aktarım saymamak (m. 9)
- VERBİS istisnasını doğrulamadan varsaymak

Ayrıntı: `${CLAUDE_PLUGIN_ROOT}/references/kvkk-m11-cevap-sablonu.md` (ilgili kişi başvurusu) · `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`

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
> **Meslek sirri (Av. K. m. 36):** uc MCP de PUBLIC arama aracidir — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| yabanci karsi tarafli veya AZ baglantili yeni is alimi — mevzuat kapsaminin gercekten var olup olmadigini once dogrula | `/arthurlegal:legal-research-kaynak-secimi` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
