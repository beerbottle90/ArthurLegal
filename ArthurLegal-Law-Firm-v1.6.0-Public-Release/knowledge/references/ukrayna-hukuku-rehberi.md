# Ukrayna Hukuku — Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK** — Ukrayna hukuku için resmi parlamento veri tabanı
> `zakon.rada.gov.ua` (Verkhovna Rada) WebFetch ile kullanılır. Bu rehber, Claude'un
> `WebFetch` aracını Ukrayna mevzuatıyla birlikte kullanma prosedürünü tanımlar.
>
> **Durum:** ✅ Açık erişim — API anahtarı gerekmez. **Dil:** Ukraynaca (UK) birincil;
> **İngilizce (EN) çeviriler** birçok temel kanun için mevcut.
>
> **[Müvekkil] neden gerekli?** Ukrayna **gaz transit koridoru** (geçmiş ve gelecekteki
> rotalar), **savaş kaynaklı force majeure / sözleşme frustration** analizi, Ukrayna
> karşı taraflarıyla sözleşmeler, AB yaptırım/karşı-yaptırım rejimleriyle etkileşim ve
> yeniden yapılanma (reconstruction) ihale/enerji projeleri açısından ilgilidir.
> **⚠️ Savaş bağlamı:** Ukrayna analizleri sıklıkla force majeure, yaptırım ve
> sözleşme ifa imkânsızlığı eksenlidir — `yaptirim-tarama-rehberi.md` ile birlikte oku.

---

## Kaynak haritası

| Kaynak | Tür | İçerik | Dil | Öncelik |
|--------|-----|--------|-----|---------|
| zakon.rada.gov.ua | WebFetch (sunucu HTML ✅) | Tüm Ukrayna mevzuatı, konsolide | UK + seçili EN | P0 — mevzuat |
| zakon.rada.gov.ua `/en` | WebFetch | İngilizce çeviriler (temel kanunlar) | EN | P0 |
| data.rada.gov.ua | Açık veri portalı | Yapılandırılmış datasetler | UK + EN | P1 — toplu |

---

## 1. zakon.rada.gov.ua — Verkhovna Rada Resmi Mevzuat Portalı

**Kaynak Kurum:** Verkhovna Rada (Ukrayna Parlamentosu)
**URL:** `https://zakon.rada.gov.ua`
**Lisans:** Hükümet portalı, kamu erişimi açık
**İçerik:** Kanunlar, cumhurbaşkanlığı kararnameleri, Bakanlar Kurulu kararları, kodlar
**Format:** Sunucu-render HTML (SPA değil) — WebFetch tam metin döndürür ✅

### URI şeması

```
https://zakon.rada.gov.ua/laws/show/{id}           ← Ukraynaca (örn. 2665-14)
https://zakon.rada.gov.ua/laws/show/{id}/en         ← İngilizce çeviri
https://zakon.rada.gov.ua/laws/show/en/{id}?lang=en ← alternatif EN URL
```

`{id}` formatı: `{numara}-{kanun-dönemi}` (örn. `2665-14` = Petrol ve Gaz Kanunu).
Dil geçişi sayfada `Укр | Eng` olarak görünür.

### WebFetch kullanımı

```
WebFetch:
  URL: https://zakon.rada.gov.ua/laws/show/{id}/en
  prompt: "Ukrayna [kanun adı] tam metnini, yürürlük durumunu ve son değişiklikleri
           çıkar. Transit/enerji/force majeure/yaptırım maddelerine odaklan."
```

---

## 2. data.rada.gov.ua — Açık Veri Portalı

Verkhovna Rada açık veri: mevzuat, kanun teklifleri, oylama sonuçları datasetleri.
`https://data.rada.gov.ua/go/zak?lang=en` (İngilizce arayüz). Toplu/yapılandırılmış
erişim gerekiyorsa bu portal kullanılır; günlük tekil sorgu için zakon.rada yeterli.

---

## 3. [Müvekkil] için kritik Ukrayna mevzuatı

| Konu | Kanun | ID | [Müvekkil] bağlantısı |
|------|-------|-----|------------------|
| **Petrol & Gaz** | Law on Oil and Gas (2001) | `2665-14` | Gaz transit, upstream rejimi |
| **Doğal Gaz Piyasası** | Law on the Natural Gas Market (2015) | `329-19` | AB uyumlu gaz piyasası, transit kodu |
| **Alternatif Yakıtlar** | On Alternative Types of Liquid and Gas Fuel | `1391-14` | LNG/CNG düzenleme |
| **Yaptırımlar** | Law on Sanctions (2014) | `1644-18` | UA yaptırım rejimi — karşı taraf taraması |

> ID bilinmiyorsa: Google `site:zakon.rada.gov.ua/laws {kanun adı}` veya portal araması.

---

## 4. Tipik kullanım pattern'ları

### 4.1 Savaş kaynaklı force majeure / sözleşme frustration

```
ADIM 1: Sözleşmenin governing law'u UA mı, force majeure klozu ne diyor?
ADIM 2: Ukrayna Ticaret ve Sanayi Odası (UCCI) force majeure sertifikası rejimi
        — UA hukuku force majeure'ü resmi sertifikayla kanıtlatır
ADIM 3: WebFetch zakon.rada — Medeni Kanun ifa imkânsızlığı maddeleri
ADIM 4: Atıf → [UA Mevzuat — zakon.rada.gov.ua — {kanun} — GG.AA.YYYY]
```

### 4.2 Ukrayna karşı taraf yaptırım taraması

```
ADIM 1: OpenSanctions → UA karşı tarafı + UA yaptırım listesi (1644-18)
ADIM 2: AB/ABD yaptırımlarıyla çakışma → yaptirim-tarama-rehberi.md
ADIM 3: Karşı-taraf NSDC (Milli Güvenlik Konseyi) yaptırım kararları kontrol
```

---

## 5. Atıf disiplini

- `[UA Mevzuat — zakon.rada.gov.ua — {kanun adı} — GG.AA.YYYY]` — Ukraynaca metin
- `[UA Mevzuat — zakon.rada.gov.ua/en — {kanun} (EN çeviri) — GG.AA.YYYY]` — İngilizce çeviri
- `[UA Yaptırım — NSDC/zakon.rada — {karar} — GG.AA.YYYY]` — yaptırım kararı

**Dil notu:** İngilizce çeviriler her kanunda yok; çeviri tarihi eski olabilir (savaş
döneminde sık değişiklik). Ukraynaca metin esastır — kritik hükümde `[review]` ekle.

---

## 6. Sınırlamalar

- **Savaş kaynaklı hızlı değişim:** Sıkıyönetim (martial law) kararnameleri sık; yürürlük
  durumunu her zaman kontrol et. Geçici tedbirler kalıcı kanunla çelişebilir.
- **İngilizce çeviri gecikmeli:** En yeni değişiklikler önce Ukraynaca yayımlanır.
- **İçtihat sınırlı:** Mahkeme kararları için ayrı reyestr (court.gov.ua) — savaş döneminde
  erişim değişken. Ticari uyuşmazlık çoğunlukla uluslararası tahkim (sözleşme seçimi).
- **Transit gerçeği:** 2020 sonrası gaz transit dinamiği savaşla köklü değişti — güncel
  ticari durum için mevzuat + güncel haber/[Müvekkil] ticari ekibi birlikte değerlendirilmeli.

---

## Versiyon disiplini

- Bu rehber **v1.9.0** (*Boru Hattı Koridoru*) ile eklendi (19. yargı çevresi).
- zakon.rada.gov.ua erişimi 08.06.2026'da test edildi ✅ (Petrol&Gaz Kanunu UK+EN).

---

*Son güncelleme: 08.06.2026 — v1.9.0. zakon.rada.gov.ua WebFetch (UK/EN) + data.rada.gov.ua; savaş/force majeure/yaptırım odaklı.*
