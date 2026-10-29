---
name: firm-operations-new-client-intake
description: >
  Yeni müvekkil ön sohbet sonrası intake akışı: müvekkil bilgisi alma, talep
  özeti, matter tipi belirleme + plugin yönlendirmesi, aciliyet kontrolü, sonraki
  zorunlu adımlar (conflict-check, MASAK, sanctions, KVKK, fee, vekalet) tetikleme.
user-invocable: true
---

# New Client Intake — Yeni Müvekkil Ön Sohbet

## Tetikleyici

İlk temas (telefon / web / referans) sonrası, atanan ortak müvekkille ön sohbeti yaptıktan sonra.

## Adımlar

### 1. Müvekkil bilgisi

**Gerçek kişi:**
- Takma ad (kayıt için — gerçek isim KVKK uyarınca minimum)
- TC kimlik no (kimlik tespit için sonradan MASAK)
- Telefon + e-posta (mümkünse KEP)
- Meslek + işveren

**Tüzel kişi:**
- Ünvan (kısaltılmış takma ad)
- Vergi no + MERSİS no
- Faaliyet alanı (NACE)
- Yetkili temsilci
- KEP adresi

### 2. Talep özeti

- 1-2 cümle özet
- Karşı taraf var mı?
- Tahmini değer
- Tarih + süreler (aciliyet kontrolü)

### 3. Matter tipi → plugin yönlendirmesi

| Talep | Plugin |
|---|---|
| Müvekkil davacı/davalı (ticari/medeni) | `litigation-legal` |
| Müvekkil idari kararı iptal | `administrative-legal` |
| Müvekkil vergi tarhiyatı iptal | `tax-legal` |
| Müvekkil ceza şüphelisi/sanığı | `criminal-defense` |
| Müvekkil sözleşme yazımı/inceleme | `commercial-legal` |
| Müvekkilin GK/YK/M&A işlemi | `corporate-legal` |
| Müvekkil işveren/işçi iş hukuku | `employment-legal` |
| Müvekkilin marka/patent/tasarım | `ip-legal` |
| Veri koruma / KVKK | `privacy-legal` |
| Düzenleyici kurum / lisans | `regulatory-legal` |
| Enerji M&A / proje finansmanı | `energy-finance` |
| Aile/miras/boşanma | **KAPSAM DIŞI** — başka büroya yönlendir |

### 4. Aciliyet kontrolü

| Süre durumu | Etiket |
|---|---|
| Dava süresi < 7 gün | 🔴 ACİL |
| Dava süresi < 30 gün | 🟠 Yüksek |
| Sözleşme imza < 3 gün | 🟠 Yüksek |
| Tutuklu müvekkil (ceza) | 🔴 ACİL — 48 saat sınırı |
| Süre kritik değil | 🟢 Standart akış |

### 5. Sonraki zorunlu adımlar listesi

```
ZORUNLU SONRAKI ADIMLAR:
[ ] /arthurlegal:firm-operations-conflict-check   ← İLK + KRİTİK
[ ] /arthurlegal:firm-operations-masak-kontrol    (önce kapsam testi: dava vekilliği çoğunlukla KAPSAM DIŞI)
[ ] /arthurlegal:firm-operations-sanctions-check
[ ] /arthurlegal:firm-operations-kvkk-aydinlatma
[ ] /arthurlegal:firm-operations-fee-agreement
[ ] /arthurlegal:firm-operations-vekalet-sablon
[ ] /arthurlegal:firm-operations-matter-open
```

## Çıktı

```markdown
[ÜST BAŞLIK — INTAKE NOTU — DAHİLİ]

# Müvekkil Intake — [Takma ad] — [Tarih]

## ⚠️ İnceleyen notu
- Aciliyet: 🔴/🟠/🟢
- Önerilen plugin: [...]
- Sonraki zorunlu adımlar: 7 adım

## Müvekkil
- Tip: Bireysel / Tüzel kişi
- Takma ad: [...]

## Talep özeti
[1-2 cümle]

## Matter tipi
[Plugin]: [...] — gerekçe

## Aciliyet
🔴/🟠/🟢 — [neden]

## Sonraki ZORUNLU adımlar
1. /arthurlegal:firm-operations-conflict-check (İLK)
2. /arthurlegal:firm-operations-masak-kontrol
3. /arthurlegal:firm-operations-sanctions-check
4. /arthurlegal:firm-operations-kvkk-aydinlatma
5. /arthurlegal:firm-operations-fee-agreement
6. /arthurlegal:firm-operations-vekalet-sablon
7. /arthurlegal:firm-operations-matter-open
```

## Hatalar

- **Müvekkilin gerçek ismini intake notuna yazma** — takma ad kullan
- **Conflict check tetiklenmeden iş başlatma** — Av. K. m. 38 ihlal riski
- **KAPSAM DIŞI matter'ı kabul etme** — yetersiz hizmet riski

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
