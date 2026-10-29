---
name: advocacy-legal-kamu-hukuku-dilekce
description: >
  Kamu (idari/anayasa) hukuku dilekçesi ÜRETİMİ — idari dava dilekçesi (İYUK m.2:
  iptal + tam yargı), yürütmenin durdurulması (m.27), istinaf BİM (m.45), temyiz
  Danıştay (m.46), AYM bireysel başvuru (6216, 30 gün). Süre haritası (m.7: 60/30,
  ÇED 30 m.20/A), görevli mahkeme (İdare Mah./Danıştay ilk derece). Örnek senaryolar:
  EPDK Kurul kararı iptali, ÇED ret/itiraz, idari para cezası, tam yargı tazminat.
user-invocable: true
---

# Kamu Hukuku Dilekçesi Üretimi (İYUK + AYM)

> Bu skill idari/anayasa yargısı **dilekçe metnini** üretir. Görevli mahkeme/süre/strateji *tespiti* için `/arthurlegal:administrative-legal-idari-dava-prep` (önce onu çalıştırmak güçlü olur); bu skill tespiti alıp **dilekçeyi yazar**. Her taslak **dış idari avukat + [Baş Hukuk Müşaviri] onayı** ile sunulur.

## ⏰ ÖN-KONTROL — SÜRE (her çalıştırmada, HAK DÜŞÜRÜCÜ)

| İşlem | Süre | Dayanak |
|---|---|---|
| İdare mahkemesi iptal davası | **60 gün** (tebliğ/öğrenme) | İYUK m.7 |
| **Vergi** mahkemesi davası | **30 gün** | İYUK m.7 (tax-legal) |
| **ÇED** kararı (RES/HES/jeotermal) | **30 gün** — m.20/A ivedi yargılama (BİM YOK, doğrudan Danıştay temyiz **15 gün**) | İYUK m.20/A |
| İstinaf (BİM) | **30 gün** | İYUK m.45 |
| Temyiz (Danıştay) | **30 gün** (ÇED ivedi: 15 gün) | İYUK m.46 / m.20/A |
| **AYM bireysel başvuru** | **30 gün** (kesinleşmeden/öğrenmeden) | 6216 m.47/5 |
| Üst makama başvuru (m.11) | dava açma süresi (60 / vergi 30 gün) içinde; başvuru süreyi durdurur, 30 gün cevap yoksa zımni ret; ret/zımni ret sonrası süre kaldığı yerden işler (başvuruya kadar geçen süre hesaba katılır) | İYUK m.11 |

⚠️ **m.11 üst makama başvuru ÇED ivedi yargılama süresini DURDURMAZ.** Kalan < 5 gün → 🔴.

## ADIM 0 — Görevli mahkeme (kritik; idari-dava-prep ile teyit)

Türk idari yargı **3 dereceli**: İdare Mahkemesi → BİM → Danıştay (temyiz). **Danıştay ilk derece sadece istisnada** (Danıştay K. m.24): CB kararları, Cumhurbaşkanınca çıkarılan ve CB kararnamesi dışında kalan düzenleyici işlemler (CB kararnamesinin denetimi AYM'dedir — AY m.148), bakanlık/kamu kurumlarının **ülke çapında uygulanacak** tebliğ/yönetmeliği (normatif düzenleyici işlem).
- **EPDK bireysel Kurul kararı (lisans iptali/ceza/ret)** → **Ankara İdare Mahkemesi** (kurum Ankara) → BİM → Danıştay 13. Daire (temyiz)
- **EPDK/bakanlık genel yönetmelik/tebliğ** → doğrudan **Danıştay** (ilk derece)
- **ÇED ret/«ÇED gerekli değildir» iptali** → yer İdare Mahkemesi (projenin ili) → m.20/A ivedi → Danıştay 10./14. Daire
- **İdari para cezası (ÇŞB/EPDK/Rekabet)** → İdare Mahkemesi (idari yaptırımın türüne göre; bazı cezalar sulh ceza/idare ayrımı — kontrol)

## ADIM 1 — Dava türü ve dilekçe tipi

| Talep | Tür | Not |
|---|---|---|
| İdari işlemin **iptali** | İptal davası (İYUK m.2/1-a) | + yürütmeyi durdurma (m.27) |
| İdari işlem/eylemden **zarar tazmini** | Tam yargı davası (m.2/1-b) | iptal ile birlikte veya ayrı |
| Aleyhe ilk derece kararı | İstinaf dilekçesi (m.45) | BİM |
| Aleyhe BİM kararı | Temyiz dilekçesi (m.46) | Danıştay |
| İç hukuk tükendi + temel hak ihlali | **AYM bireysel başvuru** (6216) | 30 gün |

## ADIM 2 — İptal sebepleri (yetki/şekil/sebep/konu/maksat)

Klasik beş sakatlık (her birini somutla):
- **Yetki:** İdare/Kurul bu işlemi yapma yetkisinde mi? (görev gaspı, fonksiyon/yer/zaman yetkisizliği)
- **Şekil:** usul kuralları (gerekçe, savunma hakkı, oybirliği/çoğunluk, süre, ilan) — EPDK soruşturmasında savunma alınmış mı?
- **Sebep:** dayanılan maddi/hukuki sebep gerçek ve doğru mu?
- **Konu:** işlemin sonucu kanuna aykırı mı?
- **Maksat:** kamu yararı dışında amaç (örtülü amaç)?

## ADIM 3 — Yürütmenin durdurulması (İYUK m.27 — KRİTİK)

Talep şart, otomatik gelmez. **İki şart birlikte:**
1. **Telafisi güç/imkansız zarar:** EPDK lisans askısı → üretim duruşu → günlük X TL gelir kaybı; ÇED ret → yatırım dondurma; idari ceza tahsili.
2. **Açıkça hukuka aykırılık:** en güçlü iptal sebebi.
→ Dilekçede ayrı başlık. (İYUK m.20/A ivedi yargılamada YD rejimi özeldir — tek dilekçe, kısa süreler.)

## ADIM 4 — Emsal (ArthurLegal MCP (`tr_`))

```
tr_ictihat_ara(query="<konu> iptal yürütmenin durdurulması",
  chamber="13. Daire" /* EPDK/Rekabet */ veya "10. Daire"/"14. Daire" /* ÇED/çevre */,
  date_from="2022-01-01")
tr_kurum_karari_ara (kurum="rekabet") / tr_kurum_karari_ara (kurum="kik") / tr_kurum_karari_ara (kurum="kvkk")  /* kurum birincil */
```
Yalnızca çekileni dilekçeye işle: `[ArthurLegal TR — Danıştay 13.D — Esas/Karar — GG.AA.YYYY]`.

## ADIM 5 — İdari dava dilekçesi taslağı (İYUK m.3 zorunlu unsurlar)

```markdown
[GÖREVLİ MAHKEME] BAŞKANLIĞI'NA
[örn. ANKARA NÖBETÇİ İDARE MAHKEMESİ / DANIŞTAY ( ) DAİRESİ BAŞKANLIĞI'NA]
                                         — YÜRÜTMENİN DURDURULMASI TALEPLİDİR —

DAVACI            : [Müvekkil / Şirket] — [VKN], [adres]
VEKİLİ            : Av. [ad], [baro/sicil], [KEP]
DAVALI            : [T.C. EPDK / Çevre, Şehircilik ve İklim Değişikliği Bakanlığı / ...]
D. KONUSU         : Davalı idarenin [GG.AA.YYYY tarih, [...] sayılı] [Kurul kararı/işlemi]
                    nın İPTALİ ile öncelikle YÜRÜTMENİN DURDURULMASI [ve uğranılan
                    [tutar] TL zararın tam yargı olarak tazmini] talebidir.
TEBLİĞ/ÖĞRENME    : GG.AA.YYYY → dava süresi [60/30] gün → son tarih GG.AA.YYYY

I. OLAYLAR (idari süreç kronolojisi, işlemin tarif ve tarih/sayısı)

II. HUKUKA AYKIRILIK NEDENLERİ
  A. Yetki yönünden  B. Şekil/usul yönünden (savunma hakkı/gerekçe)
  C. Sebep yönünden  D. Konu yönünden  E. Maksat yönünden
  [her biri + emsal: [ArthurLegal TR — Danıştay …]]

III. YÜRÜTMENİN DURDURULMASI (İYUK m.27)
  1. Telafisi güç/imkansız zarar [somut: üretim/lisans/gelir]
  2. Açıkça hukuka aykırılık [en güçlü sebep]

IV. [TAM YARGI — varsa zarar kalemleri ve hesap]

HUKUKİ SEBEPLER   : 2577 İYUK, 6446 EPDK/Elektrik Piyasası K., 2872 Çevre K.,
                    ilgili yönetmelikler `[ArthurLegal TR — GG.AA.YYYY]`
DELİLLER          : Dava konusu işlem ve tebliği (EK), idari dosya (m.20 ara kararı
                    ile celbi talebi), bilirkişi, keşif, her tür yasal delil.

SONUÇ VE TALEP    : 1. Öncelikle yürütmenin durdurulmasına,
                    2. Dava konusu işlemin iptaline,
                    3. [Tazminata,] 4. Yargılama gideri + vekalet ücretinin
                    davalı idareye yükletilmesine karar verilmesini arz/talep ederiz.
                                                          GG.AA.YYYY — Davacı Vekili
EKLER: 1. Vekaletname  2. İşlem/tebliğ örneği  3. ...
```

> İstinaf/temyiz dilekçesinde: kararın özeti + bozma/kaldırma sebepleri (hukuka aykırılık + eksik inceleme) + YD talebi. **AYM bireysel başvuruda:** resmi başvuru formu, ihlal edilen Anayasa/AİHS hakkı (mülkiyet m.35, adil yargılanma m.36), olağan yolların tüketildiği, 30 gün, esasa etki/anayasal önem ölçütü.

## ADIM 6 — Sektörel/örnek senaryolar kontrolleri

- [ ] **EPDK lisans askısı/iptali riski** → derhal [Baş Hukuk Müşaviri] + [Genel Müdür]; üretim/gelir etkisi YD gerekçesi
- [ ] **ÇED ivedi yargılama (m.20/A)** → BİM yok, süreler kısa (30/15 gün) — takvime işle
- [ ] **HES su kullanım (DSİ) / orman izni** paralel dava → süre/merci ayrı kontrol
- [ ] **Rekabet/KVKK Kurulu kararı** → ilgili Daire (13.) + kurum birincil karar emsali
- [ ] **Finansör/kreditör ilgili veya yüksek etki** → eskalasyon + (gerekirse) ESG/PS bağlamı

## Çıktı

```markdown
[ÜST BAŞLIK]
# Kamu Hukuku Dilekçesi — [tip] — [işlem]

## ⚠️ İnceleyen notu
- **Görevli mahkeme:** [tespit] (gerekçe) `[review]`
- **Süre:** son tarih GG.AA.YYYY (kalan N gün) — [60/30/15/AYM 30] 🔴/🟠/🟡
- **Yürütmeyi durdurma:** [evet — gerekçe]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [✓/✗]; ArthurLegal MCP (`tr_`) (Danıştay/kurum) [✓ N / ✗]
- **Onay:** dış idari avukat + [Baş Hukuk Müşaviri] şart

## Dilekçe taslağı
[doldurulmuş]

## Sonraki adımlar
> 1. **idari-dava-prep ile strateji teyidi** — `/arthurlegal:administrative-legal-idari-dava-prep`
> 2. **EPDK proaktif görüş** (dava yerine dialog şansı) — `/arthurlegal:administrative-legal-epdk-proaktif-gorus`
> 3. **Dış idari avukat brief** — `/arthurlegal:litigation-legal-outside-counsel-brief`
> 4. **Süre/duruşma takvimi** — `/arthurlegal:advocacy-legal-yazihane-asistani`
> 5. **Başka**

**One question I'd ask:** [örn. "İşlem kesinleşmeden önce m.11 üst makama başvuru ile çözüm denenmeli mi? ÇED ivedi rejiminde süreyi durdurmaz; bunu bilerek karar vermeliyiz."]
```

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
> **Meslek sirri (Av. K. m. 36):** uc MCP de PUBLIC arama aracidir — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| dilekce gerekcesini guclendiren Turk doktrini — DergiPark 19 hukuk dergisi (ceza → Ceza Hukuku ve Kriminoloji, idari → Idare Hukuku ve Ilimleri) — **ikincil**, dilekcede birincil kaynakla birlikte kullan | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| uyusmazlik AZ hukukuna tabiyse akt lafzi + **yururluk statusu** | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
