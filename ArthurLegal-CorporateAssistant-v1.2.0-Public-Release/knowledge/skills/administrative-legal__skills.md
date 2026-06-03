# administrative-legal - Skill Referans Kitapcigi

> Alan: Idari hukuk - 3 dereceli idari yargi, CED, EPDK
> Toplam skill: 8
> Kullanim: /{plugin}:{skill-adi} komutunu yaz, asagidaki ilgili bolumu uygula.

## Icindekiler

- /administrative-legal:ced-itiraz (139 satir)
- /administrative-legal:cold-start-interview (96 satir)
- /administrative-legal:epdk-proaktif-gorus (158 satir)
- /administrative-legal:idari-dava-prep (257 satir)
- /administrative-legal:idari-para-cezasi-itiraz (123 satir)
- /administrative-legal:istinaf-temyiz-prep (222 satir)
- /administrative-legal:kik-ihale-itiraz (133 satir)
- /administrative-legal:rekabet-kurulu-itiraz (110 satir)

---

## /administrative-legal:ced-itiraz

---
name: ced-itiraz
description: >
  ÇED (Çevresel Etki Değerlendirmesi) ret kararı geldiğinde veya ÇED süreci
  sorunlu olduğunda — [İşletme alanı] için kritik. Çevre K. 2872 + ÇED Yön.
  analizi, ilk derece İdare Mahkemesi (Ankara/İzmir), yürütmenin durdurulması,
  Danıştay 14./10. Daire emsali. Çevre Bakanlığı paralel idari ceza ile koordineli.
user-invocable: true
---

# ÇED İtiraz Hazırlık

## Tetik

İki ana senaryo:
1. **ÇED ret kararı tebliğ edildi** → ⚠️ **İYUK m. 20/A İVEDİ YARGILAMA — 30 gün dava süresi** (m. 7 genel kuralı değil! ÇED için özel rejim)
2. **ÇED süreci sorunlu** → henüz ret yok ama olumsuz gidiyor; proaktif strateji

## ⚠️ KRİTİK: İYUK m. 20/A İVEDİ YARGILAMA USULÜ

ÇED kararları (idari yaptırım/para cezası **HARİÇ**) bu özel rejime tabidir. Genel rejimden farkları:

| Genel rejim (m. 7) | ÇED rejimi (m. 20/A) |
|---|---|
| 60 gün dava süresi | **30 gün** |
| m. 11 üst makama başvuru süreyi durdurur | **m. 11 UYGULANMAZ** |
| İdare Mah. → BİM → Danıştay (3 derece) | İdare Mah. → **DOĞRUDAN Danıştay (15 gün temyiz)** — BİM YOK |
| Bilirkişi/keşif standart | Hızlı yargılama, kısıtlı |

**[ŞİRKET ADI] [işletme yeri] için bu kritik:** STAR/[HALKA AÇIK İŞTİRAK] ÇED yenileme + kapasite artırımı dosyalarında **30 günlük süreye** sıkı uyum şart. Geç kalma = hak düşürücü süre = yatırım blokesi.

## Süreç haritası

```
ÇED başvuru →
ÇED inceleme komisyonu (uzman değerlendirme) →
Bakanlık kararı (olumlu / olumsuz / koşullu) →
  [Olumsuz → İYUK 30 gün → İdare Mah. iptal davası]
  [Koşullu → Koşullar problem yaratıyorsa kısmen itiraz]

Paralel: Çevre Bakanlığı idari para cezası (ayrı süreç — `idari-para-cezasi-itiraz`)
```

## Görevli mahkeme (İYUK m. 20/A — BİM YOK)

- **Bakanlık merkez kararı** (büyük yatırım) → **Ankara İdare Mahkemesi** ilk derece (30 gün) → **DOĞRUDAN Danıştay 14./10./6. Daire temyiz** (15 gün)
- **İl müdürlüğü kararı** (yerel etkili) → ilgili **İl İdare Mahkemesi** ([İşletme Yeri] için İzmir İdare Mah.) → **DOĞRUDAN Danıştay temyiz**

⚠️ İstinaf (BİM) aşaması ATLANIR — bu önemli, çünkü genel idari davalarda BİM normal kademe.

## [ŞİRKET ADI]-özel risk

**[İşletme alanı] sürekli ÇED yenileme + değişiklik süreçlerinde:**
- [RAFİNERİ] kapasite artırımı
- [HALKA AÇIK İŞTİRAK] yeni üretim hattı
- [ŞİRKET ADI] Terminal kapasite genişleme
- [ELEKTRİK SANTRALİ] santral revizyonları

Her biri ÇED süreci tetikler. **Çevre Bakanlığı'nın ÇED ret kararı**:
- Yatırımı durdurur (büyük maliyet)
- Olası mevcut faaliyet kısıtlaması
- Basın/STK takibi yüksek

## Yarg MCP

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="14. Daire",
  arananKelime="ÇED ret iptal rafineri petrokimya",
  baslangicTarihi="2022-01-01"
)

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="10. Daire",
  arananKelime="çevre etki değerlendirme",
  baslangicTarihi="2022-01-01"
)
```

## Hukuki argümanlar (klasik ÇED itiraz)

- **ÇED komisyonu üyelerinin uzmanlığı yetersiz** — şekil itirazı
- **Bağımsız uzman görüşü göz ardı edildi** — sebep ihlali
- **AB / Türk standartlarıyla uyumlu olduğunu ispat** (BAT — best available techniques)
- **Sektör emsali yatırımların ÇED onayı** (benzer rafineri/[petrokimya iştiraki], neden bu reddedildi?)
- **Bakanlık kendi prosedürüne uymadı** (komisyon toplantı eksik, halk katılımı yetersiz)

## [ŞİRKET ADI] koordinasyon

`/administrative-legal:idari-dava-prep` skill ile birlikte çalış — dava dilekçesi taslağı oradan; ÇED-spesifik argümanlar buradan.

**Compliance ekibi:** [UYUM DİREKTÖRÜ] + [REGULATORY COMPLIANCE MÜDÜRÜ] çevre uyum bilgisi sahipdir — onlarla brief.

**İletişim Başkanlığı:** [İLETİŞİM BAŞKANI] — basın ve sosyal medya etkili olacaksa.

**İlgili iş birimi:** Mirzayev (rafineri/[petrokimya iştiraki]) — operasyonel etki bilgisi.

## Çıktı

```markdown
[ÜST BAŞLIK]

# ÇED İtiraz — [Yatırım/Tesis]

## ⚠️ İnceleyen notu
- **Karar:** ÇED ret / koşullu / süreç sorunlu
- **Görevli mahkeme:** Ankara İdare Mah. (Bakanlık merkez) / İzmir İdare Mah. (yerel)
- **Süre kalan:** [N gün]
- **Yatırım finansal etkisi:** [TL]
- **Üretim duruş riski:** [evet/hayır]
- **Basın etkisi:** [yüksek/orta/düşük]
- **Kaynaklar:** Yarg MCP (Danıştay 14./10. [N]); Mevzuat MCP (Çevre K. 2872 + ÇED Yön.)
- **Reviewer bekleyen:** N adet

## ÇED kararının özeti
[ret gerekçesi + Bakanlığın iddiası]

## Bizim pozisyonumuz
[yatırımın çevre uyumu + BAT + emsal yatırımlar]

## Hukuki argümanlar
[şekil + sebep + konu + amaç itirazları]

## Yürütmenin durdurulması
[telafisi güç zarar = yatırım blokesi; hukuka aykırılık = ...]

## Emsal Danıştay kararları
[Yarg MCP]

## Sonraki adımlar

> 1. **Dış çevre avukatı brief** — `/litigation-legal:outside-counsel-brief`
> 2. **CLCO eskalasyon** — yatırım blokesi büyük
> 3. **İletişim Başkanlığı koordinasyon** — basın hazırlığı
> 4. **Compliance brief** — [UYUM DİREKTÖRÜ]/Arıcı ile teknik koordinasyon
> 5. **Daha fazla bilgi** — [...]

**One question I'd ask:** [örn. "Aynı sektörde son 12 ayda Bakanlık ne kadar ÇED onayladı, ne kadar reddetti? Eğilim pozitif mi negatif mi?"]
```

---

## /administrative-legal:cold-start-interview

---
name: cold-start-interview
description: >
  İdari hukuk pratiğini bilgisayara öğret — düzenleyici kurum dialog modeli (EPDK
  proaktif vs defansif), aktif idari dava envanteri (İdare Mah. + BİM + Danıştay
  aşamalarında), birincil yakıcı stres (ÇED/EPDK/Rekabet/KVKK/KİK), outside
  counsel paneli (Ankara odaklı), eskalasyon eşikleri. 2dk hızlı / 10dk tam mod.
user-invocable: true
---

# Cold-Start Interview — Administrative Practice

## Modlar

Argümansız çağrılırsa:

> İki mod:
> - **Hızlı (2 dakika)** — 6 kritik soru
> - **Tam (10 dakika)** — 20+ soru
>
> Hangisi? (`--redo` sıfırlar; `--check-integrations` MCP testi)

## Hızlı mod (6 soru)

1. **Birincil yakıcı stres:** ÇED / EPDK / Rekabet / KVKK / KİK / karma
2. **Düzenleyici kurum dialog:** Proaktif / Defansif / Karma
3. **Aktif idari dava sayısı (üç aşama toplam):**
4. **Birincil dış vekil tipi:** Ankara odaklı uzman / İstanbul büronun Ankara ofisi / Konuya özel / Karma
5. **EPDK ile günlük interface:** Var / Yok / Bazı birim için var
6. **Eskalasyon:** Hangi tutar/konuda otomatik Başkan/CEO eskalasyonu?

## Tam mod (20+ soru, batch'ler)

### Batch 1 — Pratik modeli ve dava envanteri
- Aktif idari dava sayısı (İdare Mah. / BİM / Danıştay aşama dağılımı)
- Pratik alana göre dağılım (ÇED, EPDK, Rekabet, KVKK, KİK, BDDK, SPK, diğer)
- Yıllık yeni dava açma + cevap verme rakamları
- Düzenleyici kurum interface yoğunluğu

### Batch 2 — Outside counsel paneli
- Birincil büro tipi (Ankara/İstanbul + Ankara ofisi/karma)
- Pratik alana göre uzman büro var mı (ÇED için ayrı, EPDK için ayrı, vs.)
- Brief disiplini + aylık rapor
- Vekalet ücreti modeli

### Batch 3 — Eskalasyon ve onay
- Dava açma yetkisi
- İstinaf / temyiz yetkisi
- AYM bireysel başvuru yetkisi
- Yürütmenin durdurulması talep
- EPDK Kurul'a proaktif görüş sunma onayı
- Tutardan bağımsız otomatik eskalasyon listesi

### Batch 4 — Düzenleyici kurum interface
- EPDK proaktif dialog modu (varsa nasıl: toplantı, yazışma, görüş)
- Rekabet Kurumu ile genel ilişki
- Çevre Bakanlığı + il müdürlüğü koordinasyon ([İşletme Yeri] için)
- KVKK Kurumu ile ilişki
- KİK ihale itirazları sıklık
- SPK / BDDK ([HALKA AÇIK İŞTİRAK] ilgili) ilişki

### Batch 5 — Halka açık ve özel kontroller
- [HALKA AÇIK İŞTİRAK] ilgili tüm idari konular için KAP koordinasyon
- Yatırımcı ilişkileri ile interface
- Compliance ekibi koordinasyon
- Basın / İletişim Başkanlığı protokolü

## --check-integrations

1. **Yarg MCP** — test: `search_danistay_decisions(daire="13. Daire", arananKelime="EPDK lisans")` → cevap geliyor mu?
2. **Mevzuat MCP** — test: `search_mevzuat(mevzuat_no="2577", mevzuat_tur="KANUN")` → İYUK dönüyor mu?
3. **iManage** + diğerleri

Rapor formatı litigation-legal/tax-legal ile aynı.

## Çıktı

```markdown
## ✓ Administrative practice profile dolduruldu

**Doldurulan:**
- Yakıcı stres: [özet]
- Dava envanteri: [özet]
- Düzenleyici kurum dialog: [özet]
- Outside counsel: [özet]
- Eskalasyon: [özet]

**Hala [DOLDUR]:**
- [liste]

**Sonraki adım önerisi:**
- /administrative-legal:idari-dava-prep — yeni idari işleme karşı dava
- /administrative-legal:epdk-proaktif-gorus — EPDK Kurul'a görüş
- /administrative-legal:ced-itiraz — ÇED ret
- Manuel: ~/.claude/plugins/config/claude-for-legal/administrative-legal/CLAUDE.md
```

---

## /administrative-legal:epdk-proaktif-gorus

---
name: epdk-proaktif-gorus
description: >
  EPDK Kurul'a proaktif görüş/talep sunma. Dava ÖNCESİ çözüm kanalı. [ŞİRKET ADI]'ın
  EPDK ile yoğun dialog modelinde temel araç. Kurul kararı çıkmadan önce yorum,
  Tebliğ taslağına görüş, lisans şartı yorumu, görüş başvurusu. [UYUM DİREKTÖRÜ]
  (Compliance Direktörü) + [REGULATORY COMPLIANCE MÜDÜRÜ] (Regulatory Compliance Manager) ile
  koordineli hazırlanır.
user-invocable: true
---

# EPDK Proaktif Görüş Sunum

## Felsefe

[ŞİRKET ADI] pratiğinde **dava açmadan önce EPDK ile dialog kanalı** kullanılır:
- Yapısal Kurul kararı çıkmadan **erken görüş sunma**
- Tebliğ değişikliği taslağına **sektör yorumu**
- Belirsiz lisans şartı için **yorum talebi**
- Olumsuz karar belirtisi varsa **resmi pozisyon** sunma (dava'dan önce)

Bu kanal başarılı olursa **dava açmaktan kaçınılır** — zaman + maliyet + reputational avantaj.

## Tetik

> Hangi durumda EPDK'ya görüş sunuyoruz?
> A. Yayınlanacak Tebliğ taslağına yorum (kamuoyu istişaresi süreci)
> B. Mevcut Tebliğ/yönetmeliğin uygulanması belirsiz, yorum talebi
> C. Bir Kurul kararı çıkacağa benziyor (olumsuz) — pozisyon sunarak etkilemek
> D. Lisans şartı revizyon talebi
> E. Resmi olmayan dialog (toplantı sonrası takip yazısı)

## Adımlar

### 1. Karşı argüman / etkilemek istediğimiz konuyu netle

- **Sorun:** [örn. "Yeni tebliğde belirlenen rapor formatı [ŞİRKET ADI] için uygulanamaz çünkü..."]
- **Etki:** [operasyonel + mali]
- **Önerimiz:** [somut alternatif]

### 2. Dayanak araştırma

- **Mevzuat MCP** — ilgili kanun/tebliğ + EPDK Kanunu (4628 + 5015 + 4646 + 6446)
- **Yarg MCP — Danıştay 13. Daire** — benzer konularda Danıştay yorumu (EPDK aleyhine olan emsaller bizim için anchor)
- **GİB özelge** — vergi yönü varsa
- **Sektör emsali** — diğer enerji şirketleri benzer pozisyon mu? (Tüpraş, Aygaz, Akenerji)

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="13. Daire",
  arananKelime="EPDK lisans şartı yorumu emsal",
  baslangicTarihi="2022-01-01"
)
```

### 3. Görüş sunum metni

```markdown
T.C. ENERJİ PİYASASI DÜZENLEME KURUMU [Daire/Sektör Müdürlüğü]
ANKARA

Konu: [Tebliğ/Karar adı] hakkında [ŞİRKET ADI] A.Ş. görüşü

Sayın Yetkilisi,

[Yayınlanan/yayınlanacak tebliğ taslağı/Kurul kararı] hakkındaki şirketimiz
görüşünü aşağıda saygıyla sunarız.

I. KONU VE ETKİ

[Düzenlemenin neyin etkilediği, [ŞİRKET ADI]/STAR/[HALKA AÇIK İŞTİRAK]/[ELEKTRİK SANTRALİ] üzerindeki
operasyonel ve mali etki — somut rakamlar]

II. ŞİRKETİMİZ GÖRÜŞÜ

A. [Hukuki dayanak — mevcut mevzuat ile uyumluluk değerlendirmesi]
B. [Operasyonel pratikte uygulanabilirlik]
C. [Sektör pratiği ile karşılaştırma]
D. [Önerimiz / alternatif düzenleme]

III. EMSAL UYGULAMALAR

[Danıştay emsali, EPDK'nın geçmiş yorumu, sektör örnekleri]

IV. SONUÇ

Yukarıda açıklanan görüşümüzün dikkate alınmasını ve [düzenleme] taslağında
[değişiklik/yorum/açıklama] yapılmasını saygıyla arz ederiz.

Tarih: GG.AA.YYYY

[ŞİRKET ADI] A.Ş.
[Yetkili imza — Compliance Direktörü [UYUM DİREKTÖRÜ] veya CLCO [CLCO ADI]]

Ekler:
1. Operasyonel etki analizi
2. Sektör emsalleri
3. Önerilen alternatif metin (varsa)
```

### 4. Koordinasyon

- **Hukuk:** Senior Legal Counsel — hukuki argümantasyon hazırlar
- **Compliance:** [UYUM DİREKTÖRÜ] + [REGULATORY COMPLIANCE MÜDÜRÜ] — düzenleyici çerçeve uzmanlığı, EPDK ile ilişki
- **İş birimi:** Mirzayev (rafineri/[petrokimya iştiraki]) veya İbrahimov (doğal gaz) — operasyonel detay
- **Mali İşler:** Hasanov ekibi (CFO) — mali etki rakamı
- **Onay:** CLCO ([CLCO ADI]) imzalı veya yetkisi devrettiği Direktör

### 5. Takip

EPDK'dan cevap genelde 1-3 ay içinde:
- **Olumlu:** Görüş kabul edildi, taslak/karar revize → dava'ya gerek yok ✓
- **Kısmen kabul:** Müzakere devam ediyor
- **Olumsuz / sessizlik:** Dava planına geç → `/administrative-legal:idari-dava-prep`

### 6. Sektör koalisyon avantajı

Bazı görüşler **sektör koalisyonu** halinde (Türkiye Petrolleri, Tüpraş, Aygaz, vs. ile birlikte) sunulursa daha güçlü. [ŞİRKET ADI] + diğerleri ortak görüş = sektör temsili.

`PETDER`, `GAZBİR`, `EBSO` gibi sektör derneklerini koordinasyon kanalı olarak kullan.

## Çıktı

```markdown
[ÜST BAŞLIK — Compliance + Hukuk koordineli iç değerlendirme]

# EPDK Proaktif Görüş — [Konu]

## ⚠️ İnceleyen notu
- **Senaryo:** A/B/C/D/E
- **Hedef:** [Tebliğ değişikliği / Kurul karar etkisi / Yorum alma / Lisans şart revizyonu]
- **Kaynaklar:** Yarg MCP (Danıştay 13. [N]); Mevzuat MCP
- **Compliance koordinasyon:** [UYUM DİREKTÖRÜ] + [REGULATORY COMPLIANCE MÜDÜRÜ] ✓/⚠
- **İş birimi koordinasyon:** [Mirzayev/İbrahimov]
- **Mali etki:** [TL]
- **Sektör koalisyon olası:** [evet/hayır]
- **Reviewer bekleyen:** N adet

## Sorun ve etki
[somut etki açıklaması]

## Hukuki + operasyonel + mali argümantasyon
[A-D]

## Önerimiz
[somut alternatif]

## Görüş sunum metni (taslak)
[yukarıdaki şablon — doldurulmuş]

## Sonraki adımlar

> 1. **Compliance + İş birimi ortak gözden geçirme** — final pozisyon
> 2. **CLCO onayı** — imza için
> 3. **EPDK'ya sunum** — KEP veya yazılı + toplantı talebi
> 4. **Sektör koalisyon koordinasyon** — PETDER/GAZBİR
> 5. **Dava planı paralel hazırlık** — olumsuz cevap senaryosu için
```

---

## /administrative-legal:idari-dava-prep

---
name: idari-dava-prep
description: >
  İdari işleme karşı dava açılacak — KRİTİK İLK ADIM görevli mahkeme tespiti
  (İdare Mahkemesi mi, Danıştay mı ilk derece?), İYUK m. 7 (30 gün hak düşürücü)
  süre kontrolü, dava dilekçesi taslağı, yürütmenin durdurulması (m. 27),
  yetkili yer (HMK/İYUK), emsal kararlar (Yarg MCP). 3 dereceli idari yargı
  yapısına göre.
user-invocable: true
---

# İdari Dava Hazırlık

## ⏰ ÖN-KONTROL — SÜRE (her çalıştırmada)

> İdari işlem/karar **tarafa tebliğ tarihi** nedir?
> İYUK m. 7/1:
> - **İdare mahkemeleri: 60 GÜN** (özel kanun aksini belirtmedikçe)
> - **Vergi mahkemeleri: 30 GÜN** (2021 değişikliği)
> - **ÇED kararları: 30 GÜN** (İYUK m. 20/A ivedi yargılama — özel rejim)
> - **Diğer özel rejim** (kamu ihale belirli kategoriler, özelleştirme): m. 20/A kontrolü

Kalan < 5 gün → 🔴 ACİL. Dış vekille derhal koordinasyon.

⚠️ **Sık yapılan hata:** Vergi mahkemesi 30 günü idare mahkemesi davalarına yanlış uygulamak. Her zaman görevli mahkemeyi önce tespit et, sonra süreyi.

## Destination check

- **Mali İşler + Hukuk iç değerlendirme** → "GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ"
- **Dış idari hukuk avukatı brief** → "İDARİ DAVA BRIEF – AVUKATLIK K. m. 36"
- **CEO/Başkan eskalasyon** → 1 sayfa exec summary
- **Mahkemeye sunulacak dilekçe taslak** → "TASLAK" + dış vekil onayı sonrası

## ⚠️ ADIM 0 — GÖREVLİ MAHKEME TESPİTİ (en kritik)

Türk idari yargı **3 dereceli**: İdare Mahkemesi → BİM → Danıştay. **Danıştay genelde TEMYİZ mercii**, sadece dar istisnalarda ilk derece.

### Danıştay ilk derece görevli mi? (Danıştay K. m. 24 + 30)

İdari işlem bir aşağıdakilerden biri mi?
- [ ] **Cumhurbaşkanı Kararı** (tek karar, atama, vs.)
- [ ] **CB Kararıyla yürürlüğe konulan düzenleyici işlem** (Bakanlar Kurulu kararı muadili — genel norm)
- [ ] **Bakanlık veya kamu kurumu müsteşarına ilişkin müşterek kararname**
- [ ] **Bakanlık genel tebliği** veya **bakanlık yönetmeliği** (normatif düzenleyici işlem — bireysel idari işlem DEĞİL)
- [ ] EPDK / Rekabet Kurumu / BDDK / SPK gibi **kurumun genel TEBLİĞİ veya YÖNETMELİĞİ** (normatif)

**Evet** → **Doğrudan Danıştay**'a dava (ilgili daire — enerji/finans 13., çevre 10./14., diğer 5./8.)
**Hayır** → **İdare Mahkemesi**'nde ilk derece dava (sonra BİM istinaf, sonra Danıştay temyiz)

### Yetkili yer İdare Mahkemesi (eğer ilk derece İdare Mah. ise)

- **Genel kural (İYUK m. 32):** Davalı idarenin bulunduğu yer İdare Mahkemesi
  - EPDK / Rekabet / KVKK / KİK / BDDK / SPK = **Ankara** (kurumlar Ankara merkez)
  - Bakanlık merkez kararları = **Ankara**
  - İl müdürlüğü kararları (örn. İzmir Çevre İl Müdürlüğü idari ceza) = **İzmir İdare Mahkemesi**
  - [İşletme Yeri] Belediyesi imar kararları = **İzmir İdare Mahkemesi** ([İşletme Yeri] bağlı)

- **Özel yetki kuralları (İYUK m. 33-37):**
  - Vergi davası: vergi dairesinin bulunduğu yer (tax-legal kapsamında)
  - Memur statü: memurun görev yaptığı yer veya idarenin yeri
  - Kamulaştırma: taşınmazın bulunduğu yer

⚠️ **Yanlış mahkemeye dava** → görevsizlik kararı + görevli mahkemeye gönderme (m. 15) **ama süre durmaz**. Süresi geçmişse hak kaybı.

## Adımlar

### 1. İdari işlemi analiz et

| Soru | Cevap |
|---|---|
| İdari işlem tipi | Bireysel (lisans iptali, ceza, ret) / Düzenleyici (tebliğ, yönetmelik) |
| İdari işlemi yapan kurum | EPDK / Çevre Bakanlığı / Rekabet / KVKK / KİK / vs. |
| Tebliğ tarihi | GG.AA.YYYY |
| Tebliğ şekli | KEP / e-tebligat (UYAP) / yazılı / Resmi Gazete (düzenleyici işlem için) |
| Hukuki dayanak (idarenin gösterdiği) | [Kanun/Yönetmelik madde no'ları] |
| Talep edilen tutar (varsa) | TL |

### 2. Görevli mahkeme tespiti (ADIM 0 sonucu)

```markdown
**Görevli mahkeme:**
[Ankara X. İdare Mahkemesi — bireysel idari işlem için] VEYA
[Danıştay X. Daire — istisna kapsamında düzenleyici işlem için]

**Yetki gerekçesi:** [İYUK m. 32 — Ankara EPDK Kurul kararı için]
             VEYA  [Danıştay K. m. 24 — bakanlık yönetmeliği için]
```

### 3. Süre hesabı

```markdown
**Tebliğ tarihi:** GG.AA.YYYY
**Dava süresi sonu:** GG.AA.YYYY (kalan: N gün)
**İYUK m. 7 — 30 gün** [hak düşürücü]
```

### 4. Hukuki argümanlar

İdari işlemin iptali için klasik gerekçeler:
- **Yetkisizlik:** İdare bu işlemi yapma yetkisinde mi?
- **Şekil eksikliği:** Usul kurallarına uyuldu mu (kanunla aranan açıklamalar, gerekçe, oybirliği/oyçokluğu)?
- **Sebep yokluğu:** İdarenin dayandığı sebep hukuki/fiili olarak var mı?
- **Konu hukuka aykırılığı:** Kanunun açık metnine ters mi?
- **Amaç hukuka aykırılığı:** Kamu yararı dışında bir amaç gözetilmiş mi (örtülü amaç)?

### 5. Yürütmenin durdurulması (İYUK m. 27) — KRİTİK

Talep şart, **otomatik gelmez**. İki şart birden:
- **Telafisi güç veya imkansız zararlar:** EPDK lisans askıya alma → üretim duruş → milyon TL gelir kaybı; ÇED ret → yatırım dondurulur
- **Açıkça hukuka aykırılık:** Yukarıdaki argümanlardan en güçlüsü

**Talep dilekçenin içinde** ayrı bölüm olarak.

### 6. Yarg MCP — emsal arama

```
# Bireysel idari işlem için Danıştay temyiz emsali
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="13. Daire",  # EPDK/Rekabet/BDDK/SPK/KİK için
  arananKelime="<konu> iptal yürütmenin durdurulması",
  baslangicTarihi="2022-01-01"
)

# Çevre/ÇED için
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="10. Daire",
  arananKelime="çevre ÇED idari para cezası",
  baslangicTarihi="2022-01-01"
)

# İdare Mahkemesi/BİM kararları
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="<konu>",
  baslangicTarihi="2022-01-01"
)

# İdari kurum birincil kararları
mcp__claude_ai_Yarg_MCP__search_rekabet_kurumu_decisions(arananKelime="<konu>")
mcp__claude_ai_Yarg_MCP__search_kik_v2_decisions(arananKelime="<konu>")
mcp__claude_ai_Yarg_MCP__search_kvkk_decisions(arananKelime="<konu>")
```

### 7. Dava dilekçesi taslağı

```markdown
[GÖREVLİ MAHKEME BAŞLIĞI — örn. ANKARA X. İDARE MAHKEMESİ BAŞKANLIĞINA
veya DANIŞTAY X. DAİRESİ BAŞKANLIĞINA]

DAVACI:
[ŞİRKET ADI] A.Ş. — VKN, sicil, adres
Vekili: [Av. ad, baro sicil, KEP]

DAVALI:
T.C. [Bakanlık / EPDK / Rekabet Kurumu / vs.]
Vekili: [İlgili Bakanlık vekili veya Hazine ve Maliye Bakanlığı genel olarak]

DAVA KONUSU:
[Kurum] tarafından tesis edilen [GG.AA.YYYY tarih, ... sayılı] [karar/işlem]
nın **iptali** ile **yürütmenin durdurulması** talebidir.

İŞLEMİN TARİFİ:
[İdari işlemin tam tarifi, tarih, sayı, içerik]
Tebliğ tarihi: GG.AA.YYYY
Dava süresi: 30 gün → son tarih GG.AA.YYYY

I. OLAYLAR
[Kronoljik olay özeti]

II. HUKUKİ DAYANAKLARIMIZ

A. **Yetkisizlik** (eğer varsa) [argüman]
B. **Şekil eksikliği** [varsa]
C. **Sebep yokluğu** [argüman + emsal Danıştay kararı: `[Yarg MCP — danistay — daire — esas/karar — GG.AA.YYYY]`]
D. **Konu hukuka aykırılığı** [argüman]
E. **Amaç hukuka aykırılığı** [varsa]

III. YÜRÜTMENİN DURDURULMASI TALEBİMİZ (İYUK m. 27)

1. **Telafisi güç zararlar:**
   [EPDK lisans askıya alma → üretim duruş → günlük X TL kayıp]
   [veya benzeri somut zarar]

2. **Açıkça hukuka aykırılık:**
   [Yukarıdaki en güçlü argüman]

IV. SONUÇ VE TALEP

1. Yürütmenin durdurulmasına,
2. Dava konusu idari işlemin iptaline,
3. Yargılama gideri ve vekalet ücretinin davalı idareye yüklenmesine,

karar verilmesi saygıyla arz ve talep olunur.

Tarih: GG.AA.YYYY
Davacı Vekili: [imza]

EKLER:
1. Vekaletname
2. İdari işlemin tebliğ örneği
3. Konuya ilişkin belgeler
4. Emsal kararlar (Danıştay/BİM)
```

### 8. [ŞİRKET ADI]-özel kontroller

- [ ] **Tutar > 10M TL** veya **stratejik önem** → CEO + Başkan eskalasyon
- [ ] **[HALKA AÇIK İŞTİRAK] ilgili** → KAP açıklama kontrolü + IR Başkanlığı
- [ ] **EPDK lisans askıya alma riski** → derhal Başkan + CEO + iş birimi
- [ ] **[İşletme Yeri] İSG/çevre olayı sonrası idari ceza** → litigation-legal `isg-incident-response` ile koordine (üçlü-paralel dava)
- [ ] **Üst yönetim ismi var** → CEO + YK
- [ ] **Basın takibi** → İletişim Başkanlığı ([İLETİŞİM YÖNETİCİSİ]) koordinasyon
- [ ] **[BORU HATTI PROJESİ] / hükümetlerarası anlaşma alanı** → dış uzman + üst yönetim

## Çıktı

```markdown
[ÜST BAŞLIK]

# İdari Dava Hazırlık — [İdari işlem]

## ⚠️ İnceleyen notu
- **Görevli mahkeme:** [tespit] (gerekçe: [...])
- **Tebliğ tarihi:** GG.AA.YYYY → **Süre sonu: GG.AA.YYYY (kalan: N gün)** 🔴/🟠/🟡
- **Yürütmenin durdurulması:** evet (gerekçe: [...])
- **Kaynaklar:** Yarg MCP (Danıştay [N] + kurum [N]); Mevzuat MCP
- **Eskalasyon:** [tetiklendi mi?]
- **KAP açıklama:** [N/A / hazırlanıyor]
- **Reviewer bekleyen:** N adet

## İdari işlem analizi
[tablo: işlem tipi, kurum, tarih, talep, dayanak]

## Görevli mahkeme tespiti
[karar + İYUK madde gerekçesi]

## Hukuki argümanlar
[A-E: yetkisizlik, şekil, sebep, konu, amaç]

## Yürütmenin durdurulması analizi
[telafisi güç zarar + hukuka aykırılık argümanları]

## Emsal Danıştay/kurum kararları
[Yarg MCP'den çekilen tablolar]

## Dava dilekçesi taslağı (dış vekil revize için)
[yukarıdaki şablon — doldurulmuş]

## Sonraki adımlar

> 1. **Dış idari avukatı brief** — `/litigation-legal:outside-counsel-brief` (idari dava varyantı)
> 2. **Eskalasyon notu** — Başkan/CEO için 1 sayfa
> 3. **KAP açıklama metni** ([HALKA AÇIK İŞTİRAK] ilgili büyük etki)
> 4. **EPDK proaktif görüş** alternatifi düşünme — `/administrative-legal:epdk-proaktif-gorus` (dava açmadan önce dialog şansı)
> 5. **Daha fazla bilgi** — [...]

**One question I'd ask:** [örn. "Bu daire son 12 ayda benzer [ŞİRKET ADI]/sektör davalarında bir eğilim gösterdi mi? Davayı kazanma ihtimalini değiştirir."]
```

---

## /administrative-legal:idari-para-cezasi-itiraz

---
name: idari-para-cezasi-itiraz
description: >
  Çevre Bakanlığı, EPDK, KVKK, Rekabet, BDDK, SPK gibi düzenleyici kurumların
  idari para cezası kararlarına karşı iptal davası hazırlık. İYUK m. 7 + m. 27
  yürütmenin durdurulması, görevli mahkeme (ilgili il İdare Mahkemesi veya Ankara).
  `idari-dava-prep` skill'inin idari ceza odaklı varyantı.
user-invocable: true
---

# İdari Para Cezası İptal Davası

## ⏰ Süre

İdari para cezası tebliğinden **30 gün** (İYUK m. 7). Hak düşürücü.

## Tetik

> Hangi kurumun idari para cezası?
> - Çevre Bakanlığı (2872 ÇK) — [İşletme Yeri] çevre ihlali
> - EPDK (5015 PPK / 4646 DGPK / 6446 EPK) — lisans şartı ihlali
> - KVKK (6698) — veri ihlali
> - Rekabet Kurumu (4054) — Rekabet ihlali
> - BDDK / SPK / KGK — finansal düzenleyici
> - Çalışma Bakanlığı / SGK — İSG ihlali / sigorta primi

## Önemli: Tahsil + ceza ayrı

İdari para cezası kararı iki ayrı süreç:
1. **İptal davası** (İYUK m. 7 — 30 gün) → İdare Mahkemesi
2. **Tahsil** (AATUHK 6183) → Vergi Dairesi tarafından

**Tahsil paralel başlar.** İptal davasında **yürütmenin durdurulması (İYUK m. 27)** alınmazsa, dava sürerken para tahsil edilebilir.

## Görevli mahkeme

| Ceza kaynağı | İlk derece |
|---|---|
| Çevre Bakanlığı merkez | Ankara İdare Mah. |
| Çevre İl Müdürlüğü (İzmir-[İşletme Yeri]) | İzmir İdare Mah. |
| EPDK Kurul kararı | Ankara İdare Mah. |
| KVKK Kurul | Ankara İdare Mah. |
| Rekabet Kurulu | Ankara İdare Mah. |
| BDDK | Ankara İdare Mah. |
| SPK | Ankara İdare Mah. |
| ÇSGB (İSG cezası) | İlgili il İdare Mah. ([İşletme Yeri] için İzmir) |

## Adımlar

### 1. Ceza analiz

| Soru | Cevap |
|---|---|
| Kurum | [...] |
| Karar tarihi + sayı | [...] |
| Ceza tutarı | TL |
| Hukuki dayanak (idarenin gösterdiği) | [Kanun madde] |
| Tebliğ tarihi | GG.AA.YYYY |
| Süre sonu | GG.AA.YYYY (kalan: N gün) |

### 2. Bir önceki uygulama / emsal

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="<ilgili — 10. çevre, 13. enerji-finans>",
  arananKelime="<kurum> idari para cezası iptal",
  baslangicTarihi="2022-01-01"
)
```

### 3. Hukuki argümanlar (idari ceza-spesifik)

- **Yetkisizlik** — kurum bu cezayı vermeye yetkili mi?
- **Şekil eksikliği** — savunma alınmadı, tebligat hatalı, gerekçe yetersiz
- **Sebep yokluğu** — ihlal fiilen gerçekleşti mi (delil yetersiz)?
- **Konu hukuka aykırılığı** — ceza miktarı kanunda öngörülen aralık dışında
- **Amaç hukuka aykırılığı** — kurum başka bir amaç güdüyor
- **Mücbir sebep** — ihlal mücbir sebepten kaynaklandı mı?
- **İdarenin bekletme süresi** — soruşturma çok uzadıysa zaman aşımı

### 4. Yürütmenin durdurulması (m. 27)

**Telafisi güç zarar:** Ceza tutarı yüksekse nakit etkisi; EPDK lisans askıya alma ek tehdit; çevre cezası yatırım+itibar etkisi.

**Açıkça hukuka aykırılık:** Yukarıdaki en güçlü argüman.

### 5. [ŞİRKET ADI]-özel kontroller

- [ ] **Ceza tutarı > 10M TL** → CLCO + CEO eskalasyon
- [ ] **[İşletme Yeri] İSG/çevre olayı kaynaklı** → litigation-legal `isg-incident-response` ile koordine
- [ ] **[HALKA AÇIK İŞTİRAK] ilgili** → KAP açıklama kontrolü
- [ ] **EPDK lisans askıya alma riskini içeriyor mu** → derhal CLCO + iş birimi başkanı
- [ ] **Basın etkili** → İletişim Başkanlığı
- [ ] **Compliance koordinasyon** (KVKK → [KVKK SORUMLUSU/DPO]; Rekabet/EPDK → [UYUM DİREKTÖRÜ]/[REGULATORY COMPLIANCE MÜDÜRÜ])

## Çıktı

```markdown
[ÜST BAŞLIK]

# İdari Para Cezası İptal — [Kurum / Karar no]

## ⚠️ İnceleyen notu
- **Kurum + ceza tutarı:** [...]
- **Süre kalan:** [N gün] 🔴/🟠
- **Görevli mahkeme:** [Ankara/İzmir İdare Mah.]
- **Yürütmenin durdurulması:** evet (gerekçe: [...])
- **Tahsil paralel başladı mı:** evet/hayır → AATUHK tehir-i icra ek yol
- **Kaynaklar:** Yarg MCP (Danıştay [N])
- **Reviewer bekleyen:** N adet

[Ceza analizi + argümanlar + dilekçe taslak]

## Sonraki adımlar

> 1. **Dış idari avukatı brief**
> 2. **CLCO + CFO eskalasyon** (büyük tutar)
> 3. **Compliance koordinasyon** (kurum bazlı)
> 4. **KAP açıklama metni** ([HALKA AÇIK İŞTİRAK] ilgili)
> 5. **Tehir-i icra paralel** (tahsil başladıysa)

**One question I'd ask:** [örn. "Bu ceza kurumun yıllık ortalamasının üstünde mi? Cezalar genelde benzer ölçekte mi yoksa [ŞİRKET ADI]'a karşı agresif mi?"]
```

---

## /administrative-legal:istinaf-temyiz-prep

---
name: istinaf-temyiz-prep
description: >
  İlk derece İdare Mahkemesi kararı sonrası BİM istinaf (İYUK m. 45 — 30 gün) veya
  BİM kararı sonrası Danıştay temyiz (İYUK m. 46 — 30 gün) hazırlık. İstinaf vs.
  temyiz seçeneği, daire bağlayıcılığı, kesin karar durumları, dilekçe taslağı.
user-invocable: true
---

# İstinaf / Temyiz Hazırlık

## ⏰ ÖN-KONTROL — SÜRE

> İlk derece veya BİM kararı tebliğ tarihi nedir?
> - **BİM istinaf süresi (İYUK m. 45):** 30 gün
> - **Danıştay temyiz süresi (İYUK m. 46):** 30 gün
> Hak düşürücü.

## Aşama tespiti

> Şu an hangi aşamadayız?
> A. İdare Mahkemesi karar verdi → istinaf (BİM) düşünüyoruz
> B. BİM karar verdi → temyiz (Danıştay) düşünüyoruz
> C. Danıştay temyiz inceledi, bozma kararı → bu durumda mahkemeye dön (m. 50/3)
> D. Danıştay onama → kesinleşti, AYM bireysel başvuru mu (hak ihlali)?

## A: İdare Mahkemesi → BİM İstinaf

### Bazı kararlar istinafa kapalı (kesin)

İYUK + bağımlı kanunlar ile bazı kararlar **kesin** olarak verilir, istinafa kapalı. Örnek:
- Eşik tutarın altındaki vergi davaları (vergi-legal kapsamı)
- Bazı KİK iptal davaları (özel kanunda kesin)

→ Bu durumda **doğrudan AYM bireysel başvuru** (hak ihlali ise) düşünülebilir.

### İstinaf incelemesi tipi

BİM:
- **Maddi olay yeniden inceleme** yetkisi var (Yargıtay'dan farklı olarak)
- Bozma yerine **kendisi karar verebilir**
- İlk derece kararın hem hukuka uygunluğu hem maddi gerçeklik açısından değerlendirilir

### Dilekçe taslağı (BİM istinaf)

```markdown
ANKARA BÖLGE İDARE MAHKEMESİ İDARE DAVA DAİRESİ BAŞKANLIĞINA
(veya ilgili BİM)

İSTİNAF EDEN (DAVACI): [ŞİRKET ADI] A.Ş.
Vekili: [...]

KARŞI TARAF (DAVALI): [İdare]

İSTİNAF KONUSU:
[İdare Mahkemesi adı] [tarih, esas, karar no] sayılı kararın
istinaf incelemesi sonucu **kaldırılması** ile [orijinal talebimizin] kabulü talebidir.

KARARIN TARİHİ ve İLAMI:
Tebliğ: GG.AA.YYYY
Süre sonu: GG.AA.YYYY (kalan: N gün)

I. KARARIN HUKUKA AYKIRILIĞI

A. Maddi olay yanlış tespit edilmiştir [argüman + delil]
B. Hukuki dayanak yanlış uygulanmıştır [argüman]
C. Usul kurallarına uyulmamıştır [varsa]

II. SONUÇ

İdare Mahkemesi kararının kaldırılarak [dava dilekçesinin sonuç kısmındaki taleplerin] kabulüne karar verilmesi saygıyla arz olunur.

EKLER:
1. Vekaletname
2. İlk derece kararı + dosya örneği
3. Yeni deliller (varsa — İYUK m. 21)
```

## B: BİM → Danıştay Temyiz

### Bazı BİM kararları kesin (temyize kapalı)

İYUK m. 46 — bazı BİM kararları **temyiz edilemez:**
- Eşik tutarın altındaki (yıllık güncellenir)
- Bazı özel idari konular (kanunla kesin)

→ Kesin BİM kararına karşı **AYM bireysel başvuru** (hak ihlali ispatıyla).

### Danıştay temyiz incelemesi (İYUK m. 49)

Danıştay sadece **hukuka uygunluk** denetler:
- a) Görev / yetki dışı işe bakılmış
- b) Hukuka aykırı karar
- c) Usul hatası — kararı etkileyebilecek nitelikte

**Bozma → kararı veren mercie geri gönderir.** Merci uyabilir veya direnme kararı verebilir → İDDK temyiz.

### Daire seçimi (temyiz aşamasında)

[ŞİRKET ADI] ilgili daireler (CLAUDE.md'de detay):

- 13. Daire: EPDK, Rekabet, BDDK, SPK, KİK
- 10. Daire: Çevre genel
- 14. Daire: ÇED
- 8. Daire: İmar/belediye
- 5. Daire: Genel idari (memur, yabancı çalışan izni)

### Dilekçe taslağı (Danıştay temyiz)

```markdown
DANIŞTAY [X.] DAİRESİ BAŞKANLIĞINA
(Kararı veren BİM aracılığıyla — İYUK m. 48)

TEMYİZ EDEN (DAVACI/DAVALI):
[ŞİRKET ADI] A.Ş.
Vekili: [...]

KARŞI TARAF: [İdare]

TEMYİZ KONUSU:
[BİM adı + dairesi] [tarih, esas, karar no] sayılı kararın temyizen incelenerek
**bozulması** talebidir.

KARARIN TARİHİ ve TEBLİĞİ:
Tebliğ: GG.AA.YYYY
Süre sonu: GG.AA.YYYY (kalan: N gün — İYUK m. 46)

I. KARARIN HUKUKA AYKIRILIĞI (İYUK m. 49/2)

A. Görev/yetki ihlali (varsa)
B. Hukuka aykırı karar:
   1. [Argüman 1 + emsal Danıştay/İDDK kararı]
   2. [Argüman 2]
C. Usul hatası (varsa)

II. YÜRÜTMENİN DURDURULMASI (devam ediyorsa)

[İlk derece veya BİM kararıyla yürütme durdurmadı ise temyizde tekrar talep]

III. SONUÇ

BİM kararının bozulması ve [orijinal taleplerimizin] kabulü ile davalı idare aleyhine yargılama gideri ve vekalet ücretine hükmedilmesi saygıyla arz olunur.

EKLER:
1. Vekaletname
2. BİM kararı + dosya
3. Yeni emsal kararlar (eğer kararlar sonradan çıktıysa)
```

## C: Danıştay bozma → mahkemeye dönüş (İYUK m. 50)

Danıştay bozdu, dosya BİM'e gönderildi. İki seçenek:
- **BİM uyar** (m. 50/2) — bozmaya uygun yeni karar verir
- **BİM ısrar eder** (m. 50/3) — bozmaya katılmaz, eski kararı tekrar verir
  - Bu durumda ısrar kararı **İDDK'ya temyiz** edilir (m. 50/4)
  - İDDK kararı **bağlayıcıdır** (m. 50/5)

## D: Karar kesinleşti → AYM bireysel başvuru

İdari yargı tükenince ve **temel hak ihlali** varsa (mülkiyet hakkı, adil yargılanma, vs.) AYM bireysel başvuru:
- **30 gün** içinde (kararın kesinleşmesinden)
- Anayasa Mahkemesi'ne, **mülkiyet hakkı** veya **adil yargılanma hakkı ihlali** argümanıyla
- **Stratejik dava** — büyük tutarlı veya ilkesel dosyalarda

## Yarg MCP

```
# Daire bazlı temyiz emsali
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="<ilgili>",
  arananKelime="<konu>",
  baslangicTarihi="2022-01-01"
)

# İDDK kararları (bağlayıcı)
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="İdari Dava Daireleri Kurulu",
  arananKelime="<konu>",
  baslangicTarihi="2020-01-01"
)

# AYM bireysel başvuru
mcp__claude_ai_Yarg_MCP__search_anayasa_unified(
  arananKelime="<konu> mülkiyet hakkı ihlali",
  yil="2024"
)
```

## [ŞİRKET ADI]-özel

- Temyiz/istinaf karar dava açma yetkisi — practice profile eskalasyon matriksinde
- [HALKA AÇIK İŞTİRAK] ilgili → KAP açıklama
- Stratejik bozma kararları → CEO + Başkan bilgi

## Çıktı

```markdown
[ÜST BAŞLIK]

# İstinaf / Temyiz Hazırlık — [Dosya]

## ⚠️ İnceleyen notu
- **Aşama:** A/B/C/D
- **Karar veren merci:** [...]
- **Süre kalan:** [...]  🔴/🟠
- **Bizim için karar:** [İstinaf/Temyiz başvur / Başvurma]
- **Kaynaklar:** Yarg MCP [N], Mevzuat MCP
- **KAP açıklama:** [N/A / hazırlanıyor]
- **Reviewer bekleyen:** N adet

[Aşamaya göre içerik — dilekçe taslak + emsal + yürütmenin durdurulması]

## Sonraki adımlar

> 1. **Dış idari avukatı brief**
> 2. **Eskalasyon notu** (büyük tutar/stratejik)
> 3. **Karar verme paketi** (Direktör/Başkan onayı için)
> 4. **AYM bireysel başvuru paralel hazırlık** (Danıştay onama olasılığı yüksek ise)
> 5. **Daha fazla bilgi** — [...]

**One question I'd ask:** [örn. "BİM'in bu karara karşı geçmişte Danıştay tarafından bozulma oranı nedir? Temyiz başarı şansını etkiler."]
```

---

## /administrative-legal:kik-ihale-itiraz

---
name: kik-ihale-itiraz
description: >
  Kamu İhale Kurumu (KİK) süreçleri: ihale şartnamesi/ilanına itiraz, ihale
  kararına şikayet (4734 KİK 55), KİK Kurul kararına karşı dava (Ankara İdare
  Mah. → BİM → Danıştay 13. Daire). Devlet ihalelerinde teklif veren/itiraz eden
  taraf [ŞİRKET ADI] ([ELEKTRİK SANTRALİ] benzeri enerji ihaleleri).
user-invocable: true
---

# KİK İhale İtirazı

## İki süreç paralel

### A. KİK İdari Şikayet (4734 KİK m. 55-57)

Doğrudan dava değil — **önce KİK'e şikayet**:

1. **Şartname/ilana itiraz:** Şartname/ilanın yayımından **10 gün** içinde
2. **İhale kararına itiraz:** Karar tebliğinden **10 gün** içinde
3. KİK Kurul **20 iş günü** içinde karar verir (bazen uzar)
4. KİK kararı olumlu/olumsuz → tatmin etmezse dava

### B. KİK Kurul kararına karşı dava

KİK Kurul kararı **idari işlem** → İYUK m. 7:
- **İYUK 30 gün** Ankara İdare Mahkemesi'ne iptal davası
- BİM istinaf → Danıştay 13. Daire temyiz

## [ŞİRKET ADI]-özel

İhale sıklığı:
- **Devlet ihalelerine teklif veren** (Elektrik üretim teşvik ihaleleri — [ELEKTRİK SANTRALİ] benzeri)
- **Müşteri olarak devlet ihalesi** (TÜPRAŞ rakip, EÜAŞ vs.)
- **Sektörel düzenleyici ihaleler** (EPDK destek ihaleleri)

## Adımlar

### 1. Hangi aşama?

> A. Şartname/ilan henüz yayımlandı, sorunlu — 10 gün şikayet süresi
> B. İhaleye katıldık, kararı bekliyoruz / aleyhe çıktı — 10 gün şikayet
> C. KİK şikayetimize ret cevap geldi — 30 gün dava
> D. KİK rakibimizin lehine karar verdi (biz kazandık ama itiraz var) — savunma

### 2. KİK şikayet dilekçesi (4734 m. 55)

```markdown
KAMU İHALE KURUMU BAŞKANLIĞINA
ANKARA

Konu: [İdare adı] tarafından yapılan [ihale adı + numara] hakkında şikayet

İstekli/İstekli adayı: [ŞİRKET ADI] A.Ş. (veya bağlı şirket)
İhaleyi yapan idare: [...]
İhale konusu: [...]
İhale tarih + numara: [...]

ŞİKAYET KONUSU:
[Şartname maddesinde / ilanda / ihale kararında]
[hata/yanlışlık/hukuka aykırılık tarif]

ŞİKAYET GEREKÇELERİ:
1. [Madde — KİK Kanunu / Tebliği]
2. [...]

SONUÇ ve TALEP:
1. Şikayetimizin kabulü
2. [İhale iptali / şartname düzeltilmesi / yeniden değerlendirme]

Tarih: GG.AA.YYYY
İstekli (vekil): [imza]

Ekler:
- Şartname/ilan
- İhale kararı (varsa)
- Belgelerimiz
```

### 3. KİK ret sonrası dava dilekçesi

`/administrative-legal:idari-dava-prep` skill ile birlikte — KİK kararı normal idari işlem olarak ele alınır:
- Ankara İdare Mahkemesi
- 30 gün
- Yürütmenin durdurulması talep

### 4. Yarg MCP

```
mcp__claude_ai_Yarg_MCP__search_kik_v2_decisions(
  arananKelime="<konu>",
  baslangicTarihi="2022-01-01"
)

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="13. Daire",
  arananKelime="KİK karar iptal ihale",
  baslangicTarihi="2022-01-01"
)
```

### 5. [ŞİRKET ADI] koordinasyon

- **İhale Komisyonu** (iç) — iş birimi tarafında
- **Senior Legal Counsel** — KİK şikayet + dava hazırlık
- **Direktör ([HUKUKİ DİREKTÖR 1]/[HUKUKİ DİREKTÖR 2])** — onay
- **CLCO** — büyük ihale / stratejik etki
- **Compliance ([UYUM DİREKTÖRÜ])** — kamu ihale uyumu

## Çıktı

```markdown
[ÜST BAŞLIK]

# KİK İhale İtirazı — [İhale]

## ⚠️ İnceleyen notu
- **Aşama:** A/B/C/D
- **Süre kalan:** [10 gün KİK şikayet / 30 gün İdare Mah. dava]
- **İhale değeri:** [TL]
- **Kaynaklar:** Yarg MCP (KİK [N], Danıştay 13. [N]); Mevzuat MCP (4734 KİK K.)
- **İhale komisyonu koordinasyon:** [evet/hayır]
- **Reviewer bekleyen:** N adet

[Aşamaya göre içerik — KİK şikayet dilekçesi / dava dilekçesi]

## Sonraki adımlar

> 1. **KİK şikayet sun** (A/B) veya **Ankara İdare Mah. dava** (C)
> 2. **İhale komisyonu brief** — iç koordinasyon
> 3. **Dış kamu ihale avukatı brief** (büyük ihale)
> 4. **Direktör onayı**
```

---

## /administrative-legal:rekabet-kurulu-itiraz

---
name: rekabet-kurulu-itiraz
description: >
  Rekabet Kurulu kararına karşı iptal davası hazırlık — 4054 sayılı Rekabetin
  Korunması Hakkında Kanun. İlk derece Ankara İdare Mahkemesi → BİM → Danıştay 13.
  Daire. [ŞİRKET ADI] vertical entegrasyon (rafineri + [petrokimya iştiraki] + terminal + dağıtım)
  Rekabet Kurumu dikkati altında.
user-invocable: true
---

# Rekabet Kurulu Kararı İtiraz

## Tetik

Rekabet Kurulu kararı tipleri:
- **Birleşme/devralma izni** red veya koşullu izin
- **Hâkim durum ihlali** kararı + idari para cezası
- **Anlaşma yasağı** ihlali (m. 4)
- **Hâkim durumun kötüye kullanılması** (m. 6)
- **Pazar paylaşımı** soruşturması sonucu

## Süreç

```
Rekabet Kurulu kararı (idari işlem) →
İYUK m. 7 → 30 gün →
Ankara İdare Mahkemesi (ilk derece) →
Ankara BİM (istinaf) →
Danıştay 13. Daire (temyiz)
```

⚠️ **Rekabet Kurulu kararı doğrudan Danıştay'a gitmez** (artık eski uygulama değişti). 4054 m. 55 referansı yanlış uygulanmamalı.

## [ŞİRKET ADI]-özel risk

[ŞİRKET ADI] vertical entegrasyon profili Rekabet dikkatinde:
- **[RAFİNERİ] (üst kademe)** + **[HALKA AÇIK İŞTİRAK] (orta kademe petrokimya)** + **[ŞİRKET ADI] Terminal (lojistik)** + **[ŞİRKET ADI] Enerji Ticaret (dağıtım)** = baştan sona zincir kontrolü
- **[ÖZEL ENDÜSTRİ BÖLGESİ]** içinde dikey entegre yapı
- **EPC tedarik zinciri** (yan kuruluşlardan tedarik)
- **Doğal gaz dağıtım eskisi** ([DAĞITIM İŞTİRAK 1]/[DAĞITIM İŞTİRAK 2] devir öncesi pazar payı yüksek)

Rekabet Kurulu **olası ihlal alanları:**
- Dikey integrasyon → bağımsız oyuncular için pazar erişim engeli
- Bağlı tedarikçi imtiyazları → ayrımcılık
- Fiyat parlatma → predatory pricing
- Pazar paylaşımı (intra-group [ANA ORTAK] ile)

## Hukuki argümanlar

- **Yetkisizlik:** Rekabet Kurulu bu konuda yetkili mi (sektör düzenleyici EPDK paralel)?
- **Pazar tanımı yanlış:** Kurulun belirlediği ilgili ürün/coğrafi pazar dar mı?
- **Hâkim durum yok:** Pazar payı %X'in altında, hâkim sayılmayız
- **Etki yok:** Eylemimiz rekabeti gerçekten kısıtladı mı?
- **Mücbir sebep / makul gerekçe:** Eylem ticari mantıkla açıklanabilir
- **Ceza orantısız:** Cironun %X'i — kanunda öngörülen aralığın üstünde

## Yarg MCP

```
mcp__claude_ai_Yarg_MCP__search_rekabet_kurumu_decisions(
  arananKelime="<konu>",
  baslangicTarihi="2022-01-01"
)

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="13. Daire",
  arananKelime="Rekabet Kurulu karar iptal",
  baslangicTarihi="2022-01-01"
)
```

Rekabet Kurulu kararları **bağlayıcı emsal** değil ama Kurulun tutarlılığı için referans. Danıştay 13. Daire kararları temyiz için.

## [ŞİRKET ADI] koordinasyon

- **CLCO ([CLCO ADI])** + dış rekabet avukatı 24h
- **CEO (Ibadov)** — büyük tutar / stratejik için
- **İletişim ([İLETİŞİM YÖNETİCİSİ])** — basın etkili olabilir
- **[HALKA AÇIK İŞTİRAK] ilgili ise** → KAP açıklama
- **Compliance ([UYUM DİREKTÖRÜ])** — rekabet uyumu kapsamı

## Çıktı

`/administrative-legal:idari-dava-prep` skill'i ile kombine — bu skill rekabet-özel argümanları ekler.

```markdown
[ÜST BAŞLIK]

# Rekabet Kurulu Kararı İtiraz — [Karar no]

## ⚠️ İnceleyen notu
- **Kararın özeti:** [tip + tutar + koşullar]
- **Süre kalan:** [N gün]
- **Vertical entegrasyon ilişkisi:** [evet/hayır]
- **Pazar tanımı doğru mu:** [değerlendirme]
- **Kaynaklar:** Yarg MCP (Rekabet Kurulu [N], Danıştay 13. [N])
- **CEO bilgisi:** [✓/✗]
- **KAP açıklama:** [N/A / hazırlanıyor]
- **Reviewer bekleyen:** N adet

[Kararın analizi + hukuki argümanlar + emsal + dava dilekçesi taslağı]

## Sonraki adımlar

> 1. **Dış rekabet avukatı brief** — `/litigation-legal:outside-counsel-brief`
> 2. **CEO + CLCO eskalasyon**
> 3. **Compliance + iş birimi koordinasyon** — yapısal etki değerlendirmesi
> 4. **KAP açıklama** ([HALKA AÇIK İŞTİRAK] büyük etki)
> 5. **Avrupa Komisyonu paralel** (eğer AB Rekabet bağlantısı varsa — Madde 102 TFEU)
```

---

