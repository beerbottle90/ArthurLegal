---
name: case-intake
description: >
  Yeni dava dosyası / ihtarname / dava açma kararı geldiğinde ön-değerlendirme:
  yargı yeri & görevli mahkeme (HMK), husumet, zamanaşımı, TTK m. 5/A arabuluculuk
  ön-kontrol, ön delil envanteri, Yargı MCP emsal tarama, ilk strateji önerileri,
  şiddet ataması, eskalasyon önerisi.
user-invocable: true
---

# Case Intake — Dava Ön-Değerlendirme

## Matter context

Aktif matter yoksa: "Yeni matter mı? `/dispute-litigation:matter-workspace new <slug>` ile aç veya practice-level cevap." 

## Adımlar

### 1. Materyali oku ve özet çıkar

- Karşı tarafın iddiası (1 cümle)
- Talep (tutar, dava tipi — eda/tespit/inşai/men)
- Hukuki dayanak (madde no'lar)
- Süreler (cevap süresi HMK m. 127 — 2 hafta; ihtarname süresi)

### 2. Yargı yeri ve görevli mahkeme (HMK)

| Senaryo | Madde | Mahkeme |
|---|---|---|
| Genel yetki | m. 6 | Davalı yerleşim yeri |
| Şirketler | m. 14 | Şirket merkezi |
| Sözleşmesel yetki | m. 17 | Sözleşme klozu |
| Tüketici | m. 19 | Tüketici lehine kesin |
| İş davası | İş Mh. K. | İşyeri |
| Tahkim klozu | HMK 412 + ISTAC | Tahkim |

Görevli mahkeme: Asliye Hukuk / ATM (TTK m. 4) / İş Mh. / Sulh / Tüketici Hakem Heyeti

⚠️ Mevzuat MCP'den HMK çek, atıf et.

### 3. Husumet

- Aktif husumet (davacı sıfat)
- Pasif husumet (davalı = doğru tüzel kişi mi?)
- Tüzel kişilik perdesi riski

### 4. Zamanaşımı (KRİTİK)

| Dava tipi | Süre | Madde |
|---|---|---|
| Sözleşme | 10 yıl | TBK 146 |
| Haksız fiil | 2/10 yıl | TBK 72 |
| İş alacak | 5 yıl | İş K. 32 |
| Vergi davası | 30 g | İYUK 7 |
| İdari iptal | 60 g | İYUK 7 |
| Marka ihlali | 2/10 yıl | SMK 157 |

⚠️ Mevzuat MCP'den madde çek; müvekkilin söylediği zamanaşımı tarihini önce doğrula.

### 5. Ön delil envanteri

- Bizde olan belgeler
- Karşı taraf elindeki belgeler (HMK 220 delil isteme)
- Tanık (HMK 240) / bilirkişi (HMK 266) / keşif (HMK 288) ihtiyacı

### 6. Yargı MCP emsal tarama

```
mcp__claude_ai_Yargi_MCP__search_yargitay_decisions(
  arananKelime="<konu>", daire="<ilgili>", baslangicTarihi="2023-01-01"
)
```

Atıf: `[Yargı MCP — yargitay — GG.AA.YYYY]`

### 7. TTK m. 5/A Zorunlu Arabuluculuk

**Kapsam:** Ticari uyuşmazlık + alacak/tazminat. **Dava şartı.**

Kapsama giriyor mu?
- [ ] Uyuşmazlık ticari (TTK m. 4)
- [ ] Talep para alacağı (alacak veya tazminat)
- [ ] Kapsam DIŞI mı? (tüketici, iş davası, ihtiyati tedbir)

Giriyorsa: Adalet Bakanlığı arabuluculuk başvur, tutanak alınmadan dava reddi (HMK 114).

### 8. Şiddet ataması ve eskalasyon

🔴 / 🟠 / 🟡 / 🟢 — eskalasyon önerisi (atanan ortak / Yönetici Ortak / Ortaklar Kurulu)

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Dava Ön-Değerlendirme — [matter-slug / esas no]

## ⚠️ İnceleyen notu
- Kaynaklar: Yargı MCP [✓N / ✗]; Mevzuat MCP [✓X / ✗]
- Okuma kapsamı: [...]
- Şiddet: 🔴/🟠/🟡/🟢
- Güncellik: [tarih]

## Özet
Karşı taraf, iddia, talep, dayanak, süre

## Yargı yeri ve mahkeme
[mahkeme] — HMK m. [X] [Mevzuat MCP atıf]

## Husumet
Aktif/pasif değerlendirme [review]

## Zamanaşımı
Hesaplanan tarih: GG.AA.YYYY (kalan: N gün)

## Ön delil envanteri
| Delil | Bizde? | Gerekli? |

## Yargı MCP emsal
| Karar | Tarih | Eğilim |

## TTK m. 5/A
Kapsama girer/girmez

## Şiddet: [emoji] — gerekçe

## Sonraki adımlar
1. /dispute-litigation:dilekce-draft — dava dilekçesi
2. Yönetici Ortak'a eskalasyon (🔴/🟠 ise)
3. Daha fazla bilgi al (sorular)
4. Sulh teklif değerlendirme — /dispute-litigation:settlement-eval
```

## Hatalar / kenar durumlar

- **Dosya yüklemeden "yeni dava" der** → İhtarname/dilekçe yapıştırması istenir
- **Zamanaşımı çok yakın** → 🔴 + büyük uyarı
- **Tahkim klozu var ama mahkemede dava** → 🟠 + tahkim itirazı (HMK 116/c) önerisi
- **Müvekkilin söylediği madde no yanlış** → Mevzuat MCP'den doğrulama, kendi yorum yapma
