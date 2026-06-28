# Connector Sağlık Durumu & Fallback Rehberi

> Mahkeme **birincil olarak TR Legal MCP** (Mevzuat + Yargı) kullanır. Karşılaştırmalı/yabancı hukuk gerektiğinde aşağıdaki API/WebFetch connector'larına başvurulur. Bu rehber, bir kaynak erişilemediğinde **çalışan alternatifi** verir.
> Son canlı test: **2026-06-28**.

## ⚙️ API / WebFetch connector sağlık tablosu

| Jurisdiction | Birincil | Durum | Çalışan alternatif / yöntem |
|---|---|---|---|
| 🇹🇷 TR mevzuat/yargı | TR Legal MCP | ✅ | (MCP — birincil) |
| 🇬🇧 UK | legislation.gov.uk | ✅ | — |
| 🇺🇸 US mevzuat | api.govinfo.gov | ⚠️ API key | **Cornell LII** `law.cornell.edu/uscode` (no-key, ✅) |
| 🇺🇸 US içtihat | courtlistener.com/api | ✅ | — |
| 🇪🇺 AB | eur-lex.europa.eu | ✅ | — |
| 🇪🇺 ECHR | hudoc.echr.coe.int | ⚠️ JS SPA | Query API `hudoc.echr.coe.int/app/query/results` (özel sözdizimi); düz WebFetch çalışmaz |
| 🇩🇪 DE | gesetze-im-internet.de | ❌ ECONNREFUSED | **NeuRIS** `testphase.rechtsinformationen.bund.de/v1/legislation` (JSON, ✅) |
| 🇫🇷 FR | legifrance.gouv.fr | ✅ | — |
| 🇮🇹 IT | normattiva.it | ✅ | — |
| 🇯🇵 JP | laws.e-gov.go.jp/api | ✅ | — |
| 🇷🇺 RU | pravo.gov.ru | ❌ ECONNREFUSED | **consultant.ru** `consultant.ru/document/...` (✅) |
| 🇦🇿 AZ | e-qanun.az | ⚠️ anti-bot | **cis-legislation.com** (11 BDT ülkesi, EN/RU, ✅) |
| 🇨🇳 CN | HuggingFace dataset | ⚠️ gated/401 | **flk.npc.gov.cn** (resmî DB) / **gov.cn** (✅) |
| 🇷🇸 SR | paragraf.rs | ✅ | — |
| 🇨🇭 CH | OpenCaseLaw.ch / Fedlex | (MCP) | İsviçre içtihat/mevzuat — MCP üzerinden |
| 🌍 OpenSanctions | api.opensanctions.org | ✅ key gömülü | `Authorization: Apikey a1c019122d0de8880772f7282c0ae03d` |
| 🇹🇷 KAP | kap.org.tr | ✅ | — |

## Yargısal kullanım notu

- Mahkeme için **birincil kaynak daima TR Legal MCP'dir**; yabancı hukuk yalnızca **karşılaştırmalı** değer taşır ve gerekçede "karşılaştırmalı hukuk — bağlayıcı değil" notuyla anılır.
- ❌/⚠️ işaretliler bu test ortamına özgü olabilir (IP/geo/JS); kritik kullanımda yeniden doğrula.
- Atıf disiplini değişmez: her dayanak ilgili kaynaktan **verbatim** çekilir (`[CourtListener — ...]`, `[OpenCaseLaw.ch — ...]`).

---

> **Toplam 16 dış connector** (TR MCP hariç): 8 ✅ sağlıklı · 6 ⚠️ kısıtlı/alternatifli · 2 ❌ (alternatif bulundu). Detaylı durum yukarıdaki tabloda.
