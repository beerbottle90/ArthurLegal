---
name: contract-drafting-satinalma-sartnamesi
description: >
  Sipariş emriyle kurulan kısa form satınalma şartnamesini ya da sipariş genel koşullarını (mal ya da
  hizmet) sıfırdan kurar: fiyat ve ödeme, teslimat ya da hizmetin tamamlanması, muayene ve testler,
  garanti, askıya alma, fesih, tazmin, mülkiyet ve riskin geçişi, sigorta, şartname ile sipariş
  emri arasındaki öncelik. Genel işlem koşulu kurallarına göre kurulur; örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Satınalma Şartnamesi ve Sipariş Genel Koşulları Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/arthurlegal:contract-drafting-belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `${CLAUDE_PLUGIN_ROOT}/references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `firm-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** alıcı (şartnameyi koyan) mı, tedarikçi mi? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Kapsam:** mal mı, hizmet mi, ikisi mi?
3. **Tedarikçi:** yerli mi, yabancı mı? Yabancıysa `/arthurlegal:contract-drafting-ingilizce-genel-kosullar`.
4. **Kabul yolu:** sipariş emrinde açık atıf, imza ya da elektronik onay?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 2'deki kısa form sırası. Türe özgü maddeler (rehber bölüm 8 madde 3.a ve b):

- **Öncelik:** şartname ile sipariş emri arasındaki öncelik yazılır.
- **Hizmet içeriyorsa:** bağımsız işveren ve iş sağlığı ve güvenliği maddeleri eklenir.
- **Genel işlem koşulu:** şartname tek taraflı ve çok sayıda tedarikçi için hazırlandığından genel işlem koşuludur. Karşı tarafa varlığı açıkça bildirilmeli, içeriğini öğrenme imkânı verilmeli ve kabul ettirilmelidir (sipariş emrinde açık atıf, şartnamenin eklenmesi ya da erişim bağlantısı); alıcıya tek yanlı değiştirme yetkisi veren kayıt yazılmaz.
- **Genel hükümler:** rehber bölüm 5'teki setin kısa hâlleri.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- TBK m. 20 (genel işlem koşulunun tanımı)
- TBK m. 21 (karşı tarafa açıkça bilgi verilip içeriğini öğrenme imkânı sağlanmadıkça ve kabul edilmedikçe aleyhe koşul yazılmamış sayılır)
- TBK m. 24 (düzenleyene tek yanlı değiştirme yetkisi veren kayıt yazılmamış sayılır)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Satınalma Şartnamesi ve Sipariş Genel Koşulları: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Uzun form gerekiyorsa `/arthurlegal:contract-drafting-mal-alim-sozlesmesi` ya da `/arthurlegal:contract-drafting-hizmet-sozlesmesi`.
- Karşı taraf taslağı döndürünce `/arthurlegal:contract-drafting-versiyon-karsilastir`; düzeltmeleri belgeye işlemek için `/arthurlegal:contract-drafting-redline-contract`.
```

---

## Kaynak katmanı: /legal-research

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur;
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar; gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | `/arthurlegal:legal-research-sozlesme-emsali` |
| AZ hukuku secilmisse emredici hukum kontrolu: akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil): okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `${CLAUDE_PLUGIN_ROOT}/references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
