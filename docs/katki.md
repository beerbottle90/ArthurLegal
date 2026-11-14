# Katkı: iş akışı ve playbook önerileri

[English](contributing.md) · [Azərbaycan dili](tohfe.md)

ArthurLegal, Türkiye'deki avukatlar için ücretsiz ve açık kaynaktır. Masadaki iş akışları ve sözleşme playbook'ları
avukatların ortak bilgi birikimiyle büyüyebilir: siz bir iş akışını ya da bir sözleşme pozisyonunu önerirsiniz, madde
ve karar dayanağı resmî kaynaktan teyit edilir, iş akışı herkesin masasına gelir.

## Ne önerebilirsiniz

- **Yeni iş akışı:** sık yaptığınız bir işin adımları (ör. kira tespit davası ön değerlendirmesi, ihtarname kontrolü).
- **Playbook pozisyonu:** bir sözleşme türünde bir konu için başlangıç pozisyonu, vazgeçilmez ve geri çekilme noktası.
- **Düzeltme:** var olan bir iş akışında eksik, eskimiş ya da hatalı bir adım ya da madde.

## Nasıl

1. GitHub hesabınızla [öneri formunu](https://github.com/beerbottle90/ArthurLegal/issues/new?template=is-akisi-onerisi.yml) doldurun.
2. Adımları sırasıyla yazın; avukatın vermesi gereken bilgiyi ve kararın verildiği noktaları belirtin.
3. Dayanak olarak kanun maddelerini ve kararları, mümkünse resmî bağlantısıyla ekleyin.

## Ne kontrol edilir

- **Gizlilik:** müvekkil adı, dosya numarası, büro adı ya da gizli bilgi içeren öneri yayımlanmaz. Örnek gerekiyorsa
  kurgusal ya da genelleştirilmiş yazın.
- **Dayanak:** her madde `tr_mevzuat_madde_getir` ile resmî metinden okunur; maddeye yüklenen içerik (hakkın sahibi,
  şart, süre, sonuç) metinle örtüşmezse düzeltilir ya da çıkarılır. Resmî kaynaktan teyit edilemeyen bilgi eklenmez.
- **Mesleki çizgi:** iş akışı avukatın aracıdır; vatandaşa doğrudan görüş veren, reklam niteliği taşıyan ya da sonuç
  vaat eden öneri eklenmez.

## Sonra ne olur

Uygun bulunan öneri iş akışı olarak paketlere ve masadaki İş akışları ekranına eklenir, sürüm notunda anılır. Öneri
reddedilirse ya da değiştirilerek eklenirse nedeni öneri sayfasında yazılır.
