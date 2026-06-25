# Atıf — ArthurLegal Claude Corporate Assistant v1.2.0

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

## Üçüncü-taraf veri kaynakları

- **OpenSanctions API** (`api.opensanctions.org`) — paid membership; kullanıcı kendi API key'ini temin eder.
- **KAP** (`kap.org.tr`) — public özel durum açıklamaları (WebFetch).
- **e-ŞİRKET** (`e-sirket.mkk.com.tr`) — public sermaye yapısı bilgileri (WebFetch).
- WebFetch kaynaklar (auth gerektirmez): legislation.gov.uk · GovInfo · CourtListener · EUR-Lex · HUDOC · gesetze-im-internet.de · Légifrance · Normattiva · e-Gov JP · Fedlex · pravo.gov.ru · e-qanun.az · HuggingFace/twang2218 · paragraf.rs

## Lisans

MIT License — bkz. `LICENSE`.

## Kişisel veri uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket verisi içermez**. `knowledge/company-profile.md` tamamen `[DOLDUR]` yer-tutucularından oluşan bir şablondur.

Paketi kendi kurumunuza uyarladığınızda doldurduğunuz gerçek veriler **sizin kontrolünüzdedir** — public repoya commit etmeden önce gözden geçirin.
