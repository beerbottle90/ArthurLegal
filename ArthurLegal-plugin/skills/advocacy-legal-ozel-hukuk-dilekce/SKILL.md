---
name: advocacy-legal-ozel-hukuk-dilekce
description: >
  Özel hukuk (HMK 6100) dava dilekçesi ÜRETİMİ — dava dilekçesi (m.119), cevap
  dilekçesi (m.129), replik/düplik, istinaf (m.341+, 2 hafta), temyiz (m.361+),
  ihtiyati tedbir (m.389). Görevli/yetkili mahkeme, TTK m.5/A zorunlu arabuluculuk
  dava şartı, zamanaşımı, deliller, emsal içtihat (ArthurLegal MCP (`tr_`)). Örnek senaryolar:
  EPC/vendor ticari, tazminat, alacak, tespit, iş davası (işveren), HES su/ecrimisil.
user-invocable: true
---

# Özel Hukuk Dilekçesi Üretimi (HMK)

> Bu skill dava **dilekçe metnini** üretir. Dava *stratejisi/ön-değerlendirmesi* için `/arthurlegal:litigation-legal-case-intake`. Her taslak **dış vekil + Baş Hukuk Müşaviri ([Baş Hukuk Müşaviri]) onayı** ile sunulur.

## ⏰ ÖN-KONTROL — SÜRE (her çalıştırmada)

| Dilekçe | Süre | Dayanak |
|---|---|---|
| **Cevap dilekçesi** | **2 hafta** (tebliğden) — bir defaya mahsus 1 ay ek süre (m.127) | HMK m.127 |
| Replik (davacı cevaba cevap) | 2 hafta | HMK m.136 |
| Düplik (davalı ikinci cevap) | 2 hafta | HMK m.136 |
| **İstinaf** | **2 hafta** (gerekçeli karar tebliği) | HMK m.345 |
| **Temyiz** | **2 hafta** (BAM kararı tebliği) | HMK m.361 |
| İstinaf/temyiz **cevap** | 2 hafta | HMK m.347/m.366 |
| Bilirkişi raporuna itiraz | 2 hafta | HMK m.281 |

Kalan < 5 gün → 🔴 ACİL (dış vekille derhal koordine). Süre hak düşürücü/kesin — kaçırma = hak kaybı.

⚠️ Cevap süresi **dava dilekçesinin tebliğinden** işler; tensiple verilen süreyi teyit et.

## Destination check

- **Mahkemeye sunulacak dilekçe** → üst başlık YOK; en üste `TASLAK – DIŞ VEKİL/BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN SUNMAYINIZ`
- **İç değerlendirme / Baş Hukuk Müşaviri onayı** → `GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU`
- **Dış vekile revize için** → `DAVA BRIEF – AVUKATLIK K. m. 36 KAPSAMINDA`

## ADIM 1 — Dilekçe tipini ve rolü belirle

| Rolümüz | Tip | Not |
|---|---|---|
| Davacı (biz açıyoruz) | **Dava dilekçesi** (HMK m.119) | + gerekirse ihtiyati tedbir (m.389) |
| Davalı (bize açıldı) | **Cevap dilekçesi** (HMK m.129) | süre kritik |
| Davacı | Replik (cevaba cevap) | yeni vakıa/itiraz |
| Davalı | Düplik | |
| Aleyhe karar | **İstinaf dilekçesi** (m.342) | BAM |
| Aleyhe BAM kararı | **Temyiz dilekçesi** (m.361) | Yargıtay |

## ADIM 2 — Görevli ve yetkili mahkeme (dava dilekçesi ise)

**Görev (kesin, re'sen):**
- **Asliye Ticaret Mahkemesi (ATM)** — TTK m.4 mutlak/nispi ticari iş (EPC, vendor, tedarik, toptan satış uyuşmazlığı) — dosyaların çoğu
- Asliye Hukuk — genel
- İş Mahkemesi — 4857 (işçi-işveren; santral/saha personeli)
- Sulh Hukuk — kira, paylı/elbirliği mülkiyet
- Tüketici Mahkemesi/Hakem Heyeti — TKHK (nadir)

**Yetki (HMK):**
- Genel: davalının yerleşim yeri — şirkette merkezi (m.6; TMK m.51) / şube işlemlerinden doğan davada şubenin bulunduğu yer de (m.14/1)
- Sözleşmesel yetki klozu (m.17 — tacirler arası geçerli) → öncelik
- Haksız fiil: fiilin işlendiği/zararın doğduğu yer (m.16)
- Taşınmaz (HES/arazi/ecrimisil): taşınmazın bulunduğu yer (m.12) — **kesin yetki**

`[ArthurLegal MCP (`tr_`)]` ile teyit. Yanlış görev/yetki → görevsizlik/yetkisizlik kararı + gönderme (m.20); süre korunsa da gecikme/masraf.

## ADIM 3 — TTK m.5/A zorunlu arabuluculuk (DAVA ŞARTI)

Konusu **bir miktar para olan alacak, tazminat, itirazın iptali, menfi tespit ve istirdat** davası olan **ticari davalarda** dava açmadan önce **zorunlu arabuluculuk** (dava şartı; TTK m.5/A, 7445 s.K. ile genişletilmiş hâli).
- [ ] Ticari iş mi (TTK m.4)? [ ] Konusu bir miktar para olan alacak/tazminat/itirazın iptali/menfi tespit/istirdat davası mı? [ ] Kapsam dışı mı? (ihtiyati tedbir/haciz tek başına açılabilir)
- Kapsama giriyorsa: arabuluculuk **son tutanağı** (aslı/onaylı örneği) dava dilekçesine eklenmeli; eklenmemişse mahkeme 1 haftalık kesin süre verir, sunulmazsa usulden ret; **arabulucuya hiç başvurulmadan** dava açılmışsa doğrudan **dava şartı yokluğundan usulden ret** (HUAK m.18/A-2; HMK m.114/2, m.115).

> İş davaları (7036) ve tüketici davaları için de ayrı zorunlu arabuluculuk rejimi vardır — kontrol et.

## ADIM 4 — Zamanaşımı / hak düşürücü süre

| Talep | Süre | Madde |
|---|---|---|
| Sözleşmeye aykırılık (genel) | 10 yıl | TBK m.146 |
| Ticari satım/eser/hizmet | 5 yıl (eser m.147) / 10 yıl | TBK m.147/146 |
| Haksız fiil tazminatı | 2 yıl (öğrenme) / 10 yıl (mutlak) | TBK m.72 |
| İş alacağı (kıdem/ihbar/ücret) | 5 yıl | 4857 / TBK |
| Ecrimisil | 5 yıl geriye (doğrulanmadı) | Yargıtay içtihadı |

Kullanıcı zamanaşımı tarihi verdiyse **önce doğrula** (no silent supplement).

## ADIM 5 — Vakıa + hukuki sebep + delil iskeleti

- **Vakıalar:** kronolojik, somut, tarih/sayı/tutar ile. Her vakıaya bağlanacak delil.
- **Hukuki sebepler:** ilgili TBK/TTK/HMK maddeleri — `[ArthurLegal MCP (`tr_`)]` ile metni çek.
- **Deliller (HMK m.119/1-f):** sözleşme, ihtarname, e-yazışma/KEP, fatura, ticari defterler (HMK m.222), tanık (m.240), bilirkişi (m.266), keşif (m.288), yemin. **Somutlaştırma yükü** (m.194) — her delili hangi vakıa için gösterdiğini belirt.

## ADIM 6 — Emsal içtihat (ArthurLegal MCP (`tr_`))

```
tr_ictihat_ara(query="<uyuşmazlık konusu anahtar kelimeler>",
  chamber="<ilgili Yargıtay HD, örn. 11. HD/15. HD/9. HD>", date_from="2022-01-01")
```
Lehte/aleyhte eğilimi göster, dilekçeye **yalnızca çekilen** kararı işle: `[ArthurLegal TR — Yargıtay X.HD — Esas/Karar — GG.AA.YYYY]`. **Uydurma içtihat yazma.**

## ADIM 7 — Dilekçe taslağı (HMK m.119 zorunlu unsurlar)

```markdown
[NÖBETÇİ/İLGİLİ] ... MAHKEMESİ SAYIN HAKİMLİĞİ'NE
[ATM ise: ... ASLİYE TİCARET MAHKEMESİ'NE]

DAVACI            : [Müvekkil / Şirket] — [VKN], [adres]
VEKİLİ            : Av. [ad soyad], [baro] Baro sicil [no], [KEP/adres]
DAVALI            : [ad/unvan] — [adres]
KONU              : [örn. fazlaya ilişkin haklar saklı kalmak kaydıyla
                    [tutar] TL alacağın/tazminatın temerrüt faiziyle tahsili] talebidir.
HARCA ESAS DEĞER  : [tutar] TL
ARABULUCULUK      : [Anlaşmama tutanağı tarih/no — EK-1] (TTK m.5/A)

AÇIKLAMALAR
1. [Vakıa — kronolojik, delil atfı] (EK-...)
2. [Vakıa ...]
...
[Karşı tarafın temerrüdü / ihlal / zarar — somut]

HUKUKİ SEBEPLER   : TBK m. [...], TTK m. [...], HMK ve ilgili mevzuat.
                    `[ArthurLegal TR — GG.AA.YYYY]`
DELİLLER          : Sözleşme (EK-...), ihtarname (EK-...), e-yazışma/KEP,
                    fatura, ticari defterler (HMK m.222), bilirkişi, tanık,
                    keşif, yemin ve her türlü yasal delil.
EMSAL             : [ArthurLegal TR — Yargıtay X.HD — Esas/Karar — GG.AA.YYYY] (varsa)

SONUÇ VE TALEP    : Yukarıda açıklanan nedenlerle;
  1. Fazlaya ilişkin haklarımız saklı kalmak kaydıyla [tutar] TL'nin
     [temerrüt/avans faizi] ile davalıdan tahsiline,
  2. Yargılama giderleri ve vekalet ücretinin davalıya yükletilmesine,
  karar verilmesini saygıyla vekaleten talep ederiz. GG.AA.YYYY

                                              Davacı Vekili
                                              Av. [ad soyad] [imza/e-imza]
EKLER: 1. Vekaletname  2. Arabuluculuk anlaşmama tutanağı  3. Sözleşme  4. ...
```

> Cevap dilekçesinde: **ilk itirazlar** (HMK m.116 — kesin yetki kuralı bulunmayan hâllerde yetki itirazı [yetki sözleşmesi dâhil] ve tahkim itirazı; cevap dilekçesinde ileri sürülmezse dinlenmez, m.117) — görev, kesin yetki ve derdestlik ilk itiraz değil **dava şartıdır** (m.114/1-c, ç, ı), zamanaşımı def'i, vakıaların ayrı ayrı cevabı (m.129/1-d — inkar/kabul/bilmeme), karşı deliller.

## ADIM 8 — Sektörel/örnek senaryolar kontrolleri

- [ ] **EPC/vendor uluslararası** → governing law/tahkim klozu var mı? (ICC/LCIA) → `/arthurlegal:commercial-legal-governing-law-review`; varsa Türk mahkemesinde **tahkim ilk itirazı** (m.116/1-b)
- [ ] **HES su kullanım / ecrimisil / kamulaştırma** → taşınmaz kesin yetki + DSİ/idare tarafı varsa idari yargı ayrımı (`/arthurlegal:advocacy-legal-kamu-hukuku-dilekce`)
- [ ] **Yaptırım taraflı / finansör-kreditör ilgili / yüksek tutar** → [Baş Hukuk Müşaviri] + [Genel Müdür] eskalasyon
- [ ] **İş davası** → işyeri (santral/saha ili) yetki + arabuluculuk (7036)

## Çıktı

```markdown
[ÜST BAŞLIK — destination'a göre]

# Özel Hukuk Dilekçesi — [tip] — [dosya/konu]

## ⚠️ İnceleyen notu
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [✓ N madde / ✗]; ArthurLegal MCP (`tr_`) [✓ N emsal / ✗]
- **Süre:** [dilekçe tipi] son tarih GG.AA.YYYY (kalan: N gün) 🔴/🟠/🟡
- **Görev/yetki:** [mahkeme] — HMK m.[X] `[review]`
- **Arabuluculuk dava şartı:** [N/A / tutanak EK-1 var / gerekli]
- **Reviewer bekleyen [review]:** N madde
- **Onay:** dış vekil + [Baş Hukuk Müşaviri] (Baş Hukuk Müşaviri) onayı şart

## Dilekçe taslağı
[doldurulmuş şablon]

## Sonraki adımlar
> 1. **Dış vekil revizesi** — `/arthurlegal:litigation-legal-outside-counsel-brief`
> 2. **İhtiyati tedbir** ekle (HMK m.389) — gerekiyorsa
> 3. **Emsal güçlendir** — ArthurLegal MCP (`tr_`)'den ek karar
> 4. **Yazıhane** — süre/duruşma takvimine işle `/arthurlegal:advocacy-legal-yazihane-asistani`
> 5. **Başka**

**One question I'd ask:** [örn. "Karşı tarafla aktif bir EPC/çerçeve sözleşme ilişkisi sürüyor mu? Sürüyorsa dilekçe tonu/talep yapısı ticari ilişkiyi koruyacak şekilde kalibre edilmeli."]
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
