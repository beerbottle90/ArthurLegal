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

## En sık kullanılan maddeler (litigation-legal pratiği)

### Yetki ve görev
- **m. 1-2:** Görev (özel görev olmadığı sürece Asliye Hukuk)
- **m. 6:** Genel yetki — davalı yerleşim yeri
- **m. 14:** Tüzel kişiler — şirket merkezi ([Müvekkil] Türkiye için İstanbul)
- **m. 17:** Sözleşmesel yetki — yetki klozu öncelik
- **m. 19:** Tüketici lehine kesin yetki
- **m. 116/c:** Tahkim itirazı — geçerli tahkim klozunda mahkemeden derhal sunulmalı

### Dava açma ve cevap
- **m. 119:** Dava dilekçesi şekli
- **m. 127:** Cevap süresi (kural: 2 hafta)
- **m. 129:** Karşı dava
- **m. 131-133:** İslah (cevap dilekçesini değiştirme) — sınırlı koşullarda

### Deliller (en kritik bölüm — litigation için)
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

## büro pratiği için kritik

### Yetki klozu sözleşmelerinde
[Müvekkil] sözleşmelerinde genelde:
- Ticari sözleşmeler: **İstanbul Anadolu/Çağlayan ATM**
- Tahkim: **ISTAC İstanbul** (TL anlaşmazlık) veya **ICC Paris** (uluslararası)

### Aliağa ÖEB tesisleri için
İşyeri mahkemesi (iş davaları): **Aliağa İş Mahkemesi**. Bedensel zarar tazminat davası ayrıca **Asliye Hukuk** (Karşıyaka veya Bergama).

### Petkim halka açık özel
Yatırımcı davaları **İstanbul ATM** (Anadolu) — ortaklık merkezi. SPK uyuşmazlıkları **Danıştay 13. Daire**.

### Tahkim seçimi
TANAP işlemlerinde uluslararası tahkim (LCIA, ICC Cenevre). Intra-group [Ana ortak / ilişkili taraf] işlemleri tahkim seçenek (Türkiye-Azerbaycan ikili anlaşmalar).

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

- [UYAP rehberi](uyap-rehberi.md) — UYAP avukat portal ve belge çekme
- [İSG dava rehberi](isg-dava-rehberi.md) — Aliağa İSG kazalarında HMK + 6331 entegre
- [ISTAC rehberi](istac-rehberi.md) — Tahkim klozu yönetimi
- [Mevzuat MCP rehberi](mevzuat-mcp-rehberi.md) — Madde çekme pattern'ları
- [Yarg MCP rehberi](yargi-mcp-rehberi.md) — İçtihat çekme pattern'ları
