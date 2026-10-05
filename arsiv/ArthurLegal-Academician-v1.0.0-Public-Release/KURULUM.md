# Kurulum — ArthurLegal Academician Assistant v1.0.0

> Türkçe kurulum rehberi. English → [INSTALLATION.md](INSTALLATION.md)
>
> Hedef ortam: [Claude.ai Projects](https://claude.ai/projects) (web).
> Süre: ~15 dakika.

---

## Adım 1 — Claude.ai Project oluştur

1. [claude.ai](https://claude.ai) → sol menü → **Projects** → **Create Project**
2. Proje adı: `ArthurLegal Academician` (veya tercihiniz)
3. Açıklama: `Hukuk akademisyeni araştırma & yazım asistanı`

## Adım 2 — Custom Instructions'a sistem talimatlarını yapıştır

1. Projede **Set custom instructions** (veya ⚙️ → Instructions)
2. [`SYSTEM_PROMPT.md`](SYSTEM_PROMPT.md) dosyasının **tamamını** kopyalayıp yapıştır
3. Kaydet

> ⚠️ Başlıktaki alıntı bloğunu ("Bu metin claude.ai → …") dahil etmek zararsızdır.

## Adım 3 — Knowledge dosyalarını yükle

Projede **Add content / Upload** → `knowledge/` altındaki dosyaları yükle:

```
knowledge/
├─ akademisyen-profili.md      ← önce bunu doldur (Adım 4)
├─ skills/      (8 dosya)
├─ references/  (23 dosya)
└─ agents/      (4 dosya)
```

Toplu yükleme yapabiliyorsanız klasörü olduğu gibi sürükleyin. Yükleme sırası önemsizdir.

## Adım 4 — Profilini doldur

[`knowledge/akademisyen-profili.md`](knowledge/akademisyen-profili.md) dosyasını yüklemeden
**önce** kendi bilgilerinizle doldurun. Paket tüm alanları `[DOLDUR]` yer tutucusuyla gelir.

En kritik dört alan:

| Alan | Neden kritik |
|---|---|
| **Doktora tarihi** | Doçentlik puanlamasında "doktora sonrası" eşiği buna bağlı |
| **Atıf stili** | Klasik TR tam-dipnot / OSCOLA / Bluebook — çıktının biçimini belirler |
| **Rol bayrakları** (hakem / editör / panelist / jüri) | Gizlilik kuralının devreye girmesi için |
| **Başvuru dönemi ÜAK PDF'i teyidi** | Bu "Evet" olmadan doçentlik puanı kesin sunulmaz |

## Adım 5 — MCP bağlayıcılarını ekle (isteğe bağlı ama önerilir)

Claude.ai → **Settings → Connectors** üzerinden ekleyin:

| Sunucu | Ne için | Zorunlu mu |
|---|---|---|
| **TR Legal MCP** (Mevzuat + Yargı) | TR mevzuat, Yargıtay/Danıştay/AYM | TR çalışması için evet |
| **CourtListener** | ABD içtihadı (karşılaştırmalı hukuk) | Hayır |
| **Fedlex** | İsviçre federal mevzuatı | Hayır |
| **OpenCaseLaw.ch** | İsviçre içtihadı + doktrin köprüsü | Hayır |

Bağlayıcı yoksa asistan çalışır ama **atıf yapamaz** — her dayanağı
`[model bilgisi — DOĞRULAYIN]` etiketiyle işaretler ve sizden manuel doğrulama ister.
Bu, sıfır-halüsinasyon kuralının gereğidir.

> **API anahtarı gerekmez.** Crossref, OpenAlex, Semantic Scholar, DOAJ, ORCID, EUR-Lex ve
> HUDOC, WebFetch üzerinden anahtarsız kullanılır. Bu paket hiçbir anahtar gömmez.

## Adım 6 — Dene

Projede şunu yaz:

```
/yayin-etigi:uyz-beyani
```

Asistan sana araç sürümü, tarih ve kullanım kapsamını sorup hedef mecraya
(TÜBİTAK / TR Dizin / uluslararası dergi / tez) uygun beyan metnini üretmeli.

Sonra şunu dene:

```
/arastirma-tasarim:etik-kurul-triyaji
```

Çalışmanızın etik kurul izni gerektirip gerektirmediğini sorularla belirlemeli.

---

## Sık karşılaşılanlar

**Asistan atıf yapmıyor, "DOĞRULAYIN" diyor.**
Beklenen davranış. MCP bağlayıcısı yoksa veya kaynak çekilemediyse asistan **uydurmaz**.
Bağlayıcıyı ekleyin veya kaynağı kendiniz doğrulayın.

**Hakemlik yaptığım makaleyi yapıştırdım, reddetti.**
Doğru davranış. Değerlendirme altındaki müsveddenin ÜYZ araçlarına girilmesi gizlilik
ihlalidir (TÜBİTAK ÜYZ Rehberi § 2.2.1; NIH NOT-OD-23-149; NSF; Elsevier; ICMJE).
`/hakemlik-editorluk:hakem-rubrigi` kullanın — müsvedde olmadan rapor iskeleti üretir.

**Doçentlik puanımı hesaplamıyor.**
Profilde "Başvuru dönemi ÜAK PDF'i teyit edildi mi?" alanı `Evet` olmalı. Ölçütler
dönemden döneme değişir; asistan bayat tablodan kesin sonuç vermez.

**Benzerlik oranım %18, sorun var mı?**
Asistan bu soruya eşik vermez ve vermemelidir. Evrensel bir yüzde eşiği **yoktur**;
eşiği kurumunuz/derginiz belirler. `/yayin-etigi:benzerlik-yorumu` raporu **nitel**
okur: hangi eşleşme alıntı, hangisi sorunlu.

**Çıktı dili yanlış.**
`akademisyen-profili.md` → `Çıktı dili` alanını sabitleyin.

---

## Güncelleme

Yeni sürümde `SYSTEM_PROMPT.md` ve `knowledge/` dosyalarını değiştirin;
`akademisyen-profili.md` dosyanızı **koruyun** (kendi verinizdir).
Sürüm notları → [CHANGELOG.md](CHANGELOG.md)
