# AİHM/HUDOC — Kullanım Rehberi (echr-extractor ile yapılandırılmış erişim)

> **Custom MCP server YOK** — HUDOC resmî bir API sözleşmesi yayımlamaz; bu rehber
> `echr-extractor` Python kütüphanesi (Maastricht Law & Tech Lab) üzerinden
> yapılandırılmış erişim + WebFetch ile doğrudan endpoint çekimi prosedürünü tanımlar.
>
> **Durum:** ✅ Açık erişim — **API anahtarı gerekmez**, kayıt gerekmez.
> Birincil yargı çevresi Türkiye'dir; bu kaynak yalnızca işin **AİHS boyutu**
> olduğunda kullanılır (bireysel başvuru, AYM sonrası Strasbourg aşaması,
> AİHS standardıyla karşılaştırma — bkz. `karsilastirmali-hukuk-rehberi.md`).
> AİHM'in **Türkçe çevirili** kararları için birinci durak yargi-mcp'nin
> `aihm_ictihat_ara` aracıdır; bu rehber **tam korpusa doğrudan** erişimi tanımlar.

---

## HUDOC / echr-extractor nedir?

**HUDOC** (`hudoc.echr.coe.int`) — Avrupa İnsan Hakları Mahkemesi'nin resmî karar
veri tabanı; Avrupa Konseyi (Council of Europe) bünyesindeki AİHM Yazı İşleri
tarafından işletilir. **echr-extractor** — Maastricht Üniversitesi Law & Tech
Lab'in bu veri tabanından yapılandırılmış veri çeken açık kaynak Python
kütüphanesi (`maastrichtlawtech/echr-extractor`, Apache-2.0, aktif bakımda;
PyPI son sürüm 1.3.1 — 07.07.2026).

**Kapsam:**
- AİHM kararları (Daire / Komite / Büyük Daire), kabul edilebilirlik kararları,
  metadata (itemid, başvuru no, tarih, önem düzeyi, ihlal edilen maddeler)
- Tam metinler + **bölüm segmentasyonu**: procedure / facts / law / operative
- **Atıf ağı** çıktısı: kararlar arası atıflardan node/edge (DataFrame) üretimi
- Tarih aralığı **batch** çekimi, retry/exponential backoff, CSV/JSON/DataFrame export
- Kimlik doğrulama yok; `pip install echr-extractor` yeterli

**ArthurLegal için neden gerekli?** Türkiye AİHS tarafıdır ve AİHM içtihadı,
AY m.90/5 üzerinden iç hukuk yorumunda doğrudan devreye girer. yargi-mcp'nin
`aihm_ictihat_ara` aracı Türkçe çevirili alt kümeyi tarar; Türkçeye çevrilmemiş
kararlar (korpusun büyük çoğunluğu), yeni tarihli Daire kararları ve atıf-ağı
bağlamı ancak HUDOC'un tamamından gelir. echr-extractor bu tam korpusu belge
başına çekim tarihi damgasıyla, "kaynaksız hukuk yok" ilkesine uygun biçimde
getirir; atıf ağı, AYM/AİHM sonuçlarını çapraz doğrulamada bağlam sağlar.

---

## Endpoint/URI şeması

⚠️ HUDOC'un **resmî API sözleşmesi yoktur** — aşağıdaki endpoint'ler portalın
kendi sorgu arayüzüdür; **haber verilmeden değişebilir**. Kırılma gözlenirse
`aihm_ictihat_ara` + genel WebFetch rotasına dönülür.

**Sorgu API'si (JSON):**
```
https://hudoc.echr.coe.int/app/query/results?query={sorgu}&select={alanlar}&sort={alan}&start=0&length={n}
```

**Tam metin (HTML gövde) dönüşüm endpoint'i:**
```
https://hudoc.echr.coe.int/app/conversion/docx/html/body?library=ECHR&id={itemid}
```

**Resmî atıf/permalink** (JavaScript kabuğu — WebFetch ile içerik okunmaz,
yalnızca atıf URL'si olarak kullanılır):
```
https://hudoc.echr.coe.int/eng?i={itemid}
```

**Sık kullanılan sorgu/metadata alanları:**

| Alan | Anlam |
|---|---|
| `itemid` | Belge kimliği (ör. `001-200042`) — atıfın çapası |
| `appno` | Başvuru numarası (ör. `13716/12`) |
| `docname` | Dava adı |
| `kpdate` | Karar tarihi |
| `importance` | Önem düzeyi (1 = Key case … 4) |
| `languageisocode` | Metin dili (`ENG`, `FRE`, `TUR` çeviriler dâhil) |
| `article` | İlgili AİHS maddeleri |
| `conclusion` | Sonuç (ihlal / ihlal yok) |

**echr-extractor ana fonksiyonları:**

| Fonksiyon | İş |
|---|---|
| `get_echr()` | Metadata çekimi (`start_date`, `end_date`, `language`, `fields`, `batch_size`, `days_per_batch`, `retry_attempts`) |
| `get_echr_extra()` | Metadata + tam metin (paralel indirme) |
| `get_echr_segments()` | Tam metni procedure/facts/law/operative bölümlerine ayırma |
| `get_nodes_edges()` | Atıf ağı node/edge DataFrame'leri |
| `get_document_citations()` | Tek belgenin dış atıflarını çözümleme |

---

## Pratik örnekler

**Örnek 1 — Tarih aralığında karar listesi (sorgu API'si, doğrulanmış):**
```
WebFetch:
  URL: https://hudoc.echr.coe.int/app/query/results?query=contentsitename:ECHR%20AND%20((languageisocode=%22ENG%22))%20AND%20((kpdate%3E=%222020-01-01T00:00:00.0Z%22)%20AND%20(kpdate%3C=%222020-01-15T00:00:00.0Z%22))&select=itemid,docname,appno,kpdate,importance&sort=itemid%20Ascending&start=0&length=3
  prompt: "Sonuçlardaki itemid, dava adı, başvuru no ve karar tarihlerini listele"
```
Doğrulanmış dönüş (13.08.2026): 85 sonuç; ilk üçü arasında
`001-200042` — *Kapmaz v. Turkey* (13716/12) ve
`001-200036` — *Cazac and Surchician v. Moldova and Russia* (22365/10).

**Örnek 2 — Tam metin çekimi (dönüşüm endpoint'i, doğrulanmış):**
```
WebFetch:
  URL: https://hudoc.echr.coe.int/app/conversion/docx/html/body?library=ECHR&id=001-200036
  prompt: "PROCEDURE ve THE LAW bölümlerini çıkar; ihlal sonucunu ve ilgili AİHS maddelerini ver"
```
Doğrulanmış dönüş (13.08.2026): karar tam metni (PROCEDURE ile başlayan
JUDGMENT gövdesi) döner.

**Örnek 3 — Toplu çekim + atıf ağı (echr-extractor, yerel çalıştırma):**
```python
from echr_extractor import get_echr_extra, get_nodes_edges
df, texts = get_echr_extra(start_date="2024-01-01", end_date="2024-06-30",
                           language=["ENG"], save_file="n")
nodes, edges = get_nodes_edges(df)   # atıf ağı — AYM/AİHM çapraz bağlam için
```
Her satıra çekim tarihi damgası eklenir; çıktı CSV/JSON olarak paket
çalışma alanına yazılır.

---

## Atıf disiplini

HUDOC'tan oturumda fiilen çekilen karar:

```
[HUDOC — {Dava adı}, no. {başvuru no}, {karar tarihi} (itemid {001-XXXXXX}) — çekim: GG.AA.YYYY]
```

Örnek: `[HUDOC — Kapmaz v. Turkey, no. 13716/12, 07.01.2020 (itemid 001-200042) — çekim: 13.08.2026]`

- Atıf her zaman **HUDOC'a resmî kaynak olarak** çözülür; permalink
  `https://hudoc.echr.coe.int/eng?i={itemid}` verilir. echr-extractor bir
  **araçtır**, kaynak değildir — atıfta araç adı geçmez.
- Çekilmemiş bir AİHM kararı "biliniyor" diye `[HUDOC]` etiketlenemez →
  `[model bilgisi — doğrulayın]`.
- Türkçe çeviri üzerinden çalışıldıysa kaynak `aihm_ictihat_ara` çıktısındaki
  `source_url`'dir (bkz. `yargi-mcp-rehberi.md`); çeviri ile İngilizce/Fransızca
  otantik metin çelişirse otantik metin esas alınır ve fark `[review]` ile işaretlenir.
- Karar metni alıntılanan her çıktıya Avrupa Konseyi bildirimi eklenir (aşağıda).

---

## Lisans ve sınırlar

- **Karar metinleri:** © Avrupa Konseyi / ECHR-CEDH. Mahkeme sitesindeki metinler,
  **kaynak gösterilmek şartıyla** ve ücretsiz olmak kaydıyla özel kullanım ile
  Mahkeme'nin faaliyetleriyle bağlantılı bilgilendirme/eğitim amaçlı çoğaltılabilir;
  çoğaltmada **"ECHR-CEDH Council of Europe"** ibaresi zorunludur. Bunun dışındaki
  kullanımlar (özellikle ticari) **önceden yazılı izin** gerektirir
  (`echr.coe.int/copyright-and-disclaimer`; sayfa otomatik araçlara 403 dönebilir —
  ibare metni entegrasyon öncesi tarayıcıdan teyit edilmeli).
  **Uygulama:** karar alıntılayan her ArthurLegal çıktısına bu bildirim eklenir.
- **echr-extractor:** Apache-2.0 — paket içinde kullanım serbest; lisans metni korunur.
- **API sözleşmesi yok:** endpoint'ler portalın iç arayüzüdür, haber verilmeden
  değişebilir → kırılma **izlenir**; kırılınca `aihm_ictihat_ara` + WebFetch'e dönülür.
- **JS kabuğu:** `hudoc.echr.coe.int/eng?i=...` sayfası WebFetch ile okunamaz;
  içerik için dönüşüm endpoint'i veya echr-extractor kullanılır.
- **Alternatif — ECHR-OD** (`echr-od/ECHR-OD_process`, MIT; `echr-opendata.eu`):
  **KOŞULLU** — build güncelliği doğrulanamadı (13.08.2026'da site 502; kod tarafında
  ~2 yıl sessizlik gözlendi). Kullanılacaksa pipeline **kendin çalıştırılır** ve
  çıktıya **kendi build tarihin** damgalanır; hazır dump'a güncel muamelesi yapılmaz.
- Doktrin/akademik analiz bağlamdır, otorite değildir; eval verisi hiçbir zaman
  atıf kaynağı olmaz.

---

## Karar kaydı (mini-ADR)

**Bağlam.** AİHS ayağı bugüne dek generic WebFetch katmanındaydı: HUDOC arayüzü
JS kabuğu olduğundan çekim güvenilmezdi; `aihm_ictihat_ara` yalnızca Türkçe
çevirili alt kümeyi görüyordu. Çevrilmemiş korpus, yeni Daire kararları ve
atıf-ağı bağlamı erişim dışıydı.

**Karar.** echr-extractor, WebFetch katmanının üzerinde **yapılandırılmış erişim
aracı** olarak benimsendi — şu koşullarla: (1) karar alıntılayan her çıktıda
Avrupa Konseyi ibaresi, (2) HUDOC arayüzü **sözleşmesiz** kabul edilir ve kırılma
izlenir, (3) atıflar daima HUDOC'a resmî kaynak olarak çözülür.

**Sonuçlar.** Kazanım: belge başına çekim tarihli tam korpus erişimi, bölüm
segmentasyonu ve yargi-mcp'nin AYM/AİHM sonuçlarını çapraz besleyen atıf ağı.
Eski rotada kalan: Türkçe çeviriler `aihm_ictihat_ara`'da; HUDOC kırılırsa
tüm ayak WebFetch'e geri düşer. Entegrasyonda yeniden doğrulanacaklar:
sorgu/dönüşüm endpoint'lerinin çalışırlığı, copyright sayfası ibare metni,
PyPI sürümü ve ECHR-OD build durumu.

---

## İlgili rehberler

| Rehber | İlişki |
|---|---|
| `yargi-mcp-rehberi.md` | AİHM Türkçe kararları (`aihm_ictihat_ara`) + AYM içtihadı — birinci durak |
| `eu-legislation-rehberi.md` | AB hukuku ayağı; AİHS/AB temel haklar kesişimi |
| `karsilastirmali-hukuk-rehberi.md` | Yabancı/uluslararası kaynakların ne zaman devreye gireceği |

---

*Son güncelleme: 13.08.2026. echr-extractor (Apache-2.0, PyPI 1.3.1) üzerinden HUDOC yapılandırılmış erişim; açık erişim, anahtar gerektirmez; HUDOC arayüzü sözleşmesizdir — kırılma izlenir.*