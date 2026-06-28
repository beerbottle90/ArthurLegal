# Administrative Litigation Practice Profile (Türk Hukuku — Büro tarafı)

*Bu dosya `/administrative-litigation:cold-start-interview` ile doldurulur.*

---

## Kim olduğumuz

`firm-profile.md` oku. Bu eklentiye özel:

**Pratik modeli:** İdari yargı — **müvekkil adına idareye karşı dava + idarenin yaptığı işleme itiraz**
**Aktif idari dava hacmi:** `[DOLDUR — örn. 8-15 aktif dosya]`
**Birincil yakıcı sorun:** `[DOLDUR — örn. EPDK/BDDK gibi sektör regülatörü karar iptal davalarında Ankara'da duruşma günleri trafiği + Danıştay daire farkları]`
**Birincil venue:**
- İdare Mahkemeleri: `[DOLDUR — örn. İstanbul İdare Mh. + Ankara İdare Mh. (sektör kurumları)]`
- BİM (Bölge İdare Mahkemesi): İstanbul / Ankara
- Danıştay: Ankara (temyiz mercii — Danıştay K. m. 23+24+30 istisnaları hariç)

**Sorumlu ortak:** `[DOLDUR — örn. Kıdemli Ortak B (Ankara irtibat)]`

---

## Kim kullanıyor

**Rol:** [DOLDUR]
**Asıl avukat irtibatı:** [DOLDUR]

---

## Entegrasyonlar

| Entegrasyon | Durum | Alternatif |
|---|---|---|
| **Yargı MCP — Danıştay** | ✓ | UYAP/Lexpera |
| **Yargı MCP — KVKK/Rekabet/BDDK/Sayıştay** | ✓ | Kurum siteleri |
| **Mevzuat MCP** (özellikle İYUK, sektör mevzuatı) | ✓ | mevzuat.gov.tr |
| **UYAP** (İdare Mh. + Danıştay) | [DOLDUR ✓/✗] | E-tebligat takip |
| Sektör kurumu sistemleri (EPDK EPYS, EKAP, BDDK e-rapor) | [DOLDUR — sektör bazlı] | Müvekkilden talep |

---

## Müvekkil profili

| Müvekkil tipi | Tipik talep | Tipik mahkeme |
|---|---|---|
| KOBİ / kurumsal | İdari para cezası iptal | İdare Mh. |
| Enerji şirketi | EPDK kararı iptal | Danıştay 13. Daire (enerji) |
| İhale yüklenicisi | KİK kararı + ihale iptali | İdare Mh. + Danıştay 13. Daire |
| ÇED itirazcısı (yatırımcı veya muhalif STK) | ÇED kararı iptal | İdare Mh. — m. 20/A ivedi rejim |
| Veri sorumlusu / KVKK ihlali | KVKK Kurulu para cezası iptal | İdare Mh. (ilk derece) |
| Vergi mükellefi (ek tarhiyat) | → `tax-litigation` plugin'ine yönlendir | |

---

## Vekalet ücreti modeli — idari dava

**Standart yaklaşım:** `[DOLDUR — örn. Götürü matter bazlı (AAÜT × 2x) + başarı bonusu (%15)]`
- **Yürütmenin durdurulması (m. 27)** ayrı talep — ayrı ücret kaydı önerilir
- **Karşı yan vekalet ücreti:** İdare aleyhine hükmedilen vekalet ücreti AAÜT — vekile aittir (Av. K. m. 164/4)

---

## İYUK temel kontrol matrisi

| Konu | Süre | Madde | Sorumlu kontrol |
|---|---|---|---|
| **İdari işlem iptal (genel)** | **60 gün** | İYUK m. 7 | Atanan ortak |
| **Vergi mahkemesi davası** | **30 gün** | İYUK m. 7 | → `tax-litigation` |
| **ÇED davası (ivedi)** | **30 gün** + doğrudan Danıştay temyiz **15 gün** | İYUK m. 20/A | Atanan ortak |
| **Disiplin/idari para cezası** | 60 gün (tebligattan) | İYUK m. 7 | — |
| **Üst makama başvuru** (yapılırsa) | 60 g + 60 g (gizli ret) | İYUK m. 11 | — |
| **Yürütmenin durdurulması** | Dava açılışta veya sonra | İYUK m. 27 | Atanan ortak |
| **Karar düzeltme (BİM)** | 15 gün (tebliğden) | İYUK m. 54 | Atanan ortak |
| **Temyiz (Danıştay)** | 30 gün (BİM kararı tebliğden) | İYUK m. 46 | Atanan ortak |

⚠️ **30 vs. 60 gün ayrımı KRİTİK:** 2021/7331 sayılı K. değişikliği ile vergi 30 g, idare 60 g. **Doğru süreyi kontrol et — yanlış dava yanlış süreyle reddedilir.**

---

## 3 dereceli idari yargı yapısı

```
                İdare Mahkemesi (ilk derece)
                          │
                          │ İstinaf (30 g)
                          ▼
                 BİM (Bölge İdare Mahkemesi)
                          │
                          │ Temyiz (30 g)
                          ▼
                       Danıştay
```

**Danıştay'ın ilk derece görevli olduğu istisnalar (Danıştay K. m. 24):**
- CB Kararnameleri (m. 24/1-a)
- Bakanlıkların düzenleyici işlemleri (m. 24/1-b)
- Ulusal ölçekli sektör kurumlarının (EPDK, BDDK, SPK, Rekabet) **düzenleyici** işlemleri (m. 24/1-c)
- Belirtilen önemli idari işlemler

**Danıştay K. m. 30:** Belirli kamu personel davaları (yüksek yargı vb.) doğrudan Danıştay'da.

Detay: `references/idari-yargi-yapisi-rehberi.md`

---

## Eskalasyon ve onay matrisi

| Karar | Onay yetkisi | Eskalasyon |
|---|---|---|
| İdari dava açma | Atanan ortak + müvekkil yazılı talimat | — |
| **Yürütmenin durdurulması talebi** | Atanan ortak | Yönetici Ortak bilgilendir |
| Sektör kurumu (EPDK/BDDK/SPK) kararına dava | Atanan ortak + Kıdemli Ortak B | — |
| KAP'a açıklama yapan müvekkil için dava (yatırımcı etkisi) | Atanan ortak + Yönetici Ortak | — |
| BİM kararına temyiz | Müvekkil + atanan ortak | — |
| AYM bireysel başvuru (idari uyuşmazlık) | Müvekkil + atanan ortak + Yönetici Ortak | — |

**Otomatik eskalasyon:**
- 🔴 İdari para cezası > `[DOLDUR — örn. 1M TL]` — Yönetici Ortak
- 🔴 Müvekkilin lisansı (EPDK/BDDK/SPK) iptal riski — Yönetici Ortak + Ortaklar Kurulu
- 🔴 ÇED ret + büyük yatırım — Yönetici Ortak

---

## EPDK proaktif dialog modeli

Sektör kurumlarıyla (özellikle EPDK) dava öncesi **proaktif dialog** modeli:
1. **İdari itiraz** (60 g — İYUK m. 11) — değerlendirilebilir mi?
2. **Kurul'a görüş yazısı** sunma — kurulun dava açmadan önce kendi kararını revize etme ihtimali
3. **Sektör platformu** (örn. EPDK Müşavir Kurulu) görüş alışverişi
4. Hiçbiri çalışmazsa **dava açma** + paralel **yürütmenin durdurulması**

Detay: `references/epdk-rehberi.md`

---

## Outputs

**İç çalışma notu:**
```
AVUKATLIK K. m. 36 – VEKİL-MÜVEKKİL YAZIŞMASI – DAHİLİ VE GİZLİDİR
[Büro Adı] – Matter ID: [matter-slug] – [Müvekkil rumuz]
İdari işlem: [tebligat tarihi / işlem no]
Süre bitiş: [GG.AA.YYYY] — KRİTİK
Hazırlayan: Claude – avukat incelemesi öncesi
```

**Mahkemeye dilekçe taslağı:** Üst başlığı KALDIR; "TASLAK – İMZA BEKLİYOR" ekle. **Yürütmenin durdurulması talebi varsa dilekçenin başında ayrı paragraf.**

### Atıf disiplini

- `[Yargı MCP — danistay — [Daire] — GG.AA.YYYY]`
- `[Yargı MCP — kvkk-kurulu / rekabet / bddk — GG.AA.YYYY]`
- `[Mevzuat MCP — İYUK m. X — GG.AA.YYYY]`
- `[Resmi Gazete — sayı/tarih]`
- `[Sektör kurumu — EPDK/BDDK — karar no — GG.AA.YYYY]` (kurum sitesinden çekildiyse)

---

## Karar duruşu

İdari yargıda **dava açma kararı** çoğu zaman müvekkilin ticari/operasyonel hesabını içerir (örn. yatırım sürmesi, lisans korunması). Bu yüzden:
- Hukuki başarı şansı (`[review]` etiketli)
- **Operasyonel/ticari maliyet** (müvekkille birlikte değerlendirilir)
- **Yürütmenin durdurulması alma şansı** (genelde sınırlı — şartlar dar)

**Yürütmenin durdurulması — İYUK m. 27 şartları:**
1. İdari işlemin uygulanması halinde **telafisi güç veya imkânsız zararlar doğacak**, ve
2. İdari işlem **açıkça hukuka aykırı** olmalı — **iki şart birlikte**

Çoğu davada yürütmenin durdurulması REDDEDİLİR. Müvekkili gerçekçi beklenti ile bilgilendir.

---

## Shared guardrails

`dispute-litigation.md` ile aynı (Üç değer kuralı, güncellik tetikleyici, hassas karar ön-kontrol, hedef kontrolü, doğrulama günlüğü). Tekrarlamıyorum — okumak için: `tr-overlay/profiles/dispute-litigation.md`.

**İlave guardrail (idari yargı özel):**

**Süre ön-kontrol (her matter intake'inde):**
- Hangi süre uygulanır? (60 g / 30 g / m. 20/A 30 g)
- Süre başlangıç tarihi nedir? (tebliğ tarihi vs. ıttıla tarihi)
- Süre dolmadan kaç gün var? (< 7 gün ise 🔴 acil)

---

## Matter workspaces

`dispute-litigation.md` ile aynı — cross-matter OFF zorunlu.

Konum: `~/.claude/plugins/config/claude-for-legal-law-firm/matters/<müvekkil-slug>__<matter-slug>/`

---

## Seed davalar

| Dava | Müvekkil | İdare/Kurum | İşlem no | Süre kalan | Not |
|---|---|---|---|---|---|
| [DOLDUR] | | | | | |

---

*Re-run interview:* `/administrative-litigation:cold-start-interview --redo`
