# İş Hukuku – Pratik Profili (Türkiye Overlay)

> Hedef: `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`

---

## Kim olduğumuz

Bkz. `company-profile.md`. Bu eklentiye özel:

**Toplam çalışan sayısı:** [DOLDUR — toplam çalışan sayısı] ([doğrudan çalışan sayısı] + yükleniciler). Merkez ofis [DOLDUR], [Üretim Sahası] [DOLDUR], kalan dağıtım şirketleri + diğer iştirakler.
**Toplu iş sözleşmesi (TİS) var mı:** **EVET — birden fazla sendika.** [Halka Açık İştirak] için tarihsel olarak **[Sektör Sendikası]** ([Konfederasyon] üyesi) ile TİS aktif. [Rafineri Tesisi] ve diğer iştirakler için ek aktif sendika ilişkileri mevcut. [Elektrik İştiraki] devri sonrası (yakın geçmişte) elektrik üretim sektörü TİS muhatabı (varsa) eklendi. **Çoklu TİS = paralel pazarlık takvimi + farklı maddi rejim** = hukuki risk yüksek. *Not: [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] dağıtım şirketlerinin TİS muhatapları devir sürecinde devralan şirkete geçer.*
**Yabancı çalışan var mı:** **EVET — [DOLDUR — çalışma izinli yabancı çalışan sayısı].** Çoğunluk yurtdışı ana ortak kökenli (üst yönetim + teknik uzmanlık + köprü kadroları). 6735 Uluslararası İşgücü Kanunu kapsamında çalışma izinleri yıllık takip. ÇSGB ile yoğun temas. Diğer ülkeler: AB/ABD teknik uzmanlar (rafineri, mühendislik), CIS ülkeleri.
**Beyaz/mavi yaka dağılımı:** Karma. İstanbul ofis ağırlık beyaz yaka (kurumsal, ~300); [Üretim Sahası] rafineri+petrokimya ağırlık mavi yaka (operasyon, vardiya, [DOLDUR]); dağıtım şirketlerinde saha + ofis karma.
**İK platformu:** **SAP SuccessFactors** (kurumsal bulut HRIS). Çalışan veri kaynağı tek noktada — KVKK çalışan verisi + privacy-legal eklentisiyle entegre değerlendir.

---

## Türk iş hukuku zemini

### Temel mevzuat

- **4857 sayılı İş Kanunu** — özel sektör çalışanları
- **6098 TBK** — hizmet sözleşmesi genel hükümleri (m. 393-447)
- **5510 SGK Kanunu** — sosyal güvenlik
- **6356 Sendikalar ve Toplu İş Sözleşmesi Kanunu**
- **6331 İş Sağlığı ve Güvenliği Kanunu**
- **6698 KVKK** — çalışan kişisel verileri (özel nitelikli: sağlık verisi)
- **6701 Türkiye İnsan Hakları Eşitlik Kurumu** — eşit muamele
- **4904 İş-Kur Kanunu** — yabancı çalışan çalışma izinleri (6735)

### "Çalışan / bağımsız sözleşmen" sınıflandırma testi

Türk hukuku "ABC test" gibi formel test kullanmaz; **işlevsel bağımlılık** kriteri uygulanır:

1. **Kişisel iş ifası** (TBK 393) — başka birine devredemez mi?
2. **Bağımlılık unsuru** — talimat, yer, zaman, ekipman işverene mi ait?
3. **Ücret düzenliliği** — sabit ücret + sosyal haklar mı?
4. **Ekonomik bağımlılık** — gelirin tamamına yakını tek kaynaktan mı?

Yargıtay 9. ve 22. Hukuk Daireleri içtihatları bağlayıcı — **freelance / consultant / IT contractor**'lar büyük ihtimalle gerçek çalışan sayılır. Yanlış sınıflandırma riski: geriye dönük SGK + kıdem + ihbar + fazla mesai + KDV iadesi.

### Fesih çerçevesi

| Fesih türü | Şart | Tazminat |
|---|---|---|
| **İhbarlı fesih (m. 17)** | Bildirim süresi (2-8 hafta) + neden istenmez ≤30 işçi VEYA <6 ay kıdem | İhbar tazminatı (bildirim verilmezse) + kıdem |
| **Geçerli neden ile fesih (m. 18-21)** | İşletme/işyeri gereği VEYA işçi yetersizliği/davranışı; ≥30 işçi + ≥6 ay kıdem koşulunda | Kıdem + ihbar; itirazda işe iade davası |
| **Haklı neden (m. 24/25)** | Sağlık/ahlak/kanun dışı durumlar | Sebebe göre kıdem VAR/YOK |
| **Karşılıklı anlaşma** | İkale sözleşmesi | Genelde kıdem + ihbar + makul ek |
| **İstifa** | İşçi iradesi | Yok |

**Kritik:** ≥30 işçi + ≥6 ay kıdemli çalışan için **işe iade davası riski** ve **2-4 ay arası boşta geçen süre + 4-8 ay tazminat** sonucu çıkabilir. Her fesih bu eşik üstünde değerlendirilmeli.

### KVKK + iş ilişkisi özel hükümleri

- **m. 5/2-f hukuki yükümlülük** ile aydınlatma yapılır (SGK bildirimleri vs.)
- **m. 5/2-c sözleşmenin kurulması/ifası** kapsamında özlük verisi işlenir
- **m. 6 özel nitelikli veri:** Sağlık raporu, ceza sicili, sendika üyeliği — **açık rıza şart** veya kanuni istisna
- **Aydınlatma metni iş başlangıcında** + **VERBİS'te "çalışan" kategorisi** zorunlu
- E-posta/keystroke logging gibi izleme: **önceden aydınlatma + meşru menfaat dengesi** (KVKK Kurulu kararları)

### İç soruşturma — TR pratiği

- Türk hukukunda US-tarzı "internal investigation privilege" yok.
- Soruşturma kayıtları **yargısal süreçte delil olarak istenebilir**.
- Çalışan dinleme süreci **disiplin yönetmeliği + savunma hakkı (m. 19)** ile yapılır.
- Etik hat / Hotline raporları KVKK kapsamında özel veri içerebilir — anonim ihbarlarda **ihbar edenin kimliği saklı tutulur**, **ihbar edilen hakkında özel veri işleme rejimine girilir**.

### Yabancı çalışan

- **6735 Uluslararası İşgücü Kanunu** — çalışma izni Çalışma Bakanlığı'ndan online
- İzin başvurusu: işveren tarafı, çalışan dışarıdaysa konsolosluk vize
- İstisnalar: Mavi kart sahipleri (Türk vatandaşlığı çıkışlı), uluslararası kuruluş çalışanları
- Süre: ilk yıl 1 yıl → 2 yıl → 3 yıl → süresiz (8 yıl koşulu)

---

## Çıktı standardı

Bkz. `commercial-legal.md`. Ek olarak:

- **Sayısal hesaplar tablo halinde:** kıdem tazminatı tavan kontrolu (2026: [Mevzuat MCP'den teyit]), günlük ücret hesabı, son brüt vs giydirilmiş brüt, ihbar süresi tablosu.
- **İçtihat atıfları:** Yargıtay 9. HD / 22. HD esas/karar, tarih. **Yargı MCP** üzerinden çekildiyse `[Yargı MCP — yargitay — GG.AA.YYYY]`; çekilmediyse `[model bilgisi — doğrulayın]`. Yargı MCP `mcp__claude_ai_Yargi_MCP__search_yargitay_decisions` araçları ile.

---

## Eskalasyon

- 🔴 İşe iade riski yüksek fesih, **üretim kompleksinde ölümlü-yaralanmalı kaza (6331 ISG)**, sendika ([Sektör Sendikası]) toplu eylem talebi, **[Halka Açık İştirak]'i etkileyebilecek olay (KAP açıklama riski)** → Hukuk, Uyum ve Kurumsal Yönetişim Başkanı ([CLCO]) + İK Başkanı (Mammadova)
- 🟠 ≥30 işçi sınıfında fesih, taciz/mobbing iddiası, KVKK çalışan veri ihlali, **yabancı yönetici çalışma izni yenileme/iptal riski** → Counsel + İK Direktörü
- 🟡 Standart fesih, ihbar süresi hesabı, izin uyuşmazlığı, kıdem hesabı → Sözleşmeler/İK yöneticisi

**Özel durumlar (otomatik eskalasyon):**
- **TİS müzakeresi açılması** ([Sektör Sendikası] veya başka sendika) — toplu pazarlık süreci başlangıcı GC + İK Başkanı + CEO
- **üretim kompleksinde grev ihbarı** veya iş güvenliği denetim sonucu — anında üst yönetim
- **Ölümlü iş kazası** — Cumhuriyet Savcılığı + ÇSGB + Aile Bakanlığı süreçleri paralel başlar; hukuki süreç dış vekil dahil

---

## Mevzuat MCP kullanım örüntüleri

Bu eklentide en sık aranan kaynaklar:

- `search_kanun(mevzuat_adi="4857")` — İş Kanunu
- `search_kanun(mevzuat_adi="6098")` — TBK
- `search_kanun(mevzuat_adi="6356")` — Sendikalar ve TİS
- `search_kanun(mevzuat_adi="6331")` — ISG
- `search_kurum_yonetmelik(kurum="Çalışma")` — ÇSGB yönetmelikleri
- `search_within_kanun(...)` — Belirli madde aramaları

Her atıfta `[Mevzuat MCP — GG.AA.YYYY]` etiketi.

## Yargı MCP kullanım örüntüleri (içtihat)

- `search_yargitay_decisions(daire="9. Hukuk Dairesi", arananKelime="işe iade")` — iş davaları
- `search_yargitay_decisions(daire="22. Hukuk Dairesi", arananKelime="...")` — toplu iş + sendika
- `search_yargitay_decisions(daire="4. Hukuk Dairesi", arananKelime="iş kazası tazminat")` — bedensel zarar
- `search_yargitay_decisions(daire="Ceza Genel Kurulu", arananKelime="6331 ISG")` — ölümlü kaza
- `search_anayasa_bireysel_basvuru(arananKelime="çalışma hakkı")` — temel hak boyutu
- `get_yargitay_decision_text(...)` — Tam metin çek

Her atıfta `[Yargı MCP — yargitay/aym — GG.AA.YYYY]` etiketi.
