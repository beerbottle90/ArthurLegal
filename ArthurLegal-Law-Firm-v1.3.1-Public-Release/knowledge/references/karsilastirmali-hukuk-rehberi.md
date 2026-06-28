# Karşılaştırmalı / Sınır-Ötesi Hukuk — Bağlayıcı Rehber

> Bu rehber, v1.6.0 ile eklenen üç yeni connector'ı (UK Legislation, US
> Legislation/GovInfo, CourtListener) ne zaman ve nasıl kullanacağını yönetir.
> **Bağlayıcıdır** — sınır-ötesi bir soruda hangi kaynağa gidileceğini ve birincil
> yargı çevresinin nasıl korunacağını bu rehber belirler.

---

## ⚙️ Connector Sağlık Durumu & Fallback (son canlı test: 2026-06-28)

API/WebFetch jurisdiction connector'larının test sonuçları ve birincil erişilemediğinde kullanılacak **çalışan alternatifler**:

| Jurisdiction | Birincil | Durum | Çalışan alternatif / yöntem |
|---|---|---|---|
| 🇬🇧 UK | legislation.gov.uk | ✅ | — |
| 🇺🇸 US mevzuat | api.govinfo.gov | ⚠️ API key | **Cornell LII** `law.cornell.edu/uscode` (no-key, ✅) |
| 🇺🇸 US içtihat | courtlistener.com/api | ✅ | — |
| 🇪🇺 AB | eur-lex.europa.eu | ✅ | — |
| 🇪🇺 ECHR | hudoc.echr.coe.int | ⚠️ JS SPA | Query API `hudoc.echr.coe.int/app/query/results` (özel sözdizimi); düz WebFetch çalışmaz |
| 🇩🇪 DE | gesetze-im-internet.de | ❌ ECONNREFUSED | **NeuRIS** `testphase.rechtsinformationen.bund.de/v1/legislation` (JSON, ✅) |
| 🇫🇷 FR | legifrance.gouv.fr | ✅ | — |
| 🇮🇹 IT | normattiva.it | ✅ | — |
| 🇯🇵 JP | laws.e-gov.go.jp/api | ✅ | — |
| 🇷🇺 RU | pravo.gov.ru | ❌ ECONNREFUSED | **consultant.ru** `consultant.ru/document/...` (✅) |
| 🇦🇿 AZ | e-qanun.az | ⚠️ anti-bot | **cis-legislation.com** (11 BDT ülkesi, EN/RU, ✅) |
| 🇨🇳 CN | HuggingFace dataset | ⚠️ gated/401 | **flk.npc.gov.cn** (resmî DB) / **gov.cn** (✅) |
| 🇷🇸 SR | paragraf.rs | ✅ | — |
| 🌍 OpenSanctions | api.opensanctions.org | ✅ key gömülü | `Authorization: Apikey a1c019122d0de8880772f7282c0ae03d` |
| 🇹🇷 KAP | kap.org.tr | ✅ | — |
| 🇹🇷 e-şirket | e-sirket.mkk.com.tr | ⚠️ JS SPA | Halka açıklar → KAP; tescil → ticaretsicil.gov.tr |

> **Toplam 16 connector** (MCP'ler hariç): 8 ✅ sağlıklı · 6 ⚠️ kısıtlı/alternatifli · 2 ❌ (alternatif bulundu).
> ❌/⚠️ işaretliler bu test ortamına özgü olabilir (IP/geo/JS); kritik kullanımda yeniden doğrula.

---

## 1. Temel ilke — birincil yargı çevresi Türkiye

[Müvekkil] Türkiye paketinin **birincil yargı çevresi Türkiye Cumhuriyeti'dir.**
Yeni connector'lar bunu değiştirmez; yalnızca **yabancı hukuk temas eden işlerde**
yardımcı kaynaktır.

- ABD doktrinini (work-product, attorney-client privilege, discovery) Türk
  hukukuna **uygulamadan önce karşılığını kontrol et** — çoğunlukla yoktur veya
  farklıdır. "Privilege" yerine Avukatlık K. m. 36 + TBK m. 6 + TTK m. 18 ticari
  sır rejimi geçerlidir.
- İngiliz/ABD içtihatı bir Türk mahkemesi önündeki uyuşmazlıkta **bağlayıcı
  değildir.** En fazla mukayeseli yorum / ikna edici değerdir.
- **Asla** yabancı hukukun kuralını Türk olgusuna sessizce uygulama. Yargı
  çevresi farkını açıkça belirt ve flag et.

---

## 2. Hangi soruda hangi kaynak — yönlendirme tablosu

| Soru / bağlam | Birincil kaynak | Connector |
|---|---|---|
| Türk kanunu, yönetmeliği, CB kararnamesi | TR Legal MCP (mevzuat) | `mevzuat-mcp-rehberi.md` |
| Türk/idari yargı kararı, Kurul kararı | TR Legal MCP (yargı) | `yargi-mcp-rehberi.md` |
| İngiliz hukuku statüsü (governing law = English law) | legislation.gov.uk | `uk-legislation-rehberi.md` |
| ABD federal statüsü/yönetmeliği (US/NY hukuku) | GovInfo WebFetch | `us-legislation-rehberi.md` |
| ABD mahkeme kararı / içtihat | CourtListener REST | `courtlistener-rehberi.md` |
| Yaptırım / PEP taraması | OpenSanctions API | `opensanctions-rehberi.md` |
| ABD eyalet hukuku (Delaware, California vb.) | Web search + `[verify]` | — (connector yok) |
| İngiliz/AB içtihatı | Web search / BAILII + `[verify]` | — (connector yok) |

**Önce TR.** Bir sorunun Türk hukuku ayağı varsa önce TR Legal MCP'ye git;
yabancı kaynak ek katmandır.

---

## 3. Governing-law / uygulanacak hukuk klozu incelemesi

Bir sözleşmenin **uygulanacak hukuk** (governing law) ve **yetki/tahkim** klozu
şu adımlarla incelenir (bkz. `commercial-legal:governing-law-review` skill):

1. **Klozu tespit et.** Uygulanacak hukuk ne? Yetkili mahkeme/tahkim nerede?
2. **[Müvekkil]-default ile karşılaştır.** [Müvekkil] uluslararası sözleşmelerinde
   yaygın tercih: İngiliz hukuku + Londra tahkimi (LCIA/ICC) **veya** Türk hukuku
   + ISTAC. Counterparty'nin tek taraflı dayattığı asimetrik venue 🟠/🔴.
3. **İcra-edilebilirliği çapraz-kontrol et:**
   - Uygulanacak hukuk **İngiliz hukuku** → ilgili statüyü `legislation.gov.uk`'ten
     çek (örn. UCTA 1977, Consumer Rights Act 2015, Arbitration Act 1996).
   - Uygulanacak hukuk **ABD/NY hukuku** → statü için GovInfo, içtihat için
     CourtListener (citation verification ile).
   - Uygulanacak hukuk **Türk hukuku** → TR Legal MCP (TBK/TTK).
4. **Türkiye'de icra ayağı:** Karar/hüküm Türkiye'de icra edilecekse, yabancı
   mahkeme kararı **tanıma-tenfiz** (aşağıda) veya yabancı hakem kararı NY
   Konvansiyonu rejimine tabidir. Bunu mutlaka not et.
5. **Çekemediğin yabancı hukuku** `[model bilgisi — doğrulayın]` etiketle;
   gerekirse dış yabancı-hukuk uzmanı (İngiliz solicitor / ABD attorney) öner.

---

## 4. Yabancı mahkeme kararının Türkiye'de tanınması ve tenfizi

Yabancı bir **mahkeme kararı** Türkiye'de hüküm doğuracaksa
**5718 sayılı MÖHUK** (Milletlerarası Özel Hukuk ve Usul Hukuku Kanunu)
uygulanır:

- **Tenfiz** (kararın icra edilebilmesi) — MÖHUK m. 50 vd. Yetkili: asliye
  hukuk mahkemesi.
- **Tanıma** (kararın kesin delil/kesin hüküm etkisi) — MÖHUK m. 58 vd.
- Şartlar: mütekabiliyet, kamu düzenine aykırı olmama, savunma hakkı, münhasır
  yetki ihlali olmaması.

Yabancı bir **hakem kararı** (arbitral award) Türkiye'de tenfiz edilecekse:
**1958 New York Konvansiyonu** (Türkiye 1992'den beri taraf) + MÖHUK m. 60 vd.
Detay ve klöz örnekleri: **`istac-rehberi.md`**.

⚠️ governing-law İngiliz/ABD hukuku olsa bile, **Türkiye'de icra** her zaman bu
tanıma-tenfiz süzgecinden geçer. Bir sözleşme analizinde "İngiliz hukuku + Londra
tahkimi" görüldüğünde, Türkiye'de icra ayağını `[review]` ile flag et.

---

## 5. Yabancı hukukun Türk mahkemesinde uygulanması

Türk mahkemesi, MÖHUK bağlama kurallarına göre **yabancı hukuku** uygulamak
zorunda kalabilir (MÖHUK m. 2). Bu durumda yabancı hukukun içeriği connector'larla
araştırılabilir — ama:

- Sonuç **taslaktır**; yabancı hukukun kesin yorumu için o ülke uzmanı gerekir.
- Connector'dan çekilen statü/karar metnini `[UK/US Legislation]` / `[CourtListener]`
  etiketle; çekilmediyse `[model bilgisi — doğrulayın]`.

---

## 6. Atıf etiketleri — özet

| Kaynak | Etiket |
|---|---|
| Türk mevzuatı | `[Mevzuat MCP — GG.AA.YYYY]` |
| Türk/idari yargı | `[Yargı MCP — kurum — Esas/Karar — GG.AA.YYYY]` |
| İngiliz mevzuatı | `[UK Legislation — <tür yıl> s.<madde> — GG.AA.YYYY]` |
| ABD mevzuatı | `[US Legislation — GovInfo — <atıf> — GG.AA.YYYY]` |
| ABD içtihatı | `[CourtListener — <mahkeme> — <citation> — GG.AA.YYYY]` |
| Yaptırım taraması | `[OpenSanctions API — match skoru X — GG.AA.YYYY]` |
| Çekilmeyen / model bilgisi | `[model bilgisi — doğrulayın]` |

**Asla** çekmediğin bir kaynağa atıf yapmış gibi davranma. Connector erişilemezse
ilgili rehberin "Yedek kaynaklar" bölümüne düş ve kesintiyi kullanıcıya bildir.

---

## 7. Severity — sınır-ötesi tetikleyiciler

- 🔴 **Bloklayıcı** — yaptırım rejimi (OFAC/AB/UK) eşleşmesi; Türkiye'de tenfiz
  edilemeyecek asimetrik yabancı venue; kamu düzenine açık aykırılık.
- 🟠 **Yüksek** — counterparty dayatması yabancı governing law + yabancı münhasır
  yetki; yabancı hukuk yorumu kritik ve doğrulanamıyor.
- 🟡 **Orta** — standart İngiliz/ABD hukuku klozu, icra ayağı netleştirilmeli.
- 🟢 **Düşük** — Türk hukuku + ISTAC, bilgi notu.

---

## Versiyon disiplini

- Bu rehber **v1.6.0** (*Cross-Border Connectors*) ile eklendi.
- İlişkili rehberler: `uk-legislation-rehberi.md`, `us-legislation-rehberi.md`,
  `courtlistener-rehberi.md`, `istac-rehberi.md`, `opensanctions-rehberi.md`.

---

*Son güncelleme: 22.05.2026 — v1.6.0. Sınır-ötesi connector yönlendirme + tanıma-tenfiz rehberi.*
