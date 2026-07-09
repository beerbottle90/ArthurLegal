---
name: ictihat-izleyici
description: >
  Akademisyenin araştırma alanındaki yeni Yargıtay / Danıştay / AYM kararlarını ve mevzuat
  değişikliklerini haftalık tarar. Tetik: "yeni içtihat", "alanımda ne çıktı", veya
  haftalık zamanlanmış çalıştırma.
---

# İçtihat ve Mevzuat İzleyici

## Amaç

Yayımlanmış bir makale, sonradan çıkan bir Yargıtay İçtihadı Birleştirme Kararı veya AYM
iptal kararıyla **geçersizleşebilir**. Yayın öncesi ve sonrası izleme şarttır.

## Girdi

`akademisyen-profili.md` içinden:
- Birincil ve ikincil araştırma alanı
- Anahtar kelimeler (5-10 terim)
- Karşılaştırmalı ilgi alanı (varsa)

## Adımlar

1. **Yargı MCP** üzerinden anahtar kelimelerle tara:
   - Yargıtay (daireler + Hukuk/Ceza Genel Kurulu + İçtihadı Birleştirme)
   - Danıştay (daireler + İDDK/VDDK)
   - AYM (norm denetimi + bireysel başvuru)
2. **Mevzuat MCP** üzerinden ilgili kanun/yönetmelik değişikliklerini tara.
3. Karşılaştırmalı ilgi varsa: EUR-Lex (CELEX), HUDOC (App. no), CourtListener,
   OpenCaseLaw.ch.
4. Her kaydı **verbatim** çek; esas/karar numarasını **asla** kendin kurma.
5. Etki değerlendir: hangi yayınınızı veya devam eden çalışmanızı etkiliyor?

## Severity

| | Anlam |
|---|---|
| 🔴 | Yayımlanmış çalışmanızın sonucunu geçersizleştirebilir (İBK, AYM iptali, kanun değişikliği) |
| 🟠 | Devam eden çalışmanızı doğrudan etkiler; metne işlenmeli |
| 🟡 | İlgili; dipnot değeri var |
| 🟢 | Bilgi notu |

## Çıktı

```
İÇTİHAT & MEVZUAT İZLEME — [tarih aralığı]
Anahtar kelimeler: [...]

🔴 [Yargı MCP — Yargıtay HGK — E. 2025/… K. 2026/… — GG.AA.YYYY]
   Özet: …
   Etkilediği çalışmanız: "…" (2024), s. 45'teki argüman
   Yapılacak: …

⚠️ Kapsam beyanı
Taranan: Yargı MCP (Yargıtay/Danıştay/AYM/Emsal), Mevzuat MCP
Taranmayan: Lexpera, Kazancı, Legalbank; basılı doktrin
Bu tarama eksiktir.
```

## Yapma

- Karar numarası, tarih veya daire adı **uydurma**. Çekemediysen rapor etme.
- Kararın sonucunu okumadan "şu yönde karar verdi" deme.
