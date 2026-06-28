# HMK (6100 sayılı Hukuk Muhakemeleri Kanunu) – Pratik Rehber

> Türk medeni yargı usulünün temel kaynağı. Litigation skill'leri madde atıfları için bu rehbere bakar.

## Yapı

- **Birinci Kısım:** Genel hükümler (m. 1-93)
- **İkinci Kısım:** Davalar (m. 94-217)
- **Üçüncü Kısım:** Deliller (m. 218-294)
- **Dördüncü Kısım:** Karar ve kanun yolları (m. 295-381)
- **Beşinci Kısım:** Geçici hukuki koruma ve özel yargılama usulleri (m. 382-411)
- **Altıncı Kısım:** Tahkim (m. 412-444)
- **Yedinci Kısım:** Yargılama gideri (m. 445-454)

## En sık kullanılan maddeler (yargısal pratik)

### Yetki ve görev
- **m. 1-2:** Görev (özel görev olmadığı sürece Asliye Hukuk)
- **m. 6:** Genel yetki — davalı yerleşim yeri
- **m. 14:** Tüzel kişiler — tüzel kişinin merkezinin bulunduğu yer
- **m. 17:** Sözleşmesel yetki — yetki klozu öncelik
- **m. 19:** Tüketici lehine kesin yetki
- **m. 116/c:** Tahkim itirazı — geçerli tahkim klozunda mahkemeden derhal sunulmalı

### Dava açma ve cevap
- **m. 119:** Dava dilekçesi şekli
- **m. 127:** Cevap süresi (kural: 2 hafta)
- **m. 129:** Karşı dava
- **m. 131-133:** İslah (cevap dilekçesini değiştirme) — sınırlı koşullarda

### Deliller (en kritik bölüm — yargılamada)
- **m. 187:** İspat yükü (genel kural: iddia eden ispat)
- **m. 199:** Senet (yazılı delil)
- **m. 219:** Belgenin ibraz mecburiyeti
- **m. 220:** Hasım tarafın elindeki delil — istek + aleyhe karine
- **m. 240-265:** Tanık
- **m. 266-287:** Bilirkişi
- **m. 288-292:** Keşif
- **m. 293:** Uzman görüşü (yeni; bilirkişiden ayrı)

### Karar ve kanun yolları
- **m. 297:** Hüküm gerekçesi
- **m. 341-360:** İstinaf (BAM)
- **m. 361-381:** Temyiz (Yargıtay)
- **m. 400:** Delil tespit davası

### Tahkim (m. 412 vd.)
- **m. 416:** Tahkim klozu/sözleşmesi geçerliliği
- **m. 433:** Tahkim kararının ifa edilebilirliği
- **m. 439:** Tahkim kararının iptali

## Yargısal pratikte kritik kontrol noktaları

### Görev ve yetki denetimi (ön inceleme)
- **Görev** kamu düzenindendir, re'sen gözetilir (HMK m. 1, 114/1-c).
- **Yetki:** kural davalı yerleşim yeri (m. 6); tüzel kişide merkez (m. 14); sözleşmesel yetki klozu (m. 17); tüketici lehine kesin yetki (m. 19).

### Tahkim itirazı (m. 116/1-c)
- Geçerli tahkim klozu varsa, davalının tahkim itirazı **ilk itiraz** olarak **cevap dilekçesinde** ileri sürülmelidir; süresinde ileri sürülmezse itiraz düşer ve mahkeme yargılamaya devam eder.
- Tahkim klozunun geçerliliği (m. 412 vd.) ve kapsamı ayrı denetlenir.

### Özel görevli mahkeme ayrımı
- Asliye Ticaret (TTK m. 4-5), İş Mahkemesi (7036), Tüketici, Aile, Kadastro, FSH gibi özel görevli mahkemeler — görev itirazı re'sen incelenir.
- TTK m. 5/A dava şartı arabuluculuk (ticari + alacak/tazminat) — görev/dava şartı kontrolünde gözetilir.

## Mevzuat MCP ile çekme

```
mcp__claude_ai_Mevzuat_MCP__search_mevzuat(mevzuat_no="6100", mevzuat_tur="KANUN")
→ mevzuatId not
mcp__claude_ai_Mevzuat_MCP__get_mevzuat_madde_tree(mevzuatId=<id>)
→ Madde ağacı, ilgili maddeye gir
mcp__claude_ai_Mevzuat_MCP__search_within_mevzuat(mevzuatId=<id>, phrase="<madde no veya konu>")
```

Atıf: `[Mevzuat MCP — HMK m. XXX — GG.AA.YYYY]`

## Yargıtay yorumu için

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="HMK <madde no> <konu>",
  daire="Hukuk Genel Kurulu",  # En bağlayıcı
  baslangicTarihi="2022-01-01"
)
```

HGK kararları **birleştirici** niteliktedir — alt mahkemeler için bağlayıcı.

## Tipik hatalar (önlem)

- ❌ Cevap süresi **2 hafta** (kural), bazı özel hallerde değişik. Her zaman tebliğ tarihinden hesapla.
- ❌ **Tahkim klozu varken mahkemede dava açmak** — m. 116/c kapsamında geçerli tahkim klozunda mahkemenin görevsizliği vardır; davalının itiraz hakkı **ilk cevap dilekçesinde** kullanılmazsa düşer.
- ❌ **Yazılı delili tanıkla ispat etmek** — m. 200 (senetle ispat zorunluluğu eşiği)
- ❌ **İstinaf süresi kaçırma** — m. 345 — 2 hafta tebliğden
- ❌ **Yedek istem unutmak** — dava dilekçesinde yedek istem yoksa, sonradan ekleme zor (m. 131)

## Bağlantılı referanslar

- [UYAP rehberi](uyap-rehberi.md) — mahkeme tarafı UYAP iş akışı
- [Gerekçe yazım rehberi](gerekce-yazim-rehberi.md) — HMK m. 297 gerekçe tekniği
- [Bilirkişilik rehberi](bilirkisilik-rehberi.md) — m. 266-287 + m. 293
- [Mevzuat MCP rehberi](mevzuat-mcp-rehberi.md) — madde çekme pattern'ları
- [Yarg MCP rehberi](yargi-mcp-rehberi.md) — İçtihat çekme pattern'ları
