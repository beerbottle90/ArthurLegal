---
name: commercial-legal-review
description: >
  Gelen ticari sözleşmeyi (hizmet/tedarikçi sözleşmesi, gizlilik sözleşmesi,
  SaaS/abonelik) playbook'a göre inceler. Önce belge yapısını başlıklardan
  okur, doğru inceleme skill'ine (vendor-agreement-review, nda-review,
  saas-msa-review) yönlendirir, tarafların tacir olup olmadığını ve seçilen
  hukuku tarar, çıktıyı tek notta birleştirir. "Bu sözleşmeyi incele",
  "çerçeve sözleşmeye bak", "bu NDA uygun mu", "SaaS sözleşmesini kontrol et"
  denince ya da gelen bir sözleşme eklendiğinde kullan.
argument-hint: '[dosya yolu | Drive bağlantısı | [CLM ID] | metni yapıştırın]'
---

# /review — Sözleşme İncelemesi (yönlendirici)

Gelen sözleşmeyi `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`'deki playbook'a göre inceler. Hangi skill'in çalışacağına belge başlıklarından karar verir; `confirm_routing` açıksa önce kullanıcıya teyit ettirir. Esas Türk hukukudur; yabancı hukuk ya da yabancı yargı yeri seçilmişse tespitler o hukuka taşınmaz, `/arthurlegal:commercial-legal-governing-law-review`e yönlendirilir.

## Adımlar

1. **Eklenti ayarını ve `firm-profile.md`'i yükle.** Yer tutucu varsa dur: "Önce `/arthurlegal:commercial-legal-cold-start-interview` çalıştırın — playbook'unuzu öğrenmeden ona göre inceleyemem." `## Review preferences` → `confirm_routing` oku; alan yoksa `true` say.

2. **Sözleşmeyi al:** dosya, Drive bağlantısı, [CLM ID] ya da yapıştırılmış metin. Yoksa iste.

3. **Önce başlıkları oku.** Gövdeye geçmeden çıkar: ana sözleşmenin başlığı; tüm ek, ek protokol, sipariş formu, teknik şartname, iş emri başlıkları. Yönlendirme sinyali budur — 40 sayfalık çerçeve sözleşmede "gizli" kelimesinin sık geçmesi onu NDA yapmaz.

4. **Skill'i belge yapısına göre seç.**

   | Başlıkta geçen | Skill |
   |---|---|
   | Gizlilik Sözleşmesi, Gizlilik Taahhütnamesi, NDA, Confidentiality Agreement (*ana* sözleşme olarak) | **nda-review** |
   | Hizmet Sözleşmesi, Çerçeve Sözleşme, Master Services Agreement, Danışmanlık, Proje Sözleşmesi, İş Emri / Statement of Work, Satın Alma Sözleşmesi | **vendor-agreement-review** |
   | Abonelik, SaaS, Bulut Hizmeti, Kullanım Koşulları, otomatik yenilemeli Sipariş Formu, yinelenen bedelli Yazılım Lisansı | **saas-msa-review** (vendor-agreement-review'un üstüne katman) |
   | Kişisel Verilerin İşlenmesine İlişkin Ek Protokol, Veri İşleme Sözleşmesi, DPA (ek ya da ayrı) | vendor-agreement-review'da veri koruma başlığında işaretle + `/arthurlegal:privacy-legal-dpa-review` öner |
   | Hizmet Seviyesi Sözleşmesi (HSS), SLA (ek olarak) | saas-msa-review → HSS bölümü |
   | NDA ama bağlam işçi, yatırım ya da şirket alımı | Bu eklentinin işi değil → `/arthurlegal:employment-legal-hiring-review` ya da `/corporate-legal:` skill'leri; avukata |

   Birden çok skill uygulanabilir: çerçeve sözleşme + KVKK eki → vendor-agreement-review (veri eki işaretli); abonelik + sipariş formu + HSS eki → saas-msa-review (üçünü kapsar); çerçeve sözleşme + otomatik yenilemeli sipariş formu → vendor-agreement-review + saas-msa-review katmanı. Başlıklar yetmiyorsa (yalnız "Sözleşme", ek listesi yok) gövdenin ilk iki sayfasını oku, karar ver, dur.

5. **Ön tarama (yönlendirmeyle birlikte, her sözleşmede):**
   - **Taraflar tacir mi?** Bir ticari işletmeyi ilgilendiren işlem ticari iştir (TTK m. 3); her iki tarafın ticari işletmesiyle ilgili uyuşmazlık ticari davadır (TTK m. 4/1). Sonuçları: fesih ve temerrüt bildirimlerinin şekli (TTK m. 18/3), cezai şartın indirilememesi (TTK m. 22), para alacaklarında dava şartı arabuluculuk (TTK m. 5/A). İnceleme skill'leri bunları kullanır; tacir sıfatını notun başına yaz.
   - **Karşı taraf tüketici mi?** Ticari veya mesleki olmayan amaçla hareket eden kişi tüketicidir (6502 m. 3/1-k). O zaman playbook yetmez: haksız şartlar kesin hükümsüzdür (6502 m. 5/2), abonelikte otomatik uzatma ve fesih kuralları emredicidir (6502 m. 52/3-4) → avukata, ayrıca işaretle.
   - **Uygulanacak hukuk ve uyuşmazlık çözümü.** Türk hukuku dışında bir hukuk, yabancı mahkeme ya da yurt dışında tahkim seçilmişse ya da yetki kaydı tek tarafa seçim hakkı veriyorsa → hukuk seçimi MÖHUK m. 24/1'e tabidir; yabancılık unsuru olmayan saf iç sözleşmede yabancı hukuk seçiminin geçerliliği **tartışmalı — içtihadı kontrol et**. Bu incelemenin Türk hukuku tespitlerinin o hukuka geçmediğini nota yaz ve `/arthurlegal:commercial-legal-governing-law-review` öner.

6. **Yönlendirmeyi teyit et** (`confirm_routing: true` ya da alan yoksa):

   ```
   Bunu şöyle inceleyeceğim: [sözleşme türü/türleri]. Taraflar: [tacir–tacir / tüketici var].

   Tespit edilen belgeler:
   - [Ana sözleşme başlığı] → [skill]
   - [Ek 1 başlığı] → [nasıl ele alınacak]
   - [Ek 2 başlığı] → [nasıl ele alınacak]

   Doğru mu? (evet / hayır — ya da neyi yanlış anladığımı söyleyin)
   ```

   Teyit bekle; kullanıcı düzeltirse onun talimatıyla devam et. `confirm_routing: false` ise sessizce devam et, yönlendirme kararını notun en üstüne yaz.

7. **Skill(ler)i çalıştır.** Her birinin akışını eksiksiz izle. Birden çok skill varsa sırayla çalıştır ve **tek not** üret; ayrı notlar çıkarma.

8. **Eskalasyon:** Bir bulgu inceleyenin yetkisini aşıyorsa (`## Escalation` matrisi) `/arthurlegal:commercial-legal-escalation-flagger` ile yönlendir ve talebi taslakla.

9. **Takip öner:**
   - İş birimine özet → `/arthurlegal:commercial-legal-stakeholder-summary`
   - İzlenen değişikliklerle redline .docx
   - [CLM] kaydı (bağlıysa)
   - Otomatik yenileme bulunduysa yenileme kaydı → `/arthurlegal:commercial-legal-renewal-tracker`
   - Yabancı hukuk, yabancı yargı yeri ya da asimetrik yetki/tahkim → `/arthurlegal:commercial-legal-governing-law-review` (yabancı kural araçla çekilir: İngiltere `uk_search_legislation`, Almanya `de_gesetz_ara`, AB `eu_search_eu_law`; listede olmayan ülke için "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al")
   - Damga vergisi sorusu → `/tax-legal` skill'leri (oran ve tutar bu eklentide yazılmaz)

## confirm_routing ayarı

`~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → `## Review preferences`:

```markdown
## Review preferences

confirm_routing: true   # Set to false to skip routing confirmation and proceed automatically
```

Cold-start görüşmesi bu tercihi sorar. Varsayılan `true`; güven oluştukça kullanıcı `false` yapabilir.

## ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="6102", madde_no=["3","4","5/A","18","22"])
tr_mevzuat_madde_getir(number="6502", madde_no=["3","5","52"])
```

Atıf etiketi: `[ArthurLegal TR — 6102 m. X — GG.AA.YYYY]`; ezberden gelen için `[model bilgisi — doğrula]`; kullanıcıdan gelen için `[kullanıcı verdi]`. Çekilemeyen madde: "UYARI: veri çekilemedi, teyidiniz gerekli: https://www.mevzuat.gov.tr/".

## Örnekler

```
/arthurlegal:commercial-legal-review hizmet-cerceve-sozlesmesi.pdf
/arthurlegal:commercial-legal-review https://drive.google.com/file/d/ABC123
/arthurlegal:commercial-legal-review
[sözleşme metnini yapıştırın]
```

## Çıktı

İlgili skill'in biçiminde tam inceleme notu. En üstte: yönlendirme kararı, uygulanan playbook tarafı (satış / alım), taraf sıfatı (tacir / tüketici), seçilen hukuk. Sapma sapma bulgu, somut redline metni, adıyla onaylayıcı. Not, `## House style` → iş ürününün gideceği yere kaydedilir.

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
| governing law = Azerbaycan hukuku ise akt lafzi + **yururluk statusu** (`Quvvededir`/`Legv olunmus`) — statusuz akt dayanak yapilmaz | `/arthurlegal:legal-research-az-mevzuat` |
| kloz benchmark — bir sartin piyasa/agresif/muhafazakar oldugunu imzali emsallerle olc (tahkim, uygulanacak hukuk, sorumluluk tavani) | `/arthurlegal:legal-research-sozlesme-emsali` |
| sinir-otesi kavramlarda (mucbir sebep, uyarlama, stabilizasyon) karsilastirmali ogreti — **ikincil**, redline gerekcesi olamaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`

---
