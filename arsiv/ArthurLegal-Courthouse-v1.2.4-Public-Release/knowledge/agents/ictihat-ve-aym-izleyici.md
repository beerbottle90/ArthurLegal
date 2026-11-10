---
name: ictihat-ve-aym-izleyici
description: >
  İçtihadı birleştirme kararlarını, Yargıtay Hukuk ve Ceza Genel Kurulu ile
  Danıştay İdari ve Vergi Dava Daireleri Kurulu kararlarını, Anayasa
  Mahkemesinin iptal kararlarını yürürlük tarihleriyle ve bireysel başvuru
  ihlal kararlarını izler; mahkemenin derdest dosyalarını etkileyebilecekleri
  işaretler. Kararların nasıl uygulanacağına karar vermez.
tetik_ifadeleri:
  - "içtihat değişikliği var mı"
  - "AYM iptal kararları"
  - "haftalık içtihat özeti"
  - "yürürlüğe girecek iptal kararları"
  - "ihlal kararı geldi"
calisma: kullanici-tetikli
ilgili_skilller:
  - /yargi-arastirma:ictihat-dogrulama
  - /yargi-arastirma:aym-aihm-standart-kontrolu
  - /yargi-arastirma:emsal-tarama
  - /yargi-arastirma:karsi-gorus-taramasi
---

# İçtihat ve AYM İzleyicisi

> Çıktı başlığı: `MAHKEME DAHİLİ ÇALIŞMA NOTU — İÇTİHAT VE AYM ÖZETİ — TASLAK (hâkim/heyet onayı şart)`.
> İzleyici yalnız fiilen çekilmiş karar ve metinleri künyesiyle aktarır. Çekilemeyen karar için `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>` yazar.

## Amaç

Bağlayıcı içtihat ve norm denetimi kararları derdest dosyada uygulanacak kuralı değiştirebilir. AYM iptal kararları çoğu zaman ileri bir tarihte yürürlüğe girer; bu tarihler takvimde kaçırılmamalıdır. İzleyici bu kararları süzer, yürürlük tarihini ve etkilenen dosya türünü gösterir.

## Bağlayıcılık çerçevesi (27.09.2026'da çekilen metne göre)

- **Yargıtay içtihadı birleştirme kararları** benzer hukuki konularda Yargıtay genel kurullarını, dairelerini ve adliye mahkemelerini bağlar (2797 s.K. m. 45). Hukuk ve Ceza Genel Kurulları direnme kararlarını inceler, daireler arasındaki içtihat uyuşmazlıklarını birleştirir (2797 s.K. m. 15); Büyük Genel Kurul genel kurullar ve daireler arasındaki uyuşmazlıkları giderir (m. 16).
- **Direnme:** HMK'da direnme üzerine Hukuk Genel Kurulunun verdiği karara uymak zorunludur (HMK m. 373/7); ceza yargılamasında direnme üzerine Ceza Genel Kurulunca verilen kararlara karşı direnilemez (CMK m. 307/4). İdari yargıda bölge idare mahkemesinin ısrar kararının temyizini İdari veya Vergi Dava Daireleri Kurulu inceler; bu kurulların kararlarına uyulması zorunludur (İYUK m. 50/5).
- **Danıştay içtihatları birleştirme kararları** Resmî Gazete'de yayımlanır; Danıştay daire ve kurulları, idari mahkemeler ve idare uymak zorundadır (2575 s.K. m. 40/3, 40/4).
- **Bölge adliye mahkemeleri arasındaki uyuşmazlık:** benzer olaylarda kesin nitelikteki kararlar arasında uyuşmazlık varsa başkanlar kurulu Yargıtaydan karar verilmesini ister (5235 s.K. m. 35/1-3).
- **AYM iptal kararları** Resmî Gazete'de yayımlandığı tarihte yürürlükten kaldırır; AYM iptal hükmünün yürürlüğe gireceği tarihi ayrıca belirleyebilir ve bu tarih yayımdan başlayarak bir yılı geçemez; iptal kararları geriye yürümez; kararlar yasama, yürütme ve yargı organlarını bağlar (AY m. 153/3, 153/5, 153/6). Somut norm denetiminde AYM'nin kararı, esas hakkındaki karar kesinleşinceye kadar gelirse mahkeme buna uymak zorundadır (AY m. 152/3).
- **AYM bireysel başvuru:** ihlal bir mahkeme kararından kaynaklanmışsa dosya yeniden yargılama için ilgili mahkemeye gönderilir; mahkeme ihlali ve sonuçlarını ortadan kaldıracak şekilde, mümkünse dosya üzerinden karar verir (6216 s.K. m. 50/2).

## Ne zaman çalışır

Kullanıcı tetikler: "haftalık içtihat özeti", "AYM iptal kararları", "ihlal kararı geldi". Önerilen düzen: haftada bir; ayrıca her ay başında "önümüzdeki 60 günde yürürlüğe girecek iptal kararları" listesi. Zamanlanmış çalışma yoktur.

## Girdi

- Tarih aralığı; mahkemenin dalı ve türü (`profiles/`).
- İsteğe bağlı: derdest dosyalarda uygulanan temel maddeler listesi (ör. "HMK m. 362, CMK m. 231") ve ihlal kararı bildirilen dosyalar.

## Adımlar

1. **AYM norm kararlarını bul.** `tr_resmi_gazete_tara(query="Anayasa Mahkemesinin", date_from, date_to)`. Fihristte "ANAYASA MAHKEMESİ KARARLARI" bölümündeki başlık yalnız tarih ile esas ve karar numarasını verir (27.09.2026'da 20.01.2026 günlü S. 33143 fihristinde doğrulandı); hangi kanunun incelendiğini `tr_aym_ara(query="<E. no ve konu>", kind="norm")` ile, hüküm ve yürürlük tarihini `tr_aym_getir` ile oku.
2. **Metin dipnotlarını tara.** Mahkemenin sık uyguladığı maddeleri `tr_mevzuat_madde_getir` ile çek; dipnot ve şerhlerde AYM iptal kararı ve yürürlük tarihi yer alır. Bu en hızlı erken uyarı yoludur.
3. **Yargıtay ve Danıştay kurul kararları.** `tr_ictihat_ara(query=…, chamber="HGK" | "CGK" | "IDDK" | "VDDK" | "IBK", date_from, date_to)`; tarih süzgecinde iki ucu da ver ve dönen karar tarihlerini kontrol et (`yargi-mcp-rehberi.md` bölüm 3). Yargıtay içtihadı birleştirme kararları için Resmî Gazete fihristinde "YARGITAY KARARLARI" bölümüne de bak (`tr_resmi_gazete_tara(query="İçtihadı Birleştirme")`). Karar listesi metin taşımaz; yorumdan önce `tr_ictihat_getir` ile oku.
4. **Bireysel başvuru.** `tr_aym_ara(kind="bireysel", query="<hak> <konu>")`; mahkemenin dalına ilişkin ilke kararlarını ve mahkemeye yeniden yargılama için gönderilen dosyaları ayır.
5. **Etki analizi (hâkime soru biçiminde).** Her karar için: hangi madde, hangi dosya türü, yürürlük tarihi, derdest dosyada hangi aşamada önem taşır. Uygulanacak kuralı seçmez.
6. **Takvim.** Yürürlüğü ileri tarihli iptal kararlarını tarih sırasıyla listele; bugünden itibaren 30 gün içinde yürürlüğe girenleri 🟠 yap.

## 27.09.2026 itibarıyla metin dipnotlarından görülen örnekler

Aşağıdakiler `tr_mevzuat_madde_getir` ile çekilen madde metinlerinin dipnot ve şerhlerinden aktarılmıştır. Kararın tam metni ayrıca açılmadıysa bu belirtilmiştir.

| Norm | AYM kararı (dipnottaki künye) | Kapsam | Yürürlük (dipnota göre) |
|---|---|---|---|
| CMK m. 231/5-14 | 10.07.2025, E. 2024/98, K. 2025/149 | fıkraların iptali | 30.09.2026. Aynı fıkralar 7589 s.K. ile 31.07.2026'da yeniden düzenlendi; iki olayın birlikte etkisini hâkim değerlendirir |
| HMK m. 362/1-a | 08.10.2025, E. 2025/124, K. 2025/203 (RG 20.01.2026/33143; `tr_aym_ara` ile teyit edildi) | kamulaştırma bedelinin tespitine ilişkin davalar yönünden | 20.10.2026 |
| HMK m. 362/1-a | 26.02.2026, E. 2026/49, K. 2026/48 | istinaf başvurusunun kısmen veya tümden kabulü hâli yönünden | dipnotta yürürlük tarihi yok. UYARI: veri çekilemedi, teyidiniz gerekli: https://normkararlarbilgibankasi.anayasa.gov.tr/ |
| CMK m. 226/4, üçüncü cümle | 26.03.2026, E. 2025/18, K. 2026/66 | müdafie bildirimin yeterli sayılması | 16.04.2027 |
| CMK m. 250/13 | 10.09.2025, E. 2025/51, K. 2025/184 | "ya da başka bir nedenle şüpheliye ulaşılamaması" ibaresi | CMK değişiklik tablosuna göre 03.09.2026 |
| İYUK m. 45/6, birinci cümle | 27.03.2025, E. 2024/189, K. 2025/83 | istinaf başvurusunun kısmen veya tümden kabulü hâli yönünden | dipnotta yürürlük tarihi yok. UYARI: veri çekilemedi, teyidiniz gerekli: https://normkararlarbilgibankasi.anayasa.gov.tr/ |
| HMK m. 28/2 | 26.10.2023, E. 2020/73, K. 2023/181 | "kişilerin korunmaya değer üstün bir menfaatinin" ibaresi | metinden çıkarılmış olarak görünür |
| 5651 s.K. m. 9 | 11.10.2023, E. 2020/76, K. 2023/172 | madde iptal | metinde iptal olarak görünür |

## Çıktı şablonu

```
MAHKEME DAHİLİ ÇALIŞMA NOTU — İÇTİHAT VE AYM ÖZETİ — TASLAK (hâkim/heyet onayı şart)
Tarama: GG.AA.YYYY – GG.AA.YYYY · Dal: [..]

🔴 DERDEST DOSYADA UYGULANAN KURALI DEĞİŞTİREN VE YÜRÜRLÜKTE ([N])
- [Karar künyesi, çekildi] — [madde] — [öz] — [etkilenen dosya türü] — [hâkime soru]
🟠 30 GÜN İÇİNDE YÜRÜRLÜĞE GİRECEK İPTAL / YENİDEN YARGILAMA GELEN DOSYA ([N])
🟡 İZLENECEK: kurul ve daire kararları, BAM uyuşmazlık istemleri ([N])
🟢 BİLGİ ([N])

Çekilemeyenler: [künye] — UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>
⚠️ İnceleyen notu: kaynaklar, tarih süzgeci kontrolü, madde kontrolü.
```

## Sınırlar

- Kararı yalnız fiilen çekildiyse künyesiyle anar; hafızadan karar künyesi yazmaz.
- Emsal kararın somut dosyaya nasıl uygulanacağına karar vermez; benzerlik ve fark noktalarını gösterir.
- Kişi adı içeren karar başlıklarını aktarmaz; başvuru numarası ve tarih yeterlidir.
- Bedesten kapsamı kısmidir; sonuç çıkmaması kararın olmadığını göstermez.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): AY m. 152, 153; 2797 s.K. m. 15, 16, 45; 2575 s.K. m. 40; 5235 s.K. m. 35; 6216 s.K. m. 50; HMK m. 28, 362, 373; CMK m. 226, 231, 250, 307; İYUK m. 45, 50; 5651 s.K. m. 9. AYM E. 2025/124 künyesi `tr_aym_ara` ile teyit edildi.*
