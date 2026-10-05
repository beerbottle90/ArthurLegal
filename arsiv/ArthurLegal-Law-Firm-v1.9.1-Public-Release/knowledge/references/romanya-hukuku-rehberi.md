# Romanya Hukuku — Kullanım Rehberi (WebFetch yöntemi)

> ⚠️ **DURUM DEĞİŞTİ (30.08.2026 yeniden test): `legislatie.just.ro` bu ortamdan
> ERİŞİLEMİYOR.** TLS el sıkışması tamamlanıyor, istek gönderiliyor, sunucu bağlantıyı
> `close_notify` göndermeden **aniden kapatıyor**. HTTP/1.1'e zorlama, tam tarayıcı
> header seti, TLS 1.2/1.3 sabitleme — hiçbiri sonuç vermedi. Bağımsız ikinci bir
> egress'ten denendiğinde farklı ama yine ölümcül bir hata alındı ("HTTP/2 framing
> layer" stream error), yani sorun sunucu tarafındaki protokol/filtre katmanında.
> **`cdep.ro`, `scj.ro`, `idrept.ro` de aynı şekilde erişilemez; `ccr.ro` 503 veriyor.**
>
> **Sonuç: Romanya'nın agent'a açık, ücretsiz, konsolide birincil kaynağı şu an YOK.**
> Aşağıdaki bölüm 1 bir **öneri** değil, erişim sağlanabilen ortamlar için saklanan
> desendir — bu ortamdan çağırma. Çalışan yollar için bölüm 1b'ye geç.
>
> 🔧 **Kalıcı çözüm:** de-eli MCP kalıbı — kendi egress'i olan bir sunucuya
> `ro-legislatie-mcp` kurulursa bu engel tamamen kalkar (MCP sunucusu siteyi kendi
> ağından çeker). Almanya'da `de_rii_*` araçlarının, WebFetch'in ulaşamadığı
> `rechtsprechung-im-internet.de`'ye ulaşması bunun kanıtı.
>
> **[Müvekkil] neden gerekli?** `firm-profile.md` B.4: **[Müvekkil] Romania** akaryakıt perakende
> iştiraki (grupta öz-üretim yenilenebilir raporlayan tek iştirak `[AR-2024 §XVI]`);
> A.4: metanol/üre ihracatının ana pazarlarından biri RO. Perakende regülasyonu, akaryakıt
> piyasası ve emtia satış uyuşmazlıkları RO hukukuna dokunur.

---

## Kaynak haritası

| Kaynak | Tür | Durum | Dil |
|--------|-----|-------|-----|
| legislatie.just.ro | Resmi mevzuat portalı (N-Lex üyesi) | ❌ **erişilemez** — bağlantı düşüyor (30.08.2026) | RO |
| cdep.ro / scj.ro / idrept.ro | Meclis külliyatı · Yargıtay · ticari DB | ❌ erişilemez | RO |
| ccr.ro | Anayasa Mahkemesi | ❌ 503 | RO |
| **EUR-Lex CELLAR** | AB-türevli RO mevzuatı, **RO dilinde tam metin** | ✅ **BİRİNCİL** (bölüm 1b) | RO + EN |
| **portal.just.ro** | Mahkeme dosya/karar sorgu | ✅ 200 (30.08.2026) | RO |
| **just.ro/legislatie** | Bakanlık mevzuat sayfaları | ✅ 200 | RO |
| lege5.ro (ücretsiz katman) | Kanun metni — **yayımlandığı hâliyle** | ⚠️ konsolide DEĞİL, değişiklikler yok | RO |
| monitoruloficial.ro | Resmî Gazete | ⚠️ tam metin abonelikli | RO |
| anre.ro | Enerji düzenleyici (ANRE) | ✅ 200 (kök sayfa) | RO (+kısmi EN) |

## 1. legislatie.just.ro — ❌ BU ORTAMDAN ERİŞİLEMEZ (desen arşivi)

> Bu bölümdeki URL'leri **çağırma** — bağlantı düşer. Desen, erişimi olan ortamlar
> (tarayıcı, RO ağı, kendi egress'i olan MCP sunucusu) için saklanmıştır.

**URL pattern'ları:**
- Belge: `https://legislatie.just.ro/Public/DetaliiDocument/{id}` — konsolide sürüm
  linkleri tarihli olarak sunulur (en güncel konsolidasyonu seç)
- Arama formu sunucu-taraflı çalışır (tip + tarih + kurum filtreleri)

**Doğrulanmış örnekler (12.06.2026):**
- Yeni Medeni Kanun (Legea 287/2009) = `DetaliiDocument/109884` ✅ (konsolide 19.12.2025 sürümü görüldü)
- Yeni Ceza Kanunu = `DetaliiDocument/109855` ✅

```
WebFetch:
  URL: https://legislatie.just.ro/Public/DetaliiDocument/{id}
  prompt: "[madde no] maddesinin konsolide metnini çıkar; hangi tarihli konsolidasyon olduğunu belirt"
```

ID bilinmiyorsa: Google `site:legislatie.just.ro {kanun adı/no}` → DetaliiDocument linki.

---

## 1b. Çalışan yollar — bunları kullan ✅

**(a) AB-türevli RO mevzuatı → EUR-Lex CELLAR, Romence tam metin.** Enerji, şirketler
hukuku, rekabet, veri koruma, çevre — RO'nun uyum mevzuatının büyük kısmı AB direktif/
tüzüklerinin transpozisyonu. CELLAR **Romence tam metni** veriyor (30.08.2026 test ✅).

⚠️ `eur-lex.europa.eu/legal-content/...` URL'leri **WebFetch ile çalışmaz** — JS kabuğu
dönüyor, Resmî Gazete indeksi görünüyor. Çalışan zincir (bkz. `eurlex-cellar-rehberi.md`):

```
1) WebFetch: https://publications.europa.eu/resource/celex/{CELEX}
   → 303 döner; redirect URL'sindeki cellar UUID'sini al
2) SPARQL ile o dilin manifestation URI'sini çöz (dil = lang:RON)
3) WebFetch: {manifestation_uri}/DOC_1     ← Romence tam metin
```
Doğrulanmış örnek — Direktif (AB) 2019/944 (elektrik iç pazarı):
`http://publications.europa.eu/resource/cellar/8594f013-8e7c-11e9-9369-01aa75ed71a1.0020.03/DOC_1`
→ "DIRECTIVA (UE) 2019/944 A PARLAMENTULUI EUROPEAN ȘI A CONSILIULUI..." ✅

**(b) RO mahkeme kararı → `portal.just.ro`** ✅ (dosya/karar sorgu, sunucu-render).

**(c) ANRE enerji düzenlemesi → `https://www.anre.ro/`** ✅ (kök sayfadan gez;
`/legislatie/` gibi tahmini alt yollar 404 veriyor, önce kök sayfayı çek).

**(d) Konsolide olmayan kanun metni → `lege5.ro` ücretsiz katman.**
⚠️ **Kritik uyarı:** ücretsiz sürüm metni *"yayımlandığı hâliyle"* verir, **sonraki
değişiklikleri içermez**. Konsolide metin abonelik arkasında. Bu katmandan alınan
metni **asla "yürürlükteki hâli" diye atıfla** — "yayım tarihli hâli, değişiklikler
doğrulanmadı" kaydı düş.

**(e) Hiçbiri yetmiyorsa → kullanıcıdan metin iste.** RO hukuku kritik bir
uyuşmazlığın merkezindeyse, RO barosundan yerel görüş almadan nihai değerlendirme yazma.

> **Atıf kuralı:** konsolide/yürürlük durumu doğrulanamayan RO metinlerinde atıfa
> **`(konsolidasyon doğrulanmadı)`** ibaresini ekle.

## 2. [Müvekkil]-kritik RO mevzuatı

| Konu | Kanun | [Müvekkil] bağlantısı |
|------|-------|------------------|
| Medeni Kanun | Legea 287/2009 (Noul Cod Civil) — id 109884 ✅ | sözleşme genel rejimi (tedarik/satış) |
| **Enerji & gaz piyasası** | Legea 123/2012 (energiei electrice și a gazelor naturale) | ANRE lisansları, perakende yükümlülükleri |
| Petrol | Legea petrolului 238/2004 | depolama/dağıtım imtiyazları |
| Akaryakıt stok | AB 2009/119 uyumu (zorunlu stok) | perakende iştiraki stok yükümlülüğü |
| Rekabet | Legea concurenței 21/1996 | akaryakıt fiyatlama soruşturma pratiği 🟠 |
| Tüketici | OG 21/1992 + AB tüketici müktesebatı | istasyon perakende tarafı |
| Şirketler | Legea societăților 31/1990 | RO iştirak yönetişimi |

**AB üyeliği notu:** RO tam AB üyesi — tüketici, rekabet, enerji ve yaptırım katmanlarında
**önce EUR-Lex** (tüzükler doğrudan uygulanır), ulusal aktarım için legislatie.just.ro.
AB yaptırım tüzükleri (833/2014 vb.) RO operasyonunda doğrudan bağlayıcıdır.

## 3. ANRE — enerji düzenleyicisi

Autoritatea Națională de Reglementare în Domeniul Energiei — lisans kararları, tarife
metodolojileri, piyasa izleme. `https://anre.ro` `[doğrulayın — agent erişimi test edilmedi]`.
Perakende lisans şartı sorularında ANRE kararı + Legea 123/2012 maddesi birlikte okunur.

## 4. Atıf formatları

- `[RO Mevzuat — legislatie.just.ro/{id} — {kanun no/yıl + madde} — GG.AA.YYYY]`
- AB katmanı → `[EU Legislation — CELEX:{no} — GG.AA.YYYY]` (mevcut kural)
- ANRE kararı → `[RO Düzenleme — ANRE — {karar no} — GG.AA.YYYY]`
- Çekilemeyen → `[model bilgisi — doğrulayın]`

## 5. Pratik notlar

- Konsolide metin tarihini HER atıfta belirt — portal birden çok konsolidasyon sunar.
- RO mahkeme kararları için merkezi ücretsiz tam-metin DB sınırlıdır (ReJust/portal.just.ro
  `[doğrulayın]`); uyuşmazlık analizinde yerel vekil teyidi şart.
- NY Konvansiyonu + AB üyesi: tenfiz ayağı görece öngörülebilir →
  `/commercial-legal:governing-law-review` Adım 5.

---

*Test: 30.08.2026 — legislatie.just.ro / cdep.ro / scj.ro / idrept.ro **erişilemez**
(bağlantı düşüyor); ccr.ro 503. Çalışanlar: EUR-Lex CELLAR Romence tam metin ✅,
portal.just.ro ✅, just.ro/legislatie ✅, anre.ro ✅, lege5.ro ücretsiz katman ⚠️.
Birincil kaynak EUR-Lex CELLAR'a taşındı; legislatie.just.ro desen arşivine düşürüldü.
Kalıcı çözüm önerisi: kendi egress'i olan `ro-legislatie-mcp`. Sürüm: v1.12.0.*
