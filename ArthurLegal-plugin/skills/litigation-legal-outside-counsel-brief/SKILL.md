---
name: litigation-legal-outside-counsel-brief
description: >
  Dış vekile yeni bir dava dosyası iletiliyorken veya stratejik talimat verilirken
  standardize brief paketi: dosya özeti, sorulan sorular, beklentiler (timeline,
  bütçe, raporlama), iç hukuk pozisyonu, kritik notlar, escalation eşikleri. [Müvekkil]
  dış-vekil ağırlıklı modelin temel iş akışı. KEP üzerinden gönderim hazır.
user-invocable: true
---

# Outside Counsel Brief — Dış Vekil Brief'i

## Matter context

Bu skill **aktif matter** içinde çalışır (yeni dosya açıldıysa cold-start veya case-intake'den geliyor olabilir).

## Destination check

**Destinasyon: dış vekil (avukatlık bürosu)** — Avukatlık K. m. 36 + ticari sır rejimi kapsamında. Üst başlık:

```
DAVA BRIEF – DAHİLİ VE GİZLİDİR – AVUKATLIK K. m. 36 KAPSAMINDA
[Müvekkil] - Sayın [vekil adı / büro] dikkatine
Esas no: [...] | Taraflar: [...] | Mahkeme: [...]
Tarih: GG.AA.YYYY | Briefer: [in-house Counsel adı]
[Müvekkil] iç onay: [Hukuk Direktörü/Başkan onayı geçtiyse "Onaylı" + tarih]
```

KEP üzerinden gönderim için: brief tek dosyalık PDF olmalı (in-house tarafından oluşturulup KEP attachment olarak gönderilir).

## Amaç

[Müvekkil]'da **tüm davalar dış vekille yürütülüyor**. In-house ekibinin işi dış vekile **standardize edilmiş, eksiksiz, tek-istek paketleri** vermek. İyi brief = kısa iş ücreti + iyi cevap + daha az takip e-posta.

**Kötü brief'in maliyeti:** Dış vekil 5 ek soru sormak için saatlik ücret yazıyor; doğru bilgi olmayınca yanlış strateji; eksikten dolayı dosya kaybediliyor.

## Brief paketinin yapısı

### 1. Genel bilgi başlığı

```markdown
**Dosya bilgisi:**
- [Müvekkil] dosya no: [iç sistem]
- Esas no (varsa): [mahkemeden]
- Taraflar: [Davacı/Davalı [Müvekkil] mı?]
- Mahkeme/yargı yeri: [...]
- Konuya tarihi: [...]
- Cevap/itiraz süresi: [tarih + kalan gün]

**[Müvekkil] organizasyon bilgisi:**
- İlgili iş birimi: [Rafineri & Petrokimya / Doğal Gaz & Enerji / Portföy]
- İlgili tüzel kişi: [[Müvekkil] / [HALKA AÇIK İŞTİRAK] / [büyük enerji tesisi] / [Müvekkil] Enerji Ticaret / ...]
- İçeride dosya sahibi (in-house Counsel): [isim, iletişim]
- Eskalasyon zinciri: [Counsel → Direktör → ... → CEO]

**KAP / yatırımcı bilgi (halka açık iştirak ilgili ise):**
- KAP açıklama gerekli mi? [evet/hayır/değerlendiriliyor]
- İçsel bilgi listesine giren bilgi var mı? [evet/hayır]
```

### 2. Olay/uyuşmazlık özeti (Background)

Maks 1 sayfa — dış vekil bunu hızla okur. **Zaman çizgisi (timeline)** kronolojik:

```markdown
## Background

[Tarih başlangıç]: [Olay başladı / sözleşme imzalandı / kaza yaşandı]
[Tarih]: [İhtarname geldi / cevap verildi]
[Tarih]: [Dava açıldı / cevap dilekçesi verildi]
[Tarih]: [Bilirkişi atandı / keşif yapıldı]
[Bugün]: [Şu an neredeyiz]

**Karşı taraf iddiası özeti:**
[1-2 paragraf]

**Talep edilen:**
- Tutar: [...]
- Diğer: [özür, men, vs.]

**Hukuki dayanak (karşı tarafın gösterdiği):**
- [Kanun madde no'ları + içtihat]
```

### 3. İç hukuk pozisyonu

```markdown
## İç hukuk pozisyonu

### [Müvekkil]'ın pozisyonu (savunma argümanları)
1. [Argüman 1] — dayanak: [...]
2. [Argüman 2] — dayanak: [...]
3. [Argüman 3 — yedek] — dayanak: [...]

### Zayıf noktalarımız (counter-argumentation öngörüsü)
- [Zayıf nokta 1] — karşı taraf bunu nasıl kullanır
- [Zayıf nokta 2]

### İçerideki ilgili emsal davalar
- [Önceki dosya / sonuç / vekili]

### İç araştırma (ArthurLegal MCP (`tr_`)'den çekilenler)
- [Karar 1] `[ArthurLegal MCP (`tr_`) — daire — GG.AA.YYYY]` — [özet/eğilim]
- [Karar 2] — [...]
```

### 4. Dış vekilden talep ettiklerimiz

KRİTİK BÖLÜM — net olmalı, eksik kalmamalı:

```markdown
## Dış vekilden talepler

### Aksiyon (somut yapılacaklar)
1. [Cevap dilekçesi hazırla / itiraz dilekçesi sun / sulh teklifi cevapla / vs.]
2. [Tanık listesi öner]
3. [Bilirkişi seçim önerisi sun]
4. [Stratejik görüş ver]

### Sorularımız (cevap bekleniyor)
1. [Hukuki yorumlama sorusu]
2. [Strateji sorusu]
3. [Pratik soru — örn. "Sulh için hangi tutar makul olur?"]

### Hangi belge gönderildi (ek listesi)
- Ek 1: [...] (PDF/DOCX, sayfa sayısı)
- Ek 2: [...]
- Ek 3: [...]

### Cevap süresi
**Hangi tarihe kadar:** GG.AA.YYYY (en geç)
**Format:** Yazılı brief + Teams toplantı (önerilen) / sadece yazılı

### Bütçe
- Saatlik ücret: [TL/saat] — anlaşıldı
- Toplam tavan: [TL] — onaylı veya [Direktör/Başkan onayına gidecek]
- Aşma durumunda: önceden bilgi şart
```

### 5. Raporlama beklentisi

```markdown
## Raporlama disiplini ([Müvekkil] standardı)

- **Aylık rapor:** Her ayın 5'inde Excel formatında — dosya durumu, sonraki adım, yapılan iş saati, beklenen masraf
- **Acil bildirim:** Şu olaylar olduğunda derhal:
  - Karşı taraftan sulh teklifi
  - Mahkemenin önemli ara kararı
  - Bilirkişi raporu (aleyhe veya bize avantajlı)
  - Tarihsel duruşma günü değişikliği
  - Cevap süresinde kaçırma riski
- **Çıkar çatışması:** Yeni bir [Müvekkil] davası ile çakışma riski olursa derhal bildirin
- **KAP / yatırımcı etkili gelişme:** halka açık iştirak ilgili tüm önemli gelişmeler derhal ([HALKA AÇIK İŞTİRAK] dosyalarında)
```

### ⚠️ ZORUNLU ÖN-KONTROL: TTK m. 5/A Zorunlu Arabuluculuk (ticari uyuşmazlıklarda)

**6102 sayılı TTK m. 5/A:** "Bu Kanunun 4 üncü maddesinde ve diğer kanunlarda belirtilen ticari davalardan, konusu bir miktar para olan alacak, tazminat, itirazın iptali, menfi tespit ve istirdat davalarında, dava açılmadan önce **arabulucuya başvurulmuş olması dava şartıdır**." (Ek: 7155 s. K., 2018; kapsam 7445 s. K. m. 31 ile 2023'te genişletildi)

**Kapsam:**
- ✅ Ticari uyuşmazlıklar (TTK m. 4 — mutlak/nispi ticari iş)
- ✅ Konusu bir miktar para olan alacak, tazminat, itirazın iptali, menfi tespit ve istirdat davaları (vendor uyuşmazlığı, EPC, satım, lojistik)
- ❌ KAPSAM DIŞI: İhtiyati tedbir, ihtiyati haciz, geçici hukuki koruma; tüketici davaları (ayrıca TKHK m. 73/A dava şartı arabuluculuk); iş davaları (7036 sayılı İş Mahkemeleri K. m. 3 dava şartı arabuluculuk)

**[Müvekkil]/[HALKA AÇIK İŞTİRAK] için pratik:**
- Vendor 80M TL gibi büyük ticari uyuşmazlık → **dava açmadan önce arabuluculuk dava şartı**
- Arabuluculuk başlangıç: **Adalet Bakanlığı Arabuluculuk Daire Başkanlığı sistemi** üzerinden başvuru
- Süre: arabulucu atama 3 gün + ilk toplantı 3 hafta + tutanak 6 hafta tipik
- **Anlaşma sağlanırsa:** ilam niteliğinde icra edilebilir tutanak
- **Anlaşma sağlanmazsa:** "anlaşmama tutanağı" alınır → bu tutanak dava dilekçesine eklenir (yoksa dava reddi)

**Brief'te HBÖ'ye sorulacak:** "TTK m. 5/A zorunlu arabuluculuk için başvuru tarihi + arabulucu atama + müzakere stratejisi (sulh açılış teklifimiz) — dava dilekçesinden önce paralel hazırlık."

⚠️ **Bu adım atlanırsa dava reddi** (HMK m. 114 + TTK m. 5/A). Hızlı dava ihtiyacı varsa ihtiyati tedbir + arabuluculuk paralel.

### 6. sektöre-özel notlar

```markdown
## sektöre-özel notlar

- **Avukatlık K. m. 36 kapsamında gizlilik:** Bu brief ve tüm yazışmalar dahildir.
- **TTK m. 55/1-d + m. 56 (haksız rekabet — üretim ve iş sırları) ve TCK m. 239 (ticari sır):** İhlal halinde tazminat ve cezai sorumluluk.
- **Ana ortak [Ana ortak / ilişkili taraf] ile koordinasyon:** Stratejik dosyalarda [ANA ORTAK MERKEZİ] ile bilgi paylaşımı yapılmadan önce onay alınmalı (intra-group işlemler).
- **EPDK lisans riski:** Karar EPDK lisansını etkileyebilir mi? Etkilemesi mümkünse derhal in-house Counsel'a bildirin.
- **Üst yönetim ismi:** Üst yönetim adının açıkça geçtiği bir gelişme olursa derhal CEO + Hukuk Başkanı bilgi.
- **Basın takibi:** Bu davanın basına yansıma olasılığı [yüksek/orta/düşük]. Basından bir gelişme olursa İletişim Başkanlığı ([İletişim Başkanlığı]) ile koordineli — kendi başınıza basına açıklama yapmayın.
```

### 7. Çıkar çatışması beyanı

```markdown
## Çıkar çatışması (vekil tarafından doldurulacak)

Bu brief'i kabul etmeden önce lütfen kontrol edin:
- Karşı taraf [...]: bürodaki başka avukatlar tarafından temsil ediliyor mu?
- Aynı kategorideki başka dava: ileride çatışma yaratır mı?
- Yatırımcılar arası: aktif hisse sahibi misiniz?

Yazılı çıkar çatışması beyanı brief'in kabulüyle birlikte alınır.
```

## ArthurLegal MCP (`tr_`) — emsal araştırması

Brief hazırlanırken **mutlaka** karşı tarafın hukuki dayanağına ilişkin son emsal kararları çek:

```
tr_ictihat_ara(
  query="<davanın hukuki konu>",
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  date_from="2023-01-01"
)
```

Bunları brief'in **"İç araştırma"** bölümünde özetle — dış vekilin işini hızlandırır.

## Çıktı şablonu (tek dosyalık PDF için)

```markdown
[ÜST BAŞLIK]

# DAVA BRIEF — [Esas No / Dosya Slug]

## ⚠️ İnceleyen notu (bu sayfa brief'in içinde değil, eşlik eden iç memo)
- **Hazırlayan:** [in-house Counsel]
- **İç onay:** [Hukuk Direktörü onayı tarihi]
- **Dış vekil seçimi:** [Büro] — [Pratik alan uygunluğu kontrolü]
- **Cevap süresi:** [tarih + kalan gün]
- **Bütçe onayı:** [tutar + onaylayan]

---

## 1. Genel bilgi
[başlık bölümü — esas no, taraflar, mahkeme, vs.]

## 2. Background
[olay özeti + timeline]

## 3. İç hukuk pozisyonu
[argümanlar + ArthurLegal MCP (`tr_`)'den çekilen emsal]

## 4. Dış vekilden talepler
[aksiyonlar + sorular + ekler + bütçe]

## 5. Raporlama disiplini
[[Müvekkil] standardı]

## 6. sektöre-özel notlar
[Avukatlık K. m. 36 + ticari sır + EPDK + üst yönetim + basın]

## 7. Çıkar çatışması beyanı
[vekil tarafından]

## Ekler
- Ek 1: [...]
- Ek 2: [...]

---

İletişim:
[Counsel adı]
[E-posta]
[Telefon]
KEP: [[Müvekkil] KEP adresi]
```

## Sonraki adımlar (decision tree)

```markdown
> **What next? Pick one and I'll help you build it out:**
> 1. **Brief'i PDF formatına çevir** ve KEP gönderim metni hazırla
> 2. **Hukuk Direktörü onay notu** — brief'in özet hali, onay imzası için
> 3. **Dış vekil seçim önerisi** — practice profile'dan 2-3 büro karşılaştırma
> 4. **Bütçe onay paketi** — Direktör/Başkan'a tutar onayı
> 5. **Brief tasarımı revize** — eksik bilgi var, şu soruları tekrar gözden geçirelim: [...]

**One question I'd ask that isn't in my checklist:** [örn. "Bu büronun karşı taraf veya karşı taraf vekiliyle daha önceki ilişkisi nedir? Reciprocal etkisi olabilir."]
```

## Reviewer note format

Brief hazırlanırken in-house Counsel'in **mutlaka bizzat okuduğu** belge olmalı — AI sadece taslak verir. Cevap kalitesi brief'in eksiksizliğine doğru orantılı.

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
