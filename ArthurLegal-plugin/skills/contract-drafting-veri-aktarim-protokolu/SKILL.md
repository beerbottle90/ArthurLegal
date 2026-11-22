---
name: contract-drafting-veri-aktarim-protokolu
description: >
  Ana sözleşmeye ek kişisel veri aktarım protokolünü sıfırdan kurar: tarafların sıfatları (veri
  sorumlusu, veri işleyen), veri kategorileri ve amaç, aktarım, saklama ve imha, ilgili kişi
  başvuruları, veri güvenliği ve ihlal bildirimi, denetim, sorumluluk; yurt dışı aktarımda KVKK m. 9
  yolu. Örneklerden yararlanır, birebir kopyalamaz.
user-invocable: true
---

# Veri Aktarım Protokolü Hazırlama (Sözleşme Eki)

> Sıfırdan taslak kurar. Kullanıcı şablon ya da emsal verirse ondan türetilir (`/arthurlegal:contract-drafting-belge-turet`). Her çıktı **TASLAK**: avukat okur ve onaylar, karşı tarafa avukat gönderir.
> Yapı ve ifade için `${CLAUDE_PLUGIN_ROOT}/references/redline-konvansiyonlari-rehberi.md` okunur: bölüm 5 (standart kloz seti), 7 (örneklerden yararlanma), 8 (iskelet), 9 (karar listesi), 10 (sık hatalar), 11 (yazım ve Word düzeni). Oradaki ifade örnektir; birebir aktarılmaz, işe göre yeniden kurulur. Öncelik: kullanıcının şablonu, sonra `firm-profile.md` ve büro playbook'u, sonra rehber.

## ADIM 0: Netleştirme

Eksik bilgiyi **seçenekli sorularla** sorun; bilinmeyen değer uydurulmaz, `[DOLDUR: ...]` bırakılır.

1. **Taraf:** veri sorumlusu mu, veri işleyen mi, ortak veri sorumluları mı? Rehberdeki örnekler alıcı ya da iş sahibi lehinedir; karşı tarafı temsil ediyorsanız pozisyonları ters kurun.
2. **Ana sözleşme:** hangi sözleşmeye ek, veri hangi iş için aktarılıyor?
3. **Veri:** kategoriler ve ilgili kişi grupları; özel nitelikli kişisel veri var mı?
4. **Yurt dışı:** aktarım var mı; varsa ülke ve yol (yeterlilik kararı, uygun güvence, arızi aktarım)?
5. **Dil:** Türkçe, İngilizce ya da iki dilli (iki sütunlu tablo).
6. **Müvekkil bilgisi:** taraf ve iş bilgisi müvekkile özgüyse önce ArthurMask ile maskeleyin; etiketleri (`{{KİŞİ-01}}`) koruyun.

## ADIM 1: İskelet

Kısa yapı: taraflar ve sıfatları, konu ve amaç, veri kategorileri, aktarım yolu, işleme talimatı, saklama ve imha, ilgili kişi başvuruları, veri güvenliği ve ihlal bildirimi, alt işleyen, denetim, sorumluluk, süre. Türe özgü maddeler (rehber bölüm 8 madde 3.h):

- **Saklama ve imha:** süre; sözleşme bitince iade, silme, yok etme ya da anonimleştirme ve bunun teyidi.
- **Veri güvenliği ve ihlal:** teknik ve idari tedbirler; veri işleyenin veri sorumlusuna bildirim süresi (rehber bölüm 5 madde 5), veri sorumlusunun ilgiliye ve Kurula bildirimi.
- **Yurt dışı aktarım:** yol açıkça yazılır; standart sözleşme kullanılıyorsa imzadan sonra Kuruma bildirim yükümlülüğü ve süresi (ADIM 3).
- **Alt işleyen ve denetim:** onay düzeni, denetim hakkı, maliyet.

## ADIM 2: Standart klozlar ve ticari kararlar

1. Rehber bölüm 5'teki on dokuz maddelik seti tek tek kontrol edin; bu işte uygulanmayanı `[KULLANILMADI]` diye işaretleyin, sessizce atlamayın.
2. Rehber bölüm 9'daki karar listesinden açık kalanları (bedel, ödeme, avans, teminat, ceza koşulu ve tavanı, garanti, fesih süreleri) kullanıcıya sorun ya da `[DOLDUR: ...]` bırakın. Rehberdeki oranlar örnektir, öneri değildir.
3. Karşı tarafın veri işleme sözleşmesi geldiyse önce `/arthurlegal:privacy-legal-dpa-review` ile inceleyin.

## ADIM 3: Madde doğrulama kapısı

Metne yazılacak her kanun maddesini `tr_mevzuat_madde_getir` ile çekin, `citation` alanını birebir kullanın ve maddeye yüklediğiniz içeriği (hakkın sahibi, şart, süre, sonuç) başlık ve metinle eşleştirin. Bu türde sık geçenler (22.11.2026'da resmî metinden okundu; yine çekin):

- KVKK m. 7 (işlenmesini gerektiren sebepler ortadan kalkınca kişisel veri silinir, yok edilir ya da anonim hâle getirilir)
- KVKK m. 9 (yurt dışına aktarım: yeterlilik kararı, yoksa uygun güvenceler, o da yoksa arızi hâller; m. 9/5: standart sözleşme imzadan itibaren beş iş günü içinde Kuruma bildirilir)
- KVKK m. 12 (veri güvenliği; başkası adına işlemede veri sorumlusu tedbirlerden o kişiyle müştereken sorumludur; ihlal en kısa sürede ilgiliye ve Kurula bildirilir)

Çekilemeyen madde yazılmaz: `UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/`.

## ADIM 4: Son kontrol

Rehber bölüm 10'daki sık hataları tarayın; bölüm 11'e göre yazım ve Word düzenini uygulayın (tanımlı terimler, numaralandırma, imza bloğu, ek listesi, dosya adı). Taslak notları Word yorumu olarak yazılır (yazar ArthurLegal, baş harfler AL).

## Çıktı

```markdown
TASLAK: AVUKAT ONAYI ALINMADAN KARŞI TARAFA GÖNDERİLMEZ

# Veri Aktarım Protokolü (Sözleşme Eki): [taraflar]

## İnceleyen notu
- Temsil edilen taraf: … · Dil: …
- Açık ticari kararlar: [DOLDUR] listesi
- Madde kontrolü: her atıf resmî metinden okundu ve içerikle eşleşti / çekilemedi (UYARI satırı)

## Taslak metin
[rehber bölüm 8 sırasıyla, bölüm 11 düzeninde]

## Sonraki adımlar
- Ana sözleşmenin KVKK maddesini bu protokole bağlayın (rehber bölüm 5 madde 5).
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
