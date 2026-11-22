# contract-drafting-tasima-sozlesmesi

Karayolu yük taşıma sözleşmesini sıfırdan kurar: sözleşme belgeleri ve öncelik, taşıma talebi ve araç tahsisi, yükleme ve teslim süreleri, taşıyıcının personel ve araç yükümlülükleri, kayıt ve raporlar, sağlık, emniyet ve çevre, teminat, ceza koşulu tablosu, taşıyıcının bağımsızlığı. Taşıyıcının sorumluluğu ve sınırları TTK'dan çekilerek yazılır; örneklerden yararlanır, birebir kopyalamaz.

# Karayolu Taşıma Sözleşmesi Hazırlama

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (``contract-drafting-belge-turet` iş akışı (`arthurlegal-sozlesme` becerisi, `../arthurlegal-sozlesme/references/contract-drafting-belge-turet.md`)`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `../arthurlegal/references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `firm-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** gönderen (yük sahibi) mi, taşıyıcı mı? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Kapsam:** yurt içi mi, uluslararası mı? Uluslararası karayolu taşımasında uluslararası sözleşmeler (CMR) uygulanabilir; avukata işaretleyin.
3. **Yük:** tehlikeli madde ya da özel koşul (soğuk zincir, ağır yük) var mı?
4. **Yapı:** tek sefer mi, çerçeve sözleşme ve taşıma talepleri mi?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Rehber bölüm 8 madde 1'deki uzun form sırası. Türe özgü maddeler (rehber bölüm 8 madde 3.d):

- **Belgeler ve öncelik:** sözleşme, ekler ve taşıma talepleri arasındaki öncelik.
- **Taşıma talebi ve araç tahsisi:** talep yolu, tahsis süresi, araç uygun değilse sonuç.
- **Süreler:** yükleme ve teslim süreleri, gecikmenin ölçülmesi.
- **Taşıyıcının yükümlülükleri:** personel, araç ve belgeler, kayıt ve raporlar, sağlık, emniyet ve çevre kuralları.
- **Sorumluluk:** taşıyıcının zıya, hasar ve gecikmeden sorumluluğu ve kanuni sınırları (ADIM 3). Sınırı değiştiren, kaldıran ya da değer beyanına bağlayan hüküm yazılacaksa bunun mümkün olup olmadığı TTK'nın taşıma hükümleri çekilerek kontrol edilir.
- **Teminat ve ceza koşulu tablosu; taşıyıcının bağımsızlığı** (personeli üzerinde yönetim ve sorumluluk taşıyıcıdadır).

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- TTK m. 850 (taşıyıcı eşyayı varma yerine götürüp gönderilene teslim etmeyi borçlanır; taşıma işleri ticari işletme faaliyetidir)
- TTK m. 875 (taşıyıcı eşyanın teslim alınmasından teslimine kadar zıya, hasar ve teslimdeki gecikmeden doğan zarardan sorumludur)
- TTK m. 882 (sorumluluk sınırları: zıya ya da hasarda gönderinin net olmayan ağırlığının kilogramı başına 8,33 Özel Çekme Hakkı; taşıma süresinin aşılmasında taşıma ücretinin üç katı)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Karayolu Taşıma Sözleşmesi: [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Yük sigortası ve rücu için sigorta poliçesinin koşullarını ayrıca isteyin.
- Karşı taraf taslağı döndürünce ``contract-drafting-versiyon-karsilastir` iş akışı (`arthurlegal-sozlesme` becerisi, `../arthurlegal-sozlesme/references/contract-drafting-versiyon-karsilastir.md`)`; düzeltmeleri belgeye işlemek için ``contract-drafting-redline-contract` iş akışı (`arthurlegal-sozlesme` becerisi, `../arthurlegal-sozlesme/references/contract-drafting-redline-contract.md`)`.
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
| redline ve fallback pozisyonlari icin imzali emsal kloz metni | ``legal-research-sozlesme-emsali` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-sozlesme-emsali.md`)` |
| AZ hukuku secilmisse emredici hukum kontrolu: akt + statu | ``legal-research-az-mevzuat` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-az-mevzuat.md`)` |
| TR kanun maddesi (kloz govdesindeki atiflar dahil): okuma + baslik ve icerik eslestirme | ArthurLegal MCP `tr_mevzuat_madde_getir` · `../arthurlegal/references/mevzuat-mcp-rehberi.md` bolum 9 |

Rehberler: `../arthurlegal/references/eqanun-mcp-rehberi.md` · `../arthurlegal/references/lex-scholar-rehberi.md` · `../arthurlegal/references/resourcecontracts-rehberi.md` · `../arthurlegal/references/karsilastirmali-hukuk-rehberi.md` · `../arthurlegal/references/nl-rechtspraak-mcp-rehberi.md` · `../arthurlegal/references/pl-sejm-mcp-rehberi.md` · `../arthurlegal/references/at-ris-mcp-rehberi.md` · `../arthurlegal/references/ie-statutebook-mcp-rehberi.md` · `../arthurlegal/references/fi-finlex-mcp-rehberi.md` · `../arthurlegal/references/es-boe-mcp-rehberi.md`
