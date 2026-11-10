# Connector Sağlık Durumu & Fallback Rehberi

> Mahkeme **birincil olarak ArthurLegal MCP (`tr_`)** (Mevzuat + Yargı) kullanır. Karşılaştırmalı/yabancı hukuk gerektiğinde önce ArthurLegal MCP'nin ülke önekli araçlarına (`uk_`, `eu_`, `de_`, `jp_`, `az_` ...), öneki olmayan ülkede aşağıdaki API/WebFetch yollarına başvurulur. Bu rehber, bir kaynak erişilemediğinde **çalışan alternatifi** verir.
> WebFetch satırlarının son canlı testi: **2026-06-28**; MCP satırlarında güncel durum için `status` çağrılır.

## ⚙️ API / WebFetch connector sağlık tablosu

| Jurisdiction | Birincil | Durum | Çalışan alternatif / yöntem |
|---|---|---|---|
| 🇹🇷 TR mevzuat/yargı | ArthurLegal MCP (`tr_`) | ✅ | (MCP — birincil) |
| 🇬🇧 UK | ArthurLegal MCP (`uk_`) | (MCP) | Yedek: legislation.gov.uk WebFetch |
| 🇺🇸 US mevzuat | api.govinfo.gov | ⚠️ API key | **Cornell LII** `law.cornell.edu/uscode` (no-key, ✅) |
| 🇺🇸 US içtihat | courtlistener.com/api | ✅ | — |
| 🇪🇺 AB | ArthurLegal MCP (`eu_`) | (MCP) | Yedek: eur-lex.europa.eu WebFetch |
| 🇪🇺 ECHR | hudoc.echr.coe.int | ⚠️ JS SPA | Query API `hudoc.echr.coe.int/app/query/results` (özel sözdizimi); düz WebFetch çalışmaz |
| 🇩🇪 DE | ArthurLegal MCP (`de_`; madde metni `de_norm_getir`) | (MCP) | `gesetze-im-internet.de` WebFetch ile ❌ ECONNREFUSED; yedek **NeuRIS** `testphase.rechtsinformationen.bund.de/v1/legislation` (JSON) |
| 🇫🇷 FR | legifrance.gouv.fr | ✅ | — |
| 🇮🇹 IT | normattiva.it | ✅ | — |
| 🇯🇵 JP | ArthurLegal MCP (`jp_`) | (MCP) | Yedek: laws.e-gov.go.jp/api |
| 🇷🇺 RU | pravo.gov.ru | ❌ ECONNREFUSED | **consultant.ru** `consultant.ru/document/...` (✅) |
| 🇦🇿 AZ | ArthurLegal MCP (`az_`) | (MCP) | `e-qanun.az` WebFetch ⚠️ anti-bot; yedek **cis-legislation.com** (11 BDT ülkesi, EN/RU) |
| 🇨🇳 CN | HuggingFace dataset | ⚠️ gated/401 | **flk.npc.gov.cn** (resmî DB) / **gov.cn** (✅) |
| 🇷🇸 SR | paragraf.rs | ✅ | — |
| 🇨🇭 CH | OpenCaseLaw.ch / Fedlex | (MCP) | İsviçre içtihat/mevzuat — MCP üzerinden |
| 🇹🇷 KAP | kap.org.tr | ✅ | — |

## Yargısal kullanım notu

- Mahkeme için **birincil kaynak daima ArthurLegal MCP (`tr_`)'dir**; yabancı hukuk yalnızca **karşılaştırmalı** değer taşır ve gerekçede "karşılaştırmalı hukuk — bağlayıcı değil" notuyla anılır.
- ❌/⚠️ işaretliler bu test ortamına özgü olabilir (IP/geo/JS); kritik kullanımda yeniden doğrula.
- Atıf disiplini değişmez: her dayanak ilgili kaynaktan **verbatim** çekilir (`[CourtListener — ...]`, `[OpenCaseLaw.ch — ...]`).

---

> **Toplam 15 dış kaynak** (TR hariç): 6'sı MCP üzerinden · 5 ✅ sağlıklı · 3 ⚠️ kısıtlı/alternatifli · 1 ❌ (alternatif bulundu). Detaylı durum yukarıdaki tabloda.
