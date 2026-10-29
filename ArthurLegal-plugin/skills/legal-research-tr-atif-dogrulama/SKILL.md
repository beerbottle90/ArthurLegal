---
name: legal-research-tr-atif-dogrulama
description: >
  Taslakta gecen her Turk yargi karari kunyesini (Yargitay, Danistay, BAM, AYM,
  Uyusmazlik Mahkemesi) sunulmadan ONCE ArthurLegal tr_ araclariyla dogrular.
  Bulunamayan kunye "dogrulanmadi" diye isaretlenir; tamamlanmaz, tahmin edilmez.
user-invocable: true
---

# Türk Karar Künyesi Doğrulama (uydurma künye savunması)

## Ne zaman kullanılır

Taslak cevap, not, dilekçe veya sözleşme gövdesi **herhangi bir** Türk yargı kararı künyesi içeriyorsa:
"Yargıtay … HD, E. …, K. …, T. …", "HGK'nın … tarihli … sayılı kararı", "AYM, B. No: …". Kullanıcı, müvekkil veya
karşı taraf bir künye gönderip "bu karar gerçek mi?" diye sorduğunda da.

**Bu bir son kontrol değil, bir geçiştir.** Doğrulanmamış künye otorite olarak sunulmaz.

## Yöntem

Ayrıntı ve denenmiş araç davranışları: `${CLAUDE_PLUGIN_ROOT}/references/tr-atif-dogrulama-rehberi.md`.

1. Taslaktaki bütün künyeleri listele: mahkeme veya daire, E., K., tarih (AYM bireysel başvuruda B. No).
2. Her künye için:
   - **Yargıtay, Danıştay, BAM:** `tr_ictihat_ara(query=<esas numarasının yalnız sıra kısmı>, chamber=<daire kodu>,
     date_from=<tarih>, date_to=<tarih>)`. Sorguda "/" kullanılamaz. BAM'da `courts=["ISTINAFHUKUK"]` ve dairenin tam adı.
   - **AYM bireysel başvuru:** `tr_aym_ara(kind="bireysel", query=<B. No>)`.
   - **AYM norm denetimi:** numarayla aranamaz; `tr_aym_ara(kind="norm", query=<kanun + madde>)`.
   - **Uyuşmazlık Mahkemesi:** `tr_uyusmazlik_ara(query=<E. no>, scope="EsasNo")`.
3. Esas, karar ve tarih **üçü birden** aynı kayıtta eşleşiyorsa → DOĞRULANDI; yanıttaki `citation` birebir yazılır.
4. Eşleşmiyorsa rehberdeki genişletme adımlarını dene (tarih aralığı, karar numarası, daire süzgeci). Yine tutmazsa →
   DOĞRULANMADI.
5. Kayıtta farklı bir künye çıktıysa kendiliğinden düzeltme; avukata "verilen künye bulunamadı; kayıttaki künye şu"
   diye göster.

| Durum | Yapılacak |
|---|---|
| Üç unsur aynı kayıtta | `citation` birebir: `[ArthurLegal TR — citation — GG.AA.YYYY çekim]` |
| Esas bulundu ama karar no veya tarih farklı | **DOĞRULANMADI**; kayıttaki künyeyi avukata göster |
| Hiç kayıt yok | **DOĞRULANMADI**; "bulunamadı", "karar yok" demek değildir |
| Araç hatası veya hız sınırı | Bekle, yeniden dene; doğrulamayı **atlama** |

## Sert kurallar

- Doğrulanamayan künye metne yazılmaz; yazılacaksa hemen ardından `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>` satırıyla ve İnceleme notunda adıyla.
- Yalnız esas numarasının bulunması doğrulama değildir.
- Künyenin doğru olması, kararın iddia edilen şeyi söylediği anlamına gelmez. İçerik `tr_ictihat_getir` ile okunmadan
  karara hüküm veya gerekçe yüklenmez.
- Teslimden önce İnceleme notuna tek cümle: "İçtihat kontrolü: …" (kaç künye bulundu, hangileri doğrulanmadı).

## Çıktı

```markdown
İçtihat kontrolü:
| # | Verilen künye | Sonuç | Kayıttaki künye (citation) |
|---|---|---|---|
| 1 | … | ✓ DOĞRULANDI | … |
| 2 | … | ✗ DOĞRULANMADI | kayıtta aynı esas, tarih farklı: … |
```

## Bilgi tabanı

`tr-atif-dogrulama-rehberi.md` · `yargi-mcp-rehberi.md`
