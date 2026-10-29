---
name: legal-research-abd-atif-dogrulama
description: >
  Taslakta gecen her ABD atifini sunulmadan ONCE CourtListener'a karsi dogrular.
  Uydurma atif savunmasi - LLM'lerin en bilinen halusinasyon sinifi.
user-invocable: true
---

# ABD Atıf Doğrulama (uydurma atıf savunması)

## Ne zaman kullanılır

Taslak cevap, memo veya inceleme **herhangi bir biçimde** ABD atıfı içeriyorsa:
tam (`Bush v. Gore, 531 U.S. 98 (2000)`), kısa (`531 U.S., at 99`), `Id.` / `supra`
zinciri, veya kanun (`15 U.S.C. § 1`). Kullanıcı "bu atıflar gerçek mi?" diye
sorduğunda da.

**Bu bir son kontrol değil, bir geçiştir.** Doğrulanmamış ABD atıfı sunulmaz.

## Araçlar

CourtListener MCP — `extract_citations` (yerel eyecite geçişi, yalnız çıkarım) ve
`analyze_citations` (veritabanına karşı doğrulama).

## Yöntem

1. Taslaktaki tüm atıfları çıkar (`extract_citations`, `resolve: true` —
   `Id.`/`supra` zinciri öncülüne otomatik çözülür).
2. Her benzersiz atıfı doğrula (`analyze_citations`). Durum yorumu:

| Durum | Anlamı | Yapılacak |
|---|---|---|
| 200 | Bulundu | Otorite olarak kullanılabilir, `absolute_url` ile atıfla |
| 404 | Bulunamadı | Otorite olarak **GÖSTERME**; "doğrulayamadım" beyanı zorunlu |
| 400 | Ayrıştırılamadı | **Muhtemel halüsinasyon** — atıfı çıkar ve bildir |
| 300 | Çoklu eşleşme | Yıl/mahkeme ile teke indir; indirgenemiyorsa belirt |
| 429 | Hız limiti | Bekle ve yeniden dene — doğrulamayı **atlama** |

3. Reporter/mahkeme adlarını kanonik biçime çevir (reporters-db / courts-db
   konvansiyonu) — aynı karar iki yazımla iki kayıt üretmemeli.

## Sert kurallar

**Doğrulama sonucu bir SONUÇTUR.** "Doğrulayamadım" ile "yok" farklı iddialardır;
hangisi kanıtlandıysa o söylenir.

**Bellekten atıf dizesi kurulmaz.** Yalnız doğrulama geçişinden dönen atıflar sunulur.

CourtListener'a erişilemiyorsa ABD atıfları `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>` etiketi
taşır ve bu durum cevabın görünür kısmında belirtilir.

## Atıf

`[CourtListener — {dava}, {atıf} — çekim: GG.AA.YYYY]`

## Bilgi tabanı

`abd-atif-dogrulama-rehberi.md` · `courtlistener-rehberi.md` · `us-legislation-rehberi.md`
