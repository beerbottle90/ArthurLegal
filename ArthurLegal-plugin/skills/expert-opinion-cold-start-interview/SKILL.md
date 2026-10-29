---
name: expert-opinion-cold-start-interview
description: >
  expert-opinion eklentisini ilk kez kuran kullanıcı için kısa röportaj — rol,
  tipik teknik alanlar (elektrik/şebeke/EPC/su/çevre/İSG/mali), bilirkişi itirazı mı
  uzman görüşü üretimi mi ağırlıklı, dış uzman/akademisyen havuzu, onay zinciri.
  CLAUDE.md profilini doldurur. `--redo` ile yeniden çalışır.
user-invocable: true
---

# expert-opinion — Cold Start Interview

Amaç: Bu eklentinin `CLAUDE.md` profilindeki `[DOLDUR]` alanlarını 5-7 soruda doldurmak. Önce `firm-profile.md` ([Şirket/Büro adı]) okunur.

## Akış

### Adım 0 — Bağlam
`firm-profile.md` + bu plugin `CLAUDE.md` + `${CLAUDE_PLUGIN_ROOT}/references/bilirkisilik-rehberi.md` oku. Dolu alanları tekrar sorma.

### Adım 1 — Kullanıcı
> 1. Adın/rolün? ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri] / teknik birim)
> 2. Avukat mısın, hukuk müşaviri mi, teknik uzman mı? (mütalaa imza/sunum farkı için)

### Adım 2 — Kullanım profili
> 3. Daha çok hangisi: (a) karşı/mahkeme **bilirkişi raporuna itiraz**, (b) şirket lehine **uzman görüşü üretimi**, (c) ikisi de?
> 4. En sık teknik alanlar? (elektrik üretim/şebeke · EPİAŞ/YEKDEM fiyatlama · EPC/inşaat hakediş-gecikme · HES su/debi · çevre/ÇED · iş kazası/İSG kusur · mali/zarar hesabı · bilişim)

### Adım 3 — Dış uzman & onay
> 5. Dış uzman/akademisyen havuzu var mı? (alan + isim/kurum, varsa)
> 6. Mütalaa/itiraz sunum öncesi onay zinciri? (varsayılan: dış uzman + [Baş Hukuk Müşaviri] + dış vekil)
> 7. Hukuki mütalaa (legal opinion) da üretilecek mi, yoksa yalnız teknik mi?

### Adım 4 — Yaz ve onayla
Cevapları `CLAUDE.md` `[DOLDUR]` alanlarına işle (özet göster, onay al, yaz). Matter workspace açık mı? Varsayılan: açık.

## Çıktı
Kısa özet + güncellenen alanlar + "Artık `/arthurlegal:expert-opinion-bilirkisi-raporu` ve `/arthurlegal:expert-opinion-uzman-mutalaasi` kullanabilirsin." yönlendirmesi.

## Not
`--redo`: tüm alanları yeniden sor.

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
> **Meslek sirri (Av. K. m. 36):** uc MCP de PUBLIC arama aracidir — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| mutalaanin akademik dayanagi — Turk ve karsilastirmali ogreti; **hakemlilik uc durumlu** (`true`/`false`/`null`), ABD law review'lari ogrenci editorludur ve hakemli sayilmaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| sozlesmesel bir teknik meselede imzali emsal kloz metni | `/arthurlegal:legal-research-sozlesme-emsali` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
