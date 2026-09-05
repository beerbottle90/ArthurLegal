# Legal Research Practice Profile (Kaynak katmanı — Büro tarafı)

*Bu dosya `/legal-research:kaynak-secimi` ile birlikte okunur. `[DOLDUR]`
alanları `/firm-operations:cold-start-interview` ile doldurulabilir.*

> **Bu bir pratik alan değil, kaynak katmanıdır.** Tek başına müvekkile giden
> bir iş ürünü üretmez; diğer eklentilerin (advocacy, litigation, commercial,
> corporate, energy-finance, tax, expert-opinion, criminal-defense) **dayanağını
> besler**. Bir dilekçenin, mütalaanın veya görüşün altındaki kaynak bu katmandan
> gelir.

---

## Kim olduğumuz

`firm-profile.md` oku. Bu eklentiye özel:

**Kurulu MCP sunucuları:** `[DOLDUR — hangileri connector olarak eklendi?]`
**ArthurLegal MCP:** `https://arthurlegal-mcp.fly.dev/mcp` — on yargı çevresi
tek connector'da (`az_` `at_` `de_` `nl_` `pl_` `es_` `fi_` `ie_` `scholar_`
`contracts_`). Kurulu değilse `[DOLDUR — "kurulu değil"]` yaz; o hâlde AZ
mevzuatı WebFetch yoluna düşer ve **yürürlük statüsü doğrulanmaz**.
**OpenAlex API key (opsiyonel, ücretsiz):** `[DOLDUR — yoksa bütçe ~100 arama/gün]`

**Araştırma sorumlusu:** `[DOLDUR — örn. kıdemli avukat / stajyer koordinatörü]`
**Araştırma notu saklama yeri:** `[DOLDUR — örn. dosya klasörü / DMS]`

> Üç MCP de **isteğe bağlıdır.** Kurulu değilse paket çalışmaya devam eder:
> AZ mevzuatı WebFetch yoluna düşer (**statü doğrulanmaz**), doktrin ve sözleşme
> emsali kapsam dışı kalır. Bu durumda çıktıda **kapsam notu** zorunludur.

---

## Kaynak hiyerarşisi — bu büronun bağlayıcı kuralı

```
BİRİNCİL (mevzuat, içtihat)  →  EMSAL (imzalı sözleşme)  →  DOKTRİN (akademik)
```

| Kademe | Ne yapar | Ne YAPAMAZ |
|---|---|---|
| **Birincil** | Bir sonucun dayanağı olur | — |
| **Emsal** | Bir şartın piyasa/agresif/muhafazakâr olduğunu gösterir | Hukukî zorunluluk kurmaz |
| **Doktrin** | Argümanı güçlendirir, tartışmayı gösterir | Dayanak olmaz, kararı bağlamaz |

**Çelişki hâlinde birincil üstündür** — çelişkiyi **raporla**, ikincil kaynak
lehine sessizce çözme. Bir dilekçede doktrin **yalnız birincil kaynakla birlikte**
kullanılır; tek başına gerekçe olmaz.

---

## Üç kaynak — kapsam ve rol

| MCP | Rol | Kapsam | Kritik disiplin |
|---|---|---|---|
| **e-qanun** | **BİRİNCİL** | AZ mevzuatı (resmî `api.e-qanun.az`) | **`az_get_act` ile yürürlük statüsü doğrulaması zorunlu** |
| **LexScholar** | **İKİNCİL** | 10 indeks; **DergiPark 19 TR hukuk dergisi** dâhil | Hakemlilik **üç durumlu**; sorgu dili tuzağı |
| **ResourceContracts** | **EMSAL** | 5.125 imzalı PSA/JOA, 107 ülke | `page` boş = tüm anotasyonlar; CC BY-SA 4.0 atıf |

**Rehberler:** `references/eqanun-mcp-rehberi.md` ·
`references/lex-scholar-rehberi.md` · `references/resourcecontracts-rehberi.md` ·
`references/karsilastirmali-hukuk-rehberi.md`

---

## Türk doktrini — DergiPark üzerinden hangi dergi

Router konuya göre seçer; hangi derginin geldiğini **kapsam notunda belirt**:

| Konu | Beklenen dergi |
|---|---|
| Ceza / kriminoloji | Ceza Hukuku ve Kriminoloji Dergisi |
| İdari / imar / ihale | İdare Hukuku ve İlimleri Dergisi |
| Deniz / sigorta / petrol / maden | İstanbul Hukuk Mecmuası |
| Ticaret / şirket / tahkim / enerji | Marmara Hukuk Fakültesi Dergisi |
| Anayasa / vergi / milletlerarası | Ankara Hukuk Fakültesi Dergisi |
| Genel | 15 hukuk fakültesi dergisi + Adalet Dergisi + İslam Hukuku Araştırmaları |

**Türkçe hukukî terimle ara** — indeks makalenin kendi kelimesini eşler:
`mücbir sebep`, `aşırı ifa güçlüğü`, `uyarlama`, `muvazaa`, `zamanaşımı`,
`ihtiyati tedbir`. Boş dönen sonuç "bu terimle bulunamadı" demektir,
"literatür yok" demek değildir.

---

## 🔒 Meslek sırrı — Av. K. m. 36 bu araçlara da uygulanır

Üç MCP de **kamuya açık** arama aracıdır. Bir arama sorgusu, karşı tarafa veya
üçüncü kişiye vekâlet ilişkisini ele verebilecek kadar belirginse **yapma**.

**Gönderilmez:** müvekkil adı · dosya numarası · dosya özeti · gizli sözleşme
taslağı veya kloz metni · müzakere pozisyonu · ücret/eşik bilgisi · karşı taraf
adının somut bir dosyayla birlikte geçtiği ifade · kişisel veri (KVKK).

**Gönderilir:** soyut hukukî kavram — `stabilization clause cost recovery cap`,
`mücbir sebep uyarlama`, `investor-state arbitration jurisdiction`.

Detay: `references/mesleki-sir-rehberi.md`, `references/conflict-check-rehberi.md`.

---

## ⏱️ 100 saniye — dosya planlamasına etkisi

Her araç çağrısı 100 saniyede iptal edilir ve **hiçbir şey döndürmez.**

- Bir dilekçe hazırlığında araştırmayı **tek büyük çağrıya** yıkma; mesele
  başına ayrı, dar çağrılar kur.
- İptal olan çağrıyı **aynen tekrarlama** — böl.
- **Kapsam daralmasını dosya notuna yaz.** Müvekkile veya mahkemeye giden bir
  çıktıda kısmi araştırmayı tam gibi sunmak meslekî sorumluluk doğurur.
- **Özel araç > genel web arama** — özel araçlar hukuk indekslerini doğrudan
  sorgular ve saniyeler içinde döner.

---

## Araştırma notu — asgari içerik

Bir dosyaya konan araştırma notu şunları taşımalı:

1. **Soru** — hangi meselenin hangi ayağı araştırıldı
2. **Sorgulanan kaynaklar** — hangi araç, hangi indeks, **hangi terimle**
3. **Kapsanmayanlar** — atlanan indeks, boş dönen yargı çevresi, iptal olan çağrı
4. **Bulgular** — kademe işaretli (birincil / emsal / **ikincil**)
5. **Atıflar** — araç çıktısındaki hazır `citation` / `source_url` birebir
6. **Tarih** — kaynak güncelliği (eski makale bir değişikliği öncelemiş olabilir)
7. **İnceleyen notu** — Yönetici Ortak / dosya sorumlusu avukat incelemesi için taslak

---

## Yaygın hatalar — bu büroda kabul edilmez

| Hata | Neden yanlış |
|---|---|
| `Ləğv olunmuş` bir AZ aktını güncel gibi göstermek | `az_search_acts` statüyü söylemez; **`az_get_act` zorunlu** |
| ABD law review'unu "hakemli" saymak | Öğrenci editörlüdür; `peer_reviewed=false` |
| `null` hakemliliği "hakemli" diye yükseltmek | Bilinmiyor demektir — öyle yaz |
| Emsal klozu "hukuk böyle" diye sunmak | Bir tarafın müzakere sonucudur |
| Boş dönen aramayı "literatür yok" diye raporlamak | "Bu terimle/dilde bulunamadı" demektir |
| Çekilmemiş kaynağa atıf etiketi koymak | `[model bilgisi — doğrulayın]` kullan |
| Doktrini dilekçede tek gerekçe yapmak | Birincil kaynakla birlikte kullanılır |
| Müvekkil adını arama sorgusuna koymak | Av. K. m. 36 ihlali riski |

---

## Eskalasyon

- Araştırma bir **birincil kaynağa hiç ulaşamadıysa** ve sonuç dosyayı taşıyacaksa
  → dosya sorumlusu avukata bildir, dış kaynak (yabancı hukuk uzmanı, Lexpera/
  UYAP manuel doğrulama) öner.
- **Yaptırım eşleşmesi** görülürse → dur, `firm-operations:conflict-check` ve
  `references/opensanctions-rehberi.md` akışına geç.
- Bir MCP sürekli erişilemiyorsa → `[DOLDUR — teknik sorumlu]`'ya bildir; o arada
  yedek yolu kullan ve kapsam notu ekle.

---

*ArthurLegal Law Firm Assistant v1.4.0 — kaynak katmanı profili.
Companion skill: `skills/legal-research__skills.md`.*
