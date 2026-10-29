---
name: legal-research-uk-mevzuat
description: >
  UK mevzuatini The National Archives'in resmi MCP sunucusu uzerinden okur;
  madde duzeyinde, yururluk tarihi ve degisiklik zinciriyle.
user-invocable: true
---

# UK Mevzuatı (TNA resmî MCP)

## Ne zaman kullanılır

İngiliz hukuku uygulanacak hukuk seçilmişse; UK kanunu, ikincil düzenlemesi veya
belirli bir maddesi soruluyorsa; bir hükmün **belirli tarihteki** hâli gerekiyorsa.

## Ne zaman kullanılmaz

UK **içtihadı** için (Find Case Law ayrı bir servistir ve toplu/hesaplamalı
kullanım için ayrı lisans ister). AB hukuku için → `ab-mevzuat`.

## Yöntem

1. Aranan enstrümanı tür/yıl/numara ile kimlikle (ör. `ukpga/2006/46`).
2. Madde düzeyine in; **yürürlük tarihini** kontrol et — UK mevzuatında
   yürürlüğe girmemiş veya yürürlükten kalkmış hükümler aynı sayfada durur.
3. Değişiklik notlarını (amendments) oku; konsolide metin ile yürürlükteki metin
   aynı olmayabilir.

## Sert kurallar

**Yürürlük durumu atfın içindedir.** "Yürürlükte" demeden önce tarihi doğrula;
UK'de bir hükmün kabul edilmiş ama yürürlüğe konmamış olması yaygındır.

Ham API XML/Atom döndürür — JSON bekleyen bir istemciye doğrudan bağlanmaz.
Yapılandırılmış erişim için resmî MCP rotası kullanılır.

Lisans: Open Government Licence v3.0 — atıf yükümlülüğü doğurur.

## Atıf

`[UK Legislation — {enstrüman} {madde} — yürürlük: {tarih} — çekim: GG.AA.YYYY]`

## Bilgi tabanı

`uk-legislation-mcp-rehberi.md` · `uk-legislation-rehberi.md`
