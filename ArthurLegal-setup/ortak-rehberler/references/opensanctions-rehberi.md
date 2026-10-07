# OpenSanctions API – Kullanım Rehberi (ortam değişkeni + curl)

> **Custom MCP server YOK** — OpenSanctions yalnız REST API. Bu rehber, Claude Code'da kabuk komutuyla (`curl`) OpenSanctions'ı çağırma prosedürünü tanımlar.
>
> **Durum:** API anahtarı **pakette yoktur**; `OPENSANCTIONS_API_KEY` ortam değişkeninden okunur. Anahtarı hiçbir çıktıya,
> nota, dosyaya veya sohbete yazma. Önceki sürümde pakete gömülü olan anahtar public depoda yayımlandığı için
> iptal edilip yenilenmelidir (24.09.2026).

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

## {{AL_KURUM}} için neden kritik?

{{AL_KURUM}}'ın commercial-legal'da "the thing that hurts" olarak işaretlenen yaptırım taraması, 6 farklı rejimi tek tek tarama gerektiriyordu. OpenSanctions **tek API çağrısı ile 70+ liste** veriyor.

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
Authorization: ApiKey $OPENSANCTIONS_API_KEY
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

**Cevap:** Her sorgu için en yakın eşleşmeler. `score` 0 ile 1 arasındadır; `match: true`, skor eşiğe (varsayılan 0,7) ulaşınca döner (OpenSanctions dokümanı, 24.09.2026). Skor ≥ 0,70 → manuel inceleme; ≥ 0,90 → blok.

### 2. Search API — basit metin araması
**GET `/search/{scope}?q={isim}`**

```bash
GET https://api.opensanctions.org/search/default?q=Acme+Trading+LLC
Authorization: ApiKey $OPENSANCTIONS_API_KEY
```

### 3. Entities API — bilinen ID ile detay çekme
**GET `/entities/{entity_id}`**

```bash
GET https://api.opensanctions.org/entities/Q123456
Authorization: ApiKey $OPENSANCTIONS_API_KEY
```

### Scope seçimi

- `default` — tüm listeler (yaptırım + PEP + soruşturma)
- `sanctions` — sadece yaptırım listeleri
- `peps` — sadece PEP listesi

{{AL_KURUM}} için: **commercial vendor screening → `default` veya `sanctions`**, PEP'ler counterparty UBO incelemesinde alttan kontrol.

---

## API key prosedürü ({{AL_KURUM}} için)

**Adım 1:** https://www.opensanctions.org/api/ → Sign up

**Adım 2:** İletişim bilgileri + kullanım amacı (commercial screening for {{AL_KURUM}}) → ticari ekiple lisans görüşmesi

**Adım 3:** Pay-as-you-go veya volume paketi:
- 20.000 istek/ay başlangıç paketi
- Aylık abonelik + aşımda ek bedel
- Yıllık taahhüt indirim

**Adım 4:** API anahtarını `OPENSANCTIONS_API_KEY` ortam değişkenine koy (Claude Code: `~/.claude/settings.json` içindeki `env` bloğu ya da işletim sisteminin ortam değişkeni). Anahtar pakete, depoya, bu rehbere veya sohbete yazılmaz.

> **Not (24.09.2026):** Önceki sürümde anahtar bu rehbere gömülüydü ve paket public depoda yayımlandı. Yayımlanmış
> anahtarı herkes kullanabilir; iptal ettirilip yenisi alınır. Git geçmişi eski metni saklamaya devam eder;
> anahtarı dosyadan silmek tek başına yetmez.

---

## Claude'da kullanım — kabuk (curl) kalıbı

Claude Code'da, Bash aracı varken:

```bash
curl -s -X POST "https://api.opensanctions.org/match/default" \
  -H "Authorization: ApiKey $OPENSANCTIONS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"queries":{"q1":{"schema":"Company","properties":{"name":["Acme Trading LLC"],"country":["RU"]}}}}'
```

Kurallar:

1. Anahtar komuta yalnız `$OPENSANCTIONS_API_KEY` olarak girer. Değeri komuta, çıktıya, nota veya sohbete yazma;
   `echo $OPENSANCTIONS_API_KEY` çalıştırma.
2. Değişken tanımlı değilse (`[ -n "$OPENSANCTIONS_API_KEY" ]` yanlışsa) API çağrısı yapma; aşağıdaki
   "Yedek manuel kaynaklar"a geç.
3. Sorguya yalnız tarama için gereken alanlar girer (ad, ülke, doğum yılı, sicil no). Dosya ayrıntısı gönderilmez.
4. Yanıttaki `score` 0 ile 1 arasındadır; `match: true`, skor eşiğe (varsayılan 0,7) ulaşınca döner.
5. Skora göre karar: 0,90+ → 🔴 DURDUR, eskalasyon; 0,70-0,90 → 🟠 manuel inceleme, KYC + UBO doğrulama;
   0,70 altı → 🟢 devam, kaydet.
6. Çıktıda: "[OpenSanctions API — match skoru X, GG.AA.YYYY]" etiketli atıf.

Hata yanıtları (24.09.2026'da denendi): anahtar yoksa `401 {"detail":"No API key provided."}`, geçersiz anahtarda
`401 {"detail":"Invalid API key"}`.

`WebFetch` aracı POST isteği ve `Authorization` başlığı gönderemez; bu yüzden OpenSanctions API'si için kullanılmaz.
claude.ai web arayüzünde kabuk ve ortam değişkeni yoktur; orada "Yedek manuel kaynaklar" tablosunu kullan.

**Pratik:** Bu prosedürü `yaptirim-tarama-rehberi.md` ile birleştir — orada **Adım 2** (liste eşleşme taraması) yerine OpenSanctions tek çağrı.

---

## Match skoru kalibrasyon

OpenSanctions match skoru 0 ile 1 arasındadır. Genel kalibrasyon önerisi:

| Skor | Anlam | {{AL_KURUM}} aksiyon |
|---|---|---|
| 0,95-1,00 | Kesin eşleşme | 🔴 Durdur. Hukuk Başkanı + Compliance + CEO. |
| 0,80-0,95 | Yüksek olasılık | 🔴 Durdur, manuel UBO + KYC doğrula. Birkaç gün sürebilir. |
| 0,60-0,80 | Orta olasılık (fuzzy ad) | 🟠 İlave dilijans: kimlik teyit, ülke teyit, alternative isimler tara. |
| 0,40-0,60 | Düşük olasılık | 🟡 Kayıt al, ek dilijans gerekmez ama veri tabanında işaretle. |
| < 0,40 | Eşleşme yok | 🟢 Devam, kaydet. |

**Önemli:** Eşik değerleri **counterparty'nin coğrafyasına göre** sıkılaştırılmalı. Rusya/İran/Kuzey Kore origin'li ise eşik 0,20 düşürülmeli (false-negative maliyeti yüksek).

---

## Sınırlamalar

- **Lisans aktif** — {{AL_KURUM}} ticari abonelik (13.05.2026'dan itibaren). Kullanım kotası ve aşım takibi OpenSanctions panelinden izlenir.
- **Veri günlük güncellenir** — gece batch; bir günlük gecikme normal.
- **Türk MASAK listesi gözüksə də zayıf kapsama** — TR rejimine özel kararlar için MASAK web sayfasına ek bakış. ArthurLegal MCP (`tr_`)'den de KVKK Kurulu veri ihlali kararları taranabilir.
- **Çince/Arapça/Kiril yazımlarda fuzzy match daha zayıf** — original yazımı + Latin translit ikisi de gönder.
- **PEP listesi siyasi içerikli** — yanlış pozitiflere dikkat (örn. eski bakanlar, milletvekilleri).

---

## Yedek manuel kaynaklar (API kesintisi / kota aşımı durumunda)

OpenSanctions API erişilemezse (servis kesintisi, kota aşımı, ağ engeli), manuel taraması yap:

| Kaynak | URL | Tip |
|---|---|---|
| OpenSanctions web araması | https://www.opensanctions.org/search/ | Manuel arama (anahtar gerekmez; claude.ai web arayüzünde tek yol) |
| OFAC SDN Search | https://sanctionssearch.ofac.treas.gov/ | Manuel arama |
| EU Sanctions Map | https://www.sanctionsmap.eu/ | Manuel + XML feed |
| UK OFSI Search | https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets | Manuel |
| BM Consolidated List | https://www.un.org/securitycouncil/content/un-sc-consolidated-list | Manuel + XML |
| MASAK (TR donan varlık) | https://www.masak.hmb.gov.tr | Manuel |
| **ArthurLegal MCP (`tr_`) — KVKK Kurulu** | (MCP) | TR enforcement actions |

Detay: `yaptirim-tarama-rehberi.md` Adım 2.

---

## Versiyon disiplini

- **OpenSanctions API sürümü:** semver `v3` (Mayıs 2026 itibariyle)
- **Endpoint stabilitesi:** API breaking change duyurusu 6 ay öncesinden
- **Kalibrasyon yıllık:** match skoru eşikleri {{AL_KURUM}} risk komitesi tarafından yıllık gözden geçirilmeli

---

*Son güncelleme: 24.09.2026 — anahtar paketten çıkarıldı, `OPENSANCTIONS_API_KEY` ortam değişkenine taşındı; kullanım kalıbı curl; skor ölçeği 0-1.*
