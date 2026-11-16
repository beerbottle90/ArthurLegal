# firm-operations-new-client-intake

Yeni müvekkil ön sohbet sonrası intake akışı: müvekkil bilgisi alma, talep özeti, matter tipi belirleme + plugin yönlendirmesi, aciliyet kontrolü, sonraki zorunlu adımlar (conflict-check, MASAK, sanctions, KVKK, fee, vekalet) tetikleme.

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
[ ] `firm-operations-conflict-check` iş akışı (`buro-isleri` becerisi, `references/firm-operations-conflict-check.md`)   ← İLK + KRİTİK
[ ] `firm-operations-masak-kontrol` iş akışı (`buro-isleri` becerisi, `references/firm-operations-masak-kontrol.md`)    (önce kapsam testi: dava vekilliği çoğunlukla KAPSAM DIŞI)
[ ] `firm-operations-sanctions-check` iş akışı (`buro-isleri` becerisi, `references/firm-operations-sanctions-check.md`)
[ ] `firm-operations-kvkk-aydinlatma` iş akışı (`buro-isleri` becerisi, `references/firm-operations-kvkk-aydinlatma.md`)
[ ] `firm-operations-fee-agreement` iş akışı (`buro-isleri` becerisi, `references/firm-operations-fee-agreement.md`)
[ ] `firm-operations-vekalet-sablon` iş akışı (`buro-isleri` becerisi, `references/firm-operations-vekalet-sablon.md`)
[ ] `firm-operations-matter-open` iş akışı (`buro-isleri` becerisi, `references/firm-operations-matter-open.md`)
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
1. `firm-operations-conflict-check` iş akışı (`buro-isleri` becerisi, `references/firm-operations-conflict-check.md`) (İLK)
2. `firm-operations-masak-kontrol` iş akışı (`buro-isleri` becerisi, `references/firm-operations-masak-kontrol.md`)
3. `firm-operations-sanctions-check` iş akışı (`buro-isleri` becerisi, `references/firm-operations-sanctions-check.md`)
4. `firm-operations-kvkk-aydinlatma` iş akışı (`buro-isleri` becerisi, `references/firm-operations-kvkk-aydinlatma.md`)
5. `firm-operations-fee-agreement` iş akışı (`buro-isleri` becerisi, `references/firm-operations-fee-agreement.md`)
6. `firm-operations-vekalet-sablon` iş akışı (`buro-isleri` becerisi, `references/firm-operations-vekalet-sablon.md`)
7. `firm-operations-matter-open` iş akışı (`buro-isleri` becerisi, `references/firm-operations-matter-open.md`)
```

## Hatalar

- **Müvekkilin gerçek ismini intake notuna yazma** — takma ad kullan
- **Conflict check tetiklenmeden iş başlatma** — Av. K. m. 38 ihlal riski
- **KAPSAM DIŞI matter'ı kabul etme** — yetersiz hizmet riski

---

## Kaynak katmanı — /legal-research

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
> **Meslek sirri (Av. K. m. 36):** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `skills/arthurlegal/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| yabanci karsi tarafli veya AZ baglantili yeni is alimi — mevzuat kapsaminin gercekten var olup olmadigini once dogrula | ``legal-research-kaynak-secimi` iş akışı (`arastirma-ve-atif` becerisi, `references/legal-research-kaynak-secimi.md`)` |

Rehberler: `skills/arthurlegal/references/eqanun-mcp-rehberi.md` · `skills/arthurlegal/references/lex-scholar-rehberi.md` · `skills/arthurlegal/references/resourcecontracts-rehberi.md` · `skills/arthurlegal/references/karsilastirmali-hukuk-rehberi.md`
