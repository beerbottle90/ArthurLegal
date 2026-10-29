---
name: litigation-legal-evidence-collection
description: >
  Dava açılması veya beklenmesi durumunda delil toplama protokolü: Türk hukuku
  legal hold (ABD doktrini DEĞİL — TBK + TTK + KVKK üzerinden), UYAP belge çekme
  listesi, tanık listesi (HMK m. 240), bilirkişi (HMK m. 266), keşif (HMK m. 288),
  delil tespit davası (HMK m. 400). Dış vekille koordineli.
user-invocable: true
---

# Evidence Collection — Delil Toplama Protokolü

## Matter context

Matter workspaces ON. Bu skill aktif bir matter'da çalışır:

> Hangi dosya için delil topluyoruz? Aktif matter: [slug] veya yeni `/arthurlegal:litigation-legal-case-intake new`?

## Destination check

- **İç hukuk müşaviri raporu** → "GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ"
- **Dış vekile transmit** → "AVUKATLIK K. m. 36 — DIŞ VEKİL BRIEF" üst başlığı
- **Mahkemeye delil dilekçesi taslağı** → üst başlık çıkar, "TASLAK" ekle

## Amaç

İki senaryo:

1. **Dava açılmış veya başlama beklentisi yüksek** → derhal **delil koruma** (Türk versiyonu legal hold)
2. **Mahkemede delil sunumu hazırlık** → HMK delil çekme prosedürleri (m. 219 vd.)

## A. DELİL KORUMA (Litigation Hold)

### ABD doktrini Türkiye'de DOĞRUDAN yok

⚠️ **Önemli:** ABD "litigation hold" doktrini doğrudan Türk hukukunda yoktur. Buna karşı şu kanuni ödevler vardır:

| Hukuki temel | Yükümlülük |
|---|---|
| **TCK m. 281** | Suç delilini yok etme — cezai sorumluluk |
| **TBK m. 50** | Zarar gören zararı ve kusuru ispat yükü altında — delil korunmazsa ispat edilemez |
| **TTK m. 64 + 82** | Ticari defter ve belgelerin 10 yıl saklama |
| **HMK m. 219-220** | Hasım tarafın elinde olan delili sunma yükümlülüğü |
| **6698 KVKK m. 7** | Veri saklama süresi (ama dava varsa daha uzun saklanır) |
| **Vergi Usul Kanunu m. 253** | 5 yıl ticari belge saklama |
| **SGK Kanunu** | İş kazası belgeleri 10 yıl saklama |

**Pratik:** Bir dava açıldığında veya başlama beklentisi gerçekleşince:
1. **İlgili belgelerin silinmesi/yok edilmesi → TCK m. 281 kapsamında suç (belge bir suçun delili ise); ibraz edilmeyen belgede HMK m. 220/3 uyarınca karşı tarafın beyanı kabul edilebilir**
2. KVKK saklama süresi geçmiş olsa bile **dava nedeniyle saklanır** (KVKK Kurul kararı çeşitli)
3. Belge silinirse mahkeme **aleyhe karine** kurabilir (HMK m. 220)

### Legal hold notice taslağı (Türk versiyonu)

Kullanıcı bu skill'i tetiklediğinde, **konuyla ilgili çalışanlara gidecek "delil koruma duyurusu"** taslağını üret:

```markdown
[ÜST BAŞLIK: ŞİRKET İÇİ — GİZLİDİR]
[Tarih]

Konu: [Dosya / olay] ile ilgili delil koruma duyurusu

Sayın [çalışan/birim],

[Olay/uyuşmazlık] ile ilgili dava süreci başlamıştır / başlama beklenmektedir.
Bu süreçle ilgili tüm doküman, e-posta, yazışma, fiziksel belge, kamera kaydı
ve dijital veri **derhal koruma altına alınmalıdır**.

**Kapsam (örneklemeli, sınırlama değildir):**
- [Olay/sözleşme/işlem] ile ilgili tüm yazışmalar (e-posta, KEP, mesajlaşma)
- [İlgili dönem] kontrol listeleri, raporlar, tutanaklar
- [İlgili kişiler] tarafından oluşturulan tüm dokümanlar
- [İlgili sistem/teçhizat] log kayıtları
- Bu konuyla ilgili olduğunu düşündüğünüz HER doküman

**Yapılması gerekenler:**
1. Mevcut dosyaları **silmeyiniz, değiştirmeyiniz, yok etmeyiniz.**
2. Bilgisayar / e-posta / Teams / SharePoint'te otomatik silme varsa **devre dışı bırakınız** veya BT'den **istisna** isteyiniz.
3. Fiziksel belgeleri **ayrı bir dosyada saklayınız**.
4. Yeni gelen ilgili belge veya yazışmaları aynı dosyaya ekleyiniz.

**Süre:** Bu koruma talimatı **yazılı olarak Hukuk Müşavirliği tarafından kaldırılmadıkça** geçerlidir.

**Sorumluluk:** Bu talimata aykırı hareket TCK m. 281 (suç delilini yok etme)
kapsamında **kişisel cezai sorumluluk** doğurabilir; ayrıca şirket aleyhine
HMK m. 220 kapsamında **aleyhe karine** oluşur.

**Sorular için:** [Hukuk Counsel] — [e-posta/Teams]

Saygılarımla,
[Hukuk Direktörü adı]
[Müvekkil]
Hukuk, Uyum ve Kurumsal Yönetişim Başkanlığı
```

Çıktıda hangi alanların `[DOLDUR]` olduğu net olsun.

### BT koordinasyonu

- [ ] **E-posta arşivi:** İlgili kullanıcıların e-postaları "litigation hold" işaretlensin (otomatik silme devre dışı)
- [ ] **Teams / Slack mesajları:** Aynı şekilde
- [ ] **SharePoint / Drive:** İlgili dosyalar version history'si korunsun
- [ ] **ERP / case management sistemi:** İlgili kayıtlar audit log'la
- [ ] **Kamera sistemleri:** Otomatik silme cycle'ı uzatılsın
- [ ] **Backup tape'ler / soğuk depolama:** İlgili dönem backupları segregate edilsin

## B. MAHKEMEDE DELİL SUNUMU (HMK)

### Delil çeşitleri (HMK m. 187-293)

| Delil tipi | HMK madde | Kullanım | [Müvekkil]-spesifik |
|---|---|---|---|
| **Belge (yazılı delil)** | m. 199-224 | Sözleşme, ihtarname, e-posta (KEP), fatura, raporlar | KEP kaydı/delili **senet hükmünde**, aksi ispat edilinceye kadar kesin delil (KEP Yönetmeliği m. 15/1 — doğrulanmadı; HMK m. 205/2) — TTK m. 18/3 yalnız tacirler arası ihtar şekli |
| **Tanık** | m. 240-265 | Olaya tanıklık eden gerçek kişi | İSG kazasında işçi/teknisyen kritik |
| **Bilirkişi** | m. 266-287 | Teknik/uzmanlık gerektiren mesele | Rafineri/petrokimya teknik konular, çevre etkisi, vergi hesabı |
| **Keşif** | m. 288-292 | Mahkemenin yerinde inceleme | [TESİS LOKASYONU] tesisi kaza sonrası keşif |
| **Yemin** | m. 225-239 | Kesin delil ikamesi (nadir) | Genelde ticari uyuşmazlıkta |
| **Bilirkişi heyeti raporu** | m. 267 | Gerekçesi gösterilerek tek sayıda, birden fazla kişilik kurul (rapora itiraz: m. 281 — tebliğden 2 hafta) | Rafineri kazası standart 3 kişilik heyet |

### HMK m. 220 — Hasım tarafın elindeki delil

Karşı tarafta olan ama bize lazım olan bir delil için (örn. karşı tarafın iç yazışması, denetim raporu):

```markdown
Mahkemeye dilekçeyle başvurarak [HMK m. 220]:
- Belgenin niteliğini ve içeriğini tarif et
- Karşı tarafın elinde olduğunu kanıtla / gösteren delil
- İbraz edilmemesi halinde sonuçları talep et:
  - Mahkeme aleyhe karine kurabilir
  - Belgenin içeriğinin iddia edildiği gibi olduğu kabul edilebilir
```

Bu talep dilekçesinin **taslağını üret** (kullanıcıdan dosya bilgisi al → format).

### Tanık listesi (HMK m. 240)

```markdown
**Tanık listesi hazırlama:**

| Sıra | İsim | Adres | Tanıklık edeceği konu | Sıralama mantığı |
|---|---|---|---|---|
| 1 | [...] | [...] | [...] | "Olayın oluş şekli" |
| 2 | [...] | | | "Sözleşmenin kuruluşu" |

**sektöre-özel:**
- Şirket çalışanı tanıklık edebilir mi? → Evet; davada taraf olmayan herkes tanık olabilir (HMK m. 240/1); işveren bağımlılığı/yarar tanığa itiraz sebebi (m. 255) ve beyan hâkimce serbestçe değerlendirilir (m. 198) — m. 248 yalnız yakınlara tanıklıktan çekinme hakkı verir
- Yabancı uyruklu üst yönetici tanıklığı → tercüman gerekli (HMK m. 263), KEP/Apostille gerekebilir
- Sendika temsilcisi tanıklığı → [SEKTÖR SENDİKASI] ile koordinasyon
```

### Bilirkişi (HMK m. 266)

Karmaşık teknik konular (rafineri patlama nedeni, çevre kirlilik kaynağı, marka benzerlik, vergi hesabı) için bilirkişi şart.

```markdown
**Bilirkişi talep dilekçesi hazırlama:**

- Hangi konuda? (örn. "Patlamanın teknik nedeni, sorumluluk taksiri")
- Bilirkişinin nitelik şartları (örn. "Petrol rafinasyon mühendisliği ihtisası")
- Bilirkişi listesinden mi yoksa serbest meslek mensuplarından mı?
- Ön rapor vs. duruşmada savunma?
```

### Keşif (HMK m. 288)

Mahkemenin yerinde inceleme yapması:

- **Avantaj:** Soyut analiz yerine somut görme; karşı tarafın hatalı iddiasını kırma
- **Risk:** Mahkeme bizim aleyhimize bir şey görebilir
- **sektöre-özel:** [TESİS LOKASYONU] tesisinde keşif → güvenlik prosedürleri (yangın eğitimi, koruyucu ekipman); EPDK lisans kapsamında izinler

## ArthurLegal MCP (`tr_`) — emsal aramaları

Delil sunumu prosedürlerinde benzer dava emsallerini ArthurLegal MCP (`tr_`)'den çek:

```
tr_ictihat_ara(
  courts=["YARGITAYKARARI"],
  query="+HMK +220 +belge +ibraz +aleyhe +karine",
  chamber="HGK",
  date_from="2022-01-01"
)
```

KEP'in delil değeri için özel arama:

```
tr_ictihat_ara(
  query="+kayıtlı +elektronik +posta +KEP +delil",
  date_from="2020-01-01"
)
```

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Delil Toplama Protokolü — [Dosya slug]

## ⚠️ İnceleyen notu
- **Senaryo:** Delil koruma (legal hold) / Mahkeme delil sunumu / Karma
- **Acil aksiyonlar:** [liste]
- **Mevzuat referansları:** HMK m. [...], TCK m. 281, TTK m. 64, KVKK m. 7 `[ArthurLegal TR — GG.AA.YYYY]`
- **Emsal:** [N karar] `[ArthurLegal MCP (`tr_`) — yargitay — GG.AA.YYYY]`

## A. Delil koruma duyurusu (taslak)

[duyuru taslağı — yukarıdaki şablon]

**Dağıtım listesi:**
- [İlgili çalışan listesi]

**BT koordinasyonu yapılacaklar:**
- [checklist]

## B. Mahkemeye sunulacak delil planı

### B1. Belge envanteri
[tablo: belge, kaynak, ibraz edilebilir mi, m. 220 talep mi]

### B2. Tanık listesi
[tablo]

### B3. Bilirkişi talebi
[varsa — konu, nitelik]

### B4. Keşif talebi
[varsa — yer, neden]

## Sonraki adımlar (decision tree)

> **What next? Pick one and I'll help you build it out:**
> 1. **Delil koruma duyurusunu dağıt** — IT + İK koordineli; dağıtım listesini onayla
> 2. **HMK m. 220 ibraz talep dilekçesi** — karşı tarafa karşı [belge için]
> 3. **Tanık çağrı dilekçesi taslağı**
> 4. **Bilirkişi seçim önerisi** — listeden 3 isim
> 5. **Daha fazla bilgi al** — şu soruları cevaplayalım: [...]

**One question I'd ask that isn't in my checklist:** [örn. "Karşı tarafın iç soruşturmasından sızabilecek bir belge var mı? Whistleblower kanalına gitmiş olabilir mi?"]
```

## Reviewer note format

İnceleyen notu standardı `practice profile → ## Outputs` bölümündeki [Müvekkil] formatına göre.

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
| Turk doktrini (DergiPark 19 hukuk dergisi) + karsilastirmali ogreti — **ikincil**; bir karar kademesini yukseltmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| uyusmazlik AZ hukukuna tabiyse akt + statu. **AZ ictihadi bu araclarda YOK** — `azerbaycan-hukuk-rehberi.md` | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
