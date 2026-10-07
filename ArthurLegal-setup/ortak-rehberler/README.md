# Ortak rehberler: tek kaynak

Bazı rehberler birden çok pakete girer: çoğu Hukuk Bürosu ile Kurumsal'da, birkaçı dört pakette birden bulunur.
Eskiden her kopya elle tutuluyordu. Bu yüzden bir pakette yapılan düzeltme ötekine geçmiyordu. Örneğin esas
numarasıyla arama tarifi Courthouse'ta düzeltilmiş, üç pakette eski kalmıştı.

Artık bu rehberlerin tek kaynağı bu klasördedir:

- **Kaynak:** [`references/`](references/) altındaki dosyalar. Pakete göre değişen yer tutucular kaynakta
  `{{AL_KURUM}}` biçiminde yazılır. Örneğin hukuk bürosunda `[Müvekkil]`, kurumsal pakette `[ŞİRKET ADI]`.
- **Değerler ve dağılım:** [`paketler.json`](paketler.json) her değişkenin pakete göre değerini ve her rehberin
  hangi paketlere girdiğini tutar.
- **Paket kopyaları:** paket klasörlerindeki kopyalar bu kaynaktan üretilir ve commitlenir. Kurulum paket
  klasörlerini olduğu gibi okur; kurulum açısından hiçbir şey değişmedi.

## Ortak bir rehberi düzeltmek

1. Kaynağı düzeltin: `ArthurLegal-setup/ortak-rehberler/references/<ad>.md`.
2. Kopyaları üretin: `python ArthurLegal-setup/yayin/ortak_uret.py`.
3. Denetleyin: `python ArthurLegal-setup/yayin/ortak_uret.py --denetle`. Bu denetim testlerde de çalışır
   (`tests/test_ortak.py`).

Paketin içindeki kopyayı elle düzeltirseniz test kırmızı yanar ve sizi kaynağa yönlendirir.

## Kurallar

- Değişkenler yalnız yer tutucu ve hitap içindir (`[Müvekkil]` / `[ŞİRKET ADI]`, `firm-profile.md` /
  `company-profile.md`, hâkim paketinde "taraf"). İçerik farkı (bir süre, bir madde, bir cümle) değişkene dönüşmez.
- Yeni bir rehberi tek kaynağa almak için:
  `python ArthurLegal-setup/yayin/ortak_uret.py --benimse <ad>.md`. Araç kaynağı paketlerdeki kopyalardan
  türetir ve her paket için baytı baytına geri üretildiğini doğrular. Kopyalar arasında içerik farkı varsa reddeder
  ve farkı gösterir. Önce hangi metnin doğru olduğuna karar verilir, kopyalar eşitlenir, sonra rehber benimsenir.
- Bir rehberin metni bir kitle için baştan yazıldıysa (ör. hâkimler için Courthouse) o paketin kopyası tek kaynağa
  girmez ve bağımsız kalır. Öteki paketler ortak kaynağı paylaşmaya devam eder.

## Durum (07.10.2026)

- 87 ortak rehberin 67'si tek kaynakta: 64'ü Hukuk Bürosu ile Kurumsal'da, 3'ü dört pakette.
- Kalan 20 rehberde kopyalar arasında gerçek içerik farkı var. Bunlar karar bekliyor; `--benimse` hangi cümlenin
  farklı olduğunu gösterir.
