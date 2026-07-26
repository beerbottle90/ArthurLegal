# Atıf — ArthurLegal Claude Law Firm Assistant v1.4.0

## Yapı

| Rol | Kim |
|---|---|
| **Author** (kod & içerik üretimi) | Claude (Anthropic) — Opus 4.7 (`claude-opus-4-7`) |
| **Designer** (proje tasarımı & domain bilgisi) | Ertuğ Demir |
| **Knowledge base** (temel hukuk asistanı paketi) | Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0) |
| **Kardeş paket** | ArthurLegal Claude Corporate Assistant v1.4.0 (in-house tarafı; aynı metodoloji) |

## Türk Mevzuat & Yargı entegrasyonu

Bu paketin Türk mevzuat (Mevzuat MCP) ve Türk yargı (Yargı MCP) entegrasyonu, [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan açık MCP sunucularını kullanır:

- `mevzuat.surucu.dev/mcp` — Türk mevzuatı norm metinleri (mevzuat.gov.tr + bedesten.adalet.gov.tr)
- `yargimcp.surucu.dev/mcp` — Türk yargı/idari kararlar (Yargıtay, Danıştay, AYM + 12 diğer kurum)

Her iki sunucu da public, auth gerektirmez.

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
  OpenOil ve ALSF katkısıyla. **Atıf + share-alike zorunludur.** Kardeş
  veritabanı: `api.openlandcontracts.org`.

> Bu paket bu kaynakları **getirir ve atıf verir**; hiçbirinin içeriğini yeniden
> yayımlamaz veya model eğitiminde kullanmaz. Sunucular kullanıcı tarafından
> self-host edilir; paket yalnız kullanım prosedürünü tanımlar.
>
> ⚠️ **Av. K. m. 36:** üçü de public arama aracıdır — müvekkil bilgisi
> gönderilmez.

## Üçüncü-taraf veri kaynakları

- **OpenSanctions API** (`api.opensanctions.org`) — paid membership; kullanıcı kendi API key'ini temin eder. Müvekkil intake'inde yaptırım/PEP taraması için.
- **UYAP Avukat Portalı** (`uyap.gov.tr`) — avukatın kendi oturumu; dosya takip, e-tebligat, vekalet sunum.
- **KEP** (BTK lisanslı KEP sağlayıcı) — kullanıcı oturumu; müvekkil yazışmaları + ihtarname + mahkeme tebligat.
- **TÜRKPATENT** (`turkpatent.gov.tr`) — public marka/patent/tasarım arama (WebFetch).
- **EUIPO + WIPO** — public AB ve uluslararası marka arama.
- **MERSİS** (`mersis.gov.tr`) — public şirket sicili (UBO + conflict check için).

## Hukuk bürosuna özel referanslar

Bu pakette yeni olarak (Corporate paketinde olmayan) 9 hukuk bürosu spesifik referans dosyası yer alır:

| Referans | Konu | Kanun dayanağı |
|---|---|---|
| `aaut-rehberi.md` | Avukatlık Asgari Ücret Tarifesi | Av. K. m. 164-168 |
| `vekalet-uyap-rehberi.md` | Vekalet türleri + UYAP sunum | Av. K. m. 32/35/41 + HMK m. 74 |
| `mesleki-sir-rehberi.md` | Avukatlık mesleki sır | Av. K. m. 36 + TBB MK m. 36-37 + CMK m. 154 + HMK m. 249 |
| `conflict-check-rehberi.md` | Çıkar çatışması yasaklılık | Av. K. m. 38 + TBB MK m. 35-36 |
| `cmk-gorevli-rehberi.md` | CMK görevli atama yönetimi | CMK m. 91/100/102/130/147/150-156/268 + Av. K. m. 35 |
| `baro-islemleri-rehberi.md` | Baro koordinasyonu | Av. K. m. 17-67 + m. 134-158 |
| `ucret-sozlesmesi-rehberi.md` | Avukatlık ücret sözleşmesi | Av. K. m. 163-166 + DVK Tablo I + GVK m. 94 |
| `kep-etebligat-rehberi.md` | KEP + e-Tebligat | 5070 sayılı K. + TBK m. 117 + 7201 sayılı K. m. 7/A |
| `masak-kimlik-tespit-rehberi.md` | MASAK Tebliğ 5 yükümlülükleri | 5549 sayılı K. + MASAK Tebliğ Sıra No. 5 + TCK m. 282/4 |

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

## Kişisel veri ve mesleki sır uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket/müvekkil verisi içermez**. Tüm gerçek-kişi isimleri rol-bazlı yer-tutucularla (`[Yönetici Ortak]`, `[Kıdemli Ortak A]`, `[Müvekkil rumuz]`, `[KOBİ Üretici]` vb.) değiştirilmiştir. Büro örneği (`ArthurLegal Hukuk Bürosu`) tamamen kurgusaldır.

⚠️ **Avukatlık K. m. 36 hatırlatma:** Paketi kendi büronuza uyarladığınızda doldurduğunuz **gerçek müvekkil verileri** sizin ve büronuzun **mesleki sır + KVKK sorumluluğundadır**. Matter klasörlerini **cross-matter izoleli** tutmak zorundasınız (Müvekkil A'nın bilgisi Müvekkil B'nin dosyasına asla sızmamalı). Paylaşmadan önce gözden geçirin.
