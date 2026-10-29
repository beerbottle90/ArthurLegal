---
name: regulatory-legal-reg-feed-watcher
description: >
  Düzenleyici akışları şimdi kontrol eder (Resmî Gazete, mevzuat, sekiz düzenleyici kurumun
  kararları, AYM norm denetimi, izlenen yabancı yargı çevreleri) ve son kontrolden bu yana
  yeni olanı önemlilik eşiğine göre süzerek raporlar. "Akışları kontrol et", "yeni ne var",
  "mevzuat güncellemesi", "bu haftanın Resmî Gazete'si" denince, zamanlanmış ajan
  çalıştırdığında ya da kullanıcı bir düzenleyici gelişmeyi sınıflandırma ve politika
  karşılaştırması için yapıştırdığında kullan.
argument-hint: "[isteğe bağlı: --since YYYY-AA-GG]"
---

# /reg-feed-watcher

1. Profili yükle: `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → `## Regulators we watch` (watchlist), `## Materiality threshold`, `## Feed configuration`.
2. Aşağıdaki iş akışını uygula.
3. Her akışı çek; önemlilik eşiğine göre süz.
4. Çıktı: yeni olanlar, önem kademesine göre.

---

## Amaç

Akışı çek, önemliliğe göre süz, kalanı göster. Değer süzgeçtedir; süzülmemiş Resmî Gazete gürültüdür.

## Bağlamı yükle

- Eklenti profili (başlık ve anahtar adları İngilizce kalır; çevirme):
  - `## Regulators we watch` — watchlist tablosu (Regulator, Jurisdiction, Why we watch, Feed source).
  - `## Materiality threshold` — üç kademe: `**Always material (alert immediately):**`, `**Review-worthy (weekly digest):**`, `**FYI (monthly roundup or not at all):**`.
  - `## Feed configuration` — `**Free feeds (always active):**` tablosu (araç çağrısı, RSS ya da kurum duyuru sayfası), `**Paid feeds (if configured):**`, `**Manual entry:**`, `**Comment tracking:**`, `**Default comment decision owner:**`, `**Check cadence:**`, `**Digest channel:**`, `**Digest output path:**`.
- Ortak profil `firm-profile.md`: [Müvekkil]'ın sektörü, lisansları, halka açık olup olmadığı, denetime tabi olduğu kurumlar. Watchlist'te eksik kurum varsa buradan anla.
- `source-catalog.md`: Türkiye, AB, Birleşik Krallık ve yaptırım kaynaklarının küratörlü listesi. Yeni kaynak yapılandırırken ya da kapsam boşluğu görürken kullan (Adım 0).
- `mevzuat-mcp-rehberi.md` bölüm 4: `konu` süzgecinin ölçülmüş sınırları.
- `reg-feed-haftalik-sablon.md`: müvekkile ya da şirket içine haftalık bülten biçimi isteniyorsa.

## İş akışı

### Adım 0: Kapsam kontrolü (çekmeden önce)

Watchlist ve feed yapılandırmasını `source-catalog.md` ile karşılaştır:
- Kullanıcı hangi kategorileri izliyor (Türk mevzuatı, Türk kurumları, AB/Birleşik Krallık, diğer yabancı, yaptırım)?
- Bunlardan hangisinde hiç ya da çok az kaynak yapılandırılmış?

Belirgin boşluk varsa digest'in başında **bir kez** göster. Türkiye'de sık görülenler:
- [Müvekkil] EPDK lisans sahibi ama `epdk` kurum akışı yapılandırılmamış.
- Halka açık ama SPK bülteni izlenmiyor; banka ya da finansal kuruluş ama BDDK yok.
- `**Comment tracking:**` Enabled ama `**Free feeds (always active):**` tablosunda hiçbir kurumun taslak duyuru sayfası yok. Görüşe açılan taslaklar Resmî Gazete'de yayımlanmaz ve ArthurLegal araçlarında taslak akışı yoktur; bu sayfa tanımlanmadan görüş süreleri kaçar.

> **Kapsam boşluğu:** Watchlist'inizde [kategori] var ama yalnız [N] kaynak yapılandırılmış. `source-catalog.md` bu kategoride [ör. 2-3 ad] öneriyor. Ekleyeyim mi? `/arthurlegal:regulatory-legal-cold-start-interview --redo` çalıştırın ya da `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasını düzenleyin.

Aynı boşluğu her çalışmada tekrarlama. Kullanıcı "şimdilik X'i atla" dediyse uy ve bunu profile not et.

### Adım 1: Çek

Yapılandırılmış her katmandan çek. Tier 1 her kurulumda vardır; Tier 2 ve 3 eklenir.

Genel kurallar:
- `tr_` çağrılarını sırayla yap, aralarında birkaç saniye bırak (hız sınırı ortaktır).
- Her araç çağrısı 100 saniyede iptal edilir. Dar tut; iptal olursa aynı sorguyu tekrarlama, aralığı böl.
- Araç veri getiremezse (hata, `unavailable`, `upstream_blocked`) boş sonuç sayma. O kalem için şunu yaz: `UYARI: veri çekilemedi, teyidiniz gerekli: <aracın source_url'si ya da resmî giriş sayfası>`. Bağlantı uydurma.
- Pencere: `--since` verildiyse o tarih, yoksa son kontrol zamanı, o da yoksa son 7 gün.

**Tier 1 — Ücretsiz akışlar (her zaman açık): ArthurLegal MCP**

1. **Resmî Gazete (birincil akış).** Neyin yayımlandığının ölçüsü fihristtir; mevzuat araması RG akışını vermez.
   ```
   tr_resmi_gazete_tara(date_from="2026-10-19", date_to="2026-10-25", konu="enerji")
   tr_resmi_gazete_tara(date_from="2026-10-19", date_to="2026-10-25", query="Elektrik")
   tr_resmi_gazete_tara(date_from="2026-10-19", date_to="2026-10-25", query="Kişisel Veri")
   ```
   - `konu` yalnız `enerji`, `rekabet`, `vergi`, `icra` alır. Başlığında konu adı geçmeyen kalemi de bulur ama bir ön elemedir. Sonucu `query` ile tamamla; enerji taramasında `konu`'ya tek başına güvenme (elektrik, doğal gaz, petrol, lisans, EPDK ile ikinci tarama).
   - Dört konu dışındaki alanlar (KVKK, iş hukuku ve İSG, sermaye piyasası, bankacılık) yalnız `query` ile taranır.
   - Yanıttaki `konu_elenen` sayısını digest'e yaz. "Bu hafta başka bir şey çıkmadı" deme; "konu süzgecinden geçenler bunlar, N kalem elendi" de.
   - Tek çağrı en çok 60 gün tarar; uzun pencereyi böl.
   - Tek gün ya da mükerrer sayı: `tr_resmi_gazete_fihrist(date="2026-10-24", mukerrer=1)`.
   - Değişiklik metni, yürürlük maddesi ve geçiş hükmü: `tr_resmi_gazete_getir(url="<fihristteki url>")`.
   - Sonuçtaki `section` alanı (YÖNETMELİKLER, KURUL KARARLARI, CUMHURBAŞKANI KARARLARI vb.) sınıflandırmada ilk ipucudur.
2. **Mevzuat (kimlik ve konsolide metin).**
   ```
   tr_mevzuat_ara(types=["KANUN"], rg_date_from="2026-10-01", rg_date_to="2026-10-25", konu="vergi", max_pages=2)
   tr_mevzuat_ara(query="Elektrik Piyasası", types=["YONETMELIK", "KKY", "TEBLIGLER"], rg_date_from="2026-10-01")
   tr_mevzuat_ara(number="6446", types=["KANUN"])
   ```
   - Türler: `KANUN`, `KHK`, `CB_KARARNAME`, `CB_KARAR`, `CB_YONETMELIK`, `CB_GENELGE`, `YONETMELIK`, `KKY`, `UY`, `TEBLIGLER`.
   - RG tarih süzgeci RG tarihi boş kayıtları hiç getirmez ve konsolide veri tabanı yayımın gerisinde kalabilir. Boş sonuç "o dönemde düzenleme yok" demek değildir; yayımı RG fihristinden teyit et.
   - Torba kanun: `konu_kaynak: "degistirilen_kanunlar"` dönen kanunun hangi kanunları değiştirdiği `konu_degistirilen` alanındadır; `konu_kaynak: "belirsiz"` dönen kanunu `tr_mevzuat_getir` ile aç ve kendin karar ver.
3. **Kurum kararları** (yalnız watchlist'teki kurumlar):

   | Kurum | Çağrı | Not |
   |---|---|---|
   | EPDK | `tr_kurum_karari_ara(kurum="epdk", market="elektrik", year=2026, limit=20)` | `market`: elektrik, dogalgaz, petrol, lpg. Yalnız yapısal Kurul kararları; lisans tadilleri RG fihristindedir. Karar tarihi ile RG tarihi farklıdır; ikisini de yaz. |
   | Rekabet | `tr_kurum_karari_ara(kurum="rekabet", query="\"dikey anlaşma\"", decision_type="rekabet_ihlali")` | Çok kelimeli ifadeyi tırnakla. Kılavuz ve tebliğler mevzuattadır (`tr_mevzuat_ara`). |
   | SPK | `tr_kurum_karari_ara(kurum="spk", year=2026)` → son bülten no, sonra `tr_spk_bulten_icinde_ara(bulten="2026/74", query="idari para cezası")` | Kurul kararları haftalık bültendedir. |
   | BDDK | `tr_kurum_karari_ara(kurum="bddk", query="destek hizmeti", year=2026)` | Canlı arama başlıkta; metin için `tr_semantik_ara(kurum="bddk", query=…)`. |
   | KVKK | `tr_kurum_karari_ara(kurum="kvkk", params={"scan_pages": 3}, limit=30)` | Liste tarihe göre sıralı değil; `date` alanına bak. |
   | BTK | `tr_kurum_karari_ara(kurum="btk", date_from="2026-10-01", date_to="2026-10-25")` | Canlı arama başlıkta; gerekçe PDF'te. |
   | GİB | `tr_kurum_karari_ara(kurum="gib", query="<konu>", date_from="2026-10-01")` | Özelge bağlayıcı değildir; idarenin görüşüdür. |
   | Sigorta Tahkim | `tr_kurum_karari_ara(kurum="sigorta_tahkim", issue=<dergi sayısı>)` | Hakem kararı dergisi. |

   Arşivde ya da tarih aralığında konu araması: `tr_semantik_ara(kurum="<kurum>", query="<konu>", date_from="YYYY-AA-GG")`. Tam metin: `tr_kurum_karari_getir(kurum="<kurum>", id="<id>")`. Filtreleri görmek için `tr_kurum_listesi`.
4. **AYM norm denetimi** (watchlist'in dayandığı temel kanunlar için): `tr_aym_ara(kind="norm", query="6446 sayılı Elektrik Piyasası Kanunu")`. İptal kararları RG'de de yayımlanır; RG taramasında `query="Anayasa Mahkemesi"` ile yakalanır. İptal hükmü yayım tarihinde ya da AYM'nin belirlediği ileri tarihte yürürlükten kalkar (Anayasa m. 153/3); bu tarihi ayrıca yaz.
5. **Yabancı yargı çevreleri** (yalnız watchlist'te varsa):
   - AB: `eu_search_eu_law(query="electricity market", date_from="2026-10-01")`
   - Birleşik Krallık: `uk_search_legislation(title="Energy", year="2026")`; bir kanunun işlenmemiş değişiklikleri: `uk_get_effects(year="<yıl>", number="<no>", unapplied_only=true)`
   - Almanya: `de_recent_changes(since_iso="2026-10-19")`
   - Finlandiya: `fi_recent_changes()` (yalnız son değişen beş akt)
   - Hollanda, Polonya, Avusturya, İrlanda, İspanya, Japonya, Azerbaycan: kendi arama araçlarıyla (`nl_`, `pl_`, `at_`, `ie_`, `es_`, `jp_`, `az_`).
   - Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."
6. **Araç dışı kaynaklar.** KİK, Sayıştay, TÜRKPATENT ve İSTAÇ ArthurLegal'da yoktur (resmî uçları cevap vermiyor); bunlar için araç önerme, sonuç uydurma. TBMM'deki kanun teklifleri, KAP bildirimleri, kurumların taslak duyuruları, MASAK, KGK ve bakanlık duyuruları da araçlarda yoktur. Profilde sayfa adresi tanımlıysa (ajanda WebFetch ile) oku ve `[kurum sitesi]` etiketi koy; tanımlı değilse kullanıcının manuel girişine bırak. Yaptırım listeleri (OFAC, AB, Birleşik Krallık) için `source-catalog.md`.

**Tier 2 — Ek bağlayıcılar (`**Paid feeds (if configured):**`)**

Bağlıysa Thomson Reuters Regulatory Intelligence (son kontrolden bu yana, watchlist kurumlarına süzülmüş), kullanıcının kendi aboneliğiyle bağladığı başka veri tabanları ya da ABD için CourtListener (`courtlistener-rehberi.md`). Aynı belge birden çok kaynaktan gelebilir: teke indir, en zengin kaynağı kullan.

**Sessiz tamamlama yok.** Bir watchlist kurumu için akış az ya da hiç sonuç döndürürse bulduğunu raporla ve dur. Boşluğu web araması ya da model bilgisiyle doldurma; sor:
> "Akış kontrolü [N] kalem döndürdü ([kaynaklar]). [Kurum / konu] için kapsam ince görünüyor. Seçenekler: (1) tarih aralığını genişletmek, (2) başka bir araç ya da kaynak denemek, (3) web araması — sonuçlar `[web araması — doğrula]` etiketi taşır ve kullanılmadan önce kurumun sitesinden kontrol edilmelidir, (4) burada durmak. Hangisi?"

Daha düşük güvenilirlikteki kaynağı kabul etme kararı avukatındır.

**Kaynak etiketi.** Her kaleme nereden geldiğini yaz. Araçtan gelen kalem: `[ArthurLegal TR — <araç> — GG.AA.YYYY]` (ör. `[ArthurLegal TR — tr_resmi_gazete_tara — 26.10.2026]`, `[ArthurLegal TR — tr_kurum_karari_ara:epdk — 26.10.2026]`); yabancı araçta önek değişir (`[ArthurLegal EU — eu_search_eu_law — …]`). Diğerleri: `[TR Regulatory Intelligence]`, `[kurum sitesi]`, `[web araması — doğrula]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`. `doğrula` etiketli kalemlerin uydurma riski daha yüksektir; önce onlar kontrol edilir. Etiketleri silme ya da birleştirme.

**İkincil kaynak.** Büro bültenleri, meslek kuruluşu ve dernek duyuruları, haber siteleri, Lexology ve benzeri yorumcular birincil kaynak değildir. Bunlardan gelen kaleme ayrıca `[ikincil kaynak]` etiketi koy ve şu notu ekle: "→ Birincil kaynağa git: RG fihristi ya da ilgili kurumun kararı; bulunmadan güvenme." İkincil kaynağa dayanan kalemi tek başına Always material yapma; birincil kaynak bulunana kadar bir kademe aşağıda tut.

**Tier 3 — Manuel giriş**

Kullanıcı düzenleme metnini ya da özetini yapıştırdıysa onu tek kalem say, Adım 2'ye geç, kaynağı `[kullanıcı verdi]` olarak kaydet. Akış çekmek gerekmez; abonelikten bağımsız çalışır.

Çektikten sonra kontrol zamanını kaydet; sonraki çalışma oradan başlar.

### Adım 2: Sınıflandır

Her kalem profildeki `## Materiality threshold` kademelerinden birine girer: `**Always material (alert immediately):**`, `**Review-worthy (weekly digest):**`, `**FYI (monthly roundup or not at all):**`. Profildeki madde listeleri aşağıdaki tablodan önce gelir; tablo yalnız profilin sessiz kaldığı kalem türleri için varsayılandır. Kademe etiketleri İngilizce kalır.

| Kalem türü | Eşik karşılığı |
|---|---|
| RG'de yayımlanan kanun, CB kararnamesi, CB kararı ya da yönetmeliği, kurum yönetmeliği, tebliğ | İzlenen faaliyete dokunuyorsa genelde Always material. Yürürlük tarihini ve geçiş hükmünü metnin kendisinden yaz. |
| RG'de yayımlanan ya da kurumun ilan ettiği düzenleyici Kurul kararı | [Müvekkil]'ın lisansı ya da faaliyetiyle eşleşiyorsa Always material. Örnek: elektrik piyasasında lisans sahibi faaliyet alanına göre mevzuatın gereklerini yerine getirmekle yükümlüdür ve ikincil mevzuata, Kurul kararlarına aykırılık ihtar ve idari para cezasına bağlanır (6446 m. 5/2-e, 16/1-b). |
| AYM iptal kararı; Danıştay yürütmeyi durdurma ya da iptal kararı | İzlenen kuralı etkiliyorsa Always material. Bu bir durum değişikliğidir: ilgili açıkların `status_verified` alanını yeniden değerlendir (`/arthurlegal:regulatory-legal-gaps`). |
| Görüşe açılan düzenleme taslağı | Genelde Review-worthy; görüş son tarihini her zaman kaydet (`item_type: draft`). |
| Taslaksız istişare, tartışma metni, görüş çağrısı | Uyum için değil strateji için Review-worthy (`item_type: consultation`). |
| TBMM'ye sunulan kanun teklifi | İzleme (`item_type: bill`). ArthurLegal'da TBMM kaynağı yok; teklif metnini kullanıcı verir. |
| Bireysel Kurul kararı, idari para cezası | Sektör eşleşmesi → material; benzer uygulama → Review-worthy; ikisi de yoksa FYI ya da atla. |
| Kılavuz, rehber, ilke kararı, duyuru | Review-worthy. |
| Konuşma, sunum, basın açıklaması | Eşiğe göre FYI ya da atla. |
| Taahhüt ya da uzlaşma kararı (ör. Rekabet Kurulu) | Yeni bir yaklaşım ya da yüksek tutar → Review-worthy; rutin → atla. |
| [Müvekkil]'ın adının geçtiği her kalem | Always material. |

**Taslak ve istişare dalı.** Taslak ve istişare kalemleri hukuku henüz değiştirmez ama görüş son tarihi gerçektir ve kurumun yönünü gösterir. Bu yüzden ayrı ele alınır:
- İstişare ya da taslağı Always material yapma; uyum etkisi kural yayımlanana kadar sıfırdır.
- Konusu watchlist'in Always material kategorilerinden birine dokunuyorsa Review-worthy yap.
- `**Comment tracking:**` Enabled ise son tarihi `~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml` dosyasına yaz (şema `/arthurlegal:regulatory-legal-comments`'te): `item_type` (`draft`, `consultation` ya da `bill`), `decision: undecided`, `owner` = `**Default comment decision owner:**`. Son tarih kurumun duyurusundan alınır; duyuruda yoksa "son tarih belirtilmemiş — kurumdan teyit et" yaz, tarih uydurma.
- Digest satırına açıkça yaz: "Kural öncesi. Görüş son tarihi [tarih]. `/arthurlegal:regulatory-legal-policy-diff`'e yalnız ön konumlanma analizi için yönlendir (henüz uyum açığı yok)."
- Bunlar uyum açığı değildir: açık izleyiciye (gap tracker) değil görüş izleyicisine (comment tracker) gider. `gap-surfacer` bunları `comment-decision` `gap_type` ile tutar ya da hiç almaz.

### Adım 3: Zenginleştir

FYI üstündeki her kalem için:
- Tek satır: ne değişti.
- Neden önemli: "bu, [[Müvekkil]'ın yaptığı iş] hakkında".
- Bağlantı: araçtan dönen `url` / `source_url`; künye için araçtan dönen `citation` birebir.
- Yürürlük tarihi, geçiş süresi ya da görüş son tarihi. Yürürlük tarihini yürürlük maddesinden oku; "yayımı tarihinde" varsayma.

FYI kalemlerini tek tek özetleme; yalnız say.

## Çıktı

Digest varsayılan olarak sohbete yazılır. FYI üstünde en az bir kalem varsa, `**Digest output path:**` değeri "chat only" değilse **ayrıca paylaşılabilir bir dosyaya da yaz**:

1. `**Digest output path:**` bir klasörse oraya `reg-digest-YYYY-MM-DD.md`; boşsa `~/regulatory-legal-digests/reg-digest-YYYY-MM-DD.md`.
2. Üst klasör yoksa oluştur.
3. Sohbetteki içeriğin aynısını Markdown olarak yaz (üst başlık, kaynak etiketleri, doğrulama notu dâhil).
4. O gün için dosya varsa üzerine yazma; zaman damgalı yeni bir alt başlık ekle.
5. Sonra söyle: "Digest `<yol>` dosyasına yazıldı. Olduğu gibi paylaşabilir ya da Pandoc ile .docx'e çevirebilirsiniz: `pandoc <yol> -o <yol>.docx`."
6. Yazma başarısız olursa (izin, klasör, disk) yalnız sohbete yaz ve bunu söyle; dosya isteğini sessizce düşürme.
7. `**Digest channel:**` dolu ve kanal bağlıysa digest'i oraya göndermeyi öner; kişiye özel mesajlar gap-surfacer'daki gönderim başına onay kuralına tabidir.

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

## Düzenleyici Akış Kontrolü — [tarih]

**Dönem:** [son kontrol] – [şimdi]
**Taranan akışlar:** [ör. "RG fihristi (konu=enerji + query), tr_mevzuat_ara, EPDK, SPK bülteni 2026/74"]
**Konu süzgeci:** elenen [n], belirsiz [n] — kapsam garantisi değildir
**Bulunan kalem:** [N]

### Sonuç

[N kalem [tarih]e kadar işlem gerektiriyor — ilk üçü: X, Y, Z]

### 🔴 Always material (alert immediately)

**[Kurum] — [Başlık]** `[kaynak etiketi]`
[Tek satır özet]. [Neden önemli]. Yürürlük [tarih]; geçiş [varsa].
[Bağlantı]
→ Öneri: [etkilenmesi muhtemel politika] için `/arthurlegal:regulatory-legal-policy-diff`

### 🟡 Review-worthy (weekly digest)

**[Kurum] — [Başlık]** `[kaynak etiketi]`
[Tek satır]. [Neden önemli]. [Son tarih varsa].
[Bağlantı]
[Taslak / istişare: "💬 Görüş son tarihi: [tarih] — karar bekliyor"]

### 📝 FYI (monthly roundup or not at all)

[N] kalem — [başlık + bağlantı listesi, özetsiz]

### UYARI satırları

[Veri çekilemeyen her kaynak için: UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>]

---

**Son kontrol güncellendi:** [zaman damgası]
**Görüş izleyici:** kararı bekleyen [N] taslak/istişare — `/arthurlegal:regulatory-legal-comments`

---

**Atıfları doğrula.** Buradaki künyeler yapay zekâ desteğiyle derlendi. Bir düzenlemeye, karara ya da kılavuza dayanmadan önce Resmî Gazete, mevzuat.gov.tr ya da kurumun sitesinden doğruluğunu, yürürlük tarihini ve güncel durumunu kontrol et. Kaynak etiketleri her künyenin nereden geldiğini gösterir; `doğrula` etiketliler önce kontrol edilir.
```

## Ayar eksikse

Profilde gereken değer boşsa ya da `[PLACEHOLDER]` ise genel değil somut söyle:
- **Watchlist boş (`## Regulators we watch`):** dur. "Profilinizdeki izleme listesi boş; hangi kurumları izleyeceğimi bilmeden akış çekemem. `/arthurlegal:regulatory-legal-cold-start-interview --redo` çalıştırın ya da `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasına en az bir kurum ekleyin."
- **Materiality threshold boş:** yukarıdaki varsayılan kademeleri kullan ve ekle: "Profilinizde özel eşik olmadığı için varsayılan kademeler kullanıldı. `/arthurlegal:regulatory-legal-cold-start-interview --redo` ile ya da profili düzenleyerek ayarlayın."
- **Feed configuration boş:** yalnız Resmî Gazete taramasını (watchlist'teki kurum ve kanun adlarıyla `query`) çalıştır ve ekle: "Profilinizde kurum akışı ya da duyuru sayfası tanımlı olmadığı için yalnız Resmî Gazete fihristi tarandı. Kurum akışlarını `/arthurlegal:regulatory-legal-cold-start-interview --redo` ile ekleyin."

Değerler doluysa ayardan hiç söz etme.

FYI üstünde kalem yoksa: "Sakin. [N] FYI kalem, dikkat gerektiren yok. Konu süzgeci [n] kalem eledi."

## Devir

- **policy-diff'e:** politika etkisi muhtemel her Always material kalem için karşılaştırmayı öner.
- **gap-surfacer'a:** karşılaştırma açık bulursa izlenir.
- **Görüş izleyiciye:** FYI üstündeki her taslak ve istişare, `**Comment tracking:**` Enabled ise son tarihiyle otomatik kaydedilir.
- **Uzman skill'ler:** yalnız KVKK'ya dokunan ayrıntılı açık analizi `/arthurlegal:privacy-legal-reg-gap-analysis`; EPDK taslağına görüş metni `/arthurlegal:administrative-legal-epdk-proaktif-gorus`.

## Kapanış

Profildeki `## Outputs` karar ağacıyla bitir. Seçenekleri bu çıktıya uyarla; beş varsayılan dal (X'i yaz, eskale et, olgu topla, izle ve bekle, başka bir şey) başlangıçtır, kalıp değildir. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Her kalemi baştan sona okumaz. Sınıflandırır ve zenginleştirir; derin okuma süzgeçten geçenler içindir.
- Önemlilik eşiğini değiştirmez. Süzgeç yanlışsa profil düzenlenir.
- Ücretli kaynak gerektirmez. ArthurLegal araçları tabandır; ek bağlayıcılar derinlik katar.
- Taslakları kendiliğinden bulmaz. Kurum duyuru sayfası profilde tanımlı değilse taslak ancak kullanıcı yapıştırınca girer.

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
| AZ duzenleyici degisiklik takibi — akt statusu degistiyse (`Legv olunmus`) ardil akti bul | `/arthurlegal:legal-research-az-mevzuat` |
| karsilastirmali regulasyon literaturu — **ikincil**, mevzuat yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
