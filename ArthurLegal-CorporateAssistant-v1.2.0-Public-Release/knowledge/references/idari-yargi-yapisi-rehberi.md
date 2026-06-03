# Türk İdari Yargı Yapısı — Daire Haritası ([ŞİRKET ADI] Bağlamı)

> 3 dereceli idari yargı: İdare Mahkemesi → BİM → Danıştay. Bu rehber özellikle **Danıştay daire görevlerini** netleştiriyor.

## 3 derece akış

```
İdari işlem (Kurum/Bakanlık) →
İYUK m. 7 (30 gün) → İdare Mahkemesi (ilk derece) →
İYUK m. 45 (30 gün) → Bölge İdare Mahkemesi (istinaf) →
İYUK m. 46 (30 gün) → Danıştay (temyiz, ilgili daire) →
[İDDK — ısrar/çelişki]
```

## Danıştay daire görevleri (temyiz aşaması)

### [ŞİRKET ADI] için en kritik daireler

| Daire | Kapsam | [ŞİRKET ADI] ilgili |
|---|---|---|
| **5. Daire** | Genel idari uyuşmazlık | Memur statü, ÇSGB yabancı çalışan izni (Azerbaycanlı yöneticiler) |
| **8. Daire** | Belediye / imar / yapı | [ÖZEL ENDÜSTRİ BÖLGESİ] bağlantılı yatırımlar |
| **10. Daire** | **Çevre + doğal kaynak** | **[İşletme Yeri] İSG/çevre cezaları temyiz** — birincil önemli |
| **13. Daire** | **EPDK + Rekabet + BDDK + SPK + KGK + KİK** | **[ŞİRKET ADI] için TEMEL** — enerji + finansal düzenleyici |
| **14. Daire** | **ÇED + imar/çevre ek** | **[İşletme Yeri] ÇED** — birincil |
| **İDDK** | Birleştirici, ısrar incelemesi | Çelişki çözümünde |

### Diğer Danıştay daireleri ([ŞİRKET ADI]'da daha az)

- 1. Daire: Vatandaşlık + nüfus
- 2. Daire: Atama, görevde yükselme
- 3. Daire: **Vergi — KDV, ÖTV** (tax-legal kapsamı)
- 4. Daire: **Vergi — Gelir/Kurumlar vergisi** (tax-legal)
- 6. Daire: Toplu konut, yapı
- 7. Daire: **Vergi — Damga, MTV, harçlar** (tax-legal)
- 9. Daire: **Vergi cezası** (tax-legal)
- 11. Daire: Sosyal güvenlik
- 12. Daire: Atama, disiplin
- 15. Daire: Eğitim, üniversite

## Danıştay ilk derece görevli olduğu istisnalar

**Danıştay K. m. 24 + m. 30:**
- CB Kararları
- CB Kararı ile yürürlüğe konulan düzenleyici işlemler (Bakanlar Kurulu kararı muadili)
- Bakanlık ve kamu kurumu müsteşarları müşterek kararnameleri
- **Bakanlık genel tebliğleri** ve **yönetmelikleri** (normatif düzenleyici — bireysel idari işlem DEĞİL)

Bu durumda **doğrudan Danıştay'da** dava açılır, sonra İDDK temyiz.

⚠️ EPDK / Rekabet / KVKK / KİK / BDDK / SPK gibi kurumların **Tebliğ veya Yönetmelik** düzeyindeki normatif düzenlemeleri için de doğrudan Danıştay görevlidir (CB Kararıyla yürürlüğe konulmuyorsa, kurumun kendi düzenleyici yetkisiyle çıkardığı normatif metin).

**Ama** aynı kurumların **bireysel idari işlemleri** (lisans iptali, idari ceza, başvuru reddi) için İdare Mahkemesi (Ankara) ilk derece.

## Bölge İdare Mahkemesi (BİM) yapısı

8 BİM:
- Ankara, İstanbul, İzmir, Konya, Bursa, Erzurum, Gaziantep, Samsun

Her BİM içinde:
- İdare Dava Daireleri (istinaf)
- Vergi Dava Daireleri

[ŞİRKET ADI] için ana BİM'ler:
- **Ankara BİM** — EPDK/Rekabet/KVKK/KİK kararları (kurumlar Ankara merkez)
- **İzmir BİM** — [İşletme Yeri] kaynaklı il düzeyi davalar
- **İstanbul BİM** — şirket merkezi davalar

## İDDK (İdari Dava Daireleri Kurulu)

**Görevleri (Danıştay K. m. 38):**
- a) İdare Mahkemesi **ısrar** kararlarını temyizen inceler
- b) Danıştay dairelerinden **ilk derece** olarak verilen kararları temyizen inceler

İDDK kararları **bağlayıcıdır** — alt mahkemeler için.

## Yarg MCP

Bedesten birleşik API ile alt dereceleri (İdare Mah. + BİM) çekebilirsin:

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  arananKelime="<konu>",
  baslangicTarihi="2022-01-01"
)
```

Danıştay daire bazlı:

```
mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="13. Daire",
  arananKelime="<konu>"
)

mcp__claude_ai_Yarg_MCP__search_bedesten_unified(
  daire="İdari Dava Daireleri Kurulu",
  arananKelime="<konu>"
)
```

## Bağlantılı

- [İYUK rehberi](iyuk-rehberi.md)
- [ÇED rehberi](ced-rehberi.md)
- [EPDK rehberi](epdk-rehberi.md)
- [Yarg MCP rehberi](yargi-mcp-rehberi.md)
