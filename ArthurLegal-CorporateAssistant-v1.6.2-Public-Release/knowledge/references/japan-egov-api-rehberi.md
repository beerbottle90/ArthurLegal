# Japonya e-Gov 法令API v2 — Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK** — Japonya Dijital Ajansı'nın (デジタル庁) 法令API'si
> düz REST/JSON sunar; bu rehber Claude'un `WebFetch` aracıyla kullanım
> prosedürünü tanımlar. UK Legislation rehberiyle aynı kalıp.
>
> **Durum:** ✅ Açık erişim — **API anahtarı gerekmez**, kayıt gerekmez
> (13.08.2026'da canlı teyit edildi; auth modeli entegrasyon öncesi yeniden
> doğrulanmalı). Birincil yargı çevresi Türkiye'dir; bu kaynak yalnızca Japon
> hukuku temas eden işlerde kullanılır (bkz. `karsilastirmali-hukuk-rehberi.md`).
> `japan-legislation-rehberi.md` içindeki genel Japonya rotasını **tamamlar**;
> İngilizce çeviri ve içtihat için o rehber geçerli kalır.

---

## e-Gov 法令API nedir?

**e-Gov 法令API v2** — Japonya'nın resmi ulusal mevzuat veri tabanı üzerindeki
yapılandırılmış API. Dijital Ajans (Digital Agency, デジタル庁) tarafından
işletilir; v2, Mart 2025'te yayımlandı. Çalışma dili **Japonca**dır.

**Kapsam:**
- Tüm ulusal mevzuat: kanunlar (法律), kabine kararnameleri (政令), bakanlık
  yönetmelikleri (省令) — canlı teyitte 9.500+ kayıt döndü
- **JSON** yanıtlar; tam metin, madde yapısı ve metadata bir arada
- **Anahtar kelime araması** — eşleşen cümleleri `<span>` vurgusuyla döndürür
- **Point-in-time (asof)** — mevzuatın belirli bir tarihte yürürlükte olan
  revizyonunu çeker; tadil öncesi/sonrası metin karşılaştırılabilir
- OpenAPI dokümantasyonu: `https://laws.e-gov.go.jp/api/2/swagger-ui`

**ArthurLegal için neden gerekli?** Japonya bugüne dek WebFetch-tahmin
katmanındaydı: yapılandırılmış arama ve tarihli sürüm çekme yolu yoktu. Bu API,
"kaynaksız hukuk yok" ilkesinin iki bacağını — kaynak + çekim tarihi — doğrudan
karşılar; `asof` parametresi sayesinde bir Japon karşı tarafla imzalanan
sözleşmenin **imza tarihindeki** mevzuat metni kesin olarak saptanabilir.
Detay: `karsilastirmali-hukuk-rehberi.md`.

---

## Endpoint şeması

Taban: `https://laws.e-gov.go.jp/api/2`

```
GET /laws?limit={n}&offset={n}          # mevzuat listesi / metadata araması
GET /keyword?keyword={URL-encoded}      # tam metin anahtar kelime araması
GET /law_data/{law_id}                  # tam metin + metadata (JSON)
GET /law_data/{law_id}?asof=YYYY-MM-DD  # o tarihte yürürlükteki revizyon
```

**Canlı teyit edilen davranış (13.08.2026):**

| Endpoint | Teyit | Yanıtın çekirdeği |
|---|---|---|
| `/laws` | ✅ auth'suz JSON | `total_count`, `count`, `next_offset`, `laws[]` (her biri `law_info` + `revision_info` + `current_revision_info`) |
| `/keyword` | ✅ auth'suz JSON | `total_count`, `sentence_count`, `items[]`; `sentences[]` içinde `position` + `<span>` vurgulu `text` |
| `/law_data/{id}` | ✅ auth'suz JSON | `law_info`, `revision_info`, `law_full_text` (hiyerarşik madde yapısı) |
| `/law_data/{id}?asof=` | ✅ | Verilen tarihte yürürlükteki revizyonu döndürür |

**Law ID örnekleri** (teyitli):

| law_id | Mevzuat |
|---|---|
| `321CONSTITUTION` | Japonya Anayasası (日本国憲法, 1947) |
| `417AC0000000086` | Şirketler Kanunu (会社法, 2005 t. 86 s. Kanun) |

Law ID formatı (dönem-yıl + tür kodu + numara) ve diğer endpoint'ler
(`law_file`, `attachment`, revizyon listesi) için swagger-ui esas alınır;
bu rehberde canlı teyit edilmeyen parametre adları kullanılmamalıdır
(entegrasyon öncesi doğrulanmalı).

---

## Uygulamalı örnekler

**1) Anahtar kelimeyle arama — "電気事業" (elektrik işletmeciliği):**

```
WebFetch:
  URL: https://laws.e-gov.go.jp/api/2/keyword?keyword=%E9%9B%BB%E6%B0%97%E4%BA%8B%E6%A5%AD&limit=10
  prompt: "電気事業 geçen mevzuatı listele; her sonuç için law_id, law_title
           ve eşleşen cümleyi (sentences.text) çıkar"
```

Canlı teyitte 2.908 eşleşme döndü; `sentences[]` alanı vurgulu bağlam verir.
Bulunan `law_id` ile bir sonraki adımda tam metne inilir.

**2) Tam metin çekme — Şirketler Kanunu (会社法):**

```
WebFetch:
  URL: https://laws.e-gov.go.jp/api/2/law_data/417AC0000000086
  prompt: "会社法 — birleşme (合併) prosedürüne ilişkin maddeleri ve
           revision_info alanını (son tadil kanunu + yürürlük tarihi) çıkar"
```

**3) Point-in-time — belirli tarihte yürürlükteki metin:**

```
WebFetch:
  URL: https://laws.e-gov.go.jp/api/2/law_data/417AC0000000086?asof=2020-04-01
  prompt: "Bu tarihte yürürlükte olan revizyonun tadil kanunu numarasını ve
           yürürlük tarihini revision_info'dan çıkar"
```

Canlı teyitte bu çağrı, 01.04.2020'de yürürlüğe giren 令和元年法律第二号
(17.05.2019 ilanlı) tadilini içeren revizyonu döndürdü. Çok eski `asof`
tarihleri (revizyon geçmişinin başlangıcından öncesi) 400 dönebilir —
hata durumunda tarihi güncelleyerek yeniden dene.

---

## Atıf disiplini

Japon mevzuatı oturumda fiilen bu API'den çekildiyse:

```
[JP e-Gov — {kanun adı} {madde} (law_id: {id}) — çekim: GG.AA.YYYY]
```

Örnek: `[JP e-Gov — 会社法 m.748 (law_id: 417AC0000000086) — çekim: 13.08.2026]`.
`asof` kullanıldıysa atıfta belirt:
`[JP e-Gov — 会社法 m.748 — asof: 01.04.2020 — çekim: 13.08.2026]`.

Kurallar:
- Çekilmemiş bir Japon normu "biliyorum" diye `[JP e-Gov]` etiketlenemez →
  `[model bilgisi — doğrulayın]`.
- **Otoritatif metin yalnızca Japoncadır.** Rehber veya çeviri üzerinden yapılan
  açıklama doktrin/bağlam düzeyindedir; hüküm kurmaya kaynak, çekilen Japonca
  metindir.
- Japanese Law Translation (aşağıda) çevirisi kullanıldıysa ayrıca ve
  "gayriresmî çeviri" ibaresiyle atıflanır; tek başına otorite olamaz.

---

## Lisans ve sınırlar

**Lisans:** e-Gov verileri **Government of Japan Standard Terms of Use
(政府標準利用規約) v2.0** altındadır — **CC BY 4.0 ile uyumlu**; atıf şartıyla
ticari kullanım dâhil yeniden kullanım serbesttir. Kaynakta 13.08.2026'da bu
şekilde teyit edildi; entegrasyon öncesi güncel sürüm yeniden kontrol edilmeli.

**Sınırlar ve bayraklar (yumuşatılamaz):**
- ⚠️ **Deneme (trial) formatlar:** v2 yanıt formatlarının bir kısmı
  "trial"/değişebilir işaretlidir; resmî veri dokümantasyon sitesi
  (`laws.e-gov.go.jp/docs/`) bütünüyle **α版 (alfa)** etiketlidir ve "önceden
  duyurulmadan değişebilir" der (canlı teyit). Entegrasyonda **şema
  pinlenmeli** — alan adlarına (`law_info`, `revision_info`, `law_full_text`,
  `sentences` vb.) kalıcı kod bağlanacaksa sürüm sabitlenip regresyon testi
  konulmalı.
- ⚠️ **Çeviriler asla otorite değildir:** Adalet Bakanlığı'nın Japanese Law
  Translation sitesi (`japaneselawtranslation.go.jp`) İngilizce çeviriler sunar;
  site kendi beyanıyla çeviriler "not official texts" olup "only the original
  Japanese texts ... have legal effect" (canlı teyit, 13.08.2026). Çeviri
  yalnızca anlama yardımcısıdır.
- **Auth modeli:** v2 lansmanda anahtarsızdı ve 13.08.2026'da anahtarsız
  çalıştığı teyit edildi; kalıcı entegrasyon öncesi tekrar doğrulanmalı.
- **İçtihat yok:** API yalnızca mevzuat içerir; Japon mahkeme kararları için
  `japan-legislation-rehberi.md` içindeki courts.go.jp rotası kullanılır.

---

## Karar kaydı (mini-ADR)

**Bağlam.** Japonya, WebFetch-tahmin katmanındaydı: `japan-legislation-rehberi.md`
HTML sayfa çekimine ve İngilizce çeviri sitesine dayanıyordu; yapılandırılmış
arama, JSON metadata ve tarihli sürüm çekme yolu yoktu. Bu, "kaynak + çekim
tarihi" invariantının tarih bacağını Japonya'da zayıf bırakıyordu.

**Karar.** e-Gov 法令API v2, Japonya için birincil mevzuat rotası olarak
WebFetch katmanında benimsendi. Koşullar: (1) entegrasyonda şema pinlenir —
trial formatlar nedeniyle alan adları sürüme sabitlenir; (2) her kullanımda
Government Standard Terms of Use v2.0 uyarınca atıf verilir; (3) çeviriler
hiçbir zaman otorite olarak sunulmaz.

**Sonuçlar.** Kazanım: anahtar kelime araması, JSON tam metin ve `asof` ile
point-in-time çekim — imza/uyuşmazlık tarihindeki metin kesin saptanır. Eski
rotada kalanlar: İngilizce çeviri (JLT) ve içtihat/regülatör sayfaları
(`japan-legislation-rehberi.md`). Entegrasyonda yeniden doğrulanacaklar: auth
modeli, trial format listesi, `law_file`/`attachment` gibi teyit edilmemiş
endpoint'lerin parametre adları, lisans sürümü.

---

## İlgili rehberler

- `japan-legislation-rehberi.md` — Japonya genel rotası: Japanese Law
  Translation (gayriresmî İngilizce), mahkeme kararları, METI/JFTC; bu API'ye
  erişilemezse **yedek rota** olarak da o rehber kullanılır
- `karsilastirmali-hukuk-rehberi.md` — yabancı hukuk ne zaman ve hangi
  disiplinle devreye girer

---

*Son güncelleme: 13.08.2026. e-Gov 法令API v2 canlı teyit: /laws, /keyword,
/law_data ve asof parametresi anahtarsız JSON döndürdü; lisans ve JLT
gayriresmîlik beyanı kaynağından doğrulandı.*

---

## ArthurLegal MCP — `jp_` araçları

| Alan | Değer |
|------|-------|
| **MCP endpoint** | `https://arthurlegal-mcp.fly.dev/mcp` — ArthurLegal MCP (on dört yargı çevresi tek uçta) |
| **Araç öneki** | `jp_` |
| **Auth** | **Yok** |

| Araç | Ne yapar |
|---|---|
| `jp_search_laws` | Tam metin anahtar kelime araması, kanuna göre gruplanmış |
| `jp_list_laws` | Mevzuat listesi + künye ve yürürlük statüsü |
| `jp_get_law` | `law_id` ile künye + yürürlük statüsü |
| `jp_get_law_text` | Konsolide tam metin, karakterle sayfalanır |
| `jp_get_article` | Tek madde — `"331"` = 第三百三十一条, `"331_2"` = 第三百三十一条の二 |

> ⚠️ **Bir alan adının tersini söyler.** `remain_in_force` **yürürlükte** demek
> değildir; 残存効力'dir — *ilga edilmiş* bir kanunun geçiş hükümleriyle
> artakalan etkisi. Yürürlükteki kanunlar `False` taşır. Adına güvenmek tüm
> canlı külliyatı ilga edilmiş gösterir. Yürürlük `current_revision_status`
> (CurrentEnforced) + `repeal_status` ("None") üzerinden **hesaplanır** ve iki
> girdi de yanıtta verilir; muhakemeyi kontrol edebilirsin.

> ⚠️ **Sayfa boyutu cümle sayar, kanun değil.** `max_sentences=3` tek bir
> kanunun içinde üç cümle getirebilir. Kanun çeşitliliği için değeri yükselt;
> yanıt `statutes_on_this_page` ve `sentence_count`'u ayrı ayrı raporlar.

> ⚠️ **`as_of` tabanı 2017-04-01.** Daha erken bir tarih reddedilir; araç bunu
> söyler, sessizce güncel metne düşmez.

> ⚠️ **İçtihat yoktur.** Japon mahkeme kararları e-Gov'da bulunmaz. Cevap
> mahkeme uygulamasına dayanıyorsa "içtihat kontrol edilmedi" de.

> **Japonca ara:** 会社法, 電気事業, 労働契約. Romanize veya İngilizce sorgular
> çoğunlukla boş döner.
