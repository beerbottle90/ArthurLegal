# Orta Asya Hukuku (Kazakistan + Özbekistan) — Kullanım Rehberi

> **Custom MCP server YOK.** Özbekistan için **lex.uz** (resmi, direkt belge URL'leri
> WebFetch ✅); Kazakistan için resmi **adilet.zan.kz** WebFetch'te TLS sertifika hatası
> verir ⚠️ — tarayıcıda çalışır, agent için fallback aşağıda.
>
> **Durum (test 12.06.2026):** UZ lex.uz `/docs/{id}` ✅ sunucu-render · UZ arama SPA ⚠️ ·
> KZ adilet ❌ (WebFetch TLS) · KZ prg.kz (Paragraf) kısmi ücretsiz ⚠️ paywall
>
> **[Müvekkil] neden gerekli?** `firm-profile.md` A.5: **KazMunayGaz JSC** ile Roadmap
> (22.06.2023) + COP29 Stratejik Dekarbonizasyon Anlaşması; **Uzbekneftegaz JSC** ile
> Roadmap + **Karakalpak yatırım bloku anlaşması** `[AR-2024]`. Orta Asya karşı tarafları
> ile JV/arama anlaşmalarında yerel hukuk katmanı bu rehberden kurulur.

---

## Kaynak haritası

| Kaynak | Ülke | Tür | Durum | Dil |
|--------|------|-----|-------|-----|
| lex.uz/docs/{id} | 🇺🇿 | Resmi ulusal mevzuat DB (Adalet Bak.) | ✅ direkt URL sunucu-render | UZ/RU/EN (belgeye göre) |
| lex.uz arama | 🇺🇿 | Arama arayüzü | ⚠️ SPA — WebFetch'te boş kabuk | 4 dil |
| adilet.zan.kz | 🇰🇿 | Resmi hukuki bilgi sistemi | ❌ WebFetch TLS hatası — tarayıcı manuel | KZ/RU (+kısmi EN) |
| prg.kz (İS Paragraf) | 🇰🇿 | Ticari DB (18,6M belge) | ⚠️ kısmi ücretsiz (Anayasa + temel kodlar) | RU/KZ |
| aifc.kz / AIFC Court | 🇰🇿 | AIFC common-law rejimi + mahkeme | `[doğrulayın]` | EN |
| WIPO Lex (wipo.int/wipolex/en/members) | her ikisi | IP + temel kanun çevirileri | ✅ ana giriş | EN |

---

## 1. Özbekistan — lex.uz (BİRİNCİL ✅)

**Erişim pattern'ı:** Arama SPA olduğundan iki adımlı çalış:
1. Google/Bing ile `site:lex.uz [kanun adı RU/UZ]` → belge ID'sini bul
2. `https://lex.uz/docs/{id}` direkt WebFetch — tam metin sunucu-render gelir ✅
   (dil varyantı: `https://lex.uz/ru/docs/{id}` · `https://lex.uz/en/docs/{id}` çeviri varsa)

```
WebFetch:
  URL: https://lex.uz/ru/docs/{id}
  prompt: "[madde no] maddesinin tam metnini çıkar; yürürlük durumunu belirt"
```

Doğrulanmış örnek: Anayasa = `lex.uz/docs/20596` ✅ (08.12.1992 tabanlı, versiyon geçmişli).

**[Müvekkil]-kritik UZ mevzuatı:**

| Konu | Kanun | Not |
|------|-------|-----|
| **PSA rejimi** | "Mahsulot taqsimotiga oid bitimlar to'g'risida" / «О соглашениях о разделе продукции» (2001) | Karakalpak bloku anlaşmasının zemini `[doğrulayın — lex.uz ID]` |
| Yer altı kaynakları | Yer osti boyliklari to'g'risida (Subsoil K.) | arama/üretim lisansları |
| Yatırım | Investitsiyalar va investitsiya faoliyati (ZRU-598, 2019) | yatırımcı korumaları, stabilizasyon |
| Döviz | Valyuta tartibga solish | repatriasyon/konvertibilite |
| Tahkim | UNCITRAL model bazlı tahkim kanunu + NY Konv. tarafı ✅ | TIAC (Taşkent) kurumsal seçenek |

## 2. Kazakistan — adilet.zan.kz (resmi) + fallback'ler

**adilet.zan.kz:** Resmi ve ücretsiz; ancak **WebFetch TLS zincir hatası** verir (12.06.2026) —
agent çekemez, kullanıcı tarayıcıdan açıp metni yapıştırmalı. URL pattern:
`https://adilet.zan.kz/rus/docs/{kod}` (örn. `K1700000125` = Subsoil Code 2017).

**Fallback sırası:**
1. Kullanıcıdan adilet metnini yapıştırmasını iste (önerilen)
2. prg.kz ücretsiz bölümü (Anayasa + temel kodlar; ötesi paywall ⚠️)
3. Model bilgisi → `[model bilgisi — doğrulayın]` etiketi zorunlu

**[Müvekkil]-kritik KZ mevzuatı:**

| Konu | Kanun | Not |
|------|-------|-----|
| **Yer altı kodu** | "О недрах и недропользовании" Kodeksi (No. 125-VI, 27.12.2017) | arama/üretim sözleşme rejimi (eski PSA'lar grandfathered) |
| Girişimcilik Kodu | Predprinimatelskiy kodeks (2015) | yatırım sözleşmeleri, devlet destekleri |
| Medeni Kanun | Grajdanskiy kodeks | sözleşme genel hükümleri |
| Yerel içerik | Subsoil Code içinde local content yükümlülükleri | KazMunayGaz işbirliklerinde kritik |
| **AIFC rejimi** | AIFC Constitutional Statute (2015) | Astana'da **İngiliz common law adacığı**: AIFC Court + IAC tahkim — KZ taraflı sözleşmede dispute resolution alternatifi `[doğrulayın]` |

## 3. Atıf formatları

- `[UZ Mevzuat — lex.uz/docs/{id} — {kanun adı} — GG.AA.YYYY]` (fiilen çekildiyse)
- `[KZ Mevzuat — adilet.zan.kz — {kanun} — manuel/kullanıcı metni — GG.AA.YYYY]`
- Çekilemeyen her şey → `[model bilgisi — doğrulayın]`

## 4. Pratik notlar

- Her iki ülke **NY Konvansiyonu tarafı**; tenfiz ayağı için `/commercial-legal:governing-law-review` Adım 5.
- KazMunayGaz/Uzbekneftegaz **devlet şirketleri** — sözleşmede sovereign immunity feragati ve
  devlet onay şartlarını kontrol et (PSA/JV işlerinde `/energy-finance:psa-joa-review`).
- Yaptırım taraması: her iki ülke karşı tarafında RU bağlantılı ortak/UBO riski yüksek —
  OpenSanctions zorunlu (`yaptirim-tarama-rehberi.md`).

---

*Test: 12.06.2026 — lex.uz/docs ✅ · lex.uz arama SPA ⚠️ · adilet.zan.kz WebFetch TLS ❌ ·
prg.kz kısmi ⚠️. Sürüm: v1.11.0.*
