# Atıf — ArthurLegal Claude Corporate Assistant v1.4.0

## Yapı

| Rol | Kim |
|---|---|
| **Author** (kod & içerik üretimi) | Claude (Anthropic) |
| **Knowledge base** (temel hukuk asistanı paketi) | Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0) |

## Türk Mevzuat & Yargı entegrasyonu

Bu paketin Türk mevzuat + yargı entegrasyonu, [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan açık MCP sunucusunu kullanır:

- **TR Legal MCP (yargi-mcp-pro)** — `yargi-mcp-pro-production.up.railway.app/mcp`
  - Mevzuat: mevzuat.gov.tr + bedesten.adalet.gov.tr norm metinleri
  - Yargı: Yargıtay, Danıştay, AYM + 12 diğer kurum kararları
  - Auth: OAuth 2.0 (WorkOS) — claude.ai bağlantıyı yönetir

- **OpenCaseLaw.ch MCP** — `mcp.opencaselaw.ch/sse`
  - İsviçre 972K+ karar, Fedlex mevzuatı (CC0, auth yok)

## Kaynak katmanı MCP sunucuları (v1.4.0 — self-hosted, auth yok)

Üçü de bağımlılıksız (yalnız Python stdlib) MCP sunucusudur; public upstream
API'leri sarar. Kaynakları:
[`eqanun-api`](https://github.com/beerbottle90/eqanun-api) ·
[`lex-scholar-api`](https://github.com/beerbottle90/lex-scholar-api) ·
[`resourcecontracts-api`](https://github.com/beerbottle90/resourcecontracts-api)
(umbrella: [`socar-api-s`](https://github.com/beerbottle90/socar-api-s)).

- **e-qanun MCP** — upstream `api.e-qanun.az`, Azerbaycan Cumhuriyeti **Adalet
  Bakanlığı** (Ədliyyə Nazirliyi) resmî mevzuat veritabanı. Hükümet portalı,
  kamu erişimine açık.

- **LexScholar MCP** — on açık erişim indeksini federe eder. Her upstream kendi
  lisansına tabidir ve **yükümlülükler veriyle birlikte taşınır**:

  | İndeks | İşletmeci | Lisans / kısıt |
  |---|---|---|
  | **DOAJ** | DOAJ (Infrastructure Services for Open Access) | Metadata **CC0**; `robots.txt` **`ai-train=no`** → getir-ve-atıf-ver uyumlu, **model eğitimi hayır** |
  | **DergiPark** | **TÜBİTAK ULAKBİM** | Resmî **OAI-PMH** ucu (`dergipark.org.tr/api/public/oai/`); sitenin `/search` yolu `robots.txt` ile kapalıdır ve **kazınmaz** |
  | **SciELO** | SciELO / FAPESP | Açık erişim, koleksiyon bazlı |
  | **HAL** | CCSD (CNRS, Fransa) | Açık arşiv |
  | **Dialnet** | Universidad de La Rioja | `dc:rights`: çoğaltma için **açık yazılı izin** şart → **yalnız keşif/atıf** |
  | **OpenAIRE** | OpenAIRE AMKE (AB) | Açık metadata |
  | **Law Review Commons** | bepress / Elsevier | `robots.txt` `/do/` yolunu kapatır; içerik **öğrenci editörlü** (hakemli değil) |
  | **OpenAlex** | OurResearch | CC0; anonim kullanım **ölçülü** (~100 arama/gün) |
  | **Crossref** | Crossref | Metadata açık |
  | **Unpaywall** | OurResearch | Açık erişim çözücü |

- **ResourceContracts MCP** — upstream `api.resourcecontracts.org`.
  İçerik **CC BY-SA 4.0**, **Natural Resource Governance Institute (NRGI)** ve
  **Columbia Center on Sustainable Investment (CCSI)** tarafından; Dünya Bankası,
  OpenOil ve ALSF katkısıyla. **Atıf + share-alike zorunludur** — alıntılanan
  sözleşme metni ve kloz anotasyonlarında korunur. Kardeş veritabanı:
  `api.openlandcontracts.org`.

> Bu paket bu kaynakları **getirir ve atıf verir**; hiçbirinin içeriğini yeniden
> yayımlamaz veya model eğitiminde kullanmaz. Sunucular kullanıcı tarafından
> self-host edilir; paket yalnız kullanım prosedürünü tanımlar.

## Üçüncü-taraf veri kaynakları

- **OpenSanctions API** (`api.opensanctions.org`) — paid membership; kullanıcı kendi API key'ini temin eder.
- **KAP** (`kap.org.tr`) — public özel durum açıklamaları (WebFetch).
- **e-ŞİRKET** (`e-sirket.mkk.com.tr`) — public sermaye yapısı bilgileri (WebFetch).
- WebFetch kaynaklar (auth gerektirmez): legislation.gov.uk · GovInfo · CourtListener · EUR-Lex · HUDOC · gesetze-im-internet.de · Légifrance · Normattiva · e-Gov JP · Fedlex · pravo.gov.ru · constcourt.gov.az · minenergy.gov.az · CODICES (Venice Commission) · NATLEX (ILO) · HuggingFace/twang2218 · paragraf.rs

## Lisans

Bu paket **bir bütün olarak** ArthurLegal Proprietary Non-Commercial License
kapsamındadır — bkz. [LICENSE](LICENSE). **Ticari kullanım yasaktır.** In-house
counsel'ın, hukuk bürosu çalışanının ve gerçek kişinin kişisel kullanımı ile bu
kullanımlar için bizzat yapılan veya üçüncü kişiye yaptırılan geliştirmeler
ticari kullanım sayılmaz. Tüm hakları saklıdır.

Paketin türetildiği üçüncü taraf bilgi tabanı (Anthropic `claude-for-legal`)
**Apache License 2.0** altındadır. İlgili lisans ve atıf bildirimi
[LICENSE-APACHE-2.0-THIRD-PARTY.txt](LICENSE-APACHE-2.0-THIRD-PARTY.txt)
dosyasında korunmuştur ve kaldırılamaz. Çelişki hâlinde, o bileşenler bakımından
Apache 2.0 geçerlidir.

## Kişisel veri uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket verisi içermez**. `knowledge/company-profile.md` tamamen `[DOLDUR]` yer-tutucularından oluşan bir şablondur.

Paketi kendi kurumunuza uyarladığınızda doldurduğunuz gerçek veriler **sizin kontrolünüzdedir** — public repoya commit etmeden önce gözden geçirin.
