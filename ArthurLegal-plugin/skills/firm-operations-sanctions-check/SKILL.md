---
name: firm-operations-sanctions-check
description: >
  Müvekkil, temsilciler, gerçek faydalanıcılar ve (biliniyorsa) karşı taraf için yaptırım
  ve PEP taraması. OpenSanctions sonucunu ve Türk hukukundaki malvarlığı dondurma
  kararlarını (6415, 7262) ayrı raporlar. Sonuç: ✓ TEMİZ / 🟠 İNCELE / ⛔ HIT.
user-invocable: true
---

# Sanctions Check — Yaptırım Taraması

## Tetikleyici

- `/arthurlegal:firm-operations-masak-kontrol` sonrasında (gerçek faydalanıcı listesi hazırken)
- Yabancı bağlantılı müvekkil veya karşı taraf
- Ödemeyi üçüncü bir kişi yapacaksa
- Uzun süren işte periyodik tekrar (`firm-profile.md`'deki sıklık)

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- TERÖRİZMİN FİNANSMANININ ÖNLENMESİ HAKKINDA KANUN (Kanun No. 6415, RG 16.02.2013/28561) m. 5, m. 6, m. 7
- KİTLE İMHA SİLAHLARININ YAYILMASININ FİNANSMANININ ÖNLENMESİNE İLİŞKİN KANUN (Kanun No. 7262, RG 31.12.2020/31351 (Mükerrer)) m. 1, m. 3
- KİŞİSEL VERİLERİN KORUNMASI KANUNU (Kanun No. 6698, RG 07.04.2016/29677) m. 9
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36

## Türk hukukunda dondurma kararları nereden gelir

| Kaynak | Mekanizma | Dayanak |
|---|---|---|
| BMGK 1267 (1999), 1988 (2011), 1989 (2011) ve 2253 (2015) sayılı kararlarla listelenenler | Cumhurbaşkanı kararı Resmî Gazete'de yayımlanır, gecikmeksizin uygulanır | 6415 m. 5/1 |
| Yabancı devlet hükümetinin talebi | Değerlendirme Komisyonu değerlendirir, Cumhurbaşkanı karara bağlar; karşılıklılık gözetilir | 6415 m. 6/1 |
| Türkiye'deki malvarlığı (mahkemelerce terör örgütü olduğuna kesin karar verildikten sonra) | Komisyon önerisiyle Hazine ve Maliye Bakanı ile İçişleri Bakanı birlikte karar verir; karar 48 saat içinde Ankara ağır ceza mahkemesinin onayına sunulur | 6415 m. 7/3-4 |
| BMGK'nın kitle imha silahlarının yayılmasının finansmanına ilişkin kararları | Cumhurbaşkanı kararı Resmî Gazete'de yayımlanır; nihai listeler ilgili kurumların internet sitelerinde yayımlanır | 7262 m. 3/1, m. 3/3 |

AB, ABD (OFAC) ve Birleşik Krallık listeleri 6415 m. 5 ile 7262 m. 3'teki BMGK mekanizmasının parçası değildir. Yabancı devlet talebi için 6415 m. 6 yolu vardır; bu listelerin Türkiye'de doğrudan sonuç doğurduğu başka bir yol bu pakette doğrulanmadı. Yine de müvekkilin bankaları ve yabancı karşı tarafları bakımından iş ve itibar riski taşırlar; raporda **ayrı satırda** göster.

## Akış

### 1. Taranacaklar
- Müvekkil. Gerçek kişide ad, doğum yılı, uyruk; tüzel kişide unvan, ülke, sicil numarası.
- Tüzel müvekkilde temsilciler ve `masak-kontrol`'deki gerçek faydalanıcılar
- Karşı taraf (biliniyorsa) ve ödemeyi yapacak üçüncü kişi

### 2. Veri en azı ve sır
- Sorguya **yalnız tarama için gereken alanlar** girer. İşin konusu, dosya özeti, karşı tarafla ilişki ve talep **gönderilmez** (Av. K. m. 36).
- OpenSanctions yurt dışında bir hizmettir; ona kişisel veri göndermek **yurt dışına aktarımdır** (KVKK m. 9). Büronun bu aktarım için dayanağı `/arthurlegal:firm-operations-kvkk-aydinlatma` kaydında yoksa gerçek kişi taramasını durdur: 🟠 İNCELE → Yönetici Ortak.

### 3. OpenSanctions
- Çağrı kalıbı: `${CLAUDE_PLUGIN_ROOT}/references/opensanctions-rehberi.md` (match API, `default` kapsam, curl ile).
- Anahtar `OPENSANCTIONS_API_KEY` ortam değişkenindedir; pakette yoktur. Değişken tanımlı değilse API çağrısı yapma, rehberdeki manuel kaynaklarla (OpenSanctions web araması dahil) tara. Anahtarı hiçbir çıktıya, nota, dosyaya veya sohbet metnine yazma.
- Skor 0 ile 1 arasındadır (OpenSanctions dokümanı). Yorum: ≥ 0,90 → ⛔; 0,70-0,90 → 🟠, ayırt edici bilgilerle (doğum tarihi, uyruk, sicil numarası) teyit et; < 0,70 → ✓, kaydet.
- Yalnız ad benzerliğiyle hüküm kurma. Eşleşen kaydın doğum tarihi, uyruk ve sicil bilgisini müvekkilinkiyle karşılaştır.

### 4. Türk listeleri
6415 ve 7262 kapsamında yayımlanan kararları ve 7262 m. 3/3 uyarınca kurum sitelerinde yayımlanan nihai listeleri elle kontrol et; kontrol tarihini ve kaynağı yaz. OpenSanctions'ın Türk listelerini kapsayıp kapsamadığı ve güncelliği bu pakette doğrulanmadı.

### 5. Karar

| Sonuç | Anlam | Akış |
|---|---|---|
| ✓ TEMİZ | anlamlı eşleşme yok | kayıt → `/arthurlegal:firm-operations-kvkk-aydinlatma` |
| 🟠 İNCELE | orta skor, ad benzerliği, PEP, yabancı liste eşleşmesi | ek teyit + Yönetici Ortak |
| ⛔ HIT | kişi veya kuruluş bir Türk dondurma kararında yer alıyor ya da ≥ 0,90 skorla teyitli eşleşme var | iş kabulü durur → Yönetici Ortak + Ortaklar Kurulu; finansal işlem aracılığı yapılmaz; `/arthurlegal:firm-operations-masak-kontrol` şüpheli işlem değerlendirmesi |

Savunma hakkı kapsamındaki temsil ile finansal işlem aracılığı ayrı değerlendirilir. Kabul veya ret kararını bu skill vermez, Ortaklar Kurulu verir.

## Çıktı

```markdown
[ÜST BAŞLIK — YAPTIRIM TARAMASI — DAHİLİ]

# Sanctions Check — [takma ad] — GG.AA.YYYY
| Taranan | Kaynak | Sonuç | Skor | Eşleşen liste | Teyit |
|---|---|---|---|---|---|
| Müvekkil | OpenSanctions | ✓ / 🟠 / ⛔ | [X] | [liste] | [doğum tarihi / uyruk / sicil karşılaştırması] |
| GF-1 | OpenSanctions | ... | | | |
| Müvekkil | TR dondurma kararları (6415 / 7262) | ✓ / ⛔ | — | [karar, RG tarihi] | elle kontrol GG.AA.YYYY |

Atıf: [OpenSanctions API — match skoru X — GG.AA.YYYY]
SONUÇ: ✓ TEMİZ / 🟠 İNCELE / ⛔ HIT
```

## Hatalar

- Dosya ayrıntısını sorguya koymak (Av. K. m. 36)
- KVKK m. 9 dayanağı olmadan gerçek kişi verisini yurt dışındaki API'ye göndermek
- Teyitsiz ad benzerliğini HIT saymak
- OFAC veya AB eşleşmesini "Türkiye'de malvarlığı dondurulmuş" diye raporlamak
- API anahtarını çıktıya yazmak

Ayrıntı: `${CLAUDE_PLUGIN_ROOT}/references/opensanctions-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/yaptirim-tarama-rehberi.md`

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
