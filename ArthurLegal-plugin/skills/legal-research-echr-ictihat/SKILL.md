---
name: legal-research-echr-ictihat
description: >
  AIHM (ECHR) kararlarini HUDOC uzerinden arar. HUDOC'un resmi API sozlesmesi
  yoktur; arayuz habersiz degisebilir.
user-invocable: true
---

# AİHM İçtihadı (HUDOC)

## Ne zaman kullanılır

Bir AİHS maddesi (ör. m.6 adil yargılanma, m.8 özel hayat, 1 No'lu Protokol m.1
mülkiyet) ekseninde AİHM içtihadı gerekiyorsa; Türkiye aleyhine verilmiş kararlar
soruluyorsa; iç hukuk yolu tüketilmesi tartışılıyorsa.

## Kaynağın şekli — önce bunu bil

**HUDOC'un resmî bir API sözleşmesi yoktur.** Arayüz habersiz değişebilir; ham
uca doğrudan bağlanmak kırılganlığı ürünleştirir. Yapılandırılmış erişim için
`echr-extractor` (Apache-2.0) tabanlı sarmalayıcı deseni kullanılır.

Düz WebFetch HUDOC'ta çalışmaz — site bir JS uygulamasıdır; sorgu ucu kullanılır.

## Yöntem

1. Başvuru numarası biliniyorsa doğrudan onunla; bilinmiyorsa madde + ülke +
   tarih aralığı ile ara.
2. Kararın **kesinleşip kesinleşmediğini** kontrol et (Chamber / Grand Chamber /
   Committee ayrımı ve Büyük Daire'ye sevk).
3. Türkçe çeviri varsa gayriresmî olduğunu belirt; bağlayıcı metin resmî dildedir.

## Sert kurallar

**Başvuru numarası ve karar tarihi atfın zorunlu parçasıdır.** AİHM kararlarında
aynı taraf adıyla birden çok karar bulunur.

Bir Daire kararı ile Büyük Daire kararı aynı ağırlıkta sunulmaz.

## Atıf

`[AİHM — {taraf} v. {devlet}, başvuru no {no}, {tarih} — {daire} — çekim: GG.AA.YYYY]`

## Bilgi tabanı

`echr-hudoc-rehberi.md`
