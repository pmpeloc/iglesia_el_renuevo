param([int]$minutes=30)
$code = @"
using System; using System.Runtime.InteropServices; using System.Text; using System.Collections.Generic;
public class W {
 [DllImport("user32.dll")] public static extern IntPtr FindWindowEx(IntPtr p, IntPtr c, string cls, string t);
 [DllImport("user32.dll")] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
 [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc f, IntPtr l);
 [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
 [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
 public delegate bool EnumProc(IntPtr h, IntPtr l);
 public static List<KeyValuePair<IntPtr,string>> Wins(){ var r=new List<KeyValuePair<IntPtr,string>>(); EnumWindows((h,l)=>{ if(IsWindowVisible(h)){var sb=new StringBuilder(256); GetWindowText(h,sb,256); if(sb.Length>0) r.Add(new KeyValuePair<IntPtr,string>(h,sb.ToString()));} return true;},IntPtr.Zero); return r;}
 public static bool Click(IntPtr h, string btn){ var b=FindWindowEx(h,IntPtr.Zero,"Button",btn); if(b==IntPtr.Zero) return false; SendMessage(b,0x00F5,IntPtr.Zero,IntPtr.Zero); return true; }
}
"@
Add-Type -TypeDefinition $code
$log="$PSScriptRoot\dismiss.log"
$end=(Get-Date).AddMinutes($minutes)
while((Get-Date) -lt $end){
  foreach($w in [W]::Wins()){
    $t=$w.Value
    if($t -eq "Addictive Drums 2"){ if([W]::Click($w.Key,"Aceptar")){ Add-Content $log "$(Get-Date -f HH:mm:ss) clicked Aceptar on AD2 dialog" } }
    elseif($t -eq "Render Warning"){ if([W]::Click($w.Key,"Overwrite files")){ Add-Content $log "$(Get-Date -f HH:mm:ss) clicked Overwrite on Render Warning" } }
    elseif($t -eq "Render Error"){ if([W]::Click($w.Key,"Aceptar")){ Add-Content $log "$(Get-Date -f HH:mm:ss) clicked Aceptar on Render Error" } }`n    elseif($t -like "Error opening devices*"){ if([W]::Click($w.Key,"Close")){ Add-Content $log "$(Get-Date -f HH:mm:ss) clicked Close on MIDI dialog" } }
  }
  Start-Sleep -Milliseconds 700
}


