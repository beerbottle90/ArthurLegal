---
name: advocacy-legal-ceza-dilekce
description: >
  Ceza muhakemesi (CMK 5271) dilekçesi ÜRETİMİ — suç duyurusu/şikayet (m.158),
  katılma/müştekilik (m.237), şüpheli/sanık savunması, tutuklamaya/adli kontrole
  itiraz (m.267-268), KYOK'a itiraz (m.173), esas hakkında savunma, istinaf
  (m.272+, iki hafta), temyiz (m.286+), CMK m.141 koruma tedbiri tazminatı. Örnek senaryolar:
  iş kazası (TCK taksir + 6331), çevre suçu, bilişim, kaçakçılık — müşteki veya
  çalışan müdafii desteği.
user-invocable: true
---

# Ceza Dilekçesi Üretimi (CMK)

> Bu skill ceza muhakemesi **dilekçe/beyan metnini** üretir. **Kurumsal/in-house bağlam:** şirket genelde **müşteki/katılan** (örn. hırsızlık, bilişim, dolandırıcılık, ekipman/altyapı sabotajı) veya **çalışan/yönetici müdafiine destek** (iş kazası TCK m.85/89 taksir, çevre TCK m.181-182). **Sanık müdafiliği baroya kayıtlı avukat işidir** — in-house counsel destek/taslak üretir, fiili müdafilik için dış ceza avukatı + [Baş Hukuk Müşaviri] onayı.

## ⏰ ÖN-KONTROL — SÜRE (her çalıştırmada)

| İşlem | Süre | Dayanak |
|---|---|---|
| **İstinaf** (ilk derece hükme karşı) | **İki hafta** (gerekçeli hükmün tebliğinden) | CMK m.273 |
| **Temyiz** (BAM kararına karşı) | **İki hafta** (gerekçeli hükmün tebliğinden) | CMK m.291 |
| **İtiraz** (tutuklama/adli kontrol vb.) | **İki hafta** (öğrenmeden) | CMK m.268 |
| **KYOK'a itiraz** (Sulh Ceza Hâkimliği) | **İki hafta** (tebliğden) | CMK m.173 |
| **Şikayet** (şikayete bağlı suçlar) | **6 ay** (fail+fiili öğrenme) | TCK m.73 |
| Koruma tedbiri **tazminatı** (m.141) | kesinleşmenin ilgiliye tebliğinden **3 ay** / her hâlde kesinleşme tarihini izleyen **1 yıl** içinde | CMK m.142 |

Kalan < 2 gün → 🔴. Süreler kesin; kaçırma = hak kaybı. 7499 s.K. (RG 12.03.2024) öncesindeki "7 gün / 15 gün" bilgisi yürürlükte değil.

## ADIM 1 — Evre + rol + dilekçe tipi

**Evre:** Soruşturma (Cumhuriyet Başsavcılığı) → İddianame/KYOK → Kovuşturma (mahkeme).

| Rolümüz | Dilekçe/işlem | Madde |
|---|---|---|
| Mağdur/müşteki (şirket suçtan zarar gören) | **Suç duyurusu / şikayet dilekçesi** | CMK m.158 / TCK m.73 |
| Müşteki | **Katılma (müdahale) talebi** | CMK m.237-239 |
| KYOK verildi | **KYOK'a itiraz** (Sulh Ceza Hâkimliği) | CMK m.173 |
| Şüpheli/sanık (çalışan-yönetici) | **Savunma / sorgu beyanı / esas hakkında savunma** | CMK m.147, m.191 |
| Tutuklama/adli kontrol | **Tahliye talebi / itiraz** | CMK m.104, m.267-268 |
| Aleyhe hüküm | **İstinaf dilekçesi** | CMK m.273 |
| Aleyhe BAM kararı | **Temyiz dilekçesi** | CMK m.291 |
| Haksız koruma tedbiri | **m.141 tazminat istemi** (Ağır Ceza; m.141/1-e, f, l hâllerinde 6384 s.K. Tazminat Komisyonu — 7499 s.K.) | CMK m.141-142 |

## ADIM 2 — Görevli/yetkili mahkeme + uzlaştırma süzgeci

- **Görev:** Asliye Ceza (genel) / **Ağır Ceza** (TCK'da üst sınırı 10 yıl+ suçlar, örn. nitelikli yağma, kasten öldürme) / Sulh Ceza Hâkimliği (soruşturma koruma tedbirleri + KYOK itirazı).
- **Yetki:** suçun işlendiği yer (CMK m.12) — santral/saha ili.
- **Uzlaştırma (CMK m.253):** uzlaştırma kapsamındaki suçlarda (örn. taksirle yaralama, mala zarar, güveni kötüye kullanma) **soruşturma/kovuşturma şartı**; kapsamı kontrol et. Şirket müşteki ise uzlaşma kabul/ret stratejisi.

## ADIM 3 — Maddi olay + suç vasfı + delil

- **Olay:** somut, tarih/yer/kişi; iş kazasında olay yeri/SGK/iş müfettişi raporu, çevre olayında ölçüm/tutanak.
- **Suç vasfı (müşteki isek):** TCK'daki karşılığı (örn. m.142 nitelikli hırsızlık, m.157-158 dolandırıcılık, m.243-244 bilişim, m.151-152 mala zarar). Savunma isek: kast/taksir ayrımı, kusurun bulunmadığı/iştirak/illiyet.
- **Delil:** tutanak, kamera, bilirkişi (CMK m.62-73), tanık, SGK/iş müfettişi/ÇŞB raporu, dijital delil. **CMK m.153** — müdafiin dosyayı inceleme yetkisi (müdafi sıfatı gerekir).

## ADIM 4 — Emsal (ArthurLegal MCP (`tr_`))

```
tr_ictihat_ara(query="<suç + somut konu>",
  chamber="<ilgili Yargıtay CD, örn. 12. CD (taksirle ölüm), 15. CD, 11. CD>",
  date_from="2021-01-01")
```
Yalnızca çekileni işle: `[ArthurLegal TR — Yargıtay 12.CD — Esas/Karar — GG.AA.YYYY]`.

## ADIM 5 — Dilekçe taslakları

**(a) Suç duyurusu / şikayet (müşteki — [Müvekkil / Şirket]):**
```markdown
[YER] CUMHURİYET BAŞSAVCILIĞI'NA

ŞİKAYETÇİ/MÜŞTEKİ : [Müvekkil / Şirket] — [VKN], [adres]
VEKİLİ            : Av. [ad], [baro/sicil], [KEP]
ŞÜPHELİ           : [varsa kimlik / "tespit edilecek"]
SUÇ               : [örn. hırsızlık TCK m.141-142 / bilişim sistemine girme m.243 /
                    mala zarar m.151] [şikayete bağlıysa: süresi içinde]
SUÇ TARİHİ/YERİ   : GG.AA.YYYY — [santral/saha]

OLAYLAR           : [kronolojik somut anlatım + delil atfı]
DELİLLER          : kamera kaydı (EK), tutanak, bilirkişi, tanık, [SGK/ÇŞB raporu]
HUKUKİ NEDENLER   : TCK m.[...], CMK `[ArthurLegal TR — GG.AA.YYYY]`
TALEP             : Şüpheli/şüpheliler hakkında soruşturma başlatılmasına, gerekli
                    koruma/delil tedbirlerine, kamu davası açılmasına karar verilmesini
                    ve şikayetçi/müşteki sıfatımızın kabulünü saygıyla talep ederiz.
                                                  GG.AA.YYYY — Vekil Av. [ad]
EKLER: vekaletname, deliller
```

**(b) Esas hakkında savunma / istinaf (savunma — çalışan-yönetici müdafiine destek):** sanığın kimliği, isnat, **lehe deliller + kast/taksir-kusur değerlendirmesi + illiyet bağı + iştirak** + emsal beraat/HAGB; istinafta hükmün özeti + bozma/kaldırma sebepleri (eksik inceleme, hukuka aykırı delil, vasıf hatası, ceza tayini).

## ADIM 6 — Sektörel/örnek senaryolar kontrolleri

- [ ] **İş kazası (santral/saha)** → TCK m.85/89 taksir + 6331; paralel **iş mahkemesi tazminat** + **idari (SGK/iş müfettişi)** dosyaları → `/litigation-legal` ile üçlü-paralel koordinasyon. İSG ilk müdahale: `/arthurlegal:litigation-legal-isg-incident-response`.
- [ ] **Çevre olayı** → TCK m.181-182 + 2872 idari ceza paralel.
- [ ] **Sanık müdafiliği** → baroya kayıtlı (dış) avukat şart; in-house destek üretir.
- [ ] **Üst yönetim/YK adı geçiyor** → [Baş Hukuk Müşaviri] + [Genel Müdür]; basın riski → iletişim koordinasyon.
- [ ] **CMK m.153 dosya erişimi** → müdafi sıfatı yoksa tam erişim yok; hatırlat.

## Çıktı

```markdown
[ÜST BAŞLIK]
# Ceza Dilekçesi — [tip] — [dosya/soruşturma no]

## ⚠️ İnceleyen notu
- **Evre/rol:** [soruşturma/kovuşturma] — [müşteki/savunma]
- **Süre:** [işlem] son tarih GG.AA.YYYY (kalan N gün) 🔴/🟠/🟡
- **Görev/uzlaştırma:** [mahkeme] · uzlaştırma [kapsamda/değil]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [✓/✗]; ArthurLegal MCP (`tr_`) (CD) [✓ N / ✗]
- **Onay:** dış ceza avukatı + [Baş Hukuk Müşaviri] şart (sanık müdafiliğinde zorunlu)

## Dilekçe taslağı
[doldurulmuş]

## Sonraki adımlar
> 1. **Dış ceza avukatı brief** — `/arthurlegal:litigation-legal-outside-counsel-brief`
> 2. **İSG paralel dosyalar** — `/arthurlegal:litigation-legal-isg-incident-response` (iş kazası)
> 3. **Tazminat ayağı** — `/arthurlegal:advocacy-legal-ozel-hukuk-dilekce` (iş mahkemesi/haksız fiil)
> 4. **Süre/duruşma takvimi** — `/arthurlegal:advocacy-legal-yazihane-asistani`
> 5. **Başka**

**One question I'd ask:** [örn. "Bu iş kazası dosyasında SGK/iş müfettişi raporu kusur dağılımını nasıl belirledi? Ceza, tazminat ve idari dosyalardaki kusur tezimiz tutarlı olmalı."]
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
