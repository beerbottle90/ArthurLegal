---
name: litigation-legal-isg-incident-response
description: >
  İSG (iş sağlığı güvenliği) veya çevre olayı sonrası ilk 24-72 saat runbook'u —
  büyük endüstriyel tesis gibi yüksek riskli tesislerde ölümlü/ciddi kaza
  sonrası hukuk müşavirinin ATMASI gereken adımlar: delil koruma, savcılık beklenti
  planlaması, çalışan vekalet teklifi, dış vekil + crisis comms tetikleyici, EPDK/
  Çevre Bakanlığı/KAP bildirim takvimi, üst yönetim eskalasyon zinciri.
user-invocable: true
---

# İSG / Çevre Olayı — İlk 24-72 Saat Runbook

> **⚠️ Bu skill [Müvekkil] için yakıcı sorun olarak işaretlenmiştir.** büyük endüstriyel tesisnde geçmişte ölümlü/ciddi kaza dosyaları yaşandı; her olayda doğru ilk müdahale tazminat tutarını, ceza dosyasının yönünü ve EPDK lisans riskini doğrudan etkiler.

## ⚠️ KAP açıklama tetik haritası — [RAFİNERİ] vs [HALKA AÇIK İŞTİRAK] ayrımı (KRİTİK)

Olay hangi tüzel kişinin tesisinde / faaliyet alanında oldu, ona göre KAP yükümlülüğü değişir:

| Tüzel kişi | Halka açık mı? | KAP açıklama doğrudan? |
|---|---|---|
| **[halka açık iştirak]** | ✅ **EVET (BIST: [ticker])** | **DOĞRUDAN — SPK Tebliğ II-15.1 m. 5 "önemli olay"** |
| **[büyük enerji tesisi] A.Ş.** | ❌ Hayır ([Müvekkil] Rafineri A.Ş.'ye bağlı) | Doğrudan değil — ancak **[HALKA AÇIK İŞTİRAK] ile entegre operasyon etkisi varsa [HALKA AÇIK İŞTİRAK] üzerinden dolaylı KAP** |
| **[Müvekkil]** (holding) | ❌ Hayır | Doğrudan değil |
| **[Müvekkil] Depolama / Terminal / Enerji Ticaret** | ❌ Hayır | Doğrudan değil |
| **[enerji üretim tesisi]** | ❌ Hayır | EPDK bildirim, KAP değil |
| **[DAĞITIM İŞTİRAKİ]** | ❌ Hayır | KAP değil; etki [HALKA AÇIK İŞTİRAK]'e yansıyorsa dolaylı |

**Karar matrisi:**

1. Olay **[HALKA AÇIK İŞTİRAK] tesisinde** veya **[HALKA AÇIK İŞTİRAK] faaliyetiyle doğrudan ilgili** mi? → **KAP açıklama derhal** (Yatırımcı İlişkileri + [HALKA AÇIK İŞTİRAK] YK Sekreterya)
2. Olay **[RAFİNERİ]/[Müvekkil]-bağlı şirkette** ama **[HALKA AÇIK İŞTİRAK] üretim/satış zincirini etkiliyor** mu? (örn. [RAFİNERİ]'dan etilen tedariki kesilirse [HALKA AÇIK İŞTİRAK] üretimini durdurur) → **[HALKA AÇIK İŞTİRAK] üzerinden dolaylı KAP değerlendirmesi** — Yatırımcı İlişkileri ile materyalite testi
3. Olay **[RAFİNERİ]/[Müvekkil]-bağlı** ama **[HALKA AÇIK İŞTİRAK]'i etkilemiyor** → KAP açıklama **N/A**, sadece iç eskalasyon + basın koordinasyonu

**[Müvekkil] uygulama:** "[HALKA AÇIK İŞTİRAK] etkisi yok ise KAP N/A" kararı **yazılı dokümante edilmeli** (sonradan SPK denetiminde gerekçe olarak gösterilir). IR Başkanlığı + Hukuk ortak imzalı not.

---

## Matter context

Matter workspaces ON. İSG olayı yeni bir matter'dır:

> Bu yeni bir İSG/çevre olayı. Dosya açayım mı? Slug: `isg-YYYY-MM-DD-[tesis]`). Cevap: evet/hayır/manuel slug.

## Destination check

Bu skill çıktısının iki ayrı versiyonu olur — destinasyona göre seç:

| Destinasyon | Versiyon |
|---|---|
| **İçeride hukuk müşavirliği + dış vekil (gizlilik içinde)** | Tam runbook, Avukatlık K. m. 36 üst başlığı |
| **Operasyonel yönetim (tesis müdürü, ISG, HSE) bilgi notu** | "Hukuki riskler & bildirim takvimi" kısaltılmış versiyon, hukuki strateji çıkar |
| **CEO/YK eskalasyon notu** | 1 sayfa executive summary + decision points |
| **KAP açıklama metni (halka açık iştirak ilgili ise)** | Ayrı bir çıktı; bu skill başlatır, son halini SPK uzman avukat onayı sonrası |

## Olayın ciddiyet ataması (SEVERITY)

İlk olarak kullanıcıya sor:

```
Olayın seviyesi nedir?
A. 🔴 ÖLÜMLÜ veya ÇOK CİDDİ — bir veya birden fazla ölü, kalıcı sakatlık, büyük çevre kirlenmesi, basında haber
B. 🟠 CİDDİ — hastane sevki, üretim duruş, lokal çevre etki
C. 🟡 ORTA — yaralanma var ama ayakta tedavi, üretim devam, sınırlı etki
D. 🟢 KÜÇÜK — ramak kala, hafif yaralanma, raporlama amaçlı

Hangisi?
```

Cevaba göre **runbook ölçeği değişir.** A/B = tam runbook, C = sadeleştirilmiş, D = sadece raporlama checklist.

---

## TAM RUNBOOK (A/B seviyesi için)

### ⏰ İLK 1 SAAT

> **Hedef:** Kanıtların korunduğundan emin ol; üst yönetim haberdar olsun; dış vekil yola çıksın.

#### 1. Olay yeri delil koruma (KRİTİK)

**Hukuki temel:** TCK m. 281 (suç delillerini yok etme); CMK m. 161 (savcılığın delil isteme yetkisi); 6331 İSG K. m. 14 (raporlama).

Operasyonel ekibe (tesis müdürü, ISG uzmanı) **derhal iletilmesi gereken yönergeler:**

- [ ] **Olay yerini KORU** — kazadan etkilenen alana giriş kısıtlansın, fotoğraf ve video ile tüm haliyle belgelendir
- [ ] **Kamera kayıtları YEDEKLE** — kazadan önce/sonra 24 saatlik kamera kayıtları **derhal** ayrı diske kopyalansın (genelde sistem 7-30 gün geriye dönüşlü; geç kalınırsa silinir)
- [ ] **Vardiya defteri, kontrol listeleri, iş emirleri, JSA (Job Safety Analysis)** — kazaya yol açan süreçle ilgili tüm belgeler **kopyalanıp asıllar arşivlensin**
- [ ] **İlgili çalışanların eğitim dosyaları, sertifikalar, periyodik sağlık raporları, vardiya çizelgeleri** — savcılık talep etmeden hazırlansın
- [ ] **Olay öncesi 30 günlük HSE raporu / yakın kaza (near miss) raporları** — pattern olarak gelebilir
- [ ] **Olay yerine giren her kişi, saat saat log** — savcılık delil ihlali iddiasını önler

#### 2. Bildirimler (KANUNİ ZORUNLU)

| Kuruma | Yasal süre | Kim | Nasıl |
|---|---|---|---|
| **SGK** (iş kazası bildirimi) | 3 iş günü | İşveren | EBYS / SGK portalı |
| **Çalışma ve Sosyal Güvenlik Bakanlığı** | Kanunda süreli bildirim yok — 6331 m. 14/2 bildirimi SGK'ya yapılır | — | — |
| **Polise/Savcılığa** (ölümlü/ciddi yaralanma) | DERHAL | İşveren / 112 | Telefon + yazılı tutanak |
| **Çevre Bakanlığı** (çevre etkisi varsa) | DERHAL | Tesis müdürü | İl Çevre Müdürlüğü + telefon |
| **EPDK** (lisansa konu tesisin durması) | 24 saat (lisans şartlarına göre) | Lisans sahibi | EPDK portal + yazılı |
| **AKUT/AFAD** (büyük çevre / sosyal etki) | DERHAL | İl Acil Durum | — |
| **KAP** (halka açık iştirak ilgili önemli olay) | DERHAL özel durum açıklaması | [HALKA AÇIK İŞTİRAK] | KAP üzerinden, SPK Tebliğ II-15.1 |
| **[BORU HATTI PROJESİ]** ([BORU HATTI PROJESİ] altyapı etkilendiyse) | 24 saat | İşletmeci | [BORU HATTI PROJESİ] işletme sözleşmesi |

⚠️ Bu süreler **yasal**, gecikme idari para cezası + ceza dosyasında ağırlatıcı.

#### 3. Üst yönetim eskalasyon zinciri

| Saat | Kim haberdar olmalı | Nasıl |
|---|---|---|
| 0-15 dk | Tesis müdürü, ISG uzmanı, HSE Başkanı | Telefon |
| 15-30 dk | İş Birimi Başkanı ([İş Birimi Başkanı] — [enerji tesisi]; veya [İş Birimi Başkanı] — doğal gaz) | Telefon |
| 30-60 dk | **Hukuk Direktörü** (Group GC) → **Hukuk Başkanı ([CLCO / GC])** → **CEO ([CEO])** | Telefon zinciri |
| 60-90 dk | İletişim Başkanlığı ([İletişim Başkanlığı]) — basın hazırlık | Telefon + brief |
| 90 dk - 2 saat | Compliance + Yatırımcı İlişkileri ([HALKA AÇIK İŞTİRAK] ise) | E-posta + telefon |

`firm-profile.md` anahtar kişiler tablosunu kontrol et — son atamalar değişebilir.

#### 4. Dış vekil mobilizasyonu

- [ ] **İSG/iş kazası uzmanı dış vekil** derhal aranır — `practice profile → outside counsel paneli → İSG / iş kazası` ([TESİS LOKASYONU] için yerel firma kritik; İstanbul'dan sadece koordinasyon)
- [ ] **Ceza avukatı** — vekalet hazırlanır, ilgili olabilecek yöneticiler (tesis müdürü, ISG uzmanı) için **müdafilik onay formu** alınır
- [ ] **Çevre uzmanı dış vekil** (çevre etkisi varsa)
- [ ] **Sermaye piyasası uzmanı dış vekil** ([HALKA AÇIK İŞTİRAK] ise)

### ⏰ İLK 24 SAAT

> **Hedef:** Savcılık geliş anına hazır ol; çalışan haklarını koru; resmi bildirimler tamamla; iletişim koordine et.

#### 5. Savcılık beklenti planlaması

**CMK m. 153 — müdafiin dosyayı inceleme yetkisi (ve hâkim kararıyla kısıtlanması):** Sanık vekili olarak resmen atanmadan, savcılık dosyasına tam erişim YOK. Bu nedenle:

- [ ] Ceza avukatı olabilecek müdafilerin **derhal vekalet ile sanık adayı yöneticiler için** atanması
- [ ] **Yöneticilere "ifade verme hakkı"** hatırlatılır:
  - Şüpheli sıfatıyla ifade verirken (CMK m. 147) **susma hakkı** var (m. 147/1-e)
  - Kendisini suçlayan beyanda bulunmaya/delil göstermeye zorlanamama (Anayasa m. 38/5); lehine delil toplanmasını isteme (CMK m. 147/1-f)
  - Müdafi olmadan ifade vermemesi şiddetle önerilir
- [ ] İçeriği bilinmeyen tutanak / ifade tutanağına **imza atılmaması** önerisi

#### 6. Çalışan tarafı koordinasyon

- [ ] **Mağdur ailesi ile İK + İletişim koordineli** — taziye + acil destek (PR ve hukuki risk dengeli)
- [ ] **Diğer çalışan ifadeleri** — ısrarcı tanık ifadesi tutarsızlık doğurabilir, **avukat eşliğinde** verilmeli
- [ ] **Sendika ile koordinasyon** ([SEKTÖR SENDİKASI] başta) — TİS hükümleri + çalışan hakları
- [ ] Mağdur ailesinin **kendi vekili yoksa**, "size avukat öneririz" deme — etik sorun + savunmada zayıflık

#### 7. Belge / yazışma kontrol

- [ ] Olaya ilişkin **iç yazışmalar** (e-posta, Teams) — privilege/gizlilik kapsamı NETLEŞTİR (bkz. Avukatlık K. m. 36 sınırı in-house için)
- [ ] **"Olay anı" e-postaları** — kontrolsüz "biz suçluyuz" tarzı yazışmalar olabilir, hukuk bunu yönetilebilir formata çevirir
- [ ] Tüm operasyonel yazışmalar artık **avukat aracılığıyla** yapılır mesajı geçilir

#### 8. İletişim (basın, sosyal medya, yatırımcı)

- [ ] **Basın bildirisi** — İletişim Başkanlığı + Hukuk koordineli
  - Empati + sorumluluk kabul vs. soğukkanlı bilgi verme dengesi
  - "Sorumluluğu kabul ediyoruz" demek hukuki sorumluluğu artırabilir
  - "Sebepleri araştırıyoruz" güvenli formül
- [ ] **Sosyal medya monitoring** — yanıltıcı/abartılı haberlere düzeltme
- [ ] **KAP açıklaması** ([HALKA AÇIK İŞTİRAK] ise) — finansal etki + üretim duruş açıklanır

### ⏰ İLK 72 SAAT

> **Hedef:** Tablo netleşir; strateji sabitlenir; bildirimler tamamlanır.

#### 9. Olay raporu inceleme

- [ ] **İlk olay raporu (HSE/ISG uzmanı tarafından)** — hukukun gözüyle değerlendir, yanlış yorum veya zayıf nokta düzeltilsin
- [ ] **Bağımsız uzman keşfi** (kendi tarafımız) — bilirkişi ön-değerlendirmesi gerekir mi?
- [ ] **Operasyonel düzeltici aksiyon** — tekrar olmaması için derhal alınan tedbirler dökümante edilir (bu sonraki davalarda "öğrendiğimiz dersler" olarak savunmada kullanılır)

#### 10. Stratejik karar — dava beklentisi

- **Mağdur tarafı tazminat davası açar mı?** (1-2 yıl içinde muhtemel)
- **Savcılık ceza davası açacak mı?** (CMK m. 170 vd. — iddianame değerlendirme süreci)
- **Çevre Bakanlığı idari para cezası kesilecek mi?** (tebliğden itibaren 30 gün içinde idare mahkemesinde dava — Çevre K. m. 25; dava tahsili durdurmaz)
- **EPDK lisans askıya alma yapacak mı?** (lisans hükümleri + EPDK kurul kararı süreci)

Her biri için ön-strateji:
- Sulh hazırlığı (mağdurla aktif veya tazminat fonu)
- Ceza savunması (taksir derecesi argümantı, fail-vendor/altışveren ayırımı)
- İdari ceza itirazı (idare mahkemesi, 30 gün — Çevre K. m. 25)
- EPDK lisans savunması (düzeltici aksiyon ispatı)

#### 11. ArthurLegal MCP (`tr_`) — emsal kararlar

```
tr_ictihat_ara(
  courts=["YARGITAYKARARI"],
  query="+iş +kazası +ölümlü +6331 +işveren +sorumluluk",
  chamber="H9",  # iş kazası tazminat
  date_from="2023-01-01"
)

tr_ictihat_ara(
  query="+taksirle +öldürme +rafineri +patlama +yönetici +sorumluluk",
  date_from="2020-01-01"
)  # Ceza Genel Kurulu kararları

tr_ictihat_ara(
  courts=["DANISTAYKARAR"],
  chamber="D10",
  query="+çevre +kirletme +idari +para +cezası +iptali",
  date_from="2023-01-01"
)
```

Bu emsal kararlar mağdur/savcılık/çevre bakanlığı eğilimini gösterir; strateji buna göre.

---

## SADELEŞTİRİLMİŞ RUNBOOK (C seviyesi için)

C = orta seviye olay. Tam runbook'un alt-kümesi:
- Delil koruma (1, 7)
- Yasal bildirimler (2)
- Hukuk Direktörü eskalasyon (3 — sadece Counsel + Direktör)
- Dış vekil mobilizasyon (4 — sadece İSG uzmanı)
- Olay raporu inceleme (9)

Üst yönetim eskalasyon, basın koordinasyon, KAP açıklaması GENELDE gerekmez (halka açık iştirak ilgili değilse).

## SADECE RAPORLAMA (D seviyesi için)

D = küçük olay / ramak kala. Bildirim checklist + iç dosyalama yeterli:
- SGK 3 iş günü
- HSE iç raporu
- Düzeltici aksiyon takip
- Hukuk müşavirliği bilgi notu (Counsel arşivine)

---

## Çıktı şablonu

```markdown
[ÜST BAŞLIK — practice profile ## Outputs'tan]

# İSG/Çevre Olayı Runbook — [Olay slug / Tesis / Tarih]

## ⚠️ İnceleyen notu
- **Olay seviyesi:** 🔴/🟠/🟡/🟢
- **Tetiklenen runbook:** Tam / Sadeleştirilmiş / Sadece raporlama
- **Kaynaklar:** ArthurLegal MCP (`tr_`) [✓ N emsal / not yet]; ArthurLegal MCP (`tr_`) [✓ X madde]
- **Acil aksiyonlar (sonraki 1 saat):** [liste]
- **Acil aksiyonlar (sonraki 24 saat):** [liste]
- **KAP açıklama:** [N/A / hazırlanıyor / tamamlandı]
- **Eskalasyon zinciri tetiklendi:** [evet, son durağı: ...]

---

## 🚨 SONRAKI 1 SAAT

[Checklist - ☐ formatında]

## ⏰ SONRAKI 24 SAAT

[Checklist + sorumlular]

## ⏰ SONRAKI 72 SAAT

[Checklist + stratejik kararlar]

## Yasal bildirimler tablosu

[tablo — kim, ne zaman, kime, nasıl]

## Eskalasyon zinciri ([Müvekkil])

[Saat saat kim bilgilendirildi]

## Dış vekil mobilizasyonu

| Pratik alan | Büro | İletişim | Durum |
|---|---|---|---|
| İSG/iş kazası | [...] | [...] | mobilize edildi/edilmedi |
| Ceza | [...] | [...] | [...] |
| Çevre | [...] | [...] | [...] |
| KAP/SPK | [...] (halka açık iştirak ilgili ise) | [...] | [...] |

## Emsal içtihat (ArthurLegal MCP (`tr_`))

[İlgili Yargıtay/Danıştay emsal kararları]

## Stratejik karar matrisi

| Risk vektörü | Olasılık | Etki | Hazırlık |
|---|---|---|---|
| Tazminat davası | Yüksek/Orta/Düşük | [$X-Y aralık] | [...] |
| Ceza davası | [...] | [yöneticiler için] | [...] |
| Çevre idari ceza | [...] | [...] | [...] |
| EPDK lisans riski | [...] | [...] | [...] |

## Sonraki adımlar (decision tree)

> **What next? Pick one and I'll help you build it out:**
> 1. **İlk basın bildirisi taslağı** — İletişim ile koordineli
> 2. **CEO eskalasyon notu** — 1 sayfa
> 3. **KAP açıklama metni** — [HALKA AÇIK İŞTİRAK] için
> 4. **Dış vekil brief'i** — `/arthurlegal:litigation-legal-outside-counsel-brief`
> 5. **Bekle ve izle** — 24 saat sonra revize et

**One question I'd ask that isn't in my checklist:** [örn. "Mağdur ailesinin sosyal medyasında ne paylaşılıyor? Hukuki argümanı doğrudan etkileyen bir görüntü/itham var mı?"]
```

## Hatalı kullanım

- **"Küçük bir kaza, runbook gerek yok" diye atlama** — D seviyesi runbook'u en azından çağrılmalı; ramak kala olay listesi sonraki davada pattern olarak kullanılır.
- **"Sorumluluğu hemen kabul edelim" → savcılığın işini kolaylaştırır.** "Sebepleri araştırıyoruz" güvenli formül.
- **Çalışana "imzala" deme** — savunma hakkı ihlal edilebilir, sonraki davada baş ağrısı.
- **KAP'ı atlama** ([HALKA AÇIK İŞTİRAK] ise) — SPK yaptırımı + yatırımcı davası açar.

## Reviewer note

Bu skill çalıştığında **Hukuk Direktörü** ve **Hukuk Başkanı** otomatik bilgilendirme listesine eklenir (`outputs/escalation-notification.md` taslağı üretilir).

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
| Turk doktrini (DergiPark 19 hukuk dergisi) + karsilastirmali ogreti — **ikincil**; bir karar kademesini yukseltmez | `/arthurlegal:legal-research-karsilastirmali-doktrin` |
| uyusmazlik AZ hukukuna tabiyse akt + statu. **AZ ictihadi bu araclarda YOK** — `azerbaycan-hukuk-rehberi.md` | `/arthurlegal:legal-research-az-mevzuat` |

Rehberler: `${CLAUDE_PLUGIN_ROOT}/references/eqanun-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/lex-scholar-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/resourcecontracts-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/karsilastirmali-hukuk-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/nl-rechtspraak-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/pl-sejm-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/at-ris-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/ie-statutebook-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/fi-finlex-mcp-rehberi.md` · `${CLAUDE_PLUGIN_ROOT}/references/es-boe-mcp-rehberi.md`
