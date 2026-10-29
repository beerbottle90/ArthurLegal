---
name: corporate-legal-material-contract-schedule
description: >
  Pay/malvarlığı devir sözleşmesindeki (SPA/APA) "Önemli Sözleşme" tanımını
  due diligence bulgularına uygulayarak önemli sözleşmeler ekini kurar ve
  sözleşmenin ek formatına göre biçimlendirir; onay gerektirenleri (TBK m. 205,
  m. 323, 4735 m. 16, sözleşmedeki CoC) ayrı iç takip tablosuyla
  closing-checklist'e aktarır. "Sözleşmeler ekini kur", "açıklama eki",
  "Ek 3.X", "önemli sözleşmeler listesi" denildiğinde ya da açıklama ekleri
  taslaklanırken kullan.
argument-hint: "[satın alma sözleşmesi yolu ya da Önemli Sözleşme tanımını yapıştırın]"
---

# /material-contract-schedule — Önemli Sözleşmeler Eki

1. Satın alma sözleşmesini yükle → "Önemli Sözleşme" tanımı + ek formatı.
2. Tanımı due diligence bulgularına uygula; sınır vakaları işaretle.
3. Sözleşmenin formatına göre biçimlendir.
4. Onay takip tablosu closing-checklist'i besler.

## Matter bağlamı

Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:corporate-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Amaç

Satın alma sözleşmesinde bir beyan var: "Ek 3.X tüm Önemli Sözleşmeleri listeler." Bu skill o eki due diligence bulgularından kurar — sözleşmenin tanımına göre hangi sözleşmeler önemli, sözleşmenin istediği formatta. Türk hukukunda açıklama eki kanuni bir kurum değildir; içerik ve sonuç (beyan ve tekeffül ihlali, tazmin) tamamen satın alma sözleşmesine bağlıdır. Sözleşme yabancı hukuka tabiyse yorum o hukuka göre yapılır → `/arthurlegal:commercial-legal-governing-law-review`.

## Bağlam

- Satın alma sözleşmesi taslağı — "Önemli Sözleşme" tanımı ve ek formatı (İngilizce ya da iki dilli sözleşmede tanımlı terimi aynen kullan)
- `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → önemlilik eşikleri (sözleşme tanımından farklı olabilir — **sözleşmenin tanımı geçerlidir**)
- `diligence-issue-extraction` ve varsa `tabular-review` çıktısı — sözleşme düzeyinde veri
- `deals/[code]/deal-context.md` → işlem yapısı; [Müvekkil] satıcıysa ek onun beyanıdır (eksik ek = beyan ihlali riski), alıcıysa ekin eksiksizliğini due diligence'la karşılaştır

## Akış

### Adım 1: Tanımı al

Tanımı sözleşmeden çek; tanım belirleyicidir. İşlem yapısı (pay devri / malvarlığı devri / birleşme) bir kolun yorumunu değiştirebilir: pay devrinde "devri onaya bağlı sözleşme" kolu çoğu zaman CoC klozuyla birlikte okunur; malvarlığı devrinde her sözleşmenin devri karşı tarafın katılımını gerektirir (TBK m. 205). Düzenlenmiş sektör ya da kamu sözleşmesi varsa onay kuralları sözleşmenin dışında da yaşar:

| Katman | Kural | Dayanak |
|---|---|---|
| Kamu ihale sözleşmesi | Zorunlu hâllerde ihale yetkilisinin yazılı izniyle devir; devralanda ilk ihaledeki şartlar aranır; izinsiz devirde fesih ve yaptırım | 4735 m. 16 |
| İşyeri kirası | Kira ilişkisinin devri kiraya verenin yazılı rızasına bağlı; işyerinde haklı sebep olmadıkça rıza reddedilemez; devreden en fazla 2 yıl müteselsil | TBK m. 323 |
| Sınai mülkiyet lisansı/devri | Hukuki işlem yazılı; devir noter onaylı; sicile kaydedilmeyen işlem iyiniyetli üçüncü kişiye karşı ileri sürülemez | SMK m. 148/4-5 |
| Lisanslı faaliyet (enerji, bankacılık, sermaye piyasası, elektronik haberleşme, sigorta) | Pay devri ya da kontrol değişikliği için kurum onayı gerekebilir — ezberden yazma, kurum mevzuatını çek | `tr_mevzuat_ara`, `tr_kurum_karari_ara(kurum="epdk"/"bddk"/"spk"/"btk")` |

Tanımda sık görülen kollar — sözleşmeyi okumanın yerini tutmaz, sözleşmedeki liste geçerlidir: parasal eşik (yıllık / toplam), süre, CoC ya da devir yasağı, münhasırlık / rekabet yasağı, ilk N müşteri / tedarikçi, taşınmaz kiraları, fikrî hak lisansları (gelen / giden), ilişkili taraf sözleşmeleri, kamu sözleşmeleri, olağan iş akışı dışındaki sözleşmeler. Tanımı mekanik uygula: herhangi bir kolu karşılayan her sözleşme eke girer.

### Adım 2: Tanımı bulgulara uygula

| Sözleşme | Karşıladığı kol(lar) | Eke girer |
|---|---|---|
| [ad] | [yıllık X TL üstü; CoC m. 12.2] | Evet |
| [ad] | [yok] | Hayır |

**İnsan kararına işaretle:** eşiğin hemen altında ama iş için önemli; bir kolu karşılıyor ama zaten feshediliyor; sözlü anlaşma ya da yan mektup; dövizli bedelin TL karşılığı kura göre eşiğin iki yanına düşüyor (sözleşmenin kur ve tarih kuralını uygula, yoksa sor).

### Adım 3: Ek verisini topla

| Alan | Kaynak |
|---|---|
| Karşı taraf unvanı | Sözleşme (ticaret sicili kaydıyla teyit edilmiş unvan) |
| Sözleşme adı / türü | Sözleşme |
| Tarih | Sözleşme |
| Süre / bitiş | Sözleşme |
| Yıllık / toplam bedel ve para birimi | Sözleşme ya da yönetim verisi |
| Karşıladığı önemlilik kolu | Adım 2 |
| İşlem için onay gerekli mi | Due diligence bulgusu |
| VDR atfı | Due diligence envanteri |

Mevcut çıkarımlardan al. Eksik alanı işaretle — tahmin etme.

### Adım 4: Sözleşmenin formatına göre biçimlendir

Taslaktaki diğer eklerin biçimine uy (numaralı liste ya da tablo, sözleşme türüne göre alt bölümler).

```markdown
## Ek 3.[X] — Önemli Sözleşmeler

İşbu tarih itibarıyla Önemli Sözleşmeler aşağıdadır:

### (a) Müşteri Sözleşmeleri

1. [Hedef] ile [Karşı taraf] arasında [tarih] tarihli [Sözleşme Adı].
   [Format gerektiriyorsa kısa açıklama.]
   [VDR: yol]

### (b) Tedarikçi Sözleşmeleri
### (c) Taşınmaz Kiraları
### (d) Fikrî Hak Lisansları
[sözleşmedeki tanım yapısına göre alt bölümler]
```

Sözleşme İngilizce ya da iki dilliyse eki de aynı dilde/düzende kur; Türkçe karşılığı yalnız format gerektiriyorsa ekle.

### Adım 5: Onay takip tablosu

Ekin içinde değil, ayrı ve dahili olarak: hangi listelenmiş sözleşme onay gerektiriyor.

> Onay tablosu ve ekin teslim öncesi çalışma taslağı gizli due diligence malzemesinden türetilmiştir ve onun gizlilik statüsünü devralır; dağıtımı işlem ekibiyle sınırla (Av. K. m. 36 dağıtılan belgeyi korumaz). İmzalanan sözleşmeye eklenen ek ise işlem belgesidir, karşı tarafla paylaşılır — teslimden önce iç notları sil.

| Ek no | Karşı taraf | Onay gerekli | Dayanak | Durum | Sorumlu | Son gün |
|---|---|---|---|---|---|---|
| 3.X(a)(1) | [ad] | Evet — CoC | Sözleşme m. 12.2 | Talep edildi | [ad] | [tarih] |
| 3.X(c)(2) | [ad] | Evet — kira devri | TBK m. 323; kira m. 9 | Hazırlanıyor | [ad] | [tarih] |

Bu tablo closing-checklist'i besler (Mode 2 aktarım şeması: `counterparty`, `conditions`, `notice_deadline` alanlarını doldur).

## Çapraz kontrol

Teslimden önce:
- Bir kolu karşılayan her sözleşme ekte (eksiksizlik).
- Ekte, hiçbir kolu karşılamayan sözleşme yok (aşırı açıklama yok — bu bir beyandır, veri yığını değil).
- Ek diğer beyanlarla tutarlı (ekteki bir sözleşme rehin/teminat doğuruyorsa teminatlar ekinde de görünmeli).
- Her kaydın VDR atfı var; alıcı avukatı belgeyi bulabilmeli.

## Aktarımlar

- **diligence-issue-extraction'dan:** sözleşme düzeyindeki bulgular girdidir.
- **closing-checklist'e:** onay kalemleri kontrol listesine gider.

## Kapanış

CLAUDE.md `## Outputs`'taki sonraki adımlar karar ağacıyla bitir; dalları bu eke göre uyarla. Ağaç çıktıdır; seçimi avukat yapar.

## Bu skill ne yapmaz

- Önemlilik tanımını belirlemez — o satın alma sözleşmesindedir.
- Onay almaz — hangilerinin gerektiğini izler.
- Beyanı taslaklamaz — beyanın atıf yaptığı eki doldurur.

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
