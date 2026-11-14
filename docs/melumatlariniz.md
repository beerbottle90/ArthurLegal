# Məlumatlarınız hara gedir

[Türkçe](verileriniz.md) · [English](your-data.md)

ArthurLegal pulsuz və açıq mənbəlidir; sizinlə xidmət müqaviləsi bağlamır. Buna görə aşağıdakılar müqavilə öhdəliyi
deyil, **dizaynın özüdür**: hər sətrin əsası açıq koddadır və yoxlanıla bilər.

## Bir cədvəldə

| Nə | Harada qalır | Kimə gedir |
|---|---|---|
| Sualınız və Claude-un cavabı | Claude-da (Anthropic). Masanın tarixçəsi isə öz cihazınızda: kompüterinizdə ArthurLegal quraşdırılıbsa quraşdırma qovluğunda, əks halda masanın brauzer yaddaşında; 90 gündən sonra silinir. | Anthropic-ə, Claude istifadənizin öz şərtləri ilə (aşağıda "Claude ayarınız"). |
| Araşdırma sorğusu (axtarış sözləri, qanun və maddə nömrəsi, qərar məlumatları) | ArthurLegal serveri axtarış mətnini saxlamır və sorğu jurnalı aparmır. İstisnalar (Almaniya və Azərbaycan alətlərinin qısa keşi) [serverin məxfilik sənədindədir](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md). | ArthurLegal MCP serverinə (Fly.io, Amsterdam), oradan yalnız lazımi parametrlərlə rəsmi mənbəyə: mevzuat.gov.tr, Rəsmi Qəzet, Yargıtay, Danıştay, Konstitusiya Məhkəməsi və qurumlar. Semantik axtarışda axtarış mətni mənasının hesablanması üçün Voyage AI-a gedir. |
| Müştəri sənədi (ArthurMask ilə) | Əsl sənəd və real adlar, nömrələr yalnız kompüterinizdə. | Claude-a yalnız etiketli mətn gedir (məs. `{{KİŞİ-01}}`). Etiketin real qarşılığı Claude-a göndərilmir. |
| UYAP | ArthurLegal UYAP-a heç nə yazmır; UYAP-da açdığınız siyahıları kompüterinizdə oxuyur. | Claude-a iş nömrələri etiketli gedir; real dəyərlər yalnız sizin ekranınızda görünür. |
| ArthurLegal Yaddaş (Beyin) | Kompüterinizdə. | Claude-a, söhbət açılarkən yalnız seçimləriniz, düzəlişləriniz və son sessiya xülasəsi. |
| Torpaq reyestri (TKGM) parsel sorğusu | Parsel identifikatoru və məlumatı serverin yaddaşında ən çox 24 saat; diskə və ya jurnala yazılmır. | Serverdən TKGM Parsel Sorğusuna. |
| Masanın dili və mövzusu | Cihazınızda. | Heç yerə. |

## Claude ayarınız

ArthurLegal sizin Claude hesabınızla işləyir və bu hesabın ayarlarını görə və dəyişə bilmir. Claude-dan **Free, Pro
və ya Max** planı ilə istifadə edirsinizsə, **Ayarlar › Məxfilik** bölməsindəki model təkmilləşdirmə ayarı açıq olduğu
müddətdə yeni söhbətləriniz Anthropic-in modellərinin təkmilləşdirilməsində istifadə oluna bilər. Müştəri məlumatı
daxil etməzdən əvvəl bu ayarı yoxlayın və müştəri sənədini ArthurMask-dən keçirin. Team, Enterprise və API istifadəsi
Anthropic-in kommersiya şərtlərinə tabedir. Mənbə: [Anthropic, model təkmilləşdirmə məxfilik ayarı](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings).

## Nəticə haqqında

- ArthurLegal-ın və Claude-un nəticəsi **hüquqi rəy deyil**.
- Nəticə **səhv və ya natamam ola bilər**.
- **Vəkil istifadə etməzdən əvvəl rəsmi mənbədən yoxlayır**; peşə məsuliyyəti vəkildədir.

Masadakı istinad yoxlaması maddə nömrəsinin və başlığının rəsmi mətndə olduğunu göstərir. Maddənin cümlədə ona aid
edilən məzmunu (hüququn sahibi, şərt, müddət, nəticə) həqiqətən deyib-demədiyini vəkil oxuyur; masanın "Mətni göstər"
düyməsi cümləni və rəsmi mətni yan-yana açır. Mənbə məlumat verməsə ArthurLegal boşluğu doldurmur, bu sətri yazır:
`UYARI: veri çekilemedi, teyidiniz gerekli: <keçid>` ("xəbərdarlıq: məlumat alına bilmədi, təsdiqiniz lazımdır").

## Yoxlamaq istəsəniz

- Uzaq serverin ətraflı məxfilik sənədi: [arthurlegal-mcp/PRIVACY.md](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md)
- ArthurMask necə işləyir: [arthur-mask](https://github.com/beerbottle90/arthur-mask)
- Bu depo: quraşdırmanın və masanın bütün kodu.

Bu səhifə hər buraxılışla yenidən nəzərdən keçirilir; dəyişiklik tarixçəsi depodadır.
