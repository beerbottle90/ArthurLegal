---
name: firm-operations-cold-start-interview
description: >
  Büro profilini ilk doldurma — TÜM diğer plugin'lerin okuyacağı ana profil.
  Büro kadrosu, ortaklar, organizasyon yapısı, baro kayıt durumu, müvekkil
  portföyü agregat (sektör + tip + coğrafya), pratik alanları, müvekkil intake
  politikası, vekalet ücreti modeli, mesleki sır pratikleri, operasyonel platformlar.
  Sonuç: ${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md doldurulur.
user-invocable: true
---

# Cold Start Interview — firm-operations (ANA PROFİL)

## Amaç

`${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md` içindeki `[DOLDUR]` alanlarını doldur. ~20-30 dk (büronun tüm bilgisini topluyor).

⚠️ **Bu, paketteki TÜM diğer plugin'lerin okuyacağı ana profildir. Önce bu plugin'i çalıştırın, sonra diğer plugin'lerin cold-start'larını.**

## Adımlar

### 1. Büro temel bilgileri

- Büro adı, hukuki yapı (Avukatlık Ortaklığı / Hibrit / Bireysel)
- TBB Avukatlık Ortaklıkları Sicil no (varsa)
- Kuruluş yılı
- Vergi no, MERSİS (varsa Av. Ortaklığı tüzel kişiliği)

### 2. Ofis ve coğrafya

- Merkez ofis: il / ilçe / adres
- İrtibat ofisleri (varsa)
- Çalışma dilleri (Türkçe ana, İngilizce, başka?)

### 3. Kadro

- Yönetici Ortak (takma ad + baro/sicil + uzmanlık)
- Kıdemli Ortaklar (sayı + uzmanlık dağılımı)
- Bağlı avukat sayısı
- Stajyer sayısı
- Hukuk asistan + sekretarya sayısı
- **Toplam kadro** (0-30 bandı kontrol)

### 4. Baro kayıt

- İstanbul Barosu kaç ortak/avukat (asıl)
- Ankara Barosu kaç ortak/avukat (asıl/bağlı)
- Diğer barolar

### 5. Müvekkil portföyü (agregat — gerçek isim YOK)

- Aktif müvekkil sayısı
- Sürekli danışmanlık (retainer) sayısı
- Müvekkil tip dağılımı (bireysel / KOBİ / mid-cap / yabancı)
- Sektör dağılımı (inşaat / perakende / üretim / hizmet / teknoloji / bireysel)
- Coğrafi dağılım (İstanbul / Anadolu yakası / Ankara / başka / yurtdışı)

### 6. Pratik alanları

- Hangi plugin'ler aktif kullanılacak? (criminal-defense, firm-operations dahil)
- Aylık matter hacmi tahmini her plugin için

### 7. Müvekkil intake politikası

- Yeni müvekkil kabul akışında zorunlu adımlar
- Conflict check derinliği
- MASAK kimlik tespit alışkanlığı
- KVKK aydınlatma metni standardı var mı?
- Otomatik 🟠 incelemeli kabul tetikleyicileri

### 8. Vekalet ücreti modeli (büro seviye)

- Standart model: saatlik / götürü / hibrit / başarı bonusu?
- Saatlik oran (Yönetici/Kıdemli Ortak, Bağlı Avukat, Stajyer)
- Başarı bonusu sınırı (max %25 — Av. K. m. 164)
- Karşı yan vekalet ücreti politikası (vekile mi, paylaşılır mı)

### 9. Operasyonel platformlar

- Matter / belge yönetimi (iManage / SharePoint / Drive / dahili)
- Zaman takibi (Clio / TimeSolv / Excel)
- Fatura / muhasebe (dahili / dış muhasebeci)
- E-imza / KEP (büro + her ortak)
- CRM (varsa)
- Sanctions tarama (resmî listeler WebFetch ile; ayrıca ticari tarama hizmeti var mı?)

### 10. "Yakıcı" stres alanları

> "Bu büroda günlük operasyonu en çok zorlayan 1-3 şey nedir?"

## Çıktı

`${CLAUDE_PLUGIN_ROOT}/references/firm-profile.md` doldurulur.

```
✓ Büro profili tamamlandı.

Sonraki adımlar:
1. Diğer plugin'lerin cold-start-interview'larını çalıştırın:
   /arthurlegal:litigation-legal-cold-start-interview
   /arthurlegal:commercial-legal-cold-start-interview
   (her aktif plugin için)
2. İlk müvekkil için: /arthurlegal:firm-operations-new-client-intake

Re-run: /arthurlegal:firm-operations-cold-start-interview --redo
```

## Hatalar / kenar durumlar

- **Kullanıcı 30+ çalışan diyorsa** → "Bu paket 0-30 kadro için optimize edilmiş. 30+ için bazı pratikler (matter izolasyonu, ethical wall, large M&A) farklı yönetilir. Yine de devam edelim mi?"
- **Tüm soruları cevaplamak istemez** → Quick start (5 dk) vs. Full (20-30 dk) seçeneği sun
- **Müvekkil isim/şirket isteyebilir** → "ASLA gerçek müvekkil ismi yazmayın. Takma ad/agregat kullanın."

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
