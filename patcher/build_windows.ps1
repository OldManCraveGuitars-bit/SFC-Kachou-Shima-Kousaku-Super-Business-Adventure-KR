$ErrorActionPreference = 'Stop'
$releaseRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
Set-Location -LiteralPath $releaseRoot
python -X utf8 -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { throw 'Patcher tests failed' }
$patchSource = (Resolve-Path -LiteralPath 'patches/Kachou_Shima_Kousaku_KR_V0.81.ips').Path
$versionSource = (Resolve-Path -LiteralPath 'patcher/version_info.txt').Path
python -m PyInstaller --noconfirm --onefile --windowed `
    --name 'KachouShimaKRPatcher-V0.81' `
    --distpath dist --workpath build/patcher --specpath build `
    --version-file $versionSource `
    --add-data "$($patchSource):patches" `
    patcher/patcher.py
if ($LASTEXITCODE -ne 0) { throw 'Patcher EXE build failed' }
Get-Item -LiteralPath dist/KachouShimaKRPatcher-V0.81.exe | Select-Object Name,Length
