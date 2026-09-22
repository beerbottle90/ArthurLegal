# CMK (5271 sayılı Ceza Muhakemesi Kanunu) – Pratik Rehber

> **Durum:** ✅ Açık erişim. Kanun metni ArthurLegal MCP (`tr_`) + Resmi Gazete; ceza içtihatı ArthurLegal MCP (`tr_`) (Yargıtay ceza daireleri). API anahtarı gerekmez.
>
> Türk ceza yargılaması usulünün temel kaynağı. `advocacy-legal` eklentisindeki **`ceza-dilekce`** skill'i, ceza dilekçe/işlem taslakları için madde atıflarını ve süre/görev kurallarını bu rehberden alır.
>
> **Neden gerekli?** Enerji üretim ve altyapı taahhüt sahasında faaliyet gösteren bir şirket için (örn. rüzgar/HES/jeotermal santral işletme, enerji & su altyapısı proje geliştirme) ceza dosyaları genelde **şirket/çalışan** odaklıdır: iş kazası (6331 + TCK taksirle yaralama/öldürme), çevre suçları, bilişim suçları, kaçakçılık. Şirket çoğunlukla **müşteki/katılan** (zarar gören şirket) **VEYA çalışan müdafii destek** (şirket çalışanı şüpheli/sanık) tarafındadır — nadiren doğrudan fail. Tüzel kişi hakkında ceza değil, **güvenlik tedbiri** (CMK m. 138) gündeme gelir.

---

## Evre ayrımı — soruşturma vs kovuşturma

CMK'nın bütün süre/işlem mantığı bu ikiliye oturur:

| Evre | Kim yürütür | Başlangıç | Bitiş | Tipik dilekçe |
|---|---|---|---|---|
| **Soruşturma** (m. 160 vd.) | Cumhuriyet Savcısı | Suç ihbarı/şikayet (m. 158) | İddianame (m. 170) **veya** KYOK (m. 172) | Suç duyurusu, müşteki beyanı, şüpheli savunması, tahliye talebi, tutuklamaya itiraz, KYOK'a itiraz |
| **Kovuşturma** (m. 175 vd.) | Mahkeme (Asliye/Ağır Ceza) | İddianamenin kabulü (m. 174-175) | Hüküm (m. 223) | Katılma talebi, esas hakkında savunma, esas hakkında mütalaaya beyan, istinaf, temyiz |

> **Kural:** Soruşturma **gizlidir** (m. 157); kovuşturma **alenidir** (m. 182). Müdafi soruşturmada dosya inceleme yetkisi m. 153 ile sınırlanabilir (kısıtlama kararı).

---

## Dilekçe / işlem tipleri — `ceza-dilekce` üretim haritası

### Soruşturma evresi

| İşlem | Madde | Kim | Not |
|---|---|---|---|
| **Suç duyurusu / şikayet** | m. 158 | Mağdur / herkes | Şikayete bağlı suçlarda **6 ay** hak düşürücü süre (TCK m. 73); re'sen soruşturulan suçlarda süre yok. Savcılığa/kolluğa verilir. |
| **Müşteki beyanı** | m. 234 (mağdur hakları) | Mağdur / zarar gören | Delil sunma, vekil bulundurma, dosya inceleme talebi |
| **Şüpheli savunması (ifade)** | m. 147 (ifade/sorgu usulü) | Şüpheli + müdafi | Susma hakkı, müdafi hazır bulunma; **m. 148** baskı/işkence ile alınan ifade hükümsüz |
| **Tahliye talebi** | m. 104 | Şüpheli/sanık müdafii | Soruşturmada savcı/sulh ceza hakimi; her aşamada istenebilir |
| **Tutuklamaya itiraz** | m. 267-271 | Şüpheli/sanık müdafii | Sulh ceza hakimliği kararına → öğrenmeden itibaren **iki hafta** içinde itiraz (m. 268/1); inceleme mercii yargı çevresindeki **asliye ceza mahkemesi hâkimi** (m. 268/3-b) |
| **Adli kontrole itiraz** | m. 110/3 + m. 267 | Şüpheli müdafii | Tutuklama yerine adli kontrol tedbirine itiraz |
| **KYOK'a (kovuşturmaya yer olmadığı) itiraz** | m. 173 | Müşteki / suçtan zarar gören | KYOK tebliğinden **iki hafta** içinde **Sulh Ceza Hakimliği**'ne (m. 173/1). Genel itiraz süresi de iki haftadır (m. 268/1); fark başlangıçtadır: KYOK'ta tebliğ, genel itirazda öğrenme. |

### Kovuşturma evresi

| İşlem | Madde | Kim | Not |
|---|---|---|---|
| **Katılma talebi (müdahale)** | m. 237-239 | Mağdur / suçtan zarar gören | Hüküm verilene kadar her aşamada; katılan **kanun yoluna başvurabilir** (m. 260). Şirket müşteki ise **mutlaka katılma** — yoksa istinaf/temyiz hakkı sınırlı. |
| **İddianameye karşı beyan** | m. 174-176 | Sanık müdafii | İddianamenin iadesi sebepleri (m. 174); kabul sonrası "iddianamenin okunması" üzerine beyan |
| **Esas hakkında savunma** | m. 216 | Sanık + müdafi | Delillerin tartışılması sonrası, **son söz sanığındır** (m. 216/3 — bozma sebebi) |
| **Esas hakkında mütalaaya karşı beyan** | m. 216/1 | Taraflar | Savcının esas hakkındaki mütalaasına cevap |
| **İstinaf (BAM ceza dairesi)** | m. 272 vd. | Taraf / katılan | **SÜRE: İKİ HAFTA** — hükmün **gerekçesiyle birlikte tebliğinden** itibaren (m. 273/1); hüküm yüze karşı açıklanmış olsa da süre tefhimle başlamaz. Tutuklu sanık için m. 263 saklı. İstinaf edilemeyen hükümler m. 272/3 (örn. çok düşük adli para cezaları). |
| **Temyiz (Yargıtay)** | m. 286 vd. | Taraf / katılan | BAM kararına karşı; süre **iki hafta**, hükmün **gerekçesiyle birlikte tebliğinden** itibaren (m. 291/1). Temyiz edilemeyen BAM kararları m. 286/2. |
| **Koruma tedbiri tazminatı** | m. 141-144 | Haksız tedbire maruz kalan | Haksız yakalama/tutuklama/elkoyma vb. → karar/hükmün kesinleşmesinden itibaren **3 ay / her halde 1 yıl** içinde **Ağır Ceza Mahkemesi**'ne (m. 142). Çalışan haksız tutuklandıysa şirket destekli tazminat yolu. |

> **`ceza-dilekce` çıktısı** her dilekçede: (1) doğru evre + merci, (2) madde atfı, (3) süre hesabı (istinaf/temyizde gerekçeli hükmün tebliğinden, itirazda öğrenmeden), (4) sıfat (müşteki/katılan/şüpheli/sanık/müdafi), (5) talep sonucu net.

---

## Uzlaştırma (m. 253-255)

- **Zorunlu** uzlaştırma kapsamı: şikayete bağlı suçlar + m. 253/1'de sayılan katalog (örn. TCK m. 89 **taksirle yaralama** — iş kazalarında çok kritik).
- **Taksirle ÖLDÜRME (TCK m. 85) uzlaştırma kapsamı DIŞINDA** — ölümlü iş kazasında uzlaştırma yok, doğrudan kovuşturma.
- Uzlaştırma → uzlaştırmacı atanır → anlaşma olursa **KYOK** (soruşturmada) / **düşme** (kovuşturmada).
- **Örnek bağlam:** Çalışanın taksirle yaralama dosyasında uzlaştırma, ceza riskini erken kapatma fırsatı; ancak işveren ihmali/6331 yönü ayrıca değerlendirilir.

---

## Görevli mahkeme

| Mahkeme | Görev alanı | Tipik kullanım |
|---|---|---|
| **Sulh Ceza Hakimliği** | Soruşturma koruma tedbirleri (tutuklama, arama, elkoyma), itirazlar, KYOK itirazı | Tutuklama/itiraz, KYOK'a itiraz |
| **Asliye Ceza Mahkemesi** | Ağır ceza dışında kalan tüm suçlar (kural) | Taksirle yaralama (TCK m. 89), 6331 cezaları, çevre suçları (2872), bilişim (TCK m. 243-245), basit kaçakçılık |
| **Ağır Ceza Mahkemesi** | Üst sınırı **10 yıldan fazla** hapis gerektiren suçlar + kanunla özel görevlendirilenler (m. 141 tazminat dahil) | Birden fazla ölümlü/bilinçli taksirle öldürme (ağırlaşmış), nitelikli kaçakçılık, koruma tedbiri tazminatı |

> **Görev belirleme:** 5235 sayılı Kanun m. 11-12. Üst sınır 10 yıl eşiği → Ağır Ceza. Taksirle öldürme (m. 85/1: 2-6 yıl) → Asliye Ceza; birden fazla ölü/yaralı (m. 85/2: 2-15 yıl) → **Ağır Ceza**.

---

## Süre tablosu (KRİTİK — her dilekçede teyit et)

| İşlem | Süre | Başlangıç | Madde |
|---|---|---|---|
| **İtiraz** (tutuklama, adli kontrol, hakimlik kararları) | **İki hafta** | Kararın öğrenilmesi (yüze karşı açıklama veya tebliğ, m. 35) | m. 268/1 |
| **İstinaf** (yerel mahkeme hükmü → BAM) | **İki hafta** | Hükmün **gerekçesiyle birlikte tebliği** | m. 273/1 |
| **Temyiz** (BAM hükmü → Yargıtay) | **İki hafta** | Hükmün **gerekçesiyle birlikte tebliği** | m. 291/1 |
| **KYOK'a itiraz** | **İki hafta** | KYOK tebliği | m. 173/1 |
| **Şikayet** (şikayete bağlı suç) | **6 ay** | Fail+fiil öğrenme | TCK m. 73 |
| **Koruma tedbiri tazminatı (m. 141)** | **3 ay / 1 yıl** | Kararın kesinleşme tebliği / her halde kesinleşme | m. 142/1 |

> **Değişiklik uyarısı — 7499 s.K. (RG 12.03.2024):** İtiraz (m. 268), KYOK'a itiraz (m. 173), istinaf (m. 273) ve temyiz (m. 291) süreleri **iki hafta**dır. İstinaf ve temyizde süre tefhimden değil, **hükmün gerekçesiyle birlikte tebliğinden** işler. "İstinaf 7 gün / temyiz 15 gün / KYOK itirazı 15 gün" bilgisi 2024 öncesine aittir; eski kitap, şablon ve içtihat özetlerinde hâlâ geçer. Süreyi her dosyada yürürlükteki metinden (`tr_mevzuat_madde_getir`) teyit et.

---

## Sektörel/örnek senaryolar — tipik ceza dosyası senaryoları

### 1. İş kazası (6331 + TCK taksir) — santral/şantiye
- **Hukuki temel:** TCK m. 85 (taksirle öldürme), m. 89 (taksirle yaralama), m. 22/3 (bilinçli taksir = ağırlatıcı), 6331 m. 26 (idari) + ceza yönü.
- **Olası şüpheli:** Saha/santral müdürü, İSG uzmanı (çok tehlikeli işyeri → A sınıfı), vardiya amiri; büyük olayda yönetici sıfatlı üst kademe.
- **Şirket rolü:** Genelde **çalışan müdafii destek** (şirket çalışanı şüpheli). Mağdur/ölen şirket çalışanı ise şirket aynı zamanda işveren — savunma + paralel SGK rücu/tazminat (bkz. [İSG dava rehberi](isg-dava-rehberi.md)).
- **Mahkeme:** Tek ölü → Asliye Ceza; birden çok ölü → Ağır Ceza.

### 2. Çevre suçları (TCK m. 181-184 + 2872)
- Çevreyi kasten/taksirle kirletme, atık, emisyon. Santral/proje sahası emisyon olayları.
- Tüzel kişi → ceza değil **güvenlik tedbiri** (CMK m. 138) + idari para cezası (paralel; bkz. [CED rehberi](ced-rehberi.md), idari yargı).

### 3. Bilişim suçları (TCK m. 243-245, 244)
- Sistem girme, veri bozma, banka/kredi kartı kötüye kullanma. Şirket çoğunlukla **müşteki** (siber saldırı/iç fraud mağduru) → suç duyurusu + katılma.

### 4. Kaçakçılık (5607 KMK / 4926)
- Akaryakıt/enerji ürünü kaçakçılığı, gümrük. Tedarik zincirinde karşı taraf kaynaklı → şirket **müşteki/şikayetçi** veya çalışan müdafii.
- Nitelikli haller → Ağır Ceza.

> **Kural:** Şirket çoğunlukla **müşteki VEYA çalışan müdafii destek** tarafında. Dilekçe sıfatı doğru kurulmalı — müşteki dilekçesi (m. 158/237) ile sanık savunması (m. 216) farklı yapı ve farklı kanun yolu hakkı doğurur.

---

## Kaynak erişimi — MCP + Resmi Gazete

### Kanun metni (ArthurLegal MCP (`tr_`))

```
tr_mevzuat_ara(number="5271", types=["KANUN"])   # CMK
tr_mevzuat_ara(number="5237", types=["KANUN"])   # TCK
tr_mevzuat_ara(number="6331", types=["KANUN"])   # İSG K.
tr_mevzuat_ara(number="2872", types=["KANUN"])   # Çevre K.
tr_mevzuat_ara(number="5607", types=["KANUN"])   # Kaçakçılıkla Mücadele K.
tr_mevzuat_ara(number="5235", types=["KANUN"])   # Adli yargı görev/teşkilat
→ tr_mevzuat_icindekiler(mevzuat_id="<mevzuat_id>") → tr_mevzuat_madde_getir(madde_id="<madde_id>")   # şemada number ve madde_no varsa tek çağrı
→ tr_mevzuat_icinde_ara(mevzuat_id="<mevzuat_id>", query="<konu kelimeleri>")   # konu araması; madde bulma yolu değil
```

Atıf (kanun): `[ArthurLegal TR — CMK m. XXX — GG.AA.YYYY]`

### Ceza içtihatı (ArthurLegal MCP (`tr_`) — Yargıtay ceza daireleri)

```
tr_ictihat_ara(
  query="+taksirle +öldürme +iş +kazası +yönetici +sorumluluk +istinaf +süresi",
  chamber="12. Ceza Dairesi",      # iş kazası/taksir temyizi
  date_from="2023-01-01"
)
```

İlgili ceza daireleri (dosya tipine göre):

| Konu | Yargıtay ceza dairesi |
|---|---|
| Taksirle öldürme/yaralama (iş kazası) | **12. CD** |
| Çevre suçları | **18. CD / 4. CD** (dönem) |
| Bilişim, banka/kredi kartı | **8. CD / 11. CD** |
| Kaçakçılık | **7. CD / 20. CD** |
| Genel usul / birleştirme | **Ceza Genel Kurulu (CGK)** — bağlayıcı |

> **CGK kararları içtihadı birleştirir** — alt mahkeme ve diğer daireler için en yüksek ağırlık.

**Atıf (içtihat — bu rehberin standardı):** `[ArthurLegal TR — Yargıtay X.CD — Esas/Karar]`
Örn: `[ArthurLegal TR — Yargıtay 12.CD — 2023/4567 E. 2024/1234 K.]`. CGK için: `[ArthurLegal TR — Yargıtay CGK — Esas/Karar]`.

> **Asla** çekmediğin bir kararı atıfla gösterme. Çekemiyorsan `[model bilgisi — doğrulayın]`.

### Resmi Gazete (mevzuat değişikliği / yürürlük teyidi)
- CMK ve TCK sık değişir (özellikle kanun yolu süreleri — 7499 s.K. —, istinaf/temyiz parasal sınırları, infaz rejimi).
- Süre/sınır içeren her atıfta yürürlük tarihini RG'den teyit et. Atıf: `[Resmi Gazete — Sayı/Tarih]`.

---

## Tipik hatalar (önlem)

- ❌ **Ceza istinafını hâlâ 7 gün sanmak** — 7499 s.K. ile istinaf süresi **iki hafta** (m. 273/1), başlangıç **gerekçeli hükmün tebliği**. Eski kaynaklardaki 7 gün yürürlükte değil.
- ❌ **Temyizi ve KYOK itirazını 15 gün, genel itirazı 7 gün sanmak** — üçü de artık **iki hafta** (m. 291/1, m. 173/1, m. 268/1). Başlangıçları farklı: temyizde gerekçeli hükmün tebliği, KYOK'ta tebliğ, genel itirazda öğrenme.
- ❌ **Müşteki için katılma talebini atlamak** — m. 237. Katılmayan müşteki/zarar gören kanun yoluna başvuramaz (m. 260). Şirket müştekiyse **mutlaka katılma**.
- ❌ **Son söz sanığa verilmemesi** — m. 216/3 ihlali kesin bozma sebebi; savunma dilekçesinde bu hakkı koru.
- ❌ **Süre başlangıcını karıştırmak** — istinaf ve temyizde süre **gerekçeli hükmün tebliğinden** işler, tefhim süreyi başlatmaz (m. 273/1, 291/1); itirazda **öğrenme** esastır: yüze karşı açıklanan kararda açıklama, yoklukta tebliğ (m. 35, 268/1).
- ❌ **Şikayet süresini kaçırmak** — şikayete bağlı suçta 6 ay (TCK m. 73); geçince soruşturma açılmaz.
- ❌ **Tüzel kişiye "ceza" istemek** — tüzel kişiye ceza verilmez; **güvenlik tedbiri** (CMK m. 138) + idari yaptırım yolu doğru.

---

## Bağlantılı referanslar

- [İSG dava rehberi](isg-dava-rehberi.md) — İş kazasında üçlü-paralel risk (cezai + tazminat + idari); CMK cezai ayağı bununla entegre
- [HMK rehberi](hmk-rehberi.md) — Paralel tazminat davası usulü (süre/görev farkı dikkat)
- [İYUK rehberi](iyuk-rehberi.md) — Çevre/EPDK idari ceza yolu (ceza yargısından ayrı)
- [CED rehberi](ced-rehberi.md) — Çevre suçu + idari ceza arayüzü
- [ArthurLegal MCP TR mevzuat rehberi](mevzuat-mcp-rehberi.md) — CMK/TCK madde çekme pattern'ları
- [ArthurLegal MCP TR rehberi](yargi-mcp-rehberi.md) — Yargıtay ceza dairesi içtihatı çekme
- [UYAP rehberi](uyap-rehberi.md) — Ceza dosyası/UYAP üzerinden belge ve süre takibi
- [Kanun kısaltmalar](kanun-kisaltmalar.md) — CMK/TCK/KMK kısaltma standardı
