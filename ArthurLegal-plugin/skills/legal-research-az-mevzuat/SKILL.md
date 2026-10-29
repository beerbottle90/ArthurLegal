---
name: legal-research-az-mevzuat
description: >
  Azerbaycan mevzuati arastirmasi - e-qanun MCP (resmi api.e-qanun.az, Adalet
  Bakanligi). BIRINCIL kaynak. Akt arar, yururluk statusunu (Quvvededir /
  Legv olunmus) dogrular, madde metnini okur. Yalniz mevzuat; AZ ictihadi
  bu araclarda yok.
user-invocable: true
---

# Azerbaycan Mevzuatı Araştırması (e-qanun MCP)

## Ne zaman kullanılır

- Herhangi bir Azerbaycan hukuku sorusu: medeni, vergi, iş, enerji, yer altı
  serveti, gümrük, rekabet.
- **Tipik tetikleyiciler (müvekkil işleri):** Azerbaycanlı karşı tarafla
  intra-group veya ticari işlemler (ham petrol tedarik, royalty, transfer
  fiyatlandırması, JV), Azerbaycan'da istihdam edilen personel için iş hukuku,
  ortak girişim yapısı, Türk müvekkil ile Azerbaycanlı taraf arasındaki
  sözleşmelerde uygulanacak hukuk seçimi.
- Kullanıcının (veya bir belgenin) dayandığı bir aktın **hâlâ yürürlükte
  olduğunu doğrulamak.**
- Taslak veya görüş öncesi bir maddenin **gerçek lafzını okumak.**

## Ne zaman kullanılmaz

- **AZ içtihadı** → Anayasa Mahkemesi kararları bu API'de **YOK**.
  `azerbaycan-hukuk-rehberi.md` (constcourt.gov.az, CODICES).
- TR mevzuat / içtihat → ArthurLegal MCP (`tr_`).
- AZ hukuku üzerine akademik şerh → `/arthurlegal:legal-research-karsilastirmali-doktrin`
  (İKİNCİL — aktın kendisinin yerine **asla** geçmez).
- İmzalı sözleşme emsali (PSA/JOA şartları) → `/arthurlegal:legal-research-sozlesme-emsali`.
- Yaptırım / taraf taraması → OpenSanctions.

## Araçlar (6)

| Araç | Ne yapar |
|---|---|
| `az_search_acts(query, scope, status, exact, start, length)` | `scope=title` başlıkta, `scope=text` tam metinde (geniş, yavaş); `status` = `in_force` / `cancelled` / `all` |
| `az_count_acts(...)` | Yalnız sayı — konuyu ucuza boyutla |
| `az_get_act(act_id)` | Künye, kabul/yürürlük tarihleri, tür, **STATÜ**, `htmlUrl` |
| `az_get_act_fulltext(act_id, offset, max_chars)` | Temiz metin, karakterle sayfalanır |
| `az_list_types()` / `az_list_sections()` | Akt türü taksonomisi, üst düzey bölümler |

## Yöntem — statü doğrulaması opsiyonel DEĞİL

1. `az_search_acts(query, scope="title", status="in_force")` ile ara. Başlık araması
   zayıf dönerse `scope="text"`e genişlet.
2. Dönen `id` ile **`az_get_act(id)`** çağır ve `statusName` oku:
   - **`Qüvvədədir`** → yürürlükte.
   - **`Ləğv olunmuş`** → **yürürlükten kalkmış — DAYANAK YAPMA.** Ardıl aktı ara.
   - Yürürlük tarihini de kontrol et: bir akt yürürlükte olup **henüz
     uygulanabilir olmayabilir**.
3. Ancak bundan sonra `az_get_act_fulltext(id)`. Mecelleler büyüktür (Mülki Məcəllə
   ~1,96M karakter) → `offset` ile sayfala, hepsini birden çekme.
4. **Fiilen okuduğun maddeyi alıntıla.** Başlıktan parafraz yapma.

> **Bu skill'in var olma sebebi tek bir hatadır: yürürlükten kalkmış bir aktı
> yürürlükteymiş gibi göstermek.** `az_search_acts` bunu sana söyleyemez; yalnız
> `az_get_act` söyler.

## Dil

Külliyat Azerbaycancadır. **Azerbaycanca terimle ara:** `neft` (petrol), `qaz`
(gaz), `əmək` (iş), `vergi`, `mülki` (medeni), `torpaq` (arazi), `yerin təki`
(yer altı serveti), `antiinhisar` (rekabet), `mühasibat` (muhasebe), `gömrük`
(gümrük). Türkçe veya İngilizce sorgu eksik rapor eder. Diakritiksiz Türkçe
klavye girişi genellikle eşleşir (`emek` → `Əmək`) ama gerçek terimi tercih et.

## Grounding ve sınırlar

- Aracın döndürmediği bir AZ kuralını **söyleme** → `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>`.
- **`Ləğv olunmuş` bir aktı asla güncel hukuk gibi sunma**; statüyü **asla
  atlama**.
- Azerbaycanca metni Türkçe çevirisiyle birlikte ver; çevirinin **sana ait,
  resmî olmadığını** işaretle. Kritik metinde `[review]`.
- **Kapsam dürüstlüğü:** cevap gerçekte mahkemelerin uygulamasına dayanıyorsa
  "içtihat kontrol edilmedi" de ve Anayasa Mahkemesi yollarına işaret et.
- MCP erişilemezse `azerbaycan-hukuk-rehberi.md` WebFetch yedeğine düş — ama o
  yolda **statü doğrulanmamıştır**, bunu yaz.
- Bu araca müvekkil bilgisi, dosya özeti veya gizli taslak **gönderme**
  (Av. K. m. 36).
- Çıktı avukat incelemesi öncesi **taslaktır**.

## Atıf

```
[AZ Mevzuat — e-qanun MCP — {belge adı} — id:{id} — {statü} — GG.AA.YYYY]
```

Statü **atıfın içindedir** — okuyucu yeniden kontrol etmeden görebilmeli.

## Çıktı

- **Konu**
- **Kısa Cevap**
- **Dayanak** — akt adı, id, **statü**, yürürlük tarihi, ilgili madde
- **Analiz**
- **Riskler** (🔴🟠🟡🟢)
- **Kapsam Notu** — mevzuat kontrol edildi; içtihat kontrol edilmediyse belirt
- **Kaynaklar**
- **⚠️ İnceleyen notu** — nitelikli avukat incelemesi için taslak
- **Sıradaki adımlar** (3-5 seçenek)

## Entegrasyon

- Rehber: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md`; içtihat/EN kaynaklar için
  `${CLAUDE_PLUGIN_ROOT}/references/azerbaycan-hukuk-rehberi.md`.
- Besleyen skill'ler: `commercial-legal:governing-law-review`,
  `corporate-legal` (JV yapısı), `energy-finance:jv-agreement-review`,
  `tax-legal:transfer-pricing-review`, `employment-legal` (AZ personel),
  `advocacy-legal` (dilekçe dayanağı), `firm-operations:new-client-intake`.
- Karşılaştırmalı şerh: `/arthurlegal:legal-research-karsilastirmali-doktrin` (İKİNCİL).
