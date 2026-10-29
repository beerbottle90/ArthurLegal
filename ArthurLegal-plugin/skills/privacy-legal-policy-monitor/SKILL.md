---
name: privacy-legal-policy-monitor
description: >
  Aydınlatma metinlerini ve diğer gizlilik yüzeylerini uygulamayla güncel tutar;
  KVKK gelişmelerini (Kurul karar özetleri, Resmî Gazete, ikincil mevzuat, sektör
  kurumları) gerçek araçlarla izler. Üç mod: kayıtlı PIA, sözleşme incelemesi ve
  triyaj çıktılarını tarayarak kaymayı bulma; önerilen yeni bir uygulama için
  doğrudan sorgu; son taramadan bu yana dış gelişme taraması. "Aydınlatma metnimiz
  bunu kapsıyor mu", "X yapmaya başlayacağız, metin değişmeli mi", "politika
  taraması", "Kurul'dan yeni ne var" denince kullan.
argument-hint: "[önerilen uygulamanın tarifi | --sweep | --mevzuat]"
---

# /policy-monitor

**Tarama modu** (argümansız ya da `--sweep`): profilden çıktı klasörünü, aydınlatma metinlerini ve son tarama tarihini oku → o tarihten sonraki çıktıları tara → onaylanan uygulamaları metinlerle karşılaştır → açıkları ZORUNLU / TAVSİYE diye sınıflandır → her açık için mevcut metni alıntıla, açığı anlat, önerilen metni yaz → `Last policy sweep` tarihini güncelle. Sonunda dış gelişme taramasını öner.

**Doğrudan sorgu modu** (tarif ile): önerilen uygulamayı ayrıştır → veri kategorisi, amaç, hukuki sebep, alıcı grubu, yurt dışı aktarım, saklama, haklar ve bildirim bakımından metinle karşılaştır → kapsanan / eksik / çatışan + önerilen metin + zamanlama.

**Dış gelişme modu** (`--mevzuat`): `Last regulatory scan` tarihinden bugüne KVKK ve sektör gelişmelerini tara → her kalem için "bize dokunur mu?" → dokunanları `/arthurlegal:privacy-legal-reg-gap-analysis`'e yönlendir → tarihi güncelle.

```
/arthurlegal:privacy-legal-policy-monitor
/arthurlegal:privacy-legal-policy-monitor "Davranışsal veriyi karşılama e-postalarını kişiselleştirmek için kullanacağız"
/arthurlegal:privacy-legal-policy-monitor --mevzuat
```

---

# Aydınlatma ve Gelişme İzleyici

## Amaç

Metin uygulamanın gerisinde kalır: bir PIA yeni bir veri kategorisini onaylar, aydınlatmada geçmeyen bir alt işleyenle sözleşme imzalanır, bir triyaj sonucu metinde olmayan bir bildirim koşulu koyar. Aydınlatma yükümlülüğü yerine getirilirken eksik, yanıltıcı ve yanlış bilgiye yer verilmez ve işleme amacı değişirse işlemeden önce ayrıca aydınlatma yapılır (Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ m. 5/1-b, j). Bu skill kaymayı sorun olmadan yakalar; dışarıdaki değişikliği de `reg-gap-analysis`'e taşır. Çıktı hep aynıdır: açık burada, önerilen metin bu.

## Mevcut durumu yükle

`~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`:
- `## Regulatory footprint` — kapsamdaki rejimler (KVKK, sektör satırları, GDPR/UK)
- `## Privacy policy commitments` — aydınlatma metinlerinden çıkarılan taahhütler
- `## Outputs` — çıktı klasörü, metin yerleri, `Last policy sweep`, `Last regulatory scan`

`## Outputs` `[PLACEHOLDER]` içeriyorsa: "Çıktı klasörü ayarlanmamış. Yine de doğrudan sorgu yapabilirim — ne planladığınızı anlatın. Taramayı açmak için `/arthurlegal:privacy-legal-cold-start-interview` ile klasör yolunu verin."

Asıl metni `## Outputs` → **Privacy policy document** yolundan oku. Profildeki özet yalnız özettir; öneri yazmak için asıl metin esastır.

### Taahhütler birden çok yüzeydedir — hepsini tara

Profile her yüzeyin yerini ve son güncelleme tarihini yaz; tarama her birini güncel metinle karşılaştırır ve ayrışmayı bildirir ("Aydınlatma [tarih]te güncellendi; mobil uygulama etiketi [daha eski tarih] — yeni veri kategorisini yansıtmıyor olabilir").

1. **Aydınlatma metinleri** — web, mobil uygulama, çalışan, aday, ziyaretçi/kamera, tedarikçi. Sözlü, yazılı, ses kaydı, çağrı merkezi gibi ortamlarda yapılan aydınlatmalar da aynı usule tabidir (Tebliğ m. 5/1); çağrı merkezi metni de taranır.
2. **Açık rıza metinleri ve onay akışları** — açık rızaya dayanan faaliyette aydınlatma ve açık rıza ayrı ayrı yapılır (Tebliğ m. 5/1-f). Rıza ekranındaki amaç ile aydınlatmadaki amaç aynı mı?
3. **VERBİS kaydı** — kayıt yükümlüsüyse aydınlatmada verilen bilgiler Sicile açıklananlarla uyumlu olmalı (Tebliğ m. 5/1-ç); Sicildeki bilgilerdeki değişiklik yedi gün içinde bildirilir (Veri Sorumluları Sicili Hakkında Yönetmelik m. 13). Yeni amaç, kategori, alıcı grubu ya da yabancı ülkeye aktarım = VERBİS güncellemesi de gerekebilir.
4. **Çerez paneli** — paneldeki çerez kategorileri ve amaçları aydınlatma ile çerez politikasındakiyle aynı mı? Kurumun çerez uygulamalarına ilişkin rehberine dayanacaksan güncel sürümünü Kurumun sitesinden teyit et; UYARI: veri çekilemedi, teyidiniz gerekli: https://www.kvkk.gov.tr/
5. **Uygulama mağazası gizlilik etiketleri** (Apple, Google) — kendi beyanınızdır; aydınlatmadaki kategori, amaç ve paylaşımla uyumlu mu, en son ne zaman güncellendi?
6. **Ticari elektronik ileti onayları** — ticari elektronik ileti önceden onayla gönderilir; esnaf ve tacirlere onaysız gönderilebilir (6563 s. Kanun m. 6). Yeni pazarlama kanalı = onay metni ve aydınlatma birlikte kontrol.

### Sektör bildirimleri de kapsamdadır

`## Regulatory footprint`'te sektör satırı varsa tarama o kurala göre de bakar; bildirim/metin ayarlanmamışsa her taramada **kalıcı açık** olarak göster, tek seferlik bulgu değil:

| Sektör | Neye bakılır | Ne işaretlenir |
|---|---|---|
| **Bankacılık** | Müşteri sırrı paylaşımları | Yeni bir üçüncü kişiye paylaşımı ima eden çıktı: müşteri sırrı, maddedeki istisnalar dışında, açık rıza alınsa dahi müşteri talebi ya da talimatı olmaksızın paylaşılamaz (5411 s. Kanun m. 73/3). Aydınlatmada "açık rızanızla paylaşırız" demek yetmez. |
| **Elektronik haberleşme (işletmeci)** | Abone rıza kayıtları, trafik/konum verisi | Terminal cihazda bilgi saklama/erişim için açık ve kapsamlı bilgilendirme ve açık rıza; trafik ve konum verisinin yurt dışına aktarımı için açık rıza; rıza kayıtları asgari abonelik süresince saklanır (5809 s. Kanun m. 51/3, 51/6, 51/10-c). |
| **Sağlık** | Hasta aydınlatması, özel nitelikli veri | Kişisel Sağlık Verileri Hakkında Yönetmelik (RG 21.06.2019/30808) — madde atfı gerekirse `tr_mevzuat_madde_getir(mevzuat_id="105551", madde_no=...)`; çekilemezse UYARI satırı. Özel nitelikli veride Kurulun belirlediği yeterli önlemler de şarttır (KVKK m. 6/4). |

**Kapsam belirsizse sor.** Profilde sektör satırı yok ama çıktılarda sağlık, finans ya da abone/trafik verisi görünüyorsa önce sor: "Profilinizde [sektör] yok ama bu tarama [kategori] içeren çıktılara bakıyor. Haritaya ekleyelim mi, karşılaştıracağımız ayrı bir metin var mı?" Bildirimi bulamıyorsan sessizce yalnız web aydınlatmasına bakma; açığı yüksek sesle söyle.

---

## Mod 1: Tarama

### Kapsam

`Last policy sweep` tarihinden sonraki çıktı dosyalarını tara. Tarih yoksa hepsini tara ve not düş: "İlk tarama — tüm çıktılar." Yeni dosya yoksa: "[tarih]ten bu yana yeni çıktı yok. Metin yakın uygulamayla güncel görünüyor." Tarama bitince `Last policy sweep`'i bugünün tarihiyle güncelle.

### Her çıktıda ne okunur

- **PIA:** veri kategorileri, amaçlar, hukuki sebepler (KVKK m. 5 ya da m. 6), alıcılar/alt işleyenler, yurt dışı aktarım, saklama süreleri, haklara etkisi, konulan koşullar → metinde olmayanı işaretle.
- **Sözleşme incelemeleri (imzalanmış/onaylanmış):** eklenen alt işleyenler, kabul edilen veri yerleri ve aktarım yolu (yeterlilik, standart sözleşme, bağlayıcı şirket kuralları, taahhütname, arızi istisna — KVKK m. 9), kapsanan amaçlar → aydınlatmada alıcı grubu ve aktarım amacı belirtilmiş mi (KVKK m. 10/1-c; Tebliğ m. 5/1-ı), VERBİS'te yabancı ülkelere aktarım bilgisi güncel mi (Veri Sorumluları Sicili Hakkında Yönetmelik m. 9/1-d), standart sözleşme bildirildi mi (KVKK m. 9/5)?
- **Triyaj sonuçları (PIA GEREKLİ / DEVAM):** onaylanan uygulama ve kamuya dönük taahhüt ima eden koşullar ("lansmandan önce ilgili kişiler aydınlatılmalı") → metinde karşılığı yoksa işaretle.
- **Başvuru cevapları:** önceki cevaplarda olmayan yeni veri kategorileri, sistem listesine eklenen sistemler → aydınlatmada geçmeyen kategori.

### Açık sınıflandırması

**ZORUNLU** — metin bu çıktıyla çelişiyor ya da işleme sürüyor ve metinde hiç karşılığı yok. Güncellenmezse eksik veya yanıltıcı aydınlatma olur (Tebliğ m. 5/1-j); aydınlatma yükümlülüğünü yerine getirmemek idari para cezası gerektirir (KVKK m. 18/1-a — kanun metnindeki aralık; güncel tutarı teyit et, dönemsel güncellenir).
> Örnek: Metin "ad, e-posta ve ödeme bilgisi topluyoruz" diyor; bir PIA konum verisini onayladı. Konum hiç geçmiyor → ZORUNLU.

**TAVSİYE** — metin sessiz ama çelişmiyor; savunulabilir, güncellenirse daha temiz.
> Örnek: Metin "hizmet aldığımız tedarikçilere aktarabiliriz" diyor; yeni bir analitik tedarikçisiyle sözleşme imzalandı, alıcı grubu kapsanıyor → isim listesi tutuluyorsa ekle.

**Tartışmalı — içtihadı ve Kurul kararlarını kontrol et:** alıcı grubunun ne kadar genel yazılabileceği; yurt dışındaki bulut sağlayıcısının barındırmasının "aktarım" sayılıp aydınlatmada ayrıca belirtilmesi gereği. `tr_semantik_ara(kurum="kvkk", query="aydınlatma metni alıcı grupları genel ifade")` ile ara; dönen karar özetinin `citation` alanını birebir kullan.

### Tarama çıktısı

```markdown
[ÜST BAŞLIK — ## Outputs; role göre]

# Aydınlatma İzleyici — Tarama Raporu
**Tarih:** [tarih] · **Taranan çıktı:** [N] · **Son taramadan beri yeni:** [N]
**Açık:** [N] ZORUNLU | [N] TAVSİYE
**Yüzey uyumu:** aydınlatma [tarih] · açık rıza [tarih] · VERBİS [tarih] · çerez paneli [tarih] · mağaza etiketi [tarih]
**Sektör bildirimleri:** [sektör]: [yol + tarih / AYARLANMADI — çözülene dek her taramada işaretlenir]

## ZORUNLU güncellemeler
### [Açık 1 kısa adı]
**Kaynak:** [dosya / çıktı türü]
**Ne oluyor:** [yeni uygulamanın sade tarifi]
**Mevcut metin:** [ilgili bölümden alıntı — ya da "Karşılığı yok"]
**Açık:** [eksik ya da tutarsız olan]
**Etkilenen diğer yüzeyler:** [VERBİS / açık rıza / çerez paneli / mağaza etiketi]
**Önerilen metin:**
> *[bölüm adı]na ekle:* "[metnin üslubuna uygun, somut taslak]"

## TAVSİYE güncellemeler
[aynı biçim, kısaltılmış]

## İşlem gerekmeyen
[açık bulunmayan taranmış çıktılar — incelendiklerini teyit eder]

## Sonraki adımlar
- [ ] ZORUNLU'lar: ilgili özellik/işleme canlıya çıkmadan önce (zaten canlıysa hemen) karar
- [ ] TAVSİYE'ler: sonraki metin yenilemesinde
- [ ] Dış gelişme taraması: `/arthurlegal:privacy-legal-policy-monitor --mevzuat` (son: [tarih])
```

---

## Mod 2: Doğrudan sorgu

Tariften çıkar: hangi veri, hangi amaç, hangi hukuki sebep, kimler dahil (tedarikçi, ortak, yurt dışı alıcı), ilgili kişi kim (çalışan, müşteri, çocuk), otomatik karar var mı (ilgili kişinin münhasıran otomatik analizle aleyhe sonuca itiraz hakkı: KVKK m. 11/1-g), yeni bildirim gerekiyor mu. Tarif belirsizse **tek** netleştirici soru sor; uzun ön görüşme yapma.

| Kontrol | Metin ne diyor | Önerilen uygulama | Sonuç |
|---|---|---|---|
| Veri kategorileri | | | 🟢 Kapsanıyor / 🟡 Açık / 🔴 Çelişki |
| Amaçlar | | | |
| Hukuki sebep (m. 5 / m. 6) | | | |
| Alıcı grupları ve aktarım amacı | | | |
| Yurt dışı aktarım ve yolu (m. 9) | | | |
| Saklama süresi (imha politikası) | | | |
| Haklar (m. 11) | | | |
| Açık rıza gerekiyor mu, ayrı alınıyor mu | | | |
| VERBİS etkisi | | | |

Çıktı: **Sonuç** (GÜNCELLEME ZORUNLU / TAVSİYE / GEREKMEZ) → kapsananlar (kısa) → eksikler (mevcut metin, neden önemli, önerilen metin, hangi bölüme) → çelişkiler (hangisi değişmeli ve neden; çoğu zaman uygulama metne uyar ya da metin savunulabilir yeni bir duruşa güncellenir) → **Zamanlama:** ZORUNLU varsa "amaç değiştiği için işlemeden önce ayrıca aydınlatma gerekir (Tebliğ m. 5/1-b)"; yalnız TAVSİYE ise "devam edilebilir, sonraki yenilemede güncelleyin".

---

## Mod 3: Dış gelişme taraması

Pencere: `Last regulatory scan` → bugün (ilk taramada son 90 gün). `tr_` çağrılarını sırayla yap, aralarında birkaç saniye bırak (hız sınırı ortaktır). Araç veri getiremezse (hata, `unavailable`, `upstream_blocked`) boş sonuç sayma; o kalem için UYARI satırını aracın `source_url`'si ya da resmî giriş sayfasıyla yaz.

1. **Kurul karar özetleri** (canlı liste son sayfaları tarar; sıra tarihe göre değildir, `date` ve `decision_no` alanına bak):
   `tr_kurum_karari_ara(kurum="kvkk", params={"scan_pages": 3}, limit=30)`
   Konu bazlı: `tr_kurum_karari_ara(kurum="kvkk", query="çerez", params={"scan_pages": 5})`. Arşiv ve tarih aralığı için: `tr_semantik_ara(kurum="kvkk", query="yurt dışına aktarım standart sözleşme", date_from="YYYY-AA-GG")`. Metni oku: `tr_kurum_karari_getir(kurum="kvkk", id="<id>")`.
2. **Resmî Gazete** (Kurul düzenleyici kararları, yeterlilik kararları — yeterlilik kararı Resmî Gazete'de yayımlanır: KVKK m. 9/2 — ve yeni yönetmelikler). Tek çağrı en çok 60 gün; uzun pencereyi böl:
   `tr_resmi_gazete_tara(date_from="YYYY-AA-GG", date_to="YYYY-AA-GG", query="Kişisel Veri")`
   Tek gün: `tr_resmi_gazete_fihrist(date="YYYY-AA-GG", query="Kişisel Veri")`.
3. **İkincil mevzuat** (KVKK yönetmelikleri `KKY`, tebliğler `TEBLIGLER` türündedir):
   `tr_mevzuat_ara(query="Kişisel Veri", types=["KKY", "TEBLIGLER"], rg_date_from="YYYY-AA-GG")`
   Uyarı: RG tarihi boş kayıtlar tarih süzgecine girmez; boş sonuç "değişiklik yok" demek değildir. İzlenen metinlerin değişiklik tablosunu ayrıca kontrol et: `tr_mevzuat_getir(mevzuat_id="108729")` (Aydınlatma Tebliği), `"106248"` (Silme Yönetmeliği), `"106135"` (Sicil Yönetmeliği), `"328537"` (Yurt Dışına Aktarım Yönetmeliği), `"108728"` (Başvuru Tebliği) — metin sonundaki "Değişiklik Yapan" listesinde yeni tarih var mı?
4. **Kanun değişikliği:** `tr_mevzuat_madde_getir(number="6698", madde_no=["6", "9", "10", "12", "16", "18"])` → `annotations` alanındaki "(Değişik: …)" / "(Ek: …)" notlarını önceki taramanın listesiyle karşılaştır.
5. **Sektör** (yalnız haritadaysa): `tr_kurum_karari_ara(kurum="bddk", query="bilgi sistemleri")`; `tr_kurum_karari_ara(kurum="btk", query="kişisel veri", date_from="YYYY-AA-GG")`.
6. **Yabancı rejim** (yalnız haritadaysa): AB — `eu_search_eu_law(query="data protection", date_from="YYYY-AA-GG")` ve `eu_search_eu_law(query="adequate protection of personal data", date_from="YYYY-AA-GG")`; Birleşik Krallık — `uk_search_legislation(title="Data", year="YYYY")`, değişiklik için `uk_get_effects`.

**Kalem başına tek satır:** `[tarih] · [künye — araçtan birebir] · [konu] · Bize dokunur mu: Evet/Hayır/Belirsiz — [gerekçe] · Sonraki adım`. "Evet/Belirsiz" olanlara: `/arthurlegal:privacy-legal-reg-gap-analysis "[künye]"`. Bitince `Last regulatory scan`'i güncelle. Kurul karar numarasını asla ezberden yazma; yalnız araçtan dönen `citation`.

---

## Önerilen metnin kalitesi

- Asıl metnin sesine ve üslubuna uy (profil özetini değil, asıl belgeyi oku).
- Amaç belirli, açık ve meşru olsun; genel ve muğlak ifade ya da "ileride başka amaçlar için de işlenebilir" izlenimi veren ifade kullanma; dil anlaşılır, açık ve sade olsun (Tebliğ m. 5/1-g, ğ).
- Hukuki sebebi açıkça yaz — KVKK m. 5 ve 6'daki hangi şarta dayanıldığı (Tebliğ m. 5/1-h).
- Ekibin tutamayacağı taahhüt yazma ("konum verisini asla paylaşmayız" yazma, mimari analitik tedarikçisine akıtıyorsa).
- Tek cümle eklemek yetmiyor, duruş değişikliği gerekiyorsa söyle. Hangi bölüme ekleneceğini hep belirt; bölüm yoksa açılmasını öner.

## Zamanlama

Eklenti kendini zamanlamaz. Kullanıcıya önce: "Takviminize ya da görev yöneticinize haftalık `/arthurlegal:privacy-legal-policy-monitor` ve aylık `--mevzuat` hatırlatıcısı koyun." Her çalışma `Last policy sweep` / `Last regulatory scan` tarihini günceller; sonraki çalışma yalnız yenilere bakar.

## Kapanış

Profildeki `## Outputs` karar ağacıyla bitir; seçenekleri bu çıktıya uyarla (metni yaz, eskale et, olgu topla, izle ve bekle, başka bir şey). Ağaç çıktıdır; seçimi avukat yapar. On'dan fazla bulgu varsa ya da istenirse yüzeye ve önem derecesine göre sayımlı, sıralanabilir bir tablo öner.

## Bu skill ne yapmaz

- Metni kendisi değiştirmez; önerir, her değişikliği insan onaylar.
- Dış değişikliğin açık analizini yapmaz — `--mevzuat` yalnız tespit eder ve `reg-gap-analysis`'e yönlendirir.
- Çıktıların kaydedilmesini zorlamaz; klasöre kaydedilmeyen PIA'yı bulamaz (doğrudan sorgu yine çalışır).
- E-posta ya da Slack'teki gayriresmî kararları okumaz; yalnız klasördeki yapılandırılmış çıktıları okur.
