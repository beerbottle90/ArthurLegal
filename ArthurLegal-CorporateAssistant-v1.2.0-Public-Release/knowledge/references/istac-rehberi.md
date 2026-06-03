# ISTAC ve Uluslararası Tahkim Rehberi

> [ŞİRKET ADI] için stratejik dava alanlarından biri: tahkim. [BORU HATTI PROJESİ], intra-group [ANA ORTAK] işlemleri, büyük EPC sözleşmeleri tahkim klozu içerir.

## ISTAC nedir?

**İstanbul Tahkim Merkezi (ISTAC)** — Türkiye'nin bağımsız uluslararası tahkim kurumu. 2014'te kuruldu. Türk hukuku/Türk tarafları için ICC alternatifi.

- **Web:** www.istac.org.tr
- **Kurallar:** ISTAC Tahkim Kuralları (2016, güncel revizyon)
- **Dil:** Türkçe + İngilizce (taraflar seçer)
- **Hızlı tahkim:** Acele tahkim usulü (6 ay hedefli)

## Mevzuat dayanağı

- **HMK m. 412-444** — Genel tahkim hükümleri
- **4686 sayılı Milletlerarası Tahkim Kanunu (MTK)** — uluslararası tahkim
- **5718 sayılı Milletlerarası Özel Hukuk ve Usul Hukuku Kanunu (MÖHUK)** — yabancı tahkim kararlarının tanınması
- **New York Konvansiyonu (1958)** — Türkiye tarafı (1991'de katıldı)

## [ŞİRKET ADI] pratiği için tahkim klozu önerileri

### TL anlaşmazlık (Türk tarafları)
**ISTAC İstanbul** — masraf düşük, hızlı, Türkçe dilinde işliyor.

Sözleşme klozu örneği:
```
Bu sözleşmeden doğan tüm uyuşmazlıklar İstanbul Tahkim Merkezi (ISTAC)
Tahkim Kuralları uyarınca, üç hakem tarafından kesin olarak çözümlenecektir.
Tahkim yeri İstanbul, dili Türkçedir. Uygulanacak hukuk Türk hukukudur.
```

### Uluslararası anlaşmazlık (yabancı counter-party)
**ICC** (Paris, Cenevre, Singapur) veya **LCIA** (Londra) — sektörde tanınmış, uluslararası geçerlilik kuvvetli.

Klüze örneği:
```
Any dispute arising out of or in connection with this Agreement shall be
finally settled under the Rules of Arbitration of the International Chamber
of Commerce by three arbitrators appointed in accordance with the said Rules.
The seat of arbitration shall be Geneva. The language of arbitration shall be
English. The applicable law shall be [Turkish law / English law / other].
```

### [BORU HATTI PROJESİ] / hükümetlerarası anlaşma alanı
[BORU HATTI PROJESİ] Hükümetlerarası Anlaşması özel hukuki rejimde. Uyuşmazlıklar genelde **investor-state arbitration** (ICSID veya UNCITRAL) — derin uluslararası uzmanlık.

## Tahkim klozu hata-tipleri

| Hata | Sonuç |
|---|---|
| "Tahkim İstanbul'da yapılacaktır" — hangi kurum, dil belirtilmemiş | Patolojik kloz; mahkemede dava açma yolu açılabilir |
| Yetki + tahkim çelişik | Genelde tahkim önceliklidir ama mahkeme yorumu değişir |
| Tek hakem önerisi (büyük tutarlı dava) | Karar tek görüş; itiraz mümkün değil |
| Karar diliyle sözleşme dili farklı | İnfaz aşamasında çeviri/tercüme yükümlülük |
| "Türk mahkemeleri kesin yetkili" + tahkim klozu | Bir taraf tahkimi başlatamaz; kloz iptal edilebilir |

## Tahkim itirazı (HMK m. 116/c)

Eğer karşı taraf **geçerli bir tahkim klozu varken mahkemede dava açtıysa**, [ŞİRKET ADI]'ın ilk cevap dilekçesinde:

```markdown
USUL İTİRAZI: Davaya konu sözleşme [...] m. [...] uyarınca tahkim klozu
içermektedir. Bu klozdan doğan uyuşmazlık [ISTAC/ICC] tahkimine tabi olup,
mahkemenin görevsizliğinin tespiti talep edilir. (HMK m. 116/c)
```

⚠️ Bu itiraz **ilk cevap dilekçesinde** sunulmazsa tahkim hakkı düşer (HMK m. 412/3). Çok kritik süre.

## Yarg MCP — tahkim emsal

Tahkim klozu yorumu, tanıma-tenfiz davaları için:

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="tahkim itiraz mahkeme görevsizlik",
  daire="Hukuk Genel Kurulu",
  baslangicTarihi="2022-01-01"
)
```

Yabancı tahkim kararının tanınması:
```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="yabancı tahkim karar tanıma tenfiz New York",
  baslangicTarihi="2022-01-01"
)
```

## [ŞİRKET ADI]-özel notlar

### Intra-group [ANA ORTAK] işlemleri
Transfer pricing, ham petrol alım fiyatlandırması gibi konularda Bakü ile uyuşmazlık çıkması mümkün. Tahkim seçeneği:
- **ISTAC** — TL hukuku
- **Stockholm Chamber of Commerce (SCC)** — Azerbaycan tercih ediyor (Bakü'den uzak ama tarafsız)
- **Türkiye-Azerbaycan İkili Yatırım Antlaşması** (BIT) — investor-state tahkim seçenek

### [HALKA AÇIK İŞTİRAK] — KAP açıklama
[HALKA AÇIK İŞTİRAK] büyük tahkim kararı durumunda KAP özel durum açıklaması.

### [BORU HATTI PROJESİ] hükümetlerarası anlaşma
[BORU HATTI PROJESİ] Hükümetlerarası Anlaşması (TR + Azerbaycan + Gürcistan) + Ev Sahibi Hükümet Anlaşması (HGA) — uluslararası antlaşma rejimi. Uyuşmazlıklar genelde devletler arası arabuluculuk, dış vekil uzman gerek.

## Bağlantılı

- [HMK rehberi](hmk-rehberi.md) — HMK m. 412 vd. tahkim
- [Yarg MCP rehberi](yargi-mcp-rehberi.md)
