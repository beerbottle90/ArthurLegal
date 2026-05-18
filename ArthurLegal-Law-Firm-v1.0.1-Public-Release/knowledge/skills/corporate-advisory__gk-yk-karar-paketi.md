---
name: gk-yk-karar-paketi
description: >
  Olağan/olağanüstü GK veya YK karar paketi: çağrı + gündem + karar + tescil
  (İTO + TTSG). TTK m. 414/617 anonim/limited GK farkları, m. 390 YK karar
  şekilleri (toplantı vs. sirküler), tescil + gazete ilan takvimi.
user-invocable: true
---

# GK/YK Karar Paketi

## Karar tipi tespit

| Tip | Senaryo | Madde |
|---|---|---|
| Olağan GK | Yıllık (3 ay içinde — Mart sonu) | TTK m. 409 |
| Olağanüstü GK | Sermaye, esas sözleşme, birleşme, vd. | TTK m. 410-413 |
| Olağan YK | Aylık/üç aylık | TTK m. 365 |
| YK sirküler | Acil karar (oybirliği şart) | TTK m. 390 |
| Tek pay sahipli GK | "Genel kurul" yerine ortağın tek kararı | TTK m. 408/3 |

## Şirket türü farkları

### Anonim Şirket (TTK m. 329 vd.)

| Konu | Kural |
|---|---|
| **GK çağrı** | TTK m. 414 — **ilan + KEP + iadeli posta** (3 yöntem) |
| Çağrı süresi | İlan tarihinden **en az 2 hafta önce** |
| Gündem | İlanla birlikte; gündem dışı madde tartışılamaz |
| Karar nisabı (olağan) | %50 +1 toplantı + %50 +1 karar (TTK m. 418) |
| Karar nisabı (esas sözleşme değ.) | %66 toplantı + %50 +1 karar (genelde) |
| **YK toplantı** | TTK m. 390 — fiziki/dijital; %50 toplantı + %50 karar (varsayılan) |
| **YK sirküler** | TTK m. 390/2 — yazılı + **oybirliği** |
| Tescil | İTO 15 gün içinde + TTSG ilan |

### Limited Şirket (TTK m. 573 vd.)

| Konu | Kural |
|---|---|
| **GK çağrı** | TTK m. 617 — **ilan ZORUNLU değil**, KEP + posta yeterli |
| Çağrı süresi | En az 1 hafta önce |
| Karar nisabı (olağan) | %50 +1 (esas sözleşmeden artırılabilir) |
| Karar nisabı (esas sözleşme değ.) | %66 (TTK m. 621) |
| **YK** (varsa) | Kural daha esnek; **müdür** seviyesinde karar (m. 623) |
| Tescil | İTO + TTSG (anonim ile aynı) |

## Gündem maddeleri (olağan GK örneği)

1. Açılış + divan teşkili (1 başkan + 2 oy toplayıcı + 1 yazman)
2. Yönetim Kurulu yıllık faaliyet raporu
3. Bağımsız denetçi raporu (varsa SPK kayıt + yıllık sınırı aşan)
4. Mali tablolar onayı
5. YK ibrası
6. **Kâr dağıtım kararı** (varsa)
7. YK üye seçimi/atanması (görev süresi dolduysa)
8. Denetçi seçimi
9. YK üyelerine huzur hakkı belirleme (TTK m. 394)
10. Diğer

## YK karar şekli (m. 390)

**Toplantı:**
- Fiziki / dijital (e-toplantı) — 2017 değişikliği ile mümkün
- Karar **çoğunluk** (genelde %50 +1)
- Tutanak imzalı + arşivlenir

**Sirküler (yazılı karar):**
- **Tüm üyelerin oybirliği** şart
- Toplantı yapmadan karar
- "Sirküler karar" → her üye ayrı imza
- Acil ve net konular için (örn. tek imza yetkilisi atama)

## Tescil + ilan akışı

```
[Karar alındı]
    ↓
[İTO (Ticaret Sicili Müdürlüğü) tescil başvurusu — 15 gün içinde]
    - Karar tutanağı (noter onaylı imza sirküleri)
    - Hazirun cetveli (GK için)
    - Sermaye artırımı varsa: taahhüt + ödeme belgesi
    - Esas sözleşme değişikliği varsa: yeni metin
    ↓
[Tescil onaylanır]
    ↓
[TTSG (Türkiye Ticaret Sicili Gazetesi) ilanı — 15-30 gün içinde]
    - Tescil sonrası otomatik
    ↓
[MERSİS güncellemesi]
[Vergi dairesine bildirim (gerekirse — örn. ortak değişikliği)]
[Bankalara bildirim (imza sirküleri değişti)]
[(varsa) SPK bildirim — halka açık ise]
```

## Çıktı paketi

```markdown
[ÜST BAŞLIK — TASLAK + İMZA + TESCİL BEKLİYOR]

# GK/YK Karar Paketi — [Müvekkil rumuz] — [Karar türü]

## ⚠️ İnceleyen notu
- Kaynaklar: Mevzuat MCP [✓ TTK m. X]
- Tescil son tarih: GG.AA.YYYY (+15 g)
- TTSG ilan beklenen: GG.AA.YYYY
- Şirket türü: AŞ / LŞ

## Çağrı evraki (varsa GK)
- İlan metni (Resmi Gazete + müvekkilin web sitesi + KEP)
- Gündem
- Hazirun cetveli formu

## Karar tutanağı
[TASLAK — divan teşkili + karar metni]

## Tescil evrakı
- [ ] Karar tutanağı (noter onayı)
- [ ] Hazirun cetveli (GK için)
- [ ] (Esas sözleşme değ.) yeni metin
- [ ] (Sermaye artırımı) taahhüt + ödeme belgesi
- [ ] (Birleşme/bölünme) ayrı paket

## Tescil takvim
- İTO başvuru: GG.AA.YYYY
- Tescil onayı tahmini: GG.AA.YYYY (+5-10 g)
- TTSG ilan: GG.AA.YYYY

## Sonraki adımlar
- [Noter randevusu için Office Manager]
- [İTO başvurusu için stajyer]
- [Müvekkilin imza yetkilisi koordinasyonu]
- /corporate-advisory:matter-workspace
```

## Hatalar

- **Olağan GK 3 ay süresini geçirme** (TTK m. 409 — Mart sonu) → ileri tarihli GK + idari para cezası
- **AŞ'de çağrı ilanını atlama** (TTK m. 414) → GK kararı iptal edilebilir
- **Esas sözleşme değişikliği için %66 nisabını gözden kaçırma** → tescil reddi
- **YK sirküler kararında oybirliği koşulunu unutma** → karar geçersiz
- **TTSG ilan tarihini takip etmeme** → resmi ilan tarihinden itibaren süreler başlar
