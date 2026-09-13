# Değişiklik Günlüğü

[Keep a Changelog](https://keepachangelog.com/tr-TR/1.1.0/) formatına uygundur.
Semver: [Semantic Versioning 2.0](https://semver.org/lang/tr/).

---

## [1.0.2] — 2026-09-13 — *Arthur Mask: dosya belgeleri bilgisayardan çıkmadan maskelenir*

> Dava, soruşturma ve kovuşturma dosyalarındaki belgeler Claude'a verilmeden önce kullanıcının kendi Windows bilgisayarında maskelenebilir. Yerel program **Arthur Mask 1.0.0**, ArthurLegal GitHub v1.8.0 sürümüne kurulum dosyası olarak eklendi (`ArthurMask-Kurulum-1.0.0.exe`). Yalnız **Claude Desktop (Windows)** ile çalışır; claude.ai web ve mobilde çalışmaz. Önceki sürümlerde "sonraki hatta gelecek" denen veri maskeleme katmanı budur.

### Eklendi

- **`SYSTEM_PROMPT.md` — Arthur Mask bölümü:** `arthur_mask_*` araçlarının kullanımı (belge `arthur_mask_belge_getir` ile çekilir, etiketler harfi harfine korunur, gerçek değer tahmin edilmez, etiket araştırma sorgusuna konmaz, revizyon `arthur_mask_belgeyi_revize_et`, yeni belge `arthur_mask_teslim` ile UDF/Word). Sohbete soruşturma veya kovuşturma dosyasından tanımlanabilir kişisel veri yapıştırılırsa sohbet başına en çok bir kez, işi durdurmayan kısa hatırlatma.
- **`knowledge/references/arthur-mask-rehberi.md`** (referans 23 → 24): kurulum, günlük akış, kırmızı hat, çıkış kapısı ve sızıntı denetimi, kurtarma anahtarı, sorun giderme, sınırlar, araç kuralları.
- **`ARTHUR-MASK.md`:** hâkim ve kalem personeline yönelik adım adım rehber ve SSS (gizlilik veya kısıtlama kararı olan dosyalar dâhil).
- **`KURULUM.md`:** Arthur Mask adımı, SSS ve güncelleme notları.
- **`ATTRIBUTION.md`:** Arthur Mask kurulum dosyasındaki üçüncü taraf açık kaynak bileşenler.

### Değişti

- Sistem talimatının sürüm başlığı 1.0.2'ye çekildi (önceki paket başlıkta hâlâ 1.0.0 yazıyordu); "maskeleme katmanı sonraki hatta" notları kaldırıldı.
- `VERSION.md` lisans satırı paketin gerçek lisansıyla (Proprietary, Non-Commercial) eşitlendi.

### Sınırlar

- Takma adlandırma anonim hâle getirme değildir; tespit olasılığa dayalıdır. Tarihler ve tutarlar bilinçli olarak maskelenmez; resim, el yazısı, imza, kaşe ve QR kod kapsam dışıdır.
- Maskeleme; KVKK yükümlülüklerinin, soruşturma ve kovuşturma dosyalarına ilişkin gizlilik kurallarının, gizlilik veya kısıtlama kararlarının ve kurumun bilgi güvenliği kurallarının yerine geçmez.

### Yükleme

`SYSTEM_PROMPT.md` yeniden yapıştırılır; `arthur-mask-rehberi.md` Project knowledge'a eklenir. Arthur Mask için `KURULUM.md`; Project Claude Desktop'tan açılır.

---

## [1.0.1] — 2026-09-06 — *Türk hukuku ArthurLegal MCP'ye (`tr_`) taşındı*

> Yargı ve mevzuat araçları artık `arthurlegal-mcp.fly.dev/mcp` üzerinden `tr_` önekiyle gelir (auth yok). `yargi-mcp-rehberi.md` ve `mevzuat-mcp-rehberi.md` baştan yazıldı; tüm referanslardaki çağrı örnekleri ve atıf etiketleri (`[ArthurLegal TR — …]`) yeni araçlara çevrildi. KİK, Sayıştay ve AİHM bu connector'da yoktur; isteğe bağlı TR Legal MCP ile kullanılır. Kurulum ve README güncellendi.

---

## [1.0.0] — 2026-06-28 — *ArthurLegal Courthouse — İlk Sürüm (Yargı Mensubu Asistanı)*

> **8/8 plugin kurulu** (her biri 2-5 skill — toplam 28 skill) ve **22 referansın tamamı yargısal/tarafsız çerçevededir** (müşteri-spesifik içerik temizlendi).

### Konum (diğer ArthurLegal paketlerinden farkı)

ArthurLegal Corporate / Law-Firm paketleri **taraf vekili / in-house** (savunucu) perspektifindedir. **Courthouse bunu ters çevirir:** hedef kitle **mahkeme hâkimleri + mahkeme kalem memurluklarıdır**; perspektif **yargısal ve tarafsızdır**.

- **Tarafsızlık + bağımsızlık** (AY m. 138 — kanun + vicdan); "kazanan taraf" yok, iki taraf dengeli analiz edilir.
- **Sıfır-halüsinasyon atıf:** Karara girecek bir dayanak uydurulamaz; her atıf TR Legal MCP'den **verbatim**. Advocacy kullanımından daha katı.
- **"Taslak — hâkim / heyet onayı şart":** Asistan asla karar vermez; gerekçe ve usulü **yapılandırır** (decision-support).

### Eklendi

**Mimari — 4 dal × 2 rol = 8 plugin matrisi (TR adlandırma):**

| Dal | Hâkim | Kalem |
|---|---|---|
| Hukuk (HMK) | `hukuk-hakim` ✅ | `hukuk-kalem` ✅ |
| Ceza (CMK) | `ceza-hakim` ✅ | `ceza-kalem` ✅ |
| İdari (İYUK) | `idari-hakim` ✅ | `idari-kalem` ✅ |
| Vergi (VUK+İYUK) | `vergi-hakim` ✅ | `vergi-kalem` ✅ |

**Spine:**
- `SYSTEM_PROMPT.md` — yargısal/tarafsız reframe + 8-plugin haritası + sıfır-halüsinasyon atıf disiplini + hâkimlik etiği sınırları.
- `knowledge/mahkeme-profili.md` — mahkeme profil şablonu ([DOLDUR]).

**Skill kitapçıkları (8 plugin · 28 skill):**
- `hukuk-hakim` (gerekceli-karar · on-inceleme · delil-degerlendirme · **ihtiyati-tedbir**) — kalıp/şablon
- `hukuk-kalem` (tensip-zapti · tebligat · harc-hesabi)
- `ceza-hakim` (hukum-taslagi · iddianame-degerlendirme · tutuklama-degerlendirme · **hagb-degerlendirme** · **uzlastirma-denetimi**)
- `ceza-kalem` (muzekkere · ceza-tebligat · infaz-evraki)
- `idari-hakim` (idari-karar · yurutmenin-durdurulmasi · ehliyet-husumet · **ivedi-yargilama**)
- `idari-kalem` (dosya-tekemmul · idari-tebligat · **karar-uygulama-takip**)
- `vergi-hakim` (vergi-karar · tarhiyat-degerlendirme · **odeme-emri-itiraz**)
- `vergi-kalem` (vergi-tebligat · vergi-sure-takip · **karar-uygulama-iade**)

**Yeni mahkeme-tarafı referanslar (7):**
`gerekce-yazim-rehberi`, `hakimlik-etigi-rehberi`, `tebligat-7201-rehberi`, `harc-gider-rehberi`, `sulh-ceza-hakimligi-rehberi`, `yurutmenin-durdurulmasi-rehberi`, `vergi-yargisi-rehberi`.

**Ek referans:** `connector-saglik-fallback-rehberi` — dış API/WebFetch jurisdiction connector'larının canlı sağlık durumu + çalışan fallback'leri (2026-06-28 testi). OpenSanctions key gömülü.

**Paylaşılan referanslar (Law-Firm iskeletinden devralındı, 15 dosya):**
`kanun-kisaltmalar`, `mevzuat-mcp-rehberi`, `yargi-mcp-rehberi`, `hmk-rehberi`, `cmk-rehberi`, `iyuk-rehberi`, `idari-yargi-yapisi-rehberi`, `vuk-rehberi`, `gib-ozelge-rehberi`, `otv-rehberi`, `damga-vergisi-rehberi`, `uyap-rehberi`, `bilirkisilik-rehberi`, `kep-etebligat-rehberi`, `ced-rehberi`.

### Yargısal reframe (tamamlandı)

Devralınan 15 paylaşılan referans yargısal/tarafsız çerçeveye uyarlandı; taraf-vekili dili ve **müşteri-spesifik içerik** tamamen temizlendi:
- **Tam yeniden yazım (mahkeme bakışı):** `uyap-rehberi`, `bilirkisilik-rehberi`, `kep-etebligat-rehberi`.
- **Bölüm reframe + müşteri içeriği temizliği:** `hmk`, `idari-yargi-yapisi`, `yargi-mcp`, `kanun-kisaltmalar`, `damga-vergisi`, `otv`, `ced`, `gib-ozelge`, `cmk`.
- Kırık iç linkler (var olmayan dosyalara) düzeltildi.

### Yapılacaklar (sonraki iterasyonlar)

- [ ] Skill derinleştirme (devam): kanun yolu inceleme (istinaf/temyiz), ceza infaz hesabı, hukuk islah, idari tam yargı tazminat hesabı.
- [ ] Karşılaştırmalı hukuk referansları (CourtListener/OpenCaseLaw.ch) gerektiğinde.
- [ ] (v1.4.0 hattı) Veri maskeleme katmanı — dosyalardaki yoğun kişisel/özel nitelikli veri için.

### Atıf

- **Author:** Claude (Anthropic, Opus 4.8 — `claude-opus-4-8`)
- **Designer:** Ertuğ Demir
- **Knowledge base:** Anthropic [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)
