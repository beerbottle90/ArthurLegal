---
name: privacy-legal-customize
description: >
  Kişisel veri koruma profilinde tek bir şeyi değiştir — tüm kurulum görüşmesini
  yeniden yapmadan. Rol haritası (veri sorumlusu / veri işleyen), yükümlülük
  haritası (VERBİS, yurt dışı aktarım, sektör, yabancı rejim), risk duruşu,
  eskalasyon kişileri, veri işleyen sözleşmesi playbook'u, aydınlatma metni
  taahhütleri, PIA üslubu, ilgili kişi başvuru süreci ya da matter klasörleri.
  Kullanıcı "şunu değiştir", "profilimi güncelle", "playbook'umu düzenle" ya da
  "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değişikliğin tarifi]"
---

# /customize

## Ne zaman çalışır

Kullanıcı profilindeki bir şeyi — bir sözleşme duruşu, bir aktarım yolu, eskalasyon kişisi, başvuru süresi — kurulum görüşmesini baştan yapmadan ve dosyayı elle düzenlemeden değiştirmek istiyor.

## Ne yap

1. **Profili oku.** `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` ve bir üst klasördeki `~/.claude/plugins/config/claude-for-legal/firm-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa:
   > Henüz kurulum yapılmamış. Önce `/arthurlegal:privacy-legal-cold-start-interview` çalıştırın — customize mevcut bir profili ayarlamak içindir.

2. **Haritayı göster** (her biri için tek satır mevcut değer):
   - **Kim olduğumuz** — ad, sektör, ülkeler, pratik ortamı *(tüm eklentilerle ortak — değişiklik `firm-profile.md`'e yazılır)*
   - **Rol haritası** — hangi faaliyette veri sorumlusu, hangisinde veri işleyen
   - **Yükümlülük haritası** (`## Regulatory footprint`) — VERBİS durumu ve irtibat kişisi, envanter ve imha politikası, aydınlatma metinleri, özel nitelikli veri, yurt dışı aktarım yolları, sektör satırları, yabancı rejimler
   - **Risk duruşu** — temkinli / orta / atak; aktarım, saklama süresi ve sözleşme redline'ına etkisi
   - **Kişiler** — irtibat kişisi, uyum ekibi, bilgi güvenliği, dış avukat, eskalasyon zinciri
   - **Sözleşme playbook'u** (`## DPA playbook`) — denetim, ihlal bildirimi, alt işleyen, veri yeri, silme/iade, sorumluluk; veri işleyen ve veri sorumlusu tarafı ayrı
   - **Aydınlatma taahhütleri** (`## Privacy policy commitments`) — `/policy-monitor`'ün uygulamayla karşılaştırdığı metinler
   - **PIA üslubu** — bölüm sırası, risk puanlama, tetikler
   - **Başvuru süreci** (`## DSAR process`) — kanallar, kimlik doğrulama, iç SLA, sistemler, cevap şablonu
   - **İş akışı** — matter workspaces, `/policy-monitor` tarama sıklığı ve son tarama tarihleri
   - **Entegrasyonlar** — ArthurLegal MCP, belge deposu, Slack; düşüş yolları

3. **Sor:** "Neyi ayarlayalım? Bir bölüm seçin ya da değişikliği kendi cümlenizle anlatın."

4. **Değişikliği yap.** Mevcut değeri göster, yenisini al, aşağı akış etkisini açıkla, onay al, yaz. Örnekler:
   - *Alt işleyen bildirim süresi 30 gün → 14 gün:* "`/dpa-review` artık 14 günden kısa her bildirimi sapma olarak işaretleyecek. Mevcut sözleşmeler kaydedildiği gibi kalır."
   - *Yeni yurt dışı aktarım (AB'de barındırılan bulut):* "Yükümlülük haritasına satır eklenir: yeterlilik kararı yoksa uygun güvence gerekir (KVKK m. 9/4). Standart sözleşme seçilirse metin değiştirilmeden kullanılır ve imzaların tamamlanmasından itibaren beş iş günü içinde Kuruma bildirilir (Yurt Dışına Aktarım Yönetmeliği m. 14/3, 14/5). `/dpa-review` bildirimi kimin yapacağını sözleşmede arar."
   - *Rol: yalnız veri sorumlusu → veri sorumlusu + veri işleyen:* "Playbook'un veri işleyen yarısı devreye girer; `/dpa-review` her sözleşmede tarafı yeniden tespit eder."
   - *VERBİS: kayıtlı → istisna:* "Dayanak Kurul kararının künyesini araçtan getirelim (`tr_semantik_ara(kurum="kvkk", query="Sicile kayıt yükümlülüğünden istisna")` ya da `tr_resmi_gazete_tara`); künye bulunamazsa satıra UYARI satırı eklenir. İstisna, Kanundaki diğer yükümlülükleri kaldırmaz (Veri Sorumluları Sicili Hakkında Yönetmelik m. 5/1-f)."
   - *Risk duruşu orta → temkinli:* "Daha çok faaliyet PIA'ya yönlenir, aktarımda arızi istisnaya daha az dayanılır, saklama süreleri daha kısa önerilir."
   - *Yeni ülke (Almanya):* "Yabancı rejim satırı eklenir; kaynak `de_` araçları. GDPR satırı yoksa `eu_` kontrolü önerilir."

   Kullanıcı bir madde, süre ya da eşik söylüyorsa yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; idari para cezası tutarlarını sabit yazma (güncel tutarı teyit et — dönemsel güncellenir).

5. **Ortak profil değişiklikleri** (ad, sektör, ülkeler, pratik ortamı) `firm-profile.md`'e yazılır:
   > Bu değişiklik tüm eklentileri etkiler — ülke listesini okuyan her eklenti artık [yeni değer]i görür.

6. **Kapat:** "Tamam. Bir sonraki çıktı bunu yansıtacak. Başka bir şey var mı? `/arthurlegal:privacy-legal-customize` her zaman çalışır."

## Korkuluklar

- **Bölümü silme.** Bir rejim kapsamdan "çıkarılmak" istenirse `[Şu an kapsam dışı]` işaretini öner ve hangi işaretlemelerin düşeceğini açıkla.
- **İç tutarsızlığı işaretle.** Ör. "yalnız veri işleyen" + veri sorumlusu playbook'u etkin; "yurt dışı aktarım yok" + bulut sağlayıcısı yurt dışında; "VERBİS istisnası" + saklama ve imha politikası hiç yok (politika yükümlülüğü yoksa da silme yükümlülüğü sürer: Silme Yönetmeliği m. 5/3); bankacılıkta "açık rızayla paylaşırız" (müşteri sırrı, maddedeki istisnalar dışında, açık rıza alınsa dahi müşteri talebi ya da talimatı olmaksızın paylaşılamaz: 5411 s. Kanun m. 73/3).
- **Kanuni sınırın altına inme.** İç başvuru cevap süresi otuz günü aşacak şekilde ayarlanamaz (KVKK m. 13/2); periyodik imha aralığı altı ayı aşamaz (Silme Yönetmeliği m. 11/2); standart sözleşme bildirimi beş iş gününü aşamaz (KVKK m. 9/5). Böyle bir talebi reddet ve nedenini açıkla.
- **Güvence kaybını işaretle.** `tr_mevzuat_madde_getir` doğrulaması, çekilemeyen veride UYARI satırı, kaynak etiketleri, `[review]` işareti ve `/use-case-triage`'daki zorunlu PIA kontrolü yük taşır — kaldırma; ayarlamadan önce bedelini açıkla.
- **Bölüm anahtarlarını çevirme** (`## Regulatory footprint`, `## DPA playbook`, `## Outputs`, `## Matter workspaces`, `Active matter:` vb.).
- **Tek seferde tek değişiklik.** Görüşmeyi baştan sorma.
