# ceza-hakim — Skill Referans Kitapçığı

> Dal: Ceza mahkemesi · Rol: **Hâkim** · Usul: CMK 5271 (+ TCK 5237)
> Toplam skill: 5
> Kullanım: `/ceza-hakim:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **tarafsız / yargısal.** Masumiyet karinesi esastır. Çıktılar değerlendirme iskeletidir; **takdir ve hüküm hâkim/heyettedir**. Her çıktı **TASLAK**.

## İçindekiler

- /ceza-hakim:hukum-taslagi — CMK m. 223/230/232 hüküm gerekçesi iskeleti
- /ceza-hakim:iddianame-degerlendirme — CMK m. 170/174 iddianame iade kontrolü
- /ceza-hakim:tutuklama-degerlendirme — CMK m. 100-101 tutuklama/adli kontrol ölçütleri
- /ceza-hakim:hagb-degerlendirme — CMK m. 231 hükmün açıklanmasının geri bırakılması
- /ceza-hakim:uzlastirma-denetimi — CMK m. 253-255 uzlaştırma kapsam & rapor denetimi

---

## /ceza-hakim:hukum-taslagi

---
name: hukum-taslagi
description: >
  CMK m. 223 hüküm türleri ve m. 230/232 gerekçe unsurlarına göre ceza hükmü iskeleti:
  sabit görülen/görülmeyen fiiller, delil değerlendirmesi, vasıflandırma, lehe-aleyhe
  unsurlar, ceza bireyselleştirme ölçütleri. Sonucu ve cezayı DAYATMAZ.
user-invocable: true
---

# Ceza Hükmü — CMK m. 230/232 İskeleti

## Konum hatırlatması

**Masumiyet karinesi (AY m. 38, AİHS m. 6).** Şüpheden sanık yararlanır. Bu skill mahkûmiyet/beraat **sonucunu vermez**; gerekçenin iskeletini kurar, takdir hâkim/heyettedir.

## Çıktı yapısı — m. 230 unsurları

1. **İddia & savunma** — iddia makamının anlatımı + sanık savunması ayrı.
2. **Sabit görülen fiil** — hangi vakıa hangi delille sabit; çelişkilerin giderilmesi.
3. **Delil değerlendirmesi** — her delilin tartışılması (m. 217 — hukuka uygun + duruşmaya getirilmiş delil); hukuka aykırı delil (m. 206/2-a, 217/2) dışlanır.
4. **Vasıflandırma** — fiilin hukuki niteliği (TCK ilgili madde, MCP'den verbatim). **İki yönlü:** suçun oluştuğu ve oluşmadığı yorumları ayrı kurulur.
5. **Lehe kanun & bireyselleştirme** — TCK m. 7 lehe hüküm, m. 61 temel ceza, artırım/indirim, m. 62 takdiri indirim, erteleme/HAGB (CMK m. 231), seçenek yaptırımlar.
6. **Hüküm (iskelet, m. 223):** mahkûmiyet / beraat / ceza verilmesine yer olmadığı / düşme / güvenlik tedbiri — **seçenekli sunulur**, sonuç boş.

## Adımlar

1. Görev/yetki + soruşturma usulü kontrolü (yetkisiz/hukuka aykırı delil var mı).
2. Vakıa–delil eşleştirmesi; çelişki haritası.
3. TCK normunu MCP'den çek, atıf et.
4. Lehe-aleyhe unsurları dengeli sun; ceza miktarını **dayatma**, ölçüt ver.

## İnceleyen notu

- Kullanılan TCK/CMK maddeleri + emsal (atıflı)
- Hukuka aykırı delil riski işaretleri
- ⚠️ "Mahkûmiyet/beraat ve ceza takdiri hâkime/heyete aittir."

---

## /ceza-hakim:iddianame-degerlendirme

---
name: iddianame-degerlendirme
description: >
  CMK m. 170 iddianamenin unsurları ve m. 174 iade sebepleri çerçevesinde iddianamenin
  kabul/iade kontrolü. 15 günlük iade süresini ve eksiklik türlerini yapılandırır.
user-invocable: true
---

# İddianame Değerlendirme — CMK m. 170 / 174

## Amaç

İddianamenin kabule değer olup olmadığını **15 gün** içinde (m. 174/1) yapılandırılmış biçimde kontrol et.

## Kontrol listesi

1. **m. 170 zorunlu unsurlar:** şüpheli kimliği, müdafi, mağdur, suç tarihi/yeri, suçu oluşturan olaylar, deliller, sevk maddeleri, yüklenen suç.
2. **İade sebepleri (m. 174/1):**
   - 🔴 m. 170'e aykırı düzenleme (eksik unsur)
   - 🔴 Soruşturma evresi tamamlanmamış (eksik soruşturma — toplanması gereken delil)
   - 🔴 Önödeme/uzlaştırma/seri-basit yargılama yoluna gidilmemiş (gerekli hâllerde)
3. **İade edilemez (m. 174/2):** suçun hukuki nitelendirmesi sebebiyle iade yapılamaz (vasıflandırma mahkemeye ait).
4. **Süre:** 15 gün içinde iade edilmezse iddianame **kabul edilmiş sayılır** (m. 174/3).

## Çıktı

Kabul / iade önerisi (gerekçeli, seçenekli) + eksiklik listesi (🔴🟠). Karar hâkimindir. TASLAK ibareli.

---

## /ceza-hakim:tutuklama-degerlendirme

---
name: tutuklama-degerlendirme
description: >
  CMK m. 100-101 tutuklama şartları ve m. 109 adli kontrol çerçevesinde koruma tedbiri
  değerlendirme ölçütleri. Ölçülülük ve gerekçe zorunluluğunu vurgular; tedbiri DAYATMAZ.
user-invocable: true
---

# Tutuklama / Adli Kontrol — CMK m. 100-101 / 109

## Konum hatırlatması

Tutuklama **istisnai** ve **ölçülü** olmak zorundadır (AY m. 19, AİHS m. 5). Adli kontrol önceliklidir (m. 101/1). Bu skill ölçüt sunar; tedbir kararı hâkimindir.

## Ölçütler

1. **Kuvvetli suç şüphesi** + somut delil (m. 100/1).
2. **Tutuklama nedeni (m. 100/2):**
   - Kaçma şüphesi / saklanma
   - Delilleri karartma / tanık-mağdur üzerinde baskı
   - Katalog suçlar (m. 100/3) — varsayılan neden (yine de somutlaştır)
3. **Ölçülülük (m. 100/1 son):** işin önemi + beklenen ceza/tedbir ile orantı; adli kontrol yeterli mi (m. 109).
4. **Gerekçe zorunluluğu (m. 101/2):** somut olgularla; matbu gerekçe 🔴 bozma/ihlal sebebi (AYM bireysel başvuru içtihadı — Yargı MCP'den teyit).
5. **Süre & ölçülü süre** — soruşturma/kovuşturma azami süreleri.

## Çıktı

Adli kontrol ↔ tutuklama seçenek analizi + somut gerekçe iskeleti (matbu DEĞİL). Karar hâkimindir. TASLAK ibareli.

---

## /ceza-hakim:hagb-degerlendirme

---
name: hagb-degerlendirme
description: >
  CMK m. 231 hükmün açıklanmasının geri bırakılması: objektif ve sübjektif
  şartlar, sanığın kabulü, zararın giderilmesi, 5 yıllık denetim süresi.
  HAGB'yi DAYATMAZ; şart kontrolü + ölçüt sunar.
user-invocable: true
---

# HAGB — CMK m. 231/5-14

## Konum hatırlatması

HAGB, kurulan hükmün açıklanmasının geri bırakılmasıdır; uygulanıp uygulanmaması ölçütlere bağlıdır, takdir hâkim/heyettedir. **Sanığın kabulü şarttır.**

## Şartlar (m. 231/6)

1. **Ceza sınırı:** hükmolunan hapis **2 yıl veya daha az** ya da adli para cezası.
2. **Sabıka:** sanık daha önce kasıtlı suçtan mahkûm olmamış.
3. **Kanaat:** sanığın yeniden suç işlemeyeceği yönünde kanaat (kişilik + duruşmadaki tutum).
4. **Zarar:** mağdurun/kamunun zararının **aynen iade / öncesi hale getirme / tazmin** yoluyla giderilmesi.
5. **Sanığın kabulü (m. 231/6 son):** kabul etmezse HAGB uygulanmaz.

## Sonuç & denetim

- **Denetim süresi 5 yıl** (m. 231/8); denetimli serbestlik tedbiri eklenebilir.
- Süre içinde kasıtlı suç işlenmez + yükümlülüklere uyulursa → **dava düşer** (m. 231/10).
- İhlal → **hüküm açıklanır** (m. 231/11).
- Kanun yolu: **itiraz** (m. 231/12).

## Çıktı

Şart-şart kontrol tablosu (🔴 eksik) + zarar giderim durumu + kanaat ölçütleri. Karar hâkim/heyettedir. TASLAK ibareli. Detay: `cmk-rehberi.md`.

---

## /ceza-hakim:uzlastirma-denetimi

---
name: uzlastirma-denetimi
description: >
  CMK m. 253-255 uzlaştırma: kapsamdaki suçlar, uzlaştırmanın zorunluluğu,
  uzlaştırmacı raporunun mahkemece denetimi ve sonuçları. Mahkeme uzlaştırmayı
  bizzat yürütmez; kapsamı ve raporu denetler.
user-invocable: true
---

# Uzlaştırma Denetimi — CMK m. 253-255

## Konum

Uzlaştırma, uzlaştırmacı eliyle yürür; mahkeme **kapsamı** ve **raporu** denetler. Kapsamdaki suçta uzlaştırma yoluna gidilmemesi 🔴 bozma/iade sebebidir.

## Kontrol

1. **Kapsam (m. 253/1):** şikâyete bağlı suçlar + kanunda sayılan belirli suçlar. **İstisnalar (m. 253/3):** cinsel dokunulmazlığa karşı suçlar vb. uzlaştırma kapsamı dışı.
2. **Zorunluluk:** kapsamdaysa uzlaştırma zorunlu ön/ara aşamadır; atlanmışsa giderilir.
3. **Rapor denetimi:** uzlaştırmacı raporu usulüne uygun mu; tarafların özgür iradesi, edimin belirliliği.
4. **Sonuç (m. 253/19):** edim derhal ifa → kovuşturmaya yer yok / düşme; ileri tarihli/taksitli edim → denetim, ifa edilirse düşme, edilmezse devam.

## Çıktı

Kapsam kontrolü (uzlaştırmaya tabi mi) + rapor usul denetimi + sonuç önerisi (düşme/devam). Karar hâkimindir. TASLAK ibareli.

---

> 🚧 v1.0.0 — `ceza-hakim` 5 skill. Kalıp: `hukuk-hakim__skills.md`. Detay: `cmk-rehberi.md`, `sulh-ceza-hakimligi-rehberi.md`.
