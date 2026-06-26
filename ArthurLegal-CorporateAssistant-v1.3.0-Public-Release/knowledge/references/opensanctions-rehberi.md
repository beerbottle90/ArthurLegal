# OpenSanctions API – Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK** — OpenSanctions sadece REST API. Bu rehber, Claude'un `WebFetch` aracını OpenSanctions ile birlikte kullanmak için prosedürü tanımlar.
>
> **Durum:** ✅ Lisans + API key aktif (13.05.2026 itibariyle). API key güvenli env değişkeninde tutulur; bu rehberdeki çağrılar canlı çalışır.

---

## OpenSanctions nedir?

**OpenSanctions** = global yaptırım + PEP (Politically Exposed Persons) listelerini tek API'de birleştirir.

**Kapsam:**
- OFAC (ABD) — SDN List + Sectoral Sanctions
- AB Consolidated Financial Sanctions List + 269/2014 + 833/2014
- UK OFSI Consolidated List
- BM Güvenlik Konseyi
- 70+ ulusal yaptırım listesi
- Politically Exposed Persons (PEP)
- Soruşturma altındaki kişiler (örn. Interpol Red Notice)
- Şirket ticari yasak listeleri

**Veri formatı:** [FollowTheMoney](https://followthemoney.tech/) ontolojisi.

---

## [ŞİRKET ADI] için neden kritik?

[ŞİRKET ADI]'ın commercial-legal'da "the thing that hurts" olarak işaretlenen yaptırım taraması, 6 farklı rejimi tek tek tarama gerektiriyordu. OpenSanctions **tek API çağrısı ile 70+ liste** veriyor.

Pratik akış kısalır:
- **Önce:** Counterparty'yi OFAC + AB + UK + BM + TR 7262 + ek kurumsal listelerde ayrı ayrı tara (6 kontrol)
- **Sonra:** OpenSanctions Matching API'ye 1 çağrı; tüm listelerden eşleşme + skor + kaynak listele

---

## Endpoint'ler

### Base URL
```
https://api.opensanctions.org
```

### 1. Matching API — birincil kullanım
**POST `/match/{scope}`**

Counterparty bilgisini gönder, eşleşme skoru + bağlantılı varlık döndür.

```bash
POST https://api.opensanctions.org/match/default
Authorization: Apikey a1c019122d0de8880772f7282c0ae03d
Content-Type: application/json

{
  "queries": {
    "vendor-screen-001": {
      "schema": "Company",
      "properties": {
        "name": ["Acme Trading LLC"],
        "country": ["RU"],
        "registrationNumber": ["1234567890"]
      }
    }
  }
}
```

**Cevap:** Her query için en yakın eşleşmeler + match skoru (0-100). Skor ≥ 70 → manuel inceleme; ≥ 90 → blok.

### 2. Search API — basit metin araması
**GET `/search/{scope}?q={isim}`**

```bash
GET https://api.opensanctions.org/search/default?q=Acme+Trading+LLC
Authorization: Apikey a1c019122d0de8880772f7282c0ae03d
```

### 3. Entities API — bilinen ID ile detay çekme
**GET `/entities/{entity_id}`**

```bash
GET https://api.opensanctions.org/entities/Q123456
Authorization: Apikey a1c019122d0de8880772f7282c0ae03d
```

### Scope seçimi

- `default` — tüm listeler (yaptırım + PEP + soruşturma)
- `sanctions` — sadece yaptırım listeleri
- `peps` — sadece PEP listesi

[ŞİRKET ADI] için: **commercial vendor screening → `default` veya `sanctions`**, PEP'ler counterparty UBO incelemesinde alttan kontrol.

---

## API key prosedürü ([ŞİRKET ADI] için)

**Adım 1:** https://www.opensanctions.org/api/ → Sign up

**Adım 2:** İletişim bilgileri + kullanım amacı (commercial screening for [ŞİRKET ADI]) → ticari ekiple lisans görüşmesi

**Adım 3:** Pay-as-you-go veya volume paketi:
- 20.000 istek/ay başlangıç paketi
- Aylık abonelik + aşımda ek bedel
- Yıllık taahhüt indirim

**Adım 4:** API key alındı → güvenli ortam değişkenine kaydedilir:
- Claude Code: `~/.claude/settings.local.json` env section
- Veya OS env var: `OPENSANCTIONS_API_KEY`

**⚠️ Asla:** API key'i CLAUDE.md veya SYSTEM_PROMPT.md gibi paylaşılan dosyalara yazma.

---

## Claude'da kullanım — WebFetch pattern

API key'in olduğunu varsayalım. Claude WebFetch ile çağırma:

```
Claude (sen) sorgu yapıyorsun:

1. Counterparty bilgisini topla (ad, ülke, vergi no, UBO isimleri).
2. WebFetch çağrısı:
   - URL: https://api.opensanctions.org/match/default
   - Method: POST
   - Headers: Authorization: Apikey {API_KEY_FROM_ENV}, Content-Type: application/json
   - Body: { "queries": { "q1": { "schema": "Company", "properties": {...}}}}
3. Cevap JSON'ı parse et — match skoru ve eşleşen liste(ler)
4. Skora göre karar:
   - 90+ → 🔴 DURDUR, eskalasyon
   - 70-90 → 🟠 manuel inceleme, KYC + UBO doğrulama
   - <70 → 🟢 devam, kaydet
5. Çıktıda: "[OpenSanctions API — match scoru X, GG.AA.YYYY]" etiketli atıf
```

**Pratik:** Bu prosedürü `socar-yaptirim-tarama-rehberi.md` ile birleştir — orada **Adım 2** (liste eşleşme taraması) yerine OpenSanctions tek çağrı.

---

## Match skoru kalibrasyon

OpenSanctions match skoru 0-100. Genel kalibrasyon önerisi:

| Skor | Anlam | [ŞİRKET ADI] aksiyon |
|---|---|---|
| 95-100 | Kesin eşleşme | 🔴 Durdur. Hukuk Başkanı + Compliance + CEO. |
| 80-95 | Yüksek olasılık | 🔴 Durdur, manuel UBO + KYC doğrula. Birkaç gün sürebilir. |
| 60-80 | Orta olasılık (fuzzy ad) | 🟠 İlave dilijans: kimlik teyit, ülke teyit, alternative isimler tara. |
| 40-60 | Düşük olasılık | 🟡 Kayıt al, ek dilijans gerekmez ama veri tabanında işaretle. |
| <40 | Eşleşme yok | 🟢 Devam, kaydet. |

**Önemli:** Eşik değerleri **counterparty'nin coğrafyasına göre** sıkılaştırılmalı. Rusya/İran/Kuzey Kore origin'li ise eşik 20 puan düşürülmeli (false-negative maliyeti yüksek).

---

## Sınırlamalar

- **Lisans aktif** — [ŞİRKET ADI] ticari abonelik (13.05.2026'dan itibaren). Kullanım kotası ve aşım takibi OpenSanctions panelinden izlenir.
- **Veri günlük güncellenir** — gece batch; bir günlük gecikme normal.
- **Türk MASAK listesi gözüksə də zayıf kapsama** — TR rejimine özel kararlar için MASAK web sayfasına ek bakış. Yarg MCP'den de KVKK Kurulu veri ihlali kararları taranabilir.
- **Çince/Arapça/Kiril yazımlarda fuzzy match daha zayıf** — original yazımı + Latin translit ikisi de gönder.
- **PEP listesi siyasi içerikli** — yanlış pozitiflere dikkat (örn. eski bakanlar, milletvekilleri).

---

## Yedek manuel kaynaklar (API kesintisi / kota aşımı durumunda)

OpenSanctions API erişilemezse (servis kesintisi, kota aşımı, ağ engeli), manuel taraması yap:

| Kaynak | URL | Tip |
|---|---|---|
| OFAC SDN Search | https://sanctionssearch.ofac.treas.gov/ | Manuel arama |
| EU Sanctions Map | https://www.sanctionsmap.eu/ | Manuel + XML feed |
| UK OFSI Search | https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets | Manuel |
| BM Consolidated List | https://www.un.org/securitycouncil/content/un-sc-consolidated-list | Manuel + XML |
| MASAK (TR donan varlık) | https://www.masak.hmb.gov.tr | Manuel |
| **Yarg MCP — KVKK Kurulu** | (MCP) | TR enforcement actions |

Detay: `socar-yaptirim-tarama-rehberi.md` Adım 2.

---

## Versiyon disiplini

- **OpenSanctions API sürümü:** semver `v3` (Mayıs 2026 itibariyle)
- **Endpoint stabilitesi:** API breaking change duyurusu 6 ay öncesinden
- **Kalibrasyon yıllık:** match skoru eşikleri [ŞİRKET ADI] risk komitesi tarafından yıllık gözden geçirilmeli

---

*Son güncelleme: 13.05.2026 — OpenSanctions REST API entegrasyon prosedürü; lisans aktif, canlı kullanımda.*
