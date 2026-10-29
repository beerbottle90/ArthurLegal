---
name: administrative-legal-ced-itiraz
description: >
  ÇED (Çevresel Etki Değerlendirmesi) ret kararı geldiğinde veya ÇED süreci
  sorunlu olduğunda — büyük endüstriyel tesis için kritik. Çevre K. 2872 + ÇED Yön.
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

**büyük endüstriyel tesis için bu kritik:** [enerji tesisi / halka açık iştirak] ÇED yenileme + kapasite artırımı dosyalarında **30 günlük süreye** sıkı uyum şart. Geç kalma = hak düşürücü süre = yatırım blokesi.

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
- **İl müdürlüğü kararı** (yerel etkili) → ilgili **İl İdare Mahkemesi** ([tesis yeri] için ilgili il İdare Mah.) → **DOĞRUDAN Danıştay temyiz**

⚠️ İstinaf (BİM) aşaması ATLANIR — bu önemli, çünkü genel idari davalarda BİM normal kademe.

## sektöre-özel risk

**büyük endüstriyel tesis sürekli ÇED yenileme + değişiklik süreçlerinde:**
- [büyük enerji tesisi] kapasite artırımı
- halka açık iştirak yeni üretim hattı
- [Müvekkil terminali] kapasite genişleme
- [enerji santral] revizyonları

Her biri ÇED süreci tetikler. **Çevre Bakanlığı'nın ÇED ret kararı**:
- Yatırımı durdurur (büyük maliyet)
- Olası mevcut faaliyet kısıtlaması
- Basın/STK takibi yüksek

## ArthurLegal MCP (`tr_`)

```
tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="D14",
  query="+ÇED +ret +iptal +rafineri +petrokimya",
  date_from="2022-01-01"
)

tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="D10",
  query="+çevre +etki +değerlendirme",
  date_from="2022-01-01"
)
```

## Hukuki argümanlar (klasik ÇED itiraz)

- **ÇED komisyonu üyelerinin uzmanlığı yetersiz** — şekil itirazı
- **Bağımsız uzman görüşü göz ardı edildi** — sebep ihlali
- **AB / Türk standartlarıyla uyumlu olduğunu ispat** (BAT — best available techniques)
- **Sektör emsali yatırımların ÇED onayı** (benzer [enerji tesisi], neden bu reddedildi?)
- **Bakanlık kendi prosedürüne uymadı** (komisyon toplantı eksik, halk katılımı yetersiz)

## müvekkil koordinasyon

`/arthurlegal:administrative-legal-idari-dava-prep` skill ile birlikte çalış — dava dilekçesi taslağı oradan; ÇED-spesifik argümanlar buradan.

**Compliance ekibi:** [Uyum Direktörü] + [Compliance Manager] çevre uyum bilgisi sahipdir — onlarla brief.

**İletişim Başkanlığı:** [İletişim Başkanlığı] — basın ve sosyal medya etkili olacaksa.

**İlgili iş birimi:** [İş Birimi Başkanı] — operasyonel etki bilgisi.

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
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (Danıştay 14./10. [N]); ArthurLegal MCP (`tr_`) (Çevre K. 2872 + ÇED Yön.)
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
[ArthurLegal MCP (`tr_`)]

## Sonraki adımlar

> 1. **Dış çevre avukatı brief** — `/arthurlegal:litigation-legal-outside-counsel-brief`
> 2. **CLCO eskalasyon** — yatırım blokesi büyük
> 3. **İletişim Başkanlığı koordinasyon** — basın hazırlığı
> 4. **Compliance brief** — [Uyum Direktörü]/[Compliance Manager] ile teknik koordinasyon
> 5. **Daha fazla bilgi** — [...]

**One question I'd ask:** [örn. "Aynı sektörde son 12 ayda Bakanlık ne kadar ÇED onayladı, ne kadar reddetti? Eğilim pozitif mi negatif mi?"]
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
