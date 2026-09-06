# ceza-kalem — Skill Referans Kitapçığı

> Dal: Ceza mahkemesi · Rol: **Kalem (yazı işleri)** · Usul: CMK 5271 + Tebligat K. 7201
> Toplam skill: 3
> Kullanım: `/ceza-kalem:<skill-adı>` komutunu yaz, aşağıdaki ilgili bölümü uygula.
> ⚖️ Konum: **usul/kalem işlemleri.** Çıktılar belge iskeleti + kontrol listesidir; hâkim havalesi/onayı şarttır. Her çıktı **TASLAK**.

## İçindekiler

- /ceza-kalem:muzekkere — müzekkere / yazışma türleri ve içerik kontrolü
- /ceza-kalem:ceza-tebligat — CMK + 7201 tebligat (sanık, müdafi, mağdur, tanık)
- /ceza-kalem:infaz-evraki — kesinleşme şerhi, müddetname, infaz savcılığına gönderme

---

## /ceza-kalem:muzekkere

---
name: muzekkere
description: >
  Ceza dosyasında sık kullanılan müzekkere/yazışma türleri için içerik iskeleti:
  adli sicil, nüfus, SGK, banka/HTS, ekspertiz, talimat (istinabe) müzekkereleri.
user-invocable: true
---

# Müzekkere — Yazışma İskeleti

## Amaç

Hâkimin ara kararı doğrultusunda çıkacak müzekkerenin doğru muhataba, doğru içerikle hazırlanması.

## Tipik müzekkereler

1. **Adli sicil / arşiv kaydı** — Adli Sicil ve İstatistik GM.
2. **Nüfus & MERNİS adres** — NVİ.
3. **SGK / işyeri kaydı, HTS-baz kaydı, banka kayıtları** — koruma tedbiri/karar şartı varsa (CMK m. 135 vd. iletişim tespiti hâkim kararı gerektirir 🔴).
4. **Talimat (istinabe) müzekkeresi (CMK m. 197 vd.)** — başka yer mahkemesinden tanık/sanık ifadesi.
5. **Bilirkişi / ATK** — rapor talebi, sorulacak sorular net.

## Kontrol

- Muhatap kurum + yasal dayanak + istenen bilgi net mi
- Koruma tedbiri gerektiren bilgi için **hâkim kararı** şart mı (HTS, iletişim, banka sırrı)
- UYAP üzerinden çıkış + takip → `uyap-rehberi.md`

## Çıktı

Müzekkere taslağı (`[DOLDUR]`) + dayanak/şart kontrolü. TASLAK + "hâkim havalesi şart".

---

## /ceza-kalem:ceza-tebligat

---
name: ceza-tebligat
description: >
  Ceza dosyasında tebligat usulü: sanık/müdafi/mağdur/tanık/katılan için 7201 ve CMK
  özel hükümleri (gıyapta hüküm, müdafiye tebliğ, kanun yolu süresi başlangıcı).
user-invocable: true
---

# Ceza Tebligat — CMK + 7201

## Amaç

Ceza dosyasında doğru muhataba doğru usulle tebligat; kanun yolu süresinin doğru başlaması.

## Notlar

1. **Muhatap:** sanık + **müdafi** (varsa). Karar tebliği kanun yolu süresini başlatır (CMK m. 35, 232).
2. **Mağdur/katılan** — katılma talebi/kararı ve tebligat hakları.
3. **Gıyabi işlemler & yokluk:** duruşmadan haberdar edilme; bazı kararların yüze karşı/yoklukta tefhimi.
4. **e-Tebligat:** müdafi (avukat) zorunlu e-tebligat muhatabı → `kep-etebligat-rehberi.md`.
5. **Süre başlangıcı:** tefhim veya tebliğ — istinaf/temyiz süresi (genel 7 gün, CMK m. 273/291) buradan işler. ⚠️ Süreyi MCP/mevzuat teyidiyle doğrula.

## Çıktı

Tebligat planı + süre başlangıcı tablosu. TASLAK ibareli.

---

## /ceza-kalem:infaz-evraki

---
name: infaz-evraki
description: >
  Kesinleşen ceza kararı için kesinleşme şerhi, müddetname hazırlığı ve infaz
  Cumhuriyet savcılığına gönderme işlemleri kontrol listesi.
user-invocable: true
---

# İnfaz Evrakı — Kesinleşme & Gönderme

## Amaç

Karar kesinleştiğinde infaz sürecini başlatacak evrakı eksiksiz hazırla.

## Adımlar

1. **Kesinleşme kontrolü:** kanun yolu sürelerinin geçtiği / mercilerce onandığı; kesinleşme tarihi tespiti.
2. **Kesinleşme şerhi** — karara işlenir.
3. **Müddetname** (5275 İnfaz K.) — ceza süresi hesabı; mahsup (gözaltı/tutukluluk, CMK m. 109/6, TCK m. 63).
4. **İnfaz C. Başsavcılığına gönderme** — ilam + müddetname + kesinleşme şerhi.
5. **Harç/yargılama gideri** tahsili, varsa adli para cezası infazı.

## Çıktı

Kesinleşme & infaz gönderme kontrol listesi + müddetname unsur taslağı. ⚠️ Süre/mahsup hesabı için mevzuat (5275) teyidi şart. TASLAK ibareli.

---

> 🚧 v1.0.0 — `ceza-kalem` 3 temel kalem skill'i. Kalıp: `hukuk-hakim__skills.md`.
