---
name: litigation-legal-hearing-prep
description: >
  Duruşma öncesi hazırlık paketi: 1 sayfa dava özeti, karşı taraf iddia haritası,
  cevap/beyan dilekçesi taslağı, delil sunum sırası, tanık soru listesi, "olası
  hakim soruları" hazırlığı. Dış vekil ile koordineli — in-house tarafından dış
  vekile gönderilen "duruşma günü brief'i".
user-invocable: true
---

# Hearing Preparation — Duruşma Hazırlık Paketi

## Matter context

Aktif matter şart. `matter.md`'den son durum çekilir.

## Destination check

- **Dış vekile gidecek duruşma brief'i** → AVUKATLIK K. m. 36 üst başlığı
- **İç değerlendirme (Hukuk Direktörü bilgi)** → GİZLİDİR HUKUK MÜŞAVİRLİĞİ
- **Mahkemeye sunulacak cevap dilekçesi taslağı** → "TASLAK" + dış vekil onayı sonrası

## Amaç

Duruşma günü dış vekilin elinde olması gereken **tek-paketlik özet:** mahkemenin görüşeceği konuların özeti, bizim pozisyonumuz, karşı tarafın muhtemel hamleleri, hazır cevaplar.

## Adımlar

### 1. Dava 1-sayfa özeti

```markdown
# [Dosya] - Duruşma Brief'i

**Esas no:** | **Mahkeme:** | **Hâkim:** | **Tarih:** | **Saat:**
**Taraflar:** | **Karşı vekil:** | **[Müvekkil] vekili:** | **Konu özeti:**

**Bu duruşmanın gündemi (tahmin):**
- [Mahkeme talebi, varsa]
- [Bilirkişi raporu sonrası tartışma]
- [Tanık dinlenmesi]
- [Yeni delil sunumu]
- [Beyan / cevap dilekçesi alımı]

**Bugün karar verilebilecek meseleler:**
- [...]
```

### 2. Karşı taraf iddia haritası

Karşı tarafın muhtemel argümanlarını ve hazır cevapları:

| Karşı argüman | Bizim cevap | Dayanak (madde/içtihat) |
|---|---|---|
| [...] | [...] | `[ArthurLegal MCP (`tr_`) / ArthurLegal MCP (`tr_`) — GG.AA.YYYY]` |

### 3. Cevap dilekçesi / beyan taslağı (HMK)

Eğer beyan veya cevap dilekçesi sunulacaksa, **dış vekil için ön-taslak:**

```markdown
**[Mahkeme adı] HÂKİMLİĞİNE**

ESAS NO: [...]
KARAR NO: (varsa)

DAVALI / DAVACI: [[Müvekkil]]
VEKİLİ: [dış vekil, baro sicil no]

DAVACI / DAVALI: [karşı taraf]
VEKİLİ: [karşı vekil]

KONU: [Cevap dilekçesi / beyan / ek beyan]

---

I. OLAYLAR

[Olay özeti — bizim açımızdan]

II. HUKUKİ DEĞERLENDİRME

A. [Argüman 1] — [TBK m. ... / TTK m. ... / HMK m. ...]
B. [Argüman 2] — [...]
C. [Argüman 3] — [...]

III. DELİLLERİMİZ

1. [Belge]
2. [Tanık]
3. [Bilirkişi raporuna itirazlarımız]

IV. SONUÇ

Yukarıdaki açıklamalar ışığında, [davanın reddi / kabulü / kısmen kabulü] talep edilir.

Tarih: GG.AA.YYYY

Vekil: [imza]
```

**ÖNEMLİ:** Bu taslak DİREKT mahkemeye sunulmaz — dış vekil revize edip, baro pulu / e-imza ile kendi sunar.

### 4. Delil sunum sırası

Hangi delil, ne zaman, neden bu sırada?

| Sıra | Delil | Sunum anı | Sebep |
|---|---|---|---|
| 1 | [Sözleşme] | İlk beyan | "Pozisyonumuzun temeli" |
| 2 | [E-yazışma] | Karşı taraf X iddiasını yaparsa | "Karşı tarafın bilgi sahibi olduğunu kanıtlar" |

### 5. Tanık soru listesi

Eğer tanık dinlenecekse:

```markdown
**Tanık:** [İsim, sıfat]
**Bizim için sorulması gereken sorular:**
1. [Olayın yaşandığı tarihte siz neredeydiniz?]
2. [Karşı tarafla yazışma kanıtınız var mı?]
3. [...]

**Karşı taraf vekilinin tanığa soracağı muhtemel sorular:**
1. [...]

**Tanığın güçlü yönü:** [...]
**Tanığın zayıf yönü:** [bize karşı sorular bunu hedefleyebilir]
```

### 6. "Olası hakim soruları" hazırlığı

Hâkim duruşmada şu soruları sorabilir; cevaplar:

```markdown
- Hâkim: "Karşı tarafın iddia ettiği [olay] gerçekten yaşandı mı?"
  Cevap: [...]
- Hâkim: "Sulh yolunu denediniz mi?"
  Cevap: [Pratik profili → settlement-eval skill çıktısından]
- Hâkim: "Bilirkişi raporuna itirazınız nedir?"
  Cevap: [...]
```

### 7. Stratejik notlar

```markdown
- **Hâkim eğilimi:** [Önceki dosyalarda Yargıtay/HGK kararlarına bakış, sulh önerisi yapma eğilimi, vs.]
- **Karşı vekil eğilimi:** [Agresif mi, sulha açık mı, formaliteye dikkat eder mi]
- **Bu duruşmada bizim hedefimiz:** [Bilirkişi raporuna itiraz / Sulh teklifini açıkça reddetmemek / Süre kazanma / Karar talebi]
- **Risk:** [Duruşmadan kötü çıkma olasılığı varsa, neden]
```

## ArthurLegal MCP (`tr_`)

```
tr_ictihat_ara(
  query="<dava konusu> bilirkişi rapor itiraz",
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  date_from="2023-01-01"
)
```

Benzer dosyaların **bu aşamada nasıl gittiğini** öğren — strateji şekillenir.

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Duruşma Hazırlık — [Esas No / Dosya Slug]

## ⚠️ İnceleyen notu
- **Duruşma tarihi:** GG.AA.YYYY (kalan: N gün)
- **Mahkeme:** [...]
- **Karar verilebilecek:** [N adet]
- **Hazırlık tamlık:** [%X] (eksik: ...)
- **Dış vekil onayı:** [tarih]
- **Reviewer karar bekleyen:** N adet

[1-sayfa özet, iddia haritası, cevap dilekçesi taslağı, delil sırası, tanık soruları, hâkim soruları, stratejik notlar]

## Sonraki adımlar

> 1. **Cevap dilekçesini dış vekile transmit et** — KEP ile
> 2. **Stratejik karar paketi** — Hukuk Direktörü onayı için
> 3. **Bilirkişi raporu detay analizi** — `/arthurlegal:litigation-legal-evidence-collection`
> 4. **Sulh hazırlığı** — `/arthurlegal:litigation-legal-settlement-eval` (hâkim sulh önerirse)
> 5. **Daha fazla bilgi** — şu soruları cevaplayalım: [...]

**One question I'd ask that isn't in my checklist:** [örn. "Karşı tarafın bilirkişi raporuna olan tutumu nasıl? Reddetmiş mi, kabul mu etmiş? Bu duruşmada strateji değiştirebilirler mi?"]
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
| Turk doktrini (DergiPark 19 hukuk dergisi) + karsilastirmali ogreti — **ikincil**; bir karar kademesini yukseltmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| uyusmazlik AZ hukukuna tabiyse akt + statu. **AZ ictihadi bu araclarda YOK** — `azerbaycan-hukuk-rehberi.md` | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
