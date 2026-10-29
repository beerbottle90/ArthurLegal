---
name: corporate-legal-customize
description: >
  Kurumsal pratik profilinde tek bir şeyi, kurulum görüşmesini baştan yapmadan
  değiştirir: risk iştahı, eskalasyon kişileri, etkin modüller (M&A / Yönetim Kurulu ve
  Sekretarya / Halka Açık Şirket / Şirket Yönetimi), önemlilik eşikleri, açıklama listesi
  biçimi, YK karar ve GK tutanak formatı, elden dolaştırma emsalleri, şirket tablosu ve
  uyum takvimi, matter klasörleri. Kullanıcı "şunu değiştir", "profilimi güncelle",
  "ayarı değiştir" ya da "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değiştirmek istediğiniz şey]"
---

# /customize

## Ne yapar

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` ve bir üst düzeydeki ortak `~/.claude/plugins/config/claude-for-legal/firm-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa: "Kurulum henüz yapılmamış. Önce `/arthurlegal:corporate-legal-cold-start-interview` çalıştırın — customize var olan profili ayarlamak içindir."

2. **Haritayı göster** — her grup için güncel değerin tek satırlık özeti:
   - **Şirket / kimlik** — ad, sektör, ülkeler, şirket türü, halka açık mı, pratik ortamı *(ortak profil — tüm eklentilere yansır)*
   - **Active modules** — M&A, Board & Secretary, Public Company, Entity Management hangileri açık; açıp kapatmak hangi skill'in kurulum isteyeceğini değiştirir
   - **Risk iştahı** — temkinli / orta / atak; inceleme önemliliğine ve açıklama listesi kapsamına etkisi
   - **Kişiler** — işlem ekibi, YK sekreteri, şirket uyumu sorumlusu, mali müşavir, eskalasyon zinciri (`**Escalation:**`)
   - **M&A** — önemlilik eşikleri (sözleşme bedeli, çalışan sayısı, gelir; para birimiyle), güvenilen veri odaları, YZ toplu inceleme güven düzeyi (Luminance / Kira), işlem ekibi bilgilendirme sıklığı
   - **Board & Secretary** — `**Minutes template:**`, `**Consents repository:**`, `**Consent format:**`, karar defteri türü (fiziki / elektronik), komiteler, elden dolaştırma kapsamı
   - **Public Company** — KAP açıklama süreci, SPK finansal raporlama takvimi, kurumsal yönetim komiteleri
   - **Entity Management** — şirket tablosu, mali müşavir / yerel ajan, ülkeler, `compliance-tracker.yaml` rapor sıklığı
   - **İş akışı** — matter klasörleri, `closing-checklist.yaml` yeri, dataroom-watcher sıklığı
   - **Entegrasyonlar** — ArthurLegal MCP, `gleif_`, Box / Intralinks / Datasite, takvim, Slack ve geri dönüş yolları

3. **Sor:** "Neyi ayarlamak istersiniz? Bir bölüm seçin ya da değişikliği kendi sözlerinizle anlatın."

4. **Değiştir:** güncel değeri göster, yenisini al, aşağı akış etkisini söyle, onay al, yaz. Örnekler:
   - *Önemlilik eşiği 5 milyon TL → 10 milyon TL:* "`/diligence-issue-extraction` ve `/material-contract-schedule` artık 10 milyon TL'yi eşik alır; kayıtlı bulgular olduğu gibi kalır, geriye dönük uygulamak için yeniden çalıştırın."
   - *Public Company modülünü açma:* "O alanda bir şey çalıştırdığınızda KAP süreci ve SPK takvimini sorarım."
   - *YZ toplu inceleme güveni "her satırı kontrol et" → "%10 örneklem":* "`/ai-tool-handoff` artık çıkarımların %10'unu kontrol eder."
   - *Karar defteri fiziki → elektronik:* "entity-compliance YK karar defteri kapanış onayı kalemini takvimden düşürür (elektronik defterde açılış ve kapanış onayı aranmaz, TTK m. 64/3); written-consent onayların deftere geçirilmesini e-defter pratiğine göre not eder."

   Kullanıcı yeni bir kanun maddesi, nisap, süre ya da eşik söylerse yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; çelişki varsa göster ve hangisinin gireceğini sor. Dönemsel değişen eşikleri (bağımsız denetim eşikleri, Rekabet Kurulu izin eşikleri, idari para cezaları) sabit yazma.

5. **Ortak profil değişikliği** (ad, sektör, ülkeler, pratik ortamı, şirket türü): `firm-profile.md` dosyasına yaz ve söyle: "Bu değişiklik tüm eklentileri etkiler." Pratik ortamı büro ↔ şirket içi değişiyorsa `## Matter workspaces` → `Enabled` değerinin de değişmesi gerektiğini hatırlat.

6. **Kapat:** "Tamam, bir sonraki çıktı değişikliği yansıtır. Başka bir şey var mı? `/arthurlegal:corporate-legal-customize` her zaman çalışır."

## Korkuluklar

- **Bölüm silme.** "Kaldır" denirse `[Not configured]` yaz ve eklentinin davranışına etkisini anlat.
- **İç tutarsızlığı işaretle** — ör. Public Company modülü kapalı ama şirket halka açık; "atak" risk iştahı + çok düşük önemlilik eşiği; Ltd. şirket için GK'da Bakanlık temsilcisi adımı (Ltd.'de uygulanmaz, TTK m. 617/3); "sirküler karar oybirliğiyle" ev kuralı ile kanunun çoğunluk kuralı (m. 390/4) — ev kuralı esas sözleşmeden geliyorsa kaynağını yaz. Gerilimi göster, hangisini istediğini sor.
- **Korkuluk zayıflatmayı işaretle.** `[review]` bayrağı, üst başlık, kaynak etiketleri ve doğrulanmamış atıflardaki UYARI satırı yük taşır; kapatılmak istenirse neyi koruduğunu anlat ve bedeli anladığını teyit ettir.
- **Bölüm ve anahtar adlarını çevirme** — diğer skill'ler `## Board & Secretary`, `## Entity Management`, `*Active modules:*` gibi adları birebir okur.
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
| AZ istirak / JV yapisi, Azerbaycanli karsi taraf islemleri — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| yabanci sirketler hukuku karsilastirmasi, M&A yapisi ogretisi — **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| hedef sirketin maddi sozlesmelerinde kloz benchmark (diligence) | `/arthurlegal:legal-research-sozlesme-emsali` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`

---
