# Atıf — ArthurLegal Claude Corporate Assistant v1.0.0

## Yapı

| Rol | Kim |
|---|---|
| **Author** (kod & içerik üretimi) | Claude (Anthropic) — Opus 4.7 (`claude-opus-4-7`) |
| **Designer** (proje tasarımı & domain bilgisi) | [VERSİYON YÖNETİCİSİ] |
| **Knowledge base** (temel hukuk asistanı paketi) | Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0) |

## Türk Mevzuat & Yargı entegrasyonu

Bu paketin Türk mevzuat (Mevzuat MCP) ve Türk yargı (Yargı MCP) entegrasyonu, [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan açık MCP sunucularını kullanır:

- `mevzuat.surucu.dev/mcp` — Türk mevzuatı norm metinleri (mevzuat.gov.tr + bedesten.adalet.gov.tr)
- `yargimcp.surucu.dev/mcp` — Türk yargı/idari kararlar (Yargıtay, Danıştay, AYM + 12 diğer kurum)

Her iki sunucu da public, auth gerektirmez.

## Üçüncü-taraf veri kaynakları

- **OpenSanctions API** (`api.opensanctions.org`) — paid membership; kullanıcı kendi API key'ini temin eder.
- **KAP** (`kap.org.tr`) — public özel durum açıklamaları (WebFetch).
- **e-ŞİRKET** (`e-sirket.mkk.com.tr`) — public sermaye yapısı bilgileri (WebFetch).

## Lisans

Apache License 2.0 — bkz. `LICENSE`.

Bu lisans, paketi serbestçe kullanma, değiştirme ve dağıtma hakkı verir; ancak orijinal atıf ve lisans bildirimi korunmalıdır.

## Kişisel veri uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket verisi içermez**. Tüm gerçek-kişi isimleri rol-bazlı yer-tutucularla (`[CLCO]`, `[DPO]`, `[Hukuk Direktörü A]` vb.) değiştirilmiştir. Kurumsal yapı örneği (`ArthurLegal Holding`) tamamen kurgusaldır.

Paketi kendi kurumunuza uyarladığınızda doldurduğunuz gerçek veriler **sizin kontrolünüzdedir** — paylaşmadan önce gözden geçirin.