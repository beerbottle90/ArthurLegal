; ArthurLegal kurulum betiği (Inno Setup 6). Bu dosya UTF-8 BOM ile kaydedilmelidir:
; BOM olmazsa Türkçe karakterler bozulur (yayin/derle.py denetler).
; Doğrudan derlenmez; yayin/derle.py tanımları (/D...) vererek ISCC'yi çağırır.
; Kurulum iki dillidir (İngilizce ve Türkçe): açılışta dil sorulur, Windows'un diline uyan dil seçili gelir.
; Seçilen dil kur.py'ye --dil ile geçer; kısayol adları ve başlangıç rehberi aynı dilde yazılır.

#ifndef Kaynak
  #error "Kaynak tanımlı değil: yayin/derle.py ile derleyin"
#endif
#ifndef FirmaAd
  #define FirmaAd ""
#endif
; Büroya özel kurulumda ürün adı ve simge büronun markasından gelir (derle.py, ortak.urun_adi):
; programlar listesi, Başlat menüsü ve kaldırma kısayolu bu adı taşır. Kurulum klasörü değişmez.
#ifndef UrunAd
  #define UrunAd "ArthurLegal"
#endif
#ifndef Simge
  #define Simge "arthurlegal.ico"
#endif
; kur.py'deki _kaldir_adi ile aynı olmalı (iki dil).
#if UrunAd == "ArthurLegal"
  #define KaldirAdiTr "ArthurLegal'i Kaldır"
  #define KaldirAdiEn "Uninstall ArthurLegal"
#else
  #define KaldirAdiTr UrunAd + " - Kaldır"
  #define KaldirAdiEn UrunAd + " - Uninstall"
#endif

[Setup]
AppId={{5B7A1E2C-9D4F-4C8B-A6E3-2F1D0C9B8A71}
AppName={#UrunAd}
AppVersion={#Surum}
AppVerName={#UrunAd} {#Surum}
AppPublisher=ArthurLegal
AppPublisherURL=https://github.com/beerbottle90/ArthurLegal
AppSupportURL=https://github.com/beerbottle90/ArthurLegal/issues
VersionInfoVersion={#Surum}
VersionInfoDescription={#UrunAd} Setup
DefaultDirName={localappdata}\Programs\ArthurLegal
DefaultGroupName={#UrunAd}
; Üzerine kurulumda Başlat menüsü klasörü önceki kurulumdan değil ürün adından gelir (kur.py ile aynı).
UsePreviousGroup=no
DisableDirPage=yes
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
MinVersion=10.0
OutputDir={#CiktiDizini}
OutputBaseFilename={#CiktiAdi}
SetupIconFile={#Kaynak}\bin\{#Simge}
UninstallDisplayIcon={app}\bin\{#Simge}
WizardImageFile={#Varlik}\sihirbaz.png
WizardSmallImageFile={#Varlik}\sihirbaz-kucuk.png
UninstallDisplayName={#UrunAd} {#Surum}
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
; Dil her kurulumda sorulur; Windows'un arayüz diline uyan dil seçili gelir, uymuyorsa ilk dil (İngilizce).
ShowLanguageDialog=yes
LanguageDetectionMethod=uilanguage
CloseApplications=yes
RestartApplications=no
SetupLogging=yes
#ifdef Imzali
; Windows 11 Akıllı Uygulama Denetimi imzasız kurulum motorunu (.tmp) engeller; imza hem kurulumu hem kaldırıcıyı kapsar.
; Bulut imzalama (Certum SimplySign, SSL.com eSigner) hız sınırlıdır: yeniden deneme ve bekleme olmadan derleme yarıda düşer.
SignTool=imzaci
SignedUninstaller=yes
SignToolRetryCount=3
SignToolMinimumTimeBetween=2000
#endif

[Languages]
; Lisans sayfası dile göre: önsöz o dilde, lisans metinleri ikisinde de İngilizce asıllarıdır (derle.py lisans_yaz).
Name: "en"; MessagesFile: "compiler:Default.isl"; LicenseFile: "{#Kaynak}\LICENSE.txt"
Name: "tr"; MessagesFile: "compiler:Languages\Turkish.isl"; LicenseFile: "{#Kaynak}\LISANS.txt"

[Messages]
; Inno Setup 6 karşılama sayfasını göstermez; kurulum lisans sayfasıyla açılır. Bilgi "Kurulmaya hazır" sayfasında.
#if FirmaAd != ""
en.ReadyLabel1={#UrunAd} is ready to install ({#FirmaAd}): the Law Firm and Corporate Assistant packages, the research connector, ArthurLegal Tapu and Arthur Mask.
tr.ReadyLabel1={#UrunAd} kurulmaya hazır ({#FirmaAd}): Hukuk Bürosu ve Kurumsal Asistan paketleri, araştırma bağlantısı, ArthurLegal Tapu ve Arthur Mask.
#else
en.ReadyLabel1=Setup is ready to install ArthurLegal: the Law Firm and Corporate Assistant packages, the research connector, ArthurLegal Tapu and Arthur Mask.
tr.ReadyLabel1=Kurulum, ArthurLegal'i kurmaya hazır: Hukuk Bürosu ve Kurumsal Asistan paketleri, araştırma bağlantısı, ArthurLegal Tapu ve Arthur Mask.
#endif
en.ReadyLabel2a=Click Install. If Arthur Mask is not installed yet, it is downloaded (about 1 GB, a few minutes). Claude Desktop is closed if it is open, so send any message you are typing first. No administrator rights are needed; from now on updates install themselves in the background.
en.ReadyLabel2b=Click Install. If Arthur Mask is not installed yet, it is downloaded (about 1 GB, a few minutes). Claude Desktop is closed if it is open, so send any message you are typing first. No administrator rights are needed; from now on updates install themselves in the background.
tr.ReadyLabel2a=Kur düğmesine tıklayın. Arthur Mask kurulu değilse indirilir (yaklaşık 1 GB, birkaç dakika). Claude Desktop açıksa kapatılır; yazdığınız bir mesaj varsa önce gönderin. Yönetici yetkisi gerekmez; güncellemeler bundan sonra arka planda kendiliğinden kurulur.
tr.ReadyLabel2b=Kur düğmesine tıklayın. Arthur Mask kurulu değilse indirilir (yaklaşık 1 GB, birkaç dakika). Claude Desktop açıksa kapatılır; yazdığınız bir mesaj varsa önce gönderin. Yönetici yetkisi gerekmez; güncellemeler bundan sonra arka planda kendiliğinden kurulur.
en.FinishedLabel={#UrunAd} is installed.%n%nOpen a new chat in Claude Desktop and type your legal question; the assistant loads the ArthurLegal instructions itself. When Claude asks for permission the first time it uses a tool, choose 'Always allow'.%n%nThe {#UrunAd} icon on the desktop opens Claude Desktop and the start panel.
tr.FinishedLabel={#UrunAd} kuruldu.%n%nClaude Desktop'ta yeni bir sohbet açıp hukuki sorunuzu doğrudan yazın; asistan ArthurLegal talimatını kendisi yükler. Claude bir aracı ilk kez kullanırken izin sorarsa 'Always allow' (Her zaman izin ver) seçin; Claude Desktop'un menüleri İngilizcedir.%n%nMasaüstündeki {#UrunAd} simgesi Claude Desktop'u ve başlangıç panelini açar.

[CustomMessages]
en.KaldirAdi={#KaldirAdiEn}
tr.KaldirAdi={#KaldirAdiTr}
en.RehberDosyasi=baslangic-en.html
tr.RehberDosyasi=baslangic.html
en.RehberAc=Open the start guide (last step)
tr.RehberAc=Başlangıç rehberini aç (son adım)
en.ClaudeBaslat=Start Claude Desktop
tr.ClaudeBaslat=Claude Desktop'u başlat
en.MaskIndiriliyor=Downloading Arthur Mask
tr.MaskIndiriliyor=Arthur Mask indiriliyor
en.MaskAciklama=The privacy gate that masks client documents on your computer (about 1 GB). It takes a few minutes, depending on your connection.
tr.MaskAciklama=Müvekkil belgelerini bilgisayarınızda maskeleyen gizlilik kapısı (yaklaşık 1 GB). İnternet hızınıza göre birkaç dakika sürer.
en.MaskIndirilmedi=Arthur Mask could not be downloaded, or the download was stopped.
tr.MaskIndirilmedi=Arthur Mask indirilemedi ya da indirme durduruldu.
en.MaskOlmadanKur=Install ArthurLegal without Arthur Mask for now? The UYAP bridge needs Arthur Mask; Arthur Mask is downloaded again in the background at the next update check.
tr.MaskOlmadanKur=ArthurLegal şimdilik Arthur Mask olmadan kurulsun mu? UYAP bağlantısı Arthur Mask ister; Arthur Mask bir sonraki güncelleme denetiminde arka planda yeniden indirilir.
en.MaskKuruluyor=Installing Arthur Mask (this may take a few minutes)...
tr.MaskKuruluyor=Arthur Mask kuruluyor (birkaç dakika sürebilir)...
en.ClaudeBaglaniyor=Connecting to Claude Desktop...
tr.ClaudeBaglaniyor=Claude Desktop'a bağlanıyor...

[Files]
Source: "{#Kaynak}\runtime\*"; DestDir: "{app}\runtime"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#Kaynak}\bin\*"; DestDir: "{app}\bin"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#Kaynak}\surumler\{#Surum}\*"; DestDir: "{app}\surumler\{#Surum}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#Kaynak}\rehber\*"; DestDir: "{app}\rehber"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#Kaynak}\ayar.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#Kaynak}\LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#Kaynak}\LISANS.txt"; DestDir: "{app}"; Flags: ignoreversion
#if FirmaAd != ""
Source: "{#Kaynak}\firma\*"; DestDir: "{app}\firma"; Flags: ignoreversion recursesubdirs createallsubdirs
#endif

[Icons]
; Kısayolları kur.py yazar (zip yolu da aynısını yazsın diye): ana ArthurLegal simgesi, Tapu, rehber,
; knowledge klasörü, güncelleme denetimi. Burada yalnız kaldırma girdisi kalır.
Name: "{group}\{cm:KaldirAdi}"; Filename: "{uninstallexe}"

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "ArthurLegalGuncelleme"; ValueData: """{app}\runtime\pythonw.exe"" -B ""{app}\bin\al.py"" guncelle --sessiz"; Flags: uninsdeletevalue

[Run]
Filename: "{app}\rehber\{cm:RehberDosyasi}"; Description: "{cm:RehberAc}"; Flags: postinstall shellexec nowait skipifsilent
Filename: "claude://"; Description: "{cm:ClaudeBaslat}"; Flags: postinstall shellexec nowait skipifsilent

[UninstallRun]
Filename: "{app}\runtime\python.exe"; Parameters: "-B ""{app}\bin\al.py"" kur --kaldir"; Flags: runhidden waituntilterminated; RunOnceId: "ClaudeKaydiniSil"

[UninstallDelete]
; Kurulumdan sonra yazılanlar (güncellemeyle gelen sürüm klasörleri, durum.js, KALDIR.cmd, günlükler)
; Inno'nun dosya listesinde yok; klasör tümüyle silinir. Klasör yalnız ArthurLegal'e aittir.
Type: filesandordirs; Name: "{app}"

[Code]
var
  IndirmeSayfasi: TDownloadWizardPage;
  MaskIndirildi: Boolean;

function MaskKurulu: Boolean;
begin
  Result := FileExists(ExpandConstant('{localappdata}\Programs\Arthur Mask\runtime\python.exe'));
end;

function IndirmeIlerlemesi(const Url, DosyaAdi: String; const Ilerleme, Toplam: Int64): Boolean;
begin
  Result := True;
end;

procedure InitializeWizard;
begin
  IndirmeSayfasi := CreateDownloadPage(CustomMessage('MaskIndiriliyor'), CustomMessage('MaskAciklama'),
    @IndirmeIlerlemesi);
end;

function MaskIndir(Sessiz: Boolean): Boolean;
begin
  Result := MaskKurulu;
  if Result then
    exit;
  if Sessiz then
  begin
    try
      DownloadTemporaryFile('{#MaskUrl}', 'ArthurMask-Kurulum.exe', '{#MaskSha}', nil);
      MaskIndirildi := True;
      Result := True;
    except
      Log('Arthur Mask indirilemedi: ' + GetExceptionMessage);
    end;
    exit;
  end;
  IndirmeSayfasi.Clear;
  IndirmeSayfasi.Add('{#MaskUrl}', 'ArthurMask-Kurulum.exe', '{#MaskSha}');
  IndirmeSayfasi.Show;
  try
    try
      IndirmeSayfasi.Download;
      MaskIndirildi := True;
      Result := True;
    except
      if not IndirmeSayfasi.AbortedByUser then
        Log('Arthur Mask indirilemedi: ' + GetExceptionMessage);
    end;
  finally
    IndirmeSayfasi.Hide;
  end;
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
  Result := True;
  if (CurPageID = wpReady) and (not WizardSilent) and (not MaskIndir(False)) then
    Result := MsgBox(CustomMessage('MaskIndirilmedi') + #13#10#13#10 + CustomMessage('MaskOlmadanKur'),
      mbConfirmation, MB_YESNO) = IDYES;
end;

{ Yalnız Claude Desktop kapatılır. Claude Code'un Windows ikili dosyası da claude.exe'dir;
  görüntü adıyla (taskkill /IM) kapatmak açık Claude Code oturumlarını da öldürür. Süreç yoluna
  bakılır: klasik kurulum %LOCALAPPDATA%\AnthropicClaude, MSIX WindowsApps\Claude_*. }
procedure ClaudeKapat;
var
  Sonuc: Integer;
begin
  Exec(ExpandConstant('{sys}\WindowsPowerShell\v1.0\powershell.exe'),
    '-NoProfile -ExecutionPolicy Bypass -Command "$d = @(Get-Process claude -ErrorAction SilentlyContinue | ' +
    'Where-Object { $_.Path -match ''AnthropicClaude|WindowsApps\\Claude_'' }); ' +
    '$d | ForEach-Object { [void]$_.CloseMainWindow() }; if ($d.Count) { Start-Sleep -Seconds 3 }; ' +
    '$d | Where-Object { -not $_.HasExited } | Stop-Process -Force -ErrorAction SilentlyContinue"',
    '', SW_HIDE, ewWaitUntilTerminated, Sonuc);
end;

function PrepareToInstall(var NeedsRestart: Boolean): String;
begin
  Result := '';
  if WizardSilent then
    MaskIndir(True);
  ClaudeKapat;
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  Sonuc: Integer;
begin
  if CurStep <> ssPostInstall then
    exit;
  if MaskIndirildi then
  begin
    WizardForm.StatusLabel.Caption := CustomMessage('MaskKuruluyor');
    if (not Exec(ExpandConstant('{tmp}\ArthurMask-Kurulum.exe'), '/VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP-', '',
                 SW_SHOW, ewWaitUntilTerminated, Sonuc)) or (Sonuc <> 0) then
      Log('Arthur Mask kurulumu başarısız, çıkış kodu ' + IntToStr(Sonuc));
  end;
  WizardForm.StatusLabel.Caption := CustomMessage('ClaudeBaglaniyor');
  { al.py aktif.txt'deki sürümü seçer; üzerine kurulumda o hâlâ önceki sürümdür ve kısayollar önceki sürümün
    koduyla (eski adlarla) yazılırdı. aktif.txt yoksa al.py en yeni sürümü seçer, kur.py onu yeniden yazar;
    eski bir kurulum dosyası daha yeni bir sürümün üzerine çalışsa da en yeni sürüm kalır. kur.py doğrudan
    çalıştırılamaz: gömülü Python betiğin klasörünü sys.path'e eklemez (al.py bunun için vardır).
    --dil: kurulumda seçilen dil (en/tr); kısayol adları ve başlangıç rehberi bu dilde yazılır. }
  DeleteFile(ExpandConstant('{app}\aktif.txt'));
  Exec(ExpandConstant('{app}\runtime\python.exe'), '-B "' + ExpandConstant('{app}\bin\al.py') + '" kur --kurulum --kisayol --dil ' +
       ActiveLanguage, ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, Sonuc);
  if Sonuc <> 0 then
    Log('kur --kurulum çıkış kodu ' + IntToStr(Sonuc));
end;
