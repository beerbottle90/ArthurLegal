# Fransa DILA Açık Veri (LEGI/JORF/CASS/JADE/DOLE) — Kullanım Rehberi (toplu indirme + WebFetch)

> **MCP/connector durumu:** ⚠️ Hazır MCP sunucusu yok — birincil yöntem toplu dosya indirme (bulk download) ve gerektiğinde WebFetch ile dizin/dosya doğrulama. Loopback FR MCP kurulumu için altyapı kaynağıdır.
> **Erişim:** ✅ Açık erişim — API anahtarı gerekmez; kimlik bilgisi olmadan HTTPS/FTPS ile indirilir.
> **Yargı çevresi notu:** ArthurLegal'in birincil yargı çevresi Türkiye'dir. Bu kaynak yalnızca dosya Fransa hukukuna değdiğinde kullanılır; çok ülkeli karşılaştırmalı sorular için `karsilastirmali-hukuk-rehberi.md` yönlendirmesi esastır. Fransa için birincil canlı doğrulama kaynağı `france-legislation-rehberi.md`'de anlatılan Légifrance'tır; bu rehber onun toplu-veri tamamlayıcısıdır.

## DILA Açık Veri nedir?

DILA (Direction de l'information légale et administrative), Fransa Başbakanlığı'na (Premier ministre) bağlı resmi yayın idaresidir; Légifrance'ı işleten kurumdur. `echanges.dila.gouv.fr/OPENDATA/` adresinde, Légifrance'ın arkasındaki veritabanlarının **tam tabanlı (full dump) + periyodik delta** arşivlerini kimlik doğrulamasız yayımlar.

Kapsanan başlıca tabanlar (dizin adları birebir, çekim: 13.08.2026):

| Dizin | İçerik |
|---|---|
| `LEGI` | Konsolide kanun ve kod metinleri — madde bazında sürüm geçmişiyle (point-in-time) |
| `JORF` | Journal officiel de la République française (Resmî Gazete) |
| `KALI` | Toplu iş sözleşmeleri (conventions collectives) |
| `CASS` + `INCA` | Cour de cassation kararları (yayımlanmış + yayımlanmamış/inédit) |
| `JADE` | Conseil d'État ve idari istinaf mahkemeleri (CAA) kararları |
| `CAPP` | İstinaf mahkemeleri hukuk daireleri kararları |
| `CONSTIT` | Conseil constitutionnel kararları |
| `DOLE` | Yasama süreci dosyaları (dossiers législatifs — gerekçe ve tarihçe) |

Aynı dizinde `DTD_LEGIFRANCE` altında yayımlanmış DTD'ler bulunur: veri, yayımlı şemalara sahip legacy XML formatındadır.

**ArthurLegal için neden gerekli?** Fransa şu ana kadar WebFetch katmanındaydı: Légifrance sayfası tek tek çekiliyor, "belirli bir tarihte yürürlükte olan metin" sorularında sayfa navigasyonuna bağımlı kalınıyordu. DILA dökümleri, konsolide mevzuatın madde-sürüm geçmişini bütün halinde verir; bu, loopback'te self-host edilen bir FR MCP ile point-in-time mevzuat sorgusunu mümkün kılar — "kaynaksız hukuk yok" ilkesinin gerektirdiği kaynak + çekim tarihi damgası, kendi anlık görüntü (snapshot) kaydımızla birlikte atılır.

## Endpoint/URI şeması

```
https://echanges.dila.gouv.fr/OPENDATA/                  # taban dizin listesi
https://echanges.dila.gouv.fr/OPENDATA/{TABAN}/          # taban başına arşiv listesi
ftps://echanges.dila.gouv.fr                             # aynı içerik, FTPS
```

Her taban dizininde iki dosya türü bulunur (adlar canlı dizinden birebir doğrulanmıştır):

```
Freemium_{taban}_global_YYYYMMDD-HHMMSS.tar.gz   # tam taban dökümü
{TABAN}_YYYYMMDD-HHMMSS.tar.gz                   # artımlı (delta) arşiv
```

Doğrulanmış örnekler (çekim: 13.08.2026):

```
https://echanges.dila.gouv.fr/OPENDATA/LEGI/Freemium_legi_global_20250713-140000.tar.gz   (~1,1 GB)
https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20250713-205013.tar.gz                   (günlük delta)
https://echanges.dila.gouv.fr/OPENDATA/CASS/Freemium_cass_global_20250713-140000.tar.gz   (~248 MB)
https://echanges.dila.gouv.fr/OPENDATA/CASS/CASS_20260810-213209.tar.gz                   (haftalık delta)
```

Güncel taban durumu = en yakın tarihli Freemium dökümü + o tarihten sonraki tüm deltaların sırayla uygulanması. Delta sıklığı tabana göre değişir (LEGI günlük, CASS haftalık gözlemlendi); entegrasyonda taban başına ayrı takip edilmelidir.

## Uygulamalı örnekler

**Örnek 1 — LEGI dizinini doğrulayıp güncel dökümü tespit etme (WebFetch):**

```
WebFetch:
  url: https://echanges.dila.gouv.fr/OPENDATA/LEGI/
  prompt: "En güncel Freemium_legi_global_* dosyasının tam adını ve ondan
           sonraki en son üç LEGI_YYYYMMDD-HHMMSS.tar.gz delta dosyasını listele."
```

Dönen dosya adları, indirme betiğine (ör. `curl -O` / FTPS istemcisi) parametre olarak geçilir; dizin listesindeki ad hiçbir zaman elle tahmin edilmez.

**Örnek 2 — Lisans ve üretici teyidi (WebFetch, data.gouv.fr kaydı):**

```
WebFetch:
  url: https://www.data.gouv.fr/fr/datasets/legi-codes-lois-et-reglements-consolides/
  prompt: "Bu veri setinin lisansı ve üreticisi nedir? Lisans adını birebir aktar."
```

Doğrulanmış sonuç (çekim: 13.08.2026): lisans **"Licence Ouverte / Open Licence"**, üretici **Premier ministre**, indirme adresi `https://echanges.dila.gouv.fr/OPENDATA/` (HTTPS) ve `ftps://echanges.dila.gouv.fr` (FTPS).

**Örnek 3 — İndirilen arşivden madde sürümü kullanma (loopback FR MCP hedef akışı):**

Tar.gz içindeki XML'ler, `DTD_LEGIFRANCE` şemalarına göre ayrıştırılıp yerel dizine yüklenir; asistan mevzuat sorusunu loopback MCP'den yanıtlar ve atıfı **kendi snapshot tarihimizle** damgalar (aşağıdaki atıf disiplinine bakınız). Canlı teyit gerektiğinde Légifrance'a (`france-legislation-rehberi.md`) dönülür.

## Alternatifler (dürüst değerlendirme)

**Judilibre API** — Cour de cassation'un resmi açık içtihat API'sidir; kararlar zenginleştirilmiş ve anonimleştirilmiş olarak sunulur. Veri lisansı Licence Ouverte / Open Licence 2.0'dır (data.gouv.fr kaydında teyitli, üretici: Cour de cassation). **Ancak** erişim PISTE portalında hesap açma + API anahtarı (KeyId) gerektirir (`https://api.piste.gouv.fr/cassation/judilibre/v1.0`); bu, ArthurLegal'in kimlik-bilgisisiz erişim tercihine aykırıdır. İçtihat için DILA'nın CASS/INCA dökümleri aynı veriyi anahtar gerektirmeden verir; Judilibre yalnızca canlı arama gereken senaryolarda değerlendirilmelidir.

**pylegifrance + mcp-server-legifrance** — MIT lisanslı topluluk projeleri; MCP sunucusu pylegifrance üzerine kuruludur. Légifrance erişimi maintainer'ın üçüncü-taraf ağ geçidi (`lab.dassignies.law/api/`) üzerinden ve ondan alınan API anahtarıyla sağlanır: resmî olmayan tek kişilik bir aracıya hem kimlik bilgisi hem trafik bağımlılığı doğar. Bu yapı, üçüncü-taraf-geçitli anahtar bayrağıyla işaretlenmiştir; üretim akışına alınmamalıdır.

**Dahliyaal/justicelibre MCP** — MIT lisanslı; yaklaşık 3,3 milyon karar ve 1,5 milyon mevzuat maddesi indeksler, self-host edilerek loopback'te çalıştırılabilir (kamusal örneği bulut üzerindedir). Veri kaynakları Licence Ouverte 2.0 kapsamındadır. **Ancak** tek maintainer'lı bir projedir ve kaynak-bazlı veri kesim tarihi (per-source cutoff) damgalanmadan atıf sözleşmemizi karşılayamaz: hangi tabanın hangi tarihe kadar güncel olduğu bilinmeden "çekim tarihi" damgası anlamsızlaşır. Bu iki koşul çözülmeden yalnızca keşif amaçlı kullanılabilir.

## Atıf disiplini

Her hukuki önerme kaynak + çekim/snapshot tarihi taşır; döküm verisinde "çekim tarihi" = kullanılan snapshot'ın durum tarihi:

```
[DILA LEGI — {kod/kanun adı, madde no, sürüm yürürlük tarihi} — snapshot: GG.AA.YYYY]
[DILA CASS — Cour de cassation, {daire, karar tarihi, esas no} — snapshot: GG.AA.YYYY]
[DILA JORF — JORF {tarih, metin no} — snapshot: GG.AA.YYYY]
```

Canlı Légifrance teyidi yapıldıysa ek olarak: `[Légifrance — {URL} — çekim: GG.AA.YYYY]`.

Kurallar:
- Snapshot tarihi, uygulanmış son delta dosyasının tarihidir; Freemium dökümünün tarihi değil.
- İçtihat tabanları (CASS, INCA, JADE, CAPP) **kanunen pseudonymize edilmiştir**; taraf adları metinde yoktur ve atıfta bu durum belirtilir (ör. "karar metni DILA açık verisinde kişisel veriler yönünden anonimleştirilmiş haliyle yer alır"). OPENDATA dizinindeki `AVERTISSEMENT-Donnees_a_caractere_personnel.pdf` uyarısı bu rejimin parçasıdır.
- Doktrin bağlamdır, otorite değildir; DOLE'daki yasama gerekçeleri yorum bağlamı olarak kullanılır, bağlayıcı norm olarak sunulmaz.
- Değerlendirme (eval) verisi hiçbir zaman atıf kaynağı değildir.
- İndirilip ayrıştırılmamış bir metin, indirilmiş gibi sunulmaz; snapshot'ta olmayan güncel değişiklik için Légifrance canlı teyidi zorunludur.

## Lisans ve sınırlar

- **Lisans:** "Licence Ouverte / Open Licence" (data.gouv.fr LEGI kaydında birebir teyitli; üretici: Premier ministre, çekim: 13.08.2026). Kaynak gösterme koşuluyla ticari kullanım dahil yeniden kullanım serbesttir. Taban bazında lisans sürümü (1.0/2.0) entegrasyon öncesi taban taban doğrulanmalı.
- **Pseudonymization bayrağı:** Fransız içtihat tabanları kanun gereği pseudonymize edilir; bu, atıflarda açıkça yüzeye çıkarılır. Kişileri yeniden tanımlamaya (re-identification) yönelik hiçbir kullanım yapılmaz.
- **Mühendislik maliyeti bayrağı:** Yük governance değil mühendisliktir — legacy XML + DTD ayrıştırma, Freemium + delta durum takibi, taban başına farklı güncelleme sıklığı. Delta zinciri kırılırsa taban tam dökümden yeniden kurulmalıdır.
- **Güncellik sınırı:** Döküm verisi tanımı gereği snapshot'tır. "Bugün yürürlükte mi?" sorusunun nihai cevabı Légifrance'tır; DILA verisi tek başına canlı teyit yerine geçmez.
- **Format sınırı:** JSON/REST yoktur; tar.gz + XML vardır. Doğrudan WebFetch ile içerik sorgusu pratik değildir — WebFetch yalnızca dizin listeleri ve meta doğrulama için kullanılır.

## Karar kaydı (mini-ADR)

**Bağlam.** Fransa, ArthurLegal'de WebFetch katmanındaydı: Légifrance sayfa sayfa çekiliyor, madde sürüm geçmişi ve point-in-time sorgular (belirli tarihte yürürlükteki metin) güvenilir şekilde yanıtlanamıyordu; içtihat için toplu erişim hiç yoktu.

**Karar.** DILA açık veri dökümleri (öncelik: LEGI, ardından CASS/JADE/DOLE) toplu-veri katmanı olarak benimsenir; hedef, loopback'te self-host edilen bir FR MCP'dir. Koşullar: (1) Freemium + delta zinciri için kendi snapshot-durum takibimiz tutulur ve atıflar snapshot tarihiyle damgalanır; (2) içtihat pseudonymization'ı atıflarda belirtilir; (3) Légifrance canlı doğrulama çapası olarak kalır.

**Sonuçlar.** Kazanım: point-in-time konsolide mevzuat, kimlik bilgisisiz ve self-host edilebilir; içtihat ve yasama tarihçesi aynı boru hattına girer. Eski rotada kalanlar: güncel yürürlük teyidi ve tekil sayfa doğrulaması Légifrance/WebFetch'te. Entegrasyonda yeniden doğrulanacaklar: taban başına lisans sürümü, delta sıklıkları ve dosya adlandırma deseni, DTD sürümleri, Judilibre/justicelibre alternatiflerinin koşullarının değişip değişmediği.

## İlgili rehberler

- `france-legislation-rehberi.md` — Fransa için birincil canlı kaynak (Légifrance/WebFetch); bu rehber onun toplu-veri tamamlayıcısıdır, canlı teyit oraya döner.
- `karsilastirmali-hukuk-rehberi.md` — Fransa'nın ne zaman devreye gireceği; çok yargı çevreli sorularda yönlendirme çerçevesi.