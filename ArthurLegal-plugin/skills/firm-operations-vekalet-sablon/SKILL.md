---
name: firm-operations-vekalet-sablon
description: >
  İş türüne göre vekâletname yetki listesi: HMK m. 74 özel yetkileri, tevkil, ibraz
  (HMK m. 76-77), avukat onaylı örnek ve yetki belgesi (Av. K. m. 56), çekilme ve azlin
  sonuçları. Tek tip vekâletnamenin biçimini TBB ile Türkiye Noterler Birliği hazırlar;
  bu skill noter metnini değil, eklenecek yetkileri üretir.
user-invocable: true
---

# Vekâlet Şablonu — Yetki Listesi

## Tetikleyici

`/arthurlegal:firm-operations-fee-agreement` imzalandıktan sonra, noter randevusundan önce.

## Dayanak (tr_mevzuat_madde_getir ile doğrulandı — 24.09.2026)

- HUKUK MUHAKEMELERİ KANUNU (Kanun No. 6100, RG sayı 27836) m. 74, m. 75, m. 76, m. 77
- AVUKATLIK KANUNU (Kanun No. 1136, RG sayı 13168) m. 41, m. 56, m. 171, m. 174
- TÜRK BORÇLAR KANUNU (Kanun No. 6098, RG sayı 27836) m. 512
- CEZA MUHAKEMESİ KANUNU (Kanun No. 5271, RG sayı 25673) m. 149, m. 150

⚠️ Av. K. m. 32 **mülgadır** (30/1/1979 - 2178/8); vekâletname şekline dayanak gösterilemez. Av. K. m. 35 "yalnız avukatların yapabileceği işler"i düzenler; müdafilikte vekâletname kuralı içermez.

## Akış

### 1. Biçim
Vekâletnameler Türkiye için tek tiptir; biçim ve içeriğini Türkiye Barolar Birliği ile Türkiye Noterler Birliği hazırlar (Av. K. m. 56/6). Bu skill tek tip metne eklenecek **yetkileri** belirler.

### 2. Özel yetki gerektiren işlemler (HMK m. 74)
Açıkça yetki verilmemişse vekil aşağıdakileri yapamaz. İşe göre gerekenleri işaretle:

| Yetki (HMK m. 74'teki sırayla) | Tipik iş |
|---|---|
| sulh olmak | her dava |
| hâkimi reddetmek | dava |
| davanın tamamını ıslah etmek | dava |
| yemin teklif etmek; yemini kabul, iade veya reddetmek | dava |
| başkasını tevkil etmek | her iş (bkz. 3) |
| haczi kaldırmak | icra |
| müvekkilin iflasını istemek | icra-iflas |
| tahkim ve hakem sözleşmesi yapmak | ticari uyuşmazlık |
| konkordato ya da sermaye şirketleri ve kooperatiflerin uzlaşma yoluyla yeniden yapılandırılması teklifinde bulunmak, bunlara muvafakat vermek | yeniden yapılandırma |
| alternatif uyuşmazlık çözüm yollarına başvurmak | arabuluculuk |
| davadan veya kanun yollarından feragat etmek | dava |
| karşı tarafı ibra etmek; davasını kabul etmek | dava |
| yargılamanın iadesi yoluna gitmek | kesinleşmiş karar |
| hâkimlerin fiilleri sebebiyle Devlet aleyhine tazminat davası açmak | istisnai |
| kişiye sıkı sıkıya bağlı haklarla ilgili dava açmak ve takip etmek (**hangileri olduğu açıkça yazılarak**) | kişilik hakları vb. |

Liste HMK m. 74 metnindeki kalemlerden oluşur. Listede olmayan bir yetkiyi HMK m. 74'e dayandırma.

### 3. Tevkil ve yetki belgesi
- Vekâletnamede tevkil yetkisi varsa iş başka bir avukatla birlikte veya başka bir avukata verilerek takip ettirilebilir. Genel tevkil yetkisiyle sonraki işlerde yeniden vekâlet gerekmez (Av. K. m. 171/2).
- Avukat veya avukatlık ortaklığı, tevkil yetkili tüm vekâletnamelerini kapsayan bir **yetki belgesi** verebilir; yetki belgesi vekâletname hükmündedir (Av. K. m. 56/5).
- Birden fazla vekil varsa her biri yetkilerini diğerinden bağımsız kullanır; aksi yöndeki sınırlama karşı taraf bakımından geçersizdir (HMK m. 75).

### 4. İbraz ve örnek
- Noter onaylı ya da düzenlenmiş vekâletname aslı veya avukat onaylı örneği dosyaya ibraz edilir (HMK m. 76/1).
- Avukatın onayladığı vekâletname örneği bütün yargı mercileri, resmi daireler ve kişiler için resmi örnek hükmündedir (Av. K. m. 56/1).
- Aslı olmayan vekâletnamenin örneğini onaylamak veya aslına aykırı örnek vermek üç yıldan altı yıla kadar hapis cezası gerektirir (Av. K. m. 56/3).
- Vekâletnamesiz dava açılamaz; gecikmede zarar doğabilecek hâlde mahkeme kesin süre verebilir (HMK m. 77/1).

### 5. Ceza dosyası
Şüpheli veya sanık soruşturma ve kovuşturmanın her aşamasında müdafi yardımından yararlanabilir (CMK m. 149/1). Müdafi seçebilecek durumda değilse istemi hâlinde; çocuk, kendini savunamayacak derecede malul ya da sağır ve dilsizse ve alt sınırı beş yıldan fazla hapis cezası gerektiren suçlarda istemi aranmaksızın müdafi görevlendirilir (CMK m. 150). Seçilmiş müdafinin hangi aşamada vekâletname ibraz etmesi gerektiği bu skill'de **doğrulanmadı**; bkz. `/arthurlegal:criminal-defense-cmk-gorev-atama`.

### 6. Sona erme
- Vekâlet veren de vekil de sözleşmeyi her zaman tek taraflı sona erdirebilir; uygun olmayan zamanda sona erdiren taraf diğerinin zararını giderir (TBK m. 512).
- Avukat çekilirse vekâlet görevi, durumun müvekkile **tebliğinden itibaren 15 gün** devam eder (Av. K. m. 41/1). Bu bir "15 gün önceden bildirim" kuralı değildir.
- Azilde ücret: Av. K. m. 174/2 (bkz. `/arthurlegal:firm-operations-fee-agreement`).

### 7. Yurt dışında düzenlenen vekâletname
Onay (apostil veya konsolosluk) ve tercüme gereklilikleri bu pakette doğrulanmadı; noterle teyit et.

## Çıktı

```markdown
[ÜST BAŞLIK — VEKÂLETNAME YETKİ LİSTESİ — NOTER / MÜVEKKİL İÇİN]

Müvekkil: [takma ad] — İş: [kısa ad] — GG.AA.YYYY
Vekil(ler): [avukat(lar) / avukatlık ortaklığı]
Genel yetki: tek tip vekâletname (Av. K. m. 56/6)
Özel yetkiler (HMK m. 74): [işaretlenenler]
Tevkil: var / yok — yetki belgesi: gerekli / gerekmez
Not: noter metni tek tip şablondan gelir; bu liste yalnız yetkileri gösterir.
```

## Hatalar

- Av. K. m. 32'yi dayanak göstermek (mülga)
- HMK m. 74'te olmayan bir yetkiyi ("kambiyo taahhüdü", "şikâyetten vazgeçme" gibi) HMK m. 74'e dayandırmak. Bunlar için başka bir kanunda özel yetki aranıp aranmadığı ayrıca doğrulanmalı.
- Tevkil yetkisini unutmak (iş devri yapılamaz)
- Çekilmedeki 15 günü "önceden bildirim" sanmak

Ayrıntı: `${CLAUDE_PLUGIN_ROOT}/references/vekalet-uyap-rehberi.md`

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
| yabanci karsi tarafli veya AZ baglantili yeni is alimi — mevzuat kapsaminin gercekten var olup olmadigini once dogrula | `/arthurlegal:legal-research-kaynak-secimi` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
