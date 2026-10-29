---
name: expert-opinion-uzman-mutalaasi
description: >
  Uzman mütalaası / uzman görüşü ÜRETİMİ (HMK m.293) — şirket lehine taraf delili
  olarak bilimsel/teknik veya hukuki mütalaa taslağı. Yapı: konu & sorular, özet
  görüş, gerekçeli analiz (mevzuat + içtihat + doktrin), sonuç. Bilirkişiden farkı:
  taraf delili, her aşamada sunulabilir. Hukuki mütalaada (legal opinion) doktrin +
  yerleşik içtihat sentezi. Tipik alanlar: enerji/EPC/su/çevre/İSG + ticari hukuk.
user-invocable: true
---

# Uzman Mütalaası (Uzman Görüşü — HMK m.293)

> **HMK m.293:** Taraf, dava konusu uyuşmazlığa ilişkin **kendi seçtiği uzmandan** bilimsel mütalaa (uzman görüşü) alıp dosyaya sunabilir — **taraf delilidir**, her aşamada sunulabilir, ücretini talep eden taraf öder. Bilirkişiden farkı: mahkeme atamaz, tarafsızlık iddiası taşımaz ama **bilimsel/metodolojik** olmak zorundadır (zayıf görüş karşı tarafça çürütülür). Her çıktı **TASLAK** — fiilen mütalaayı **uzman/akademisyen imzalar**; şirket/büro için [Baş Hukuk Müşaviri] onayı.

## İlk soru: mütalaa türü?
- **Teknik/bilimsel mütalaa** — mühendislik/mali/aktüeryal (örn. HES üretim kaybı hesabı, EPC gecikme analizi, kusur dağılımı, zarar/yoksun kâr).
- **Hukuki mütalaa (legal opinion)** — bir hukuki sorunun doktrin + yerleşik içtihat ışığında analizi (örn. sözleşme hükmünün yorumu, lisans devri rejimi, force majeure, zamanaşımı). *Not: mahkemeye sunulan uzman görüşü genelde teknik konuda güçlüdür; hukuki mütalaa daha çok strateji/ikna + emsal akademik destek içindir.*

## Yapı (her iki tür için iskelet)

```markdown
UZMAN GÖRÜŞÜ (HMK m. 293)
Hazırlayan: [Uzman ad — unvan/akademik kariyer — uzmanlık alanı]
Talep eden: [Müvekkil / Şirket] vekili Av. [ad]
İlgili dava: [Mahkeme — Esas No]   Tarih: GG.AA.YYYY

I. KONU VE YÖNELTİLEN SORULAR
   [Cevaplanması istenen somut soru(lar) — net]
II. İNCELENEN BELGELER / VERİ
   [dosya kapsamı, teknik veri, sözleşme]
III. ÖZET GÖRÜŞ (yönetici özeti)
   [2-4 cümlede ana sonuç]
IV. GEREKÇELİ ANALİZ
   [Teknik: metodoloji + hesap + standart/norm atfı + alternatif senaryolar]
   [Hukuki: ilgili mevzuat `[ArthurLegal MCP (`tr_`)]` + yerleşik içtihat `[ArthurLegal MCP (`tr_`)]`
    + doktrin yazar/eser; çekilemezse `UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>` sentezi; karşı argümanların ele alınması]
V. SONUÇ
   [Soru(lar)a net, gerekçeli cevap; varsayım/sınırlamalar açık]
   [İmza/kaşe alanı — uzman]
EKLER: özgeçmiş (uzmanlık ispatı), hesap tabloları, kaynak listesi
```

## İlkeler (mütalaayı güçlü kılan)
- **Metodoloji şeffaf:** her sonuç izlenebilir hesap/standart/kaynağa dayanmalı.
- **Karşı argümanı ele al:** güçlü mütalaa, aleyhe görüşü tartışıp neden zayıf olduğunu gösterir (yalnızca lehe seçmece değil).
- **Aşırılıktan kaçın:** abartılı/tek yanlı görüş itibar kaybettirir; "taraf delili ama bilimsel" dengesi.
- **Hukuki nitelendirme:** uzman görüşü (özellikle hukuki mütalaa) bilirkişiden farklı olarak hukuki yorum yapabilir, ama **mahkemeyi bağlamaz**; "nihai takdir mahkemenindir".
- **Atıf disiplini:** içtihat/madde **ArthurLegal MCP (`tr_`)'den çekilir**; doktrin atfı doğrulanır. **Uydurma kaynak = mütalaanın çürütülmesi.**

## Kaynak (ArthurLegal MCP (`tr_`))
```
tr_mevzuat_ara / tr_mevzuat_getir   # dayanak madde metni
tr_ictihat_ara(query="<hukuki sorun>", chamber="<ilgili daire>")  # yerleşik içtihat
tr_aym_ara                  # AYM (anayasal boyut varsa)
```
Sektörel teknik dayanak: `${CLAUDE_PLUGIN_ROOT}/references/epdk-rehberi.md`, `${CLAUDE_PLUGIN_ROOT}/references/ced-rehberi.md`, `${CLAUDE_PLUGIN_ROOT}/references/isg-dava-rehberi.md`, `${CLAUDE_PLUGIN_ROOT}/references/bilirkisilik-rehberi.md`.

## Tipik mütalaa konuları
- HES üretim/su kullanım kaybı, çevre debisi etkisi hesabı (teknik)
- EPC gecikme/uzatma hakkı, hakediş/iş artışı, ayıp analizi (teknik)
- EPDK lisans devri / pay devri rejimi, YEKDEM hak kazanımı yorumu (hukuki)
- Force majeure / aşırı ifa güçlüğü (TBK m.138) enerji sözleşmesinde (hukuki)
- İş kazası kusur dağılımı + tazminat hesabı (teknik+mali)
- Sözleşme yorumu / sınırlı sorumluluk klozu geçerliliği (hukuki)

## Bilirkişi raporuna karşı mütalaa
Karşı/mahkeme bilirkişi raporu zayıfsa, **uzman görüşü** o raporu çürütmek için güçlü araçtır → `/arthurlegal:expert-opinion-bilirkisi-raporu` (itiraz) ile **birlikte** sunulur (itiraz dilekçesi + ekinde uzman görüşü).

## Çıktı
```markdown
[ÜST BAŞLIK]
# Uzman Görüşü Taslağı — [tür] — [konu]

## ⚠️ İnceleyen notu
- **Tür:** teknik / hukuki
- **Yöneltilen soru(lar):** [N adet]
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [✓ N / ✗]; ArthurLegal MCP (`tr_`) [✓ N emsal / ✗]; doktrin [✓ / UYARI: veri çekilemedi, teyidiniz gerekli: <bağlantı>]
- **Metodoloji:** [hesap/standart belirtildi mi]
- **Sınırlama/varsayım:** [N adet]
- **Onay:** uzman/akademisyen imzası + [Baş Hukuk Müşaviri] şart (taslak imzasız geçersiz)

## Uzman görüşü taslağı
[doldurulmuş iskelet]

## Sonraki adımlar
> 1. **Dış uzman/akademisyen** ile içeriği teyit + imza
> 2. **Bilirkişi raporu itirazına ekle** — `/arthurlegal:expert-opinion-bilirkisi-raporu`
> 3. **Dilekçeye delil olarak bağla** — `/arthurlegal:advocacy-legal-ozel-hukuk-dilekce` / `:kamu-hukuku-dilekce`
> 4. **Emsal/doktrin güçlendir** — ArthurLegal MCP (`tr_`)
> 5. **Başka**

**One question I'd ask:** [örn. "Bu mütalaayı imzalayacak uzmanın alandaki tanınırlığı/akademik ağırlığı ne? Uzman görüşünün ikna gücü, imzalayanın otoritesiyle doğru orantılı."]
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
