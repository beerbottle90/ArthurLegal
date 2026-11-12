; *** Inno Setup version 6.5.0+ Azerbaijani (Latin) messages ***
;
; ArthurLegal kurulumunun Azerbaycanca iletileri: Default.isl'in (Inno Setup 6.5+) bütün iletilerinin çevirisi.
; Bu dosya UTF-8 BOM ile kaydedilmelidir (yayin/derle.py denetler). Yeni bir Inno Setup sürümü Default.isl'e ileti
; eklerse buraya da eklenir; eksik ileti derlemede uyarı verir ve İngilizce görünür.
;
; Note: When translating this text, do not add periods (.) to the end of
; messages that didn't have them already, because on those messages Inno
; Setup adds the periods automatically (appending a period would result in
; two periods being displayed).

[LangOptions]
; The following three entries are very important. Be sure to read and
; understand the '[LangOptions] section' topic in the help file.
LanguageName=Az<0259>rbaycan dili
LanguageID=$042C
; LanguageCodePage should always be set if possible, even if this file is Unicode
LanguageCodePage=1254
; If the language you are translating to requires special font faces or
; sizes, uncomment any of the following entries and change them accordingly.
;DialogFontName=
;DialogFontSize=9
;DialogFontBaseScaleWidth=7
;DialogFontBaseScaleHeight=15
;WelcomeFontName=Segoe UI
;WelcomeFontSize=14

[Messages]

; *** Application titles
SetupAppTitle=Quraşdırma
SetupWindowTitle=Quraşdırma - %1
UninstallAppTitle=Silmə
UninstallAppFullTitle=%1 - Silmə

; *** Misc. common
InformationTitle=Məlumat
ConfirmTitle=Təsdiq
ErrorTitle=Xəta

; *** SetupLdr messages
SetupLdrStartupMessage=%1 quraşdırılacaq. Davam etmək istəyirsiniz?
LdrCannotCreateTemp=Müvəqqəti fayl yaradıla bilmədi. Quraşdırma dayandırıldı
LdrCannotExecTemp=Müvəqqəti qovluqdakı fayl işə salına bilmədi. Quraşdırma dayandırıldı
HelpTextNote=

; *** Startup error messages
LastErrorMessage=%1.%n%nXəta %2: %3
SetupFileMissing=Quraşdırma qovluğunda %1 faylı çatışmır. Zəhmət olmasa, problemi aradan qaldırın və ya proqramın yeni nüsxəsini əldə edin.
SetupFileCorrupt=Quraşdırma faylları zədələnib. Zəhmət olmasa, proqramın yeni nüsxəsini əldə edin.
SetupFileCorruptOrWrongVer=Quraşdırma faylları zədələnib və ya quraşdırma proqramının bu versiyası ilə uyğun deyil. Zəhmət olmasa, problemi aradan qaldırın və ya proqramın yeni nüsxəsini əldə edin.
InvalidParameter=Əmr sətrində yanlış parametr verilib:%n%n%1
SetupAlreadyRunning=Quraşdırma artıq işləyir.
WindowsVersionNotSupported=Bu proqram kompüterinizdəki Windows versiyasını dəstəkləmir.
WindowsServicePackRequired=Bu proqram üçün %1 Service Pack %2 və ya daha yenisi tələb olunur.
NotOnThisPlatform=Bu proqram %1 üzərində işləmir.
OnlyOnThisPlatform=Bu proqram yalnız %1 üzərində işə salına bilər.
OnlyOnTheseArchitectures=Bu proqram yalnız aşağıdakı prosessor arxitekturaları üçün nəzərdə tutulmuş Windows versiyalarına quraşdırıla bilər:%n%n%1
WinVersionTooLowError=Bu proqram üçün %1 versiya %2 və ya daha yenisi tələb olunur.
WinVersionTooHighError=Bu proqram %1 versiya %2 və ya daha yenisinə quraşdırıla bilməz.
AdminPrivilegesRequired=Bu proqramı quraşdırmaq üçün sistemə administrator kimi daxil olmalısınız.
PowerUserPrivilegesRequired=Bu proqramı quraşdırmaq üçün sistemə administrator və ya Power Users qrupunun üzvü kimi daxil olmalısınız.
SetupAppRunningError=Quraşdırma %1 proqramının hazırda işlədiyini aşkar etdi.%n%nZəhmət olmasa, onun bütün pəncərələrini indi bağlayın, sonra davam etmək üçün "OK", çıxmaq üçün "Ləğv et" düyməsinə klikləyin.
UninstallAppRunningError=Silmə proqramı %1 proqramının hazırda işlədiyini aşkar etdi.%n%nZəhmət olmasa, onun bütün pəncərələrini indi bağlayın, sonra davam etmək üçün "OK", çıxmaq üçün "Ləğv et" düyməsinə klikləyin.

; *** Startup questions
PrivilegesRequiredOverrideTitle=Quraşdırma rejimini seçin
PrivilegesRequiredOverrideInstruction=Quraşdırma rejimini seçin
PrivilegesRequiredOverrideText1=%1 bütün istifadəçilər üçün (administrator hüquqları tələb olunur) və ya yalnız sizin üçün quraşdırıla bilər.
PrivilegesRequiredOverrideText2=%1 yalnız sizin üçün və ya bütün istifadəçilər üçün (administrator hüquqları tələb olunur) quraşdırıla bilər.
PrivilegesRequiredOverrideAllUsers=&Bütün istifadəçilər üçün quraşdır
PrivilegesRequiredOverrideAllUsersRecommended=&Bütün istifadəçilər üçün quraşdır (tövsiyə olunur)
PrivilegesRequiredOverrideCurrentUser=&Yalnız mənim üçün quraşdır
PrivilegesRequiredOverrideCurrentUserRecommended=&Yalnız mənim üçün quraşdır (tövsiyə olunur)

; *** Misc. errors
ErrorCreatingDir=Quraşdırma "%1" qovluğunu yarada bilmədi
ErrorTooManyFilesInDir="%1" qovluğunda fayl yaradıla bilmədi, çünki orada həddindən çox fayl var

; *** Setup common messages
ExitSetupTitle=Quraşdırmadan çıxış
ExitSetupMessage=Quraşdırma tamamlanmayıb. İndi çıxsanız, proqram quraşdırılmayacaq.%n%nQuraşdırmanı tamamlamaq üçün onu başqa vaxt yenidən işə sala bilərsiniz.%n%nQuraşdırmadan çıxmaq istəyirsiniz?
AboutSetupMenuItem=Quraşdırma &haqqında...
AboutSetupTitle=Quraşdırma haqqında
AboutSetupMessage=%1 versiya %2%n%3%n%n%1 ana səhifəsi:%n%4
AboutSetupNote=
TranslatorNote=

; *** Buttons
ButtonBack=< &Geri
ButtonNext=&Növbəti >
ButtonInstall=&Quraşdır
ButtonOK=OK
ButtonCancel=Ləğv et
ButtonYes=&Bəli
ButtonYesToAll=&Hamısına bəli
ButtonNo=&Xeyr
ButtonNoToAll=Hamısına x&eyr
ButtonFinish=&Bitir
ButtonBrowse=&Gözdən keçir...
ButtonWizardBrowse=Gö&zdən keçir...
ButtonNewFolder=&Yeni qovluq yarat

; *** "Select Language" dialog messages
SelectLanguageTitle=Quraşdırma dilini seçin
SelectLanguageLabel=Quraşdırma zamanı istifadə olunacaq dili seçin.

; *** Common wizard text
ClickNext=Davam etmək üçün "Növbəti", quraşdırmadan çıxmaq üçün "Ləğv et" düyməsinə klikləyin.
BeveledLabel=
BrowseDialogTitle=Qovluq seçin
BrowseDialogLabel=Aşağıdakı siyahıdan qovluq seçin, sonra "OK" düyməsinə klikləyin.
NewFolderName=Yeni qovluq

; *** "Welcome" wizard page
WelcomeLabel1=[name] quraşdırma sehrbazına xoş gəlmisiniz
WelcomeLabel2=Bu sehrbaz [name/ver] proqramını kompüterinizə quraşdıracaq.%n%nDavam etməzdən əvvəl bütün digər proqramları bağlamağınız tövsiyə olunur.

; *** "Password" wizard page
WizardPassword=Parol
PasswordLabel1=Bu quraşdırma parolla qorunur.
PasswordLabel3=Zəhmət olmasa, parolu daxil edin, sonra davam etmək üçün "Növbəti" düyməsinə klikləyin. Parollarda böyük və kiçik hərflər fərqləndirilir.
PasswordEditLabel=&Parol:
IncorrectPassword=Daxil etdiyiniz parol düzgün deyil. Zəhmət olmasa, yenidən cəhd edin.

; *** "License Agreement" wizard page
WizardLicense=Lisenziya müqaviləsi
LicenseLabel=Zəhmət olmasa, davam etməzdən əvvəl aşağıdakı vacib məlumatı oxuyun.
LicenseLabel3=Zəhmət olmasa, aşağıdakı lisenziya müqaviləsini oxuyun. Quraşdırmaya davam etmək üçün bu müqavilənin şərtlərini qəbul etməlisiniz.
LicenseAccepted=Müqaviləni &qəbul edirəm
LicenseNotAccepted=Müqaviləni qəbul &etmirəm

; *** "Information" wizard pages
WizardInfoBefore=Məlumat
InfoBeforeLabel=Zəhmət olmasa, davam etməzdən əvvəl aşağıdakı vacib məlumatı oxuyun.
InfoBeforeClickLabel=Quraşdırmaya davam etməyə hazır olduqda "Növbəti" düyməsinə klikləyin.
WizardInfoAfter=Məlumat
InfoAfterLabel=Zəhmət olmasa, davam etməzdən əvvəl aşağıdakı vacib məlumatı oxuyun.
InfoAfterClickLabel=Quraşdırmaya davam etməyə hazır olduqda "Növbəti" düyməsinə klikləyin.

; *** "User Information" wizard page
WizardUserInfo=İstifadəçi məlumatı
UserInfoDesc=Zəhmət olmasa, məlumatlarınızı daxil edin.
UserInfoName=İ&stifadəçi adı:
UserInfoOrg=&Təşkilat:
UserInfoSerial=Seriya &nömrəsi:
UserInfoNameRequired=Ad daxil etməlisiniz.

; *** "Select Destination Location" wizard page
WizardSelectDir=Quraşdırma yerini seçin
SelectDirDesc=[name] hara quraşdırılsın?
SelectDirLabel3=Quraşdırma [name] proqramını aşağıdakı qovluğa quraşdıracaq.
SelectDirBrowseLabel=Davam etmək üçün "Növbəti" düyməsinə klikləyin. Başqa qovluq seçmək istəyirsinizsə, "Gözdən keçir" düyməsinə klikləyin.
DiskSpaceGBLabel=Ən azı [gb] GB boş disk sahəsi tələb olunur.
DiskSpaceMBLabel=Ən azı [mb] MB boş disk sahəsi tələb olunur.
CannotInstallToNetworkDrive=Quraşdırma şəbəkə diskinə aparıla bilməz.
CannotInstallToUNCPath=Quraşdırma UNC yoluna aparıla bilməz.
InvalidPath=Disk hərfi ilə birlikdə tam yol daxil etməlisiniz; məsələn:%n%nC:\APP%n%nvə ya bu formada UNC yolu:%n%n\\server\share
InvalidDrive=Seçdiyiniz disk və ya UNC paylaşımı mövcud deyil və ya ona giriş mümkün deyil. Zəhmət olmasa, başqasını seçin.
DiskSpaceWarningTitle=Disk sahəsi kifayət deyil
DiskSpaceWarning=Quraşdırma üçün ən azı %1 KB boş sahə tələb olunur, lakin seçilmiş diskdə yalnız %2 KB boş sahə var.%n%nYenə də davam etmək istəyirsiniz?
DirNameTooLong=Qovluğun adı və ya yolu çox uzundur.
InvalidDirName=Qovluğun adı düzgün deyil.
BadDirName32=Qovluq adlarında aşağıdakı simvollardan heç biri ola bilməz:%n%n%1
DirExistsTitle=Qovluq mövcuddur
DirExists=Bu qovluq:%n%n%1%n%nartıq mövcuddur. Yenə də həmin qovluğa quraşdırmaq istəyirsiniz?
DirDoesntExistTitle=Qovluq mövcud deyil
DirDoesntExist=Bu qovluq:%n%n%1%n%nmövcud deyil. Qovluğun yaradılmasını istəyirsiniz?

; *** "Select Components" wizard page
WizardSelectComponents=Komponentləri seçin
SelectComponentsDesc=Hansı komponentlər quraşdırılsın?
SelectComponentsLabel2=Quraşdırmaq istədiyiniz komponentləri işarələyin; quraşdırmaq istəmədiklərinizin işarəsini götürün. Davam etməyə hazır olduqda "Növbəti" düyməsinə klikləyin.
FullInstallation=Tam quraşdırma
; if possible don't translate 'Compact' as 'Minimal' (I mean 'Minimal' in your language)
CompactInstallation=Yığcam quraşdırma
CustomInstallation=Fərdi quraşdırma
NoUninstallWarningTitle=Komponentlər mövcuddur
NoUninstallWarning=Quraşdırma aşağıdakı komponentlərin kompüterinizdə artıq quraşdırıldığını aşkar etdi:%n%n%1%n%nBu komponentlərin işarəsini götürmək onları silməyəcək.%n%nYenə də davam etmək istəyirsiniz?
ComponentSize1=%1 KB
ComponentSize2=%1 MB
ComponentsDiskSpaceGBLabel=Cari seçim üçün ən azı [gb] GB disk sahəsi tələb olunur.
ComponentsDiskSpaceMBLabel=Cari seçim üçün ən azı [mb] MB disk sahəsi tələb olunur.

; *** "Select Additional Tasks" wizard page
WizardSelectTasks=Əlavə tapşırıqları seçin
SelectTasksDesc=Hansı əlavə tapşırıqlar yerinə yetirilsin?
SelectTasksLabel2=[name] quraşdırılarkən yerinə yetirilməsini istədiyiniz əlavə tapşırıqları seçin, sonra "Növbəti" düyməsinə klikləyin.

; *** "Select Start Menu Folder" wizard page
WizardSelectProgramGroup="Başlat" menyusu qovluğunu seçin
SelectStartMenuFolderDesc=Quraşdırma proqramın qısayollarını hara yerləşdirsin?
SelectStartMenuFolderLabel3=Quraşdırma proqramın qısayollarını "Başlat" menyusunun aşağıdakı qovluğunda yaradacaq.
SelectStartMenuFolderBrowseLabel=Davam etmək üçün "Növbəti" düyməsinə klikləyin. Başqa qovluq seçmək istəyirsinizsə, "Gözdən keçir" düyməsinə klikləyin.
MustEnterGroupName=Qovluq adı daxil etməlisiniz.
GroupNameTooLong=Qovluğun adı və ya yolu çox uzundur.
InvalidGroupName=Qovluğun adı düzgün deyil.
BadGroupName=Qovluq adında aşağıdakı simvollardan heç biri ola bilməz:%n%n%1
NoProgramGroupCheck2="Başlat" menyusunda qovluq &yaradılmasın

; *** "Ready to Install" wizard page
WizardReady=Quraşdırmağa hazırdır
ReadyLabel1=Quraşdırma [name] proqramını kompüterinizə quraşdırmağa hazırdır.
ReadyLabel2a=Quraşdırmaya davam etmək üçün "Quraşdır" düyməsinə, parametrlərə baxmaq və ya onları dəyişmək istəyirsinizsə, "Geri" düyməsinə klikləyin.
ReadyLabel2b=Quraşdırmaya davam etmək üçün "Quraşdır" düyməsinə klikləyin.
ReadyMemoUserInfo=İstifadəçi məlumatı:
ReadyMemoDir=Quraşdırma yeri:
ReadyMemoType=Quraşdırma növü:
ReadyMemoComponents=Seçilmiş komponentlər:
ReadyMemoGroup="Başlat" menyusu qovluğu:
ReadyMemoTasks=Əlavə tapşırıqlar:

; *** TDownloadWizardPage wizard page and DownloadTemporaryFile
DownloadingLabel2=Fayllar yüklənir...
ButtonStopDownload=Yükləməni &dayandır
StopDownload=Yükləməni dayandırmaq istədiyinizə əminsiniz?
ErrorDownloadAborted=Yükləmə dayandırıldı
ErrorDownloadFailed=Yükləmə alınmadı: %1 %2
ErrorDownloadSizeFailed=Ölçü alına bilmədi: %1 %2
ErrorProgress=Yanlış irəliləyiş: %1 / %2
ErrorFileSize=Yanlış fayl ölçüsü: gözlənilən %1, tapılan %2

; *** TExtractionWizardPage wizard page and ExtractArchive
ExtractingLabel=Fayllar çıxarılır...
ButtonStopExtraction=Çıxarmanı &dayandır
StopExtraction=Çıxarmanı dayandırmaq istədiyinizə əminsiniz?
ErrorExtractionAborted=Çıxarma dayandırıldı
ErrorExtractionFailed=Çıxarma alınmadı: %1

; *** Archive extraction failure details
ArchiveIncorrectPassword=Parol düzgün deyil
ArchiveIsCorrupted=Arxiv zədələnib
ArchiveUnsupportedFormat=Arxivin formatı dəstəklənmir

; *** "Preparing to Install" wizard page
WizardPreparing=Quraşdırmaya hazırlıq
PreparingDesc=Quraşdırma [name] proqramını kompüterinizə quraşdırmağa hazırlaşır.
PreviousInstallNotCompleted=Əvvəlki bir proqramın quraşdırılması və ya silinməsi tamamlanmayıb. Həmin əməliyyatı tamamlamaq üçün kompüterinizi yenidən başlatmalısınız.%n%nKompüteri yenidən başlatdıqdan sonra [name] proqramının quraşdırılmasını tamamlamaq üçün quraşdırmanı yenidən işə salın.
CannotContinue=Quraşdırma davam edə bilmir. Çıxmaq üçün "Ləğv et" düyməsinə klikləyin.
ApplicationsFound=Aşağıdakı proqramlar quraşdırmanın yeniləməli olduğu fayllardan istifadə edir. Quraşdırmanın bu proqramları avtomatik bağlamasına icazə verməyiniz tövsiyə olunur.
ApplicationsFound2=Aşağıdakı proqramlar quraşdırmanın yeniləməli olduğu fayllardan istifadə edir. Quraşdırmanın bu proqramları avtomatik bağlamasına icazə verməyiniz tövsiyə olunur. Quraşdırma tamamlandıqdan sonra proqramları yenidən başlatmağa çalışacaq.
CloseApplications=Proqramları &avtomatik bağla
DontCloseApplications=Proqramları &bağlama
ErrorCloseApplications=Quraşdırma bütün proqramları avtomatik bağlaya bilmədi. Davam etməzdən əvvəl quraşdırmanın yeniləməli olduğu fayllardan istifadə edən bütün proqramları bağlamağınız tövsiyə olunur.
PrepareToInstallNeedsRestart=Quraşdırma kompüterinizi yenidən başlatmalıdır. Kompüteri yenidən başlatdıqdan sonra [name] proqramının quraşdırılmasını tamamlamaq üçün quraşdırmanı yenidən işə salın.%n%nİndi yenidən başlatmaq istəyirsiniz?

; *** "Installing" wizard page
WizardInstalling=Quraşdırılır
InstallingLabel=Zəhmət olmasa, [name] kompüterinizə quraşdırılana qədər gözləyin.

; *** "Setup Completed" wizard page
FinishedHeadingLabel=[name] quraşdırma sehrbazı tamamlanır
FinishedLabelNoIcons=[name] proqramının kompüterinizə quraşdırılması başa çatdı.
FinishedLabel=[name] proqramının kompüterinizə quraşdırılması başa çatdı. Proqramı quraşdırılmış qısayolları seçməklə işə sala bilərsiniz.
ClickFinish=Quraşdırmadan çıxmaq üçün "Bitir" düyməsinə klikləyin.
FinishedRestartLabel=[name] proqramının quraşdırılmasını tamamlamaq üçün kompüteriniz yenidən başladılmalıdır. İndi yenidən başlatmaq istəyirsiniz?
FinishedRestartMessage=[name] proqramının quraşdırılmasını tamamlamaq üçün kompüteriniz yenidən başladılmalıdır.%n%nİndi yenidən başlatmaq istəyirsiniz?
ShowReadmeCheck=Bəli, README faylına baxmaq istəyirəm
YesRadio=&Bəli, kompüter indi yenidən başladılsın
NoRadio=&Xeyr, kompüteri sonra özüm yenidən başladacağam
; used for example as 'Run MyProg.exe'
RunEntryExec=%1 proqramını işə sal
; used for example as 'View Readme.txt'
RunEntryShellExec=%1 faylına bax

; *** "Setup Needs the Next Disk" stuff
ChangeDiskTitle=Quraşdırma üçün növbəti disk lazımdır
SelectDiskLabel2=Zəhmət olmasa, %1 nömrəli diski yerləşdirin və "OK" düyməsinə klikləyin.%n%nBu diskdəki fayllar aşağıda göstəriləndən başqa qovluqdadırsa, düzgün yolu daxil edin və ya "Gözdən keçir" düyməsinə klikləyin.
PathLabel=&Yol:
FileNotInDir2="%1" faylı "%2" yerində tapılmadı. Zəhmət olmasa, düzgün diski yerləşdirin və ya başqa qovluq seçin.
SelectDirectoryLabel=Zəhmət olmasa, növbəti diskin yerini göstərin.

; *** Installation phase messages
SetupAborted=Quraşdırma tamamlanmadı.%n%nZəhmət olmasa, problemi aradan qaldırın və quraşdırmanı yenidən işə salın.
AbortRetryIgnoreSelectAction=Əməliyyatı seçin
AbortRetryIgnoreRetry=&Yenidən cəhd et
AbortRetryIgnoreIgnore=Xətanı &nəzərə alma və davam et
AbortRetryIgnoreCancel=Quraşdırmanı ləğv et
RetryCancelSelectAction=Əməliyyatı seçin
RetryCancelRetry=&Yenidən cəhd et
RetryCancelCancel=Ləğv et

; *** Installation status messages
StatusClosingApplications=Proqramlar bağlanır...
StatusCreateDirs=Qovluqlar yaradılır...
StatusExtractFiles=Fayllar çıxarılır...
StatusDownloadFiles=Fayllar yüklənir...
StatusCreateIcons=Qısayollar yaradılır...
StatusCreateIniEntries=INI qeydləri yaradılır...
StatusCreateRegistryEntries=Reyestr qeydləri yaradılır...
StatusRegisterFiles=Fayllar qeydiyyata alınır...
StatusSavingUninstall=Silmə məlumatı saxlanılır...
StatusRunProgram=Quraşdırma başa çatdırılır...
StatusRestartingApplications=Proqramlar yenidən başladılır...
StatusRollback=Dəyişikliklər geri qaytarılır...

; *** Misc. errors
ErrorInternal2=Daxili xəta: %1
ErrorFunctionFailedNoCode=%1 uğursuz oldu
ErrorFunctionFailed=%1 uğursuz oldu; kod %2
ErrorFunctionFailedWithMessage=%1 uğursuz oldu; kod %2.%n%3
ErrorExecutingProgram=Fayl işə salına bilmədi:%n%1

; *** Registry errors
ErrorRegOpenKey=Reyestr açarı açılarkən xəta baş verdi:%n%1\%2
ErrorRegCreateKey=Reyestr açarı yaradılarkən xəta baş verdi:%n%1\%2
ErrorRegWriteKey=Reyestr açarına yazılarkən xəta baş verdi:%n%1\%2

; *** INI errors
ErrorIniEntry="%1" faylında INI qeydi yaradılarkən xəta baş verdi.

; *** File copying errors
FileAbortRetryIgnoreSkipNotRecommended=Bu faylı &ötür (tövsiyə olunmur)
FileAbortRetryIgnoreIgnoreNotRecommended=Xətanı &nəzərə alma və davam et (tövsiyə olunmur)
SourceIsCorrupted=Mənbə fayl zədələnib
SourceDoesntExist="%1" mənbə faylı mövcud deyil
SourceVerificationFailed=Mənbə faylın yoxlanması uğursuz oldu: %1
VerificationSignatureDoesntExist="%1" imza faylı mövcud deyil
VerificationSignatureInvalid="%1" imza faylı etibarsızdır
VerificationKeyNotFound="%1" imza faylı naməlum açardan istifadə edir
VerificationFileNameIncorrect=Faylın adı düzgün deyil
VerificationFileTagIncorrect=Faylın etiketi düzgün deyil
VerificationFileSizeIncorrect=Faylın ölçüsü düzgün deyil
VerificationFileHashIncorrect=Faylın heş dəyəri düzgün deyil
ExistingFileReadOnly2=Mövcud fayl "yalnız oxunan" kimi işarələndiyi üçün əvəz edilə bilmədi.
ExistingFileReadOnlyRetry="Yalnız oxunan" atributunu &götür və yenidən cəhd et
ExistingFileReadOnlyKeepExisting=Mövcud faylı &saxla
ErrorReadingExistingDest=Mövcud fayl oxunarkən xəta baş verdi:
FileExistsSelectAction=Əməliyyatı seçin
FileExists2=Fayl artıq mövcuddur.
FileExistsOverwriteExisting=Mövcud faylın &üzərinə yaz
FileExistsKeepExisting=Mövcud faylı &saxla
FileExistsOverwriteOrKeepAll=Növbəti toqquşmalarda da &belə et
ExistingFileNewerSelectAction=Əməliyyatı seçin
ExistingFileNewer2=Mövcud fayl quraşdırmanın yazmağa çalışdığı fayldan daha yenidir.
ExistingFileNewerOverwriteExisting=Mövcud faylın &üzərinə yaz
ExistingFileNewerKeepExisting=Mövcud faylı &saxla (tövsiyə olunur)
ExistingFileNewerOverwriteOrKeepAll=Növbəti toqquşmalarda da &belə et
ErrorChangingAttr=Mövcud faylın atributları dəyişdirilərkən xəta baş verdi:
ErrorCreatingTemp=Hədəf qovluqda fayl yaradılarkən xəta baş verdi:
ErrorReadingSource=Mənbə fayl oxunarkən xəta baş verdi:
ErrorCopying=Fayl kopyalanarkən xəta baş verdi:
ErrorDownloading=Fayl yüklənərkən xəta baş verdi:
ErrorExtracting=Arxiv çıxarılarkən xəta baş verdi:
ErrorReplacingExistingFile=Mövcud fayl əvəz edilərkən xəta baş verdi:
ErrorRestartReplace=RestartReplace uğursuz oldu:
ErrorRenamingTemp=Hədəf qovluqdakı faylın adı dəyişdirilərkən xəta baş verdi:
ErrorRegisterServer=DLL/OCX qeydiyyata alına bilmədi: %1
ErrorRegSvr32Failed=RegSvr32 %1 çıxış kodu ilə uğursuz oldu
ErrorRegisterTypeLib=Tip kitabxanası qeydiyyata alına bilmədi: %1

; *** Uninstall display name markings
; used for example as 'My Program (32-bit)'
UninstallDisplayNameMark=%1 (%2)
; used for example as 'My Program (32-bit, All users)'
UninstallDisplayNameMarks=%1 (%2, %3)
UninstallDisplayNameMark32Bit=32 bit
UninstallDisplayNameMark64Bit=64 bit
UninstallDisplayNameMarkAllUsers=Bütün istifadəçilər
UninstallDisplayNameMarkCurrentUser=Cari istifadəçi

; *** Post-installation errors
ErrorOpeningReadme=README faylı açılarkən xəta baş verdi.
ErrorRestartingComputer=Quraşdırma kompüteri yenidən başlada bilmədi. Zəhmət olmasa, bunu özünüz edin.

; *** Uninstaller messages
UninstallNotFound="%1" faylı mövcud deyil. Silmək mümkün deyil.
UninstallOpenError="%1" faylı açıla bilmədi. Silmək mümkün deyil
UninstallUnsupportedVer="%1" silmə jurnalı faylı silmə proqramının bu versiyasının tanımadığı formatdadır. Silmək mümkün deyil
UninstallUnknownEntry=Silmə jurnalında naməlum qeydə (%1) rast gəlindi
ConfirmUninstall=%1 proqramını və onun bütün komponentlərini tamamilə silmək istədiyinizə əminsiniz?
UninstallOnlyOnWin64=Bu quraşdırma yalnız 64 bitlik Windows-da silinə bilər.
OnlyAdminCanUninstall=Bu quraşdırmanı yalnız administrator hüquqları olan istifadəçi silə bilər.
UninstallStatusLabel=Zəhmət olmasa, %1 kompüterinizdən silinənə qədər gözləyin.
UninstalledAll=%1 kompüterinizdən uğurla silindi.
UninstalledMost=%1 proqramının silinməsi tamamlandı.%n%nBəzi elementlər silinə bilmədi. Onları əl ilə silə bilərsiniz.
UninstalledAndNeedsRestart=%1 proqramının silinməsini tamamlamaq üçün kompüteriniz yenidən başladılmalıdır.%n%nİndi yenidən başlatmaq istəyirsiniz?
UninstallDataCorrupted="%1" faylı zədələnib. Silmək mümkün deyil

; *** Uninstallation phase messages
ConfirmDeleteSharedFileTitle=Ortaq fayl silinsin?
ConfirmDeleteSharedFile2=Sistem aşağıdakı ortaq fayldan artıq heç bir proqramın istifadə etmədiyini bildirir. Silmə proqramının bu ortaq faylı silməsini istəyirsiniz?%n%nHər hansı proqram hələ də bu fayldan istifadə edirsə və fayl silinərsə, həmin proqramlar düzgün işləməyə bilər. Əmin deyilsinizsə, "Xeyr" seçin. Faylın sistemdə qalması heç bir zərər verməz.
SharedFileNameLabel=Fayl adı:
SharedFileLocationLabel=Yeri:
WizardUninstalling=Silmə vəziyyəti
StatusUninstalling=%1 silinir...

; *** Shutdown block reasons
ShutdownBlockReasonInstallingApp=%1 quraşdırılır.
ShutdownBlockReasonUninstallingApp=%1 silinir.

; The custom messages below aren't used by Setup itself, but if you make
; use of them in your scripts, you'll want to translate them.

[CustomMessages]

NameAndVersion=%1 versiya %2
AdditionalIcons=Əlavə qısayollar:
CreateDesktopIcon=İş &masasında qısayol yarat
CreateQuickLaunchIcon=&Sürətli başlatma panelində qısayol yarat
ProgramOnTheWeb=%1 internetdə
UninstallProgram=%1 proqramını sil
LaunchProgram=%1 proqramını işə sal
AssocFileExtension=%1 proqramını %2 fayl uzantısı ilə &əlaqələndir
AssocingFileExtension=%1 proqramı %2 fayl uzantısı ilə əlaqələndirilir...
AutoStartProgramGroupDescription=Avtomatik başlatma:
AutoStartProgram=%1 avtomatik başladılsın
AddonHostProgramNotFound=%1 seçdiyiniz qovluqda tapılmadı.%n%nYenə də davam etmək istəyirsiniz?
