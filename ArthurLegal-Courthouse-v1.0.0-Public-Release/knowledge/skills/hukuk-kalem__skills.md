# hukuk-kalem — Skill Referans Kitapçığı

> Dal: Hukuk mahkemesi · Rol: **Kalem (yazı işleri)** · Usul: HMK 6100 + Tebligat K. 7201 + Harçlar K. 492
> Toplam skill: 3
> Kullanım: `/hukuk-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar belge iskeleti ve kontrol listesidir; hâkim havalesi/onayı şarttır. Her çıktı **TASLAK**.

## İçindekiler

- /hukuk-kalem:tensip-zapti — HMK m. 137 sonrası tensip tutanağı & tahkikat planı
- /hukuk-kalem:tebligat — 7201 Tebligat K. usulü, tebliğ şerhi, e-tebligat
- /hukuk-kalem:harc-hesabi — Harçlar K. 492 nispi/maktu harç + gider avansı (HMK m. 120)

---

## /hukuk-kalem:tensip-zapti

---
name: tensip-zapti
description: >
  Dava açıldıktan sonra düzenlenen tensip zaptı (tahkikat planı) iskeletini üretir:
  dava şartı ön-kontrol, taraflara verilecek süreler, harç/avans kontrolü,
  tebligat çıkışları, ilk duruşma. Hâkim havalesine sunulur.
user-invocable: true
---

# Tensip Zaptı — Tahkikat Planı İskeleti

## Amaç

Dava dosyası açıldığında kalemin hazırladığı ilk işlem zincirini eksiksiz yapılandır. Tensip zaptı hâkim tarafından imzalanır; kalem **taslağını** hazırlar.

## Kontrol & adımlar

1. **Dava dilekçesi kontrolü (HMK m. 119):** zorunlu unsurlar tam mı (taraflar, talep, vakıa, deliller, hukuki sebep, imza). Eksikse 1 haftalık kesin süre (m. 119/2).
2. **Harç & gider avansı (m. 120):** başvuru + peşin harç yatırılmış mı; gider avansı tarifesi. Eksikse muhtıra. → `harc-gider-rehberi.md`.
3. **Tensip maddeleri (kalıp):**
   - Dilekçenin davalıya tebliği, **2 hafta** cevap süresi (m. 127)
   - Delil avansı ve delillerin sunulması (m. 121, 129)
   - Ön inceleme duruşma günü tayini
   - Varsa tedbir taleplerinin ayrı değerlendirilmesi
4. **Tebligat çıkışları:** kime, hangi adrese, hangi usulle (aşağıdaki `tebligat` skill'i).
5. **UYAP işlemleri:** dosya açılış, taraf/vekil kaydı, tevzi. → `uyap-rehberi.md`.

## Çıktı

`[DOLDUR]` alanlı tensip zaptı taslağı + eksik/muhtıra listesi (🔴🟠🟡). Üst başlık TASLAK + "hâkim havalesi şart".

---

## /hukuk-kalem:tebligat

---
name: tebligat
description: >
  7201 sayılı Tebligat Kanunu çerçevesinde tebligat usulünü belirler: muhatap,
  adres, tebliğ türü (normal / 21 / 35 / e-tebligat), şerh ve süre başlangıcı.
user-invocable: true
---

# Tebligat — 7201 Usulü

## Amaç

Bir evrakın hangi usulle, kime ve nasıl tebliğ edileceğini doğru belirle. Yanlış tebligat = sürelerin işlememesi + bozma riski 🔴.

## Karar ağacı

1. **Muhatap kim?** Gerçek kişi / tüzel kişi / vekil. Vekil varsa **vekile** tebliğ (HMK m. 73-81, Teb. K. m. 11).
2. **Adres var mı, doğru mu?** MERNİS adresi esas. Tüzel kişide ticaret sicil adresi.
3. **Tebliğ türü:**
   - **Normal tebliğ** (Teb. K. m. 10) — muhatap adreste.
   - **m. 21/1** — adreste bulunamazsa muhtara/komşu + 2 no'lu haber kâğıdı.
   - **m. 21/2** — bilinen adrese tebliğ edilemezse (adres kaydındaki yere).
   - **m. 35** — daha önce tebligat yapılmış adres değişmişse.
   - **e-Tebligat** (m. 7/a) — zorunlu muhataplar (avukat, tüzel kişi, kamu) için. → `kep-etebligat-rehberi.md`.
4. **Şerh & süre:** tebliğ tarihi sürelerin başlangıcı (m. 297 kanun yolu süresi de buradan). Şerhin usulüne uygunluğunu kontrol et.

## Çıktı

Tebligat türü önerisi + tebliğ mazbatası kontrol listesi + süre başlangıcı hesabı. TASLAK ibareli.

---

## /hukuk-kalem:harc-hesabi

---
name: harc-hesabi
description: >
  Harçlar Kanunu 492 ve HMK m. 120 çerçevesinde dava harcı (başvuru, peşin nispi/maktu,
  karar-ilam) ve gider avansı hesabı için kontrol listesi. Adli yardım hâllerini de gözetir.
user-invocable: true
---

# Harç & Gider Avansı

## Amaç

Dava türüne göre alınacak harç ve avansı doğru belirle. Eksik harç = davanın açılmamış sayılması riski (HMK m. 150 muhtıra süreci).

## Adımlar

1. **Dava türü → harç türü:**
   - **Konusu para ile ölçülebilen** → nispi harç (dava değeri üzerinden, Harçlar K. 492 (1) tarife).
   - **Konusu para ile ölçülemeyen** (tespit, bazı aile davaları) → maktu harç.
2. **Harç kalemleri:** başvurma harcı + peşin harç (nispi davada 1/4) + karar-ilam harcı (sonda).
3. **Gider avansı (HMK m. 120):** tarifeye göre; tebligat, bilirkişi, tanık, keşif giderleri. Delil avansı ayrı (m. 324).
4. **Adli yardım (HMK m. 334-340):** talep varsa harç/avanstan geçici muafiyet değerlendirmesi — hâkim kararına sunulur.
5. **Eksiklik → muhtıra:** kesin süre + sonuç (açılmamış sayılma / delilden vazgeçme).

## Çıktı

Harç/avans kalem tablosu (`[DOLDUR]` tutarlı) + eksiklik muhtırası taslağı. Güncel tarife için → `damga-vergisi-rehberi.md` ve yıllık Harçlar tarifesi (Resmi Gazete teyidi).

---

> 🚧 v1.0.0 — `hukuk-kalem` 3 temel kalem skill'i. Kalıp: `hukuk-hakim__skills.md`.
