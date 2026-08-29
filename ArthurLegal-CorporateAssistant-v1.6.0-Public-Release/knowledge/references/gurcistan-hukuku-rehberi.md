# Gürcistan Hukuku — Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK** — Gürcistan hukuku için resmi yasama veri tabanı
> `matsne.gov.ge` WebFetch ile kullanılır. Bu rehber, Claude'un `WebFetch` aracını
> Gürcü mevzuatıyla birlikte kullanma prosedürünü tanımlar.
>
> **Durum:** ✅ Açık erişim — API anahtarı gerekmez. **Dil:** Gürcüce (KA) birincil;
> **İngilizce (EN) ve Rusça (RU) çeviriler** birçok kanun için mevcut.
>
> **[ŞİRKET ADI] neden gerekli?** Gürcistan, [ŞİRKET ADI]'ın **BTC (Bakü-Tiflis-Ceyhan ham petrol)**
> ve **SCP (Güney Kafkasya Boru Hattı — gaz, [BORU HATTI PROJESİ] besleyicisi)** boru hatlarının
> **transit ülkesidir**. [ŞİRKET ADI] Georgia Petroleum ülkenin en büyük akaryakıt ve doğal gaz
> dağıtım operatörlerindendir. Transit anlaşmaları, enerji lisansları, gümrük, çevre
> izinleri ve istihdam Gürcü hukukunu doğrudan ilgilendirir.

---

## Kaynak haritası

| Kaynak | Tür | İçerik | Dil | Öncelik |
|--------|-----|--------|-----|---------|
| matsne.gov.ge | WebFetch (sunucu HTML ✅) | Tüm Gürcü mevzuatı, konsolide sürümler | KA + EN + RU | P0 — mevzuat |
| matsne.gov.ge `/en/` | WebFetch | İngilizce resmi çeviriler | EN | P0 — [ŞİRKET ADI] odağı |
| RAAEY (Yunanistan'la kıyas için bkz. enerji) | — | — | — | — |

---

## 1. matsne.gov.ge — Resmi Yasama Bülteni (საქართველოს საკანონმდებლო მაცნე)

**Kaynak Kurum:** Gürcistan Adalet Bakanlığı — Yasama Bülteni (LEPL)
**URL:** `https://matsne.gov.ge`
**Lisans:** Hükümet portalı, kamu erişimi açık
**İçerik:** Kanunlar, cumhurbaşkanlığı/hükümet kararnameleri, bakanlık emirleri, konsolide metinler
**Format:** Sunucu-render HTML (SPA değil) — WebFetch tam metin döndürür ✅. PDF + .doc export de var.

### URI şeması

```
https://matsne.gov.ge/ka/document/view/{id}        ← Gürcüce
https://matsne.gov.ge/en/document/view/{id}        ← İngilizce resmi çeviri
https://matsne.gov.ge/ru/document/view/{id}        ← Rusça
https://matsne.gov.ge/en/document/download/{id}/{ver}/en/pdf   ← PDF indir
```

Her belge sayfası üst köşede `ქარ | ENG | РУС` dil geçişi sunar; konsolide
(değişiklik işlenmiş) sürümler tarih bazlı listelenir.

### WebFetch kullanımı

```
WebFetch:
  URL: https://matsne.gov.ge/en/document/view/{id}
  prompt: "Gürcistan [kanun adı] tam metnini, yürürlük tarihini ve son
           konsolide sürümünü çıkar. Transit/enerji/lisans maddelerine odaklan."
```

---

## 2. [ŞİRKET ADI] için kritik Gürcü mevzuatı

| Konu | Kanun | matsne ID | [ŞİRKET ADI] bağlantısı |
|------|-------|-----------|------------------|
| **Petrol & Gaz** | Law of Georgia on Oil and Gas (1999) | `18424` | BTC/SCP transit, upstream lisans |
| **Elektrik & Doğal Gaz** | Law on Electricity and Natural Gas | `31744` | Gaz dağıtım, SCP transit, lisans |
| **Enerji & Su Temini** | Law on Energy and Water Supply (2019) | `4747785` | Yeni enerji çerçeve kanunu, GNERC düzenleme |
| **Çevre Etki İzni** | Law on Environmental Impact Permits | `20206` | Boru hattı projeleri ÇED |
| **Demiryolu Kodu** | Railway Code of Georgia | `14404` | Ham petrol demiryolu taşıma (alternatif) |

> ID bilinmiyorsa: `https://matsne.gov.ge/en/document/view/` ana sayfasından arama
> veya Google `site:matsne.gov.ge/en {kanun adı}` ile bul.

---

## 3. GNERC — Enerji Düzenleyici (referans)

Gürcistan Ulusal Enerji ve Su Temini Düzenleme Komisyonu (GNERC):
`https://gnerc.org/en` — lisanslar, tarifeler, düzenleyici kararlar (İngilizce).
Boru hattı/gaz dağıtım lisans şartları için kullanılabilir.

---

## 4. Tipik kullanım pattern'ları

### 4.1 BTC/SCP transit anlaşması incelemesi

```
ADIM 1: WebFetch matsne /en/document/view/18424 (Petrol ve Gaz Kanunu)
        → transit boru hattı tanımı, devlet hakları, lisans rejimi
ADIM 2: Çevre izni (20206) — boru hattı ÇED yükümlülükleri
ADIM 3: Atıf → [GE Mevzuat — matsne.gov.ge — {kanun} — GG.AA.YYYY]
```

### 4.2 [ŞİRKET ADI] Georgia Petroleum gaz dağıtım lisansı

```
ADIM 1: Elektrik ve Doğal Gaz Kanunu (31744) + Enerji ve Su Temini (4747785)
ADIM 2: GNERC lisans şartları (gnerc.org/en)
ADIM 3: Türk hukuku ile kıyas gerekiyorsa → EPDK rehberi
```

---

## 5. Atıf disiplini

- `[GE Mevzuat — matsne.gov.ge — {kanun adı} — GG.AA.YYYY]` — matsne'den çekilen mevzuat
- `[GE Mevzuat — matsne.gov.ge/en — {kanun} (EN çeviri) — GG.AA.YYYY]` — İngilizce resmi çeviri
- `[GE Düzenleme — GNERC — {karar/lisans} — GG.AA.YYYY]` — enerji düzenleyici kararı

**Dil notu:** İngilizce çeviri "resmi" olsa da Gürcüce metin esastır; kritik hükümlerde
`[review]` + Gürcü hukuk çevirisi teyidi öner. Çeviri eski olabilir — konsolide tarih kontrol et.

---

## 6. Sınırlamalar

- **İngilizce çeviri her kanunda yok** veya güncel olmayabilir — Gürcüce metin bağlayıcı.
- **İçtihat sınırlı:** matsne mevzuat odaklı; Gürcü mahkeme kararları için ayrı portal
  (supremecourt.ge) sınırlı erişim. Ticari uyuşmazlık çoğunlukla tahkim (sözleşme seçimi).
- **Transit anlaşmaları gizli:** BTC/SCP devletlerarası anlaşmaları (host government agreement)
  matsne'de tam yayımlanmamış olabilir — [ŞİRKET ADI] iç arşivi + dış vekil gerekir.

---

## Versiyon disiplini

- Bu rehber **v1.9.0** (*Boru Hattı Koridoru*) ile eklendi (18. yargı çevresi).
- matsne.gov.ge erişimi 08.06.2026'da test edildi ✅ (Petrol&Gaz + Elektrik&Gaz kanunları EN).

---

*Son güncelleme: 08.06.2026 — v1.9.0. matsne.gov.ge WebFetch (KA/EN/RU); BTC/SCP transit odaklı.*
