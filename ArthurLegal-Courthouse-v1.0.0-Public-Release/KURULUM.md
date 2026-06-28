# Kurulum — ArthurLegal Courthouse

**Hedef ortam:** [Claude.ai Projects](https://claude.ai/projects) (web)
**Süre:** ~10 dakika

> ⚠️ Bu paket **yargı mensupları** (mahkeme hâkimleri + kalem memurlukları) içindir. Tüm çıktılar **taslaktır** ve **hâkim / heyet onayı** gerektirir; hiçbir çıktı yargısal karar yerine geçmez.

## 4 adım

1. **Yeni Claude.ai Project oluşturun** — [claude.ai/projects](https://claude.ai/projects) → "+ New Project".
2. **`SYSTEM_PROMPT.md`** içeriğini Custom Instructions alanına yapıştırın.
3. **`knowledge/`** klasöründeki dosyaları Project Knowledge'a sürükle-bırak ile yükleyin.
4. **`knowledge/mahkeme-profili.md`** içindeki `[DOLDUR]` alanlarını kendi mahkemenize göre özelleştirin (opsiyonel).

## TR Legal MCP bağlantısı (önerilir)

Yargı/mevzuat araçları için Claude.ai → Settings → Connectors üzerinden TR Legal MCP bağlantısını ekleyin (detay: `knowledge/references/yargi-mcp-rehberi.md` ve `mevzuat-mcp-rehberi.md`). MCP olmadan da çalışır; ancak güncel içtihat/mevzuat çekimi için MCP şarttır.

## İlk kullanım

```text
/hukuk-hakim:gerekceli-karar
[dosya özetini / uyuşmazlığı yapıştır]
```

Bir plugin'in tüm komutlarını görmek için yeni konuşmada sadece `/<plugin>:` yazın (örn. `/hukuk-hakim:`).

## Komut haritası (v1.0.0)

| Plugin | Skill'ler |
|---|---|
| `/hukuk-hakim:` | gerekceli-karar · on-inceleme · delil-degerlendirme · ihtiyati-tedbir |
| `/hukuk-kalem:` | tensip-zapti · tebligat · harc-hesabi |
| `/ceza-hakim:` | hukum-taslagi · iddianame-degerlendirme · tutuklama-degerlendirme · hagb-degerlendirme · uzlastirma-denetimi |
| `/ceza-kalem:` | muzekkere · ceza-tebligat · infaz-evraki |
| `/idari-hakim:` | idari-karar · yurutmenin-durdurulmasi · ehliyet-husumet · ivedi-yargilama |
| `/idari-kalem:` | dosya-tekemmul · idari-tebligat · karar-uygulama-takip |
| `/vergi-hakim:` | vergi-karar · tarhiyat-degerlendirme · odeme-emri-itiraz |
| `/vergi-kalem:` | vergi-tebligat · vergi-sure-takip · karar-uygulama-iade |

## Kişisel veri uyarısı

Mahkeme dosyaları yoğun **kişisel ve özel nitelikli veri** içerir. Bu pakete gerçek dosya verisi yüklemeden önce kurumsal gizlilik kurallarınızı ve veri minimizasyonu ilkesini gözetin. (Veri maskeleme katmanı ArthurLegal v1.4.0 hattında ayrı geliştirilmektedir.)
