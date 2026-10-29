---
name: commercial-legal-review-proposals
description: >
  playbook-monitor ajanının bekleyen playbook güncelleme önerilerini tek tek gözden
  geçirir; avukat kabul, ret, düzenleme ya da erteleme seçer ve onaylanan değişiklik
  profile yazılır. playbook-monitor öneri çıkardığında, kullanıcı "playbook önerilerini
  gözden geçir", "bekleyen playbook güncellemeleri ne" dediğinde ya da sapmaya dayalı
  değişiklikleri adım adım görmek istediğinde kullan.
argument-hint: "[argüman gerekmez — bekleyen öneri dosyasından çalışır]"
---

# /review-proposals

`~/.claude/plugins/config/claude-for-legal/commercial-legal/playbook-proposals.md` dosyasındaki önerileri tek tek gösterir ve onaylananları `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` dosyasına uygular.

## Talimat

1. **playbook-monitor ajanının Adım 5'ini (gözden geçirme ve onay akışı) yükle ve çalıştır.**
2. **Öneri dosyası yoksa ya da boşsa:** "Bekleyen öneri yok. Playbook güncel." de ve dur.
3. **Önerileri tek tek göster.** Her biri için tam öneri bloğunu ve dört seçeneği ver: **[K] Kabul**, **[R] Ret**, **[D] Düzenle**, **[E] Ertele**.
4. **Kabul ya da Düzenle:** yazmadan önce profildeki tam farkı göster (`- eski` / `+ yeni`); yalnız avukat açıkça onaylarsa yaz. Yalnız ilgili tarafın (`### Sales-side playbook` / `### Purchasing-side playbook`) ilgili alt bölümünü değiştir; başlık ve anahtar adlarını çevirme.
5. **Ret ya da Ertele:** kararı (varsa gerekçesiyle) `playbook-monitor-log.yaml`'a işle; profili değiştirme. Reddedilen öneri, ret tarihinden sonra yeni bir desen oluşmadıkça yeniden önerilmez.
6. **Hukuki sınır kontrolü:** Önerilen yeni duruş emredici bir hükme takılıyorsa kabulden önce söyle ve maddeyi `tr_mevzuat_madde_getir` ile çekip göster. Örnekler: tavanın kast ve ağır kusuru da kapsaması (önceden yapılan bu anlaşma kesin hükümsüzdür, TBK m. 115/1); borçlu olduğumuz yüksek cezai şartı "kabul edilebilir geri çekilme" yapmak (tacir borçlu aşırılık iddiasıyla indirim isteyemez, TTK m. 22); tüketici aboneliğinde otomatik uzama (6502 m. 52/3). Uygulamada sık kabul edilmiş olması, duruşu hukuken geçerli kılmaz.
7. **Hepsi bitince:** neyin değiştiğinin özetini göster, sonra öneri dosyasını `playbook-proposals-[YYYYMMDD].md` adıyla arşivle.

```
/arthurlegal:commercial-legal-review-proposals
(playbook-monitor bildirim gönderdikten sonra çalıştırın)
```

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
