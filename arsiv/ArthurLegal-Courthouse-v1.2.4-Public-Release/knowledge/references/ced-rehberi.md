# ÇED (Çevresel Etki Değerlendirmesi) Rehberi

> 2872 sayılı Çevre Kanunu ve ÇED Yönetmeliği kapsamındaki kararlara ("ÇED gerekli değildir", "ÇED olumlu", "ÇED olumsuz") karşı açılan iptal davalarında idare mahkemesi için usul haritası. ÇED kararları İYUK m. 20/A ivedi yargılama usulüne tabidir. Bu dosya karar vermez.

## Hukuki çerçeve

- **2872 sayılı Çevre Kanunu:** ÇED yükümlülüğünü ve idari yaptırımları düzenleyen hükümler. Bu oturumda madde metni çekilmediği için madde numarası yazılmadı; uygulamadan önce `tr_mevzuat_ara(number="2872", types=["KANUN"])` ile ilgili maddeyi çekin. `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`
- **ÇED Yönetmeliği:** karar türleri, kapsamlama, halkın katılımı toplantısı ve inceleme değerlendirme komisyonu usulü yönetmelikte düzenlenir; dava tarihinde yürürlükte olan yönetmelik metni `tr_mevzuat_ara(query="Çevresel Etki Değerlendirmesi", types=["YONETMELIK"])` ile çekilir.

## Usul: İYUK m. 20/A ivedi yargılama

İvedi yargılama usulü, 2872 s.K. uyarınca idari yaptırım kararları hariç çevresel etki değerlendirmesi sonucu alınan kararlardan doğan uyuşmazlıklarda uygulanır (İYUK m. 20/A/1-e).

| Kalem | İvedi yargılama (ÇED kararı) | Dayanak |
|---|---|---|
| Dava açma süresi | **otuz gün** | İYUK m. 20/A/2-a |
| Üst makama başvuru | uygulanmaz | İYUK m. 20/A/2-b (m. 11 hükümleri) |
| İlk inceleme | yedi gün içinde; dilekçe ve ekleri tebliğe çıkarılır | İYUK m. 20/A/2-c |
| Savunma süresi | on beş gün, bir defa en fazla on beş gün uzatılabilir; savunmanın verilmesi veya sürenin geçmesiyle dosya tekemmül eder | İYUK m. 20/A/2-d |
| Yürütmenin durdurulması | YD talebi hakkındaki kararlara itiraz edilemez | İYUK m. 20/A/2-e |
| Karar süresi | tekemmülden itibaren en geç bir ay; ara karar, keşif, bilirkişi ve duruşma ivedilikle sonuçlandırılır | İYUK m. 20/A/2-f |
| İstinaf | başvurulamaz | İYUK m. 45/8 |
| Temyiz | nihai kararlara tebliğ tarihinden itibaren **on beş gün** içinde; cevap süresi on beş gün | İYUK m. 20/A/2-g, 2-ı |
| Temyiz incelemesi | Danıştay evrak üzerinde esasa karar verebilir; temyiz üzerine verilen kararlar kesindir; temyiz istemi en geç iki ayda karara bağlanır | İYUK m. 20/A/2-i, 2-j |

- ÇED kararıyla ilgili olmayan çevre idari para cezalarında ivedi usul uygulanmaz (m. 20/A/1-e'deki istisna); bu yaptırımlarda görevli yargı yeri ve dava süresi 2872 s.K.'daki ilgili hükümden çekilerek belirlenir.
- Genel dava açma süresi özel kanunda ayrı süre yoksa idare mahkemelerinde altmış gündür (İYUK m. 7/1); ivedi yargılamada otuz gündür.
- Yetki: kanunda veya özel kanunda ayrı yetki kuralı yoksa dava konusu işlemi yapan idari merciin bulunduğu yerdeki idare mahkemesi (İYUK m. 32/1); yetki kamu düzenindendir (m. 32/2).

## Yargısal denetimde sık tartışılan unsurlar

- **Kümülatif etki:** aynı alandaki projelerin toplam etkisinin değerlendirilip değerlendirilmediği.
- **Halkın katılımı toplantısı:** yönetmelikte öngörülen usule uyulup uyulmadığı.
- **İnceleme değerlendirme komisyonu:** değerlendirmenin gerekçesi ve bilimsel dayanağı.
- **Bilirkişi ve keşif:** mahkeme dava konusu hakkında her türlü incelemeyi kendiliğinden yapar (İYUK m. 20); ivedi yargılamada bu işlemler ivedilikle sonuçlandırılır (m. 20/A/2-f). Bilirkişi seçimi ve soruların yazımı: `bilirkisilik-rehberi.md`.

## ArthurLegal MCP (`tr_`) ile çekme

```
tr_mevzuat_madde_getir(number="2577", madde_no=["20/A", "45"])   # ivedi yargılama ve istinaf yasağı
tr_mevzuat_ara(number="2872", types=["KANUN"])                    # Çevre Kanunu
tr_ictihat_ara(query="+\"çevresel etki değerlendirmesi\" +iptal", courts=["DANISTAYKARAR"], date_from="2023-01-01", date_to="2026-09-27")
```

Danıştay'da ÇED davalarına bakan daire, iş bölümü kararlarıyla belirlenir ve değişebilir; daire tahmin edilmez, `chamber` boş bırakılarak aranır ve dönen kararların dairesine bakılır.

## Bağlantılı

- [İYUK rehberi](iyuk-rehberi.md) — dava usulü
- [Yürütmenin durdurulması rehberi](yurutmenin-durdurulmasi-rehberi.md) — m. 27 ve m. 20/A
- [İdari yargı yapısı rehberi](idari-yargi-yapisi-rehberi.md)
- [Bilirkişilik rehberi](bilirkisilik-rehberi.md)

---

*Madde kontrolü (27.09.2026, ArthurLegal MCP): İYUK m. 7, 11, 20, 20/A, 27, 32, 45. 2872 s.K. maddeleri bu oturumda çekilmedi, numarasız anıldı (UYARI). Önceki sürümdeki "doğrudan Danıştay'a temyiz", Danıştay daire eşlemesi, "çevre idari para cezasında 60 gün / 30 gün" ifadeleri ile avukat bakışlı "büro pratiği" ve "hukuki argümanlar" bölümleri doğrulanamadığı veya mahkeme kullanımına uymadığı için kaldırıldı.*
