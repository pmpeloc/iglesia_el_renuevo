$P='C:\Users\pmpel\OneDrive\Documentos\Addictive Drums 2\00100'
$prev=''; $prevProcs=''
$end=(Get-Date).AddMinutes(25)
while((Get-Date) -lt $end){
  $cur=(Get-ChildItem $P -Filter '*.AD2Preset' | Sort-Object Name | ForEach-Object { "$($_.Name)|$($_.Length)|$($_.LastWriteTime.ToString('HH:mm:ss'))" }) -join ';'
  $procs=(Get-Process | Where-Object { $_.ProcessName -match 'OneDrive|XLN|Addictive|reaper|Explorer|FileCoAuth|Backup|Drive' } | Sort-Object ProcessName | ForEach-Object { "$($_.ProcessName):$($_.Id)" }) -join ','
  if($cur -ne $prev){ "$(Get-Date -f HH:mm:ss.fff) FILES: $cur"; $prev=$cur }
  if($procs -ne $prevProcs){ "$(Get-Date -f HH:mm:ss.fff) PROCS: $procs"; $prevProcs=$procs }
  Start-Sleep -Milliseconds 500
}
