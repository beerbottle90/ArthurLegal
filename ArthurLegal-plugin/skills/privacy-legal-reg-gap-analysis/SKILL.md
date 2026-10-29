---
name: privacy-legal-reg-gap-analysis
description: >
  Yeni ya da değişen bir düzenlemeyi (KVKK değişikliği, yönetmelik, tebliğ, Kurul
  kararı, sektör kuralı ya da yabancı rejim) mevcut aydınlatma metinleri ve
  uygulamayla karşılaştırır; açık listesi ve sorumlu ile tarih içeren düzeltme
  planı üretir. Yeni bir düzenleme çıktığında, "[düzenleme] bizi etkiliyor mu",
  "[yönetmelik] için açık analizi", "KVKK uyum kontrolü" denince ya da düzenleme
  metni yapıştırıldığında kullan.
argument-hint: "[düzenleme adı ya da künyesi, veya metni yapıştırın]"
---

# /reg-gap-analysis

1. Profili yükle: aydınlatma taahhütleri, yükümlülük haritası, başvuru sistemleri.
2. Kapsam: düzenleme bize uygulanır mı (kişi, sektör, eşik, istisna, yürürlük)?
3. Gereklilikleri araçla çek → mevcut durumla karşılaştır → açık listesi.
4. Önceliklendir; sorumlu ve tarihli düzeltme planı yaz.
5. Tarihli belge olarak kaydet. "Açık yok" sonucu da belgelenir.

```
/arthurlegal:privacy-legal-reg-gap-analysis "Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik"
/arthurlegal:privacy-legal-reg-gap-analysis
[Kurul kararı ya da düzenleme metni]
```

---

# Düzenleme–Uygulama Açık Analizi

## Amaç

Bir şey değişir — kanun değişikliği, yeni yönetmelik, Kurulun ilan ettiği standart sözleşme ya da yeni bir karar özeti — ve neyi değiştirmeniz gerektiğini bilmeniz gerekir. Bu skill yeni gerekliliği mevcut uygulamayla (profil → `## Privacy policy commitments`, `## Regulatory footprint`, `## DSAR process` ve PIA'larda belgelenen uygulamalar) karşılaştırır, açık listesi ve düzeltme planı üretir. `/policy-monitor --mevzuat` tespit eder; analiz burada yapılır.

## Mevcut durumu yükle

`~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`: aydınlatma taahhütleri, yükümlülük haritası (VERBİS, aktarım yolları, sektör, yabancı rejim), başvuru sistemleri listesi. Düzenleme size uygulanmıyorsa analiz tek satırdır: "Uygulanmaz. Nedeni: [gerekçe]. İşlem gerekmez." — yine kaydet.

## Adım 1 — Kapsam

- **Uygulanır mı?** Kişi (veri sorumlusu / veri işleyen — 7499 sonrası yurt dışı aktarım ve standart sözleşme bildirimi veri işleyeni de doğrudan bağlar: KVKK m. 9/1, 9/5, 18/1-d ve 18/2), sektör, eşik, istisna. Kanunun hiç uygulanmadığı hâller ile aydınlatma (m. 10), haklar (m. 11, tazminat hariç) ve VERBİS (m. 16) hükümlerinin uygulanmadığı hâller ayrıdır (KVKK m. 28/1, 28/2) — hangisine girdiğini ayrı yaz. VERBİS istisnası Kurul kararıyla belirlenir ve diğer yükümlülükleri kaldırmaz (KVKK m. 16/2; Veri Sorumluları Sicili Hakkında Yönetmelik m. 5/1-f, 16).
- **Ne zaman?** Yürürlük tarihi, geçiş hükmü. Örnek: 7499 s. Kanunla değişen m. 9 yürürlüğe girdi; eski m. 9/1 değişik hâliyle birlikte 1/9/2024'e kadar uygulanmaya devam etti; 1/6/2024 itibarıyla sulh ceza hâkimliklerinde görülen başvurular orada görülmeye devam eder (KVKK geçici m. 3). Yürürlük maddesini metinden çek (ör. Yurt Dışına Aktarım Yönetmeliği m. 18: yayımı tarihinde).
- **Gerçekten yeni olan ne?** Tüm metni değil, zaten uyduğunuz şeyden farkı (delta) çıkar. GDPR'a uyuyor olmak KVKK'ya uyduğunuz anlamına gelmez; farkı her kalemde ayrıca kontrol et.

## Adım 2 — Gereklilikleri çıkar (araçla)

Metni ezberden özetleme; çek:
- Bul: `tr_mevzuat_ara(query="<başlıktan kelimeler>", types=["KKY", "TEBLIGLER"])` (KVKK yönetmelikleri `KKY`, tebliğler `TEBLIGLER` türündedir; kanun için `types=["KANUN"]`).
- Oku: `tr_mevzuat_madde_getir(mevzuat_id="<id>", madde_no=["5", "6", ...])` (en çok 10). Madde ağacı yoksa (`tr_mevzuat_icindekiler` hata verebilir) tam metin: `tr_mevzuat_getir(mevzuat_id="<id>")`.
- Kurul kararı / ilan: `tr_semantik_ara(kurum="kvkk", query="<konu>")`, `tr_kurum_karari_ara(kurum="kvkk", query="<konu>", params={"scan_pages": 5})`, `tr_kurum_karari_getir(kurum="kvkk", id="<id>")`; Resmî Gazete'de yayımlananlar için `tr_resmi_gazete_tara(date_from, date_to, query="Kişisel Veri")`.
- Sektör: `tr_kurum_karari_ara(kurum="bddk" | "btk", query=...)`, ilgili kanun maddesi `tr_mevzuat_madde_getir`.

| # | Gereklilik | Atıf (araçtan dönen `citation`) | Kategori |
|---|---|---|---|

**Kategoriler:** Aydınlatma · Haklar ve başvuru · Güvenlik ve ihlal · Veri işleyen ve aktarım · Rıza · Kayıt ve yönetişim (VERBİS, envanter) · Saklama ve imha.

### Çapa kontrol listesi (doğrulanmış; karşılaştırmanın tabanı)

| Alan | Doğrulanmış kural |
|---|---|
| İlkeler | Hukuka ve dürüstlüğe uygunluk, doğruluk, belirli/açık/meşru amaç, amaçla bağlantılı-sınırlı-ölçülü olma, gerekli süre kadar muhafaza (KVKK m. 4/2). |
| Hukuki sebep | Kural açık rıza; m. 5/2'deki şartlardan biri varsa aranmaz (m. 5). Özel nitelikli veri yasak; m. 6/3 hâllerinde ve Kurulun yeterli önlemleriyle (m. 6/3-4). |
| Aydınlatma | Asgari içerik (m. 10; Aydınlatma Tebliği m. 4); her işlemede, amaç değişince önceden ayrıca; talebe bağlı değil; ispat veri sorumlusunda; açık rızadan ayrı; hukuki sebep ve alıcı grupları açıkça; anlaşılır ve sade dil (Tebliğ m. 5/1). Veri ilgili kişiden alınmadıysa makul süre / ilk iletişim / en geç ilk aktarım (Tebliğ m. 6). |
| Haklar ve başvuru | m. 11 hakları; en geç otuz gün, kural olarak ücretsiz (m. 13/2); Türkçe başvuru, kanallar, cevabın asgari içeriği, ücret (Başvuru Tebliği m. 4-7); şikâyet süreleri (m. 14). |
| Güvenlik ve ihlal | Teknik ve idari tedbir; veri işleyenle müşterek sorumluluk; iç denetim; ihlalde en kısa sürede ilgilisine ve Kurula bildirim (m. 12). |
| Aktarım | Genel kural: açık rıza ya da m. 5/2 şartları; özel nitelikli veride yeterli önlemlerle m. 6/3 şartları (m. 8). Yurt dışı: yeterlilik kararı → uygun güvence → arızi istisna; standart sözleşme beş iş günü içinde bildirim; sonraki aktarımlarda da aynı güvenceler (m. 9). Usul: Yurt Dışına Aktarım Yönetmeliği m. 5-7, 14 (standart sözleşme değiştirilmeden kullanılır, bildirim usulü), 15 (taahhütnamede Kurul izni), 16 (arızi: düzenli olmayan, tek veya birkaç sefer, süreklilik arz etmeyen). |
| Kayıt ve yönetişim | Veri işlemeye başlamadan önce VERBİS kaydı; Kurul istisnası (m. 16); envanter, irtibat kişisi, değişiklikte yedi gün (Sicil Yönetmeliği m. 5, 11, 13). |
| Saklama ve imha | Sebep ortadan kalkınca silme/yok etme/anonimleştirme (m. 7); kayıt yükümlüsü için saklama ve imha politikası (Silme Yönetmeliği m. 5-6); işlem kayıtları en az üç yıl (m. 7/3); periyodik imha en fazla altı ay, politikası olmayan için üç ay (m. 11); talep hâlinde otuz gün (m. 12). |
| Yaptırım | İdari para cezaları: aydınlatma, veri güvenliği, Kurul kararına uymama, VERBİS, standart sözleşme bildirimi (KVKK m. 18/1 a-d — kanun metnindeki aralıklar; güncel tutarı teyit et, dönemsel güncellenir); cezaya karşı idare mahkemesi (m. 18/3). Suçlar için TCK 135-140; silmeyen/anonimleştirmeyen TCK 138'e göre (KVKK m. 17). |
| Sektör | Bankacılık müşteri sırrı (5411 m. 73/3); elektronik haberleşme (5809 m. 51); sağlık (Kişisel Sağlık Verileri Hakkında Yönetmelik — madde atfı için önce çek). |

## Adım 3 — Mevcut durumla karşılaştır

```markdown
### Gereklilik #N: [kısa ad]
**Düzenleme diyor ki:** [alıntı ya da yakın özet + atıf]
**Bizde şu an:** [profil / aydınlatma metni / uygulama ne gösteriyor]
**Açık:** [Yok | Kısmi | Tam]
**Eksik olan (kısmi/tam ise):** [somut]
**Kapatma eforu:** [Yalnız metin | Ürün değişikliği | Sözleşme yeniden müzakeresi | Yeni süreç | Kuruma bildirim/başvuru]
**Uyumsuzluk riski:** [yaptırım türü ve dayanağı; Kurulun yakın kararlarında görülen eğilim — araçtan; itibar]
```

## Adım 4 — Önceliklendir

1. **Dişli son tarih** — yürürlük + yaptırım + kısa süreli yükümlülük (ör. standart sözleşme bildirimi, VERBİS değişikliği).
2. **Efor/etki oranı** — metin güncellemesi ucuz, ürün yeniden yapımı pahalı.
3. **Yarısı yapılmış olan** — mevcut uyum (GDPR dahil) farkı küçültebilir, ama farkı kalem kalem göster.

## Adım 5 — Düzeltme planı

Profildeki `## Outputs` üst başlığını ekle (role göre değişir).

**Araştırma bağlantısı ön kontrolü.** Planı yazmadan önce bu oturumda ArthurLegal MCP'nin cevap verip vermediğini kontrol et. Vermediyse inceleyen notunun **Kaynaklar:** satırına yaz: "ArthurLegal MCP bağlı değil — atıflar model bilgisinden; önce yürürlük/geçiş tarihlerini, madde-fıkra-bent numaralarını ve Kurul kararı künyelerini kontrol edin." Satır içi etiketler kalır; çıktının üstüne ayrı afiş koyma.

```markdown
[ÜST BAŞLIK — ## Outputs]

## Düzeltme Planı: [düzenleme — künye]
**Yürürlük:** [tarih — maddeden] · **Geçiş hükmü:** [varsa]

### Yürürlükten / son tarihten önce yapılacaklar
| Açık | Çözüm | Sorumlu | Son tarih | Durum |
|---|---|---|---|---|

### Yapılması iyi olanlar (engelleyici değil)
[aynı tablo]

### Zaten uyumlu
[açık = Yok olan gereklilikler]

### Kabul edilen açıklar (risk kabul edildi)
[gerekçe ve riski kabul eden kişi]

> ⚠️ **İnceleyen notu** — Kaynaklar: [araçlar / bağlı değil]. Tartışmalı noktalar: [liste]. Avukat incelemesi olmadan dışa gönderilmez.
```

## Kaynak etiketleri ve sessiz tamamlama yasağı

Her atfı kaynağıyla etiketle; etiketleri silme ya da birleştirme:
- `[ArthurLegal TR — <citation> — GG.AA.YYYY]` — `tr_` aracından birebir.
- `[eu_ — CELEX <no>]`, `[uk_ — <citation>]` — yabancı rejim araçlarından.
- `[kullanıcı verdi]` — kullanıcının sağladığı metin.
- `[model bilgisi — doğrula]` — araçla doğrulanamayan; tarih, eşik, yürürlük, Kurul kararı.
- `[model bilgisi — doğrula-pinpoint]` — fıkra/bent numarası; en yüksek uydurma riski, her zaman birincil kaynakla kontrol.
- `[web — doğrula]` — yalnız kullanıcı izin verdiyse.

**Sessiz tamamlama yok.** Araç bir düzenleme ya da karar için az veya hiç sonuç döndürürse bulduğunu söyle ve dur: "[araç] [N] sonuç döndürdü; [konu] için kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç (`tr_semantik_ara`, `tr_resmi_gazete_tara`), (3) web araması — sonuçlar `[web — doğrula]` etiketli, (4) doğrulanmadı diye işaretle ve dur. Hangisi?" Çekilemeyen maddeye: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`; Kurul kararına aracın `source_url`'si ya da https://www.kvkk.gov.tr/Icerik/5406/kurul-karar-ozetleri. Kurul karar numarasını ve yabancı madde numarasını ezberden yazma.

## Yabancı rejimle karşılaştırma

Yalnız haritada varsa ve araçla:
- **GDPR:** `eu_search_eu_law(query="General Data Protection Regulation")` → CELEX 32016R0679; metin `eu_get_document_text(celex="32016R0679", offset=..., max_chars=...)` (~350.000 karakter; `next_offset` ile ilerle). Madde numarasını dönen metinden al.
- **Birleşik Krallık:** `uk_search_legislation(title="Data Protection", year="2018", type="ukpga")`, `uk_get_section(year="2018", number="12", section="...")`; alıntıdan önce `uk_get_effects` ile güncelliği kontrol et.
- **ABD (karşılaştırmalı not):** eyalet gizlilik yasaları için ArthurLegal'da mevzuat kaynağı yok; yerel hukukçu görüşü al. Yalnız yapı benzetmesi yapılabilir (ör. "çoğu yeni eyalet yasası tek bir temel modelin varyantıdır; farkı çıkar") — kural olarak atıf yapma.

## Tartışmalı — içtihadı ve Kurul kararlarını kontrol et

- Meşru menfaat dengesi (m. 5/2-f) ve "sözleşmenin ifası için gerekli" (m. 5/2-c) ile açık rıza arasındaki sınır.
- 7499 sonrası özel nitelikli verinin m. 6/3 hâllerine (ör. istihdam, sağlık) dayanılarak işlenmesinin kapsamı.
- Yurt dışındaki bulut barındırmasının aktarım sayılması ve "arızi" aktarımın sınırı (Yönetmelik m. 16/1 tanımına rağmen uygulama).
- Aydınlatmada alıcı gruplarının ne kadar genel yazılabileceği.
- İdari para cezasına karşı dava açma süresi (`/arthurlegal:privacy-legal-matter-workspace` kritik süreler notu).

Her biri için sorgu: `tr_semantik_ara(kurum="kvkk", query="<konu>")`, `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="<konu>")`; dönen künyeyi birebir kullan, "yerleşik uygulama" diyorsan karar numarası verme. Düzenleme belirsizse söyle: "[hüküm] [A] ya da [B] okunabilir; [A] temkinli okuma. Önemliyse dış avukat görüşü önerilir."

## Diğer skill'lerle bağlantı

- **`/pia-generation`:** PIA'ların bulduğu metin tutarsızlıkları buraya bilinen açık olarak gelir.
- **`/policy-monitor --mevzuat`:** dış gelişmeyi tespit eder ve buraya yönlendirir.
- **regulatory-legal eklentisi (kuruluysa):** kaynakları izler; bu skill elle tetiklenen sürümdür.

## Çıktı

Tarihli markdown belge olarak kaydet; plan tablosu takipçidir, kalemler kapandıkça durumu güncelle. "Açık yok, uyumluyuz" sonucu da yazılır — sonradan baktığınızın kanıtıdır.

**Atıf doğrulama notuyla bitir:** "Bu çıktıdaki atıflar bir yapay zekâ modeliyle hazırlandı; `tr_` etiketli olanlar araçla çekildi, diğerleri birincil kaynakla doğrulanmadı. Bir düzenlemeye, karara ya da yaptırıma dayanmadan önce resmî kaynakla (mevzuat.gov.tr, resmigazete.gov.tr, kvkk.gov.tr) doğruluğunu ve güncelliğini kontrol edin; `doğrula` etiketlileri önce kontrol edin."

Profildeki `## Outputs` karar ağacıyla kapat; seçenekleri bu çıktıya uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Belirsiz düzenleyici dili bağlayıcı biçimde yorumlamaz; okuma seçeneklerini gösterir.
- Değişiklikleri kendiliğinden izlemez — işaret edildiğinde çalışır (`/policy-monitor --mevzuat` ya da regulatory-legal).
- Düzeltmeleri uygulamaz; planlar.
