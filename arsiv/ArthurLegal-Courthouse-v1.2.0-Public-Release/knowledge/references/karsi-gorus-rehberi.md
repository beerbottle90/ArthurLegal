# Karşı Görüş Rehberi — Taslağı En Güçlü Karşı Argümanla Sınamak

> Kullanan: `yargi-arastirma:karsi-gorus-taramasi`, `yargi-arastirma:emsal-tarama`, `istinaf-hakim` skill'leri, heyet müzakeresine hazırlık.
> Amaç taraf tutmak değil, esaslı iddiaların karşılıksız kalmamasını ve gözden kaçmış bağlayıcı içtihadın bulunmasını sağlamaktır. Hangi görüşün doğru olduğuna hâkim veya heyet karar verir. Madde içerikleri 27.09.2026'da ArthurLegal MCP ile çekilen metne dayanır.

## 1. Neden

- Davanın sonucunu değiştirebilecek nitelikteki iddia ve savunmalara makul bir gerekçeyle yanıt verilmesi gerekir (AYM, B. No: 2015/439, 08.02.2018, § 22). Karşı görüş taraması bu yanıtın taslakta eksik kalmamasına yarar.
- Hukuki dinlenilme hakkı, mahkemenin açıklamaları dikkate alarak değerlendirmesini ve kararların somut ve açık gerekçelendirilmesini içerir (HMK m. 27/2-c).
- Heyet kararlarında karşı oy, gerekçesiyle birlikte karara yazılır (HMK m. 298/3; CMK m. 34/1; İYUK m. 24/h). Karşı görüş notu müzakereye hazırlıkta kullanılabilir; karşı oyun yerine geçmez.
- Bağlayıcı kaynaklar gözden kaçırılmamalıdır: Yargıtay içtihadı birleştirme kararları (2797 s.K. m. 45), Danıştay içtihatları birleştirme kararları (2575 s.K. m. 40/4), direnme üzerine Hukuk ve Ceza Genel Kurulu kararları (HMK m. 373/7; CMK m. 307/4), ısrar üzerine İdari ve Vergi Dava Daireleri Kurulu kararları (İYUK m. 50/5), AYM kararları (AY m. 153/6). Ayrıntı: `ictihat-dogrulama-rehberi.md`.

## 2. Tarama sırası

1. **Önermeleri ayıkla.** Taslaktaki her hukuki önerme tek satıra yazılır: "X hâlinde Y sonucu doğar."
2. **Karşı önermeyi yaz.** "X hâlinde Y doğmaz, çünkü ..." Karşı önerme tarafların dilekçelerinden, bilirkişi raporuna itirazlardan ve varsa karşı oydan beslenir.
3. **Bağlayıcı kaynak.** `tr_ictihat_ara(chamber="IBK" | "HGK" | "CGK" | "IDDK" | "VDDK", query=...)`; AYM için `tr_aym_ara(kind="norm" | "bireysel", query=...)`.
4. **Daire içtihadı.** Aynı dairenin veya diğer dairelerin farklı yönde kararları. Hukuk ve Ceza Genel Kurullarının daireler arasındaki içtihat uyuşmazlıklarına ilişkin görevi 2797 s.K. m. 15'te, Büyük Genel Kurulunki m. 16'dadır; farklılık bulunursa not edilir.
5. **Bölge adliye mahkemeleri.** Kesin nitelikteki BAM kararları arasında uyuşmazlık varsa başkanlar kurulunun Yargıtaydan karar isteme yolu (5235 s.K. m. 35) not edilir.
6. **Anlamsal tarama.** `tr_ictihat_semantik_ara(query="<karşı önerme tek cümle>", initial_keyword="<2-3 terim>", courts=[...], max_docs=5)`. Sıralama yalnız anahtar kelimeyle çekilen adaylar üzerindedir; keşif aracı değildir (`yargi-mcp-rehberi.md`).
7. **Doktrin (ikincil).** `scholar_search_legal_scholarship` ile; Türk doktrini kapsamı sınırlı olabilir. Sonuç yoksa "doktrin taraması sonuç vermedi" yazılır; yazar, eser veya sayfa numarası asla hafızadan yazılmaz.
8. **Doğrulama.** Bulunan her karar `ictihat-dogrulama-rehberi.md` adımlarıyla açılır ve künye ile içerik eşleştirilir. Doğrulanamayan karar yalnız İnceleyen notunda `UYARI` satırıyla yer alır.

## 3. Ağırlıklandırma

| Bulgu | Etki | Taslakta ne yapılır |
|---|---|---|
| 🔴 Bağlayıcı karşı kaynak (İBK, AYM kararı, dosyadaki direnme üzerine genel kurul kararı) | taslağın sonucunu doğrudan etkileyebilir | hâkime bildirilir; taslak revize edilir veya somut olayın neden farklı olduğu gerekçelendirilir |
| 🟠 Yargıtay veya Danıştay daire kararları farklı yönde | ikna edici; tercih gerekçesi ister | gerekçede tartışılır; hangi görüşün neden tercih edildiği yazılır |
| 🟡 BAM kararları farklı yönde | bilgi; kesin kararlarda uyuşmazlık ihtimali | not edilir; gerekirse 5235 s.K. m. 35 yolu hatırlatılır |
| 🟢 Doktrin görüşü | bilgi | gerekirse gerekçede anılır; künyesi doğrulanmış olmalı |

## 4. Ayırt etme şablonu (hâkim doldurur)

```
Karşı karar: [künye — doğrulandı / UYARI]
Karşı kararın olay unsurları: [..]
Bu dosyada farklı olan unsur: [..]
Fark sonucu neden değiştirir: [..]
Sonuç: ayırt edildi / uygulanmalı / hâkim değerlendirmesi bekleniyor
```

## 5. Çıktı şablonu

```
MAHKEME DAHİLİ ÇALIŞMA NOTU — KARŞI GÖRÜŞ TARAMASI — TASLAK (hâkim/heyet onayı şart)
Önerme 1: [..]
  Karşı önerme: [..]
  🔴 Bağlayıcı: [künye, doğrulama durumu]
  🟠 Daire içtihadı: [..]
  🟡 BAM: [..]
  🟢 Doktrin: [..]
  Hâkime soru: [..]
Taranan: [araç — sorgu — courts/chamber — tarih aralığı]
Not: sonuç bulunmaması karşı görüşün olmadığı anlamına gelmez (Bedesten kapsamı kısmidir).
```

## 6. Sınırlar

- Asistan taraflardan biri adına yeni iddia, olgu veya delil üretmez; yalnız dosyada ileri sürülmüş iddiaları ve kaynaklardaki karşı görüşleri düzenler.
- Hangi görüşün doğru olduğunu söylemez; "hâkime soru" biçiminde bırakır.
- Kişi adı içeren karar başlıklarını aktarmaz; künye esas ve karar numarasıyla, AYM bireysel kararları başvuru numarası ve tarihle verilir.

---
*Madde kontrolü (27.09.2026, ArthurLegal MCP): HMK m. 27, 298, 373; CMK m. 34, 307; İYUK m. 24, 50; 2797 s.K. m. 15, 16, 45; 2575 s.K. m. 40; 5235 s.K. m. 35; AY m. 153. AYM B. No: 2015/439 kararı `tr_aym_getir` ile okundu.*
