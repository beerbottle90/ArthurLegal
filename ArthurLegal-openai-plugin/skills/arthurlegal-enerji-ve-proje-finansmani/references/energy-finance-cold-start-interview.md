# energy-finance-cold-start-interview

Energy Finance & M&A plugin'ini yapılandır. Aktif işlem portföyü, dış vekil paneli, onay matrisi ve proje finansmanı modeli sorgulanır. 5 dakika.

# Cold-Start Interview — Energy Finance & M&A Practice

## Amaç

Diğer skill'ler bu profil olmadan körce çalışır. Yeni kurulumda çalıştır.

## Hızlı mod (5 soru)

1. **Aktif işlem türleri:** M&A devralma / proje finansmanı / JV kurma / LNG offtake / karma
2. **Tipik işlem büyüklüğü:** <50M USD / 50-500M / >500M
3. **Dış vekil modeli:** Global büro (Clifford Chance vb.) / Türk büro / karma
4. **Yönetim dili:** İngilizce ağırlıklı (uluslararası karşı taraf) / Türkçe ağırlıklı
5. **VDR platformu:** Datasite / Intralinks / SharePoint / başka

## Tam mod (ek sorular)

### Portföy
- Aktif M&A dosyası sayısı ve aşamaları
- Aktif proje finansmanı dosyaları (pre-financial close / construction / refinancing)
- Aktif JV müzakereleri
- LNG offtake portföyü (mevcut + müzakere halinde)

### Dış vekil ve danışman
- Finansman hukuku ana büro + yerel ofis bağlantısı
- Vergi danışmanı (TP + transfer vergisi)
- Teknik danışman (lender's engineer, owner's engineer)
- Sigorta danışmanı
- VDR yöneticisi

### Onay ve eskalasyon
- Hangi tutarda Yönetici Ortak devreye giriyor?
- SPK/EPDK bildirim tetikleyici eşiği (müvekkil halka açıksa)
- Kamu açıklaması tetikleyici (varsa)

## Çıktı

```markdown
## ✓ Energy Finance profile dolduruldu

**Portföy:** [özet]
**Dış vekil:** [özet]
**Onay matrisi:** [özet]

**Önerilen ilk skill:**
- `energy-finance-ma-diligence-energy` iş akışı (`arthurlegal-enerji-ve-proje-finansmani` becerisi, `../arthurlegal-enerji-ve-proje-finansmani/references/energy-finance-ma-diligence-energy.md`) — aktif devralma varsa
- `energy-finance-project-finance-review` iş akışı (`arthurlegal-enerji-ve-proje-finansmani` becerisi, `../arthurlegal-enerji-ve-proje-finansmani/references/energy-finance-project-finance-review.md`) — finansman kapatma yakınsa
- `energy-finance-jv-agreement-review` iş akışı (`arthurlegal-enerji-ve-proje-finansmani` becerisi, `../arthurlegal-enerji-ve-proje-finansmani/references/energy-finance-jv-agreement-review.md`) — JV müzakere aşamasındaysa
- `energy-finance-lng-offtake-review` iş akışı (`arthurlegal-enerji-ve-proje-finansmani` becerisi, `../arthurlegal-enerji-ve-proje-finansmani/references/energy-finance-lng-offtake-review.md`) — LNG sözleşmesi inceleme gerekiyorsa
```

---

## Kaynak katmanı — /legal-research

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
> **Gizlilik:** az_, scholar_ ve contracts_ araclari kamuya acik kaynaklarda arama yapar — gizli taslak, muzakere
> pozisyonu veya kisisel veri **gonderilmez**.

| Ihtiyac | Kaynak skill |
|---|---|
| **bu plugin icin birincil kullanim** — PSA/JOA, cost recovery, profit split, stabilizasyon, DMO, decommissioning, yerel icerik benchmark'i | ``legal-research-sozlesme-emsali` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-sozlesme-emsali.md`)` |
| AZ upstream/yer alti serveti rejimi, JV ve enerji mevzuati — akt + statu | ``legal-research-az-mevzuat` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-az-mevzuat.md`)` |
| Energy Charter Treaty, yatirim tahkimi, stabilizasyon klozu ogretisi — **ikincil** | ``legal-research-karsilastirmali-doktrin` iş akışı (`arthurlegal-arastirma-ve-atif` becerisi, `../arthurlegal-arastirma-ve-atif/references/legal-research-karsilastirmali-doktrin.md`)` |

Rehberler: `../arthurlegal/references/eqanun-mcp-rehberi.md` · `../arthurlegal/references/lex-scholar-rehberi.md` · `../arthurlegal/references/resourcecontracts-rehberi.md` · `../arthurlegal/references/karsilastirmali-hukuk-rehberi.md` · `../arthurlegal/references/nl-rechtspraak-mcp-rehberi.md` · `../arthurlegal/references/pl-sejm-mcp-rehberi.md` · `../arthurlegal/references/at-ris-mcp-rehberi.md` · `../arthurlegal/references/ie-statutebook-mcp-rehberi.md` · `../arthurlegal/references/fi-finlex-mcp-rehberi.md` · `../arthurlegal/references/es-boe-mcp-rehberi.md`
