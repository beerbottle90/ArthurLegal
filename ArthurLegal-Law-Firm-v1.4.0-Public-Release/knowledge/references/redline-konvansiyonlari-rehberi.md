> **Durum:** ✅ Konvansiyon rehberi (erişim gerektirmez). `contract-drafting` eklentisinin (redline-contract, belge-turet, versiyon-karsilastir, tadil-protokol) ev redline & comment standardı. [Şirket/Büro adı]

# Redline & Comment Konvansiyonları — Pratik Rehber

## 1. Ortam gerçeği

- **Claude.ai Projects:** native Word tracked-changes (.docx OOXML) ÜRETİLEMEZ → **markdown redline görünümü** kullanılır.
- **Claude Code (VS Code):** `python-docx` ile gerçek `w:ins`/`w:del` (yazar/tarih) + `w:comment` üretilip `.docx` döndürülebilir.

## 2. Redline işaretleme (markdown)

| Eylem | Gösterim |
|---|---|
| Silinen | `~~silinen metin~~` |
| Eklenen | `**eklenen metin**` (veya `__altı çizili__`) |
| Alternatif (düz) | `[-silinen-]` / `[+eklenen+]` |
| Comment | `> 💬 [Av. — severity] gerekçe + fallback` |

## 3. Severity (tutarlı, üç eksen)
- 🔴 **Bloklayıcı** — imzalanmaz · 🟠 **Yüksek** — müzakere şart · 🟡 **Orta** — fix · 🟢 **Düşük** — not.
- Üst incelemenin 🔴'sı sessizce düşürülmez.

## 4. Sessiz fix vs comment
- **Sessiz:** yazım, atıf/numara, tutarlılık, tanım hizalama.
- **Comment ZORUNLU:** hukuki/ticari pozisyon değişikliği, risk dağılımı, tutar/süre/eşik, sorumluluk, fesih, hukuk/yetki.

## 5. Comment yapısı (her zaman fallback)
```
> 💬 [Av. — 🟠] Sorumluluk tavanı %50'ye çekilmiş; müvekkil için risk.
>     Tercih: tavan = sözleşme bedeli (kasıt/ağır kusur hariç tutulur).
>     Kabul edilmezse asgari: %75 + can/mal güvenliği istisnası.
```

## 6. Standart kloz seti (her enerji sözleşmesinde kontrol)
- Mücbir sebep + aşırı ifa güçlüğü (TBK m.136/138) — şebeke kesintisi, mevzuat değişikliği, kuraklık (HES)
- Sınırlı sorumluluk + cezai şart (TBK m.179-182; fahiş ceza tenkisi)
- Yaptırım & uyum (OFAC/AB/BM/OFSI + uluslararası finans kuruluşu yasaklı listeleri) — `yaptirim-tarama-rehberi.md`
- KVKK (6698) · gizlilik · fikri mülkiyet
- Uyuşmazlık & uygulanacak hukuk (Türk mah. vs ICC/LCIA) — `governing-law-review`
- EPDK lisans/pay devri ön-onayı (kontrol değişikliği)
- Ödeme/teminat (akreditif, teminat mektubu) · damga vergisi/gross-up
- Devir/temlik · tadil · fesih · süre/yenileme · rekabet klozu (`rekabet-hukuku-rehberi.md`)

## 7. Üst başlık / onay
```
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ([Baş Hukuk Müşaviri]) ONAYI ALINMADAN İMZALANMAZ
```
Her çıktı taslaktır; imza öncesi onay zinciri ([Baş Hukuk Müşaviri] → yüksek tutar/stratejik: [Genel Müdür] → SHA reserved matter: [Yönetim Kurulu] + kredi veren/ortak kuruluş onayı).

## Bağlantılı referanslar
`kanun-kisaltmalar.md` · `rekabet-hukuku-rehberi.md` · `yaptirim-tarama-rehberi.md` · `kvkk-m11-cevap-sablonu.md`

*Son güncelleme: 25.06.2026 — contract-drafting eklentisi için.*
