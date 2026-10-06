# GİB Özelgesi (İzahat) Rehberi

> Vergi davasında idarenin dayandığı veya tarafın ileri sürdüğü özelge ve sirkülerlerin nasıl okunacağına dair mahkeme rehberi. Bu dosya karar vermez; ilgili maddeyi `tr_mevzuat_madde_getir(number="213", madde_no="413")` ile güncel metninden çekin.

## Yasal çerçeve

- **VUK m. 413 — Mükelleflerin izahat talebi:** mükellefler, vergi durumları ve vergi uygulaması bakımından müphem ve tereddütlü gördükleri hususlarda Gelir İdaresi Başkanlığından veya yetkili kıldığı makamlardan yazıyla izahat isteyebilir. Başkanlık izahatı **özelge** ile cevaplandırabilir veya aynı durumdaki tüm mükellefler için **sirküler** yayımlayabilir. Sirküler ve özelgeler Başkanlık bünyesindeki komisyonca oluşturulur; komisyon özelgesiyle tamamen aynı mahiyetteki hususlarda taşra teşkilatı da özelge verebilir. Özelgeler vergi mahremiyeti gözetilerek internette yayımlanır. Uygulama usulü Bakanlıkça çıkarılan yönetmelikle belirlenir.
- **VUK m. 369 — Yanılma ve görüş değişikliği:** yetkili makamların mükellefe yazıyla yanlış izahat vermesi veya bir hükmün uygulanma tarzına ilişkin içtihadın değişmesi hâlinde vergi cezası kesilmez ve gecikme faizi hesaplanmaz. Genel tebliğ veya sirkülerle yapılan görüş değişikliği yayımlandığı tarihten itibaren geçerlidir, geriye yürümez; yargı mercilerince iptal edilen genel tebliğ ve sirküler için bu kural uygulanmaz.
- Önceki sürümdeki "VUK m. 369 — Mukteza talep hakkı" ifadesi yanlıştı: izahat talebi m. 413'tedir.

## Özelgenin yargıdaki değeri (hâkim için)

- **Mahkemeyi bağlamaz:** özelge, idarenin talep eden mükellefin durumuna ilişkin görüşüdür. Hâkim Anayasaya, kanuna ve hukuka uygun olarak vicdani kanaatine göre hüküm verir (AY m. 138/1); özelgedeki yorum kanuna aykırıysa uygulanmaz.
- **Ceza ve gecikme faizi yönünden:** mükellefin idareden aldığı yazılı izahat yanlış çıkmışsa vergi cezası kesilmez ve gecikme faizi hesaplanmaz (VUK m. 369/1). Bu değerlendirmede dosyadaki özelge metni ile mükellefin başvuru yazısında anlattığı olay karşılaştırılır: özelge, başvuruda anlatılan olaya göre verilmiştir.
- **Görüş değişikliğinin zamanı:** idarenin genel tebliğ veya sirkülerle değiştirdiği görüş, yayım tarihinden önceki dönemlere uygulanamaz (VUK m. 369/2).
- **İzaha davet ve pişmanlık:** özelge konusu, izaha davet (VUK m. 370) veya pişmanlık ve ıslah (VUK m. 371) süreçleriyle birlikte ileri sürülmüşse bu maddelerin şartları ayrıca incelenir (bkz. `vuk-rehberi.md` bölüm 7).
- **Dava konusu edilebilirlik:** özelgenin tek başına iptal davasına konu olup olmayacağı ve görevli mahkeme kanunda açıkça düzenlenmemiştir; güncel Danıştay içtihadı `tr_ictihat_ara` ile çekilmeden bu konuda görüş yazılmaz. Dava açma süresi özel kanunda ayrı süre yoksa Danıştayda ve idare mahkemelerinde altmış, vergi mahkemelerinde otuz gündür (İYUK m. 7/1).

## ArthurLegal MCP (`tr_`) ile çekme

Dosyada idarenin dayandığı veya tarafın ileri sürdüğü özelgeyi ve benzer özelgeleri görmek için:

```
tr_kurum_karari_ara(kurum="gib", query="<konu anahtar kelimeleri>")
tr_kurum_karari_getir(kurum="gib", id="<ozelge_no>")
tr_mevzuat_madde_getir(number="213", madde_no=["369", "413"])
```

Çekilemeyen özelge için: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.gib.gov.tr/`

## Bağlantılı

- [VUK rehberi](vuk-rehberi.md)
- [Vergi yargısı rehberi](vergi-yargisi-rehberi.md)
- [ArthurLegal MCP TR rehberi](yargi-mcp-rehberi.md) — GİB araç ayrıntısı

---

*Madde kontrolü (27.09.2026, ArthurLegal MCP): VUK m. 369, 370, 371, 413; İYUK m. 7; AY m. 138. Önceki sürümdeki "VUK m. 369 — Mukteza talep hakkı", doğrulanmamış tebliğ numarası, ortalama cevap süresi ve "Danıştay vergi dairesinde dava, 30 gün" ifadeleri metinle örtüşmediği veya doğrulanamadığı için kaldırıldı.*
