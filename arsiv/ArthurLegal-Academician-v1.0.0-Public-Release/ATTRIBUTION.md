# Atıf

## ArthurLegal Academician Assistant

- **Author** (kod & içerik üretimi): Claude (Anthropic) — Opus 4.8 (`claude-opus-4-8`)
- **Designer** (proje tasarımı & domain bilgisi): Ertuğ Demir
- **Knowledge base** (temel iskelet): Anthropic — [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)

## Türetme notu

Bu paket, ArthurLegal **Law-Firm**, **Corporate** ve **Courthouse** paketlerinin
iskeletinden türetilmiştir; paylaşılan referanslar (MCP entegrasyon rehberleri, kanun
kısaltmaları, atıf disiplini) o paketlerden devralınmıştır.

Ancak konumsal çerçeve temelden farklıdır. Diğer paketlerde asistan, düzenlemenin
**öznesine** yardım eder. Academician'da **asistanın kendisi düzenlemenin nesnesidir**:
akademik yayın ve proje süreçlerinde üretken yapay zekâ kullanımı hem Türkiye'de hem
uluslararası düzlemde doğrudan düzenlenmiştir. Bu, paketin merkezine **ÜYZ Kapısı**'nı
koyar ve `hakemlik-editorluk` plugin'inin müsvedde-almayan tasarımını zorunlu kılar.

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

## Normatif kaynaklar

Bu paketin kuralları aşağıdaki belgelere dayanır. Hiçbiri bu pakete kopyalanmamıştır;
paket yalnızca **atıf yapar ve yönlendirir**. Güncel metinler ilgili kurumdan teyit edilmelidir.

**Türkiye**
- YÖK — *Üretken Yapay Zekâ Kullanımına Dair Etik Rehber* (2024)
- YÖK — *Yükseköğretim Kurumları Bilimsel Araştırma ve Yayın Etiği Yönergesi* (değişik 28/8/2025)
- ÜAK — Doçentlik Başvuru Şartları, Hukuk Temel Alanı (dönem bazlı)
- TÜBİTAK — *Üretken Yapay Zekânın Sorumlu ve Güvenilir Kullanımı Rehberi*
- ULAKBİM TR Dizin — Dergi Değerlendirme Kriterleri
- 2547 sayılı Kanun; Öğretim Üyeliğine Yükseltilme ve Atanma Yönetmeliği

**Uluslararası**
- COPE — *Authorship and AI tools* (13.02.2023); *Retraction Guidelines*
- ICMJE — *Recommendations* (AI bölümleri)
- WAME — *Chatbots, Generative AI, and Scholarly Manuscripts*
- Avrupa Komisyonu (ERA Forum) — *Living guidelines on the responsible use of generative AI in research*
- ALLEA — *The European Code of Conduct for Research Integrity* (revize baskı 2023)
- NIH — NOT-OD-23-149; NSF — merit review AI bildirimi
- NISO — CRediT, ANSI/NISO Z39.104-2022
- DORA · CoARA · Leiden Manifesto
- COPE/DOAJ/OASPA/WAME — *Principles of Transparency and Best Practice in Scholarly Publishing*
- cOAlition S — Plan S, Rights Retention Strategy

## Veri kaynakları

**MCP:** TR Legal MCP (Mevzuat + Yargı) · CourtListener (Free Law Project) · Fedlex ·
OpenCaseLaw.ch

**Ücretsiz REST:** Crossref · OpenAlex · Semantic Scholar · DOAJ · ORCID · EUR-Lex · HUDOC

> **Bu paket hiçbir API anahtarı içermez.**

## Önemli

Bu paket **gerçek kişi veya kurum verisi içermez**. Tüm örnekler kurgusaldır; profil
alanları `[DOLDUR]` yer tutucularıyla gelir.

Çıktılar daima **taslaktır**. **Üretken yapay zekâ yazar olamaz** ve hukuki veya etik
anlamda sorumlu tutulamaz; yazarlık ve sorumluluk yazardadır. Bu araçtan yararlanılması,
ilgili dergi / kurum / fon sağlayıcının öngördüğü biçimde **beyan edilmelidir**.

Değerlendirme altındaki yayımlanmamış müsvedde, proje önerisi veya tez metni bu asistana
**girilemez** — gizlilik yükümlülüğünün ihlalidir.
