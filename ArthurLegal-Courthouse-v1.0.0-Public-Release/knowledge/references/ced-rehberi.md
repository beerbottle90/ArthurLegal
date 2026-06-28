# ÇED (Çevresel Etki Değerlendirmesi) Rehberi

> 2872 sayılı Çevre Kanunu + ÇED Yönetmeliği. İdari yargıda ÇED kararlarının (olumlu/olumsuz/gerekli değil) iptal davalarında başvurulur; İYUK m. 20/A ivedi yargılama rejimiyle bağlantılıdır.

## Hukuki çerçeve

- **2872 sayılı Çevre Kanunu** — m. 10 ÇED zorunluluğu, m. 20-22 idari para cezaları
- **ÇED Yönetmeliği** (yıllık güncellenir, Çevre Bakanlığı tebliği)
- **ÇED Genel Müdürlüğü** — Çevre, Şehircilik ve İklim Değişikliği Bakanlığı

## ÇED süreci tipleri

| Tip | Kapsam | Örnek |
|---|---|---|
| **ÇED gereklilik var/yok** | Ön inceleme | Yeni proje başlangıç |
| **ÇED olumlu/olumsuz** | Tam ÇED süreci | Kapasite artırımı, yeni üretim hattı |
| **Proje tanıtım dosyası (PTD)** | Küçük etkili proje | Tank, ek depo |
| **ÇED muafiyeti** | Listede yok ise | — |
| **Kümülatif etki değerlendirmesi** | Birden fazla proje birlikte | Endüstri bölgesi içi yeni yatırımlar |

## Süreç akışı

```
Başvuru (proje sahibi) →
ÇED kapsamlama (scoping) — komisyon →
ÇED raporu (proje sahibi tarafından bağımsız uzman ile hazırlanır) →
Halk katılımı (toplantı) →
Komisyon inceleme + bakanlık değerlendirme →
ÇED Olumlu / ÇED Olumsuz / Koşullu Olumlu →
  [Olumsuz → İYUK 30 gün → İdare Mah. iptal davası]
```

## Büyük endüstriyel tesis davalarında özellik arz eden noktalar

### Sık dava konusu işlem tipleri
- Kapasite artırımı / yeni ünite ÇED kararları
- Yeni üretim hattı (petrokimya, rafineri vb.) ÇED'i
- Terminal/depolama tesisi genişleme ÇED'i
- Endüstri bölgesi ortak altyapı ÇED'i

### Yargısal denetimde sık tartışılan unsurlar
- **Kümülatif etki** — tek tek projeler değerlendirilirken toplam etkinin gözetilip gözetilmediği
- **Halk katılımı toplantısı** usulüne uygunluk
- **Komisyon değerlendirmesinin** denetlenebilirliği (gerekçe + bilimsel dayanak)
- **Re'sen araştırma (İYUK m. 20)** kapsamında bilirkişi/keşif ihtiyacı

## ÇED ret kararına dava — ⚠️ ÖZEL REJİM: İYUK m. 20/A İVEDİ YARGILAMA USULÜ

**ÇED kararları (idari yaptırım/para cezası HARİÇ) İYUK m. 20/A kapsamındadır:**

| Kalem | ÇED ret kararı (m. 20/A) | Çevre idari para cezası (genel rejim) |
|---|---|---|
| **Dava açma süresi** | **30 gün** (hak düşürücü) | **60 gün** |
| İYUK m. 11 üst makama başvuru | **UYGULANMAZ** (süre durmaz) | Uygulanır |
| İstinaf (BİM) | **YOK — atlanır** | Var (30 gün) |
| Temyiz | **Doğrudan Danıştay (15 gün)** | Danıştay (BİM kararına 30 gün) |
| Temyiz dairesi | Danıştay **14. Daire** (ÇED) veya **10. Daire** veya **6. Daire** (imar/çevre işbölümüne göre) | Danıştay 10. Daire |
| Yürütmenin durdurulması | Talep edilebilir | Talep edilebilir |

⚠️ **KRİTİK BUG TARİHÇESİ:** v1.3.0'da bu rehberde ÇED için "60 gün + BİM + Danıştay" yazılıydı — **yanlış**. v1.3.1 patch ile düzeltildi. Mevzuat MCP'den teyit edilen doğru rejim: m. 20/A → 30 gün, BİM yok, 15 gün temyiz.

**Büro pratiği:**
- **ÇED ret kararı geldiyse derhal 30 gün takvim başlatılır** — kaçırılırsa hak düşer, m. 11 başvurusu süreyi DURDURMAZ
- Doğrudan Ankara İdare Mahkemesi (Bakanlık merkez) veya il İdare Mahkemesi (il müdürlüğü)
- Yürütmenin durdurulması talebi (telafisi güç zarar = yatırım blokesi)
- Kararla aleyhe karara karşı 15 gün içinde **doğrudan Danıştay'a** temyiz

**Mevzuat MCP doğrulama:**
```
mcp__claude_ai_Mevzuat_MCP__search_within_mevzuat(mevzuat_id="103161", keyword="20/A")
```

## Hukuki argümanlar (klasik)

- **Komisyon uzmanlığı yetersiz** — komisyon üyelerinin niteliği
- **Bağımsız uzman raporu göz ardı edildi** — bizim hazırlattığımız rapor
- **BAT (Best Available Techniques) uyumu** — AB direktif paraleli
- **Sektör emsali yatırımların ÇED onayı** — neden bizim red?
- **Bakanlık prosedürü ihlali** — halk katılımı, komisyon toplantı

## Paralel idari ceza

Çevre Bakanlığı **idari para cezası** (2872 m. 20-22) ayrı süreçtir:
- Çevre denetiminden çıkar (planlı veya şikayet üzerine)
- Ceza kararı tebliğden 30 gün → İdare Mah. dava (`idari-para-cezasi-itiraz`)
- ÇED ret + idari ceza birlikte → koordine savunma

## Yarg MCP

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="14. Daire",
  arananKelime="ÇED ret iptal",
  baslangicTarihi="2022-01-01"
)

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="10. Daire",
  arananKelime="çevre cezası 2872",
  baslangicTarihi="2022-01-01"
)
```

## Mevzuat MCP

```
search_mevzuat(mevzuat_no="2872", mevzuat_tur="KANUN")  # Çevre K.
search_mevzuat(mevzuat_adi="ÇED", mevzuat_tur="YONETMELIK")  # ÇED Yön.
```

## Bağlantılı

- [İYUK rehberi](iyuk-rehberi.md) — dava usulü
- [Yürütmenin durdurulması rehberi](yurutmenin-durdurulmasi-rehberi.md) — m. 27 / m. 20/A ivedi rejim
- [İdari yargı yapısı rehberi](idari-yargi-yapisi-rehberi.md) — Danıştay 14./10. Daire
