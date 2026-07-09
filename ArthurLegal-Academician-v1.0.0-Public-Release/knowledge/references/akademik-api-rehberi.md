# Akademik API Rehberi (Anahtarsız, Ücretsiz)

> Bu paket **hiçbir API anahtarı gömmez.** Aşağıdaki kaynaklar WebFetch ile anahtarsız
> veya kullanıcının kendi ücretsiz anahtarıyla kullanılır.

---

## Neden önemli

Atıf doğrulama, bu paketin en kritik işlevidir. Şansımız şu: hukuk akademisyeninin
ihtiyaç duyduğu **künye ve DOI doğrulaması** için gereken kaynakların çoğu ücretsiz ve
programatiktir. Bu, sıfır-halüsinasyon kuralını **fiilen uygulanabilir** kılar.

---

## Kaynaklar

| Kaynak | Ne verir | Anahtar | Provenans etiketi |
|---|---|---|---|
| **Crossref** | DOI metadata: yazar, başlık, dergi, cilt, sayı, sayfa, yıl | Gerekmez (nezaket havuzu için e-posta önerilir) | `[Crossref — DOI — GG.AA.YYYY]` |
| **OpenAlex** | Eser/yazar/kurum metadata, atıf grafiği | Gerekmez | `[OpenAlex — ID — GG.AA.YYYY]` |
| **Semantic Scholar** | Makale metadata, atıf/referans grafiği | Gerekmez (anahtarla yüksek limit) | `[Semantic Scholar — ID — GG.AA.YYYY]` |
| **DOAJ** | Denetlenmiş açık erişim dergiler | Gerekmez | `[DOAJ — ISSN — GG.AA.YYYY]` |
| **ORCID** | Araştırmacı kimliği ve eser listesi | Public API ücretsiz | `[ORCID — iD — GG.AA.YYYY]` |
| **EUR-Lex** | AB hukuku (CELEX no ile) | Gerekmez | `[EUR-Lex — CELEX — GG.AA.YYYY]` |
| **HUDOC** | AİHM kararları (App. no ile) | Gerekmez | `[HUDOC — App. no — GG.AA.YYYY]` |

> **HUDOC ve CURIA'nın resmî belgelenmiş API durumu net değildir; doğrulanmalıdır.**
> AB hukukunda en sağlam programatik yol EUR-Lex'tir (CELEX / SPARQL-Cellar).

---

## Bağlı MCP sunucuları

| Sunucu | Kapsam |
|---|---|
| **TR Legal MCP** (Mevzuat + Yargı) | TR mevzuat + Yargıtay / Danıştay / AYM / Emsal |
| **CourtListener** | ABD federal + eyalet içtihadı, RECAP dockets (resmî MCP) |
| **Fedlex** | İsviçre federal mevzuatı |
| **OpenCaseLaw.ch** | İsviçre içtihadı + doktrin ↔ karar köprüsü, citation graph |

---

## Doğrulama iş akışı

```
1. Kaynak türünü belirle (makale / kitap / karar / mevzuat)
2. Uygun kaynağa git:
   - DOI varsa      → Crossref
   - DOI yoksa      → OpenAlex / Semantic Scholar (başlık + yazar araması)
   - TR karar/mevzuat → Yargı / Mevzuat MCP
   - AB / AİHM      → EUR-Lex / HUDOC
   - Kitap          → genellikle API yok → [MANUEL DOĞRULAYIN]
3. Künye alanlarını KARŞILAŞTIR (yıl, cilt, sayı, sayfa)
4. Sonucu işaretle: ✅ / ⚠️ / 🟠 / 🔴
5. Bulunamayan kaynak için ALTERNATİF ÖNERME — kaldırılmasını söyle
```

---

## Kısıtlar

- **Kitaplar ve monografiler** için güvenilir açık API yoktur. Türk hukuk doktrininin
  büyük kısmı buradadır. `[MANUEL DOĞRULAYIN]`
- **Crossref**, DOI'si olmayan eseri bilmez. Türk hukuk dergilerinin bir kısmı DOI kullanmaz.
- **OpenAlex/Semantic Scholar** metadata verir, **tam metin vermez**.
- **CourtListener** kullanım limitleri vardır; yoğun kullanım için üyelik gerekir.

---

## Kullanım kuralı

Bir kaynağı **çekemediysen, uydurma.** `[MANUEL DOĞRULAYIN]` veya
`[model bilgisi — DOĞRULAYIN]` etiketiyle işaretle ve kullanıcıya nasıl doğrulayacağını anlat.

---

## İlgili

`ticari-veritabani-rehberi.md` · `karsilastirmali-hukuk-rehberi.md` ·
`/atif-kaynak:atif-dogrulama`
