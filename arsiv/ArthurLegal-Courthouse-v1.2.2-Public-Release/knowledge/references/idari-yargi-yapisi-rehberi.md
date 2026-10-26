# Türk İdari Yargı Yapısı — Danıştay Daire Haritası

> 3 dereceli idari yargı: İdare Mahkemesi → BİM → Danıştay. Bu rehber özellikle **Danıştay daire görevlerini** netleştiriyor.

## 3 derece akış

```
İdari işlem (Kurum/Bakanlık) →
İYUK m. 7 (60 gün; vergi mahkemesinde 30 gün) → İdare veya Vergi Mahkemesi (ilk derece) →
İYUK m. 45 (30 gün) → Bölge İdare Mahkemesi (istinaf) →
İYUK m. 46 (30 gün) → Danıştay (temyiz, ilgili daire) →
[İDDK / VDDK — BİM ısrar kararının temyizi, İYUK m. 50/5]
```

## Danıştay daire görevleri (temyiz aşaması)

### Daire görev haritası (temyiz aşaması)

| Daire | Kapsam |
|---|---|
| **5. Daire** | Genel idari uyuşmazlık, memur statü |
| **8. Daire** | Belediye / imar / yapı |
| **10. Daire** | Çevre + doğal kaynak |
| **13. Daire** | EPDK + Rekabet + BDDK + SPK + KGK + KİK (düzenleyici kurum) |
| **14. Daire** | ÇED + imar/çevre ek |
| **İDDK** | Birleştirici, ısrar incelemesi |

### Vergi ve diğer daireler

> Vergi daireleri `vergi-hakim` ve `idari-hakim` plugin'lerini ilgilendirir.

- 1. Daire: Vatandaşlık + nüfus
- 2. Daire: Atama, görevde yükselme
- 3. Daire: **Vergi — KDV, ÖTV**
- 4. Daire: **Vergi — Gelir/Kurumlar vergisi**
- 6. Daire: Toplu konut, yapı
- 7. Daire: **Vergi — Damga, MTV, harçlar**
- 9. Daire: **Vergi cezası**
- 11. Daire: Sosyal güvenlik
- 12. Daire: Atama, disiplin
- 15. Daire: Eğitim, üniversite

## Danıştay ilk derece görevli olduğu istisnalar

**Danıştay K. m. 24/1 (m. 30 yürürlükten kaldırılmıştır):**
- Cumhurbaşkanı kararları
- Cumhurbaşkanlığı kararnameleri dışında Cumhurbaşkanınca çıkarılan düzenleyici işlemler
- Bakanlıklar, kamu kuruluşları veya kamu kurumu niteliğindeki meslek kuruluşlarınca çıkarılan ve **ülke çapında uygulanacak** düzenleyici işlemler (ör. genel tebliğ ve yönetmelikler; normatif düzenleyici — bireysel idari işlem DEĞİL)
- Birden çok idare veya vergi mahkemesinin yetki alanına giren işler ve m. 24/1'de sayılan diğer işler

Bu durumda **doğrudan Danıştay'da** dava açılır; dava dairesinin ilk derece sıfatıyla verdiği kararın temyizini İDDK veya VDDK inceler (Danıştay K. m. 38).

⚠️ EPDK / Rekabet / KVKK / KİK / BDDK / SPK gibi kurumların **Tebliğ veya Yönetmelik** düzeyindeki normatif düzenlemeleri, ülke çapında uygulanacak düzenleyici işlem niteliğindeyse doğrudan Danıştayda dava konusu edilir (Danıştay K. m. 24/1-c).

**Ama** aynı kurumların **bireysel idari işlemleri** (lisans iptali, idari ceza, başvuru reddi) için İdare Mahkemesi (Ankara) ilk derece.

## Bölge İdare Mahkemesi (BİM) yapısı

8 BİM:
- Ankara, İstanbul, İzmir, Konya, Bursa, Erzurum, Gaziantep, Samsun

Her BİM içinde:
- İdare Dava Daireleri (istinaf)
- Vergi Dava Daireleri

Not: Düzenleyici kurum (EPDK/Rekabet/KVKK/KİK vb.) kararları kurumların Ankara merkezli olması nedeniyle çoğunlukla **Ankara** idari yargı çevresinde görülür.

## İDDK (İdari Dava Daireleri Kurulu)

**Görevleri (Danıştay K. m. 38):**
- a) İdare Mahkemesi **ısrar** kararlarını temyizen inceler
- b) Danıştay dairelerinden **ilk derece** olarak verilen kararları temyizen inceler

Not: Bugünkü düzende Danıştayın bozma kararına uyma veya ısrar kararını bölge idare mahkemesi verir; ısrar kararının temyizini konusuna göre İDDK veya VDDK inceler (İYUK m. 50/3, 50/5). Vergi uyuşmazlıklarında aynı görevler Vergi Dava Daireleri Kurulundadır (Danıştay K. m. 38/2).

Israr üzerine verilen İDDK ve VDDK kararlarına uyulması zorunludur (İYUK m. 50/5).

## ArthurLegal MCP (`tr_`)

Bedesten birleşik API ile alt dereceleri (İdare Mah. + BİM) çekebilirsin:

```
tr_ictihat_ara(
  query="<konu>",
  date_from="2022-01-01"
)
```

Danıştay daire bazlı:

```
tr_ictihat_ara(
  chamber="13. Daire",
  query="<konu>"
)

tr_ictihat_ara(
  chamber="İdari Dava Daireleri Kurulu",
  query="<konu>"
)
```

## Bağlantılı

- [İYUK rehberi](iyuk-rehberi.md)
- [ÇED rehberi](ced-rehberi.md)
- [Yürütmenin durdurulması rehberi](yurutmenin-durdurulmasi-rehberi.md)
- [ArthurLegal MCP TR rehberi](yargi-mcp-rehberi.md)
