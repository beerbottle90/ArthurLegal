---
name: litigation-legal-settlement-eval
description: >
  Sulh teklifi geldiğinde veya verilecekken kapsamlı değerlendirme: tutar pencere
  analizi (TBK m. 53 destek tazminatı, AAÜT vekalet ücreti, yargılama masrafı,
  damga vergisi), risk-benefit matriksi, emsal sulh tutarları (ArthurLegal MCP (`tr_`)),
  eskalasyon kararı, müzakere paketi. [Müvekkil] sulh yetki matriksine entegre.
user-invocable: true
---

# Settlement Evaluation — Sulh Teklifi Değerlendirme

## Matter context

Aktif matter zorunlu — sulh tek bir davaya ait olur.

## Destination check

- **İç değerlendirme + Hukuk Direktörü onayı** → "GİZLİDİR – HUKUK MÜŞAVİRLİĞİ DAHİLİ"
- **CEO/Başkan eskalasyon paketi** → "GİZLİDİR – CEO/BAŞKAN ONAYI İÇİN"
- **Karşı tarafa karşı sulh teklif metni** → üst başlık çıkar, "TASLAK" + dış vekil onayı sonrası

## Amaç

Sulh kararı en az 5 boyutta hesaplanır:

1. **Hukuki maruziyet** — eğer dava devam ederse muhtemel mahkeme kararı tutarı
2. **Maliyetler** — vekalet ücreti, yargılama gideri, dış vekil saatleri, içeride harcanan zaman
3. **Vergi/damga** — sulh anlaşmasının damga vergisi (DVK Tablo I)
4. **Reputational risk** — basın, müşteri algısı, çalışan moral
5. **Ekosistem etkisi** — emsal oluşturma riski, sektörde diğer dosyalar

## Adımlar

### 1. Karşı tarafın teklifini incele (veya kendi teklifimizi oluştur)

| Soru | Cevap |
|---|---|
| Karşı tarafın talebi (dava açılışındaki rakam) | [tutar] |
| Şu anda sunduğu sulh rakamı | [tutar] |
| **Düşüş %** | (talep - sulh) / talep × 100 |
| Talep edilen vade | peşin / taksit / koşullu |
| Eklenen koşullar | (gizlilik, ibra, ödül kabulü) |
| Vekalet ücreti dahil mi? | evet/hayır |
| Damga vergisi kim öder? | [açıkça yazılı mı?] |

Karşı taraftan gelen teklifte **gizli koşullar** olabilir (örn. "şirketin halka açıklaması yasak", "diğer çalışanlara öneri yapılmaz"). Bunlar hukukidan çok ticari/itibar etkisi taşır.

### 2. Hukuki maruziyet — kötümser senaryo

Eğer dava devam ederse, **muhtemel mahkeme kararı** ne olur?

- **Emsal Yargıtay/Danıştay kararları** (ArthurLegal MCP (`tr_`)):
```
tr_ictihat_ara(
  query="<dava konusu>",
  chamber="<daire kodu, ör. H9, C12, D13, HGK, IDDK>",
  date_from="2023-01-01"
)
```
- Kazanma olasılığı %
- Kaybedersek hangi tutarı ödemek zorundayız

**İSG kazasında tazminat hesabı (KRİTİK):**

| Kalem | Hesap |
|---|---|
| **Maddi zarar** (tedavi, kayıp ücret) | Belgeli, kesin |
| **Manevi tazminat** | Yargıtay HGK eğilim (genelde 50K-500K TL arası ölümlü kazada; ağırlık takdiri) (doğrulanmadı) |
| **Destek tazminatı (TBK m. 53)** | Yaşam süresi × destek oranı × pasif sermaye katsayısı (Yargıtay HGK 2017/123 metod) |
| **Faiz** | Yasal faiz (TBK + 3095 — değişken) |
| **Vekalet ücreti** | AAÜT (Türkiye Barolar Birliği) — genelde davacı vekiline %12-15 (doğrulanmadı) |
| **Yargılama gideri** | Bilirkişi, tanık masrafı |

**Toplam beklenen maruziyet:** [TL]

### 3. Maliyet hesabı (sulh yaparsa vs. devam ederse)

| Kalem | Sulh yaparsak | Dava devam ederse |
|---|---|---|
| Karşı tarafa ödeme | [sulh tutarı] | [muhtemel karar tutarı] |
| Karşı taraf vekalet (AAÜT) | dahil / hariç | %12-15 × karar tutarı (doğrulanmadı) |
| Dış vekil ücreti (bizim) | [bittiği tutar] | [tahmin: + N saat × saat ücreti] |
| Yargılama masrafı | yok | [bilirkişi, harç, posta] |
| Damga vergisi (DVK Tablo I) | sulh tutarı × ‰9,48 | yok (adli yargı ilamı (1) sayılı tabloda yer almaz — DVK m. 1; hakem kararı ise tabidir: (1) sayılı tablo II-1) |
| İç zaman (in-house) | düşük | yüksek (her duruşma 1-2 gün) |
| **TOPLAM** | [...] | [...] |

⚠️ **Damga vergisi unutulmaz:** 5M TL sulh = ~47.400 TL damga. Sulh anlaşmasında "kim ödeyecek?" netleştirilmeli. Standart: yarı yarıya.

### 4. Reputational ve stratejik risk

- [ ] **Basına yansıma riski:** Dava devam ederse duruşma açık, basın takibi olabilir. Sulh ise gizlilik klozu eklenebilir.
- [ ] **Çalışan algısı (İSG davasında):** Düşük sulh = "şirket çalışana değer vermiyor" algısı; yüksek sulh = "şirket sorumluluk kabul ediyor" algısı.
- [ ] **Sendika etkisi ([SEKTÖR SENDİKASI]):** TİS müzakerelerinde geçmiş davalar argüman.
- [ ] **Yatırımcı algısı ([HALKA AÇIK İŞTİRAK]):** Yüksek tutarlı sulh KAP açıklaması gerektirebilir, hisse fiyatına etki.
- [ ] **Emsal oluşturma riski:** Bu sulhten sonra benzer davalar açılır mı? (örn. [TESİS LOKASYONU]'da bir çalışana 5M TL sulh = diğer çalışan davaları için baseline)
- [ ] **Düzenleyici dikkat:** EPDK / Çevre Bakanlığı / SPK dikkatini çekebilir mi?

### 5. [Müvekkil] sulh yetki matriksi kontrolü

Practice profile → `## Eskalasyon ve onay matrisi` → sulh tutar kademelerine bak:

- < 500K TL → Counsel + Direktör
- 500K - 5M TL → Direktör onay, Başkan bilgi
- 5M - 50M TL → Başkan onay, CEO bilgi
- > 50M TL veya stratejik → CEO + YK

**Tutardan bağımsız eskalasyon kontrolü:**
- [ ] halka açık iştirak ilgili mi? → KAP açıklama hazırlığı
- [ ] [TESİS LOKASYONU] İSG kazası mı? → otomatik Başkan
- [ ] Üst yönetim ismi var mı? → CEO + YK
- [ ] Basına yansımış mı? → İletişim Başkanlığı koordinasyon

### 6. Müzakere stratejisi

Sulh kararı verildikten sonra **müzakere paketi:**

- **Yürürlüğe giriş ön-koşul** (örn. ibra mektubu, KAP onayı)
- **Ödeme takvimi** (peşin avantajlı mı, taksitli mi)
- **Gizlilik klozu** (genelde her iki tarafın talebi)
- **Karşılıklı feragat** (gelecekteki dava açma hakkı)
- **Cezai şart** (sulhe aykırı paylaşım için)
- **Vergi yansımaları** (KDV, stopaj, gelir vergisi — tarafların pozisyonu)
- **Yetki ve hukuk seçimi** (genelde Türk hukuku + İstanbul ATM)

### 7. Yazılı sulh anlaşması taslağı

Karar verildiyse:

```markdown
SULH ANLAŞMASI

Taraflar:
- [Müvekkil] ("[Müvekkil]")
- [Karşı taraf] ("Mağdur" / "Karşı Taraf")

Konu: [İhtilaf konusu]

Açıklamalar:
[önceki dava bilgisi, esas no, mahkeme]

Anlaşma maddeleri:
1. [Müvekkil], Mağdur'a [tutar] TL ödemeyi kabul eder; ödeme tarihi [tarih].
2. Mağdur, ödemenin alınmasının ardından [Müvekkil]'a karşı bu konudaki tüm taleplerinden feragat ettiğini ve ibra ettiğini beyan eder.
3. Bu anlaşma ve içeriği taraflarca gizli tutulacaktır; ihlali halinde [cezai şart] TL cezai şart ödenir.
4. Damga vergisi taraflarca yarı yarıya ödenir.
5. Uygulanacak hukuk: Türk hukuku. Yetki: [mahkeme/tahkim].

İmza:
[[Müvekkil] yetkilisi] _______
[Mağdur / vekili] _______
Tarih: GG.AA.YYYY
```

**Bu taslak DIŞ VEKİL ONAYINDAN GEÇMEDEN imzalanmaz.**

## Çıktı şablonu

```markdown
[ÜST BAŞLIK]

# Sulh Teklifi Değerlendirme — [Dosya slug]

## ⚠️ İnceleyen notu
- **Karar:** Sulh ÖNERİLİR / SULH ÖNERİLMEZ / Müzakere DEVAM
- **Önerilen sulh tutarı aralığı:** [TL min - TL max]
- **Eskalasyon noktası:** [Counsel/Direktör/Başkan/CEO]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [N emsal], ArthurLegal MCP (`tr_`) [X madde]
- **KAP açıklama:** [N/A / gerekli / hazırlanıyor]
- **Reviewer karar bekleyen:** N adet
- **Önerilen son aksiyon:** [1 cümle]

## Karşı tarafın teklifi

| Kalem | Değer |
|---|---|
| Talep edilen | [TL] |
| Sulh teklifi | [TL] (düşüş %X) |
| Vade | [...] |
| Gizlilik klozu | [...] |
| Vekalet ücreti dahil mi? | [...] |
| Damga vergisi | [...] |

## Hukuki maruziyet (kötümser senaryo)

**Emsal kararlar:** `[ArthurLegal MCP (`tr_`) — yargitay/danistay — GG.AA.YYYY]`

[tablo: emsal davanın özelliği, karar tutarı, bizim davaya benzerlik]

**Beklenen maruziyet:** [TL aralık] — [%] kazanma olasılığı

## Maliyet karşılaştırma

| Kalem | Sulh | Devam |
|---|---|---|
| ... | ... | ... |
| **TOPLAM** | [TL] | [TL] |

**Sulh net avantaj/dezavantaj:** [TL]

## Reputational ve stratejik

- Basın riski: [değerlendirme]
- Çalışan algısı: [değerlendirme] (İSG ise kritik)
- Yatırımcı ([HALKA AÇIK İŞTİRAK]): [değerlendirme + KAP gereği]
- Emsal oluşturma: [değerlendirme]
- Düzenleyici: [değerlendirme]

## Önerilen sulh tutarı

**Aralık:** [TL min] - [TL max]
**Hedef:** [TL]
**Yetkisi:** [Counsel/Direktör/Başkan/CEO seviyesinde — neden]

## Müzakere stratejisi

[Anahtar koşullar tablosu]

## Sonraki adımlar (decision tree)

> **What next? Pick one and I'll help you build it out:**
> 1. **Hukuk Direktörü eskalasyon notu** (sulh önerisi resmi)
> 2. **CEO/Başkan paket** (büyük tutar / stratejik dava ise)
> 3. **Müzakere paketi taslağı** — karşı tarafa karşı kontroffer
> 4. **Sulh anlaşması taslağı** — onaylandıysa, dış vekil revize için
> 5. **Bekle ve izle** — karşı taraf revize teklif yapsın

**One question I'd ask that isn't in my checklist:** [örn. "Karşı taraf vekiline kişisel bonus tarzı bir çıkar bağlanmış mı? Sulh oranını yapay yükseltebilir; geçmişte böyle pattern var mı?"]
```

## Reviewer note format

Reviewer note standardı — sulh kararı **kesinlikle dış vekil görüşü + Direktör onayı** olmadan finalize edilmez; AI çıktısı bağlayıcı önerme değildir.

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
