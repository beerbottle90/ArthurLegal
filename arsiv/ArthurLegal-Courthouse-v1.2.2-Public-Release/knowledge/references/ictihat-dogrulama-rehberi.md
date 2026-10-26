# İçtihat Doğrulama Rehberi — Künye ve İçerik Kontrolü

> `yargi-arastirma:ictihat-dogrulama` skill'i ve bütün hâkim plugin'leri, bir karar künyesini gerekçeye, ara karara veya çalışma notuna koymadan önce bu rehbere bakar. Amaç, var olmayan, yanlış künyeli veya içeriği çarpıtılmış kararın karara girmesini önlemektir.
> Araç ayrıntısı: `yargi-mcp-rehberi.md`. Madde ve künye kontrolü 27.09.2026'da ArthurLegal MCP ile yapılmıştır.

## Neden

Taraf dilekçelerinde, bilirkişi raporlarında ve yapay zekâ çıktılarında künyesi hatalı ya da hiç var olmayan kararlar görülebilir. Gerekçede atıf yapılan kararın içeriğinin yanlış aktarılması, gerekçeli karar hakkı bakımından da risktir (bkz. `gerekceli-karar-hakki-rehberi.md`). Kural: bu sohbette çekilmemiş karar künyesi gerekçe gövdesine girmez.

## Doğrulama adımları

1. **Künyeyi ayrıştır.** Mahkeme ve daire, esas numarası, karar numarası, karar tarihi. Eksik unsur varsa not et; eksik künye "doğrulandı" sayılmaz.
2. **Ara.** `tr_ictihat_ara` ile:
   - `courts`: Yargıtay için `YARGITAYKARARI`, Danıştay için `DANISTAYKARAR`, BAM hukuk için `ISTINAFHUKUK`, ilk derece hukuk için `YERELHUKUK`.
   - `chamber`: `H1`-`H23`, `C1`-`C23`, `HGK`, `CGK`, `D1`-`D17`, `IDDK`, `VDDK`, `IBK`.
   - `query`: esas numarasını **eğik çizgi olmadan**, yıl ile sıra numarası arasında boşlukla ve tırnak içinde yaz. 27.09.2026'daki denemede `"2009/11668"` sorgusu Bedesten'den "Sadece harf ve rakam içeren aramalar yapılabilir" hatası döndü; `"2009 11668"` sorgusu (`courts=["YARGITAYKARARI"]`, `chamber="C9"`) Yargıtay 9. Ceza Dairesinin E. 2009/11668, K. 2011/2181, 11.04.2011 tarihli kararını buldu. `yargi-mcp-rehberi.md` bölüm 3 aynı boşluklu biçimi kullanır.
   - Tarih süzgeci kullanırsan iki ucu da ver ve dönen karar tarihlerinin aralıkta olduğunu kontrol et.
3. **Metni aç.** `tr_ictihat_getir(document_id=…)`. Liste metin taşımaz; yorum ve alıntı yalnız açılan metinden yapılır.
4. **Künyeyi eşleştir.** Daire, esas, karar ve tarih metindeki bilgiyle birebir aynı mı? Tek unsur farklıysa künye "düzeltildi" olarak kaydedilir; düzeltme kaynağı yazılır.
5. **İçeriği eşleştir.** Kararın, atıf yapan metinde yüklenen ilkeyi gerçekten içerip içermediğine bak. Alıntı varsa metinde birebir bul; bulunamıyorsa "alıntı metinde yok" yaz.
6. **Güncelliği kontrol et.** Karardan sonra içtihadı birleştirme kararı, genel kurul kararı veya AYM kararı çıkmış mı (`ictihat-ve-aym-izleyici`)? Kararın dayandığı madde değişmiş mi (`tr_mevzuat_madde_getir` şerh ve dipnotları)? Örnek: HMK m. 107 (belirsiz alacak davası) 7589 s.K. ile yürürlükten kaldırılmıştır; bu maddeye dayanan kararlar yalnız geçiş hükmü kapsamındaki eski davalar için anlam taşır.
7. **Ağırlığı belirle** (aşağıdaki tablo) ve çıktıya "Doğrulama sonucu" satırı ekle.

## Bağlayıcılık ve ağırlık (metne göre)

| Karar türü | Etkisi | Dayanak |
|---|---|---|
| Yargıtay içtihadı birleştirme kararı | benzer hukuki konularda Yargıtay genel kurullarını, dairelerini ve adliye mahkemelerini bağlar | 2797 s.K. m. 45 |
| Danıştay içtihatları birleştirme kararı | Danıştay daire ve kurulları, idari mahkemeler ve idare uymak zorundadır | 2575 s.K. m. 40/4 |
| HGK'nın direnme üzerine kararı | o dosyada uyulması zorunlu | HMK m. 373/7 |
| CGK'nın direnme üzerine kararı | karşı direnilemez | CMK m. 307/4 |
| İDDK ve VDDK'nın ısrar üzerine kararı | uyulması zorunlu | İYUK m. 50/5 |
| AYM kararları | yasama, yürütme ve yargı organlarını bağlar | AY m. 153/6 |
| AYM bireysel başvuru ihlal kararı | yeniden yargılama; ihlal ve sonuçlarının giderilmesi | 6216 s.K. m. 50/2 |
| Yargıtay ve Danıştay daire kararları, BAM kararları | ikna edici emsal; bağlayıcılık kanunda öngörülmemiştir | — |

BAM hukuk veya ceza daireleri arasında kesin nitelikteki kararlarda uyuşmazlık varsa başkanlar kurulu Yargıtaydan karar verilmesini ister (5235 s.K. m. 35/1-3); böyle bir uyuşmazlık kararı bulunursa ağırlığı ayrıca belirtilir.

## Uyarı işaretleri

- Künye biçimi olağan dışı (ör. karar numarası esas numarasından önceki yıla ait, daire adı eksik).
- Arama sonuç vermiyor. Bedesten kapsamı kısmidir; sıfır sonuç yokluk kanıtı değildir, ama künye doğrulanmış da sayılmaz.
- Metin bulundu, fakat atfedilen ilke metinde yok veya bağlamı farklı (ör. karşı oy gerekçesinden alıntı çoğunluk görüşü gibi sunulmuş).
- Karar tarihi, kararın dayandığı kanun maddesinin yürürlüğünden önce veya iptalinden sonra.

## Çekilemeyen künye

Karar çekilemiyorsa künye gerekçe gövdesine yazılmaz; İnceleyen notunda aynen şu satır kullanılır:

- Yargıtay: `UYARI: veri çekilemedi, teyidiniz gerekli: https://karararama.yargitay.gov.tr/`
- Danıştay: `UYARI: veri çekilemedi, teyidiniz gerekli: https://karararama.danistay.gov.tr/`
- BAM ve ilk derece: `UYARI: veri çekilemedi, teyidiniz gerekli: https://emsal.uyap.gov.tr/`
- AYM: `UYARI: veri çekilemedi, teyidiniz gerekli: https://kararlarbilgibankasi.anayasa.gov.tr/` (bireysel), `https://normkararlarbilgibankasi.anayasa.gov.tr/` (norm)

## Çıktı biçimi

```
DOĞRULAMA SONUCU — [künye]
- Bulundu mu: evet / hayır (arama: courts, chamber, query)
- Künye eşleşmesi: tam / düzeltildi (neden) / eşleşmedi
- İçerik eşleşmesi: ilke metinde var / yok / bağlam farklı
- Güncellik: sonraki İBK, genel kurul, AYM kararı; dayandığı maddenin durumu
- Ağırlık: [tablodan]
- Kullanım: gerekçe gövdesine girebilir / yalnız İnceleyen notunda / kullanılmamalı
```

## Kişisel veri

Karar başlığında kişi adı geçse bile çıktıda künye esas ve karar numarasıyla verilir; AYM bireysel başvuru kararlarında başvuru numarası ve tarih yeterlidir.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): 2797 s.K. m. 45; 2575 s.K. m. 40; HMK m. 107, 373; CMK m. 307; İYUK m. 50; AY m. 153; 6216 s.K. m. 50; 5235 s.K. m. 35. Örnek künye `tr_ictihat_ara` ile bulundu.*
