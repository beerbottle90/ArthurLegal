---
name: litigation-legal-cold-start-interview
description: >
  Litigation pratiğini bilgisayara öğret — dava modeli, dış vekil paneli, eskalasyon
  matriksi, settlement yetkisi, takip sistemi, yakıcı sorun. 2-dakikalık hızlı vs.
  10-dakikalık tam mod. Çıktı: practice profile CLAUDE.md'nin doldurulması.
user-invocable: true
---

# Cold-Start Interview — Litigation Practice

## Amaç

Bu eklentinin diğer tüm skill'leri practice profile'a (`~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`) dayanır. Yeni kurulumda veya pratik değişikliğinde bu skill'i çalıştır — sorulara cevap ver, profil otomatik dolar.

## Modlar

Kullanıcı bir argüman vermezse, sor:

> İki mod:
> - **Hızlı (2 dakika)** — sadece kritik 6 soru. Çoğu alan `[DOLDUR]` kalır; sonra elinle doldurursun.
> - **Tam (10 dakika)** — 20+ soru; tüm profili doldurur. Önerilen.
>
> Hangisini istersin? Veya `--side` (taraf) gibi spesifik argüman var mı? (`--redo` mevcut profili sıfırlar, `--check-integrations` sadece MCP ve sistem bağlantıları kontrol eder.)

## Hızlı mod (6 soru)

1. **Dava modeli:** "Tüm davalar dış vekille mi, içeride ekip mi, karma mı?"
2. **Aktif dava hacmi:** "Yaklaşık kaç aktif dava? 10-50, 50-200, 200+?"
3. **Yakıcı sorun:** "En yakıcı dava kategorisi: İSG/çevre, iş davaları hacim, vendor/ticari, regulator itirazları?"
4. **Birincil venue:** "Çoğu dava nereye gidiyor? (İstanbul/Ankara/İzmir/karma)"
5. **Birincil dış vekil:** "Ana büro(lar) — isim ver veya [DOLDUR]"
6. **Settlement onay matriksi:** "Tutara göre kademeli mi, hep üst yönetim mi, daha gevşek mi?"

Cevaplara göre profil doldurulur. Eksik kalan kısımlar açıkça `[DOLDUR]` etiketli kalır.

## Tam mod (20+ soru, batch'ler halinde)

### Batch 1 — Pratik modeli ve hacim
- Dava modeli (içeri/dış/karma)
- Aktif dava sayısı + tip dağılımı (iş, ticari, İSG, regulator, idari, ceza)
- Birincil yakıcı sorun + ikincil yakıcı sorunlar
- Trend (artıyor/azalıyor/sabit)

### Batch 2 — Outside counsel paneli
- Her pratik alan için birincil + ikincil büro
- Aylık rapor cadence + format
- Brief verme süreci
- Vekalet ücreti modeli (saatlik / başarı / sabit / karma)
- KEP iletişim disiplini

### Batch 3 — Eskalasyon ve onay
- Sulh teklifi yetkisi (tutar kademeleri)
- İstinaf/temyiz başvuru yetkisi
- AYM bireysel başvuru yetkisi
- Ceza dosyası savunma stratejisi onayı
- **Tutardan bağımsız otomatik eskalasyon listesi** ([HALKA AÇIK İŞTİRAK], üst yönetim isim, basın, EPDK lisans riski, yaptırım, vs.)

### Batch 4 — Venue ve teknoloji
- Birincil mahkemeler (davacı/davalı sıfat ayrı)
- Tahkim politikası (ISTAC/ICC/ad hoc)
- UYAP erişimi (kim, nasıl)
- Case management yazılımı (var/yok, hangi)
- iManage / SharePoint / Drive tercihi

### Batch 5 — Halka açık ve özel kontroller
- Halka açık şirket varsa (örn. [HALKA AÇIK İŞTİRAK]) — KAP açıklama disiplini
- Yatırımcı ilişkileri koordinasyonu
- Compliance ekibi ile interaction (MASAK, OFAC vs.)
- Crisis communications protokolü (basın, sosyal medya)

## Çıktı

Profil dolduktan sonra:

1. **CLAUDE.md güncellenir** — `[DOLDUR]` kalanlar açıkça gösterilir
2. **Özet** kullanıcıya gösterilir:

```markdown
## ✓ Practice profile dolduruldu

**Doldurulan:**
- Dava modeli: [özet]
- Hacim: [özet]
- Yakıcı sorun: [özet]
- Outside counsel paneli: [özet]
- Eskalasyon: [özet]
- ...

**Hala [DOLDUR]:**
- [liste]

**Sonraki adım önerisi:**
- /arthurlegal:litigation-legal-case-intake — yeni dosya geldi
- /arthurlegal:litigation-legal-isg-incident-response — İSG/çevre olayı oldu
- Manuel: ~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md
```

## Bağımsız çağırma (--check-integrations)

Sadece şu kontrolleri yap:

1. **ArthurLegal MCP (`tr_`)** — test sorgu: `tr_ictihat_ara(courts=["YARGITAYKARARI"], query="+işe +iade", date_from="2025-01-01")` → cevap geliyor mu?
2. **ArthurLegal MCP (`tr_`)** — test sorgu: `tr_mevzuat_ara(number="6100", types=["KANUN"])` → HMK dönüyor mu?
3. **iManage** (varsa) — bağlantı testi
4. **Slack / Teams** (varsa) — bağlantı testi

Rapor:
```markdown
## Entegrasyon kontrolü

| Entegrasyon | Durum | Not |
|---|---|---|
| ArthurLegal MCP (`tr_`) | ✅ N karar döndü | Aktif |
| ArthurLegal MCP (`tr_`) | ✅ HMK 6100 bulundu | Aktif |
| iManage | ⚠️/❌ | [neden] |
```

## Reviewer note

Profil doldurma çıktısı için:
> ⚠️ İnceleyen notu: Cold-start interview ile dolduruldu. Profil eksik alanlar `[DOLDUR]` etiketli. İlk gerçek skill çağrısı öncesi en azından dış vekil paneli + eskalasyon matriksi doldurulmalı.

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
| Turk doktrini (DergiPark 19 hukuk dergisi) + karsilastirmali ogreti — **ikincil**; bir karar kademesini yukseltmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| uyusmazlik AZ hukukuna tabiyse akt + statu. **AZ ictihadi bu araclarda YOK** — `azerbaycan-hukuk-rehberi.md` | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
