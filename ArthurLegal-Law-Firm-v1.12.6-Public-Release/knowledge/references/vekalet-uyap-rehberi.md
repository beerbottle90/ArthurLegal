# Vekalet İşlemleri + UYAP Rehberi

> Avukatın müvekkili adına işlem yapma yetkisini düzenler.
> Vekalet türleri, özel yetkiler, ibraz, UYAP'a sunum, azil ve çekilme.
> Uygulama skill'i: `/firm-operations:vekalet-sablon`.

---

## Hukuki dayanak (24.09.2026'da `tr_mevzuat_madde_getir` ile doğrulandı)

- **AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168)**
  - m. 41: Avukatın vekâletten çekilmesi (görev, tebliğden itibaren 15 gün sürer)
  - m. 56: Örnek çıkarabilme ve tebligat yapabilme hakkı (avukat onaylı vekâletname örneği, yetki belgesi, tek tip vekâletname)
  - m. 171: İşi sonuna kadar takip ve tevkil
  - m. 174: Takipten vazgeçme, azil ve ücret
- **HUKUK MUHAKEMELERİ KANUNU (Kanun No. 6100, RG sayı 27836)**
  - m. 74: Davaya vekâlette özel yetki gerektiren hâller
  - m. 75: Birden fazla vekil
  - m. 76: Vekâletnamenin ibrazı
  - m. 77: Vekâletnamesiz dava açılması ve işlem yapılması
- **TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG sayı 27836) m. 512** — vekâlet sözleşmesinin tek taraflı sona erdirilmesi
- **CEZA MUHAKEMESİ KANUNU (Kanun No. 5271, RG sayı 25673) m. 149, m. 150** — müdafi seçimi ve görevlendirilmesi

> **Düzeltme (24.09.2026):** Önceki sürüm Av. K. m. 32'yi "vekaletname noter onaylı olmalı" kuralı, m. 35'i "müdafilikte
> yazılı talep yeterli" kuralı, m. 41'i "azil + istifa" maddesi olarak gösteriyordu. **m. 32 mülgadır**
> (30/1/1979 - 2178/8). m. 35 "yalnız avukatların yapabileceği işler"dir. m. 41 yalnız avukatın çekilmesini düzenler;
> azlin ücret sonucu m. 174/2'dedir. HMK m. 74 listesi de metinle birebir değildi; aşağıda düzeltildi.

---

## Vekalet türleri — pratik tablo

| Tip | Kapsam | Şekil | Dayanak |
|---|---|---|---|
| **Genel vekalet** | Müvekkilin tüm dava ve işleri | Tek tip vekâletname; dosyaya noter onaylı/düzenlenmiş aslı veya avukat onaylı örneği | Av. K. m. 56/6; HMK m. 76/1 |
| **Özel vekalet** | Belirli iş | Aynı | Aynı |
| **Özel yetkili vekalet** | HMK m. 74'teki işlemler | Yetki **açıkça** yazılmalı | HMK m. 74 |
| **Yetki belgesi** | Avukatın tevkil yetkili tüm vekâletnameleri | Vekâletname hükmünde | Av. K. m. 56/5 |
| **Seçilmiş müdafi** | Ceza dosyası | Vekâletname ibraz zamanı bu rehberde doğrulanmadı | CMK m. 149 |
| **Görevlendirilen müdafi** | CMK kapsamında zorunlu veya istem üzerine müdafilik | Baro görevlendirmesi | CMK m. 150 |
| **Vekâletnamesiz acil işlem** | Gecikmesinde zarar doğabilecek hâller | Mahkeme kesin süre vererek izin verebilir | HMK m. 77/1 |

---

## HMK m. 74 — Özel yetki gerektiren işlemler

Açıkça yetki verilmemiş ise vekil (metindeki sırayla):

- sulh olamaz
- hâkimi reddedemez
- davanın tamamını ıslah edemez
- yemin teklif edemez; yemini kabul, iade veya reddedemez
- başkasını tevkil edemez
- haczi kaldıramaz
- müvekkilinin iflasını isteyemez
- tahkim ve hakem sözleşmesi yapamaz
- konkordato veya sermaye şirketleri ve kooperatiflerin uzlaşma yoluyla yeniden yapılandırılması teklifinde bulunamaz, bunlara muvafakat veremez
- alternatif uyuşmazlık çözüm yollarına başvuramaz
- davadan veya kanun yollarından feragat edemez
- karşı tarafı ibra edemez ve davasını kabul edemez
- yargılamanın iadesi yoluna gidemez
- hâkimlerin fiilleri sebebiyle Devlet aleyhine tazminat davası açamaz
- hangileri hakkında yetki verildiği açıklanmadıkça kişiye sıkı sıkıya bağlı haklarla ilgili davaları açamaz ve takip edemez

Önceki sürümdeki "hâkim/bilirkişi reddini geri alma", "ölmüş kimsenin hatırasına ait dava", "kambiyo taahhüdü" ve
"şikâyet / şikâyetten vazgeçme" kalemleri HMK m. 74'te **yoktur**. Bunlar için başka bir kanunda özel yetki aranıp
aranmadığı ayrıca doğrulanmalı.

Vekaletnamede bu yetkiler **açıkça** yer almıyorsa vekil bu işlemleri yapamaz.

---

## Noter vekaletnamesi pratiği

### Süreç

1. Müvekkille noter randevusu (genelde 30-60 dk)
2. Yetki listesi önceden hazırlanır (`/firm-operations:vekalet-sablon`)
3. Noterde müvekkil + (varsa) tercüman, **kimlikle** imza
4. Noter ücreti: `[DOLDUR — TL aralık]`
5. Noterin mühürlü ve numaralı nüshası alınır

### İçerik

Vekâletnameler Türkiye için **tek tiptir**; biçim ve içeriğini Türkiye Barolar Birliği ile Türkiye Noterler Birliği
hazırlar (Av. K. m. 56/6). Büro yalnız eklenecek yetkileri belirler:

```
EKLENECEK YETKİLER (örnek)

1. Dava açma, davaya cevap verme, takip
2. HMK m. 74 özel yetkileri — işe göre işaretlenenler:
   - sulh olmak
   - davayı kabul, davadan ve kanun yollarından feragat
   - karşı tarafı ibra
   - tahkim ve hakem sözleşmesi yapmak
   - alternatif uyuşmazlık çözüm yollarına başvurmak
   - başkasını tevkil etmek
   - [diğerleri — işe göre]
3. UYAP üzerinden işlem ve tebligat
4. Karşı taraftan tahsil edilecek paraları almak
```

### Yabancı ülkede düzenlenen vekaletname

Onay (apostil veya konsolosluk) ve yeminli tercüme gereklilikleri bu rehberde **doğrulanmadı**; noterle teyit et.

---

## UYAP'a vekalet sunumu

### İbraz kuralı

- Avukat, açtığı veya takip ettiği dava ve işlerde, noter onaylı ya da düzenlenmiş vekâletname aslını veya avukat
  tarafından onaylanmış aslına uygun örneğini dosyaya ibraz etmek zorundadır (HMK m. 76/1).
- Avukatın onayladığı vekâletname örneği tüm yargı mercileri, resmi daireler ve kişiler için resmi örnek hükmündedir
  (Av. K. m. 56/1). Aslı olmayan belgenin örneğini onaylamak üç yıldan altı yıla kadar hapis cezası gerektirir (m. 56/3).
- Vekâletnamesini vermeyen avukat dava açamaz ve yargılamayla ilgili işlem yapamaz. Gecikmesinde zarar doğabilecek
  hâllerde mahkeme kesin süre vererek izin verebilir; süre içinde vekâletname verilmez veya asıl taraf işlemleri kabul
  ettiğini dilekçeyle bildirmezse dava açılmamış veya işlem yapılmamış sayılır (HMK m. 77/1).
- Kamu kurum ve kuruluşlarının avukatları için yetkili amirin verdiği temsil belgesi geçerlidir (HMK m. 76/2).

### E-vekalet sunumu

UYAP Avukat Portalı üzerinden:
1. Vekaletnameyi tarayıp PDF olarak yükle
2. Dosya numarasıyla ilişkilendir
3. E-tebligatların akışını kontrol et

### Manuel sunum

- Mahkeme kalemine vekaletname örneği bırak
- Gider avansı ödenir
- Karar ve tebligat fiziki olarak gelir

---

## Azil + çekilme prosedürü

### Müvekkilin azli

- Vekâlet veren sözleşmeyi **her zaman** tek taraflı sona erdirebilir; uygun olmayan zamanda sona erdiren taraf
  diğerinin zararını giderir (TBK m. 512)
- Yazılı bildirim + dosyaya ve UYAP'a bildirim
- **Ücret:** azilde ücretin **tamamı** ödenir; avukat kusur veya ihmali nedeniyle azledilmişse ödenmez (Av. K. m. 174/2).
  Önceki sürümdeki "yalnız yapılmış işe isabet eden ücret" kuralı madde metninde yoktur.

### Avukatın çekilmesi (Av. K. m. 41)

- Belli bir işi takipten veya savunmadan isteğiyle çekilen avukatın vekâlet görevi, durumun müvekkile
  **tebliğinden itibaren 15 gün** devam eder (m. 41/1). Bu bir "15 gün önceden bildirim" kuralı değildir.
- Adli müzaharet bürosu veya baro başkanının tayin ettiği avukat, kaçınılmaz sebep veya haklı özür olmadıkça
  görevden çekinemez (m. 41/2)
- Haklı sebep olmadan takipten vazgeçen avukat ücret isteyemez, peşin aldığı ücreti iade eder (Av. K. m. 174/1)
- Avukatın istifası veya azli sebebiyle yargılama başka güne bırakılamaz (HMK m. 77/4)
- KEP veya iadeli taahhütlü posta

### Disiplin riski

- Yetersiz takip → baro disiplin
- Müvekkili bilgilendirmeden çekilme → baro disiplin + tazminat
- Vekalet ücreti tartışması → ücret alacağı davası (TBK m. 502 vd.; yol ve görevli mahkeme bu rehberde doğrulanmadı)

---

## UYAP Avukat Portalı kullanım

### Modüller

| Modül | İşlev |
|---|---|
| **Dosya Sorgulama** | Esas/karar no ile dosya arama |
| **Dilekçe Sunumu** | Dilekçeyi PDF olarak yükle, otomatik teslim |
| **E-Tebligat** | Mahkeme + idare e-tebligatlarını al (KEP gerekli) |
| **Vekaletname Sunumu** | E-vekalet yükleme |
| **Duruşma Takvimi** | Önümüzdeki duruşmalar listesi |
| **Karar Sorgu** | Verilen kararlar |
| **Bedesten** | Yargıtay/Danıştay birleşik karar arama |

### Avukat oturumu

- E-imza veya mobil imza ile giriş
- Sicil no + baro üyeliği aktif olmalı
- Her ortak/avukat kendi oturumunu açar

### Pratik notlar

- **E-tebligat günlük kontrol** — özellikle süre kritik matter'larda
- **Dilekçe sunumu** son gün ofis saatleri içinde başla (sistem yoğunluğu)
- **Yedek** — UYAP'tan indirilen her belge matter klasörüne kopya
- UYAP **gece bakımı** — planlı işlemde dikkat (saat aralığı varsayımsal; resmi duyurudan kontrol et)

---

## Atıf disiplini

- Madde atfı: `tr_mevzuat_madde_getir` yanıtındaki `citation` alanı birebir
- `[ArthurLegal TR — Av. K. m. 41 / 56 / 171 / 174 — GG.AA.YYYY]`
- `[ArthurLegal TR — HMK m. 74-77 — GG.AA.YYYY]`
- `[Noter onaylı vekaletname — yevmiye no — GG.AA.YYYY]`
- `[UYAP — dosya işlemi no — GG.AA.YYYY HH:MM]`

---

## Yaygın hatalar

1. **HMK m. 74 özel yetkisi** yazılmamış vekaletnameyle sulh imzalamak → vekil bu işlemi yapamaz (HMK m. 74)
2. **Vekâletname ibraz edilmeden işlem yapmak** → mahkeme kesin süre vermemişse işlem yapılamaz; süre içinde getirilmezse işlem yapılmamış sayılır (HMK m. 77/1)
3. **Yabancı vekaletnameyi onay ve tercüme gerekliliklerini kontrol etmeden sunmak** (gereklilikler bu rehberde doğrulanmadı)
4. **Azil bildirilmeden karşı tarafla görüşmek** → meslek kuralı sorunu (kural metni bu rehberde doğrulanmadı)
5. **Çekilmede 15 günü "önceden bildirim" sanmak** → görev tebliğden itibaren 15 gün sürer (Av. K. m. 41/1)
6. **Av. K. m. 32'yi dayanak göstermek** → madde mülgadır
