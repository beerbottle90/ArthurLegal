# Regülasyon Haftalık Digest – Şablon

> Her Pazartesi 08:00. Geçen haftanın Resmi Gazetelerini + sektör kurumu kararlarını tarar, etki sınıflar.

---

## Format

```markdown
# Hukuk & Uyum Haftalık Bülteni — [Hafta tarih aralığı]

📅 [GG.AA.YYYY - GG.AA.YYYY] | 📊 Toplam: [N] yayın | 🔴 [N] zorunlu uyum | 🟠 [N] süreç güncellemesi

---

## 🔴 ZORUNLU UYUM (X gün içinde aksiyon)

### [Mevzuat adı + sayı]
**Kaynak:** RG [GG.AA.YYYY] sayı [N] [Mevzuat MCP — GG.AA.YYYY]
**Yürürlük tarihi:** [GG.AA.YYYY]
**Etkilenen birim:** [İK / Finans / IT / Operasyon]

**Özet:** [2-3 cümle özet]

**Şirket etkisi:**
- [Spesifik etki — politika değişikliği gerekli mi? sistem güncellemesi gerekli mi?]
- [Mali etki: TL üzerinden tahmini]

**Aksiyon:**
- [ ] [Belirli aksiyon 1] — Sahibi: [Kim] — Süre: [GG.AA.YYYY]
- [ ] [Belirli aksiyon 2] — ...

---

## 🟠 SÜREÇ GÜNCELLEMESİ (politika revizyonu gerekli)

[Aynı yapı]

---

## 🟡 İZLEME (sektör yorumu / kamuoyu görüşü)

[Aynı yapı]

---

## 🟢 BİLGİLENDİRME

[Tek satır liste — başlık + kaynak]

- [Yayın adı] [RG sayı/tarih] — [tek cümle ne]
- ...

---

## ⚠️ İnceleyen notu

- Kaynaklar: Mevzuat MCP ✓ verify | Resmi Gazete tarama ✓
- Okudum: RG [n] adet (mükerrer dahil), kurum kararları [n] adet
- Flagged: [n] adet [review] etiketli ürün etki gerektiriyor
- Güncellik: [GG.AA.YYYY] itibarıyla teyit
- Önceki haftanın aksiyon takibi: [✓ N tamamlandı / ✗ N gecikti]

---

## 📋 Önceki haftanın aksiyonları (follow-up)

| Aksiyon | Sahibi | Söz verilen | Durum |
|---|---|---|---|
| [örn. politika P12 revizyonu] | [Counsel] | [tarih] | ☐ Devam ediyor / ✓ Tamam / ✗ Gecikti |

---

**Sonraki hafta odaklanılacak:** [özellikle takip edilecek tasarı/karar]
```

---

## Production akışı

1. **Pazartesi 07:00** — Otomatik trigger (cron / agent)
2. **Geçen 7 günün RG'lerini Mevzuat MCP üzerinden tara:**
   - `search_mevzuat(query="<sektör anahtar kelime>", mevzuat_turu="all")`
   - `search_cbk(query="<>")` / `search_cbgenelge(...)`
3. **Sektör kurumu sitelerini web fetch:** EPDK, BDDK, SPK, KVKK Kurul, Rekabet
4. **Politika kütüphanesi diff:** Her yeni regülasyonun şirket politika kataloğundaki ilgili dokümanı belirle
5. **Sınıflandır:** 🔴/🟠/🟡/🟢 — bkz. `regulatory-legal` CLAUDE.md eskalasyon
6. **Önceki haftanın aksiyonlarını çek** (verification-log + tracker)
7. **Teams kanalı veya KEP'e gönder**
8. **Pazartesi 12:00 — toplantıda gözden geçir**

---

## [Müvekkil] Türkiye için özel kaynak listesi (her hafta zorunlu)

### Birincil mevzuat kaynakları
| Kaynak | URL | Periyot | Sorumluluk |
|---|---|---|---|
| Resmi Gazete | https://www.resmigazete.gov.tr | Günlük (09:30) | Tüm grup |
| Mevzuat Bilgi Sistemi | https://www.mevzuat.gov.tr (Mevzuat MCP) | Sürekli | Hukuk |
| TBMM tasarı/teklif takibi | https://www.tbmm.gov.tr | Haftalık | Hukuk |

### Sektör düzenleyici kurum kararları (Mevzuat MCP'de değil — kurum siteleri)
| Kurum | URL | Etki alanı |
|---|---|---|
| **EPDK** | https://www.epdk.gov.tr/Detay/Icerik/3-0-0-94/karar-tarihi | Petrol, doğal gaz, elektrik (Petkim, STAR, İÇAN, dağıtım) — **kritik** |
| **SPK** | https://www.spk.gov.tr/Sayfa/Index/12/1 | Petkim için (BIST: PETKM) |
| **KAP** | https://www.kap.org.tr/tr/Bildirim/PETKM | Petkim özel durum açıklamaları — günlük |
| **Rekabet Kurumu** | https://www.rekabet.gov.tr/tr/Sayfa/Kurul-kararlari | Enerji + petkim birleşme + dikey entegrasyon |
| **KGK** | https://www.kgk.gov.tr | Petkim bağımsız denetim |
| **KVKK Kurulu** | https://www.kvkk.gov.tr/Icerik/4232/Kurul-Kararlari | Veri ihlal kararları, sektörel rehberler |
| **Çevre, Şehircilik ve İklim Değişikliği Bakanlığı** | https://www.csb.gov.tr | ÇED, atık, emisyon — Aliağa kompleksi |
| **ÇSGB** | https://www.csgb.gov.tr | İş izinleri (yabancı çalışan), 6331 ISG |
| **MASAK** | https://www.masak.hmb.gov.tr | Yaptırım + AML rehberleri |
| **TÜRKPATENT** | https://www.turkpatent.gov.tr | Marka/patent ilanları + İlanlar Bülteni |
| **BTK** | https://www.btk.gov.tr | Millenicom, [Müvekkil] Fiber |
| **Sanayi ve Teknoloji Bakanlığı** | https://www.sanayi.gov.tr | Aliağa ÖEB rejimi |

### Uluslararası izleme (Mevzuat MCP kapsamı dışında)
| Kaynak | URL | Etki |
|---|---|---|
| **OFAC Recent Actions** | https://ofac.treasury.gov/recent-actions | Haftalık SDN List + sectoral updates — **kritik** |
| **AB Sanctions Map** | https://www.sanctionsmap.eu/ | AB yaptırım rejimleri |
| **EU Lex (Energy + Climate)** | https://eur-lex.europa.eu/ | CBAM, ETS, Green Deal |
| **UK OFSI Notice Updates** | https://www.gov.uk/government/collections/financial-sanctions-notices-and-news | UK yaptırım güncellemeleri |
| **[Ana ortak / ilişkili taraf] grup compliance bültenleri** | İç dağıtım | Ana ortak grup politikası |

### [Müvekkil]'a özel kategorik etki alanları (her hafta dön)
- 🔴 **EPDK kurul kararları** (Petkim/STAR/İÇAN lisansları, doğal gaz pazar dengesi)
- 🔴 **CBAM güncellemeleri** (Petkim petrokimya ihracatı)
- 🔴 **OFAC SDN List** + **AB 833/2014** ek listeler
- 🟠 **TR İklim Kanunu tasarı** + **karbon vergisi rejimi**
- 🟠 **KVKK m.9 yurt dışı aktarım** SCC + yeterlilik kararı duyuruları
- 🟠 **Petkim KAP açıklamaları** (kendi şirketimiz — içsel bilgi koordinasyonu)
- 🟡 **6331 ISG yönetmelik değişiklikleri** (Aliağa kompleksi)
- 🟡 **TTK + SPK Kurumsal Yönetim** güncellemeleri
- 🟢 **TÜRKPATENT** marka itiraz bültenleri (defansif tarama)
