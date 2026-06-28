> **Durum:** ✅ Açık — TR Legal MCP `search_rekabet_kurumu_decisions` + mevzuat araçları; rekabet.gov.tr WebFetch. Bu rehber 4054 sayılı Kanun'un esas/usul çatısını ve sektörel/örnek senaryoları derler. Bağlantılı skill'ler: `administrative-legal:rekabet-kurulu-itiraz`, `corporate-legal:merger-notification`, `energy-finance:ma-diligence-energy`.

# Rekabet Hukuku — Pratik Rehber (4054 sayılı Kanun)

## 1. Çerçeve

- **4054 sayılı Rekabetin Korunması Hakkında Kanun** — uygulayıcı: **Rekabet Kurumu** (karar organı: **Rekabet Kurulu**, Ankara).
- **Üç yasak / kontrol alanı:**
  - **m. 4 — Rekabeti sınırlayan anlaşma / uyumlu eylem / teşebbüs birliği kararı** (kartel: fiyat tespiti, pazar/müşteri paylaşımı, arz kısıtlama, **bilgi paylaşımı**, ihale danışıklığı). Yatay + dikey.
  - **m. 6 — Hakim durumun kötüye kullanılması** (dışlayıcı/sömürücü: fiyat sıkıştırma, ayrımcılık, münhasırlık, fahiş fiyat, mal vermeyi reddetme).
  - **m. 7 — Birleşme ve devralmalar (merger control)** — eşik aşılırsa **ön izin** (suspensory — kapanış öncesi onay şart).
- **Muafiyet (m. 5):** m.4 kapsamına giren anlaşma, dört şartı (verimlilik + tüketici payı + zorunluluk + rekabeti tümden kaldırmama) sağlıyorsa muaf. **Grup muafiyeti tebliğleri** (dikey anlaşmalar 2002/2, Ar-Ge, uzmanlaşma, teknoloji transferi) — self-assessment.
- **Menfi tespit / bireysel muafiyet** başvurusu Kurul'a yapılabilir.

## 2. Birleşme-devralma kontrolü (m. 7 + Tebliğ 2010/4)

**Bildirim eşikleri (2022 güncellemesi — TL):**
- İşlem taraflarının **Türkiye ciroları toplamı > 750 mln TL** **VE** en az iki tarafın her birinin Türkiye cirosu **> 250 mln TL**; **VEYA**
- Devralınan varlık/faaliyetin (devralmada) veya taraflardan birinin (birleşmede) Türkiye cirosu **> 250 mln TL** **VE** diğer tarafın **dünya cirosu > 3 milyar TL**.
- **Teknoloji teşebbüsü** istisnası: hedef bir "teknoloji teşebbüsü" ise 250 mln TL eşikleri aranmaz (dünya/Türkiye faaliyeti yeterli).

**Süreç:** Bildirim → **30 iş günü** ön inceleme (Faz I) → şartsız izin / nihai inceleme (Faz II ~6 ay). **Kapanış öncesi izin zorunlu** (gun-jumping = ciro %'si ceza + işlem geçersizliği). Bildirimsiz tamamlama: ayrı idari para cezası.

> **Örnek senaryo:** Bir RES/HES/jeotermal **santral devralma** veya **pay/lisans devri** eşiği aşıyorsa Rekabet Kurumu bildirimi + EPDK pay devri onayı **paralel** yürür (ikisi de kapanış ön şartı). `corporate-legal:merger-notification` ile eşik testi yap.

## 3. Soruşturma usulü ve ceza

- **Önaraştırma → Soruşturma açılması → yazılı savunma (3 yazılı savunma turu) → sözlü savunma → Kurul kararı.**
- **İdari para cezası:** ihlal yılı **cironun %10'una kadar** (yıllık gayrisafi gelir); yöneticilere ayrıca %5'e kadar. **Süreli/günlük** ceza (bilgi vermeme).
- **Pişmanlık (leniency):** kartelde ilk başvurana **tam bağışıklık**, sonrakilere indirim (Pişmanlık Yönetmeliği).
- **Uzlaşma (settlement):** soruşturmada ihlali kabul → **%25'e kadar indirim** + hızlı kapanış (Uzlaşma Yönetmeliği, 2021).
- **De minimis:** ciro/pazar payı eşiği altındaki (kartel hariç) ihlallerde soruşturma açmama takdiri (2021).

## 4. Dava (Kurul kararına itiraz)

- Rekabet Kurulu kararı = **idari işlem** → **iptal davası**: ilk derece **Ankara İdare Mahkemesi → BİM → Danıştay 13. Daire** (temyiz). Süre **İYUK m.7 = 60 gün**.
- Yürütmeyi durdurma (İYUK m.27): ceza tahsili/yapısal tedbir telafisi güç zarar. Detay: `administrative-legal:rekabet-kurulu-itiraz` + `advocacy-legal:kamu-hukuku-dilekce`.

## 5. Enerji sektörüne özgü yakıcı alanlar

- **Toptan elektrik satışı (organize toptan piyasalar):** Elektrik piyasalarında **fiyat/teklif davranışı**, kapasite saklama (capacity withholding), **rakiplerle bilgi paylaşımı** — m.4/m.6 riski.
- **Dernek/platform:** Sektörel dernek/platform toplantılarında **rekabete duyarlı bilgi** (fiyat, kapasite, strateji) paylaşımı = teşebbüs birliği kararı/uyumlu eylem riski. Toplantı protokolü + hukuk filtresi.
- **Devralmalar:** RES/HES portföy büyütme → merger bildirimi.
- **Dikey anlaşmalar:** uzun vadeli PPA/tedarik münhasırlığı → grup muafiyeti (2002/2) self-assessment.
- **Hakim durum:** bölgesel/ürün pazarında pay yüksekse m.6 hassasiyeti.

## 6. Kaynak erişimi (TR Legal MCP)

```
# Rekabet Kurulu kararı arama (kartel, hakim durum, birleşme emsali)
mcp__...__search_rekabet_kurumu_decisions(PdfText="<konu — örn. elektrik toptan bilgi paylaşımı>")
# 4054 ve tebliğ metinleri
mcp__...__search_mevzuat(mevzuat_no="4054")   # + Tebliğ 2010/4, 2002/2
```
Atıf: `[Rekabet Kurulu — karar no/tarih — GG.AA.YYYY]` (MCP'den çekildiyse `[Yargı MCP — rekabet — ...]`); mevzuat → `[Mevzuat MCP — GG.AA.YYYY]`. Çekmediğin karara atıf yapma.

## Tipik hatalar
- Birleşme eşiğini güncel olmayan rakamla hesaplamak (2022 TL eşikleri); **teknoloji teşebbüsü istisnasını** atlamak.
- Gun-jumping: bildirimden/izinden önce kontrolü fiilen devralmak.
- Dernek toplantısında bilgi paylaşımını "sektör sohbeti" sanmak — uyumlu eylem karinesi.
- Kurul kararına itirazda süreyi (60 gün) ve görevli mahkemeyi (Ankara İdare Mah., Danıştay 13. D temyiz) karıştırmak.

## Bağlantılı referanslar
`idari-yargi-yapisi-rehberi.md` · `iyuk-rehberi.md` · `kanun-kisaltmalar.md` · `yargi-mcp-rehberi.md` · `mevzuat-mcp-rehberi.md`

*Son güncelleme: 25.06.2026 — Enerji sektörü (üretim + toptan satış + M&A) rekabet bağlamı; 2022 birleşme ciro eşikleri ve uzlaşma/de minimis (2021) dâhil. Güncel eşik/oranları Mevzuat MCP'den teyit edin.*
