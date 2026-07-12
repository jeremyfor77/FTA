$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$exts = '*.mp3','*.m4a','*.mp4','*.wav','*.ogg'
$files = @(Get-ChildItem "$dir\*" -File -Include $exts | Select-Object -ExpandProperty Name | Sort-Object)
$items = $files | ForEach-Object { '"' + $_ + '"' }
'{ "tracks": [' + ($items -join ', ') + '] }' | Set-Content -Encoding utf8 "$dir\playlist.json"
Write-Host ("playlist.json updated with " + $files.Count + " song(s):")
$files | ForEach-Object { Write-Host ("  " + $_) }
