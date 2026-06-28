# Sırbistan Hukuku — Kullanım Rehberi (WebFetch yöntemi)

> **Custom MCP server YOK** — Sırbistan hukuku için 3 açık erişim kaynağı WebFetch
> ile kullanılır. Bu rehber, Claude'un `WebFetch` aracını Sırbistan mevzuatı ve
> mahkeme kararlarıyla birlikte kullanma prosedürünü tanımlar.
>
> **Durum:** ✅ Açık erişim — API anahtarı gerekmez.
> **Dil:** Sırpça (Latin yazısı) birincil; Anayasa Mahkemesi kararlarında İngilizce mevcut.
>
> **Bu rehber neden gerekli?** Balkan enerji ticaret koridoru (doğalgaz, petrol ürünleri),
> Srbijagas/EPS gibi Sırp enerji şirketleriyle potansiyel tedarik sözleşmeleri, Sırbistan
> hukukunu uygulanacak hukuk seçen çapraz sınır işlemler ve Sırbistan'ın AB üyelik süreci
> kapsamındaki mevzuat uyumu takibi.

---

## Kaynak haritası — 3 kaynak, 2 kullanım türü

| Kaynak | Tür | İçerik | Dil | Öncelik |
|--------|-----|--------|-----|---------|
| paragraf.rs | WebFetch | Tüm Sırbistan mevzuatı, tam metin | SR (Latin) | **P0 — mevzuat** |
| ustavni.sud.rs | WebFetch | Anayasa Mahkemesi kararları | SR + EN | P1 — kararlar |
| CODICES (Venice Commission) | WebFetch | Anayasa Mah. kararları İngilizce özet | EN + FR | P1 — kararlar EN |

---

## 1. paragraf.rs — Birincil Mevzuat Kaynağı

**Kaynak:** Paragraf Lex d.o.o. (Belgrade)
**URL:** `https://www.paragraf.rs/propisi/`
**Lisans:** Ücretsiz kamu erişimi (kayıt gerektirmez)
**İçerik:** Tüm Sırbistan kanun ve yönetmelikleri, yürürlükteki metinler, PDF indirme
**Dil:** Sırpça — Latin yazısı (srpski latinica)
**Güncelleme:** Resmi Gazete (Službeni glasnik RS) değişikliklerine göre sürekli

### URI şeması

```
https://www.paragraf.rs/propisi/{zakon-adi}.html
```

Belge adı Sırpça kanun adından türetilir: boşluklar alt çizgi `_`, özel karakterler (`š`, `ć`, `č`, `ž`, `đ`) ASCII karşılıklarına dönüştürülür.

### WebFetch kullanımı

```
WebFetch:
  URL: https://www.paragraf.rs/propisi/{zakon-adi}.html
  prompt: "[Kanun adı] tam metnini getir: yürürlük tarihi, Resmi Gazete referansı ve
           ilgili maddeler"
```

**Arama yapılamıyor** — doğrudan URL gerekir. Kanun adını bilmiyorsan önce Google ile
`site:paragraf.rs "{konu}"` araması yap, URL'yi al, sonra WebFetch ile çek.

---

## 2. Müvekkil için hangi kanunlar?

| Konu | Sırpça Kanun Adı | paragraf.rs URL | Olası Bağlantı |
|------|-----------------|-----------------|-----------------|
| **Sözleşme hukuku** | Zakon o obligacionim odnosima | `zakon_o_obligacionim_odnosima.html` | Governing law SR seçilmişse |
| **Şirket hukuku** | Zakon o privrednim društvima | `zakon_o_privrednim_drustvima.html` | SR bağlı ortaklık / JV |
| **İş hukuku** | Zakon o radu | `zakon_o_radu.html` | SR çalışanlar |
| **Enerji** | Zakon o energetici | `zakon_o_energetici.html` | Srbijagas/EPS tedarik sözleşmeleri |
| **Kişisel Veri (GDPR-uyumlu)** | Zakon o zaštiti podataka o ličnosti | `zakon_o_zastiti_podataka_o_licnosti.html` | SR KVKK eşdeğeri |
| **Tahkim** | Zakon o arbitraži | `zakon_o_arbitrazi.html` | SR seated tahkim, NY Konvansiyonu |
| **Rekabet** | Zakon o zaštiti konkurencije | `zakon_o_zastiti_konkurencije.html` | Piyasa davranışı |
| **Vergi (KV)** | Zakon o porezu na dobit pravnih lica | `zakon_o_porezu_na_dobit_pravnih_lica.html` | SR kurumlar vergisi + TP |
| **KDV** | Zakon o porezu na dodatu vrednost | `zakon_o_porezu_na_dodatu_vrednost.html` | SR KDV |
| **Yabancı Yatırım** | Zakon o stranim ulaganjima | `zakon_o_stranim_ulaganjima.html` | [Müvekkil] Türkiye → SR yatırım |
| **Yaptırım / Embargo** | Zakon o ograničavanju raspolaganja imovinom | ilgili URL | OFAC/AB ile ilişki |
| **Çevre** | Zakon o zaštiti životne sredine | `zakon_o_zastiti_zivotne_sredine.html` | Çevre mevzuatı |

### Önemli Sırp hukuk terimleri

| Sırpça | Türkçe |
|--------|--------|
| Zakon | Kanun |
| Uredba | Yönetmelik (Hükümet) |
| Pravilnik | Yönetmelik (Bakanlık) |
| Sl. glasnik RS | Resmi Gazete Sırbistan |
| Privredna društva | Ticaret şirketleri |
| Obligacioni odnosi | Borç ilişkileri |
| Arbitraža | Tahkim |
| Ugovor | Sözleşme |
| Sporazum | Anlaşma |
| Tužba | Dava |

---

## 3. Tipik kullanım pattern'ları

### 3.1 Sözleşme governing-law incelemesi (Sırbistan hukuku seçilmişse)

```
ADIM 1: Borçlar Kanunu'ndan ilgili hükümleri getir
  WebFetch: https://www.paragraf.rs/propisi/zakon_o_obligacionim_odnosima.html
  → Sözleşme serbestisi, sözleşme ihlali, tazminat maddelerini oku

ADIM 2: Sektöre özel kanunu getir (enerji ise zakon_o_energetici.html)

ADIM 3: Atıf ekle → [SR Mevzuat — paragraf.rs — {Kanun adı} — GG.AA.YYYY]
```

### 3.2 Srbijagas/EPS enerji tedarik sözleşmesi

```
ADIM 1: Enerji Kanunu'nu getir
  WebFetch: https://www.paragraf.rs/propisi/zakon_o_energetici.html
  → Lisans, tedarik, piyasa katılımcıları, gizlilik maddeleri

ADIM 2: Şirket Kanunu'ndan karşı taraf temsil yetkisi kontrol
  WebFetch: https://www.paragraf.rs/propisi/zakon_o_privrednim_drustvima.html

ADIM 3: OpenSanctions → Sırp karşı taraf yaptırım durumu
```

### 3.3 GDPR uyumu (Sırbistan KVKK eşdeğeri)

```
ADIM 1: Kişisel Veri Kanunu'nu getir
  WebFetch: https://www.paragraf.rs/propisi/zakon_o_zastiti_podataka_o_licnosti.html
  → Veri aktarımı koşulları (Madde 64+), yurt dışı transfer

ADIM 2: TR KVKK + SR Kişisel Veri Kanunu paralel yükümlülükleri değerlendir
  (SR, AB ile yeterlilik kararı aldığından GDPR eşdeğeri)
```

### 3.4 Anayasal haklar / mülkiyet ihtilafı

```
ADIM 1: ustavni.sud.rs'den ilgili kararı bul
  WebFetch: https://ustavni.sud.rs/eng/case-law
  → Mülkiyet hakkı, sözleşme özgürlüğü, yabancı yatırımcı haklarına dair kararlar

ADIM 2: Gerekirse CODICES/Venice Commission üzerinden EN özet
  WebFetch: https://www.venice.coe.int/webforms/pages/?p=02_CODICES&lang=EN
```

---

## 4. ustavni.sud.rs — Anayasa Mahkemesi Kararları

**URL:** `https://ustavni.sud.rs/eng`
**Lisans:** Hükümet portalı, kamu erişimi açık
**İçerik:** Anayasa Mahkemesi kararları — norm denetimi + bireysel başvurular
**Dil:** Sırpça birincil; İngilizce versiyon (`/eng/`) mevcut
**Yeniden tasarım:** Şubat 2024 (Council of Europe + AB desteğiyle)

### WebFetch kullanımı

```
WebFetch:
  URL: https://ustavni.sud.rs/eng/case-law
  prompt: "Mülkiyet hakkı / yabancı yatırımcı / ticari uyuşmazlık konularındaki
           kararları listele"
```

> ⚠️ **Not:** vk.sud.rs (Yargıtay) 2025 itibarıyla "sistem bakımda" durumunda —
> erişilemezse CODICES üzerinden içtihat araştır. Durum değişirse bu notu güncelle.

---

## 5. CODICES — Venice Commission (Venedik Komisyonu)

**URL:** `https://www.venice.coe.int/webforms/pages/?p=02_CODICES&lang=EN`
**Lisans:** Avrupa Konseyi, açık erişim
**İçerik:** Sırbistan Anayasa Mahkemesi kararları — EN + FR özetler
**Güncelleme:** İki haftada bir

### WebFetch kullanımı

```
WebFetch:
  URL: https://www.venice.coe.int/webforms/pages/?p=02_CODICES&lang=EN
  prompt: "Serbia constitutional court decisions on property rights / foreign investment ara"
```

---

## 6. Atıf disiplini

Bu rehberdeki kaynaklardan alınan atıflar **mutlaka** etiketli olmalı:

- `[SR Mevzuat — paragraf.rs — {Kanun adı SR} — GG.AA.YYYY]` — Sırbistan mevzuatı
- `[SR Anayasa Mah. — ustavni.sud.rs — {karar no} — GG.AA.YYYY]` — Anayasa Mahkemesi
- `[SR Anayasa Mah. — CODICES — {karar adı} — GG.AA.YYYY]` — CODICES üzerinden

**Asla:** Çekmediğin Sırbistan hukuku kaynağına atıf koyma.
→ `[model bilgisi — doğrulayın]` kullan.

**Dil notu:** paragraf.rs metinleri Sırpça (Latin yazısı). Alıntıda Sırpça orijinal +
Türkçe/İngilizce çevirisi birlikte ver. Kritik hukuki metinlerde `[review]` ekle.

---

## 7. Sınırlamalar

- **Yalnızca Sırpça (Latin):** paragraf.rs tam metin çevirisi modele kalır;
  kritik hukuki metinlerde `[review]` + uzman hukuk çevirisi önerisi ekle.
- **Arama yok:** paragraf.rs'de arama API'si mevcut değil; kanun adı bilinmiyorsa
  Google `site:paragraf.rs` ile URL bul.
- **Ticari içtihat sınırlı:** vk.sud.rs (Yargıtay) 2025'te erişilemez durumda;
  ticari içtihat için paragraf.rs sudska-praksa kısmi erişim veya PKLex (ücretli).
- **AB üyelik süreci:** Sırbistan AB aday ülkesi; mevzuat hızlı değişiyor,
  güncellik için paragraf.rs yayın tarihini kontrol et.
- **Cyrillics:** Resmi Gazete (Sl. glasnik) bazen Kiril yazısı kullanır;
  paragraf.rs Latin transliterasyonunu tercih eder.
- **paragraf.rs URL tahminleme:** URL pattern tahmin edilebilir ama her zaman
  doğru çalışmaz; 404 gelirse kanunun alternatif adını dene.

---

## 8. [Müvekkil] Sırbistan hukuku kullanım disiplini

1. **Sırbistan governing-law sözleşmesi** → paragraf.rs'den ZOO (Borçlar Kanunu) +
   sektöre özel kanunu getir. Türk hukuku seçilmişse → SR analizi karşılaştırmalı arka plan.

2. **Sırp enerji karşı tarafı** (Srbijagas, EPS, NIS) → OpenSanctions + Zakon o
   energetici + Zakon o privrednim društvima (şirket yapısı) birlikte.

3. **Kişisel veri aktarımı (SR → TR)** → Zakon o zaštiti podataka o ličnosti; SR AB
   yeterlilik kararı aldığından GDPR mekanizmaları geçerli. KVKK + SR kanunu paralel.

4. **Tahkim klozu — Sırbistan seated** → Zakon o arbitraži + NY Konvansiyonu + [Müvekkil]
   Türkiye icra analizi (MÖHUK 5718 m. 54).

5. **Dil notu:** [Müvekkil]'ın Sırp karşı taraflarıyla yazışması İngilizce ya da Türkçe.
   Sırpça mevzuat alıntısı → SR orijinal + EN/TR çeviri birlikte.

---

## Versiyon disiplini

- Bu rehber **v1.8.3** (*Sırbistan + Çek Cumhuriyeti Entegrasyonu*) ile eklendi.
- Kaynaklar 31.05.2026 tarihli araştırmaya dayanır.
- paragraf.rs WebFetch'i test edildi ✅ — Borçlar Kanunu, Şirketler Kanunu, İş Kanunu,
  Enerji Kanunu, Kişisel Veri Kanunu, Tahkim Kanunu başarıyla çekildi.
- vk.sud.rs erişilemez (2025) — durum değişirse güncelle.

---

*Son güncelleme: 31.05.2026 — v1.8.3. Sırbistan hukuku WebFetch entegrasyon prosedürü; 3 kaynak, açık erişim.*
