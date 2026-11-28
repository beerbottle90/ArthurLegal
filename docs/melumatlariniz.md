# Məlumatlarınız hara gedir

[Türkçe](verileriniz.md) · [English](your-data.md)

ArthurLegal pulsuz və açıq mənbəlidir; sizinlə xidmət müqaviləsi bağlamır. Buna görə aşağıdakılar müqavilə öhdəliyi
deyil, **dizaynın özüdür**: hər sətrin əsası açıq koddadır və yoxlanıla bilər.

ArthurLegal quraşdırmada seçdiyiniz süni intellekt tətbiqinin içində işləyir: Claude Desktop, ChatGPT masaüstü tətbiqi
və ya hər ikisi. Cədvəl hər ikisini əhatə edir; yalnız ChatGPT-yə aid olanlar ayrıca yazılıb.

## Bir cədvəldə

| Nə | Harada qalır | Kimə gedir |
|---|---|---|
| Sualınız və Claude-un cavabı | Claude-da (Anthropic). Masanın tarixçəsi isə öz cihazınızda: kompüterinizdə ArthurLegal quraşdırılıbsa quraşdırma qovluğunda, əks halda masanın brauzer yaddaşında; 90 gündən sonra silinir. | Anthropic-ə, Claude istifadənizin öz şərtləri ilə (aşağıda "Claude ayarınız"). |
| Sualınız və ChatGPT-nin cavabı (ChatGPT-ni seçmisinizsə) | ChatGPT-də (OpenAI). Masanın tarixçəsi isə kompüterinizdə, quraşdırma qovluğunda; 90 gündən sonra silinir. | OpenAI-a, ChatGPT istifadənizin öz şərtləri ilə (aşağıda "ChatGPT ayarınız"). Sualınızla birlikdə ChatGPT-nin alətlərdən aldığı nəticələr də (qanunvericilik, məhkəmə təcrübəsi, qərarlar kimi rəsmi mənbələrdən gələn mətnlər) ChatGPT-yə gedir. |
| Araşdırma sorğusu (axtarış sözləri, qanun və maddə nömrəsi, qərar məlumatları) | ArthurLegal serveri axtarış mətnini saxlamır və sorğu jurnalı aparmır. İstisnalar (Almaniya və Azərbaycan alətlərinin qısa keşi) [serverin məxfilik sənədindədir](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md). | ArthurLegal MCP serverinə (Fly.io, Amsterdam), oradan yalnız lazımi parametrlərlə rəsmi mənbəyə: mevzuat.gov.tr, Rəsmi Qəzet, Yargıtay, Danıştay, Konstitusiya Məhkəməsi və qurumlar. Semantik axtarışda axtarış mətni mənasının hesablanması üçün Voyage AI-a gedir. |
| Müştəri sənədi (ArthurMask ilə) | Əsl sənəd və real adlar, nömrələr (ArthurMask-ın real adlar cədvəli) yalnız kompüterinizdə. Real adlar cədvəli siz silənə qədər qalır; maskalanmış aralıq nüsxələr 30 gündən sonra avtomatik silinir. | Claude-a və ya ChatGPT-yə yalnız etiketli mətn gedir (məs. `{{KİŞİ-01}}`). Etiketin real qarşılığı süni intellektə göndərilmir. |
| UYAP | ArthurLegal UYAP-a heç nə yazmır; UYAP-da açdığınız siyahıları kompüterinizdə oxuyur. | Claude-a və ya ChatGPT-yə iş nömrələri etiketli gedir; real dəyərlər yalnız sizin ekranınızda görünür. |
| ArthurLegal Yaddaş (Beyin) | Kompüterinizdə; siz silənə qədər qalır (ArthurLegal-ı silmək də onu silmir). | Claude-a və ya ChatGPT-yə, söhbət açılarkən yalnız seçimləriniz, düzəlişləriniz və son sessiya xülasəsi. |
| Claude-un hazırladığı fayllar (Word, Excel və bənzəri) | Kompüterinizdə, Sənədlər içindəki ArthurLegal qovluğunda; siz silənə qədər qalır. | Heç yerə. |
| Torpaq reyestri (TKGM) parsel sorğusu | Parsel identifikatoru və məlumatı serverin yaddaşında ən çox 24 saat; diskə və ya jurnala yazılmır. | Serverdən TKGM Parsel Sorğusuna. |
| Masanın dili və mövzusu | Cihazınızda. | Heç yerə. |

## Bu kompüterdə qalan qeydlər və onların silinməsi

TBB-nin süni intellekt bələdçisi prompt, çıxış və yüklənən sənədlərin saxlama müddəti bitəndə silinməsini tövsiyə
edir (s. 22). ArthurLegal-ın kompüterinizdə qoyduğu hər qeyd, nə qədər qaldığı və əl ilə necə silindiyi:

| Qeyd | Harada | Nə qədər qalır | Əl ilə silmə |
|---|---|---|---|
| Masanın tarixçəsi (suallar, cavablar, araşdırmalar) | Quraşdırmanın `veri\masa-gecmisi` qovluğu (Windows: `%LOCALAPPDATA%\Programs\ArthurLegal`, macOS: `~/Library/Application Support/ArthurLegal`); quraşdırma yoxdursa masanın brauzer yaddaşı | 90 gün və ya ən çox 2.000 qeyd; köhnələri avtomatik silinir | Masanın Tarixçə ekranında qeydin yanındakı Sil düyməsi və ya Tarixçəni təmizlə |
| İş axınlarım (yadda saxladığınız iş axınları) | Eyni qovluq | Müddətsiz (ən çox 200); Tarixçəni təmizlə onları silmir | Masanın İş axınları ekranında bir bir Sil |
| Claude-un hazırladığı fayllar | Sənədlər içindəki ArthurLegal qovluğu | Siz silənə qədər | Qovluqdakı faylı silin |
| ArthurLegal Yaddaş | Ev qovluğunuzdakı `ArthurLegal-Hafiza` (və ya quraşdırmada seçdiyiniz qovluq) | Siz silənə qədər; ArthurLegal-ı silmək onu silmir | Qovluqdakı Markdown fayllarını silin |
| ArthurMask: maskalanmış aralıq nüsxələr | Sənədlər içindəki ArthurMask qovluğunda hər işin `maskeli` qovluğu (macOS: `~/ArthurMask`) | 30 gün; ArthurMask körpüsü hər başlayanda müddəti bitənlər avtomatik silinir | Qovluqdakı faylı silin |
| ArthurMask: real adlar cədvəli (kasa), açılmış cavablar, `claude-giden.jsonl` (Claude-a göndərilən maskalanmış alət cavabları) və `kirmizi-hat.jsonl` (qırmızı xətt təsdiqləri) | Həmin işin qovluğu | Siz silənə qədər | İşin qovluğunu silin; ArthurMask-da ayrıca silmə düyməsi yoxdur |
| Masanın "Ümumi veb" ayarı (hər söhbət üçün açıq və ya bağlı) | Söhbətin qeydləri və masanın brauzer yaddaşı; müştəri məlumatı yoxdur | Söhbətin qeydləri qədər | Söhbətin qeydlərini silin; ayar onlarla silinir |
| UYAP körpüsünün şifrələnmiş arxivi (iş siyahıları, iş gedişatı, sənədlər) | Ev qovluğunuzdakı `.arthurlegal\uyap\arsiv` (`arsiv.sqlite` və şifrələnmiş `bloblar`) | İş UYAP siyahılarında sonuncu dəfə görüldükdən sonra mülki, icra və inzibati işlərdə 1.095 gün, cinayət işlərində 730 gün; körpü hər başlayanda müddəti bitənlər silinir | Claude Desktop-u bağlayıb `arsiv` qovluğunu silin; körpü növbəti açılışda boş arxivlə başlayır |

ArthurLegal bu qeydləri sizin əvəzinizə başqa müddətlə silmir; büronuzun saxlama və məhvetmə qaydası daha uzun və ya
daha qısa müddət nəzərdə tutursa, silməni o qaydaya görə özünüz edirsiniz.

## Claude ayarınız

ArthurLegal sizin Claude hesabınızla işləyir və bu hesabın ayarlarını görə və dəyişə bilmir. Claude-dan **Free, Pro
və ya Max** planı ilə istifadə edirsinizsə, **Ayarlar › Məxfilik** bölməsindəki model təkmilləşdirmə ayarı açıq olduğu
müddətdə yeni söhbətləriniz Anthropic-in modellərinin təkmilləşdirilməsində istifadə oluna bilər. Müştəri məlumatı
daxil etməzdən əvvəl bu ayarı yoxlayın və müştəri sənədini ArthurMask-dən keçirin. Team, Enterprise və API istifadəsi
Anthropic-in kommersiya şərtlərinə tabedir. Mənbə: [Anthropic, model təkmilləşdirmə məxfilik ayarı](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings).

## ChatGPT ayarınız

Quraşdırmada ChatGPT-ni seçmisinizsə, ArthurLegal sizin ChatGPT hesabınızla, ChatGPT masaüstü tətbiqində işləyir.
ChatGPT-yə sualınız, ChatGPT-nin alətlərdən aldığı nəticələr (qanunvericilik, məhkəmə təcrübəsi, qərarlar kimi rəsmi
mənbələrdən gələn mətnlər) və ArthurMask ilə **maskalanmış** sənəd mətni gedir. ArthurMask-ın real adlar cədvəli,
Yaddaş qovluğu, masanın tarixçəsi, UYAP məlumatları və Tapu qeydinin mətni Claude-da olduğu kimi kompüterinizdə qalır.
ArthurLegal-ın uzaq araşdırma serveri sualın məzmununu qeydə almır. ChatGPT-nin məlumat və məxfilik ayarları
OpenAI-ın hesabınıza tətbiq etdiyi şərtlərə tabedir; ArthurLegal onları dəyişmir. Quraşdırma ChatGPT-yə yalnız
ArthurLegal-ın serverlərini və bacarıqlarını əlavə edir. Müştəri məlumatı daxil etməzdən əvvəl ChatGPT-nin məlumat və
məxfilik ayarlarını yoxlayın.

Fərdi məlumatların xaricə ötürülməsi (Türkiyənin 6698 saylı Kişisel Verilerin Korunması Kanunu, KVKK, 9-cu maddə)
baxımından qiymətləndirmə Claude-da olduğu kimi ChatGPT-də də istifadəçiyə aiddir; müştəri sənədini ArthurMask-dən
keçirin.

KVKK-nın vəkillər üçün bələdçisinə görə, provayder Türkiyədə olsa belə, fərdi məlumat olan sənədi süni intellekt
alətinə vermək ölkə daxilində ötürmə (8-ci maddə) sayıla bilər. Axtarış xanasına və araşdırma sorğusuna da müştəri
adını və ya iş təfərrüatını yazmayın: ArthurLegal-ın araşdırma serveri Amsterdamdadır və semantik axtarışın mətni
Voyage AI-a gedir.

## Nəticə haqqında

- ArthurLegal-ın, Claude-un və ChatGPT-nin nəticəsi **hüquqi rəy deyil**.
- Nəticə **səhv və ya natamam ola bilər**.
- **Vəkil istifadə etməzdən əvvəl rəsmi mənbədən yoxlayır**; peşə məsuliyyəti vəkildədir.

Masadakı istinad yoxlaması maddə nömrəsinin və başlığının rəsmi mətndə olduğunu göstərir. Maddənin cümlədə ona aid
edilən məzmunu (hüququn sahibi, şərt, müddət, nəticə) həqiqətən deyib-demədiyini vəkil oxuyur; masanın "Mətni göstər"
düyməsi cümləni və rəsmi mətni yan-yana açır. Mənbə məlumat verməsə ArthurLegal boşluğu doldurmur, bu sətri yazır:
`UYARI: veri çekilemedi, teyidiniz gerekli: <keçid>` ("xəbərdarlıq: məlumat alına bilmədi, təsdiqiniz lazımdır").

## Yoxlamaq istəsəniz

- Uzaq serverin ətraflı məxfilik sənədi: [arthurlegal-mcp/PRIVACY.md](https://github.com/beerbottle90/arthurlegal-mcp/blob/master/PRIVACY.md)
- ArthurMask necə işləyir: [arthur-mask](https://github.com/beerbottle90/arthur-mask)
- Quraşdırmanın ChatGPT-yə nə yazdığı: [codex_ayari.py](../ArthurLegal-setup/istemci/codex_ayari.py) (ayar faylına yalnız ArthurLegal-ın sətirləri yazılır, fayl dəyişdirilməzdən əvvəl ehtiyat nüsxəsi çıxarılır; bacarıqlar adı `arthurlegal` ilə başlayan qovluqlardır)
- Bu depo: quraşdırmanın və masanın bütün kodu.

Bu səhifə hər buraxılışla yenidən nəzərdən keçirilir; dəyişiklik tarixçəsi depodadır.

<sub>ChatGPT və OpenAI OpenAI-ın ticarət nişanlarıdır.</sub>
