---
name: legal-research-alman-hukuku
description: >
  Alman mevzuati, ictihadi ve yasama gerekcelerini de-eli MCP uzerinden okur.
  Dort ust kaynak tek uc: NeuRIS (federal mevzuat), rechtsprechung-im-internet
  (yedi federal mahkeme, tam), Open Legal Data (16 eyalet), Bundestag DIP.
user-invocable: true
---

# Alman Hukuku Araştırması (de-eli MCP)

## Ne zaman kullanılır

- Alman kanunu, yönetmeliği veya bir maddesinin yürürlükteki metni sorulduğunda.
- Alman mahkeme kararı arandığında — özellikle BVerfG, BGH, BAG, BFH, BVerwG,
  BSG, BPatG.
- Bir Alman düzenlemesinin **gerekçesi** (Gesetzesbegründung) gerektiğinde.
- Karşılaştırmalı analizde Almanya yargı çevrelerinden biriyse.
- Alman hukuku uygulanacak hukuk seçilmiş bir sözleşme incelenirken.

## Ne zaman kullanılmaz

- AB düzeyi enstrüman soruluyorsa → `ab-mevzuat` (Cellar). Bir Alman ölçütü AB
  direktifini uyguluyor olsa bile ikisi **ayrı korpustur**.
- Alman **doktrini** isteniyorsa → `karsilastirmali-doktrin` (LexScholar).
  Bu araç birincil kaynak verir, şerh vermez.
- Başka bir yargı çevresinin hukuku için.

## Araçlar (14)

**Mevzuat:** `de_search` · `de_get_act` · `de_get_text` · `de_list_publishers` ·
`de_recent_changes`
**İçtihat (yedi federal mahkeme, TAM):** `de_rii_case_search` · `de_rii_get_case_text`
**İçtihat (NeuRIS beta dilimi):** `de_case_search` · `de_get_decision` · `de_get_decision_text`
**İçtihat (eyaletler + tam metin):** `de_oldp_case_search` · `de_oldp_get_case`
**Parlamento:** `de_dip_search` · `de_dip_get_document`

## Yöntem

1. **İçtihatta önce `de_rii_*`.** Yedi federal mahkeme için RII resmî ve tamdır;
   NeuRIS içtihadı beta bir örneklemdir. Eyalet mahkemesi veya tam metin taraması
   gerekiyorsa `de_oldp_*`.
2. **Mevzuatta** `de_search` → `de_get_act` (künye) → `de_get_text` (metin).
3. Yürürlük tarihi tartışmalıysa `de_recent_changes` ile değişiklik zincirini gör.
4. Gerekçe gerekiyorsa `de_dip_search` ile Drucksache'yi bul.

## Sert kurallar

**Atıf dizesi ASLA kurulmaz.** Her yanıt `eli_uri` (içtihatta `ECLI`),
`human_readable_citation` ve `source_url` taşır — birebir kullan. Uydurulmuş bir
ELI/ECLI son derece makul görünür.

**NeuRIS eksiktir (BETA).** Bir aktın bulunmaması yok olduğunun kanıtı değildir;
`dataset_note` alanını oku ve kapsam sınırını cevaba taşı.

**Open Legal Data resmî değildir.** Topluluk agregatörü (ODbL v1.0). Eyalet
içtihadı ve tam metin taraması için kullan; sonuç yük taşıyacaksa resmî kaynaktan
teyit et. Yeniden yayımlanan alıntıda atıf + aynı lisansla paylaşım yükümlülüğü doğar.

## Atıf

```
[Alman Mevzuatı — de-eli MCP — {human_readable_citation} — {eli_uri} — GG.AA.YYYY]
[Alman İçtihadı — de-eli MCP — {mahkeme} — {ECLI} — GG.AA.YYYY]
```

## Bilgi tabanı

`de-eli-mcp-rehberi.md` · `germany-legislation-rehberi.md` (WebFetch yedeği)
