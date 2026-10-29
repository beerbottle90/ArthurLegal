---
name: administrative-legal-epdk-proaktif-gorus
description: >
  EPDK Kurul'a proaktif görüş/talep sunma. Dava ÖNCESİ çözüm kanalı. [Müvekkil]'ın
  EPDK ile yoğun dialog modelinde temel araç. Kurul kararı çıkmadan önce yorum,
  Tebliğ taslağına görüş, lisans şartı yorumu, görüş başvurusu. [Uyum Direktörü]
  (Compliance Direktörü) + [Compliance Manager] (Regulatory Compliance Manager) ile
  koordineli hazırlanır.
user-invocable: true
---

# EPDK Proaktif Görüş Sunum

## Felsefe

büro pratiğinde **dava açmadan önce EPDK ile dialog kanalı** kullanılır:
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

- **Sorun:** [örn. "Yeni tebliğde belirlenen rapor formatı [Müvekkil] için uygulanamaz çünkü..."]
- **Etki:** [operasyonel + mali]
- **Önerimiz:** [somut alternatif]

### 2. Dayanak araştırma

- **ArthurLegal MCP (`tr_`)** — ilgili kanun/tebliğ + EPDK Kanunu (4628 + 5015 + 4646 + 6446)
- **ArthurLegal MCP (`tr_`) — Danıştay 13. Daire** — benzer konularda Danıştay yorumu (EPDK aleyhine olan emsaller bizim için anchor)
- **GİB özelge** — vergi yönü varsa
- **Sektör emsali** — diğer enerji şirketleri benzer pozisyon mu? (Tüpraş, Aygaz, Akenerji)

```
tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="D13",
  query="+EPDK +lisans +şartı +yorumu +emsal",
  date_from="2022-01-01"
)
```

### 3. Görüş sunum metni

```markdown
T.C. ENERJİ PİYASASI DÜZENLEME KURUMU [Daire/Sektör Müdürlüğü]
ANKARA

Konu: [Tebliğ/Karar adı] hakkında [Müvekkil] görüşü

Sayın Yetkilisi,

[Yayınlanan/yayınlanacak tebliğ taslağı/Kurul kararı] hakkındaki şirketimiz
görüşünü aşağıda saygıyla sunarız.

I. KONU VE ETKİ

[Düzenlemenin neyin etkilediği, [Müvekkil]/[enerji tesisi / halka açık iştirak]/[enerji üretim tesisi] üzerindeki
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

[Müvekkil]
[Yetkili imza — Compliance Direktörü [Uyum Direktörü] veya CLCO [CLCO ADI]]

Ekler:
1. Operasyonel etki analizi
2. Sektör emsalleri
3. Önerilen alternatif metin (varsa)
```

### 4. Koordinasyon

- **Hukuk:** Senior Legal Counsel — hukuki argümantasyon hazırlar
- **Compliance:** [Uyum Direktörü] + [Compliance Manager] — düzenleyici çerçeve uzmanlığı, EPDK ile ilişki
- **İş birimi:** [İş Birimi Başkanı] veya [Doğal Gaz İş Birimi Başkanı] — operasyonel detay
- **Mali İşler:** CFO ekibi ([CFO ADI]) — mali etki rakamı
- **Onay:** CLCO ([CLCO ADI]) imzalı veya yetkisi devrettiği Direktör

### 5. Takip

EPDK'dan cevap genelde 1-3 ay içinde:
- **Olumlu:** Görüş kabul edildi, taslak/karar revize → dava'ya gerek yok ✓
- **Kısmen kabul:** Müzakere devam ediyor
- **Olumsuz / sessizlik:** Dava planına geç → `/arthurlegal:administrative-legal-idari-dava-prep`

### 6. Sektör koalisyon avantajı

Bazı görüşler **sektör koalisyonu** halinde (Türkiye Petrolleri, Tüpraş, Aygaz, vs. ile birlikte) sunulursa daha güçlü. [Müvekkil] + diğerleri ortak görüş = sektör temsili.

`PETDER`, `GAZBİR`, `EBSO` gibi sektör derneklerini koordinasyon kanalı olarak kullan.

## Çıktı

```markdown
[ÜST BAŞLIK — Compliance + Hukuk koordineli iç değerlendirme]

# EPDK Proaktif Görüş — [Konu]

## ⚠️ İnceleyen notu
- **Senaryo:** A/B/C/D/E
- **Hedef:** [Tebliğ değişikliği / Kurul karar etkisi / Yorum alma / Lisans şart revizyonu]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (Danıştay 13. [N]); ArthurLegal MCP (`tr_`)
- **Compliance koordinasyon:** [Uyum Direktörü] + [Compliance Manager] ✓/⚠
- **İş birimi koordinasyon:** [[İş Birimi Başkanı]/[İş Birimi Başkanı]]
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
| idare hukuku ogretisi — DergiPark *Idare Hukuku ve Ilimleri* dergisi router tarafindan secilir; **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
