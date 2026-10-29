---
name: employment-legal-policy-drafting
description: >
  İşyeri politikası / personel yönetmeliği bölümü taslağı (Türk hukuku) —
  çekirdek politika + gerektiğinde ülke, işyeri ya da TİS ekleri; dayanak
  maddeler (İş K., TBK m. 399 ve 417, 6331 İSG, KVKK aydınlatma) canlı çekilir,
  m. 22 esaslı değişiklik riski işaretlenir. "[konu] politikası hazırla",
  "şuna dair bir politikamız olmalı", "[konu] politikasını güncelle" denince ya
  da bir politika boşluğu adlandırıldığında kullan.
argument-hint: "[politika konusu — ör. 'uzaktan çalışma', 'taciz ve mobbing', 'yıllık izin']"
---

# /policy-drafting — Politika Taslağı

Türkiye için doğru olan bir politika, ayak izindeki başka bir ülke ya da TİS'li bir işyeri için eksik kalabilir. Bu skill tek bir çekirdek politika yazar; yalnız kuralın farklılaştığı yerde ek üretir. Personel yönetmeliği iş sözleşmesinin eki sayılabildiğinden (4857 m. 22/1) yazılan her cümle bir sözdür.

## Bağlamı yükle

`firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → ayak izi (ülkeler, işyerleri, TİS'ler), el kitabı/personel yönetmeliği yeri ve biçimi.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:employment-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Kapsam

- Politika ne için? Neden şimdi (kanuni zorunluluk, olay, büyüme, fark edilen boşluk)?
- Kime uygulanır (tüm çalışanlar, belirli işyerleri, alt işveren/geçici işçiler)?
- Yeni bir hak mı tanıyor, mevcut bir hakkı mı daraltıyor? Daraltma → Adım 5'teki m. 22 kontrolü zorunlu.

### 2. Mevzuat taraması

Konunun çıpa maddelerini `tr_mevzuat_madde_getir` ile çek; aşağıdaki tablo başlangıçtır:

| Konu | Çıpa (metinden doğrula) |
|---|---|
| Genel düzenleme yetkisi | TBK m. 399 — işveren işin görülmesi ve işyerindeki davranışlarla ilgili genel düzenleme ve özel talimat verebilir; işçi dürüstlük kurallarının gerektirdiği ölçüde uyar |
| Taciz, mobbing, kişiliğin korunması | TBK m. 417 — psikolojik ve cinsel tacizi önleme ve mağdurun daha fazla zarar görmemesi için önlem; 4857 m. 24/II-b, d (işçinin haklı fesih hâlleri), m. 25/II-c (işverenin haklı fesih hâli) |
| İş sağlığı ve güvenliği | 6331 m. 4 (işverenin genel yükümlülüğü, risk değerlendirmesi), m. 16 (bilgilendirme), m. 17 (eğitim), m. 19 (çalışanın yükümlülükleri) |
| Kişisel veri, izleme (e-posta, kamera, cihaz) | 6698 m. 4 (ölçülülük), m. 5–6 (hukuki sebep, özel nitelikli veri), m. 10 (aydınlatma) |
| Çalışma süresi, fazla çalışma | 4857 m. 41, m. 63, m. 68, m. 69 |
| Yıllık izin | 4857 m. 53–60 (bölünme m. 56; izin kayıt belgesi m. 56) |
| Analık, ebeveynlik, mazeret izni | 4857 m. 74, m. 13/5, ek m. 2 |
| Uzaktan çalışma | 4857 m. 14 (yazılı sözleşme, zorunlu içerik, İSG bilgilendirmesi) + Bakanlık yönetmeliği |
| Disiplin, ücret kesme cezası | 4857 m. 38 (yalnız TİS/iş sözleşmesindeki sebepler; ayda 2 gündelik sınırı), m. 19 (savunma), m. 25 |
| Eşit davranma | 4857 m. 5; 6701 m. 3, m. 6 |

Konunun mevzuatta özel karşılığı yoksa (ör. kıyafet kuralı) yalnız TBK m. 399 ölçülülük ve KVKK boyutunu kontrol et, bu adımı kısa geç.

Ayak izinde Türkiye dışı ülke varsa her biri için ayrı ek gerekip gerekmediğine bak; kural ezberden yazılmaz: AB `eu_search_eu_law(query="work-life balance for parents and carers")`, İngiltere `uk_search_legislation`, Almanya `de_gesetz_ara`, Hollanda `nl_search_legislation`, Azerbaycan `az_search_acts(query="Əmək Məcəlləsi", types=[107])`. Listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al."

### 3. Çekirdek politikayı yaz

Tek politika, her yerde geçerli; çalışan avukatsız anlayabilmeli. Yapı:
- **Amaç** (tek cümle)
- **Kapsam** (kime)
- **Kural** (ne zorunlu / serbest / yasak)
- **Süreç** (nasıl talep edilir, kim onaylar, ihlalde ne olur — disiplin yaptırımı varsa m. 38 ve savunma hakkı)
- **Kişisel veri** (politika veri işliyorsa aydınlatma metnine atıf)
- **Sorular** (kime sorulur)

Kaçın: "işbu", "mezkûr", iç içe istisnalar. Bu bir personel politikasıdır, sözleşme metni değil.

### 4. Ekler (yalnız farklılık varsa)

```markdown
### [Ülke / işyeri / TİS] Eki

[Ülke/işyeri/TİS kapsamındaki] çalışanlara çekirdek politikaya ek olarak / yerine şunlar uygulanır:
- [Somut fark]
- [Dayanak — yalnız araçla doğrulanmışsa]
```

Ekler kısa: yalnız farklı olan; çekirdeği tekrar etme. TİS'li işyerinde politikanın TİS hükümleriyle çatışıp çatışmadığını ayrıca kontrol et.

### 5. Çapraz kontrol

- **Esaslı değişiklik (4857 m. 22):** politika mevcut çalışma koşullarını (iş sözleşmesi, personel yönetmeliği, işyeri uygulaması) işçi aleyhine esaslı biçimde değiştiriyor mu? Öyleyse yazılı bildirim ve işçinin 6 iş günü içinde yazılı kabulü gerekir; kabul etmeyeni bağlamaz; değişiklik geçmişe etkili olamaz (m. 22/2). Neyin "esaslı" olduğu **tartışmalı — içtihadı kontrol et**.
- **Söz kontrolü:** şirketin vermek istemediği bir hakkı vaat ediyor mu? İşyeri uygulamasına dönüşebilecek tekrar eden ödemeler/izinler var mı?
- **Mevcut el kitabıyla çatışma:** aynı konuyu düzenleyen başka bölüm var mı?
- **KVKK:** yeni bir veri işleme getiriyorsa aydınlatma metni güncellenmeli (6698 m. 10).
- **İSG:** risk değerlendirmesini değiştiriyorsa bilgilendirme ve eğitim (6331 m. 16, m. 17).

### 6. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6098", madde_no=["399","417"])
tr_mevzuat_madde_getir(number="4857", madde_no=["22","38"])
tr_mevzuat_madde_getir(number="6331", madde_no=["4","16","17","19"])
tr_kurum_karari_ara(kurum="kvkk", query="çalışan e-posta kamera izleme")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="personel yönetmeliği esaslı değişiklik işçi aleyhine", date_from="2022-01-01")
```

Sonuç azsa sessizce doldurma; seçenekleri sun. Atıf etiketleri: `[ArthurLegal TR — 4857 m. 22 — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`.

## Çıktı

```markdown
# [Politika Adı]

## Çekirdek Politika
[Tam metin]

## Ekler
### [Ülke / işyeri / TİS 1]
[Ek]

---

## Taslak notları (dahili — yönetmeliğe eklemeden önce çıkar)
- **Mevzuat taraması:** [çekilen maddeler; farklılık çıkan ülke/işyeri/TİS]
- **m. 22 değerlendirmesi:** [aleyhe esaslı değişiklik yok / var — yazılı kabul süreci]
- **Mevcut el kitabıyla çatışma:** [yok / liste]
- **KVKK / İSG etkisi:** [aydınlatma, bilgilendirme, eğitim]
- **Değişen mevzuat:** [madde notlarında görülen yakın değişiklikler]
- **Tartışmalı noktalar:** [liste]
- **Gözden geçirme sıklığı:** [yıllık / X olunca]
```

> **Taslak, yürürlükteki politika değil.** Bu metin avukat incelemesi için bir yardımcıdır. Personel politikası yayımlamak hukuki sonuç doğurur: iş sözleşmesinin eki sayılabilir, aleyhe değişiklikler m. 22'ye tabidir, ücret/izin/disiplin hükümleri işveren aleyhine yorumlanabilir. Yetkili bir avukat inceleyip sorumluluğu üstlenmeden yayımlama ve dağıtma.

## Devir

Politika onaylanınca `/arthurlegal:employment-legal-handbook-updates` mevcut el kitabıyla karşılaştırır ve değişiklikleri işaretler.

## Bu skill ne yapmaz

- Politikayı onaylamaz; taslak yazar, insan onaylar.
- Çalışanlara duyurmaz; bu İK süreci (yazılı tebliğ ve gerekiyorsa kabul imzası İK'da).
- Ayak izi dışındaki ülkeleri kapsamaz; ayak izi genişlerse yeniden çalıştır.

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
