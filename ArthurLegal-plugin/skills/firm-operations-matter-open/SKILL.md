---
name: firm-operations-matter-open
description: >
  Kabul kararından sonra matter kaydını açar: ön koşul kapısı (conflict, MASAK,
  sanctions, KVKK, ücret, vekâlet), matter-slug, klasör ve erişim düzeni, süre takvimi,
  vekâletname ibrazı ve ilgili plugin'e devir.
user-invocable: true
---

# Matter Open — Dosya Açılışı

## Tetikleyici

Kabul kararı verildikten sonra (rutin dosyada atanan ortak + Yönetici Ortak; 🟠 dosyada Ortaklar Kurulu).

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36, m. 171, m. 174
- HUKUK MUHAKEMELERİ KANUNU (Kanun No. 6100, RG sayı 27836) m. 76, m. 77
- KİŞİSEL VERİLERİN KORUNMASI KANUNU (Kanun No. 6698, RG 07.04.2016/29677) m. 9, m. 12
- SUÇ GELİRLERİNİN AKLANMASININ ÖNLENMESİ HAKKINDA KANUN (Kanun No. 5549, RG 18.10.2006/26323) m. 4, m. 8

## Akış

### 1. Ön koşul kapısı

| Adım | Aranan kayıt | Eksikse |
|---|---|---|
| `/arthurlegal:firm-operations-conflict-check` | ✓ TEMİZ ya da 🟠 + Ortaklar Kurulu kararı | ⛔ **açma**; istisnası yok |
| `/arthurlegal:firm-operations-masak-kontrol` | KAPSAM DIŞI ya da ✓ TAMAM | ⛔ kapsamdaysa açma (Yön. m. 22) |
| `/arthurlegal:firm-operations-sanctions-check` | ✓ TEMİZ ya da karar kaydı | ⛔ |
| `/arthurlegal:firm-operations-kvkk-aydinlatma` | ispat kaydı | 🟠 aç, ilk yazışmada tamamla |
| `/arthurlegal:firm-operations-fee-agreement` | imzalı sözleşme | 🟠 peşin ücret ödenmediyse avukat işe başlamak zorunda değil (Av. K. m. 174/3) |
| `/arthurlegal:firm-operations-vekalet-sablon` | vekâletname | dava işinde bkz. adım 5 |

### 2. matter-slug
`<müvekkil-slug>__<konu-slug>__<yyyy>`. Yalnız takma ad kullanılır; gerçek isim, TCKN veya VKN slug'a girmez. Örnek: `mv-ay-insaat__kira-tahliye__2026`.

### 3. Klasör düzeni
`pre-matter/<tarih>__<müvekkil-takma-ad>/` içeriği `matters/<müvekkil-slug>__<matter-slug>/` altına taşınır:

```
00-intake/          intake notu, conflict sonucu
01-uyum/            MASAK ve sanctions notları (erişim: atanan ortak + Yönetici Ortak)
02-sozlesme/        ücret sözleşmesi, KVKK aydınlatma ispatı
03-vekalet/         vekâletname, yetki belgesi
04-yazisma/
05-taslak/
06-delil/
07-karar-tebligat/
```

Şüpheli işlem değerlendirmesi **hiçbir** matter klasörüne girmez (5549 m. 4/2, açıklama yasağı); ayrı ve kısıtlı uyum kaydında durur.

### 4. Erişim ve sır
- Erişim yalnız atanan ekipte olur. Conflict-check 🟠 ile açılan dosyada ayrı erişim grubu kurulur (ethical wall).
- Avukat, görevi dolayısıyla öğrendiklerini açığa vuramaz (Av. K. m. 36). Klasör paylaşım bağlantısı "herkese açık" olamaz.
- Veri güvenliği için teknik ve idari tedbir alınır (KVKK m. 12/1). Bulut sağlayıcı yurt dışındaysa m. 9 dayanağı `/arthurlegal:firm-operations-kvkk-aydinlatma` kaydında yer almalıdır.

### 5. Dava veya takip işi: vekâletname
- Avukat, açtığı veya takip ettiği iş için noter onaylı ya da düzenlenmiş vekâletname aslını veya avukat onaylı örneğini dosyaya ibraz eder (HMK m. 76/1).
- Vekâletnamesiz dava açılamaz, işlem yapılamaz. Gecikmede zarar doğabilecek hâlde mahkeme kesin süre vererek izin verebilir; süre içinde vekâletname getirilmezse dava açılmamış veya işlem yapılmamış sayılır (HMK m. 77/1). Acil dosyada vekâletname tarihini takvime **ilk** kalem olarak gir.

### 6. Süre takvimi
- intake'teki aciliyet etiketiyle birlikte dosyadaki her kesin süre, zamanaşımı ve hak düşürücü süre takvime girer; iki kişi (avukat + asistan) kontrol eder.
- Süre hesabı ilgili plugin'in skill'inde yapılır; burada yalnız kayıt açılır.

### 7. Muhafaza etiketi
- MASAK kapsamındaki işte: son işlem + sekiz yıl (5549 m. 8).
- Diğer saklama süreleri (vergi, meslek kuralları) bu pakette doğrulanmadı; `firm-profile.md`'deki büro politikası uygulanır.

### 8. Devir
`/arthurlegal:firm-operations-new-client-intake`'teki yönlendirme tablosuna göre ilgili plugin'e geç: dava için `/arthurlegal:litigation-legal-case-intake`; diğer işlerde ilgili plugin'in skill listesi (profil boşsa önce o plugin'in `cold-start-interview`'u). Avukat, üzerine aldığı işi yazılı sözleşme olmasa bile sonuna kadar takip eder (Av. K. m. 171/1).

## Çıktı

```markdown
[ÜST BAŞLIK — MATTER AÇILIŞ KAYDI — DAHİLİ]

# [matter-slug] — açılış GG.AA.YYYY
- Atanan ortak / ekip: [...]
- Ön koşullar: conflict ✓ · MASAK [KAPSAM DIŞI / ✓] · sanctions ✓ · KVKK ✓ · ücret ✓ · vekâlet ✓ / bekliyor
- Erişim grubu: [...] — ethical wall: yok / var
- İlk 3 süre: [tarih — iş — kaynak]
- Muhafaza: [son işlem + 8 yıl / büro politikası]
- Devir: [/plugin:skill]
```

## Hatalar

- Conflict-check olmadan klasör açmak
- Slug'a gerçek isim yazmak
- Uyum notlarını, özellikle şüpheli işlem değerlendirmesini, matter klasörüne koymak
- Vekâletname gelmeden işlem yapıp HMK m. 77'deki kesin süreyi takvime yazmamak

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
