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

## Yarg MCP — benzer özelge tarama

Vergi uyuşmazlığında, idarenin dayandığı veya tarafların ileri sürdüğü özelgeleri taramak için:

```
mcp__claude_ai_Yarg_MCP__search_gib_ozelge(
  arananKelime="<konu anahtar kelimeleri>"
)
```

GİB özelge veri tabanı 18.000+ özelge içerir; benzer konuda görüş bulunabilir.

## Özelgenin yargıdaki değeri (hâkim için)

- **İdareyi bağlar, mahkemeyi bağlamaz:** Özelge, idarenin mükellefe verdiği görüştür (VUK m. 413); hâkim hukuku serbestçe uygular, özelgeyle bağlı değildir.
- **İyiniyet / ceza koruması:** Özelgeye uygun davranan mükellef yönünden ceza ve gecikme faizi koruması (VUK m. 369) — ceza/iyiniyet değerlendirmesinde gözetilir.
- **Tutarlılık denetimi:** İdarenin aynı konudaki çelişkili özelgeleri, işlemin sebep/hukuka uygunluk denetiminde tartışılabilir.
- **İzaha davet / pişmanlık** (VUK m. 370, 371) ile ilişkisi ayrıca değerlendirilir.

## Mevzuat MCP

```
search_mevzuat(mevzuat_no="213", mevzuat_tur="KANUN")  # VUK m. 369
```

## Bağlantılı

- [VUK rehberi](vuk-rehberi.md)
- [Yarg MCP rehberi](yargi-mcp-rehberi.md) — GİB araç detayı
