# Alman Hukuku — de-eli MCP (Kullanım Rehberi)

> ✅ **Custom MCP server VAR (v1.5.0).** Alman mevzuatı, içtihadı ve yasama
> belgeleri artık WebFetch kazımasıyla değil, dört resmî/kamusal üst kaynağı tek
> uçta birleştiren bir MCP sunucusu üzerinden okunuyor. **14 araç.**
>
> **BİRİNCİL kaynaktır** — mevzuat ve içtihat için. Buradan dönen bir kanun ya da
> karar hukukun kendisidir ve bir sonucun dayanağı olabilir.
>
> **Erişim sorununu da çözer.** `germany-legislation-rehberi.md` içinde kayıtlı
> ölçüm, `gesetze-im-internet.de` ve NeuRIS domain'lerinin bazı ortamlardan
> **ECONNREFUSED** döndürdüğünü gösteriyor. MCP sunucusu bu çağrıları **kendi
> tarafında** yapar; istemcinin çıkış ağı devreye girmez.

---

## 0. Bağlantı bilgileri (ÖNCE BUNU GİR)

| Alan | Değer |
|------|-------|
| **MCP endpoint — uzak** | `https://<DEPLOY-FQDN>/mcp` ⟵ deploy sonrası doldur |
| **MCP endpoint — yerel** | `http://127.0.0.1:8790/mcp` |
| **Transport** | Streamable HTTP (`/mcp`, SSE-or-JSON) |
| **Auth** | **Yok** (upstream'lerin hepsi public) |
| **Sunucu kaynağı** | `github.com/beerbottle90/de-eli-mcp` |
| **Doğrulanmış sürüm** | `de-eli-mcp` v3.4.6 — 14 araç |

**claude.ai kurulumu:** Settings → Connectors → *Add custom connector* → MCP
endpoint URL'sini gir → auth "None". Araçlar bağlantı sonrası otomatik keşfedilir.
Tool isim prefiksi verdiğin connector adına göre üretilir — **prefiksi sabit
varsayma**, aşağıdaki base isimleri kullan.

> ⚠️ Host geçici bir tünel (`*.trycloudflare.com`) ise **her yeniden başlatmada
> değişir** ve connector sessizce kırılır: tanım doğru görünür, çağrılar düşer.
> Kalıcı kullanım için adlandırılmış tünel veya hosted deploy gerekir.

---

## 1. Dört üst kaynak — hangisi ne veriyor, sınırı ne

| Kaynak | Kapsam | Statü |
|---|---|---|
| **NeuRIS** (`rechtsinformationen.bund.de`, BMJV) | Federal mevzuat | **RESMÎ ama BETA** — mevzuat kümesi **eksik** (~2.413 akt). Her yanıt bir `dataset_note` taşır. |
| **rechtsprechung-im-internet.de** (BMJ/juris) | BVerfG, BGH, BAG, BFH, BVerwG, BSG, BPatG | **RESMÎ ve bu yedi mahkeme için TAM** (~83.300 karar) |
| **Open Legal Data** | ~424.000 karar, ~1.119 mahkeme, 16 eyalet dahil | **TOPLULUK agregatörü** (ODbL v1.0), resmî servis **değil**. Buradaki tek tam metin araması. |
| **Bundestag DIP** | ~287.000 Drucksache (Gesetzesbegründungen dahil), genel kurul tutanakları, yasama süreçleri | Resmî parlamento kaydı |

---

## 2. Araçlar (14) — bağlanınca otomatik keşfedilir

**Mevzuat (NeuRIS)**

| Araç | Ne yapar |
|---|---|
| `de_search` | Terim ve tarihle federal mevzuat araması |
| `de_get_act` | ELI ile akt künyesi |
| `de_get_text` | Aktın tam metni (`html` veya LegalDocML.de `xml`) |
| `de_list_publishers` | Yayın organları (BGBl I/II, Bundesanzeiger) |
| `de_recent_changes` | Belirli tarihten sonra yayımlanan aktlar, yeniden eskiye |

**İçtihat — yedi federal yüksek mahkeme (RII)**

| Araç | Ne yapar |
|---|---|
| `de_rii_case_search` | Yedi federal mahkemede karar araması |
| `de_rii_get_case_text` | Kararın tam metni |

**İçtihat — NeuRIS beta dilimi**

| Araç | Ne yapar |
|---|---|
| `de_case_search` · `de_get_decision` · `de_get_decision_text` | Beta karar kümesi |

**İçtihat — eyalet mahkemeleri ve tam metin taraması (Open Legal Data)**

| Araç | Ne yapar |
|---|---|
| `de_oldp_case_search` · `de_oldp_get_case` | 16 eyalet dahil geniş külliyat, tam metin araması |

**Parlamento (Bundestag DIP)**

| Araç | Ne yapar |
|---|---|
| `de_dip_search` · `de_dip_get_document` | Drucksachen, gerekçeler, tutanaklar, yasama süreçleri |

---

## 3. Kullanım disiplini — üç sert kural

**1) Alman atıf dizesi ASLA kurulmaz.** Her yanıt `eli_uri` (içtihatta `ECLI`),
`human_readable_citation` ve doğrulanabilir `source_url` taşır. Bu alanları
**birebir** kullan. Uydurulmuş bir ELI veya ECLI son derece makul görünür — bu
sunucunun var oluş sebebi tam olarak o hatayı önlemektir.

**2) Yedi federal mahkeme için `de_rii_*` tercih edilir.** RII o mahkemeler için
resmî ve tamdır; NeuRIS'in içtihat dilimi beta bir örneklemdir. Aynı kararı iki
kaynaktan aramak zaman kaybı değil, yanlış kapsam iddiasıdır.

**3) Open Legal Data nihai otorite değildir.** Topluluk agregatörüdür (ODbL v1.0).
Eyalet içtihadı ve tam metin taraması için kullan; sonuç yük taşıyacaksa resmî
kaynaktan teyit et. ODbL, yeniden yayımlanan alıntılarda **atıf ve aynı lisansla
paylaşım** yükümlülüğü doğurur.

**Ek uyarı — NeuRIS eksikliği:** Bir aktın burada bulunmaması, o aktın var
olmadığının kanıtı **değildir**. `dataset_note` alanını oku ve kapsam sınırını
cevaba taşı.

---

## 4. Atıf kalıbı

```
[Alman Mevzuatı — de-eli MCP — {human_readable_citation} — {eli_uri} — GG.AA.YYYY]
[Alman İçtihadı — de-eli MCP — {mahkeme} — {ECLI} — GG.AA.YYYY]
[Bundestag DIP — {belge türü} {numara} — GG.AA.YYYY]
```

MCP'ye erişilemiyorsa Alman kaynakları `[model bilgisi — doğrulayın]` etiketi
taşır; `germany-legislation-rehberi.md` içindeki WebFetch rotaları yedektir.

---

## 5. [ŞİRKET ADI] için neden gerekli?

Almanya iki ayrı eksende iş üretir: **karşılaştırmalı hukuk analizinde referans
yargı çevresi** (Alman doktrini ve içtihadı Türk hukukunun kaynaklarından biridir)
ve **AB enerji/rekabet düzenlemesinin ulusal uygulaması**. Alman karşı taraflarla
sözleşme, Alman hukukunun uygulanacak hukuk seçildiği anlaşmalar, ve AB
tüzüklerinin Almanya'da nasıl uygulandığı sorusu bu araca düşer.

**Bağlantılı rehberler:** `germany-legislation-rehberi.md` (WebFetch yedeği ve
kaynak haritası) · `eu-legislation-rehberi.md` (AB düzeyi) ·
`karsilastirmali-hukuk-rehberi.md` (yargı çevresi yönlendirme).
