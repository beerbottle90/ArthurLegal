---
name: expert-opinion-bilirkisi-raporu
description: >
  Bilirkişi raporu ÜRETİMİ ve karşı rapora İTİRAZ — (a) teknik bilirkişi rapor
  taslağı (Bilirkişilik K. 6754 + HMK m.266-287 / CMK m.62-73), (b) mahkeme/karşı
  bilirkişi raporuna itiraz & ek rapor talebi (HMK m.281). HMK m.266 sınırı: yalnız
  teknik/özel bilgi, hukuki nitelendirme YASAK. Tipik teknik alanlar:
  elektrik/şebeke, EPC hakediş-gecikme, HES su/debi, çevre, İSG kusur, mali zarar.
user-invocable: true
---

# Bilirkişi Raporu Üretimi & İtiraz

> **Şirket içi (in-house) gerçeği:** Şirket personeli kendi davasında bilirkişi atanmaz (çıkar çatışması, HMK m.272 red). Bu skill'in **birincil kullanımı (b) karşı/mahkeme bilirkişi raporuna İTİRAZ**; ikincil (a) bağımsız/dış teknik bilirkişinin rapor **taslaklaması**. Her çıktı **TASLAK** + dış uzman + [Baş Hukuk Müşaviri] onayı.

## İlk soru: hangi mod?
- **(a) Rapor taslağı** — atanmış (dış/bağımsız) bilirkişi adına teknik rapor iskeleti.
- **(b) Rapora itiraz** — eldeki bilirkişi raporunu eleştir + ek rapor/yeni bilirkişi talebi (HMK m.281).

## KRİTİK İLKE (her iki modda)

**HMK m.266 / m.279:** Bilirkişi yalnızca **özel veya teknik bilgi** gerektiren konuda görüş verir. **Hâkimlik mesleğinin gerektirdiği genel ve hukuki bilgiyle** çözülecek konuda bilirkişiye gidilemez; **bilirkişi hukuki nitelendirme/değerlendirme yapamaz** (kusurun hukuki sonucu, sözleşmenin yorumu, tazminata hükmedilmesi → hâkimin işi). Rapor bunu aşıyorsa = **itiraz sebebi**.

## MOD (a) — Teknik bilirkişi rapor taslağı

### Yapı (6754 + BDB rapor standardı)
```markdown
[MAHKEME] — Esas No: [...] — BİLİRKİŞİ RAPORU
Bilirkişi: [ad, uzmanlık alanı, sicil no]   Tarih: GG.AA.YYYY

1. GÖREVLENDİRME VE İNCELEME KONUSU
   [Mahkemenin sorduğu teknik sorular — aynen]
2. DOSYA KAPSAMI / İNCELENEN BELGELER
   [klasör/sayfa, keşif, numune — neyin incelendiği]
3. TEKNİK TESPİTLER (olgu)
   [ölçülebilir, metodolojili: hesap/standart/norm atfı]
4. DEĞERLENDİRME (özel/teknik bilgi — HUKUKİ NİTELENDİRME YOK)
   [sorulara teknik cevap; varsayımlar açık; alternatif senaryolar]
5. SONUÇ (teknik)
   [her soruya net teknik karşılık; takdir mahkemenindir notu]
EKLER: hesap tabloları, standartlar, fotoğraf, kroki
```
- Metodoloji + standart (TS/IEC/şebeke yönetmeliği/EPDK tebliği/YEKDEM hesap esasları) atıfla; ArthurLegal MCP (`tr_`) ile çekilir; çekilemezse `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>`.
- Belirsizlik/varsayım → açıkça yaz. "Takdir mahkemenindir."

## MOD (b) — Bilirkişi raporuna itiraz (HMK m.281)

### İtiraz sebepleri kontrol listesi (raporu bunlara karşı tara)
- [ ] **Görev/kapsam aşımı** — bilirkişi **hukuki nitelendirme** yapmış mı? (m.266 ihlali)
- [ ] **Eksik inceleme** — dosyadaki belge/keşif/numune dikkate alınmamış
- [ ] **Metodoloji hatası** — yanlış standart/hesap/varsayım; kontrol edilebilir değil
- [ ] **Dosya kapsamı dışı veri** — dayanaksız kabul, taraflardan birine ait varsayım
- [ ] **Çelişki** — rapor içi veya dosyadaki diğer delil/raporla çelişki
- [ ] **Soruların yanıtsızlığı** — mahkeme sorularına cevap vermemiş
- [ ] **Güncel mevzuat/standart** — yürürlükten kalkmış norm kullanımı

### İtiraz dilekçesi taslağı
```markdown
[MAHKEME] SAYIN HAKİMLİĞİ'NE — Esas No: [...]
KONU: GG.AA.YYYY tarihli bilirkişi raporuna İTİRAZLARIMIZ ve EK RAPOR / YENİ
      BİLİRKİŞİ İNCELEMESİ talebimizdir. (HMK m.281)

I. RAPORUN ÖZETİ [bilirkişinin sonucu]
II. İTİRAZLARIMIZ
  1. [Görev aşımı — hukuki nitelendirme: rapor m.266'yı aşmış; örnek alıntı]
  2. [Eksik inceleme — dikkate alınmayan EK-... belgesi]
  3. [Metodoloji/hesap hatası — doğru hesap: ...]
  4. [Çelişki — ...]
III. SONUÇ VE TALEP
  1. İtirazlarımız doğrultusunda **aynı bilirkişiden EK RAPOR** alınmasına,
     (kabul görmezse) **yeni bir bilirkişi/heyetten rapor** alınmasına,
  2. [gerekirse uzman görüşümüzün (HMK m.293) dosyaya kabulüne],
  karar verilmesini talep ederiz. GG.AA.YYYY — Vekil
EKLER: itiraza esas belgeler, (varsa) uzman görüşü
```

## Emsal / dayanak (ArthurLegal MCP (`tr_`))
```
tr_ictihat_ara(query="+bilirkişi +raporu +eksik +inceleme +<teknik +konu>",
  chamber="<ilgili HD/CD>", date_from="2021-01-01")
```
Yerleşik içtihat: "denetime elverişli olmayan rapor hükme esas alınamaz" vb. — yalnızca çekileni işle.

## CMK bilirkişisi (ceza dosyası)
İş kazası/çevre ceza dosyasında bilirkişi → CMK m.62-73; kusur dağılımı raporuna itiraz aynı mantık + CMK usulü. `/arthurlegal:advocacy-legal-ceza-dilekce` ile koordine.

## Teknik alan ipuçları
- **Elektrik/şebeke:** kurulu güç, kapasite faktörü, şebeke kısıtı, sayaç/uzlaştırma (EPİAŞ), YEKDEM hesabı `[${CLAUDE_PLUGIN_ROOT}/references/epdk-rehberi.md]`
- **EPC/inşaat:** hakediş, gecikme/uzatma analizi (delay), iş artışı, ayıp/kusur
- **HES:** su kullanım hakkı, çevre debisi (can suyu), üretim kaybı hesabı
- **İSG/iş kazası:** kusur dağılımı, kişisel koruyucu, SGK/iş müfettişi raporuyla tutarlılık
- **Mali:** zarar/yoksun kalınan kâr hesabı, faiz, ıskonto

## Çıktı
```markdown
[ÜST BAŞLIK]
# Bilirkişi [Raporu Taslağı / Rapora İtiraz] — [dosya/esas no]

## ⚠️ İnceleyen notu
- **Mod:** (a) rapor taslağı / (b) itiraz
- **İncelenen rapor kapsamı:** [okunan sayfa/bölüm]
- **m.266 sınırı:** [rapor hukuki nitelendirme yapmış mı? evet→güçlü itiraz]
- **Kaynaklar:** Mevzuat/standart [✓/✗]; ArthurLegal MCP (`tr_`) emsal [✓ N / ✗]
- **Onay:** dış uzman + [Baş Hukuk Müşaviri] şart

## [Rapor taslağı / İtiraz dilekçesi]
[doldurulmuş]

## Sonraki adımlar
> 1. **Uzman görüşü ile güçlendir** — `/arthurlegal:expert-opinion-uzman-mutalaasi`
> 2. **İtirazı dilekçeye bağla** — `/arthurlegal:advocacy-legal-ozel-hukuk-dilekce` (HMK m.281)
> 3. **Dış teknik uzman** revizesi
> 4. **Süre takibi** — `/arthurlegal:advocacy-legal-yazihane-asistani` (itiraz 2 hafta, HMK m.281)
> 5. **Başka**

**One question I'd ask:** [örn. "Raporun yanlış olduğunu düşündüğümüz teknik nokta, dosyadaki hangi somut belge/ölçümle çürütülüyor? İtiraz ancak somut dayanakla güçlü olur."]
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
> **Meslek sirri (Av. K. m. 36):** uc MCP de PUBLIC arama aracidir — muvekkil
> bilgisi, dosya ozeti, karsi taraf adi veya gizli taslak **gonderilmez**. Sorgu
> soyut hukuki kavram olur (`mucbir sebep uyarlama`), dosya alintisi olmaz.
> Ayrica bkz. `${CLAUDE_PLUGIN_ROOT}/references/mesleki-sir-rehberi.md`.

| Ihtiyac | Kaynak skill |
|---|---|
| mutalaanin akademik dayanagi — Turk ve karsilastirmali ogreti; **hakemlilik uc durumlu** (`true`/`false`/`null`), ABD law review'lari ogrenci editorludur ve hakemli sayilmaz | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| sozlesmesel bir teknik meselede imzali emsal kloz metni | `/arthurlegal:legal-research-sozlesme-emsali` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md`
