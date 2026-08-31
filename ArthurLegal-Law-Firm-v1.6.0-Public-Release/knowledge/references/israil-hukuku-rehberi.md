# İsrail Hukuku — Kullanım Rehberi

> **Custom MCP server YOK; resmi kaynak erişimi sınırlı.** gov.il agent'lara 403 döner;
> Knesset EN sitesi WebFetch'te boş içerik verir; Nevo ücretli (test 12.06.2026).
> Çalışma modeli: **kullanıcı-yapıştırma birincil + WIPO Lex yardımcı** +
> `[model bilgisi — doğrulayın]` disiplini.
>
> **[Müvekkil] neden gerekli?** `firm-profile.md` A.5: **NewMed Energy + bp ile İsrail
> offshore ortak arama programı** — detaylar anlaşıldı, yüklenici listesi hazırlandı
> `[AR-2024]`. Offshore petrol/gaz lisans rejimi, ihracat kısıtları ve İsrail sözleşme
> hukuku katmanı bu dosyalarda gündeme gelir.

---

## Kaynak haritası

| Kaynak | İçerik | Durum (12.06.2026) |
|--------|--------|--------------------|
| gov.il (Enerji Bak. dahil) | Resmi kurum sayfaları, lisans rejimi | ❌ 403 — tarayıcı manuel |
| Knesset ulusal mevzuat DB | Tüm İsrail kanunları (İbranice) | ⚠️ EN sayfa boş içerik; HE arayüz tarayıcıda |
| Nevo (nevo.co.il) | İçtihat + mevzuat (fiili standart DB) | ⚠️ ücretli abonelik |
| WIPO Lex → IL profili | Temel kanunların EN çevirileri | ✅ giriş çalışır — kapsam sınırlı |
| Kullanıcı yapıştırması | Her şey | ✅ önerilen birincil yol |

**Dil gerçeği:** Bağlayıcı metin İbranicedir; resmi İngilizce çeviri istisnadır. EN çeviri
kullanıldığında "non-binding translation" notu düş.

## [Müvekkil]-kritik İsrail mevzuatı (model bilgisi — her kullanımda doğrulat)

| Konu | Düzenleme | Not |
|------|-----------|-----|
| **Petrol rejimi** | Petroleum Law 5712-1952 + Petroleum Regulations | arama lisansı (license) → keşif sonrası lease; Petroleum Commissioner (Enerji Bak.) onayları |
| Offshore politika | Tzemach Komitesi kararları + ihracat kotaları (hükümet kararları) | üretimin iç pazar payı yükümlülüğü — offtake planını etkiler 🟠 |
| Sözleşme genel | Contracts Law (General Part) 5733-1973 + (Remedies) 5731-1970 | common law etkili karma sistem |
| Şirketler | Companies Law 5759-1999 | JV/SPV kurulumu |
| Tahkim | Arbitration Law 5728-1968; NY Konv. tarafı ✅ | uluslararası işlemde yabancı seat yaygın |
| Doğal kaynak vergisi | Petroleum Profits Taxation Law 5771-2011 ("Sheshinski vergisi") | windfall/levy katmanı — ekonomik modellemede kritik 🟠 |
| Yabancı yatırım taraması | Hükümet içi danışma komitesi mekanizması | enerji altyapısında devlet onay katmanı `[doğrulayın]` |

## Offshore arama programı pratik kontrol listesi (NewMed + bp dosyaları)

1. **Lisans zinciri:** license → lease dönüşüm şartları ve süreleri; Commissioner onayı
   gereken devirler (farm-in/out)
2. **Ortaklık yapısı:** İsrail JOA pratiği AIPN modeline yakındır — `/energy-finance:psa-joa-review`
   JOA adımını uygula (İsrail'de PSA değil **vergi-royalty rejimi** geçerli; profit split yok)
3. **İhracat izni:** kota/iç pazar yükümlülüğü — Türkiye/AB'ye gaz ihracat senaryosunda 🟠
4. **Güvenlik/jeopolitik FM:** bölgesel çatışma force majeure klozu — sigorta (war risk) katmanı
5. **Yaptırım/uyum:** Arap Ligi boykot mevzuatı ile etkileşim — çok-uluslu konsorsiyumda
   ortakların kendi rejimleri çelişebilir 🟠 grup uyum birimi görüşü
6. İcra ayağı → `/commercial-legal:governing-law-review` Adım 5 (ev = aktif entite)

## Atıf formatı

- Varsayılan: `[model bilgisi — doğrulayın — {kanun adı + yıl}]`
- Kullanıcı yapıştırdıysa: `[IL Mevzuat — kullanıcı sağladı — {kanun} — GG.AA.YYYY]`
- WIPO Lex çevirisinden: `[IL Mevzuat — WIPO Lex (EN çeviri, bağlayıcı değil) — {kanun} — GG.AA.YYYY]`

---

*Test: 12.06.2026 — gov.il 403 · Knesset EN boş · Nevo ücretli · WIPO Lex girişi ✅.
Sürüm: v1.11.0.*
