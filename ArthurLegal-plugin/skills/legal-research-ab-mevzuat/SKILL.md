---
name: legal-research-ab-mevzuat
description: >
  AB enstrumanlarini ve ABAD kararlarini EUR-Lex Cellar uzerinden KESIN olarak
  kimlikler (CELEX/ELI); metin eu_get_document_text ile cekilir.
user-invocable: true
---

# AB Mevzuatı ve ABAD İçtihadı (EUR-Lex Cellar)

## Ne zaman kullanılır

Bir AB tüzüğü, direktifi veya ABAD kararı **kesin olarak kimliklenmeli**;
konsolidasyon ve tadil zinciri önemli; ya da bir ulusal ölçütün hangi AB
enstrümanını uyguladığı soruluyor.

## Yöntem

1. `eu_search_eu_law(query="...")` ile **CELEX numarasını** bul (gerekirse `eu_sparql`).
2. **Metni `eu_get_document_text(celex=..., language=...)` ile çek** — EUR-Lex
   `legal-content` sayfaları WebFetch'te metin döndürmez.
3. `eu_get_metadata(celex=...)` ile yürürlüğü (`in_force`) ve konsolidasyon durumunu kontrol et.

## Sert kurallar

**Konsolide olmayan bir metin yürürlükteki sürüm gibi sunulmaz.** Atıfta CELEX
kimliği, konsolidasyon durumu ve erişim tarihi birlikte verilir.

**Yaptırım rotası değildir.** Bir yaptırım enstrümanının OJ referansı, o kişinin
**güncel listede olduğu** anlamına gelmez — güncel listeleme resmî konsolide listeden
(`yaptirim-tarama-rehberi.md`) doğrulanır.

Ulusal uygulama ölçütleri ayrı korpustur (Almanya için → `alman-hukuku`).

Lisans: içerik CC BY 4.0, metadata CC0.

## Atıf

`[EUR-Lex — CELEX {no} — {konsolidasyon durumu} — çekim: GG.AA.YYYY]`

## Bilgi tabanı

`eurlex-cellar-rehberi.md` · `eu-legislation-rehberi.md`
