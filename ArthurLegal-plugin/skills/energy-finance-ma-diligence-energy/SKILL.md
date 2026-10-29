---
name: energy-finance-ma-diligence-energy
description: >
  Enerji sektörü M&A durum tespiti — EPDK lisans, ÇED, yaptırım, vergi borcu,
  iş güvenliği sicil, rekabet eşiği ve SPK bildirim kontrolü içerir.
argument-hint: "[VDR index | due diligence request list | target company profile]"
---

# /ma-diligence-energy — Enerji M&A Due Diligence

## Adım 0 — Hedef şirket profili

| Unsur | Değer |
|---|---|
| Hedef şirket adı + tüzel kişilik | |
| Varlık türü | Elektrik üretim / doğal gaz / rafineri / terminal / karma |
| EPDK lisans türü | Üretim / Dağıtım / İletim / Depolama / İhracat-İthalat |
| Kapasite (MW / m³/yıl) | |
| Halka açık mı? (BIST) | |
| Tahmini işlem büyüklüğü (USD) | |

## Adım 1 — Düzenleyici & lisans tarama (KRİTİK)

**EPDK:**
- Lisans geçerliliği + süresi + kapasite kısıtları
- Lisans devri için EPDK izni gerekiyor mu? (genellikle gerekli)
- Ön bildirim süresi ve koşulları
- Aktif soruşturma / yaptırım prosedürü var mı?
- ArthurLegal MCP (`tr_`): `kurum_karari_ara (kurum="rekabet")` (enerji piyasası) çek

**ÇED ve çevre:**
- ÇED izni mevcut mu? Kapsamı yeterli mi?
- Emisyon, atık, izin şartları ihlali var mı?
- Seveso/Büyük Endüstriyel Kaza statüsü? (Rehber: `${CLAUDE_PLUGIN_ROOT}/references/seveso-buyuk-kaza-rehberi.md`)

**Rekabet:**
- İşlem rekabet eşiği aşıyor mu? (Rekabet Kurulundan İzin Alınması Gereken Birleşme ve Devralmalar Hakkında Tebliğ, Tebliğ No: 2010/4)
- Müvekkilin/alıcının halihazırdaki pazar payı + hedef = eşik aşımı?
- Avrupa Komisyonu AB Birleşme Tüzüğü (ECMR) — AB cirosu eşiği kontrolü

## Adım 2 — Yaptırım & KYC taraması

1. Hedef şirket ve gerçek yararlanan sahipleri OpenSanctions'da tara
2. Türk ortaklar: MKK teyit
3. Yabancı ortak: CAATSA m.232 riski değerlendirmesi (Rusya/CIS bağlantılı ise)
4. Yaptırım eşleşmesi → **Yönetici Ortak / Uyum görevlisine eskalasyon, işleme devam etme**

## Adım 3 — Vergi durum tespiti

- Vergi borcunun tespiti: Gelir İdaresi GİB sorgusu (ArthurLegal MCP (`tr_`): `kurum_karari_ara (kurum="gib")`)
- Aktif Danıştay vergi davaları
- Transfer pricing pozisyonu (intra-group bağlantı varsa özel dikkat)
- KDV iade alacakları — devralma sonrası talep edilebilir mi?
- Değer artış kazancı — satıcı tarafında vergi yükü → fiyata etkisi

## Adım 4 — İş güvenliği & iş hukuku

- İSGK 6331 iş güvenliği sicil — son 5 yıl kaza kaydı
- İş kazası + meslek hastalığı davaları — HMK süreçleri
- Sendika yapısı: TİS döngüsü, grev/lokavt tarihi
- Toplu işçi çıkarma geçmişi
- Yabancı çalışan varsa çalışma izni uyumu

## Adım 5 — Sözleşme portföyü & bağlı yükümlülükler

- Temel offtake / satış sözleşmeleri: change of control klozu var mı?
- EPC, O&M sözleşmeleri: devir halinde yeniden müzakere tetikler mi?
- Finansman sözleşmeleri: cross-default, prepayment riski
- Kilit personel tutma anlaşmaları
- Çevresel yükümlülükler (atık bertaraf, restorasyon)

## Adım 6 — Findings tablosu

| # | Bulgu | Kategori | Severity | Eylem |
|---|---|---|---|---|
| 1 | | Lisans / Vergi / Yaptırım / ISG / Sözleşme | 🔴/🟠/🟡/🟢 | |

## Çıktı şablonu

```markdown
GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU

# Enerji M&A Due Diligence — [Hedef şirket / tarih]

## ⚠️ Reviewer note
- Kapsam: [okunan belgeler, erişilemeyen alanlar]
- Bloklayıcı bulgu: [evet/hayır]
- [review] sayısı: N

## Bottom line

## Findings tablosu (özet)

## Düzenleyici & lisans (EPDK/ÇED/Rekabet)

## Yaptırım & KYC

## Vergi

## İş güvenliği & iş hukuku

## Sözleşme portföyü

## Önerilen adımlar
```

---

## Kaynak katmani — /legal-research (v1.4.0)

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur —
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| **bu plugin icin birincil kullanim** — PSA/JOA, cost recovery, profit split, stabilizasyon, DMO, decommissioning, yerel icerik benchmark'i | `/arthurlegal:legal-research-sozlesme-emsali` |
| AZ upstream/yer alti serveti rejimi, JV ve enerji mevzuati — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| Energy Charter Treaty, yatirim tahkimi, stabilizasyon klozu ogretisi — **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
