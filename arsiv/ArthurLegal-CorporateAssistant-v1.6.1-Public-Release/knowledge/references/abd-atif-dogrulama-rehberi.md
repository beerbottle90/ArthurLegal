# ABD Atıf Doğrulama — Kullanım Rehberi (eyecite + CourtListener citation-lookup)

> **Durum:** ⚠️ Ayrı bir MCP/connector değil — CourtListener connector'ının kardeş yeteneği (citation-lookup API) + yerel Python kütüphaneleri (eyecite, reporters-db, courts-db, x-ray).
> **Erişim:** ✅ Kütüphaneler açık kaynak, API anahtarı gerekmez, tamamı offline çalışır. Yalnızca CourtListener `citation-lookup` REST uç noktası token ister (`Authorization: Token ...`).
> **Yargı çevresi notu:** ArthurLegal'in birincil yargı çevresi **Türkiye**'dir. Bu rehber yalnızca dosya ABD hukukuna dokunduğunda ve ABD atıfları (case citation, statutory citation) doğrulanacağında kullanılır. Çok yargı çevreli dosyalarda önce `karsilastirmali-hukuk-rehberi.md` içindeki yönlendirme kurallarına bakın.

## Bu yığın nedir?

Free Law Project (kâr amacı gütmeyen, CourtListener'ın işletmecisi) tarafından geliştirilen, ABD hukuki atıflarının makine ile çıkarılması, normalize edilmesi ve doğrulanması için kullanılan açık kaynak araç zinciri:

- **eyecite** (`github.com/freelawproject/eyecite`) — metin bloklarından atıf çıkarır ve çözümler: tam atıf (*Bush v. Gore, 531 U.S. 98*), kısa atıf (*531 U.S., at 99*), *id.*, *supra*, kanun atfı (*Mass. Gen. Laws ch. 1, § 2*) ve dergi atfı (*1 Minn. L. Rev. 1*). 55 milyondan fazla gerçek atıf üzerinde doğrulanmıştır; CourtListener ve Harvard Caselaw Access Project üretim hattında kullanılır.
- **reporters-db** (`github.com/freelawproject/reporters-db`) — 1.167 ABD reporter'ı + 2.102 isim varyasyonu; JSON ve Python (`REPORTERS`, `LAWS`, `JOURNALS`) olarak erişilir. eyecite'ın tanıma altyapısıdır.
- **courts-db** (`github.com/freelawproject/courts-db`) — güncel ve tarihsel tüm ABD mahkemeleri; `find_court()` (serbest metinden string eşleme) ve `find_court_by_id()` fonksiyonları.
- **x-ray** (`github.com/freelawproject/x-ray`) — PDF'lerde **kötü redaksiyon** (metnin üzerine yalnızca siyah kutu çizilmiş, altındaki metin hâlâ okunabilir) tespiti. `pip install x-ray`.
- **CourtListener citation-lookup API** — çıkarılan atıfların gerçek bir karara karşılık gelip gelmediğini teyit eden REST uç noktası (aşağıda).

**ArthurLegal için neden gerekli?** "Kaynaksız hukuk yok" ilkesinin ABD ayağındaki en büyük tehdit uydurma atıftır: biçimsel olarak kusursuz görünen ama var olmayan bir *F.3d* atfı, elle bakışla ayırt edilemez. Bu yığın, taslak cevaptaki her ABD atfını sunumdan **önce** deterministik olarak çıkarıp CourtListener veritabanına karşı doğrulamayı mümkün kılar; doğrulanamayan atıf hiçbir zaman otorite olarak gösterilmez. Bu, paketlerdeki CourtListener MCP'nin mevcut atıf-doğrulama uyarısının ("her atıf sunulmadan önce doğrulanır") operasyonel karşılığıdır.

## Kodlanan disiplin (üç kural)

1. **Çıkar → doğrula → sonra göster.** Taslak cevaptaki her ABD atfı eyecite ile çıkarılır ve CourtListener'a karşı doğrulanır. Doğrulama başarısız olursa (status 404/400) atıf otorite olarak **sunulmaz**; asistan "bu atfı doğrulayamadım" der ve atfı doğrulanmamış olarak işaretler. Status 300 (birden çok eşleşme) belirsizlik demektir — eşleşme adayları gösterilmeden atıf tekilmiş gibi sunulmaz.
2. **Deterministik normalizasyon.** Reporter ve mahkeme adları reporters-db / courts-db üzerinden kanonik forma çevrilir; böylece bulgu defterine (ledger) yazılan kayıtlar deterministiktir — aynı atıf iki farklı yazımla iki kayıt üretmez.
3. **PDF girişinde x-ray QA.** Rekabet Gözcüsü intake hattına giren her PDF, salt-ekleme (append-only) bulgu defterine yazılmadan önce x-ray'den geçirilir. Kötü redaksiyon tespit edilirse belge karantinaya alınır ve tespit defterde ayrı bir olay olarak kaydedilir; redaksiyon altındaki metin bulgu olarak kullanılmaz.

## Endpoint / URI şeması

**Citation-lookup (CourtListener REST v4):**

```
POST https://www.courtlistener.com/api/rest/v4/citation-lookup/
Authorization: Token <token>

# İki sorgu biçimi:
#   text=<64.000 karaktere kadar serbest metin>
#   volume=<cilt>&reporter=<reporter kısaltması>&page=<sayfa>
```

Yanıt: atıf başına JSON nesnesi — `citation`, `normalized_citations` (yazım hatası/kanonik olmayan kısaltma düzeltmeleri), `start_index`/`end_index`, `status`, `error_message`, `clusters` (eşleşen CourtListener kayıtları).

| `status` | Anlamı | Ledger davranışı |
|---|---|---|
| 200 | Atıf bulundu | Doğrulanmış; kanonik formla kaydet |
| 300 | Birden çok eşleşme | Belirsiz; adaylar çözülmeden otorite olarak sunma |
| 400 | Geçersiz reporter kısaltması | Doğrulanamadı; asistan bunu açıkça söyler |
| 404 | Biçimi geçerli ama veritabanında yok | Doğrulanamadı; **uydurma atıf şüphesi** — otorite olarak asla gösterme |
| 429 | Throttle (dakikada 60 geçerli atıf) | `wait_until` süresini bekle, yeniden dene |

Limitler: istek başına en çok 250 atıf; `text` alanı 64.000 karakter (~50 sayfa).

**Yerel kütüphaneler (offline, anahtar gerekmez):**

```
pip install eyecite          # atıf çıkarma/çözümleme
pip install reporters-db     # reporter veritabanı (JSON + Python)
pip install courts_db        # mahkeme veritabanı, find_court()
pip install x-ray            # PDF kötü-redaksiyon tespiti; CLI: xray dosya.pdf
```

## Uygulamalı örnekler

**Örnek 1 — Taslak cevaptaki atıfların sunum öncesi doğrulanması (MCP + REST):**

Paketlerdeki CourtListener connector'ı bu iş için hazır araçlar taşır; önce bunlar denenir:

```
mcp: CourtListener → extract_citations
  args: { "text": "Under Bush v. Gore, 531 U.S. 98 (2000), and id. at 104, ..." }
# → tam atıf + id. zinciri çözülmüş olarak döner

mcp: CourtListener → analyze_citations
  args: { "text": "<taslak cevabın tamamı>" }
# → her atıf için eşleşme/doğrulama durumu
```

Connector'ın bulunmadığı ortamda (ör. Copilot Studio) aynı sonuç REST ile alınır:

```
POST https://www.courtlistener.com/api/rest/v4/citation-lookup/
  text=Under Bush v. Gore, 531 U.S. 98 (2000), the Court held ...
# → [{ "citation": "531 U.S. 98", "status": 200, "clusters": [ ... ] }]
```

`status` 200 dönmeyen hiçbir atıf cevapta otorite olarak yer almaz.

**Örnek 2 — Kütüphane dokümantasyonunun ve davranışının teyidi (WebFetch):**

```
WebFetch:
  url: https://github.com/freelawproject/eyecite
  prompt: "Hangi atıf türlerini çıkarıyor, lisansı ne, hangi veritabanları üzerine kurulu?"

WebFetch:
  url: https://wiki.free.law/c/courtlistener/help/api/rest/v4/citation-lookup
  prompt: "citation-lookup uç noktasının parametreleri, limitleri ve status kodları neler?"
```

(Not: `courtlistener.com/help/api/rest/citation-lookup/` adresi `wiki.free.law` üzerine 301 ile yönlenir; güncel doküman oradadır.)

**Örnek 3 — Rekabet Gözcüsü intake'inde redaksiyon QA (yerel):**

```
xray indirilen-dava-dosyasi.pdf
# → JSON: sayfa numarası, şüpheli kutunun koordinatları, kutunun ALTINDAKİ metin
# Boş sonuç → belge ledger'a girebilir.
# Dolu sonuç → karantina + ledger'a "bad redaction detected" olayı.
```

## Türkçe atıf ayrıştırıcısına şablon

eyecite'ın mimarisi — atıf kalıplarının koddan ayrı, sürümlenebilir bir veritabanında (reporters-db) tutulması, çıkarımın deterministik ve offline olması, *id./supra* gibi bağlam-bağımlı kısa atıfların zincir çözümlemesi — ArthurLegal'in planlanan **Türkçe atıf ayrıştırıcısı** için referans şablondur: Yargıtay ("Y. 11. HD, E. 2020/1234, K. 2021/5678"), Danıştay ve AYM (başvuru no / E-K sayısı) atıf kalıpları, reporters-db'nin muadili bir TR kalıp veritabanında tutulacak ve aynı çıkar-doğrula-sonra-göster disiplinine Yargı MCP doğrulaması eşlik edecektir.

## Atıf disiplini

Doğrulanmış her ABD atfı, kanonik form + doğrulama kaynağı + çekim tarihi ile sunulur:

```
[CourtListener citation-lookup — Bush v. Gore, 531 U.S. 98 (2000) — status 200 — çekim: 13.08.2026]
```

Kurallar:

- Atıf metni, `normalized_citations` alanındaki **kanonik form** ile yazılır; kullanıcının verdiği yazım farklıysa bu ayrıca belirtilir.
- Doğrulanamayan atıf gösterilecekse yalnızca şu biçimde gösterilebilir: "⚠️ doğrulanamadı (status 404) — otorite olarak kullanılmayın".
- Çekim tarihi, doğrulamanın yapıldığı gündür; eski bir doğrulama yeni bir cevapta tarihsiz tekrar kullanılamaz.
- Değerlendirme (eval) verisi hiçbir zaman atıf kaynağı değildir; doktrin bağlamdır, otorite değildir.

## Lisans ve sınırlar

- **Lisans:** eyecite, reporters-db, courts-db ve x-ray'in tamamı **BSD-2-Clause** (kaynak depolarında doğrulandı, 13.08.2026). Ticari kullanım ve yeniden dağıtım serbesttir; lisans ve telif notunun korunması gerekir.
- **API tarafı:** citation-lookup uç noktası token ister; dakikada 60 geçerli atıf throttle'ı ve istek başına 250 atıf limiti vardır. Toplu doğrulama işleri buna göre parçalanmalıdır.
- **Kapsam sınırı:** CourtListener 404'ü "karar hiç var olmamış" demek değildir — "veritabanında yok" demektir. Bu yüzden 404, atfı çürütmez; yalnızca **doğrulanamadığını** kanıtlar ve doğrulanamayan atıf otorite olarak sunulmaz. Bu ayrım kullanıcıya da aynen aktarılır.
- **Governance bayrakları (yumuşatılamaz):** (1) doğrulamadan geçmemiş metin hiçbir zaman "doğrulanmış" gibi sunulmaz; (2) x-ray QA'sından geçmemiş PDF Rekabet Gözcüsü bulgu defterine giremez; (3) x-ray'in ortaya çıkardığı, redaksiyon altındaki içerik bulgu veya delil olarak kullanılamaz — yalnızca "kötü redaksiyon var" tespiti kaydedilir; (4) eval verisi atıf kaynağı değildir.
- **Sürüm bağımlılığı:** reporters-db/courts-db sayıları (1.167 reporter, 2.102 varyasyon) sürüme bağlıdır (v3.2.32 itibarıyla); pin'lenen sürüm ledger meta verisine yazılmalıdır (entegrasyon öncesi doğrulanmalı).

## İlgili rehberler

- `courtlistener-rehberi.md` — CourtListener connector'ının arama/docket yetenekleri ve mevcut atıf-doğrulama uyarısı
- `us-legislation-rehberi.md` — ABD mevzuat kaynakları (kanun atıflarının içerik doğrulaması)
- `yargi-mcp-rehberi.md` — Türk içtihat/mevzuat doğrulaması; Türkçe atıf ayrıştırıcısının doğrulama arka ucu
- `karsilastirmali-hukuk-rehberi.md` — yargı çevresi yönlendirme kuralları