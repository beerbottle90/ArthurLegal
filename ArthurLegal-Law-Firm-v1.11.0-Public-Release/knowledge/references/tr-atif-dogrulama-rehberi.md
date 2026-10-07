# Türk Yargı Kararı Künye Doğrulama Rehberi

> **Kural:** Bir yargı kararının künyesi (mahkeme veya daire, esas, karar, tarih) bu sohbette ArthurLegal araçlarıyla
> bulunmadıkça metne yazılmaz. Bulunamayan künye **"doğrulanmadı"** diye işaretlenir; tamamlanmaz, düzeltilmez,
> tahmin edilmez. Bu, SYSTEM_PROMPT bölüm 4'teki madde doğrulama kapısının içtihat karşılığıdır.
>
> Uygulama skill'i: `/legal-research:tr-atif-dogrulama`. Yöntem 24.09.2026'da ArthurLegal MCP'nin canlı ucunda
> denendi; aşağıdaki davranışlar o denemeden. ABD karşılığı: `abd-atif-dogrulama-rehberi.md`.

---

## Neden

Dil modelinin en tehlikeli hatası biçimce kusursuz ama var olmayan künyedir. Denemede görülen bozulma tipleri:

| Tip | Örnek | Neden tehlikeli |
|---|---|---|
| Doğru numara, yanlış tarih | E. ve K. doğru, tarih bir ay kaymış | Numara araması "buldum" der; tarih bakılmazsa hata geçer |
| Doğru numara, yanlış daire | 12. Hukuk Dairesi kararı "14. Hukuk Dairesi" diye | Her dairenin numaralandırması ayrıdır; aynı numara başka dairede başka karardır |
| Esas ve karar numarası farklı kararlardan | Aynı gün aynı kurulda iki karar; E. birinden, K. ötekinden | Yalnız esas numarası eşleşir, künye yine yanlıştır |
| Başvuru numarası doğru, tarih yanlış | AYM bireysel başvuru | Başvuru bulunur, tarih tutmaz |

**Yalnız esas numarasının bulunması doğrulama değildir.** Künyenin bütün unsurları aynı kayıtta birlikte eşleşmelidir.

---

## Hangi mahkeme, hangi araç

| Mahkeme | Künye unsurları | Araç |
|---|---|---|
| Yargıtay (HD, CD, HGK, CGK), Danıştay (daireler, İDDK, VDDK), BAM (istinaf hukuk), yerel hukuk, KYB | daire veya kurul + E. + K. + karar tarihi | `tr_ictihat_ara` → (içerik gerekiyorsa) `tr_ictihat_getir` |
| AYM bireysel başvuru | B. No + karar tarihi | `tr_aym_ara(kind="bireysel")` |
| AYM norm denetimi | E. + K. + karar tarihi + konu (kanun ve madde) | `tr_aym_ara(kind="norm")` |
| Uyuşmazlık Mahkemesi | E. + K. + tarih | `tr_uyusmazlik_ara(scope="EsasNo")` |
| Düzenleyici kurum kararı (Rekabet, EPDK, SPK, BDDK, KVKK, BTK) | kurum + karar no + tarih | `tr_kurum_karari_ara(kurum=…, decision_no=…)` (bu rehberde denenmedi) |

---

## Yöntem — Yargıtay, Danıştay, BAM (Bedesten)

1. **Ayrıştır.** Daire kodu: Yargıtay 9. Hukuk Dairesi → `H9`, 3. Ceza Dairesi → `C3`, Hukuk Genel Kurulu → `HGK`,
   Ceza Genel Kurulu → `CGK`; Danıştay 13. Daire → `D13`, `VDDK`, `IDDK`. BAM için `courts=["ISTINAFHUKUK"]` ve
   `chamber` alanına tam ad yazılır: `"İstanbul Bölge Adliye Mahkemesi 12. Hukuk Dairesi"`.
2. **Sorgu olarak numaranın yalnız sıra kısmını ver.** "2024/13727" → `query="13727"`.
   - Bedesten sorgusunda "/" kabul edilmez: `"2024/13727"` hata döner ("Sadece harf ve rakam içeren aramalar yapılabilir").
   - `"2024 13727"` gibi iki parçalı sorgu binlerce ilgisiz sonuç döndürür.
   - Sıra no sorgusu hem esas hem karar numarası alanında eşleşir; bu yüzden sonuçtaki her iki alana da bakılır.
3. **Süzgeç:** `chamber` = daire kodu; `date_from` = `date_to` = künyedeki karar tarihi (YYYY-MM-DD).
4. **Karşılaştır:** sonuçtaki `esas_no`, `karar_no` ve `karar_tarihi` **üçü birden** künyeyle aynıysa → **DOĞRULANDI**.
   Metne yanıttaki `citation` alanı birebir yazılır.
5. **Sonuç yoksa ya da üçü birden tutmuyorsa:**
   - a) Tarih aralığını genişlet (karar yılı ile bir sonraki yıl) ve aynı sorguyu tekrarla. Aynı esas farklı karar
     numarası veya tarihle çıkarsa künye **hatalıdır**.
   - b) Karar numarasının sıra kısmıyla da ara.
   - c) Daire şüpheliyse `chamber` süzgecini kaldırıp tarih süzgeciyle ara.
6. **Hiçbiri tutmazsa → DOĞRULANMADI.** Künye metinde kullanılmaz; yazılması gerekiyorsa hemen ardından `UYARI: veri çekilemedi, teyidiniz gerekli:
   <bağlantı>` yazılır ve künye İnceleme notunda adıyla gösterilir.
7. Kayıtta farklı bir künye bulunduysa ("aynı esas, tarih 17.12.2024") bunu **kendiliğinden düzeltip doğru künye gibi
   kullanma**. Avukata göster: "verilen künye bulunamadı; kayıtta aynı esasın künyesi şu". Hangi kararın kastedildiğine
   avukat karar verir.

**Tuzak (24.09.2026'da görüldü):** Danıştay VDDK aynı gün (24.12.2025) çok sayıda karar verdi; E. 2024/1073'ün kararı
K. 2025/1128, E. 2024/49'unki K. 2025/1130. "VDDK, E. 2024/1073, K. 2025/1130, 24.12.2025" künyesinde esas da tarih
de kayıtta vardır, ama künye **yanlıştır**: K. 2025/1130 başka bir esasa aittir. Esas eşleşmesine bakıp durmak bu
hatayı kaçırır.

---

## Yöntem — Anayasa Mahkemesi

- **Bireysel başvuru:** `tr_aym_ara(kind="bireysel", query="2013/1821")` başvuru numarasıyla doğrudan bulur.
  `basvuru_no` ve `karar_tarihi` künyeyle aynı olmalıdır.
- **Norm denetimi:** `tr_aym_ara` esas veya karar numarasıyla **bulmaz**. Denemede "2019/…" ve "E.… K.…" biçimindeki
  numara sorguları ilgisiz sonuç döndürdü. Konuyla ara: kanun adı veya numarası + madde
  (`"4721 sayılı Türk Medeni Kanunu 161. madde"`). Sonuçtaki `esas_no`, `karar_no` ve `karar_tarihi`
  künyeyle karşılaştırılır. Konu bilinmiyorsa ve numara bulunamıyorsa → **DOĞRULANMADI**.
- AYM tarihleri araçta YYYY-MM-DD biçiminde döner; karşılaştırırken biçimi çevir.

## Yöntem — Uyuşmazlık Mahkemesi

`tr_uyusmazlik_ara(query="2025/483", scope="EsasNo")` esas numarasıyla doğrudan bulur; `scope="KararNo"` karar
numarasıyla arar. Tarih araçta GG/AA/YYYY biçimindedir.

---

## Çıktıda gösterim

- **Doğrulanan:** `[ArthurLegal TR — <citation alanı birebir> — GG.AA.YYYY çekim]`
- **Doğrulanamayan:** `[doğrulanmadı — verilen künye: …]`
- **İnceleme notu**, tek cümle, "İçtihat kontrolü:" ile başlar: "İçtihat kontrolü: Yargıtay 9. HD E. 2024/13727,
  K. 2024/16274 bulundu; karşı taraf dilekçesindeki 'Yargıtay 9. HD E. 2024/12332, 17.11.2024' künyesi bulunamadı,
  kayıtta aynı esasın tarihi 17.12.2024."
- Kararın **içeriği** (ne dediği) ayrıca `tr_ictihat_getir` ile okunmadan karara hüküm veya gerekçe yüklenmez. Künyeyi
  doğrulamak, kararın o sonucu söylediğini doğrulamak değildir.

---

## Sınırlar

- Bedesten her kararı içermez. Bulunamamak "karar yok" demek değildir; **"doğrulanmadı"** demektir.
- Hız sınırı: 30 saniyede 10 istek, mevzuat ve içtihat araçlarında ortak. Aynı turda en çok 5 çağrı gönder;
  `retry: true` gelirse birkaç saniye bekle.
- Kararın kesinleşip kesinleşmediği `kesinlesme` alanında görünebilir; alan boşsa kesinleşme doğrulanmış değildir.
