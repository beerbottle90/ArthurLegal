---
name: tax-legal-cold-start-interview
description: >
  Tax pratiğini bilgisayara öğret — tax modeli (Mali İşler ana / Büyük 4 ortak /
  karma), dış vergi danışmanı + vergi avukatı paneli, eskalasyon eşikleri (özellikle
  uzlaşma yetkisi), aktif vergi davaları envanteri, yakıcı stres alanları
  (TP / KDV iade / ÖTV). 2dk hızlı veya 10dk tam mod.
user-invocable: true
---

# Cold-Start Interview — Tax Practice

## Amaç

Diğer skill'ler bu profil olmadan körce çalışır. Yeni kurulumda veya pratik değişikliğinde çalıştır.

## Modlar

Argümansız çağrılırsa sor:

> İki mod:
> - **Hızlı (2 dakika)** — 6 kritik soru
> - **Tam (10 dakika)** — 20+ soru, tüm profil
>
> Hangisini istersin? (`--redo` mevcut sıfırlar; `--check-integrations` sadece bağlantı testi)

## Hızlı mod (6 soru)

1. **Tax modeli:** Mali İşler ana / Büyük 4 ortak / Karma / İçeride tax ekibi var
2. **Hukukun rolü:** Sadece dava aşamasında / planlama dahil / tüm aşamalarda
3. **Birincil yakıcı stres:** TP / KDV iade / ÖTV / damga / karma
4. **Aktif vergi davası sayısı:** yaklaşık
5. **Büyük 4 firma:** PwC / Deloitte / EY / KPMG / başka
6. **Uzlaşma onay matrisi:** Mali İşler özerk mi, hukuk dahil mi, CFO'da mı

## Tam mod (20+ soru, batch'ler)

### Batch 1 — Tax pratik modeli
- Tax modeli + iç rol
- Mali İşler içinde dedicated vergi yöneticisi var mı
- Hukuk müşaviri devreye giriş eşiği (otomatik vs. çağrı üzerine)
- Yakıcı stres alanları (sıralı)
- Aktif vergi davaları envanteri (yaklaşık adet + tip)

### Batch 2 — Dış vergi danışmanı + avukat paneli
- Büyük 4 ana firma + sözleşme tipi (yıllık paket vs. iş başı)
- Transfer pricing dokümantasyon — hazırlayan, onaylayan
- YMM (Yeminli Mali Müşavir) — kim, hangi konularda
- Vergi davası dış avukat — Ankara mı, İstanbul mı, uzman büro mu
- AYM bireysel başvuru için ayrı uzman var mı

### Batch 3 — Eskalasyon ve onay matrisi
- Özelge talebi onay
- İdari itiraz onay
- Tarhiyat öncesi/sonrası uzlaşma onay (tutar kademeli)
- Vergi davası açma onayı
- AYM bireysel başvuru onay
- VUK m. 359 kaçakçılık iddiasında ceza savunma

### Batch 4 — Sistem ve entegrasyonlar
- SAP ERP vergi modülü
- e-Beyanname / GİB İBİS portalı
- iManage / SharePoint vergi dosyaları
- Büyük 4 firma portal entegrasyonu
- Vergi dava case management

### Batch 5 — Halka açık ve özel
- [HALKA AÇIK İŞTİRAK] KDV iade büyüklüğü (yıllık tahmin)
- [RAFİNERİ] ÖTV mahsubu hacmi
- [Ana ortak / ilişkili taraf] intra-group işlem hacmi (TP risk)
- KAP açıklama tetikleyici tutar (büyük tarhiyat → özel durum açıklama)
- MASAK koordinasyon (yüksek tutarlı uluslararası işlem)

## Çıktı

```markdown
## ✓ Tax practice profile dolduruldu

**Doldurulan:**
- Tax modeli: [özet]
- Yakıcı stres: [özet]
- Outside panel: [özet]
- Eskalasyon: [özet]
- ...

**Hala [DOLDUR]:**
- [liste]

**Sonraki adım önerisi:**
- /arthurlegal:tax-legal-transfer-pricing-review — yıllık TP dokümantasyon dönemi
- /arthurlegal:tax-legal-vergi-incelemesi-response — Maliye inceleme geldi
- /arthurlegal:tax-legal-tax-litigation-prep — aktif vergi davası dosyaları
- Manuel: ~/.claude/plugins/config/claude-for-legal/tax-legal/CLAUDE.md
```

## --check-integrations

1. **ArthurLegal MCP (`tr_`)** — test: `tr_kurum_karari_ara(kurum="gib", query="transfer fiyatlandırma")` → cevap geliyor mu?
2. **ArthurLegal MCP (`tr_`)** — test: `tr_mevzuat_ara(number="213", types=["KANUN"])` → VUK dönüyor mu?
3. **iManage** — test
4. **(SAP ERP)** — bağlantı raporu

Rapor formatı litigation-legal'daki ile aynı.

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
| AZ Vergi Mecellesi, intra-group transfer fiyatlandirmasi — akt + statu | `/arthurlegal:legal-research-az-mevzuat` |
| transfer pricing ve uluslararasi vergi ogretisi — **ikincil**; ozelge ve Danistay karari yerine gecmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
