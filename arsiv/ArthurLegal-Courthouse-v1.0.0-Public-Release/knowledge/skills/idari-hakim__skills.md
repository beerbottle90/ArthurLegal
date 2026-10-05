# idari-hakim — Skill Referans Kitapçığı

> Dal: İdari yargı (idare mahkemesi) · Rol: **Hâkim** · Usul: İYUK 2577
> Toplam skill: 4
> Kullanım: `/idari-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Re'sen araştırma ilkesi (İYUK m. 20) geçerlidir. Çıktılar değerlendirme iskeletidir; **takdir hâkim/heyettedir**. Her çıktı **TASLAK**.

## İçindekiler

- /idari-hakim:idari-karar — iptal / tam yargı davası karar iskeleti (İYUK)
- /idari-hakim:yurutmenin-durdurulmasi — İYUK m. 27 iki şart değerlendirmesi
- /idari-hakim:ehliyet-husumet — İYUK m. 14-15 ilk inceleme (ehliyet, husumet, süre)
- /idari-hakim:ivedi-yargilama — İYUK m. 20/A ivedi + m. 20/B merkezî sınav özel rejimleri

---

## /idari-hakim:idari-karar

---
name: idari-karar
description: >
  İptal (İYUK m. 2/1-a) veya tam yargı (m. 2/1-b) davasında karar iskeleti üretir:
  idari işlemin beş unsuru üzerinden hukuka uygunluk denetimi, re'sen araştırma,
  iptal/ret veya tazminat değerlendirmesi. Sonucu DAYATMAZ.
user-invocable: true
---

# İdari Karar — İptal / Tam Yargı İskeleti

## Konum hatırlatması

İdari yargı **hukuka uygunluk** denetimi yapar; yerindelik denetimi yapamaz (İYUK m. 2/2). Re'sen araştırma ilkesi geçerli (m. 20). Sonuç hâkim/heyet takdiridir.

## Çıktı yapısı

1. **Dava konusu işlem** — hangi idari işlem/eylem, hangi makam.
2. **İlk inceleme sonucu** — (aşağıdaki `ehliyet-husumet` skill'i) süre/ehliyet/husumet temiz mi.
3. **İşlemin beş unsuru üzerinden denetim:**
   - **Yetki** — makam yetkili mi
   - **Şekil** — usul/şekil kuralları (gerekçe, savunma alma)
   - **Sebep** — maddi/hukuki sebep var ve doğru mu
   - **Konu** — işlemin sonucu hukuka uygun mu
   - **Maksat** — kamu yararı / yetki saptırması var mı
4. **Re'sen araştırma (m. 20):** eksik bilgi/belge ara kararla istenir.
5. **Tam yargıda** ayrıca: idarenin hizmet kusuru/kusursuz sorumluluğu + illiyet + zarar + tazminat hesabı (ölçütlü, miktar dayatılmadan).
6. **Hüküm (iskelet):** iptal / ret / kısmen iptal / tazminat — **seçenekli**, sonuç boş.

## Adımlar

1. İlgili mevzuatı (ilgili kanun + yönetmelik) MCP'den çek, atıf et.
2. Danıştay emsali varsa Yargı MCP'den çek (`[Yargı MCP — Danıştay — Esas/Karar — GG.AA.YYYY]`).
3. Beş unsuru tek tek denetle; iptal ve ret gerekçesini **ayrı** kur.

## İnceleyen notu

- Kullanılan mevzuat + Danıştay emsali (atıflı)
- Re'sen araştırılması gereken eksikler
- ⚠️ "Sonuç ve takdir hâkime/heyete aittir; yerindelik denetimi yapılmaz."

---

## /idari-hakim:yurutmenin-durdurulmasi

---
name: yurutmenin-durdurulmasi
description: >
  İYUK m. 27 çerçevesinde yürütmenin durdurulması talebini iki şart (açıkça hukuka
  aykırılık + telafisi güç/imkânsız zarar) yönünden değerlendirir; teminat ve gerekçe
  zorunluluğunu vurgular.
user-invocable: true
---

# Yürütmenin Durdurulması — İYUK m. 27

## Konum hatırlatması

YD **istisnai** tedbirdir ve **gerekçeli** olmak zorundadır (m. 27/2). İki şart **birlikte** aranır.

## İki şart

1. **Açıkça hukuka aykırılık** — işlemin uygulanmasının açık hukuka aykırılığı.
2. **Telafisi güç veya imkânsız zarar** — uygulanması hâlinde doğacak zarar.

> Her ikisi birlikte gerçekleşmezse YD verilemez (m. 27/2). Gerekçe somut olmalı.

## Ek noktalar

- **Teminat (m. 27/6):** kural olarak teminat karşılığı; istisnaları.
- **Vergi davalarında özel rejim (m. 27/4):** tarh/ceza işlemlerinde dava açılması tahsilatı kendiliğinden durdurur (ihtirazi kayıt/teminat ayrımı) — `vergi-yargisi-rehberi.md`.
- **İvedi yargılama (m. 20/A)** ve **merkezî sınav (m. 20/B)** özel süre rejimleri.
- **İtiraz:** YD kararına itiraz mercii (BİM/Danıştay).

## Çıktı

İki-şart değerlendirme tablosu + somut gerekçe iskeleti + teminat notu. Karar hâkim/heyettedir. TASLAK ibareli.

---

## /idari-hakim:ehliyet-husumet

---
name: ehliyet-husumet
description: >
  İYUK m. 14-15 ilk inceleme: görev-yetki, ehliyet (menfaat ihlali), husumet (doğru
  idare), süre (m. 7 — 60/30 gün), idari merci tecavüzü gibi sebepleri kontrol eder.
user-invocable: true
---

# İlk İnceleme — İYUK m. 14-15

## Amaç

Dava dilekçesini esastan önce m. 14 yönlerinden incele; m. 15 ret/işlem sonuçlarını uygula.

## Kontrol (m. 14/3 sıralı)

1. **Görev ve yetki** — idari yargı + yetkili mahkeme.
2. **İdari merci tecavüzü** — önce başvurulması gereken makam (varsa m. 11) → m. 15/1-e dilekçe ilgili mercie tevdi.
3. **Ehliyet** — menfaat ihlali / kişisel-meşru-güncel menfaat (iptal); hak ihlali (tam yargı).
4. **İdari davaya konu kesin ve yürütülebilir işlem** mi.
5. **Süre (m. 7):** **idare 60 gün, vergi 30 gün**; ÇED ivedi 30 gün (m. 20/A). Süre aşımı 🔴 m. 15/1-b ret.
6. **Husumet** — doğru idareye yöneltilmiş mi; değilse m. 15/1-c re'sen husumet düzeltme.
7. **Dilekçe usulü (m. 3-5)** — şekil, aynı dilekçeyle dava açma şartları.

## Çıktı

m. 14 kontrol tablosu + m. 15 sonuç önerisi (ret / tevdi / düzeltme), 🔴🟠🟡 işaretli. Karar hâkimindir. TASLAK ibareli. Detay: `iyuk-rehberi.md`, `idari-yargi-yapisi-rehberi.md`.

---

## /idari-hakim:ivedi-yargilama

---
name: ivedi-yargilama
description: >
  İYUK m. 20/A ivedi yargılama ve m. 20/B merkezî sınav özel usulleri:
  kısalmış süreler, sınırlı/değişik kanun yolu, YD özellikleri. Hangi davaların
  bu rejime tabi olduğunu ve usul sapmalarını yapılandırır.
user-invocable: true
---

# İvedi Yargılama — İYUK m. 20/A ve 20/B

## m. 20/A — ivedi yargılama usulü

Kanunda sayılan belirli dava türlerinde (örn. ÇED, acele kamulaştırma, özelleştirme, doğal kaynak/maden gibi) uygulanır.

**Genel rejimden sapmalar:**
- **Dava açma süresi 30 gün** (genel 60 gün yerine).
- Savunma/ara işlem süreleri kısa.
- **İstinaf yok** — ilk derece kararına karşı doğrudan **Danıştay'da temyiz** (kısa süre).
- **YD kararına itiraz edilemez** (m. 20/A özelliği).

## m. 20/B — merkezî sınav usulü

Merkezî sınav (ÖSYM vb.) iş ve işlemlerine ilişkin davalarda toplu/kısa süreli özel usul.

## Hâkim/kalem kontrolü

1. Dava bu özel rejimlerden birine giriyor mu? (Kanuni sayım — Mevzuat MCP teyidi.)
2. Süreler (dava açma, savunma, temyiz) genel rejimden farklı uygulandı mı?
3. Kanun yolu doğru mu (istinaf yok → doğrudan Danıştay)?
4. YD itiraz yasağı gözetildi mi?

## Çıktı

Rejim tespiti + süre/kanun-yolu sapma tablosu + usul kontrol listesi. TASLAK ibareli. Detay: `iyuk-rehberi.md`, `ced-rehberi.md`, `yurutmenin-durdurulmasi-rehberi.md`.

---

> 🚧 v1.0.0 — `idari-hakim` 4 skill. Kalıp: `hukuk-hakim__skills.md`.
