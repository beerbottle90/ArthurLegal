---
name: privacy-legal-dpa-review
description: >
  Veri işleme sözleşmesi (DPA; veri sorumlusu–veri işleyen sözleşmesi)
  incelemesi — tarafın veri işleyen mi veri sorumlusu mu olduğunu belirler,
  sözleşmeyi DPA playbook'unun ilgili yarısına ve KVKK tabanına (m. 3 roller,
  m. 12 veri güvenliği ve müşterek sorumluluk, m. 8–9 aktarım, standart
  sözleşmenin 5 iş günü içinde bildirimi) göre madde madde tarar, en küçük
  ölçekte redline önerir. "Bu DPA'yı incele", "veri işleme sözleşmesi",
  "müşteri kendi DPA'sını gönderdi", "tedarikçi sözleşmesindeki KVKK eki",
  "bu DPA uygun mu" denince ya da bir DPA eklendiğinde kullan.
argument-hint: "[dosya | bağlantı | metni yapıştırın]"
---

# /dpa-review — Veri İşleme Sözleşmesi İncelemesi

DPA iki türlüdür ve inceleme ikisinde neredeyse terstir: müşteri kendi DPA'sını gönderdiğinde operasyonel esnekliğimizi savunuruz; tedarikçiyle sözleşirken kendi (ve müşterilerimizin) verisini koruruz. İkisi de aynı playbook'tan, karşı satırlardan okunur.

KVKK, veri işleyenle yapılacak sözleşmenin asgari içeriğini saymaz. Taban; rol tanımları (m. 3), veri güvenliği yükümlülükleri ve müşterek sorumluluk (m. 12), aktarım kuralları (m. 8–9) ve Yurt Dışına Aktarım Yönetmeliği'nden gelir; rakamlar (bildirim saatleri, süreler) playbook'tan. AB rejimi de uygulanıyorsa asgari içerik için GDPR Art. 28'i araçla çek. Her madde atfından önce `tr_mevzuat_madde_getir`.

## ⏰ ÖN-KONTROL — Süre

| Durum | Süre | Dayanak |
|---|---|---|
| Yurt dışı aktarım standart sözleşmeyle | İmzaların tamamlanmasından itibaren **5 iş günü** içinde Kuruma bildirim (fiziki, KEP ya da Kurul'un belirlediği yöntem); kimin bildireceği sözleşmede belirlenebilir, belirlenmemişse veri aktaran bildirir | 6698 m. 9/5; Yurt Dışına Aktarım Yön. m. 14/5 |
| Bildirim yapılmazsa | İdari para cezası (tutar yazma — kanun metnindeki sınırlar her yıl yeniden değerlenir) | 6698 m. 18/1-d; 5326 m. 17/7 |
| Veri ihlali | Veri sorumlusu ilgilisine ve Kurula **en kısa sürede** bildirir | 6698 m. 12/5 |
| İhlal — Kurul uygulaması | Kurul karar özetleri ihlalin **tespitinden itibaren 72 saat** ölçütünü uygular; ölçütü koyan düzenleyici kararın metni araçla bulunamadı → atıf yapmadan önce yeniden ara, bulunamazsa UYARI satırı | `tr_semantik_ara(kurum="kvkk", query="veri ihlali bildirimi 72 saat")` |
| VERBİS bilgisi değişirse (yeni alıcı grubu, yurt dışı aktarım) | Kanun: derhâl; Yönetmelik: değişiklikten itibaren 7 gün içinde VERBİS üzerinden | 6698 m. 16/3-ç, d, m. 16/4; Veri Sorumluları Sicili Hakkında Yön. m. 13/1 |

72 saat Kanun'da değildir; "Kanun 72 saat öngörür" yazma (GDPR'daki 72 saat ayrı bir kuraldır: Art. 33 — AB tarafında araçla çek). Veri işleyenden veri sorumlusuna bildirim süresini, veri sorumlusunun bu uygulamaya yetişeceği şekilde playbook'tan kur.

## Destination check

- **Dahili inceleme notu** → profilin `## Outputs` bölümündeki role göre üst başlık.
- **Karşı tarafa giden redline ya da açıklama** → iç gerekçe, risk puanı, fallback ve "kabul edebileceğimiz en kötü pozisyon" çıkarılır; başlık konmaz.
- **İş birimine özet** → hukuki analiz kısaltılır; "imzalanabilir mi, neyin değişmesi gerekir" iki cümleyle.

## ADIM 0 — Yön: veri işleyen mi, veri sorumlusu mu?

- Veri sorumlusu: işleme amaçlarını ve vasıtalarını belirleyen, veri kayıt sisteminin kurulmasından ve yönetilmesinden sorumlu kişi (m. 3/1-ı). Veri işleyen: veri sorumlusunun verdiği yetkiye dayanarak onun adına işleyen kişi (m. 3/1-ğ).
- [Müvekkil] veri işleyen → müşterinin DPA'sı → playbook'un veri işleyen tarafı → **savunma**.
- [Müvekkil] veri sorumlusu → tedarikçinin DPA'sı ya da bizim şablon → playbook'un veri sorumlusu tarafı → **koruma**.
- Etiket gerçeği belirlemez: "veri işleyen" diye adlandırılan taraf veriyi kendi amacıyla (hizmet geliştirme, model eğitimi, pazarlama) kullanıyorsa o kullanımda veri sorumlusudur → aktarım (m. 8) ve aydınlatma (m. 10) sorunu. "Ortak veri sorumluluğu" KVKK'da tanımlanmamıştır — **tartışmalı; Kurul kararlarını ara**.
- Belirsizse sor. Yön yanlışsa her öneri tersine döner.

## Bağlamı yükle

- `firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DPA playbook` (veri işleyen tarafı | veri sorumlusu tarafı | otomatik ret), `## Privacy policy commitments` (aydınlatma metinleri), `## Regulatory footprint` (sektör ve yabancı rejim satırları), `## Escalation`, `## Outputs`, `## Who's using this`. Yer tutucu varsa dur ve `/arthurlegal:privacy-legal-cold-start-interview` öner.
- **Önceki çıktılar** (`## Outputs` klasörü): aynı karşı taraf ya da faaliyet için `use-case-triage`, `pia-generation`, önceki `dpa-review`. Bulunursa incelemede an: "Önceki triage ([tarih]) [risk] dedi ve onayı [X] şartına bağladı; bu inceleme onunla tutarlı / şu nedenle ayrılıyor: [yeni olgu, kapsam, kloz]." **Ciddiyet tabanı:** önceki çıktının 🔴'si sessizce 🟢'ye inmez; her düşürme gerekçesiyle yazılır. Bulunamazsa açıkça yaz: "Bu karşı taraf/faaliyet için önceki triage veya PIA yok."

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:privacy-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Sektörel katman (madde madde incelemeden önce sor)

Genel KVKK tabanının üstüne sektör kuralı binebilir; KVKK'ya uygun bir DPA sektör kuralına kör olabilir.

| Veri | Ek kural | Ara |
|---|---|---|
| Banka müşteri verisi | Bankacılık faaliyetine özgü müşteri ilişkisi verileri müşteri sırrıdır; istisnalar dışında, KVKK uyarınca açık rıza alınsa dahi müşteriden talep ya da talimat olmaksızın yurt içi/yurt dışı üçüncü kişilerle paylaşılamaz; BDDK yurt dışına paylaşımı yasaklamaya ve bilgi sistemleri ile yedeklerin yurt içinde tutulmasına karar verebilir; destek/hizmet alımına ilişkin istisna ve şartları m. 73/4'te | `tr_mevzuat_madde_getir(number="5411", madde_no=["73"], max_chars_per_article=8000)`; `tr_kurum_karari_ara(kurum="bddk", query="destek hizmeti")` |
| Sağlık verisi | Özel nitelikli (m. 6/1); m. 6/3-e; Kişisel Sağlık Verileri Hakkında Yönetmelik | `tr_mevzuat_ara(query="Kişisel Sağlık Verileri", types=["KKY"])` |
| Elektronik haberleşme | Elektronik Haberleşme Sektöründe Kişisel Verilerin İşlenmesi ve Gizliliğin Korunmasına İlişkin Yönetmelik | `tr_mevzuat_ara(query="Elektronik Haberleşme Sektöründe Kişisel Verilerin", types=["KKY"])` |
| Sigorta, sermaye piyasası, ödeme hizmetleri | Sektör mevzuatındaki sır ve dış hizmet kuralları | `tr_mevzuat_ara(query=..., search_in="fulltext")`; `tr_kurum_karari_ara(kurum="spk"/"bddk", ...)` |
| Özel nitelikli veri (her sektör) | Kurul'un belirlediği yeterli önlemler şarttır (m. 6/4) | `tr_semantik_ara(kurum="kvkk", query="özel nitelikli kişisel veri yeterli önlemler")` — düzenleyici kararın metni indekste yoksa UYARI satırı |

Hiçbiri yoksa açıkça yaz: "sektörel katman yok — kontrol edildi."

## Madde madde inceleme (her DPA)

Rakamlar playbook'tan, yasal taban Kanun'dan. Taban az sonuç dönerse sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) burada dur ve avukat teyidine işaretle."

| Konu | Aranan | KVKK / TBK tabanı | Tipik kavga |
|---|---|---|---|
| Roller | Gerçeğe uygun rol | m. 3/1-ğ, ı | "Ortak sorumlu" etiketi; karşı tarafın kendi amaçları |
| Kapsam ve talimat | Belgelenmiş talimat, tanımlı amaç | m. 3/1-ğ ("verdiği yetkiye dayanarak onun adına"); m. 12/4 (amaç dışı kullanım ve açıklama yasağı) | "ve ilgili amaçlar" genişletmesi |
| Alt veri işleyenler | Güncel liste, değişiklik usulü | Kanun'da ayrı hüküm yok → playbook; yurt dışındaysa sonraki aktarım (m. 9/8) | Toptan onay / veto / yalnız bildirim |
| Güvenlik | Somut tedbir eki | m. 12/1 (teknik ve idari tedbirler); m. 12/2 (veri sorumlusu, adına işleyenle birlikte **müştereken sorumlu**) | Eki olmayan "uygun tedbirler" |
| Denetim | Yöntem, sıklık, bildirim, maliyet | m. 12/3 (veri sorumlusu denetim yapmak veya yaptırmak zorunda) | Kısa bildirimli yerinde denetim |
| Gizlilik | Çalışanlar dahil, sözleşme sonrası | m. 12/4 (görevden ayrıldıktan sonra da sürer) | Süre sınırı |
| İhlal bildirimi | Tetik ("öğrenme" mi "teyit" mi), süre, içerik, iş birliği | m. 12/5 "en kısa sürede" + Kurul uygulaması (yukarıda) | Belirsiz "gecikmeksizin" |
| Yurt dışı aktarım | Mekanizma | m. 9 (aşağıda) | Mekanizma yok; değiştirilmiş standart sözleşme |
| Silme / iade | Sona ermede süre, tutanak, yedek | m. 7; Silme Yönetmeliği | "Ticari olarak makul" silme |
| Sorumluluk | Ana sözleşme tavanı mı, ayrı mı; istisnalar | TBK m. 115/1 (ağır kusurdan önceden sorumsuzluk anlaşması kesin hükümsüz); m. 18/2 (cezanın muhatabı) | Sınırsız veri sorumluluğu; ceza tazmini |

- **m. 12/2 "müştereken"**: bunun ilgili kişiye karşı müteselsil sorumluluk anlamına gelip gelmediği ve iç ilişkide kusur dağılımı **tartışmalı — doktrin ve içtihadı kontrol et** (`scholar_search_legal_scholarship`, `tr_ictihat_semantik_ara`). Rücu ve tazmin klozunu bu belirsizliği gözeterek kur.
- **İdari para cezası:** m. 18/1-a–ç cezaları veri sorumlusuna, (d) bendindeki standart sözleşme bildirim cezası veri sorumlusu ya da veri işleyen gerçek kişi ve özel hukuk tüzel kişilerine uygulanır (m. 18/2). Cezanın sözleşmeyle karşı tarafa yansıtılabilirliği (tazmin klozu) **tartışmalı — içtihadı kontrol et**.
- **Tavan klozu:** kast ve ağır kusur tavan dışında kalmalı (TBK m. 115/1).
- **Karşı tarafın matbu DPA'sı:** tek başına önceden hazırlanıp sunulan hükümler genel işlem koşuludur (TBK m. 20); karşı tarafın menfaatine aykırı koşul, açıkça bilgi verilip içeriği öğrenme imkânı sağlanmadıysa yazılmamış sayılır (TBK m. 21/1). Tacirler arası uygulamadaki etkisi için içtihadı kontrol et.

### Yurt dışı aktarım (m. 9 — 7499 s.K. ile değişik)

Sırayla:
1. **Yeterlilik kararı** (ülke, ülke içindeki sektör ya da uluslararası kuruluş; Kurul verir, RG'de yayımlanır) + m. 5 ya da m. 6 şartlarından biri (m. 9/1-2).
2. Yoksa **uygun güvence** + m. 5/6 şartı + ilgili kişinin aktarım ülkesinde de haklarını kullanma ve etkili kanun yollarına başvurma imkânı (m. 9/4): (a) kamu kurumları arası anlaşma + Kurul izni; (b) Kurul onaylı bağlayıcı şirket kuralları; (c) Kurul'un ilan ettiği **standart sözleşme**; (ç) yazılı taahhütname + Kurul izni.
   - Standart sözleşme metni **hiç değiştirilmeden** kullanılır; yabancı dilde de akdedilirse Türkçe metin esastır (Yön. m. 14/3). Taraflarca ya da temsile ve imzaya yetkililerce imzalanır (m. 14/4). Bildirime yetki belgeleri ve yabancı dildeki her belgenin noter onaylı çevirisi eklenir (m. 14/6). Değiştirilmiş metin ya da eksik imza → Kurul incelemesi (m. 14/7). Taraf/içerik değişikliği ya da sona ermede yeniden bildirim (m. 14/8). → DPA'da standart sözleşmeyi "uyarlayan" ya da onunla çelişen kloz 🔴; ticari hükümleri ayrı belgeye taşı.
   - Hangi standart sözleşme metninin (aktarım yönüne göre) kullanılacağını Kurul'un ilan ettiği metinlerden kullanıcıya teyit ettir; metin araçta yoksa "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.kvkk.gov.tr/".
3. O da yoksa **arızi aktarım** (m. 9/6-a–f) — yalnız arızi: düzenli olmayan, tek ya da birkaç sefer gerçekleşen, süreklilik arz etmeyen ve olağan faaliyet akışında bulunmayan aktarım (Yön. m. 16/1). Süregelen bulut/SaaS ilişkisi arızi değildir.
4. **Veri işleyenin aktarımı** veri sorumlusunun sorumluluğunu kaldırmaz; veri sorumlusu tedbirlerin veri işleyence alınmasını sağlamakla yükümlüdür (Yön. m. 7/2); bildirim yükümlüsü veri işleyense talimat beklemeden bildirir (Yön. m. 7/3).
5. **Sonraki aktarımlar** (alt işleyen zinciri) için de aynı güvenceler (m. 9/8).

- Yurt dışındaki sunucuda barındırmanın yurt dışı aktarım sayılması **yerleşik Kurul uygulaması — kararı çek** (`tr_semantik_ara(kurum="kvkk", query="yurt dışında bulunan sunucu bulut hizmeti aktarım")`).
- Yurt dışı aktarım var, mekanizma yok → 🔴 (hukuka uygun aktarım yolu yok).
- **AB tarafı** (veri aktaran AB'de ya da GDPR uygulanıyor): `eu_search_eu_law(query="standard contractual clauses transfer of personal data to third countries")` → CELEX 32021D0914; veri sorumlusu–veri işleyen klozları için `eu_search_eu_law(query="standard contractual clauses controllers processors")`; Türkiye hakkında AB yeterlilik kararı olup olmadığını araçla kontrol et, ezberden söyleme. **İngiltere:** `uk_search_legislation(query="Data Protection Act 2018")`. Aktarım etki değerlendirmesi gerekip gerekmediğini işaretle; değerlendirmeyi bu skill yapmaz.

### Veri işleyen olduğumuzda — savunma

| Kloz | Risk | Pozisyon |
|---|---|---|
| Alt işleyen veto hakkı | Altyapıyı müşteri müşteri onaya bağlar | Playbook (bildirim + itiraz) |
| Kısa bildirimli yerinde denetim | Ölçekte yürümez | Rapor/sertifika + sınırlı yerinde denetim; m. 12/3 makul bir denetim hakkını haklı kılar |
| Aşırı kısa ihlal bildirimi | Olay anlaşılmadan bildirim | Playbook süresi; içerik kademeli tamamlanır |
| Katı veri yerelleştirme | Mimari uymayabilir | Gerçekte taahhüt edilebilen; bankacılıkta 5411 m. 73 BDDK kararları |
| Sınırsız sorumluluk / ceza tazmini | Şirketi batırabilir | Playbook; kast/ağır kusur dışında tavan (TBK m. 115/1) |
| Açık uçlu "talimat" yetkisi | Sınırsız operasyonel kontrol | "Sözleşmede belgelenen ya da yazılı kararlaştırılan talimat" |
| Çok kısa silme süresi | Yedek/log nedeniyle imkânsız | Playbook; yedek rotasyonu istisnası belgelenir |
| Standart sözleşmeyi değiştiren kloz | Kurul incelemesi, m. 18/1-d riski | Metin değiştirilmeden; ticari hükümler ayrı |

### Veri sorumlusu olduğumuzda — koruma

| Kloz | Açık | Talep |
|---|---|---|
| Alt işleyen listesi yok | Verimize kim dokunuyor bilinmez | Yayımlanmış güncel liste + önceden bildirim |
| "Sektör standardı güvenlik" | m. 12/2 müşterek sorumluluk bizde | Somut tedbir eki ya da adlandırılmış standart (ISO 27001, SOC 2) |
| İhlal bildirim süresi yok | m. 12/5 yükü bizde | Playbook süresi (Kurul uygulamasına yetişecek kadar kısa) |
| Denetim hakkı yok | m. 12/3 yerine getirilemez | En az bağımsız denetim raporu |
| "Hizmet geliştirme" / model eğitimi | Tedarikçi o amaçla veri sorumlusu olur; m. 8, m. 10 | Sil; işleme yalnız hizmet sunumu için |
| Yurt dışı aktarım mekanizması yok | m. 9 | Standart sözleşme + 5 iş günü bildirim takvimi + bildirimi kimin yapacağı |
| Silme taahhüdü yok | m. 7 | Süre + talep üzerine imha tutanağı |

## Aydınlatma metni ve gizlilik politikası tutarlılığı

- DPA'daki amaçlar aydınlatma metninde var mı (m. 10/1-b)? Aktarılan alıcılar ve amaçları (m. 10/1-c)? VERBİS'teki alıcı grupları ve yurt dışı aktarım bilgisi (m. 16/3-ç, d) DPA ile örtüşüyor mu?
- Politika "verilerinizi yurt dışına aktarmayız" diyor, DPA yurt dışı bulut içeriyor → çelişki.

Uyumsuzluğu bayrakla; çoğunlukla eski olan politikadır, ama biri değişmeli (→ `/arthurlegal:privacy-legal-reg-gap-analysis`). *Karşılaştırmalı not:* ABD eyalet yasalarındaki "satış/paylaşım" nitelendirmesinin Türk hukukundaki karşılığı aktarım şartlarıdır (m. 8–9).

## Redline inceliği

En küçük düzeltme: kelime → ifade → alt bent → cümle → ancak gerekirse tüm madde. Tüm maddeyi değiştirdiysen ileti notunda söyle: "8.2'yi değişiklikler kapsamlı olduğu için işaretlemek yerine yeniden yazdık; farkı birlikte geçebiliriz." Küçük redline dikkatli okunduğunu gösterir.

## ArthurLegal MCP

```
tr_mevzuat_madde_getir(number="6698", madde_no=["3","6","8","9","10","12","16","18"])
tr_mevzuat_ara(query="Kişisel Verilerin Yurt Dışına Aktarılmasına", types=["KKY"])      → mevzuat_id
tr_mevzuat_madde_getir(mevzuat_id=<yukarıdaki>, madde_no=["7","14","15","16"])
tr_mevzuat_madde_getir(number="6098", madde_no=["20","21","115"])
tr_semantik_ara(kurum="kvkk", query="veri ihlali bildirimi 72 saat")
tr_kurum_karari_ara(kurum="kvkk", query="veri ihlal bildirimi")   ← yalnız son sayfaları tarar; sıra tarihe göre değil
eu_get_document_text(celex="32016R0679", offset=211000)           ← GDPR Art. 28 (veri işleyen sözleşmesi); Art. 33 (ihlal) ≈ offset 221500
```

Dönen kararın künyesini birebir kullan; karar numarası ezberden yazılmaz. Çekilemeyen madde için: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/". Atıf etiketi: `[ArthurLegal TR — 6698 m. X — GG.AA.YYYY]`, `[ArthurLegal EU — CELEX … — GG.AA.YYYY]`, ezberden gelen için `[model bilgisi — doğrula]`, kullanıcıdan gelen için `[kullanıcı verdi]`.

## Çıktı

```markdown
[ÜST BAŞLIK — profil ## Outputs]

# DPA İncelemesi: [Karşı taraf]

**Yön:** [Veri işleyeniz / Veri sorumlusuyuz]   **Tarih:** [GG.AA.YYYY]   **Bağlı olduğu sözleşme:** [ana sözleşme / tek başına]

## ⚠️ İnceleyen notu
- **Önceki çıktılar:** [triage/PIA/DPA — tarih ve sonuç / yok]
- **Sektörel katman:** [yok — kontrol edildi / 5411 / sağlık / …]
- **Yurt dışı aktarım:** [yok / yeterlilik / standart sözleşme — bildirim son günü GG.AA.YYYY / BCR / taahhütname / arızi]
- **Kaynaklar:** ArthurLegal MCP — [madde sayısı, Kurul kararı]; doğrulanamayan: [liste]
- **Tartışmalı noktalar:** [liste]
- **Eskalasyon:** [yok / [isim] — hangi kloz]

## Sonuç
[İki cümle: imzalanabilir mi, neyin değişmesi gerekir.]
**Bulgular:** [N]🟢 [N]🟡 [N]🟠 [N]🔴

## Madde madde
[Her konu için kısa blok: karşı tarafın metni · playbook · fark · risk · önerilen redline]

## Aydınlatma / politika tutarlılığı
[🟢 Tutarlı | 🟡 Bayraklar: liste]

## Önerilen redline'lar
[Toplu, gönderilmeye hazır — iç gerekçe olmadan]

## Karşı taraf kabul etmezse
[Her konu için playbook fallback'i ya da `## Escalation` yönlendirmesi]
```

## Sonuç doğuran işlem kapısı (DPA'nın imzalanması)

İnceleme araştırmadır; **imza** (ya da imzalı nüshayı iade, karşı tarafın platformunda otomatik kabul, imzacıya talimat) hukuki işlemdir. Bu aşamaya geçmeden önce eklenti ayarında `## Who's using this` oku. Rol **avukat değilse**:

> DPA imzalamak şirketi ilgili kişilere ve Kurula karşı somut veri koruma yükümlülüklerine bağlar; standart sözleşme içeriyorsa 5 iş günlük bildirim süresi imzayla başlar. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet: karşı taraf, yön (veri işleyen / veri sorumlusu), playbook'tan sapan klozlar ve nasıl çözüldükleri, yurt dışı aktarım yolu ve bildirim takvimi, açık fallback kararları; avukata sorulacak üç soru. Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık "evet" olmadan imzaya yönlendirme.

## Kapanış

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları bu incelemeye göre uyarla (redline'ı gönder, eskalasyon, ek olgu iste — ör. alt işleyen listesi, standart sözleşme bildirimini takvime al, diğer). Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Sıfırdan DPA yazmaz; cevap "şablonumuzu kullanalım" ise şablonu profildeki `## Seed documents` yolundan alır.
- Aktarım etki değerlendirmesini kendisi yapmaz; gerektiğini işaretler.
- Fallback dışındaki şartları kabul etmeye karar vermez; `## Escalation`'a göre yönlendirir.
