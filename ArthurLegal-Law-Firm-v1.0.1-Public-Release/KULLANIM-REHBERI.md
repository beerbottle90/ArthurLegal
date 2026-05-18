# ArthurLegal Claude Law Firm Assistant — KULLANIM REHBERİ

**Sürüm:** v1.0.0 — Initial Public Release
**Tarih:** 17.05.2026
**Lisans:** Apache 2.0
**Hedef ortam:** Claude.ai Projects (web — `claude.ai`)

---

## Bu paket nedir?

Türk hukukuna uyarlanmış, **dava + danışmanlık dengeli çalışan 0–30 çalışanlı hukuk büroları** için **danışman tarafı** Claude tabanlı asistan paketi. Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiş; Türk mevzuatı + **avukatlık meslek pratiği** (Av. K. m. 36/38/164, AAÜT, TBB Meslek Kuralları) zemininde kurgulanmıştır.

**9 pratik alan:** dispute-litigation, administrative-litigation, tax-litigation, criminal-defense, commercial-advisory, corporate-advisory, employment-advisory, ip-advisory, firm-operations.

**Yer-tutucu yapı:** Tüm gerçek-kişi/müvekkil isimleri rol-bazlı (`[Yönetici Ortak]`, `[Kıdemli Ortak A]`, `[Müvekkil rumuz]`, `[KOBİ Üretici]` vb.) tutulmuştur. Büro örneği (`ArthurLegal Hukuk Bürosu`) tamamen kurgusaldır.

---

## Bu pakette ne var?

```
ArthurLegal-Law-Firm-v1.0.0-Public-Release/
├── KULLANIM-REHBERI.md        ← Bu dosya (önce bunu okuyun)
├── SYSTEM_PROMPT.md           ← Claude.ai Project Custom Instructions'a YAPIŞTIRACAĞINIZ metin
├── knowledge/                 ← Claude.ai Project Knowledge'a SÜRÜKLE-BIRAK ile yükleyeceğiniz dosyalar
│   ├── firm-profile.md        (1 dosya — büro profil şablonu)
│   ├── profiles/              (9 dosya — her plugin için pratik playbook)
│   ├── references/            (33 dosya — TR mevzuat + meslek pratiği referansları)
│   └── skills/                (19 dosya — adım-adım iş yöntemleri — flat naming)
├── README.md                  ← Tanıtım + 9 pratik alan + özellikler
├── ATTRIBUTION.md             ← Author / Designer / Knowledge atfı
├── LICENSE                    ← Apache 2.0 + disclaimer
└── CHANGELOG.md               ← Sürüm notları
```

**Toplam knowledge dosyası: 62** | **Toplam paket boyutu: ~350 KB**.

---

## Kurulum — 4 adım, ~10 dakika

### Adım 1 — Yeni Claude.ai Project oluşturun

1. Tarayıcıda [https://claude.ai/projects](https://claude.ai/projects) açın.
2. Sağ üstte **"+ New Project"** butonuna tıklayın.
3. Proje ismi: `ArthurLegal Hukuk Bürosu Assistant` (veya kendi tercihinizle, örn. `[Büronuz adı] – Claude Asistan`).
4. Açıklama (opsiyonel): "Türk hukuku — dava + danışmanlık + büro işletim — TR overlay v1.0.0".

### Adım 2 — `SYSTEM_PROMPT.md` içeriğini yapıştırın

1. Proje sayfasında **"Custom Instructions"** alanına gidin (genelde proje ayarları içinde).
2. Bu paketin içindeki **`SYSTEM_PROMPT.md`** dosyasını bir metin editörü ile açın (Notepad, VSCode vb.).
3. Tüm içeriği seçin (`Ctrl+A`), kopyalayın (`Ctrl+C`), Claude.ai Custom Instructions alanına yapıştırın (`Ctrl+V`).
4. **Kaydet**.

> Not: İlk satır `# Sistem Talimatları — ArthurLegal Claude Law Firm Assistant v1.0.0` olmalıdır. Markdown başlıkları, listelemeler, kod blokları ile beraber kopyalayın — Claude bunları doğal olarak işler.

### Adım 3 — `knowledge/` klasörünün içeriğini Project Knowledge'a yükleyin

1. Aynı projede **"Project Knowledge"** veya **"Add files"** bölümüne gidin.
2. Bu paketin **`knowledge/`** klasörünü açın.
3. İçindeki tüm dosya ve alt-klasörleri (`firm-profile.md` + `profiles/` + `references/` + `skills/`) **sürükle-bırak** ile Project Knowledge alanına yükleyin.

Beklenen sonuç: Project Knowledge'da **62 dosya** görmelisiniz.

> Not: Claude.ai Projects, alt-klasör yapısını otomatik düzleştirir. Bu sorun değil — sistem prompt'undaki yönlendirmeler dosya isimlerine göre çalışır (`<plugin>__<skill>.md` adlandırma).

### Adım 4 — Büro profilini özelleştirin (önerilen)

Bu sürümün **şablon** olarak gelmesinin en güçlü tarafı: kendi büronuza uyarlanabilir olması.

1. **Yerel olarak** (paketi bilgisayarınızda) `knowledge/firm-profile.md` dosyasını açın.
2. Köşeli parantezli alanları kendi büronuza göre doldurun:
   - `[Büro Adı]`, `[Yönetici Ortak]`, `[Kıdemli Ortak A/B/C]`
   - `[Hukuk Asistanı / Sekretarya]`, `[İstanbul Barosu sicil no]`
   - Müvekkil portföyü agregat (sektör + tip + coğrafya — gerçek isim YOK)
   - Vekalet ücreti modeli (saatlik oran + AAÜT katsayı)
   - Operasyonel platformlar (iManage / SharePoint / Drive vb.)
3. Doldurulmuş dosyayı Claude.ai Project Knowledge'a yeniden yükleyin (eskisini silin).
4. **Aynı işlemi** `profiles/` klasöründeki 9 plugin profili için de yapın. Conflict-check eşikleri, AAÜT katsayı tercihi, baro koordinasyonu gibi alanları kendi prosedürlerinize göre uyarlayın.

> İpucu: İlk kez kullanıyorsanız Adım 4'ü atlayıp doğrudan kullanmaya başlayabilirsiniz. Asistan size hangi alanların boş olduğunu söyleyecektir; tek tek doldurabilirsiniz.

> ⚠️ **MESLEKİ SIR UYARISI:** `firm-profile.md`'ye gerçek müvekkil isimleri YAZMAYIN. Müvekkil portföyü **agregat sektör/tip/coğrafya** olarak tutulur. Matter-spesifik bilgi her matter için ayrı çalışmada — Claude.ai Projects'te müvekkil rumuzu (`[Müvekkil-001]`, `[KOBİ Üretici]`) kullanın.

---

## İlk kullanım — örnekler

Claude.ai projesinde yeni bir konuşma açın ve şu komutları deneyin:

### Yeni müvekkil intake (ana akış)
```
/firm-operations:new-client-intake

Müvekkil tipi: KOBİ (üretim — gıda)
Talep: tedarikçi alacağı tahsili (yaklaşık 2,5 M TL)
Karşı taraf: rumuz "Tedarikçi-X" (KOBİ, gıda ambalaj)
İlk temas: bugün, telefonla
```
Asistan müvekkil bilgisi alır, matter tipini `dispute-litigation` olarak yönlendirir, 7-adımlı zorunlu zinciri (conflict / MASAK / sanctions / KVKK / fee / vekalet / matter-open) listeler.

### Conflict check (zorunlu ikinci adım)
```
/firm-operations:conflict-check

Müvekkil: [yeni gelen müvekkilin TC/Vergi no rumuzlanmış]
Karşı taraf: Tedarikçi-X (Vergi no rumuzlanmış)
Atanan ortak: Kıdemli Ortak A
```
Asistan üç eksen tarama yapar (müvekkil geçmişi / karşı taraf geçmişi / atanan avukat geçmişi). Sonuç: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ.

### CMK görevli atama yönetimi
```
/criminal-defense:cmk-gorev-atama

Atama: Baro CMK Servisi mesajı (TC son 4: 1234)
Suçlama: TCK m. 86/1 (kasten yaralama)
Yer: [İlçe] Karakolu
Atama zamanı: bugün 23:45
```
Asistan 48 saat akışı, susma hakkı hatırlatması, ifade hazırlık checklist, tutukluluk değerlendirme ve CMK ödeme cetveli için adım listesi üretir.

### Vergi davası — 30 g süre kontrolü
```
/tax-litigation:vergi-davasi-prep

Mükellef: [KOBİ rumuz]
Vergi türü: KDV (ek tarhiyat — 800K TL + ceza)
İhbarname tebliğ tarihi: 10.05.2026
```
**30 g süre KRİTİK kontrolü:** süre bitiş 09.06.2026 — kalan N gün. Uzlaşma vs. dava matrisi, Danıştay 7. Daire (KDV) emsal araması, YMM raporu ihtiyacı.

### NDA hızlı inceleme
```
/commercial-advisory:draft-nda

Karşı yan: yurtdışı satıcı (potansiyel JV görüşmesi)
Müvekkil pozisyonu: B-tarafı (denk müzakere)
[NDA taslağını yapıştır]
```
Asistan TBK m. 115 sorumsuzluk şartı kontrolü, damga vergisi hesabı, KEP teslim, ISTAC tahkim klozu önerisi, GREEN/YELLOW/RED triage uygular.

### İşveren tarafı fesih değerlendirmesi
```
/employment-advisory:fesih-degerlendirme

Müvekkil: KOBİ işveren (45 işçi)
İşçi: 6 yıl hizmet, brüt 35.000 TL/ay, orta kademe
Fesih sebebi: performans (geçerli fesih düşünülüyor)
```
4857 m. 18 değerlendirme, tahmini tazminat yükü (kıdem + ihbar + işe iade riski 4-8 ay), arabuluculuk + dava akışı, hukuki risk skalası.

### Marka clearance
```
/ip-advisory:marka-clearance

Marka: "[müvekkil markası]"
Sınıf: 25 (giyim)
Hedef coğrafya: TR + Madrid (EU + ABD)
```
TÜRKPATENT + EUIPO + Madrid + ticaret unvanı (MERSİS) + alan adı tarama. 6769 SMK m. 5 (mutlak red) + m. 6 (nispi red) değerlendirme. 🟢/🟡/🟠/🔴 risk skoru.

> Tüm `/<plugin>:<skill>` komutlarının listesi için: yeni konuşmada sadece `/firm-operations:` yazdığınızda Claude size o eklentinin skill listesini gösterir.

---

## MCP entegrasyonları (opsiyonel — gelişmiş kullanım)

Bu paket aşağıdaki MCP sunucularını referans alır. Claude.ai hesabınızda **Connectors** bölümünden bunları etkinleştirirseniz, asistan canlı sorgu yapabilir:

| MCP Sunucu | URL | Auth | Kapsam |
|---|---|---|---|
| **Mevzuat MCP** | `mevzuat.surucu.dev/mcp` | Yok | TR mevzuat norm metinleri (kanun, KHK, tüzük, yönetmelik...) |
| **Yargı MCP** | `yargimcp.surucu.dev/mcp` | Yok | TR yargı/idari kararlar (15 kurum, 24 araç) |
| **OpenSanctions** | `api.opensanctions.org` | API key | Müvekkil due diligence (yaptırım/PEP taraması) |

Her ikisi de [saidsurucu](https://github.com/saidsurucu) tarafından yayımlanan public MCP'lerdir.

OpenSanctions için: API key alın (paid membership) → Claude.ai Project'in environment'ına `OPENSANCTIONS_API_KEY` olarak ekleyin. Müvekkil intake'inde `sanctions-check` skill'i bu key'i WebFetch ile kullanır.

---

## Mesleki sır + KVKK uyarısı (büro tarafı kritik)

⚠️ **claude.ai'a yüklediğiniz tüm bilgiler Anthropic'in altyapısında işlenir.** Av. K. m. 36 + KVKK açısından:

- **Anonimleştirme:** Müvekkil + karşı yan + tanık isimlerini **rumuz** ile değiştirin. "X" + "Y" yeterli.
- **Sayı maskeleme:** TC kimlik / vergi no son 4 rakam yeter — tam değil
- **Adres maskeleme:** "İstanbul" yeterli — tam adres değil
- **Belge yükleme:** Hassas belgeleri (kimlik fotokopisi, banka detay) yüklemeyin — özet/agregat yeter
- **Project paylaşımı:** Tek kullanıcı, başkalarıyla paylaşmayın

Aksi halde **Av. K. m. 36 mesleki sır ihlali + KVKK m. 12 ihlali** riski.

---

## Sınırlamalar — "yapmaz"lar

- **Hukuki tavsiye değildir.** Tüm çıktılar **atanan ortak / Yönetici Ortak** incelemesi öncesi taslaktır.
- **Mesleki sorumluluk** yine avukatındır; baroya kayıtlı **imzalı** belge olmadan müvekkile/mahkemeye sunulamaz.
- **Mevzuat / içtihat değişebilir.** Asistan model bilgisinden de cevap üretebilir — kritik karar öncesi UYAP / Lexpera / Resmi Gazete manuel doğrulama yapın.
- **Conflict check otomatik** ama Av. K. m. 38 nüansları **insan yargısı** ister; otomatik tarama eşik filter görevi görür.
- **CMK görevli atama** baro CMK servisi üzerinden gelir — paket atama otomasyonu sağlamaz.
- **Aile/miras + denizcilik + enerji ihtisas** kapsam dışıdır — başka uzmana yönlendirme önerisi otomatik flag.
- **Yerel idari düzenleme** sınırlı (belediye yönetmelik vb.).
- **R&W insurance, sınır-ötesi sofistike tahkim** alanlarında Türk pratiği sınırlıdır.

---

## Sorun bildirimi & geri bildirim

Bu sürüm `v1.0.0` ilk halka açık sürümdür. Deneme & geri bildirim çok değerli:

- ✉️ Karşılaştığınız hatalar, kötü çıktılar, eksik referanslar
- 💡 Eklenmesi gereken pratik alanlar (örn. aile/miras plugin'i v1.1 için aday)
- 🔁 Kullandığınız iyileştirme / pattern paylaşımı (anonimleştirilmiş)

---

## Atıf

- **Author:** Claude (Anthropic, Opus 4.7)
- **Designer:** Ertuğ Demir
- **Knowledge base:** Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal)
- **Kardeş paket:** ArthurLegal Claude Corporate Assistant v1.0.0 (in-house, danışan tarafı)

Detay için: `ATTRIBUTION.md` ve `LICENSE` dosyalarına bakınız.

---

*Sürüm: 1.0.0 — Initial Public Release | 17.05.2026*
