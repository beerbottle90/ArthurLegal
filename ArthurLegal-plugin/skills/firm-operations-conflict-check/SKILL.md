---
name: firm-operations-conflict-check
description: >
  Av. K. m. 38 + TBB Meslek Kuralları m. 35-36 çatışma taraması. Müvekkil + karşı
  yan + atanan avukat üç eksen tarama; eşzamanlı / eski müvekkil / grup içi /
  vekil değişimi / kamu görevi geçmişi senaryoları. Sonuç: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ.
user-invocable: true
---

# Conflict Check — Çıkar Çatışması Taraması

## Tetikleyici

- Yeni müvekkil intake (her yeni matter için zorunlu)
- Mevcut matter'da karşı yan kimliği netleştiğinde
- Mevcut müvekkilin başka bir işi
- Yeni ortak/avukat alındığında (retrospektif)
- Müvekkil yapısı değişti (M&A, pay devri)

## Tarama girdisi

### Müvekkil bilgisi
- Tip: Bireysel / Tüzel kişi
- TC kimlik / Vergi no / MERSİS no
- Ad-soyad / Ünvan
- (Tüzel) yan-grup şirketler — UBO + holding zinciri

### Karşı yan bilgisi
- Tip: Bireysel / Tüzel kişi
- TC kimlik / Vergi no / MERSİS no
- Ad-soyad / Ünvan
- (Tüzel) yan-grup şirketler

### Atanan avukat
- Sicil + baro
- Eski büro/iş geçmişi
- Kamu görevi (hakim/savcı/müfettiş) geçmişi
- Aile/yakın ilişki (büro içi)

## Tarama akışı

### 1. Müvekkilin geçmiş matter'ları taraması

Veritabanı sorgu:
- **Tam eşleşme** (TC/Vergi no)
- **Fonetik benzer ad** (Soundex TR varyasyon — Ş/S, İ/I, Ç/C, Ö/O, Ü/U, Ğ/G)
- **Tarih kapsamı:** son 10+ yıl (Av. K. m. 36 süresiz, ama 10 yıl pratik baseline)

### 2. Karşı yan taraması

- Karşı yanın geçmiş matter'ları (eski müvekkilimiz mi?)
- Karşı yanın grup ilişkileri (MERSİS sicili)

### 3. Atanan avukat taraması

- Atanan avukatın eski büro/iş geçmişi
- Hâkim/savcı/hakem/bilirkişi/memur olarak aynı işte görev (Av. K. m. 38/1-c)
- Aile/yakın ilişki — büro içi

### 4. Çatışma sınıflandırma

Dayanak: AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 38 (doğrulandı 24.09.2026). Reddetme zorunluluğu avukatın **ortaklarını ve yanında çalışan avukatları da** kapsar (m. 38/2), yani tarama büro çapındadır. TBB Meslek Kuralları m. 35-36 metni bu araçla doğrulanamadı (mevzuat.gov.tr'de yok).

| Tip | Kural | Karar |
|---|---|---|
| Aynı işte menfaati zıt tarafa avukatlık etmiş veya mütalaa vermiş (eşzamanlı ya da önceden) | Av. K. m. 38/1-b | ⛔ MUTLAK YASAK |
| Evvelce hâkim, hakem, Cumhuriyet savcısı, bilirkişi veya memur olarak o işte görev | Av. K. m. 38/1-c | ⛔ MUTLAK YASAK |
| Kendi düzenlediği senet veya sözleşmenin hükümsüzlüğünü ileri sürme durumu | Av. K. m. 38/1-d | ⛔ MUTLAK YASAK |
| Teklif yolsuz veya haksız | Av. K. m. 38/1-a | ⛔ RET |
| Eski müvekkil — farklı iş, bilgi bağlantısı var | Av. K. m. 36 (sır) + TBB MK m. 35-36 (doğrulanamadı) | 🟠 İNCELE (yazılı rıza) |
| Grup içi (aynı holding) | "aynı iş" ölçütüyle m. 38/1-b'ye göre değerlendir | 🟠 İNCELE (bilgi izolasyonu mümkün?) |
| Vekil değişimi (yeni gelen avukat) | Eski büro geçmişi; m. 38/2 büro çapında | 🟠 İNCELE (ethical wall) |
| Avukatın kendi menfaati | Self-dealing | ⛔ MUTLAK YASAK |
| Hiçbir çakışma yok | — | ✓ TEMİZ |

## Çıktı

```markdown
[ÜST BAŞLIK — CONFLICT CHECK SONUCU — DAHİLİ]

# Conflict Check — [Müvekkil takma adı] vs. [Karşı yan takma adı]
Tarih: GG.AA.YYYY
Atanan ortak: [Yönetici Ortak veya öneri]

## ⚠️ İnceleyen notu
- SONUÇ: ⛔ RET / 🟠 İNCELE / ✓ TEMİZ

## SONUÇ
[Gerekçeli değerlendirme]

## Sonraki adımlar
[✓ TEMİZ ise] → /arthurlegal:firm-operations-new-client-intake devam
[🟠 ise] → Ortaklar Kurulu + yazılı rıza
[⛔ ise] → Müvekkile red + REJECTED.md kaydı
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
> **Meslek sirri (Av. K. m. 36):** uc MCP de PUBLIC arama aracidir — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| yabanci karsi tarafli veya AZ baglantili yeni is alimi — mevzuat kapsaminin gercekten var olup olmadigini once dogrula | `/arthurlegal:legal-research-kaynak-secimi` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
