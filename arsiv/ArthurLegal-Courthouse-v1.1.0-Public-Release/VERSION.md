# Sürüm Bilgisi

**Sürüm:** 1.1.0
**Yayın tarihi:** 2026-09-23
**Önceki sürüm:** 1.0.5
**Lisans:** Proprietary, Non-Commercial (bkz. [LICENSE](LICENSE)); `claude-for-legal` bileşenleri Apache 2.0

## Semver özeti

- **Major (1.x.x):** Geriye uyumsuz mimari değişiklik
- **Minor (x.1.x):** Geriye uyumlu yeni plugin / dal / rol / referans ekleme
- **Patch (x.x.1):** Hata düzeltme, içerik güncelleme

## Bu sürümde

**v1.1.0 — Tapu-kadastro.** ArthurLegal MCP'nin `tkgm_` araçları kaynak listesinde: parsel TKGM Parsel Sorgu'dan canlı gelir (bilgi amaçlı; bilirkişi raporu ve kadastro kaydı yerine geçmez). `tapu-kadastro-rehberi.md` eklendi. GİB özelge aramasındaki `phrase` süzgeci yoktu (arama metni gitmiyordu), `query` oldu. Türkiye 0.5.0.

**v1.0.5 — Madde doğrulama kapısı.** Gerekçe, tensip zaptı ve usul belgelerinin gövdesindeki her madde numarası da atıftır: bu sohbette çekilmiş olmalı ve maddeye yüklenen içerik başlık ve metinle örtüşmeli. HMK m. 269 ile 278 bilirkişi haritası ve diğer yanlış madde atıfları resmî metne göre düzeltildi (CHANGELOG).

**v1.0.4 — İçtihat tarih süzgeci ve araştırma rehberleri.** Bedesten tek taraflı tarih aralığını sessizce yok sayıyordu; yalnız `date_from` ile yapılan içtihat araması süzgeçsiz dönüyordu. Türkiye backend'i 0.4.0 bunu düzeltti; `yargi-mcp-rehberi.md` ve `mevzuat-mcp-rehberi.md` yenilendi (tarih kontrolü, yerel arşivin kurum bazında gerçek kapsamı, `konu` ön elemesi ve ölçülmüş sınırları). Talimat metni yalnız sürüm etiketinde değişti.

**v1.0.3 — Süre düzeltmeleri.** CMK itiraz, KYOK'a itiraz, istinaf ve temyiz süreleri 7499 s.K.'ya göre iki hafta; istinaf ve temyizde başlangıç gerekçeli hükmün tebliği. 6183 m. 58 ödeme emrine itiraz 15 gün. Talimat metni değişmedi.

**v1.0.2 — Arthur Mask.** Dosya belgeleri Claude'a verilmeden önce kullanıcının Windows bilgisayarında maskelenebilir (yalnız Claude Desktop). Sistem talimatına Arthur Mask bölümü, `arthur-mask-rehberi.md` referansı, `ARTHUR-MASK.md` kullanım rehberi eklendi.

> **8/8 plugin kurulu** (her biri 2-5 skill — toplam 28 skill + 25 referans). Referansların tamamı yargısal/tarafsız çerçevededir.

v1.0.0 — **ArthurLegal Courthouse** ilk sürüm. Türk **yargı mensubu** (mahkeme hâkimleri + mahkeme kalem memurlukları) için **yargısal / tarafsız** decision-support asistanı. Diğer ArthurLegal paketlerinden farkı: savunuculuk değil, **tarafsızlık + sıfır-halüsinasyon atıf** disiplini.

**Mimari:** 4 dal × 2 rol = **8 plugin** matrisi.

| Dal | Hâkim | Kalem |
|---|---|---|
| Hukuk (HMK) | `hukuk-hakim` | `hukuk-kalem` |
| Ceza (CMK) | `ceza-hakim` | `ceza-kalem` |
| İdari (İYUK) | `idari-hakim` | `idari-kalem` |
| Vergi (VUK+İYUK) | `vergi-hakim` | `vergi-kalem` |

Detay → [CHANGELOG.md](CHANGELOG.md)
