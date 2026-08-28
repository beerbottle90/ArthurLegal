# BAE Hukuku (onshore + DIFC/ADGM) — Kullanım Rehberi

> **Custom MCP server YOK ve resmi portallar agent'lara KAPALI.** uaelegislation.gov.ae,
> DIFC legal database ve ADGM (Thomson Reuters) siteleri WebFetch'e **403** döner
> (test 12.06.2026). Bu yargı çevresi **manuel-tarayıcı + kullanıcı-yapıştırma** modeliyle
> çalışır; agent çıktılarında `[model bilgisi — doğrulayın]` disiplini en katı burada uygulanır.
>
> **[ŞİRKET ADI] neden gerekli?** `company-profile.md` A.6: **Masdar** (Bilasuvar 445 MW +
> Neftchala 315 MW + Absheron-Garadagh OWP 240 MW + 2 GW JDA + 3,5 GW offshore MoU) ve
> **ACWA Power** ortaklıkları `[AR-2024]`. Yenilenebilir paket sözleşmelerinde BAE karşı
> taraf hukuku ve DIFC/ADGM seçimli uyuşmazlık çözümü gündeme gelir.

---

## Kritik kavramsal ayrım — üç hukuk düzeni

| Düzen | Hukuk ailesi | Mahkeme | Ne zaman karşına çıkar |
|-------|--------------|---------|------------------------|
| **Onshore BAE** | Kıta Avrupası/Mısır etkili medeni hukuk + şeriat tamamlayıcı | Yerel mahkemeler (AR) | Masdar/ACWA ana şirket sözleşmeleri, yerel operasyon |
| **DIFC** (Dubai) | **İngiliz common law** (kendi kanunları) | DIFC Courts (EN) | Finans/yatırım sözleşmelerinde nötr forum seçimi |
| **ADGM** (Abu Dabi) | **İngiliz common law — English law doğrudan uygulanır** (2015 Regulations) | ADGM Courts (EN) | Abu Dabi bağlantılı işlemler (Masdar = Abu Dabi!) |

⚠️ "BAE hukuku" klozu tek başına belirsizdir — onshore mu, hangi free zone mu, **mutlaka netleştir** 🟠.

## Kaynak haritası

| Kaynak | İçerik | Durum (12.06.2026) |
|--------|--------|--------------------|
| uaelegislation.gov.ae | Resmi federal mevzuat (EN çevirili) | ❌ 403 — tarayıcı manuel |
| difc.ae → Legal Database | DIFC kanun/regülasyonları (EN) | ❌ 403 — tarayıcı manuel |
| en.adgm.thomsonreuters.com | ADGM mevzuat külliyatı (EN) | ❌ 403 — tarayıcı manuel |
| elaws.moj.gov.ae | Adalet Bakanlığı e-laws | ❌ ECONNREFUSED |
| WIPO Lex → UAE profili | Temel kanun çevirileri | ✅ giriş çalışır — kapsam sınırlı |
| Kullanıcı yapıştırması | Her şey | ✅ önerilen birincil yol |

**Çalışma kuralı:** BAE hukuku sorusunda önce kullanıcıdan ilgili kanun/kloz metnini iste;
yapıştırılamıyorsa analizini `[model bilgisi — doğrulayın]` etiketiyle ver ve doğrulama
adımını (hangi portal, hangi kanun no) açıkça tarif et.

## [ŞİRKET ADI]-kritik BAE mevzuatı (model bilgisi — her kullanımda doğrulat)

| Konu | Düzenleme | Not |
|------|-----------|-----|
| Medeni Kanun (onshore) | Federal Law No. 5/1985 (Civil Transactions) | sözleşme genel rejimi; faiz sınırlamaları |
| Şirketler | Federal Decree-Law No. 32/2021 (Commercial Companies) | onshore JV kurulumu |
| Tahkim | Federal Decree-Law No. 6/2018 (UNCITRAL bazlı) | onshore tahkim; NY Konv. tarafı ✅ |
| **DIAC reorganizasyonu** | Dubai Decree No. 34/2021 | **DIFC-LCIA lağvedildi** → davalar DIAC'a; eski DIFC-LCIA klozlarının akıbeti tartışmalı 🟠 `[review]` |
| ADGM uygulama | ADGM English Law Regulations 2015 | İngiliz hukuku + equity doğrudan uygulanır |
| Yenilenebilir/enerji | Emirlik bazlı (DEWA/EWEC ihale rejimleri) | Masdar projeleri AZ'de — BAE tarafı kurumsal/finansman katmanı |

## Tahkim klozu pratik kontrolü (Masdar/ACWA paketlerinde)

1. Kurum: ICC / LCIA / DIAC / ADGM Arbitration Centre — **DIFC-LCIA yazıyorsa 🟠 flag** (Decree 34/2021 sonrası geçerlilik sorusu)
2. Seat: DIFC veya ADGM seçimi → common law usul + EN dil avantajı; onshore seat → AR dil riski
3. İcra: BAE NY Konvansiyonu tarafı; DIFC "conduit" içtihadı `[model bilgisi — doğrulayın]`
4. Ev entitesi icra ayağı → `/commercial-legal:governing-law-review` Adım 5

## Atıf formatı

- Fiilen çekilemediği için varsayılan: `[model bilgisi — doğrulayın — {kanun no/yıl}]`
- Kullanıcı metin yapıştırdıysa: `[AE Mevzuat — kullanıcı sağladı — {kanun} — GG.AA.YYYY]`
- WIPO Lex'ten çekildiyse: `[AE Mevzuat — WIPO Lex — {kanun} — GG.AA.YYYY]`

---

*Test: 12.06.2026 — resmi portallar agent erişimine kapalı (403/ECONNREFUSED); rehber
manuel-doğrulama modeliyle yazıldı. Sürüm: v1.11.0.*
