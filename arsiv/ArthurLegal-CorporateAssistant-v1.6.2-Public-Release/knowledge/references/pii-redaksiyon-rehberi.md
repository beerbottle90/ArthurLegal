# Presidio + TAB — Kullanım Rehberi (PII maskeleme ve redaksiyon)

> **Durum:** ⚠️ MCP/connector yok — Presidio yerel Python kütüphanesi veya self-host servis olarak çalıştırılır; TAB, GitHub üzerinden indirilen statik bir değerlendirme korpusudur.
> **Erişim:** ✅ Açık kaynak (her ikisi de MIT) — API anahtarı gerekmez, tam çevrimdışı çalışabilir.
> **Yargı çevresi notu:** ArthurLegal'in birincil yargı çevresi Türkiye'dir; bu rehberdeki maskeleme disiplini tüm dosya türlerine uygulanır, ancak KVKK çerçevesi yalnızca Türkiye'ye temas eden kişisel veri işlemelerinde bağlayıcıdır. Yabancı yargı çevrelerindeki veri koruma rejimleri için `karsilastirmali-hukuk-rehberi.md` üzerinden ilgili rehbere geçilir.

## Presidio nedir?

Presidio, serbest metin, görüntü ve yapılandırılmış veride kişisel veri (PII) tespiti ve anonimleştirme yapan açık kaynak bir çerçevedir. Microsoft bünyesinde geliştirilmiş olup **topluluk yönetimli "Data Privacy Stack" organizasyonuna devredilmiştir**: depo artık `github.com/data-privacy-stack/presidio` adresindedir; eski `github.com/microsoft/presidio` ve `microsoft.github.io/presidio` adresleri yeni adreslere yönlendirir (çekim: 13.08.2026). Dört ana modülden oluşur:

- **Presidio Analyzer** — NER (spaCy/transformers), regex kalıpları, bağlam kelimeleri ve checksum doğrulaması birleştiren tespit motoru;
- **Presidio Anonymizer** — tespit edilen varlıkları maskeleme, silme, hash'leme veya sahte değerle değiştirme;
- **Presidio Image Redactor** — görüntü ve DICOM dosyalarındaki metinlerin karartılması;
- **Presidio Structured** — tablo/yarı yapılandırılmış veride sütun bazlı PII işleme.

Çok dilli çalışır (`analyzer/languages/` dokümantasyonu), tamamen çevrimdışı ve self-host edilebilir (Python, Docker, Kubernetes) ve özel tanıyıcı (custom recognizer) eklemek doğrudan desteklenir. Doğrulanmış önemli ayrıntı: **`TR_NATIONAL_ID` (TCKN, 11 haneli) ve `TR_LICENSE_PLATE` tanıyıcıları artık yerleşiktir** (çekim: 13.08.2026); vergi kimlik numarası (10 haneli) için hâlâ özel tanıyıcı gerekir.

**ArthurLegal için neden gerekli?** Rekabet Gözcüsü, çalışan iletişimlerini rekabet hukuku riski açısından izler; ArthurLegal paketleri müvekkil dosyalarındaki dilekçe, karar ve yazışmaları işler. Her iki akışta da metin, dış işleyicilere (Anthropic API, Yargı MCP) aktarılmadan **önce** çalışan/üçüncü kişi PII'sinin maskelenmesi zorunludur. Presidio bu maskeleme katmanının motorudur; TAB ise bu katmanın ne kadar güvenilir olduğunu ölçmenin yöntemidir. Ölçülmemiş bir redaksiyon katmanına üretimde güvenilmez.

## TAB (Text Anonymization Benchmark) nedir?

TAB, Norsk Regnesentral tarafından yayımlanan, metin anonimleştirme yöntemlerini değerlendirmek için tasarlanmış açık korpustur (`github.com/NorskRegnesentral/text-anonymization-benchmark`, MIT). İçeriği:

- **1.268 İngilizce AİHM kararı**, elle işaretlenmiş;
- her varlık için **DIRECT / QUASI tanımlayıcı türü ve maskeleme kararı (maskele / NO_MASK)** — yeniden kimliklendirme riski temelinde;
- **gizli nitelikler** (inanç, cinsel yönelim vb.) ve **eş-gönderim (co-reference) ilişkileri**;
- train/dev/test bölümleri, standoff JSON formatında (`echr_train.json`, `echr_dev.json`, `echr_test.json`) ve `evaluation.py` değerlendirme betiği;
- tanıtım makalesi: Pilán vd., "The Text Anonymization Benchmark (TAB)" (arXiv:2202.00443).

TAB'ın değeri, gerçek mahkeme metni üzerinde redaksiyon **recall/precision** ölçümüne izin vermesidir: hukuki metinde "hangi ifade kişiyi yeniden kimliklendirir" sorusu, genel amaçlı PII testlerinden çok daha zordur ve TAB bu soruyu insan kararlarıyla cevaplamış tek yaygın ölçüttür.

## Endpoint / URI şeması

Kaynak depolar ve dokümantasyon (tümü 13.08.2026 tarihinde doğrulandı):

```text
https://github.com/data-privacy-stack/presidio          # güncel Presidio deposu (MIT)
https://github.com/microsoft/presidio                   # eski adres — yenisine yönlendirir
https://presidio.dataprivacystack.org/                  # dokümantasyon ana sayfası
https://presidio.dataprivacystack.org/supported_entities/       # desteklenen varlık listesi
https://presidio.dataprivacystack.org/analyzer/adding_recognizers/  # özel tanıyıcı geliştirme
https://presidio.dataprivacystack.org/analyzer/languages/       # çok dilli yapılandırma
https://github.com/NorskRegnesentral/text-anonymization-benchmark   # TAB deposu (MIT)
https://arxiv.org/abs/2202.00443                        # TAB makalesi
```

Kurulum (pip paket adları doğrulandı):

```text
pip install presidio-analyzer presidio-anonymizer
pip install presidio-image-redactor presidio-structured   # gerektiğinde
```

Rekabet Gözcüsü / ArthurLegal akışlarında öncelikli varlık türleri:

| Varlık kodu | Kapsam | Tespit yöntemi |
|---|---|---|
| `TR_NATIONAL_ID` | TCKN (11 hane) | Kalıp + checksum (yerleşik) |
| `PERSON` | Ad-soyad | NER + bağlam |
| `EMAIL_ADDRESS` | E-posta | Kalıp + RFC-822 doğrulama |
| `PHONE_NUMBER` | Telefon | Kalıp + bölgesel bağlam |
| `IBAN_CODE` | IBAN | Kalıp + checksum |
| `CREDIT_CARD` | Kart numarası | Kalıp + checksum (Luhn) |
| `IP_ADDRESS` | IPv4/IPv6 | Kalıp |
| `LOCATION` | Yer adları | NER |
| `TR_LICENSE_PLATE` | TR plaka | Kalıp (il kodu + alfanümerik) |

Özel tanıyıcı yaklaşımı (kod değil, kroki): vergi kimlik numarası gibi yerleşik olmayan TR tanımlayıcıları için `PatternRecognizer` ile 10 haneli regex kalıbı tanımlanır, `context` parametresine "vergi", "VKN", "vergi kimlik" gibi bağlam kelimeleri verilir ve `EntityRecognizer.validate_result()` içinde VKN checksum algoritması uygulanarak yanlış pozitifler elenir; tanıyıcı `registry.add_recognizer()` ile kayda eklenir. Kod gerektirmeyen alternatif: YAML tanımı + `add_recognizers_from_yaml()`.

## Uygulamalı örnekler

**Örnek 1 — Yerleşik TR desteğini entegrasyon öncesi teyit etme.** Presidio sürüm atlamalarında varlık listesi değişebilir; TCKN tanıyıcısının hâlâ yerleşik olduğu her kurulumdan önce teyit edilir:

```text
WebFetch:
  url: https://presidio.dataprivacystack.org/supported_entities/
  prompt: "TR_NATIONAL_ID ve TR_LICENSE_PLATE listede mi? Tespit yöntemleri ne?"
```

Beklenen çıktı: `TR_NATIONAL_ID` — "a unique 11-digit number issued to all Turkish citizens", kalıp + checksum (çekim: 13.08.2026).

**Örnek 2 — TAB korpusunu yöntem doğrulaması için indirme.** Redaksiyon boru hattının recall'u, TAB test bölümü üzerinde `evaluation.py` ile ölçülür:

```text
WebFetch:
  url: https://github.com/NorskRegnesentral/text-anonymization-benchmark
  prompt: "echr_train/dev/test.json dosya konumları ve evaluation.py'nin ölçtüğü metrikler"
```

Korpus dosyaları depo kökündedir: `echr_train.json`, `echr_dev.json`, `echr_test.json`; anotasyon kılavuzu `guidelines.md` içindedir.

**Örnek 3 — Aktarım kapısında maskeleme akışı (kroki).** Rekabet Gözcüsü'nde bir yazışma alıntısı dış işleyiciye gitmeden önce: (1) `AnalyzerEngine.analyze(text, language=...)` ile varlıklar tespit edilir; (2) `AnonymizerEngine.anonymize()` ile her varlık rol etiketiyle değiştirilir (ör. `<CALISAN_1>`, `<TCKN>`); (3) etiket–kimlik eşlemesi yalnızca yerel, erişimi kısıtlı bir kasada tutulur; (4) ancak maskelenmiş metin Anthropic API'ye veya Yargı MCP sorgusuna girer. Aynı akış, bulgu defterine (append-only ledger) yazılacak alıntılar için de zorunludur.

## Redaksiyon disiplini (bağlayıcı kurallar)

1. **Aktarım öncesi maskeleme:** İzlenen iletişimlerdeki çalışan/kişi PII'si, herhangi bir dış işleyiciye (Anthropic API, Yargı MCP dahil) aktarılmadan **önce** maskelenir. Bu adım, Rekabet Gözcüsü'nün dört aktarım kapısından biridir; kapı atlanarak ham metin gönderilemez.
2. **Defter anonimleştirmesi:** Append-only bulgu defterine giren her alıntı anonimleştirilmiş hâliyle yazılır. Defter geri alınamaz olduğundan, maskeleme hatası da geri alınamaz — defter yazımı en yüksek özen eşiğine tabidir.
3. **Olasılıksal katman, garanti değil:** Presidio'nun kendi uyarısı aynen: "there is no guarantee that Presidio will find all sensitive information. Consequently, additional systems and protections should be employed." Presidio bir **katmandır**; tek başına yeterlilik iddiası kurulamaz. Katmanın performansı ölçülmeden üretime güvenilmez: yöntem doğrulaması TAB ile yapılır; **Türkçe recall için ayrı bir TR değerlendirme seti kurulmadan Türkçe metinde üretim güveni verilemez** (TAB İngilizce'dir ve TR performansına delil oluşturmaz).
4. **KVKK çerçevesi:** Maskeleme bir **veri minimizasyonu** aracıdır (KVKK m.4 ilkeleri yönünde); yurt dışına aktarımın **hukuki dayanağını ikame etmez**. Maskelenmiş veri aktarımı dahi, aktarım rejiminin (KVKK m.9 ve ilgili kurul kararları) ayrıca değerlendirilmesini gerektirir; bu değerlendirme `kvkk-m11-cevap-sablonu.md` ekseni ile birlikte okunur.

## Atıf disiplini

Bu rehber kapsamındaki kaynaklar **teknik/yöntemsel** kaynaklardır; atıf kalıbı diğer rehberlerle aynıdır — kaynak + çekim tarihi:

```text
[Presidio Docs — supported_entities — çekim: 13.08.2026]
[Presidio GitHub — data-privacy-stack/presidio README — çekim: 13.08.2026]
[TAB — NorskRegnesentral/text-anonymization-benchmark, echr_test.json — çekim: 13.08.2026]
```

Kritik sınır: **TAB bir değerlendirme veri setidir; asla hukuki atıf kaynağı değildir.** TAB içindeki AİHM kararları anonimleştirme ölçümü için derlenmiştir; bir dosyada AİHM içtihadına dayanılacaksa karar HUDOC/ilgili resmi kaynaktan yeniden çekilir ve o çekimle atıflanır ("kaynaksız hukuk yok" ilkesinin eval-verisi ayağı). Çekilmemiş hiçbir metin çekilmiş gibi sunulmaz; benchmark skorları da hukuki bir önermenin kaynağı olarak gösterilemez, yalnızca sistemin kendi performans beyanıdır.

## Lisans ve sınırlar

- **Presidio:** MIT lisansı (`github.com/data-privacy-stack/presidio`, çekim: 13.08.2026). Proje topluluk yönetimine ("Data Privacy Stack") devredilmiştir; artık bir Microsoft ürünü olarak konumlanmamaktadır. Eski microsoft/* adresleri yönlendirme yapmaktadır — entegrasyon yapılandırmalarında güncel adresler kullanılmalı, yönlendirmelerin süreceği varsayılmamalıdır (entegrasyon öncesi doğrulanmalı).
- **TAB:** MIT lisansı (`LICENSE.txt`, çekim: 13.08.2026). Korpus AİHM'in kamuya açık kararlarından türetilmiştir; içerdiği kişisel veriler nedeniyle korpusun kendisi de özenle işlenir — değerlendirme dışı amaçla kopyalanıp dağıtılmaz.
- **Governance bayrakları (yumuşatılamaz):**
  - Presidio olasılıksaldır; üretici dahi tüm PII'nin yakalanacağını garanti etmez. Ek koruma katmanları zorunludur.
  - TAB yalnızca yöntem doğrulaması içindir; Türkçe üretim güveni için ayrı TR değerlendirme seti kurulması **ön şarttır**.
  - Maskeleme, aktarımın hukuki dayanağını ikame etmez; KVKK aktarım analizi her durumda ayrıca yapılır.
  - Maskeleme katmanının sürüm, model ve tanıyıcı yapılandırması değiştiğinde benchmark ölçümü tekrarlanır; eski skorla yeni yapılandırmaya güven verilmez.

## İlgili rehberler

- `kvkk-m11-cevap-sablonu.md` — ilgili kişi başvurularında maskelenmiş defter kayıtlarının kullanımı ve KVKK cevap disiplini.
- `yargi-mcp-rehberi.md` — Yargı MCP'ye giden sorguların aktarım kapısından geçirilmesi; içtihat atıf disiplini.
- `karsilastirmali-hukuk-rehberi.md` — Türkiye dışı veri koruma rejimlerine temas eden dosyalarda yargı çevresi yönlendirmesi.