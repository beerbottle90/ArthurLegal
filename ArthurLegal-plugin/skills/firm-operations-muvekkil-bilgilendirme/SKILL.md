---
name: firm-operations-muvekkil-bilgilendirme
description: >
  Müvekkile dosyanın durumunu sade dille anlatan bilgilendirme yazısı: ne oldu, ne anlama geliyor,
  sırada ne var, sizden hangi karar ya da belge bekleniyor. Avukatın onayından geçmeden gönderilmez;
  müvekkil adları ArthurMask etiketleriyle korunur, belge Word olarak avukata teslim edilir. Portal ya
  da müvekkile doğrudan açılan bir yüzey değildir.
user-invocable: true
---

# Müvekkil Bilgilendirme Yazısı

## Tetikleyici

Duruşma, tebligat, karar, bilirkişi raporu ya da karşı tarafın yeni bir adımı sonrası avukat müvekkile durumu
anlatmak istediğinde; ya da müvekkil "dosyam ne durumda?" diye sorduğunda.

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 14.11.2026)

- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 36: avukat, görevi dolayısıyla öğrendiklerini açığa vuramaz.
  Yazı yalnız müvekkile gider; üçüncü kişiye, gruba ya da paylaşılan bir sayfaya konmaz.
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 55: iş elde etmek için reklam sayılabilecek teşebbüs yasaktır.
  Yazı mevcut müvekkile dosyası hakkında bilgi verir; başka hizmetlerin tanıtımını, başarı vaadini ya da kampanya dilini içermez.

## ADIM 0 — Girdi

1. **Dosya:** ArthurMask'li belge ya da avukatın özeti. Gerçek ad ve dosya numarası yazılmaz; etiketler (`{{KİŞİ-01}}`,
   `{{DOSYA_NO-01}}`) korunur, teslimde yerelde çözülür.
2. **Son gelişme:** ne oldu, hangi tarihte (tebliğ, duruşma, karar, rapor).
3. **Sırada ne var:** sonraki adım ve tarihi. Süre hesabı yapılmaz: avukatın girdiği son gün yazılır; avukat vermediyse
   `[avukat dolduracak]` bırakılır.
4. **Müvekkilden beklenen:** karar, belge, ödeme ya da bilgi. Yoksa "sizden bir şey beklenmiyor" yazılır.

Eksik varsa **seçenekli sorun** (ör. "Müvekkilden karar mı bekleniyor, yalnız bilgi mi veriyoruz?").

## ADIM 1 — Üslup

- Hukukçu olmayan okura yazın: terim kullanmanız gerekiyorsa aynı cümlede açıklayın ("istinaf, yani bir üst mahkemeye başvuru").
- Kısa paragraflar, en çok bir sayfa. İlk cümle sonucu söyler.
- Sınırları yazın: kesin olmayanı kesin gibi anlatmayın; sonuç vaadi yok.
- Tutarları (harç, masraf, talep edilen bedel) ayrı bir satırda, kaynağıyla verin; hesap gerekiyorsa hesap kartlarından ve
  tazelik satırıyla.
- Kanun maddesi gerekiyorsa `tr_mevzuat_madde_getir` ile çekin; müvekkile madde numarası yerine ne anlama geldiğini yazın.

## ADIM 2 — Çıktı

```markdown
TASLAK — AVUKAT ONAYI ALINMADAN GÖNDERİLMEZ

Sayın {{KİŞİ-01}},

[Bir cümlelik sonuç: dosyanızda ne oldu.]

**Ne oldu:** [tarih — gelişme, sade dille]
**Ne anlama geliyor:** [iki üç cümle; kesin olmayan kısım açıkça belirtilir]
**Sırada ne var:** [adım — tarih ya da [avukat dolduracak]]

**Sizden beklenen:** [karar / belge / bilgi — son tarihiyle] · ya da: Şu an sizden bir şey beklenmiyor.

[Tutar varsa ayrı satır: kalem — tutar — kaynak]

Sorularınız için bana ulaşabilirsiniz.
[Avukat adı]
```

Teslim: `arthur_mask_teslim` ile Word olarak avukatın bilgisayarına; etiketler orada çözülür. Gönderimi avukat yapar.

## Hatalar

- Avukat onayı olmadan müvekkile göndermek ya da göndermeyi önermek
- Süre ya da son günü kendiniz hesaplayıp yazmak
- Başarı vaadi, "kesin kazanırız" gibi ifade, başka hizmetin tanıtımı
- Gerçek ad ya da dosya numarasını etiket yerine yazmak

---

## Kaynak katmanı — /legal-research

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
> **Meslek sirri (Av. K. m. 36):** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| yabanci karsi tarafli veya AZ baglantili yeni is alimi — mevzuat kapsaminin gercekten var olup olmadigini once dogrula | `/arthurlegal:legal-research-kaynak-secimi` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
