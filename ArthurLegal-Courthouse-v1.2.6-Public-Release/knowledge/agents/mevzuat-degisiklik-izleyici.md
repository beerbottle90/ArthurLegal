---
name: mevzuat-degisiklik-izleyici
description: >
  Resmî Gazete'yi kullanıcının verdiği tarih aralığında tarar, mahkemenin
  dalına göre süzer (hukuk, ceza, idari, vergi, icra), yürürlük tarihlerini
  ve geçiş hükümlerini çıkarır, derdest dosyaları etkileyebilecek değişiklikleri
  işaretler. Hangi hükmün uygulanacağına karar vermez; hâkime soru ve kaynak
  listesi sunar.
tetik_ifadeleri:
  - "mevzuat değişikliği var mı"
  - "resmî gazete taraması"
  - "haftalık mevzuat özeti"
  - "yeni kanun çıktı mı"
  - "yürürlük tarihleri"
calisma: kullanici-tetikli
ilgili_skilller:
  - /yargi-arastirma:ictihat-dogrulama
  - /yargi-arastirma:emsal-tarama
---

# Mevzuat Değişiklik İzleyicisi

> Çıktı başlığı: `MAHKEME DAHİLİ ÇALIŞMA NOTU — MEVZUAT DEĞİŞİKLİK ÖZETİ — TASLAK (hâkim/heyet onayı şart)`.
> Bir hükmün derdest dosyaya uygulanıp uygulanmayacağı hâkimin takdiridir. İzleyici değişikliği, yürürlük tarihini ve geçiş hükmünü metinden aktarır; yorumu hâkime bırakır.

## Amaç

Usul kanunları sık değişir ve değişiklikler çoğu zaman "Bazı Kanunlarda Değişiklik" başlıklı torba kanunlarla gelir. Bir kanunun farklı maddeleri farklı tarihlerde yürürlüğe girebilir. İzleyici, mahkemenin işini etkileyen değişiklikleri süzer ve her biri için "ne değişti, ne zaman yürürlükte, geçiş hükmü ne diyor, hangi dosya türünü etkiler" sorularını cevaplar.

## Ne zaman çalışır

Kullanıcı tetikler: "haftalık mevzuat özeti", "resmî gazete taraması". Önerilen düzen: haftada bir, son çalıştırma tarihinden bugüne. Zamanlanmış çalışma yoktur.

## Girdi

- Tarih aralığı (bir çağrıda en çok 60 gün).
- Mahkemenin dalı ve türü (`mahkeme-profili.md` ve seçilen `profiles/` dosyası).
- İsteğe bağlı: derdest dosya türleri listesi (maskeli; yalnız tür ve aşama).

## Adımlar

1. **Tara.** `tr_resmi_gazete_tara(query=…, date_from=…, date_to=…)`. Dal için sorgu terimleri: hukuk için "Hukuk Muhakemeleri", "Türk Medenî", "Borçlar", "Arabuluculuk", "Tebligat", "Harçlar"; ceza için "Ceza Muhakemesi", "Türk Ceza", "İnfaz", "Çocuk Koruma"; idari ve vergi için "İdari Yargılama", "Vergi Usul", "Amme Alacakları", "Danıştay"; ortak "Hâkimler ve Savcılar Kurulu", "Anayasa Mahkemesinin". Vergi ve icra için `konu="vergi"` ve `konu="icra"` ön elemesi de kullanılabilir; bu bir ön elemedir, "başka değişiklik yok" sonucuna tek başına dayanak olmaz (`mevzuat-mcp-rehberi.md` bölüm 4).
2. **Kanun kalemlerini ayrıca yokla.** 27.09.2026'daki denemede 31.07.2026 (S. 33326) ve 18.08.2026 (S. 33344) fihristlerinde YASAMA BÖLÜMÜ kalemleri listede görünmedi; kalem adresleri `-3` ve `-4`'ten başlıyordu. 7589 s.K. yalnız `tr_resmi_gazete_getir(url="https://www.resmigazete.gov.tr/eskiler/2026/07/20260731-1.htm")` ile okunabildi. Aynı torba kanun `tr_mevzuat_ara(number="7589")` ile ayrı kayıt olarak da bulunamadı. Bu yüzden:
   - fihristte ilk kalem `-1` değilse o günün `-1`, `-2` adreslerini `tr_resmi_gazete_getir` ile aç;
   - temel usul kanununun maddesini çek ve değişiklik şerhlerine bak (`(Ek: GG/AA/YYYY-NNNN/..)`, `(Değişik: …)`, `(Mülga: …)`);
   - değiştiren kanunun izini `tr_mevzuat_icinde_ara(number="5271", query="7593")` gibi bir aramayla sür (27.09.2026'da CMK'da 7593 s.K. izi bu yolla bulundu).
   Kanun kalemi hiçbir yolla açılamıyorsa: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.resmigazete.gov.tr/`.
3. **Her değişiklik için çıkar:** tür (kanun, CB kararnamesi, yönetmelik, HSK kararı, AYM kararı), değişen madde, yürürlük maddesi (maddeler farklı tarihlerde yürürlüğe girebilir), geçiş hükmü (geçici madde), etkilenen dosya türü.
4. **Zaman bakımından uygulama çerçevesi.** Genel kural metinleri: HMK hükümleri tamamlanmış işlemleri etkilememek kaydıyla derhâl uygulanır (HMK m. 448). Ceza hukukunda failin lehine olan kanun uygulanır; infaz rejimine ilişkin hükümler, hapis cezasının ertelenmesi, koşullu salıverilme ve tekerrür hariç derhâl uygulanır (TCK m. 7/2, 7/3). Özel geçiş hükmü varsa önce o okunur. Bu çerçeve hâkime sunulur; izleyici sonuç çıkarmaz.
5. **Konsolide metni teyit et.** RG metni yalnız değişiklik hükmüdür. Yürürlüğe girmiş değişikliğin metne işlenip işlenmediğini `tr_mevzuat_madde_getir` ile kontrol et. İleri tarihli değişiklik çoğu zaman yürürlüğe girdiği gün işlenir; o güne kadar dipnotta "yürürlüğe girdiği tarihte işlenecek" notu görünür.
6. **Profil dosyalarına not düş.** Değişiklik bir `profiles/` dosyasındaki süreyi, görevi veya kanun yolunu eskitiyorsa çıktıda "profil güncellemesi gerekir" satırı yaz.

## Örnek: 7589 s.K. (RG 31.07.2026, S. 33326)

"Yargının Etkin ve Verimli İşlemesine Yönelik Bazı Kanunlarda Değişiklik Yapılmasına Dair Kanun" RG metninden okunarak özetlendi. Yürürlük (m. 26): 3. madde 23.07.2026'dan geçerli olmak üzere yayım tarihinde; 11, 12 ve 22. maddeler yayımından üç ay sonra (31.10.2026); diğer maddeler yayım tarihinde.

| Değişen hüküm | Özü | Yürürlük ve geçiş |
|---|---|---|
| HMK m. 107 | belirsiz alacak davası maddesi yürürlükten kaldırıldı | 31.07.2026; kaldırılmadan önce açılan davalarda uygulanmaya devam (geçici m. 1/10) |
| HMK m. 109/4 | kısmi davada talep, bir defaya mahsus ve tahkikatın sonuna kadar artırılabilir; zamanaşımı artırılan kısım için de dava tarihinden kesilmiş sayılır | 31.07.2026 |
| HMK m. 147/3 | duruşmalar arası üç aydan uzun olamaz; zorunlu hâlde gerekçeli | 31.07.2026 |
| HMK m. 149/4 | ses ve görüntü nakliyle katılanlarda elle atılan imza hükümleri (ikrar, yemin, feragat, kabul, sulh hariç) uygulanmaz | 31.10.2026 |
| HMK m. 166, 168 | birleştirme kararının bağlayıcılığı; birleştirme kararına istinaf, ayırma kararına hükümle birlikte kanun yolu | 31.07.2026 |
| HMK m. 362/3 | BAM'ın yeniden esas hakkında verdiği kararların temyiz edilebilirliği | 31.07.2026 |
| CMK m. 231/5-14 | HAGB yeniden düzenlendi; HAGB kararına istinaf (m. 231/12) | 31.07.2026 |
| CMK m. 80, 247/3, 308 | genetik inceleme kayıtları; kaçak sanık; Yargıtay Cumhuriyet Başsavcısının itirazı (üç ay) | 31.07.2026; m. 308 için geçici m. 1/8 |
| TCK m. 158/4 | belirli iştirak hâlinde indirim | 31.07.2026; kanun yolundaki ve infazdaki dosyalar için geçici m. 1/6, 1/7 |
| İYUK m. 45/3, 45/5; m. 46 | BİM'in kaldırma hâlleri sınırlandı; yeniden verilen kararlar için temyiz yolu | 31.07.2026; m. 46 değişikliği yürürlükten sonra BİM'lerce verilen kararlara (geçici m. 1/3) |
| 2576 s.K. m. 7 | tek hâkimle çözülecek davalarda parasal sınır | 31.07.2026; yürürlükten sonra açılan davalara (geçici m. 1/2) |
| İİK m. 114; TMK m. 440, 444 | ortaklığın giderilmesinde mirasçılar arası ilk artırma; vesayette elektronik satış portalı | İİK: 31.07.2026, geçici m. 1/1; TMK: 31.10.2026, geçici m. 1/5 |
| TBK m. 55; 3095 s.K. m. 1 | bedensel zarar ve destekten yoksunlukta faiz başlangıcı ve mahsup; kanuni faiz oranı | 31.07.2026; TBK m. 55 için geçici m. 1/9 |
| 2802 s.K. m. 63/2-f | hukuki bilgiyle çözülebilecek konuda bilirkişiye başvurmak uyarma cezası hâli | 31.07.2026 |

Aynı dönemde metin şerhlerinden görülen diğer değişiklikler: 7593 s.K. (CMK m. 174/1-e: 15 yaşını doldurmamış çocuk hakkında sosyal inceleme yaptırılmadan düzenlenen iddianamenin iadesi; 5395 s.K. m. 35/3; CMK değişiklik tablosunda yürürlük 18.08.2026), 7588 s.K. (İYUK m. 28/1'e ek cümle), 7590 s.K. (5651 s.K. m. 9/A'da merci ibaresi), 7571 s.K. (5235 s.K. m. 12'den "nitelikli dolandırıcılık" çıkarıldı; CMK değişiklik tablosunda yürürlük 25.12.2025).

## Çıktı şablonu

```
MAHKEME DAHİLİ ÇALIŞMA NOTU — MEVZUAT DEĞİŞİKLİK ÖZETİ — TASLAK (hâkim/heyet onayı şart)
Tarama: GG.AA.YYYY – GG.AA.YYYY · Dal: [..] · Kaynak: tr_resmi_gazete_tara + tr_resmi_gazete_getir

🔴 YÜRÜRLÜKTE VE DERDEST DOSYAYI ETKİLEYEBİLİR ([N])
- [Kanun/karar, RG tarih/sayı] — [değişen madde] — [öz] — Yürürlük: [..] — Geçiş: [..] — Etkilenen dosya türü: [..]
🟠 30 GÜN İÇİNDE YÜRÜRLÜĞE GİRECEK ([N])
🟡 İZLENECEK (ikincil düzenleme bekleyen, HSK iş bölümü vb.) ([N])
🟢 BİLGİ ([N])

Tarama yöntemi: kullanılan sorgular; konu süzgecinde elenen kalem sayısı; açılamayan kalemler (UYARI satırıyla).
Profil güncellemesi gerekenler: [profiles/…]
⚠️ İnceleyen notu: uygulanacak hükmün seçimi hâkimdedir; madde kontrolü.
```

## Sınırlar

- UYAP'a veya mevzuat sistemine bağlanmaz, kayıt eklemez; yalnız ArthurLegal MCP ile kamuya açık metni okur.
- Hangi metnin derdest dosyaya uygulanacağına karar vermez; geçiş hükmünü ve genel kuralı aktarır.
- Konu süzgeci ön elemedir. "Bu dönemde başka değişiklik yok" demez; taranan sorguları ve elenen kalem sayısını yazar.
- Açılamayan metin için yorum yapmaz; UYARI satırı yazar.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): HMK m. 107, 109, 147, 149, 166, 168, 362, 448; TCK m. 7, 158; CMK m. 80, 174, 231, 247, 308; İYUK m. 28, 45, 46; 2576 s.K. m. 7; İİK m. 114; TMK m. 440, 444; TBK m. 55; 3095 s.K. m. 1; 2802 s.K. m. 63; 5235 s.K. m. 12; 5395 s.K. m. 35; 5651 s.K. m. 9/A. 7589 s.K. metni RG 31.07.2026/33326'dan (`tr_resmi_gazete_getir`) okundu.*
