# Japonya Mevzuatı — Kullanım Rehberi (v1.7.0)

> **Erişim tipi:** WebFetch (GET) — e-Gov API v2, auth yok
> **Auth:** Yok (e-Gov Digital Agency API — tamamen açık)
> **Kapsam:** Tüm Japon ulusal mevzuatı; ~1.000 kanun İngilizce çeviri mevcut
> **[ŞİRKET ADI] bağlamı:** Japon trading house karşı tarafları (Mitsui, Mitsubishi, JERA), LNG sözleşmeleri

---

## 1. e-Gov API v2 — Tüm Japon Federal Mevzuatı

**Dijital Ajans resmi API'si. Auth yok. Japonca.**

```
# Kanun başlığına göre arama
GET https://laws.e-gov.go.jp/api/2/laws?lawTitle={encoded_baslik}

# Kanun ID ile tam metin
GET https://laws.e-gov.go.jp/api/2/lawdata/{lawId}

# Tüm kanun listesi (büyük yanıt)
GET https://laws.e-gov.go.jp/api/2/lawlists/1
```

Swagger dokümantasyonu: `https://laws.e-gov.go.jp/api/2/swagger-ui`

**Örnek — Şirketler Kanunu aramak:**
```
WebFetch("https://laws.e-gov.go.jp/api/2/laws?lawTitle=%E4%BC%9A%E7%A4%BE%E6%B3%95",
         "Şirketler Kanunu (会社法) araması — lawId değerini çıkar")
```

---

## 2. Japanese Law Translation — İngilizce Çeviri

**Adalet Bakanlığı resmi çevirisi. ~1.000 temel kanun. Auth yok.**

```
GET https://www.japaneselawtranslation.go.jp/en/laws/search?q={sorgu}&search%5B%5D=title
```

**[ŞİRKET ADI] için kritik Japon mevzuatı (İngilizce mevcut):**

| Mevzuat | Japon başlığı | JLT ID | İçerik |
|---|---|---|---|
| Companies Act | 会社法 | 3151 | Şirket kurumu, yapısı |
| Civil Code | 民法 | 2057 | Sözleşme hukuku temeli |
| Act on Prohibition of Private Monopolization (Antimonopoly) | 私的独占の禁止及び公正取引の確保に関する法律 | 53 | Rekabet |
| Foreign Exchange and Foreign Trade Act (FEFTA) | 外国為替及び外国貿易法 | 120 | Yabancı yatırım, ihracat kontrolü |
| Act on the Protection of Personal Information (APPI) | 個人情報の保護に関する法律 | 3003 | Veri koruma |
| Electricity Business Act | 電気事業法 | 2190 | Enerji piyasası |

**Doğrudan kanun metni:**
```
WebFetch("https://www.japaneselawtranslation.go.jp/en/laws/view/3151",
         "Companies Act — şirket birleşmesi prosedürü")

WebFetch("https://www.japaneselawtranslation.go.jp/en/laws/view/120",
         "FEFTA — Japon enerji şirketine yatırım için yabancı yatırımcı bildirimleri")
```

---

## 3. Mahkeme Kararları

⚠️ **Japon mahkeme kararlarına API erişimi yoktur.**

Mevcut ücretsiz seçenekler:
- **Yüksek Mahkeme İngilizce özetler**: `https://www.courts.go.jp/english/Judgments/search/index.html`
- **IP High Court** (İngilizce): `https://www.ip.courts.go.jp/eng/index.html`
- **Westlaw Japan / LexisNexis Japan**: Ücretli

```
WebFetch("https://www.courts.go.jp/english/Judgments/search/index.html",
         "LNG contract force majeure Japon Yüksek Mahkeme kararları")
```

---

## 4. METI — Enerji Bakanlığı Düzenlemeleri

Japonya Ekonomi, Ticaret ve Endüstri Bakanlığı:
```
WebFetch("https://www.meti.go.jp/english/policy/energy_environment/",
         "Japon enerji politikası ve lisans düzenlemeleri")
```

**JFTC** (Japon Rekabet Kurumu):
```
WebFetch("https://www.jftc.go.jp/en/",
         "Enerji sektörü rekabet kararları")
```

---

## Atıf formatı

```
[JP Mevzuat — {Kanun adı} Art.{no} — e-Gov/JLT — GG.AA.YYYY]
[JP Yüksek Mahkeme — {tarih karar özeti} — courts.go.jp — GG.AA.YYYY]
```

---

## [ŞİRKET ADI] için özel notlar

- **Mitsui/Mitsubishi ile LNG sözleşmeleri** — Japon hukuku seçimi veya Singapore/English law; FEFTA bildirimleri
- **JERA** (TEPCO + Chubu Electric JV) — potansiyel LNG alıcısı; Companies Act yapısı
- **APPI** — Japon çalışanlar veya müşterilere ait kişisel veri işleme yükümlülükleri
- Japon şirket araştırması için: `https://www.houjin-bangou.nta.go.jp/en/` (ticaret sicili, auth yok)
- FEFTA kapsamında Japon enerji varlığı edinimi → önceden METI bildirimi zorunlu

*Son güncelleme: 29.05.2026 — v1.7.0. e-Gov API v2 + Japanese Law Translation entegrasyonu.*
