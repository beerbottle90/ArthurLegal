# atif-kaynak — Skill Referans Kitapçığı

> Kapsam: Atıf doğrulama, kaynakça, stil dönüştürme · Rol: **Doğrulama motoru**
> Toplam skill: 3
> Kullanım: `/atif-kaynak:<skill-adı>`
> 🔴 Konum: Bu plugin **sıfır-halüsinasyon atıf** kuralının uygulayıcısıdır.
> Çekilmemiş hiçbir kaynak dipnota giremez.

## İçindekiler

- /atif-kaynak:atif-dogrulama — Bir dipnot/kaynakça listesini tek tek birincil kaynaktan doğrular
- /atif-kaynak:kaynakca-uret — Doğrulanmış kaynaklardan hedef stilde kaynakça üretir
- /atif-kaynak:stil-donusturme — Atıfları stiller arası dönüştürür (Klasik TR ↔ OSCOLA ↔ Bluebook ↔ …)

---

## /atif-kaynak:atif-dogrulama

---
name: atif-dogrulama
description: >
  Kullanıcının dipnot veya kaynakça listesini alır; her kalemi birincil kaynaktan
  (MCP / DOI / resmî yayın) doğrulamaya çalışır. Doğrulanamayanı AÇIKÇA işaretler.
  Asla uydurmaz, asla "muhtemelen doğru" demez.
user-invocable: true
---

# Atıf Doğrulama

## Neden en kritik skill

Uydurma dipnot yalnızca hata değil; YÖK Bilimsel Araştırma ve Yayın Etiği Yönergesi'nin
**intihal / sahtecilik / çarpıtma** başlıklarına giren, unvan geri alınmasına kadar
gidebilen bir risktir. Dil modelleri sahte DOI, sahte esas/karar numarası ve sahte sayfa
numarası üretmeye **yapısal olarak eğilimlidir**. Bu skill o eğilime karşı kurulmuştur.

## Doğrulama kaynakları ve sırası

| Kaynak türü | Doğrulama yolu | Provenans etiketi |
|---|---|---|
| TR mevzuat | Mevzuat MCP | `[Mevzuat MCP — GG.AA.YYYY]` |
| Yargıtay / Danıştay / BAM | Yargı MCP | `[Yargı MCP — kurum — Esas/Karar — GG.AA.YYYY]` |
| AYM (norm / bireysel) | Yargı MCP | `[Yargı MCP — AYM — Esas/Karar veya BB no — GG.AA.YYYY]` |
| Resmî Gazete | WebFetch resmigazete.gov.tr | `[Resmî Gazete — sayı/tarih]` |
| ABD içtihadı | CourtListener MCP | `[CourtListener — mahkeme — citation — GG.AA.YYYY]` |
| İsviçre içtihadı / doktrin | OpenCaseLaw.ch MCP | `[OpenCaseLaw.ch — mahkeme — ref — GG.AA.YYYY]` |
| İsviçre federal mevzuat | Fedlex MCP | `[Fedlex — SR no — GG.AA.YYYY]` |
| AB hukuku | EUR-Lex (CELEX) | `[EUR-Lex — CELEX no — GG.AA.YYYY]` |
| AİHM | HUDOC (App. no) | `[HUDOC — App. no — GG.AA.YYYY]` |
| Akademik makale (DOI) | Crossref API | `[Crossref — DOI — GG.AA.YYYY]` |
| Akademik metadata | OpenAlex / Semantic Scholar | `[OpenAlex — ID — GG.AA.YYYY]` |
| Açık erişim dergi | DOAJ | `[DOAJ — ISSN — GG.AA.YYYY]` |
| Abonelik veritabanı | **erişim yok** | `[Lexpera/Kazancı/HeinOnline — MANUEL DOĞRULAYIN]` |
| Kitap / monografi | genellikle API yok | `[MANUEL DOĞRULAYIN — künye teyidi]` |

Detay → `references/akademik-api-rehberi.md` · `references/ticari-veritabani-rehberi.md`

## Girdi

Kullanıcının dipnot listesi veya kaynakçası. Ham makale metni **gerekmez**.

## Adımlar

1. Her kalemi ayrıştır: yazar · başlık · yayın yeri · yıl · sayfa · DOI/esas-karar no.
2. Türüne göre doğrulama kaynağını seç (yukarıdaki tablo).
3. Çek. **Çekemiyorsan uydurma.**
4. Karşılaştır: künye alanları eşleşiyor mu? Özellikle **yıl, cilt, sayı, sayfa aralığı**.
5. Sınıflandır (aşağıdaki tablo).
6. Rapor üret.

## Sınıflandırma

| İşaret | Anlam | Ne yapılmalı |
|---|---|---|
| ✅ **Doğrulandı** | Kaynak çekildi, künye eşleşti | — |
| ⚠️ **Kısmen doğrulandı** | Kaynak var ama bir alan tutmuyor (yıl/sayfa/cilt) | Alanı düzelt |
| 🟠 **Doğrulanamadı — erişim yok** | Kaynak muhtemelen gerçek, ama API yok (kitap, abonelik DB) | Kullanıcı manuel doğrulasın |
| 🔴 **Bulunamadı** | Aramalarda hiçbir iz yok | **Kaynağı kaldırın veya elinizdeki fiziki/PDF nüshadan künyeyi teyit edin.** Uydurma atıf riski. |
| 🔴 **Çelişkili** | DOI başka esere ait; esas/karar no başka kararı gösteriyor | Ciddi hata — düzeltilmeden gönderilmemeli |

> 🔴 **Bulunamadı** çıkan bir kalem için asla "muhtemelen şudur" diye alternatif **önerme**.
> Kullanıcıya bulunamadığını söyle ve nasıl doğrulayacağını anlat.

## Çıktı

Üst başlık: `AKADEMİK ÇALIŞMA NOTU — TASLAK (yazarlık ve sorumluluk yazardadır)`

```
ATIF DOĞRULAMA RAPORU — [N] kalem

✅ Doğrulandı            : [n]
⚠️ Kısmen doğrulandı     : [n]
🟠 Doğrulanamadı (erişim) : [n]
🔴 Bulunamadı / çelişkili : [n]   ← GÖNDERİM ÖNCESİ ÇÖZÜLMELİ

---
[dn 12] ✅  Yazar, "Başlık", Dergi, C.X S.Y (2024) s. 45-67
        Doğrulama: [Crossref — 10.xxxx/yyyy — 09.07.2026]

[dn 13] ⚠️  Yazar, ... (2023) s. 12
        Doğrulama: [Crossref — 10.xxxx/zzzz — 09.07.2026]
        Uyuşmazlık: Crossref yılı 2024; dipnotta 2023.

[dn 14] 🔴  Yazar, "Başlık", Dergi (2021)
        Crossref, OpenAlex ve Semantic Scholar'da bulunamadı.
        Yapılacak: Elinizdeki nüshadan künyeyi teyit edin; teyit edemiyorsanız
        bu dipnotu KALDIRIN. Uydurma atıf, yayın etiği ihlali riskidir.
```

Sonda: `⚠️ ÜYZ Beyanı` + `⚠️ Doğrulama notu` (hangi API'ler kullanıldı, hangileri kapsam dışı).

## Yapma

- Bulunamayan bir kaynak için **alternatif künye önerme**.
- "Bu kaynak muhtemelen gerçektir" **deme**. Doğrulandı ya da doğrulanmadı.
- Erişimin olmayan bir veritabanından çekmiş gibi davranma.
- Sayfa numarasını **hesaplama veya tahmin etme**.

---

## /atif-kaynak:kaynakca-uret

---
name: kaynakca-uret
description: >
  Yalnızca DOĞRULANMIŞ kaynaklardan, hedef stilde kaynakça üretir. Doğrulanmamış kalemleri
  ayrı bir "doğrulanmadı" bölümünde tutar; sessizce kaynakçaya karıştırmaz.
user-invocable: true
---

# Kaynakça Üretimi

## Önkoşul

Bu skill, `/atif-kaynak:atif-dogrulama` çıktısı üzerinde çalışır. Doğrulama yapılmadıysa
önce onu çalıştır. Doğrulanmamış kalem **kaynakçaya girmez**.

## Girdi

- Doğrulama raporu (veya doğrulanmış künye listesi)
- Hedef stil (profilden oku; yoksa sor)
- Hedef derginin yazım kuralları (varsa) — **dergi kuralı stil kılavuzundan üstündür**

## Kaynakça bölümleri (Türk hukuk teamülü)

Türk hukuk dergilerinde kaynakça genellikle türe göre ayrılır:

```
KAYNAKÇA

Kitaplar ve Monografiler
Makaleler
İçtihat
Mevzuat
Elektronik Kaynaklar
```

> Bazı dergiler tek liste ister. Derginin kuralını uygula.

## Çıktı

1. Hedef stilde kaynakça
2. `🔴 KAYNAKÇAYA ALINMAYANLAR` bölümü — doğrulanamayan kalemler ve nedeni
3. `⚠️ Doğrulama notu`

## Yapma

- Doğrulanmamış kalemi sessizce kaynakçaya ekleme.
- Eksik alanı (sayfa aralığı, cilt no) **doldurma**; `[EKSİK — teyit edin]` yaz.

---

## /atif-kaynak:stil-donusturme

---
name: stil-donusturme
description: >
  Doğrulanmış atıfları stiller arasında dönüştürür: Klasik TR tam-dipnot, OSCOLA, Bluebook,
  AGLC, McGill, Chicago. Künye verisini değiştirmez, yalnızca biçimlendirir.
user-invocable: true
---

# Atıf Stili Dönüştürme

## Desteklenen stiller

| Stil | Coğrafya | Not |
|---|---|---|
| **Klasik TR tam-dipnot** | Türkiye | Baskın; kıta Avrupası geleneği |
| **OSCOLA** | Birleşik Krallık | Dipnot temelli, minimal noktalama |
| **Bluebook** | ABD | Kapsamlı; baskı numarasını doğrula |
| **AGLC** | Avustralya | Dipnot temelli |
| **McGill Guide** | Kanada | İki dilli (EN/FR) |
| **Chicago (Notes-Bibliography)** | Disiplinlerarası | Hukukta birincil stil değildir |

Detay → `references/atif-usulu-tr-rehberi.md` ·
`references/atif-stilleri-uluslararasi-rehberi.md`

## Kural

1. **Dergi kılavuzu her zaman üstündür.** Profil "OSCOLA" dese bile dergi klasik TR
   istiyorsa dergiye uy ve bunu söyle.
2. Dönüştürme **yalnızca biçimseldir**. Yıl, sayfa, cilt gibi verileri değiştirme.
   Eksik alan varsa `[EKSİK — teyit edin]` bırak; uydurma.
3. Mükerrer atıf biçimini stile göre ayarla:
   - Klasik TR: `Yazar, age., s. 40` veya kısa başlık
   - OSCOLA uyarlaması (bazı TR dergileri): `Yazar (n 12) 40`
   - Bluebook: `Yazar, supra note 12, at 40`
   > `supra`, `infra`, `op cit`, `loc cit`, `id` klasik TR usulünde **kullanılmaz**.

## Çıktı

Yan yana karşılaştırmalı tablo (kaynak stil → hedef stil) + dönüştürülmüş liste +
`⚠️ Doğrulama notu` (hangi stil kılavuzunun hangi baskısına dayanıldığı; baskı numarası
güncelliği kullanıcı tarafından teyit edilmeli).

## Yapma

- Stil kılavuzunun baskı/yıl bilgisini **kesin** verme; "teyit edin" notu düş.
- Dönüştürürken künye alanı **ekleme veya çıkarma**.
