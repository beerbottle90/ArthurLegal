---
name: legal-research-kaynak-secimi
description: >
  Bir hukuki soru icin hangi kaynaga gidilecegini belirler. Kaynak hiyerarsisi,
  100 saniye arac limiti, gizlilik siniri ve "arac ne tutmuyor" kontrolu.
  Diger legal-research skill'lerinden once calistirilir.
user-invocable: true
---

# Kaynak Seçimi — Yönlendirme Matrisi

## Amaç

Yanlış kaynağa gitmek iki şekilde zarar verir: (1) 100 saniyelik araç limitine
takılıp **hiçbir şey** döndürmez, (2) ikincil bir kaynağı birincilmiş gibi
sunmaya yol açar. Bu skill, aramadan önce hangi araca gidileceğini belirler.

## 1. Kaynak hiyerarşisi — çelişki hâlinde sıralama

```
BİRİNCİL (mevzuat, içtihat)  >  EMSAL (imzalı sözleşme)  >  DOKTRİN (akademik)
```

- Bir sonucun **dayanağı** yalnız birincil kaynak olabilir.
- Bir emsal sözleşmedeki kloz, **bir tarafın müzakere sonucudur** — hukukun emri
  değil. "Piyasa böyle" demek, "hukuk böyle" demek değildir.
- Doktrin **argümandır, otorite değildir.** Mevzuatla çelişirse birincil kaynak
  üstündür — çelişkiyi **raporla**, makale lehine sessizce çözme.

## 2. Yönlendirme tablosu

| Soru | Araç | Rol | Rehber |
|---|---|---|---|
| TR kanun / yönetmelik / CBK metni | ArthurLegal MCP (`tr_`) (mevzuat) | BİRİNCİL | `mevzuat-mcp-rehberi.md` |
| TR yargı / Kurul kararı | ArthurLegal MCP (`tr_`) (yargı) | BİRİNCİL | `yargi-mcp-rehberi.md` |
| **AZ mevzuatı + yürürlük statüsü** | **e-qanun MCP** | **BİRİNCİL** | `eqanun-mcp-rehberi.md` |
| AZ Anayasa Mahkemesi kararı | WebFetch (constcourt / CODICES) | BİRİNCİL | `azerbaycan-hukuk-rehberi.md` |
| CH içtihat / Fedlex | OpenCaseLaw.ch MCP | BİRİNCİL | `switzerland-caselaw-rehberi.md` |
| US / IT mevzuatı | WebFetch | BİRİNCİL | ilgili `*-legislation-rehberi.md` |
| **İmzalı PSA/JOA emsali, kloz benchmark** | **ResourceContracts MCP** | **EMSAL** | `resourcecontracts-rehberi.md` |
| **Türk akademik doktrini** | **LexScholar MCP** (DergiPark, 19 dergi) | **İKİNCİL** | `lex-scholar-rehberi.md` |
| **Yabancı / karşılaştırmalı doktrin** | **LexScholar MCP** (10 indeks) | **İKİNCİL** | `lex-scholar-rehberi.md` |
| Yaptırım / PEP / UBO taraması | OpenSanctions | STOP-RULE | `yaptirim-tarama-rehberi.md` |
| Halka açık şirket açıklaması | KAP / e-ŞİRKET WebFetch | BİRİNCİL | `kap-esirket-webfetch-rehberi.md` |
| **DE mevzuatı + içtihat + yasama gerekçesi** | **de-eli MCP** | **BİRİNCİL** | `de-eli-mcp-rehberi.md` |
| **NL içtihadı (3,75 M ECLI) + mevzuatı** | **nl-rechtspraak MCP** | **BİRİNCİL** | `nl-rechtspraak-mcp-rehberi.md` |
| **PL mevzuatı + yürürlük statüsü** | **pl-sejm MCP** | **BİRİNCİL** | `pl-sejm-mcp-rehberi.md` |
| **AT mevzuatı + OGH/VwGH/VfGH içtihadı** | **at-ris MCP** | **BİRİNCİL** | `at-ris-mcp-rehberi.md` |
| **IE Act'leri (madde düzeyi)** | **ie-statutebook MCP** | **BİRİNCİL** | `ie-statutebook-mcp-rehberi.md` |
| **FI mevzuatı (fin + swe)** | **fi-finlex MCP** | **BİRİNCİL** | `fi-finlex-mcp-rehberi.md` |
| **ES konsolide mevzuatı** | **es-boe MCP** | **BİRİNCİL** | `es-boe-mcp-rehberi.md` |
| **ABD atıfı doğrulama (uydurma savunması)** | **CourtListener** | **ZORUNLU GEÇİŞ** | `abd-atif-dogrulama-rehberi.md` |
| **TR kanun maddesi doğrulama (teslim öncesi, belge gövdesi dâhil)** | **ArthurLegal MCP `tr_mevzuat_madde_getir`** | **ZORUNLU GEÇİŞ** | `mevzuat-mcp-rehberi.md` bölüm 9 |
| **Karşı taraf kimliği (LEI, ana ortak)** | **GLEIF** | **TARAMA ÖN ADIMI** | `gleif-rehberi.md` |
| UK mevzuatı (yapılandırılmış) | TNA resmî MCP | BİRİNCİL | `uk-legislation-mcp-rehberi.md` |
| AB tüzük/direktif/ABAD kimlikleme | EUR-Lex Cellar | BİRİNCİL | `eurlex-cellar-rehberi.md` |
| JP mevzuatı (as-of-date) | e-Gov API v2 | BİRİNCİL | `japan-egov-api-rehberi.md` |
| FR mevzuatı | DILA açık veri | BİRİNCİL | `france-dila-rehberi.md` |
| AİHM kararı | HUDOC | BİRİNCİL | `echr-hudoc-rehberi.md` |
| ABD şirket beyanı / imzalı sözleşme eki | SEC EDGAR | EMSAL | `edgar-rehberi.md` |
| Dış aktarım öncesi PII maskeleme | Presidio deseni | ZORUNLU GEÇİŞ | `pii-redaksiyon-rehberi.md` |

**Birden çok araç uygunsa: açıklaması en net olan EN DAR aracı seç.**

## 3. ⏱️ 100 saniye kuralı

Her araç çağrısı 100 saniyede iptal edilir ve iptal edilen çağrı **hiçbir şey
döndürmez.**

- Tek çağrıya "kanunu bul + öncü kararları özetle + resmî URL'leri topla"
  yaptırma. **Tek yargı çevresi, tek mesele, makul `limit`.**
- Tam metni her zaman `offset` / sayfa penceresiyle sayfala.
- İptal olursa **aynı sorguyu tekrarlama** — böl, sonra **hangi kısmın
  kapsanmadığını söyle.** Kısmi cevabı tam gibi sunma.
- **Özel araç > genel web arama.** Özel araçlar hukuk indekslerini doğrudan
  sorgular ve saniyeler içinde döner; genel web-arama sohbeti gezinmek zorundadır
  ve bu limite rutin olarak takılır. Ölçüm (25.07.2026): üç yargı çevresini
  kapsayan bir karşılaştırmalı soru özel araçtan **1 saniyenin altında** isabetli
  sonuç verdi; aynı soru genel web-arama sohbetinde **iki kez 100 saniyede iptal
  edildi**. Genel web aramasına yalnız hiçbir özel araç o kaynağı kapsamıyorsa git.

## 4. Araçların NE TUTMADIĞI — kapsam dürüstlüğü

| Araç | Tutmaz |
|---|---|
| e-qanun MCP | **AZ içtihadı** (yalnız mevzuat) |
| LexScholar MCP | Kanun/karar **resmî metni** (yalnız hukuk *hakkında* literatür) |
| ResourceContracts MCP | Mevzuat, içtihat, **gizli sözleşmeler** |
| ArthurLegal MCP (`tr_`) | Yabancı hukuk |

Güney Afrika, Almanya ve pek çok yabancı **birincil** kaynak için connector
**yoktur**. Bu durumda: "resmî metin çekilmedi" de, literatürü **şerh/yorum**
olarak atıfla — resmî kaynağa bakılmış gibi **ima etme**.

## 5. 🔒 Meslek sırrı sınırı — üç MCP de PUBLIC

e-qanun, LexScholar ve ResourceContracts **kamuya açık kaynak arama
araçlarıdır.** **Avukatlık Kanunu m. 36** (sır saklama yükümlülüğü) ve
`${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md` bu araçlar bakımından da geçerlidir.
Bunlara **gönderilmez**:

- Müvekkil adı, dosya numarası, dosya özeti
- Gizli sözleşme taslağı veya kloz metni
- Müzakere pozisyonu, ücret/eşik bilgisi
- Karşı taraf adının somut bir dosyayla birlikte geçtiği herhangi bir ifade
- Kişisel veri (KVKK)

Arama sorgusu **soyut hukuki kavram** olmalıdır ("stabilization clause cost
recovery cap", "mücbir sebep uyarlama"), **dosya alıntısı değil**.
Bir arama, karşı tarafa veya üçüncü kişiye vekâlet ilişkisini ele verebilecek
kadar belirginse **yapma** — kavramı soyutlaştır.

## 6. Çıktı

Bu skill tek başına bir iş ürünü üretmez. Çıktısı, çağıran skill'in formatına
girer ve şunu içerir:

- **Seçilen kaynak(lar)** + neden (hiyerarşideki yeri)
- **Kapsanmayan** ne varsa açıkça (hangi araç neyi tutmuyor)
- İptal/boş dönen çağrı olduysa **kapsam daralması notu**
