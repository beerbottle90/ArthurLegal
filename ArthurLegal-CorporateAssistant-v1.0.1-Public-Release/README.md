# ArthurLegal — Claude Corporate Legal Assistant (TR)

**Sürüm:** v1.0.1 · **Tarih:** 23.05.2026 · **Lisans:** Apache 2.0
**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web)

> Türk hukukuna ve kurumsal in-house pratiğine adapte edilmiş, **Claude tabanlı hibrit hukuk asistanı paketi**. Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiştir.
>
> *A Turkish-law adaptation of Anthropic's [claude-for-legal](https://github.com/anthropics/claude-for-legal) — packaged as a Claude.ai Projects bundle (SYSTEM_PROMPT + ~100 knowledge files) for in-house corporate legal teams.*

---

## Ne işe yarar?

Türkiye'de bir in-house hukuk ekibinin gündelik üretim akışı için **avukat incelemesi öncesi taslak çıktılar** üretir: NDA triage, M&A diligence, KVKK DSAR cevabı, İSG runbook, idari dava ön-değerlendirme, marka clearance, haftalık regülasyon digest, transfer pricing kontrol notu, vergi davası akışı vb.

Çıktılar daima **taslaktır** ve avukat onayı gerektirir; paket bunu sıkı atıf disiplini ile zorlar (`[Mevzuat MCP — tarih]`, `[Yargı MCP — kurum — tarih]`, `[model bilgisi — doğrulayın]`).

---

## 9 pratik alan

| Plugin | Kapsam |
|---|---|
| `commercial-legal` | TBK + TTK + damga vergisi + KEP + ISTAC; NDA GREEN/YELLOW/RED triage |
| `corporate-legal` | TTK 134-209, Rekabet Kurulu 2010/4, SPK, VERBİS; M&A diligence |
| `employment-legal` | 4857, 5510, 6356, 6331; iç soruşturma, fesih, kıdem tazminatı tavanı |
| `privacy-legal` | 6698 KVKK + GDPR ikili rejim, m. 9 yurt dışı 2024 rejimi, DSAR 30 gün |
| `regulatory-legal` | Resmi Gazete + EPDK/BDDK/SPK/KGK + CBK haftalık digest |
| `ip-legal` | 6769 SMK, TÜRKPATENT, 5651 + 5846 FSEK; marka clearance, UDRP |
| `litigation-legal` | HMK + UYAP + İSG runbook (0-1/0-24/0-72 saat); TTK m. 5/A ön-kontrol |
| `tax-legal` | VUK 213, KVK 5520 (TP), KDVK 3065, ÖTV 4760, GİB özelge; Mali İşler-Hukuk koordinasyon |
| `administrative-legal` | İYUK 2577 (idare 60 g / vergi 30 g + m. 20/A ÇED ivedi); 3 dereceli idari yargı |

Detaylı içerik için → [CHANGELOG.md](CHANGELOG.md).

---

## MCP entegrasyonları

| Sunucu | URL | Auth | Kapsam |
|---|---|---|---|
| **Mevzuat MCP** | `mevzuat.surucu.dev/mcp` | Yok | TR mevzuat norm metinleri (kanun, KHK, tüzük, yönetmelik…) — 26 araç |
| **Yargı MCP** | `yargimcp.surucu.dev/mcp` | Yok | TR yargı/idari kararlar (Yargıtay, Danıştay, AYM + 12 kurum) — 24 araç |
| **OpenSanctions** | `api.opensanctions.org` | API key | Yaptırım/PEP taraması (paid membership) |
| **KAP + e-ŞİRKET** | `kap.org.tr`, `e-sirket.mkk.com.tr` | Yok | BIST açıklamaları + ortaklık yapısı (WebFetch) |

Mevzuat MCP ve Yargı MCP, [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan public MCP sunucularıdır.

---

## Kurulum — 5 adım, ~15 dakika

Tam rehber için → [KULLANIM-REHBERI.md](KULLANIM-REHBERI.md).

1. **Yeni Claude.ai Project oluşturun** — [claude.ai/projects](https://claude.ai/projects) → "+ New Project".
2. **`SYSTEM_PROMPT.md`** içeriğini Custom Instructions alanına yapıştırın.
3. **`knowledge/`** klasöründeki ~100 dosyayı Project Knowledge'a sürükle-bırak ile yükleyin.
4. **MCP bağlantılarını ekleyin** — Claude.ai Settings → Integrations → `mevzuat.surucu.dev/mcp` ve `yargimcp.surucu.dev/mcp` (auth yok).
5. **`knowledge/company-profile.md`** ve `profiles/*.md` dosyalarındaki `[DOLDUR]` yer-tutucularını kendi kurumunuza göre özelleştirin (opsiyonel — atlanabilir).

---

## İlk kullanım örnekleri

```text
/commercial-legal:nda-review
[NDA metnini yapıştır]
```
→ TBK 115 sorumsuzluk, damga vergisi, KEP, GREEN/YELLOW/RED triage.

```text
/privacy-legal:dsar-response
[DSAR başvurusunu yapıştır]
```
→ 30 gün takvimi, KVKK m. 28 istisna kontrolü, Türkçe cevap taslağı.

```text
/litigation-legal:isg-incident-response
[Olay özetini yaz]
```
→ 0-1 / 0-24 / 0-72 saat fazlarına bölünmüş runbook; ceza + tazminat + idari üçlü-paralel risk.

```text
/administrative-legal:idari-dava-prep
```
→ Görevli mahkeme (İdare Mah. mı, Danıştay mı?), İYUK m. 7 + m. 20/A + m. 27.

Tüm komutlar için yeni konuşmada sadece `/<plugin>:` yazın — Claude o plugin'in skill listesini gösterir.

---

## Paket içeriği

```
ArthurLegal-v1.0.0-Public-Release/
├── README.md                  ← Bu dosya
├── KULLANIM-REHBERI.md        ← Detaylı kurulum & kullanım
├── SYSTEM_PROMPT.md           ← Claude.ai Custom Instructions metni
├── knowledge/                 ← Project Knowledge'a yüklenecek dosyalar (~100)
│   ├── company-profile.md     (kurum profil şablonu)
│   ├── profiles/              (9 plugin profili)
│   ├── references/            (~27 TR mevzuat referansı)
│   ├── skills/                (50+ adım-adım iş yöntemi)
│   └── agents/                (7 periyodik iş tanımı)
├── ATTRIBUTION.md             ← Author / Designer / Knowledge atfı
├── LICENSE                    ← Apache 2.0
└── CHANGELOG.md               ← Sürüm notları
```

---

## Sınırlamalar

- **Hukuki tavsiye değildir.** Tüm çıktılar avukat incelemesi öncesi taslaktır.
- **Mevzuat / içtihat değişebilir** — kritik karar öncesi UYAP / Lexpera / Resmi Gazete manuel doğrulama.
- Yerel idari düzenleme, tasarı/teklif aşaması, R&W insurance ve sınır-ötesi sofistike tahkim kapsam dışı veya sınırlıdır.

---

## Kişisel veri uyarısı

Bu paket halka açık sürümünde **gerçek kişi/şirket verisi içermez**. Tüm gerçek-kişi isimleri rol-bazlı yer-tutucularla (`[CLCO]`, `[DPO]`, `[Hukuk Direktörü A]` vb.) değiştirilmiştir. Kurumsal yapı örneği (`ArthurLegal Holding`) tamamen kurgusaldır. Paketi kendi kurumunuza uyarladığınızda doldurduğunuz veriler **sizin kontrolünüzdedir** — paylaşmadan önce gözden geçirin.

---

## Atıf

- **Author** (kod & içerik üretimi): Claude (Anthropic) — Opus 4.7 (`claude-opus-4-7`)
- **Designer** (proje tasarımı & domain bilgisi): Ertuğ Demir
- **Knowledge base**: Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)

Detay için → [ATTRIBUTION.md](ATTRIBUTION.md).

---

## Lisans

Apache License 2.0 — bkz. [LICENSE](LICENSE). Serbest kullanım, değiştirme ve dağıtım hakkı verir; orijinal atıf ve lisans bildirimi korunmalıdır.
