# OSS Kaynak Dalgası — 2026-08

13 Ağustos 2026 tarihli derin araştırmanın (89 aday → 48 bağımsız vet kararı;
GitHub + Hugging Face + legal-oss.com + 14 yargı çevresi taraması) uygulama
paketi. İki ekosistemde aynı içerik kullanılır:

- **Claude paketleri** (ArthurLegal Corporate / Law Firm): `knowledge/references/`
  klasörüne aday dosyalar — v1.5.0 sürümüne girecek şekilde.
- **Copilot Studio** (SOCAR LC Digital Twin): bu klasör knowledge pack olarak
  yüklenir; `manifest.yml` yükleme sırasını ve uyarıları, `oss-source-catalog.json`
  makine-okur kaynak kaydını verir.

## İçerik

**Hızlı kazanım (governance-temiz, düşük efor):**

| Dosya | Konu |
|---|---|
| `abd-atif-dogrulama-rehberi.md` | eyecite + reporters-db + courts-db + x-ray + CourtListener citation-lookup — uydurma atıf savunması |
| `pii-redaksiyon-rehberi.md` | Presidio + TAB — dış aktarım öncesi PII maskeleme disiplini |
| `gleif-rehberi.md` | GLEIF LEI (CC0) — OpenSanctions'ın kimlik tamamlayıcısı |
| `edgar-rehberi.md` | SEC EDGAR (kamu malı) — birleşme/beyan katmanı |

**Konnektör dalgası (Fedlex kalıbının tekrarı; her rehberde mini-ADR):**

| Dosya | Yükseltme |
|---|---|
| `uk-legislation-mcp-rehberi.md` | UK: TNA'nın resmî MCP sunucusu (OGL v3.0) |
| `eurlex-cellar-rehberi.md` | EU/CJEU: Cellar SPARQL/REST, CELEX/ELI (CC BY 4.0 + CC0) |
| `japan-egov-api-rehberi.md` | JP: e-Gov 法令API v2, as-of-date çekim |
| `france-dila-rehberi.md` | FR: DILA açık veri dökümleri (Licence Ouverte) |
| `echr-hudoc-rehberi.md` | ECHR: echr-extractor (Apache-2.0) yapılandırılmış HUDOC erişimi |

## Governance çerçevesi

Tüm kararlar beş değişmeze karşı verildi: (1) resmî provenans veya beyan edilmiş
kesim tarihi, (2) kaynağında yazılı açık lisans, (3) kimlik bilgisisiz /
self-host loopback erişim, (4) aktif bakım veya tamamlanmış tasarım, (5) kaynak +
çekim tarihi atıf disiplini — eval verisi asla atıf kaynağı değildir, doktrin
otorite değildir.

Lisanslar 13.08.2026'da kaynağında doğrulanmıştır; **entegrasyon anında yeniden
doğrulayın**. Ayrıntılı gerekçeler ve RED listesi için araştırma raporuna bakın.
