# ArthurLegal — Claude Courthouse Assistant (TR)

**Sürüm:** v1.0.2 · **Tarih:** 2026-09-13 · **Lisans:** Proprietary — Non-Commercial (bkz. [LICENSE](LICENSE))
**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web ve Claude Desktop; Arthur Mask için Claude Desktop, Windows)

> **v1.0.0 — 8/8 plugin kurulu** (her biri 2-5 skill, toplam 28 skill + 24 referans). Referansların tamamı yargısal/tarafsız çerçevede (müşteri-spesifik içerik temizlendi).

> Türk **yargı mensubu** (mahkeme hâkimleri + mahkeme kalem memurlukları) için **yargısal / tarafsız** decision-support asistanı. ArthurLegal Law-Firm / Corporate iskeletinden türetilmiştir; ancak konum **savunucu değil, yargısaldır**.


> ### ⬇ Arthur Mask — belgeleri Claude'a vermeden önce bilgisayarınızda maskeleyin
> **[Kurulum dosyasını indirin (Windows, yaklaşık 1 GB)](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)**. Tıklayınca doğrudan iner; GitHub hesabı gerekmez.
> İnen `ArthurMask-Kurulum.exe` dosyasına çift tıklayın. Adım adım anlatım: **[ARTHUR-MASK.md](ARTHUR-MASK.md)**
> Claude Desktop (Windows) gerekir; claude.ai web ve mobil uygulamada çalışmaz.

---

## Diğer ArthurLegal paketlerinden farkı

| | Corporate / Law-Firm | **Courthouse** |
|---|---|---|
| Kullanıcı | In-house ekip / hukuk bürosu | **Mahkeme hâkimi + kalem memurluğu** |
| Perspektif | Taraf vekili (savunucu) | **Yargısal / tarafsız** |
| Amaç | Müvekkil lehine taslak | **Gerekçe + usulü yapılandırma** |
| Atıf | Katı | **Sıfır-halüsinasyon (karara girecek)** |
| Üst başlık | GİZLİDİR – HUKUK MÜŞAVİRLİĞİ | **MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK** |

**Temel ilke:** Asistan asla karar vermez. İki tarafı dengeli analiz eder, gerekçe iskeleti ve usul kontrolü üretir; nihai değerlendirme **hâkim / heyet** tarafından yapılır.

---

## Mimari — 4 dal × 2 rol = 8 plugin

| Dal | Usul | Hâkim plugin | Kalem plugin |
|---|---|---|---|
| **Hukuk** | HMK 6100 | `hukuk-hakim` ✅ | `hukuk-kalem` ✅ |
| **Ceza** | CMK 5271 | `ceza-hakim` ✅ | `ceza-kalem` ✅ |
| **İdari** | İYUK 2577 | `idari-hakim` ✅ | `idari-kalem` ✅ |
| **Vergi** | VUK 213 + İYUK | `vergi-hakim` ✅ | `vergi-kalem` ✅ |

- **Hâkim plugin'leri:** gerekçeli karar/hüküm taslağı, delil değerlendirme metodu, içtihat-emsal tarama, usul kontrol.
- **Kalem plugin'leri:** tensip zaptı, müzekkere, tebligat (7201), duruşma tutanağı, harç/gider, UYAP iş akışı, süre/zamanaşımı takibi.
- **DRY:** Çapraz içerik (tarafsızlık/atıf disiplini, tebligat, harç) paylaşılan referans katmanında tutulur, her plugin oradan çağırır.

---

## MCP entegrasyonları

| Sunucu | Kapsam |
|---|---|
| **ArthurLegal MCP** (`tr_`, `arthurlegal-mcp.fly.dev/mcp`, auth yok) | TR mevzuat norm metni, madde ağacı, gerekçe + Yargıtay/Danıştay/BAM/yerel/KYB + AYM + Uyuşmazlık Mah. + Resmî Gazete + 8 düzenleyici kurum + semantik arşiv |
| TR Legal MCP (isteğe bağlı) | AİHM, KİK, Sayıştay, Reklam Kurulu, KDK, TBB, HSK — ArthurLegal MCP'nin taşımadıkları |
| **CourtListener / OpenCaseLaw.ch** (ops.) | Karşılaştırmalı hukuk gerektiğinde ABD / İsviçre içtihadı |

Detay → `knowledge/references/yargi-mcp-rehberi.md`, `mevzuat-mcp-rehberi.md`.

---

## Arthur Mask — yerel gizlilik kapısı (v1.0.2)

Dava, soruşturma ve kovuşturma dosyalarındaki belgeler Claude'a verilmeden önce **kullanıcının kendi Windows bilgisayarında** maskelenebilir. **Arthur Mask 1.0.0**, tek bir Windows kurulum dosyasıyla gelen yerel programdır: **[ArthurMask-Kurulum.exe dosyasını indirin](https://github.com/beerbottle90/ArthurLegal/releases/download/arthur-mask/ArthurMask-Kurulum.exe)** (yaklaşık 1 GB; tıklayınca iner, GitHub hesabı gerekmez). UYAP UDF, Word, PDF veya taranmış belge bırakılır; taraf, şüpheli, sanık, mağdur ve tanık adları, TCKN, adres, telefon, dosya numarası gibi bilgiler `{{KİŞİ-01}}` gibi etiketlere dönüşür, gerçek değerler bilgisayardaki şifreli kasada kalır. Claude yalnız maskeli metni görür; cevap bilgisayarda gerçek adlarla Word veya UYAP editöründe açılır.

- **Korumalar:** belirsiz tespitler için inceleme ekranı · kırmızı hat (gerekçe yazılmadan gönderilmez) · Claude'a giden her yanıtın kasaya karşı son taranması (çıkış kapısı) · gönderim kaydı ve sızıntı denetimi.
- **Tamamen çevrimdışı.** Tespit ve OCR modelleri kurulum dosyasının içindedir.
- **Yalnız Claude Desktop (Windows).** claude.ai web ve mobilde çalışmaz; Project Claude Desktop'tan açılır.
- **Takma adlandırma, anonim hâle getirme değil.** Tespit olasılığa dayalıdır; KVKK, dosya gizliliği ve kurum kuralları bakımından sorumluluk kullanıcıdadır. Gizlilik veya kısıtlama kararı olan dosyalar maskeli olsa bile kurum kuralları izin vermedikçe verilmez.

Kurulum: [KURULUM.md](KURULUM.md) · kullanım rehberi: [ARTHUR-MASK.md](ARTHUR-MASK.md).

---

## Kurulum

Tam rehber → [KURULUM.md](KURULUM.md). Özet: Claude.ai Project oluştur → `SYSTEM_PROMPT.md`'yi Custom Instructions'a yapıştır → `knowledge/` dosyalarını yükle.

---

## Paket içeriği

```
ArthurLegal-Courthouse-v1.0.2-Public-Release/
├── KURULUM.md             ← Kurulum rehberi (buradan başlayın)
├── ARTHUR-MASK.md         ← Arthur Mask kullanım rehberi
├── SYSTEM_PROMPT.md       ← Claude.ai Custom Instructions metni
├── README.md              ← Bu dosya
├── CHANGELOG.md           ← Sürüm notları
├── VERSION.md             ← 1.0.2
├── ATTRIBUTION.md         ← Atıf bilgisi
├── LICENSE                ← Proprietary — Non-Commercial
└── knowledge/             ← Project Knowledge'a yüklenecek dosyalar
    ├── mahkeme-profili.md      (mahkeme profil şablonu — [DOLDUR])
    ├── skills/                 (8 plugin skill kitapçığı — 8/8, 28 skill)
    └── references/             (24 referans: 15 paylaşılan + 7 mahkeme-tarafı + 1 connector-sağlık + 1 Arthur Mask)
```

---

## Sınırlamalar

- **Yargısal karar değildir.** Tüm çıktılar hâkim/heyet incelemesi öncesi **taslaktır**.
- **Arthur Mask takma adlandırma yapar, anonimleştirmez.** Tespit olasılığa dayalıdır; tarihler ve tutarlar bilinçli olarak maskelenmez; resim, el yazısı, imza, kaşe ve QR kod maskelenmez. Yalnız Claude Desktop (Windows) ile çalışır.
- **Mevzuat / içtihat değişebilir** — kritik karar öncesi UYAP / Resmi Gazete manuel doğrulama.
- v1.0.0: 8 plugin de kuruludur (her biri 2-5 skill, toplam 28); referansların tamamı yargısal çerçevede. Skill derinliği sonraki patch'lerde artırılacaktır.

---

## Lisans

Bu paket **bir bütün olarak** ArthurLegal Proprietary Non-Commercial License
kapsamındadır — bkz. [LICENSE](LICENSE). **Ticari kullanım yasaktır.** In-house
counsel'ın, hukuk bürosu çalışanının ve gerçek kişinin kişisel kullanımı ile bu
kullanımlar için bizzat yapılan veya üçüncü kişiye yaptırılan geliştirmeler ticari
kullanım sayılmaz. Tüm hakları saklıdır.

Paketin türetildiği üçüncü taraf bilgi tabanı (Anthropic `claude-for-legal`)
**Apache License 2.0** altındadır. İlgili lisans ve atıf bildirimi
[LICENSE-APACHE-2.0-THIRD-PARTY.txt](LICENSE-APACHE-2.0-THIRD-PARTY.txt) dosyasında
korunmuştur ve kaldırılamaz. Çelişki hâlinde, o bileşenler bakımından Apache 2.0
geçerlidir. Atıf için → [ATTRIBUTION.md](ATTRIBUTION.md).
