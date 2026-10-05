# CHANGELOG — ArthurLegal Academician Assistant

Bu paketteki tüm önemli değişiklikler burada belgelenir.

---

## [1.0.3] — 2026-09-22 — *Madde Doğrulama Kapısı; Yanlış Madde Atıfları Düzeltildi*

> **Düzeltme sürümü.** Bir iş ve fikri haklar protokolünün 5.5 klozuna "SMK m. 120, ŞİRKET'in önalım hakkı" yazıldı. SMK m. 120
> "Çalışanın önalım hakkı"dır: işveren iflas eder ve iflas idaresi buluşu işletmeden ayrı devretmek isterse hak çalışanındır.
> Kök neden: belge gövdesine yazılan madde numaraları atıf disiplininin dışında kalıyordu, bir maddeyi okumak iki çağrı ve
> büyük bir madde ağacı gerektiriyordu ve bilgi dosyalarındaki bazı madde haritaları yanlıştı. Talimat metni değişti.

### Değişti

1. `SYSTEM_PROMPT.md` (ÜYZ Kapısı): **madde doğrulama kapısı.** Not, sözleşme, protokol, dilekçe veya dosya gövdesinde geçen her
   kanun maddesi bu sohbette çekilmiş olmalı; maddeye yüklenen içerik (hakkın sahibi, şart, süre, sonuç) başlık ve metinle
   örtüşmeli; çekilemeyen madde gövdeye numarasıyla yazılmaz. İnceleme notunda "Madde kontrolü:" cümlesi. Doğrulama çağrıları
   "en az çağrı" kuralına tabi değildir; Bedesten hız kuralı bir tempo kuralıdır, doğrulanacak madde sayısına sınır değildir.
2. `knowledge/references/mevzuat-mcp-rehberi.md`: bölüm 9 (madde doğrulama kapısı); tek çağrılı madde okuma
   (`tr_mevzuat_madde_getir(number="6769", madde_no="120")`, araç şemasında görünüyorsa; görünmüyorsa ağaç yolu);
   `tr_mevzuat_icinde_ara` madde numarasıyla madde bulma yolu değildir.

### Düzeltildi

1. Bu paketin bilgi dosyalarında ikinci denetimden geçen madde atfı düzeltmesi yoktur.
2. `smk-rehberi.md` (Law Firm, Corporate): m. 5/1 ve m. 6 bentleri, m. 29 ve 30 ile 149 ile 151 (ceza m. 30'dadır), m. 156,
   m. 101 (koruma süresi), m. 18 ve 20 itiraz süreleri resmî metne göre düzeltildi; **Çalışan buluşları (SMK m. 113 ile 122)**
   bölümü eklendi. `ip-advisory.md`: m. 115 ile 118 faydalı model değil çalışan buluşu hükümleridir.

### Bilinen açık

- İdari yargı ve vergi dosya gruplarındaki 130 bulgu ikinci denetimden geçmediği için uygulanmadı; fikri mülkiyet ve ticaret,
  avukatlık ve büro, iş hukuku ve KVKK grupları henüz denetlenmedi. Madde doğrulama kapısı bu dosyalardaki numaraları da
  çekmeden kullanmayı yasaklar.

### Yükleme

`SYSTEM_PROMPT.md` yeniden yapıştırılır. Project knowledge'da şu dosyalar yenilenir: `knowledge/references/mevzuat-mcp-rehberi.md`, `knowledge/skills/atif-kaynak__skills.md`.

---

## [1.0.2] — 2026-09-20

Türkiye backend'i (ArthurLegalTR) 0.4.0: içtihat ve mevzuat aramasında tek taraflı tarih aralığı artık çalışıyor. Bedesten yalnız
`date_from` verilen aramayı sessizce süzgeçsiz döndürüyordu (`+"işe iade"` için 1.048 yerine 52.993 karar); literatür taramasında
"son beş yılın içtihadı" diye daraltılmış aramalar bu gözle yeniden yapılmalıdır. `knowledge/references/yargi-mcp-rehberi.md` ve
`knowledge/references/mevzuat-mcp-rehberi.md` yenilendi: tarih kontrolü, `tr_mevzuat_ara` sayfa boyu (en çok 20), sorgusuz
listeleme, yerel arşivin kurum bazında gerçek kapsamı ve `konu` ön elemesi (sunucuda koşan yerel model; ölçülmüş sınırlarıyla).
Akademik yazımda `konu` süzgeci bir kaynak tarama yöntemi olarak yöntem bölümünde anılabilir; kapsam iddiasına dayanak yapılamaz.
`status` çıktısında `backend_status.tr.version` 0.4.0 veya üstü olmalıdır.

---

## [1.0.1] — 2026-09-06

Türk hukuku artık ArthurLegal MCP'nin `tr_` araçlarından çekilir (`arthurlegal-mcp.fly.dev/mcp`, auth yok): mevzuat ve gerekçe, Yargıtay/Danıştay/AYM içtihadı, Resmî Gazete, sekiz düzenleyici kurum ve 19.404 belgelik semantik arşiv; DergiPark doktrini aynı uçta `scholar_` ile. `yargi-mcp-rehberi.md` ve `mevzuat-mcp-rehberi.md` baştan yazıldı; agent ve skill dosyalarındaki atıf etiketleri `[ArthurLegal TR — …]` oldu. TR Legal MCP (yargi-mcp-pro) yalnız AİHM, KİK, Sayıştay gibi kapsam dışı kaynaklar için isteğe bağlıdır.

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
