# Sürüm Bilgisi

**Sürüm:** 1.0.2
**Yayın tarihi:** 2026-09-13
**Önceki sürüm:** 1.0.1
**Lisans:** Proprietary, Non-Commercial (bkz. [LICENSE](LICENSE)); `claude-for-legal` bileşenleri Apache 2.0

## Semver özeti

- **Major (1.x.x):** Geriye uyumsuz mimari değişiklik
- **Minor (x.1.x):** Geriye uyumlu yeni plugin / dal / rol / referans ekleme
- **Patch (x.x.1):** Hata düzeltme, içerik güncelleme

## Bu sürümde

**v1.0.2 — Arthur Mask.** Dosya belgeleri Claude'a verilmeden önce kullanıcının Windows bilgisayarında maskelenebilir (yalnız Claude Desktop). Sistem talimatına Arthur Mask bölümü, `arthur-mask-rehberi.md` referansı, `ARTHUR-MASK.md` kullanım rehberi eklendi.

> **8/8 plugin kurulu** (her biri 2-5 skill — toplam 28 skill + 24 referans). Referansların tamamı yargısal/tarafsız çerçevededir.

v1.0.0 — **ArthurLegal Courthouse** ilk sürüm. Türk **yargı mensubu** (mahkeme hâkimleri + mahkeme kalem memurlukları) için **yargısal / tarafsız** decision-support asistanı. Diğer ArthurLegal paketlerinden farkı: savunuculuk değil, **tarafsızlık + sıfır-halüsinasyon atıf** disiplini.

**Mimari:** 4 dal × 2 rol = **8 plugin** matrisi.

| Dal | Hâkim | Kalem |
|---|---|---|
| Hukuk (HMK) | `hukuk-hakim` | `hukuk-kalem` |
| Ceza (CMK) | `ceza-hakim` | `ceza-kalem` |
| İdari (İYUK) | `idari-hakim` | `idari-kalem` |
| Vergi (VUK+İYUK) | `vergi-hakim` | `vergi-kalem` |

Detay → [CHANGELOG.md](CHANGELOG.md)
