---
name: administrative-legal-cold-start-interview
description: >
  İdari hukuk pratiğini bilgisayara öğret — düzenleyici kurum dialog modeli (EPDK
  proaktif vs defansif), aktif idari dava envanteri (İdare Mah. + BİM + Danıştay
  aşamalarında), birincil yakıcı stres (ÇED/EPDK/Rekabet/KVKK/KİK), outside
  counsel paneli (Ankara odaklı), eskalasyon eşikleri. 2dk hızlı / 10dk tam mod.
user-invocable: true
---

# Cold-Start Interview — Administrative Practice

## Modlar

Argümansız çağrılırsa:

> İki mod:
> - **Hızlı (2 dakika)** — 6 kritik soru
> - **Tam (10 dakika)** — 20+ soru
>
> Hangisi? (`--redo` sıfırlar; `--check-integrations` MCP testi)

## Hızlı mod (6 soru)

1. **Birincil yakıcı stres:** ÇED / EPDK / Rekabet / KVKK / KİK / karma
2. **Düzenleyici kurum dialog:** Proaktif / Defansif / Karma
3. **Aktif idari dava sayısı (üç aşama toplam):**
4. **Birincil dış vekil tipi:** Ankara odaklı uzman / İstanbul büronun Ankara ofisi / Konuya özel / Karma
5. **EPDK ile günlük interface:** Var / Yok / Bazı birim için var
6. **Eskalasyon:** Hangi tutar/konuda otomatik Başkan/CEO eskalasyonu?

## Tam mod (20+ soru, batch'ler)

### Batch 1 — Pratik modeli ve dava envanteri
- Aktif idari dava sayısı (İdare Mah. / BİM / Danıştay aşama dağılımı)
- Pratik alana göre dağılım (ÇED, EPDK, Rekabet, KVKK, KİK, BDDK, SPK, diğer)
- Yıllık yeni dava açma + cevap verme rakamları
- Düzenleyici kurum interface yoğunluğu

### Batch 2 — Outside counsel paneli
- Birincil büro tipi (Ankara/İstanbul + Ankara ofisi/karma)
- Pratik alana göre uzman büro var mı (ÇED için ayrı, EPDK için ayrı, vs.)
- Brief disiplini + aylık rapor
- Vekalet ücreti modeli

### Batch 3 — Eskalasyon ve onay
- Dava açma yetkisi
- İstinaf / temyiz yetkisi
- AYM bireysel başvuru yetkisi
- Yürütmenin durdurulması talep
- EPDK Kurul'a proaktif görüş sunma onayı
- Tutardan bağımsız otomatik eskalasyon listesi

### Batch 4 — Düzenleyici kurum interface
- EPDK proaktif dialog modu (varsa nasıl: toplantı, yazışma, görüş)
- Rekabet Kurumu ile genel ilişki
- Çevre Bakanlığı + il müdürlüğü koordinasyon ([TESİS LOKASYONU] için)
- KVKK Kurumu ile ilişki
- KİK ihale itirazları sıklık
- SPK / BDDK (halka açık iştirak ilgili) ilişki

### Batch 5 — Halka açık ve özel kontroller
- halka açık iştirak ilgili tüm idari konular için KAP koordinasyon
- Yatırımcı ilişkileri ile interface
- Compliance ekibi koordinasyon
- Basın / İletişim Başkanlığı protokolü

## --check-integrations

1. **ArthurLegal MCP (`tr_`)** — test: `tr_ictihat_ara(courts=["DANISTAYKARAR"], chamber="D13", query="+EPDK +lisans")` → cevap geliyor mu?
2. **ArthurLegal MCP (`tr_`)** — test: `tr_mevzuat_ara(number="2577", types=["KANUN"])` → İYUK dönüyor mu?
3. **iManage** + diğerleri

Rapor formatı litigation-legal/tax-legal ile aynı.

## Çıktı

```markdown
## ✓ Administrative practice profile dolduruldu

**Doldurulan:**
- Yakıcı stres: [özet]
- Dava envanteri: [özet]
- Düzenleyici kurum dialog: [özet]
- Outside counsel: [özet]
- Eskalasyon: [özet]

**Hala [DOLDUR]:**
- [liste]

**Sonraki adım önerisi:**
- /arthurlegal:administrative-legal-idari-dava-prep — yeni idari işleme karşı dava
- /arthurlegal:administrative-legal-epdk-proaktif-gorus — EPDK Kurul'a görüş
- /arthurlegal:administrative-legal-ced-itiraz — ÇED ret
- Manuel: ~/.claude/plugins/config/claude-for-legal/administrative-legal/CLAUDE.md
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
| idare hukuku ogretisi — DergiPark *Idare Hukuku ve Ilimleri* dergisi router tarafindan secilir; **ikincil** | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
