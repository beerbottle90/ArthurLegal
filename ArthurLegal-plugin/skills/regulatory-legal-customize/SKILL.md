---
name: regulatory-legal-customize
description: >
  Mevzuat izleme profilinde tek bir şeyi değiştir — tüm kurulum görüşmesini
  yeniden yapmadan. İzlenen kurumlar (EPDK, BDDK, SPK, BTK, KVKK, Rekabet, GİB,
  Sigorta Tahkim, Resmî Gazete, yabancı rejimler), politika kütüphanesi,
  önemlilik eşiği, açık yönetim süreci, akışlar, tarama sıklığı, özetin
  alıcıları ya da matter klasörleri. Kullanıcı "şunu değiştir", "kurum ekle",
  "izleme listemi güncelle", "eşiği değiştir" ya da "customize" dediğinde kullan.
argument-hint: "[bölüm adı ya da değişikliğin tarifi]"
---

# /customize

## Ne zaman çalışır

Kullanıcı profilindeki bir şeyi — izlenen bir kurumu, önemlilik eşiğini, bir akışı, tarama sıklığını — kurulum görüşmesini baştan yapmadan ve dosyayı elle düzenlemeden değiştirmek istiyor.

## Ne yap

1. **Profili oku.** `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` ve bir üst klasördeki `~/.claude/plugins/config/claude-for-legal/firm-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa:
   > Henüz kurulum yapılmamış. Önce `/arthurlegal:regulatory-legal-cold-start-interview` çalıştırın — customize mevcut bir profili ayarlamak içindir.

2. **Haritayı göster** (her biri için tek satır mevcut değer):
   - **Kim olduğumuz** — ad, sektör, ülkeler, pratik ortamı *(tüm eklentilerle ortak — değişiklik `firm-profile.md`'e yazılır)*
   - **İzlenen kurumlar** (`## Regulators we watch`) — kurum, neden, akış kaynağı; "öncelikli" (politikayı en çok etkileyen) ve "izleme" ayrımı
   - **Politika kütüphanesi** (`## Policy library`) — politikalar, yerleri, sahipleri
   - **Önemlilik eşiği** (`## Materiality threshold`) — anında / haftalık özet / FYI; `/arthurlegal:regulatory-legal-reg-feed-watcher` çıktısını nasıl süzdüğü
   - **Açık yönetimi** (`## Gap response process`) — kim triyaj yapar, kim politikayı günceller, nerede takip edilir, eskalasyon
   - **Akışlar** (`## Feed configuration`) — ArthurLegal araçları, RSS adresleri, ücretli abonelik, `**Check cadence:**`, `**Digest channel:**`, `Digest output path`, taslak görüş takibi ve karar sahibi
   - **Kişiler** — hukuk müdürü, uyum yöneticisi, politika sahipleri, görüş yazısı hazırlayan, eskalasyon zinciri
   - **İş akışı** — matter workspaces, açık takip kaydı, `comment-tracker.yaml`, özet yayım sıklığı
   - **Entegrasyonlar** — ArthurLegal MCP, Thomson Reuters, Slack, belge deposu; düşüş yolları

3. **Sor:** "Neyi ayarlayalım? Bir bölüm seçin ya da değişikliği kendi cümlenizle anlatın."

4. **Değişikliği yap.** Mevcut değeri göster, yenisini al, aşağı akış etkisini açıkla, onay al, yaz. Örnekler:
   - *Kurum ekleme (EPDK, elektrik):* "Satıra neden ve akış yazılır: `tr_kurum_karari_ara(kurum="epdk", market="elektrik")` + `tr_resmi_gazete_tara(konu="enerji", query=…)`. `reg-feed-watcher` bir sonraki taramada bu kurumu süzer; `/arthurlegal:regulatory-legal-policy-diff` bu kurumdan gelen düzenlemeyi girdi olarak kabul eder. Dayanak: lisanslı piyasa faaliyetleri 6446 s. Kanun m. 4/1."
   - *Kullanıcı KİK, Sayıştay, TÜRKPATENT ya da İSTAÇ eklemek istiyor:* "ArthurLegal'da bu kaynaklar yok (resmî uçları cevap vermiyor). Satırı `Feed source: manual` ile ekleyebilirim; RG'de yayımlanan yönetmelik ve tebliğleri `tr_resmi_gazete_tara(query=…)` yakalar, kurul kararları için kurumun sitesini ya da RSS adresini siz verirsiniz."
   - *Ödeme kuruluşu için BDDK ekleme talebi:* "Ödeme kuruluşu faaliyet iznini Merkez Bankası verir (6493 s. Kanun m. 3/1-b, m. 15/1); doğru satır TCMB'dir ve akışı RG'dir. BDDK'yı da tutalım mı?"
   - *Eşiği sıkılaştırma:* "Haftalık özet kısalır; yeni eşiğin altındaki kalemler özetten düşer ama aranabilir kalır."
   - *Sıklık haftalık → günlük:* "`reg-change-monitor` her gün çalışır; RG taraması gün başına bir istek atar ve tek seferde en çok 60 günlük aralık tarar."
   - *Yeni politika eklendi:* "`/arthurlegal:regulatory-legal-policy-diff` yeni kuralları bu politikayla da karşılaştırır; görüş takibi bu politikayı etkileyen taslakları etiketler. Sahibi boşsa açıklar `owner: [unassigned]` düşer."
   - *Yabancı rejim (AB):* "Satır eklenir; kaynak `eu_search_eu_law`. ABD için ArthurLegal kaynağı yok — Federal Register API ya da kurum RSS'i `Free feeds` tablosuna, yorum için ABD'li avukat."
   - *Özet alıcısı değişti:* "`**Digest channel:**` güncellenir; Slack bağlı değilse özet yalnız dosya olarak yazılır."

   Kullanıcı bir madde, süre ya da eşik söylüyorsa yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; idari para cezası tutarlarını sabit yazma (güncel tutarı teyit et — dönemsel güncellenir).

5. **Ortak profil değişiklikleri** (ad, sektör, ülkeler, pratik ortamı) `firm-profile.md`'e yazılır:
   > Bu değişiklik tüm eklentileri etkiler — ülke listesini okuyan her eklenti artık [yeni değer]i görür.

   Pratik ortamı kurum içinden büroya geçiyorsa `## Matter workspaces` → `**Enabled:** ✓` ve `**Cross-matter context:** off` önerilir; Av. K. m. 38 gereği çatışma kontrolünü hatırlat (Hukuk Bürosu paketinde `/arthurlegal:firm-operations-conflict-check`).

6. **Kapat:** "Tamam. Bir sonraki çıktı bunu yansıtacak. Başka bir şey var mı? `/arthurlegal:regulatory-legal-customize` her zaman çalışır."

## Korkuluklar

- **Bölümü silme.** Bir kurum "çıkarılmak" istenirse `[Monitor only]` işaretini öner: akış arşivde kalır, aktif özetten çıkar.
- **İç tutarsızlığı işaretle.** Ör. izlenen kurum + o kurumun alanında faaliyet yok (EPDK var, lisans yok); "haftalık özet" + çeyrekte bir kalem bile çıkarmayacak eşik; "Sigorta Tahkim" düzenleyici gibi yazılmış (hakem kararıdır; düzenleyici SEDDK, akışı RG); KVKK izleniyor ama `/privacy-legal` profili farklı kurum listesi taşıyor.
- **Güvence kaybını işaretle.** Kaynak etiketleri, çekilemeyen veride UYARI satırı, `[verify]` etiketleri ve açık triyajındaki `[review]` işareti yük taşır — kaldırma. Eşik ayarlanabilir; ama aleyhe düzenleyici işlemi "anında"dan düşürmek isteniyorsa uyar: ilanı gereken düzenleyici işlemde dava süresi ilan tarihini izleyen günden işler (İYUK m. 7/4).
- **Anahtarları çevirme** (`## Regulators we watch`, `## Materiality threshold`, `## Feed configuration`, `**Check cadence:**`, `## Matter workspaces`, `Active matter:` vb.).
- **Tek seferde tek değişiklik.** Görüşmeyi baştan sorma.

---

## Kaynak katmani — /legal-research (v1.4.0)

> Bu plugin'in skill'leri **birincil kaynagi kendileri uretmez**. Mevzuat,
> ictihat, emsal sozlesme veya akademik doktrin gerektiginde asagidaki kaynak
> skill'lerine gec; sonucu bu plugin'in cikti formatina geri tasi.
>
> **Kaynak hiyerarsisi:** BIRINCIL (mevzuat/ictihat) → EMSAL (imzali
> sozlesme) → DOKTRIN (akademik). Cakisma halinde birincil ustundur —
> cakismayi raporla, ikincil kaynak lehine sessizce cozme.
>
> **100 saniye:** her arac cagrisi 100 saniyede iptal edilir ve *hicbir sey*
> dondurmez. Dar sorgu; iptal olursa ayni sorguyu tekrarlama, bol ve hangi kismin
> kapsanmadigini soyle.
>
> **Gizlilik:** uc MCP de PUBLIC arama aracidir — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| AZ duzenleyici degisiklik takibi — akt statusu degistiyse (`Legv olunmus`) ardil akti bul | `/arthurlegal:legal-research-az-mevzuat` |
| karsilastirmali regulasyon literaturu — **ikincil**, mevzuat yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
