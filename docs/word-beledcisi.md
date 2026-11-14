# Word-də ArthurLegal

[Türkçe](word-rehberi.md) · [English](word-guide.md)

Anthropic-in Word əlavəsi Claude-u sənədin yanında bir paneldə açır. ArthurLegal-in araşdırma bağlayıcısı claude.ai
hesabınıza qoşulubsa, Word-dəki Claude da Türkiyə qanunvericiliyini və məhkəmə təcrübəsini rəsmi mənbədən canlı
gətirir: maddəni sənədin yanında oxuyur, düzəlişi izlənən dəyişiklik kimi təklif edir, əsaslandırmanı şərh kimi
qoyur. Ayrıca quraşdırma və ya ödəniş yoxdur; Claude abunəliyinizlə işləyir.

## Nə lazımdır

- **Claude planı:** Pro, Max, Team və ya Enterprise.
- **Word versiyası:**
  - Word-ün veb versiyası (brauzerdə; pulsuz Microsoft hesabı da kifayətdir), və ya
  - Microsoft 365 abunəliyi ilə Windows-da Word, Version 2205 (build 15202.10000) və ya daha yeni, və ya
  - Mac-da Word 16.61 və ya daha yeni.
- **İşləmir:** Word 2016 və 2019 (daimi və ya toplu lisenziya), iPad və Android-də Word, `.doc` faylı (əvvəlcə
  `.docx` kimi yadda saxlayın). Daimi lisenziyalı Word 2021 və 2024 rəsmi səhifədə qeyd olunmur; əmin deyilsinizsə,
  Word-ün veb versiyasından istifadə edin.

Kompüterinizdəki Word köhnədirsə, əlavəni mağazada ümumiyyətlə görməyəcəksiniz. Bu axtarış xətası deyil; Word-ün veb
versiyası problemsiz işləyir.

## Quraşdırma

1. **ArthurLegal bağlayıcısı:** claude.ai-də Settings › Connectors bölməsində ArthurLegal qoşulu olmalıdır. Qoşulu
   deyilsə, **Add custom connector** ilə bu ünvanı əlavə edin: `https://arthurlegal-mcp.fly.dev/mcp`
2. **Word-ü açın:** Word-ün veb versiyasını (word.cloud.microsoft) və ya Microsoft 365 Word-ü açın və bir sənəd açın.
3. **Əlavəni quraşdırın:** **Home › Add-ins** (bəzi görünüşlərdə **Insert › Add-ins**) düyməsini basın, axtarışa
   `Claude` yazın. Mağazadakı adı **Claude for Microsoft 365**-dir (naşir Anthropic); "Claude for Word" kimi
   axtarılarsa, çıxmaya bilər. **Add** düyməsini basın. Mağaza səhifəsi:
   [Claude for Microsoft 365](https://marketplace.microsoft.com/en-us/product/office/WA200010725)
4. **Daxil olun:** sağda açılan Claude panelində **Claude hesabınızla** daxil olun. Bu, Microsoft hesabınızdan
   ayrıdır; Claude abunəliyiniz hansı hesabdadırsa, onu istifadə edin.

### Büro və ya şirkət hesabında əlavə görünmürsə

Bəzi təşkilatlarda əlavə quraşdırmağa inzibatçı icazə verir. Microsoft 365 inzibatçı mərkəzində:

- **Settings › Org settings › User owned apps and services**: "Let users access the Office Store" açıq olmalıdır, və ya
- **Settings › Integrated apps › Add-ins**: Claude for Microsoft 365 axtarılır və təşkilata, şəxslərə və ya qruplara
  təyin edilir. Bütün təşkilata yayılması 24 saata qədər çəkə bilər.

Mağaza bağlı saxlanılırsa, Anthropic-in Word səhifəsi inzibatçının yükləyə biləcəyi əlavə faylı da verir (aşağıdakı
mənbələrə baxın).

## Nümunə istifadələr

Əvvəlcə müvafiq mətni seçin, sonra panelə yazın.

- **Maddənin yoxlanılması:** "Bu maddəni Türkiyə Borclar Qanununa görə yoxla; əsaslandığın maddəni ArthurLegal ilə
  rəsmi mətndən gətir." Cavabın üstündə **Used … tools** sətri görünür; bu, Claude-un maddəni yaddaşdan deyil, alətlə
  gətirdiyini göstərir. Maddənin mətni mevzuat.gov.tr keçidi ilə gəlməlidir.
- **İzlənən dəyişikliklə düzəliş:** "Bu maddəni qanuna uyğun olacaq şəkildə yenidən yaz, dəyişikliyi izlənən dəyişiklik
  kimi tətbiq et və əsaslandırmanı şərh kimi əlavə et." Dəyişikliklər Word-ün öz **Review** bölməsində qəbul və ya
  rədd edilir; geri qaytarmaq üçün Ctrl+Z (Mac-da Cmd+Z).
- **Şərhlərə görə düzəliş:** "Sənəddəki şərhləri ardıcıllıqla işlə, hər birini izlənən dəyişiklik kimi tətbiq et."
  Claude hər şərh zəncirinə nə etdiyini yazır.
- **Qarşı tərəfin dəyişiklikləri:** "Qarşı tərəfin izlənən dəyişikliklərini xülasə et; qanuna zidd və ya müştərinin
  əleyhinə olanları qeyd et."
- **Bacarıqlar:** Claude ayarlarınızda açıq olan bacarıqlar Word-də də işləyir. Paneldə `/` yazanda siyahılanır.

## Hədlər

- **Yalnız araşdırma bağlayıcısı gəlir.** Word-dəki Claude claude.ai hesabınızdakı bağlayıcılardan istifadə edir.
  Kompüterinizdə işləyən ArthurMask, UYAP Dashboard, Beyin və ArthurLegal Masası Word-də görünmür.
- **Sənədin məzmunu Anthropic-ə gedir.** Claude hesabı ilə daxil olduqda söhbət, Claude-un sənəddən oxuduğu məzmun
  (mətn, şərhlər, izlənən dəyişikliklər, haşiyələr, cədvəllər) və əlavə etdiyiniz fayllar Anthropic-ə göndərilir.
  ArthurMask burada araya girmir: müştəri sirri və ya şəxsi məlumat olan sənəddə əvvəlcə ArthurMask ilə maskalayın,
  Word-də maskalanmış sənədlə işləyin. Ətraflı: [Məlumatlarınız hara gedir](melumatlariniz.md).
- **Saxlama.** Anthropic-in Word səhifəsinə görə girişlər və çıxışlar məxfilik səhifəsindəki istisnalar xaricində 30
  gün ərzində silinir. Təşkilatınızın xüsusi saxlama ayarları bu əlavəyə tətbiq olunmur. Söhbət tarixçəsi yalnız həmin
  brauzerdə qalır (hər tətbiq üçün son 50 söhbət). Əlavə sənədə öz identifikatorunu yazır; sənəd paylaşılanda bu
  məlumat da sənədlə gedir.
- **Son yoxlama vəkilindir.** Anthropic də əlavədən yalnız etibarlı sənədlərlə istifadə etməyi və müştəriyə və ya qarşı
  tərəfə gedəcək son mətni insan yoxlamasından keçirməyi tövsiyə edir. ArthurLegal hüquqi rəy vermir; tapdığı mənbə
  ilə işinizi sürətləndirir.

## Mənbələr

- Anthropic, Claude for Word: https://claude.com/docs/office-agents/word
- Anthropic, Connectors and skills: https://claude.com/docs/office-agents/connectors-and-skills
- Anthropic, Data storage: https://claude.com/docs/office-agents/data-storage
- Microsoft Marketplace, Claude for Microsoft 365: https://marketplace.microsoft.com/en-us/product/office/WA200010725

Rəsmi səhifələr dəyişə bilər; versiya tələbində tərəddüd etsəniz, əvvəlcə Anthropic-in Word səhifəsinə baxın.

---

Microsoft, Word və Microsoft 365 Microsoft şirkətlər qrupunun ticarət nişanlarıdır. Claude Anthropic-in ticarət
nişanıdır. ArthurLegal bu şirkətlərlə əlaqəli deyil; adlar yalnız uyğunluğu bildirmək üçün çəkilir.
