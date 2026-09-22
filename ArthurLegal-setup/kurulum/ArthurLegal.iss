; ArthurLegal kurulum betiği (Inno Setup 6). Bu dosya UTF-8 BOM ile kaydedilmelidir:
; BOM olmazsa Türkçe karakterler bozulur (yayin/derle.py denetler).
; Doğrudan derlenmez; yayin/derle.py tanımları (/D...) vererek ISCC'yi çağırır.

#ifndef Kaynak
  #error "Kaynak tanımlı değil: yayin/derle.py ile derleyin"
#endif
#ifndef FirmaAd
  #define FirmaAd ""
#endif

[Setup]
AppId={{5B7A1E2C-9D4F-4C8B-A6E3-2F1D0C9B8A71}
AppName=ArthurLegal
AppVersion={#Surum}
AppVerName=ArthurLegal {#Surum}
AppPublisher=ArthurLegal
AppPublisherURL=https://github.com/beerbottle90/ArthurLegal
AppSupportURL=https://github.com/beerbottle90/ArthurLegal/issues
VersionInfoVersion={#Surum}
VersionInfoDescription=ArthurLegal Kurulum
DefaultDirName={localappdata}\Programs\ArthurLegal
DefaultGroupName=ArthurLegal
DisableDirPage=yes
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
MinVersion=10.0
OutputDir={#CiktiDizini}
OutputBaseFilename={#CiktiAdi}
LicenseFile={#Kaynak}\LISANS.txt
SetupIconFile={#Kaynak}\bin\arthurlegal.ico
UninstallDisplayIcon={app}\bin\arthurlegal.ico
WizardImageFile={#Varlik}\sihirbaz.png
WizardSmallImageFile={#Varlik}\sihirbaz-kucuk.png
UninstallDisplayName=ArthurLegal
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
ShowLanguageDialog=no
CloseApplications=yes
RestartApplications=no
SetupLogging=yes
#ifdef Imzali
; Windows 11 Akıllı Uygulama Denetimi imzasız kurulum motorunu (.tmp) engeller; imza hem kurulumu hem kaldırıcıyı kapsar.
SignTool=imzaci
SignedUninstaller=yes
#endif

[Languages]
Name: "tr"; MessagesFile: "compiler:Languages\Turkish.isl"

[Messages]
; Inno Setup 6 karşılama sayfasını göstermez; kurulum lisans sayfasıyla açılır. Bilgi "Kurulmaya hazır" sayfasında.
#if FirmaAd != ""
ReadyLabel1=Kurulum, {#FirmaAd} için ArthurLegal'i kurmaya hazır: Hukuk Bürosu ve Kurumsal Asistan paketleri, Arthur Mask, ArthurLegal Tapu ve UYAP bağlantısı.
#else
ReadyLabel1=Kurulum, ArthurLegal'i kurmaya hazır: Hukuk Bürosu ve Kurumsal Asistan paketleri, Arthur Mask, ArthurLegal Tapu ve UYAP bağlantısı.
#endif
ReadyLabel2a=Kur düğmesine tıklayın. Arthur Mask indirilir (yaklaşık 1 GB, birkaç dakika) ve açıksa Claude Desktop kapatılır. Yönetici yetkisi gerekmez; güncellemeler bundan sonra arka planda kendiliğinden kurulur.
ReadyLabel2b=Kur düğmesine tıklayın. Arthur Mask indirilir (yaklaşık 1 GB, birkaç dakika) ve açıksa Claude Desktop kapatılır. Yönetici yetkisi gerekmez; güncellemeler bundan sonra arka planda kendiliğinden kurulur.
FinishedLabel=ArthurLegal kuruldu.%n%nSon adım (bir dakika): açılan başlangıç rehberindeki talimatı kopyalayın ve Claude Desktop'ta yeni bir Proje oluşturup Talimatlar alanına yapıştırın. Bu adım bir kez yapılır; sonraki güncellemeler kendiliğinden gelir.

[Tasks]
Name: "masaustu"; Description: "Masaüstüne kısayol ekle (Tapu, Başlangıç Rehberi)"; GroupDescription: "Kısayollar:"

[Files]
Source: "{#Kaynak}\runtime\*"; DestDir: "{app}\runtime"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#Kaynak}\bin\*"; DestDir: "{app}\bin"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#Kaynak}\surumler\{#Surum}\*"; DestDir: "{app}\surumler\{#Surum}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#Kaynak}\rehber\*"; DestDir: "{app}\rehber"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#Kaynak}\ayar.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#Kaynak}\LISANS.txt"; DestDir: "{app}"; Flags: ignoreversion
#if FirmaAd != ""
Source: "{#Kaynak}\firma\*"; DestDir: "{app}\firma"; Flags: ignoreversion recursesubdirs createallsubdirs
#endif

[Icons]
Name: "{group}\ArthurLegal - Başlangıç Rehberi"; Filename: "{app}\rehber\baslangic.html"; IconFilename: "{app}\bin\ArthurLegal.ico"
Name: "{group}\ArthurLegal - Tapu"; Filename: "{app}\runtime\pythonw.exe"; Parameters: "-B ""{app}\bin\al.py"" kisayol tapu"; WorkingDir: "{app}"; IconFilename: "{app}\bin\ArthurLegal-Tapu.ico"
Name: "{group}\ArthurLegal - UYAP Tarayıcısı"; Filename: "{app}\runtime\python.exe"; Parameters: "-B ""{app}\bin\al.py"" kisayol uyap-tarayici"; WorkingDir: "{app}"; IconFilename: "{app}\bin\ArthurLegal.ico"
Name: "{group}\ArthurLegal - Güncellemeleri Denetle"; Filename: "{app}\runtime\python.exe"; Parameters: "-B ""{app}\bin\al.py"" guncelle"; WorkingDir: "{app}"; IconFilename: "{app}\bin\ArthurLegal.ico"
Name: "{group}\ArthurLegal'i Kaldır"; Filename: "{uninstallexe}"
Name: "{userdesktop}\ArthurLegal - Tapu"; Filename: "{app}\runtime\pythonw.exe"; Parameters: "-B ""{app}\bin\al.py"" kisayol tapu"; WorkingDir: "{app}"; IconFilename: "{app}\bin\ArthurLegal-Tapu.ico"; Tasks: masaustu
Name: "{userdesktop}\ArthurLegal - Başlangıç Rehberi"; Filename: "{app}\rehber\baslangic.html"; IconFilename: "{app}\bin\ArthurLegal.ico"; Tasks: masaustu

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "ArthurLegalGuncelleme"; ValueData: """{app}\runtime\pythonw.exe"" -B ""{app}\bin\al.py"" guncelle --sessiz"; Flags: uninsdeletevalue

[Run]
Filename: "{app}\rehber\baslangic.html"; Description: "Başlangıç rehberini aç (son adım)"; Flags: postinstall shellexec nowait skipifsilent
Filename: "claude://"; Description: "Claude Desktop'u başlat"; Flags: postinstall shellexec nowait skipifsilent

[UninstallRun]
Filename: "{app}\runtime\python.exe"; Parameters: "-B ""{app}\bin\al.py"" kur --kaldir"; Flags: runhidden waituntilterminated; RunOnceId: "ClaudeKaydiniSil"

[UninstallDelete]
Type: filesandordirs; Name: "{app}\surumler"
Type: filesandordirs; Name: "{app}\veri"
Type: files; Name: "{app}\aktif.txt"

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
  IndirmeSayfasi := CreateDownloadPage('Arthur Mask indiriliyor',
    'Müvekkil belgelerini bilgisayarınızda maskeleyen gizlilik kapısı (yaklaşık 1 GB). İnternet hızınıza göre birkaç dakika sürer.',
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
    Result := MsgBox('Arthur Mask indirilemedi (internet bağlantısını denetleyin).' + #13#10#13#10 +
      'ArthurLegal şimdilik Arthur Mask olmadan kurulsun mu? UYAP bağlantısı Arthur Mask ister; ' +
      'Arthur Mask bir sonraki güncelleme denetiminde kendiliğinden yeniden denenir.',
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
    WizardForm.StatusLabel.Caption := 'Arthur Mask kuruluyor (birkaç dakika sürebilir)...';
    if (not Exec(ExpandConstant('{tmp}\ArthurMask-Kurulum.exe'), '/VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP-', '',
                 SW_SHOW, ewWaitUntilTerminated, Sonuc)) or (Sonuc <> 0) then
      Log('Arthur Mask kurulumu başarısız, çıkış kodu ' + IntToStr(Sonuc));
  end;
  WizardForm.StatusLabel.Caption := 'Claude Desktop''a bağlanıyor...';
  Exec(ExpandConstant('{app}\runtime\python.exe'), '-B "' + ExpandConstant('{app}\bin\al.py') + '" kur --kurulum',
       ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, Sonuc);
  if Sonuc <> 0 then
    Log('kur --kurulum çıkış kodu ' + IntToStr(Sonuc));
end;
