---
name: legal-research-jp-mevzuat
description: >
  Japon ulusal mevzuatini e-Gov API v2 uzerinden okur; imza veya uyusmazlik
  tarihindeki metin icin as-of-date cekim destekler.
user-invocable: true
---

# Japon Mevzuatı (e-Gov API v2)

## Ne zaman kullanılır

Japon kanunu, kabine kararnamesi veya bakanlık yönetmeliği soruluyorsa; Japon
karşı taraf veya Japon hukuku uygulanacak bir enstrüman kapsamdaysa.

## Yöntem

1. `KeywordSearch` ile mevzuatı bul → `law_id` al.
2. `GetLawData` ile tam metni çek.
3. `revision_info` alanından yürürlük ve tadil durumunu doğrula.
4. İmza veya uyuşmazlık tarihindeki metin gerekiyorsa `asof=YYYY-MM-DD` kullan
   **ve bunu atıfta belirt**.

## Sert kurallar

**Otoritatif metin YALNIZCA Japoncadır.** Japanese Law Translation çevirileri
gayriresmîdir ve bağlayıcı metin olarak atıf verilemez; yalnız anlama yardımcısıdır.

**Japon içtihadı bu API'de YOKTUR.** Sorulursa kontrol edilmiş gibi ima etme,
yokluğunu söyle.

Lisans: Government of Japan Standard Terms of Use v2.0 (CC BY 4.0 uyumlu).

## Atıf

`[JP Mevzuat — e-Gov — {kanun adı} — law_id {id} — asof {tarih} — çekim: GG.AA.YYYY]`

## Bilgi tabanı

`japan-egov-api-rehberi.md` · `japan-legislation-rehberi.md`
