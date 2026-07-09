# VERSION

**Paket:** ArthurLegal Academician Assistant
**Sürüm:** 1.0.0
**Tarih:** 2026-07-09
**Hedef ortam:** Claude.ai Projects (web)
**Lisans:** ArthurLegal Proprietary Non-Commercial License (bkz. `LICENSE`)

---

## İçerik sayımı

| Bileşen | Adet |
|---|---|
| Plugin | 8 |
| Skill | 28 |
| Referans | 23 |
| Agent | 4 |
| Profil dosyası | 1 (`akademisyen-profili.md`) |

## Plugin dağılımı

| Plugin | Skill |
|---|---|
| `arastirma-tasarim` | 4 |
| `makale-yazim` | 4 |
| `atif-kaynak` | 3 |
| `yayin-etigi` | 4 |
| `akademik-yukselme` | 3 |
| `proje-fon` | 3 |
| `tez-danismanlik` | 3 |
| `hakemlik-editorluk` | 4 |

## Dil

Tam iki dilli (TR + EN). Kurulum: `KURULUM.md` (TR) + `INSTALLATION.md` (EN).

## MCP bağlayıcıları

TR Legal MCP (Mevzuat + Yargı) · CourtListener · Fedlex · OpenCaseLaw.ch

## Anahtarsız REST

Crossref · OpenAlex · Semantic Scholar · DOAJ · ORCID · EUR-Lex · HUDOC

> Bu paket **hiçbir API anahtarı gömmez**.

## Doğrulanması gereken kalemler

Aşağıdakiler zamanla değişir; paket bunları **kasıtlı olarak sabitlemez** ve kullanıcıdan
teyit ister:

- ÜAK Hukuk Temel Alanı doçentlik puan tablosu ve zorunlu koşullar (başvuru dönemi PDF'i)
- Doçentlik yabancı dil barajı
- Atıf stili kılavuzlarının güncel baskı numaraları (OSCOLA, Bluebook, McGill, AGLC, Chicago)
- Dergi ve yayıncı ÜYZ politikaları
- iThenticate / Turnitin kurumsal benzerlik eşikleri (**resmî tek oran yoktur**)
- HUDOC ve CURIA resmî API durumu
- TÜBİTAK ve Horizon Europe çağrı metinleri, form alanları, bütçe sınırları
