# İzleyici Rehberi — Yedi İzleyicinin Ortak Çalışma Kuralları

> `knowledge/agents/` altındaki izleyiciler bu kurallara göre çalışır. Her izleyicinin eşikleri, girdi alanları ve adımları kendi dosyasındadır; bu rehber ortak çerçeveyi, önerilen çalışma ritmini ve yakın yürürlük tarihlerini verir.
> Ortak ilke: izleyiciyi kullanıcı tetikler; zamanlanmış çalışma yoktur. İzleyici UYAP'a bağlanmaz, kayıt oluşturmaz veya değiştirmez, karar vermez. Madde içerikleri 27.09.2026'da ArthurLegal MCP ile çekilen metne dayanır.

## 1. Bir bakışta

| İzleyici | Ne izler | Tetik örneği | Önerilen düzen | Temel dayanak |
|---|---|---|---|---|
| `tutukluluk-inceleme-izleyici` | otuz günlük inceleme, azami tutukluluk, dört aylık adli kontrol incelemesi | "sabah tutuklu listesi" | her iş günü sabahı; adli kontrol haftada bir | CMK m. 102, 108, 110/4 |
| `durusma-hazirlik` | ertesi günün veya haftanın duruşmaları: tebligat, kanuni ara süre, rapor, müzekkere, SEGBİS, zorunlu müdafi, kapalılık | "yarının duruşmaları" | kalem her iş günü öğleden sonra; hâkim hafta başında | HMK m. 139, 147; CMK m. 176/4, 188 |
| `kanun-yolu-kesinlesme-izleyici` | kanun yolu süreleri, cevap süreleri, gönderme, kesinleşme kaydı | "kesinleşme kontrolü" | haftada bir; yoğun tefhim günlerinin ertesinde ek | HMK m. 302/4-5, 345, 361; CMK m. 273, 291; İYUK m. 45, 46; İİK m. 363, 364 |
| `bilirkisi-rapor-izleyici` | rapor süresi ve uzatma, raporun tebliği, itiraz süresi | "bilirkişi takibi" | haftada bir | HMK m. 266, 274, 281; CMK m. 66 |
| `mevzuat-degisiklik-izleyici` | Resmî Gazete taraması, dala göre süzme, yürürlük ve geçiş hükümleri | "haftalık mevzuat özeti" | haftada bir | HMK m. 448; TCK m. 7 |
| `ictihat-ve-aym-izleyici` | içtihadı birleştirme, genel kurul ve daireler kurulu kararları, AYM iptal ve ihlal kararları | "haftalık içtihat özeti" | haftada bir; ay başında 60 günlük yürürlük listesi | AY m. 153; 2797 s.K. m. 45; 2575 s.K. m. 40; 6216 s.K. m. 50 |
| `makul-sure-izleyici` | eski ve hareketsiz dosyalar, kanunda süreye bağlı aşamalar, Tazminat Komisyonu bildirimi | "aylık dosya yaşı raporu" | ayda bir; adli yıl başında ve adli tatil öncesinde ek | AY m. 141/4; HMK m. 147/3, 320/3; İYUK m. 20/5; 6384 s.K. m. 8 |

## 2. Önerilen ritim

Aşağıdaki düzen öneridir; mahkeme kendi düzenini `[DOLDUR]` alanlarına yazar.

| Zaman | Hukuk ve icra | Ceza ve sulh ceza | İdare ve vergi |
|---|---|---|---|
| Her iş günü sabahı | — | `tutukluluk-inceleme-izleyici` | — |
| Her iş günü öğleden sonra | `durusma-hazirlik` (ertesi gün) | `durusma-hazirlik` (ertesi gün) | `durusma-hazirlik` (duruşmalı işler) |
| Haftada bir | `kanun-yolu-kesinlesme-izleyici`, `bilirkisi-rapor-izleyici`, `mevzuat-degisiklik-izleyici`, `ictihat-ve-aym-izleyici` | aynıları ile adli kontrol listesi | `kanun-yolu-kesinlesme-izleyici`, `mevzuat-degisiklik-izleyici`, `ictihat-ve-aym-izleyici` |
| Ayda bir | `makul-sure-izleyici`; AYM yürürlük listesi | aynı | aynı; tekemmülden altı ay kontrolü (İYUK m. 20/5) |
| Adli tatil öncesi ve adli yıl başı | süre uzamaları (HMK m. 104), `makul-sure-izleyici` | süre uzamaları (CMK m. 331/4) | süre uzamaları (İYUK m. 8/3) |

Adli tatil 20 Temmuz'da başlar, 31 Ağustos'ta biter; yeni adli yıl 1 Eylül'de başlar (HMK m. 102; CMK m. 331/1; idari yargıda çalışmaya ara verme İYUK m. 61/1).

## 3. Girdi

- **Kaynak, öncelik sırasıyla:**
  1. **Kullanıcının verdiği liste:** kalem memurunun UYAP'tan dışa aktardığı liste (dosya, yapıştırılan tablo veya CSV), tercihen Arthur Mask'ten geçmiş olarak. Liste bugün dışa aktarılmamışsa listenin tarihi çıktıda belirtilir.
  2. **Liste yoksa:** liste, tarih veya dosya bilgisi tahminle doldurulmaz, örnek satır uydurulmaz. Çıktı tek satırla durur: `UYARI: veri çekilemedi, teyidiniz gerekli: UYAP'taki kendi ekranınız (adliyede UYAP; dışarıda VPN ile vpn.uyap.gov.tr ya da UYAP Mobil)`
- İzleyici kendisi UYAP sorgusu yapmaz; kullanıcının verdiği listenin dışına çıkmaz.
- **Maskeleme:** ad yerine rol etiketi veya sıra numarası yeterlidir. Arthur Mask'in ürettiği `{{DOSYA_NO-01}}`, `{{KİŞİ-01}}` gibi etiketler harfi harfine korunur; gerçek değerler yalnız kullanıcının ekranındadır (`arthur-mask-rehberi.md`).
- **Gizli dosyalar:** soruşturma evresindeki usul işlemleri gizlidir (CMK m. 157); müdafiin dosya inceleme yetkisinin kısıtlandığı dosyalar (CMK m. 153/2) kurum kuralları izin vermedikçe listeye konmaz.
- **Eksik alan:** bilinmeyen alan boş bırakılabilir; izleyici o satırı "olgu eksik" diye ayırır.
- **Hafıza yok:** izleyici önceki çalıştırmayı hatırlamaz. Karşılaştırma isteniyorsa önceki çıktı kullanıcı tarafından yeniden verilir.

## 4. Hesap ve belirsizlik kuralı

- Süre hatırlatmadır; son günü hâkim veya yazı işleri müdürü teyit eder.
- Olgu bilinmiyorsa (ör. tebliğ tarihi) en erken olası gün esas alınır ve satır 🟠 "olgu eksik" işaretlenir.
- Hesap kuralları: `sure-ve-adli-tatil-rehberi.md`; kanun yolu haritası: `istinaf-temyiz-rehberi.md`.
- Madde metni her çalıştırmada yeniden çekilir; özellikle aşağıdaki tarihler yaklaştıkça.

## 5. 27.09.2026 itibarıyla takvimdeki yürürlük tarihleri

| Tarih | Ne olur | Kaynak |
|---|---|---|
| 30.09.2026 | CMK m. 231/5-14 hakkındaki AYM iptal kararı (10.07.2025, E. 2024/98, K. 2025/149) yürürlüğe girer; aynı fıkralar 7589 s.K. ile 31.07.2026'da yeniden düzenlenmiştir | CMK m. 231 dipnotu |
| 20.10.2026 | HMK m. 362/1-a'nın kamulaştırma bedelinin tespiti davaları yönünden iptali (AYM 08.10.2025, E. 2025/124, K. 2025/203) yürürlüğe girer | HMK m. 362 dipnotu |
| 31.10.2026 | 7589 s.K.'nın HMK m. 149'a eklediği fıkra ile TMK m. 440 ve 444 değişiklikleri yürürlüğe girer | HMK m. 149 dipnotu; 7589 s.K. m. 26 (RG 31.07.2026/33326) |
| 16.04.2027 | CMK m. 226/4 üçüncü cümlesine ilişkin AYM iptal kararı (26.03.2026, E. 2025/18, K. 2026/66) yürürlüğe girer | CMK m. 226 dipnotu |
| belirsiz | HMK m. 362/1-a'nın "istinaf başvurusunun kısmen veya tümden kabulü hâli" yönünden iptali (AYM 26.02.2026, E. 2026/49, K. 2026/48) ve İYUK m. 45/6 birinci cümlesinin aynı yönden iptali (AYM 27.03.2025, E. 2024/189, K. 2025/83): dipnotta yürürlük tarihi yok | `UYARI: veri çekilemedi, teyidiniz gerekli: https://normkararlarbilgibankasi.anayasa.gov.tr/` |

Bu tablo `ictihat-ve-aym-izleyici` ve `mevzuat-degisiklik-izleyici` her çalıştırıldığında güncellenir; tarih geçtikten sonra satır bilgi amaçlı kalır.

## 6. Çıktı standardı

- Başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — [İZLEYİCİ] — TASLAK (hâkim/heyet onayı şart)`.
- Renkler (ortak çerçeve; eşikler izleyici dosyasında): 🔴 bugün, yarın veya geçmiş tarih ya da kanuni yasak; 🟠 yakın tarih veya olgu eksik; 🟡 izlenecek; 🟢 bilgi.
- Satır biçimi: `dosya no (maskeli) — olay — son gün — dayanak (madde) — önerilen skill`.
- Sonda: çekilemeyen kaynaklar için `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>` ve "İnceleyen notu" (kullanılan kaynaklar, madde kontrolü, belirsizlikler).
- Kişi adı yazılmaz.

## 7. İzleyiciden skill'e geçiş

| Bulgu | Sonraki adım |
|---|---|
| Tutukluluk incelemesi bugün veya azami süre yakın | `/ceza-hakim:tutukluluk-incelemesi` |
| Duruşmada ara karar seçenekleri | `/hukuk-hakim:ara-karar`, `/idari-hakim:ara-karar-bilgi-belge` |
| Bilirkişi süresi aşıldı | `/hukuk-hakim:ara-karar` (HMK m. 274/2 seçenekleri hâkime sorulur) |
| Rapor tebliğ edildi, itiraz geldi | `/hukuk-hakim:bilirkisi-raporu-denetimi` |
| Kanun yolu süresi doldu | `/hukuk-kalem:kesinlesme-serhi`, `/ceza-kalem:infaz-evraki` |
| Kanun yoluna başvuruldu, cevap süresi doldu | `/hukuk-kalem:istinaf-gonderme-kontrol`, `/ceza-kalem:kanun-yolu-gonderme`, `/idari-kalem:kanun-yolu-gonderme` |
| Yeni kanun veya AYM kararı derdest dosyayı etkiliyor | `/yargi-arastirma:ictihat-dogrulama`, `/yargi-arastirma:aym-aihm-standart-kontrolu` |
| Hareketsiz dosya | `/hukuk-kalem:tebligat`, `/ceza-kalem:muzekkere`, `/idari-kalem:dosya-tekemmul` |

## 8. Ortak sınırlar

- UYAP'a bağlanmaz, kayıt oluşturmaz veya değiştirmez, e-imza işlemi yapmaz.
- Karar vermez: tutuklama ve tahliye, kesinleşme şerhi, bilirkişi değişikliği, uygulanacak hükmün seçimi hâkime veya yetkili personele aittir.
- Hâkim veya personel hakkında performans değerlendirmesi yapmaz.
- Hatırlatma kullanıcının kendi takvimindedir; izleyici kendiliğinden çalışmaz.

## 9. Mahkemeye uyarlama

- Mahkeme türü profili: `profiles/` altından seçilir; `mahkeme-profili.md`'de hangi izleyicilerin kullanıldığı yazılır.
- Eşik değişikliği (ör. 🟠 için yedi gün yerine on gün): `[DOLDUR]`.
- Çalışma saatleri ve sorumlu personel (unvan): `[DOLDUR]`.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): AY m. 141, 153; HMK m. 102, 104, 139, 147, 149, 266, 274, 281, 302, 320, 345, 361, 362, 448; CMK m. 66, 102, 108, 110, 153, 157, 176, 188, 226, 231, 273, 291, 331; İYUK m. 8, 20, 45, 46, 61; İİK m. 363, 364; TCK m. 7; TMK m. 440, 444; 2797 s.K. m. 45; 2575 s.K. m. 40; 6216 s.K. m. 50; 6384 s.K. m. 8. 7589 s.K. yürürlük maddesi RG 31.07.2026/33326 metninden okundu.*
