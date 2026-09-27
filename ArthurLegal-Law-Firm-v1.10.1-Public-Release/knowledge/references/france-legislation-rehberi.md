# Fransa Mevzuatı & İçtihadı — Kullanım Rehberi (v1.7.0)

> **Erişim tipi:** WebFetch (GET) — Légifrance HTML erişimi auth gerektirmez
> **Auth:** Légifrance DILA REST API için PISTE kaydı gerekli (ücretsiz, bir kez)
> **Kapsam:** Fransız kodlar, yasalar, Cour de cassation kararları
> **[Müvekkil] bağlamı:** Fransız karşı taraflar (Total/TotalEnergies, Paris arbitrajı), ICC Paris

---

## 1. Légifrance — HTML Erişimi (Kayıt Gerektirmez)

Bireysel madde veya kanun metni için:

```
GET https://www.legifrance.gouv.fr/codes/section_lc/{KOD_ID}/{BOLUM_ID}
```

**[Müvekkil] için kritik Fransız mevzuatı:**

| Mevzuat | URL |
|---|---|
| Code civil (tüm metin) | `https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006070721/` |
| Code de commerce | `https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000005634379/` |
| Code du travail | `https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/` |
| Code de l'énergie | `https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000023983208/` |
| Code de la propriété intellectuelle | `https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069414/` |
| RGPD (FR uygulama) | `https://www.legifrance.gouv.fr/loda/id/JORFTEXT000037085952/` |

**Belirli madde çekimi** (LEGIARTI numarasıyla):
```
WebFetch("https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006436298/",
         "Code civil m.1134 sözleşmelerin bağlayıcılığı")
```

---

## 2. Légifrance DILA REST API (PISTE — Ücretsiz Kayıt Sonrası)

**Kurulum:** https://piste.gouv.fr → Kayıt → Uygulama oluştur → Client ID + Secret al

Token alma (OAuth2):
```
POST https://oauth.piste.gouv.fr/api/oauth/token
Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials&client_id={ID}&client_secret={SECRET}&scope=openid
```

Token ile arama:
```
POST https://api.piste.gouv.fr/dila/legifrance/lf-engine-app/consult/lawId
Authorization: Bearer {token}
Content-Type: application/json
{"id":"LEGITEXT000006070721"}
```

---

## 3. Judilibre — Cour de cassation Kararları

**Fransa'nın açık temyiz mahkemesi API'si. PISTE kaydı sonrası erişim.**

```
GET https://api.piste.gouv.fr/cassation/judilibre/v1.0/search?query={sorgu}&type=arret
Authorization: Bearer {token}
```

**Kayıt gerektirmeden arama** (PISTE olmadan HTML):
```
WebFetch("https://www.courdecassation.fr/recherche-judilibre?expression={sorgu}",
         "Enerji sözleşmesi force majeure Fransız Yargıtay kararları")
```

---

## 4. Conseil d'État (İdare Mahkemesi)

```
WebFetch("https://www.conseil-etat.fr/fr/decisions-de-justice#",
         "Enerji lisansı iptal kararları")
```

Karar arama: `https://www.conseil-etat.fr/fr/recherche?q={sorgu}`

---

## 5. LEGI Bulk Download (Tüm Kodlar — Ücretsiz)

Tüm konsolide kodları indirmek için (setup amaçlı):
- `https://www.data.gouv.fr/datasets/legi-codes-lois-et-reglements-consolides`

---

## Atıf formatı

```
[FR Mevzuat — Code civil Art.{no} / {Kanun adı} — Légifrance — GG.AA.YYYY]
[Cass. — {Daire} — {Karar no/tarih} — GG.AA.YYYY]
[CE — {Daire} — {Karar no} — GG.AA.YYYY]
```

---

## [Müvekkil] için özel notlar

- TotalEnergies (Paris merkezli) ile olası işbirliği veya rakip pozisyonlarda **droit français** klozları
- **ICC Tahkim Kuralları** Paris merkezli — Fransız PACI (Arbitration) hukuku uygulanabilir
- **Code de l'énergie** — Fransız enerji lisansları ve piyasa erişimi
- Fransız şirketler için KBIS (ticaret sicil belgesi) kamuya açık: `https://data.inpi.fr/`

*Son güncelleme: 29.05.2026 — v1.7.0. Légifrance HTML + PISTE API + Judilibre entegrasyonu.*
