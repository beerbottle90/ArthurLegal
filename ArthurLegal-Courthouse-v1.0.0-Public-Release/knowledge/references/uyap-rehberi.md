# UYAP (Ulusal Yargı Ağı Bilişim Sistemi) — Mahkeme Pratiği Rehberi

> Türk yargısının elektronik altyapısı. Mahkeme hâkimleri ve kalem personeli dosya açma, inceleme, karar yazma/imzalama, tebligat ve müzekkere çıkışını UYAP üzerinden yürütür.
> ⚖️ Bu rehber mahkeme (hâkim + kalem) bakışındandır; taraf/vekil erişimi yalnızca bağlam olarak anılır.

## UYAP modülleri (mahkeme tarafı)

| Modül | Kullanan | İşlev |
|---|---|---|
| **Hâkim/Savcı ekranı** | Hâkim | Dosya inceleme, ara karar, karar yazımı + e-imza, duruşma yönetimi |
| **Personel (kalem) ekranı** | Yazı işleri/zabıt kâtibi | Dosya açma, tevzi, tebligat/müzekkere çıkışı, harç/gider, tutanak |
| **e-Duruşma / SEGBİS** | Hâkim + kalem | Sesli-görüntülü duruşma, istinabe, uzaktan ifade/tanık |
| **Bilirkişi Portalı** | Bilirkişi (atama mahkemece) | Atama, rapor sunumu, ücret |
| **Avukat / Vatandaş Portalı** | Taraf/vekil | Dilekçe sunma, dosya görüntüleme (mahkeme dışı taraf) |
| **EBYS entegrasyonu** | Kalem | Elektronik belge yönetimi, gelen-giden evrak |

## Hâkim tarafında tipik akış

1. **Tevzi edilen dosya** hâkim ekranına düşer; taraflar, esas no, talep, tebligatlar görülür.
2. **İnceleme** — dilekçeler, deliller, bilirkişi raporu, ara kararlar tek ekranda.
3. **Ara karar / tensip** — UYAP üzerinden oluşturulur, kaleme havale edilir.
4. **Karar yazımı** — gerekçeli karar UYAP'ta yazılır, **e-imza** ile imzalanır.
5. **Tefhim/tebliğ** — karar UYAP üzerinden taraflara/vekillere tebliğe çıkar; süreler tebliğden işler.

## Kalem tarafında tipik akış

1. **Dosya açılış & tevzi** — yeni dava kaydı, otomatik tevzi.
2. **Tebligat çıkışı** — UYAP + UETS (e-tebligat) → `tebligat-7201-rehberi.md`, `kep-etebligat-rehberi.md`.
3. **Müzekkere** — kurum yazışmaları UYAP üzerinden.
4. **Harç/gider** — tahsilat kaydı, eksik harç muhtırası → `harc-gider-rehberi.md`.
5. **Duruşma tutanağı** — zabıt kâtibi tutanağı UYAP'ta tutar; SEGBİS kaydı.

## Belge & sunum (HMK/CMK/İYUK + UYAP)

| Belge | Format | UYAP |
|---|---|---|
| Dava/cevap dilekçesi (taraf) | PDF (e-imzalı) | Avukat portalından sunulur |
| Ara karar / tensip | UYAP | Hâkim oluşturur |
| Bilirkişi raporu | PDF (bilirkişi e-imzası) | Bilirkişi portalı |
| Gerekçeli karar | UYAP + e-imza | Hâkim imzalar, tebliğe çıkar |
| Tebligat mazbatası | UYAP/UETS/fiziksel | Kalem takip eder |

## UYAP Emsal — içtihat arşivi (Yargı MCP üzerinden)

UYAP karar arşivindeki emsal kararlara **Yargı MCP** ile erişilir (gerekçe/karar yazımında emsal taraması için):

```
mevzuat/yargı araçları → Bedesten/Emsal birleşik arama (konu + tarih aralığı)
```

> Bu **karar arşivi** araştırmasıdır; canlı dosya durumu hâkim/kalem ekranındadır. Emsal atıfları daima **verbatim** çekilir: `[Yargı MCP — kurum — Esas/Karar — GG.AA.YYYY]`.

## Tipik teknik sorunlar (mahkeme)

| Sorun | Not |
|---|---|
| e-İmza süresi dolmuş | Karar imzalanamaz; e-imza yenileme |
| e-Tebligat okunmamış ama süre işliyor | UETS'te gönderimi izleyen 5. günün sonunda tebliğ sayılır (süre işler) |
| SEGBİS/e-duruşma bağlantı sorunu | İstinabe/uzaktan ifade için yedek plan; tutanağa şerh |
| Fiziksel sunulan evrak | Taranıp dosyaya eklenir; UYAP kaydı tutulur |

## Bağlantılı referanslar

- [HMK rehberi](hmk-rehberi.md) · [CMK rehberi](cmk-rehberi.md) · [İYUK rehberi](iyuk-rehberi.md)
- [Tebligat 7201 rehberi](tebligat-7201-rehberi.md) · [KEP/e-tebligat rehberi](kep-etebligat-rehberi.md)
- [Yargı MCP rehberi](yargi-mcp-rehberi.md)
