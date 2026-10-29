---
name: regulatory-legal-comments
description: Görüşe açılan düzenleme taslaklarını ve istişareleri izler, görüş son tarihlerini gösterir, görüş verme kararını kaydeder. Bir kurum ya da bakanlık taslağı görüşe açtığında son tarihi görmek, görüş verip vermeme kararını almak ya da kararı kaydetmek (--decide CMT-ID) için kullan.
argument-hint: "[isteğe bağlı: --decide CMT-ID]"
---

# /comments

## Amaç

Türkiye'de düzenleyici kurumlar ve bakanlıklar taslak düzenlemeleri çoğu zaman internet sitelerinde görüşe açar; son tarih duyuruda yazar. Görüş verip vermemek avukatın kararıdır; risk, son tarihin kayıtlı bir karar olmadan geçip gitmesidir. Bu skill açık görüş sürelerini gösterir ve kararları kaydeder. Kural Resmî Gazete'de yayımlandıktan sonra ikinci bir süre başlar: düzenleyici işleme karşı dava süresi (aşağıda); o tarih de buraya yazılır.

> ABD ile karşılaştırma: ABD'deki zorunlu "notice-and-comment" usulünün (Federal Register'da NPRM) Türkiye'de genel ve bağlayıcı bir karşılığı yoktur. Aşağıdaki çerçeve ve kurum uygulaması geçerlidir.

## Hukuki çerçeve (doğrulanmış)

Aşağıda "m." atıfları, aksi yazılmadıkça Mevzuat Hazırlama Usul ve Esasları Hakkında Yönetmelik'e (RG 24.02.2022/31760) aittir.

- **Kapsam.** Yönetmelik Cumhurbaşkanlığı, bakanlıklar, bağlı, ilgili, ilişkili kurum ve kuruluşlar ile diğer kamu kurum ve kuruluşlarının hazırladığı mevzuat taslaklarını kapsar; milletvekillerinin TBMM'ye sunduğu kanun teklifleri kapsam dışıdır (m. 1/2, 1/3).
- **Paydaş görüşü.** Taslaklar hakkında ilgili mahallî idareler, üniversiteler, sendikalar, kamu kurumu niteliğindeki meslek kuruluşları ve sivil toplum kuruluşlarının; iş ve yatırım ortamına ilişkin taslaklarda ayrıca özel sektör paydaşlarının görüşlerinden faydalanılır (m. 6/4).
- **Kamuoyuna açma takdire bağlıdır.** Kamuoyunu ilgilendiren taslaklar Cumhurbaşkanlığına iletilmeden önce internet, basın veya yayın yoluyla kamuoyunun bilgisine sunulabilir; toplanan görüşler değerlendirildikten sonra teklifte bulunulur (m. 6/5). "Sunulabilir"dir; her taslak görüşe açılmaz.
- **Meslek kuruluşu ve STK süresi.** Görüşü istenen kamu kurumu niteliğindeki meslek kuruluşu ve sivil toplum kuruluşu görüşünü on beş gün içinde bildirir; süresinde bildirilmezse olumlu görüş verilmiş sayılır (m. 7/2). [Müvekkil] görüşünü bir oda, birlik ya da sektör derneği üzerinden iletecekse iç son tarihi bu süreye göre kur.
- **Yürürlük için makul süre.** Ekonomik ve ticari alan ile yatırım ortamını etkileyen düzenlemelerde mümkün olduğunca yayım ile yürürlük arasında makul süre bırakılır (m. 17/2). Kısa uyum süresi görüşte ileri sürülebilecek bir noktadır.
- **Dayanak sınırı.** Kanun, CB kararnamesi ve Cumhurbaşkanı kararıyla yürürlüğe konulanlar dışındaki taslaklarda, dayanağında belirtilenler dışında yükümlülük getiren hükme yer verilmez (m. 24/1-a). Dayanağı aşan yükümlülük görüşün güçlü bir başlığıdır.
- **Düzenleyici etki analizi.** Kanun ve CB kararnamesi taslakları içindir (Düzenleyici Etki Analizinin Uygulanmasına İlişkin Usul ve Esaslar m. 1, 4/1-ç); ilgili taraflar ve paydaşlarla istişare edilerek yapılır ve analiz raporunda danışılan paydaşların görüş ve önerilerine yer verilir (m. 6/5, 9/4).
- **Bağımsız kurulların kendi düzenlemeleri.** EPDK, BDDK, SPK, BTK, KVKK ve Rekabet Kurumu yönetmelik ve tebliğ taslaklarını sitelerinde görüşe açabilmektedir; bu bir kurum uygulamasıdır. Kurumun kendi kanununda ya da yönetmeliğinde görüş alma hükmü varsa bul ve yalnız çektiğin maddeye atıf yap: `tr_mevzuat_icinde_ara(number="<kurum kanunu>", query="görüş taslak")`, sonra `tr_mevzuat_madde_getir`. Bulamazsan kural yazma; "kurum uygulaması" de ve gerekirse şunu ekle: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.
- **Tartışmalı — içtihadı kontrol et:** Mevzuat Hazırlama Yönetmeliği'nin görüş alma usulünün bağımsız kurulların kendi düzenlemelerine ne ölçüde uygulandığı ve görüş alınmamasının düzenleyici işlemin iptal sebebi olup olmadığı. Ara: `tr_ictihat_ara(courts=["DANISTAYKARAR"], query="\"görüş alınmadan\" yönetmelik iptal")`; dönen kararın künyesini birebir kullan, karar numarasını ezberden yazma.

**Kural yayımlandıktan sonra.** Dava açma süresi özel kanununda ayrı süre yoksa Danıştay ve idare mahkemelerinde altmış gündür; ilanı gereken düzenleyici işlemlerde süre ilan tarihini izleyen günden başlar; ilgililer işlemin kendilerine uygulanması üzerine düzenleyici işlem ya da uygulama işlemi aleyhine de dava açabilir (İYUK m. 7/1, 7/4). Dava açılması işlemin yürütülmesini durdurmaz (İYUK m. 27/1). Özel kanunda farklı süre olup olmadığını ve görevli mercii `/arthurlegal:administrative-legal-idari-dava-prep` ile kontrol et.

## Bağlamı yükle

- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml` → izlenen tüm taslak ve istişareler.
- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` → `## Feed configuration` altındaki `**Comment tracking:**` ve `**Default comment decision owner:**`, `## Who's using this` → `**Role:**`.

Şema (anahtarlar ve değerler İngilizce kalır):

```yaml
comments:
  - id: CMT-001
    item_type: draft          # draft (görüşe açılmış taslak) | consultation (taslaksız istişare) | bill (TBMM kanun teklifi)
    regulator: "[kurum]"
    title: "[taslağın adı]"
    link: "[duyuru bağlantısı — uydurma]"
    source_tag: "[kurum sitesi]"   # ya da [kullanıcı verdi], [ikincil kaynak], [ArthurLegal TR — <araç> — GG.AA.YYYY]
    deadline: 2026-11-20      # duyurudaki son tarih; yoksa null ve not
    decision: undecided       # undecided | filing | not-filing | waived
    owner: "[ad]"
    owner_slack: "[kimlik]"
    rationale: ""
    final_publication: ""     # kural yayımlanınca: RG tarih/sayı
    challenge_deadline: ""    # kural yayımlanınca: dava süresinin son günü (hesap notuyla)
```

## Varsayılan görünüm — açık görüş süreleri

```markdown
## Görüş Süresi İzleyici — [tarih]

### ⏰ Son tarihe 14 günden az

| ID | Düzenleme | Tür | Son tarih | Kalan gün | Karar | Sahip |
|---|---|---|---|---|---|---|
| CMT-001 | [ad] | taslak | [tarih] | [N] | Karar yok | [sahip] |

### 🟡 Açık (14 günden fazla)

[aynı tablo]

### ⚖️ Yayımlanan kurallar — dava süresi işliyor

| ID | Düzenleme | RG | Dava süresinin son günü | Not |
|---|---|---|---|---|

### Son kararlar

| ID | Düzenleme | Karar | Gerekçe |
|---|---|---|---|
| CMT-002 | [ad] | not-filing | [gerekçe] |

---

**Toplam açık:** [N]  **30 günden az kalan ve kararsız:** [N]
```

Son tarihi belirtilmemiş kalemi "son tarih yok — kurumdan teyit et" diye ayrı satırda göster; tarih uydurma.

## Karar kaydet

```
/arthurlegal:regulatory-legal-comments --decide CMT-001
Decision: [filing / not-filing / waived]
Rationale: "[kısa — ör. 'Taslak bizim faaliyetimize uygulanmıyor' ya da 'Taslağın geçiş süresi ve 4. maddesi hakkında görüş vereceğiz']"
```

İzleyiciyi günceller. Karar `filing` ise iç inceleme hatırlatması öner: görüş son tarihinden 5 iş günü önce.

**Görüş metni.** Bu skill görüş yazmaz. EPDK taslağına görüş için `/arthurlegal:administrative-legal-epdk-proaktif-gorus`; diğer kurumlar için avukat taslağı. Görüş bir oda, birlik ya da sektör derneği üzerinden ortak verilecekse rakiplerle rekabete duyarlı bilgi (fiyat, maliyet, müşteri, kapasite planı) paylaşma: teşebbüsler arası anlaşma, uyumlu eylem ve teşebbüs birliklerinin rekabeti kısıtlayan kararları yasaktır (4054 m. 4). Ortak çalışmayı rekabet hukuku açısından avukata kontrol ettir.

## Bildirimler

Taslak ilk kez kaydedildiğinde (reg-feed-watcher tarafından) Slack ya da profildeki kanal bağlıysa ve `owner_slack` doluysa görüş karar sahibine mesaj. Kararsız kalırsa son tarihten 14 gün önce hatırlatma; hâlâ kararsızsa 3 gün önce yüksek öncelikli hatırlatma. Her mesaj gap-surfacer'daki gönderim başına onay kuralına tabidir: önizle, açık "evet" bekle, sonra gönder.

## Sonuç doğuran eylem kapısı (kuruma görüş sunma ya da cevap verme)

**Bir kararı `filing` olarak kaydetmeden önce — ve sunulmaya hazır bir görüş ya da kuruma cevap taslağı üretmeden önce her zaman:** profildeki `## Who's using this` bölümünü oku. Rol **Non-lawyer** ise:

> Bir kuruma görüş ya da cevap sunmak hukuki sonuç doğurur. Şirketin tutumunu kayda geçirir; kurum dosyasında kalır ve sonraki inceleme, denetim ya da davada şirket aleyhine kullanılabilir. Bunu bir avukatla incelediniz mi? Evetse devam ediyorum. Hayırsa avukata götüreceğiniz özet:
>
> - Düzenleme ya da istişare (kurum, taslak, son tarih)
> - Görüşün neyi söylediği ve hangi maddelere ilişkin olduğu
> - Açık sorular
> - Ne ters gidebilir (aleyhe ikrar, önceki tutumlarla çelişki, sektör derneği üzerinden ortak görüşte rekabet hukuku riski)
> - Avukata sorulacaklar (görüş verelim mi; dernek üzerinden mi verelim; hangi tutumu almayalım)
>
> Avukat bulmak için bağlı olduğunuz baroya başvurabilirsiniz.

Açık bir "evet" olmadan `filing` kararı kaydetme ve sunulmaya hazır taslak üretme. İzleme görünümleri, son tarih hatırlatmaları ve `not-filing` / `waived` kararları kapıya tabi değildir.

---

## Bu skill ne yapmaz

- Görüş metnini yazmaz; ayrı bir avukat işidir (EPDK için `/arthurlegal:administrative-legal-epdk-proaktif-gorus`).
- Görüş verme kararını vermez; kararı kaydeder, kararı avukat verir.
- Kurumların taslak duyurularını kendiliğinden bulmaz; ArthurLegal araçlarında taslak akışı yoktur. Duyuru sayfası profilde tanımlıysa reg-feed-watcher okur, değilse kullanıcı yapıştırır.
- Görüş sunulduktan sonraki süreci izlemez; kural yayımlanınca `/arthurlegal:regulatory-legal-reg-feed-watcher` yakalar, dava süresi buraya işlenir.

> `comment-decision` `gap_type` anlamı ve gönderim başına onay kuralı **gap-surfacer** referans skill'indedir; asıl işe başlamadan önce onu yükle.

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
