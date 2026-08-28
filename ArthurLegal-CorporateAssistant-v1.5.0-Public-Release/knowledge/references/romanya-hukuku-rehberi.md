# Romanya Hukuku — Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK — gerek de yok:** resmi **legislatie.just.ro** (Adalet Bakanlığı)
> sunucu-render çalışır, direkt belge URL'leri ve **konsolide metinler** WebFetch ile
> çekilebilir ✅ (test 12.06.2026). AB katmanı EUR-Lex'ten (`eu-legislation-rehberi.md`).
>
> **[ŞİRKET ADI] neden gerekli?** `company-profile.md` B.4: **[ŞİRKET ADI] Romania** akaryakıt perakende
> iştiraki (grupta öz-üretim yenilenebilir raporlayan tek iştirak `[AR-2024 §XVI]`);
> A.4: metanol/üre ihracatının ana pazarlarından biri RO. Perakende regülasyonu, akaryakıt
> piyasası ve emtia satış uyuşmazlıkları RO hukukuna dokunur.

---

## Kaynak haritası

| Kaynak | Tür | Durum | Dil |
|--------|-----|-------|-----|
| legislatie.just.ro | Resmi mevzuat portalı (N-Lex üyesi) | ✅✅ sunucu-render + direkt URL + konsolide | RO |
| EUR-Lex | AB-türevli RO uyum mevzuatı | ✅ | RO + EN |
| anre.ro | Enerji düzenleyici (ANRE) kararları | `[doğrulayın]` | RO (+kısmi EN) |
| portal.just.ro | Mahkeme dosya sorgu | `[doğrulayın]` | RO |

## 1. legislatie.just.ro — BİRİNCİL ✅

**URL pattern'ları:**
- Belge: `https://legislatie.just.ro/Public/DetaliiDocument/{id}` — konsolide sürüm
  linkleri tarihli olarak sunulur (en güncel konsolidasyonu seç)
- Arama formu sunucu-taraflı çalışır (tip + tarih + kurum filtreleri)

**Doğrulanmış örnekler (12.06.2026):**
- Yeni Medeni Kanun (Legea 287/2009) = `DetaliiDocument/109884` ✅ (konsolide 19.12.2025 sürümü görüldü)
- Yeni Ceza Kanunu = `DetaliiDocument/109855` ✅

```
WebFetch:
  URL: https://legislatie.just.ro/Public/DetaliiDocument/{id}
  prompt: "[madde no] maddesinin konsolide metnini çıkar; hangi tarihli konsolidasyon olduğunu belirt"
```

ID bilinmiyorsa: Google `site:legislatie.just.ro {kanun adı/no}` → DetaliiDocument linki.

## 2. [ŞİRKET ADI]-kritik RO mevzuatı

| Konu | Kanun | [ŞİRKET ADI] bağlantısı |
|------|-------|------------------|
| Medeni Kanun | Legea 287/2009 (Noul Cod Civil) — id 109884 ✅ | sözleşme genel rejimi (tedarik/satış) |
| **Enerji & gaz piyasası** | Legea 123/2012 (energiei electrice și a gazelor naturale) | ANRE lisansları, perakende yükümlülükleri |
| Petrol | Legea petrolului 238/2004 | depolama/dağıtım imtiyazları |
| Akaryakıt stok | AB 2009/119 uyumu (zorunlu stok) | perakende iştiraki stok yükümlülüğü |
| Rekabet | Legea concurenței 21/1996 | akaryakıt fiyatlama soruşturma pratiği 🟠 |
| Tüketici | OG 21/1992 + AB tüketici müktesebatı | istasyon perakende tarafı |
| Şirketler | Legea societăților 31/1990 | RO iştirak yönetişimi |

**AB üyeliği notu:** RO tam AB üyesi — tüketici, rekabet, enerji ve yaptırım katmanlarında
**önce EUR-Lex** (tüzükler doğrudan uygulanır), ulusal aktarım için legislatie.just.ro.
AB yaptırım tüzükleri (833/2014 vb.) RO operasyonunda doğrudan bağlayıcıdır.

## 3. ANRE — enerji düzenleyicisi

Autoritatea Națională de Reglementare în Domeniul Energiei — lisans kararları, tarife
metodolojileri, piyasa izleme. `https://anre.ro` `[doğrulayın — agent erişimi test edilmedi]`.
Perakende lisans şartı sorularında ANRE kararı + Legea 123/2012 maddesi birlikte okunur.

## 4. Atıf formatları

- `[RO Mevzuat — legislatie.just.ro/{id} — {kanun no/yıl + madde} — GG.AA.YYYY]`
- AB katmanı → `[EU Legislation — CELEX:{no} — GG.AA.YYYY]` (mevcut kural)
- ANRE kararı → `[RO Düzenleme — ANRE — {karar no} — GG.AA.YYYY]`
- Çekilemeyen → `[model bilgisi — doğrulayın]`

## 5. Pratik notlar

- Konsolide metin tarihini HER atıfta belirt — portal birden çok konsolidasyon sunar.
- RO mahkeme kararları için merkezi ücretsiz tam-metin DB sınırlıdır (ReJust/portal.just.ro
  `[doğrulayın]`); uyuşmazlık analizinde yerel vekil teyidi şart.
- NY Konvansiyonu + AB üyesi: tenfiz ayağı görece öngörülebilir →
  `/commercial-legal:governing-law-review` Adım 5.

---

*Test: 12.06.2026 — legislatie.just.ro ana sayfa + DetaliiDocument/109884 ✅✅.
Sürüm: v1.11.0.*
