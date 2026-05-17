---
name: new-client-intake
description: >
  Yeni müvekkil ön sohbet sonrası intake akışı: müvekkil bilgisi alma, talep
  özeti, matter tipi belirleme + plugin yönlendirmesi, aciliyet kontrolü, sonraki
  zorunlu adımlar (conflict-check, MASAK, sanctions, KVKK, fee, vekalet) tetikleme.
user-invocable: true
---

# New Client Intake — Yeni Müvekkil Ön Sohbet

## Tetikleyici

İlk temas (telefon / web / referans) sonrası, atanan ortak müvekkille **ön sohbet**i yaptıktan sonra. Genelde 30-60 dakika sürer.

## Pre-matter klasörü

```
~/.claude/plugins/config/claude-for-legal-law-firm/pre-matter/<YYYYMMDD>__<müvekkil-rumuz>/
```

Bu skill bu klasöre çıktı yazar. Karar (KABUL/RET) sonrası matter klasörüne taşınır.

## Adımlar

### 1. Müvekkil bilgisi

**Gerçek kişi:**
- Rumuz (kayıt için — gerçek isim KVKK uyarınca minimum)
- TC kimlik no (kimlik tespit için sonradan MASAK)
- Doğum tarihi-yeri
- İkamet adresi
- Telefon + e-posta (mümkünse KEP)
- Meslek + işveren

**Tüzel kişi:**
- Ünvan (kısaltılmış rumuz da OK ama tam ünvanı sonradan kayda al)
- Vergi no + MERSİS no
- Faaliyet alanı (NACE)
- Yetkili temsilci (imza yetkili)
- KEP adresi (zorunlu — AŞ/LŞ için)
- Ortaklık yapısı genel (UBO için sonradan)

### 2. Talep özeti

> "Bizden ne istiyorsunuz? Size nasıl yardımcı olabiliriz?"

- 1-2 cümle özet
- Hukuki problem mi? Ticari pratik sorun mu?
- Karşı taraf var mı? (varsa: kim — rumuz + tüzel kişi tipi)
- Tahmini değer (uyuşmazlığa konu tutar)
- Tarih + süreler (aciliyet kontrolü)

### 3. Matter tipi → plugin yönlendirmesi

| Talep | Plugin |
|---|---|
| Müvekkil davacı/davalı (ticari/medeni) | `dispute-litigation` |
| Müvekkil idari kararı iptal istiyor | `administrative-litigation` |
| Müvekkil vergi tarhiyatı iptal | `tax-litigation` |
| Müvekkil ceza şüphelisi/sanığı / mağdur müdahil | `criminal-defense` |
| Müvekkil sözleşme yazımı/inceleme istiyor | `commercial-advisory` |
| Müvekkilin GK/YK/M&A işlemi | `corporate-advisory` |
| Müvekkil işveren/işçi iş hukuku | `employment-advisory` |
| Müvekkilin marka/patent/tasarım/UDRP | `ip-advisory` |
| Aile/miras/boşanma | **KAPSAM DIŞI** — başka büroya yönlendir (bu pakette plugin yok) |
| Sektör ihtisas (denizcilik, enerji uzman vd.) | Harici uzman önerisi |

### 4. Aciliyet kontrolü

| Süre durumu | Etiket |
|---|---|
| Dava süresi < 7 gün | 🔴 ACİL — bu hafta karar |
| Dava süresi < 30 gün | 🟠 Yüksek — bu hafta intake tamamla |
| Sözleşme imza < 3 gün | 🟠 Yüksek — 24 saat içinde değerlendirme |
| Tutuklu müvekkil (ceza) | 🔴 ACİL — 48 saat sınırı |
| Süre kritik değil | 🟢 Standart akış |

### 5. Müvekkilin "hızlı bilgi" kontrolü (Av. K. m. 36 baseline)

İlk sohbette müvekkil ne paylaştıysa:
- **Sözlü** anlatım Av. K. m. 36 kapsamında **gizli**
- Önerilen "ücret sözleşmesi imzalanmadan iş başlamaz" ilkesi — istisna: acil durum (örn. tutuklu müdafi atama)
- Ön sohbette ne kadar bilgi paylaşıldı not düş

### 6. Sonraki zorunlu adımlar listesi

```
ZORUNLU SONRAKİ ADIMLAR:
[ ] /firm-operations:conflict-check  ← İLK + KRİTİK
[ ] /firm-operations:masak-kontrol   ← Kimlik tespit + UBO
[ ] /firm-operations:sanctions-check ← Tüzel/yabancı için
[ ] /firm-operations:kvkk-aydinlatma ← Aydınlatma metni
[ ] /firm-operations:fee-agreement   ← Ücret sözleşmesi
[ ] /firm-operations:vekalet-sablon  ← Vekalet
[ ] /firm-operations:matter-open     ← Matter klasörü açma
```

Conflict bulunursa **iş zinciri durur** → ret kararı.

## Çıktı

```markdown
[ÜST BAŞLIK — INTAKE NOTU — DAHİLİ]

# Müvekkil Intake — [Rumuz] — [Tarih]

## ⚠️ İnceleyen notu
- Pre-matter klasörü: pre-matter/[YYYYMMDD]__[rumuz]/
- Aciliyet: 🔴/🟠/🟢
- Önerilen plugin: [dispute-litigation / commercial-advisory / vd.]
- Sonraki zorunlu adımlar: 7 adım

## Müvekkil
- Tip: Bireysel / Tüzel kişi
- Rumuz: [...]
- Kimlik (sonradan MASAK): [TC / Vergi no]
- KEP: [varsa]
- İletişim: [...]

## Talep özeti
[1-2 cümle]
- Karşı taraf: [varsa rumuz + tip]
- Tahmini değer: [TL]
- Süre kritik mi: ✓/✗

## Matter tipi
[Plugin]: [...] — gerekçe

## Aciliyet
🔴/🟠/🟢 — [neden]

## Sonraki ZORUNLU adımlar
1. /firm-operations:conflict-check (İLK — bu olmadan devam EDİLMEZ)
2. /firm-operations:masak-kontrol
3. /firm-operations:sanctions-check (tüzel kişi/yabancı için)
4. /firm-operations:kvkk-aydinlatma
5. /firm-operations:fee-agreement
6. /firm-operations:vekalet-sablon
7. /firm-operations:matter-open

## Conflict ve MASAK sonrası karar
[Henüz değerlendirilmedi — adım 1-3 tamamlanınca güncellenecek]

## Atanan ortak
[Yönetici Ortak ataması veya öneri]
```

## Hatalar

- **Müvekkilin gerçek ismini intake notuna yazma** — rumuz kullan (gerçek isim MASAK + KVKK kontrolünden sonra sadece matter dosyasında)
- **Conflict check tetiklenmeden iş başlatma** — Av. K. m. 38 ihlal riski
- **Aciliyet yanlış değerlendirme** — tutuklu müvekkil veya 7 g dava süresi varsa hemen Yönetici Ortak'a bildir
- **Müvekkilin "şimdi bilgi vereyim, sonra anlaşırız" baskısı** — ücret sözleşmesi olmadan derin matter bilgisi alma; özet düzeyde tut
- **KAPSAM DIŞI matter'ı atlayıp kabul** — örn. boşanma davasını "biz hallederiz" deyip alma — bu pakette family plugin yok, yetersiz hizmet riski
