---
name: corporate-legal-ai-tool-handoff
description: >
  Luminance, Kira ya da benzeri bir toplu inceleme aracı kullanıldığını tespit
  eder, yüksek hacimli kloz çıkarımını ona devreder ve dönen çıktıyı
  `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`'deki
  güven düzeyine göre kalite kontrolünden geçirir; ardından Türk hukuku
  yargı katmanını (işlem yapısına göre CoC/devir gerçekten tetikleniyor mu —
  TBK m. 205, TTK m. 153) uygular. "Luminance'a gönder", "toplu inceleme",
  "yapay zekâ çıkarımı" denildiğinde ya da diligence-issue-extraction yüksek
  hacimli bir kategoriye geldiğinde kullan.
---

# /ai-tool-handoff — Toplu İnceleme Aracına Devir

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Luminance ve Kira tek bir işte iyidir: 500 sözleşmeyi okuyup her kontrol değişikliği klozunu bulmak. Yargıda zayıftır: belirli bir CoC hükmünün bu işlem yapısında gerçekten tetiklenip tetiklenmediğine karar vermek. Bu skill toplu çıkarımı doğru araca verir, dönen sonuca kalite kontrolü ve yargı katmanını uygular.

**Devretmeden önce:** `/arthurlegal:corporate-legal-tabular-review`'i dene. Ortamın kaldırabildiği işte (birkaç yüz belge, tanımlı sütun şeması) yerel tablolu inceleme daha hızlı kurulur, belge başı maliyeti yoktur ve iş ürünü yerelde kalır. Korpus gerçekten çok büyükse, ekibin lisansı ve iş akışı zaten varsa ya da matter doğrulanmış bir köken zinciri olan araç gerektiriyorsa devret.

## Bağlam

CLAUDE.md → `## M&A` YZ toplu inceleme aracı ayarı (`AI-assisted review`): kullanılan araç (Luminance / Kira / yok), ne için kullanıldığı (hangi kloz türleri), güven düzeyi (olduğu gibi kullan / örneklem kontrolü / tam yeniden inceleme), devir süreci (kim yükler, kim kontrol eder). CLAUDE.md araç yok diyorsa bu skill işlem yapmaz; her şey doğrudan diligence-issue-extraction'dan geçer.

## Ne zaman devret

Hepsi birlikte varsa: kategoride 50'den fazla belge (altında okumak daha hızlı); çıkarım hedefi aracın iyi olduğu kloz türü (CoC, devir, münhasırlık, MFN, fesih, otomatik yenileme); belgeler makul ölçüde tek tip (aynı kâğıt üzerinde müşteri sözleşmeleri — sözleşme, mektup ve YK kararı karışımı değil).

Devretme: özel ya da yoğun müzakere edilmiş belgeler; yan mektuplar ve tadiller (ana sözleşmeyle etkileşimi araç kaçırır); sorunun "bu kloz var mı" değil "bu işlem için ne anlama geliyor" olduğu her şey.

**Türkçe belgeler.** Aracın Türkçe metinde (özellikle taranmış, OCR'lı belgelerde ve Türkçe karakterlerde) başarısı bu ekipte ölçülmediyse "olduğu gibi kullan" güven düzeyini uygulama; en az örneklem kontrolü öner ve CLAUDE.md'ye not düşmeyi teklif et.

**Kişisel veri ve gizlilik.** Kişisel veri içeren belgeleri üçüncü taraf platforma yüklemek, platformla veri işleyen ilişkisini ve aktarım kurallarını (KVKK m. 8) gündeme getirir — yurt içi hizmet sağlayıcıya iletimin nitelendirilmesi **tartışmalı**; platform sunucusu yurt dışındaysa veri işleyenleri de kapsayan yurt dışına aktarım kuralları uygulanır (KVKK m. 9: yeterlilik kararı ya da uygun güvenceler, standart sözleşmenin 5 iş günü içinde Kurula bildirimi). Hangi işleme ve aktarım şartının uygulanacağı olaya bağlıdır — yüklemeden önce `/arthurlegal:privacy-legal-dpa-review` ile platform sözleşmesini kontrol ettir; gerekirse çalışan dosyaları gibi kişisel veri yoğun klasörleri partiden çıkar ya da maskele. Müvekkil sırrı için de aynı dikkat: platformun hizmet koşulları gizliliği nasıl düzenliyor?

## Devir

### Adım 1: Partiyi hazırla

VDR envanterinden belgeleri seç; CLAUDE.md'ye göre çıkarım hedeflerini belirt; çıktının süzülebilmesi için önemlilik eşiğini not et.

### Adım 2: Yükle (ya da yükleyene talimat ver)

CLAUDE.md kimin yüklediğini söyler. Sen isen yükleme talimatını üret; başkasıysa talebi:

```markdown
## [Araç] Yükleme Talebi — [işlem kodu] — [kategori]

**Belgeler:** VDR klasörü [yol]'dan [N] belge
**Yüklenecek yer:** [araç çalışma alanı / matter]
**Çıkarım hedefleri:**
- Kontrol değişikliği / devir (birleşme, bölünme, tür değiştirmeye atıflar dahil)
- Münhasırlık
- [CLAUDE.md'ye göre diğerleri]
**Çıktı süzgeci:** yalnız hedefin bulunduğu belgeleri işaretle — her belge için "CoC yok" satırı gerekmez.
**Dönüş tarihi:** [tarih]
```

### Adım 3: Kalite kontrolü

Araç sonuç döndürünce güven düzeyini uygula:
- **"Olduğu gibi kullan":** doğrudan bulgulara al. (Yalnız CLAUDE.md böyle diyorsa — nadirdir.)
- **"%X örneklem kontrolü":** işaretlenen belgelerin %X'ini rastgele seç; her birinde gerçek klozu oku ve aracın çıkarımıyla karşılaştır. Hata oranı düşükse partiyi kabul et; hata varsa örneklemi genişlet.
- **"İşaretlenenlerin tamamını insan okur":** araç evreni daraltır (500 belge → CoC'li 80); insan 80'in hepsini okur. Araç temiz 420'yi okuma zamanını kazandırmıştır.

### Adım 4: Yargı katmanı

Araç klozları buldu; şimdi her CoC/devir hükmü için sor: **bu işlem onu gerçekten tetikliyor mu?**
- **İşlem yapısı:** pay devrinde sözleşmenin tarafı değişmez — yalnız CoC klozu tetiklenir, devir yasağı tetiklenmez. Malvarlığı/işletme devrinde sözleşmenin devri karşı tarafın katılımını ya da izni/onayını gerektirir (TBK m. 205) — devir hükmü sessiz olsa bile. Birleşmede tescille aktif ve pasif kendiliğinden geçer (TTK m. 153/1); sözleşmedeki devir yasağının birleşmeye uygulanması **tartışmalı — içtihadı kontrol et**, metin birleşmeyi açıkça anıyorsa ona göre.
- **"Kontrol" tanımı:** pay çoğunluğu mu, YK çoğunluğunu seçme hakkı mı, dolaylı kontrol mü, başka bir şey mi? Üst şirket düzeyindeki işlem dolaylı kontrolü değiştiriyor mu?
- **İstisna:** grup içi yeniden yapılanma, halka arz ya da bu tür işlem için bir istisna var mı?
- **Uygulanacak hukuk:** sözleşme yabancı hukuka tabiyse yorumu o hukuka göre çek (`uk_`, `de_`, `eu_`, `nl_` …) ya da `/arthurlegal:commercial-legal-governing-law-review`.

Bu, aracın yapamadığı kısımdır. Sonuç büro formatında due diligence bulgularına gider.

## Çıktı

> Aşağıdaki kalite kontrol özeti gizli VDR belgelerinden türetilmiştir ve onların gizlilik statüsünü devralır; dağıtımı işlem ekibiyle sınırla (Av. K. m. 36 dağıtılan belgeyi korumaz).

```markdown
## Toplu İnceleme Devri Özeti — [kategori]

**Araç:** [Luminance / Kira]   **İşlenen belge:** [N]   **Hedefler:** [kloz türleri]
**İşlem yapısı:** [pay devri / malvarlığı devri / birleşme]

### Kalite kontrolü
**Güven düzeyi:** [CLAUDE.md'ye göre]
**Örneklem:** [N] belge   **Hata oranı:** %[X] — [Kabul / Örneklem genişletildi / Tam yeniden inceleme]

### Sonuçlar
| Kloz türü | İşaretlenen | Yargı katmanı sonrası | Önemli |
|---|---|---|---|
| Kontrol değişikliği | [N] | [N — bu yapıda gerçekten tetiklenen] | [N — eşik üstü] |
| Devir | [N] | [N] | [N] |

**→ due diligence bulgularına [N] sorun eklendi**
**→ kapanış listesine [N] onay eklendi**
```

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu çıktıya göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Luminance ya da Kira'yı çalıştırmaz — devri ve kalite kontrolünü yönetir; çıkarımı insan ya da aracın kendi arayüzü yapar.
- Aracın çıktısını tamamen kendi yargısıyla değiştirmez — CLAUDE.md %10 diyorsa %10 kontrol eder, %100 değil.
- Güven düzeyine karar vermez — o, cold-start'ta ekibin araç deneyimine göre CLAUDE.md'ye yazılmıştır.

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
