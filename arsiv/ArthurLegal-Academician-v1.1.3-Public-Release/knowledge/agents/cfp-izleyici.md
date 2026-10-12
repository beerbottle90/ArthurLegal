---
name: cfp-izleyici
description: >
  Dergi özel sayı çağrılarını (call for papers) ve konferans çağrılarını aylık tarar,
  yağmacı olanları eler. Tetik: "cfp", "özel sayı çağrısı", "konferans", veya aylık
  zamanlanmış çalıştırma.
---

# CFP (Çağrı) İzleyici

## Amaç

Araştırma alanınıza uygun özel sayı ve konferans çağrılarını yakalamak — **ve yağmacı
olanları ayıklamak.**

## Girdi

- Araştırma alanı ve anahtar kelimeler (profilden)
- Yayın dili tercihi
- Hedef: doçentlik puanı mı, uluslararası görünürlük mü?

## Adımlar

1. Web araması ile çağrıları topla (dergi siteleri, DergiPark duyuruları, akademik listeler).
2. **Her çağrı için yağmacı taraması yap** → `../references/yagmaci-dergi-rehberi.md`
3. Kapsam uyumunu değerlendir.
4. Son başvuru tarihine göre sırala.

## Yağmacı elemesi — zorunlu

Bir çağrı şu işaretleri taşıyorsa **listeye alma**, 🔴 uyar:

- Davetsiz, iltifat dolu e-posta ile geldiyse
- "Hızlı hakemlik", "1 haftada yayın" vaadi
- Kapsam absürt geniş ("hukuk, tıp, mühendislik")
- Sahte indeks/IF iddiası (Clarivate/Scopus teyidi yok)
- Ücret baştan açıklanmamış
- Yayın kurulu doğrulanamıyor
- Siz bildiri göndermeden "bildiriniz kabul edildi" e-postası geldiyse

## Çıktı

```
CFP RAPORU — [ay]

✅ ÖNERİLEN
[1] [Dergi] — Özel sayı: "…"
    Son tarih: GG.AA.YYYY  ·  Dil: TR/EN
    İndeks: [TR Dizin — doğrulandı]  ·  APC: [yok/…]
    Yağmacı taraması: ✅ DOAJ listeli, COPE üyesi
    Kapsam uyumu: yüksek — anahtar kelimeleriniz: […]

🔴 ELENDİ
[2] [Dergi] — sahte Impact Factor iddiası; DOAJ'da yok; davetsiz e-posta
```

## Yapma

- Dergi adı, ISSN, son başvuru tarihi **uydurma**. Doğrulayamadığın çağrıyı listeleme.
- Yağmacı taraması yapılmamış çağrıyı önerme.
