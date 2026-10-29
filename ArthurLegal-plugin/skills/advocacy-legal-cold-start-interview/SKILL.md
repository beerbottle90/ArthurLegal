---
name: advocacy-legal-cold-start-interview
description: >
  advocacy-legal eklentisini ilk kez kuran kullanıcı için kısa röportaj —
  kullanıcı rolü ([Baş Hukuk Müşaviri] / [Kıdemli Hukuk Müşaviri] / [Hukuk Müşaviri] / diğer), dilekçe
  üretim tercihleri, onay/eskalasyon, dış vekil dağılımı, varsayılan çıktı modu.
  CLAUDE.md profilini doldurur. `--redo` ile yeniden çalışır.
user-invocable: true
---

# advocacy-legal — Cold Start Interview

Amaç: Bu eklentinin `CLAUDE.md` profilindeki `[DOLDUR]` alanlarını kullanıcıyla 5-8 soruda doldurmak. Önce knowledge'daki `firm-profile.md` ([Şirket/Büro adı]) okunur — şirket bilgisi oradan gelir, burada **tekrar sorulmaz**.

## Akış

### Adım 0 — Bağlamı oku
- `firm-profile.md` ([Şirket/Büro adı]) + bu plugin `CLAUDE.md`'yi oku. Zaten dolu alanları tekrar sorma; yalnızca `[DOLDUR]` olanları sor.

### Adım 1 — Kullanıcı kim?
> 1. Adın ve rolün? (örn. **[Baş Hukuk Müşaviri]** — Baş Hukuk Müşaviri / **[Kıdemli Hukuk Müşaviri]** — Senior Legal Counsel / **[Hukuk Müşaviri]** — Junior Legal Counsel / diğer)
> 2. Baroya kayıtlı avukat mısın, yoksa hukuk müşaviri/legal counsel mı? (vekaletname/imza yetkisi farkı için)
> 3. Doğrudan amirin? (varsayılan: [Baş Hukuk Müşaviri])

### Adım 2 — Dilekçe üretim tercihleri
> 4. Hangi dilekçe tiplerini en çok üretiyorsun? (özel hukuk HMK / idari İYUK / ceza CMK / karma)
> 5. Dilekçe taslakları **dış vekil revizesi öncesi mi** (in-house first-draft) yoksa **doğrudan sunum için mi** üretilecek? (onay zinciri buna göre)
> 6. Varsayılan çıktı: tam dilekçe metni mi, yoksa önce iskelet/argüman haritası mı?

### Adım 3 — Onay ve dış vekil
> 7. Yüksek tutarlı/stratejik dilekçelerde onay eşiği? (tutar veya "her istinaf/temyiz/AYM" gibi)
> 8. Dış vekil paneli (ticari / idari-Danıştay / ceza / tahkim) — büro adları varsa.

### Adım 4 — Yaz ve onayla
- Cevapları `CLAUDE.md`'deki ilgili `[DOLDUR]` alanlarına işle (kullanıcıya özetini göster, onay al, sonra yaz).
- Matter workspace kullanımı (dilekçe dosya-bazlı) açık mı? Varsayılan: açık.

## Çıktı
Kısa özet + güncellenen `CLAUDE.md` alanları listesi + "Artık `/arthurlegal:advocacy-legal-ozel-hukuk-dilekce`, `:kamu-hukuku-dilekce`, `:ceza-dilekce`, `:yazihane-asistani` komutlarını kullanabilirsin." yönlendirmesi.

## Notlar
- `--redo`: tüm alanları yeniden sor.
- Bu eklenti **kurumsal in-house** içindir; kullanıcı serbest avukatlık bağlamı tarif ederse, çıktı başlıklarını ona göre uyarlamayı öner ama varsayılan in-house kalır.

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
| dilekce gerekcesini guclendiren Turk doktrini — DergiPark 19 hukuk dergisi (ceza → Ceza Hukuku ve Kriminoloji, idari → Idare Hukuku ve Ilimleri) — **ikincil**, dilekcede birincil kaynakla birlikte kullan | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| uyusmazlik AZ hukukuna tabiyse akt lafzi + **yururluk statusu** | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
