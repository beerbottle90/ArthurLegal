# Atıf

## ArthurLegal Courthouse Assistant v1.0.2

- **Author** (kod & içerik üretimi): Claude (Anthropic) — Opus 4.8 (`claude-opus-4-8`)
- **Designer** (proje tasarımı & domain bilgisi): Ertuğ Demir
- **Knowledge base** (temel iskelet): Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)

## Türetme notu

Bu paket, ArthurLegal **Law-Firm** ve **Corporate** paketlerinin iskeletinden türetilmiştir; ortak dokümanlar (usul referansları, atıf disiplini, MCP entegrasyon rehberleri) o paketlerden devralınmıştır. Türk hukuku entegrasyonu ArthurLegal MCP'nin Türkiye backend'i [`ArthurLegalTR`](https://github.com/beerbottle90/ArthurLegalTR) (MIT) üzerinden çalışır; uç bilgisi [saidsurucu](https://github.com/saidsurucu)'nun yargi-mcp ve mevzuat-mcp projelerinden (MIT) alınmıştır. Ancak konumsal çerçeve **savunucu/taraf-vekili** perspektifinden **yargısal/tarafsız** perspektife çevrilmiştir — bu, Courthouse'u ayrı bir ürün hattı yapan temel farktır.

## Arthur Mask kurulum dosyası (v1.8.0)

Arthur Mask, ArthurLegal GitHub v1.8.0 sürümüne eklenen `ArthurMask-Kurulum-1.0.0.exe` kurulum
dosyasıyla dağıtılan yerel gizlilik kapısıdır. Arthur Mask'in kendisi bu paketle aynı
**ArthurLegal Proprietary Non-Commercial License** kapsamındadır; kaynak kodu yayımlanmaz.

Kurulum dosyası aşağıdaki üçüncü taraf açık kaynak bileşenleri içerir. Bu bileşenler kendi
lisanslarına tabidir. Tam lisans metinleri ve atıf bildirimleri kurulum klasöründe
(`%LOCALAPPDATA%\Programs\Arthur Maskelgeler`) `ATTRIBUTION.md` dosyası ve `ucuncu-taraf-lisanslari` klasörüyle
birlikte gelir ve kaldırılamaz.

| Bileşen | Lisans |
|---|---|
| Microsoft Presidio | MIT |
| spaCy | MIT |
| GLiNER ve `urchade/gliner_multi_pii-v1` modeli | Apache-2.0 |
| mDeBERTa-v3 tokenizer | MIT |
| PyTorch | BSD-3-Clause |
| Hugging Face Transformers | Apache-2.0 |
| RapidOCR | Apache-2.0 |
| PaddleOCR PP-OCRv6 modelleri | Apache-2.0 |
| ONNX Runtime | MIT |
| pypdfium2 | Apache-2.0 / BSD-3-Clause |
| pypdf | BSD-3-Clause |
| Pillow | MIT-CMU |
| NumPy | BSD-3-Clause |
| cryptography | Apache-2.0 / BSD |
| Model Context Protocol Python SDK | MIT |
| PyYAML | MIT |
| Python | PSF License |

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

## Önemli

Bu paket **gerçek dosya / gerçek kişi verisi içermez**. Tüm örnekler kurgusaldır; profil alanları `[DOLDUR]` yer-tutucularıyla gelir. Çıktılar daima **taslaktır** ve **hâkim / heyet onayı** gerektirir — hiçbir çıktı yargısal karar yerine geçmez.
