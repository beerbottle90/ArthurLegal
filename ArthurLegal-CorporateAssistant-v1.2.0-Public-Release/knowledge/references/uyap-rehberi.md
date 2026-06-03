# UYAP (Ulusal Yargı Ağı Bilişim Sistemi) – Pratik Rehber

> Türk yargısının elektronik altyapısı. Davaların açılması, takibi, belge sunumu, kararların tebliği UYAP üzerinden yapılır. [ŞİRKET ADI] pratiğinde **dış vekiller UYAP avukat portalı** üzerinden erişir; in-house genelde dış vekilden alınan raporlara bakar.

## UYAP modülleri (litigation için)

| Modül | Kullanım |
|---|---|
| **UYAP Avukat Portalı** | Dava dosyalarına erişim, dilekçe sunma, duruşma takvimi |
| **UYAP Vatandaş Portalı** | Vatandaşın kendi davalarını görmesi |
| **UYAP Kurum Portalı** | Kamu kurumlarının erişimi ([ŞİRKET ADI] için sınırlı) |
| **e-Duruşma** | Online duruşma katılım (pandemi sonrası kalıcı) |
| **UYAP Bilirkişi Portalı** | Bilirkişilerin atama ve rapor sunumu |
| **EBYS entegrasyonu** | Elektronik belge yönetim sistemi |

## Avukat girişi

- **e-İmza** veya **mobil imza** (Turkcell, Vodafone, Türk Telekom)
- Baro kayıt bilgileri ile

## [ŞİRKET ADI] pratiğinde tipik akış

1. **Yeni dava** — Mahkemeden [ŞİRKET ADI]'a yapılan tebligat KEP üzerinden gelir (TTK m. 18/3) veya fiziksel olarak. In-house Counsel dış vekili haberdar eder.
2. **Dış vekil dosyayı UYAP'tan açar** — taraflar, mahkeme, esas no, tebligatlar görülür.
3. **Belgeleri çeker** — dava dilekçesi, ekleri, mahkeme ara kararları.
4. **Aylık özetler** — dış vekil UYAP'tan dava durum raporları çıkarır, Excel formatında [ŞİRKET ADI]'a gönderir.
5. **Duruşma takibi** — UYAP duruşma günlerini gösterir; e-duruşma talep edilebilir.

## In-house tarafında UYAP

[ŞİRKET ADI] in-house hukuk müşaviri genelde UYAP avukat portalına **doğrudan giriş yapmaz** (dış vekil giriyor) — ancak:

- Vatandaş portalından **kendi davalarımı** görebilir (eğer şahsen taraf varsa)
- Kurum portalına [ŞİRKET ADI]'ın resmi kanalları üzerinden erişim olabilir (ihtisas mahkemelerinde)

## Kritik belgeler ve sunum (HMK + UYAP)

| Belge | Format | UYAP üzerinden mi? |
|---|---|---|
| Dava dilekçesi | PDF (e-imzalı) | Evet (m. 119) |
| Cevap dilekçesi | PDF | Evet |
| Delil eki | PDF/Word/Excel | Evet |
| Bilirkişi raporu | PDF (bilirkişi e-imzası) | Evet |
| Mahkeme kararı | PDF | Evet, vekile UYAP üzerinden tebliğ |
| Karşı vekil tebligatı | PDF | UYAP veya KEP/fiziksel posta |

## Yararlı pattern'lar

### Dava durum bilgisi sorgulama (dış vekilden)

In-house olarak istek formu:

```markdown
Sayın [vekil],

[Esas no] dosyası için UYAP üzerinden:
1. Son durum (sonraki duruşma tarihi)
2. Karşı tarafın yeni sunduğu delil/dilekçe (varsa)
3. Mahkeme ara kararları (varsa)
4. Bilirkişi raporu durumu (atandı/sunuldu)

bilgisini rica ederim.

Teşekkürler.
[Counsel]
```

### Karşı taraf tebligatını UYAP'tan çekme

Karşı tarafa tebligat **UYAP üzerinden** veya KEP üzerinden yapılır. [ŞİRKET ADI]'da KEP tebligatı zorunludur (TTK m. 18/3 tacir).

## Tipik sorunlar ve çözüm

| Sorun | Çözüm |
|---|---|
| UYAP'a dış vekil giriş yapamıyor (e-imza süresi dolmuş) | Avukatı yeni e-imzayla mı? Veya başka vekil üzerinden? |
| Mahkeme kararı UYAP'tan tebliğ geldi ama dış vekil görmedi | E-tebligat UYAP'ta okunmuş sayılır (Tebligat K.); süre işlemiş, derhal aksiyon |
| Karşı taraf vekili UYAP üzerinden değil fiziksel sunmuş | Mahkemenin kabulu vardır ama dış vekilimiz fiziksel kopyaya da bakmalı |
| e-Duruşma talep ettik ama mahkeme reddetti | Fiziksel duruşma gerekli; dış vekil İstanbul'dan [İşletme Yeri]'ya gidiyor — maliyet artar |

## Yarg MCP — UYAP entegre

Yarg MCP'nin **Emsal (UYAP)** aracı UYAP arşivindeki emsal kararlara erişir:

```
mcp__claude_ai_Yarg_MCP__search_emsal_detailed_decisions(
  arananKelime="<konu>",
  baslangicTarihi="2023-01-01"
)
```

Bu **karar arşividir**, dava durum sorgulama değildir. Dava durum için her zaman dış vekil.

## [ŞİRKET ADI]-özel notlar

- **[İşletme Yeri] İş Mahkemesi** ve **Karşıyaka Asliye Hukuk** — UYAP destekli ama bazı duruşmalar fiziksel yapılır; İzmir'deki yerel vekil önemli.
- **Ankara Danıştay** — tamamen UYAP üzerinden; yazılı yargı ağırlıklı.
- **İstanbul Anadolu ATM** — UYAP + duruşma karması.

## Bağlantılı referanslar

- [HMK rehberi](hmk-rehberi.md)
- [İSG dava rehberi](isg-dava-rehberi.md)
- [Yarg MCP rehberi](yargi-mcp-rehberi.md)
