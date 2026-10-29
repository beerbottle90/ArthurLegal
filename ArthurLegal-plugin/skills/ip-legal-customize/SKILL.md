---
name: ip-legal-customize
description: >
  Fikri mülkiyet pratik profilinde tek bir şeyi, kurulum görüşmesini baştan
  yapmadan değiştirir: risk iştahı, eskalasyon kişileri, dış avukat ve vekil
  listesi, portföy kapsamı, marka izleme, uygulama duruşu ve onay matrisi,
  araştırma eşikleri, açık kaynak kuralları, matter klasörleri. Kullanıcı
  "şunu değiştir", "profilimi güncelle", "ayarı değiştir" ya da "customize"
  dediğinde kullan.
argument-hint: "[bölüm adı ya da değiştirmek istediğiniz şey]"
---

# /customize

## Ne yapar

1. **Profili oku:** `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` ve ortak `~/.claude/plugins/config/claude-for-legal/firm-profile.md`. Eklenti profili yoksa ya da `[PLACEHOLDER]` içeriyorsa: "Kurulum henüz yapılmamış. Önce `/arthurlegal:ip-legal-cold-start-interview` çalıştırın — customize var olan profili ayarlamak içindir."

2. **Haritayı göster** — her grup için güncel değerin tek satırlık özeti:
   - **Şirket / kimlik** — ad, sektör, ülkeler, pratik ortamı *(ortak profil — tüm eklentilere yansır)*
   - **IP practice profile** — kapsamdaki alanlar (patent, marka, telif, ticari sır, açık kaynak, tasarım) ve alt odak; `Registered in:`; `Outside counsel roster` (dış avukat, marka/patent vekili, yabancı muhabir)
   - **Risk iştahı** — temkinli / orta / atak; araştırma eşiklerine, FTO değerlendirmesine ve ihtarname eskalasyonuna etkisi
   - **Kişiler** — fikri mülkiyet sorumlusu, alan bazında dış büro ve vekiller, uygulama eskalasyon zinciri, buluş değerlendirme kurulu
   - **Portföy** — patent aileleri, marka sınıfları, ana markalar, tescil ülkeleri; `portfolio.yaml` ve yenileme uyarı kanalı (`Renewal alerts`)
   - **Brand protection** — izlenen markalar, izleme kaynakları (TÜRKPATENT Bülteni elle/vekil, izleme hizmeti), sıklık; pazaryeri ve alan adı tutumu
   - **Enforcement posture** — `Default posture:`, ne zaman yumuşak mektup / ihtarname / dava; `Approval matrix` satırları (`DMCA takedown (ordinary)`, `Soft letter`, `Cease-and-desist`, `Filing suit`), `Automatic escalations`
   - **Araştırma ve FTO** — arama kaynakları, güven eşikleri, FTO notu biçimi
   - **OSS review** — kabul / inceleme / yasak lisans katmanları, gönderimi durduran lisanslar, yeni bağımlılık inceleme sıklığı, `OSS policy` yolu
   - **İş akışı** — matter klasörleri, portföy kaydı, buluş bildirim formu
   - **Entegrasyonlar** — ArthurLegal MCP, IP yönetim sistemi, belge deposu, Slack; TÜRKPATENT (her zaman manuel)

3. **Sor:** "Neyi ayarlamak istersiniz? Bir bölüm seçin ya da değişikliği kendi sözlerinizle anlatın."

4. **Değiştir:** güncel değeri göster, yenisini al, aşağı akış etkisini söyle, onay al, yaz. Örnekler:
   - *İzlemeye yeni bir sınıf:* "`/arthurlegal:ip-legal-portfolio` izleme raporlarına bu sınıfı ekler; `/arthurlegal:ip-legal-infringement-triage` bu sınıftaki bulguları buna göre yönlendirir."
   - *Duruş atak → ölçülü:* "`/arthurlegal:ip-legal-cease-desist` belirsiz vakalarda ilk seçenek olarak yumuşak mektup taslağı sunar, doğrudan ihtarnameye gitmez."
   - *Yeni yasak açık kaynak lisansı:* "`/arthurlegal:ip-legal-oss-review` bu lisansı içeren incelemeyi uyarı değil, gönderimi durduran bulgu olarak verir."
   - *İzleme sıklığı aylıktan üç aylığa:* "Bülten yayımına itiraz süresi yayımdan itibaren iki aydır (SMK m. 18/1); üç aylık izleme itiraz penceresini kaçırabilir. Yine de değiştireyim mi?"

   Kullanıcı yeni bir kanun maddesi, süre ya da eşik söylerse yazmadan önce `tr_mevzuat_madde_getir` ile doğrula; çelişki varsa göster ve hangisinin gireceğini sor. TÜRKPATENT ücretleri ve harçlar gibi dönemsel tutarları sabit yazma.

5. **Ortak profil değişikliği** (ad, sektör, ülkeler, pratik ortamı): `firm-profile.md` dosyasına yaz ve söyle: "Bu değişiklik tüm eklentileri etkiler — yargı çevresi ayak izinizi okuyan her eklenti artık [yeni değer]'i görür." Pratik ortamı büro ↔ şirket içi değişiyorsa `## Matter workspaces` → `Enabled` değerinin ve `## Çıkar çatışması` notunun da değişmesi gerektiğini hatırlat.

6. **Kapat:** "Tamam, bir sonraki çıktı değişikliği yansıtır. Başka bir şey var mı? `/arthurlegal:ip-legal-customize`'ı istediğiniz zaman çalıştırabilirsiniz."

## Korkuluklar

- **Bölüm silme.** Bir alan kapsamdan çıkarılmak istenirse `[Not currently in scope]` yaz ve neyin devre dışı kaldığını anlat.
- **İç tutarsızlığı işaretle** — ör. marka kapsam dışı ama marka izleme hizmeti tanımlı; atak duruş ama "her ihtarname dış avukata"; rol "marka/patent vekili" ama çıktı başlığı Av.K. m. 36 kapsamı diyor. Gerilimi göster, hangisini istediğini sor.
- **Korkuluk zayıflatmayı işaretle.** `[review]` bayrağı, kaynak etiketleri, doğrulanmamış atıflardaki `[doğrula]` etiketi ve UYARI satırı, `/arthurlegal:ip-legal-clearance` güven derecesi yük taşır; kapatılmak istenirse neyi koruduğunu anlat ve bedeli anladığını teyit ettir.
- **Bölüm ve anahtar adlarını çevirme** — diğer skill'ler `## Enforcement posture`, `Approval matrix`, `## IP practice profile`, `Registered in:` gibi adları birebir okur.
- **Tek seferde tek değişiklik** — görüşmeyi baştan sorma.
