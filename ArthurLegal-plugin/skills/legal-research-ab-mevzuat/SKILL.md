---
name: legal-research-ab-mevzuat
description: >
  AB enstrumanlarini ve ABAD kararlarini EUR-Lex Cellar uzerinden KESIN olarak
  kimlikler (CELEX/ELI); metin EUR-Lex'te okunur.
user-invocable: true
---

# AB Mevzuatı ve ABAD İçtihadı (EUR-Lex Cellar)

## Ne zaman kullanılır

Bir AB tüzüğü, direktifi veya ABAD kararı **kesin olarak kimliklenmeli**;
konsolidasyon ve tadil zinciri önemli; ya da bir ulusal ölçütün hangi AB
enstrümanını uyguladığı soruluyor.

## Yöntem

1. Cellar üzerinde SPARQL ile **CELEX numarasını veya ELI'yi** bul.
2. **Metni EUR-Lex'te oku** — Cellar kimlik ve metadata katmanıdır, operatif
   metin katmanı değil.
3. Konsolidasyon durumunu ve yürürlüğü kontrol et.

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
