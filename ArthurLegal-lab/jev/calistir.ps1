# Jev pilotlari - tek komut.
#
#   .\calistir.ps1              her seyi calistirir (anahtar varsa gercek Jev)
#   .\calistir.ps1 -Sahte       anahtar varsa bile cevrimdisi
#
# Anahtar: .env dosyasi varsa okunur. Yoksa SahteJev'e duser, hata vermez.
#
# NOT: Bu dosya bilerek saf ASCII tutulmustur. Windows PowerShell 5.1 BOM'suz
# betikleri ANSI okur; Turkce karakterler ve uzun tire parse hatasi verir.
# Turkce ciktinin tamami Python tarafindan (UTF-8) basilir.

param([switch]$Sahte)

$ErrorActionPreference = "Stop"
$kok = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $kok

# .env oku - KEY=value satirlari, # yorum.
$env_dosyasi = Join-Path $kok ".env"
if (Test-Path $env_dosyasi) {
    Get-Content $env_dosyasi -Encoding utf8 | ForEach-Object {
        $satir = $_.Trim()
        if ($satir -and -not $satir.StartsWith("#") -and $satir.Contains("=")) {
            $parca = $satir.Split("=", 2)
            [Environment]::SetEnvironmentVariable($parca[0].Trim(), $parca[1].Trim(), "Process")
        }
    }
    Write-Host ".env okundu." -ForegroundColor DarkGray
}

$bayrak = @()
if ($Sahte) { $bayrak = @("--sahte") }

$anahtar_var = $env:JEV_API_KEY -or $env:OPENROUTER_API_KEY
if ($anahtar_var -and -not $Sahte) {
    Write-Host "Anahtar bulundu: GERCEK Jev ucuna istek atilacak." -ForegroundColor Yellow
} else {
    Write-Host "Anahtar yok veya -Sahte verildi: cevrimdisi calisilacak." -ForegroundColor DarkGray
}

Write-Host ""
Write-Host "=== TESTLER ===" -ForegroundColor Cyan
python -m pytest tests/ -q
if (-not $?) {
    Write-Host "Testler dustu. Pilotlar calistirilmadi." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== PILOT B (Resmi Gazete on eleme) ===" -ForegroundColor Cyan
python pilot_b_fihrist.py @bayrak --tarama

Write-Host ""
Write-Host "=== PILOT C (maskeleme denetcisi) ===" -ForegroundColor Cyan
python pilot_c_maske.py @bayrak
$c = $LASTEXITCODE
if ($c -eq 1) {
    Write-Host "Pilot C: denetci sizinti kacirdi. KACANLAR listesine bakin." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Bitti." -ForegroundColor Green
