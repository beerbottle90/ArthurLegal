---
name: commercial-legal-customize
description: >
  Ticari sözleşme profilinde tek bir şeyi, kurulum görüşmesini baştan yapmadan
  değiştirir: risk iştahı, eskalasyon kişileri ve tutar eşikleri, imza yetkisi notu,
  playbook duruşları (sorumluluk sınırı, tazmin, cezai şart, veri koruma, süre/fesih,
  uygulanacak hukuk ve yetki), NDA triyaj tercihleri, ev üslubu, inceleme tercihleri,
  matter klasörleri. Kullanıcı "şunu değiştir", "profilimi güncelle", "playbook'umu
  düzenle", "ayarı değiştir" ya da "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değiştirmek istediğiniz şey]"
---

# /customize

## Ne yapar

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` ve ortak `~/.claude/plugins/config/claude-for-legal/firm-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa: "Kurulum henüz yapılmamış. Önce `/arthurlegal:commercial-legal-cold-start-interview` çalıştırın — customize var olan profili ayarlamak içindir."

2. **Haritayı göster** — her grup için güncel değerin tek satırlık özeti:
   - **Şirket / kimlik** — ad, sektör, ülkeler, pratik ortamı, satış/satın alma yönü *(ortak profil — tüm eklentilere yansır)*
   - **Risk iştahı** — temkinli / orta / atak; geri çekilme ve eskalasyon tetiklerine etkisi
   - **Kişiler** — eskalasyon zinciri, tutar ve kloz türüne göre onaylayanlar, `**Signing authority:**` notu (tek/çift imza, imza sirküleri tarihi)
   - **Playbook duruşları** — her taraf için `#### Limitation of liability`, `#### Indemnification`, `#### Penalty clause`, `#### Data protection`, `#### Term and termination`, `#### Governing law and venue`, `#### Stamp duty`, `#### The one thing`; ayrıca `## AI/ML training rights`
   - **NDA triyaj tercihleri** — YEŞİL / SARI / KIRMIZI ölçüsü, `closing_action`
   - **İnceleme tercihleri** — redline üslubu, açıklama derinliği, varsayılan paydaş özeti, `confirm_routing`
   - **Ev üslubu** — belge biçimi, imza bloğu, `**Renewal alerts:**` kanalı, KEP adresi, sapma günlüğü biçimi
   - **İş akışı** — matter klasörleri, renewal-watcher sıklığı, `## Playbook monitor settings` (`pattern_threshold`, `lookback_months`)
   - **Entegrasyonlar** — ArthurLegal MCP, CLM, e-imza, Slack, belge deposu ve geri dönüş yolları

3. **Sor:** "Neyi ayarlamak istersiniz? Bir bölüm seçin ya da değişikliği kendi sözlerinizle anlatın."

4. **Değiştir:** güncel değeri göster, yenisini al, aşağı akış etkisini söyle, onay al, yaz. Örnekler:
   - *Sorumluluk tavanı geri çekilmesi 12 ay → 6 ay:* "`/review` artık 6 ayı aşanı sapma işaretler; deal-debrief'in daha önce yazdığı kayıtlar olduğu gibi kalır."
   - *Yeni onaylayan:* "Yetkinizi aşan redline'lar artık bu kişiye yönlenir; `/escalation-flagger` ilgili risk bandında onu varsayılan olarak yazar."
   - *Cezai şart "asla" listesine ekleme:* "Borçlu olduğunuz cezai şartta tacir olarak aşırılık iddiasıyla indirim isteyemeyeceğiniz (TTK m. 22) için bu klozlar artık otomatik eskalasyon olur."
   - *Risk iştahı orta → atak:* "Tedarikçi lehine daha fazla duruşu işaretlemeden kabul ederim; `[review]` çıtası yükselir."

   Kullanıcı yeni bir kanun maddesi, süre ya da eşik söylerse yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; çelişki varsa göster ve hangisinin gireceğini sor. Dönemsel tutarları (damga vergisi oranı, faiz) sabit yazma.

5. **Ortak profil değişikliği** (ad, sektör, ülkeler, pratik ortamı): `firm-profile.md` dosyasına yaz ve söyle: "Bu değişiklik tüm eklentileri etkiler." Pratik ortamı büro ↔ kurum içi değişiyorsa `## Matter workspaces` → `Enabled` değerinin de değişmesi gerektiğini hatırlat.

6. **Kapat:** "Tamam, bir sonraki çıktı değişikliği yansıtır. Başka bir şey var mı?"

## Korkuluklar

- **Bölüm silme.** "Kaldır" denirse `[Not configured]` yaz ve eklentinin davranışına etkisini anlat.
- **İç tutarsızlığı işaretle** — ör. "atak" risk iştahı + "her redline genel müdür onayına"; "satış tarafı" + satın alma duruşu; tavanın kast ve ağır kusuru da kapsaması (TBK m. 115/1 karşısında kesin hükümsüzlük riski). Gerilimi göster, hangisini istediğini sor.
- **Korkuluk zayıflatmayı işaretle.** `[review]` bayrağı, üst başlık, kaynak etiketleri ve doğrulanmamış atıflardaki UYARI satırı yük taşır; kapatılmak istenirse neyi koruduğunu anlat ve bedeli anladığını teyit ettir.
- **Bölüm ve anahtar adlarını çevirme** — diğer skill'ler `## Playbook`, `**Active side:**`, `## Escalation` gibi adları birebir okur.
- **Tek seferde tek değişiklik** — görüşmeyi baştan sorma.

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
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/arthurlegal:legal-research-az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/arthurlegal:legal-research-sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
