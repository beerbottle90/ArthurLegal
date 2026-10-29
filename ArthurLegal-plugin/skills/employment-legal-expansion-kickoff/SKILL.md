---
name: employment-legal-expansion-kickoff
description: >
  Yeni bir ülke için uluslararası genişleme planlamasını başlat — yönü belirler
  (Türkiye'den dışarı / dışarıdan Türkiye'ye), ön bilgiyi toplar, yapı seçeneklerini
  çerçeveler (Türkiye'de İş K. m. 7 sınırları), vergi/finans/İK sorularını taslaklar,
  ArthurLegal MCP ile hedef ülke mevzuatını arar ya da kaynak yoksa yerel avukata
  yönlendirir ve kalıcı takip dosyası oluşturur. "[Ülke]de işe alıyoruz", "[ülke]ye
  genişleme", "[ülke]de ilk çalışan" ya da "yabancı şirket Türkiye'de işe alacak"
  denildiğinde kullan.
argument-hint: "[ülke adı] [yön: disari | turkiye]"
---

# /expansion-kickoff

Yeni bir ülke için genişleme projesini başlatır: yön ve ön bilgi, yapı çerçevesi, paydaş soruları, ülke kaynağı ya da yerel avukat brifi, kalıcı takip dosyası.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → eşik tablosu (yurt dışı satırları), eskalasyon. Matter workspace etkinse aktif matter'ı teyit et.
2. `international-expansion` referans skill'ini yükle ve tüm akışı uygula (Adım 0 yön → Adım 6 çıktı).
3. Takip dosyası yolu: matter workspace kapalıysa `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-<ulke-slug>.yaml`; açıksa aktif matter klasöründe aynı ad. Bu ülke için dosya zaten varsa uyar: "[Ülke] için bir genişleme takip dosyası zaten var. Güncellemek için `/arthurlegal:employment-legal-expansion-update [ülke]` kullanın ya da baştan başlamak istediğinizi teyit edin."
4. Hedef ülke ArthurLegal MCP kapsamında değilse (önek tablosunda yoksa) açıkça yaz: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al." Kural uydurma.
5. Türkiye'ye ilişkin her madde atfını yazmadan önce `tr_mevzuat_madde_getir` ile çek; çekilemeyen için UYARI satırı.
6. Bitişte takip dosyasını oluştur ve yolunu göster.

## Örnekler

```
/arthurlegal:employment-legal-expansion-kickoff Almanya disari
```

```
/arthurlegal:employment-legal-expansion-kickoff Türkiye turkiye
(yabancı ana şirket İstanbul'da ilk iki mühendisi işe alacak)
```

```
/arthurlegal:employment-legal-expansion-kickoff
(skill ülkeyi ve yönü soracak)
```

> Yapı çerçevesi, paydaş soruları, ArthurLegal önek tablosu, brif şablonu ve takip dosyası
> şeması `international-expansion` referans skill'indedir — esaslı işe başlamadan önce yükle.

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
