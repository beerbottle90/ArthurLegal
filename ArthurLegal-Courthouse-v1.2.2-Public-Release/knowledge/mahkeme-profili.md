# Mahkeme Profili — [DOLDUR]

> **Önce mahkeme türü profilini seçin.** Görev, süreler, kanun yolu, sık usul riskleri ve kalem akışı `profiles/` altındaki hazır profillerdedir: `asliye-hukuk`, `asliye-ticaret`, `is-mahkemesi`, `aile-mahkemesi`, `tuketici-mahkemesi`, `sulh-hukuk`, `icra-hukuk`, `ceza-mahkemeleri`, `sulh-ceza-hakimligi`, `idare-vergi-mahkemeleri`. Bu şablon yalnız mahkemeye özgü bilgiyi (kadro, iş yükü, yerel uygulama) tutar.
> **Seçilen profil:** [DOLDUR — örn. `profiles/asliye-hukuk.md`] · **Kullanılan izleyiciler:** [DOLDUR — `agents/` altından; ortak kurallar `references/izleyici-rehberi.md`]

> Bu dosya mahkemenin baseline'ıdır. Asistan her cevapta bunu baz alır.
> `[DOLDUR]` alanlarını kendi mahkemenize göre doldurun. Gerçek kişi verisi girmeyin; rol-bazlı tanım yeterlidir.

## Temel

- **Dal:** [DOLDUR — Hukuk / Ceza / İdari / Vergi]
- **Mahkeme türü:** [DOLDUR — örn. Asliye Hukuk / Ağır Ceza / İdare / Vergi Mahkemesi]
- **Yargı çevresi:** [DOLDUR — il / ilçe / adliye]
- **Daire/numara:** [DOLDUR — örn. 3. Asliye Hukuk]
- **Bağlı olduğu istinaf:** [DOLDUR — ilgili BAM / BİM]

## Kadro (rol-bazlı, isim değil)

- **Hâkim / Başkan:** [DOLDUR]
- **Üye hâkimler (heyetliyse):** [DOLDUR]
- **Yazı işleri müdürü:** [DOLDUR]
- **Zabıt kâtibi / kalem:** [DOLDUR]

## İş yükü & öncelikler

- **Tipik dosya tipi:** [DOLDUR — örn. ticari, kira, iş, kamulaştırma]
- **Yoğun usul kalemleri:** [DOLDUR — örn. bilirkişi yönetimi, tebligat, keşif]
- **Kritik süreler:** [DOLDUR — örn. tutuklu işler, ivedi yargılama]

## Sistem & araçlar

- **UYAP modülleri:** [DOLDUR]
- **ArthurLegal MCP (`tr_`) bağlı mı:** [DOLDUR — Evet/Hayır] (aynı connector tapu-kadastro `tkgm_` araçlarını da taşır)

## Özel notlar

- [DOLDUR — mahkemeye özgü yerel uygulama, içtihat eğilimi, sık karşılaşılan usul sorunu]

---

> Profil doldurulmadıysa asistan genel yargısal modda çalışır ve `[DOLDUR]` alanlarına dair varsayım yapmadan, eksik bilgiyi kullanıcıdan ister.
