# legal-research — OSS Kaynak Dalgası Ek Skill'leri (v1.5.0 adayı)

> Bu dosya, 13.08.2026 OSS kaynak dalgasının Claude paketi (Corporate / Law
> Firm) tarafındaki **skill kitabı ekidir**. v1.5.0 derlemesinde mevcut
> `legal-research` skill kitabına eklenmek üzere adaydır. Bilgi tabanı
> karşılıkları `knowledge/references/` altındaki yeni rehberi dosyalarıdır.

---

## Skill: ABD atıf doğrulama (uydurma atıf savunması)

**Ne zaman:** Taslak cevap, memo veya inceleme herhangi bir biçimde ABD atıfı
içeriyorsa (tam: `Bush v. Gore, 531 U.S. 98 (2000)`; kısa: `531 U.S., at 99`;
`Id.` / `supra`; kanun: `15 U.S.C. § 1`). Kullanıcı "bu atıflar gerçek mi?"
diye sorduğunda da.

**Araçlar:** Entegre CourtListener MCP — `extract_citations` (yerel eyecite
geçişi; yalnız çıkarım) ve `analyze_citations` (veritabanına karşı doğrulama).

**Yöntem:**
1. Taslaktaki tüm atıfları çıkar (`extract_citations`, `resolve: true` —
   `Id.`/`supra` zinciri öncülüne otomatik çözülür).
2. Her benzersiz atıfı doğrula (`analyze_citations`). Durum yorumu:
   200 bulundu → otorite olarak kullanılabilir, `absolute_url` ile atıfla;
   404 → otorite olarak GÖSTERME, "doğrulayamadım" beyanı zorunlu;
   400 → muhtemel halüsinasyon, atıfı çıkar ve bildir;
   300 → yıl/mahkeme ile teke indir, indirgenemiyorsa belirt;
   429 → bekle ve yeniden dene, doğrulamayı atlama.
3. Reporter/mahkeme adlarını kanonik biçime çevir (reporters-db / courts-db
   konvansiyonu) — aynı karar iki yazımla iki kayıt üretemez.
4. Atıf kalıbı: `[CourtListener — {dava}, {atıf} — çekim: GG.AA.YYYY]`.

**Sert kurallar:** Doğrulama sonucu bir SONUÇTUR: "doğrulanamadı" ile "yok"
farklı iddialardır, hangisi kanıtlandıysa onu söyle. Bellekten atıf dizesi
kurma; yalnız doğrulama geçişinden dönen atıflar sunulur. CourtListener'a
erişilemiyorsa ABD atıfları `[model bilgisi — doğrulayın]` etiketi taşır.

**Bilgi tabanı:** `references/abd-atif-dogrulama-rehberi.md`

---

## Skill: Karşı-taraf kimlik çözümleme ve tarama (GLEIF → OpenSanctions)

**Ne zaman:** Yeni karşı-taraf KYC dosyası; imza öncesi kontrol; grup yapısı
soruları ("kimin iştiraki?", "nihai ana ortak kim?"); her OpenSanctions
taramasının ön adımı olarak.

**Sıra sabittir: önce kimlik, sonra listeler.** Serbest metin unvanla yaptırım
taraması hem yanlış pozitif (aynı adlı şirketler) hem yanlış negatif
(transliterasyon kayması — AZ/RU/CN adlarında belirgin) üretir.

**Araçlar:** GLEIF REST API (`api.gleif.org`, auth'suz, CC0 — WebFetch) +
entegre OpenSanctions.

**Yöntem:**
1. Kimlik çözümle: `GET /api/v1/autocompletions?field=fulltext&q={unvan}` →
   yargı çevresi/adres eşleşen adayı seç → `GET /api/v1/lei-records/{lei}` ile
   `registration.status` kontrol et (LAPSED kayıtta veri bayat olabilir).
2. Grubu haritala: `/ultimate-parent` ve `/direct-parent`. Hem sözleşme
   tarafını hem nihai ana ortağı ayrı ayrı tara.
3. Tara: doğrulanmış unvan + yargı çevresi + sicil no ile OpenSanctions.
4. Raporla: `[GLEIF — LEI {lei} — çekim: GG.AA.YYYY]` +
   `[OpenSanctions — {taraf} — çekim: GG.AA.YYYY]`.

**Sert sınırlar (her raporda beyan edilir):** GLEIF Level 2 = muhasebe
konsolidasyonu ana ortaklığı, gerçek kişi UBO DEĞİL — MASAK/AML gerçek
faydalanıcı tespiti yerel sicil/beyan ister. LEI yokluğu ≠ şirket yokluğu
(kapsam düzenlenmiş işlemlere eğik; TR ≈ 10,9 bin kayıt). İlişki kaydının
yokluğu bağımsızlık kanıtı değildir. Yaptırım çıktısı, aleyhe işlemden önce
insan uyum incelemesinden geçer.

**Bilgi tabanı:** `references/gleif-rehberi.md`, `references/opensanctions-rehberi.md`

---

*Son güncelleme: 13.08.2026. Bu iki skill'in Copilot ikizi karşılıkları:*
`skills/us-citation-verification/` *ve* `skills/counterparty-identity-screening/`
*(copilot-socar-lc-digital-twin).*
