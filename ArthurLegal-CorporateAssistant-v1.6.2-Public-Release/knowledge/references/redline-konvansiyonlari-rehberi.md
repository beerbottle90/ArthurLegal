> **Durum:** Konvansiyon rehberi (erişim gerektirmez). `contract-drafting` eklentisinin (redline-contract, belge-turet, versiyon-karsilastir, tadil-protokol) ev redline ve yorum standardı. Sistem talimatlarının 1. ve 3. bölümleriyle uyumludur; çelişki hâlinde sistem talimatı üstündür. [Şirket/Şirket adı]

# Redline ve Yorum Konvansiyonları: Pratik Rehber

## 1. Ortam ve çıktı biçimi

1. Dosya üretimi açık olan her ortamda (Claude.ai'da dosya oluşturma, Claude Code) redline gerçek izlenen değişiklik içeren `.docx` olarak verilir: `w:ins` ve `w:del` öğeleri, `w:author="ArthurLegal"`, tarih o günün tarihi; yorumlar `w:comment` ile `w:author="ArthurLegal"`, `w:initials="AL"`. python-docx ile `core_properties.author` ve `core_properties.last_modified_by` de `ArthurLegal` olur.
2. Dosya üretimi kapalıysa redline metin olarak verilir: silinen kısım `[silinen: ...]`, eklenen kısım `[eklenen: ...]`. Üstü çizili, kalın ve renk kullanılmaz. Kullanıcıya "Word'de Değişiklikleri İzle açıkken uygulayın" notu düşülür.
3. Dosya adı alt çizgili ve Türkçe karaktersizdir: `hizmet_sozlesmesi_redline_05092026.docx`.
4. Kullanıcının yüklediği belgede var olan biçim korunur; değiştirilen bölümler belgenin kendi biçimini izler.

## 2. Yorum yapısı (her zaman fallback ile)

Yorum tek paragraf düz metindir; emoji, tire, başlık ve kalın kullanılmaz. Sıra sabittir: önem derecesi kelimeyle, sorun, tercih edilen pozisyon, kabul edilmezse asgari pozisyon.

```
Yüksek: Sorumluluk tavanı sözleşme bedelinin yüzde 50'sine çekilmiş; müvekkil için risk. Tercih: tavan sözleşme bedeline eşit olsun, kasıt ve ağır kusur hariç tutulsun. Kabul edilmezse asgari: yüzde 75 ve can ve mal güvenliği istisnası.
```

## 3. Önem derecesi (dört kademe, kelimeyle)

Bloklayıcı: imzalanmaz. Yüksek: müzakere şart. Orta: düzeltme gerekli, işlemi bozmaz. Düşük: bilgi notu. Üst incelemenin Bloklayıcı dediği bulgu alt incelemede sessizce düşürülmez. Renkli daire veya simge kullanılmaz; knowledge dosyalarındaki renk kodları bu kelimelere çevrilir.

## 4. Sessiz düzeltme ve yorum ayrımı

Sessiz düzeltilir: yazım, atıf ve numara, tutarlılık, tanım hizalama. Yorum zorunludur: hukuki veya ticari pozisyon değişikliği, risk dağılımı, tutar, süre ve eşik, sorumluluk, fesih, uygulanacak hukuk ve yetki.

## 5. Standart kloz seti (her enerji sözleşmesinde kontrol)

1. Mücbir sebep ve aşırı ifa güçlüğü (TBK m. 136 ve 138): şebeke kesintisi, mevzuat değişikliği, kuraklık (HES).
2. Sınırlı sorumluluk ve cezai şart (TBK m. 179 ile 182; fahiş cezanın tenkisi).
3. Yaptırım ve uyum (OFAC, AB, BM, OFSI ve uluslararası finans kuruluşu yasaklı listeleri): `yaptirim-tarama-rehberi.md`.
4. KVKK (6698), gizlilik, fikri mülkiyet.
5. Uyuşmazlık ve uygulanacak hukuk (Türk mahkemeleri, ICC, LCIA): `governing-law-review`.
6. EPDK lisans ve pay devri ön onayı (kontrol değişikliği).
7. Ödeme ve teminat (akreditif, teminat mektubu), damga vergisi ve gross-up.
8. Devir ve temlik, tadil, fesih, süre ve yenileme, rekabet klozu: `rekabet-hukuku-rehberi.md`.

## 6. Üst başlık ve onay

Her çıktının ilk satırı:

```
TASLAK. DIŞ VEKİL VE BAŞ HUKUK MÜŞAVİRLİĞİ ([Baş Hukuk Müşaviri]) ONAYI ALINMADAN İMZALANMAZ.
```

Her çıktı taslaktır; imza öncesi onay zinciri: [Baş Hukuk Müşaviri], yüksek tutar veya stratejik işlemde [Genel Müdür], SHA reserved matter'da [Yönetim Kurulu] ve kredi veren veya ortak kuruluş onayı.

## Bağlantılı referanslar

`kanun-kisaltmalar.md`, `rekabet-hukuku-rehberi.md`, `yaptirim-tarama-rehberi.md`, `kvkk-m11-cevap-sablonu.md`

*Son güncelleme: 05.09.2026. Yazar, yorum ve başlık kuralları sistem talimatlarıyla hizalandı.*
