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
; Modül ekranı yalnız bu derlemedeki paketleri ve Tapu'yu gösterir (derle.py /DPaketler, /DTapuVar).
#ifndef Paketler
  #define Paketler "hukuk-burosu,kurumsal,adliye,akademisyen"
#endif
#ifndef TapuVar
  #define TapuVar "1"
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
; Modüller kendi sayfalarında seçilir (Kod: ModulSayfasiOlustur); "Kurulmaya hazır" sayfası seçimi listeler.
#if FirmaAd != ""
en.ReadyLabel1={#UrunAd} is ready to install ({#FirmaAd}) with the modules below and the research connector.
tr.ReadyLabel1={#UrunAd} kurulmaya hazır ({#FirmaAd}): aşağıdaki modüller ve araştırma bağlantısı.
#else
en.ReadyLabel1=Setup is ready to install ArthurLegal with the modules below and the research connector.
tr.ReadyLabel1=Kurulum, ArthurLegal'i kurmaya hazır: aşağıdaki modüller ve araştırma bağlantısı.
#endif
en.ReadyLabel2a=Click Install. If you chose Arthur Mask and it is not installed yet, it is downloaded (about 1 GB, a few minutes). Claude Desktop is closed if it is open, so send any message you are typing first. No administrator rights are needed; from now on updates install themselves in the background.
en.ReadyLabel2b=Click Install. If you chose Arthur Mask and it is not installed yet, it is downloaded (about 1 GB, a few minutes). Claude Desktop is closed if it is open, so send any message you are typing first. No administrator rights are needed; from now on updates install themselves in the background.
tr.ReadyLabel2a=Kur düğmesine tıklayın. Arthur Mask'i seçtiyseniz ve bilgisayarda kurulu değilse indirilir (yaklaşık 1 GB, birkaç dakika). Claude Desktop açıksa kapatılır; yazdığınız bir mesaj varsa önce gönderin. Yönetici yetkisi gerekmez; güncellemeler bundan sonra arka planda kendiliğinden kurulur.
tr.ReadyLabel2b=Kur düğmesine tıklayın. Arthur Mask'i seçtiyseniz ve bilgisayarda kurulu değilse indirilir (yaklaşık 1 GB, birkaç dakika). Claude Desktop açıksa kapatılır; yazdığınız bir mesaj varsa önce gönderin. Yönetici yetkisi gerekmez; güncellemeler bundan sonra arka planda kendiliğinden kurulur.
en.FinishedLabel={#UrunAd} is installed.%n%nOpen a new chat in Claude Desktop and type your question; the assistant loads the instructions of the package you chose itself. When Claude asks for permission the first time it uses a tool, choose 'Always allow'.%n%nThe package icons on the desktop ({#UrunAd}, Courthouse, Academician) open Claude Desktop and the start panel. To add or remove modules, run this setup again.
tr.FinishedLabel={#UrunAd} kuruldu.%n%nClaude Desktop'ta yeni bir sohbet açıp sorunuzu doğrudan yazın; asistan seçtiğiniz paketin talimatını kendisi yükler. Claude bir aracı ilk kez kullanırken izin sorarsa 'Always allow' (Her zaman izin ver) seçin; Claude Desktop'un menüleri İngilizcedir.%n%nMasaüstündeki paket simgeleri ({#UrunAd}, Courthouse, Akademisyen) Claude Desktop'u ve başlangıç panelini açar. Modül eklemek ya da çıkarmak için bu kurulumu yeniden çalıştırın.

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
; Modül ekranı. Kısa açıklamalar istemci/kur.py'deki MODUL_METNI ile aynı tutulur (zip kurulumunun sorusu).
en.ModulBaslik=Choose modules
tr.ModulBaslik=Modülleri seçin
en.ModulAciklama=Tick what you want to install. At least one package is needed; run setup again later to change.
tr.ModulAciklama=Kurmak istediklerinizi işaretleyin. En az bir paket gerekir; sonra kurulumu yeniden çalıştırıp değiştirebilirsiniz.
en.ModulPaketler=Assistant packages (choose at least one)
tr.ModulPaketler=Asistan paketleri (en az birini seçin)
en.ModulAraclar=Tools
tr.ModulAraclar=Araçlar
en.ModulHukuk=Law Firm
tr.ModulHukuk=Hukuk Bürosu
en.ModulHukukAciklama=For lawyers: petitions, contracts, case-law and legislation research, deadlines.
tr.ModulHukukAciklama=Avukatlar için dilekçe, sözleşme, içtihat ve mevzuat araştırması, süre takibi.
en.ModulKurumsal=Corporate Assistant
tr.ModulKurumsal=Kurumsal Asistan
en.ModulKurumsalAciklama=For in-house legal teams: contract review, compliance, data protection, company law.
tr.ModulKurumsalAciklama=Şirket hukuk birimleri için sözleşme incelemesi, uyum, KVKK ve şirketler hukuku.
en.ModulAdliye=Courthouse
tr.ModulAdliye=Courthouse
en.ModulAdliyeAciklama=For judges and court clerks: neutral drafts of reasoning, orders, writs and service.
tr.ModulAdliyeAciklama=Hâkim ve kalem için tarafsız taslak: gerekçe iskeleti, tensip, müzekkere, tebligat.
en.ModulAkademisyen=Academician
tr.ModulAkademisyen=Akademisyen
en.ModulAkademisyenAciklama=For legal academics: literature, citation checks, journal choice, publication ethics.
tr.ModulAkademisyenAciklama=Hukuk akademisyenleri için literatür, atıf doğrulama, dergi seçimi, yayın etiği.
en.ModulTapu=ArthurLegal Tapu
tr.ModulTapu=ArthurLegal Tapu
en.ModulTapuAciklama=Live Turkish land-registry parcels (TKGM) by block/parcel or place name, with sketch.
tr.ModulTapuAciklama=Ada/parsel ya da yer adıyla TKGM'den canlı parsel bilgisi, kroki ve harç.
en.ModulMask=Arthur Mask
tr.ModulMask=Arthur Mask
en.ModulMaskAciklama=Masks documents on this computer before Claude sees them; about 1 GB download.
tr.ModulMaskAciklama=Belgeleri Claude'a vermeden önce bu bilgisayarda maskeler; yaklaşık 1 GB indirilir.
en.ModulMaskKurulu=Arthur Mask (already installed)
tr.ModulMaskKurulu=Arthur Mask (bu bilgisayarda kurulu)
en.ModulMaskKuruluAciklama=Installed on this computer; its updates arrive by themselves.
tr.ModulMaskKuruluAciklama=Bu bilgisayarda kurulu; güncellemeleri kendiliğinden gelir.
en.ModulPaketGerekli=Choose at least one package: Law Firm, Corporate Assistant, Courthouse or Academician.
tr.ModulPaketGerekli=En az bir paket seçin: Hukuk Bürosu, Kurumsal Asistan, Courthouse ya da Akademisyen.
en.ModulGecersiz=Invalid /MODULLER value: %1%n%nUse a comma-separated list with at least one package, for example /MODULLER=adliye,tapu,mask. Modules: hukuk-burosu, kurumsal, adliye, akademisyen, tapu, mask.
tr.ModulGecersiz=Geçersiz /MODULLER değeri: %1%n%nEn az bir paket içeren, virgülle ayrılmış bir liste verin, örneğin /MODULLER=adliye,tapu,mask. Modüller: hukuk-burosu, kurumsal, adliye, akademisyen, tapu, mask.
en.ModulOzet=Modules:
tr.ModulOzet=Modüller:

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
const
  MODUL_SAYISI = 6;
  { 2.5.0'dan önceki kurulumların modülleri (ortak.ESKI_SECIM): seçim verilmeyen sessiz kurulum bunlarla sürer. }
  ESKI_SECIM = 'hukuk-burosu,kurumsal,tapu,mask';

var
  IndirmeSayfasi: TDownloadWizardPage;
  MaskIndirildi: Boolean;
  ModulSayfasi: TWizardPage;
  ModulKutusu: array[0..5] of TNewCheckBox;
  { Seçilen modüller, virgüllü ve ortak.MODULLER sırasıyla (ör. "adliye,tapu,mask"). kur.py'ye --moduller ile geçer;
    önceki veri olarak saklanır, kurulum yeniden açılınca işaretli gelir. }
  Secim: String;

function MaskKurulu: Boolean;
begin
  Result := FileExists(ExpandConstant('{localappdata}\Programs\Arthur Mask\runtime\python.exe'));
end;

function IndirmeIlerlemesi(const Url, DosyaAdi: String; const Ilerleme, Toplam: Int64): Boolean;
begin
  Result := True;
end;

{ Modüller ortak.MODULLER sırasıyla: dört paket, sonra Tapu ve Arthur Mask. }
function ModulKodu(I: Integer): String;
begin
  case I of
    0: Result := 'hukuk-burosu';
    1: Result := 'kurumsal';
    2: Result := 'adliye';
    3: Result := 'akademisyen';
    4: Result := 'tapu';
  else
    Result := 'mask';
  end;
end;

function ModulIletisi(I: Integer): String;
begin
  case I of
    0: Result := 'ModulHukuk';
    1: Result := 'ModulKurumsal';
    2: Result := 'ModulAdliye';
    3: Result := 'ModulAkademisyen';
    4: Result := 'ModulTapu';
  else
    Result := 'ModulMask';
  end;
end;

function ListedeVar(const Liste, Kod: String): Boolean;
begin
  Result := Pos(',' + Kod + ',', ',' + Liste + ',') > 0;
end;

function DerlemedeVar(I: Integer): Boolean;
begin
  if I <= 3 then
    Result := ListedeVar('{#Paketler}', ModulKodu(I))
  else if I = 4 then
    Result := '{#TapuVar}' = '1'
  else
    Result := True;
end;

function PaketVar(const Liste: String): Boolean;
var
  I: Integer;
begin
  Result := False;
  for I := 0 to 3 do
    if ListedeVar(Liste, ModulKodu(I)) then
      Result := True;
end;

{ "Adliye, tapu;mask" gibi bir listeyi doğrular ve sıraya koyar. Bilinmeyen ad, bu derlemede olmayan modül ya da
  hiç paket yoksa False: kurulum yanlış bir seçimle sessizce sürmez (kur.py de aynı denetimi yapar). }
function SecimiDogrula(const Ham: String; var Temiz: String): Boolean;
var
  Liste, Artan: String;
  I: Integer;
begin
  Liste := Lowercase(Ham);
  StringChangeEx(Liste, ' ', '', True);
  StringChangeEx(Liste, ';', ',', True);
  Artan := ',' + Liste + ',';
  Temiz := '';
  Result := True;
  for I := 0 to MODUL_SAYISI - 1 do
    if ListedeVar(Liste, ModulKodu(I)) then
    begin
      if not DerlemedeVar(I) then
        Result := False;
      if Temiz <> '' then
        Temiz := Temiz + ',';
      Temiz := Temiz + ModulKodu(I);
      while Pos(',' + ModulKodu(I) + ',', Artan) > 0 do
        StringChangeEx(Artan, ',' + ModulKodu(I) + ',', ',', True);
    end;
  StringChangeEx(Artan, ',', '', True);
  Result := Result and (Artan = '') and PaketVar(Temiz);
end;

{ BT'nin sessiz dağıtımı için: ArthurLegal-Kurulum.exe /VERYSILENT /MODULLER=adliye,tapu,mask }
function InitializeSetup: Boolean;
var
  Param, Temiz: String;
begin
  Result := True;
  Param := ExpandConstant('{param:MODULLER|}');
  if Param = '' then
    exit;
  if SecimiDogrula(Param, Temiz) then
    Secim := Temiz
  else
  begin
    Log('Geçersiz /MODULLER: ' + Param);
    SuppressibleMsgBox(FmtMessage(CustomMessage('ModulGecersiz'), [Param]), mbCriticalError, MB_OK, IDOK);
    Result := False;
  end;
end;

procedure AciklamaTiklandi(Sender: TObject);
var
  I: Integer;
begin
  I := TNewStaticText(Sender).Tag;
  if (ModulKutusu[I] <> nil) and ModulKutusu[I].Enabled then
    ModulKutusu[I].Checked := not ModulKutusu[I].Checked;
end;

{ Lisanstan sonraki sayfa: her modül bir onay kutusu (kalın) ve altında kısa açıklama (gri). Açıklamaya tıklamak da
  kutuyu işaretler. Kurulu Arthur Mask işaretli ve kilitli görünür: kaldırmak bu kurulumun işi değildir. }
procedure ModulSayfasiOlustur;
var
  I, Ust, Girinti: Integer;
  PaketBasligi, AracBasligi: Boolean;
  Baslik, Aciklama: TNewStaticText;
  Kutu: TNewCheckBox;
begin
  ModulSayfasi := CreateCustomPage(wpLicense, CustomMessage('ModulBaslik'), CustomMessage('ModulAciklama'));
  Ust := 0;
  Girinti := ScaleX(18);
  PaketBasligi := False;
  AracBasligi := False;
  for I := 0 to MODUL_SAYISI - 1 do
  begin
    if not DerlemedeVar(I) then
      continue;
    if ((I <= 3) and not PaketBasligi) or ((I >= 4) and not AracBasligi) then
    begin
      if Ust > 0 then
        Ust := Ust + ScaleY(2);
      Baslik := TNewStaticText.Create(ModulSayfasi);
      Baslik.Parent := ModulSayfasi.Surface;
      Baslik.Left := 0;
      Baslik.Top := Ust;
      if I <= 3 then
      begin
        Baslik.Caption := CustomMessage('ModulPaketler');
        PaketBasligi := True;
      end
      else
      begin
        Baslik.Caption := CustomMessage('ModulAraclar');
        AracBasligi := True;
      end;
      Ust := Ust + Baslik.Height + ScaleY(4);
    end;
    Kutu := TNewCheckBox.Create(ModulSayfasi);
    Kutu.Parent := ModulSayfasi.Surface;
    Kutu.Left := 0;
    Kutu.Top := Ust;
    Kutu.Width := ModulSayfasi.SurfaceWidth;
    Kutu.Height := ScaleY(17);
    Kutu.Font.Style := [fsBold];
    Kutu.Caption := CustomMessage(ModulIletisi(I));
    Kutu.Checked := ListedeVar(Secim, ModulKodu(I));
    ModulKutusu[I] := Kutu;
    Aciklama := TNewStaticText.Create(ModulSayfasi);
    Aciklama.Parent := ModulSayfasi.Surface;
    Aciklama.Left := Girinti;
    Aciklama.Top := Ust + Kutu.Height;
    Aciklama.Width := ModulSayfasi.SurfaceWidth - Girinti;
    Aciklama.AutoSize := False;
    Aciklama.WordWrap := True;
    Aciklama.Font.Color := clGrayText;
    Aciklama.Tag := I;
    Aciklama.OnClick := @AciklamaTiklandi;
    Aciklama.Caption := CustomMessage(ModulIletisi(I) + 'Aciklama');
    if (I = 5) and MaskKurulu then
    begin
      Kutu.Caption := CustomMessage('ModulMaskKurulu');
      Aciklama.Caption := CustomMessage('ModulMaskKuruluAciklama');
      Kutu.Checked := True;
      Kutu.Enabled := False;
    end;
    Aciklama.AdjustHeight;
    Ust := Aciklama.Top + Aciklama.Height + ScaleY(5);
  end;
  Log(Format('Modül sayfası: içerik %d, yüzey %d piksel yüksekliğinde', [Ust, ModulSayfasi.SurfaceHeight]));
end;

procedure InitializeWizard;
var
  Temiz: String;
begin
  { /MODULLER verilmediyse önceki kurulumun seçimi işaretli gelir. İlk kurulumda hiçbir kutu işaretli değildir;
    yalnız seçimsiz sessiz kurulum 2.5.0 öncesinin modülleriyle sürer. }
  if Secim = '' then
  begin
    if SecimiDogrula(GetPreviousData('Moduller', ''), Temiz) then
      Secim := Temiz
    else if WizardSilent then
      Secim := ESKI_SECIM;
  end;
  ModulSayfasiOlustur;
  IndirmeSayfasi := CreateDownloadPage(CustomMessage('MaskIndiriliyor'), CustomMessage('MaskAciklama'),
    @IndirmeIlerlemesi);
end;

procedure RegisterPreviousData(PreviousDataKey: Integer);
begin
  SetPreviousData(PreviousDataKey, 'Moduller', Secim);
end;

function UpdateReadyMemo(Space, NewLine, MemoUserInfoInfo, MemoDirInfo, MemoTypeInfo, MemoComponentsInfo,
  MemoGroupInfo, MemoTasksInfo: String): String;
var
  I: Integer;
begin
  Result := CustomMessage('ModulOzet');
  for I := 0 to MODUL_SAYISI - 1 do
    if ListedeVar(Secim, ModulKodu(I)) then
      Result := Result + NewLine + Space + CustomMessage(ModulIletisi(I));
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
var
  I: Integer;
  Liste: String;
begin
  Result := True;
  if CurPageID = ModulSayfasi.ID then
  begin
    Liste := '';
    for I := 0 to MODUL_SAYISI - 1 do
      if (ModulKutusu[I] <> nil) and ModulKutusu[I].Checked then
      begin
        if Liste <> '' then
          Liste := Liste + ',';
        Liste := Liste + ModulKodu(I);
      end;
    if not PaketVar(Liste) then
    begin
      MsgBox(CustomMessage('ModulPaketGerekli'), mbError, MB_OK);
      Result := False;
      exit;
    end;
    Secim := Liste;
  end;
  if (CurPageID = wpReady) and (not WizardSilent) and ListedeVar(Secim, 'mask') and (not MaskIndir(False)) then
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
  if WizardSilent and ListedeVar(Secim, 'mask') then
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
    --dil: kurulumda seçilen dil (en/tr); kısayol adları ve başlangıç rehberi bu dilde yazılır.
    --moduller: modül ekranındaki seçim; kur.py moduller.json'a yazar, kısayollar ve Claude kaydı ona göre olur. }
  DeleteFile(ExpandConstant('{app}\aktif.txt'));
  Exec(ExpandConstant('{app}\runtime\python.exe'), '-B "' + ExpandConstant('{app}\bin\al.py') + '" kur --kurulum --kisayol --dil ' +
       ActiveLanguage + ' --moduller ' + Secim, ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, Sonuc);
  if Sonuc <> 0 then
    Log('kur --kurulum çıkış kodu ' + IntToStr(Sonuc));
end;
