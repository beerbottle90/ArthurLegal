---
name: legal-research-karsi-taraf-kimlik
description: >
  Karsi tarafin KIM oldugunu (LEI, tescilli unvan, yargi cevresi, ana ortaklik
  zinciri) yaptirim taramasindan ONCE sabitler. Sira degismez.
user-invocable: true
---

# Karşı Taraf Kimlik Çözümleme ve Tarama (GLEIF → OpenSanctions)

## Ne zaman kullanılır

Yeni karşı taraf KYC dosyası; imza öncesi kontrol; grup yapısı soruları ("kimin
iştiraki?", "nihai ana ortak kim?"); **her OpenSanctions taramasının ön adımı olarak.**

## Sıra sabittir: önce kimlik, sonra listeler

Serbest metin unvanla yaptırım taraması **hem yanlış pozitif** (aynı adlı
şirketler) **hem yanlış negatif** (transliterasyon kayması — AZ/RU/CN adlarında
belirgin) üretir. Taraf önce tescilli kimliğine indirgenir, sonra taranır.

## Araçlar

GLEIF REST API (`api.gleif.org`, auth'suz, CC0 — WebFetch) + OpenSanctions.

## Yöntem

1. **Kimlik çözümle:** `GET /api/v1/autocompletions?field=fulltext&q={unvan}` →
   yargı çevresi/adres eşleşen adayı seç → `GET /api/v1/lei-records/{lei}` ile
   `registration.status` kontrol et (LAPSED kayıtta veri bayat olabilir).
2. **Grubu haritala:** `/ultimate-parent` ve `/direct-parent`. Hem sözleşme
   tarafını hem nihai ana ortağı **ayrı ayrı** tara.
3. **Tara:** doğrulanmış unvan + yargı çevresi + sicil no ile OpenSanctions.
4. **Raporla:** `[GLEIF — LEI {lei} — çekim: GG.AA.YYYY]` +
   `[OpenSanctions — {taraf} — çekim: GG.AA.YYYY]`

## Sert sınırlar (her raporda beyan edilir)

- **GLEIF Level 2 = muhasebe konsolidasyonu ana ortaklığı, gerçek kişi UBO DEĞİL.**
  MASAK/AML gerçek faydalanıcı tespiti yerel sicil veya beyan ister.
- **LEI yokluğu ≠ şirket yokluğu.** Kapsam düzenlenmiş işlemlere eğiktir.
- **İlişki kaydının yokluğu bağımsızlık kanıtı değildir.**
- Yaptırım çıktısı, aleyhe işlemden önce **insan uyum incelemesinden** geçer.

## Bilgi tabanı

`gleif-rehberi.md` · `yaptirim-tarama-rehberi.md` · `yaptirim-tarama-rehberi.md`
