---
name: contract-drafting-redline-contract
description: >
  Yüklenen sözleşmeyi inceleme bulgularına göre REDLINE'la — değişiklikleri belgeye
  ekleme/silme + comment olarak işler, 3 çıktı formundan birinde teslim eder.
  commercial-legal inceleme akışıyla bütünleşir (vendor/NDA/SaaS/governing-law).
  Claude.ai Projects: markdown redline görünümü; Claude Code: gerçek .docx tracked-changes.
  TBK/TTK + standart (EPC/PPA/vendor/SHA) fallback pozisyonları.
user-invocable: true
---

# Sözleşme Redline (incele → belgeye uygula)

> Bu skill **bulguları belgeye uygular**. Henüz inceleme yapılmadıysa önce `/arthurlegal:commercial-legal-review` (veya ilgili review skill'i) çalıştır; sonra bulguları buraya getir. Her çıktı **TASLAK** — Baş Hukuk Müşaviri + dış vekil onayı ile imzalanır.

## ADIM 0 — Girdi & ortam & form

1. **Belge var mı?** Kullanıcı sözleşme metnini yapıştırsın/yüklesin. "Okuma kapsamı"nı belirt; tamamını okumadıysan söyle.
2. **Bizim kağıt mı, karşı tarafın kağıdı mı?** (redline yönü/agresifliği değişir)
3. **Ortam:** Claude.ai Projects → **markdown redline**; Claude Code → **gerçek .docx tracked-changes** (python-docx) opsiyonu.
4. **Çıktı formu (sor):**
   - (a) **Redline görünümü** — madde içinde ~~silinen~~ / **eklenen** + comment dipnotları
   - (b) **Temiz revize + değişiklik/comment listesi**
   - (c) **Yapılandırılmış tablo** — `madde | mevcut | önerilen | gerekçe | severity`

## ADIM 1 — Bulguları topla / üret

Inceleme bulgusu varsa al; yoksa playbook'a göre çıkar (sözleşme tipini tespit et → `references/` + `commercial-legal` profili + `firm-profile.md` standart pozisyonları). Her bulgu için:
- **Sorun** (kloz + neden) · **Severity** (🔴🟠🟡🟢) · **Önerilen redline** (somut metin) · **Fallback** ("tercih X; kabul edilmezse asgari Y") · **Hukuki dayanak** (çekilmiş madde, `[ArthurLegal TR — kanun m. X — GG.AA.YYYY]`; önerilen redline metnine yazılan madde numarası da belge-turet ADIM 2'deki doğrulama kapısından geçer, çekilemiyorsa redline numarasız yazılır).

**Standart kontrol listesi (enerji sözleşmesi):**
- Mücbir sebep + aşırı ifa güçlüğü (TBK m.136/138) — şebeke kısıtı, mevzuat değişikliği, kuraklık (HES)
- Sınırlı sorumluluk / cezai şart (TBK m.179-182 — fahiş ceza tenkisi)
- Yaptırım & uyum klozu (OFAC/AB/BM/OFSI + **uluslararası finans kuruluşu dışlama listesi**) — `${CLAUDE_PLUGIN_ROOT}/references/yaptirim-tarama-rehberi.md`
- Uyuşmazlık & uygulanacak hukuk (Türk mah. vs ICC/LCIA) — `/arthurlegal:commercial-legal-governing-law-review`
- **EPDK lisans/pay devri ön-onayı** (6446) — kontrol değişikliği klozu
- KVKK (6698) veri işleme/aktarım · gizlilik · fikri mülkiyet
- Damga vergisi / vergi gross-up · ödeme/teminat (akreditif, teminat mektubu)
- Devir/temlik · değişiklik (tadil) · fesih · süre/yenileme

## ADIM 2 — Redline'ı üret (seçilen form)

**Form (a) — Redline görünümü (Projects varsayılanı):**
```markdown
**Madde 12.3 (Mücbir Sebep)**
Taraflar, ~~savaş, grev ve doğal afet~~ **mücbir sebep hâllerinde (TBK m.136 anlamında, şebeke
operatörü kaynaklı kesinti ve mevzuat değişikliği dâhil)** edimlerini ~~7 gün~~ **30 gün** içinde
yerine getiremezse...
> 💬 [Av. — 🟠] Mücbir sebep tanımı dar; şirket için şebeke/regülasyon riskini kapsamalı.
>     Tercih: TBK m.136 atfı + açık liste. Kabul edilmezse asgari: "şebeke kesintisi" eklensin.
```

**Form (b) — Temiz revize + liste:** temiz metin (değişiklikler uygulanmış) + ayrı tablo:
```markdown
| # | Madde | Değişiklik | Gerekçe | Severity |
|---|---|---|---|---|
| 1 | 12.3 Mücbir sebep | tanım genişletildi + 30 gün | şebeke/regülasyon riski | 🟠 |
```

**Form (c) — Yapılandırılmış tablo:** `madde | mevcut | önerilen | gerekçe | severity` (uygulamayı kullanıcı yapar).

> **Claude Code yolu:** python-docx ile `w:del`/`w:ins` (yazar="ArthurLegal", tarih) + `w:comment` üretip `<dosya>_redline.docx` döndürülebilir. Projects'te dosya oluşturma açıksa aynı yol izlenir; kapalıysa metin redline ([silinen: ...] / [eklenen: ...]) + "Word'de Değişiklikleri İzle açıkken uygulayın" notu.

## ADIM 3 — Çıktı

```markdown
TASLAK – DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ONAYI ALINMADAN İMZALANMAZ

# Redline — [sözleşme adı] — [karşı taraf]

## ⚠️ İnceleyen notu
- **Belge / okuma kapsamı:** [tip, N sayfa okundu]
- **Kağıt:** bizim / karşı taraf · **Form:** (a)/(b)/(c) · **Ortam:** Projects/Code
- **Değişiklik sayısı:** 🔴 N · 🟠 N · 🟡 N · 🟢 N
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [✓/✗]
- **Madde kontrolü:** [redline, yorum ve gerekçedeki her madde atfı → okundu ve eşleşti / çekilemedi, çıkarıldı]
- **Onay:** Baş Hukuk Müşaviri + dış vekil şart

[seçilen formda redline]

## Sonraki adımlar
> 1. **Eksik inceleme** — `/arthurlegal:commercial-legal-review` ile derinleştir
> 2. **Governing law / yaptırım** — `/arthurlegal:commercial-legal-governing-law-review`
> 3. **Karşı teklif turu** — kabul/ret sonrası `/arthurlegal:contract-drafting-versiyon-karsilastir`
> 4. **Temiz nüsha** — kabul edilen değişikliklerle final taslak
> 5. **Başka**

**One question I'd ask:** [örn. "Bu karşı tarafla ilişki sürüyor mu? Sürüyorsa redline tonu agresif değil 'işbirlikçi-ama-korumalı' olmalı."]
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
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | `/arthurlegal:legal-research-sozlesme-emsali` |
| AZ hukuku secilmisse emredici hukum kontrolu — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil) — okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `${CLAUDE_PLUGIN_ROOT}/references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
