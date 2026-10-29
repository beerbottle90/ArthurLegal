---
name: employment-legal-expansion-update
description: >
  Süren bir uluslararası genişleme projesinin durumunu güncelle — neyin önünün
  açıldığını yeniden hesaplar, gecikenleri işaretler, sıradaki öncelikleri çıkarır;
  çalışma izni, SGK tescili gibi süreli Türkiye kalemlerini ve yerel avukat brifini
  izler. Son oturumdan bu yana iş ilerlediğinde ve takip dosyası güncel durumu
  yansıtmalıyken kullan.
argument-hint: "[ülke adı]"
---

# /expansion-update

Açık bir genişleme takip dosyasına döner ve son oturumdan bu yana olanlara göre kalemleri günceller: önü açılanlar, gecikenler, sıradaki öncelikler.

## Talimat

1. `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını yükle; matter workspace etkinse aktif matter'ı teyit et.

2. Takip dosyasını bul: `~/.claude/plugins/config/claude-for-legal/employment-legal/expansion-<ulke-slug>.yaml` (matter workspace açıksa aktif matter klasöründe). Yoksa: "[Ülke] için genişleme takip dosyası yok. Başlatmak için `/arthurlegal:employment-legal-expansion-kickoff [ülke]` çalıştırın." Birden fazla dosya varsa ve ülke verilmediyse hangisi olduğunu sor.

3. Dosyayı oku ve durumu göster:

```
[Ülke] genişlemesi ([yön]) — son güncelleme [tarih]
Açık: [N] | Devam: [N] | Tamam: [N] | Blokeli: [N]

Sıradaki öncelikler (en yakın son tarih ya da en çok kalemi bekleten):
  [kalem] — sahibi: [sahip]
  [kalem] — sahibi: [sahip]
  [kalem] — sahibi: [sahip]
```

4. Güncellemeleri **tek seferde** iste — kalem kalem sorma:

   > Son baktığımızdan beri neler ilerledi? Değişenleri söyleyin (ör. "yapı kararı verildi — İstanbul'da şirket kuruluyor", "yerel avukat tutuldu, perşembe görüşme", "çalışma izni başvurusu yapıldı", "işyeri riski analizi vergide bekliyor"). Yeni kalem ekleyebilir, son tarih değiştirebilirsiniz.

5. Güncellemeleri dosyaya uygula. `tamam` olan her kalem için `bagimli_oldugu` alanında onu bekleyen kalemleri bul ve "artık yapılabilir" diye işaretle. Örnek bağımlılıklar: şirket kuruluşu → SGK işyeri bildirgesi (5510 m. 11) → işe giriş bildirgeleri (5510 m. 8); çalışma izni (6735 m. 6) → yabancı çalışanın başlangıç tarihi; yerel avukat brifinin cevabı → yerel sözleşme taslağı.

6. Son tarihi geçmiş ve hâlâ `acik` ya da `devam` olan kalemleri işaretle:

```
⚠️ Gecikti: [kalem] — son tarih [tarih], sahibi: [sahip]
```

   Türkiye kalemlerinde kanuni süreyi kaçırma riski varsa (ör. işyeri bildirgesi en geç sigortalı çalıştırmaya başlanan tarihte, işe giriş bildirgesi sigortalılık başlangıcından önce) 🔴 ile ayrıca işaretle ve eskalasyon tablosundaki kişiye bildirmeyi öner.

7. Yeni bir yasal dayanak girilecekse yazmadan önce doğrula: Türkiye maddesi için `tr_mevzuat_madde_getir`; yabancı ülke için ilgili ArthurLegal aracı (kaynak yoksa "yerel hukukçu görüşü"). Yerel avukat cevabı geldiyse kaleme özetini ve atıflarını işle; tarihini `dayanak` alanına yaz.

8. Dosyayı yaz ve teyit et:

```
Takip dosyası güncellendi — [N] kalem kapandı, [N] açık.
Sıradaki öncelik: [en üstteki açık kalem].
```

## Örnekler

```
/arthurlegal:employment-legal-expansion-update Almanya
```

```
/arthurlegal:employment-legal-expansion-update
(birden fazla takip dosyası varsa ülkeyi sorar)
```

> Takip dosyası şeması, durum kuralları ve bağımlılık mantığı `international-expansion`
> referans skill'indedir — esaslı işe başlamadan önce yükle.

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
