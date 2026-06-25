# KEP + e-Tebligat Rehberi

> Resmî elektronik posta + e-tebligat sistemi — büronun ana resmî iletişim kanalı.

---

## Hukuki dayanak

- **5070 sayılı Elektronik İmza Kanunu** — KEP altyapı
- **6102 sayılı TTK m. 18/3** — Tacirler arası KEP yazışma
- **7201 sayılı Tebligat Kanunu m. 7/A** — Elektronik tebligat
- **e-Tebligat Yönetmeliği** (RG 06.12.2018 / 30617)
- **Avukatlar için KEP zorunluluğu** — TBB tavsiyesi (zorunlu değil ama pratik)

---

## KEP — temel kavramlar

### KEP nedir?

**Kayıtlı Elektronik Posta** — kanunla tanımlı **güvenli elektronik posta** sistemi:
- Gönderici + alıcı kimliği **doğrulanmış**
- Gönderim + alma + okuma zamanları **noter onaylı** delil değerinde
- Posta operatörü (KEP hizmet sağlayıcı — BTK lisanslı) tarafından **arşivlenir** (15 yıl)
- **5070 sayılı K. çerçevesinde** — yazılı belge gücünde

### KEP hizmet sağlayıcıları (BTK lisanslı)

- PttKep
- ETBA KEP (e-Tuğra)
- Türk Telekom KEP
- Vodafone KEP
- TNB KEP
- (BTK'nın güncel listesinden teyit — `btk.gov.tr`)

### KEP adresi yapısı

`isim@kepadresi.com` veya `isim@hs[N].kep.tr` formatında. Her adres **gerçek kişi veya tüzel kişi** bazlı, **TC kimlik veya vergi no** ile eşleştirilmiş.

---

## KEP — büro pratiği

### Kim ne için kullanır?

| Aktör | KEP kullanımı |
|---|---|
| **Büro (tüzel kişi)** | Müvekkil yazışmaları, resmî tebligat alma, dış muhasebeci/YMM |
| **Her ortak (bireysel)** | Karşı yan vekille, mahkeme/savcılık, kendi müvekkilleri |
| **Müvekkil** | Sözleşme teslim, ihtarname, e-tebligat (varsa) |
| **Bağlı avukatlar** | Genelde büro KEP'i ile işlerini yapar (Yönetici Ortak yetkilendirir) |

### Standart kullanım

1. **Müvekkille birinci kanal** — sözleşme + matter dokümanı alışverişi
2. **Karşı yan vekille resmî yazışma** — sulh teklifi, müzakere, ihtarname
3. **Mahkeme/savcılık dilekçe** — bazı mahkemeler KEP kabul ediyor (UYAP'tan paralel)
4. **İhtarname çekme** — noter yerine doğrudan KEP üzerinden (TBK m. 117 + 5070)
5. **Müvekkilin VERBİS bildirimi** kontrol/sunum

⚠️ **KEP gönderimi kalıcı kayıt** — sonra silinemez. Yanlış göndermeye dikkat.

---

## İhtarname — KEP üzerinden

Klasik noter ihtarname yerine **KEP ihtarname** mümkün:

### Şartlar (TBK m. 117 + 5070)

- Karşı yanın **KEP adresi olmalı** ve adına kayıtlı
- İhtarname **net + gerekçeli + süreli**
- KEP gönderim kaydı **delil**

### Avantaj — dezavantaj

| KEP ihtarname | Noter ihtarname |
|---|---|
| Anında gönderim | 1-2 gün |
| 50-200 TL (KEP gönderim ücreti) | 500-2.000 TL (noter ücreti) |
| Karşı yanın KEP'i şart | Karşı yan adres yeterli |
| Delil değeri (Yargıtay kabul ediyor) | Tartışmasız delil |

Bazı durumlarda Yargıtay **KEP ihtarnamenin tebligat değeri**ni tartışıyor (özellikle karşı yan KEP'i unutmuşsa). **Önemli matter'larda her ikisini de gönder** (KEP + iadeli posta).

### Pratik şablon

```
KEP İhtarname — [Tarih]
Konu: [Sözleşme adı / matter] kapsamında ihtarname

Sayın [karşı yan adı, KEP],

[Müvekkil] adına vekil olarak, [tarihinde imzalanmış] [sözleşme adı]
kapsamında [tarih] tarihinde ifa edilmesi gereken [yükümlülük]
yerine getirilmemiştir.

İşbu ihtarname ile [Müvekkil] sizi:

1. [Yapılması gereken] [N gün] içinde yerine getirmeniz,
2. Aksi halde [hukuki sonuç] meydana geleceğini

bildiririz. Süre bu KEP'in tarafınıza ulaşmasından itibaren başlar.

Saygılarımızla,

[Av. Ad - Sicil - Baro]
[Büro Adı]
KEP gönderim no: [...]
```

---

## e-Tebligat (7201 sayılı Tebligat K. m. 7/A)

### Kapsam

- **Anonim Şirketler + Limited Şirketler:** Zorunlu (2019 sonrası)
- **Avukatlar:** Zorunlu (TBB üyesi olarak)
- **Noterler, kamu kurumları:** Zorunlu
- **Gerçek kişi:** İsteğe bağlı (talep ederse)

### Sistem

- **PTT KEP** üzerinden çalışır
- UYAP'la entegre — mahkeme/savcılık/icra tebligatı bu kanaldan
- Açma + okuma kayıtları — tebligat tarihi otomatik

### Tebligat tarihi hesabı

7201 m. 7/A:
- e-Tebligat **gönderildikten sonra 5. günün sonunda** **tebliğ edilmiş sayılır** (alıcı açmasa bile)
- Açıldığı tarih erkenkse — açıldığı tarih
- **5 günlük süre dolduğunda tüm yargı süreleri başlar**

⚠️ **Bu nedenle e-Tebligat günlük kontrol** — özellikle dava süresi kritik matter'larda.

### Pratik

- Office Manager (veya atanmış avukat) her sabah e-Tebligat kontrolü
- Süre kritik tebligat (örn. 30 g dava süresi başlayan) → matter notlarına işle + ilgili avukatı bilgilendir
- Tebligat içeriği matter klasörüne kopya

---

## Müvekkil ile KEP koordinasyonu

### Müvekkilin KEP'i yoksa

- Bireysel müvekkil: opsiyonel (öneririz ama zorlanmaz)
- KOBİ tüzel kişi: zaten zorunlu — yoksa MERSİS uyumsuzluk
- Sözleşme paylaşımı için **şifreli e-posta** alternatif

### Müvekkil KEP adresini doğrulama

Yeni müvekkil intake'inde:
- KEP adresini iste
- KEP rehberinden kontrol (resmi olarak kayıtlı mı, müvekkile mi ait?)
- Test mesajı gönder → müvekkil cevap versin

### Müvekkilden gelen "şüpheli KEP"

KEP'in **kimliğin doğrulanmış** olması delil bağlayıcılığını sağlar. Ancak:
- **Yanlış kişi KEP'i bilse** (örn. şirket müdürü değişti, eski müdür KEP'e erişiyor)
- **Hacked KEP** (nadir — kimlik doğrulamayı geçemez)

Şüphede:
- KEP gönderiminin **başka bir kanal** ile teyidi (telefon, yüz yüze)
- Müvekkilden **doğrulayıcı imza** isteme

---

## KEP fatura + ücret

- KEP hizmet ücreti: yıllık ~`[DOLDUR — örn. 200-500 TL/yıl]` (bireysel)
- Büro KEP'i: aylık paket (örn. 1.000 mesaj/ay) veya pay-per-mesaj
- Yıllık KEP yenileme (kimlik tespit yenilenir) — atlanmaması için takvim

---

## Karşı yan vekille KEP yazışması — örnek pratik

### Sulh teklifi

```
KEP — Sulh Teklif Görüşmesi
Konu: [Matter adı] — sulh önerisi

Sayın Av. [karşı vekil],

Müvekkilim [rumuz] adına, [matter] kapsamındaki uyuşmazlık için
aşağıdaki sulh teklifimi sunarım:

1. [Teklif maddeleri]
2. [...]

Cevabınızı [tarih] tarihine kadar bekliyoruz.

Bu yazışma Avukatlık K. m. 36 ve TBB Meslek Kuralları çerçevesinde
yapılmaktadır.

Saygılarımla,
[Av. Ad]
[Büro]
```

⚠️ **KEP yazışma müvekkili bağlar** — yazılı teklif = yazılı yetki gerekli. Müvekkilin yazılı talimatı olmadan **bağlayıcı** sulh teklifi gönderme.

---

## Atıf disiplini

- `[KEP gönderim no — tarih GG.AA.YYYY HH:MM]`
- `[e-Tebligat — UYAP — tebligat no — tarih]`
- `[Mevzuat MCP — 5070 sayılı K. / TBK m. 117 / 7201 m. 7/A — GG.AA.YYYY]`

---

## Yaygın hatalar

1. **e-Tebligat 5. gün kuralını atlamak** — süreyi hesaplama yanlışı
2. **KEP göndermeden önce müvekkil yazılı yetki almama** — bağlayıcı teklif
3. **KEP adresini yanlış doğrulama** — eski şirket yetkilisine teklif
4. **Hassas matter'da sadece KEP kullanmak** — Yargıtay zaman zaman noter ister
5. **KEP arşivini silme** — KEP sağlayıcı 15 yıl tutuyor ama büroda yedek yok = delil kaybı
