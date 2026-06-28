# Rusya Mevzuatı — Kullanım Rehberi (v1.7.0)

> **⚠️ KULLANIM KAPSAMI:** Bu rehber YALNIZCA yaptırım uyumu ve karşı taraf durum tespiti içindir.
> Rusya hukuku yönetimli işlem desteği bu asistanın kapsamı dışındadır.
> **Auth:** Yok
> **⚠️ 2026-06-28 testi:** `pravo.gov.ru` / `publication.pravo.gov.ru` bu ortamdan **ECONNREFUSED** (geo-block). **Çalışan alternatif → consultant.ru:** `https://www.consultant.ru/document/...` (Rus mevzuat tam metni, ✅ test edildi). KYC/yaptırım amacıyla **OpenSanctions API birincil** kalır.
> **[ŞİRKET ADI] bağlamı:** Rus karşı taraf taraması, OFAC/AB yaptırım listesi kontrolü, önceki sözleşme yükümlülükleri

---

## ⚠️ ZORUNLU UYARI

Azerbaycan ana ortaklı [ŞİRKET ADI] için Rusya hukuku temas eden her analizde:
1. **OpenSanctions API** ile karşı taraf taraması zorunlu (önce)
2. **OFAC SDN + AB 269/2014 + AB 833/2014** kontrolleri
3. **CAATSA m.232** — Rus enerji sektörüyle belirli işlemler yaptırım riski
4. Hukuki görüş Counsel + Compliance ([UYUM DİREKTÖRÜ]) onayı şart

---

## 1. pravo.gov.ru — Resmi Rus Mevzuatı

**Resmi Rus federal normatif akt yayın platformu. Ücretsiz.**

```
GET http://publication.pravo.gov.ru/Document/View/{BELGE_NUMARASI}
```

Arama:
```
WebFetch("http://pravo.gov.ru/proxy/ips/?searchall={encoded_sorgu}",
         "Arama sonuçlarını listele")
```

**[ŞİRKET ADI] için kritik Rus mevzuatı (yaptırım/karşı taraf araştırması):**

| Mevzuat | İçerik | Kullanım |
|---|---|---|
| ГК РФ (Sivil Kanun) | Sözleşme hukuku | Önceki sözleşme yorumu |
| ФЗ-57 (Stratejik yatırım) | Yabancı yatırım kısıtlamaları | Devralma kontrolü |
| ФЗ-44 (Kamu ihalesi) | Devlet alımları | Devlet şirketi ilişkisi tespiti |
| ФЗ-115 (AML/KYC) | Kara para aklama | Karşı taraf uyum durumu |

**Kodlara genel erişim (Konsultant-benzeri portal):**
```
WebFetch("https://www.consultant.ru/document/cons_doc_LAW_5142/",
         "Rus Sivil Kanunu temel sözleşme hükümleri")
```

---

## 2. Rusya Şirket Kaydı (ЕГРЮЛ/FNS)

Rusya Federal Vergi Servisi şirket kaydı — **karşı taraf kimlik tespiti için kritik:**

```
WebFetch("https://egrul.nalog.ru/index.html?query={OGRN_veya_sirket_adi}",
         "Şirket kayıt bilgileri, kurucu yapısı, yönetim")
```

OGRN/INN ile doğrudan:
```
WebFetch("https://egrul.nalog.ru/",
         "{Rus şirket adı} için OGRN/INN ve kayıt durumunu çıkar")
```

---

## 3. Tahkim / Mahkeme Kararları

**kad.arbitr.ru** — Rusya Tahkim Mahkemeleri dava kayıtları:
```
WebFetch("https://kad.arbitr.ru/kad/search?number={DAVA_NO}",
         "Dava durumu ve taraflar")
```

**Dikkat:** Bu dava kayıtları Rusça olup şirketin aktif dava listesini gösterir — KYC/durum tespiti için kullanılır.

---

## 4. Yaptırım Araştırması (Asıl Amaç)

Bu rehberin [ŞİRKET ADI] açısından **asıl kullanım amacı** Rusya değil, Rusya bağlantılı varlıkların yaptırım kontrolüdür. Birincil araç: `socar-yaptirim-tarama-rehberi.md`

Ek kontrol kaynakları:
```
# AB yaptırım arama
WebFetch("https://www.sanctionsmap.eu/api/v1/sanction?name={ad}&lang=en",
         "AB yaptırım listesinde sorgula")

# OFAC SDN list (statik liste, OpenSanctions zaten kapsıyor)
# → opensanctions-rehberi.md'ye bak

# BM yaptırım listesi
WebFetch("https://scsanctions.un.org/search?q={ad}",
         "BM Güvenlik Konseyi yaptırım listesinde sorgula")
```

---

## 5. Rusya Enerji Sektörü — Özel Not

Rosneft, Gazprom, Lukoil vd. Rus enerji şirketleri:
- **AB 833/2014** ve ek tüzükler: enerji sektörü işlemleri kısıtlama kapsamında
- **CAATSA Bölüm 232**: Rus boru hattı projelerine "önemli işlem" — ABD yaptırım riski
- **OFAC Sectoral Sanctions** (SSI): enerji, finans, savunma sektörleri
- OpenSanctions `POST /match/default` ile her Rus şirketi için `schema=Company, country=ru` sorgusu yap

---

## Atıf formatı

```
[RU Mevzuat — {Kanun adı/ФЗ no} md.{no} — pravo.gov.ru — GG.AA.YYYY]
[ЕГРЮЛ — {şirket adı} OGRN:{no} — nalog.ru — GG.AA.YYYY]
[OpenSanctions — {şirket} — score:{skor} — GG.AA.YYYY]
```

---

## Kullanım dışı bırakılan senaryolar

❌ Bu rehberi şu amaçlarla KULLANMA:
- Rusya hukukunun yönetim hukuku olduğu sözleşme taslağı
- Rusya'da ticaret yapmayı kolaylaştıran hukuki görüş
- Rusya mahkemelerinde strateji geliştirme

✅ Bu rehberi şu amaçlar için kullan:
- Rus karşı taraf kimliği + sahiplik yapısı tespiti
- Yaptırım listesi kontrolü (ön adım olarak)
- Mevcut sözleşme yükümlülükleri yorumu (zorunlu halde)
- Önceki işlemlerden doğan tazminat/fesih analizi

*Son güncelleme: 29.05.2026 — v1.7.0.*
