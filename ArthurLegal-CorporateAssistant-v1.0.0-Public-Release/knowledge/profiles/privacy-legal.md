# Veri Koruma (KVKK + GDPR) – Pratik Profili (Türkiye Overlay)

> Hedef: `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`

---

## Kim olduğumuz

Bkz. `company-profile.md`. Bu eklentiye özel:

**Veri Sorumlusu mu Veri İşleyen mi:** Her ikisi.
- **Veri Sorumlusu:** Çalışan verileri ([DOLDUR — toplam çalışan sayısı]), müşteri verileri ([Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] milyonlarca doğal gaz abonesi), [Halka Açık İştirak]/[Rafineri Tesisi] müşteri ve tedarikçi verileri, web/marka/sosyal medya ziyaretçi verileri.
- **Veri İşleyen:** B2B müşteri verisinin işlenmesinde (Ticaret A.Ş., Enerji Ticaret A.Ş.) işleyen rolünde olabilir; intra-group veri akışında [Yurtdışı Ana Şirket] adına işlemler.
**VERBİS sicil kaydı:** **Her tüzel kişi için ayrı kayıt var** — ArthurLegal Holding A.Ş. + [Halka Açık İştirak] + [Rafineri Tesisi] + Terminal A.Ş. + Depolama A.Ş. + Enerji Ticaret A.Ş. + [Enerji Ticareti A] + [Halka Açık İştirak] RES + [Liman İştiraki] + [Elektrik İştiraki] (yeni — 2025) + diğer iştirakler her biri ayrı veri sorumlusu olarak kayıtlı. *Sicil numaraları kullanıcının VERBİS hesabından bireysel olarak çekilmeli — yıllık güncelleme zorunluluğu kapsamındadır.* **⚠️ [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] devri tamamlandı / tamamlanıyor — VERBİS'te bu sicillerin Şirket adına yenilenmemesi/devredilmesi gerekir; aboneye iletişim geçişi KVKK m. 8 aktarım koşullarını tetikler.**
**DPO yapısı:** **Tek merkezi DPO** — Hukuk, Uyum ve Kurumsal Yönetişim Başkanlığı bünyesinde. Tüm grup şirketleri merkezi ofisten yönetilir; her tüzel kişi için ayrı irtibat kişisi tek bir DPO ofisinin altındadır.
**Aylık ortalama DSAR (m.11 başvurusu):** [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] çıkışı sonrası **abone tabanlı yoğunluk büyük ölçüde azaldı**; ağırlıklı olarak çalışan başvuruları ([DOLDUR — toplam çalışan sayısı]) + B2B müşteri/tedarikçi + [Halka Açık İştirak] müşterileri kalıyor. Tahmin: aylık onlarca. Devir sürecindeki [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] başvuruları için **devralan şirkete yönlendirme + 1 yıl bilgilendirme yükümlülüğü** sürebilir.
**AB veri akışı var mı:** **EVET — TR → AB yoğun.** AB tedarikçiler (rafineri/petrokimya ekipmanı, IT/SaaS — Microsoft 365, SAP, cloud), AB müşteri ([Halka Açık İştirak] petrokimya ihracatı, AB enerji alıcıları), [Boru Hattı Projesi] üzerinden AB iletişimi (BOTAŞ, BP, Şirket, AzCo paydaş ekosistemi), AB kökenli ana ortak/ortak girişim geçmişi (örn. Şirket-BP). **Standart sözleşme + TIA (transfer impact assessment) zorunlu.** Ayrıca **TR → [Yabancı Ana Ortak Ülkesi] ([Yurtdışı Ana Şirket])** ana ortak veri aktarımı — [Yabancı Ana Ortak Ülkesi] yeterlilik kararı henüz YOK, açık rıza veya KVKK yeni m.9 SCC modeli kullanılmalı.
**Kullanılan veri işleyen sayısı (üçüncü taraf vendor):** Yüksek — IT/SaaS (Microsoft 365, SAP, vb.), bulut (muhtemelen Azure veya AWS), bordro/İK servis, çağrı merkezi, müşteri faturalama, ekipman bakım, vb. [DOLDUR — gerçek liste İK/IT/DPO'dan]
**DPO / İrtibat kişisi:** [DOLDUR — Hukuk, Uyum ve Kurumsal Yönetişim Başkanlığı ([CLCO]) bünyesinde olması muhtemel; her grup şirketi için ayrı veri sorumlusu irtibat noktası]

---

## İkili rejim: KVKK + GDPR

**KVKK (6698) — yerel zemin:**
- m. 4: İlkeler
- m. 5: Kişisel veri işleme şartları (rıza istisnaları)
- m. 6: Özel nitelikli veri (sağlık, biyometrik, ceza, sendika, etnik vs.)
- m. 8-9: Yurt içi/yurt dışı aktarım (2024 değişikliği)
- m. 10: Aydınlatma
- m. 11: İlgili kişi hakları
- m. 12: Veri güvenliği + ihlal bildirim (72 saat Kurul + ilgili kişi)
- m. 17: İdari para cezaları (2026 tutarları için Mevzuat MCP)

**GDPR — paralel rejim:**
- AB'de yerleşik müşteri, çalışan veya ziyaretçi verisi işliyorsanız UYGULANIR.
- Art. 27 — AB temsilcisi atama zorunluluğu (AB'de yerleşik değilseniz)
- Art. 33-34 — 72 saat ihlal bildirim
- Art. 44-50 — yurt dışı aktarım (SCC + TIA)

**Çakışma noktaları:**
- KVKK 2024 değişiklikleri yurt dışı aktarımı GDPR'a yaklaştırdı (BCR + ESCC + onaylı sertifika modelleri)
- KVKK'da "açık rıza" pratikte GDPR'dan daha sıkı — geri çekme + dengeli olmama riski
- Veri ihlal bildirim eşiği KVKK'da "hesaba katılır olasılık" → kabaca her ihlal Kurul'a; GDPR'da "yüksek risk" → kullanıcıya da bildirim
- KVKK Kurul kararları ışığında **biyometrik PDPS, kimlik fotokopisi** özel nitelikli sayılır — açık rıza şart

---

## Sıkça yapılan işler

### 1. İlgili kişi başvurusu (KVKK m. 11 — "DSAR")

- **30 gün süre.** Veri sorumlusunun başvuru formuna uygunluk reddi başvuru süresini durdurmaz.
- Tebligat: KEP, noter, güvenli e-posta (kayıtlı), veya yazılı.
- Ücretsiz; istisnai durumda Kurul belirler.
- Reddedilirse → Kurula şikayet (30 gün) → idari yargı (Ankara İdare Mahkemesi).
- Çıktı şablonu: `references/kvkk-m11-cevap-sablonu.md`

### 2. Veri İşleyen Sözleşmesi (DPA — m. 12)

Zorunlu unsurlar:
- Veri işleyenin işleme amacı/süresi/türü
- Veri sorumlusu talimatına uyma
- Gizlilik
- Teknik ve idari tedbirler (m. 12)
- Alt işleyen onayı
- Veri sorumlusuna yardım yükümlülüğü
- Sözleşme bitince veri silme/iade

### 3. PIA / VIA (Veri İşleme Etki Değerlendirmesi)

Türk hukukunda zorunlu DEĞİL ama Kurul "tavsiye" niteliğinde rehber yayınladı (2022, 2024). Yüksek riskli işleme (biyometrik, profil, büyük ölçek özel nitelikli) için yapın. GDPR Art. 35 DPIA paraleli — AB tarafı varsa zaten zorunlu.

### 4. VERBİS kaydı

- ≥50 çalışan VEYA yıllık ciro ≥25M TL VE özel kategorilerde veri işliyor mu → kayıt zorunlu
- Her veri kategorisi için: amaç, hukuki sebep, saklama süresi, alıcı grupları, yurt dışı aktarım
- **Yıllık güncellik kontrolü zorunlu** — değişiklik 30 gün içinde

### 5. Veri ihlal bildirimi (m. 12/5)

- 72 saat içinde Kurul'a (https://www.kvkk.gov.tr/ihlal-bildirim)
- Etki büyükse ilgili kişiye doğrudan
- Bildirim formu: olayın açıklaması, etkilenen veri kategorileri/sayısı, sonuçları, alınan tedbirler
- İhlal kaydı tutma yükümlülüğü (Kurul "Veri İhlali Bildirim Rehberi")

---

## Yurt dışı aktarım — 2024 sonrası

**Yeni rejim (m. 9 değiştirilmiş hali):**

1. **Yeterlilik kararı bulunan ülke** — Kurul listesinde (henüz yayınlanmadı)
2. **Uygun güvenceler:**
   - Standart sözleşme (Kurul tarafından ilan edilmiş şablon — 2024 yayında)
   - Bağlayıcı kurumsal kurallar (BCR — Kurul onaylı)
   - Onaylı sertifika
   - Onaylı davranış kuralı + taahhüt
3. **Arızi durumlar** — açık rıza, sözleşme ifası, kamu yararı, hak savunma vs.

**Pratik:** Çoğu kurumsal aktarım için **Standart Sözleşme + TIA (transfer etki değerlendirmesi)** kombinasyonu. ABD vendor'a aktarım (Microsoft, AWS, Google) için zorunlu.

---

## Çıktı standardı

Bkz. `commercial-legal.md`. Veri koruma özel:

- Her görüş çıktısında **hukuki sebep matrisi** tablosu (hangi m.5 / m.6 dayanağı)
- İhlal bildirimi taslaklarında **dakika dakika zaman çizelgesi**
- DSAR cevaplarında **m. 28 istisnaları** kontrol listesi (savunma hakkı, suç önleme vs.)

---

## Eskalasyon

- 🔴 Veri ihlali (≥1000 ilgili kişi VEYA özel nitelikli VEYA [Şehir Gazı Dağıtım A]/[Şehir Gazı Dağıtım B] abone verisi VEYA [Halka Açık İştirak] için içsel bilgi içeren) → Hukuk Başkanı ([CLCO]) + Bilgi Güvenliği + 24 saat içinde DPO toplantı + **72 saat içinde Kurul bildirim** + [Halka Açık İştirak] ile ilgiliyse KAP açıklama
- 🟠 DSAR'da çatışma (sır, başkasının verisi), Kurul ön incelemesi, **AB veri akışı standart sözleşme gözden geçirme** → Counsel
- 🟡 Standart DSAR cevabı, vendor DPA negotiation, VERBİS yıllık güncelleme → Sözleşmeler / DPO

---

## Mevzuat MCP kullanım örüntüleri

- `search_kanun(mevzuat_adi="6698")` — KVKK
- `search_kurum_yonetmelik(kurum="Kişisel")` — KVKK Yönetmelik
- `search_teblig(...)` — KVKK Kurul tebliğleri

## Yargı MCP kullanım örüntüleri (KVKK Kurulu kararları — emsal idari para cezaları)

- `search_kvkk_decisions(arananKelime="veri ihlali 72 saat bildirim")` — bildirim eşik kararları
- `search_kvkk_decisions(arananKelime="açık rıza geri çekme")` — rıza yönetimi emsali
- `search_kvkk_decisions(arananKelime="yurt dışı aktarım")` — yeni m. 9 uygulamaları
- `search_danistay_decisions(daire="10. Daire", arananKelime="KVKK idari para cezası")` — yargı temyizi
- `search_anayasa_bireysel_basvuru(arananKelime="özel hayat kişisel veri")` — anayasal boyut

Her atıfta `[Yargı MCP — kvkk-kurulu / danistay / aym — GG.AA.YYYY]` etiketi.
