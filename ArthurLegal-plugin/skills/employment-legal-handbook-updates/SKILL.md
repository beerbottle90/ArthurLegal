---
name: employment-legal-handbook-updates
description: >
  Personel yönetmeliği / çalışan el kitabı değişikliğini mevcut sürümle
  karşılaştırır; çapraz atıf kırılmalarını, ülke/işyeri/TİS eklerine etkisini
  ve işçi aleyhine esaslı değişiklik riskini (İş K. m. 22: yazılı bildirim, 6
  iş günü içinde yazılı kabul, geçmişe etkisizlik) işaretler. "El kitabını
  güncelle", "bunu yönetmeliğe ekle", "personel yönetmeliği değişikliği"
  denince ya da yerleştirilmeye hazır bir politika olduğunda kullan.
---

# /handbook-updates — Personel Yönetmeliği Güncellemesi

El kitabı değişikliğinin dalga etkisi vardır: yıllık izin bölümünü değiştirirsin, fesihteki izin ücreti hesabı, izin politikası atfı ve iki işyeri eki etkilenir. Türk hukukunda bir de m. 22 boyutu vardır: personel yönetmeliği iş sözleşmesinin eki niteliğinde olabilir ve işçi aleyhine esaslı değişiklik tek taraflı yapılamaz. Bu skill dalgaları tutarsızlığa dönüşmeden bulur.

## Bağlamı yükle

`firm-profile.md` ve `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → el kitabı/personel yönetmeliği yeri, ekler listesi (ülke/işyeri/TİS), güncelleme sıklığı.

**Matter bağlamı.** Eklenti ayarında `## Matter workspaces` → `Enabled` `✗` ise bu paragrafı atla. Etkinse ve aktif matter yoksa sor: "Bu hangi matter için? `/arthurlegal:employment-legal-matter-workspace switch <slug>` çalıştırın ya da `practice-level` deyin." Aktif matter'ın `matter.md` dosyasını yükle; çıktıları `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/` altına yaz. `Cross-matter context` `on` değilse başka matter'ın dosyasını okuma.

## Adımlar

### 1. Değişikliği al

- Hangi bölüm değişiyor? Yeni metin ne?
- Neden: kanuni zorunluluk (hangi madde, hangi değişiklik), şirket kararı, temizlik?
- Kimlere uygulanacak; yürürlük tarihi ne?

### 2. Mevcutla karşılaştır

```diff
- [eski metin]
+ [yeni metin]
```

Değişiklik bir kanun değişikliğine dayanıyorsa ilgili maddeyi `tr_mevzuat_madde_getir` ile çek ve madde metnindeki değişiklik notunu (tarih, değiştiren kanun) yaz. Örnek: analık izni ve babalık izni süreleri 2026'da değişti (4857 m. 74 ve ek m. 2'deki değişiklik notları) — eski sürelerle kalmış bölümleri ara.

### 3. Çapraz atıfları bul

- Bu bölüme atıf yapan diğer politikalar ("izin süreleri için bkz. ...")
- Bu bölümün tanımladığı ya da kullandığı tanımlı terimler
- Bu bölümü değiştiren ekler
- İş sözleşmesi şablonu ve teklif mektubu şablonundaki atıflar

Her atıf değişiklikten sonra hâlâ doğru mu? Kırılanı işaretle.

### 4. Eklere etkisi

Eklenti ayarındaki her ülke/işyeri/TİS eki için:
- Ek, değişen bölümü değiştiriyor mu?
- Değişiklik eki eskitiyor, yanlış ya da eksik bırakıyor mu?
- Daha önce ek gerektirmeyen bir yerde yeni ek gerekiyor mu? (Türkiye dışı ülke için kural ezberden yazılmaz; ilgili önekle ara: `eu_`, `uk_`, `de_`, `nl_`, `az_` …; listede olmayan ülke: "ArthurLegal'da bu ülkenin kaynağı yok; yerel hukukçu görüşü al.")
- TİS'li işyerinde yeni metin TİS hükmüyle çatışıyor mu?

### 5. Söz kontrolü — İş K. m. 22

Değişiklik eski sürümün verdiği bir şeyi azaltıyor mu?

- Personel yönetmeliği, iş sözleşmesi ya da işyeri uygulamasıyla oluşan çalışma koşullarında **esaslı değişiklik** ancak işçiye **yazılı bildirimle** yapılabilir; işçi **6 iş günü** içinde yazılı kabul etmezse değişiklik onu bağlamaz (m. 22/1).
- Kabul edilmezse işveren, değişikliğin geçerli nedene dayandığını ya da başka geçerli fesih nedeni olduğunu yazılı açıklayıp bildirim süresine uyarak feshedebilir; işçi m. 17–21'e göre dava açabilir (m. 22/1).
- Taraflar anlaşarak her zaman değiştirebilir; değişiklik **geçmişe etkili** yürürlüğe konamaz (m. 22/2).
- Neyin "esaslı" sayıldığı ve işyeri uygulamasının ne zaman çalışma koşulu hâline geldiği **tartışmalı — içtihadı kontrol et**.
- İşçi lehine değişiklikler ve salt düzenleme/talimat niteliğindeki kurallar (TBK m. 399) için yazılı kabul gerekmez; yine de duyuru ve imza kaydı tut.

Engelleme; ama işaretle ve hangi çalışan grubunun yazılı kabulünün gerektiğini yaz.

### 6. Yan yükümlülükler

- **KVKK:** değişiklik yeni bir kişisel veri işlemesi getiriyorsa aydınlatma metni güncellenir (6698 m. 10).
- **İSG:** risk ya da çalışma yöntemi değişiyorsa çalışanlar bilgilendirilir, gerekiyorsa eğitim yenilenir (6331 m. 16, m. 17).

### 7. ArthurLegal MCP (`tr_`)

```
tr_mevzuat_madde_getir(number="4857", madde_no="22")
tr_mevzuat_madde_getir(number="6098", madde_no="399")
tr_ictihat_ara(courts=["YARGITAYKARARI"], query="işyeri uygulaması çalışma koşulu esaslı değişiklik", date_from="2022-01-01")
```

Atıf etiketleri: `[ArthurLegal TR — 4857 m. 22 — GG.AA.YYYY]`, `[model bilgisi — doğrula]`, `[kullanıcı verdi]`.

## Çıktı

```markdown
## El Kitabı Güncellemesi: [Bölüm adı]

### Değişiklik
[diff]

### Çapraz atıf etkisi
| Bölüm | Değişen bölüme atıf | Hâlâ doğru mu? | Gereken düzeltme |
|---|---|---|---|
| [ad] | [nasıl] | ✅/⚠️ | [ne] |

### Ek etkisi
| Ülke / işyeri / TİS | Mevcut ek | Değişiklikten sonra | Eylem |
|---|---|---|---|
| [ad] | [ne diyor] | [geçerli / eskidi / güncellenmeli] | [yok / güncelle / yeni ek] |

### m. 22 söz kontrolü
[Aleyhe esaslı değişiklik yok / var → yazılı bildirim + 6 iş günü yazılı kabul gereken grup; geçmişe etki yok]

### Yayına hazır
- [ ] Çapraz atıflar güncellendi
- [ ] Ekler güncellendi
- [ ] [Aleyhe değişiklikse: yazılı bildirim gönderildi, kabul/ret kayıtları toplandı]
- [ ] Yürürlük tarihi ileriye dönük
- [ ] KVKK aydınlatma / İSG bilgilendirmesi (gerekiyorsa)
- [ ] Sürüm numarası ve tarih güncellendi
- [ ] Tebliğ ve imza kaydı
```

## Bu skill ne yapmaz

- Değişikliği onaylamaz; İK/hukuk yönetimi onaylar.
- Çalışanlara duyurmaz.
- Kabul/imza takibini yürütmez.

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
