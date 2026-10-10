$p='C:\ProgramData\XLN Audio\XLN Online Installer\App\config.txt'
$s=[IO.File]::ReadAllText($p)
$s=$s -replace 'vst3,"C:\\Program Files\\Common Files\\VST3\\XLN Audio\\"','vst3,"C:\Program Files\Common Files\VST3\"'
[IO.File]::WriteAllText($p,$s)
