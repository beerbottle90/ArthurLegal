# HMK (6100 sayılı Hukuk Muhakemeleri Kanunu) – Pratik Rehber

> Türk medeni yargı usulünün temel kaynağı. Litigation skill'leri madde atıfları için bu rehbere bakar.

## Yapı

- **Birinci Kısım:** Genel hükümler — görev, yetki, taraflar, süreler, adli tatil (m. 1-104)
- **İkinci Kısım:** Dava çeşitleri, dava şartları ve ilk itirazlar (m. 105-117); **Üçüncü Kısım:** Yazılı yargılama usulü (m. 118-186)
- **Dördüncü Kısım:** İspat ve deliller (m. 187-293)
- **Beşinci Kısım:** Hüküm ve davaya son veren taraf işlemleri (m. 294-315); **Altıncı Kısım:** Basit yargılama usulü (m. 316-322); **Sekizinci Kısım:** Kanun yolları (m. 341-381)
- **Dokuzuncu Kısım:** Çekişmesiz yargı (m. 382-388); **Onuncu Kısım:** Geçici hukuki korumalar — ihtiyati tedbir, delil tespiti (m. 389-406)
- **Onbirinci Kısım:** Tahkim (m. 407-444)
- **Yedinci Kısım:** Yargılama giderleri ve adli yardım (m. 323-340); **Onikinci Kısım:** Son hükümler — UYAP/elektronik işlemler (m. 445-452)

## En sık kullanılan maddeler (litigation-legal pratiği)

### Yetki ve görev
- **m. 1-2:** Görev (özel görev olmadığı sürece Asliye Hukuk)
- **m. 6:** Genel yetki — davalı yerleşim yeri
- **m. 6/1 + TMK m. 51:** Tüzel kişi davalıda genel yetki (m. 14: şube işlemlerinde şube yeri de yetkili; ortaklık/üyelik davalarında merkez kesin yetkili) — şirket merkezi ([Müvekkil] için İstanbul)
- **m. 17-18:** Yetki sözleşmesi — yalnız tacirler veya kamu tüzel kişileri arasında, yazılı; aksi kararlaştırılmadıkça dava yalnız seçilen mahkemede açılır
- **TKHK m. 73/5:** Tüketici davası tüketicinin yerleşim yerindeki tüketici mahkemesinde de açılabilir (seçimlik, kesin değil); **HMK m. 19:** yetki itirazının ileri sürülmesi
- **m. 116/1-b:** Tahkim itirazı (ilk itiraz) — cevap dilekçesinde ileri sürülmeli (m. 117/1); kabulünde dava usulden reddedilir (m. 413/1)

### Dava açma ve cevap
- **m. 119:** Dava dilekçesi şekli
- **m. 127:** Cevap süresi (kural: 2 hafta)
- **m. 132-133:** Karşı dava (cevap dilekçesiyle veya cevap süresi içinde ayrı dilekçeyle)
- **m. 176-182:** Islah (tarafın kendi usul işlemlerini kısmen/tamamen düzeltmesi; aynı davada bir kez, tahkikat sona erinceye kadar)

### Deliller (en kritik bölüm — litigation için)
- **m. 190:** İspat yükü (kural: iddia edilen vakıaya bağlanan hukuki sonuçtan lehine hak çıkaran taraf ispat eder); m. 187 = ispatın konusu
- **m. 199:** Belge (yazılı/basılı metin, senet, elektronik veri vb.); senetle ispat m. 200 vd.
- **m. 219:** Belgenin ibraz mecburiyeti
- **m. 220:** Hasım tarafın elindeki delil — istek + aleyhe karine
- **m. 240-265:** Tanık
- **m. 266-287:** Bilirkişi
- **m. 288-292:** Keşif
- **m. 293:** Uzman görüşü (yeni; bilirkişiden ayrı)

### Karar ve kanun yolları
- **m. 297:** Hüküm gerekçesi
- **m. 341-360:** İstinaf (BAM)
- **m. 361-373:** Temyiz (Yargıtay); **m. 374-381:** Yargılamanın iadesi
- **m. 400:** Delil tespit davası

### Tahkim (m. 412 vd.)
- **m. 412:** Tahkim sözleşmesinin tanımı ve şekli (yazılı şekil; asıl sözleşmeden bağımsızlık)
- **m. 439/4:** İptal davası, hakem kararının (veya tavzih, düzeltme ya da tamamlama kararının) taraflara bildiriminden itibaren bir ay içinde açılır; iptal davası icrayı durdurmaz, ancak hükmolunan değeri karşılayacak teminat gösterilirse icra durdurulabilir
- **m. 439:** Tahkim kararının iptali

## büro pratiği için kritik

### Yetki klozu sözleşmelerinde
[Müvekkil] sözleşmelerinde genelde:
- Ticari sözleşmeler: **İstanbul Anadolu/Çağlayan ATM**
- Tahkim: **ISTAC İstanbul** (TL anlaşmazlık) veya **ICC Paris** (uluslararası)

### [TESİS LOKASYONU] ÖEB tesisleri için
İşyeri mahkemesi (iş davaları): **[TESİS LOKASYONU] İş Mahkemesi**. Bedensel zarar tazminat davası ayrıca **Asliye Hukuk** (Karşıyaka veya Bergama).

### [HALKA AÇIK İŞTİRAK] halka açık özel
Yatırımcı davaları **İstanbul ATM** (Anadolu) — ortaklık merkezi. SPK uyuşmazlıkları **Danıştay 13. Daire**.

### Tahkim seçimi
[BORU HATTI PROJESİ] işlemlerinde uluslararası tahkim (LCIA, ICC Cenevre). Intra-group [Ana ortak / ilişkili taraf] işlemleri tahkim seçenek (ilgili ikili yatırım anlaşmaları).

## ArthurLegal MCP (`tr_`) ile çekme

```
tr_mevzuat_ara(number="6100", types=["KANUN"])
→ mevzuatId not
tr_mevzuat_icindekiler(mevzuat_id=<id>)
→ Madde ağacı, ilgili maddeye gir
tr_mevzuat_madde_getir(madde_id=<ağaçtaki madde_id>)   # şemada number ve madde_no varsa: tr_mevzuat_madde_getir(number="6100", madde_no="<no>")
tr_mevzuat_icinde_ara(mevzuat_id=<id>, query="<konu kelimeleri>")   # konu araması; madde numarasıyla madde bulmaz
```

Atıf: `[ArthurLegal TR — HMK m. XXX — GG.AA.YYYY]`

## Yargıtay yorumu için

```
tr_ictihat_ara(
  courts=["YARGITAYKARARI"],
  query="+HMK +<madde +no> +<konu>",
  chamber="HGK",  # En bağlayıcı
  date_from="2022-01-01"
)
```

HGK kararları kural olarak emsal niteliğindedir; HGK'nın direnme (m. 373/5) veya m. 373/6 üzerine verdiği karara o dosyada uyulması zorunludur (HMK m. 373/7). Genel bağlayıcılık **içtihadı birleştirme kararlarına** aittir (2797 s. Yargıtay K. m. 45).

## Tipik hatalar (önlem)

- ❌ Cevap süresi **2 hafta** (kural), bazı özel hallerde değişik. Her zaman tebliğ tarihinden hesapla.
- ❌ **Tahkim klozu varken mahkemede dava açmak** — m. 116/1-b uyarınca tahkim itirazı bir **ilk itirazdır** (görevsizlik değildir, re'sen gözetilmez); **cevap dilekçesinde** ileri sürülmezse dinlenemez (m. 117/1), kabulünde dava usulden reddedilir (m. 413/1).
- ❌ **Yazılı delili tanıkla ispat etmek** — m. 200 (senetle ispat zorunluluğu eşiği)
- ❌ **İstinaf süresi kaçırma** — m. 345 — 2 hafta tebliğden
- ❌ **Yedek istem unutmak** — dava dilekçesinde terditli (yedek) talep yoksa, cevaba cevap dilekçesinden sonra ancak karşı tarafın açık muvafakati veya ıslahla eklenebilir (m. 111 terditli dava; m. 141 iddianın genişletilmesi; m. 176-177 ıslah)

## Bağlantılı referanslar

- [UYAP rehberi](uyap-rehberi.md) — UYAP avukat portal ve belge çekme
- [İSG dava rehberi](isg-dava-rehberi.md) — [TESİS LOKASYONU] İSG kazalarında HMK + 6331 entegre
- [ISTAC rehberi](istac-rehberi.md) — Tahkim klozu yönetimi
- [ArthurLegal MCP TR mevzuat rehberi](mevzuat-mcp-rehberi.md) — Madde çekme pattern'ları
- [ArthurLegal MCP TR rehberi](yargi-mcp-rehberi.md) — İçtihat çekme pattern'ları
