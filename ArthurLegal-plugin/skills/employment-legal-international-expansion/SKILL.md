---
name: employment-legal-international-expansion
description: >
  Referans: sınır ötesi işe alım için uygulama planı çerçevesi — iki yön: (A) Türk
  işverenin yurt dışında işe alımı ya da personel göndermesi, (B) yabancı işverenin
  Türkiye'de işe alımı. Yapı seçeneklerinin çerçevelenmesi (Türkiye'de ABD tarzı EOR
  yerine İş K. m. 7 sınırları), Türkiye ilk gün yükümlülükleri (sözleşme, SGK, çalışma
  izni, KVKK aktarımı), ArthurLegal MCP ile yabancı mevzuat araması, vergi/finans/İK
  soruları, yerel avukat brif talebi ve kalıcı takip dosyası. /expansion-kickoff ve
  /expansion-update tarafından yüklenir; doğrudan çağrılmaz.
user-invocable: false
---

# Uluslararası Genişleme — Ortak Çerçeve

## Matter bağlamı

Uygulama CLAUDE.md'sinde `## Matter workspaces` bölümüne bak. `Enabled` `✗` ise bu paragrafın gerisini atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:employment-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Sınır ötesi işe alım dağınık yürür: hukuk iş hukuku sorularını bilir ama vergi bakımından işyeri riskini bilmez; finans maliyeti bilir ama çalışma izni süresini bilmez; İK ücreti bilir ama ilk gün tescil yükümlülüklerini bilmez. Bu skill haritayı çıkarır, her paydaşa doğru soruyu taslaklar, yerel avukata brif hazırlar ve oturumlar arası süren bir takip dosyası kurar. Genişleme kararı verilmiş varsayılır; "genişlemeli miyiz?" çerçevesi değildir.

**Kaynak kuralı.** Türkiye kuralları `tr_mevzuat_madde_getir` ile doğrulanmış maddelere dayanır; uygularken metni yeniden çek ve değişiklik dipnotlarını oku. Yabancı ülke kuralı **ezberden yazılmaz**: ArthurLegal MCP'nin ulaştığı ülkelerde araçla aranır; diğerlerinde "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al". Araç sonucu olsa bile her ülke için yerel avukat brifi gönderilir — uygulama bilgisi ve güncellik onunla teyit edilir.

## Bağlam ve üst başlık

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → eşik tablosu (yurt dışı satırları dahil), eskalasyon, önceki genişleme notları. Her çıktı `## Outputs` başlığıyla açılır.

## Adım 0 — Yön

> Hangi yön?
> - **A — Türkiye'den dışarı:** [Müvekkil] yurt dışında işe alıyor ya da Türkiye'deki personelini yurt dışına gönderiyor.
> - **B — Dışarıdan Türkiye'ye:** yabancı işveren Türkiye'de işe alıyor ya da yabancı uyruklu personel Türkiye'de çalışacak.

İkisi birlikte olabilir; her ülke-yön çifti ayrı takip dosyasıdır.

## Adım 1 — Bilgi toplama (tek blokta sor, cevap bekle)

> Planı kurmadan önce genişlemenin şeklini anlamam gerekiyor; cevaplayamadıklarınız da bilgi verir:
>
> **Genişleme** — Hangi ülke? Hangi roller (satış kapatan biri ile kod yazan mühendis farklı risk doğurur)? 12 ayda kaç kişi? İlk kişi ne zaman başlamalı? Çalışanların uyruğu (Türk, yerel, üçüncü ülke)?
>
> **Mevcut durum** — O ülkede şirket/şube var mı? Aynı grupta orada ya da Türkiye'de şirket var mı? Aracı (EOR) ya da özel istihdam bürosu düşünülüyor mu? Vergi/finans haberdar mı? Yerel avukat var mı?
>
> **Yapı** — Yerel işe alım mı, Türkiye'den (ya da ana şirketten) geçici görevlendirme mi; ne kadar süre?
>
> **Stratejik bağlam** — Kalıcı ekip mi, pazar testi mi? Yapı kararını hangi yönetici verecek?

## Adım 2 — Yapı seçenekleri (karar verme, çerçevele)

Kararı CFO ve vergi ekibinin verebileceği netlikte çerçevele.

| Faktör | Aracı modeli lehine | Şirket/şube lehine |
|---|---|---|
| 12 aylık kişi sayısı | Az | Çok |
| İlk işe alıma kalan süre | Kısa | Uzun |
| Stratejik bağlılık | Pazar testi | Kalıcı varlık |
| Maliyet | Aracı payı kabul edilebilir | Ölçek şirketi verimli kılar |
| Kontrol ihtiyacı | Düşük | Yüksek — doğrudan işveren ilişkisi |
| Fikri hak hassasiyeti | Düşük | Yüksek — sahiplik daha temiz |

Başa baş sayısı, aracı payı, kuruluş maliyeti ve süresi ülkeye ve sağlayıcıya göre değişir — sabit yazma; vergi/finans ve sağlayıcıya sor.

### B yönü — Türkiye'de yapı seçenekleri

| Seçenek | Ne gerektirir | Dikkat |
|---|---|---|
| Türkiye'de şirket/şube kurup doğrudan istihdam | Şirket kuruluşu (kurumsal ekip); işyeri bildirimi ve SGK tescili (Adım 4B) | Asıl yol; eşikler işçi sayısıyla büyür |
| Grup şirketinden geçici devir | Türkiye'de grup şirketi varsa: devir sırasında işçinin yazılı rızası; yazılı olarak en çok altı ay, en fazla iki yenileme; devreden işverenin ücret ödeme yükümlülüğü sürer, devralan ödenmeyen ücret ve prim için birlikte sorumlu (İş K. m. 7 son fıkra) | Yalnız holding ya da aynı şirketler topluluğu içinde |
| Özel istihdam bürosu üzerinden geçici işçi | İŞKUR izinli büro; yalnız m. 7/2'de sayılan hâllerde; (a)-(c) dışındaki hâllerde en fazla dört ay, (g) hariç toplam sekiz ayı geçmemek üzere en fazla iki yenileme; işveren özel istihdam bürosudur (İş K. m. 7) | **ABD tarzı süresiz EOR'un Türkiye'de doğrudan karşılığı yok.** Sürekli işi bu yolla gördürmek m. 7 sınırlarını aşar; gerçek işverenin kim sayılacağı riski — tartışmalı, içtihadı kontrol et |
| Yabancı şirketin Türkiye'de tüzel kişilik/şube olmadan işçi çalıştırması | SGK işyeri tescili, bordro ve vergi uygulaması | Uygulamada sorunlu — SGK/vergi uzmanıyla teyit et; tartışmalı |
| Serbest meslek / yüklenici | Gerçek bağımsızlık | Bağımlı çalışma varsa iş sözleşmesidir (İş K. m. 8 tanımı) → `/arthurlegal:employment-legal-worker-classification` |

```
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="geçici iş ilişkisi özel istihdam bürosu muvazaa")
```
Dönen kararların künyesini birebir kullan; karar numarası ezberden yazma.

### A yönü — Türkiye'den dışarı

- **Yerel işe alım** (hedef ülkedeki şirket ya da aracı): hedef ülke hukuku — Adım 4A.
- **Türkiye'den personel götürme:** İŞKUR'dan izin almadan kendi işlerinde çalıştıracakları işçileri yurt dışına götürenlere ve Kuruma onaylatılmayan her yurt dışı hizmet akdine idari para cezası öngörülür (4904 s. Kanun m. 20/1-g). İzin usulünü ilgili yönetmelikte bul: `tr_mevzuat_ara(query="yurt dışına işçi", types=["YONETMELIK"])`. Ceza tutarlarını yazma — yeniden değerleme ile güncellenir, teyit et.
- **Sosyal güvenlik:** hedef ülkeyle ikili sosyal güvenlik sözleşmesi var mı: `tr_mevzuat_ara(query="sosyal güvenlik sözleşmesi [ülke]")`. Yoksa çifte prim riski → finans.

### Uygulanacak hukuk ve yetki (her iki yön)

- Taraflar hukuk seçebilir; ancak işçinin mutad işyeri hukukunun emredici hükümlerinin sağlayacağı asgari koruma saklıdır. Seçim yoksa işçinin işini mutad olarak yaptığı işyeri hukuku uygulanır; başka ülkede geçici çalışma mutad işyerini değiştirmez; devamlı birden fazla ülkede çalışmada işverenin esas işyeri hukuku; hâlin bütün şartlarına göre sözleşmeyle daha sıkı ilişkili bir hukuk varsa — işin yapıldığı yerin zorunlu uygulanan hükümleri saklı kalmak üzere — o uygulanabilir (MÖHUK m. 27). **m. 27, 4/6/2025 tarihli 7550 s. Kanunla değişti — eski metne dayanan kaynak ve şablonları kullanma.**
- Türk mahkemesinin yetkisi: mutad işyeri Türkiye'deyse orası; işçinin işverene karşı davasında işverenin ya da işçinin Türkiye'deki yerleşim yeri veya mutad meskeni mahkemesi de yetkilidir (MÖHUK m. 44).

### Vergi bakımından işyeri riski (vergi ekibine)

Satış, iş geliştirme, müşteri yönetimi ya da şirket adına sözleşme müzakere/imza yetkisi olan roller varsa açıkça işaretle:

> **İşyeri riski:** [rol], [ülke]de şirket kurulmadan vergi bakımından işyeri ya da daimi temsilci doğurabilir. Bu iş hukuku değil vergi sorusudur; ilk işe alımdan önce vergi ekibi değerlendirmeli (`tax-legal` eklentisi), çifte vergilendirmeyi önleme anlaşması kontrol edilmeli.

## Adım 3 — Paydaşlar: ne yapacaklar, hukuk ne soracak

"Finansa haber verin" deme; soruyu taslakla.

**CFO / vergi** (ilk işe alımdan önce zorunlu) — yapı ekonomisi, işyeri analizi, pay/opsiyon vergisi.
- 12 ayda [N] kişide, aracı payı, kuruluş maliyeti ve uyum yükü hesaba katıldığında hangi sayıda şirket kurmak daha ekonomik? Aracıdan şirkete geçişte mevcut çalışanların devri nasıl olur (B yönünde m. 7 süre sınırları)? Sağlayıcının yerel uyum geçmişi incelendi mi?
- [Rol] [ülke]de şirket kurulmadan işyeri ya da vergisel bağ doğurur mu; doğurursa şirket takvimi değişir mi? Soru çözülmeden işe alırsak risk penceresi ne?
- Pay/opsiyon planımız [ülke]de nasıl vergilenir; çalışana tahsis ve hak edişte yerel danışman gerekir mi?
- Şirket kurulursa ana şirketle hangi grup içi hizmet sözleşmesi ve transfer fiyatlandırması gerekir? (`/arthurlegal:tax-legal-transfer-pricing-review`)

**Finans / bordro** (ilk maaştan önce) — bordro sağlayıcı, zorunlu işveren katkıları, banka.
- Yerel bordro sağlayıcı belli mi (aracıysa sosyal katkılar dahil bordroyu üstleniyor mu)?
- Zorunlu işveren katkıları (emeklilik, sosyal sigorta, sağlık) ücret modelinde var mı? Oranları sabit yazma; güncel oranı teyit et. B yönünde SGK primleri dahil.
- Pay planında hak edişte işveren tarafı vergi kesintisi modellendi mi?

**İK / ücret ve yan haklar** (teklif öncesi) — yan hak ve ücret karşılaştırması, zorunlu ve piyasa standardı haklar.
- [Ülke]de hangi haklar kanunen zorunlu, hangileri piyasa standardı? (Zorunludan az ya da piyasadan fazla vaat etmeyelim.)
- Standart pay paketimiz bu pazarda rekabetçi mi?
- Günlük yönetici yerel mi, merkezden uzaktan mı? (Bazı ülkelerde temsil ve sözleşme şartlarını etkiler.)

**Yerel avukat** (zorunlu — atlanmaz): Adım 4A'daki brif bu işin gündemidir; baştan tek seferde gönder.

**B yönünde Türk hukuku ekibi:** Adım 4B kontrol listesi.

## Adım 4A — Yabancı ülke: önce ArthurLegal, sonra yerel avukat

| Ülke | Önek | Başlangıç çağrısı |
|---|---|---|
| AB üyesi (ortak çerçeve) | `eu_` | `eu_search_eu_law(query="transparent and predictable working conditions")` → `eu_get_document_text(celex="32019L1152")`; gönderme: `eu_search_eu_law(query="posting of workers")`; uygulanacak hukuk: `eu_search_eu_law(query="law applicable to contractual obligations")`; çalışan verisi: `eu_search_eu_law(query="protection of natural persons processing of personal data")` |
| Almanya | `de_` | `de_norm_getir(kanun="KSchG", norm="1")` (fesih koruması); `de_gesetz_ara(sorgu="Nachweisgesetz")`; işyeri temsili: `de_norm_getir(kanun="BetrVG", norm="1")`; içtihat: `de_rii_case_search(query={"court": "BAG", "date_from": "2022-01-01"})` |
| Birleşik Krallık | `uk_` | `uk_search_legislation(title="Employment Rights Act", type="ukpga")`; `uk_get_section(year="1996", number="18", section="94")`; alıntıdan önce `uk_get_effects` |
| Hollanda | `nl_` | `nl_search_legislation(query="Burgerlijk Wetboek Boek 7")` |
| Polonya | `pl_` | `pl_search_by_title(title="Kodeks pracy", in_force_only=true)` → `pl_get_act_text(publisher="DU", year=..., pos=...)` (güncel birleştirilmiş metni sonuçlardan seç) |
| Avusturya | `at_` | `at_search_legislation(title="Arbeitsverfassungsgesetz")`; konu araması: `at_search_legislation(terms="Kündigung Arbeitnehmer")` |
| İrlanda | `ie_` | `ie_search_acts(query="unfair dismissals")` → `ie_get_section(year=..., number=..., section=...)` |
| Finlandiya | `fi_` | `fi_search_acts(query="työsopimuslaki")` → `fi_get_act(year=..., number=...)` |
| İspanya | `es_` | `es_search_legislation(query="Estatuto de los Trabajadores", only_in_force=true)` → `es_get_act_text(boe_id=...)` |
| Japonya | `jp_` | `jp_search_laws(keyword="労働基準法")` (law_id `322AC0000000049`) → `jp_get_article(law_id="322AC0000000049", article=...)`; ayrıca `jp_search_laws(keyword="労働契約法")` |
| Azerbaycan | `az_` | `az_search_acts(query="Əmək Məcəlləsi", types=[107])` → `az_get_act_fulltext(act_id=...)` |
| Diğer tüm ülkeler (ABD, BAE, İsviçre, Rusya …) | — | **ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al.** (ABD için yalnız kuruluysa üçüncü taraf CourtListener bağlayıcısı.) |

Kurallar: sonuç ince görünürse önce `status` çağır (yüklenmemiş kaynak ≠ boş sonuç). Dizin kapsamı yıl aralığıyla sınırlı araçlarda (`ie_`, `fi_`, `pl_search_indexed`) kapsamı rapora yaz. Aracın döndürdüğü atıf ve bağlantıyı birebir kullan; veri gelmezse "UYARI: veri çekilemedi, teyidiniz gerekli: <aracın source_url'si>". Sağlayıcı ya da grup şirketi kimliği için `gleif_search_entities(name="[tam unvan]", jurisdiction="[ISO kodu]")`.

**Yerel avukat brif talebi — [Ülke]** (takip dosyasına tek açık kalem: sahibi Yerel avukat, sorular alanında brifin tamamı; ülke daha önce sorulduysa yine gönder — bu bir güncellik kontrolüdür):

> [Ülke]de [tarih]ten itibaren [roller] için [N] kişi istihdam etmeyi planlıyoruz; 12 ay hedefi [N]. Tercih edilen yapı (görüşünüze ve vergi ekibine bağlı): [aracı / şirket / görevlendirme / belirsiz]. Lütfen her soruyu birincil kaynak atfıyla, tablo değil soru-cevap olarak yanıtlayın — değişiklikleri izleyebilmek istiyoruz:
> 1. **Yapı** — şirket, aracı, yüklenici seçenekleri ve bu sayı ve roller için ödünleşim.
> 2. **Sözleşme** — zorunlu şekil ve içerik, geçersiz hükümler, dil/çeviri şartı.
> 3. **Fesih** — bildirim süresi ve tazminat, korunan sebepler, toplu çıkarmada seçim kuralları; ilk günden kurulacak belge standardı.
> 4. **Zorunlu haklar ve işveren katkıları** — emeklilik, sosyal sigorta, sağlık, ücretli izin, ikramiye; güncel oranlar ve dayanak.
> 5. **Rekabet yasağı, gizlilik, fikri haklar** — geçerlilik şartları, tazminat zorunluluğu.
> 6. **Çalışan temsili** — işyeri konseyi, sendika, toplu sözleşme; hangi sayıda tetiklenir; sendikasız olsak da sektörel sözleşmeye tabi miyiz?
> 7. **Çalışan verisi** — yerel yükümlülükler ve Türkiye'ye veri aktarım mekanizması.
> 8. **Çalışma ve oturma izni** — Türk ve üçüncü ülke vatandaşları için izin türleri ve süreler.
> 9. **Sektörel kurallar.**
> 10. **Yüklenici sınıflandırması** — ölçüt ve yeniden nitelendirme riski.
> 11. **Pay/opsiyon** — yerel vergi, sermaye piyasası ve iş hukuku kuralları.
> 12. **İlk gün uyumu** — tescil, bildirim, ilan yükümlülükleri.
> 13. **Bu ülkede ilk kez işe alan Türk işverenleri en çok neyi şaşırtıyor** ve yakın zamanda ne değişti?

A yönünde Türk tarafında ayrıca: KVKK m. 9 (çalışan verisinin yurt dışına aktarımı — aşağıdaki 4B/7. satır), MÖHUK m. 27 hukuk seçimi klozu, 4904 m. 20 İŞKUR izni.

## Adım 4B — Türkiye (B yönü): ilk gün kontrol listesi

| # | Kalem | Dayanak | Sahibi |
|---|---|---|---|
| 1 | İş sözleşmesi — süresi bir yıl ve daha fazla olan sözleşme yazılı; yazılı sözleşme yoksa en geç iki ay içinde çalışma koşullarını gösteren yazılı belge | İş K. m. 8 | Hukuk |
| 2 | İşyeri bildirimi — işyerini kuran işveren bir ay içinde bölge müdürlüğüne; şirketlerde tescil kaydı ticaret sicilinin gönderdiği belgelerle | İş K. m. 3 | Hukuk / kurumsal |
| 3 | SGK işyeri bildirgesi — en geç sigortalı çalıştırmaya başlanan tarihte; şirket kuruluşunun ticaret siciline bildirimi SGK'ya yapılmış sayılır | 5510 m. 11 | Bordro |
| 4 | Sigortalı işe giriş bildirgesi — sigortalılık başlangıcından önce (kanundaki istisnalar saklı) | 5510 m. 8 | Bordro |
| 5 | Yabancı çalışan — çalışma izni olmaksızın çalışma ve çalıştırma yasak; başvuru yurt içinde Bakanlığa, yurt dışında konsolosluğa; belgeler tamsa otuz günde değerlendirme; ilk izin en çok bir yıl ve belirli işyeri için; yabancı ortak-müdür/YK üyesi izinle çalışabilir; nitelikli işgücü, proje çalışanı, AB vatandaşı gibi istisnai kategoriler | 6735 m. 6, 7, 10, 16 | İK / hukuk |
| 6 | İzinsiz çalıştırma yaptırımı — idari para cezası (tutarları teyit et — yeniden değerleme), sınır dışı ve dönüş masraflarının işverence karşılanması | 6735 m. 23 | Hukuk |
| 7 | Çalışan aydınlatması ve ana şirkete veri aktarımı — yeterlilik kararı yoksa uygun güvence: standart sözleşme (imzadan itibaren beş iş günü içinde Kuruma bildirim), bağlayıcı şirket kuralları ya da diğer m. 9 yolları | KVKK m. 10, m. 9 | Hukuk / uyum |
| 8 | Uygulanacak hukuk ve yetki klozu | MÖHUK m. 27, m. 44 | Hukuk |
| 9 | Büyüme eşikleri — 30 işçi iş güvencesi (m. 18), toplu işçi çıkarma (m. 29), 50 işçi engelli kontenjanı (m. 30); CLAUDE.md eşik tablosuna satır ekle | İş K. | Hukuk / İK |
| 10 | Uyuşmazlıkta arabuluculuk dava şartı | 7036 m. 3 | Hukuk |
| 11 | Vergi, SGK prim oranları, asgari ücret, kıdem tazminatı tavanı — sabit yazma; güncel değeri teyit et | — | Finans |

Açık sorular (Türk hukuku ekibi + SGK/vergi uzmanı): şube mi şirket mi; tüzel kişilik kurulmadan istihdamın SGK ve vergi uygulaması; grup içi geçici devirde ücretin hangi şirketten ödeneceği ve bordro düzeni.

## Adım 5 — Takip dosyası

Yol: matter workspace kapalıysa `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-<ulke-slug>.yaml`; açıksa aktif matter klasöründe aynı ad. Dosya oturumlar arası kalır. Adım 2-4'te çıkan her eylem **ayrı kalem** olur; her kalem tek sahibe atanır ve tamamlanabilir olur.

```yaml
# [ÜST BAŞLIK — CLAUDE.md ## Outputs]
ulke: [ad]
ulke_slug: [kucuk-harf-tireli]
yon: [TR-yurtdisi | yurtdisi-TR]
arthurlegal_kaynak: [eu_ / de_ / ... | yok — yerel hukukçu]
baslangic: [ISO tarih]
ilk_ise_alim_hedefi: [ISO tarih | belirsiz]
kisi_12_ay: [N]
roller: [liste]
stratejik: [test | kalici]
yapi: [sirket | grup-ici-devir | ozel-istihdam-burosu | araci | yuklenici | belirsiz]
yerel_avukat: [true | false]
vergi_isyeri_riski: [true | false]
son_guncelleme: [ISO tarih]

acik_kalemler:
  - id: 1
    kategori: [yapi | vergi | finans | ik | yerel-avukat | uyum | izin]
    kalem: "[ne yapılacak]"
    sahibi: "[birim ya da kişi]"
    durum: [acik | devam | tamam | blokeli]
    son_tarih: [ISO tarih | null]
    bagimli_oldugu: []        # önce kapanması gereken kalem id'leri
    dayanak: "[doğrulanmış madde ya da araç sonucu atfı]"
    sorular:
      - "[Adım 2-4'te taslaklanan soru]"
    notlar: ""
```

## Adım 6 — Çıktı

> **Yargı çevresi varsayımı.** Bu plan ön görüşmedeki tek ülke ve yön içindir. Yerel iş hukuku, vergi, çalışan temsili ve veri koruma kuralları ülkeye, bölgeye, sektöre ve kişi sayısına göre değişir ve sık değişir. Yabancı ülkeye ilişkin esaslı cevap ArthurLegal araç sonucundan ve yerel avukat brifinden gelir; bu skill'in kendi bilgisinden gelmez. Plan başka ülkeye uyarlanırsa brifi yeniden gönder.

```markdown
[ÜST BAŞLIK — CLAUDE.md ## Outputs]
## Uluslararası Genişleme: [Ülke] ([yön]) — [Tarih]
**İlk işe alım hedefi:** [tarih] · **12 ay:** [N] kişi · **Roller:** [liste]
**ArthurLegal kaynağı:** [önek | yok — yerel hukukçu] · **Takip dosyası:** [yol]
⚠️ İnceleyen notu: doğrulanamayan madde / çekilemeyen yabancı kaynak: [liste | yok] · tartışmalı: [liste]

### Yapı seçenekleri — [Adım 2 tablosu; B yönünde m. 7 notu; işyeri riski işareti]
### Uygulanacak hukuk ve yetki — [MÖHUK m. 27 / m. 44 özeti; önerilen klozun ana hatları]
### Kimler devreye girmeli — Vergi [N] soru · Finans/bordro [N] · İK [N] · Yerel avukat (brif aşağıda)
### [A yönü] ArthurLegal notları + yerel avukat brifi — [çağrılar, dönen atıflar; brifin tamamı]
### [B yönü] Türkiye ilk gün kontrol listesi — [Adım 4B tablosu, doğrulama tarihiyle]
### Açık kalemler ([N])
| # | Kalem | Sahibi | Durum | Son tarih |
|---|---|---|---|---|

Kalemler kapandıkça `/arthurlegal:employment-legal-expansion-update [ülke]` çalıştırın.
```

## Bu skill ne yapmaz

- Yabancı ülkenin iş hukuku hakkında kendi bilgisinden kural söylemez — ArthurLegal aracı ve yerel avukat brifi üzerinden gider.
- Yapı kararını vermez — doğru karar vericiler için çerçeveler.
- Yerel iş sözleşmesini yazmaz — yerel avukatın yazması gerektiğini işaretler. (B yönünde Türk iş sözleşmesi için `/arthurlegal:employment-legal-hiring-review`.)
- Yerel avukatın yerini tutmaz — ArthurLegal'ın kaynağı olan ülkelerde de her yeni ülke yerel teyit ister.

---

## Kaynak katmani — /legal-research (v1.4.0)

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur —
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
