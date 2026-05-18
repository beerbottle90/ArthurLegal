# Atıf — ArthurLegal Claude Law Firm Assistant v1.0.0

## Yapı

| Rol | Kim |
|---|---|
| **Author** (kod & içerik üretimi) | Claude (Anthropic) — Opus 4.7 (`claude-opus-4-7`) |
| **Designer** (proje tasarımı & domain bilgisi) | Ertuğ Demir |
| **Knowledge base** (temel hukuk asistanı paketi) | Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0) |
| **Kardeş paket** | ArthurLegal Claude Corporate Assistant v1.0.0 (in-house tarafı; aynı metodoloji) |

## Türk Mevzuat & Yargı entegrasyonu

Bu paketin Türk mevzuat (Mevzuat MCP) ve Türk yargı (Yargı MCP) entegrasyonu, [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan açık MCP sunucularını kullanır:

- `mevzuat.surucu.dev/mcp` — Türk mevzuatı norm metinleri (mevzuat.gov.tr + bedesten.adalet.gov.tr)
- `yargimcp.surucu.dev/mcp` — Türk yargı/idari kararlar (Yargıtay, Danıştay, AYM + 12 diğer kurum)

Her iki sunucu da public, auth gerektirmez.

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

Apache License 2.0 — bkz. `LICENSE`.

Bu lisans, paketi serbestçe kullanma, değiştirme ve dağıtma hakkı verir; ancak orijinal atıf ve lisans bildirimi korunmalıdır.

## Kişisel veri ve mesleki sır uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket/müvekkil verisi içermez**. Tüm gerçek-kişi isimleri rol-bazlı yer-tutucularla (`[Yönetici Ortak]`, `[Kıdemli Ortak A]`, `[Müvekkil rumuz]`, `[KOBİ Üretici]` vb.) değiştirilmiştir. Büro örneği (`ArthurLegal Hukuk Bürosu`) tamamen kurgusaldır.

⚠️ **Avukatlık K. m. 36 hatırlatma:** Paketi kendi büronuza uyarladığınızda doldurduğunuz **gerçek müvekkil verileri** sizin ve büronuzun **mesleki sır + KVKK sorumluluğundadır**. Matter klasörlerini **cross-matter izoleli** tutmak zorundasınız (Müvekkil A'nın bilgisi Müvekkil B'nin dosyasına asla sızmamalı). Paylaşmadan önce gözden geçirin.
