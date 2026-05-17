# GİB Özelge (Mukteza) Rehberi

> Belirsiz bir vergi konusunda GİB'den bağlayıcı görüş alma. Türk vergi pratiğinin önemli aracı.

## Yasal çerçeve

- **VUK m. 369** — Mukteza talep hakkı
- **395 Sıra No.lu VUK Genel Tebliği** — Özelge format ve usulleri
- **Özelge "mükellef kişiye özel" bağlayıcıdır** — başka mükellef bunu doğrudan kullanamaz ama emsal referans olabilir

## Özelge'nin avantajları

- Bağlayıcı GİB görüşü (sadece talep eden için)
- Sonraki Maliye incelemesinde **kalkan**
- Belirsiz konuda risk azaltma

## Dezavantajları / riskler

- **Süre:** 6-9 ay ortalama
- **Olumsuz cevap → pozisyonu zayıflatır** (sonraki incelemede Maliye bu kararı kullanır)
- **Konunun açığa çıkması** — Maliye'nin dikkatini çekebilir
- Olumsuz özelgeye **idari itiraz yolu yok**, sadece dava

## Özelge talep süreci

1. **Yetkili otorite:**
   - Büyük şirket → İstanbul/Ankara Vergi Dairesi Başkanlığı veya GİB Genel Müdürlüğü
   - Genelde belirsizliğin önemine göre

2. **Dilekçe formatı (Tebliğ 395):**
   - Mükellef bilgileri (VKN, ünvan, adres)
   - Konu (kısa)
   - Fiili durum (ayrıntılı)
   - Hukuki değerlendirme
   - Talep
   - Ekler (sözleşme örneği, benzer özelge, vs.)

3. **Cevap süresi:** Genelde 6-9 ay; bazen 1 yıl+

4. **Olumsuz cevap → Danıştay dava:**
   - İlgili Danıştay vergi dairesinde
   - İYUK m. 7 — 30 gün (özelge tebliğden)

## Yargı MCP — benzer özelge tarama

**Özelge talep etmeden ÖNCE** mutlaka mevcut özelgelerde aynı/benzer konu var mı bak:

```
mcp__claude_ai_Yargi_MCP__search_gib_decisions(
  arananKelime="<konu anahtar kelimeleri>"
)
```

GİB özelge veri tabanı 18.000+ özelge — büyük ihtimal benzer konu var. Eğer:
- **Bizim lehimize karar** varsa: Özelge talep etmeye gerek yok; mevcut özelgeyi referans olarak kullan.
- **Aleyhe karar** varsa: Özelge talep etme; pozisyon zayıflar.
- **Belirsiz / yok** ise: Özelge talep mantıklı (risk değerlendirmesiyle).

## şirket-özel kontroller

- **[Halka Açık İştirak] ilgili büyük etki:** KAP açıklama gerekebilir (özelge cevabı önemli mali sonuç doğurur)
- **[Boru Hattı Projesi] işlem özelgesi:** Hükümetlerarası anlaşma + GİB ortak yorum
- **[Yurtdışı Ana Şirket] intra-group:** Özelge talep edersek Maliye dikkati çekiyor — risk
- **EPDK paralel:** Enerji vergisi konusunda EPDK görüşü de paralel etkili

## Mevzuat MCP

```
search_mevzuat(mevzuat_no="213", mevzuat_tur="KANUN")  # VUK m. 369
```

## Bağlantılı

- [VUK rehberi](vuk-rehberi.md)
- [Yargı MCP rehberi](yargi-mcp-rehberi.md) — GİB araç detayı
