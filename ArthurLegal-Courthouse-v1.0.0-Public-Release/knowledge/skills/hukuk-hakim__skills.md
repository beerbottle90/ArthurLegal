# hukuk-hakim — Skill Referans Kitapçığı

> Dal: Hukuk mahkemesi · Rol: **Hâkim** · Usul: HMK 6100
> Toplam skill: 4
> Kullanım: `/hukuk-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Çıktılar gerekçe ve usulü yapılandırır; karar hâkimindir. Her çıktı **TASLAK — hâkim/heyet onayı şart**.

## İçindekiler

- /hukuk-hakim:gerekceli-karar — HMK m. 297 yapısında gerekçeli karar iskeleti
- /hukuk-hakim:on-inceleme — HMK m. 137-142 ön inceleme tutanağı & kontrol
- /hukuk-hakim:delil-degerlendirme — HMK m. 187 vd. ispat yükü & delil takdiri metodu
- /hukuk-hakim:ihtiyati-tedbir — HMK m. 389-399 geçici hukuki koruma değerlendirmesi

---

## /hukuk-hakim:gerekceli-karar

---
name: gerekceli-karar
description: >
  Bir hukuk uyuşmazlığında HMK m. 297'ye uygun gerekçeli karar iskeleti üretir:
  taraf iddiaları, uyuşmazlık konusu, delil değerlendirmesi, uygulanacak norm ve
  hukuki gerekçe ayrı ayrı yapılandırılır. Sonucu DAYATMAZ; gerekçenin iskeletini kurar.
user-invocable: true
---

# Gerekçeli Karar — HMK m. 297 İskeleti

## Konum hatırlatması

Sen tarafsızsın. Bu skill **kararı yazmaz**, kararın **gerekçe iskeletini** kurar. Sonuç (kabul/ret/kısmen kabul) **hâkim/heyet takdiridir**. İki tarafı dengeli sun.

## Girdi

Kullanıcı şunları sağlamalı (eksikse iste, varsayma):
- Dava türü (eda / tespit / inşai) ve talep
- Tarafların temel iddiaları (davacı + davalı)
- Toplanan deliller (belge, tanık, bilirkişi, keşif)
- Varsa bilirkişi raporu sonucu ve itirazlar

## Çıktı yapısı — HMK m. 297 unsurları

Üst başlık: `MAHKEME DAHİLİ ÇALIŞMA NOTU — TASLAK (hâkim/heyet onayı şart)`

1. **Başlık & taraflar** — mahkeme, esas no, taraflar ve vekilleri (kalıp; `[DOLDUR]`).
2. **Dava ve talep** — davacının talebi, hukuki sebep (1-2 cümle özet).
3. **Savunma** — davalının savunması ve karşı talepleri.
4. **Uyuşmazlık konusu** — tarafların üzerinde anlaştığı ve çekiştiği noktalar ayrı ayrı.
5. **Deliller ve değerlendirilmesi** — her delil için: ne ispatlıyor, çekişme var mı, ispat yükü kimde (HMK m. 187). Bilirkişi raporu varsa: rapor sonucu + itirazların karşılanması.
6. **Gerekçe** — uygulanacak norm (MCP'den `[Mevzuat MCP — GG.AA.YYYY]`) + varsa emsal içtihat (`[Yargı MCP — kurum — Esas/Karar — GG.AA.YYYY]`) + somut olaya uygulama. **İki yönlü:** kabul gerekçesi ile ret gerekçesi ayrı ayrı kurulur; hangisinin daha güçlü olduğunu hâkim takdir eder.
7. **Hüküm (iskelet)** — HMK m. 297/2 unsurları: talep kalemleri tek tek, vekâlet ücreti, yargılama gideri, kanun yolu/süre. **Sonuç boş bırakılır veya seçenekli sunulur.**

## Adımlar

1. **Usulü önce kontrol et.** Görev/yetki, dava şartları (HMK m. 114-115), husumet, derdestlik/kesin hüküm. Engel varsa 🔴/🟠 flag'le ve esasa geçme.
2. **Uyuşmazlığı daralt.** Çekişmesiz vakıaları ayır (ispat gerektirmez, HMK m. 187/2).
3. **İspat yükünü dağıt.** Her çekişmeli vakıa için kim ispatla yükümlü (m. 190) ve ispat edildi mi.
4. **Normu MCP'den çek.** İlgili TBK/TMK/TTK/HMK maddelerini verbatim al, atıf et. Çekmeden madde numarası yazma.
5. **Emsal varsa** Yargı MCP'den çek; yoksa "emsal teyidi gerekir" notu düş.
6. **İki yönlü gerekçe** kur, sonucu dayatma.

## İnceleyen notu (çıktının sonunda)

- Kullanılan normlar ve içtihat (atıflı)
- Teyit gereken noktalar (`[UYAP/Lexpera — manuel doğrulayın]`)
- ⚠️ "Sonuç ve takdir hâkime/heyete aittir."

## Sıradaki adımlar (öner)

- `/hukuk-hakim:delil-degerlendirme` — ispat yükü derinleştirme
- Emsal içtihat taraması (Yargı MCP)
- Bilirkişi raporuna itirazların ayrı değerlendirmesi (`bilirkisilik-rehberi.md`)

---

## /hukuk-hakim:on-inceleme

---
name: on-inceleme
description: >
  HMK m. 137-142 ön inceleme aşaması için kontrol listesi ve tutanak iskeleti:
  dava şartları, ilk itirazlar, sulh/arabuluculuk teşviki, uyuşmazlık noktalarının
  tespiti, tahkikata hazırlık.
user-invocable: true
---

# Ön İnceleme — HMK m. 137-142

## Amaç

Ön inceleme duruşması öncesi/sırasında hâkimin kontrol etmesi gerekenleri **eksiksiz** yapılandır. Bu aşama atlanırsa tahkikat sakatlanır.

## Kontrol listesi

1. **Dava şartları (m. 114) — re'sen:** görev, yetki (kesin mi), hukuki yarar, taraf/dava ehliyeti, derdestlik, kesin hüküm. 🔴 eksikse dava usulden ret.
2. **İlk itirazlar (m. 116):** yetki (kesin değilse), tahkim itirazı, iş bölümü — **cevap dilekçesinde** ileri sürülmüş mü; süresinde değilse dinlenmez.
3. **TTK m. 5/A dava şartı arabuluculuk:** ticari/alacak-tazminat davasıysa arabuluculuk şartı sağlanmış mı. 🔴 değilse dava şartı yokluğundan ret.
4. **Sulh ve arabuluculuk teşviki (m. 140/2):** tarafları teşvik et, tutanağa geçir.
5. **Uyuşmazlık noktalarının tespiti (m. 140/3):** çekişmeli/çekişmesiz vakıalar ayrılır — tahkikatın sınırını çizer.
6. **Delil gösterme & sunma süresi (m. 140/5, 145):** taraflara kesin süre; sonradan delil sınırlı.

## Çıktı

Ön inceleme tutanağı iskeleti (`[DOLDUR]` alanlı) + 🔴🟠🟡 işaretli eksiklik listesi. Üst başlık TASLAK ibareli.

---

## /hukuk-hakim:delil-degerlendirme

---
name: delil-degerlendirme
description: >
  HMK m. 187 vd. çerçevesinde ispat yükü dağılımı ve delil takdiri metodu:
  hangi vakıa ispat gerektirir, yük kimde, deliller nasıl tartılır, bilirkişi
  raporu nasıl değerlendirilir. Takdiri DAYATMAZ; ölçüt sunar.
user-invocable: true
---

# Delil Değerlendirme — İspat Yükü & Takdir Metodu

## Amaç

Delil takdirini **yöntemli** hale getir. Sonucu söyleme; hâkimin vicdani kanaatine (HMK m. 198 serbest delil takdiri, senette m. 200 sınır) **ölçüt** sun.

## Yöntem

1. **Vakıaları ayır:** çekişmeli mi, çekişmesiz mi (m. 187/2 — çekişmesiz ispat gerektirmez).
2. **İspat yükü (m. 190):** kural — iddia eden ispatla yükümlü. Karine/aksi ispat hâlleri ayrıca işaretle.
3. **Delil türü sınırları:**
   - Senetle ispat zorunluluğu ve istisnaları (m. 200-201).
   - Tanıkla ispat sınırı (senede karşı tanık yasağı, m. 201).
   - Kesin deliller (senet, yemin, kesin hüküm) ↔ takdiri deliller (tanık, bilirkişi, keşif, özel uzman görüşü m. 293).
4. **Bilirkişi raporu (m. 266 vd.):** rapor hâkimi bağlamaz; teknik/özel bilgi alanı mı, denetime elverişli mi, itirazlar karşılandı mı. Çelişki varsa ek rapor/yeni bilirkişi. Detay: `bilirkisilik-rehberi.md`.
5. **Belgenin ibrazı (m. 219-220):** karşı tarafın elindeki belge — ibraz etmezse aleyhe takdir karinesi.

## Çıktı

Vakıa × delil × ispat-yükü tablosu + her çekişmeli vakıa için "ispat edildi / edilmedi / eksik" ölçütlü değerlendirme. **Sonuç hâkim takdirine bırakılır.**

---

## /hukuk-hakim:ihtiyati-tedbir

---
name: ihtiyati-tedbir
description: >
  HMK m. 389-399 geçici hukuki koruma: ihtiyati tedbir talebinin şartları
  (yaklaşık ispat + tedbir sebebi), teminat, tedbir türü ve ölçülülük
  değerlendirmesi. Tedbiri DAYATMAZ; ölçüt sunar.
user-invocable: true
---

# İhtiyati Tedbir — HMK m. 389-399

## Konum hatırlatması

Geçici koruma istisnaidir ve **gerekçeli** olmalıdır. Uyuşmazlık konusu hakkında esası çözer nitelikte tedbir kural olarak verilemez. Karar hâkimindir.

## Şartlar

1. **Tedbir sebebi (m. 389):** mevcut durumda meydana gelebilecek değişiklik nedeniyle hakkın elde edilmesinin önemli ölçüde zorlaşması / imkânsızlaşması veya gecikmede sakınca / ciddi zarar.
2. **Yaklaşık ispat (m. 390/3):** talep eden, davanın esası yönünden haklılığını **yaklaşık** ispatla yükümlü (kesin ispat aranmaz).
3. **Teminat (m. 392):** kural olarak teminat karşılığı; istisnaları (yaklaşık ispatın kuvveti / kamu).

## Adımlar

1. Talebin türü ve dayanağı (m. 389) — neye yönelik tedbir.
2. Yaklaşık ispat değerlendirmesi (m. 390/3).
3. **Ölçülülük:** talep edilen tedbir korunacak hakla orantılı mı; esası çözer nitelikte mi (aşırı tedbir riski).
4. Teminat (m. 392) + tedbir kararının içeriği (m. 391).
5. **Karşı tarafın dinlenmesi:** kural; gecikmesinde sakınca varsa dinlenmeden (sonra itiraz — m. 394).
6. **Tamamlayıcı işlemler:** uygulama + esas dava süreleri (m. 393, 397).

## Çıktı

Şart-şart değerlendirme + teminat + tedbir türü önerisi (seçenekli) + somut gerekçe iskeleti. İtiraz yolu (m. 394) ve haksız tedbir tazminatı (m. 399) notu. Karar hâkimindir. TASLAK ibareli.

---

> 🚧 **v1.0.0.** `hukuk-hakim` için 4 skill (gerekçe yazımı, ön inceleme, delil değerlendirme, ihtiyati tedbir) ve diğer plugin'lerin yapı kalıbıdır. Genişletme sırası → [CHANGELOG.md](../../CHANGELOG.md).
