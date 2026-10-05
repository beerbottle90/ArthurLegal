# CHANGELOG — ArthurLegal Academician Assistant

Bu paketteki tüm önemli değişiklikler burada belgelenir.

---

## [1.0.0] — 2026-07-09

İlk yayın. Hukuk akademisyeni (araştırma görevlisi → profesör) için araştırma, yazım,
atıf doğrulama, yayın etiği, tez danışmanlığı ve fon başvurusu asistanı.

### Konumsal ilke — ÜYZ Kapısı

Bu paketi diğer ArthurLegal paketlerinden ayıran temel karar: diğerlerinde asistan
düzenlemenin **öznesine** yardım ederken, burada **asistanın kendisi düzenlemenin
nesnesidir.** Akademik yayın ve proje süreçlerinde üretken yapay zekâ kullanımı hem
Türkiye'de hem uluslararası düzlemde doğrudan düzenlenmiştir.

Dört kural her çıktıdan önce gelir:

1. **ÜYZ yazar olamaz** — sorumluluk her zaman insandadır.
2. **Kullanım beyan edilir** — her esaslı çıktı, kopyala-yapıştır hazır bir ÜYZ beyan
   bloğuyla biter.
3. **Gizli müsvedde yutulmaz** — değerlendirme altındaki metin asistana girilmez.
4. **Sıfır-halüsinasyon atıf** — çekilmemiş hiçbir kaynak dipnota giremez.

### Eklenen — 8 plugin, 28 skill

- `arastirma-tasarim` (4): `arastirma-sorusu`, `literatur-haritasi`, `yontem-secimi`,
  `etik-kurul-triyaji`
- `makale-yazim` (4): `makale-iskeleti`, `dergi-secimi`, `hakem-yanit-mektubu`,
  `ozet-anahtar-kelime`
- `atif-kaynak` (3): `atif-dogrulama`, `kaynakca-uret`, `stil-donusturme`
- `yayin-etigi` (4): `uyz-beyani`, `ihlal-triyaji`, `benzerlik-yorumu`, `yazarlik-credit`
- `akademik-yukselme` (3): `docentlik-puan-analizi`, `dosya-eksik-analizi`,
  `atama-kriter-kontrol`
- `proje-fon` (3): `tubitak-basvuru`, `ab-horizon-basvuru`, `is-paketi-kurgu`
- `tez-danismanlik` (3): `tez-yapisi`, `savunma-hazirlik`, `ogrenci-geribildirim`
- `hakemlik-editorluk` (4): `hakem-rubrigi`, `editor-karar-mektubu`, `cope-vaka-akisi`,
  `jury-tez-degerlendirme`

### Eklenen — 23 referans

ÜYZ ve etik: `uyz-beyan-rehberi`, `hakemlik-gizlilik-rehberi`, `yayin-etigi-rehberi`,
`etik-kurul-rehberi`, `benzerlik-raporu-rehberi`, `yazarlik-credit-rehberi`

Kariyer ve fon: `docentlik-hukuk-temel-alani-rehberi`, `atama-yukseltme-rehberi`,
`tubitak-ardeb-rehberi`, `ab-horizon-plan-s-rehberi`

Yayın ekosistemi: `dergi-secimi-rehberi`, `yagmaci-dergi-rehberi`, `bibliyometri-rehberi`,
`trdizin-dergipark-rehberi`, `acik-erisim-rehberi`

Atıf: `atif-usulu-tr-rehberi`, `atif-stilleri-uluslararasi-rehberi`

Kaynak erişimi: `akademik-api-rehberi`, `ticari-veritabani-rehberi`,
`karsilastirmali-hukuk-rehberi`, `yargi-mcp-rehberi`, `mevzuat-mcp-rehberi`,
`kanun-kisaltmalar`

### Eklenen — 4 agent

`atif-izleyici` (haftalık) · `ictihat-izleyici` (haftalık) · `cfp-izleyici` (aylık) ·
`docentlik-ilerleme` (aylık)

### Bilinçli tasarım kısıtları

- **`hakemlik-editorluk` müsvedde metni istemez ve kabul etmez.** Kullanıcı değerlendirdiği
  bir metni yapıştırırsa asistan durur ve gizlilik uyarısı verir. Metin okumaz, süreç
  yürütür. Dayanak: TÜBİTAK ÜYZ Rehberi § 2.2.1 · NIH NOT-OD-23-149 · NSF · Elsevier ·
  Springer Nature · Wiley · ICMJE.
- **Doçentlik puan tablosu pakete gömülmemiştir.** ÜAK Hukuk Temel Alanı ölçütleri
  dönemden döneme değişir. Referans dosyası tablonun **mimarisini** anlatır; hiçbir
  hesaplama, kullanıcı kendi başvuru dönemine ait ÜAK PDF'ini teyit etmeden yapılmaz.
- **Benzerlik raporu için hiçbir yüzde eşiği önerilmez.** Evrensel eşik yoktur; eşiği
  kurum/dergi belirler. Rapor **nitel** okunur.
- **Bibliyometrinin sınırı açıkça beyan edilir.** Hukuk kitap ve ulusal-dil dergisi
  ağırlıklı bir disiplindir; WoS'ta büyük ölçüde AHCI'da yer alır ve AHCI'ya Impact Factor
  veya quartile atanmaz. JIF ve h-index hukukta yanıltıcıdır (DORA · CoARA · Leiden).
- **Erişilmeyen kaynaklar dürüstçe beyan edilir.** Lexpera, Kazancı, Jurix, Legalbank,
  HeinOnline, Westlaw, LexisNexis ve Beck-online'ın halka açık API'si yoktur; asistan
  onlardan çekmiş gibi davranmaz. Literatür taraması kütüphane taramasının yerine geçmez.
- **Hiçbir API anahtarı gömülmemiştir.** Tüm programatik kaynaklar anahtarsızdır veya
  kullanıcının kendi hesabıyla erişilir.

### Gizlilik ve veri

- Paket **gerçek kişi veya kurum verisi içermez**; tüm profil alanları `[DOLDUR]`.
- Katılımcı verisi, mülakat kaydı ve ham araştırma verisi asistana girilmez.

### Lisans

Paket bir bütün olarak **ArthurLegal Proprietary Non-Commercial License** altındadır.
Türetildiği Anthropic `claude-for-legal` bilgi tabanı Apache 2.0'dır; ilgili bildirim
`LICENSE-APACHE-2.0-THIRD-PARTY.txt` içinde korunmuştur.
