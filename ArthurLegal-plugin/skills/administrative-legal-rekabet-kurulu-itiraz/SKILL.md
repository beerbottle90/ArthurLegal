---
name: administrative-legal-rekabet-kurulu-itiraz
description: >
  Rekabet Kurulu kararına karşı iptal davası hazırlık — 4054 sayılı Rekabetin
  Korunması Hakkında Kanun. İlk derece Ankara İdare Mahkemesi → BİM → Danıştay 13.
  Daire. [Müvekkil] vertical entegrasyon (rafineri + petrokimya + terminal + dağıtım)
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
İYUK m. 7 → 60 gün (4054 m. 55'te özel süre yok) →
Ankara İdare Mahkemesi (ilk derece) →
Ankara BİM (istinaf) →
Danıştay 13. Daire (temyiz)
```

⚠️ **Rekabet Kurulu kararı doğrudan Danıştay'a gitmez** (artık eski uygulama değişti). 4054 m. 55 referansı yanlış uygulanmamalı.

## sektöre-özel risk

[Müvekkil] vertical entegrasyon profili Rekabet dikkatinde:
- **[büyük enerji tesisi] (üst kademe)** + **[HALKA AÇIK İŞTİRAK] (orta kademe petrokimya)** + **[Müvekkil terminali] (lojistik)** + **[Müvekkil] Enerji Ticaret (dağıtım)** = baştan sona zincir kontrolü
- **[ÖZEL ENDÜSTRİ BÖLGESİ]** içinde dikey entegre yapı
- **EPC tedarik zinciri** (yan kuruluşlardan tedarik)
- **Doğal gaz dağıtım** ([DAĞITIM İŞTİRAKİ] pazar payı)

Rekabet Kurulu **olası ihlal alanları:**
- Dikey integrasyon → bağımsız oyuncular için pazar erişim engeli
- Bağlı tedarikçi imtiyazları → ayrımcılık
- Fiyat parlatma → predatory pricing
- Pazar paylaşımı (intra-group [Ana ortak / ilişkili taraf] ile)

## Hukuki argümanlar

- **Yetkisizlik:** Rekabet Kurulu bu konuda yetkili mi (sektör düzenleyici EPDK paralel)?
- **Pazar tanımı yanlış:** Kurulun belirlediği ilgili ürün/coğrafi pazar dar mı?
- **Hâkim durum yok:** Pazar payı %X'in altında, hâkim sayılmayız
- **Etki yok:** Eylemimiz rekabeti gerçekten kısıtladı mı?
- **Mücbir sebep / makul gerekçe:** Eylem ticari mantıkla açıklanabilir
- **Ceza orantısız:** Cironun %X'i — kanunda öngörülen aralığın üstünde

## ArthurLegal MCP (`tr_`)

```
tr_kurum_karari_ara(
  kurum="rekabet",
  query="<konu>"
)

tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="D13",
  query="+Rekabet +Kurulu +karar +iptal",
  date_from="2022-01-01"
)
```

Rekabet Kurulu kararları **bağlayıcı emsal** değil ama Kurulun tutarlılığı için referans. Danıştay 13. Daire kararları temyiz için.

## müvekkil koordinasyon

- **CLCO ([CLCO ADI])** + dış rekabet avukatı 24h
- **CEO ([CEO ADI])** — büyük tutar / stratejik için
- **İletişim ([İletişim Başkanlığı])** — basın etkili olabilir
- **halka açık iştirak ilgili ise** → KAP açıklama
- **Compliance ([Uyum Direktörü])** — rekabet uyumu kapsamı

## Çıktı

`/arthurlegal:administrative-legal-idari-dava-prep` skill'i ile kombine — bu skill rekabet-özel argümanları ekler.

```markdown
[ÜST BAŞLIK]

# Rekabet Kurulu Kararı İtiraz — [Karar no]

## ⚠️ İnceleyen notu
- **Kararın özeti:** [tip + tutar + koşullar]
- **Süre kalan:** [N gün]
- **Vertical entegrasyon ilişkisi:** [evet/hayır]
- **Pazar tanımı doğru mu:** [değerlendirme]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) (Rekabet Kurulu [N], Danıştay 13. [N])
- **CEO bilgisi:** [✓/✗]
- **KAP açıklama:** [N/A / hazırlanıyor]
- **Reviewer bekleyen:** N adet

[Kararın analizi + hukuki argümanlar + emsal + dava dilekçesi taslağı]

## Sonraki adımlar

> 1. **Dış rekabet avukatı brief** — `/arthurlegal:litigation-legal-outside-counsel-brief`
> 2. **CEO + CLCO eskalasyon**
> 3. **Compliance + iş birimi koordinasyon** — yapısal etki değerlendirmesi
> 4. **KAP açıklama** ([HALKA AÇIK İŞTİRAK] büyük etki)
> 5. **Avrupa Komisyonu paralel** (eğer AB Rekabet bağlantısı varsa — Madde 102 TFEU)
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
