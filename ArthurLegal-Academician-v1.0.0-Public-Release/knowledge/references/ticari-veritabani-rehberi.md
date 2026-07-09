# Ticari Veritabanları — Dürüst Sınır Beyanı

> Bu dosyanın amacı, asistanın **erişemediği** kaynaklardan alıntı yapıyormuş gibi
> davranmasını önlemektir.

---

## Kural

Aşağıdaki veritabanlarının **halka açık, dokümante API'si yoktur** ve bu asistan onlara
**erişemez**. Asistan bunlardan çekmiş gibi davranamaz.

Bu kaynaklardan gelen her künye `[MANUEL DOĞRULAYIN]` etiketiyle işaretlenir.

---

## Türkiye

| Platform | Kapsam | Erişim | API |
|---|---|---|---|
| **Lexpera** | Mevzuat, içtihat, kitap, madde şerhi, makale | Kurumsal abonelik | Dokümante resmî API yok |
| **Kazancı** | İçtihat ve mevzuat bilgi bankası | Kurumsal abonelik | Yok |
| **Jurix** | Hukuk **dergileri** odaklı, makale arşivi | Abonelik | Yok |
| **Legalbank** | Karar, mevzuat, makale, dilekçe | Abonelik | Yok |
| **Hukuk Türk / Sinerji / Kanunum** | Mevzuat + içtihat | Abonelik | Yok |

> Türk hukuk **doktrininin** (monografi, şerh, makale) büyük kısmı bu platformlarda ve
> basılı eserlerdedir. Literatür taraması bu nedenle **eksiktir** ve asistan bunu her
> seferinde beyan eder. → `/arastirma-tasarim:literatur-haritasi`

---

## Uluslararası

| Platform | Kapsam | Erişim | API |
|---|---|---|---|
| **HeinOnline** | Tarihsel hukuk dergileri (sayfa-birebir PDF) | Üniversite aboneliği | Kurumsal API (anahtar/IP) |
| **Westlaw / Westlaw Precision** | ABD, UK, uluslararası; içtihat + editoryal katman (KeyCite) | Kurumsal | Kurumsal, ücretli |
| **LexisNexis / Lexis+** | ABD, UK, uluslararası; Shepard's | Kurumsal | Kurumsal, ücretli |
| **Bloomberg Law** | ABD hukuk + regülasyon, dockets | Kurumsal | Sınırlı |
| **Kluwer Arbitration** | Uluslararası tahkim | Abonelik | Halka açık API yok |
| **Beck-online / juris** | Almanya: Kommentar, NJW, içtihat | Abonelik | Halka açık API yok |
| **vLex** (Fastcase dahil) | 100+ ülke | Abonelik | Geliştirici portalı var; MCP doğrulanmalı |

> **HeinOnline**, dergi makalesi atfı için altın standarttır (orijinal sayfa numaraları).
> Erişiminiz varsa dipnot sayfa numaralarını oradan teyit edin.

---

## Asistanın davranışı

1. Kullanıcı "Lexpera'dan şu kararı bul" derse: erişimi olmadığını söyler; Yargı MCP'yi
   dener; bulamazsa `[MANUEL DOĞRULAYIN]` verir.
2. Bir doktrin görüşünü "Lexpera'da şöyle deniyor" diye **sunmaz**.
3. Abonelik veritabanından geldiği söylenen künyeyi **doğrulamadan** kabul etmez;
   kullanıcıya teyit ettirir.
4. `akademisyen-profili.md` → *Erişilebilen veritabanları* tablosuna bakar; kullanıcının
   erişimi varsa **manuel doğrulama adımını** ona verir.

---

## Sonuç

Bu paketin literatür taraması, **kütüphane taramasının yerine geçmez.** En güçlü olduğu
yer: DOI'li akademik makalelerin doğrulanması, TR içtihat/mevzuatın MCP'den verbatim
çekilmesi ve karşılaştırmalı hukuk için açık kaynaklardır.

---

## İlgili

`akademik-api-rehberi.md` · `karsilastirmali-hukuk-rehberi.md`
