---
name: tax-legal-gib-ozelge-request
description: >
  GİB (Gelir İdaresi Başkanlığı) özelge (mukteza) talep dilekçesi hazırlama: VUK m.
  413 + Genel Tebliğ formatı, benzer özelgeleri ArthurLegal MCP (`tr_`)'den çekme, talep dilekçesi
  taslağı, beklenen cevap süresi (6-9 ay) ve risk yönetimi.
user-invocable: true
---

# GİB Özelge Talep Hazırlama

## Amaç

Vergi mevzuatında belirsiz bir konuda **bağlayıcı yorum** almak için GİB'den özelge talep edilir (VUK m. 413 — mükelleflerin izahat talebi; 395 Sıra No.lu VUK Genel Tebliği (doğrulanmadı)).

**Önemli:**
- GİB özelgesi **sadece talep eden mükellefi** bağlar (kişiye özel)
- Süre: ortalama 6-9 ay
- Olumsuz cevap halinde **idari itiraz yolu var değil**, ama **dava açılabilir**
- **Risk:** GİB olumsuz cevap verirse pozisyon zayıflar

## Destination check

- **Mali İşler iç değerlendirme** → "GİZLİDİR – HUKUK + MALİ İŞLER ÖZELGE TALEP DEĞERLENDİRMESİ"
- **GİB'e sunulacak dilekçe** → resmi format
- **Büyük 4 firma koordinasyon** → "TAX BRIEF"

## Adımlar

### 1. Özelge talep gerekli mi?

Sor:

> Bu konu için özelge talep etmek istiyorsun. Önce:
> 1. Konuda zaten var olan bir özelge var mı? → ArthurLegal MCP (`tr_`)'den ara
> 2. Cevap olumsuz çıkarsa ne kaybedersin? (özelge'siz pozisyon koru → kovuşturma riski; ya da farklı yaklaş)
> 3. Süre kritik mi? (6-9 ay beklemek mümkün mü?)

### 2. ArthurLegal MCP (`tr_`) — benzer özelge tarama

```
tr_kurum_karari_ara(
  kurum="gib",
  query="<konu anahtar kelimeleri>"
)
```

Bulunan benzer özelgelerden:
- GİB'in yaklaşımı (genelde mükellefe karşı muhafazakar mı, esnek mi)
- Atıf edilen mevzuat
- Cevap argümantasyonu

### 3. Dilekçe taslağı

```markdown
GELİR İDARESİ BAŞKANLIĞI
[İlgili Vergi Dairesi Başkanlığı veya GİB Genel Müdürlüğü]
ANKARA / İSTANBUL

Konu: Mukteza Talebi — [konunun kısa tarifi]

Sayın Yetkilisi,

Şirketimiz **[Müvekkil]** [vergi kimlik no, sicil no, adres] olarak,
[konu] hususunda aşağıda açıklanan duruma ilişkin GİB görüşüne ihtiyaç duymaktayız.

I. FİİLİ DURUM

[İşlemin/konunun ayrıntılı tarifi — taraflar, tutar, sıklık, fiziksel veya ekonomik gerçekçilik]

II. HUKUKİ DEĞERLENDİRME

Konuyla ilgili mevzuat:
- [Kanun maddesi]
- [Tebliğ]
- [Genelge]

Şirketimiz görüşü: [...]

III. TALEP

Yukarıda açıklanan duruma ilişkin **GİB görüşünüzü** ve özelgenin tarafımıza
ibrazını talep ederiz.

Saygılarımızla,

[Yetkili imza]
[Müvekkil]
Tarih: GG.AA.YYYY

Ekler:
1. [İlgili belge]
2. [Sözleşme örneği — varsa]
3. [Benzer GİB özelge örnekleri — bizim pozisyonumuzu destekler]
```

### 4. ArthurLegal MCP (`tr_`) — Danıştay vergi içtihatı

Eğer özelge red gelirse dava açılır → şimdiden Danıştay eğilimini bil:

```
tr_ictihat_ara(
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  query="<konu> mukteza GİB",
  date_from="2022-01-01"
)
```

### 5. sektöre-özel notlar

- **[HALKA AÇIK İŞTİRAK] ilgili özelge** — KAP açıklama tetikleyici olabilir (büyük mali etki)
- **[BORU HATTI PROJESİ] işlem özelgesi** — hükümetlerarası anlaşma + GİB ortak görüşü
- **[Ana ortak / ilişkili taraf] intra-group** — özelge talep edersek Maliye'nin dikkati çekiyor, risk

### 6. Risk analizi

Özelge talep etmenin riskleri:
- **Olumsuz cevap = pozisyonu zayıflatır** (sonraki incelemede Maliye bu özelgeyi kullanabilir)
- **Bekleme süresi** (6-9 ay) operasyonel karar geciktirebilir
- **Konunun açığa çıkması** — özelge talep ettiğin işlem GİB'in dikkatini çeker

## Çıktı

```markdown
[ÜST BAŞLIK]

# GİB Özelge Talep Değerlendirme — [Konu]

## ⚠️ İnceleyen notu
- **Tavsiye:** Özelge TALEP EDİLSİN / EDİLMESİN / FARKLI YOL
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (benzer özelge [N]); ArthurLegal MCP (`tr_`) (madde [N])
- **Olumlu/olumsuz cevap olasılığı:** [tahmin]
- **Süre tahmini:** [6-9 ay]
- **Reviewer karar bekleyen:** N adet

## Mevcut özelge taraması (ArthurLegal MCP (`tr_`)'den)
[tablo: özelge no, tarih, konu, sonuç, bizim için anlamı]

## Özelge talep dilekçesi taslağı
[yukarıdaki şablon — doldurulmuş]

## Risk değerlendirmesi
[olumsuz cevap senaryosu + alternatif yollar]

## Sonraki adımlar

> 1. Dilekçeyi GİB'e gönder — Mali İşler imza
> 2. Hukuk dava planı paralel hazırla — olumsuz cevap senaryosuna
> 3. Büyük 4 ile koordinasyon — onların görüşü
> 4. Bekle ve izle — 6-9 ay
> 5. Farklı yol — Büyük 4'ün muktezasız tutarlı uygulaması (risk al)
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
| AZ Vergi Mecellesi, intra-group transfer fiyatlandirmasi — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| transfer pricing ve uluslararasi vergi ogretisi — **ikincil**; ozelge ve Danistay karari yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
