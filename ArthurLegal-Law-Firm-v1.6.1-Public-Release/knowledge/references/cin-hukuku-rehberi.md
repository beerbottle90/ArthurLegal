# Çin Hukuku — Kullanım Rehberi (HuggingFace + court.gov.cn + Yuandian MCP)

> **Erişim yöntemleri:**
> 1. **HuggingFace Datasets API** — 22,552 kanun ve düzenlemenin tam metni, filtrelenebilir JSON
> 2. **court.gov.cn (SPC)** — Yüksek Mahkeme yargı yorumları + 指导性案例 (Guiding Cases, 1–279+);
>    sunucu taraflı render, giriş yok, WebFetch doğrudan çalışır ✅
> 3. **flk.npc.gov.cn** — Resmi NPC portalı (SPA tabanlı; WebFetch çalışmaz,
>    programatik erişim için Python/Node.js gerekir — referans amaçlıdır)
>
> **Durum:** ✅ Açık erişim — HF API ve court.gov.cn API anahtarı gerektirmez.
> **Dil:** Yalnızca Çince (中文). Çeviri modele kalır — kritik hukuki metinlerde `[review]` ekle.
>
> **[Müvekkil] neden gerekli?** Çin firmalarıyla enerji tedarik sözleşmeleri (CNOOC, Sinopec,
> PetroChina, CNPC), BRI projeleri, Çin hukukunu uygulanacak hukuk olarak seçen sözleşmeler,
> Çin karşı taraf hukuki durum tespiti (due diligence) ve Çin bağlantılı yaptırım/uyum takibi.

---

## Kaynak haritası

| Kaynak | Tür | İçerik | Dil | Kapsam |
|--------|-----|--------|-----|--------|
| HuggingFace Datasets API (twang2218) | JSON API | 22,552 kanun + düzenleme, tam metin | ZH | **P0 — mevzuat** |
| court.gov.cn (SPC) | Sunucu HTML — WebFetch ✅ | 指导性案例 279+, yargı yorumları, haberler | ZH | **P1 — içtihat/yorum** |
| CAIL Serisi (2018–2024) | GitHub statik dataset | 2,68M+ dava (çoğunluk ceza), yıllık güncel | ZH | P2 — offline/araştırma |
| flk.npc.gov.cn | SPA (WebFetch çalışmaz) | Resmi NPC kaynağı, 45K+ belge | ZH | referans |
| wenshu.court.gov.cn | SPA + login gerekli | Mahkeme kararları | ZH | erişim kısıtlı (2024+) |

---

## 1. HuggingFace Datasets API — Çin Mevzuatı

**Dataset:** `twang2218/chinese-law-and-regulations`
**Kaynak:** flk.npc.gov.cn (NPC resmi portalı) aynalı corpus
**Boyut:** 22,552 kayıt, ~160 MB
**Lisans:** Apache 2.0
**Güncelleme:** Ara sıra (son yayınlanma: 2024)

### Alanlar (kolonlar)

| Alan | Tür | Açıklama |
|------|-----|---------|
| `title` | string | Kanun adı (Çince) |
| `type` | enum | Mevzuat türü (bkz. aşağıda) |
| `office` | string | Yayınlayan kurum |
| `office_level` | enum | Kurum düzeyi |
| `status` | enum | Yürürlük durumu |
| `publish_date` | timestamp | Yayın tarihi |
| `effective_date` | timestamp | Yürürlüğe giriş tarihi |
| `effective_period` | enum | Yürürlük dönemi (2000_2020 vb.) |
| `content` | string | Tam metin (Markdown formatında) |

### Mevzuat türleri (`type`)

| Çince | Türkçe | Açıklama |
|-------|--------|---------|
| 宪法 | Anayasa | Çin Halk Cumhuriyeti Anayasası |
| 法律 | Kanun | NPC veya NPC Daimi Komitesi tarafından kabul edilen |
| 行政法规 | İdari Yönetmelik | Devlet Konseyi tarafından yayımlanan |
| 部门规章 | Bakanlık Yönetmeliği | Bakanlıklar tarafından |
| 地方性法规 | Yerel Yönetmelik | Eyalet/Şehir meclisleri |
| 司法解释 | Yargı Yorumu | Yüksek Halk Mahkemesi yorumları |
| 地方政府规章 | Yerel Hükümet Yönetmeliği | Şehir/ilçe yönetimleri |

### Yürürlük durumları (`status`)

| Çince | Türkçe |
|-------|--------|
| 有效 | Yürürlükte |
| 已修改 | Değiştirilmiş (daha yeni sürüm var) |
| 已废止 | Yürürlükten kaldırılmış |
| 部分有效 | Kısmen yürürlükte |

---

## 2. API Endpoint'leri ve Kullanım Kalıpları

### 2.1 Başlık araması — `LIKE` filtresi

```
WebFetch:
  URL: https://datasets-server.huggingface.co/filter?dataset=twang2218%2Fchinese-law-and-regulations&config=default&split=train&where=%22title%22+LIKE+%27%25[ARAMA_TERİMİ]%25%27&offset=0&length=10
  prompt: "Sonuçları listele: başlık, tür, yürürlük durumu, yayın tarihi"
```

**Sık kullanılan arama terimleri:**

| Arama | URL-encoded | Türkçe |
|-------|-------------|--------|
| `公司法` | `%E5%85%AC%E5%8F%B8%E6%B3%95` | Şirketler Kanunu |
| `合同法` | `%E5%90%88%E5%90%8C%E6%B3%95` | Sözleşme Kanunu (eski) |
| `民法典` | `%E6%B0%91%E6%B3%95%E5%85%B8` | Medeni Kanun (2021) |
| `劳动法` | `%E5%8A%B3%E5%8A%A8%E6%B3%95` | İş Kanunu |
| `劳动合同法` | `%E5%8A%B3%E5%8A%A8%E5%90%88%E5%90%8C%E6%B3%95` | İş Sözleşmesi Kanunu |
| `税法` | `%E7%A8%8E%E6%B3%95` | Vergi Kanunu |
| `反垄断法` | `%E5%8F%8D%E5%9E%84%E6%96%AD%E6%B3%95` | Rekabet Kanunu |
| `仲裁法` | `%E4%BB%B2%E8%A3%81%E6%B3%95` | Tahkim Kanunu |
| `外商投资法` | `%E5%A4%96%E5%95%86%E6%8A%95%E8%B5%84%E6%B3%95` | Yabancı Yatırım Kanunu |
| `石油` | `%E7%9F%B3%E6%B2%B9` | Petrol |
| `能源法` | `%E8%83%BD%E6%BA%90%E6%B3%95` | Enerji Kanunu |
| `个人信息保护法` | `%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF%E4%BF%9D%E6%8A%A4%E6%B3%95` | Kişisel Veri Koruma Kanunu |
| `反制裁法` | `%E5%8F%8D%E5%88%B6%E8%A3%81%E6%B3%95` | Karşı Yaptırım Kanunu |

### 2.2 Tam ad ile belirli kanunu getir

```
WebFetch:
  URL: https://datasets-server.huggingface.co/filter?dataset=twang2218%2Fchinese-law-and-regulations&config=default&split=train&where=%22title%22+%3D+%27%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%85%AC%E5%8F%B8%E6%B3%95%27+AND+%22status%22+%3D+%27%E6%9C%89%E6%95%88%27&offset=0&length=1
  prompt: "Şirketler Kanununun yürürlükteki tam metnini ver: başlık, yayın tarihi, kurum ve madde içerikleri"
```

### 2.3 Yürürlükte kanunları tür filtresiyle listele

```
WebFetch:
  URL: https://datasets-server.huggingface.co/filter?dataset=twang2218%2Fchinese-law-and-regulations&config=default&split=train&where=%22type%22+%3D+%27%E6%B3%95%E5%BE%8B%27+AND+%22status%22+%3D+%27%E6%9C%89%E6%95%88%27&offset=0&length=20
  prompt: "Yürürlükteki kanunları (法律) listele: başlık, yayın tarihi, kurum"
```

### 2.4 Arama olmadan sayfalı listeleme

```
WebFetch:
  URL: https://datasets-server.huggingface.co/rows?dataset=twang2218%2Fchinese-law-and-regulations&config=default&split=train&offset=0&limit=10
  prompt: "İlk 10 kaydı listele: başlık, tür, yürürlük durumu"
```

**Parametreler:**
- `offset` — kaçıncı kayıttan başla (0-tabanlı)
- `limit` / `length` — kaç kayıt getir (max 100)
- `where` — SQL WHERE koşulu; kolon adları çift tırnak `"`, string değerler tek tırnak `'`

---

## 3. [Müvekkil] için hangi kanunlar?

| Konu | Çince Kanun Adı | [Müvekkil] Bağlantısı |
|------|-----------------|-----------------|
| **Şirket yapısı** | 中华人民共和国公司法 (2023 rev.) | Çin bağlı ortaklık / JV kurulumu |
| **Yabancı yatırım** | 外商投资法 (2019) | Çin'e yabancı sermaye rejimi |
| **Sözleşme hukuku** | 中华人民共和国民法典 (2021) — 合同编 | Governing law Çin seçilmişse |
| **Enerji** | 中华人民共和国能源法 (2024) | Enerji tedarik sözleşmeleri |
| **Petrol & Gaz** | 石油及天然气资源法 / 对外合作开采陆上石油资源条例 | CNOOC/CNPC ile işbirliği |
| **Tahkim** | 中华人民共和国仲裁法 | CIETAC tahkimi — Çin seated |
| **Rekabet** | 中华人民共和国反垄断法 (2022 rev.) | Piyasa davranışı |
| **Veri / PDPA** | 个人信息保护法 (PIPL, 2021) | Çin KVKK eşdeğeri — veri transferi |
| **Yaptırım karşı** | 反外国制裁法 (2021) | Karşı yaptırım yükümlülükleri (ABD/AB yaptırımlarıyla çakışma) |
| **İş hukuku** | 中华人民共和国劳动法 + 劳动合同法 | Çin'deki çalışanlar |
| **Vergi** | 企业所得税法 | Kurumlar Vergisi + TP |

---

## 4. Yargı Kararları

### 4.1 CAIL Serisi (2018–2025) — Offline Araştırma Dataset

CAIL (China AI & Law Challenge) yıllık yarışma serisi; **2018'de kalmıyor**, her yıl güncelleniyor.

| Versiyon | Repo | Kayıt | Kapsam | Durum |
|----------|------|-------|--------|-------|
| CAIL2018 | github.com/thunlp/CAIL | 2,68M ceza davası | Wenshu 2013–2018 | Arşiv |
| CAIL2019 | china-ai-law-challenge/CAIL2019 | — | Ceza + hukuki soru yanıtlama | Arşiv |
| CAIL2020 | china-ai-law-challenge/CAIL2020 | — | Ceza, davranış tanıma | Arşiv |
| CAIL2021 | china-ai-law-challenge/CAIL2021 | — | Olay çıkarımı, dava özeti | Arşiv |
| CAIL2022 | china-ai-law-challenge/CAIL2022 | 26K+ soru | Sınav QA, tür arama, karar tahmini (8 track) | Arşiv |
| CAIL2023 | china-ai-law-challenge/CAIL2023 | — | LLM tabanlı hukuk görevleri | Arşiv |
| CAIL2024 | china-ai-law-challenge/CAIL2024 | — | Karar yorumlama, uyuşmazlık analizi (Tem 2025) | Son sürüm |

**CAIL2018 JSON örnek yapısı:**
```json
{
  "fact": "被告人张某于2017年...",
  "meta": {
    "criminals": ["张某"],
    "term_of_imprisonment": {"death_penalty": false, "life_imprisonment": false, "imprisonment": 36},
    "charge": ["盗窃"],
    "relevant_articles": [264]
  }
}
```

**Not:** CAIL verileri ağırlıklı ceza hukuku — ticari/sözleşme uyuşmazlığı yok.
Offline analiz / NLP / araştırma için kullanılır; canlı arama değil.

---

### 4.2 court.gov.cn (SPC) — Yargı Yorumları ve Guiding Cases

**URL:** `https://www.court.gov.cn`
**Durum:** ✅ Sunucu taraflı render — WebFetch doğrudan çalışır, giriş gerekmez.
**Kapsam:** 最高人民法院 (Yüksek Halk Mahkemesi — SPC) resmi sitesi.

| Sayfa | URL | İçerik |
|-------|-----|--------|
| Yargı yorumları + Guiding Cases | `/shenpan.html` | 指导性案例 279+, yeni yargı yorumları |
| Duyurular | `/fabu.html` | Resmi SPC duyuruları |
| Haberler | `/zixun.html` | SPC güncel haberler |

**Guiding Cases (指导性案例):** SPC tarafından yayımlanan, tüm mahkemelerin uyması beklenen emsal niteliğinde kararlar.
- Sözleşme, ticaret, fikri mülkiyet, çevre ve ceza konularını kapsar.
- court.gov.cn/shenpan.html → "指导性案例" bölümünden listeye erişilir.

**Kullanım:**
```
WebFetch:
  URL: https://www.court.gov.cn/shenpan.html
  prompt: "指导性案例 listele: numara, başlık, konu alanı. Özellikle sözleşme veya ticari uyuşmazlık
           olanları işaretle."
```

---


## 5. flk.npc.gov.cn — Resmi Portal (Referans)

Resmi URL: `https://flk.npc.gov.cn/`

SPA (Vite/Vue tabanlı) mimarisi nedeniyle `WebFetch` yalnızca boş HTML döndürür.
Programatik erişim için Python `requests` + session veya Go crawler gerekir:
- Repo: https://github.com/twang2218/law-datasets (crawler.go / crawler.py)
- API endpoint (JS içinde): `https://flk.npc.gov.cn/api/` (GET, AJAX headers gerekli)
- Doküman sunucu: `https://wb.flk.npc.gov.cn` (SSL sertifikası süresi dolmuş — erişim yok)

**Günlük kullanım için HuggingFace mirror yeterli;** resmi portal kaynakları şüphe
durumunda teyit için kullanılır.

---

## 6. Tipik kullanım pattern'ları

### 6.1 Sözleşme governing-law incelemesi (Çin hukuku seçilmişse)

```
ADIM 1: İlgili kanunu getir
  WebFetch: HF filter → "title" LIKE '%民法典%' AND "status" = '有效'
  → content alanından ilgili hükümleri oku

ADIM 2: Sözleşme maddelerini Çin kanununun ilgili hükümleriyle karşılaştır

ADIM 3: Atıf ekle → [CN Mevzuat — HuggingFace/twang2218 — {başlık} — GG.AA.YYYY]
```

### 6.2 Çin karşı taraf due diligence (enerji tedarik)

```
ADIM 1: OpenSanctions → Çin şirketinin yaptırım durumu kontrol
ADIM 2: HF filter → 外商投资法 + 石油 + 能源法 — tedarik kısıtlamaları kontrol
ADIM 3: Karşı Yaptırım Kanunu (反外国制裁法) — ABD/AB yaptırım çakışma riski
```

### 6.3 PIPL (Kişisel Veri) uyum kontrolü

```
ADIM 1: HF filter → "title" LIKE '%个人信息保护法%' AND "status" = '有效'
ADIM 2: Veri transfer maddeleri (madde 38-43) — Çin dışı transfer koşulları
ADIM 3: TR KVKK ile karşılaştır → her iki yükümlülük paralel uygulanır
```

### 6.4 CIETAC tahkimi için kanun teyidi

```
ADIM 1: HF filter → "title" LIKE '%仲裁法%'
ADIM 2: 中华人民共和国仲裁法 — geçerlilik, itiraz, tenfiz maddeleri
ADIM 3: NY Konvansiyonu (m.54 tenfiz) + governing-law-review skill
```

### 6.5 SPC Guiding Case araması (sözleşme uyuşmazlığı)

```
ADIM 1: WebFetch: court.gov.cn/shenpan.html
  → "指导性案例" listesinden sözleşme/ticaret olanları seç

ADIM 2: İlgili Guiding Case'i oku, [Müvekkil] davasıyla bağlantısını değerlendir

ADIM 3: Atıf ekle → [CN Yargı — court.gov.cn/SPC — 指导性案例 {numara} — yıl]
```

---

## 7. Atıf disiplini

Bu rehberdeki kaynaklardan alınan atıflar **mutlaka** etiketli olmalı:

- `[CN Mevzuat — HuggingFace/twang2218 — {kanun adı} — GG.AA.YYYY]` — HF API'dan çekilen mevzuat
- `[CN Mevzuat — flk.npc.gov.cn — {kanun adı}]` — crawler ile doğrudan alınan (nadir)
- `[CN Yargı — CAIL{yıl} — {dava özeti} — yıl]` — CAIL offline veri (araştırma amaçlı)
- `[CN Yargı — court.gov.cn/SPC — 指导性案例 {numara} — yıl]` — SPC Guiding Case
- `[CN Yargı — court.gov.cn/SPC — 司法解释 — {kısa başlık} — yıl]` — SPC yargı yorumu

**Asla:** API'dan çekilmediğin Çin hukuku kaynağına atıf koyma.
Çin hukukunu "biliyorum" diye `[CN Mevzuat]` etiketiyle gösterme → `[model bilgisi — doğrulayın]` kullan.

**⚠️ Dil uyarısı:** Tüm Çin mevzuatı Çincedir. Her atıfta Çince başlığı + Türkçe çevirisini birlikte sun:
- `中华人民共和国公司法` → "Şirketler Kanunu"
- `中华人民共和国民法典 — 合同编` → "Medeni Kanun — Sözleşme Kitabı"

---

## 8. Sınırlamalar

- **Yalnızca Çince:** İngilizce çeviri yok. Çeviri modele kalır; kritik hukuki metinlerde
  `[review]` + uzman hukuk çevirisi önerisi ekle.
- **Güncellik:** HF dataset 2024 itibarıyla güncelleme aldı; en yeni değişiklikler için
  flk.npc.gov.cn'de elle teyit önerilir.
- **wenshu erişim kısıtlı:** wenshu.court.gov.cn 2024'ten login zorunlu. Guiding Cases
  (279 adet) ve yargı yorumları için court.gov.cn/shenpan.html ücretsiz kullanılabilir;
  daha geniş içtihat araması için PKULaw (ücretli abonelik) gereklidir.
- **Yargı yorumu kısmı:** 司法解释 HF dataset'te kısmi kapsam — `司法解释` filtresiyle
  ne kadar kapsandığını kontrol et; eksikse court.gov.cn ile tamamla.
- **Yerel mevzuat sınırlı:** Eyalet/şehir düzeyindeki yerel yönetmelikler HF'te sınırlı kapsam.
- **Karşı Yaptırım Kanunu çelişkisi:** 反外国制裁法 (2021) ABD/AB yaptırım uyumunu
  zorlaştırabilir — her iki tarafın yükümlülük çakışmasını `[review]` ile flagle.
- **wb.flk.npc.gov.cn:** SSL sertifikası süresi dolmuş (08.06.2026 itibarıyla) — bu endpoint'e WebFetch yapma.
- **CAIL verileri ceza hukuku ağırlıklı:** Ticari/sözleşme uyuşmazlığı içtihadı için
  PKULaw (ücretli abonelik) gereklidir.

---

## 9. [Müvekkil] Çin hukuku kullanım disiplini

1. **Çin governing-law sözleşmesi** → HF API'dan 民法典 (Medeni Kanun) + ilgili 法律'yi getir.
   Türk hukuku seçilmişse → Çin hukuku analizi karşılaştırmalı arka plan; Türk analizi önce.

2. **Çin karşı tarafıyla enerji tedarik** → OpenSanctions + 反外国制裁法 + 外商投资法 +
   enerji sektörü mevzuatı (能源法, 石油 düzenlemeleri) birlikte.

3. **PIPL uyumu** → 个人信息保护法 madde 38-43 (yurt dışı transfer şartları). Hem Çin hem
   KVKK zorunlulukları aynı anda değerlendirilmeli.

4. **Tahkim klozu — Çin seated** → CIETAC tahkimi çoğunlukla; 仲裁法 geçerlilik +
   NY Konvansiyonu tenfiz analizi.

5. **İçtihat araştırması** → court.gov.cn/shenpan.html (ücretsiz, Guiding Cases 279+);
   daha derin arama için PKULaw veya benzeri ticari abonelik gereklidir.

6. **Dil notu:** [Müvekkil]'ın Çin karşı taraflarıyla yazışması genellikle İngilizce.
   Çin mevzuat alıntısı kullanılıyorsa → Çince orijinal + EN/TR çeviri birlikte.

---

## 10. HuggingFace API hızlı referans

| İşlem | URL şablonu |
|-------|-------------|
| Başlık arama | `…/filter?…&where="title" LIKE '%TERIM%'` |
| Tam başlık | `…/filter?…&where="title" = 'TAM_AD'` |
| Yürürlükte filtrele | `…&where="status" = '有效'` |
| Tür filtrele | `…&where="type" = '法律'` |
| Birden fazla koşul | `…&where="type" = '法律' AND "status" = '有效'` |
| Sayfalı liste | `…/rows?…&offset=0&limit=10` |
| Base URL | `https://datasets-server.huggingface.co` |
| Dataset adı (encoded) | `twang2218%2Fchinese-law-and-regulations` |
| Config | `default` |
| Split | `train` |

---

## 11. Ek GitHub Kaynakları (araştırma / NLP)

| Repo | Yıldız | Kapsam | Kullanım |
|------|--------|--------|----------|
| [cncases/cases](https://github.com/cncases/cases) | 1.000 | 85M+ mahkeme belgesi, Rust tabanlı yerel arama | Offline büyük ölçekli analiz |
| [myx666/LeCaRD](https://github.com/myx666/LeCaRD) | 166 | 107 sorgu, 10.700 aday dava, SPC ceza kararları | Ceza davası benzerlik araştırması |
| [THUIR/LeCaRDv2](https://github.com/THUIR/LeCaRDv2) | 89 | 800 sorgu, 55K aday dava | Genişletilmiş LeCaRD |
| [CSHaitao/Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources) | 303 | Küratöre edilmiş Çin hukuki AI kaynakları | Yeni dataset/araç keşfi |

---

## Versiyon disiplini

- Bu rehber **v1.8.2** (*Çin Hukuku Entegrasyonu*) ile eklendi.
- **08.06.2026 güncellemesi:** court.gov.cn (SPC Guiding Cases), CAIL2019–2024 serisi
  ve ek GitHub kaynakları eklendi. Erişim testleri bu tarihte gerçekleştirildi.
- HuggingFace `/filter` ve `/rows` endpoint'leri çalışıyor (08.06.2026 test ✅).
- `wb.flk.npc.gov.cn` SSL sertifikası süresi dolmuş — bu alt domain'e WebFetch yapma.

---

*Son güncelleme: 08.06.2026 — court.gov.cn + CAIL serisi (2018–2024) eklendi. 5 kaynak, 3 erişim yöntemi.*
