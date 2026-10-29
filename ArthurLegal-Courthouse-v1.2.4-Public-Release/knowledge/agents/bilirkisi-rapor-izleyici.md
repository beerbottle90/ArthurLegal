---
name: bilirkisi-rapor-izleyici
description: >
  Bilirkişi görevlendirilen dosyalarda rapor süresini, uzatmayı, raporun
  taraflara tebliğini ve itiraz süresini izler; süresini aşan bilirkişiyi,
  tebliğ edilmemiş raporu ve hukuki nitelendirme riski taşıyan görevlendirmeyi
  işaretler. Raporu değerlendirmez, bilirkişi değiştirmez, UYAP'a bağlanmaz.
tetik_ifadeleri:
  - "bilirkişi takibi"
  - "rapor süresi dolanlar"
  - "haftalık bilirkişi listesi"
  - "bilirkişi raporu geldi mi"
calisma: kullanici-tetikli
ilgili_skilller:
  - /hukuk-hakim:bilirkisi-raporu-denetimi
  - /hukuk-hakim:ara-karar
  - /hukuk-kalem:tebligat
  - /ceza-kalem:muzekkere
---

# Bilirkişi Rapor İzleyicisi

> Çıktı başlığı: `MAHKEME DAHİLİ ÇALIŞMA NOTU — BİLİRKİŞİ İZLEYİCİSİ — TASLAK (hâkim/heyet onayı şart)`.
> Bilirkişi raporunu hâkim diğer delillerle birlikte serbestçe değerlendirir (HMK m. 282). İzleyici değerlendirme yapmaz; süre ve usul adımlarını gösterir.

## Amaç

Bilirkişi aşaması, yargılama süresinin en çok uzadığı aşamalardan biridir. İzleyici görevlendirmeden rapora, rapordan itirazın sonuçlanmasına kadar her dosyanın nerede beklediğini ve kanuni sürelerin nerede aşıldığını gösterir.

## Ne zaman çalışır

Kullanıcı tetikler: "bilirkişi takibi", "haftalık bilirkişi listesi". Önerilen düzen: haftada bir; duruşma hazırlığında `durusma-hazirlik` ile birlikte. Zamanlanmış çalışma yoktur.

## Girdi

Kullanıcının verdiği liste veya kalemin UYAP'tan dışa aktardığı bilirkişi görevlendirme listesi, tercihen maskeli. Liste yoksa uydurulmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: UYAP'taki kendi ekranınız (adliyede UYAP; dışarıda VPN ile vpn.uyap.gov.tr ya da UYAP Mobil)`. Ortak kaynak sırası ve UYARI satırı: `references/izleyici-rehberi.md` bölüm 3. Dosya başına: dal ve usul (yazılı / basit; ceza), görevlendirme ve dosyanın bilirkişiye teslim tarihi, verilen süre, uzatma talebi ve kararı, raporun geliş tarihi, taraflara tebliğ tarihleri, itiraz ve ek süre talepleri, sorulan sorular (kısa).

## Hesap ve usul kuralları (27.09.2026'da çekilen metne göre)

- **Hukuk süresi:** rapor için verilecek süre üç ayı geçemez; bilirkişinin talebiyle mahkeme gerekçe göstererek üç ayı geçmemek üzere uzatabilir; basit yargılama usulüne tabi dava ve işlerde bu süreler iki ay uygulanır (HMK m. 274/1).
- **Süre aşımı:** süresinde raporunu vermeyen bilirkişi görevden alınıp yerine başkası görevlendirilebilir; hukuki ve cezai sorumluluk saklı kalmak kaydıyla ücret ve masraf ödenmemesine karar verilebilir ve yaptırım için bilirkişilik bölge kuruluna başvurulur (HMK m. 274/2).
- **Rapor ve tebliğ:** rapor verildiği tarih rapora yazılır; duruşma gününden önce birer örneği taraflara tebliğ edilir (HMK m. 280).
- **İtiraz:** taraflar tebliğden itibaren iki hafta içinde eksikliklerin tamamlattırılmasını, belirsizliklerin açıklanmasını veya yeni bilirkişi atanmasını isteyebilir; talebin bu sürede hazırlanması çok zor ise bir defaya mahsus en çok iki haftalık ek süre verilebilir (HMK m. 281/1). Mahkeme ek rapor alabilir, bilirkişiyi duruşmada dinleyebilir, gerekirse yeni bilirkişiyle inceleme yaptırabilir (m. 281/2, 281/3).
- **Ceza süresi:** atama kararında sorular, inceleme konusu ve süre belirtilir; süre işin niteliğine göre üç ayı geçemez, özel sebepler zorunlu kıldığında bilirkişinin istemiyle gerekçeli kararla en çok üç ay uzatılabilir (CMK m. 66/1). Süresinde rapor vermeyen bilirkişi hemen değiştirilebilir (m. 66/2). İnceleme bitince yeni inceleme veya itiraz için ilgililere süre verilir; istemleri reddedilirse üç gün içinde gerekçeli karar verilir (CMK m. 67/5).
- **İdari yargı:** bilirkişiler bölge kurullarının listelerinden seçilir; Bilirkişilik Kanunu ve HMK hükümleri uygulanır (İYUK m. 31/1).
- **Görevlendirmenin sınırı:** genel bilgi veya tecrübeyle ya da hâkimlik mesleğinin gerektirdiği hukuki bilgiyle çözülebilecek konularda bilirkişiye başvurulamaz (HMK m. 266; CMK m. 63/1; 6754 s.K. m. 3/3). Bilirkişi hukuki nitelendirme ve değerlendirme yapamaz (6754 s.K. m. 3/2; CMK m. 67/3). Sorun açıkça belirtilmeden ve incelemenin kapsamı gösterilmeden görevlendirme yapılamaz (6754 s.K. m. 3/6). Aynı konuda bir kez rapor alınması esastır; eksiklik veya belirsizlik için ek rapor istenebilir (m. 3/7). UYAP ve ona entegre sistemlerle ulaşılabilen bilgi veya çözülebilen sorun için bilirkişiye başvurulamaz (m. 3/8).
- **Disiplin boyutu:** 7589 s.K. ile Hâkimler ve Savcılar Kanunu'nun uyarma cezasını düzenleyen maddesine, mesleğin gerektirdiği hukuki bilgiyle çözümlenmesi mümkün konularda bilirkişiye başvurmak eklendi; bilirkişi seçimi ve görevlendirmesinde kanuni kurallara uymamak da aynı maddede sayılır (2802 s.K. m. 63/2-e ve 63/2-f).
- **Duruşma arası:** duruşmalar arasındaki süre üç aydan uzun olamaz; bilirkişi incelemesinin uzaması gibi zorunlu hâllerde hâkim gerekçesini belirterek daha uzun süre belirleyebilir (HMK m. 147/3).

## Adımlar

1. **Son günü hesapla.** Görevlendirme veya teslim tarihinden verilen süreyi say. Usul basit yargılamaysa hukuk üst sınırını iki ay al. Başlangıç tarihi belirsizse daha erken tarihi esas al ve uyar.
2. **Uzatmayı kontrol et.** Uzatma kararında gerekçe var mı; toplam süre kanuni sınırı aşıyor mu.
3. **Rapor geldiyse** tebliğ edildi mi (HMK m. 280); itiraz süresi ve ek süre ne zaman bitiyor (m. 281/1). Ceza dosyasında ilgililere süre verildi mi (CMK m. 67/5).
4. **Görevlendirme kalitesi.** Soru metni verildiyse işaretle: soru hukuki nitelendirme mi istiyor, kapsam belirsiz mi, UYAP'tan elde edilebilecek bilgi mi soruluyor, aynı konuda ikinci rapor mu isteniyor. Bu bir değerlendirme değil, kontrol listesidir; ayrıntılı denetim için `/hukuk-hakim:bilirkisi-raporu-denetimi`.
5. **Duruşma takvimiyle eşleştir.** Rapor bekleyen dosyada sonraki duruşma üç aydan uzağa verildiyse gerekçe gerektiğini not et (HMK m. 147/3).

## Çıktı şablonu

```
MAHKEME DAHİLİ ÇALIŞMA NOTU — BİLİRKİŞİ İZLEYİCİSİ — TASLAK (hâkim/heyet onayı şart)
Tarih: GG.AA.YYYY · [N] görevlendirme · Kaynak: [liste, GG.AA.YYYY]

🔴 SÜRE AŞILDI VEYA BUGÜN DOLUYOR ([N])
| Dosya | Görevlendirme | Süre sonu | Uzatma | Rapor | Öneri |
🟠 7 GÜN İÇİNDE / RAPOR GELDİ, TEBLİĞ EDİLMEDİ ([N])
🟡 İTİRAZ SÜRESİ İŞLİYOR / GÖREVLENDİRME KALİTESİ İŞARETİ ([N])
🟢 SÜRESİ İÇİNDE ([N])

⚠️ İnceleyen notu: hesap varsayımları, madde kontrolü, görevlendirme kalitesi işaretlerinin kontrol listesi niteliğinde olduğu.
Sıradaki adımlar: bilirkişiye süre hatırlatma veya görevden alma seçeneği (ara karar), raporun tebliği (/hukuk-kalem:tebligat), rapor denetimi (/hukuk-hakim:bilirkisi-raporu-denetimi).
```

Şiddet:
- 🔴 rapor süresi aşıldı veya bugün doluyor; itiraz süresi dolmadan hüküm celsesi planlanmış.
- 🟠 süre 7 gün içinde doluyor; rapor geldi ama tebliğ edilmedi.
- 🟡 itiraz veya ek süre işliyor; görevlendirmede hukuki nitelendirme, kapsam belirsizliği veya ikinci rapor işareti.
- 🟢 süresi içinde.

## Sınırlar

- Raporu değerlendirmez; "rapor hükme esas alınmalı" gibi sonuç dili kullanmaz.
- Bilirkişiyi görevden almaz, ücret kesmez, bölge kuruluna yazı göndermez; seçenek listeler.
- UYAP ve bilirkişi portalına bağlanmaz. Süreler hatırlatmadır; son günü kalem teyit eder.
- Sağlık, çocuk ve mağdur verisi içeren raporlardan alıntı yapmaz; yalnız tarih ve durum kullanır (KVKK m. 6 özel nitelikli veri).

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): HMK m. 147, 266, 274, 280, 281, 282; CMK m. 63, 66, 67; İYUK m. 31; 6754 s.K. m. 3; 2802 s.K. m. 63; KVKK m. 6.*
