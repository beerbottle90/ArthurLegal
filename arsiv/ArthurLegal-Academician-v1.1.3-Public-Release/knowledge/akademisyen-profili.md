# Akademisyen Profili

> Bu dosya, tüm plugin'lerin **her oturumun başında** okuduğu profil dosyasıdır.
>
> **Bu dosya bir şablondur.** Köşeli parantezli alanları (`[DOLDUR]`) kendinize göre
> doldurun. Paket **hiçbir gerçek kişi veya kurum verisi içermez**.
>
> ⚠️ **Asistana not:** Bir alan `[DOLDUR]` olarak kalmışsa **varsayma** — kullanıcıya sor.

---

## 1. Kimlik ve kadro

| Alan | Değer |
|---|---|
| Unvan | `[DOLDUR — Arş. Gör. / Dr. Öğr. Üyesi / Doçent / Profesör]` |
| Kurum | `[DOLDUR — Üniversite, Hukuk Fakültesi]` |
| Anabilim dalı | `[DOLDUR — örn. Ticaret Hukuku / Anayasa Hukuku / Ceza ve Ceza Usulü]` |
| ORCID | `[DOLDUR — 0000-0000-0000-0000]` |
| YÖKSİS / YÖK Akademik profili | `[DOLDUR — bağlantı]` |
| Doktora tarihi | `[DOLDUR — doçentlik puanlamasında "doktora sonrası" eşiği için kritik]` |

## 2. Araştırma alanı

- **Birincil alan:** `[DOLDUR]`
- **İkincil alanlar:** `[DOLDUR]`
- **Anahtar kelimeler (izleme agent'ları bunları kullanır):** `[DOLDUR — 5-10 terim]`
- **Karşılaştırmalı hukuk ilgisi:** `[DOLDUR — örn. Alman / İsviçre / AB / ABD / yok]`

> Karşılaştırmalı ilgi alanı, hangi MCP'nin öncelikli kullanılacağını belirler:
> İsviçre → OpenCaseLaw.ch + Fedlex · ABD → CourtListener · AB → EUR-Lex · AİHM → HUDOC

## 3. Dil ve çıktı tercihi

| Alan | Değer |
|---|---|
| Çıktı dili | `[DOLDUR — Türkçe / İngilizce / kullanıcının yazdığı dil]` |
| Yayın dili | `[DOLDUR — TR / EN / her ikisi]` |
| Yabancı dil belgesi | `[DOLDUR — YDS/YÖKDİL/TOEFL puanı ve tarihi — doçentlik ön koşulu]` |

## 4. Atıf stili

| Alan | Değer |
|---|---|
| Birincil stil | `[DOLDUR — Klasik TR tam-dipnot / OSCOLA / Bluebook / AGLC / McGill / Chicago]` |
| Hedef dergi kılavuzu | `[DOLDUR — derginin yazım kuralları bağlantısı]` |
| Mükerrer atıf biçimi | `[DOLDUR — "Yazar (n 12) s. 40" / "age. s. 40" / dergiye göre]` |

> Dergi kılavuzu profil ile çelişirse **dergi kılavuzu üstündür**; asistan bunu söyler.

## 5. Hedefler

| Alan | Değer |
|---|---|
| Aktif hedef | `[DOLDUR — örn. doçentlik başvurusu / doktora tezi / SSCI makalesi / TÜBİTAK 1001]` |
| Doçentlik başvuru dönemi | `[DOLDUR — örn. Mart 2027]` |
| Başvuru dönemi ÜAK PDF'i teyit edildi mi? | `[DOLDUR — Evet, tarih: ... / Hayır]` |

> ⚠️ **Doçentlik puan hesabı, bu satır "Evet" olmadan kesin sunulmaz.** ÜAK Hukuk Temel
> Alanı ölçütleri dönemden döneme değişir. → `references/docentlik-hukuk-temel-alani-rehberi.md`

## 6. Kurumsal yükümlülükler

| Alan | Değer |
|---|---|
| Kurumun ÜYZ beyan formu var mı? | `[DOLDUR — Evet (bağlantı) / Hayır / Bilmiyorum]` |
| Kurumun benzerlik oranı yönergesi | `[DOLDUR — eşik ve kaynak; evrensel eşik YOKTUR]` |
| Etik kurul adı | `[DOLDUR — ampirik çalışma yapılacaksa]` |
| Fon sağlayıcı açık erişim mandatı | `[DOLDUR — örn. Horizon Europe / TÜBİTAK / yok]` |

## 7. Erişilebilen veritabanları

Asistan, erişiminiz olmayan bir kaynaktan alıntı yapıyormuş gibi davranmaz.
Hangilerine **kurumsal aboneliğiniz** olduğunu işaretleyin:

| Veritabanı | Erişim | Not |
|---|---|---|
| Lexpera | `[DOLDUR — var/yok]` | Resmî API yok — manuel doğrulama |
| Kazancı | `[DOLDUR]` | Resmî API yok — manuel doğrulama |
| Jurix | `[DOLDUR]` | Hukuk dergileri odaklı; API yok |
| Legalbank | `[DOLDUR]` | API yok |
| HeinOnline | `[DOLDUR]` | Dergi atfı için altın standart; API kurumsal |
| Westlaw / LexisNexis | `[DOLDUR]` | API kurumsal |
| Beck-online / juris | `[DOLDUR]` | Alman doktrini |
| iThenticate / Turnitin | `[DOLDUR]` | Benzerlik raporu |

> Ücretsiz ve programatik olanlar (Crossref, OpenAlex, Semantic Scholar, DOAJ, ORCID,
> EUR-Lex, HUDOC) ile bağlı MCP'ler (TR Legal, CourtListener, Fedlex, OpenCaseLaw.ch)
> profil doldurulmasa da kullanılabilir.

## 8. Rol bayrakları (gizlilik açısından kritik)

| Rol | Aktif mi? |
|---|---|
| Bir dergide **hakem**im | `[DOLDUR — evet/hayır]` |
| Bir dergide **editör / yayın kurulu** üyesiyim | `[DOLDUR]` |
| TÜBİTAK / AB **panelisti veya değerlendiricisi**yim | `[DOLDUR]` |
| Tez **jüri** üyesiyim | `[DOLDUR]` |

> ⚠️ Bu rollerden herhangi biri aktifse: değerlendirme altındaki **hiçbir metin** bu
> asistana girilemez. Gizlilik yükümlülüğünün ihlalidir.
> → `references/hakemlik-gizlilik-rehberi.md` · `/hakemlik-editorluk:hakem-rubrigi`

---

## Örnek (kurgusal — kendi bilgilerinizle değiştirin)

> Bu örnek tamamen **kurgusaldır** ve yalnızca alanların nasıl doldurulacağını gösterir.

- Unvan: Dr. Öğr. Üyesi · Kurum: `[Üniversite] Hukuk Fakültesi`
- Anabilim dalı: Ticaret Hukuku · Doktora: 2023
- Birincil alan: Sermaye piyasası hukuku; ikincil: karşılaştırmalı şirketler hukuku
- Anahtar kelimeler: halka açık ortaklık, pay sahipliği, kurumsal yönetim, açıklama yükümlülüğü
- Karşılaştırmalı ilgi: İsviçre + AB → OpenCaseLaw.ch, Fedlex, EUR-Lex öncelikli
- Çıktı dili: Türkçe · Yayın dili: TR + EN
- Atıf stili: Klasik TR tam-dipnot; İngilizce yayında OSCOLA
- Aktif hedef: Doçentlik (Mart 2027) — ÜAK PDF'i teyit edildi mi? **Hayır**
- Rol bayrakları: Hakem → evet (bir TR Dizin dergisinde). Editör → hayır.
