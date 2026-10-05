# CMK (5271 sayılı Ceza Muhakemesi Kanunu) – Pratik Rehber

> **Durum:** ✅ Açık erişim. Kanun metni Mevzuat MCP + Resmi Gazete; ceza içtihatı Yargı MCP (Yargıtay ceza daireleri). API anahtarı gerekmez.
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
| **Tutuklamaya itiraz** | m. 267-271 | Şüpheli/sanık müdafii | Sulh ceza hakimliği kararına → **7 gün** içinde itiraz (m. 268) |
| **Adli kontrole itiraz** | m. 110/3 + m. 267 | Şüpheli müdafii | Tutuklama yerine adli kontrol tedbirine itiraz |
| **KYOK'a (kovuşturmaya yer olmadığı) itiraz** | m. 173 | Müşteki / suçtan zarar gören | KYOK tebliğinden **15 gün** içinde **Sulh Ceza Hakimliği**'ne (m. 173/1). Dikkat: bu süre 15 gün — itiraz genel süresi 7 günden **farklı**. |

### Kovuşturma evresi

| İşlem | Madde | Kim | Not |
|---|---|---|---|
| **Katılma talebi (müdahale)** | m. 237-239 | Mağdur / suçtan zarar gören | Hüküm verilene kadar her aşamada; katılan **kanun yoluna başvurabilir** (m. 260). Şirket müşteki ise **mutlaka katılma** — yoksa istinaf/temyiz hakkı sınırlı. |
| **İddianameye karşı beyan** | m. 174-176 | Sanık müdafii | İddianamenin iadesi sebepleri (m. 174); kabul sonrası "iddianamenin okunması" üzerine beyan |
| **Esas hakkında savunma** | m. 216 | Sanık + müdafi | Delillerin tartışılması sonrası, **son söz sanığındır** (m. 216/3 — bozma sebebi) |
| **Esas hakkında mütalaaya karşı beyan** | m. 216/1 | Taraflar | Savcının esas hakkındaki mütalaasına cevap |
| **İstinaf (BAM ceza dairesi)** | m. 272 vd. | Taraf / katılan | **SÜRE: 7 GÜN** — hüküm yüze karşı açıklandıysa **tefhimden**, yoksa **tebliğden** (m. 273/1). İstinaf edilemeyen hükümler m. 272/3 (örn. çok düşük adli para cezaları). |
| **Temyiz (Yargıtay)** | m. 286 vd. | Taraf / katılan | BAM kararına karşı; süre **15 gün** (tefhim/tebliğ — m. 291). Temyiz edilemeyen BAM kararları m. 286/2. |
| **Koruma tedbiri tazminatı** | m. 141-144 | Haksız tedbire maruz kalan | Haksız yakalama/tutuklama/elkoyma vb. → karar/hükmün kesinleşmesinden itibaren **3 ay / her halde 1 yıl** içinde **Ağır Ceza Mahkemesi**'ne (m. 142). Çalışan haksız tutuklandıysa şirket destekli tazminat yolu. |

> **`ceza-dilekce` çıktısı** her dilekçede: (1) doğru evre + merci, (2) madde atfı, (3) süre hesabı (tefhim/tebliğ tarihinden), (4) sıfat (müşteki/katılan/şüpheli/sanık/müdafi), (5) talep sonucu net.

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
| **İtiraz** (tutuklama, adli kontrol, hakimlik kararları) | **7 gün** | Kararın öğrenilmesi/tebliği | m. 268/1 |
| **İstinaf** (yerel mahkeme hükmü → BAM) | **7 gün** | Hüküm **tefhim** (yüze karşı) **veya tebliğ** | m. 273/1 |
| **Temyiz** (BAM hükmü → Yargıtay) | **15 gün** | Tefhim / tebliğ | m. 291/1 |
| **KYOK'a itiraz** | **15 gün** | KYOK tebliği | m. 173/1 |
| **Şikayet** (şikayete bağlı suç) | **6 ay** | Fail+fiil öğrenme | TCK m. 73 |
| **Koruma tedbiri tazminatı (m. 141)** | **3 ay / 1 yıl** | Kararın kesinleşme tebliği / her halde kesinleşme | m. 142/1 |

> **En sık hata:** İstinaf süresini 7 gün yerine HMK refleksiyle 2 hafta sanmak. **Ceza istinafı 7 gündür** (hukuk istinafı 2 hafta — karıştırma). Tefhimde süre **tefhim anından**, sanık duruşmada hazır değilse **tebliğden** işler.

---

## Görev ayrımı — tipik suç kategorileri (Asliye ↔ Ağır Ceza)

> ⚖️ Hâkim/kalem için görevli mahkeme tespiti. Taraf sıfatı (müşteki/sanık) değerlendirmesi tarafsızdır; suç vasfı **iddianamede** ileri sürülür, nihai vasıflandırma mahkemece yapılır (CMK m. 226).

| Suç kategorisi | Tipik dayanak | Görevli mahkeme |
|---|---|---|
| **Taksirle öldürme/yaralama (iş kazası)** | TCK m. 85, 89, 22/3; 6331 | Tek ölü → Asliye Ceza; birden çok ölü / nitelikli → Ağır Ceza |
| **Çevre suçları** | TCK m. 181-184 + 2872 | Asliye Ceza (idari para cezası ayrı, idari yargıda) |
| **Bilişim suçları** | TCK m. 243-245 | Asliye Ceza |
| **Kaçakçılık** | 5607 KMK | Asliye Ceza; nitelikli haller → Ağır Ceza |

> **Görev (CMK m. 3-7):** Kural Asliye Ceza; ağır cezalık suçlar (kanunda gösterilen) Ağır Ceza Mahkemesinde. Görev kamu düzenindendir, her aşamada re'sen gözetilir.
> **Tüzel kişi:** Ceza verilemez; yalnızca **güvenlik tedbiri** (TCK m. 60 / CMK ilgili hükümler) uygulanabilir.

---

## Kaynak erişimi — MCP + Resmi Gazete

### Kanun metni (Mevzuat MCP)

```
search_mevzuat(mevzuat_no="5271", mevzuat_tur="KANUN")   # CMK
search_mevzuat(mevzuat_no="5237", mevzuat_tur="KANUN")   # TCK
search_mevzuat(mevzuat_no="6331", mevzuat_tur="KANUN")   # İSG K.
search_mevzuat(mevzuat_no="2872", mevzuat_tur="KANUN")   # Çevre K.
search_mevzuat(mevzuat_no="5607", mevzuat_tur="KANUN")   # Kaçakçılıkla Mücadele K.
search_mevzuat(mevzuat_no="5235", mevzuat_tur="KANUN")   # Adli yargı görev/teşkilat
→ get_mevzuat_content(...) / search_within_mevzuat(phrase="<madde no>")
```

Atıf (kanun): `[Mevzuat MCP — CMK m. XXX — GG.AA.YYYY]`

### Ceza içtihatı (Yargı MCP — Yargıtay ceza daireleri)

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  phrase="taksirle öldürme iş kazası yönetici sorumluluk istinaf süresi",
  birimAdi="12. Ceza Dairesi",      # iş kazası/taksir temyizi
  kararTarihiStart="2023-01-01"
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

**Atıf (içtihat — bu rehberin standardı):** `[Yargı MCP — Yargıtay X.CD — Esas/Karar]`
Örn: `[Yargı MCP — Yargıtay 12.CD — 2023/4567 E. 2024/1234 K.]`. CGK için: `[Yargı MCP — Yargıtay CGK — Esas/Karar]`.

> **Asla** çekmediğin bir kararı atıfla gösterme. Çekemiyorsan `[model bilgisi — doğrulayın]`.

### Resmi Gazete (mevzuat değişikliği / yürürlük teyidi)
- CMK ve TCK sık değişir (özellikle istinaf/temyiz parasal sınırları, infaz rejimi).
- Süre/sınır içeren her atıfta yürürlük tarihini RG'den teyit et. Atıf: `[Resmi Gazete — Sayı/Tarih]`.

---

## Tipik hatalar (önlem)

- ❌ **İstinaf süresini 2 hafta sanmak** — ceza istinafı **7 gün** (m. 273). Hukuk istinafıyla (HMK 2 hafta) karıştırma.
- ❌ **KYOK itirazını 7 gün sanmak** — KYOK'a itiraz **15 gün** (m. 173), genel itiraz 7 gün (m. 268). İki ayrı süre.
- ❌ **Müşteki için katılma talebini atlamak** — m. 237. Katılmayan müşteki/zarar gören kanun yoluna başvuramaz (m. 260). Şirket müştekiyse **mutlaka katılma**.
- ❌ **Son söz sanığa verilmemesi** — m. 216/3 ihlali kesin bozma sebebi; savunma dilekçesinde bu hakkı koru.
- ❌ **Süreyi tefhim yerine tebliğden başlatmak (veya tersi)** — sanık duruşmada hazırsa **tefhim**, değilse **tebliğ** esas.
- ❌ **Şikayet süresini kaçırmak** — şikayete bağlı suçta 6 ay (TCK m. 73); geçince soruşturma açılmaz.
- ❌ **Tüzel kişiye "ceza" istemek** — tüzel kişiye ceza verilmez; **güvenlik tedbiri** (CMK m. 138) + idari yaptırım yolu doğru.

---

## Bağlantılı referanslar

- [Sulh ceza hâkimliği rehberi](sulh-ceza-hakimligi-rehberi.md) — soruşturma evresi koruma tedbirleri
- [HMK rehberi](hmk-rehberi.md) — Paralel tazminat davası usulü (süre/görev farkı dikkat)
- [İYUK rehberi](iyuk-rehberi.md) — Çevre/EPDK idari ceza yolu (ceza yargısından ayrı)
- [CED rehberi](ced-rehberi.md) — Çevre suçu + idari ceza arayüzü
- [Mevzuat MCP rehberi](mevzuat-mcp-rehberi.md) — CMK/TCK madde çekme pattern'ları
- [Yarg MCP rehberi](yargi-mcp-rehberi.md) — Yargıtay ceza dairesi içtihatı çekme
- [UYAP rehberi](uyap-rehberi.md) — Ceza dosyası/UYAP üzerinden belge ve süre takibi
- [Kanun kısaltmalar](kanun-kisaltmalar.md) — CMK/TCK/KMK kısaltma standardı
