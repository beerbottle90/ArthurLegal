# Yunanistan Hukuku — Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK** — Yunanistan hukuku için iki açık kaynak WebFetch ile
> kullanılır: **RAAEY** (enerji düzenleyici, EN) ve **et.gr** (Resmi Gazete arama).
> AB-türevli mevzuat için **EUR-Lex** Yunanca/İngilizce.
>
> **Durum:** ✅ Açık erişim — API anahtarı gerekmez. **Dil:** Yunanca (EL) birincil;
> RAAEY ve EUR-Lex İngilizce sunar.
>
> **[Müvekkil] neden gerekli?** Yunanistan **TAP (Trans Adriyatik Boru Hattı)** iniş/transit
> noktasıdır — [BORU HATTI PROJESİ]'tan gelen Azerbaycan gazı TAP üzerinden Yunanistan-Arnavutluk-İtalya
> rotasıyla Avrupa'ya ulaşır. TAP'ın Yunanistan ayağı RAAEY (eski RAE) tarafından düzenlenir.
> Gaz piyasası erişimi, şebeke kodu, kapasite tahsisi ve AB enerji uyumu Yunan hukukunu
> ilgilendirir.

---

## Kaynak haritası

| Kaynak | Tür | İçerik | Dil | Öncelik |
|--------|-----|--------|-----|---------|
| raaey.gr/energeia/en | WebFetch (sunucu HTML ✅) | Enerji düzenleme çerçevesi, TAP kararları | EN | P0 — [Müvekkil] odağı |
| search.et.gr/en | WebFetch (Resmi Gazete arama ✅) | Tüm Yunan mevzuatı (ΦΕΚ) | EL + EN arayüz | P1 — tam metin |
| EUR-Lex | WebFetch | AB-türevli Yunan uyum mevzuatı | EL + EN | P1 — AB |
| greeklawdigest.gr | WebFetch | İngilizce konu rehberi (full-text değil) | EN | P2 — referans |

---

## 1. RAAEY — Enerji ve Su Düzenleme Kurumu (BİRİNCİL — [Müvekkil] odağı)

**Kaynak Kurum:** Ρυθμιστική Αρχή Αποβλήτων, Ενέργειας & Υδάτων (RAAEY, eski RAE)
**URL:** `https://www.raaey.gr/energeia/en`
**İçerik:** Elektrik, doğal gaz, YEK, petrol düzenleme çerçeveleri; TAP şebeke kodu,
kapasite kararları, uyum programları (İngilizce). Sunucu-render ✅.

```
WebFetch:
  URL: https://www.raaey.gr/energeia/en/res/framework/
  prompt: "Yunanistan doğal gaz düzenleme çerçevesini ve TAP'a ilişkin kararları listele"
```

**TAP-spesifik:** RAAEY TAP Network Code (Decision 1036/2020), Market Test çerçevesi ve
Compliance Program kararlarını yayımlamıştır — TAP kapasite/erişim sorularında birincil kaynak.

---

## 2. et.gr — Resmi Gazete (Εθνικό Τυπογραφείο / ΦΕΚ)

**Kaynak Kurum:** Ulusal Matbaa (National Printing House)
**URL:** `https://search.et.gr/en/`
**İçerik:** Tüm Yunan kanunları, cumhurbaşkanlığı kararnameleri, bakanlık kararları —
Resmi Gazete (ΦΕΚ — Φύλλο Εφημερίδας της Κυβερνήσεως) tam metni. Ücretsiz
(Law 3861/2010 m.7 gereği). İngilizce arama arayüzü ✅.

```
WebFetch:
  URL: https://search.et.gr/en/
  prompt: "[kanun no/ΦΕΚ sayısı] ile yayını bul ve tam metnini çıkar"
```

**Not:** Yunan kanun metni Yunancadır; et.gr çeviri sunmaz. Tam metin için et.gr,
İngilizce yorum için RAAEY/greeklawdigest birlikte kullan.

---

## 3. [Müvekkil] için kritik Yunan mevzuatı

| Konu | Kanun | Kaynak | [Müvekkil] bağlantısı |
|------|-------|--------|------------------|
| **Enerji Çerçeve Kanunu** | Law 4001/2011 | et.gr / RAAEY | Gaz piyasası, şebeke erişimi |
| **Enerji Borsası** | Law 4425/2016 | et.gr | Toptan enerji ticareti |
| **TAP Şebeke Kodu** | RAAEY Decision 1036/2020 | RAAEY | TAP kapasite/erişim |
| **AB Gaz Direktifi uyumu** | 2009/73/EC ulusal uyum | EUR-Lex + et.gr | Üçüncü taraf erişimi (TPA) |

---

## 4. Tipik kullanım pattern'ı — TAP kapasite/erişim

```
ADIM 1: WebFetch raaey.gr/en → TAP Network Code + kapasite tahsis kararları
ADIM 2: AB Gaz Direktifi (2009/73/EC) → EUR-Lex (eu-legislation-rehberi.md)
ADIM 3: Ulusal uyum detayı → et.gr (Law 4001/2011)
ADIM 4: Atıf → [GR Düzenleme — RAAEY — Decision {no} — GG.AA.YYYY]
```

---

## 5. Atıf disiplini

- `[GR Düzenleme — RAAEY — {karar/çerçeve} — GG.AA.YYYY]` — enerji düzenleyici (İngilizce)
- `[GR Mevzuat — et.gr ΦΕΚ {sayı/yıl} — {kanun} — GG.AA.YYYY]` — Resmi Gazete tam metni
- `[GR Mevzuat — EUR-Lex — {CELEX} (Yunan uyumu) — GG.AA.YYYY]` — AB-türevli
- `[GR — greeklawdigest — {konu}]` — İngilizce yorum (full-text değil, yönlendirme)

**Dil notu:** Resmi metin Yunancadır; RAAEY İngilizcesi düzenleyici özet, kanun değil.
Bağlayıcı analizde Yunanca ΦΕΚ metni esas — kritik hükümde `[review]`.

---

## 6. Sınırlamalar

- **et.gr tam metin Yunanca:** İngilizce çeviri yok; çeviri modele kalır, kritik metinde
  Yunan hukuk teyidi öner.
- **NOMOS (ticari DB) ücretli:** Kapsamlı içtihat+mevzuat için NOMOS abonelik gerekir.
- **İçtihat sınırlı:** Yunan mahkeme kararları için yapılandırılmış ücretsiz kaynak zayıf;
  Symvoulio tis Epikrateias (Danıştay) kararları kısmen ste.gr'de.
- **TAP odaklı kapsam:** Bu rehber [Müvekkil]'ın TAP ilgisine kalibre — genel Yunan ticari/şirket
  hukuku için EUR-Lex (AB uyumu) + et.gr yeterli ama derinlik sınırlı.

---

## Versiyon disiplini

- Bu rehber **v1.9.0** (*Boru Hattı Koridoru*) ile eklendi (20. yargı çevresi).
- raaey.gr/en ve search.et.gr/en erişimi 08.06.2026'da test edildi ✅.

---

*Son güncelleme: 08.06.2026 — v1.9.0. RAAEY (EN) + et.gr (ΦΕΚ) WebFetch; TAP boru hattı odaklı.*
