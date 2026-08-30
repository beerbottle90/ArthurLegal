# Düzenleyici kaynak kataloğu (reg-feed)

> `regulatory-legal` skill'inin besleme yapılandırması için küratörlü kaynak
> listesi. Kullanıcının watchlist'inde kapsama boşluğu varsa buradan tamamla.
>
> ✅ **Aşağıdaki her URL 30.08.2026'da canlı test edildi.** Çalışmayanlar
> listeye alınmadı; test edilen ama başarısız olanlar en altta kayıt için duruyor.

---

## Nasıl kullanılır

1. Kullanıcının `CLAUDE.md` → watchlist'indeki **kategorileri** belirle.
2. O kategorilerde **yapılandırılmış besleme sayısı sıfır ya da çok azsa**
   boşluğu digest'in başında **bir kez** yüzeye çıkar.
3. Kullanıcı onaylarsa beslemeyi yapılandırmaya ekle.

> ⚠️ Katalogdaki bir kaynağı kullanıcıya sormadan watchlist'e **ekleme**.
> Kapsam kararı kullanıcınındır; bu dosya öneri listesidir.

---

## 🇹🇷 Türkiye

| Kurum | Kaynak | Not |
|---|---|---|
| Resmî Gazete | `https://www.resmigazete.gov.tr/` ✅ | Günlük. **YargiMCP `resmi_gazete_fihrist` aracı varsa onu tercih et** — yapılandırılmış döner |
| KVKK | `https://www.kvkk.gov.tr/` ✅ | Kurul kararları + duyurular |
| EPDK | `https://www.epdk.gov.tr/` ✅ | Enerji piyasası düzenlemeleri |
| Rekabet Kurumu | `https://www.rekabet.gov.tr/` ✅ | Kurul kararları, birleşme bildirimleri |

## 🇪🇺 Avrupa Birliği

| Kurum | Kaynak | Not |
|---|---|---|
| EUR-Lex | `https://eur-lex.europa.eu/EN/display-feed.rss?myRssId=...` ✅ | Resmî Gazete RSS |
| ESMA | `https://www.esma.europa.eu/rss.xml` ✅ | Sermaye piyasaları |
| ACER | `https://www.acer.europa.eu/rss.xml` ✅ | **AB enerji düzenleyicisi — enerji pratiği için birincil** |
| EDPB | `https://www.edpb.europa.eu/news/news_en` ✅ | ⚠️ `/feed_en` **404**; HTML sayfa kullan |
| CNIL (FR) | `https://www.cnil.fr/fr/rss.xml` ✅ | Fransız veri koruma |

## 🇬🇧 Birleşik Krallık

| Kurum | Kaynak | Not |
|---|---|---|
| legislation.gov.uk | `https://www.legislation.gov.uk/new/data.feed` ✅ | **Yeni mevzuat Atom feed'i** |
| ICO | `https://ico.org.uk/about-the-ico/media-centre/` ✅ | ⚠️ `/news-and-blogs/rss/` **404** |
| Ofgem | `https://www.ofgem.gov.uk/publications` ✅ | ⚠️ `/rss/publications` **404** |

## 🇺🇸 ABD

| Kurum | Kaynak | Not |
|---|---|---|
| Federal Register | `https://www.federalregister.gov/api/v1/documents.json` ✅ | **JSON API** — filtrelenebilir, en kullanışlısı |
| SEC | `https://www.sec.gov/news/pressreleases.rss` ✅ | Basın açıklamaları |
| FTC | `https://www.ftc.gov/feeds/press-release.xml` ✅ | Rekabet + tüketici |

## 🌍 Yaptırım (STOP-RULE kaynakları)

| Liste | Kaynak | Not |
|---|---|---|
| AB konsolide (FSF) | `https://webgate.ec.europa.eu/fsd/fsf/public/files/xmlFullSanctionsList_1_1/content?token=dG9rZW4tMjAxNw` ✅ | XML; CSV eşleniği de var |
| BM konsolide | `https://scsanctions.un.org/resources/xml/en/consolidated.xml` ✅ | ⚠️ `/search` yolu **404** |
| OFAC SDN | `https://www.treasury.gov/ofac/downloads/sdn.xml` ✅ | CSV: `.../sdn.csv` |
| OFAC son işlemler | `https://ofac.treasury.gov/recent-actions` ✅ | HTML |

> 🔴 **Yaptırım taraması bir digest işi değildir.** Bu kaynaklar izleme içindir;
> karşı taraf taraması için **OpenSanctions** birincildir
> (`opensanctions-rehberi.md`). Digest'te çıkan bir isim, tarama yerine geçmez.

---

## Test edilip **başarısız** olanlar (kayıt için — kullanma)

| Kaynak | Sonuç (30.08.2026) |
|---|---|
| `edpb.europa.eu/feed_en` | 404 |
| `ico.org.uk/.../news-and-blogs/rss/` | 404 |
| `ofgem.gov.uk/rss/publications` | 404 |
| `ferc.gov/news-events/news` | **403** — FERC agent'a kapalı, alternatifi bulunamadı |
| `bafin.de/.../RSSNewsfeed_Meldungen.xml` | 404 |
| `ofac.treasury.gov/system/files/126/sdn.xml` | 404 — doğrusu `treasury.gov/ofac/downloads/sdn.xml` |

> 📌 **Kaynak eklerken durum koduna güvenme, içeriği doğrula.** Bu paketin
> v1.6.0 denetiminde HTTP 200 dönen ama boş JS kabuğu veren kaynaklar bulundu
> (bkz. `MCP-ROADMAP.md` → Lüksemburg).

---

*Test: 30.08.2026 — tüm ✅ işaretli URL'ler canlı doğrulandı.
Sürüm: v1.6.0 (yeni — daha önce atıf vardı, dosya yoktu).*
