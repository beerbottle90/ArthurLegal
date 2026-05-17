# Değişiklik Günlüğü

[Keep a Changelog](https://keepachangelog.com/tr-TR/1.1.0/) formatına uygundur.
Semver: [Semantic Versioning 2.0](https://semver.org/lang/tr/).

---

## [1.0.0] — 2026-05-17 — *Initial Public Release*

İlk halka açık sürüm. Anthropic'in [claude-for-legal](https://github.com/anthropics/claude-for-legal) referans paketinden türetilmiş, **dava + danışmanlık dengeli, 0–30 çalışanlı Türk hukuk büroları** için **danışman tarafı** adapte edilmiş hibrit hukuk asistanı paketi. Kardeş paket: [ArthurLegal Claude Corporate Assistant](../ArthurLegal%20Claude%20Corporate%20Assistant/) (in-house, danışan tarafı).

### Eklendi

**9 plugin:**

**Dava (4):**

- `dispute-litigation` — Genel dava yönetimi (HMK 6100 + UYAP); ticari + adli yargı; TTK m. 5/A zorunlu arabuluculuk ön-kontrol; AAÜT vekalet ücreti hesabı; tahkim klozu yorumu (ISTAC/ICC)
- `administrative-litigation` — İdari dava (İYUK 2577); 3 dereceli idari yargı (İdare Mah. → BİM → Danıştay); ÇED davaları m. 20/A ivedi rejim; EPDK/BDDK/SPK kararlarına dava
- `tax-litigation` — Vergi davası; İYUK m. 7 — **30 günlük süre kritik kontrolü**; uzlaşma vs. dava matrisi; Danıştay 3/4/7/9. Daire içtihat tarama; KDV iadesi davası, mukteza talebi
- `criminal-defense` — Ceza müdafaa; CMK 5271 + TCK 5237 + Avukatlık K. m. 35; **CMK görevli atama yönetimi** (48 saat sınırı); tutuklu müvekkil; müdahil vekilliği; uzlaştırma

**Danışmanlık (4):**

- `commercial-advisory` — Ticari sözleşme **yazma + inceleme** (TBK + TTK); NDA, satış, hizmet, distribütörlük, lisans; damga vergisi hesabı; KEP teslim; ISTAC tahkim klozu seçimi
- `corporate-advisory` — KOBİ + aile şirketi kurumsal danışmanlık (TTK GK/YK kararları, pay devri, esas sözleşme değişikliği); küçük ölçek M&A (share deal/asset deal); kurumsallaşma yol haritası
- `employment-advisory` — İş hukuku (4857 + 5510 + 6356 + 6331); **işveren tarafı** (fesih, iç soruşturma, mobbing iddia yönetimi) + **işçi tarafı** (kıdem-ihbar hesabı, işe iade davası, alacak davası); KVKK iş ilişkisi
- `ip-advisory` — Fikri sınai haklar (6769 SMK + TÜRKPATENT + Madrid Protokolü); marka clearance + tescil + yenileme; YİDK itiraz; **ihtarname yazımı**; UDRP domain takedown; 5651 + 5846 FSEK

**Büro işletim (1):**

- `firm-operations` — **Yeni müvekkil intake** (KVKK aydınlatma + MASAK Tebliğ 5 kimlik tespit + OpenSanctions tarama); **conflict check** (Av. K. m. 38 + TBB Meslek Kuralları m. 35-36); **ücret sözleşmesi** taslağı (AAÜT + KDV + stopaj + damga); vekalet şablonları (genel + özel + sınırlı yetki); baro koordinasyonu (CMK ödemeleri, aidat, levha değişikliği); aylık matter bazlı fatura

**MCP entegrasyonları (her plugin .mcp.json'da):**

- ✅ Mevzuat MCP (https://mevzuat.surucu.dev/mcp) — 26 araç
- ✅ Yargı MCP (https://yargimcp.surucu.dev/mcp) — 24 araç, 15 kurum
- ⚙️ OpenSanctions API (REST/WebFetch) — müvekkil due diligence
- ✅ UYAP / KEP / e-Tebligat — manuel oturum + WebFetch pattern rehberleri
- (Kütüphane) iManage, Slack, GDrive, Box vd.

**TR Overlay:**

- `tr-overlay/firm-profile.md` — Büro profil şablonu (ortaklık yapısı + müvekkil portföyü + sektör dağılımı + baro kayıt + AAÜT tercihi), varsayımsal `ArthurLegal Hukuk Bürosu` örneği üzerinden
- 9 plugin için TR-adapte CLAUDE.md profilleri (`tr-overlay/profiles/`)
- 20+ TR referans dosyası (`tr-overlay/references/`):

  **Avukatlık meslek pratiği (YENİ — hukuk bürosuna özel):**
  - `aaut-rehberi.md` — Avukatlık Asgari Ücret Tarifesi — uygulama, ücretsiz dava, müdafaa, vekalet ücretine hükmedilmesi
  - `vekalet-uyap-rehberi.md` — Vekalet (genel + özel + sınırlı), noter onayı vs. baro onayı, UYAP'ta vekalet sunumu, azil + istifa prosedürü
  - `mesleki-sir-rehberi.md` — Avukatlık K. m. 36 + TBB Meslek Kuralları m. 36-37; CMK m. 130; istisnalar (suç önleme, ifade verme); pratik scenarios
  - `conflict-check-rehberi.md` — Av. K. m. 38 yasaklılık + TBB MK m. 35-36 nüansları; bireysel/kurumsal/grup çatışma; mevcut/eski müvekkil; conflict-clearance prosedürü
  - `cmk-gorevli-rehberi.md` — CMK 5271 + Av. K. m. 35 müdafiilik; baro CMK servisi atama prosedürü; 48 saat sınırı; tutukluluk sorgu prosedürü; ödeme takibi
  - `baro-islemleri-rehberi.md` — Baro işlemleri: ruhsat, levha kayıt, levha değişikliği (asıl→bağlı), yıllık aidat, sicil dosyası, disiplin süreçleri
  - `ucret-sozlesmesi-rehberi.md` — Avukatlık ücret sözleşmesi (Av. K. m. 163-166); saatlik vs. götürü vs. **başarı bonusu (success fee — Av. K. m. 164 sınırı)**; KDV (% 20) + Stopaj (% 20) + Damga (binde 9,48); ücret tahsil yolları
  - `kep-etebligat-rehberi.md` — KEP + e-Tebligat sistemi (5070 sayılı K. + 7201 sayılı Tebligat K.); müvekkille KEP iletişimi; mahkemeden gelen e-tebligata cevap süresi
  - `masak-kimlik-tespit-rehberi.md` — MASAK Tebliğ Sıra No. 5 — avukatın kimlik tespit yükümlülüğü; gerçek faydalanıcı sorgusu; şüpheli işlem bildirimi (suç gelirleri)

  **Türk mevzuatı + içtihat (kardeş projeden uyarlanmış):**
  - `kanun-kisaltmalar.md` — TR mevzuat + enerji + sermaye piyasası + yaptırım kısaltma sözlüğü
  - `mevzuat-mcp-rehberi.md` — Mevzuat MCP kullanım kılavuzu
  - `yargi-mcp-rehberi.md` — Yargı MCP 24 araç + büro pratiğinde kullanım pattern'ları
  - `hmk-rehberi.md` — HMK temel maddeler + dava akışı (büro tarafı: dilekçe yazımı + duruşma)
  - `uyap-rehberi.md` — UYAP modülleri + **avukat portalı** kullanım rehberi
  - `iyuk-rehberi.md` — İYUK m. 7 (idare 60 g / vergi 30 g) + m. 20/A (ÇED ivedi) + m. 27 (yürütmenin durdurulması) + m. 45/46 (istinaf/temyiz)
  - `idari-yargi-yapisi-rehberi.md` — 3 dereceli yapı + Danıştay K. m. 24/30 istisnaları
  - `damga-vergisi-rehberi.md` — DVK hesabı + sözleşme tiplerine göre tipik oranlar
  - `kvkk-m11-cevap-sablonu.md` — DSAR cevap şablonu (avukatın müvekkilinin VERBİS sicilinde danıştığı durum)
  - `smk-rehberi.md` — 6769 SMK marka/patent/tasarım pratiği
  - `turkpatent-rehberi.md` — TÜRKPATENT online araçlar + YİDK itiraz prosedürü
  - `udrp-domain-rehberi.md` — Sahte domain takedown
  - `vuk-rehberi.md` — Vergi Usul Kanunu temel maddeler + süreler (vergi davası için)
  - `gib-ozelge-rehberi.md` — Özelge talep süreci
  - `istac-rehberi.md` — ISTAC + ICC tahkim
  - `opensanctions-rehberi.md` — Müvekkil due diligence için REST API WebFetch pattern
  - `yaptirim-tarama-rehberi.md` — 6 yaptırım rejimi + müvekkilin yurtdışı tarafı varsa kontrol

**Dağıtım paketleri:**

- `dist/claude-code/` — Claude Code (CLI / VSCode) kurulum rehberi
- `dist/claude-projects/` — Claude.ai Projects için SYSTEM_PROMPT.md + knowledge dosyaları (açık halde)
- `release/ArthurLegal-Claude-Law-Firm-Assistant-v1.0.0.zip` — Tek dosya kurulum paketi

**Manifest:**

- `.claude-plugin/marketplace.json` — 9 plugin'i expose eden marketplace manifest

**Sürüm disiplini:**

- `VERSION.md` + `CHANGELOG.md` — Semver 2.0

### Tasarım notları

- **TR overlay orijinal Anthropic skill'lerini DEĞİŞTİRMEZ;** üstüne ek context koyar. Upstream güncellemesi cherry-pick ile alınabilir.
- **"Danışan → Danışman" geçişi:** Corporate paketten farklı olarak tek "şirket" yerine **çok-müvekkilli matter workspace + zorunlu conflict check** modeli kurulmuştur. Avukatlık K. m. 36 + TBB Meslek Kuralları çerçevesi birincil guardrail'dır.
- **Çıktı başlığı yeniden tasarlandı:** `AVUKATLIK K. m. 36 – VEKİL-MÜVEKKİL YAZIŞMASI – DAHİLİ VE GİZLİDİR – [Matter ID]`. Corporate'taki `HUKUK MÜŞAVİRLİĞİ DAHİLİ ÇALIŞMA NOTU` yerine geçer.
- **Cross-matter context default OFF.** Müvekkil A'nın bilgisi müvekkil B'nin dosyasına asla sızmaz.
- **AAÜT entegre:** Tüm fee/sulh/dava değerlendirmelerinde AAÜT (TBB tarafından yayımlanır) bağlayıcı eşik olarak kontrol edilir.
- **CMK görevli atama akışı:** 48 saat sınırı (CMK m. 91), savunma stratejisi taslağı, baro CMK ödeme süreç takibi entegre.
- **3 dereceli idari yargı doğru kurgulandı:** İdare Mah. → BİM → Danıştay; Danıştay K. m. 24/30 dar istisnalar ayrı.
- **İYUK süre ayrımı:** İdare mahkemeleri 60 g, vergi mahkemeleri 30 g (2021/7331 sayılı K. değişikliği); ÇED davaları için m. 20/A ivedi rejim.
- **TTK m. 5/A zorunlu arabuluculuk:** Ticari uyuşmazlık + alacak/tazminat davalarında dava şartı; `dispute-litigation` skill'leri ön-kontrol yapar.
- **MASAK Tebliğ 5 entegre:** Yeni müvekkil intake'inde kimlik tespit yükümlülüğü + şüpheli işlem bildirim takvimi otomatik tetiklenir.

### Bilinen sınırlar

- `tr-overlay/firm-profile.md` ve plugin profillerindeki `[DOLDUR]` ve `[…]` yer-tutucular kurulum sonrası kullanıcı tarafından doldurulmalıdır.
- OpenSanctions API key kullanıcı tarafından temin edilmeli (paid membership).
- En güncel Yargıtay/Danıştay kararları için UYAP/Lexpera manuel doğrulama hâlâ tavsiye edilir.
- Conflict check otomatiktir ama Av. K. m. 38'in nüansları **insan yargısı** ister; otomatik tarama eşik filter görevi görür.
- CMK görevli atama baro CMK servisi üzerinden gelir — paket atama otomasyonu sağlamaz.
- Tasarı/kanun teklifi aşamasındaki düzenlemeler kapsam dışıdır.

### Atıf

- **Author:** Claude (Anthropic, Opus 4.7 — `claude-opus-4-7`)
- **Designer:** Ertuğ Demir
- **Knowledge base:** Anthropic [claude-for-legal](https://github.com/anthropics/claude-for-legal) (Apache 2.0)
- **Kardeş paket:** ArthurLegal Claude Corporate Assistant v1.0.0

---

[1.0.0]: ./VERSION.md
