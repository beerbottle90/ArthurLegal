---
name: employment-legal-wage-hour-qa
description: >
  Ücret, çalışma süresi ve iş hukuku soru-cevabı (Türk hukuku) — ücretin
  ödenmesi, asgari ücret, fazla çalışma ve fazla sürelerle çalışma, ara
  dinlenmesi, gece çalışması, hafta tatili, genel tatil, yıllık izin,
  zamanaşımı ve alacak hesabı; kontrol eden kural canlı çekilip atıfla verilir,
  ezberden söylenmez. "Fazla mesai ödemek zorunda mıyız", "kural ne", "izin kaç
  gün", "alacağı hesapla" ya da herhangi bir iş hukuku sorusunda kullan.
argument-hint: "[soru]"
---

# /wage-hour-qa — Ücret ve Çalışma Süresi Soru-Cevap

"Duruma göre değişir" doğru ama işe yaramaz. Bu skill soruya, kontrol eden maddeyi canlı çekip atıfla cevap verir ve sorunun insan muhakemesi gerektirecek kadar sınırda olduğunu açıkça söyler. Tutarlar (asgari ücret, kıdem tavanı, faiz oranları) dönemsel değişir; hiçbiri sabit yazılmaz.

## Bağlamı yükle

`firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → yargı çevresi ayak izi, [Müvekkil] tarafı (işveren/işçi), TİS bilgisi.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:employment-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Hangi hukuk, hangi rejim?

- İş nerede yapılıyor? Türkiye dışındaysa uygulanacak hukuk MÖHUK 5718 m. 27 (hukuk seçimi + mutad işyeri emredici asgari koruması).
- İşçi 4857 kapsamında mı? m. 4 istisnaları (ör. ev hizmetleri, 50 ve daha az işçili tarım işyerleri, sporcular) → TBK hizmet sözleşmesi hükümleri. Basın ve deniz iş ilişkileri ayrı kanunlara tabidir — ilgili kanunu `tr_mevzuat_ara` ile bul.
- TİS var mı? TİS ve iş sözleşmesi kanuni asgarileri işçi lehine artırabilir.

### 2. Kuralı çek, sonra söyle

Önce `tr_mevzuat_madde_getir` ile maddeyi çek, sonra tek paragrafta atıfla söyle. Sık soruların çıpaları (4857 s.K.):

| Konu | Çıpa | Kural özeti (metinden doğrula) |
|---|---|---|
| Ücretin ödenmesi | m. 32 | Türk parası, işyerinde ya da bankada; en geç ayda bir; sona ermede tam ödeme (m. 32/6); ücret alacağında zamanaşımı 5 yıl (m. 32/8) |
| Gecikme | m. 34 | Ödeme gününden itibaren 20 gün içinde ödenmezse işçi çalışmaktan kaçınabilir; gününde ödenmeyen ücrete mevduata uygulanan en yüksek faiz |
| Ücretin saklı kısmı | m. 35 | Aylık ücretin dörtte birinden fazlası haczedilemez/devredilemez (nafaka saklı) |
| Ücret hesap pusulası | m. 37 | Her ödemede ekler ve kesintiler ayrı ayrı gösterilir |
| Ücret kesme cezası | m. 38 | Yalnız TİS/iş sözleşmesinde gösterilen sebeplerle; ayda 2 gündeliği aşamaz; derhal sebebiyle bildirilir |
| Asgari ücret | m. 39 | Komisyonca en geç iki yılda bir belirlenir, RG'de yayımlanır → güncel tutarı teyit et (`tr_resmi_gazete_tara`) |
| Haftalık çalışma süresi | m. 63 | En çok 45 saat; anlaşmayla günde 11 saati aşmadan farklı dağıtım; denkleştirme 2 ay (TİS ile 4 aya kadar; turizmde ayrı) |
| Fazla çalışma | m. 41 | 45 saati aşan çalışma → saat ücreti %50 zamlı; sözleşmeyle 45'in altında süre varsa fazla sürelerle çalışma → %25 zamlı; işçi isterse 1 s 30 dk / 1 s 15 dk serbest zaman (6 ay içinde); işçinin onayı gerekir; yılda en çok 270 saat |
| Ara dinlenmesi | m. 68 | 4 saate kadar 15 dk; 4–7,5 saat 30 dk; 7,5 saat üstü 1 saat; çalışma süresinden sayılmaz |
| Gece çalışması | m. 69 | 7,5 saati geçemez (sayılı sektörlerde yazılı onayla istisna); gece çalışmasında fazla çalışma yapılamaz (m. 41/6) |
| Çalışma süresinden sayılanlar | m. 66 | Hazır bekleme, görevle başka yere gönderilme, süt izni vb. |
| Hafta tatili | m. 46 | 7 günlük dilimde kesintisiz en az 24 saat; çalışılmayan hafta tatili günü ücreti tam ödenir |
| Genel tatil | m. 47 | Çalışılmazsa o günün ücreti tam; çalışılırsa ayrıca bir günlük ücret |
| Yıllık izin | m. 53–60 | 1–5 yıl (5 dahil) en az 14 gün; 5 yıldan fazla 15 yıldan az en az 20 gün; 15 yıl (dahil) ve fazlası en az 26 gün; 18 yaş ve altı ile 50 yaş ve üstü en az 20 gün; vazgeçilemez; bölünmesi tarafların anlaşmasıyla, bir bölüm en az 10 gün (m. 56); izin ücreti izinden önce peşin (m. 57); sona ermede kullanılmayan izin son ücretle ödenir (m. 59) |
| Zamanaşımı | m. 32/8; ek m. 3 | Ücret 5 yıl; yıllık izin ücreti, kıdem, ihbar, kötüniyet ve eşit davranmama tazminatı 5 yıl; izin ücretinde zamanaşımı sözleşmenin sona ermesinden başlar (m. 59/1) |

ABD'deki "muaf (exempt) çalışan" testinin (maaş eşiği + görev testi) Türk hukukunda karşılığı yoktur. Benzer sorular Türkiye'de şöyle sorulur — hepsi **tartışmalı / yerleşik uygulamaya bağlı, içtihadı kontrol et**:
- "Fazla çalışma ücrete dahildir" klozu geçerli mi, hangi sınırla? (yıllık 270 saat sınırıyla bağlantı kurulması yerleşik uygulamadır)
- Kendi çalışma saatini belirleyen üst düzey yönetici fazla çalışma isteyebilir mi?
- İmzalı bordroda tahakkuk görünen aylar için daha fazlası nasıl ispatlanır?

### 2a. Alacak hesabı iskeleti (fazla çalışma ve benzeri)

Çıplak "ücret × saat" hesabı yapma. Önce varsayımları yaz, eksik girdi varsa **hesaplamadan önce sor**: ücretin brüt/net olduğu, prim ve ek ödemelerin niteliği, puantaj ya da tanık dayanağı, bordroda tahakkuk ve ödeme görünen aylar, izin/rapor haftaları, arabuluculuk başvuru tarihi.

```
Saat ücreti               = aylık brüt ücret ÷ 225            [yerleşik uygulama — teyit et]
Fazla çalışma saat ücreti = saat ücreti × 1,5                 [m. 41/2]
Fazla sürelerle çalışma   = saat ücreti × 1,25                [m. 41/3]
Haftalık fazla saat       = fiilî çalışma − ara dinlenmeleri (m. 68) − 45
Alacak                    = Σ haftalık fazla saat × fazla çalışma saat ücreti
                            − bordroda tahakkuk edip ödenen tutar (mahsup)
Hafta tatili / genel tatil çalışması: ayrı kalem (m. 46, m. 47)
Dönem                     = başvuru tarihinden geriye 5 yıl (m. 32/8); arabuluculuk süresince zamanaşımı durur (7036 m. 3/17)
Faiz                      = ücret alacağında mevduata uygulanan en yüksek faiz (m. 34); kalem bazında faiz türü tartışmalı — içtihadı kontrol et
```

- Formülü ve girdileri her zaman yaz; formülsüz rakam avukatın işine yaramaz.
- Tanık beyanına dayanan fazla çalışmada mahkemelerin hakkaniyet indirimi uyguladığı yerleşik uygulamadır — oran ezberden verilmez.
- Rakamın yanına: `[doğrula — iş hukuku uzmanı kontrolünden geçmeden iddia edilmez/ödenmez]`.
- Arabuluculuk dava şartıdır (7036 m. 3/1); hesap başvurudan önce bitmeli (profil: sonradan ek alacak riski).

### 3. Bayrak

- **Açık:** "m. 41'e göre 45 saati aşan her saat %50 zamlı ödenir."
- **Sınırda:** "Kloz yerleşik uygulamaya göre tartışmalı; risk şu — formal görüş önerilir."
- **Değişmiş/değişen mevzuat:** madde metnindeki değişiklik notunu oku (ör. 2026 değişiklikleri) ve yürürlük tarihini yaz.
- **Teyit edilemedi:** "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/" — tahmin etme.

### 4. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="4857", madde_no=["41","63","68","69"])
tr_mevzuat_madde_getir(number="4857", madde_no=["32","34","ek 3"])
tr_resmi_gazete_tara(query="Asgari Ücret Tespit Komisyonu Kararı")
tr_ictihat_ara(courts=["YARGITAYKARARI"], chamber="H9", query="fazla çalışma ücretin içinde 270 saat", date_from="2022-01-01")
tr_ictihat_semantik_ara(initial_keyword="imzalı bordro fazla mesai", query="imzalı bordroda fazla çalışma tahakkuku varsa ispat")
```

Sonuç azsa sessizce doldurma: "[araç] [N] sonuç döndü; kapsam ince. Seçenekler: (1) sorguyu genişlet, (2) başka araç, (3) web — `[web — doğrula]` etiketiyle, (4) doğrulanmamış diye işaretle ve dur." Etiketler: `[ArthurLegal TR — 4857 m. X — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`; etiketleri silme.

Yabancı yargı çevresi: kural ezberden verilmez. AB çalışma süresi: `eu_search_eu_law(query="organisation of working time")`; Azerbaycan: `az_search_acts(query="Əmək Məcəlləsi", types=[107])`; İngiltere: `uk_search_legislation(query="Working Time Regulations")`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

## Çıktı

Sohbet biçiminde; not değil.

```
**[Hukuk / rejim]:** [Kural, tek paragraf, madde atfı ve güncellik notu.]

[Sınırda ya da değişen mevzuat varsa: bayrak.]

[Ayak izindeki başka bir ülkede ya da TİS'te fark varsa: tek satır, farkın önemli olup olmadığı.]
```

> **Atıfları doğrula.** Yukarıdaki madde ve karar atıfları yapay zekâ desteğiyle üretildi. Dilekçe ya da resmî görüşte kullanmadan önce mevzuat.gov.tr, UYAP Emsal ya da büro araştırma aracıyla doğruluk ve güncelliği kontrol et.

Profilin `## Outputs` bölümündeki sonraki adımlar karar ağacıyla bitir; dalları cevaba göre uyarla.

## Bu skill ne yapmaz

- Kuralı ezberden söylemez; her cevap çekilen maddeye dayanır.
- Sınırdaki sınıflandırma ya da kloz geçerliliği kararını vermez; kuralı söyler, sınırı işaretler.
- İstenmedikçe çok ülkeli tarama yapmaz.
- Tutar değişikliklerini takip etmez; cevap eskiyebilir, güncel için yeniden sor.
- İşçi/serbest çalışan ayrımında → `/arthurlegal:employment-legal-worker-classification`.

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
| Azerbaycan'da istihdam edilen personel — Emek Mecellesi, akt + statu | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
