# ArthurLegal Claude Corporate Assistant — KULLANIM REHBERİ

**Sürüm:** v1.0.0 — Initial Public Release
**Tarih:** 17.05.2026
**Lisans:** Apache 2.0
**Hedef ortam:** Claude.ai Projects (web — `claude.ai`)

---

## Bu paket nedir?

Türk hukukuna uyarlanmış, kurumsal in-house hukuk ekipleri için bir **Claude tabanlı hukuk asistanı paketi**. Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiş, Türk mevzuatına ve uygulamasına (Mevzuat MCP + Yargı MCP) adapte edilmiş hibrit bir şablondur.

**9 pratik alan:** commercial, corporate, employment, privacy (KVKK), regulatory, ip, litigation, tax, administrative.

**Yer-tutucu yapı:** Tüm gerçek-kişi isimleri rol-bazlı (`[CLCO]`, `[DPO]`, `[Hukuk Direktörü A]` vb.) çevrilmiştir. Kurumsal yapı örneği (`ArthurLegal Holding`) tamamen kurgusaldır. Paketi kendi kurumunuza uyarlayabilirsiniz.

---

## Bu pakette ne var?

```
ArthurLegal-v1.0.0-Public-Release/
├── KULLANIM-REHBERI.md        ← Bu dosya (önce bunu okuyun)
├── SYSTEM_PROMPT.md           ← Claude.ai Project Custom Instructions'a YAPIŞTIRACAĞINIZ metin
├── knowledge/                 ← Claude.ai Project Knowledge'a SÜRÜKLE-BIRAK ile yükleyeceğiniz dosyalar
│   ├── company-profile.md     (1 dosya — kurum profil şablonu)
│   ├── profiles/              (9 dosya — her plugin için pratik playbook)
│   ├── references/            (27 dosya — TR mevzuat hızlı referansları)
│   ├── skills/                (50+ dosya — adım-adım iş yöntemleri)
│   └── agents/                (7 dosya — periyodik iş tanımları)
├── ATTRIBUTION.md             ← Author / Designer / Knowledge atfı
├── LICENSE                    ← Apache 2.0 + disclaimer
└── CHANGELOG.md               ← Sürüm notları
```

Toplam knowledge dosyası: **100** | Toplam paket boyutu: ~500 KB.

---

## Kurulum — 4 adım, ~10 dakika

### Adım 1 — Yeni Claude.ai Project oluşturun

1. Tarayıcıda [https://claude.ai/projects](https://claude.ai/projects) açın.
2. Sağ üstte **"+ New Project"** butonuna tıklayın.
3. Proje ismi: `ArthurLegal Hukuk Asistanı` (veya kendi tercihinizle).
4. Açıklama (opsiyonel): "Türk hukuku odaklı kurumsal in-house asistan — TR overlay v1.0.0".

### Adım 2 — `SYSTEM_PROMPT.md` içeriğini yapıştırın

1. Proje sayfasında **"Custom Instructions"** alanına gidin (genelde proje ayarları içinde).
2. Bu paketin içindeki **`SYSTEM_PROMPT.md`** dosyasını bir metin editörü ile açın (Notepad, VSCode vb.).
3. Tüm içeriği seçin (`Ctrl+A`), kopyalayın (`Ctrl+C`), Claude.ai Custom Instructions alanına yapıştırın (`Ctrl+V`).
4. **Kaydet**.

> Not: İlk satır `# Sistem Talimatları — ArthurLegal Claude Corporate Assistant v1.0.0` olmalıdır. Markdown başlıkları, listelemeler, kod blokları ile beraber kopyalayın — Claude bunları doğal olarak işler.

### Adım 3 — `knowledge/` klasörünün içeriğini Project Knowledge'a yükleyin

1. Aynı projede **"Project Knowledge"** veya **"Add files"** bölümüne gidin.
2. Bu paketin **`knowledge/`** klasörünü açın.
3. İçindeki tüm dosya ve alt-klasörleri (`company-profile.md` + `profiles/` + `references/` + `skills/` + `agents/`) **sürükle-bırak** ile Project Knowledge alanına yükleyin.

Beklenen sonuç: Project Knowledge'da **~100 dosya** görmelisiniz.

> Not: Claude.ai Projects, alt-klasör yapısını otomatik düzleştirir. Bu sorun değil — sistem prompt'undaki yönlendirmeler dosya isimlerine göre çalışır.

### Adım 4 — Kurum profilini özelleştirin (önerilen)

Bu sürümün **şablon** olarak gelmesinin en güçlü tarafı: kendi kurumunuza uyarlanabilir olması.

1. **Yerel olarak** (paketi bilgisayarınızda) `knowledge/company-profile.md` dosyasını açın.
2. Köşeli parantezli alanları kendi kurumunuza göre doldurun:
   - `[Şirket Adı]`, `[Endüstri]`, `[CEO]`, `[CLCO]`, `[Hukuk Direktörü A]` vb.
   - Yer-tutucu listesi ~40 alan civarındadır; eksiksiz değil — doldurabildiğiniz kadarını doldurun.
3. Doldurulmuş dosyayı Claude.ai Project Knowledge'a yeniden yükleyin (eskisini silin).
4. **Aynı işlemi** `profiles/` klasöründeki 9 plugin profili için de yapın (`commercial-legal.md`, `corporate-legal.md`, ...). Onay eşikleri, dış vekil paneli, eskalasyon matriksi gibi alanları kendi prosedürlerinize göre uyarlayın.

> İpucu: İlk kez kullanıyorsanız Adım 4'ü atlayıp doğrudan kullanmaya başlayabilirsiniz. Asistan size hangi alanların boş olduğunu söyleyecektir; tek tek doldurabilirsiniz.

---

## İlk kullanım — örnekler

Claude.ai projesinde yeni bir konuşma açın ve şu komutları deneyin:

### Ticari sözleşme — NDA hızlı inceleme
```
/commercial-legal:nda-review

[NDA metnini yapıştır]
```
Asistan TBK 115 sorumsuzluk şartı, damga vergisi, KEP, eskalasyon yönlendirmesini GREEN / YELLOW / RED triage ile döndürür.

### KVKK — DSAR cevap taslağı
```
/privacy-legal:dsar-response

[Başvuru metnini yapıştır]
```
30 gün takvimi, KVKK m. 28 istisna kontrolü, Türkçe cevap mektubu taslağı.

### İSG kazası ilk-müdahale runbook
```
/litigation-legal:isg-incident-response

[Olayın temel bilgilerini yaz]
```
0–1 saat / 0–24 saat / 0–72 saat fazlarına bölünmüş runbook; üçlü-paralel risk (ceza + tazminat + idari).

### İdari dava ön-değerlendirme
```
/administrative-legal:idari-dava-prep
```
Görevli mahkeme tespiti (İdare Mah. mı, Danıştay mı?), İYUK m. 7 (idare 60 g / vergi 30 g), m. 20/A ÇED ivedi rejimi, m. 27 yürütmenin durdurulması.

### Marka clearance
```
/ip-legal:clearance --mark "[Marka adı]" --classes "9,42"
```

### Haftalık regülasyon digest
```
/regulatory-legal:reg-feed-watcher --week last
```

> Tüm `/<plugin>:<skill>` komutlarının listesi için: yeni konuşmada sadece `/commercial-legal:` yazdığınızda Claude size o eklentinin skill listesini gösterir.

---

## MCP entegrasyonları (opsiyonel — gelişmiş kullanım)

Bu paket aşağıdaki MCP sunucularını referans alır. Claude.ai hesabınızda **Connectors** bölümünden bunları etkinleştirirseniz, asistan canlı sorgu yapabilir:

| MCP Sunucu | URL | Auth | Kapsam |
|---|---|---|---|
| **Mevzuat MCP** | `mevzuat.surucu.dev/mcp` | Yok | TR mevzuat norm metinleri (kanun, KHK, tüzük, yönetmelik...) |
| **Yargı MCP** | `yargimcp.surucu.dev/mcp` | Yok | TR yargı/idari kararlar (15 kurum, 24 araç) |
| **OpenSanctions** | `api.opensanctions.org` | API key | Yaptırım/PEP taraması |

Her ikisi de [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan public MCP'lerdir.

OpenSanctions için: API key alın → Claude.ai Project'in environment'ına `OPENSANCTIONS_API_KEY` olarak ekleyin.

---

## Sınırlamalar — "yapmaz"lar

- **Hukuki tavsiye değildir.** Tüm çıktılar avukat incelemesi öncesi taslaktır.
- **Mevzuat / içtihat değişebilir.** Asistan model bilgisinden de cevap üretebilir — kritik karar öncesi UYAP / Lexpera / Resmi Gazete manuel doğrulama yapın.
- **Yerel idari düzenleme (belediye yönetmelik vs.) sınırlı.**
- **Tasarı/kanun teklifi aşaması kapsam dışıdır** — TBMM sitesinden manuel kontrol.
- **R&W insurance, sınır-ötesi sofistike tahkim** gibi alanlarda Türk pratiği sınırlıdır.

---

## Sorun bildirimi & geri bildirim

Bu sürüm `v1.0.0` ilk halka açık sürümdür. Deneme & geri bildirim çok değerli:

- ✉️ Karşılaştığınız hatalar, kötü çıktılar, eksik referanslar
- 💡 Eklenmesi gereken pratik alanlar veya referans dosyaları
- 🔁 Kullandığınız iyileştirme / pattern paylaşımı

---

## Atıf

- **Author:** Claude (Anthropic, Opus 4.7)
- **Designer:** Ertuğ Demir
- **Knowledge base:** Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal)

Detay için: `ATTRIBUTION.md` ve `LICENSE` dosyalarına bakınız.

---

*Sürüm: 1.0.0 — Initial Public Release | 17.05.2026*