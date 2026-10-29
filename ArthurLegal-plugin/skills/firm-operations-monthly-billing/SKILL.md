---
name: firm-operations-monthly-billing
description: >
  Ay sonu matter bazlı ücret hesabı ve tahsilat takibi: süre kayıtları × ücret modeli,
  AAÜT tabanı ve %25 tavanı, karşı taraf vekâlet ücretinin ayrı tutulması, serbest meslek
  makbuzu, tevkifat kontrolü, geç ödemede temerrüt ve faiz.
user-invocable: true
---

# Monthly Billing — Aylık Ücret ve Tahsilat

## Tetikleyici

Ay sonu. Ayrıca yüzde ücretin muaccel olduğu an (sözleşmedeki şarta göre: karar kesinleşti, tahsil edildi vb.).

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36, m. 164, m. 166, m. 174
- VERGİ USUL KANUNU (Kanun No. 213, RG sayı 10705) m. 236
- GELİR VERGİSİ KANUNU (GVK) (Kanun No. 193, RG sayı 10700) m. 94
- TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG sayı 27836) m. 117, m. 120
- KANUNİ FAİZ VE TEMERRÜT FAİZİNE İLİŞKİN KANUN (Kanun No. 3095, RG sayı 18610) m. 1, m. 2
- TÜRK TİCARET KANUNU (Kanun No. 6102, RG sayı 27846) m. 1530

## Akış

### 1. Liste
Aktif matter'lar ve her birinin `/arthurlegal:firm-operations-fee-agreement` kaydındaki ücret modeli ile ödeme takvimi.

### 2. Tutar

| Model | Hesap | Kontrol |
|---|---|---|
| Saatlik | onaylı süre kaydı × oran | açıklamada sır içeren ayrıntı yok |
| Sabit / sürekli danışmanlık | sözleşmedeki aylık tutar | kapsam dışı iş ayrı faturalanır |
| Aşama | aşama gerçekleştiyse aşama tutarı | aşamanın kanıtı (karar, tutanak) |
| Yüzde | sözleşmedeki şart gerçekleştiyse değer × oran | **%25 tavanı** (Av. K. m. 164/2) |

Her matter için ücretin AAÜT altında kalmadığını kontrol et (Av. K. m. 164/4).

### 3. Karşı taraf vekâlet ücreti
Kararla karşı tarafa yüklenen vekâlet ücreti avukata aittir; iş sahibinin borcu nedeniyle **takas ve mahsup edilmez** (Av. K. m. 164/5). Müvekkil faturasına indirim kalemi olarak yazma, ayrı izle.

### 4. Belge
- Her tahsilat için **iki nüsha serbest meslek makbuzu** düzenlenir, bir nüshası müvekkile verilir (VUK m. 236). Elektronik makbuz (e-SMM) usulü bu pakette doğrulanmadı; muhasebeciyle teyit et.
- Makbuz ve fatura açıklaması genel kalır ("hukuki danışmanlık — Eylül 2026"). Dosya içeriği, karşı taraf adı veya strateji yazılmaz (Av. K. m. 36).

### 5. Tevkifat ve KDV
- Ödeyici GVK m. 94'te sayılanlardan biriyse (ör. ticaret şirketi, kamu idaresi, gerçek gelirini beyan eden ticaret veya serbest meslek erbabı) ödeme sırasında tevkifat yapar; makbuzda brüt, tevkifat ve net ayrı gösterilir. Olağan bireysel müvekkil tevkifat yapmaz.
- Tevkifat ve KDV **oranları** doğrulanmadı: `[ORAN — doğrulanmadı]` yaz. Muhasebeci onayı olmadan paket gönderilmez.

### 6. Tahsilat takibi ve temerrüt
- **Temerrüt:** muaccel borçta alacaklının ihtarıyla; ifa günü birlikte belirlenmişse o günün geçmesiyle (TBK m. 117). Sözleşmeye ödeme günü yaz; böylece ihtar gerekmez.
- **Oran:** sözleşmede yoksa faiz borcunun doğduğu tarihteki mevzuata göre belirlenir. Sözleşmeyle kararlaştırılan temerrüt faizi, mevzuattaki oranın **%100 fazlasını** aşamaz (TBK m. 120/1-2).
- **Mevzuattaki oran:** kanuni faiz, TCMB'nin önceki yılın 31 Aralık günü kısa vadeli kredi işlemlerinde uyguladığı reeskont oranının **%80'idir** (3095 m. 1, 16.07.2026 tarihli 7589 sayılı Kanunla değişik). Temerrüt faizi de bu orana göre işler (3095 m. 2/1). Güncel oranı her hesapta TCMB duyurusundan çek.
- **Ticari işlerde avans oranı** (3095 m. 2/2) ve **TTK m. 1530** (ticari işletmeler arasında mal ve hizmet tedarikinde geç ödeme; ihtarsız temerrüt, 30 günlük süreler): avukatlık ücret alacağının "ticari iş" ya da "ticari işletmeler arası tedarik" sayılıp sayılmadığı bu pakette **doğrulanmadı**. Uygulamadan önce içtihatla doğrula; doğrulanmadıysa TBK m. 117-120 ve 3095 m. 1 ile m. 2/1'e göre hesapla.

### 7. Ücret güvenceleri
- Peşin ücret ödenmezse avukat işe başlamak zorunda değildir (Av. K. m. 174/3).
- Hapis hakkı ve rüçhan (Av. K. m. 166).
- Ödenmeyen ücret için dava veya takip kararı: atanan ortak + Yönetici Ortak.

## Çıktı

```markdown
[ÜST BAŞLIK — AYLIK ÜCRET PAKETİ — DAHİLİ — GG.AA.YYYY]

| Matter | Model | Bu ay | AAÜT kontrolü | Tevkifat | Makbuz | Vade | Durum |
|---|---|---|---|---|---|---|---|
| [slug] | saatlik | [TL] | ✓ | evet / hayır | [no] | GG.AA | ödendi / bekliyor / temerrüt |

## Temerrüt uyarıları
- [slug] — vade GG.AA — ihtar: gerekli / gerekmez (TBK m. 117) — faiz esası: [3095 m. 1 ve m. 2/1 | sözleşme]

## Doğrulanmamış kalemler
- [oran / e-SMM / ticari iş niteliği]
```

## Hatalar

- Karşı taraf vekâlet ücretini müvekkilin ücret borcundan düşmek (Av. K. m. 164/5)
- Yüzde ücreti %25 tavanını aşan oranla hesaplamak
- Her müvekkilin tevkifat yapacağını varsaymak
- TTK m. 1530'u doğrulamadan avukatlık ücretine uygulamak
- Makbuz açıklamasına dosya ayrıntısı yazmak

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
