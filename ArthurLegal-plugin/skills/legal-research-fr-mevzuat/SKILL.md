---
name: legal-research-fr-mevzuat
description: >
  Fransiz mevzuatini DILA acik veri dokumleri ve Legifrance uzerinden okur.
  REST API degil, bulk dokum tabanli bir kaynaktir.
user-invocable: true
---

# Fransız Mevzuatı (DILA açık veri)

## Ne zaman kullanılır

Fransız kanunu, kararnamesi veya kod maddesi soruluyorsa; Fransız hukuku
uygulanacak hukuk seçilmişse.

## Kaynağın şekli — önce bunu bil

DILA **REST API değil**, toplu döküm (tar.gz + delta, eski XML/DTD) yayımlar.
Yapılandırılmış sorgu için önce ingestion + JSON servis katmanı gerekir; bu
nedenle bu kaynak **connector almadı**. Günlük kullanımda Legifrance doğrudan
okunur.

Judilibre (içtihat) REST API'si vardır ama PISTE kaydı + API anahtarı ister —
kimlik bilgisisiz erişim tercihine aykırı olduğu için bilinçli olarak ertelenmiştir.

## Yöntem

1. Legifrance üzerinde enstrümanı kimlikle (kod adı + madde numarası).
2. Yürürlük (`version en vigueur`) ve tadil tarihini kontrol et.
3. Toplu döküm gerekiyorsa DILA açık veri portalından çek; lisans **Licence Ouverte**.

## Sert kurallar

Konsolide sürüm ile yürürlükteki sürüm farkı Fransız mevzuatında sık — atıfta
sürüm tarihi verilir. Fransız içtihadı için ayrı erişim gerekir; bu skill mevzuat
kapsamındadır.

## Atıf

`[FR Mevzuat — Légifrance — {kod/kanun} m.{no} — sürüm: {tarih} — çekim: GG.AA.YYYY]`

## Bilgi tabanı

`france-dila-rehberi.md` · `france-legislation-rehberi.md`
