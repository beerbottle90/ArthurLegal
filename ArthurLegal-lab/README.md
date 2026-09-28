# ArthurLegal Lab (test)

Bu klasör ArthurLegal'in ölçüm laboratuvarıdır. Burada denenen hiçbir şey ürün değildir;
paketlere ancak ölçülüp onaylandıktan sonra girer. Bu dal (`test/jev-atif`) ana dala
birleştirilmez.

## jev/ — karar modeli ve madde atfı denetimi

TypeSafe'in Jev modeli metin üretmez; bir metne bakıp olasılıklı bir karar döndürür
("evet/hayır", "şu seçenek"). Buradaki çalışma, bu tür bir modelin hukuk işinde nerede işe
yaradığını ölçer.

| Çalışma | Durum |
|---|---|
| Resmî Gazete konu ön elemesi (enerji, rekabet, vergi, icra) | Tamamlandı. Buradan çıkan yerel motor ürüne girdi: `tr_resmi_gazete_tara(konu=…)` ve `tr_mevzuat_ara(konu=…)`, paketler v1.9.0 ve sonrası. |
| Madde atfı denetimi ("ikinci göz") | Sürüyor. 153 kalemlik Türkçe sınav kümesi hukukçu onayı bekliyor; ölçüm onaydan sonra yapılacak. |

Madde atfı denetiminin sorusu tektir: bir taslağın bir kanun maddesine yüklediği hüküm (hakkın
sahibi, şart, süre, sürenin başlangıcı, sonuç) madde metninde gerçekten var mı? Paketlerdeki
madde doğrulama kapısının (`mevzuat-mcp-rehberi.md`, bölüm 9, adım 4) bağımsız ikinci gözü
olarak düşünülüyor.

### İlkeler

- Ölçmeden söylenmez. Satıcının iddiası ile ölçülen değer yan yana yazılır.
- Kural yalnız ekler, asla elemez: `p = max(p_kural, p_model)`.
- Sınav kümesine bakılarak istem, eşik ya da kural ayarlanmaz.
- Müvekkil verisi yoktur. Madde metinleri resmî kaynaktan canlı çekilir, iddialar uydurmadır.
- Buluttaki bir modele yalnız kamuya açık metin ve maskelenmiş iddia cümlesi gider.

### Çalıştırma

```bash
cd ArthurLegal-lab/jev
python -m pytest tests/ -q      # çevrimdışı, anahtar gerekmez
python atif_altin.py            # sınav kümesini doğrula ve dışa aktar
```

Jev'i gerçekten çağırmak için `.env.ornek` dosyasını `.env` adıyla kopyalayın; `.env` git'e
girmez. `hasat.py`, `disa_aktar.py --mcp` ve `olc_mevzuat.py` Türkiye arka ucunun
(arthur-tr-hukuk-mcp) kaynak kodunu yan klasörde bekler; bu klasörde tek başlarına çalışmazlar.

Ayrıntılı bulgular ve ölçüm tabloları: [jev/README.md](jev/README.md).
