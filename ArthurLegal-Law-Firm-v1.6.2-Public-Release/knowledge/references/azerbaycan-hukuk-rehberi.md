# Azerbaycan Hukuku — Kullanım Rehberi (içtihat + EN kaynaklar + yedekler)

> ⚠️ **v1.4.0 DEĞİŞİKLİĞİ — mevzuat artık buradan okunmuyor.**
> Azerbaycan **mevzuatı** için birincil yol **`eqanun-mcp-rehberi.md`**
> (resmî `api.e-qanun.az` üzerinde MCP sunucusu, **yürürlük statüsü
> doğrulamalı**). Bu rehber artık MCP'nin **kapsamadığı** üç işi yönetir:
> **(1) içtihat** (Anayasa Mahkemesi), **(2) İngilizce enerji ve iş hukuku
> kaynakları**, **(3) MCP erişilemezse WebFetch yedekleri.**
>
> **Durum:** ✅ Açık erişim — API anahtarı gerekmez.
> **[enerji şirketi] neden gerekli?** [Azerbaycanlı enerji karşı tarafı] ile intra-group işlemler (ham petrol tedarik,
> royalty, transfer fiyatlandırması, JV), 200+ Azerbaycanlı çalışan için iş hukuku,
> [enerji şirketi] Turkey ile [enerji şirketi] [ANA ORTAK MERKEZİ] arasındaki sözleşmelerde uygulanacak hukuk seçimi
> ve [RAFİNERİ] ortak girişim yapısı Azerbaycan hukukunu doğrudan ilgilendirir.

---

## Kaynak haritası — hangi ihtiyaç, hangi yol

| İhtiyaç | Birincil yol | Bu rehberde |
|---|---|---|
| **Mevzuat lafzı + yürürlük statüsü** | **e-qanun MCP** → `eqanun-mcp-rehberi.md` | §1 (yalnız yedek) |
| Anayasa Mahkemesi kararı | constcourt.gov.az / CODICES | §3, §4 |
| Enerji sektörü mevzuatı (EN) | minenergy.gov.az | §2 |
| İş hukuku mevzuatı (EN/RU) | NATLEX (ILO) | §5 |
| AZ hukuku hakkında doktrin | `lex-scholar-rehberi.md` (İKİNCİL — AZ'de açık erişim hukuk dergisi yok, yalnız OpenAlex) | — |
| İmzalı AZ sözleşme emsali (PSA/JOA) | `resourcecontracts-rehberi.md` | — |

| Kaynak | Tür | İçerik | Dil | Öncelik |
|--------|-----|--------|-----|---------|
| **e-qanun MCP** | **MCP** | **Tüm AZ mevzuatı + STATÜ** | AZ | **P0 — mevzuat (BİRİNCİL)** |
| e-qanun.az | WebFetch | Aynı külliyat, statü bilgisi yok | AZ | P2 — yalnız MCP yoksa |
| minenergy.gov.az/en/qanunlar | WebFetch | Enerji sektörü kanunları | EN + AZ | P0 — Enerji sektörü odağı |
| constcourt.gov.az | WebFetch | Anayasa Mahkemesi kararları | AZ + seçili EN | P1 — kararlar |
| CODICES (Venice Commission) | WebFetch | AY kararları İngilizce özet | EN + FR | P1 — kararlar EN |
| NATLEX (ILO) | WebFetch | İş hukuku mevzuatı | EN + AZ + RU | P2 — iş hukuku |

---

## 1. e-qanun.az — Resmi Azerbaycan Mevzuat Portalı (YEDEK yol)

> 🔻 **Önce `eqanun-mcp-rehberi.md`'yi dene.** MCP sunucusu aynı külliyatı resmî
> API üzerinden okur, **yürürlük statüsünü (`Qüvvədədir` / `Ləğv olunmuş`)
> raporlar** ve sitenin anti-bot korumasına takılmaz. Aşağıdaki WebFetch yolu
> yalnız MCP erişilemediğinde kullanılır — ve o hâlde **statü doğrulanmamıştır**;
> bunu çıktıda açıkça yaz ve `[review]` flag ekle. Müvekkile giden bir görüşte
> yürürlükten kalkmış bir aktın güncelmiş gibi görünmesi, bu paketin önlemek
> istediği tek hatadır.

**Kaynak Kurum:** Adalet Bakanlığı (Ədliyyə Nazirliyi)
**URL:** `https://e-qanun.az`
**Lisans:** Hükümet portalı, kamu erişimi açık
**İçerik:** Tüm kanunlar, cumhurbaşkanlığı kararname ve emirleri, yönetmelikler
**Dil:** Azerbaycan Türkçesi (AZ) birincil; sınırlı Rusça

### URI şeması

```
https://e-qanun.az/framework/{id}           ← bireysel belge
https://e-qanun.az/framework?...            ← arama
```

Belge ID'leri `LocalDoc/azerbaijan_legislation` HuggingFace dataset'indeki `id`
alanlarıyla eşleşir — eğer dataset'e ayrıca erişim varsa kaynak doğrulama için
kullanılabilir.

### WebFetch kullanımı

```
WebFetch:
  URL: https://e-qanun.az/framework/{id}
  prompt: "Azerbaycan [kanun adı] tam metnini, yürürlük tarihini ve son
           değişiklikleri çıkar"
```

**Arama yaklaşımı:** Doğrudan ID bilinmiyorsa arama sayfasını `WebFetch` ile çek:
```
WebFetch:
  URL: https://e-qanun.az/framework?tip=0&number={kanun_numarasi}
  prompt: "Kanun listesini ve her birinin ID'sini ver"
```

### Azerbaycan ile işlem yapan müvekkil için hangi kanunlar?

| Azerbaycan Kanunu | e-qanun.az konu | Olası bağlantı (enerji/ticaret sektörü) |
|---|---|---|
| Neft və qaz haqqında Qanun (1996) | Petrol ve gaz rejimi | Enerji şirketleri upstream hakları |
| Mülki Məcəllə | Medeni Kanun | Azerbaycanlı taraf ile sözleşmeler |
| Əmək Məcəlləsi | İş Kanunu | 200+ AZ çalışan |
| Mühasibat uçotu haqqında Qanun | Muhasebe | Intra-group mali raporlama |
| Vergi Məcəlləsi | Vergi Kanunu | Transfer fiyatlandırması |
| Antiinhisar Qanunu | Rekabet | Piyasa davranışı |

---

## 2. minenergy.gov.az — Enerji Bakanlığı Mevzuatı (İngilizce)

**URL:** `https://minenergy.gov.az/en/qanunlar`
**Lisans:** Hükümet portalı, kamu erişimi açık
**İçerik:** Enerji sektörü mevzuatı — elektrik, gaz, enerji verimliliği kanunları
**Dil:** İngilizce (EN) + Azerbaycan Türkçesi (AZ) — dil değiştirme mevcut
**Güncelleme:** Düzenli (2022–2025 değişiklikler mevcut)

### WebFetch kullanımı

```
WebFetch:
  URL: https://minenergy.gov.az/en/qanunlar
  prompt: "Enerji sektörü kanunlarını ve son değişiklik tarihlerini listele"
```

Bireysel kanun sayfaları e-qanun.az'a yönlendiriyor — referans için bu sayfadan
ilgili kanun bulunur, tam metin e-qanun.az'dan alınır.

### Enerji sektörü odağı

Bu sayfada doğrudan ilgili kanunlar:
- **Elektrik enerjisi haqqında Qanun** — [ELEKTRİK ÜRETİM İŞTİRAKİ] / elektrik üretim faaliyetleri
- **Qaz təchizatı haqqında Qanun** (No. 233-VIIQ, 2025) — Yeni Gaz Tedarik Kanunu
- **Energetika resurslarından istifadənin effektivliyi haqqında Qanun** — enerji verimliliği
- **Alternativ enerji mənbələrindən istifadə haqqında Qanun** — yenilenebilir enerji

---

## 3. constcourt.gov.az — Azerbaycan Anayasa Mahkemesi

**URL:** `https://www.constcourt.gov.az/en`
**Lisans:** Hükümet portalı, kamu erişimi açık
**İçerik:** Anayasa Mahkemesi plenum kararları
**Dil:** AZ birincil; seçili kararlar EN + FR

### URI şeması

```
https://www.constcourt.gov.az/en/decisions          ← karar listesi
https://www.constcourt.gov.az/en/decision/{id}      ← bireysel karar
```

> ⚠️ **SSL uyarısı:** Site zaman zaman SSL sertifika sorunları yaşıyor.
> Erişilemezse CODICES üzerinden aynı kararın EN özetine ulaşılabilir.

### WebFetch kullanımı

```
WebFetch:
  URL: https://www.constcourt.gov.az/en/decisions
  prompt: "Mülkiyet hakkı / sözleşme özgürlüğü / ticari uyuşmazlık konularındaki
           kararları listele"
```

### İngilizce yayınlar

Anayasa Mahkemesi yılda 3 kez İngilizce bülten yayınlar. Bu bültenler CODICES
veritabanında da yer alır.

---

## 4. CODICES — Venice Commission (Venedik Komisyonu)

**URL:** `https://www.venice.coe.int/webforms/pages/?p=02_CODICES&lang=EN`
**Lisans:** Avrupa Konseyi, açık erişim
**İçerik:** Azerbaycan Anayasa Mahkemesi kararları — EN + FR özetler + orijinal tam metinler
**Güncelleme:** İki haftada bir
**Kapsam:** 2018'den itibaren düzenli AZ kararları

**Bu kaynak neden değerli?** Azerbaycan kararlarının İngilizce özetlerini içerir —
`constcourt.gov.az`'ın SSL sorunu yaşadığı durumlarda ya da İngilizce özet
yeterliyse birincil tercih.

### WebFetch kullanımı

```
WebFetch:
  URL: https://www.venice.coe.int/webforms/pages/?p=02_CODICES&lang=EN
  prompt: "Azerbaijan constitutional court decisions on [konu] ara"
```

```
WebFetch:
  URL: https://www.venice.coe.int/WebForms/pages/?p=02_CODICES_dec&id={karar_id}
  prompt: "Bu Azerbaycan Anayasa Mahkemesi kararının özetini ve tam metnine
           bağlantıyı ver"
```

---

## 5. NATLEX — ILO Ulusal İş Hukuku Veritabanı (❌ ARTIK KULLANMA)

> ⚠️ **NATLEX agent'a kapalı — 403** (30.08.2026). Hem eski
> `ilo.org/dyn/natlex/natlex4.listResults` yolu hem yeni `natlex.ilo.org` host'u
> WebFetch'e **403** döndürüyor. Bu bölüm yalnızca kayıt amaçlı bırakıldı.
>
> **Bunun yerine ne kullan — AZ iş hukuku için sıralama:**
>
> 1. **e-qanun MCP** (`eqanun-mcp-rehberi.md`) — **BİRİNCİL**. Əmək Məcəlləsi ve tüm
>    iş / sosyal güvenlik mevzuatı, **statü doğrulamalı** (`Qüvvədədir` / ləğv edilib).
>    `az_search_acts(query="Əmək Məcəlləsi")` → `az_get_act_fulltext(id)`.
>    NATLEX'in verebileceği her şeyi daha güncel ve statü bilgisiyle verir.
> 2. **e-qanun.az WebFetch** (`https://e-qanun.az/framework/{id}` ✅ 200) — MCP yoksa.
>    ⚠️ Bu yolda **statü doğrulanmaz**; atıfa `(statü doğrulanmadı)` kaydını düş.
> 3. **LexScholar MCP** — AZ iş hukuku doktrini (**ikincil** kaynak).

*(Aşağıdaki desen arşivdir — çağırma.)*

```
# ❌ 403 — çalışmıyor
http://www.ilo.org/dyn/natlex/natlex4.listResults?p_lang=en&p_country=AZE
https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/{id}/AZE-{id}.pdf
```

### Enerji sektörü odağı

200+ Azerbaycanlı çalışan için NATLEX'teki kritik belgeler:
- **İş Kanunu (Əmək Məcəlləsi)** — işe alım, fesih, kıdem
- **Sosyal Sigorta Kanunu** — AZ vatandaşı çalışan sosyal güvenlik hakları
- **Yabancı Çalışan Kanunu** — eğer AZ'da çalıştırılan TR vatandaşı varsa

---

## Ek: HuggingFace Toplu Veri Kümeleri (Offline/RAG kullanımı)

> **Not:** Bu kaynaklar WebFetch ile doğrudan kullanılamaz. Offline bilgi tabanı
> oluşturmak veya RAG pipeline için kullanılır.

| Dataset | URL | İçerik | Lisans |
|---------|-----|--------|--------|
| LocalDoc/azerbaijan_legislation | huggingface.co/datasets/LocalDoc/azerbaijan_legislation | 59K belge, 4.29M satır, e-qanun.az tam metinler | Apache 2.0 |
| allmalab/eqanun | huggingface.co/datasets/allmalab/eqanun | ~150 MB, e-qanun.az ID eşleşmeli | Apache 2.0 |
| vrashad/az-legal-retrieval-xlm | huggingface.co/vrashad/az-legal-retrieval-xlm | AZ hukuk retrieval modeli | — |

Bu veriler, gelecekte Azerbaycan hukuku için bir bilgi tabanı (knowledge base) ya da
yerel vektör veritabanı oluşturulacaksa temel corpus'u sağlar.

---

## Atıf disiplini

Bu rehberdeki kaynaklardan alınan atıflar **mutlaka** etiketli olmalı:

- `[AZ Mevzuat — e-qanun MCP — {belge adı} — id:{id} — {statü} — GG.AA.YYYY]`
  — **tercih edilen biçim**; statü atıfın içindedir (bkz. `eqanun-mcp-rehberi.md`)
- `[AZ Mevzuat — e-qanun.az (WebFetch, statü doğrulanmadı) — {belge adı} — GG.AA.YYYY]`
  — yalnız MCP erişilemediğinde; **statü doğrulanmadığını gizleme**
- `[AZ Mevzuat — minenergy.gov.az — {kanun adı} — GG.AA.YYYY]` — Enerji Bakanlığı
- `[AZ Anayasa Mah. — constcourt.gov.az — {karar no} — GG.AA.YYYY]` — Anayasa Mahkemesi
- `[AZ Anayasa Mah. — CODICES — {karar adı} — GG.AA.YYYY]` — CODICES üzerinden
- `[AZ İş Hukuku — NATLEX/ILO — {belge adı} — GG.AA.YYYY]` — ILO NATLEX

**Asla:** Çekmediğin Azerbaycan hukuku kaynağına atıf yapmış gibi davranma.
Azerbaycan hukukunu "biliyorum" diye `[AZ Mevzuat]` etiketi koyamazsın →
`[model bilgisi — doğrulayın]` kullan.

---

## Sınırlamalar

- **Dil:** Birincil kaynak Azerbaycan Türkçesi (Kiril değil, Latin alfabe). Türkçe
  bilen Claude için kısmen okunabilir ama kesin anlam için İngilizce versiyonu
  öncelikle kullan (minenergy.gov.az EN sayfası, NATLEX EN, CODICES EN).
- **İçtihat kısıtlı:** AZ iç mahkeme kararları (Yargıtay eşdeğeri — Ali Məhkəmə)
  yapısal olarak erişilebilir değil. Yalnızca Anayasa Mahkemesi kararları açıkta.
- **Güncellik / statü:** WebFetch yolunda `e-qanun.az` sayfası güncel olabilir
  ama **yürürlük statüsünü yapılandırılmış olarak vermez** — yürürlükten kalkmış
  bir aktı yürürlükteymiş gibi sunma riski buradadır. Statü için **e-qanun MCP →
  `az_get_act`** kullan.
- **İçtihat e-qanun MCP'de de yok** — cevap mahkemelerin uygulamasına dayanıyorsa
  "içtihat kontrol edilmedi" de, kontrol edilmiş gibi ima etme.
- **SSL:** `constcourt.gov.az` zaman zaman sorunlu → CODICES'e yönlen.
- **Makine çevirisi yok:** Otomatik çeviri kalitesi sınırlı; kritik hukuki metin
  için uzman tercüme şart. `[review]` flag ekle.

---

## [enerji şirketi] Azerbaycan hukuku kullanım disiplini

1. **[Azerbaycanlı enerji karşı tarafı] intra-group sözleşmeler** (ham petrol alım-satım, royalty, hizmet
   ücretleri) → Önce `governing-law` maddesini kontrol et. AZ hukuku seçildiyse
   → e-qanun.az (Medeni Kanun, Vergi Kanunu ilgili maddeleri).

2. **200+ Azerbaycanlı çalışan** → Azerbaycan'da istihdam edilenlerin hakları için
   NATLEX/ILO (Əmək Məcəlləsi). Türkiye'de çalışıyorlarsa Türk iş hukuku geçerli.

3. **Enerji sektörü düzenlemeleri** → minenergy.gov.az/en/qanunlar (EN) — [enerji şirketi]
   [ANA ORTAK MERKEZİ]'nün tabi olduğu AZ enerji rejimi anlayışı için.

4. **Anayasal haklar / mülkiyet sorunu** → CODICES (EN özetler güvenilir) →
   Gerekirse constcourt.gov.az.

5. **Dil notu:** [Azerbaycanlı enerji karşı tarafı] ile yazışma → `SYSTEM_PROMPT.md`: "AZ/EN ikili dil."
   Azerbaycan mevzuatından alıntı kullanılıyorsa AZ orijinal + EN çevirisi birlikte.

---

## Versiyon disiplini

- Bu rehber **v1.8.1** (*Azerbaycan Hukuku Entegrasyonu*) ile eklendi.
- **Paket v1.4.0'da kapsamı daraltıldı:** mevzuat okuma yolu
  `eqanun-mcp-rehberi.md`'ye taşındı; bu rehber içtihat + İngilizce kaynaklar +
  WebFetch yedekleri için kaldı. v1.3.1'deki "e-qanun.az anti-bot →
  cis-legislation.com" kısıtı, MCP resmî API'yi kullandığı için mevzuat
  tarafında geçerliliğini yitirdi.
- Kaynaklar 2026-05-30 tarihli ön araştırmaya dayanır (GitHub + web taraması).
- LocalDoc/allmalab HuggingFace dataset'lerinin erişilebilirliği değişebilir;
  WebFetch hedefleri (e-qanun.az, minenergy.gov.az) kararlıdır.

---

*Son güncelleme: 26.07.2026 — paket v1.4.0. Azerbaycan içtihadı + EN kaynaklar +
WebFetch yedekleri. Mevzuat için: `eqanun-mcp-rehberi.md` (BİRİNCİL).*
