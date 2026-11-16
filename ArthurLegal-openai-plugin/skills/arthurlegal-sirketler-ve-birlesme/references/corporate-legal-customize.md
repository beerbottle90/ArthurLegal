# corporate-legal-customize

Kurumsal pratik profilinde tek bir şeyi, kurulum görüşmesini baştan yapmadan değiştirir: risk iştahı, eskalasyon kişileri, etkin modüller (M&A / Yönetim Kurulu ve Sekretarya / Halka Açık Şirket / Şirket Yönetimi), önemlilik eşikleri, açıklama listesi biçimi, YK karar ve GK tutanak formatı, elden dolaştırma emsalleri, şirket tablosu ve uyum takvimi, matter klasörleri. Kullanıcı "şunu değiştir", "profilimi güncelle", "ayarı değiştir" ya da "customize" dediğinde kullan.

# /customize

## Ne yapar

1. **Profili oku:** `Hafıza › Pratik/corporate-legal/PROFIL.md` ve bir üst düzeydeki ortak `../arthurlegal/references/firm-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa: "Kurulum henüz yapılmamış. Önce ``corporate-legal-cold-start-interview` iş akışı (`arthurlegal-sirketler-ve-birlesme` becerisi, `../arthurlegal-sirketler-ve-birlesme/references/corporate-legal-cold-start-interview.md`)` çalıştırın — customize var olan profili ayarlamak içindir."

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

6. **Kapat:** "Tamam, bir sonraki çıktı değişikliği yansıtır. Başka bir şey var mı? ``corporate-legal-customize` iş akışı (`arthurlegal-sirketler-ve-birlesme` becerisi, `../arthurlegal-sirketler-ve-birlesme/references/corporate-legal-customize.md`)` her zaman çalışır."

## Korkuluklar

- **Bölüm silme.** "Kaldır" denirse `[Not configured]` yaz ve eklentinin davranışına etkisini anlat.
- **İç tutarsızlığı işaretle** — ör. Public Company modülü kapalı ama şirket halka açık; "atak" risk iştahı + çok düşük önemlilik eşiği; Ltd. şirket için GK'da Bakanlık temsilcisi adımı (Ltd.'de uygulanmaz, TTK m. 617/3); "sirküler karar oybirliğiyle" ev kuralı ile kanunun çoğunluk kuralı (m. 390/4) — ev kuralı esas sözleşmeden geliyorsa kaynağını yaz. Gerilimi göster, hangisini istediğini sor.
- **Korkuluk zayıflatmayı işaretle.** `[review]` bayrağı, üst başlık, kaynak etiketleri ve doğrulanmamış atıflardaki UYARI satırı yük taşır; kapatılmak istenirse neyi koruduğunu anlat ve bedeli anladığını teyit ettir.
- **Bölüm ve anahtar adlarını çevirme** — diğer skill'ler `## Board & Secretary`, `## Entity Management`, `*Active modules:*` gibi adları birebir okur.
- **Tek seferde tek değişiklik** — görüşmeyi baştan sorma.

---

## Kaynak katmanı — /legal-research

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
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| AZ istirak / JV yapisi, Azerbaycanli karsi taraf islemleri — akt + statu | ``legal-research-az-mevzuat` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-az-mevzuat.md`)` |
| yabanci sirketler hukuku karsilastirmasi, M&A yapisi ogretisi — **ikincil** | ``legal-research-karsilastirmali-doktrin` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-karsilastirmali-doktrin.md`)` |
| hedef sirketin maddi sozlesmelerinde kloz benchmark (diligence) | ``legal-research-sozlesme-emsali` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-sozlesme-emsali.md`)` |

Rehberler: `../arthurlegal/references/eqanun-mcp-rehberi.md` · `../arthurlegal/references/lex-scholar-rehberi.md` · `../arthurlegal/references/resourcecontracts-rehberi.md` · `../arthurlegal/references/karsilastirmali-hukuk-rehberi.md` · `../arthurlegal/references/nl-rechtspraak-mcp-rehberi.md` · `../arthurlegal/references/pl-sejm-mcp-rehberi.md` · `../arthurlegal/references/at-ris-mcp-rehberi.md` · `../arthurlegal/references/ie-statutebook-mcp-rehberi.md` · `../arthurlegal/references/fi-finlex-mcp-rehberi.md` · `../arthurlegal/references/es-boe-mcp-rehberi.md`

---
